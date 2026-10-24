# 02. Bảng Tra Cứu Các Mã Sự Kiện Push (Event Codes Dictionary)

Khi có sự kiện phát sinh, Shopee sẽ gửi một request `POST` đến Callback URL của bạn. Trường `code` trong payload JSON quy định loại sự kiện.

---

## 1. Bảng Tra Cứu Toàn Bộ Các Mã Sự Kiện (`code`)

| Mã Code | Tên Sự Kiện | Ý Nghĩa Nghiệp Vụ | Tần Suất & Mức Độ Ưu Tiên |
| :---: | :--- | :--- | :--- |
| **`1`** | **Shop Authorization Push** | Có một gian hàng Shopee vừa hoàn tất ủy quyền cho ứng dụng. | Rất quan trọng (Lưu token ban đầu) |
| **`2`** | **Shop Deauthorization Push** | Gian hàng đã chủ động hủy cấp quyền ứng dụng trên Kênh Người Bán. | Quan trọng (Dừng tiến trình sync của shop này) |
| **`3`** | **Order Status Update Push** | Trạng thái đơn hàng thay đổi (Có đơn mới `READY_TO_SHIP`, Đơn bị hủy `CANCELLED`, Đơn hoàn tất `COMPLETED`). | **CỰC KỲ QUAN TRỌNG** (Đồng bộ tồn kho & đơn hàng realtime) |
| **`4`** | **TrackingNo Push** | Đã tạo thành công mã vận đơn (`tracking_no`) cho đơn hàng. | Quan trọng (In tem & cập nhật vận chuyển) |
| **`6`** | **Banned Item Push** | Sản phẩm bị Shopee tạm khóa, xóa hoặc phạt vi phạm chính sách đăng bán. | Cảnh báo quản trị viên |
| **`8`** | **Reserved Stock Change Push** | Tồn kho dự trữ thay đổi (do chạy Flash Sale hoặc chương trình khuyến mãi Shopee). | Quan trọng (Điều chỉnh kho đa sàn) |
| **`10`** | **Open API Expiry Push** | Quyền ủy quyền 30 ngày của Shop sắp hết hạn. | Nhắc nhở người bán xác nhận gia hạn |
| **`15`** | **Return Updates Push** | Khách hàng vừa gửi yêu cầu Trả hàng / Hoàn tiền mới hoặc Shopee đã phán quyết. | Xử lý khiếu nại CSKH |

---

## 2. Cấu Trúc Payload Mẫu Cho Từng Sự Kiện Tiêu Biểu

### Sự Kiện Code 3: Trạng Thái Đơn Hàng Thay Đổi (`order_status_push`)
```json
{
  "shop_id": 98765432,
  "code": 3,
  "timestamp": 1700012345,
  "data": {
    "ordersn": "261023ABCD1234",
    "status": "READY_TO_SHIP",
    "completed_scenario": "",
    "update_time": 1700012345
  }
}
```

Các giá trị khả dĩ trong `data.status`:
- `UNPAID`: Đơn vừa đặt, chờ người mua thanh toán thẻ/ví.
- `READY_TO_SHIP`: Đã thanh toán hoặc đơn COD đã duyệt, Shop cần chuẩn bị hàng.
- `PROCESSED`: Shop đã xác nhận đơn và có mã vận đơn.
- `SHIPPED`: Bưu tá đã lấy hàng, kiện đang trên đường giao.
- `COMPLETED`: Giao hàng thành công, đơn hoàn tất.
- `CANCELLED`: Đơn đã bị hủy.
- `IN_CANCEL`: Đang chờ Shop phê duyệt yêu cầu hủy từ khách.

---

### Sự Kiện Code 4: Cập Nhật Mã Vận Đơn (`tracking_no_push`)
```json
{
  "shop_id": 98765432,
  "code": 4,
  "timestamp": 1700012500,
  "data": {
    "ordersn": "261023ABCD1234",
    "tracking_no": "SPXVN0123456789"
  }
}
```

---

### Sự Kiện Code 1: Gian Hàng Cấp Quyền Thành Công (`shop_auth_push`)
```json
{
  "shop_id": 98765432,
  "code": 1,
  "timestamp": 1700000000,
  "data": {
    "shop_id_list": [98765432],
    "success": true
  }
}
```

---

### Sự Kiện Code 6: Sản Phẩm Bị Khóa Vi Phạm (`banned_item_push`)
```json
{
  "shop_id": 98765432,
  "code": 6,
  "timestamp": 1700020000,
  "data": {
    "item_id": 10928374,
    "banned_reason": "Vi phạm bản quyền hình ảnh / Thương hiệu chưa có giấy ủy quyền"
  }
}
```

