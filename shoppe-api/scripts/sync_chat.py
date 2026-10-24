"""
Script Trích Xuất Lịch Sử Hội Thoại & Tin Nhắn CSKH (Sync Seller Chat)
=====================================================================
Hỗ trợ:
- Lấy toàn bộ danh sách cuộc hội thoại khách hàng (get_conversation_list)
- Tải lịch sử tin nhắn chi tiết của từng hội thoại (get_message)
- Xuất dữ liệu sạch ra JSON và CSV phục vụ huấn luyện AI hoặc phân tích CSKH
"""

import os
import time
import json
import csv
from datetime import datetime
from typing import List, Dict, Any

from shopee_client import ShopeeClient


def sync_all_chat(
    client: ShopeeClient,
    max_conversations: int = 50,
    output_dir: str = "./data",
) -> List[Dict[str, Any]]:
    """
    Trích xuất danh sách hội thoại và tin nhắn chi tiết của Shop.
    """
    os.makedirs(output_dir, exist_ok=True)
    full_chat_data = []

    print(f"\n[INFO] Đang quét danh sách cuộc hội thoại (tối đa {max_conversations} cuộc)...")
    c_res = client.get_conversation_list(conversation_type="all", page_size=min(max_conversations, 50))
    if c_res.get("error"):
        print(f"[ERROR] Không thể lấy danh sách chat: {c_res.get('message')}")
        print("Lưu ý: Ứng dụng phải được phê duyệt quyền Customer Service App để gọi API Chat.")
        return []

    conversations = c_res.get("response", {}).get("conversations", [])
    print(f" -> Tìm thấy {len(conversations)} cuộc hội thoại.")

    for conv in conversations:
        conv_id = conv.get("conversation_id")
        to_name = conv.get("to_name", "")
        to_id = conv.get("to_id")
        print(f"[INFO] Đang tải tin nhắn của khách hàng: {to_name} (ID: {to_id})...")

        # Lấy lịch sử tin nhắn
        m_res = client.get_message(conversation_id=conv_id, page_size=50)
        messages = []
        if not m_res.get("error"):
            messages = m_res.get("response", {}).get("messages", [])

        conv["messages"] = messages
        full_chat_data.append(conv)
        time.sleep(0.2)

    # Xuất file JSON
    json_path = os.path.join(output_dir, "shopee_chat.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(full_chat_data, f, ensure_ascii=False, indent=2)
    print(f"\n[EXPORT] Đã lưu file JSON tại: {json_path}")

    # Làm phẳng dữ liệu ra CSV (Mỗi dòng là 1 tin nhắn)
    csv_path = os.path.join(output_dir, "shopee_chat_messages.csv")
    flattened_messages = []
    for c in full_chat_data:
        conv_id = c.get("conversation_id")
        buyer_id = c.get("to_id")
        buyer_name = c.get("to_name")

        for m in c.get("messages", []):
            msg_id = m.get("message_id")
            sender_id = m.get("sender_id")
            is_from_shop = (sender_id == client.shop_id)
            sender_role = "SHOP" if is_from_shop else "BUYER"
            msg_type = m.get("message_type")
            content = m.get("content", {})
            text_body = content.get("text") or content.get("url") or str(content)
            created_nano = m.get("created_timestamp", 0)
            created_dt = datetime.fromtimestamp(created_nano / 1e9).strftime("%Y-%m-%d %H:%M:%S") if created_nano else ""

            flattened_messages.append({
                "conversation_id": conv_id,
                "buyer_id": buyer_id,
                "buyer_name": buyer_name,
                "message_id": msg_id,
                "sender_role": sender_role,
                "message_type": msg_type,
                "text_content": text_body,
                "created_time": created_dt,
            })

    if flattened_messages:
        keys = flattened_messages[0].keys()
        with open(csv_path, "w", encoding="utf-8-sig", newline="") as f:
            dict_writer = csv.DictWriter(f, fieldnames=keys)
            dict_writer.writeheader()
            dict_writer.writerows(flattened_messages)
        print(f"[EXPORT] Đã lưu file CSV tại: {csv_path}")

    return full_chat_data


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

    sync_all_chat(client)

