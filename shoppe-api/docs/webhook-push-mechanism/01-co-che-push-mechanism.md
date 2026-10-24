# 01. Cơ Chế Bắn Tin Tự Động (Shopee Push Mechanism / Webhooks)

Tài liệu này giải thích bản chất cơ chế Webhook (Shopee gọi là **Push Mechanism**) trên Shopee Open Platform, so sánh với giải pháp Polling truyền thống và cách cấu hình để nhận thông báo thời gian thực.

---

## 1. Tại Sao Phải Sử Dụng Webhook Thay Vì Polling?

Trong các hệ thống bán hàng đa kênh (Omnichannel/ERP), khi một khách hàng đặt đơn mới trên Shopee, hệ thống của bạn cần biết ngay lập tức để trừ tồn kho trên các sàn khác (Lazada, TikTok Shop, Website) nhằm chống bán quá số lượng (overselling).

Có 2 cách tiếp cận:

```
CÁCH 1: POLLING (Thăm dò liên tục - Lạc hậu)
Ứng dụng: "Có đơn mới chưa?" -> Shopee: "Chưa"
(10 giây sau) Ứng dụng: "Có đơn mới chưa?" -> Shopee: "Chưa"
(10 giây sau) Ứng dụng: "Có đơn mới chưa?" -> Shopee: "Có 1 đơn"
==> Tiêu tốn băng thông, dễ chạm trần Rate Limit (QPS limit), độ trễ cao.

CÁCH 2: SHOPEE PUSH MECHANISM (Webhook - Hiện đại & Tối ưu)
Ứng dụng: Đứng chờ yên lặng ở Callback URL.
Shopee: Có sự kiện đơn hàng mới -> Tự động bắn HTTP POST ngay tức thì!
==> Thời gian cập nhật: Dưới 1 giây! Tiết kiệm 99% tài nguyên CPU và số lượt gọi API.
```

---

## 2. Quy Trình Cấu Hình Callback URL Trong Console

Để kích hoạt tính năng Push Mechanism:

1. Đăng nhập vào [Shopee Open Platform Console](https://open.shopee.com).
2. Vào mục **App Management > Chọn Ứng Dụng Của Bạn**.
3. Chọn thẻ **Push Mechanism**:
   - **Callback URL**: Điền đường dẫn công khai trên máy chủ của bạn (bắt buộc có **HTTPS**), ví dụ: `https://api.yourdomain.com/webhook/shopee`.
   - **Bật các loại sự kiện (Event Types)**: Tích chọn các sự kiện bạn muốn nhận thông báo:
     - `Order Status Push` (Sự kiện trạng thái đơn hàng).
     - `Tracking No Push` (Sự kiện mã vận đơn).
     - `Shop Authorization Push` (Sự kiện shop ủy quyền / hủy ủy quyền).
     - `Banned Item Push` (Sản phẩm bị khóa).
     - `Reserved Stock Change Push` (Tồn kho dự trữ thay đổi).
     - `Return Updates Push` (Khiếu nại trả hàng).
4. Nhấn **Save** và thực hiện **Test Ping** để kiểm tra máy chủ của bạn phản hồi HTTP 200 thành công.

---

## 3. Tiêu Chuẩn Kỹ Thuật Cho Máy Chủ Tiếp Nhận Webhook

Để đảm bảo kết nối không bị ngắt quãng, máy chủ webhook của bạn phải tuân thủ nghiêm ngặt các quy tắc sau:

1. **Phản hồi cực nhanh (< 3 giây)**:
   - Khi nhận được request từ Shopee, hãy xác thực chữ ký, đẩy ngay payload vào Hàng đợi thông điệp (Message Queue như Redis, RabbitMQ, Kafka, Celery) để xử lý ngầm ở background, và **lập tức trả về HTTP `200 OK`**.
   - Tuyệt đối không thực hiện các tác vụ nặng (như ghi đĩa chậm, query database phức tạp, gửi email) ngay trong luồng request chính của webhook vì sẽ gây timeout.
2. **Cấu trúc phản hồi**:
   - Mã trạng thái: `200 OK`.
   - Header: `Content-Type: application/json`.
   - Body: JSON rỗng `{}` hoặc chuỗi rỗng.
3. **Chính sách gửi lại của Shopee (Retry Policy)**:
   - Nếu máy chủ của bạn trả về mã lỗi (`4xx`, `5xx`) hoặc không phản hồi sau 5 giây, Shopee sẽ xem như giao dịch thất bại và tiến hành gửi lại (retry) theo chu kỳ tăng dần (ví dụ: sau 1 phút, 5 phút, 15 phút, 1 giờ...).
   - Nếu tỷ lệ thất bại kéo dài, Shopee có thể tạm thời đình chỉ gửi webhook cho ứng dụng của bạn.

