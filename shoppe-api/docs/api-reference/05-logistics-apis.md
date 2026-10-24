# Tham Khảo API: Vận Chuyển & Giao Nhận (Logistics APIs)

Tài liệu này cung cấp chi tiết đặc tả kỹ thuật và câu lệnh **cURL** cho toàn bộ các API trong phân hệ Hậu cần, Vận chuyển và In phiếu giao hàng của Shopee Open API v2.

---

## 1. Lấy Danh Sách Kênh Vận Chuyển (Get Channel List)

- **Tên Endpoint**: `v2.logistics.get_channel_list`
- **Đường dẫn**: `GET /api/v2/logistics/get_channel_list`
- **Loại API**: Shop API

### Lệnh cURL mẫu:
```bash
curl -X GET "https://partner.shopeemobile.com/api/v2/logistics/get_channel_list?partner_id=123456&timestamp=1700000000&access_token=c71a39d892ef65a43b1234567890abcd&shop_id=98765432&sign=calculated_sign_here" \
  -H "Content-Type: application/json"
```

### Phản hồi mẫu (JSON):
```json
{
  "error": "",
  "message": "",
  "request_id": "...",
  "response": {
    "logistics_channel_list": [
      {
        "logistics_channel_id": 5001,
        "logistics_channel_name": "SPX Express",
        "enabled": true,
        "cod_enabled": true,
        "fee_type": "SIZE_SELECTION"
      },
      {
        "logistics_channel_id": 5002,
        "logistics_channel_name": "Giao Hàng Tiết Kiệm",
        "enabled": true,
        "cod_enabled": true,
        "fee_type": "WEIGHT"
      }
    ]
  }
}
```

---

## 2. Xác Nhận Giao Hàng & Chuẩn Bị Hàng (Ship Order)

- **Tên Endpoint**: `v2.logistics.ship_order`
- **Đường dẫn**: `POST /api/v2/logistics/ship_order`
- **Loại API**: Shop API

### Lệnh cURL mẫu khi chọn Bưu tá đến lấy hàng tại kho (`pickup`):
```bash
curl -X POST "https://partner.shopeemobile.com/api/v2/logistics/ship_order?partner_id=123456&timestamp=1700000000&access_token=c71a39d892ef65a43b1234567890abcd&shop_id=98765432&sign=calculated_sign_here" \
  -H "Content-Type: application/json" \
  -d '{
    "order_sn": "261023ABCD1234",
    "pickup": {
      "address_id": 1234567,
      "pickup_time_id": "slot_morning_20261024"
    }
  }'
```

### Lệnh cURL mẫu khi Shop tự mang ra bưu cục gửi (`dropoff`):
```bash
curl -X POST "https://partner.shopeemobile.com/api/v2/logistics/ship_order?partner_id=123456&timestamp=1700000000&access_token=c71a39d892ef65a43b1234567890abcd&shop_id=98765432&sign=calculated_sign_here" \
  -H "Content-Type: application/json" \
  -d '{
    "order_sn": "261023ABCD1234",
    "dropoff": {
      "branch_id": 0,
      "sender_real_name": "Kho Tổng Shopee VN"
    }
  }'
```

---

## 3. Lấy Lộ Trình & Mã Vận Đơn (Get Tracking Info)

- **Tên Endpoint**: `v2.logistics.get_tracking_info`
- **Đường dẫn**: `GET /api/v2/logistics/get_tracking_info`
- **Loại API**: Shop API

### Lệnh cURL mẫu:
```bash
curl -X GET "https://partner.shopeemobile.com/api/v2/logistics/get_tracking_info?partner_id=123456&timestamp=1700000000&access_token=c71a39d892ef65a43b1234567890abcd&shop_id=98765432&sign=calculated_sign_here&order_sn=261023ABCD1234" \
  -H "Content-Type: application/json"
```

### Phản hồi mẫu (JSON):
```json
{
  "error": "",
  "message": "",
  "request_id": "...",
  "response": {
    "logistics_status": "LOGISTICS_IN_TRANSIT",
    "tracking_number": "SPXVN0123456789",
    "tracking_info": [
      {
        "update_time": 1700010000,
        "description": "Bưu tá đã lấy hàng thành công từ kho người bán",
        "logistics_status": "LOGISTICS_PICKED_UP"
      }
    ]
  }
}
```

---

## 4. Tạo & Tải Phiếu Giao Hàng AWB (Air Waybill Document)

### Bước 1: Khởi tạo tác vụ tạo file in nhiệt (`create_shipping_document`):
```bash
curl -X POST "https://partner.shopeemobile.com/api/v2/logistics/create_shipping_document?partner_id=123456&timestamp=1700000000&access_token=c71a39d892ef65a43b1234567890abcd&shop_id=98765432&sign=calculated_sign_here" \
  -H "Content-Type: application/json" \
  -d '{
    "order_list": [
      { "order_sn": "261023ABCD1234" }
    ],
    "shipping_document_type": "THERMAL_AIR_WAYBILL"
  }'
```

### Bước 2: Kiểm tra trạng thái render file PDF (`get_shipping_document_result`):
```bash
curl -X POST "https://partner.shopeemobile.com/api/v2/logistics/get_shipping_document_result?partner_id=123456&timestamp=1700000000&access_token=c71a39d892ef65a43b1234567890abcd&shop_id=98765432&sign=calculated_sign_here" \
  -H "Content-Type: application/json" \
  -d '{
    "order_list": [
      { "order_sn": "261023ABCD1234" }
    ]
  }'
```

### Bước 3: Tải trực tiếp file PDF in nhiệt về máy tính (`download_shipping_document`):
```bash
curl -X GET "https://partner.shopeemobile.com/api/v2/logistics/download_shipping_document?partner_id=123456&timestamp=1700000000&access_token=c71a39d892ef65a43b1234567890abcd&shop_id=98765432&sign=calculated_sign_here&order_sn_list=261023ABCD1234" \
  --output "van_don_261023ABCD1234.pdf"
```
*(Kết quả lưu trực tiếp thành file `van_don_261023ABCD1234.pdf` khổ A6 chuẩn 100x150 mm).*
