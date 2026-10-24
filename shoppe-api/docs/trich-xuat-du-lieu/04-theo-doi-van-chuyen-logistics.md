# 04. Hướng Dẫn Vận Chuyển, Theo Dõi Đơn & In Phiếu Giao (Logistics & Tracking)

Tài liệu này hướng dẫn cách trích xuất hành trình vận chuyển của kiện hàng, lấy mã vận đơn và tự động hóa quy trình in phiếu giao hàng (Air Waybill - AWB).

---

## 1. Hệ Thống Đơn Vị Vận Chuyển (Logistics Channels)

Mỗi gian hàng Shopee được liên kết với nhiều kênh vận chuyển khác nhau (Shopee Xpress - SPX, Giao Hàng Tiết Kiệm - GHTK, Giao Hàng Nhanh - GHN, J&T Express, Viettel Post, Ninja Van...).

### Lấy danh sách kênh vận chuyển của Shop:
- **API**: `GET /api/v2/logistics/get_channel_list`
- **Dữ liệu trả về**: Danh sách các `logistics_channel_id`, tên kênh (`logistics_channel_name`), trạng thái bật/tắt và cấu hình hỗ trợ Thu hộ COD (`cod_enabled`).

---

## 2. Quy Trình Chuẩn Bị Hàng & Lấy Mã Vận Đơn (Fulfillment Flow)

Để xử lý một đơn hàng từ trạng thái `READY_TO_SHIP` sang có mã vận đơn:

```
[get_shipping_parameter]  -->  [ship_order]  -->  [get_tracking_info / Webhook Code 4]
(Lấy khung giờ bưu tá lấy)     (Xác nhận giao)     (Nhận mã vận đơn tracking_no)
```

1. **Lấy tham số giao hàng (`get_shipping_parameter`)**:
   - Xác định kênh vận chuyển yêu cầu Bưu tá đến lấy hàng tại nhà (`pickup`) hay Shop tự mang ra bưu cục gửi (`dropoff`).
2. **Xác nhận giao hàng (`ship_order`)**:
   - Gửi yêu cầu chuẩn bị hàng. Sau khi gọi API này, đơn hàng sẽ chuyển sang trạng thái `PROCESSED`.
3. **Nhận mã vận đơn (`tracking_no`)**:
   - Shopee sẽ tạo mã vận đơn định danh cho kiện hàng.
   - Bạn có thể nhận mã này tức thì qua Webhook Push Code 4 hoặc gọi API `get_tracking_info`.

---

## 3. Trích Xuất Hành Trình Vận Chuyển (`get_tracking_info`)

- **API**: `GET /api/v2/logistics/get_tracking_info`
- **Lệnh cURL tra cứu vận đơn**:
```bash
curl -X GET "https://partner.shopeemobile.com/api/v2/logistics/get_tracking_info?partner_id=123456&timestamp=1700000000&access_token=your_token&shop_id=98765432&sign=calculated_sign_here&order_sn=261023ABCD1234" \
  -H "Content-Type: application/json"
```

### Cấu trúc phản hồi lịch sử di chuyển (Milestone History):
```json
{
  "error": "",
  "message": "",
  "request_id": "...",
  "response": {
    "logistics_status": "LOGISTICS_DELIVERED",
    "tracking_number": "SPXVN03928172910B",
    "tracking_info": [
      {
        "update_time": 1700020000,
        "description": "Giao hàng thành công. Người nhận: Lê Văn B",
        "logistics_status": "LOGISTICS_DELIVERED"
      },
      {
        "update_time": 1700012000,
        "description": "Bưu tá đang phát hàng đến địa chỉ người nhận",
        "logistics_status": "LOGISTICS_OUT_FOR_DELIVERY"
      },
      {
        "update_time": 1700005000,
        "description": "Kiện hàng đã đến kho phân loại Củ Chi SOC",
        "logistics_status": "LOGISTICS_IN_TRANSIT"
      },
      {
        "update_time": 1700001000,
        "description": "Bưu tá đã lấy hàng thành công từ người bán",
        "logistics_status": "LOGISTICS_PICKED_UP"
      }
    ]
  }
}
```

---

## 4. Tự Động Hóa In Phiếu Giao Hàng (Air Waybill - AWB)

Shopee hỗ trợ xuất phiếu giao hàng dạng PDF định dạng chuẩn in nhiệt khổ A6 (100x150 mm) qua chu trình 3 bước bất đồng bộ:

1. **Tạo yêu cầu in (`create_shipping_document`)**:
   - Gửi danh sách các `order_sn` cần in tem.
2. **Kiểm tra trạng thái tạo file (`get_shipping_document_result`)**:
   - Chờ hệ thống Shopee render xong file PDF.
3. **Tải file PDF (`download_shipping_document`)**:
   - Tải luồng file nhị phân (binary PDF stream) để chuyển tiếp trực tiếp vào máy in nhiệt tem nhãn của kho hàng.

