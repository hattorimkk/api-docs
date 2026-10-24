# Tham Khảo API: Shopee Live & Shopee Video

Tài liệu này cung cấp chi tiết đặc tả kỹ thuật và câu lệnh **cURL** cho các tính năng truyền phát trực tiếp (Shopee Live) và video ngắn (Shopee Video) trên Shopee Open Platform.

---

## PHẦN 1: SHOPEE LIVE (Livestream)

Shopee Live là kênh bán hàng tương tác trực tiếp, cho phép người bán gắn sản phẩm vào giỏ hàng live (Orange Bag), tung mã giảm giá độc quyền và chốt đơn trong phiên livestream.

### 1.1. Lấy Danh Sách Phiên Livestream Của Shop (Get Livestream List)
- **Endpoint**: `v2.livestream.get_session_list`
- **Đường dẫn**: `GET /api/v2/livestream/get_session_list`
- **Loại API**: Shop API

```bash
curl -X GET "https://partner.shopeemobile.com/api/v2/livestream/get_session_list?partner_id=123456&timestamp=1700000000&access_token=c71a39d892ef65a43b1234567890abcd&shop_id=98765432&sign=calculated_sign_here&page_size=20" \
  -H "Content-Type: application/json"
```

### 1.2. Thống Kê Hiệu Quả Phiên Live (Get Livestream Insight / Performance)
Endpoint này trả về số người xem cùng lúc cao nhất (Peak PCU), tổng lượt xem, tổng số đơn hàng chốt được và GMV phát sinh trong phiên live.

- **Endpoint**: `v2.livestream.get_session_metric`
- **Đường dẫn**: `GET /api/v2/livestream/get_session_metric`

```bash
curl -X GET "https://partner.shopeemobile.com/api/v2/livestream/get_session_metric?partner_id=123456&timestamp=1700000000&access_token=c71a39d892ef65a43b1234567890abcd&shop_id=98765432&sign=calculated_sign_here&session_id=live_88339911" \
  -H "Content-Type: application/json"
```

---

## PHẦN 2: SHOPEE VIDEO (Short Video)

Shopee Video cho phép nhà sáng tạo và người bán đăng tải các clip ngắn trải nghiệm sản phẩm và gắn link mua hàng trực tiếp.

### 2.1. Lấy Danh Sách Video Đã Xuất Bản (Get Video List)
- **Endpoint**: `v2.video.get_video_list`
- **Đường dẫn**: `GET /api/v2/video/get_video_list`
- **Loại API**: Shop API

```bash
curl -X GET "https://partner.shopeemobile.com/api/v2/video/get_video_list?partner_id=123456&timestamp=1700000000&access_token=c71a39d892ef65a43b1234567890abcd&shop_id=98765432&sign=calculated_sign_here&page_no=1&page_size=30" \
  -H "Content-Type: application/json"
```

### 2.2. Đo Lường Tương Tác & Chuyển Đổi Đơn Hàng Từ Video
- **Endpoint**: `v2.video.get_video_insight`
- **Đường dẫn**: `GET /api/v2/video/get_video_insight`

```bash
curl -X GET "https://partner.shopeemobile.com/api/v2/video/get_video_insight?partner_id=123456&timestamp=1700000000&access_token=c71a39d892ef65a43b1234567890abcd&shop_id=98765432&sign=calculated_sign_here&video_id=vid_5544332211" \
  -H "Content-Type: application/json"
```

