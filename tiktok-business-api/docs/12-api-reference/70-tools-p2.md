# Công cụ tra cứu (Tools) — phần 2/3

> Phân hệ: apiref:Tools.
> Tài liệu biên dịch kỹ thuật chi tiết theo chuẩn TikTok Business API v1.3.

---

## Mục lục điều hướng
- [1. Lấy danh sách nhà cung cấp dịch vụ Internet (Get internet service providers) (#doc-1762962378261506)](#doc-1762962378261506)
- [2. Lấy các thẻ ngữ cảnh khả dụng (#doc-1747747118654465)](#doc-1747747118654465)
- [3. Lấy thông tin chi tiết thẻ ngữ cảnh (#doc-1747747180830722)](#doc-1747747180830722)
- [4. Lấy danh mục loại trừ nội dung khả dụng (#doc-1769738074686465)](#doc-1769738074686465)
- [5. Lấy thông tin chi tiết danh mục loại trừ nội dung (#doc-1769738105333826)](#doc-1769738105333826)
- [6. (Sắp ngừng hoạt động) Lấy ngân sách đề xuất ((To-be-deprecated) Get recommended budgets) (#doc-1746463695763458)](#doc-1746463695763458)
- [7. (Sắp ngừng hoạt động) Lấy giá thầu đề xuất ((To-be-deprecated) Get recommended bids) (#doc-1746463732779009)](#doc-1746463732779009)
- [8. Lấy giá thầu gợi ý (Get a suggested bid) (#doc-1737107845597186)](#doc-1737107845597186)
- [9. Kiểm tra tính hợp lệ tối ưu hóa dựa trên giá trị (Check Value-Based Optimization eligibility) (#doc-1770016073586753)](#doc-1770016073586753)
- [10. Lấy trạng thái ủy quyền của đối tác Brand Safety (Get the authorization status of a Brand Safety partner) (#doc-1738456743621634)](#doc-1738456743621634)
- [11. (Đã lỗi thời) Lấy đối tác đo lường bên thứ ba post-bid khả dụng ((Deprecated) Get available post-bid third-party measurement partners) (#doc-1755436556897281)](#doc-1755436556897281)
- [12. Lấy kết quả xác minh URL (Get the verification results of a URL) (#doc-1774487686007810)](#doc-1774487686007810)
- [13. Lấy mã vùng quay số và mã quốc gia cho số điện thoại (Get region calling codes and region codes for phone numbers) (#doc-1774488637039618)](#doc-1774488637039618)
- [14. Lấy danh sách múi giờ (Get time zones) (#doc-1738455961470977)](#doc-1738455961470977)
- [15. Lấy liên kết trong ứng dụng TikTok (Get a TikTok in-app link) (#doc-1738457335681026)](#doc-1738457335681026)
- [16. Lấy nhãn chiến dịch của tài khoản quảng cáo (Get the campaign labels of an ad account) (#doc-1851286489283585)](#doc-1851286489283585)
- [17. Lấy danh sách TikTok Minis trong tài khoản quảng cáo (Get the TikTok Minis within an ad account) (#doc-1853450329535490)](#doc-1853450329535490)
- [18. Lấy danh sách TikTok Series khả dụng trong tài khoản quảng cáo (Get the available TikTok Series within an ad account) (#doc-1863332009162754)](#doc-1863332009162754)
- [19. Lấy nguồn phân bổ và nguồn dữ liệu khả dụng cho ứng dụng (Get available attribution sources and data sources for an app) (#doc-1870952425111618)](#doc-1870952425111618)
- [20. Lấy trạng thái bảo vệ giá thầu (Get bid protection statuses) (#doc-1874392512912449)](#doc-1874392512912449)

---

<a id="doc-1762962378261506"></a>
<!-- doc_id: 1762962378261506 -->
<!-- doc_id: 1762962378261506 -->
# Lấy danh sách nhà cung cấp dịch vụ Internet (Get internet service providers)
> Đường dẫn: API Reference > Tools > Get internet service providers
Sử dụng endpoint này để lấy thông tin các thẻ nhắm mục tiêu (targeting tags). 

Bạn có thể lấy một loại thẻ nhắm mục tiêu duy nhất dùng để nhắm đối tượng mục tiêu quảng cáo: mã ISP ID. Sau đó, để áp dụng ISP ID cho quảng cáo, bạn có thể truyền các ISP ID nhận được vào trường `isp_ids` khi gọi [/adgroup/create/](07-ad-groups-p2.md#doc-1739499616346114), [/adgroup/update/](07-ad-groups-p3.md#doc-1739586761631745) hoặc [/ad/audience_size/estimate/](07-ad-groups-p1.md#doc-1740302379236353).

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/tool/targeting/list/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type  ****(Bắt buộc)**** | string | Định dạng dữ liệu yêu cầu. ⏎ Định dạng cho phép: `application/json`. |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
| advertiser_id***(Bắt buộc)*** | string | ID tài khoản quảng cáo TikTok. |
| location_ids ***(Bắt buộc)*** | string[] | ID của các vị trí mà bạn muốn lấy ID `ISP` được hỗ trợ. <br>Kích thước tối đa: 1000. <br>To find out the list of location IDs, see **Location IDs**.<br><p><span style="color:darkred"><b>Note</b></span>: You need to pass location IDs at the country or region level. To get the available locations and corresponding IDs based on your placement and objective, use the [/tool/region/](70-tools-p1.md#doc-1737189539571713) and the returned `level` for location IDs at the country or region level will be `COUNTRY`. |
| scene ***(Bắt buộc)*** | string | Loại nhắm mục tiêu mà các thẻ nhắm mục tiêu được sử dụng. <br>The allowed Các giá trị enum hỗ trợ: `ISP` ( Internet Service Provider targeting). |
### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location "https://business-api.tiktok.com/open_api/v1.3/tool/targeting/list/?advertiser_id={{advertiser_id}}&location_ids=["357994"]&scene=ISP" 
--header "Access-Token: {{Access-Token}}" 
--header "Content-Type: application/json"
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|-|-|-|
|code |number|Response code. For the complete list of response codes and descriptions, see [Appendix-Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message|string|Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|request_id |string|Mã nhật ký yêu cầu (request log ID) để định danh duy nhất cho mỗi lượt gọi API.  |
|data |object|Returned data.|
#|targeting_tag_list| object[] | Information about the targeting tags. |
##|targeting_type| string | The targeting type that the targeting tag is used for. <br>Các giá trị enum hỗ trợ: `ISP` ( Internet Service Provider targeting). |
##| name | string | The name of the targeting tag. |
##| status_info | object | Information about the status of the targeting tag. |
###| status | string | The status of the targeting tag. <br>Các giá trị enum hỗ trợ: `ENABLED` (can be used for targeting), `DISABLED`(cannot be used for targeting). |
###| reason | string | The reason why the targeting tag cannot be used for targeting. <br>Returned when `status` = `DISABLED`. <br>Các giá trị enum hỗ trợ: <ul><li>`OFFLINE`: The targeting tag is offline. </li><li>`NOT_SUPPORTED`: The targeting tag is not offline but is not supported for the specified settings. </li></ul>|
##| isp | object | Information about the targeting tag that is used for Internet service provider targeting. |
###| isp_id | string | The ID of the Internet service provider that you can target. |
###| location_id | string | The location ID that the `isp_id` can be used together with. <br>Only location IDs at the country or region level are supported. |
###| region_code | string | The code of the region or country that the `isp_id` belongs to. |
##| geo | object | Information about the targeting tag that is used for location targeting. |
#| parent_tags | object[] | Information about all the parent targeting tags. |
### Ví dụ lệnh cURL (Example)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "parent_tags": [],
        "targeting_tag_list": [
            {
                "name": "Etisalat Misr",
                "targeting_type": "ISP",
                "geo": null,
                "status_info": {
                    "status": "ENABLED",
                    "reason": null
                },
                "isp": {
                    "isp_id": "EG00045",
                    "location_id": "357994",
                    "region_code": "EG"
                }
            },
            {
                "name": "Orange Egypt",
                "targeting_type": "ISP",
                "geo": null,
                "status_info": {
                    "status": "ENABLED",
                    "reason": null
                },
                "isp": {
                    "isp_id": "EG00081",
                    "location_id": "357994",
                    "region_code": "EG"
                }
            },
            {
                "name": "Telecom Egypt",
                "targeting_type": "ISP",
                "geo": null,
                "status_info": {
                    "status": "ENABLED",
                    "reason": null
                },
                "isp": {
                    "isp_id": "EG00098",
                    "location_id": "357994",
                    "region_code": "EG"
                }
            },
            {
                "name": "Vodafone Egypt",
                "targeting_type": "ISP",
                "geo": null,
                "status_info": {
                    "status": "ENABLED",
                    "reason": null
                },
                "isp": {
                    "isp_id": "EG00105",
                    "location_id": "357994",
                    "region_code": "EG"
                }
            },
            {
                "name": "other",
                "targeting_type": "ISP",
                "geo": null,
                "status_info": {
                    "status": "ENABLED",
                    "reason": null
                },
                "isp": {
                    "isp_id": "EG0",
                    "location_id": "357994",
                    "region_code": "EG"
                }
            }
        ]
    }
}
```

---

<a id="doc-1747747118654465"></a>
<!-- doc_id: 1747747118654465 -->
<!-- doc_id: 1747747118654465 -->
# Lấy các thẻ ngữ cảnh khả dụng (Get available contextual tags)
> Đường dẫn: API Reference > Tools > Get available contextual tags
Sử dụng endpoint này để lấy thông tin các thẻ ngữ cảnh (contextual tags) mà bạn có thể nhắm mục tiêu. Bạn cần chỉ định ID tài khoản quảng cáo TikTok, mục tiêu quảng cáo và mã khu vực trong truy vấn để nhận các thẻ khả dụng.

Xem [tại đây](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1745292519923713) để tìm hiểu cách sử dụng nhắm mục tiêu theo ngữ cảnh. 
>**Note:**  Contextual targeting is currently an allowlist-only feature. If you would like to access it, please contact your TikTok representative.

## Yêu cầu gọi API (Request)

**Endpoint**  https://business-api.tiktok.com/open_api/v1.3/tool/contextual_tag/get/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
| advertiser_id {required} | string | ID tài khoản quảng cáo TikTok. |
| objective_type {required} | string | Mục tiêu quảng cáo. <br><br>Only supports `REACH`, `VIDEO_VIEWS`, `RF_REACH`. |
| region_codes | string[] | Country or region codes. |
| brand_safety_type | string | Loại an toàn thương hiệu (Brand safety type). <br><br>Giá trị mặc định: `STANDARD_INVENTORY`. <br><br>Các giá trị enum hỗ trợ: <ul><li>`EXPANDED_INVENTORY`: Use TikTok's brand safety solution. Expanded inventory means that your ads will appear next to content where most inappropriate content has been removed, and may contain some mature themes. In the next API version, `EXPANDED_INVENTORY` will replace `NO_BRAND_SAFETY` and will be the default brand safety option.</li><li>`STANDARD_INVENTORY`: Use TikTok's brand safety solution. Standard inventory means that ads will appear next to content that is appropriate for most brands. </li><li>`LIMITED_INVENTORY`: Use TikTok's brand safety solution. Limited inventory means that your ads will not appear next to content that contains mature themes.</li></ul> <br><p><span style="color:darkred"><b>Note</b></span>: <ul><li> Pre-bid first-party Brand Safety solutions for `APP_PROMOTION`,  `WEB_CONVERSIONS`, `TRAFFIC`, `LEAD_GENERATION` objectives in Auction ads, and pre-bid third-party brand safety solutions are currently allowlist-only features. If you would like to access them, please contact your TikTok representative. </li><li> See [Brand safety](../09-marketing-api/quan-ly-chien-dich-tom-tat.md#doc-1739381752981505) to learn about the supported advertising objectives for pre-bid Brand Safety filtering. </li></ul>|
| rf_campaign_type | string | Loại chiến dịch. <br><br>Các giá trị enum hỗ trợ: `STANDARD`(Reach & Frequency campaign), `PULSE`(TikTok Pulse campaign).  <br><br><p><span style="color:darkred"><b>Note</b></span>: <ul><li>When `objective_type` is specified as `RF_REACH`, use this field to set the campaign as a TikTok Pulse campaign, then you can get available premium contextual tags. </li><li>Do not pass in this field when `objective_type` is not specified as `RF_REACH`.</li></ul>|

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/tool/contextual_tag/get/?advertiser_id={{advertiser_id}}&objective_type=RF_REACH&rf_campaign_type=PULSE' \
--header 'Access-Token: {{Access-Token}}'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|-|-|-|
|code |number|Response code. For the complete list of response codes and descriptions, see [Appendix-Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message|string|Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|request_id |string|Mã nhật ký yêu cầu (request log ID) để định danh duy nhất cho mỗi lượt gọi API.  |
|data |object|Returned data.|
#| contextual_tag_list | object[] | Contextual tag list. <br><p><span style="color:darkred"><b>Note</b></span>: Contextual targeting is currently an allowlist-only feature. The returned value will be empty(`[]`) if you don't apply for the allowlisting. |
##| contextual_tag_id | string | Contextual tag ID. <br><p><span style="color:darkred"><b>Note</b></span>: Currently contextual tags can only be used together with audience targeting settings that target the following countries: <ul><li>General tags: `US` (the United States), `CA` (Canada), `GB` (the United Kingdom), `DE` (Germany), `FR` (France), `IT` (Italy) , `ES` (Spain), `JP` (Japan), `KR` (South Korea), `AU` (Australia)，`BR` (Brazil), `MX`(Mexico).</li><li>Premium tags: `US` (the United States), `CA` (Canada), `GB` (the United Kingdom), `DE` (Germany), `FR` (France), `IT` (Italy) , `ES` (Spain), `JP` (Japan), `KR` (South Korea), `AU` (Australia)，`BR` (Brazil), `MX`(Mexico).</li></ul> |
##| name | string | Contextual tag name. |
##| type | string | Contextual tag category. Các giá trị enum hỗ trợ: `GENERAL` (general category), `PREMIUM`(premium category). |
##| content_lineup_type | string | Content lineup type.<br><br>Các giá trị enum hỗ trợ: <ul><li>`MAX_PULSE`: Max Pulse. Your ads will show next to top content from any topics on TikTok.</li><li>`CUSTOM` : Your ads will show next to one of the custom lineups you've previously created.</li><li>`CATEGORY`: Category lineups. Your ads will show next to top content from the categories you select.</li><li>`SEASONAL`: Seasonal lineups. Your ads will show next to top content from a seasonal event you select. </li></ul><br><p><span style="color:darkred"><b>Note</b></span>: Currently, you can run Max Pulse targeting `AE` (United Arab Emirates), `AU` (Australia), `BR` (Brazil), `CA` (Canada), `DE` (Germany), `ES` (Spain), `FR` (France), `GB` (United Kingdom), `IT` (Italy), `MX` (Mexico), `SA` (Saudi Arabia), `TR` (Turkey), and `US` (United States), and Category Lineups targeting `US`(the United States), `CA`(Canada), `BR`(Brazil), `AU`(Australia), `GB`(the United Kingdom), `FR`(France), `IT`(Italy), `ES`(Spain), `DE`(Germany). Both features are allowlist only. If you want to use them in the above markets, please contact your TikTok representative. |
##| status | string | Contextual tag status. <br><br>Các giá trị enum hỗ trợ: `ONLINE`, `OFFLINE`.<br><br> Only `ONLINE` tags can be used to create ads. |
##| description | string | Contextual tag description. |
##| objective_types | string[] | The advertising objectives that the contextual tag supports. |
##| region_codes | string[] | The country or region codes that the contextual tag supports. |

### Ví dụ lệnh cURL (Example)
```http
// curl
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "contextual_tag_list": [
            {
                "content_lineup_type": "CATEGORY",
                "contextual_tag_id": "{{contextual_tag_id}}",
                "description": "{{description}}",
                "name": "{{name}}",
                "objective_types": [
                    "RF_REACH"
                ],
                "region_codes": [
                    "US",
                    "CA",
                    "BR",
                    "MX",
                    "GB",
                    "DE",
                    "FR",
                    "IT",
                    "ES",
                    "AU",
                    "JP",
                    "ID",
                    "TH",
                    "SA",
                    "AE",
                    "TR",
                    "NL",
                    "PL",
                    "SE",
                    "VN",
                    "MY",
                    "PH",
                    "CO",
                    "AR",
                    "ZA",
                    "EG",
                    "PE",
                    "CL"
                ],
                "status": "ONLINE",
                "type": "PREMIUM"
            },
            {
                "content_lineup_type": "CATEGORY",
                "contextual_tag_id": "{{contextual_tag_id}}",
                "description": "{{description}}",
                "name": "{{name}}",
                "objective_types": [
                    "RF_REACH"
                ],
                "region_codes": [
                    "US",
                    "CA",
                    "BR",
                    "GB",
                    "DE",
                    "FR",
                    "IT",
                    "ES",
                    "AU"
                ],
                "status": "ONLINE",
                "type": "PREMIUM"
            }
        ]
    }
}
```

---

<a id="doc-1747747180830722"></a>
<!-- doc_id: 1747747180830722 -->
<!-- doc_id: 1747747180830722 -->
# Lấy thông tin chi tiết thẻ ngữ cảnh (Get details of contextual tags)
> Đường dẫn: API Reference > Tools > Get details of contextual tags
Sử dụng endpoint này để lấy thông tin the detailed information of contextual tags. In your query, you need to specify the ID tài khoản quảng cáo TikTok and contextual tag ID that you get from the response of [/tool/contextual_tag/get/](70-tools-p2.md#doc-1747747118654465).

Xem [tại đây](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1745292519923713) để tìm hiểu cách sử dụng nhắm mục tiêu theo ngữ cảnh. 
>**Note:**  Contextual targeting is currently an allowlist-only feature. If you would like to access it, please contact your TikTok representative.

## Yêu cầu gọi API (Request)

**Endpoint**  https://business-api.tiktok.com/open_api/v1.3/tool/contextual_tag/info/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
| advertiser_id {required} | string | ID tài khoản quảng cáo TikTok. |
| contextual_tag_ids {required} | string[] | Contextual tag IDs.|

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/tool/contextual_tag/info/?advertiser_id={{advertiser_id}}&contextual_tag_ids=["53","82","51"]' \
--header 'Access-Token: {{Access-Token}}'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|-|-|-|
|code |number|Response code. For the complete list of response codes and descriptions, see [Appendix-Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message|string|Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|request_id |string|Mã nhật ký yêu cầu (request log ID) để định danh duy nhất cho mỗi lượt gọi API.  |
|data |object|Returned data.|
#| contextual_tag_list | object[] | Contextual tag list. <br><p><span style="color:darkred"><b>Note</b></span>: Contextual targeting is currently an allowlist-only feature. The returned value will be empty(`[]`) if you don't apply for the allowlisting. |
##| contextual_tag_id | string | Contextual tag ID. <br><p><span style="color:darkred"><b>Note</b></span>: Currently contextual tags can only be used together with audience targeting settings that target the following countries: <ul><li>General tags: `US` (the United States), `CA` (Canada), `GB` (the United Kingdom), `DE` (Germany), `FR` (France), `IT` (Italy) , `ES` (Spain), `JP` (Japan), `KR` (South Korea), `AU` (Australia)，`BR` (Brazil), `MX`(Mexico).</li><li>Premium tags: `US` (the United States), `CA` (Canada), `GB` (the United Kingdom), `DE` (Germany), `FR` (France), `IT` (Italy) , `ES` (Spain), `JP` (Japan), `KR` (South Korea), `AU` (Australia)，`BR` (Brazil), `MX`(Mexico).</li></ul> |
##| name | string | Contextual tag name. |
##| type | string | Contextual tag category. Các giá trị enum hỗ trợ: `GENERAL` (general category), `PREMIUM`(premium category). |
##| content_lineup_type | string | Content lineup type.<br><br>Các giá trị enum hỗ trợ: <ul><li>`MAX_PULSE`: Max Pulse. Your ads will show next to top content from any topics on TikTok.</li><li>`CUSTOM` : Your ads will show next to one of the custom lineups you've previously created.</li><li>`CATEGORY`: Category lineups. Your ads will show next to top content from the categories you select.</li><li>`SEASONAL`: Seasonal lineups. Your ads will show next to top content from a seasonal event you select. </li></ul><br><p><span style="color:darkred"><b>Note</b></span>: Currently, you can run Max Pulse targeting `AE` (United Arab Emirates), `AU` (Australia), `BR` (Brazil), `CA` (Canada), `DE` (Germany), `ES` (Spain), `FR` (France), `GB` (United Kingdom), `IT` (Italy), `MX` (Mexico), `SA` (Saudi Arabia), `TR` (Turkey), and `US` (United States), and Category Lineups targeting `US`(the United States), `CA`(Canada), `BR`(Brazil), `AU`(Australia), `GB`(the United Kingdom), `FR`(France), `IT`(Italy), `ES`(Spain), `DE`(Germany). Both features are allowlist only. If you want to use them in the above markets, please contact your TikTok representative. |
##| status | string | Contextual tag status. Enum: `ONLINE`, `OFFLINE`. Only `ONLINE` tags can be used to create ads. |
##| description | string | Contextual tag description. |
##| objective_types | string[] | The advertising objectives that the contextual tag supports. |
##| region_codes | string[] | The country or region codes that the contextual tag supports. |

### Ví dụ lệnh cURL (Example)
```http
// curl
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "contextual_tag_list": [
            {
                "content_lineup_type": "CATEGORY",
                "contextual_tag_id": "53",
                "description": "{{description}}",
                "name": "{{name}}",
                "objective_types": [
                    "RF_REACH"
                ],
                "region_codes": [
                    "US",
                    "CA",
                    "MX",
                    "BR",
                    "GB",
                    "DE",
                    "FR",
                    "IT",
                    "ES",
                    "AU",
                    "JP",
                    "ID",
                    "TH",
                    "SA",
                    "AE",
                    "NL",
                    "TR",
                    "PL",
                    "SE",
                    "VN",
                    "MY",
                    "PH",
                    "ZA"
                ],
                "status": "ONLINE",
                "type": "PREMIUM"
            },
            {
                "content_lineup_type": "SEASONAL",
                "contextual_tag_id": "82",
                "description": "{{description}}",
                "name": "{{name}}",
                "objective_types": [
                    "RF_REACH"
                ],
                "region_codes": [
                    "US",
                    "CA",
                    "BR",
                    "MX",
                    "GB",
                    "DE",
                    "FR",
                    "IT",
                    "ES",
                    "ID",
                    "SA",
                    "AE",
                    "TR",
                    "TH",
                    "NL",
                    "PL",
                    "SE",
                    "VN",
                    "MY",
                    "PH",
                    "CO",
                    "AR",
                    "ZA"
                ],
                "status": "ONLINE",
                "type": "PREMIUM"
            },
            {
                "content_lineup_type": "MAX_PULSE",
                "contextual_tag_id": "51",
                "description": "{{description}}",
                "name": "{{name}}",
                "objective_types": [
                    "RF_REACH"
                ],
                "region_codes": [
                    "US",
                    "CA",
                    "BR",
                    "MX",
                    "GB",
                    "DE",
                    "FR",
                    "IT",
                    "ES",
                    "AU",
                    "JP",
                    "ID",
                    "TH",
                    "SA",
                    "AE",
                    "TR",
                    "NL",
                    "PL",
                    "SE",
                    "VN",
                    "MY",
                    "PH",
                    "CO",
                    "AR",
                    "ZA",
                    "EG",
                    "PE",
                    "CL"
                ],
                "status": "ONLINE",
                "type": "PREMIUM"
            }
        ]
    }
}
```

---

<a id="doc-1769738074686465"></a>
<!-- doc_id: 1769738074686465 -->
<!-- doc_id: 1769738074686465 -->
# Lấy danh mục loại trừ nội dung khả dụng (Get available content exclusion categories)
> Đường dẫn: API Reference > Tools > Get available content exclusion categories
Sử dụng endpoint này để lấy thông tin **content categories** or **vertical sensitivity categories** that can be excluded from appearing next to your ads.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/tool/content_exclusion/get/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id  ****(Bắt buộc)**** | string | ID tài khoản quảng cáo TikTok. |
| objective_type  ****(Bắt buộc)**** | string | Mục tiêu quảng cáo. Chỉ hỗ trợ `REACH`, `VIDEO_VIEWS` và `ENGAGEMENT`. |
| brand_safety_type | string | Loại an toàn thương hiệu (Brand safety type). Giá trị mặc định: `NO_BRAND_SAFETY`. Các giá trị enum hỗ trợ: • `NO_BRAND_SAFETY`: To not use any brand safety solution. Full inventory, which means your ads may appear next to some content featuring mature themes. • `EXPANDED_INVENTORY`: Use TikTok's brand safety solution. Expanded inventory means that your ads will appear next to content where most inappropriate content has been removed, and that does not contain mature themes. In the next API version, `EXPANDED_INVENTORY` will replace `NO_BRAND_SAFETY` and will be the default brand safety option. ⏎ **Note**:`EXPANDED_INVENTORY` is currently an allowlist-only feature. If you would like to access it, please contact your TikTok representative. • `STANDARD_INVENTORY`: Use TikTok's brand safety solution. Standard inventory means that ads will appear next to content that is appropriate for most brands. • `LIMITED_INVENTORY`: Use TikTok's brand safety solution. Limited inventory means that your ads will not appear next to content that contains mature themes. ⏎ **Note**:  • If you want to retrieve vertical sensitivity category IDs(`vertical_sensitivity_list`), you can only use `STANDARD_INVENTORY` or `LIMITED_INVENTORY`. • If you are not on the allowlist for vertical sensitivity, the `vertical_sensitivity_list` will be null in the response. |

### Ví dụ lệnh cURL (Example)

``` xcodeblock
(code curl http)
curl --location 'https://business-api.tiktok.com/open_api/v1.3/tool/content_exclusion/get/?advertiser_id={{advertiser_id}}&objective_type=VIDEO_VIEWS' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
(/code)
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Response code. For the complete list of error codes and descriptions, see [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | Mã nhật ký yêu cầu (request log ID) để định danh duy nhất cho mỗi lượt gọi API. |
| data | object | Returned data. |
| ↳ excluded_category_list | object[] | Danh sách các danh mục loại trừ nội dung. |
| ↳↳ category_id | string | Category ID. |
| ↳↳ category_name | string | Category name. |
| ↳↳ supported_regions | string[] | Mã quốc gia hoặc khu vực mà danh mục hỗ trợ. |
| ↳↳ description | string | Category description. |
| ↳↳ category_type | string | Category type.  For `excluded_category_list`,`CATEGORY_TYPE_EXCLUSION`(content exclusion category ) will be returned . |
| ↳ vertical_sensitivity_list | object[] | Danh sách các danh mục ngành dọc chứa nội dung nhạy cảm. |
| ↳↳ category_id | string | Category ID. |
| ↳↳ category_name | string | Category name. |
| ↳↳ supported_regions | string[] | Mã quốc gia hoặc khu vực mà danh mục hỗ trợ. |
| ↳↳ description | string | Category description. |
| ↳↳ category_type | string | Category type. For `vertical_sensitivity_list`,`CATEGORY_TYPE_VERTICAL`(vertical sensitivity category) will be returned. |

### Ví dụ lệnh cURL (Example)

``` xcodeblock
(code curl http)
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "excluded_category_list": [
            {
                "description": "YouthContentDescriptionKey",
                "category_type": "CATEGORY_TYPE_EXCLUSION",
                "supported_regions": [
                    "US",
                    "GB",
                    "AU",
                    "CA"
                ],
                "category_id": "200",
                "category_name": "Youth content"
            },
            {
                "description": "CombatSportsDescriptionKey",
                "category_type": "CATEGORY_TYPE_EXCLUSION",
                "supported_regions": [
                    "US",
                    "GB",
                    "AU",
                    "CA"
                ],
                "category_id": "201",
                "category_name": "Combat sports"
            },
            {
                "description": "ViolentVideoGamesDescriptionKey",
                "category_type": "CATEGORY_TYPE_EXCLUSION",
                "supported_regions": [
                    "US",
                    "GB",
                    "AU",
                    "CA"
                ],
                "category_id": "202",
                "category_name": "Violent video games"
            },
            {
                "description": "GamblingDescriptionKey",
                "category_type": "CATEGORY_TYPE_EXCLUSION",
                "supported_regions": [
                    "US",
                    "GB",
                    "AU",
                    "CA"
                ],
                "category_id": "203",
                "category_name": "Gambling and lotteries"
            }
        ],
        "vertical_sensitivity_list": []
    }
}

{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "excluded_category_list": [
            {
                "category_type": "CATEGORY_TYPE_EXCLUSION",
                "category_id": "200",
                "category_name": "Youth content",
                "description": "YouthContentDescriptionKey",
                "supported_regions": [
                    "US",
                    "GB",
                    "AU",
                    "CA"
                ]
            },
            {
                "category_type": "CATEGORY_TYPE_EXCLUSION",
                "category_id": "201",
                "category_name": "Combat sports",
                "description": "CombatSportsDescriptionKey",
                "supported_regions": [
                    "US",
                    "GB",
                    "AU",
                    "CA"
                ]
            },
            {
                "category_type": "CATEGORY_TYPE_EXCLUSION",
                "category_id": "202",
                "category_name": "Violent video games",
                "description": "ViolentVideoGamesDescriptionKey",
                "supported_regions": [
                    "US",
                    "GB",
                    "AU",
                    "CA"
                ]
            },
            {
                "category_type": "CATEGORY_TYPE_EXCLUSION",
                "category_id": "203",
                "category_name": "Gambling and lotteries",
                "description": "GamblingDescriptionKey",
                "supported_regions": [
                    "US",
                    "GB",
                    "AU",
                    "CA"
                ]
            }
        ],
        "vertical_sensitivity_list": [
            {
                "category_type": "CATEGORY_TYPE_VERTICAL",
                "category_id": "1000",
                "category_name": "Beauty",
                "description": "This will exclude any content that TikTok deems as controversial or negative beauty-related patterns which may impact your campaign performance.",
                "supported_regions": [
                    "US",
                    "GB",
                    "AU",
                    "CA"
                ]
            },
            {
                "category_type": "CATEGORY_TYPE_VERTICAL",
                "category_id": "1001",
                "category_name": "Food",
                "description": "This will exclude any content that TikTok deems as unhealthy food behaviors, body shaming, or graphic food content which may impact your campaign performance.",
                "supported_regions": [
                    "US",
                    "GB",
                    "AU",
                    "CA"
                ]
            },
            {
                "category_type": "CATEGORY_TYPE_VERTICAL",
                "category_id": "1002",
                "category_name": "Pets",
                "description": "This will exclude any content that TikTok deems as unfair treatment to animals or pets, such as sensitive issues like animal testing, animal products used in fashion or pet illness, or demise-related content which may impact your campaign performance.",
                "supported_regions": [
                    "US",
                    "GB",
                    "AU",
                    "CA"
                ]
            }
        ]
    }
}
(/code)
```

---

<a id="doc-1769738105333826"></a>
<!-- doc_id: 1769738105333826 -->
<!-- doc_id: 1769738105333826 -->
# Lấy thông tin chi tiết danh mục loại trừ nội dung (Get details of content exclusion categories)
> Đường dẫn: API Reference > Tools > Get details of content exclusion categories
Sử dụng endpoint này để lấy thông tin the detailed information of **content categories** or **vertical categories** that can be excluded from appearing next to your ads.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/tool/content_exclusion/info/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id  ****(Bắt buộc)**** | string | ID tài khoản quảng cáo TikTok. |
| category_ids  ****(Bắt buộc)**** | string[] | IDs of the content exclusion categories or vertical sensitivity categories. You can get `category_id` from the response of **/tool/content_exclusion/get/**. |

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location -g 'https://business-api.tiktok.com/open_api/v1.3/tool/content_exclusion/info/?advertiser_id={{advertiser_id}}&category_ids=[{{category_id}},{{category_id}}]' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Response code. For the complete list of error codes and descriptions, see [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | Mã nhật ký yêu cầu (request log ID) để định danh duy nhất cho mỗi lượt gọi API. |
| data | object | Returned data. |
| ↳ content_exclusion_list | object[] | Danh sách các danh mục nội dung hoặc danh mục ngành dọc. |
| ↳↳ category_id | string | Category ID. |
| ↳↳ category_name | string | Category name. |
| ↳↳ supported_regions | string[] | Mã quốc gia hoặc khu vực mà danh mục hỗ trợ. |
| ↳↳ description | string | Category description. |
| ↳↳ category_type | string | Category type. Các giá trị enum hỗ trợ: `CATEGORY_TYPE_EXCLUSION`(content exclusion category ) and `CATEGORY_TYPE_VERTICAL`(vertical sensitivity category). |

### Ví dụ lệnh cURL (Example)
```http
// curl
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "content_exclusion_list": [
            {
                "description": "CombatSportsDescriptionKey",
                "category_type": "CATEGORY_TYPE_EXCLUSION",
                "supported_regions": [
                    "US",
                    "GB",
                    "AU",
                    "CA"
                ],
                "category_id": "201",
                "category_name": "Combat sports"
            },
            {
                "description": "ViolentVideoGamesDescriptionKey",
                "category_type": "CATEGORY_TYPE_EXCLUSION",
                "supported_regions": [
                    "US",
                    "GB",
                    "AU",
                    "CA"
                ],
                "category_id": "202",
                "category_name": "Violent video games"
            },
            {
                "description": "GamblingDescriptionKey",
                "category_type": "CATEGORY_TYPE_EXCLUSION",
                "supported_regions": [
                    "US",
                    "GB",
                    "AU",
                    "CA"
                ],
                "category_id": "203",
                "category_name": "Gambling and lotteries"
            },
            {
                "description": "YouthContentDescriptionKey",
                "category_type": "CATEGORY_TYPE_EXCLUSION",
                "supported_regions": [
                    "US",
                    "GB",
                    "AU",
                    "CA"
                ],
                "category_id": "200",
                "category_name": "Youth content"
            }，
            {
                "category_type": "CATEGORY_TYPE_VERTICAL",
                "category_id": "1002",
                "category_name": "Pets",
                "description": "This will exclude any content that TikTok deems as unfair treatment to animals or pets, such as sensitive issues like animal testing, animal products used in fashion or pet illness, or demise-related content which may impact your campaign performance.",
                "supported_regions": [
                    "US",
                    "GB",
                    "AU",
                    "CA"
                ]
            }
        ]
    }
}
```

---

<a id="doc-1746463695763458"></a>
<!-- doc_id: 1746463695763458 -->
<!-- doc_id: 1746463695763458 -->
# (Sắp ngừng hoạt động) Lấy ngân sách đề xuất ((To-be-deprecated) Get recommended budgets)
> Đường dẫn: API Reference > Tools > (To-be-deprecated) Get recommended budgets
> **Important:** 
> Endpoint này sẽ ngừng hoạt động trong phiên bản API tiếp theo. Chúng tôi khuyến nghị bạn chuyển sang [/tool/diagnosis/get/](06-ad-diagnosis.md#doc-1738674986981378) và lấy kết quả phân phối ước tính theo ngân sách thông qua tham số phản hồi `budget_edr_info`.

Sử dụng endpoint này để lấy thông tin 15 bộ ngân sách đề xuất và dữ liệu chuyển đổi ước tính tương ứng cho từng mức ngân sách trong cùng ngày áp dụng ngân sách. Xem [tại đây](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1746463333984258) để biết các điều kiện tiên quyết và các bước lấy kết quả phân phối ước tính theo ngân sách.

>**Note:**  • Budget estimated delivery results are given according to your ad group setting. If you evaluate multiple ad groups of the same setting via this endpoint , you can only get results for the earliest ad group.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/delivery/budget/recommend/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id {required} |string| ID tài khoản quảng cáo TikTok. |
| adgroup_ids {required} | string[] | Danh sách ID nhóm quảng cáo. Số lượng ID không được vượt quá 20. |
### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/delivery/budget/recommend/?advertiser_id={{advertiser_id}}&adgroup_ids=["{{adgroup_id}}"]' \
--header 'Access-Token: {{Access-Token}}'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|code |number| Response code. For the complete list of response codes and descriptions, see [Appendix-Return codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|message |string| Response message. Để biết chi tiết, xem [Appendix-Return codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|request_id |string| Mã nhật ký yêu cầu (request log ID) để định danh duy nhất cho mỗi lượt gọi API. |
|data |object| Returned data. |
#| results |object[] | List of ad group IDs and corresponding budget recommendation results.|
##| adgroup_id | string | ID nhóm quảng cáo. |
##| recommendations | object[] | 15 sets of data for recommended budget raise ratios from -20% to 50% with a step of 5%, and corresponding estimated results. |
###| recommended_budget |  float| Recommended budget. Please adopt one suitable budget using [/adgroup/budget/update/](07-ad-groups-p3.md#doc-1739591133130817) within the same day (advertiser account time zone). |
###| budget_increase_ratio | float | Tỷ lệ tăng ngân sách ước tính. |
###| estimated_conversion | integer | Lượt chuyển đổi ước tính. |
###| conversion_uplift | integer | Mức tăng lượt chuyển đổi ước tính. |
###| conversion_uplift_ratio | float | Tỷ lệ tăng lượt chuyển đổi ước tính. |

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "results": [
            {
                "recommendations": [
                    {
                        "budget_increase_ratio": -0.2,
                        "conversion_uplift": 0,
                        "recommended_budget": 80.0,
                        "estimated_conversion": 39,
                        "conversion_uplift_ratio": 0.0
                    },
                    {
                        "budget_increase_ratio": -0.15,
                        "conversion_uplift": 0,
                        "recommended_budget": 85.0,
                        "estimated_conversion": 40,
                        "conversion_uplift_ratio": 0.0
                    },
                    {
                        "budget_increase_ratio": -0.1,
                        "conversion_uplift": 0,
                        "recommended_budget": 90.0,
                        "estimated_conversion": 41,
                        "conversion_uplift_ratio": 0.0
                    },
                    {
                        "budget_increase_ratio": -0.05,
                        "conversion_uplift": 0,
                        "recommended_budget": 95.0,
                        "estimated_conversion": 41,
                        "conversion_uplift_ratio": 0.0
                    },
                    {
                        "budget_increase_ratio": 0.0,
                        "conversion_uplift": 0,
                        "recommended_budget": 100.0,
                        "estimated_conversion": 41,
                        "conversion_uplift_ratio": 0.0
                    },
                    {
                        "budget_increase_ratio": 0.05,
                        "conversion_uplift": 0,
                        "recommended_budget": 105.0,
                        "estimated_conversion": 43,
                        "conversion_uplift_ratio": 0.0
                    },
                    {
                        "budget_increase_ratio": 0.1,
                        "conversion_uplift": 0,
                        "recommended_budget": 110.0,
                        "estimated_conversion": 45,
                        "conversion_uplift_ratio": 0.0
                    },
                    {
                        "budget_increase_ratio": 0.15,
                        "conversion_uplift": 0,
                        "recommended_budget": 115.0,
                        "estimated_conversion": 46,
                        "conversion_uplift_ratio": 0.0
                    },
                    {
                        "budget_increase_ratio": 0.2,
                        "conversion_uplift": 0,
                        "recommended_budget": 120.0,
                        "estimated_conversion": 48,
                        "conversion_uplift_ratio": 0.0
                    },
                    {
                        "budget_increase_ratio": 0.25,
                        "conversion_uplift": 0,
                        "recommended_budget": 125.0,
                        "estimated_conversion": 49,
                        "conversion_uplift_ratio": 0.0
                    },
                    {
                        "budget_increase_ratio": 0.3,
                        "conversion_uplift": 0,
                        "recommended_budget": 130.0,
                        "estimated_conversion": 51,
                        "conversion_uplift_ratio": 0.0
                    },
                    {
                        "budget_increase_ratio": 0.35,
                        "conversion_uplift": 0,
                        "recommended_budget": 135.0,
                        "estimated_conversion": 52,
                        "conversion_uplift_ratio": 0.0
                    },
                    {
                        "budget_increase_ratio": 0.4,
                        "conversion_uplift": 0,
                        "recommended_budget": 140.0,
                        "estimated_conversion": 53,
                        "conversion_uplift_ratio": 0.0
                    },
                    {
                        "budget_increase_ratio": 0.45,
                        "conversion_uplift": 0,
                        "recommended_budget": 145.0,
                        "estimated_conversion": 54,
                        "conversion_uplift_ratio": 0.0
                    },
                    {
                        "budget_increase_ratio": 0.5,
                        "conversion_uplift": 0,
                        "recommended_budget": 150.0,
                        "estimated_conversion": 55,
                        "conversion_uplift_ratio": 0.0
                    }
                ],
                "adgroup_id": "{{adgroup_id}}"
            }
        ]
    }
}
```

---

<a id="doc-1746463732779009"></a>
<!-- doc_id: 1746463732779009 -->
<!-- doc_id: 1746463732779009 -->
# (Sắp ngừng hoạt động) Lấy giá thầu đề xuất ((To-be-deprecated) Get recommended bids)
> Đường dẫn: API Reference > Tools > (To-be-deprecated) Get recommended bids
> **Important:** 
> Endpoint này sẽ ngừng hoạt động trong phiên bản API tiếp theo. Chúng tôi khuyến nghị bạn chuyển sang [/tool/diagnosis/get/](06-ad-diagnosis.md#doc-1738674986981378) và lấy kết quả phân phối ước tính theo giá thầu thông qua tham số phản hồi `bid_edr_info`.

Sử dụng endpoint này để lấy thông tin 9 sets of recommended bids and the corresponding estimated cost data for each bid on the same day when the bid is adopted.

Nếu muốn lấy giá trị giá thầu đề xuất cho nhóm quảng cáo dựa trên cài đặt cơ bản của chiến dịch và nhóm quảng cáo, xem [Get suggested bid](https://ads.tiktok.com/marketing_api/docs?id=1737107845597186).

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/delivery/bid/recommend/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id {required} |string| ID tài khoản quảng cáo TikTok. |
| adgroup_ids {required} | string[] | Danh sách ID nhóm quảng cáo. Số lượng ID không được vượt quá 20. |

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/delivery/bid/recommend/?advertiser_id={{advertiser_id}}&adgroup_ids=["{{adgroup_id}}"]' \
--header 'Access-Token: {{Access-Token}}'
```
## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|code |number| Response code. For the complete list of response codes and descriptions, see [Appendix-Return codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|message |string| Response message. Để biết chi tiết, xem [Appendix-Return codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|request_id |string| Mã nhật ký yêu cầu (request log ID) để định danh duy nhất cho mỗi lượt gọi API. |
|data |object| Returned data. |
#| results |object[] | List of ad group IDs and corresponding bid recommendation results.|
##| adgroup_id | string | ID nhóm quảng cáo. |
##| recommendations | object[] | 9 sets of data for recommended bid raise ratios from -10% to 30% with a step of 5% and corresponding estimated results.|
###| recommended_bid | float | Recommended bid. Please adopt one suitable bid using [/adgroup/update/](07-ad-groups-p3.md#doc-1739586761631745) and pass the adopted bid price to `conversion_bid_price` within the same day (advertiser account time zone). |
###| bid_increase_ratio | float | Tỷ lệ tăng giá thầu ước tính. |
###| estimated_cost | float | Chi phí ước tính. |
###| cost_uplift | float | Mức tăng chi phí ước tính. |
###| cost_uplift_ratio | float | Tỷ lệ tăng chi phí ước tính. |
### Ví dụ lệnh cURL (Example)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "results": [
            {
                "recommendations": [
                    {
                        "cost_uplift_ratio": 0.83,
                        "estimated_cost": 553.43,
                        "recommended_bid": 0.63,
                        "bid_increase_ratio": 0.25,
                        "cost_uplift": 251.4
                    },
                    {
                        "cost_uplift_ratio": 0.47,
                        "estimated_cost": 444.8,
                        "recommended_bid": 0.57,
                        "bid_increase_ratio": 0.15,
                        "cost_uplift": 142.36
                    },
                    {
                        "cost_uplift_ratio": -0.14,
                        "estimated_cost": 261.17,
                        "recommended_bid": 0.48,
                        "bid_increase_ratio": -0.05,
                        "cost_uplift": -42.4
                    },
                    {
                        "cost_uplift_ratio": -0.27,
                        "estimated_cost": 222.25,
                        "recommended_bid": 0.45,
                        "bid_increase_ratio": -0.1,
                        "cost_uplift": -81.78
                    },
                    {
                        "cost_uplift_ratio": 0.0,
                        "estimated_cost": 302.89,
                        "recommended_bid": 0.5,
                        "bid_increase_ratio": 0.0,
                        "cost_uplift": 0
                    },
                    {
                        "cost_uplift_ratio": 0.15,
                        "estimated_cost": 347.4,
                        "recommended_bid": 0.53,
                        "bid_increase_ratio": 0.05,
                        "cost_uplift": 45.43
                    },
                    {
                        "cost_uplift_ratio": 1.02,
                        "estimated_cost": 611.93,
                        "recommended_bid": 0.65,
                        "bid_increase_ratio": 0.3,
                        "cost_uplift": 308.95
                    },
                    {
                        "cost_uplift_ratio": 0.64,
                        "estimated_cost": 497.73,
                        "recommended_bid": 0.6,
                        "bid_increase_ratio": 0.2,
                        "cost_uplift": 193.85
                    },
                    {
                        "cost_uplift_ratio": 0.3,
                        "estimated_cost": 394.72,
                        "recommended_bid": 0.55,
                        "bid_increase_ratio": 0.1,
                        "cost_uplift": 90.87
                    }
                ],
                "adgroup_id": "adgroup_id"
            }
        ]
    }
}
```

---

<a id="doc-1737107845597186"></a>
<!-- doc_id: 1737107845597186 -->
<!-- doc_id: 1737107845597186 -->
# Lấy giá thầu gợi ý (Get a suggested bid)
> Đường dẫn: API Reference > Tools > Get a suggested bid
Sử dụng endpoint này để lấy thông tin a suggested bid value for your ad group based on basic campaign and ad group settings like objectives, conversion events, and locations. Note that the suggested bid can only be used with Cost Cap bidding strategy (`bid_type = BID_TYPE_CUSTOM`).

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/tool/bid/recommend/

**Method** POST

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id  ****(Bắt buộc)**** | string | ID tài khoản quảng cáo TikTok. |
| campaign_id | string | ID chiến dịch quảng cáo. |
| objective_type  ****(Bắt buộc)**** | string | Mục tiêu chiến dịch. The current API endpoint only supports Traffic and Website conversions objectives. For enum values and descriptions, see [Objectives](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1737585562434561). ⏎ **Note**: This API is being revamped to support larger function scope and more accurate result. Please stay tuned for updates. |
| location_ids  ****(Bắt buộc)**** | string[] | IDs of the locations that you want to target. |
| external_action | string | Conversion event for the ad group. |

### Ví dụ lệnh cURL (Example)

```http
// curl
curl -H "Access-Token:xxx" -H "Content-Type:application/json" -X POST \
-d '{
    "advertiser_id": "ADVERTISER_ID",
    "campaign_id": "CAMPAIGN_ID",
    "objective_type": "OBJECTIVE_TYPE",
    "locations": [
        "LOCATIONS"
    ],
    "external_action": "EXTERNAL_ACTION"
}' \
https://business-api.tiktok.com/open_api/v1.3/tool/bid/recommend/
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Response code. For the complete list of error codes and descriptions, see [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | Mã nhật ký yêu cầu (request log ID) để định danh duy nhất cho mỗi lượt gọi API. |
| data | object | Returned data. |
| ↳ bid | number | Recommended bid value. |

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "1234",
    "data": {
       "bid": 1.0
	   }
}
```

---

<a id="doc-1770016073586753"></a>
<!-- doc_id: 1770016073586753 -->
<!-- doc_id: 1770016073586753 -->
# Kiểm tra tính hợp lệ tối ưu hóa dựa trên giá trị (Check Value-Based Optimization eligibility)
> Đường dẫn: API Reference > Tools > Check Value-Based Optimization eligibility
Sử dụng endpoint này để kiểm tra Liệu certain settings are eligible for Value-Based Optimization (VBO), and to get the available VBO bidding strategies for the specified settings.

Để tìm hiểu cách bật VBO, tham khảo [Bật tối ưu hóa dựa trên giá trị (Enable Value-Based Optimization)](../09-marketing-api/quan-ly-chien-dich-tom-tat.md#doc-1770019181843458).

>**Note:**  
> If you specify through the request an allowlist-only VBO feature, and you are not allowlisted for the feature, the response will indicate that your settings are ineligible for VBO (`vo_status` = `NOT_SUPPORT`).

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/tool/vbo_status/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id ***(Bắt buộc)*** | string | ID tài khoản quảng cáo TikTok.   |
| objective_type ***(Bắt buộc)*** | string | Mục tiêu quảng cáo.  <br>Set this field to `APP_PROMOTION`, `WEB_CONVERSIONS`, or `PRODUCT_SALES`. <br>When you set this field to any other objective, `vo_status` will be `NOT_SUPPORT` because these objectives are not supported for VBO.  <br>For enum values and descriptions, see [Objectives](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1737585562434561).  <br><p><span style="color:darkred"><b>Note</b></span>:  When `objective_type` is set to `PRODUCT_SALES` and `promotion_type` is set to `LIVE_SHOPPING` or `VIDEO_SHOPPING`, do not pass in `pixel_id` or `app_id`. Otherwise, pass in either `pixel_id` or `app_id`.   |
| app_promotion_type**(Điều kiện)** | string | Bắt buộc khi `objective_type` is `APP_PROMOTION`.   <br> Loại quảng bá ứng dụng.  <br>Các giá trị enum hỗ trợ: <ul><li>`APP_INSTALL`: Get new users to install your app. </li><li>`APP_RETARGETING`: Re-engage existing users to take action in your app.</li><li>`MINIS`: TikTok Minis. Get people to watch your series or play your games with TikTok Minis.<ul><li>To learn more about the campaign type where this setting is supported, see [Create an Upgraded Smart+ Minis Campaign](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1853377811982657).</li></ul></li></ul><br><p><span style="color:darkred"><b>Note</b></span>: Only the enum value `APP_INSTALL` can be used in an iOS14 Dedicated Campaign.   |
| campaign_type | string | Không truyền đồng thời `campaign_type` và `ios14_quota_type`. If both fields are passed, `ios14_quota_type` will be ignored. <br><br>Loại chiến dịch. <br><br>Enums values: <ul><li>`REGULAR_CAMPAIGN`: non-iOS 14 Dedicated Campaign.</li><li> `IOS14_CAMPAIGN`: iOS 14 Dedicated Campaign.</li></ul><br>The value `IOS14_CAMPAIGN` can only be used when: <ul><li>`objective_type` is `PRODUCT_SALES`. </li><li>`objective_type` is `APP_PROMOTION` and `app_promotion_type` is `APP_INSTALL`.</li></ul>|
| is_advanced_dedicated_campaign | boolean | Liệu campaign is an Advanced Dedicated Campaign. Advanced Dedicated Campaigns leverage advanced delivery models that benefit from real-time signals. <br><br>Các giá trị được hỗ trợ: `true`, `false`. <br>Giá trị mặc định: `false`. <br><br>Để tìm hiểu cách tạo các chiến dịch này, xem [Create Advanced Dedicated Campaigns](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1797011827608577). <br><br><p><span style="color:darkred"><b>Note</b></span>: Once set, this field cannot be updated. |
| disable_skan_campaign | boolean | Chỉ hợp lệ khi tất cả các điều kiện sau đều được thỏa mãn: <ul><li>`objective_type` is `APP_PROMOTION`.</li><li>`app_promotion_type` is `APP_INSTALL`.</li><li>`campaign_type` is `IOS14_CAMPAIGN`.</li><li>`app_id` is set to the ID of an iOS app that is eligible for [Advanced Dedicated Campaigns](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1797011827608577). To confirm Liệu an app is eligible for Advanced Dedicated Campaigns, use [/app/list/](43-events-1-0-p1.md#doc-1740859313270786) and check the returned `advanced_dedicated_campaign_allowed`.</li></ul><br>Có thực hiện disable SKAN (SKAdNetwork) attribution, Apple's conversion attribution solution for iOS campaigns<br><br>Các giá trị enum hỗ trợ: <ul><li>`true`: To disable SKAN attribution. The campaign will not be bound by [Dedicated Campaign quota limits](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1752256248260610) and you will be able to retrieve [Self Attribution Network (SAN) metrics](../09-marketing-api/bao-cao-p2.md#doc-1751443967255553) for the campaign. However, you cannot retrieve [SKAN reporting metrics](../09-marketing-api/bao-cao-p2.md#doc-1751443967255553) for the campaign. Learn more about [SAN integration](https://ads.tiktok.com/help/article/about-self-attribution-transition). <ul><li>For a Dedicated Campaign using an app that is eligible for Advanced Dedicated Campaigns, you need to enable SKAN attribution or Advanced Dedicated Campaign or both. You cannot disable SKAN attribution and Advanced Dedicated Campaign simultaneously.</li></ul></li><li>`false`: To enable SKAN attribution. The campaign will be bound by [Dedicated Campaign quota limits](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1752256248260610) and you will be able to retrieve [SKAN metrics](../09-marketing-api/bao-cao-p2.md#doc-1751443967255553) for the campaign.<ul><li>If you enable Advanced Dedicated Campaign by setting `is_advanced_dedicated_campaign` to `true` simultaneously, you'll be able to retrieve both [SAN](../09-marketing-api/bao-cao-p2.md#doc-1751443967255553) and [SKAN reporting metrics](../09-marketing-api/bao-cao-p2.md#doc-1751443967255553) for the campaign. </li></ul></li></ul><br><p><span style="color:darkred"><b>Note</b></span>: <ul><li>Disabling SKAN attribution for Dedicated Campaigns is currently an allowlist-only feature. If you would like to access it, please contact your TikTok representative.</li><li>If you are allowlisted for disabling SKAN attribution for Dedicated Campaigns, you cannot set `bid_type` to `BID_TYPE_CUSTOM` at the ad group level when the following conditions are all met:<ul><li>At the campaign level: <ul><li>`is_advanced_dedicated_campaign` is `false`.</li><li>`disable_skan_campaign` is `false`.</li></ul></li><li>At the ad group level:<ul><li>`optimization_goal` is `INSTALL` or `IN_APP_EVENT`.</li></ul></li></ul></li><li>Once set, this field cannot be updated.</li><li>Getting access to Advanced Dedicated Campaign requires the app to meet certain criteria. If your app is ineligible for Advanced Dedicated Campaign, reach out to your TikTok representative. Your TikTok representative will be able to provide troubleshooting support to help your app get access to Advanced Dedicated Campaign.</li></ul> |
| bid_align_type | string |Chỉ hợp lệ khi tất cả các điều kiện sau đều được thỏa mãn: <ul><li>`objective_type` is `APP_PROMOTION`.</li><li>`app_promotion_type` is `APP_INSTALL`.</li><li>`campaign_type` is `IOS14_CAMPAIGN`.</li><li>`app_id` is set to the ID of an iOS app that is eligible for [Advanced Dedicated Campaigns](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1797011827608577). To confirm Liệu an app is eligible for Advanced Dedicated Campaigns, use [/app/list/](43-events-1-0-p1.md#doc-1740859313270786) and check the returned `advanced_dedicated_campaign_allowed`.</li></ul><br>The attribution type for the Dedicated Campaign. The type determines which attribution network the target CPA or ROAS at the ad group level is based on.<br><br>Enum value:<ul><li>`SAN`: Self Attributing Network(SAN).</li><li>`SKAN`: SKAdNetwork (SKAN).</li></ul><br><ul><li>When `is_advanced_dedicated_campaign` is `true` and you are not allowlisted for disabling SKAN attribution for Dedicated Campaigns, set this field to `SKAN`.</li><li>When `is_advanced_dedicated_campaign` is `true`, you are allowlisted for disabling SKAN attribution for Dedicated Campaigns, and `disable_skan_campaign` is `false`, set this field to `SAN`.</li><li>When `is_advanced_dedicated_campaign` is `true` and `disable_skan_campaign` is `true`, set this field to `SAN`.</li><li>When `is_advanced_dedicated_campaign` is `false` and `disable_skan_campaign` is `false`, set this field to `SKAN`. </li></ul>|
| promotion_type ***(Bắt buộc)*** | string | Promotion type and you can decide where you'd like to promote your products using this field. <br>Để xem danh sách giá trị enum, xem [Enumeration - Promotion Type](../15-appendix/phu-luc-p1.md#doc-1737174886619138).  <br><p><span style="color:darkred"><b>Note</b></span>:   When `objective_type` is set to `PRODUCT_SALES` and `promotion_type` is set to `LIVE_SHOPPING` or `VIDEO_SHOPPING`, do not pass in `pixel_id` or `app_id`. Otherwise, pass in either `pixel_id` or `app_id`.   |
| placements ***(Bắt buộc)*** | string[] | The apps where you want to deliver your ads.   <br><p><span style="color:darkred"><b>Note</b></span>:  <ul><li> Currently, we support `PLACEMENT_TIKTOK`, `PLACEMENT_PANGLE` and `PLACEMENT_GLOBAL_APP_BUNDLE`.  </li><li> For Product Sales campaigns (`objective_type` = `PRODUCT_SALES`), only TikTok placement (`PLACEMENT_TIKTOK`) is supported. </li></ul>    |
| ios14_quota_type{-To be deprecated} | string |Không truyền đồng thời `campaign_type` và `ios14_quota_type`. If both fields are passed, `ios14_quota_type` will be ignored. <br>We recommend using `campaign_type` alone when you specify an iOS 14 Dedicated Campaign. <br> <ul><li>`campaign_type` as `REGULAR_CAMPAIGN` or `ios14_quota_type` as `UNOCCUPIED` both indicate a non-iOS 14 Dedicated Campaign.</li><li>`campaign_type` as `IOS14_CAMPAIGN` or `ios14_quota_type` as `OCCUPIED` both indicate an iOS 14 Dedicated Campaign. </li></ul><br> Liệu campaign will be counted towards the iOS 14 Dedicated Campaign quota.  <br>Các giá trị enum hỗ trợ: <ul><li>`OCCUPIED`: The campaign is an iOS 14 Dedicated Campaign. </li><li>`UNOCCUPIED`: The campaign is not an iOS 14 Dedicated Campaign. </li></ul>|
| campaign_app_profile_page_state | string | Có thực hiện use App Profile Page at the campaign level to optimize delivery.  <br>Các giá trị enum hỗ trợ: `ON`, `OFF`.<br> You can use the field only when `objective_type` is `APP_PROMOTION` and your campaign is an iOS14 Dedicated Campaign (`ios14_quota_type` =`OCCUPIED`). Otherwise, an error will occur.   |
| pixel_id **(Điều kiện)** | string | Not supported when `objective_type` is set to `PRODUCT_SALES` and `promotion_type` is set to `LIVE_SHOPPING` or `VIDEO_SHOPPING` or when `app_promotion_type` is `MINIS`.   <br>Otherwise, pass in either `pixel_id` or `app_id`. <br><br>ID TikTok Pixel. <br>When you pass in this field, you need to specify `optimization_event` at the same time. <br>To get Pixel IDs, use the [/pixel/list/](43-events-1-0-p1.md#doc-1740858697598978) endpoint.   |
| app_id **(Điều kiện)** | string | Not supported when `objective_type` is set to `PRODUCT_SALES` and `promotion_type` is set to `LIVE_SHOPPING` or `VIDEO_SHOPPING` or when `app_promotion_type` is `MINIS`.   <br>Otherwise, pass in either `pixel_id` or `app_id`.   <br><br> The Application ID of the promoted app. <br>To get App IDs, use the [/app/list/](43-events-1-0-p1.md#doc-1740859313270786) endpoint.   |
| optimization_event **(Điều kiện)** | string | Bắt buộc khi `pixel_id` is passed.  <br>Ignored when `app_id` is passed.  <br> Conversion event for the ad group. <br> See [Conversion events](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1739361474981889) for more.   |
| store_id | string | Chỉ hợp lệ khi `objective_type` is `PRODUCT_SALES`.  <br>ID of the TikTok Shop.<br><p><span style="color:darkred"><b>Note</b></span>: To get the TikTok Shop ID, you can use [/bc/asset/get/](15-bc-assets.md#doc-1739432717798401):  <ul><li> When in the response `asset_type` is `TIKTOK_SHOP`, the returned `asset_id` is the TikTok Shop ID.</li></ul>  |
| is_smart_performance_campaign<br> {-to-be-deprecated}| boolean | Liệu campaign is a Smart+ Campaign or not.   <br>Các giá trị enum hỗ trợ: `true`, `false`.   |
| campaign_automation_type | string | Campaign automation type.<br><br>Các giá trị enum hỗ trợ: <ul><li>`MANUAL`: Manual Campaigns.</li><li>`SMART_PLUS`: Smart+ Campaigns.</li><li>`UPGRADED_SMART_PLUS`: Upgraded Smart+ Campaigns, a new automated campaign type. To learn more about Upgraded Smart+ Campaigns, see [Upgraded Smart+ Campaign](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1853452461203458).</li></ul> |
| budget_optimize_on | boolean | Có thực hiện enable Campaign Budget Optimization (CBO).   <br> Các giá trị enum hỗ trợ: `true`, `false`.<br> For details about CBO, see [Campaign Budget Optimization](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1739381757818881). |

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location  --request GET 'https://business-api.tiktok.com/open_api/v1.3/tool/vbo_status/?advertiser_id={{advertiser_id}}&promotion_type=LIVE_SHOPPING&placements=["PLACEMENT_TIKTOK"]&objective_type=PRODUCT_SALES&optimization_event=SHOPPING&store_id={{store_id}}' \
--header 'Access-Token: {{Access-Token}}' \
```
## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|-|-|-|
|code |number|Response code. For the complete list of response codes and descriptions, see [Appendix-Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message|string|Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|request_id |string|Mã nhật ký yêu cầu (request log ID) để định danh duy nhất cho mỗi lượt gọi API.  |
|data |object|Returned data.|
#|vo_status | string | The status of VBO for Web or VBO IAP for App for the settings in the request.  <br>Các giá trị enum hỗ trợ: <ul><li>`QUALIFIED`: Eligible. </li><li>`NO_EVENT`: Not eligible because the pixel (`pixel_id`) or App (`app_id`) has not accumulated any event. </li><li>`NO_VALUE`: Not eligible because the pixel (`pixel_id`) or App (`app_id`) has not accumulated any value. </li><li>`INSUFFICIENT_EVENTS`: Not eligible because the pixel (`pixel_id`) or App (`app_id`) has not accumulated enough events. </li><li>`NOT_SUPPORT`: Not eligible for any of the following reasons: <ul><li> The settings are not supported. </li><li> The settings are supported, but you are not allowlisted to use the allowlist-only feature specified through the settings. </li></ul></li></ul> |
#| vo_min | string | The status of the Cost Cap bidding strategy for the settings in the request when VBO for Web or VBO IAP for App is enabled.  <br> Các giá trị enum hỗ trợ: <ul><li> `QUALIFIED`: Eligible. </li><li>`NO_EVENT`: Not eligible because the pixel (`pixel_id`) or App (`app_id`) has not accumulated any event.  </li><li>`NO_VALUE`: Not eligible because the pixel (`pixel_id`) or App (`app_id`) has not accumulated any value. </li><li>`INSUFFICIENT_EVENTS`: Not eligible because the pixel (`pixel_id`) or App (`app_id`) has not accumulated enough events.</li><li>`NOT_SUPPORT`: Not eligible for any of the following reasons: <ul><li> The settings are not supported. </li><li> The settings are supported, but you are not allowlisted to use the allowlist-only feature specified through the settings. </li></ul></li></ul> <br><p><span style="color:darkred"><b>Note</b></span>: The Cost Cap bidding strategy is no longer supported for VBO. Therefore, the value of this field is always `NOT_SUPPORT`.   |
#| vo_min_roas | string | The status of the bidding strategy Minimum ROAS for the settings in the request when VBO  for Web or VBO IAP for App is enabled.  <br>Các giá trị enum hỗ trợ: <ul><li> `QUALIFIED`: Eligible. </li><li> `NO_EVENT`: Not eligible because the pixel (`pixel_id`) or App (`app_id`) has not accumulated any event. </li><li>`NO_VALUE`: Not eligible because the pixel (`pixel_id`) or App (`app_id`) has not accumulated any value. </li><li>`INSUFFICIENT_EVENTS`: Not eligible because the pixel (`pixel_id`) or App (`app_id`) has not accumulated enough events. </li><li>`NOT_SUPPORT`: Not eligible for any of the following reasons: <ul><li> The settings are not supported. </li><li> The settings are supported, but you are not allowlisted to use the allowlist-only feature specified through the settings.</li></ul></li></ul>    |
#| vo_highest_value | string | The status of the bidding strategy Highest Value for the settings in the request when VBO for Web or VBO IAP for App is enabled.  <br>Các giá trị enum hỗ trợ: <ul><li>`QUALIFIED`: Eligible. </li><li> `NO_EVENT`: Not eligible because the pixel (`pixel_id`) or App (`app_id`) has not accumulated any event.  </li><li> `NO_VALUE`: Not eligible because the pixel (`pixel_id`) or App (`app_id`) has not accumulated any value.  </li><li>`INSUFFICIENT_EVENTS`: Not eligible because the pixel (`pixel_id`) or App (`app_id`) has not accumulated enough events. </li><li>`NOT_SUPPORT`: Not eligible for any of the following reasons: <ul><li> The settings are not supported.</li><li> The settings are supported, but you are not allowlisted to use the allowlist-only feature specified through the settings. </li></ul></li></ul>  |
#| vo_iaa_min_roas| string | The status of the Day 7 bidding strategy Minimum ROAS (Day 7 ROAS) for the settings in the request when VBO IAA for App is enabled. <br><br>Các giá trị enum hỗ trợ: <ul><li>`QUALIFIED`: Eligible.</li><li> `NO_EVENT`: Not eligible because the App (`app_id`) has not accumulated any event.</li><li>`NO_VALUE`: Not eligible because the App (`app_id`) has not accumulated any events with a conversion value greater than 0.</li><li> `INSUFFICIENT_EVENTS`: Not eligible because the App (`app_id`) has not accumulated enough events with a conversion value greater than 0. </li><li>`NOT_SUPPORT`: Not eligible for any of the following reasons: <ul><li> The settings are not supported.</li><li> The settings are supported, but the App (`app_id`) has not met the unlocking criteria for the feature.</li></ul></li></ul>
#| vo_iaa_highest_value | string | The status of the Day 7 bidding strategy Highest Value (Day 7 Highest Value) for the settings in the request when VBO IAA for App is enabled. <br><br> Các giá trị enum hỗ trợ: <ul><li>`QUALIFIED`: Eligible.</li><li>`NO_EVENT`: Not eligible because the App (`app_id`) has not accumulated any event.</li><li>`NO_VALUE`: Not eligible because the App (`app_id`) has not accumulated any events with a conversion value greater than 0. </li><li>`INSUFFICIENT_EVENTS`: Not eligible because the App (`app_id`) has not accumulated enough events with a conversion value greater than 0.</li><li>`NOT_SUPPORT`: Not eligible for any of the following reasons: <ul><li> The settings are not supported.</li><li> The settings are supported, but the App (`app_id`) has not met the unlocking criteria for the feature.</li></ul></li></ul>|
#| vo_iaa_min_roas_zero_day| string | The status of the Day 0 bidding strategy Minimum ROAS (Day 0 ROAS) for the settings in the request when VBO IAA for App is enabled. <br><br>Các giá trị enum hỗ trợ: <ul><li>`QUALIFIED`: Eligible.</li><li> `NO_EVENT`: Not eligible because the App (`app_id`) has not accumulated any event.</li><li>`NO_VALUE`: Not eligible because the App (`app_id`) has not accumulated any events with a conversion value greater than 0.</li><li> `INSUFFICIENT_EVENTS`: Not eligible because the App (`app_id`) has not accumulated enough events with a conversion value greater than 0. </li><li>`NOT_SUPPORT`: Not eligible for any of the following reasons: <ul><li> The settings are not supported.</li><li> The settings are supported, but the advertiser (`advertiser_id`) has not been allowlisted for day 0 bidding of VBO IAA.</li></ul></li></ul>|
#| vo_iaa_highest_value_zero_day | string | The status of the Day 0 bidding strategy Highest Value (Day 0 Highest Value) for the settings in the request when VBO IAA for App is enabled. <br><br> Các giá trị enum hỗ trợ: <ul><li>`QUALIFIED`: Eligible.</li><li>`NO_EVENT`: Not eligible because the App (`app_id`) has not accumulated any event.</li><li>`NO_VALUE`: Not eligible because the App (`app_id`) has not accumulated any events with a conversion value greater than 0. </li><li>`INSUFFICIENT_EVENTS`: Not eligible because the App (`app_id`) has not accumulated enough events with a conversion value greater than 0.</li><li>`NOT_SUPPORT`: Not eligible for any of the following reasons: <ul><li> The settings are not supported.</li><li>  The settings are supported, but the advertiser (`advertiser_id`) has not been allowlisted for day 0 bidding of VBO IAA.</li></ul></li></ul>|
#| roas_status_day7 | string | The status of the Day 7 bidding strategy Minimum ROAS (Day 7 ROAS) for the settings in the request when VBO IAP for App is enabled.<br><br> Các giá trị enum hỗ trợ: <ul><li>`QUALIFIED`: Eligible.</li><li> `NO_EVENT`: Not eligible because the App (`app_id`) has not accumulated any event. </li><li>`NO_VALUE`: Not eligible because the App (`app_id`) has not accumulated any events with a conversion value greater than 0.</li><li> `INSUFFICIENT_EVENTS`: Not eligible because the App (`app_id`) has not accumulated enough events with a conversion value greater than 0.</li><li>`NOT_SUPPORT`: Not eligible for any of the following reasons:<ul><li> The settings are not supported.</li><li>The settings are supported, but the App (`app_id`) has not been allowlisted for day 7 bidding of VBO IAP.</li></ul></li></ul> |
#| highest_value_status_day7 | string | The status of the Day 7 bidding strategy Highest Value (Day 7 Highest Value) for the settings in the request when VBO IAP for App is enabled.<br><br> Các giá trị enum hỗ trợ: <ul><li>`QUALIFIED`: Eligible.</li><li> `NO_EVENT`: Not eligible because the App (`app_id`) has not accumulated any event. </li><li>`NO_VALUE`: Not eligible because the App (`app_id`) has not accumulated any events with a conversion value greater than 0.</li><li> `INSUFFICIENT_EVENTS`: Not eligible because the App (`app_id`) has not accumulated enough events with a conversion value greater than 0.</li><li>`NOT_SUPPORT`: Not eligible for any of the following reasons:<ul><li>The settings are not supported.</li><li>The settings are supported, but the App (`app_id`) has not been allowlisted for day 7 bidding of VBO IAP.</li></ul></li></ul> |
#| roas_status_day0 | string | The status of the Day 0 bidding strategy Minimum ROAS (Day 7 ROAS) for the settings in the request when VBO IAP for App is enabled.<br><br> Các giá trị enum hỗ trợ: <ul><li>`QUALIFIED`: Eligible.</li><li> `NO_EVENT`: Not eligible because the App (`app_id`) has not accumulated any event. </li><li>`NO_VALUE`: Not eligible because the App (`app_id`) has not accumulated any events with a conversion value greater than 0.</li><li> `INSUFFICIENT_EVENTS`: Not eligible because the App (`app_id`) has not accumulated enough events with a conversion value greater than 0.</li><li>`NOT_SUPPORT`: Not eligible for any of the following reasons:<ul><li>The settings are not supported.</li><li>The settings are supported, but the App (`app_id`) has not been allowlisted for day 0 bidding of VBO IAP.</li></ul></li></ul> |
#| highest_value_status_day0 | string | The status of the Day 0 bidding strategy Highest Value (Day 7 Highest Value) for the settings in the request when VBO IAP for App is enabled.<br><br> Các giá trị enum hỗ trợ: <ul><li>`QUALIFIED`: Eligible.</li><li> `NO_EVENT`: Not eligible because the App (`app_id`) has not accumulated any event. </li><li>`NO_VALUE`: Not eligible because the App (`app_id`) has not accumulated any events with a conversion value greater than 0.</li><li> `INSUFFICIENT_EVENTS`: Not eligible because the App (`app_id`) has not accumulated enough events with a conversion value greater than 0.</li><li>`NOT_SUPPORT`: Not eligible for any of the following reasons:<ul><li>The settings are not supported.</li><li>The settings are supported, but the App (`app_id`) has not been allowlisted for day 0 bidding of VBO IAP.</li></ul></li></ul> |
### Ví dụ lệnh cURL (Example)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "vo_highest_value": "QUALIFIED",
        "vo_min_roas": "QUALIFIED",
        "vo_status": "QUALIFIED",
        "vo_min": "NOT_SUPPORT",
		"vo_iaa_highest_value": "NOT_SUPPORT",
        "vo_iaa_min_roas": "NOT_SUPPORT",
        "vo_iaa_highest_value_zero_day": "NOT_SUPPORT",
        "vo_iaa_min_roas_zero_day": "NOT_SUPPORT"
    }
}
```

---

<a id="doc-1738456743621634"></a>
<!-- doc_id: 1738456743621634 -->
<!-- doc_id: 1738456743621634 -->
# Lấy trạng thái ủy quyền của đối tác Brand Safety (Get the authorization status of a Brand Safety partner)
> Đường dẫn: API Reference > Tools > Get the authorization status of a Brand Safety partner
Sử dụng endpoint này để lấy thông tin the  authorization status of your Brand Safety partner. 
* For Zefr, please go to [https://measurement.zefr.com/tiktok/connect](https://measurement.zefr.com/tiktok/connect) to complete setup.

## Yêu cầu gọi API (Request)

**Endpoint**
https://business-api.tiktok.com/open_api/v1.3/tool/brand_safety/partner/authorize/status/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id  ****(Bắt buộc)**** | string | ID tài khoản quảng cáo TikTok |
| partner  ****(Bắt buộc)**** | string | Brand Safety post bid measurement partner. Các giá trị enum hỗ trợ: `Zefr`. |

### Ví dụ lệnh cURL (Example)

```http
// curl
curl --get -H "Access-Token:xxx" \
--data-urlencode "advertiser_id=ADVERTISER_ID" \
--data-urlencode "partner=PARTNER" \
https://business-api.tiktok.com/open_api/v1.3/tool/brand_safety/partner/authorize/status/
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Response code. For the complete list of response codes and descriptions, see [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| data | object | Returned data. |
| ↳ status | string | Authorization status. Các giá trị enum hỗ trợ: `OK`, `NOT_FOUND`. |
| request_id | string | Mã nhật ký yêu cầu (request log ID) để định danh duy nhất cho mỗi lượt gọi API. |

### Ví dụ lệnh cURL (Example)

```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "202105120919540102360412202805EB06",
    "data": {
        "status": "OK"
    }
}
```

---

<a id="doc-1755436556897281"></a>
<!-- doc_id: 1755436556897281 -->
<!-- doc_id: 1755436556897281 -->
# (Đã lỗi thời) Lấy đối tác đo lường bên thứ ba post-bid khả dụng ((Deprecated) Get available post-bid third-party measurement partners)
> Đường dẫn: API Reference > Tools > (Deprecated) Get available post-bid third-party measurement partners
Sử dụng endpoint này để lấy thông tin available post-bid third-party measurement partners, and the reason why you cannot choose a certain partner.

## Yêu cầu gọi API (Request)

**Endpoint** `https://business-api.tiktok.com/open_api/v1.3/tool/vast_option/`

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type  ****(Bắt buộc)**** | string | Định dạng dữ liệu yêu cầu ⏎ Allowed format:`application/json` |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id  ****(Bắt buộc)**** | string | ID tài khoản quảng cáo TikTok |
| objective_type  ****(Bắt buộc)**** | string | Mục tiêu quảng cáo của bạn. Xem chi tiết tại [Mục tiêu quảng cáo](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1737585562434561). |
| region_codes | string[] | List of country or region codes. For example: `["US", "JP", "KR"]`. ⏎ See [Appendix - Location code](../15-appendix/phu-luc-p1.md#doc-1737585867307010) for enum values. |
| brand_safety_type | string | Loại an toàn thương hiệu (Brand safety type). The allowed Các giá trị enum hỗ trợ: • `STANDARD_INVENTORY`: Use TikTok's brand safety solution. Standard inventory means that ads will appear next to content that is appropriate for most brands.  • `LIMITED_INVENTORY`: Use TikTok's brand safety solution. Limited inventory means that your ads will not appear next to content that contains mature themes.  To get the countries and regions that your ads can be deployed to based on your brand safety settings, use the [/tool/region/](70-tools-p1.md#doc-1737189539571713) endpoint. |

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Phụ lục - Mã lỗi trả về](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi từ hệ thống. Xem [Phụ lục - Mã lỗi trả về](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | Mã nhật ký yêu cầu (request log ID) để định danh duy nhất cho mỗi lượt gọi API. |
| data | object | Returned data. |
| ↳ option_list | object[] | The list of post-bid third-party measurement partners. |
| ↳↳ partner | string | Post-bid third-party brand safety or viewability measurement partner. Các giá trị enum hỗ trợ: `MOAT`, `DOUBLE_VERIFY`, `IAS`, `ZEFR`. ⏎ You can set post-bid third-party measurement partners at the ad level via `viewability_postbid_partner` and `brand_safety_postbid_partner` when calling [/ad/create/](02-ads-p1.md#doc-1739953377508354). |
| ↳↳ partner_name | string | Name of the post-bid third-party brand safety or viewability measurement partner. |
| ↳↳ vast_type | string | The type of post-bid third-party measurement that the partner offers. Các giá trị enum hỗ trợ: `VIEWABILITY` (viewability measurement), `BRAND_SAFETY` (brand safety measurement). |
| ↳↳ is_require_url | boolean | Liệu you need to provide a VAST URL when you choose the post-bid third-party measurement partner. |
| ↳↳ is_available | boolean | Liệu you can choose the post-bid third-party measurement partner when creating or updating ads. |
| ↳↳ unavailable_reason | object[] | The information about why you cannot select the post-bid third-party measurement partner. Returned when `is_available` = `False`. |
| ↳↳↳ reason | string | The reason why you cannot choose the post-bid third-party measurement partner. |
| ↳↳↳ reason_type | string | The reason type. Các giá trị enum hỗ trợ: • `UNSUPPORTED_PARTNER`: You are not authorized to choose this partner.  • `UNSUPPORTED_OBJ_TYPE`: The partner is not supported for the specified advertising objective.  • `UNSUPPORTED_COUNTRY`: The partner is not supported for one or more of the specified country or region codes.  • `UNSUPPORTED_PREBID`: The partner is not supported for post-bid third-party measurement because of your pre-bid brand safety setting via `brand_safety_type` in the request. |

---

<a id="doc-1774487686007810"></a>
<!-- doc_id: 1774487686007810 -->
<!-- doc_id: 1774487686007810 -->
# Lấy kết quả xác minh URL (Get the verification results of a URL)
> Đường dẫn: API Reference > Tools > Get the verification results of a URL
Sử dụng endpoint này để kiểm tra Liệu a URL is a custom URL scheme, Apple’s universal link, or Android App Link, and Liệu URL is valid.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/tool/url_validate/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
| advertiser_id ***(Bắt buộc)*** | string | ID tài khoản quảng cáo TikTok. |
| url ***(Bắt buộc)*** | string | The URL that you want to get verification results for. |
### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/tool/url_validate/?advertiser_id={{advertiser_id}}&url={{url}}' \
--header 'Access-Token: {{Access-Token}}' \
```
## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|-|-|-|
|code |number|Response code. For the complete list of response codes and descriptions, see [Appendix-Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message|string|Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|request_id |string|Mã nhật ký yêu cầu (request log ID) để định danh duy nhất cho mỗi lượt gọi API.  |
|data |object|Returned data.|
#| landing_page_url_info | object | Information about the URL. |
##| validate_info | object | Information about the verification results for the URL. |
###| is_scheme_link | boolean | Liệu URL is a custom URL scheme. |
###| is_valid_url | boolean | Liệu URL is a valid URL (Apple’s universal link, Android App Link, or custom URL scheme). |
###| is_valid_scheme | boolean | Liệu URL is a valid custom URL scheme. |

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "url_info": {
            "validate_info": {
                "is_valid_scheme": true,
                "is_scheme_link": true,
                "is_valid_url": true
            }
        }
    }
}
```

---

<a id="doc-1774488637039618"></a>
<!-- doc_id: 1774488637039618 -->
<!-- doc_id: 1774488637039618 -->
# Lấy mã vùng quay số và mã quốc gia cho số điện thoại (Get region calling codes and region codes for phone numbers)
> Đường dẫn: API Reference > Tools > Get region calling codes and region codes for phone numbers
Sử dụng endpoint này để truy xuất the region codes, region names, and region calling codes for phone numbers.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/tool/phone_region_code/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
| advertiser_id ***(Bắt buộc)*** | string | ID tài khoản quảng cáo TikTok. |

### Ví dụ lệnh cURL (Example)

```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/tool/phone_region_code/?advertiser_id={{advertiser_id}}' \
--header 'Access-Token: {{Access-Token}}' \
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|-|-|-|
|code |number|Response code. For the complete list of response codes and descriptions, see [Appendix-Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message|string|Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|request_id |string|Mã nhật ký yêu cầu (request log ID) để định danh duy nhất cho mỗi lượt gọi API.  |
|data |object|Returned data.|
#| phone_region_code_infos | object[] | Information about the region codes, region names, and region calling codes for phone numbers.|
##| phone_region_name| string | The name of the region of a phone number.<br>Example: `"Austria"`. |
##| phone_region_code | string | The region code for a phone number.<br>Example: `"AT"`. |
##| phone_region_calling_code| string | The region calling code for a phone number.<br>Example: `"+43"`. |

### Ví dụ lệnh cURL (Example)

```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "phone_region_code_infos": [
            {
                "phone_region_code": "AC",
                "phone_region_name": "Antigua and Barbuda",
                "phone_region_calling_code": "+247"
            },
            {
                "phone_region_code": "AD",
                "phone_region_name": "Andorra",
                "phone_region_calling_code": "+376"
            },
            {
                "phone_region_code": "AE",
                "phone_region_name": "United Arab Emirates",
                "phone_region_calling_code": "+971"
            },
            {
                "phone_region_code": "AF",
                "phone_region_name": "Afghanistan",
                "phone_region_calling_code": "+93"
            },
            {
                "phone_region_code": "AG",
                "phone_region_name": "Antigua and Barbuda",
                "phone_region_calling_code": "+1"
            },
            {
                "phone_region_code": "AI",
                "phone_region_name": "Anguilla",
                "phone_region_calling_code": "+1"
            },
            {
                "phone_region_code": "AL",
                "phone_region_name": "Albania",
                "phone_region_calling_code": "+355"
            },
            {
                "phone_region_code": "AM",
                "phone_region_name": "Armenia",
                "phone_region_calling_code": "+374"
            },
            {
                "phone_region_code": "AO",
                "phone_region_name": "Angola",
                "phone_region_calling_code": "+244"
            },
            {
                "phone_region_code": "AR",
                "phone_region_name": "Argentina",
                "phone_region_calling_code": "+54"
            },
            {
                "phone_region_code": "AS",
                "phone_region_name": "American Samoa",
                "phone_region_calling_code": "+1"
            },
            {
                "phone_region_code": "AT",
                "phone_region_name": "Austria",
                "phone_region_calling_code": "+43"
            },
            {
                "phone_region_code": "AU",
                "phone_region_name": "Australia",
                "phone_region_calling_code": "+61"
            },
            {
                "phone_region_code": "AW",
                "phone_region_name": "Aruba",
                "phone_region_calling_code": "+297"
            },
            {
                "phone_region_code": "AX",
                "phone_region_name": "Åland Islands",
                "phone_region_calling_code": "+358"
            },
            {
                "phone_region_code": "AZ",
                "phone_region_name": "Azerbaijan",
                "phone_region_calling_code": "+994"
            },
            {
                "phone_region_code": "BA",
                "phone_region_name": "Bosnia and Herzegovina",
                "phone_region_calling_code": "+387"
            },
            {
                "phone_region_code": "BB",
                "phone_region_name": "Barbados",
                "phone_region_calling_code": "+1"
            },
            {
                "phone_region_code": "BD",
                "phone_region_name": "Bangladesh",
                "phone_region_calling_code": "+880"
            },
            {
                "phone_region_code": "BE",
                "phone_region_name": "Belgium",
                "phone_region_calling_code": "+32"
            },
            {
                "phone_region_code": "BF",
                "phone_region_name": "Burkina Faso",
                "phone_region_calling_code": "+226"
            },
            {
                "phone_region_code": "BG",
                "phone_region_name": "Bulgaria",
                "phone_region_calling_code": "+359"
            },
            {
                "phone_region_code": "BH",
                "phone_region_name": "Bahrain",
                "phone_region_calling_code": "+973"
            },
            {
                "phone_region_code": "BI",
                "phone_region_name": "Burundi",
                "phone_region_calling_code": "+257"
            },
            {
                "phone_region_code": "BJ",
                "phone_region_name": "Benin",
                "phone_region_calling_code": "+229"
            },
            {
                "phone_region_code": "BL",
                "phone_region_name": "Saint Barthélemy",
                "phone_region_calling_code": "+590"
            },
            {
                "phone_region_code": "BM",
                "phone_region_name": "Bermuda",
                "phone_region_calling_code": "+1"
            },
            {
                "phone_region_code": "BN",
                "phone_region_name": "Brunei Darussalam",
                "phone_region_calling_code": "+673"
            },
            {
                "phone_region_code": "BO",
                "phone_region_name": "Bolivia, Plurinational State of",
                "phone_region_calling_code": "+591"
            },
            {
                "phone_region_code": "BQ",
                "phone_region_name": "Bonaire, Sint Eustatius and Saba",
                "phone_region_calling_code": "+599"
            },
            {
                "phone_region_code": "BR",
                "phone_region_name": "Brazil",
                "phone_region_calling_code": "+55"
            },
            {
                "phone_region_code": "BS",
                "phone_region_name": "Bahamas",
                "phone_region_calling_code": "+1"
            },
            {
                "phone_region_code": "BT",
                "phone_region_name": "Bhutan",
                "phone_region_calling_code": "+975"
            },
            {
                "phone_region_code": "BW",
                "phone_region_name": "Botswana",
                "phone_region_calling_code": "+267"
            },
            {
                "phone_region_code": "BY",
                "phone_region_name": "Belarus",
                "phone_region_calling_code": "+375"
            },
            {
                "phone_region_code": "BZ",
                "phone_region_name": "Belize",
                "phone_region_calling_code": "+501"
            },
            {
                "phone_region_code": "CA",
                "phone_region_name": "Canada",
                "phone_region_calling_code": "+1"
            },
            {
                "phone_region_code": "CC",
                "phone_region_name": "Cocos (Keeling) Islands",
                "phone_region_calling_code": "+61"
            },
            {
                "phone_region_code": "CF",
                "phone_region_name": "Central African Republic",
                "phone_region_calling_code": "+236"
            },
            {
                "phone_region_code": "CG",
                "phone_region_name": "Congo",
                "phone_region_calling_code": "+242"
            },
            {
                "phone_region_code": "CH",
                "phone_region_name": "Switzerland",
                "phone_region_calling_code": "+41"
            },
            {
                "phone_region_code": "CK",
                "phone_region_name": "Cook Islands",
                "phone_region_calling_code": "+682"
            },
            {
                "phone_region_code": "CL",
                "phone_region_name": "Chile",
                "phone_region_calling_code": "+56"
            },
            {
                "phone_region_code": "CM",
                "phone_region_name": "Cameroon",
                "phone_region_calling_code": "+237"
            },
            {
                "phone_region_code": "CN",
                "phone_region_name": "China",
                "phone_region_calling_code": "+86"
            },
            {
                "phone_region_code": "CO",
                "phone_region_name": "Colombia",
                "phone_region_calling_code": "+57"
            },
            {
                "phone_region_code": "CR",
                "phone_region_name": "Costa Rica",
                "phone_region_calling_code": "+506"
            },
            {
                "phone_region_code": "CV",
                "phone_region_name": "Cape Verde",
                "phone_region_calling_code": "+238"
            },
            {
                "phone_region_code": "CW",
                "phone_region_name": "Curaçao",
                "phone_region_calling_code": "+599"
            },
            {
                "phone_region_code": "CX",
                "phone_region_name": "Christmas Island",
                "phone_region_calling_code": "+61"
            },
            {
                "phone_region_code": "CY",
                "phone_region_name": "Cyprus",
                "phone_region_calling_code": "+357"
            },
            {
                "phone_region_code": "CZ",
                "phone_region_name": "Czech Republic",
                "phone_region_calling_code": "+420"
            },
            {
                "phone_region_code": "DE",
                "phone_region_name": "Germany",
                "phone_region_calling_code": "+49"
            },
            {
                "phone_region_code": "DJ",
                "phone_region_name": "Djibouti",
                "phone_region_calling_code": "+253"
            },
            {
                "phone_region_code": "DK",
                "phone_region_name": "Denmark",
                "phone_region_calling_code": "+45"
            },
            {
                "phone_region_code": "DM",
                "phone_region_name": "Dominica",
                "phone_region_calling_code": "+1"
            },
            {
                "phone_region_code": "DO",
                "phone_region_name": "Dominican Republic",
                "phone_region_calling_code": "+1"
            },
            {
                "phone_region_code": "DZ",
                "phone_region_name": "Algeria",
                "phone_region_calling_code": "+213"
            },
            {
                "phone_region_code": "EC",
                "phone_region_name": "Ecuador",
                "phone_region_calling_code": "+593"
            },
            {
                "phone_region_code": "EE",
                "phone_region_name": "Estonia",
                "phone_region_calling_code": "+372"
            },
            {
                "phone_region_code": "EG",
                "phone_region_name": "Egypt",
                "phone_region_calling_code": "+20"
            },
            {
                "phone_region_code": "EH",
                "phone_region_name": "Western Sahara",
                "phone_region_calling_code": "+212"
            },
            {
                "phone_region_code": "ER",
                "phone_region_name": "Eritrea",
                "phone_region_calling_code": "+291"
            },
            {
                "phone_region_code": "ES",
                "phone_region_name": "Spain",
                "phone_region_calling_code": "+34"
            },
            {
                "phone_region_code": "ET",
                "phone_region_name": "Ethiopia",
                "phone_region_calling_code": "+251"
            },
            {
                "phone_region_code": "FI",
                "phone_region_name": "Finland",
                "phone_region_calling_code": "+358"
            },
            {
                "phone_region_code": "FJ",
                "phone_region_name": "Fiji",
                "phone_region_calling_code": "+679"
            },
            {
                "phone_region_code": "FK",
                "phone_region_name": "Falkland Islands (Malvinas)",
                "phone_region_calling_code": "+500"
            },
            {
                "phone_region_code": "FM",
                "phone_region_name": "Micronesia, Federated States of",
                "phone_region_calling_code": "+691"
            },
            {
                "phone_region_code": "FO",
                "phone_region_name": "Faroe Islands",
                "phone_region_calling_code": "+298"
            },
            {
                "phone_region_code": "FR",
                "phone_region_name": "France",
                "phone_region_calling_code": "+33"
            },
            {
                "phone_region_code": "GA",
                "phone_region_name": "Gabon",
                "phone_region_calling_code": "+241"
            },
            {
                "phone_region_code": "GD",
                "phone_region_name": "Grenada",
                "phone_region_calling_code": "+1"
            },
            {
                "phone_region_code": "GE",
                "phone_region_name": "Georgia",
                "phone_region_calling_code": "+995"
            },
            {
                "phone_region_code": "GF",
                "phone_region_name": "French Guiana",
                "phone_region_calling_code": "+594"
            },
            {
                "phone_region_code": "GG",
                "phone_region_name": "Guernsey",
                "phone_region_calling_code": "+44"
            },
            {
                "phone_region_code": "GH",
                "phone_region_name": "Ghana",
                "phone_region_calling_code": "+233"
            },
            {
                "phone_region_code": "GI",
                "phone_region_name": "Gibraltar",
                "phone_region_calling_code": "+350"
            },
            {
                "phone_region_code": "GL",
                "phone_region_name": "Greenland",
                "phone_region_calling_code": "+299"
            },
            {
                "phone_region_code": "GM",
                "phone_region_name": "Gambia",
                "phone_region_calling_code": "+220"
            },
            {
                "phone_region_code": "GN",
                "phone_region_name": "Guinea",
                "phone_region_calling_code": "+224"
            },
            {
                "phone_region_code": "GP",
                "phone_region_name": "Guadeloupe",
                "phone_region_calling_code": "+590"
            },
            {
                "phone_region_code": "GQ",
                "phone_region_name": "Equatorial Guinea",
                "phone_region_calling_code": "+240"
            },
            {
                "phone_region_code": "GR",
                "phone_region_name": "Greece",
                "phone_region_calling_code": "+30"
            },
            {
                "phone_region_code": "GT",
                "phone_region_name": "Guatemala",
                "phone_region_calling_code": "+502"
            },
            {
                "phone_region_code": "GU",
                "phone_region_name": "Guam",
                "phone_region_calling_code": "+1"
            },
            {
                "phone_region_code": "GW",
                "phone_region_name": "Guinea-Bissau",
                "phone_region_calling_code": "+245"
            },
            {
                "phone_region_code": "GY",
                "phone_region_name": "Guyana",
                "phone_region_calling_code": "+592"
            },
            {
                "phone_region_code": "HK",
                "phone_region_name": "Hong Kong",
                "phone_region_calling_code": "+852"
            },
            {
                "phone_region_code": "HN",
                "phone_region_name": "Honduras",
                "phone_region_calling_code": "+504"
            },
            {
                "phone_region_code": "HR",
                "phone_region_name": "Croatia",
                "phone_region_calling_code": "+385"
            },
            {
                "phone_region_code": "HT",
                "phone_region_name": "Haiti",
                "phone_region_calling_code": "+509"
            },
            {
                "phone_region_code": "HU",
                "phone_region_name": "Hungary",
                "phone_region_calling_code": "+36"
            },
            {
                "phone_region_code": "ID",
                "phone_region_name": "Indonesia",
                "phone_region_calling_code": "+62"
            },
            {
                "phone_region_code": "IE",
                "phone_region_name": "Ireland",
                "phone_region_calling_code": "+353"
            },
            {
                "phone_region_code": "IL",
                "phone_region_name": "Israel",
                "phone_region_calling_code": "+972"
            },
            {
                "phone_region_code": "IM",
                "phone_region_name": "Isle of Man",
                "phone_region_calling_code": "+44"
            },
            {
                "phone_region_code": "IN",
                "phone_region_name": "India",
                "phone_region_calling_code": "+91"
            },
            {
                "phone_region_code": "IO",
                "phone_region_name": "British Indian Ocean Territory",
                "phone_region_calling_code": "+246"
            },
            {
                "phone_region_code": "IQ",
                "phone_region_name": "Iraq",
                "phone_region_calling_code": "+964"
            },
            {
                "phone_region_code": "IS",
                "phone_region_name": "Iceland",
                "phone_region_calling_code": "+354"
            },
            {
                "phone_region_code": "IT",
                "phone_region_name": "Italy",
                "phone_region_calling_code": "+39"
            },
            {
                "phone_region_code": "JE",
                "phone_region_name": "Jersey",
                "phone_region_calling_code": "+44"
            },
            {
                "phone_region_code": "JM",
                "phone_region_name": "Jamaica",
                "phone_region_calling_code": "+1"
            },
            {
                "phone_region_code": "JO",
                "phone_region_name": "Jordan",
                "phone_region_calling_code": "+962"
            },
            {
                "phone_region_code": "JP",
                "phone_region_name": "Japan",
                "phone_region_calling_code": "+81"
            },
            {
                "phone_region_code": "KE",
                "phone_region_name": "Kenya",
                "phone_region_calling_code": "+254"
            },
            {
                "phone_region_code": "KG",
                "phone_region_name": "Kyrgyzstan",
                "phone_region_calling_code": "+996"
            },
            {
                "phone_region_code": "KH",
                "phone_region_name": "Cambodia",
                "phone_region_calling_code": "+855"
            },
            {
                "phone_region_code": "KI",
                "phone_region_name": "Kiribati",
                "phone_region_calling_code": "+686"
            },
            {
                "phone_region_code": "KM",
                "phone_region_name": "Comoros",
                "phone_region_calling_code": "+269"
            },
            {
                "phone_region_code": "KN",
                "phone_region_name": "Saint Kitts and Nevis",
                "phone_region_calling_code": "+1"
            },
            {
                "phone_region_code": "KR",
                "phone_region_name": "Korea, Republic of",
                "phone_region_calling_code": "+82"
            },
            {
                "phone_region_code": "KW",
                "phone_region_name": "Kuwait",
                "phone_region_calling_code": "+965"
            },
            {
                "phone_region_code": "KY",
                "phone_region_name": "Cayman Islands",
                "phone_region_calling_code": "+1"
            },
            {
                "phone_region_code": "KZ",
                "phone_region_name": "Kazakhstan",
                "phone_region_calling_code": "+7"
            },
            {
                "phone_region_code": "LA",
                "phone_region_name": "Lao People's Democratic Republic",
                "phone_region_calling_code": "+856"
            },
            {
                "phone_region_code": "LB",
                "phone_region_name": "Lebanon",
                "phone_region_calling_code": "+961"
            },
            {
                "phone_region_code": "LC",
                "phone_region_name": "Saint Lucia",
                "phone_region_calling_code": "+1"
            },
            {
                "phone_region_code": "LI",
                "phone_region_name": "Liechtenstein",
                "phone_region_calling_code": "+423"
            },
            {
                "phone_region_code": "LK",
                "phone_region_name": "Sri Lanka",
                "phone_region_calling_code": "+94"
            },
            {
                "phone_region_code": "LS",
                "phone_region_name": "Lesotho",
                "phone_region_calling_code": "+266"
            },
            {
                "phone_region_code": "LT",
                "phone_region_name": "Lithuania",
                "phone_region_calling_code": "+370"
            },
            {
                "phone_region_code": "LU",
                "phone_region_name": "Luxembourg",
                "phone_region_calling_code": "+352"
            },
            {
                "phone_region_code": "LV",
                "phone_region_name": "Latvia",
                "phone_region_calling_code": "+371"
            },
            {
                "phone_region_code": "LY",
                "phone_region_name": "Libya",
                "phone_region_calling_code": "+218"
            },
            {
                "phone_region_code": "MA",
                "phone_region_name": "Morocco",
                "phone_region_calling_code": "+212"
            },
            {
                "phone_region_code": "MC",
                "phone_region_name": "Monaco",
                "phone_region_calling_code": "+377"
            },
            {
                "phone_region_code": "MD",
                "phone_region_name": "Moldova, Republic of",
                "phone_region_calling_code": "+373"
            },
            {
                "phone_region_code": "ME",
                "phone_region_name": "Montenegro",
                "phone_region_calling_code": "+382"
            },
            {
                "phone_region_code": "MF",
                "phone_region_name": "Saint Martin (French part)",
                "phone_region_calling_code": "+590"
            },
            {
                "phone_region_code": "MG",
                "phone_region_name": "Madagascar",
                "phone_region_calling_code": "+261"
            },
            {
                "phone_region_code": "MH",
                "phone_region_name": "Marshall Islands",
                "phone_region_calling_code": "+692"
            },
            {
                "phone_region_code": "MK",
                "phone_region_name": "Macedonia, the Former Yugoslav Republic of",
                "phone_region_calling_code": "+389"
            },
            {
                "phone_region_code": "ML",
                "phone_region_name": "Mali",
                "phone_region_calling_code": "+223"
            },
            {
                "phone_region_code": "MN",
                "phone_region_name": "Mongolia",
                "phone_region_calling_code": "+976"
            },
            {
                "phone_region_code": "MO",
                "phone_region_name": "Macao",
                "phone_region_calling_code": "+853"
            },
            {
                "phone_region_code": "MP",
                "phone_region_name": "Northern Mariana Islands",
                "phone_region_calling_code": "+1"
            },
            {
                "phone_region_code": "MQ",
                "phone_region_name": "Martinique",
                "phone_region_calling_code": "+596"
            },
            {
                "phone_region_code": "MR",
                "phone_region_name": "Mauritania",
                "phone_region_calling_code": "+222"
            },
            {
                "phone_region_code": "MS",
                "phone_region_name": "Montserrat",
                "phone_region_calling_code": "+1"
            },
            {
                "phone_region_code": "MT",
                "phone_region_name": "Malta",
                "phone_region_calling_code": "+356"
            },
            {
                "phone_region_code": "MU",
                "phone_region_name": "Mauritius",
                "phone_region_calling_code": "+230"
            },
            {
                "phone_region_code": "MV",
                "phone_region_name": "Maldives",
                "phone_region_calling_code": "+960"
            },
            {
                "phone_region_code": "MW",
                "phone_region_name": "Malawi",
                "phone_region_calling_code": "+265"
            },
            {
                "phone_region_code": "MX",
                "phone_region_name": "Mexico",
                "phone_region_calling_code": "+52"
            },
            {
                "phone_region_code": "MY",
                "phone_region_name": "Malaysia",
                "phone_region_calling_code": "+60"
            },
            {
                "phone_region_code": "MZ",
                "phone_region_name": "Mozambique",
                "phone_region_calling_code": "+258"
            },
            {
                "phone_region_code": "NA",
                "phone_region_name": "Namibia",
                "phone_region_calling_code": "+264"
            },
            {
                "phone_region_code": "NC",
                "phone_region_name": "New Caledonia",
                "phone_region_calling_code": "+687"
            },
            {
                "phone_region_code": "NE",
                "phone_region_name": "Niger",
                "phone_region_calling_code": "+227"
            },
            {
                "phone_region_code": "NF",
                "phone_region_name": "Norfolk Island",
                "phone_region_calling_code": "+672"
            },
            {
                "phone_region_code": "NG",
                "phone_region_name": "Nigeria",
                "phone_region_calling_code": "+234"
            },
            {
                "phone_region_code": "NI",
                "phone_region_name": "Nicaragua",
                "phone_region_calling_code": "+505"
            },
            {
                "phone_region_code": "NL",
                "phone_region_name": "Netherlands",
                "phone_region_calling_code": "+31"
            },
            {
                "phone_region_code": "NO",
                "phone_region_name": "Norway",
                "phone_region_calling_code": "+47"
            },
            {
                "phone_region_code": "NP",
                "phone_region_name": "Nepal",
                "phone_region_calling_code": "+977"
            },
            {
                "phone_region_code": "NR",
                "phone_region_name": "Nauru",
                "phone_region_calling_code": "+674"
            },
            {
                "phone_region_code": "NU",
                "phone_region_name": "Niue",
                "phone_region_calling_code": "+683"
            },
            {
                "phone_region_code": "NZ",
                "phone_region_name": "New Zealand",
                "phone_region_calling_code": "+64"
            },
            {
                "phone_region_code": "OM",
                "phone_region_name": "Oman",
                "phone_region_calling_code": "+968"
            },
            {
                "phone_region_code": "PA",
                "phone_region_name": "Panama",
                "phone_region_calling_code": "+507"
            },
            {
                "phone_region_code": "PE",
                "phone_region_name": "Peru",
                "phone_region_calling_code": "+51"
            },
            {
                "phone_region_code": "PF",
                "phone_region_name": "French Polynesia",
                "phone_region_calling_code": "+689"
            },
            {
                "phone_region_code": "PG",
                "phone_region_name": "Papua New Guinea",
                "phone_region_calling_code": "+675"
            },
            {
                "phone_region_code": "PH",
                "phone_region_name": "Philippines",
                "phone_region_calling_code": "+63"
            },
            {
                "phone_region_code": "PK",
                "phone_region_name": "Pakistan",
                "phone_region_calling_code": "+92"
            },
            {
                "phone_region_code": "PL",
                "phone_region_name": "Poland",
                "phone_region_calling_code": "+48"
            },
            {
                "phone_region_code": "PM",
                "phone_region_name": "Saint Pierre and Miquelon",
                "phone_region_calling_code": "+508"
            },
            {
                "phone_region_code": "PR",
                "phone_region_name": "Puerto Rico",
                "phone_region_calling_code": "+1"
            },
            {
                "phone_region_code": "PS",
                "phone_region_name": "Palestine, State of",
                "phone_region_calling_code": "+970"
            },
            {
                "phone_region_code": "PT",
                "phone_region_name": "Portugal",
                "phone_region_calling_code": "+351"
            },
            {
                "phone_region_code": "PW",
                "phone_region_name": "Palau",
                "phone_region_calling_code": "+680"
            },
            {
                "phone_region_code": "PY",
                "phone_region_name": "Paraguay",
                "phone_region_calling_code": "+595"
            },
            {
                "phone_region_code": "QA",
                "phone_region_name": "Qatar",
                "phone_region_calling_code": "+974"
            },
            {
                "phone_region_code": "RE",
                "phone_region_name": "Réunion",
                "phone_region_calling_code": "+262"
            },
            {
                "phone_region_code": "RO",
                "phone_region_name": "Romania",
                "phone_region_calling_code": "+40"
            },
            {
                "phone_region_code": "RS",
                "phone_region_name": "Serbia",
                "phone_region_calling_code": "+381"
            },
            {
                "phone_region_code": "RU",
                "phone_region_name": "Russian Federation",
                "phone_region_calling_code": "+7"
            },
            {
                "phone_region_code": "RW",
                "phone_region_name": "Rwanda",
                "phone_region_calling_code": "+250"
            },
            {
                "phone_region_code": "SA",
                "phone_region_name": "Saudi Arabia",
                "phone_region_calling_code": "+966"
            },
            {
                "phone_region_code": "SB",
                "phone_region_name": "Solomon Islands",
                "phone_region_calling_code": "+677"
            },
            {
                "phone_region_code": "SC",
                "phone_region_name": "Seychelles",
                "phone_region_calling_code": "+248"
            },
            {
                "phone_region_code": "SE",
                "phone_region_name": "Sweden",
                "phone_region_calling_code": "+46"
            },
            {
                "phone_region_code": "SG",
                "phone_region_name": "Singapore",
                "phone_region_calling_code": "+65"
            },
            {
                "phone_region_code": "SH",
                "phone_region_name": "Saint Helena, Ascension and Tristan da Cunha",
                "phone_region_calling_code": "+290"
            },
            {
                "phone_region_code": "SI",
                "phone_region_name": "Slovenia",
                "phone_region_calling_code": "+386"
            },
            {
                "phone_region_code": "SJ",
                "phone_region_name": "Svalbard and Jan Mayen",
                "phone_region_calling_code": "+47"
            },
            {
                "phone_region_code": "SK",
                "phone_region_name": "Slovakia",
                "phone_region_calling_code": "+421"
            },
            {
                "phone_region_code": "SL",
                "phone_region_name": "Sierra Leone",
                "phone_region_calling_code": "+232"
            },
            {
                "phone_region_code": "SM",
                "phone_region_name": "San Marino",
                "phone_region_calling_code": "+378"
            },
            {
                "phone_region_code": "SN",
                "phone_region_name": "Senegal",
                "phone_region_calling_code": "+221"
            },
            {
                "phone_region_code": "SO",
                "phone_region_name": "Somalia",
                "phone_region_calling_code": "+252"
            },
            {
                "phone_region_code": "SR",
                "phone_region_name": "Suriname",
                "phone_region_calling_code": "+597"
            },
            {
                "phone_region_code": "SS",
                "phone_region_name": "South Sudan",
                "phone_region_calling_code": "+211"
            },
            {
                "phone_region_code": "ST",
                "phone_region_name": "Sao Tome and Principe",
                "phone_region_calling_code": "+239"
            },
            {
                "phone_region_code": "SV",
                "phone_region_name": "El Salvador",
                "phone_region_calling_code": "+503"
            },
            {
                "phone_region_code": "SX",
                "phone_region_name": "Sint Maarten (Dutch part)",
                "phone_region_calling_code": "+1"
            },
            {
                "phone_region_code": "SZ",
                "phone_region_name": "Swaziland",
                "phone_region_calling_code": "+268"
            },
            {
                "phone_region_code": "TC",
                "phone_region_name": "Turks and Caicos Islands",
                "phone_region_calling_code": "+1"
            },
            {
                "phone_region_code": "TD",
                "phone_region_name": "Chad",
                "phone_region_calling_code": "+235"
            },
            {
                "phone_region_code": "TG",
                "phone_region_name": "Togo",
                "phone_region_calling_code": "+228"
            },
            {
                "phone_region_code": "TH",
                "phone_region_name": "Thailand",
                "phone_region_calling_code": "+66"
            },
            {
                "phone_region_code": "TJ",
                "phone_region_name": "Tajikistan",
                "phone_region_calling_code": "+992"
            },
            {
                "phone_region_code": "TK",
                "phone_region_name": "Tokelau",
                "phone_region_calling_code": "+690"
            },
            {
                "phone_region_code": "TL",
                "phone_region_name": "Timor-Leste",
                "phone_region_calling_code": "+670"
            },
            {
                "phone_region_code": "TM",
                "phone_region_name": "Turkmenistan",
                "phone_region_calling_code": "+993"
            },
            {
                "phone_region_code": "TN",
                "phone_region_name": "Tunisia",
                "phone_region_calling_code": "+216"
            },
            {
                "phone_region_code": "TO",
                "phone_region_name": "Tonga",
                "phone_region_calling_code": "+676"
            },
            {
                "phone_region_code": "TR",
                "phone_region_name": "Turkey",
                "phone_region_calling_code": "+90"
            },
            {
                "phone_region_code": "TT",
                "phone_region_name": "Trinidad and Tobago",
                "phone_region_calling_code": "+1"
            },
            {
                "phone_region_code": "TV",
                "phone_region_name": "Tuvalu",
                "phone_region_calling_code": "+688"
            },
            {
                "phone_region_code": "TW",
                "phone_region_name": "Taiwan",
                "phone_region_calling_code": "+886"
            },
            {
                "phone_region_code": "TZ",
                "phone_region_name": "Tanzania, United Republic of",
                "phone_region_calling_code": "+255"
            },
            {
                "phone_region_code": "UA",
                "phone_region_name": "Ukraine",
                "phone_region_calling_code": "+380"
            },
            {
                "phone_region_code": "UG",
                "phone_region_name": "Uganda",
                "phone_region_calling_code": "+256"
            },
            {
                "phone_region_code": "UK",
                "phone_region_name": "United Kingdom",
                "phone_region_calling_code": "+44"
            },
            {
                "phone_region_code": "US",
                "phone_region_name": "United States",
                "phone_region_calling_code": "+1"
            },
            {
                "phone_region_code": "UY",
                "phone_region_name": "Uruguay",
                "phone_region_calling_code": "+598"
            },
            {
                "phone_region_code": "UZ",
                "phone_region_name": "Uzbekistan",
                "phone_region_calling_code": "+998"
            },
            {
                "phone_region_code": "VA",
                "phone_region_name": "Holy See (Vatican City State)",
                "phone_region_calling_code": "+39"
            },
            {
                "phone_region_code": "VC",
                "phone_region_name": "Saint Vincent and the Grenadines",
                "phone_region_calling_code": "+1"
            },
            {
                "phone_region_code": "VE",
                "phone_region_name": "Venezuela, Bolivarian Republic of",
                "phone_region_calling_code": "+58"
            },
            {
                "phone_region_code": "VG",
                "phone_region_name": "Virgin Islands, British",
                "phone_region_calling_code": "+1"
            },
            {
                "phone_region_code": "VI",
                "phone_region_name": "Virgin Islands, U.S.",
                "phone_region_calling_code": "+1"
            },
            {
                "phone_region_code": "VN",
                "phone_region_name": "Viet Nam",
                "phone_region_calling_code": "+84"
            },
            {
                "phone_region_code": "VU",
                "phone_region_name": "Vanuatu",
                "phone_region_calling_code": "+678"
            },
            {
                "phone_region_code": "WF",
                "phone_region_name": "Wallis and Futuna",
                "phone_region_calling_code": "+681"
            },
            {
                "phone_region_code": "WS",
                "phone_region_name": "Samoa",
                "phone_region_calling_code": "+685"
            },
            {
                "phone_region_code": "XK",
                "phone_region_name": "Kosovo",
                "phone_region_calling_code": "+383"
            },
            {
                "phone_region_code": "YE",
                "phone_region_name": "Yemen",
                "phone_region_calling_code": "+967"
            },
            {
                "phone_region_code": "YT",
                "phone_region_name": "Mayotte",
                "phone_region_calling_code": "+262"
            },
            {
                "phone_region_code": "ZA",
                "phone_region_name": "South Africa",
                "phone_region_calling_code": "+27"
            },
            {
                "phone_region_code": "ZM",
                "phone_region_name": "Zambia",
                "phone_region_calling_code": "+260"
            },
            {
                "phone_region_code": "GB",
                "phone_region_name": "United Kingdom",
                "phone_region_calling_code": "+44"
            }
        ]
    }
}
```

---

<a id="doc-1738455961470977"></a>
<!-- doc_id: 1738455961470977 -->
<!-- doc_id: 1738455961470977 -->
# Lấy danh sách múi giờ (Get time zones)
> Đường dẫn: API Reference > Tools > Get time zones
Sử dụng endpoint này để lấy thông tin time zone enumeration values, and their offsets from GMT.

Lưu ý các độ lệch trả về (`gmt_offset`) là cố định và không tính đến thay đổi giờ mùa hè. Ví dụ, với New York (`America/New_York`), độ lệch luôn là `GMT-05:00`, bất kể New York hiện có đang áp dụng giờ mùa hè hay không.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/tool/timezone/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id  ****(Bắt buộc)**** | string | ID tài khoản quảng cáo TikTok |

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request GET https://business-api.tiktok.com/open_api/v1.3/tool/timezone/?advertiser_id={{advertiser_id}}
--header 'Access-Token: {{Access-Token}}'
--header 'Content-Type: application/json'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | The Mã trạng thái phản hồi (0: Thành công). For the complete list of error codes and descriptions, see [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | The Thông điệp phản hồi từ máy chủ. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | Mã nhật ký yêu cầu (request log ID) để định danh duy nhất cho mỗi lượt gọi API. |
| data | object | Returned data. |
| ↳ timezones | object[] | Time Zone list. |
| ↳↳ timezone | string | Múi giờ. Ví dụ: "Pacific/Auckland". |
| ↳↳ gmt_offset | string | Offset from GMT. For example, "GMT+12:00". |

### Ví dụ lệnh cURL (Example)

```JSON
// JSON
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "202107161139170102310210720317DD89",
    "data": {
        "timezones": [
            {
                "gmt_offset": "GMT+12:00",
                "timezone": "Pacific/Auckland"
            },
            {
                "gmt_offset": "GMT+12:00",
                "timezone": "Pacific/Majuro"
            },
            {
                "gmt_offset": "GMT+11:00",
                "timezone": "Asia/Magadan"
            },
            {
                "gmt_offset": "GMT+12:00",
                "timezone": "Asia/Kamchatka"
            },
            {
                "gmt_offset": "GMT+10:00",
                "timezone": "Australia/Sydney"
            },
            {
                "gmt_offset": "GMT+10:00",
                "timezone": "Asia/Vladivostok"
            },
            {
                "gmt_offset": "GMT+09:00",
                "timezone": "Australia/Broken_Hill"
            },
            {
                "gmt_offset": "GMT+09:00",
                "timezone": "Asia/Jayapura"
            },
            {
                "gmt_offset": "GMT+09:00",
                "timezone": "Asia/Tokyo"
            },
            {
                "gmt_offset": "GMT+09:00",
                "timezone": "Asia/Seoul"
            },
            {
                "gmt_offset": "GMT+09:00",
                "timezone": "Asia/Yakutsk"
            },
            {
                "gmt_offset": "GMT+08:00",
                "timezone": "Australia/Perth"
            },
            {
                "gmt_offset": "GMT+08:00",
                "timezone": "Asia/Shanghai"
            },
            {
                "gmt_offset": "GMT+08:00",
                "timezone": "Asia/Hong_Kong"
            },
            {
                "gmt_offset": "GMT+08:00",
                "timezone": "Asia/Makassar"
            },
            {
                "gmt_offset": "GMT+08:00",
                "timezone": "Asia/Kuala_Lumpur"
            },
            {
                "gmt_offset": "GMT+08:00",
                "timezone": "Asia/Manila"
            },
            {
                "gmt_offset": "GMT+08:00",
                "timezone": "Asia/Irkutsk"
            },
            {
                "gmt_offset": "GMT+08:00",
                "timezone": "Asia/Singapore"
            },
            {
                "gmt_offset": "GMT+08:00",
                "timezone": "Asia/Taipei"
            },
            {
                "gmt_offset": "GMT+07:00",
                "timezone": "Asia/Jakarta"
            },
            {
                "gmt_offset": "GMT+07:00",
                "timezone": "Asia/Krasnoyarsk"
            },
            {
                "gmt_offset": "GMT+07:00",
                "timezone": "Asia/Bangkok"
            },
            {
                "gmt_offset": "GMT+07:00",
                "timezone": "Asia/Ho_Chi_Minh"
            },
            {
                "gmt_offset": "GMT+06:00",
                "timezone": "Asia/Dhaka"
            },
            {
                "gmt_offset": "GMT+06:00",
                "timezone": "Asia/Omsk"
            },
            {
                "gmt_offset": "GMT+05:30",
                "timezone": "Asia/Kolkata"
            },
            {
                "gmt_offset": "GMT+05:30",
                "timezone": "Asia/Colombo"
            },
            {
                "gmt_offset": "GMT+05:00",
                "timezone": "Indian/Maldives"
            },
            {
                "gmt_offset": "GMT+05:00",
                "timezone": "Asia/Karachi"
            },
            {
                "gmt_offset": "GMT+05:00",
                "timezone": "Asia/Yekaterinburg"
            },
            {
                "gmt_offset": "GMT+04:00",
                "timezone": "Asia/Dubai"
            },
            {
                "gmt_offset": "GMT+04:00",
                "timezone": "Indian/Mauritius"
            },
            {
                "gmt_offset": "GMT+04:00",
                "timezone": "Asia/Muscat"
            },
            {
                "gmt_offset": "GMT+03:00",
                "timezone": "Asia/Bahrain"
            },
            {
                "gmt_offset": "GMT+03:00",
                "timezone": "Asia/Baghdad"
            },
            {
                "gmt_offset": "GMT+03:00",
                "timezone": "Africa/Nairobi"
            },
            {
                "gmt_offset": "GMT+03:00",
                "timezone": "Asia/Kuwait"
            },
            {
                "gmt_offset": "GMT+03:00",
                "timezone": "Asia/Qatar"
            },
            {
                "gmt_offset": "GMT+03:00",
                "timezone": "Europe/Moscow"
            },
            {
                "gmt_offset": "GMT+04:00",
                "timezone": "Europe/Samara"
            },
            {
                "gmt_offset": "GMT+03:00",
                "timezone": "Asia/Riyadh"
            },
            {
                "gmt_offset": "GMT+02:00",
                "timezone": "Europe/Sofia"
            },
            {
                "gmt_offset": "GMT+02:00",
                "timezone": "Asia/Nicosia"
            },
            {
                "gmt_offset": "GMT+02:00",
                "timezone": "Europe/Tallinn"
            },
            {
                "gmt_offset": "GMT+02:00",
                "timezone": "Africa/Cairo"
            },
            {
                "gmt_offset": "GMT+02:00",
                "timezone": "Europe/Helsinki"
            },
            {
                "gmt_offset": "GMT+02:00",
                "timezone": "Europe/Athens"
            },
            {
                "gmt_offset": "GMT+02:00",
                "timezone": "Asia/Jerusalem"
            },
            {
                "gmt_offset": "GMT+02:00",
                "timezone": "Asia/Amman"
            },
            {
                "gmt_offset": "GMT+02:00",
                "timezone": "Asia/Beirut"
            },
            {
                "gmt_offset": "GMT+02:00",
                "timezone": "Europe/Vilnius"
            },
            {
                "gmt_offset": "GMT+02:00",
                "timezone": "Europe/Riga"
            },
            {
                "gmt_offset": "GMT+02:00",
                "timezone": "Asia/Gaza"
            },
            {
                "gmt_offset": "GMT+02:00",
                "timezone": "Europe/Bucharest"
            },
            {
                "gmt_offset": "GMT+02:00",
                "timezone": "Europe/Kaliningrad"
            },
            {
                "gmt_offset": "GMT+03:00",
                "timezone": "Europe/Istanbul"
            },
            {
                "gmt_offset": "GMT+02:00",
                "timezone": "Europe/Kiev"
            },
            {
                "gmt_offset": "GMT+02:00",
                "timezone": "Africa/Johannesburg"
            },
            {
                "gmt_offset": "GMT+01:00",
                "timezone": "Europe/Vienna"
            },
            {
                "gmt_offset": "GMT+01:00",
                "timezone": "Europe/Sarajevo"
            },
            {
                "gmt_offset": "GMT+01:00",
                "timezone": "Europe/Brussels"
            },
            {
                "gmt_offset": "GMT+01:00",
                "timezone": "Europe/Zurich"
            },
            {
                "gmt_offset": "GMT+01:00",
                "timezone": "Europe/Prague"
            },
            {
                "gmt_offset": "GMT+01:00",
                "timezone": "Europe/Berlin"
            },
            {
                "gmt_offset": "GMT+01:00",
                "timezone": "Europe/Copenhagen"
            },
            {
                "gmt_offset": "GMT+01:00",
                "timezone": "Europe/Madrid"
            },
            {
                "gmt_offset": "GMT+01:00",
                "timezone": "Europe/Paris"
            },
            {
                "gmt_offset": "GMT+01:00",
                "timezone": "Europe/Zagreb"
            },
            {
                "gmt_offset": "GMT+01:00",
                "timezone": "Europe/Budapest"
            },
            {
                "gmt_offset": "GMT+01:00",
                "timezone": "Europe/Rome"
            },
            {
                "gmt_offset": "GMT+01:00",
                "timezone": "Europe/Luxembourg"
            },
            {
                "gmt_offset": "GMT+01:00",
                "timezone": "Europe/Skopje"
            },
            {
                "gmt_offset": "GMT+01:00",
                "timezone": "Europe/Malta"
            },
            {
                "gmt_offset": "GMT+01:00",
                "timezone": "Africa/Lagos"
            },
            {
                "gmt_offset": "GMT+01:00",
                "timezone": "Europe/Amsterdam"
            },
            {
                "gmt_offset": "GMT+01:00",
                "timezone": "Europe/Oslo"
            },
            {
                "gmt_offset": "GMT+01:00",
                "timezone": "Europe/Warsaw"
            },
            {
                "gmt_offset": "GMT+01:00",
                "timezone": "Europe/Belgrade"
            },
            {
                "gmt_offset": "GMT+01:00",
                "timezone": "Europe/Stockholm"
            },
            {
                "gmt_offset": "GMT+01:00",
                "timezone": "Europe/Ljubljana"
            },
            {
                "gmt_offset": "GMT+01:00",
                "timezone": "Europe/Bratislava"
            },
            {
                "gmt_offset": "GMT+01:00",
                "timezone": "Africa/Tunis"
            },
            {
                "gmt_offset": "GMT+00:00",
                "timezone": "Atlantic/Canary"
            },
            {
                "gmt_offset": "GMT+00:00",
                "timezone": "Europe/London"
            },
            {
                "gmt_offset": "GMT+00:00",
                "timezone": "Africa/Accra"
            },
            {
                "gmt_offset": "GMT+01:00",
                "timezone": "Europe/Dublin"
            },
            {
                "gmt_offset": "GMT+00:00",
                "timezone": "Atlantic/Reykjavik"
            },
            {
                "gmt_offset": "GMT+01:00",
                "timezone": "Africa/Casablanca"
            },
            {
                "gmt_offset": "GMT+00:00",
                "timezone": "Europe/Lisbon"
            },
            {
                "gmt_offset": "GMT-01:00",
                "timezone": "Atlantic/Azores"
            },
            {
                "gmt_offset": "GMT-02:00",
                "timezone": "America/Noronha"
            },
            {
                "gmt_offset": "GMT-03:00",
                "timezone": "America/Argentina/San_Luis"
            },
			...
        ]
    }
}
```

---

<a id="doc-1738457335681026"></a>
<!-- doc_id: 1738457335681026 -->
<!-- doc_id: 1738457335681026 -->
# Lấy liên kết trong ứng dụng TikTok (Get a TikTok in-app link)
> Đường dẫn: API Reference > Tools > Get a TikTok in-app link
Sử dụng endpoint này để lấy thông tin liên kết trong ứng dụng TikTok tương ứng cho một URL TikTok công khai. Liên kết trong ứng dụng nhận được có thể được truyền vào trường `deeplink` khi tạo hoặc cập nhật quảng cáo Tiếp cận & Tần suất (Reach & Frequency).

> **Note:** TikTok In-app links is currently an allowlist-only feature. If you would like to access it, please contact your TikTok representative.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/tool/open_url/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id  ****(Bắt buộc)**** | string | ID tài khoản quảng cáo TikTok |
| url  ****(Bắt buộc)**** | string | Open URL that you want to get the internal link for. |
| url_type  ****(Bắt buộc)**** | string | Type of the open TikTok URL. Enum:  • `USER_PROFILE` • `VIDEO`: Video detail page • `HASHTAG_CHALLENGE`: Hashtag challenge page • `MUSIC`: Music page • `STICKER`: Sticker (special effect) page • `STICKER_SHOOTER`: Shoot a video with a sticker (special effect). |

### Ví dụ lệnh cURL (Example)

```CURL
// CURL
curl --location  --request GET 'https://business-api.tiktok.com/open_api/v1.3/tool/open_url/?advertiser_id={{advertiser_id}}&url={{url}}&url_type=USER_PROFILE' \
--header 'Access-Token: {{Access-Token}}'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | The Mã trạng thái phản hồi (0: Thành công). For the complete list of error codes and descriptions, see [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | The Thông điệp phản hồi từ máy chủ. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | Mã nhật ký yêu cầu (request log ID) để định danh duy nhất cho mỗi lượt gọi API. |
| data | object | Returned data |
| ↳ open_url | string | TikTok internal link. |
| ↳ supported_regions | string[] | Countries and/or regions that the sticker (special effect) can be used. Returned when `url_type` is `STICKER` or `STICKER_SHOOTER`. |

### Ví dụ lệnh cURL (Example)
```JSON
// JSON
{
    "code": 0,
    "message": "OK",
    "request_id": "2021090212163301024502410742C587F8",
    "data": {
        "open_url": "sslocal://user/profile/60320267633123456?sec_uid=MS4wLjABAAAAzUKwYoagO3vLvQVSeMxAFUc5INu7rqzoCFmlOYtAtbd9Rah9FpoMg9wpr8QdkdIf"
    }
}
```

---

<a id="doc-1851286489283585"></a>
<!-- doc_id: 1851286489283585 -->
<!-- doc_id: 1851286489283585 -->
# Lấy nhãn chiến dịch của tài khoản quảng cáo (Get the campaign labels of an ad account)
> Đường dẫn: API Reference > Tools > Get the campaign labels of an ad account
Sử dụng endpoint này để truy xuất the list of campaign labels within an ad account.

## Yêu cầu gọi API (Request)

**Endpoint** 
https://business-api.tiktok.com/open_api/v1.3/campaign_label/get/

**Method** 
GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id  ****(Bắt buộc)**** | string | ID tài khoản quảng cáo TikTok. |
| campaign_label_ids | string[] | Danh sách ID nhãn chiến dịch. ⏎ Kích thước tối đa: 50. ⏎ Mỗi ID nhãn phải là một chuỗi 19 chữ số. ⏎ **Lưu ý**: Bộ lọc này chỉ được hỗ trợ trong báo cáo cơ bản đồng bộ. |
| campaign_label_names | string[] | Danh sách tên nhãn chiến dịch. ⏎ Hỗ trợ so khớp mờ (fuzzy matching). ⏎ Kích thước tối đa: 10. |
| campaign_label_types | string[] | Danh sách các loại nhãn chiến dịch. ⏎ Các giá trị enum hỗ trợ: • `GENERAL`: Nhãn chung. • `MARKETING_EVENT`: Nhãn sự kiện tiếp thị. |
| page | number | Current Số trang cần lấy dữ liệu. ⏎ Giá trị mặc định: 1. ⏎ Value range: ≥1. |
| page_size | number | Page size. ⏎ Giá trị mặc định: 10. ⏎ Value range: 1-1,000. |

### Ví dụ lệnh cURL (Example)

```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/campaign_label/get/?advertiser_id={{advertiser_id}}&page=1&page_size=1000' \
--header 'Access-Token: {{Access-Token}}'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Response code. For the complete list of response codes and descriptions, see [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | Mã nhật ký yêu cầu (request log ID) để định danh duy nhất cho mỗi lượt gọi API. |
| data | object | Returned data. |
| ↳ list | object[] | Details of the campaign labels within an ad account. |
| ↳↳ campaign_label_id | string | The ID of the campaign label. |
| ↳↳ campaign_label_name | string | Tên của nhãn chiến dịch. |
| ↳↳ campaign_label_type | string | The type of the campaign label. ⏎ Các giá trị enum hỗ trợ: • `GENERAL`: General label. • `MARKETING_EVENT`: Marketing event label. |
| ↳↳ campaign_label_color | string | The color of the campaign label. |
| ↳↳ create_time | string | The time when the campaign label was created, in the format of `YYYY-MM-DD HH:MM:SS` (UTC+0). ⏎ Example: `2025-01-01 00:00:01`. |
| ↳ page_info | object | Pagination information. |
| ↳↳ page | number | Current Số trang cần lấy dữ liệu. |
| ↳↳ page_size | number | Page size. |
| ↳↳ total_number | number | Tổng số kết quả tìm thấy. |
| ↳↳ total_page | number | Tổng số trang kết quả. |

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
                "campaign_label_color": "pinkFilled",
                "campaign_label_id": "{{campaign_label_id}}",
                "campaign_label_name": "{{campaign_label_name}}",
                "campaign_label_type": "MARKETING_EVENT",
                "create_time": "{{create_time}}"
            },
            {
                "campaign_label_color": "blueOutlined",
                "campaign_label_id": "{{campaign_label_id}}",
                "campaign_label_name": "{{campaign_label_name}}",
                "campaign_label_type": "GENERAL",
                "create_time": "{{create_time}}"
            }
        ],
        "page_info": {
            "page": 1,
            "page_size": 1000,
            "total_number": 2,
            "total_page": 1
        }
    }
}
```

---

<a id="doc-1853450329535490"></a>
<!-- doc_id: 1853450329535490 -->
<!-- doc_id: 1853450329535490 -->
# Lấy danh sách TikTok Minis trong tài khoản quảng cáo (Get the TikTok Minis within an ad account)
> Đường dẫn: API Reference > Tools > Get the TikTok Minis within an ad account
Sử dụng endpoint này để truy xuất the list of TikTok Minis within an ad account.

Để tìm hiểu thêm về loại chiến dịch bạn có thể quảng bá TikTok Mini, xem [Tạo chiến dịch Nâng cấp Smart+ TikTok Growth Max: Mini Games](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1868121865281538) và [Tạo chiến dịch Nâng cấp Smart+ TikTok Growth Max: Mini Dramas](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1853377811982657).

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/minis/get/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
|advertiser_id ***(Bắt buộc)***|string|ID tài khoản quảng cáo TikTok.|
|page|number|Current Số trang cần lấy dữ liệu.<br><br>Giá trị mặc định: 1. Value range: ≥ 1.|
|page_size|number|Page size.<br><br>Giá trị mặc định: 10. Value range: 1-50.|

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/minis/get/?advertiser_id={{advertiser_id}}&page=1&page_size=50' \
--header 'Access-Token: {{Access-Token}}'
```
## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|code|number|Response code. For the complete list of response codes and descriptions, see [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|message|string|Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|request_id|string|Mã nhật ký yêu cầu (request log ID) để định danh duy nhất cho mỗi lượt gọi API.|
|data|object|Returned data.|
#|list|object[]|A list of TikTok Minis within an ad account.|
##|minis_id|string|The ID of the TikTok Mini.|
##|minis_name|string|The name of the TikTok Mini.|
##|minis_icon_url|string|The URL to the app icon image of the TikTok Mini.|
##|minis_status|string|The status of the TikTok Mini.<br><br>Các giá trị enum hỗ trợ: <ul><li>`ACTIVE`: active. You can use the TikTok Mini to create ads.</li><li>`INACTIVE`: inactive. You cannot use the TikTok Mini to create ads.</li></ul>|
##|minis_type|string|The type of the TikTok Mini.<br><br>Các giá trị enum hỗ trợ: <ul><li>`MINI_SERIES`: mini drama.</li><li>`MINI_GAME`: mini game.</li></ul>|
##|region_codes|string[]|The region codes of the supported country or region for the TikTok Mini.<br><br>Example: `["ID", "US"]`.|
#|page_info|object|Pagination information.|
##|page|number|Current Số trang cần lấy dữ liệu.|
##|page_size|number|Paging size.|
##|total_number|number|Tổng số kết quả tìm thấy.|
##|total_page|number|Tổng số trang kết quả.|

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
                "minis_icon_url": "{{minis_icon_url}}",
                "minis_id": "{{minis_id}}",
                "minis_name": "{{minis_name}}",
                "minis_status": "ACTIVE",
                "minis_type": "MINI_GAME",
                "region_codes": [
                    "JP",
                    "US",
                    "ID"
                ]
            },
            {
                "minis_icon_url": "{{minis_icon_url}}",
                "minis_id": "{{minis_id}}",
                "minis_name": "{{minis_name}}",
                "minis_status": "ACTIVE",
                "minis_type": "MINI_GAME",
                "region_codes": [
                    "JP",
                    "US",
                    "ID"
                ]
            },
            {
                "minis_icon_url": "{{minis_icon_url}}",
                "minis_id": "{{minis_id}}",
                "minis_name": "{{minis_name}}",
                "minis_status": "ACTIVE",
                "minis_type": "MINI_SERIES",
                "region_codes": [
                    "JP"
                ]
            },
            {
                "minis_icon_url": "{{minis_icon_url}}",
                "minis_id": "{{minis_id_4}}",
                "minis_name": "{{minis_name_4}}",
                "minis_status": "ACTIVE",
                "minis_type": "MINI_SERIES",
                "region_codes": [
                    "US"
                ]
            }
        ],
        "page_info": {
            "page": 1,
            "page_size": 50,
            "total_number": 4,
            "total_page": 1
        }
    }
}
```

---

<a id="doc-1863332009162754"></a>
<!-- doc_id: 1863332009162754 -->
<!-- doc_id: 1863332009162754 -->
# Lấy danh sách TikTok Series khả dụng trong tài khoản quảng cáo (Get the available TikTok Series within an ad account)
> Đường dẫn: API Reference > Tools > Get the available TikTok Series within an ad account
Sử dụng endpoint này để truy xuất a list of available TikTok Series from a specified TikTok account (identity) that can be promoted by an ad account.

Series cung cấp các gói video độc quyền và cao cấp do nhà sáng tạo thực hiện. Bạn có thể mua quyền truy cập Series thông qua trang cá nhân của nhà sáng tạo và các liên kết đính kèm video TikTok.
> **Note:** 
> If you would like to create TikTok Series within your TikTok account, please contact your TikTok representative.

## Yêu cầu gọi API (Request)
**Endpoint** https://business-api.tiktok.com/open_api/v1.3/identity/native_series/get/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id  ****(Bắt buộc)**** | string | ID tài khoản quảng cáo TikTok. |
| identity_id  ****(Bắt buộc)**** | string | Identity ID. ⏎ To get the list of identities under your ad account, use [/identity/get/](46-identity.md#doc-1740218420781057). |
| identity_type  ****(Bắt buộc)**** | string | Identity type. ⏎ Các giá trị enum hỗ trợ: `TT_USER`, `BC_AUTH_TT`. ⏎ See [Identities](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1738958351620097) for details. |
| identity_authorized_bc_id **(Điều kiện)** | string | Bắt buộc khi `identity_type` is `BC_AUTH_TT`. ⏎ ID of the Business Center that a TikTok Account User in Business Center identity is associated with. |
| cursor | integer | The cursor for paginating results. ⏎ If `has_more` in the response is `true`, use the returned cursor in your subsequent request to fetch the next set of data. ⏎ Giá trị mặc định: 0. |
| count | number | The maximum number of Series to return in the response. ⏎ Value range: 1-20. ⏎ Giá trị mặc định: 10. |

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/identity/native_series/get/?advertiser_id={{advertiser_id}}&identity_type=BC_AUTH_TT&identity_id={{identity_id}}&identity_authorized_bc_id={{identity_authorized_bc_id}}' \
--header 'Access-Token: {{Access-Token}}'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| - | - | - |
| code | number | Response code. For the complete list of response codes and descriptions, see [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | Mã nhật ký yêu cầu (request log ID) để định danh duy nhất cho mỗi lượt gọi API. |
| data | object | Returned data. |
| ↳ list | object[] | The list of Series that you can access from the identity (`identity_id`). |
| ↳↳ native_series_id | string | The ID of the TikTok Series. |
| ↳↳ native_series_name | string | Tên của TikTok Series. |
| ↳↳ native_series_cover_url | string | The URL to the cover image of the TikTok Series. |
| ↳↳ native_series_total_episode | number | Tổng số tập trong TikTok Series. |
| ↳↳ native_series_total_duration | number | The combined duration of all episodes in the TikTok Series, measured in seconds. |
| ↳ cursor | integer | The cursor for paginating results. ⏎ If `has_more` in the response is `true`, use this cursor in your subsequent request to fetch the next set of data. |
| ↳ has_more | boolean | Liệu more data is available. |

### Ví dụ lệnh cURL (Example)
```http
// curl
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "cursor": {{cursor}},
        "has_more": false,
        "list": [
            {
                "native_series_cover_url": "{{native_series_cover_url}}",
                "native_series_id": "{{native_series_id}}",
                "native_series_name": "{{native_series_name}}",
                "native_series_total_duration": 31,
                "native_series_total_episode": 2
            },
            {
                "native_series_cover_url": "{{native_series_cover_url}}",
                "native_series_id": "{{native_series_id}}",
                "native_series_name": "{{native_series_name}}",
                "native_series_total_duration": 153,
                "native_series_total_episode": 6
            },
            {
                "native_series_cover_url": "{{native_series_cover_url}}",
                "native_series_id": "{{native_series_id}}",
                "native_series_name": "{{native_series_name}}",
                "native_series_total_duration": 84,
                "native_series_total_episode": 1
            },
            {
                "native_series_cover_url": "{{native_series_cover_url}}",
                "native_series_id": "{{native_series_id}}",
                "native_series_name": "{{native_series_name}}",
                "native_series_total_duration": 84,
                "native_series_total_episode": 1
            },
            {
                "native_series_cover_url": "{{native_series_cover_url}}",
                "native_series_id": "{{native_series_id}}",
                "native_series_name": "{{native_series_name}}",
                "native_series_total_duration": 116,
                "native_series_total_episode": 1
            },
            {
                "native_series_cover_url": "{{native_series_cover_url}}",
                "native_series_id": "{{native_series_id}}",
                "native_series_name": "{{native_series_name}}",
                "native_series_total_duration": 147,
                "native_series_total_episode": 2
            },
            {
                "native_series_cover_url": "{{native_series_cover_url}}",
                "native_series_id": "{{native_series_id}}",
                "native_series_name": "{{native_series_name}}",
                "native_series_total_duration": 179,
                "native_series_total_episode": 2
            },
            {
                "native_series_cover_url": "{{native_series_cover_url}}",
                "native_series_id": "{{native_series_id}}",
                "native_series_name": "{{native_series_name}}",
                "native_series_total_duration": 28,
                "native_series_total_episode": 1
            }
        ]
    }
}
```

---

<a id="doc-1870952425111618"></a>
<!-- doc_id: 1870952425111618 -->
<!-- doc_id: 1870952425111618 -->
# Lấy nguồn phân bổ và nguồn dữ liệu khả dụng cho ứng dụng (Get available attribution sources and data sources for an app)
> Đường dẫn: API Reference > Tools > Get available attribution sources and data sources for an app
Sử dụng endpoint này để truy xuất các nguồn phân bổ và nguồn dữ liệu khả dụng cho ứng dụng di động của bạn khi tạo Nhóm quảng cáo Smart+ nâng cấp.

## Yêu cầu gọi API (Request)
**Endpoint** https://business-api.tiktok.com/open_api/v1.3/tool/available/attribution_source/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id  ****(Bắt buộc)**** | string | ID tài khoản quảng cáo TikTok. |
| app_id  ****(Bắt buộc)**** | string | ID ứng dụng di động (App ID). ⏎ Để lấy App ID, sử dụng [/app/list/](43-events-1-0-p1.md#doc-1740859313270786). |
| optimization_event | string | Sự kiện tối ưu hóa (Sự kiện chuyển đổi). ⏎ Để xem danh sách các giá trị enum, xem Danh sách giá trị cho `optimization_event`. |
| campaign_type | string | Loại chiến dịch. ⏎ Các giá trị enum hỗ trợ: • `REGULAR_CAMPAIGN`: a campaign with the iOS 14 Dedicated Campaign setting disabled. • `IOS14_CAMPAIGN`: a campaign with the iOS 14 Dedicated Campaign setting enabled. ⏎ Giá trị mặc định: `REGULAR_CAMPAIGN`. |

### Danh sách giá trị cho `optimization_event`

| Optimization event | optimization_event value |
|---|---|
| Install | `ACTIVE` |
| Registration | `ACTIVE_REGISTER` |
| Purchase ⏎ /Purchase value (for Value-Based Optimization) | `ACTIVE_PAY` |
| Checkout | `IN_APP_ORDER` |
| Add to Cart | `IN_APP_CART` |
| Generate Lead | `SALES_LEAD` |
| View Content | `IN_APP_DETAIL_UV` |
| Achieve Level | `UPDATE_LEVEL` |
| Create Role | `CREATE_GAMEROLE` |
| Loan is disbursed | `LOAN_COMPLETION` |
| Loan Approval | `LOAN_CREDIT` |
| Login | `LOGIN` |
| Loan Apply | `LOAN_APPLY` |
| Add Payment Info | `ADD_PAYMENT_INFO` |
| Add to Wishlist | `ADD_TO_WISHLIST` |
| Launch App | `LAUNCH_APP` |
| Complete Tutorial | `COMPLETE_TUTORIAL` |
| In-App Ad Click | `IN_APP_AD_CLICK` |
| In-App Ad Impression | `IN_APP_AD_IMPR` |
| Join Group | `JOIN_GROUP` |
| Rate | `RATE` |
| Search | `SEARCH` |
| Start Trial | `START_TRIAL` |
| Subscribe | `SUBSCRIBE` |
| Unlock Achievement | `UNLOCK_ACHIEVEMENT` |
| Ad revenue value (for Value-Based Optimization) | `AD_REVENUE_VALUE`/`IMPRESSION_LEVEL_AD_REVENUE` |

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/tool/available/attribution_source/?advertiser_id={{advertiser_id}}&app_id={{app_id}}&campaign_type=REGULAR_CAMPAIGN' \
--header 'Access-Token: {{Access-Token}}'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| - | - | - |
| code | number | Response code. For the complete list of response codes and descriptions, see [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | Mã nhật ký yêu cầu (request log ID) để định danh duy nhất cho mỗi lượt gọi API. |
| data | object | Returned data. |
| ↳ connected_data_source | string[] | The list of data sources that the app is connected to. ⏎ Các giá trị enum hỗ trợ: • `MMP`: MMP (mobile measurement partner). • `EVENT_SDK`: TikTok App Events SDK. • `EVENT_API`: TikTok Events API. |
| ↳ available_attribution_source_list | object[] | The details of the attribution sources and data sources you can configure for the app when creating Upgraded Smart+ Ad Groups. ⏎ You can pass the values from `available_attribution_source` and `available_data_source` to the `app_attribution_source` and `app_data_source` parameters when you call [/smart_plus/adgroup/create/](62-upgraded-smartplus-p3.md#doc-1843314887930946). |
| ↳↳ available_attribution_source | string | The attribution source that you can configure for the app when creating Upgraded Smart+ Ad Groups. ⏎ The attribution source you choose will be used for optimization, bidding, and reporting. ⏎ Các giá trị enum hỗ trợ: • `MMP`: MMP (mobile measurement partner) attribution. Signals from your selected MMP will be used for attribution. • `SAN`: SAN (self-attribution network) attribution. Signals from TikTok SAN will be used for attribution. |
| ↳↳ available_data_source | string[] | The list of data sources that you can configure for the app when creating Upgraded Smart+ Ad Groups. ⏎ The attribution signals you select will be used for reporting. ⏎ Các giá trị enum hỗ trợ: • `MMP`: MMP signals. Signals from your MMP will be used for reporting. • `EVENT_SDK`: App Events SDK signals. Signals from TikTok App Events SDK will be used for reporting. • `EVENT_API`: Events API signals. Signals from TikTok Events API will be used for reporting. |

### Ví dụ lệnh cURL (Example)
```http
// curl
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "available_attribution_source_list": [
            {
                "available_attribution_source": "SAN",
                "available_data_source": [
                    "EVENT_SDK"
                ]
            }
        ],
        "connected_data_source": [
            "EVENT_SDK"
        ]
    }
}
```

---

<a id="doc-1874392512912449"></a>
<!-- doc_id: 1874392512912449 -->
<!-- doc_id: 1874392512912449 -->
# Lấy trạng thái bảo vệ giá thầu (Get bid protection statuses)
> Đường dẫn: API Reference > Tools > Get bid protection statuses
Sử dụng endpoint này để truy xuất trạng thái bảo vệ giá thầu hiện tại cho danh sách các Chiến dịch Smart+ nâng cấp (Upgraded Smart+ Campaigns) hoặc Nhóm quảng cáo Smart+ nâng cấp (Upgraded Smart+ Ad Groups).

## Yêu cầu gọi API (Request)
**Endpoint** https://business-api.tiktok.com/open_api/v1.3/report/bid_protection/status/get/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id  ****(Bắt buộc)**** | string | ID tài khoản quảng cáo TikTok. |
| data_level  ****(Bắt buộc)**** | string | The data level you want to query. ⏎ Các giá trị enum hỗ trợ: • `CAMPAIGN`: Campaign level. • `ADGROUP`: Ad group level. |
| query_ids  ****(Bắt buộc)**** | string[] | The list of IDs you want to query. ⏎ Kích thước tối đa: 200. • When `data_level` is `CAMPAIGN`, specify a list of Upgraded Smart+ Campaign IDs. • To retrieve these IDs, use [/smart_plus/campaign/get/](62-upgraded-smartplus-p1.md#doc-1843312818332930). • When `data_level` is `ADGROUP`, specify a list of Upgraded Smart+ Ad Group IDs. • To retrieve these IDs, use [/smart_plus/adgroup/get/](62-upgraded-smartplus-p2.md#doc-1843314879617026). ⏎ All IDs must belong to the same advertiser. |

## Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/report/bid_protection/status/get/?advertiser_id={{advertiser_id}}&data_level=CAMPAIGN&query_ids=["{{query_id}}"]' \
--header 'Access-Token: {{Access-Token}}'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| - | - | - |
| code | number | Response code. For the complete list of response codes and descriptions, see [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | Mã nhật ký yêu cầu (request log ID) để định danh duy nhất cho mỗi lượt gọi API. |
| data | object | Returned data. |
| ↳ list | object[] | The bid protection status information for your queried campaigns or ad groups. |
| ↳↳ data_level | string | The data level. ⏎ Các giá trị enum hỗ trợ: • `CAMPAIGN`: Campaign level. • `ADGROUP`: Ad group level. |
| ↳↳ query_id | string | The specific ID you queried. • When `data_level` is `CAMPAIGN`, this field represents an Upgraded Smart+ ID chiến dịch quảng cáo. • When `data_level` is `ADGROUP`, this field represents an Upgraded Smart+ ID nhóm quảng cáo. |
| ↳↳ bid_protection_status | string | The current bid protection status for the campaign or ad group. ⏎ Các giá trị enum hỗ trợ: • `ACTIVE`: Bid protection is active for the campaign or ad group. You’re eligible for ad credits when costs exceed your bid. You can query historical records through [/report/bid_protection/detail/get/](70-tools-p3.md#doc-1874392516418561). • `INVALID`: Bid protection is temporarily ineligible for the campaign or ad group because the campaign or ad group was paused or deleted within the first 3 days after creation. • `INACTIVE`: Bid protection is permanently ineligible for the campaign or ad group. |
| ↳↳ compensation_category | string | The bid protection compensation category. ⏎ Các giá trị enum hỗ trợ: • `FULL_LIFE_CYCLE`: Full lifecycle compensation.[Bid Protection (Full Lifecycle)](https://ads.tiktok.com/resources/help/article/about-smart-plus-bid-protection) is the default solution, covering the campaign's entire duration. • `THREE_DAY`: Three-day compensation. Only bidding strategies that are currently unsupported in the Full Lifecycle version will use [Bid Protection (Learning Phase)](https://ads.tiktok.com/help/article/incentive-offer). This covers the first three full consecutive days from the day you activate the campaign. |

## Ví dụ lệnh cURL (Example)
```http
// curl
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "list": [
            {
                "bid_protection_status": "ACTIVE",
                "compensation_category": "FULL_LIFE_CYCLE",
                "data_level": "CAMPAIGN",
                "query_id": "{{query_id}}"
            }
        ]
    }
}
```
---

## Hướng dẫn thực hành Data Retrieval (Python & cURL)

Dưới đây là mã nguồn mẫu minh họa quy trình gọi API thực tế cho phân hệ **Công cụ tra cứu (Tools) — phần 2/3**:

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

