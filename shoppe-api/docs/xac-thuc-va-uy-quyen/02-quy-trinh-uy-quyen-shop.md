# 02. Quy Trình Ủy Quyền Gian Hàng (Shop Authorization Flow)

Để ứng dụng có quyền truy cập và thao tác với dữ liệu của một gian hàng Shopee, chủ Shop phải thực hiện quy trình ủy quyền theo chuẩn OAuth 2.0.

---

## 1. Sơ Đồ Quy Trình Ủy Quyền (OAuth 2.0 Sequence Diagram)

```
[Chủ Shop]              [Ứng Dụng Của Bạn]              [Shopee Server]
    |                           |                              |
    |  1. Nhấn nút "Ủy quyền"   |                              |
    |-------------------------->|                              |
    |                           |  2. Tính sign & tạo URL      |
    |  3. Chuyển hướng trình duyệt đến Shopee OAuth URL        |
    |<--------------------------|                              |
    |                                                          |
    |  4. Đăng nhập tài khoản Bán Hàng & Bấm "Confirm"         |
    |--------------------------------------------------------->|
    |                                                          |
    |  5. Redirect về redirect_url?code=ABC&shop_id=12345      |
    |<---------------------------------------------------------|
    |                                                          |
    |  6. Trình duyệt gửi GET về Callback URL của ứng dụng     |
    |-------------------------->|                              |
    |                           |  7. POST /api/v2/auth/token/get
    |                           |     (code, partner_id, shop_id)
    |                           |----------------------------->|
    |                           |                              |
    |                           |  8. Trả về access_token &    |
    |                           |     refresh_token            |
    |                           |<-----------------------------|
    |                           |                              |
    |  9. Báo ủy quyền thành công!                             |
    |<--------------------------|                              |
```

---

## 2. Bước 1: Tạo Đường Link Ủy Quyền (Authorization Link)

Ứng dụng tạo đường dẫn để chuyển hướng chủ Shop sang trang xác thực của Shopee.

- **Đường dẫn API**: `/api/v2/shop/auth_partner`
- **Công thức ký chữ ký `sign`**:
  $$\text{Base String} = \text{partner\_id} + \text{"/api/v2/shop/auth_partner"} + \text{timestamp}$$

### Tham số trên URL:
| Tham số | Bắt buộc | Mô tả |
| :--- | :--- | :--- |
| `partner_id` | Có | ID ứng dụng của bạn. |
| `timestamp` | Có | Unix timestamp hiện tại tính bằng giây. |
| `sign` | Có | Chữ ký số HMAC-SHA256 được tính từ Base String ở trên. |
| `redirect` | Có | URL chuyển hướng đã đăng ký trong App Console (URL-encoded). |

### Ví dụ tạo link ủy quyền bằng Bash / OpenSSL:
```bash
PARTNER_ID="123456"
PARTNER_KEY="your_partner_key"
API_PATH="/api/v2/shop/auth_partner"
TIMESTAMP=$(date +%s)
REDIRECT_URL="https://your-domain.com/shopee/callback"

# Tính sign
BASE_STRING="${PARTNER_ID}${API_PATH}${TIMESTAMP}"
SIGN=$(printf "%s" "$BASE_STRING" | openssl dgst -sha256 -hmac "$PARTNER_KEY" | awk '{print $2}')

# URL-encode redirect url
REDIRECT_ENCODED=$(python3 -c "import urllib.parse; print(urllib.parse.quote('$REDIRECT_URL', safe=''))")

AUTH_URL="https://partner.shopeemobile.com${API_PATH}?partner_id=${PARTNER_ID}&timestamp=${TIMESTAMP}&sign=${SIGN}&redirect=${REDIRECT_ENCODED}"
echo "Gửi link này cho chủ shop mở trên trình duyệt để cấp quyền:"
echo "$AUTH_URL"
```

Link tạo ra sẽ có dạng:
```text
https://partner.shopeemobile.com/api/v2/shop/auth_partner?partner_id=123456&timestamp=1700000000&sign=ab12...cd34&redirect=https%3A%2F%2Fyour-domain.com%2Fshopee%2Fcallback
```

---

## 3. Bước 2: Nhận Callback & Mã Code

Khi chủ shop đăng nhập và nhấn **Xác nhận (Confirm Authorization)**, Shopee chuyển hướng trình duyệt của người bán về đường dẫn `redirect_url` kèm 2 tham số Query:
```text
https://your-domain.com/shopee/callback?code=616263...&shop_id=98765432
```

- **`code`**: Authorization Code tạm thời (chỉ dùng được 1 lần và có hạn dùng trong khoảng 10 phút).
- **`shop_id`**: ID của gian hàng vừa thực hiện cấp quyền.

---

## 4. Bước 3: Đổi Code Lấy Access Token & Refresh Token

Ngay sau khi nhận được `code` tại callback endpoint, máy chủ của bạn phải gửi request `POST` đến API Public `/api/v2/auth/token/get` để đổi lấy Token.

- **Đường dẫn API**: `/api/v2/auth/token/get`
- **Phương thức**: `POST`
- **Công thức tính sign**:
  $$\text{Base String} = \text{partner\_id} + \text{"/api/v2/auth/token/get"} + \text{timestamp}$$

### URL Query Parameters:
- `partner_id`: `123456`
- `timestamp`: `1700000000`
- `sign`: `calculated_signature`

### Request Body (JSON):
```json
{
  "code": "616263...",
  "partner_id": 123456,
  "shop_id": 98765432
}
```

### Lệnh cURL đổi code lấy Token:
```bash
curl -X POST "https://partner.shopeemobile.com/api/v2/auth/token/get?partner_id=123456&timestamp=1700000000&sign=calculated_signature_here" \
  -H "Content-Type: application/json" \
  -d '{
    "code": "616263...",
    "partner_id": 123456,
    "shop_id": 98765432
  }'
```

### Phản hồi thành công từ Shopee:
```json
{
  "error": "",
  "message": "",
  "request_id": "890123abcdef...",
  "access_token": "4a5b6c7d8e...",
  "refresh_token": "9z8y7x6w5v...",
  "expire_in": 14400,
  "shop_id": 98765432,
  "merchant_id_list": []
}
```

- **`access_token`**: Dùng để gọi tất cả các API Shop sau này. Có hiệu lực trong **14.400 giây (4 giờ)**.
- **`refresh_token`**: Dùng để cấp lại `access_token` mới khi hết hạn. Có hiệu lực trong **30 ngày**.
- **`expire_in`**: Thời gian tồn tại của `access_token` tính bằng giây.

> [!IMPORTANT]
> Hãy lưu trữ `access_token`, `refresh_token`, `shop_id` và mốc thời gian hết hạn (`expires_at = now + expire_in`) vào Cơ sở dữ liệu (PostgreSQL, MySQL, MongoDB hoặc Redis) của bạn ngay lập tức!

