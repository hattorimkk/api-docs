#!/usr/bin/env python3
"""
Meta Conversions API (CAPI) Event Dispatcher
Ho tro ma hoa chuan hoa SHA-256 tu dong cho email, so dien thoai.
Thiet ke bang thu vien chuan Python (urllib.request), khong can cai them dependencies.
"""

import hashlib
import time
import json
import sys
import urllib.request
import urllib.error

def hash_sha256(value: str) -> str:
    if not value:
        return ""
    clean_val = value.strip().lower()
    return hashlib.sha256(clean_val.encode('utf-8')).hexdigest()

def normalize_vn_phone(phone: str) -> str:
    p = phone.strip().replace(" ", "").replace(".", "").replace("+", "").replace("-", "")
    if p.startswith("0"):
        p = "84" + p[1:]
    return hash_sha256(p)

def send_capi_event(pixel_id: str, access_token: str, event_data: dict, test_code: str = None):
    url = f"https://graph.facebook.com/v22.0/{pixel_id}/events"
    
    # Xay dung user_data voi chuan hoa SHA-256
    user_data = {}
    if "email" in event_data:
        user_data["em"] = [hash_sha256(event_data["email"])]
    if "phone" in event_data:
        user_data["ph"] = [normalize_vn_phone(event_data["phone"])]
    if "client_ip" in event_data:
        user_data["client_ip_address"] = event_data["client_ip"]
    if "user_agent" in event_data:
        user_data["client_user_agent"] = event_data["user_agent"]
    if "fbp" in event_data:
        user_data["fbp"] = event_data["fbp"]
    if "fbc" in event_data:
        user_data["fbc"] = event_data["fbc"]

    payload_event = {
        "event_name": event_data.get("event_name", "Purchase"),
        "event_time": int(time.time()),
        "event_id": event_data["event_id"],
        "event_source_url": event_data.get("source_url", "https://myshop.vn"),
        "action_source": "website",
        "user_data": user_data,
        "custom_data": event_data.get("custom_data", {})
    }

    body = {
        "data": [payload_event],
        "access_token": access_token
    }
    
    if test_code:
        body["test_event_code"] = test_code

    req_data = json.dumps(body).encode('utf-8')
    req = urllib.request.Request(
        url,
        data=req_data,
        headers={"Content-Type": "application/json"}
    )

    print(f"[*] Dang gui su kien CAPI len Pixel: {pixel_id}...")
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            status = resp.status
            result = json.loads(resp.read().decode('utf-8'))
            return status, result
    except urllib.error.HTTPError as e:
        error_body = e.read().decode('utf-8')
        try:
            return e.code, json.loads(error_body)
        except Exception:
            return e.code, {"error_raw": error_body}

if __name__ == "__main__":
    print("=== Meta Conversions API Test Tool ===")
    sample_order = {
        "event_name": "Purchase",
        "event_id": f"ORDER_{int(time.time())}",
        "source_url": "https://myshop.vn/checkout/success",
        "email": "khachhang_test@gmail.com",
        "phone": "0912345678",
        "client_ip": "113.190.234.12",
        "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
        "custom_data": {
            "currency": "VND",
            "value": 850000,
            "order_id": f"ORDER_{int(time.time())}",
            "contents": [
                {"id": "SKU_01", "quantity": 1, "item_price": 850000}
            ]
        }
    }
    print(f"Payload mau chuan hoa:\n{json.dumps(sample_order, indent=2, ensure_ascii=False)}")
    print("\nDe thuc thi that, goi ham send_capi_event(pixel_id, access_token, event_data, test_code).")

