# Creative Tools API — Công Cụ Sáng Tạo Tự Động Thông Minh (AI)

> **Phân hệ**: Creative API > AI Creative Tools  
> **Phiên bản API**: TikTok Business Marketing API v1.3  
> **Giao thức gọi**: RESTful API với **100% lệnh mẫu bằng cURL**

---

## 📌 1. Giới thiệu tổng quan

Creative Tools API là bộ giải pháp tích hợp trí tuệ nhân tạo (AI) giúp các nhà quảng cáo tự động hóa quá trình sáng tạo nội dung từ con số 0:
1. **Smart Video**: Ghép nối hình ảnh sản phẩm và nhạc nền thành video hoàn chỉnh chỉ trong vài giây.
2. **Smart Video Soundtrack**: Tự động phân tích nhịp điệu video và ghép nhạc nền đồng bộ hoàn hảo (Beat matching).
3. **Smart Fix**: Phát hiện và sửa tự động các lỗi kỹ thuật như tỷ lệ khung hình sai chuẩn, video mờ hoặc thiếu độ phân giải.
4. **Smart Text**: Dùng mô hình ngôn ngữ lớn (LLM) để sinh tiêu đề và văn bản quảng cáo hấp dẫn dựa trên ngành hàng và từ khóa.
5. **CTA Recommendation**: Đề xuất các nút kêu gọi hành động (Call To Action) đạt tỷ lệ chuyển đổi cao nhất theo từng mục tiêu chiến dịch.
6. **Ads Preview**: Tạo liên kết xem trước giao diện quảng cáo thực tế trên ứng dụng TikTok trước khi xuất bản.

---

## 🚀 2. Danh sách Endpoints & Hướng dẫn cURL

### 2.1. Tạo video thông minh từ hình ảnh (`/creative/smart_video/create/`)

Cung cấp danh sách ảnh sản phẩm và văn bản, hệ thống AI sẽ tự động sinh video chuyển động bắt mắt.

- **Endpoint**: `POST https://business-api.tiktok.com/open_api/v1.3/creative/smart_video/create/`
- **Phương thức**: `POST`

```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/creative/smart_video/create/" \
  -H "Access-Token: 0123456789abcdef0123456789abcdef01234567" \
  -H "Content-Type: application/json" \
  -d '{
    "advertiser_id": "7123456789012345678",
    "image_ids": [
      "tos-maliva-i-0068/anh_san_pham_01",
      "tos-maliva-i-0068/anh_san_pham_02",
      "tos-maliva-i-0068/anh_san_pham_03"
    ],
    "video_duration": 15,
    "style": "DYNAMIC",
    "aspect_ratio": "9:16",
    "music_id": "7198273645123984512"
  }'
```

#### Phản hồi mẫu (JSON Response)

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20261023224940010245041042005N3O4P",
  "data": {
    "task_id": "sv_task_20261023_abc12345",
    "status": "PROCESSING"
  }
}
```

---

### 2.2. Ghép nhạc nền tự động theo nhịp video (`/creative/video_soundtrack/create/`)

Tự động phân tích video đã có và chèn nhạc nền ăn khớp với nhịp chuyển cảnh.

- **Endpoint**: `POST https://business-api.tiktok.com/open_api/v1.3/creative/video_soundtrack/create/`
- **Phương thức**: `POST`

```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/creative/video_soundtrack/create/" \
  -H "Access-Token: 0123456789abcdef0123456789abcdef01234567" \
  -H "Content-Type: application/json" \
  -d '{
    "advertiser_id": "7123456789012345678",
    "video_id": "v10033g50000cf7m1g3c77u3g2example",
    "music_id": "7198273645123984512",
    "volume": 0.8
  }'
```

---

### 2.3. Tạo tác vụ sửa lỗi video tự động — Smart Fix (`/video/fix/task/create/`)

Nếu video của bạn bị lỗi tỷ lệ khung hình (ví dụ video quay ngang 16:9 nhưng muốn chạy dạng dọc 9:16) hoặc độ phân giải thấp hơn 720p, API này sẽ tự động làm nét và bổ sung viền nền thông minh.

- **Endpoint**: `POST https://business-api.tiktok.com/open_api/v1.3/video/fix/task/create/`
- **Phương thức**: `POST`

