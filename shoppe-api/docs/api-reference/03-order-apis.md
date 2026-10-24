# Tham Khảo API: Quản Lý Đơn Hàng (Order APIs)

Tài liệu này cung cấp chi tiết đặc tả kỹ thuật và câu lệnh **cURL** cho toàn bộ các API trong phân hệ Quản lý Đơn hàng của Shopee Open API v2.

---

## 1. Lấy Danh Sách Đơn Hàng (Get Order List)

- **Tên Endpoint**: `v2.order.get_order_list`
- **Đường dẫn**: `GET /api/v2/order/get_order_list`
- **Loại API**: Shop API

### Công thức tính chữ ký `sign`:
$$\text{Base String} = \text{partner\_id} + \text{"/api/v2/order/get_order_list"} + \text{timestamp} + \text{access\_token} + \text{shop\_id}$$

### Tham số URL (Query Parameters):
| Tham Số | Kiểu Dữ Liệu | Bắt Buộc | Mô Tả & Quy Tắc |
| :--- | :--- | :--- | :--- |
| `time_range_field` | string | Có | Lọc theo thời gian: `create_time` (tạo đơn) hoặc `update_time` (cập nhật). |
| `time_from` | int64 | Có | Unix timestamp bắt đầu. Khoảng cách với `time_to` $\le$ 15 ngày. |
| `time_to` | int64 | Có | Unix timestamp kết thúc. |
| `page_size` | int32 | Có | Số lượng mã đơn trả về mỗi trang (1 đến 100). |
| `cursor` | string | Không | Con trỏ trang tiếp theo. Để trống cho trang đầu tiên. |
| `order_status` | string | Không | Lọc theo trạng thái: `UNPAID`, `READY_TO_SHIP`, `PROCESSED`, `SHIPPED`, `COMPLETED`, `IN_CANCEL`, `CANCELLED`, `INVOICE_PENDING`. |

### Lệnh cURL mẫu:
```bash
# Lấy danh sách 50 đơn hàng sẵn sàng giao (READY_TO_SHIP)
curl -X GET "https://partner.shopeemobile.com/api/v2/order/get_order_list?partner_id=123456&timestamp=1700000000&access_token=c71a39d892ef65a43b1234567890abcd&shop_id=98765432&sign=calculated_sign_here&time_range_field=create_time&time_from=1698790400&time_to=1700000000&page_size=50&order_status=READY_TO_SHIP" \
  -H "Content-Type: application/json"
```

### Phản hồi mẫu (JSON):
```json
{
  "error": "",
  "message": "",
  "request_id": "319a0be7612f0...",
  "response": {
    "more": true,
    "next_cursor": "eyJvZmZzZXQiOjEwMH0=",
    "order_list": [
      { "order_sn": "261023ABCD1234" },
      { "order_sn": "261023ABCD5678" }
    ]
  }
}
```

---

## 2. Lấy Chi Tiết Đơn Hàng (Get Order Detail)

- **Tên Endpoint**: `v2.order.get_order_detail`
- **Đường dẫn**: `GET /api/v2/order/get_order_detail`
- **Loại API**: Shop API

### Tham số URL (Query Parameters):
| Tham Số | Kiểu Dữ Liệu | Bắt Buộc | Mô Tả |
| :--- | :--- | :--- | :--- |
| `order_sn_list` | string | Có | Danh sách mã đơn cách nhau bởi dấu phẩy `,` (tối đa 50 đơn). |
| `response_optional_fields` | string | Không | Các trường bổ sung: `buyer_user_id,buyer_username,estimated_shipping_fee,recipient_address,actual_shipping_fee,package_list,item_list,invoice_data,payment_method,note,cancel_reason,fulfillment_flag`. |

### Lệnh cURL mẫu:
```bash
curl -X GET "https://partner.shopeemobile.com/api/v2/order/get_order_detail?partner_id=123456&timestamp=1700000000&access_token=c71a39d892ef65a43b1234567890abcd&shop_id=98765432&sign=calculated_sign_here&order_sn_list=261023ABCD1234,261023ABCD5678&response_optional_fields=buyer_user_id,buyer_username,recipient_address,item_list,payment_method,actual_shipping_fee,note" \
  -H "Content-Type: application/json"
```

### Phản hồi mẫu (JSON):
```json
{
  "error": "",
  "message": "",
  "request_id": "...",
  "response": {
    "order_list": [
      {
        "order_sn": "261023ABCD1234",
        "order_status": "READY_TO_SHIP",
        "region": "VN",
        "currency": "VND",
        "cod": true,
        "total_amount": 350000.00,
        "actual_shipping_fee": 22000.00,
        "estimated_shipping_fee": 22000.00,
        "payment_method": "Cash on Delivery",
        "create_time": 1700001000,
        "update_time": 1700003000,
        "note": "Giao hàng giờ hành chính giúp mình",
        "recipient_address": {
          "name": "Nguy** V** A**",
          "phone": "098*****12",
          "full_address": "Số ** Đường **, Phường 1, Quận Bình Thạnh, TP. Hồ Chí Minh",
          "city": "Thành phố Hồ Chí Minh",
          "district": "Quận Bình Thạnh"
        },
        "item_list": [
          {
            "item_id": 10928374,
            "item_name": "Bình Giữ Nhiệt Inox 316 Cao Cấp 800ml",
            "item_sku": "BINH-GIU-NHIET-800",
            "model_id": 556677,
            "model_name": "Màu Bạc Metal",
            "model_sku": "BINH-800-BAC",
            "model_quantity_purchased": 1,
            "model_original_price": 400000.00,
            "model_discounted_price": 350000.00
          }
        ]
      }
    ]
  }
}
```

---

## 3. Lấy Danh Sách Kiện Hàng Cần Giao (Get Shipment List)

- **Tên Endpoint**: `v2.order.get_shipment_list`
- **Đường dẫn**: `GET /api/v2/order/get_shipment_list`
- **Loại API**: Shop API

### Lệnh cURL mẫu:
```bash
curl -X GET "https://partner.shopeemobile.com/api/v2/order/get_shipment_list?partner_id=123456&timestamp=1700000000&access_token=c71a39d892ef65a43b1234567890abcd&shop_id=98765432&sign=calculated_sign_here&page_size=50" \
  -H "Content-Type: application/json"
```

---

## 4. Xử Lý Yêu Cầu Hủy Đơn Của Khách (Handle Buyer Cancellation)

- **Tên Endpoint**: `v2.order.handle_buyer_cancellation`
- **Đường dẫn**: `POST /api/v2/order/handle_buyer_cancellation`
- **Loại API**: Shop API

### Lệnh cURL mẫu:
```bash
# Đồng ý hủy đơn hàng (operation: ACCEPT) hoặc Từ chối (operation: REJECT)
curl -X POST "https://partner.shopeemobile.com/api/v2/order/handle_buyer_cancellation?partner_id=123456&timestamp=1700000000&access_token=c71a39d892ef65a43b1234567890abcd&shop_id=98765432&sign=calculated_sign_here" \
  -H "Content-Type: application/json" \
  -d '{
    "order_sn": "261023ABCD1234",
    "operation": "ACCEPT"
  }'
```
