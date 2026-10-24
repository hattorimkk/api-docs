import re

path = "/Users/hattorimk/Desktop/api-docs/tiktok-business-api/docs/09-marketing-api/bao-cao-p3.md"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

# Common phrases & sentences
replacements = [
    # Notes in Section 1 (Filters)
    ("> -  If the provided filter field `field_name` and `data_level` don't match, the system will return an error: \"Invalid value for filter field: xxxx is not supported\". For example, if `data_level` is `AUCTION_AD`, you can only set `field_name` to a filter field at the ad level (such as `ad_ids`).",
     "> - Nếu trường bộ lọc `field_name` được cung cấp và `data_level` không khớp, hệ thống sẽ trả về lỗi: \"Invalid value for filter field: xxxx is not supported\". Ví dụ: nếu `data_level` là `AUCTION_AD`, bạn chỉ có thể đặt `field_name` thành trường bộ lọc ở cấp quảng cáo (chẳng hạn như `ad_ids`)."),
    ("> - In asynchronous basic reports, the only supported filter fields are `campaign_ids`, `adgroup_ids`, and `ad_ids`.",
     "> - Trong báo cáo cơ bản không đồng bộ (asynchronous basic reports), các trường bộ lọc duy nhất được hỗ trợ là `campaign_ids`, `adgroup_ids` và `ad_ids`."),
    ("> -  Basic reports now include data for Auction ads, Reach & Frequency ads, and TopView ads. To filter data for a specific buying type, use [/report/integrated/get/](../12-api-reference/58-reporting.md#doc-1740302848100353) to run a basic report. Within the filtering object, specify the `buying_type` field and enter the values of either `AUCTION`, `RESERVATION_TOP_VIEW`, or `RESERVATION_RF`.",
     "> - Báo cáo cơ bản hiện bao gồm dữ liệu cho Quảng cáo Đấu thầu (Auction ads), Quảng cáo Tiếp cận & Tần suất (Reach & Frequency ads) và Quảng cáo TopView. Để lọc dữ liệu theo loại hình mua cụ thể, hãy sử dụng [/report/integrated/get/](../12-api-reference/58-reporting.md#doc-1740302848100353) để chạy báo cáo cơ bản. Trong đối tượng bộ lọc, chỉ định trường `buying_type` và nhập một trong các giá trị `AUCTION`, `RESERVATION_TOP_VIEW` hoặc `RESERVATION_RF`."),
    ("> -  For TopView ads, cost-related metrics at ad level and cost-related metrics for audience breakdown will only include data for ads delivered after January 18th, 2024.",
     "> - Đối với quảng cáo TopView, các chỉ số liên quan đến chi phí ở cấp quảng cáo và các chỉ số chi phí phân tích theo đối tượng sẽ chỉ bao gồm dữ liệu cho các quảng cáo được phân phối sau ngày 18 tháng 1 năm 2024."),
    ("> -  The reporting data for [Product GMV max ads](https://ads.tiktok.com/help/article/how-to-create-product-gmv-max-ads-in-seller-center) and LIVE GMV max ads created from TikTok Shop is excluded from synchronous Auction basic reports, audience reports, playable ad reports, and DSA reports. Shopping Ads created via API or TikTok Ads Manager are not affected.",
     "> - Dữ liệu báo cáo cho [quảng cáo Product GMV Max](https://ads.tiktok.com/help/article/how-to-create-product-gmv-max-ads-in-seller-center) và quảng cáo LIVE GMV Max tạo từ TikTok Shop sẽ bị loại trừ khỏi các báo cáo cơ bản Đấu thầu đồng bộ, báo cáo đối tượng, báo cáo quảng cáo tương tác và báo cáo DSA. Quảng cáo Mua sắm (Shopping Ads) được tạo qua API hoặc TikTok Ads Manager không bị ảnh hưởng."),

    # Table descriptions in Section 1
    ("Filter value example: `\"[123,456,789]\"`.", "Ví dụ giá trị lọc: `\"[123,456,789]\"`."),
    ("Campaign automation type. ⏎ Các giá trị enum hỗ trợ: • `MANUAL`: Manual Campaigns. • `SMART_PLUS`: Smart+ Campaigns. • `UPGRADED_SMART_PLUS`: Upgraded Smart+ Campaigns. To learn more about Upgraded Smart+ Campaigns, see [Upgraded Smart+ Campaign](quan-ly-chien-dich-p1.md#doc-1853452461203458). • When `campaign_automation_type` is `UPGRADED_SMART_PLUS`, the returned `ad_id_v2` is the ID of the Upgraded Smart+ Ad.",
     "Loại tự động hóa chiến dịch (Campaign automation type). ⏎ Các giá trị enum hỗ trợ: • `MANUAL`: Chiến dịch thủ công. • `SMART_PLUS`: Chiến dịch Smart+. • `UPGRADED_SMART_PLUS`: Chiến dịch Upgraded Smart+. Để tìm hiểu thêm về Chiến dịch Upgraded Smart+, xem [Chiến dịch Upgraded Smart+](quan-ly-chien-dich-p1.md#doc-1853452461203458). • Khi `campaign_automation_type` là `UPGRADED_SMART_PLUS`, trường `ad_id_v2` trả về là ID của Quảng cáo Upgraded Smart+."),
    ("The campaign origins (campaign sources). ⏎ Các giá trị enum hỗ trợ: • `PROMOTE`: The campaign is a Promote campaign created through the TikTok mobile App. • `TT_ADS_PLATFORM`: The campaign is a non-Promote campaign created through the API or in TikTok Ads Manager.  Giá trị mặc định: `\"[\\\"TT_ADS_PLATFORM\\\"]\"`. ⏎ To learn more about the supported dimensions, metrics and filters for Promote ads, see [Promote campaigns](quan-ly-chien-dich-p1.md#doc-1785880454546433). ⏎ **Note**:  •  This filter is only supported in synchronous basic reports.  •  In asynchronous basic reports, the results include the data for Promote ads by default.",
     "Nguồn gốc chiến dịch (nguồn chiến dịch). ⏎ Các giá trị enum hỗ trợ: • `PROMOTE`: Chiến dịch là chiến dịch Promote được tạo qua ứng dụng TikTok trên thiết bị di động. • `TT_ADS_PLATFORM`: Chiến dịch là chiến dịch thông thường không phải Promote được tạo qua API hoặc trên TikTok Ads Manager. Giá trị mặc định: `\"[\\\"TT_ADS_PLATFORM\\\"]\"`. ⏎ Để tìm hiểu thêm về các chiều dữ liệu, chỉ số và bộ lọc được hỗ trợ cho quảng cáo Promote, xem [Chiến dịch Promote](quan-ly-chien-dich-p1.md#doc-1785880454546433). ⏎ **Lưu ý**: • Bộ lọc này chỉ được hỗ trợ trong báo cáo cơ bản đồng bộ. • Trong báo cáo cơ bản không đồng bộ, kết quả mặc định bao gồm dữ liệu của quảng cáo Promote."),
    ("• The types of IDs you can filter include: • the ID of a Manual Ad. • the ID of an Upgraded Smart+ **Ad** (**Asset Group**). • You need to set `data_level` to `AUCTION_AD`and include `ad_id_v2` in `dimensions`. • You can specify up to 100 values when using this filter. • You cannot use it together with the dimension `ad_id` or the filter `ad_ids`.",
     "• Các loại ID bạn có thể lọc bao gồm: • ID của Quảng cáo thủ công. • ID của **Quảng cáo** Upgraded Smart+ (**Nhóm tài sản - Asset Group**). • Bạn cần đặt `data_level` thành `AUCTION_AD` và đưa `ad_id_v2` vào `dimensions`. • Bạn có thể chỉ định tối đa 100 giá trị khi dùng bộ lọc này. • Bạn không thể sử dụng bộ lọc này cùng với chiều dữ liệu `ad_id` hoặc bộ lọc `ad_ids`."),
    ("Campaign status. Để xem danh sách giá trị enum, xem [Enumeration-Ad Management-Primary Status](../15-appendix/phu-luc-p1.md#doc-1737174886619138). ⏎ **Note**: If not set, this filter field will default to `STATUS_NOT_DELETE` in synchronous basic reports.",
     "Trạng thái chiến dịch (Campaign status). Để xem danh sách giá trị enum, xem [Enum - Quản lý quảng cáo - Trạng thái chính](../15-appendix/phu-luc-p1.md#doc-1737174886619138). ⏎ **Lưu ý**: Nếu không đặt, trường bộ lọc này sẽ mặc định là `STATUS_NOT_DELETE` trong báo cáo cơ bản đồng bộ."),
    ("Ad Group status. Để xem danh sách giá trị enum, xem [Enumeration-Ad Management-Primary Status](../15-appendix/phu-luc-p1.md#doc-1737174886619138). ⏎ **Note**: If not set, this filter field will default to `STATUS_NOT_DELETE` in synchronous basic reports.",
     "Trạng thái nhóm quảng cáo (Ad Group status). Để xem danh sách giá trị enum, xem [Enum - Quản lý quảng cáo - Trạng thái chính](../15-appendix/phu-luc-p1.md#doc-1737174886619138). ⏎ **Lưu ý**: Nếu không đặt, trường bộ lọc này sẽ mặc định là `STATUS_NOT_DELETE` trong báo cáo cơ bản đồng bộ."),
    ("Ad Status. Để xem danh sách giá trị enum, xem [Enumeration-Ad Management-Primary Status](../15-appendix/phu-luc-p1.md#doc-1737174886619138). ⏎ **Note**: If not set, this filter field will default to `STATUS_NOT_DELETE` in synchronous basic reports.",
     "Trạng thái quảng cáo (Ad Status). Để xem danh sách giá trị enum, xem [Enum - Quản lý quảng cáo - Trạng thái chính](../15-appendix/phu-luc-p1.md#doc-1737174886619138). ⏎ **Lưu ý**: Nếu không đặt, trường bộ lọc này sẽ mặc định là `STATUS_NOT_DELETE` trong báo cáo cơ bản đồng bộ."),
    ("A list of campaign label IDs. ⏎ Kích thước tối đa: 50. ⏎ Each label ID must be a 19-digit numeric string. ⏎ **Note**: This filter is only supported in synchronous reports.",
     "Danh sách ID nhãn chiến dịch. ⏎ Kích thước tối đa: 50. ⏎ Mỗi ID nhãn phải là một chuỗi số 19 chữ số. ⏎ **Lưu ý**: Bộ lọc này chỉ được hỗ trợ trong báo cáo đồng bộ."),
    ("A list of campaign label names. ⏎ Fuzzy matching is supported. ⏎ Kích thước tối đa: 10. ⏎ **Note**: This filter is only supported in synchronous reports.",
     "Danh sách tên nhãn chiến dịch. ⏎ Hỗ trợ khớp mờ (fuzzy matching). ⏎ Kích thước tối đa: 10. ⏎ **Lưu ý**: Bộ lọc này chỉ được hỗ trợ trong báo cáo đồng bộ."),
    ("A list of campaign label types. ⏎ Các giá trị enum hỗ trợ: • `GENERAL`: General label. • `MARKETING_EVENT`: Marketing event label. ⏎ **Note**: This filter is only supported in synchronous reports.",
     "Danh sách loại nhãn chiến dịch. ⏎ Các giá trị enum hỗ trợ: • `GENERAL`: Nhãn chung. • `MARKETING_EVENT`: Nhãn sự kiện tiếp thị. ⏎ **Lưu ý**: Bộ lọc này chỉ được hỗ trợ trong báo cáo đồng bộ."),
    ("Advertising Objective. ⏎ Các giá trị enum hỗ trợ:", "Mục tiêu quảng cáo (Advertising Objective). ⏎ Các giá trị enum hỗ trợ:"),
    ("Events that you want to pay for. Để xem danh sách giá trị enum, xem Enumeration - [Billing Event](../15-appendix/phu-luc-p1.md#doc-1737174886619138).",
     "Sự kiện tính phí (Billing Event). Để xem danh sách giá trị enum, xem [Enum - Sự kiện tính phí](../15-appendix/phu-luc-p1.md#doc-1737174886619138)."),
    ("Age groups you want to target. ⏎ Để xem danh sách giá trị enum, xem [Enumeration - Targeting Age Group](../15-appendix/phu-luc-p1.md#doc-1737174886619138).",
     "Nhóm tuổi mục tiêu. ⏎ Để xem danh sách giá trị enum, xem [Enum - Nhóm tuổi mục tiêu](../15-appendix/phu-luc-p1.md#doc-1737174886619138)."),
    ("Gender that you want to target. ⏎ Enum values:", "Giới tính mục tiêu. ⏎ Các giá trị enum:"),
    ("The audience type for DPA campaigns. ⏎ Enum values:", "Loại đối tượng cho chiến dịch DPA. ⏎ Các giá trị enum:"),
    ("The buying type. ⏎ Các giá trị enum hỗ trợ:", "Loại hình mua (Buying type). ⏎ Các giá trị enum hỗ trợ:"),
    ("Targeting language code. ⏎ Supports single language code or JSON array of languages.",
     "Mã ngôn ngữ mục tiêu. ⏎ Hỗ trợ một mã ngôn ngữ đơn lẻ hoặc mảng JSON chứa các ngôn ngữ."),
    ("Filter by Smart+ campaign type.", "Lọc theo loại chiến dịch Smart+."),
    ("Bid strategy. ⏎ Các giá trị enum hỗ trợ:", "Chiến lược giá thầu (Bid strategy). ⏎ Các giá trị enum hỗ trợ:"),
    ("Delivery Type (pacing). ⏎ Các giá trị enum hỗ trợ:", "Kiểu phân phối ngân sách (Delivery Type / pacing). ⏎ Các giá trị enum hỗ trợ:"),
    ("Ad type. ⏎ Các giá trị enum hỗ trợ:", "Loại quảng cáo (Ad type). ⏎ Các giá trị enum hỗ trợ:"),
    ("Identity type. ⏎ Các giá trị enum hỗ trợ:", "Loại danh tính (Identity type). ⏎ Các giá trị enum hỗ trợ:"),
    ("Creative format. ⏎ Các giá trị enum hỗ trợ: • `IMAGE_MODE_LARGE`：Image • `IMAGE_MODE_VIDEO`：Video (16:9) • `IMAGE_MODE_VIDEO_SQUARE`：Video (1:1) • `IMAGE_MODE_VIDEO_VERTICAL`：Video (9:16) • `CAROUSEL_ADS`: Carousel. ⏎ **Note**: This filter is only supported in synchronous basic reports.",
     "Định dạng nội dung sáng tạo (Creative format). ⏎ Các giá trị enum hỗ trợ: • `IMAGE_MODE_LARGE`：Hình ảnh • `IMAGE_MODE_VIDEO`：Video (16:9) • `IMAGE_MODE_VIDEO_SQUARE`：Video (1:1) • `IMAGE_MODE_VIDEO_VERTICAL`：Video (9:16) • `CAROUSEL_ADS`: Bộ sưu tập hình ảnh xoay vòng (Carousel). ⏎ **Lưu ý**: Bộ lọc này chỉ được hỗ trợ trong báo cáo cơ bản đồng bộ."),
    ("The strategy that your creatives will be delivered.  Các giá trị enum hỗ trợ: `CUSTOM`(custom), `DYNAMIC`(automated), `SMART_CREATIVE`(Smart Creative).",
     "Chiến lược phân phối mẫu quảng cáo sáng tạo. Các giá trị enum hỗ trợ: `CUSTOM` (tùy chỉnh), `DYNAMIC` (tự động hóa), `SMART_CREATIVE` (Smart Creative)."),
    ("The campaign type. Các giá trị enum hỗ trợ:", "Loại chiến dịch (The campaign type). Các giá trị enum hỗ trợ:"),
    ("Filter by Liệu campaign is a Smart+, Search Ads Campaign, or neither.", "Lọc theo loại chiến dịch Smart+, Search Ads Campaign, hoặc chiến dịch thông thường."),
    ("Destination page type. ⏎ Các giá trị enum hỗ trợ: •  `APP`: The download page for the promoted App in Google Play or Apple Store. The `promotion_type` for the corresponding ad group is set as `APP_ANDROID` or `APP_IOS`.  • `TIKTOK_INSTANT_PAGE`: TikTok Instant Pages, including Custom Page, Instant Form, App Profile Page, and Instant Product Page. The page ID (`page_id`) of a TikTok Instant Page is specified for the ad.  • `WEBSITE`: Website page. A landing page URL (`landing_page_url`) is specified for the ad. • `SOCIAL_MEDIA_APP`: Social media URL. To learn about the ads where the destination can be set as social media URL, see [Create a Lead Generation ad with promotion type as instant messaging apps](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1774482999036930). • `PHONE_CALL`: Phone number. To learn about the ads where the destination can be set as phone number, see [Create a Lead Generation ad with promotion type as phone call](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1774482936048641). ⏎ **Note**: This filter is only supported in synchronous basic reports.",
     "Loại trang đích (Destination page type). ⏎ Các giá trị enum hỗ trợ: • `APP`: Trang tải xuống ứng dụng được quảng bá trên Google Play hoặc Apple App Store. Trường `promotion_type` của nhóm quảng cáo tương ứng được đặt thành `APP_ANDROID` hoặc `APP_IOS`. • `TIKTOK_INSTANT_PAGE`: Trang tức thì TikTok (TikTok Instant Pages), bao gồm Trang tùy chỉnh (Custom Page), Biểu mẫu tức thì (Instant Form), Trang hồ sơ ứng dụng (App Profile Page), và Trang sản phẩm tức thì (Instant Product Page). ID trang (`page_id`) của TikTok Instant Page được chỉ định cho quảng cáo. • `WEBSITE`: Trang web. URL trang đích (`landing_page_url`) được chỉ định cho quảng cáo. • `SOCIAL_MEDIA_APP`: URL ứng dụng mạng xã hội. Để tìm hiểu về quảng cáo có thể đặt trang đích là mạng xã hội, xem [Tạo quảng cáo Tìm kiếm khách hàng tiềm năng với loại quảng bá ứng dụng nhắn tin tức thì](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1774482999036930). • `PHONE_CALL`: Số điện thoại. Để tìm hiểu về quảng cáo có thể đặt trang đích là cuộc gọi, xem [Tạo quảng cáo Tìm kiếm khách hàng tiềm năng với loại quảng bá cuộc gọi](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1774482936048641). ⏎ **Lưu ý**: Bộ lọc này chỉ được hỗ trợ trong báo cáo cơ bản đồng bộ."),
    ("Time range of Thời gian tạo of requested ID dimension (`campaign_id`/`adgroup_id`/`ad_id`). The value needs to be a valid JSON array of 2-element string. The 1st element is start time, the 2nd element is end time. E.g. `\"[\\\"2022-02-24 11:57:51\\\",\\\"2022-03-24 11:57:51\\\"]\"`. This filter can only be used in synchronous reports. ⏎ Suggestion: A time range within 6 months is suggested when applying a Thời gian tạo filter, to ensure that the success and speed of the task won't be affected.",
     "Khoảng thời gian tạo của chiều ID được yêu cầu (`campaign_id`/`adgroup_id`/`ad_id`). Giá trị cần là một mảng JSON hợp lệ gồm 2 phần tử chuỗi. Phần tử thứ 1 là thời gian bắt đầu, phần tử thứ 2 là thời gian kết thúc. Ví dụ: `\"[\\\"2022-02-24 11:57:51\\\",\\\"2022-03-24 11:57:51\\\"]\"`. Bộ lọc này chỉ có thể sử dụng trong báo cáo đồng bộ. ⏎ Khuyến nghị: Nên chọn khoảng thời gian trong vòng 6 tháng khi áp dụng bộ lọc Thời gian tạo, để đảm bảo tốc độ và tỷ lệ thành công của tác vụ không bị ảnh hưởng."),
    ("Creation start time of requested ID dimension (`campaign_id`/`adgroup_id`/`ad_id`). The value is in `YYYY-MM-DD HH:MM:SS` format (UTC time zone). E.g. `\"2022-02-24 11:57:51\"` - dimensions created later than this time will be returned. This filter can only be used in synchronous reports. ⏎ Suggestion: A time range within 6 months is suggested when applying a Thời gian tạo filter, to ensure that the success and speed of the task won't be affected.",
     "Thời gian bắt đầu tạo của chiều ID được yêu cầu (`campaign_id`/`adgroup_id`/`ad_id`). Giá trị ở định dạng `YYYY-MM-DD HH:MM:SS` (múi giờ UTC). Ví dụ: `\"2022-02-24 11:57:51\"` - các chiều dữ liệu được tạo sau thời điểm này sẽ được trả về. Bộ lọc này chỉ có thể sử dụng trong báo cáo đồng bộ. ⏎ Khuyến nghị: Nên chọn khoảng thời gian trong vòng 6 tháng khi áp dụng bộ lọc Thời gian tạo, để đảm bảo tốc độ và tỷ lệ thành công của tác vụ không bị ảnh hưởng."),
    ("Creation end time of requested ID dimension (`campaign_id`/`adgroup_id`/`ad_id`). The value is in `YYYY-MM-DD HH:MM:SS` format (UTC time zone). E.g. `\"2022-02-24 11:57:51\"` - dimensions created earlier than this time will be returned. This filter can only be used in synchronous reports. ⏎ Suggestion: A time range within 6 months is suggested when applying a Thời gian tạo filter, to ensure that the success and speed of the task won't be affected.",
     "Thời gian kết thúc tạo của chiều ID được yêu cầu (`campaign_id`/`adgroup_id`/`ad_id`). Giá trị ở định dạng `YYYY-MM-DD HH:MM:SS` (múi giờ UTC). Ví dụ: `\"2022-02-24 11:57:51\"` - các chiều dữ liệu được tạo trước thời điểm này sẽ được trả về. Bộ lọc này chỉ có thể sử dụng trong báo cáo đồng bộ. ⏎ Khuyến nghị: Nên chọn khoảng thời gian trong vòng 6 tháng khi áp dụng bộ lọc Thời gian tạo, để đảm bảo tốc độ và tỷ lệ thành công của tác vụ không bị ảnh hưởng."),

    # Section 2: Audience reports
    ("Audience reports are a type of report from which you can get audience data, including age, gender, region, or interest.",
     "Báo cáo đối tượng là loại báo cáo cho phép bạn lấy dữ liệu nhân khẩu học và hành vi của đối tượng khán giả, bao gồm độ tuổi, giới tính, khu vực địa lý hoặc sở thích."),
    ("> **Notes** • The data in audience reports is not real-time data. There is 10-12 hours of processing latency for audience data. • Running audience reports in CHUNK mode (`query_mode`= `CHUNK`) is not supported. You can only run synchronous basic reports in CHUNK mode. • We have optimized reporting performance for audience reports with the dimension of `behavior_id` via [/report/integrated/get/](../12-api-reference/58-reporting.md#doc-1740302848100353) (without `order_field` and `enable_total_metrics` parameters). This optimization can increase the number of queried IDs to 2000. Please note that the first request may take a long time to generate responses. However, subsequent requests with the same query parameters but different page numbers can be returned quickly.\nCurrently, this optimization is currently an allowlist-only feature. If you would like to access it, please contact your TikTok representative. Once you are on the allowlist, there is no need to add a new request parameter, as we will automatically enable it in the downstream.",
     "> **Lưu ý:** • Dữ liệu trong báo cáo đối tượng không phải là dữ liệu thời gian thực. Độ trễ xử lý dữ liệu đối tượng khoảng 10-12 giờ. • Không hỗ trợ chạy báo cáo đối tượng ở chế độ CHUNK (`query_mode`= `CHUNK`). Bạn chỉ có thể chạy báo cáo cơ bản đồng bộ ở chế độ CHUNK. • Chúng tôi đã tối ưu hóa hiệu năng báo cáo cho báo cáo đối tượng với chiều dữ liệu `behavior_id` qua [/report/integrated/get/](../12-api-reference/58-reporting.md#doc-1740302848100353) (không kèm tham số `order_field` và `enable_total_metrics`). Tối ưu hóa này có thể tăng số lượng ID truy vấn lên tới 2000. Xin lưu ý rằng yêu cầu đầu tiên có thể mất nhiều thời gian hơn để trả về phản hồi. Tuy nhiên, các yêu cầu tiếp theo với cùng tham số truy vấn nhưng khác số trang sẽ được phản hồi rất nhanh chóng.\nHiện tại, tính năng tối ưu hóa này chỉ áp dụng cho tài khoản trong danh sách cho phép (allowlist). Nếu muốn truy cập, vui lòng liên hệ đại diện TikTok của bạn. Sau khi được duyệt, bạn không cần thêm tham số yêu cầu mới nào vì hệ thống sẽ tự động kích hoạt phía dưới."),
    ("Lifetime metrics for audience reports are not available in v1.3.",
     "Chỉ số trọn đời (lifetime metrics) cho báo cáo đối tượng hiện chưa hỗ trợ trong phiên bản API v1.3."),
    ("**1. Query the overall age distribution of the audience within a period of time, sorted in Sắp xếp tăng dần (ASC) of spend.**",
     "**1. Truy vấn phân bổ độ tuổi tổng thể của đối tượng khán giả trong một khoảng thời gian, sắp xếp tăng dần (ASC) theo chi tiêu (spend).**"),
    ("**2. Query the region distribution of all undeleted ad groups under certain campaigns over a period of time.**",
     "**2. Truy vấn phân bổ khu vực địa lý của tất cả các nhóm quảng cáo chưa bị xóa thuộc các chiến dịch nhất định trong một khoảng thời gian.**"),

    # Section 3: Supported dimensions for Audience
    (">  **Note:** Querying UV metrics with audience dimensions is not supported in asynchronous reports. Please query UV metrics without audience dimensions or audience dimensions without UV metrics in asynchronous reports instead. UV metrics include \"average_frequency\", \"frequency\", and \"reach\".",
     "> **Lưu ý:** Không hỗ trợ truy vấn các chỉ số UV (Unique Visitors) cùng với các chiều dữ liệu đối tượng trong báo cáo không đồng bộ. Vui lòng truy vấn các chỉ số UV mà không kèm chiều đối tượng, hoặc truy vấn chiều đối tượng mà không kèm chỉ số UV trong báo cáo không đồng bộ. Các chỉ số UV bao gồm \"average_frequency\", \"frequency\" và \"reach\"."),
    ("## Dimension grouping rules\nThe grouping can be **one** audience dimension (**required**), **one** ID dimension *(Không bắt buộc)*, and **one** time dimension *(Không bắt buộc)*. You cannot have more than one dimension of the same type in one request. For example, you cannot group by `age` and `gender` at the same time. The grouping rules for dimensions are detailed as follows:",
     "## Quy tắc nhóm chiều dữ liệu (Dimension grouping rules)\nNhóm kết hợp có thể gồm **một** chiều đối tượng (**bắt buộc**), **một** chiều ID *(Không bắt buộc)*, và **một** chiều thời gian *(Không bắt buộc)*. Bạn không thể có nhiều hơn một chiều cùng loại trong một yêu cầu. Ví dụ: bạn không thể nhóm theo cả `age` và `gender` cùng một lúc. Các quy tắc nhóm chiều dữ liệu chi tiết như sau:"),
    ("- Special scenarios: \n\t- If `advertiser_ids` is specified via [/report/task/create/](../12-api-reference/58-reporting.md#doc-1740302766489602) (POST method), the grouping can be **one** audience dimension (**required**), **one or two** ID dimensions (required), and **one** time dimension *(Không bắt buộc)*. For example, `dimensions` can be [\"country_code\",\"advertiser_id\",\"campaign_id\",\"stat_time_day\"].\n\t- If `service_type` is set to `RESERVATION`, the grouping can be **one** audience dimension (**required**), **one** ID dimension *(Không bắt buộc)*, and **one** time dimension *(Không bắt buộc)*. \n\t- If `service_type` is set to `RESERVATION` and `data_level` is `AUCTION_AD`, `dimensions` must contain `ad_id`.",
     "- Các trường hợp đặc biệt:\n\t- Nếu `advertiser_ids` được chỉ định qua [/report/task/create/](../12-api-reference/58-reporting.md#doc-1740302766489602) (phương thức POST), nhóm kết hợp có thể gồm **một** chiều đối tượng (**bắt buộc**), **một hoặc hai** chiều ID (bắt buộc) và **một** chiều thời gian *(Không bắt buộc)*. Ví dụ: `dimensions` có thể là [\"country_code\",\"advertiser_id\",\"campaign_id\",\"stat_time_day\"].\n\t- Nếu `service_type` được đặt thành `RESERVATION`, nhóm kết hợp có thể gồm **một** chiều đối tượng (**bắt buộc**), **một** chiều ID *(Không bắt buộc)* và **một** chiều thời gian *(Không bắt buộc)*.\n\t- Nếu `service_type` được đặt thành `RESERVATION` và `data_level` là `AUCTION_AD`, `dimensions` bắt buộc phải chứa `ad_id`."),
    ("* The following dimensions cannot be used with any time dimension. \n  * interest_category\n  * interest_category_tier2\n  * interest_category_tier3\n  * interest_category_tier4\n  * device_brand_id",
     "* Các chiều dữ liệu sau đây không thể sử dụng cùng với bất kỳ chiều thời gian nào:\n  * interest_category\n  * interest_category_tier2\n  * interest_category_tier3\n  * interest_category_tier4\n  * device_brand_id"),
    ("* In synchronous audience reports, `behavior_id` can be used with `stat_time_day` to retrieve the reporting data of up to 5,000 ads, although in all other synchronous reports you can retrieve the reporting data of up to 20,000 ads.\n* Age and gender cannot be grouped together. \n* Country and region cannot be grouped together. \n* Audience dimensions cannot be grouped with secondary placement dimensions (`placement` + `secondary_placement`).",
     "* Trong báo cáo đối tượng đồng bộ, `behavior_id` có thể dùng cùng với `stat_time_day` để truy xuất dữ liệu báo cáo của tối đa 5.000 quảng cáo, mặc dù trong tất cả các báo cáo đồng bộ khác bạn có thể truy xuất dữ liệu báo cáo lên tới 20.000 quảng cáo.\n* Độ tuổi (Age) và Giới tính (Gender) không thể nhóm chung với nhau.\n* Quốc gia (Country) và Khu vực (Region) không thể nhóm chung với nhau.\n* Chiều đối tượng không thể nhóm chung với các chiều vị trí hiển thị phụ (`placement` + `secondary_placement`)."),

    # Section 4: Attribute metrics intro
    ("Attribute metrics, such as ad group names and promotion types, are basic attributes of your campaigns, ad groups or ads. Attribute metrics are Chỉ hợp lệ khi an ID type of dimension is used.",
     "Các chỉ số thuộc tính (Attribute metrics), chẳng hạn như tên nhóm quảng cáo và loại quảng bá, là các thuộc tính cơ bản của chiến dịch, nhóm quảng cáo hoặc quảng cáo. Chỉ số thuộc tính chỉ hợp lệ khi sử dụng một chiều dữ liệu loại ID."),
    ("Basic data metrics are data about spend and performance of your ads.",
     "Các chỉ số dữ liệu cơ bản (Basic data metrics) là dữ liệu về chi phí và hiệu suất phân phối quảng cáo của bạn."),
    ("Engagement metrics, such as the number of likes and comments, are data about how people interact with your ads.",
     "Các chỉ số tương tác (Engagement metrics), chẳng hạn như số lượt thích và bình luận, là dữ liệu về cách người dùng tương tác với quảng cáo của bạn."),
    ("> **Note:** \n> The only [audience dimensions](bao-cao-p3.md#doc-1751454103714818) supported for Attribution metrics in audience reports are `placement` and `ad_type`.",
     "> **Lưu ý:** \n> Các [chiều đối tượng](bao-cao-p3.md#doc-1751454103714818) duy nhất được hỗ trợ cho các chỉ số Phân bổ (Attribution metrics) trong báo cáo đối tượng là `placement` và `ad_type`."),
    ("Other than [the same filters that are supported in basic reports](bao-cao-p3.md#doc-1751443975608321), audience reports also support the following filters.",
     "Ngoài [các bộ lọc được hỗ trợ trong báo cáo cơ bản](bao-cao-p3.md#doc-1751443975608321), báo cáo đối tượng cũng hỗ trợ thêm các bộ lọc dưới đây."),
    ("> **Note:** \n> - In asynchronous audience reports, the only supported filter fields are `campaign_ids`, `adgroup_ids`, and `ad_ids`.\n> - Audience reports now include data for Auction ads, Reach & Frequency ads, and TopView ads. To filter data for a specific buying type, use [/report/integrated/get/](../12-api-reference/58-reporting.md#doc-1740302848100353) to run an audience report. Within the filtering object, specify the `buying_type` field and enter the values of either `AUCTION`, `RESERVATION_TOP_VIEW`, or `RESERVATION_RF`.\n> - For TopView ads, cost-related metrics for audience breakdown will only include data for ads delivered after January 18th, 2024.\n> - The reporting data for [Product GMV max ads](https://ads.tiktok.com/help/article/how-to-create-product-gmv-max-ads-in-seller-center) and LIVE GMV max ads created from TikTok Shop is excluded from synchronous Auction basic reports, audience reports, playable ad reports, and DSA reports. Shopping Ads created via API or TikTok Ads Manager are not affected.",
     "> **Lưu ý:** \n> - Trong báo cáo đối tượng không đồng bộ, các trường bộ lọc duy nhất được hỗ trợ là `campaign_ids`, `adgroup_ids` và `ad_ids`.\n> - Báo cáo đối tượng hiện bao gồm dữ liệu cho Quảng cáo Đấu thầu, Quảng cáo Tiếp cận & Tần suất và Quảng cáo TopView. Để lọc dữ liệu theo loại hình mua cụ thể, hãy sử dụng [/report/integrated/get/](../12-api-reference/58-reporting.md#doc-1740302848100353) để chạy báo cáo đối tượng. Trong đối tượng bộ lọc, chỉ định trường `buying_type` và nhập một trong các giá trị `AUCTION`, `RESERVATION_TOP_VIEW` hoặc `RESERVATION_RF`.\n> - Đối với quảng cáo TopView, các chỉ số liên quan đến chi phí phân tích theo đối tượng sẽ chỉ bao gồm dữ liệu cho các quảng cáo được phân phối sau ngày 18 tháng 1 năm 2024.\n> - Dữ liệu báo cáo cho [quảng cáo Product GMV Max](https://ads.tiktok.com/help/article/how-to-create-product-gmv-max-ads-in-seller-center) và quảng cáo LIVE GMV Max tạo từ TikTok Shop sẽ bị loại trừ khỏi các báo cáo cơ bản Đấu thầu đồng bộ, báo cáo đối tượng, báo cáo quảng cáo tương tác và báo cáo DSA. Quảng cáo Mua sắm tạo qua API hoặc TikTok Ads Manager không bị ảnh hưởng."),

    # Playable ad reports
    ("> **Note:**  • Playable ads report returns data of playable creatives. `data_level` is not required in your request.  • Running playable ad reports in CHUNK mode (`query_mode`= `CHUNK`) is not supported. You can only run synchronous basic reports in CHUNK mode.",
     "> **Lưu ý:** • Báo cáo quảng cáo tương tác (Playable ad reports) trả về dữ liệu của các mẫu nội dung sáng tạo có thể chơi được. Tham số `data_level` không bắt buộc trong yêu cầu của bạn. • Không hỗ trợ chạy báo cáo quảng cáo tương tác ở chế độ CHUNK (`query_mode`= `CHUNK`). Bạn chỉ có thể chạy báo cáo cơ bản đồng bộ ở chế độ CHUNK."),
    ("Breakdown by time or location is not supported when querying for lifetime metrics, so when `query_lifetime` = `True` , `dimensions` cannot contain `stat_time_day`, `stat_time_hour`, or `country_code`.",
     "Không hỗ trợ phân tách theo thời gian hoặc vị trí khi truy vấn các chỉ số trọn đời (lifetime metrics), vì vậy khi `query_lifetime` = `True`, tham số `dimensions` không được chứa `stat_time_day`, `stat_time_hour`, hoặc `country_code`."),
    ("You can use lifetime metrics in synchronous playable ad reports only, because playable ad reports do not support the asynchronous mode.",
     "Bạn chỉ có thể sử dụng các chỉ số trọn đời trong báo cáo quảng cáo tương tác đồng bộ, vì báo cáo quảng cáo tương tác không hỗ trợ chế độ không đồng bộ."),
    ("**1. Query data of the playable ads whose spend are between 0 and 100 in a certain period of time.**",
     "**1. Truy vấn dữ liệu của các quảng cáo tương tác có chi tiêu nằm trong khoảng từ 0 đến 100 trong một khoảng thời gian nhất định.**"),
    ("**2. Query data of each playable ads in different countries during a certain period of time.**",
     "**2. Truy vấn dữ liệu của từng quảng cáo tương tác tại các quốc gia khác nhau trong một khoảng thời gian nhất định.**"),
    ("Attribute metrics, such as playable names and playable ids, are basic attributes of your playable ads. Attribute metrics are supported only when dimensions contain `playable_id`.",
     "Các chỉ số thuộc tính (Attribute metrics), chẳng hạn như tên tài nguyên tương tác và ID tài nguyên tương tác, là các thuộc tính cơ bản của quảng cáo tương tác. Chỉ số thuộc tính chỉ được hỗ trợ khi `dimensions` chứa `playable_id`."),
    ("In-App event metrics are data about in-app conversion events.",
     "Các chỉ số sự kiện trong ứng dụng (In-App event metrics) là dữ liệu về các sự kiện chuyển đổi diễn ra trong ứng dụng."),
    ("When you use the `IN` filter type, `filter_value` must be a valid JSON array of string. E.g. `\"[123,456,789]\"`.",
     "Khi bạn sử dụng kiểu lọc `IN`, giá trị `filter_value` phải là một chuỗi mảng JSON hợp lệ. Ví dụ: `\"[123,456,789]\"`."),

    # DSA reports
    ("> **Note:**  • Running asynchronous DSA reports for Video Shopping Ads with product source as catalog is currently an allowlist-only feature. If you would like to access it, please contact your TikTok representative.  • Running DSA reports in CHUNK mode (`query_mode`= `CHUNK`) is not supported. You can only run synchronous basic reports in CHUNK mode.",
     "> **Lưu ý:** • Tính năng chạy báo cáo DSA không đồng bộ cho Video Shopping Ads có nguồn sản phẩm là danh mục (catalog) hiện chỉ dành cho tài khoản trong danh sách cho phép (allowlist). Nếu bạn muốn truy cập, vui lòng liên hệ đại diện TikTok của bạn. • Không hỗ trợ chạy báo cáo DSA ở chế độ CHUNK (`query_mode`= `CHUNK`). Bạn chỉ có thể chạy báo cáo cơ bản đồng bộ ở chế độ CHUNK."),
    ("Lifetime metrics for DSA reports are not available in v1.3.",
     "Chỉ số trọn đời (lifetime metrics) cho báo cáo DSA hiện chưa hỗ trợ trong phiên bản API v1.3."),
    ("**1. Query data of catalog ads whose spend are between 0 and 100 in a certain period of time.**",
     "**1. Truy vấn dữ liệu của quảng cáo danh mục có chi tiêu từ 0 đến 100 trong một khoảng thời gian nhất định.**"),
    ("**2. Query data of each dynamic showcase ads in different countries during a certain period of time.**",
     "**2. Truy vấn dữ liệu của từng quảng cáo trưng bày động (DSA) tại các quốc gia khác nhau trong một khoảng thời gian nhất định.**"),

    # Reservation ad reports
    ("Reservation ad reports are a type of report from which you can get data about reservation ads. Reservation ads include Reach & Frequency (R&F) ads and TopView ads.",
     "Báo cáo quảng cáo đặt trước là loại báo cáo cho phép bạn lấy dữ liệu về các quảng cáo đặt trước. Quảng cáo đặt trước bao gồm Quảng cáo Tiếp cận & Tần suất (R&F) và Quảng cáo TopView."),
    ("> **Note:** \n> As of January 18th, 2024, reservation ad reports are deprecated. Reservation ads are now fully supported in [Basic reports](bao-cao-p1.md#doc-1738864915188737) and [Audience reports](bao-cao-p3.md#doc-1738864928947201).",
     "> **Lưu ý:** \n> Kể từ ngày 18 tháng 1 năm 2024, báo cáo quảng cáo đặt trước đã ngừng hỗ trợ (deprecated). Quảng cáo đặt trước hiện được hỗ trợ đầy đủ trong [Báo cáo cơ bản](bao-cao-p1.md#doc-1738864915188737) và [Báo cáo đối tượng](bao-cao-p3.md#doc-1738864928947201)."),
    ("Lifetime metrics for reservation ad reports are not available in v1.3.",
     "Chỉ số trọn đời cho báo cáo quảng cáo đặt trước không khả dụng trong v1.3."),
    ("**1. Query data of reservation ads in a certain period of time.**",
     "**1. Truy vấn dữ liệu của quảng cáo đặt trước trong một khoảng thời gian nhất định.**"),

    # Business Center reports
    ("Business Center reports are a type of report from which you can get advertising data at the Business Center level.",
     "Báo cáo Business Center là loại báo cáo cho phép bạn lấy dữ liệu quảng cáo tổng hợp ở cấp độ Trung tâm Doanh nghiệp (Business Center)."),
    ("See [here](bao-cao-p3.md#doc-1775747465089026) for supported dimensions of Business Center reports.",
     "Xem [tại đây](bao-cao-p3.md#doc-1775747465089026) về các chiều dữ liệu được hỗ trợ của báo cáo Business Center."),
    ("See [here](bao-cao-p3.md#doc-1775747492072449) for supported metrics for a dimension in Business Center reports.",
     "Xem [tại đây](bao-cao-p3.md#doc-1775747492072449) về các chỉ số hỗ trợ theo chiều dữ liệu trong báo cáo Business Center."),
    ("See [here](bao-cao-p3.md#doc-1751454103714818) for supported dimensions of audience reports.",
     "Xem [tại đây](bao-cao-p3.md#doc-1751454103714818) về các chiều dữ liệu được hỗ trợ của báo cáo đối tượng."),
    ("See [here](bao-cao-p3.md#doc-1751454162042882) for supported metrics of audience reports.",
     "Xem [tại đây](bao-cao-p3.md#doc-1751454162042882) về các chỉ số được hỗ trợ của báo cáo đối tượng."),
    ("See [here](bao-cao-p3.md#doc-1751454172429314) for supported filters of audience reports.",
     "Xem [tại đây](bao-cao-p3.md#doc-1751454172429314) về các bộ lọc được hỗ trợ của báo cáo đối tượng."),
    ("See [here](bao-cao-p3.md#doc-1751617879104514) for supported dimensions of playable ad reports.",
     "Xem [tại đây](bao-cao-p3.md#doc-1751617879104514) về các chiều dữ liệu được hỗ trợ của báo cáo quảng cáo tương tác."),
    ("See [here](bao-cao-p3.md#doc-1751617882108929) for supported metrics of playable ad reports.",
     "Xem [tại đây](bao-cao-p3.md#doc-1751617882108929) về các chỉ số được hỗ trợ của báo cáo quảng cáo tương tác."),
    ("See [here](bao-cao-p3.md#doc-1751617884206210) for supported filters of playable ad reports.",
     "Xem [tại đây](bao-cao-p3.md#doc-1751617884206210) về các bộ lọc được hỗ trợ của báo cáo quảng cáo tương tác."),
    ("See [here](bao-cao-p3.md#doc-1751625287345154) for supported dimensions of DSA reports.",
     "Xem [tại đây](bao-cao-p3.md#doc-1751625287345154) về các chiều dữ liệu được hỗ trợ của báo cáo DSA."),
    ("See [here](bao-cao-p3.md#doc-1751625293044737) for supported metrics of DSA reports.",
     "Xem [tại đây](bao-cao-p3.md#doc-1751625293044737) về các chỉ số được hỗ trợ của báo cáo DSA."),
    ("See [here](bao-cao-p3.md#doc-1751625296192514) for supported filters of DSA reports.",
     "Xem [tại đây](bao-cao-p3.md#doc-1751625296192514) về các bộ lọc được hỗ trợ của báo cáo DSA."),
    ("See [here](bao-cao-p3.md#doc-1751631253780482) for supported dimensions of reservation ad reports.",
     "Xem [tại đây](bao-cao-p3.md#doc-1751631253780482) về các chiều dữ liệu được hỗ trợ của báo cáo quảng cáo đặt trước."),
    ("See [here](bao-cao-p3.md#doc-1751631257050114) for supported metrics of reservation ad reports.",
     "Xem [tại đây](bao-cao-p3.md#doc-1751631257050114) về các chỉ số được hỗ trợ của báo cáo quảng cáo đặt trước."),
    ("See [here](bao-cao-p3.md#doc-1751631259350017) for supported filters of reservation ad reports.",
     "Xem [tại đây](bao-cao-p3.md#doc-1751631259350017) về các bộ lọc được hỗ trợ của báo cáo quảng cáo đặt trước.")
]

for o, n in replacements:
    if o in text:
        text = text.replace(o, n)
    else:
        print(f"NOT FOUND: {o[:40]}...")

with open(path, "w", encoding="utf-8") as f:
    f.write(text)

print("Updated finalize_u120.py")
