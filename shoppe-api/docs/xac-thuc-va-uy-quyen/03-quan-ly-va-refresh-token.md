# 03. Quản Lý Vòng Đời & Làm Mới Token (Token Rotation)

Một trong những nguyên nhân phổ biến nhất khiến các hệ thống tích hợp Shopee bị gián đoạn là xử lý sai cơ chế làm mới Token (Refresh Token). Tài liệu này cung cấp hướng dẫn toàn diện về vòng đời Token và kiến trúc làm mới an toàn.

---

## 1. Vòng Đời Của Token (Token Lifecycle)

| Loại Token | Thời Gian Hiệu Lực | Mục Đích Sử Dụng |
| :--- | :--- | :--- |
| **`access_token`** | **4 Giờ** (14.400 giây) | Đính kèm vào mọi yêu cầu truy xuất dữ liệu của Shop (`get_order_list`, `get_item_list`,...). |
| **`refresh_token`** | **30 Ngày** (2.592.000 giây) | Chỉ dùng duy nhất để gọi API `/api/v2/auth/access_token/get` nhằm cấp mới một cặp Token. |

---

## 2. Cơ Chế Xoay Vòng Token (Token Rotation Mechanism)

> [!CAUTION]
> **Quy Tắc Sống Còn:**
> Khi bạn gọi API làm mới Access Token, Shopee sẽ trả về **CẢ `access_token` MỚI VÀ `refresh_token` MỚI**:
> - `access_token` cũ bị vô hiệu hóa.
> - `refresh_token` cũ **ngay lập tức bị hủy bỏ**.
> - Bạn **BẮT BUỘC** phải ghi đè cả hai giá trị mới này vào Cơ sở dữ liệu của mình. Nếu bạn chỉ cập nhật `access_token` mà quên lưu `refresh_token` mới, sau 30 ngày (hoặc ở lần refresh tiếp theo), bạn sẽ mất hoàn toàn quyền truy cập và buộc chủ Shop phải thực hiện ủy quyền lại từ đầu!

---

## 3. Chi Tiết API Làm Mới Token

- **Đường dẫn API**: `/api/v2/auth/access_token/get`
- **Phương thức**: `POST`
- **Công thức tính sign**:
  $$\text{Base String} = \text{partner\_id} + \text{"/api/v2/auth/access_token/get"} + \text{timestamp}$$

### URL Query Parameters:
- `partner_id`: `123456`
- `timestamp`: `1700000000`
- `sign`: `calculated_signature`

### Request Body (JSON):
```json
{
  "refresh_token": "current_refresh_token_string",
  "partner_id": 123456,
  "shop_id": 98765432
}
```

### Lệnh cURL làm mới Token:
```bash
curl -X POST "https://partner.shopeemobile.com/api/v2/auth/access_token/get?partner_id=123456&timestamp=1700000000&sign=calculated_signature_here" \
  -H "Content-Type: application/json" \
  -d '{
    "refresh_token": "current_refresh_token_string",
    "partner_id": 123456,
    "shop_id": 98765432
  }'
```

### Phản hồi thành công từ Shopee:
```json
{
  "error": "",
  "message": "",
  "request_id": "abc123xyz...",
  "access_token": "new_access_token_value",
  "refresh_token": "new_refresh_token_value",
  "expire_in": 14400,
  "shop_id": 98765432
}
```

---

## 4. Chiến Lược Làm Mới Token Tự Động & An Toàn

### 1. Làm mới trước hạn (Proactive Refresh)
Không đợi đến khi `access_token` hết hạn (4 tiếng) mới refresh. Hãy cấu hình hệ thống tự động làm mới khi thời hạn còn **dưới 5 đến 10 phút**.

### 2. Xử lý tranh chấp luồng (Concurrency & Distributed Lock)
Nếu hệ thống của bạn chạy nhiều tiến trình (đa luồng / đa container Docker / microservices) cùng lúc gọi Shopee API:
- Nguy cơ: Tiến trình A và Tiến trình B cùng thấy token sắp hết hạn và cùng gửi lệnh `refresh_token`. Tiến trình nào đến trước sẽ làm mới thành công, tiến trình đến sau sẽ bị lỗi do dùng `refresh_token` cũ vừa bị hủy!
- **Giải pháp**: Sử dụng khóa phân tán (**Distributed Lock** bằng Redis với `Redlock` hoặc Redis SETNX) khi thực hiện refresh token cho một `shop_id`.

```python
import redis
import time

r = redis.Redis(host="localhost", port=6379, db=0)

def refresh_token_safe(client, shop_id):
    lock_key = f"lock:shopee:refresh:{shop_id}"
    # Đặt lock trong 10 giây
    acquired = r.set(lock_key, "1", nx=True, ex=10)
    
    if acquired:
        try:
            print(f"Đang làm mới token cho shop {shop_id}...")
            new_tokens = client.refresh_access_token()
            # Cập nhật DB hoặc Redis cache
            r.set(f"shopee:access_token:{shop_id}", new_tokens["access_token"])
            r.set(f"shopee:refresh_token:{shop_id}", new_tokens["refresh_token"])
            r.set(f"shopee:expires_at:{shop_id}", time.time() + new_tokens["expire_in"])
        finally:
            r.delete(lock_key)
    else:
        # Nếu đang có tiến trình khác refresh, chỉ cần đợi 2 giây rồi đọc lại token mới từ Redis
        time.sleep(2)
```

---

## 5. Cảnh Báo Sắp Hết Hạn 30 Ngày (Shopee Push Code 10)

Shopee hỗ trợ sự kiện Webhook:
- **Push Code 10**: `Open API Authorization Expiry Push`.
- Bắn thông báo trước khi thời hạn 30 ngày của gian hàng kết thúc, giúp hệ thống của bạn gửi cảnh báo qua Email/Zalo/Telegram cho người quản trị để chủ động can thiệp nếu cần.

