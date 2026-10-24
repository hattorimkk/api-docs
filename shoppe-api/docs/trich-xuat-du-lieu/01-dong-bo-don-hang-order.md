# 01. Hướng Dẫn Trích Xuất & Đồng Bộ Đơn Hàng (Order Data Extraction)

Đơn hàng là trung tâm dữ liệu quan trọng nhất trong hệ thống bán hàng đa kênh. Tài liệu này hướng dẫn chi tiết chiến lược kỹ thuật để lấy toàn bộ dữ liệu đơn hàng sạch, chính xác và tối ưu hiệu năng.

---

## 1. Chiến Lược 2 Bước (Two-Step Retrieval Pattern)

Shopee Open Platform thiết kế việc trích xuất đơn hàng theo mô hình 2 bước nhằm tối ưu tải máy chủ:

```
[Hệ Thống Của Bạn]                                             [Shopee Server]
        |                                                              |
        |  Bước 1: get_order_list (cursor, time_from, time_to)         |
        |------------------------------------------------------------->|
        |  Trả về: Danh sách mã đơn [order_sn_1, order_sn_2, ...]     |
        |<-------------------------------------------------------------|
        |                                                              |
        |  Bước 2: get_order_detail (Gom cụm tối đa 50 mã đơn/lần)     |
        |------------------------------------------------------------->|
        |  Trả về: Chi tiết sản phẩm, giá tiền, địa chỉ, trạng thái    |
        |<-------------------------------------------------------------|
```

- **Bước 1 (`v2.order.get_order_list`)**: Quét nhanh để lấy danh sách mã định danh đơn hàng (`order_sn`). API này trả về kết quả rất nhẹ và nhanh.
- **Bước 2 (`v2.order.get_order_detail`)**: Gom các mã đơn hàng thành từng mẻ (batch) **tối đa 50 đơn** để lấy chi tiết từng sản phẩm, đơn giá, địa chỉ và thuế.

---

## 2. Bước 1: Quét Danh Sách Mã Đơn Hàng (`get_order_list`)

- **Đường dẫn API**: `GET /api/v2/order/get_order_list`
- **Phương thức**: `GET`

### Các tham số quan trọng:
| Tham số | Kiểu | Bắt buộc | Mô tả & Lưu ý |
| :--- | :--- | :--- | :--- |
| `time_range_field` | string | Có | Lọc theo thời gian nào: `create_time` (thời gian tạo đơn) hoặc `update_time` (thời gian trạng thái đơn cập nhật). |
| `time_from` | int | Có | Mốc bắt đầu (Unix timestamp tính bằng giây). |
| `time_to` | int | Có | Mốc kết thúc (Unix timestamp tính bằng giây). **Khoảng cách tối đa giữa time_from và time_to là 15 ngày!** |
| `page_size` | int | Có | Số lượng mã đơn trả về mỗi trang (tối đa 100). |
| `cursor` | string | Không | Con trỏ phân trang. Trang đầu tiên để chuỗi rỗng `""`. Các trang tiếp theo truyền giá trị `next_cursor` nhận được từ lần gọi trước. |
| `order_status` | string | Không | Lọc theo trạng thái cụ thể: `UNPAID`, `READY_TO_SHIP`, `PROCESSED`, `SHIPPED`, `COMPLETED`, `IN_CANCEL`, `CANCELLED`, `INVOICE_PENDING`. Nếu muốn lấy tất cả, không cần truyền tham số này. |

### Lệnh cURL quét danh sách đơn:
```bash
curl -X GET "https://partner.shopeemobile.com/api/v2/order/get_order_list?partner_id=123456&timestamp=1700000000&access_token=your_token&shop_id=98765432&sign=calculated_sign_here&time_range_field=create_time&time_from=1698790400&time_to=1700000000&page_size=100&cursor=" \
  -H "Content-Type: application/json"
```

### Cấu trúc phản hồi:
```json
{
  "error": "",
  "message": "",
  "request_id": "...",
  "response": {
    "more": true,
    "next_cursor": "eyJvZmZzZXQiOjEwMH0=",
    "order_list": [
      { "order_sn": "261023ABCD001" },
      { "order_sn": "261023ABCD002" }
    ]
  }
}
```

---

## 3. Bước 2: Truy Vấn Chi Tiết Đơn Hàng (`get_order_detail`)

