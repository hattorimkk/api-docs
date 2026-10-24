# Smart+ nâng cấp (Upgraded Smart+) — phần 4/7

> Phân hệ: apiref:Upgraded Smart+.
> Tài liệu biên dịch kỹ thuật chi tiết theo chuẩn TikTok Business API v1.3.

---

## Mục lục điều hướng
- [1. Cập nhật nhóm quảng cáo Smart+ nâng cấp (#doc-1843314894279682)](#doc-1843314894279682)
- [2. Cập nhật trạng thái hoạt động của nhóm quảng cáo Smart+ nâng cấp (#doc-1843314908153858)](#doc-1843314908153858)
- [3. Cập nhật ngân sách của nhóm quảng cáo Smart+ nâng cấp (#doc-1843314914438466)](#doc-1843314914438466)
- [4. Quảng cáo (#doc-1843310530260097)](#doc-1843310530260097)
- [5. Lấy danh sách quảng cáo Smart+ nâng cấp (#doc-1843317378982914)](#doc-1843317378982914)

---

<a id="doc-1843314894279682"></a>
<!-- doc_id: 1843314894279682 -->
<!-- doc_id: 1843314894279682 -->
# Cập nhật nhóm quảng cáo Smart+ nâng cấp (Update an Upgraded Smart+ Ad Group)
> Đường dẫn: API Reference > Smart+ nâng cấp > Nhóm quảng cáo > Cập nhật nhóm quảng cáo Smart+ nâng cấp
Sử dụng endpoint này để cập nhật một nhóm quảng cáo Smart+ nâng cấp.

Endpoint này hỗ trợ cập nhật tăng dần (incremental updates).

## Yêu cầu gọi API (Request)
**Endpoint** https://business-api.tiktok.com/open_api/v1.3/smart_plus/adgroup/update/

**Method** POST

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type  ****(Bắt buộc)**** | string | Định dạng dữ liệu yêu cầu. ⏎ Allowed value: `application/json`. |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id  ****(Bắt buộc)**** | string | ID tài khoản quảng cáo TikTok. |
| adgroup_id  ****(Bắt buộc)**** | string | ID nhóm quảng cáo. ⏎ Để lấy ID nhóm quảng cáo, sử dụng [/smart_plus/adgroup/get/](62-upgraded-smartplus-p2.md#doc-1843314879617026). |
| adgroup_name | string | Ad group name. ⏎ Giới hạn độ dài: 512 characters. Emoji is not supported. |
| bid_price | float | Valid when the following conditions are met: • `optimization_goal` is `CLICK`. • `bid_type` is `BID_TYPE_CUSTOM`. ⏎ Giá thầu mục tiêu cho mỗi lượt nhấp. Hệ thống sẽ nhắm tới việc đạt được nhiều kết quả nhất trong khi vẫn duy trì chi phí trung bình trên mỗi kết quả xấp xỉ hoặc thấp hơn mức chỉ định. ⏎ `bid_price` cần phải thấp hơn ngân sách. Xem [Đấu thầu - Giới hạn giá thầu](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1745292444424193) để tìm hiểu thêm về cơ chế xác thực giá thầu. ⏎ **Quan trọng**: Khi chiến dịch của bạn có nhiều nhóm quảng cáo, việc cập nhật `bid_price` cho một nhóm quảng cáo sẽ tự động cập nhật `bid_price` cho tất cả các nhóm quảng cáo khác thuộc cùng chiến dịch bằng giá trị mới. ⏎ **Lưu ý**: Khi tính năng Tối ưu hóa ngân sách chiến dịch (CBO) được bật (`budget_optimize_on` là `true`) ở cấp chiến dịch, cài đặt này (nếu được chỉ định) phải giống nhau trên tất cả các nhóm quảng cáo trong cùng chiến dịch. |
| conversion_bid_price | float | Valid when the following conditions are met: • `optimization_goal` is `CONVERT`, `TRAFFIC_LANDING_PAGE_VIEW`, `INSTALL`, or `IN_APP_EVENT`. • `bid_type` is `BID_TYPE_CUSTOM`. ⏎ Giá thầu mục tiêu cho mỗi lượt chuyển đổi hoặc chi phí cho mỗi lượt xem trang đích. Hệ thống sẽ nhắm tới việc đạt được nhiều kết quả nhất trong khi vẫn duy trì chi phí trung bình trên mỗi kết quả xấp xỉ hoặc thấp hơn mức chỉ định. ⏎ `conversion_bid_price` cần phải thấp hơn ngân sách. Xem [Đấu thầu - Giới hạn giá thầu](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1745292444424193) để tìm hiểu thêm về cơ chế xác thực giá thầu. ⏎ **Quan trọng**: Khi chiến dịch của bạn có nhiều nhóm quảng cáo, việc cập nhật `conversion_bid_price` cho một nhóm quảng cáo sẽ tự động cập nhật `bid_price` cho tất cả các nhóm quảng cáo khác thuộc cùng chiến dịch bằng giá trị mới. ⏎ **Lưu ý**: Khi CBO được bật (`budget_optimize_on` là `true`) ở cấp chiến dịch, cài đặt này (nếu được chỉ định) phải giống nhau trên tất cả các nhóm quảng cáo trong cùng chiến dịch. |
| roas_bid | float | Valid when `deep_bid_type` is `VO_MIN_ROAS`. ⏎ ROAS mục tiêu cho tính năng Tối ưu hóa theo giá trị (Value-Based Optimization). ⏎ Value range: 0.01-1,000. ⏎ **Quan trọng**: Khi chiến dịch của bạn có nhiều nhóm quảng cáo, việc cập nhật `roas_bid` cho một nhóm quảng cáo sẽ tự động cập nhật `bid_price` cho tất cả các nhóm quảng cáo khác thuộc cùng chiến dịch bằng giá trị mới. ⏎ **Note**: When CBO is enabled (`budget_optimize_on` is `true`) at the campaign level, this setting, if specified, must be the same across all ad groups within the same campaign. |
| value_rule_set_id | string | ID của bộ quy tắc giá trị (value rule set) cần liên kết với nhóm quảng cáo. ⏎ Quy tắc giá trị cho phép bạn điều chỉnh giá thầu. Ví dụ: đặt giá thầu cao hơn cho người dùng iOS. Bạn có thể nhận được nhiều kết quả hơn, nhưng chi phí chung trên mỗi kết quả có thể tăng. ⏎ • Để truy xuất các bộ quy tắc hiện có trong tài khoản quảng cáo, sử dụng [/smart_plus/value_rule_set/get/](70-tools-p3.md#doc-1879581236824514). • Để tạo bộ quy tắc mới trong tài khoản quảng cáo, sử dụng [/smart_plus/value_rule_set/create_or_update/](70-tools-p3.md#doc-1879581240885250). ⏎ **Note**:  • Bằng việc sử dụng trường này, bạn xác nhận hiểu rằng các quy tắc giá trị có thể làm tăng giá thầu cho các đối tượng được chọn, điều này có thể làm tăng chi phí trên mỗi kết quả (như CPA) vượt mức mục tiêu của bạn. • Quy tắc giá trị không tương thích với danh mục quảng cáo đặc biệt. Do đó, bạn không thể sử dụng trường này khi `special_industries` được thiết lập giá trị không rỗng ở cấp chiến dịch. |
| automated_keywords_enabled | boolean | Chỉ hợp lệ khi ở cấp chiến dịch `is_search_campaign` là `true`. ⏎ Có bật từ khóa tự động và cho phép hệ thống tìm kiếm các từ khóa liên quan để mở rộng phạm vi tiếp cận và cải thiện kết quả hay không. ⏎ Các giá trị được hỗ trợ: `true`, `false`. |
| search_keywords | object[] | Chỉ hợp lệ khi ở cấp chiến dịch `is_search_campaign` là `true`. ⏎ A list of search keywords, that is, words or phrases that are used to match your ads with the terms people are searching for. ⏎ Kích thước tối đa: 1,000. ⏎ To confirm Liệu an Upgraded Smart+ Campaign is a Search Ads Campaign, call [/smart_plus/campaign/get/](62-upgraded-smartplus-p1.md#doc-1843312818332930) and check the `is_search_campaign` returned for the campaign. ⏎ To learn more about how to create Search Ads Campaigns, see [Create Upgraded Smart+ Search Ads Campaigns](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1873144295333889). ⏎ **Note**:  • Once the search keywords or the targeted locations are updated, the keywords will go into the review process again. |
| ↳ keyword | string | When `search_keywords` is specified, you need to provide at least one `keyword` and the corresponding `match_type`. ⏎ The search keyword. ⏎ Giới hạn độ dài: 80 characters. ⏎ The name needs to exclude emojis and the following special characters: `!` `#` `$` `%` `&` `(` `)` `*` `-` `/` `:` `;` `` `?` `@` `\` `^` `_` `¥` `……`. Otherwise, an error will occur. ⏎ To obtain the review result for search keywords, call [/smart_plus/adgroup/get/](62-upgraded-smartplus-p2.md#doc-1843314879617026) and check the `audit_status` within the `search_keywords` object array. ⏎ **Important**: Search keywords must comply with TikTok's [Advertising Terms](https://ads.tiktok.com/help/article/advertising-on-tiktok-first-things-to-note) and Community Guidelines. • If all of your keywords are found to be non-compliant, your campaign will not be delivered. • If part of your search keywords are rejected, you need to remove the violative keywords or replace them with a suitable alternative by using [/smart_plus/adgroup/update/](62-upgraded-smartplus-p4.md#doc-1843314894279682). Your campaign will continue with the approved keywords. |
| ↳ match_type | string | When `search_keywords` is specified, you need to provide at least one `keyword` and the corresponding `match_type`. ⏎ The match type for the search keyword. ⏎ Các giá trị enum hỗ trợ: • `PRECISE_WORD`: exact match. Ads only show when a search includes the exact phrase or close variations, with additional words allowed before or after. • `PHRASE_WORD`: phrase match. Ads only show when a search exactly matches your keyword or a very close variation. • `BROAD_WORD`: broad match. Ads are shown for a wide range of relevant searches to offer the widest reach. |
| comment_disabled | boolean | Có thực hiện allow comments on your campaigns on TikTok. ⏎ Các giá trị được hỗ trợ: `true`, `false`. |
| share_disabled | boolean | Có vô hiệu hóa chia sẻ chiến dịch lên các nền tảng của bên thứ ba hay không. ⏎ Các giá trị được hỗ trợ: `true`, `false`. |
| schedule_type | string | Schedule type. ⏎ Các giá trị enum hỗ trợ: • `SCHEDULE_FROM_NOW`: To run the ad group continuously after the scheduled start time. • `SCHEDULE_START_END`: To run the ad group between the scheduled start time and end time. ⏎ You can only set `schedule_type` to `SCHEDULE_START_END` in any of the following scenarios: • At the campaign level, `budget_mode` is `BUDGET_MODE_TOTAL` • At the ad group level, `budget_mode` is `BUDGET_MODE_TOTAL` |
| schedule_start_time | string | Schedule start time, in the format of `YYYY-MM-DD HH:MM:SS` (UTC+0). ⏎ The start time can be up to 12 hours earlier than the current time, but cannot be later than `2028-01-01 00:00:00`. |
| schedule_end_time | string | Hợp lệ khi `schedule_type` là `SCHEDULE_START_END`. ⏎ Schedule end time, in the format of `YYYY-MM-DD HH:MM:SS` (UTC+0). ⏎ The end time cannot be later than `2038-01-01 00:00:00`. |
| dayparting | string | Ad delivery arrangement, in the format of a string that consists of 48 x 7 characters. Each character is mapped to a 30-minute timeframe from Monday to Sunday. Each character can be set to either 0 or 1. 1 represents delivery in the 30-minute timeframe, and 0 stands for non-delivery in the 30-minute timeframe. The first character is mapped to 0:01-0:30 of Monday; The second character is mapped to 0:31-1:00 of Monday, and the last character represents 23:31-0:00 Sunday. ⏎ **Note**: An all-0 value, an all-1 value and when this field is not specified, are considered full-time delivery. |
| is_hfss | boolean | Chỉ hợp lệ khi `targeting_optimization_mode` là `MANUAL`. ⏎ Liệu promoted content is HFSS (High Fat, Salt, Sugar) Product/Brand. ⏎ If your ad is promoting or prominently featuring a product/brand classed as high in fat, salt or sugar, set this field to `true`. ⏎ In regulated regions, HFSS ads must only be targeted to users aged 18 or over. ⏎ You can set this field to `true`when your targeting locations include locations in the UK, Australia, New Zealand, and the European Union. ⏎ Các giá trị được hỗ trợ: `true`, `false`. |
| is_lhf_compliance **(Điều kiện)** | boolean | When the targeting locations include locations in the UK and `is_hfss` is `true`, this field is required and must be set to `true`. ⏎ Liệu promoted content complies with LHF (Less Healthy Foods) regulations. ⏎ By setting `is_lhf_compliance` to `true`, you confirm that any food or drink products you advertise on TikTok in the UK comply with the [2024 Less Healthy Foods Regulations](https://www.legislation.gov.uk/uksi/2024/1266/made) and all other applicable laws. ⏎ Các giá trị được hỗ trợ: `true`, `false`. |
| targeting_optimization_mode | string | Chế độ tối ưu hóa nhắm mục tiêu đối tượng. • `AUTOMATIC`: Automatic targeting. You can use automatic targeting to leverage real-time data and machine learning to target audiences most likely to engage with your ads. • When `targeting_optimization_mode` is `AUTOMATIC` and `suggestion_audience_enabled` is `false`, you can specify the following optional audience control settings: • `location_ids` • `zipcode_ids` • `spc_audience_age` • `languages` • `operating_systems` • `excluded_audience_ids` • When `targeting_optimization_mode` is `AUTOMATIC` and `suggestion_audience_enabled` is `true`, you can specify additional audience targeting settings as suggestions that guide automatic targeting. To learn more about the available settings, see the description of the parameter `suggestion_audience_enabled`. • `MANUAL`: Nhắm mục tiêu tùy chỉnh. Bạn có thể sử dụng các cài đặt nhắm mục tiêu tùy chỉnh để kiểm soát chính xác người nhìn thấy quảng cáo. Điều này có thể hạn chế phân phối và ảnh hưởng đến hiệu suất chiến dịch. • When `targeting_optimization_mode` is `MANUAL`, you can specify the following audience settings: • `location_ids` • `zipcode_ids` • `age_groups` • `gender` • `languages` • `audience_ids` • `excluded_audience_ids` • `interest_category_ids` • `interest_keyword_ids` • `purchase_intention_keyword_ids` • `actions` • `smart_interest_behavior_enabled` • `smart_audience_enabled` • `spending_power` • `household_income` • `operating_systems` • `min_android_version` • `min_ios_version` • `device_model_ids` • `network_types` • `carrier_ids` • `isp_ids` • `device_price_ranges` • `saved_audience_id` ⏎ **Note**: If you specify targeting settings that don’t align with your targeting optimization mode settings (`targeting_optimization_mode` and `suggestion_audience_enabled`), those settings will be ignored, and no errors will occur. |
| suggestion_audience_enabled | boolean | Chỉ hợp lệ khi `targeting_optimization_mode` là `AUTOMATIC`. ⏎ Có bật tính năng gợi ý đối tượng (audience suggestions) hay không. ⏎ Gợi ý đối tượng định hướng nhắm mục tiêu tự động bằng cách chỉ định các cài đặt đối tượng bổ sung. Các cài đặt này chỉ đóng vai trò gợi ý, việc phân phối đến các đối tượng đó không được đảm bảo. ⏎ Các giá trị được hỗ trợ: `true`, `false`. ⏎ When `suggestion_audience_enabled` is `true`, you can specify the following additional audience targeting settings: • `age_groups` • `gender` • `audience_ids` • `interest_category_ids` • `interest_keyword_ids` • `purchase_intention_keyword_ids` • `actions` ⏎ **Note**: ⏎ • If you specify targeting settings that don’t align with your targeting optimization mode settings (`targeting_optimization_mode` and `suggestion_audience_enabled`), those settings will be ignored, and no errors will occur. • You cannot set this field to `true` if Realtime API (RTA) is enabled at the campaign level. |
| targeting_spec | object | Cài đặt nhắm mục tiêu đối tượng. |
| ↳ location_ids | string[] | • When `catalog_type` is `TRAVEL_ENTERTAINMENT` at the campaign level, you need to set `location_ids` or `zipcode_ids` or both. • When you create other types of Smart+ Campaigns, `location_ids` is required. ⏎ IDs of the locations that you want to target. ⏎ To get the available locations and corresponding IDs based on your placement and objective, use the [/tool/targeting/search/](70-tools-p1.md#doc-1761236883355649) or [/tool/region/](70-tools-p1.md#doc-1737189539571713) endpoint. ⏎ To get the list of location IDs, see **Location IDs**. ⏎ **Note**: If you add the US as your target location, then you can not remove the US after campaign creation. |
| ↳ zipcode_ids | string[] | • When `catalog_type` is `TRAVEL_ENTERTAINMENT` at the campaign level, you need to set `location_ids` or `zipcode_ids` or both. •  When you create other types of Smart+ Campaigns, `zipcode_ids` is not supported. ⏎ Zip code IDs or postal code IDs that you want to use to target locations. ⏎ Kích thước tối đa: 3,000. If you provide both `location_ids` and `zipcode_ids`, the combined total of location IDs, zip code IDs, and postal code IDs cannot exceed 3,000 per ad group. ⏎ You can get the available zip code IDs or postal code IDs based on your placement, objective and keyword via `geo_id` (when `geo_type` = `ZIP_CODE`) returned from the [/tool/targeting/search/](70-tools-p1.md#doc-1761236883355649) endpoint. ⏎ **Note**: ⏎ • Zip code targeting is currently only supported for the US and postal code targeting is currently only supported for Canada, Brazil, Indonesia, Thailand, and Vietnam. • Targeting postal code areas in Brazil, Indonesia, Thailand, and Vietnam is currently an allowlist-only feature. If you would like to access it, please contact your TikTok representative. • You cannot use zip code targeting or postal code targeting in campaigns that have enabled special ad categories (`special_industries`). • You cannot use zip code targeting or postal code targeting in campaigns with the `objective_type` as `RF_REACH`. • Overlapping targeted locations are not supported. For instance, you cannot target the US and the state of California at the same time. • If you target locations in the US via `location_ids` or `zipcode_ids` during ad group creation, you can subsequently update those IDs to other US locations but you cannot remove all US locations to target only non-US countries. • To get information about the zip code IDs or postal code IDs, you can only use [/tool/targeting/info/](70-tools-p1.md#doc-1761237001980929). |
| ↳ spc_audience_age | string | Nhóm tuổi mà nhóm quảng cáo nhắm mục tiêu. ⏎ Các giá trị enum hỗ trợ: • `ALL`: all age groups. • `OVER_EIGHTEEN`: 18+. • `OVER_TWENTY_FIVE`: 25+. ⏎ **Note**:  • Targeting all age groups (`ALL`) is currently an allowlist-only feature. If you would like to access it, please contact your TikTok representative. • You can only use the value `ALL` when at the campaign level `smart_plus_adgroup_mode` is `MULTIPLE`. To check the `smart_plus_adgroup_mode` of a campaign, use [/smart_plus/campaign/get/](62-upgraded-smartplus-p1.md#doc-1843312818332930). |
| ↳ languages | string[] | Mã các ngôn ngữ bạn muốn nhắm mục tiêu. ⏎ For the list of language codes supported, see [Enumeration - Language Code](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ operating_systems | string[] | Hệ điều hành thiết bị bạn muốn nhắm mục tiêu. ⏎ Các giá trị enum hỗ trợ: `ANDROID`, `IOS`. ⏎ Only one value is allowed. • When `promotion_type` is `APP_ANDROID`, this field will be ignored and default to `["ANDROID"]`. • When `promotion_type` is `APP_IOS`, this field will be ignored and default to `["IOS"]`. |
| ↳ excluded_audience_ids | string[] | Danh sách các ID đối tượng cần loại trừ. ⏎ To get a list of audience IDs, use [/dmp/custom_audience/list/](09-audience.md#doc-1739940506015746). ⏎ **Note**: When at the campaign level `rta_id` is specified, this field is not supported. |
| ↳ age_groups | string[] | Các nhóm tuổi bạn muốn nhắm mục tiêu. ⏎ Các giá trị enum hỗ trợ: • `AGE_13_17`: 13-17. • `AGE_18_24`: 18-24. • `AGE_25_34`: 25-34. • `AGE_35_44`: 35-44. • `AGE_45_54`: 45-54. • `AGE_55_100`: 55+ ⏎ **Note**: You can only use the value `AGE_13_17` in the following scenario: • At the campaign level `objective_type` is `APP_PROMOTION` and `app_promotion_type` is `APP_INSTALL` or `APP_RETARGETING`. |
| ↳ gender | string | Gender that you want to target. ⏎ Các giá trị enum hỗ trợ: `GENDER_FEMALE`,`GENDER_MALE`,`GENDER_UNLIMITED`. |
| ↳ audience_ids | string[] | Danh sách các ID đối tượng. ⏎ To get audience IDs, use [/dmp/custom_audience/list/](09-audience.md#doc-1739940506015746). ⏎ **Note**: When at the campaign level `rta_id` is specified, this field is not supported. |
| ↳ shopping_ads_retargeting_type | string | Chỉ hợp lệ khi the following conditions are all met: • At the campaign level: • `objective_type` is `WEB_CONVERSION` • `sales_destination` is `WEB_AND_APP`, `WEBSITE`, or `APP` • `catalog_type` is `ECOMMERCE` • At the ad group level: `targeting_optimization_mode` is `MANUAL`. ⏎ The retargeting type. ⏎ Các giá trị enum hỗ trợ: • `LAB1`: Retargeting audiences who viewed products or added products to cart but didn't purchase products. • `LAB2`: Retargeting audiences who added products to cart but didn't purchase products. • `LAB3`: Retargeting audiences using custom combination. • `OFF`: No retargeting. |
| ↳ shopping_ads_retargeting_actions_days**(Điều kiện)** | number | Bắt buộc khi `shopping_ads_retargeting_type` is `LAB1` or `LAB2`. ⏎ The valid time range for the specified audience action. Audiences who have completed the specified action within the time range will be retargeted. ⏎ Value range: 1, 2, 3, 7, 14, 30, 60, 90, 180. |
| ↳ included_custom_actions**(Điều kiện)** | object[] | When `shopping_ads_retargeting_type` is `LAB3`, you need to specify either `included_custom_actions` or `excluded_custom_actions`. ⏎ Details of the catalog audience to include. ⏎ Catalog audience is based on people's interactions with specific products and often drives better performance than custom audience. |
| ↳↳ code | string | The custom action used to filter the audiences to be retargeted. ⏎ Các giá trị enum hỗ trợ: • `VIEW_PRODUCT`: The audience viewed the product. • `ADD_TO_CART`: The audience added the product to the cart. • `PURCHASE`: The audience purchased the product. |
| ↳↳ days | integer | The time range used to filter the audiences that completed the specified action. ⏎ Value range: 1-180. |
| ↳ excluded_custom_actions**(Điều kiện)** | object[] | When `shopping_ads_retargeting_type` is `LAB3`, you need to specify either `included_custom_actions` or `excluded_custom_actions`. ⏎ Details of the catalog audience to exclude. ⏎ Improve ad performance by excluding products that people have already interacted with, ensuring they only see relevant ads from your brand. |
| ↳↳ code | string | The custom action used to filter out the audiences. ⏎ Các giá trị enum hỗ trợ: • `VIEW_PRODUCT`: The audience viewed the product. • `ADD_TO_CART`: The audience added the product to the cart. • `PURCHASE`: The audience purchased the product. |
| ↳↳ days | integer | The time range used to filter out the audiences that completed the specified action. ⏎ Value range: 1-180. |
| ↳ shopping_ads_retargeting_custom_audience_relation | string | Chỉ hợp lệ khi the following conditions are both met: • `shopping_ads_retargeting_type` is set to `LAB1`, `LAB2`, or `LAB3`. • `audience_ids` is specified. ⏎ The logical relation between the retargeting audience specified by `shopping_ads_retargeting_type` and the custom audience specified by `audience_ids`. ⏎ Các giá trị enum hỗ trợ: • `OR`: To combine the retargeting audience and the custom audience to create the targeted audience. The ad group will target anyone in catalog or custom audiences. • `AND`: To intersect between the retargeting audience and the custom audience to create the targeted audience. The ad group will target individuals who belong to both the retargeting audience and the custom audience. ⏎ If this field is not set, the targeted audience will consist of individuals who belong to both the retargeting audience and the custom audience. ⏎ **Note**: Once set, this field cannot be updated to a null value. |
| ↳ interest_category_ids | string[] | IDs of general interest keywords that you want to use to target audiences. ⏎ • To search for or list general interest category IDs, use [/targeting/search/](70-tools-p1.md#doc-1796638342793218) (recommended) or [/tool/interest_category/](70-tools-p1.md#doc-1737174348712961). • To get recommended interest category IDs based on your industry, use [/tool/targeting_category/recommend/](70-tools-p1.md#doc-1736275204260866). |
| ↳ interest_keyword_ids | string[] | IDs of additional interest categories that you want to use to target audience. ⏎ To search for additional interest categories, use [/targeting/search/](70-tools-p1.md#doc-1796638342793218) (recommended) or [/tool/interest_keyword/recommend/](70-tools-p1.md#doc-1763590884474882). |
| ↳ purchase_intention_keyword_ids | string[] | IDs of purchase intention categories that you want to use to target audiences with an interest in purchases related to a content category. ⏎ To search for or list purchase intention category IDs, use [/targeting/search/](70-tools-p1.md#doc-1796638342793218). ⏎ **Note**: The placement setting should include TikTok (`PLACEMENT_TIKTOK`) or Pangle (`PLACEMENT_PANGLE`). |
| ↳ actions | object[] | A list of targeting behavioral category objects. |
| ↳↳ action_scene | string | The type of user behavior that you want to target. ⏎ Các giá trị enum hỗ trợ: • `VIDEO_RELATED`: Video interactions. • `CREATOR_RELATED`: Creator interactions. • `HASHTAG_RELATED`: Hashtag interactions. |
| ↳↳ action_period | number | The time period to include behaviors from. ⏎ Các giá trị enum hỗ trợ: `0`, `7`, `15`. ⏎ If `action_scene` is `CREATOR_RELATED` or `HASHTAG_RELATED`, `0` will be used regardless of the value you specify. `0` means that there is no definite timeframe to select actions from. ⏎ **Note**: Currently, when creating an ad group with video interactions targeting (`action_scene`= `VIDEO_RELATED`) via **TikTok Ads Manager**, you cannot select the time period (`action_period`), and 15 days (`15`) will be used by default. However, when creating ad groups via **API**, `0`, `7`, or `15` can still be passed. |
| ↳↳ video_user_actions | string[] | The specific user interactions that you want to target for the user behavior type. • If `action_scene` is `VIDEO_RELATED`, the allowed values are: `WATCHED_TO_END`,`LIKED`,`COMMENTED`,`SHARED`. • If `action_scene` is `CREATOR_RELATED`, the allowed values are: `FOLLOWING`, `VIEW_HOMEPAGE`. • If `action_scene` is `HASHTAG_RELATED`, the allowed value is `VIEW_HASHTAG`. ⏎ **Note**: ⏎ Currently, when creating an ad group via **TikTok Ads Manager (TTAM)**, you cannot define the kind of user actions (`video_user_actions`). By default, the ad group created via **TTAM** will use the options as follows: • For an ad group with video interaction targeting (`action_scene`= `VIDEO_RELATED`), all the four options (`["WATCHED_TO_END","LIKED","COMMENTED","SHARED"]`) will be used. • For an ad group with creator interaction targeting (`action_scene`=`CREATOR_RELATED`), both options(`["FOLLOWING","VIEW_HOMEPAGE"]`) will be used.However, when creating ad groups via **API**, you can still pass in the desired enum value combinations, for example: `["LIKED","COMMENTED"]` if `action_scene`=`VIDEO_RELATED`. |
| ↳↳ action_category_ids | string[] | Chỉ hợp lệ khi TikTok placement is the only placement selected. ⏎ IDs of the video interactions categories, creator interactions categories, hashtags, or hashtag bundles that you want to use to target audiences. ⏎ • To search for or list video interactions category IDs or creator interactions category IDs, use [/targeting/search/](70-tools-p1.md#doc-1796638342793218) (recommended) or [/tool/action_category/](70-tools-p1.md#doc-1737166752522241). • To get hashtag IDs or hashtag bundle IDs, use [/targeting/search/](70-tools-p1.md#doc-1796638342793218) (recommended) or [/tool/hashtag/recommend/](70-tools-p1.md#doc-1736271339521025). • To get recommended video interactions category IDs, creator interactions category IDs, hashtag IDs, or hashtag bundle IDs based on your industry, use [/tool/targeting_category/recommend/](70-tools-p1.md#doc-1736275204260866). |
| ↳ smart_interest_behavior_enabled | boolean | Liệu Smart interests & behaviors is turned on. ⏎ Các giá trị được hỗ trợ: `true`, `false`. ⏎ To learn more about Smart interests & behaviors and how to turn on Smart interests & behaviors, see [Smart Targeting](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1783164662979586). |
| ↳ smart_audience_enabled | boolean | Có thực hiện turn on Smart audience. ⏎ Các giá trị được hỗ trợ: `true`, `false`. ⏎ To learn more about Smart audience and how to turn on Smart audience, see [Smart Targeting](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1783164662979586). |
| ↳ spending_power | string | Spending power that you want to target. ⏎ Các giá trị enum hỗ trợ: `ALL`, `HIGH`. ⏎ If it is set to `HIGH`, you can target high spending users who typically spend more on purchases on TikTok ads than average users. |
| ↳ household_income | string[] | Household income that you want to target. ⏎ Các giá trị enum hỗ trợ: `TOP5`(Top 5% of ZIP codes), `TOP10`(Top 10% of ZIP codes), `TOP10_25`(Top 10% -25% of ZIP codes), `TOP25_50`(Top 25% - 50% of ZIP codes). |
| ↳ min_android_version | string | Minimum Android version. ⏎ Để xem danh sách giá trị enum, xem [Enumeration - Minimum Android Version](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ min_ios_version | string | Audience minimum ios version. ⏎ Để xem danh sách giá trị enum, xem [Enumeration - Minimum iOS Version](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ device_model_ids | string[] | List of device model IDs. ⏎ To get the complete list of device model IDs and their statuses, use [/tool/device_model/](70-tools-p1.md#doc-1737172880570369). Only active devices (`is_active` = `true` in the response of [/tool/device_model/](70-tools-p1.md#doc-1737172880570369)) can be used to create ad groups. ⏎ **Note**: Device model (`device_model_ids`) and device price (`device_price_ranges`) cannot be set at the same time. |
| ↳ network_types | string[] | Network types that you want to target. ⏎ Để xem danh sách giá trị enum, xem [Enumeration - Connection Type](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ carrier_ids | string[] | Carriers that you want to target. ⏎ The carriers must be consistent with the location(s) that you want to target. ⏎ To get the enum values, use [/tool/carrier/](70-tools-p1.md#doc-1737168013095938). A carrier is Chỉ hợp lệ khi the `in_use` field for the carrier is `true`. |
| ↳ isp_ids | string[] | Chỉ hợp lệ khi you specify a valid location ID at the country or region level via `location_ids` at the same time. ⏎ IDs of the Internet service providers (ISP) that you want to target. ⏎ You can use [/tool/targeting/list/](70-tools-p2.md#doc-1762962378261506) to get the ISP IDs that you can target for a location ID. ⏎ **Note**: When you pass in `isp_ids`, you cannot set the placement as Global App Bundle only (`placements` =`PLACEMENT_GLOBAL_APP_BUNDLE`). |
| ↳ device_price_ranges | number[] | Targeting device price range. ⏎ 10000 means 1000+. The numbers must be in multiples of 50. ⏎ **Important**: The upper limit you set will be added by 50 and the resulting new number will be used as the actual upper limit for device targeting. The actual upper limit is shown in the ad group settings in TikTok Ads Manager. If you set and get the price range of [0, 250], it actually means [0, 300]. |
| ↳ saved_audience_id | string | Valid when the following conditions are both met: • The category of Housing, Employment, or Credit (`specical_industries`) is NOT specified in your campaign. • TikTok placement is selected in your ad group (i.e., `placement_type` is set as `PLACEMENT_TYPE_AUTOMATIC` or `placement_type` is set as `PLACEMENT_TYPE_NORMAL` and `PLACEMENT_TIKTOK` is included in `placements`). ⏎ Saved Audience ID. ⏎ To obtain the list of Saved Audiences within your ad account, use [/dmp/saved_audience/list/](09-audience.md#doc-1780154619404290). ⏎ Before using this field, call [/dmp/saved_audience/create/](09-audience.md#doc-1780154541898754) to create a Saved Audience and get the Saved Audience ID in response. The ID tài khoản quảng cáo TikTok associated with your Saved Audience should be the same as the ID tài khoản quảng cáo TikTok in your ad group. Otherwise, an error will occur. ⏎ If you use `saved_audience_id` to create an ad group, we will return both the Saved Audience ID and the targeting options that are included within your Saved Audience in response. ⏎ See [Create a Saved Audience](../09-marketing-api/audience.md#doc-1780156510696449) to find out the detailed workflow and code examples. ⏎ **Note**: ⏎ • When creating a Saved Audience via [/dmp/saved_audience/create/](09-audience.md#doc-1780154541898754), you can specify various targeting options, including `gender`. However, be aware that if you are creating an ad group based on a Saved Audience, it’s essential to avoid setting both the `saved_audience_id` and targeting options (such as `gender`) defined within your Saved Audience at the same time.. • In cases where the targeting settings in your Saved Audience conflict with those in your ad group, the settings from your Saved Audience will take precedence. As a result, the conflicting targeting options in your ad group will be ignored. • For example, if you create a Saved Audience where `gender` is set to `GENDER_FEMALE` and then use that Saved Audience to create an ad group while specifying `gender` as `GENDER_MALE`, the resulting ad group will adopt `GENDER_FEMALE` as the gender targeting configuration, reflecting what is set in the Saved Audience. • If the `saved_audience_id` was created with `age_groups` specified, the age restriction rules outlined in [New age restrictions for ads on TikTok](../15-appendix/phu-luc-p1.md#doc-1788755983247362) for different advertising objectives also apply. Make sure that the age targeting setting is allowed before you use the Saved Audience (`saved_audience_id` ) in the ad group. |
| ↳ blocked_pangle_app_ids | string[] | Pangle app block ID list. ⏎ You can get an ID via the `app_package_id` field returned by [/pangle_block_list/get/](55-pangle.md#doc-1740039957181441). It only takes effect when Pangle placement is selected. |
| budget_auto_adjust_strategy | string | Chỉ hợp lệ khi the following conditions are all met:  • At the campaign level: `budget_optimize_on` is `false`.  • At the ad group level:  • When `objective_type` is `APP_PROMOTION`:  • `budget_mode` is `BUDGET_MODE_DYNAMIC_DAILY_BUDGET`. • `optimization_goal` is `VALUE`. • `deep_bid_type` is `VO_MIN_ROAS`. • `vbo_window` is `ZERO_DAY`.  • When `objective_type` is `LEAD_GENERATION`: • `budget_mode` is `BUDGET_MODE_DYNAMIC_DAILY_BUDGET`. • `bid_type` is`BID_TYPE_CUSTOM`. ⏎ The ad group budget strategy for custom ad group budget. ⏎ Các giá trị enum hỗ trợ: • `AUTO_BUDGET_INCREASE`: To enable Goal-based budget increase. Allow your budget to automatically increase when your ads are performing well and target CPA, Day 0 target ROAS, and budget requirements are met.   • When `budget_auto_adjust_strategy` is `AUTO_BUDGET_INCREASE`, the specified `budget` will be the initial daily budget. Your daily budget will be allowed to automatically increase by 20%, up to 10 times per day, when your budget utilization reaches 90% or more. Your daily budget will reset to your original daily budget each day. • `UNSET`: To disable Goal-based budget increase. ⏎ **Note**: Enabling Goal-based budget increase is currently an allowlist-only feature. If you would like to access it, please contact your TikTok representative. |
| budget | float | Fixed ad group budget or initial ad group budget. • When `budget_auto_adjust_strategy`  is `UNSET`, this field represents your fixed ad group budget. • When `budget_auto_adjust_strategy`  is `AUTO_BUDGET_INCREASE`, this field represents your initial ad group budget. To retrieve the current ad group budget, check the returned `current_budget`. ⏎ For how to configure budget settings, see [Budget](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1739381246298114). To directly see the daily budget value range for a currency, see [Currency-Daily budget value range](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1737585839634433). |

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location  --request POST 'https://business-api.tiktok.com/open_api/v1.3/smart_plus/adgroup/update/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id": "{{advertiser_id}}",
    "adgroup_id": "{{adgroup_id}}",
    "adgroup_name": "{{adgroup_name}}"
}'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| - | - | - |
| code | number | Mã phản hồi. Để xem danh sách đầy đủ các mã phản hồi và mô tả, xem [Phụ lục - Mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | ID nhật ký (log ID) của yêu cầu, dùng để định danh duy nhất yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ advertiser_id | string | ID tài khoản quảng cáo TikTok. |
| ↳ campaign_id | string | ID chiến dịch quảng cáo. |
| ↳ campaign_name | string | The name of the campaign that the ad group belongs to. |
| ↳ adgroup_id | string | ID nhóm quảng cáo. |
| ↳ adgroup_name | string | Ad group name. |
| ↳ operation_status | string | Trạng thái hoạt động. ⏎ Các giá trị enum hỗ trợ: • `ENABLE` : The ad group is enabled (in 'ON' status). • `DISABLE`: The ad group is disabled (in 'OFF' status). |
| ↳ secondary_status | string | Ad group secondary status. ⏎ Để xem danh sách giá trị enum, xem [Enumeration- Ad group Status - Secondary Status](https://business-api.tiktok.com/portal/docs/enumerations-appendix/v1.3#anchor-2-2). |
| ↳ catalog_id | string | Returned when `catalog_enabled` is  `true` at the campaign level. ⏎ The ID of the catalog used in the ad group. |
| ↳ catalog_authorized_bc_id | string | Returned when `catalog_enabled` is  `true` at the campaign level. ⏎ The ID of the Business Center that the catalog (`catalog_id`) belongs to. |
| ↳ product_source | string | Product source where you want to get products for promotion. ⏎ Enum value: `CATALOG` (catalog). |
| ↳ promotion_type | string | Promotion type (Optimization location). You can decide where you'd like to promote your products using this field. ⏎ Currently, we support `APP_ANDROID`, `APP_IOS`, `WEBSITE`, `MINI_GAME`, `NATIVE_SERIES`, `LEAD_GENERATION`, and `LEAD_GENERATION_MULTI_DESTINATION`. • When `objective_type` is `APP_PROMOTION`  and `app_promotion_type` is `APP_INSTAL`, this field will be `APP_ANDROID` or `APP_IOS`. • When `objective_type` is `APP_PROMOTION` and `app_promotion_type` is `MINIS`, this field will be `MINI_APP`, `MINI_GAME`, or `NATIVE_SERIES`. • When `objective_type` is `WEB_CONVERSIONS`: • If `sales_destination` is `WEBSITE`, this field will be `WEBSITE`. • If `sales_destination` is `APP`, this field will be `APP_ANDROID` or `APP_IOS`. • When `objective_type` is `LEAD_GENERATION`, this field will be any of the following values: • `LEAD_GENERATION` • `LEAD_GEN_CLICK_TO_TT_DIRECT_MESSAGE` • `LEAD_GEN_CLICK_TO_SOCIAL_MEDIA_APP_MESSAGE` • `LEAD_GEN_CLICK_TO_CALL` • `LEAD_GENERATION_MULTI_DESTINATION` |
| ↳ optimization_locations | object[] | Returned when `promotion_type` is `LEAD_GENERATION_MULTI_DESTINATION`. ⏎ A list of optimization locations for the Lead Generation ad group. ⏎ To learn about the ad type where this field can be used, see [Create an Upgraded Smart+ Lead Generation Campaign with multiple location selection](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1876685025962241). |
| ↳↳ promotion_type | string | Promotion type (Optimization location). ⏎ You can decide where you want audiences to convert or complete an action. ⏎ Các giá trị enum hỗ trợ: `LEAD_GENRATION`, `LEAD_GEN_CLICK_TO_TT_DIRECT_MESSAGE`. |
| ↳↳ promotion_target_type | string | The optimization location for Lead Generation objective. ⏎ Các giá trị enum hỗ trợ: • `INSTANT_PAGE`: Instant Form. To create a fast-loading in-app TikTok Instant Form to collect more leads. • `EXTERNAL_WEBSITE`: Website Form. To use a landing page that has the Website Form or the TikTok Instant Page that redirects to the website with the Website Form to collect more leads. |
| ↳↳ optimization_event | string | Optimization event. ⏎ Các giá trị enum hỗ trợ: • `ON_WEB_REGISTER`: Complete registration. • `CONSULT`: Contact. • `FORM`: Submit form. • `ON_WEB_SUBSCRIBE`: Subscribe. |
| ↳ promotion_website_type | string | TikTok Instant Page type. ⏎ Currently, we only support `TIKTOK_NATIVE_PAGE`(To use TikTok Instant Page). |
| ↳ promotion_target_type | string | The optimization location for Lead Generation objective. ⏎ Các giá trị enum hỗ trợ: • `INSTANT_PAGE`: Instant Form. To create a fast-loading in-app TikTok Instant Form to collect more leads. • `EXTERNAL_WEBSITE`: Website Form. To use a landing page that has the Website Form or the TikTok Instant Page that redirects to the website with the Website Form to collect more leads. |
| ↳ optimization_goal | string | The measurable results that you'd like to drive your ads with. ⏎ Để xem danh sách giá trị enum, xem [Enumeration - Optimization Goal](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ app_id | string | The App ID of the app to promote. ⏎ To get a list of App IDs, use [/app/list/](43-events-1-0-p1.md#doc-1740859313270786). |
| ↳ gaming_ad_compliance_agreement | string | Returned only in any of the following scenarios: • Scenario 1: When the following conditions are both met at the campaign level: • `objective_type` is `APP_PROMOTION`. • `app_promotion_type` is `APP_RETARGETING`. • Scenario 2: When the following conditions are all met at the campaign level: • `objective_type` is `APP_PROMOTION`. • `app_promotion_type` is `APP_INSTALL`. • `campaign_type` is `REGULAR_CAMPAIGN`. ⏎ Có thực hiện agree to the Compliance Assurance Policy for Gaming Advertisers on TikTok. ⏎ The policy is as follows: Yo confirms and attest that any gaming application, product or service (game) you desire to advertise on TikTok, including any associated URL(s), (a) complies with all applicable laws and regulations of the jurisdictions where the game can be accessed or played, and upon request, can provide supporting documentation as evidence of why the game is not considered illegal gambling or lottery; and (b) has not been and is not part of any investigation or lawsuit regarding the game's legality or regulatory compliance. ⏎ Các giá trị enum hỗ trợ: • `ON`: To agree to the policy. • `OFF`: To leave the policy not accepted. |
| ↳ pixel_id | string | ID TikTok Pixel. |
| ↳ app_config | object[] | Returned when `sales_destination` is `WEB_AND_APP`. ⏎ Details of the app or apps to promote. |
| ↳↳ app_id | string | The App ID of the app to promote. |
| ↳ minis_id | string | Returned when `promotion_type` is `MINI_APP` or `MINI_GAME`. ⏎ The ID of the TikTok Mini. |
| ↳ optimization_event | string | Conversion event for the ad group. ⏎ See [Conversion events](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1739361474981889) for more. ⏎ **Note**: If you enable Value-Based Optimization during ad group creation by setting your `optimization_event` to either `IMPRESSION_LEVEL_AD_REVENUE` or `AD_REVENUE_VALUE`(note that both enums are equivalent and have the exact same effect), you will always receive `IMPRESSION_LEVEL_AD_REVENUE` as the `optimization_event` in the response. |
| ↳ custom_conversion_id | string | The ID of the Custom Conversion used in the ad group. |
| ↳ deep_funnel_optimization_status | string | With deep funnel optimization, you can select a secondary event alongside the primary optimization event, which can help improve campaign effectiveness. ⏎ Các giá trị enum hỗ trợ: • `ON`: enabled. • `OFF`: disabled. |
| ↳ deep_funnel_event_source | string | Returned when `deep_funnel_optimization_status` is `ON`. ⏎ The event source type. ⏎ Các giá trị enum hỗ trợ: • `PIXEL`: Pixel. • `OFFLINE`: Offline Event Set. • `CRM`: CRM Event Set. |
| ↳ deep_funnel_event_source_id | string | Returned when `deep_funnel_optimization_status` is `ON`. ⏎ Event Source ID. • When `deep_funnel_event_source` is `PIXEL` , this field represents a ID TikTok Pixel. • When `deep_funnel_event_source` is `OFFLINE`, this field represents an Offline Event Set ID. • When `deep_funnel_event_source` is `CRM`, this field represents a CRM Event Set ID. |
| ↳ deep_funnel_optimization_event | string | Returned when `deep_funnel_optimization_status` is `ON`. ⏎ Deep funnel optimization event. ⏎ Example: `SHOPPING`. |
| ↳ app_attribution_source | string | Attribution source for your app. ⏎ The attribution source you choose will be used for optimization, bidding, and reporting. ⏎ Các giá trị enum hỗ trợ: • `MMP`: MMP (mobile measurement partner) attribution. Signals from your selected MMP will be used for attribution. • `SAN`: SAN (self-attribution network) attribution. Signals from TikTok SAN will be used for attribution. |
| ↳ app_data_source | string | Data source for your app. ⏎ The attribution signals you select will be used for reporting. ⏎ Các giá trị enum hỗ trợ: • `MMP`: MMP signals. Signals from your MMP will be used for reporting. • `EVENT_SDK`: App Events SDK signals. Signals from TikTok App Events SDK will be used for reporting. • `EVENT_API`: Events API signals. Signals from TikTok Events API will be used for reporting. |
| ↳ identity_id | string | Returned only in any of the following scenarios:  • Scenario 1: When `promotion_type` is `NATIVE_SERIES`. • Scenario 2: When `promotion_type` is `LEAD_GEN_CLICK_TO_TT_DIRECT_MESSAGE` and your ad account is allowlisted for selecting a TikTok account at the ad group level in TikTok Direct Messaging Ads. ⏎ Identity ID. |
| ↳ identity_type | string | Returned only  in any of the following scenarios:  • Scenario 1: When `promotion_type` is `NATIVE_SERIES`. • Scenario 2: When `promotion_type` is `LEAD_GEN_CLICK_TO_TT_DIRECT_MESSAGE` and your ad account is allowlisted for selecting a TikTok account at the ad group level in TikTok Direct Messaging Ads. ⏎ Identity type. ⏎ Các giá trị enum hỗ trợ: • `TT_USER` : TikTok Business Account User. • `BC_AUTH_TT`: The TikTok account that a Business Center is authorized to access. ⏎ See [Identities](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1738958351620097) for details. |
| ↳ identity_authorized_bc_id | string | Returned when `identity_type` is `BC_AUTH_TT`. ⏎ ID of the Business Center that a TikTok Account User in Business Center identity is associated with. |
| ↳ native_series_id | string | The ID of a TikTok Series. ⏎ Series offers exclusive and premium video packages produced by creators. Access to Series is available to purchase through the creator's profile and links attached to TikTok videos. |
| ↳ messaging_app_type | string | The type of instant messaging app or customized URL to use in the Instant Messaging Ad Group. ⏎ Các giá trị enum hỗ trợ: • `MESSENGER`: Messenger.  • `WHATSAPP`: WhatsApp.  • `ZALO`: Zalo.  • `LINE`: Line.  • `IM_URL`: Instant Messaging URL. ⏎ To learn more about how to create Upgraded Smart+ TikTok Instant Messaging Ads, see [Create an Upgraded Smart+ Lead Generation Campaign with optimization location as instant messaging apps](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1847302988449921). |
| ↳ zalo_id_type | string | The type of Zalo contact format. ⏎ Các giá trị enum hỗ trợ: • `ZALO_OFFICIAL_ACCOUNT`: Zalo Official Account ID.  • `ZALO_PHONE_ACCOUNT`: Zalo phone number. |
| ↳ messaging_app_account_id | string | The ID of the instant messaging app account. • When `messaging_app_type` is `MESSENGER`, this field represents the Facebook Page ID. • When `messaging_app_type` is `LINE`, this field represents the LINE Business ID. • When `zalo_id_type` is `ZALO_OFFICIAL_ACCOUNT`, this field represents the Zalo Official Account ID. • When `messaging_app_type` is `WHATSAPP` or when `zalo_id_type` is `ZALO_PHONE_ACCOUNT`, this field represents the WhatsApp or Zalo phone number automatically populated based on the specified `phone_info`. |
| ↳ message_event_set_id | string | The ID of the message event set to be used in the Instant Messaging Ad Group. ⏎ If the instant messaging app account, either the Messenger account or Zalo Official Account specified via `messaging_app_account_id` or the WhatsApp or Zalo phone account matched from the specified `phone_info`, in your ad group settings matches an existing event set, this field will be **automatically populated** with the unique message event set associated with the instant messaging app account you choose. |
| ↳ phone_info | object | Details of WhatsApp or Zalo phone number. |
| ↳↳ phone_region_code | string | The region code for WhatsApp or Zalo phone number. ⏎ Example: `US`. |
| ↳↳ phone_region_calling_code | string | The region calling code for the WhatsApp or Zalo phone number. ⏎ Example: `+1`. |
| ↳↳ phone_number | string | The WhatsApp or Zalo phone number. |
| ↳ bid_type | string | Bidding strategy. ⏎ For enum values and their descriptions, see [Enumeration - Bidding Strategy](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ bid_price | float | Giá thầu mục tiêu cho mỗi lượt nhấp. Hệ thống sẽ nhắm tới việc đạt được nhiều kết quả nhất trong khi vẫn duy trì chi phí trung bình trên mỗi kết quả xấp xỉ hoặc thấp hơn mức chỉ định. |
| ↳ conversion_bid_price | float | Giá thầu mục tiêu cho mỗi lượt chuyển đổi hoặc chi phí cho mỗi lượt xem trang đích. Hệ thống sẽ nhắm tới việc đạt được nhiều kết quả nhất trong khi vẫn duy trì chi phí trung bình trên mỗi kết quả xấp xỉ hoặc thấp hơn mức chỉ định. |
| ↳ deep_bid_type | string | Bidding strategy for in-app events. ⏎ For enum values and their descriptions, see [Enumeration - Deep Event Bidding Strategy](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ roas_bid | float | ROAS mục tiêu cho tính năng Tối ưu hóa theo giá trị (Value-Based Optimization). |
| ↳ value_rule_set_id | string | ID of the value rule set associated with the ad group. |
| ↳ incentive_offer_type | string | The type of incentive offer applicable to the Upgraded Smart+ Ad Group. ⏎ If your ad group meets the eligibility criteria and exceeds certain CPA or Minimum ROAS/Target ROAS thresholds, you will be incentivized with ad credits to use within the same ad account. ⏎ To learn more about the incentive offer eligibility criteria and the calculation of incentive amount, see [Smart+ Platform Incentive Offer (Cost Cap/Minimum ROAS/Target ROAS)](https://ads.tiktok.com/help/article/incentive-offer). ⏎ Các giá trị enum hỗ trợ: • `INELIGIBLE`: The ad group is ineligible for any incentive offer. • `COST_CAP_AND_MIN_ROAS`: The ad group uses the Cost Cap or Minimum ROAS/Target ROAS bidding strategy and is eligible for the incentive offer. ⏎ • To check the bid protection (incentive offer) eligibility for a list of Upgraded Smart+ Campaigns or Upgraded Smart+ Ad Groups, use [/report/bid_protection/status/get/](70-tools-p2.md#doc-1874392512912449). • To retrieve the bid protection history and ad credit from the past 60 days for a list of Upgraded Smart+ Campaigns or Upgraded Smart+ Ad Groups, use [/report/bid_protection/detail/get/](70-tools-p3.md#doc-1874392516418561). |
| ↳ vbo_window | string | The time window of the specified bidding strategy for [VBO IAA](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1739381743067137) (Value-Based Optimization for in-app advertising) or [VBO IAP](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1739381743067137) (Value-Based Optimization for in-app purchase). ⏎ Các giá trị enum hỗ trợ: • `SEVEN_DAYS`: The first seven days (day 7). • `ZERO_DAY`: The current day (day 0). |
| ↳ click_attribution_window | string | Click-through window. This attribution window is the time between when a person clicks your ad and then takes an action. ⏎ Các giá trị enum hỗ trợ: • `OFF`: Off. • `ONE_DAY`: 1-day click. • `SEVEN_DAYS`: 7-day click. • `FOURTEEN_DAYS`: 14-day click. • `TWENTY_EIGHT_DAYS`: 28-day click. • `THIRTY_DAYS`: 30-day click. • `THIRTY_TWO_DAYS`: 32-day click. • `ONE_HUNDRED_EIGHTY_DAYS`: 180-day click. |
| ↳ engaged_view_attribution_window | string | Engaged view-through window. This attribution window is the time after someone watches at least 6 seconds of your video ad that a conversion is counted. ⏎ Các giá trị enum hỗ trợ: • `OFF`: off. • `ONE_DAY`: 1-day engaged view. • `SEVEN_DAYS`: 7-day engaged view. • `FOURTEEN_DAYS`: 14-day engaged view. • `TWENTY_EIGHT_DAYS`: 28-day engaged view. |
| ↳ view_attribution_window | string | View-through window. This attribution window is the time between when a person views your ad and then takes an action. ⏎ Các giá trị enum hỗ trợ: • `OFF`: Off. • `ONE_DAY`: 1-day view. • `SEVEN_DAYS`: 7-day view. |
| ↳ attribution_event_count | string | Event count (Statistic type). ⏎ The way that people's actions are counted after only viewing or clicking an ad. ⏎ Các giá trị enum hỗ trợ: • `UNSET`: Unset. • `EVERY`: Every. To count multiple events from someone as separate conversions. • `ONCE`: Once. To count multiple events from someone as 1 conversion. |
| ↳ billing_event | string | Billing event. ⏎ Để xem danh sách giá trị enum, xem [Enumerations - Billing event](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ pacing | string | Delivery type. Your choice of ad delivery type determines the speed at which your daily budget is used. ⏎ Các giá trị enum hỗ trợ: • `PACING_MODE_SMOOTH`: Standard. Your budget will be used as evenly as possible depending on market demand and peaktime rates. This delivery type is suitable for advertisers who prefer steady spending. |
| ↳ automated_keywords_enabled | boolean | Có bật từ khóa tự động và cho phép hệ thống tìm kiếm các từ khóa liên quan để mở rộng phạm vi tiếp cận và cải thiện kết quả hay không. ⏎ Các giá trị được hỗ trợ: `true`, `false`. |
| ↳ search_keywords | object[] | Returned only for Search Ads Campaigns. ⏎ A list of search keywords, that is, words or phrases that are used to match your ads with the terms people are searching for. |
| ↳↳ keyword | string | The search keyword. |
| ↳↳ match_type | string | The match type for the search keyword. ⏎ Các giá trị enum hỗ trợ: • `PRECISE_WORD`: exact match. Ads only show when a search includes the exact phrase or close variations, with additional words allowed before or after. • `PHRASE_WORD`: phrase match. Ads only show when a search exactly matches your keyword or a very close variation. • `BROAD_WORD`: broad match. Ads are shown for a wide range of relevant searches to offer the widest reach. |
| ↳↳ audit_status | string | The review status of the search keyword. ⏎ Các giá trị enum hỗ trợ: • `AUDITING`: The keyword is under review. • `PASS`: The keyword has passed review and can be delivered. • `REJECTED`: The keyword failed to pass the review and cannot be delivered. |
| ↳↳ reject_info | object[] | Returned only when `audit_status` is `REJECTED`. ⏎ Details about the rejection. |
| ↳↳↳ forbidden_location | string | The targeted region that failed the review. ⏎ Để xem danh sách giá trị enum, xem [Appendix - Location codes](../15-appendix/phu-luc-p1.md#doc-1737585867307010). |
| ↳↳↳ reject_reasons | object[] | List of rejection reasons. |
| ↳↳↳↳ reason | string | The rejection reason. |
| ↳ budget_mode | string | Ad group budget mode. ⏎ Các giá trị enum hỗ trợ: • `BUDGET_MODE_TOTAL`: Lifetime budget. • `BUDGET_MODE_DYNAMIC_DAILY_BUDGET`: Dynamic daily budget. It is the average daily budget over a week. Daily costs will not exceed 125% of the average daily budget. Weekly costs will not exceed the average daily budget * 7. |
| ↳ budget_auto_adjust_strategy | string | Returned only when the following conditions are both met: • At the campaign level: `budget_optimize_on` is `false`. • At the ad group level: `budget_mode` is `BUDGET_MODE_DYNAMIC_DAILY_BUDGET`. ⏎ The ad group budget strategy for custom ad group budget. ⏎ Các giá trị enum hỗ trợ: • `AUTO_BUDGET_INCREASE`: To enable Goal-based budget increase. Allow your budget to automatically increase when your ads are performing well and target CPA, Day 0 target ROAS, and budget requirements are met.  • When `budget_auto_adjust_strategy` is `AUTO_BUDGET_INCREASE`, the specified `budget` will be the initial daily budget. Your daily budget will be allowed to automatically increase by 20%, up to 10 times per day, when your budget utilization reaches 90% or more. Your daily budget will reset to your original daily budget each day. • `UNSET`: To disable Goal-based budget increase. |
| ↳ budget | float | Fixed ad group budget or initial ad group budget. • When `budget_auto_adjust_strategy`  is `UNSET`, this field represents your fixed ad group budget. • When `budget_auto_adjust_strategy`  is `AUTO_BUDGET_INCREASE`, this field represents your initial ad group budget. To retrieve the current campaign budget, check the returned `current_budget`. |
| ↳ current_budget | float | Returned only when `budget_auto_adjust_strategy`  is `AUTO_BUDGET_INCREASE`. ⏎ Current ad group budget for an ad group with Goal-based budget increase enabled. |
| ↳ min_budget | float | Ad group minimum budget. ⏎ The system will aim to spend at least this amount, but it is not guaranteed. |
| ↳ schedule_type | string | Schedule type. ⏎ Các giá trị enum hỗ trợ: • `SCHEDULE_FROM_NOW`: To run the ad group continuously after the scheduled start time. • `SCHEDULE_START_END`: To run the ad group between the scheduled start time and end time. |
| ↳ schedule_start_time | string | Ad group delivery start time, in the format of `YYYY-MM-DD HH:MM:SS` (UTC+0). |
| ↳ schedule_end_time | string | Ad group delivery end time, in the format of`YYYY-MM-DD HH:MM:SS` (UTC+0). |
| ↳ movie_premiere_date | string | The theatrical release date, in the format of `YYYY-MM-DD` (UTC+0). ⏎ Providing the movie release date allows the system to incorporate this timing into performance enhancements. |
| ↳ dayparting | string | Ad delivery arrangement, in the format of a string that consists of 48 x 7 characters. Each character is mapped to a 30-minute timeframe from Monday to Sunday. Each character can be set to either 0 or 1. 1 represents delivery in the 30-minute timeframe, and 0 stands for non-delivery in the 30-minute timeframe. The first character is mapped to 0:01-0:30 of Monday; The second character is mapped to 0:31-1:00 of Monday, and the last character represents 23:31-0:00 Sunday. ⏎ **Note**: All-0 and all-1 values are considered full-time delivery. |
| ↳ targeting_optimization_mode | string | Chế độ tối ưu hóa nhắm mục tiêu đối tượng. • `MANUAL`: Nhắm mục tiêu tùy chỉnh. Bạn có thể sử dụng các cài đặt nhắm mục tiêu tùy chỉnh để kiểm soát chính xác người nhìn thấy quảng cáo. Điều này có thể hạn chế phân phối và ảnh hưởng đến hiệu suất chiến dịch. • `AUTOMATIC`: Automatic targeting. You can use automatic targeting to leverage real-time data and machine learning to target audiences most likely to engage with your ads |
| ↳ suggestion_audience_enabled | boolean | Có bật tính năng gợi ý đối tượng (audience suggestions) hay không. ⏎ Audience suggestions guide automatic targeting by choosing additional audience settings. These serve as suggestions only, and delivery to those audiences is not guaranteed. ⏎ Các giá trị được hỗ trợ: `true`, `false`. |
| ↳ targeting_spec | object | Cài đặt nhắm mục tiêu đối tượng. |
| ↳↳ app_targeting_type | string | Returned only when the following conditions are all met: • At the campaign level: • `objective_type` is `WEB_CONVERSIONS` • `sales_destination` is `APP`. • `optimization_goal` is `CLICK`, `IN_APP_EVENT`, or `VALUE`. ⏎ App targeting type. ⏎ Các giá trị enum hỗ trợ: • `PROSPECT`: Prospecting. Find prospective customers, including those who have not interacted with your products. • `RETARGETING`: Retargeting. Show ads to people who have already interacted with your business on and off TikTok. |
| ↳↳ location_ids | string[] | IDs of the locations that you want to target. |
| ↳↳ zipcode_ids | string[] | Zip code IDs or postal code IDs of the targeted locations. |
| ↳↳ spc_audience_age | string | Nhóm tuổi mà nhóm quảng cáo nhắm mục tiêu. ⏎ Các giá trị enum hỗ trợ: • `ALL`: all age groups. • `OVER_EIGHTEEN`: 18+. • `OVER_TWENTY_FIVE`: 25+. |
| ↳↳ languages | string[] | Mã các ngôn ngữ bạn muốn nhắm mục tiêu. ⏎ For the list of language codes supported, see [Enumerations - Language Code](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳↳ operating_systems | string[] | Hệ điều hành thiết bị bạn muốn nhắm mục tiêu. ⏎ Các giá trị enum hỗ trợ: `ANDROID`, `IOS` |
| ↳↳ excluded_audience_ids | string[] | List of audience IDs to be excluded. |
| ↳↳ age_groups | string[] | Các nhóm tuổi bạn muốn nhắm mục tiêu. ⏎ Để xem danh sách giá trị enum, xem [Enumeration - Age Group](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳↳ gender | string | Gender that you want to target. ⏎ Các giá trị enum hỗ trợ: `GENDER_FEMALE`, `GENDER_MALE`, `GENDER_UNLIMITED`. |
| ↳↳ audience_ids | string[] | Danh sách các ID đối tượng. |
| ↳↳ shopping_ads_retargeting_type | string | The retargeting type. ⏎ Các giá trị enum hỗ trợ: • `LAB1`: Retargeting audiences who viewed products or added products to cart but didn't purchase products. • `LAB2`: Retargeting audiences who added products to cart but didn't purchase products. • `LAB3`: Retargeting audiences using custom combination. • `OFF`: No retargeting. |
| ↳↳ shopping_ads_retargeting_actions_days | number | Returned when `shopping_ads_retargeting_type` is `LAB1` or `LAB2`. ⏎ The valid time range for the specified audience action. Audiences who have completed the specified action within the time range will be retargeted. |
| ↳↳ included_custom_actions | object[] | Details of the catalog audience to include. ⏎ Catalog audience is based on people's interactions with specific products and often drives better performance than custom audience. |
| ↳↳↳ code | string | The custom action used to filter the audiences to be retargeted. ⏎ Các giá trị enum hỗ trợ: • `VIEW_PRODUCT`: The audience viewed the product. • `ADD_TO_CART`: The audience added the product to the cart. • `PURCHASE`: The audience purchased the product. |
| ↳↳↳ days | integer | The time range used to filter the audiences that completed the specified action. |
| ↳↳ excluded_custom_actions | object[] | Details of the catalog audience to exclude. ⏎ Improve ad performance by excluding products that people have already interacted with, ensuring they only see relevant ads from your brand. |
| ↳↳↳ code | string | The custom action used to filter out the audiences. ⏎ Các giá trị enum hỗ trợ: • `VIEW_PRODUCT`: The audience viewed the product. • `ADD_TO_CART`: The audience added the product to the cart. • `PURCHASE`: The audience purchased the product. |
| ↳↳↳ days | integer | The time range used to filter out the audiences that completed the specified action. |
| ↳↳ shopping_ads_retargeting_custom_audience_relation | string | The logical relation between the retargeting audience specified by `shopping_ads_retargeting_type` and the custom audience specified by `audience_ids`. ⏎ Các giá trị enum hỗ trợ: • `OR`: To combine the retargeting audience and the custom audience to create the targeted audience. The ad group will target anyone in catalog or custom audiences. • `AND`: To intersect between the retargeting audience and the custom audience to create the targeted audience. The ad group will target individuals who belong to both the retargeting audience and the custom audience. |
| ↳↳ included_pangle_audience_package_ids | string[] | IDs of the Pangle audiences that you want to include. |
| ↳↳ excluded_pangle_audience_package_ids | string[] | IDs of the Pangle audiences that you want to exclude. |
| ↳↳ interest_category_ids | string[] | IDs of general interest keywords that you want to use to target audiences. |
| ↳↳ interest_keyword_ids | string[] | IDs of additional interest categories that you want to use to target audience. ⏎ To search for additional interest categories, use [/targeting/search/](70-tools-p1.md#doc-1796638342793218) (recommended) or [/tool/interest_keyword/recommend/](70-tools-p1.md#doc-1763590884474882). |
| ↳↳ purchase_intention_keyword_ids | string[] | IDs of purchase intention categories that you want to use to target audiences with an interest in purchases related to a content category. |
| ↳↳ actions | object[] | A list of targeting behavioral category objects. |
| ↳↳↳ action_scene | string | The type of user behavior that you want to target. ⏎ Các giá trị enum hỗ trợ: • `VIDEO_RELATED`: Video interactions. • `CREATOR_RELATED`: Creator interactions. • `HASHTAG_RELATED`: Hashtag interactions. |
| ↳↳↳ action_period | number | The time period to include behaviors from. |
| ↳↳↳ video_user_actions | string[] | The specific user interactions that you want to target for the user behavior type. • If `action_scene` is `VIDEO_RELATED`, the allowed values are: `WATCHED_TO_END`,`LIKED`,`COMMENTED`,`SHARED`. • If `action_scene` is `CREATOR_RELATED`, the allowed values are: `FOLLOWING`, `VIEW_HOMEPAGE`. • If `action_scene` is `HASHTAG_RELATED`, the allowed value is `VIEW_HASHTAG`. |
| ↳↳↳ action_category_ids | string[] | IDs of the video interactions categories, creator interactions categories, hashtags, or hashtag bundles that you want to use to target audiences. |
| ↳↳ smart_interest_behavior_enabled | boolean | Liệu Smart interests & behaviors is turned on. ⏎ Các giá trị được hỗ trợ: `true`, `false`. ⏎ To learn more about Smart interests & behaviors and how to turn on Smart interests & behaviors, see [Smart Targeting](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1783164662979586). |
| ↳↳ smart_audience_enabled | boolean | Có thực hiện turn on Smart audience. ⏎ Các giá trị được hỗ trợ: `true`, `false`. ⏎ To learn more about Smart audience and how to turn on Smart audience, see [Smart Targeting](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1783164662979586). |
| ↳↳ spending_power | string | Spending power that you want to target. ⏎ Các giá trị enum hỗ trợ: `ALL`, `HIGH`. ⏎ If it is set to `HIGH`, you can target high spending users who typically spend more on purchases on TikTok ads than average users. |
| ↳↳ household_income | string[] | Household income that you want to target. ⏎ Các giá trị enum hỗ trợ: `TOP5`(Top 5% of ZIP codes), `TOP10`(Top 10% of ZIP codes), `TOP10_25`(Top 10% -25% of ZIP codes), `TOP25_50`(Top 25% - 50% of ZIP codes). |
| ↳↳ min_android_version | string | Minimum Android version. ⏎ Để xem danh sách giá trị enum, xem [Enumeration - Minimum Android Version](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳↳ min_ios_version | string | Audience minimum ios version. ⏎ Để xem danh sách giá trị enum, xem [Enumeration - Minimum iOS Version](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳↳ device_model_ids | string[] | List of device model IDs. |
| ↳↳ network_types | string[] | Network types that you want to target. ⏎ Để xem danh sách giá trị enum, xem [Enumeration - Connection Type](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳↳ carrier_ids | string[] | Carriers that you want to target. |
| ↳↳ isp_ids | string[] | IDs of the targeted Internet service providers. |
| ↳↳ device_price_ranges | number[] | Targeting device price range. 10000 means 1000+. The numbers must be in multiples of 50. ⏎ **Important**: The upper limit you set will be added by 50 and the resulting new number will be used as the actual upper limit for device targeting. The actual upper limit is shown in the ad group settings in TikTok Ads Manager. If you set and get the price range of [0, 250], it actually means [0, 300]. |
| ↳↳ saved_audience_id | string | Returned when you have specified `saved_audience_id` when creating an ad group. ⏎ Saved Audience ID. |
| ↳↳ blocked_pangle_app_ids | string[] | Pangle app block ID list. |
| ↳↳ brand_safety_type | string | Inventory filter tier for the Smart+ Campaign. ⏎ Các giá trị enum hỗ trợ: • `EXPANDED_INVENTORY`: Expanded inventory. Your ads will not appear next to explicitly inappropriate content, but they may appear next to content that features mature themes. • `STANDARD_INVENTORY`: Standard inventory. Your ads will appear next to content that is appropriate for most brands. • `LIMITED_INVENTORY`: Limited inventory. Your ads will not appear next to content that contains mature themes. • `NO_BRAND_SAFETY`: Full inventory without using any brand safety solution, which means your ads may appear next to some content featuring mature themes. ⏎ **Note**: The setting is automatically applied based on your [Brand Safety Hub](../09-marketing-api/quan-ly-chien-dich-tom-tat.md#doc-1739381752981505) configurations. To retrieve the details of such settings for your ad account, use [/tiktok_inventory_filters/get/](22-brand-safety.md#doc-1830112550443073). |
| ↳↳ category_exclusion_ids | string[] | Content exclusion category IDs. |
| ↳ is_hfss | boolean | Liệu promoted content is HFSS (High Fat, Salt, Sugar) Product/Brand. ⏎ Các giá trị được hỗ trợ: `true`, `false`. |
| ↳ is_lhf_compliance | boolean | Liệu promoted content complies with LHF (Less Healthy Foods) regulations. ⏎ When `is_lhf_compliance` is `true`, you confirm that any food or drink products you advertise on TikTok in the UK comply with the [2024 Less Healthy Foods Regulations](https://www.legislation.gov.uk/uksi/2024/1266/made) and all other applicable laws. ⏎ Các giá trị được hỗ trợ: `true`, `false`. |
| ↳ placement_type | string[] | The placement strategy that decides where your ads will be shown. ⏎ Các giá trị enum hỗ trợ: • `PLACEMENT_TYPE_AUTOMATIC`: Automatic placement. • `PLACEMENT_TYPE_NORMAL` : Select placement. |
| ↳ placements | string[] | The apps where you want to deliver your ads. ⏎ Các giá trị enum hỗ trợ: • `PLACEMENT_TIKTOK`: TikTok. • `PLACEMENT_PANGLE`: Pangle. • `PLACEMENT_GLOBAL_APP_BUNDLE`: Global App Bundle. |
| ↳ tiktok_subplacements | string[] | The subplacements within TikTok for your ads, allowing you to choose where your ads will appear. ⏎ Các giá trị enum hỗ trợ: • `LEMON8`: Lemon8, a community app for lifestyle content, focusing on real-life experiences, tips, guides, and product reviews. By including Lemon8 as a subplacement, your ads will appear in its For You feed, Search feed, and Immersive Video feed. [Learn more about Lemon8 for Performance Auction](https://ads.tiktok.com/help/article/about-lemon8-in-tiktok-ads-manager). • `PINE_DRAMA`: PineDrama, an app for watching short-form dramas. Ads will be placed on recommendation pages, within episode streams, and more. [Learn more about PineDrama for Performance Auction](https://ads.tiktok.com/help/article/about-pinedrama-for-performance-auction-in-tiktok-ads-manager). |
| ↳ search_result_enabled | boolean | Có thực hiện include your ads in Search Ads, namely to show your ads to users when they search for your business on TikTok. ⏎ Các giá trị được hỗ trợ: `true`, `false`. |
| ↳ comment_disabled | boolean | Có thực hiện allow comments on your ads on TikTok. ⏎ Các giá trị được hỗ trợ: `true`, `false`. |
| ↳ share_disabled | boolean | Có vô hiệu hóa chia sẻ chiến dịch lên các nền tảng của bên thứ ba hay không. ⏎ Các giá trị được hỗ trợ: `true`, `false`. |
| ↳ video_download_disabled | boolean | Liệu users can download your video ads on TikTok. ⏎ Các giá trị được hỗ trợ: `true`, `false`. |
| ↳ skip_learning_phase | boolean | Có thực hiện skip the learning stage. ⏎ Supported value: `true`. |
| ↳ create_time | string | The time when the ad group was created, in the format of `YYYY-MM-DD HH:MM:SS`(UTC+0). ⏎ Example: `2025-01-01 00:00:01`. |
| ↳ modify_time | string | The time when the ad group was last modified, in the format of `YYYY-MM-DD HH:MM:SS`(UTC+0). ⏎ Example: `2025-01-01 00:00:01`. |

### Ví dụ lệnh cURL (Example)
```http
// curl
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "adgroup_id": "{{adgroup_id}}",
        "adgroup_name": "{{adgroup_name}}",
        "advertiser_id": "{{advertiser_id}}",
        "app_id": "{{app_id}}",
        "attribution_event_count": "ONCE",
        "bid_type": "BID_TYPE_NO_BID",
        "billing_event": "OCPM",
        "budget": {{budget}},
        "budget_mode": "BUDGET_MODE_TOTAL",
        "campaign_id": "{{campaign_id}}",
        "campaign_name": "{{campaign_name}}",
        "click_attribution_window": "SEVEN_DAYS",
        "comment_disabled": false,
        "conversion_bid_price": 0,
        "create_time": "{{create_time}}",
        "dayparting": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111",
        "deep_bid_type": "DEFAULT",
        "engaged_view_attribution_window": "SEVEN_DAYS",
        "min_budget": 0,
        "modify_time": "{{modify_time}}",
        "operation_status": "ENABLE",
        "optimization_event": "ACTIVE",
        "optimization_goal": "INSTALL",
        "pacing": "PACING_MODE_SMOOTH",
        "placement_type": "PLACEMENT_TYPE_AUTOMATIC",
        "placements": [
            "PLACEMENT_TIKTOK",
            "PLACEMENT_GLOBAL_APP_BUNDLE",
            "PANGLE"
        ],
        "promotion_type": "APP_ANDROID",
        "schedule_end_time": "{{schedule_end_time}}",
        "schedule_start_time": "{{schedule_start_time}}",
        "schedule_type": "SCHEDULE_START_END",
        "search_result_enabled": true,
        "secondary_status": "ADGROUP_STATUS_CREATE",
        "share_disabled": false,
        "skip_learning_phase": true,
        "targeting_optimization_mode": "AUTOMATIC",
        "targeting_spec": {
            "actions": [],
            "age_groups": [
                "AGE_18_24",
                "AGE_25_34",
                "AGE_35_44",
                "AGE_45_54",
                "AGE_55_100"
            ],
            "brand_safety_type": "EXPANDED_INVENTORY",
            "gender": "GENDER_UNLIMITED",
            "location_ids": [
                "1562822"
            ],
            "operating_systems": [
                "ANDROID"
            ],
            "spc_audience_age": "OVER_EIGHTEEN",
            "spending_power": "ALL"
        },
        "video_download_disabled": false,
        "view_attribution_window": "ONE_DAY"
    }
}
```

---

<a id="doc-1843314908153858"></a>
<!-- doc_id: 1843314908153858 -->
<!-- doc_id: 1843314908153858 -->
# Cập nhật trạng thái hoạt động của nhóm quảng cáo Smart+ nâng cấp (Update the operation statuses of Upgraded Smart+ Ad Groups)
> Đường dẫn: API Reference > Smart+ nâng cấp > Nhóm quảng cáo > Cập nhật trạng thái hoạt động của nhóm quảng cáo Smart+ nâng cấp
Sử dụng endpoint này để bật, tạm dừng hoặc xóa các nhóm quảng cáo Smart+ nâng cấp.

## Yêu cầu gọi API (Request)
**Endpoint** https://business-api.tiktok.com/open_api/v1.3/smart_plus/adgroup/status/update/

**Method** POST

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type  ****(Bắt buộc)**** | string | Định dạng dữ liệu yêu cầu. ⏎ Allowed value: `application/json`. |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id  ****(Bắt buộc)**** | string | ID tài khoản quảng cáo TikTok. |
| adgroup_ids  ****(Bắt buộc)**** | string[] | Danh sách các ID nhóm quảng cáo cần thao tác. ⏎ Size range: 1-20. ⏎ Để lấy ID nhóm quảng cáo, sử dụng [/smart_plus/adgroup/get/](62-upgraded-smartplus-p2.md#doc-1843314879617026). |
| operation_status  ****(Bắt buộc)**** | string | The operation to perform on the ad groups. ⏎ Các giá trị enum hỗ trợ: `DISABLE` (pause), `ENABLE` (enable), `DELETE` (delete). ⏎ **Note**: The status of deleted ad groups or ad groups in deleted campaigns cannot be modified. |

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/smart_plus/adgroup/status/update/' \
--header 'Access-Token: "{{Access-Token}}"' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id": "{{advertiser_id}}",
    "adgroup_ids": ["{{adgroup_id}}","{{adgroup_id}}"],
    "operation_status":"DISABLE"
}'
```

### Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Mã phản hồi. Để xem danh sách đầy đủ các mã phản hồi và mô tả, xem [Phụ lục - Mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | ID nhật ký (log ID) của yêu cầu, dùng để định danh duy nhất yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ adgroup_list | object[] | A list of ad groups for which the operation was successful. |
| ↳↳ adgroup_id | string | The ID of the ad group for which the operation was successful. |
| ↳↳ status | string | The current status of the ad group for which the operation was successful. ⏎ Các giá trị enum hỗ trợ: `DISABLE` (paused), `ENABLE` (enabled), `DELETE` (deleted). |
| ↳ error_list | object[] | A list of errors and the corresponding failed ad groups. |
| ↳↳ adgroup_id | string | The ID of the ad group for which the operation failed. |
| ↳↳ error_message | string | Thông báo lỗi chi tiết liên quan đến nhóm quảng cáo thao tác thất bại. |

### Ví dụ lệnh cURL (Example)
#### Đối với cập nhật thành công
```http
// Success-Response
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "adgroup_list": [
            {
                "adgroup_id": "{{adgroup_id}}",
                "status": "DISABLE"
            },
            {
                "adgroup_id": "{{adgroup_id}}",
                "status": "DISABLE"
            }
        ],
        "error_list": []
    }
}
```

#### Đối với cập nhật thất bại
```http
// Success-Response
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "adgroup_list": [],
        "error_list": [
            {
                "adgroup_id": "{{adgroup_id}}",
                "error_message": "Adgroup does not exist. adgroup_id {{adgroup_id}}."
            }
        ]
    }
}
```

---

<a id="doc-1843314914438466"></a>
<!-- doc_id: 1843314914438466 -->
<!-- doc_id: 1843314914438466 -->
# Cập nhật ngân sách của nhóm quảng cáo Smart+ nâng cấp (Update the budgets of Upgraded Smart+ Ad Groups)
> Đường dẫn: API Reference > Smart+ nâng cấp > Nhóm quảng cáo > Cập nhật ngân sách của nhóm quảng cáo Smart+ nâng cấp
Sử dụng endpoint này để cập nhật ngân sách của các nhóm quảng cáo Smart+ nâng cấp.

### Yêu cầu gọi API (Request)
**Endpoint** https://business-api.tiktok.com/open_api/v1.3/smart_plus/adgroup/budget/update/

**Method** POST

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type  ****(Bắt buộc)**** | string | Định dạng dữ liệu yêu cầu. ⏎ Allowed value: `application/json`. |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id  ****(Bắt buộc)**** | string | ID tài khoản quảng cáo TikTok. |
| budget**(Điều kiện)** | object[] | Either `budget` or `scheduled_budget` has to be set. • To update the budgets of one or more ad groups, specify `budget`. • To set a scheduled budget change to the budgets of one or more ad groups, specify `scheduled_budget`. ⏎ Information about the new budgets that you want to set for one or more ad groups. ⏎ Kích thước tối đa: 20. ⏎ **Note**: The changes to the budgets of one or more ad groups will take effect immediately. |
| ↳ adgroup_id **(Điều kiện)** | string | Bắt buộc khi the object array `budget` is specified. ⏎ ID nhóm quảng cáo. ⏎ Để lấy ID nhóm quảng cáo, sử dụng [/smart_plus/adgroup/get/](62-upgraded-smartplus-p2.md#doc-1843314879617026). |
| ↳ budget **(Điều kiện)** | float | Bắt buộc khi the object array `budget` is specified. ⏎ The new budget for the ad group (`adgroup_id`). |
| scheduled_budget **(Điều kiện)** | object[] | Either `budget` or `scheduled_budget` has to be set. • To update the budgets of one or more ad groups, specify `budget`. • To set a scheduled budget change to the budgets of one or more ad groups, specify `scheduled_budget`. ⏎ Information about a list of scheduled budget adjustments for one or more ad groups. ⏎ Kích thước tối đa: 20. ⏎ **Note**: • Configuring scheduled budget changes for your Upgraded Smart+ Ad Groups is currently an allowlist-only feature. If you would like to access it, please contact your TikTok representative. • The scheduled budget changes will take effect from 00:00 a.m. the following day in the ad account's time zone. |
| ↳ adgroup_id **(Điều kiện)** | string | Bắt buộc khi the object array `scheduled_budget` is specified. ⏎ ID nhóm quảng cáo. ⏎ **Note**: • If the ad group (`adgroup_id`) is part of a CBO campaign (where `budget_optimize_on` is`true`), a `min_budget` or `max_budget` or both must be configured. • No prerequisites apply for ad groups within non-CBO campaigns (where `budget_optimize_on` is `false`). |
| ↳ scheduled_budget **(Điều kiện)** | float | Bắt buộc khi the object array `scheduled_budget` is specified. ⏎ The maximum budget control or the new budget for the ad group (`adgroup_id`). ⏎ • For an ad group in a CBO campaign (where `budget_optimize_on` is `true`), a `min_budget` or `max_budget` or both must be configured. This field will set the maximum daily budget control for the ad group. • For an ad group in a non-CBO campaign (where `budget_optimize_on` is `false`), this field sets the new dynamic daily budget for the ad group, with no prerequisites. |

#### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/smart_plus/adgroup/budget/update/' \
--header 'Access-Token: "{{Access-Token}}"' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id": "{{advertiser_id}}",
    "budget": [
        {
            "adgroup_id":"{{adgroup_id}}",
            "budget": "{{budget}}"
        },
        {
            "adgroup_id":"{{adgroup_id}}",
            "budget": "{{budget}}"
        }
    ]
}'
```

### Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Mã phản hồi. Để xem danh sách đầy đủ các mã phản hồi và mô tả, xem [Phụ lục - Mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | ID nhật ký (log ID) của yêu cầu, dùng để định danh duy nhất yêu cầu. |
| data | object | Dữ liệu trả về. |

#### Ví dụ lệnh cURL (Example)
```http
// Success-Response
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {}
}
```

---

<a id="doc-1843310530260097"></a>
<!-- doc_id: 1843310530260097 -->
<!-- doc_id: 1843310530260097 -->
# Quảng cáo (Ads)
> Đường dẫn: API Reference > Smart+ nâng cấp > Quảng cáo
Quảng cáo là đơn vị quảng cáo nhỏ nhất và là nội dung hiển thị trực tiếp đến đối tượng mục tiêu.

Nhóm này bao gồm các endpoint sau:
* [Lấy danh sách quảng cáo Smart+ nâng cấp](62-upgraded-smartplus-p4.md#doc-1843317378982914)
* [Tạo quảng cáo Smart+ nâng cấp](62-upgraded-smartplus-p5.md#doc-1843317390059522)
* [Cập nhật quảng cáo Smart+ nâng cấp](62-upgraded-smartplus-p6.md#doc-1843317411665921)
* [Cập nhật trạng thái hoạt động của quảng cáo Smart+ nâng cấp](62-upgraded-smartplus-p6.md#doc-1843317423164482)
* [Bật hoặc tắt mẫu quảng cáo trong quảng cáo Smart+ nâng cấp](62-upgraded-smartplus-p6.md#doc-1843317433577601)
* [Xem trước quảng cáo Smart+ nâng cấp](62-upgraded-smartplus-p6.md#doc-1843317445798914)

---

<a id="doc-1843317378982914"></a>
<!-- doc_id: 1843317378982914 -->
<!-- doc_id: 1843317378982914 -->
# Lấy danh sách quảng cáo Smart+ nâng cấp (Get Upgraded Smart+ Ads)
> Đường dẫn: API Reference > Smart+ nâng cấp > Quảng cáo > Get Upgraded Smart+ Ads
Sử dụng endpoint này để truy xuất danh sách quảng cáo Smart+ nâng cấp trong tài khoản quảng cáo. 

> **Important:** 
> This endpoint only returns creatives that you have explicitly selected. Automatically added creatives are not included in the response.
> Excluded creatives include:
> - TikTok creator content, creator content from TikTok One, Content Suite, and authorized TikTok post
> - Your own content, content you've previously used from your linked TikTok accounts and Creative Library
> - Content generated for you, such as remixing images from your app store page
> 
> To retrieve all creatives in a campaign, including those added automatically, use [/ad/get/](02-ads-p1.md#doc-1735735588640770). 

## Yêu cầu gọi API (Request)
**Endpoint** https://business-api.tiktok.com/open_api/v1.3/smart_plus/ad/get/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id   ****(Bắt buộc)**** | string | ID tài khoản quảng cáo TikTok. |
| fields | string[] | Fields that you want to get. ⏎ When not specified, all fields are returned by default. ⏎ For allowed fields, see the fields under `list` and fields under `ad_configuration` in the Response section excluding `advertiser_id` and `smart_plus_ad_id`, which are returned by default. |
| include_effective_status | boolean | Có thực hiện include the parameter `effective_status` in the response. ⏎ Các giá trị được hỗ trợ: `true`, `false`. ⏎ Giá trị mặc định: `false`. |
| filtering | object | Điều kiện lọc dữ liệu. ⏎ Example: `filtering={"objective_type":"APP_PROMOTION"}` |
| ↳ campaign_ids | string[] | Lọc theo danh sách ID chiến dịch. ⏎ Kích thước tối đa: 100. ⏎ To obtain campaign IDs, use [/smart_plus/campaign/get/](62-upgraded-smartplus-p1.md#doc-1843312818332930). |
| ↳ adgroup_ids | string[] | Danh sách các ID nhóm quảng cáo. ⏎ Kích thước tối đa: 100. ⏎ Để lấy ID nhóm quảng cáo, sử dụng [/smart_plus/adgroup/get/](62-upgraded-smartplus-p2.md#doc-1843314879617026). |
| ↳ smart_plus_ad_ids | string[] | A list of Ad IDs. ⏎ Kích thước tối đa: 100. |
| ↳ effective_statuses | string[] | Filter by a list of ad statuses. ⏎ Các giá trị enum hỗ trợ: • `UNDER_REVIEW`: Under review. • `NOT_DELIVERED`: Not delivered. • `SCHEDULED`: Scheduled. • `PARTIAL_DELIVERY`: Partial delivery. • `ACTIVE`: Active. • `ENDED`: Ended. • `PAUSED`: Paused. • `DELETED`: Deleted. |
| ↳ primary_status | string | Primary status. ⏎ Để xem danh sách giá trị enum, xem [Enumeration-Primary Status](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ secondary_status | string | Filter by ad secondary status. ⏎ Để xem danh sách giá trị enum, xem [Enumeration- Ad Status - Secondary Status](../15-appendix/phu-luc-p1.md#doc-1737174886619138). ⏎ The following secondary statuses are newly added for Upgraded Smart+ Ads: • `AD_STATUS_DELIVERY_AND_REAUDIT`: Review of modifications in progress. • `AD_STATUS_DELIVERY_AND_TRANSCODING_FAIL`: Transcoding of the video or videos in the ad failed. • `AD_STATUS_REVIEW_PARTIALLY_APPROVED`: Ad in partial review and in delivery. • `AD_STATUS_COLLECTION_TOGGLED_OFF`: Lead collection has ended. • `AD_STATUS_PRIVACY_POLICY_REJECTED`: Ad rejected due to privacy policy violations. • `AD_STATUS_PRIVACY_POLICY_AUDIT`: Ad in review for privacy policy compliance. |
| ↳ objective_type | string | Filter by advertising objective. ⏎ Currently, we support `APP_PROMOTION`, `WEB_CONVERSIONS`, and `LEAD_GENERATION`. ⏎ For detailed explanation of enum values, see [Enumeration-Advertising Objectives](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ sales_destination | string | Sales destination, the destination where you want to drive your sales. ⏎ Các giá trị enum hỗ trợ: • `WEBSITE`: Website. Drive sales on your website. • `APP`: App. Drive sales on your app (product catalog required). • `WEB_AND_APP`: Website and app. Drive sales on both your website and your app. |
| ↳ optimization_goal | string | Optimization goal. ⏎ To find the enum values, see [Enumeration - Optimization Goal](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ creation_filter_start_time | string | The earliest ad Thời gian tạo, in the format of `YYYY-MM-DD HH:MM:SS` (UTC time). This filter will retrieve ads created after this time. ⏎ Example: `2025-01-01 00:00:01`. ⏎ If `creation_filter_start_time` and `creation_filter_end_time` are not specified, the results will include ads created at any time. ⏎ **Important**: To ensure task efficiency and speed, consider setting a time range within six months for the Thời gian tạo filters. |
| ↳ creation_filter_end_time | string | The latest ad Thời gian tạo, in the format of `YYYY-MM-DD HH:MM:SS` (UTC time). This filter will retrieve ads created before this time. ⏎ Example: `2025-02-01 00:00:01`. ⏎ If `creation_filter_start_time` and `creation_filter_end_time` are not specified, the results will include ads created at any time. ⏎ **Important**: To ensure task efficiency and speed, consider setting a time range within six months for the Thời gian tạo filters. |
| ↳ modified_after | string | The latest ad modification time, in the format of `YYYY-MM-DD HH:MM:SS` (UTC time). This filter will retrieve ads last modified after this time. ⏎ **Important**: To ensure task efficiency and speed, consider setting a time range within six months for the Thời gian tạo filters. |
| page | number | Current Số trang cần lấy dữ liệu. ⏎ Value range: ≥ 1. ⏎ Giá trị mặc định: 1. |
| page_size | number | Page size. ⏎ Value range: 1-100. ⏎ Giá trị mặc định: 10. |

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location  --request GET 'https://business-api.tiktok.com/open_api/v1.3/smart_plus/ad/get/?advertiser_id={{advertiser_id}}&page=1&page_size=100' \
--header 'Access-Token: {{Access-Token}}'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| - | - | - |
| code | number | Mã phản hồi. Để xem danh sách đầy đủ các mã phản hồi và mô tả, xem [Phụ lục - Mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | ID nhật ký (log ID) của yêu cầu, dùng để định danh duy nhất yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ list | object[] | A list of ads. The returned fields are generated based on the `fields` specified in the request parameters. If not specified, all fields are returned by default. |
| ↳↳ advertiser_id | string | ID tài khoản quảng cáo TikTok. |
| ↳↳ campaign_id | string | ID chiến dịch quảng cáo. |
| ↳↳ campaign_name | string | Campaign name. |
| ↳↳ adgroup_id | string | ID nhóm quảng cáo. |
| ↳↳ adgroup_name | string | Ad group name. |
| ↳↳ smart_plus_ad_id | string | ID mẫu quảng cáo. |
| ↳↳ ad_name | string | Ad name. |
| ↳↳ operation_status | string | Trạng thái hoạt động. ⏎ Các giá trị enum hỗ trợ: • `ENABLE` : The ad is enabled (in 'ON' status). • `DISABLE`: The ad is disabled (in 'OFF' status). • `FROZEN`: The ad is terminated and cannot be enabled. |
| ↳↳ effective_status | string | Returned only when `effective_status` is `true` in the request. ⏎ The effective status of the ad. ⏎ Các giá trị enum hỗ trợ: • `UNDER_REVIEW`: Under review. • `NOT_DELIVERED`: Not delivered. • `SCHEDULED`: Scheduled. • `PARTIAL_DELIVERY`: Partial delivery. • `ACTIVE`: Active. • `ENDED`: Ended. • `PAUSED`: Paused. • `DELETED`: Deleted. |
| ↳↳ secondary_status | string | Ad secondary status. ⏎ Để xem danh sách giá trị enum, xem [Enumeration-Ad Status - Secondary Status](../15-appendix/phu-luc-p1.md#doc-1737174886619138). ⏎ The following secondary statuses are newly added for Upgraded Smart+ Ads: • `AD_STATUS_DELIVERY_AND_REAUDIT`: Review of modifications in progress. • `AD_STATUS_DELIVERY_AND_TRANSCODING_FAIL`: Transcoding of the video or videos in the ad failed. • `AD_STATUS_REVIEW_PARTIALLY_APPROVED`: Ad in partial review and in delivery. • `AD_STATUS_COLLECTION_TOGGLED_OFF`: Lead collection has ended. • `AD_STATUS_PRIVACY_POLICY_REJECTED`: Ad rejected due to privacy policy violations. • `AD_STATUS_PRIVACY_POLICY_AUDIT`: Ad in review for privacy policy compliance. |
| ↳↳ create_time | string | The time when the ad was created, in the format of `YYYY-MM-DD HH:MM:SS` (UTC+0). ⏎ Example: `2025-01-01 00:00:01`. |
| ↳↳ modify_time | string | The time when the ad was last modified, in the format of `YYYY-MM-DD HH:MM:SS` (UTC+0). ⏎ Example: `2025-01-01 00:00:01`. |
| ↳↳ creative_list | object[] | Danh sách các mẫu quảng cáo (creatives). ⏎ **Important**: This field only returns creatives that you have explicitly selected. Automatically added creatives are not included in the response. Excluded creatives include: • TikTok creator content, creator content from TikTok One, Content Suite, and authorized TikTok post • Your own content, content you've previously used from your linked TikTok accounts and Creative Library • Content generated for you, such as remixing images from your app store pageTo retrieve all creatives in a campaign, including those added automatically, use [/ad/get/](02-ads-p1.md#doc-1735735588640770). |
| ↳↳↳ ad_material_id | string | An ad-specific material ID generated when a particular creative is used in an ad. ⏎ This ID differs from the creative ID you receive when uploading the creative to your ad account’s Creative Library. |
| ↳↳↳ smart_plus_creative_id | string | The ID of the creative in the Upgraded Smart+ Ad. ⏎ This ID is the same as the creative ID you retrieve in the following scenarios: • The `ad_id` you receive from [/ad/get/](02-ads-p1.md#doc-1735735588640770) when you do not specify the `ad_ids_v2` filter. • The `ad_id` metric you retrieve from [/report/integrated/get/](58-reporting.md#doc-1740302848100353) when you set `data_level` to `AUCTION_AD` and include `ad_id` in `dimensions`. |
| ↳↳↳ material_operation_status | string | The status of the creative. ⏎ Các giá trị enum hỗ trợ: • `ENABLE`: The creative is enabled (in 'ON' status). • `DISABLE`: The creative is disabled (in 'OFF' status). |
| ↳↳↳ creative_info | object | Creative information. |
| ↳↳↳↳ ad_format | string | The ad format. ⏎ Các giá trị enum hỗ trợ: • `SINGLE_VIDEO`: Single Video. • `CAROUSEL_ADS`: Standard Carousel. • `CATALOG_CAROUSEL`: Catalog Carousel. |
| ↳↳↳↳ material_name | string | Material name. |
| ↳↳↳↳ video_info | object | Video information. |
| ↳↳↳↳↳ video_id | string | Video ID. |
| ↳↳↳↳↳ file_name | string | Video name. |
| ↳↳↳↳ thumbnail_mode | string | The mode of the video thumbnail. ⏎ The thumbnail will be shown as the first image on a search results page. Thumbnails are critical for catching your audience's attention and driving clicks. ⏎ Các giá trị enum hỗ trợ: • `AUTOMATIC`: Smart thumbnail. The system will show a different frame from your video customized for different audiences to closely match what they're searching for and what they're most likely to tap. The video cover specified through `image_info` will be used as the fallback video thumbnail if no matching thumbnails are found. • `MANUAL`: Manual thumbnail. The video cover specified through `image_info` will be used as the video thumbnail. |
| ↳↳↳↳ image_info | object[] | Image information. |
| ↳↳↳↳↳ web_uri | string | Image ID. |
| ↳↳↳↳ music_info | object | Music information. |
| ↳↳↳↳↳ music_id | string | The ID of the piece of music to use in the Carousel Ads. |
| ↳↳↳↳ aigc_disclosure_type | string | Có thực hiện turn on the AIGC (Artificial Intelligence Generated Content) self-disclosure toggle to indicate the ad contains AI-generated content. After the toggle is turned on, your ad will carry an "Advertiser labeled as Al-generated" label when viewed in full. ⏎ Các giá trị enum hỗ trợ: • `SELF_DISCLOSURE`: To turn on the toggle to declare that the ad contains AI-generated content. • `NOT_DECLARED`: To not declare that the ad contains AI-generated content. |
| ↳↳↳↳ tiktok_item_id | string | The ID of the TikTok post to be used as an ad (Spark Ads). |
| ↳↳↳↳ identity_type | string | Returned for Spark Ads created without using catalog creatives. ⏎ Identity type. ⏎ Các giá trị enum hỗ trợ: `AUTH_CODE`, `TT_USER`, `BC_AUTH_TT`. ⏎ For details about identities, see [Identities](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1738958351620097). |
| ↳↳↳↳ identity_id | string | Returned for Spark Ads created without using catalog creatives. ⏎ Identity ID. |
| ↳↳↳↳ identity_authorized_bc_id | string | Returned when `identity_type` within `creative_info` is `BC_AUTH_TT`. ⏎ The ID of the Business Center that a TikTok Account User in Business Center identity is associated with. |
| ↳↳ playable_list | object[] | A list of playables. |
| ↳↳↳ playable_url | string | The URL of the playable. |
| ↳↳ ad_text_list | object[] | A list of ad texts. ⏎ Ad texts are shown to your audience as part of your ad creatives, to deliver the message you intend to communicate to them. |
| ↳↳↳ ad_text | string | Ad text. |
| ↳↳ auto_message_list | object[] | Returned only when `promotion_type` is `LEAD_GEN_CLICK_TO_TT_DIRECT_MESSAGE` at the ad group level. ⏎ Details of the automatic message to use in a TikTok Direct Messaging Ad. |
| ↳↳↳ auto_message_id | string | The ID of the automatic message to use in a TikTok Direct Messaging Ad. ⏎ Currently, the only supported automatic message type is welcome message. • To obtain a list of welcome messages within your ad account, use [/creative/auto_message/get/](73-welcome-messages.md#doc-1822106498804738). • To create a welcome message within your ad account, use [/creative/auto_message/create/](73-welcome-messages.md#doc-1822106113771521). ⏎ To learn more about how to create TikTok Direct Messaging Ads with welcome messages, see [Create an Upgraded Smart+ Lead Generation Campaign with optimization location as TikTok direct messages](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1847302969710913). |
| ↳↳ call_to_action_list | object[] | Call-to-action list. |
| ↳↳↳ call_to_action | string | Call-to-action text. ⏎ Để xem danh sách giá trị enum, xem [Enumeration - Call-to-action](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳↳ interactive_add_on_list | object[] | A list of interactive add-on (creative portfolio) IDs. |
| ↳↳↳ card_id | string | The ID of an interactive add-on. |
| ↳↳ page_list | object[] | A list of pages. |
| ↳↳↳ page_id | string | Page ID. |
| ↳↳ landing_page_url_list | object[] | A list of landing page URLs. |
| ↳↳↳ landing_page_url | string | Landing page URL. |
| ↳↳ custom_product_page_list | object[] | Details of the custom product page to use in the ad. |
| ↳↳↳ custom_product_page_url | string | The Custom Product Page (CPP) URL. ⏎ CPPs are product pages with customized screenshots, promotional text, and app previews that can be used to highlight specific content or features of the promoted app, or reach specific audiences. ⏎ Example: `https://apps.apple.com/us/app/tiktok/id835599320?ppid=12345a6b-c789-12d3-e4f5-g6h78i91jk2l`. |
| ↳↳ deeplink_list | object[] | A list of deeplinks. |
| ↳↳↳ deeplink | string | Deeplink, the specific location where you want your audience to go if they have your app installed. |
| ↳↳↳ deeplink_type | string | The deeplink type. ⏎ Các giá trị enum hỗ trợ: • `NORMAL`: non-deferred deeplink. • `DEFERRED_DEEPLINK`: deferred deeplink. |
| ↳↳ multi_dest_list | object[] | Returned only when `promotion_type` is `LEAD_GENERATION_MULTI_DESTINATION` is specified at the ad group level. ⏎ A list of destinations for the Lead Generation ad. |
| ↳↳↳ dest_type | string | Destination type. ⏎ Các giá trị enum hỗ trợ: • `EXTERNAL_WEBSITE`: Website URL. You need to specify `landing_page_url` simultaneously. • `INSTANT_PAGE`: Instant Form. You need to specify `page_id` simultaneously. • `TT_DIRECT_MESSAGAE`: Message template. You need to specify `auto_message_id` simultaneously. |
| ↳↳↳ landing_page_url | string | Returned when `dest_type` is `EXTERNAL_WEBSITE`. ⏎ Landing page URL. |
| ↳↳↳ page_id | string | Returned when `dest_type` is `INSTANT_PAGE`. ⏎ The ID of an Instant Form. |
| ↳↳↳ auto_message_id | string | Returned when `dest_type` is `TT_DIRECT_MESSAGAE`. ⏎ The ID of the automatic message to use in a TikTok Direct Messaging Ad. |
| ↳↳ disclaimer | object | Disclaimer information. |
| ↳↳↳ disclaimer_type | string | The type of disclaimer in the ad. ⏎ Các giá trị enum hỗ trợ: • `TEXT_LINK`: clickable disclaimers. • `TEXT_ONLY`: text-only disclaimers. |
| ↳↳↳ disclaimer_text | object | The text-only disclaimer in the ad. |
| ↳↳↳↳ text | string | The disclaimer text. |
| ↳↳↳ disclaimer_clickable_texts | object[] | The clickable disclaimer or clickable disclaimers in the ad. |
| ↳↳↳↳ text | string | The disclaimer text. |
| ↳↳↳↳ url | string | The URL for the clickable disclaimer. ⏎ When users tap each text, they will be redirected to the URL and see more disclaimer details. |
| ↳↳ ad_configuration | object | Additional configurations. |
| ↳↳↳ identity_type | string | Returned in any of the following scenarios: • For non-Spark Ads on non-TikTok placements. Non-Spark Ads on the TikTok placement are no longer supported. • For Spark Ads created using catalog creatives. ⏎ Identity type. • Enum values for non-Spark Ads on non-TikTok placements: `CUSTOMIZED_USER`. • Enum values for Upgraded Smart+ Catalog Spark Ads (with `catalog_creative_toggle` as `true`): `TT_USER`, `BC_AUTH_TT`. ⏎ For details about identities, see [Identities](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1738958351620097). |
| ↳↳↳ identity_id | string | Returned in any of the following scenarios: • For non-Spark Ads on non-TikTok placements. Non-Spark Ads on the TikTok placement are no longer supported. • For Spark Ads created using catalog creatives. ⏎ Identity ID. |
| ↳↳↳ identity_authorized_bc_id | string | Returned when `identity_type` within `ad_configuration` is `BC_AUTH_TT`. ⏎ ID of the Business Center that a TikTok Account User in Business Center identity is associated with. |
| ↳↳↳ dark_post_status | string | The status of the "Ads-only mode" for your creatives. ⏎ Các giá trị enum hỗ trợ: • `ON`: Enable the ads-only mode to limit your posts to paid traffic. • `OFF`: Disable the ads-only mode. The post will appear on your TikTok profile and will be eligible to receive organic traffic. |
| ↳↳↳ product_specific_type | string | Different dimensions to choose products. ⏎ Các giá trị enum hỗ trợ: • `ALL`: Allow TikTok to dynamically choose from all products. • `PRODUCT_SET`: Specify a product set. TikTok will dynamically choose products from this set. • `CUSTOMIZED_PRODUCTS`: Specify a customized number of products. • `UNSET`: Unset. |
| ↳↳↳ product_set_id | string | The ID of a product set. |
| ↳↳↳ product_ids | string[] | The product IDs of catalog products. |
| ↳↳↳ catalog_creative_toggle | boolean | Có thực hiện enable auto-selection of creatives from your catalog. ⏎ Các giá trị được hỗ trợ: `true`, `false`. |
| ↳↳↳ catalog_creative_info | object | Additional settings for catalog creatives to use in your ads. |
| ↳↳↳↳ catalog_media_settings | string[] | The types of creatives from your E-commerce, entertainment, generic, or online-to-offline catalog to use in the ad. ⏎ Các giá trị enum hỗ trợ: • `VIDEO`: Video. • `IMAGE`: Image. • `TEMPLATE_VIDEO`: Video templates. • `TEMPLATE_VIDEO`: Video templates.  • `MULTI_SHOW`: Multi-Show. Multi-Show Experience is an auto-play video carousel experience designed to drive user exploration and engagement across a breadth of personally-relevant title offerings within your content library. Multi-Show Experience consists of 4 video tiles delivered from your catalog. Each tile's clip plays sequentially (starting in the upper left-hand corner), and offers you the ability to assign a corresponding title-specific landing page. ⏎ The availability of the enum values varies by ad type. Refer to the [Upgraded Smart+ Campaign Use Case Guide](https://business-api.tiktok.com/portal/docs/create-an-upgraded-smart+-campaign-use-case/v1.3#anchor-3) to see the exact supported values for your scenario. |
| ↳↳↳↳ catalog_template_video_id | string | The ID of a video template in your catalog to use in the ad. |
| ↳↳↳ creative_auto_add_toggle | boolean | Có thực hiện auto-add newly generated assets during delivery. ⏎ During your campaign, the system will generate new creative assets from your existing campaign assets and creative library. By using TikTok's latest trending elements (hooks, music, text, and more), you'll get high-quality, ready-to-use content that delivers alongside your other selected assets. ⏎ New assets will be added to your campaign automatically and won't appear on your TikTok profile. You can turn off this feature anytime. ⏎ Các giá trị được hỗ trợ: `true`, `false`. |
| ↳↳↳ creative_auto_enhancement_strategy_list | string[] | The list of automatic enhancement strategies to apply to your ads. ⏎ Automatic enhancements are real-time edits applied to your ads during your campaign. They can improve performance by creating more engaging and impactful visuals, sound, and more. ⏎ Các giá trị enum hỗ trợ: • `TRANSLATE_AND_DUB`: Translate and dub. Connect with global audiences by delivering your ad in 50+ languages. • `MUSIC_REFRESH`: Music refresh. Stay on-trend by swapping in music currently popular on TikTok. • `VIDEO_QUALITY`: Video quality. Improve overall visual quality with increased resolution and clarity. • `IMAGE_QUALITY`: Image quality. Improve overall visual quality with increased resolution and clarity. • `IMAGE_RESIZE`: Resize. Resize your image to take advantage of full-screen capabilities. • `CALL_TO_ACTION_ENHANCEMENT`: CTA enhancement. Tailor and optimize your call to action based on specific use cases to enhance performance. • `AIGC_CARD`: Generate ad card. Increase engagement by showcasing key messages and visuals designed to drive clicks and conversions. ⏎ **Note**: Currently, you cannot enable the strategies `CALL_TO_ACTION_ENHANCEMENT` and `AIGC_CARD` through `creative_auto_enhancement_strategy_list` via API. |
| ↳↳↳ deeplink_utm_params | object[] | A list of deeplink URL parameters. URL parameters are snippets of code that can be added to the end of the URLs to help you track clicks across different channels and understand how visitors interact with a website through third-party analytics platforms. They consist of key-value pairs that are specified through `key` and `value`. |
| ↳↳↳↳ key | string | Tham số URL liên kết sâu. ⏎ Có thể là tham số tùy chỉnh hoặc tham số UTM. ⏎ The supported UTM parameters are: • `utm_source`: The app, site, etc., that brings traffic to your website. For example: TikTok. • `utm_medium`: The advertising or marketing medium. For example: cpm, cpc, banner, video. • `utm_content`: The creative content used for promotion. For example: ad name, CTA text, asset, color, etc. • `utm_campaign`: The individual campaign name, slogan, or promo code. For example: BlackFridayProm. |
| ↳↳↳↳ value | string | The value of the deeplink URL parameter. ⏎ It can be a custom value or the name of a macro. ⏎ The supported macros are: • `__CAMPAIGN_NAME__`: This will be replaced by your campaign name. • `__CAMPAIGN_ID__`: This will be replaced by your ID chiến dịch quảng cáo. • `__AID_NAME__`: This will be replaced by your ad group name. • `__AID__`: This will be replaced by your ID nhóm quảng cáo. • `__CID_NAME__`: This will be replaced by your ad name. • `__CID__`: This will be replaced by your ID mẫu quảng cáo. • `__PLACEMENT__`: This will be replaced by your placement. |
| ↳↳↳ end_card_cta | string | Call-to-action for the end card (`image_ids`) of an Upgraded Smart+ [Automotive Carousel Ad for Inventory](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1843325008693250) or [Automotive Carousel Ad for Models](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1843325022799873), or [the catalog solution for Upgraded Smart+ TikTok Direct Messaging Ads](https://business-api.tiktok.com/portal/docs/create-an-upgraded-smart-lead-generation-campaign-with-optimization-location-as-tiktok-direct-messages/v1.3#anchor-2-2). ⏎ Các giá trị enum hỗ trợ: • `SEARCH_INVENTORY` (Recommended): Search inventory. • `LEARN_MORE`: Learn more. • `SHOP_NOW`: Shop now. • `SIGN_UP`: Sign up. • `CONTACT_US`: Contact us. • `BOOK_NOW`: Book now. • `READ_MORE`: Read more. • `VIEW_MORE`: View now. • `ORDER_NOW`: Order now. • `SEND_MESSAGE`: Send message. • This value is only available for [the catalog solution for Upgraded Smart+ TikTok Direct Messaging Ads](https://business-api.tiktok.com/portal/docs/create-an-upgraded-smart-lead-generation-campaign-with-optimization-location-as-tiktok-direct-messages/v1.3#anchor-2-2). |
| ↳↳↳ product_display_field_list | string[] | A list of product details to display in your [Automotive Carousel Ad for Inventory](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1843325008693250) or [Upgraded Smart+ Lead Generic Catalog Ads](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1874421377372161). ⏎ Enum values for Automotive Carousel Ad for Inventory: • `DEALER_NAME`: the `dealer_name` field of vehicles. • `MAKE`: the `make` field of vehicles. • `MODEL`: the `model` field of vehicles. • `YEAR`: the `year` field of vehicles. • `MILEAGE`: the `mileage` field of vehicles. • `PRICE`: the `price` field of vehicles. • `SALE_PRICE`: the `sale_price` field of vehicles. • `EXTERIOR_COLOR`: the `exterior_color` field of vehicles. • `TRIM`: the `trim` field of vehicles. • `ADDRESS_CITY`: the `city` field of vehicles. • `VEHICLE_STATE`: the `state_of_vehicle` field of vehicles. ⏎ Enum values for Upgraded Smart+ Lead Generic Catalog Ads: • `RATING`: the `rating` field of generic products or services. • `SALE_PRICE`: the `sale_price` field of generic products or services. • `PRICE`: the `price` field of generic products or services. • `DESCRIPTION`: the `description` field of generic products or services. • `ADDRESS_CITY`: the `address.city` field of generic products or services. • `ADDRESS_REGION`: the `address.region` field of generic products or services. • `ADDRESS_STREET`: the `address.street` field of generic products or services. • `CUSTOM_LABEL_0`: the `custom_label_0` field of generic products or services. • `CUSTOM_LABEL_1`: the `custom_label_1` field of generic products or services. • `CUSTOM_LABEL_2`: the `custom_label_2` field of generic products or services. ⏎ The title of each vehicle, product, or service is displayed automatically. For instance, if you set this field to `["MILEAGE","YEAR"]`, the ad will display the `mileage`, `price` and `title` fields of each vehicle. ⏎ To retrieve the product detail fields of your vehicles in an Auto-Inventory catalog or that of your products or services in a generic catalog and check Liệu you need to update the details, use [/catalog/product/get/](28-catalog-products-p2.md#doc-1740564136678402). |
| ↳↳↳ auto_disclaimer_types | string[] | The type of disclaimer to show in the [Automotive Carousel Ad for Models](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1843325022799873). ⏎ Các giá trị enum hỗ trợ: • `EMISSION`: Emission disclaimer. • `DISCOUNT`: Discount or offer disclaimer. |
| ↳↳↳ utm_params | object[] | A list of URL parameters. ⏎ URL parameters are snippets of code that can be added to the end of the URLs to help you track clicks across different channels and understand how visitors interact with a website through third-party analytics platforms. They consist of key-value pairs that are specified through `key` and `value`. |
| ↳↳↳↳ key | string | Tham số URL. ⏎ Tham số có thể là tham số tùy chỉnh hoặc tham số UTM. ⏎ The supported UTM parameters are: • `utm_source`: The app, site, etc., that brings traffic to your website. For example: TikTok. • `utm_medium`: The advertising or marketing medium. For example: cpm, cpc, banner, video. • `utm_content`: The creative content used for promotion. For example: ad name, CTA text, asset, color, etc. • `utm_campaign`: The individual campaign name, slogan, or promo code. For example: BlackFridayProm.Note that UTM parameters are case-sensitive. |
| ↳↳↳↳ value | string | The value of the URL parameter. ⏎ The value can be a custom value or the name of a macro. ⏎ The supported macros are: • `__CAMPAIGN_NAME__`: This will be replaced by your campaign name. • `__CAMPAIGN_ID__`: This will be replaced by your ID chiến dịch quảng cáo. • `__AID_NAME__`: This will be replaced by your ad group name. • `__AID__`: This will be replaced by your ID nhóm quảng cáo. • `__CID_NAME__`: This will be replaced by your ad name. • `__CID__`: This will be replaced by your ID mẫu quảng cáo. • `__PLACEMENT__`: This will be replaced by your placement. |
| ↳↳↳ fallback_type | string | Fallback type. ⏎ The destination when the user is unable to access the deeplink because the app has not been installed. ⏎ Các giá trị enum hỗ trợ: • `WEBSITE`: The promoted web page as fallback URL. You need to simultaneously specify the fallback URL through `landing_page_url_list`. • `APP_INSTALL`: The App Store or Google Play page for the promoted App. ⏎ The availability of the enum values varies by ad type. Refer to the [Upgraded Smart+ Campaign Use Case Guide](https://business-api.tiktok.com/portal/docs/create-an-upgraded-smart+-campaign-use-case/v1.3#anchor-3) to see the exact supported values for your scenario. |
| ↳↳↳ product_info | object | Product information. ⏎ This information will be used in different ad variations to create personalized ad delivery with the goal of improving ad performance. Based on past data, ads with complete information often have more clicks and conversions. Results may vary. |
| ↳↳↳↳ product_titles | string[] | Danh sách tên sản phẩm. |
| ↳↳↳↳ product_image_list | object[] | Danh sách hình ảnh sản phẩm. |
| ↳↳↳↳↳ web_uri | string | ID hình ảnh của sản phẩm. |
| ↳↳↳↳ selling_points | string[] | Danh sách các điểm bán hàng nổi bật (selling points). |
| ↳↳↳↳ catalog_tag_list | string[] | Returned in any of the following scenarios: • Scenario 1: At the campaign level `objective_type` is `WEB_CONVERSIONS` and `catalog_type` is `ECOMMERCE`. • Scenario 2:  • At the campaign level, `objective_type` is `LEAD_GENERATION` and `catalog_enabled` is `true`. • At the ad group level, an Auto-Inventory catalog is specified through `catalog_id`. • Scenario 3: • At the campaign level, `objective_type` is `WEB_CONVERSIONS` or `LEAD_GENERATION`, `catalog_enabled` is `true`, and `catalog_type` is `GENERIC`.Details of the product information for catalog ads. • For scenario 1, the specified product information will be automatically displayed from your catalog to drive results. The enum values are: • `PRICE`: Price. • `STRIKETHROUGH_PRICE`: Strikethrough price. • `DISCOUNT`: Discount. • `FREE_SHIPPING`: Free shipping. • For scenario 2, the corresponding text for the specified product information will be displayed on the inventory card. The enum values are: • `DEALER_NAME`: Dealer name. • `CURRENT_MILEAGE`: Current mileage. • `LEAD_PRICE`: Price. • `LEAD_SALE_PRICE`: Sale price. • `EXTERIOR_COLOR`: Exterior color. • `TRIM`: Trim. • `ADDRESS_CITY`: City. • `VEHICLE_STATE`: Vehicle state. • For scenario 3, the enum values are: • `GENERIC_RATING`: Rating. • `GENERIC_SALE_PRICE`: Sale price. • `GENERIC_PRICE`: Price. • `GENERIC_DESCRIPTION`: Product description. • `GENERIC_ADDRESS_CITY`: City. • `GENERIC_ADDRESS_REGION`: Locations or regions. • `GENERIC_ADDRESS_STREET`: Street address. • `GENERIC_CUSTOM_LABEL_0`: Custom label 0. • `GENERIC_CUSTOM_LABEL_1`: Custom label 1. • `GENERIC_CUSTOM_LABEL_2`: Custom label 2. |
| ↳↳↳↳ product_card_type | string[] | The product card display type. ⏎ Các giá trị enum hỗ trợ: • `PRODUCT_CARD`: Product Card. • `PRODUCT_TILE`: Product Tiles. • `PRODUCT_INFO_CARD`: Info Card. • `PRODUCT_SHOWCASE_TILE`: Showcase Tiles. • `ANCHOR`: Anchor. • `CAROUSEL_LABEL`: Carousel label. |
| ↳↳↳↳ promo_info_list | object[] | Returned only for [regular Upgraded Smart+ Web Campaigns](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1847302878676994). ⏎ Details of promo codes and offers. ⏎ Your offer details for promo codes, offers, or events will be highlighted to boost engagement and ad performance. Promo codes require shoppers to enter a code at checkout. Offers apply automatically and no code is needed. |
| ↳↳↳↳↳ discount_type | string | Returned only when `promo_info_list` is specified. ⏎ Loại chiết khấu/giảm giá. ⏎ Các giá trị enum hỗ trợ: • `PERCENTAGE`: Percentage off discount. • `CASH`: Cash off discount. |
| ↳↳↳↳↳ discount_value | float | Returned when `promo_info_list` is specified. ⏎ Giá trị chiết khấu/giảm giá. |
| ↳↳↳↳↳ discount_currency | string | Returned when `discount_type` is `CASH`. ⏎ Loại tiền tệ chiết khấu. ⏎ Để xem danh sách giá trị enum, xem List of values for `discount_currency` or `minimum_purchase_currency`. |
| ↳↳↳↳↳ promo_code | string | The promo code. |
| ↳↳↳↳↳ minimum_purchase_type | string | Minimum purchase type. ⏎ Các giá trị enum hỗ trợ: • `QUANTITY`: Minimum quantity. • `SUBTOTAL`: Minimum subtotal. |
| ↳↳↳↳↳ minimum_purchase_value | float | Returned only when `minimum_purchase_type` is specified. ⏎ Giá trị mua hàng tối thiểu. |
| ↳↳↳↳↳ minimum_purchase_currency | string | Returned only when `minimum_purchase_type` is `SUBTOTAL`. ⏎ Loại tiền tệ cho giá trị mua hàng tối thiểu. ⏎ Để xem danh sách giá trị enum, xem List of values for `discount_currency` or `minimum_purchase_currency`. |
| ↳↳↳↳↳ valid_start_time | string | Thời gian bắt đầu có hiệu lực (UTC+0) của mã khuyến mãi hoặc ưu đãi, theo định dạng `YYYY-MM-DD HH:MM:SS`. |
| ↳↳↳↳↳ valid_end_time | string | Thời gian kết thúc hiệu lực (UTC+0) của mã khuyến mãi hoặc ưu đãi, theo định dạng `YYYY-MM-DD HH:MM:SS`. |
| ↳↳↳ product_info_enabled | string | Chế độ thông tin sản phẩm. ⏎ Các giá trị enum hỗ trợ: • `UNSET`: To disable product information mode. • `NON_CATALOG`: To enable the non-catalog version of product information. • `CATALOG`: To enable the catalog version of product information. |
| ↳↳↳ call_to_action_id | string | ID danh mục lời kêu gọi hành động (CTA portfolio) sử dụng trong quảng cáo của bạn. |
| ↳↳↳ phone_info | object | Returned only when `promotion_type` is set to `LEAD_GEN_CLICK_TO_CALL` at the ad group level. ⏎ Details of the phone number that the ad audience can directly reach out to you (the advertiser) through when they click the call-to-action button within the ad. ⏎ Learn about how to [create an Upgraded Smart+ Lead Generation Campaign with optimization location as phone call](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1847302998941697). |
| ↳↳↳↳ phone_region_code | string | Mã vùng của số điện thoại mà đối tượng mục tiêu có thể nhấp vào quảng cáo để gọi. ⏎ Example: `US`. |
| ↳↳↳↳ phone_region_calling_code | string | Mã quay số quốc gia của số điện thoại mà đối tượng có thể nhấp vào quảng cáo để gọi. ⏎ Example: `+1`. |
| ↳↳↳↳ phone_number | string | Số điện thoại mà đối tượng mục tiêu có thể nhấp vào quảng cáo để gọi. ⏎ Example: `12638282`. |
| ↳↳↳ tracking_info | object | Tracking information. |
| ↳↳↳↳ viewability_postbid_partner | string | Post-bid third-party viewability measurement partner. ⏎ Các giá trị enum hỗ trợ: `DOUBLE_VERIFY`, `IAS`, `ZEFR`. |
| ↳↳↳↳ viewability_vast_url | string | Returned when `viewability_postbid_partner` is `IAS`. ⏎ The wrapped VAST URL used by the post-bid third-party partner to measure viewability. You need to get the URL from the measurement partner IAS. |
| ↳↳↳↳ brand_safety_postbid_partner | string | Post-bid third-party brand safety measurement partner. ⏎ Các giá trị enum hỗ trợ: `DOUBLE_VERIFY`, `IAS`, `ZEFR`. |
| ↳↳↳↳ brand_safety_vast_url | string | Returned when `brand_safety_postbid_partner` is `IAS`. ⏎ The wrapped VAST URL used by the post-bid third-party partner to measure brand safety. You need to get the URL from the measurement partner IAS. |
| ↳↳↳↳ impression_tracking_url | string | Default Impression Tracking URL. |
| ↳↳↳↳ click_tracking_url | string | Click Tracking URL. |
| ↳↳↳↳ tracking_app_id | string | ID của ứng dụng được đo lường. |
| ↳↳↳↳ tracking_pixel_id | string | The ID of the pixel for tracking the actions people take on your website, such as page views, add to cart, purchases, and more. |
| ↳↳↳↳ tracking_offline_event_set_ids | string[] | A list of Offline Event set IDs for tracking customer actions that happen in-person, such as in-store purchases or live event attendance. |
| ↳↳↳↳ tracking_message_event_set_id | string | The ID of the message event set that you want to measure in the Instant Messaging Ad. |
| ↳↳↳↳ app_tracking_info_list | object[] | Chi tiết cài đặt theo dõi của bên thứ ba (Third-party tracking). |
| ↳↳↳↳↳ app_type | string | Returned when `app_tracking_info_list` is specified. ⏎ App type. ⏎ Các giá trị enum hỗ trợ: • `APP_ANDROID`: Android App. • `APP_IOS`: iOS App. |
| ↳↳↳↳↳ app_id | string | Returned when `app_tracking_info_list` is specified. ⏎ The App ID of the App. • When `app_type` is `APP_ANDROID`, this field represents the App ID for an Android App. • When `app_type` is `APP_IOS`, this field represents the App ID for an iOS App. |
| ↳↳↳↳↳ impression_tracking_url | string | URL theo dõi lượt hiển thị (impression tracking URL). • When `app_type` is `APP_ANDROID`, this field represents an impression tracking URL for Android. • When `app_type` is `APP_IOS`, this field represents an impression tracking URL for iOS. |
| ↳↳↳↳↳ click_tracking_url | string | URL theo dõi lượt nhấp (click tracking URL). • When `app_type` is `APP_ANDROID`, this field represents a click tracking URL for Android. • When `app_type` is `APP_IOS`, this field represents a click tracking URL for iOS. |
| ↳ page_info | object | Thông tin phân trang. |
| ↳↳ page | number | Số trang hiện tại cần lấy dữ liệu. |
| ↳↳ page_size | number | Kích thước trang. |
| ↳↳ total_number | number | Tổng số kết quả tìm thấy. |
| ↳↳ total_page | number | Tổng số trang kết quả. |

### Danh sách giá trị cho `discount_currency` hoặc `minimum_purchase_currency`
Bảng sau đây liệt kê các giá trị enum cho `discount_currency` hoặc `minimum_purchase_currency`.

| Giá trị enum cho discount_currency hoặc minimum_purchase_currency | Tiền tệ (Currency) |
|---|---|
| `AED` | UAE Dirham |
| `ARS` | Argentine Peso |
| `AUD` | Australian Dollar |
| `BDT` | Bangladesh Taka |
| `BHD` | Bahraini Dinar |
| `BOB` | Bolivian Boliviano |
| `BRL` | Brazilian Real |
| `BYN` | Belarusian Ruble |
| `CAD` | Canadian Dollar |
| `CHF` | Swiss Franc |
| `CLP` | Chilean Peso |
| `CNY` | Chinese Yuan |
| `COP` | Colombian Peso |
| `CRC` | Costa Rican Colón |
| `CZK` | Czech Republic Koruna |
| `DKK` | Danish Krone |
| `DZD` | Algerian Dinar |
| `EGP` | Egyptian Pound |
| `EUR` | Euro |
| `GBP` | British Pound |
| `GTQ` | Guatemalan Quetzal |
| `HKD` | Hong Kong Dollar |
| `HNL` | Honduran Lempira |
| `HUF` | Hungarian Forint |
| `IDR` | Indonesian Rupiah |
| `ILS` | New Israeli Shekel |
| `INR` | Indian Rupee |
| `IQD` | Iraqi Dinar |
| `ISK` | Icelandic Króna |
| `JOD` | Jordanian Dinar |
| `JPY` | Japanese Yen |
| `KES` | Kenyan Shilling |
| `KHR` | Cambodian Riel |
| `KRW` | South Korean Won |
| `KWD` | Kuwaiti Dinar |
| `KZT` | Tenge |
| `LBP` | Lebanese Pound |
| `LKR` | Sri Lanka Rupee |
| `MAD` | Moroccan Dirham |
| `MOP` | Pataca |
| `MXN` | Mexican Peso |
| `MYR` | Malaysian Ringgit |
| `NGN` | Nigerian Naira |
| `NIO` | Nicaraguan Cordoba |
| `NOK` | Norwegian Krone |
| `NZD` | New Zealand Dollar |
| `OMR` | Rial Omani |
| `PEN` | Peruvian Sol |
| `PHP` | Philippine Piso |
| `PKR` | Pakistan Rupee |
| `PLN` | Polish ZŁOty |
| `PYG` | Paraguayan Guarani |
| `QAR` | Qatari Rial |
| `RON` | Romanian Leu |
| `RSD` | Serbian Dinar |
| `RUB` | Russian Ruble |
| `SAR` | Saudi Riyal |
| `SEK` | Krona |
| `SGD` | Singapore Dollar |
| `THB` | Thai Baht |
| `TRY` | Turkish Lira |
| `TWD` | New Taiwan Dollar |
| `UAH` | Hryvnia |
| `USD` | US Dollar |
| `UYU` | Peso Uruguayo |
| `VEF` | Venezuelan Bolívar |
| `VND` | Vietnamese Dong |
| `ZAR` | South African Rand |

### Ví dụ lệnh cURL (Example)
```http
// curl
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "list": [
            {
                "ad_configuration": {
                    "call_to_action_id": "{{call_to_action_id}}",
                    "catalog_creative_toggle": false,
                    "product_ids": [
                        "{{product_id}}",
                        "{{product_id}}",
                        "{{product_id}}",
                        "{{product_id}}"
                    ],
                    "product_specific_type": "CUSTOMIZED_PRODUCTS"
                },
                "ad_name": "",
                "ad_text_list": [],
                "adgroup_id": "{{adgroup_id}}",
                "adgroup_name": "{{adgroup_name}}",
                "advertiser_id": "{{advertiser_id}}",
                "campaign_id": "{{campaign_id}}",
                "campaign_name": "{{campaign_name}}",
                "create_time": "{{create_time}}",
                "creative_list": [
                    {
                        "ad_material_id": "{{ad_material_id}}",
                        "creative_info": {
                            "ad_format":"SINGLE_VIDEO",
                            "identity_authorized_bc_id": "0",
                            "identity_id": "{{identity_id}}",
                            "identity_type": "TT_USER",
                            "tiktok_item_id": "{{tiktok_item_id}}"
                        },
                        "material_operation_status": "ENABLE"
                    }
                ],
                "landing_page_url_list": [
                    {
                        "landing_page_url": "{{landing_page_url}}"
                    }
                ],
                "modify_time": "{{modify_time}}",
                "operation_status": "ENABLE",
                "secondary_status": "AD_STATUS_DONE",
                "smart_plus_ad_id": "{{smart_plus_ad_id}}"
            },
            {
                "ad_configuration": {
                    "call_to_action_id": "{{call_to_action_id}}",
                    "catalog_creative_toggle": false,
                    "identity_id": "{{identity_id}}",
                    "identity_type": "CUSTOMIZED_USER",
                    "product_set_id": "{{product_set_id}}",
                    "product_specific_type": "PRODUCT_SET",
                    "utm_params": [
                        {
                            "field": "{{field}}",
                            "value": "{{value}}"
                        }
                    ]
                },
                "ad_name": "{{ad_name}}",
                "ad_text_list": [
                    {
                        "ad_text": "{{ad_text}}"
                    },
                    {
                        "ad_text": "{{ad_text}}"
                    },
                    {
                        "ad_text": "{{ad_text}}"
                    },
                    {
                        "ad_text": "{{ad_text}}"
                    },
                    {
                        "ad_text": "{{ad_text}}"
                    }
                ],
                "adgroup_id": "{{adgroup_id}}",
                "adgroup_name": "{{adgroup_name}}",
                "advertiser_id": "{{advertiser_id}}",
                "campaign_id": "{{campaign_id}}",
                "campaign_name": "{{campaign_name}}",
                "create_time": "{{create_time}}",
                "creative_list": [
                    {
                        "ad_material_id": "{{ad_material_id}}",
                        "creative_info": {
                            "ad_format":"SINGLE_VIDEO",
                            "identity_id": "{{identity_id}}",
                            "identity_type": "CUSTOMIZED_USER",
                            "image_info": [
                                {
                                    "web_uri": "{{web_uri}}"
                                }
                            ],
                            "material_name": "",
                            "video_info": {
                                "file_name": "",
                                "video_id": "{{video_id}}"
                            }
                        },
                        "material_operation_status": "ENABLE"
                    }
                ],
                "landing_page_url_list": [
                    {
                        "landing_page_url": "{{landing_page_url}}"
                    }
                ],
                "modify_time": "{{modify_time}}",
                "operation_status": "ENABLE",
                "secondary_status": "AD_STATUS_AUDIT",
                "smart_plus_ad_id": "{{smart_plus_ad_id}}"
            },
            {
                "ad_configuration": {
                    "call_to_action_id": "{{call_to_action_id}}"
                },
                "ad_name": "{{ad_name}}",
                "ad_text_list": [],
                "adgroup_id": "{{adgroup_id}}",
                "adgroup_name": "{{adgroup_name}}",
                "advertiser_id": "{{advertiser_id}}",
                "campaign_id": "{{campaign_id}}",
                "campaign_name": "{{campaign_name}}",
                "create_time": "{{create_time}}",
                "creative_list": [
                    {
                        "ad_material_id": "{{ad_material_id}}",
                        "creative_info": {
                            "ad_format":"SINGLE_VIDEO",
                            "identity_authorized_bc_id": "{{identity_authorized_bc_id}}",
                            "identity_id": "{{identity_id}}",
                            "identity_type": "BC_AUTH_TT",
                            "tiktok_item_id": "{{tiktok_item_id}}"
                        },
                        "material_operation_status": "ENABLE"
                    },
                    {
                        "ad_material_id": "{{ad_material_id}}",
                        "creative_info": {
                            "ad_format":"SINGLE_VIDEO",
                            "identity_authorized_bc_id": "{{identity_authorized_bc_id}}",
                            "identity_id": "{{identity_id}}",
                            "identity_type": "BC_AUTH_TT",
                            "tiktok_item_id": "{{tiktok_item_id}}"
                        },
                        "material_operation_status": "ENABLE"
                    }
                ],
                "interactive_add_on_list": [
                    {
                        "card_id": "{{card_id}}"
                    }
                ],
                "modify_time": "{{modify_time}}",
                "operation_status": "ENABLE",
                "page_list": [
                    {
                        "page_id": "{{page_id}}"
                    }
                ],
                "secondary_status": "AD_STATUS_AUDIT",
                "smart_plus_ad_id": "{{smart_plus_ad_id}}"
            }
        ],
        "page_info": {
            "page": 1,
            "page_size": 100,
            "total_number": 3,
            "total_page": 1
        }
    }
}
```
---

## Hướng dẫn thực hành Data Retrieval (Python & cURL)

Dưới đây là mã nguồn mẫu minh họa quy trình gọi API thực tế cho phân hệ **Smart+ nâng cấp (Upgraded Smart+) — phần 4/7**:

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

