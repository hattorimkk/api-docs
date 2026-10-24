# Hướng Dẫn Thực Chiến: Quản Lý Nội Dung Sáng Tạo (Creatives)

> **Phân hệ**: Marketing API > Creatives Guide  
> **Phiên bản API**: TikTok Business Marketing API v1.3  
> **Ưu tiên thực thi**: **100% lệnh mẫu bằng cURL**

Chào mừng bạn đến với cẩm nang hướng dẫn thực chiến về quản lý nội dung sáng tạo (Creatives) trên nền tảng TikTok Ads. Nội dung sáng tạo chính là yếu tố sống còn quyết định hiệu suất chiến dịch, tỷ lệ nhấp (CTR) và tỷ lệ chuyển đổi (CVR).

---

## 🧭 Bảng Điều Hướng: Hệ Thống 10 Module Creative API Chuyên Sâu

Để tra cứu chi tiết danh sách tham số và ví dụ cURL hoàn chỉnh cho từng nghiệp vụ, vui lòng xem các tài liệu chuyên đề trong thư mục `../creative-api/`:

| STT | Tài liệu chuyên sâu | Nội dung nghiệp vụ | Lệnh cURL chính |
| :---: | :--- | :--- | :--- |
| **01** | [**Video API**](creatives/01-video-api.md) | Tải lên video (Multipart/URL/Chunk), tìm kiếm, thông tin chi tiết, ảnh bìa | `/file/video/ad/upload/`, `/file/video/ad/search/` |
| **02** | [**Image API**](creatives/02-image-api.md) | Upload hình ảnh, tìm kiếm ảnh, Smart Image Edit | `/file/image/ad/upload/`, `/creative/image/edit/` |
| **03** | [**Music API**](creatives/03-music-api.md) | Kho nhạc thương mại CML, upload nhạc bản quyền riêng | `/file/music/get/`, `/file/music/upload/` |
| **04** | [**Creative Tools API**](creatives/04-creative-tools-api.md) | Video thông minh AI, Nhạc nền thông minh, Tự động sửa lỗi Smart Fix, Văn bản thông minh Smart Text, Gợi ý CTA | `/creative/smart_video/create/`, `/video/fix/task/create/` |
| **05** | [**Creative Portfolios API**](creatives/05-creative-portfolios-api.md) | Quản lý danh mục Portfolio, chia sẻ tài sản giữa các tài khoản | `/creative/portfolio/create/`, `/creative/asset/share/` |
| **06** | [**Creative Reports & Fatigue**](creatives/06-creative-reports-fatigue-api.md) | Đo lường Video Retention (2s/6s/100%) & Bão hòa sáng tạo | `/creative/report/get/`, `/creative_fatigue/get/` |
| **07** | [**Creative Pre-review API**](creatives/07-creative-pre-review-api.md) | Tiền kiểm duyệt video/văn bản trước khi khởi chạy quảng cáo | `/creative/pre_review/task/create/`, `/task/get/` |
| **08** | [**Playable Ads API**](creatives/08-playable-ads-api.md) | Upload và xác thực mini-game HTML5 tương tác | `/playable/upload/`, `/playable/validate/` |
| **09** | [**Spark Ads & Creator Video API**](creatives/09-spark-ads-creator-video-api.md) | Quảng cáo video TikTok tự nhiên & mã code Creator | `/tt_video/authorize/`, `/identity/video/get/` |
| **10** | [**Catalog Video Packages API**](creatives/10-catalog-video-packages-api.md) | Tự động sinh hàng loạt video sản phẩm từ Catalog | `/catalog/video_package/create/`, `/template_preview/create/` |

---

## ⚡ Quy Trình 5 Bước Vận Hành Creative Thực Chiến Bằng cURL

### Bước 1: Tải lên tài nguyên Video qua cURL
```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/file/video/ad/upload/" \
  -H "Access-Token: YOUR_ACCESS_TOKEN" \
  -F "advertiser_id=YOUR_ADVERTISER_ID" \
  -F "upload_type=UPLOAD_BY_FILE" \
  -F "file_name=video_quang_cao_tet.mp4" \
  -F "video_file=@/duong/dan/toi/video.mp4" \
  -F "flaw_detect=true" \
  -F "auto_fix_enabled=true"
```

### Bước 2: Tự động sửa lỗi video (Smart Fix) & ghép nhạc AI
```bash
# Tạo tác vụ tự động sửa lỗi tỷ lệ khung hình và độ phân giải
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/video/fix/task/create/" \
  -H "Access-Token: YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "advertiser_id": "YOUR_ADVERTISER_ID",
    "video_id": "YOUR_VIDEO_ID",
    "flaw_types": ["ILLEGAL_VIDEO_SIZE", "LOW_RESOLUTION"],
    "target_aspect_ratio": "9:16"
  }'
```

### Bước 3: Tiền kiểm duyệt nội dung trước khi xuất bản chiến dịch
```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/creative/pre_review/task/create/" \
  -H "Access-Token: YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
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
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/ad/create/" \
  -H "Access-Token: YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
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
curl -X GET "https://business-api.tiktok.com/open_api/v1.3/creative/report/get/?advertiser_id=YOUR_ADVERTISER_ID&start_date=2026-10-01&end_date=2026-10-23&metrics=%5B%22video_watched_2s%22%2C%22video_watched_6s%22%2C%22video_views_p100%22%2C%22average_video_play%22%5D" \
  -H "Access-Token: YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json"

# 5.2. Quét các video đang bị bão hòa (Creative Fatigue)
curl -X GET "https://business-api.tiktok.com/open_api/v1.3/creative_fatigue/get/?advertiser_id=YOUR_ADVERTISER_ID&page=1&page_size=20" \
  -H "Access-Token: YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json"
```

---



> Phân hệ: guide:Marketing API/Creatives.
> Tài liệu biên dịch kỹ thuật chi tiết theo chuẩn TikTok Business API v1.3.

---

