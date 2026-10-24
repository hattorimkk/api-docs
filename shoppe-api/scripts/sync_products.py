"""
Script Trích Xuất Dữ Liệu Danh Mục Sản Phẩm (Sync Products & Variations)
========================================================================
Hỗ trợ:
- Lấy toàn bộ danh sách sản phẩm theo trạng thái (NORMAL, BANNED, UNLIST)
- Batching 50 sản phẩm/lần lấy thông tin chi tiết get_item_base_info
- Tự động phát hiện sản phẩm có biến thể để gọi get_model_list lấy SKU, giá, tồn kho
- Xuất dữ liệu sạch ra file JSON và CSV
"""

import os
import time
import json
import csv
from typing import List, Dict, Any

from shopee_client import ShopeeClient


def sync_all_products(
    client: ShopeeClient,
    item_status: str = "NORMAL",
    output_dir: str = "./data",
) -> List[Dict[str, Any]]:
    """
    Trích xuất toàn bộ sản phẩm của gian hàng bao gồm thông tin chi tiết và biến thể.
    """
    os.makedirs(output_dir, exist_ok=True)
    all_item_ids = []
    offset = 0
    page_size = 100
    has_more = True

    print(f"\n[INFO] Đang quét danh sách mã sản phẩm (status: {item_status})...")

    while has_more:
        res = client.get_item_list(
            offset=offset,
            page_size=page_size,
            item_status=item_status
        )

        if res.get("error"):
            print(f"[ERROR] get_item_list thất bại: {res.get('message')}")
            break

        response_data = res.get("response", {})
        item_list = response_data.get("item", [])
        for it in item_list:
            all_item_ids.append(it.get("item_id"))

        has_more = response_data.get("has_next_page", False)
        offset = response_data.get("next_offset", offset + page_size)
        print(f" -> Lấy được {len(item_list)} sản phẩm (Tổng: {len(all_item_ids)} sản phẩm)")
        time.sleep(0.2)

    print(f"[INFO] Bắt đầu lấy chi tiết thông tin cho {len(all_item_ids)} sản phẩm...")
    full_products = []

    # Batching 50 item mỗi lần gọi get_item_base_info
    for i in range(0, len(all_item_ids), 50):
        chunk = all_item_ids[i : i + 50]
        base_res = client.get_item_base_info(item_id_list=chunk)
        if base_res.get("error"):
            print(f"[ERROR] get_item_base_info thất bại: {base_res.get('message')}")
            continue

        items = base_res.get("response", {}).get("item_list", [])
        for item in items:
            item_id = item.get("item_id")
            has_model = item.get("has_model", False)

            # Nếu sản phẩm có phân loại biến thể, lấy thêm model_list
            models = []
            if has_model:
                model_res = client.get_model_list(item_id=item_id)
                if not model_res.get("error"):
                    models = model_res.get("response", {}).get("model", [])
                time.sleep(0.1)

            item["models"] = models
            full_products.append(item)

        print(f" -> Đã lấy chi tiết {len(items)} sản phẩm ({len(full_products)}/{len(all_item_ids)})")
        time.sleep(0.3)

    print(f"\n[THÀNH CÔNG] Đã trích xuất {len(full_products)} sản phẩm chi tiết!")

    # Xuất file JSON
    json_path = os.path.join(output_dir, "shopee_products.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(full_products, f, ensure_ascii=False, indent=2)
    print(f"[EXPORT] Đã lưu file JSON tại: {json_path}")

    # Làm phẳng dữ liệu ra CSV (Mỗi dòng là 1 biến thể SKU hoặc 1 sản phẩm đơn)
    csv_path = os.path.join(output_dir, "shopee_products.csv")
    flattened_rows = []
    for p in full_products:
        item_id = p.get("item_id")
        item_name = p.get("item_name")
        item_sku = p.get("item_sku", "")
        item_status = p.get("item_status")
        category_id = p.get("category_id")
        weight = p.get("weight")
        price_info = p.get("price_info", [{}])[0] if p.get("price_info") else {}
        stock_info = p.get("stock_info_v2", {}).get("summary_info", {})

        models = p.get("models", [])
        if not models:
            flattened_rows.append({
                "item_id": item_id,
                "item_name": item_name,
                "item_sku": item_sku,
                "item_status": item_status,
                "category_id": category_id,
                "weight_kg": weight,
                "model_id": "",
                "model_name": "Sản phẩm đơn (Không có biến thể)",
                "model_sku": item_sku,
                "original_price": price_info.get("original_price", 0),
                "current_price": price_info.get("current_price", 0),
                "normal_stock": stock_info.get("total_available_stock", 0),
                "reserved_stock": stock_info.get("total_reserved_stock", 0),
            })
        else:
            for m in models:
                m_price = m.get("price_info", [{}])[0] if m.get("price_info") else {}
                m_stock = m.get("stock_info_v2", {}).get("summary_info", {})
                flattened_rows.append({
                    "item_id": item_id,
                    "item_name": item_name,
                    "item_sku": item_sku,
                    "item_status": item_status,
                    "category_id": category_id,
                    "weight_kg": weight,
                    "model_id": m.get("model_id"),
                    "model_name": m.get("model_name"),
                    "model_sku": m.get("model_sku"),
                    "original_price": m_price.get("original_price", 0),
                    "current_price": m_price.get("current_price", 0),
                    "normal_stock": m_stock.get("total_available_stock", 0),
                    "reserved_stock": m_stock.get("total_reserved_stock", 0),
                })

    if flattened_rows:
        keys = flattened_rows[0].keys()
        with open(csv_path, "w", encoding="utf-8-sig", newline="") as f:
            dict_writer = csv.DictWriter(f, fieldnames=keys)
            dict_writer.writeheader()
            dict_writer.writerows(flattened_rows)
        print(f"[EXPORT] Đã lưu file CSV tại: {csv_path}")

    return full_products


if __name__ == "__main__":
    PARTNER_ID = int(os.getenv("SHOPEE_PARTNER_ID", "123456"))
    PARTNER_KEY = os.getenv("SHOPEE_PARTNER_KEY", "your_partner_key_here")
    SHOP_ID = int(os.getenv("SHOPEE_SHOP_ID", "98765432"))
    ACCESS_TOKEN = os.getenv("SHOPEE_ACCESS_TOKEN", "your_access_token_here")
    REFRESH_TOKEN = os.getenv("SHOPEE_REFRESH_TOKEN", "your_refresh_token_here")

    client = ShopeeClient(
        partner_id=PARTNER_ID,
        partner_key=PARTNER_KEY,
        shop_id=SHOP_ID,
        access_token=ACCESS_TOKEN,
        refresh_token=REFRESH_TOKEN,
        sandbox=False,
    )

    sync_all_products(client, item_status="NORMAL")

