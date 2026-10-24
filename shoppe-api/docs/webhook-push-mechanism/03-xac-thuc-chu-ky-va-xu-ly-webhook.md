# 03. Xác Thực Chữ Ký Webhook & Xử Lý Idempotency

Để đảm bảo máy chủ của bạn không bị tấn công giả mạo (Man-in-the-middle hoặc gửi request rác từ bên ngoài), Shopee đính kèm một chữ ký bảo mật trong HTTP Header `Authorization`. Tài liệu này hướng dẫn cách kiểm tra chữ ký và đảm bảo tính Idempotency khi nhận webhook.

---

## 1. Công Thức Xác Thực Chữ Ký Webhook

Shopee ký thông điệp gửi sang webhook bằng thuật toán HMAC-SHA256:

$$\text{Base String} = \text{Callback URL} + \text{"\|"} + \text{Raw Request Body (Bytes)}$$

$$\text{Authorization Header} = \text{HMAC-SHA256}(\text{Base String}, \text{partner\_key})$$

### Các quy tắc cốt tử:
1. **Dấu gạch đứng phân tách (`|`)**: Nằm ngay giữa URL và Body, không có khoảng trắng.
2. **Callback URL**: Phải là đường dẫn đầy đủ chính xác từng ký tự như bạn đã lưu trong App Console (ví dụ: `https://api.yourdomain.com/webhook/shopee`).
3. **Bảo toàn Raw Request Body**:
   > [!CAUTION]
   > Bạn phải đọc nội dung Body dưới dạng **chuỗi byte nguyên bản (Raw Stream Bytes)** trước khi bất kỳ middleware phân tích cú pháp JSON nào (như `body-parser` trong Express hoặc tự động parse trong FastAPI/Django) kịp can thiệp. Nếu một parser format lại khoảng trắng hoặc đảo thứ tự các key trong JSON, chuỗi byte sẽ thay đổi và chữ ký xác thực **CHẮC CHẮN SẼ BỊ SAI**!

---

## 2. Code Mẫu Xác Thực Chữ Ký Chuẩn

### Python (FastAPI / Flask)
```python
import hmac
import hashlib

def verify_shopee_webhook(callback_url: str, raw_body_bytes: bytes, partner_key: str, authorization_header: str) -> bool:
    """
    Xác thực chữ ký Shopee Webhook một cách an toàn (chống timing attack).
    """
    base_string = callback_url.encode("utf-8") + b"|" + raw_body_bytes
    calculated_sign = hmac.new(
        partner_key.encode("utf-8"),
        base_string,
        hashlib.sha256
    ).hexdigest()
    
    # So sánh an toàn bằng hmac.compare_digest
    return hmac.compare_digest(calculated_sign.lower(), authorization_header.lower())
```

### Node.js (Express)
```javascript
const crypto = require('crypto');

function verifyShopeeWebhook(callbackUrl, rawBodyBuffer, partnerKey, authHeader) {
    const baseBuffer = Buffer.concat([
        Buffer.from(callbackUrl + '|', 'utf-8'),
        rawBodyBuffer
    ]);
    
    const calculatedSign = crypto
        .createHmac('sha256', partnerKey)
        .update(baseBuffer)
        .digest('hex');
        
    return crypto.timingSafeEqual(
        Buffer.from(calculatedSign.toLowerCase()),
        Buffer.from(authHeader.toLowerCase())
    );
}
```

---

## 3. Lệnh cURL Mô Phỏng Gửi Webhook Để Kiểm Thử Server (Test Webhook)

Bạn có thể tự kiểm thử máy chủ tiếp nhận Webhook của mình bằng lệnh `cURL` trên Terminal:

```bash
# 1. Khai báo URL webhook máy chủ của bạn
WEBHOOK_URL="http://localhost:8080"
PARTNER_KEY="your_partner_key_here"

# 2. Khởi tạo nội dung JSON mẫu (Sự kiện Code 3: Đơn hàng mới READY_TO_SHIP)
BODY='{"shop_id":98765432,"code":3,"timestamp":1700012345,"data":{"ordersn":"261023ABCD1234","status":"READY_TO_SHIP","update_time":1700012345}}'

# 3. Tạo chữ ký số HMAC-SHA256 mô phỏng Shopee
SIGN=$(printf "%s|%s" "$WEBHOOK_URL" "$BODY" | openssl dgst -sha256 -hmac "$PARTNER_KEY" | awk '{print $2}')

# 4. Gửi HTTP POST kèm Authorization Header bằng cURL
curl -X POST "$WEBHOOK_URL" \
  -H "Content-Type: application/json" \
  -H "Authorization: $SIGN" \
  -d "$BODY"
```

---

## 4. Xử Lý Trùng Lặp Thông Điệp (Idempotency Pattern)

Trong môi trường mạng phân tán, Shopee có thể gửi lại cùng một sự kiện nhiều lần (do mạng lag, phản hồi chậm, hoặc cơ chế retry tự động). Hệ thống của bạn phải đảm bảo tính **Idempotent** (xử lý nhiều lần cùng một sự kiện nhưng kết quả chỉ ghi nhận một lần duy nhất).

### Chiến lược sử dụng Redis Caching:
1. Tạo một khóa định danh duy nhất (Idempotency Key) cho mỗi thông điệp nhận được:
   $$\text{Key} = \text{"shopee:event:"} + \text{code} + \text{":"} + \text{shop\_id} + \text{":"} + \text{order\_sn / item\_id} + \text{":"} + \text{timestamp}$$
2. Kiểm tra trong Redis bằng lệnh `SET NX` (chỉ đặt nếu chưa tồn tại) với thời hạn hết hạn (TTL) là 24 giờ:
```python
import redis

r = redis.Redis(host="localhost", port=6379, db=0)

def process_webhook_event(payload: dict):
    code = payload.get("code")
    shop_id = payload.get("shop_id")
    timestamp = payload.get("timestamp")
    data = payload.get("data", {})
    
    identifier = data.get("ordersn") or data.get("item_id") or "general"
    event_key = f"shopee:event:{code}:{shop_id}:{identifier}:{timestamp}"
    
    # Chỉ xử lý nếu key chưa từng xuất hiện trong 24 giờ qua
    is_new_event = r.set(event_key, "processed", nx=True, ex=86400)
    if not is_new_event:
        print(f"Sự kiện {event_key} đã được xử lý trước đó, bỏ qua để tránh trùng lặp.")
        return True
        
    # Tiếp tục logic xử lý nghiệp vụ thực tế (ghi DB, bắn thông báo...)
    return True
```