## Mục lục điều hướng
- [1. Nội dung sáng tạo (Creatives) (#doc-1736271785207810)](#doc-1736271785207810)
- [2. Tổng quan (Overview) (#doc-1748896830086145)](#doc-1748896830086145)
- [3. Hướng dẫn (Guides) (#doc-1748896852671489)](#doc-1748896852671489)
- [4. Tài sản sáng tạo (Creative assets) (#doc-1739361739523073)](#doc-1739361739523073)
- [5. Tải lên video, hình ảnh và âm nhạc (#doc-1738963828459521)](#doc-1738963828459521)
- [6. Tải lên Playables (#doc-1868153086739601)](#doc-1868153086739601)
- [7. Trang tức thì (Instant pages) (#doc-1739953260466178)](#doc-1739953260466178)
- [8. Nút kêu gọi hành động (Call-to-action texts) (#doc-1749018853745665)](#doc-1749018853745665)
- [9. Tiện ích tương tác (Interactive Add-ons) (#doc-1749019605861377)](#doc-1749019605861377)
- [10. Thẻ tương tác (Cards) (#doc-1749019652141058)](#doc-1749019652141058)
- [11. Nhãn dán tương tác (Stickers) (#doc-1749019667506177)](#doc-1749019667506177)
- [12. Tiện ích tương tác cao cấp (Premium Add-ons) (#doc-1749019676181505)](#doc-1749019676181505)
- [13. Thêm tuyên bố miễn trừ trách nhiệm (Disclaimers) vào quảng cáo (#doc-1739953274550273)](#doc-1739953274550273)
- [14. Công cụ sáng tạo (Creative tools) (#doc-1740286998081538)](#doc-1740286998081538)
- [15. SDK Trình chỉnh sửa Trang tức thì (Instant Page Editor SDK) (#doc-1740307202170881)](#doc-1740307202170881)
- [16. Xem trước quảng cáo (Ads preview) (#doc-1740317791125506)](#doc-1740317791125506)
- [17. (Không còn hỗ trợ) Phân cảnh động (Dynamic Scene) (#doc-1740307384545345)](#doc-1740307384545345)
- [18. Gợi ý nút kêu gọi hành động (CTA recommendations) (#doc-1740307296329730)](#doc-1740307296329730)
- [19. Tự động sửa lỗi video (Smart Fix) (#doc-1741472523309058)](#doc-1741472523309058)
- [20. (Không còn hỗ trợ) Nhạc nền thông minh, Video thông minh và Tối ưu nhanh (#doc-1749022727865345)](#doc-1749022727865345)
- [21. Phát hiện bão hòa nội dung sáng tạo (Creative Fatigue Detection) (#doc-1767568085608450)](#doc-1767568085608450)
- [22. Nhận kết quả tiền kiểm duyệt nội dung sáng tạo (#doc-1874110837867522)](#doc-1874110837867522)
- [23. Báo cáo sáng tạo (Creative reports) (#doc-1739067487319042)](#doc-1739067487319042)
- [24. Báo cáo sáng tạo cơ bản (Creative basic reports) (#doc-1749023062758401)](#doc-1749023062758401)
- [25. Báo cáo chi tiết video (Video Insights reports) (#doc-1789769972291585)](#doc-1789769972291585)
- [26. Dữ liệu chi tiết về sáng tạo (Creative insights) (#doc-1749023065231362)](#doc-1749023065231362)
- [27. Danh mục API (API reference) (#doc-1740649324143617)](#doc-1740649324143617)

---

<a id="doc-1736271785207810"></a>
<!-- doc_id: 1736271785207810 -->
<!-- doc_id: 1736271785207810 -->
# Quản lý nội dung sáng tạo (Creatives)
> Đường dẫn: Marketing API > Creatives
Bạn có thể sử dụng Creative API để quản lý các tài nguyên sáng tạo, vận hành các công cụ sáng tạo tự động và xuất báo cáo hiệu suất nội dung sáng tạo.
- Để tìm hiểu tổng quan về hệ sinh thái quản lý sáng tạo của TikTok, xem [Tổng quan](creatives.md#doc-1748896830086145).
- Để tìm hiểu các thuật ngữ và khái niệm cốt lõi, xem **Khái niệm sáng tạo (Concepts-Creatives)**.
- Để nắm rõ các loại tài nguyên, công cụ và báo cáo sáng tạo cùng cách khai thác chúng, xem [Hướng dẫn thực chiến](creatives.md#doc-1748896852671489):
  - [Tài nguyên sáng tạo](creatives.md#doc-1739361739523073): Phân tích chi tiết các định dạng tài nguyên và quy trình đưa tài nguyên vào mẫu quảng cáo. Xem [Tải lên video, hình ảnh và âm nhạc](creatives.md#doc-1738963828459521) để biết cách tải lên media, [Tải lên Playables](creatives.md#doc-1868153086739601) để xử lý quảng cáo tương tác micro-game, và [Thẻ tương tác (Cards)](creatives.md#doc-1749019652141058) để cấu hình hiển thị thẻ tương tác.
  - [Công cụ sáng tạo](creatives.md#doc-1740286998081538): Hướng dẫn sử dụng các công cụ AI như Smart Fix, gợi ý CTA, xem trước quảng cáo nhằm gia tăng hiệu quả chiến dịch.
  - [Báo cáo sáng tạo](creatives.md#doc-1739067487319042): Chi tiết các chỉ số giữ chân, dữ liệu phân tích khung hình theo từng giây và phát hiện bão hòa quảng cáo.
- Để tra cứu danh mục đầy đủ các endpoint API liên quan, xem [Tài liệu tham khảo API](creatives.md#doc-1740649324143617).

---

<a id="doc-1748896830086145"></a>
<!-- doc_id: 1748896830086145 -->
<!-- doc_id: 1748896830086145 -->
# Tổng quan (Overview)
> Đường dẫn: Marketing API > Creatives > Overview
Nội dung sáng tạo (Creative) bao gồm toàn bộ các phần tử đa phương tiện hiển thị tới người dùng trong quảng cáo, chẳng hạn như video, hình ảnh và âm thanh. Mỗi vị trí hiển thị (placement) có các tiêu chuẩn kỹ thuật riêng.
Hệ thống quản lý nội dung sáng tạo bao gồm 3 phân hệ chính:
- [Tài nguyên sáng tạo](creatives.md#doc-1739361739523073): Quản lý tập trung mọi chất liệu quảng cáo: video, hình ảnh, âm nhạc, Trang tức thì (Instant Pages), tiện ích tương tác (Interactive Add-ons)...
- [Công cụ sáng tạo](creatives.md#doc-1740286998081538): Cung cấp bộ công cụ tự động hóa như Smart Fix, xem trước quảng cáo, gợi ý CTA thông minh giúp sản xuất và chuẩn hóa video nhanh chóng.
- [Báo cáo sáng tạo](creatives.md#doc-1739067487319042): Theo dõi dữ liệu hiệu suất của từng tài nguyên, từ đó đưa ra quyết định tối ưu hóa nội dung và phân bổ ngân sách quảng cáo chính xác.

---

<a id="doc-1748896852671489"></a>
<!-- doc_id: 1748896852671489 -->
<!-- doc_id: 1748896852671489 -->
# Hướng dẫn chi tiết (Guides)
> Đường dẫn: Marketing API > Creatives > Guides
Tài liệu này hướng dẫn chi tiết quy trình khai thác các tài nguyên sáng tạo, công cụ hỗ trợ và hệ thống báo cáo:
- [Tài nguyên sáng tạo](creatives.md#doc-1739361739523073): Phân loại tài nguyên và cách ứng dụng vào chiến dịch quảng cáo.
  - Xem [Tải lên video, hình ảnh và âm nhạc](creatives.md#doc-1738963828459521) để biết cách tải media lên Asset Library.
  - Xem [Tải lên Playables](creatives.md#doc-1868153086739601) để tạo định dạng trải nghiệm tương tác.
  - Xem [Thẻ tương tác (Cards)](creatives.md#doc-1749019652141058) để cấu hình hiển thị thẻ tương tác đa dạng.
- [Công cụ sáng tạo](creatives.md#doc-1740286998081538): Hướng dẫn sử dụng các công cụ tối ưu hóa để cải thiện chỉ số phân phối quảng cáo.
- [Báo cáo sáng tạo](creatives.md#doc-1739067487319042): Khám phá các góc nhìn dữ liệu chuyên sâu phục vụ tối ưu hóa liên tục.

---

<a id="doc-1739361739523073"></a>
<!-- doc_id: 1739361739523073 -->
<!-- doc_id: 1739361739523073 -->
# Tài nguyên sáng tạo (Creative Assets)
> Đường dẫn: Marketing API > Creatives > Guides > Creative assets
Tài nguyên sáng tạo bao gồm các phần tử đa phương tiện xuất hiện trực tiếp trong quảng cáo, truyền tải thông điệp thương hiệu đến đối tượng mục tiêu.

# Các phân loại tài nguyên sáng tạo
Hệ thống hỗ trợ các loại tài nguyên sáng tạo sau:
- **Hình ảnh (Images)**: Xem [Tải lên video, hình ảnh và âm nhạc](creatives.md#doc-1738963828459521) để biết cách tải ảnh.
- **Video**: Xem [Tải lên video, hình ảnh và âm nhạc](creatives.md#doc-1738963828459521) để biết cách tải và kiểm tra chuẩn video.
- **Âm nhạc (Music)**: Xem [Tải lên video, hình ảnh và âm nhạc](creatives.md#doc-1738963828459521) để chọn hoặc tải nhạc nền phù hợp.
- **Playables (Quảng cáo tương tác)**: Xem [Tải lên Playables](creatives.md#doc-1868153086739601) để tạo quảng cáo chơi thử ứng dụng (HTML5).
- **Văn bản quảng cáo (Ad texts)**: Chỉ định trường `ad_text` để truyền tải thông điệp quảng cáo thông qua endpoint [/ad/create/](../12-api-reference/02-ads-p1.md#doc-1739953377508354) hoặc [/ad/update/](../12-api-reference/02-ads-p2.md#doc-1739953405142018).
- **Trang tức thì (Instant Pages)**: Xem [Trang tức thì](creatives.md#doc-1739953260466178) để biết cách cấu hình trang đích tải siêu nhanh.
- **Nút kêu gọi hành động (Call-to-action texts)**: Xem [Nút kêu gọi hành động](creatives.md#doc-1749018853745665) để tìm hiểu danh mục CTA và tính năng gợi ý CTA động.
- **Tiện ích tương tác (Interactive Add-ons)**: Xem [Tiện ích tương tác](creatives.md#doc-1749019605861377) để nắm bắt các định dạng hỗ trợ và cách kích hoạt trong quảng cáo. Xem chi tiết tại [Thẻ tương tác (Cards)](creatives.md#doc-1749019652141058).

# Tiêu chuẩn kỹ thuật sáng tạo
Quy chuẩn nội dung sáng tạo sẽ khác nhau tùy theo vị trí hiển thị (TikTok In-Feed, Pangle, Global App Bundle). Xem chi tiết tại bài viết [Quy cách định dạng quảng cáo (Ad Formats)](https://ads.tiktok.com/help/article?aid=9629) trên Trung tâm trợ giúp TikTok Business.

---

<a id="doc-1738963828459521"></a>
<!-- doc_id: 1738963828459521 -->
<!-- doc_id: 1738963828459521 -->
# Tải lên video, hình ảnh và âm nhạc
> Đường dẫn: Marketing API > Tài sản sáng tạo > Hướng dẫn > Tài sản sáng tạo > Tải lên video, hình ảnh và âm nhạc
Tài liệu này hướng dẫn chi tiết quy trình tải các tài nguyên sáng tạo (video, hình ảnh và âm nhạc) lên Thư viện tài sản TikTok (Asset Library) và liên kết chúng vào các mẫu quảng cáo phân phối trên TikTok, Pangle hoặc Global App Bundle.

# Tải lên video

Sử dụng endpoint [/file/video/ad/upload/](../12-api-reference/71-video.md#doc-1737587322856449) để tải video lên. Đối với video dùng làm quảng cáo TikTok, tỷ lệ khung hình (width & height) phải là 1:1, 9:16 hoặc 16:9. Độ phân giải tối thiểu tương ứng là ≥540\*960px, ≥640\*640px hoặc ≥960\*540px.

Để tra cứu đầy đủ thông số kỹ thuật video áp dụng cho các vị trí hiển thị TikTok, Global App Bundle và Pangle, xem [Quy chuẩn kỹ thuật video quảng cáo](https://ads.tiktok.com/help/article?aid=9626).

# Tải lên hình ảnh

Hình ảnh quảng cáo được phân loại thành 3 nhóm: hình ảnh dùng làm mẫu quảng cáo, hình ảnh làm ảnh bìa video (cover) và hình ảnh đại diện hồ sơ (profile avatar).

## Hình ảnh dùng làm quảng cáo
Sử dụng endpoint [/file/image/ad/upload/](../12-api-reference/47-images.md#doc-1739067433456642) để tải hình ảnh lên Thư viện tài sản. Trong phản hồi trả về, trường `image_id` sẽ chứa ID của ảnh. Bạn sử dụng mã ID này khi khởi tạo quảng cáo.

Để xem quy chuẩn kích thước ảnh trên Global App Bundle và Pangle, xem [Quy chuẩn hình ảnh quảng cáo](https://ads.tiktok.com/help/article/image-ads-specification?lang=zh).

Quy trình tạo quảng cáo hình ảnh đơn, xem [Tạo quảng cáo hình ảnh đơn (Single image ads)](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1777633230937090).

Quy trình tạo quảng cáo bộ sưu tập thẻ quay vòng, xem [Tạo quảng cáo Carousel (Carousel Ads)](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1766217791987713).

## Ảnh bìa video (Video covers)
Đối với quảng cáo video trên TikTok, bạn bắt buộc phải có một hình ảnh làm ảnh bìa video. Ảnh bìa phải có cùng tỷ lệ khung hình với video quảng cáo. TikTok cung cấp endpoint tự động tạo ảnh bìa (thumbnail) đề xuất từ nội dung video. Nếu bạn chưa có sẵn ảnh bìa và muốn tiết kiệm thời gian thiết kế thủ công, hãy gọi endpoint [/file/video/suggestcover/](../12-api-reference/71-video.md#doc-1740051189071873) để hệ thống tự động trích xuất các khung hình đẹp nhất. Phản hồi sẽ trả về danh sách `image_id` và link xem trước để bạn lựa chọn.

## Ảnh đại diện hồ sơ (Profile images)
Sử dụng endpoint [/file/image/ad/upload/](../12-api-reference/47-images.md#doc-1739067433456642) để tải ảnh đại diện lên Thư viện tài sản TikTok. Nếu hình ảnh được dùng làm avatar hiển thị của tài khoản quảng cáo (`avatar_icon_web_uri`), tỷ lệ khung hình bắt buộc phải là hình vuông chuẩn 1:1.

# Tải lên âm nhạc
Gọi endpoint [/file/music/get/](../12-api-reference/52-music.md#doc-1740053909509122) để lấy danh sách các bản nhạc thương mại có sẵn trong kho nhạc của TikTok. Nếu không tìm thấy bài hát phù hợp, bạn có thể tải tệp âm thanh của riêng mình lên thông qua endpoint [/file/music/upload/](../12-api-reference/52-music.md#doc-1740052650395650).

# Tải lên tệp dung lượng lớn qua kho lưu trữ tạm thời
Bạn có thể tải video, âm nhạc và hình ảnh lên kho tệp tạm thời của TikTok (temporary file repository). Tệp tin lưu tại kho tạm có vòng đời 24 giờ trước khi tự động hết hạn. Đối với các tệp có dung lượng trên 20 MB, bạn có thể chia nhỏ tệp thành nhiều phân đoạn (chunks) và tải lên tuần tự. Sau đó, tệp sẽ được chuyển hợp nhất vào Thư viện tài sản TikTok (Asset Library) để đưa vào quảng cáo.

## Tải tệp đơn lẻ lên kho tạm
Đối với âm nhạc, video hoặc hình ảnh, bạn có thể sử dụng endpoint hợp nhất [/file/temporarily/upload/](../12-api-reference/44-files.md#doc-1737720893061122) để đưa tệp lên Thư viện tài sản. Cần chỉ định phương thức tải (`FILE` hoặc `URL`) và loại tệp (`image`, `music`, `video`). Phản hồi sẽ trả về ID tài nguyên để gắn vào chiến dịch.

## Tải tệp phân đoạn (chunked upload) lên kho tạm
Đối với các tệp có kích thước vượt quá 20 MB, bạn thực hiện chia tệp thành các phân đoạn, tải từng đoạn lên và ghép nối thành tệp hoàn chỉnh:
1. Gọi endpoint [/file/start/upload/](../12-api-reference/44-files.md#doc-1737721229896705) để khởi tạo phiên tải lên phân đoạn.
2. Gọi endpoint [/file/transfer/upload/](../12-api-reference/44-files.md#doc-1737721489945601) để tải từng phân đoạn. Kích thước mỗi phân đoạn trung gian cố định là 20 MB. Phân đoạn cuối cùng có thể dao động từ 5 MB đến 25 MB. Dựa vào giá trị `start_offset` và `end_offset` trong phản hồi để xác định phân đoạn cuối.
3. Khi tải xong phân đoạn cuối cùng, gọi [/file/finish/upload/](../12-api-reference/44-files.md#doc-1737721642924033) để máy chủ ghép nối hoàn thiện tệp. Phản hồi trả về `file_id`. Bạn sử dụng `file_id` này để chuyển tài nguyên sang Thư viện tài sản chính thức trong vòng 24 giờ.

# Các bước tiếp theo

Khi tạo mới hoặc cập nhật mẫu quảng cáo qua [/ad/create/](../12-api-reference/02-ads-p1.md#doc-1739953377508354) hoặc [/ad/update/](../12-api-reference/02-ads-p2.md#doc-1739953405142018), hãy truyền các trường sau để gắn tài nguyên vào quảng cáo:
- `image_ids`: Đối với ảnh bìa video, chỉ truyền DUY NHẤT một ID trong danh sách. Nếu chưa rõ mã ID, hãy gọi [/file/image/ad/search/](../12-api-reference/47-images.md#doc-1740052016789506) để tìm kiếm ID ảnh cần dùng.
- `video_id`: Truyền mã ID của video bạn muốn dùng cho mẫu quảng cáo. Nếu chưa rõ ID, gọi [/file/video/ad/search/](../12-api-reference/71-video.md#doc-1740050472224769) để tra cứu danh sách video sẵn có.

---

<a id="doc-1868153086739601"></a>
<!-- doc_id: 1868153086739601 -->
<!-- doc_id: 1868153086739601 -->
# Tải lên Playables (Quảng cáo tương tác)
> Đường dẫn: Marketing API > Creatives > Guides > Creative assets > Upload playables
Tài liệu này hướng dẫn quy trình tải các tài nguyên tương tác Playables lên Thư viện sáng tạo của TikTok và gắn vào chiến dịch quảng cáo thông qua API.

Playables là định dạng quảng cáo HTML5 tương tác trực tiếp, cho phép người dùng trải nghiệm bản demo hoặc chơi thử một đoạn game/ứng dụng ngắn ngay trên bảng tin TikTok. Nhờ cơ chế "dùng thử trước khi cài đặt", quảng cáo playable giúp sàng lọc tệp khách hàng tiềm năng và tối ưu tỷ lệ chuyển đổi cài đặt chất lượng cao.

## Các bước thực hiện
**1. Tải lên tài nguyên Playable.**

Gọi endpoint [/playable/upload/](../12-api-reference/56-playable-ads.md#doc-1737730926765057) để tải gói tệp Playable. Hệ thống sẽ tự động đối soát kỹ thuật với các tiêu chuẩn của TikTok.

**2. Kiểm tra trạng thái xác thực và kiểm duyệt (Audit status).**

Gọi endpoint [/playable/validate/](../12-api-reference/56-playable-ads.md#doc-1737732054892545) để kiểm tra tiến trình xác thực và trạng thái kiểm duyệt nội dung. Sau khi vượt qua bước kiểm tra kỹ thuật ban đầu, tài nguyên sẽ tự động chuyển sang quy trình kiểm duyệt nội dung quảng cáo.

**3. Lưu vào Thư viện sáng tạo (Creative Library).**

Khi trạng thái đạt `VALIDATE_SUCCESS` hoặc `AUDIT_SUCCESS`, gọi endpoint [/playable/save/](../12-api-reference/56-playable-ads.md#doc-1737732203851777) để hoàn tất việc lưu tài nguyên vào Thư viện sáng tạo. Phản hồi sẽ trả về `playable_url`. Bạn lưu lại URL này để sử dụng ở bước kế tiếp.

**Lưu ý**: Mặc dù bạn có thể lưu tài nguyên khi ở trạng thái `VALIDATE_SUCCESS`, chỉ những tài nguyên đã đạt trạng thái phê duyệt chính thức `AUDIT_SUCCESS` mới được phép phân phối trong các chiến dịch quảng cáo thực tế.

**4. Gắn Playable vào mẫu quảng cáo.**

Để sử dụng Playable trong mẫu quảng cáo Upgraded Smart+, hãy truyền đường dẫn `playable_url` vào trường `playable_list` khi gọi endpoint [/smart_plus/ad/create/](../12-api-reference/62-upgraded-smartplus-p5.md#doc-1843317390059522) hoặc [/smart_plus/ad/update/](../12-api-reference/62-upgraded-smartplus-p6.md#doc-1843317411665921).

---

<a id="doc-1739953260466178"></a>
<!-- doc_id: 1739953260466178 -->
<!-- doc_id: 1739953260466178 -->
# Trang tức thì (Instant Pages)
> Đường dẫn: Marketing API > Creatives > Guides > Creative assets > Instant pages
Trang tức thì (TikTok Instant Page) là trang đích nhẹ tối ưu hiển thị trên thiết bị di động, tải nhanh hơn tới 11 lần so với trang web tiêu chuẩn mở qua trình duyệt ngoài.

Hiện tại, bạn có thể tích hợp [SDK Trình tạo Trang tức thì TIP Editor SDK](creatives.md#doc-1740307202170881) để khởi tạo các định dạng Trang tức thì sau:
- **Trang tùy biến (Customized Page)**: Trang đích được thiết kế theo nhận diện thương hiệu, mang lại trải nghiệm tương tác liền mạch cho người dùng.
- **Biểu mẫu tức thì (Instant Form)**: Biểu mẫu thu thập thông tin khách hàng tiềm năng (Leads) trực tiếp trong ứng dụng TikTok, giúp người dùng gửi thông tin liên hệ và phản hồi khảo sát dễ dàng.
- **Trang hồ sơ ứng dụng (App Profile Pages)**: Trang giới thiệu tính năng ứng dụng chuyên sâu, thúc đẩy tỷ lệ chuyển đổi cài đặt đặc biệt hiệu quả trên các thiết bị chạy iOS 14.5+ nhờ thu thập tín hiệu chuyển đổi tại chỗ.
- **Biểu mẫu cửa sổ bật (Pop-up Form)**: Biểu mẫu gửi qua tin nhắn trực tiếp để thu thập khách hàng tiềm năng.

Sau khi tạo Trang tức thì thành công, bạn lấy mã ID trang bằng cách gọi endpoint [/page/get/](../12-api-reference/54-page.md#doc-1820826387779586). Mã ID này sẽ được truyền khi khởi tạo mẫu quảng cáo.

Để xem hướng dẫn chi tiết về tích hợp SDK, xem [Tạo trang tức thì bằng TIP Editor SDK](creatives.md#doc-1740307202170881).

---

<a id="doc-1749018853745665"></a>
<!-- doc_id: 1749018853745665 -->
<!-- doc_id: 1749018853745665 -->
# Văn bản kêu gọi hành động (Call-to-action texts)
> Đường dẫn: Marketing API > Tài sản sáng tạo > Hướng dẫn > Tài sản sáng tạo > Văn bản kêu gọi hành động (Call-to-action texts)
Nút kêu gọi hành động (CTA) là phần văn bản trên nút hiển thị trong quảng cáo giúp định hướng người dùng thực hiện một hành động cụ thể sau khi xem quảng cáo. Xem [Danh mục giá trị enum - Call-to-action](../15-appendix/phu-luc-p1.md#doc-1737174886619138) để tra cứu các giá trị enum của trường `call_to_action`. 

# Danh mục CTA (CTA portfolio)
Danh mục CTA được dùng để chứa các nút CTA tự động tối ưu hóa. Để tạo danh mục CTA, bạn cần lấy nhóm CTA tối ưu bằng endpoint [/creative/cta/recommend/](../12-api-reference/38-creative-tools.md#doc-1739362202742785), sau đó đưa dữ liệu trả về vào yêu cầu tạo danh mục tại endpoint [/creative/portfolio/create/](../12-api-reference/36-creative-portfolios.md#doc-1739091950439426).

# Gợi ý nút CTA (Recommended CTAs)
Bạn có thể sử dụng [/creative/cta/recommend/](../12-api-reference/38-creative-tools.md#doc-1739362202742785) để lấy danh sách CTA đề xuất cho quảng cáo. Có 2 loại đề xuất: CTA tiêu chuẩn và CTA động. Xem chi tiết tại [Gợi ý CTA](creatives.md#doc-1740307296329730).

---

<a id="doc-1749019605861377"></a>
<!-- doc_id: 1749019605861377 -->
<!-- doc_id: 1749019605861377 -->
# Tiện ích tương tác (Interactive Add-ons)
> Đường dẫn: Marketing API > Creatives > Guides > Creative assets > Interactive Add-ons
Tiện ích tương tác (Interactive Add-ons) giúp thu hút trọn vẹn sự chú ý của người xem trong môi trường toàn màn hình và bật tiếng của TikTok, từ đó gia tăng tương tác thương hiệu và thúc đẩy tỷ lệ chuyển đổi.

Hệ thống hỗ trợ 3 nhóm tiện ích tương tác chính: [Thẻ tương tác (Cards)](creatives.md#doc-1749019652141058), [Nhãn dán (Stickers)](creatives.md#doc-1749019667506177) và [Tiện ích cao cấp (Premium Add-ons)](creatives.md#doc-1749019676181505).

---

<a id="doc-1749019652141058"></a>
<!-- doc_id: 1749019652141058 -->
<!-- doc_id: 1749019652141058 -->
# Thẻ tương tác (Cards)
> Đường dẫn: Marketing API > Creatives > Guides > Creative assets > Interactive Add-ons > Cards
Bạn có thể nâng tầm quảng cáo với các loại Thẻ tương tác sau đây:

- **Thẻ hiển thị hình ảnh (Display Cards)**: Cho phép chèn hình ảnh tùy biến trong quảng cáo video in-feed. Khi xuất hiện, thẻ đóng vai trò như một nút CTA trực quan dẫn người dùng tới website hoặc trang tải ứng dụng. Xem chi tiết tại [hướng dẫn Display Card](https://ads.tiktok.com/resources/help/article/interactive-add-on-auction-ads-reach-frequency-display-card).
- **Thẻ khách sạn (Hotel Card)**: Tiện ích tự động trích xuất thông tin phòng và giá ưu đãi từ danh mục khách sạn để thúc đẩy người dùng đặt phòng.
- **Thẻ vé máy bay (Flight Card)**: Tiện ích tự động hiển thị thông tin chuyến bay từ danh mục hàng không để khuyến khích mua vé.
- **Thẻ điểm đến (Destination Card)**: Tự động đề xuất các địa điểm du lịch hấp dẫn từ danh mục sản phẩm du lịch.
- **Thẻ thông tin website (Website Info Cards)**: Hướng dẫn người dùng truy cập trang web để khám phá thông tin chi tiết về thương hiệu và sản phẩm.
- **Thẻ tải ứng dụng (Download Cards)**: Hiển thị các thông tin uy tín của ứng dụng như xếp hạng sao, số lượng đánh giá, danh mục ngành hàng; nhấp vào thẻ sẽ mở trang cài đặt ứng dụng trên App Store / Google Play. Xem chi tiết tại [hướng dẫn Download Card](https://ads.tiktok.com/resources/help/article/interactive-add-on-download-card).
- **Thẻ kho hàng (Inventory Cards)**: Thẻ hiển thị ở cuối quảng cáo khuyến khích người xem duyệt toàn bộ danh mục sản phẩm trong kho (phổ biến trong ngành ô tô).
- **Thẻ sản phẩm (Product Cards)**: Hiển thị thông tin sản phẩm đính kèm nhãn giá trên nền thẻ hình ảnh tùy biến.
- **Thẻ ô sản phẩm cuộn (Product Tiles)**: Hiển thị nhiều sản phẩm dưới dạng thanh trượt ngang trong cùng một mẫu quảng cáo.

# Cách ứng dụng thẻ trong quảng cáo

Thẻ tương tác là một định dạng bổ trợ đột phá trên hệ thống quảng cáo đấu thầu TikTok, giúp mẫu quảng cáo bắt mắt hơn và gia tăng chuyển đổi rõ rệt.

## Display Card
#### Điều kiện tiên quyết
- Để sử dụng Thẻ hiển thị hình ảnh (Display Card) trong quảng cáo, hãy bảo đảm đáp ứng các yêu cầu sau:
 	- Đối với các mục tiêu `REACH`, `TRAFFIC`, `VIDEO_VIEWS`, `APP_PROMOTION`, `WEB_CONVERSIONS`, hoặc `PRODUCT_SALES`:
 		- `placement_type` là `PLACEMENT_TYPE_AUTOMATIC`, hoặc `placement_type` là `PLACEMENT_TYPE_NORMAL` và có chứa `PLACEMENT_TIKTOK` trong giá trị của `placements`
	- Đối với mục tiêu `LEAD_GENERATION`:
    	- Ở cấp nhóm quảng cáo:
    		- `promotion_type` là `LEAD_GENERATION`
    		- `placement_type` là `PLACEMENT_TYPE_AUTOMATIC`, hoặc `placement_type` là `PLACEMENT_TYPE_NORMAL` và có chứa `PLACEMENT_TIKTOK` trong giá trị của `placements`
    	- Ở cấp quảng cáo: `ad_format` là `SINGLE_VIDEO`
- Bảo đảm bạn đã chuẩn bị sẵn hình ảnh cho thẻ. Kích thước hình ảnh bắt buộc phải là chiều rộng 750 px và chiều cao 421 px. 
	 - Tải hình ảnh lên bằng endpoint [/file/image/ad/upload/](../12-api-reference/47-images.md#doc-1739067433456642). Giá trị `image_id` trong phản hồi sẽ được dùng để tạo danh mục thẻ (card portfolio). 

 #### Các bước thực hiện
 1. Sử dụng [/creative/portfolio/create/](../12-api-reference/36-creative-portfolios.md#doc-1739091950439426) để tạo portfolio Thẻ hiển thị hình ảnh (Display Card portfolio).
- Thiết lập `creative_portfolio_type` thành `CARD`.
- Thiết lập `card_type` thành `IMAGE`.
- Truyền mã ID ảnh vào trường `image_id`. Endpoint này trả về mã ID danh mục thẻ (`creative_portfolio_id`) vừa tạo. 
2. Sử dụng portfolio trong quảng cáo của bạn.
- Đối với quảng cáo Upgraded Smart+: Truyền giá trị `creative_portfolio_id` vào trường `card_id` khi gọi [/smart_plus/ad/create/](../12-api-reference/62-upgraded-smartplus-p5.md#doc-1843317390059522) hoặc [/smart_plus/ad/update/](../12-api-reference/62-upgraded-smartplus-p6.md#doc-1843317411665921) để tạo hoặc cập nhật mẫu quảng cáo.
- Đối với quảng cáo thủ công (Manual Ads): Truyền giá trị `creative_portfolio_id` vào trường `card_id` khi gọi [/ad/create/](../12-api-reference/02-ads-p1.md#doc-1739953377508354) hoặc [/ad/update/](../12-api-reference/02-ads-p2.md#doc-1739953405142018) để tạo hoặc cập nhật mẫu quảng cáo.

## Hotel Card

#### Hình ảnh thẻ minh họa
![Thẻ khách sạn (Hotel Card)](https://images.ctfassets.net/5jqet0ab9qci/2UVi4AXv8Bn24q5ZnBSy0D/37723e84cd9c48bc140be23e1a1d806c/Hotel_Card.png)

#### Các bước thực hiện

1. Sử dụng endpoint [/creative/portfolio/create/](../12-api-reference/36-creative-portfolios.md#doc-1739091950439426) để tạo portfolio Thẻ khách sạn. Endpoint này trả về mã ID portfolio (`creative_portfolio_id`) vừa được tạo.
- Thiết lập `creative_portfolio_type` thành `HOTEL_CARD`.
- Thẻ khách sạn hiển thị các thông tin chi tiết về sản phẩm trong danh mục khách sạn kèm nút CTA điều hướng người dùng tới trang đích của bên thứ ba. Cấu hình các trường tùy biến (`primary_text`, `secondary_text` và `card_show_price`) theo nhu cầu của bạn.

| Thành phần thẻ | Tùy chỉnh khi tạo thẻ? | Các tùy chọn khả dụng | Trường API tương ứng | Giá trị trường tương ứng |
|---|---|---|---|---|
| Ảnh chính | ❌ Không | Ảnh chính (`image_url`) của sản phẩm khách sạn sẽ được sử dụng. Để lấy ảnh chính của sản phẩm khách sạn, gọi [/catalog/product/get/](https://business-api.tiktok.com/portal/docs/get-products/v1.3). | - | - |
| Văn bản chính | ✅ Có | • Không: Không hiển thị văn bản chính phía trên tiêu đề.<br>• Ưu đãi: Hiển thị nhãn "Ưu đãi" (Deals) làm văn bản chính phía trên tiêu đề.<br>• Nhãn tùy chỉnh: Hiển thị nhãn tùy chỉnh đầu tiên được chỉ định cho sản phẩm làm văn bản chính phía trên tiêu đề. Để lấy nhãn tùy chỉnh đầu tiên của sản phẩm khách sạn, kiểm tra trường `custom_label_0` trả về từ [/catalog/product/get/](https://business-api.tiktok.com/portal/docs/get-products/v1.3). | `primary_text` | • `NONE`<br>• `DEALS`<br>• `CUSTOM_LABEL` |
| Tiêu đề | ❌ Không | Tiêu đề (`name`) của sản phẩm khách sạn sẽ được sử dụng. Để lấy tiêu đề của sản phẩm khách sạn, gọi [/catalog/product/get/](https://business-api.tiktok.com/portal/docs/get-products/v1.3). | - | - |
| Văn bản phụ | ✅ Có | • Không: Không hiển thị văn bản phụ dưới tiêu đề.<br>• Đánh giá: Hiển thị thông tin xếp hạng (điểm tối đa, điểm thực tế và số lượt đánh giá) làm văn bản phụ dưới tiêu đề. Để lấy thông tin đánh giá, kiểm tra các trường `max_score`, `score` và `number_of_reviewers` trả về từ [/catalog/product/get/](https://business-api.tiktok.com/portal/docs/get-products/v1.3).<br>• Nhãn tùy chỉnh: Hiển thị nhãn tùy chỉnh thứ hai của sản phẩm làm văn bản phụ dưới tiêu đề. Để lấy nhãn tùy chỉnh thứ hai, kiểm tra trường `custom_label_1` trả về từ [/catalog/product/get/](https://business-api.tiktok.com/portal/docs/get-products/v1.3). | `secondary_text` | • `NONE`<br>• `RATING`<br>• `CUSTOM_LABEL` |
| Dùng AI tối ưu ảnh đại diện | ✅ Có | • Bật: Sử dụng AI để tối ưu hóa ảnh đại diện (chuyển ảnh không vuông thành ảnh vuông).<br>• Tắt: Không sử dụng AI để tối ưu hóa ảnh đại diện. | `image_optimization_enabled` | `true`<br>`false` |
| Giá (Hiển thị giá) | ✅ Có | • Bật: Hiển thị mức giá ở phía dưới thẻ. Để lấy giá sản phẩm khách sạn, kiểm tra trường `price` trả về từ [/catalog/product/get/](https://business-api.tiktok.com/portal/docs/get-products/v1.3).<br>• Tắt: Không hiển thị giá ở dưới đáy thẻ. | `card_show_price` | `true`<br>`false` |

2. Sử dụng [/smart_plus/ad/create/](../12-api-reference/62-upgraded-smartplus-p5.md#doc-1843317390059522) hoặc [/smart_plus/ad/update/](../12-api-reference/62-upgraded-smartplus-p6.md#doc-1843317411665921) để tạo hoặc cập nhật mẫu quảng cáo của bạn.
- Để sử dụng danh mục trong mẫu quảng cáo, truyền giá trị `creative_portfolio_id` vào trường `card_id`. Để tìm hiểu thêm về định dạng quảng cáo có thể dùng Hotel Cards, xem [Quảng cáo danh mục du lịch ứng dụng](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1879220213492353).

## Flight Card

#### Hình ảnh thẻ minh họa
![Thẻ chuyến bay (Flight Card)](https://images.ctfassets.net/5jqet0ab9qci/73NbRvICBxw4zjQOmzggmg/536b9078d933bf45a20c57c2b08ba621/Flight_Card.png)

#### Các bước thực hiện

1. Sử dụng endpoint [/creative/portfolio/create/](../12-api-reference/36-creative-portfolios.md#doc-1739091950439426) để tạo portfolio Thẻ chuyến bay. Endpoint này trả về mã ID portfolio (`creative_portfolio_id`) vừa được tạo.
- Thiết lập `creative_portfolio_type` thành `FLIGHT_CARD`.
- Thẻ chuyến bay hiển thị thông tin sản phẩm vé máy bay trong danh mục kèm nút CTA điều hướng. Bạn có thể cấu hình các cài đặt tùy chỉnh (`primary_text`, `secondary_text` và `card_show_price`) tùy ý.

| Thành phần thẻ | Tùy chỉnh khi tạo thẻ? | Các tùy chọn khả dụng | Trường API tương ứng | Giá trị trường tương ứng |
|---|---|---|---|---|
| Ảnh chính | ❌ Không | Ảnh chính (`image_url`) của sản phẩm vé máy bay sẽ được sử dụng. Để lấy ảnh chính, gọi [/catalog/product/get/](https://business-api.tiktok.com/portal/docs/get-products/v1.3). | - | - |
| Văn bản chính | ✅ Có | • Không: Không hiển thị văn bản chính phía trên thành phố đi và đến.<br>• Ưu đãi: Hiển thị nhãn "Ưu đãi" (Deals) phía trên thành phố đi và đến.<br>• Nhãn tùy chỉnh: Hiển thị nhãn tùy chỉnh đầu tiên làm văn bản chính. Để lấy nhãn tùy chỉnh đầu tiên của chuyến bay, kiểm tra `custom_label_0` trả về từ [/catalog/product/get/](https://business-api.tiktok.com/portal/docs/get-products/v1.3). | `primary_text` | • `NONE`<br>• `DEALS`<br>• `CUSTOM_LABEL` |
| Thành phố khởi hành & Đến | ❌ Không | Thành phố đi (`origin_city`) và đến (`destination_city`) sẽ được lấy từ dữ liệu chuyến bay qua [/catalog/product/get/](https://business-api.tiktok.com/portal/docs/get-products/v1.3). | - | - |
| Văn bản phụ | ✅ Có | • Không: Không hiển thị văn bản phụ dưới tiêu đề.<br>• Nhãn tùy chỉnh: Hiển thị nhãn tùy chỉnh thứ hai của sản phẩm làm văn bản phụ. Để lấy nhãn tùy chỉnh thứ hai, kiểm tra trường `custom_label_1` từ [/catalog/product/get/](https://business-api.tiktok.com/portal/docs/get-products/v1.3). | `secondary_text` | • `NONE`<br>• `CUSTOM_LABEL` |
| Dùng AI tối ưu ảnh đại diện | ✅ Có | • Bật: Sử dụng AI để tối ưu hóa ảnh đại diện (chuyển ảnh không vuông thành ảnh vuông).<br>• Tắt: Không sử dụng AI để tối ưu hóa ảnh đại diện. | `image_optimization_enabled` | `true`<br>`false` |
| Giá (Hiển thị giá) | ✅ Có | • Bật: Hiển thị giá vé dưới đáy thẻ. Để lấy giá vé chuyến bay, kiểm tra `price` trả về từ [/catalog/product/get/](https://business-api.tiktok.com/portal/docs/get-products/v1.3).<br>• Tắt: Không hiển thị giá ở dưới đáy thẻ. | `card_show_price` | `true`<br>`false` |

2. Sử dụng [/smart_plus/ad/create/](../12-api-reference/62-upgraded-smartplus-p5.md#doc-1843317390059522) hoặc [/smart_plus/ad/update/](../12-api-reference/62-upgraded-smartplus-p6.md#doc-1843317411665921) để tạo hoặc cập nhật mẫu quảng cáo của bạn.
- Để sử dụng danh mục trong mẫu quảng cáo, truyền giá trị `creative_portfolio_id` vào trường `card_id`. Để tìm hiểu thêm về định dạng quảng cáo có thể dùng Flight Cards, xem [Quảng cáo danh mục du lịch ứng dụng](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1879220213492353).

## Destination Card

#### Các bước thực hiện

1. Sử dụng [/creative/portfolio/create/](../12-api-reference/36-creative-portfolios.md#doc-1739091950439426) để tạo portfolio Thẻ điểm đến (Destination Card portfolio).
- Thiết lập `creative_portfolio_type` thành `DESTINATION_CARD`.
- Cấu hình các cài đặt cho Thẻ điểm đến thông qua `primary_text`, `secondary_text`, `image_optimization_enabled` và `display_price_enabled`. Endpoint này trả về mã ID danh mục (`creative_portfolio_id`) vừa tạo.

2. Sử dụng [/smart_plus/ad/create/](../12-api-reference/62-upgraded-smartplus-p5.md#doc-1843317390059522) hoặc [/smart_plus/ad/update/](../12-api-reference/62-upgraded-smartplus-p6.md#doc-1843317411665921) để tạo hoặc cập nhật mẫu quảng cáo của bạn.
- Để sử dụng danh mục trong mẫu quảng cáo, truyền giá trị `creative_portfolio_id` vào trường `card_id`. Để tìm hiểu thêm về định dạng quảng cáo có thể dùng Destination Card, xem [Quảng cáo danh mục du lịch ứng dụng](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1879220213492353).

## Thẻ thông tin website (Website Info Card)
### Điều kiện tiên quyết
- Để sử dụng Thẻ thông tin website trong quảng cáo, chiến dịch cần đáp ứng:
  - Mục tiêu chiến dịch: `WEB_CONVERSIONS` hoặc `TRAFFIC` (với `promotion_type` được thiết lập là `WEBSITE`).

### Các bước thực hiện
1. Gọi endpoint [/creative/portfolio/create/](../12-api-reference/36-creative-portfolios.md#doc-1739091950439426) để tạo portfolio Thẻ thông tin website:
	- Thiết lập `creative_portfolio_type` thành `WEB_INFO_CARD`.
	- Cấu hình thông tin thẻ qua các tham số `image_id`, `title` và `selling_points`. Endpoint này trả về mã `creative_portfolio_id` của danh mục thẻ.
2. Gọi endpoint [/ad/create/](../12-api-reference/02-ads-p1.md#doc-1739953377508354) hoặc [/ad/update/](../12-api-reference/02-ads-p2.md#doc-1739953405142018) để tạo hoặc cập nhật mẫu quảng cáo:
	- Để gắn thẻ vào quảng cáo, truyền giá trị `creative_portfolio_id` vào trường `card_id`.  

## Thẻ tải ứng dụng (Download Card)
### Điều kiện tiên quyết
- Để sử dụng Thẻ tải ứng dụng trong quảng cáo, hãy đảm bảo các tiêu chí:
 	- Mục tiêu chiến dịch: `TRAFFIC`, `APP_PROMOTION` hoặc `WEB_CONVERSIONS`
 	- Loại hình quảng bá (`promotion_type`): `WEBSITE` hoặc `App`
	- Vị trí hiển thị: `TikTok`

### Các bước thực hiện
1. Sử dụng endpoint [/creative/portfolio/create/](../12-api-reference/36-creative-portfolios.md#doc-1739091950439426) để tạo portfolio Thẻ tải ứng dụng:
	- Thiết lập `creative_portfolio_type` thành `DOWNLOAD_CARD`.
	- Cấu hình thông số hiển thị thẻ qua các tham số: `layouts`, `description`, `tags`, `category_label` (bắt buộc khi `tags` chứa `CATEGORIES`), `app_id`, `profile_image`, `call_to_action`, `mobile_app_id`, `country_code`. Endpoint trả về `creative_portfolio_id`.
2. Sử dụng endpoint [/ad/create/](../12-api-reference/02-ads-p1.md#doc-1739953377508354) hoặc [/ad/update/](../12-api-reference/02-ads-p2.md#doc-1739953405142018) để tạo hoặc cập nhật mẫu quảng cáo:
	- Truyền giá trị `creative_portfolio_id` vào trường `card_id`.  

## Thẻ kho hàng (Inventory Card)
### Các bước thực hiện
1. Sử dụng [/creative/portfolio/create/](../12-api-reference/36-creative-portfolios.md#doc-1739091950439426) để tạo portfolio Thẻ kho hàng:
  - Thiết lập `creative_portfolio_type` thành `INVENTORY_CARD`.
  - Cấu hình thông tin thẻ qua `image_id` và `description`. Endpoint trả về `creative_portfolio_id`.
2. Gắn portfolio thẻ vào quảng cáo:
- Đối với quảng cáo Upgraded Smart+: Truyền giá trị `creative_portfolio_id` vào trường `card_id` khi gọi [/smart_plus/ad/create/](../12-api-reference/62-upgraded-smartplus-p5.md#doc-1843317390059522) hoặc [/smart_plus/ad/update/](../12-api-reference/62-upgraded-smartplus-p6.md#doc-1843317411665921).
- Đối với quảng cáo thủ công (Manual Ads): Truyền giá trị `creative_portfolio_id` vào trường `card_id` khi gọi [/ad/create/](../12-api-reference/02-ads-p1.md#doc-1739953377508354) hoặc [/ad/update/](../12-api-reference/02-ads-p2.md#doc-1739953405142018).

> **Lưu ý:**
> Thẻ kho hàng Inventory Card chỉ áp dụng cho các chiến dịch quảng cáo ngành ô tô (Automotive Ads).

## Thẻ ô sản phẩm cuộn (Product Tiles)
### Điều kiện tiên quyết
- Trước khi tạo portfolio Thẻ ô sản phẩm, hãy đảm bảo danh mục của bạn chứa ít nhất 4 sản phẩm đã được kiểm duyệt phê duyệt. Để kiểm tra số lượng sản phẩm đủ điều kiện, gọi endpoint [/catalog/product/get/](../12-api-reference/28-catalog-products-p2.md#doc-1740564136678402) và xác nhận trường `audit_status` của ít nhất 4 sản phẩm là `approved`.
- Tính năng sử dụng Thẻ ô sản phẩm Product Tiles hiện đang trong danh sách thử nghiệm hạn chế (allowlist). Vui lòng liên hệ đại diện TikTok để được kích hoạt.
- Đảm bảo mẫu quảng cáo đáp ứng các yêu cầu kỹ thuật:
  - Mục tiêu chiến dịch: Doanh số sản phẩm (`objective_type` là `PRODUCT_SALES` ở cấp campaign)
  - Nguồn sản phẩm: Danh mục (`campaign_product_source` là `CATALOG` ở cấp campaign)
  - Loại quảng cáo mua sắm: Quảng cáo video mua sắm (`shopping_ads_type` là `VIDEO` ở cấp ad group)

### Các bước thực hiện
1. Sử dụng endpoint [/creative/portfolio/create/](../12-api-reference/36-creative-portfolios.md#doc-1739091950439426) để tạo portfolio Product Tiles:
  - Thiết lập `creative_portfolio_type` thành `PRODUCT_TILE`.
  - Cấu hình các tham số chi tiết:
    - `product_source` (đặt thành `CATALOG`)
    - `identity_id`
    - `identity_type`
    - `identity_authorized_bc_id` (khi `identity_type` là `BC_AUTH_TT`)
    - `catalog_id`
    - `catalog_authorized_bc_id`
    - `product_specific_type`
    - Một trong các trường `product_set_id`, `item_group_ids`, hoặc `sku_ids`
    - `card_image_index` *(Không bắt buộc)*

  Endpoint trả về mã định danh portfolio (`creative_portfolio_id`).

2. Sử dụng [/ad/create/](../12-api-reference/02-ads-p1.md#doc-1739953377508354) hoặc [/ad/update/](../12-api-reference/02-ads-p2.md#doc-1739953405142018) để tạo hoặc cập nhật mẫu quảng cáo. Cần tuân thủ cấu hình bảng sau:

| Tham số (Parameter) | Hướng dẫn cấu hình tham số |
|---|---|
| `card_id` | Truyền ID của danh mục Product Tiles vừa tạo. |
| `ad_format` | Thiết lập thành `SINGLE_VIDEO`. |
| `vertical_video_strategy` | Chọn một trong các giá trị: • `SINGLE_VIDEO` • `CATALOG_UPLOADED_VIDEOS`. |
| `dynamic_format` | Thiết lập thành `UNSET`. |
| • `catalog_id`<br>• `product_specific_type`<br>• Một trong `item_group_ids`, `product_set_id`, hoặc `sku_ids` | Truyền các trường và giá trị đồng nhất với lúc khởi tạo danh mục Product Tiles. |

## Thẻ sản phẩm (Product Card)
### Điều kiện tiên quyết
Để sử dụng Thẻ sản phẩm Product Card, chiến dịch cần đáp ứng:
- Mục tiêu: Doanh số sản phẩm (`objective_type` là `PRODUCT_SALES` ở cấp campaign)
- Định dạng quảng cáo mua sắm: Video Shopping ads (`shopping_ads_type` là `VIDEO` ở cấp ad group)

### Các bước thực hiện
1. Sử dụng endpoint [/creative/portfolio/create/](../12-api-reference/36-creative-portfolios.md#doc-1739091950439426) để tạo portfolio Product Card:
  - Thiết lập `creative_portfolio_type` thành `PRODUCT_CARD`.
  - Cấu hình các thiết lập của thẻ tùy theo nguồn sản phẩm:

| Nguồn sản phẩm (Product source) | Danh mục (Catalog) | Cửa hàng TikTok Shop |
|---|---|---|
| Cài đặt (Settings) | • `product_source` (đặt là `CATALOG`)<br>• `identity_id`<br>• `identity_type`<br>• `identity_authorized_bc_id` (khi `identity_type` là `BC_AUTH_TT`)<br>• `catalog_id`<br>• `catalog_authorized_bc_id`<br>• `product_specific_type`<br>• Một trong `product_set_id`, `item_group_ids`, hoặc `sku_ids`<br>• `dynamic_format`<br>• `vertical_video_strategy`<br>• `ad_text`<br>• `card_show_price`<br>• `card_tags`<br>• `card_image_index` *(Không bắt buộc)* | • `product_source` (đặt là `STORE`)<br>• `identity_id`<br>• `identity_type`<br>• `identity_authorized_bc_id` (khi `identity_type` là `BC_AUTH_TT`)<br>• `store_id`<br>• `store_authorized_bc_id`<br>• `item_group_ids`<br>• `ad_text`<br>• `card_show_price`<br>• `card_tags`<br>• `card_image_index` *(Không bắt buộc)* |

Endpoint này trả về mã định danh portfolio (`creative_portfolio_id`).

2. Sử dụng [/ad/create/](../12-api-reference/02-ads-p1.md#doc-1739953377508354) hoặc [/ad/update/](../12-api-reference/02-ads-p2.md#doc-1739953405142018) để tạo hoặc cập nhật mẫu quảng cáo:
  - Để gắn thẻ vào quảng cáo, truyền giá trị `creative_portfolio_id` vào trường `card_id`.

---

<a id="doc-1749019667506177"></a>
<!-- doc_id: 1749019667506177 -->
<!-- doc_id: 1749019667506177 -->
# Stickers
> Đường dẫn: Marketing API > Creatives > Guides > Creative assets > Interactive Add-ons > Stickers
# Countdown Sticker
Bạn có thể sử dụng loại Nhãn dán đếm ngược (Countdown Sticker) trong mẫu quảng cáo. Đây là tiện ích sáng tạo cho phép thêm đồng hồ đếm ngược vào video để thu hút sự chú ý của người xem và tạo cảm giác cấp bách. Xem [tại đây](https://ads.tiktok.com/help/article?aid=10007621) để xem giới thiệu chi tiết và hình ảnh minh họa. 

> **Note:** 
>   • Nhãn dán đếm ngược thông thường (`sticker_type` là `COUNTDOWN`) chỉ dùng cho quảng cáo đấu thầu có mục tiêu Reach (`REACH`), Traffic (`TRAFFIC`), Video views (`VIDEO_VIEW`), App promotion (`APP_PROMOTION`), Lead generation (`LEAD_GENERATION`), Website conversions (`WEB_CONVERSIONS`) hoặc Product sales (`PRODUCT_SALES`), cũng như quảng cáo R&F (`RF_REACH`). • Nhãn dán đếm ngược nhắc nhở (`sticker_type` là `REMINDER_COUNTDOWN` hoặc `LIVE_REMINDER_COUNTDOWN`) hỗ trợ thêm mục tiêu Tương tác cộng đồng (`ENGAGEMENT`).  • Nhãn dán đếm ngược nhắc nhở (`sticker_type` là `REMINDER_COUNTDOWN` hoặc `LIVE_REMINDER_COUNTDOWN`) là tính năng giới hạn (allowlist) đối với quảng cáo Traffic (`TRAFFIC`), App promotion (`APP_PROMOTION`), Website conversions (`WEB_CONVERSIONS`). Vui lòng liên hệ đại diện TikTok để kích hoạt.  •  Nếu bạn muốn dùng Countdown Sticker trong quảng cáo Tìm kiếm khách hàng tiềm năng, bạn chỉ có thể chọn Địa điểm tối ưu hóa là Website ở cấp nhóm quảng cáo. Xem chi tiết tại [Tạo quảng cáo Lead Generation với địa điểm tối ưu là Website](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1774482976097281).

## Sử dụng Nhãn dán đếm ngược (Use Countdown Sticker)
Để sử dụng Nhãn dán đếm ngược trong quảng cáo, hãy thực hiện các bước sau: 
1. Sử dụng [/creative/portfolio/create/](../12-api-reference/36-creative-portfolios.md#doc-1739091950439426) để tạo portfolio Nhãn dán đếm ngược (Countdown Sticker portfolio).
- Thiết lập `creative_portfolio_type` thành `STICKER`.
- Truyền giá trị `COUNTDOWN`, `REMINDER_COUNTDOWN` hoặc `LIVE_REMINDER_COUNTDOWN` vào trường `sticker_type` tùy theo loại nhãn dán bạn muốn tạo.
- Cấu hình các thiết lập cơ bản của nhãn dán qua `title`, `cutoff_time`, `color`, `display_angle`, `position_x`, `position_y`, `size` (hoặc `predefined_placement` thay thế cho tọa độ và kích thước) và độ trong suốt `opacity`.
- Cấu hình các cài đặt đặc biệt cho nhãn dán nhắc nhở (khi `sticker_type` khác `COUNTDOWN`):
  - Đối với nhãn dán nhắc sự kiện LIVE: Đặt `reminder_time` là 1 phút, 5 phút hoặc 10 phút sau khi phiên LIVE bắt đầu, đồng thời truyền mã `live_tiktok_user_id`.
  - Đối với nhãn dán sự kiện thông thường: Đặt `reminder_time` là 1 phút, 1 giờ hoặc 1 ngày trước sự kiện, đồng thời truyền đường dẫn `landing_page_url`.
  
  Endpoint này trả về mã ID danh mục thẻ (`creative_portfolio_id`) vừa tạo. 
2. Sử dụng portfolio trong quảng cáo của bạn.
- Đối với quảng cáo Upgraded Smart+: Truyền giá trị `creative_portfolio_id` vào trường `card_id` khi gọi [/smart_plus/ad/create/](../12-api-reference/62-upgraded-smartplus-p5.md#doc-1843317390059522) hoặc [/smart_plus/ad/update/](../12-api-reference/62-upgraded-smartplus-p6.md#doc-1843317411665921) để tạo hoặc cập nhật mẫu quảng cáo.
- Đối với quảng cáo thủ công (Manual Ads): Truyền giá trị `creative_portfolio_id` vào trường `card_id` khi gọi [/ad/create/](../12-api-reference/02-ads-p1.md#doc-1739953377508354) hoặc [/ad/update/](../12-api-reference/02-ads-p2.md#doc-1739953405142018) để tạo hoặc cập nhật mẫu quảng cáo.
  
# Nhãn dán mã quà tặng (Gift Code Sticker)
Bạn có thể sử dụng Nhãn dán mã quà tặng (Gift Code Sticker) trong mẫu quảng cáo. Tiện ích này cho phép bạn gắn mã khuyến mại đặc quyền vào video quảng cáo. Xem [tại đây](https://ads.tiktok.com/help/article/interactive-add-on-create-ad-gift-code-sticker?lang=en) để xem chi tiết và hình ảnh mẫu.

> **Note:** 
> Nhãn dán mã quà tặng chỉ áp dụng cho quảng cáo đấu thầu có mục tiêu Reach (`REACH`), Traffic (`TRAFFIC`), Video views (`VIDEO_VIEW`), App promotion (`APP_PROMOTION`), Lead generation (`LEAD_GENERATION`), Website conversions (`WEB_CONVERSIONS`) hoặc Product sales (`PRODUCT_SALES`), cũng như quảng cáo Tiếp cận & Tần suất R&F (`RF_REACH`).  •  Nếu bạn muốn dùng Gift Code Sticker trong quảng cáo Tìm kiếm khách hàng tiềm năng, bạn chỉ có thể chọn Địa điểm tối ưu hóa là Website. Xem chi tiết tại [Tạo quảng cáo Lead Generation với địa điểm tối ưu là Website](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1774482976097281).

## Sử dụng Nhãn dán mã quà tặng (Use Gift Code Sticker)
Để sử dụng Nhãn dán mã quà tặng trong quảng cáo, hãy thực hiện các bước sau:
1. Sử dụng [/creative/portfolio/create/](../12-api-reference/36-creative-portfolios.md#doc-1739091950439426) để tạo portfolio Nhãn dán mã quà tặng (Gift Code Sticker portfolio).
- Thiết lập `creative_portfolio_type` thành `STICKER`.
- Truyền giá trị `GIFTCODE` vào trường `sticker_type`.
- Cấu hình các thông số cơ bản qua `title`, mã ưu đãi `giftcode`, màu sắc `color`, tọa độ `position_x` và `position_y` (hoặc dùng `predefined_placement`).
- Endpoint này trả về mã ID danh mục thẻ (`creative_portfolio_id`) vừa tạo.
2. Sử dụng portfolio trong quảng cáo của bạn.
- Đối với quảng cáo Upgraded Smart+: Truyền giá trị `creative_portfolio_id` vào trường `card_id` khi gọi [/smart_plus/ad/create/](../12-api-reference/62-upgraded-smartplus-p5.md#doc-1843317390059522) hoặc [/smart_plus/ad/update/](../12-api-reference/62-upgraded-smartplus-p6.md#doc-1843317411665921) để tạo hoặc cập nhật mẫu quảng cáo.
- Đối với quảng cáo thủ công (Manual Ads): Truyền giá trị `creative_portfolio_id` vào trường `card_id` khi gọi [/ad/create/](../12-api-reference/02-ads-p1.md#doc-1739953377508354) hoặc [/ad/update/](../12-api-reference/02-ads-p2.md#doc-1739953405142018) để tạo hoặc cập nhật mẫu quảng cáo.

---

<a id="doc-1749019676181505"></a>
<!-- doc_id: 1749019676181505 -->
<!-- doc_id: 1749019676181505 -->
# Tiện ích tương tác cao cấp (Premium Add-ons)
> Đường dẫn: Marketing API > Creatives > Guides > Creative assets > Interactive Add-ons > Premium Add-ons
Bạn có thể nâng cao hiệu quả quảng cáo với 3 loại Tiện ích tương tác cao cấp (Premium Add-ons) sau:
- **Hộp hiển thị bật nổi (Pop-out Showcase)**: Bao gồm hình ảnh sản phẩm và nút CTA, tự động bật nổi sau khi video phát được vài giây. 
- **Cử chỉ tương tác (Gesture)**: Bao gồm hình ảnh và thẻ pop-up, hướng dẫn người xem chạm hoặc vuốt màn hình để mở khóa phần thưởng hoặc thông tin ưu đãi.
- **Nút thả tim đặc biệt (Superlike)**: Tạo hoạt ảnh biểu tượng trái tim tùy biến bay khắp màn hình khi người xem nhấn thích hoặc chạm đúp vào video.

# Sử dụng Hộp hiển thị bật nổi (Use Pop-out Showcase)
Để sử dụng Pop-out Showcase trong quảng cáo, thực hiện các bước sau: 

### Điều kiện tiên quyết
Tải hình ảnh huy hiệu cao cấp (Premium Badge) bằng [/file/image/ad/upload/](../12-api-reference/47-images.md#doc-1739067433456642). Giá trị `image_id` trả về sẽ được dùng để tạo danh mục Pop-out Showcase. 
Bảo đảm hình ảnh đáp ứng các quy chuẩn kỹ thuật sau:
  - Kích thước: Chiều rộng 448 pixel và chiều cao 448 pixel.
  - Định dạng hình ảnh: JPG, JPEG, PNG hoặc GIF.
  - Dung lượng tệp: Trong giới hạn 1 MB.
  
### Các bước thực hiện
1. Sử dụng [/creative/portfolio/create/](../12-api-reference/36-creative-portfolios.md#doc-1739091950439426) để tạo portfolio Hộp hiển thị bật nổi (Pop-out Showcase portfolio). 
- Thiết lập `creative_portfolio_type` thành `PREMIUM_BADGE`.
- Truyền mã ID ảnh vào trường `image_id` bên trong đối tượng `badge_image_info`.
- Chỉ định thời điểm bắt đầu xuất hiện huy hiệu qua trường `badge_show_time` (ví dụ: 5 giây). Ba giây đầu và năm giây cuối của video không được dùng làm thời điểm xuất hiện.
- Thiết lập văn bản kêu gọi hành động qua trường dữ liệu `call_to_action_text`.
- Cấu hình tọa độ tương đối góc trên bên trái của huy hiệu qua đối tượng `badge_position`. Trong đó `position_x` là tọa độ x chia cho 720; `position_y` là tọa độ y chia cho 1280. 

Endpoint này trả về mã ID danh mục thẻ (`creative_portfolio_id`) vừa tạo. 

2. Sử dụng [/ad/create/](../12-api-reference/02-ads-p1.md#doc-1739953377508354) hoặc [/ad/update/](../12-api-reference/02-ads-p2.md#doc-1739953405142018) để tạo hoặc cập nhật mẫu quảng cáo của bạn.  

Để sử dụng danh mục thẻ trong quảng cáo, hãy truyền `creative_portfolio_id` vào trường `card_id`. 

> **Note:** 
>  • Pop-out Showcase chỉ hỗ trợ các mục tiêu quảng cáo APP_PROMOTION, WEB_CONVERSIONS, TRAFFIC, VIDEO_VIEWS, REACH và RF_REACH. • Việc sử dụng portfolio Pop-out Showcase trong các chiến dịch APP_PROMOTION, WEB_CONVERSIONS hoặc TRAFFIC hiện là tính năng allowlist. Vui lòng liên hệ đại diện TikTok để được kích hoạt.

# Sử dụng Cử chỉ tương tác (Use Gesture)
Để sử dụng Cử chỉ tương tác Gesture trong quảng cáo, thực hiện các bước sau:
### Điều kiện tiên quyết
- Tải lên hình ảnh thẻ popup cử chỉ bằng [/file/image/ad/upload/](../12-api-reference/47-images.md#doc-1739067433456642). Mã `image_id` trong phản hồi sẽ được dùng để tạo danh mục Gesture. 
Bảo đảm hình ảnh đáp ứng các quy chuẩn kỹ thuật sau:
  - Kích thước khuyến nghị: 620 pixel chiều rộng và 788 pixel chiều cao.
  - Định dạng hình ảnh: JPG, JPEG, PNG hoặc GIF.
  - Dung lượng tệp: Trong giới hạn 3 MB.
- Tải lên âm thanh nền cho cử chỉ bằng [/file/music/upload/](../12-api-reference/52-music.md#doc-1740052650395650). Đường dẫn `url` trong phản hồi sẽ được dùng để tạo danh mục Gesture. 
Bảo đảm hình ảnh đáp ứng các quy chuẩn kỹ thuật sau:
  - Dung lượng tệp: Trong giới hạn 1 MB.
  - Định dạng tệp: MP3.
  - Thời lượng khuyến nghị: six seconds.

> **Note:** 
>  Để đảm bảo trải nghiệm quảng cáo đồng nhất, hãy sử dụng nhạc nền của video làm nhạc nền cho cử chỉ Gesture.

### Các bước thực hiện
1. Sử dụng [/creative/portfolio/create/](../12-api-reference/36-creative-portfolios.md#doc-1739091950439426) để tạo portfolio Cử chỉ tương tác (Gesture portfolio).
- Thiết lập `creative_portfolio_type` thành `GESTURE`.
- Truyền ID hình ảnh thẻ popup cử chỉ vào trường `pop_up_window_image_id`.
- Thiết lập văn bản hướng dẫn tương tác qua trường `call_to_action_text`.
- Chỉ định thời điểm cử chỉ bắt đầu xuất hiện qua trường `badge_show_time`. Ba giây đầu và năm giây cuối của video không được dùng làm thời điểm bắt đầu.
- Cấu hình tọa độ tương đối góc trên bên trái của cử chỉ qua hai tham số `position_x` và `position_y`.
- Chỉ định nhạc nền tương tác cho cử chỉ bằng trường `interactive_music_id`.
- Cấu hình các thông số chi tiết khác tùy theo loại cử chỉ:
  - Đối với cử chỉ Nhấp (`gesture_type` là `CLICK`), không truyền `angle`, `slide_length` và `slide_dimension`.
  - Đối với cử chỉ Vuốt thẳng (`gesture_type` là `STRAIGHT_SLIDE`), chỉ định góc và chiều dài vuốt bằng `angle` và `slide_length`, không truyền `slide_dimension`.
  - Đối với cử chỉ Vuốt cong (`gesture_type` là `CURVED_SLIDE`), chỉ định góc và kích thước vuốt bằng `angle` và `slide_dimension`, không truyền `slide_length`.

Endpoint này trả về mã ID danh mục thẻ (`creative_portfolio_id`) vừa tạo.

2. Sử dụng [/ad/create/](../12-api-reference/02-ads-p1.md#doc-1739953377508354) hoặc [/ad/update/](../12-api-reference/02-ads-p2.md#doc-1739953405142018) để tạo hoặc cập nhật mẫu quảng cáo của bạn.

Để sử dụng danh mục thẻ trong quảng cáo, hãy truyền `creative_portfolio_id` vào trường `card_id`.

> **Note:** 
> - Thời lượng khuyến nghị của video quảng cáo khi gắn cử chỉ Gesture là tối thiểu 15 giây.
> - Cử chỉ Gesture chỉ hỗ trợ các mục tiêu chiến dịch REACH, TRAFFIC, VIDEO_VIEWS (với optimization_goal là ENGAGED_VIEW), APP_PROMOTION, WEB_CONVERSIONS và RF_REACH.
> - Việc sử dụng portfolio Gesture trong chiến dịch có mục tiêu APP_PROMOTION, TRAFFIC hoặc WEB_CONVERSIONS hiện là tính năng thử nghiệm giới hạn (allowlist). Vui lòng liên hệ đại diện TikTok để được kích hoạt.

# Sử dụng Nút thả tim đặc biệt (Use Superlike)
Để sử dụng Superlike trong quảng cáo, thực hiện các bước sau:
### Điều kiện tiên quyết
- Tải lên hình ảnh bằng [/file/image/ad/upload/](../12-api-reference/47-images.md#doc-1739067433456642). Mã `image_id` trong phản hồi sẽ được dùng để tạo danh mục Superlike.
Bảo đảm hình ảnh đáp ứng các quy chuẩn kỹ thuật sau:
  - Kích thước khuyến nghị: 200 pixel chiều rộng và 200 pixel chiều cao.
  - Định dạng hình ảnh: JPG, JPEG hoặc PNG.
  - Dung lượng tệp: Trong giới hạn 50 KB.
- *(Tùy chọn)* Nếu muốn thêm cửa sổ popup tùy biến xuất hiện sau hiệu ứng tim bay giúp dẫn người xem tới trang đích khi nhấp vào, tải thêm hình ảnh popup qua [/file/image/ad/upload/](../12-api-reference/47-images.md#doc-1739067433456642). Mã `image_id` trả về sẽ được dùng để tạo danh mục Superlike.
Bảo đảm hình ảnh đáp ứng các quy chuẩn kỹ thuật sau:
  - Kích thước khuyến nghị: 620 pixel chiều rộng và 788 pixel chiều cao.
  - Định dạng hình ảnh: JPG, JPEG, PNG hoặc GIF.
  - Dung lượng tệp: Trong giới hạn 3 MB.
  
### Các bước thực hiện
1. Sử dụng [/creative/portfolio/create/](../12-api-reference/36-creative-portfolios.md#doc-1739091950439426) để tạo portfolio Nút thả tim đặc biệt (Superlike portfolio).
- Thiết lập `creative_portfolio_type` thành `SUPER_LIKE`.
- Truyền mã ID hình ảnh vào trường `image_id`.
- Tùy chọn: Chỉ định hình ảnh cửa sổ popup qua trường `pop_up_window_image_id`.
  
Endpoint này trả về mã ID danh mục thẻ (`creative_portfolio_id`) vừa tạo.

2. Sử dụng [/ad/create/](../12-api-reference/02-ads-p1.md#doc-1739953377508354) hoặc [/ad/update/](../12-api-reference/02-ads-p2.md#doc-1739953405142018) để tạo hoặc cập nhật mẫu quảng cáo của bạn.
- Để sử dụng danh mục thẻ trong quảng cáo, hãy truyền `creative_portfolio_id` vào trường `card_id`.

> **Note:** 
>  • Superlike chỉ hỗ trợ các mục tiêu chiến dịch REACH, TRAFFIC, VIDEO_VIEWS (với optimization_goal là ENGAGED_VIEW), ENGAGEMENT (với optimization_goal là PAGE_VISIT), APP_PROMOTION, WEB_CONVERSIONS và RF_REACH. • Việc dùng portfolio Superlike cho chiến dịch có mục tiêu APP_PROMOTION hoặc TRAFFIC hiện là tính năng allowlist. Vui lòng liên hệ đại diện TikTok để được kích hoạt.

---

<a id="doc-1739953274550273"></a>
<!-- doc_id: 1739953274550273 -->
<!-- doc_id: 1739953274550273 -->
# Thêm tuyên bố miễn trừ trách nhiệm (Disclaimers) vào quảng cáo
> Đường dẫn: Marketing API > Tài sản sáng tạo > Hướng dẫn > Tài sản sáng tạo > Thêm tuyên bố từ chối trách nhiệm vào quảng cáo
Khi quảng bá một số ngành hàng đặc thù (như dược phẩm, tài chính), luật pháp yêu cầu nhà quảng cáo phải hiển thị tuyên bố từ chối trách nhiệm rõ ràng trên mẫu quảng cáo. TikTok hỗ trợ hiển thị cả tuyên bố dạng văn bản thuần túy và dạng liên kết có thể nhấp vào.

## Yêu cầu kỹ thuật

* Các mục tiêu hỗ trợ:
  - Quảng cáo thủ công (Manual Ads): `APP_PROMOTION`, `WEB_CONVERSIONS`, `REACH`, `TRAFFIC`, `VIDEO_VIEWS`, `ENGAGEMENT`, `LEAD_GENERATION` (khi `catalog_enabled` là `false` hoặc không truyền), `RF_REACH`.
  - Quảng cáo Upgraded Smart+: `APP_PROMOTION`, `WEB_CONVERSIONS`, `LEAD_GENERATION` (khi `catalog_enabled` là `false` hoặc không truyền).
* Vị trí hiển thị: Chỉ áp dụng trên TikTok (`TikTok only`).
* Không áp dụng cho quảng cáo Tối ưu hóa Sáng tạo Tự động (ACO).

## Các bước cấu hình

1. Xác định định dạng: Chọn hiển thị liên kết nhấp (`TEXT_LINK`) hoặc văn bản thuần (`TEXT_ONLY`) (không dùng đồng thời cả hai dạng trong cùng một mẫu quảng cáo).
2. Khi gọi API tạo/cập nhật mẫu quảng cáo, cấu hình trường `disclaimer_type` với giá trị tương ứng (`TEXT_LINK` hoặc `TEXT_ONLY`).
3. Hoàn tất thông tin chi tiết:
	* Đối với liên kết nhấp (`TEXT_LINK`): Truyền mảng đối tượng `disclaimer_clickable_texts` gồm các cặp `text` và `url`. Tối đa 3 đối tượng; tổng độ dài toàn bộ văn bản không quá 40 ký tự. Không được truyền trường `disclaimer_text`.
	* Đối với văn bản thuần (`TEXT_ONLY`): Truyền chuỗi vào trường `text` trong đối tượng `disclaimer_text`. Độ dài tối đa 90 ký tự; chỉ được phép có 1 đối tượng duy nhất. Không được truyền trường `disclaimer_clickable_texts`.

>  **Lưu ý:**
>   • Khi cập nhật quảng cáo, bạn không thể đổi loại disclaimer (từ liên kết sang thuần văn bản hoặc ngược lại). Tuy nhiên, bạn có thể bổ sung disclaimer vào quảng cáo chưa có hoặc chỉnh sửa nội dung văn bản/URL của disclaimer hiện có.<br>
>   • Một khi đã thêm vào quảng cáo, disclaimer không thể bị xóa bỏ hoàn toàn.

- Chi tiết tham số cho Upgraded Smart+ Ads, xem [/smart_plus/ad/create/](../12-api-reference/62-upgraded-smartplus-p5.md#doc-1843317390059522), [/smart_plus/ad/update/](../12-api-reference/62-upgraded-smartplus-p6.md#doc-1843317411665921) và [/smart_plus/ad/get/](../12-api-reference/62-upgraded-smartplus-p4.md#doc-1843317378982914).
- Chi tiết tham số cho Manual Ads, xem [/ad/create/](../12-api-reference/02-ads-p1.md#doc-1739953377508354), [/ad/update/](../12-api-reference/02-ads-p2.md#doc-1739953405142018) và [/ad/get/](../12-api-reference/02-ads-p1.md#doc-1735735588640770).

---

<a id="doc-1740286998081538"></a>
<!-- doc_id: 1740286998081538 -->
<!-- doc_id: 1740286998081538 -->
# Creative tools
> Đường dẫn: Marketing API > Creatives > Guides > Creative tools
Hệ thống công cụ sáng tạo cung cấp khả năng tự động hóa việc khởi tạo, xem trước, chỉnh sửa và tối ưu hóa tài nguyên sáng tạo (hình ảnh, video và mẫu quảng cáo).
- [SDK Trình chỉnh sửa Trang tức thì (Instant Page Editor SDK)](creatives.md#doc-1740307202170881): Sử dụng công cụ này để tạo và chỉnh sửa các trang tức thì.
- [Xem trước quảng cáo (Ads Preview)](creatives.md#doc-1740317791125506): Vận hành ở chế độ bất đồng bộ, dùng để xem trước giao diện hiển thị thực tế của tài nguyên trên vị trí phân phối.
- [Gợi ý nút kêu gọi hành động (CTA Recommendations)](creatives.md#doc-1740307296329730): Nhận các đề xuất nút CTA tiêu chuẩn hoặc động để gắn vào mẫu quảng cáo.
- [Tự động sửa lỗi video (Smart Fix)](creatives.md#doc-1741472523309058): Tự động phát hiện và xử lý lỗi video (kích thước, độ phân giải) nhằm tránh bị từ chối phê duyệt trong chiến dịch.
- [Chỉnh sửa hình ảnh](../12-api-reference/38-creative-tools.md#doc-1739067107903489): Hoạt động đồng bộ, cho phép cắt và chỉnh kích thước ảnh theo ý muốn.
- [Văn bản thông minh (Smart Text)](../12-api-reference/38-creative-tools.md#doc-1739084248002626): Cung cấp gợi ý văn bản quảng cáo phù hợp với ngành hàng và sản phẩm.
- [Phát hiện bão hòa sáng tạo (Creative Fatigue Detection)](creatives.md#doc-1767568085608450): Giúp nhận biết các quảng cáo bị bão hòa nội dung để kịp thời tối ưu.
- [Chia sẻ tài nguyên sáng tạo](../12-api-reference/38-creative-tools.md#doc-1773192725768193): Chia sẻ tài nguyên sáng tạo với các tài khoản nhà quảng cáo khác.

---

<a id="doc-1740307202170881"></a>
<!-- doc_id: 1740307202170881 -->
<!-- doc_id: 1740307202170881 -->
# SDK Trình chỉnh sửa Trang tức thì (Instant Page Editor SDK)
> Đường dẫn: Marketing API > Creatives > Guides > Creative tools > Instant Page Editor SDK
TikTok Instant Page (TIP) Editor SDK là thư viện JavaScript gọn nhẹ cho phép nhúng trực tiếp trình tạo và chỉnh sửa [Trang tức thì](creatives.md#doc-1739953260466178) vào ứng dụng hoặc website quản trị nội bộ của bạn. SDK tải hoàn toàn bất đồng bộ (async), không làm chậm trang web của bạn và mở dưới dạng popup trực quan mà không cần đăng nhập vào giao diện TikTok Ads Manager.

SDK hỗ trợ tạo 4 loại trang: Trang tùy biến, Biểu mẫu tức thì (Instant Form), Trang hồ sơ ứng dụng và Biểu mẫu cửa sổ bật.
Sau khi người dùng hoàn tất thiết kế trang qua popup, bạn lấy mã định danh trang (`page_id`) thông qua endpoint [/page/get/](../12-api-reference/54-page.md#doc-1820826387779586) để gắn vào chiến dịch quảng cáo.

> **Lưu ý:**
> TIP Editor SDK hiện không hỗ trợ môi trường tài khoản thử nghiệm Sandbox.

# Hướng dẫn tạo Trang tức thì bằng TIP Editor SDK
## Điều kiện tiên quyết

Bạn đã được cấp quyền truy cập TikTok Business Marketing API. Xem chi tiết tại [Hướng dẫn bắt đầu - Quy trình tích hợp](../04-get-started/bat-dau.md#doc-1735713609895937).

## Các bước triển khai
1. Tạo mã truy cập (SDK Access Token) cho TIP Editor thông qua endpoint [/oauth2/access_token/tip_sdk/create/](../12-api-reference/54-page.md#doc-1820826755283969).

Mỗi mã token có hiệu lực trong 24 giờ. Bạn kiểm tra tính hợp lệ bằng [/oauth2/access_token/tip_sdk/validate/](../12-api-reference/54-page.md#doc-1820826826000385) và làm mới token bằng [/oauth2/access_token/tip_sdk/renew/](../12-api-reference/54-page.md#doc-1820826847199234).

2. Khởi tạo và tải mã nguồn SDK.

Đặt đoạn mã sau vào tệp HTML của bạn, thay thế `your_appid` bằng **App ID** ứng dụng của bạn (tra cứu tại **[My Apps](https://ads.tiktok.com/marketing_api/apps/)** > **App Detail** > **Basic Information**):

```html
// HTML
<script>
  // Initialize SDK
  window.InstantPageAsyncInit = (val) => {
    InstantPage.init({
      appId: 'your_appid', // App ID ứng dụng nhà phát triển của bạn
      version: 'v1.0' // Hiện tại chỉ hỗ trợ v1.0
    });
  };
</script>

<script async defer crossorigin="anonymous" src="https://sf-unpkg.tiktokcdn.com/obj/unpkg-va/latest/byted/instant_page_sdk/dist/index.js"></script>
```

3. Khởi chạy Trình tạo Trang tức thì TIP Editor.
Gọi hàm SDK `InstantPage.start()` tại thời điểm phù hợp để mở popup Trình chỉnh sửa Trang tức thì. Cú pháp gọi hàm theo định dạng: `InstantPage.start(params, callback)`.

**Example**
```JS
// JavaScript
InstantPage.start(
  {
    accountId: 'your_adv_id', //advertiser id
    appId: 'appId', // App ID ứng dụng nhà phát triển của bạn
    ixAccessToken: 'your_SDK_token', //TIP Editor SDK access token
    businessType: 1, // Support 1=Instant Form, 4=App Profile Page, 6=Customized Page, 14=pop-up form, default value: 1
    display: 'popup', // Hiện tại chỉ hỗ trợ dạng popup
    actionType: 'create', 
    language: 'en' //  Support ar,de,en,es,fr,hi,id,it,ja,ko,ms,ru,th,tr,vi,zh,zh-Hant, default value: en
  },
  (response) => {
    console.log(response);
    // pageId
    // status 
    // accountId
    // ...
  }
);
```

Bảng sau đây mô tả chi tiết các tham số của hàm khởi tạo:

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| accountId  **(Required)** | string | ID tài khoản quảng cáo TikTok. |
| appId  **(Required)** | string | ID ứng dụng nhà phát triển của bạn. ⏎ Để tra cứu **App ID**, truy cập **[My Apps](https://ads.tiktok.com/marketing_api/apps/)** > **App Detail** > **Basic Information**. |
| ixAccessToken  **(Required)** | string | Mã token truy cập TIP Editor SDK. ⏎ Để nhận token, gọi endpoint [/oauth2/access_token/tip_sdk/create/](../12-api-reference/54-page.md#doc-1820826755283969). |
| actionType  **(Required)** | string | Loại thao tác. ⏎ Các giá trị enum hỗ trợ: `create`. |
| display   **(Required)** | string | Định dạng hiển thị. ⏎ Hiện tại giá trị duy nhất được hỗ trợ là `popup`. |
| businessType | number | Loại Trang tức thì. ⏎ Các giá trị enum: • `1`: Biểu mẫu tức thì (Instant Form). • `4`: Trang hồ sơ ứng dụng (App Profile Page). • `6`: Trang tùy biến (Customized Instant Page). • `14`: Biểu mẫu popup (Pop-up Form). Giá trị mặc định: `1`. |
| language | string | Ngôn ngữ hiển thị của trình chỉnh sửa. ⏎ Giá trị mặc định: `en`. ⏎ Danh sách ngôn ngữ hỗ trợ xem tại bảng mã ngôn ngữ bên dưới. |

### Các mã ngôn ngữ được hỗ trợ cho `language`

| Value | Description |
|---|---|
| `ar` | Tiếng Ả Rập (Arabic) |
| `de` | Tiếng Đức (German) |
| `en` | Tiếng Anh (English) |
| `es` | Tiếng Tây Ban Nha (Spanish) |
| `fr` | Tiếng Pháp (French) |
| `hi` | Tiếng Hindi |
| `id` | Tiếng Indonesia |
| `it` | Tiếng Ý (Italian) |
| `ja` | Tiếng Nhật (Japanese) |
| `ko` | Tiếng Hàn (Korean) |
| `ms` | Tiếng Mã Lai (Malay) |
| `ru` | Tiếng Nga (Russian) |
| `th` | Tiếng Thái (Thai) |
| `tr` | Tiếng Thổ Nhĩ Kỳ (Turkish) |
| `vi` | Tiếng Việt (Vietnamese) |
| `zh` | Tiếng Trung giản thể (Simplified Chinese) |
| `zh-Hant` | Tiếng Trung phồn thể (Traditional Chinese) |

Bảng sau đây mô tả các tham số trong dữ liệu phản hồi của hàm callback:

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| pageId | string | ID trang tức thì (Page ID). |
| status | number | Trạng thái của trang tức thì. ⏎ Giá trị enum: • `2`: Sẵn sàng (Ready). |
| accountId | string | ID tài khoản quảng cáo TikTok. |

## Ví dụ mã nguồn HTML hoàn chỉnh

```html
// HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <title>InstantPage SDK Test</title>
</head>
<style>
    .title {
        display: flex;
        justify-content: center;
        width: 100%;
    }
</style>
<body>
<h1>InstantPage SDK Test</h1>

<!-- select page source -->
<div class="title">
    <button style="margin-top: 32px;font-size: 16px" onclick="start()">Start</button>
</div>

<script>
    /// Initialize SDK
    window.InstantPageAsyncInit = (val) => {
        InstantPage.init({
              appId: 'your_appid', // App ID ứng dụng nhà phát triển của bạn
              version: 'v1.0' // Hiện tại chỉ hỗ trợ v1.0
        });
    };

    function start() {
        // Khởi chạy SDK vào thời điểm thích hợp
        InstantPage.start(
            {
                accountId: 'your_adv_id', //advertiser id
                appId: 'appId', // App ID ứng dụng nhà phát triển của bạn
                ixAccessToken: 'your_SDK_token', //TIP Editor SDK access token
                businessType: 1, // Support 1=Instant Form, 4=App Profile Page, 6=Customized Page, 14=pop-up form, default value: 1
                display: 'popup', // Hiện tại chỉ hỗ trợ dạng popup
                actionType: 'create', // create
                language: 'en' //  Support ar,de,en,es,fr,hi,id,it,ja,ko,ms,ru,th,tr,vi,zh,zh-Hant, default value: en
            },
            (response) => {
                console.log(response);
                // pageId
                // status 2 ready
                // accountId
                // ...
            }
        );
    };
</script>
<script src="https://sf-unpkg.tiktokcdn.com/obj/unpkg-va/latest/byted/instant_page_sdk/dist/index.js"></script>
</body>
</html>
```

# Câu hỏi thường gặp (FAQ)

## Q1: Làm thế nào để cập nhật phiên bản SDK mới nhất?

**Trả lời:** Bạn không cần thực hiện nâng cấp thủ công vì đường dẫn CDN của SDK luôn trỏ về phiên bản mới nhất trên máy chủ TikTok.

## Q2: Khi nào hàm gọi lại (callback function) được kích hoạt?

**Trả lời:** Hàm callback sẽ được kích hoạt ngay khi người dùng hoàn thành việc xuất bản trang tức thì trong cửa sổ TIP Editor và đóng giao diện. Nếu người dùng tắt cửa sổ khi chưa hoàn tất thiết kế, hàm callback sẽ không được gọi.

# Các endpoint API liên quan

**Page**
- [Lấy mã định danh trang (Get the Page ID)](../12-api-reference/54-page.md#doc-1820826387779586)
- [Tạo mã token truy cập TIP Editor SDK](../12-api-reference/54-page.md#doc-1820826755283969)
- [Xác thực mã token truy cập TIP Editor SDK](../12-api-reference/54-page.md#doc-1820826826000385)
- [Làm mới mã token truy cập TIP Editor SDK](../12-api-reference/54-page.md#doc-1820826847199234)

**Khách hàng tiềm năng thử nghiệm (Test leads)**
* [Tạo khách hàng tiềm năng thử nghiệm](../12-api-reference/48-leads.md#doc-1739047132614722)
* [Lấy thông tin khách hàng tiềm năng thử nghiệm](../12-api-reference/48-leads.md#doc-1739048460493826)
* [Xóa khách hàng tiềm năng thử nghiệm](../12-api-reference/48-leads.md#doc-1739049313198081)

**Tải xuống khách hàng tiềm năng (Download leads)**
* [Tạo tác vụ tải xuống khách hàng tiềm năng](../12-api-reference/48-leads.md#doc-1739052936772610)
* [Tải xuống dữ liệu khách hàng tiềm năng](../12-api-reference/48-leads.md#doc-1739053563877378)

**Đăng ký nhận dữ liệu khách hàng tiềm năng (Subscribe to leads)**
* [Tạo gói đăng ký webhook (Subscription)](../12-api-reference/66-subscription.md#doc-1739092028876801)
* [Lấy chi tiết gói đăng ký webhook](../12-api-reference/66-subscription.md#doc-1739093832125442)
* [Hủy gói đăng ký webhook](../12-api-reference/66-subscription.md#doc-1739094758789122)

**Chuyển giao khách hàng tiềm năng (Migrate leads)**
* [Chuyển giao khách hàng tiềm năng vào Business Center](../12-api-reference/48-leads.md#doc-1740029931324417)
* [Lấy thư viện biểu mẫu](../12-api-reference/48-leads.md#doc-1740029915327489)

**Các mục khác (Others)**
* [Lấy các trường của biểu mẫu Instant Form](../12-api-reference/48-leads.md#doc-1739054080455681)
* [Lấy sự kiện trên Trang tức thì](../12-api-reference/43-events-1-0-p1.md#doc-1740898639412226)

---

<a id="doc-1740317791125506"></a>
<!-- doc_id: 1740317791125506 -->
<!-- doc_id: 1740317791125506 -->
# Xem trước quảng cáo (Ads preview)
> Đường dẫn: Marketing API > Creatives > Guides > Creative tools > Ads preview
Bạn có thể tạo liên kết xem trước giao diện thực tế của mẫu quảng cáo trên thiết bị di động trước khi khởi chạy. Tùy thuộc vào định dạng muốn xem trước, danh sách tham số sẽ khác nhau. Tra cứu chi tiết tại endpoint [/creative/ads_preview/create/](../12-api-reference/38-creative-tools.md#doc-1739403070695426).

Các định dạng hỗ trợ xem trước bao gồm:
- Mẫu quảng cáo dự kiến tạo mới
- Mẫu quảng cáo tiêu chuẩn đã tồn tại
- Thẻ sản phẩm đã cấu hình
- Trang đích tức thì sản phẩm
- Video riêng lẻ
- Hình ảnh riêng lẻ

> **Lưu ý:** Quảng cáo Tối ưu hóa sáng tạo tự động (ACO) hiện không hỗ trợ xem trước.

Phản hồi API sẽ trả về đường dẫn `preview_link` có hiệu lực trong 24 giờ. Khi hết hạn, bạn chỉ cần gọi lại endpoint để tạo đường dẫn mới.

---

<a id="doc-1740307384545345"></a>
<!-- doc_id: 1740307384545345 -->
<!-- doc_id: 1740307384545345 -->
# (Không còn hỗ trợ) Phân cảnh động (Dynamic Scene)
> Đường dẫn: Marketing API > Creatives > Guides > Creative tools > (Deprecated) Dynamic Scene
Phân cảnh động (Dynamic Scene) sử dụng thuật toán máy học để tự động ghép nối các đoạn video phân cảnh ngắn cùng các hiệu ứng chuyển cảnh và âm nhạc, tạo ra hàng loạt biến thể video quảng cáo chất lượng cao trong thời gian ngắn.

Tích hợp Dynamic Scene API cho phép bạn:
* Tăng tốc quy mô sản xuất video: Tự động ghép nối các phân cảnh thành hàng trăm biến thể video khác nhau.
* Đánh giá hiệu suất phân cảnh: Phân tích tỷ lệ giữ chân và tỷ lệ bỏ dở ở từng phân đoạn để định hướng kịch bản cho các video sau.

> **Lưu ý:** Tính năng Phân cảnh động hiện đã dừng phát triển tính năng mới và dần được thay thế bởi Smart Creative / Upgraded Smart+.

## Thuật ngữ cốt lõi

* **Phân cảnh (Scene)**: Đoạn video ngắn mang tính thông điệp hoàn chỉnh, đóng vai trò đơn vị nhỏ nhất trong kịch bản.
* **Mạch truyện (Story Arc)**: Cấu trúc tổng thể của câu chuyện video, gồm nhiều vị trí phân cảnh liên kết với nhau.

## Các bước tạo quảng cáo với Phân cảnh động

1. **Tạo chiến dịch** qua endpoint [/campaign/create/](../12-api-reference/24-campaign.md#doc-1739318962329602).
2. **Tạo nhóm quảng cáo** qua [/adgroup/create/](../12-api-reference/07-ad-groups-p2.md#doc-1739499616346114), bắt buộc đặt trường `creative_material_mode` thành `DYNAMIC`.
3. **Tải lên các đoạn phân cảnh video gốc** qua [/file/video/ad/upload/](../12-api-reference/71-video.md#doc-1737587322856449) để nhận danh sách `video_id`.
   Thông số khuyến nghị cho phân cảnh:
   - Thời lượng: 3 - 20 giây mỗi đoạn.
   - Độ phân giải: Tối thiểu 720P trở lên.
   - Định dạng khung hình: Khuyến nghị dọc (9:16); chấp nhận ngang (16:9) hoặc vuông (1:1).
4. **Tạo video phân cảnh động tự động**:
   1. Gọi [/dynamic_scene/material/submit/](../12-api-reference/41-deprecated-dynamic-scene.md#doc-1740317263937538), truyền `video_ids` để nhận `material_package_id`.
   2. Gọi [/dynamic_scene/task/create/](../12-api-reference/41-deprecated-dynamic-scene.md#doc-1740317320231938) để khởi tạo tác vụ bất đồng bộ tạo video từ gói tài nguyên `material_package_id`, nhận `task_id`.
   3. Gọi [/dynamic_scene/task/get/](../12-api-reference/41-deprecated-dynamic-scene.md#doc-1740317337705473) để thăm dò kết quả tác vụ theo `task_id`. Khi thành công, phản hồi trả về danh sách `video_id` hoàn thiện.
5. **Tạo quảng cáo tự động** qua [/ad/aco/create/](../12-api-reference/60-smart-creative.md#doc-1739473063234626), gán các ID video vừa tạo vào trường `video_id`.
6. **Xuất báo cáo phân cảnh** qua [/dynamic_scene/report/get/](../12-api-reference/41-deprecated-dynamic-scene.md#doc-1740317382510593) để xem chi tiết số lượt xem hết và số lượt bỏ ngang ở từng phân cảnh. 

## Các endpoint API liên quan 

* [Gửi tài liệu phân cảnh](../12-api-reference/41-deprecated-dynamic-scene.md#doc-1740317263937538)
* [Tạo tác vụ bất đồng bộ](../12-api-reference/41-deprecated-dynamic-scene.md#doc-1740317320231938)
* [Lấy kết quả tác vụ](../12-api-reference/41-deprecated-dynamic-scene.md#doc-1740317337705473)
* [Lấy danh sách tất cả video](../12-api-reference/41-deprecated-dynamic-scene.md#doc-1740317360823297)
* [Chạy báo cáo hiệu suất phân cảnh](../12-api-reference/41-deprecated-dynamic-scene.md#doc-1740317382510593)

---

<a id="doc-1740307296329730"></a>
<!-- doc_id: 1740307296329730 -->
<!-- doc_id: 1740307296329730 -->
# Gợi ý nút kêu gọi hành động (CTA recommendations)
> Đường dẫn: Marketing API > Creatives > Guides > Creative tools > CTA recommendations
Vì nhiều lý do khác nhau, văn bản nút kêu gọi hành động (CTA) do nhà quảng cáo tự chọn có thể chưa đạt hiệu quả tối ưu. Bạn có thể sử dụng các nút CTA do hệ thống TikTok đề xuất dựa trên phân tích ngành hàng và mục tiêu chiến dịch. 

Hệ thống cung cấp hai loại đề xuất CTA: CTA tiêu chuẩn đề xuất và CTA động (Dynamic CTAs).

## Các nút CTA tiêu chuẩn được đề xuất

CTA tiêu chuẩn đề xuất là một nút CTA cố định có thể sử dụng trực tiếp khi tạo mới hoặc cập nhật mẫu quảng cáo. 

Để sử dụng CTA tiêu chuẩn đề xuất, hãy gọi endpoint [/creative/cta/recommend/](../12-api-reference/38-creative-tools.md#doc-1739362202742785) và chọn giá trị `CTA_NORMAL` cho trường `asset_type`. Hệ thống trả về nhóm CTA được khuyến nghị để bạn gán vào trường `call_to_action` trong endpoint [/ad/create/](../12-api-reference/02-ads-p1.md#doc-1739953377508354) hoặc [/ad/update/](../12-api-reference/02-ads-p2.md#doc-1739953405142018). 

## Nút CTA động (Dynamic CTAs)

CTA động là một tập hợp các nút CTA ứng viên. Khi bật tính năng này, hệ thống sẽ tự động luân phiên hiển thị văn bản CTA phù hợp nhất theo từng đối tượng người dùng nhằm đạt tỷ lệ chuyển đổi cao nhất.

 Để sử dụng CTA động, bạn thực hiện theo các bước sau: 

1. Lấy nhóm nút CTA động thông qua [/creative/cta/recommend/](../12-api-reference/38-creative-tools.md#doc-1739362202742785). 

 Bạn có thể lựa chọn endpoint phiên bản nâng cấp hoặc phiên bản cũ. 

 **(Khuyến nghị) Tùy chọn A: Sử dụng endpoint phiên bản nâng cấp**

- Thiết lập `new_version` thành `true`.
- Bỏ qua các trường `asset_type` và `content_type`.
- Chỉ định các giá trị hợp lệ cho `advertiser_id`, `objective_type` và `promotion_type`.
- *(Không bắt buộc)* Bạn có thể chỉ định thêm các trường: `language`, `app_id`, `placements`, `region_codes`, `optimization_goal`, `ad_texts` và `landing_page_url`.

2. Tạo portfolio chứa nhóm CTA động thu được từ Bước 1 bằng endpoint [/creative/portfolio/create/](../12-api-reference/36-creative-portfolios.md#doc-1739091950439426).

- Thiết lập `creative_portfolio_type` thành `CTA`.
- Đặt trường `asset_content` và `asset_ids` tương ứng với các giá trị trả về từ `/creative/cta/recommend/` ở Bước 1.

 Dữ liệu phản hồi sẽ bao gồm mã ID danh mục thẻ (`creative_portfolio_id`) vừa được khởi tạo.

3. Sử dụng danh mục CTA động trong mẫu quảng cáo của bạn.
- Đối với quảng cáo Upgraded Smart+: Gán trường `call_to_action_id` trong endpoint [/smart_plus/ad/create/](../12-api-reference/62-upgraded-smartplus-p5.md#doc-1843317390059522) hoặc [/smart_plus/ad/update/](../12-api-reference/62-upgraded-smartplus-p6.md#doc-1843317411665921) bằng mã ID danh mục CTA động (`creative_portfolio_id`) thu được từ Bước 2.
- Đối với quảng cáo thông thường (Manual Ads): Gán trường `call_to_action_id` trong endpoint [/ad/create/](../12-api-reference/02-ads-p1.md#doc-1739953377508354) hoặc [/ad/update/](../12-api-reference/02-ads-p2.md#doc-1739953405142018) bằng mã ID danh mục CTA động (`creative_portfolio_id`) thu được từ Bước 2.

**Tùy chọn B: Sử dụng endpoint phiên bản cũ**

- Thiết lập `new_version` thành `false`, hoặc để trống không truyền. 
- Thiết lập `asset_type` thành `CTA_AUTO_OPTIMIZED`.
- Chỉ định các giá trị hợp lệ cho `advertiser_id` và `content_type`.

---

<a id="doc-1741472523309058"></a>
<!-- doc_id: 1741472523309058 -->
<!-- doc_id: 1741472523309058 -->
# Smart Fix
> Đường dẫn: Marketing API > Creatives > Guides > Creative tools > Smart Fix
Smart Fix là tính năng giúp bạn phát hiện và khắc phục các sự cố kỹ thuật của video (như kích thước, độ phân giải) có nguy cơ khiến quảng cáo bị từ chối duyệt.

Khi bật Smart Fix, hệ thống sẽ tự động phát hiện và xử lý các lỗi sau trong video của bạn: 
* `LOW_RESOLUTION`: Độ phân giải video thấp hơn 540x960px, không đáp ứng yêu cầu kỹ thuật tối thiểu của hệ thống.
* `ILLEGAL_VIDEO_SIZE`: Kích thước video không đúng quy chuẩn. Vui lòng sử dụng các tỷ lệ tiêu chuẩn: Vuông (1:1) / Dọc (9:16) / Ngang (16:9).

Chức năng của Smart Fix API bao gồm hai khía cạnh:
- Khi tải video mới lên, bạn có thể bật Smart Fix. Hệ thống sẽ tiến hành tiền kiểm duyệt video và tự động sửa nhanh các lỗi được phát hiện, giúp video tuân thủ tiêu chuẩn của TikTok.
- Đối với video đã có sẵn trong tài khoản, hệ thống cung cấp 2 endpoint để tạo tác vụ kiểm tra và lấy kết quả xử lý, giúp rà soát toàn diện các sự cố kỹ thuật.

## Hướng dẫn kích hoạt Smart Fix
### Bật Smart Fix khi tải video mới lên
1. Sử dụng endpoint [/file/video/ad/upload/](../12-api-reference/71-video.md#doc-1737587322856449) để tải video mới lên. Thiết lập các trường sau để bật Smart Fix: 
* Đặt `flaw_detect` thành `true` để tự động phát hiện lỗi trong video.
* Đặt `auto_fix_enabled` thành `true` để tự động sửa các lỗi phát hiện được. 
* Đặt `auto_bind_enabled` thành `true` nếu bạn muốn tự động tải video đã sửa vào thư viện sáng tạo.

 Nếu phát hiện lỗi, hệ thống sẽ thực hiện sửa lỗi và trả về `fix_task_id` cùng `flaw_types` trong phản hồi. 

2. Sử dụng [/video/fix/task/get/](../12-api-reference/38-creative-tools.md#doc-1741469487859714) để lấy kết quả tác vụ. 
* Truyền mã ID tác vụ sửa lỗi (`fix_task_id`) nhận được từ Bước 1 vào trường `task_id`.  
* Truyền ID tài khoản quảng cáo vào trường `advertiser_id`. 
 
 Hệ thống sẽ trả về trạng thái tác vụ trong phản hồi. Nếu trạng thái là `SUCCESS`, bạn sử dụng mã `video_id` trả về để tạo quảng cáo. 

### Bật Smart Fix cho video đã có sẵn

1. Sử dụng endpoint [/video/fix/task/create/](../12-api-reference/38-creative-tools.md#doc-1741468875279361) để tạo tác vụ bất đồng bộ kiểm tra và sửa lỗi video.
* Chọn video bạn muốn sửa lỗi và truyền mã ID video vào trường `video_id`. 
* Truyền ID tài khoản quảng cáo vào trường `advertiser_id`. 

 Nếu phát hiện lỗi, hệ thống sẽ thực hiện sửa lỗi và trả về `fix_task_id` cùng `flaw_types` trong phản hồi. 
 
 2. Sử dụng [/video/fix/task/get/](../12-api-reference/38-creative-tools.md#doc-1741469487859714) để lấy kết quả tác vụ. 
* Truyền mã ID tác vụ sửa lỗi (`fix_task_id`) nhận được từ Bước 1 vào trường `task_id`.  
* Truyền ID tài khoản quảng cáo vào trường `advertiser_id`. 
 
 Hệ thống sẽ trả về trạng thái tác vụ trong phản hồi. Nếu trạng thái là `SUCCESS`, bạn sử dụng mã `video_id` trả về để tạo quảng cáo.

---

<a id="doc-1749022727865345"></a>
<!-- doc_id: 1749022727865345 -->
<!-- doc_id: 1749022727865345 -->
# (Không còn hỗ trợ) Nhạc nền thông minh, Video thông minh và Tối ưu nhanh
> Đường dẫn: Marketing API > Tài sản sáng tạo > Hướng dẫn > Công cụ sáng tạo > (Không còn hỗ trợ) Nhạc nền thông minh (Smart Video Soundtrack), Smart Video, and Quick Optimization
Bộ công cụ Nhạc nền thông minh, Video thông minh và Tối ưu nhanh hoạt động ở chế độ bất đồng bộ, giúp cải thiện hiệu suất quảng cáo một cách tự động và tối ưu. 

## Nhạc nền video thông minh (Smart Video Soundtrack) 
Smart Video Soundtrack tự động lựa chọn bản nhạc nền phù hợp nhất với hình ảnh và chủ đề của quảng cáo. Bạn có thể thay đổi bài nhạc và tinh chỉnh âm lượng video, âm lượng nhạc để tạo ra video hấp dẫn. Công cụ cung cấp hơn 500.000 bản nhạc bản quyền thuộc 10 thể loại phong phú. 
## Video thông minh (Smart Video)
Công cụ sản xuất video thông minh ứng dụng AI tự động phân tích chất liệu gốc và nhịp điệu âm nhạc để tạo ra nhiều phiên bản video chỉ bằng một cú nhấp. Xem [Smart Video](https://ads.tiktok.com/help/article?aid=9527) để biết thêm chi tiết. 
## Tối ưu hóa nhanh (Quick Optimization)
Tối ưu nhanh (Quick Optimization) là công cụ chuyển đổi video thương hiệu của bạn thành video chuẩn định dạng TikTok chỉ trong tích tắc. Xem [Quick Optimization](https://ads.tiktok.com/help/article/quick-optimization-video-tutorial?redirected=2) để xem hướng dẫn. 
## Hướng dẫn sử dụng Nhạc nền thông minh, Video thông minh và Tối ưu nhanh 
Các công cụ sáng tạo này vận hành theo cơ chế bất đồng bộ và hỗ trợ callback:
1. Gọi endpoint của công cụ để tạo tác vụ xử lý. Mã tác vụ `task_id` sẽ được trả về trong phản hồi.
  - [Nhạc nền video thông minh (Smart Video Soundtrack)](../12-api-reference/38-creative-tools.md#doc-1739089635852289)
  - [Tối ưu hóa nhanh (Quick Optimization)](../12-api-reference/38-creative-tools.md#doc-1739355078757377)
  - [Video thông minh (Smart Video)](../12-api-reference/38-creative-tools.md#doc-1739352294717441)
2. Thăm dò trạng thái và lấy kết quả tác vụ qua endpoint **/creative/status/get/**. 
3. Nếu bạn đã cung cấp thông tin callback (`callback_info`) khi tạo tác vụ, máy chủ sẽ tự động gọi webhook gửi kết quả ngay khi xử lý xong. Xem [Chi tiết yêu cầu callback](../12-api-reference/38-creative-tools.md#doc-1739067004677122).

---

<a id="doc-1767568085608450"></a>
<!-- doc_id: 1767568085608450 -->
<!-- doc_id: 1767568085608450 -->
# Phát hiện bão hòa sáng tạo (Creative Fatigue Detection)
> Đường dẫn: Marketing API > Creatives > Guides > Creative tools > Creative Fatigue Detection
Phát hiện bão hòa sáng tạo (Creative Fatigue Detection) là tính năng giúp nhận biết hiện tượng bão hòa nội dung, xảy ra khi hiệu suất quảng cáo sụt giảm do tần suất hiển thị lặp lại quá mức đối với một nhóm khán giả. Tính năng này giúp bạn chủ động theo dõi và bổ sung nội dung mới vào cùng nhóm quảng cáo để duy trì hiệu quả chiến dịch.

## Tiêu chí xác định hiện tượng bão hòa sáng tạo
Tính năng phát hiện bão hòa sáng tạo được thực hiện bằng cách đánh giá các khía cạnh sau:
- Hiệu suất sụt giảm:
  - Chỉ số CPA (chi phí trên mỗi hành động kết quả) tăng vọt vượt ngưỡng cho phép.
  - Tốc độ cắn tiền/chi phí quảng cáo sụt giảm xuống dưới mức kỳ vọng.
- Phạm vi tiếp cận đối tượng mới suy giảm:
  - Số lượng đối tượng người dùng mới tiếp cận được ngày càng giảm và được dự báo tiếp tục suy giảm.

## Quy trình phát hiện bão hòa sáng tạo
1. **Tạo chiến dịch** bằng cách gọi [/smart_plus/campaign/create/](../12-api-reference/62-upgraded-smartplus-p1.md#doc-1843312852800706).
2. **Tạo nhóm quảng cáo** bằng endpoint [/smart_plus/adgroup/create/](../12-api-reference/62-upgraded-smartplus-p3.md#doc-1843314887930946).
3. **Tạo mẫu quảng cáo** bằng endpoint [/smart_plus/ad/create/](../12-api-reference/62-upgraded-smartplus-p5.md#doc-1843317390059522).
4. **Phát hiện bão hòa sáng tạo** bằng cách gọi [/creative_fatigue/get/](../12-api-reference/38-creative-tools.md#doc-1767568466842626).
5. *(Tùy chọn)* Nếu phát hiện tài nguyên bị bão hòa, **bổ sung thêm tài nguyên sáng tạo mới vào cùng mẫu quảng cáo** qua [/smart_plus/ad/create/](../12-api-reference/62-upgraded-smartplus-p5.md#doc-1843317390059522).

## Tài liệu liên quan
- [Lấy kết quả phát hiện bão hòa sáng tạo](../12-api-reference/38-creative-tools.md#doc-1767568466842626)

---

<a id="doc-1874110837867522"></a>
<!-- doc_id: 1874110837867522 -->
<!-- doc_id: 1874110837867522 -->
# Lấy kết quả tiền kiểm duyệt cho tài nguyên sáng tạo (Obtain pre-review results for your creatives)
> Đường dẫn: Marketing API > Creatives > Guides > Creative tools > Obtain pre-review results for your creatives
Tài liệu này hướng dẫn bạn quy trình lấy kết quả tiền kiểm duyệt nội dung sáng tạo thông qua Creative Pre-review API.

## Giới thiệu (Introduction)
Creative Pre-review API được thiết kế để tối ưu hóa quy trình xuất bản bằng cách kiểm duyệt sơ bộ các nội dung sáng tạo trước khi gắn vào chiến dịch chính thức, giúp gia tăng tỷ lệ phê duyệt và đảm bảo chiến dịch ra mắt đúng tiến độ.

Lợi ích của Creative Pre-review API bao gồm:
- **Chủ động tối ưu hóa**: Xử lý sớm các rào cản duyệt quảng cáo tiềm ẩn ngay từ khâu tiền kiểm duyệt, giúp tài nguyên sẵn sàng xuất bản.
- **Tỷ lệ phê duyệt cao vượt trội**: Tài nguyên trải qua tiền kiểm duyệt luôn tuân thủ chặt chẽ tiêu chuẩn nền tảng, đảm bảo tỷ lệ duyệt thực tế cao nhất.
- **Quy trình tinh gọn**: Tiết kiệm tối đa thời gian và chi phí bằng cách giảm thiểu việc sửa đổi qua lại nhiều lần.

## Điều kiện tiên quyết (Prerequisites)

- Bạn đã có quyền truy cập TikTok Business API. Xem chi tiết tại [Hướng dẫn bắt đầu - Quy trình tích hợp](../04-get-started/bat-dau.md#doc-1735713609895937).
  - Để sử dụng tính năng tiền kiểm duyệt, bạn cần các quyền hạn tương ứng. Xem [Tài liệu tham khảo API](../02-overview/tong-quan-va-phien-ban.md#doc-1735712062490625) để biết quyền cần thiết và xem [Cập nhật quyền ứng dụng](../04-get-started/bat-dau.md#doc-1738855280338946) để biết cách cấp quyền.

## Các bước thực hiện (Steps)

Để nhận kết quả tiền kiểm duyệt cho tài nguyên sáng tạo, hãy thực hiện các bước sau:

1. **Tạo tác vụ tiền kiểm duyệt trực tiếp cho tài nguyên** qua endpoint [/creative/pre_review/task/create/](../12-api-reference/35-creative-pre-review.md#doc-1874110632584577).
  - Tùy chọn: Bạn cũng có thể **tạo tác vụ tiền kiểm duyệt đồng thời khi tải video/hình ảnh lên tài khoản** qua endpoint [/file/video/ad/upload/](../12-api-reference/71-video.md#doc-1737587322856449) hoặc [/file/image/ad/upload/](../12-api-reference/47-images.md#doc-1739067433456642).

2. **Kiểm tra kết quả tác vụ tiền kiểm duyệt** qua endpoint [/creative/pre_review/task/get/](../12-api-reference/35-creative-pre-review.md#doc-1874110636550082).

---

<a id="doc-1739067487319042"></a>
<!-- doc_id: 1739067487319042 -->
<!-- doc_id: 1739067487319042 -->
# Báo cáo sáng tạo (Creative Reports)
> Đường dẫn: Marketing API > Creatives > Guides > Creative reports
Báo cáo chuyên sâu ở cấp tài nguyên sáng tạo giúp bạn hiểu rõ mức độ thu hút của từng video, hình ảnh đối với khán giả mục tiêu, làm cơ sở khoa học để tối ưu nội dung và phân bổ ngân sách:

- [Báo cáo sáng tạo cơ bản (Creative basic reports)](creatives.md#doc-1749023062758401): Cung cấp các chỉ số phân phối cơ bản và thông số kỹ thuật (chiều cao, chiều rộng, thời lượng...) của tài nguyên trong tài khoản.
- [Báo cáo chuyên sâu video (Video Insights reports)](creatives.md#doc-1789769972291585): Tổng hợp hiệu suất video xuyên suốt nhiều tài khoản quảng cáo, bao gồm cả Spark Ads và quảng cáo thông thường.
- [Dữ liệu chi tiết về sáng tạo (Creative insights)](creatives.md#doc-1749023065231362): Phân tích biểu đồ giữ chân người xem theo từng giây để xác định đoạn video hấp dẫn nhất.

---

<a id="doc-1749023062758401"></a>
<!-- doc_id: 1749023062758401 -->
<!-- doc_id: 1749023062758401 -->
# Báo cáo sáng tạo cơ bản (Creative basic reports)
> Đường dẫn: Marketing API > Creatives > Guides > Creative reports > Creative basic reports
Sử dụng endpoint [/creative/report/get/](../12-api-reference/37-creative-reports.md#doc-1740662135093314) để xuất báo cáo tài nguyên sáng tạo, nhận các chỉ số hiệu suất cơ bản cũng như các thuộc tính kỹ thuật như chiều cao, chiều rộng và thời lượng.  

Để tra cứu danh sách các chỉ số được hỗ trợ, xem **Các chỉ số được hỗ trợ trong báo cáo sáng tạo**.

---

<a id="doc-1789769972291585"></a>
<!-- doc_id: 1789769972291585 -->
<!-- doc_id: 1789769972291585 -->
# Báo cáo chi tiết video (Video Insights reports)
> Đường dẫn: Marketing API > Creatives > Guides > Creative reports > Video Insights reports
Sử dụng [/creative/report/get/](../12-api-reference/37-creative-reports.md#doc-1789700050715650) để tạo báo cáo Video Insights cho nhiều video trên một hoặc nhiều tài khoản quảng cáo, bao gồm cả Spark Ads và quảng cáo tiêu chuẩn.

Để tra cứu các chỉ số Video Insights được API hỗ trợ, xem [Các chỉ số được hỗ trợ trong báo cáo Video Insights](../12-api-reference/37-creative-reports.md#doc-1789703614085122).

---

<a id="doc-1749023065231362"></a>
<!-- doc_id: 1749023065231362 -->
<!-- doc_id: 1749023065231362 -->
# Dữ liệu chi tiết sáng tạo (Creative insights)
> Đường dẫn: Marketing API > Creatives > Guides > Creative reports > Creative insights
Dữ liệu chi tiết sáng tạo giúp bạn tối ưu hóa mẫu quảng cáo đạt hiệu quả cao nhất. Chúng tôi cung cấp 3 loại dữ liệu: dữ liệu đối sánh chuẩn ngành (benchmark), dữ liệu hiệu suất theo từng giây và dữ liệu phân tích khung hình Video Insights.

## Dữ liệu đối sánh chuẩn ngành (Benchmark data)
Bạn có thể gọi [/report/ad_benchmark/get/](../12-api-reference/37-creative-reports.md#doc-1738824501176321) để lấy dữ liệu so sánh quảng cáo với tiêu chuẩn chuẩn ngành. 

## Dữ liệu hiệu suất quảng cáo theo từng giây (Second-level ad performance data)
Bạn có thể gọi [/report/video_performance/get/](../12-api-reference/37-creative-reports.md#doc-1738825259075586) để truy xuất dữ liệu phân tích theo từng giây của mẫu quảng cáo. 

## Dữ liệu chi tiết Video Insights
Bạn cũng có thể gọi endpoint [/report/video_performance/get/](../12-api-reference/37-creative-reports.md#doc-1738825259075586) để trích xuất dữ liệu chi tiết Video Insights cho một video cụ thể. 
 
Hiện tại, hệ thống hỗ trợ các chỉ số khung hình chính (key frame) như CTR và chuyển đổi, cho phép phân tích từng giây để phát hiện các khung hình hiệu quả cao và khung hình gây sụt giảm tương tác, từ đó liên tục tối ưu các video sau.
 
Để tra cứu danh sách chỉ số được hỗ trợ, xem [/report/video_performance/get/](../12-api-reference/37-creative-reports.md#doc-1738825259075586). Xem thêm thông tin về Video Insights tại [Trung tâm trợ giúp](https://ads.tiktok.com/help/article/video-insights?redirected=2&lang=en).

---

<a id="doc-1740649324143617"></a>
<!-- doc_id: 1740649324143617 -->
<!-- doc_id: 1740649324143617 -->
# Danh mục API (API reference)
> Đường dẫn: Marketing API > Creatives > API reference
Creative APIs bao gồm các nhóm endpoint sau:

- **Tài nguyên sáng tạo (Creative assets)**:
 	* [Danh mục sáng tạo (Creative portfolios)](../12-api-reference/36-creative-portfolios.md#doc-1739091934311426)
		- [Tạo mới danh mục portfolio](../12-api-reference/36-creative-portfolios.md#doc-1739091950439426)
		- [Lấy thông tin danh mục portfolio](../12-api-reference/36-creative-portfolios.md#doc-1739092113671170)
		- [Danh sách portfolio trong tài khoản](../12-api-reference/36-creative-portfolios.md#doc-1766324010279938)
		- [Xóa portfolio](../12-api-reference/36-creative-portfolios.md#doc-1834560049625089)
	* [Hình ảnh (Images)](../12-api-reference/47-images.md#doc-1739067422728193)
	* [Tài nguyên Video (Video API)](../12-api-reference/71-video.md#doc-1737587293087810)
	* [Âm nhạc (Music)](../12-api-reference/52-music.md#doc-1740052369141761)
	* [Trang đích (Page)](../12-api-reference/54-page.md#doc-1737719918220290)
- **Công cụ sáng tạo (Creative tools)**:
	- [Chỉnh sửa hình ảnh](../12-api-reference/38-creative-tools.md#doc-1739067107903489)
	- [Xem trước quảng cáo hoặc tài nguyên](../12-api-reference/38-creative-tools.md#doc-1739403070695426)
	- [Gợi ý văn bản quảng cáo thông minh](../12-api-reference/38-creative-tools.md#doc-1739084248002626)
	- [Gợi ý nút kêu gọi hành động CTA](../12-api-reference/38-creative-tools.md#doc-1739362202742785)
	- [Tạo tác vụ tự động sửa lỗi video Smart Fix](../12-api-reference/38-creative-tools.md#doc-1741468875279361) 
	- [Lấy kết quả tác vụ Smart Fix](../12-api-reference/38-creative-tools.md#doc-1741469487859714)
	- [Lấy kết quả phát hiện bão hòa sáng tạo](../12-api-reference/38-creative-tools.md#doc-1767568466842626)
	- [Chia sẻ tài nguyên sáng tạo](../12-api-reference/38-creative-tools.md#doc-1773192725768193)
	- [Xóa tài nguyên sáng tạo](../12-api-reference/38-creative-tools.md#doc-1797202997456897)	
- **Báo cáo sáng tạo (Creative reports)**:
	- [Báo cáo sáng tạo cơ bản](../12-api-reference/37-creative-reports.md#doc-1740662135093314)
	- [Báo cáo chi tiết video (Video Insights)](../12-api-reference/37-creative-reports.md#doc-1789700050715650)
	* [Dữ liệu chi tiết sáng tạo (Creative Insights)](../12-api-reference/37-creative-reports.md#doc-1738824477276162)
		- [Lấy dữ liệu đối sánh chuẩn ngành (Benchmarks)](../12-api-reference/37-creative-reports.md#doc-1738824501176321)
		- [Lấy dữ liệu hiệu suất theo từng giây](../12-api-reference/37-creative-reports.md#doc-1738825259075586)
- **Tin nhắn chào mừng (Welcome Messages)**:
	- [Tạo tin nhắn chào mừng trong tài khoản](../12-api-reference/73-welcome-messages.md#doc-1822106113771521)
	- [Lấy danh sách tin nhắn chào mừng](../12-api-reference/73-welcome-messages.md#doc-1822106498804738)
---

## Hướng dẫn thực hành Data Retrieval (Python & cURL)

Dưới đây là mã nguồn mẫu minh họa quy trình gọi API thực tế cho phân hệ **Hướng dẫn Creatives**:

### cURL mẫu
```bash
curl -s -X GET "https://business-api.tiktok.com/open_api/v1.3/example/get/?advertiser_id=YOUR_ADVERTISER_ID" \
  -H "Access-Token: YOUR_ACCESS_TOKEN"
```

### Python script mẫu
```python
import requests
import json

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ADVERTISER_ID = "YOUR_ADVERTISER_ID"
BASE_URL = "https://business-api.tiktok.com/open_api/v1.3"

headers = {
    "Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}

def execute_request():
    url = f"{BASE_URL}/example/get/"
    params = {"advertiser_id": ADVERTISER_ID}
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    if data.get("code") == 0:
        print("Truy vấn thành công:", data.get("data"))
        return data.get("data")
    else:
        print(f"Lỗi: {data.get('code')} - {data.get('message')}")
        return None

if __name__ == "__main__":
    execute_request()
```

