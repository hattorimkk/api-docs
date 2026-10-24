# Smart+ nâng cấp (Upgraded Smart+) — phần 1/7

> Phân hệ: apiref:Upgraded Smart+.
> Tài liệu biên dịch kỹ thuật chi tiết theo chuẩn TikTok Business API v1.3.

---

## Mục lục điều hướng
- [1. Smart+ nâng cấp (#doc-1843301794874370)](#doc-1843301794874370)
- [2. Chiến dịch (#doc-1843310518576130)](#doc-1843310518576130)
- [3. Lấy danh sách chiến dịch Smart+ nâng cấp (#doc-1843312818332930)](#doc-1843312818332930)
- [4. Tạo chiến dịch Smart+ nâng cấp (#doc-1843312852800706)](#doc-1843312852800706)
- [5. Cập nhật chiến dịch Smart+ nâng cấp (#doc-1843312876001282)](#doc-1843312876001282)
- [6. Cập nhật trạng thái hoạt động của chiến dịch Smart+ nâng cấp (#doc-1843312888885314)](#doc-1843312888885314)
- [7. Tạo tác vụ sao chép bất đồng bộ cho chiến dịch Smart+ nâng cấp (#doc-1866528879472641)](#doc-1866528879472641)
- [8. Lấy kết quả tác vụ sao chép bất đồng bộ cho chiến dịch Smart+ nâng cấp (#doc-1866529943741441)](#doc-1866529943741441)
- [9. Nhóm quảng cáo (#doc-1843310524500993)](#doc-1843310524500993)

---

<a id="doc-1843301794874370"></a>
<!-- doc_id: 1843301794874370 -->
<!-- doc_id: 1843301794874370 -->
# Smart+ nâng cấp (Upgraded Smart+)
> Đường dẫn: API Reference > Smart+ nâng cấp
Chiến dịch Smart+ nâng cấp (Upgraded Smart+ Campaigns) sở hữu quy trình làm việc thống nhất mới, được gọi là trải nghiệm Smart+ nâng cấp (Upgraded Smart+ experience). Quy trình tinh gọn này cho phép bạn tiếp cận cả các tính năng [thủ công](24-campaign.md#doc-1739315728330753) và [Smart+](61-to-be-deprecated-legacy-smartplus.md#doc-1765314260115458) khi tạo chiến dịch. [Tìm hiểu thêm về các nâng cấp cho Smart+](https://ads.tiktok.com/help/article/about-updates-to-smart-plus).

Nhóm này bao gồm các endpoint sau:

**Campaigns**
* [Lấy danh sách chiến dịch Smart+ nâng cấp](62-upgraded-smartplus-p1.md#doc-1843312818332930)
* [Tạo chiến dịch Smart+ nâng cấp](62-upgraded-smartplus-p1.md#doc-1843312852800706)
* [Cập nhật chiến dịch Smart+ nâng cấp](62-upgraded-smartplus-p1.md#doc-1843312876001282)
* [Cập nhật trạng thái hoạt động của chiến dịch Smart+ nâng cấp](62-upgraded-smartplus-p1.md#doc-1843312888885314)
* [Tạo tác vụ sao chép bất đồng bộ cho chiến dịch Smart+ nâng cấp](62-upgraded-smartplus-p1.md#doc-1866528879472641)
* [Lấy kết quả tác vụ sao chép bất đồng bộ cho chiến dịch Smart+ nâng cấp](62-upgraded-smartplus-p1.md#doc-1866529943741441)

**Ad groups**
* [Lấy danh sách nhóm quảng cáo Smart+ nâng cấp](62-upgraded-smartplus-p2.md#doc-1843314879617026)
* [Tạo nhóm quảng cáo Smart+ nâng cấp](62-upgraded-smartplus-p3.md#doc-1843314887930946)
* [Cập nhật nhóm quảng cáo Smart+ nâng cấp](62-upgraded-smartplus-p4.md#doc-1843314894279682)
* [Cập nhật trạng thái hoạt động của nhóm quảng cáo Smart+ nâng cấp](62-upgraded-smartplus-p4.md#doc-1843314908153858)
* [Cập nhật ngân sách của nhóm quảng cáo Smart+ nâng cấp](62-upgraded-smartplus-p4.md#doc-1843314914438466)

**Ads**
* [Lấy danh sách quảng cáo Smart+ nâng cấp](62-upgraded-smartplus-p4.md#doc-1843317378982914)
* [Tạo quảng cáo Smart+ nâng cấp](62-upgraded-smartplus-p5.md#doc-1843317390059522)
* [Cập nhật quảng cáo Smart+ nâng cấp](62-upgraded-smartplus-p6.md#doc-1843317411665921)
* [Cập nhật trạng thái hoạt động của quảng cáo Smart+ nâng cấp](62-upgraded-smartplus-p6.md#doc-1843317423164482)
* [Bật hoặc tắt mẫu quảng cáo trong quảng cáo Smart+ nâng cấp](62-upgraded-smartplus-p6.md#doc-1843317433577601)
* [Xem trước quảng cáo Smart+ nâng cấp](62-upgraded-smartplus-p6.md#doc-1843317445798914)

**Ad review**
* [Lấy thông tin xét duyệt quảng cáo Smart+ nâng cấp](62-upgraded-smartplus-p6.md#doc-1843317465695233)
* [Lấy thông tin xét duyệt mẫu quảng cáo Smart+ nâng cấp](62-upgraded-smartplus-p6.md#doc-1843317474334722)
* [Kháng nghị từ chối duyệt quảng cáo Smart+ nâng cấp](62-upgraded-smartplus-p6.md#doc-1843317522553106)

**Reporting**
* [Chạy báo cáo tổng quan mẫu quảng cáo Smart+ nâng cấp](62-upgraded-smartplus-p6.md#doc-1843317489576961)
* [Chạy báo cáo chi tiết mẫu quảng cáo Smart+ nâng cấp](62-upgraded-smartplus-p7.md#doc-1843317510389761)

---

<a id="doc-1843310518576130"></a>
<!-- doc_id: 1843310518576130 -->
<!-- doc_id: 1843310518576130 -->
# Chiến dịch (Campaigns)
> Đường dẫn: API Reference > Smart+ nâng cấp > Campaigns
Chiến dịch là cấp độ cao nhất trong cấu trúc quảng cáo. Để triển khai quảng bá trên TikTok for Business, trước tiên bạn cần tạo một chiến dịch và thiết lập mục tiêu quảng cáo.

Nhóm này bao gồm các endpoint sau:

* [Lấy danh sách chiến dịch Smart+ nâng cấp](62-upgraded-smartplus-p1.md#doc-1843312818332930)
* [Tạo chiến dịch Smart+ nâng cấp](62-upgraded-smartplus-p1.md#doc-1843312852800706)
* [Cập nhật chiến dịch Smart+ nâng cấp](62-upgraded-smartplus-p1.md#doc-1843312876001282)
* [Cập nhật trạng thái hoạt động của chiến dịch Smart+ nâng cấp](62-upgraded-smartplus-p1.md#doc-1843312888885314)
* [Tạo tác vụ sao chép bất đồng bộ cho chiến dịch Smart+ nâng cấp](62-upgraded-smartplus-p1.md#doc-1866528879472641)
* [Lấy kết quả tác vụ sao chép bất đồng bộ cho chiến dịch Smart+ nâng cấp](62-upgraded-smartplus-p1.md#doc-1866529943741441)

---

<a id="doc-1843312818332930"></a>
<!-- doc_id: 1843312818332930 -->
<!-- doc_id: 1843312818332930 -->
# Lấy danh sách chiến dịch Smart+ nâng cấp (Get Upgraded Smart+ Campaigns)
> Đường dẫn: API Reference > Smart+ nâng cấp > Campaigns > Get Upgraded Smart+ Campaigns
Sử dụng endpoint này để truy xuất danh sách các chiến dịch Smart+ nâng cấp trong tài khoản quảng cáo.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/smart_plus/campaign/get/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id  ****(Bắt buộc)**** | string | ID tài khoản quảng cáo TikTok. |
| fields | string[] | Danh sách các trường bạn muốn lấy. ⏎ Khi không chỉ định, tất cả các trường sẽ được trả về theo mặc định. ⏎ Để biết các trường được phép, xem các trường dưới mục `list` trong phần Dữ liệu phản hồi (Response). |
| page | integer | Số trang hiện tại cần lấy dữ liệu. ⏎ Giá trị mặc định: 1. ⏎ Khoảng giá trị: ≥ 1. |
| page_size | integer | Kích thước trang. ⏎ Giá trị mặc định: 10. ⏎ Khoảng giá trị: 1-1.000. |
| include_effective_status | boolean | Có bao gồm tham số `effective_status` trong phản hồi hay không. ⏎ Các giá trị được hỗ trợ: `true`, `false`. ⏎ Giá trị mặc định: `false`. |
| filtering | object | Điều kiện lọc dữ liệu. ⏎ Example: `filtering={"objective_type":"APP_PROMOTION"}` |
| ↳ campaign_ids | string[] | Lọc theo ID chiến dịch. ⏎ Kích thước tối đa: 100. |
| ↳ campaign_name | string | Lọc theo tên chiến dịch. ⏎ Hỗ trợ so khớp gần đúng (fuzzy match). |
| ↳ creative_campaign_type | string[] | Lọc theo việc chiến dịch có phải là Chiến dịch Quảng cáo Tìm kiếm hay không. ⏎ Giá trị enum: • `SEARCH_CAMPAIGN`: Lọc các Chiến dịch Quảng cáo Tìm kiếm. ⏎ Nếu không chỉ định trường này, bạn sẽ nhận được cả Chiến dịch Quảng cáo Tìm kiếm và chiến dịch thông thường. |
| ↳ effective_statuses | string[] | Lọc theo danh sách trạng thái chiến dịch. ⏎ Các giá trị enum hỗ trợ: • `UNDER_REVIEW`: Đang xét duyệt (Under review). • `NOT_DELIVERED`: Chưa phân phối (Not delivered). • `SCHEDULED`: Đã lên lịch (Scheduled). • `PARTIAL_DELIVERY`: Phân phối một phần (Partial delivery). • `ACTIVE`: Đang hoạt động (Active). • `ENDED`: Đã kết thúc (Ended). • `PAUSED`: Đã tạm dừng (Paused). • `DELETED`: Đã xóa (Deleted). |
| ↳ primary_status | string | Trạng thái chính (Primary status). ⏎ Để xem danh sách giá trị enum, xem [Enumeration-Primary Status](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ secondary_status | string | Lọc theo trạng thái phụ của chiến dịch (Secondary status). ⏎ Để xem danh sách giá trị enum, xem [Enumeration- Campaign Status - Secondary Status](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ objective_type | string | Lọc theo mục tiêu quảng cáo. ⏎ Để xem danh sách giá trị enum, xem [Enumeration-Advertising Objective](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ sales_destination | string | Đích đến bán hàng (Sales destination), nơi bạn muốn thúc đẩy doanh số. ⏎ Các giá trị enum hỗ trợ: • `WEBSITE`: Trang web. Thúc đẩy doanh số trên trang web của bạn. • `APP`: Ứng dụng. Thúc đẩy doanh số trên ứng dụng của bạn (yêu cầu danh mục sản phẩm). • `WEB_AND_APP`: Trang web và ứng dụng. Thúc đẩy doanh số trên cả trang web và ứng dụng. |
| ↳ creation_filter_start_time | string | Thời gian tạo chiến dịch sớm nhất, theo định dạng `YYYY-MM-DD HH:MM:SS` (giờ UTC). Bộ lọc này sẽ truy xuất các chiến dịch được tạo sau thời điểm này. ⏎ Ví dụ: `2025-01-01 00:00:01`. ⏎ Nếu không chỉ định `creation_filter_start_time` và `creation_filter_end_time`, kết quả sẽ bao gồm các chiến dịch được tạo vào bất kỳ lúc nào. ⏎ **Lưu ý**: Để đảm bảo hiệu suất và tốc độ xử lý tác vụ, hãy cân nhắc đặt khoảng thời gian trong vòng 6 tháng cho các bộ lọc thời gian tạo. |
| ↳ creation_filter_end_time | string | Thời gian tạo chiến dịch muộn nhất, theo định dạng `YYYY-MM-DD HH:MM:SS` (giờ UTC). Bộ lọc này sẽ truy xuất các chiến dịch được tạo trước thời điểm này. ⏎ Ví dụ: `2025-02-01 00:00:01`. ⏎ Nếu không chỉ định `creation_filter_start_time` và `creation_filter_end_time`, kết quả sẽ bao gồm các chiến dịch được tạo vào bất kỳ lúc nào. ⏎ **Lưu ý**: Để đảm bảo hiệu suất và tốc độ xử lý tác vụ, hãy cân nhắc đặt khoảng thời gian trong vòng 6 tháng cho các bộ lọc thời gian tạo. |

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/smart_plus/campaign/get/?advertiser_id={{advertiser_id}}&page=1&page_size=1000' \
--header 'Access-Token: {{Access-Token}}'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Mã phản hồi. Để xem danh sách đầy đủ các mã phản hồi và mô tả, xem [Phụ lục - Mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | ID nhật ký (log ID) của yêu cầu, dùng để định danh duy nhất yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ list | object[] | Danh sách các chiến dịch Smart+ nâng cấp. |
| ↳↳ advertiser_id | string | ID tài khoản quảng cáo TikTok. |
| ↳↳ campaign_id | string | ID chiến dịch quảng cáo. |
| ↳↳ create_time | string | Thời điểm chiến dịch được tạo, theo định dạng `YYYY-MM-DD HH:MM:SS` (giờ UTC). |
| ↳↳ modify_time | string | Thời điểm chiến dịch được chỉnh sửa lần gần nhất, theo định dạng `YYYY-MM-DD HH:MM:SS` (giờ UTC). |
| ↳↳ objective_type | string | Advertising objective. ⏎ Để xem danh sách giá trị enum, xem [Enumeration-Advertising Objective](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳↳ app_promotion_type | string | Loại quảng bá ứng dụng. ⏎ Giá trị enum: • `APP_INSTALL`: Cài đặt ứng dụng. Thu hút người dùng mới cài đặt ứng dụng. • `APP_RETARGETING`: Nhắm mục tiêu lại ứng dụng. Tái tương tác người dùng ứng dụng hiện tại để thực hiện hành động trong ứng dụng. • `MINIS`: TikTok Mini hoặc Series. Quảng bá Series, phim ngắn nhiều tập hoặc mini game bằng cách tối ưu hóa lưu lượng truy cập tự nhiên và quảng cáo. |
| ↳↳ sales_destination | string | Đích đến bán hàng (Sales destination), nơi bạn muốn thúc đẩy doanh số. ⏎ Các giá trị enum hỗ trợ: • `WEBSITE`: Trang web. Thúc đẩy doanh số trên trang web. • `APP`: Ứng dụng. Thúc đẩy doanh số trên ứng dụng (yêu cầu danh mục sản phẩm). • `WEB_AND_APP`: Trang web và ứng dụng. Thúc đẩy doanh số trên cả trang web và ứng dụng. |
| ↳↳ campaign_type | string | Loại chiến dịch. ⏎ Hiện tại hỗ trợ `REGULAR_CAMPAIGN` và `IOS14_CAMPAIGN`. |
| ↳↳ app_id | string | App ID của ứng dụng cần quảng bá. ⏎ Để lấy danh sách App ID, sử dụng [/app/list/](43-events-1-0-p1.md#doc-1740859313270786). |
| ↳↳ gaming_ad_compliance_agreement | string | Có thực hiện agree to the Compliance Assurance Policy for Gaming Advertisers on TikTok. ⏎ The policy is as follows: Yo confirms and attest that any gaming application, product or service (game) you desire to advertise on TikTok, including any associated URL(s), (a) complies with all applicable laws and regulations of the jurisdictions where the game can be accessed or played, and upon request, can provide supporting documentation as evidence of why the game is not considered illegal gambling or lottery; and (b) has not been and is not part of any investigation or lawsuit regarding the game's legality or regulatory compliance. ⏎ Các giá trị enum hỗ trợ: • `ON`: To agree to the policy. • `OFF`: To leave the policy not accepted. |
| ↳↳ is_advanced_dedicated_campaign | boolean | Liệu campaign is an Advanced Dedicated Campaign. Advanced Dedicated Campaigns leverage advanced delivery models that benefit from real-time signals. ⏎ Các giá trị được hỗ trợ: `true`, `false`. ⏎ By default, Upgraded Smart+ App Campaigns with iOS 14 dedicated campaign setting enabled are all Advanced Dedicated Campaigns. |
| ↳↳ disable_skan_campaign | boolean | Có thực hiện disable SKAN (SKAdNetwork) attribution, Apple's conversion attribution solution for iOS campaigns. ⏎ Các giá trị enum hỗ trợ: • `true`: To disable SKAN attribution. The campaign will not be bound by [Dedicated Campaign quota limits](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1752256248260610) and you will be able to retrieve [Self Attribution Network (SAN) metrics](../09-marketing-api/bao-cao-p2.md#doc-1751443967255553) for the campaign. However, you cannot retrieve [SKAN reporting metrics](../09-marketing-api/bao-cao-p2.md#doc-1751443967255553) for the campaign. Learn more about [SAN integration](https://ads.tiktok.com/help/article/about-self-attribution-transition). • `false`: To enable SKAN attribution. The campaign will be bound by [Dedicated Campaign quota limits](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1752256248260610) and you will be able to retrieve [SKAN metrics](../09-marketing-api/bao-cao-p2.md#doc-1751443967255553) for the campaign. |
| ↳↳ bid_align_type | string | The attribution type for the Dedicated Campaign. The type determines which attribution network the target CPA (`conversion_bid_price`) or ROAS (`roas_bid`) at the ad group level is based on. ⏎ Các giá trị enum hỗ trợ: • `SAN`: SAN. • `SKAN`: SKAN. |
| ↳↳ campaign_app_profile_page_state | string | Indicates the status of the App Profile Page. ⏎ Các giá trị enum hỗ trợ: `ON`, `OFF`. |
| ↳↳ is_search_campaign | boolean | Liệu campaign is a Search Ads Campaign. ⏎ With Search Ads Campaigns, you set up your campaign to target ads in TikTok search results. Search Ads Campaigns reach those in your audience actively looking for products or information related to your brand. You'll use relevant keywords and search terms to help guide audiences to your ads. ⏎ Các giá trị được hỗ trợ: `true`, `false`. |
| ↳↳ catalog_enabled | boolean | Có thực hiện use your catalog to automatically advertise relevant products or services to people based on their unique interests, intent and actions. ⏎ Các giá trị được hỗ trợ: `true`, `false`. |
| ↳↳ catalog_type | string | The type of catalog. ⏎ Các giá trị enum hỗ trợ: • `ECOMMERCE`: e-commerce • `TRAVEL_ENTERTAINMENT`: travel and entertainment. • `MINI_SERIES`: mini series. • `GENERIC`: generic. • `ONLINE_TO_OFFLINE`: online-to-offline. |
| ↳↳ campaign_name | string | Tên chiến dịch. |
| ↳↳ special_industries | string[] | Ad categories. ⏎ Các giá trị enum hỗ trợ: • `HOUSING`: Ads for real estate listings, homeowners insurance, mortgage loans or other related opportunities. • `EMPLOYMENT`: Ads for job offers, internships, professional certification programs or other related opportunities. • `CREDIT`: Ads for credit card offers, auto loans, long-term financing or other related opportunities. |
| ↳↳ budget_optimize_on | boolean | Liệu CBO is enabled. ⏎ Supported value: `true` (enabled), `false` (disabled). |
| ↳↳ budget_mode | string | Chế độ ngân sách. ⏎ • Khi `budget_optimize_on` là `true` hoặc không chỉ định, các giá trị enum gồm: • `BUDGET_MODE_DYNAMIC_DAILY_BUDGET`: Ngân sách chiến dịch hàng ngày động. Là mức ngân sách hàng ngày trung bình trong một tuần. Chi phí hàng ngày sẽ không vượt quá 125% ngân sách trung bình và chi phí hàng tuần không vượt quá 7 lần ngân sách hàng ngày trung bình. • `BUDGET_MODE_TOTAL`: Ngân sách chiến dịch trọn đời. • Khi `budget_optimize_on` là `false`, các giá trị enum gồm: • `BUDGET_MODE_INFINITE`: Không giới hạn ngân sách cho các nhóm quảng cáo trong chiến dịch này. • `BUDGET_MODE_DAY`: Giới hạn ngân sách hàng ngày cho tất cả các nhóm quảng cáo trong chiến dịch. • `BUDGET_MODE_TOTAL`: Giới hạn tổng ngân sách cho tất cả các nhóm quảng cáo trong chiến dịch. |
| ↳↳ budget_auto_adjust_strategy | string | Returned only when the following conditions are all met: • `budget_optimize_on` is `true` or not specified. • `budget_mode` is `BUDGET_MODE_DYNAMIC_DAILY_BUDGET`. • `app_promotion_type` is not `MINIS`. ⏎ The campaign budget strategy for automatic daily campaign budget. ⏎ Các giá trị enum hỗ trợ: • `AUTO_BUDGET_INCREASE`: To enable Goal-based budget increase. Allow your budget to automatically increase when your ads are performing well and target CPA, Day 0 target ROAS, and budget requirements are met. 	 • When `budget_auto_adjust_strategy` is `AUTO_BUDGET_INCREASE`, the specified `budget` will be the initial daily budget. Your daily budget will be allowed to automatically increase by 20%, up to 10 times per day, when your budget utilization reaches 90% or more. Your daily budget will reset to your original daily budget each day. • `UNSET`: To disable Goal-based budget increase. |
| ↳↳ budget | float | • Khi `budget_optimize_on` là `true` hoặc không chỉ định, trường này đại diện cho ngân sách chiến dịch cố định hoặc ngân sách ban đầu. • Khi `budget_auto_adjust_strategy` là `UNSET`, trường này đại diện cho ngân sách chiến dịch cố định. • Khi `budget_auto_adjust_strategy` là `AUTO_BUDGET_INCREASE`, trường này đại diện cho ngân sách ban đầu. Để lấy ngân sách chiến dịch hiện tại, kiểm tra trường `current_budget` được trả về. • Khi `budget_optimize_on` là `false`, trường này đại diện cho hạn mức cho tất cả nhóm quảng cáo trong chiến dịch. • Khi `budget_mode` là `BUDGET_MODE_DAY`, trường này đại diện cho hạn mức hàng ngày. • Khi `budget_mode` là `BUDGET_MODE_TOTAL`, trường này đại diện cho hạn mức tổng ngân sách. |
| ↳↳ current_budget | float | Chỉ trả về khi `budget_auto_adjust_strategy` là `AUTO_BUDGET_INCREASE`. ⏎ Ngân sách chiến dịch hiện tại cho chiến dịch đã bật tự động tăng ngân sách theo mục tiêu. |
| ↳↳ operation_status | string | Trạng thái hoạt động. ⏎ Các giá trị enum hỗ trợ: • `ENABLE` : The campaign is enabled (in 'ON' status). • `DISABLE`: The campaign is disabled (in 'OFF' status). |
| ↳↳ effective_status | string | Returned only when `effective_status` is `true` in the request. ⏎ The status of the campaign. ⏎ Các giá trị enum hỗ trợ: • `UNDER_REVIEW`: Under review. • `NOT_DELIVERED`: Not delivered. • `SCHEDULED`: Scheduled. • `PARTIAL_DELIVERY`: Partial delivery. • `ACTIVE`: Active. • `ENDED`: Ended. • `PAUSED`: Paused. • `DELETED`: Deleted. |
| ↳↳ secondary_status | string | Campaign secondary status. ⏎ Để xem danh sách giá trị enum, xem [Enumeration- Campaign Status - Secondary Status](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳↳ smart_plus_adgroup_mode | string | The ad group mode for the campaign. ⏎ Các giá trị enum hỗ trợ: • `SINGLE`: You can only create one single ad group within the campaign. • `MULTIPLE`: You can only create multiple ad groups within the campaign. |
| ↳↳ postback_window_mode | string | The mode that determines which SKAN 4.0 postback you want to secure. ⏎ Các giá trị enum hỗ trợ: • `POSTBACK_WINDOW_MODE1`: This option secures the first postback, which corresponds to the 0-2 day attribution window. The data can take up to 4 days to return, and the campaign will wait for 4 days to release the campaign quota. • `POSTBACK_WINDOW_MODE2`: This mode secures the first two postbacks, which correspond to the 3-7 day attribution window. The data can take up to 13 days to return, and the campaign will wait for 13 days to release the campaign quota. • `POSTBACK_WINDOW_MODE3`: This mode secures all three postbacks, which correspond to the 8-35 day attribution window. The data can take up to 41 days to return, and the campaign will wait for 41 days to release the campaign quota. ⏎ **Note**: If you have set up Mobile Measurement Partner (MMP) Tracking with **Adjust**, **Airbridge**, **Appsflyer**, **Branch**, **Kochava**, or **Singular** for your App and your MMP SDK version is updated to a SKAN 4.0 supported SDK, you can transition your App to SKAN 4.0 on Events Manager. To learn about how to set up MMP tracking for your App, see [How to Set Up App Attribution in TikTok Ads Manager](https://ads.tiktok.com/help/article/set-up-app-attribution-tiktok-ads-manager). To learn more about how to transition your App to SKAN 4.0, see [About SKAN 4.0 and TikTok](https://ads.tiktok.com/help/article/about-skan-4-0-and-tiktok) and [How to transition to SKAN 4.0](https://ads.tiktok.com/help/article/how-to-transition-to-skan-4-0). |
| ↳↳ po_number | string | Số đơn đặt hàng (PO - Purchase Order). ⏎ Số PO rất hữu ích cho việc theo dõi và đối soát hóa đơn. ⏎ [Tìm hiểu thêm về số PO trên hóa đơn hàng tháng](https://ads.tiktok.com/help/article/update-po-number-on-monthly-invoices). |
| ↳↳ is_promotional_campaign | boolean | Có thực hiện use promotion campaign settings. ⏎ Enable this feature to activate specialized campaign setup flows and optimization for new releases, event-driven campaigns, theatrical releases, streaming service promotions, events, or time-bound offers. ⏎ Các giá trị được hỗ trợ: `true`, `false`. |
| ↳↳ rta_id | string | ID Realtime API (RTA), mã định danh chiến lược RTA. |
| ↳↳ rta_bid_enabled | boolean | Có thực hiện use RTA bid. ⏎ Các giá trị được hỗ trợ: • `true`: enabled. • `false`: not enabled. |
| ↳↳ rta_product_selection_enabled | boolean | Có thực hiện use RTA to automatically select products. ⏎ Các giá trị enum hỗ trợ: • `true`: enabled. • `false`: not enabled. |
| ↳ page_info | object | Thông tin phân trang. |
| ↳↳ page | number | Số trang hiện tại cần lấy dữ liệu. |
| ↳↳ page_size | number | Kích thước trang. |
| ↳↳ total_number | number | Tổng số kết quả tìm thấy. |
| ↳↳ total_page | number | Tổng số trang kết quả. |

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "list": [
            {
                "advertiser_id": "{{advertiser_id}}",
                "budget": {{budget}},
                "budget_mode": "BUDGET_MODE_DYNAMIC_DAILY_BUDGET",
                "budget_optimize_on": true,
                "campaign_id": "{{campaign_id}}",
                "campaign_name": "{{campaign_name}}",
                "catalog_enabled": false,
                "create_time": "{{create_time}}",
                "modify_time": "{{modify_time}}",
                "objective_type": "LEAD_GENERATION",
                "operation_status": "ENABLE",
                "secondary_status": "CAMPAIGN_STATUS_ENABLE",
                "smart_plus_adgroup_mode": "MULTIPLE"
            },
            {
                "advertiser_id": "{{advertiser_id}}",
                "budget": {{budget}},
                "budget_mode": "BUDGET_MODE_DYNAMIC_DAILY_BUDGET",
                "budget_optimize_on": true,
                "campaign_id": "{{campaign_id}}",
                "campaign_name": "{{campaign_name}}",
                "campaign_type": "REGULAR_CAMPAIGN",
                "create_time": "{{create_time}}",
                "modify_time": "{{modify_time}}",
                "objective_type": "WEB_CONVERSIONS",
                "operation_status": "ENABLE",
                "sales_destination": "WEBSITE",
                "secondary_status": "CAMPAIGN_STATUS_ENABLE",
                "smart_plus_adgroup_mode": "MULTIPLE"
            },
            {
                "advertiser_id": "{{advertiser_id}}",
                "budget": {{budget}},
                "budget_mode": "BUDGET_MODE_DYNAMIC_DAILY_BUDGET",
                "budget_optimize_on": true,
                "campaign_id": "{{campaign_id}}",
                "campaign_name": "{{campaign_name}}",
                "campaign_type": "REGULAR_CAMPAIGN",
                "catalog_enabled": true,
                "catalog_type": "TRAVEL_ENTERTAINMENT",
                "create_time": "{{create_time}}",
                "modify_time": "{{modify_time}}",
                "objective_type": "WEB_CONVERSIONS",
                "operation_status": "ENABLE",
                "sales_destination": "WEBSITE",
                "secondary_status": "CAMPAIGN_STATUS_ENABLE",
                "smart_plus_adgroup_mode": "MULTIPLE"
            },
            {
                "advertiser_id": "{{advertiser_id}}",
                "app_promotion_type": "APP_INSTALL",
                "budget": {{budget}},
                "budget_mode": "BUDGET_MODE_DYNAMIC_DAILY_BUDGET",
                "budget_optimize_on": true,
                "campaign_id": "{{campaign_id}}",
                "campaign_name": "{{campaign_name}}",
                "campaign_type": "REGULAR_CAMPAIGN",
                "create_time": "{{create_time}}",
                "modify_time": "{{modify_time}}",
                "objective_type": "APP_PROMOTION",
                "operation_status": "ENABLE",
                "secondary_status": "CAMPAIGN_STATUS_ENABLE",
                "smart_plus_adgroup_mode": "SINGLE"
            }
        ],
        "page_info": {
            "page": 1,
            "page_size": 1000,
            "total_number": 4,
            "total_page": 1
        }
    }
}
```

---

<a id="doc-1843312852800706"></a>
<!-- doc_id: 1843312852800706 -->
<!-- doc_id: 1843312852800706 -->
# Tạo chiến dịch Smart+ nâng cấp (Create an Upgraded Smart+ Campaign)
> Đường dẫn: API Reference > Smart+ nâng cấp > Campaigns > Create an Upgraded Smart+ Campaign
Sử dụng endpoint này để tạo an Upgraded Smart+ Campaign.

> **Important:** 
> Bắt đầu từ cuối tháng 9 năm 2026, bạn sẽ không còn có thể tạo các chiến dịch VBO Cài đặt ứng dụng không dùng CBO (Tối ưu hóa ngân sách chiến dịch) qua API. Cụ thể, hạn chế này áp dụng cho các chiến dịch có `app_promotion_type` được đặt thành `APP_INSTALL` và `budget_optimize_on` là `false` ở cấp chiến dịch, trong khi `optimization_goal` được đặt thành `VALUE` ở cấp nhóm quảng cáo. Thay đổi này được thực hiện vì các cấu hình này cho thấy hiệu suất phân phối yếu hơn đáng kể so với các chiến dịch sử dụng CBO. Thay đổi này chỉ áp dụng cho việc tạo mới chiến dịch và không ảnh hưởng đến các thiết lập chiến dịch hiện có. Để đảm bảo tích hợp API diễn ra suôn sẻ, chúng tôi khuyến nghị bạn nên bật cài đặt CBO cho các chiến dịch VBO Cài đặt ứng dụng bằng cách đặt `budget_optimize_on` thành `true` ở cấp chiến dịch.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/smart_plus/campaign/create/

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
| request_id  ****(Bắt buộc)**** | string | Request ID with which you can create campaigns with duplicate names. It also supports idempotency to prevent you from sending the same request twice. If you retry requests with the same request ID multiple times, then only one will succeed. ⏎ It is different from the `request_id` returned in the response parameters, which is used to uniquely identify an HTTP request. ⏎ The value should be a string representation of a 64-bit integer number. ⏎ Example: `123456789`. |
| operation_status | string | The status of the campaign when created. ⏎ Các giá trị enum hỗ trợ: • `ENABLE`: The campaign is enabled when created. • `DISABLE`: The campaign is disabled when created. ⏎ Giá trị mặc định: `ENABLE`. |
| objective_type  ****(Bắt buộc)**** | string | Advertising objective. ⏎ Currently, we support `APP_PROMOTION`, `WEB_CONVERSIONS`, and `LEAD_GENERATION`. ⏎ For detailed explanation of enum values, see [Enumeration-Advertising Objective](../15-appendix/phu-luc-p1.md#doc-1737174886619138). ⏎ • To learn about how to create an Upgraded Smart+ App Campaign or Upgraded Smart+ TikTok Growth Max campaign, see [Create Upgraded Smart+ App Campaigns](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1843309500205058) and [Create Upgraded Smart+ Growth Max campaigns](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1868120855134226). • To learn about how to create an Upgraded Smart+ Web Campaign, see [Create Upgraded Smart+ Web Campaigns](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1843309514567809). • To learn about how to create an Upgraded Smart+ Lead Generation Campaign, see [Create Upgraded Smart+ Lead Generation Campaigns](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1843324498993154). |
| app_promotion_type **(Điều kiện)** | string | Bắt buộc khi `objective_type` is `APP_PROMOTION`. ⏎ App promotion type. ⏎ Enum value: • `APP_INSTALL`: App install. Get new users to install your app. • `APP_RETARGETING`: App retargeting. Re-engage existing app users to take action in your app. • `MINIS`: TikTok Mini or Series. Promote your Series, mini series, or mini game by optimizing for organic and ads traffic.  • To learn more about the campaign type where this setting is supported, see [Create Upgraded Smart+ Growth Max campaigns](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1868120855134226). |
| sales_destination **(Điều kiện)** | string | Bắt buộc khi `objective_type` is `WEB_CONVERSIONS`. ⏎ Sales destination, the destination where you want to drive your sales. ⏎ Các giá trị enum hỗ trợ: • `WEBSITE`: Website. Drive sales on your website. • `APP`: App. Drive sales on your app (product catalog required). Learn more about [how to create Upgraded Smart+ Catalog Ads for App](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1847303035303106).  • When `sales_destination` is `APP`: • Set `catalog_enabled` to  `true` and `catalog_type` to `ECOMMERCE` or `TRAVEL_ENTERTAINMENT`.  • The type of catalog that you can specify at the ad group level varies depending on your `rta_id` setting: • If `rta_id` is not specified, you can set `catalog_id` at the ad group level to the ID of a catalog with `catalog_type` as `ECOM`, `HOTEL`,`FLIGHT`,`DESTINATION`, or `ENTERTAINMENT`. • If `rta_id` is specified, you can set `catalog_id` at the ad group level to the ID of a catalog with `catalog_type` as `ECOM` or `ENTERTAINMENT`. • `WEB_AND_APP`: Website and app. Drive sales on both your website and your app. • Learn more about how to [create Upgraded Smart+ Ads with Website and App Optimization](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1854746404386113). ⏎ **Note**: Once set, this field cannot be updated. |
| is_search_campaign | boolean | Chỉ hợp lệ khi `objective_type` is `APP_PROMOTION`, `WEB_CONVERSIONS`, or `LEAD_GENERATION`. ⏎ Có thực hiện create a Search Ads Campaign. ⏎ With Search Ads Campaigns, you set up your campaign to target ads in TikTok search results. Search Ads Campaigns reach those in your audience actively looking for products or information related to your brand. You'll use relevant keywords and search terms to help guide audiences to your ads. ⏎ Các giá trị được hỗ trợ: `true`, `false`. ⏎ Giá trị mặc định: `false`. ⏎ To learn more about how to create Search Ads Campaigns, see [Create Upgraded Smart+ Search Ads Campaigns](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1873144295333889). ⏎ **Note**:  • Upgraded Smart+ Search Ads Campaigns are currently an allowlist-only feature. If you would like to access it, please contact your TikTok representative. • When `is_search_campaign` is `true`, you can only set `budget_optimize_on` to `false`. • Once set, this field cannot be updated. |
| catalog_enabled | boolean | Chỉ hợp lệ khi `objective_type` is `WEB_CONVERSIONS`, `LEAD_GENERATION`, or `APP_PROMOTION`. ⏎ Có thực hiện use catalog in the campaign. ⏎ Các giá trị được hỗ trợ: `true`, `false`. |
| catalog_type **(Điều kiện)** | string | Required in any of the following scenarios: • When `objective_type` is `WEB_CONVERSIONS` and `catalog_enabled` is `true`. • When `objective_type` is `LEAD_GENERATION`, `catalog_enabled` is `true`, and you want to create [Upgraded Smart+ Lead Generic Catalog Ads](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1874421377372161). • When `objective_type` is `APP_PROMOTION` and `catalog_enabled` is `true`, and you want to create [Upgraded Smart+ App Online-to-Offline Catalog Ads](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1875231879602658). • When `objective_type` is `APP_PROMOTION` and `catalog_enabled` is `true`, and you want to create [Upgraded Smart+ App Travel Catalog Ads](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1879220213492353). ⏎ The type of catalog. ⏎ Enum values when `objective_type` is `WEB_CONVERSIONS` and `catalog_enabled` is `true`: • `ECOMMERCE`: e-commerce. • `TRAVEL_ENTERTAINMENT`: travel and entertainment. • `MINI_SERIES`: mini series. • `GENERIC`: generic. ⏎ Enum value when you want to create Upgraded Smart+ Lead Generic Catalog Ads: • `GENERIC`: generic. ⏎ Enum values when you want to create Upgraded Smart+ App O2O Catalog Ads: • `ONLINE_TO_OFFLINE`: online-to-offline. ⏎ Enum values when you want to create Upgraded Smart+ App Travel Catalog Ads: • `TRAVEL_ENTERTAINMENT`: travel and entertainment. ⏎ **Note**:  • Creating Upgraded Smart+ Mini Series Catalog Ads is currently an allowlist-only feature. If you would like to access it, please contact your TikTok representative. • Creating Upgraded Smart+ App O2O Catalog Ads is currently an allowlist-only feature. If you would like to access it, please contact your TikTok representative. • Creating Upgraded Smart+ App Travel Catalog Ads is currently an allowlist-only feature. If you would like to access it, please contact your TikTok representative. |
| campaign_type | string | Campaign type. ⏎ Các giá trị enum hỗ trợ: `REGULAR_CAMPAIGN`, `IOS14_CAMPAIGN`. ⏎ Giá trị mặc định: `REGULAR_CAMPAIGN`. |
| is_promotional_campaign | boolean | Valid in any of the following scenarios: • Scenario 1: `objective_type` is `APP_PROMOTION` and `app_promotion_type` is `APP_INSTALL`. • Scenario 2: `objective_type` is `WEB_CONVERSIONS` and `sales_destination` is `WEBSITE`. ⏎ Có thực hiện use promotion campaign settings. ⏎ Enable this feature to activate specialized campaign setup flows and optimization for new releases, event-driven campaigns, theatrical releases, streaming service promotions, events, or time-bound offers. ⏎ Giá trị mặc định: `false`. ⏎ Các giá trị được hỗ trợ: `true`, `false`. ⏎ **Note**:  • Using promotion campaign settings for theatrical releases and for streaming service promotions are currently separate allowlist-only features. If you would like to access them, please contact your TikTok  representative. • Using promotion campaign settings for the `APP_INSTALL` scenario is currently an allowlist-only feature. If you would like to access it, please contact your TikTok representative. |
| app_id **(Điều kiện)** | string | Bắt buộc khi the following conditions are both met: • `objective_type` is `APP_PROMOTION` and `app_promotion_type` is `APP_INSTALL`, or `objective_type` is `WEB_CONVERSIONS` and `sales_destination` is `APP`. • `camapign_type` is `IOS14_CAMPAIGN`. ⏎ The App ID of the app to promote. ⏎ To get a list of App IDs, use [/app/list/](43-events-1-0-p1.md#doc-1740859313270786). ⏎ **Note**: You cannot specify an App that has not activated the SAN module on your MMP through this field to create iOS Dedicated Campaigns. To ensure that TikTok SAN integration is enabled for your App, see [How to migrate your app to SAN integration](https://ads.tiktok.com/help/article/transition-to-san-for-existing-apps). |
| gaming_ad_compliance_agreement | string | Chỉ hợp lệ khi the following conditions are all met: • `objective_type` is `APP_PROMOTION`. • `app_promotion_type` is `APP_INSTALL`. • `campaign_type` is `IOS14_CAMPAIGN`. ⏎ Có thực hiện agree to the Compliance Assurance Policy for Gaming Advertisers on TikTok. ⏎ The policy is as follows: You confirm and attest that any gaming application, product or service (game) you desire to advertise on TikTok, including any associated URL(s), (a) complies with all applicable laws and regulations of the jurisdictions where the game can be accessed or played, and upon request, can provide supporting documentation as evidence of why the game is not considered illegal gambling or lottery; and (b) has not been and is not part of any investigation or lawsuit regarding the game's legality or regulatory compliance. ⏎ Các giá trị enum hỗ trợ: • `ON`: To agree to the policy. • `OFF`: To leave the policy not accepted. ⏎ Giá trị mặc định: `OFF`. ⏎ **Note**: Agreeing to the Compliance Assurance Policy for Gaming Advertisers on TikTok is currently an allowlist-only feature. If you would like to access it, please contact your TikTok representative. |
| campaign_app_profile_page_state | string | Có thực hiện use app profile page to optimize delivery. ⏎ Các giá trị enum hỗ trợ: `ON`, `OFF`. ⏎ Giá trị mặc định: `OFF`. ⏎ **Note**: • You can use the field only when `objective_type` is `APP_PROMOTION`, your campaign is an iOS 14 Dedicated Campaign, and `catalog_enabled` is `false`. Otherwise, an error will occur. • When `ON` is selected, pass in the `page_id` of App Profile Page. • To create an App Profile Page, use [Instant Page Editor SDK](../09-marketing-api/creatives.md#doc-1740307202170881) and set `businessType` to `4`. |
| disable_skan_campaign | boolean | Chỉ hợp lệ khi the following conditions are all met: • `objective_type` is `APP_PROMOTION` and `app_promotion_type` is `APP_INSTALL`, or `objective_type` is `WEB_CONVERSIONS` and `sales_destination` is `APP`. • `campaign_type` is `IOS14_CAMPAIGN`. • `app_id` is set to the ID of an iOS app that is eligible for [Advanced Dedicated Campaigns](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1797011827608577). To confirm Liệu an app is eligible for Advanced Dedicated Campaigns, use [/app/list/](43-events-1-0-p1.md#doc-1740859313270786) and check the returned `advanced_dedicated_campaign_allowed`. ⏎ Có thực hiện disable SKAN (SKAdNetwork) attribution, Apple's conversion attribution solution for iOS campaigns ⏎ Các giá trị enum hỗ trợ: • `true`: To disable SKAN attribution. The campaign will not be bound by [Dedicated Campaign quota limits](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1752256248260610) and you will be able to retrieve [Self Attribution Network (SAN) metrics](../09-marketing-api/bao-cao-p2.md#doc-1751443967255553) for the campaign. However, you cannot retrieve [SKAN reporting metrics](../09-marketing-api/bao-cao-p2.md#doc-1751443967255553) for the campaign. Learn more about [SAN integration](https://ads.tiktok.com/help/article/about-self-attribution-transition). • For a Dedicated Campaign using an app that is eligible for Advanced Dedicated Campaigns, you need to enable SKAN attribution or Advanced Dedicated Campaign or both. You cannot disable SKAN attribution and Advanced Dedicated Campaign simultaneously. • `false`: To enable SKAN attribution. The campaign will be bound by [Dedicated Campaign quota limits](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1752256248260610) and you will be able to retrieve [SKAN metrics](../09-marketing-api/bao-cao-p2.md#doc-1751443967255553) for the campaign. • If you enable Advanced Dedicated Campaign by setting `is_advanced_dedicated_campaign` to `true` simultaneously, you'll be able to retrieve both [SAN](../09-marketing-api/bao-cao-p2.md#doc-1751443967255553) and [SKAN reporting metrics](../09-marketing-api/bao-cao-p2.md#doc-1751443967255553) for the campaign. ⏎ **Note**: • Disabling SKAN attribution for Dedicated Campaigns is currently an allowlist-only feature. If you would like to access it, please contact your TikTok representative. • If you are allowlisted for disabling SKAN attribution for Dedicated Campaigns, you cannot set `bid_type` to `BID_TYPE_CUSTOM` when the following conditions are all met: • `is_advanced_dedicated_campaign` is `false`. • `disable_skan_campaign` is `false`. • `optimization_goal` is `INSTALL` or `IN_APP_EVENT`. • Getting access to Advanced Dedicated Campaign requires the app to meet certain criteria. If your app is ineligible for Advanced Dedicated Campaign, reach out to your TikTok representative. Your TikTok representative will be able to provide troubleshooting support to help your app get access to Advanced Dedicated Campaign. |
| campaign_name  ****(Bắt buộc)**** | string | Campaign name. ⏎ Giới hạn độ dài: 512 characters. Emoji is not supported. ⏎ Each word in Chinese or Japanese counts as two characters, while each letter in English counts as one character. |
| special_industries | string[] | Ad categories. Các giá trị enum hỗ trợ: • `HOUSING`: Ads for real estate listings, homeowners insurance, mortgage loans or other related opportunities. • `EMPLOYMENT`: Ads for job offers, internships, professional certification programs or other related opportunities. • `CREDIT`: Ads for credit card offers, auto loans, long-term financing or other related opportunities. ⏎ **Note**: • Once you've specified the industry type, the system will adjust your target options to help you comply with advertising policies. See [Ad targeting](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1739381236849665) for details. • This field is only supported for advertisers who are registered in the US or Canada. |
| budget_optimize_on | boolean | Có thực hiện enable Campaign Budget Optimization (CBO). ⏎ Các giá trị được hỗ trợ: `true` (enabled), `false` (disabled). ⏎ Giá trị mặc định: `true`. |
| budget_mode | string | Budget mode. • When `budget_optimize_on` is `true` or not specified, this field represents the campaign budget mode. The enum values are: • `BUDGET_MODE_DYNAMIC_DAILY_BUDGET`: Dynamic daily budget. It is the average daily budget over a week. Daily costs will not exceed 125% of the average daily budget. Weekly costs will not exceed the average daily budget * 7. • `BUDGET_MODE_TOTAL`: Lifetime budget.Giá trị mặc định when `budget_optimize_on` is `true` or not specified: `BUDGET_MODE_DYNAMIC_DAILY_BUDGET`. • When `budget_optimize_on` is `false`, this field allows you to set a fixed limit for the total budget of all ad groups under this campaign. The enum values are: • `BUDGET_MODE_INFINITE`: No limit. • `BUDGET_MODE_DAY`: Daily budget. • `BUDGET_MODE_TOTAL`: Lifetime budget.Giá trị mặc định when `budget_optimize_on` is `false`: `BUDGET_MODE_INFINITE`. ⏎ **Note**: • Once set, this field cannot be updated. |
| budget_auto_adjust_strategy | string | Chỉ hợp lệ khi the following conditions are all met: • `budget_optimize_on` is `true` or not specified. • `budget_mode` is `BUDGET_MODE_DYNAMIC_DAILY_BUDGET`. • `app_promotion_type` is not `MINIS`. ⏎ The campaign budget strategy for automatic daily campaign budget. ⏎ Enum value:  • `AUTO_BUDGET_INCREASE`: To enable Goal-based budget increase. Allow your budget to automatically increase when your ads are performing well and target CPA, Day 0 target ROAS, and budget requirements are met.  • When `budget_auto_adjust_strategy` is `AUTO_BUDGET_INCREASE`, the specified `budget` will be the initial daily budget. Your daily budget will be allowed to automatically increase by 20%, up to 10 times per day, when your budget utilization reaches 90% or more. Your daily budget will reset to your original daily budget each day. ⏎ **Note**: Enabling Goal-based budget increase is currently an allowlist-only feature. If you would like to access it, please contact your TikTok representative. |
| budget **(Điều kiện)** | float | Bắt buộc khi `budget_mode` is set to `BUDGET_MODE_DYNAMIC_DAILY_BUDGET`, `BUDGET_MODE_TOTAL`, or `BUDGET_MODE_DAY`. • When `budget_optimize_on` is `true` or not specified, this field represents fixed campaign budget or initial campaign budget. • When `budget_auto_adjust_strategy` is `UNSET`, this field represents your fixed campaign budget. • When `budget_auto_adjust_strategy` is `AUTO_BUDGET_INCREASE`, this field represents your initial campaign budget. To retrieve the current campaign budget, check the returned `current_budget`. • When `budget_optimize_on` is `false`, this field represents the limit for all ad groups under this campaign. • When `budget_mode` is `BUDGET_MODE_DAY`, this field represents the daily limit for all ad groups under this campaign. • When `budget_mode` is `BUDGET_MODE_TOTAL`, this field represents the total limit for all ad groups under this campaign. ⏎ To learn about the minimum budget and how to set budget modes, see [Budget](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1739381246298114). ⏎ To directly see the daily budget value range for a currency, see [Currency-Daily budget value range](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1737585839634433). |
| postback_window_mode | string | Chỉ hợp lệ khi `campaign_type` is `IOS14_CAMPAIGN` and `operation_status` is `DISABLE`. ⏎ You can specify this field when you create a disabled campaign or when you disable an existing campaign by using [/smart_plus/campaign/status/update/](62-upgraded-smartplus-p1.md#doc-1843312888885314). The recommended practice is to specify this field when disabling an existing campaign. ⏎ The mode that determines which SKAN (SKAdNetwork) 4.0 postback you want to secure. Options with longer windows require more time to receive, and as a result, more time to release the campaign back to the available number. ⏎ Các giá trị enum hỗ trợ: • `POSTBACK_WINDOW_MODE1`: This option secures the first postback, which corresponds to the 0-2 day attribution window. The data can take up to 4 days to return, and the campaign will wait for 4 days to release the campaign quota. • `POSTBACK_WINDOW_MODE2`: This mode secures the first two postbacks, which correspond to the 3-7 day attribution window. The data can take up to 13 days to return, and the campaign will wait for 13 days to release the campaign quota. • `POSTBACK_WINDOW_MODE3`: This mode secures all three postbacks, which correspond to the 8-35 day attribution window. The data can take up to 41 days to return, and the campaign will wait for 41 days to release the campaign quota. ⏎ **Note**:  • If you have set up Mobile Measurement Partner (MMP) Tracking with **Adjust**, **Airbridge**, **Appsflyer**, **Branch**, **Kochava**, or **Singular** for your App and your MMP SDK version is updated to a SKAN 4.0 supported SDK, you can transition your App to SKAN 4.0 on Events Manager. To learn about how to set up MMP tracking for your App, see [How to Set Up App Attribution in TikTok Ads Manager](https://ads.tiktok.com/help/article/set-up-app-attribution-tiktok-ads-manager). To learn more about how to transition your App to SKAN 4.0, see [About SKAN 4.0 and TikTok](https://ads.tiktok.com/help/article/about-skan-4-0-and-tiktok) and [How to transition to SKAN 4.0](https://ads.tiktok.com/help/article/how-to-transition-to-skan-4-0). • Once set, this field cannot be updated. • If `operation_status` is set to `ENABLE` or not specified, this field will be ignored. • If you pass in this field when you have not enabled SKAN 4.0 for your App (`app_id`), an error will occur. • If this field is not specified when `campaign_type` is set to `IOS14_CAMPAIGN`, `operation_status` is set to `DISABLE`, and you have enabled SKAN 4.0 for your App, this field will default to `POSTBACK_WINDOW_MODE1`. • If you have enabled SKAN 4.0 for your App, ensure that you target devices running iOS 16.1 and later so that you can receive SKAN 4.0 postbacks. To only target iOS 16.1+ devices, set `min_ios_version` to `16.1` at the ad group level. |
| po_number | string | Số đơn đặt hàng (PO - Purchase Order). ⏎ Số PO rất hữu ích cho việc theo dõi và đối soát hóa đơn. ⏎ [Tìm hiểu thêm về số PO trên hóa đơn hàng tháng](https://ads.tiktok.com/help/article/update-po-number-on-monthly-invoices). |
| rta_id | string | ID Realtime API (RTA), mã định danh chiến lược RTA. ⏎ RTA cho phép bạn tích hợp dữ liệu đối tượng thời gian thực để tùy chỉnh đấu thầu và nhắm mục tiêu, qua đó mang lại hiệu suất tốt hơn. ⏎ Để lấy danh sách ID RTA liên kết với tài khoản quảng cáo, hãy liên hệ với đại diện TikTok của bạn. ⏎ **Lưu ý**: • Bật RTA cho quảng cáo hiện là tính năng chỉ dành cho danh sách cho phép (allowlist-only). Nếu bạn muốn truy cập, vui lòng liên hệ với đại diện TikTok của bạn. • Bạn không thể cập nhật `rta_id` sau khi tạo chiến dịch. |
| rta_bid_enabled | boolean | Có thực hiện use RTA bid. ⏎ Các giá trị được hỗ trợ: • `true`: enabled. • `false`: not enabled. ⏎ Giá trị mặc định: `false`. ⏎ You can only set this field to `true` in any of the following scenarios: • Scenario 1:  • `objective_type` is set to `WEB_CONVERSIONS`. • `sales_destination` is set to `APP`. • `rta_id` is passed. • Scenario 2:  • `objective_type` is set to `APP_PROMOTION`. • `app_promotion_type` is set to `APP_RETARGETING`. • `rta_id` is passed. ⏎ **Note**:  • Enabling RTA bid is currently an allowlist-only feature. If you would like to access it, please contact your TikTok representative. • Once set, this field cannot be updated. |
| rta_product_selection_enabled | boolean | Có thực hiện use RTA to automatically select products. ⏎ Các giá trị enum hỗ trợ: • `true`: enabled. • `false`: not enabled. ⏎ Giá trị mặc định: `false`. ⏎ You can only set this field to `true` when the following conditions are met: • `objective_type` is set to `WEB_CONVERSIONS`. • `sales_destination` is set to `APP`. • `rta_id` is specified. ⏎ **Note**:  • Once set, this field cannot be updated. • When `rta_product_selection_enabled` is `true` , you can only set `product_specific_type` to `ALL` at the ad level. |

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/smart_plus/campaign/create/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id": "{{advertiser_id}}",
    "request_id": "{{request_id}}",
    "objective_type": "WEB_CONVERSIONS",
    "sales_destination": "WEBSITE",
    "campaign_name": "{{campaign_name}}",
    "budget": {{budget}}
}'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Mã phản hồi. Để xem danh sách đầy đủ các mã phản hồi và mô tả, xem [Phụ lục - Mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | ID nhật ký (log ID) của yêu cầu, dùng để định danh duy nhất yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ advertiser_id | string | ID tài khoản quảng cáo TikTok. |
| ↳ campaign_id | string | ID chiến dịch quảng cáo. |
| ↳ create_time | string | Thời điểm chiến dịch được tạo, theo định dạng `YYYY-MM-DD HH:MM:SS` (giờ UTC). |
| ↳ modify_time | string | Thời điểm chiến dịch được chỉnh sửa lần gần nhất, theo định dạng `YYYY-MM-DD HH:MM:SS` (giờ UTC). |
| ↳ objective_type | string | Mục tiêu quảng cáo. ⏎ Hiện tại hỗ trợ `APP_PROMOTION`, `WEB_CONVERSIONS` và `LEAD_GENERATION`. |
| ↳ app_promotion_type | string | Loại quảng bá ứng dụng. ⏎ Giá trị enum: • `APP_INSTALL`: Cài đặt ứng dụng. Thu hút người dùng mới cài đặt ứng dụng. • `APP_RETARGETING`: Nhắm mục tiêu lại ứng dụng. Tái tương tác người dùng ứng dụng hiện tại để thực hiện hành động. • `MINIS`: TikTok Mini hoặc Series. Quảng bá Series, phim ngắn nhiều tập hoặc mini game bằng cách tối ưu hóa lưu lượng tự nhiên và quảng cáo. |
| ↳ sales_destination | string | Đích đến bán hàng (Sales destination), nơi bạn muốn thúc đẩy doanh số. ⏎ Các giá trị enum hỗ trợ: • `WEBSITE`: Trang web. Thúc đẩy doanh số trên trang web của bạn. • `APP`: Ứng dụng. Thúc đẩy doanh số trên ứng dụng của bạn (yêu cầu danh mục sản phẩm). • `WEB_AND_APP`: Trang web và ứng dụng. Thúc đẩy doanh số trên cả trang web và ứng dụng. |
| ↳ campaign_type | string | Loại chiến dịch. ⏎ Hiện tại hỗ trợ `REGULAR_CAMPAIGN` và `IOS14_CAMPAIGN`. |
| ↳ app_id | string | App ID của ứng dụng cần quảng bá. ⏎ Để lấy danh sách App ID, sử dụng [/app/list/](43-events-1-0-p1.md#doc-1740859313270786). |
| ↳ gaming_ad_compliance_agreement | string | Có thực hiện agree to the Compliance Assurance Policy for Gaming Advertisers on TikTok. ⏎ The policy is as follows: Yo confirms and attest that any gaming application, product or service (game) you desire to advertise on TikTok, including any associated URL(s), (a) complies with all applicable laws and regulations of the jurisdictions where the game can be accessed or played, and upon request, can provide supporting documentation as evidence of why the game is not considered illegal gambling or lottery; and (b) has not been and is not part of any investigation or lawsuit regarding the game's legality or regulatory compliance. ⏎ Các giá trị enum hỗ trợ: • `ON`: To agree to the policy. • `OFF`: To leave the policy not accepted. |
| ↳ is_advanced_dedicated_campaign | boolean | Liệu campaign is an Advanced Dedicated Campaign. Advanced Dedicated Campaigns leverage advanced delivery models that benefit from real-time signals. ⏎ Các giá trị được hỗ trợ: `true`, `false`. |
| ↳ disable_skan_campaign | boolean | Có thực hiện disable SKAN (SKAdNetwork) attribution, Apple's conversion attribution solution for iOS campaigns. ⏎ Các giá trị enum hỗ trợ: • `true`: To disable SKAN attribution. The campaign will not be bound by [Dedicated Campaign quota limits](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1752256248260610) and you will be able to retrieve [Self Attribution Network (SAN) metrics](../09-marketing-api/bao-cao-p2.md#doc-1751443967255553) for the campaign. However, you cannot retrieve [SKAN reporting metrics](../09-marketing-api/bao-cao-p2.md#doc-1751443967255553) for the campaign. Learn more about [SAN integration](https://ads.tiktok.com/help/article/about-self-attribution-transition). • `false`: To enable SKAN attribution. The campaign will be bound by [Dedicated Campaign quota limits](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1752256248260610) and you will be able to retrieve [SKAN metrics](../09-marketing-api/bao-cao-p2.md#doc-1751443967255553) for the campaign. |
| ↳ bid_align_type | string | The attribution type for the Dedicated Campaign. The type determines which attribution network the target CPA (conversion_bid_price) or ROAS (roas_bid) at the ad group level is based on. ⏎ Các giá trị enum hỗ trợ: • `SAN`: SAN. • `SKAN`: SKAN. |
| ↳ campaign_app_profile_page_state | string | Indicates the status of the App Profile Page. ⏎ Các giá trị enum hỗ trợ: `ON`, `OFF`. |
| ↳ is_search_campaign | boolean | Liệu campaign is a Search Ads Campaign. ⏎ With Search Ads Campaigns, you set up your campaign to target ads in TikTok search results. Search Ads Campaigns reach those in your audience actively looking for products or information related to your brand. You'll use relevant keywords and search terms to help guide audiences to your ads. ⏎ Các giá trị được hỗ trợ: `true`, `false`. |
| ↳ catalog_enabled | boolean | Có thực hiện use your catalog to automatically advertise relevant products or services to people based on their unique interests, intent and actions. ⏎ Các giá trị được hỗ trợ: `true`, `false`. |
| ↳ catalog_type | string | The type of catalog. ⏎ Các giá trị enum hỗ trợ: • `ECOMMERCE`: e-commerce. • `TRAVEL_ENTERTAINMENT`: travel and entertainment. • `MINI_SERIES`: mini series. • `GENERIC`: generic. • `ONLINE_TO_OFFLINE`: online-to-offline. |
| ↳ campaign_name | string | Tên chiến dịch. |
| ↳ special_industries | string[] | Ad categories. ⏎ Các giá trị enum hỗ trợ: • `HOUSING`: Ads for real estate listings, homeowners insurance, mortgage loans or other related opportunities. • `EMPLOYMENT`: Ads for job offers, internships, professional certification programs or other related opportunities. • `CREDIT`: Ads for credit card offers, auto loans, long-term financing or other related opportunities. |
| ↳ budget_optimize_on | boolean | Liệu CBO is enabled. ⏎ Các giá trị được hỗ trợ: `true` (enabled), `false` (disabled). |
| ↳ budget_mode | string | Chế độ ngân sách. ⏎ • Khi `budget_optimize_on` là `true` hoặc không chỉ định, các giá trị enum gồm: • `BUDGET_MODE_DYNAMIC_DAILY_BUDGET`: Ngân sách chiến dịch hàng ngày động. • `BUDGET_MODE_TOTAL`: Ngân sách chiến dịch trọn đời. • Khi `budget_optimize_on` là `false`, các giá trị enum gồm: • `BUDGET_MODE_INFINITE`: Không giới hạn ngân sách. • `BUDGET_MODE_DAY`: Giới hạn ngân sách hàng ngày. • `BUDGET_MODE_TOTAL`: Giới hạn tổng ngân sách. |
| ↳ budget_auto_adjust_strategy | string | Returned only when the following conditions are all met: • `budget_optimize_on` is `true` or not specified. • `budget_mode` is `BUDGET_MODE_DYNAMIC_DAILY_BUDGET`. • `app_promotion_type` is not `MINIS`. ⏎ The campaign budget strategy for automatic daily campaign budget. ⏎ Các giá trị enum hỗ trợ: • `AUTO_BUDGET_INCREASE`: To enable Goal-based budget increase. Allow your budget to automatically increase when your ads are performing well and target CPA, Day 0 target ROAS, and budget requirements are met.  • When `budget_auto_adjust_strategy` is `AUTO_BUDGET_INCREASE`, the specified `budget` will be the initial daily budget. Your daily budget will be allowed to automatically increase by 20%, up to 10 times per day, when your budget utilization reaches 90% or more. Your daily budget will reset to your original daily budget each day. • `UNSET`: To disable Goal-based budget increase. |
| ↳ budget | float | • Khi `budget_optimize_on` là `true` hoặc không chỉ định, trường này đại diện cho ngân sách chiến dịch cố định hoặc ngân sách ban đầu. • Khi `budget_auto_adjust_strategy` là `UNSET`, trường này đại diện cho ngân sách chiến dịch cố định. • Khi `budget_auto_adjust_strategy` là `AUTO_BUDGET_INCREASE`, trường này đại diện cho ngân sách ban đầu. Để lấy ngân sách chiến dịch hiện tại, kiểm tra trường `current_budget` được trả về. • Khi `budget_optimize_on` là `false`, trường này đại diện cho hạn mức cho tất cả nhóm quảng cáo trong chiến dịch. • Khi `budget_mode` là `BUDGET_MODE_DAY`, trường này đại diện cho hạn mức hàng ngày. • Khi `budget_mode` là `BUDGET_MODE_TOTAL`, trường này đại diện cho hạn mức tổng ngân sách. |
| ↳ current_budget | float | Chỉ trả về khi `budget_auto_adjust_strategy` là `AUTO_BUDGET_INCREASE`. ⏎ Ngân sách chiến dịch hiện tại cho chiến dịch đã bật tự động tăng ngân sách theo mục tiêu. |
| ↳ operation_status | string | Trạng thái hoạt động. ⏎ Các giá trị enum hỗ trợ: • `ENABLE` : The campaign is enabled (in 'ON' status). • `DISABLE`: The campaign is disabled (in 'OFF' status). |
| ↳ secondary_status | string | Campaign secondary status. ⏎ Để xem danh sách giá trị enum, xem [Enumeration- Campaign Status - Secondary Status](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ smart_plus_adgroup_mode | string | The ad group mode for the campaign. ⏎ Các giá trị enum hỗ trợ: • `SINGLE`: You can only create one single ad group within the campaign. • `MULTIPLE`: You can only create multiple ad groups within the campaign. |
| ↳ postback_window_mode | string | The mode that determines which SKAN 4.0 postback you want to secure. ⏎ Các giá trị enum hỗ trợ: • `POSTBACK_WINDOW_MODE1`: This option secures the first postback, which corresponds to the 0-2 day attribution window. The data can take up to 4 days to return, and the campaign will wait for 4 days to release the campaign quota. • `POSTBACK_WINDOW_MODE2`: This mode secures the first two postbacks, which correspond to the 3-7 day attribution window. The data can take up to 13 days to return, and the campaign will wait for 13 days to release the campaign quota. • `POSTBACK_WINDOW_MODE3`: This mode secures all three postbacks, which correspond to the 8-35 day attribution window. The data can take up to 41 days to return, and the campaign will wait for 41 days to release the campaign quota. ⏎ **Note**: If you have set up Mobile Measurement Partner (MMP) Tracking with **Adjust**, **Airbridge**, **Appsflyer**, **Branch**, **Kochava**, or **Singular** for your App and your MMP SDK version is updated to a SKAN 4.0 supported SDK, you can transition your App to SKAN 4.0 on Events Manager. To learn about how to set up MMP tracking for your App, see [How to Set Up App Attribution in TikTok Ads Manager](https://ads.tiktok.com/help/article/set-up-app-attribution-tiktok-ads-manager). To learn more about how to transition your App to SKAN 4.0, see [About SKAN 4.0 and TikTok](https://ads.tiktok.com/help/article/about-skan-4-0-and-tiktok) and [How to transition to SKAN 4.0](https://ads.tiktok.com/help/article/how-to-transition-to-skan-4-0). |
| ↳ po_number | string | Số đơn đặt hàng (PO - Purchase Order). ⏎ Số PO rất hữu ích cho việc theo dõi và đối soát hóa đơn. ⏎ [Tìm hiểu thêm về số PO trên hóa đơn hàng tháng](https://ads.tiktok.com/help/article/update-po-number-on-monthly-invoices). |
| ↳ is_promotional_campaign | boolean | Có thực hiện use promotion campaign settings. ⏎ Enable this feature to activate specialized campaign setup flows and optimization for new releases, event-driven campaigns, theatrical releases, streaming service promotions, events, or time-bound offers. ⏎ Các giá trị được hỗ trợ: `true`, `false`. |
| ↳ rta_id | string | ID Realtime API (RTA), mã định danh chiến lược RTA. |
| ↳ rta_bid_enabled | boolean | Có thực hiện use RTA bid. ⏎ Các giá trị được hỗ trợ: • `true`: enabled. • `false`: not enabled. |
| ↳ rta_product_selection_enabled | boolean | Có thực hiện use RTA to automatically select products. ⏎ Các giá trị enum hỗ trợ: • `true`: enabled. • `false`: not enabled. |

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "advertiser_id": "{{advertiser_id}}",
        "budget": {{budget}},
        "budget_mode": "BUDGET_MODE_DYNAMIC_DAILY_BUDGET",
        "budget_optimize_on": true,
        "campaign_id": "{{campaign_id}}",
        "campaign_name": "{{campaign_name}}",
        "campaign_type": "REGULAR_CAMPAIGN",
        "create_time": "{{create_time}}",
        "modify_time": "{{modify_time}}",
        "objective_type": "WEB_CONVERSIONS",
        "operation_status": "ENABLE",
        "sales_destination": "WEBSITE",
        "secondary_status": "CAMPAIGN_STATUS_ENABLE",
        "smart_plus_adgroup_mode": "MULTIPLE"
    }
}
```

---

<a id="doc-1843312876001282"></a>
<!-- doc_id: 1843312876001282 -->
<!-- doc_id: 1843312876001282 -->
# Cập nhật chiến dịch Smart+ nâng cấp (Update an Upgraded Smart+ Campaign)
> Đường dẫn: API Reference > Smart+ nâng cấp > Campaigns > Update an Upgraded Smart+ Campaign
> **Note:** 

Sử dụng endpoint này để cập nhật an Upgraded Smart+ Campaign.

Endpoint này hỗ trợ cập nhật tăng dần (incremental updates).

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/smart_plus/campaign/update/

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
| campaign_id  ****(Bắt buộc)**** | string | ID chiến dịch quảng cáo. ⏎ To obtain campaign IDs, use [/smart_plus/campaign/get/](62-upgraded-smartplus-p1.md#doc-1843312818332930). |
| campaign_name | string | Campaign name. ⏎ Giới hạn độ dài: 512 characters. Emoji is not supported. ⏎ Each word in Chinese or Japanese counts as two characters, while each letter in English counts as one character. |
| is_promotional_campaign | boolean | Valid in the following scenario: • `objective_type` is `APP_PROMOTION` and `app_promotion_type` is `APP_INSTALL`. ⏎ Có thực hiện use promotion campaign settings. ⏎ Enable this feature to activate specialized campaign setup flows and optimization for new releases, event-driven campaigns, or time-bound offers. ⏎ Các giá trị được hỗ trợ: `true`, `false`. |
| budget_auto_adjust_strategy | string | Chỉ hợp lệ khi the following conditions are all met: • `budget_optimize_on` is `true`. • `budget_mode` is `BUDGET_MODE_DYNAMIC_DAILY_BUDGET`. • `app_promotion_type` is not `MINIS`. ⏎ The campaign budget strategy for automatic daily campaign budget. ⏎ Các giá trị enum hỗ trợ: • `AUTO_BUDGET_INCREASE`: To enable Goal-based budget increase. Allow your budget to automatically increase when your ads are performing well and target CPA, Day 0 target ROAS, and budget requirements are met.  • When `budget_auto_adjust_strategy` is `AUTO_BUDGET_INCREASE`, the specified `budget` will be the initial daily budget. Your daily budget will be allowed to automatically increase by 20%, up to 10 times per day, when your budget utilization reaches 90% or more. Your daily budget will reset to your original daily budget each day. • `UNSET`: To disable Goal-based budget increase. ⏎ **Note**: Enabling Goal-based budget increase is currently an allowlist-only feature. If you would like to access it, please contact your TikTok representative. |
| budget | float | Ngân sách chiến dịch cố định hoặc ngân sách ban đầu. • Khi `budget_auto_adjust_strategy` là `UNSET`, trường này đại diện cho ngân sách cố định. • Khi `budget_auto_adjust_strategy` là `AUTO_BUDGET_INCREASE`, trường này đại diện cho ngân sách ban đầu. Để lấy ngân sách chiến dịch hiện tại, kiểm tra trường `current_budget` được trả về. |
| po_number | string | Số đơn đặt hàng (PO - Purchase Order). ⏎ Số PO rất hữu ích cho việc theo dõi và đối soát hóa đơn. ⏎ [Tìm hiểu thêm về số PO trên hóa đơn hàng tháng](https://ads.tiktok.com/help/article/update-po-number-on-monthly-invoices). |

### Ví dụ lệnh cURL (Example)

```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/smart_plus/campaign/update/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id": "{{advertiser_id}}",
    "campaign_id": "{{campaign_id}}",
    "campaign_name": "{{campaign_name}}"
}'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Mã phản hồi. Để xem danh sách đầy đủ các mã phản hồi và mô tả, xem [Phụ lục - Mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | ID nhật ký (log ID) của yêu cầu, dùng để định danh duy nhất yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ advertiser_id | string | ID tài khoản quảng cáo TikTok. |
| ↳ campaign_id | string | ID chiến dịch quảng cáo. |
| ↳ create_time | string | Thời điểm chiến dịch được tạo, theo định dạng `YYYY-MM-DD HH:MM:SS` (giờ UTC). |
| ↳ modify_time | string | Thời điểm chiến dịch được chỉnh sửa lần gần nhất, theo định dạng `YYYY-MM-DD HH:MM:SS` (giờ UTC). |
| ↳ objective_type | string | Mục tiêu quảng cáo. ⏎ Hiện tại hỗ trợ `APP_PROMOTION`, `WEB_CONVERSIONS` và `LEAD_GENERATION`. |
| ↳ app_promotion_type | string | Loại quảng bá ứng dụng. ⏎ Giá trị enum: • `APP_INSTALL`: Cài đặt ứng dụng. Thu hút người dùng mới cài đặt ứng dụng. • `APP_RETARGETING`: Nhắm mục tiêu lại ứng dụng. Tái tương tác người dùng ứng dụng hiện tại để thực hiện hành động. • `MINIS`: TikTok Mini hoặc Series. Quảng bá Series, phim ngắn nhiều tập hoặc mini game bằng cách tối ưu hóa lưu lượng tự nhiên và quảng cáo. |
| ↳ sales_destination | string | Đích đến bán hàng (Sales destination), nơi bạn muốn thúc đẩy doanh số. ⏎ Các giá trị enum hỗ trợ: • `WEBSITE`: Trang web. Thúc đẩy doanh số trên trang web của bạn. • `APP`: Ứng dụng. Thúc đẩy doanh số trên ứng dụng của bạn (yêu cầu danh mục sản phẩm). • `WEB_AND_APP`: Trang web và ứng dụng. Thúc đẩy doanh số trên cả trang web và ứng dụng. |
| ↳ campaign_type | string | Loại chiến dịch. ⏎ Hiện tại hỗ trợ `REGULAR_CAMPAIGN` và `IOS14_CAMPAIGN`. |
| ↳ app_id | string | App ID của ứng dụng cần quảng bá. ⏎ Để lấy danh sách App ID, sử dụng [/app/list/](43-events-1-0-p1.md#doc-1740859313270786). |
| ↳ gaming_ad_compliance_agreement | string | Có thực hiện agree to the Compliance Assurance Policy for Gaming Advertisers on TikTok. ⏎ The policy is as follows: Yo confirms and attest that any gaming application, product or service (game) you desire to advertise on TikTok, including any associated URL(s), (a) complies with all applicable laws and regulations of the jurisdictions where the game can be accessed or played, and upon request, can provide supporting documentation as evidence of why the game is not considered illegal gambling or lottery; and (b) has not been and is not part of any investigation or lawsuit regarding the game's legality or regulatory compliance. ⏎ Các giá trị enum hỗ trợ: • `ON`: To agree to the policy. • `OFF`: To leave the policy not accepted. |
| ↳ is_advanced_dedicated_campaign | boolean | Liệu campaign is an Advanced Dedicated Campaign. Advanced Dedicated Campaigns leverage advanced delivery models that benefit from real-time signals. ⏎ Các giá trị được hỗ trợ: `true`, `false`. |
| ↳ disable_skan_campaign | boolean | Có thực hiện disable SKAN (SKAdNetwork) attribution, Apple's conversion attribution solution for iOS campaigns. ⏎ Các giá trị enum hỗ trợ: • `true`: To disable SKAN attribution. The campaign will not be bound by [Dedicated Campaign quota limits](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1752256248260610) and you will be able to retrieve [Self Attribution Network (SAN) metrics](../09-marketing-api/bao-cao-p2.md#doc-1751443967255553) for the campaign. However, you cannot retrieve [SKAN reporting metrics](../09-marketing-api/bao-cao-p2.md#doc-1751443967255553) for the campaign. Learn more about [SAN integration](https://ads.tiktok.com/help/article/about-self-attribution-transition). • `false`: To enable SKAN attribution. The campaign will be bound by [Dedicated Campaign quota limits](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1752256248260610) and you will be able to retrieve [SKAN metrics](../09-marketing-api/bao-cao-p2.md#doc-1751443967255553) for the campaign. |
| ↳ bid_align_type | string | The attribution type for the Dedicated Campaign. The type determines which attribution network the target CPA (conversion_bid_price) or ROAS (roas_bid) at the ad group level is based on. ⏎ Các giá trị enum hỗ trợ: • `SAN`: SAN. • `SKAN`: SKAN. |
| ↳ campaign_app_profile_page_state | string | Indicates the status of the App Profile Page. ⏎ Các giá trị enum hỗ trợ: `ON`, `OFF`. |
| ↳ is_search_campaign | boolean | Liệu campaign is a Search Ads Campaign. ⏎ With Search Ads Campaigns, you set up your campaign to target ads in TikTok search results. Search Ads Campaigns reach those in your audience actively looking for products or information related to your brand. You'll use relevant keywords and search terms to help guide audiences to your ads. ⏎ Các giá trị được hỗ trợ: `true`, `false`. |
| ↳ catalog_enabled | boolean | Có thực hiện use your catalog to automatically advertise relevant products or services to people based on their unique interests, intent and actions. ⏎ Các giá trị được hỗ trợ: `true`, `false`. |
| ↳ catalog_type | string | The type of catalog. ⏎ Các giá trị enum hỗ trợ: • `ECOMMERCE`: e-commerce. • `TRAVEL_ENTERTAINMENT`: travel and entertainment. • `MINI_SERIES`: mini series. • `GENERIC`: generic. • `ONLINE_TO_OFFLINE`: online-to-offline. |
| ↳ campaign_name | string | Tên chiến dịch. |
| ↳ special_industries | string[] | Ad categories. ⏎ Các giá trị enum hỗ trợ: • `HOUSING`: Ads for real estate listings, homeowners insurance, mortgage loans or other related opportunities. • `EMPLOYMENT`: Ads for job offers, internships, professional certification programs or other related opportunities. • `CREDIT`: Ads for credit card offers, auto loans, long-term financing or other related opportunities. |
| ↳ budget_optimize_on | boolean | Liệu CBO is enabled. ⏎ Các giá trị được hỗ trợ: `true` (enabled), `false` (disabled). |
| ↳ budget_mode | string | Chế độ ngân sách. ⏎ • Khi `budget_optimize_on` là `true` hoặc không chỉ định, các giá trị enum gồm: • `BUDGET_MODE_DYNAMIC_DAILY_BUDGET`: Ngân sách chiến dịch hàng ngày động. • `BUDGET_MODE_TOTAL`: Ngân sách chiến dịch trọn đời. • Khi `budget_optimize_on` là `false`, các giá trị enum gồm: • `BUDGET_MODE_INFINITE`: Không giới hạn ngân sách. • `BUDGET_MODE_DAY`: Giới hạn ngân sách hàng ngày. • `BUDGET_MODE_TOTAL`: Giới hạn tổng ngân sách. |
| ↳ budget_auto_adjust_strategy | string | Returned only when the following conditions are all met: • `budget_optimize_on` is `true` or not specified. • `budget_mode` is `BUDGET_MODE_DYNAMIC_DAILY_BUDGET`. • `app_promotion_type` is not `MINIS`. ⏎ The campaign budget strategy for automatic daily campaign budget. ⏎ Các giá trị enum hỗ trợ: • `AUTO_BUDGET_INCREASE`: To enable Goal-based budget increase. Allow your budget to automatically increase when your ads are performing well and target CPA, Day 0 target ROAS, and budget requirements are met.  • When `budget_auto_adjust_strategy` is `AUTO_BUDGET_INCREASE`, the specified `budget` will be the initial daily budget. Your daily budget will be allowed to automatically increase by 20%, up to 10 times per day, when your budget utilization reaches 90% or more. Your daily budget will reset to your original daily budget each day. • `UNSET`: To disable Goal-based budget increase. |
| ↳ budget | float | • Khi `budget_optimize_on` là `true` hoặc không chỉ định, trường này đại diện cho ngân sách chiến dịch cố định hoặc ngân sách ban đầu. • Khi `budget_auto_adjust_strategy` là `UNSET`, trường này đại diện cho ngân sách chiến dịch cố định. • Khi `budget_auto_adjust_strategy` là `AUTO_BUDGET_INCREASE`, trường này đại diện cho ngân sách ban đầu. Để lấy ngân sách chiến dịch hiện tại, kiểm tra trường `current_budget` được trả về. • Khi `budget_optimize_on` là `false`, trường này đại diện cho hạn mức cho tất cả nhóm quảng cáo trong chiến dịch. • Khi `budget_mode` là `BUDGET_MODE_DAY`, trường này đại diện cho hạn mức hàng ngày. • Khi `budget_mode` là `BUDGET_MODE_TOTAL`, trường này đại diện cho hạn mức tổng ngân sách. |
| ↳ current_budget | float | Chỉ trả về khi `budget_auto_adjust_strategy` là `AUTO_BUDGET_INCREASE`. ⏎ Ngân sách chiến dịch hiện tại cho chiến dịch đã bật tự động tăng ngân sách theo mục tiêu. |
| ↳ operation_status | string | Trạng thái hoạt động. ⏎ Các giá trị enum hỗ trợ: • `ENABLE` : The campaign is enabled (in 'ON' status). • `DISABLE`: The campaign is disabled (in 'OFF' status). |
| ↳ secondary_status | string | Campaign secondary status. ⏎ Để xem danh sách giá trị enum, xem [Enumeration- Campaign Status - Secondary Status](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ smart_plus_adgroup_mode | string | The ad group mode for the campaign. ⏎ Các giá trị enum hỗ trợ: • `SINGLE`: You can only create one single ad group within the campaign. • `MULTIPLE`: You can only create multiple ad groups within the campaign. |
| ↳ postback_window_mode | string | The mode that determines which SKAN 4.0 postback you want to secure. ⏎ Các giá trị enum hỗ trợ: • `POSTBACK_WINDOW_MODE1`: This option secures the first postback, which corresponds to the 0-2 day attribution window. The data can take up to 4 days to return, and the campaign will wait for 4 days to release the campaign quota. • `POSTBACK_WINDOW_MODE2`: This mode secures the first two postbacks, which correspond to the 3-7 day attribution window. The data can take up to 13 days to return, and the campaign will wait for 13 days to release the campaign quota. • `POSTBACK_WINDOW_MODE3`: This mode secures all three postbacks, which correspond to the 8-35 day attribution window. The data can take up to 41 days to return, and the campaign will wait for 41 days to release the campaign quota. ⏎ **Note**: If you have set up Mobile Measurement Partner (MMP) Tracking with **Adjust**, **Airbridge**, **Appsflyer**, **Branch**, **Kochava**, or **Singular** for your App and your MMP SDK version is updated to a SKAN 4.0 supported SDK, you can transition your App to SKAN 4.0 on Events Manager. To learn about how to set up MMP tracking for your App, see [How to Set Up App Attribution in TikTok Ads Manager](https://ads.tiktok.com/help/article/set-up-app-attribution-tiktok-ads-manager). To learn more about how to transition your App to SKAN 4.0, see [About SKAN 4.0 and TikTok](https://ads.tiktok.com/help/article/about-skan-4-0-and-tiktok) and [How to transition to SKAN 4.0](https://ads.tiktok.com/help/article/how-to-transition-to-skan-4-0). |
| ↳ po_number | string | Số đơn đặt hàng (PO - Purchase Order). ⏎ Số PO rất hữu ích cho việc theo dõi và đối soát hóa đơn. ⏎ [Tìm hiểu thêm về số PO trên hóa đơn hàng tháng](https://ads.tiktok.com/help/article/update-po-number-on-monthly-invoices). |
| ↳ is_promotional_campaign | boolean | Có thực hiện use promotion campaign settings. ⏎ Enable this feature to activate specialized campaign setup flows and optimization for new releases, event-driven campaigns, theatrical releases, streaming service promotions, events, or time-bound offers. ⏎ Các giá trị được hỗ trợ: `true`, `false`. |
| ↳ rta_id | string | ID Realtime API (RTA), mã định danh chiến lược RTA. |
| ↳ rta_bid_enabled | boolean | Có thực hiện use RTA bid. ⏎ Các giá trị được hỗ trợ: • `true`: enabled. • `false`: not enabled. |
| ↳ rta_product_selection_enabled | boolean | Có thực hiện use RTA to automatically select products. ⏎ Các giá trị enum hỗ trợ: • `true`: enabled. • `false`: not enabled. |

### Ví dụ lệnh cURL (Example)

```http
// Success-Response
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "advertiser_id": "{{advertiser_id}}",
        "app_id": "{{app_id}}",
        "app_promotion_type": "APP_INSTALL",
        "budget": {{budget}},
        "budget_mode": "BUDGET_MODE_DYNAMIC_DAILY_BUDGET",
        "budget_optimize_on": true,
        "campaign_app_profile_page_state": "ON",
        "campaign_id": "{{campaign_id}}",
        "campaign_name": "{{campaign_name}}",
        "campaign_type": "IOS14_CAMPAIGN",
        "create_time": "{{create_time}}",
        "disable_skan_campaign": false,
        "is_advanced_dedicated_campaign": true,
        "modify_time": "{{modify_time}}",
        "objective_type": "APP_PROMOTION",
        "operation_status": "ENABLE",
        "secondary_status": "CAMPAIGN_STATUS_ENABLE",
        "smart_plus_adgroup_mode": "MULTIPLE"
    }
}
```

---

<a id="doc-1843312888885314"></a>
<!-- doc_id: 1843312888885314 -->
<!-- doc_id: 1843312888885314 -->
# Cập nhật trạng thái hoạt động của chiến dịch Smart+ nâng cấp (Update the operation statuses of Upgraded Smart+ Campaigns)
> Đường dẫn: API Reference > Smart+ nâng cấp > Campaigns > Update the operation statuses of Upgraded Smart+ Campaigns
Sử dụng endpoint này để bật, tạm dừng hoặc xóa các Chiến dịch Smart+ nâng cấp.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/smart_plus/campaign/status/update/

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
| campaign_ids  ****(Bắt buộc)**** | string[] | The IDs of the campaigns to operate on. ⏎ To obtain campaign IDs, use [/smart_plus/campaign/get/](62-upgraded-smartplus-p1.md#doc-1843312818332930). ⏎ Size range:  1-20. |
| operation_status  ****(Bắt buộc)**** | string | The operation to perform on the campaigns. ⏎ Các giá trị enum hỗ trợ: `DELETE` (delete),` DISABLE` (pause), `ENABLE` (enable). ⏎ **Note**: The status of deleted campaigns cannot be modified. |
| postback_window_mode | string | Chỉ hợp lệ khi the following conditions are all met: • The campaigns (`campaign_ids`) are Dedicated Campaigns (`campaign_type` is `IOS14_CAMPAIGN`). • You specify `operation_status` as `DISABLE` at the same time in the request. • `postback_window_mode` has not been configured for the campaign. • You have enabled SKAN 4.0 for your App. ⏎ The mode that defines which SKAN (SKAdNetwork) 4.0 postback you want to secure. Options with longer windows require more time to receive and, as a result, more time to release the campaign back to the available number. ⏎ Các giá trị enum hỗ trợ: • `POSTBACK_WINDOW_MODE1`: This option secures the first postback, which corresponds to the 0-2 day attribution window. The data can take up to 4 days to return, and the campaign will wait for 4 days to release the campaign quota. • `POSTBACK_WINDOW_MODE2`: This mode secures the first two postbacks, which corresponds to the 3-7 day attribution window. The data can take up to 13 days to return, and the campaign will wait for 13 days to release the campaign quota. • `POSTBACK_WINDOW_MODE3`: This mode secures all three postbacks, which corresponds to the 8-35 day attribution window. The data can take up to 41 days to return, and the campaign will wait for 41 days to release the campaign quota. ⏎ To learn more about SKAN 4.0 attribution window configuration and campaign quota, see [Dedicated Campaigns](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1740029173531649). ⏎ **Note**: • If you have set up Mobile Measurement Partner (MMP) Tracking with **Adjust**, **Airbridge**, **Appsflyer**, **Branch**, **Kochava**, or **Singular** for your App and your MMP SDK version is updated to a SKAN 4.0 supported SDK, you can transition your App to SKAN 4.0 on Events Manager. To learn about how to set up MMP tracking for your App, see [How to Set Up App Attribution in TikTok Ads Manager](https://ads.tiktok.com/help/article/set-up-app-attribution-tiktok-ads-manager). To learn more about how to transition your App to SKAN 4.0, see [About SKAN 4.0 and TikTok](https://ads.tiktok.com/help/article/about-skan-4-0-and-tiktok) and [How to transition to SKAN 4.0](https://ads.tiktok.com/help/article/how-to-transition-to-skan-4-0). • If `operation_status` is set to `ENABLE` or not passed, and you pass in this field at the same time, an error will occur. • If you pass in this field when you have not enabled SKAN 4.0 for your App (`app_id`), an error will occur. • If this field is not passed when `campaign_type` is set to `IOS14_CAMPAIGN`, `operation_status` is set to `DISABLE`, and you have enabled SKAN 4.0 for your App, this field will default to `POSTBACK_WINDOW_MODE1`. • The postback window mode configuration can be partially successful. If you provide `campaign_ids` for non-Dedicated Campaigns, or Dedicated Campaigns for which `postback_window_mode` has been configured, those campaigns will be ignored and their `postback_window_mode` will not be modified. Only the Dedicated Campaigns that meet the conditions mentioned above will have their `postback_window_mode` configured. • If you have enabled SKAN 4.0 for your App, ensure that you target devices running iOS 16.1 and later so that you can receive SKAN 4.0 postbacks. To only target iOS 16.1+ devices, set `min_ios_version` to `16.1` at the ad group level. |

### Ví dụ lệnh cURL (Example)

```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/smart_plus/campaign/status/update/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id": "{{advertiser_id}}",
    "campaign_ids": ["{{campaign_ids}}"],
    "operation_status": "DISABLE"
}'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Response code. For the complete list of response codes and descriptions, see [Appendix-Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | ID nhật ký (log ID) của yêu cầu, dùng để định danh duy nhất yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ campaign_list | object[] | Danh sách các chiến dịch mà thao tác được thực hiện thành công. |
| ↳↳ campaign_id | string | ID của chiến dịch mà thao tác được thực hiện thành công. |
| ↳↳ status | string | The current status of the campaign for which the operation was successful. ⏎ Các giá trị enum hỗ trợ: `DISABLE` (paused), `ENABLE` (enabled), `DELETE` (deleted). |
| ↳↳ postback_window_mode | string | The mode that determines which SKAN 4.0 postback you want to secure. ⏎ Các giá trị enum hỗ trợ: • `POSTBACK_WINDOW_MODE1`: This option secures the first postback, which corresponds to the 0-2 day attribution window. The data can take up to 4 days to return, and the campaign will wait for 4 days to release the campaign quota. • `POSTBACK_WINDOW_MODE2`: This mode secures the first two postbacks, which corresponds to the 3-7 day attribution window. The data can take up to 13 days to return, and the campaign will wait for 13 days to release the campaign quota. • `POSTBACK_WINDOW_MODE3`: This mode secures all three postbacks, which corresponds to the 8-35 day attribution window. The data can take up to 41 days to return, and the campaign will wait for 41 days to release the campaign quota. |
| ↳ error_list | object[] | Danh sách các lỗi và các chiến dịch thất bại tương ứng. |
| ↳↳ campaign_id | string | ID của chiến dịch mà thao tác thất bại. |
| ↳↳ error_message | string | Thông báo lỗi liên quan đến chiến dịch thất bại. |

### Ví dụ lệnh cURL (Example)

```http
// Success-Response
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "campaign_list": [
            {
                "campaign_id": "{{campaign_id}}",
                "status": "DISABLE"
            }
        ],
        "error_list": []
    }
}
```

---

<a id="doc-1866528879472641"></a>
<!-- doc_id: 1866528879472641 -->
<!-- doc_id: 1866528879472641 -->
# Tạo tác vụ sao chép bất đồng bộ cho chiến dịch Smart+ nâng cấp (Create an asynchronous copy task for an Upgraded Smart+ Campaign)
> Đường dẫn: API Reference > Smart+ nâng cấp > Campaigns > Create an asynchronous copy task for an Upgraded Smart+ Campaign
Sử dụng endpoint này để tạo an asynchronous copy task for an Upgraded Smart+ Campaign.

Bạn chỉ có thể sao chép một chiến dịch tại một thời điểm. Để tìm hiểu các bước chi tiết, xem [Sao chép chiến dịch Smart+ nâng cấp](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1874421347053569).

> **Note:** 
> - Asynchronous Campaign Copy API hiện là tính năng chỉ dành cho danh sách cho phép (allowlist-only). Nếu bạn muốn sử dụng, vui lòng liên hệ với đại diện TikTok của bạn.
> - The rate limits for this endpoint are 1 query per second (QPS) and 30 queries per minute (QPM) per developer app. [Global rate limits](../04-get-started/bat-dau.md#doc-1740029171730433) are not applicable to this endpoint.

## Yêu cầu gọi API (Request)
**Endpoint** https://business-api.tiktok.com/open_api/v1.3/smart_plus/campaign/copy/task/create/

**Method** POST

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type  ****(Bắt buộc)**** | string | Định dạng dữ liệu yêu cầu. ⏎ Allowed value: `application/json`. |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|advertiser_id ***(Bắt buộc)***|string|ID tài khoản quảng cáo TikTok.|
|request_id ***(Bắt buộc)***|string|Request ID that supports idempotency to prevent you from sending the same request twice. If you retry requests with the same request ID multiple times within the 10-second cache time, then only one request will succeed. If a duplicate request with the expired request ID is received after the cache time, the server will treat it as a new request and process it accordingly.<br><br>It is different from the `request_id` returned in the response parameters, which is used to uniquely identify an HTTP request.<br><br>The value should be a string representation of a 64-bit integer.<br><br>Example: `"123456789"`.|
|campaign_id ***(Bắt buộc)***|string|The ID of an Upgraded Smart+ Campaign that you want to copy. <br><br>To retrieve Upgraded Smart+ Campaigns within your ad account, use [/smart_plus/campaign/get/](62-upgraded-smartplus-p1.md#doc-1843312818332930).<br><br><p><span style="color:darkred"><b>Note</b></span>: <ul><li>The source campaign must use one of these advertising objectives: `APP_PROMOTION`, `LEAD_GENERATION`, `WEB_CONVERSIONS`</li><li>The source campaign must not be deleted.</li><li>The source campaign must contain at least 1 undeleted ad group, which must contain at least 1 undeleted ad.</li><li>The source campaign must satisfy all per-level limits, and the total copied assets must also not exceed the global new campaign limits:<ul><li>On the source campaign: you may have a maximum of 10 undeleted ad groups, each ad group may contain a maximum of 30 undeleted ads, and each individual ad may use a maximum of 50 creatives.</li><li>Separately, there are hard global caps that apply to the resulting new campaign: no more than 200 total ads may be copied over, and no more than 1,000 total creatives may be copied into the new campaign.</li></ul></li></ul>|
|operation_status|string|The status of the new campaign when created.<br><br>Các giá trị enum hỗ trợ: <ul><li>`ENABLE`: The campaign is enabled when created.</li><li>`DISABLE`: The campaign is disabled when created.</li></ul><br>Giá trị mặc định: `DISABLE`.<br><br>If you want to update the status of the campaign after creation, use [/smart_plus/campaign/status/update/](62-upgraded-smartplus-p1.md#doc-1843312888885314).|
|campaign_name|string|The name for the new campaign.<br><br>Giới hạn độ dài: 512 characters. Emojis are not supported. Each word in Chinese or Japanese counts as two characters, while each letter in English counts as one character.<br><br>If not specified, this field will default to `"COPIED_&#123;&#123;name_of_the_source_campaign&#125;&#125;"`. For instance, if the source campaign is named `"FIRST_CAMPAIGN"` and this field is not specified, the name of the new campaign will be `"COPIED_FIRST_CAMPAIGN"`.<br><br>|
|budget|number|Ngân sách cho chiến dịch mới hoặc giới hạn ngân sách cho tất cả các nhóm quảng cáo trong chiến dịch mới.<br><br>Để biết các quy tắc thiết lập trường này, xem [Ngân sách chiến dịch](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1745292231199745).|
|schedule_type|string|<ul><li>Specify this field only when you want to set the same schedule for all ad groups in the new campaign.</li><li>If you want to use schedules of the source ad groups in the new campaign, leave this field unspecified.</li></ul><br>Schedule type for all new ad groups.<br><br>Các giá trị enum hỗ trợ: <ul><li>`SCHEDULE_START_END`: Set start time and end time to run ad groups. You need to pass both `schedule_start_time` and `schedule_end_time` at the same time.</li><li>`SCHEDULE_FROM_NOW`: Set start time to run ad groups continuously. You need to pass `schedule_start_time` and the end time will be automatically set to 10 years later than the start time.</li></ul>|
|schedule_start_time **(Điều kiện)**|string|Bắt buộc khi `schedule_type` is passed.<br><br>Schedule start time (UTC+0) for all new ad groups, in the format of `YYYY-MM-DD HH:MM:SS`.<br><br>The start time can be up to 12 hours earlier than the current time, but cannot be later than `2028-01-01 00:00:00`.|
|schedule_end_time **(Điều kiện)**|string|<ul><li>Bắt buộc khi `schedule_type` is `SCHEDULE_START_END`.</li><li>Not supported when `schedule_type` is `SCHEDULE_FROM_NOW`.</li></ul><br>Schedule end time (UTC+0) for all new ad groups, in the format of `YYYY-MM-DD HH:MM:SS`.<br><br>The end time cannot be later than `2038-01-01 00:00:00`.|
|dayparting|string|Phân bổ thời gian phân phối quảng cáo theo khung giờ cho tất cả các nhóm quảng cáo trong chiến dịch mới, định dạng chuỗi gồm 48 x 7 ký tự.<br><br>Mỗi ký tự tương ứng với một khung thời gian 30 phút từ Thứ Hai đến Chủ Nhật (1: có phân phối, 0: không phân phối). Chuỗi toàn 0 hoặc toàn 1 được coi là phân phối toàn thời gian.|
|deep_copy_mode|string|Chế độ sao chép xác định cách tạo nhóm quảng cáo và quảng cáo trong chiến dịch mới. <br><br>Các giá trị enum hỗ trợ: <ul><li>`DEFAULT`: Chế độ sao chép mặc định. Sao chép tất cả các nhóm quảng cáo và quảng cáo chưa bị xóa từ chiến dịch nguồn sang chiến dịch mới. Có thể bỏ qua trường `adgroup_list` vì API sẽ bỏ qua trường này trong chế độ mặc định.</li><li>`CUSTOM`: Chế độ sao chép tùy chỉnh. Chỉ sao chép các nhóm quảng cáo và quảng cáo chưa bị xóa được chỉ định từ chiến dịch nguồn sang chiến dịch mới. Bạn cũng có thể tùy chỉnh các cài đặt nhóm quảng cáo hoặc quảng cáo để ghi đè cấu hình nguồn.<ul><li>Khi sử dụng chế độ này, bạn cần cung cấp đồng thời trường `adgroup_list`. Bạn có thể sao chép tối đa 20 quảng cáo trên mỗi nhóm quảng cáo, tối đa 30 nhóm quảng cáo.</li></ul></li></ul> Giá trị mặc định: `DEFAULT`.|
|adgroup_list|object[]|<ul><li>When `deep_copy_mode` is set to `DEFAULT` or not passed, this field is ignored.</li><li>When `deep_copy_mode` is set to `CUSTOM`, this field is required.</li></ul><br>Cài đặt tùy chỉnh cho các nhóm quảng cáo trong chiến dịch mới.<br><br>Kích thước tối đa: 10.|
#|adgroup_id {+Conditional}|string|Bắt buộc khi `adgroup_list` is passed.<br><br>ID của nhóm quảng cáo bạn muốn sao chép. Nhóm quảng cáo phải thuộc chiến dịch nguồn (`campaign_id`).|
#|operation_status|string|Trạng thái của nhóm quảng cáo mới khi được tạo.<br><br>Các giá trị enum hỗ trợ: <ul><li>`ENABLE`: Nhóm quảng cáo được bật khi tạo.</li><li>`DISABLE`: Nhóm quảng cáo bị tắt khi tạo.</li></ul><br>Giá trị mặc định: `ENABLE`.<br><br>Nếu bạn muốn cập nhật trạng thái của nhóm quảng cáo sau khi tạo, sử dụng [/smart_plus/adgroup/status/update/](62-upgraded-smartplus-p4.md#doc-1843314908153858).|
#|adgroup_name|string|Tên cho nhóm quảng cáo mới.<br><br>Giới hạn độ dài: 512 ký tự. Không hỗ trợ biểu tượng cảm xúc (emoji).<br> Mỗi từ tiếng Trung hoặc tiếng Nhật tính là 2 ký tự, mỗi chữ cái tiếng Anh tính là 1 ký tự.<br><br>Nếu không chỉ định, trường này sẽ mặc định lấy tên của nhóm quảng cáo nguồn.|
#|budget|number|<ul><li>Valid when Campaign Budget Optimization (CBO) is disabled (`budget_optimize_on` is `false`) at the campaign level.</li><li>Ignored when CBO is enabled (`budget_optimize_on` is `true`) at the campaign level.</li></ul><br>Ngân sách cố định hoặc ngân sách ban đầu cho nhóm quảng cáo mới.<ul><li>Khi `budget_auto_adjust_strategy` của nhóm quảng cáo nguồn là `UNSET`, trường này đại diện cho ngân sách cố định cho nhóm quảng cáo mới.</li><li>Khi `budget_auto_adjust_strategy` là `AUTO_BUDGET_INCREASE`, trường này đại diện cho ngân sách ban đầu cho nhóm quảng cáo mới. Để lấy ngân sách nhóm quảng cáo hiện tại, sử dụng [/smart_plus/adgroup/get/](62-upgraded-smartplus-p2.md#doc-1843314879617026) sau khi hoàn tất tác vụ sao chép và kiểm tra `current_budget` được trả về.</li></ul>|
#|min_budget|number|Chỉ hợp lệ khi the following conditions are all met:<ul><li>At the campaign level:<ul><li>`budget_optimize_on` is `true`</li><li>`budget_mode` is `BUDGET_MODE_DYNAMIC_DAILY_BUDGET`</li></ul></li><li>At the ad group level:<ul><li>`bid_type` is `BID_TYPE_NO_BID`</li></ul></li></ul><br>Ngân sách tối thiểu của nhóm quảng cáo.<br><br>Hệ thống sẽ cố gắng chi tiêu ít nhất số tiền này nhưng không đảm bảo tuyệt đối.|
#|targeting_spec|object|<ul><li>Chỉ chỉ định trường này khi bạn muốn tùy chỉnh các cài đặt nhắm mục tiêu cho nhóm quảng cáo mới trong chiến dịch mới.</li><li>Nếu bạn muốn dùng cùng cài đặt nhắm mục tiêu của nhóm quảng cáo nguồn trong chiến dịch mới, hãy để trống trường này.</li></ul><br>Cài đặt nhắm mục tiêu.|
##|location_ids|string[]|Danh sách ID vị trí bạn muốn nhắm mục tiêu trong nhóm quảng cáo mới.<br><br>Để lấy các vị trí khả dụng và ID tương ứng dựa trên vị trí hiển thị và mục tiêu, sử dụng endpoint [/tool/targeting/search/](70-tools-p1.md#doc-1761236883355649) hoặc [/tool/region/](70-tools-p1.md#doc-1737189539571713).<br><p><span style="color:darkred"><b>Lưu ý</b></span>: Nếu bạn thêm Hoa Kỳ (US) làm vị trí mục tiêu, bạn sẽ không thể xóa Hoa Kỳ sau khi tạo nhóm quảng cáo.|
##|zipcode_ids|string[]|Zip code IDs or postal code IDs that you want to use to target locations in the new ad group.<br><br>Kích thước tối đa: 3,000. If you provide both `location_ids` and `zipcode_ids`, the combined total of location IDs, zip code IDs, and postal code IDs cannot exceed 3,000 per ad group.<br><br>You can get the available zip code IDs or postal code IDs based on your placement, objective and keyword via `geo_id` (when `geo_type` = `ZIP_CODE`) returned from the [/tool/targeting/search/](70-tools-p1.md#doc-1761236883355649) endpoint. <br><br><p><span style="color:darkred"><b>Note</b></span>:<ul><li>Zip code targeting is currently only supported for the US and postal code targeting is currently only supported for Canada, Brazil, Indonesia, Thailand, and Vietnam.</li><li>Targeting postal code areas in Brazil, Indonesia, Thailand, and Vietnam is currently an allowlist-only feature. If you would like to access it, please contact your TikTok representative.</li><li>You cannot use zip code targeting or postal code targeting in campaigns that have enabled special ad categories (`special_industries`).</li><li>Overlapping targeted locations are not supported. For instance, you cannot target the US and the state of California at the same time.</li><li>If you target locations in the US via `location_ids` or `zipcode_ids` during ad group creation, you can subsequently update those IDs to other US locations but you cannot remove all US locations to target only non-US countries.</li><li>To get information about the zip code IDs or postal code IDs, you can only use [/tool/targeting/info/](70-tools-p1.md#doc-1761237001980929).</li></ul>|
##|excluded_audience_ids|string[]|Danh sách ID đối tượng cần loại trừ.<br><br>Để lấy danh sách ID đối tượng, sử dụng [/dmp/custom_audience/list/](09-audience.md#doc-1739940506015746).|
##|audience_ids|string[]|Danh sách ID đối tượng.<br><br>Để lấy danh sách ID đối tượng, sử dụng [/dmp/custom_audience/list/](09-audience.md#doc-1739940506015746).|
##|saved_audience_id|string|Valid when the following conditions are both met:<ul><li>The `targeting_optimization_mode` of the source ad group is `MANUAL`.</li><li>The category of Housing, Employment, or Credit (`specical_industries`) is NOT specified in your campaign.</li><li>TikTok placement is selected in your ad group (i.e., `placement_type` is set as `PLACEMENT_TYPE_AUTOMATIC` <b>or</b> `placement_type` is set as `PLACEMENT_TYPE_NORMAL` and `PLACEMENT_TIKTOK` is included in `placements`).</li></ul><br>Saved Audience ID.<br><br>To obtain the list of Saved Audiences within your ad account, use [/dmp/saved_audience/list/](09-audience.md#doc-1780154619404290).<br><br>Before using this field, call [/dmp/saved_audience/create/](09-audience.md#doc-1780154541898754) to create a Saved Audience and get the Saved Audience ID in response. The ID tài khoản quảng cáo TikTok associated with your Saved Audience should be the same as the ID tài khoản quảng cáo TikTok in your ad group. Otherwise, an error will occur.<br><br>If you use `saved_audience_id` to create an ad group, we will return both the Saved Audience ID and the targeting options that are included within your Saved Audience in response.<br><br><p><span style="color:darkred"><b>Note</b></span>:<ul><li>When creating a Saved Audience via [/dmp/saved_audience/create/](09-audience.md#doc-1780154541898754), you can specify various targeting options, including `gender`. However, be aware that if you are creating an ad group based on a Saved Audience, it’s essential to avoid setting both the `saved_audience_id` and targeting options (such as `gender`) defined within your Saved Audience at the same time.</li><li>In cases where the targeting settings in your Saved Audience conflict with those in your ad group, the settings from your Saved Audience will take precedence. As a result, the conflicting targeting options in your ad group will be ignored.<ul><li>For example, if you create a Saved Audience where `gender` is set to `GENDER_FEMALE` and then use that Saved Audience to create an ad group while specifying `gender` as `GENDER_MALE`, the resulting ad group will adopt `GENDER_FEMALE` as the gender targeting configuration, reflecting what is set in the Saved Audience.</li></ul></li><li>If the `saved_audience_id` was created with `age_groups` specified, the age restriction rules outlined in [New age restrictions for ads on TikTok](../15-appendix/phu-luc-p1.md#doc-1788755983247362) for different advertising objectives also apply. Make sure that the age targeting setting is allowed before you use the Saved Audience (`saved_audience_id` ) in the ad group.</li></ul>|
#|ad_list {+Conditional}|object[]|<ul><li>When `deep_copy_mode` is set to `DEFAULT` or not passed, this field is ignored.</li><li>When `deep_copy_mode` is set to `CUSTOM`, this field is required.<ul><li>If you don't want to customize the settings of the ads to be generated in the new ad group, only pass `ad_id` in this object array.</li><li>If you want to customize the settings of the ads to be generated in the new ad group, pass `ad_id` and other parameters simultaneously in this object array.</li></ul></li></ul><br>The settings for ads in the new ad group.<br><br>Kích thước tối đa: 30.<br><br><p><span style="color:darkred"><b>Note</b></span>: The maximum number of ads that you can specify in the new campaign is 200.</p>|
##|smart_plus_ad_id {+Conditional}|string|Bắt buộc khi `ad_list` is passed.<br><br>The ID of the ad that you want to copy. The ad should belong to the source ad group (`adgroup_id`).|
##|operation_status|string|The status of the new ad when created.<br><br>Các giá trị enum hỗ trợ: <ul><li>`ENABLE`: The ad is enabled when created.</li><li>`DISABLE`: The ad is disabled when created.</li></ul><br>Giá trị mặc định: `ENABLE`.<br><br>If you want to update the status of the ad after creation, use [/smart_plus/ad/status/update/](62-upgraded-smartplus-p6.md#doc-1843317423164482).|
##|ad_name|string|The name for the new ad.<br><br>Giới hạn độ dài: 512 characters. Emojis are not supported. Each word in Chinese or Japanese counts as two characters, while each letter in English counts as one character.<br><br>If not specified, this field will default to `"COPIED_&#123;&#123;name_of_the_source_ad&#125;&#125;_&#123;&#123;ID_of_the_source_ad&#125;&#125;"`. For instance, if the source ad is named `"FIRST_AD"` with the ID mẫu quảng cáo 1234567891234567, and this field is not specified, the name of the new ad will be `"COPIED_FIRST_AD_1234567891234567"`.<br><br>|
##|creative_list|object[]|Danh sách các mẫu quảng cáo. Khoảng kích thước: 1-50.<br><br><p><span style="color:darkred"><b>Lưu ý</b></span>: Khi bạn cung cấp trường này, các mẫu quảng cáo trong nhóm quảng cáo mới sẽ bị ghi đè hoàn toàn.|
###|creative_info {+Conditional}|object|Bắt buộc khi `creative_list` is specified.<br><br> Creative information.|
####|ad_format {+Conditional}|string|Bắt buộc khi `creative_info` is specified.<br><br> The ad format.<ul><li>`SINGLE_VIDEO`: Single Video.<ul><li>To use this format, specify any of the following:<ul><li>a video through `video_id` and a video cover through `web_uri`</li><li>a TikTok video post through `tiktok_item_id`.</li></ul></li></ul></li><li>`CAROUSEL_ADS`: Standard Carousel.<ul><li>To use this format, specify any of the following:<ul><li>carousel images through `web_uri` and a piece of music through `music_id`.</li><li>TikTok photo posts images through `tiktok_item_id`.</li></ul></li></ul> </li></ul><br><p><span style="color:darkred"><b>Note</b></span>: You can copy a Standard Carousel ad into a Single Video ad and vice versa.</p>|
####|video_info {+Conditional}|object|Bắt buộc đối với quảng cáo Spark Ads Video đơn thông qua Spark Ads Push hoặc quảng cáo Video không phải Spark Ads.<br><br>Chi tiết về video.|
######|video_id {+Conditional}|string|Bắt buộc khi `video_info` is specified.<br><br>Video ID.<br><br>To upload a video and obtain the video ID, use [/file/video/ad/upload/](71-video.md#doc-1737587322856449). <br>To search for videos within your ad account, use [/file/video/ad/search/](71-video.md#doc-1740050472224769).|
######|file_name|string|Tên video.|
####|image_info {+Conditional}|object[]|Bắt buộc đối với các loại quảng cáo Carousel (Spark Ads Standard Carousel hoặc Standard Carousel thông thường).<br><br>Chi tiết về hình ảnh.|
######|web_uri {+Conditional}|string|Bắt buộc khi `image_info` is specified.<br><br>Image ID.<br><br>To upload an image and obtain the image ID, use [/file/image/ad/upload/](47-images.md#doc-1739067433456642).<br> To search for images within your ad account, use [/file/image/ad/search/](47-images.md#doc-1740052016789506).|
####|music_info {+Conditional}|object|Bắt buộc khi tạo quảng cáo Standard Carousel thông thường sử dụng âm nhạc.<br><br>Chi tiết về âm nhạc.|
######|music_id {+Conditional}|string|Bắt buộc khi `music_info` is specified.<br><br>The ID of the piece of music to use in the carousel ads.|
####|aigc_disclosure_type|string|Có thực hiện turn on the AIGC (Artificial Intelligence Generated Content) self-disclosure toggle to indicate the ad contains AI-generated content. After the toggle is turned on, your ad will carry an "Advertiser labeled as Al-generated" label when viewed in full.<br><br>Các giá trị enum hỗ trợ: <ul><li>`SELF_DISCLOSURE`: To turn on the toggle to declare that the ad contains AI-generated content.</li><li>`NOT_DECLARED`: To not declare that the ad contains AI-generated content. Giá trị mặc định: `NOT_DECLARED`.</li></ul>|
####|tiktok_item_id {+Conditional}|string|<ul><li>Bắt buộc khi you create Spark Ads through Spark Ads Pull, including:<ul><li>Spark Ads Single Video ads through Spark Ads Pull. You need to specify a TikTok video post.</li><li>Spark Ads Standard Carousel ads through Spark Ads Pull. You need to specify a TikTok photo post.</li></ul></li><li>Not supported when `catalog_creative_toggle` is `true`.</li></ul><br>The ID of the TikTok post to be used as an ad (Spark Ads).<br><br>Pass in the `item_id` you get from the response of the [/tt_video/info/](64-spark-ads-using-authorized-posts.md#doc-1738376324021250) and [/identity/video/get/](46-identity.md#doc-1740218475032577) endpoints.<br><br>When you pass in `tiktok_item_id`, you don't need to pass in the objects `image_info`, `video_info`, and `ad_text_list`. <br><br><p><span style="color:darkred"><b>Note</b></span>: By using Spark Ads, you confirm that you have the rights to use the music in the videos for commercial purposes.|
####|identity_type {+Conditional}|string|Bắt buộc khi you create Spark Ads.<br><br>Identity type for Spark Ads.<br><br>Các giá trị enum hỗ trợ: `AUTH_CODE`, `TT_USER`, `BC_AUTH_TT`.<br><br>For details about identities, see [Identities](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1738958351620097).|
####|identity_id {+Conditional}|string|Bắt buộc khi you create Spark Ads.<br><br>Identity ID for Spark Ads.|
####|identity_authorized_bc_id {+Conditional}|string|Bắt buộc khi `identity_type` is `BC_AUTH_TT`.<br><br>ID of the Business Center that a TikTok Account User in Business Center identity is associated with.|
##|ad_text_list {+Conditional}|object[]|Bắt buộc khi `tiktok_item_id` is not specified.<br><br>List of ad texts. <br>Ad texts are shown to your audience as part of your ad creatives, to deliver the message you intend to communicate to them.<br><br>Kích thước tối đa: 5.|
###|ad_text {+Conditional}|string|Bắt buộc khi `ad_text_list` is specified.<br><br>Văn bản quảng cáo.|
##|call_to_action_list {+Conditional}|object[]|Call-to-action list.<br><br>Kích thước tối đa: 3.<br><br><p><span style="color:darkred"><b>Note</b></span>: This field is not supported in any of the following scenarios and you need to use `call_to_action_id` instead.<ul><li>Scenario 1:<ul><li>At the campaign level, `objective_type` is `LEAD_GENERATION`.</li><li>At the ad group level, `placement_type` is `PLACEMENT_TYPE_NORMAL` and `placements` includes `PLACEMENT_TIKTOK`, or `placement_type` is `PLACEMENT_TYPE_AUTOMATIC`.</li></ul></li><li>Scenario 2:<ul><li>At the campaign level, `objective_type` is `APP_PROMOTION` or `WEB_CONVERSIONS`.</li><li>At the ad group level, `placement_type` is `PLACEMENT_TYPE_NORMAL` and `placements` includes `PLACEMENT_TIKTOK`, or `placement_type` is `PLACEMENT_TYPE_AUTOMATIC`.</li><li>At the ad level, `identity_type` within the `creative_info` object to `TT_USER`, `BC_AUTH_TT`, or `AUTH_CODE`.</li></ul></li></ul>|
###|call_to_action {+Conditional}|string|Bắt buộc khi `call_to_action_list` is specified.<br><br>Văn bản lời kêu gọi hành động (CTA).<br><br>Để xem danh sách giá trị enum, xem [Enumeration - Call-to-action](../15-appendix/phu-luc-p1.md#doc-1737174886619138).|
##|landing_page_url_list|object[]|Danh sách URL trang đích.<br><br>Khoảng kích thước: 0-1.|
###|landing_page_url {+Conditional}|string|Bắt buộc khi `landing_page_url_list` is specified.<br><br>URL trang đích.|
##|ad_configuration|object|Các cấu hình bổ sung.|
###|utm_params|object[]|Valid when `objective_type` is `WEB_CONVERSIONS` at the campaign level.<br><br>Danh sách các tham số URL (URL parameters). Tham số URL là các đoạn mã được gắn vào cuối URL giúp bạn theo dõi lượt nhấp qua các kênh khác nhau và hiểu cách khách truy cập tương tác với trang web thông qua các nền tảng phân tích bên thứ ba. Chúng bao gồm các cặp khóa-giá trị được chỉ định qua `key` và `value`.<br><br>Kích thước tối đa: 14.<br><br>Nếu bạn đặt `landing_page_url` thành một URL đã có sẵn các tham số URL, bạn có thể truyền `utm_params` đồng thời để lưu trữ các tham số này. Trong trường hợp đó, bạn cần đảm bảo `utm_params` khớp chính xác với các tham số đã dùng trong URL. Các tham số URL sẽ không được tự động gắn thêm vào `landing_page_url` khi phân phối quảng cáo.|
####|key|string|Các tham số UTM được hỗ trợ gồm:<ul><li>`utm_source`: Ứng dụng, trang web mang lại lưu lượng truy cập. Ví dụ: TikTok.</li><li>`utm_medium`: Phương tiện quảng cáo hoặc tiếp thị. Ví dụ: cpm, cpc, banner, video.</li><li>`utm_content`: Nội dung mẫu quảng cáo dùng để quảng bá. Ví dụ: tên quảng cáo, văn bản CTA, tài sản, màu sắc, v.v.</li><li>`utm_campaign`: Tên chiến dịch cụ thể, khẩu hiệu hoặc mã khuyến mại. Ví dụ: BlackFridayProm. Lưu ý rằng các tham số UTM có phân biệt chữ hoa chữ thường.</li></ul><br>Giới hạn độ dài khi chỉ định tham số tùy chỉnh: 100 ký tự.|
####|value|string|Giá trị của tham số URL.<br><br>Bạn có thể chỉ định giá trị tùy chỉnh hoặc tên của một macro.<br><br>Các macro được hỗ trợ gồm:<ul><li>`CAMPAIGN_NAME`: Sẽ được thay thế bằng tên chiến dịch của bạn.</li><li>`CAMPAIGN_ID`: Sẽ được thay thế bằng ID chiến dịch quảng cáo của bạn.</li><li>`AID_NAME`: Sẽ được thay thế bằng tên nhóm quảng cáo của bạn.</li><li>`AID`: Sẽ được thay thế bằng ID nhóm quảng cáo của bạn.</li><li>`CID_NAME`: Sẽ được thay thế bằng tên quảng cáo của bạn.</li><li>`CID`: Sẽ được thay thế bằng ID mẫu quảng cáo của bạn.</li><li>`PLACEMENT`: Sẽ được thay thế bằng vị trí hiển thị của bạn.</li></ul><br>Giới hạn độ dài khi chỉ định giá trị tùy chỉnh: 600 ký tự.|
###|call_to_action_id|string|Valid in any of the following scenarios:<ul><li>Scenario 1:<ul><li>At the campaign level `objective_type` is `LEAD_GENERATION`.</li><li>At the ad group level, `placement_type` is `PLACEMENT_TYPE_NORMAL` and `placements` includes `PLACEMENT_TIKTOK`, or `placement_type` is `PLACEMENT_TYPE_AUTOMATIC`.</li></ul></li><li>Scenario 2:<ul><li>At the campaign level, `objective_type` is `APP_PROMOTION` or `WEB_CONVERSIONS`.</li><li>At the ad group level, `placement_type` is `PLACEMENT_TYPE_NORMAL` and `placements` includes `PLACEMENT_TIKTOK`, or `placement_type` is `PLACEMENT_TYPE_AUTOMATIC`.</li><li>At the ad level, `identity_type` within the `creative_info` object to `TT_USER`, `BC_AUTH_TT`, or `AUTH_CODE`.</li></ul></li></ul><br>ID của danh mục lời kêu gọi hành động (CTA) (còn gọi là CTA động) bạn muốn sử dụng trong quảng cáo. Danh mục CTA là một nhóm các CTA được tự động tối ưu hóa.<br><br>Để biết chi tiết về CTA tự động tối ưu hóa, xem [Đề xuất CTA > CTA động](../09-marketing-api/creatives.md#doc-1740307296329730).|

### **Example**

Depending on Liệu you want to use default settings or apply custom settings at different levels, ad group or ad settings, you can copy a campaign using any of the following code examples:

#### Chế độ sao chép mặc định: nhân bản chính xác tất cả cài đặt từ chiến dịch nguồn
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/smart_plus/campaign/copy/task/create/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id": {{advertiser_id}},
    "request_id": "{{request_id}}",
    "campaign_id": "{{campaign_id}}"
}'
```

#### Chế độ sao chép mặc định: ghi đè cấp chiến dịch và dùng chung lịch chạy cho các nhóm quảng cáo mới
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/smart_plus/campaign/copy/task/create/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id": "{{advertiser_id}}",
    "request_id": "{{request_id}}",
    "campaign_id": "{{campaign_id}}",
    "operation_status": "ENABLE",
    "campaign_name": "{{campaign_name}}",
    "budget": {{budget}},
    "schedule_type": "SCHEDULE_START_END",
    "schedule_start_time": "{{schedule_start_time}}",
    "schedule_end_time": "{{schedule_end_time}}",
    "deep_copy_mode": "DEFAULT"
}'
```

#### Chế độ sao chép tùy chỉnh: ghi đè cấp chiến dịch, dùng chung lịch chạy cho nhóm quảng cáo mới và ghi đè cấp nhóm quảng cáo
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/smart_plus/campaign/copy/task/create/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id": "{{advertiser_id}}",
    "request_id": "{{request_id}}",
    "campaign_id": "{{campaign_id}}",
    "operation_status": "ENABLE",
    "campaign_name": "{{campaign_name}}",
    "budget": {{budget}},
    "schedule_type": "SCHEDULE_START_END",
    "schedule_start_time": "{{schedule_start_time}}",
    "schedule_end_time": "{{schedule_end_time}}",
    "deep_copy_mode": "CUSTOM",
    "adgroup_list": [
        {
            "adgroup_id": "{{adgroup_id}}",
            "operation_status": "ENABLE",
            "adgroup_name": "{{adgroup_name}}",
            "budget": {{budget}},
            "targeting_spec": {
                "location_ids": [
                    "{{location_ids}}"
                ]
            },
            "ad_list": [
                {
                    "smart_plus_ad_id": "{{smart_plus_ad_id}}"
                }
            ]
        }
    ]
}'
```

#### Chế độ sao chép tùy chỉnh: ghi đè cấp chiến dịch, dùng chung lịch chạy cho nhóm quảng cáo mới, ghi đè cấp nhóm quảng cáo và ghi đè cấp quảng cáo
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/smart_plus/campaign/copy/task/create/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id": "{{advertiser_id}}",
    "request_id": "{{request_id}}",
    "campaign_id": "{{campaign_id}}",
    "operation_status": "ENABLE",
    "campaign_name": "{{campaign_name}}",
    "schedule_type": "SCHEDULE_START_END",
    "schedule_start_time": "{{schedule_start_time}}",
    "schedule_end_time": "{{schedule_end_time}}",
    "deep_copy_mode": "CUSTOM",
    "adgroup_list": [
        {
            "adgroup_id": "{{adgroup_id}}",
            "operation_status": "ENABLE",
            "adgroup_name": "{{adgroup_name}}",
            "budget": {{budget}},
            "targeting_spec": {
                "location_ids": [
                    "{{location_ids}}"
                ]
            },
            "ad_list": [
                {
                    "smart_plus_ad_id": "{{smart_plus_ad_id}}",
                    "operation_status": "ENABLE",
                    "ad_name": "{{ad_name}}",
                    "creative_info": {
                        "ad_format": "SINGLE_VIDEO",
                        "identity_type": "BC_AUTH_TT",
                        "identity_id": "{{identity_id}}",
                        "identity_authorized_bc_id": "{{identity_authorized_bc_id}}",
                        "image_info": [
                            {
                                "web_uri": "{{web_uri}}"
                            }
                        ],
                        "video_info": {
                            "file_name": "{{file_name}}",
                            "video_id": "{{video_id}}"
                        }
                    },
                    "ad_text_list": [
                        {
                            "ad_text": "{{ad_text}}"
                        }
                    ],
                    "ad_configuration": {
                        "call_to_action_id": "{{call_to_action_id}}"
                    }
                }
            ]
        }
    ]
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
| ↳ task_id | string | ID của tác vụ sao chép chiến dịch bất đồng bộ. ⏎ Để kiểm tra kết quả của tác vụ, sử dụng [/smart_plus/campaign/copy/task/check/](62-upgraded-smartplus-p1.md#doc-1866529943741441). |
| ↳ adgroup_error_list | object[] | Các lỗi phát sinh trong quá trình sao chép các nhóm quảng cáo cụ thể. |
| ↳↳ adgroup_id | string | ID của nhóm quảng cáo sao chép không thành công. |
| ↳↳ error_message | string | Lỗi phát sinh trong quá trình sao chép nhóm quảng cáo (`adgroup_id`). |

### Ví dụ lệnh cURL (Example)
```http
// curl
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "task_id": "{{task_id}}"
    }
}
```

---

<a id="doc-1866529943741441"></a>
<!-- doc_id: 1866529943741441 -->
<!-- doc_id: 1866529943741441 -->
# Lấy kết quả tác vụ sao chép bất đồng bộ cho chiến dịch Smart+ nâng cấp (Get the results of an asynchronous copy task for an Upgraded Smart+ Campaign)
> Đường dẫn: API Reference > Smart+ nâng cấp > Campaigns > Get the results of an asynchronous copy task for an Upgraded Smart+ Campaign
Sử dụng endpoint này để kiểm tra the results of an asynchronous copy task for an Upgraded Smart+ Campaign.

Chúng tôi khuyến nghị nên đợi khoảng 5 phút sau khi tạo tác vụ bằng endpoint [/smart_plus/campaign/copy/task/create/](62-upgraded-smartplus-p1.md#doc-1866528879472641) trước khi kiểm tra kết quả.

> **Note:** 
> - Asynchronous Campaign Copy API hiện là tính năng chỉ dành cho danh sách cho phép (allowlist-only). Nếu bạn muốn sử dụng, vui lòng liên hệ với đại diện TikTok của bạn.
> - [Giới hạn tần suất toàn cầu](../04-get-started/bat-dau.md#doc-1740029171730433) được áp dụng cho endpoint này.

## Yêu cầu gọi API (Request)
**Endpoint** https://business-api.tiktok.com/open_api/v1.3/smart_plus/campaign/copy/task/check/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id ***(Bắt buộc)*** | string | ID tài khoản quảng cáo TikTok.|
| task_id ***(Bắt buộc)*** | string | ID of the asynchronous campaign copy task.<br><br>To get the task ID, use [/smart_plus/campaign/copy/task/create/](62-upgraded-smartplus-p1.md#doc-1866528879472641).|

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/smart_plus/campaign/copy/task/check/?advertiser_id={{advertiser_id}}&task_id={{task_id}}' \
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
| ↳ task_status | string | The status of the asynchronous campaign copy task. ⏎ Các giá trị enum hỗ trợ: • `RUNNING`: The task is being processed. • `SUCCESS`: The task has been processed. Check the `task_result` to see if the task has succeeded. • `FAILURE`: The task fails to be processed. |
| ↳ task_info | object | Tổng quan về kết quả tác vụ. |
| ↳↳ total_ad_count | number | Tổng số lượng quảng cáo bạn đã cố gắng sao chép. |
| ↳↳ success_ad_count | number | Số lượng quảng cáo đã được sao chép thành công. |
| ↳ task_result | object | Chi tiết kết quả tác vụ. |
| ↳↳ campaign_id | string | ID của chiến dịch mới được tạo. |
| ↳↳ campaign_name | string | Tên của chiến dịch mới được tạo. ⏎ Nếu quá trình sao chép chiến dịch thất bại, trường này vẫn được trả về để cho biết chiến dịch chưa được sao chép thành công. |
| ↳↳ campaign_error_infos | string[] | Các lỗi phát sinh trong quá trình sao chép chiến dịch. ⏎ Nếu không có lỗi, giá trị trường này là danh sách trống (`[]`). |
| ↳↳ adgroup_result_list | object[] | Chi tiết kết quả sao chép nhóm quảng cáo. |
| ↳↳↳ adgroup_id | string | ID của nhóm quảng cáo mới được tạo. |
| ↳↳↳ adgroup_name | string | Tên của nhóm quảng cáo mới được tạo. ⏎ Nếu quá trình sao chép nhóm quảng cáo thất bại, trường này vẫn được trả về để cho biết nhóm quảng cáo chưa được sao chép thành công. |
| ↳↳↳ total_ad_count | number | Số lượng quảng cáo bạn đã cố gắng sao chép vào nhóm quảng cáo mới. |
| ↳↳↳ success_ad_count | number | Số lượng quảng cáo đã được sao chép thành công vào nhóm quảng cáo mới. |
| ↳↳↳ adgroup_error_list | string[] | Các lỗi phát sinh trong quá trình sao chép nhóm quảng cáo. ⏎ Nếu không có lỗi, giá trị trường này là danh sách trống (`[]`). |
| ↳↳↳ ad_status | string | The result of copying the ads from the source ad group to the newly created ad group. ⏎ Các giá trị enum hỗ trợ: • `ALL_SUCCESS`: All ads from the source ad group were successfully copied. • `PARTIAL_SUCCESS`: Some or all ads from the source ad group failed to be copied. |
| ↳↳↳ ad_result_list | object[] | Chi tiết kết quả sao chép quảng cáo. |
| ↳↳↳↳ is_success | boolean | Liệu copy of the source ad was successful. ⏎ Các giá trị được hỗ trợ: `true`, `false`. |
| ↳↳↳↳ smart_plus_ad_id | string | ID của quảng cáo mới được tạo. |
| ↳↳↳↳ ad_name | string | Tên của quảng cáo mới được tạo. ⏎ Nếu quá trình sao chép quảng cáo thất bại, trường này vẫn được trả về để cho biết quảng cáo chưa được sao chép thành công. |
| ↳↳↳↳ ad_error_list | string[] | Các lỗi phát sinh trong quá trình sao chép quảng cáo. ⏎ Nếu không có lỗi, giá trị trường này là danh sách trống (`[]`). |

### Ví dụ lệnh cURL (Example)
```http
// curl
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "task_info": {
            "success_ad_count": 1,
            "total_ad_count": 1
        },
        "task_result": {
            "adgroup_result_list": [
                {
                    "ad_result_list": [
                        {
                            "ad_error_list": [],
                            "ad_name": "{{ad_name}}",
                            "is_success": true,
                            "smart_plus_ad_id": "{{smart_plus_ad_id}}"
                        }
                    ],
                    "ad_status": "ALL_SUCCESS",
                    "adgroup_error_list": [],
                    "adgroup_id": "{{adgroup_id}}",
                    "adgroup_name": "{{adgroup_name}}",
                    "success_ad_count": 1,
                    "total_ad_count": 1
                }
            ],
            "campaign_error_infos": [],
            "campaign_id": "{{campaign_id}}",
            "campaign_name": "{{campaign_name}}"
        },
        "task_status": "SUCCESS"
    }
}
```

---

<a id="doc-1843310524500993"></a>
<!-- doc_id: 1843310524500993 -->
<!-- doc_id: 1843310524500993 -->
# Nhóm quảng cáo (Ad groups)
> Đường dẫn: API Reference > Smart+ nâng cấp > Ad groups
Nhóm quảng cáo là cấp độ trung gian trong cấu trúc phân cấp quảng cáo. Bạn có thể thiết lập các vị trí hiển thị quảng cáo cụ thể, đối tượng nhắm mục tiêu, ngân sách, lịch chạy, giá thầu và mục tiêu tối ưu hóa cho từng nhóm quảng cáo ở cấp nhóm quảng cáo.

Nhóm này bao gồm các endpoint sau:

* [Lấy danh sách nhóm quảng cáo Smart+ nâng cấp](62-upgraded-smartplus-p2.md#doc-1843314879617026)
* [Tạo nhóm quảng cáo Smart+ nâng cấp](62-upgraded-smartplus-p3.md#doc-1843314887930946)
* [Cập nhật nhóm quảng cáo Smart+ nâng cấp](62-upgraded-smartplus-p4.md#doc-1843314894279682)
* [Cập nhật trạng thái hoạt động của nhóm quảng cáo Smart+ nâng cấp](62-upgraded-smartplus-p4.md#doc-1843314908153858)
* [Cập nhật ngân sách của nhóm quảng cáo Smart+ nâng cấp](62-upgraded-smartplus-p4.md#doc-1843314914438466)
---

## Hướng dẫn thực hành Data Retrieval (Python & cURL)

Dưới đây là mã nguồn mẫu minh họa quy trình gọi API thực tế cho phân hệ **Smart+ nâng cấp (Upgraded Smart+) — phần 1/7**:

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

