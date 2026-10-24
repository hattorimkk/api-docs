# Tham Khảo API: Xác Thực & Public APIs (Authentication & Public)

Tài liệu này cung cấp đặc tả kỹ thuật chi tiết các Endpoint liên quan đến phân hệ Xác thực và Token của Shopee Open API v2, kèm theo các câu lệnh **cURL** đầy đủ để bạn có thể copy và thực thi trực tiếp trên Terminal.

---

## 1. Tạo Đường Link Ủy Quyền Gian Hàng (Shop Auth Partner)

- **Tên Endpoint**: `v2.public.auth_partner`
- **Đường dẫn**: `GET /api/v2/shop/auth_partner`
- **Môi trường Live**: `https://partner.shopeemobile.com/api/v2/shop/auth_partner`
- **Môi trường Sandbox**: `https://partner.test-stable.shopeemobile.com/api/v2/shop/auth_partner`

### Công thức tính chữ ký `sign`:
$$\text{Base String} = \text{partner\_id} + \text{"/api/v2/shop/auth_partner"} + \text{timestamp}$$

### Tham số URL (Query Parameters):
| Tên Tham Số | Kiểu Dữ Liệu | Bắt Buộc | Mô Tả |
| :--- | :--- | :--- | :--- |
| `partner_id` | int64 | Có | ID của ứng dụng Partner (ví dụ: `123456`). |
| `timestamp` | int64 | Có | Unix timestamp hiện tại tính theo giây. |
| `sign` | string | Có | Mã băm HMAC-SHA256 của chuỗi Base String bằng `partner_key`. |
| `redirect` | string | Có | URL chuyển hướng callback sau khi chủ shop bấm đồng ý (được URL-encode). |

### Lệnh cURL mẫu:
```bash
# Tạo đường dẫn ủy quyền (mở đường dẫn này trên trình duyệt để chủ shop đăng nhập)
curl -X GET "https://partner.shopeemobile.com/api/v2/shop/auth_partner?partner_id=123456&timestamp=1700000000&sign=4b61dcc1e39a01dfabf8f4f325325efd5af5efc138ddf8e7e30352bb53239cf4&redirect=https%3A%2F%2Fyour-domain.com%2Fcallback"
```

---

## 2. Đổi Mã Code Lấy Access Token & Refresh Token (Get Token)

- **Tên Endpoint**: `v2.public.get_access_token`
- **Đường dẫn**: `POST /api/v2/auth/token/get`
- **Môi trường Live**: `https://partner.shopeemobile.com/api/v2/auth/token/get`
- **Môi trường Sandbox**: `https://partner.test-stable.shopeemobile.com/api/v2/auth/token/get`

### Công thức tính chữ ký `sign`:
$$\text{Base String} = \text{partner\_id} + \text{"/api/v2/auth/token/get"} + \text{timestamp}$$

### Tham số URL (Query Parameters):
`partner_id`, `timestamp`, `sign`

### Request Body (JSON):
| Trường Dữ Liệu | Kiểu Dữ Liệu | Bắt Buộc | Mô Tả |
| :--- | :--- | :--- | :--- |
| `code` | string | Có | Authorization Code nhận được từ tham số `?code=...` tại Callback URL. |
| `partner_id` | int64 | Có | ID ứng dụng Partner. |
| `shop_id` | int64 | Có (với Shop) | ID của gian hàng vừa cấp quyền. |

### Lệnh cURL mẫu:
```bash
curl -X POST "https://partner.shopeemobile.com/api/v2/auth/token/get?partner_id=123456&timestamp=1700000000&sign=d9f3d99ee8cd4e4c8b13c843cd352b41fa4d6ec1f749b08599df436ac87d9d69" \
  -H "Content-Type: application/json" \
  -d '{
    "code": "6162636465666768...",
    "partner_id": 123456,
    "shop_id": 98765432
  }'
```

### Phản Hồi Mẫu (Response JSON):
```json
{
  "error": "",
  "message": "",
  "request_id": "76ba370b77c3858739191d9e798e4d1a",
  "access_token": "c71a39d892ef65a43b1234567890abcd",
  "refresh_token": "9876543210fedcba0987654321fedcba",
  "expire_in": 14400,
  "shop_id": 98765432,
  "merchant_id_list": []
}
```

---

## 3. Làm Mới Access Token Khi Hết Hạn (Refresh Token)

- **Tên Endpoint**: `v2.public.refresh_access_token`
- **Đường dẫn**: `POST /api/v2/auth/access_token/get`
- **Môi trường Live**: `https://partner.shopeemobile.com/api/v2/auth/access_token/get`

### Công thức tính chữ ký `sign`:
$$\text{Base String} = \text{partner\_id} + \text{"/api/v2/auth/access_token/get"} + \text{timestamp}$$

### Tham số URL (Query Parameters):
`partner_id`, `timestamp`, `sign`

### Request Body (JSON):
| Trường Dữ Liệu | Kiểu Dữ Liệu | Bắt Buộc | Mô Tả |
| :--- | :--- | :--- | :--- |
| `refresh_token` | string | Có | Chuỗi `refresh_token` hiện tại đang lưu trong cơ sở dữ liệu. |
| `partner_id` | int64 | Có | ID ứng dụng Partner. |
| `shop_id` | int64 | Có | ID gian hàng cần làm mới token. |

### Lệnh cURL mẫu:
```bash
curl -X POST "https://partner.shopeemobile.com/api/v2/auth/access_token/get?partner_id=123456&timestamp=1700000000&sign=8488e02511470ad46b3e8c95029e24b7a1b2c3d4e5f60718293a4b5c6d7e8f90" \
  -H "Content-Type: application/json" \
  -d '{
    "refresh_token": "9876543210fedcba0987654321fedcba",
    "partner_id": 123456,
    "shop_id": 98765432
  }'
```

### Phản Hồi Mẫu (Response JSON):
```json
{
  "error": "",
  "message": "",
  "request_id": "8488e02511470ad46b3e8c95029e24b7",
  "access_token": "f0e1d2c3b4a59687new_token_value",
  "refresh_token": "a1b2c3d4e5f60718new_refresh_token_value",
  "expire_in": 14400,
  "shop_id": 98765432
}
```

---

## 4. Hủy Quyền Ủy Quyền Gian Hàng (Cancel Shop Auth)

- **Tên Endpoint**: `v2.public.cancel_auth_partner`
- **Đường dẫn**: `POST /api/v2/shop/cancel_auth_partner`

### Lệnh cURL mẫu:
```bash
curl -X POST "https://partner.shopeemobile.com/api/v2/shop/cancel_auth_partner?partner_id=123456&timestamp=1700000000&access_token=c71a39d892ef65a43b1234567890abcd&shop_id=98765432&sign=calculated_sign_here" \
  -H "Content-Type: application/json" \
  -d '{
    "partner_id": 123456,
    "shop_id": 98765432
  }'
```
