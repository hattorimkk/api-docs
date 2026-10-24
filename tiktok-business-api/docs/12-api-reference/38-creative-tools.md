# Công cụ sáng tạo (Creative Tools)

Tài liệu hướng dẫn và tham chiếu toàn bộ các API thuộc nhóm Công cụ sáng tạo (Creative Tools) trên TikTok Business API.

---

<a id="doc-1737583624272897"></a>
<!-- doc_id: 1737583624272897 -->
## 1. Tổng quan về Công cụ sáng tạo (Creative Tools Overview)

Bộ công cụ sáng tạo (Creative Tools) của TikTok cung cấp giải pháp toàn diện hỗ trợ nhà quảng cáo và nhà phát triển trong việc xem trước (preview), tạo lập, tối ưu hóa và quản lý hiệu suất tài sản hình ảnh và video quảng cáo.

Các tính năng nổi bật bao gồm:
- **Xem trước quảng cáo đa định dạng:** Xem trước mẫu quảng cáo trước khi xuất bản hoặc xem trước các quảng cáo hiện có, video đơn, hình ảnh đơn, trang tức thì (Instant Page) và tiện ích tương tác (Interactive Add-on).
- **Chỉnh sửa hình ảnh thông minh:** Cắt ảnh theo kích thước cố định, phủ mờ Gaussian viền ảnh tự động phù hợp với chuẩn định dạng quảng cáo.
- **Tạo và tối ưu video:** Chuyển đổi khung hình video ngang sang dọc, ghép nhạc nền tự động, tạo video thông minh.
- **Chia sẻ và quản lý tài sản:** Chia sẻ hình ảnh, video, âm nhạc giữa các tài khoản quảng cáo và dọn dẹp tài sản không còn sử dụng.
- **Gợi ý văn bản và CTA thông minh:** Tự động tạo nội dung tiêu đề quảng cáo và đề xuất các nút kêu gọi hành động (Call To Action - CTA) tối ưu theo ngành hàng và mục tiêu chiến dịch.
- **Khắc phục lỗi video (Smart Fix):** Tự động phát hiện và sửa các lỗi hiển thị phổ biến của video quảng cáo.
- **Phát hiện suy giảm hiệu quả sáng tạo (Creative Fatigue Detection):** Đo lường và cảnh báo khi mẫu quảng cáo bị bão hòa để kịp thời làm mới nội dung.

