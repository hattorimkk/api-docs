# 06. Hướng Dẫn Trích Xuất Lịch Sử Tin Nhắn & Đánh Giá CSKH (Chat & Service Quality)

Tài liệu này hướng dẫn cách trích xuất toàn bộ lịch sử trao đổi của người mua, bóc tách các cuộc hội thoại chăm sóc khách hàng (CSKH) và đo lường các chỉ số dịch vụ trên Shopee Open Platform.

---

## 1. Ứng Dụng Thực Tế Của Việc Trích Xuất Dữ Liệu Chat

1. **Hợp nhất tin nhắn đa kênh (Omnichannel Inbox)**: Gom toàn bộ tin nhắn từ Shopee, Lazada, TikTok Shop, Fanpage về một màn hình duy nhất cho nhân viên trực chat.
2. **Phân tích phản hồi khách hàng (Sentiment Analysis)**: Dùng AI hoặc mô hình NLP phân tích nội dung khách chat để phát hiện các sản phẩm hay bị phàn nàn về lỗi, chất lượng hoặc giao thiếu hàng.
3. **Đo lường KPI nhân viên CSKH**: Đo thời gian phản hồi trung bình (First Response Time) và số lượng hội thoại đã xử lý trong ca trực.
4. **Bảo toàn Tỷ Lệ Phản Hồi Chat (Chat Response Rate - CRR)**: Tự động phát hiện các hội thoại chưa đọc sắp vượt quá khung 12 giờ của Shopee để cảnh báo nhân viên phản hồi ngay.

---

## 2. Chiến Lược Thu Thập Toàn Bộ Hội Thoại & Tin Nhắn

Quy trình trích xuất gồm 2 cấp độ:

```
[get_conversation_list]  --------------------->  Lấy danh sách các conversation_id
          |
          v
[get_message (lặp phân trang direction=older)] ->  Tải toàn bộ dòng tin nhắn chi tiết
```

### Bước 1: Quét danh sách các cuộc hội thoại
- **Lệnh cURL mẫu**:
```bash
curl -X GET "https://partner.shopeemobile.com/api/v2/sellerchat/get_conversation_list?partner_id=123456&timestamp=1700000000&access_token=your_token&shop_id=98765432&sign=calculated_sign_here&type=all&direction=latest&page_size=50" \
  -H "Content-Type: application/json"
```
- Sử dụng tham số `next_timestamp_nano` để lật trang liên tục đến khi `more == false`.
- Mỗi cuộc hội thoại cung cấp: `conversation_id`, `to_id` (ID người mua), `to_name` (Username người mua), `unread_count`, và `last_message_timestamp`.

### Bước 2: Tải lịch sử tin nhắn của từng hội thoại
- **Lệnh cURL mẫu**:
```bash
curl -X GET "https://partner.shopeemobile.com/api/v2/sellerchat/get_message?partner_id=123456&timestamp=1700000000&access_token=your_token&shop_id=98765432&sign=calculated_sign_here&conversation_id=conv_98765432_12345678&direction=older&page_size=50" \
  -H "Content-Type: application/json"
```
- Dữ liệu tin nhắn thu về gồm:
  - `message_id`: ID duy nhất của tin nhắn.
  - `from_id`: ID người gửi (nếu trùng `shop_id` thì là Shop nhắn, ngược lại là khách nhắn).
  - `message_type`: `text`, `image`, `item`, `order`.
  - `content`: Nội dung văn bản hoặc link ảnh/sản phẩm.
  - `created_timestamp`: Thời điểm gửi chính xác đến nano giây.

---

## 3. Khuyến Nghị Xử Lý Dữ Liệu Thời Gian Thực Bằng Webchat Webhook

Để không bỏ sót tin nhắn và tránh bị khóa do gọi API liên tục:
- Cấu hình nhận sự kiện Webchat Push Notification từ Shopee.
- Khi có tin nhắn mới từ khách hàng, Shopee sẽ bắn Webhook ngay lập tức sang Callback URL của bạn.
- Hệ thống đẩy tin nhắn vào cơ sở dữ liệu và hiển thị lên giao diện nhân viên CSKH trong vòng dưới 1 giây.
- Khi nhân viên gõ câu trả lời, hệ thống gọi `v2.sellerchat.send_message` và lập tức gọi `v2.sellerchat.read_conversation` để xác nhận đã xử lý xong.