- **Đường dẫn API**: `GET /api/v2/order/get_order_detail`
- **Phương thức**: `GET`

### Các tham số quan trọng:
| Tham số | Kiểu | Bắt buộc | Mô tả & Lưu ý |
| :--- | :--- | :--- | :--- |
| `order_sn_list` | string | Có | Danh sách các mã đơn cách nhau bởi dấu phẩy `,` (ví dụ: `261023ABCD001,261023ABCD002`). **Tối đa 50 đơn/lần gọi**. |
| `response_optional_fields` | string | Không | Danh sách các trường thông tin bổ sung cần lấy, cách nhau bởi dấu phẩy. Mặc định Shopee chỉ trả các trường tối giản. |

> [!IMPORTANT]
> **Danh sách các trường `response_optional_fields` khuyến nghị luôn truyền đầy đủ:**
> `buyer_user_id,buyer_username,estimated_shipping_fee,recipient_address,actual_shipping_fee,package_list,item_list,invoice_data,payment_method,note,cancel_reason,fulfillment_flag`

### Lệnh cURL lấy chi tiết tối đa 50 đơn hàng cùng lúc:
```bash
curl -X GET "https://partner.shopeemobile.com/api/v2/order/get_order_detail?partner_id=123456&timestamp=1700000000&access_token=your_token&shop_id=98765432&sign=calculated_sign_here&order_sn_list=261023ABCD001,261023ABCD002&response_optional_fields=buyer_user_id,buyer_username,recipient_address,item_list,payment_method,actual_shipping_fee,note,cancel_reason" \
  -H "Content-Type: application/json"
```

### Cấu trúc dữ liệu chi tiết trả về:
```json
{
  "error": "",
  "message": "",
  "request_id": "...",
  "response": {
    "order_list": [
      {
        "order_sn": "261023ABCD001",
        "order_status": "READY_TO_SHIP",
        "create_time": 1700001234,
        "update_time": 1700002345,
        "total_amount": 250000,
        "currency": "VND",
        "payment_method": "ShopeePay",
        "actual_shipping_fee": 18000,
        "recipient_address": {
          "name": "Ngu*** A**",
          "phone": "09****123",
          "city": "Thành phố Hồ Chí Minh",
          "district": "Quận 1",
          "full_address": "Số ** Đường **, Phường Bến Nghé, Quận 1"
        },
        "item_list": [
          {
            "item_id": 12345678,
            "item_name": "Áo Thun Unisex Cotton 100%",
            "item_sku": "AO-THUN-01",
            "model_id": 887766,
            "model_name": "Màu Đen, Size L",
            "model_sku": "AO-THUN-01-DEN-L",
            "model_quantity_purchased": 2,
            "model_original_price": 150000,
            "model_discounted_price": 125000
          }
        ]
      }
    ]
  }
}
```

---

## 4. Chiến Lược Đồng Bộ Định Kỳ & Đồng Bộ Tăng Dần (Incremental Sync)

Để dữ liệu trong Data Warehouse luôn cập nhật mà không bị quá tải:

1. **Đồng bộ lần đầu (Initial Sync - Backfill)**:
   - Chạy script `sync_orders.py` chia nhỏ từng khung 14 ngày quét ngược về quá khứ (ví dụ: quét 6 tháng hoặc 1 năm qua).
2. **Đồng bộ tăng dần theo lịch (Incremental Sync)**:
   - Đặt cron job chạy mỗi 15 phút hoặc 30 phút một lần.
   - Sử dụng `time_range_field="update_time"`.
   - `time_from`: Thời điểm chạy thành công lần trước (trừ hao lùi lại 10 phút để phòng trễ mạng).
   - `time_to`: Thời điểm hiện tại.
   - Nhờ lọc theo `update_time`, mọi đơn hàng vừa phát sinh trạng thái mới (từ Chuẩn bị hàng $\rightarrow$ Đã giao $\rightarrow$ Hoàn tất $\rightarrow$ Hủy) đều sẽ được bắt trọn vẹn và cập nhật vào Database.
3. **Kết hợp Webhook (Thời gian thực)**:
   - Dùng Shopee Push Code 3 (`order_status_push`) để cập nhật trạng thái đơn ngay trong 1-2 giây sau khi người mua thao tác.

