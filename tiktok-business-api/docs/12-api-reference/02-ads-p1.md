# Quảng cáo (Ads) — phần 1/2

Quảng cáo (Ad) là đơn vị quảng cáo nhỏ nhất và là nội dung trực tiếp hiển thị tới đối tượng mục tiêu trên nền tảng TikTok và mạng lưới hiển thị đối tác. Nhóm API Quảng cáo cho phép nhà quảng cáo truy xuất dữ liệu chi tiết của các quảng cáo thông thường và quảng cáo sáng tạo thông minh (Smart Creative), đồng thời khởi tạo các mẫu quảng cáo đa dạng như video đơn, hình ảnh đơn, quảng cáo quay vòng (Carousel), quảng cáo Spark Ads và quảng cáo mua sắm (Shopping Ads). Phần 1 này bao gồm tài liệu tổng quan, endpoint lấy dữ liệu quảng cáo (`/ad/get/`) và endpoint tạo quảng cáo (`/ad/create/`).

## Mục lục các endpoint

| Endpoint | Phương thức | Mục đích |
|---|---|---|
| [/ad/get/](02-ads-p1.md#doc-1735735588640770) | `GET` | Lấy dữ liệu chi tiết các quảng cáo thông thường và quảng cáo Smart Creative |
| [/ad/create/](02-ads-p1.md#doc-1739953377508354) | `POST` | Tải lên nội dung sáng tạo và tạo quảng cáo thông thường mới |

---

## Tổng quan Quảng cáo (`Ads`)
<a id="doc-1735735524758530"></a>
<!-- doc_id: 1735735524758530 -->

> Đường dẫn: API Reference > Ads

Quảng cáo (Ad) là đơn vị quảng cáo nhỏ nhất và đại diện cho nội dung được hiển thị tới tệp đối tượng mục tiêu của bạn:
- Tham khảo [Hướng dẫn - Quảng cáo (Guides-Ad)](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1745292235571201) để tìm hiểu quy trình tạo quảng cáo và nắm rõ khái niệm danh tính (identity).
- Xem [Cấu trúc phân cấp quảng cáo (Ad structure)](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1739381193120770) để tìm hiểu ba cấp độ quảng cáo (Chiến dịch > Nhóm quảng cáo > Quảng cáo).

Nhóm chức năng Quảng cáo bao gồm các endpoint sau:
* [Lấy dữ liệu quảng cáo (Get ads)](02-ads-p1.md#doc-1735735588640770)
* [Tạo quảng cáo (Create ads)](02-ads-p1.md#doc-1739953377508354)
* [Cập nhật thông tin quảng cáo (Update ads)](02-ads-p2.md#doc-1739953405142018)
* [Cập nhật trạng thái quảng cáo (Update the statuses of ads)](02-ads-p2.md#doc-1739953422970882)

---

## Lấy dữ liệu quảng cáo (`Get ads`)
<a id="doc-1735735588640770"></a>
<!-- doc_id: 1735735588640770 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/ad/get/`

**Mục đích**: Lấy dữ liệu chi tiết của các quảng cáo thông thường (regular ads) và quảng cáo sáng tạo thông minh (Smart Creative ads) thuộc tài khoản quảng cáo.

Để truy xuất các nội dung sáng tạo chi tiết cho quảng cáo Smart Creative, hãy sử dụng endpoint [/ad/aco/get/](60-smart-creative.md#doc-1739473020978177).

> [!NOTE]
> Để lấy danh sách các quảng cáo đã bị xóa, bạn cần chỉ định giá trị `STATUS_DELETE` trong trường `primary_status` hoặc một trong các giá trị `AD_STATUS_CAMPAIGN_DELETE` / `AD_STATUS_ADGROUP_DELETE` / `AD_STATUS_DELETE` trong trường `secondary_status`. Mặc định hệ thống không truy vấn dữ liệu đã bị xóa.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Bắt buộc | Access token đã được cấp quyền. Chi tiết xem tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (GET: query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | Bắt buộc | ID tài khoản quảng cáo. |
| `fields` | string[] | Không bắt buộc | Danh sách các trường thông tin bạn muốn lấy trong phản hồi (mảng chuỗi JSON URL-encode). Danh sách các trường khả dụng tương ứng với các trường bên dưới đối tượng `list` trong phần phản hồi. Nếu không chỉ định, hệ thống mặc định trả về tất cả các trường. |
| `exclude_field_types_in_response` | string[] | Không bắt buộc | Loại trường muốn loại bỏ khỏi kết quả phản hồi.<br>Giá trị enum cho phép:<br>• `NULL_FIELD`: Loại bỏ các trường có giá trị là null. |
| `filtering` | object | Không bắt buộc | Bộ lọc dữ liệu quảng cáo dưới dạng chuỗi JSON URL-encode. Ví dụ: `filtering={"campaign_automation_type":"UPGRADED_SMART_PLUS"}`. |
| ↳ `campaign_automation_type` | string | Không bắt buộc | Loại hình tự động hóa chiến dịch.<br>Giá trị enum:<br>• `MANUAL`: Chiến dịch thiết lập thủ công.<br>• `SMART_PLUS`: Chiến dịch Smart+ tự động.<br>• `UPGRADED_SMART_PLUS`: Chiến dịch Smart+ Nâng cấp (Upgraded Smart+ Campaign). Chi tiết xem tại [Upgraded Smart+ Campaign](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1853452461203458). |
| ↳ `ad_ids_v2` | string[] | Không bắt buộc | Danh sách ID quảng cáo phiên bản v2 (tối đa 100 ID). Hỗ trợ lọc theo:<br>• ID quảng cáo thủ công (Manual Ad).<br>• ID quảng cáo Smart+ Nâng cấp (Upgraded Smart+ Ad). Để tạo quảng cáo Smart+ Nâng cấp qua API, sử dụng [Upgraded Smart+ Ads API](62-upgraded-smartplus-p1.md#doc-1843301794874370).<br>**Lưu ý**: Khi lọc theo ID quảng cáo Upgraded Smart+, phản hồi sẽ chỉ bao gồm: `advertiser_id`, `campaign_id`, `campaign_name`, `adgroup_id`, `adgroup_name`, `ad_id_v2`, `ad_name`, `campaign_automation_type`. |
| ↳ `campaign_ids` | string[] | Không bắt buộc | Danh sách ID chiến dịch cần lọc. Tối đa 100 ID. |
| ↳ `campaign_system_origins` | string[] | Không bắt buộc | Nguồn gốc hệ thống tạo ra chiến dịch chứa quảng cáo.<br>Giá trị enum:<br>• `PROMOTE`: Chiến dịch Quảng bá (Promote) tạo qua ứng dụng di động TikTok.<br>• `TT_ADS_PLATFORM`: Chiến dịch thông thường tạo qua API hoặc TikTok Ads Manager.<br>Giá trị mặc định: `["TT_ADS_PLATFORM"]`.<br>Đối với quảng cáo Promote, chỉ có thể truy xuất các trường sau: `advertiser_id`, `campaign_id`, `campaign_name`, `adgroup_id`, `adgroup_name`, `ad_id`, `ad_name`, `create_time`, `operation_status`, `secondary_status`. Xem chi tiết tại [Promote campaigns](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1785880454546433). |
| ↳ `adgroup_ids` | string[] | Không bắt buộc | Danh sách ID nhóm quảng cáo cần lọc. Tối đa 100 ID. |
| ↳ `ad_ids` | string[] | Không bắt buộc | Danh sách ID quảng cáo cần lọc. Tối đa 100 ID. |
| ↳ `primary_status` | string | Không bắt buộc | Trạng thái chính của quảng cáo. Xem giá trị enum tại [Enumeration -Primary status](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ `secondary_status` | string | Không bắt buộc | Trạng thái phụ của quảng cáo. Xem giá trị enum tại [Enumeration - Ad Status - Secondary Status](../15-appendix/phu-luc-p1.md#doc-1737174886619138).<br>**Lưu ý**: Trường này không trả về trong môi trường sandbox vì quảng cáo không thực sự được phân phối. Tham khảo [Supported secondary statuses for a primary status](../09-marketing-api/quan-ly-chien-dich-tom-tat.md#doc-1757239620352002) để biết các trạng thái phụ hợp lệ ứng với từng trạng thái chính. |
| ↳ `objective_type` | string | Không bắt buộc | Mục tiêu quảng cáo. Xem giá trị enum tại [Enumeration - Advertising Objective](../15-appendix/phu-luc-p1.md#doc-1737174886619138). Lưu ý: Dù bạn chọn `WEB_CONVERSIONS` hay `CONVERSIONS`, hệ thống sẽ trả về dữ liệu của cả hai. |
| ↳ `buying_types` | string[] | Không bắt buộc | Lọc theo hình thức mua quảng cáo.<br>Giá trị enum:<br>• `AUCTION`: Quảng cáo đấu thầu.<br>• `RESERVATION_RF`: Quảng cáo đặt trước Tiếp cận & Tần suất (Reach & Frequency) và quảng cáo TikTok Pulse.<br>• `RESERVATION_TOP_VIEW`: Quảng cáo đặt trước TopView.<br>Giá trị mặc định: `["AUCTION", "RESERVATION_RF"]`.<br>Lưu ý: Giá trị `RESERVATION_TOP_VIEW` không thể kết hợp cùng các giá trị khác; để lọc quảng cáo TopView, hãy đặt chính xác trường này là `["RESERVATION_TOP_VIEW"]`. Chi tiết xem tại [TopView](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1804258360285186). |
| ↳ `optimization_goal` | string | Không bắt buộc | Mục tiêu tối ưu hóa. Xem giá trị enum tại [Enumeration - Optimization Goal](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ `creative_material_mode` | string | Không bắt buộc | Chiến lược phân phối nội dung sáng tạo.<br>Giá trị enum: `CUSTOM` (tùy chỉnh), `DYNAMIC` (tự động linh hoạt), `SMART_CREATIVE` (sáng tạo thông minh Smart Creative). |
| ↳ `destination` | string | Không bắt buộc | Loại trang đích cần lọc.<br>Giá trị enum:<br>• `APP`: Trang tải ứng dụng trên Google Play hoặc Apple App Store (khi `promotion_type` của nhóm quảng cáo là `APP_ANDROID` hoặc `APP_IOS`).<br>• `TIKTOK_INSTANT_PAGE`: Trang tức thì TikTok Instant Page (Trang tùy chỉnh, Biểu mẫu tức thì, Trang hồ sơ ứng dụng hoặc Trang sản phẩm tức thì).<br>• `WEBSITE`: Trang web đích thông thường (`landing_page_url`).<br>• `SOCIAL_MEDIA_APP`: URL ứng dụng mạng xã hội. Xem thêm [Create a Lead Generation ad with promotion type as instant messaging apps](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1774482999036930).<br>• `PHONE_CALL`: Cuộc gọi điện thoại. Xem thêm [Create a Lead Generation ad with promotion type as phone call](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1774482936048641).<br>Nếu đồng thời chỉ định `objective_type`, xem [Filterable destination page type for an advertising objective](../15-appendix/phu-luc-p1.md#doc-1764306884771842). |
| ↳ `creation_filter_start_time` | string | Không bắt buộc | Lọc quảng cáo tạo sau thời điểm này, định dạng `YYYY-MM-DD HH:MM:SS` (theo múi giờ UTC). Khuyến nghị giới hạn khoảng thời gian trong vòng 6 tháng để đảm bảo tốc độ phản hồi. |
| ↳ `creation_filter_end_time` | string | Không bắt buộc | Lọc quảng cáo tạo trước thời điểm này, định dạng `YYYY-MM-DD HH:MM:SS` (theo múi giờ UTC). |
| ↳ `modified_after` | string | Không bắt buộc | Lọc quảng cáo được chỉnh sửa sau thời điểm này, định dạng `YYYY-MM-DD HH:MM:SS` (múi giờ UTC). |
| `page` | number | Không bắt buộc | Số trang hiện tại. Giá trị mặc định: `1`. Khoảng giá trị: `>= 1`. |
| `page_size` | number | Không bắt buộc | Số lượng bản ghi trên một trang. Giá trị mặc định: `10`. Khoảng giá trị: `[1, 1000]`. |


### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Chi tiết xem tại [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi. Chi tiết xem tại [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `request_id` | string | ID nhật ký duy nhất của request. |
| `data` | object | Dữ liệu trả về. Danh sách quảng cáo mặc định được sắp xếp giảm dần theo ID quảng cáo (`ad_id`).<br>**Lưu ý**: Dữ liệu quảng cáo GMV Max cho sản phẩm và GMV Max cho LIVE tạo từ TikTok Shop sẽ không được trả về trong endpoint này. Quảng cáo Shopping Ads tạo qua API hoặc TikTok Ads Manager không bị ảnh hưởng. |
| ↳ `list` | object[] | Danh sách các quảng cáo. Các trường trả về phụ thuộc vào tham số `fields` trong request; nếu không chỉ định, trả về tất cả. |
| ↳↳ `advertiser_id` | string | ID tài khoản quảng cáo. |
| ↳↳ `campaign_id` | string | ID chiến dịch. |
| ↳↳ `campaign_name` | string | Tên chiến dịch. |
| ↳↳ `campaign_automation_type` | string | Loại hình tự động hóa chiến dịch.<br>Giá trị enum:<br>• `MANUAL`: Chiến dịch thủ công.<br>• `SMART_PLUS`: Chiến dịch Smart+.<br>• `UPGRADED_SMART_PLUS`: Chiến dịch Smart+ Nâng cấp (trường `ad_id_v2` trả về sẽ là ID quảng cáo Smart+ Nâng cấp).<br>• `UPGRADED_SMART_PLUS_CREATIVE`: Nhóm nội dung sáng tạo trong chiến dịch Smart+ Nâng cấp (trường `ad_id` trả về là ID của mẫu sáng tạo). Chi tiết xem tại [Upgraded Smart+ Campaign](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1853452461203458). |
| ↳↳ `campaign_system_origin` | string | Nguồn gốc hệ thống chiến dịch (chỉ trả về cho quảng cáo Promote tạo từ ứng dụng TikTok di động, giá trị: `PROMOTE`). |
| ↳↳ `adgroup_id` | string | ID nhóm quảng cáo. |
| ↳↳ `adgroup_name` | string | Tên nhóm quảng cáo. |
| ↳↳ `smart_plus_ad_id` | string | Chỉ trả về khi `campaign_automation_type` là `UPGRADED_SMART_PLUS_CREATIVE`. ID của quảng cáo Smart+ Nâng cấp chứa mẫu sáng tạo này. |
| ↳↳ `ad_id` | string | ID quảng cáo.<br>• Với chiến dịch `MANUAL`: ID quảng cáo thủ công.<br>• Với `SMART_PLUS`: ID quảng cáo trong chiến dịch Smart+.<br>• Với `UPGRADED_SMART_PLUS_CREATIVE`: ID của mẫu nội dung sáng tạo. |
| ↳↳ `ad_id_v2` | string | ID quảng cáo phiên bản v2.<br>• Với `MANUAL`: ID quảng cáo thủ công.<br>• Với `SMART_PLUS`: ID quảng cáo Smart+.<br>• Với `UPGRADED_SMART_PLUS`: ID quảng cáo Smart+ Nâng cấp (Asset Group). |
| ↳↳ `ad_name` | string | Tên quảng cáo. |
| ↳↳ `create_time` | string | Thời gian tạo quảng cáo, định dạng `YYYY-MM-DD HH:MM:SS` (múi giờ UTC). |
| ↳↳ `modify_time` | string | Thời gian chỉnh sửa quảng cáo lần cuối, định dạng `YYYY-MM-DD HH:MM:SS` (múi giờ UTC). |
| ↳↳ `identity_id` | string | ID danh tính (Identity ID) sử dụng cho quảng cáo. |
| ↳↳ `identity_type` | string | Loại danh tính.<br>Giá trị enum: `CUSTOMIZED_USER`, `AUTH_CODE`, `TT_USER`, `BC_AUTH_TT`. |
| ↳↳ `identity_authorized_bc_id` | string | ID của Business Center mà tài khoản TikTok liên kết tới. Trả về khi `identity_type` là `BC_AUTH_TT`. |
| ↳↳ `catalog_id` | string | ID danh mục sản phẩm (Catalog ID) chọn cho quảng cáo. |
| ↳↳ `product_specific_type` | string | Chiều không gian chọn sản phẩm trong danh mục. Giá trị enum: `ALL`, `PRODUCT_SET`, `CUSTOMIZED_PRODUCTS`. |
| ↳↳ `item_group_ids` | string[] | Danh sách ID SPU của sản phẩm. |
| ↳↳ `product_set_id` | string | ID của bộ sản phẩm (Product Set ID). |
| ↳↳ `sku_ids` | string[] | Danh sách ID mã sản phẩm chi tiết (SKU ID). |
| ↳↳ `vehicle_ids` | string[] | Danh sách ID xe (áp dụng cho quảng cáo ngành ô tô Automotive Ads). |
| ↳↳ `showcase_products` | object[] | Danh sách sản phẩm trưng bày (Showcase products) sử dụng trong quảng cáo. |
| ↳↳↳ `item_group_id` | string | SPU ID của sản phẩm trưng bày. |
| ↳↳↳ `store_id` | string | ID cửa hàng chứa sản phẩm. |
| ↳↳↳ `catalog_id` | string | ID danh mục chứa sản phẩm. |
| ↳↳ `ad_format` | string | Định dạng quảng cáo.<br>Giá trị enum:<br>• `SINGLE_IMAGE`: Hình ảnh đơn.<br>• `SINGLE_VIDEO`: Video đơn.<br>• `LIVE_CONTENT`: Nội dung phát trực tiếp.<br>• `CAROUSEL_ADS`: Quảng cáo quay vòng tiêu chuẩn TikTok Carousel Ads.<br>• `CATALOG_CAROUSEL`: Quảng cáo quay vòng sản phẩm danh mục (VSA Carousel Ads). |
| ↳↳ `vertical_video_strategy` | string | Chiến lược loại video sử dụng trong kịch bản Doanh số Sản phẩm (Product Sales). Enum: `UNSET`, `SINGLE_VIDEO`, `CATALOG_VIDEOS`, `CATALOG_UPLOADED_VIDEOS`, `LIVE_STREAM`. |
| ↳↳ `dynamic_format` | string | Định dạng động. Enum: `UNSET`, `DYNAMIC_CREATIVE`. |
| ↳↳ `video_id` | string | ID của video. Giá trị này bằng null nếu là quảng cáo Spark Ads lấy từ video tự nhiên có sẵn (xem qua `tiktok_item_id`). |
| ↳↳ `image_ids` | string[] | Danh sách ID hình ảnh sử dụng làm nội dung quảng cáo hoặc ảnh bìa video. |
| ↳↳ `carousel_image_index` | integer | Vị trí chỉ mục ảnh bổ sung dùng trong quảng cáo quay vòng ô tô. |
| ↳↳ `end_card_cta` | string | Lời kêu gọi hành động cho thẻ kết thúc (End Card) của quảng cáo quay vòng ô tô. |
| ↳↳ `auto_disclaimer_types` | string[] | Danh sách loại tuyên bố miễn trừ trách nhiệm hiển thị trong quảng cáo quay vòng ô tô. |
| ↳↳ `product_display_field_list` | string[] | Danh sách thông tin chi tiết sản phẩm hiển thị trong quảng cáo quay vòng ô tô. |
| ↳↳ `music_id` | string | ID bản nhạc sử dụng trong quảng cáo quay vòng TikTok Carousel Ad. |
| ↳↳ `tiktok_item_id` | string | ID bài đăng video TikTok sử dụng làm mẫu quảng cáo Spark Ads. Chi tiết xem tại [Create Spark Ads](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1739470744631298). |
| ↳↳ `promotional_music_disabled` | boolean | Có tắt việc sử dụng nhạc cho mục đích quảng bá trong bài đăng video Spark Ads hay không. |
| ↳↳ `item_duet_status` | string | Trạng thái cho phép Duet của bài đăng Spark Ads (`ENABLE`, `DISABLE`). |
| ↳↳ `item_stitch_status` | string | Trạng thái cho phép Stitch của bài đăng Spark Ads (`ENABLE`, `DISABLE`). |
| ↳↳ `dark_post_status` | string | Xác định xem quảng cáo có phải là Spark Ads Dark Post (bài đăng ẩn không hiển thị trên trang cá nhân) hay không. Enum: `ON`, `OFF`. |
| ↳↳ `branded_content_disabled` | boolean | Có tắt nhãn nội dung có thương hiệu hay không. Mặc định là `false`. |
| ↳↳ `shopping_ads_video_package_id` | string | ID gói mẫu video danh mục sản phẩm (Catalog video template ID). |
| ↳↳ `ad_text` | string | Văn bản nội dung quảng cáo hiển thị tới người xem. |
| ↳↳ `ad_texts` | string[] | Danh sách các văn bản quảng cáo (trong trường hợp thử nghiệm nhiều văn bản). |
| ↳↳ `call_to_action` | string | Lời kêu gọi hành động (CTA). Xem giá trị enum tại [Enumeration - Call-to-action](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳↳ `call_to_action_id` | string | ID của danh mục CTA tự động tối ưu hóa (CTA Portfolio ID). Xem [CTA Recommendations - Dynamic CTAs](../09-marketing-api/creatives.md#doc-1740307296329730). |
| ↳↳ `card_id` | string | ID danh mục sáng tạo tương tác (Creative portfolio ID). |
| ↳↳ `landing_page_url` | string | URL trang đích của quảng cáo. |
| ↳↳ `utm_params` | object[] | Danh sách các tham số UTM gắn trên URL trang đích. |
| ↳↳↳ `key` | string | Tên tham số URL. |
| ↳↳↳ `value` | string | Giá trị tham số URL. |
| ↳↳ `page_id` | number | ID của trang tức thì TikTok Instant Page. |
| ↳↳ `cpp_url` | string | URL trang sản phẩm tùy chỉnh trên App Store (Custom Product Page - CPP). |
| ↳↳ `tiktok_page_category` | string | Danh mục trang TikTok được quảng bá. Enum: `PROFILE`, `OTHER_TIKTOK_PAGE`. |
| ↳↳ `phone_region_code` | string | Mã quốc gia theo chuẩn ISO của số điện thoại (trả về khi `promotion_type` là `LEAD_GEN_CLICK_TO_CALL`). |
| ↳↳ `phone_region_calling_code` | string | Mã vùng gọi quốc tế của số điện thoại (ví dụ: `+84`). |
| ↳↳ `phone_number` | string | Số điện thoại để người dùng bấm gọi trực tiếp từ quảng cáo. |
| ↳↳ `creative_auto_enhancement_strategy_list` | string[] | Danh sách chiến lược tự động nâng cao chất lượng nội dung sáng tạo (`VIDEO_QUALITY`, `MUSIC_REFRESH`, `IMAGE_QUALITY`, `IMAGE_RESIZE`). |
| ↳↳ `deeplink` | string | Đường dẫn liên kết sâu (deeplink) điều hướng người dùng trực tiếp vào vị trí cụ thể trong ứng dụng đã cài đặt. |
| ↳↳ `deeplink_type` | string | Loại deeplink. Enum: `NORMAL` (deeplink thông thường), `DEFERRED_DEEPLINK` (deeplink trì hoãn cho người chưa cài app). |
| ↳↳ `deeplink_format_type` | string | Định dạng deeplink. Enum: `UNIVERSAL_OR_APP_LINK`, `SCHEME_LINK`, `NONE`. |
| ↳↳ `shopping_ads_deeplink_type` | string | Nguồn deeplink dùng trong Shopping Ads. Enum: `NONE`, `CUSTOM`, `SHOPPING_ADS`. |
| ↳↳ `deeplink_utm_params` | object[] | Danh sách tham số UTM gắn trên URL deeplink. |
| ↳↳↳ `key` | string | Tên tham số deeplink. |
| ↳↳↳ `value` | string | Giá trị tham số deeplink. |
| ↳↳ `shopping_ads_fallback_type` | string | Loại trang dự phòng khi deeplink không thể kích hoạt trong kịch bản Shopping Ads Retargeting (`DEFAULT`, `CUSTOM`, `SHOPPING_ADS`). |
| ↳↳ `fallback_type` | string | Loại đích dự phòng khi người dùng chưa cài đặt ứng dụng. Enum: `APP_INSTALL` (chuyển tới kho ứng dụng App Store/Google Play), `WEBSITE` (chuyển tới `landing_page_url`), `UNSET`. |
| ↳↳ `dynamic_destination` | string | Chiến lược trang đích động. Enum: `DLP` (Dynamic Landing Page - tự động điều hướng người dùng tới trang web tùy chỉnh hoặc Instant Product Page phù hợp nhất), `UNSET`. |
| ↳↳ `auto_message_id` | string | ID tin nhắn tự động mở đầu (Welcome Message) trong quảng cáo tin nhắn trực tiếp TikTok Direct Messaging Ad. |
| ↳↳ `aigc_disclosure_type` | string | Tự công bố nội dung do trí tuệ nhân tạo tạo ra (AIGC).<br>Giá trị enum:<br>• `SELF_DISCLOSURE`: Bật nhãn công bố quảng cáo có chứa nội dung do AI tạo ra.<br>• `NOT_DECLARED`: Không công bố nội dung AI. |
| ↳↳ `disclaimer_type` | string | Loại tuyên bố từ chối trách nhiệm trong quảng cáo. Enum: `TEXT_LINK` (có liên kết có thể nhấp), `TEXT_ONLY` (chỉ có văn bản thuần túy). |
| ↳↳ `disclaimer_text` | object | Thông tin tuyên bố từ chối trách nhiệm chỉ có văn bản. |
| ↳↳↳ `text` | string | Nội dung văn bản tuyên bố. |
| ↳↳ `disclaimer_clickable_texts` | object[] | Danh sách các tuyên bố từ chối trách nhiệm có liên kết có thể nhấp. |
| ↳↳↳ `text` | string | Đoạn văn bản hiển thị. |
| ↳↳↳ `url` | string | Đường dẫn URL chi tiết của tuyên bố từ chối trách nhiệm. |
| ↳↳ `tracking_pixel_id` | number | ID của TikTok Pixel dùng để theo dõi sự kiện chuyển đổi bên ngoài. |
| ↳↳ `tracking_app_id` | string | ID của ứng dụng được theo dõi sự kiện cài đặt/sử dụng. |
| ↳↳ `tracking_offline_event_set_ids` | string[] | Danh sách ID bộ sự kiện ngoại tuyến (Offline Event set) dùng để đo lường. Xem thêm [Quản lý Offline Event set](../09-marketing-api/do-luong-quang-cao-p1.md#doc-1758051319816193). |
| ↳↳ `tracking_message_event_set_id` | string | ID bộ sự kiện tin nhắn dùng để đo lường trong quảng cáo tin nhắn trực tiếp. |
| ↳↳ `vast_moat_enabled` | boolean | Có bật tích hợp đo lường hiển thị Moat Viewability Verification hay không (khuyến nghị thay thế bằng `viewability_postbid_partner: MOAT`). |
| ↳↳ `viewability_postbid_partner` | string | Đối tác đo lường khả năng hiển thị bên thứ ba sau đấu thầu (Post-bid). Enum: `UNSET`, `MOAT`, `DOUBLE_VERIFY`, `IAS`, `ZEFR`. |
| ↳↳ `viewability_vast_url` | string | URL VAST đóng gói của đối tác đo lường khả năng hiển thị (áp dụng khi đối tác là `IAS`). |
| ↳↳ `brand_safety_postbid_partner` | string | Đối tác đo lường an toàn thương hiệu bên thứ ba. Enum: `UNSET`, `DOUBLE_VERIFY`, `IAS`, `ZEFR`. |
| ↳↳ `brand_safety_vast_url` | string | URL VAST đóng gói của đối tác đo lường an toàn thương hiệu. |
| ↳↳ `impression_tracking_url` | string | URL theo dõi lượt hiển thị của bên thứ ba (Impression Tracking URL). |
| ↳↳ `click_tracking_url` | string | URL theo dõi lượt nhấp chuột của bên thứ ba (Click Tracking URL). |
| ↳↳ `playable_url` | string | URL tài nguyên quảng cáo có thể chơi được (Playable Ad URL). |
| ↳↳ `operation_status` | string | Trạng thái vận hành của quảng cáo.<br>Giá trị enum:<br>• `ENABLE`: Quảng cáo đang bật (ON).<br>• `DISABLE`: Quảng cáo đang tắt (OFF).<br>• `FROZEN`: Quảng cáo bị đóng băng và không thể bật lại. |
| ↳↳ `secondary_status` | string | Trạng thái chi tiết (Secondary status) phản ánh tình trạng duyệt và phân phối. Xem chi tiết tại [Enumeration-Ad Status - Secondary Status](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳↳ `creative_type` | string | Phân loại mẫu quảng cáo cho các kịch bản Live Shopping, Product Shopping, Đăng ký trước ứng dụng hoặc Ô tô. Enum: `SHOP_PDP`, `SHOP_PLP`, `SHORT_VIDEO_LIVE`, `DIRECT_LIVE`, `PSA`, `CUSTOM_INSTANT_PAGE`, `AUTO_INVENTORY_INSTANT_PAGE`. |
| ↳↳ `app_name` | string | Tên ứng dụng hiển thị trên quảng cáo cài đặt ứng dụng. |
| ↳↳ `display_name` | string | Tên hiển thị thương hiệu/nhà quảng cáo trên trang đích hoặc quảng cáo thuần hiển thị. |
| ↳↳ `avatar_icon_web_uri` | string | Mã URI định danh ảnh đại diện (avatar image). |
| ↳↳ `profile_image_url` | string | Đường dẫn URL xem ảnh đại diện. |
| ↳↳ `creative_authorized` | boolean | Cho phép hiển thị quảng cáo trên TikTok For Business Creative Center hay không (mặc định: `false`). Chỉ áp dụng cho quảng cáo video ngoài nước Mỹ. |
| ↳↳ `is_aco` | boolean | Quảng cáo có phải là quảng cáo tự động hóa hoặc sáng tạo thông minh Smart Creative hay không (`true`/`false`). |
| ↳↳ `is_new_structure` | boolean | Chiến dịch có tuân theo cấu trúc phân cấp mới hay không. |
| ↳↳ `optimization_event` | string | Sự kiện tối ưu hóa chuyển đổi của nhóm quảng cáo. Xem chi tiết tại [Conversion events](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1739361474981889). |
| ↳↳ `share_disabled` | boolean | Đã tắt tính năng chia sẻ quảng cáo sang nền tảng bên thứ ba hay chưa (chỉ áp dụng ở cấp quảng cáo cho [TopView ads](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1804258360285186)). |
| ↳↳ `comment_disabled` | boolean | Đã tắt tính năng bình luận trên quảng cáo hay chưa (chỉ dành cho [TopView ads](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1804258360285186)). |
| ↳↳ `video_download_disabled` | boolean | Đã tắt tính năng tải video quảng cáo về máy hay chưa (chỉ dành cho [TopView ads](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1804258360285186)). |
| ↳ `page_info` | object | Thông tin phân trang. |
| ↳↳ `page` | number | Số trang hiện tại. |
| ↳↳ `page_size` | number | Số bản ghi trên mỗi trang. |
| ↳↳ `total_number` | number | Tổng số lượng quảng cáo thỏa mãn bộ lọc. |
| ↳↳ `total_page` | number | Tổng số trang kết quả. |

### Ví dụ

#### cURL
```bash
curl -G --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/ad/get/' \
--header 'Access-Token: your_access_token_here' \
--data-urlencode 'advertiser_id=7000000000000000001' \
--data-urlencode 'filtering={"primary_status":"STATUS_ALL"}' \
--data-urlencode 'page=1' \
--data-urlencode 'page_size=10'
```

#### Python
```python
import json
import requests

ACCESS_TOKEN = "your_access_token_here"
ADVERTISER_ID = "7000000000000000001"

url = "https://business-api.tiktok.com/open_api/v1.3/ad/get/"
headers = {"Access-Token": ACCESS_TOKEN}
params = {
    "advertiser_id": ADVERTISER_ID,
    "filtering": json.dumps({
        "primary_status": "STATUS_ALL"
    }),
    "page": 1,
    "page_size": 10
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20231023120000010188059082070",
  "data": {
    "page_info": {
      "page": 1,
      "page_size": 10,
      "total_page": 1,
      "total_number": 1
    },
    "list": [
      {
        "advertiser_id": "7000000000000000001",
        "campaign_id": "1730000000000000001",
        "campaign_name": "Summer_Sale_Campaign",
        "campaign_automation_type": "MANUAL",
        "adgroup_id": "1740000000000000001",
        "adgroup_name": "Audience_Broad_Targeting",
        "ad_id": "1750000000000000001",
        "ad_id_v2": "1750000000000000001",
        "ad_name": "Ad_Video_Creative_V1",
        "create_time": "2023-10-23 10:00:00",
        "modify_time": "2023-10-23 10:30:00",
        "identity_id": "7100000000000000001",
        "identity_type": "CUSTOMIZED_USER",
        "ad_format": "SINGLE_VIDEO",
        "video_id": "v09044g40000cf1234567890abcdef",
        "image_ids": ["ad-site-i18n-sg/2023102312345678.jpg"],
        "ad_text": "Khám phá ngay ưu đãi mùa hè cùng TikTok!",
        "call_to_action": "SHOP_NOW",
        "landing_page_url": "https://example.com/summer-sale",
        "operation_status": "ENABLE",
        "secondary_status": "AD_STATUS_DELIVERY_OK",
        "display_name": "TikTok Brand Store",
        "is_aco": false,
        "is_new_structure": true
      }
    ]
  }
}
```


---

## Tạo quảng cáo (`Create ads`)
<a id="doc-1739953377508354"></a>
<!-- doc_id: 1739953377508354 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/ad/create/`

**Mục đích**: Tải lên các thành phần nội dung sáng tạo (video, hình ảnh, văn bản, lời kêu gọi hành động CTA) và tạo một hoặc nhiều quảng cáo thông thường mới trong một nhóm quảng cáo.

Đối với các vị trí hiển thị khác nhau, định dạng mẫu quảng cáo và quy định kỹ thuật sẽ có sự khác biệt. Vui lòng tải lên nội dung sáng tạo theo đúng yêu cầu của vị trí phân phối. Xem chi tiết hướng dẫn tại [Cách tạo quảng cáo thông thường](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1745292553358338).

> [!IMPORTANT]
> **Thay đổi quan trọng về Danh tính tùy chỉnh (Custom Identity):**
> Việc tạo quảng cáo non-Spark Ads sử dụng Custom Identity trong các nhóm quảng cáo phân phối tới Vị trí tự động hoặc Vị trí chọn có bao gồm TikTok hiện **không còn được hỗ trợ** cho các tài khoản quảng cáo hiện tại. Tất cả các tài khoản quảng cáo mới tạo từ ngày 15/01/2026 trở đi không thể tạo quảng cáo non-Spark Ads bằng Custom Identity cho các vị trí này. Các quảng cáo cũ đã tạo trước đó không bị ảnh hưởng và vẫn có thể chỉnh sửa. Các chiến dịch chỉ phân phối tới Pangle hoặc Global App Bundle không bị ảnh hưởng. Tìm hiểu thêm tại [Thay đổi về Custom Identity](https://ads.tiktok.com/help/article/about-changes-coming-to-custom-identity) và [Chuyển đổi sang Spark Ads](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1848048566169730).

### Chuẩn bị trước khi bắt đầu
- Tham khảo [Tạo chiến dịch (Campaign Creation)](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1758526151905281) để chọn đúng tình huống triển khai phù hợp.
- **Giới hạn số lượng quảng cáo trong một nhóm quảng cáo:**
  - Nếu mục tiêu quảng cáo là `RF_REACH` (Reach & Frequency): Nhóm quảng cáo chứa tối đa **20** quảng cáo.
  - Nếu mục tiêu quảng cáo là `PRODUCT_SALES` (Doanh số sản phẩm): Chứa tối đa **20** quảng cáo khi nguồn sản phẩm là `STORE` (TikTok Shop) hoặc tối đa **50** quảng cáo khi nguồn sản phẩm là `CATALOG`.
  - Đối với các mục tiêu quảng cáo khác: Chứa tối đa **50** quảng cáo trong một nhóm quảng cáo.
- **Giới hạn trong mỗi lượt gọi API:** Mỗi request gọi `/ad/create/` chỉ có thể tạo tối đa **20 quảng cáo** trong mảng `creatives`. Nếu muốn tạo thêm quảng cáo cho cùng một nhóm quảng cáo, bạn cần thực hiện nhiều lượt gọi API riêng biệt.
- Để tạo quảng cáo sáng tạo thông minh (Smart Creative), vui lòng sử dụng endpoint [/ad/aco/create/](60-smart-creative.md#doc-1739473063234626).
- Xem bảng đối chiếu tính năng giữa giao diện TikTok Ads Manager và cấu hình API tại [Mapping between campaign features on TikTok Ads Manager and API configurations](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1740673047618561).

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Bắt buộc | Access token đã được cấp quyền. Chi tiết xem tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| `Content-Type` | string | Bắt buộc | Định dạng dữ liệu gửi lên: `"application/json"`. |

### Tham số (POST: JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | Bắt buộc | ID tài khoản quảng cáo. |
| `adgroup_id` | string | Bắt buộc | ID nhóm quảng cáo mà bạn muốn thêm quảng cáo vào. |
| `creatives` | object[] | Bắt buộc | Danh sách các mẫu nội dung sáng tạo quảng cáo. Kích thước tối đa: **20**. Trong một nhóm quảng cáo, bạn có thể tạo tối đa 20 quảng cáo trong một request duy nhất. |
| ↳ `ad_name` | string | Bắt buộc | Tên quảng cáo. Để hệ thống tự động đặt tên quảng cáo, hãy truyền chuỗi rỗng `""` (định dạng tên tự tạo sẽ là `ad_id`). Độ dài tối đa 512 ký tự và không được chứa emoji. |
| ↳ `identity_type` | string | Bắt buộc | Loại danh tính sử dụng cho quảng cáo.<br>Giá trị enum: `CUSTOMIZED_USER`, `AUTH_CODE`, `TT_USER`, `BC_AUTH_TT`. Chi tiết xem tại [Identities](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1738958351620097). |
| ↳ `identity_id` | string | Bắt buộc | ID danh tính. |
| ↳ `identity_authorized_bc_id` | string | Điều kiện | Bắt buộc khi `identity_type` là `BC_AUTH_TT`. ID Business Center mà tài khoản người dùng TikTok được liên kết. |
| ↳ `catalog_id` | string | Điều kiện | ID danh mục sản phẩm. Bắt buộc đối với Shopping Ads có nguồn sản phẩm là danh mục (Catalog). |
| ↳ `product_specific_type` | string | Điều kiện | Chiều không gian chọn sản phẩm từ catalog. Bắt buộc đối với Shopping Ads nguồn Catalog. Enum: `ALL`, `PRODUCT_SET`, `CUSTOMIZED_PRODUCTS`. |
| ↳ `item_group_ids` | string[] | Điều kiện | Bắt buộc khi `product_specific_type` là `CUSTOMIZED_PRODUCTS`. Danh sách ID nhóm sản phẩm (SPU ID). Tối đa 50 ID. |
| ↳ `product_set_id` | string | Điều kiện | Bắt buộc khi `product_specific_type` là `PRODUCT_SET`. ID bộ sản phẩm. |
| ↳ `sku_ids` | string[] | Không bắt buộc | Danh sách ID mã sản phẩm chi tiết (SKU ID) thuộc SPU chỉ định. |
| ↳ `vehicle_ids` | string[] | Điều kiện | Danh sách ID xe (dành cho quảng cáo ngành ô tô Automotive Ads). |
| ↳ `showcase_products` | object[] | Không bắt buộc | Danh sách sản phẩm trưng bày dùng trong quảng cáo. |
| ↳↳ `item_group_id` | string | Bắt buộc | ID nhóm sản phẩm (SPU ID) của sản phẩm trưng bày. |
| ↳↳ `store_id` | string | Điều kiện | ID cửa hàng chứa sản phẩm. Bắt buộc khi nguồn sản phẩm là Store. |
| ↳↳ `catalog_id` | string | Điều kiện | ID danh mục chứa sản phẩm. Bắt buộc khi nguồn sản phẩm là Catalog. |
| ↳ `ad_format` | string | Điều kiện | Định dạng mẫu quảng cáo.<br>Giá trị enum:<br>• `SINGLE_VIDEO`: Video đơn (bắt buộc cho quảng cáo video đơn).<br>• `SINGLE_IMAGE`: Hình ảnh đơn (bắt buộc cho quảng cáo ảnh đơn).<br>• `CAROUSEL_ADS`: Quảng cáo quay vòng tiêu chuẩn TikTok Standard Carousel Ads.<br>• `CATALOG_CAROUSEL`: Quảng cáo quay vòng sản phẩm danh mục (VSA Carousel Ads) hoặc quảng cáo quay vòng ngành ô tô.<br>• `LIVE_CONTENT`: Quảng cáo Live Shopping.<br>**Lưu ý**: Một khi đã đặt là `CAROUSEL_ADS` hoặc `CATALOG_CAROUSEL`, trường này không thể chỉnh sửa cập nhật sau này. |
| ↳ `vertical_video_strategy` | string | Không bắt buộc | Chiến lược loại video sử dụng trong kịch bản Doanh số Sản phẩm (Product Sales). Enum: `UNSET`, `SINGLE_VIDEO`, `CATALOG_VIDEOS`, `CATALOG_UPLOADED_VIDEOS`, `LIVE_STREAM`. |
| ↳ `dynamic_format` | string | Không bắt buộc | Định dạng động. Enum: `UNSET`, `DYNAMIC_CREATIVE`. |
| ↳ `video_id` | string | Điều kiện | ID video.<br>• Bắt buộc khi `ad_format` là `SINGLE_VIDEO` và `identity_type` là `CUSTOMIZED_USER`.<br>• Khi `identity_type` là `TT_USER` hoặc `BC_AUTH_TT`, truyền `video_id` hoặc `tiktok_item_id`.<br>• Không hỗ trợ khi `ad_format` là `SINGLE_IMAGE` hoặc `CAROUSEL_ADS`. Lấy ID video qua [/file/video/ad/search/](71-video.md#doc-1740050472224769). |
| ↳ `image_ids` | string[] | Điều kiện | Danh sách ID hình ảnh sử dụng trong quảng cáo hoặc làm ảnh bìa thumbnail của video.<br>• Khi `ad_format` là `SINGLE_VIDEO`: Bắt buộc với Non-Spark Ads hoặc Spark Ads Push để làm ảnh bìa video (chỉ truyền 1 ảnh, tỷ lệ khớp với video).<br>• Khi `ad_format` là `CAROUSEL_ADS`: Bắt buộc với Standard Carousel Non-Spark hoặc Spark Ads Push. Kích thước mảng: `[1, 35]`. Thứ tự ID quyết định thứ tự xuất hiện ảnh trong carousel.<br>• Khi `ad_format` là `CATALOG_CAROUSEL`: Bắt buộc làm ảnh tổng quan (1 ảnh).<br>• Khi `ad_format` là `SINGLE_IMAGE`: Bắt buộc (chỉ truyền 1 ảnh).<br>Lấy ID hình ảnh qua [/file/image/ad/search/](47-images.md#doc-1740052016789506) hoặc upload qua [/file/image/ad/upload/](47-images.md#doc-1739067433456642). |
| ↳ `carousel_image_index` | integer | Không bắt buộc | Vị trí chỉ mục ảnh bổ sung dùng trong quảng cáo quay vòng ô tô. |
| ↳ `end_card_cta` | string | Không bắt buộc | Lời kêu gọi hành động cho thẻ kết thúc (End Card) của quảng cáo quay vòng ô tô. |
| ↳ `auto_disclaimer_types` | string[] | Không bắt buộc | Danh sách loại tuyên bố miễn trừ trách nhiệm hiển thị trong quảng cáo quay vòng ô tô. |
| ↳ `product_display_field_list` | string[] | Không bắt buộc | Danh sách thông tin chi tiết sản phẩm hiển thị trong quảng cáo quay vòng ô tô. |
| ↳ `music_id` | string | Không bắt buộc | ID bản nhạc sử dụng trong quảng cáo quay vòng TikTok Carousel Ad. |
| ↳ `tiktok_item_id` | string | Điều kiện | ID bài đăng video TikTok dùng làm mẫu quảng cáo Spark Ads. Chi tiết xem tại [Create Spark Ads](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1739470744631298). |
| ↳ `promotional_music_disabled` | boolean | Không bắt buộc | Có tắt việc sử dụng nhạc cho mục đích quảng bá trong bài đăng video Spark Ads hay không. |
| ↳ `item_duet_status` | string | Không bắt buộc | Trạng thái cho phép Duet của bài đăng Spark Ads (`ENABLE`, `DISABLE`). |
| ↳ `item_stitch_status` | string | Không bắt buộc | Trạng thái cho phép Stitch của bài đăng Spark Ads (`ENABLE`, `DISABLE`). |
| ↳ `dark_post_status` | string | Không bắt buộc | Xác định xem quảng cáo có phải là Spark Ads Dark Post (bài đăng ẩn không hiển thị trên trang cá nhân của tài khoản TikTok) hay không. Enum: `ON`, `OFF`. |
| ↳ `branded_content_disabled` | boolean | Không bắt buộc | Có tắt nhãn nội dung có thương hiệu hay không. Mặc định là `false`. |
| ↳ `shopping_ads_video_package_id` | string | Không bắt buộc | ID gói mẫu video danh mục sản phẩm (Catalog video template ID). |
| ↳ `ad_text` | string | Bắt buộc | Văn bản nội dung quảng cáo hiển thị tới người xem. Độ dài tối đa 100 ký tự. |
| ↳ `ad_texts` | string[] | Không bắt buộc | Danh sách các văn bản quảng cáo bổ sung (dành cho thử nghiệm nội dung). |
| ↳ `call_to_action` | string | Không bắt buộc | Lời kêu gọi hành động (CTA). Xem giá trị enum tại [Enumeration - Call-to-action](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ `call_to_action_id` | string | Không bắt buộc | ID của danh mục CTA tự động tối ưu hóa (CTA Portfolio ID). Nếu truyền cả trường này và `call_to_action`, giá trị `call_to_action` sẽ bị bỏ qua. Xem [CTA Recommendations - Dynamic CTAs](../09-marketing-api/creatives.md#doc-1740307296329730). |
| ↳ `card_id` | string | Không bắt buộc | ID danh mục sáng tạo tương tác (Interactive Card Portfolio ID). |
| ↳ `landing_page_url` | string | Điều kiện | URL trang đích của quảng cáo. Bắt buộc khi đích đến là Website. |
| ↳ `utm_params` | object[] | Không bắt buộc | Danh sách các tham số theo dõi URL (UTM parameters). |
| ↳↳ `key` | string | Bắt buộc | Tên tham số URL. |
| ↳↳ `value` | string | Bắt buộc | Giá trị tham số URL. |
| ↳ `page_id` | number | Điều kiện | ID của trang tức thì TikTok Instant Page. Bắt buộc khi đích đến là trang tức thì. |
| ↳ `instant_product_page_used` | boolean | Không bắt buộc | Có sử dụng trang sản phẩm tức thì tạo tự động (Instant Product Page) hay không. |
| ↳ `page_image_index` | integer | Không bắt buộc | Chỉ hợp lệ khi `instant_product_page_used` là `true`. Vị trí chỉ mục hình ảnh đại diện hiển thị trên trang sản phẩm tức thì. |
| ↳ `cpp_url` | string | Không bắt buộc | URL trang sản phẩm tùy chỉnh trên App Store (Custom Product Page - CPP). |
| ↳ `tiktok_page_category` | string | Không bắt buộc | Danh mục trang TikTok được quảng bá (`PROFILE`, `OTHER_TIKTOK_PAGE`). |
| ↳ `phone_region_code` | string | Điều kiện | Bắt buộc khi loại quảng cáo là gọi điện `LEAD_GEN_CLICK_TO_CALL`. Mã quốc gia của số điện thoại. |
| ↳ `phone_region_calling_code` | string | Điều kiện | Bắt buộc khi loại quảng cáo là gọi điện. Mã vùng quốc tế của số điện thoại (ví dụ: `+84`). |
| ↳ `phone_number` | string | Điều kiện | Bắt buộc khi loại quảng cáo là gọi điện. Số điện thoại nhận cuộc gọi. |
| ↳ `creative_auto_enhancement_strategy_list` | string[] | Không bắt buộc | Danh sách chiến lược tự động nâng cao chất lượng nội dung sáng tạo (`VIDEO_QUALITY`, `MUSIC_REFRESH`, `IMAGE_QUALITY`, `IMAGE_RESIZE`). |
| ↳ `deeplink` | string | Không bắt buộc | Đường dẫn liên kết sâu (deeplink) vào ứng dụng. |
| ↳ `deeplink_type` | string | Không bắt buộc | Loại deeplink (`NORMAL`, `DEFERRED_DEEPLINK`). |
| ↳ `deeplink_format_type` | string | Không bắt buộc | Định dạng deeplink (`UNIVERSAL_OR_APP_LINK`, `SCHEME_LINK`, `NONE`). |
| ↳ `shopping_ads_deeplink_type` | string | Không bắt buộc | Nguồn deeplink trong Shopping Ads (`NONE`, `CUSTOM`, `SHOPPING_ADS`). |
| ↳ `deeplink_utm_params` | object[] | Không bắt buộc | Danh sách tham số UTM cho deeplink. |
| ↳↳ `key` | string | Bắt buộc | Tên tham số deeplink. |
| ↳↳ `value` | string | Bắt buộc | Giá trị tham số deeplink. |
| ↳ `shopping_ads_fallback_type` | string | Không bắt buộc | Loại trang dự phòng cho Shopping Ads Retargeting (`DEFAULT`, `CUSTOM`, `SHOPPING_ADS`). |
| ↳ `fallback_type` | string | Không bắt buộc | Loại đích dự phòng khi chưa cài đặt ứng dụng (`APP_INSTALL`, `WEBSITE`, `UNSET`). |
| ↳ `dynamic_destination` | string | Không bắt buộc | Chiến lược trang đích động (`DLP`, `UNSET`). |
| ↳ `auto_message_id` | string | Không bắt buộc | ID tin nhắn tự động mở đầu (Welcome Message) cho quảng cáo Direct Messaging. |
| ↳ `aigc_disclosure_type` | string | Không bắt buộc | Tự công bố nội dung AI. Enum: `SELF_DISCLOSURE`, `NOT_DECLARED`. Mặc định: `NOT_DECLARED`. |
| ↳ `disclaimer_type` | string | Không bắt buộc | Loại tuyên bố từ chối trách nhiệm (`TEXT_LINK`, `TEXT_ONLY`). |
| ↳ `disclaimer_text` | object | Điều kiện | Bắt buộc khi `disclaimer_type` là `TEXT_ONLY`. |
| ↳↳ `text` | string | Bắt buộc | Nội dung văn bản tuyên bố. |
| ↳ `disclaimer_clickable_texts` | object[] | Điều kiện | Bắt buộc khi `disclaimer_type` là `TEXT_LINK`. |
| ↳↳ `text` | string | Bắt buộc | Văn bản hiển thị. |
| ↳↳ `url` | string | Bắt buộc | Đường dẫn URL chi tiết. |
| ↳ `tracking_pixel_id` | number | Không bắt buộc | ID Pixel TikTok dùng để theo dõi sự kiện chuyển đổi. |
| ↳ `tracking_app_id` | string | Không bắt buộc | ID ứng dụng được theo dõi sự kiện. |
| ↳ `tracking_offline_event_set_ids` | string[] | Không bắt buộc | Danh sách ID bộ sự kiện ngoại tuyến (Offline Event set). |
| ↳ `tracking_message_event_set_id` | string | Không bắt buộc | ID bộ sự kiện tin nhắn đo lường trong quảng cáo tin nhắn trực tiếp. |
| ↳ `vast_moat_enabled` | boolean | Không bắt buộc | Bật đo lường hiển thị Moat Viewability (khuyến nghị dùng `viewability_postbid_partner`). |
| ↳ `viewability_postbid_partner` | string | Không bắt buộc | Đối tác đo lường hiển thị bên thứ ba (`UNSET`, `MOAT`, `DOUBLE_VERIFY`, `IAS`, `ZEFR`). |
| ↳ `viewability_vast_url` | string | Không bắt buộc | URL VAST của đối tác đo lường hiển thị. |
| ↳ `brand_safety_postbid_partner` | string | Không bắt buộc | Đối tác đo lường an toàn thương hiệu (`UNSET`, `DOUBLE_VERIFY`, `IAS`, `ZEFR`). |
| ↳ `brand_safety_vast_url` | string | Không bắt buộc | URL VAST của đối tác đo lường an toàn thương hiệu. |
| ↳ `impression_tracking_url` | string | Không bắt buộc | URL theo dõi lượt hiển thị của bên thứ ba. |
| ↳ `click_tracking_url` | string | Không bắt buộc | URL theo dõi lượt nhấp chuột của bên thứ ba. |
| ↳ `video_view_tracking_url` | string | Không bắt buộc | URL theo dõi lượt xem video của bên thứ ba. |
| ↳ `playable_url` | string | Không bắt buộc | URL tài nguyên quảng cáo có thể chơi được (Playable material URL). |
| ↳ `operation_status` | string | Không bắt buộc | Trạng thái ban đầu của quảng cáo sau khi tạo (`ENABLE` hoặc `DISABLE`). Mặc định: `ENABLE`. |
| ↳ `schedule_id` | string | Điều kiện | Chỉ dành cho quảng cáo Reach & Frequency. ID lịch phát đã được đặt trước. |
| ↳ `creative_type` | string | Không bắt buộc | Loại mẫu quảng cáo (`SHOP_PDP`, `SHOP_PLP`, `SHORT_VIDEO_LIVE`, `DIRECT_LIVE`, `PSA`, `CUSTOM_INSTANT_PAGE`, `AUTO_INVENTORY_INSTANT_PAGE`). |
| ↳ `app_name` | string | Điều kiện | Tên ứng dụng hiển thị trên quảng cáo cài đặt ứng dụng. |
| ↳ `display_name` | string | Điều kiện | Tên hiển thị thương hiệu/nhà quảng cáo. Bắt buộc cho quảng cáo dẫn về Website hoặc quảng cáo thuần hiển thị. |
| ↳ `avatar_icon_web_uri` | string | Không bắt buộc | Mã định danh hình ảnh đại diện (avatar icon URI). |
| ↳ `profile_image_url` | string | Không bắt buộc | Đường dẫn URL ảnh đại diện. |
| ↳ `creative_authorized` | boolean | Không bắt buộc | Cho phép đưa quảng cáo vào TikTok Creative Center hay không (mặc định: `false`). |


### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Chi tiết xem tại [Appendix - Return Codes](../11-business-messaging-api/business-messaging-api.md#doc-1832184306529874). |
| `message` | string | Thông điệp phản hồi. |
| `request_id` | string | ID nhật ký duy nhất của request. |
| `data` | object | Dữ liệu trả về sau khi tạo quảng cáo thành công. |
| ↳ `ad_ids` | string[] | Danh sách các ID quảng cáo vừa được tạo thành công. |
| ↳ `creatives` | object[] | Danh sách các đối tượng quảng cáo chi tiết vừa được tạo. |
| ↳↳ `advertiser_id` | string | ID tài khoản quảng cáo. |
| ↳↳ `campaign_id` | string | ID chiến dịch. |
| ↳↳ `campaign_name` | string | Tên chiến dịch. |
| ↳↳ `adgroup_id` | string | ID nhóm quảng cáo. |
| ↳↳ `adgroup_name` | string | Tên nhóm quảng cáo. |
| ↳↳ `ad_id` | string | ID quảng cáo vừa tạo. |
| ↳↳ `ad_name` | string | Tên quảng cáo. |
| ↳↳ `create_time` | string | Thời gian tạo quảng cáo (`YYYY-MM-DD HH:MM:SS` UTC). |
| ↳↳ `modify_time` | string | Thời gian chỉnh sửa quảng cáo gần nhất. |
| ↳↳ `identity_id` | string | ID danh tính. |
| ↳↳ `identity_type` | string | Loại danh tính (`CUSTOMIZED_USER`, `AUTH_CODE`, `TT_USER`, `BC_AUTH_TT`). |
| ↳↳ `identity_authorized_bc_id` | string | ID Business Center liên kết với tài khoản TikTok. |
| ↳↳ `catalog_id` | string | ID danh mục sản phẩm. |
| ↳↳ `product_specific_type` | string | Chiều không gian chọn sản phẩm (`ALL`, `PRODUCT_SET`, `CUSTOMIZED_PRODUCTS`). |
| ↳↳ `item_group_ids` | string[] | Danh sách SPU ID sản phẩm. |
| ↳↳ `product_set_id` | string | ID bộ sản phẩm. |
| ↳↳ `sku_ids` | string[] | Danh sách SKU ID. |
| ↳↳ `vehicle_ids` | string[] | Danh sách ID xe. |
| ↳↳ `showcase_products` | object[] | Danh sách sản phẩm trưng bày trong quảng cáo. |
| ↳↳↳ `item_group_id` | string | SPU ID sản phẩm. |
| ↳↳↳ `store_id` | string | ID cửa hàng chứa sản phẩm. |
| ↳↳↳ `catalog_id` | string | ID danh mục chứa sản phẩm. |
| ↳↳ `ad_format` | string | Định dạng quảng cáo (`SINGLE_IMAGE`, `SINGLE_VIDEO`, `LIVE_CONTENT`, `CAROUSEL_ADS`, `CATALOG_CAROUSEL`). |
| ↳↳ `vertical_video_strategy` | string | Chiến lược loại video cho Product Sales (`UNSET`, `SINGLE_VIDEO`, `CATALOG_VIDEOS`, `CATALOG_UPLOADED_VIDEOS`, `LIVE_STREAM`). |
| ↳↳ `dynamic_format` | string | Định dạng động (`UNSET`, `DYNAMIC_CREATIVE`). |
| ↳↳ `video_id` | string | ID video quảng cáo. |
| ↳↳ `image_ids` | string[] | Danh sách ID hình ảnh sử dụng trong quảng cáo. |
| ↳↳ `carousel_image_index` | integer | Chỉ mục ảnh bổ sung cho quảng cáo quay vòng ô tô. |
| ↳↳ `end_card_cta` | string | Lời kêu gọi hành động của thẻ kết thúc quảng cáo ô tô. |
| ↳↳ `auto_disclaimer_types` | string[] | Danh sách loại tuyên bố từ chối trách nhiệm ô tô. |
| ↳↳ `product_display_field_list` | string[] | Danh sách trường thông tin sản phẩm hiển thị trên quảng cáo ô tô. |
| ↳↳ `music_id` | string | ID đoạn nhạc nền sử dụng trong carousel. |
| ↳↳ `tiktok_item_id` | string | ID bài đăng video TikTok dùng cho Spark Ads. |
| ↳↳ `promotional_music_disabled` | boolean | Tắt việc dùng nhạc cho mục đích quảng bá của bài đăng Spark Ads. |
| ↳↳ `item_duet_status` | string | Trạng thái cho phép Duet (`ENABLE`, `DISABLE`). |
| ↳↳ `item_stitch_status` | string | Trạng thái cho phép Stitch (`ENABLE`, `DISABLE`). |
| ↳↳ `dark_post_status` | string | Trạng thái Spark Ads Dark Post (`ON`, `OFF`). |
| ↳↳ `branded_content_disabled` | boolean | Trạng thái tắt nhãn nội dung có thương hiệu. |
| ↳↳ `shopping_ads_video_package_id` | string | ID gói mẫu video danh mục sản phẩm. |
| ↳↳ `ad_text` | string | Văn bản quảng cáo chính. |
| ↳↳ `ad_texts` | string | Danh sách văn bản quảng cáo bổ sung. |
| ↳↳ `call_to_action` | string | Lời kêu gọi hành động CTA. |
| ↳↳ `call_to_action_id` | string | ID danh mục CTA động. |
| ↳↳ `card_id` | string | ID danh mục thẻ tương tác (Interactive Card). |
| ↳↳ `landing_page_url` | string | URL trang đích. |
| ↳↳ `utm_params` | object[] | Danh sách tham số UTM theo dõi URL. |
| ↳↳↳ `key` | string | Tên tham số URL. |
| ↳↳↳ `value` | string | Giá trị tham số URL. |
| ↳↳ `page_id` | number | ID trang tức thì TikTok Instant Page. |
| ↳↳ `cpp_url` | string | URL Custom Product Page trên App Store. |
| ↳↳ `tiktok_page_category` | string | Danh mục trang TikTok (`PROFILE`, `OTHER_TIKTOK_PAGE`). |
| ↳↳ `phone_region_code` | string | Mã quốc gia số điện thoại (chỉ có trong Lead Gen cuộc gọi). |
| ↳↳ `phone_region_calling_code` | string | Mã vùng gọi quốc tế của số điện thoại. |
| ↳↳ `phone_number` | string | Số điện thoại nhận cuộc gọi. |
| ↳↳ `creative_auto_enhancement_strategy_list` | string[] | Danh sách chiến lược tự động nâng cao chất lượng nội dung. |
| ↳↳ `deeplink` | string | Đường dẫn liên kết sâu vào ứng dụng. |
| ↳↳ `deeplink_type` | string | Loại deeplink (`NORMAL`, `DEFERRED_DEEPLINK`). |
| ↳↳ `deeplink_format_type` | string | Định dạng deeplink (`UNIVERSAL_OR_APP_LINK`, `SCHEME_LINK`, `NONE`). |
| ↳↳ `shopping_ads_deeplink_type` | string | Nguồn deeplink trong Shopping Ads (`NONE`, `CUSTOM`, `SHOPPING_ADS`). |
| ↳↳ `shopping_ads_fallback_type` | string | Loại trang dự phòng cho Shopping Ads Retargeting (`DEFAULT`, `CUSTOM`, `SHOPPING_ADS`). |
| ↳↳ `deeplink_utm_params` | object[] | Danh sách tham số UTM gắn trên deeplink. |
| ↳↳↳ `key` | string | Tên tham số deeplink. |
| ↳↳↳ `value` | string | Giá trị tham số deeplink. |
| ↳↳ `fallback_type` | string | Loại đích dự phòng (`APP_INSTALL`, `WEBSITE`, `UNSET`). |
| ↳↳ `dynamic_destination` | string | Chiến lược đích động (`DLP`, `UNSET`). |
| ↳↳ `auto_message_id` | string | ID tin nhắn chào tự động trong quảng cáo Direct Messaging. |
| ↳↳ `aigc_disclosure_type` | string | Tự công bố nội dung AI (`SELF_DISCLOSURE`, `NOT_DECLARED`). |
| ↳↳ `disclaimer_type` | string | Loại tuyên bố từ chối trách nhiệm (`TEXT_LINK`, `TEXT_ONLY`). |
| ↳↳ `disclaimer_text` | object | Thông tin tuyên bố chỉ có văn bản. |
| ↳↳↳ `text` | string | Nội dung văn bản tuyên bố. |
| ↳↳ `disclaimer_clickable_texts` | object[] | Danh sách tuyên bố có liên kết nhấp được. |
| ↳↳↳ `text` | string | Văn bản hiển thị. |
| ↳↳↳ `url` | string | URL đích chi tiết. |
| ↳↳ `tracking_pixel_id` | number | ID TikTok Pixel đo lường sự kiện. |
| ↳↳ `tracking_app_id` | string | ID ứng dụng đo lường. |
| ↳↳ `tracking_offline_event_set_ids` | string[] | Danh sách ID bộ sự kiện ngoại tuyến. |
| ↳↳ `tracking_message_event_set_id` | string | ID bộ sự kiện tin nhắn. |
| ↳↳ `vast_moat_enabled` | boolean | Trạng thái bật Moat Viewability. |
| ↳↳ `viewability_postbid_partner` | string | Đối tác đo lường khả năng hiển thị (`UNSET`, `MOAT`, `DOUBLE_VERIFY`, `IAS`, `ZEFR`). |
| ↳↳ `viewability_vast_url` | string | URL VAST đo lường hiển thị. |
| ↳↳ `brand_safety_postbid_partner` | string | Đối tác đo lường an toàn thương hiệu (`UNSET`, `DOUBLE_VERIFY`, `IAS`, `ZEFR`). |
| ↳↳ `brand_safety_vast_url` | string | URL VAST đo lường an toàn thương hiệu. |
| ↳↳ `impression_tracking_url` | string | URL theo dõi lượt hiển thị của bên thứ ba. |
| ↳↳ `click_tracking_url` | string | URL theo dõi lượt nhấp chuột của bên thứ ba. |
| ↳↳ `playable_url` | string | URL tài nguyên Playable material. |
| ↳↳ `operation_status` | string | Trạng thái vận hành của quảng cáo (`ENABLE`, `DISABLE`, `FROZEN`). |
| ↳↳ `secondary_status` | string | Trạng thái chi tiết (Secondary status). Xem chi tiết tại [Enumeration - Secondary Status](../11-business-messaging-api/business-messaging-api.md#doc-1832184306529874). |
| ↳↳ `creative_type` | string | Loại mẫu quảng cáo (`SHOP_PDP`, `SHOP_PLP`, `SHORT_VIDEO_LIVE`, `DIRECT_LIVE`, `PSA`, `CUSTOM_INSTANT_PAGE`, `AUTO_INVENTORY_INSTANT_PAGE`). |
| ↳↳ `app_name` | string | Tên ứng dụng hiển thị trên quảng cáo tải app. |
| ↳↳ `display_name` | string | Tên hiển thị trang đích hoặc quảng cáo thuần hiển thị. |
| ↳↳ `profile_image_url` | string | Đường dẫn URL ảnh đại diện. |
| ↳↳ `creative_authorized` | boolean | Cho phép hiển thị trên Creative Center (`true`/`false`). |
| ↳↳ `is_aco` | boolean | Quảng cáo tự động hóa hoặc sáng tạo thông minh (`true`/`false`). |
| ↳↳ `is_new_structure` | boolean | Cấu trúc phân cấp mới (`true`/`false`). |
| ↳↳ `optimization_event` | string | Sự kiện tối ưu hóa chuyển đổi. Xem chi tiết tại [Conversion events](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1739361474981889). |
| ↳ `page_info` | object | Thông tin phân trang. |
| ↳↳ `page` | number | Số trang hiện tại. |
| ↳↳ `page_size` | number | Số bản ghi trên mỗi trang. |
| ↳↳ `total_number` | number | Tổng số lượng kết quả. |
| ↳↳ `total_page` | number | Tổng số trang. |

### Ví dụ gọi API

```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/ad/create/' \
--header 'Access-Token: your_access_token_here' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id": "7000000000000000001",
    "adgroup_id": "1740000000000000001",
    "creatives": [
        {
            "ad_name": "Summer_Promotion_Video_Ad_1",
            "identity_type": "CUSTOMIZED_USER",
            "identity_id": "7100000000000000001",
            "ad_format": "SINGLE_VIDEO",
            "video_id": "v09044g40000cf1234567890abcdef",
            "image_ids": ["ad-site-i18n-sg/2023102312345678.jpg"],
            "ad_text": "Ưu đãi lớn chào hè - Giảm ngay 30% cho đơn hàng đầu tiên!",
            "call_to_action": "SHOP_NOW",
            "landing_page_url": "https://example.com/summer-sale",
            "display_name": "TikTok Shop Vietnam",
            "operation_status": "ENABLE"
        }
    ]
}'
```

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20231023120000010188059082080",
  "data": {
    "ad_ids": [
      "1750000000000000002"
    ],
    "creatives": [
      {
        "advertiser_id": "7000000000000000001",
        "campaign_id": "1730000000000000001",
        "campaign_name": "Summer_Sale_Campaign",
        "adgroup_id": "1740000000000000001",
        "adgroup_name": "Audience_Broad_Targeting",
        "ad_id": "1750000000000000002",
        "ad_name": "Summer_Promotion_Video_Ad_1",
        "create_time": "2023-10-23 16:00:00",
        "modify_time": "2023-10-23 16:00:00",
        "identity_id": "7100000000000000001",
        "identity_type": "CUSTOMIZED_USER",
        "ad_format": "SINGLE_VIDEO",
        "video_id": "v09044g40000cf1234567890abcdef",
        "image_ids": [
          "ad-site-i18n-sg/2023102312345678.jpg"
        ],
        "ad_text": "Ưu đãi lớn chào hè - Giảm ngay 30% cho đơn hàng đầu tiên!",
        "call_to_action": "SHOP_NOW",
        "landing_page_url": "https://example.com/summer-sale",
        "display_name": "TikTok Shop Vietnam",
        "operation_status": "ENABLE",
        "secondary_status": "AD_STATUS_AUDIT",
        "is_aco": false,
        "is_new_structure": true
      }
    ]
  }
}
```