```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/video/fix/task/create/" \
  -H "Access-Token: 0123456789abcdef0123456789abcdef01234567" \
  -H "Content-Type: application/json" \
  -d '{
    "advertiser_id": "7123456789012345678",
    "video_id": "v10033g50000cf7m1g3c77u3g2example",
    "flaw_types": ["ILLEGAL_VIDEO_SIZE", "LOW_RESOLUTION"],
    "target_aspect_ratio": "9:16"
  }'
```

#### Tra cứu trạng thái tác vụ sửa lỗi (`/video/fix/task/get/`)

```bash
curl -X GET "https://business-api.tiktok.com/open_api/v1.3/video/fix/task/get/?advertiser_id=7123456789012345678&task_id=sv_task_20261023_abc12345" \
  -H "Access-Token: 0123456789abcdef0123456789abcdef01234567" \
  -H "Content-Type: application/json"
```

---

### 2.4. Sinh tiêu đề quảng cáo thông minh — Smart Text (`/creative/smart_text/generate/`)

Sử dụng AI để gợi ý hàng loạt câu tiêu đề quảng cáo TikTok hấp dẫn dựa trên từ khóa sản phẩm.

- **Endpoint**: `POST https://business-api.tiktok.com/open_api/v1.3/creative/smart_text/generate/`
- **Phương thức**: `POST`

```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/creative/smart_text/generate/" \
  -H "Access-Token: 0123456789abcdef0123456789abcdef01234567" \
  -H "Content-Type: application/json" \
  -d '{
    "advertiser_id": "7123456789012345678",
    "keywords": ["son môi", "dưỡng ẩm", "khuyến mãi tết"],
    "language": "VI",
    "industry": "BEAUTY_PERSONAL_CARE",
    "text_count": 5
  }'
```

#### Phản hồi mẫu (JSON Response)

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20261023224950010245041042005Q5R6S",
  "data": {
    "texts": [
      "Son dưỡng môi hot nhất TikTok mùa Tết này - Mua 1 tặng 1!",
      "Môi mềm mịn cả ngày với ưu đãi cực sốc lên đến 50%. Nhấp xem ngay!",
      "Bí quyết dưỡng ẩm môi căng mọng cho dịp lễ hội. Khám phá ngay!",
      "Top 1 son môi được giới trẻ săn lùng nhất tuần qua!",
      "Ưu đãi Tết cực ngọt - Giao hàng miễn phí toàn quốc hôm nay."
    ]
  }
}
```

---

### 2.5. Đề xuất nút kêu gọi hành động CTA (`/creative/cta/recommend/`)

Tra cứu danh sách nút CTA tối ưu nhất dựa theo mục tiêu chiến dịch (Traffic, Conversions, App Install).

- **Endpoint**: `GET https://business-api.tiktok.com/open_api/v1.3/creative/cta/recommend/`
- **Phương thức**: `GET`

```bash
curl -X GET "https://business-api.tiktok.com/open_api/v1.3/creative/cta/recommend/?advertiser_id=7123456789012345678&objective_type=CONVERSIONS&language=VI" \
  -H "Access-Token: 0123456789abcdef0123456789abcdef01234567" \
  -H "Content-Type: application/json"
```

---

### 2.6. Tạo liên kết xem trước quảng cáo trên app — Ads Preview (`/creative/ads_preview/create/`)

Sinh mã QR hoặc đường link để bạn mở ứng dụng TikTok và xem trước video quảng cáo hiển thị chính xác như thế nào trên điện thoại.

- **Endpoint**: `POST https://business-api.tiktok.com/open_api/v1.3/creative/ads_preview/create/`
- **Phương thức**: `POST`

```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/creative/ads_preview/create/" \
  -H "Access-Token: 0123456789abcdef0123456789abcdef01234567" \
  -H "Content-Type: application/json" \
  -d '{
    "advertiser_id": "7123456789012345678",
    "ad_format": "SINGLE_VIDEO",
    "video_id": "v10033g50000cf7m1g3c77u3g2example",
    "ad_text": "Khuyến mãi Tết cực đỉnh - Mua ngay hôm nay!",
    "call_to_action": "SHOP_NOW",
    "landing_page_url": "https://example.com/tet2026"
  }'
```

#### Phản hồi mẫu (JSON Response)

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20261023225000010245041042005T7U8V",
  "data": {
    "preview_link": "https://ads.tiktok.com/preview/?token=eyJhbGciOi...",
    "qrcode_url": "https://p16-va.tiktokcdn.com/obj/qrcode_preview.png"
  }
}
```
