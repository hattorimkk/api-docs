# Tham Khảo API: Danh Mục Shop & Flash Sale Của Shop

Tài liệu này cung cấp chi tiết đặc tả kỹ thuật và câu lệnh **cURL** cho hai phân hệ quan trọng: **Danh mục riêng của Shop (`v2.shop_category`)** và **Flash Sale của Shop (`v2.shop_flash_sale`)**.

---

## PHẦN 1: QUẢN LÝ DANH MỤC RIÊNG CỦA SHOP (Shop Category)

Khác với ngành hàng chung của Shopee (Platform Categories), Danh mục của Shop là các bộ sưu tập hoặc nhóm sản phẩm do người bán tự tổ chức trong gian hàng (ví dụ: "Hàng Mới Về 2026", "Top Bán Chạy", "Xả Kho Đón Hè").

### 1.1. Lấy Danh Sách Danh Mục Shop (Get Shop Category List)
- **Endpoint**: `v2.shop_category.get_shop_category_list`
- **Đường dẫn**: `GET /api/v2/shop_category/get_shop_category_list`
- **Loại API**: Shop API

```bash
curl -X GET "https://partner.shopeemobile.com/api/v2/shop_category/get_shop_category_list?partner_id=123456&timestamp=1700000000&access_token=c71a39d892ef65a43b1234567890abcd&shop_id=98765432&sign=calculated_sign_here&page_no=1&page_size=20" \
  -H "Content-Type: application/json"
```

### 1.2. Thêm Danh Mục Shop Mới (Add Shop Category)
- **Endpoint**: `v2.shop_category.add_shop_category`
- **Đường dẫn**: `POST /api/v2/shop_category/add_shop_category`

```bash
curl -X POST "https://partner.shopeemobile.com/api/v2/shop_category/add_shop_category?partner_id=123456&timestamp=1700000000&access_token=c71a39d892ef65a43b1234567890abcd&shop_id=98765432&sign=calculated_sign_here" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Bộ Sưu Tập Mùa Hè 2026",
    "sort_weight": 10
  }'
```

### 1.3. Thêm Sản Phẩm Vào Danh Mục Shop (Add Item List)
- **Endpoint**: `v2.shop_category.add_item_list`
- **Đường dẫn**: `POST /api/v2/shop_category/add_item_list`

```bash
curl -X POST "https://partner.shopeemobile.com/api/v2/shop_category/add_item_list?partner_id=123456&timestamp=1700000000&access_token=c71a39d892ef65a43b1234567890abcd&shop_id=98765432&sign=calculated_sign_here" \
  -H "Content-Type: application/json" \
  -d '{
    "shop_category_id": 105522,
    "item_list": [1122334455, 1122334456]
  }'
```

### 1.4. Lấy Danh Sách Sản Phẩm Thuộc Danh Mục (Get Item List)
- **Endpoint**: `v2.shop_category.get_item_list`
- **Đường dẫn**: `GET /api/v2/shop_category/get_item_list`

```bash
curl -X GET "https://partner.shopeemobile.com/api/v2/shop_category/get_item_list?partner_id=123456&timestamp=1700000000&access_token=c71a39d892ef65a43b1234567890abcd&shop_id=98765432&sign=calculated_sign_here&shop_category_id=105522&page_no=1&page_size=50" \
  -H "Content-Type: application/json"
```

---

## PHẦN 2: QUẢN LÝ FLASH SALE CỦA SHOP (In-Shop Flash Sale)

Flash Sale của Shop là chương trình giảm giá sốc có giới hạn thời gian (theo từng khung giờ vàng) hiển thị trực tiếp trên trang chủ gian hàng của bạn.

### 2.1. Lấy Khung Giờ Flash Sale Khả Dụng (Get Time Slot ID)
- **Endpoint**: `v2.shop_flash_sale.get_time_slot_id`
- **Đường dẫn**: `GET /api/v2/shop_flash_sale/get_time_slot_id`
- **Loại API**: Shop API

```bash
curl -X GET "https://partner.shopeemobile.com/api/v2/shop_flash_sale/get_time_slot_id?partner_id=123456&timestamp=1700000000&access_token=c71a39d892ef65a43b1234567890abcd&shop_id=98765432&sign=calculated_sign_here" \
  -H "Content-Type: application/json"
```

### 2.2. Lấy Tiêu Chí & Điều Kiện Sản Phẩm (Get Item Criteria)
- **Endpoint**: `v2.shop_flash_sale.get_item_criteria`
- **Đường dẫn**: `GET /api/v2/shop_flash_sale/get_item_criteria`

```bash
curl -X GET "https://partner.shopeemobile.com/api/v2/shop_flash_sale/get_item_criteria?partner_id=123456&timestamp=1700000000&access_token=c71a39d892ef65a43b1234567890abcd&shop_id=98765432&sign=calculated_sign_here" \
  -H "Content-Type: application/json"
```

### 2.3. Khởi Tạo Chương Trình Flash Sale Mới (Create Shop Flash Sale)
- **Endpoint**: `v2.shop_flash_sale.create_shop_flash_sale`
- **Đường dẫn**: `POST /api/v2/shop_flash_sale/create_shop_flash_sale`

```bash
curl -X POST "https://partner.shopeemobile.com/api/v2/shop_flash_sale/create_shop_flash_sale?partner_id=123456&timestamp=1700000000&access_token=c71a39d892ef65a43b1234567890abcd&shop_id=98765432&sign=calculated_sign_here" \
  -H "Content-Type: application/json" \
  -d '{
    "timeslot_id": 992201,
    "items": [
      {
        "item_id": 1122334455,
        "models": [
          {
            "model_id": 55667788,
            "input_promo_price": 129000,
            "campaign_stock": 100,
            "purchase_limit": 2
          }
        ]
      }
    ]
  }'
```

### 2.4. Lấy Danh Sách Chương Trình Flash Sale Của Shop (Get Shop Flash Sale List)
- **Endpoint**: `v2.shop_flash_sale.get_shop_flash_sale_list`
- **Đường dẫn**: `GET /api/v2/shop_flash_sale/get_shop_flash_sale_list`

```bash
curl -X GET "https://partner.shopeemobile.com/api/v2/shop_flash_sale/get_shop_flash_sale_list?partner_id=123456&timestamp=1700000000&access_token=c71a39d892ef65a43b1234567890abcd&shop_id=98765432&sign=calculated_sign_here&type=1&page_size=20" \
  -H "Content-Type: application/json"
```
*(Tham số `type`: 1: Đang diễn ra, 2: Sắp diễn ra, 3: Đã kết thúc)*