### Danh mục các Endpoint trong nhóm:
1. [Chi tiết yêu cầu Webhook Callback (Callback request details)](#2-chi-tiết-yêu-cầu-webhook-callback-deprecated): Thông số kỹ thuật callback webhook khi hoàn thành tác vụ video.
2. [Chỉnh sửa hình ảnh (Edit an image)](#3-chỉnh-sửa-hình-ảnh-edit-an-image): `POST /open_api/v1.3/creative/image/edit/`
3. [Xem trước quảng cáo hoặc mẫu sáng tạo (Preview an ad or creative)](#4-xem-trước-quảng-cáo-hoặc-mẫu-sáng-tạo-preview-an-ad-or-a-creative): `POST /open_api/v1.3/creative/ads_preview/create/`
4. [Tạo tác vụ nhạc nền video thông minh (Smart Video Soundtrack)](#5-tạo-tác-vụ-nhạc-nền-video-thông-minh-deprecated): `POST /open_api/v1.3/creative/video_soundtrack/create/`
5. [Tạo tác vụ tối ưu hóa nhanh (Quick Optimization)](#6-tạo-tác-vụ-tối-ưu-hóa-nhanh-deprecated): `POST /open_api/v1.3/creative/quick_optimization/create/`
6. [Tạo tác vụ video thông minh (Smart Video)](#7-tạo-tác-vụ-video-thông-minh-deprecated): `POST /open_api/v1.3/creative/smart_video/create/`
7. [Chia sẻ tài sản sáng tạo (Share creative assets)](#8-chia-sẻ-tài-sản-sáng-tạo-share-creative-assets): `POST /open_api/v1.3/creative/asset/share/`
8. [Xóa tài sản sáng tạo (Delete creative assets)](#9-xóa-tài-sản-sáng-tạo-delete-creative-assets): `POST /open_api/v1.3/creative/asset/delete/`
9. [Nhận gợi ý văn bản thông minh (Get Smart Text recommendations)](#10-nhận-gợi-ý-văn-bản-thông-minh-get-smart-text-recommendations): `POST /open_api/v1.3/creative/smart_text/generate/`
10. [Nhận gợi ý nút kêu gọi hành động CTA (Get recommended CTAs)](#11-nhận-gợi-ý-nút-kêu-gọi-hành-động-cta-get-recommended-ctas): `GET /open_api/v1.3/creative/cta/recommend/`
11. [Tạo tác vụ sửa lỗi video Smart Fix (Create a Smart Fix task)](#12-tạo-tác-vụ-sửa-lỗi-video-smart-fix-create-a-smart-fix-task): `POST /open_api/v1.3/video/fix/task/create/`
12. [Lấy kết quả tác vụ Smart Fix (Get results of a Smart Fix task)](#13-lấy-kết-quả-tác-vụ-smart-fix-get-the-results-of-a-smart-fix-task): `GET /open_api/v1.3/video/fix/task/get/`
13. [Lấy kết quả phát hiện suy giảm hiệu quả sáng tạo (Creative Fatigue Detection)](#14-lấy-kết-quả-phát-hiện-suy-giảm-hiệu-quả-sáng-tạo): `GET /open_api/v1.3/creative_fatigue/get/`

---

<a id="doc-1739067004677122"></a>
<!-- doc_id: 1739067004677122 -->
## 2. Chi tiết yêu cầu Webhook Callback (Deprecated)

Nếu bạn cung cấp tham số `callback_url` khi khởi tạo một tác vụ xử lý sáng tạo (ví dụ trong các tác vụ tạo video thông minh hoặc tối ưu nhanh), máy chủ TikTok sẽ gửi yêu cầu HTTP POST đến URL này ngay sau khi tác vụ hoàn thành. Thông tin bổ sung `callback_extra_info` được chỉ định khi tạo tác vụ sẽ được gửi trả nguyên vẹn trong trường `extra_info` của body yêu cầu callback cùng kết quả xử lý.

> **Yêu cầu xử lý Webhook:**
> - Khi nhận được yêu cầu webhook thành công, máy chủ của bạn cần phản hồi mã trạng thái HTTP 200 trong vòng 5 giây.
> - Nếu quá 5 giây hoặc gặp lỗi kết nối, hệ thống TikTok sẽ tự động gửi lại yêu cầu (thử lại tối đa 2 lần). Hãy đảm bảo endpoint callback của bạn được thiết kế có tính lũy thừa (idempotency) để xử lý các yêu cầu gửi lại an toàn.

### Thông tin Yêu cầu Callback
- **URL nhận:** Đường dẫn `callback_url` bạn đã cung cấp khi tạo tác vụ video.
- **Phương thức:** `POST`

### Tiêu đề HTTP (Header)
| Header | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Content-Type | string | Có | Kiểu nội dung của yêu cầu: `application/json`. |

### Tham số Body (Callback Payload)
| Tham số | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `task_id` | string | Có | Mã ID định danh của tác vụ xử lý sáng tạo. |
| `status` | string | Có | Trạng thái hoàn thành của tác vụ: `SUCCESS` (thành công), `FAILED` (thất bại), `PROCESSING` (đang xử lý). |
| `video_ids` | string[] | Điều kiện | Danh sách mã ID của các video đã được tạo/tối ưu thành công. Chỉ xuất hiện khi `status` là `SUCCESS`. |
| `error_msg` | string | Điều kiện | Thông báo lỗi chi tiết nếu tác vụ thất bại. |
| `extra_info` | object | Điều kiện | Dữ liệu bổ sung `callback_extra_info` mà bạn đã truyền vào khi tạo tác vụ ban đầu. |

### Ví dụ Payload Webhook nhận được
```json
{
  "task_id": "task_v3_vid_897123456789",
  "status": "SUCCESS",
  "video_ids": [
    "v09033a60000bt1posj6hujpgbgomlo2",
    "v090336c0000bt1pp2ac3teiuedco26s"
  ],
  "extra_info": {
    "campaign_internal_id": "cmp_2026_q4_flash_sale"
  }
}
```

---

<a id="doc-1739067107903489"></a>
<!-- doc_id: 1739067107903489 -->
## 3. Chỉnh sửa hình ảnh (Edit an image)

Sử dụng endpoint này để chỉnh sửa kích thước hoặc áp dụng các hiệu ứng cắt/mờ viền sáng tạo cho một hình ảnh đã tải lên Thư viện tài sản (Asset Library). Hình ảnh sau khi chỉnh sửa sẽ được tự động lưu vào Thư viện tài sản của tài khoản quảng cáo và hệ thống sẽ trả về mã hình ảnh (`image_id`) mới để tạo quảng cáo.

Nếu bạn cần tải ảnh mới lên Thư viện tài sản, hãy sử dụng endpoint `/file/image/ad/upload/`.

### Các phương thức chỉnh sửa hình ảnh (`edit_method`):
1. `fix_size`: Cắt hình ảnh theo chiều rộng và chiều cao cố định, không tạo hiệu ứng viền mờ.
2. `only_gauss_pad`: Chỉ áp dụng hiệu ứng làm mờ Gaussian cho phần viền để đạt tỷ lệ mong muốn, không cắt xén nội dung ảnh gốc.
3. `gauss_padding_reserve_score`: Tự động cân đối làm mờ Gaussian thông minh dựa trên kích thước và bố cục của chủ thể chính trong bức ảnh gốc.

> **Khuyến nghị độ phân giải:** Đối với hình ảnh quảng cáo, nên sử dụng độ phân giải tối thiểu ≥ 1.200 × 628px để đảm bảo chất lượng hiển thị sắc nét nhất.

### Thông tin Endpoint
- **URL:** `https://business-api.tiktok.com/open_api/v1.3/creative/image/edit/`
- **Phương thức:** `POST`

### Tiêu đề HTTP (Header)
| Header | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Có | Access Token được cấp quyền xác thực. |
| Content-Type | string | Có | Kiểu nội dung yêu cầu: `application/json`. |

### Tham số Body (Request Body)
| Tham số | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | Có | ID của tài khoản quảng cáo. |
| `image_id` | string | Có | ID hình ảnh gốc trong thư viện tài sản cần chỉnh sửa. |
| `edit_method` | string | Không | Phương thức chỉnh sửa: `fix_size` (mặc định), `only_gauss_pad`, `gauss_padding_reserve_score`. |
| `width` | number | Có | Chiều rộng mong muốn của hình ảnh sau khi chỉnh sửa (pixel). |
| `height` | number | Có | Chiều cao mong muốn của hình ảnh sau khi chỉnh sửa (pixel). |
| `image_name` | string | Không | Tên đặt cho hình ảnh mới. Nếu để trống, hệ thống sẽ tự động tạo tên ngẫu nhiên. |

### Tham số Response
| Trường | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi từ API (`0` thể hiện thành công). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Log ID định danh duy nhất của yêu cầu hệ thống. |
| `data` | object | Dữ liệu hình ảnh sau khi chỉnh sửa thành công. |
| ↳ `image_id` | string | Mã ID hình ảnh mới dùng để tạo quảng cáo. |
| ↳ `material_id` | string | Mã định danh vật liệu (Material ID) trong kho tài nguyên. |
| ↳ `displayable` | boolean | Khả năng hiển thị được của ảnh trên nền tảng (`true`/`false`). |
| ↳ `width` | number | Chiều rộng thực tế của ảnh sau chỉnh sửa. |
| ↳ `height` | number | Chiều cao thực tế của ảnh sau chỉnh sửa. |
| ↳ `format` | string | Định dạng tệp ảnh (ví dụ: `jpeg`, `png`). |
| ↳ `image_url` | string | Đường dẫn URL xem ảnh (có hiệu lực trong vòng 1 giờ). |
| ↳ `signature` | string | Chuỗi MD5 hash định danh của tệp hình ảnh. |
| ↳ `size` | number | Dung lượng tệp ảnh tính theo Byte. |
| ↳ `file_name` | string | Tên tệp hình ảnh. |
| ↳ `create_time` | string | Thời gian tạo (UTC, định dạng ISO 8601). |
| ↳ `modify_time` | string | Thời gian chỉnh sửa cập nhật (UTC). |

### Ví dụ cURL
```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/creative/image/edit/" \
  -H "Access-Token: YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "advertiser_id": "7112345678901234567",
    "image_id": "ad-site-i18n/202610235d0de2e725f892ed4e31beb4",
    "edit_method": "fix_size",
    "width": 1200,
    "height": 628,
    "image_name": "hero_banner_1200x628"
  }'
```

### Ví dụ Python
```python
import requests

url = "https://business-api.tiktok.com/open_api/v1.3/creative/image/edit/"
headers = {
    "Access-Token": "YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}
payload = {
    "advertiser_id": "7112345678901234567",
    "image_id": "ad-site-i18n/202610235d0de2e725f892ed4e31beb4",
    "edit_method": "gauss_padding_reserve_score",
    "width": 720,
    "height": 1280
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())
```

### Phản hồi thành công mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202610231305000101",
  "data": {
    "image_id": "ad-site-i18n/202610231305009876543210abcdef",
    "material_id": "7223344556677889910",
    "displayable": true,
    "width": 720,
    "height": 1280,
    "format": "jpeg",
    "image_url": "https://p16-va.tiktokcdn.com/obj/ad-site-i18n/202610231305009876543210abcdef",
    "signature": "d96d4e822020e862ed43e1d0bd104fda",
    "size": 184520,
    "file_name": "hero_banner_vertical",
    "create_time": "2026-10-23T13:05:00Z",
    "modify_time": "2026-10-23T13:05:00Z"
  }
}
```

---

<a id="doc-1739403070695426"></a>
<!-- doc_id: 1739403070695426 -->
## 4. Xem trước quảng cáo hoặc mẫu sáng tạo (Preview an ad or a creative)

Sử dụng endpoint này để tạo liên kết xem trước (preview link) cho quảng cáo hoặc các tài nguyên sáng tạo. Bạn có thể xem trước mẫu quảng cáo trước khi chính thức tạo chiến dịch hoặc xem trước các quảng cáo, video, hình ảnh, trang tức thì và tiện ích tương tác đã có sẵn trong tài khoản.

### Thông tin Endpoint
- **URL:** `https://business-api.tiktok.com/open_api/v1.3/creative/ads_preview/create/`
- **Phương thức:** `POST`

### Tiêu đề HTTP (Header)
| Header | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Có | Access Token được cấp quyền xác thực. |
| Content-Type | string | Có | Kiểu nội dung yêu cầu: `application/json`. |

---

### A. Xem trước quảng cáo dự định tạo (`preview_type` = `ADS_CREATION`)

Cho phép bạn xem trước định dạng và trải nghiệm người dùng của quảng cáo dựa trên các tham số cấu hình trước khi khởi tạo quảng cáo thực tế trên hệ thống.

| Tham số | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | Có | ID tài khoản quảng cáo. Bạn cần có quyền Quản trị viên (Admin) hoặc Nhà vận hành (Toán tử điều kiện). |
| `preview_type` | string | Có | Kiểu xem trước. Để xem trước quảng cáo dự định tạo, điền `ADS_CREATION`. |
| `objective_type` | string | Có | Mục tiêu quảng cáo: `REACH`, `TRAFFIC`, `VIDEO_VIEWS`, `ENGAGEMENT`, `APP_PROMOTION`, `LEAD_GENERATION`, `WEB_CONVERSIONS`, `PRODUCT_SALES`, `RF_REACH`. |
| `is_smart_performance_campaign` | boolean | Không | Chiến dịch có phải là Smart+ Campaign hay không. Mặc định: `false`. |
| `placement` | string | Không | Vị trí phân phối ứng dụng: `PLACEMENT_TIKTOK`, `PLACEMENT_PANGLE`, `PLACEMENT_GLOBAL_APP_BUNDLE`, `ALL`. Khi `ad_format` là `CAROUSEL_ADS` hoặc `CATALOG_CAROUSEL`, đặt là `PLACEMENT_TIKTOK` hoặc bỏ qua. |
| `tiktok_subplacement` | string | Không | Vị trí phụ bên trong TikTok (khi mục tiêu là `REACH` và vị trí là `PLACEMENT_TIKTOK`). Giá trị: `LEMON8`, `UNSET`. |
| `preview_format` | string | Không | Định dạng xem trước tùy theo vị trí phân phối: `IN_FEED`, `SEARCH_RESULTS`, `SEARCH_FEED`, `TIKTOK_LITE`, `PRODUCT_SEARCH`, `PRODUCT_SHOP_CENTER`. |
| `shopping_ads_type` | string | Điều kiện | Bắt buộc khi `objective_type` là `PRODUCT_SALES`. Các giá trị enum: `VIDEO`, `LIVE`, `PRODUCT_SHOPPING_ADS`. |
| `product_source` | string | Điều kiện | Nguồn sản phẩm (cho Video Shopping Ads và Product Shopping Ads): `STORE` (TikTok Shop), `SHOWCASE`, `CATALOG`. |
| `store_id` | string | Điều kiện | ID của TikTok Shop. Bắt buộc khi `product_source` là `STORE`. |
| `store_authorized_bc_id` | string | Điều kiện | ID của Business Center ủy quyền TikTok Shop khi truyền `store_id`. |
| `showcase_products` | object[] | Điều kiện | Danh sách sản phẩm từ Showcase khi `shopping_ads_type` là `VIDEO` và `product_source` là `SHOWCASE`. |
| ↳ `item_group_id` | string | Có | Mã SPU ID của sản phẩm trong Showcase. |
| ↳ `store_id` | string | Có | ID của cửa hàng tương ứng trong Showcase. |
| `promotion_type` | string | Điều kiện | Loại hình quảng bá: `WEBSITE`, `APP_ANDROID`, `APP_IOS`, `LEAD_GENERATION`. |
| `identity_id` | string | Có | ID của danh tính người sáng tạo hoặc tài khoản TikTok phát quảng cáo. |
| `identity_type` | string | Có | Loại danh tính: `CUSTOMIZED_USER`, `AUTH_CODE`, `TT_USER`, `BC_AUTH_TT`. |
| `identity_authorized_bc_id` | string | Điều kiện | ID của Business Center cấp quyền danh tính khi `identity_type` là `BC_AUTH_TT`. |
| `ad_format` | string | Có | Định dạng quảng cáo: `SINGLE_VIDEO`, `SINGLE_IMAGE`, `CAROUSEL_ADS`, `CATALOG_CAROUSEL`, `LIVE_CONTENT`. |
| `video_id` | string | Điều kiện | ID của video quảng cáo. Bắt buộc khi `ad_format` là `SINGLE_VIDEO`. |
| `image_ids` | string[] | Điều kiện | Danh sách ID hình ảnh (dùng cho quảng cáo xoay vòng ảnh Carousel hoặc ảnh đơn). |
| `end_card_cta` | string | Điều kiện | Nút kêu gọi hành động hiển thị trên thẻ kết thúc (End Card) của video. |
| `music_id` | string | Điều kiện | ID âm nhạc đính kèm mẫu quảng cáo. |
| `tiktok_item_id` | string | Điều kiện | ID bài viết TikTok khi sử dụng Spark Ads (`identity_type` là `AUTH_CODE` hoặc `BC_AUTH_TT`). |
| `carousel_image_index` | integer | Không | Chỉ số thứ tự ảnh trong Carousel làm ảnh đại diện xem trước. |
| `ad_text` | string | Điều kiện | Văn bản mô tả quảng cáo hiển thị cho người dùng. |
| `call_to_action` | string | Điều kiện | Văn bản nút kêu gọi hành động CTA (ví dụ: `SHOP_NOW`, `LEARN_MORE`, `SIGN_UP`...). |
| `call_to_action_id` | string | Điều kiện | ID gói danh mục CTA tùy chỉnh linh hoạt. |
| `card_id` | string | Không | ID tiện ích tương tác sáng tạo (Interactive Add-on như Display Card, Countdown Sticker, Gift Code...). |
| `landing_page_url` | string | Điều kiện | Đường dẫn URL trang đích của trang web quảng cáo. |
| `page_id` | string | Điều kiện | ID trang tức thì TikTok Instant Page để xem trước trang đích tốc độ cao. |
| `catalog_id` | string | Điều kiện | ID danh mục sản phẩm (ID danh mục sản phẩm) khi chạy quảng cáo động hoặc `CATALOG_CAROUSEL`. |
| `product_specific_type` | string | Điều kiện | Chiều kích thước chọn sản phẩm trong danh mục: `ALL` (tất cả), `PRODUCT_SET` (tập hợp sản phẩm), `CUSTOMIZED_PRODUCTS` (sản phẩm tùy chọn). |
| `item_group_ids` | string[] | Điều kiện | Danh sách mã SPU ID của các nhóm sản phẩm trong catalog hoặc store. |
| `product_set_id` | string | Điều kiện | ID bộ sản phẩm được chỉ định từ danh mục catalog. |
| `sku_ids` | string[] | Điều kiện | Danh sách mã SKU sản phẩm thương mại điện tử (tối đa 20 SKU). |
| `hotel_ids` | string[] | Không | Danh sách ID khách sạn cho quảng cáo du lịch (tối đa 20 ID). |
| `flight_ids` | string[] | Không | Danh sách ID chuyến bay cho ngành vé máy bay (tối đa 20 ID). |
| `destination_ids` | string[] | Không | Danh sách ID điểm đến du lịch (tối đa 20 ID). |
| `vehicle_ids` | string[] | Điều kiện | Danh sách ID phương tiện xe ô tô cho danh mục ô tô Auto-Model (tối đa 20 ID). |
| `auto_disclaimer_types` | string[] | Không | Kiểu điều khoản miễn trừ trách nhiệm cho quảng cáo ô tô: `EMISSION`, `DISCOUNT`. |
| `catalog_authorized_bc_id` | string | Không | ID của Business Center được ủy quyền quản lý danh mục catalog (`bc_id`). |
| `dynamic_format` | string | Không | Định dạng động: `UNSET`, `DYNAMIC_CREATIVE`. |
| `vertical_video_strategy` | string | Không | Chiến lược video dọc: `SINGLE_VIDEO`, `CATALOG_VIDEOS`, `LIVE_STREAM`, `UNSET`. |
| `shopping_ads_video_template_id` | string | Không | ID mẫu gói video sản phẩm mẫu. |
| `shopping_ads_fallback_type` | string | Điều kiện | Loại trang đích dự phòng khi liên kết sâu deeplink không kích hoạt được: `DEFAULT`, `CUSTOM`, `SHOPPING_ADS`. |
| `dynamic_destination` | string | Không | Chiến lược trang đích động: `DLP` (Dynamic Landing Page), `UNSET`. |
| `instant_product_page_used` | boolean | Không | Có sử dụng trang sản phẩm tức thì TikTok Instant Product Page hay không (`true`/`false`). |

---

### B. Xem trước quảng cáo hiện có (`preview_type` = `AD`)

| Tham số | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | Có | ID tài khoản quảng cáo. |
| `preview_type` | string | Có | Điền giá trị `AD`. |
| `ad_id` | string | Có | ID của quảng cáo đã được tạo trên hệ thống cần xem trước. |
| `device` | string[] | Không | Danh sách các kiểu dòng thiết bị cần mô phỏng xem trước. |
| `language` | string | Không | Ngôn ngữ quảng cáo: `ENGLISH`, `CHINESE`, `JAPANESE`. Mặc định: `ENGLISH`. |
| `placement` | string | Không | Vị trí phân phối muốn mô phỏng (ví dụ: `PLACEMENT_TIKTOK`). |

---

### C. Xem trước tiện ích tương tác hiện có (`preview_type` = `CARD`)

| Tham số | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | Có | ID tài khoản quảng cáo. |
| `preview_type` | string | Có | Điền giá trị `CARD`. |
| `card_id` | string | Có | ID của tiện ích tương tác sáng tạo (Display Card, Gift Code...). |

---

### D. Xem trước trang tức thì hiện có (`preview_type` = `PAGE`)

| Tham số | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | Có | ID tài khoản quảng cáo. |
| `preview_type` | string | Có | Điền giá trị `PAGE`. |
| `page_id` | string | Có | ID của TikTok Instant Page cần xem trước. |

---

### E. Xem trước video đơn (`preview_type` = `SINGLE_VIDEO`)

| Tham số | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | Có | ID tài khoản quảng cáo. |
| `preview_type` | string | Có | Điền giá trị `SINGLE_VIDEO`. |
| `video_id` | string | Có | ID của tệp video trong thư viện. |
| `thumbnail` | string | Không | ID hình ảnh đại diện (thumbnail) của video. |
| `profile_image` | string | Không | ID hình ảnh đại diện (avatar) của tài khoản phát quảng cáo. |
| `display_name` | string | Có | Tên thương hiệu hiển thị (1 - 40 ký tự tiếng Anh). |
| `ad_text` | string | Có | Nội dung văn bản mô tả quảng cáo (1 - 100 ký tự). |
| `call_to_action` | string | Điều kiện | Văn bản nút kêu gọi hành động CTA. |
| `call_to_action_id` | string | Điều kiện | ID gói nút CTA tùy chỉnh. |
| `placements` | string[] | Có | Danh sách vị trí phân phối (ví dụ: `["PLACEMENT_TIKTOK"]`). |
| `device` | string[] | Không | Dòng thiết bị mô phỏng hiển thị. |
| `language` | string | Không | Ngôn ngữ quảng cáo (`ENGLISH`, `CHINESE`, `JAPANESE`). |

---

### F. Xem trước hình ảnh đơn (`preview_type` = `SINGLE_IMAGE`)

| Tham số | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | Có | ID tài khoản quảng cáo. |
| `preview_type` | string | Có | Điền giá trị `SINGLE_IMAGE`. |
| `image_id` | string | Có | ID hình ảnh trong thư viện tài sản. |
| `display_name` | string | Có | Tên thương hiệu hiển thị (1 - 40 ký tự). |
| `ad_text` | string | Có | Nội dung văn bản quảng cáo (1 - 100 ký tự). |
| `call_to_action` | string | Điều kiện | Văn bản nút kêu gọi hành động CTA. |
| `call_to_action_id` | string | Điều kiện | ID gói nút CTA tùy chỉnh. |
| `placements` | string[] | Có | Danh sách vị trí phân phối. |
| `device` | string[] | Không | Dòng thiết bị mô phỏng hiển thị. |
| `language` | string | Không | Ngôn ngữ quảng cáo. |

---

### Tham số Response
| Trường | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi từ API (`0` là thành công). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Log ID định danh duy nhất của yêu cầu hệ thống. |
| `data` | object | Dữ liệu trả về. |
| ↳ `preview_link` | string | Đường dẫn liên kết xem trước trực tiếp trên trình duyệt hoặc điện thoại. Thời hạn hiệu lực: 30 ngày đối với `ADS_CREATION` hoặc `AD`; 24 giờ đối với `CARD`, `PAGE`, `SINGLE_VIDEO` hoặc `SINGLE_IMAGE`. |
| ↳ `iframe` | string | Đoạn mã nhúng thẻ `<iframe>` chứa đường dẫn xem trước để bạn tích hợp trực tiếp vào giao diện web nội bộ. |
| ↳ `tips` | list | Danh sách các gợi ý điều chỉnh tối ưu hóa để mẫu quảng cáo đạt chất lượng hiển thị tốt nhất. |
| ↳↳ `placement` | string | Vị trí phân phối chưa phù hợp cần điều chỉnh (nếu có). |
| ↳↳ `messages` | string[] | Danh sách thông điệp chi tiết về các lỗi hiển thị hoặc cảnh báo kỹ thuật. |

### Ví dụ cURL
```bash
# Xem trước quảng cáo video đơn dự định tạo
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/creative/ads_preview/create/" \
  -H "Access-Token: YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "advertiser_id": "7112345678901234567",
    "preview_type": "ADS_CREATION",
    "objective_type": "WEB_CONVERSIONS",
    "placement": "PLACEMENT_TIKTOK",
    "identity_id": "7098765432109876543",
    "identity_type": "CUSTOMIZED_USER",
    "ad_format": "SINGLE_VIDEO",
    "video_id": "v09033a60000bt1posj6hujpgbgomlo2",
    "ad_text": "Khám phá bộ sưu tập thời trang thu đông mới nhất ngay hôm nay!",
    "call_to_action": "SHOP_NOW",
    "landing_page_url": "https://example.com/collection/autumn-winter"
  }'
```

### Ví dụ Python
```python
import requests

url = "https://business-api.tiktok.com/open_api/v1.3/creative/ads_preview/create/"
headers = {
    "Access-Token": "YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}
payload = {
    "advertiser_id": "7112345678901234567",
    "preview_type": "ADS_CREATION",
    "objective_type": "PRODUCT_SALES",
    "shopping_ads_type": "VIDEO",
    "product_source": "STORE",
    "store_id": "7299999888877776666",
    "placement": "PLACEMENT_TIKTOK",
    "identity_id": "7098765432109876543",
    "identity_type": "TT_USER",
    "ad_format": "SINGLE_VIDEO",
    "vertical_video_strategy": "SINGLE_VIDEO",
    "video_id": "v09033a60000bt1posj6hujpgbgomlo2",
    "ad_text": "Ưu đãi sốc cho đơn hàng đầu tiên!",
    "call_to_action": "ORDER_NOW"
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())
```

### Phản hồi thành công mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202610231306000101",
  "data": {
    "preview_link": "https://ads.tiktok.com/ad_preview_tool?ad_preview_id=5681cba0fcd211eab33c351a98abcdef",
    "iframe": "<iframe src=\"https://ads.tiktok.com/ad_preview_tool?ad_preview_id=5681cba0fcd211eab33c351a98abcdef\"></iframe>",
    "tips": [
      {
        "placement": "PLACEMENT_TIKTOK",
        "messages": [
          "Video resolution is optimal for 9:16 vertical full screen."
        ]
      }
    ]
  }
}
```

---

<a id="doc-1739089635852289"></a>
<!-- doc_id: 1739089635852289 -->
## 5. Tạo tác vụ nhạc nền video thông minh (Deprecated)

> **Cảnh báo không dùng nữa (Deprecated):** Endpoint này đã ngừng được khuyến nghị phát triển mới. Vui lòng chuyển sang sử dụng các công cụ tạo video hiện đại trên TikTok Ads Manager hoặc các API thế hệ mới.

Sử dụng endpoint này để tạo một tác vụ lồng ghép nhạc nền thông minh (Smart Video Soundtrack) cho video quảng cáo. Thời gian xử lý tác vụ tương đương khoảng 1/2 thời lượng của video.

### Giới hạn tần suất gọi API (Rate Limits):
| Level | Query Per Second | Query Per Minute | Query Per Day |
|---|---|---|---|
| Basic | 1 | 30 | 5000 |
| Advanced | 2 | 60 | 10000 |
| Premium | 3 | 90 | 15000 |

> **Lưu ý bản quyền âm nhạc:** Bạn không được phép tải xuống, phân phối hoặc phát lại tệp video/âm nhạc tạo từ endpoint này trên bất kỳ nền tảng nào khác ngoài TikTok trừ khi có sự đồng ý riêng từ chủ sở hữu bản quyền âm nhạc.

### Thông tin Endpoint
- **URL:** `https://business-api.tiktok.com/open_api/v1.3/creative/video_soundtrack/create/`
- **Phương thức:** `POST`

### Tiêu đề HTTP (Header)
| Header | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Có | Access Token được cấp quyền xác thực. |
| Content-Type | string | Có | Kiểu nội dung yêu cầu: `application/json`. |

### Tham số Body (Request Body)
| Tham số | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | Có | ID của tài khoản quảng cáo. |
| `video_id` | string | Có | ID của video gốc cần ghép nhạc nền. |
| `music_ids` | string[] | Không | Danh sách mã ID âm nhạc tùy chọn bạn muốn sử dụng (tối đa < 9 ID). Nếu muốn dùng nhạc do AI hệ thống tự động đề xuất, hãy bỏ qua trường này. |
| `video_volume` | float | Không | Âm lượng video gốc. Dải giá trị: [0, 1]. Mặc định: `0.5`. |
| `music_volume` | float | Không | Âm lượng nhạc nền. Dải giá trị: [0, 1]. Mặc định: `0.5`. |
| `name_prefix` | string | Không | Tiền tố đặt cho tên video mới tạo (1 - 90 ký tự). Nếu để trống, hệ thống dùng tên video gốc làm `name_prefix`. |
| `callback_info` | object | Không | Cấu hình webhook nhận kết quả xử lý tự động khi hoàn thành. |
| ↳ `callback_url` | string | Điều kiện | Địa chỉ URL webhook nhận thông báo kết quả. Bắt buộc khi truyền `callback_info`. |
| ↳ `callback_extra_info` | object | Không | Thông tin bổ sung tùy chỉnh được gửi trả nguyên vẹn trong payload webhook. |

### Tham số Response
| Trường | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi từ API (`0` là thành công). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Log ID định danh duy nhất của yêu cầu hệ thống. |
| `data` | object | Dữ liệu trả về. |
| ↳ `task_id` | string | Mã định danh tác vụ xử lý âm thanh video được tạo thành công. |

### Ví dụ cURL
```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/creative/video_soundtrack/create/" \
  -H "Access-Token: YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "advertiser_id": "7112345678901234567",
    "video_id": "v09033a60000bt1posj6hujpgbgomlo2",
    "video_volume": 0.4,
    "music_volume": 0.6,
    "name_prefix": "promo_autumn",
    "callback_info": {
      "callback_url": "https://api.example.com/tiktok/callback",
      "callback_extra_info": {
        "batch_id": "batch_music_01"
      }
    }
  }'
```

### Ví dụ Python
```python
import requests

url = "https://business-api.tiktok.com/open_api/v1.3/creative/video_soundtrack/create/"
headers = {
    "Access-Token": "YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}
payload = {
    "advertiser_id": "7112345678901234567",
    "video_id": "v09033a60000bt1posj6hujpgbgomlo2",
    "music_volume": 0.7
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())
```

### Phản hồi thành công mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202610231307000101",
  "data": {
    "task_id": "task_v3_snd_9876543210abcdef"
  }
}
```

---

<a id="doc-1739355078757377"></a>
<!-- doc_id: 1739355078757377 -->
## 6. Tạo tác vụ tối ưu hóa nhanh (Deprecated)

> **Cảnh báo không dùng nữa (Deprecated):** Tính năng này chủ yếu chuyển đổi video ngang (Horizontal) sang video dọc (Vertical) và đã ngừng hỗ trợ cho các tích hợp mới.

Sử dụng endpoint này để khởi tạo tác vụ tối ưu hóa video nhanh. Thời gian thực thi xấp xỉ 1/2 thời lượng của video. Tên video tạo ra có định dạng `_optimize_.mp4`.

### Giới hạn tần suất gọi API (Rate Limits):
| Level | Query Per Second | Query Per Minute | Query Per Day |
|---|---|---|---|
| Basic | 1 | 30 | 5000 |
| Advanced | 2 | 60 | 10000 |
| Premium | 3 | 90 | 15000 |

### Thông tin Endpoint
- **URL:** `https://business-api.tiktok.com/open_api/v1.3/creative/quick_optimization/create/`
- **Phương thức:** `POST`

### Tiêu đề HTTP (Header)
| Header | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Có | Access Token được cấp quyền xác thực. |
| Content-Type | string | Có | Kiểu nội dung yêu cầu: `application/json`. |

### Tham số Body (Request Body)
| Tham số | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | Có | ID của tài khoản quảng cáo. |
| `video_id` | string | Có | ID của video gốc cần tối ưu hóa khung hình. |
| `logo` | string | Không | ID hình ảnh logo thương hiệu sẽ xuất hiện trong video tối ưu. |
| `title` | string | Không | Tiêu đề hiển thị trong video (từ 2 - 20 ký tự). |
| `description` | string | Không | Đoạn mô tả hiển thị trong video. |
| `callback_info` | object | Không | Cấu hình callback webhook khi xử lý xong video. |
| ↳ `callback_url` | string | Điều kiện | Địa chỉ URL callback webhook. Bắt buộc khi truyền `callback_info`. |
| ↳ `callback_extra_info` | object | Không | Dữ liệu bổ sung được phản hồi nguyên vẹn qua webhook. |

### Tham số Response
| Trường | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi từ API (`0` là thành công). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Log ID định danh duy nhất của yêu cầu hệ thống. |
| `data` | object | Dữ liệu trả về. |
| ↳ `task_id` | string | Mã ID định danh của tác vụ tối ưu hóa video vừa tạo. |

### Ví dụ cURL
```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/creative/quick_optimization/create/" \
  -H "Access-Token: YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "advertiser_id": "7112345678901234567",
    "video_id": "v09033a60000bt1posj6hujpgbgomlo2",
    "title": "Sale Mùa Hè 50%",
    "callback_info": {
      "callback_url": "https://api.example.com/tiktok/callback"
    }
  }'
```

### Ví dụ Python
```python
import requests

url = "https://business-api.tiktok.com/open_api/v1.3/creative/quick_optimization/create/"
headers = {
    "Access-Token": "YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}
payload = {
    "advertiser_id": "7112345678901234567",
    "video_id": "v09033a60000bt1posj6hujpgbgomlo2",
    "title": "Khám Phá Ngay"
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())
```

### Phản hồi thành công mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202610231308000101",
  "data": {
    "task_id": "task_v3_opt_1234567890abcdef"
  }
}
```

---

<a id="doc-1739352294717441"></a>
<!-- doc_id: 1739352294717441 -->
## 7. Tạo tác vụ video thông minh (Deprecated)

> **Cảnh báo không dùng nữa (Deprecated):** Endpoint tạo video thông minh này đã ngừng sử dụng. 

Sử dụng endpoint này để khởi tạo tác vụ tự động ghép và sản xuất video quảng cáo thông minh từ danh sách hình ảnh, video ngắn, văn bản và mẫu khung hình kết thúc. Tên video tạo ra có định dạng `video_smart_video_.mp4`.

### Giới hạn tần suất gọi API (Rate Limits):
| Level | Query Per Second | Query Per Minute | Query Per Day |
|---|---|---|---|
| Basic | 1 | 30 | 5000 |
| Advanced | 2 | 60 | 10000 |
| Premium | 3 | 90 | 15000 |

### Thông tin Endpoint
- **URL:** `https://business-api.tiktok.com/open_api/v1.3/creative/smart_video/create/`
- **Phương thức:** `POST`

### Tiêu đề HTTP (Header)
| Header | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Có | Access Token được cấp quyền xác thực. |
| Content-Type | string | Có | Kiểu nội dung yêu cầu: `application/json`. |

### Tham số Body (Request Body)
| Tham số | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | Có | ID tài khoản quảng cáo. |
| `videos` | object[] | Điều kiện | Danh sách tệp video đầu vào (tối đa ≤ 5 video). Phải truyền ít nhất `videos` hoặc `images`. |
| ↳ `video_id` | string | Có | ID của video tài nguyên. |
| ↳ `tag` | string | Không | Nhãn phân loại tài liệu (Material tag). |
| `images` | object[] | Điều kiện | Danh sách tệp hình ảnh đầu vào (tối đa ≤ 10 ảnh). Phải truyền ít nhất `videos` hoặc `images`. |
| ↳ `image_id` | string | Có | ID của hình ảnh tài nguyên. |
| ↳ `tag` | string | Không | Nhãn phân loại tài liệu. |
| `texts` | object[] | Không | Danh sách câu chữ hiển thị trong video. |
| ↳ `text` | string | Có | Nội dung văn bản. |
| ↳ `tag` | string | Không | Nhãn phân loại văn bản. |
| `layout` | string | Có | Bố cục màn hình hiển thị: `VERTICAL` (video dọc), `HORIZONTAL` (video ngang). |
| `style` | string | Có | Phong cách nhạc nền: `PEACEFUL` (nhẹ nhàng), `DYNAMIC` (sôi động), `CUSTOM` (tùy chỉnh). |
| `music_id` | string | Điều kiện | ID của bài nhạc cụ thể. Bắt buộc khi `style` là `CUSTOM`. |
| `duration` | number | Không | Thời lượng video mong muốn (tối đa 60 giây). |
| `frame` | object[] | Không | Cấu hình khung hình chính / khung hình kết thúc (Keyframe). |
| ↳ `frame_type` | string | Không | Loại khung hình. Hỗ trợ: `FINAL_FRAME` (khung hình kết thúc). |
| ↳ `material_type` | string | Không | Loại vật liệu: `VIDEO`, `IMAGE`, `TEMPLATE`. |
| ↳ `video_id` | string | Điều kiện | ID video khi `material_type` là `VIDEO`. |
| ↳ `image_id` | string | Điều kiện | ID hình ảnh khi `material_type` là `IMAGE`. |
| ↳ `template_type` | string | Điều kiện | Kiểu mẫu template tạo sẵn (ví dụ: `end_frame_vertical_3`...). Bắt buộc khi `material_type` là `TEMPLATE`. |
| ↳ `logo` | string | Điều kiện | ID hình ảnh logo thương hiệu khi dùng mẫu template. |
| ↳ `call_to_action` | string | Điều kiện | Lời kêu gọi hành động hiển thị ở khung cuối (khuyến nghị < 20 ký tự). |
| ↳ `slogan` | string | Điều kiện | Câu khẩu hiệu slogan của thương hiệu (khuyến nghị < 40 ký tự). |
| ↳ `brand_name` | string | Điều kiện | Tên thương hiệu hiển thị ở khung cuối (khuyến nghị < 40 ký tự). |
| `callback_info` | object | Không | Thông tin callback webhook khi tác vụ hoàn tất. |
| ↳ `callback_url` | string | Điều kiện | Địa chỉ nhận webhook. |
| ↳ `callback_extra_info` | object | Không | Dữ liệu bổ sung kèm theo webhook. |

### Tham số Response
| Trường | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi từ API (`0` là thành công). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Log ID định danh duy nhất của yêu cầu hệ thống. |
| `data` | object | Dữ liệu trả về. |
| ↳ `task_id` | string | ID định danh tác vụ tạo video thông minh. |

### Ví dụ cURL
```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/creative/smart_video/create/" \
  -H "Access-Token: YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "advertiser_id": "7112345678901234567",
    "layout": "VERTICAL",
    "style": "DYNAMIC",
    "images": [
      {
        "image_id": "ad-site-i18n/20261023img01"
      },
      {
        "image_id": "ad-site-i18n/20261023img02"
      }
    ],
    "texts": [
      {
        "text": "Bộ sưu tập mùa thu mới"
      }
    ]
  }'
```

### Ví dụ Python
```python
import requests

url = "https://business-api.tiktok.com/open_api/v1.3/creative/smart_video/create/"
headers = {
    "Access-Token": "YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}
payload = {
    "advertiser_id": "7112345678901234567",
    "layout": "VERTICAL",
    "style": "DYNAMIC",
    "images": [{"image_id": "ad-site-i18n/20261023img01"}],
    "duration": 15
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())
```

### Phản hồi thành công mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202610231309000101",
  "data": {
    "task_id": "task_v3_smart_vid_11223344"
  }
}
```

---

<a id="doc-1773192725768193"></a>
<!-- doc_id: 1773192725768193 -->
## 8. Chia sẻ tài sản sáng tạo (Share creative assets)

Sử dụng endpoint này để chia sẻ các tài sản sáng tạo có sẵn trong một tài khoản quảng cáo (hình ảnh, video, âm nhạc) sang các tài khoản quảng cáo khác.

### Điều kiện thực hiện:
- Bạn phải có quyền Quản trị viên (Admin) hoặc Nhà vận hành (Toán tử điều kiện) trên cả tài khoản quảng cáo nguồn (đang sở hữu tài sản) và các tài khoản quảng cáo đích (nhận chia sẻ).
- Bạn phải là chủ sở hữu hợp pháp của các tài nguyên sáng tạo đó.
- Thao tác chỉ thất bại nếu ở tài khoản đích đã tồn tại một tài nguyên sáng tạo trùng tên với tài nguyên bạn muốn chia sẻ.

### Thông tin Endpoint
- **URL:** `https://business-api.tiktok.com/open_api/v1.3/creative/asset/share/`
- **Phương thức:** `POST`

### Tiêu đề HTTP (Header)
| Header | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Có | Access Token được cấp quyền xác thực. |
| Content-Type | string | Có | Kiểu nội dung yêu cầu: `application/json`. |

### Tham số Body (Request Body)
| Tham số | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | Có | ID tài khoản quảng cáo người vận hành (tài khoản nguồn sở hữu tài sản). |
| `asset_type` | string | Không | Loại tài sản sáng tạo cần chia sẻ: `VIDEO`, `IMAGE`, `MUSIC`. Mặc định: `VIDEO`. |
| `material_ids` | string[] | Có | Danh sách ID tài nguyên sáng tạo cần chia sẻ (tối đa 20 ID). |
| `shared_advertiser_ids` | string[] | Có | Danh sách ID các tài khoản quảng cáo đích nhận chia sẻ tài nguyên (tối đa 10 tài khoản). |

### Tham số Response
| Trường | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi từ API (`0` là thành công). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Log ID định danh duy nhất của yêu cầu hệ thống. |
| `data` | object | Dữ liệu trả về. |
| ↳ `failed_infos` | map<string, string[]> | Bản đồ thông tin chi tiết về các tài nguyên bị chia sẻ thất bại theo từng tài khoản đích (nếu có trùng tên). Khóa (key): ID tài khoản quảng cáo đích; Giá trị (value): Danh sách ID tài nguyên chia sẻ không thành công. |

### Ví dụ cURL
```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/creative/asset/share/" \
  -H "Access-Token: YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "advertiser_id": "7112345678901234567",
    "asset_type": "VIDEO",
    "material_ids": [
      "v09033a60000bt1posj6hujpgbgomlo2"
    ],
    "shared_advertiser_ids": [
      "7112345678909876543"
    ]
  }'
```

### Ví dụ Python
```python
import requests

url = "https://business-api.tiktok.com/open_api/v1.3/creative/asset/share/"
headers = {
    "Access-Token": "YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}
payload = {
    "advertiser_id": "7112345678901234567",
    "asset_type": "IMAGE",
    "material_ids": ["ad-site-i18n/20261023img01"],
    "shared_advertiser_ids": ["7112345678909876543"]
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())
```

### Phản hồi thành công mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202610231310000101",
  "data": {
    "failed_infos": {}
  }
}
```

---

<a id="doc-1797202997456897"></a>
<!-- doc_id: 1797202997456897 -->
## 9. Xóa tài sản sáng tạo (Delete creative assets)

Sử dụng endpoint này để xóa bớt các tài sản sáng tạo (hình ảnh hoặc video) không còn nhu cầu sử dụng trong tài khoản quảng cáo nhằm giải phóng dung lượng thư viện.

### Thông tin Endpoint
- **URL:** `https://business-api.tiktok.com/open_api/v1.3/creative/asset/delete/`
- **Phương thức:** `POST`

### Tiêu đề HTTP (Header)
| Header | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Có | Access Token được cấp quyền xác thực. |
| Content-Type | string | Có | Kiểu nội dung yêu cầu: `application/json`. |

### Tham số Body (Request Body)
| Tham số | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | Có | ID của tài khoản quảng cáo. |
| `video_ids` | string[] | Không | Danh sách mã ID video cần xóa (tối đa 50 ID trong danh sách). |
| `image_ids` | string[] | Không | Danh sách mã ID hình ảnh cần xóa (tối đa 50 ID trong danh sách). |

### Tham số Response
| Trường | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi từ API (`0` là thành công). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Log ID định danh duy nhất của yêu cầu hệ thống. |
| `data` | object | Dữ liệu trả về. |
| ↳ `failed_video_ids` | string[] | Danh sách các ID video xóa không thành công (nếu có video đang được chiến dịch quảng cáo hoạt động sử dụng). |
| ↳ `failed_image_ids` | string[] | Danh sách các ID hình ảnh xóa không thành công. |

### Ví dụ cURL
```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/creative/asset/delete/" \
  -H "Access-Token: YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "advertiser_id": "7112345678901234567",
    "video_ids": [
      "v09033a60000bt1posj6hujpgbgomlo2"
    ],
    "image_ids": [
      "ad-site-i18n/20261023img01"
    ]
  }'
```

### Ví dụ Python
```python
import requests

url = "https://business-api.tiktok.com/open_api/v1.3/creative/asset/delete/"
headers = {
    "Access-Token": "YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}
payload = {
    "advertiser_id": "7112345678901234567",
    "video_ids": ["v09033a60000bt1posj6hujpgbgomlo2"]
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())
```

### Phản hồi thành công mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202610231311000101",
  "data": {
    "failed_video_ids": [],
    "failed_image_ids": []
  }
}
```

---

<a id="doc-1739084248002626"></a>
<!-- doc_id: 1739084248002626 -->
## 10. Nhận gợi ý văn bản thông minh (Get Smart Text recommendations)

Sử dụng endpoint này để nhận các đề xuất văn bản quảng cáo thông minh (Smart Text). 

Smart Text là tính năng tự động tạo văn bản quảng cáo ứng dụng AI, giúp gợi ý các mẫu tiêu đề và mô tả quảng cáo hấp dẫn, có độ liên quan cao nhất tới ngành hàng và sản phẩm của bạn trên TikTok. Tính năng này giúp tiết kiệm thời gian sáng tạo nội dung và nâng cao tỷ lệ nhấp chuột.

Tính năng Smart Text hỗ trợ các ngôn ngữ: Tiếng Anh (`EN`), Tiếng Nhật (`JA`), Tiếng Nga (`RU`), Tiếng Việt (`VI`) (hiện chưa khả dụng cho các tài khoản đăng ký tại Hoa Kỳ và Canada).

### A. Tạo gợi ý văn bản quảng cáo
- **URL:** `https://business-api.tiktok.com/open_api/v1.3/creative/smart_text/generate/`
- **Phương thức:** `POST`

#### Tiêu đề HTTP (Header)
| Header | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Có | Access Token được cấp quyền xác thực. |

#### Tham số Form-Urlencoded (Request Parameters)
| Tham số | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | Có | ID của tài khoản quảng cáo. |
| `adgroup_id` | string | Có | ID của nhóm quảng cáo. |
| `param_type` | string | Không | Phương thức truyền tham số:<ul><li>`RECOMMENDED`: Hệ thống tự động dự đoán ngôn ngữ, ngành hàng và từ khóa dựa trên thông tin nhóm quảng cáo.</li><li>`CUSTOMIZED`: Bạn tự chỉ định cụ thể các tham số để kết quả chính xác nhất (mặc định).</li></ul> |
| `language` | string | Điều kiện | Ngôn ngữ văn bản cần tạo: `EN`, `JA`, `RU`, `VI`. Bắt buộc khi `param_type` là `CUSTOMIZED`. |
| `industry_id` | string | Không | ID ngành nghề kinh doanh. |
| `keywords` | string[] | Điều kiện | Danh sách từ khóa mô tả sản phẩm/dịch vụ. Bắt buộc khi `param_type` là `CUSTOMIZED`. |
| `limit` | number | Không | Số lượng câu văn bản cần tạo (từ 1 đến 20). Mặc định: `10`. |

#### Tham số Response
| Trường | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi từ API (`0` là thành công). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Log ID định danh duy nhất của yêu cầu hệ thống. |
| `data` | object | Dữ liệu trả về. |
| ↳ `generate_id` | string | Mã ID định danh của phiên tạo văn bản gợi ý. |
| ↳ `industry_id` | string | ID ngành hàng được chỉ định hoặc do AI dự đoán. |
| ↳ `language` | string | Mã ngôn ngữ được sử dụng. |
| ↳ `texts` | string[] | Danh sách các câu văn bản quảng cáo gợi ý được AI sinh ra. |

---

### B. Gửi phản hồi văn bản đã sử dụng (Send Back the Text Being Used)

Để giúp cải thiện độ chính xác và chất lượng của các đề xuất văn bản trong tương lai, bạn nên gửi phản hồi về những câu văn bản đã thực tế được áp dụng vào mẫu quảng cáo.

- **URL:** `https://business-api.tiktok.com/open_api/v1.3/creative/smart_text/feedback/`
- **Phương thức:** `POST`

#### Tiêu đề HTTP (Header)
| Header | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Có | Access Token được cấp quyền xác thực. |

#### Tham số Body (Request Parameters)
| Tham số | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | Có | ID tài khoản quảng cáo. |
| `adgroup_id` | string | Có | ID nhóm quảng cáo. |
| `generated_text_id` | string | Có | Mã ID của văn bản đã được tạo từ endpoint gợi ý (`generate_id`). |
| `selected_titles` | object[] | Có | Danh sách các tiêu đề đã được bạn lựa chọn sử dụng trong quảng cáo. Có thể để mảng rỗng nếu không có tiêu đề nào được chọn. |
| ↳ `generated_title` | string | Có | Câu văn bản gốc được AI sinh ra từ `/creative/smart_text/generate/`. |
| ↳ `final_title` | string | Có | Tiêu đề thực tế cuối cùng được bạn đưa vào mẫu quảng cáo (nếu bạn dùng nguyên vẹn câu của AI thì điền trùng với `generated_title`). |

#### Ví dụ cURL
```bash
# 1. Tạo gợi ý văn bản quảng cáo tiếng Việt
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/creative/smart_text/generate/" \
  -H "Access-Token: YOUR_ACCESS_TOKEN" \
  --data-urlencode "advertiser_id=7112345678901234567" \
  --data-urlencode "adgroup_id=7112345678909876543" \
  --data-urlencode "param_type=CUSTOMIZED" \
  --data-urlencode "language=VI" \
  --data-urlencode 'keywords=["thời trang", "giảm giá", "freeship"]' \
  --data-urlencode "limit=5"

# 2. Gửi phản hồi văn bản đã chọn
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/creative/smart_text/feedback/" \
  -H "Access-Token: YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "advertiser_id": "7112345678901234567",
    "adgroup_id": "7112345678909876543",
    "generated_text_id": "3414796565638865",
    "selected_titles": [
      {
        "generated_title": "Ưu đãi sốc mùa hè! Mua ngay freeship toàn quốc",
        "final_title": "Ưu đãi sốc mùa hè! Mua ngay freeship toàn quốc hôm nay"
      }
    ]
  }'
```

#### Ví dụ Python
```python
import requests

url = "https://business-api.tiktok.com/open_api/v1.3/creative/smart_text/generate/"
headers = {
    "Access-Token": "YOUR_ACCESS_TOKEN"
}
data = {
    "advertiser_id": "7112345678901234567",
    "adgroup_id": "7112345678909876543",
    "param_type": "CUSTOMIZED",
    "language": "VI",
    "keywords": '["giày thể thao", "chính hãng"]',
    "limit": 5
}

response = requests.post(url, headers=headers, data=data)
print(response.json())
```

#### Phản hồi thành công mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202610231312000101",
  "data": {
    "generate_id": "3414796565638865",
    "industry_id": "29140301",
    "language": "VI",
    "texts": [
      "Giày thể thao êm ái, bứt phá mọi giới hạn!",
      "Hàng chính hãng giá cực hời - Đặt ngay hôm nay!",
      "Freeship toàn quốc cho đơn hàng đầu tiên!"
    ]
  }
}
```

---

<a id="doc-1739362202742785"></a>
<!-- doc_id: 1739362202742785 -->
## 11. Nhận gợi ý nút kêu gọi hành động CTA (Get recommended CTAs)

Sử dụng endpoint này để lấy danh sách các nút kêu gọi hành động (Call To Action - CTA) được đề xuất tối ưu cho chiến dịch quảng cáo.

Hệ thống hỗ trợ 2 nhóm CTA:
- **Nút CTA tiêu chuẩn được đề xuất (Standard Recommended CTAs):** Các văn bản nút CTA cố định phù hợp với từng định dạng nội dung.
- **Nút CTA động (Dynamic CTAs):** Tự động luân chuyển và cá nhân hóa nội dung nút bấm dựa trên hành vi và sở thích của từng người xem cụ thể.

### Thông tin Endpoint
- **URL:** `https://business-api.tiktok.com/open_api/v1.3/creative/cta/recommend/`
- **Phương thức:** `GET`

### Tiêu đề HTTP (Header)
| Header | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Có | Access Token được cấp quyền xác thực. |

### Tham số Query (Query Parameters)
| Tham số | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | Có | ID của tài khoản quảng cáo. |
| `new_version` | boolean | Không | Có sử dụng phiên bản API mới hỗ trợ truy xuất CTA động dựa trên thiết lập quảng cáo hay không (`true`/`false`). Mặc định: `false`. |
| `asset_type` | string | Điều kiện | Bắt buộc khi `new_version` là `false`. Loại tài sản CTA: `CTA_NORMAL` (CTA tiêu chuẩn), `CTA_AUTO_OPTIMIZED` (CTA động). Bị bỏ qua khi `new_version` là `true`. |
| `content_type` | string | Điều kiện | Bắt buộc khi `new_version` là `false`. Loại nội dung quảng cáo: `APP_DOWNLOAD`, `LANDING_PAGE`, `OTHER`, `MESSAGE`, `SOCIAL_MEDIA_APP_MESSAGE`, `PHONE_CALL`. |
| `objective_type` | string | Điều kiện | Bắt buộc khi `new_version` là `true`. Mục tiêu quảng cáo (ví dụ: `WEB_CONVERSIONS`, `APP_PROMOTION`...). |
| `promotion_type` | string | Điều kiện | Bắt buộc khi `new_version` là `true`. Vị trí tối ưu hóa quảng bá: `WEBSITE`, `APP_ANDROID`, `APP_IOS`... |
| `language` | string | Không | Mã ngôn ngữ cho văn bản nút CTA (ví dụ: `en`, `vi`, `fr`...). Mặc định: `en`. Hợp lệ khi `new_version` là `true`. |
| `app_id` | string | Không | ID của ứng dụng được quảng bá khi `new_version` là `true`. |
| `placements` | string[] | Không | Vị trí phân phối ứng dụng: `PLACEMENT_TIKTOK`, `PLACEMENT_PANGLE`, `PLACEMENT_GLOBAL_APP_BUNDLE`. |
| `region_codes` | string[] | Không | Mã các quốc gia hoặc khu vực mục tiêu (ví dụ: `["VN"]`, `["US"]`). |
| `optimization_goal` | string | Không | Mục tiêu tối ưu hóa kết quả đo lường được (Optimization Goal). |
| `ad_texts` | string[] | Không | Danh sách văn bản mô tả quảng cáo (từ 1 - 100 ký tự). |
| `landing_page_url` | string | Không | Đường dẫn URL trang đích mà người dùng sẽ chuyển tiếp tới. |

### Tham số Response
| Trường | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi từ API (`0` là thành công). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Log ID định danh duy nhất của yêu cầu hệ thống. |
| `data` | object | Dữ liệu trả về. |
| ↳ `cta_list` | object[] | Danh sách các đề xuất CTA. |
| ↳↳ `cta_id` | string | ID định danh của gói CTA hoặc nút CTA. |
| ↳↳ `cta_text` | string | Văn bản hiển thị trên nút CTA (ví dụ: `SHOP_NOW`, `TẢI_NGAY`, `MUA_NGAY`...). |

### Ví dụ cURL
```bash
# Lấy gợi ý CTA theo cấu hình quảng cáo mới
curl -X GET "https://business-api.tiktok.com/open_api/v1.3/creative/cta/recommend/?advertiser_id=7112345678901234567&new_version=true&objective_type=WEB_CONVERSIONS&promotion_type=WEBSITE&language=vi" \
  -H "Access-Token: YOUR_ACCESS_TOKEN"
```

### Ví dụ Python
```python
import requests

url = "https://business-api.tiktok.com/open_api/v1.3/creative/cta/recommend/"
headers = {
    "Access-Token": "YOUR_ACCESS_TOKEN"
}
params = {
    "advertiser_id": "7112345678901234567",
    "new_version": True,
    "objective_type": "WEB_CONVERSIONS",
    "promotion_type": "WEBSITE",
    "language": "vi"
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

### Phản hồi thành công mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202610231313000101",
  "data": {
    "cta_list": [
      {
        "cta_id": "cta_btn_01",
        "cta_text": "MUA_NGAY"
      },
      {
        "cta_id": "cta_btn_02",
        "cta_text": "TÌM_HIỂU_THÊM"
      }
    ]
  }
}
```

---

<a id="doc-1741468875279361"></a>
<!-- doc_id: 1741468875279361 -->
## 12. Tạo tác vụ sửa lỗi video Smart Fix (Create a Smart Fix task)

Sử dụng endpoint này để khởi tạo tác vụ tự động phát hiện và khắc phục các lỗi kỹ thuật phổ biến trong video quảng cáo.

Các lỗi có thể được phát hiện và xử lý bao gồm:
- Độ phân giải quá thấp (`LOW_RESOLUTION` < 540x960 px).
- Tỷ lệ khung hình video không chuẩn (`ILLEGAL_VIDEO_SIZE`).
- Viền đen che khuất tầm nhìn người xem (`BLACK_EDGE`).
- Thời lượng video quá ngắn hoặc quá dài (`ILLEGAL_DURATION`).

### Thông tin Endpoint
- **URL:** `https://business-api.tiktok.com/open_api/v1.3/video/fix/task/create/`
- **Phương thức:** `POST`

### Tiêu đề HTTP (Header)
| Header | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Có | Access Token được cấp quyền xác thực. |
| Content-Type | string | Có | Kiểu nội dung yêu cầu: `application/json`. |

### Tham số Body (Request Body)
| Tham số | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | Có | ID của tài khoản quảng cáo. |
| `tasks` | object[] | Có | Mảng chứa danh sách các video cần kiểm tra và sửa lỗi (tối đa 10 tác vụ). |
| ↳ `video_id` | string | Có | ID của video cần kiểm tra và sửa lỗi. |
| ↳ `auto_bind_enabled` | boolean | Không | Có tự động tải video đã sửa lỗi lên Thư viện tài sản sáng tạo hay không (`true`/`false`). Mặc định: `false`. |

### Tham số Response
| Trường | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi từ API (`0` là thành công). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Log ID định danh duy nhất của yêu cầu hệ thống. |
| `data` | object | Dữ liệu trả về. |
| ↳ `tasks` | object[] | Danh sách kết quả khởi tạo tác vụ kiểm tra video. |
| ↳↳ `video_id` | string | ID của video (trả về khi video không có lỗi nào được phát hiện). |
| ↳↳ `fix_task_id` | string | Mã ID tác vụ sửa lỗi (chỉ trả về khi hệ thống phát hiện có lỗi cần xử lý). Mã này được dùng để tra cứu kết quả ở endpoint tiếp theo. |
| ↳↳ `flaw_types` | string[] | Danh sách các loại lỗi kỹ thuật phát hiện được: `LOW_RESOLUTION`, `ILLEGAL_VIDEO_SIZE`, `NO_BGM`, `BLACK_EDGE`, `ILLEGAL_DURATION`. |

### Ví dụ cURL
```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/video/fix/task/create/" \
  -H "Access-Token: YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "advertiser_id": "7112345678901234567",
    "tasks": [
      {
        "video_id": "v09033a60000bt1posj6hujpgbgomlo2",
        "auto_bind_enabled": true
      }
    ]
  }'
```

### Ví dụ Python
```python
import requests

url = "https://business-api.tiktok.com/open_api/v1.3/video/fix/task/create/"
headers = {
    "Access-Token": "YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}
payload = {
    "advertiser_id": "7112345678901234567",
    "tasks": [
        {
            "video_id": "v09033a60000bt1posj6hujpgbgomlo2",
            "auto_bind_enabled": True
        }
    ]
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())
```

### Phản hồi thành công mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202610231314000101",
  "data": {
    "tasks": [
      {
        "fix_task_id": "fix_tsk_9876543210abcdef",
        "flaw_types": [
          "LOW_RESOLUTION",
          "BLACK_EDGE"
        ]
      }
    ]
  }
}
```

---

<a id="doc-1741469487859714"></a>
<!-- doc_id: 1741469487859714 -->
## 13. Lấy kết quả tác vụ Smart Fix (Get the results of a Smart Fix task)

Sử dụng endpoint này để lấy kết quả hoàn tất của tác vụ sửa lỗi video thông minh (Smart Fix).

### Thông tin Endpoint
- **URL:** `https://business-api.tiktok.com/open_api/v1.3/video/fix/task/get/`
- **Phương thức:** `GET`

### Tiêu đề HTTP (Header)
| Header | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Có | Access Token được cấp quyền xác thực. |

### Tham số Query (Query Parameters)
| Tham số | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | Có | ID của tài khoản quảng cáo. |
| `task_id` | string | Có | ID của tác vụ sửa lỗi video (truyền mã `fix_task_id` nhận được từ endpoint tạo tác vụ sửa lỗi `/video/fix/task/create/`). |

### Tham số Response
| Trường | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi từ API (`0` là thành công). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Log ID định danh duy nhất của yêu cầu hệ thống. |
| `data` | object | Dữ liệu trả về. |
| ↳ `status` | string | Trạng thái của tác vụ sửa lỗi: `PROCESSING` (đang xử lý), `FAILED` (thất bại), `SUCCESS` (thành công). |
| ↳ `error_msg` | string | Thông điệp báo lỗi chi tiết nếu trạng thái là `FAILED`. |
| ↳ `videos` | object[] | Danh sách video đã được khắc phục lỗi thành công (tối đa 3 video). Chỉ xuất hiện khi `status` là `SUCCESS`. |
| ↳↳ `video_id` | string | ID của video sau khi sửa lỗi thành công. |
| ↳↳ `video_url` | string | Đường dẫn URL xem trước video đã sửa lỗi (có hiệu lực trong vòng 7 ngày). |

### Ví dụ cURL
```bash
curl -X GET "https://business-api.tiktok.com/open_api/v1.3/video/fix/task/get/?advertiser_id=7112345678901234567&task_id=fix_tsk_9876543210abcdef" \
  -H "Access-Token: YOUR_ACCESS_TOKEN"
```

### Ví dụ Python
```python
import requests

url = "https://business-api.tiktok.com/open_api/v1.3/video/fix/task/get/"
headers = {
    "Access-Token": "YOUR_ACCESS_TOKEN"
}
params = {
    "advertiser_id": "7112345678901234567",
    "task_id": "fix_tsk_9876543210abcdef"
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

### Phản hồi thành công mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202610231315000101",
  "data": {
    "status": "SUCCESS",
    "error_msg": null,
    "videos": [
      {
        "video_id": "v09033a60000bt1posj6hujpgbgomfixed",
        "video_url": "https://v16m-default.akamaized.net/fixed_video_preview.mp4"
      }
    ]
  }
}
```

---

<a id="doc-1767568466842626"></a>
<!-- doc_id: 1767568466842626 -->
## 14. Lấy kết quả phát hiện suy giảm hiệu quả sáng tạo

Sử dụng endpoint này để phát hiện hiện tượng **Suy giảm hiệu quả sáng tạo (Creative Fatigue)** đối với các mẫu quảng cáo trong một khoảng thời gian nhất định trong quá khứ.

Creative Fatigue xảy ra khi khán giả mục tiêu xem cùng một mẫu quảng cáo lặp lại quá nhiều lần dẫn đến hiệu quả chuyển đổi giảm dần và chi phí trên mỗi hành động (CPA) tăng cao. Việc phát hiện sớm hiện tượng này giúp nhà quảng cáo chủ động thay mới tài nguyên video hoặc điều chỉnh đối tượng mục tiêu.

### Thông tin Endpoint
- **URL:** `https://business-api.tiktok.com/open_api/v1.3/creative_fatigue/get/`
- **Phương thức:** `GET`

### Tiêu đề HTTP (Header)
| Header | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Có | Access Token được cấp quyền xác thực. |

### Tham số Query (Query Parameters)
| Tham số | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | Có | ID của tài khoản quảng cáo. |
| `adgroup_id` | string | Có | ID của nhóm quảng cáo cần kiểm tra. |
| `ad_id` | string | Không | ID của quảng cáo cụ thể (trường cũ, không bắt buộc). |
| `ad_material_ids` | string[] | Có | Danh sách mã định danh tài liệu sáng tạo cụ thể trong quảng cáo (`ad_material_id`, tối đa 100 ID). |
| `filtering` | object | Có | Điều kiện lọc thời gian kiểm tra. |
| ↳ `start_date` | string | Có | Ngày bắt đầu truy vấn theo định dạng `YYYY-MM-DD` (múi giờ của tài khoản quảng cáo, chỉ trong vòng 14 ngày gần nhất). |
| ↳ `end_date` | string | Có | Ngày kết thúc truy vấn theo định dạng `YYYY-MM-DD` (trong vòng 14 ngày gần nhất). |
| `page` | number | Không | Số trang hiện tại. Mặc định: `1`. Dải giá trị: ≥ 1. |
| `page_size` | number | Không | Số lượng kết quả trên một trang. Mặc định: `10`. Dải giá trị: [1, 500]. |

### Tham số Response
| Trường | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi từ API (`0` là thành công). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Log ID định danh duy nhất của yêu cầu hệ thống. |
| `data` | object | Dữ liệu trả về. |
| ↳ `list` | object[] | Danh sách kết quả đo lường suy giảm hiệu quả sáng tạo. |
| ↳↳ `adgroup_id` | string | ID nhóm quảng cáo. |
| ↳↳ `ad_id` | string | ID quảng cáo nếu có. |
| ↳↳ `date` | string | Ngày ghi nhận dữ liệu chỉ số. |
| ↳↳ `metrics` | object[] | Mảng thông tin chi tiết các chỉ số đo lường. |
| ↳↳↳ `ad_material_id` | string | Mã định danh tài liệu sáng tạo trong mẫu quảng cáo. |
| ↳↳↳ `has_fatigue` | boolean | Có phát hiện dấu hiệu suy giảm hiệu quả hay không: `true` (có hiện tượng bão hòa mỏi mẫu sáng tạo), `false` (hiệu quả vẫn ổn định). |
| ↳↳↳ `spend` | number | Tổng chi phí ước tính đã chi tiêu cho mẫu sáng tạo vào ngày này. |
| ↳↳↳ `cost_per_conversion` | number | Chi phí trung bình trên mỗi chuyển đổi (CPA) của mẫu sáng tạo này. |
| ↳ `page_info` | object | Thông tin phân trang (`page`, `page_size`, `total_number`, `total_page`). |

### Ví dụ cURL
```bash
curl -X GET "https://business-api.tiktok.com/open_api/v1.3/creative_fatigue/get/?advertiser_id=7112345678901234567&adgroup_id=7112345678909876543&ad_material_ids=%5B%22mat_123456789%22%5D&filtering=%7B%22start_date%22%3A%222026-10-10%22%2C%22end_date%22%3A%222026-10-23%22%7D&page=1&page_size=10" \
  -H "Access-Token: YOUR_ACCESS_TOKEN"
```

### Ví dụ Python
```python
import json
import requests

url = "https://business-api.tiktok.com/open_api/v1.3/creative_fatigue/get/"
headers = {
    "Access-Token": "YOUR_ACCESS_TOKEN"
}
params = {
    "advertiser_id": "7112345678901234567",
    "adgroup_id": "7112345678909876543",
    "ad_material_ids": json.dumps(["mat_123456789"]),
    "filtering": json.dumps({
        "start_date": "2026-10-10",
        "end_date": "2026-10-23"
    }),
    "page": 1,
    "page_size": 10
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

### Phản hồi thành công mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202610231316000101",
  "data": {
    "list": [
      {
        "adgroup_id": "7112345678909876543",
        "date": "2026-10-22",
        "metrics": [
          {
            "ad_material_id": "mat_123456789",
            "has_fatigue": true,
            "spend": 1250.50,
            "cost_per_conversion": 18.25
          }
        ]
      }
    ],
    "page_info": {
      "page": 1,
      "page_size": 10,
      "total_number": 1,
      "total_page": 1
    }
  }
}
```
