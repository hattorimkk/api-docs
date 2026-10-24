"""
Script Trích Xuất Dữ Liệu Khuyến Mãi & Marketing (Sync Marketing & Promotions)
=============================================================================
Hỗ trợ:
- Lấy danh sách Voucher của shop (mã code, giảm giá, điều kiện áp dụng, số lượng đã dùng)
- Lấy các chương trình giảm giá sản phẩm (Shop Discount)
- Lấy hiệu quả chiến dịch Ưu đãi người theo dõi (Follow Prize)
- Xuất dữ liệu sạch ra JSON và CSV
"""

import os
import time
import json
import csv
from typing import List, Dict, Any

from shopee_client import ShopeeClient


def sync_all_marketing(
    client: ShopeeClient,
    output_dir: str = "./data",
) -> Dict[str, Any]:
    """
    Trích xuất toàn bộ dữ liệu Marketing & Khuyến mãi của Shop.
    """
    os.makedirs(output_dir, exist_ok=True)
    results: Dict[str, Any] = {
        "vouchers": [],
        "discounts": [],
        "follow_prizes": [],
    }

    print("\n[INFO] 1. Đang quét danh sách mã giảm giá (Vouchers)...")
    v_res = client.get_voucher_list(status="ALL", page_size=50)
    if not v_res.get("error"):
        voucher_list = v_res.get("response", {}).get("voucher_list", [])
        results["vouchers"] = voucher_list
        print(f" -> Lấy được {len(voucher_list)} vouchers.")

    print("\n[INFO] 2. Đang quét danh sách chương trình giảm giá (Discounts)...")
    d_res = client.get_discount_list(discount_status="ALL", page_size=50)
    if not d_res.get("error"):
        discount_list = d_res.get("response", {}).get("discount_list", [])
        results["discounts"] = discount_list
        print(f" -> Lấy được {len(discount_list)} chương trình giảm giá.")

    print("\n[INFO] 3. Đang quét chiến dịch Ưu Đãi Người Theo Dõi (Follow Prize)...")
    fp_res = client.get_follow_prize_list(status="all", page_size=50)
    if not fp_res.get("error"):
        fp_list = fp_res.get("response", {}).get("follow_prize_list", [])
        full_fps = []
        for fp in fp_list:
            c_id = fp.get("campaign_id")
            detail = client.get_follow_prize_detail(campaign_id=c_id)
            if not detail.get("error"):
                full_fps.append(detail.get("response", {}))
            time.sleep(0.1)
        results["follow_prizes"] = full_fps
        print(f" -> Lấy được {len(full_fps)} chiến dịch Follow Prize chi tiết.")

    # Xuất file JSON
    json_path = os.path.join(output_dir, "shopee_marketing.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\n[EXPORT] Đã lưu file JSON tại: {json_path}")

    # Làm phẳng dữ liệu Voucher ra CSV
    csv_voucher_path = os.path.join(output_dir, "shopee_vouchers.csv")
    if results["vouchers"]:
        with open(csv_voucher_path, "w", encoding="utf-8-sig", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=[
                "voucher_id", "voucher_code", "voucher_name", "voucher_type",
                "reward_type", "discount_amount", "percentage", "min_basket_price",
                "usage_quantity", "current_usage", "start_time", "end_time"
            ])
            writer.writeheader()
            for v in results["vouchers"]:
                writer.writerow({
                    "voucher_id": v.get("voucher_id"),
                    "voucher_code": v.get("voucher_code"),
                    "voucher_name": v.get("voucher_name"),
                    "voucher_type": v.get("voucher_type"),
                    "reward_type": v.get("reward_type"),
                    "discount_amount": v.get("discount_amount"),
                    "percentage": v.get("percentage"),
                    "min_basket_price": v.get("min_basket_price"),
                    "usage_quantity": v.get("usage_quantity"),
                    "current_usage": v.get("current_usage"),
                    "start_time": v.get("start_time"),
                    "end_time": v.get("end_time"),
                })
        print(f"[EXPORT] Đã lưu file CSV Voucher tại: {csv_voucher_path}")

    return results


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

    sync_all_marketing(client)

