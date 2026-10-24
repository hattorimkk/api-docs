"""
Script Trích Xuất Dữ Liệu Đối Soát Doanh Thu & Escrow (Sync Financial Income)
=============================================================================
Hỗ trợ:
- Lấy danh sách các đơn hàng đã được quyết toán tiền về ví (get_escrow_list)
- Truy vấn bảng kê tài chính chi tiết từng đơn hàng (get_escrow_detail)
- Bóc tách doanh thu ròng (escrow_amount), phí sàn (commission, service, transaction fees)
- Xuất dữ liệu đối soát ra JSON và CSV
"""

import os
import time
import json
import csv
from datetime import datetime, timedelta
from typing import List, Dict, Any

from shopee_client import ShopeeClient


def sync_escrow_income(
    client: ShopeeClient,
    start_date: datetime,
    end_date: datetime,
    output_dir: str = "./data",
) -> List[Dict[str, Any]]:
    """
    Trích xuất toàn bộ báo cáo doanh thu đã quyết toán từ start_date đến end_date.
    """
    os.makedirs(output_dir, exist_ok=True)
    t_from = int(start_date.timestamp())
    t_to = int(end_date.timestamp())

    print(f"\n[INFO] Đang quét danh sách quyết toán từ {start_date.strftime('%Y-%m-%d')} "
          f"đến {end_date.strftime('%Y-%m-%d')}...")

    all_escrow_orders = []
    page_no = 1
    page_size = 50
    has_more = True

    while has_more:
        res = client.get_escrow_list(
            release_time_from=t_from,
            release_time_to=t_to,
            page_size=page_size,
            page_no=page_no,
        )

        if res.get("error"):
            print(f"[ERROR] get_escrow_list thất bại: {res.get('message')}")
            break

        response_data = res.get("response", {})
        escrow_list = response_data.get("escrow_list", [])
        for item in escrow_list:
            all_escrow_orders.append(item.get("order_sn"))

        has_more = response_data.get("more", False)
        page_no += 1
        print(f" -> Lấy được {len(escrow_list)} đơn quyết toán (Tổng: {len(all_escrow_orders)} đơn)")
        time.sleep(0.2)

    print(f"[INFO] Bắt đầu lấy chi tiết tài chính cho {len(all_escrow_orders)} đơn hàng...")
    escrow_details = []

    for idx, order_sn in enumerate(all_escrow_orders, 1):
        detail_res = client.get_escrow_detail(order_sn=order_sn)
        if detail_res.get("error"):
            print(f"[ERROR] get_escrow_detail thất bại cho đơn {order_sn}: {detail_res.get('message')}")
            continue

        detail = detail_res.get("response", {})
        escrow_details.append(detail)
        if idx % 20 == 0 or idx == len(all_escrow_orders):
            print(f" -> Đã lấy chi tiết {idx}/{len(all_escrow_orders)} đơn hàng...")
        time.sleep(0.15)

    print(f"\n[THÀNH CÔNG] Đã trích xuất {len(escrow_details)} bản ghi tài chính chi tiết!")

    # Xuất file JSON
    json_path = os.path.join(output_dir, "shopee_escrow.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(escrow_details, f, ensure_ascii=False, indent=2)
    print(f"[EXPORT] Đã lưu file JSON tại: {json_path}")

    # Làm phẳng dữ liệu ra CSV
    csv_path = os.path.join(output_dir, "shopee_escrow.csv")
    flattened_rows = []
    for d in escrow_details:
        order_income = d.get("order_income", {})
        buyer_payment = d.get("buyer_payment_info", {})

        flattened_rows.append({
            "order_sn": d.get("order_sn"),
            "buyer_user_name": d.get("buyer_user_name", ""),
            "payout_amount": order_income.get("escrow_amount", 0),  # Tiền thực nhận của shop
            "buyer_total_amount": buyer_payment.get("buyer_total_amount", 0),
            "original_cost_of_goods_sold": order_income.get("original_cost_of_goods_sold", 0),
            "seller_discount": order_income.get("seller_discount", 0),
            "shopee_discount": order_income.get("shopee_discount", 0),
            "voucher_from_seller": order_income.get("voucher_from_seller", 0),
            "voucher_from_shopee": order_income.get("voucher_from_shopee", 0),
            "commission_fee": order_income.get("commission_fee", 0),  # Phí hoa hồng
            "service_fee": order_income.get("service_fee", 0),        # Phí dịch vụ (Freeship Xtra, Hoàn xu)
            "transaction_fee": order_income.get("transaction_fee", 0),# Phí thanh toán
            "actual_shipping_fee": order_income.get("actual_shipping_fee", 0),
            "shopee_shipping_rebate": order_income.get("shopee_shipping_rebate", 0),
            "cross_border_tax": order_income.get("cross_border_tax", 0),
        })

    if flattened_rows:
        keys = flattened_rows[0].keys()
        with open(csv_path, "w", encoding="utf-8-sig", newline="") as f:
            dict_writer = csv.DictWriter(f, fieldnames=keys)
            dict_writer.writeheader()
            dict_writer.writerows(flattened_rows)
        print(f"[EXPORT] Đã lưu file CSV tại: {csv_path}")

    return escrow_details


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

    end = datetime.now()
    start = end - timedelta(days=15)
    sync_escrow_income(client, start_date=start, end_date=end)

