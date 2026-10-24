# Tham Khảo API: Kho Hàng Shopee & Quản Lý Hoàn Tất (Fulfillment by Shopee - FBS / SBS)

Tài liệu này cung cấp chi tiết đặc tả kỹ thuật và câu lệnh **cURL** cho phân hệ Kho dịch vụ Shopee (Shopee Business Services - SBS) và Hoàn tất đơn hàng bởi Shopee (Fulfillment by Shopee - FBS).

---

## 1. Kiểm Tra Thông Tin Kho Hàng Đã Liên Kết (Get Bound Warehouse Info)

Endpoint này trả về mã định danh và thông tin khu vực kho Shopee được gán cho gian hàng.

- **Tên Endpoint**: `v2.sbs.get_bound_whs_info`
- **Đường dẫn**: `GET /api/v2/sbs/get_bound_whs_info`
- **Loại API**: Shop API

### Lệnh cURL mẫu:
```bash
curl -X GET "https://partner.shopeemobile.com/api/v2/sbs/get_bound_whs_info?partner_id=123456&timestamp=1700000000&access_token=c71a39d892ef65a43b1234567890abcd&shop_id=98765432&sign=calculated_sign_here" \
  -H "Content-Type: application/json"
```

---

## 2. Kiểm Tra Tồn Kho Thực Tế Tại Kho Shopee (Get Current Inventory)

Endpoint này lấy danh sách số lượng tồn kho khả dụng, tồn kho bị khóa do đang có đơn hàng, và tồn kho lỗi đang lưu giữ tại trung tâm hoàn tất đơn hàng của Shopee.

- **Tên Endpoint**: `v2.sbs.get_current_inventory`
- **Đường dẫn**: `GET /api/v2/sbs/get_current_inventory`
- **Loại API**: Shop API

### Lệnh cURL mẫu:
```bash
curl -X GET "https://partner.shopeemobile.com/api/v2/sbs/get_current_inventory?partner_id=123456&timestamp=1700000000&access_token=c71a39d892ef65a43b1234567890abcd&shop_id=98765432&sign=calculated_sign_here&page_no=1&page_size=50" \
  -H "Content-Type: application/json"
```

### Phản hồi mẫu (JSON):
```json
{
  "error": "",
  "message": "",
  "request_id": "76fa9021eebb4401",
  "response": {
    "inventory_list": [
      {
        "item_id": 1122334455,
        "model_id": 55667788,
        "item_name": "Áo Thun Nam Thể Thao Shopee FBS",
        "model_sku": "TSHIRT-BLK-L",
        "available_stock": 420,
        "reserved_stock": 35,
        "defective_stock": 2,
        "warehouse_id": "VN_WH_NORTH_01"
      }
    ],
    "total_count": 150
  }
}
```

---

## 3. Lịch Sử Biến Động Kho Hàng (Get Stock Movement)

Endpoint này theo dõi toàn bộ lịch sử xuất - nhập - tồn, xuất kho giao cho đơn hàng hoặc điều chuyển nội bộ giữa các trung tâm phân loại của Shopee.

- **Tên Endpoint**: `v2.sbs.get_stock_movement`
- **Đường dẫn**: `GET /api/v2/sbs/get_stock_movement`
- **Loại API**: Shop API

### Lệnh cURL mẫu:
```bash
curl -X GET "https://partner.shopeemobile.com/api/v2/sbs/get_stock_movement?partner_id=123456&timestamp=1700000000&access_token=c71a39d892ef65a43b1234567890abcd&shop_id=98765432&sign=calculated_sign_here&model_id=55667788&page_no=1&page_size=20" \
  -H "Content-Type: application/json"
```

---

## 4. Báo Cáo Tuổi Thọ Tồn Kho & Hạn Sử Dụng (Get Stock Aging & Expiry Report)

Dành cho các mặt hàng thực phẩm, mỹ phẩm và hàng FMCG có ngày hết hạn hoặc hàng lưu kho lâu ngày chịu phí lưu kho quá hạn:

### 4.1. Báo cáo hạn sử dụng (Get Expiry Report):
```bash
curl -X GET "https://partner.shopeemobile.com/api/v2/sbs/get_expiry_report?partner_id=123456&timestamp=1700000000&access_token=c71a39d892ef65a43b1234567890abcd&shop_id=98765432&sign=calculated_sign_here&page_no=1&page_size=50" \
  -H "Content-Type: application/json"
```

### 4.2. Báo cáo tuổi thọ hàng tồn kho (Get Stock Aging):
```bash
curl -X GET "https://partner.shopeemobile.com/api/v2/sbs/get_stock_aging?partner_id=123456&timestamp=1700000000&access_token=c71a39d892ef65a43b1234567890abcd&shop_id=98765432&sign=calculated_sign_here&page_no=1&page_size=50" \
  -H "Content-Type: application/json"
```
*(Giúp người bán phát hiện các sản phẩm lưu kho quá 60 - 90 ngày để kịp thời giảm giá hoặc tạo Flash sale xả hàng)*

