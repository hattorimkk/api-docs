# TikTok One — phần 2/2

> Phân hệ: apiref:TikTok One.
> Tài liệu biên dịch kỹ thuật chi tiết theo chuẩn TikTok Business API v1.3.

---

## Mục lục điều hướng
- [1. Report on TTO Creator Marketplace videos (#doc-1815693573340162)](#doc-1815693573340162)
- [2. Apply for Spark Ads authorization (#doc-1751098904942594)](#doc-1751098904942594)
- [3. Get the authorization status (#doc-1751098935842817)](#doc-1751098935842817)
- [4. Create a webpage anchor (#doc-1826564934723585)](#doc-1826564934723585)
- [5. Get webpage anchors (#doc-1826564965840066)](#doc-1826564965840066)
- [6. Delete a draft anchor (#doc-1826564985760770)](#doc-1826564985760770)
- [7. Join a TTO Creator Marketplace campaign as a creator (#doc-1836584318657537)](#doc-1836584318657537)
- [8. Link a video to a TTO Creator Marketplace campaign as a creator (#doc-1836584551347201)](#doc-1836584551347201)
- [9. Get TTO video linking requests as a creator (#doc-1837247726007298)](#doc-1837247726007298)
- [10. Approve or reject a TTO video linking request as a creator (#doc-1837247744649345)](#doc-1837247744649345)

---

<a id="doc-1815693573340162"></a>
<!-- doc_id: 1815693573340162 -->
<!-- doc_id: 1815693573340162 -->
# Report on TTO Creator Marketplace videos
> Đường dẫn: API Reference > TikTok One > Report on TTO Creator Marketplace videos
Use this endpoint to obtain the reporting data on videos within a TikTok One (TTO) Creator Marketplace campaign. 

>**Note:**  
>   • Reporting data is available from the moment the video is uploaded to TikTok. If a Creator retroactively uses an invite link to tag a video, the reporting data will be backfilled. • For campaigns that are created via API, reporting data will not be accessible through [the TTO Creator Marketplace platform](https://ads.tiktok.com/creative/creatormarketplace).

## Comparing TCM and TTO Creator Marketplace endpoints
The following table outlines the differences between TCM and TTO Creator Marketplace endpoints.

| Changes | TCM Endpoint | TTO Creator Marketplace Endpoint |
|---|---|---|
| Endpoint path | /v1.3/tcm/report/get/v2/ | /v1.3/tto/tcm/report/ |
| Same request parameters | `start_date` ⏎ `end_date` ⏎ `page` ⏎ `page_size` | `start_date` ⏎ `end_date` ⏎ `page` ⏎ `page_size` |
| Deprecated request parameters | N/A | `tcm_account_id` ⏎ `order_ids` ⏎ `need_daily_stats` ⏎ `metrics` |
| New request parameters | N/A | `tto_tcm_account_id` ⏎ `campaign_id` |
| Response parameters of the same name ⏎ Note: These parameters might be nested within different objects or object arrays. | `insights.metrics.video_id` ⏎ `insights.metrics.video_views` ⏎ `insights.metrics.video_views_organic` ⏎ `insights.metrics.video_views_paid` ⏎ `insights.metrics.reach` ⏎ `insights.metrics.engagement_count` ⏎ `insights.metrics.engagement_rate` ⏎ `insights.metrics.video_completion_rate` ⏎ `insights.metrics.likes` ⏎ `insights.metrics.comments` ⏎ `insights.metrics.shares` ⏎ `insights.metrics.total_play_time` ⏎ `insights.metrics.average_view_time` ⏎ `insights.metrics.two_seconds_views` ⏎ `insights.metrics.six_seconds_views` ⏎ `insights.metrics.video_view_retention` ⏎ `insights.metrics.video_views_by_source` ⏎ `insights.metrics.video_views_by_source.for_you` ⏎ `insights.metrics.video_views_by_source.hashtag` ⏎ `insights.metrics.video_views_by_source.sound` ⏎ `insights.metrics.video_views_by_source.personal_profile` ⏎ `insights.metrics.video_views_by_source.search` ⏎ `insights.metrics.video_views_by_source.following` ⏎ `insights.metrics.audience_interest_distribution` ⏎ `insights.metrics.audience_interest_distribution. ⏎ interest_tag` ⏎ `insights.metrics.audience_interest_distribution. ⏎ percentage` ⏎ `insights.metrics.daily_stats` ⏎ `insights.metrics.daily_stats.date` ⏎ `insights.metrics.daily_stats.views` ⏎ `insights.metrics.daily_stats.video_views_organic` ⏎ `insights.metrics.daily_stats.video_views_paid` ⏎ `insights.metrics.daily_stats.engagement_rate` ⏎ `insights.metrics.daily_stats.video_completion_rate` ⏎ `insights.metrics.daily_stats.likes` ⏎ `insights.metrics.daily_stats.comments` ⏎ `insights.metrics.daily_stats.shares` ⏎ `page_info` ⏎ `page_info.page` ⏎ `page_info.page_size` ⏎ `page_info.total_page` ⏎ `page_info.total_number` | `videos.video_info.video_id` ⏎ `videos.video_views` ⏎ `videos.video_views_organic` ⏎ `videos.video_views_paid` ⏎ `videos.reach` ⏎ `videos.engagement_count` ⏎ `videos.engagement_rate` ⏎ `videos.video_completion_rate` ⏎ `videos.likes` ⏎ `videos.comments` ⏎ `videos.shares` ⏎ `videos.total_play_time` ⏎ `videos.average_view_time` ⏎ `videos.two_seconds_views` ⏎ `videos.six_seconds_views` ⏎ `videos.video_view_retention` ⏎ `videos.video_views_by_source` ⏎ `videos.video_views_by_source.for_you` ⏎ `videos.video_views_by_source.hashtag` ⏎ `videos.video_views_by_source.sound` ⏎ `videos.video_views_by_source.personal_profile` ⏎ `videos.video_views_by_source.search` ⏎ `videos.video_views_by_source.following` ⏎ `videos.audience_interest_distribution` ⏎ `videos.audience_interest_distribution. ⏎ interest_tag` ⏎ `videos.audience_interest_distribution. ⏎ percentage` ⏎ `videos.daily_stats` ⏎ `videos.daily_stats.date` ⏎ `videos.daily_stats.views` ⏎ `videos.daily_stats.video_views_organic` ⏎ `videos.daily_stats.video_views_paid` ⏎ `videos.daily_stats.engagement_rate` ⏎ `videos.daily_stats.video_completion_rate` ⏎ `videos.daily_stats.likes` ⏎ `videos.daily_stats.comments` ⏎ `videos.daily_stats.shares` ⏎ `page_info` ⏎ `page_info.page` ⏎ `page_info.page_size` ⏎ `page_info.total_page` ⏎ `page_info.total_number` |
| Deprecated response parameters | N/A | `insights` ⏎ `insights.dimensions` ⏎ `insights.dimensions.tcm_account_id` ⏎ `insights.dimensions.order_id` ⏎ `insights.dimensions.order_type` ⏎ `insights.dimensions.video_id` ⏎ `insights.dimensions.handle_name` ⏎ `insights.dimensions.video_first_release_time` ⏎ `insights.metrics` ⏎ `insights.metrics.video_boosted_date` ⏎ `insights.metrics.engagement_rate_benchmark_p25` ⏎ `insights.metrics.engagement_rate_benchmark_p50` ⏎ `insights.metrics. ⏎ most_popular_country_state_distribution` ⏎ `insights.metrics.most_popular_country_state_distribution.country` ⏎ `insights.metrics.most_popular_country_state_distribution.locale_distribution` ⏎ `insights.metrics.most_popular_country_state_distribution.locale_distribution.locale` ⏎ `insights.metrics.most_popular_country_state_distribution.locale_distribution.percentage` ⏎ `insights.metrics. ⏎ video_complete_rate_benchmark_p25` ⏎ `insights.metrics. ⏎ video_complete_rate_benchmark_p50` ⏎ `insights.metrics. ⏎ lifetime_top_country_distribution` ⏎ `insights.metrics. ⏎ lifetime_top_country_distribution.country` ⏎ `insights.metrics. ⏎ lifetime_top_country_distribution.percentage` ⏎ `insights.metrics.lifetime_device_distribution` ⏎ `insights.metrics. ⏎ lifetime_device_distribution.device` ⏎ `insights.metrics. ⏎ lifetime_device_distribution.percentage` ⏎ `insights.metrics.lifetime_gender_distribution` ⏎ `insights.metrics.lifetime_gender_distribution. ⏎ gender` ⏎ `insights.metrics.lifetime_gender_distribution. ⏎ percentage` ⏎ `insights.metrics.lifetime_top_age_distribution` ⏎ `insights.metrics.lifetime_top_age_distribution. ⏎ age` ⏎ `insights.metrics.lifetime_top_age_distribution. ⏎ percentage` ⏎ `insights.metrics.daily_stats.reach` |
| New response parameters | N/A | `tto_tcm_account_id` ⏎ `campaign_id` ⏎ `country_code` ⏎ `videos` ⏎ `videos.video_info` ⏎ `videos.video_info.create_time` ⏎ `videos.video_info.embed_url` ⏎ `videos.video_info.thumbnail_url` ⏎ `videos.video_info.authorization_code` ⏎ `videos.creator_info` ⏎ `videos.creator_info.display_name` ⏎ `videos.creator_info.handle_name` ⏎ `videos.audience_genders_distribution` ⏎ `videos.audience_genders_distribution.gender` ⏎ `videos.audience_genders_distribution.percentage` ⏎ `videos.audience_countries_distribution` ⏎ `videos.audience_countries_distribution.country` ⏎ `videos.audience_countries_distribution. ⏎ percentage` ⏎ `videos.audience_age_distribution` ⏎ `videos.audience_age_distribution.age` ⏎ `videos.audience_age_distribution.percentage` ⏎ `videos.audience_device_distribution` ⏎ `videos.audience_device_distribution.device` ⏎ `videos.audience_device_distribution.percentage` ⏎ `videos.audience_locale_distribution` ⏎ `videos.audience_locale_distribution.locale` ⏎ `videos.audience_locale_distribution.percentage` ⏎ `videos.likes_paid` ⏎ `videos.likes_organic` ⏎ `videos.comments_paid` ⏎ `videos.comments_organic` ⏎ `videos.shares_paid` ⏎ `videos.shares_organic` ⏎ `videos.engagement_rate_paid` ⏎ `videos.engagement_rate_organic` ⏎ `videos.anchor_metrics` ⏎ `videos.anchor_metrics.anchor_views` ⏎ `videos.anchor_metrics.anchor_clicks` ⏎ `videos.anchor_metrics.anchor_unique_views` ⏎ `videos.anchor_metrics.anchor_unique_clicks` ⏎ `videos.anchor_id` ⏎ `campaign_type` ⏎ `campaign_channel_type` ⏎ `ad_impressions` ⏎ `ad_cost` ⏎ `ad_cpa` ⏎ `ad_ctr` ⏎ `ad_cvr` ⏎ `reach_organic` ⏎ `reach_paid` ⏎ `video_completion_rate_organic` ⏎ `video_completion_rate_paid` ⏎ `average_view_time_organic` ⏎ `average_view_time_paid` ⏎ `organic_two_seconds_views` ⏎ `paid_two_seconds_views` ⏎ `organic_six_seconds_views` ⏎ `paid_six_seconds_views` ⏎ `audience_language_distribution` ⏎ `language` ⏎ `percentage` ⏎ `videos.daily_stats.engagement_rate_organic` ⏎ `videos.daily_stats.engagement_rate_paid` ⏎ `videos.daily_stats.likes_organic` ⏎ `videos.daily_stats.likes_paid` ⏎ `videos.daily_stats.comments_organic` ⏎ `videos.daily_stats.comments_paid` ⏎ `videos.daily_stats.shares_organic` ⏎ `videos.daily_stats.shares_paid` ⏎ `videos.favorites` ⏎ `videos.favorites_organic` ⏎ `videos.favorites_paid` ⏎ `videos.daily_stats.favorites` ⏎ `videos.daily_stats.favorites_organic` ⏎ `videos.daily_stats.favorites_paid` |

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/tto/tcm/report/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Access token authorized by a TikTok One Creator Marketplace account. ⏎ Để biết chi tiết, xem [Authentication](../10-organic-api/tiktok-one-api.md#doc-1825117875361793). |
| Country-Code  ****(Bắt buộc)**** | string | A country or region code that is associated with the TikTok One Creator Marketplace campaign (`campaign_id`). ⏎ To obtain a valid country or region code associated with the TikTok One Creator Marketplace campaign, use [/tto/tcm/campaign/](68-tiktok-one-p1.md#doc-1815693562720258) and select one code from the returned `country_codes`. |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
| tto_tcm_account_id ***(Bắt buộc)*** | string | The ID of the TikTok One Creator Marketplace account.<br><br>To obtain the IDs of the accounts that you can access via `Access-Token`, use [/tto/oauth2/tcm/](68-tiktok-one-p1.md#doc-1815693478150146). |
|campaign_id ***(Bắt buộc)*** | string | The ID of a TikTok One Creator Marketplace campaign with a [campaign-level invite link](../10-organic-api/tiktok-one-api.md#doc-1830337139853313) or [brand-level invite link](../10-organic-api/tiktok-one-api.md#doc-1830337139853313). <br><br>To create a campaign and obtain the ID chiến dịch quảng cáo, use [/tto/tcm/campaign/create/](68-tiktok-one-p1.md#doc-1815693549459458). |
| start_date **(Điều kiện)** | string | Bắt buộc khi `end_date` is passed. <br><br>  <ul><li>If you specify both `start_date` and `end_date`, the response will include the `daily_stats` parameter that shows the daily metrics for the specified time range.</li><li>If you don't specify both `start_date` and `end_date`, the response will not include the daily metrics (`daily_stats`).</li></ul> <br> Report start date, in the format of `YYYY-MM-DD` (UTC+0 time).  <br> <br>The `start_date` should not be earlier than the campaign Thời gian tạo. To obtain the campaign Thời gian tạo, check the `create_time` returned from [/tto/tcm/campaign/create/](68-tiktok-one-p1.md#doc-1815693549459458) or [/tto/tcm/campaign/](68-tiktok-one-p1.md#doc-1815693562720258).<br> <br> Example: `2024-01-01`. |
| end_date **(Điều kiện)** | string | Bắt buộc khi `start_date` is passed.<br><br>  <ul><li>If you specify both `start_date` and `end_date`, the response will include the `daily_stats` parameter that shows the daily metrics for the specified time range.</li><li>If you don't specify both `start_date` and `end_date`, the response will not include the daily metrics (`daily_stats`).</li></ul> <br>Report end date, in the format of `YYYY-MM-DD` (UTC+0 time).<br> <br> Example: `2024-02-01`. |
| page | integer | Current Số trang cần lấy dữ liệu. <br>This field specifies which page of results to retrieve. The number of pages is based on the total number of records and the `page_size`. <br><br>Giá trị mặc định: 1. <br>Value range: ≥ 1. |
|page_size|integer|Page size.<br>This specifies the number of records (the performance metrics for videos linked to the specified ID chiến dịch quảng cáo) that you try to retrieve for each request.<br><br>Giá trị mặc định: 25.<br>Value range: 1-100.|
### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/tto/tcm/report/?tto_tcm_account_id={{tto_tcm_account_id}}&campaign_id={{campaign_id}}&start_date=2024-09-25&end_date=2024-09-27' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Country-Code: {{Country-Code}}' \
```
## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|code |number|Response code. For the complete list of response codes and descriptions, see [Appendix-Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message|string|Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|request_id |string|The log ID of a request, which uniquely identifies the request.  |
|data |object|Returned data.|
#| tto_tcm_account_id | string | The ID of the TikTok One Creator Marketplace account. |
#| campaign_id | string | The ID of the TikTok One Creator Marketplace campaign. |
#| country_code | string | A country or region code that is associated with the TikTok One Creator Marketplace campaign. |
#| campaign_type | string | The type of the TTO Creator Marketplace campaign.<br><br>Các giá trị enum hỗ trợ: <ul><li>`CAMPAIGN`: A campaign with a [campaign-level invite link](../10-organic-api/tiktok-one-api.md#doc-1830337139853313).</li><li>`BRAND_LINK`: A campaign with a [brand-level invite link](../10-organic-api/tiktok-one-api.md#doc-1830337139853313).</li></ul> |
#|campaign_channel_type|string|The channel type where the campaign was created.<br><br>Các giá trị enum hỗ trợ: <ul><li>`STANDARD_CAMPAIGN`: A Standard Campaign created on the TikTok One platform.</li><li>`LITE_CAMPAIGN`: A Lite Campaign created on the TikTok One platform.</li><li>`API_LITE_CAMPAIGN`: A Lite Campaign created via the API.</li></ul>|
#| page_info | object | Pagination information. |
##| page | integer | Current Số trang cần lấy dữ liệu. |
##| page_size | integer | Current page size. |
##| total_page | integer | Tổng số trang. |
##| total_number | integer | Total number of videos.<br><br><p><span style="color:darkred"><b>Note</b></span>: This number is country-specific and depends on the header parameter `Country-Code`. For example, if a campaign includes two videos in the US and one video in Canada, `total_number` will be 2 when `Country-Code` is set to `US`, and 1 when set to `CA`. |
#| videos | object[] | The list of videos that have been linked to the TikTok One Creator Marketplace campaign. |
##| video_info | object | Information about the video. |
###| create_time | string | The time when the video was published, in the format of `YYYY-MM-DD HH:MM:SS` (UTC+0 time). <br><br>Example: `2024-01-01 00:00:01`. |
###| embed_url | string | An embeddable link to the TikTok video. This URL can be used to embed the TikTok video in external websites or applications.<br><br> Example: `https://v77.tiktokcdn.com/&#123;&#123;embed_url&#125;&#125;`. |
###| thumbnail_url | string | Temporary URL for thumbnail of the video. Expiration date-time is included in the `x-expires` query param as Epoch/Unix time in seconds. <br><br>Example: `https://p16-sign-va.tiktokcdn.com/obj/tos-maliva-p-0068/12345678a12e3456a02017dcf822217e_1725607566?lk3s=c6b69ba0&nonce=51584&refresh_token=73f581ee21c7de32951926a0104f51a2&x-expires=1729173600&x-signature=vIBf8%2Bmp4%2FxXQpKrca1B5%2B%2FfpTU%3D&shp=c6b69ba0&shcp=-`. |
###| video_id | string | The unique identifier for the video. |
###| authorization_code | string | The Spark Ads authorization code for the video. |
##| reach_organic | integer | Organic reach (unique viewers).<br>The estimated number of unique viewers who viewed the video at least once from organic traffic. |
##| reach_paid | integer | Paid reach (unique viewers).<br>The estimated number of unique viewers who viewed the video at least once from paid traffic. |
##| video_completion_rate_organic | double | Organic video completion rate.<br>The percentage of viewers who watched a video in its entirety. It’s calculated by dividing the number of complete video views by total number of video views. |
##| video_completion_rate_paid | double | Paid video completion rate.<br>The percentage of viewers who watched a video in its entirety. It’s calculated by dividing the number of complete video views by total number of video views. |
##| average_view_time_organic | double | Organic average view time, in seconds.<br>The average amount of time viewers spend watching a video. It’s calculated by dividing the total organic play time of the video by the total number of video views. |
##| average_view_time_paid | double | Paid average view time, in seconds.<br>The average amount of time viewers spend watching a video. It’s calculated by dividing the total paid play times of the video by the total number of video views. |
##| organic_two_seconds_views | double | Organic 2-Second video views.<br>Percentage of views that lasted at least 2 seconds long. It's calculated as the number of organic views that lasted more than 2 seconds divided by views. |
##| paid_two_seconds_views | double | Paid 2-Second video views.<br>Percentage of views that lasted at least 2 seconds long. It's calculated as the number of paid views that lasted more than 2 seconds divided by views. |
##| organic_six_seconds_views | double | Organic 6-Second video views.<br>Percentage of views that lasted at least 6 seconds long. It's calculated as the number of organic views that lasted more than 6 seconds divided by views. |
##| paid_six_seconds_views | double | Paid 6-Second video views.<br>Percentage of views that lasted at least 6 seconds. It's calculated as the number of paid views that lasted more than 6 seconds divided by views. |
##| audience_language_distribution | object[] | Distribution of video views by audience countries.<br>Updated daily. |
###| language | string | The language code representing the user’s configured browsing language. You can use this value to map language codes to languages by using [/tool/language/](70-tools-p1.md#doc-1737188554152962).<br>Example: `en`. |
###| percentage | double | The percentage of the audience using a language.<br>Example: `0.10526315789473684`. <br>A value of 0.10526315789473684 indicates a percentage of approx. 10.52%. |
##| creator_info | object | Information about the TikTok Creator. |
###| display_name | string | The display name of the Creator. |
###| handle_name | string | The handle name of the Creator. |
##| ad_clicks | float | The number of clicks on your ads. |
##| ad_conversions | float | The number of times your ad achieved an outcome based on the objective and settings you selected.<br><br><p><span style="color:darkred"><b>Note</b></span>: This field is based on the selected campaign objective and settings. |
##|ad_cost|double|Ads cost.<br>The estimated total amount of money you've spent on your campaign, ad group, or ad during its schedule.<br><br>Updated in real time.|
##|ad_cpa|double|Cost per conversion.<br>The average amount of money you've spent on a paid conversion.<br><br>Updated in real time.|
##| ad_cpc | float | The average amount of money you've spent on a paid click. |
##| ad_cpm | float | The average amount of money you've spent per 1,000 paid impressions. |
##|ad_ctr|double|CTR (destination).<br>The percentage of times people saw your ad and performed a click.<br><br>Updated in real time.|
##|ad_cvr|double|Conversion rate (CVR).<br>The percentage of conversions from all impressions on your ads.<br><br>Updated in real time.|
##|ad_impressions|integer|Impressions.<br>The number of times your ads were on screen.<br><br>Updated in real time.|
##| video_views | integer | Total views.<br>Total number of times the video has been watched. <br><br> Updated in real time |
##| video_views_organic | integer | Organic video views.<br> Total number of views acquired through organic delivery, and not through [Spark Ads](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1739470744631298). <br><br> Updated in real time |
##| video_views_paid | integer | Paid views.<br> Total number of views acquired through [Spark Ads](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1739470744631298).<br><br> Updated in real time |
##| reach | integer | Reach (Unique viewers). <br> Estimated number of unique users who viewed the video at least once.<br><br>Updated daily |
##| engagement_count | integer | Engagement count. <br> Total number of likes (`likes`), shares (`shares`), and comments (`comments`). <br><br> Updated in real time |
##| engagement_rate | double | Engagement rate, calculated as the engagement count (`engagement_count`) divided by the total number of views (`video_views`). <br><br> Updated in real time |
##| engagement_rate_organic | double  | Organic engagement rate. <br>The percentage of the audience who interacted with the campaign or video through organic delivery. It is calculated by dividing the number of organic interactions (likes, comments, and shares from non-paid views) by the total number of organic video views.<br><br> Updated in real time |
##| engagement_rate_paid | double  | Paid engagement rate.<br>The percentage of the audience who interacted with the campaign or video through Spark Ads. It is calculated by dividing the number of paid interactions (likes, comments, and shares from paid views) by the total number of paid video views.<br><br>Updated in real time |
##| video_completion_rate | double | Video completion rate, calculated as total completed video views divided by the total number of views (`video_views`). <br><br> Updated in real time for the first seven days after the post was created and then updated daily afterwards |
##| likes | integer | Likes. <br>Total number of likes associated with the video. <br><br>Updated in real time |
##| likes_organic |integer | Organic likes. <br>Total number of likes generated through non-paid (organic) delivery. <br><br>Updated in real time |
##| likes_paid |integer | Paid likes. <br>Total number of likes generated through Spark Ads. <br><br>Updated in real time |
##| comments | integer | Comments.<br> Total number of comments associated with the video. <br><br>Updated in real time |
##| comments_organic | integer | Organic comments.<br>Total number of comments generated through non-paid (organic) delivery. <br><br>Updated in real time |
##| comments_paid | integer| Paid comments.<br>Total number of comments generated through Spark Ads. <br><br>Updated in real time |
##| shares | integer | Shares. <br> Total number of shares associated with the video.<br><br> Updated in real time |
##| shares_organic | integer | Organic shares. <br>Total number of shares generated through non-paid (organic) delivery.<br><br> Updated in real time |
##| shares_paid | integer | Paid shares. <br> Total number of shares generated through Spark Ads. <br><br>Updated in real time |
##|favorites|integer|Favorites.<br>Total number of favorites received from the video.<br><br>Updated daily|
##|favorites_organic|integer|Organic favorites.<br>Total number of favorites received from the video through non-paid (organic) delivery.<br><br>Updated daily|
##|favorites_paid|integer|Paid favorites.<br>Total number of favorites received from the video through Spark Ads.<br><br>Updated daily|
##| total_play_time | integer | Total play time, in seconds.<br> Total amount of time users spend watching the video. <br><br> Updated in real time for the first seven days after the post was created and then updated daily afterwards |
##| average_view_time | double | Average view time, in seconds.<br>Average amount of time users spend watching the video, calculated as the total play time (`total_play_time`) divided by views (`video_views`). <br><br>Updated in real time for the first seven days after the post was created and then updated daily afterwards |
##| two_seconds_views | double | 2-Second video views. <br> Percentage of views that lasted more than two seconds, calculated as the number of views that lasted more than 2 seconds divided by views (`video_views`).<br><br>Updated daily |
##| six_seconds_views | double | 6-Second video views. <br>Percentage of views that lasted more than six seconds, calculated as the number of views that lasted more than six seconds divided by views (`video_views`).<br><br> Updated daily |
##| video_view_retention | double[] | A list of numbers indicating the video retention rate at each second. <br><br>For instance, the value `&#91;1, 0.61, 0.27, 0.2, 0.16, 0.14, 0.11, 0.09, 0.08, 0.07, 0.07, 0.06, 0.05, 0.05, 0.05, 0.04, 0.04&#93;` indicates that during the first second, the video retention rate decreases from 100% to 61%.  <br><br>Updated in real time for the first seven days after the post was created and then updated daily afterwards |
##| video_views_by_source | object | View sources. <br> Breakdown of how viewers were exposed to the video. <br><br>Updated in real time for the first seven days after the post was created and then updated daily afterwards |
###| for_you | integer | Video views from For You page. |
###| hashtag | integer| Video views from hashtag. |
###| sound | integer| Video views from sound. |
###| personal_profile | integer | Video views from personal profile. |
###| search | integer | Video views from search. |
###| following | integer | Video views from following. |
###| other | integer | Video views from other. |
##| audience_genders_distribution | object[] | Breakdown of male and female users among viewers. <br><br> Updated daily|
###| gender | string | Gender.<br><br> Các giá trị enum hỗ trợ: <ul><li> `FEMALE`: female. </li><li> `MALE`: male. </li></ul><br><p><span style="color:darkred"><b>Note</b></span>: This field might return `null` if the system cannot determine the gender.  |
###| percentage | double | Percentage. |
##| audience_countries_distribution | object[] | Distribution of video views by audience countries. <br><br> Updated daily |
###| country | string | Country or region code.<br><br> Example: `US`. |
###| percentage | double | Percentage. |
##| audience_age_distribution | object[] | Breakdown of viewers by age group.<br><br>Updated daily |
###| age | string | Age group. <br><br>Các giá trị enum hỗ trợ: <ul><li>`1`: 13-17. </li><li>`2`: 18-24.</li><li>`3`: 25-34.</li><li> `4`: 35-44 </li><li>`5`: 45-54.</li><li>`6`: 55+. </li></ul>|
###| percentage | double | Percentage. |
##| audience_device_distribution | object[] | Breakdown of viewers by operating system. <br><br>  Updated daily |
###| device | string | Device operating system.<br><br> Các giá trị enum hỗ trợ: <ul><li>`android`: Android.</li><li>`ios`: iOS.</li></ul>|
###| percentage | double | Percentage. |
##| audience_locale_distribution | object[] | Breakdown of viewers by state-level locales in the country or region. <br><br> Only available for the US. <br><br>  Updated daily |
###| locale | string | State-level locale. <br><br> Để xem danh sách giá trị enum, xem **Location IDs**. |
###| percentage | double | Percentage. <br>Total number of viewers in the state (`locale`) divided by the total number of viewers in the country or region. |
##| audience_interest_distribution | object[] | Breakdown of viewers by interest categories.<br><br>Updated daily |
###| interest_tag | string | The ID of the interest category.<br><br> To learn about the corresponding interest category name for each interest category ID, see <a href="#item-link-Mapping between interest category ID and name">Mapping between interest category ID and name</a>. |
###| percentage | double | Percentage. |
##|anchor_id|string|The ID of the anchor that is associated with the campaign.|
##|anchor_metrics|object|Anchor metrics.|
###|anchor_views|number|Anchor views.<br>Total number of times the anchor has been viewed.|
###|anchor_clicks|number|Anchor clicks.<br>Total number of clicks on the anchor.|
###|anchor_unique_views|number|Unique anchor views.<br>The number of unique viewers who saw the anchor.|
###|anchor_unique_clicks|number|Unique anchor clicks.<br>The number of times the anchor was clicked by distinct users.|
##| daily_stats | object[] | Daily statistics breakdown.<br><br><p><span style="color:darkred"><b>Note</b></span>: <ul><li>`daily_stats` is only available for the most recent 90 days. If the specified `start_date` and `end_date` fall outside this 90-day window, `daily_stats` will return null.</li><li>We won't fill in the missing metrics with any Giá trị mặc định (such as 0), so if one metric is missing from one day, that means the data is not available.</li></ul> |
###| date | string | Date, in the format of `YYYY-MM-DD` (UTC+0 time). |
###| views | integer | Total views. <br>Total number of times the video has been watched on the date. |
###| video_views_organic | integer | Organic video views.<br>Total number of views acquired through organic delivery, and not through [Spark Ads](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1739470744631298) on the date. |
###| video_views_paid | integer | Paid views. <br>Total number of views acquired through [Spark Ads](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1739470744631298) on the date. |
###| engagement_rate | double | Engagement rate, calculated as the total number of likes (`likes`), shares (`shares`), and comments (`comments`) divided by the total number of views (`views`) on the date. |
###|engagement_rate_organic|double|Organic engagement rate.<br>Engagement rate acquired through organic delivery, and not through [Spark Ads](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1739470744631298) on the date.|
###|engagement_rate_paid|double|Paid engagement rate.<br>Engagement rate acquired through [Spark Ads](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1739470744631298) on the date.|
###| video_completion_rate | double | Video completion rate, calculated as total completed video views divided by the total number of views (`views`) on the date. |
###| likes | integer | Likes.<br> Total number of likes associated with the video on the date. |
###|likes_organic|integer|Organic likes.<br>Total number of likes acquired through organic delivery, and not through [Spark Ads](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1739470744631298) on the date.|
###|likes_paid|integer|Paid likes.<br>Total number of likes acquired through [Spark Ads](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1739470744631298) on the date.|
###| comments | integer | Comments.<br> Total number of comments associated with the video on the date. |
###|comments_organic|integer|Organic comments.<br>Total number of comments acquired through organic delivery, and not through [Spark Ads](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1739470744631298) on the date.|
###|comments_paid|integer|Paid comments.<br>Total number of comments acquired through [Spark Ads](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1739470744631298) on the date.|
###| shares | integer | Shares. <br>Total number of shares associated with the video on the date. |
###|shares_organic|integer|Organic shares.<br>Total number of shares acquired through organic delivery, and not through [Spark Ads](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1739470744631298) on the date.|
###|shares_paid|integer|Paid shares.<br>Total number of shares acquired through [Spark Ads](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1739470744631298) on the date.|
###|favorites|integer|Favorites.<br>Total number of favorites received from the video on the date.|
###|favorites_organic|integer|Organic favorites.<br>Total number of favorites received from the video through organic delivery, and not through [Spark Ads](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1739470744631298) on the date.|
###|favorites_paid|integer|Paid favorites.<br>Total number of favorites received from the video through [Spark Ads](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1739470744631298) on the date.|
### Mapping between interest category ID and name

| Interest category ID ⏎ （interest_id） | Interest category name |
|---|---|
| 10 | Education |
| 11 | Vehicles & Transportation |
| 12 | Baby, Kids & Maternity |
| 13 | Financial Services |
| 14 | Beauty & Personal Care |
| 15 | Tech & Electronics |
| 16 | Appliances |
| 17 | Travel |
| 18 | Household Products |
| 19 | Pets |
| 20 | Apps |
| 21 | Home Improvement |
| 22 | Apparel & Accessories |
| 23 | News & Entertainment |
| 24 | Business Services |
| 25 | Games |
| 26 | Life Services |
| 27 | Food & Beverage |
| 28 | Sports & Outdoors |
| 29 | Health |
| 30 | E-Commerce (Non-app) |

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "campaign_channel_type": "API_LITE_CAMPAIGN",
        "campaign_id": "{{campaign_id}}",
        "campaign_type": "CAMPAIGN",
        "page_info": {
            "page": 1,
            "page_size": 25,
            "total_number": 1,
            "total_page": 1
        },
        "tto_tcm_account_id": "{{tto_tcm_account_id}}",
        "videos": [
            {
                "ad_cost": 0,
                "ad_cpa": 0,
                "ad_ctr": 0,
                "ad_cvr": 0,
                "ad_impressions": 0,
                "ad_roas": 0,
                "anchor_id": null,
                "anchor_metrics": null,
                "audience_age_distribution": [
                    {
                        "age": "4",
                        "percentage": 0.625
                    },
                    {
                        "age": "3",
                        "percentage": 0.375
                    }
                ],
                "audience_countries_distribution": [
                    {
                        "country": "US",
                        "percentage": 0.7142857142857143
                    },
                    {
                        "country": "GB",
                        "percentage": 0.14285714285714285
                    },
                    {
                        "country": "SA",
                        "percentage": 0.14285714285714285
                    }
                ],
                "audience_device_distribution": [
                    {
                        "device": "ios",
                        "percentage": 1
                    },
                    {
                        "device": "android",
                        "percentage": 0
                    }
                ],
                "audience_genders_distribution": [
                    {
                        "gender": "MALE",
                        "percentage": 0.875
                    },
                    {
                        "gender": "FEMALE",
                        "percentage": 0.125
                    }
                ],
                "audience_interest_distribution": [
                    {
                        "interest_tag": "14",
                        "percentage": 0.047619047619047616
                    },
                    {
                        "interest_tag": "18",
                        "percentage": 0.047619047619047616
                    },
                    {
                        "interest_tag": "11",
                        "percentage": 0.047619047619047616
                    },
                    {
                        "interest_tag": "10",
                        "percentage": 0.047619047619047616
                    },
                    {
                        "interest_tag": "17",
                        "percentage": 0.047619047619047616
                    },
                    {
                        "interest_tag": "20",
                        "percentage": 0.047619047619047616
                    },
                    {
                        "interest_tag": "21",
                        "percentage": 0.047619047619047616
                    },
                    {
                        "interest_tag": "22",
                        "percentage": 0.047619047619047616
                    },
                    {
                        "interest_tag": "26",
                        "percentage": 0.047619047619047616
                    },
                    {
                        "interest_tag": "30",
                        "percentage": 0.047619047619047616
                    }
                ],
                "audience_locale_distribution": null,
                "average_view_time": 3.63,
                "comments": 0,
                "comments_organic": null,
                "comments_paid": null,
                "creator_info": {
                    "display_name": "{{display_name}}",
                    "handle_name": "{{handle_name}}"
                },
                "daily_stats": null,
                "engagement_count": 0,
                "engagement_rate": 0,
                "engagement_rate_organic": null,
                "engagement_rate_paid": null,
                "likes": 0,
                "likes_organic": null,
                "likes_paid": null,
                "reach": 6,
                "shares": 0,
                "shares_organic": null,
                "shares_paid": null,
                "six_seconds_views": 0.2222222222222222,
                "total_play_time": 29,
                "two_seconds_views": 0.6666666666666666,
                "video_completion_rate": 0.5,
                "video_info": {
                    "create_time": "{{create_time}}",
                    "embed_url": "{{embed_url}}",
                    "thumbnail_url": "{{thumbnail_url}}",
                    "video_id": "{{video_id}}"
                },
                "video_view_retention": [
                    1,
                    1,
                    0.83,
                    0.67,
                    0.5
                ],
                "video_views": 6,
                "video_views_by_source": [
                    {
                        "source": "sound",
                        "video_views": 0
                    },
                    {
                        "source": "hashtag",
                        "video_views": 0
                    },
                    {
                        "source": "following",
                        "video_views": 0
                    },
                    {
                        "source": "for_you",
                        "video_views": 0
                    },
                    {
                        "source": "search",
                        "video_views": 3
                    },
                    {
                        "source": "personal_profile",
                        "video_views": 3
                    }
                ],
                "video_views_organic": 6,
                "video_views_paid": null
            }
        ]
    }
}
```

---

<a id="doc-1751098904942594"></a>
<!-- doc_id: 1751098904942594 -->
<!-- doc_id: 1751098904942594 -->
# Apply for Spark Ads authorization
> Đường dẫn: API Reference > TikTok One > Apply for Spark Ads authorization
Use this endpoint to send a request to apply for TikTok creator's authorization to boost their video for a TikTok One (TTO) Creator Marketplace campaign.

## Yêu cầu gọi API (Request)

**Endpoint** `https://business-api.tiktok.com/open_api/v1.3/tcm/tt_video/apply/`

**Method** POST

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Access token authorized by a TTO Creator Marketplace account. Để biết chi tiết, xem [Authentication](../10-organic-api/tiktok-one-api.md#doc-1825117875361793). |
| Content-Type  ****(Bắt buộc)**** | string | Định dạng dữ liệu yêu cầu. ⏎ Allowed format: `application/json`. |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| video_id  ****(Bắt buộc)**** | string | ID of the video that is created under the creator account. ⏎ The video needs to meet the following requirement:  • The video has been uploaded and tagged as branded content, and the creator has linked the video to a TTO Creator Marketplace campaign via the invite link (`invite_link`) created via [/tto/tcm/campaign/create/](68-tiktok-one-p1.md#doc-1815693549459458). • You can get `video_id` via [/tto/tcm/campaign/](68-tiktok-one-p1.md#doc-1815693562720258) or [/tto/tcm/report/](68-tiktok-one-p2.md#doc-1815693573340162). |
| tcm_account_id  ****(Bắt buộc)**** | string | The ID of the TTO Creator Marketplace account. ⏎ To obtain the IDs of the TTO Creator Marketplace accounts that you can access via `Access-Token`, use [/tto/oauth2/tcm/](68-tiktok-one-p1.md#doc-1815693478150146). |
| authorization_days | number | Authorization validity period (in days). ⏎ Value range: 1-365. ⏎ Giá trị mặc định: 30. ⏎ **Note**: You can use this field to specify the validity period of the authorization, or to request an update for the validity period of approved authorization. ⏎ The actual validity period can be different from the validity period you request, because the creator can choose any validity period (one to 365 days) when approving the request. |
| action | string | The action to take. ⏎ Enum value: • `EXTEND`: To extend the validity period of the authorization by the specified days (`authorization_days`). For instance, when `authorization_days` is 30, you'll request the authorization to be extended by 30 days. |

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location  --request GET 'https://business-api.tiktok.com/open_api/v1.3/tcm/tt_video/apply/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "tcm_account_id":"{{tcm_account_id}}",
    "video_id":"{{video_id}}",
    "authorization_days": 30
}'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Response code. For the complete list of response codes and descriptions, see [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | Unique ID of the request. |
| data | object | Returned data. |

### Ví dụ lệnh cURL (Example)
```http
// curl
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {}
}
```

---

<a id="doc-1751098935842817"></a>
<!-- doc_id: 1751098935842817 -->
<!-- doc_id: 1751098935842817 -->
# Get the authorization status
> Đường dẫn: API Reference > TikTok One > Get the authorization status
Sử dụng endpoint này để lấy thông tin the Spark Ads authorization status of a TikTok One (TTO) Creator Marketplace campaign.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/tcm/tt_video/status/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Access token authorized by a TTO Creator Marketplace account. Để biết chi tiết, xem [Authentication](../10-organic-api/tiktok-one-api.md#doc-1825117875361793). |

**Parameters**

 Place these parameters in the query section.

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| video_id  ****(Bắt buộc)**** | string | ID of the video that is created under the creator account. ⏎ The video needs to meet the following requirement:  • The video has been uploaded and tagged as branded content, and the creator has linked the video to a TTO Creator Marketplace campaign via the invite link (`invite_link`) created via [/tto/tcm/campaign/create/](68-tiktok-one-p1.md#doc-1815693549459458). • You can get `video_id` via [/tto/tcm/campaign/](68-tiktok-one-p1.md#doc-1815693562720258) or [/tto/tcm/report/](68-tiktok-one-p2.md#doc-1815693573340162). |
| tcm_account_id  ****(Bắt buộc)**** | string | The ID of the TTO Creator Marketplace account. ⏎ To obtain the IDs of the TTO Creator Marketplace accounts that you can access via `Access-Token`, use [/tto/oauth2/tcm/](68-tiktok-one-p1.md#doc-1815693478150146). |

 ### Ví dụ lệnh cURL (Example)

```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/tcm/tt_video/status/?tcm_account_id={{tcm_account_id}}&video_id={{video_id}}' \
--header 'Access-Token: {{Access-Token}}'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | The Mã trạng thái phản hồi (0: Thành công). For the complete list of error codes and descriptions, see [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | The Thông điệp phản hồi từ máy chủ. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | Unique ID of the request. |
| data | object | Returned data. |
| ↳ video_id | string | Video ID. |
| ↳ auth_status | string | The status of the authorization. ⏎ Các giá trị enum hỗ trợ: • `WAITING`: The creator has not rejected or approved your request for authorization. ⏎ The creator will receive a notification on their TikTok app regarding your request and can approve or reject it through the System Notification page within the app. Even if the creator has enabled "Ad authorization" in the "Branded content and ad" settings, the `auth_status` will remain `WAITING` until the creator approves your request. However, in this case, you can receive an `auth_code` that can be used to grant video authorization to an advertiser account. • `REJECTED`: The creator has rejected your request for authorization. • `ACCEPTED`: The creator has approved your request for authorization. |
| ↳ auth_status_updated_time | string | The time when `auth_status` was last updated. ⏎ For example, when `auth_status` changed from `WAITING` to `ACCEPTED`. |
| ↳ num_remaining_request | number | Returned only for videos linked to TTCM orders. ⏎ The number of times left for you to request Spark Ads authorization. You have 30 times left at most to request authorization before the request is approved or rejected. |
| ↳ requested_authorization_days | number | The validity period (in days) that you request for spark ads authorization or the new validity period you want to update for the approved authorization. ⏎ Các giá trị enum hỗ trợ: `7`, `30`, `60`, `365`. ⏎ Giá trị mặc định: `30`. ⏎ **Note**: The actual validity period (`auth_code_end_time` - `auth_code_start_time`) can be different from the validity period you request, because the creator can choose any validity period (`7`，`30`，`60`，`365`) when approving the request. |
| ↳ auth_code | string | Returned only when `auth_status` is `ACCEPTED`. ⏎ Authorization code to boost the video in the order. |
| ↳ auth_code_start_time | string | Returned only when `auth_status` is `ACCEPTED`. ⏎ The UTC+0 date and time when the authorization code becomes valid. |
| ↳ auth_code_end_time | string | Returned only when `auth_status` is `ACCEPTED`. ⏎ UTC+0 date and time when the authorization code expires. |
| ↳ auth_code_status | string | Returned only when `auth_status` is `ACCEPTED`. ⏎ The status of the authorization code. ⏎ Các giá trị enum hỗ trợ: • `NOT_USED`: The authorization code has been generated but has not been used yet. • `IN_USE`: The authorization code has been generated and is in use now.  • `EXPIRED`: The authorization code has been generated and has expired. • `DELETED`: The authorization code has been deleted. |

### Ví dụ lệnh cURL (Example)
#### When authorization request is pending
```http
// curl
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "auth_status": "WAITING",
        "auth_status_updated_time": "{{auth_status_updated_time}}",
        "requested_authorization_days": 30,
        "video_id": "{{video_id}}"
    }
}
```
#### When authorization request is accepted
```http
// curl
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "auth_code": "{{auth_code}}",
        "auth_code_end_time": "{{auth_code_end_time}}",
        "auth_code_start_time": "{{auth_code_start_time}}",
        "auth_code_status": "NOT_USED",
        "auth_status": "ACCEPTED",
        "auth_status_updated_time": "{{auth_status_updated_time}}",
        "requested_authorization_days": 30,
        "video_id": "{{video_id}}"
    }
}
```
#### When authorization request is rejected
```http
// curl
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "auth_status": "REJECTED",
        "auth_status_updated_time": "{{auth_status_updated_time}}",
        "requested_authorization_days": 30,
        "video_id": "{{video_id}}"
    }
}
```

---

<a id="doc-1826564934723585"></a>
<!-- doc_id: 1826564934723585 -->
<!-- doc_id: 1826564934723585 -->
# Create a webpage anchor
> Đường dẫn: API Reference > TikTok One > Create a webpage anchor
Sử dụng endpoint này để tạo a webpage anchor of the web destination link type.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/tto/tcm/anchor/create/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Access token authorized by a TikTok One Creator Marketplace account. ⏎ Để biết chi tiết, xem [Authentication](../10-organic-api/tiktok-one-api.md#doc-1825117875361793). |
| Content-Type  ****(Bắt buộc)**** | string | Định dạng dữ liệu yêu cầu. ⏎ • If `upload_type` is `UPLOAD_BY_FILE`, use `multipart/form-data`. • If `upload_type` is `UPLOAD_BY_URL`, use `application/json`. |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
| tto_tcm_account_id ***(Bắt buộc)*** | string | The ID of the TTO Creator Marketplace account.<br><br>To obtain the IDs of the accounts that you can access via `Access-Token`, use [/tto/oauth2/tcm/](68-tiktok-one-p1.md#doc-1815693478150146). |
|anchor_type ***(Bắt buộc)***|string|The type of anchor.<br><br>Các giá trị enum hỗ trợ: <ul><li>`WEB_ANCHOR`: Webpage anchor. A type of anchor through which you can display your website link above the creator's video description.</li></ul>|
|anchor_sub_type **(Điều kiện)**|string|Bắt buộc khi `anchor_type` is `WEB_ANCHOR`.<br><br> The specific type of webpage anchor.<br><br>Các giá trị enum hỗ trợ: <ul><li>`DESTINATION`: Web destination link. This type directs viewers to a web destination link that can be opened in TikTok. The anchor shows up both in the creator's video and the comment section.<br><br><span style="color:darkred"><b>Note</b></span>: The web destination link is available for countries where TikTok Shop is not yet available. TikTok Shop is currently available in Indonesia, Thailand, Vietnam, Philippines, Malaysia, Singapore, United States, United Kingdom, and Saudi Arabia.</li></ul>|
|category_label_id **(Điều kiện)**|number|Bắt buộc khi `anchor_sub_type` is `DESTINATION`. <br><br>The ID of the category of your product or service.<br><br>To learn about the supported values, see <a href="#item-link-Supported values for category_label_id">Supported values for `category_label_id`</a>.|
|country_code ***(Bắt buộc)***|string|The code of the country or region. <br>The app information from this country or region's app store will be used. This anchor won’t be available in other countries or regions.<br><br>When `anchor_sub_type` is `DESTINATION`, the supported values vary based on `category_label_id`. To learn about the supported values for a specific category ID, see <a href="#item-link-Supported values for category_label_id">Supported values for `category_label_id`</a>. <br><br>To learn about the country or region that the code represents, see [Location code](../15-appendix/phu-luc-p1.md#doc-1737585867307010).<br><br>Example: `AU`.|
|call_to_action ***(Bắt buộc)***|object|Anchor link information.|
#|landing_page_url {+Conditional}|string|Bắt buộc khi `anchor_sub_type` is `DESTINATION`. <br><br>The URL of the page that the anchor will redirect viewers to. This page shows more information about your product or service.<br>Ensure that the link provided is a product or service detail page. Otherwise, the anchor may be rejected during review.|
|anchor_title ***(Bắt buộc)***|string|The title of the anchor.<br><br>When `anchor_sub_type` is `DESTINATION`, the enum values are:<ul><li>`WATCH_NOW`: Watch Now.</li><li>`LISTEN_NOW`: Listen Now.</li><li>`READ_MORE`: Read More.</li><li>`SHOW_NOW`: Shop Now.</li><li>`GET_OFFER`: Get Offer.</li><li>`LEARN_MORE`: Learn More.</li><li>`CONTACT_US`: Contact Us.</li><li>`JOIN_NOW`: Join Now.</li><li>`APPLY_NOW`: Apply Now.</li></ul>|
|anchor_name ***(Bắt buộc)***|string|The name of the anchor.<br><br>Giới hạn độ dài: 32 characters.<br><br>This information will not be shown to users in TikTok App.|
|upload_type ***(Bắt buộc)***|string|The upload method for thumbnail.<br><br>Các giá trị enum hỗ trợ: <ul><li>`UPLOAD_BY_FILE`: Upload by file. You need to specify `thumbnail_file` simultaneously.</li><li>`UPLOAD_BY_URL`: Upload by URL. You need to specify `thumbnail_url` simultaneously.</li></ul>|
|thumbnail_file **(Điều kiện)**|file|Bắt buộc khi `upload_type` is `UPLOAD_BY_FILE`. <br><br>The thumbnail file for the anchor.<br><br>Specification requirements: <ul><li>File size: within 2 MB.</li><li>Format: JPEG, PNG, and GIF.</li><li>Resolution: 210 (width) x 375 (height) pixels.</li></ul><br>This information will not be shown to users in TikTok App.|
|thumbnail_url **(Điều kiện)**|string|Bắt buộc khi `upload_type` is `UPLOAD_BY_URL`. <br><br>A publicly accessible thumbnail URL for the anchor.<br><br>Specification requirements: <ul><li>File size: within 2 MB.</li><li>Format: JPEG, PNG, and GIF.</li><li>Resolution: 210 (width) x 375 (height) pixels.</li></ul><br>This information will not be shown to users in TikTok App.|
### Supported values for `category_label_id`

| Category | Corresponding category_label_id value | Available country_code value |
|---|---|---|
| Automotive & Motorcycle | `3` | `AE`, `AR`, `AT`, `AU`, `BD`, `BE`, `BR`, `CA`, `CH`, `CL`, `CO`, `CZ`, `DE`, `DK`, `EC`, `EG`, `ES`, `FI`, `FR`, `GR`, `HU`, `IE`, `IL`, `IQ`, `IT`, `JP`, `KH`, `KR`, `KZ`, `MA`, `MX`, `NL`, `NO`, `NZ`, `PE`, `PK`, `PL`, `PT`, `RO`, `SE`, `TR`, `ZA` |
| Baby & Nursery | `13` | `AE`, `AR`, `AT`, `AU`, `BD`, `BE`, `BR`, `CA`, `CH`, `CL`, `CO`, `CZ`, `DE`, `DK`, `EC`, `EG`, `ES`, `FI`, `FR`, `GR`, `HU`, `IE`, `IL`, `IQ`, `IT`, `JP`, `KH`, `KR`, `KZ`, `MA`, `MX`, `NL`, `NO`, `NZ`, `PE`, `PK`, `PL`, `PT`, `RO`, `SE`, `TR`, `ZA` |
| Beauty & Personal Care | `16` | `AE`, `AR`, `AT`, `AU`, `BD`, `BE`, `BR`, `CA`, `CH`, `CL`, `CO`, `CZ`, `DE`, `DK`, `EC`, `EG`, `ES`, `FI`, `FR`, `GR`, `HU`, `IE`, `IL`, `IQ`, `IT`, `JP`, `KH`, `KR`, `KZ`, `MA`, `MX`, `NL`, `NO`, `NZ`, `PE`, `PK`, `PL`, `PT`, `RO`, `SE`, `TR`, `ZA` |
| Books, Magazines & Audio | `31` | `AE`, `AR`, `AT`, `AU`, `BD`, `BE`, `BR`, `CA`, `CH`, `CL`, `CO`, `CZ`, `DE`, `DK`, `EC`, `EG`, `ES`, `FI`, `FR`, `GR`, `HU`, `IE`, `IL`, `IQ`, `IT`, `JP`, `KH`, `KR`, `KZ`, `MA`, `MX`, `NL`, `NO`, `NZ`, `PE`, `PK`, `PL`, `PT`, `RO`, `SE`, `TR`, `ZA` |
| Collectibles | `33` | `AE`, `AR`, `AT`, `AU`, `BD`, `BE`, `BR`, `CA`, `CH`, `CL`, `CO`, `CZ`, `DE`, `DK`, `EC`, `EG`, `ES`, `FI`, `FR`, `GR`, `HU`, `IE`, `IL`, `IQ`, `IT`, `JP`, `KH`, `KR`, `KZ`, `MA`, `MX`, `NL`, `NO`, `NZ`, `PE`, `PK`, `PL`, `PT`, `RO`, `SE`, `TR`, `ZA` |
| Computers & Office Equipment | `7` | `AE`, `AR`, `AT`, `AU`, `BD`, `BE`, `BR`, `CA`, `CH`, `CL`, `CO`, `CZ`, `DE`, `DK`, `EC`, `EG`, `ES`, `FI`, `FR`, `GR`, `HU`, `IE`, `IL`, `IQ`, `IT`, `JP`, `KH`, `KR`, `KZ`, `MA`, `MX`, `NL`, `NO`, `NZ`, `PE`, `PK`, `PL`, `PT`, `RO`, `SE`, `TR`, `ZA` |
| Entertainment & media | `27` | `AU`, `BR`, `CA`, `DE`, `ES`, `FR`, `GB`, `ID`, `IT`, `JP`, `KR`, `MX`, `MY`, `PH`, `SG`, `TH`, `TW`, `US`, `VN` |
| Fashion Accessories | `23` | `AE`, `AR`, `AT`, `AU`, `BD`, `BE`, `BR`, `CA`, `CH`, `CL`, `CO`, `CZ`, `DE`, `DK`, `EC`, `EG`, `ES`, `FI`, `FR`, `GR`, `HU`, `IE`, `IL`, `IQ`, `IT`, `JP`, `KH`, `KR`, `KZ`, `MA`, `MX`, `NL`, `NO`, `NZ`, `PE`, `PK`, `PL`, `PT`, `RO`, `SE`, `TR`, `ZA` |
| Finance | `20` | `AE`, `AR`, `AT`, `AU`, `BD`, `BE`, `BR`, `CA`, `CH`, `CL`, `CO`, `CZ`, `DE`, `DK`, `EC`, `EG`, `ES`, `FI`, `FR`, `GR`, `HU`, `IE`, `IL`, `IQ`, `IT`, `JP`, `KH`, `KR`, `KZ`, `MA`, `MX`, `NL`, `NO`, `NZ`, `PE`, `PK`, `PL`, `PT`, `RO`, `SE`, `TR`, `ZA` |
| Food & Beverages | `10` | `AE`, `AR`, `AT`, `AU`, `BD`, `BE`, `BR`, `CA`, `CH`, `CL`, `CO`, `CZ`, `DE`, `DK`, `EC`, `EG`, `ES`, `FI`, `FR`, `GR`, `HU`, `IE`, `IL`, `IQ`, `IT`, `JP`, `KH`, `KR`, `KZ`, `MA`, `MX`, `NL`, `NO`, `NZ`, `PE`, `PK`, `PL`, `PT`, `RO`, `SE`, `TR`, `ZA` |
| Furniture | `1` | `AE`, `AR`, `AT`, `AU`, `BD`, `BE`, `BR`, `CA`, `CH`, `CL`, `CO`, `CZ`, `DE`, `DK`, `EC`, `EG`, `ES`, `FI`, `FR`, `GR`, `HU`, `IE`, `IL`, `IQ`, `IT`, `JP`, `KH`, `KR`, `KZ`, `MA`, `MX`, `NL`, `NO`, `NZ`, `PE`, `PK`, `PL`, `PT`, `RO`, `SE`, `TR`, `ZA` |
| Health | `25` | `AE`, `AR`, `AT`, `AU`, `BD`, `BE`, `BR`, `CA`, `CH`, `CL`, `CO`, `CZ`, `DE`, `DK`, `EC`, `EG`, `ES`, `FI`, `FR`, `GR`, `HU`, `IE`, `IL`, `IQ`, `IT`, `JP`, `KH`, `KR`, `KZ`, `MA`, `MX`, `NL`, `NO`, `NZ`, `PE`, `PK`, `PL`, `PT`, `RO`, `SE`, `TR`, `ZA` |
| Home Improvement | `24` | `AE`, `AR`, `AT`, `AU`, `BD`, `BE`, `BR`, `CA`, `CH`, `CL`, `CO`, `CZ`, `DE`, `DK`, `EC`, `EG`, `ES`, `FI`, `FR`, `GR`, `HU`, `IE`, `IL`, `IQ`, `IT`, `JP`, `KH`, `KR`, `KZ`, `MA`, `MX`, `NL`, `NO`, `NZ`, `PE`, `PK`, `PL`, `PT`, `RO`, `SE`, `TR`, `ZA` |
| Home Supplies | `5` | `AE`, `AR`, `AT`, `AU`, `BD`, `BE`, `BR`, `CA`, `CH`, `CL`, `CO`, `CZ`, `DE`, `DK`, `EC`, `EG`, `ES`, `FI`, `FR`, `GR`, `HU`, `IE`, `IL`, `IQ`, `IT`, `JP`, `KH`, `KR`, `KZ`, `MA`, `MX`, `NL`, `NO`, `NZ`, `PE`, `PK`, `PL`, `PT`, `RO`, `SE`, `TR`, `ZA` |
| Household Appliances | `14` | `AE`, `AR`, `AT`, `AU`, `BD`, `BE`, `BR`, `CA`, `CH`, `CL`, `CO`, `CZ`, `DE`, `DK`, `EC`, `EG`, `ES`, `FI`, `FR`, `GR`, `HU`, `IE`, `IL`, `IQ`, `IT`, `JP`, `KH`, `KR`, `KZ`, `MA`, `MX`, `NL`, `NO`, `NZ`, `PE`, `PK`, `PL`, `PT`, `RO`, `SE`, `TR`, `ZA` |
| Jewelry Accessories & Derivatives | `32` | `AE`, `AR`, `AT`, `AU`, `BD`, `BE`, `BR`, `CA`, `CH`, `CL`, `CO`, `CZ`, `DE`, `DK`, `EC`, `EG`, `ES`, `FI`, `FR`, `GR`, `HU`, `IE`, `IL`, `IQ`, `IT`, `JP`, `KH`, `KR`, `KZ`, `MA`, `MX`, `NL`, `NO`, `NZ`, `PE`, `PK`, `PL`, `PT`, `RO`, `SE`, `TR`, `ZA` |
| Kid's Fashion | `2` | `AE`, `AR`, `AT`, `AU`, `BD`, `BE`, `BR`, `CA`, `CH`, `CL`, `CO`, `CZ`, `DE`, `DK`, `EC`, `EG`, `ES`, `FI`, `FR`, `GR`, `HU`, `IE`, `IL`, `IQ`, `IT`, `JP`, `KH`, `KR`, `KZ`, `MA`, `MX`, `NL`, `NO`, `NZ`, `PE`, `PK`, `PL`, `PT`, `RO`, `SE`, `TR`, `ZA` |
| Kitchenware | `21` | `AE`, `AR`, `AT`, `AU`, `BD`, `BE`, `BR`, `CA`, `CH`, `CL`, `CO`, `CZ`, `DE`, `DK`, `EC`, `EG`, `ES`, `FI`, `FR`, `GR`, `HU`, `IE`, `IL`, `IQ`, `IT`, `JP`, `KH`, `KR`, `KZ`, `MA`, `MX`, `NL`, `NO`, `NZ`, `PE`, `PK`, `PL`, `PT`, `RO`, `SE`, `TR`, `ZA` |
| Luggage & Bags | `30` | `AE`, `AR`, `AT`, `AU`, `BD`, `BE`, `BR`, `CA`, `CH`, `CL`, `CO`, `CZ`, `DE`, `DK`, `EC`, `EG`, `ES`, `FI`, `FR`, `GR`, `HU`, `IE`, `IL`, `IQ`, `IT`, `JP`, `KH`, `KR`, `KZ`, `MA`, `MX`, `NL`, `NO`, `NZ`, `PE`, `PK`, `PL`, `PT`, `RO`, `SE`, `TR`, `ZA` |
| Menswear & Underwear | `8` | `AE`, `AR`, `AT`, `AU`, `BD`, `BE`, `BR`, `CA`, `CH`, `CL`, `CO`, `CZ`, `DE`, `DK`, `EC`, `EG`, `ES`, `FI`, `FR`, `GR`, `HU`, `IE`, `IL`, `IQ`, `IT`, `JP`, `KH`, `KR`, `KZ`, `MA`, `MX`, `NL`, `NO`, `NZ`, `PE`, `PK`, `PL`, `PT`, `RO`, `SE`, `TR`, `ZA` |
| Muslim Fashion | `34` | `AE`, `AR`, `AT`, `AU`, `BD`, `BE`, `BR`, `CA`, `CH`, `CL`, `CO`, `CZ`, `DE`, `DK`, `EC`, `EG`, `ES`, `FI`, `FR`, `GR`, `HU`, `IE`, `IL`, `IQ`, `IT`, `JP`, `KH`, `KR`, `KZ`, `MA`, `MX`, `NL`, `NO`, `NZ`, `PE`, `PK`, `PL`, `PT`, `RO`, `SE`, `TR`, `ZA` |
| Others | `29` | `AU`, `BR`, `CA`, `DE`, `ES`, `FR`, `GB`, `ID`, `IT`, `JP`, `KR`, `MX`, `MY`, `PH`, `SG`, `TH`, `TW`, `US`, `VN` |
| Pet Supplies | `9` | `AE`, `AR`, `AT`, `AU`, `BD`, `BE`, `BR`, `CA`, `CH`, `CL`, `CO`, `CZ`, `DE`, `DK`, `EC`, `EG`, `ES`, `FI`, `FR`, `GR`, `HU`, `IE`, `IL`, `IQ`, `IT`, `JP`, `KH`, `KR`, `KZ`, `MA`, `MX`, `NL`, `NO`, `NZ`, `PE`, `PK`, `PL`, `PT`, `RO`, `SE`, `TR`, `ZA` |
| Phones & Electronics | `22` | `AE`, `AR`, `AT`, `AU`, `BD`, `BE`, `BR`, `CA`, `CH`, `CL`, `CO`, `CZ`, `DE`, `DK`, `EC`, `EG`, `ES`, `FI`, `FR`, `GR`, `HU`, `IE`, `IL`, `IQ`, `IT`, `JP`, `KH`, `KR`, `KZ`, `MA`, `MX`, `NL`, `NO`, `NZ`, `PE`, `PK`, `PL`, `PT`, `RO`, `SE`, `TR`, `ZA` |
| Pre-Owned | `11` | `AE`, `AR`, `AT`, `AU`, `BD`, `BE`, `BR`, `CA`, `CH`, `CL`, `CO`, `CZ`, `DE`, `DK`, `EC`, `EG`, `ES`, `FI`, `FR`, `GR`, `HU`, `IE`, `IL`, `IQ`, `IT`, `JP`, `KH`, `KR`, `KZ`, `MA`, `MX`, `NL`, `NO`, `NZ`, `PE`, `PK`, `PL`, `PT`, `RO`, `SE`, `TR`, `ZA` |
| Restaurant & bar | `26` | `AU`, `BR`, `CA`, `DE`, `ES`, `FR`, `GB`, `ID`, `IT`, `JP`, `KR`, `MX`, `MY`, `PH`, `SG`, `TH`, `TW`, `US`, `VN` |
| Service | `12` | `AE`, `AR`, `AT`, `AU`, `BD`, `BE`, `BR`, `CA`, `CH`, `CL`, `CO`, `CZ`, `DE`, `DK`, `EC`, `EG`, `ES`, `FI`, `FR`, `GR`, `HU`, `IE`, `IL`, `IQ`, `IT`, `JP`, `KH`, `KR`, `KZ`, `MA`, `MX`, `NL`, `NO`, `NZ`, `PE`, `PK`, `PL`, `PT`, `RO`, `SE`, `TR`, `ZA` |
| Shoes | `17` | `AE`, `AR`, `AT`, `AU`, `BD`, `BE`, `BR`, `CA`, `CH`, `CL`, `CO`, `CZ`, `DE`, `DK`, `EC`, `EG`, `ES`, `FI`, `FR`, `GR`, `HU`, `IE`, `IL`, `IQ`, `IT`, `JP`, `KH`, `KR`, `KZ`, `MA`, `MX`, `NL`, `NO`, `NZ`, `PE`, `PK`, `PL`, `PT`, `RO`, `SE`, `TR`, `ZA` |
| Sports & Outdoor | `35` | `AE`, `AR`, `AT`, `AU`, `BD`, `BE`, `BR`, `CA`, `CH`, `CL`, `CO`, `CZ`, `DE`, `DK`, `EC`, `EG`, `ES`, `FI`, `FR`, `GR`, `HU`, `IE`, `IL`, `IQ`, `IT`, `JP`, `KH`, `KR`, `KZ`, `MA`, `MX`, `NL`, `NO`, `NZ`, `PE`, `PK`, `PL`, `PT`, `RO`, `SE`, `TR`, `ZA` |
| Textiles & Soft Furnishings | `15` | `AE`, `AR`, `AT`, `AU`, `BD`, `BE`, `BR`, `CA`, `CH`, `CL`, `CO`, `CZ`, `DE`, `DK`, `EC`, `EG`, `ES`, `FI`, `FR`, `GR`, `HU`, `IE`, `IL`, `IQ`, `IT`, `JP`, `KH`, `KR`, `KZ`, `MA`, `MX`, `NL`, `NO`, `NZ`, `PE`, `PK`, `PL`, `PT`, `RO`, `SE`, `TR`, `ZA` |
| Tools & Hardware | `19` | `AE`, `AR`, `AT`, `AU`, `BD`, `BE`, `BR`, `CA`, `CH`, `CL`, `CO`, `CZ`, `DE`, `DK`, `EC`, `EG`, `ES`, `FI`, `FR`, `GR`, `HU`, `IE`, `IL`, `IQ`, `IT`, `JP`, `KH`, `KR`, `KZ`, `MA`, `MX`, `NL`, `NO`, `NZ`, `PE`, `PK`, `PL`, `PT`, `RO`, `SE`, `TR`, `ZA` |
| Toys & Hobbies | `18` | `AE`, `AR`, `AT`, `AU`, `BD`, `BE`, `BR`, `CA`, `CH`, `CL`, `CO`, `CZ`, `DE`, `DK`, `EC`, `EG`, `ES`, `FI`, `FR`, `GR`, `HU`, `IE`, `IL`, `IQ`, `IT`, `JP`, `KH`, `KR`, `KZ`, `MA`, `MX`, `NL`, `NO`, `NZ`, `PE`, `PK`, `PL`, `PT`, `RO`, `SE`, `TR`, `ZA` |
| Travel & hotel | `28` | `AU`, `BR`, `CA`, `DE`, `ES`, `FR`, `GB`, `ID`, `IT`, `JP`, `KR`, `MX`, `MY`, `PH`, `SG`, `TH`, `TW`, `US`, `VN` |
| Virtual Products | `6` | `AE`, `AR`, `AT`, `AU`, `BD`, `BE`, `BR`, `CA`, `CH`, `CL`, `CO`, `CZ`, `DE`, `DK`, `EC`, `EG`, `ES`, `FI`, `FR`, `GR`, `HU`, `IE`, `IL`, `IQ`, `IT`, `JP`, `KH`, `KR`, `KZ`, `MA`, `MX`, `NL`, `NO`, `NZ`, `PE`, `PK`, `PL`, `PT`, `RO`, `SE`, `TR`, `ZA` |
| Womenswear & Underwear | `4` | `AE`, `AR`, `AT`, `AU`, `BD`, `BE`, `BR`, `CA`, `CH`, `CL`, `CO`, `CZ`, `DE`, `DK`, `EC`, `EG`, `ES`, `FI`, `FR`, `GR`, `HU`, `IE`, `IL`, `IQ`, `IT`, `JP`, `KH`, `KR`, `KZ`, `MA`, `MX`, `NL`, `NO`, `NZ`, `PE`, `PK`, `PL`, `PT`, `RO`, `SE`, `TR`, `ZA` |

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/tto/tcm/anchor/create/' \
--header 'Access-Token: {{access_token}}' \
--header 'Content-Type: application/json' \
--data '{
    "tto_tcm_account_id": "{{tto_tcm_account_id}}",
    "anchor_type": "WEB_ANCHOR",
    "anchor_sub_type": "DESTINATION",
    "category_label_id": 3,
    "country_code": "AU",
    "call_to_action": {
        "landing_page_url": "{{landing_page_url}}"
    },
    "anchor_title": "WATCH_NOW",
    "anchor_name": "WEB_DESTINATION",
    "upload_type": "UPLOAD_BY_URL",
    "thumbnail_url": "{{thumbnail_url}}"
}'
```
## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|code |number|Response code. For the complete list of response codes and descriptions, see [Appendix-Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message|string|Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|request_id |string|The log ID of a request, which uniquely identifies the request.  |
|data |object|Returned data.|
#|anchor_id|string|The ID of the anchor.|
#|status|string|The status of the anchor.<br><br>Enum value: <ul><li>`IN_REVIEW`: under review.</li></ul>|
#|anchor_type|string|The type of anchor.<br><br>Enum value: <ul><li>`WEB_ANCHOR`: Webpage anchor. An anchor type through which you can display your website link above the creator's video description.</li></ul>|
#|anchor_sub_type|string|The specific type of webpage anchor.<br><br>Enum value: <ul><li>`DESTINATION`: Web destination link. This type directs viewers to a web destination link that can be opened in TikTok. The anchor shows up both in the creator's video and the comment section.</li></ul>|
#|category_label_id|number|The ID of the category of your product or service.<br><br>To learn about the supported values, see <a href="#item-link-Supported values for category_label_id">Supported values for `category_label_id`</a>.|
#|country_code|string|The code of the country or region. <br>The app information from this country or region's app store will be used. This anchor won’t be available in other countries or regions.<br><br>To learn about the country or region that the code represents, see [Location code](../15-appendix/phu-luc-p1.md#doc-1737585867307010).<br><br>Example: `AU`.|
#|call_to_action|object|Anchor link information.|
##|landing_page_url|string|The URL of the page that the anchor will redirect viewers to. This page shows more information about your product or service.|
#|anchor_title|string|The title of the anchor.|
#|anchor_name|string|The name of the anchor.|
#|anchor_sub_title|string|When `anchor_sub_type` is `DESTINATION`, this field returns an empty string (`""`). <br><br>The title of the anchor, which is used to tell TikTok users what you're promoting about your product or service.|
#|thumbnail_url|string|The thumbnail URL for the anchor. <br><br>The URL won't expire.|

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "anchor_id": "{{anchor_id}}",
        "anchor_name": "WEB_DESTINATION",
        "anchor_sub_title": "",
        "anchor_sub_type": "DESTINATION",
        "anchor_title": "Watch Now",
        "anchor_type": "WEB_ANCHOR",
        "call_to_action": {
            "landing_page_url": "{{landing_page_url}}"
        },
        "category_label_id": 3,
        "country_code": "AU",
        "status": "IN_REVIEW",
        "thumbnail_url": "{{thumbnail_url}}"
    }
}
```

---

<a id="doc-1826564965840066"></a>
<!-- doc_id: 1826564965840066 -->
<!-- doc_id: 1826564965840066 -->
# Get webpage anchors
> Đường dẫn: API Reference > TikTok One > Get webpage anchors
Sử dụng endpoint này để truy xuất existing webpage anchors within your TikTok One (TTO) Creator Marketplace account.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/tto/tcm/anchor/get/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Access token authorized by a TikTok One Creator Marketplace account. ⏎ Để biết chi tiết, xem [Authentication](../10-organic-api/tiktok-one-api.md#doc-1825117875361793). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
| tto_tcm_account_id ***(Bắt buộc)*** | string | The ID of the TTO Creator Marketplace account.<br><br>To obtain the IDs of the accounts that you can access via `Access-Token`, use [/tto/oauth2/tcm/](68-tiktok-one-p1.md#doc-1815693478150146). |
|anchor_ids|string[]|A list of anchor IDs.<br><br>Kích thước tối đa: 100.<br><br>If `anchor_ids` is not passed, all anchors within the TTO Creator Marketplace account will be returned.|
|page|integer|Current Số trang cần lấy dữ liệu.<br><br>Value range: ≥ 1.<br>Giá trị mặc định: 1.|
|page_size|integer|Page size.<br><br>Value range: 1-50.<br>Giá trị mặc định: 10.|

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/tto/tcm/anchor/get/?tto_tcm_account_id={{tto_tcm_account_id}}&page=1&page_size=50' \
--header 'Access-Token: {{access_token}}'
```
## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|code |number|Response code. For the complete list of response codes and descriptions, see [Appendix-Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message|string|Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|request_id |string|The log ID of a request, which uniquely identifies the request.  |
|data |object|Returned data.|
#|anchors|object[]|A list of anchors.|
##|anchor_id|string|The ID of the anchor.|
##|status|string|The status of the anchor.<br><br>Enum value: <ul><li>`DRAFT`: The anchor is in draft mode.</li><li>`CREATED`: The anchor has been created but has not been under review.</li><li>`IN_REVIEW`: The anchor is under review.</li><li>`APPROVED`: The anchor has passed review.</li><li>`REJECTED_BY_AUDIT`: The anchor was rejected during the review.</li></ul>|
##|anchor_type|string|The type of anchor.<br><br>Enum value: <ul><li>`WEB_ANCHOR`: Webpage anchor. A type of anchor through which you can display your website link above the creator's video description.</li></ul>|
##|anchor_sub_type|string|Returned when `anchor_type` is `WEB_ANCHOR`. The specific type of webpage anchor.<br><br>Enum value: <ul><li>`DESTINATION`: Web destination link. This type directs viewers to a web destination link that can be opened in TikTok. The anchor shows up both in the creator's video and the comment section.</li><li>`ECOMMERCE`: E-commerce template. This type directs viewers to an internal landing page where brands can add a coupon link. The anchor shows up only in the creator's video comment section.</li><li>`ENTERTAINMENT`: Entertainment template. This type directs viewers to an internal landing page where brands can add a video clip. The anchor shows up only in the creator's video comment section.</li></ul>|
##|country_code|string|The code of the country or region. The app information from this country or region's app store will be used. This anchor won’t be available in other countries or regions.<br><br>To learn about the country or region that the code represents, see [Location code](../15-appendix/phu-luc-p1.md#doc-1737585867307010).|
##|call_to_action|object|Anchor link information.|
###|landing_page_url|string|The URL of the page that the anchor will redirect viewers to. This page shows more information about your product or service.|
###|ios_download_link|string|The iOS download link where people can download your app. <br><br>When `anchor_type` is `WEB_ANCHOR`, this field will be null.|
###|ios_deep_link|string|The iOS download deeplink where people can download your app. <br><br>When `anchor_type` is `WEB_ANCHOR`, this field will be null.|
###|android_download_link|string|The Android download link where people can download your app.<br><br> When `anchor_type` is `WEB_ANCHOR`, this field will be null.|
###|android_deep_link|string|The Android download deeplink where people can download your app. <br><br>When `anchor_type` is `WEB_ANCHOR`, this field will be null.|
##|anchor_title|string|The title of the anchor.|
##|anchor_name|string|The name of the anchor.|
##|anchor_sub_title|string|The title of the anchor, which is used to tell TikTok users what you're promoting about your product or service.<br><br> When `anchor_sub_type` is `DESTINATION`, this field will be null.|
##|thumbnail_url|string|The thumbnail URL for the anchor.|
##|coupon_link|object|This field returns a non-null value only when `anchor_sub_type` is `ECOMMERCE`. <br><br>Information about the coupon link that redirects users to a page with more information about your campaign discount.|
###|discount|number|Discount.<br><br>For instance, a `discount` of `5` means 5% off.|
###|coupon_url|string|Coupon URL.|
###|coupon_code|string|Coupon code.|
##|pixel_id|string|The ID of the pixel that measures and analyzes campaign performance.|
##|creator_preview_url|string|The preview URL of the anchor and landing page that you can use for mobile phone preview purposes.<br><br> The URL won't expire.|
##|advertiser_preview_url|string|The mobile preview URL of the anchor and landing page that you can use for desktop preview purposes. <br><br>The URL won't expire. <br><br>When `anchor_sub_type` is `DESTINATION`, this field will be null.|
#|page_info|object|Pagination Information.|
##|page|number|Current Số trang cần lấy dữ liệu.|
##|page_size|number|Current page size.|
##|total_number|number|Tổng số kết quả tìm thấy.|
##|total_page|number|Tổng số trang.|

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "anchors": [
            {
                "advertiser_preview_url": "{{advertiser_preview_url}}",
                "anchor_id": "{{anchor_id}}",
                "anchor_name": "{{anchor_name}}",
                "anchor_sub_title": "{{anchor_sub_title}}",
                "anchor_sub_type": "ENTERTAINMENT",
                "anchor_title": "{{anchor_title}}",
                "anchor_type": "WEB_ANCHOR",
                "call_to_action": {
                    "android_deep_link": null,
                    "android_download_link": null,
                    "ios_deep_link": null,
                    "ios_download_link": null,
                    "landing_page_url": "{{landing_page_url}}"
                },
                "country_code": "TW",
                "coupon_link": null,
                "creator_preview_url": "{{creator_preview_url}}",
                "pixel_id": null,
                "status": "IN_REVIEW",
                "thumbnail_url": "{{thumbnail_url}}"
            },
            {
                "advertiser_preview_url": "{{advertiser_preview_url}}",
                "anchor_id": "{{anchor_id}}",
                "anchor_name": "{{anchor_name}}",
                "anchor_sub_title": "{{anchor_sub_title}}",
                "anchor_sub_type": "ECOMMERCE",
                "anchor_title": "{{anchor_title}}",
                "anchor_type": "WEB_ANCHOR",
                "call_to_action": {
                    "android_deep_link": null,
                    "android_download_link": null,
                    "ios_deep_link": null,
                    "ios_download_link": null,
                    "landing_page_url": "{{landing_page_url}}"
                },
                "country_code": "US",
                "coupon_link": {
                    "coupon_code": "",
                    "coupon_url": "",
                    "discount": 5
                },
                "creator_preview_url": "{{creator_preview_url}}",
                "status": "IN_REVIEW",
                "thumbnail_url": "{{thumbnail_url}}"
            },
            {
                "advertiser_preview_url": null,
                "anchor_id": "{{anchor_id}}",
                "anchor_name": "{{anchor_name}}",
                "anchor_sub_title": null,
                "anchor_sub_type": "DESTINATION",
                "anchor_title": "Watch Now",
                "anchor_type": "WEB_ANCHOR",
                "call_to_action": {
                    "android_deep_link": null,
                    "android_download_link": null,
                    "ios_deep_link": null,
                    "ios_download_link": null,
                    "landing_page_url": "{{landing_page_url}}"
                },
                "country_code": "CA",
                "coupon_link": null,
                "creator_preview_url": "{{creator_preview_url}}",
                "pixel_id": "7258197703320944642",
                "status": "IN_REVIEW",
                "thumbnail_url": "{{thumbnail_url}}"
            }
        ],
        "page_info": {
            "page": 1,
            "page_size": 50,
            "total_number": 3,
            "total_page": 1
        }
    }
}
```

---

<a id="doc-1826564985760770"></a>
<!-- doc_id: 1826564985760770 -->
<!-- doc_id: 1826564985760770 -->
# Delete a draft anchor
> Đường dẫn: API Reference > TikTok One > Delete a draft anchor
Sử dụng endpoint này để xóa an anchor in draft mode that was created on the [TikTok One](https://ads.tiktok.com/creative) platform.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/tto/tcm/anchor/delete/

**Method** POST

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Access token authorized by a TikTok One Creator Marketplace account. ⏎ Để biết chi tiết, xem [Authentication](../10-organic-api/tiktok-one-api.md#doc-1825117875361793). |
| Content-Type  ****(Bắt buộc)**** | string | Định dạng dữ liệu yêu cầu. ⏎ Allowed format: `application/json`. |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
| tto_tcm_account_id ***(Bắt buộc)*** | string | The ID of the TTO Creator Marketplace account.<br><br>To obtain the IDs of the accounts that you can access via `Access-Token`, use [/tto/oauth2/tcm/](68-tiktok-one-p1.md#doc-1815693478150146). |
|anchor_id ***(Bắt buộc)***|string|Anchor ID.<br><br>To obtain a draft anchor within your TikTok One (TTO) Creator Marketplace account, use [/tto/tcm/anchor/get/](68-tiktok-one-p2.md#doc-1826564965840066) and confirm that the `status` of the anchor is `DRAFT`.|

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/tto/tcm/anchor/delete/' \
--header 'Access-Token: {{Access_Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "tto_tcm_account_id" : "{{tto_tcm_account_id}}",
    "anchor_id" : "{{anchor_id}}"
}'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|code |number|Response code. For the complete list of response codes and descriptions, see [Appendix-Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message|string|Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|request_id |string|The log ID of a request, which uniquely identifies the request.  |
|data |object|Returned data.|

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {}
}
```

---

<a id="doc-1836584318657537"></a>
<!-- doc_id: 1836584318657537 -->
<!-- doc_id: 1836584318657537 -->
# Join a TTO Creator Marketplace campaign as a creator
> Đường dẫn: API Reference > TikTok One > Join a TTO Creator Marketplace campaign as a creator
Use this endpoint to join a TikTok One (TTO) Creator Marketplace campaign as a TikTok creator.

After you join the campaign, you can use publish video posts using [/business/video/publish/](01-accounts-p1.md#doc-1762228496095234) and link the videos to the campaign using [/tto/creator/campaign/video/link/](68-tiktok-one-p2.md#doc-1836584551347201).

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/tto/creator/campaign/join/

**Method** POST

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Access token authorized by TikTok creators. ⏎ Use [/tt_user/oauth2/token/](https://business-api.tiktok.com/portal/docs/get-renew-or-revoke-a-creator-access-token/v1.3#item-link-Obtain%20a%20Creator%20access%20token) or [/tt_user/oauth2/refresh_token/](https://business-api.tiktok.com/portal/docs/get-renew-or-revoke-a-creator-access-token/v1.3#item-link-Renew%20a%20Creator%20access%20token) endpoint to get or renew an access token. |
| Content-Type  ****(Bắt buộc)**** | string | Định dạng dữ liệu yêu cầu. ⏎ Allowed format: `application/json`. |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
|creator_id ***(Bắt buộc)***|string|Application specific unique ID of the TikTok account.<br><br> Pass the value of the `open_id` field returned in the response of [/tt_user/oauth2/token/](68-tiktok-one-p1.md#doc-1768493902119937) or [/tt_user/oauth2/refresh_token/](68-tiktok-one-p1.md#doc-1768493902119937) to this field.|
| tto_invite_link ***(Bắt buộc)*** | string | An invite link that is associated with a TTO Creator Marketplace campaign.<br><br>To create a TTO Creator Marketplace campaign and obtain the associated invite link, use [/tto/tcm/campaign/create/](68-tiktok-one-p1.md#doc-1815693549459458). <br><br><p><span style="color:darkred"><b>Note</b></span>: <ul><li> If the invite link is a campaign level invite link (the `campaign_type` of the associated campaign is `CAMPAIGN`), the creator should be one of the creators invited to the campaign. To confirm this, use [/tto/tcm/campaign/](68-tiktok-one-p1.md#doc-1815693562720258) and check Liệu returned `handle_names` includes the handle name of the creator (`creator_id`).</li><li> If the invite link is a brand level invite link (the `campaign_type` of the associated campaign is `BRAND`), the creator can be any TTO creator.</li></ul> |

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/tto/creator/campaign/join/' \
--header 'Access-Token: "{{Access-Token}}"' \
--header 'Content-Type: application/json' \
--data '{
    "creator_id": "{{creator_id}}",
    "tto_invite_link": "{{tto_invite_link}}"
}'
```
## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|code |number|Response code. For the complete list of response codes and descriptions, see [Appendix-Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message|string|Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|request_id |string|The log ID of a request, which uniquely identifies the request.  |
|data |object|Returned data. <br> <br>For a successful request, this field will be an empty object (`{}`).|

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {}
}
```

---

<a id="doc-1836584551347201"></a>
<!-- doc_id: 1836584551347201 -->
<!-- doc_id: 1836584551347201 -->
# Link a video to a TTO Creator Marketplace campaign as a creator
> Đường dẫn: API Reference > TikTok One > Link a video to a TTO Creator Marketplace campaign as a creator
Use this endpoint to link a video to a TikTok One (TTO) Creator Marketplace campaign as a TikTok creator.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/tto/creator/campaign/video/link/

**Method** POST

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Access token authorized by TikTok creators. ⏎ Use [/tt_user/oauth2/token/](https://business-api.tiktok.com/portal/docs/get-renew-or-revoke-a-creator-access-token/v1.3#item-link-Obtain%20a%20Creator%20access%20token) or [/tt_user/oauth2/refresh_token/](https://business-api.tiktok.com/portal/docs/get-renew-or-revoke-a-creator-access-token/v1.3#item-link-Renew%20a%20Creator%20access%20token) endpoint to get or renew an access token. |
| Content-Type  ****(Bắt buộc)**** | string | Định dạng dữ liệu yêu cầu. ⏎ Allowed format: `application/json`. |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
|creator_id ***(Bắt buộc)***|string|Application specific unique ID of the TikTok account.<br><br> Pass the value of the `open_id` field returned in the response of [/tt_user/oauth2/token/](68-tiktok-one-p1.md#doc-1768493902119937) or [/tt_user/oauth2/refresh_token/](68-tiktok-one-p1.md#doc-1768493902119937) to this field.|
| tto_invite_link ***(Bắt buộc)*** | string | An invite link that is associated with a TTO Creator Marketplace campaign.<br><br>To create a TTO Creator Marketplace campaign and obtain the associated invite link, use [/tto/tcm/campaign/create/](68-tiktok-one-p1.md#doc-1815693549459458). <br><br><p><span style="color:darkred"><b>Note</b></span>: <ul><li> If the invite link is a campaign level invite link (the `campaign_type` of the associated campaign is `CAMPAIGN`), the creator should be one of the creators invited to the campaign. To confirm this, use [/tto/tcm/campaign/](68-tiktok-one-p1.md#doc-1815693562720258) and check Liệu returned `handle_names` includes the handle name of the creator (`creator_id`).</li><li> If the invite link is a brand level invite link (the `campaign_type` of the associated campaign is `BRAND`), the creator can be any TTO creator.</li></ul> |
| video_id***(Bắt buộc)***  | string | The ID of a video posted by the TTO creator.<br><br>To obtain a list of videos posted by a TTO creator, use [/tto/creator/authorized/video/list/](68-tiktok-one-p1.md#doc-1834913554657282). <br>To publish a video post from the TikTok account of a TTO creator, use [/business/video/publish/](01-accounts-p1.md#doc-1762228496095234).<br><br><p><span style="color:darkred"><b>Note</b></span>: The ID cannot be of a video that has been linked to an existing TTO Creator Marketplace campaign. |

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/tto/creator/campaign/video/link/' \
--header 'Access-Token: "{{Access-Token}}"' \
--header 'Content-Type: application/json' \
--data '{
    "creator_id": "{{creator_id}}",
    "tto_invite_link": "{{tto_invite_link}}",
    "video_id": "{{video_id}}"
}'
```
## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|code |number|Response code. For the complete list of response codes and descriptions, see [Appendix-Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message|string|Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|request_id |string|The log ID of a request, which uniquely identifies the request.  |
|data |object|Returned data. <br> <br>For a successful request, this field will be an empty object (`{}`).|

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {}
}
```

---

<a id="doc-1837247726007298"></a>
<!-- doc_id: 1837247726007298 -->
<!-- doc_id: 1837247726007298 -->
# Get TTO video linking requests as a creator
> Đường dẫn: API Reference > TikTok One > Get TTO video linking requests as a creator
Sử dụng endpoint này để truy xuất the requests for linking your public videos to TikTok One (TTO) Creator Marketplace campaigns.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/tto/creator/link/request/get/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Access token authorized by TikTok creators. ⏎ Use [/tt_user/oauth2/token/](https://business-api.tiktok.com/portal/docs/get-renew-or-revoke-a-creator-access-token/v1.3#item-link-Obtain%20a%20Creator%20access%20token) or [/tt_user/oauth2/refresh_token/](https://business-api.tiktok.com/portal/docs/get-renew-or-revoke-a-creator-access-token/v1.3#item-link-Renew%20a%20Creator%20access%20token) endpoint to get or renew an access token. |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
|creator_id ***(Bắt buộc)***|string|Application specific unique ID of the TikTok account.<br><br> Pass the value of the `open_id` field returned in the response of [/tt_user/oauth2/token/](68-tiktok-one-p1.md#doc-1768493902119937) or [/tt_user/oauth2/refresh_token/](68-tiktok-one-p1.md#doc-1768493902119937) to this field.|
| tto_invite_link ***(Bắt buộc)*** | string | The invite link associated with a TTO Creator Marketplace campaign that the creator (TikTok account) has been invited to.<br><br>To create a TTO Creator Marketplace campaign as a brand and obtain the associated invite link, use  [/tto/tcm/campaign/create/](68-tiktok-one-p1.md#doc-1815693549459458). |

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/tto/creator/link/request/get/?creator_id={{creator_id}}&tto_invite_link={{tto_invite_link}}' \
--header 'Access-Token: {{Access-Token}}'
```
## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|code |number|Response code. For the complete list of response codes and descriptions, see [Appendix-Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message|string|Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|request_id |string|The log ID of a request, which uniquely identifies the request.  |
|data |object|Returned data. |
#| campaign_id | string | The ID of the TTO Creator Marketplace campaign. |
#| spark_authorization_days | number | The default Spark Ads authorization days for videos uploaded to the campaign.<br><br>Các giá trị enum hỗ trợ: 0, 7, 30, 60, 180, 365. |
#| link_requests | object[] | A list of linking requests that the creator has received. |
##| video_id | string | The ID of the creator video that has been requested to be linked to the campaign. |
##| link_request_id | string | The ID of the linking request.<br><br>You can pass the ID to [/tto/creator/link/request/confirm/](68-tiktok-one-p2.md#doc-1837247744649345) to approve or reject the linking request. |

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "campaign_id": "{{campaign_id}}",
        "link_requests": [
            {
                "link_request_id": "{{link_request_id}}",
                "video_id": "{{video_id}}"
            }
        ],
        "spark_authorization_days": 7
    }
}
```

---

<a id="doc-1837247744649345"></a>
<!-- doc_id: 1837247744649345 -->
<!-- doc_id: 1837247744649345 -->
# Approve or reject a TTO video linking request as a creator
> Đường dẫn: API Reference > TikTok One > Approve or reject a TTO video linking request as a creator
Use this endpoint to approve or reject a request for linking your public video to a TikTok One (TTO) Creator Marketplace campaign.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/tto/creator/link/request/confirm/

**Method** POST

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Access token authorized by TikTok creators. ⏎ Use [/tt_user/oauth2/token/](https://business-api.tiktok.com/portal/docs/get-renew-or-revoke-a-creator-access-token/v1.3#item-link-Obtain%20a%20Creator%20access%20token) or [/tt_user/oauth2/refresh_token/](https://business-api.tiktok.com/portal/docs/get-renew-or-revoke-a-creator-access-token/v1.3#item-link-Renew%20a%20Creator%20access%20token) endpoint to get or renew an access token. |
| Content-Type  ****(Bắt buộc)**** | string | Định dạng dữ liệu yêu cầu. ⏎ Allowed format: `application/json`. |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
|creator_id ***(Bắt buộc)***|string|Application specific unique ID of the TikTok account.<br><br> Pass the value of the `open_id` field returned in the response of [/tt_user/oauth2/token/](68-tiktok-one-p1.md#doc-1768493902119937) or [/tt_user/oauth2/refresh_token/](68-tiktok-one-p1.md#doc-1768493902119937) to this field.|
| link_request_id ***(Bắt buộc)*** | string | The ID of the linking request.<br><br>To obtain the ID, use [/tto/creator/link/request/get/](68-tiktok-one-p2.md#doc-1837247726007298) and check the returned `link_request_id`. |
| action ***(Bắt buộc)*** | string | Action to be taken.<br><br>Các giá trị enum hỗ trợ: <ul><li>`APPROVE`: To approve the linking request.</li><li>`REJECT`: To reject the linking request.</li></ul> |

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/tto/creator/link/request/confirm/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "creator_id": "{{creator_id}}",
    "link_request_id": "{{link_request_id}}",
    "action": "APPROVE"
}'
```
## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|code |number|Response code. For the complete list of response codes and descriptions, see [Appendix-Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message|string|Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|request_id |string|The log ID of a request, which uniquely identifies the request.  |
|data |object|Returned data. <br> <br>For a successful request, this field will be an empty object (`{}`).|

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {}
}
```
---

## Hướng dẫn thực hành Data Retrieval (Python & cURL)

Dưới đây là mã nguồn mẫu minh họa quy trình gọi API thực tế cho phân hệ **TikTok One — phần 2/2**:

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

