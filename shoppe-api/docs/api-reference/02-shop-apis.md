# Tham Khảo API: Thông Tin & Hồ Sơ Gian Hàng (Shop APIs)

Tài liệu này cung cấp chi tiết đặc tả kỹ thuật và câu lệnh **cURL** cho các API quản lý thông tin cơ bản, hồ sơ và trạng thái ủy quyền của gian hàng Shopee.

---

## 1. Lấy Thông Tin Cơ Bản Gian Hàng (Get Shop Info)

- **Tên Endpoint**: `v2.shop.get_shop_info`
- **Đường dẫn**: `GET /api/v2/shop/get_shop_info`
- **Loại API**: Shop API

### Công thức tính chữ ký `sign`:
$$\text{Base String} = \text{partner\_id} + \text{"/api/v2/shop/get_shop_info"} + \text{timestamp} + \text{access\_token} + \text{shop\_id}$$

### Tham số URL (Query Parameters):
| Tham Số | Kiểu Dữ Liệu | Bắt Buộc | Mô Tả |
| :--- | :--- | :--- | :--- |
| `partner_id` | int64 | Có | ID ứng dụng Partner. |
| `timestamp` | int64 | Có | Thời gian Unix timestamp (giây). |
| `access_token` | string | Có | Access token hợp lệ của Shop. |
| `shop_id` | int64 | Có | ID gian hàng cần tra cứu. |
| `sign` | string | Có | Chữ ký số HMAC-SHA256. |

### Lệnh cURL mẫu:
```bash
curl -X GET "https://partner.shopeemobile.com/api/v2/shop/get_shop_info?partner_id=123456&timestamp=1700000000&access_token=c71a39d892ef65a43b1234567890abcd&shop_id=98765432&sign=f749b08599df436ac87d9d69d9f3d99ee8cd4e4c8b13c843cd352b41fa4d6ec1" \
  -H "Content-Type: application/json"
```

### Phản hồi mẫu (Response JSON):
```json
{
  "error": "",
  "message": "",
  "request_id": "90812abef77c3858...",
  "response": {
    "shop_name": "Antigravity Official Store",
    "region": "VN",
    "status": "NORMAL",
    "is_sip": false,
    "is_cb": false,
    "auth_time": 1699990000,
    "expire_time": 1702582000
  }
}
```

---

## 2. Lấy Hồ Sơ Gian Hàng (Get Shop Profile)

- **Tên Endpoint**: `v2.shop.get_profile`
- **Đường dẫn**: `GET /api/v2/shop/get_profile`
- **Loại API**: Shop API

### Lệnh cURL mẫu:
```bash
curl -X GET "https://partner.shopeemobile.com/api/v2/shop/get_profile?partner_id=123456&timestamp=1700000000&access_token=c71a39d892ef65a43b1234567890abcd&shop_id=98765432&sign=calculated_sign_here" \
  -H "Content-Type: application/json"
```

### Phản hồi mẫu (JSON):
```json
{
  "error": "",
  "message": "",
  "request_id": "...",
  "response": {
    "shop_logo": "https://down-vn.img.susercontent.com/file/vn-11134207-7r98o-lst123456789ab",
    "description": "Chào mừng bạn đến với gian hàng chính hãng. Cam kết đổi trả trong 7 ngày."
  }
}
```

---

## 3. Cập Nhật Hồ Sơ Gian Hàng (Update Shop Profile)

- **Tên Endpoint**: `v2.shop.update_profile`
- **Đường dẫn**: `POST /api/v2/shop/update_profile`
- **Loại API**: Shop API

### Lệnh cURL mẫu:
```bash
curl -X POST "https://partner.shopeemobile.com/api/v2/shop/update_profile?partner_id=123456&timestamp=1700000000&access_token=c71a39d892ef65a43b1234567890abcd&shop_id=98765432&sign=calculated_sign_here" \
  -H "Content-Type: application/json" \
  -d '{
    "shop_logo": "https://down-vn.img.susercontent.com/file/new_logo_url",
    "description": "Mô tả mới của gian hàng đã được cập nhật thành công."
  }'
```
