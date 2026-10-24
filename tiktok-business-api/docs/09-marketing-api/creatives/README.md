# Tổng Quan Phân Hệ Creative API (Nội Dung Sáng Tạo)

> **Phân hệ**: Creative API (Quản lý Nội dung Sáng tạo & Tài sản Đa phương tiện)  
> **Phiên bản API**: TikTok Business Marketing API v1.3  
> **Giao thức gọi**: RESTful API với **100% lệnh mẫu bằng cURL**

---

## 📌 1. Giới thiệu tổng quan

Trong hệ sinh thái quảng cáo TikTok, **Nội dung sáng tạo (Creatives)** là yếu tố quyết định hàng đầu đến hiệu suất chiến dịch, tỷ lệ nhấp (CTR) và tỷ lệ chuyển đổi (CVR). TikTok Business API cung cấp một hệ thống API toàn diện giúp bạn:

1. **Quản lý tài nguyên đa phương tiện (Creative Assets)**: Tải lên, tìm kiếm, kiểm tra và tổ chức video, hình ảnh, âm nhạc thương mại, tài liệu HTML5 Playable.
2. **Tự động hóa sản xuất nội dung (Creative Tools)**: Tận dụng trí tuệ nhân tạo (AI) của TikTok để sinh video thông minh (Smart Video), ghép nhạc tự động (Smart Soundtrack), tự động phát hiện và sửa lỗi video (Smart Fix), gợi ý văn bản quảng cáo (Smart Text) và nút kêu gọi hành động (CTA).
3. **Tiền kiểm duyệt (Pre-review API)**: Gửi video và văn bản đi kiểm duyệt trước khi tạo quảng cáo, giúp giảm thiểu rủi ro bị từ chối quảng cáo và đẩy nhanh thời gian khởi chạy chiến dịch.
4. **Đo lường & Phân tích chuyên sâu (Creative Reports & Fatigue)**: Theo dõi tỷ lệ giữ chân người xem video theo từng giây (2s, 6s), tỷ lệ xem hết (100%), và phát hiện sớm hiện tượng **"bão hòa/mệt mỏi sáng tạo" (Creative Fatigue)** để tự động thay mới video kịp thời.

---

## 🗺️ 2. Bản đồ các module Creative API

Toàn bộ tài liệu chi tiết được tổ chức thành các bài hướng dẫn chuyên đề sau:

| STT | Tài liệu chi tiết | Mô tả nghiệp vụ | Endpoints chính |
| :---: | :--- | :--- | :--- |
| **01** | [**Video API**](01-video-api.md) | Upload video (file/URL), chunk upload file lớn, tìm kiếm & quản lý video | `/file/video/ad/upload/`, `/file/video/ad/info/`, `/file/video/ad/search/`, `/file/video/ad/update/`, `/file/video/suggestcover/` |
| **02** | [**Image API**](02-image-api.md) | Upload ảnh, tìm kiếm ảnh, lấy thông tin và chỉnh sửa ảnh thông minh | `/file/image/ad/upload/`, `/file/image/ad/info/`, `/file/image/ad/search/`, `/creative/image/edit/` |
| **03** | [**Music API**](03-music-api.md) | Khai thác kho nhạc thương mại TikTok, upload bài hát và ủy quyền | `/file/music/get/`, `/file/music/upload/`, `/identity/music/authorization/` |
| **04** | [**Creative Tools API**](04-creative-tools-api.md) | Các công cụ AI: Smart Video, Smart Soundtrack, Smart Fix, Smart Text, CTA gợi ý | `/creative/smart_video/create/`, `/creative/video_soundtrack/create/`, `/video/fix/task/create/`, `/creative/smart_text/generate/`, `/creative/cta/recommend/` |
| **05** | [**Creative Portfolios API**](05-creative-portfolios-api.md) | Quản lý danh mục tài sản sáng tạo, chia sẻ tài sản giữa các tài khoản | `/creative/portfolio/create/`, `/creative/portfolio/get/`, `/creative/asset/share/`, `/creative/asset/delete/` |
| **06** | [**Creative Reports & Fatigue**](06-creative-reports-fatigue-api.md) | Báo cáo hiệu suất video, chỉ số drop-off, đo lường độ suy giảm sáng tạo | `/creative/report/get/`, `/creative_fatigue/get/`, `/report/video_performance/get/` |
| **07** | [**Creative Pre-review API**](07-creative-pre-review-api.md) | Tiền kiểm duyệt video, văn bản và trang đích trước khi xuất bản chiến dịch | `/creative/pre_review/task/create/`, `/creative/pre_review/task/get/` |
| **08** | [**Playable Ads API**](08-playable-ads-api.md) | Upload và xác thực tài liệu quảng cáo tương tác (Mini Game HTML5) | `/playable/upload/`, `/playable/validate/`, `/playable/save/`, `/playable/get/` |
| **09** | [**Spark Ads & Creator Video API**](09-spark-ads-creator-video-api.md) | Lấy bài đăng TikTok tự nhiên, ủy quyền Spark Ads code, video Creator | `/tt_video/list/`, `/tt_video/info/`, `/tt_video/authorize/`, `/identity/video/get/` |
| **10** | [**Catalog Video Packages API**](10-catalog-video-packages-api.md) | Tạo hàng loạt video sản phẩm tự động từ danh mục Catalog | `/catalog/video_package/create/`, `/catalog/video_package/get/`, `/catalog/template_preview/create/` |

