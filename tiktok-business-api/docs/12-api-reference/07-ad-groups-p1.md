# Nhóm quảng cáo (Ad Groups) — phần 1/3

Tài liệu này cung cấp hướng dẫn chi tiết và đặc tả kỹ thuật cho các API quản lý Nhóm quảng cáo (Ad Groups) trong TikTok for Business API v1.3 — Phần 1.

Nhóm quảng cáo là cấp độ trung gian trong cấu trúc quảng cáo TikTok (Chiến dịch > Nhóm quảng cáo > Quảng cáo). Ở cấp độ nhóm quảng cáo, bạn có thể thiết lập vị trí phân phối (placements), tệp đối tượng mục tiêu (target audiences), ngân sách (budgets), lịch chạy (schedule), giá thầu (bids), và mục tiêu tối ưu hóa (optimization goals).

Phần 1/3 bao gồm các endpoint quan trọng để truy xuất thông tin nhóm quảng cáo, tra cứu hạn mức động và ước tính quy mô tệp đối tượng mục tiêu.

## Danh sách các endpoint (Phần 1)

| Phương thức | Endpoint | Mô tả |
|---|---|---|
| `GET` | `/open_api/v1.3/adgroup/get/` | Lấy danh sách nhóm quảng cáo chi tiết kèm bộ lọc |
| `GET` | `/open_api/v1.3/adgroup/quota/` | Lấy hạn mức động cho các nhóm quảng cáo đấu thầu đang hoạt động |
| `POST` | `/open_api/v1.3/ad/audience_size/estimate/` | Ước tính quy mô tệp đối tượng mục tiêu |

---

## Tổng quan về Nhóm quảng cáo (`Ad Groups`)
<a id="doc-1739314549888002"></a>
<!-- doc_id: 1739314549888002 -->

Nhóm quảng cáo (Ad groups) là cấp độ trung gian trong cấu trúc quảng cáo. Bạn có thể thiết lập các vị trí phân phối quảng cáo cụ thể, tệp đối tượng mục tiêu, ngân sách, lịch chạy, giá thầu và mục tiêu tối ưu hóa cho từng nhóm quảng cáo.

Xem [Hướng dẫn - Nhóm quảng cáo (Guides-Ad group)](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1745292233615362) để tìm hiểu quy trình tạo nhóm quảng cáo và nắm bắt các khái niệm về nhắm mục tiêu (targeting), vị trí phân phối (placements), đặt giá thầu (bidding), an toàn thương hiệu (brand safety), Tối ưu hóa nội dung sáng tạo tự động (Automatic Creative Optimization - ACO), và Thử nghiệm phân tách (Split testing). Xem [Cấu trúc quảng cáo (Ad structure)](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1739381193120770) để tìm hiểu ba cấp độ phân cấp quảng cáo của TikTok.

Nhóm chức năng này bao gồm các endpoint sau:

