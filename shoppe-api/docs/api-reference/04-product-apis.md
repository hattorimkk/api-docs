# Tham Khảo API: Quản Lý Sản Phẩm (Product & Item APIs)

Tài liệu này cung cấp chi tiết đặc tả kỹ thuật và câu lệnh **cURL** cho toàn bộ các API trong phân hệ Sản phẩm và Quản lý Tồn kho của Shopee Open API v2.

---

## 1. Lấy Danh Sách Sản Phẩm (Get Item List)

- **Tên Endpoint**: `v2.product.get_item_list`
- **Đường dẫn**: `GET /api/v2/product/get_item_list`
- **Loại API**: Shop API

### Tham số URL (Query Parameters):
| Tham Số | Kiểu Dữ Liệu | Bắt Buộc | Mô Tả |
| :--- | :--- | :--- | :--- |
| `offset` | int32 | Có | Vị trí bắt đầu (bắt đầu từ 0). |
| `page_size` | int32 | Có | Số lượng ID sản phẩm trả về mỗi trang (tối đa 100). |
| `item_status` | string | Có | Trạng thái: `NORMAL` (đang bán), `BANNED` (bị khóa vi phạm), `UNLIST` (đang ẩn). |

### Lệnh cURL mẫu:
```bash
curl -X GET "https://partner.shopeemobile.com/api/v2/product/get_item_list?partner_id=123456&timestamp=1700000000&access_token=c71a39d892ef65a43b1234567890abcd&shop_id=98765432&sign=calculated_sign_here&offset=0&page_size=100&item_status=NORMAL" \
  -H "Content-Type: application/json"
```

### Phản hồi mẫu (JSON):
```json
{
  "error": "",
  "message": "",
  "request_id": "...",
  "response": {
    "item": [
      {
        "item_id": 10928374,
        "item_status": "NORMAL",
        "update_time": 1700000000
      }
    ],
    "total_count": 150,
    "has_next_page": true,
    "next_offset": 100
  }
}
```

---

## 2. Lấy Thông Tin Cơ Bản Sản Phẩm (Get Item Base Info)

- **Tên Endpoint**: `v2.product.get_item_base_info`
- **Đường dẫn**: `GET /api/v2/product/get_item_base_info`
- **Loại API**: Shop API

### Tham số URL (Query Parameters):
| Tham Số | Kiểu Dữ Liệu | Bắt Buộc | Mô Tả |
| :--- | :--- | :--- | :--- |
| `item_id_list` | string | Có | Danh sách các `item_id` cách nhau bởi dấu phẩy `,` (tối đa 50 ID/lần). |

### Lệnh cURL mẫu:
```bash
curl -X GET "https://partner.shopeemobile.com/api/v2/product/get_item_base_info?partner_id=123456&timestamp=1700000000&access_token=c71a39d892ef65a43b1234567890abcd&shop_id=98765432&sign=calculated_sign_here&item_id_list=10928374,10928375" \
  -H "Content-Type: application/json"
```

### Phản hồi mẫu (JSON):
```json
{
  "error": "",
  "message": "",
  "request_id": "...",
  "response": {
    "item_list": [
      {
        "item_id": 10928374,
        "category_id": 100012,
        "item_name": "Bình Giữ Nhiệt Inox 316 Cao Cấp 800ml",
        "item_sku": "BINH-GIU-NHIET-800",
        "item_status": "NORMAL",
        "has_model": true,
        "weight": "0.45",
        "dimension": {
          "package_length": 10,
          "package_width": 10,
          "package_height": 25
        },
        "price_info": [
          {
            "currency": "VND",
            "original_price": 400000.00,
            "current_price": 350000.00
          }
        ]
      }
    ]
  }
}
```

---

## 3. Lấy Danh Sách Biến Thể & Tồn Kho SKU (Get Model List)

- **Tên Endpoint**: `v2.product.get_model_list`
- **Đường dẫn**: `GET /api/v2/product/get_model_list`
- **Loại API**: Shop API

### Lệnh cURL mẫu:
```bash
curl -X GET "https://partner.shopeemobile.com/api/v2/product/get_model_list?partner_id=123456&timestamp=1700000000&access_token=c71a39d892ef65a43b1234567890abcd&shop_id=98765432&sign=calculated_sign_here&item_id=10928374" \
  -H "Content-Type: application/json"
```

### Phản hồi mẫu (JSON):
```json
{
  "error": "",
  "message": "",
  "request_id": "...",
  "response": {
    "tier_variation": [
      {
        "name": "Màu Sắc",
        "options": ["Bạc Metal", "Đen Nhám"]
      }
    ],
    "model": [
      {
        "model_id": 556677,
        "model_sku": "BINH-800-BAC",
        "model_name": "Bạc Metal",
        "tier_index": [0],
        "price_info": [
          {
            "original_price": 400000.00,
            "current_price": 350000.00
          }
        ],
        "stock_info_v2": {
          "summary_info": {
            "total_available_stock": 85,
            "total_reserved_stock": 15
          }
        }
      }
    ]
  }
}
```

---

## 4. Lấy Cây Ngành Hàng Shopee (Get Category)

- **Tên Endpoint**: `v2.product.get_category`
- **Đường dẫn**: `GET /api/v2/product/get_category`
- **Loại API**: Shop API

### Lệnh cURL mẫu:
```bash
curl -X GET "https://partner.shopeemobile.com/api/v2/product/get_category?partner_id=123456&timestamp=1700000000&access_token=c71a39d892ef65a43b1234567890abcd&shop_id=98765432&sign=calculated_sign_here&language=vi" \
  -H "Content-Type: application/json"
```

---

## 5. Cập Nhật Tồn Kho & Giá Bán (Update Stock & Price)

### Cập nhật tồn kho sản phẩm/biến thể:
```bash
curl -X POST "https://partner.shopeemobile.com/api/v2/product/update_stock?partner_id=123456&timestamp=1700000000&access_token=c71a39d892ef65a43b1234567890abcd&shop_id=98765432&sign=calculated_sign_here" \
  -H "Content-Type: application/json" \
  -d '{
    "item_id": 10928374,
    "stock_list": [
      {
        "model_id": 556677,
        "normal_stock": 120
      }
    ]
  }'
```

### Cập nhật giá bán sản phẩm/biến thể:
```bash
curl -X POST "https://partner.shopeemobile.com/api/v2/product/update_price?partner_id=123456&timestamp=1700000000&access_token=c71a39d892ef65a43b1234567890abcd&shop_id=98765432&sign=calculated_sign_here" \
  -H "Content-Type: application/json" \
  -d '{
    "item_id": 10928374,
    "price_list": [
      {
        "model_id": 556677,
        "original_price": 380000.00
      }
    ]
  }'
```