---

## 🔄 3. Sơ đồ quy trình làm việc với Creative API

```text
[Chuẩn bị tài nguyên]
       │
       ├─► 1. Tải lên Video / Ảnh thô (01-video-api / 02-image-api)
       ├─► 2. Dùng AI sinh video tự động (04-creative-tools: Smart Video)
       └─► 3. Ủy quyền video TikTok tự nhiên (09-spark-ads-creator-video)
       │
       ▼
[Kiểm tra & Tối ưu hóa chất lượng]
       │
       ├─► Tự động phát hiện lỗi độ phân giải, tỉ lệ khung hình (Smart Fix)
       ├─► Gợi ý ảnh bìa thu hút (Suggested Thumbnails)
       └─► Gửi tiền kiểm duyệt (07-creative-pre-review)
       │
       ▼
[Khởi tạo Quảng cáo (Ads Management)]
       │
       ├─► Gán video_id / image_id vào mẫu quảng cáo (/ad/create/)
       └─► Thiết lập Smart Creative hoặc ACO (Automated Creative Optimization)
       │
       ▼
[Theo dõi & Tối ưu hóa liên tục]
       │
       ├─► Theo dõi tỷ lệ giữ chân người xem: 2s, 6s, 25%, 50%, 75%, 100%
       ├─► Kiểm tra chỉ số Creative Fatigue (Phát hiện video bị bão hòa)
       └─► Tự động đổi video mới hoặc bật tắt vật liệu qua API (/material_status/update/)
```

---

## ⚙️ 4. Quy tắc kỹ thuật chung khi gọi Creative API bằng cURL

### Header bắt buộc
Mọi request gọi đến Creative API đều yêu cầu 2 header sau:

```bash
-H "Access-Token: <YOUR_ACCESS_TOKEN>" \
-H "Content-Type: application/json"
```

> **Lưu ý**: Đối với các API tải tệp tin cục bộ (ví dụ `/file/video/ad/upload/` với `upload_type=UPLOAD_BY_FILE`), cURL sẽ tự động đặt `Content-Type: multipart/form-data` khi bạn dùng cờ `-F`.

### Cấu trúc phản hồi chuẩn (Response Envelope)
Mọi phản hồi từ Creative API đều tuân theo chuẩn envelope của TikTok:

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20261023224745010245041042005ABCDE",
  "data": { ... }
}
```
- `code == 0`: Thao tác thành công.
- `code != 0`: Lỗi (tham khảo mã lỗi tại `message` hoặc tra cứu phụ lục mã lỗi).
