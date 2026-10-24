# Tổng quan GMV Max (GMV Max) — phần 1/3

> Phân hệ: apiref:GMV Max.
> Tài liệu biên dịch kỹ thuật chi tiết theo chuẩn TikTok Business API v1.3.

---

## Mục lục điều hướng
- [1. Tổng quan GMV Max (#doc-1822000911166465)](#doc-1822000911166465)
- [2. Lấy danh sách chiến dịch GMV Max (#doc-1826463372290177)](#doc-1826463372290177)
- [3. Lấy thông tin chi tiết chiến dịch GMV Max (#doc-1822000968821762)](#doc-1822000968821762)
- [4. Tạo chiến dịch GMV Max (#doc-1822000988713089)](#doc-1822000988713089)
- [5. Cập nhật chiến dịch GMV Max (#doc-1822001009002497)](#doc-1822001009002497)
- [6. Lấy mục tiêu ROI và ngân sách đề xuất cho GMV Max (#doc-1822001024720897)](#doc-1822001024720897)
- [7. Tạo phiên tăng tốc phân phối tối đa hoặc tăng tốc mẫu sáng tạo (#doc-1835246967275522)](#doc-1835246967275522)
- [8. Cập nhật phiên tăng tốc phân phối tối đa hoặc tăng tốc mẫu sáng tạo (#doc-1835247009119233)](#doc-1835247009119233)
- [9. Lấy danh sách các phiên tăng tốc trong một chiến dịch (#doc-1835246996436162)](#doc-1835246996436162)
- [10. Lấy thông tin chi tiết các phiên tăng tốc (#doc-1835247031331842)](#doc-1835247031331842)
- [11. Xóa một phiên tăng tốc (#doc-1835246983475217)](#doc-1835246983475217)

---

<a id="doc-1822000911166465"></a>
<!-- doc_id: 1822000911166465 -->
<!-- doc_id: 1822000911166465 -->
# Tổng quan GMV Max (GMV Max)
> Đường dẫn: API Reference > GMV Max
GMV Max là một loại chiến dịch quảng cáo tự động giúp tối ưu hóa tổng ROI trên toàn kênh cho TikTok Shop của bạn. 

Để tìm hiểu cách tạo các chiến dịch này, xem [Tạo chiến dịch GMV Max](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1822009058467842).

Nhóm này gồm các endpoint sau:

**Campaign**
- [Lấy danh sách chiến dịch GMV Max](45-gmv-max-p1.md#doc-1826463372290177)
- [Lấy thông tin chi tiết chiến dịch GMV Max](45-gmv-max-p1.md#doc-1822000968821762)
- [Tạo chiến dịch GMV Max](45-gmv-max-p1.md#doc-1822000988713089)
- [Cập nhật chiến dịch GMV Max](45-gmv-max-p1.md#doc-1822001009002497)
- [Lấy mục tiêu ROI và ngân sách đề xuất cho GMV Max](45-gmv-max-p1.md#doc-1822001024720897)
- [Tạo phiên tăng tốc phân phối tối đa hoặc tăng tốc mẫu sáng tạo](45-gmv-max-p1.md#doc-1835246967275522)
- [Cập nhật phiên tăng tốc phân phối tối đa hoặc tăng tốc mẫu sáng tạo](45-gmv-max-p1.md#doc-1835247009119233)
- [Lấy danh sách các phiên tăng tốc trong một chiến dịch](45-gmv-max-p1.md#doc-1835246996436162)
- [Lấy thông tin chi tiết các phiên tăng tốc](45-gmv-max-p1.md#doc-1835247031331842)
- [Xóa một phiên tăng tốc](45-gmv-max-p1.md#doc-1835246983475217)
- [Xóa hoặc thêm lại mẫu sáng tạo trong chiến dịch GMV Max](45-gmv-max-p2.md#doc-1861260625563202)

**TikTok Shop and products**
- [Lấy danh sách TikTok Shop cho chiến dịch GMV Max](45-gmv-max-p2.md#doc-1822001044479041)
- [Lấy danh sách sản phẩm trong một TikTok Shop](69-tiktok-store.md#doc-1793482248880130)
- [Kiểm tra tính khả dụng của TikTok Shop cho chiến dịch GMV Max sản phẩm](45-gmv-max-p2.md#doc-1822001084174338)

**Identities and posts**
- [Lấy danh tính cho chiến dịch GMV Max](45-gmv-max-p2.md#doc-1822001101474882)
- [Kiểm tra mức độ chiếm dụng của danh tính hoặc sản phẩm trong Quảng cáo mua sắm](45-gmv-max-p2.md#doc-1822001136924674)
- [Lấy các bài đăng cho chiến dịch GMV Max sản phẩm](45-gmv-max-p2.md#doc-1822001168512129)
- [Lấy chi tiết video trong các bài đăng tùy chỉnh](45-gmv-max-p2.md#doc-1830215925061633)
- [Tạo bài đăng TikTok tùy chỉnh cấp cửa hàng](45-gmv-max-p2.md#doc-1866513154013585)
- [Lấy các bài đăng TikTok tùy chỉnh](45-gmv-max-p2.md#doc-1866513156712449)
- [Xóa các bài đăng TikTok tùy chỉnh](45-gmv-max-p2.md#doc-1866513159202306)
- [Lấy chi tiết liên kết sản phẩm của video trong các bài đăng tùy chỉnh](45-gmv-max-p2.md#doc-1866513161692161)

**Ad account exclusive authorization**
- [Get the TikTok Shop exclusive authorization status of an ad account](45-gmv-max-p2.md#doc-1822001184635905)
- [Grant an ad account exclusive authorization for a TikTok Shop](45-gmv-max-p2.md#doc-1822001200356354)

**Reporting**
- [Run a GMV Max Campaign report](45-gmv-max-p2.md#doc-1824721673497601)
	- [Metrics in GMV Max Campaign reports](45-gmv-max-p3.md#doc-1824722485971009)

---

<a id="doc-1826463372290177"></a>
<!-- doc_id: 1826463372290177 -->
<!-- doc_id: 1826463372290177 -->
# Lấy danh sách chiến dịch GMV Max (Get GMV Max Campaigns)
> Đường dẫn: API Reference > GMV Max > Get GMV Max Campaigns
Sử dụng endpoint này để truy xuất danh sách các chiến dịch GMV Max trong một tài khoản quảng cáo.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/gmv_max/campaign/get/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
|advertiser_id ***(Bắt buộc)***|string|ID tài khoản quảng cáo TikTok.|
|fields|string[]|Fields that you want to get.<br><br>If this field is not specified, all fields are returned by default.<br><br>For allowed fields, see the fields under `list` in the response.|
|filtering ***(Bắt buộc)***|object|Filters on the data.<br><br>Example: `filtering=&#123;"gmv_max_promotion_types":["PRODUCT_GMV_MAX"]&#125;`.|
#|gmv_max_promotion_types {Required}|string[]|GMV Max Campaign type.<br><br>Các giá trị enum hỗ trợ: <ul><li>`PRODUCT_GMV_MAX`: [Product GMV Max Campaign](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1822009220448257).</li><li>`LIVE_GMV_MAX`: [Live GMV Max Campaign](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1822009242546258).</li></ul>|
#|store_ids|string[]|A list of TikTok Shop IDs.<br><br>Kích thước tối đa: 10.<br><br>To obtain a TikTok Shop that is available for GMV Max Campaigns, use [/gmv_max/store/list/](45-gmv-max-p2.md#doc-1822001044479041) and confirm that the returned `is_gmv_max_available` is `true`.|
#|campaign_ids|string[]|A list of campaign IDs.<br><br>Kích thước tối đa: 100.|
#|campaign_name|string|Campaign name.|
#|primary_status|string|Primary status.<br><br>Các giá trị enum hỗ trợ: <ul><li>`STATUS_DELIVERY_OK`: Active.</li><li>`STATUS_DISABLE`: Inactive.</li><li>`STATUS_DELETE`: Deleted.</li></ul>|
#|creation_filter_start_time|string|The earliest campaign Thời gian tạo, in the format of `YYYY-MM-DD HH:MM:SS` (UTC time). This filter will retrieve campaigns created after this time.<br><br>Example: `2025-01-01 00:00:01`.<br><br>If `creation_filter_start_time` and `creation_filter_end_time` are not specified, the results will include GMV Max Campaigns created at any time.<br><br><p><span style="color:darkred"><b>Note</b></span>: To ensure task efficiency and speed, consider setting a time range within 6 months for the Thời gian tạo filters.|
#|creation_filter_end_time|string|The latest campaign Thời gian tạo, in the format of `YYYY-MM-DD HH:MM:SS` (UTC time). This filter will retrieve campaigns created before this time.<br><br>Example: `2025-02-01 00:00:01`.<br><br>If `creation_filter_start_time` and `creation_filter_end_time` are not specified, the results will include GMV Max Campaigns created at any time.<br><br><p><span style="color:darkred"><b>Note</b></span>: To ensure task efficiency and speed, consider setting a time range within 6 months for the Thời gian tạo filters.|
|page|integer|Current Số trang cần lấy dữ liệu.<br><br>Value range: ≥ 1.<br>Giá trị mặc định: 1.|
|page_size|integer|Page size.<br><br>Value range: 1-100.<br>Giá trị mặc định: 10.|

### Ví dụ lệnh cURL (Example)
#### Lấy danh sách chiến dịch GMV Max sản phẩm (Retrieve Product GMV Max Campaigns)
```http
// curl
curl --location  --request GET 'https://business-api.tiktok.com/open_api/v1.3/gmv_max/campaign/get/?advertiser_id={{advertiser_id}}&filtering={"gmv_max_promotion_types": ["PRODUCT_GMV_MAX"]}' \
--header 'Access-Token: {{Access-Token}}'
```

#### Lấy danh sách chiến dịch GMV Max LIVE (Retrieve LIVE GMV Max Campaigns)
```http
// curl
curl --location  --request GET 'https://business-api.tiktok.com/open_api/v1.3/gmv_max/campaign/get/?advertiser_id={{advertiser_id}}&filtering={"gmv_max_promotion_types": ["LIVE_GMV_MAX"]}' \
--header 'Access-Token: {{Access-Token}}'
```
## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|code |number|Response code. For the complete list of response codes and descriptions, see [Appendix-Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message|string|Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|request_id |string|Mã log ID của một yêu cầu, dùng để định danh duy nhất yêu cầu đó.  |
|data |object|Returned data.|
#|list|object[]|A list of campaigns.<br><br>The returned fields are generated based on the `fields` specified in the request. All fields are returned by default.|
##|advertiser_id|string|ID tài khoản quảng cáo TikTok.|
##|campaign_id|string|ID chiến dịch quảng cáo.|
##|campaign_name|string|Campaign name.|
##|operation_status|string|The ON/OFF status of campaign.<br><br>Các giá trị enum hỗ trợ: <ul><li>`ENABLE`: in the ON status.</li><li>`DISABLE`: in the OFF status.</li></ul>|
##|create_time|string|The time when the campaign was created, in the format of `YYYY-MM-DD HH:MM:SS` (UTC time).<br><br>Example: `2025-01-01 00:00:01`.|
##|modify_time|string|The time when the campaign was last modified, in the format of `YYYY-MM-DD HH:MM:SS` (UTC time).<br><br>Example: `2025-01-01 00:00:01`.|
##|objective_type|string|Advertising objective.<br><br>Enum value: `PRODUCT_SALES` (Product Sales).|
##|secondary_status|string|Secondary status.<br><br>Để xem danh sách giá trị enum, xem [Supported campaign secondary statuses for GMV Max Campaigns](../09-marketing-api/quan-ly-chien-dich-tom-tat.md#doc-1757239620352002).|
##|roi_protection_compensation_status|string|The ROI protection compensation status of the campaign.<br>ROI protection is a feature that automatically issues ad credits when the return on investment (ROI) for your campaign falls below a certain threshold despite following GMV Max guidelines and best practices. To learn about the eligibility criteria for ROI protection and scenarios where the campaign is ineligible for ROI protection, see [About ROI protection for GMV Max campaigns](https://ads.tiktok.com/help/article/about-roi-protection-for-gmv-max-campaigns).<br><br>Các giá trị enum hỗ trợ: <ul><li>`IN_EFFECT`: ROI protection eligible. This campaign is eligible for an ad credit if your ads drive more than 20 conversions in 24 hours, but your ROI result is less than 90% of your target. To maintain campaign eligibility for ROI protection, don't edit your ROI, pause ad delivery, or enable max delivery. Campaign eligibility resets every 24 hours.</li><li>`NOT_ELIGIBLE`: ROI protection ineligible. This campaign isn't eligible for an ad credit if the target ROI isn't met because its ROI has been edited, the campaign has been paused, max delivery is enabled, or there are issues with your shop, ad accounts, livestreams, or products. Campaign eligibility resets every 24 hours.</li></ul>|
#|page_info|object|Pagination information.|
##|page|integer|Current Số trang cần lấy dữ liệu.|
##|page_size|integer|Paging size.|
##|total_number|integer|Tổng số kết quả tìm thấy.|
##|total_page|integer|Total pages of results.|

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "list": [
            {
                "campaign_name": "{{campaign_name}}",
                "advertiser_id": "{{advertiser_id}}",
                "objective_type": "PRODUCT_SALES",
                "modify_time": "{{modify_time}}",
                "secondary_status": "CAMPAIGN_STATUS_DISABLE",
                "campaign_id": "{{campaign_id}}",
                "create_time": "{{create_time}}",
                "operation_status": "DISABLE"
            },
            {
                "campaign_name": "{{campaign_name}}",
                "advertiser_id": "{{advertiser_id}}",
                "objective_type": "PRODUCT_SALES",
                "modify_time": "{{modify_time}}",
                "secondary_status": "CAMPAIGN_STATUS_DISABLE",
                "campaign_id": "{{campaign_id}}",
                "create_time": "{{create_time}}",
                "operation_status": "DISABLE"
            }
        ],
        "page_info": {
            "page": 1,
            "page_size": 10,
            "total_page": 1,
            "total_number": 2
        }
    }
}
```

---

<a id="doc-1822000968821762"></a>
<!-- doc_id: 1822000968821762 -->
<!-- doc_id: 1822000968821762 -->
# Lấy thông tin chi tiết chiến dịch GMV Max (Get the details of a GMV Max Campaign)
> Đường dẫn: API Reference > GMV Max > Get the details of a GMV Max Campaign
Sử dụng endpoint này để truy xuất thông tin chi tiết của một chiến dịch GMV Max.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/campaign/gmv_max/info/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). ⏎ Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**
| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
| advertiser_id ***(Bắt buộc)*** | string | ID tài khoản quảng cáo TikTok. |
| campaign_id ***(Bắt buộc)*** | string | ID của một chiến dịch GMV Max.<br><br><ul><li>To create a GMV Max Campaign and obtain the ID chiến dịch quảng cáo, use [/campaign/gmv_max/create/](45-gmv-max-p1.md#doc-1822000988713089).</li><li>To filter existing GMV Max Campaigns within your ad account, use [/gmv_max/campaign/get/](45-gmv-max-p1.md#doc-1826463372290177).</li></ul> |

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/campaign/gmv_max/info/?advertiser_id={{advertiser_id}}&campaign_id={{campaign_id}}' \
--header 'Access-Token: {{Access-Token}}'
```
## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|code |number|Response code. For the complete list of response codes and descriptions, see [Appendix-Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message|string|Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|request_id |string|Mã log ID của một yêu cầu, dùng để định danh duy nhất yêu cầu đó.  |
|data |object|Returned data.|
#| advertiser_id | string | ID tài khoản quảng cáo TikTok. |
#| operation_status| string | The status of the GMV Max Campaign.<br><br>Các giá trị enum hỗ trợ: <ul><li>`DISABLE`: Disabled.</li><li>`ENABLE`: Enabled. </li></ul> |
#| campaign_id | string | The ID of the GMV Max Campaign. |
#| campaign_name | string | The name of the GMV Max Campaign. |
#| store_id | string | ID của TikTok Shop. |
#| store_authorized_bc_id | string | ID của Business Center được ủy quyền truy cập vào TikTok Shop (`store_id`). |
#| shopping_ads_type | string | Loại chiến dịch GMV Max.<br><br>Các giá trị enum hỗ trợ: <ul><li>`PRODUCT`: Product GMV Max Campaign.</li><li>`LIVE`: Live GMV Max Campaign. </li></ul> |
#| product_specific_type | string | Các chiều khác nhau để lựa chọn sản phẩm. <br><br>Các giá trị enum hỗ trợ: <ul><li>`ALL`: Allow TikTok to dynamically choose from all products within the TikTok Shop.</li><li>`CUSTOMIZED_PRODUCTS`: Specify a customized number of products within the TikTok Shop.</li><li>`UNSET`: Unset.</li></ul> |
#| item_group_ids | string[] | Returned only when `shopping_ads_type` is `PRODUCT` and `product_specific_type` is `CUSTOMIZED_PRODUCTS`. <br><br>Product SPU (standard product unit) IDs. |
#| optimization_goal | string | Optimization goal. <br><br>Enum value:<ul><li>`VALUE`: Gross revenue.</li></ul>|
#| roi_protection_enabled | boolean | Liệu campaign is eligible for ROI protection. <br>ROI protection is a feature that automatically issues ad credits when the return on investment (ROI) for your campaign falls below a certain threshold despite following GMV Max guidelines and best practices. To learn about the eligibility criteria for ROI protection and scenarios where the campaign is ineligible for ROI protection, see [About ROI protection for GMV Max campaigns](https://ads.tiktok.com/help/article/about-roi-protection-for-gmv-max-campaigns).<br><br>Các giá trị được hỗ trợ: `true`, `false`.|
#| deep_bid_type | string | Bid strategy. <br><br>Enum value:<ul><li>`VO_MIN_ROAS`: Minimum ROAS. Bid with an ROI target.</li></ul>|
#| roas_bid | number | Returned only when `deep_bid_type` is `VO_MIN_ROAS`.<br><br>ROI target. |
#| budget | number | Ngân sách hàng ngày. |
#| promotion_days | object | Chi tiết thiết lập các ngày diễn ra chương trình khuyến mại. |
##| is_enabled | boolean | Có thực hiện enable promotion days to automatically optimize your campaign for higher GMV during high-intent shopping dates in regions where your ads are delivering. <br><br>Các giá trị được hỗ trợ: `true`, `false`. |
##| auto_schedule_enabled | boolean | Có thực hiện use TikTok Shop promotion days schedule.<br><br>Các giá trị được hỗ trợ: `true`, `false`. |
##| custom_schedule_list | object[] | Details of the custom promotion day schedules. |
###| start_time | string | The start time of the custom promotion day schedule, in the format of `YYYY-MM-DD` (ad account time zone). |
###| end_time | string | The end time of the custom promotion day schedule, in the format of `YYYY-MM-DD`  (ad account time zone). |
##| roas_bid_multiplier |number | The target ROI index.<br>Changes to your target ROI will be in effect during promotion days and may drive higher GMV for this campaign.<br><br>Các giá trị enum hỗ trợ: <ul><li>`90`: -10%. To decrease your target ROI by 10% during promotion days.</li><li>`80`: -20%. To decrease your target ROI by 20% during promotion days.</li><li>`70`: -30%. To decrease your target ROI by 30% during promotion days.</li></ul> |
##| adjusted_roas_bid | number | Promotion days target ROI. |
##|budget_increase_percentage|integer|The increase percentage for the budget during promotion days.<br><br>A value of 50 means a 50% budget increase when the automatic budget increase is triggered.|
##|increase_limit|integer|The increase limit for the daily budget during promotion days.<br><br>A value of 10 means allows up to 10 budget increases per day when the automatic budget increases are triggered.|
##| current_budget | number | The specified campaign daily budget (`budget`).|
##| next_increase | number | The increase in budget compared with your specified campaign daily budget (`budget`).<br><br>Formula: `next_increase` = `current_budget` x `budget_increase_percentage`.<br><br>For example, if `budget` is 300 USD and `budget_increase_percentage` is 50, `next_increase` will be 150 USD, indicating a daily budget increase of 150 USD.|
##|remained_times|number|The remaining times of automatic budget increases.|
##|maximum_budget|number|The maximum possible budget.<br><br>Formula: `maximum_budget` = `current_budget` + `current_budget` x `budget_increase_percentage` x `remained_times`.<br><br>For example, if `current_budget` is 200 USD, `budget_increase_percentage` is 50, and `remained_times` is 10,  your `maximum_budget` will be 1200 USD, as the increase can occur up to 10 times daily.|
##| estimated_gross_revenue_increase | string | The estimated percentage increase in gross revenue due to the ROI change during promotion days. <br><br>Example: `24%`. |
#|auto_budget|object|Chi tiết thiết lập ngân sách tự động trong những ngày không khuyến mại.|
##|auto_budget_enabled|boolean|Có thực hiện enable automatic budget increase during non-promotion days.<br><br>Enabling automatic budget increase will allow your daily budget to be automatically increased to optimize your campaign for more sales on days when your campaign has reached at least 90% of your ROI target and at least 80% of your budget has been used. Your daily budget will reset to its original amount each day.<br><br>Các giá trị được hỗ trợ: `true`, `false`.|
##|budget_increase_percentage|integer|The increase percentage for the budget during non-promotion days.<br><br>A value of 50 means a 50% budget increase when the automatic budget increase is triggered.|
##|increase_limit|integer|The increase limit for the daily budget during non-promotion days.<br><br>A value of 10 means allows up to 10 budget increases per day when the automatic budget increases are triggered.|
##|current_budget|number|The specified campaign daily budget (`budget`).|
##|next_increase|number|The increase in budget compared with your specified campaign daily budget (`budget`).<br><br>Formula: `next_increase` = `current_budget` x `budget_increase_percentage`.<br><br>For example, if `budget` is 300 USD and `budget_increase_percentage` is 50, `next_increase` will be 150 USD, indicating a daily budget increase of 150 USD.|
##|remained_times|number|The remaining times of automatic budget increases.|
##|maximum_budget|number|The maximum possible budget.<br><br>Formula: `maximum_budget` = `current_budget` + `current_budget` x `budget_increase_percentage` x `remained_times`.<br><br>For example, if `current_budget` is 200 USD, `budget_increase_percentage` is 50, and `remained_times` is 10,  your `maximum_budget` will be 1200 USD, as the increase can occur up to 10 times daily.|
#| auto_budget_enabled  {-to be deprecated}| boolean | Có thực hiện enable automatic budget increase.<br>When your achieved ROI reaches at least 90% of the target and 80% or more of your budget has been used, your daily campaign budget may automatically increase by up to 10 times to capture more sales. Your budget will reset to its original amount each day.<br><br><ul><li>When `is_enabled` within the object `promotion_days` is `true` and`auto_budget_enabled` is `false`, your ROI target will decrease and your daily budget will automatically increase during TikTok Shop promotion days (when `auto_schedule_enabled` is `true`) and custom promotion days as defined by `custom_schedule_list`. Your daily budget will reset to its original amount every day. During standard days, your ROI target and budget won't change.</li><li>When `is_enabled` within the object `promotion_days` is `true` and`auto_budget_enabled` is `true`, auto budget increase will be turned on during TikTok Shop promotion days (when `auto_schedule_enabled` is `true`), custom promotion days as defined by `custom_schedule_list`,**&nbsp;and standard days**. Your daily budget will reset to its original amount every day. During TikTok Shop promotion days and custom promotion days as defined by `custom_schedule_list`, your ROI target will decrease. During standard days, your ROI target won't change.</li><li>When `is_enabled` within the object `promotion_days` is `false` and`auto_budget_enabled` is `true`, your ROI won't change, your daily campaign budget may automatically increase up to 10 times to optimize gross revenue. Your daily budget will reset to its original amount every day.</li></ul><br>Các giá trị được hỗ trợ: `true`, `false`.|
#| schedule_type | string | Schedule type.<br><br>Các giá trị enum hỗ trợ: <ul><li>`SCHEDULE_FROM_NOW`: To run the campaign continuously after the scheduled start time.</li><li>`SCHEDULE_START_END`: To run the campaign between the scheduled start time and end time.</li></ul> |
#| schedule_start_time | string | Campaign delivery start time, in the format of `YYYY-MM-DD HH:MM:SS` (UTC+0). |
#| schedule_end_time | string | Campaign delivery end time, in the format of `YYYY-MM-DD HH:MM:SS` (UTC+0). |
#| placements | string[] | Placements.<br>The apps where you want to deliver your campaign. <br><br> Các giá trị enum hỗ trợ: <ul><li>`PLACEMENT_TIKTOK`: TikTok.</li><li>`PLACEMENT_PANGLE`: Pangle.</li></ul><br><p><span style="color:darkred"><b>Note</b></span>:  <ul><li>Product GMV Max Campaigns automatically explore and choose from the most extensive audience scope across TikTok and Pangle. Learn more [about Pangle](https://ads.tiktok.com/help/article/pangle-placement).</li><li>If you want to opt out of the Pangle placement for your Product GMV Max Campaigns, contact your TikTok representative.</li></ul>|
#| location_ids | string[] | The IDs of the targeted locations. <br><br> To learn about the corresponding location for a location ID, see **Location IDs**. |
#| age_groups | string[] | The targeted age groups.<br><br> Để xem danh sách giá trị enum, xem [Enumeration - Age Group](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
#| product_video_specific_type | string | The video selection mode. <br><br>Các giá trị enum hỗ trợ: <ul><li>`AUTO_SELECTION`: To autoselect videos.</li><li>`CUSTOM_SELECTION`: To manually select videos. </li><li>`UNSET`: Unset. </li></ul>|
#|accelerate_testing_for_new_videos|string|Có thực hiện accelerate testing for new videos, that is, prioritize performance testing for your new, recently authorized, and updated videos as part of your campaign.<br>Videos that have been uploaded or authorized in the past 7 days, including recently authorized TikTok account videos, customized posts, and videos with new or updated product links, will be prioritized for testing. This may temporarily reduce gross revenue, but your campaign's overall ROI will stay within your target ROI range. Your campaign will still be eligible for ROI protection when you turn on accelerated learning.<br><br>Các giá trị enum hỗ trợ: <ul><li>`ON`: To accelerate testing for new videos.</li><li>`OFF`: To not accelerate testing for new videos.</li></ul>|
#| identity_list | object[] | The list of identities (TikTok accounts) associated with the GMV Max Campaign. |
##| identity_id | string | Identity ID. |
##| identity_type | string | Identity type. <br><br>Các giá trị enum hỗ trợ: <ul><li>`AUTH_CODE`: Authorized User. This type of identity is created when you use the authorization code to access a TikTok account or a TikTok post.</li><li>`TT_USER`: TikTok User. This type of identity is created when you bind your TikTok For Business account with your TikTok Business Account, or when you bind your TikTok For Business account with your regular TikTok account and then upgrade the account to Business Account.</li><li>`BC_AUTH_TT`: TikTok Account User in Business Center. This type of identity is created when you add a TikTok account to your Business Center, and the TikTok account owner approves your request. </li><li>`TTS_TT`: TikTok Account User for TikTok Shop. This type of identity is created when you set an official TikTok account for the TikTok Shop.</li></ul> |
##| identity_authorized_bc_id | string | Returned only when `identity_type` is `BC_AUTH_TT`. <br><br>The ID of the Business Center that a TikTok Account User in Business Center identity is associated with. |
##| identity_authorized_shop_id | string | Returned for some `BC_AUTH_TT` identities. <br><br>The ID of the TikTok Shop that the TikTok Account User in Business Center identity is associated with. |
##| store_id | string | Returned only when `identity_type` is `TTS_TT`. <br><br>The ID of the TikTok Shop that a TikTok Account User for TikTok Shop identity is associated with. |
#|affiliate_posts_enabled |boolean|Có thực hiện enable affiliate posts for your Product GMV Max Campaign.<br>Affiliate posts are TikTok posts created by affiliates (creators participating in the TikTok Shop Affiliate Program) and authorized for use in TikTok Shop Ads. Learn more [about affiliate creatives for TikTok Shop Ads](https://ads.tiktok.com/help/article/about-affiliate-creatives-for-tiktok-shop-ads).<br><br>Các giá trị được hỗ trợ: `true`, `false`.|
#| item_list| object[] | The list of authorized TikTok posts or customized TikTok posts associated with the GMV Max campaign. <br><br><ul><li>Authorized TikTok posts are existing posts featuring your selected products from your TikTok accounts or authorized using video codes. </li><li>Customized TikTok posts are newly created posts for the campaign, built by adding customized product links to your selected videos. These posts are exclusive to this Product GMV Max campaign.</li></ul>|
##| item_id | string | The ID of the TikTok post. |
##| text | string | The caption of the TikTok post. |
##| spu_id_list| string[] | The list of Product SPU IDs that the TikTok post is associated with. |
##| identity_info | object | Information about the identity associated with the TikTok post. |
###| identity_id | string | Identity ID. |
###| identity_type | string | Identity type. <br><br>Các giá trị enum hỗ trợ: <ul><li>`AUTH_CODE`: Authorized User. This type of identity is created when you use the authorization code to access a TikTok account or a TikTok post.</li><li>`TT_USER`: TikTok User. This type of identity is created when you bind your TikTok For Business account with your TikTok Business Account, or when you bind your TikTok For Business account with your regular TikTok account and then upgrade the account to Business Account.</li><li>`BC_AUTH_TT`: TikTok Account User in Business Center. This type of identity is created when you add a TikTok account to your Business Center, and the TikTok account owner approves your request. </li><li>`TTS_TT`: TikTok Account User for TikTok Shop. This type of identity is created when you set an official TikTok account for the TikTok Shop.</li></ul> |
###| identity_authorized_bc_id | string | Returned only when `identity_type` is `BC_AUTH_TT`. <br><br>The ID of the Business Center that a TikTok Account User in Business Center identity is associated with. |
###| identity_authorized_shop_id | string | Returned for some `BC_AUTH_TT` identities. <br><br>The ID of the TikTok Shop that the TikTok Account User in Business Center identity is associated with. |
###| store_id | string | Returned only when `identity_type` is `TTS_TT`. <br><br>The ID of the TikTok Shop that a TikTok Account User for TikTok Shop identity is associated with. |
###| profile_image | string | Temporary profile image URL for the TikTok account that is associated with the identity. <br><br>Validity period: around 48 hours. The expiration time is included in the URL after the `x-expires` parameter, in the format of an Epoch/Unix timestamp in seconds.<br><br>Once the URL expires, you need to call [/campaign/gmv_max/info/](45-gmv-max-p1.md#doc-1822000968821762) to obtain a new URL. |
###| user_name| string | The username of the TikTok account that is associated with the identity. |
##| video_info | object | Details of the video in the post. |
###| video_id | string | The ID of the video. |
###| video_cover_url | string | Temporary URL for the video cover.<br><br>Validity period: around 24 hours. The expiration time is included in the URL after the `x-expires` parameter, in the format of an Epoch/Unix timestamp in seconds. <br><br>Once the URL expires, you need to call [/campaign/gmv_max/info/](45-gmv-max-p1.md#doc-1822000968821762) to obtain a new URL. |
###| preview_url | string | Temporary preview URL for the video. <br><br>Validity period: six hours.<br><br>Once the URL expires, you need to call [/campaign/gmv_max/info/](45-gmv-max-p1.md#doc-1822000968821762) to obtain a new URL. |
###| height | number | The height of the video in pixels. <br><br> Example: 1920. |
###| width | number | The width of the video in pixels.<br><br>Example: 1080. |
###| bit_rate | number | The bit rate of the video in bps. <br><br>Example: 8500323. |
###| duration | number | The duration of the video in seconds. <br><br>Example: 3.669. |
###| size | number | The size of the video in bytes. <br><br>Example: 3898461. |
###| signature | string | The MD5 of the video. <br><br>Example: `ab1cd2345e678fghi91jkl23b456m7no`. |
###| format | string | The format of the video.<br><br>Example: `mp4`. |
###| definition | string | The definition of the video.<br><br> Example: `1080p`. |
###| fps | number | The frames per second (FPS) of the video. <br><br>Example: 27. |
#|campaign_custom_anchor_video_id{-To-be-deprecated}|string|The ID of the collection of customized posts created in the Product GMV Max Campaign.<br><br>You can pass this field to [/gmv_max/custom_anchor_video_list/get/](45-gmv-max-p2.md#doc-1830215925061633) to obtain the details of the customized posts within the collection.<br><br><p><span style="color:darkred"><b>Important</b></span>: This field will be deprecated in the next API version. To ensure a seamless integration, retrieve the details of videos used in customized posts using [/gmv_max/creation/custom_anchor_video_list/get/](45-gmv-max-p2.md#doc-1866513156712449) and [/gmv_max/creation/shop_video/video_anchors/](45-gmv-max-p2.md#doc-1866513161692161).|
#| custom_anchor_video_list {-To-be-deprecated}| object[] | The list of customized TikTok posts associated with the GMV Max campaign. <br>Customized TikTok posts are posts with custom product links. <br><br><p><span style="color:darkred"><b>Important</b></span>: This field will be deprecated in the next API version. To ensure a seamless integration, retrieve the details of videos used in customized posts using [/gmv_max/creation/custom_anchor_video_list/get/](45-gmv-max-p2.md#doc-1866513156712449) and [/gmv_max/creation/shop_video/video_anchors/](45-gmv-max-p2.md#doc-1866513161692161).|
##| item_id | string | The ID of the TikTok post. |
##| spu_id_list| string[] | The list of Product SPU IDs that the TikTok post is associated with. |
##| identity_info | object | Information about the identity associated with the TikTok post. |
###| identity_id | string | Identity ID. |
###| identity_type | string | Identity type. <br><br>Các giá trị enum hỗ trợ: <ul><li>`AUTH_CODE`: Authorized User. This type of identity is created when you use the authorization code to access a TikTok account or a TikTok post.</li><li>`TT_USER`: TikTok User. This type of identity is created when you bind your TikTok For Business account with your TikTok Business Account, or when you bind your TikTok For Business account with your regular TikTok account and then upgrade the account to Business Account.</li><li>`BC_AUTH_TT`: TikTok Account User in Business Center. This type of identity is created when you add a TikTok account to your Business Center, and the TikTok account owner approves your request. </li><li>`TTS_TT`: TikTok Account User for TikTok Shop. This type of identity is created when you set an official TikTok account for the TikTok Shop.</li></ul> |
###| identity_authorized_bc_id | string | Returned only when `identity_type` is `BC_AUTH_TT`. <br><br>The ID of the Business Center that a TikTok Account User in Business Center identity is associated with. |
###| identity_authorized_shop_id | string | Returned for some `BC_AUTH_TT` identities. <br><br>The ID of the TikTok Shop that the TikTok Account User in Business Center identity is associated with. |
###| store_id | string | Returned only when `identity_type` is `TTS_TT`. <br><br>The ID of the TikTok Shop that a TikTok Account User for TikTok Shop identity is associated with. |

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "advertiser_id": "{{advertiser_id}}",
        "age_groups": [
            "AGE_18_24",
            "AGE_25_34",
            "AGE_35_44",
            "AGE_45_54",
            "AGE_55_100"
        ],
        "budget": 300,
        "campaign_id": "{{campaign_id}}",
        "campaign_name": "{{campaign_name}}",
        "custom_anchor_video_list": [],
        "deep_bid_type": "VO_MIN_ROAS",
        "identity_list": [
            {
                "identity_id": "{{identity_id}}",
                "identity_type": "TT_USER"
            },
            {
                "identity_authorized_bc_id": "{{identity_authorized_bc_id}}",
                "identity_id": "{{identity_id}}",
                "identity_type": "BC_AUTH_TT"
            },
            {
                "identity_authorized_bc_id": "{{identity_authorized_bc_id}}",
                "identity_id": "{{identity_id}}",
                "identity_type": "BC_AUTH_TT"
            },
            {
                "identity_authorized_bc_id": "{{identity_authorized_bc_id}}",
                "identity_id": "{{identity_id}}",
                "identity_type": "BC_AUTH_TT"
            },
            {
                "identity_authorized_bc_id": "{{identity_authorized_bc_id}}",
                "identity_id": "{{identity_id}}",
                "identity_type": "BC_AUTH_TT"
            },
            {
                "identity_authorized_bc_id": "{{identity_authorized_bc_id}}",
                "identity_id": "{{identity_id}}",
                "identity_type": "BC_AUTH_TT"
            },
            {
                "identity_authorized_bc_id": "{{identity_authorized_bc_id}}",
                "identity_id": "{{identity_id}}",
                "identity_type": "BC_AUTH_TT"
            },
            {
                "identity_authorized_bc_id": "{{identity_authorized_bc_id}}",
                "identity_id": "{{identity_id}}",
                "identity_type": "BC_AUTH_TT"
            },
            {
                "identity_authorized_bc_id": "{{identity_authorized_bc_id}}",
                "identity_id": "{{identity_id}}",
                "identity_type": "BC_AUTH_TT"
            },
            {
                "identity_authorized_bc_id": "{{identity_authorized_bc_id}}",
                "identity_id": "{{identity_id}}",
                "identity_type": "BC_AUTH_TT"
            },
            {
                "identity_authorized_bc_id": "{{identity_authorized_bc_id}}",
                "identity_id": "{{identity_id}}",
                "identity_type": "BC_AUTH_TT"
            },
            {
                "identity_authorized_bc_id": "{{identity_authorized_bc_id}}",
                "identity_id": "{{identity_id}}",
                "identity_type": "BC_AUTH_TT"
            },
            {
                "identity_authorized_bc_id": "{{identity_authorized_bc_id}}",
                "identity_id": "{{identity_id}}",
                "identity_type": "BC_AUTH_TT"
            },
            {
                "identity_authorized_bc_id": "{{identity_authorized_bc_id}}",
                "identity_id": "{{identity_id}}",
                "identity_type": "BC_AUTH_TT"
            }
        ],
        "item_group_ids": [
            "{{item_group_id}}",
            "{{item_group_id}}",
            "{{item_group_id}}",
            "{{item_group_id}}",
            "{{item_group_id}}",
            "{{item_group_id}}",
            "{{item_group_id}}",
            "{{item_group_id}}",
            "{{item_group_id}}",
            "{{item_group_id}}",
            "{{item_group_id}}",
            "{{item_group_id}}",
            "{{item_group_id}}",
            "{{item_group_id}}",
            "{{item_group_id}}",
            "{{item_group_id}}",
            "{{item_group_id}}",
            "{{item_group_id}}",
            "{{item_group_id}}",
            "{{item_group_id}}",
            "{{item_group_id}}",
            "{{item_group_id}}",
            "{{item_group_id}}"
        ],
        "item_list": [],
        "location_ids": [
            "1643084"
        ],
        "operation_status": "DISABLE",
        "optimization_goal": "VALUE",
        "placements": [
            "PLACEMENT_TIKTOK"
        ],
        "product_specific_type": "CUSTOMIZED_PRODUCTS",
        "product_video_specific_type": "AUTO_SELECTION",
		"affiliate_posts_enabled": true,
        "roas_bid": 2,
        "schedule_end_time": "{{schedule_end_time}}",
        "schedule_start_time": "{{schedule_start_time}}",
        "schedule_type": "SCHEDULE_START_END",
        "shopping_ads_type": "PRODUCT",
        "store_authorized_bc_id": "{{store_authorized_bc_id}}",
        "store_id": "{{store_id}}"
    }
}
```

---

<a id="doc-1822000988713089"></a>
<!-- doc_id: 1822000988713089 -->
<!-- doc_id: 1822000988713089 -->
# Tạo chiến dịch GMV Max (Create a GMV Max Campaign)
> Đường dẫn: API Reference > GMV Max > Create a GMV Max Campaign
Sử dụng endpoint này để tạo một chiến dịch GMV Max.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/campaign/gmv_max/create/

**Method** POST

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). ⏎ Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type  ****(Bắt buộc)**** | string | Định dạng dữ liệu yêu cầu. ⏎ Allowed format: `application/json`. |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
| request_id ***(Bắt buộc)*** | string | Mã Request ID hỗ trợ tính lũy thừa (idempotency) để tránh gửi cùng một yêu cầu hai lần. <br>If you retry requests with the same request ID multiple times within the 10-second cache time, then only one request will succeed. If a duplicate request with the expired request ID is received after the cache time, the server will treat it as a new request and process it accordingly. <br><br>The ID is different from the `request_id` returned in the response parameters, which is used to uniquely identify an HTTP request.<br><br> The value should be a string representation of a 64-bit integer. <br><br>Example: `"123456789"`. |
| store_id ***(Bắt buộc)*** | string | ID của TikTok Shop.<br><br> To obtain a TikTok Shop that is available for GMV Max Campaigns, use [/gmv_max/store/list/](45-gmv-max-p2.md#doc-1822001044479041) and confirm that the returned `is_gmv_max_available` is `true`. |
| store_authorized_bc_id ***(Bắt buộc)*** | string | ID của Business Center được ủy quyền truy cập vào TikTok Shop (`store_id`). |
| advertiser_id ***(Bắt buộc)*** | string | ID tài khoản quảng cáo TikTok. <br><br>To ensure that the ad account has exclusive GMV Max authorization for the TikTok Shop that you want to promote, call [/gmv_max/store/list/](45-gmv-max-p2.md#doc-1822001044479041) and confirm that the returned `advertiser_id` within `exclusive_authorized_advertiser_info` is the same as the ad account that you want to use to create GMV Max Campaigns.<ul><li>If the returned `advertiser_id` is not the same as the ad account that you want to use to create GMV Max Campaigns, use [/gmv_max/exclusive_authorization/create/](45-gmv-max-p2.md#doc-1822001200356354) to grant the ad account exclusive GMV Max authorization for the TikTok Shop.</li></ul>|
| shopping_ads_type ***(Bắt buộc)*** | string | Loại chiến dịch GMV Max.<br><br>Các giá trị enum hỗ trợ: <ul><li>`PRODUCT`: Product GMV Max Campaign.</li><li>`LIVE`: Live GMV Max Campaign. </li></ul> <br> Để tìm hiểu cách tạo các chiến dịch này, xem [Create Product GMV Max Campaigns](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1822009220448257) and [Create LIVE GMV Max Campaigns](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1822009242546258). |
| product_specific_type | string | Chỉ hợp lệ khi `shopping_ads_type` is `PRODUCT`.<br><br>Các chiều khác nhau để lựa chọn sản phẩm. <br><br>Các giá trị enum hỗ trợ: <ul><li>`ALL`: Allow TikTok to dynamically choose from all products within the TikTok Shop.</li><li>`CUSTOMIZED_PRODUCTS`: Specify a customized number of products within the TikTok Shop.</li></ul> <br>To confirm Liệu you can promote all products in the TikTok Shop, call [/gmv_max/store/shop_ad_usage_check/](45-gmv-max-p2.md#doc-1822001084174338) and check the returned `promote_all_products_allowed`. |
| item_group_ids **(Điều kiện)** | string[] | Bắt buộc khi `shopping_ads_type` is `PRODUCT` and `product_specific_type` is `CUSTOMIZED_PRODUCTS`. <br><br>Product SPU (standard product unit) IDs. <br><br> Kích thước tối đa: 50.<br><br>To obtain the list of SPU IDs for products within a TikTok Shop, use [/store/product/get/](69-tiktok-store.md#doc-1793482248880130). Set `ad_creation_eligible` to `GMV_MAX` and select `item_group_id` values where `status` is `AVAILABLE` and `gmv_max_ads_status` is `UNOCCUPIED`. |
| optimization_goal ***(Bắt buộc)*** | string | Optimization goal. <br><br>Enum value:<ul><li>`VALUE`: Gross revenue.</li></ul>|
| deep_bid_type ***(Bắt buộc)*** | string | Bid strategy. <br><br>Enum value:<ul><li>`VO_MIN_ROAS`: Minimum ROAS. Bid with an ROI target.</li></ul>|
| roas_bid **(Điều kiện)** | number | Required only when `deep_bid_type` is `VO_MIN_ROAS`.<br><br> ROI target, kept to up to one decimal place. <br><br>Examples: 3.2, 3.<br><br>To obtain the recommended ROI target, use [/gmv_max/bid/recommend/](45-gmv-max-p1.md#doc-1822001024720897) and check the returned `roas_bid`. |
| budget ***(Bắt buộc)*** | number | Ngân sách hàng ngày. <br><br> To obtain the recommended budget, use [/gmv_max/bid/recommend/](45-gmv-max-p1.md#doc-1822001024720897) and check the returned `budget`. |
| promotion_days | object | Chi tiết thiết lập các ngày diễn ra chương trình khuyến mại.<br><br><p><span style="color:darkred"><b>Note</b></span>: To customize the percentage and the maximum times the budget can increase per day within your promotion days settings, use `budget_increase_percentage` and `increase_limit`within this object.|
#| is_enabled | boolean | Có thực hiện enable promotion days to automatically optimize your campaign for higher GMV during high-intent shopping dates in regions where your ads are delivering. <br><br>Các giá trị được hỗ trợ: `true`, `false`.<br>Giá trị mặc định: `false`.<br><br>When `promotion_days` is specified, this field will be automatically set to `true`. |
#| auto_schedule_enabled | boolean | Chỉ hợp lệ khi `is_enabled` is `true`.<br><br>Có thực hiện use TikTok Shop promotion days schedule.<br><br>Các giá trị được hỗ trợ: `true`, `false`.<br><br>When`is_enabled` is `true`, this field will be automatically set to `true`. |
#| custom_schedule_list {+Conditional} | object[] | Details of the custom promotion day schedules.<br><br><ul><li>If `auto_schedule_enabled` is `false`, specify at least one set of `start_date` and `end_date` in `custom_schedule_list`.</li><li>If `auto_schedule_enabled` is `true`, `custom_schedule_list` is optional.</li></ul>Kích thước tối đa: 50. |
##| start_date | string | The start date of the custom promotion day schedule, in the format of `YYYY-MM-DD`(ad account time zone).<br><br><p><span style="color:darkred"><b>Note</b></span>: <ul><li>The start date cannot be after the `end_date`.</li><li>The start date cannot be earlier than the current date.</li><li>The start date must be on the same day as or after the `schedule_start_time` of the campaign.</li><li>The custom promotion days schedule will automatically start at 00:00:00 of the start date in the ad account time zone.</li></ul> |
##| end_date | string | The end date of the custom promotion day schedule, in the format of `YYYY-MM-DD` (ad account time zone) .<br><br><p><span style="color:darkred"><b>Note</b></span>: <ul><li>The end date cannot be earlier than the current time.</li><li>The custom promotion days schedule will automatically end at 00:00:00 of the end date in the ad account time zone.</li></ul> |
#| roas_bid_multiplier | number | The target ROI index.<br>Changes to your target ROI will be in effect during promotion days and may drive higher GMV for this campaign.<br><br>Các giá trị enum hỗ trợ: <ul><li>`90`: -10%. To decrease your target ROI by 10% during promotion days.</li><li>`80`: -20%. To decrease your target ROI by 20% during promotion days.</li><li>`70`: -30%. To decrease your target ROI by 30% during promotion days.</li></ul>Giá trị mặc định: `90`. <br><br><p><span style="color:darkred"><b>Note</b></span>: We will be updating the way ROI goals are calculated during promotions to improve performance accuracy and ensure fairness across campaigns. Instead of using just the value you manually specify, the system will calculate your promotional ROI goal based on <b>the lower of your recent campaign performance (last 7 non-promotion days) or your entered ROI</b>, and then apply the selected reduction (10%, 20%, or 30%). This will be an allowlist-only feature. You might not need to make code changes, but the returned value of ROI goal will be different. |
#|budget_increase_percentage|integer|The increase percentage for the budget during promotion days.<br><br>Value range: 50-300.<br>A value of 50 means a 50% budget increase when the automatic budget increase is triggered.<br>Giá trị mặc định: 50.|
#|increase_limit|integer|The increase limit for the daily budget during promotion days.<br><br>Value range: 1-10.<br>A value of 10 means allows up to 10 budget increases per day when the automatic budget increases are triggered.<br>Giá trị mặc định: 10.|
|auto_budget|object|Chi tiết thiết lập ngân sách tự động trong những ngày không khuyến mại.|
#|auto_budget_enabled|boolean|Có thực hiện enable automatic budget increase during non-promotion days.<br>Enabling automatic budget increase will allow your daily budget to be automatically increased to optimize your campaign for more sales on days when your campaign has reached at least 90% of your ROI target and at least 80% of your budget has been used. Your daily budget will reset to its original amount each day.<br><br>Các giá trị được hỗ trợ: `true`, `false`.<br>Giá trị mặc định: `false`.|
#|budget_increase_percentage|integer|The increase percentage for the budget during non-promotion days.<br><br>Value range: 50-300.<br>A value of 50 means a 50% budget increase when the automatic budget increase is triggered.<br>Giá trị mặc định: 50.|
#|increase_limit|integer|The increase limit for the budget during non-promotion days.<br><br>Value range: 1-10.<br>A value of 10 means allows up to 10 budget increases per day when the automatic budget increases are triggered.<br>Giá trị mặc định: 10.|
| auto_budget_enabled {-To be deprecated} | boolean | Có thực hiện enable automatic budget increase.<br>When your achieved ROI reaches at least 90% of the target and 80% or more of your budget has been used, your daily campaign budget may automatically increase by up to 10 times to capture more sales. Your budget will reset to its original amount each day.<br><br><ul><li>When `is_enabled` within the object `promotion_days` is `true` and`auto_budget_enabled` is `false`, your ROI target will decrease and your daily budget will automatically increase during TikTok Shop promotion days (when `auto_schedule_enabled` is `true`) and custom promotion days as defined by `custom_schedule_list`. Your daily budget will reset to its original amount every day. During standard days, your ROI target and budget won't change.</li><li>When `is_enabled` within the object `promotion_days` is `true` and`auto_budget_enabled` is `true`, auto budget increase will be turned on during TikTok Shop promotion days (when `auto_schedule_enabled` is `true`), custom promotion days as defined by `custom_schedule_list`, <b>and standard days</b>. Your daily budget will reset to its original amount every day. During TikTok Shop promotion days and custom promotion days as defined by `custom_schedule_list`, your ROI target will decrease. During standard days, your ROI target won't change.</li><li>When `is_enabled` within the object `promotion_days` is `false` and`auto_budget_enabled` is `true`, your ROI won't change, your daily campaign budget may automatically increase up to 10 times to optimize gross revenue. Your daily budget will reset to its original amount every day. <ul><li>However, if you specify `auto_budget_enabled` and `auto_budget` at the same time, `auto_budget_enabled` will be ignored.</li></ul></li></ul><br>Các giá trị được hỗ trợ: `true`, `false`.<br>Giá trị mặc định: `false`.<br><br><p><span style="color:darkred"><b>Note</b></span>: When you use this parameter, the automatic budget increase settings for GMV Max Campaigns are fixed in terms of percentage and maximum frequency. If you want to customize the percentage and the maximum times the budget can increase per day during non-promotion days, use `auto_budget` instead. |
| schedule_type ***(Bắt buộc)*** | string | Schedule type.<br><br>Các giá trị enum hỗ trợ: <ul><li>`SCHEDULE_FROM_NOW`: To run the campaign continuously after the scheduled start time.</li><li>`SCHEDULE_START_END`: To run the campaign between the scheduled start time and end time.</li></ul> |
| schedule_start_time ***(Bắt buộc)*** | string | Campaign delivery start time, in the format of `YYYY-MM-DD HH:MM:SS` (UTC+0). <br><br> The start time can be up to 12 hours earlier than the current time, but cannot be later than `2028-01-01 00:00:00`.|
| schedule_end_time **(Điều kiện)** | string | <ul><li>Bắt buộc khi `schedule_type` is `SCHEDULE_START_END`. </li><li>Not supported when `schedule_type` is `SCHEDULE_FROM_NOW`. </li></ul><br>Campaign delivery end time, in the format of `YYYY-MM-DD HH:MM:SS` (UTC+0).<br><br> The end time cannot be later than `2038-01-01 00:00:00`. |
| product_video_specific_type **(Điều kiện)** | string | Bắt buộc khi `shopping_ads_type` is `PRODUCT`. <br><br>The video selection mode. <br><br>Các giá trị enum hỗ trợ: <ul><li>`AUTO_SELECTION`: To autoselect videos. You need to specify `identity_list` simultaneously.</li><li>`CUSTOM_SELECTION`: To manually select videos. You need to specify `item_list` simultaneously.</li></ul>|
| identity_list **(Điều kiện)** | object[] | <ul><li>Bắt buộc khi `shopping_ads_type` is `LIVE`.</li><li>Optional when `shopping_ads_type` is `PRODUCT` and `product_video_specific_type` is `AUTO_SELECTION`.</li></ul><br>The list of identities (TikTok accounts) to associate with the GMV Max Campaign.<br><br><ul><li>When `shopping_ads_type` is `PRODUCT` and `product_video_specific_type` is `AUTO_SELECTION`, specify 0-20 identities as the source of video creatives via this field.<ul><li>To obtain a list of identities available for a Product GMV Max Campaign using the same TikTok Shop, use [/gmv_max/identity/get/](45-gmv-max-p2.md#doc-1822001101474882) and select identities with `product_gmv_max_available` as `true`.</li><li>When no identities are specified through `identity_list`, the product images will be used as ad creatives.</li></ul></li><li>When `shopping_ads_type` is `LIVE`, specify one identity as the LIVE source via this field. <ul><li>To obtain an identity that is available for LIVE GMV Max Campaigns, call [/gmv_max/identity/get/](45-gmv-max-p2.md#doc-1822001101474882) and select identities with `live_gmv_max_available` as `true`.</li></ul></li></ul>|
#| identity_id {+Conditional} | string | Bắt buộc khi `identity_list` is passed.<br><br>Identity ID. |
#| identity_type {+Conditional} | string | Bắt buộc khi `identity_list` is passed.<br><br> Identity type. <br><br>Các giá trị enum hỗ trợ: <ul><li>`AUTH_CODE`: Authorized User. This type of identity is created when you use the authorization code to access a TikTok account or a TikTok post.</li><li>`TT_USER`: TikTok User. This type of identity is created when you bind your TikTok For Business account with your TikTok Business Account, or when you bind your TikTok For Business account with your regular TikTok account and then upgrade the account to Business Account.</li><li>`BC_AUTH_TT`: TikTok Account User in Business Center. This type of identity is created when you add a TikTok account to your Business Center, and the TikTok account owner approves your request. </li><li>`TTS_TT`: TikTok Account User for TikTok Shop. This type of identity is created when you set an official TikTok account for the TikTok Shop.</li></ul> |
#| identity_authorized_bc_id {+Conditional} | string | Bắt buộc khi `identity_type` is `BC_AUTH_TT`. <br><br> The ID of the Business Center that a TikTok Account User in Business Center identity is associated with. |
#| identity_authorized_shop_id {+Conditional} | string | Required only when `dentity_type` is `BC_AUTH_TT` and `identity_authorized_shop_id` is returned for the identity from [/gmv_max/identity/get/](45-gmv-max-p2.md#doc-1822001101474882). <br><br> The ID of the TikTok Shop that a TikTok Account User in Business Center identity is associated with. |
#| store_id {+Conditional} | string | Bắt buộc khi `identity_type` is `TTS_TT`. <br><br>The ID of the TikTok Shop that a TikTok Account User for TikTok Shop identity is associated with. |
|affiliate_posts_enabled |boolean|This field is valid and defaults to `true` when the following conditions are both met:<ul><li>`shopping_ads_type` is `PRODUCT`</li><li>`product_video_specific_type` is `AUTO_SELECTION`</li></ul>Có thực hiện enable affiliate posts for your Product GMV Max Campaign.<br>Affiliate posts are TikTok posts created by affiliates (creators participating in the TikTok Shop Affiliate Program) and authorized for use in TikTok Shop Ads. Learn more [about affiliate creatives for TikTok Shop Ads](https://ads.tiktok.com/help/article/about-affiliate-creatives-for-tiktok-shop-ads).<br><br>Các giá trị được hỗ trợ: `true`, `false`.|
| item_list **(Điều kiện)** | object[] | Bắt buộc khi `shopping_ads_type` is `PRODUCT` and `product_video_specific_type` is `CUSTOM_SELECTION`. <br><br>The list of authorized TikTok posts or customized TikTok posts to associate with the Product GMV Max campaign.<ul><li>Authorized TikTok posts are existing posts featuring your selected products from your TikTok accounts or authorized using video codes.<ul><li>If you want to manually select authorized TikTok posts only for the Product GMV Max campaign, include their details using `item_list` and do not specify `custom_anchor_video_list`.</li></ul></li><li>Customized TikTok posts are created by adding customized product links to your videos. You can use two types of customized posts: campaign-level and shop-level.<ul><li><b>Campaign-level customized posts</b> are generated specifically for a campaign by adding customized product links to selected videos at the campaign level. These posts are exclusive to the Product GMV Max campaign in which they are created.<ul><li>To manually select campaign-level customized posts for a Product GMV Max campaign, provide the video details in the `item_list` parameter and specify the `custom_anchor_video_list` parameter simultaneously.</li></ul></li><li><b>Shop-level customized posts</b> are generated for a specific TikTok Shop by adding customized product links to selected videos at the shop level. These posts are automatically included in a Product GMV Max campaign if their linked products are part of that active campaign.<ul><li>To manually select shop-level customized TikTok posts for a Product GMV Max campaign, provide their details in the `item_list` parameter, but do not specify the `custom_anchor_video_list` parameter.</li><li>To retrieve shop-level customized TikTok posts, use [/gmv_max/creation/custom_anchor_video_list/get/](45-gmv-max-p2.md#doc-1866513156712449) and leave the `campaign_id` filter unspecified.</li></ul></li></ul></li></ul><br>Kích thước tối đa: 50.<br><br>To obtain a list of TikTok posts available for a Product GMV Max Campaign using the same TikTok Shop, use [/gmv_max/video/get/](45-gmv-max-p2.md#doc-1822001168512129).<br><br><p><span style="color:darkred"><b>Important</b></span>: The campaign-level customized posts feature will be deprecated in the upcoming API version. To ensure a seamless integration, create shop-level customized posts using [/gmv_max/creation/custom_anchor_video_list/create/](45-gmv-max-p2.md#doc-1866513154013585) and retrieve the details of videos used in customized posts using [/gmv_max/creation/custom_anchor_video_list/get/](45-gmv-max-p2.md#doc-1866513156712449) and [/gmv_max/creation/shop_video/video_anchors/](45-gmv-max-p2.md#doc-1866513161692161). |
#| item_id {+Conditional} | string | Bắt buộc khi `item_list` is passed.<br><br> The ID of the TikTok post. |
#| spu_id_list {+Conditional} | string[] | Bắt buộc khi `item_list` is passed. <br><br> Product SPU IDs associated or to associate with the TikTok post. |
#| identity_info {+Conditional} | object | Bắt buộc khi `item_list` is passed. <br><br>Information about the identity associated or to associate with the TikTok post. |
##| identity_id {+Conditional} | string | Bắt buộc khi `item_list` is passed.<br><br> Identity ID. |
##| identity_type {+Conditional} | string | Bắt buộc khi `item_list` is passed.<br><br>Identity type. <br><br>Các giá trị enum hỗ trợ: <ul><li>`AUTH_CODE`: Authorized User. This type of identity is created when you use the authorization code to access a TikTok account or a TikTok post.</li><li>`TT_USER`: TikTok User. This type of identity is created when you bind your TikTok For Business account with your TikTok Business Account, or when you bind your TikTok For Business account with your regular TikTok account and then upgrade the account to Business Account.</li><li>`BC_AUTH_TT`: TikTok Account User in Business Center. This type of identity is created when you add a TikTok account to your Business Center, and the TikTok account owner approves your request. </li><li>`TTS_TT`: TikTok Account User for TikTok Shop. This type of identity is created when you set an official TikTok account for the TikTok Shop.</li></ul> |
##| identity_authorized_bc_id {+Conditional} | string | Bắt buộc khi `identity_type` is `BC_AUTH_TT`. <br><br> The ID of the Business Center that a TikTok Account User in Business Center identity is associated with. |
##| identity_authorized_shop_id {+Conditional} | string | Required only when `dentity_type` is `BC_AUTH_TT` and `identity_authorized_shop_id` is returned for the identity from [/gmv_max/identity/get/](45-gmv-max-p2.md#doc-1822001101474882). <br><br> The ID of the TikTok Shop that a TikTok Account User in Business Center identity is associated with. |
##| store_id {+Conditional} | string | Bắt buộc khi `identity_type` is `TTS_TT`. <br><br>The ID of the TikTok Shop that a TikTok Account User for TikTok Shop identity is associated with. |
#| video_info {+Conditional} | object | Bắt buộc khi `item_list` is passed. <br><br>Details of the video in the post. |
##| video_id {+Conditional} | string | Bắt buộc khi `item_list` is passed. <br><br> The ID of the video. |
| custom_anchor_video_list{-To-be-deprecated} | object[] | The list of customized TikTok posts to associate with the Product GMV Max campaign.<br>Customized TikTok posts are posts created during campaign setup by adding customized product links for your products (`spu_id_list` within `custom_anchor_video_list`) to specified videos (`item_id` within `custom_anchor_video_list`). These posts will be exclusive to this Product GMV Max campaign.<ul><li>For manual selection: When `shopping_ads_type` is `PRODUCT` and `product_video_specific_type` is `CUSTOM_SELECTION`, specify the videos to be used in customized posts using this field.</li><li>For auto selection: When `shopping_ads_type` is `PRODUCT` and `product_video_specific_type` is `AUTO_SELECTION`, specify the videos to be auto-selected for customized posts using this field.</li></ul><br>Kích thước tối đa: 200.<br><br><p><span style="color:darkred"><b>Important</b></span>: This field will be deprecated along with the campaign-level customized posts feature in the next API version. To ensure a seamless integration, create shop-level customized posts using [/gmv_max/creation/custom_anchor_video_list/create/](45-gmv-max-p2.md#doc-1866513154013585) and retrieve the details of videos used in customized posts using [/gmv_max/creation/custom_anchor_video_list/get/](45-gmv-max-p2.md#doc-1866513156712449) and [/gmv_max/creation/shop_video/video_anchors/](45-gmv-max-p2.md#doc-1866513161692161).<br><br><p><span style="color:darkred"><b>Note</b></span>: Although you can add a maximum number of 200 customized posts during campaign creation, one Product GMV Max campaign can eventually include up to 2,000 customized posts. If you want to specify more than 200 customized posts for a Product GMV Max Campaign, you can update the `custom_anchor_video_list` of the campaign incrementally using [/campaign/gmv_max/update/](45-gmv-max-p1.md#doc-1822001009002497), with updates limited to 200 additional posts per request. |
#| item_id {+Conditional}| string | Bắt buộc khi `custom_anchor_video_list` is passed.<br><br>The ID of a TikTok video to be used in a customized post.<br><br>To retrieve eligible videos, use [/gmv_max/video/get/](45-gmv-max-p2.md#doc-1822001168512129) with `custom_posts_eligible` set to true. |
#| spu_id_list {+Conditional}| string[] | Bắt buộc khi `custom_anchor_video_list` is passed.<br><br>The SPU IDs of the products to associate with the customized product anchor link in the TikTok post.<br><br>Kích thước tối đa: 1. |
#| identity_info {+Conditional}| object | Bắt buộc khi `custom_anchor_video_list` is passed.<br><br>Information about the identity to associate with the post. |
##| identity_id {+Conditional}| string | Bắt buộc khi `custom_anchor_video_list` is passed.<br><br>Identity ID.<br><br>To obtain a list of identities available for GMV Max Campaigns, use [/gmv_max/identity/get/](45-gmv-max-p2.md#doc-1822001101474882). |
##| identity_type{+Conditional} | string | Bắt buộc khi `custom_anchor_video_list` is passed.<br><br>Identity type.<br><br>Các giá trị enum hỗ trợ: <ul><li>`AUTH_CODE`: Authorized User. This type of identity is created when you use the authorization code to access a TikTok account or a TikTok post.</li><li>`TT_USER`: TikTok User. This type of identity is created when you bind your TikTok For Business account with your TikTok Business Account, or when you bind your TikTok For Business account with your regular TikTok account and then upgrade the account to Business Account.</li><li>`BC_AUTH_TT`: TikTok Account User in Business Center. This type of identity is created when you add a TikTok account to your Business Center, and the TikTok account owner approves your request.</li><li>`TTS_TT`: TikTok Account User for TikTok Shop. This type of identity is created when you set an official TikTok account for the TikTok Shop.</li></ul> |
##| identity_authorized_bc_id {+Conditional}| string | Bắt buộc khi `identity_type` is `BC_AUTH_TT`.<br><br>The ID of the Business Center that a TikTok Account User in Business Center identity is associated with. |
##| identity_authorized_shop_id {+Conditional}| string | Required only when `identity_type` is `BC_AUTH_TT` and `identity_authorized_shop_id` is returned for the identity from [/gmv_max/identity/get/](45-gmv-max-p2.md#doc-1822001101474882).<br><br>The ID of the TikTok Shop that a TikTok Account User in Business Center identity is associated with. |
##| store_id {+Conditional}| string | Bắt buộc khi `identity_type` is `TTS_TT`.<br><br>The ID of the TikTok Shop that a TikTok Account User for TikTok Shop identity is associated with. |
| campaign_name ***(Bắt buộc)*** | string | The name of the GMV Max Campaign. |

### Ví dụ lệnh cURL (Example)

#### Tạo chiến dịch GMV Max sản phẩm (Create a Product GMV Max Campaign)
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/campaign/gmv_max/create/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "request_id": "{{request_id}}",
    "advertiser_id": "{{advertiser_id}}",
    "store_id": "{{store_id}}",
    "store_authorized_bc_id": "{{store_authorized_bc_id}}",
    "shopping_ads_type": "PRODUCT",
    "product_specific_type": "ALL",
    "optimization_goal": "VALUE",
    "deep_bid_type": "VO_MIN_ROAS",
    "roas_bid": {{roas_bid}},
    "budget": {{budget}},
    "schedule_type": "SCHEDULE_START_END",
    "schedule_start_time": "{{schedule_start_time}}",
    "schedule_end_time": "{{schedule_end_time}}",
    "product_video_specific_type": "AUTO_SELECTION",
        "identity_list": [
            {
                "identity_id": "{{identity_id}}",
                "identity_type": "TTS_TT",
                "store_id": "{{store_id}}"
            },
            {
                "identity_id": "{{identity_id}}",
                "identity_type": "TT_USER"
            },
            {
                "identity_authorized_bc_id": "{{identity_authorized_bc_id}}",
                "identity_id": "{{identity_id}}",
                "identity_type": "BC_AUTH_TT"
            }
        ],
    "campaign_name": "{{campaign_name}}"
}'
```

#### Tạo chiến dịch GMV Max LIVE (Create a LIVE GMV Max Campaign)
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/campaign/gmv_max/create/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "request_id": "{{request_id}}",
    "advertiser_id": "{{advertiser_id}}",
    "store_id": "{{store_id}}",
    "store_authorized_bc_id": "{{store_authorized_bc_id}}",
    "shopping_ads_type": "LIVE",
    "identity_list": [
        {
            "identity_id": "{{identity_id}}",
            "identity_type": "BC_AUTH_TT",
            "identity_authorized_bc_id": "{{identity_authorized_bc_id}}"
        }
    ],
    "optimization_goal": "VALUE",
    "deep_bid_type": "VO_MIN_ROAS",
    "roas_bid": {{roas_bid}},
    "budget": {{budget}},
    "schedule_type": "{{schedule_type}}",
    "schedule_start_time": "{{schedule_start_time}}",
    "schedule_end_time": "{{schedule_end_time}}",
    "campaign_name": "{{campaign_name}}"
}'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|code |number|Response code. For the complete list of response codes and descriptions, see [Appendix-Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message|string|Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|request_id |string|Mã log ID của một yêu cầu, dùng để định danh duy nhất yêu cầu đó.  |
|data |object|Returned data.|
#| advertiser_id | string | ID tài khoản quảng cáo TikTok. |
#| operation_status| string | The status of the GMV Max Campaign.<br><br>Các giá trị enum hỗ trợ: <ul><li>`DISABLE`: Disabled.</li><li>`ENABLE`: Enabled. </li></ul> |
#| campaign_id | string | The ID of the GMV Max Campaign. |
#| campaign_name | string | The name of the GMV Max Campaign. |
#| store_id | string | ID của TikTok Shop. |
#| store_authorized_bc_id | string | ID của Business Center được ủy quyền truy cập vào TikTok Shop (`store_id`). |
#| shopping_ads_type | string | Loại chiến dịch GMV Max.<br><br>Các giá trị enum hỗ trợ: <ul><li>`PRODUCT`: Product GMV Max Campaign.</li><li>`LIVE`: Live GMV Max Campaign. </li></ul> |
#| product_specific_type | string | Các chiều khác nhau để lựa chọn sản phẩm. <br><br>Các giá trị enum hỗ trợ: <ul><li>`ALL`: Allow TikTok to dynamically choose from all products within the TikTok Shop.</li><li>`CUSTOMIZED_PRODUCTS`: Specify a customized number of products within the TikTok Shop.</li><li>`UNSET`: Unset.</li></ul> |
#| item_group_ids | string[] | Returned only when `shopping_ads_type` is `PRODUCT` and `product_specific_type` is `CUSTOMIZED_PRODUCTS`. <br><br>Product SPU (standard product unit) IDs. |
#| optimization_goal | string | Optimization goal. <br><br>Enum value:<ul><li>`VALUE`: Gross revenue.</li></ul>|
#| roi_protection_enabled | boolean | Liệu campaign is eligible for ROI protection. <br>ROI protection is a feature that automatically issues ad credits when the return on investment (ROI) for your campaign falls below a certain threshold despite following GMV Max guidelines and best practices. To learn about the eligibility criteria for ROI protection and scenarios where the campaign is ineligible for ROI protection, see [About ROI protection for GMV Max campaigns](https://ads.tiktok.com/help/article/about-roi-protection-for-gmv-max-campaigns).<br><br>Các giá trị được hỗ trợ: `true`, `false`.|
#| deep_bid_type | string | Bid strategy. <br><br>Enum value:<ul><li>`VO_MIN_ROAS`: Minimum ROAS. Bid with an ROI target.</li></ul>|
#| roas_bid | number | Returned only when `deep_bid_type` is `VO_MIN_ROAS`.<br><br>ROI target. |
#| budget | number | Ngân sách hàng ngày. |
#| promotion_days | object | Chi tiết thiết lập các ngày diễn ra chương trình khuyến mại. |
##| is_enabled | boolean | Có thực hiện enable promotion days to automatically optimize your campaign for higher GMV during high-intent shopping dates in regions where your ads are delivering. <br>When promotion days are active for this campaign, your ad credits will be calculated for your promotion days target ROI setting.<br><br>Các giá trị được hỗ trợ: `true`, `false`. |
##| auto_schedule_enabled | boolean | Có thực hiện use TikTok Shop promotion days schedule.<br><br>Các giá trị được hỗ trợ: `true`, `false`. |
##| custom_schedule_list | object[] | Details of the custom promotion day schedules. |
###| start_date | string | The start date of the custom promotion day schedule, in the format of `YYYY-MM-DD` (ad account time zone). |
###| end_date | string | The end date of the custom promotion day schedule, in the format of `YYYY-MM-DD`  (ad account time zone). |
##| roas_bid_multiplier | number| The target ROI index.<br>Changes to your target ROI will be in effect during promotion days and may drive higher GMV for this campaign.<br><br>Các giá trị enum hỗ trợ: <ul><li>`90`: -10%. To decrease your target ROI by 10% during promotion days.</li><li>`80`: -20%. To decrease your target ROI by 20% during promotion days.</li><li>`70`: -30%. To decrease your target ROI by 30% during promotion days.</li></ul> |
##| adjusted_roas_bid | number | Promotion days target ROI. |
##|budget_increase_percentage|integer|The increase percentage for the budget during promotion days.<br><br>A value of 50 means a 50% budget increase when the automatic budget increase is triggered.|
##|increase_limit|integer|The increase limit for the daily budget during promotion days.<br><br>A value of 10 means allows up to 10 budget increases per day when the automatic budget increases are triggered.|
##| current_budget | number | The specified campaign daily budget (`budget`). |
##| next_increase | number | The increase in budget compared with your specified campaign daily budget (`budget`).<br><br>Formula: `next_increase` = `current_budget` x `budget_increase_percentage`.<br><br>For example, if `budget` is 300 USD and `budget_increase_percentage` is 50, `next_increase` will be 150 USD, indicating a daily budget increase of 150 USD.|
##|remained_times|number|The remaining times of automatic budget increases.|
##|maximum_budget|number|The maximum possible budget.<br><br>Formula: `maximum_budget` = `current_budget` + `current_budget` x `budget_increase_percentage` x `remained_times`.<br><br>For example, if `current_budget` is 200 USD, `budget_increase_percentage` is 50, and `remained_times` is 10,  your `maximum_budget` will be 1200 USD, as the increase can occur up to 10 times daily.|
##| estimated_gross_revenue_increase | string | The estimated percentage increase in gross revenue due to the ROI change during promotion days. <br><br>Example: `24%`. |
#|auto_budget|object|Chi tiết thiết lập ngân sách tự động trong những ngày không khuyến mại.|
##|auto_budget_enabled|boolean|Có thực hiện enable automatic budget increase during non-promotion days.<br><br>Enabling automatic budget increase will allow your daily budget to be automatically increased to optimize your campaign for more sales on days when your campaign has reached at least 90% of your ROI target and at least 80% of your budget has been used. Your daily budget will reset to its original amount each day.<br><br>Các giá trị được hỗ trợ: `true`, `false`.|
##|budget_increase_percentage|integer|The increase percentage for the budget during non-promotion days.<br><br>A value of 50 means a 50% budget increase when the automatic budget increase is triggered.|
##|increase_limit|integer|The increase limit for the daily budget during non-promotion days.<br><br>A value of 10 means allows up to 10 budget increases per day when the automatic budget increases are triggered.|
##|current_budget|number|The specified campaign daily budget (`budget`).|
##|next_increase|number|The increase in budget compared with your specified campaign daily budget (`budget`).<br><br>Formula: `next_increase` = `current_budget` x `budget_increase_percentage`.<br><br>For example, if `budget` is 300 USD and `budget_increase_percentage` is 50, `next_increase` will be 150 USD, indicating a daily budget increase of 150 USD.|
##|remained_times|number|The remaining times of automatic budget increases.|
##|maximum_budget|number|The maximum possible budget.<br><br>Formula: `maximum_budget` = `current_budget` + `current_budget` x `budget_increase_percentage` x `remained_times`.<br><br>For example, if `current_budget` is 200 USD, `budget_increase_percentage` is 50, and `remained_times` is 10,  your `maximum_budget` will be 1200 USD, as the increase can occur up to 10 times daily.|
#| auto_budget_enabled {-to be deprecated} | boolean | Có thực hiện enable automatic budget increase.<br>When your achieved ROI reaches at least 90% of the target and 80% or more of your budget has been used, your daily campaign budget may automatically increase by up to 10 times to capture more sales. Your budget will reset to its original amount each day.<br><br><ul><li>When `is_enabled` within the object `promotion_days` is `true` and`auto_budget_enabled` is `false`, your ROI target will decrease and your daily budget will automatically increase during TikTok Shop promotion days (when `auto_schedule_enabled` is `true`) and custom promotion days as defined by `custom_schedule_list`. Your daily budget will reset to its original amount every day. During standard days, your ROI target and budget won't change.</li><li>When `is_enabled` within the object `promotion_days` is `true` and`auto_budget_enabled` is `true`, auto budget increase will be turned on during TikTok Shop promotion days (when `auto_schedule_enabled` is `true`), custom promotion days as defined by `custom_schedule_list`, <b>and standard days</b>. Your daily budget will reset to its original amount every day. During TikTok Shop promotion days and custom promotion days as defined by `custom_schedule_list`, your ROI target will decrease. During standard days, your ROI target won't change.</li><li>When `is_enabled` within the object `promotion_days` is `false` and`auto_budget_enabled` is `true`, your ROI won't change, your daily campaign budget may automatically increase up to 10 times to optimize gross revenue. Your daily budget will reset to its original amount every day.</li></ul><br>Các giá trị được hỗ trợ: `true`, `false`.|
#| schedule_type | string | Schedule type.<br><br>Các giá trị enum hỗ trợ: <ul><li>`SCHEDULE_FROM_NOW`: To run the campaign continuously after the scheduled start time.</li><li>`SCHEDULE_START_END`: To run the campaign between the scheduled start time and end time.</li></ul> |
#| schedule_start_time | string | Campaign delivery start time, in the format of `YYYY-MM-DD HH:MM:SS` (UTC+0). |
#| schedule_end_time | string | Campaign delivery end time, in the format of `YYYY-MM-DD HH:MM:SS` (UTC+0). |
#| placements | string[] | Placements.<br>The apps where you want to deliver your campaign. <br><br> Các giá trị enum hỗ trợ: <ul><li>`PLACEMENT_TIKTOK`: TikTok.</li><li>`PLACEMENT_PANGLE`: Pangle.</li></ul><br><p><span style="color:darkred"><b>Note</b></span>:  <ul><li>Product GMV Max Campaigns automatically explore and choose from the most extensive audience scope across TikTok and Pangle. Learn more [about Pangle](https://ads.tiktok.com/help/article/pangle-placement).</li><li>If you want to opt out of the Pangle placement for your Product GMV Max Campaigns, contact your TikTok representative.</li></ul>|
#| location_ids | string[] | The IDs of the targeted locations. <br><br> To learn about the corresponding location for a location ID, see **Location IDs**. |
#| age_groups | string[] | The targeted age groups.<br><br> Để xem danh sách giá trị enum, xem [Enumeration - Age Group](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
#| product_video_specific_type | string | The video selection mode. <br><br>Các giá trị enum hỗ trợ: <ul><li>`AUTO_SELECTION`: To autoselect videos.</li><li>`CUSTOM_SELECTION`: To manually select videos. </li><li>`UNSET`: Unset. </li></ul>|
#| identity_list | object[] | The list of identities (TikTok accounts) associated with the GMV Max Campaign. |
##| identity_id | string | Identity ID. |
##| identity_type | string | Identity type. <br><br>Các giá trị enum hỗ trợ: <ul><li>`AUTH_CODE`: Authorized User. This type of identity is created when you use the authorization code to access a TikTok account or a TikTok post.</li><li>`TT_USER`: TikTok User. This type of identity is created when you bind your TikTok For Business account with your TikTok Business Account, or when you bind your TikTok For Business account with your regular TikTok account and then upgrade the account to Business Account.</li><li>`BC_AUTH_TT`: TikTok Account User in Business Center. This type of identity is created when you add a TikTok account to your Business Center, and the TikTok account owner approves your request. </li><li>`TTS_TT`: TikTok Account User for TikTok Shop. This type of identity is created when you set an official TikTok account for the TikTok Shop.</li></ul> |
##| identity_authorized_bc_id | string | Returned only when `identity_type` is `BC_AUTH_TT`. <br><br>The ID of the Business Center that a TikTok Account User in Business Center identity is associated with. |
##| identity_authorized_shop_id | string | Returned for some `BC_AUTH_TT` identities. <br><br>The ID of the TikTok Shop that the TikTok Account User in Business Center identity is associated with. |
##| store_id | string | Returned only when `identity_type` is `TTS_TT`. <br><br>The ID of the TikTok Shop that a TikTok Account User for TikTok Shop identity is associated with. |
#|affiliate_posts_enabled |boolean|Có thực hiện enable affiliate posts for your Product GMV Max Campaign.<br>Affiliate posts are TikTok posts created by affiliates (creators participating in the TikTok Shop Affiliate Program) and authorized for use in TikTok Shop Ads. Learn more [about affiliate creatives for TikTok Shop Ads](https://ads.tiktok.com/help/article/about-affiliate-creatives-for-tiktok-shop-ads).<br><br>Các giá trị được hỗ trợ: `true`, `false`.|
#| item_list| object[] | The list of authorized TikTok posts associated with the GMV Max campaign. <br>Authorized TikTok posts are existing posts featuring your selected products from your TikTok accounts or authorized using video codes. |
##| item_id | string | The ID of the TikTok post. |
##| text | string | The caption of the TikTok post. |
##| spu_id_list| string[] | The list of Product SPU IDs that the TikTok post is associated with. |
##| identity_info | object | Information about the identity associated with the TikTok post. |
###| identity_id | string | Identity ID. |
###| identity_type | string | Identity type. <br><br>Các giá trị enum hỗ trợ: <ul><li>`AUTH_CODE`: Authorized User. This type of identity is created when you use the authorization code to access a TikTok account or a TikTok post.</li><li>`TT_USER`: TikTok User. This type of identity is created when you bind your TikTok For Business account with your TikTok Business Account, or when you bind your TikTok For Business account with your regular TikTok account and then upgrade the account to Business Account.</li><li>`BC_AUTH_TT`: TikTok Account User in Business Center. This type of identity is created when you add a TikTok account to your Business Center, and the TikTok account owner approves your request. </li><li>`TTS_TT`: TikTok Account User for TikTok Shop. This type of identity is created when you set an official TikTok account for the TikTok Shop.</li></ul> |
###| identity_authorized_bc_id | string | Returned only when `identity_type` is `BC_AUTH_TT`. <br><br>The ID of the Business Center that a TikTok Account User in Business Center identity is associated with. |
###| identity_authorized_shop_id | string | Returned for some `BC_AUTH_TT` identities. <br><br>The ID of the TikTok Shop that the TikTok Account User in Business Center identity is associated with. |
###| store_id | string | Returned only when `identity_type` is `TTS_TT`. <br><br>The ID of the TikTok Shop that a TikTok Account User for TikTok Shop identity is associated with. |
###| profile_image | string | Temporary profile image URL for the TikTok account that is associated with the identity. <br><br>Validity period: around 48 hours. The expiration time is included in the URL after the `x-expires` parameter, in the format of an Epoch/Unix timestamp in seconds.<br><br>Once the URL expires, you need to call [/campaign/gmv_max/info/](45-gmv-max-p1.md#doc-1822000968821762) to obtain a new URL. |
###| user_name| string | The username of the TikTok account that is associated with the identity. |
##| video_info | object | Details of the video in the post. |
###| video_id | string | The ID of the video. |
###| video_cover_url | string | Temporary URL for the video cover.<br><br>Validity period: around 24 hours. The expiration time is included in the URL after the `x-expires` parameter, in the format of an Epoch/Unix timestamp in seconds. <br><br>Once the URL expires, you need to call [/campaign/gmv_max/info/](45-gmv-max-p1.md#doc-1822000968821762) to obtain a new URL. |
###| preview_url | string | Temporary preview URL for the video. <br><br>Validity period: six hours.<br><br>Once the URL expires, you need to call [/campaign/gmv_max/info/](45-gmv-max-p1.md#doc-1822000968821762) to obtain a new URL. |
###| height | number | The height of the video in pixels. <br><br> Example: 1920. |
###| width | number | The width of the video in pixels.<br><br>Example: 1080. |
###| bit_rate | number | The bit rate of the video in bps. <br><br>Example: 8500323. |
###| duration | number | The duration of the video in seconds. <br><br>Example: 3.669. |
###| size | number | The size of the video in bytes. <br><br>Example: 3898461. |
###| signature | string | The MD5 of the video. <br><br>Example: `ab1cd2345e678fghi91jkl23b456m7no`. |
###| format | string | The format of the video.<br><br>Example: `mp4`. |
###| definition | string | The definition of the video.<br><br> Example: `1080p`. |
###| fps | number | The frames per second (FPS) of the video. <br><br>Example: 27. |
#|campaign_custom_anchor_video_id{-To-be-deprecated}|string|The ID of the collection of customized posts created in the Product GMV Max Campaign.<br><br>You can pass this field to [/gmv_max/custom_anchor_video_list/get/](45-gmv-max-p2.md#doc-1830215925061633) to obtain the details of the customized posts within the collection.<br><br><p><span style="color:darkred"><b>Important</b></span>: This field will be deprecated in the next API version. To ensure a seamless integration, retrieve the details of videos used in customized posts using [/gmv_max/creation/custom_anchor_video_list/get/](45-gmv-max-p2.md#doc-1866513156712449) and [/gmv_max/creation/shop_video/video_anchors/](45-gmv-max-p2.md#doc-1866513161692161).|
#| custom_anchor_video_list{-To-be-deprecated} | object[] | The list of customized TikTok posts associated with the GMV Max campaign. <br>Customized TikTok posts are posts with custom product links.<br><br><p><span style="color:darkred"><b>Important</b></span>: This field will be deprecated in the next API version. To ensure a seamless integration, retrieve the details of videos used in customized posts using [/gmv_max/creation/custom_anchor_video_list/get/](45-gmv-max-p2.md#doc-1866513156712449) and [/gmv_max/creation/shop_video/video_anchors/](45-gmv-max-p2.md#doc-1866513161692161). |
##| item_id | string | The ID of the TikTok post. |
##| spu_id_list| string[] | The list of Product SPU IDs that the TikTok post is associated with. |
##| identity_info | object | Information about the identity associated with the TikTok post. |
###| identity_id | string | Identity ID. |
###| identity_type | string | Identity type. <br><br>Các giá trị enum hỗ trợ: <ul><li>`AUTH_CODE`: Authorized User. This type of identity is created when you use the authorization code to access a TikTok account or a TikTok post.</li><li>`TT_USER`: TikTok User. This type of identity is created when you bind your TikTok For Business account with your TikTok Business Account, or when you bind your TikTok For Business account with your regular TikTok account and then upgrade the account to Business Account.</li><li>`BC_AUTH_TT`: TikTok Account User in Business Center. This type of identity is created when you add a TikTok account to your Business Center, and the TikTok account owner approves your request. </li><li>`TTS_TT`: TikTok Account User for TikTok Shop. This type of identity is created when you set an official TikTok account for the TikTok Shop.</li></ul> |
###| identity_authorized_bc_id | string | Returned only when `identity_type` is `BC_AUTH_TT`. <br><br>The ID of the Business Center that a TikTok Account User in Business Center identity is associated with. |
###| identity_authorized_shop_id | string | Returned for some `BC_AUTH_TT` identities. <br><br>The ID of the TikTok Shop that the TikTok Account User in Business Center identity is associated with. |
###| store_id | string | Returned only when `identity_type` is `TTS_TT`. <br><br>The ID of the TikTok Shop that a TikTok Account User for TikTok Shop identity is associated with. |

### Ví dụ lệnh cURL (Example)

#### Tạo chiến dịch GMV Max sản phẩm (Create a Product GMV Max Campaign)
```http
// curl
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "advertiser_id": "{{advertiser_id}}",
        "age_groups": [
            "AGE_18_24",
            "AGE_25_34",
            "AGE_35_44",
            "AGE_45_54",
            "AGE_55_100"
        ],
        "budget": {{budget}},
        "campaign_id": "{{campaign_id}}",
        "campaign_name": "{{campaign_name}}",
        "custom_anchor_video_list": [],
        "deep_bid_type": "VO_MIN_ROAS",
        "identity_list": [
            {
                "identity_id": "{{identity_id}}",
                "identity_type": "TTS_TT",
                "store_id": "{{store_id}}"
            },
            {
                "identity_id": "{{identity_id}}",
                "identity_type": "TT_USER"
            },
            {
                "identity_authorized_bc_id": "{{identity_authorized_bc_id}}",
                "identity_id": "{{identity_id}}",
                "identity_type": "BC_AUTH_TT"
            }
        ],
        "item_list": [],
        "location_ids": [
            "1562822"
        ],
        "operation_status": "ENABLE",
        "optimization_goal": "VALUE",
        "placements": [
            "PLACEMENT_TIKTOK"
        ],
        "product_specific_type": "ALL",
        "product_video_specific_type": "AUTO_SELECTION",
		"affiliate_posts_enabled": true,
        "roas_bid": {{roas_bid}},
        "schedule_end_time": "{{schedule_end_time}}",
        "schedule_start_time": "{{schedule_start_time}}",
        "schedule_type": "SCHEDULE_START_END",
        "shopping_ads_type": "PRODUCT",
        "store_authorized_bc_id": "{{store_authorized_bc_id}}",
        "store_id": "{{store_id}}"
    }
}
```

#### Tạo chiến dịch GMV Max LIVE (Create a LIVE GMV Max Campaign)
```http
// curl
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "advertiser_id": "{{advertiser_id}}",
        "age_groups": [
            "AGE_18_24",
            "AGE_25_34",
            "AGE_35_44",
            "AGE_45_54",
            "AGE_55_100"
        ],
        "budget": {{budget}},
        "campaign_id": "{{campaign_id}}",
        "campaign_name": "{{campaign_name}}",
        "custom_anchor_video_list": [],
        "deep_bid_type": "VO_MIN_ROAS",
        "identity_list": [
            {
                "identity_authorized_bc_id": "{{identity_authorized_bc_id}}",
                "identity_id": "{{identity_id}}",
                "identity_type": "BC_AUTH_TT"
            }
        ],
        "item_list": [],
		"affiliate_posts_enabled": false,
        "location_ids": [
            "1562822"
        ],
        "operation_status": "ENABLE",
        "optimization_goal": "VALUE",
        "placements": [
            "PLACEMENT_TIKTOK"
        ],
        "roas_bid": {{roas_bid}},
        "schedule_end_time": "{{schedule_end_time}}",
        "schedule_start_time": "{{schedule_start_time}}",
        "schedule_type": "SCHEDULE_START_END",
        "shopping_ads_type": "LIVE",
        "store_authorized_bc_id": "{{store_authorized_bc_id}}",
        "store_id": "{{store_id}}"
    }
}
```

---

<a id="doc-1822001009002497"></a>
<!-- doc_id: 1822001009002497 -->
<!-- doc_id: 1822001009002497 -->
# Cập nhật chiến dịch GMV Max (Update a GMV Max Campaign)
> Đường dẫn: API Reference > GMV Max > Update a GMV Max Campaign
Sử dụng endpoint này để cập nhật một chiến dịch GMV Max.

Endpoint này hỗ trợ cập nhật tăng dần.

> **Note:** 
> Nếu bạn muốn cập nhật trạng thái bật/tắt của Chiến dịch GMV Max, hãy sử dụng [/campaign/status/update/](24-campaign.md#doc-1739320994354178).

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/campaign/gmv_max/update/

**Method** POST

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). ⏎ Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type  ****(Bắt buộc)**** | string | Định dạng dữ liệu yêu cầu. ⏎ Allowed format: `application/json`. |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
| advertiser_id ***(Bắt buộc)*** | string | ID tài khoản quảng cáo TikTok. <br><br>To ensure that the ad account has exclusive GMV Max authorization for the TikTok Shop that you want to promote, call [/gmv_max/store/list/](45-gmv-max-p2.md#doc-1822001044479041) and confirm that the returned `advertiser_id` within `exclusive_authorized_advertiser_info` is the same as the ad account that you want to use to create GMV Max Campaigns.<ul><li>If the returned `advertiser_id` is not the same as the ad account that you want to use to create GMV Max Campaigns, use [/gmv_max/exclusive_authorization/create/](45-gmv-max-p2.md#doc-1822001200356354) to grant the ad account exclusive GMV Max authorization for the TikTok Shop.</li></ul>|
| campaign_id ***(Bắt buộc)*** | string | ID của một chiến dịch GMV Max.<br><br><ul><li>To create a GMV Max Campaign and obtain the ID chiến dịch quảng cáo, use [/campaign/gmv_max/create/](45-gmv-max-p1.md#doc-1822000988713089).</li><li>To filter existing GMV Max Campaigns within your ad account, use [/gmv_max/campaign/get/](45-gmv-max-p1.md#doc-1826463372290177).</li></ul> |
| roas_bid | number | Chỉ hợp lệ khi `deep_bid_type` of the campaign is `VO_MIN_ROAS`.<br><br> ROI target, kept to up to one decimal place. <br><br>Examples: 3.2, 3.<br><br>To obtain the recommended ROI target, use [/gmv_max/bid/recommend/](45-gmv-max-p1.md#doc-1822001024720897) and check the returned `roas_bid`. |
| budget | number | Ngân sách hàng ngày. <br><br> To obtain the recommended budget, use [/gmv_max/bid/recommend/](45-gmv-max-p1.md#doc-1822001024720897) and check the returned `budget`. |
| promotion_days | object | Chi tiết thiết lập các ngày diễn ra chương trình khuyến mại.<br><br><p><span style="color:darkred"><b>Note</b></span>: To customize the percentage and the maximum times the budget can increase per day within your promotion days settings, use `budget_increase_percentage` and `increase_limit`within this object.|
#| is_enabled | boolean | Có thực hiện enable promotion days to automatically optimize your campaign for higher GMV during high-intent shopping dates in regions where your ads are delivering. <br><br>Các giá trị được hỗ trợ: `true`, `false`.<br><br>When `promotion_days` is specified, this field will be automatically set to `true`. |
#| auto_schedule_enabled | boolean | Chỉ hợp lệ khi `is_enabled` is `true`.<br><br>Có thực hiện use TikTok Shop promotion days schedule.<br><br>Các giá trị được hỗ trợ: `true`, `false`.<br><br>When`is_enabled` is `true`, this field will be automatically set to `true`. |
#| custom_schedule_list {+Conditional} | object[] | Details of the custom promotion day schedules.<br><br><ul><li>If `auto_schedule_enabled` is `false`, specify at least one set of `start_date` and `end_date` in `custom_schedule_list`.</li><li>If `auto_schedule_enabled` is `true`, `custom_schedule_list` is optional.</li></ul>Kích thước tối đa: 50. |
##| start_date | string | The start date of the custom promotion day schedule, in the format of `YYYY-MM-DD`(ad account time zone).<br><br><p><span style="color:darkred"><b>Note</b></span>: <ul><li>The start date cannot be after the `end_date`.</li><li>The start date cannot be earlier than the current date.</li><li>The start date must be on the same day as or after the `schedule_start_time` of the campaign.</li><li>The custom promotion days schedule will automatically start at 00:00:00 of the start date in the ad account time zone.</li></ul> |
##| end_date | string | The end date of the custom promotion day schedule, in the format of `YYYY-MM-DD` (ad account time zone) .<br><br><p><span style="color:darkred"><b>Note</b></span>: <ul><li>The end date cannot be earlier than the current time.</li><li>The custom promotion days schedule will automatically end at 00:00:00 of the end date in the ad account time zone.</li></ul> |
#| roas_bid_multiplier | number | The target ROI index.<br>Changes to your target ROI will be in effect during promotion days and may drive higher GMV for this campaign.<br><br>Các giá trị enum hỗ trợ: <ul><li>`90`: -10%. To decrease your target ROI by 10% during promotion days.</li><li>`80`: -20%. To decrease your target ROI by 20% during promotion days.</li><li>`70`: -30%. To decrease your target ROI by 30% during promotion days.</li></ul> <br><p><span style="color:darkred"><b>Note</b></span>: We will be updating the way ROI goals are calculated during promotions to improve performance accuracy and ensure fairness across campaigns. Instead of using just the value you manually specify, the system will calculate your promotional ROI goal based on <b>the lower of your recent campaign performance (last 7 non-promotion days) or your entered ROI</b>, and then apply the selected reduction (10%, 20%, or 30%). This will be an allowlist-only feature. You might not need to make code changes, but the returned value of ROI goal will be different. |
#|budget_increase_percentage|integer|The increase percentage for the budget during promotion days.<br><br>Value range: 50-300.<br>A value of 50 means a 50% budget increase when the automatic budget increase is triggered.|
#|increase_limit|integer|The increase limit for the daily budget during promotion days.<br><br>Value range: 1-10.<br>A value of 10 means allows up to 10 budget increases per day when the automatic budget increases are triggered.|
|auto_budget|object|Chi tiết thiết lập ngân sách tự động trong những ngày không khuyến mại.|
#|auto_budget_enabled|boolean|Có thực hiện enable automatic budget increase during non-promotion days.<br>Enabling automatic budget increase will allow your daily budget to be automatically increased to optimize your campaign for more sales on days when your campaign has reached at least 90% of your ROI target and at least 80% of your budget has been used. Your daily budget will reset to its original amount each day.<br><br>Các giá trị được hỗ trợ: `true`, `false`.|
#|budget_increase_percentage|integer|The increase percentage for the budget during non-promotion days.<br><br>Value range: 50-300.<br>A value of 50 means a 50% budget increase when the automatic budget increase is triggered.|
#|increase_limit|integer|The increase limit for the budget during non-promotion days.<br><br>Value range: 1-10.<br>A value of 10 means allows up to 10 budget increases per day when the automatic budget increases are triggered.|
| auto_budget_enabled {-to be deprecated} | boolean | Có thực hiện enable automatic budget increase.<br>When your achieved ROI reaches at least 90% of the target and 80% or more of your budget has been used, your daily campaign budget may automatically increase by up to 10 times to capture more sales. Your budget will reset to its original amount each day.<br><br><ul><li>When `is_enabled` within the object `promotion_days` is `true` and`auto_budget_enabled` is `false`, your ROI target will decrease and your daily budget will automatically increase during TikTok Shop promotion days (when `auto_schedule_enabled` is `true`) and custom promotion days as defined by `custom_schedule_list`. Your daily budget will reset to its original amount every day. During standard days, your ROI target and budget won't change.</li><li>When `is_enabled` within the object `promotion_days` is `true` and`auto_budget_enabled` is `true`, auto budget increase will be turned on during TikTok Shop promotion days (when `auto_schedule_enabled` is `true`), custom promotion days as defined by `custom_schedule_list`,<b>and standard days</b>. Your daily budget will reset to its original amount every day. During TikTok Shop promotion days and custom promotion days as defined by `custom_schedule_list`, your ROI target will decrease. During standard days, your ROI target won't change.</li><li>When `is_enabled` within the object `promotion_days` is `false` and`auto_budget_enabled` is `true`, your ROI won't change, your daily campaign budget may automatically increase up to 10 times to optimize gross revenue. Your daily budget will reset to its original amount every day.<ul><li>However, if you specify `auto_budget_enabled` and `auto_budget` at the same time, `auto_budget_enabled` will be ignored.</li></ul></li></ul><br>Các giá trị được hỗ trợ: `true`, `false`.<br><br><p><span style="color:darkred"><b>Note</b></span>: When you use this parameter, the automatic budget increase settings for GMV Max Campaigns are fixed in terms of percentage and maximum frequency. If you want to customize the percentage and the maximum times the budget can increase per day during non-promotion days, use `auto_budget` instead. |
| item_group_ids | string[] | Valid when `shopping_ads_type` is `PRODUCT` and `product_specific_type` is `CUSTOMIZED_PRODUCTS`. <br><br>Product SPU (standard product unit) IDs. <br><br> Kích thước tối đa: 50.<br><br>To obtain the list of SPU IDs for products within a TikTok Shop, use [/store/product/get/](69-tiktok-store.md#doc-1793482248880130). Set `ad_creation_eligible` to `GMV_MAX` and select `item_group_id` values where `status` is `AVAILABLE` and `gmv_max_ads_status` is `UNOCCUPIED`. |
| schedule_type | string | Schedule type.<br><br>Các giá trị enum hỗ trợ: <ul><li>`SCHEDULE_FROM_NOW`: To run the campaign continuously after the scheduled start time.</li><li>`SCHEDULE_START_END`: To run the campaign between the scheduled start time and end time.</li></ul> |
| schedule_end_time **(Điều kiện)** | string | <ul><li>Bắt buộc khi `schedule_type` is `SCHEDULE_START_END`. </li><li>Not supported when `schedule_type` is `SCHEDULE_FROM_NOW`. </li></ul><br>Campaign delivery end time, in the format of `YYYY-MM-DD HH:MM:SS` (UTC+0). |
|affiliate_posts_enabled |boolean|Chỉ hợp lệ khi the following conditions are both met:<ul><li>`shopping_ads_type` is `PRODUCT`</li><li>`product_video_specific_type` is `AUTO_SELECTION`</li></ul>Có thực hiện enable affiliate posts for your Product GMV Max Campaign.<br>Affiliate posts are TikTok posts created by affiliates (creators participating in the TikTok Shop Affiliate Program) and authorized for use in TikTok Shop Ads. Learn more [about affiliate creatives for TikTok Shop Ads](https://ads.tiktok.com/help/article/about-affiliate-creatives-for-tiktok-shop-ads).<br><br>Các giá trị được hỗ trợ: `true`, `false`.|
| item_list  | object[] | Valid when `shopping_ads_type` is `PRODUCT` and `product_video_specific_type` is `CUSTOM_SELECTION`. <br><br>The list of authorized TikTok posts or customized TikTok posts to associate with the Product GMV Max campaign.<ul><li>Authorized TikTok posts are existing posts featuring your selected products from your TikTok accounts or authorized using video codes.<ul><li>If you want to manually select authorized TikTok posts only for the Product GMV Max campaign, include their details using `item_list` and do not specify `custom_anchor_video_list`.</li></ul></li><li>Customized TikTok posts are posts built by adding customized product links to videos. Two types are supported: campaign-level customized posts and shop-level customized posts.<ul><li>Campaign-level customized TikTok posts are newly created posts for the campaign, built by adding customized product links to your selected videos at the campaign level. These posts will be exclusive to this Product GMV Max campaign.<ul><li>If you want to manually select campaign-level customized TikTok posts for the Product GMV Max campaign, include details of the videos to be used in customized posts using `item_list` and specify `custom_anchor_video_list` simultaneously.</li></ul></li><li>Shop-level customized TikTok posts are newly created posts for the TikTok Shop, built by adding customized product links to your selected videos at the TikTok Shop level. These posts will be automatically added to this Product GMV Max campaign if the linked products are included in the campaign.<ul><li>If you want to manually select shop-level customized TikTok posts for the Product GMV Max campaign, include their details using `item_list` and do not specify `custom_anchor_video_list`.</li><li>To obtain shop-level customized TikTok posts, use [/gmv_max/creation/custom_anchor_video_list/get/](45-gmv-max-p2.md#doc-1866513156712449) with the `campaign_id` filter unspecified.</li></ul></li></ul></li></ul><br>Kích thước tối đa: 50.<br><br>To obtain a list of TikTok posts available for a Product GMV Max Campaign using the same TikTok Shop, use [/gmv_max/video/get/](45-gmv-max-p2.md#doc-1822001168512129). <br><br><p><span style="color:darkred"><b>Important</b></span>: The campaign-level customized posts feature will be deprecated in the next API version. To ensure a seamless integration, create shop-level customized posts using [/gmv_max/creation/custom_anchor_video_list/create/](45-gmv-max-p2.md#doc-1866513154013585) and retrieve the details of videos used in customized posts using [/gmv_max/creation/custom_anchor_video_list/get/](45-gmv-max-p2.md#doc-1866513156712449) and [/gmv_max/creation/shop_video/video_anchors/](45-gmv-max-p2.md#doc-1866513161692161).|
#| item_id {+Conditional} | string | Bắt buộc khi `item_list` is passed.<br><br> The ID of the TikTok post. |
#| spu_id_list {+Conditional} | string[] | Bắt buộc khi `item_list` is passed. <br><br> Product SPU IDs associated with the TikTok post. |
#| identity_info {+Conditional} | object | Bắt buộc khi `item_list` is passed. <br><br>Information about the identity associated with the TikTok post. |
##| identity_id {+Conditional} | string | Bắt buộc khi `item_list` is passed.<br><br> Identity ID. |
##| identity_type {+Conditional} | string | Bắt buộc khi `item_list` is passed.<br><br>Identity type. <br><br>Các giá trị enum hỗ trợ: <ul><li>`AUTH_CODE`: Authorized User. This type of identity is created when you use the authorization code to access a TikTok account or a TikTok post.</li><li>`TT_USER`: TikTok User. This type of identity is created when you bind your TikTok For Business account with your TikTok Business Account, or when you bind your TikTok For Business account with your regular TikTok account and then upgrade the account to Business Account.</li><li>`BC_AUTH_TT`: TikTok Account User in Business Center. This type of identity is created when you add a TikTok account to your Business Center, and the TikTok account owner approves your request. </li><li>`TTS_TT`: TikTok Account User for TikTok Shop. This type of identity is created when you set an official TikTok account for the TikTok Shop.</li></ul> |
##| identity_authorized_bc_id {+Conditional} | string | Bắt buộc khi `identity_type` is `BC_AUTH_TT`. <br><br> The ID of the Business Center that a TikTok Account User in Business Center identity is associated with. |
##| identity_authorized_shop_id {+Conditional} | string | Required only when `dentity_type` is `BC_AUTH_TT` and `identity_authorized_shop_id` is returned for the identity from [/gmv_max/identity/get/](45-gmv-max-p2.md#doc-1822001101474882). <br><br> The ID of the TikTok Shop that a TikTok Account User in Business Center identity is associated with. |
##| store_id {+Conditional} | string | Bắt buộc khi `identity_type` is `TTS_TT`. <br><br>The ID of the TikTok Shop that a TikTok Account User for TikTok Shop identity is associated with. |
#| video_info {+Conditional} | object | Bắt buộc khi `item_list` is passed. <br><br>Details of the video in the post. |
##| video_id {+Conditional} | string | Bắt buộc khi `item_list` is passed. <br><br> The ID of the video. |
| custom_anchor_video_list{-To-be-deprecated} | object[] | The list of customized TikTok posts to associate with the Product GMV Max campaign.<br>Customized TikTok posts are posts created during campaign setup by adding customized product links for your products (`spu_id_list` within `custom_anchor_video_list`) to specified videos (`item_id` within `custom_anchor_video_list`). These posts will be exclusive to this Product GMV Max campaign.<ul><li>For manual selection: When `shopping_ads_type` is `PRODUCT` and `product_video_specific_type` is `CUSTOM_SELECTION`, specify the videos to be used in customized posts using this field.</li><li>For auto selection: When `shopping_ads_type` is `PRODUCT` and `product_video_specific_type` is `AUTO_SELECTION`, specify the videos to be auto-selected for customized posts using this field.</li></ul><br>Kích thước tối đa: 2,000.<br><br><p><span style="color:darkred"><b>Important</b></span>: This field will be deprecated along with the campaign-level customized posts feature in the next API version. To ensure a seamless integration, create shop-level customized posts using [/gmv_max/creation/custom_anchor_video_list/create/](45-gmv-max-p2.md#doc-1866513154013585) and retrieve the details of videos used in customized posts using [/gmv_max/creation/custom_anchor_video_list/get/](45-gmv-max-p2.md#doc-1866513156712449) and [/gmv_max/creation/shop_video/video_anchors/](45-gmv-max-p2.md#doc-1866513161692161).<br><br><p><span style="color:darkred"><b>Note</b></span>: <ul><li>If you want to specify more than 200 customized posts for a Product GMV Max Campaign, you can update the `custom_anchor_video_list` of the campaign incrementally, with updates limited to 200 additional posts per request. <ul><li>For example, if you created the campaign with 200 customized posts and want to increase the post count to 400, specify 400 customized posts including the original 200 and the additional 200 ones through this field. </li></ul></li><li>If you want to remove certain customized posts from the Product GMV Max Campaign, make sure to remove the posts from both `custom_anchor_video_list` and `item_list` simultaneously. </li></ul>|
#| item_id {+Conditional}| string | Bắt buộc khi `custom_anchor_video_list` is passed.<br><br>The ID of a TikTok video to be used in a customized post.<br><br>To retrieve eligible videos, use [/gmv_max/video/get/](45-gmv-max-p2.md#doc-1822001168512129) with `custom_posts_eligible` set to true. |
#| spu_id_list {+Conditional}| string[] | Bắt buộc khi `custom_anchor_video_list` is passed.<br><br>The SPU IDs of the products to associate with the customized product anchor link in the TikTok post.<br><br>Kích thước tối đa: 1. |
#| identity_info {+Conditional}| object | Bắt buộc khi `custom_anchor_video_list` is passed.<br><br>Information about the identity to associate with the post. |
##| identity_id {+Conditional}| string | Bắt buộc khi `custom_anchor_video_list` is passed.<br><br>Identity ID.<br><br>To obtain a list of identities available for GMV Max Campaigns, use [/gmv_max/identity/get/](45-gmv-max-p2.md#doc-1822001101474882). |
##| identity_type{+Conditional} | string | Bắt buộc khi `custom_anchor_video_list` is passed.<br><br>Identity type.<br><br>Các giá trị enum hỗ trợ: <ul><li>`AUTH_CODE`: Authorized User. This type of identity is created when you use the authorization code to access a TikTok account or a TikTok post.</li><li>`TT_USER`: TikTok User. This type of identity is created when you bind your TikTok For Business account with your TikTok Business Account, or when you bind your TikTok For Business account with your regular TikTok account and then upgrade the account to Business Account.</li><li>`BC_AUTH_TT`: TikTok Account User in Business Center. This type of identity is created when you add a TikTok account to your Business Center, and the TikTok account owner approves your request.</li><li>`TTS_TT`: TikTok Account User for TikTok Shop. This type of identity is created when you set an official TikTok account for the TikTok Shop.</li></ul> |
##| identity_authorized_bc_id {+Conditional}| string | Bắt buộc khi `identity_type` is `BC_AUTH_TT`.<br><br>The ID of the Business Center that a TikTok Account User in Business Center identity is associated with. |
##| identity_authorized_shop_id {+Conditional}| string | Required only when `identity_type` is `BC_AUTH_TT` and `identity_authorized_shop_id` is returned for the identity from [/gmv_max/identity/get/](45-gmv-max-p2.md#doc-1822001101474882).<br><br>The ID of the TikTok Shop that a TikTok Account User in Business Center identity is associated with. |
##| store_id {+Conditional}| string | Bắt buộc khi `identity_type` is `TTS_TT`.<br><br>The ID of the TikTok Shop that a TikTok Account User for TikTok Shop identity is associated with. |
| campaign_name | string | The name of the GMV Max Campaign. |

### Ví dụ lệnh cURL (Example)

```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/campaign/gmv_max/update/' \
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
|code |number|Response code. For the complete list of response codes and descriptions, see [Appendix-Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message|string|Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|request_id |string|Mã log ID của một yêu cầu, dùng để định danh duy nhất yêu cầu đó.  |
|data |object|Returned data.|
#| advertiser_id | string | ID tài khoản quảng cáo TikTok. |
#| operation_status| string | The status of the GMV Max Campaign.<br><br>Các giá trị enum hỗ trợ: <ul><li>`DISABLE`: Disabled.</li><li>`ENABLE`: Enabled. </li></ul> |
#| campaign_id | string | The ID of the GMV Max Campaign. |
#| campaign_name | string | The name of the GMV Max Campaign. |
#| store_id | string | ID của TikTok Shop. |
#| store_authorized_bc_id | string | ID của Business Center được ủy quyền truy cập vào TikTok Shop (`store_id`). |
#| shopping_ads_type | string | Loại chiến dịch GMV Max.<br><br>Các giá trị enum hỗ trợ: <ul><li>`PRODUCT`: Product GMV Max Campaign.</li><li>`LIVE`: Live GMV Max Campaign. </li></ul> |
#| product_specific_type | string | Các chiều khác nhau để lựa chọn sản phẩm. <br><br>Các giá trị enum hỗ trợ: <ul><li>`ALL`: Allow TikTok to dynamically choose from all products within the TikTok Shop.</li><li>`CUSTOMIZED_PRODUCTS`: Specify a customized number of products within the TikTok Shop.</li><li>`UNSET`: Unset.</li></ul> |
#| item_group_ids | string[] | Returned only when `shopping_ads_type` is `PRODUCT` and `product_specific_type` is `CUSTOMIZED_PRODUCTS`. <br><br>Product SPU (standard product unit) IDs. |
#| optimization_goal | string | Optimization goal. <br><br>Enum value:<ul><li>`VALUE`: Gross revenue.</li></ul>|
#| roi_protection_enabled | boolean | Liệu campaign is eligible for ROI protection. <br>ROI protection is a feature that automatically issues ad credits when the return on investment (ROI) for your campaign falls below a certain threshold despite following GMV Max guidelines and best practices. To learn about the eligibility criteria for ROI protection and scenarios where the campaign is ineligible for ROI protection, see [About ROI protection for GMV Max campaigns](https://ads.tiktok.com/help/article/about-roi-protection-for-gmv-max-campaigns).<br><br>Các giá trị được hỗ trợ: `true`, `false`.|
#| deep_bid_type | string | Bid strategy. <br><br>Enum value:<ul><li>`VO_MIN_ROAS`: Minimum ROAS. Bid with an ROI target.</li></ul>|
#| roas_bid | number | Returned only when `deep_bid_type` is `VO_MIN_ROAS`.<br><br>ROI target. |
#| budget | number | Ngân sách hàng ngày. |
#| promotion_days | object | Chi tiết thiết lập các ngày diễn ra chương trình khuyến mại. |
##| is_enabled | boolean | Có thực hiện enable promotion days to automatically optimize your campaign for higher GMV during high-intent shopping dates in regions where your ads are delivering. <br>When promotion days are active for this campaign, your ad credits will be calculated for your promotion days target ROI setting.<br><br>Các giá trị được hỗ trợ: `true`, `false`. |
##| auto_schedule_enabled | boolean | Có thực hiện use TikTok Shop promotion days schedule.<br><br>Các giá trị được hỗ trợ: `true`, `false`. |
##| custom_schedule_list | object[] | Details of the custom promotion day schedules. |
###| start_time | string | The start time of the custom promotion day schedule, in the format of `YYYY-MM-DD` (ad account time zone). |
###| end_time | string | The end time of the custom promotion day schedule, in the format of `YYYY-MM-DD`  (ad account time zone). |
##| roas_bid_multiplier | number | The target ROI index.<br>Changes to your target ROI will be in effect during promotion days and may drive higher GMV for this campaign.<br><br>Các giá trị enum hỗ trợ: <ul><li>`90`: -10%. To decrease your target ROI by 10% during promotion days.</li><li>`80`: -20%. To decrease your target ROI by 20% during promotion days.</li><li>`70`: -30%. To decrease your target ROI by 30% during promotion days.</li></ul> |
##| adjusted_roas_bid | number | Promotion days target ROI. |
##|budget_increase_percentage|integer|The increase percentage for the budget during promotion days.<br><br>A value of 50 means a 50% budget increase when the automatic budget increase is triggered.|
##|increase_limit|integer|The increase limit for the daily budget during promotion days.<br><br>A value of 10 means allows up to 10 budget increases per day when the automatic budget increases are triggered.|
##| current_budget | number |The specified campaign daily budget (`budget`). |
##| next_increase | number | The increase in budget compared with your specified campaign daily budget (`budget`).<br><br>Formula: `next_increase` = `current_budget` x `budget_increase_percentage`.<br><br>For example, if `budget` is 300 USD and `budget_increase_percentage` is 50, `next_increase` will be 150 USD, indicating a daily budget increase of 150 USD.|
##|remained_times|number|The remaining times of automatic budget increases.|
##|maximum_budget|number|The maximum possible budget.<br><br>Formula: `maximum_budget` = `current_budget` + `current_budget` x `budget_increase_percentage` x `remained_times`.<br><br>For example, if `current_budget` is 200 USD, `budget_increase_percentage` is 50, and `remained_times` is 10,  your `maximum_budget` will be 1200 USD, as the increase can occur up to 10 times daily.|
##| estimated_gross_revenue_increase | string | The estimated percentage increase in gross revenue due to the ROI change during promotion days. <br><br>Example: `24%`. |
#|auto_budget|object|Chi tiết thiết lập ngân sách tự động trong những ngày không khuyến mại.|
##|auto_budget_enabled|boolean|Có thực hiện enable automatic budget increase during non-promotion days.<br><br>Enabling automatic budget increase will allow your daily budget to be automatically increased to optimize your campaign for more sales on days when your campaign has reached at least 90% of your ROI target and at least 80% of your budget has been used. Your daily budget will reset to its original amount each day.<br><br>Các giá trị được hỗ trợ: `true`, `false`.|
##|budget_increase_percentage|integer|The increase percentage for the budget during non-promotion days.<br><br>A value of 50 means a 50% budget increase when the automatic budget increase is triggered.|
##|increase_limit|integer|The increase limit for the daily budget during non-promotion days.<br><br>A value of 10 means allows up to 10 budget increases per day when the automatic budget increases are triggered.|
##|current_budget|number|The specified campaign daily budget (`budget`).|
##|next_increase|number|The increase in budget compared with your specified campaign daily budget (`budget`).<br><br>Formula: `next_increase` = `current_budget` x `budget_increase_percentage`.<br><br>For example, if `budget` is 300 USD and `budget_increase_percentage` is 50, `next_increase` will be 150 USD, indicating a daily budget increase of 150 USD.|
##|remained_times|number|The remaining times of automatic budget increases.|
##|maximum_budget|number|The maximum possible budget.<br><br>Formula: `maximum_budget` = `current_budget` + `current_budget` x `budget_increase_percentage` x `remained_times`.<br><br>For example, if `current_budget` is 200 USD, `budget_increase_percentage` is 50, and `remained_times` is 10,  your `maximum_budget` will be 1200 USD, as the increase can occur up to 10 times daily.|
#| auto_budget_enabled{-to be deprecated} | boolean | Có thực hiện enable automatic budget increase.<br>When your achieved ROI reaches at least 90% of the target and 80% or more of your budget has been used, your daily campaign budget may automatically increase by up to 10 times to capture more sales. Your budget will reset to its original amount each day.<br><br><ul><li>When `is_enabled` within the object `promotion_days` is `true` and`auto_budget_enabled` is `false`, your ROI target will decrease and your daily budget will automatically increase during TikTok Shop promotion days (when `auto_schedule_enabled` is `true`) and custom promotion days as defined by `custom_schedule_list`. Your daily budget will reset to its original amount every day. During standard days, your ROI target and budget won't change.</li><li>When `is_enabled` within the object `promotion_days` is `true` and`auto_budget_enabled` is `true`, auto budget increase will be turned on during TikTok Shop promotion days (when `auto_schedule_enabled` is `true`), custom promotion days as defined by `custom_schedule_list`,<b>and standard days</b>. Your daily budget will reset to its original amount every day. During TikTok Shop promotion days and custom promotion days as defined by `custom_schedule_list`, your ROI target will decrease. During standard days, your ROI target won't change.</li><li>When `is_enabled` within the object `promotion_days` is `false` and`auto_budget_enabled` is `true`, your ROI won't change, your daily campaign budget may automatically increase up to 10 times to optimize gross revenue. Your daily budget will reset to its original amount every day.</li></ul><br>Các giá trị được hỗ trợ: `true`, `false`.|
#| schedule_type | string | Schedule type.<br><br>Các giá trị enum hỗ trợ: <ul><li>`SCHEDULE_FROM_NOW`: To run the campaign continuously after the scheduled start time.</li><li>`SCHEDULE_START_END`: To run the campaign between the scheduled start time and end time.</li></ul> |
#| schedule_start_time | string | Campaign delivery start time, in the format of `YYYY-MM-DD HH:MM:SS` (UTC+0). |
#| schedule_end_time | string | Campaign delivery end time, in the format of `YYYY-MM-DD HH:MM:SS` (UTC+0). |
#| placements | string[] | Placements.<br>The apps where you want to deliver your campaign. <br><br> Các giá trị enum hỗ trợ: <ul><li>`PLACEMENT_TIKTOK`: TikTok.</li><li>`PLACEMENT_PANGLE`: Pangle.</li></ul><br><p><span style="color:darkred"><b>Note</b></span>:  <ul><li>Product GMV Max Campaigns automatically explore and choose from the most extensive audience scope across TikTok and Pangle. Learn more [about Pangle](https://ads.tiktok.com/help/article/pangle-placement).</li><li>If you want to opt out of the Pangle placement for your Product GMV Max Campaigns, contact your TikTok representative.</li></ul>|
#| location_ids | string[] | The IDs of the targeted locations. <br><br> To learn about the corresponding location for a location ID, see **Location IDs**. |
#| age_groups | string[] | The targeted age groups.<br><br> Để xem danh sách giá trị enum, xem [Enumeration - Age Group](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
#| product_video_specific_type | string | The video selection mode. <br><br>Các giá trị enum hỗ trợ: <ul><li>`AUTO_SELECTION`: To autoselect videos.</li><li>`CUSTOM_SELECTION`: To manually select videos. </li><li>`UNSET`: Unset. </li></ul>|
#| identity_list | object[] | The list of identities (TikTok accounts) associated with the GMV Max Campaign. |
##| identity_id | string | Identity ID. |
##| identity_type | string | Identity type. <br><br>Các giá trị enum hỗ trợ: <ul><li>`AUTH_CODE`: Authorized User. This type of identity is created when you use the authorization code to access a TikTok account or a TikTok post.</li><li>`TT_USER`: TikTok User. This type of identity is created when you bind your TikTok For Business account with your TikTok Business Account, or when you bind your TikTok For Business account with your regular TikTok account and then upgrade the account to Business Account.</li><li>`BC_AUTH_TT`: TikTok Account User in Business Center. This type of identity is created when you add a TikTok account to your Business Center, and the TikTok account owner approves your request. </li><li>`TTS_TT`: TikTok Account User for TikTok Shop. This type of identity is created when you set an official TikTok account for the TikTok Shop.</li></ul> |
##| identity_authorized_bc_id | string | Returned only when `identity_type` is `BC_AUTH_TT`. <br><br>The ID of the Business Center that a TikTok Account User in Business Center identity is associated with. |
##| identity_authorized_shop_id | string | Returned for some `BC_AUTH_TT` identities. <br><br>The ID of the TikTok Shop that the TikTok Account User in Business Center identity is associated with. |
##| store_id | string | Returned only when `identity_type` is `TTS_TT`. <br><br>The ID of the TikTok Shop that a TikTok Account User for TikTok Shop identity is associated with. |
#|affiliate_posts_enabled |boolean|Có thực hiện enable affiliate posts for your Product GMV Max Campaign.<br>Affiliate posts are TikTok posts created by affiliates (creators participating in the TikTok Shop Affiliate Program) and authorized for use in TikTok Shop Ads. Learn more [about affiliate creatives for TikTok Shop Ads](https://ads.tiktok.com/help/article/about-affiliate-creatives-for-tiktok-shop-ads).<br><br>Các giá trị được hỗ trợ: `true`, `false`.|
#| item_list| object[] | The list of authorized TikTok posts associated with the GMV Max campaign. <br>Authorized TikTok posts are existing posts featuring your selected products from your TikTok accounts or authorized using video codes. |
##| item_id | string | The ID of the TikTok post. |
##| text | string | The caption of the TikTok post. |
##| spu_id_list| string[] | The list of Product SPU IDs that the TikTok post is associated with. |
##| identity_info | object | Information about the identity associated with the TikTok post. |
###| identity_id | string | Identity ID. |
###| identity_type | string | Identity type. <br><br>Các giá trị enum hỗ trợ: <ul><li>`AUTH_CODE`: Authorized User. This type of identity is created when you use the authorization code to access a TikTok account or a TikTok post.</li><li>`TT_USER`: TikTok User. This type of identity is created when you bind your TikTok For Business account with your TikTok Business Account, or when you bind your TikTok For Business account with your regular TikTok account and then upgrade the account to Business Account.</li><li>`BC_AUTH_TT`: TikTok Account User in Business Center. This type of identity is created when you add a TikTok account to your Business Center, and the TikTok account owner approves your request. </li><li>`TTS_TT`: TikTok Account User for TikTok Shop. This type of identity is created when you set an official TikTok account for the TikTok Shop.</li></ul> |
###| identity_authorized_bc_id | string | Returned only when `identity_type` is `BC_AUTH_TT`. <br><br>The ID of the Business Center that a TikTok Account User in Business Center identity is associated with. |
###| identity_authorized_shop_id | string | Returned for some `BC_AUTH_TT` identities. <br><br>The ID of the TikTok Shop that the TikTok Account User in Business Center identity is associated with. |
###| store_id | string | Returned only when `identity_type` is `TTS_TT`. <br><br>The ID of the TikTok Shop that a TikTok Account User for TikTok Shop identity is associated with. |
###| profile_image | string | Temporary profile image URL for the TikTok account that is associated with the identity. <br><br>Validity period: around 48 hours. The expiration time is included in the URL after the `x-expires` parameter, in the format of an Epoch/Unix timestamp in seconds.<br><br>Once the URL expires, you need to call [/campaign/gmv_max/info/](45-gmv-max-p1.md#doc-1822000968821762) to obtain a new URL. |
###| user_name| string | The username of the TikTok account that is associated with the identity. |
##| video_info | object | Details of the video in the post. |
###| video_id | string | The ID of the video. |
###| video_cover_url | string | Temporary URL for the video cover.<br><br>Validity period: around 24 hours. The expiration time is included in the URL after the `x-expires` parameter, in the format of an Epoch/Unix timestamp in seconds. <br><br>Once the URL expires, you need to call [/campaign/gmv_max/info/](45-gmv-max-p1.md#doc-1822000968821762) to obtain a new URL. |
###| preview_url | string | Temporary preview URL for the video. <br><br>Validity period: six hours.<br><br>Once the URL expires, you need to call [/campaign/gmv_max/info/](45-gmv-max-p1.md#doc-1822000968821762) to obtain a new URL. |
###| height | number | The height of the video in pixels. <br><br> Example: 1920. |
###| width | number | The width of the video in pixels.<br><br>Example: 1080. |
###| bit_rate | number | The bit rate of the video in bps. <br><br>Example: 8500323. |
###| duration | number | The duration of the video in seconds. <br><br>Example: 3.669. |
###| size | number | The size of the video in bytes. <br><br>Example: 3898461. |
###| signature | string | The MD5 of the video. <br><br>Example: `ab1cd2345e678fghi91jkl23b456m7no`. |
###| format | string | The format of the video.<br><br>Example: `mp4`. |
###| definition | string | The definition of the video.<br><br> Example: `1080p`. |
###| fps | number | The frames per second (FPS) of the video. <br><br>Example: 27. |
#|campaign_custom_anchor_video_id{-To-be-deprecated}|string|The ID of the collection of customized posts created in the Product GMV Max Campaign.<br><br>You can pass this field to [/gmv_max/custom_anchor_video_list/get/](45-gmv-max-p2.md#doc-1830215925061633) to obtain the details of the customized posts within the collection.<br><br><p><span style="color:darkred"><b>Important</b></span>: This field will be deprecated in the next API version. To ensure a seamless integration, retrieve the details of videos used in customized posts using [/gmv_max/creation/custom_anchor_video_list/get/](45-gmv-max-p2.md#doc-1866513156712449) and [/gmv_max/creation/shop_video/video_anchors/](45-gmv-max-p2.md#doc-1866513161692161).|
#| custom_anchor_video_list {-To-be-deprecated}| object[] | The list of customized TikTok posts associated with the GMV Max campaign. <br>Customized TikTok posts are posts with custom product links. <br><br><p><span style="color:darkred"><b>Important</b></span>: This field will be deprecated in the next API version. To ensure a seamless integration, retrieve the details of videos used in customized posts using [/gmv_max/creation/custom_anchor_video_list/get/](45-gmv-max-p2.md#doc-1866513156712449) and [/gmv_max/creation/shop_video/video_anchors/](45-gmv-max-p2.md#doc-1866513161692161).|
##| item_id | string | The ID of the TikTok post. |
##| spu_id_list| string[] | The list of Product SPU IDs that the TikTok post is associated with. |
##| identity_info | object | Information about the identity associated with the TikTok post. |
###| identity_id | string | Identity ID. |
###| identity_type | string | Identity type. <br><br>Các giá trị enum hỗ trợ: <ul><li>`AUTH_CODE`: Authorized User. This type of identity is created when you use the authorization code to access a TikTok account or a TikTok post.</li><li>`TT_USER`: TikTok User. This type of identity is created when you bind your TikTok For Business account with your TikTok Business Account, or when you bind your TikTok For Business account with your regular TikTok account and then upgrade the account to Business Account.</li><li>`BC_AUTH_TT`: TikTok Account User in Business Center. This type of identity is created when you add a TikTok account to your Business Center, and the TikTok account owner approves your request. </li><li>`TTS_TT`: TikTok Account User for TikTok Shop. This type of identity is created when you set an official TikTok account for the TikTok Shop.</li></ul> |
###| identity_authorized_bc_id | string | Returned only when `identity_type` is `BC_AUTH_TT`. <br><br>The ID of the Business Center that a TikTok Account User in Business Center identity is associated with. |
###| identity_authorized_shop_id | string | Returned for some `BC_AUTH_TT` identities. <br><br>The ID of the TikTok Shop that the TikTok Account User in Business Center identity is associated with. |
###| store_id | string | Returned only when `identity_type` is `TTS_TT`. <br><br>The ID of the TikTok Shop that a TikTok Account User for TikTok Shop identity is associated with. |

### Ví dụ lệnh cURL (Example)

```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "advertiser_id": "{{advertiser_id}}",
        "age_groups": [
            "AGE_18_24",
            "AGE_25_34",
            "AGE_35_44",
            "AGE_45_54",
            "AGE_55_100"
        ],
        "budget": {{budget}},
        "campaign_id": "{{campaign_id}}",
        "campaign_name": "{{campaign_name}}",
        "custom_anchor_video_list": [],
        "deep_bid_type": "VO_MIN_ROAS",
        "identity_list": [
            {
                "identity_id": "{{identity_id}}",
                "identity_type": "TTS_TT",
                "store_id": "{{store_id}}"
            },
            {
                "identity_id": "{{identity_id}}",
                "identity_type": "TT_USER"
            },
            {
                "identity_authorized_bc_id": "{{identity_authorized_bc_id}}",
                "identity_id": "{{identity_id}}",
                "identity_type": "BC_AUTH_TT"
            }
        ],
        "item_list": [],
        "location_ids": [
            "1562822"
        ],
        "operation_status": "ENABLE",
        "optimization_goal": "VALUE",
        "placements": [
            "PLACEMENT_TIKTOK"
        ],
        "product_specific_type": "ALL",
        "product_video_specific_type": "AUTO_SELECTION",
		"affiliate_posts_enabled": true,
        "roas_bid": {{roas_bid}},
        "schedule_end_time": "{{schedule_end_time}}",
        "schedule_start_time": "{{schedule_start_time}}",
        "schedule_type": "SCHEDULE_START_END",
        "shopping_ads_type": "PRODUCT",
        "store_authorized_bc_id": "{{store_authorized_bc_id}}",
        "store_id": "{{store_id}}"
    }
}
```

---

<a id="doc-1822001024720897"></a>
<!-- doc_id: 1822001024720897 -->
<!-- doc_id: 1822001024720897 -->
# Lấy mục tiêu ROI và ngân sách đề xuất cho GMV Max (Get the recommended GMV Max ROI target and budget)
> Đường dẫn: API Reference > GMV Max > Get the recommended GMV Max ROI target and budget
Dùng endpoint này để lấy mục tiêu ROI và ngân sách đề xuất cho chiến dịch Product GMV Max hoặc Live GMV sử dụng một TikTok Shop cụ thể.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/gmv_max/bid/recommend/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). ⏎ Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
| advertiser_id ***(Bắt buộc)*** | string | ID tài khoản quảng cáo TikTok. |
| store_id ***(Bắt buộc)*** | string | ID của TikTok Shop.<br><br> To obtain a TikTok Shop that is available for GMV Max Campaigns, use [/gmv_max/store/list/](45-gmv-max-p2.md#doc-1822001044479041) and confirm that the returned `is_gmv_max_available` is `true`. |
| shopping_ads_type ***(Bắt buộc)*** | string | Loại chiến dịch GMV Max.<br><br>Các giá trị enum hỗ trợ: <ul><li>`PRODUCT`: Product GMV Max Campaign.</li><li>`LIVE`: Live GMV Max Campaign. </li></ul> |
| optimization_goal ***(Bắt buộc)*** | string | Optimization goal. <br><br>Enum value:<ul><li>`VALUE`: Gross revenue.</li></ul>|
| item_group_ids  | string[] | Chỉ hợp lệ khi `shopping_ads_type` is `PRODUCT`. <br><br>The list of SPU (standard product unit) IDs for specific products to be promoted in a Product GMV Max Campaign.<br><br> <ul><li>If you want to promote all products from the TikTok Shop in the Product GMV Max Campaign, you don't need to pass this field.</li><li>If you want to promote specific products from the TikTok Shop in the Product GMV Max Campaign, specify these products via this field.</li></ul><br> Kích thước tối đa: 50.<br><br>To obtain the list of SPU IDs for products within a TikTok Shop, use [/store/product/get/](69-tiktok-store.md#doc-1793482248880130). Set `ad_creation_eligible` to `GMV_MAX` and select `item_group_id` values where `status` is `AVAILABLE` and `gmv_max_ads_status` is `UNOCCUPIED`. |
|identity_id **(Điều kiện)**|string|Required and Chỉ hợp lệ khi `shopping_ads_type` is `LIVE` <br><br>The LIVE source identity that you want to use in a LIVE GMV Max Campaign.  <br><br>To obtain a list of identities for LIVE GMV Max Campaigns, use [/gmv_max/identity/get/](45-gmv-max-p2.md#doc-1822001101474882) and select identities with`live_gmv_max_available` as `true`.|

### Ví dụ lệnh cURL (Example)
#### Dành cho chiến dịch GMV Max sản phẩm (For Product GMV Max Campaigns)
```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/gmv_max/bid/recommend/?advertiser_id={{advertiser_id}}&store_id={{store_id}}&shopping_ads_type=PRODUCT&optimization_goal=VALUE' \
--header 'Access-Token: {{Access_Token}}'
```

#### Dành cho chiến dịch GMV Max LIVE (For LIVE GMV Max Campaigns)
```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/gmv_max/bid/recommend/?advertiser_id={{advertiser_id}}&store_id={{store_id}}&shopping_ads_type=LIVE&optimization_goal=VALUE&identity_id={{identity_id}}' \
--header 'Access-Token: {{Access_Token}}'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|code |number|Response code. For the complete list of response codes and descriptions, see [Appendix-Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message|string|Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|request_id |string|Mã log ID của một yêu cầu, dùng để định danh duy nhất yêu cầu đó.  |
|data |object|Returned data.|
#| roas_bid | number | Recommended ROI target for the optimization goal Groess revenue.<br> The ROI is based on the average ROI for your product category. |
#| budget | number | Recommended daily budget for the optimization goal Groess revenue, in the currency of the ad account. <br>The budget is calculated with your average ad spend for your selected products or average ad spend in your product category from the previous 14 days. Higher budgets are recommended to ensure delivery throughout the day because lower budgets may spend more quickly and limit your campaign performance. <br><br>To retrieve the currency of an ad account, use [/advertiser/info/](03-ad-accounts.md#doc-1739593083610113) and check the returned `currency`. |

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "budget": 300,
        "roas_bid": 2
    }
}
```

---

<a id="doc-1835246967275522"></a>
<!-- doc_id: 1835246967275522 -->
<!-- doc_id: 1835246967275522 -->
# Tạo phiên tăng tốc phân phối tối đa hoặc tăng tốc mẫu sáng tạo (Create a max delivery or creative boost session)
> Đường dẫn: API Reference > GMV Max > Create a max delivery or creative boost session
Sử dụng endpoint này để tạo a max delivery session for a specific product or a creative boost session for a specific video in a Product GMV Max Campaign.

- Max delivery for GMV Max uses an additional budget and maximizes gross revenue for selected products in your campaign over a selected period of time. Learn more [about Max delivery optimization for GMV Max](https://ads.tiktok.com/help/article/about-max-delivery-optimization-for-gmv-max). 
- Creative Boost is a functionality within Product GMV Max that allows sellers to manually promote specific videos by allocating extra daily budget. 

## Điều kiện tiên quyết trước khi bắt đầu
### Điều kiện tiên quyết để tạo phiên tăng tốc phân phối tối đa (Prerequisites for creating a max delivery session)
- Ensure that the current optimization mode of the campaign is Target ROI. Use [/gmv_max/report/get/](45-gmv-max-p2.md#doc-1824721673497601) to retrieve campaign details and verify that the `bid_type` metric is `CUSTOM`. Learn about [available GMV Max Campaign report metrics](45-gmv-max-p3.md#doc-1824722485971009).
- Để lấy `campaign_id` hợp lệ, bạn có thể sử dụng một trong các cách sau:
  - Create a new Product GMV Max Campaign using [/campaign/gmv_max/create/](45-gmv-max-p1.md#doc-1822000988713089) with `shopping_ads_type` set to `PRODUCT`.
  - Filter existing Product GMV Max Campaigns within your ad account using [/gmv_max/campaign/get/](45-gmv-max-p1.md#doc-1826463372290177) with `filtering` set to `{"gmv_max_promotion_types":["PRODUCT_GMV_MAX"]}`.

### Điều kiện tiên quyết để tạo phiên tăng tốc mẫu sáng tạo (Prerequisites for creating a creative boost session)
- Ensure that the campaign is in active status. 
	- To filter active Product GMV Max Campaigns within your ad account, use [/gmv_max/campaign/get/](45-gmv-max-p1.md#doc-1826463372290177) and set `filtering` to `{"gmv_max_promotion_types":["PRODUCT_GMV_MAX"], "primary_status":"STATUS_DELIVERY_OK"}`.
- Ensure that for the product associated with the video that you want to enable creative boost for, no max delivery session is currently set.
    - Để xác nhận điều này, hãy sử dụng [/campaign/gmv_max/session/list/](45-gmv-max-p1.md#doc-1835246996436162) và check the `spu_id` associated with any sessions where `bid_type` is `NO_BID`.
 - Ensure that creative boost is enabled for fewer than 100 videos. Within one Product GMV Max Campaign, you can enable creative boost for at most 100 videos.
    - Để xác nhận điều này, hãy sử dụng [/campaign/gmv_max/session/list/](45-gmv-max-p1.md#doc-1835246996436162) và check the number of sessions with `bid_type` as `CREATIVE_NO_BID` and a unique `item_id`.
- Ensure that the creative boost session you want to create for a video does not overlap with any existing creative boost sessions. At any given time, only one active creative boost session is allowed per video. 
    - Để xác nhận điều này, hãy sử dụng [/campaign/gmv_max/session/list/](45-gmv-max-p1.md#doc-1835246996436162) và check the `schedule_start_time` and `schedule_end_time` for sessions where `bid_type` is `CREATIVE_NO_BID`.
- Ensure that the video you want to enable creative boost for does not need authorization and is not excluded, rejected, or unavailable.
    - To confirm this, use [/gmv_max/report/get/](45-gmv-max-p2.md#doc-1824721673497601) and [retrieve the creative-level data](45-gmv-max-p3.md#doc-1824722485971009), including the metric `creative_delivery_status`. The `creative_delivery_status` of the video cannot be `AUTHORIZATION_NEEDED`, `EXCLUDED`, `REJECTED`, or `UNAVAILABLE`.
	
## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/campaign/gmv_max/session/create/

**Method** POST

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type  ****(Bắt buộc)**** | string | Định dạng dữ liệu yêu cầu. ⏎ Allowed format: `application/json`. |

**Parameters**

### Bảng tham số (Parameters) để tạo phiên tăng tốc phân phối tối đa
| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
| advertiser_id  ***(Bắt buộc)*** | string | ID tài khoản quảng cáo TikTok. |
| campaign_id  ***(Bắt buộc)*** | string | The ID of the Product GMV Max Campaign.<br><br><ul><li>To create a Product GMV Max Campaign and obtain the ID chiến dịch quảng cáo, use [/campaign/gmv_max/create/](45-gmv-max-p1.md#doc-1822000988713089) and set `shopping_ads_type` to `PRODUCT`.</li><li>To filter existing Product GMV Max Campaigns within your ad account, use [/gmv_max/campaign/get/](45-gmv-max-p1.md#doc-1826463372290177) and set `filtering` to `&#123;"gmv_max_promotion_types":["PRODUCT_GMV_MAX"]&#125;`.</li></ul>|
| store_id  ***(Bắt buộc)*** | string | ID của TikTok Shop.<br><br>To obtain the ID of the TikTok Shop that is associated with a GMV Max Campaign, use [/campaign/gmv_max/info/](45-gmv-max-p1.md#doc-1822000968821762). |
| session  ***(Bắt buộc)*** | object | Details about the max delivery mode for the campaign. |
#| bid_type{Required} | string | The session type.<br><br>Các giá trị enum hỗ trợ: <ul><li>`NO_BID`: max delivery session. Learn about <a href="#item-link-Prerequisites for creating a max delivery session">the prerequisites for creating a max delivery session</a>.</li></ul>Giá trị mặc định: `NO_BID`. <br><br><p><span style="color:darkred"><b>Note</b></span>: To create a creative boost session, see <a href="#item-link-Parameters for creating a creative boost session">Parameters for creating a creative boost session</a> and set `bid_type` to `CREATIVE_NO_BID`.</p> |
#| product_list {Required}  | object[] | Details about the specific products.<br><br>Kích thước tối đa: 1. |
##| spu_id {Required}  | string | The Product SPU (standard product unit) ID.<br><br>To obtain the list of SPU IDs for products within a TikTok Shop, use [/store/product/get/](69-tiktok-store.md#doc-1793482248880130) and set `ad_creation_eligible` to `GMV_MAX` and select `item_group_id` values where `status` is `AVAILABLE`. |
#| budget  {Required} | float | The daily max delivery budget.<br>Max delivery uses additional budget, separate from target ROI optimization budget, paced for more predictable ad spending. Your target ROI budget won’t be used for products using max delivery while max delivery is active.<br><br>Value range: ≥ 10 (USD). |
#| schedule_type | string | Schedule type for max delivery.<br><br>Các giá trị enum hỗ trợ: <ul><li>`SCHEDULE_FROM_NOW`: To enable the max delivery mode for the product continuously after the `schedule_start_time`, until the campaign scheduled end time.</li><li>`SCHEDULE_START_END`: To enable the max delivery mode for the product between the `schedule_start_time` and `schedule_end_time`.</li></ul><br>Giá trị mặc định: `SCHEDULE_FROM_NOW`. |
#| schedule_start_time | string | The start time for the max delivery mode, in the format of `YYYY-MM-DD HH:MM:SS` (UTC+0).<br><br>If not specified, this field will default to the current time.<br><br><p><span style="color:darkred"><b>Note</b></span>: <ul><li>The start time cannot be earlier than the current time.</li><li>The start time should be later than or equal to the campaign start time.</li><li>Your daily budget will be spent evenly throughout the day. If your max delivery duration is less than 24 hours in a given day, your full budget will still be spent.</li><li>Max delivery will be active between your set start and end times for your selected products. If your campaign is still active when max delivery ends, the optimization mode for those products will automatically change to target ROI.</li></ul> |
#| schedule_end_time  {+Conditional} | string | <ul><li>Bắt buộc khi `schedule_type` is `SCHEDULE_START_END`.</li><li> Not supported when `schedule_type` is `SCHEDULE_FROM_NOW`.</li></ul><br>The end time for the max delivery mode, in the format of `YYYY-MM-DD HH:MM:SS` (UTC+0).<br><br><p><span style="color:darkred"><b>Note</b></span>: <ul><li>The end time cannot be earlier than the current time.</li><li>The end time should be earlier or equal to the campaign end time.</li></ul> |

#### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/campaign/gmv_max/session/create/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id": "{{advertiser_id}}",
    "store_id": "{{store_id}}",
    "campaign_id": "{{campaign_id}}",
    "session":{
		"bid_type":"NO_BID",
        "product_list":[
            {
                "spu_id": "{{spu_id}}"
            }
        ],
        "budget": {{budget}},
        "schedule_start_time": "{{schedule_start_time}}"
    }
}'
```

### Bảng tham số (Parameters) để tạo phiên tăng tốc mẫu sáng tạo
| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
| advertiser_id  ***(Bắt buộc)*** | string | ID tài khoản quảng cáo TikTok. |
| campaign_id  ***(Bắt buộc)*** | string | The ID of the Product GMV Max Campaign.<br><br><ul><li>To create a Product GMV Max Campaign and obtain the ID chiến dịch quảng cáo, use [/campaign/gmv_max/create/](45-gmv-max-p1.md#doc-1822000988713089) and set `shopping_ads_type` to `PRODUCT`.</li><li>To filter existing Product GMV Max Campaigns within your ad account, use [/gmv_max/campaign/get/](45-gmv-max-p1.md#doc-1826463372290177) and set `filtering` to `&#123;"gmv_max_promotion_types":["PRODUCT_GMV_MAX"]&#125;`.</li></ul>|
| store_id  ***(Bắt buộc)*** | string | ID của TikTok Shop.<br><br>To obtain the ID of the TikTok Shop that is associated with a GMV Max Campaign, use [/campaign/gmv_max/info/](45-gmv-max-p1.md#doc-1822000968821762). |
| session  ***(Bắt buộc)*** | object | Details about the creative boost settings for the campaign. |
#| bid_type{Required} | string | Session type.<br><br>Các giá trị enum hỗ trợ: <ul><li>`CREATIVE_NO_BID`: creative boost session. Learn about <a href="#item-link-Prerequisites for creating a creative boost session">the prerequisites for creating a creative boost session</a>.</li></ul><br><p><span style="color:darkred"><b>Note</b></span>: To create a max delivery session, see <a href="#item-link-Parameters for creating a max delivery session">Parameters for creating a max delivery session</a> and set `bid_type` to `NO_BID` or leave `bid_type` unspecified.</p> |
#| product_list {Required}  | object[] | Details about the specific products.<br><br>Kích thước tối đa: 1. |
##| spu_id {Required}  | string | The Product SPU (standard product unit) ID.<br><br>To obtain the list of SPU IDs for products within a TikTok Shop, use [/store/product/get/](69-tiktok-store.md#doc-1793482248880130) and set `ad_creation_eligible` to `GMV_MAX` and select `item_group_id` values where `status` is `AVAILABLE`. |
#| item_id{Required} | string | The ID of the video to enable creative boost for.<br><br>To obtain the list of TikTok videos within an existing GMV Max Campaign, use [/gmv_max/report/get/](45-gmv-max-p2.md#doc-1824721673497601) and [retrieve the creative-level data](45-gmv-max-p3.md#doc-1824722485971009). You can get the TikTok video ID through the metric `item_id`. Ensure that the `creative_delivery_status` of the video is not `AUTHORIZATION_NEEDED`, `EXCLUDED`, `REJECTED`, or `UNAVAILABLE`. |
#| budget{Required} | float | The daily creative boost budget.<br>Creative boost utilizes budget, separate from campaign budget, paced throughout your schedule for more predictable ad spending.<br><br>Creative boost budget isn't included in calculations for your campaign's ROI protection. <br><br>Value range: ≥ 10 (USD). |
#| schedule_type{Required} | string | Schedule type for creative boost.<br><br>Các giá trị enum hỗ trợ: <ul><li>`SCHEDULE_FROM_NOW`: To enable creative boost for the product continuously after the current time, until the campaign scheduled end time.</li><li>`SCHEDULE_START_END`: To enable creative boost for the product between the current time and `schedule_end_time`.</li></ul>Giá trị mặc định: `SCHEDULE_FROM_NOW`. |
#| schedule_end_time{+Conditional} | string | <ul><li> Bắt buộc khi `schedule_type` is `SCHEDULE_START_END`.</li><li>Not supported when `schedule_type` is `SCHEDULE_FROM_NOW`.</li></ul><br>The end time for creative boost, in the format of `YYYY-MM-DD HH:MM:SS` (UTC+0).<br><br><p><span style="color:darkred"><b>Note</b></span>: <ul><li>The end time cannot be earlier than the current time.</li><li>The end time should be earlier or equal to the campaign end time.</li></ul></p> |

#### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/campaign/gmv_max/session/create/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id": "{{advertiser_id}}",
    "store_id": "{{store_id}}",
    "campaign_id": "{{campaign_id}}",
    "session":{
        "bid_type":"CREATIVE_NO_BID",
        "product_list":[
            {
                "spu_id": "{{spu_id}}"
            }
        ],
        "item_id":"{{item_id}}",
        "budget": {{budget}}
    }
}'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|code |number|Response code. For the complete list of response codes and descriptions, see [Appendix-Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message|string|Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|request_id |string|Mã log ID của một yêu cầu, dùng để định danh duy nhất yêu cầu đó.  |
|data |object|Returned data.|
#|session_id|string|The ID of the max delivery session for the product or of the creative boost session for the video in the Product GMV Max Campaign.|

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "session_id": "{{session_id}}"
    }
}
```

---

<a id="doc-1835247009119233"></a>
<!-- doc_id: 1835247009119233 -->
<!-- doc_id: 1835247009119233 -->
# Cập nhật phiên tăng tốc phân phối tối đa hoặc tăng tốc mẫu sáng tạo (Update a max delivery or creative boost session)
> Đường dẫn: API Reference > GMV Max > Update a max delivery or creative boost session
Sử dụng endpoint này để cập nhật a max delivery session for a specific product or a creative boost session for a specific video within a Product GMV Max Campaign.

>**Note:**  
> You cannot update max delivery or creative boost sessions that have ended.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/campaign/gmv_max/session/update/

**Method** POST

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type  ****(Bắt buộc)**** | string | Định dạng dữ liệu yêu cầu. ⏎ Allowed format: `application/json`. |

**Parameters**
### Bảng tham số (Parameters) để cập nhật phiên tăng tốc phân phối tối đa
| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
|advertiser_id***(Bắt buộc)***|string|ID tài khoản quảng cáo TikTok.|
| campaign_id  ***(Bắt buộc)*** | string | The ID of the Product GMV Max Campaign.<br><br><ul><li>To create a Product GMV Max Campaign and obtain the ID chiến dịch quảng cáo, use [/campaign/gmv_max/create/](45-gmv-max-p1.md#doc-1822000988713089) and set `shopping_ads_type` to `PRODUCT`.</li><li>To filter existing Product GMV Max Campaigns within your ad account, use [/gmv_max/campaign/get/](45-gmv-max-p1.md#doc-1826463372290177) and set `filtering` to `&#123;"gmv_max_promotion_types":["PRODUCT_GMV_MAX"]&#125;`.</li></ul>|
|store_id***(Bắt buộc)***|string|ID của TikTok Shop.<br><br>To obtain the ID of the TikTok Shop that is associated with a GMV Max Campaign, use [/campaign/gmv_max/info/](45-gmv-max-p1.md#doc-1822000968821762). |
|session_id***(Bắt buộc)***|string|The ID of the max delivery session for a product in the Product GMV Max Campaign.<br><br>To obtain the ID list of active max delivery sessions within a Product GMV Max Campaign, use [/campaign/gmv_max/session/list/](45-gmv-max-p1.md#doc-1835246996436162) and select sessions with `bid_type` as `NO_BID`.|
|session***(Bắt buộc)***|object|Details about the max delivery mode for the campaign.|
#|budget|float|The daily max delivery budget.<br>Max delivery uses additional budget, separate from target ROI optimization budget, paced for more predictable ad spending. Your target ROI budget won't be used for products using max delivery while max delivery is active.<br><br>Value range: ≥ 10 (USD).|
#|schedule_type|string|Schedule type for max delivery.<br><br>Các giá trị enum hỗ trợ: <ul><li>`SCHEDULE_FROM_NOW`: To enable the max delivery mode for the product continuously after the `schedule_start_time`, until the campaign scheduled end time.</li><li>`SCHEDULE_START_END`: To enable the max delivery mode for the product between the `schedule_start_time` and `schedule_end_time`.</li></ul>|
#|schedule_start_time|string|The start time for the max delivery mode, in the format of `YYYY-MM-DD HH:MM:SS` (UTC+0).<br><br><p><span style="color:darkred"><b>Note</b></span>:<ul><li>The start time cannot be earlier than the current time + 5 minutes.</li><li>The start time should be later than or equal to the campaign start time.</li><li>Your daily budget will be spent evenly throughout the day. If your max delivery duration is less than 24 hours in a given day, your full budget will still be spent.</li><li>Max delivery will be active between your set start and end times for your selected products. If your campaign is still active when max delivery ends, the optimization mode for those products will automatically change to target ROI.</li></ul>|
#|schedule_end_time {+Conditional}|string|<ul><li>Bắt buộc khi `schedule_type` is `SCHEDULE_START_END`.</li><li>Not supported when `schedule_type` is `SCHEDULE_FROM_NOW`.</li></ul><br>The end time for the max delivery mode, in the format of `YYYY-MM-DD HH:MM:SS` (UTC+0).<br><br><p><span style="color:darkred"><b>Note</b></span>:<ul><li>The end time cannot be earlier than the current time.</li><li>The end time should be earlier or equal to the campaign end time.</li></ul>|

#### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/campaign/gmv_max/session/update/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id": "{{advertiser_id}}",
    "store_id": "{{store_id}}",
    "campaign_id": "{{campaign_id}}",
    "session_id": "{{session_id}}",
    "session":
    {
        "schedule_start_time": "{{schedule_start_time}}"
    }
}'
```

### Bảng tham số (Parameters) để cập nhật phiên tăng tốc mẫu sáng tạo
| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
| advertiser_id  ***(Bắt buộc)*** | string | ID tài khoản quảng cáo TikTok. |
| campaign_id  ***(Bắt buộc)*** | string | The ID of the Product GMV Max Campaign.<br><br><ul><li>To create a Product GMV Max Campaign and obtain the ID chiến dịch quảng cáo, use [/campaign/gmv_max/create/](45-gmv-max-p1.md#doc-1822000988713089) and set `shopping_ads_type` to `PRODUCT`.</li><li>To filter existing Product GMV Max Campaigns within your ad account, use [/gmv_max/campaign/get/](45-gmv-max-p1.md#doc-1826463372290177) and set `filtering` to `&#123;"gmv_max_promotion_types":["PRODUCT_GMV_MAX"]&#125;`.</li></ul>|
| store_id  ***(Bắt buộc)*** | string | ID của TikTok Shop.<br><br>To obtain the ID of the TikTok Shop that is associated with a GMV Max Campaign, use [/campaign/gmv_max/info/](45-gmv-max-p1.md#doc-1822000968821762). |
|session_id***(Bắt buộc)***|string|The ID of the creative boost session for a video in the Product GMV Max Campaign.<br><br>To obtain the ID list of active creative boost sessions within a Product GMV Max Campaign, use [/campaign/gmv_max/session/list/](45-gmv-max-p1.md#doc-1835246996436162) and select sessions with `bid_type` as `CREATIVE_NO_BID`.|
| session  ***(Bắt buộc)*** | object | Details about the creative boost settings for the campaign. |
#| budget | float | The daily creative boost budget.<br>Creative boost utilizes budget, separate from campaign budget, paced throughout your schedule for more predictable ad spending.<br><br>Creative boost budget isn't included in calculations for your campaign's ROI protection. <br><br>Value range: ≥ 10 (USD). |
#| schedule_type| string | Schedule type for creative boost.<br><br>Các giá trị enum hỗ trợ: <ul><li>`SCHEDULE_FROM_NOW`: To enable creative boost for the product continuously after the current time, until the campaign scheduled end time.</li><li>`SCHEDULE_START_END`: To enable creative boost for the product between the current time and `schedule_end_time`.</li></ul>Giá trị mặc định: `SCHEDULE_FROM_NOW`. |
#| schedule_end_time{+Conditional} | string | <ul><li> Bắt buộc khi `schedule_type` is `SCHEDULE_START_END`.</li><li>Not supported when `schedule_type` is `SCHEDULE_FROM_NOW`.</li></ul><br>The end time for creative boost, in the format of `YYYY-MM-DD HH:MM:SS` (UTC+0).<br><br><p><span style="color:darkred"><b>Note</b></span>: <ul><li>The end time cannot be earlier than the current time.</li><li>The end time should be earlier or equal to the campaign end time.</li></ul></p> |

#### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/campaign/gmv_max/session/update/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id": "{{advertiser_id}}",
    "store_id": "{{store_id}}",
    "campaign_id": "{{campaign_id}}",
    "session_id": "{{session_id}}",
    "session":
    {
        "budget": {{budget}}
    }
}'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|code |number|Response code. For the complete list of response codes and descriptions, see [Appendix-Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message|string|Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|request_id |string|Mã log ID của một yêu cầu, dùng để định danh duy nhất yêu cầu đó.  |
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

<a id="doc-1835246996436162"></a>
<!-- doc_id: 1835246996436162 -->
<!-- doc_id: 1835246996436162 -->
# Lấy danh sách các phiên tăng tốc trong một chiến dịch (Get max delivery or creative boost sessions within a campaign)
> Đường dẫn: API Reference > GMV Max > Get max delivery or creative boost sessions within a campaign
Sử dụng endpoint này để truy xuất all active max delivery sessions for products or creative boost sessions for videos within a Product GMV Max Campaign.

Không thể truy cập các phiên đã kết thúc qua `/campaign/gmv_max/session/list/`. Để xem chi tiết các phiên đó, hãy dùng [/campaign/gmv_max/session/get/](45-gmv-max-p1.md#doc-1835247031331842).

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/campaign/gmv_max/session/list/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
| advertiser_id  ***(Bắt buộc)*** | string | ID tài khoản quảng cáo TikTok. |
| campaign_id  ***(Bắt buộc)*** | string | The ID of the Product GMV Max Campaign.<br><br><ul><li>To create a Product GMV Max Campaign and obtain the ID chiến dịch quảng cáo, use [/campaign/gmv_max/create/](45-gmv-max-p1.md#doc-1822000988713089) and set `shopping_ads_type` to `PRODUCT`.</li><li>To filter existing Product GMV Max Campaigns within your ad account, use [/gmv_max/campaign/get/](45-gmv-max-p1.md#doc-1826463372290177) and set `filtering` to `&#123;"gmv_max_promotion_types":["PRODUCT_GMV_MAX"]&#125;`.</li></ul>|

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/campaign/gmv_max/session/list/?advertiser_id={{advertiser_id}}&campaign_id={{campaign_id}}' \
--header 'Access-Token: {{Access-Token}}'
```
## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|code |number|Response code. For the complete list of response codes and descriptions, see [Appendix-Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message|string|Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|request_id |string|Mã log ID của một yêu cầu, dùng để định danh duy nhất yêu cầu đó.  |
|data |object|Returned data.|
#|session_list|object[]|The list of max delivery sessions for products or creative boost sessions for videos within the Product GMV Max Campaign.|
##|campaign_id|string|The ID of the Product GMV Max Campaign.|
##| bid_type|string|Session type.<br><br>Các giá trị enum hỗ trợ: <ul><li>`NO_BID`: max delivery session.</li><li>`CREATIVE_NO_BID`: creative boost session.</li></ul>|
##| session_id|string|The ID of the max delivery session for the product or creative boost session for the video in the Product GMV Max Campaign.<br><br><ul><li>When `bid_type` is `NO_BID`, this field represents the ID of a max delivery session.</li><li>When `bid_type` is `CREATIVE_NO_BID`, this field represents the ID of a creative boost session.</li></ul> |
##| budget|float|The daily max delivery budget or daily creative boost budget.<br><br><ul><li>Max delivery uses additional budget, separate from target ROI optimization budget, paced for more predictable ad spending. Your target ROI budget won’t be used for products using max delivery while max delivery is active.</li><li>Creative Boost is a functionality within Product GMV Max that allows sellers to manually promote specific videos by allocating extra daily budget.</li></ul> |
##|product_list|object[]|Details about the specific products.|
###|spu_id|string|The Product SPU (standard product unit) ID.|
##|schedule_type|string|Schedule type for max delivery or creative boost.<br><br>Các giá trị enum hỗ trợ: <br><ul><li>`SCHEDULE_FROM_NOW`: To enable the max delivery or creative boost mode for the product continuously after the `schedule_start_time`, until the campaign scheduled end time.</li><li>`SCHEDULE_START_END`: To enable the max delivery or creative boost mode for the product between the `schedule_start_time` and `schedule_end_time`.</li></ul>|
##|schedule_start_time|string|The start time for the max delivery or creative boost mode, in the format of `YYYY-MM-DD HH:MM:SS` (UTC+0).|
##|schedule_end_time|string|The end time for the max delivery or creative boost mode, in the format of `YYYY-MM-DD HH:MM:SS` (UTC+0).|

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "session_list": [
            {
                "bid_type": "NO_BID",
                "budget": {{budget}},
                "campaign_id": "{{campaign_id}}",
                "product_list": [
                    {
                        "spu_id": "{{spu_id}}"
                    }
                ],
                "schedule_end_time": "{{schedule_end_time}}",
                "schedule_start_time": "{{schedule_start_time}}",
                "schedule_type": "SCHEDULE_FROM_NOW",
                "session_id": "{{session_id}}"
            }
        ]
    }
}
```

---

<a id="doc-1835247031331842"></a>
<!-- doc_id: 1835247031331842 -->
<!-- doc_id: 1835247031331842 -->
# Lấy thông tin chi tiết các phiên tăng tốc (Get details of max delivery or creative boost sessions)
> Đường dẫn: API Reference > GMV Max > Get details of max delivery or creative boost sessions
Sử dụng endpoint này để truy xuất the details of max delivery or creative boost sessions for a list of given session IDs.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/campaign/gmv_max/session/get/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
|advertiser_id***(Bắt buộc)***|string|ID tài khoản quảng cáo TikTok.|
|session_ids***(Bắt buộc)***|string[]|An ID list of the max delivery or creative boost sessions for products in a Product GMV Max Campaign.<br><br>Kích thước tối đa: 20.<br><br><ul><li>To obtain the ID list of active max delivery sessions within a Product GMV Max Campaign, use [/campaign/gmv_max/session/list/](45-gmv-max-p1.md#doc-1835246996436162) and select sessions with `bid_type` as `NO_BID`.</li><li>To obtain the ID list of active creative boost sessions within a Product GMV Max Campaign, use [/campaign/gmv_max/session/list/](45-gmv-max-p1.md#doc-1835246996436162) and select sessions with `bid_type` as `CREATIVE_NO_BID`.</li></ul>|

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/campaign/gmv_max/session/get/?advertiser_id={{advertiser_id}}&session_ids=["{{session_id}}"]' \
--header 'Access-Token: {{Access-Token}}'
```
## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|code |number|Response code. For the complete list of response codes and descriptions, see [Appendix-Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message|string|Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|request_id |string|Mã log ID của một yêu cầu, dùng để định danh duy nhất yêu cầu đó.  |
|data |object|Returned data.|
#|session_list|object[]|The list of max delivery or creative boost sessions.|
##|campaign_id|string|The ID of the Product GMV Max Campaign.|
##| bid_type|string|Session type.<br><br>Các giá trị enum hỗ trợ: <ul><li>`NO_BID`: max delivery session.</li><li>`CREATIVE_NO_BID`: creative boost session.</li></ul>|
##| session_id|string|The ID of the max delivery session for the product or creative boost session for the video in the Product GMV Max Campaign.<br><br><ul><li>When `bid_type` is `NO_BID`, this field represents the ID of a max delivery session.</li><li>When `bid_type` is `CREATIVE_NO_BID`, this field represents the ID of a creative boost session.</li></ul> |
##| budget|float|The daily max delivery budget or daily creative boost budget.<br><br><ul><li>Max delivery uses additional budget, separate from target ROI optimization budget, paced for more predictable ad spending. Your target ROI budget won’t be used for products using max delivery while max delivery is active.</li><li>Creative Boost is a functionality within Product GMV Max that allows sellers to manually promote specific videos by allocating extra daily budget.</li></ul> |
##|product_list|object[]|Details about the specific products.|
###|spu_id|string|The Product SPU (standard product unit) ID.|
##|schedule_type|string|Schedule type for max delivery or creative boost.<br><br>Các giá trị enum hỗ trợ: <br><ul><li>`SCHEDULE_FROM_NOW`: To enable the max delivery or creative boost mode for the product continuously after the `schedule_start_time`, until the campaign scheduled end time.</li><li>`SCHEDULE_START_END`: To enable the max delivery or creative boost mode for the product between the `schedule_start_time` and `schedule_end_time`.</li></ul>|
##|schedule_start_time|string|The start time for the max delivery or creative boost mode, in the format of `YYYY-MM-DD HH:MM:SS` (UTC+0).|
##|schedule_end_time|string|The end time for the max delivery or creative boost mode, in the format of `YYYY-MM-DD HH:MM:SS` (UTC+0).|
##|item_id|string|Returned only when `bid_type` is `CREATIVE_NO_BID`.<br><br>The ID of the video for which creative boost is enabled.|

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "session_list": [
            {
                "bid_type": "NO_BID",
                "budget": {{budget}},
                "campaign_id": "{{campaign_id}}",
                "product_list": [
                    {
                        "spu_id": "{{spu_id}}"
                    }
                ],
                "schedule_start_time": "{{schedule_start_time}}",
                "schedule_type": "SCHEDULE_FROM_NOW",
                "session_id": "{{session_id}}"
            }
        ]
    }
}
```

---

<a id="doc-1835246983475217"></a>
<!-- doc_id: 1835246983475217 -->
<!-- doc_id: 1835246983475217 -->
# Xóa một phiên tăng tốc (Delete a max delivery or creative boost session)
> Đường dẫn: API Reference > GMV Max > Delete a max delivery or creative boost session
Sử dụng endpoint này để xóa a max delivery session for a specific product or a creative boost session for a specific video in an active Product GMV Max Campaign.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/campaign/gmv_max/session/delete/

**Method** POST

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type  ****(Bắt buộc)**** | string | Định dạng dữ liệu yêu cầu. ⏎ Allowed format: `application/json`. |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
| advertiser_id ***(Bắt buộc)*** | string | ID tài khoản quảng cáo TikTok. |
|session_id ***(Bắt buộc)***|string|The ID of the max delivery session for a product or creative boost session for a video in the Product GMV Max Campaign.<br><br><ul><li>To obtain the ID list of active max delivery sessions within a Product GMV Max Campaign, use [/campaign/gmv_max/session/list/](45-gmv-max-p1.md#doc-1835246996436162) and select sessions with `bid_type` as `NO_BID`.</li><li>To obtain the ID list of active creative boost sessions within a Product GMV Max Campaign, use [/campaign/gmv_max/session/list/](45-gmv-max-p1.md#doc-1835246996436162) and select sessions with `bid_type` as `CREATIVE_NO_BID`.</li></ul>|

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/campaign/gmv_max/session/delete/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id": "{{advertiser_id}}",
    "session_id": "{{session_id}}"
}'
```
## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|code |number|Response code. For the complete list of response codes and descriptions, see [Appendix-Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message|string|Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|request_id |string|Mã log ID của một yêu cầu, dùng để định danh duy nhất yêu cầu đó.  |
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

## Hướng dẫn thực hành Data Retrieval (Python & cURL)

Dưới đây là mã nguồn mẫu minh họa quy trình gọi API thực tế cho phân hệ **GMV Max — phần 1/3**:

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

