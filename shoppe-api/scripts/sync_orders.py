"""
Script Trích Xuất Dữ Liệu Toàn Bộ Đơn Hàng (Sync Orders)
=======================================================
Hỗ trợ:
- Phân trang con trỏ (cursor) tự động qua get_order_list
- Tự động chia nhỏ khoảng thời gian nếu vượt quá 15 ngày
- Gom nhóm theo mẻ (batching tối đa 50 đơn) gọi get_order_detail
- Xuất dữ liệu sạch ra file JSON và CSV
"""

import sys
import os
import time
import json
import csv
from datetime import datetime, timedelta
from typing import List, Dict, Any

from shopee_client import ShopeeClient


def sync_all_orders(
    client: ShopeeClient,
    start_date: datetime,
    end_date: datetime,
    order_status: str = None,
    output_dir: str = "./data",
) -> List[Dict[str, Any]]:
    """
    Trích xuất toàn bộ đơn hàng trong khoảng thời gian từ start_date đến end_date.
    Nếu khoảng thời gian > 14 ngày, tự động chia nhỏ thành các khung thời gian 14 ngày.
    """
    os.makedirs(output_dir, exist_ok=True)
    all_order_details = []

    # Shopee giới hạn tối đa 15 ngày mỗi lần query get_order_list
    chunk_days = 14
    current_start = start_date

    while current_start < end_date:
        current_end = min(current_start + timedelta(days=chunk_days), end_date)
        t_from = int(current_start.timestamp())
        t_to = int(current_end.timestamp())

        print(f"\n[INFO] Đang quét đơn hàng từ {current_start.strftime('%Y-%m-%d %H:%M:%S')} "
              f"đến {current_end.strftime('%Y-%m-%d %H:%M:%S')}...")

        cursor = ""
        has_more = True
        batch_order_sns = []

        while has_more:
            res = client.get_order_list(
                time_range_field="create_time",
                time_from=t_from,
                time_to=t_to,
                page_size=100,
                cursor=cursor,
                order_status=order_status,
            )

            if res.get("error"):
                print(f"[ERROR] get_order_list thất bại: {res.get('message')}")
                break

            response_data = res.get("response", {})
            order_list = response_data.get("order_list", [])
            for item in order_list:
                batch_order_sns.append(item.get("order_sn"))

            has_more = response_data.get("more", False)
            cursor = response_data.get("next_cursor", "")
            print(f" -> Lấy được {len(order_list)} mã đơn (Tổng đợt này: {len(batch_order_sns)} mã đơn)")
            time.sleep(0.2)  # Giảm tải QPS

        # Lấy chi tiết đơn hàng theo từng mẻ 50 đơn
        print(f"[INFO] Bắt đầu lấy chi tiết cho {len(batch_order_sns)} đơn hàng...")
        for i in range(0, len(batch_order_sns), 50):
            chunk = batch_order_sns[i : i + 50]
            detail_res = client.get_order_detail(order_sn_list=chunk)
            if detail_res.get("error"):
                print(f"[ERROR] get_order_detail thất bại: {detail_res.get('message')}")
                continue

            orders = detail_res.get("response", {}).get("order_list", [])
            all_order_details.extend(orders)
            print(f" -> Đã lấy chi tiết {len(orders)} đơn hàng ({len(all_order_details)}/{len(batch_order_sns)})")
            time.sleep(0.3)

        current_start = current_end

    print(f"\n[THÀNH CÔNG] Tổng cộng đã trích xuất {len(all_order_details)} đơn hàng chi tiết!")

    # Lưu ra file JSON
    json_path = os.path.join(output_dir, "shopee_orders.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(all_order_details, f, ensure_ascii=False, indent=2)
    print(f"[EXPORT] Đã lưu file JSON tại: {json_path}")

    # Làm phẳng dữ liệu và lưu ra CSV
    csv_path = os.path.join(output_dir, "shopee_orders.csv")
    flattened_rows = []
    for o in all_order_details:
        order_sn = o.get("order_sn")
        order_status = o.get("order_status")
        create_time = datetime.fromtimestamp(o.get("create_time", 0)).strftime("%Y-%m-%d %H:%M:%S")
        total_amount = o.get("total_amount", 0)
        actual_shipping_fee = o.get("actual_shipping_fee", 0)
        payment_method = o.get("payment_method", "")
        recipient = o.get("recipient_address", {})
        recipient_name = recipient.get("name", "")
        recipient_phone = recipient.get("phone", "")
        city = recipient.get("city", "")
        district = recipient.get("district", "")

        item_list = o.get("item_list", [])
        if not item_list:
            flattened_rows.append({
                "order_sn": order_sn,
                "order_status": order_status,
                "create_time": create_time,
                "total_amount": total_amount,
                "actual_shipping_fee": actual_shipping_fee,
                "payment_method": payment_method,
                "recipient_name": recipient_name,
                "recipient_phone": recipient_phone,
                "city": city,
                "district": district,
                "item_id": "",
                "item_name": "",
                "item_sku": "",
                "model_name": "",
                "model_quantity": 0,
                "model_discounted_price": 0,
            })
        else:
            for item in item_list:
                flattened_rows.append({
                    "order_sn": order_sn,
                    "order_status": order_status,
                    "create_time": create_time,
                    "total_amount": total_amount,
                    "actual_shipping_fee": actual_shipping_fee,
                    "payment_method": payment_method,
                    "recipient_name": recipient_name,
                    "recipient_phone": recipient_phone,
                    "city": city,
                    "district": district,
                    "item_id": item.get("item_id"),
                    "item_name": item.get("item_name"),
                    "item_sku": item.get("item_sku"),
                    "model_name": item.get("model_name"),
                    "model_quantity": item.get("model_quantity_purchased"),
                    "model_discounted_price": item.get("model_discounted_price"),
                })

    if flattened_rows:
        keys = flattened_rows[0].keys()
        with open(csv_path, "w", encoding="utf-8-sig", newline="") as f:
            dict_writer = csv.DictWriter(f, fieldnames=keys)
            dict_writer.writeheader()
            dict_writer.writerows(flattened_rows)
        print(f"[EXPORT] Đã lưu file CSV tại: {csv_path}")

    return all_order_details


if __name__ == "__main__":
    # Thay thông số thực tế của bạn tại đây
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

    # Ví dụ quét đơn 30 ngày qua
    end = datetime.now()
    start = end - timedelta(days=30)
    sync_all_orders(client, start_date=start, end_date=end)

