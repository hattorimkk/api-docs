import os

path = '/Users/hattorimk/Desktop/api-docs/tiktok-business-api/docs/huong-dan/creatives.md'
with open(path, 'r', encoding='utf-8') as f:
    old = f.read()

header_section = """# Hướng Dẫn Thực Chiến: Quản Lý Nội Dung Sáng Tạo (Creatives)

> **Phân hệ**: Marketing API > Creatives Guide  
> **Phiên bản API**: TikTok Business Marketing API v1.3  
> **Ưu tiên thực thi**: **100% lệnh mẫu bằng cURL**

Chào mừng bạn đến với cẩm nang hướng dẫn thực chiến về quản lý nội dung sáng tạo (Creatives) trên nền tảng TikTok Ads. Nội dung sáng tạo chính là yếu tố sống còn quyết định hiệu suất chiến dịch, tỷ lệ nhấp (CTR) và tỷ lệ chuyển đổi (CVR).

---

## 🧭 Bảng Điều Hướng: Hệ Thống 10 Module Creative API Chuyên Sâu

Để tra cứu chi tiết danh sách tham số và ví dụ cURL hoàn chỉnh cho từng nghiệp vụ, vui lòng xem các tài liệu chuyên đề trong thư mục `../creative-api/`:

| STT | Tài liệu chuyên sâu | Nội dung nghiệp vụ | Lệnh cURL chính |
| :---: | :--- | :--- | :--- |
| **01** | [**Video API**](../creative-api/01-video-api.md) | Upload video (Multipart/URL/Chunk), search, info, cover | `/file/video/ad/upload/`, `/file/video/ad/search/` |
| **02** | [**Image API**](../creative-api/02-image-api.md) | Upload hình ảnh, tìm kiếm ảnh, Smart Image Edit | `/file/image/ad/upload/`, `/creative/image/edit/` |
| **03** | [**Music API**](../creative-api/03-music-api.md) | Kho nhạc thương mại CML, upload nhạc bản quyền riêng | `/file/music/get/`, `/file/music/upload/` |
| **04** | [**Creative Tools API**](../creative-api/04-creative-tools-api.md) | AI Smart Video, Smart Soundtrack, Smart Fix, Smart Text, CTA | `/creative/smart_video/create/`, `/video/fix/task/create/` |
| **05** | [**Creative Portfolios API**](../creative-api/05-creative-portfolios-api.md) | Quản lý danh mục Portfolio, chia sẻ tài sản giữa các tài khoản | `/creative/portfolio/create/`, `/creative/asset/share/` |
| **06** | [**Creative Reports & Fatigue**](../creative-api/06-creative-reports-fatigue-api.md) | Đo lường Video Retention (2s/6s/100%) & Bão hòa sáng tạo | `/creative/report/get/`, `/creative_fatigue/get/` |
| **07** | [**Creative Pre-review API**](../creative-api/07-creative-pre-review-api.md) | Tiền kiểm duyệt video/văn bản trước khi khởi chạy quảng cáo | `/creative/pre_review/task/create/`, `/task/get/` |
| **08** | [**Playable Ads API**](../creative-api/08-playable-ads-api.md) | Upload và xác thực mini-game HTML5 tương tác | `/playable/upload/`, `/playable/validate/` |
| **09** | [**Spark Ads & Creator Video API**](../creative-api/09-spark-ads-creator-video-api.md) | Quảng cáo video TikTok tự nhiên & mã code Creator | `/tt_video/authorize/`, `/identity/video/get/` |
| **10** | [**Catalog Video Packages API**](../creative-api/10-catalog-video-packages-api.md) | Tự động sinh hàng loạt video sản phẩm từ Catalog | `/catalog/video_package/create/`, `/template_preview/create/` |

---

## ⚡ Quy Trình 5 Bước Vận Hành Creative Thực Chiến Bằng cURL

### Bước 1: Tải lên tài nguyên Video qua cURL
```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/file/video/ad/upload/" \\
  -H "Access-Token: YOUR_ACCESS_TOKEN" \\
  -F "advertiser_id=YOUR_ADVERTISER_ID" \\
  -F "upload_type=UPLOAD_BY_FILE" \\
  -F "file_name=video_quang_cao_tet.mp4" \\
  -F "video_file=@/duong/dan/toi/video.mp4" \\
  -F "flaw_detect=true" \\
  -F "auto_fix_enabled=true"
```

### Bước 2: Tự động sửa lỗi video (Smart Fix) & ghép nhạc AI
```bash
# Tạo tác vụ tự động sửa lỗi tỷ lệ khung hình và độ phân giải
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/video/fix/task/create/" \\
  -H "Access-Token: YOUR_ACCESS_TOKEN" \\
  -H "Content-Type: application/json" \\
  -d '{
    "advertiser_id": "YOUR_ADVERTISER_ID",
    "video_id": "YOUR_VIDEO_ID",
    "flaw_types": ["ILLEGAL_VIDEO_SIZE", "LOW_RESOLUTION"],
    "target_aspect_ratio": "9:16"
  }'
```

### Bước 3: Tiền kiểm duyệt nội dung trước khi xuất bản chiến dịch
```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/creative/pre_review/task/create/" \\
  -H "Access-Token: YOUR_ACCESS_TOKEN" \\
  -H "Content-Type: application/json" \\
  -d '{
    "advertiser_id": "YOUR_ADVERTISER_ID",
    "video_id": "YOUR_VIDEO_ID",
    "ad_text": "Ưu đãi Tết đặc biệt - Mua 1 tặng 1!",
    "landing_page_url": "https://example.com/khuyen-mai-tet",
    "location_codes": ["VN"]
  }'
```

### Bước 4: Tạo mẫu quảng cáo gắn Video Creative
```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/ad/create/" \\
  -H "Access-Token: YOUR_ACCESS_TOKEN" \\
  -H "Content-Type: application/json" \\
  -d '{
    "advertiser_id": "YOUR_ADVERTISER_ID",
    "adgroup_id": "YOUR_ADGROUP_ID",
    "ad_name": "Ad_Tet_Creative_01",
    "creatives": [{
      "ad_format": "SINGLE_VIDEO",
      "video_id": "YOUR_VIDEO_ID",
      "ad_text": "Ưu đãi Tết đặc biệt - Mua 1 tặng 1!",
      "call_to_action": "SHOP_NOW",
      "landing_page_url": "https://example.com/khuyen-mai-tet"
    }]
  }'
```

### Bước 5: Đo lường tỷ lệ giữ chân người xem & Bão hòa sáng tạo
```bash
# 5.1. Báo cáo tỷ lệ xem Video 2 giây, 6 giây, 100%
curl -X GET "https://business-api.tiktok.com/open_api/v1.3/creative/report/get/?advertiser_id=YOUR_ADVERTISER_ID&start_date=2026-10-01&end_date=2026-10-23&metrics=%5B%22video_watched_2s%22%2C%22video_watched_6s%22%2C%22video_views_p100%22%2C%22average_video_play%22%5D" \\
  -H "Access-Token: YOUR_ACCESS_TOKEN" \\
  -H "Content-Type: application/json"

# 5.2. Quét các video đang bị bão hòa (Creative Fatigue)
curl -X GET "https://business-api.tiktok.com/open_api/v1.3/creative_fatigue/get/?advertiser_id=YOUR_ADVERTISER_ID&page=1&page_size=20" \\
  -H "Access-Token: YOUR_ACCESS_TOKEN" \\
  -H "Content-Type: application/json"
```

---

"""

content_to_keep = old
if '# Hướng dẫn Creatives' in old:
    content_to_keep = old.split('# Hướng dẫn Creatives', 1)[1]

final_content = header_section + content_to_keep
with open(path, 'w', encoding='utf-8') as f:
    f.write(final_content)

print("Enhanced creatives.md successfully.")