* [Lấy danh sách nhóm quảng cáo](07-ad-groups-p1.md#doc-1739314558673922)
* [Lấy hạn mức động cho các nhóm quảng cáo đang hoạt động](07-ad-groups-p1.md#doc-1768463039162369)
* [Ước tính quy mô tệp đối tượng](07-ad-groups-p1.md#doc-1740302379236353)
* [Tạo nhóm quảng cáo](07-ad-groups-p2.md#doc-1739499616346114)
* [Cập nhật nhóm quảng cáo](07-ad-groups-p3.md#doc-1739586761631745)
* [Cập nhật trạng thái của các nhóm quảng cáo](07-ad-groups-p3.md#doc-1739591716326402)
* [Cập nhật ngân sách của các nhóm quảng cáo](07-ad-groups-p3.md#doc-1739591133130817)

---

## Lấy danh sách nhóm quảng cáo (`Get ad groups`)
<a id="doc-1739314558673922"></a>
<!-- doc_id: 1739314558673922 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/adgroup/get/`

**Mục đích**: Sử dụng endpoint này để lấy thông tin chi tiết của một hoặc nhiều nhóm quảng cáo thuộc tài khoản quảng cáo.

Thông tin trả về có thể được tùy chỉnh thông qua tham số `fields` trong yêu cầu. Bạn có thể sử dụng tham số `filtering` để lọc danh sách nhóm quảng cáo theo: ID chiến dịch, mục tiêu quảng cáo, ID nhóm quảng cáo, tên nhóm quảng cáo, thời gian tạo, sự kiện tính phí (billing event), và trạng thái nhóm quảng cáo.

> [!NOTE]
> Nếu bạn muốn truy vấn cả dữ liệu đã bị xóa, hãy chỉ định giá trị `STATUS_DELETE` trong trường `primary_status` hoặc `ADGROUP_STATUS_DELETE` / `ADGROUP_STATUS_CAMPAIGN_DELETE` trong trường `secondary_status`. Theo mặc định, dữ liệu đã xóa sẽ không được truy vấn.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Access token (mã truy cập) đã được ủy quyền. Chi tiết xem [Xác thực (Authentication)](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (Query Parameters)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| advertiser_id | string | Bắt buộc | ID của nhà quảng cáo / tài khoản quảng cáo. |
| fields | string[] | Không bắt buộc | Danh sách các trường bạn muốn nhận về trong kết quả. Khi không chỉ định, tất cả các trường sẽ được trả về theo mặc định. Xem danh sách các trường được hỗ trợ dưới mục `list` trong phần Phản hồi. |
| exclude_field_types_in_response | string[] | Không bắt buộc | Loại trường muốn loại bỏ khỏi phản hồi.<br>Giá trị enum:<br>• `NULL_FIELD`: Các trường có giá trị null. |
| filtering | object | Không bắt buộc | Điều kiện lọc dữ liệu. Truyền dưới dạng chuỗi JSON trong query string.<br>Ví dụ: `filtering={"campaign_automation_type":"UPGRADED_SMART_PLUS"}` |
| ↳ campaign_automation_type | string | Không bắt buộc | Loại tự động hóa chiến dịch.<br>Giá trị enum:<br>• `MANUAL`: Chiến dịch thủ công.<br>• `SMART_PLUS`: Chiến dịch Smart+.<br>• `UPGRADED_SMART_PLUS`: Chiến dịch Smart+ nâng cấp. Xem thêm tại [Chiến dịch Smart+ nâng cấp](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1853452461203458). |
| ↳ campaign_ids | string[] | Không bắt buộc | Danh sách ID chiến dịch cần lọc.<br>Số lượng tối đa: 100. |
| ↳ campaign_system_origins | string[] | Không bắt buộc | Nguồn gốc hệ thống của các chiến dịch mà nhóm quảng cáo trực thuộc.<br>Giá trị enum:<br>• `PROMOTE`: Chiến dịch Promote tạo qua ứng dụng TikTok di động.<br>• `TT_ADS_PLATFORM`: Chiến dịch thông thường tạo qua API hoặc TikTok Ads Manager.<br>Giá trị mặc định: `["TT_ADS_PLATFORM"]`.<br>Đối với nhóm quảng cáo thuộc chiến dịch Promote, chỉ lấy được các trường: `advertiser_id`, `campaign_id`, `campaign_name`, `adgroup_id`, `adgroup_name`, `create_time`, `budget`, `schedule_type`, `schedule_start_time`, `schedule_end_time`, `operation_status`, `secondary_status`. Xem thêm tại [Chiến dịch Promote](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1785880454546433). |
| ↳ adgroup_ids | string[] | Không bắt buộc | Danh sách ID nhóm quảng cáo cần lọc.<br>Số lượng tối đa: 100. |
| ↳ adgroup_name | string | Không bắt buộc | Tên nhóm quảng cáo cần lọc. |
| ↳ primary_status | string | Không bắt buộc | Trạng thái chính của nhóm quảng cáo. Xem [Enum - Trạng thái chính](../15-appendix/phu-luc-p1.md#doc-1737174886619138).<br>Giá trị mặc định là `STATUS_NOT_DELETE` (trả về các nhóm quảng cáo ở mọi trạng thái ngoại trừ `STATUS_DELETE`). Nếu muốn lấy tất cả các nhóm quảng cáo bao gồm cả đã xóa, hãy truyền `STATUS_ALL`. |
| ↳ secondary_status | string | Không bắt buộc | Trạng thái phụ của nhóm quảng cáo. Xem [Enum - Trạng thái nhóm quảng cáo - Trạng thái phụ](../15-appendix/phu-luc-p1.md#doc-1737174886619138).<br>**Lưu ý**:<br>• Trường này không được trả về trong môi trường sandbox vì nhóm quảng cáo không thực sự phân phối.<br>• Xem [Trạng thái phụ được hỗ trợ theo trạng thái chính](../09-marketing-api/quan-ly-chien-dich-tom-tat.md#doc-1757239620352002) để biết các giá trị hợp lệ. |
| ↳ objective_type | string | Không bắt buộc | Mục tiêu quảng cáo. Xem chi tiết tại [Enum - Mục tiêu quảng cáo](../15-appendix/phu-luc-p1.md#doc-1737174886619138).<br>**Lưu ý**: Dù bạn chọn `WEB_CONVERSIONS` hay `CONVERSIONS`, hệ thống đều sẽ trả về dữ liệu của cả hai mục tiêu này. |
| ↳ buying_types | string[] | Không bắt buộc | Lọc theo hình thức mua.<br>Giá trị enum:<br>• `AUCTION`: Quảng cáo đấu thầu.<br>• `RESERVATION_RF`: Quảng cáo đặt trước Tiếp cận & Tần suất (Reach & Frequency) và TikTok Pulse.<br>• `RESERVATION_TOP_VIEW`: Quảng cáo đặt trước TopView.<br>Giá trị mặc định: `["AUCTION", "RESERVATION_RF"]`.<br>Xem thêm tại [TopView](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1804258360285186).<br>**Lưu ý**: `RESERVATION_TOP_VIEW` không thể kết hợp cùng lúc với các giá trị khác. Để lọc quảng cáo TopView, đặt thành `["RESERVATION_TOP_VIEW"]`. |
| ↳ optimization_goal | string | Không bắt buộc | Mục tiêu tối ưu hóa. Giá trị enum xem tại [Enum - Mục tiêu tối ưu hóa](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ promotion_type | string | Không bắt buộc | Loại hình quảng bá (vị trí tối ưu hóa) cần lọc.<br>Giá trị enum:<br>• `APP`: Ứng dụng.<br>• `WEBSITE`: Trang đích.<br>• `INSTANT_FORM`: Biểu mẫu tức thì (Instant Form).<br>• `LEAD_GEN_CLICK_TO_TT_DIRECT_MESSAGE`: Tin nhắn trực tiếp TikTok.<br>• `LEAD_GEN_CLICK_TO_SOCIAL_MEDIA_APP_MESSAGE`: Ứng dụng mạng xã hội.<br>• `LEAD_GEN_CLICK_TO_CALL`: Cuộc gọi điện thoại.<br>**Lưu ý**: Bộ lọc này khác với trường `promotion_type` dùng khi tạo nhóm quảng cáo. Xem [Phụ lục - Ánh xạ giữa các loại hình quảng bá](../15-appendix/phu-luc-p1.md#doc-1758485431181314). |
| ↳ bid_strategy | string | Không bắt buộc | Chiến lược giá thầu.<br>Giá trị enum: `BID_STRATEGY_COST_CAP`, `BID_STRATEGY_BID_CAP`, `BID_STRATEGY_MAX_CONVERSION`, `BID_STRATEGY_LOWEST_COST`. |
| ↳ creative_material_mode | string | Không bắt buộc | Chiến lược phân phối nội dung sáng tạo.<br>Giá trị enum:<br>• `CUSTOM`: Tùy chỉnh.<br>• `SMART_CREATIVE`: Nội dung sáng tạo thông minh (Smart Creative). |
| ↳ billing_events | string[] | Không bắt buộc | Sự kiện tính phí bạn muốn thanh toán. Giá trị enum xem tại [Enum - Sự kiện tính phí](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ creation_filter_start_time | string | Không bắt buộc | Lọc theo thời gian bắt đầu tạo nhóm quảng cáo (`YYYY-MM-DD HH:MM:SS`, múi giờ UTC). Các nhóm quảng cáo tạo sau thời điểm này sẽ được trả về. Khoảng thời gian khuyến nghị tối đa là 6 tháng. |
| ↳ creation_filter_end_time | string | Không bắt buộc | Lọc theo thời gian kết thúc tạo nhóm quảng cáo (`YYYY-MM-DD HH:MM:SS`, múi giờ UTC). Các nhóm quảng cáo tạo trước thời điểm này sẽ được trả về. Khoảng thời gian khuyến nghị tối đa là 6 tháng. |
| ↳ split_test_enabled | boolean | Không bắt buộc | Lọc theo việc nhóm quảng cáo có bật thử nghiệm phân tách (split test) hay không:<br>`true`: Chỉ lấy nhóm quảng cáo bật split test.<br>`false`: Chỉ lấy nhóm quảng cáo tắt split test.<br>Nếu không chỉ định, trả về tất cả. |
| page | number | Không bắt buộc | Số trang hiện tại. Mặc định: `1`. Khoảng giá trị: ≥ 1. |
| page_size | number | Không bắt buộc | Số bản ghi trên mỗi trang. Mặc định: `10`. Khoảng giá trị: 1–1.000.<br>**Lưu ý**: Nếu dùng `RESERVATION_TOP_VIEW` trong bộ lọc `buying_types`, giá trị tối đa cho `page_size` là 100. |


### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi. Xem chi tiết tại [Phụ lục - Mã trả về (Return Codes)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. |
| request_id | string | ID log của yêu cầu, định danh duy nhất cho một yêu cầu HTTP. |
| data | object | Dữ liệu trả về. Danh sách được sắp xếp giảm dần theo ID nhóm quảng cáo (`adgroup_id`).<br>**Lưu ý**: Dữ liệu quảng cáo GMV Max Sản phẩm và GMV Max Phát trực tiếp tạo từ TikTok Shop bị loại trừ khỏi phản hồi. Shopping Ads tạo qua API hoặc TikTok Ads Manager không bị ảnh hưởng. |
| ↳ list | object[] | Danh sách nhóm quảng cáo. Các trường trả về phụ thuộc vào tham số `fields` trong yêu cầu. Nếu không chỉ định, trả về tất cả các trường. |
| ↳↳ advertiser_id | string | ID của nhà quảng cáo. |
| ↳↳ campaign_id | string | ID của chiến dịch. |
| ↳↳ campaign_name | string | Tên chiến dịch mà nhóm quảng cáo trực thuộc. |
| ↳↳ campaign_system_origin | string | Chỉ trả về cho nhóm quảng cáo thuộc chiến dịch Promote.<br>Nguồn gốc hệ thống của chiến dịch: `PROMOTE`.<br>Chỉ truy xuất được: `advertiser_id`, `campaign_id`, `campaign_name`, `adgroup_id`, `adgroup_name`, `create_time`, `budget`, `schedule_type`, `schedule_start_time`, `schedule_end_time`, `operation_status`, `secondary_status`. |
| ↳↳ campaign_automation_type | string | Loại tự động hóa chiến dịch: `MANUAL`, `SMART_PLUS`, `UPGRADED_SMART_PLUS`. |
| ↳↳ is_smart_performance_campaign | boolean | Chiến dịch có thuộc loại tự động hay không.<br>• `true`: Chiến dịch là Smart+ Campaign kế thừa.<br>• `false`: Chiến dịch là Manual Campaign hoặc Upgraded Smart+ Campaign (xem `campaign_automation_type`). |
| ↳↳ adgroup_id | string | ID nhóm quảng cáo. |
| ↳↳ adgroup_name | string | Tên nhóm quảng cáo. |
| ↳↳ create_time | string | Thời gian tạo nhóm quảng cáo, định dạng `"YYYY-MM-DD HH:MM:SS"`. Ví dụ: `"2023-01-01 00:00:01"`. |
| ↳↳ modify_time | string | Thời gian sửa đổi nhóm quảng cáo gần nhất, định dạng `"YYYY-MM-DD HH:MM:SS"`. |
| ↳↳ shopping_ads_type | string | Trả về khi `objective_type` của chiến dịch là `PRODUCT_SALES`.<br>Loại quảng cáo mua sắm: `VIDEO` (Video Shopping Ads), `LIVE` (Live Shopping Ads), `PRODUCT_SHOPPING_ADS`, `CATALOG_LISTING_ADS`, `UNSET`. |
| ↳↳ identity_id | string | ID danh tính. Trả về khi `shopping_ads_type` là `VIDEO` và `product_source` là `SHOWCASE`, hoặc khi `shopping_ads_type` là `LIVE`. |
| ↳↳ identity_type | string | Loại danh tính: `AUTH_CODE`, `TT_USER`, `BC_AUTH_TT`. Xem chi tiết tại [Danh tính (Identities)](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1738958351620097). |
| ↳↳ identity_authorized_bc_id | string | Trả về khi `identity_type` là `BC_AUTH_TT`. ID Business Center liên kết với tài khoản TikTok. |
| ↳↳ product_source | string | Nguồn sản phẩm: `UNSET`, `CATALOG` (Danh mục), `STORE` (TikTok Shop), `SHOWCASE` (TikTok Showcase). |
| ↳↳ catalog_id | string | ID danh mục sản phẩm (Catalog ID). |
| ↳↳ catalog_authorized_bc_id | string | ID Business Center sở hữu danh mục sản phẩm. |
| ↳↳ store_id | string | ID của TikTok Shop. |
| ↳↳ store_authorized_bc_id | string | ID Business Center được ủy quyền truy cập TikTok Shop (`store_id`). |
| ↳↳ promotion_type | string | Loại hình quảng bá (vị trí tối ưu hóa). Xem [Enum - Loại hình quảng bá](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳↳ promotion_target_type | string | Loại đích quảng bá cho mục tiêu Tìm kiếm khách hàng tiềm năng (Lead Generation): `INSTANT_PAGE`, `EXTERNAL_WEBSITE`, `UNSET`. |
| ↳↳ messaging_app_type | string | Loại ứng dụng nhắn tin tức thì hoặc URL tùy chỉnh: `MESSENGER`, `WHATSAPP`, `ZALO`, `LINE`, `IM_URL`. |
| ↳↳ messaging_app_account_id | string | ID tài khoản ứng dụng nhắn tin (Facebook Page ID, LINE Business ID, hoặc số điện thoại WhatsApp). |
| ↳↳ phone_region_code | string | Mã vùng quốc gia cho số điện thoại WhatsApp hoặc Zalo (ví dụ: `US`). |
| ↳↳ phone_region_calling_code | string | Mã gọi quốc tế cho số điện thoại WhatsApp hoặc Zalo (ví dụ: `+1`). |
| ↳↳ phone_number | string | Số điện thoại WhatsApp hoặc Zalo. |
| ↳↳ promotion_website_type | string | Loại trang tức thì TikTok trong nhóm quảng cáo: `UNSET`, `TIKTOK_NATIVE_PAGE`. |
| ↳↳ app_id | string | ID ứng dụng của ứng dụng được quảng bá. Lấy qua endpoint [/app/list/](43-events-1-0-p1.md#doc-1740859313270786). |
| ↳↳ app_type | string | Hệ điều hành của ứng dụng được quảng bá: `APP_ANDROID` (Android), `APP_IOS` (iOS). |
| ↳↳ app_download_url | string | Liên kết tải xuống ứng dụng. |
| ↳↳ pixel_id | string | Pixel ID (chỉ áp dụng cho trang đích). |
| ↳↳ optimization_event | string | Sự kiện chuyển đổi của nhóm quảng cáo. Xem [Sự kiện chuyển đổi](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1739361474981889). |
| ↳↳ custom_conversion_id | string | ID chuyển đổi tùy chỉnh (Custom Conversion ID) sử dụng trong nhóm quảng cáo. |
| ↳↳ app_config | object[] | Trả về khi `sales_destination` là `WEB_AND_APP` ở cấp chiến dịch. Chi tiết các ứng dụng được quảng bá. |
| ↳↳↳ app_id | string | ID ứng dụng được quảng bá. |
| ↳↳ deep_funnel_optimization_status | string | Trạng thái tối ưu hóa phễu chuyên sâu (deep funnel optimization): `ON` (bật), `OFF` (tắt). Cho phép chọn sự kiện thứ cấp bên cạnh sự kiện tối ưu hóa chính. |
| ↳↳ deep_funnel_event_source | string | Trả về khi bật tối ưu hóa phễu chuyên sâu. Nguồn sự kiện: `PIXEL` (Pixel), `OFFLINE` (Bộ sự kiện ngoại tuyến), `CRM` (Bộ sự kiện CRM). |
| ↳↳ deep_funnel_event_source_id | string | Trả về khi bật tối ưu hóa phễu chuyên sâu. ID nguồn sự kiện (Pixel ID, Offline Event Set ID, hoặc CRM Event Set ID). |
| ↳↳ deep_funnel_optimization_event | string | Sự kiện tối ưu hóa phễu chuyên sâu (ví dụ: `SHOPPING`). |
| ↳↳ placement_type | string | Chiến lược vị trí phân phối: `PLACEMENT_TYPE_AUTOMATIC` (Vị trí tự động), `PLACEMENT_TYPE_NORMAL` (Chọn vị trí cụ thể). |
| ↳↳ placements | string[] | Danh sách ứng dụng phân phối quảng cáo: `PLACEMENT_TIKTOK`, `PLACEMENT_PANGLE`, `PLACEMENT_GLOBAL_APP_BUNDLE`. Xem [Enum - Vị trí phân phối](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳↳ tiktok_subplacements | string[] | Vị trí phân phối phụ trong TikTok:<br>• `IN_FEED`: Bảng tin For You, Trang hồ sơ, Bảng tin Following.<br>• `SEARCH_FEED`: Bảng tin tìm kiếm.<br>• `TIKTOK_LITE`: TikTok Lite (hiện hỗ trợ Nhật Bản và Hàn Quốc).<br>• `LEMON8`: Lemon8 (xuất hiện trên For You feed, Search feed và Immersive Video feed của Lemon8). Xem thêm [Về Lemon8 trong TikTok Ads Manager](https://ads.tiktok.com/help/article/about-lemon8-in-tiktok-ads-manager). |
| ↳↳ search_result_enabled | boolean | Có đưa quảng cáo vào Quảng cáo tìm kiếm (Search Ads) trên TikTok hay không. |
| ↳↳ automated_keywords_enabled | boolean | Có bật tự động tạo từ khóa tìm kiếm hay không: `true`, `false`. |
| ↳↳ search_keywords | object[] | Chỉ trả về cho Search Ads Campaigns. Danh sách từ khóa tìm kiếm khớp với truy vấn của người dùng. |
| ↳↳↳ keyword | string | Từ khóa tìm kiếm. |
| ↳↳↳ match_type | string | Loại khớp từ khóa: `PRECISE_WORD` (khớp chính xác), `PHRASE_WORD` (khớp cụm từ), `BROAD_WORD` (khớp mở rộng). |
| ↳↳↳ keyword_bid_type | string | Loại giá thầu cho từ khóa: `FOLLOW_ADGROUP` (dùng giá thầu nhóm quảng cáo), `CUSTOM` (giá thầu tùy chỉnh). |
| ↳↳↳ keyword_bid | float | Mức giá thầu cho từ khóa và kiểu khớp. |
| ↳↳↳ audit_status | string | Trạng thái xét duyệt từ khóa: `AUDITING` (đang duyệt), `PASS` (đã duyệt), `REJECTED` (bị từ chối). |
| ↳↳↳ reject_info | object[] | Chi tiết lý do từ chối (trả về khi `audit_status` là `REJECTED`). |
| ↳↳↳↳ forbidden_location | string | Khu vực nhắm mục tiêu bị từ chối xét duyệt. Xem [Phụ lục - Mã vị trí](../15-appendix/phu-luc-p1.md#doc-1737585867307010). |
| ↳↳↳↳ reject_reasons | object[] | Danh sách lý do từ chối. |
| ↳↳↳↳↳ reason | string | Lý do từ chối chi tiết. |
| ↳↳ comment_disabled | boolean | Có tắt tính năng bình luận trên quảng cáo hay không: `true`, `false`. |
| ↳↳ video_download_disabled | boolean | Có tắt tính năng tải video quảng cáo về máy hay không: `true`, `false`. |
| ↳↳ share_disabled | boolean | Có tắt tính năng chia sẻ quảng cáo sang nền tảng bên thứ ba hay không: `true`, `false`. |
| ↳↳ blocked_pangle_app_ids | string[] | Danh sách ID danh sách chặn ứng dụng Pangle. |
| ↳↳ audience_type | string | Loại tệp đối tượng nhắm mục tiêu lại ứng dụng. Xem [Enum - Loại đối tượng nhắm lại ứng dụng](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳↳ audience_rule | object | Quy tắc xác định tệp đối tượng. Xem chi tiết tại [Quy tắc đối tượng](../09-marketing-api/audience.md#doc-1739566532187138). |
| ↳↳ auto_targeting_enabled {-To be deprecated} | boolean | *(Sắp ngừng hỗ trợ)* Có bật nhắm mục tiêu tự động hay không. Khuyến nghị chuyển sang [Smart Targeting](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1783164662979586). |
| ↳↳ shopping_ads_retargeting_type | string | Trả về khi `shopping_ads_type` là `VIDEO` và `product_source` là `CATALOG`.<br>Loại nhắm mục tiêu lại của quảng cáo mua sắm:<br>• `LAB1`: Xem sản phẩm hoặc thêm vào giỏ nhưng chưa mua.<br>• `LAB2`: Thêm vào giỏ nhưng chưa mua.<br>• `LAB3`: Kết hợp tùy chỉnh.<br>• `OFF`: Không nhắm mục tiêu lại.<br>• `RTA_RETARGETING`: Nhắm mục tiêu lại cho Realtime API (RTA). |
| ↳↳ shopping_ads_retargeting_actions_days | number | Khoảng thời gian hợp lệ cho hành vi đối tượng (ngày): 1, 2, 3, 7, 14, 30, 60, 90, 180. |
| ↳↳ included_custom_actions | object[] | Hành vi tùy chỉnh dùng làm điều kiện "Bao gồm" để lọc đối tượng nhắm lại. |
| ↳↳↳ code | string | Mã hành vi: `VIEW_PRODUCT` (xem sản phẩm), `ADD_TO_CART` (thêm vào giỏ), `PURCHASE` (mua hàng). |
| ↳↳↳ days | integer | Khoảng thời gian đã hoàn thành hành vi (1–180 ngày). |
| ↳↳ excluded_custom_actions | object[] | Hành vi tùy chỉnh dùng làm điều kiện "Loại trừ" để lọc đối tượng nhắm lại. |
| ↳↳↳ code | string | Mã hành vi: `VIEW_PRODUCT`, `ADD_TO_CART`, `PURCHASE`. |
| ↳↳↳ days | integer | Khoảng thời gian không thực hiện hành vi (1–180 ngày). |
| ↳↳ shopping_ads_retargeting_custom_audience_relation | string | Mối quan hệ logic giữa đối tượng nhắm lại VSA và tệp đối tượng tùy chỉnh (`audience_ids`): `OR` (kết hợp hợp nhất), `AND` (giao nhau). |
| ↳↳ location_ids | string[] | Danh sách ID vị trí địa lý nhắm mục tiêu. |
| ↳↳ zipcode_ids | string[] | Danh sách mã bưu chính nhắm mục tiêu. |
| ↳↳ languages | string[] | Mã ngôn ngữ nhắm mục tiêu. Xem [Enum - Mã ngôn ngữ](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳↳ gender | string | Giới tính nhắm mục tiêu: `GENDER_FEMALE`, `GENDER_MALE`, `GENDER_UNLIMITED`. |
| ↳↳ age_groups | string[] | Nhóm tuổi nhắm mục tiêu. Xem [Enum - Nhóm tuổi](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳↳ spending_power | string | Sức chi tiêu của người dùng mục tiêu: `ALL` (tất cả), `HIGH` (chi tiêu cao). |
| ↳↳ household_income | string[] | Thu nhập hộ gia đình: `TOP5`, `TOP10`, `TOP10_25`, `TOP25_50` (chỉ áp dụng tại Mỹ cho vị trí TikTok). |
| ↳↳ audience_ids | string[] | Danh sách ID tệp đối tượng tùy chỉnh nhắm mục tiêu. |
| ↳↳ smart_audience_enabled | boolean | Có bật Đối tượng thông minh (Smart audience) hay không: `true`, `false`. Xem [Smart Targeting](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1783164662979586). |
| ↳↳ excluded_audience_ids | string[] | Danh sách ID tệp đối tượng loại trừ. |
| ↳↳ interest_category_ids | string[] | Danh sách ID danh mục sở thích chung để nhắm mục tiêu. |
| ↳↳ interest_keyword_ids | string[] | Danh sách ID từ khóa sở thích bổ sung để nhắm mục tiêu. |
| ↳↳ purchase_intention_keyword_ids | string[] | Danh sách ID danh mục ý định mua sắm để nhắm mục tiêu. |
| ↳↳ actions | object[] | Danh sách đối tượng danh mục hành vi nhắm mục tiêu. |
| ↳↳↳ action_scene | string | Loại hành vi người dùng: `VIDEO_RELATED` (tương tác video), `CREATOR_RELATED` (tương tác nhà sáng tạo), `HASHTAG_RELATED` (tương tác hashtag). |
| ↳↳↳ action_period | number | Khung thời gian ghi nhận hành vi (ngày): `0`, `7`, `15`. |
| ↳↳↳ video_user_actions | string[] | Hành vi tương tác cụ thể:<br>• `VIDEO_RELATED`: `WATCHED_TO_END`, `LIKED`, `COMMENTED`, `SHARED`.<br>• `CREATOR_RELATED`: `FOLLOWING`, `VIEW_HOMEPAGE`.<br>• `HASHTAG_RELATED`: `VIEW_HASHTAG`. |
| ↳↳↳ action_category_ids | string[] | Danh sách ID danh mục tương tác video, nhà sáng tạo hoặc hashtag. |
| ↳↳ smart_interest_behavior_enabled | boolean | Có bật Sở thích & Hành vi thông minh (Smart interests & behaviors) hay không: `true`, `false`. |
| ↳↳ included_pangle_audience_package_ids | string[] | Danh sách ID gói đối tượng Pangle bao gồm (chỉ áp dụng cho Pangle). |
| ↳↳ excluded_pangle_audience_package_ids | string[] | Danh sách ID gói đối tượng Pangle loại trừ (chỉ áp dụng cho Pangle). |
| ↳↳ operating_systems | string[] | Hệ điều hành thiết bị nhắm mục tiêu: `ANDROID`, `IOS`. |
| ↳↳ min_android_version | string | Phiên bản Android tối thiểu. Xem [Enum - Phiên bản Android](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳↳ ios14_targeting | string | Thiết bị iOS nhắm mục tiêu: `UNSET`, `IOS14_MINUS`, `IOS14_PLUS`, `ALL`. |
| ↳↳ min_ios_version | string | Phiên bản iOS tối thiểu. Xem [Enum - Phiên bản iOS](70-tools-p1.md#doc-1738308662898689). |
| ↳↳ ios14_quota_type | string | Nhóm quảng cáo có tính vào hạn mức chiến dịch iOS 14 hay không: `OCCUPIED`, `UNOCCUPIED`. |
| ↳↳ device_model_ids | string[] | Danh sách ID mẫu thiết bị nhắm mục tiêu. Xem [Mẫu thiết bị](70-tools-p1.md#doc-1737172880570369). |
| ↳↳ network_types | string[] | Loại kết nối mạng nhắm mục tiêu: `WIFI`, `2G`, `3G`, `4G`, `5G`. Xem [Enum - Loại kết nối](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳↳ carrier_ids | string[] | Danh sách nhà mạng viễn thông nhắm mục tiêu. Xem [Nhà mạng](70-tools-p1.md#doc-1737168013095938). |
| ↳↳ isp_ids | string[] | Danh sách ID nhà cung cấp dịch vụ Internet (ISP) nhắm mục tiêu. |
| ↳↳ device_price_ranges | number[] | Khoảng giá thiết bị nhắm mục tiêu (bội số của 50). Ví dụ: `[0, 250]` thực tế biểu thị khoảng [0, 300]. |
| ↳↳ targeting_expansion {-To be deprecated} | object | Cài đặt mở rộng nhắm mục tiêu (Targeting expansion). |
| ↳↳↳ expansion_enabled | boolean | Có bật mở rộng nhắm mục tiêu hay không. |
| ↳↳↳ expansion_types | string[] | Loại đối tượng mục tiêu muốn mở rộng: `AGE`, `GENDER`, `INTEREST_AND_BEHAVIOR`, `CUSTOM_AUDIENCE`. |
| ↳↳ saved_audience_id | string | ID tệp đối tượng đã lưu (Saved Audience ID). |
| ↳↳ contextual_tag_ids | string[] | Danh sách ID thẻ ngữ cảnh (Contextual tag IDs). Xem [Nhắm mục tiêu theo ngữ cảnh](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1745292519923713). |
| ↳↳ brand_safety_type | string | Loại an toàn thương hiệu: `NO_BRAND_SAFETY`, `EXPANDED_INVENTORY`, `STANDARD_INVENTORY`, `LIMITED_INVENTORY`, `THIRD_PARTY`. |
| ↳↳ brand_safety_partner | string | Đối tác an toàn thương hiệu bên thứ ba (khi chọn `THIRD_PARTY`): `IAS`, `OPEN_SLATE` (DoubleVerify). |
| ↳↳ inventory_filter_enabled | boolean | Bộ lọc khoảng không quảng cáo an toàn (chỉ áp dụng cho `PLACEMENT_TIKTOK`): `true`, `false`. |
| ↳↳ category_exclusion_ids | string[] | Danh sách ID danh mục loại trừ nội dung. |
| ↳↳ vertical_sensitivity_id | string | ID danh mục nhạy cảm theo ngành dọc. |
| ↳↳ budget_mode | string | Chế độ ngân sách của nhóm quảng cáo. Nếu bật CBO ở cấp chiến dịch, trường này trả về `BUDGET_MODE_INFINITE`. Xem [Ngân sách](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1739381246298114). |
| ↳↳ budget | float | Ngân sách nhóm quảng cáo (trả về 0.0 nếu bật CBO). Đối với TopView, đây là ngân sách ước tính sau chiết khấu. |
| ↳↳ scheduled_budget | float | Ngân sách lên lịch cho ngày tiếp theo. Giá trị khác 0 biểu thị ngân sách đã đặt lịch. |
| ↳↳ schedule_type | string | Loại lịch chạy: `SCHEDULE_START_END` (có thời gian bắt đầu và kết thúc), `SCHEDULE_FROM_NOW` (bắt đầu và chạy liên tục). |
| ↳↳ schedule_start_time | datetime | Thời gian bắt đầu phân phối quảng cáo (UTC+0), định dạng `YYYY-MM-DD HH:MM:SS`. |
| ↳↳ schedule_end_time | datetime | Thời gian kết thúc phân phối quảng cáo (UTC+0), định dạng `YYYY-MM-DD HH:MM:SS`. |
| ↳↳ predict_impression | number | Chỉ trả về cho quảng cáo TopView. Số lượt hiển thị ước tính (tính theo nghìn). Ví dụ: `1291` tương ứng 1.291.000 lượt hiển thị. |
| ↳↳ topview_reach_range | number[] | Chỉ trả về cho quảng cáo TopView. Khoảng tiếp cận ước tính (tính theo nghìn cá nhân). |
| ↳↳ pre_discount_cpm | number | Chỉ trả về cho TopView. CPM ước tính trước chiết khấu (ví dụ: `11.33`). |
| ↳↳ cpm | number | Chỉ trả về cho TopView. CPM ước tính sau chiết khấu. |
| ↳↳ discount_type | string | Loại chiết khấu áp dụng cho TopView: `NO_DISCOUNT`, `BY_PERCENTAGE`, `BY_AMOUNT`. |
| ↳↳ discount_amount | number | Số tiền chiết khấu cố định cho TopView khi `discount_type` là `BY_AMOUNT`. |
| ↳↳ discount_percentage | number | Tỷ lệ phần trăm chiết khấu cho TopView khi `discount_type` là `BY_PERCENTAGE`. |
| ↳↳ pre_discount_budget | number | Ngân sách TopView trước chiết khấu. |
| ↳↳ schedule_infos | object[] | Thông tin phân phối lịch chạy cho nhóm quảng cáo Tiếp cận & Tần suất (R&F). |
| ↳↳↳ schedules | object[] | Chi tiết lịch phân phối theo khung giờ cho quảng cáo. |
| ↳↳↳↳ start_time | string | Thời gian bắt đầu phân phối quảng cáo. |
| ↳↳↳↳ end_time | string | Thời gian kết thúc phân phối quảng cáo. |
| ↳↳↳ expected_orders | number[] | Thứ tự phân phối quảng cáo trong nhóm quảng cáo (ví dụ: `[1]` là phân phối đầu tiên). |
| ↳↳↳ is_draft | boolean | Thông tin phân phối có đang ở chế độ bản nháp (chưa gán với quảng cáo cụ thể nào) hay không. |
| ↳↳↳ schedule_id | string | ID lịch chạy (Schedule ID). Dùng để gán với quảng cáo qua tham số `schedule_id` trong [/ad/create/](02-ads-p1.md#doc-1739953377508354). |
| ↳↳ delivery_mode | string | Chiến lược sắp xếp thứ tự và lịch phân phối quảng cáo trong nhóm R&F:<br>• `STANDARD`: Phân phối đồng đều.<br>• `SCHEDULE`: Phân phối theo lịch thời gian cụ thể.<br>• `SEQUENCE`: Phân phối theo thứ tự tuần tự.<br>• `VIEW_OPTIMIZE`: Tối ưu hóa lượt xem (ưu tiên tỷ lệ xem hết VTR cao).<br>• `OPTIMIZE`: Tối ưu hóa hiệu suất tổng thể. |
| ↳↳ dayparting | string | Lịch phân phối theo khung giờ trong tuần, gồm chuỗi 48 x 7 = 336 ký tự (mỗi ký tự đại diện cho 30 phút từ Thứ Hai đến Chủ Nhật, giá trị `1` là chạy, `0` là không chạy). Không chỉ định hoặc toàn `0`/`1` nghĩa là phân phối cả ngày. |
| ↳↳ optimization_goal | string | Mục tiêu tối ưu hóa. Xem [Enum - Mục tiêu tối ưu hóa](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳↳ secondary_optimization_event | string | Mục tiêu thứ cấp khi `optimization_goal` là `INSTALL` hoặc `VALUE`. Xem [Sự kiện chuyển đổi - Sự kiện mục tiêu thứ cấp](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1739361474981889). |
| ↳↳ message_event_set_id | string | ID bộ sự kiện tin nhắn sử dụng trong nhóm quảng cáo Tin nhắn tức thì. |
| ↳↳ frequency | number | Tần suất hiển thị quảng cáo tối đa (kết hợp với `frequency_schedule`, chỉ áp dụng cho mục tiêu `REACH`). Điều kiện: 1 ≤ `frequency` ≤ 1.000. |
| ↳↳ frequency_schedule | number | Khoảng thời gian tính tần suất (ngày). Điều kiện: 1 ≤ `frequency_schedule` ≤ 30. Ví dụ: `frequency` = 2 & `frequency_schedule` = 3 nghĩa là không quá 2 lần trong mỗi 3 ngày. |
| ↳↳ bid_type | string | Chiến lược giá thầu. Xem [Enum - Chiến lược giá thầu](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳↳ bid_price | float | Giá thầu mục tiêu (áp dụng cho chiến lược Cost Cap). |
| ↳↳ conversion_bid_price | float | Chi phí mục tiêu cho mỗi lượt chuyển đổi (target CPA) trong phương thức oCPM. |
| ↳↳ deep_bid_type | string | Chiến lược giá thầu cho sự kiện chuyên sâu trong ứng dụng. Xem [Enum - Chiến lược giá thầu chuyên sâu](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳↳ roas_bid | float | Mục tiêu ROAS cho Tối ưu hóa giá trị (Value Optimization). |
| ↳↳ vbo_window | string | Khung thời gian cho chiến lược tối ưu hóa giá trị (VBO): `SEVEN_DAYS` (7 ngày đầu), `ZERO_DAY` (ngày 0). Xem [VBO IAA / VBO IAP](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1739381743067137). |
| ↳↳ bid_display_mode | string | Cách tính và đo lường chi phí mỗi lượt xem (Cost per View). |
| ↳↳ deep_cpa_bid | float | Mức giá thầu CPA chuyên sâu sau khi chọn chiến lược sự kiện trong ứng dụng (ví dụ: `VO_MIN`). |
| ↳↳ cpv_video_duration | string | Thời lượng phát video tối ưu hóa: `SIX_SECONDS` (6 giây), `TWO_SECONDS` (2 giây). |
| ↳↳ next_day_retention | float | Tỷ lệ giữ chân ngày thứ 2: `next_day_retention` = `conversion_bid_price` / `deep_cpa_bid`. Khoảng giá trị (0, 1]. |
| ↳↳ click_attribution_window | string | Khung thời gian phân bổ lượt nhấp (Click-through window): `OFF`, `ONE_DAY`, `SEVEN_DAYS`, `FOURTEEN_DAYS`, `TWENTY_EIGHT_DAYS`. |
| ↳↳ engaged_view_attribution_window | string | Khung thời gian phân bổ lượt xem tương tác (Engaged view-through window, xem ≥ 6 giây video): `ONE_DAY`, `SEVEN_DAYS`. |
| ↳↳ view_attribution_window | string | Khung thời gian phân bổ lượt xem (View-through window): `OFF`, `ONE_DAY`, `SEVEN_DAYS`. |
| ↳↳ attribution_event_count | string | Cách tính đếm sự kiện phân bổ (Statistic type): `UNSET`, `EVERY` (mỗi sự kiện tính là 1 chuyển đổi riêng), `ONCE` (nhiều sự kiện từ 1 người chỉ tính là 1 chuyển đổi). |
| ↳↳ billing_event | string | Sự kiện tính phí. Xem [Enum - Sự kiện tính phí](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳↳ pacing | string | Tốc độ phân phối ngân sách: `PACING_MODE_SMOOTH` (phân phối đều đặn), `PACING_MODE_FAST` (phân phối nhanh nhất có thể). Bị bỏ qua và tự động đặt là `PACING_MODE_SMOOTH` khi bật CBO. |
| ↳↳ operation_status | string | Trạng thái hoạt động: `ENABLE` (đang bật), `DISABLE` (đang tắt), `FROZEN` (bị đóng băng, không thể kích hoạt lại). |
| ↳↳ secondary_status | string | Trạng thái phụ của nhóm quảng cáo. Xem [Enum - Trạng thái nhóm quảng cáo - Trạng thái phụ](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳↳ statistic_type | string | Loại thống kê giá thầu chuyển đổi: `EVERYTIME` (Mỗi lượt mua), `NONE` (Lượt mua duy nhất). |
| ↳↳ is_hfss | boolean | Nội dung quảng bá có phải là sản phẩm/thương hiệu HFSS (Nhiều chất béo, muối, đường) hay không: `true`, `false`. |
| ↳↳ is_lhf_compliance | boolean | Nội dung quảng bá có tuân thủ quy định Thực phẩm kém lành mạnh (LHF) tại Vương quốc Anh hay không: `true`, `false`. Xem [Quy định LHF 2024](https://www.legislation.gov.uk/uksi/2024/1266/made). |
| ↳↳ creative_material_mode | string | Chiến lược phân phối nội dung sáng tạo: `CUSTOM` (tùy chỉnh), `DYNAMIC` (ACO), `SMART_CREATIVE` (Smart Creative). Đối với nhóm quảng cáo Upgraded Smart+, trường này sẽ là null. |
| ↳↳ adgroup_app_profile_page_state | string | Nhóm quảng cáo có sử dụng Trang hồ sơ ứng dụng hay không: `INVALID`, `UNSET`, `ON`, `OFF`. |
| ↳↳ feed_type | string | Tùy chọn loại bảng tin: `STANDARD_FEED`, `TOP_FEED`. |
| ↳↳ rf_purchased_type | string | Phương thức thanh toán của nhóm quảng cáo Tiếp cận & Tần suất. Xem [Enum - Hình thức mua R&F](../15-appendix/phu-luc-p1.md#doc-1737174886619138). Với quảng cáo không phải R&F, giá trị luôn là null. |
| ↳↳ purchased_impression | number | Số lượt hiển thị đã mua (R&F). |
| ↳↳ purchased_reach | number | Lượng người dùng tiếp cận đã mua (R&F). |
| ↳↳ rf_estimated_cpr | number | Chi phí ước tính cho mỗi nghìn người tiếp cận (Cost per mille reach - CPR) của nhóm R&F. |
| ↳↳ rf_estimated_frequency | number | Tần suất hiển thị ước tính của nhóm R&F. |
| ↳↳ split_test_group_id | string | ID nhóm thử nghiệm phân tách (nếu nhóm quảng cáo nằm trong split test). |
| ↳↳ split_test_status | string | Trạng thái thử nghiệm phân tách. |
| ↳↳ is_new_structure | boolean | Nhóm quảng cáo có sử dụng cấu trúc mới hay không. |
| ↳↳ skip_learning_phase | boolean | Có bỏ qua giai đoạn máy học (learning phase) hay không. |
| ↳↳ conversion_window {-Deprecated} | string | *(Đã ngừng hỗ trợ)* Cửa sổ chuyển đổi sau khi nhấp hoặc xem quảng cáo để tối ưu hóa phân phối. Xem [Enum - Cửa sổ chuyển đổi](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ page_info | object | Thông tin phân trang. |
| ↳↳ page | number | Số trang hiện tại. |
| ↳↳ page_size | number | Số bản ghi trên mỗi trang. |
| ↳↳ total_number | number | Tổng số nhóm quảng cáo thỏa mãn điều kiện. |
| ↳↳ total_page | number | Tổng số trang kết quả. |


### Ví dụ

#### 1. Lấy danh sách nhóm quảng cáo chưa bị xóa

```bash
curl -G --location "https://business-api.tiktok.com/open_api/v1.3/adgroup/get/" \
  --header "Access-Token: YOUR_ACCESS_TOKEN" \
  --data-urlencode "advertiser_id=7123456789012345678"
```

#### 2. Lấy tất cả nhóm quảng cáo (bao gồm cả đã xóa)

```bash
curl -G --location "https://business-api.tiktok.com/open_api/v1.3/adgroup/get/" \
  --header "Access-Token: YOUR_ACCESS_TOKEN" \
  --data-urlencode "advertiser_id=7123456789012345678" \
  --data-urlencode 'filtering={"primary_status":"STATUS_ALL"}'
```

#### 3. Lấy nhóm quảng cáo thuộc một chiến dịch cụ thể

```bash
curl -G --location "https://business-api.tiktok.com/open_api/v1.3/adgroup/get/" \
  --header "Access-Token: YOUR_ACCESS_TOKEN" \
  --data-urlencode "advertiser_id=7123456789012345678" \
  --data-urlencode 'filtering={"campaign_ids":["1765432109876545"]}'
```

#### 4. Lấy nhóm quảng cáo tạo trong khoảng thời gian cụ thể

```bash
curl -G --location "https://business-api.tiktok.com/open_api/v1.3/adgroup/get/" \
  --header "Access-Token: YOUR_ACCESS_TOKEN" \
  --data-urlencode "advertiser_id=7123456789012345678" \
  --data-urlencode 'filtering={"creation_filter_start_time":"2024-01-01 00:00:00","creation_filter_end_time":"2024-01-30 00:00:00"}'
```

#### Gọi API bằng Python

```python
import json
import requests

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ADVERTISER_ID = "7123456789012345678"

url = "https://business-api.tiktok.com/open_api/v1.3/adgroup/get/"
headers = {
    "Access-Token": ACCESS_TOKEN
}
params = {
    "advertiser_id": ADVERTISER_ID,
    "page": 1,
    "page_size": 10,
    "filtering": json.dumps({
        "primary_status": "STATUS_NOT_DELETE",
        "campaign_ids": ["1765432109876545"]
    })
}

response = requests.get(url, headers=headers, params=params)
print(response.status_code)
print(response.json())
```

#### Ví dụ phản hồi thành công

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "2023052210032301011023224213560",
  "data": {
    "list": [
      {
        "budget_mode": "BUDGET_MODE_TOTAL",
        "included_custom_actions": [],
        "delivery_mode": null,
        "auto_targeting_enabled": false,
        "app_download_url": null,
        "placements": [
          "PLACEMENT_TIKTOK"
        ],
        "pixel_id": null,
        "conversion_window": null,
        "schedule_type": "SCHEDULE_START_END",
        "brand_safety_partner": null,
        "interest_category_ids": [],
        "adgroup_id": "1765432109876599",
        "campaign_name": "Summer_Promotion_2023",
        "schedule_infos": null,
        "share_disabled": false,
        "brand_safety_type": "NO_BRAND_SAFETY",
        "campaign_id": "1765432109876545",
        "ios14_quota_type": "UNOCCUPIED",
        "network_types": [],
        "app_type": null,
        "bid_type": "BID_TYPE_NO_BID",
        "conversion_bid_price": 0,
        "optimization_goal": "CLICK",
        "deep_bid_type": null,
        "video_download_disabled": false,
        "schedule_end_time": "2023-06-30 23:59:59",
        "scheduled_budget": 0,
        "is_hfss": false,
        "frequency": null,
        "bid_price": 0,
        "actions": [],
        "deep_cpa_bid": 0,
        "adgroup_name": "Summer_Traffic_AdGroup_1",
        "purchased_impression": null,
        "budget": 500.0,
        "app_id": null,
        "promotion_type": "WEBSITE",
        "age_groups": null,
        "next_day_retention": null,
        "pacing": "PACING_MODE_SMOOTH",
        "device_price_ranges": null,
        "location_ids": [
          "6252001"
        ],
        "secondary_status": "ADGROUP_STATUS_ENABLE",
        "billing_event": "CPC",
        "advertiser_id": "7123456789012345678",
        "create_time": "2023-05-22 10:05:00",
        "operation_status": "ENABLE",
        "placement_type": "PLACEMENT_TYPE_NORMAL",
        "optimization_event": null,
        "audience_ids": [],
        "secondary_optimization_event": null,
        "excluded_custom_actions": [],
        "languages": [],
        "modify_time": "2023-05-22 11:20:00",
        "excluded_audience_ids": [],
        "rf_estimated_cpr": null,
        "skip_learning_phase": false,
        "operating_systems": [
          "ANDROID"
        ],
        "creative_material_mode": "CUSTOM",
        "search_result_enabled": false,
        "rf_purchased_type": null,
        "inventory_filter_enabled": false,
        "adgroup_app_profile_page_state": null,
        "rf_estimated_frequency": null,
        "gender": "GENDER_UNLIMITED",
        "statistic_type": null,
        "purchased_reach": null,
        "is_new_structure": true,
        "interest_keyword_ids": [],
        "bid_display_mode": "CPMV",
        "dayparting": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111",
        "schedule_start_time": "2023-06-01 00:00:00",
        "comment_disabled": false,
        "frequency_schedule": null,
        "feed_type": null
      }
    ],
    "page_info": {
      "page": 1,
      "page_size": 10,
      "total_page": 1,
      "total_number": 1
    }
  }
}
```

---

## Lấy hạn mức động cho các nhóm quảng cáo đang hoạt động (`Get the dynamic quota on active ad groups`)
<a id="doc-1768463039162369"></a>
<!-- doc_id: 1768463039162369 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/adgroup/quota/`

**Mục đích**: Sử dụng endpoint này để lấy thông tin hạn mức động về số lượng nhóm quảng cáo đấu thầu đang hoạt động mà một nhà quảng cáo có thể sở hữu.

> [!NOTE]
> • Nếu tài khoản nhà quảng cáo (`advertiser_id`) thuộc diện áp dụng hạn mức cố định, bạn sẽ nhận được `total_adgroup_quota` = 5000 và `used_adgroup_quota` = 0 trong phản hồi.<br>• Nếu tài khoản nhà quảng cáo đang bị xử phạt (punished), bạn sẽ không được phép tạo thêm nhóm quảng cáo hoạt động nào (`total_adgroup_quota` và `used_adgroup_quota` đều bằng 0). Bạn có thể kiểm tra xem tài khoản quảng cáo có đang bị phạt hay không thông qua trường `status` trả về từ endpoint [/advertiser/info/](03-ad-accounts.md#doc-1739593083610113).<br>• Khi đã sử dụng hết hạn mức nhóm quảng cáo hoạt động (`total_adgroup_quota` = `used_adgroup_quota`), bạn vẫn có thể tạo thêm nhóm quảng cáo mới, nhưng các nhóm quảng cáo mới sẽ tự động bị hủy kích hoạt (deactivated) sau vài giây. Đồng thời, bạn không thể sử dụng [/adgroup/status/update/](07-ad-groups-p3.md#doc-1739591716326402) để kích hoạt lại các nhóm quảng cáo này.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Access token (mã truy cập) đã được ủy quyền. Chi tiết xem [Xác thực](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (Query Parameters)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| advertiser_id | string | Bắt buộc | ID của nhà quảng cáo / tài khoản quảng cáo. |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi. Xem chi tiết tại [Phụ lục - Mã trả về](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. |
| request_id | string | ID log của yêu cầu, định danh duy nhất cho một yêu cầu HTTP. |
| data | object | Dữ liệu hạn mức trả về. |
| ↳ total_adgroup_quota | number | Số lượng nhóm quảng cáo đang hoạt động tối đa mà nhà quảng cáo (`advertiser_id`) có thể có. |
| ↳ used_adgroup_quota | number | Số lượng nhóm quảng cáo đang hoạt động hiện tại của nhà quảng cáo. |

### Ví dụ

#### Gọi API bằng curl

```bash
curl -G --location "https://business-api.tiktok.com/open_api/v1.3/adgroup/quota/" \
  --header "Access-Token: YOUR_ACCESS_TOKEN" \
  --data-urlencode "advertiser_id=7123456789012345678"
```

#### Gọi API bằng Python

```python
import requests

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ADVERTISER_ID = "7123456789012345678"

url = "https://business-api.tiktok.com/open_api/v1.3/adgroup/quota/"
headers = {
    "Access-Token": ACCESS_TOKEN
}
params = {
    "advertiser_id": ADVERTISER_ID
}

response = requests.get(url, headers=headers, params=params)
print(response.status_code)
print(response.json())
```

#### Ví dụ phản hồi thành công

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "2023052210032301011023224213561",
  "data": {
    "total_adgroup_quota": 4980,
    "used_adgroup_quota": 20
  }
}
```


---

## Ước tính quy mô tệp đối tượng (`Estimate audience size`)
<a id="doc-1740302379236353"></a>
<!-- doc_id: 1740302379236353 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/ad/audience_size/estimate/`

**Mục đích**: Sử dụng endpoint này để ước tính quy mô tệp đối tượng mục tiêu có thể tiếp cận dựa trên các tiêu chí nhắm mục tiêu. Các tham số của endpoint này tương tự như các tham số được dùng khi tạo nhóm quảng cáo.

> [!NOTE]
> Do yêu cầu bảo mật và an toàn dữ liệu, quy mô đối tượng ước tính không bao gồm đối tượng người dùng dưới 18 tuổi. Việc phân phối quảng cáo thực tế tuân theo các luật hiện hành sẽ không bị ảnh hưởng.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Access token (mã truy cập) đã được ủy quyền. Chi tiết xem [Xác thực](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type | string | Bắt buộc | Định dạng nội dung yêu cầu. Giá trị hợp lệ: `application/json`. |

### Tham số (JSON Body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| advertiser_id | string | Bắt buộc | ID của nhà quảng cáo / tài khoản quảng cáo. |
| placement_type | string | Không bắt buộc | Loại vị trí phân phối.<br>Giá trị enum:<br>• `PLACEMENT_TYPE_AUTOMATIC`: Vị trí tự động.<br>• `PLACEMENT_TYPE_NORMAL`: Chọn vị trí cụ thể.<br>Giá trị mặc định: `PLACEMENT_TYPE_NORMAL`. |
| placements | string[] | Có điều kiện | Các ứng dụng bạn muốn phân phối quảng cáo. Bắt buộc khi `placement_type` là `PLACEMENT_TYPE_NORMAL`, và bị bỏ qua khi `placement_type` là `PLACEMENT_TYPE_AUTOMATIC`.<br>Hỗ trợ: `PLACEMENT_TIKTOK`, `PLACEMENT_PANGLE`, `PLACEMENT_GLOBAL_APP_BUNDLE`. Xem [Enum - Vị trí phân phối](../15-appendix/phu-luc-p1.md#doc-1737174886619138).<br>**Lưu ý**:<br>• Vị trí Global App Bundle chỉ áp dụng cho một số quốc gia (Brazil, Indonesia, Việt Nam, Philippines, Thái Lan, Malaysia, Mexico, Ả Rập Xê Út, Nhật Bản) và không hỗ trợ mục tiêu tối ưu hóa `TRAFFIC_LANDING_PAGE_VIEW`.<br>• Với chiến dịch Doanh số sản phẩm (`objective_type` = `PRODUCT_SALES`), chỉ hỗ trợ vị trí TikTok (`PLACEMENT_TIKTOK`). |
| app_id | string | Có điều kiện | ID của ứng dụng được quảng bá. Bắt buộc khi mục tiêu chiến dịch là `APP_PROMOTION`. |
| pixel_id | string | Có điều kiện | ID TikTok Pixel (chỉ áp dụng cho trang đích). Cần truyền cùng trường `external_action`. Sử dụng endpoint [/pixel/list/](43-events-1-0-p1.md#doc-1740858697598978) để lấy danh sách Pixel ID. |
| ios14_targeting | string | Có điều kiện | Thiết bị iOS bạn muốn nhắm mục tiêu.<br>**Lưu ý**: Khi `campaign_type` là `IOS14_CAMPAIGN`, trường này là bắt buộc và phải đặt là `IOS14_PLUS`.<br>Giá trị enum:<br>• `UNSET`: Thiết bị iOS 14.4 trở xuống.<br>• `IOS14_MINUS`: Thiết bị iOS 14.4 trở xuống không bị ảnh hưởng bởi bản cập nhật quyền riêng tư.<br>• `IOS14_PLUS`: Thiết bị iOS 14.5 trở lên áp dụng chính sách quyền riêng tư ATT của Apple. (Hệ thống sẽ kiểm tra tính hợp lệ của `app_id`, `operating_systems`, `min_ios_version`, `optimization_goal`). |
| objective_type | string | Bắt buộc | Mục tiêu quảng cáo. Xem [Enum - Mục tiêu quảng cáo](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| optimization_goal | string | Bắt buộc | Mục tiêu tối ưu hóa. Xem [Enum - Mục tiêu tối ưu hóa](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| promotion_type | string | Có điều kiện | Bắt buộc khi `objective_type` = `PRODUCT_SALES`. Loại hình quảng bá sản phẩm. Xem [Enum - Loại hình quảng bá](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| product_source | string | Có điều kiện | Bắt buộc khi `objective_type` = `PRODUCT_SALES`. Nguồn sản phẩm: `UNSET`, `CATALOG` (Danh mục), `STORE` (TikTok Shop). |
| catalog_id | string | Có điều kiện | Bắt buộc khi `objective_type` = `PRODUCT_SALES` và `product_source` là `CATALOG`. ID danh mục sản phẩm. |
| product_set_id | string | Không bắt buộc | ID bộ sản phẩm (ProductSet ID) trong danh mục. Giá trị `0` biểu thị chọn tất cả các bộ sản phẩm. Giá trị mặc định: `0`. |
| catalog_authorized_bc_id | string | Có điều kiện | Đối với danh mục trong Business Center, bạn phải chỉ định ID của Business Center sở hữu danh mục đó. |
| shopping_ads_retargeting_type | string | Không bắt buộc | Hợp lệ khi `objective_type` là `PRODUCT_SALES`. Loại nhắm mục tiêu lại của quảng cáo mua sắm:<br>• `LAB1`: Nhắm lại người dùng đã xem sản phẩm hoặc thêm vào giỏ nhưng chưa mua.<br>• `LAB2`: Nhắm lại người dùng đã thêm vào giỏ nhưng chưa mua.<br>• `LAB3`: Nhắm lại theo tổ hợp tùy chỉnh.<br>• `OFF`: Không nhắm mục tiêu lại. |
| shopping_ads_retargeting_actions_days | number | Có điều kiện | Bắt buộc khi `shopping_ads_retargeting_type` là `LAB1` hoặc `LAB2`. Khoảng thời gian thực hiện hành vi (ngày): `1`, `2`, `3`, `7`, `14`, `30`, `60`, `90`, `180`. |
| included_custom_actions | object[] | Có điều kiện | Khi `shopping_ads_retargeting_type` là `LAB3`, cần truyền `included_custom_actions` hoặc `excluded_custom_actions`. Hành vi tùy chỉnh làm điều kiện "Bao gồm". |
| ↳ code | string | Mã hành vi: `VIEW_PRODUCT` (xem sản phẩm), `ADD_TO_CART` (thêm vào giỏ), `PURCHASE` (mua hàng). |
| ↳ days | integer | Khoảng thời gian người dùng đã thực hiện hành vi (1–180 ngày). |
| excluded_custom_actions | object[] | Có điều kiện | Khi `shopping_ads_retargeting_type` là `LAB3`, hành vi tùy chỉnh làm điều kiện "Loại trừ". |
| ↳ code | string | Mã hành vi: `VIEW_PRODUCT`, `ADD_TO_CART`, `PURCHASE`. |
| ↳ days | integer | Khoảng thời gian người dùng không thực hiện hành vi (1–180 ngày). |
| audience_ids | string[] | Không bắt buộc | Danh sách ID tệp đối tượng tùy chỉnh. Lấy qua endpoint [/dmp/custom_audience/list/](09-audience.md#doc-1739940506015746). |
| excluded_audience_ids | string[] | Không bắt buộc | Danh sách ID tệp đối tượng cần loại trừ. |
| audience_rule | object | Không bắt buộc | Quy tắc đối tượng, hợp lệ khi `objective_type` là `TRAFFIC` hoặc `WEB_CONVERSIONS`. Xem chi tiết tại [Quy tắc đối tượng](../09-marketing-api/audience.md#doc-1739566532187138). |
| audience_type | string | Không bắt buộc | Loại tệp đối tượng nhắm lại ứng dụng. Xem [Enum - Loại đối tượng nhắm lại ứng dụng](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| location_ids | string[] | Có điều kiện | Danh sách ID vị trí địa lý muốn nhắm mục tiêu. Cần thiết lập `location_ids` hoặc `zipcode_ids` hoặc cả hai. Tối đa 3.000 phần tử. Xem **Location IDs**. Không hỗ trợ các vị trí trùng lặp/chồng chéo (ví dụ: không thể cùng lúc nhắm toàn bộ Hoa Kỳ và bang California). |
| zipcode_ids | string[] | Có điều kiện | Danh sách mã bưu chính muốn nhắm mục tiêu (hỗ trợ US, Canada, Brazil, Indonesia, Thái Lan, Việt Nam). Cần thiết lập `location_ids` hoặc `zipcode_ids` hoặc cả hai. Tối đa 3.000 phần tử. |
| isp_ids | string[] | Không bắt buộc | Danh sách ID nhà cung cấp dịch vụ Internet (ISP). Chỉ hợp lệ khi chỉ định vị trí cấp quốc gia/vùng lãnh thổ qua `location_ids`. Lấy qua [/tool/targeting/list/](70-tools-p2.md#doc-1762962378261506). |
| gender | string | Không bắt buộc | Giới tính nhắm mục tiêu: `GENDER_FEMALE`, `GENDER_MALE`, `GENDER_UNLIMITED`. |
| age_groups | string[] | Không bắt buộc | Nhóm tuổi nhắm mục tiêu. Xem [Enum - Nhóm tuổi](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| languages | string[] | Không bắt buộc | Mã ngôn ngữ muốn nhắm mục tiêu. Xem [Enum - Mã ngôn ngữ](../15-appendix/phu-luc-p1.md#doc-1737174886619138). Để trống hoặc không truyền nếu không muốn giới hạn ngôn ngữ. |
| interest_category_ids | string[] | Không bắt buộc | Danh sách ID danh mục sở thích chung. Tra cứu qua [/targeting/search/](70-tools-p1.md#doc-1796638342793218) hoặc [/tool/interest_category/](70-tools-p1.md#doc-1737174348712961). |
| interest_keyword_ids | string[] | Không bắt buộc | Danh sách ID từ khóa sở thích bổ sung. Tra cứu qua [/targeting/search/](70-tools-p1.md#doc-1796638342793218). |
| purchase_intention_keyword_ids | string[] | Không bắt buộc | Danh sách ID danh mục ý định mua sắm. Tra cứu qua [/targeting/search/](70-tools-p1.md#doc-1796638342793218). Không truyền đồng thời với `interest_keyword_ids`. |
| actions | object[] | Không bắt buộc | Danh sách đối tượng danh mục hành vi nhắm mục tiêu. |
| ↳ action_scene | string | Không bắt buộc | Loại hành vi người dùng: `VIDEO_RELATED`, `CREATOR_RELATED`, `HASHTAG_RELATED`. |
| ↳ action_period | number | Không bắt buộc | Khung thời gian ghi nhận hành vi (ngày): `0`, `7`, `15`. Với `CREATOR_RELATED` hoặc `HASHTAG_RELATED`, giá trị luôn là `0`. |
| ↳ video_user_actions | string[] | Không bắt buộc | Hành vi người dùng cụ thể: `WATCHED_TO_END`, `LIKED`, `COMMENTED`, `SHARED`, `FOLLOWING`, `VIEW_HOMEPAGE`, `VIEW_HASHTAG`. |
| ↳ action_category_ids | string[] | Không bắt buộc | Danh sách ID danh mục tương tác video, người sáng tạo hoặc hashtag (chỉ hợp lệ khi chỉ chọn vị trí TikTok). |
| operating_systems | string[] | Có điều kiện | Hệ điều hành thiết bị: `ANDROID`, `IOS`. Bắt buộc khi `objective_type` là `APP_PROMOTION`, hoặc `objective_type` là `TRAFFIC` và `promotion_type` là `APP_IOS`/`APP_ANDROID`. |
| min_ios_version | string | Không bắt buộc | Phiên bản iOS tối thiểu. Xem [Enum - Phiên bản iOS](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| min_android_version | string | Không bắt buộc | Phiên bản Android tối thiểu. Xem [Enum - Phiên bản Android](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| device_model_ids | string[] | Không bắt buộc | Danh sách ID mẫu thiết bị nhắm mục tiêu. Xem [/tool/device_model/](70-tools-p1.md#doc-1737172880570369). Không thể thiết lập đồng thời với `device_price_ranges`. |
| network_types | string[] | Không bắt buộc | Loại kết nối mạng thiết bị: `WIFI`, `2G`, `3G`, `4G`, `5G`. Mặc định: `unlimited`. |
| household_income | string[] | Không bắt buộc | Thu nhập hộ gia đình: `TOP5`, `TOP10`, `TOP10_25`, `TOP25_50`. Chỉ hỗ trợ quảng cáo đấu thầu cho vị trí TikTok tại Mỹ. |
| spending_power | string | Không bắt buộc | Sức chi tiêu của người dùng: `ALL`, `HIGH` (người dùng chi tiêu cao). Không hỗ trợ mục tiêu `PRODUCT_SALES` và `RF_REACH`. |
| device_price_ranges | number[] | Không bắt buộc | Khoảng giá thiết bị (bội số của 50). Ví dụ: `[0, 250]` thực tế đại diện cho khoảng [0, 300]. |
| carrier_ids | string[] | Không bắt buộc | Nhà mạng viễn thông nhắm mục tiêu. Xem [/tool/carrier/](70-tools-p1.md#doc-1737168013095938). |
| included_pangle_audience_package_ids | string[] | Không bắt buộc | Danh sách ID gói đối tượng Pangle bao gồm (chỉ hợp lệ cho vị trí Pangle). Không truyền đồng thời với `excluded_pangle_audience_package_ids`. |
| excluded_pangle_audience_package_ids | string[] | Không bắt buộc | Danh sách ID gói đối tượng Pangle loại trừ. |
| blocked_pangle_app_ids | string[] | Không bắt buộc | ID danh sách chặn ứng dụng Pangle. Xem [Lấy danh sách chặn Pangle](55-pangle.md#doc-1740039957181441). |
| targeting_expansion {-To be deprecated} | object | Không bắt buộc | Cài đặt mở rộng nhắm mục tiêu. |
| ↳ expansion_enabled | boolean | Không bắt buộc | Có bật mở rộng nhắm mục tiêu hay không. |
| ↳ expansion_types | string[] | Có điều kiện | Các loại đối tượng muốn mở rộng: `AGE`, `GENDER`, `INTEREST_AND_BEHAVIOR`, `CUSTOM_AUDIENCE`. Bắt buộc khi `expansion_enabled` là `true`. |
| auto_targeting_enabled {-To be deprecated} | boolean | Không bắt buộc | Có bật nhắm mục tiêu tự động hay không: `True`, `False`. |
| contextual_tag_ids | string[] | Không bắt buộc | Danh sách ID thẻ ngữ cảnh. Chỉ hỗ trợ mục tiêu `REACH` và `VIDEO_VIEWS`. Cần allowlist. Xem [Nhắm mục tiêu theo ngữ cảnh](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1745292519923713). |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi. Xem chi tiết tại [Phụ lục - Mã trả về](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. |
| request_id | string | ID log của yêu cầu, định danh duy nhất cho một yêu cầu HTTP. |
| data | object | Dữ liệu ước tính quy mô tệp đối tượng. |
| ↳ user_count_stage | number | Đánh giá mức độ quy mô của đối tượng ước tính.<br>Giá trị enum:<br>• `1`: Quá hẹp (Too Narrow). Quy mô ước tính dưới 10.000 và chiếm dưới 20% quy mô tiềm năng tại các vị trí đã chọn.<br>• `2`: Hẹp (Narrow). Quy mô từ 10.000 trở lên nhưng vẫn chiếm dưới 20% quy mô tiềm năng.<br>• `3`: Cân bằng (Balanced). Quy mô chiếm từ 20% đến dưới 80% quy mô tiềm năng.<br>• `4`: Khá rộng (Fairly Broad). Quy mô chiếm từ 80% trở lên quy mô tiềm năng. |
| ↳ user_count | object | Quy mô đối tượng ước tính (khoảng số lượng người dùng). |
| ↳↳ lower_end | number | Cận dưới của khoảng quy mô đối tượng ước tính. |
| ↳↳ upper_end | number | Cận trên của khoảng quy mô đối tượng ước tính. |
| ↳ purchase_intention_keyword_ids | string[] | Danh sách ID từ khóa ý định mua sắm dùng để nhắm mục tiêu. |

### Ví dụ

#### Gọi API bằng curl

```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/ad/audience_size/estimate/' \
  --header 'Access-Token: YOUR_ACCESS_TOKEN' \
  --header 'Content-Type: application/json' \
  --data '{
    "advertiser_id": "7123456789012345678",
    "placement_type": "PLACEMENT_TYPE_AUTOMATIC",
    "objective_type": "REACH",
    "optimization_goal": "CLICK",
    "location_ids": [
        "6252001"
    ],
    "auto_targeting_enabled": true
}'
```

#### Gọi API bằng Python

```python
import requests

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ADVERTISER_ID = "7123456789012345678"

url = "https://business-api.tiktok.com/open_api/v1.3/ad/audience_size/estimate/"
headers = {
    "Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}
payload = {
    "advertiser_id": ADVERTISER_ID,
    "placement_type": "PLACEMENT_TYPE_AUTOMATIC",
    "objective_type": "REACH",
    "optimization_goal": "CLICK",
    "location_ids": ["6252001"],
    "auto_targeting_enabled": True
}

response = requests.post(url, headers=headers, json=payload)
print(response.status_code)
print(response.json())
```

#### Ví dụ phản hồi thành công

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "2021090909090909024510008412345678",
  "data": {
    "user_count_stage": 3,
    "user_count": {
      "lower_end": 107229000,
      "upper_end": 131059000
    }
  }
}
```
