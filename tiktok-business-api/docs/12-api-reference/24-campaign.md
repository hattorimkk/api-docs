# Chiến dịch (Campaign)

Tài liệu này cung cấp hướng dẫn chi tiết và đặc tả kỹ thuật cho các API quản lý Chiến dịch (Campaign) trong TikTok for Business API v1.3.

Chiến dịch là cấp độ cao nhất trong cấu trúc quảng cáo TikTok (bao gồm Chiến dịch > Nhóm quảng cáo > Quảng cáo). Khi tạo chiến dịch, bạn xác định mục tiêu quảng cáo (advertising objective), ngân sách (budget), loại hình chiến dịch (thủ công, Smart+, hoặc chiến dịch chuyên dụng cho ứng dụng iOS) cùng các chính sách liên quan.

## Danh sách các endpoint

| Phương thức | Endpoint | Mô tả |
|---|---|---|
| `GET` | `/open_api/v1.3/campaign/get/` | Lấy danh sách chiến dịch của tài khoản quảng cáo kèm bộ lọc |
| `POST` | `/open_api/v1.3/campaign/create/` | Tạo mới một chiến dịch quảng cáo |
| `POST` | `/open_api/v1.3/campaign/update/` | Cập nhật thông tin chiến dịch đã tạo |
| `POST` | `/open_api/v1.3/campaign/status/update/` | Cập nhật trạng thái hoạt động (bật, tắt, xóa) của chiến dịch |
| `GET` | `/open_api/v1.3/campaign/quota/info/` | Lấy hạn mức Chiến dịch chuyên dụng SKAN theo mạng quảng cáo |
| `POST` | `/open_api/v1.3/campaign/copy/task/create/` | Tạo tác vụ sao chép bất đồng bộ cho Chiến dịch thủ công |
| `GET` | `/open_api/v1.3/campaign/copy/task/check/` | Kiểm tra kết quả tác vụ sao chép bất đồng bộ cho Chiến dịch thủ công |
| `GET` | `/open_api/v1.3/campaign/quota/get/` | *(Không dùng nữa)* Lấy hạn mức cho Chiến dịch chuyên dụng iOS 14 |

---

## Tổng quan về Chiến dịch (`Campaign`)
<a id="doc-1739315728330753"></a>
<!-- doc_id: 1739315728330753 -->

Chiến dịch (Campaign) là cấp độ cao nhất trong cấu trúc phân cấp quảng cáo. Để triển khai quảng cáo trên TikTok for Business, trước tiên bạn cần tạo một chiến dịch và thiết lập mục tiêu quảng cáo (advertising objective).

Xem [Hướng dẫn - Chiến dịch (Guides-Campaign)](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1745292231199745) để tìm hiểu quy trình tạo chiến dịch và nắm bắt các khái niệm về mục tiêu quảng cáo, ngân sách, Tiếp cận & Tần suất (Reach & Frequency), cũng như Chiến dịch chuyên dụng iOS 14 (iOS 14 Dedicated Campaign). Xem [Cấu trúc quảng cáo (Ad structure)](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1739381193120770) để tìm hiểu chi tiết về ba cấp độ quảng cáo của TikTok.

Nhóm API này bao gồm các endpoint sau:

