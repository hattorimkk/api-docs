#!/usr/bin/env python3
"""
Tiện ích ký số HMAC-SHA256 chuẩn cho TikTok Shop Partner API v2.
Dùng để tạo chữ ký (sign) và tự động sinh câu lệnh cURL sẵn sàng thực thi.

Thuật toán chuẩn theo tài liệu TikTok Shop Partner:
1. Lấy tất cả query parameters ngoại trừ 'sign' và 'access_token'.
2. Sắp xếp các key theo thứ tự bảng chữ cái (A-Z).
3. Nối các cặp theo định dạng: {key}{value}.
4. Đặt request path lên phía trước: {path}{params}.
5. Nếu request body tồn tại và content-type khác multipart/form-data, nối nguyên vẹn body vào cuối chuỗi: {path}{params}{body}.
6. Bao chuỗi vừa tạo bằng app_secret ở cả 2 đầu: {app_secret}{path}{params}{body}{app_secret}.
7. Dùng HMAC-SHA256 với salt là app_secret để băm và chuyển thành chuỗi hex lowercase.
"""

import hmac
import hashlib
import time
import urllib.parse
import json
import sys

def calculate_sign(app_key: str, app_secret: str, path: str, queries: dict, body: str = "") -> str:
    # 1 & 2. Sắp xếp key loại trừ 'sign' và 'access_token'
    sorted_keys = sorted([k for k in queries.keys() if k not in ("sign", "access_token")])
    
    # 3. Nối {key}{value}
    param_str = "".join([f"{k}{queries[k]}" for k in sorted_keys])
    
    # 4 & 5. Nối {path} + {param_str} + {body}
    input_str = f"{path}{param_str}{body}"
    
    # 6. Bao bọc với app_secret
    wrapped_str = f"{app_secret}{input_str}{app_secret}"
    
    # 7. Ký HMAC-SHA256
    sign = hmac.new(
        app_secret.encode("utf-8"),
        wrapped_str.encode("utf-8"),
        hashlib.sha256
    ).hexdigest()
    
    return sign

def build_curl(app_key: str, app_secret: str, access_token: str, path: str, queries: dict, method: str = "GET", body: dict = None) -> str:
    timestamp = queries.get("timestamp", str(int(time.time())))
    queries["app_key"] = app_key
    queries["timestamp"] = timestamp
    
    body_str = json.dumps(body, separators=(",", ":"), ensure_ascii=False) if body else ""
    sign = calculate_sign(app_key, app_secret, path, queries, body_str)
    queries["sign"] = sign
    
    encoded_query = urllib.parse.urlencode(queries)
    full_url = f"https://open-api.tiktokglobalshop.com{path}?{encoded_query}"
    
    curl_cmd = f"curl -X {method} \\\n  '{full_url}' \\\n  -H 'x-tts-access-token: {access_token}' \\\n  -H 'Content-Type: application/json'"
    if body_str:
        curl_cmd += f" \\\n  -d '{body_str}'"
        
    return curl_cmd

if __name__ == "__main__":
    # Test case mẫu chuẩn trong tài liệu TikTok Shop
    test_key = "29a39d"
    test_secret = "e59af819cc"
    test_path = "/authorization/202309/shops"
    test_queries = {"app_key": test_key, "timestamp": "1623812664"}
    
    expected_sign = "b596b73e0cc6de07ac26f036364178ab16b0a907af13d43f0a0cd2345f582dc8"
    actual_sign = calculate_sign(test_key, test_secret, test_path, test_queries)
    
    print("=== KIỂM THỬ THUẬT TOÁN KÝ SỐ TIKTOK SHOP ===")
    print(f"Chữ ký tính toán: {actual_sign}")
    print(f"Chữ ký kỳ vọng  : {expected_sign}")
    assert actual_sign == expected_sign, "Thuật toán ký số không khớp!"
    print("=> Kết quả: CHÍNH XÁC 100% khớp tài liệu chuẩn của TikTok Shop!\n")
    
    sample_curl = build_curl(
        app_key="YOUR_APP_KEY",
        app_secret="YOUR_APP_SECRET",
        access_token="YOUR_ACCESS_TOKEN",
        path="/authorization/202309/shops",
        queries={}
    )
    print("Mẫu cURL sinh tự động:")
    print(sample_curl)

