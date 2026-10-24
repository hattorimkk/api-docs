# 04. Ủy Quyền Tài Khoản Tổng Merchant (CNSC - Cross-Border)

Tài liệu này dành cho các doanh nghiệp bán hàng xuyên biên giới (Cross-border Sellers) quản lý các gian hàng Shopee ở nhiều quốc gia thông qua hệ thống **China Seller Centre (CNSC)** hoặc tài khoản tổng **Merchant**.

---

## 1. Sự Khác Biệt Giữa Shop và Merchant

- **Shop (`shop_id`)**: Đại diện cho 1 gian hàng vật lý tại một thị trường đơn lẻ (ví dụ: Shop tại Việt Nam, Shop tại Thái Lan).
- **Merchant (`merchant_id`)**: Là tài khoản cấp cha (Parent Account). Một Merchant có thể sở hữu và liên kết hàng chục Shop con ở nhiều quốc gia Đông Nam Á và Mỹ Latinh.

---

## 2. Quy Trình Ủy Quyền Cấp Merchant (Merchant Authorization)

Đối với Merchant, quy trình ủy quyền diễn ra tương tự Shop nhưng sử dụng các API dành riêng cho Merchant:

### Bước 1: Tạo link ủy quyền Merchant
- **Đường dẫn**: `/api/v2/merchant/auth_partner`
- **Công thức tính sign**:
  $$\text{Base String} = \text{partner\_id} + \text{"/api/v2/merchant/auth_partner"} + \text{timestamp}$$

### Bước 2: Đổi code lấy Token Merchant
- **Đường dẫn**: `/api/v2/auth/token/get`
- **Lệnh cURL mẫu**:
```bash
curl -X POST "https://partner.shopeemobile.com/api/v2/auth/token/get?partner_id=123456&timestamp=1700000000&sign=calculated_sign_here" \
  -H "Content-Type: application/json" \
  -d '{
    "code": "merchant_auth_code_here",
    "partner_id": 123456,
    "main_account_id": 99988877
  }'
```

---

## 3. Lấy Danh Sách Các Shop Con Thuộc Merchant

Sau khi có Access Token của Merchant, bạn có thể gọi API để lấy danh sách toàn bộ các Shop con thuộc quyền quản lý:

- **Đường dẫn API**: `GET /api/v2/merchant/get_shop_list_by_merchant`
- **Công thức ký sign**:
  $$\text{Base String} = \text{partner\_id} + \text{"/api/v2/merchant/get_shop_list_by_merchant"} + \text{timestamp} + \text{access\_token} + \text{merchant\_id}$$

### Lệnh cURL mẫu:
```bash
curl -X GET "https://partner.shopeemobile.com/api/v2/merchant/get_shop_list_by_merchant?partner_id=123456&timestamp=1700000000&access_token=merchant_access_token_here&merchant_id=99988877&sign=calculated_sign_here" \
  -H "Content-Type: application/json"
```

### Phản hồi mẫu từ Shopee:
```json
{
  "error": "",
  "message": "",
  "request_id": "...",
  "response": {
    "merchant_id": 99988877,
    "shop_list": [
      {
        "shop_id": 10012345,
        "region": "VN",
        "shop_name": "Official Store VN",
        "auth_time": 1700000000
      },
      {
        "shop_id": 10012346,
        "region": "TH",
        "shop_name": "Official Store TH",
        "auth_time": 1700000000
      }
    ]
  }
}
```

---

## 4. Lưu Ý Quan Trọng Về Nghiệp Vụ
- Để lấy đơn hàng hoặc tồn kho của từng thị trường cụ thể, bạn vẫn sử dụng `shop_id` của từng shop con.
- Để quản lý kho sản phẩm gốc (Global Products) và nhân bản sang các shop vùng, bạn sử dụng API nhóm `global_product` với `merchant_id`.