* [Lấy danh sách chiến dịch](24-campaign.md#doc-1739315828649986)
* [Tạo chiến dịch](24-campaign.md#doc-1739318962329602)
* [Cập nhật chiến dịch](24-campaign.md#doc-1739320422086657)
* [Cập nhật trạng thái hoạt động của chiến dịch](24-campaign.md#doc-1739320994354178)
* [Lấy hạn mức cho Chiến dịch chuyên dụng theo mạng quảng cáo](24-campaign.md#doc-1752256376677378)
* [Tạo tác vụ sao chép bất đồng bộ cho Chiến dịch thủ công](24-campaign.md#doc-1788434394151938)
* [Lấy kết quả tác vụ sao chép bất đồng bộ cho Chiến dịch thủ công](24-campaign.md#doc-1788434463507458)

---

## Lấy danh sách chiến dịch (`Get campaigns`)
<a id="doc-1739315828649986"></a>
<!-- doc_id: 1739315828649986 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/campaign/get/`

**Mục đích**: Sử dụng endpoint này để lấy danh sách tất cả các chiến dịch thuộc một tài khoản quảng cáo. Bạn có thể áp dụng các bộ lọc trong yêu cầu để chỉ nhận về các chiến dịch thỏa mãn điều kiện nhất định.

> [!NOTE]
> Nếu bạn muốn truy vấn các chiến dịch đã bị xóa trong yêu cầu, hãy chỉ định giá trị `STATUS_DELETE` trong trường `primary_status` hoặc `CAMPAIGN_STATUS_DELETE` trong trường `secondary_status`. Dữ liệu đã xóa theo mặc định sẽ không được trả về.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Access token (mã truy cập) đã được ủy quyền. Chi tiết xem [Xác thực (Authentication)](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (Query Parameters)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| advertiser_id | string | Bắt buộc | ID của nhà quảng cáo / tài khoản quảng cáo. |
| fields | string[] | Không bắt buộc | Danh sách các trường bạn muốn lấy trong kết quả.<br>Khi không chỉ định, tất cả các trường sẽ được trả về theo mặc định.<br>Để biết các trường được hỗ trợ, hãy xem các trường dưới mục `list` trong phần Phản hồi. |
| exclude_field_types_in_response | string[] | Không bắt buộc | Loại trường bạn muốn loại bỏ khỏi phản hồi.<br>Giá trị enum được hỗ trợ:<br>• `NULL_FIELD`: Các trường có giá trị null. |
| filtering | object | Không bắt buộc | Bộ lọc dữ liệu. Được truyền dưới dạng chuỗi JSON.<br>Ví dụ: `filtering={"campaign_automation_type":"UPGRADED_SMART_PLUS"}` |
| ↳ campaign_automation_type | string | Không bắt buộc | Loại tự động hóa chiến dịch.<br>Giá trị enum:<br>• `MANUAL`: Chiến dịch thủ công (Manual Campaigns).<br>• `SMART_PLUS`: Chiến dịch Smart+ (Smart+ Campaigns).<br>• `UPGRADED_SMART_PLUS`: Chiến dịch Smart+ nâng cấp (Upgraded Smart+ Campaigns), một loại chiến dịch tự động mới. Để tìm hiểu thêm, xem [Chiến dịch Smart+ nâng cấp](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1853452461203458). |
| ↳ campaign_ids | string[] | Không bắt buộc | Lọc theo danh sách ID chiến dịch.<br>Số lượng tối đa: 100. |
| ↳ campaign_name | string | Không bắt buộc | Lọc theo tên chiến dịch. Hỗ trợ khớp mờ (fuzzy match). |
| ↳ campaign_system_origins | string[] | Không bắt buộc | Lọc theo nguồn gốc hệ thống của chiến dịch (campaign sources).<br>Giá trị enum:<br>• `PROMOTE`: Chiến dịch Promote được tạo qua ứng dụng TikTok trên di động.<br>• `TT_ADS_PLATFORM`: Chiến dịch thông thường (không phải Promote) được tạo qua API hoặc trên TikTok Ads Manager.<br>Giá trị mặc định: `["TT_ADS_PLATFORM"]`.<br>Lưu ý: Đối với chiến dịch Promote, chỉ có các thiết lập sau được trả về: `advertiser_id`, `campaign_id`, `create_time`, `campaign_name`, `operation_status`, `secondary_status`.<br>Để tìm hiểu thêm về tính khả dụng và bộ lọc hỗ trợ cho chiến dịch Promote, xem [Chiến dịch Promote](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1785880454546433). |
| ↳ primary_status | string | Không bắt buộc | Trạng thái chính của chiến dịch.<br>Để biết các giá trị enum, xem [Enum - Trạng thái chính (Primary Status)](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ secondary_status | string | Không bắt buộc | Lọc theo trạng thái phụ của chiến dịch.<br>Để biết các giá trị enum, xem [Enum - Trạng thái chiến dịch - Trạng thái phụ](../15-appendix/phu-luc-p1.md#doc-1737174886619138).<br>**Lưu ý**:<br>• Trường này không được trả về trong môi trường sandbox vì chiến dịch không thực sự phân phối.<br>• Xem [Trạng thái phụ được hỗ trợ theo trạng thái chính](../09-marketing-api/quan-ly-chien-dich-tom-tat.md#doc-1757239620352002) để biết các giá trị hợp lệ có thể truyền vào `secondary_status` tương ứng với `primary_status` đã chỉ định. |
| ↳ objective_type | string | Không bắt buộc | Lọc theo mục tiêu quảng cáo.<br>Xem [Enum - Mục tiêu quảng cáo (Advertising Objective)](../15-appendix/phu-luc-p1.md#doc-1737174886619138) để biết các giá trị enum. |
| ↳ sales_destination | string | Không bắt buộc | Đích bán hàng, nơi bạn muốn thúc đẩy doanh số.<br>Giá trị enum:<br>• `TIKTOK_SHOP`: TikTok Shop. Thúc đẩy doanh số trên TikTok Shop của bạn.<br>• `WEBSITE`: Website. Thúc đẩy doanh số trên trang web của bạn.<br>• `APP`: Ứng dụng (App). Thúc đẩy doanh số trên ứng dụng của bạn (yêu cầu danh mục sản phẩm).<br>• `WEB_AND_APP`: Website và ứng dụng. Thúc đẩy doanh số trên cả trang web lẫn ứng dụng. |
| ↳ buying_types | string[] | Không bắt buộc | Lọc theo hình thức mua.<br>Giá trị enum:<br>• `AUCTION`: Quảng cáo đấu thầu (Auction ads).<br>• `RESERVATION_RF`: Quảng cáo đặt trước Tiếp cận & Tần suất (Reservation Reach & Frequency ads) và quảng cáo TikTok Pulse.<br>• `RESERVATION_TOP_VIEW`: Quảng cáo đặt trước TopView.<br>Giá trị mặc định: `["AUCTION", "RESERVATION_RF"]`.<br>Để tìm hiểu thêm về tính khả dụng của quảng cáo TopView trong API, xem [TopView](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1804258360285186).<br>**Lưu ý**: Giá trị enum `RESERVATION_TOP_VIEW` không thể kết hợp cùng lúc với các giá trị khác. Để lọc quảng cáo TopView, hãy đặt trường này thành `["RESERVATION_TOP_VIEW"]`. |
| ↳ is_smart_performance_campaign | boolean | Không bắt buộc | Lọc theo việc chiến dịch có phải là loại chiến dịch tự động hay không.<br>Giá trị hỗ trợ:<br>• `true`: Chiến dịch là Smart+ Campaign hoặc Smart Performance Web Campaign.<br>• `false`: Chiến dịch thuộc loại tiêu chuẩn (standard campaign).<br>**Lưu ý**: Nếu bạn không chỉ định trường này, API sẽ trả về tất cả các chiến dịch. |
| ↳ creative_campaign_type | string[] | Không bắt buộc | Lọc xem chiến dịch là Smart+, Chiến dịch quảng cáo tìm kiếm (Search Ads Campaign), hay loại khác.<br>Giá trị enum:<br>• `SPC`: Lọc các Chiến dịch Smart+.<br>• `SEARCH_CAMPAIGN`: Lọc các Chiến dịch quảng cáo tìm kiếm.<br>• `OTHER`: Lọc các chiến dịch không phải Smart+ và không phải Search Ads.<br>Nếu không chỉ định trường này, bạn sẽ nhận được tất cả các chiến dịch. |
| ↳ split_test_enabled | boolean | Không bắt buộc | Lọc theo việc thử nghiệm phân tách (split test) có được bật cho chiến dịch hay không.<br>`true`: Chỉ lấy các chiến dịch đã bật split test.<br>`false`: Chỉ lấy các chiến dịch tắt split test.<br>**Lưu ý**: Nếu không chỉ định, bạn sẽ nhận về tất cả các chiến dịch. |
| ↳ campaign_product_source | string | Không bắt buộc | Lọc theo nguồn sản phẩm của chiến dịch.<br>Giá trị enum:<br>• `CATALOG`: Danh mục sản phẩm (Catalog).<br>• `STORE`: TikTok Shop hoặc TikTok Showcase.<br>Nếu bạn truyền trường này, kết quả sẽ chỉ bao gồm các chiến dịch có mục tiêu quảng cáo Doanh số sản phẩm (`objective_type` = `PRODUCT_SALES`). Bộ lọc `objective_type` nếu chỉ định đồng thời thì chỉ có thể đặt là `PRODUCT_SALES`. |
| ↳ optimization_goal | string | Không bắt buộc | Mục tiêu tối ưu hóa.<br>Giá trị enum xem tại [Enum - Mục tiêu tối ưu hóa (Optimization Goal)](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ campaign_type | string | Không bắt buộc | Dùng trường này để lọc chiến dịch thông thường hoặc chiến dịch iOS 14.<br>Giá trị enum: `REGULAR_CAMPAIGN`, `IOS14_CAMPAIGN`.<br>Để tìm hiểu cách tạo chiến dịch iOS 14, xem [Tạo chiến dịch iOS 14](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1737719523561474). |
| ↳ creation_filter_start_time | string | Không bắt buộc | Lọc theo mốc thời gian bắt đầu tạo chiến dịch, định dạng `YYYY-MM-DD HH:MM:SS` (múi giờ UTC). Các chiến dịch được tạo sau thời điểm này sẽ được trả về.<br>Khuyến nghị: Khoảng thời gian lọc không nên vượt quá 6 tháng để đảm bảo tốc độ và tỷ lệ thành công của truy vấn. |
| ↳ creation_filter_end_time | string | Không bắt buộc | Lọc theo mốc thời gian kết thúc tạo chiến dịch, định dạng `YYYY-MM-DD HH:MM:SS` (múi giờ UTC). Các chiến dịch được tạo trước thời điểm này sẽ được trả về.<br>Khuyến nghị: Khoảng thời gian lọc không nên vượt quá 6 tháng. |
| ↳ gmv_max_promotion_types {-Deprecated} | string[] | Không bắt buộc | *(Đã ngừng hỗ trợ)* Loại Chiến dịch GMV Max.<br>Giá trị enum:<br>• `PRODUCT_GMV_MAX`: [Chiến dịch GMV Max Sản phẩm](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1822009220448257).<br>• `LIVE_GMV_MAX`: [Chiến dịch GMV Max Phát trực tiếp (Live)](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1822009242546258).<br>**Lưu ý**: Để lọc các chiến dịch GMV Max, hãy sử dụng endpoint [/gmv_max/campaign/get/](45-gmv-max-p1.md#doc-1826463372290177). |
| ↳ store_ids {-Deprecated} | string[] | Không bắt buộc | *(Đã ngừng hỗ trợ)* Chỉ hợp lệ khi giá trị `gmv_max_promotion_types` chứa `LIVE_GMV_MAX` hoặc `PRODUCT_GMV_MAX`.<br>Danh sách ID TikTok Shop.<br>Số lượng tối đa: 10.<br>**Lưu ý**: Để lọc Chiến dịch GMV Max, sử dụng [/gmv_max/campaign/get/](45-gmv-max-p1.md#doc-1826463372290177). |
| page | number | Không bắt buộc | Số trang hiện tại.<br>Giá trị mặc định: `1`.<br>Khoảng giá trị: ≥ 1. |
| page_size | number | Không bắt buộc | Số bản ghi mỗi trang.<br>Giá trị mặc định: `10`.<br>Khoảng giá trị: 1–1.000. |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi. Xem danh sách đầy đủ mã phản hồi và mô tả tại [Phụ lục - Mã trả về (Return Codes)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. |
| request_id | string | ID log của yêu cầu, dùng để định danh duy nhất yêu cầu. |
| data | object | Dữ liệu trả về. Danh sách mặc định được sắp xếp giảm dần theo ID chiến dịch (`campaign_id`). |
| ↳ list | object[] | Danh sách các chiến dịch. Các trường trả về được tạo dựa trên tham số `fields` chỉ định trong yêu cầu. Mặc định trả về tất cả các trường. |
| ↳↳ advertiser_id | string | ID của nhà quảng cáo. |
| ↳↳ campaign_id | string | ID của chiến dịch. |
| ↳↳ campaign_system_origin | string | Chỉ trả về cho chiến dịch Promote. Không trả về cho chiến dịch thông thường.<br>Nguồn gốc hệ thống của chiến dịch.<br>Giá trị enum:<br>• `PROMOTE`: Chiến dịch Promote được tạo qua ứng dụng TikTok di động.<br>Chỉ các cài đặt sau có thể được truy xuất: `advertiser_id`, `campaign_id`, `create_time`, `campaign_name`, `operation_status`, `secondary_status`. |
| ↳↳ create_time | string | Thời gian tạo chiến dịch. |
| ↳↳ modify_time | string | Thời gian sửa đổi chiến dịch gần nhất. |
| ↳↳ objective_type | string | Mục tiêu quảng cáo.<br>Giá trị enum xem tại [Enum - Mục tiêu quảng cáo](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳↳ app_promotion_type | string | Loại quảng bá ứng dụng.<br>Giá trị enum:<br>• `APP_INSTALL`: Cài đặt ứng dụng. Tiếp cận người dùng mới để họ cài đặt ứng dụng.<br>• `APP_RETARGETING`: Nhắm mục tiêu lại ứng dụng. Tái tương tác với người dùng hiện tại để họ thực hiện hành động trong ứng dụng.<br>• `APP_PREREGISTRATION`: Đăng ký trước ứng dụng. Thu hút người dùng mới đăng ký trước khi ứng dụng ra mắt.<br>• `APP_POSTS_PROMOTION`: Quảng bá bài đăng ứng dụng. Quảng bá các bài đăng TikTok để tăng mức độ nhận biết ứng dụng và đo lường lượt chuyển đổi.<br>**Lưu ý**: Hiện tại chưa hỗ trợ tạo chiến dịch quảng bá bài đăng ứng dụng qua API. Bạn chỉ có thể cập nhật hoặc truy xuất các chiến dịch này qua API. |
| ↳↳ virtual_objective_type | string | Loại mục tiêu ảo mới.<br>Giá trị enum: `SALES`.<br>Sử dụng trường này để tạo chiến dịch với mục tiêu Bán hàng (Sales), mục tiêu kết hợp cho Chuyển đổi trên trang web (Website Conversions) và Doanh số sản phẩm (Product Sales). Tìm hiểu thêm về [mục tiêu Bán hàng](https://business-api.tiktok.com/portal/docs?id=). |
| ↳↳ sales_destination | string | Đích bán hàng, nơi bạn muốn thúc đẩy doanh số.<br>Giá trị enum:<br>• `TIKTOK_SHOP`: TikTok Shop.<br>• `WEBSITE`: Trang web.<br>• `APP`: Ứng dụng (yêu cầu danh mục sản phẩm).<br>• `WEB_AND_APP`: Trang web và ứng dụng. |
| ↳↳ is_search_campaign | boolean | Chiến dịch có phải là Chiến dịch quảng cáo tìm kiếm (Search Ads Campaign) hay không. Với Search Ads Campaign, bạn có thể chọn từ khóa và phân phối quảng cáo trên trang kết quả tìm kiếm của TikTok.<br>Giá trị: `true`, `false`. |
| ↳↳ campaign_automation_type | string | Loại tự động hóa chiến dịch.<br>Giá trị enum: `MANUAL`, `SMART_PLUS`, `UPGRADED_SMART_PLUS`. Xem thêm tại [Chiến dịch Smart+ nâng cấp](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1853452461203458). |
| ↳↳ is_smart_performance_campaign | boolean | Chiến dịch có phải là loại chiến dịch tự động hay không.<br>Giá trị hỗ trợ:<br>• `true`: Chiến dịch là Smart+ Campaign kế thừa (legacy Smart+ Campaign).<br>• `false`: Chiến dịch là Manual Campaign hoặc Upgraded Smart+ Campaign.<br>• Để xác định chiến dịch là Manual Campaign hay Upgraded Smart+ Campaign, hãy kiểm tra trường `campaign_automation_type` được trả về. Khi `campaign_automation_type` là `MANUAL`, đó là chiến dịch thủ công. Khi là `UPGRADED_SMART_PLUS`, đó là chiến dịch Smart+ nâng cấp. |
| ↳↳ campaign_type | string | Loại chiến dịch, cho biết chiến dịch thông thường hay chiến dịch iOS 14.<br>Giá trị enum: `REGULAR_CAMPAIGN`, `IOS14_CAMPAIGN`. |
| ↳↳ app_id | string | ID ứng dụng của ứng dụng được quảng bá.<br>Có thể lấy `app_id` qua endpoint [/app/list/](43-events-1-0-p1.md#doc-1740859313270786). |
| ↳↳ is_advanced_dedicated_campaign | boolean | Chiến dịch có phải là Chiến dịch chuyên dụng nâng cao (Advanced Dedicated Campaign) hay không. Loại chiến dịch này tận dụng các mô hình phân phối nâng cao hưởng lợi từ tín hiệu thời gian thực.<br>Giá trị enum: `true`, `false`. |
| ↳↳ disable_skan_campaign | boolean | Có tắt tính năng phân bổ SKAN (SKAdNetwork - giải pháp phân bổ chuyển đổi của Apple cho chiến dịch iOS) hay không.<br>Giá trị enum:<br>• `true`: Tắt phân bổ SKAN. Chiến dịch sẽ không bị ràng buộc bởi [Hạn mức Chiến dịch chuyên dụng](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1752256248260610) và bạn có thể lấy [các chỉ số Mạng tự phân bổ - SAN](../09-marketing-api/bao-cao-p2.md#doc-1751443967255553) cho chiến dịch. Tuy nhiên, bạn không thể truy xuất các chỉ số báo cáo SKAN. Xem thêm về [Tích hợp SAN](https://ads.tiktok.com/help/article/about-self-attribution-transition).<br>• `false`: Bật phân bổ SKAN. Chiến dịch sẽ bị ràng buộc bởi hạn mức và bạn có thể lấy các chỉ số SKAN. |
| ↳↳ bid_align_type | string | Loại phân bổ cho Chiến dịch chuyên dụng, xác định mạng phân bổ mà CPA mục tiêu (`conversion_bid_price`) hoặc ROAS mục tiêu (`roas_bid`) ở cấp nhóm quảng cáo dựa trên.<br>Giá trị enum: `SAN`, `SKAN`. |
| ↳↳ campaign_app_profile_page_state | string | Trạng thái của Trang hồ sơ ứng dụng (App Profile Page).<br>Giá trị enum: `INVALID`, `UNSET`, `ON`, `OFF`. |
| ↳↳ rf_campaign_type | string | Khi `objective_type` là `RF_REACH`, trường này chỉ định loại chiến dịch Đặt trước cụ thể.<br>Giá trị enum:<br>• `STANDARD`: Chiến dịch Tiếp cận & Tần suất (Reach & Frequency).<br>• `PULSE`: Chiến dịch TikTok Pulse.<br>• `TOPVIEW`: Chiến dịch TopView. |
| ↳↳ campaign_product_source | string | Chỉ trả về khi `objective_type` là `PRODUCT_SALES` và nguồn sản phẩm đã được cấu hình cho chiến dịch.<br>Nguồn sản phẩm của chiến dịch.<br>Giá trị enum: `CATALOG` (Danh mục), `STORE` (TikTok Shop hoặc TikTok Showcase). |
| ↳↳ catalog_enabled | boolean | Có sử dụng danh mục để tự động quảng cáo các sản phẩm/dịch vụ liên quan đến người dùng dựa trên sở thích, ý định và hành vi độc nhất của họ hay không. |
| ↳↳ campaign_name | string | Tên chiến dịch. |
| ↳↳ special_industries | string[] | Danh mục quảng cáo đặc biệt.<br>Giá trị enum:<br>• `HOUSING`: Bất động sản, bảo hiểm nhà ở, vay thế chấp.<br>• `EMPLOYMENT`: Tuyển dụng, thực tập, chương trình chứng chỉ chuyên môn.<br>• `CREDIT`: Thẻ tín dụng, vay mua ô tô, tài chính dài hạn.<br>**Lưu ý**:<br>• Áp dụng danh mục quảng cáo đặc biệt cho Shopping Ads với nguồn Danh mục hoặc ngoài Danh mục hiện là các tính năng chỉ dành cho danh sách cho phép (allowlist).<br>• Trường này khả dụng chung cho các nhà quảng cáo đăng ký tại Mỹ hoặc Canada. Nhà quảng cáo ở quốc gia khác muốn nhắm mục tiêu vào các quốc gia này với danh mục đặc biệt cần gửi yêu cầu đưa vào danh sách cho phép. |
| ↳↳ budget_optimize_on | boolean | Chỉ trả về cho các chiến dịch bật Tối ưu hóa ngân sách chiến dịch (Campaign Budget Optimization - CBO).<br>CBO có được bật hay không.<br>Giá trị enum: `true` (đã bật). Chi tiết về CBO xem [Tối ưu hóa ngân sách chiến dịch](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1739381757818881).<br>**Lưu ý**: Đối với Smart+ Campaigns hoặc Smart Performance Web Campaigns, giá trị trường này luôn là `true` vì CBO được bật mặc định. |
| ↳↳ bid_type | string | Chiến lược giá thầu ở cấp chiến dịch. |
| ↳↳ deep_bid_type | string | Chiến lược giá thầu cho sự kiện chuyên sâu trong ứng dụng.<br>Giá trị enum xem tại [Enum - Chiến lược giá thầu chuyên sâu](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳↳ roas_bid | float | Mục tiêu ROAS cho Tối ưu hóa giá trị (Value Optimization). |
| ↳↳ optimization_goal | string | Mục tiêu tối ưu hóa. |
| ↳↳ budget_mode | string | Chế độ ngân sách.<br>Giá trị enum:<br>• `BUDGET_MODE_INFINITE`: Ngân sách không giới hạn.<br>• `BUDGET_MODE_TOTAL`: Ngân sách trọn đời (tổng ngân sách).<br>• `BUDGET_MODE_DAY`: Ngân sách hàng ngày.<br>• `BUDGET_MODE_DYNAMIC_DAILY_BUDGET`: Ngân sách hàng ngày động. Đây là mức ngân sách hàng ngày trung bình trong một tuần. Chi phí mỗi ngày sẽ không vượt quá 125% mức trung bình và chi phí mỗi tuần không vượt quá ngân sách trung bình * 7. |
| ↳↳ budget | float | Ngân sách của chiến dịch. |
| ↳↳ rta_id | string | Realtime API (RTA) ID, mã định danh chiến lược RTA. |
| ↳↳ rta_bid_enabled | boolean | Có sử dụng giá thầu RTA hay không.<br>Giá trị: `true` (bật), `false` (tắt). |
| ↳↳ rta_product_selection_enabled | boolean | Có sử dụng RTA để tự động chọn sản phẩm hay không.<br>Giá trị enum: `true` (bật), `false` (tắt). |
| ↳↳ operation_status | string | Trạng thái hoạt động.<br>Giá trị enum:<br>• `ENABLE`: Chiến dịch đang bật.<br>• `DISABLE`: Chiến dịch đang tắt. |
| ↳↳ secondary_status | string | Trạng thái phụ của chiến dịch.<br>Xem [Enum - Trạng thái chiến dịch - Trạng thái phụ](../15-appendix/phu-luc-p1.md#doc-1737174886619138).<br>**Lưu ý**: Không trả về trong môi trường sandbox. |
| ↳↳ postback_window_mode | string | Chế độ xác định khung thời gian nhận postback SKAN 4.0 bạn muốn đảm bảo.<br>Giá trị enum:<br>• `POSTBACK_WINDOW_MODE1`: Đảm bảo postback đầu tiên (cửa sổ phân bổ 0–2 ngày). Dữ liệu có thể mất tối đa 4 ngày để trả về, và chiến dịch sẽ đợi 4 ngày để giải phóng hạn mức.<br>• `POSTBACK_WINDOW_MODE2`: Đảm bảo hai postback đầu (cửa sổ 3–7 ngày). Dữ liệu mất tối đa 13 ngày để trả về, và chiến dịch sẽ đợi 13 ngày để giải phóng hạn mức.<br>• `POSTBACK_WINDOW_MODE3`: Đảm bảo cả ba postback (cửa sổ 8–35 ngày). Dữ liệu mất tối đa 41 ngày để trả về, và chiến dịch sẽ đợi 41 ngày để giải phóng hạn mức.<br>**Lưu ý**: Xem thêm hướng dẫn chuyển đổi sang SKAN 4.0 tại [Về SKAN 4.0 và TikTok](https://ads.tiktok.com/help/article/about-skan-4-0-and-tiktok?lang=en). |
| ↳↳ is_new_structure | boolean | Chiến dịch có sử dụng cấu trúc mới hay không (trong cùng chiến dịch, cấu trúc chiến dịch, nhóm quảng cáo và quảng cáo đồng nhất). |
| ↳↳ objective | string | Loại chiến dịch (ứng dụng hoặc trang đích).<br>Giá trị enum: `APP` (ứng dụng), `LANDING_PAGE` (trang đích). |
| ↳↳ po_number | string | Mã đơn đặt hàng (Purchase Order - PO number). Hữu ích cho việc theo dõi hóa đơn và đối soát thanh toán.<br>Xem thêm tại [Cập nhật mã PO trên hóa đơn hàng tháng](https://ads.tiktok.com/help/article/update-po-number-on-monthly-invoices). |
| ↳ page_info | object | Thông tin phân trang. |
| ↳↳ page | number | Số trang hiện tại. |
| ↳↳ page_size | number | Số bản ghi trên mỗi trang. |
| ↳↳ total_number | number | Tổng số bản ghi kết quả. |
| ↳↳ total_page | number | Tổng số trang kết quả. |

### Ví dụ

#### Gọi API bằng curl

```bash
curl -G --location "https://business-api.tiktok.com/open_api/v1.3/campaign/get/" \
  --header "Access-Token: YOUR_ACCESS_TOKEN" \
  --data-urlencode "advertiser_id=7123456789012345678" \
  --data-urlencode "page=1" \
  --data-urlencode "page_size=10" \
  --data-urlencode 'filtering={"primary_status":"STATUS_ALL"}'
```

#### Gọi API bằng Python

```python
import json
import requests

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ADVERTISER_ID = "7123456789012345678"

url = "https://business-api.tiktok.com/open_api/v1.3/campaign/get/"
headers = {
    "Access-Token": ACCESS_TOKEN
}
params = {
    "advertiser_id": ADVERTISER_ID,
    "page": 1,
    "page_size": 10,
    "filtering": json.dumps({"primary_status": "STATUS_ALL"})
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
  "request_id": "2023052210032301011023224213551",
  "data": {
    "list": [
      {
        "secondary_status": "CAMPAIGN_STATUS_ENABLE",
        "advertiser_id": "7123456789012345678",
        "is_smart_performance_campaign": false,
        "campaign_name": "Summer_Promotion_2023",
        "is_new_structure": true,
        "campaign_type": "REGULAR_CAMPAIGN",
        "campaign_id": "1765432109876543",
        "roas_bid": 0,
        "budget_mode": "BUDGET_MODE_TOTAL",
        "modify_time": "2023-05-22 10:00:00",
        "operation_status": "ENABLE",
        "objective": "LANDING_PAGE",
        "objective_type": "TRAFFIC",
        "budget": 1000.0,
        "create_time": "2023-05-20 08:30:00",
        "deep_bid_type": null
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

## Tạo chiến dịch (`Create a campaign`)
<a id="doc-1739318962329602"></a>
<!-- doc_id: 1739318962329602 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/campaign/create/`

**Mục đích**: Sử dụng endpoint này để tạo một chiến dịch quảng cáo mới. Mỗi tài khoản quảng cáo có thể có tối đa 999 chiến dịch. Một chiến dịch có thể chứa một hoặc nhiều nhóm quảng cáo (ad groups).

Trước khi chuyển đổi các lệnh gọi API sang phiên bản v1.3, vui lòng xem [Di chuyển API quản lý chiến dịch (Migrate campaign management APIs)](../02-overview/tong-quan-va-phien-ban.md#doc-1749537346290689) để nắm bắt các điểm khác biệt nổi bật giữa API v1.2 và v1.3.

Để tìm hiểu về mối liên hệ giữa các tính năng trên TikTok Ads Manager (TTAM) ở cấp chiến dịch, nhóm quảng cáo, quảng cáo với cấu hình API tương ứng, xem [Ánh xạ giữa tính năng chiến dịch trên TikTok Ads Manager và cấu hình API](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1740673047618561).

> [!IMPORTANT]
> **Điều khoản Dữ liệu Trực tuyến (Online Data Terms)**: Khi sử dụng endpoint này, trong phạm vi bạn và TikTok chia sẻ dữ liệu cá nhân cho mục đích chiến dịch của bạn (ví dụ: nếu bạn chọn sử dụng công cụ nhà quảng cáo như TikTok Pixel hoặc làm việc với đối tác đo lường), bạn đồng ý với Điều khoản Dữ liệu Trực tuyến của TikTok, bao gồm [Điều khoản Sản phẩm Doanh nghiệp (Dữ liệu)](https://ads.tiktok.com/i18n/official/policy/business-products-terms), [Điều khoản Dữ liệu Người kiểm soát với Người kiểm soát](https://ads.tiktok.com/i18n/official/policy/controller-to-controller) và tất cả các điều khoản thành phần.
> Bạn đồng ý rằng Điều 13 của [Điều khoản dịch vụ thương mại TikTok](https://ads.tiktok.com/i18n/official/policy/commercial-terms-of-service) sẽ áp dụng cho mọi trách nhiệm pháp lý phát sinh từ hoặc liên quan đến Điều khoản Dữ liệu Trực tuyến. Để biết thêm thông tin, xem [Công cụ nhà quảng cáo TikTok và các điều khoản liên quan](https://ads.tiktok.com/help/article/tiktok-advertiser-tools-and-related-terms?redirected=1&lang=en) và [Điều khoản dữ liệu bên kiểm soát với bên kiểm soát](https://ads.tiktok.com/i18n/official/article?aid=619083947221699642).

### Trước khi bắt đầu
Xem lại các hướng dẫn từng bước trong [Tạo chiến dịch (Campaign creation)](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1758526151905281) để nắm rõ yêu cầu tham số cho các loại chiến dịch hoặc quảng cáo khác nhau. Nếu loại quảng cáo hoặc chiến dịch bạn muốn tạo chưa có trong tài liệu hướng dẫn hiện tại và bạn muốn yêu cầu tài liệu bổ sung, hãy liên hệ với đại diện TikTok của bạn.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Access token (mã truy cập) đã được ủy quyền. Chi tiết xem [Xác thực](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type | string | Bắt buộc | Định dạng nội dung yêu cầu. Giá trị hợp lệ: `application/json`. |

### Tham số (JSON Body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| advertiser_id | string | Bắt buộc | ID của nhà quảng cáo / tài khoản quảng cáo. |
| objective_type | string | Bắt buộc | Mục tiêu quảng cáo.<br>Xem danh sách giá trị enum và mô tả chi tiết tại [Mục tiêu quảng cáo (Objectives)](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1737585562434561). |
| app_promotion_type | string | Có điều kiện | Bắt buộc khi `objective_type` là `APP_PROMOTION`.<br>Loại quảng bá ứng dụng.<br>Giá trị enum:<br>• `APP_INSTALL`: Cài đặt ứng dụng.<br>• `APP_RETARGETING`: Nhắm mục tiêu lại ứng dụng.<br>• `APP_PREREGISTRATION`: Đăng ký trước ứng dụng. Để tìm hiểu cách tạo quảng cáo Đăng ký trước ứng dụng, xem [tại đây](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1772549012687873).<br>**Lưu ý**:<br>• `APP_INSTALL` có thể sử dụng trong Chiến dịch chuyên dụng iOS 14, trong khi `APP_RETARGETING` và `APP_PREREGISTRATION` thì không thể.<br>• Đăng ký trước ứng dụng hiện là tính năng chỉ dành cho danh sách cho phép (allowlist-only). Nếu cần dùng, hãy liên hệ đại diện TikTok của bạn. |
| virtual_objective_type | string | Không bắt buộc | Loại mục tiêu ảo mới.<br>Giá trị enum: `SALES`.<br>Dùng trường này để tạo chiến dịch với mục tiêu Bán hàng (Sales), mục tiêu kết hợp cho Chuyển đổi trên trang web (Website Conversions) và Doanh số sản phẩm (Product Sales). Xem thêm về [mục tiêu Bán hàng](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1834189283112962). |
| sales_destination | string | Có điều kiện | Bắt buộc và chỉ hợp lệ khi `virtual_objective_type` được chỉ định.<br>Đích bán hàng, nơi bạn muốn thúc đẩy doanh số.<br>Giá trị enum:<br>• `TIKTOK_SHOP`: TikTok Shop.<br>• `WEBSITE`: Trang web.<br>• `APP`: Ứng dụng (yêu cầu danh mục sản phẩm).<br>• `WEB_AND_APP`: Trang web và ứng dụng.<br>Để tìm hiểu cách tạo quảng cáo với thiết lập này, xem [Tạo quảng cáo với Tối ưu hóa Website và Ứng dụng](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1839876593708034).<br>**Lưu ý**: Tạo quảng cáo với Tối ưu hóa Website và Ứng dụng (`sales_destination` đặt là `WEB_AND_APP`) là tính năng chỉ dành cho danh sách cho phép. |
| is_search_campaign | boolean | Không bắt buộc | Có tạo Chiến dịch quảng cáo tìm kiếm (Search Ads Campaign) hay không.<br>Với Search Ads Campaign, bạn có thể chọn từ khóa và phân phối quảng cáo trên trang kết quả tìm kiếm của TikTok. Xem chi tiết tại [Tạo Chiến dịch quảng cáo tìm kiếm](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1815394136739841).<br>Giá trị hỗ trợ: `true`, `false`.<br>**Lưu ý**:<br>• Search Ads Campaign là tính năng chỉ dành cho danh sách cho phép.<br>• Một khi đã thiết lập, trường này không thể cập nhật. |
| campaign_type | string | Không bắt buộc | Loại chiến dịch.<br>Giá trị enum: `REGULAR_CAMPAIGN`, `IOS14_CAMPAIGN`.<br>Giá trị `IOS14_CAMPAIGN` hỗ trợ các mục tiêu quảng cáo `PRODUCT_SALES` và `APP_PROMOTION` (khi `app_promotion_type` = `APP_INSTALL`).<br>Nếu `app_promotion_type` là `APP_RETARGETING` hoặc `APP_PREREGISTRATION`, `campaign_type` chỉ có thể đặt là `REGULAR_CAMPAIGN`.<br>Đối với Chiến dịch chuyên dụng iOS với các mục tiêu khác, đặt `campaign_type` là `REGULAR_CAMPAIGN`.<br>Tìm hiểu thêm về Chiến dịch chuyên dụng tại [Chiến dịch chuyên dụng (Dedicated Campaign)](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1740029173531649). |
| app_id | string | Có điều kiện | Bắt buộc khi chiến dịch là Chiến dịch chuyên dụng iOS 14 (`campaign_type` = `IOS14_CAMPAIGN`) với mục tiêu quảng cáo (`objective_type`) là `PRODUCT_SALES` hoặc `APP_PROMOTION` (`app_promotion_type` = `APP_INSTALL`).<br>ID ứng dụng của ứng dụng được quảng bá.<br>Có thể lấy qua endpoint [/app/list/](43-events-1-0-p1.md#doc-1740859313270786).<br>**Lưu ý**: Bạn không thể chỉ định một ứng dụng chưa kích hoạt mô-đun SAN trên MMP để tạo Chiến dịch chuyên dụng iOS. Xem [Cách chuyển đổi sang SAN cho ứng dụng hiện có](https://ads.tiktok.com/help/article/transition-to-san-for-existing-apps) và [Cách tích hợp SAN cho ứng dụng mới](https://ads.tiktok.com/help/article/integrate-to-san-for-new-apps). |
| is_advanced_dedicated_campaign | boolean | Không bắt buộc | Chiến dịch có phải là Chiến dịch chuyên dụng nâng cao (Advanced Dedicated Campaign) hay không. Mô hình này tận dụng các tín hiệu thời gian thực.<br>Giá trị enum: `true`, `false`.<br>Giá trị mặc định: `false`.<br>Xem hướng dẫn tạo tại [Tạo Chiến dịch chuyên dụng nâng cao](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1797011827608577).<br>**Lưu ý**: Một khi đã thiết lập, trường này không thể sửa đổi. |
| disable_skan_campaign | boolean | Không bắt buộc | Chỉ hợp lệ khi đáp ứng đồng thời tất cả các điều kiện sau:<br>• `objective_type` là `APP_PROMOTION`.<br>• `app_promotion_type` là `APP_INSTALL`.<br>• `campaign_type` là `IOS14_CAMPAIGN`.<br>• `app_id` là ID của một ứng dụng iOS đủ điều kiện cho [Chiến dịch chuyên dụng nâng cao](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1797011827608577) (kiểm tra trường `advanced_dedicated_campaign_allowed` từ [/app/list/](43-events-1-0-p1.md#doc-1740859313270786)).<br>Quy định tắt phân bổ SKAN (giải pháp phân bổ của Apple cho iOS):<br>Giá trị enum:<br>• `true`: Tắt phân bổ SKAN. Chiến dịch không bị ràng buộc bởi [Hạn mức Chiến dịch chuyên dụng](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1752256248260610) và bạn có thể lấy [chỉ số SAN](../09-marketing-api/bao-cao-p2.md#doc-1751443967255553), nhưng không thể lấy chỉ số báo cáo SKAN. Đối với ứng dụng đủ điều kiện cho Chiến dịch chuyên dụng nâng cao, bạn phải bật ít nhất một trong hai: phân bổ SKAN hoặc Chiến dịch chuyên dụng nâng cao.<br>• `false`: Bật phân bổ SKAN. Chiến dịch bị ràng buộc bởi hạn mức và lấy được chỉ số SKAN. Nếu đồng thời đặt `is_advanced_dedicated_campaign` thành `true`, bạn sẽ lấy được cả chỉ số SAN lẫn SKAN.<br>**Lưu ý**:<br>• Tắt phân bổ SKAN cho Chiến dịch chuyên dụng là tính năng cần danh sách cho phép (allowlist).<br>• Nếu đã nằm trong danh sách cho phép tắt SKAN, bạn không thể đặt `bid_type` thành `BID_TYPE_CUSTOM` ở cấp nhóm quảng cáo khi cả `is_advanced_dedicated_campaign` và `disable_skan_campaign` đều là `false` và `optimization_goal` là `INSTALL` hoặc `IN_APP_EVENT`.<br>• Một khi đã thiết lập, trường này không thể sửa đổi. |
| campaign_app_profile_page_state | string | Không bắt buộc | Có sử dụng trang hồ sơ ứng dụng (App Profile Page) để tối ưu hóa phân phối hay không.<br>Giá trị enum: `ON`, `OFF`.<br>Giá trị mặc định: `OFF`.<br>Chỉ có thể dùng trường này khi `objective_type` là `APP_PROMOTION` và chiến dịch là Chiến dịch chuyên dụng iOS 14. Nếu không, lỗi sẽ xảy ra. |
| rf_campaign_type | string | Không bắt buộc | Khi `objective_type` là `RF_REACH`, sử dụng trường này để đặt chiến dịch thành chiến dịch TikTok Pulse, từ đó nhận các thẻ ngữ cảnh cao cấp (premium contextual tags).<br>Không truyền trường này khi `objective_type` không phải `RF_REACH`.<br>Giá trị enum: `STANDARD` (Chiến dịch Tiếp cận & Tần suất), `PULSE` (Chiến dịch TikTok Pulse).<br>**Lưu ý**:<br>• Đây là tính năng chỉ dành cho danh sách cho phép.<br>• Không thể sửa đổi trường này sau khi tạo.<br>• Nếu chọn `PULSE`, bạn phải nhập thẻ ngữ cảnh loại `PREMIUM` vào trường `contextual_tag_ids` trong [/adgroup/rf/create/](57-reach-and-frequency.md#doc-1738235338194945). Khi đó, CPM ở nhóm quảng cáo là cố định.<br>• Nếu đặt là `PULSE`, vị trí nhắm mục tiêu không thể cập nhật trong [/adgroup/rf/update/](57-reach-and-frequency.md#doc-1738235402874882) và `feed_type` không thể là `TOP_FEED` trong [/adgroup/rf/create/](57-reach-and-frequency.md#doc-1738235338194945). |
| campaign_product_source | string | Có điều kiện | Bắt buộc khi `objective_type` đặt là `PRODUCT_SALES`.<br>Nguồn sản phẩm của chiến dịch.<br>Giá trị enum:<br>• `CATALOG`: Danh mục sản phẩm.<br>• `STORE`: TikTok Shop hoặc TikTok Showcase.<br>**Lưu ý**:<br>• Mục tiêu `PRODUCT_SALES` là tính năng cần đưa vào danh sách cho phép.<br>• Với [Quảng cáo mua sắm dạng video (Video Shopping Ads)](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1741942291730434), cài đặt nguồn sản phẩm ở cấp chiến dịch quyết định nguồn sản phẩm khả dụng ở cấp nhóm quảng cáo: Nếu đặt là `CATALOG`, nhóm quảng cáo bên dưới phải đặt `product_source` là `CATALOG`; nếu đặt là `STORE`, nhóm quảng cáo bên dưới phải đặt `product_source` là `STORE` hoặc `SHOWCASE`. |
| catalog_enabled | boolean | Không bắt buộc | Có sử dụng danh mục để tự động quảng cáo các sản phẩm/dịch vụ phù hợp hay không.<br>Giá trị: `true`, `false`. Giá trị mặc định: `false`.<br>Chỉ đặt trường này thành `true` khi bạn muốn [tạo Quảng cáo ô tô cho kho hàng](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1827752507854850) hoặc [Quảng cáo ô tô cho mẫu xe](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1829635758164994).<br>Khi `objective_type` là `PRODUCT_SALES` và `campaign_product_source` là `CATALOG`, trường này sẽ tự động ghi đè thành `true`.<br>**Lưu ý**: Một khi đã đặt, không thể sửa đổi. |
| campaign_name | string | Bắt buộc | Tên chiến dịch.<br>Giới hạn độ dài: tối đa 512 ký tự. Không hỗ trợ emoji.<br>Mỗi ký tự tiếng Trung hoặc tiếng Nhật tính là 2 ký tự, mỗi chữ cái tiếng Anh tính là 1 ký tự. |
| request_id | string | Không bắt buộc | ID yêu cầu cho phép tạo các chiến dịch có tên trùng lặp hoặc thực hiện cơ chế gửi lại an toàn (idempotency).<br>Để tạo các chiến dịch có cùng tên, gửi hai yêu cầu có cùng `campaign_name` nhưng khác `request_id`.<br>Endpoint hỗ trợ tính lũy thừa (idempotency) để tránh gửi hai yêu cầu trùng lặp trong vòng 10 giây. Nếu bạn thử lại với cùng `request_id` trong 10 giây, chỉ một yêu cầu thành công.<br>Khác với `request_id` trả về trong phản hồi HTTP.<br>Giá trị phải là chuỗi biểu diễn số nguyên 64-bit. Ví dụ: `"123456789"`. |
| special_industries | string[] | Không bắt buộc | Danh mục quảng cáo đặc biệt.<br>Khi chọn danh mục nhà ở, việc làm hoặc tín dụng cho chiến dịch, bạn cam kết không sử dụng TikTok để phân biệt đối xử và tuân thủ [Chính sách danh mục quảng cáo đặc biệt của TikTok](https://ads.tiktok.com/help/article/housing-employment-credit-hec-ad-policy?redirected=2).<br>Khi bật trường này, các tùy chọn nhắm mục tiêu ở cấp nhóm quảng cáo sẽ bị giới hạn để tuân thủ luật chống phân biệt đối xử. Xem [Yêu cầu nhắm mục tiêu cho nhóm quảng cáo có danh mục đặc biệt](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1739381236849665).<br>Giá trị enum:<br>• `HOUSING`: Bất động sản, bảo hiểm nhà ở, thế chấp.<br>• `EMPLOYMENT`: Cơ hội việc làm, thực tập, chứng chỉ nghề.<br>• `CREDIT`: Thẻ tín dụng, vay mua ô tô, tài chính dài hạn.<br>**Lưu ý**:<br>• Khả dụng chung cho nhà quảng cáo đăng ký tại Mỹ hoặc Canada. Nhà quảng cáo ở nơi khác muốn nhắm mục tiêu tới các nước này với danh mục đặc biệt phải xin cấp quyền allowlist.<br>• Sau khi chọn danh mục đặc biệt cho chiến dịch, bạn có thể gỡ bỏ chúng, nhưng không thể thay đổi danh mục hoặc bật lại danh mục đặc biệt cho một chiến dịch hiện có nếu hiện tại chúng đang bị tắt. |
| budget_optimize_on | boolean | Không bắt buộc | Có bật Tối ưu hóa ngân sách chiến dịch (CBO) hay không.<br>Giá trị enum: `true` (bật). Chi tiết xem [Tối ưu hóa ngân sách chiến dịch (CBO)](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1739381757818881).<br>**Lưu ý**: CBO cho Video Shopping Ads với nguồn sản phẩm là Catalog hiện là tính năng cần allowlist. |
| budget_mode | string | Có điều kiện | Bắt buộc khi `objective_type` **KHÔNG PHẢI** là `RF_REACH`.<br>Khi `objective_type` là `RF_REACH`, `budget_mode` chỉ hỗ trợ `BUDGET_MODE_INFINITE`.<br>Chế độ ngân sách.<br>Khi bật CBO, `budget_mode` ở cấp chiến dịch hỗ trợ các giá trị enum sau:<br>• `BUDGET_MODE_TOTAL`: Ngân sách trọn đời.<br>• `BUDGET_MODE_DYNAMIC_DAILY_BUDGET`: Ngân sách hàng ngày động (trung bình theo tuần). Chi phí ngày không vượt quá 125% ngân sách trung bình ngày; chi phí tuần không vượt quá ngân sách trung bình ngày * 7. Khi `objective_type` là `TRAFFIC`, `APP_PROMOTION`, `WEB_CONVERSIONS`, `LEAD_GENERATION`, `PRODUCT_SALES` (chỉ Video Shopping Ads), `REACH`, `VIDEO_VIEWS`, hoặc `ENGAGEMENT`, và bạn muốn đặt ngân sách không trọn đời, hãy chọn chế độ này. (Lưu ý: chế độ này cho `REACH`, `VIDEO_VIEWS`, `ENGAGEMENT` hiện cần allowlist).<br>• `BUDGET_MODE_DAY`: Ngân sách hàng ngày cố định.<br>Khi tắt CBO, `budget_mode` hỗ trợ:<br>• `BUDGET_MODE_INFINITE`: Ngân sách không giới hạn.<br>• `BUDGET_MODE_TOTAL`: Ngân sách trọn đời.<br>• `BUDGET_MODE_DAY`: Ngân sách hàng ngày (đã ngừng hỗ trợ cho các mục tiêu `REACH`, `VIDEO_VIEWS`, `ENGAGEMENT` khi không dùng CBO).<br>Xem chi tiết tại [Ngân sách (Budget)](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1739381246298114). |
| budget | float | Có điều kiện | Bắt buộc khi `budget_mode` là `BUDGET_MODE_DAY`, `BUDGET_MODE_DYNAMIC_DAILY_BUDGET` hoặc `BUDGET_MODE_TOTAL`.<br>Ngân sách chiến dịch.<br>Để biết mức ngân sách tối thiểu và quy tắc thiết lập, xem [Ngân sách](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1739381246298114). Để tra cứu khoảng giá trị ngân sách theo loại tiền tệ, xem [Tiền tệ - Khoảng giá trị ngân sách hàng ngày](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1737585839634433). |
| rta_id | string | Không bắt buộc | Realtime API (RTA) ID, mã định danh chiến lược RTA.<br>Liên hệ đại diện TikTok để nhận danh sách RTA ID liên kết với tài khoản quảng cáo của bạn. Xem điều kiện tiên quyết tại [Realtime API](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1805437148769281).<br>**Lưu ý**: Kích hoạt RTA là tính năng cần danh sách cho phép (allowlist). |
| rta_bid_enabled | boolean | Không bắt buộc | Có sử dụng giá thầu RTA hay không.<br>Giá trị: `true` (bật), `false` (tắt). Mặc định: `false`.<br>Chỉ có thể đặt là `true` khi `objective_type` là `APP_PROMOTION`, `WEB_CONVERSIONS`, hoặc `PRODUCT_SALES` và đã truyền `rta_id`. Cần allowlist. |
| rta_product_selection_enabled | boolean | Không bắt buộc | Có sử dụng RTA để tự động chọn sản phẩm hay không.<br>Giá trị enum: `true`, `false`. Mặc định: `false`.<br>Chỉ có thể đặt là `true` khi `objective_type` là `PRODUCT_SALES`, `campaign_product_source` là `CATALOG`, và đã truyền `rta_id`. |
| operation_status | string | Không bắt buộc | Trạng thái chiến dịch khi tạo.<br>Giá trị enum:<br>• `ENABLE`: Chiến dịch được bật khi tạo.<br>• `DISABLE`: Chiến dịch bị tắt khi tạo.<br>Giá trị mặc định: `ENABLE`.<br>**Lưu ý**: Đối với chiến dịch Tiếp cận & Tần suất (Reach & Frequency), vui lòng chỉ định `ENABLE` hoặc không truyền. Không được đặt là `DISABLE`.<br>Sau khi tạo, nếu muốn đổi trạng thái, hãy dùng [/campaign/status/update/](24-campaign.md#doc-1739320994354178). |
| postback_window_mode | string | Không bắt buộc | Chỉ hợp lệ khi `campaign_type` là `IOS14_CAMPAIGN` và `operation_status` là `DISABLE`.<br>Chế độ xác định khung thời gian nhận postback SKAN 4.0 bạn muốn đảm bảo.<br>Giá trị enum:<br>• `POSTBACK_WINDOW_MODE1`: Đảm bảo postback đầu tiên (cửa sổ phân bổ 0–2 ngày, tối đa 4 ngày để trả về dữ liệu và giải phóng hạn mức).<br>• `POSTBACK_WINDOW_MODE2`: Đảm bảo hai postback đầu (cửa sổ 3–7 ngày, tối đa 13 ngày).<br>• `POSTBACK_WINDOW_MODE3`: Đảm bảo cả ba postback (cửa sổ 8–35 ngày, tối đa 41 ngày).<br>Xem thêm tại [Chiến dịch chuyên dụng](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1740029173531649).<br>**Lưu ý**:<br>• Ứng dụng phải được cấu hình MMP hỗ trợ SKAN 4.0 trên Events Manager.<br>• Một khi đã đặt, trường này không thể cập nhật.<br>• Nếu `operation_status` là `ENABLE` hoặc không truyền, trường này sẽ bị bỏ qua.<br>• Nếu truyền trường này khi chưa bật SKAN 4.0 cho ứng dụng, lỗi sẽ xảy ra.<br>• Nếu không truyền khi `campaign_type` là `IOS14_CAMPAIGN`, `operation_status` là `DISABLE` và đã bật SKAN 4.0, trường này mặc định là `POSTBACK_WINDOW_MODE1`.<br>• Đảm bảo nhóm quảng cáo nhắm mục tiêu thiết bị chạy iOS 16.1 trở lên (`min_ios_version` đặt là `16.1`). |
| po_number | string | Không bắt buộc | Mã đơn đặt hàng (PO number). Dùng để theo dõi hóa đơn và đối soát thanh toán.<br>Xem thêm [Cập nhật mã PO trên hóa đơn](https://ads.tiktok.com/help/article/update-po-number-on-monthly-invoices). |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi. Xem [Phụ lục - Mã trả về](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. |
| request_id | string | ID log của yêu cầu. |
| data | object | Dữ liệu chiến dịch đã tạo. |
| ↳ advertiser_id | string | ID của nhà quảng cáo. |
| ↳ campaign_id | string | ID của chiến dịch vừa được tạo. |
| ↳ create_time | string | Thời gian tạo chiến dịch. |
| ↳ modify_time | string | Thời gian sửa đổi chiến dịch gần nhất. |
| ↳ objective_type | string | Mục tiêu quảng cáo. Xem [Enum - Mục tiêu quảng cáo](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ app_promotion_type | string | Loại quảng bá ứng dụng: `APP_INSTALL`, `APP_RETARGETING`, `APP_PREREGISTRATION`. |
| ↳ virtual_objective_type | string | Loại mục tiêu ảo: `SALES`. |
| ↳ sales_destination | string | Đích bán hàng: `TIKTOK_SHOP`, `WEBSITE`, `APP`, `WEB_AND_APP`. |
| ↳ is_search_campaign | boolean | Chiến dịch quảng cáo tìm kiếm hay không. |
| ↳ is_smart_performance_campaign | boolean | Chiến dịch có thuộc loại tự động hay không. |
| ↳ campaign_type | string | Loại chiến dịch: `REGULAR_CAMPAIGN`, `IOS14_CAMPAIGN`. |
| ↳ app_id | string | ID ứng dụng được quảng bá. |
| ↳ is_advanced_dedicated_campaign | boolean | Chiến dịch chuyên dụng nâng cao hay không. |
| ↳ disable_skan_campaign | boolean | Tắt phân bổ SKAN hay không. |
| ↳ bid_align_type | string | Loại phân bổ cho Chiến dịch chuyên dụng: `SAN`, `SKAN`. |
| ↳ campaign_app_profile_page_state | string | Trạng thái Trang hồ sơ ứng dụng: `INVALID`, `UNSET`, `ON`, `OFF`. |
| ↳ rf_campaign_type | string | Loại chiến dịch Đặt trước: `STANDARD`, `PULSE`. |
| ↳ campaign_product_source | string | Nguồn sản phẩm: `CATALOG`, `STORE`. |
| ↳ catalog_enabled | boolean | Sử dụng danh mục sản phẩm hay không. |
| ↳ campaign_name | string | Tên chiến dịch. |
| ↳ special_industries | string[] | Danh mục quảng cáo đặc biệt: `HOUSING`, `EMPLOYMENT`, `CREDIT`. |
| ↳ budget_optimize_on | boolean | Có bật Tối ưu hóa ngân sách chiến dịch (CBO) hay không. |
| ↳ bid_type | string | Chiến lược giá thầu cấp chiến dịch. |
| ↳ deep_bid_type | string | Chiến lược giá thầu cho sự kiện chuyên sâu trong ứng dụng. Xem [Enum - Chiến lược giá thầu chuyên sâu](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1739381757818881). |
| ↳ roas_bid | float | Mục tiêu ROAS cho Tối ưu hóa giá trị. |
| ↳ optimization_goal | string | Mục tiêu tối ưu hóa. |
| ↳ budget_mode | string | Chế độ ngân sách: `BUDGET_MODE_INFINITE`, `BUDGET_MODE_TOTAL`, `BUDGET_MODE_DAY`, `BUDGET_MODE_DYNAMIC_DAILY_BUDGET`. |
| ↳ budget | float | Ngân sách của chiến dịch. |
| ↳ rta_id | string | Realtime API ID. |
| ↳ rta_bid_enabled | boolean | Có bật giá thầu RTA hay không. |
| ↳ rta_product_selection_enabled | boolean | Có bật tự động chọn sản phẩm bằng RTA hay không. |
| ↳ operation_status | string | Trạng thái hoạt động: `ENABLE`, `DISABLE`. |
| ↳ secondary_status | string | Trạng thái phụ của chiến dịch. |
| ↳ postback_window_mode | string | Chế độ cửa sổ nhận postback SKAN 4.0: `POSTBACK_WINDOW_MODE1`, `POSTBACK_WINDOW_MODE2`, `POSTBACK_WINDOW_MODE3`. |
| ↳ is_new_structure | boolean | Có sử dụng cấu trúc mới hay không. |
| ↳ objective | string | Loại mục tiêu chiến dịch: `APP`, `LANDING_PAGE`. |
| ↳ po_number | string | Mã đơn đặt hàng (Purchase Order number). |

### Ví dụ

#### Gọi API bằng curl

```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/campaign/create/' \
  --header 'Access-Token: YOUR_ACCESS_TOKEN' \
  --header 'Content-Type: application/json' \
  --data '{
    "advertiser_id": "7123456789012345678",
    "objective_type": "TRAFFIC",
    "campaign_name": "Summer_Promotion_Traffic_2023",
    "budget_mode": "BUDGET_MODE_TOTAL",
    "budget": 500.0,
    "operation_status": "ENABLE"
}'
```

#### Gọi API bằng Python

```python
import requests

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ADVERTISER_ID = "7123456789012345678"

url = "https://business-api.tiktok.com/open_api/v1.3/campaign/create/"
headers = {
    "Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}
payload = {
    "advertiser_id": ADVERTISER_ID,
    "objective_type": "TRAFFIC",
    "campaign_name": "Summer_Promotion_Traffic_2023",
    "budget_mode": "BUDGET_MODE_TOTAL",
    "budget": 500.0,
    "operation_status": "ENABLE"
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
  "request_id": "2023052210032301011023224213552",
  "data": {
    "operation_status": "ENABLE",
    "modify_time": "2023-05-22 10:05:00",
    "create_time": "2023-05-22 10:05:00",
    "campaign_id": "1765432109876545",
    "roas_bid": 0,
    "campaign_name": "Summer_Promotion_Traffic_2023",
    "campaign_type": "REGULAR_CAMPAIGN",
    "is_new_structure": true,
    "advertiser_id": "7123456789012345678",
    "is_smart_performance_campaign": false,
    "objective": "LANDING_PAGE",
    "secondary_status": "CAMPAIGN_STATUS_ENABLE",
    "budget_mode": "BUDGET_MODE_TOTAL",
    "budget": 500.0,
    "objective_type": "TRAFFIC",
    "deep_bid_type": null
  }
}
```


---

## Cập nhật chiến dịch (`Update a campaign`)
<a id="doc-1739320422086657"></a>
<!-- doc_id: 1739320422086657 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/campaign/update/`

**Mục đích**: Sử dụng endpoint này để chỉnh sửa thông tin của chiến dịch sau khi đã được tạo (ví dụ: tên chiến dịch, ngân sách, danh mục ngành nghề đặc biệt hoặc mã đơn đặt hàng PO).

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Access token (mã truy cập) đã được ủy quyền. Chi tiết xem [Xác thực](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type | string | Bắt buộc | Định dạng nội dung yêu cầu. Giá trị hợp lệ: `application/json`. |

### Tham số (JSON Body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| advertiser_id | string | Bắt buộc | ID của nhà quảng cáo / tài khoản quảng cáo. |
| campaign_id | string | Bắt buộc | ID của chiến dịch cần cập nhật. |
| campaign_name | string | Không bắt buộc | Tên mới cho chiến dịch.<br>Giới hạn độ dài: tối đa 512 ký tự. Không hỗ trợ emoji.<br>Mỗi ký tự tiếng Trung hoặc tiếng Nhật tính là 2 ký tự, mỗi chữ cái tiếng Anh tính là 1 ký tự. |
| special_industries | string[] | Không bắt buộc | Danh mục quảng cáo đặc biệt.<br>Bằng việc chọn danh mục nhà ở, việc làm hoặc tín dụng cho chiến dịch, bạn cam kết không sử dụng TikTok để phân biệt đối xử và tuân thủ [Chính sách danh mục quảng cáo đặc biệt của TikTok](https://ads.tiktok.com/help/article/housing-employment-credit-hec-ad-policy?redirected=2).<br>Khi sử dụng trường này, các tùy chọn nhắm mục tiêu ở cấp nhóm quảng cáo sẽ bị hạn chế theo luật hiện hành. Xem chi tiết tại [Yêu cầu nhắm mục tiêu cho nhóm quảng cáo có danh mục đặc biệt](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1739381236849665).<br>Giá trị enum:<br>• `HOUSING`: Bất động sản, bảo hiểm nhà ở, vay thế chấp.<br>• `EMPLOYMENT`: Tuyển dụng, thực tập, chương trình cấp chứng chỉ.<br>• `CREDIT`: Thẻ tín dụng, vay mua xe, tài chính dài hạn.<br>**Lưu ý**:<br>• Dùng danh mục đặc biệt cho Shopping Ads nguồn Danh mục và ngoài Danh mục hiện là các tính năng cần allowlist riêng.<br>• Khả dụng chung cho nhà quảng cáo tại Mỹ hoặc Canada. Nhà quảng cáo ngoài hai quốc gia này muốn nhắm mục tiêu tới Mỹ/Canada với danh mục đặc biệt cần gửi yêu cầu phê duyệt allowlist.<br>• Nếu trước đó đã chọn danh mục đặc biệt, bạn có thể gỡ bỏ chúng, nhưng không thể thay đổi danh mục hoặc bật lại danh mục đặc biệt cho chiến dịch nếu hiện tại chúng đang bị tắt. |
| budget | float | Không bắt buộc | Ngân sách mới của chiến dịch.<br>Để biết mức ngân sách tối thiểu và quy tắc thiết lập chế độ ngân sách, xem [Ngân sách (Budget)](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1739381246298114). Để tra cứu khoảng giá trị ngân sách theo loại tiền tệ, xem [Tiền tệ - Khoảng giá trị ngân sách hàng ngày](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1737585839634433).<br>**Lưu ý**: Mức ngân sách mới phải tối thiểu bằng 105% số tiền đã chi tiêu hiện tại. Bạn có thể chạy [báo cáo đồng bộ](58-reporting.md#doc-1740302848100353) hoặc [báo cáo bất đồng bộ](58-reporting.md#doc-1740302766489602) để lấy dữ liệu chi tiêu thông qua chỉ số dữ liệu cơ bản `spend`. |
| po_number | string | Không bắt buộc | Mã đơn đặt hàng (Purchase Order - PO number). Hữu ích cho việc theo dõi hóa đơn và đối soát thanh toán.<br>Xem thêm tại [Cập nhật mã PO trên hóa đơn hàng tháng](https://ads.tiktok.com/help/article/update-po-number-on-monthly-invoices). |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi. Xem [Phụ lục - Mã trả về](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. |
| request_id | string | ID log của yêu cầu. |
| data | object | Dữ liệu chiến dịch sau khi cập nhật. |
| ↳ advertiser_id | string | ID của nhà quảng cáo. |
| ↳ campaign_id | string | ID của chiến dịch. |
| ↳ create_time | string | Thời gian tạo chiến dịch. |
| ↳ modify_time | string | Thời gian sửa đổi chiến dịch vừa thực hiện. |
| ↳ objective_type | string | Mục tiêu quảng cáo. Xem [Enum - Mục tiêu quảng cáo](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ app_promotion_type | string | Loại quảng bá ứng dụng: `APP_INSTALL`, `APP_RETARGETING`, `APP_PREREGISTRATION`, `APP_POSTS_PROMOTION`. |
| ↳ virtual_objective_type | string | Loại mục tiêu ảo: `SALES`. Xem thêm về [mục tiêu Bán hàng](https://business-api.tiktok.com/portal/docs?id=). |
| ↳ sales_destination | string | Đích bán hàng: `TIKTOK_SHOP`, `WEBSITE`, `APP`, `WEB_AND_APP`. |
| ↳ is_search_campaign | boolean | Chiến dịch quảng cáo tìm kiếm hay không. |
| ↳ is_smart_performance_campaign | boolean | Chiến dịch có thuộc loại tự động hay không (Smart+ hoặc Smart Performance Web Campaign). |
| ↳ campaign_type | string | Loại chiến dịch: `REGULAR_CAMPAIGN`, `IOS14_CAMPAIGN`. |
| ↳ app_id | string | ID ứng dụng được quảng bá. |
| ↳ is_advanced_dedicated_campaign | boolean | Chiến dịch chuyên dụng nâng cao hay không. |
| ↳ disable_skan_campaign | boolean | Tắt phân bổ SKAN hay không. |
| ↳ bid_align_type | string | Loại phân bổ cho Chiến dịch chuyên dụng: `SAN`, `SKAN`. |
| ↳ campaign_app_profile_page_state | string | Trạng thái Trang hồ sơ ứng dụng: `INVALID`, `UNSET`, `ON`, `OFF`. |
| ↳ rf_campaign_type | string | Loại chiến dịch Đặt trước: `STANDARD`, `PULSE`. |
| ↳ campaign_product_source | string | Nguồn sản phẩm: `CATALOG`, `STORE`. |
| ↳ catalog_enabled | boolean | Có sử dụng danh mục sản phẩm hay không. |
| ↳ campaign_name | string | Tên chiến dịch sau cập nhật. |
| ↳ special_industries | string[] | Danh mục quảng cáo đặc biệt: `HOUSING`, `EMPLOYMENT`, `CREDIT`. |
| ↳ budget_optimize_on | boolean | Có bật Tối ưu hóa ngân sách chiến dịch (CBO) hay không. |
| ↳ bid_type | string | Chiến lược giá thầu cấp chiến dịch. |
| ↳ deep_bid_type | string | Chiến lược giá thầu sự kiện chuyên sâu trong ứng dụng. Xem [Enum - Chiến lược giá thầu chuyên sâu](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ roas_bid | float | Mục tiêu ROAS cho Tối ưu hóa giá trị. |
| ↳ optimization_goal | string | Mục tiêu tối ưu hóa. |
| ↳ budget_mode | string | Chế độ ngân sách: `BUDGET_MODE_INFINITE`, `BUDGET_MODE_TOTAL`, `BUDGET_MODE_DAY`, `BUDGET_MODE_DYNAMIC_DAILY_BUDGET`. |
| ↳ budget | float | Ngân sách chiến dịch sau khi cập nhật. |
| ↳ rta_id | string | Realtime API ID. |
| ↳ rta_bid_enabled | boolean | Có bật giá thầu RTA hay không. |
| ↳ rta_product_selection_enabled | boolean | Có bật tự động chọn sản phẩm bằng RTA hay không. |
| ↳ operation_status | string | Trạng thái hoạt động: `ENABLE`, `DISABLE`. |
| ↳ secondary_status | string | Trạng thái phụ của chiến dịch. |
| ↳ postback_window_mode | string | Chế độ cửa sổ nhận postback SKAN 4.0: `POSTBACK_WINDOW_MODE1`, `POSTBACK_WINDOW_MODE2`, `POSTBACK_WINDOW_MODE3`. |
| ↳ is_new_structure | bool | Chiến dịch có sử dụng cấu trúc mới hay không. |
| ↳ objective | string | Loại chiến dịch: `APP`, `LANDING_PAGE`. |
| ↳ po_number | string | Mã đơn đặt hàng (PO number). |

### Ví dụ

#### Gọi API bằng curl

```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/campaign/update/' \
  --header 'Access-Token: YOUR_ACCESS_TOKEN' \
  --header 'Content-Type: application/json' \
  --data '{
    "advertiser_id": "7123456789012345678",
    "campaign_id": "1765432109876545",
    "campaign_name": "Summer_Promotion_Updated_2023",
    "budget": 600.0
}'
```

#### Gọi API bằng Python

```python
import requests

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ADVERTISER_ID = "7123456789012345678"
CAMPAIGN_ID = "1765432109876545"

url = "https://business-api.tiktok.com/open_api/v1.3/campaign/update/"
headers = {
    "Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}
payload = {
    "advertiser_id": ADVERTISER_ID,
    "campaign_id": CAMPAIGN_ID,
    "campaign_name": "Summer_Promotion_Updated_2023",
    "budget": 600.0
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
  "request_id": "2023052210032301011023224213553",
  "data": {
    "is_new_structure": true,
    "secondary_status": "CAMPAIGN_STATUS_ENABLE",
    "campaign_type": "REGULAR_CAMPAIGN",
    "budget": 600.0,
    "budget_mode": "BUDGET_MODE_TOTAL",
    "special_industries": [],
    "deep_bid_type": null,
    "advertiser_id": "7123456789012345678",
    "objective_type": "TRAFFIC",
    "create_time": "2023-05-22 10:05:00",
    "operation_status": "ENABLE",
    "is_smart_performance_campaign": false,
    "campaign_id": "1765432109876545",
    "roas_bid": 0,
    "campaign_name": "Summer_Promotion_Updated_2023",
    "objective": "LANDING_PAGE",
    "rf_campaign_type": "STANDARD",
    "modify_time": "2023-05-22 11:20:00"
  }
}
```

---

## Cập nhật trạng thái hoạt động của chiến dịch (`Update the operation statuses of campaigns`)
<a id="doc-1739320994354178"></a>
<!-- doc_id: 1739320994354178 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/campaign/status/update/`

**Mục đích**: Sử dụng endpoint này để bật (enable), tắt (disable/pause) hoặc xóa (delete) một hoặc nhiều chiến dịch cùng lúc.

> [!NOTE]
> Không thể sửa đổi trạng thái hoạt động của chiến dịch đã bị xóa. Bạn có thể sử dụng endpoint [/campaign/get/](24-campaign.md#doc-1739315828649986) để kiểm tra trạng thái hoạt động hiện tại của chiến dịch qua trường `operation_status`.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Access token (mã truy cập) đã được ủy quyền. Chi tiết xem [Xác thực](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type | string | Bắt buộc | Định dạng nội dung yêu cầu. Giá trị hợp lệ: `application/json`. |

### Tham số (JSON Body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| advertiser_id | string | Bắt buộc | ID của nhà quảng cáo / tài khoản quảng cáo. |
| campaign_ids | string[] | Bắt buộc | Danh sách các ID chiến dịch cần cập nhật trạng thái. Số lượng cho phép: từ 1 đến 20 ID. |
| operation_status | string | Bắt buộc | Thao tác trạng thái thực hiện.<br>Giá trị enum:<br>• `ENABLE`: Bật chiến dịch.<br>• `DISABLE`: Tạm dừng / tắt chiến dịch.<br>• `DELETE`: Xóa chiến dịch.<br>**Lưu ý**: Trạng thái của chiến dịch đã xóa không thể sửa đổi lại. |
| postback_window_mode | string | Không bắt buộc | Chỉ hợp lệ khi đáp ứng đồng thời tất cả các điều kiện sau:<br>• Các chiến dịch (`campaign_ids`) là Chiến dịch chuyên dụng (`campaign_type` là `IOS14_CAMPAIGN`).<br>• Bạn chỉ định `operation_status` là `DISABLE` trong yêu cầu.<br>• `postback_window_mode` chưa từng được cấu hình cho chiến dịch trước đó.<br>• Bạn đã kích hoạt SKAN 4.0 cho ứng dụng của mình.<br>Chế độ xác định khung thời gian nhận postback SKAN 4.0 bạn muốn đảm bảo. Khung thời gian càng dài thì dữ liệu nhận về càng lâu và thời gian giải phóng hạn mức chiến dịch càng chậm.<br>Giá trị enum:<br>• `POSTBACK_WINDOW_MODE1`: Đảm bảo postback đầu tiên (cửa sổ phân bổ 0–2 ngày; dữ liệu mất tối đa 4 ngày để trả về và giải phóng hạn mức).<br>• `POSTBACK_WINDOW_MODE2`: Đảm bảo hai postback đầu (cửa sổ 3–7 ngày; mất tối đa 13 ngày).<br>• `POSTBACK_WINDOW_MODE3`: Đảm bảo cả ba postback (cửa sổ 8–35 ngày; mất tối đa 41 ngày).<br>Xem thêm tại [Chiến dịch chuyên dụng](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1740029173531649).<br>**Lưu ý**:<br>• Cần tích hợp MMP tương thích SKAN 4.0 (Adjust, Airbridge, Appsflyer, Branch, Kochava, Singular) và chuyển đổi sang SKAN 4.0 trên Events Manager.<br>• Một khi đã thiết lập, trường này không thể sửa đổi.<br>• Nếu truyền trường này khi `operation_status` là `ENABLE` hoặc không truyền, lỗi sẽ phát sinh.<br>• Nếu truyền trường này khi chưa bật SKAN 4.0 cho ứng dụng (`app_id`), lỗi sẽ phát sinh.<br>• Nếu không truyền trường này khi `campaign_type` là `IOS14_CAMPAIGN`, `operation_status` là `DISABLE` và đã bật SKAN 4.0, trường này mặc định là `POSTBACK_WINDOW_MODE1`.<br>• Thao tác cấu hình postback window mode có thể thành công một phần. Nếu bạn truyền `campaign_ids` gồm cả chiến dịch không phải chuyên dụng hoặc chiến dịch chuyên dụng đã cấu hình `postback_window_mode`, các chiến dịch đó sẽ bị bỏ qua và không đổi `postback_window_mode`. Chỉ những chiến dịch chuyên dụng thỏa mãn điều kiện mới được áp dụng.<br>• Đảm bảo nhóm quảng cáo nhắm tới iOS 16.1+ (`min_ios_version` đặt là `16.1`) để nhận postback SKAN 4.0. |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi. Xem [Phụ lục - Mã trả về](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. |
| data | object | Dữ liệu phản hồi chi tiết. |
| ↳ campaign_ids | string[] | Danh sách các ID chiến dịch đã được chỉnh sửa trạng thái. |
| ↳ status | string | Thao tác đã thực hiện. Giá trị: `DELETE`, `DISABLE`, `ENABLE`. |
| ↳ campaign_list | object[] | Thông tin chi tiết về danh sách chiến dịch đã chỉ định. |
| ↳↳ campaign_id | string | ID của chiến dịch. |
| ↳↳ status | string | Trạng thái hiện tại của chiến dịch (`campaign_id`).<br>Giá trị enum: `DELETE` (đã xóa), `DISABLE` (đã tạm dừng), `ENABLE` (đang bật). |
| ↳↳ postback_window_mode | string | Chế độ xác định khung thời gian nhận postback SKAN 4.0.<br>Giá trị enum: `POSTBACK_WINDOW_MODE1`, `POSTBACK_WINDOW_MODE2`, `POSTBACK_WINDOW_MODE3`. |
| request_id | string | ID log của yêu cầu. |

### Ví dụ

#### Gọi API bằng curl

```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/campaign/status/update/' \
  --header 'Access-Token: YOUR_ACCESS_TOKEN' \
  --header 'Content-Type: application/json' \
  --data '{
    "advertiser_id": "7123456789012345678",
    "campaign_ids": [
        "1765432109876545",
        "1765432109876546"
    ],
    "operation_status": "ENABLE"
}'
```

#### Gọi API bằng Python

```python
import requests

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ADVERTISER_ID = "7123456789012345678"

url = "https://business-api.tiktok.com/open_api/v1.3/campaign/status/update/"
headers = {
    "Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}
payload = {
    "advertiser_id": ADVERTISER_ID,
    "campaign_ids": ["1765432109876545", "1765432109876546"],
    "operation_status": "ENABLE"
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
  "request_id": "2023052210032301011023224213554",
  "data": {
    "status": "ENABLE",
    "campaign_ids": [
      "1765432109876545",
      "1765432109876546"
    ],
    "campaign_list": [
      {
        "campaign_id": "1765432109876545",
        "status": "ENABLE",
        "postback_window_mode": null
      },
      {
        "campaign_id": "1765432109876546",
        "status": "ENABLE",
        "postback_window_mode": null
      }
    ]
  }
}
```


---

## Lấy hạn mức Chiến dịch chuyên dụng SKAN theo mạng quảng cáo (`Get the quota for a SKAN Dedicated Campaign per ad network`)
<a id="doc-1752256376677378"></a>
<!-- doc_id: 1752256376677378 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/campaign/quota/info/`

**Mục đích**: Sử dụng endpoint này để lấy thông tin hạn mức Chiến dịch chuyên dụng SKAN theo từng mạng quảng cáo, hạn mức nhóm quảng cáo thuộc chiến dịch, và hạn mức quảng cáo của một nhóm quảng cáo trong Chiến dịch chuyên dụng SKAN 4.0.

Một ứng dụng iOS có thể có tối đa 15 hoặc 25 (chỉ dành cho danh sách cho phép - allowlist) Chiến dịch chuyên dụng SKAN đang hoạt động trên mỗi mạng quảng cáo và tối đa 5 nhóm quảng cáo đang hoạt động trong mỗi Chiến dịch chuyên dụng SKAN.

Để tìm hiểu thêm về các quy tắc hạn mức Chiến dịch chuyên dụng SKAN và các mạng quảng cáo, xem [Giới hạn hạn mức Chiến dịch chuyên dụng (Dedicated Campaign quota limits)](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1752256248260610).

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Access token (mã truy cập) đã được ủy quyền. Chi tiết xem [Xác thực](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (Query Parameters)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| advertiser_id | string | Bắt buộc | ID của nhà quảng cáo / tài khoản quảng cáo. |
| app_id | string | Bắt buộc | ID ứng dụng của ứng dụng được quảng bá. Bạn có thể lấy `app_id` bằng cách sử dụng endpoint [/app/list/](43-events-1-0-p1.md#doc-1740859313270786). |
| campaign_id | string | Không bắt buộc | ID của Chiến dịch chuyên dụng SKAN.<br>Chỉ định trường này nếu bạn muốn lấy thông tin hạn mức nhóm quảng cáo (`adgroup_quota_info`) cho một chiến dịch cụ thể.<br>**Lưu ý**: Nếu ID không phải là ID của một Chiến dịch chuyên dụng SKAN, lỗi sẽ phát sinh. Để xác định chiến dịch chuyên dụng có phải là Chiến dịch chuyên dụng SKAN hay không, hãy gọi [/campaign/get/](24-campaign.md#doc-1739315828649986) và kiểm tra xem giá trị `disable_skan_campaign` trả về có phải là `false` hay không. |
| adgroup_id | string | Không bắt buộc | ID của một nhóm quảng cáo thuộc Chiến dịch chuyên dụng SKAN 4.0. Chỉ định trường này nếu bạn muốn lấy thông tin hạn mức quảng cáo (`ad_quota_info`) cho một nhóm cụ thể.<br>**Lưu ý**: Nếu ID không thuộc nhóm quảng cáo của Chiến dịch chuyên dụng SKAN 4.0, giá trị của `ad_quota_info` trả về sẽ là null. |
| has_advertiser_quota | boolean | Không bắt buộc | Có trả về thông tin hạn mức theo từng ID nhà quảng cáo thuộc ứng dụng được quảng bá hay không.<br>Đặt thành `true` nếu bạn muốn lấy hạn mức chiến dịch chia theo các ID nhà quảng cáo khác nhau.<br>Giá trị mặc định: `false`. |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi. Xem chi tiết tại [Phụ lục - Mã trả về](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. Xem chi tiết tại [Phụ lục - Mã trả về](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| data | object | Dữ liệu hạn mức được trả về. |
| ↳ split_test_quota | object | Thông tin hạn mức thử nghiệm phân tách (split test). |
| ↳↳ max_test_number | number | Số nhóm thử nghiệm tối đa trong một thử nghiệm phân tách. Giá trị của trường này là `2`. |
| ↳↳ available_test_group | number | Số lượng nhóm thử nghiệm phân tách bạn có thể khởi chạy ngay bây giờ trong ứng dụng này. |
| ↳↳ used_test_group | number | Số lượng nhóm thử nghiệm phân tách đã được khởi chạy. |
| ↳↳ releasing_test_group | number | Số lượng nhóm thử nghiệm phân tách đang chờ giải phóng hạn mức. |
| ↳↳ used_quota | number | Số lượng hạn mức đã được sử dụng (khởi chạy). |
| ↳↳ releasing_quota | number | Số lượng hạn mức đang chờ giải phóng. |
| ↳ campaign_quota_info | object | Thông tin hạn mức chiến dịch. |
| ↳↳ tiktok_campaign_quota_info | object | Hạn mức chiến dịch thuộc mạng TikTok. Các vị trí vị trí phân phối (placements) thuộc mạng TikTok gồm `PLACEMENT_TIKTOK` và `PLACEMENT_GLOBAL_APP_BUNDLE`. |
| ↳↳↳ total_campaign_quota_info | object | Tổng hạn mức chiến dịch theo App ID. |
| ↳↳↳↳ total_campaign_quota | number | Tổng hạn mức Chiến dịch chuyên dụng đang hoạt động. Giá trị của trường này sẽ là `15` hoặc `25`.<br>**Lưu ý**: Mở rộng hạn mức lên 25 chiến dịch chuyên dụng đang hoạt động cho mỗi mạng quảng cáo của ứng dụng iOS là tính năng chỉ dành cho danh sách cho phép (allowlist). |
| ↳↳↳↳ used_campaign_quota | number | Số lượng Chiến dịch chuyên dụng đã khởi chạy. |
| ↳↳↳↳ releasing_campaign_quota | number | Số lượng Chiến dịch chuyên dụng đang chờ giải phóng hạn mức. |
| ↳↳↳↳ available_campaign_quota | number | Số lượng Chiến dịch chuyên dụng bạn có thể khởi chạy lúc này. |
| ↳↳↳↳ used_campaign_ids | string[] | Danh sách ID của các Chiến dịch chuyên dụng đã khởi chạy. |
| ↳↳↳↳ releasing_campaign_ids | string[] | Danh sách ID của các Chiến dịch chuyên dụng đang chờ giải phóng hạn mức. |
| ↳↳↳ campaign_quota_by_adv | object[] | Hạn mức chiến dịch theo từng ID nhà quảng cáo. |
| ↳↳↳↳ used_campaign_quota | number | Số lượng Chiến dịch chuyên dụng đã khởi chạy của nhà quảng cáo này. |
| ↳↳↳↳ releasing_campaign_quota | number | Số lượng Chiến dịch chuyên dụng đang chờ giải phóng của nhà quảng cáo này. |
| ↳↳↳↳ advertiser_id | string | ID của nhà quảng cáo. |
| ↳↳ pangle_campaign_quota_info | object | Hạn mức chiến dịch thuộc mạng Pangle. Vị trí phân phối khả dụng cho mạng Pangle là `PLACEMENT_PANGLE`. |
| ↳↳↳ total_campaign_quota_info | object | Tổng hạn mức chiến dịch theo App ID trên mạng Pangle. |
| ↳↳↳↳ total_campaign_quota | number | Tổng hạn mức Chiến dịch chuyên dụng đang hoạt động (`15` hoặc `25`). |
| ↳↳↳↳ used_campaign_quota | number | Số lượng Chiến dịch chuyên dụng đã khởi chạy trên Pangle. |
| ↳↳↳↳ releasing_campaign_quota | number | Số lượng Chiến dịch chuyên dụng đang chờ giải phóng trên Pangle. |
| ↳↳↳↳ available_campaign_quota | number | Số lượng Chiến dịch chuyên dụng có thể khởi chạy trên Pangle. |
| ↳↳↳↳ used_campaign_ids | string[] | Danh sách ID các Chiến dịch chuyên dụng đã khởi chạy trên Pangle. |
| ↳↳↳↳ releasing_campaign_ids | string[] | Danh sách ID các Chiến dịch chuyên dụng đang chờ giải phóng trên Pangle. |
| ↳↳↳ campaign_quota_by_adv | object[] | Hạn mức chiến dịch theo từng ID nhà quảng cáo trên mạng Pangle. |
| ↳↳↳↳ used_campaign_quota | number | Số lượng Chiến dịch chuyên dụng đã khởi chạy của nhà quảng cáo trên Pangle. |
| ↳↳↳↳ releasing_campaign_quota | number | Số lượng Chiến dịch chuyên dụng đang chờ giải phóng của nhà quảng cáo trên Pangle. |
| ↳↳↳↳ advertiser_id | string | ID của nhà quảng cáo. |
| ↳ adgroup_quota_info | object | Hạn mức nhóm quảng cáo thuộc Chiến dịch chuyên dụng. |
| ↳↳ total_adgroup_quota | number | Hạn mức nhóm quảng cáo đang hoạt động. Giá trị trường này là `5`. |
| ↳↳ used_adgroup_quota | number | Số lượng nhóm quảng cáo đã khởi chạy. |
| ↳↳ available_adgroup_quota | number | Số lượng nhóm quảng cáo bạn có thể khởi chạy lúc này. |
| ↳↳ placements | string[] | Các vị trí phân phối được phép cho nhóm quảng cáo. Bạn không thể tạo nhóm quảng cáo với vị trí phân phối không nằm trong danh sách này. |
| ↳↳ campaign_id | string | ID của chiến dịch. |
| ↳ ad_quota_info | object | Hạn mức quảng cáo trong một nhóm quảng cáo thuộc Chiến dịch chuyên dụng SKAN 4.0.<br>**Lưu ý**:<br>• Nếu nhóm quảng cáo chỉ định (`adgroup_id`) không thuộc Chiến dịch chuyên dụng SKAN 4.0, giá trị của trường này sẽ là null.<br>• Nếu bạn cung cấp SKAN 4.0 App ID (`app_id`) mà không chỉ định `campaign_id` và `adgroup_id` trong yêu cầu, trường này sẽ thể hiện hạn mức quảng cáo mặc định cho một Chiến dịch chuyên dụng SKAN 4.0 thông thường (không bật Smart+, ACO hay Smart Creative). Ví dụ: `{"available_ad_quota": 9, "total_ad_quota": 9, "adgroup_id": "0", "used_ad_quota": 0}`. |
| ↳↳ total_ad_quota | number | Hạn mức quảng cáo đang hoạt động. Đối với nhóm quảng cáo trong Chiến dịch chuyên dụng SKAN 4.0 thông thường, giá trị này là `9`. |
| ↳↳ used_ad_quota | number | Số lượng quảng cáo đã khởi chạy. |
| ↳↳ available_ad_quota | number | Số lượng quảng cáo bạn có thể khởi chạy lúc này. |
| ↳↳ adgroup_id | string | ID nhóm quảng cáo. |
| request_id | string | ID log của yêu cầu. |

### Ví dụ

#### 1. Truy vấn hạn mức Chiến dịch chuyên dụng cho ứng dụng iOS

```bash
curl -G --location "https://business-api.tiktok.com/open_api/v1.3/campaign/quota/info/" \
  --header "Access-Token: YOUR_ACCESS_TOKEN" \
  --data-urlencode "advertiser_id=7123456789012345678" \
  --data-urlencode "app_id=1234567890"
```

#### 2. Truy vấn hạn mức nhóm quảng cáo trong Chiến dịch chuyên dụng

```bash
curl -G --location "https://business-api.tiktok.com/open_api/v1.3/campaign/quota/info/" \
  --header "Access-Token: YOUR_ACCESS_TOKEN" \
  --data-urlencode "advertiser_id=7123456789012345678" \
  --data-urlencode "app_id=1234567890" \
  --data-urlencode "campaign_id=1765432109876545"
```

#### 3. Truy vấn hạn mức quảng cáo trong nhóm quảng cáo SKAN 4.0

```bash
curl -G --location "https://business-api.tiktok.com/open_api/v1.3/campaign/quota/info/" \
  --header "Access-Token: YOUR_ACCESS_TOKEN" \
  --data-urlencode "advertiser_id=7123456789012345678" \
  --data-urlencode "app_id=1234567890" \
  --data-urlencode "adgroup_id=1765432109876599"
```

#### Gọi API bằng Python

```python
import requests

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ADVERTISER_ID = "7123456789012345678"
APP_ID = "1234567890"

url = "https://business-api.tiktok.com/open_api/v1.3/campaign/quota/info/"
headers = {
    "Access-Token": ACCESS_TOKEN
}
params = {
    "advertiser_id": ADVERTISER_ID,
    "app_id": APP_ID,
    "has_advertiser_quota": False
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
  "request_id": "2023052210032301011023224213555",
  "data": {
    "ad_quota_info": {
      "available_ad_quota": 9,
      "total_ad_quota": 9,
      "adgroup_id": "0",
      "used_ad_quota": 0
    },
    "adgroup_quota_info": {
      "campaign_id": "0",
      "used_adgroup_quota": 0,
      "placements": [
        "PLACEMENT_PANGLE",
        "PLACEMENT_GLOBAL_APP_BUNDLE",
        "PLACEMENT_TIKTOK"
      ],
      "total_adgroup_quota": 5,
      "available_adgroup_quota": 5
    },
    "split_test_quota": {
      "max_test_number": 2,
      "used_test_group": 2,
      "releasing_test_group": 0,
      "used_quota": 4,
      "releasing_quota": 0,
      "available_test_group": 0
    },
    "campaign_quota_info": {
      "tiktok_campaign_quota_info": {
        "campaign_quota_by_adv": [],
        "total_campaign_quota_info": {
          "total_campaign_quota": 20,
          "releasing_campaign_quota": 4,
          "available_campaign_quota": 15,
          "used_campaign_quota": 1,
          "used_campaign_ids": ["1765432109876545"],
          "releasing_campaign_ids": ["1765432109876540"]
        }
      },
      "pangle_campaign_quota_info": {
        "campaign_quota_by_adv": [],
        "total_campaign_quota_info": {
          "total_campaign_quota": 20,
          "releasing_campaign_quota": 3,
          "available_campaign_quota": 12,
          "used_campaign_quota": 5,
          "used_campaign_ids": ["1765432109876541"],
          "releasing_campaign_ids": ["1765432109876542"]
        }
      }
    }
  }
}
```


---

## Tạo tác vụ sao chép bất đồng bộ cho Chiến dịch thủ công (`Create an asynchronous copy task for a Manual Campaign`)
<a id="doc-1788434394151938"></a>
<!-- doc_id: 1788434394151938 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/campaign/copy/task/create/`

**Mục đích**: Sử dụng endpoint này để tạo một tác vụ sao chép bất đồng bộ cho một Chiến dịch thủ công (Manual Campaign).

Bạn chỉ có thể sao chép một chiến dịch tại một thời điểm. Để tìm hiểu các bước chi tiết, xem [Sao chép Chiến dịch thủ công (Copy a Manual Campaign)](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1788434533212162). Sau khi tạo tác vụ, sử dụng endpoint [/campaign/copy/task/check/](24-campaign.md#doc-1788434463507458) để kiểm tra kết quả.

Để sao chép Chiến dịch Smart+ nâng cấp, vui lòng sử dụng [/smart_plus/campaign/copy/task/create/](62-upgraded-smartplus-p1.md#doc-1866528879472641).

> [!NOTE]
> • API sao chép chiến dịch bất đồng bộ hiện là tính năng chỉ dành cho danh sách cho phép (allowlist-only). Nếu bạn muốn truy cập, vui lòng liên hệ với đại diện TikTok của bạn.<br>• Giới hạn tốc độ gọi (rate limit) cho endpoint này là 1 truy vấn/giây (QPS) và 30 truy vấn/phút (QPM) cho mỗi ứng dụng nhà phát triển (developer app). [Giới hạn tốc độ toàn cầu](../04-get-started/bat-dau.md#doc-1740029171730433) không áp dụng cho endpoint này.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Access token (mã truy cập) đã được ủy quyền. Chi tiết xem [Xác thực](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type | string | Bắt buộc | Định dạng nội dung yêu cầu. Giá trị hợp lệ: `application/json`. |

### Tham số (JSON Body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| advertiser_id | string | Bắt buộc | ID của nhà quảng cáo / tài khoản quảng cáo. |
| campaign_id | string | Bắt buộc | ID của chiến dịch bạn muốn sao chép.<br>**Lưu ý**:<br>• Không thể sao chép Chiến dịch GMV Max hiện có chứa bài đăng tùy chỉnh của TikTok. Để kiểm tra, hãy dùng [/campaign/gmv_max/info/](45-gmv-max-p1.md#doc-1822000968821762) và xem `custom_anchor_video_list` có rỗng không.<br>• Không thể sao chép Chiến dịch chuyên dụng iOS có ứng dụng chưa kích hoạt mô-đun SAN trên MMP.<br>• Từ ngày 30/09/2024, không thể sao chép chiến dịch chứa [Quảng cáo có thể chơi (Playable Ads)](56-playable-ads.md#doc-1737730803189826) phân phối tới vị trí TikTok.<br>• Chỉ các chiến dịch có mục tiêu quảng cáo được hỗ trợ (`REACH`, `TRAFFIC`, `VIDEO_VIEWS`, `ENGAGEMENT`, `APP_PROMOTION`, `LEAD_GENERATION`, `WEB_CONVERSIONS`) mới có thể sao chép.<br>• Nhóm quảng cáo thuộc chiến dịch `ENGAGEMENT` có `promotion_type` là `LIVE_SHOPPING` hoặc `optimization_goal` là `PAGE_VISIT` không thể sao chép.<br>• Không hỗ trợ Smart+ Campaign và Upgraded Smart+ Campaign.<br>• Chiến dịch cần sao chép phải có ít nhất một nhóm quảng cáo chưa bị xóa chứa ít nhất một quảng cáo chưa bị xóa.<br>• Chiến dịch không được vượt quá giới hạn 20 nhóm quảng cáo chưa xóa, tối đa 50 quảng cáo chưa xóa mỗi nhóm.<br>• Không thể sao chép nhóm quảng cáo Tối ưu hóa sáng tạo tự động (ACO), nhưng có thể sao chép nhóm quảng cáo Smart Creative.<br>• Nếu sao chép chiến dịch chứa nhóm quảng cáo liên kết thử nghiệm phân tách (split test), chỉ có nhóm quảng cáo được sao chép; nhóm thử nghiệm phân tách sẽ không được tạo. |
| request_id | string | Bắt buộc | ID yêu cầu hỗ trợ tính lũy thừa (idempotency) để ngăn gửi trùng lặp trong 10 giây. Giá trị là chuỗi biểu diễn số nguyên 64-bit. Ví dụ: `"123456789"`. |
| operation_status | string | Không bắt buộc | Trạng thái của chiến dịch mới khi được tạo.<br>Giá trị enum: `ENABLE` (bật), `DISABLE` (tắt). Mặc định: `DISABLE`.<br>Để cập nhật trạng thái sau khi tạo, dùng [/campaign/status/update/](24-campaign.md#doc-1739320994354178). |
| virtual_objective_type | string | Không bắt buộc | Loại mục tiêu ảo mới: `SALES`. Xem thêm [mục tiêu Bán hàng](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1834189283112962). |
| sales_destination | string | Có điều kiện | Bắt buộc và chỉ hợp lệ khi `virtual_objective_type` được chỉ định.<br>Đích bán hàng: `TIKTOK_SHOP`, `WEBSITE`, `APP`. |
| campaign_name | string | Không bắt buộc | Tên của chiến dịch mới.<br>Giới hạn: tối đa 512 ký tự, không chứa emoji.<br>Nếu không chỉ định, mặc định sẽ là `"COPIED_{{name_of_the_original_campaign}}"`. Ví dụ chiến dịch gốc là `"FIRST_CAMPAIGN"`, tên mới sẽ là `"COPIED_FIRST_CAMPAIGN"`. |
| is_advanced_dedicated_campaign | boolean | Không bắt buộc | Có bật thiết lập Chiến dịch chuyên dụng nâng cao cho chiến dịch mới hay không.<br>Giá trị enum: `true`, `false`.<br>Nếu không truyền, chiến dịch mới kế thừa cài đặt từ chiến dịch gốc.<br>**Lưu ý**: Một khi đã thiết lập, không thể sửa đổi. |
| budget | number | Không bắt buộc | Ngân sách cho chiến dịch mới. Nếu không chỉ định, mặc định lấy theo ngân sách của chiến dịch gốc. |
| rta_id | string | Không bắt buộc | Realtime API ID. Cần được đưa vào danh sách cho phép (allowlist). Xem [Realtime API](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1805437148769281). |
| po_number | string | Không bắt buộc | Mã đơn đặt hàng (PO number). |
| schedule_type | string | Không bắt buộc | Loại lịch chạy cho tất cả các nhóm quảng cáo mới (chỉ truyền khi muốn áp dụng lịch chạy chung cho toàn bộ nhóm quảng cáo).<br>Giá trị enum:<br>• `SCHEDULE_START_END`: Đặt thời gian bắt đầu và kết thúc (cần truyền cả `schedule_start_time` và `schedule_end_time`).<br>• `SCHEDULE_FROM_NOW`: Đặt thời gian bắt đầu và chạy liên tục (chỉ truyền `schedule_start_time`, thời gian kết thúc tự động đặt là 10 năm sau). |
| schedule_start_time | string | Có điều kiện | Bắt buộc khi truyền `schedule_type`.<br>Thời gian bắt đầu lịch chạy (UTC+0), định dạng `"YYYY-MM-DD HH:MM:SS"`. Có thể sớm hơn hiện tại tối đa 12 giờ và không muộn hơn `"2028-01-01 00:00:00"`. |
| schedule_end_time | string | Có điều kiện | Bắt buộc khi `schedule_type` là `SCHEDULE_START_END`. Không hỗ trợ khi `schedule_type` là `SCHEDULE_FROM_NOW`.<br>Thời gian kết thúc lịch chạy (UTC+0), định dạng `"YYYY-MM-DD HH:MM:SS"`. Không muộn hơn `"2038-01-01 00:00:00"`. |
| deep_copy_mode | string | Không bắt buộc | Chế độ sao chép, xác định cách thức các nhóm quảng cáo và quảng cáo được tạo trong chiến dịch mới.<br>Giá trị enum:<br>• `DEFAULT`: Chế độ sao chép mặc định. Sao chép tất cả các nhóm quảng cáo và quảng cáo chưa bị xóa từ chiến dịch gốc. Trường `adgroup_list` sẽ bị bỏ qua.<br>• `CUSTOM`: Chế độ sao chép tùy chỉnh. Chỉ sao chép các nhóm quảng cáo và quảng cáo chưa bị xóa được chỉ định cụ thể qua trường `adgroup_list`. Tối đa 20 nhóm quảng cáo và 50 quảng cáo mỗi nhóm.<br>Giá trị mặc định: `DEFAULT`. |
| adgroup_list | object[] | Có điều kiện | Bắt buộc khi `deep_copy_mode` là `CUSTOM`. Bị bỏ qua khi `deep_copy_mode` là `DEFAULT`.<br>Cài đặt tùy chỉnh cho các nhóm quảng cáo trong chiến dịch mới. Tối đa 20 phần tử. |
| ↳ adgroup_id | string | Có điều kiện | Bắt buộc khi truyền `adgroup_list`. ID của nhóm quảng cáo gốc cần sao chép (thuộc `campaign_id` gốc). |
| ↳ operation_status | string | Không bắt buộc | Trạng thái nhóm quảng cáo mới khi tạo: `ENABLE` (mặc định), `DISABLE`. |
| ↳ adgroup_name | string | Không bắt buộc | Tên nhóm quảng cáo mới. Tối đa 512 ký tự. Mặc định lấy theo tên nhóm gốc. |
| ↳ automated_keywords_enabled | boolean | Không bắt buộc | Chỉ hợp lệ khi `is_search_campaign` là `true`. Có bật từ khóa tự động hay không: `true`, `false` (mặc định: `false`). Cần allowlist. |
| ↳ location_ids | string[] | Không bắt buộc | Danh sách ID vị trí nhắm mục tiêu mới. Tối đa 3.000 phần tử (tổng location ID + zipcode ID không vượt quá 3.000). Xem **Location IDs**. |
| ↳ zipcode_ids | string[] | Không bắt buộc | Mã bưu chính nhắm mục tiêu (hỗ trợ US, Canada, Brazil, Indonesia, Thái Lan, Việt Nam). Tối đa 3.000 phần tử. |
| ↳ audience_ids | string[] | Không bắt buộc | Danh sách ID tệp đối tượng nhắm mục tiêu. Xem [/dmp/custom_audience/list/](09-audience.md#doc-1739940506015746). |
| ↳ excluded_audience_ids | string[] | Không bắt buộc | Danh sách ID tệp đối tượng loại trừ. |
| ↳ age_groups | string[] | Không bắt buộc | Nhóm tuổi nhắm mục tiêu. Xem [Enum - Nhóm tuổi](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ budget | number | Không bắt buộc | Ngân sách cho nhóm quảng cáo mới. |
| ↳ schedule_type | string | Có điều kiện | Loại lịch chạy tùy chỉnh cho riêng nhóm quảng cáo này: `SCHEDULE_START_END`, `SCHEDULE_FROM_NOW`. |
| ↳ schedule_start_time | string | Có điều kiện | Thời gian bắt đầu lịch chạy cho nhóm quảng cáo này (`YYYY-MM-DD HH:MM:SS`, UTC+0). |
| ↳ schedule_end_time | string | Có điều kiện | Thời gian kết thúc lịch chạy cho nhóm quảng cáo này (`YYYY-MM-DD HH:MM:SS`, UTC+0). |
| ↳ ad_list | object[] | Có điều kiện | Cài đặt danh sách quảng cáo tùy chỉnh khi sao chép nhóm quảng cáo thông thường (không phải ACO/Smart Creative) ở chế độ `CUSTOM`. Tối đa 50 phần tử. |
| ↳↳ ad_id | string | Có điều kiện | Bắt buộc khi truyền `ad_list`. ID quảng cáo gốc cần sao chép. |
| ↳↳ operation_status | string | Không bắt buộc | Trạng thái quảng cáo mới: `ENABLE` (mặc định), `DISABLE`. |
| ↳↳ ad_name | string | Không bắt buộc | Tên quảng cáo mới. Giới hạn 512 ký tự. Mặc định là `"COPIED_{{name_of_the_original_ad}}_{{ID_of_the_original_ad}}"`. |
| ↳↳ identity_type | string | Không bắt buộc | Loại danh tính: `CUSTOMIZED_USER`, `AUTH_CODE`, `TT_USER`, `BC_AUTH_TT`. Xem [Danh tính (Identities)](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1738958351620097). |
| ↳↳ identity_id | string | Không bắt buộc | ID danh tính. |
| ↳↳ identity_authorized_bc_id | string | Có điều kiện | Bắt buộc khi `identity_type` là `BC_AUTH_TT`. ID Business Center liên kết. |
| ↳↳ ad_format | string | Có điều kiện | Định dạng quảng cáo: `SINGLE_VIDEO`, `SINGLE_IMAGE`, `CAROUSEL_ADS`. |
| ↳↳ video_id | string | Không bắt buộc | ID video. Xem [/file/video/ad/search/](71-video.md#doc-1740050472224769). |
| ↳↳ image_ids | string[] | Không bắt buộc | Danh sách ID hình ảnh sử dụng trong quảng cáo hoặc làm ảnh bìa video. |
| ↳↳ music_id | string | Không bắt buộc | ID bản nhạc sử dụng cho TikTok Carousel Ad. |
| ↳↳ tiktok_item_id | string | Không bắt buộc | ID bài đăng TikTok sử dụng làm Spark Ad. Xem [Tạo Spark Ads](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1739470744631298). |
| ↳↳ ad_text | string | Không bắt buộc | Văn bản quảng cáo. Giới hạn tối đa 100 ký tự. Có thể tham khảo [Smart Text](38-creative-tools.md#doc-1739084248002626). |
| ↳↳ aigc_disclosure_type | string | Không bắt buộc | Bật nhãn tự công bố nội dung do AI tạo (AIGC): `SELF_DISCLOSURE`, `NOT_DECLARED` (mặc định). Xem [Nhãn tự công bố AIGC](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1799186631031809). |
| ↳↳ creative_auto_enhancement_strategy_list | string[] | Không bắt buộc | Danh sách chiến lược tự động nâng cao chất lượng nội dung sáng tạo: `VIDEO_QUALITY`, `MUSIC_REFRESH`, `IMAGE_QUALITY`, `IMAGE_RESIZE`. |
| ↳↳ tracking_pixel_id | string | Không bắt buộc | ID TikTok Pixel để theo dõi sự kiện ngoài trang web. |
| ↳↳ tracking_app_id | string | Không bắt buộc | ID ứng dụng để theo dõi sự kiện ứng dụng ngoài trang web. |
| ↳ smart_creative_info | object | Không bắt buộc | Tùy chỉnh thông tin nội dung sáng tạo cho nhóm quảng cáo Smart Creative khi ở chế độ `CUSTOM`. |
| ↳↳ media_info_list | object[] | Có điều kiện | Bắt buộc khi truyền `smart_creative_info`. Danh sách tài liệu đa phương tiện (tối đa 30 phần tử). |
| ↳↳↳ media_info | object | Có điều kiện | Thông tin vật liệu (hình ảnh/video). |
| ↳↳↳↳ image_info | object[] | Không bắt buộc | Thông tin hình ảnh (chứa `web_uri` và `file_name`). |
| ↳↳↳↳ video_info | object | Không bắt buộc | Thông tin video (chứa `video_id` và `file_name`). |
| ↳↳↳↳ aigc_disclosure_type | string | Không bắt buộc | Tự công bố AIGC: `SELF_DISCLOSURE`, `NOT_DECLARED`. |
| ↳↳↳↳ tiktok_item_id | string | Không bắt buộc | ID bài đăng TikTok làm Spark Ad. |
| ↳↳↳↳ identity_id | string | Có điều kiện | ID danh tính. |
| ↳↳↳↳ identity_type | string | Có điều kiện | Loại danh tính: `AUTH_CODE`, `TT_USER`. |
| ↳↳ title_list | object[] | Không bắt buộc | Danh sách tiêu đề / văn bản quảng cáo (tối đa 5). Mỗi tiêu đề từ 12–40 ký tự. |
| ↳↳ call_to_action_list | object[] | Không bắt buộc | Danh sách lời kêu gọi hành động (CTA) (tối đa 3). Xem [Enum - CTA](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳↳ deeplink_list | object[] | Không bắt buộc | Danh sách liên kết sâu (deeplink) (tối đa 1). Chứa `deeplink` và `deeplink_type` (`NORMAL`, `DEFERRED_DEEPLINK`). |
| ↳↳ display_name_list | object[] | Không bắt buộc | Danh sách tên hiển thị (chứa `app_name` hoặc `landing_page_name`, tối đa 40 ký tự). |
| ↳↳ page_list | object[] | Không bắt buộc | Danh sách ID trang đích tức thì (Instant Page) (tối đa 3). Chứa `page_id`. |
| ↳↳ card_list | object[] | Không bắt buộc | Danh sách thẻ sáng tạo portfolio (`card_id` cho Sticker đếm ngược, Thẻ tải xuống...). |
| ↳↳ landing_page_urls | object[] | Có điều kiện | Danh sách URL trang đích khi `fallback_type` là `WEBSITE`. |
| ↳↳ common_material | object | Không bắt buộc | Cấu hình vật liệu chung (`identity_id`, `identity_type`, `ad_name`, `call_to_action_id`, `creative_authorized`, `playable_url`, `fallback_type`, `tracking_info`). |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi. Xem chi tiết tại [Phụ lục - Mã trả về](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. |
| request_id | string | ID log của yêu cầu. |
| data | object | Dữ liệu tác vụ được trả về. |
| ↳ task_id | string | ID của tác vụ sao chép chiến dịch bất đồng bộ.<br>Sử dụng endpoint [/campaign/copy/task/check/](24-campaign.md#doc-1788434463507458) để kiểm tra tiến độ và kết quả.<br>Nếu xảy ra lỗi (danh sách `adgroup_error_list` không rỗng), ID tác vụ sẽ không được tạo và giá trị trường này là chuỗi rỗng (`""`). |
| ↳ adgroup_error_list | object[] | Danh sách lỗi gặp phải trong quá trình sao chép các nhóm quảng cáo cụ thể. Nếu không có lỗi, trường này là danh sách rỗng (`[]`). |
| ↳↳ adgroup_id | string | ID của nhóm quảng cáo bị lỗi không thể sao chép. |
| ↳↳ error_message | string | Thông điệp lỗi chi tiết đối với nhóm quảng cáo (`adgroup_id`). |

### Ví dụ

#### 1. Chế độ sao chép mặc định không áp dụng lịch chạy chung

```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/campaign/copy/task/create/' \
  --header 'Access-Token: YOUR_ACCESS_TOKEN' \
  --header 'Content-Type: application/json' \
  --data '{
    "advertiser_id": "7123456789012345678",
    "campaign_id": "1765432109876545",
    "request_id": "1684742400123456",
    "deep_copy_mode": "DEFAULT"
}'
```

#### 2. Chế độ sao chép tùy chỉnh với nhóm quảng cáo và quảng cáo được chọn

```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/campaign/copy/task/create/' \
  --header 'Access-Token: YOUR_ACCESS_TOKEN' \
  --header 'Content-Type: application/json' \
  --data '{
    "advertiser_id": "7123456789012345678",
    "campaign_id": "1765432109876545",
    "request_id": "1684742400123457",
    "deep_copy_mode": "CUSTOM",
    "schedule_type": "SCHEDULE_START_END",
    "schedule_start_time": "2023-06-01 00:00:00",
    "schedule_end_time": "2023-06-30 23:59:59",
    "adgroup_list": [
      {
        "adgroup_id": "1765432109876599",
        "ad_list": [
          {"ad_id": "1765432109876611"}
        ]
      }
    ]
}'
```

#### Ví dụ phản hồi thành công (tạo tác vụ thành công)

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "2023052210032301011023224213556",
  "data": {
    "task_id": "copy_task_7123456789012345678_1684742400",
    "adgroup_error_list": []
  }
}
```

#### Ví dụ phản hồi có lỗi (không tạo được tác vụ)

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "2023052210032301011023224213557",
  "data": {
    "task_id": "",
    "adgroup_error_list": [
      {
        "adgroup_id": "1765432109876599",
        "error_message": "Start time cannot be earlier than the current time. Please edit the start time and try again."
      }
    ]
  }
}
```


---

## Lấy kết quả tác vụ sao chép bất đồng bộ cho Chiến dịch thủ công (`Get the results of an asynchronous copy task for a Manual Campaign`)
<a id="doc-1788434463507458"></a>
<!-- doc_id: 1788434463507458 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/campaign/copy/task/check/`

**Mục đích**: Sử dụng endpoint này để kiểm tra tiến độ và kết quả của tác vụ sao chép bất đồng bộ cho Chiến dịch thủ công.

Chúng tôi khuyến nghị bạn nên đợi khoảng 1 phút sau khi tạo tác vụ bằng endpoint [/campaign/copy/task/create/](24-campaign.md#doc-1788434394151938) trước khi gọi endpoint này để kiểm tra kết quả.

Để kiểm tra kết quả tác vụ sao chép bất đồng bộ cho Chiến dịch Smart+ nâng cấp, vui lòng sử dụng [/smart_plus/campaign/copy/task/check/](62-upgraded-smartplus-p1.md#doc-1866529943741441).

> [!NOTE]
> • API sao chép chiến dịch bất đồng bộ hiện là tính năng chỉ dành cho danh sách cho phép (allowlist-only). Nếu bạn muốn truy cập, vui lòng liên hệ đại diện TikTok của bạn.<br>• Giới hạn tốc độ gọi (rate limit) cho endpoint này là 2 truy vấn/giây (QPS) và 60 truy vấn/phút (QPM) cho mỗi ứng dụng nhà phát triển (developer app). [Giới hạn tốc độ toàn cầu](../04-get-started/bat-dau.md#doc-1740029171730433) không áp dụng cho endpoint này.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Access token (mã truy cập) đã được ủy quyền. Chi tiết xem [Xác thực](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (Query Parameters)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| advertiser_id | string | Bắt buộc | ID của nhà quảng cáo / tài khoản quảng cáo. |
| task_id | string | Bắt buộc | ID của tác vụ sao chép chiến dịch bất đồng bộ.<br>Để lấy ID tác vụ, sử dụng endpoint [/campaign/copy/task/create/](24-campaign.md#doc-1788434394151938). |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi. Xem chi tiết tại [Phụ lục - Mã trả về](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. Xem chi tiết tại [Phụ lục - Mã trả về](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | ID log của yêu cầu, định danh duy nhất cho một yêu cầu HTTP. |
| data | object | Dữ liệu kết quả tác vụ. |
| ↳ task_status | string | Trạng thái của tác vụ sao chép chiến dịch bất đồng bộ.<br>Giá trị enum:<br>• `RUNNING`: Tác vụ đang được xử lý.<br>• `SUCCESS`: Tác vụ đã được xử lý xong. Kiểm tra `task_result` để xem chi tiết kết quả thành công.<br>• `FAILURE`: Tác vụ xử lý thất bại. |
| ↳ task_info | object | Tổng quan về kết quả thực hiện tác vụ. |
| ↳↳ total_ad_count | number | Tổng số quảng cáo đã gửi yêu cầu sao chép. |
| ↳↳ success_ad_count | number | Số lượng quảng cáo đã được sao chép thành công. |
| ↳↳ total_smart_creative_adgroup_count | number | Tổng số nhóm quảng cáo Smart Creative đã gửi yêu cầu sao chép. |
| ↳↳ success_smart_creative_adgroup_count | number | Số lượng nhóm quảng cáo Smart Creative đã được sao chép thành công. |
| ↳ task_result | object | Chi tiết kết quả của tác vụ. |
| ↳↳ campaign_id | string | ID của chiến dịch mới vừa được tạo sau khi sao chép. |
| ↳↳ campaign_name | string | Tên của chiến dịch mới.<br>Nếu quá trình sao chép chiến dịch thất bại, trường này vẫn được trả về để biểu thị chiến dịch chưa sao chép thành công. |
| ↳↳ campaign_error_infos | string[] | Danh sách thông tin lỗi gặp phải trong quá trình sao chép chiến dịch. Nếu không có lỗi, trường này là danh sách rỗng (`[]`). |
| ↳↳ adgroup_result_list | object[] | Chi tiết kết quả sao chép cho từng nhóm quảng cáo. |
| ↳↳↳ adgroup_id | string | ID của nhóm quảng cáo mới vừa được tạo. |
| ↳↳↳ adgroup_name | string | Tên của nhóm quảng cáo mới. |
| ↳↳↳ total_ad_count | number | Số lượng quảng cáo đã thử sao chép vào nhóm quảng cáo mới này. |
| ↳↳↳ success_ad_count | number | Số lượng quảng cáo đã được sao chép thành công vào nhóm quảng cáo mới này. |
| ↳↳↳ adgroup_error_list | string[] | Danh sách lỗi gặp phải trong quá trình sao chép nhóm quảng cáo. Nếu không có lỗi, trường này là danh sách rỗng (`[]`). |
| ↳↳↳ ad_status | string | Kết quả sao chép quảng cáo từ nhóm quảng cáo gốc sang nhóm quảng cáo mới.<br>Giá trị enum:<br>• `ALL_SUCCESS`: Tất cả quảng cáo từ nhóm gốc đã được sao chép thành công.<br>• `PARTIAL_SUCCESS`: Một phần hoặc toàn bộ quảng cáo từ nhóm gốc bị lỗi không sao chép được. |
| ↳↳↳ is_smart_creative | boolean | Nhóm quảng cáo mới có phải là nhóm Smart Creative hay không: `true`, `false`. |
| ↳↳↳ smart_creative_result | object | Chỉ trả về khi `is_smart_creative` là `true`. Chi tiết kết quả sao chép các vật liệu nội dung sáng tạo trong nhóm Smart Creative. |
| ↳↳↳↳ is_success | boolean | Việc sao chép các vật liệu nội dung sáng tạo có thành công hay không: `true`, `false`. |
| ↳↳↳↳ smart_creative_error_list | string[] | Danh sách lỗi gặp phải khi sao chép vật liệu sáng tạo. Nếu không có lỗi, trường này trả về `[]`. |
| ↳↳↳ ad_result_list | object[] | Chi tiết kết quả sao chép của từng quảng cáo. |
| ↳↳↳↳ is_success | boolean | Sao chép quảng cáo thành công hay không: `true`, `false`. |
| ↳↳↳↳ ad_id | string | ID của quảng cáo mới được tạo. |
| ↳↳↳↳ ad_name | string | Tên của quảng cáo mới. |
| ↳↳↳↳ ad_error_list | string[] | Danh sách lỗi gặp phải trong quá trình sao chép quảng cáo. |

### Ví dụ

#### Gọi API bằng curl

```bash
curl -G --location "https://business-api.tiktok.com/open_api/v1.3/campaign/copy/task/check/" \
  --header "Access-Token: YOUR_ACCESS_TOKEN" \
  --data-urlencode "advertiser_id=7123456789012345678" \
  --data-urlencode "task_id=copy_task_7123456789012345678_1684742400"
```

#### Gọi API bằng Python

```python
import requests

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ADVERTISER_ID = "7123456789012345678"
TASK_ID = "copy_task_7123456789012345678_1684742400"

url = "https://business-api.tiktok.com/open_api/v1.3/campaign/copy/task/check/"
headers = {
    "Access-Token": ACCESS_TOKEN
}
params = {
    "advertiser_id": ADVERTISER_ID,
    "task_id": TASK_ID
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
  "request_id": "2023052210032301011023224213558",
  "data": {
    "task_status": "SUCCESS",
    "task_info": {
      "total_ad_count": 1,
      "total_smart_creative_adgroup_count": 0,
      "success_smart_creative_adgroup_count": 0,
      "success_ad_count": 1
    },
    "task_result": {
      "campaign_id": "1765432109876550",
      "campaign_name": "COPIED_Summer_Promotion_Traffic_2023",
      "campaign_error_infos": [],
      "adgroup_result_list": [
        {
          "adgroup_id": "1765432109876690",
          "adgroup_name": "COPIED_AdGroup_1",
          "total_ad_count": 1,
          "success_ad_count": 1,
          "adgroup_error_list": [],
          "is_smart_creative": false,
          "ad_status": "ALL_SUCCESS",
          "ad_result_list": [
            {
              "ad_id": "1765432109876790",
              "ad_name": "COPIED_Ad_1_1765432109876611",
              "is_success": true,
              "ad_error_list": []
            }
          ]
        }
      ]
    }
  }
}
```

---

## (Không dùng nữa) Lấy hạn mức cho Chiến dịch chuyên dụng iOS 14 (`(Deprecated) Get the quota for an iOS 14 Dedicated Campaign`)
<a id="doc-1739324098894850"></a>
<!-- doc_id: 1739324098894850 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/campaign/quota/get/`

**Mục đích**: Lấy thông tin hạn mức cho Chiến dịch chuyên dụng iOS 14 (Dedicated Campaign - DC) và các nhóm quảng cáo thuộc chiến dịch. Mỗi ứng dụng iOS có thể có tối đa 11 DC và mỗi DC có thể có tối đa 2 nhóm quảng cáo.

> [!WARNING]
> **Endpoint đã ngừng hỗ trợ (Deprecated)**: Để lấy thông tin hạn mức chính xác, vui lòng sử dụng [/campaign/quota/info/](24-campaign.md#doc-1752256376677378) thay vì endpoint này, vì hạn mức trả về bởi endpoint này không còn chính xác.

Theo quy định Thực thi tính minh bạch trong theo dõi ứng dụng (ATT) của Apple, bạn chỉ có thể tạo tối đa 11 iOS 14 DC dưới một ứng dụng iOS. Tuy nhiên, với cơ chế tối ưu hóa hạn mức DC, bạn có thể tạo tối đa 11 iOS DC cho mỗi mạng quảng cáo trong một ứng dụng iOS. Xem [Tối ưu hóa hạn mức Chiến dịch chuyên dụng iOS 14](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1752256248260610) để tìm hiểu các thay đổi chi tiết ở cấp chiến dịch và nhóm quảng cáo. Xem [Chiến dịch chuyên dụng iOS 14 - Hạn mức Chiến dịch chuyên dụng iOS 14](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1740029173531649) để nắm rõ các quy tắc hạn mức.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Access token (mã truy cập) đã được ủy quyền. Chi tiết xem [Xác thực](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (Query Parameters)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| advertiser_id | string | Bắt buộc | ID của nhà quảng cáo / tài khoản quảng cáo. |
| app_id | string | Bắt buộc | ID ứng dụng của ứng dụng được quảng bá. Bạn có thể lấy `app_id` qua endpoint [/app/list/](43-events-1-0-p1.md#doc-1740859313270786). |
| campaign_id | string | Không bắt buộc | ID chiến dịch cần truy vấn hạn mức nhóm quảng cáo. |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi. Xem [Phụ lục - Mã trả về](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. |
| data | object | Dữ liệu hạn mức được trả về. |
| ↳ campaign_quota | object | Hạn mức chiến dịch theo ID nhà quảng cáo. |
| ↳↳ used_quota | number | Số lượng chiến dịch iOS 14 đã được khởi chạy. |
| ↳↳ releasing_quota | number | Số lượng chiến dịch iOS 14 đang chờ giải phóng hạn mức. |
| ↳↳ available_quota | number | Số lượng chiến dịch iOS 14 bạn có thể khởi chạy lúc này. |
| ↳↳ total_quota | number | Tổng hạn mức chiến dịch iOS 14 đang hoạt động. |
| ↳ adgroup_quota | object | Hạn mức nhóm quảng cáo thuộc chiến dịch. |
| ↳↳ campaign_id | number | ID của chiến dịch. |
| ↳↳ used_quota | number | Số lượng nhóm quảng cáo đã khởi chạy. |
| ↳↳ available_quota | number | Số lượng nhóm quảng cáo bạn có thể khởi chạy lúc này. |
| ↳↳ total_quota | number | Tổng hạn mức nhóm quảng cáo đang hoạt động. |
| ↳ split_test_quota | object | Thông tin hạn mức thử nghiệm phân tách (split test). |
| ↳↳ max_test_number | integer | Số nhóm thử nghiệm tối đa trong một thử nghiệm phân tách (chỉ có thể là `2`). |
| ↳↳ available_test_group | integer | Số nhóm thử nghiệm phân tách iOS 14 có thể khởi chạy ngay trong ứng dụng này. |
| ↳↳ used_test_group | integer | Số nhóm thử nghiệm phân tách iOS 14 đã được khởi chạy. |
| ↳↳ releasing_test_group | integer | Số nhóm thử nghiệm phân tách iOS 14 đang chờ giải phóng. |
| ↳↳ used_quota | integer | Số lượng hạn mức đã khởi chạy. |
| ↳↳ releasing_quota | integer | Số lượng hạn mức đang chờ giải phóng. |
| request_id | string | ID log duy nhất của yêu cầu. |

### Ví dụ

#### Gọi API bằng curl

```bash
curl -G --location "https://business-api.tiktok.com/open_api/v1.3/campaign/quota/get/" \
  --header "Access-Token: YOUR_ACCESS_TOKEN" \
  --data-urlencode "advertiser_id=7123456789012345678" \
  --data-urlencode "app_id=1234567890"
```

#### Gọi API bằng Python

```python
import requests

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ADVERTISER_ID = "7123456789012345678"
APP_ID = "1234567890"

url = "https://business-api.tiktok.com/open_api/v1.3/campaign/quota/get/"
headers = {
    "Access-Token": ACCESS_TOKEN
}
params = {
    "advertiser_id": ADVERTISER_ID,
    "app_id": APP_ID
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
  "request_id": "2021012712121901023101600706029954",
  "data": {
    "campaign_quota": {
      "used_quota": 5,
      "releasing_quota": 0,
      "available_quota": 6,
      "total_quota": 11
    }
  }
}
```
