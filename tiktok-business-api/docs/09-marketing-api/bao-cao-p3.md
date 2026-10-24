# Hướng dẫn Báo cáo (Reporting) — phần 3/4

> Phân hệ: guide:Marketing API/Reporting.
> Tài liệu biên dịch kỹ thuật chi tiết theo chuẩn TikTok Business API v1.3.

---

## Mục lục điều hướng
- [1. Các bộ lọc được hỗ trợ (Supported filters) (#doc-1751443975608321)](#doc-1751443975608321)
- [2. Báo cáo đối tượng (Audience reports) (#doc-1738864928947201)](#doc-1738864928947201)
- [3. Các chiều dữ liệu được hỗ trợ (Supported dimensions) (#doc-1751454103714818)](#doc-1751454103714818)
- [4. Chỉ số hỗ trợ theo chiều dữ liệu trong báo cáo đối tượng (#doc-1762404685488130)](#doc-1762404685488130)
- [5. Các chỉ số được hỗ trợ (Supported metrics) (#doc-1751454162042882)](#doc-1751454162042882)
- [6. Các bộ lọc được hỗ trợ (Supported filters) (#doc-1751454172429314)](#doc-1751454172429314)
- [7. Báo cáo quảng cáo tương tác (Playable ad reports) (#doc-1738864940608513)](#doc-1738864940608513)
- [8. Các chiều dữ liệu được hỗ trợ (Supported dimensions) (#doc-1751617879104514)](#doc-1751617879104514)
- [9. Chỉ số hỗ trợ theo chiều dữ liệu trong báo cáo quảng cáo tương tác (#doc-1762405483224065)](#doc-1762405483224065)
- [10. Các chỉ số được hỗ trợ (Supported metrics) (#doc-1751617882108929)](#doc-1751617882108929)
- [11. Các bộ lọc được hỗ trợ (Supported filters) (#doc-1751617884206210)](#doc-1751617884206210)
- [12. Báo cáo quảng cáo mua sắm động DSA (DSA reports) (#doc-1738864960144385)](#doc-1738864960144385)
- [13. Các chiều dữ liệu được hỗ trợ (Supported dimensions) (#doc-1751625287345154)](#doc-1751625287345154)
- [14. Các chỉ số được hỗ trợ (Supported metrics) (#doc-1751625293044737)](#doc-1751625293044737)
- [15. Các bộ lọc được hỗ trợ (Supported filters) (#doc-1751625296192514)](#doc-1751625296192514)
- [16. (Không còn hỗ trợ) Báo cáo quảng cáo đặt trước (Reservation ad reports) (#doc-1738864971714562)](#doc-1738864971714562)
- [17. (Không còn hỗ trợ) Các chiều dữ liệu được hỗ trợ (#doc-1751631253780482)](#doc-1751631253780482)
- [18. (Không còn hỗ trợ) Chỉ số theo chiều dữ liệu trong báo cáo quảng cáo đặt trước (#doc-1762405922636802)](#doc-1762405922636802)
- [19. (Không còn hỗ trợ) Các chỉ số được hỗ trợ (#doc-1751631257050114)](#doc-1751631257050114)
- [20. (Không còn hỗ trợ) Các bộ lọc được hỗ trợ (#doc-1751631259350017)](#doc-1751631259350017)
- [21. Báo cáo Business Center (Business Center reports) (#doc-1775747432712194)](#doc-1775747432712194)
- [22. Các chiều dữ liệu được hỗ trợ (Supported dimensions) (#doc-1775747465089026)](#doc-1775747465089026)
- [23. Chỉ số theo chiều dữ liệu trong báo cáo Business Center (#doc-1775747492072449)](#doc-1775747492072449)

---

<a id="doc-1751443975608321"></a>
<!-- doc_id: 1751443975608321 -->
<!-- doc_id: 1751443975608321 -->
# Các bộ lọc được hỗ trợ (Supported filters)
> Đường dẫn: Marketing API > Reporting > Guides > Report types > Basic reports > Supported filters
Bạn có thể sử dụng các bộ lọc sau để thu hẹp phạm vi kết quả báo cáo.

Vui lòng đọc kỹ các lưu ý dưới đây trước khi bắt đầu:

* Khi bạn truyền nhiều bộ lọc, các điều kiện lọc sẽ kết hợp theo quan hệ logic `AND` (đồng thời thỏa mãn).
* Khi sử dụng kiểu lọc `IN`, giá trị `filter_value` phải là chuỗi JSON danh sách hợp lệ. Ví dụ: `"[\"ID1\",\"ID2\",\"ID3\"]"`.
* Khi sử dụng kiểu lọc `BETWEEN`, giá trị `filter_value` phải là mảng JSON chứa 2 phần tử chuỗi ngày giờ (bắt đầu và kết thúc). Ví dụ: `"[\"2022-02-24 11:57:51\",\"2022-03-24 11:57:51\"]"`.
* Xem ví dụ gọi lệnh cURL mẫu tại [Báo cáo cơ bản - Các trường hợp sử dụng](bao-cao-p1.md#doc-1738864915188737).

> **Note:** 
> - Nếu trường bộ lọc `field_name` được cung cấp và `data_level` không khớp, hệ thống sẽ trả về lỗi: "Invalid value for filter field: xxxx is not supported". Ví dụ: nếu `data_level` là `AUCTION_AD`, bạn chỉ có thể đặt `field_name` thành trường bộ lọc ở cấp quảng cáo (chẳng hạn như `ad_ids`).
> - Trong báo cáo cơ bản không đồng bộ (asynchronous basic reports), các trường bộ lọc duy nhất được hỗ trợ là `campaign_ids`, `adgroup_ids` và `ad_ids`.
> - Báo cáo cơ bản hiện bao gồm dữ liệu cho Quảng cáo Đấu thầu (Auction ads), Quảng cáo Tiếp cận & Tần suất (Reach & Frequency ads) và Quảng cáo TopView. Để lọc dữ liệu theo loại hình mua cụ thể, hãy sử dụng [/report/integrated/get/](../12-api-reference/58-reporting.md#doc-1740302848100353) để chạy báo cáo cơ bản. Trong đối tượng bộ lọc, chỉ định trường `buying_type` và nhập một trong các giá trị `AUCTION`, `RESERVATION_TOP_VIEW` hoặc `RESERVATION_RF`.
> - Đối với quảng cáo TopView, các chỉ số liên quan đến chi phí ở cấp quảng cáo và các chỉ số chi phí phân tích theo đối tượng sẽ chỉ bao gồm dữ liệu cho các quảng cáo được phân phối sau ngày 18 tháng 1 năm 2024.
> - Dữ liệu báo cáo cho [quảng cáo Product GMV Max](https://ads.tiktok.com/help/article/how-to-create-product-gmv-max-ads-in-seller-center) và quảng cáo LIVE GMV Max tạo từ TikTok Shop sẽ bị loại trừ khỏi các báo cáo cơ bản Đấu thầu đồng bộ, báo cáo đối tượng, báo cáo quảng cáo tương tác và báo cáo DSA. Quảng cáo Mua sắm (Shopping Ads) được tạo qua API hoặc TikTok Ads Manager không bị ảnh hưởng.

| Bộ lọc (Filter Field) | Kiểu lọc hỗ trợ (Supported Filter Types) | Cấp quảng cáo hỗ trợ (Supported Advertising Levels) | Ghi chú chi tiết (Notes) |
|---|---|---|---|
| campaign_ids | IN | Chiến dịch / Nhóm quảng cáo / Quảng cáo | Danh sách ID chiến dịch, bạn có thể truyền tối đa 100 `campaign_id` khi dùng bộ lọc này. Ví dụ giá trị lọc: `"[123,456,789]"`. |
| campaign_automation_type | IN | Chiến dịch / Nhóm quảng cáo / Quảng cáo | Loại tự động hóa chiến dịch (Campaign automation type). ⏎ Các giá trị enum hỗ trợ: • `MANUAL`: Chiến dịch thủ công. • `SMART_PLUS`: Chiến dịch Smart+. • `UPGRADED_SMART_PLUS`: Chiến dịch Upgraded Smart+. Để tìm hiểu thêm về Chiến dịch Upgraded Smart+, xem [Chiến dịch Upgraded Smart+](quan-ly-chien-dich-p1.md#doc-1853452461203458). • Khi `campaign_automation_type` là `UPGRADED_SMART_PLUS`, trường `ad_id_v2` trả về là ID của Quảng cáo Upgraded Smart+. |
| campaign_system_origins | IN | Chiến dịch / Nhóm quảng cáo / Quảng cáo | Nguồn gốc chiến dịch (nguồn chiến dịch). ⏎ Các giá trị enum hỗ trợ: • `PROMOTE`: Chiến dịch là chiến dịch Promote được tạo qua ứng dụng TikTok trên thiết bị di động. • `TT_ADS_PLATFORM`: Chiến dịch là chiến dịch thông thường không phải Promote được tạo qua API hoặc trên TikTok Ads Manager. Giá trị mặc định: `"[\"TT_ADS_PLATFORM\"]"`. ⏎ Để tìm hiểu thêm về các chiều dữ liệu, chỉ số và bộ lọc được hỗ trợ cho quảng cáo Promote, xem [Chiến dịch Promote](quan-ly-chien-dich-p1.md#doc-1785880454546433). ⏎ **Lưu ý**: • Bộ lọc này chỉ được hỗ trợ trong báo cáo cơ bản đồng bộ. • Trong báo cáo cơ bản không đồng bộ, kết quả mặc định bao gồm dữ liệu của quảng cáo Promote. |
| adgroup_ids | IN | Nhóm quảng cáo / Quảng cáo | Danh sách ID nhóm quảng cáo, bạn có thể truyền tối đa 100 `adgroup_id` khi dùng bộ lọc này. |
| ad_ids_v2 | IN | Ad | • Các loại ID bạn có thể lọc bao gồm: • ID của Quảng cáo thủ công. • ID của **Quảng cáo** Upgraded Smart+ (**Nhóm tài sản - Asset Group**). • Bạn cần đặt `data_level` thành `AUCTION_AD` và đưa `ad_id_v2` vào `dimensions`. • Bạn có thể chỉ định tối đa 100 giá trị khi dùng bộ lọc này. • Bạn không thể sử dụng bộ lọc này cùng với chiều dữ liệu `ad_id` hoặc bộ lọc `ad_ids`. |
| ad_ids | IN | Ad | Danh sách ID quảng cáo, bạn có thể truyền tối đa 100 `ad_id` khi dùng bộ lọc này. |
| campaign_status | IN | Campaign | Trạng thái chiến dịch (Campaign status). Để xem danh sách giá trị enum, xem [Enum - Quản lý quảng cáo - Trạng thái chính](../15-appendix/phu-luc-p1.md#doc-1737174886619138). ⏎ **Lưu ý**: Nếu không đặt, trường bộ lọc này sẽ mặc định là `STATUS_NOT_DELETE` trong báo cáo cơ bản đồng bộ. |
| adgroup_status | IN | Ad group | Trạng thái nhóm quảng cáo (Ad Group status). Để xem danh sách giá trị enum, xem [Enum - Quản lý quảng cáo - Trạng thái chính](../15-appendix/phu-luc-p1.md#doc-1737174886619138). ⏎ **Lưu ý**: Nếu không đặt, trường bộ lọc này sẽ mặc định là `STATUS_NOT_DELETE` trong báo cáo cơ bản đồng bộ. |
| ad_status | IN | Ad | Trạng thái quảng cáo (Ad Status). Để xem danh sách giá trị enum, xem [Enum - Quản lý quảng cáo - Trạng thái chính](../15-appendix/phu-luc-p1.md#doc-1737174886619138). ⏎ **Lưu ý**: Nếu không đặt, trường bộ lọc này sẽ mặc định là `STATUS_NOT_DELETE` trong báo cáo cơ bản đồng bộ. |
| campaign_label_ids | IN, NOT_IN | Chiến dịch / Nhóm quảng cáo / Quảng cáo | Danh sách ID nhãn chiến dịch. ⏎ Kích thước tối đa: 50. ⏎ Mỗi ID nhãn phải là một chuỗi số 19 chữ số. ⏎ **Lưu ý**: Bộ lọc này chỉ được hỗ trợ trong báo cáo đồng bộ. |
| campaign_label_names | CONTAIN_ANY_OF | Chiến dịch / Nhóm quảng cáo / Quảng cáo | Danh sách tên nhãn chiến dịch. ⏎ Hỗ trợ khớp mờ (fuzzy matching). ⏎ Kích thước tối đa: 10. ⏎ **Lưu ý**: Bộ lọc này chỉ được hỗ trợ trong báo cáo đồng bộ. |
| campaign_label_types | IN, NOT_IN | Chiến dịch / Nhóm quảng cáo / Quảng cáo | Danh sách loại nhãn chiến dịch. ⏎ Các giá trị enum hỗ trợ: • `GENERAL`: Nhãn chung. • `MARKETING_EVENT`: Nhãn sự kiện tiếp thị. ⏎ **Lưu ý**: Bộ lọc này chỉ được hỗ trợ trong báo cáo đồng bộ. |
| objective_type | IN | Chiến dịch / Nhóm quảng cáo / Quảng cáo | Mục tiêu quảng cáo (Advertising Objective). ⏎ Các giá trị enum hỗ trợ: `APP_PROMOTION`, `APP_INSTALL`, `CONVERSIONS`, `REACH`, `BRAND_CONSIDERATION`, `TRAFFIC`, `VIDEO_VIEWS`, `PRODUCT_SALES`, `ENGAGEMENT`, `LEAD_GENERATION`, `CATALOG_SALES`, `SHOP_PURCHASES`. |
| billing_event | IN | Chiến dịch / Nhóm quảng cáo / Quảng cáo | Sự kiện tính phí (Billing Event). Để xem danh sách giá trị enum, xem [Enum - Sự kiện tính phí](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| age | IN | Chiến dịch / Nhóm quảng cáo / Quảng cáo | Nhóm tuổi mục tiêu. ⏎ Để xem danh sách giá trị enum, xem [Enum - Nhóm tuổi mục tiêu](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| gender | IN | Chiến dịch / Nhóm quảng cáo / Quảng cáo | Gender that you want to target. ⏎ Enum values：`GENDER_FEMALE`, `GENDER_MALE` |
| dpa_target_audience_type | IN | Chiến dịch / Nhóm quảng cáo / Quảng cáo | The audience type for DPA. Các giá trị enum hỗ trợ: `RETARGETING`, `PROSPECTING`. This filter can only be used in synchronous reports. |
| buying_type | IN | Chiến dịch / Nhóm quảng cáo / Quảng cáo | Loại hình mua (Buying type). ⏎ Các giá trị enum hỗ trợ: `AUCTION`, `RESERVATION_TOP_VIEW`, `RESERVATION_RF`. |
| is_cbo_enabled | IN | Chiến dịch / Nhóm quảng cáo / Quảng cáo | Campaign Budget Optimization. ⏎ Các giá trị enum hỗ trợ: `CBO_CAMPAIGN`, `NON_CBO_CAMPAIGN`. |
| app_promotion_type | IN | Chiến dịch / Nhóm quảng cáo / Quảng cáo | The app promotion type. ⏎ Các giá trị enum hỗ trợ: ⏎ `APP_INSTALL`: App install. Get new users to install your app. ⏎ `APP_RETARGETING`: App retargeting. Re-engage existing users to take action in your app. |
| campaign_product_source | IN | Chiến dịch / Nhóm quảng cáo / Quảng cáo | Product source of the campaign. ⏎ Các giá trị enum hỗ trợ: • `CATALOG`: Catalog. •  `STORE`: TikTok Shop, or TikTok Showcase. |
| optimization_goal | IN | Chiến dịch / Nhóm quảng cáo / Quảng cáo | The measurable results you'd like to drive with your ads. See [Enumeration - Optimization Goal](../15-appendix/phu-luc-p1.md#doc-1737174886619138) for enum values. |
| promotion_type | IN | Chiến dịch / Nhóm quảng cáo / Quảng cáo | Promotion type (Optimization location). ⏎ Các giá trị enum hỗ trợ: • `APP`: App. • `WEBSITE`: Landing page. • `INSTANT_FORM`: Instant Form. • `LEAD_GEN_CLICK_TO_TT_DIRECT_MESSAGE`: TikTok direct messages. • `LEAD_GEN_CLICK_TO_SOCIAL_MEDIA_APP_MESSAGE`: Instant messaging apps. • `LEAD_GEN_CLICK_TO_CALL`: Phone call. • `OTHERS`: Others. ⏎ This filter can only be used in synchronous reports. |
| bid_strategy | IN | Chiến dịch / Nhóm quảng cáo / Quảng cáo | Bidding strategy.  Các giá trị enum hỗ trợ: `BID_STRATEGY_COST_CAP`, `BID_STRATEGY_BID_CAP`, `BID_STRATEGY_MAX_CONVERSION` and `BID_STRATEGY_LOWEST_COST`, `BID_STRATEGY_HIGHEST_VALUE`, `BID_STRATEGY_GMV`, `BID_STRATEGY_MINIMUM_ROAS`. |
| delivery_type | IN | Chiến dịch / Nhóm quảng cáo / Quảng cáo | Kiểu phân phối ngân sách (Delivery Type / pacing). ⏎ Các giá trị enum hỗ trợ: `PACING_MODE_SMOOTH`, `PACING_MODE_FAST` |
| ad_entity_type | IN | Chiến dịch / Nhóm quảng cáo / Quảng cáo | Loại quảng cáo (Ad type). ⏎ Các giá trị enum hỗ trợ: ⏎ `VIDEO_SHOPPING_ADS`, `LIVE_SHOPPING_ADS`, `CATALOG_LISTING_ADS`, `PRODUCT_SHOPPING_ADS` |
| identity_type | IN | Chiến dịch / Nhóm quảng cáo / Quảng cáo | Loại danh tính (Identity type). ⏎ Các giá trị enum hỗ trợ: `TT_ACCOUNT`, `CUSTOM_IDENTITY` |
| image_mode | IN | Ad | Định dạng nội dung sáng tạo (Creative format). ⏎ Các giá trị enum hỗ trợ: • `IMAGE_MODE_LARGE`：Hình ảnh • `IMAGE_MODE_VIDEO`：Video (16:9) • `IMAGE_MODE_VIDEO_SQUARE`：Video (1:1) • `IMAGE_MODE_VIDEO_VERTICAL`：Video (9:16) • `CAROUSEL_ADS`: Bộ sưu tập hình ảnh xoay vòng (Carousel). ⏎ **Lưu ý**: Bộ lọc này chỉ được hỗ trợ trong báo cáo cơ bản đồng bộ. |
| creative_material_mode | IN | Nhóm quảng cáo / Quảng cáo | Chiến lược phân phối mẫu quảng cáo sáng tạo. Các giá trị enum hỗ trợ: `CUSTOM` (tùy chỉnh), `DYNAMIC` (tự động hóa), `SMART_CREATIVE` (Smart Creative). |
| destination | IN | Ad | Loại trang đích (Destination page type). ⏎ Các giá trị enum hỗ trợ: • `APP`: Trang tải xuống ứng dụng được quảng bá trên Google Play hoặc Apple App Store. Trường `promotion_type` của nhóm quảng cáo tương ứng được đặt thành `APP_ANDROID` hoặc `APP_IOS`. • `TIKTOK_INSTANT_PAGE`: Trang tức thì TikTok (TikTok Instant Pages), bao gồm Trang tùy chỉnh (Custom Page), Biểu mẫu tức thì (Instant Form), Trang hồ sơ ứng dụng (App Profile Page), và Trang sản phẩm tức thì (Instant Product Page). ID trang (`page_id`) của TikTok Instant Page được chỉ định cho quảng cáo. • `WEBSITE`: Trang web. URL trang đích (`landing_page_url`) được chỉ định cho quảng cáo. • `SOCIAL_MEDIA_APP`: URL ứng dụng mạng xã hội. Để tìm hiểu về quảng cáo có thể đặt trang đích là mạng xã hội, xem [Tạo quảng cáo Tìm kiếm khách hàng tiềm năng với loại quảng bá ứng dụng nhắn tin tức thì](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1774482999036930). • `PHONE_CALL`: Số điện thoại. Để tìm hiểu về quảng cáo có thể đặt trang đích là cuộc gọi, xem [Tạo quảng cáo Tìm kiếm khách hàng tiềm năng với loại quảng bá cuộc gọi](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1774482936048641). ⏎ **Lưu ý**: Bộ lọc này chỉ được hỗ trợ trong báo cáo cơ bản đồng bộ. |
| campaign_type | IN | Chiến dịch / Nhóm quảng cáo / Quảng cáo | Loại chiến dịch (The campaign type). Các giá trị enum hỗ trợ: `REGULAR_CAMPAIGN`, `IOS14_CAMPAIGN`, `IOS14_CAMPAIGN_WITH_APP_PROFILE_PAGE`, `IOS14_CAMPAIGN_WITHOUT_APP_PROFILE_PAGE`. |
| creative_campaign_type | IN | Chiến dịch / Nhóm quảng cáo / Quảng cáo | Lọc theo loại chiến dịch Smart+, Search Ads Campaign, hoặc chiến dịch thông thường. ⏎ Các giá trị enum hỗ trợ: • `SMART+`: To filter Smart+ Campaigns. • `SEARCH_CAMPAIGN`: To filter Search Ads Campaigns. • `OTHER`: To filter non-Smart+ non-Search Ads Campaigns. ⏎ If you do not specify this field, you will get all campaigns. ⏎ **Note**: This filter is only supported in synchronous basic reports. |
| create_time | BETWEEN | Chiến dịch / Nhóm quảng cáo / Quảng cáo | Khoảng thời gian tạo của chiều ID được yêu cầu (`campaign_id`/`adgroup_id`/`ad_id`). Giá trị cần là một mảng JSON hợp lệ gồm 2 phần tử chuỗi. Phần tử thứ 1 là thời gian bắt đầu, phần tử thứ 2 là thời gian kết thúc. Ví dụ: `"[\"2022-02-24 11:57:51\",\"2022-03-24 11:57:51\"]"`. Bộ lọc này chỉ có thể sử dụng trong báo cáo đồng bộ. ⏎ Khuyến nghị: Nên chọn khoảng thời gian trong vòng 6 tháng khi áp dụng bộ lọc Thời gian tạo, để đảm bảo tốc độ và tỷ lệ thành công của tác vụ không bị ảnh hưởng. |
| create_time | GREATER_THAN | Chiến dịch / Nhóm quảng cáo / Quảng cáo | Thời gian bắt đầu tạo của chiều ID được yêu cầu (`campaign_id`/`adgroup_id`/`ad_id`). Giá trị ở định dạng `YYYY-MM-DD HH:MM:SS` (múi giờ UTC). Ví dụ: `"2022-02-24 11:57:51"` - các chiều dữ liệu được tạo sau thời điểm này sẽ được trả về. Bộ lọc này chỉ có thể sử dụng trong báo cáo đồng bộ. ⏎ Khuyến nghị: Nên chọn khoảng thời gian trong vòng 6 tháng khi áp dụng bộ lọc Thời gian tạo, để đảm bảo tốc độ và tỷ lệ thành công của tác vụ không bị ảnh hưởng. |
| create_time | LOWER_THAN | Chiến dịch / Nhóm quảng cáo / Quảng cáo | Thời gian kết thúc tạo của chiều ID được yêu cầu (`campaign_id`/`adgroup_id`/`ad_id`). Giá trị ở định dạng `YYYY-MM-DD HH:MM:SS` (múi giờ UTC). Ví dụ: `"2022-02-24 11:57:51"` - các chiều dữ liệu được tạo trước thời điểm này sẽ được trả về. Bộ lọc này chỉ có thể sử dụng trong báo cáo đồng bộ. ⏎ Khuyến nghị: Nên chọn khoảng thời gian trong vòng 6 tháng khi áp dụng bộ lọc Thời gian tạo, để đảm bảo tốc độ và tỷ lệ thành công của tác vụ không bị ảnh hưởng. |

---

<a id="doc-1738864928947201"></a>
<!-- doc_id: 1738864928947201 -->
<!-- doc_id: 1738864928947201 -->
# Báo cáo đối tượng (Audience reports)
> Đường dẫn: Marketing API > Reporting > Guides > Report types > Audience reports
Báo cáo đối tượng là loại báo cáo cho phép bạn lấy dữ liệu nhân khẩu học và hành vi của đối tượng khán giả, bao gồm độ tuổi, giới tính, khu vực địa lý hoặc sở thích.  

> **Lưu ý:** • Dữ liệu trong báo cáo đối tượng không phải là dữ liệu thời gian thực. Độ trễ xử lý dữ liệu đối tượng khoảng 10-12 giờ. • Không hỗ trợ chạy báo cáo đối tượng ở chế độ CHUNK (`query_mode`= `CHUNK`). Bạn chỉ có thể chạy báo cáo cơ bản đồng bộ ở chế độ CHUNK. • Chúng tôi đã tối ưu hóa hiệu năng báo cáo cho báo cáo đối tượng với chiều dữ liệu `behavior_id` qua [/report/integrated/get/](../12-api-reference/58-reporting.md#doc-1740302848100353) (không kèm tham số `order_field` và `enable_total_metrics`). Tối ưu hóa này có thể tăng số lượng ID truy vấn lên tới 2000. Xin lưu ý rằng yêu cầu đầu tiên có thể mất nhiều thời gian hơn để trả về phản hồi. Tuy nhiên, các yêu cầu tiếp theo với cùng tham số truy vấn nhưng khác số trang sẽ được phản hồi rất nhanh chóng.
Hiện tại, tính năng tối ưu hóa này chỉ áp dụng cho tài khoản trong danh sách cho phép (allowlist). Nếu muốn truy cập, vui lòng liên hệ đại diện TikTok của bạn. Sau khi được duyệt, bạn không cần thêm tham số yêu cầu mới nào vì hệ thống sẽ tự động kích hoạt phía dưới.

# Các chiều dữ liệu được hỗ trợ (Supported dimensions)
Xem [tại đây](bao-cao-p3.md#doc-1751454103714818) về các chiều dữ liệu được hỗ trợ của báo cáo đối tượng.
# Các chỉ số được hỗ trợ (Supported metrics)
Xem [tại đây](bao-cao-p3.md#doc-1751454162042882) về các chỉ số được hỗ trợ của báo cáo đối tượng.
# Các bộ lọc được hỗ trợ (Supported filters)
Xem [tại đây](bao-cao-p3.md#doc-1751454172429314) về các bộ lọc được hỗ trợ của báo cáo đối tượng.
# Hỗ trợ theo thời gian trọn đời (Lifetime supports)
Chỉ số trọn đời (lifetime metrics) cho báo cáo đối tượng hiện chưa hỗ trợ trong phiên bản API v1.3. 

# Các trường hợp sử dụng (Use Cases)

**1. Truy vấn phân bổ độ tuổi tổng thể của đối tượng khán giả trong một khoảng thời gian, sắp xếp tăng dần (ASC) theo chi tiêu (spend).**

**Request Parameters:**

``` xcodeblock
(code json JSON)
{
    "advertiser_id": 66,
    "service_type": "AUCTION",
    "report_type": "AUDIENCE",
    "data_level": "AUCTION_ADVERTISER",
    "dimensions": [
        "age"
    ],
    "metrics": [
        "spend",
        "impressions"
    ],
    "order_field": "spend",
    "order_type": "ASC",
    "start_date": "2020-10-16",
    "end_date": "2020-10-17",
    "page": 1,
    "page_size": 100
}
(/code)
```

**2. Truy vấn phân bổ khu vực địa lý của tất cả các nhóm quảng cáo chưa bị xóa thuộc các chiến dịch nhất định trong một khoảng thời gian.**

**Request Parameters:**

``` xcodeblock
(code json JSON)
{
    "advertiser_id": 66,
    "service_type": "AUCTION",
    "report_type": "AUDIENCE",
    "data_level": "AUCTION_ADGROUP",
    "dimensions": [
        "country_code",
        "adgroup_id"
    ],
    "metrics": [
        "spend",
        "impressions"
    ],
    "start_date": "2020-10-16",
    "end_date": "2020-10-16",
    "filtering": [
        {
            "field_name": "campaign_ids",
            "filter_type": "IN",
            "filter_value": "[1678604630215698,1678604630215698]"
        },
        {
            "field_name": "adgroup_status",
            "filter_type": "IN",
            "filter_value": "[\"STATUS_NOT_DELETE\"]"
        }
    ],
    "page": 1,
    "page_size": 100
}
(/code)
```

---

<a id="doc-1751454103714818"></a>
<!-- doc_id: 1751454103714818 -->
<!-- doc_id: 1751454103714818 -->
# Các chiều dữ liệu được hỗ trợ (Supported dimensions)
> Đường dẫn: Marketing API > Reporting > Guides > Report types > Audience reports > Supported dimensions
A dimension is an attribute to group your data by. Audience reports support the following dimensions. Please note that currently, we don't support all dimensions available on TikTok Ads Manager.

# Các chiều dữ liệu được hỗ trợ (Supported dimensions)

| Dimension Name | Description |
|---|---|
| advertiser_id | Nhóm theo ID tài khoản quảng cáo TikTok (Advertiser ID). ⏎ **Note**: Reporting data for [Branded Mission](https://ads.tiktok.com/help/article/about-branded-mission) ads is exclusively accessible when you query the advertiser level data using the `advertiser_id` dimension. Queries using the `campaign_id`, `adgroup_id`, or `ad_id` dimension will not return Branded Mission ad data. |
| campaign_id | Nhóm theo ID chiến dịch quảng cáo (Campaign ID). ⏎ **Note**:  • By default, the `campaign_status` filter is applied and defaults to `STATUS_NOT_DELETE` in synchronous audience reports. If you want to get breakdown data for all campaigns, including the deleted ones via synchronous audience reports, you need to set `campaign_status` to `STATUS_ALL`. • Reporting data for [Branded Mission](https://ads.tiktok.com/help/article/about-branded-mission) ads is exclusively accessible when you query the advertiser level data using the `advertiser_id` dimension. Queries using the `campaign_id`, `adgroup_id`, or `ad_id` dimension will not return Branded Mission ad data. |
| adgroup_id | Nhóm theo ID nhóm quảng cáo (Adgroup ID). ⏎ **Note**:  • By default, the `adgroup_status` filter is applied and defaults to `STATUS_NOT_DELETE` in synchronous audience reports. If you want to get breakdown data for all ad groups, including the deleted ones via synchronous audience reports, you need to set `adgroup_status` to `STATUS_ALL`. • Reporting data for [Branded Mission](https://ads.tiktok.com/help/article/about-branded-mission) ads is exclusively accessible when you query the advertiser level data using the `advertiser_id` dimension. Queries using the `campaign_id`, `adgroup_id`, or `ad_id` dimension will not return Branded Mission ad data. |
| ad_id_v2 | Nhóm theo ID mẫu quảng cáo (Ad ID). ⏎ Các loại dữ liệu bạn có thể nhận được bao gồm: • the ad level data for Manual Ads • the ad level data for Smart+ Campaigns • the **ad (asset group)** level data for Upgraded Smart+ Ads ⏎ **Note**: • You cannot use it together with the dimension `ad_id`, the filter `ad_ids`, or the attribute metric `ad_id`. |
| ad_id | Nhóm theo ID mẫu quảng cáo (Ad ID). ⏎ Các loại dữ liệu bạn có thể nhận được bao gồm: • the ad level data for Manual Ads • the ad level data for Smart+ Campaigns • the **creative** level data for Upgraded Smart+ Ads ⏎ **Note**:  • By default, the `ad_status` filter is applied and defaults to `STATUS_NOT_DELETE` in synchronous audience reports. If you want to get breakdown data for all ads, including the deleted ones via synchronous audience reports, you need to set `ad_status` to `STATUS_ALL`. • Reporting data for [Branded Mission](https://ads.tiktok.com/help/article/about-branded-mission) ads is exclusively accessible when you query the advertiser level data using the `advertiser_id` dimension. Queries using the `campaign_id`, `adgroup_id`, or `ad_id` dimension will not return Branded Mission ad data. |
| stat_time_day | Nhóm theo ngày (Group by day) |
| stat_time_hour | Nhóm theo giờ (Group by hour) |
| gender | Nhóm theo giới tính (Group by gender) |
| age | Nhóm theo độ tuổi (Group by age) |
| country_code | Nhóm theo mã vị trí địa lý (location code). ⏎ See [Supported metrics for a dimension in audience reports](bao-cao-p3.md#doc-1762404685488130) to learn about the supported metrics for this dimension. ⏎ **Note**: In synchronous audience reports, the value of `None` for `country_code` represents "Unknown". |
| province_id | Nhóm theo ID vị trí địa lý (location ID). For available values, see **Appendix - Location IDs**. ⏎ **Note**:  • If you include `province_id` in the `dimensions` field of your request, it is recommended to narrow down the query scope in order to avoid timeouts. For instance, you can use a limited number of IDs as a filter.  • In synchronous audience reports, the value of  `-1` for `province_id` represents "Unknown". |
| dma_id | Nhóm theo Khu vực thị trường được chỉ định (DMA). ⏎ Chỉ có Hoa Kỳ mới có DMA. ⏎ For available DMAs, see **Appendix - Location IDs**. ⏎ **Note**: In synchronous audience reports, the value of `0` for `dma_id` represents "Unknown". |
| ac | Nhóm theo mạng đối tượng (audience network) |
| language | Nhóm theo ngôn ngữ đối tượng (audience language) |
| platform | Grouped by operating system |
| interest_category | Nhóm theo danh mục sở thích cấp 1 (first-level interest category) |
| interest_category_tier2 | Nhóm theo danh mục sở thích cấp 2 (second-level interest category) |
| interest_category_tier3 | Nhóm theo danh mục sở thích cấp 3 (third-level interest category) |
| interest_category_tier4 | Nhóm theo danh mục sở thích cấp 4 (fourth-level interest category) |
| behavior_id | Nhóm theo hành vi (Group by behavior) |
| placement | Nhóm theo vị trí hiển thị (Group by placement) ⏎ **Note**: If you want to distinguish between the ads with Global App Bundle placement (`PLACEMENT_GLOBAL_APP_BUNDLE` ) and those with BuzzVideo/Babe placement (`PLACEMENT_TOPBUZZ`) via the attribute metric `placement_type`, you need to specify `placement` together with `adgroup_id` or `ad_id` in the `dimensions` field of the request. |
| ad_type | Group by ad type. See [Supported metrics for a dimension in audience reports - Supported metrics for `ad_type`](bao-cao-p3.md#doc-1762404685488130) to learn about the supported metrics for this dimension. |
| device_brand_id | Group by device brand. When this dimension is used, `lifetime` cannot be `true`. |
| contextual_tag | Group by contextual tags. `contextual_tag` only supports auction ads. You can use [/tool/contextual_tag/get/](../12-api-reference/70-tools-p2.md#doc-1747747118654465) to get a list of available contextual tags. |
| hashtag | Group by hashtag. See [Supported metrics for a dimension in audience reports - Supported metrics for `hashtag`](bao-cao-p3.md#doc-1762404685488130) to learn about the supported metrics for this dimension. |
| audience_tags | Group by audience tags. See [Supported metrics for a dimension in audience reports - Supported metrics for `audience_tags`](bao-cao-p3.md#doc-1762404685488130) to learn about the supported metrics for this dimension. |
| additional_interests | Group by additional interests. |
| purchase_intention | Group by purchase intention. See [Supported metrics for a dimension in audience reports - Supported metrics for `purchase_intention`](bao-cao-p3.md#doc-1762404685488130) to learn about the supported metrics for this dimension. ⏎ **Note**: This dimension can only be used in async reports. |
| bucket_id | Group by RTA (Real-Time API) bucket ID. An RTA bucket ID is an integer that identifies the traffic segment group (bucket) for your data. Pangle divides traffic into these groups for testing and optimization, enabling you to adjust your real-time bidding strategies through RTA based on the user characteristics of these different buckets and evaluate different strategies on various traffic segments. ⏎ The supported metrics for this dimension are:  •  `cost` • `impressions` • `clicks`  • `real_time_conversion` ⏎ The supported dimension grouping for this dimension is: `bucket_id` + *(Không bắt buộc)* `advertiser_id`/`campaign_id`+ *(Không bắt buộc)* `placement`/`country_code` + *(Không bắt buộc)* `stat_time_day`/`stat_time_hour`. ⏎ **Note**:  • This dimension can only be used in synchronous reports. • The `bucket_id` dimension is currently an allowlist-only feature. If you would like to access it, please contact your TikTok representative. |

# Nhóm chiều dữ liệu (Dimension grouping)

## Available dimension categories
**ID dimensions**

* advertiser_id
* campaign_id
* adgroup_id
* ad_id

**Time dimensions**

* stat_time_day
* stat_time_hour

**Audience dimensions** 

* gender
* age
* country_code 
* ac 
* language
* platform
* interest_category
* placement
* contextual_tag (cannot be used together with other audience dimensions)
* province_id
* dma_id
* interest_category
* interest_category_tier2
* interest_category_tier3
* interest_category_tier4
* device_brand_id
* behavior_id
* ad_type
* hashtag
* audience_tags
* additional_interests
* purchase_intention
- bucket_id

>  **Note:** Querying UV metrics with audience dimensions is not supported in asynchronous reports. Please query UV metrics without audience dimensions or audience dimensions without UV metrics in asynchronous reports instead. UV metrics include "average_video_play_per_user", "frequency", "cost_per_1000_reached", "real_time_result", "real_time_result_rate", "real_time_cost_per_result", "result", "result_rate", "cost_per_result", "reach", "live_play_count".

## Dimension grouping rules
Nhóm phân tích có thể gồm **một** chiều đối tượng (**bắt buộc**), **một** chiều ID *(Không bắt buộc)*, và **một** chiều thời gian *(Không bắt buộc)*. You cannot have more than one dimension of the same type in one request. The only exception is `age` and `gender`, and you can have both `age` and `gender` dimensions in one request.

- Special scenarios: 
	- Nếu `advertiser_ids` được chỉ định qua [/report/task/create/](../12-api-reference/58-reporting.md#doc-1740302766489602) (phương thức POST), nhóm phân tích có thể gồm **một** chiều đối tượng (**bắt buộc**), **một hoặc hai** chiều ID *(Không bắt buộc)*, và **một** chiều thời gian *(Không bắt buộc)*. Khi bạn truyền hai chiều ID cùng lúc, một trong số đó phải là `advertiser_id`. Ví dụ, `["advertiser_id", "campaign_id", "stat_time_day", "gender"]`.
    - Nếu bạn muốn dùng vị trí làm bộ lọc gom nhóm, bạn có thể chỉ định bất kỳ kết hợp nhóm chiều dữ liệu nào sau đây trong trường `dimensions` của yêu cầu:
        - `country_code`/`province_id` only
        - `country_code`/`province_id` + **one** ID dimension
        - `country_code`/`province_id` + **one** ID dimension + `stat_time_day`
        - `country_code`/`province_id` + `stat_time_day`
        - `country_code` + `bucket_id` + *(Không bắt buộc)* `advertiser_id`/`campaign_id` + *(Không bắt buộc)*  `stat_time_day` / `stat_time_hour`
    - Nhóm chiều dữ liệu được hỗ trợ cho chiều `bucket_id` là: `bucket_id`+  *(Không bắt buộc)* `advertiser_id`/`campaign_id`+  *(Không bắt buộc)* `placement`/`country_code` +  *(Không bắt buộc)*  `stat_time_day`/ `stat_time_hour`
	

**Additional dimension grouping rules**

* Các chiều dữ liệu sau đây không thể sử dụng cùng với bất kỳ chiều thời gian nào:
  * interest_category
  * interest_category_tier2
  * interest_category_tier3
  * interest_category_tier4
  * device_brand_id

* Trong báo cáo đối tượng đồng bộ, `behavior_id` có thể dùng kèm `stat_time_day` để truy xuất dữ liệu báo cáo của tối đa 5.000 quảng cáo, mặc dù trong tất cả các báo cáo đồng bộ khác bạn có thể truy xuất dữ liệu của tối đa 20.000 quảng cáo.
* Độ tuổi và giới tính có thể cùng tồn tại đồng thời trong chiều đối tượng. Ví dụ: `["stat_time_day", "age", "gender"]`.
* `ad_type` cannot be used with `advertiser_id` in the dimension grouping.

---

<a id="doc-1762404685488130"></a>
<!-- doc_id: 1762404685488130 -->
<!-- doc_id: 1762404685488130 -->
# Chỉ số hỗ trợ theo chiều dữ liệu trong báo cáo đối tượng (Supported metrics for a dimension in audience reports)
> Đường dẫn: Marketing API > Reporting > Guides > Report types > Audience reports > Supported dimensions > Supported metrics for a dimension in audience reports
Xem các bảng dưới đây để biết các chỉ số được hỗ trợ khi bạn sử dụng một chiều dữ liệu trong báo cáo đối tượng. You can find out the detailed introductions of the metrics in [Audience reports-Supported metrics](bao-cao-p3.md#doc-1751454162042882).

## Supported metrics for `country_code`

| Trường dữ liệu (Field) | Mô tả chi tiết (Description) | Hỗ trợ trong báo cáo đối tượng đồng bộ | Hỗ trợ trong báo cáo đối tượng bất đồng bộ |
|---|---|---|---|
| Chỉ số dữ liệu cơ bản (Basic data metrics) | | | |
#|`spend`	| Total Cost 	| ✅ 	| ✅ |
#|`cpc`	| CPC 	| ✅ 	| ✅ |
#|`cpm`	| CPM 	| ✅ 	| ✅ |
#|`impressions`	| Impressions 	| ✅ 	| ✅ |
#|`gross_impressions`	| Gross Impressions (Includes Invalid Impressions) 	| ✅ 	| ✅ |
#|`clicks`	| Clicks 	| ✅ 	| ✅ |
#|`ctr`	| CTR (%) 	| ✅ 	| ✅ |
#|`conversion`	| Conversion 	| ✅ 	| ✅ |
#|`cost_per_conversion`	| CPA 	| ✅ 	| ✅ |
#|`conversion_rate`	| CVR (%) 	| ✅ 	| ✅ |
#|`real_time_conversion`	| Real-time Conversions 	| ✅ 	| ✅ |
#|`real_time_cost_per_conversion`	| Real-time CPA 	| ✅ 	| ✅ |
#|`real_time_conversion_rate`	| Real-time CVR (%) 	| ✅ 	| ✅ |
#|`result`	| Result 	| ✅ 	| ❌ |
#|`cost_per_result`	| Cost Per Result 	| ✅ 	| ❌ |
#|`result_rate`	| Result Rate (%) 	| ✅ 	| ❌ |
#|`real_time_result`	| Real-time Result 	| ✅ 	| ❌ |
#|`real_time_cost_per_result`	| Real-time Cost Per Result 	| ✅ 	| ❌ |
#|`real_time_result_rate`	| Real-time Result Rate (%) 	| ✅ 	| ❌ |
| Chỉ số phát video (Video play metrics) | | | |
#|`video_play_actions`	| Video Views 	| ✅ 	| ✅ |
#|`video_watched_2s`	| 2-Second Video Views 	| ✅ 	| ✅ |
#|`video_watched_6s`	| 6-Second Video Views 	| ✅ 	| ✅ |
#|`average_video_play`	| Video Average Watch Time Per Video View 	| ✅ 	| ✅ |
#|`video_views_p25`	| Video Views at 25% 	| ✅ 	| ✅ |
#|`video_views_p50`	| Video Views at 50% 	| ✅ 	| ✅ |
#|`video_views_p75`	| Video Views at 75% 	| ✅ 	| ✅ |
#|`video_views_p100`	| Video Views at 100% 	| ✅ 	| ✅ |
| Chỉ số tương tác (Engagement metrics) | | | |
#|`profile_visits`	| Paid Profile Visit 	| ✅ 	| ✅ |
#|`profile_visits_rate`	| Paid Profile Visit Rate 	| ✅ 	| ✅ |
#|`likes`	| Paid Likes 	| ✅ 	| ✅ |
#|`comments`	| Paid Comments 	| ✅ 	| ✅ |
#|`shares`	| Paid Shares 	| ✅ 	| ✅ |
#|`follows`	| Paid Followers 	| ✅ 	| ✅ |
#|`clicks_on_music_disc`	| Music Clicks 	| ✅ 	| ✅ |
| Chỉ số sự kiện trang web (Page event metrics) | | |
#|Landing Page View	| | | |
##|`total_landing_page_view`	| Total Landing Page View 	| ✅ 	| ✅ |
##|`cost_per_landing_page_view`	| Cost per Landing Page View 	| ✅ 	| ✅ |
##|`landing_page_view_rate`	| Landing Page View Rate 	| ✅ 	| ✅ |

## Supported metrics for `ad_type`/`hashtag`/`audience_tags`/`purchase_intention`
| Field 	| Description 	| 
|---|---|
|Basic data metrics|  |
#|    `spend`    |     Total cost     |
#|     `cpc`    |     CPC(Destination)    |
#|     `cpm`    |     CPM    |
#|     `impressions`    |     Impressions    |
#|     `clicks`    |     Clicks(Destination)    |
#|     `ctr `   |     CTR(Destination)    |
#|     `conversion`    |     Conversions    |
#|     `cost_per_conversion`    |     CPA    |
#|     `conversion_rate`    |     CVR(Clicks)    |
#|     `conversion_rate_v2`    |     CVR(Impressions)    |
#|     `real_time_conversion`    |     Real-time conversions    |
#|     `real_time_cost_per_conversion`    |     Real-time CPA    |
#|     `real_time_conversion_rate`    |     Real-time CVR(Clicks)    |
#|     `real_time_conversion_rate_v2`    |     Real-time CVR(Impressions)    |
|Video play|  |
#|     `video_play_actions`    |     Video views    |
#|     `video_watched_2s `   |     2-second video views    |
#|    `video_watched_6s`    |     6-second video views    |
#|     `video_views_p100`    |     Video views at 100%    |
#|     `video_views_p75`    |     Video views at 75%    |
#|     `video_views_p50`    |     Video views at 50%    |
#|     `video_views_p25`    |     Video views at 25%    |
#|    `average_video_play`    |     Average watch time per video view    |
#|    `engaged_view`    |     6-second views (Focused view)    |
#|    `engaged_view_15s`    |     15-second views (Focused view)    |
|Engagement metrics|  |
#|     `follows`    |     Paid followers    |
#|    ` likes `   |     Paid likes    |
#|     `comments`    |     Paid comments    |
#|     `shares`    |     Paid share    |
#|     `profile_visits_rate`    |     Paid profile visits    |
#|     `profile_visits`    |     Paid Profile visit rate    |
#|     `clicks_on_music_disc`    |     Music clicks    |
| Page event metrics |  |
#|     `total_landing_page_view`    |     Total Landing Page View    |
#|    ` cost_per_landing_page_view `   |     Cost per Landing Page View    |
#|    ` landing_page_view_rate`    |     Landing Page View Rate    |

---

<a id="doc-1751454162042882"></a>
<!-- doc_id: 1751454162042882 -->
<!-- doc_id: 1751454162042882 -->
# Các chỉ số được hỗ trợ (Supported metrics)
> Đường dẫn: Marketing API > Reporting > Guides > Report types > Audience reports > Supported metrics
Bạn có thể sử dụng các chỉ số sau trong báo cáo đối tượng. Các chỉ số không phát sinh tiêu dùng sẽ được trả về dạng `-`. Xin lưu ý hiện tại chúng tôi chưa hỗ trợ toàn bộ các chỉ số có trên Trình quản lý quảng cáo TikTok.

# Chỉ số thuộc tính (Attribute metrics)
Các chỉ số thuộc tính (Attribute metrics), chẳng hạn như tên nhóm quảng cáo và loại quảng bá, là các thuộc tính cơ bản của chiến dịch, nhóm quảng cáo hoặc quảng cáo. Chỉ số thuộc tính chỉ hợp lệ khi sử dụng một chiều dữ liệu loại ID. 

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết | Chi tiết hỗ trợ (Detail) |
|---|---|---|---|
| advertiser_name | string | Account name | Được hỗ trợ ở cấp Nhà quảng cáo, Chiến dịch, Nhóm quảng cáo và Quảng cáo. |
| advertiser_id | string | Account ID | Được hỗ trợ ở cấp Nhà quảng cáo, Chiến dịch, Nhóm quảng cáo và Quảng cáo. |
| campaign_automation_type | string | Loại tự động hóa chiến dịch (Campaign automation type). ⏎ Các giá trị enum hỗ trợ: • `MANUAL`: Chiến dịch thủ công. • `SMART_PLUS`: Chiến dịch Smart+. • `UPGRADED_SMART_PLUS`: Chiến dịch Upgraded Smart+. Để tìm hiểu thêm về Chiến dịch Upgraded Smart+, xem [Chiến dịch Upgraded Smart+](quan-ly-chien-dich-p1.md#doc-1853452461203458). • Khi `campaign_automation_type` là `UPGRADED_SMART_PLUS`, trường `ad_id_v2` trả về là ID của Quảng cáo Upgraded Smart+. • `UPGRADED_SMART_PLUS_CREATIVE`: Upgraded Smart+ Campaigns. To learn more about Upgraded Smart+ Campaigns, see [Upgraded Smart+ Campaign](quan-ly-chien-dich-p1.md#doc-1853452461203458). • When `campaign_automation_type` is `UPGRADED_SMART_PLUS_CREATIVE`, the returned `ad_id` is the ID of a creative in the Upgraded Smart+ Ad. | Được hỗ trợ ở cấp Chiến dịch, Nhóm quảng cáo và Quảng cáo. |
| campaign_name | string | Campaign name | Được hỗ trợ ở cấp Chiến dịch, Nhóm quảng cáo và Quảng cáo. |
| campaign_id | string | ID chiến dịch quảng cáo | Được hỗ trợ ở cấp Nhóm quảng cáo và Quảng cáo. |
| objective_type | string | Advertising objective | Được hỗ trợ ở cấp Chiến dịch, Nhóm quảng cáo và Quảng cáo. |
| split_test | string | Split test status | Được hỗ trợ ở cấp Chiến dịch, Nhóm quảng cáo và Quảng cáo. |
| campaign_budget | string | Campaign budget | Được hỗ trợ ở cấp Chiến dịch, Nhóm quảng cáo và Quảng cáo. |
| campaign_dedicate_type | string | Campaign type | iOS 14 Dedicated Campaign or regular campaign. Được hỗ trợ ở cấp Chiến dịch, Nhóm quảng cáo và Quảng cáo. |
| app_promotion_type | string | App promotion type | Được hỗ trợ ở cấp Chiến dịch, Nhóm quảng cáo và Quảng cáo. |
| adgroup_name | string | Ad group name | Được hỗ trợ ở cấp Nhóm quảng cáo và Quảng cáo. |
| adgroup_id | string | ID nhóm quảng cáo | Được hỗ trợ ở cấp Quảng cáo. |
| placement_type | string | Placement type | Được hỗ trợ ở cấp Nhóm quảng cáo và Quảng cáo. |
| promotion_type | string | Promotion type | It can be app, website, or others. Supported at Adgroup and Ad levels in both synchronous and asynchronous reports. |
| opt_status | string | Automated creative optimization | Được hỗ trợ ở cấp Nhóm quảng cáo và Quảng cáo. |
| adgroup_download_url | string | Download URL/Website URL | Được hỗ trợ ở cấp Nhóm quảng cáo và Quảng cáo. |
| profile_image | string | Profile image | Được hỗ trợ ở cấp Nhóm quảng cáo và Quảng cáo. |
| dpa_target_audience_type | string | Target audience type for DPA | The Audience that DPA products target. Supported at Ad group or Ad levels in both synchronous and asynchronous reports. |
| budget | string | Ad group budget | Được hỗ trợ ở cấp Nhóm quảng cáo và Quảng cáo. |
| smart_target | string | Optimization goal | Được hỗ trợ ở cấp Nhóm quảng cáo và Quảng cáo. |
| pricing_category {-To be deprecated} | string | Billing Event | Được hỗ trợ ở cấp Nhóm quảng cáo và Quảng cáo. ⏎ If you want to retrieve the billing event of your ads, use the new metric `billing_event`. |
| billing_event | string | Billing Event | Được hỗ trợ ở cấp Nhóm quảng cáo và Quảng cáo. ⏎ Example: `"Clicks"`, `"Impression"`. |
| bid_strategy | string | Bid strategy | Được hỗ trợ ở cấp Nhóm quảng cáo và Quảng cáo. |
| bid | string | Bid | Được hỗ trợ ở cấp Nhóm quảng cáo và Quảng cáo. |
| bid_secondary_goal | string | Bid for secondary goal | Được hỗ trợ ở cấp Nhóm quảng cáo và Quảng cáo. |
| aeo_type | string | App Event Optimization Type | Được hỗ trợ ở cấp Nhóm quảng cáo và Quảng cáo. (Already Supported at adgoup, will add in ad level) |
| ad_name | string | Ad name | Được hỗ trợ ở cấp Quảng cáo. |
| ad_id_v2 | string | Các loại dữ liệu bạn có thể nhận được bao gồm: • the ad IDs of Manual Ads. • the ad IDs of Smart+ Campaigns. • the ad IDs of Upgraded Smart+ Ads. ⏎ • You cannot use it together with the dimension `ad_id`, the filter `ad_ids`, or the attribute metric `ad_id`. | Được hỗ trợ ở cấp Quảng cáo. |
| ad_id | string | ID mẫu quảng cáo | Được hỗ trợ ở cấp Quảng cáo. |
| ad_text | string | Ad title | Available in Ad level. |
| call_to_action | string | Call to action | Được hỗ trợ ở cấp Quảng cáo. |
| ad_profile_image | string | Profile image (Ad level) | Được hỗ trợ ở cấp Quảng cáo. |
| ad_url | string | URL (Ad level) | Được hỗ trợ ở cấp Quảng cáo. |
| tt_app_id | string | TikTok App ID | TikTok App ID, the App ID you used when creating an Ad Group. Được hỗ trợ ở cấp Nhóm quảng cáo và Quảng cáo. Returned if the promotion type of one Ad Group is App. |
| tt_app_name | string | TikTok App Name | The name of your TikTok App. Được hỗ trợ ở cấp Nhóm quảng cáo và Quảng cáo. Returned if the promotion type of one Ad Group is App. |
| mobile_app_id | string | Mobile App ID | Mobile App ID. ⏎ Examples are, App Store: https://apps.apple.com/us/app/angry-birds/id**343200656**; Google Play：https://play.google.com/store/apps/details?id=**com.rovio.angrybirds**. ⏎ Được hỗ trợ ở cấp Nhóm quảng cáo và Quảng cáo. Returned if the promotion type of one Ad Group is App. |
| device_brand_name | string | Device brand name | Available when the `device_brand_id` dimension is used. |
| behavior_name | string | Behavior name | Available when the `behavior_id` dimension is used. |
| action_category | string | Action / behavior category | Available only when the `behavior_id` dimension is used. This metric does not support asynchronous reports. |
| action_scene | string | Action scene. Các giá trị enum hỗ trợ: `VIDEO_RELATED`, `CREATOR_RELATED`. | Available only when the `behavior_id` dimension is used. This metric does not support asynchronous reports. |
| user_action | string | User action | For the `VIDEO_RELATED` scene, available values include `WATCHED_TO_END`, `LIKED`, `COMMENTED`, and `SHARED`. For the `CREATOR_RELATED` scene, available values are `FOLLOWING` and `VIEW_HOMEPAGE`. |
| action_period | string | Number of days for the action. Các giá trị enum hỗ trợ: `7`, `15`. | This metric does not support asynchronous reports. |
| rf_campaign_type | string | Campaign type. Các giá trị enum hỗ trợ: `0` (Reach & Frequency campaign), `1` (TikTok Pulse campaign). | Supported at Campaign, Ad Group and Ad levels in both synchronous and asynchronous reports. |
| delivery_type | string | Delivery type. | Được hỗ trợ ở cấp Nhóm quảng cáo và Quảng cáo. |
| adgroup_display_name | string | Ad group display name. | Được hỗ trợ ở cấp Nhóm quảng cáo và Quảng cáo. |
| adgroup_schedule | string | Ad group schedule. Example: "2024-01-09-Ongoing". | Được hỗ trợ ở cấp Nhóm quảng cáo và Quảng cáo. |
| optimization_preference | string | Optimization preference. Example: "Optimize conversion at learning phase". | Được hỗ trợ ở cấp Nhóm quảng cáo và Quảng cáo. |
| image_info | string | Image information. Example: `https://p16-sign-sg.tiktokcdn.com/tos-alisg-p-0051c001-sg/o4PDmEEDgzoBf7VFfmlNBBAtE7p2uqI4TduOYQ~tplv-noop.image?x-expires=1707528999&x-signature=91iFceqlBWKfwNuOJjyaijC5qU0%3D` | Được hỗ trợ ở cấp Quảng cáo. |
| ad_display_name | string | Ad display name. | Được hỗ trợ ở cấp Quảng cáo. |
| identity_type | string | Identity type. Example: "TikTok account (Spark Ads)". | Được hỗ trợ ở cấp Quảng cáo. |
| currency | string | currency | The currency code, e. g. USD. Note that if you want to use `currency` as metrics, then the `dimensions` field in your request must include `adgroup_id`/`ad_id`/`campaign_id`/`advertiser_id`. |
| is_aco | boolean | Liệu ad is an automated ad or a Smart Creative ad. Set to `True` for an automated ad or Smart Creative ad. | Supported at AUCTION_ADGROUP level. |
| is_smart_creative | boolean | Liệu ad is a Smart Creative ad. | Supported at AUCTION_AD level. |

# Chỉ số dữ liệu cơ bản (Basic data metrics)
 Các chỉ số dữ liệu cơ bản (Basic data metrics) là dữ liệu về chi phí và hiệu suất phân phối quảng cáo của bạn. 

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết | Chi tiết hỗ trợ (Detail) |
|---|---|---|---|
| spend | string | Cost | Sum of your total ad spend, calculated in the currency of your ad account. |
| cost | string | Cost | Sum of your total ad spend, calculated in USD. ⏎ **Note**: This metric can only be used together with the `bucket_id` dimension. |
| cpc | string | CPC (destination) | Average cost of each click to a specified destination. |
| cpm | string | CPM | Average amount you spent per 1,000 impressions. |
| impressions | string | Impressions | Number of times your ads were shown. |
| gross_impressions | string | Gross Impressions (Includes Invalid Impressions) | The number of times an ad was seen on screen, including invalid impressions. |
| clicks | string | Clicks (destination) | Number of clicks from your ads to a specified destination. |
| ctr | string | CTR (destination) | Percentage of impressions that resulted in a destination click out of all impressions. |
| reach | string | Reach | Number of unique users who saw your ads at least once. ⏎ **Note**: If you want to use this metric, you need to specify any of the following audience dimension groupings along with one optional ID dimension and one optional time dimension in the `dimensions` field of the request:  • `age` • `gender` •  `age` + `gender` • `country_code` • `province_id` • `language` |
| cost_per_1000_reached | string | Cost per 1,000 people reached | Average cost to reach 1,000 unique users. ⏎ **Note**: If you want to use this metric, you need to specify any of the following audience dimension groupings along with one optional ID dimension and one optional time dimension in the `dimensions` field of the request:  • `age` • `gender` •  `age` + `gender` • `country_code` • `province_id` • `language` |
| frequency | string | Frequency | The average number of times each user saw your ad over a given time period. ⏎ **Note**: If you want to use this metric, you need to specify any of the following audience dimension groupings along with one optional ID dimension and one optional time dimension in the `dimensions` field of the request:  • `age` • `gender` •  `age` + `gender` • `country_code` • `province_id` • `language` |
| conversion | string | Conversions | Number of times your ad resulted in the optimization event you selected. |
| cost_per_conversion | string | Cost per conversion | Average amount spent on a conversion. |
| conversion_rate | string | Conversion rate (CVR, clicks) | Percentage of results you received out of all destination clicks on your ads. ⏎ **Note**: Starting late October, 2023, the calculation logic for this metric will be updated to be impression-based (the same as `conversion_rate_v2`). To ensure a smooth API integration and avoid disruptions caused by the change in calculation logic, we recommend you switch to using the impression-based metric `conversion_rate_v2` as soon as possible. |
| conversion_rate_v2 | string | Conversion rate (CVR) | Percentage of results you received out of all impressions on your ads. |
| real_time_conversion | string | Real-time conversions | Number of times your ad resulted in the optimization event you selected. |
| real_time_cost_per_conversion | string | Real-time cost per conversion | Average amount spent on a conversion. |
| real_time_conversion_rate | string | Real-time conversion rate (CVR, clicks) | Percentage of conversions you received out of all destination clicks on your ads. ⏎ **Note**: Starting late October, 2023, the calculation logic for this metric will be updated to be impression-based (the same as `real_time_conversion_rate_v2`). To ensure a smooth API integration and avoid disruptions caused by the change in calculation logic, we recommend you switch to using the impression-based metric `real_time_conversion_rate_v2` as soon as possible. |
| real_time_conversion_rate_v2 | string | Real-time conversion rate (CVR) | Percentage of conversions you received out of all impressions on your ads. |
| result | string | Results | Number of times your ad resulted in an intended outcome based on your campaign objective and optimization goal. |
| cost_per_result | string | Cost per result | Average cost per each result from your ads. |
| result_rate | string | Result rate | Percentage of results that happened out of all impressions on your ads. |
| real_time_result | string | Real-time results | Number of times your ad resulted in an intended outcome based on your campaign objective and optimization goal. |
| real_time_cost_per_result | string | Real-time cost per result | Average cost per each result from your ads. |
| real_time_result_rate | string | Real-time result rate | Percentage of results that happened out of all impressions on your ads. |

# Chỉ số phát video (Video play metrics)
Video play metrics, such as 2-Second Video Views and Video Views at 50%, are data about video view performance. 

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết | Chi tiết hỗ trợ (Detail) |
|---|---|---|---|
| video_play_actions | string | Video views | Number of times your video started to play. For each video impression, plays are counted separately and replays are excluded. |
| video_watched_2s | string | 2-second video views | Number of times your video was played for at least 2 seconds. For each video impression, plays are counted separately and replays are excluded. |
| video_watched_6s | string | 6-second video views | Number of times your video was played for at least 6 seconds. For each video impression, plays are counted separately and replays are excluded. |
| engaged_view | string | 6-second focused views | Number of times your video was played for at least 6 seconds, played in full if it is less than 6 seconds, or received at least 1 engagement within the first 6 seconds. |
| engaged_view_15s | string | 15-second focused views | Number of times your video was played for at least 15 seconds, played in full if it is less than 15 seconds, or received at least 1 engagement within the first 15 seconds. |
| video_views_p25 | string | Video views at 25% | Number of times your video was played at least 25% of its length. For each impression, views are counted separately and replays are excluded. |
| video_views_p50 | string | Video views at 50% | Number of times your video was played at least 50% of its length. For each impression, views are counted separately and replays are excluded. |
| video_views_p75 | string | Video views at 75% | Number of times your video was played at least 75% of its length. For each impression, views are counted separately and replays are excluded. |
| video_views_p100 | string | Video views at 100% | Number of times your video was played 100% of its length. For each impression, views are counted separately and replays are excluded. |
| average_video_play | string | Average play time per video view | Average time your video was played per single video view, including any time spent replaying the video. |
| average_video_play_per_user | string | Average play time per user | Average time your video was played per user, including any time spent replaying the video. ⏎ **Note**: This metric is supported only when `placement` is specified in the `dimensions` field of the request. |

# Chỉ số tương tác (Engagement metrics)
 Các chỉ số tương tác (Engagement metrics), chẳng hạn như số lượt thích và bình luận, là dữ liệu về cách người dùng tương tác với quảng cáo của bạn. 
 

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết | Chi tiết hỗ trợ (Detail) |
|---|---|---|---|
| follows | string | Paid follows | Number of follows to the associated profile during the ad impression. |
| likes | string | Paid likes | Number of times your ad was liked during the ad impression. |
| comments | string | Paid comments | Number of comments sent on your ad during the ad impression. |
| shares | string | Paid shares | Number of shares of your ad during the ad impression. |
| profile_visits | string | Paid profile visits | Number of visits to the associated profile during the ad impression. |
| profile_visits_rate | string | Paid profile visit rate | Percentage of profile visits from ads out of all impressions on your ads. |
| clicks_on_music_disc | string | Sound clicks | Number of clicks on the sound associated with your ad during the ad impression. |
| ix_page_duration_avg | string | Instant experience average view time | Average time your Instant Experience was shown. ⏎ **Note**: This metric is supported only when `placement` is specified in the `dimensions` field of the request. |
| ix_page_viewrate_avg | string | Instant experience average view percentage | Average percentage of content on your Instant Experience that was viewed. ⏎ **Note**: This metric is supported only when `placement` is specified in the `dimensions` field of the request. |

# Chỉ số phân bổ (Attribution metrics)
Attribution metrics are data about how events are attributed.

> **Lưu ý:** 
> Các [chiều đối tượng](bao-cao-p3.md#doc-1751454103714818) duy nhất được hỗ trợ cho các chỉ số Phân bổ (Attribution metrics) trong báo cáo đối tượng là `placement` và `ad_type`.

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết | Chi tiết hỗ trợ (Detail) |
|---|---|---|---|
| vta_complete_payment | string | VTA complete payment | Complete payment events attributed to someone only viewing your ad. |
| cost_per_vta_payments_completed | string | Cost per VTA complete payment | Average cost of each complete payment event attributed to someone only viewing your ad. |
| vta_complete_payment_value | string | Total VTA complete payment value | Total value of complete payment events attributed to someone only viewing your ad. |
| vta_complete_payment_roas | string | VTA complete payment ROAS | Return on ad spend (ROAS) from complete payment events attributed to someone only viewing your ad. |

# Chỉ số sự kiện trang (Page event metrics)
Page Event Metrics are data about website conversion events.

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết | Chi tiết hỗ trợ (Detail) |
|---|---|---|---|
| Landing Page View |  |  |  |
| ↳ total_landing_page_view | string | Total Landing Page View | The number of landing page view events from your ads. |
| ↳ cost_per_landing_page_view | string | Cost per Landing Page View | The average cost of each landing page view event. |
| ↳ landing_page_view_rate | string | Landing Page View Rate | The percentage of click events that are landing page view events. |

---

<a id="doc-1751454172429314"></a>
<!-- doc_id: 1751454172429314 -->
<!-- doc_id: 1751454172429314 -->
# Các bộ lọc được hỗ trợ (Supported filters)
> Đường dẫn: Marketing API > Reporting > Guides > Report types > Audience reports > Supported filters
Bạn có thể sử dụng các bộ lọc sau để thu hẹp phạm vi kết quả báo cáo. 

Ngoài [các bộ lọc được hỗ trợ trong báo cáo cơ bản](bao-cao-p3.md#doc-1751443975608321), báo cáo đối tượng cũng hỗ trợ thêm các bộ lọc dưới đây.

> **Note:** 
> - Trong báo cáo đối tượng bất đồng bộ, các trường bộ lọc duy nhất được hỗ trợ là `campaign_ids`, `adgroup_ids`, và `ad_ids`.
> - Báo cáo đối tượng hiện bao gồm dữ liệu cho quảng cáo Đấu giá (Auction), quảng cáo Tiếp cận & Tần suất (Reach & Frequency), và TopView. Tuy nhiên, you can not filter data for a specific buying type in audience reports. To filter data for a specific buying type, use [/report/integrated/get/](../12-api-reference/58-reporting.md#doc-1740302848100353) to run a basic report. Within the filtering object, specify the `buying_type` field and enter the values of either `AUCTION`, `RESERVATION_TOP_VIEW`, or `RESERVATION_RF`.
> - Đối với quảng cáo TopView, các chỉ số liên quan đến chi phí ở cấp quảng cáo và các chỉ số chi phí phân tích theo đối tượng sẽ chỉ bao gồm dữ liệu cho các quảng cáo được phân phối sau ngày 18 tháng 1 năm 2024.
> - Dữ liệu báo cáo cho [quảng cáo Product GMV Max](https://ads.tiktok.com/help/article/how-to-create-product-gmv-max-ads-in-seller-center) và quảng cáo LIVE GMV Max tạo từ TikTok Shop sẽ bị loại trừ khỏi các báo cáo cơ bản Đấu thầu đồng bộ, báo cáo đối tượng, báo cáo quảng cáo tương tác và báo cáo DSA. Quảng cáo Mua sắm (Shopping Ads) được tạo qua API hoặc TikTok Ads Manager không bị ảnh hưởng.

| Bộ lọc (Filter) | Kiểu lọc hỗ trợ (Supported Filter Types) | Cấp dữ liệu hỗ trợ (Supported Data Level) | Ghi chú chi tiết (Notes) |
|---|---|---|---|
| campaign_system_origins | IN | Chiến dịch / Nhóm quảng cáo / Quảng cáo | The campaign origins (campaign sources). ⏎ Các giá trị enum hỗ trợ: • `PROMOTE`: The campaign is a Promote campaign created through the TikTok mobile App. • `TT_ADS_PLATFORM`: The campaign is a non-Promote campaign created through the API or in TikTok Ads Manager.  Giá trị mặc định: `"[\"TT_ADS_PLATFORM\"]"`. ⏎ To learn more about the supported dimensions, metrics and filters for Promote ads, see [Promote campaigns](quan-ly-chien-dich-p1.md#doc-1785880454546433). ⏎ **Note**:  •  This filter is only supported in synchronous audience reports.  •  In asynchronous audience reports, the results include the data for Promote ads by default. |
| dma_ids | IN | Chiến dịch / Nhóm quảng cáo / Quảng cáo | Filter by DMA IDs. Chỉ hợp lệ khi the `dma_id` dimension is used. Để xem danh sách giá trị enum, xem **Location IDs**. |
| region_ids | IN | Chiến dịch / Nhóm quảng cáo / Quảng cáo | Filter by region IDs on the state or provincial level. Chỉ hợp lệ khi the `province_id` dimension is used. |
| interest_category | IN | Chiến dịch / Nhóm quảng cáo / Quảng cáo | Filter by tier-1 interest categories. Chỉ hợp lệ khi the `interest_category` dimension is used. For available values, see [Get interest categories](../12-api-reference/70-tools-p1.md#doc-1737174348712961). |
| interest_category_tier2 | IN | Chiến dịch / Nhóm quảng cáo / Quảng cáo | Filter by tier-2 interest categories. Chỉ hợp lệ khi the `interest_category_tier2` dimension is used. For available values, see [Get interest categories](../12-api-reference/70-tools-p1.md#doc-1737174348712961). |
| interest_category_tier3 | IN | Chiến dịch / Nhóm quảng cáo / Quảng cáo | Filter by tier-3 interest categories. Chỉ hợp lệ khi the `interest_category_tier3` dimension is used. For available values, see [Get interest categories](../12-api-reference/70-tools-p1.md#doc-1737174348712961). |
| interest_category_tier4 | IN | Chiến dịch / Nhóm quảng cáo / Quảng cáo | Filter by tier-4 interest categories. Chỉ hợp lệ khi the `interest_category_tier4` dimension is used. For available values, see [Get interest categories](../12-api-reference/70-tools-p1.md#doc-1737174348712961). |
| destination | IN | Ad | Destination page type. ⏎ Các giá trị enum hỗ trợ: •  `APP`: The download page for the promoted App in Google Play or Apple Store. The `promotion_type` for the corresponding ad group is set as `APP_ANDROID` or `APP_IOS`.  • `TIKTOK_INSTANT_PAGE`: TikTok Instant Pages, including Custom Page, Instant Form, App Profile Page, and Instant Product Page. The page ID (`page_id`) of a TikTok Instant Page is specified for the ad.  • `WEBSITE`: Website page. A landing page URL (`landing_page_url`) is specified for the ad. • `SOCIAL_MEDIA_APP`: Social media URL. To learn about the ads where the destination can be set as social media URL, see [Create a Lead Generation ad with promotion type as instant messaging apps](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1774482999036930). • `PHONE_CALL`: Phone number. To learn about the ads where the destination can be set as phone number, see [Create a Lead Generation ad with promotion type as phone call](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1774482936048641). ⏎ **Note**: This filter is only supported in synchronous audience reports. |
| creative_material_mode | IN | Nhóm quảng cáo / Quảng cáo | Chiến lược phân phối mẫu quảng cáo sáng tạo. Các giá trị enum hỗ trợ: `CUSTOM` (tùy chỉnh), `DYNAMIC` (tự động hóa), `SMART_CREATIVE` (Smart Creative). |
| bid_strategy | IN | Ad group | Bidding strategy.  Các giá trị enum hỗ trợ: `BID_STRATEGY_COST_CAP`, `BID_STRATEGY_BID_CAP`, `BID_STRATEGY_MAX_CONVERSION` and `BID_STRATEGY_LOWEST_COST`. |

---

<a id="doc-1738864940608513"></a>
<!-- doc_id: 1738864940608513 -->
<!-- doc_id: 1738864940608513 -->
# Báo cáo quảng cáo tương tác (Playable ad reports)
> Đường dẫn: Marketing API > Reporting > Guides > Report types > Playable ad reports
Playable ad reports are a type of report from which you can get data about playable creatives. 

> **Lưu ý:** • Báo cáo quảng cáo tương tác (Playable ad reports) trả về dữ liệu của các mẫu nội dung sáng tạo có thể chơi được. Tham số `data_level` không bắt buộc trong yêu cầu của bạn. • Không hỗ trợ chạy báo cáo quảng cáo tương tác ở chế độ CHUNK (`query_mode`= `CHUNK`). Bạn chỉ có thể chạy báo cáo cơ bản đồng bộ ở chế độ CHUNK.

# Các chiều dữ liệu được hỗ trợ (Supported dimensions)
Xem [tại đây](bao-cao-p3.md#doc-1751617879104514) về các chiều dữ liệu được hỗ trợ của báo cáo quảng cáo tương tác.
# Các chỉ số được hỗ trợ (Supported metrics)
Xem [tại đây](bao-cao-p3.md#doc-1751617882108929) về các chỉ số được hỗ trợ của báo cáo quảng cáo tương tác.
# Các bộ lọc được hỗ trợ (Supported filters)
Xem [tại đây](bao-cao-p3.md#doc-1751617884206210) về các bộ lọc được hỗ trợ của báo cáo quảng cáo tương tác.
# Hỗ trợ theo thời gian trọn đời (Lifetime supports)
Playable ad reports support lifetime metrics at the Advertiser, Campaign, Ad group, and Ad levels.

Không hỗ trợ phân tách theo thời gian hoặc vị trí khi truy vấn các chỉ số trọn đời (lifetime metrics), vì vậy khi `query_lifetime` = `True`, tham số `dimensions` không được chứa `stat_time_day`, `stat_time_hour`, hoặc `country_code`.

Bạn chỉ có thể sử dụng các chỉ số trọn đời trong báo cáo quảng cáo tương tác đồng bộ, vì báo cáo quảng cáo tương tác không hỗ trợ chế độ không đồng bộ.

# Các trường hợp sử dụng (Use Cases)

**1. Truy vấn dữ liệu của các quảng cáo tương tác có chi tiêu nằm trong khoảng từ 0 đến 100 trong một khoảng thời gian nhất định.**

**Request Parameters：**

``` xcodeblock
(code json JSON)
{
    "advertiser_id": 666,
    "service_type": "AUCTION",
    "report_type": "PLAYABLE_MATERIAL",
    "dimensions": [
        "playable_id"
    ],
    "metrics": [
    	"playable_id",
        "playable_name",   
        "spend",
        "cpm",
        "impressions",
        "clicks",
        "ctr"
    ],
    "filtering": [
        {
            "field_name": "spend",
            "filter_type": "RANGE",
            "filter_value": "[0,100]"
        }
    ],
    "start_date": "2020-10-10",
    "end_date": "2020-11-10",
    "page": 1,
    "page_size": 100
}
(/code)
```

**2. Truy vấn dữ liệu của từng quảng cáo tương tác tại các quốc gia khác nhau trong một khoảng thời gian nhất định.**

**Request Parameters：**

``` xcodeblock
(code json JSON)
{
    "advertiser_id": 666,
    "service_type": "AUCTION",
    "report_type": "PLAYABLE_MATERIAL",
    "dimensions": [
        "playable_id", "country_code"
    ],
    "metrics": [
    	"playable_id",
        "playable_name",   
        "spend",
        "cpm",
        "impressions",
        "clicks",
        "ctr"
    ],
    "start_date": "2020-10-10",
    "end_date": "2020-11-10",
    "page": 1,
    "page_size": 100
}
(/code)
```

---

<a id="doc-1751617879104514"></a>
<!-- doc_id: 1751617879104514 -->
<!-- doc_id: 1751617879104514 -->
# Các chiều dữ liệu được hỗ trợ (Supported dimensions)
> Đường dẫn: Marketing API > Reporting > Guides > Report types > Playable ad reports > Supported dimensions
A dimension is an attribute to group your data by. Playable ad reports support the following dimensions. Please note that currently, we don't support all dimensions available on TikTok Ads Manager.
# Các chiều dữ liệu được hỗ trợ (Supported dimensions)

| Dimension Name | Description |
| --- | --- |
| playable_id| Group by playable ID.|
| country_code| Group by location code. Để xem danh sách giá trị enum, xem **Appendix-Location IDs**. <br>Note that `country_code` only works for playable synchronous reports.  <br>See [Supported metrics for a dimension in playable ad reports](bao-cao-p3.md#doc-1762405483224065) to learn about the supported metrics for this dimension.|

# Nhóm chiều dữ liệu (Dimension grouping)
- playable_id
- playable_id + country_code

---

<a id="doc-1762405483224065"></a>
<!-- doc_id: 1762405483224065 -->
<!-- doc_id: 1762405483224065 -->
# Chỉ số hỗ trợ theo chiều dữ liệu trong báo cáo quảng cáo tương tác (Supported metrics for a dimension in playable ad reports)
> Đường dẫn: Marketing API > Reporting > Guides > Report types > Playable ad reports > Supported dimensions > Supported metrics for a dimension in playable ad reports
Xem các bảng dưới đây để biết các chỉ số được hỗ trợ khi bạn sử dụng một chiều dữ liệu trong báo cáo quảng cáo có thể chơi (playable ads). You can find out the detailed introductions of the metrics in [Playable ad reports-Supported metrics](bao-cao-p3.md#doc-1751617882108929).

## Supported metrics for `country_code`

| Trường dữ liệu (Field) | Mô tả chi tiết (Description) | Hỗ trợ trong báo cáo tương tác đồng bộ |
|---|---|---|
| Chỉ số dữ liệu cơ bản (Basic data metrics) | | |
#|`spend`	| Total Cost 	| ✅ 	|
#|`cpm`	| CPM 	| ✅ 	|
#|`impressions`	| Impressions 	| ✅ 	|
#|`clicks`	| Clicks 	| ✅ 	|
#|`ctr`	| CTR (%) 	| ✅ 	|
#|`conversion`	| Conversion 	| ✅ 	|
#|`cost_per_conversion`	| CPA 	| ✅ 	|
#|`conversion_rate`	| CVR (%) 	| ✅ 	|
| Chỉ số sự kiện trong ứng dụng duy nhất (In-App Event metrics - Unique) | | |
#|`app_install`	| App Install 	| ✅ 	|
#|`cost_per_app_install`	| Cost per App Install 	| ✅ 	|
#|`app_install_rate`	| App Install Rate 	| ✅ 	|
| Chỉ số sự kiện quảng cáo tương tác (Playable ads event metrics) | | |
#|`playable_page_view_count`	| Playable page views 	| ✅ 	|
#|`playable_first_scene_view_count`	| Playable views: first scene 	| ✅ 	|
#|`playable_second_scene_view_count`	| Playable views: second scene 	| ✅ 	|
#|`playable_third_scene_view_count`	| Playable views: third scene 	| ✅ 	|
#|`playable_cta_click`	| Playable CTA button clicks 	| ✅ 	|

---

<a id="doc-1751617882108929"></a>
<!-- doc_id: 1751617882108929 -->
<!-- doc_id: 1751617882108929 -->
# Các chỉ số được hỗ trợ (Supported metrics)
> Đường dẫn: Marketing API > Reporting > Guides > Report types > Playable ad reports > Supported metrics
Bạn có thể sử dụng các chỉ số sau trong báo cáo quảng cáo có thể chơi. Các chỉ số không phát sinh tiêu dùng sẽ được trả về dạng `-`. Xin lưu ý hiện tại chúng tôi chưa hỗ trợ toàn bộ các chỉ số có trên Trình quản lý quảng cáo TikTok.

## Chỉ số thuộc tính (Attribute metrics)
Các chỉ số thuộc tính (Attribute metrics), chẳng hạn như tên tài nguyên tương tác và ID tài nguyên tương tác, là các thuộc tính cơ bản của quảng cáo tương tác. Chỉ số thuộc tính chỉ được hỗ trợ khi `dimensions` chứa `playable_id`.
| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết | Chi tiết hỗ trợ (Detail) |
|---|---|---|---|
| playable_id | string | Playable ID| Playable creative ID |
| playable_name | string | Playable Name | Playable creative name |
| playable_url | string | Playable URL | Playable creative URL |
| preview_url | string | Thumbnail | |
| create_time | datetime | Create time | |
| modify_time | datetime | Modify time | |
| playable_status | string | Status | |
| orientation | string | Display orientation | |
| country | string | Delivery country or location | |
| associated_adgroup_count | string | No. of Related Ad Groups ||
## Chỉ số dữ liệu cơ bản (Basic data metrics)
Basic data metrics are data about spend and performance of your playable ads.
| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết | Chi tiết hỗ trợ (Detail) |
|---|---|---|---|
| spend | string | Cost | Sum of your total ad spend. |
| cpm | string | CPM | Average amount you spent per 1,000 impressions. |
| impressions | string | Impressions | Number of times your ads were shown. |
| clicks | string | Clicks (destination) | Number of clicks from your ads to a specified destination. |
| ctr | string | CTR (destination) | Percentage of impressions that resulted in a destination click out of all impressions. |
| conversion | string | Conversions | Number of times your ad resulted in the optimization event you selected. |
| cost_per_conversion | string | Cost per conversion | Average amount spent on a conversion. |
| conversion_rate | string | Conversion rate (CVR, clicks) | Percentage of results you received out of all destination clicks on your ads. <br><br><p><span style="color:darkred"><b>Note</b></span>: Starting late October, 2023, the calculation logic for this metric will be updated to be impression-based (the same as `conversion_rate_v2`). To ensure a smooth API integration and avoid disruptions caused by the change in calculation logic, we recommend you switch to using the impression-based metric `conversion_rate_v2` as soon as possible.  |
| conversion_rate_v2 | string | Conversion rate (CVR) | Percentage of results you received out of all impressions on your ads. |
| currency | string | currency | The currency code, e. g. USD. Note that if you want to use `currency` as metrics, then the `dimensions` field in your request must include `adgroup_id`/`ad_id`/`campaign_id`/`advertiser_id`.  `currency`only works for playable synchronous reports. |

## In-App Event metrics (Unique)
Các chỉ số sự kiện trong ứng dụng (In-App event metrics) là dữ liệu về các sự kiện chuyển đổi diễn ra trong ứng dụng. 
| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết | Chi tiết hỗ trợ (Detail) |
|---|---|---|---|
| app_install | string | App Install | The number of times your mobile app was installed that were recorded as app events and attributed to your ads. (The total count is calculated based on the time each ad impression occurred.) |
| cost_per_app_install| string | Cost per App Install | The average cost for each app install event. (The total count is calculated based on the time each ad impression occurred.) |
| app_install_rate| string | App Install Rate | App Install Rate. (The total count is calculated based on the time each ad impression occurred.)|
## Playable ads event metrics
Playable ads event metrics are data about how people interact with your playale ads.
| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết | Chi tiết hỗ trợ (Detail) |
|---|---|---|---|
| playable_page_view_count | string | Playable page views | Number of times your playable page was shown. |
| playable_first_scene_view_count | string | Playable views of first scene | Number of views of your playable page that reach at least the first scene of your ad. |
| playable_second_scene_view_count | string | Playable views of second scene | Number of views of your playable page that reach at least the second scene of your ad. |
| playable_third_scene_view_count | string | Playable views of third scene | Number of views of your playable page that reach the third scene of your ad. |
| playable_cta_click | string | Playable download button clicks | Number of clicks on the download button on your playable page. |

---

<a id="doc-1751617884206210"></a>
<!-- doc_id: 1751617884206210 -->
<!-- doc_id: 1751617884206210 -->
# Các bộ lọc được hỗ trợ (Supported filters)
> Đường dẫn: Marketing API > Reporting > Guides > Report types > Playable ad reports > Supported filters
Bạn có thể sử dụng các bộ lọc sau để thu hẹp phạm vi kết quả báo cáo.

Vui lòng đọc kỹ các lưu ý dưới đây trước khi bắt đầu:
* Khi bạn truyền nhiều bộ lọc, các điều kiện lọc sẽ kết hợp theo quan hệ logic `AND` (đồng thời thỏa mãn).
* Khi bạn sử dụng kiểu bộ lọc `IN`, `filter_value` phải là chuỗi JSON dạng mảng hợp lệ.

> **Note:** 
> - Dữ liệu báo cáo cho [quảng cáo Product GMV Max](https://ads.tiktok.com/help/article/how-to-create-product-gmv-max-ads-in-seller-center) và quảng cáo LIVE GMV Max tạo từ TikTok Shop sẽ bị loại trừ khỏi các báo cáo cơ bản Đấu thầu đồng bộ, báo cáo đối tượng, báo cáo quảng cáo tương tác và báo cáo DSA. Quảng cáo Mua sắm (Shopping Ads) được tạo qua API hoặc TikTok Ads Manager không bị ảnh hưởng.

| Bộ lọc (Filter Field) | Kiểu lọc hỗ trợ (Supported Filter Types) | Mô tả chi tiết (Description) |
|---|---|---|
| playable_ids | IN | Danh sách ID tài nguyên tương tác, bạn có thể truyền tối đa 100 `playable_id` khi dùng bộ lọc này. |
| country_code | IN | Location code. See **Appendix-Location IDs** for details. |
| orientation | IN | Display orientation. Các giá trị enum hỗ trợ: `PORTRAIT`, `LANDSCAPE`, `BOTH`. |
| playable_status | IN | Status. Các giá trị enum hỗ trợ: `VALIDATING`, `VALIDATE_FAIL`, `VALIDATE_SUCCESS`, `AUDIT_FAIL`, `AUDIT_SUCCESS`. |
| playable_name | MATCH | Playable name. |
| spend | LOWER_THAN/GREATER_THAN/RANGE | Total cost. |

---

<a id="doc-1738864960144385"></a>
<!-- doc_id: 1738864960144385 -->
<!-- doc_id: 1738864960144385 -->
# Báo cáo quảng cáo mua sắm động DSA (DSA reports)
> Đường dẫn: Marketing API > Reporting > Guides > Report types > DSA reports
Báo cáo Quảng cáo động (DSA - Dynamic Showcase Ads) là loại báo cáo cho phép bạn lấy dữ liệu về [Quảng cáo mua sắm video (cho Danh mục)](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1750361698613249) hoặc Quảng cáo động (còn gọi là Dynamic Product Ads). 

> **Note:**  • Chạy báo cáo DSA bất đồng bộ cho Video Shopping Ads có nguồn sản phẩm là danh mục hiện là tính năng chỉ dành cho danh sách cho phép (allowlist). Nếu muốn truy cập, vui lòng liên hệ đại diện TikTok của bạn. • Khi bạn chạy báo cáo DSA cho Video Shopping Ads có nguồn sản phẩm là danh mục, chỉ hỗ trợ chế độ bất đồng bộ. • Để báo cáo DSA tạo dữ liệu cho Quảng cáo động, bạn phải có quyền truy cập vào Dynamic Showcase Ads API. Nếu không, báo cáo sẽ không hiển thị dữ liệu. Dynamic Showcase Ads API là tính năng chỉ dành cho danh sách cho phép. • Không hỗ trợ chạy báo cáo DSA ở chế độ CHUNK (`query_mode`= `CHUNK`). Bạn chỉ có thể chạy báo cáo cơ bản đồng bộ ở chế độ CHUNK.

# Các chiều dữ liệu được hỗ trợ (Supported dimensions)
Xem [tại đây](bao-cao-p3.md#doc-1751625287345154) về các chiều dữ liệu được hỗ trợ của báo cáo DSA.
# Các chỉ số được hỗ trợ (Supported metrics)
Xem [tại đây](bao-cao-p3.md#doc-1751625293044737) về các chỉ số được hỗ trợ của báo cáo DSA.
# Các bộ lọc được hỗ trợ (Supported filters)
Xem [tại đây](bao-cao-p3.md#doc-1751625296192514) về các bộ lọc được hỗ trợ của báo cáo DSA. Chúng giống với các bộ lọc được hỗ trợ trong **Báo cáo cơ bản**. 
# Hỗ trợ theo thời gian trọn đời (Lifetime supports)
Chỉ số trọn đời (lifetime metrics) cho báo cáo DSA hiện chưa hỗ trợ trong phiên bản API v1.3. 

# Các trường hợp sử dụng (Use cases)

**1. Query the performance of catalog products in Video Shopping campaigns within a specific time period.** 

**Request Parameters**

``` xcodeblock
(code json JSON)
{
    "advertiser_id": "{{advertiser_id}}",
    "report_type":"CATALOG",
    "data_level":"AUCTION_CAMPAIGN",
    "dimensions": ["campaign_id","sku_id_v2"],
    "metrics": ["campaign_name","product_name_v2", "conversion", "complete_payment", "value_per_complete_payment","total_complete_payment_rate"],
    "start_date": "2023-12-01",
    "end_date": "2023-12-18"
}
(/code)
```

---

<a id="doc-1751625287345154"></a>
<!-- doc_id: 1751625287345154 -->
<!-- doc_id: 1751625287345154 -->
# Các chiều dữ liệu được hỗ trợ (Supported dimensions)
> Đường dẫn: Marketing API > Reporting > Guides > Report types > DSA reports > Supported dimensions
A dimension is an attribute to group your data by. DSA reports support the following dimensions. Please note that currently, we don't support all dimensions available on TikTok Ads Manager.

# Dành cho Quảng cáo danh mục (For Catalog Ads)

> **Note:** 
> Khi bạn chạy báo cáo DSA cho Catalog Ads (trước đây gọi là Video Shopping Ads với nguồn sản phẩm là danh mục), chỉ hỗ trợ chế độ bất đồng bộ.

## Các chiều dữ liệu được hỗ trợ (Supported dimensions)

| Dimension Name | Description |
|---|---|
| advertiser_id | Nhóm theo ID tài khoản quảng cáo TikTok (Advertiser ID). |
| campaign_id | Nhóm theo ID chiến dịch quảng cáo (Campaign ID). |
| adgroup_id | Nhóm theo ID nhóm quảng cáo (Adgroup ID). |
| ad_id_v2 | Nhóm theo ID mẫu quảng cáo (Ad ID). ⏎ Các loại dữ liệu bạn có thể nhận được bao gồm: • the ad level data for Manual Ads • the ad level data for Smart+ Campaigns • the **ad (asset group)** level data for Upgraded Smart+ Ads ⏎ **Note**: • You cannot use it together with the dimension `ad_id`, the filter `ad_ids`, or the attribute metric `ad_id`. |
| ad_id | Nhóm theo ID mẫu quảng cáo (Ad ID). ⏎ Các loại dữ liệu bạn có thể nhận được bao gồm: • the ad level data for Manual Ads • the ad level data for Smart+ Campaigns • the **creative** level data for Upgraded Smart+ Ads |
| stat_time_day | Group by day. |
| catalog_id_v2 | Group by ID danh mục sản phẩm |
| product_id_v2 | Group by Catalog product ID. |
| sku_id_v2 | Group by SKU ID. |
| brand | Group by Brand. ⏎ **Note**:  • See the “**Dimension grouping**” section below to learn about the supported dimension grouping. • This dimension is supported at all levels (`data_level` = `AUCTION_CAMPAIGN`, `AUCTION_ADGROUP`, `AUCTION_AD`, or `AUCTION_ADVERTISER`). • The supported metrics for this dimension are:  • `offline_shopping_events` • `value_per_offline_shopping_event` • `offline_shopping_events_value` • `total_purchase_value` • `total_complete_payment_rate` • `conversion` |
| content_category | Group by Content Category. ⏎ **Note**:  • See the “**Dimension grouping**” section below to learn about the supported dimension grouping. • This dimension is supported at all levels (`data_level` = `AUCTION_CAMPAIGN`, `AUCTION_ADGROUP`, `AUCTION_AD`, or `AUCTION_ADVERTISER`). • The supported metrics for this dimension are:  • `offline_shopping_events` • `value_per_offline_shopping_event` • `offline_shopping_events_value` • `total_purchase_value` • `total_complete_payment_rate` • `conversion` |

## Nhóm chiều dữ liệu (Dimension grouping)

Các chiều dữ liệu được hỗ trợ được phân loại thành chiều ID, thời gian, DSA và chiều Thương hiệu. 
- ID Dimensions：`advertiser_id`, `campaign_id`, `adgroup_id`, `ad_id`
- Time Dimensions: `stat_time_day`
- DSA Dimensions: `catalog_id_v2`,  `product_id_v2`, `sku_id_v2`
- Brand Dimensions: `brand`, `content_category`.

Trong yêu cầu của bạn, nếu không sử dụng chiều Thương hiệu, bạn cần có ít nhất một chiều DSA. Chiều ID và thời gian là tùy chọn:
- One or more DSA dimensions **(Bắt buộc)** + single ID dimension *(Không bắt buộc)* + single time dimension *(Không bắt buộc)*

Nếu bạn muốn sử dụng chiều Thương hiệu, hãy đảm bảo nhóm chiều dữ liệu của bạn đáp ứng yêu cầu sau:
- One Brand dimension **(Bắt buộc)** + single DSA dimension *(Không bắt buộc)* + single ID dimension *(Không bắt buộc)* + single time dimension *(Không bắt buộc)* 

> **Note:** 
> Số lượng chiều dữ liệu tối đa bạn có thể sử dụng trong một yêu cầu là 4. Sử dụng quá nhiều chiều có thể dẫn đến thời gian xử lý lâu hơn.

# Dành cho Quảng cáo giới thiệu động (For Dynamic Showcase Ads)
## Các chiều dữ liệu được hỗ trợ (Supported dimensions)

| Dimension Name | Description |
|---|---|
| advertiser_id | Group by ID tài khoản quảng cáo TikTok |
| campaign_id | Group by ID chiến dịch quảng cáo ⏎ **Note**: By default the `campaign_status` filter is applied and defaults to `STATUS_NOT_DELETE` in synchronous DSA reports. If you want to get breakdown data for all campaigns including the deleted ones via synchronous DSA reports, you need to set `campaign_status` to `STATUS_ALL`. |
| adgroup_id | Group by ID nhóm quảng cáo ⏎ **Note**: By default the `adgroup_status` filter is applied and defaults to `STATUS_NOT_DELETE` in synchronous DSA reports. If you want to get breakdown data for all ad groups including the deleted ones via synchronous DSA reports, you need to set `adgroup_status` to `STATUS_ALL`. |
| ad_id | Group by ID mẫu quảng cáo ⏎ **Note**: By default the `ad_status` filter is applied and defaults to `STATUS_NOT_DELETE` in synchronous DSA reports. If you want to get breakdown data for all ads including the deleted ones via synchronous DSA reports, you need to set `ad_status` to `STATUS_ALL`. |
| stat_time_day | Nhóm theo ngày (Group by day) |
| catalog_id | Group by ID danh mục sản phẩm |
| product_set_id | Group by Product Set ID |
| product_id | Group by Product ID |
| sku_id | Group by SKU ID |

## Nhóm chiều dữ liệu (Dimension grouping)

Các chiều dữ liệu được hỗ trợ được phân loại thành các chiều ID, thời gian và DSA. 
- ID Dimensions：`advertiser_id`, `campaign_id`, `adgroup_id`, `ad_id`
- Time Dimensions: `stat_time_day`
- DSA Dimensions: `catalog_id`, `product_set_id`, `product_id`, `sku_id`

Trong yêu cầu của bạn, cần có ít nhất một chiều DSA. Chiều ID và thời gian là tùy chọn. 
- Multiple DSA dimensions **(Bắt buộc)** + single ID dimension *(Không bắt buộc)* + single time dimension *(Không bắt buộc)*

> **Note:** Đối với chiều DSA, không được sử dụng đồng thời `product_set_id` cùng với `product_id` hoặc `sku_id`.

---

<a id="doc-1751625293044737"></a>
<!-- doc_id: 1751625293044737 -->
<!-- doc_id: 1751625293044737 -->
# Các chỉ số được hỗ trợ (Supported metrics)
> Đường dẫn: Marketing API > Reporting > Guides > Report types > DSA reports > Supported metrics
Bạn có thể sử dụng các chỉ số sau trong báo cáo DSA. Các chỉ số không phát sinh tiêu dùng sẽ được trả về dạng `-`. Xin lưu ý hiện tại chúng tôi chưa hỗ trợ toàn bộ các chỉ số có trên Trình quản lý quảng cáo TikTok.

## Dành cho Quảng cáo danh mục (For Catalog Ads)
> **Note:** 
> Khi bạn chạy báo cáo DSA cho Catalog Ads (trước đây gọi là Video Shopping Ads với nguồn sản phẩm là danh mục), chỉ hỗ trợ chế độ bất đồng bộ.

### Chỉ số thuộc tính (Attribute metrics)
Attribute metrics are basic attributes of your campaigns, ad groups or ads. Attribute metrics are Chỉ hợp lệ khi an ID type of dimension is used.

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
| ---- | ---- | ---- |
| product_name_v2 | string | Catalog product name |
| product_image_v2 | string | Catalog product image |
| catalog_name_v2 | string | Catalog name |
| campaign_name | string | Campaign name. Được hỗ trợ ở cấp Chiến dịch, Nhóm quảng cáo và Quảng cáo. |
| campaign_id | string | ID chiến dịch quảng cáo. Được hỗ trợ ở cấp Nhóm quảng cáo và Quảng cáo. |
| adgroup_name | string | Ad group name. Được hỗ trợ ở cấp Nhóm quảng cáo và Quảng cáo. |
| adgroup_id | string | ID nhóm quảng cáo. Được hỗ trợ ở cấp Quảng cáo. |
| ad_id_v2 | string | Các loại dữ liệu bạn có thể nhận được bao gồm:<ul><li>the ad IDs of Manual Ads.</li><li>the ad IDs of Smart+ Campaigns.</li><li>the ad IDs of Upgraded Smart+ Ads.</li></ul><br><ul><li>You cannot use it together with the dimension `ad_id`, the filter `ad_ids`, or the attribute metric `ad_id`.</li></ul><br>Được hỗ trợ ở cấp Quảng cáo. |
| ad_name | string | Ad name. Được hỗ trợ ở cấp Quảng cáo. |

### Core metrics
Core metrics provide fundamental insights into your advertising performance, covering essential aspects.

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết | Chi tiết hỗ trợ (Detail) |
|---|---|---|---|
| conversion | string | Conversions | Number of times your ad resulted in the optimization event you selected.|

### Product metrics
Product metrics are data about the performance of your products.

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết | Chi tiết hỗ trợ (Detail) |
|---|---|---|---|
| product_impressions | string | Product impressions | Number of times your products were shown. |
| product_clicks | string | Product clicks (destination) | Number of clicks from your products to a specified destination. |
| product_cta | string | Product click-through rate (destination) | Percentage of product impressions that resulted in a destination click out of all product impressions. |

### App metrics
App metrics measure actions taken in relation to mobile apps.

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết | Chi tiết hỗ trợ (Detail) |
|---|---|---|---|
| Purchase |  |  |  |
| ↳ purchase | string | Unique purchases (app) | The number of unique app purchase actions attributed to your ads. |
| ↳ total_purchase | string | Purchases (app) | The number of app purchase actions attributed to your ads. |
| ↳ value_per_total_purchase | string | Value per purchase (app) | The average value per app purchase action attributed to your ads. |
| ↳ total_purchase_value | string | Purchase value (app) | The total value of app purchase actions attributed to your ads. |
| Add to Cart |  |  |  |
| ↳ app_event_add_to_cart | string | Unique adds to cart (app) | The number of unique app add to cart actions attributed to your ads. |
| ↳ total_app_event_add_to_cart | string | Adds to cart (app) | The number of app add to cart actions attributed to your ads. |
| ↳ value_per_total_app_event_add_to_cart | string | Value per add to cart (app) | The average value per app add to cart action attributed to your ads. |
| ↳ total_app_event_add_to_cart_value | string | Add to cart value (app) | The total value of app add to cart actions attributed to your ads. |
| Checkout |  |  |  |
| ↳ checkout | string | Unique checkouts (app) | The number of unique app checkout actions attributed to your ads. |
| ↳ total_checkout | string | Checkouts (app) | The number of app checkout actions attributed to your ads. |
| ↳ value_per_checkout | string | Value per checkout (app) | The average value per app checkout action attributed to your ads. |
| ↳ total_checkout_value | string | Checkout value (app) | The total value of app checkout actions attributed to your ads. |
| View Content |  |  |  |
| ↳ view_content | string | Unique content views (app) | The number of unique app view content actions attributed to your ads. |
| ↳ total_view_content | string | Content views (app) | The number of app view content actions attributed to your ads. |
| ↳ value_per_total_view_content | string | Value per content view (app) | The average value per app view content action attributed to your ads. |
| ↳ total_view_content_value | string | Content view value (app) | The total value of app view content actions attributed to your ads. |

### Website metrics
Website metrics measure actions taken on websites as a result of ads, such as completed purchases. 

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết | Chi tiết hỗ trợ (Detail) |
|---|---|---|---|
| Purchase |  |  |  |
| ↳ complete_payment | string | Purchases (website) | The number of website purchase actions attributed to your ads. |
| ↳ value_per_complete_payment | string | Value per purchase (website) | The average value per website purchase action attributed to your ads. |
| ↳ total_complete_payment_rate | string | Purchase value (website) | The total value of website purchase actions attributed to your ads. |
| Page View |  |  |  |
| ↳ total_pageview | string | Total Page View | The total number of page view events.The total count is calculated based on the time each ad impression occurred. |
| ↳ avg_value_per_pageview | string | Value per Page View | The average value returned from page view events. |
| ↳ total_value_per_pageview | string | Total Page View Value | The total value returned from page view events. |
| View Content |  |  |  |
| ↳ page_content_view_events | string | Content views (page) | The number of page view content actions attributed to your ads. |
| ↳ value_per_page_content_view_event | string | Value per content view (page) | The average value per page view content action attributed to your ads. |
| ↳ total_page_view_content_events_value | string | Content view value (page) | The total value of page view content actions attributed to your ads. |
| Add to Cart |  |  |  |
| ↳ web_event_add_to_cart | string | Adds to cart (page) | The number of page add to cart actions attributed to your ads. |
| ↳ value_per_web_event_add_to_cart | string | Value per add to cart (page) | The average value per page add to cart action attributed to your ads. |
| ↳ total_web_event_add_to_cart_value | string | Add to cart value (page) | The total value of page add to cart actions attributed to your ads. |
| Initiate Checkout |  |  |  |
| ↳ initiate_checkout | string | Checkouts initiated (page) | The number of page initiate checkout actions attributed to your ads. |
| ↳ value_per_initiate_checkout | string | Value per checkout initiated (page) | The average value per page initiate checkout action attributed to your ads. |
| ↳ total_initiate_checkout_value | string | Checkout initiation value (page) | The total value of page initiate checkout actions attributed to your ads. |

### Offline metrics
Offline metrics measure offline actions attributed to ads, such as completed purchases in physical stores.

 
| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết | Chi tiết hỗ trợ (Detail) |
|---|---|---|---|
| Purchase |  |  |  |
| ↳ offline_shopping_events | string | Purchases (offline) | The number of offline purchase actions attributed to your ads. |
| ↳ value_per_offline_shopping_event | string | Value per purchase (offline) | The average value per offline purchase action attributed to your ads. |
| ↳ offline_shopping_events_value | string | Purchase value (offline) | The total value of offline purchase actions attributed to your ads. |

### Chỉ số phân bổ (Attribution metrics)
Attribution metrics are data about how events are attributed.

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết | Chi tiết hỗ trợ (Detail) |
|---|---|---|---|
| vta_conversion | string | VTA Conversion | The number of conversion events that are attributed to an ad impression. |
| vta_complete_payment | string | VTA Complete Payment | Complete payment events attributed to someone only viewing your ad. |
| vta_complete_payment_value | string | Total VTA Complete Payment Value | Total value of complete payment events attributed to someone only viewing your ad. |
| cta_conversion | string | CTA Conversion | The number of conversion events that are attributed to a click on your ad. |
| cta_complete_payment | string | CTA Complete Payment | Complete payment events attributed to someone clicking on your ad. |
| cta_complete_payment_value | string | Total CTA Complete Payment Value | Total value of complete payment events attributed to someone clicking on your ad. |

## Dành cho Quảng cáo giới thiệu động (For Dynamic Showcase Ads)
### Chỉ số thuộc tính (Attribute metrics)
 Các chỉ số thuộc tính (Attribute metrics), chẳng hạn như tên nhóm quảng cáo và loại quảng bá, là các thuộc tính cơ bản của chiến dịch, nhóm quảng cáo hoặc quảng cáo. Chỉ số thuộc tính chỉ hợp lệ khi sử dụng một chiều dữ liệu loại ID. 
| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
| ---- | ---- | ---- |
| catalog_name | string |Catalog name |
| product_set_name | string | Product set name|
| product_name | string | Product name |
| campaign_name | string | Campaign name. Được hỗ trợ ở cấp Chiến dịch, Nhóm quảng cáo và Quảng cáo. |
| campaign_id | string| ID chiến dịch quảng cáo. Được hỗ trợ ở cấp Nhóm quảng cáo và Quảng cáo. |
| adgroup_name | string | Ad group name. Được hỗ trợ ở cấp Nhóm quảng cáo và Quảng cáo. |
| placement_type| string | Placement type. Được hỗ trợ ở cấp Nhóm quảng cáo và Quảng cáo. |
| adgroup_id | string| ID nhóm quảng cáo. Được hỗ trợ ở cấp Quảng cáo. |
| ad_name | string | Ad name. Được hỗ trợ ở cấp Quảng cáo. |
| ad_text | string | Ad text. Được hỗ trợ ở cấp Quảng cáo. |
|product_image|string| URL of the product image. Supported at ad level.|
| tt_app_id | string | TikTok App ID, the App ID you used when creating an Ad Group. Được hỗ trợ ở cấp Nhóm quảng cáo và Quảng cáo. Returned if the promotion type of one Ad Group is App. |
| tt_app_name | string | TikTok App Name. The name of your TikTok App. Được hỗ trợ ở cấp Nhóm quảng cáo và Quảng cáo. Returned if the promotion type of one Ad Group is App. |
| mobile_app_id | string | Mobile App ID. Examples: <ul><li>App Store: https://apps.apple.com/us/app/angry-birds/id<b>343200656.</li><li>Google Play: https://play.google.com/store/apps/details?id=<b>com.rovio.angrybirds</b></li>Được hỗ trợ ở cấp Nhóm quảng cáo và Quảng cáo. Returned if the promotion type of one Ad Group is App. |
|promotion_type|string| Promotion type. It can be app, website, or others. Supported at Adgroup and Ad levels in both synchronous and asynchronous reports. |
|dpa_target_audience_type| string | Target audience type for DPA. The Audience that DPA products target. Supported at Adgroup or Ad levels in both synchronous and asynchronous reports.|
### Chỉ số dữ liệu cơ bản (Basic data metrics)
 Các chỉ số dữ liệu cơ bản (Basic data metrics) là dữ liệu về chi phí và hiệu suất phân phối quảng cáo của bạn. 
| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
| ---- | ---- | ---- |
| impressions | string | Impressions. The number of times your ads were on screen. |
| clicks | string | Clicks (Destination). The number of clicks on your ads that led to advertiser-specified destinations.<br><p><span style="color:darkred"><b>Note</b></span>: Starting from July 6, the metric name in async reports has been updated from Clicks to Clicks (Destination).  |
| spend| string | Total Cost. The estimated total amount of money you've spent on your campaign, ad group or ad during its schedule. |
| conversion| string |Conversions. <br>The number of times your ad achieved an outcome based on the objective and settings you selected. <br>(The total count is calculated based on the time each ad impression occurred.)|
| cost_per_conversion | string | CPA. The average amount of money you've spent on a conversion. (The total count is calculated based on the time each ad impression occurred.) |
| conversion_rate | string | CVR (Clicks) .The percentage of conversions from all clicks on your ads. <br>(The total count is calculated based on the time each ad impression occurred.) <br><p><span style="color:darkred"><b>Note</b></span>: Starting late October, 2023, the calculation logic for this metric will be updated to be impression-based (the same as `conversion_rate_v2`). To ensure a smooth API integration and avoid disruptions caused by the change in calculation logic, we recommend you switch to using the impression-based metric `conversion_rate_v2` as soon as possible. |
| conversion_rate_v2 | string | CVR (Impressions). The percentage of conversions from all impressions on your ads. <br>  (The total count is calculated based on the time each ad impression occurred.) |
| ctr | string | CTR (Destination). The percentage of times people saw your ad and performed a click (destination).<br><p><span style="color:darkred"><b>Note</b></span>: Starting from July 6, the metric name in async reports has been updated from CTR to CTR (Destination). |
| cpc | string | CPC (Destination). The average amount of money you've spent on a click (destination). <br><p><span style="color:darkred"><b>Note</b></span>: Starting from July 6, the metric name in async reports has been updated from CPC to CPC (Destination). |
| cpm | string | CPM. The average amount of money you've spent per 1,000 impressions. |
| real_time_result | string | Real-time Result. The number of times your ad achieved an outcome, based on the optimization goal you selected. As a campaign may have different optimization goals, the total number of result is not supported in campaign section now. Please go to the ad group section to view the result. (The total count is based on when the conversion actually happened.) |
| real_time_cost_per_result| string | Real-time Cost Per Result. As a campaign may have different optimization goals, the total number of result is not supported in campaign section now, please go to the ad group section to view the cost per Result. (The total count is based on when the conversion actually happened.) |
| real_time_result_rate | string | Real-time Result Rate (%). As a campaign may have different optimization goals, the total number of result is not supported in campaign section now. Please go to the ad group section to view the Result Rate. (The total count is based on when the conversion actually happened.) |
| result | string | Result. The number of times your ad achieved an outcome, based on the optimization goal you selected. As one campaign may have a number of different optimization goals, this statistic is not supported for campaigns. Please go to ad groups or ads to view the results. (The total count is calculated based on the time each ad impression occurred.) |
| cost_per_result| string | Cost Per Result. The average cost for each result from your ads. As one campaign may have a number of different optimization goals, this statistic is not supported for campaigns. Please go to ad groups or ads to view the cost per result. (The total count is calculated based on the time each ad impression occurred.) |
| result_rate | string | Result Rate (%). The percentage of results you achieved out of all of the views/clicks on your ads. As one campaign may have a number of different optimization goals, this statistic is not supported for campaigns. Please go to ad groups or ads to view the result rate. (The total count is calculated based on the time each ad impression occurred.) |
| currency | string | The currency code, e. g. USD. Note that if you want to use `currency` as metrics, then the `dimensions` field in your request must include `adgroup_id`/`ad_id`/`campaign_id`/`advertiser_id`. |
### In-App Event metrics
 Các chỉ số sự kiện trong ứng dụng (In-App event metrics) là dữ liệu về các sự kiện chuyển đổi diễn ra trong ứng dụng. 

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết | Chi tiết hỗ trợ (Detail) |
|---|---|---|---|
| Real-time App Install |  |  |  |
| ↳ real_time_app_install | string | Real-time App Install | The number of times your mobile app was installed that were recorded as app events and attributed to your ads. (The total count is based on when the conversion actually happened.) |
| ↳ real_time_app_install_cost | string | Cost per Real-time App Install | The average cost for each app install event. (The total count is based on when the conversion actually happened.) |
| App Install |  |  |  |
| ↳ app_install | string | App Install | The number of times your mobile app was installed that were recorded as app events and attributed to your ads. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ cost_per_app_install | string | Cost per App Install | The average cost for each app install event. (The total count is calculated based on the time each ad impression occurred.) |
| Registration |  |  |  |
| ↳ registration | string | Unique Registration | The number of unique registrations in your mobile app that were recorded as app events and attributed to your ads. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ cost_per_registration | string | Cost per Unique Registration | The average cost for each unique registration that is attributed to your ad. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ registration_rate | string | Registration Rate (%) | The percentage of unique registration events out of all app install events. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ total_registration | string | Total Registration | Total Registration. The total count is based on when you were billed. |
| ↳ cost_per_total_registration | string | Cost per Registration | Cost per Registration (The total count is based on when you were billed.) |
| Purchase |  |  |  |
| ↳ purchase | string | Unique Purchase | The number of unique purchases event occurred in your app that were recorded by your measurement partner. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ cost_per_purchase | string | Cost per Unique Purchase | The average cost of each unique purchase. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ purchase_rate | string | Purchase Rate (%) | The percentage of unique purchase event out of all the app install event. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ total_purchase | string | Purchase (Total No.) | Purchase (Total No.) (The total count is based on when you were billed.) |
| ↳ cost_per_total_purchase | string | Cost per Purchase | Cost per Purchase (The total count is based on when you were billed.) |
| ↳ value_per_total_purchase | string | Value per Purchase | Value per Purchase (The total count is based on when you were billed.) |
| ↳ total_purchase_value | string | Total Purchase Value | Total Purchase Value (The total count is based on when you were billed.) |
| ↳ total_active_pay_roas | string | Purchase ROAS | Return on ad spend (ROAS) from purchase events. (The total count is based on when you were billed.) |
| Add to Cart |  |  |  |
| ↳ app_event_add_to_cart | string | Unique Add to Cart | The number of unique times a user added items to a shopping cart in your mobile app that were recorded as app events and attributed to your ads. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ cost_per_app_event_add_to_cart | string | Cost per Unique Add to Cart | The average cost for each unique add to cart event that is attributed to your ads. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ app_event_add_to_cart_rate | string | Unique Add to Cart Rate (%) | The percentage of unique add to cart events out of all app install events. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ total_app_event_add_to_cart | string | Total Add to Cart | Add to Cart (Total No.) (The total count is based on when you were billed.) |
| ↳ cost_per_total_app_event_add_to_cart | string | Cost per Add to Cart | Cost per Add to Cart (The total count is based on when you were billed.) |
| ↳ value_per_total_app_event_add_to_cart | string | Value per Add to Cart | Value per Add to Cart (The total count is based on when you were billed.) |
| ↳ total_app_event_add_to_cart_value | string | Total Add to Cart Value | Total Add to Cart Value (The total count is based on when you were billed.) |
| Checkout |  |  |  |
| ↳ checkout | string | Unique Checkout | The number of unique times a user made a checkout in your mobile app that were recorded as app events and attributed to your ads. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ cost_per_checkout | string | Cost per Unique Checkout | The average cost for each unique checkout event that is attributed to your ads. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ checkout_rate | string | Unique Checkout Rate (%) | The percentage of unique checkout events out of all app install events. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ total_checkout | string | Total Checkout | Checkout (Total No.) (The total count is based on when you were billed.) |
| ↳ cost_per_total_checkout | string | Cost per Checkout | Cost per Checkout (The total count is based on when you were billed.) |
| ↳ value_per_checkout | string | Value per Checkout | Value per Checkout (The total count is based on when you were billed.) |
| ↳ total_checkout_value | string | Total Checkout Value | Total Checkout Value (The total count is based on when you were billed.) |
| View Content |  |  |  |
| ↳ view_content | string | Unique View Content | The number of unique times a user viewed content in your mobile app that were recorded as app events and attributed to your ads. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ cost_per_view_content | string | Cost per Unique View Content | The average cost for each unique view content event that is attributed to your ads. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ view_content_rate | string | View Content Rate (%) | The percentage of unique view content events out of all app install events. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ total_view_content | string | Total View Content | Total View Content. The total count is based on when you were billed. |
| ↳ cost_per_total_view_content | string | Cost per View Content | Cost per View Content (The total count is based on when you were billed.) |
| ↳ value_per_total_view_content | string | Value per View Content | Value per View Content (The total count is based on when you were billed.) |
| ↳ total_view_content_value | string | Total View Content Value | Total View Content Value (The total count is based on when you were billed.) |
| Day 1 Retention |  |  |  |
| ↳ next_day_open | string | Unique Day 1 Retention | The number of unique day 1 retentions in your mobile app that were recorded as app events and attributed to your ads. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ cost_per_next_day_open | string | Cost per Unique Day 1 Retention | The average cost for each unique day 1 retention event that is attributed to your ads. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ next_day_open_rate | string | Day 1 Retention Rate (%) | The percentage of unique day 1 retention events out of all app install events. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ total_next_day_open | string | Day 1 Retention (Total No.) | Day 1 Retention (Total No.) (The total count is based on when you were billed.) |
| ↳ cost_per_total_next_day_open | string | Cost per Day 1 Retention | Cost per Day 1 Retention (The total count is based on when you were billed.) |
| Add Payment Info |  |  |  |
| ↳ add_payment_info | string | Unique Add Payment Info | The number of unique times a user added payment info in your mobile app that were recorded as app events and attributed to your ads. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ cost_per_add_payment_info | string | Cost per Unique Add Payment Info | The average cost for each unique add payment info event that is attributed to your ads. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ add_payment_info_rate | string | Add Payment Info Rate (%) | The percentage of unique add payment info events out of all app install events. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ total_add_payment_info | string | Total Add Payment Info | Total Add Payment Info. The total count is based on when you were billed. |
| ↳ cost_total_add_payment_info | string | Cost per Add Payment Info | Cost per Add Payment Info (The total count is based on when you were billed.) |
| Add to Wishlist |  |  |  |
| ↳ add_to_wishlist | string | Unique Add to Wishlist | The number of unique times users added items to a wishlist in your mobile app that were recorded as app events and attributed to your ads. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ cost_per_add_to_wishlist | string | Cost per Unique Add to Wishlist | The average cost for each unique add to wishlist event that is attributed to your ads. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ add_to_wishlist_rate | string | Add to Wishlist Rate (%) | The percentage of unique add to wishlist events out of all app install events. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ total_add_to_wishlist | string | Total Add to Wishlist | Add to Wishlist (Total No.) (The total count is based on when you were billed.) |
| ↳ cost_per_total_add_to_wishlist | string | Cost per Add to Wishlist | Cost per Add to Wishlist (The total count is based on when you were billed.) |
| ↳ value_per_total_add_to_wishlist | string | Value per Add to Wishlist | Value per Add to Wishlist (The total count is based on when you were billed.) |
| ↳ total_add_to_wishlist_value | string | Total Add to Wishlist Value | Total Add to Wishlist Value (The total count is based on when you were billed.) |
| Launch App |  |  |  |
| ↳ launch_app | string | Unique Launch App | The number of unique times a user launched your mobile app that were recorded as app events and attributed to your ads. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ cost_per_launch_app | string | Cost per Unique Launch App | The average cost for each unique launch app event that is attributed to your ads. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ launch_app_rate | string | Launch App Rate (%) | The percentage of unique launch app events out of all app install events. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ total_launch_app | string | Launch App (Total No.) | Launch App (Total No.) (The total count is based on when you were billed.) |
| ↳ cost_per_total_launch_app | string | Cost per Launch App | Cost per Launch App (The total count is based on when you were billed.) |
| Complete Tutorial |  |  |  |
| ↳ complete_tutorial | string | Unique Complete Tutorial | The number of unique times a user completed a tutorial in your mobile app that were recorded as app events and attributed to your ads. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ cost_per_complete_tutorial | string | Cost per Unique Complete Tutorial | The average cost for each unique complete tutorial event that is attributed to your ads. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ complete_tutorial_rate | string | Complete Tutorial Rate (%) | The percentage of unique complete tutorial events out of all app install events. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ total_complete_tutorial | string | Complete Tutorial (Total No.) | Complete Tutorial (Total No.) (The total count is based on when you were billed.) |
| ↳ cost_per_total_complete_tutorial | string | Cost per Complete Tutorial | Cost per Complete Tutorial (The total count is based on when you were billed.) |
| ↳ value_per_total_complete_tutorial | string | Value per Complete Tutorial | Value per Complete Tutorial (The total count is based on when you were billed.) |
| ↳ total_complete_tutorial_value | string | Total Complete Tutorial Value | Total Complete Tutorial Value (The total count is based on when you were billed.) |
| Create Group |  |  |  |
| ↳ create_group | string | Unique Create Group | The number of unique times a user created a group in your mobile game app that were recorded as app events and attributed to your ads. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ cost_per_create_group | string | Cost per Unique Create Group | The average cost for each unique create group event that is attributed to your ads. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ create_group_rate | string | Create Group Rate (%) | The percentage of unique create group events out of all app install events. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ total_create_group | string | Create Group (Total No.) | Create Group (Total No.) (The total count is based on when you were billed.) |
| ↳ cost_per_total_create_group | string | Cost per Create Group | Cost per Create Group (The total count is based on when you were billed.) |
| ↳ value_per_total_create_group | string | Value per Create Group | Value per Create Group (The total count is based on when you were billed.) |
| ↳ total_create_group_value | string | Total Create Group Value | Total Create Group Value (The total count is based on when you were billed.) |
| Join Group |  |  |  |
| ↳ join_group | string | Unique Join Group | The number of unique times a user joined a group in your mobile game app that were recorded as app events and attributed to your ads. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ cost_per_join_group | string | Cost per Unique Join Group | The average cost for each unique join group event that is attributed to your ads. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ join_group_rate | string | Join Group Rate (%) | The percentage of unique join group events out of all app install events. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ total_join_group | string | Join Group (Total No.) | Join Group (Total No.) (The total count is based on when you were billed.) |
| ↳ cost_per_total_join_group | string | Cost per Join Group | Cost per Join Group (The total count is based on when you were billed.) |
| ↳ value_per_total_join_group | string | Value per Join Group | Value per Join Group (The total count is based on when you were billed.) |
| ↳ total_join_group_value | string | Total Join Group Value | Total Join Group Value (The total count is based on when you were billed.) |
| Create Role |  |  |  |
| ↳ create_gamerole | string | Unique Create Role | The number of unique times a user created a character or role in your mobile game app that were recorded as app events and attributed to your ads. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ cost_per_create_gamerole | string | Cost per Unique Create Role | The average cost for each unique create role event that is attributed to your ads. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ create_gamerole_rate | string | Unique Create Role Rate (%) | The percentage of unique create role events out of all app install events. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ total_create_gamerole | string | Create Role (Total No.) | Create Role (Total No.) (The total count is based on when you were billed.) |
| ↳ cost_per_total_create_gamerole | string | Cost per Create Role | Cost per Create Role (The total count is based on when you were billed.) |
| ↳ value_per_total_create_gamerole | string | Value per Create Role | Value per Create Role (The total count is based on when you were billed.) |
| ↳ total_create_gamerole_value | string | Total Create Role Value | Total Create Role Value (The total count is based on when you were billed.) |
| Spend Credit |  |  |  |
| ↳ spend_credits | string | Unique Spend Credit | The number of unique times a user spent credit in your mobile game app that were recorded as app events and attributed to your ads. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ cost_per_spend_credits | string | Cost per Unique Spend Credit | The average cost for each unique spend credits event that is attributed to your ads. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ spend_credits_rate | string | Spend Credit Rate (%) | The percentage of unique spend credits events out of all app install events. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ total_spend_credits | string | Spend Credit (Total No.) | Spend Credit (Total No.) (The total count is based on when you were billed.) |
| ↳ cost_per_total_spend_credits | string | Cost per Spend Credit | Cost per Spend Credit (The total count is based on when you were billed.) |
| ↳ value_per_total_spend_credits | string | Value per Spend Credit | Value per Spend Credit (The total count is based on when you were billed.) |
| ↳ total_spend_credits_value | string | Total Spend Credit Value | Total Spend Credit Value (The total count is based on when you were billed.) |
| Achieve Level |  |  |  |
| ↳ achieve_level | string | Unique Achieve Level | The number of unique times a user achieved a level in your mobile app that were recorded as app events and attributed to your ads. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ cost_per_achieve_level | string | Cost per Unique Achieve Level | The average cost for each unique achieve level event that is attributed to your ads. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ achieve_level_rate | string | Achieve Level Rate (%) | The percentage of unique achieve level events out of all app install events. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ total_achieve_level | string | Achieve Level (Total No.) | Achieve Level (Total No.) (The total count is based on when you were billed.) |
| ↳ cost_per_total_achieve_level | string | Cost per Achieve Level | Cost per Achieve Level (The total count is based on when you were billed.) |
| ↳ value_per_total_achieve_level | string | Value per Achieve Level | Value per Achieve Level (The total count is based on when you were billed.) |
| ↳ total_achieve_level_value | string | Total Achieve Level Value | Total Achieve Level Value (The total count is based on when you were billed.) |
| Unlock Achievement |  |  |  |
| ↳ unlock_achievement | string | Unique Unlock Achievement | The number of unique times that a user unlocked an achievement in your mobile game app that were recorded as app events and attributed to your ads. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ cost_per_unlock_achievement | string | Cost per Unique Unlock Achievement | The average cost for each unique unlock achievement event that is attributed to your ads. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ unlock_achievement_rate | string | Unlock Achievement Rate (%) | The percentage of unique unlock achievement events out of all app install events. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ total_unlock_achievement | string | Unlock Achievement (Total No.) | Unlock Achievement (Total No.) (The total count is based on when you were billed.) |
| ↳ cost_per_total_unlock_achievement | string | Cost per Unlock Achievement | Cost per Unlock Achievement (The total count is based on when you were billed.) |
| ↳ value_per_total_unlock_achievement | string | Value per Unlock Achievement | Value per Unlock Achievement (The total count is based on when you were billed.) |
| ↳ total_unlock_achievement_value | string | Total Unlock Achievement Value | Total Unlock Achievement Value (The total count is based on when you were billed.) |
| Generate Lead |  |  |  |
| ↳ sales_lead | string | Unique Generate Lead | The number of unique leads generated in your mobile app that were recorded as app events and attributed to your ads. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ cost_per_sales_lead | string | Cost per Unique Generate Lead | The average cost for each unique generate lead event that is attributed to your ads. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ sales_lead_rate | string | Generate Lead Rate (%) | The percentage of unique generate lead events out of all app install events. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ total_sales_lead | string | Generate Lead (Total No.) | Generate Lead (Total No.) (The total count is based on when you were billed.) |
| ↳ cost_per_total_sales_lead | string | Cost per Generate Lead | Cost per Generate Lead (The total count is based on when you were billed.) |
| ↳ value_per_total_sales_lead | string | Value per Generate Lead | Value per Generate Lead (The total count is based on when you were billed.) |
| ↳ total_sales_lead_value | string | Total Generate Lead Value | Total Generate Lead Value (The total count is based on when you were billed.) |
| In-App Ad Click |  |  |  |
| ↳ in_app_ad_click | string | Unique In-App Ad Click | The number of unique in-app ad click events that occurred in your mobile app and are attributed to your ads. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ cost_per_in_app_ad_click | string | Cost per Unique In-App Ad Click | The average cost for each unique in-app ad click event that is attributed to your ads. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ in_app_ad_click_rate | string | In-App Ad Click Rate (%) | The percentage of unique in-app ad click events out of all app install events. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ total_in_app_ad_click | string | In-App Ad Click (Total No.) | In-App Ad Click (Total No.) (The total count is based on when you were billed.) |
| ↳ cost_per_total_in_app_ad_click | string | Cost per In-App Ad Click | Cost per In-App Ad Click (The total count is based on when you were billed.) |
| ↳ value_per_total_in_app_ad_click | string | Value per In-App Ad Click | Value per In-App Ad Click (The total count is based on when you were billed.) |
| ↳ total_in_app_ad_click_value | string | Total In-App Ad Click Value | Total In-App Ad Click Value (The total count is based on when you were billed.) |
| In-App Ad Impression |  |  |  |
| ↳ in_app_ad_impr | string | Unique In-App Ad Impr | The number of unique in-app ad impression events that occurred in your mobile app and are attributed to your ads. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ cost_per_in_app_ad_impr | string | Cost per Unique In-App Ad Impr | The average cost for each unique in-app ad impression event that is attributed to your ads. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ in_app_ad_impr_rate | string | In-App Ad Impr Rate (%) | The percentage of unique in-app ad impression events out of all app install events. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ total_in_app_ad_impr | string | In-App Ad Impr (Total No.) | In-App Ad Impr (Total No.) (The total count is based on when you were billed.) |
| ↳ cost_per_total_in_app_ad_impr | string | Cost per In-App Ad Impr | Cost per In-App Ad Impr (The total count is based on when you were billed.) |
| ↳ value_per_total_in_app_ad_impr | string | Value per In-App Ad Impr | Value per In-App Ad Impr (The total count is based on when you were billed.) |
| ↳ total_in_app_ad_impr_value | string | Total In-App Ad Impr Value | Total In-App Ad Impr Value (The total count is based on when you were billed.) |
| Loan Apply |  |  |  |
| ↳ loan_apply | string | Unique Loan Apply | The number of unique times a user applied for a loan in your mobile app that were recorded as app events and attributed to your ads. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ cost_per_loan_apply | string | Cost per Unique Loan Apply | The average cost for each unique loan apply event that is attributed to your ads. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ loan_apply_rate | string | Loan Apply Rate (%) | The percentage of unique loan apply events out of all app install events. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ total_loan_apply | string | Loan Apply (Total No.) | Loan Apply (Total No.) (The total count is based on when you were billed.) |
| ↳ cost_per_total_loan_apply | string | Cost per Loan Apply | Cost per Loan Apply (The total count is based on when you were billed.) |
| Loan Approval |  |  |  |
| ↳ loan_credit | string | Unique Loan Approval | The number of unique times a user was approved a loan in your mobile app that were recorded as app events and attributed to your ads. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ cost_per_loan_credit | string | Cost per Unique Loan Approval | The average cost for each unique loan approval event that is attributed to your ads. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ loan_credit_rate | string | Loan Approval Rate (%) | The percentage of unique loan approval events out of all app install events. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ total_loan_credit | string | Loan Approval (Total No.) | Loan Approval (Total No.) (The total count is based on when you were billed.) |
| ↳ cost_per_total_loan_credit | string | Cost per Loan Approval | Cost per Loan Approval (The total count is based on when you were billed.) |
| Loan Disbursal |  |  |  |
| ↳ loan_disbursement | string | Unique Loan Disbursement | The number of unique loan disbursal in your mobile app that were recorded as app events and attributed to your ads. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ cost_per_loan_disbursement | string | Cost per Unique Loan Disbursement | The average cost for each unique loan disbursal event that is attributed to your ads. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ loan_disbursement_rate | string | Loan Disbursement Rate (%) | The number of unique loan disbursals in your mobile app that were recorded as app events and attributed to your ads. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ total_loan_disbursement | string | Loan Disbursement (Total No.) | Loan Disbursement (Total No.) (The total count is based on when you were billed.) |
| ↳ cost_per_total_loan_disbursement | string | Cost per Loan Disbursement | Cost per Loan Disbursement (The total count is based on when you were billed.) |
| Login |  |  |  |
| ↳ login | string | Unique Login | The number of unique logins in your mobile app that were recorded as app events and attributed to your ads. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ cost_per_login | string | Cost per Unique Login | The average cost for each unique login event that is attributed to your ads. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ login_rate | string | Login Rate (%) | The percentage of unique login events out of all app install events. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ total_login | string | Login (Total No.) | Login (Total No.) (The total count is based on when you were billed.) |
| ↳ cost_per_total_login | string | Cost per Login | Cost per Login (The total count is based on when you were billed.) |
| Rate |  |  |  |
| ↳ ratings | string | Unique Rate | The number of unique ratings in your mobile app that were recorded as app events and attributed to your ads. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ cost_per_ratings | string | Cost per Unique Rate | The average cost for each unique rate event that is attributed to your ads. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ ratings_rate | string | Rate Rate (%) | The percentage of unique rate events out of all app install events. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ total_ratings | string | Rate (Total No.) | Rate (Total No.) (The total count is based on when you were billed.) |
| ↳ cost_per_total_ratings | string | Cost per Rate | Cost per Rate (The total count is based on when you were billed.) |
| ↳ value_per_total_ratings | string | Value per Rate | Value per Rate (The total count is based on when you were billed.) |
| ↳ total_ratings_value | string | Total Rate Value | Total Rate Value (The total count is based on when you were billed.) |
| Search |  |  |  |
| ↳ search | string | Unique Search | The number of unique searches in your mobile app that were recorded as app events and attributed to your ads. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ cost_per_search | string | Cost per Unique Search | The average cost for each unique search event that is attributed to your ads. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ search_rate | string | Search Rate (%) | The percentage of unique search events out of all app install events. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ total_search | string | Total Search | Total search (The total count is based on when you were billed.) |
| ↳ cost_per_total_search | string | Cost per Search | Cost per Search (The total count is based on when you were billed.) |
| Start Trial |  |  |  |
| ↳ start_trial | string | Unique Start Trial | The number of unique times a user started a trial in your mobile app that were recorded as app events and attributed to your ads. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ cost_per_start_trial | string | Cost per Unique Start Trial | The average cost for each unique start trial event that is attributed to your ads. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ start_trial_rate | string | Start Trial Rate (%) | The percentage of unique start trial events out of all app install events. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ total_start_trial | string | Start Trial (Total No.) | Start Trial (Total No.) (The total count is based on when you were billed.) |
| ↳ cost_per_total_start_trial | string | Cost per Start Trial | Cost per Start Trial (The total count is based on when you were billed.) |
| Subscribe |  |  |  |
| ↳ subscribe | string | Unique Subscribe | The number of unique subscriptions in your mobile app that were recorded as app events and attributed to your ads. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ cost_per_subscribe | string | Cost per Unique Subscribe | The average cost for each unique subscribe event that is attributed to your ads. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ subscribe_rate | string | Subscribe Rate (%) | The percentage of unique subscribe events out of all app install events. (The total count is calculated based on the time each ad impression occurred.) |
| ↳ total_subscribe | string | Subscribe (Total No.) | Subscribe (Total No.) (The total count is based on when you were billed.) |
| ↳ cost_per_total_subscribe | string | Cost per Subscribe | Cost per Subscribe (The total count is based on when you were billed.) |
| ↳ value_per_total_subscribe | string | Value per Subscribe | Value per Subscribe (The total count is based on when you were billed.) |
| ↳ total_subscribe_value | string | Total Subscribe Value | Total Subscribe Value (The total count is based on when you were billed.) |

### Chỉ số sự kiện trang (Page event metrics)
 Page event metrics are data about website conversion events. 

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết | Chi tiết hỗ trợ (Detail) |
|---|---|---|---|
| Complete Payment ROAS |  |  |  |
| ↳ complete_payment_roas | string | Complete Payment ROAS | The total return on ad spend (ROAS) from complete payment events that are attributed to your ads. |
| Complete Payment |  |  |  |
| ↳ complete_payment | string | Total Complete Payment | The number of complete payment events. |
| ↳ cost_per_complete_payment | string | Cost per Complete Payment | The average cost of each complete payment event. |
| ↳ complete_payment_rate | string | Complete Payment Rate (%) | The percentage of complete payment events out of all click events. |
| ↳ value_per_complete_payment | string | Value per Complete Payment | The average value returned from complete payment events. |
| ↳ total_complete_payment_rate | string | Total Complete Payment Value | The total value returned from complete payment events. |
| Click Button |  |  |  |
| ↳ value_per_button_click | string | Value per Button Click | The average value returned from button click events. |
| ↳ total_button_click_value | string | Total Button Click Value | The total value returned from button click events. |
| Complete Registration |  |  |  |
| ↳ user_registration | string | Total Complete Registration | The number of user registration events. |
| ↳ cost_per_user_registration | string | Cost per Complete Registration | The average cost of each user registration event. |
| ↳ user_registration_rate | string | Complete Registration Rate (%) | The percentage of user registration events out of all click events. |
| ↳ value_per_user_registration | string | Value per Complete Registration | The average value returned from user registration events. |
| ↳ total_user_registration_value | string | Total Complete Registration Value | The total value returned from user registration events. |
| Add to Cart |  |  |  |
| ↳ web_event_add_to_cart | string | Add to Cart | The number of add to cart events. |
| ↳ cost_per_web_event_add_to_cart | string | Cost per Add to Cart | The average cost of each add to cart event. |
| ↳ web_event_add_to_cart_rate | string | Add to Cart Rate (%) | The percentage of add to cart events out of all click events. |
| ↳ value_per_web_event_add_to_cart | string | Value per Add to Cart | The average value returned from add to cart events. |
| ↳ total_web_event_add_to_cart_value | string | Total Add to Cart Value | The total value returned from add to cart events. |
| Place an Order |  |  |  |
| ↳ on_web_order | string | Total Place an Order | The number of place an order events. |
| ↳ cost_per_on_web_order | string | Cost per Place an Order | The average cost of each place an order event. |
| ↳ on_web_order_rate | string | Place an Order Rate (%) | The percentage of place an order events out of all click events. |
| ↳ value_per_on_web_order | string | Value per Place an Order | The average value returned from place an order events. |
| ↳ total_on_web_order_value | string | Total Place an Order Value | The total value returned from place an order events. |
| Initiate Checkout |  |  |  |
| ↳ initiate_checkout | string | Total Initiate Checkout | The number of initiate checkout events. |
| ↳ cost_per_initiate_checkout | string | Cost per Initiate Checkout | The average cost of each initiate checkout event. |
| ↳ initiate_checkout_rate | string | Initiate Checkout Rate (%) | The percentage of initiate checkout events out of all click events. |
| ↳ value_per_initiate_checkout | string | Value per Initiate Checkout | The average value returned from initiate checkout events. |
| ↳ total_initiate_checkout_value | string | Total Initiate Checkout Value | The total value returned from initiate checkout events. |
| Add Payment Info |  |  |  |
| ↳ add_billing | string | Add Billing | The number of add billing events. |
| ↳ cost_per_add_billing | string | Add Billing Cost | The average cost of each add billing event. |
| ↳ add_billing_rate | string | Add Billing Rate (%) | The percentage of add billing events out of all click events. |
| ↳ value_per_add_billing | string | Value per Add Billing | The average value returned from add billing events. |
| ↳ total_add_billing_value | string | Total Add Billing Value | The total value returned from add billing events. |
| Search |  |  |  |
| ↳ page_event_search | string | Search | The number of search events. |
| ↳ cost_per_page_event_search | string | Search Cost | The average cost of each search event. |
| ↳ page_event_search_rate | string | Search Rate (%) | The percentage of search events out of all click events. |
| ↳ value_per_page_event_search | string | Value per Search | The average value returned from search events. |
| ↳ total_page_event_search_value | string | Total Search Value | The total value returned from search events. |
| Submit Form |  |  |  |
| ↳ form | string | Total Submit Form | The number of form submission events. |
| ↳ cost_per_form | string | Cost per Submit Form | The average cost of each form submission event. |
| ↳ form_rate | string | Submit Form Rate (%) | The percentage of form submission events out of all click events. |
| ↳ value_per_form | string | Value per Submit Form | The average value returned from form submission events. |
| ↳ total_form_value | string | Total Submit Form Value | The total value returned from form submission events. |
| Download |  |  |  |
| ↳ download_start | string | Total Download | The number of download button click events. |
| ↳ cost_per_download_start | string | Cost per Download | The average cost of each download button click events. |
| ↳ download_start_rate | string | Download Rate (%) | The percentage of download button click events out of all click events. |
| ↳ value_per_download_start | string | Value per Download | The average value returned from download button click events. |
| ↳ total_download_start_value | string | Total Download Value | The total value returned from download button click events. |
| Add to Wishlist |  |  |  |
| ↳ on_web_add_to_wishlist | string | Total Add to Wishlist | The number of add to wishlist events that are attributed to your ads. |
| ↳ cost_per_on_web_add_to_wishlist | string | Cost per Add To Wishlist | The average cost of each add to wishlist event. |
| ↳ on_web_add_to_wishlist_per_click | string | Add To Wishlist Rate | The percentage of add to wishlist events out of all click events. |
| ↳ value_per_on_web_add_to_wishlist | string | Value per Add To Wishlist | The average value returned from each add to wishlist event. |
| ↳ total_on_web_add_to_wishlist_value | string | Total Add To Wishlist Value | The total value returned from all add to wishlist events. |
| Subscribe |  |  |  |
| ↳ on_web_subscribe | string | Total Subscribe | The number of subscribe events that are attributed to your ads. |
| ↳ cost_per_on_web_subscribe | string | Subscribe Cost | The average cost of each subscribe event. |
| ↳ on_web_subscribe_per_click | string | Subscribe Rate (%) | The percentage of subscribe events out of all click events. |
| ↳ value_per_on_web_subscribe | string | Value per Subscribe | The average value returned from each subscribe event. |
| ↳ total_on_web_subscribe_value | string | Total Subscribe Value | The total value returned from all subscribe events. |

---

<a id="doc-1751625296192514"></a>
<!-- doc_id: 1751625296192514 -->
<!-- doc_id: 1751625296192514 -->
# Các bộ lọc được hỗ trợ (Supported filters)
> Đường dẫn: Marketing API > Reporting > Guides > Report types > DSA reports > Supported filters
Bạn có thể sử dụng các bộ lọc sau để thu hẹp phạm vi kết quả báo cáo.

Vui lòng đọc kỹ các lưu ý dưới đây trước khi bắt đầu:

* Khi bạn truyền nhiều bộ lọc, các điều kiện lọc sẽ kết hợp theo quan hệ logic `AND` (đồng thời thỏa mãn).
* Khi sử dụng kiểu lọc `IN`, giá trị `filter_value` phải là chuỗi JSON danh sách hợp lệ. Ví dụ: `"[\"ID1\",\"ID2\",\"ID3\"]"`.
* Khi sử dụng kiểu lọc `BETWEEN`, giá trị `filter_value` phải là mảng JSON chứa 2 phần tử chuỗi ngày giờ (bắt đầu và kết thúc). Ví dụ: `"[\"2022-02-24 11:57:51\",\"2022-03-24 11:57:51\"]"`.

> **Note:** 
> - Nếu trường bộ lọc `field_name` được cung cấp và `data_level` không khớp, hệ thống sẽ trả về lỗi: "Invalid value for filter field: xxxx is not supported". Ví dụ: nếu `data_level` là `AUCTION_AD`, bạn chỉ có thể đặt `field_name` thành trường bộ lọc ở cấp quảng cáo (chẳng hạn như `ad_ids`).
> -  Trong báo cáo DSA bất đồng bộ, các trường bộ lọc duy nhất được hỗ trợ là `campaign_ids`, `adgroup_ids`, và `ad_ids`.
> - Dữ liệu báo cáo cho [quảng cáo Product GMV Max](https://ads.tiktok.com/help/article/how-to-create-product-gmv-max-ads-in-seller-center) và quảng cáo LIVE GMV Max tạo từ TikTok Shop sẽ bị loại trừ khỏi các báo cáo cơ bản Đấu thầu đồng bộ, báo cáo đối tượng, báo cáo quảng cáo tương tác và báo cáo DSA. Quảng cáo Mua sắm (Shopping Ads) được tạo qua API hoặc TikTok Ads Manager không bị ảnh hưởng.

| Bộ lọc (Filter Field) | Kiểu lọc hỗ trợ (Supported Filter Types) | Cấp quảng cáo hỗ trợ (Supported Advertising Levels) | Ghi chú chi tiết (Notes) |
|---|---|---|---|
| campaign_ids | IN | Chiến dịch / Nhóm quảng cáo / Quảng cáo | Danh sách ID chiến dịch, bạn có thể truyền tối đa 100 `campaign_id` khi dùng bộ lọc này. Ví dụ giá trị lọc: `"[123,456,789]"`. |
| campaign_type | IN | Campaign/Ad group | Loại chiến dịch (The campaign type). Các giá trị enum hỗ trợ: `REGULAR_CAMPAIGN`, `SKAN_CAMPAIGN`(iOS 14 Dedicated Campaigns). |
| campaign_status | IN | Campaign | Campaign status. Để xem danh sách giá trị enum, xem [Enumeration-Ad Management-Primary Status](../15-appendix/phu-luc-p1.md#doc-1737174886619138). ⏎ **Note**: If not set, this filter field will default to `STATUS_NOT_DELETE` in synchronous DSA reports. |
| adgroup_ids | IN | Nhóm quảng cáo / Quảng cáo | Danh sách ID nhóm quảng cáo, bạn có thể truyền tối đa 100 `adgroup_id` khi dùng bộ lọc này. |
| adgroup_status | IN | Ad group | Ad Group status. Để xem danh sách giá trị enum, xem [Enumeration-Ad Management-Primary Status](../15-appendix/phu-luc-p1.md#doc-1737174886619138). ⏎ **Note**: If not set, this filter field will default to `STATUS_NOT_DELETE` in synchronous DSA reports. |
| ad_ids_v2 | IN | Ad | • Các loại ID bạn có thể lọc bao gồm: • ID của Quảng cáo thủ công. • ID của **Quảng cáo** Upgraded Smart+ (**Nhóm tài sản - Asset Group**). • Bạn cần đặt `data_level` thành `AUCTION_AD` và đưa `ad_id_v2` vào `dimensions`. • Bạn có thể chỉ định tối đa 100 giá trị khi dùng bộ lọc này. • Bạn không thể sử dụng bộ lọc này cùng với chiều dữ liệu `ad_id` hoặc bộ lọc `ad_ids`. |
| ad_ids | IN | Ad | Danh sách ID quảng cáo, bạn có thể truyền tối đa 100 `ad_id` khi dùng bộ lọc này. |
| ad_status | IN | Ad | Ad Status. Để xem danh sách giá trị enum, xem [Enumeration-Ad Management-Primary Status](../15-appendix/phu-luc-p1.md#doc-1737174886619138). ⏎ **Note**: If not set, this filter field will default to `STATUS_NOT_DELETE` in synchronous DSA reports. |
| campaign_label_ids | IN, NOT_IN | Chiến dịch / Nhóm quảng cáo / Quảng cáo | Danh sách ID nhãn chiến dịch. ⏎ Kích thước tối đa: 50. ⏎ Mỗi ID nhãn phải là một chuỗi số 19 chữ số. ⏎ **Lưu ý**: Bộ lọc này chỉ được hỗ trợ trong báo cáo đồng bộ. |
| campaign_label_names | CONTAIN_ANY_OF | Chiến dịch / Nhóm quảng cáo / Quảng cáo | Danh sách tên nhãn chiến dịch. ⏎ Hỗ trợ khớp mờ (fuzzy matching). ⏎ Kích thước tối đa: 10. ⏎ **Lưu ý**: Bộ lọc này chỉ được hỗ trợ trong báo cáo đồng bộ. |
| campaign_label_types | IN, NOT_IN | Chiến dịch / Nhóm quảng cáo / Quảng cáo | Danh sách loại nhãn chiến dịch. ⏎ Các giá trị enum hỗ trợ: • `GENERAL`: Nhãn chung. • `MARKETING_EVENT`: Nhãn sự kiện tiếp thị. ⏎ **Lưu ý**: Bộ lọc này chỉ được hỗ trợ trong báo cáo đồng bộ. |
| promotion_type | IN | Chiến dịch / Nhóm quảng cáo / Quảng cáo | Promotion type (Optimization location). ⏎ Các giá trị enum hỗ trợ: • `APP`: App. • `WEBSITE`: Landing page. • `INSTANT_FORM`: Instant Form. • `LEAD_GEN_CLICK_TO_TT_DIRECT_MESSAGE`: TikTok direct message. • `LEAD_GEN_CLICK_TO_SOCIAL_MEDIA_APP_MESSAGE`: social media app. • `LEAD_GEN_CLICK_TO_CALL`: Phone call. • `OTHERS`: Others. ⏎ This filter can only be used in synchronous reports. |
| dpa_target_audience_type | IN | Chiến dịch / Nhóm quảng cáo / Quảng cáo | The audience type for DPA. Các giá trị enum hỗ trợ: `RETARGETING`, `PROSPECTING`. This filter can only be used in synchronous reports. |
| create_time | BETWEEN | Chiến dịch / Nhóm quảng cáo / Quảng cáo | Khoảng thời gian tạo của chiều ID được yêu cầu (`campaign_id`/`adgroup_id`/`ad_id`). Giá trị cần là một mảng JSON hợp lệ gồm 2 phần tử chuỗi. Phần tử thứ 1 là thời gian bắt đầu, phần tử thứ 2 là thời gian kết thúc. Ví dụ: `"[\"2022-02-24 11:57:51\",\"2022-03-24 11:57:51\"]"`. Bộ lọc này chỉ có thể sử dụng trong báo cáo đồng bộ. ⏎ Khuyến nghị: Nên chọn khoảng thời gian trong vòng 6 tháng khi áp dụng bộ lọc Thời gian tạo, để đảm bảo tốc độ và tỷ lệ thành công của tác vụ không bị ảnh hưởng. |
| create_time | GREATER_THAN | Chiến dịch / Nhóm quảng cáo / Quảng cáo | Thời gian bắt đầu tạo của chiều ID được yêu cầu (`campaign_id`/`adgroup_id`/`ad_id`). Giá trị ở định dạng `YYYY-MM-DD HH:MM:SS` (múi giờ UTC). Ví dụ: `"2022-02-24 11:57:51"` - các chiều dữ liệu được tạo sau thời điểm này sẽ được trả về. Bộ lọc này chỉ có thể sử dụng trong báo cáo đồng bộ. ⏎ Khuyến nghị: Nên chọn khoảng thời gian trong vòng 6 tháng khi áp dụng bộ lọc Thời gian tạo, để đảm bảo tốc độ và tỷ lệ thành công của tác vụ không bị ảnh hưởng. |
| create_time | LOWER_THAN | Chiến dịch / Nhóm quảng cáo / Quảng cáo | Thời gian kết thúc tạo của chiều ID được yêu cầu (`campaign_id`/`adgroup_id`/`ad_id`). Giá trị ở định dạng `YYYY-MM-DD HH:MM:SS` (múi giờ UTC). Ví dụ: `"2022-02-24 11:57:51"` - các chiều dữ liệu được tạo trước thời điểm này sẽ được trả về. Bộ lọc này chỉ có thể sử dụng trong báo cáo đồng bộ. ⏎ Khuyến nghị: Nên chọn khoảng thời gian trong vòng 6 tháng khi áp dụng bộ lọc Thời gian tạo, để đảm bảo tốc độ và tỷ lệ thành công của tác vụ không bị ảnh hưởng. |

---

<a id="doc-1738864971714562"></a>
<!-- doc_id: 1738864971714562 -->
<!-- doc_id: 1738864971714562 -->
# (Không còn hỗ trợ) Báo cáo quảng cáo đặt trước (Reservation ad reports)
> Đường dẫn: Marketing API > Reporting > Guides > Report types > (Deprecated) Reservation ad reports
> **Important:** 
> Để truy xuất dữ liệu báo cáo của quảng cáo TopView, hãy sử dụng [báo cáo cơ bản](bao-cao-p1.md#doc-1738864915188737) hoặc [báo cáo đối tượng](bao-cao-p3.md#doc-1738864928947201) và chỉ định giá trị `RESERVATION_TOP_VIEW` cho [bộ lọc](bao-cao-p3.md#doc-1751443975608321) `buying_type`.

Báo cáo quảng cáo đặt chỗ (Reservation ad reports) là loại báo cáo cho phép bạn lấy dữ liệu chi tiêu và hiệu suất của quảng cáo trong tài khoản quảng cáo **đặt chỗ** của bạn. Hiện tại, để truy vấn báo cáo quảng cáo đặt chỗ, bạn cần đặt `service_type` thành `RESERVATION` và `report_type` duy nhất được hỗ trợ là `BASIC`.

Nếu bạn muốn truy xuất dữ liệu báo cáo của quảng cáo đặt chỗ trong tài khoản quảng cáo **đấu giá** (tài khoản Trình quản lý quảng cáo TikTok), hãy đặt `service_type` thành `AUCTION` và `report_type` thành `BASIC` để chạy [báo cáo cơ bản](bao-cao-p1.md#doc-1738864915188737).

> **Note:** 
> Không hỗ trợ chạy báo cáo quảng cáo đặt chỗ ở chế độ CHUNK (`query_mode`= `CHUNK`). Bạn chỉ có thể chạy báo cáo cơ bản đồng bộ ở chế độ CHUNK.

# Các chiều dữ liệu được hỗ trợ (Supported dimensions)
See [here](bao-cao-p3.md#doc-1751631253780482) for supported dimensions of reservation ads reports.
# Các chỉ số được hỗ trợ (Supported metrics)
See [here](bao-cao-p3.md#doc-1751631257050114) for supported metrics of reservation ads reports.
# Các bộ lọc được hỗ trợ (Supported filters)
See [here](bao-cao-p3.md#doc-1751631259350017) for supported filters of reservation ads reports.

# Hỗ trợ theo thời gian trọn đời (Lifetime supports)
Chỉ số trọn đời cho báo cáo quảng cáo đặt trước không khả dụng trong v1.3. 

# **Các trường hợp sử dụng (Use Cases)**

**1. Query the total consumption of advertiser in a certain period of time.**

**Request Parameters：**

```JSON
// json
{
    "advertiser_id": 66,
    "service_type": "RESERVATION",
    "report_type": "BASIC",
    "data_level": "RESERVATION_ADVERTISER",
    "dimensions": [
        "advertiser_id"
    ],
    "metrics": [
        "spend",
        "impressions"
    ],
    "start_date": "2020-10-25",
    "end_date": "2020-11-23",
    "page": 1,
    "page_size": 100
}
```

**2. Query the daily reporting data of advertiser in a certain period of time.**

**Request Parameters：**
```JSON
// json
{
    "advertiser_id": 66,
    "service_type": "RESERVATION",
    "report_type": "BASIC",
    "data_level": "RESERVATION_ADVERTISER",
    "dimensions": [
        "advertiser_id", "stat_time_day"
    ],
    "metrics": [
        "spend",
        "impressions"
    ],
    "start_date": "2020-10-25",
    "end_date": "2020-11-23",
    "page": 1,
    "page_size": 100
}
```

**3. Query the daily reporting data of some Ad Groups within a certain period of time.**

**Request Parameters：**

```JSON
// json
{
    "advertiser_id": 66,
    "service_type": "RESERVATION",
    "report_type": "BASIC",
    "data_level": "RESERVATION_ADGROUP",
    "dimensions": [
        "adgroup_id",
        "stat_time_day"
    ],
    "metrics": [
        "spend",
        "impressions"
    ],
    "filtering": [
        {
            "field_name": "adgroup_ids",
            "filter_type": "IN",
            "filter_value": "[123, 456]"
        },
        {
            "field_name": "adgroup_status",
            "filter_type": "IN",
            "filter_value": "[\"COMPLETE\", \"DELIVERING\"]"
        }
    ],
    "start_date": "2020-10-25",
    "end_date": "2020-11-23",
    "page": 1,
    "page_size": 100
}
```

---

<a id="doc-1751631253780482"></a>
<!-- doc_id: 1751631253780482 -->
<!-- doc_id: 1751631253780482 -->
# (Không còn hỗ trợ) Các chiều dữ liệu được hỗ trợ
> Đường dẫn: Marketing API > Reporting > Guides > Report types > (Deprecated) Reservation ad reports > (Deprecated) Supported dimensions
A dimension is an attribute to group your data by. Reservation ad reports support the following dimensions. Please note that currently, we don't support all dimensions available on Reservation Ad Platform.

# Các chiều dữ liệu được hỗ trợ (Supported Dimensions)
| Value  | Description  |
| ---- | --- |
| advertiser_id | Group by ID tài khoản quảng cáo TikTok |
| campaign_id | Group by ID chiến dịch quảng cáo |
| adgroup_id | Group by ID nhóm quảng cáo |
| ad_id | Group by ID mẫu quảng cáo <br><br><p><span style="color:darkred"><b>Note</b></span>: The title for this dimension in the title row of the asynchronous Reservation ad report, after translation, will be `Creative ID`, rather than `ID mẫu quảng cáo`.|
| stat_time_day | Nhóm theo ngày (Group by day) |
| stat_time_hour | Nhóm theo giờ (Group by hour) |
| country_code | Group by location code <br> See [Supported metrics for a dimension in reservation ad reports](bao-cao-p3.md#doc-1762405922636802) to learn about the supported metrics for this dimension.  |

# Nhóm chiều dữ liệu (Dimension Grouping)

Các chiều dữ liệu được hỗ trợ được phân loại thành chiều ID, thời gian và vị trí địa lý. 
- ID dimensions: `advertiser_id`, `campaign_id`, `adgroup_id`, and`ad_id`.
- Time dimensions: `stat_time_day` and `stat_time_hour`.
- Location dimension: `country_code`.

Trong mỗi yêu cầu, bạn chỉ có thể có **một** chiều ID và **một** chiều thời gian. For example, `["campaign_id", "stat_time_day"]`. 

Nếu bạn muốn dùng vị trí làm bộ lọc gom nhóm, bạn có thể chỉ định trong trường `dimensions` của yêu cầu:
- `country_code` only, or
- `country_code` + **one** ID dimension, or 
- `country_code` + **one** ID dimension + `stat_time_day`, or
- `country_code` + `stat_time_day`.

---

<a id="doc-1762405922636802"></a>
<!-- doc_id: 1762405922636802 -->
<!-- doc_id: 1762405922636802 -->
# (Không còn hỗ trợ) Chỉ số theo chiều dữ liệu trong báo cáo quảng cáo đặt trước
> Đường dẫn: Marketing API > Reporting > Guides > Report types > (Deprecated) Reservation ad reports > (Deprecated) Supported dimensions > (Deprecated) Supported metrics for a dimension in reservation ad reports
Xem các bảng dưới đây để biết các chỉ số được hỗ trợ khi bạn sử dụng một chiều dữ liệu trong báo cáo quảng cáo đặt chỗ. You can find out the detailed introductions of the metrics in [Reservation ad reports-Supported metrics](bao-cao-p3.md#doc-1751631257050114).

## Supported metrics for `country_code`

| Trường dữ liệu (Field) | Mô tả chi tiết (Description) | Hỗ trợ trong báo cáo đặt trước đồng bộ | Hỗ trợ trong báo cáo đặt trước bất đồng bộ |
|---|---|---|---|
| Chỉ số dữ liệu cơ bản (Basic data metrics) | | | |
#|`impressions`	| Impressions 	| ✅ 	| ✅ 	|
#|`clicks`	| Clicks 	| ✅ 	| ✅ 	|
#|`ctr`	| CTR 	| ✅ 	| ✅ 	|
#|`reach`	| Reach 	| ✅ 	| ❌ 	|
#|`frequency`	| Frequency 	| ✅ 	| ❌ 	|
| Chỉ số phát video (Video play metrics) | | | |
#|`video_play_actions`	| Video Views 	| ✅ 	| ✅ 	|
#|`video_watched_2s`	| 2-Second Video Views 	| ✅ 	| ✅ 	|
#|`video_watched_6s`	| 6-Second Video Views 	| ✅ 	| ✅ 	|
#|`average_video_play`	| Video Average Watch Time Per Video View 	| ✅ 	| ✅ 	|
#|`video_views_p25`	| Video Views at 25% 	| ✅ 	| ✅ 	|
#|`video_views_p50`	| Video Views at 50% 	| ✅ 	| ✅ 	|
#|`video_views_p75`	| Video Views at 75% 	| ✅ 	| ✅ 	|
#|`video_views_p100`	| Video Views at 100% 	| ✅ 	| ✅ 	|
| Chỉ số tương tác (Engagement metrics) | | | |
#|`profile_visits`	| Paid Profile Visit 	| ✅ 	| ✅ 	|
#|`follows`	| Paid Followers 	| ✅ 	| ✅ 	|
#|`clicks_on_music_disc`	| Music Clicks 	| ✅ 	| ✅ 	|

---

<a id="doc-1751631257050114"></a>
<!-- doc_id: 1751631257050114 -->
<!-- doc_id: 1751631257050114 -->
# (Không còn hỗ trợ) Các chỉ số được hỗ trợ
> Đường dẫn: Marketing API > Reporting > Guides > Report types > (Deprecated) Reservation ad reports > (Deprecated) Supported metrics
Bạn có thể sử dụng các chỉ số sau trong báo cáo quảng cáo đặt chỗ. Các chỉ số không phát sinh tiêu dùng sẽ được trả về dạng `-`. Xin lưu ý hiện tại chúng tôi chưa hỗ trợ toàn bộ các chỉ số có trên Nền tảng quảng cáo đặt chỗ.

# Chỉ số thuộc tính (Attribute metrics)
 Các chỉ số thuộc tính (Attribute metrics), chẳng hạn như tên nhóm quảng cáo và loại quảng bá, là các thuộc tính cơ bản của chiến dịch, nhóm quảng cáo hoặc quảng cáo. Chỉ số thuộc tính chỉ hợp lệ khi sử dụng một chiều dữ liệu loại ID. 

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết | Chi tiết hỗ trợ (Detail) |
|---|---|---|---|
| campaign_name | string | Campaign name | Được hỗ trợ ở cấp Chiến dịch, Nhóm quảng cáo và Quảng cáo. |
| campaign_id | string | ID chiến dịch quảng cáo | Supported at the Ad Group and Ad levels only. |
| objective_type | string | Advertising objective | Được hỗ trợ ở cấp Chiến dịch, Nhóm quảng cáo và Quảng cáo. |
| adgroup_name | string | Ad Group name | Supported at the Ad Group and Ad levels only. |
| adgroup_id | string | ID nhóm quảng cáo | Supported at the Ad level only. |
| ad_name | string | Ad name | Supported at the Ad level only. |

# Chỉ số dữ liệu cơ bản (Basic data metrics)
Các chỉ số dữ liệu cơ bản (Basic data metrics) là dữ liệu về chi phí và hiệu suất phân phối quảng cáo của bạn.

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết | Chi tiết hỗ trợ (Detail) |
|---|---|---|---|
| spend | string | Cost | Sum of your total ad spend. ⏎ Not supported at the Ad level. |
| impressions | string | Impressions | Number of times your ads were shown. |
| clicks | string | Clicks (destination) | Number of clicks from your ads to a specified destination. |
| ctr | string | CTR (destination) | Percentage of impressions that resulted in a destination click out of all impressions. |
| reach | string | Reach | Number of unique users who saw your ads at least once. |
| cost_per_1000_reached | string | Cost per 1,000 people reached | Average cost to reach 1,000 unique users. |
| frequency | string | Frequency | The average number of times each user saw your ad over a given time period. |
| currency | string | currency | The currency code, e.g. USD. Note that if you want to use currency as metrics,  then the 'dimensions' field in your request must include adgroup_id/ ad_id/campaign_id/advertiser_id. |

# Chỉ số phát video (Video play metrics)
Video play metrics, such as 2-Second Video Views and Video Views at 50%, are data about video view performance.

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết | Chi tiết hỗ trợ (Detail) |
|---|---|---|---|
| video_play_actions | string | Video views | Number of times your video started to play. For each video impression, plays are counted separately and replays are excluded. |
| video_watched_2s | string | 2-second video views | Number of times your video was played for at least 2 seconds. For each video impression, plays are counted separately and replays are excluded. |
| video_watched_6s | string | 6-second video views | Number of times your video was played for at least 6 seconds. For each video impression, plays are counted separately and replays are excluded. |
| video_views_p25 | string | Video views at 25% | Number of times your video was played at least 25% of its length. For each impression, views are counted separately and replays are excluded. |
| video_views_p50 | string | Video views at 50% | Number of times your video was played at least 50% of its length. For each impression, views are counted separately and replays are excluded. |
| video_views_p75 | string | Video views at 75% | Number of times your video was played at least 75% of its length. For each impression, views are counted separately and replays are excluded. |
| video_views_p100 | string | Video views at 100% | Number of times your video was played 100% of its length. For each impression, views are counted separately and replays are excluded. |
| average_video_play | string | Average play time per video view | Average time your video was played per single video view, including any time spent replaying the video. |
| average_video_play_per_user | string | Average play time per user | Average time your video was played per user, including any time spent replaying the video. |

# Chỉ số tương tác (Engagement metrics)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết | Chi tiết hỗ trợ (Detail) |
|---|---|---|---|
| engagements | string | Clicks (all) | Number of clicks from your ads. This includes clicks that lead to destination as well as those for social and interaction purposes. ⏎ Supported at the Ad group level only. |
| engagement_rate | string | CTR (all) | Percentage of impressions that resulted in a click out of all impressions. ⏎ Supported at the Ad group level only. |
| follows | string | Paid follows | Number of follows to the associated profile during the ad impression. ⏎ Supported at the Ad group level only. |
| likes | string | Paid likes | Number of times your ad was liked during the ad impression. ⏎ Supported at the Ad group level only. |
| comments | string | Paid comments | Number of comments sent on your ad during the ad impression. ⏎ Supported at the Ad group level only. |
| shares | string | Paid shares | Number of shares of your ad during the ad impression. ⏎ Supported at the Ad group level only. |
| profile_visits | string | Paid profile visits | Number of visits to the associated profile during the ad impression. |
| clicks_on_music_disc | string | Sound clicks | Number of clicks on the sound associated with your ad during the ad impression. |
| clicks_on_hashtag_challenge | string | Hashtag clicks | Number of clicks on the hashtag challenge associated with your ad during the ad impression. |
| skip_ad | string | Ad skips | Number of clicks or swipes to skip your ad. |

# Chỉ số định dạng bổ sung (Additional format metrics)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết | Chi tiết hỗ trợ (Detail) |
|---|---|---|---|
| interact_card_show_cnt | string | Interactive Card Impression | Interactive Card Impression |
| interact_card_a_click_cnt | string | Interactive Card Button A Click | Interactive Card Button A Click |
| interact_card_b_click_cnt | string | Interactive Card Button B Click | Interactive Card Button B Click |
| vote_card_show_cnt | string | Voting Card Impression | Voting Card Impression |
| vote_card_a_click_cnt | string | Voting Card Button A Click | Voting Card Button A Click |
| vote_card_b_click_cnt | string | Voting Card Button B Click | Voting Card Button B Click |
| vote_card_convert_click_cnt | string | Voting Card CTA Button Click | Voting Card CTA Button Click |
| redpacket_show_cnt | string | Premium Badge Impression | Premium Badge Impression |
| redpacket_click_cnt | string | Premium Badge Click | Premium Badge Click |
| image_card_show_cnt | string | Display Card Impression | Display Card Impression |
| image_card_click_cnt | string | Display Card Click | Display Card Click |

---

<a id="doc-1751631259350017"></a>
<!-- doc_id: 1751631259350017 -->
<!-- doc_id: 1751631259350017 -->
# (Không còn hỗ trợ) Các bộ lọc được hỗ trợ
> Đường dẫn: Marketing API > Reporting > Guides > Report types > (Deprecated) Reservation ad reports > (Deprecated) Supported filters
Bạn có thể sử dụng các bộ lọc sau để thu hẹp phạm vi kết quả báo cáo.

Vui lòng đọc kỹ các lưu ý dưới đây trước khi bắt đầu:
  - Khi truyền nhiều bộ lọc, các điều kiện lọc có mối quan hệ kết hợp logic `AND`.
  - When using `IN` filter type, `filter_value` needs to be a valid JSON list character string.

> **Note:** 
> Trong báo cáo quảng cáo đặt chỗ bất đồng bộ, các trường bộ lọc duy nhất được hỗ trợ là `campaign_ids`, `adgroup_ids`, và `ad_ids`.

# Các bộ lọc được hỗ trợ (Supported filters)

| Bộ lọc (Filter Field) | Kiểu lọc hỗ trợ (Supported Filter Types) | Cấp dữ liệu hỗ trợ (Supported Data Levels) | Mô tả chi tiết (Description) |
|---|---|---|---|
| campaign_ids | IN | Chiến dịch / Nhóm quảng cáo / Quảng cáo | ID chiến dịch quảng cáo, when using this filter, you can pass up to 100 campaign IDs. filter_value example: `"[123,456,789]"`. |
| campaign_name | MATCH | Campaign | Campaign name. |
| campaign_status | IN | Chiến dịch / Nhóm quảng cáo / Quảng cáo | Campaign status, optional: `NOTDELIVERY`, `DISABLE`, `DELIVERING`, `DELETE`. No filter indicates all states. |
| adgroup_ids | IN | Nhóm quảng cáo / Quảng cáo | ID nhóm quảng cáo, when using this filter, you can pass up to 100 `adgroup_id`. |
| adgroup_name | MATCH | Ad group | Ad Group Name. |
| adgroup_status | IN | Nhóm quảng cáo / Quảng cáo | Ad Group status, optional: `COMPLETE`, `FROZEN`, `DELIVERING`, `CLOSED`, `NOTDELIVERY`, `DELETE`. No filtering indicates all states. |
| ad_ids | IN | Ad | ID mẫu quảng cáo, when using this filter, you can pass up to 100 `ad_id`. |
| ad_status | IN | Ad | Ad status, optional: `DELIVERING`, `NOT_DELIVERY`, `COMPLETE`, `DISABLE`, `DELETE`, `FROZEN`, `CLOSED`. No filtering indicates all states. |
| app | IN | Ad group | Available products: `BUZZ_UP`, `SPICY`, `BABE`, `BABE_PLUS`, `TOP_BUZZ`, `NEWS_REPUBLIC`, `ULIKE`, `BUZZ_VIDEO`, `TIKTOK`. filter_value example: `[\" TIKTOK\, "\" BUZZVIDEO\ "]`. No filter means all products. |
| billing_events | IN | Ad group | Billing method, optional `GD`, `CPT`. |
| platform | IN | Ad group | Delivery platform, optional: `UNLIMITED`, `ANDROID`, `IOS`. |
| locations | IN | Ad group | Countries or regions that you want to target. Để xem danh sách giá trị enum, xem [Appendix - Location code](../15-appendix/phu-luc-p1.md#doc-1737585867307010). |
| ad_placement | IN | Ad group | Ad placement. |
| schedule_start_time | LESS_THAN/GREATER_THAN/RANGE | Ad group | Ad delivery start time(UTC+0). Format: `YYYY-MM-DD`. For example: `2021-01-01`. |
| schedule_end_time | LESS_THAN/GREATER_THAN/RANGE | Ad group | Ad delivery end time(UTC+0). Format: `YYYY-MM-DD`. For example:  `2021-01-01`. |

  
  ## Examples
  
Để lấy các nhóm quảng cáo bắt đầu phân phối trong khoảng từ 2021-04-01 đến 2021-04-10, chúng ta có thể sử dụng bộ lọc sau:
>  {"field_name": "schedule_start_time", "filter_type": "RANGE", "filter_value": "[\"2021-04-01\", \"2021-04-10\"]"}

---

<a id="doc-1775747432712194"></a>
<!-- doc_id: 1775747432712194 -->
<!-- doc_id: 1775747432712194 -->
# Báo cáo Business Center (Business Center reports)
> Đường dẫn: Marketing API > Reporting > Guides > Report types > Business Center reports
Báo cáo Trung tâm Doanh nghiệp (Business Center reports) là loại báo cáo cho phép bạn lấy dữ liệu toàn diện về các tài khoản quảng cáo trong Business Center, bao gồm dữ liệu chi tiêu và hiệu suất, dữ liệu phát video cũng như dữ liệu sự kiện trong ứng dụng (in-app events).

> **Note:** Hiện tại, báo cáo Business Center chỉ hỗ trợ chế độ đồng bộ. To learn about how to create a synchronous Business Center report, refer to [Run a synchronous report](bao-cao-p1.md#doc-1738864778664961). Báo cáo Business Center hỗ trợ truy xuất dữ liệu lên tới 365 ngày bằng các tham số `start_date` và `end_date`.

## Các chiều dữ liệu được hỗ trợ (Supported dimensions)
Xem [tại đây](bao-cao-p3.md#doc-1775747465089026) về các chiều dữ liệu được hỗ trợ của báo cáo Business Center.

## Các chỉ số được hỗ trợ (Supported metrics)
See [here](bao-cao-p4.md#doc-1775747476019266) for supported metrics of Business Center reports.

## Các bộ lọc được hỗ trợ (Supported filters)
See [here](bao-cao-p4.md#doc-1775747484045313) for supported filters of Business Center reports.

## Hỗ trợ theo thời gian trọn đời (Lifetime supports)
Lifetime metrics are not supported for Business Center reports.

## Các trường hợp sử dụng (Use cases)

> **Note:** 
> Báo cáo Business Center hỗ trợ truy xuất dữ liệu lên tới 365 ngày bằng các tham số `start_date` và `end_date`.

**1. Retrieve the reporting data of ad accounts within a specific Business Center, segmented by ad account, during a designated time period.**

**Request Parameters：**

``` xcodeblock
(code json JSON)
{
    "bc_id": "{{bc_id}}",
    "report_type": "BC",
    "dimensions": [
         "advertiser_id"
    ],
    "metrics": [
        "spend",
        "impressions",
        "reach"
    ],
    "start_date": "{{start_date}}",
    "end_date": "{{end_date}}", 
    "page": 1,
    "page_size": 1000
}
(/code)
```

**2. Retrieve the reporting data of ad accounts within a specific Business Center, segmented by region, during a designated time period.**

**Request Parameters：**

``` xcodeblock
(code json JSON)
{
    "bc_id": "{{bc_id}}",
    "report_type": "BC",
    "dimensions": [
        "advertiser_id",
        "country_code"
    ],
    "start_date": "{{start_date}}",
    "end_date": "{{end_date}}", 
    "page": 1,
    "page_size": 1000
}

(/code)
```

**3. Retrieve the daily reporting data of ad accounts within a specific Business Center, during a designated time period.**

**Request Parameters：**

``` xcodeblock
(code json JSON)
{
    "bc_id": "{{bc_id}}",
    "report_type": "BC",
    "dimensions": [
        "stat_time_day"
    ],
    "start_date": "{{start_date}}",
    "end_date": "{{end_date}}", 
    "page": 1,
    "page_size": 1000
}
(/code)
```

---

<a id="doc-1775747465089026"></a>
<!-- doc_id: 1775747465089026 -->
<!-- doc_id: 1775747465089026 -->
# Các chiều dữ liệu được hỗ trợ (Supported dimensions)
> Đường dẫn: Marketing API > Reporting > Guides > Report types > Business Center reports > Supported dimensions
A dimension is an attribute to group your data by. Business Center reports support the following dimensions. 

## Các chiều dữ liệu được hỗ trợ (Supported dimensions)

| Dimension Name | Description |
|---|---|
| advertiser_id | Nhóm theo ID tài khoản quảng cáo TikTok (Advertiser ID). ⏎ All metrics in Business Center reports are supported for this dimension. To find out the complete list of metrics in Business Center reports, refer to [Business Center reports - Supported metrics](bao-cao-p4.md#doc-1775747476019266). |
| stat_time_day | Group by day (date). ⏎ To learn about the supported metrics for this dimension, refer to [Supported metrics for a dimension in Business Center reports - Supported metrics for `stat_time_day`, `stat_time_week` or `stat_time_month`](bao-cao-p3.md#doc-1775747492072449). |
| stat_time_week | Group by week. ⏎ To learn about the supported metrics for this dimension, refer to [Supported metrics for a dimension in Business Center reports - Supported metrics for `stat_time_day`, `stat_time_week` or `stat_time_month`](bao-cao-p3.md#doc-1775747492072449). |
| stat_time_month | Group by month. ⏎ To learn about the supported metrics for this dimension, refer to [Supported metrics for a dimension in Business Center reports - Supported metrics for `stat_time_day`, `stat_time_week` or `stat_time_month`](bao-cao-p3.md#doc-1775747492072449). |
| placement | Nhóm theo vị trí hiển thị (Group by placement). ⏎ To learn about the supported metrics for this dimension, refer to [Supported metrics for a dimension in Business Center reports - Supported metrics for `placement`](bao-cao-p3.md#doc-1775747492072449). |
| country_code | Group by country or region code. ⏎ To learn about the supported metrics for this dimension, refer to [Supported metrics for a dimension in Business Center reports - Supported metrics for `country_code`](bao-cao-p3.md#doc-1775747492072449). |

  
  
 ## Nhóm chiều dữ liệu (Dimension grouping)
Bạn có thể chỉ định trong trường `dimensions` của yêu cầu bất kỳ nhóm gom nào dưới đây:
- `["advertiser_id"]`
- `["stat_time_day"]`
- `["stat_time_week"]`
- `["stat_time_month"]`
- `["advertiser_id", "placement"]`
- `["advertiser_id", "country_code"]`

---

<a id="doc-1775747492072449"></a>
<!-- doc_id: 1775747492072449 -->
<!-- doc_id: 1775747492072449 -->
# Chỉ số theo chiều dữ liệu trong báo cáo Business Center (Supported metrics for a dimension in Business Center reports)
> Đường dẫn: Marketing API > Reporting > Guides > Report types > Business Center reports > Supported dimensions > Supported metrics for a dimension in Business Center reports
Xem các bảng dưới đây để biết các chỉ số được hỗ trợ khi bạn sử dụng một chiều dữ liệu trong báo cáo Business Center. You can find out the detailed introductions of the metrics in [Business Center reports - Supported metrics](bao-cao-p4.md#doc-1775747476019266).

## Supported metrics for `advertiser_id`
Tất cả các chỉ số được liệt kê trong [Báo cáo Business Center - Các chỉ số được hỗ trợ](bao-cao-p4.md#doc-1775747476019266) đều được hỗ trợ cho chiều dữ liệu này.

## Supported metrics for `stat_time_day`, `stat_time_week` or `stat_time_month`

| Field | Description |
|---|---|
| Basic data metrics |  |
| ↳ `spend` | Cost |
| ↳ `billed_cost` | Net cost |
| ↳ `cash_spend` | Cost (Cash) |
| ↳ `voucher_spend` | Cost (Voucher) |
| ↳ `cashback_coupon_spend` | Cost (Cashback) |
| ↳ `tax_spend` | Cost (Tax) |
| ↳ `cpc` | CPC |
| ↳ `cpm` | CPM |
| ↳ `impressions` | Impression |
| ↳ `clicks` | Clicks |
| ↳ `ctr` | CTR (Destination) |
| ↳ `conversion` | Conversions |
| ↳ `cost_per_conversion` | CPA |
| ↳ `conversion_rate` | CVR (Conversion rate) |
| ↳ `reach` | Reach |
| ↳ `real_time_conversion` | Real-time conversions |
| ↳ `real_time_cost_per_conversion` | Real-time CPA |
| ↳ `real_time_conversion_rate` | Real-time CVR |
| ↳ `account_type` | Account type |
| ↳ `skan_conversion` | Conversions (SKAN) |
| ↳ `skan_cost_per_conversion` | CPA (SKAN) |
| ↳ `skan_conversion_rate` | CVR (SKAN) |
| In-app events metrics |  |
| ↳ `registration` | Unique registration |
| ↳ `cost_per_registration` | Cost per unique registration |
| ↳ `registration_rate` | Unique registration rate |
| ↳ `purchase` | Purchase |
| ↳ `cost_per_purchase` | Cost per purchase |
| ↳ `purchase_rate` | Unique purchase rate |
| ↳ `value_per_total_purchase` | Value per purchase |
| ↳ `total_purchase_value` | Total purchase value |
| ↳ `app_install` | App install |
| ↳ `cost_per_app_install` | Cost per app install |
| ↳ `app_install_rate` | App install rate |
| ↳ `real_time_app_install` | Real-time app install |
| ↳ `real_time_app_install_cost` | Cost per real-time app install |
| ↳ `real_time_app_install_rate` | Real-time app install rate |
| In-app events (SKAN) metrics |  |
| ↳ `skan_app_install` | App install (SKAN) |
| ↳ `skan_cost_per_app_install` | Cost per app install (SKAN) |
| ↳ `skan_registration` | Unique registration (SKAN) |
| ↳ `skan_cost_per_registration` | Cost per unique registration (SKAN) |
| ↳ `skan_registration_rate` | Unique registration rate (SKAN) |
| ↳ `skan_total_registration` | Total registration (SKAN) |
| ↳ `skan_cost_per_total_registration` | Cost per registration (SKAN) |
| ↳ `skan_purchase` | Unique purchase (SKAN) |
| ↳ `skan_cost_per_purchase` | Cost per unique purchase (SKAN) |
| ↳ `skan_purchase_rate` | Unique purchase rate (SKAN) |
| ↳ `skan_total_purchase` | Total purchase (SKAN) |
| ↳ `skan_cost_per_total_purchase` | Cost per purchase (SKAN) |
| ↳ `skan_total_purchase_value` | Total purchase value (SKAN) |
| Video plays metrics |  |
| ↳ `video_watched_2s` | 2-second video views |
| ↳ `video_watched_6s` | 6-second video views |
| ↳ `video_views_p100` | Video views at 100% |
| ↳ `video_views_p75` | Video views at 75% |
| ↳ `video_views_p50` | Video views at 50% |
| ↳ `video_views_p25` | Video views at 25% |

## Supported metrics for `placement`

| Field | Description |
|---|---|
| Attribute metrics |  |
| ↳ `advertiser_name` | Ad Account name |
| Basic data metrics |  |
| ↳ `currency` | Currency |
| ↳ `spend` | Cost |
| ↳ `cpc` | CPC |
| ↳ `cpm` | CPM |
| ↳ `impressions` | Impression |
| ↳ `clicks` | Clicks |
| ↳ `ctr` | CTR (Destination) |
| ↳ `conversion` | Conversions |
| ↳ `cost_per_conversion` | CPA |
| ↳ `conversion_rate` | CVR (Conversion rate) |
| ↳ `real_time_conversion` | Real-time conversions |
| ↳ `real_time_cost_per_conversion` | Real-time CPA |
| ↳ `real_time_conversion_rate` | Real-time CVR |

## Supported metrics for `country_code`

| Field | Description |
|---|---|
| Attribute metrics |  |
| ↳ `advertiser_name` | Ad Account name |
| Basic data metrics |  |
| ↳ `currency` | Currency |
| ↳ `spend` | Cost |
| ↳ `cash_spend` | Cost (Cash) |
| ↳ `voucher_spend` | Cost (Voucher) |
| ↳ `cashback_coupon_spend` | Cost (Cashback) |
| ↳ `cpc` | CPC |
| ↳ `cpm` | CPM |
| ↳ `impressions` | Impression |
| ↳ `clicks` | Clicks |
| ↳ `ctr` | CTR (Destination) |
| ↳ `conversion` | Conversions |
| ↳ `cost_per_conversion` | CPA |
| ↳ `conversion_rate` | CVR (Conversion rate) |
| ↳ `real_time_conversion` | Real-time conversions |
| ↳ `real_time_cost_per_conversion` | Real-time CPA |
| ↳ `real_time_conversion_rate` | Real-time CVR |
---

## Hướng dẫn thực hành Data Retrieval (Python & cURL)

Dưới đây là mã nguồn mẫu minh họa quy trình gọi API thực tế cho phân hệ **Hướng dẫn Báo cáo (Reporting) — phần 3/4**:

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

