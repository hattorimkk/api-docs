# 12. Chiến Dịch & Khuyến Mại (Promotions API - 12 Endpoints)

Phân hệ Promotion API cho phép nhà bán hàng tự động hóa các chương trình tiếp thị kích cầu: tạo chương trình Giảm giá trực tiếp (Direct Discount), Flash Sale theo khung giờ vàng và cài đặt các sản phẩm áp dụng ưu đãi qua API.

---

## 1. Các Loại Hình Khuyến Mại Được Hỗ Trợ (Promotion Types)

| Loại khuyến mại | Mã Type | Ý nghĩa thực tế |
| :--- | :--- | :--- |
| **Direct Discount** | `DIRECT_DISCOUNT` | Giảm giá theo % hoặc số tiền cố định trực tiếp trên sản phẩm |
| **Flash Deal / Flash Sale** | `FLASH_SALE` | Giảm giá sốc trong khung giờ giới hạn với số lượng suất mua quy định |
| **Shipping Discount** | `SHIPPING_DISCOUNT` | Nhà bán hàng tài trợ một phần hoặc toàn bộ phí vận chuyển |

---

## 2. Danh Mục Các Endpoint Khuyến Mại

| Tên chức năng | Method | Endpoint Path | Mục đích |
| :--- | :--- | :--- | :--- |
| **Create Promotion Activity** | `POST` | `/promotion/202309/activities` | Khởi tạo một chiến dịch khuyến mại mới |
| **Update Promotion Activity** | `PUT` | `/promotion/202309/activities/{activity_id}` | Cập nhật thời gian bắt đầu, kết thúc hoặc tên chương trình |
| **Update Promotion Items** | `PUT` | `/promotion/202309/activities/{activity_id}/items` | Thêm, bớt sản phẩm hoặc sửa giá khuyến mại trong chiến dịch |
| **Deactivate Activity** | `POST` | `/promotion/202309/activities/{activity_id}/deactivate` | Tắt/Dừng khẩn cấp một chương trình khuyến mại đang chạy |
| **Get Activity Details** | `GET` | `/promotion/202309/activities/{activity_id}` | Xem chi tiết cài đặt và danh sách sản phẩm trong khuyến mại |
| **Search Activities** | `POST` | `/promotion/202309/activities/search` | Tìm kiếm và phân trang danh sách các chiến dịch khuyến mại |

---

## 3. Tạo Mới Một Chương Trình Flash Sale Qua API

- **Endpoint**: `/promotion/202309/activities`
- **Method**: `POST`

#### Mẫu cURL

```bash
curl -X POST \
  'https://open-api.tiktokglobalshop.com/promotion/202309/activities?app_key=YOUR_APP_KEY&timestamp=1792827493&shop_cipher=YOUR_SHOP_CIPHER&sign=CALCULATED_SIGN' \
  -H 'x-tts-access-token: YOUR_ACCESS_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{
    "title": "Flash Sale Khung Giờ Vàng 20h - 22h",
    "activity_type": "FLASH_SALE",
    "begin_time": 1729515600,
    "end_time": 1729522800,
    "product_level": "VARIATION",
    "items": [
      {
        "id": "1729482910482910",
        "skus": [
          {
            "id": "1729482910482910",
            "promotion_price": {
              "amount": "99000",
              "currency": "VND"
            },
            "quantity_limit": 50,
            "user_limit": 1
          }
        ]
      }
    ]
  }'
```

- `promotion_price`: Giá bán trong khung giờ flash sale (giảm từ 149.000 đ xuống 99.000 đ).
- `quantity_limit`: Giới hạn tổng số lượng xuất bán với giá ưu đãi (50 chiếc).
- `user_limit`: Giới hạn mỗi người mua tối đa 1 chiếc để tránh đầu cơ gom hàng.

