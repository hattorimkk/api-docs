# Tham Khảo API: Sản Phẩm Toàn Cầu Merchant CNSC (Global Product APIs)

Tài liệu này cung cấp chi tiết đặc tả kỹ thuật và câu lệnh **cURL** cho phân hệ **Global Product (Sản phẩm toàn cầu)** dành cho các tài khoản tổng **Merchant (China Seller Centre - CNSC)**.

---

## 1. Lấy Danh Sách Sản Phẩm Toàn Cầu (Get Global Item List)

- **Tên Endpoint**: `v2.global_product.get_global_item_list`
- **Đường dẫn**: `GET /api/v2/global_product/get_global_item_list`
- **Loại API**: Merchant API

### Lệnh cURL mẫu:
```bash
curl -X GET "https://partner.shopeemobile.com/api/v2/global_product/get_global_item_list?partner_id=123456&timestamp=1700000000&access_token=merchant_access_token_here&merchant_id=99988877&sign=calculated_sign_here&offset=0&page_size=50&global_item_status=NORMAL" \
  -H "Content-Type: application/json"
```

### Phản hồi mẫu (JSON):
```json
{
  "error": "",
  "message": "",
  "request_id": "...",
  "response": {
    "global_item_list": [
      {
        "global_item_id": 900112233,
        "global_item_status": "NORMAL",
        "update_time": 1700005000
      }
    ],
    "has_next_page": true,
    "next_offset": 50
  }
}
```

---

## 2. Xem Chi Tiết Sản Phẩm Toàn Cầu (Get Global Item Info)

- **Tên Endpoint**: `v2.global_product.get_global_item_info`
- **Đường dẫn**: `GET /api/v2/global_product/get_global_item_info`
- **Loại API**: Merchant API

### Lệnh cURL mẫu:
```bash
curl -X GET "https://partner.shopeemobile.com/api/v2/global_product/get_global_item_info?partner_id=123456&timestamp=1700000000&access_token=merchant_access_token_here&merchant_id=99988877&sign=calculated_sign_here&global_item_id_list=900112233" \
  -H "Content-Type: application/json"
```

---

## 3. Nhân Bản Sản Phẩm Sang Shop Địa Phương (Create Publish Task)

- **Tên Endpoint**: `v2.global_product.create_publish_task`
- **Đường dẫn**: `POST /api/v2/global_product/create_publish_task`
- **Loại API**: Merchant API

### Lệnh cURL mẫu:
```bash
curl -X POST "https://partner.shopeemobile.com/api/v2/global_product/create_publish_task?partner_id=123456&timestamp=1700000000&access_token=merchant_access_token_here&merchant_id=99988877&sign=calculated_sign_here" \
  -H "Content-Type: application/json" \
  -d '{
    "publish_list": [
      {
        "global_item_id": 900112233,
        "shop_id": 10012345,
        "price": 10.50
      },
      {
        "global_item_id": 900112233,
        "shop_id": 10012346,
        "price": 10.50
      }
    ]
  }'
```
