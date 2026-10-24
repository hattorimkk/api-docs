# Tiền kiểm duyệt creative (Creative Pre-review)

> Phân hệ: apiref:Creative Pre-review.
> Tài liệu biên dịch kỹ thuật chi tiết theo chuẩn TikTok Business API v1.3.

---

## Mục lục điều hướng
- [1. Creative Pre-review (#doc-1874110575134722)](#doc-1874110575134722)
- [2. Create a creative pre-review task (#doc-1874110632584577)](#doc-1874110632584577)
- [3. Get the result of a creative pre-review task (#doc-1874110636550082)](#doc-1874110636550082)

---

<a id="doc-1874110575134722"></a>
<!-- doc_id: 1874110575134722 -->
<!-- doc_id: 1874110575134722 -->
# Creative Pre-review
> Đường dẫn: API Reference > Creative Pre-review
The Creative Pre-review API is designed to streamline the ad creation process by offering a preliminary review of your ad creatives. This proactive approach allows you to assess and refine creatives ahead of the standard ad approval process, enhancing the overall quality and effectiveness of submissions.

To learn more about the benefits of and step-by-step instructions for Creative Pre-review API, see [Obtain pre-review results for your creatives](../09-marketing-api/creatives.md#doc-1874110837867522).

This group consists of the following endpoints:

- [Create a creative pre-review task](35-creative-pre-review.md#doc-1874110632584577)
- [Get the result of a creative pre-review task](35-creative-pre-review.md#doc-1874110636550082)
- [Upload a video](71-video.md#doc-1737587322856449)
- [Upload an image](47-images.md#doc-1739067433456642)

---

<a id="doc-1874110632584577"></a>
<!-- doc_id: 1874110632584577 -->
<!-- doc_id: 1874110632584577 -->
# Create a creative pre-review task
> Đường dẫn: API Reference > Creative Pre-review > Create a creative pre-review task
Sử dụng endpoint này để tạo a pre-review task for your creatives.

A pre-review task is a process initiated to evaluate and assess the compliance and quality of your creatives before they are used to create ads, ensuring that they meet TikTok advertising guidelines and standards.

After you create the task, call [/creative/pre_review/task/get/](35-creative-pre-review.md#doc-1874110636550082) to check the task result. The time required to process each task may vary based on the number of creatives. The average processing time of each pre-review task is around five minutes.

# Yêu cầu gọi API (Request)
**Endpoint** https://business-api.tiktok.com/open_api/v1.3/creative/pre_review/task/create/

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
| material_list  ****(Bắt buộc)**** | object[] | Danh sách các nội dung sáng tạo (creatives) gửi đi để tiền kiểm duyệt. ⏎ Size range: 1-5. |
| ↳ material_type  ****(Bắt buộc)**** | string | The material type of the creative. ⏎ Các giá trị enum hỗ trợ: • `VIDEO`: video. • `IMAGE`: image. • `AD_TEXT`: ad text. • `LANDING_PAGE_URL`: landing page URL. |
| ↳ material_id  ****(Bắt buộc)**** | string | The ID or content of the creative. • When `material_type` is `VIDEO`, specify a video ID. • To search for video IDs within your ad account, use [/file/video/ad/search/](71-video.md#doc-1740050472224769) and check the returned `video_id`. • When `material_type` is `IMAGE`, specify an image ID. • To search for image IDs within your ad account, use [/file/image/ad/search/](47-images.md#doc-1740052016789506) and check the returned `image_id`. • When `material_type` is `AD_TEXT`, specify an ad text. • When `material_type` is `LANDING_PAGE_URL`, specify a landing page URL. |
| location_codes  ****(Bắt buộc)**** | string[] | Danh sách mã quốc gia/khu vực bạn muốn nhắm mục tiêu. ⏎ Kích thước tối đa: 1. ⏎ Để xem danh sách giá trị enum, xem [List of values for `location_codes` or `location_code`](https://business-api.tiktok.com/portal/docs/create-a-creative-pre-review-task/v1.3#anchor-1-1). ⏎ Example: `US`. |
| is_ecommerce | boolean | Liệu creatives are intended for use in E-commerce ads, including [GMV Max Campaigns](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1822009058467842) and Catalog Ads. ⏎ Các giá trị được hỗ trợ: `true`, `false`. ⏎ Giá trị mặc định: `false`. |

## List of values for `location_codes` or `location_code`

Bảng sau đây liệt kê các giá trị enum cho tham số yêu cầu `location_codes` trong [/creative/pre_review/task/create/](35-creative-pre-review.md#doc-1874110632584577), [/file/video/ad/upload/](71-video.md#doc-1737587322856449), and [/file/image/ad/upload/](47-images.md#doc-1739067433456642), and the response parameter `location_code` in [/creative/pre_review/task/get/](35-creative-pre-review.md#doc-1874110636550082).

| Mã quốc gia (Location Code) | Tên quốc gia/vùng lãnh thổ |
|---|---|
| `AD` | Andorra |
| `AE` | United Arab Emirates |
| `AG` | Antigua and Barbuda |
| `AI` | Anguilla |
| `AL` | Albania |
| `AO` | Angola |
| `AR` | Argentina |
| `AT` | Austria |
| `AU` | Australia |
| `AW` | Aruba |
| `AZ` | Azerbaijan |
| `BA` | Bosnia and Herzegovina |
| `BB` | Barbados |
| `BD` | Bangladesh |
| `BE` | Belgium |
| `BG` | Bulgaria |
| `BH` | Bahrain |
| `BL` | Saint Barthélemy |
| `BM` | Bermuda |
| `BO` | Bolivia |
| `BQ` | Caribbean Netherlands |
| `BR` | Brazil |
| `BS` | The Bahamas |
| `BY` | Belarus |
| `BZ` | Belize |
| `CA` | Canada |
| `CD` | Democratic Republic of the Congo |
| `CH` | Switzerland |
| `CL` | Chile |
| `CO` | Colombia |
| `CR` | Costa Rica |
| `CU` | Cuba |
| `CV` | Cabo Verde |
| `CW` | Curaçao |
| `CY` | Cyprus |
| `CZ` | Czech Republic |
| `DE` | Germany |
| `DJ` | Djibouti |
| `DK` | Denmark |
| `DM` | Dominica |
| `DO` | Dominican Republic |
| `DZ` | Algeria |
| `EC` | Ecuador |
| `EE` | Estonia |
| `EG` | Egypt |
| `ER` | Eritrea |
| `ES` | Spain |
| `FI` | Finland |
| `FO` | Faroe Islands |
| `FR` | France |
| `GB` | United Kingdom |
| `GD` | Grenada |
| `GE` | Georgia |
| `GF` | French Guiana |
| `GG` | Bailiwick of Guernsey |
| `GI` | Gibraltar |
| `GL` | Greenland |
| `GN` | Guinea |
| `GP` | Guadeloupe |
| `GQ` | Equatorial Guinea |
| `GR` | Greece |
| `GT` | Guatemala |
| `GW` | Guinea-Bissau |
| `HK` | Hong Kong |
| `HN` | Honduras |
| `HR` | Croatia |
| `HT` | Haiti |
| `HU` | Hungary |
| `ID` | Indonesia |
| `IE` | Ireland |
| `IL` | Israel |
| `IM` | Isle of Man |
| `IN` | India |
| `IQ` | Iraq |
| `IS` | Iceland |
| `IT` | Italy |
| `JE` | Jersey |
| `JM` | Jamaica |
| `JO` | Jordan |
| `JP` | Japan |
| `KE` | Kenya |
| `KH` | Cambodia |
| `KM` | Comoros |
| `KN` | Saint Kitts and Nevis |
| `KR` | South Korea |
| `KW` | Kuwait |
| `KY` | Cayman Islands |
| `KZ` | Kazakhstan |
| `LB` | Lebanon |
| `LC` | Saint Lucia |
| `LI` | Liechtenstein |
| `LK` | Sri Lanka |
| `LT` | Lithuania |
| `LU` | Luxembourg |
| `LV` | Latvia |
| `LY` | Libya |
| `MA` | Morocco |
| `MC` | Monaco |
| `MD` | Moldova |
| `ME` | Montenegro |
| `MF` | Saint Martin |
| `MK` | North Macedonia |
| `MM` | Myanmar |
| `MO` | Macao |
| `MQ` | Martinique |
| `MR` | Mauritania |
| `MS` | Montserrat |
| `MT` | Malta |
| `MX` | Mexico |
| `MY` | Malaysia |
| `MZ` | Mozambique |
| `NG` | Nigeria |
| `NI` | Nicaragua |
| `NL` | Netherlands |
| `NO` | Norway |
| `NP` | Nepal |
| `NZ` | New Zealand |
| `OM` | Oman |
| `PA` | Panama |
| `PE` | Peru |
| `PF` | French Polynesia |
| `PH` | Philippines |
| `PK` | Pakistan |
| `PL` | Poland |
| `PM` | Saint Pierre and Miquelon |
| `PR` | Puerto Rico |
| `PS` | Palestine |
| `PT` | Portugal |
| `PY` | Paraguay |
| `QA` | Qatar |
| `RO` | Romania |
| `RS` | Serbia |
| `RU` | Russia |
| `SA` | Saudi Arabia |
| `SD` | Sudan |
| `SE` | Sweden |
| `SG` | Singapore |
| `SI` | Slovenia |
| `SJ` | Svalbard and Jan Mayen |
| `SK` | Slovakia |
| `SM` | San Marino |
| `SO` | Somalia |
| `SS` | South Sudan |
| `ST` | Sao Tome and Principe |
| `SV` | El Salvador |
| `SX` | Sint Maarten |
| `SY` | Syria |
| `TC` | Turks and Caicos Islands |
| `TD` | Chad |
| `TF` | French Southern and Antarctic Lands |
| `TH` | Thailand |
| `TN` | Tunisia |
| `TR` | Turkey |
| `TT` | Trinidad and Tobago |
| `TW` | Taiwan (Province of China) |
| `UA` | Ukraine |
| `US` | United States |
| `UY` | Uruguay |
| `UZ` | Uzbekistan |
| `VC` | Saint Vincent and the Grenadines |
| `VE` | Venezuela |
| `VG` | British Virgin Islands |
| `VI` | Virgin Islands of the United States |
| `VN` | Vietnam |
| `YE` | Yemen |
| `ZA` | South Africa |

## Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/creative/pre_review/task/create/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id": "{{advertiser_id}}",
    "material_list": [
        {
            "material_type": "VIDEO",
            "material_id": "{{material_id}}"
        },
        {
            "material_type": "IMAGE",
            "material_id": "{{material_id}}"
        },
        {
            "material_type": "AD_TEXT",
            "material_id": "{{material_id}}"
        }
    ],
    "location_codes": [
        "US"
    ],
    "is_ecommerce": false
}'
```

# Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| - | - | - |
| code | number | Response code. For the complete list of response codes and descriptions, see [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | The log ID of the request, which uniquely identifies a request. |
| data | object | Returned data. |
| ↳ pre_review_task_id | string | ID của tác vụ tiền kiểm duyệt. ⏎ To obtain the result of the pre-review task, pass the value of this field to the `task_id` field in [/creative/pre_review/task/get/](35-creative-pre-review.md#doc-1874110636550082). |

## Ví dụ lệnh cURL (Example)
```http
// curl
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "pre_review_task_id": "{{pre_review_task_id}}"
    }
}
```

---

<a id="doc-1874110636550082"></a>
<!-- doc_id: 1874110636550082 -->
<!-- doc_id: 1874110636550082 -->
# Get the result of a creative pre-review task
> Đường dẫn: API Reference > Creative Pre-review > Get the result of a creative pre-review task
Sử dụng endpoint này để truy xuất the result of a pre-review task for creatives.

# Yêu cầu gọi API (Request)
**Endpoint** https://business-api.tiktok.com/open_api/v1.3/creative/pre_review/task/get/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id  ****(Bắt buộc)**** | string | ID tài khoản quảng cáo TikTok. |
| task_id  ****(Bắt buộc)**** | string | ID của tác vụ tiền kiểm duyệt. ⏎ To create a pre-review task and obtain the task ID, use any of the following endpoints: • [/creative/pre_review/task/create/](35-creative-pre-review.md#doc-1874110632584577) • [/file/video/ad/upload/](71-video.md#doc-1737587322856449) • [/file/image/ad/upload/](47-images.md#doc-1739067433456642) ⏎ **Note**: If the `task_id` doesn't match the `advertiser_id`, an error will occur. |

## Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/creative/pre_review/task/get/?advertiser_id={{advertiser_id}}&task_id={{task_id}}' \
--header 'Access-Token: {{Access-Token}}'
```

# Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| - | - | - |
| code | number | Response code. For the complete list of response codes and descriptions, see [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | The log ID of the request, which uniquely identifies a request. |
| data | object | Returned data. |
| ↳ task_status | string | The status of the pre-review task. ⏎ Các giá trị enum hỗ trợ: • `PROCESSING`: The task is being processed. • `SUCCESS`: The task has been completed. |
| ↳ pre_review_result_list | object[] | The list of results for the pre-reviews of the creatives. |
| ↳↳ pre_review_status | string | The result of the pre-review for the creative. ⏎ Các giá trị enum hỗ trợ: • `APPROVED`: Approved by the pre-review. • `REJECTED`: Rejected during pre-review. • `UNSURE`: Result cannot be determined. • `UNAVAILABLE`: Result unavailable. |
| ↳↳ material_type | string | The material type of the creative. ⏎ Các giá trị enum hỗ trợ: • `VIDEO`: video. • `IMAGE`: image. • `AD_TEXT`: ad text. • `LANDING_PAGE_URL`: landing page URL. |
| ↳↳ material_id | string | The ID or content of the creative. • When `material_type` is `VIDEO`, this field represents the video ID of the video. • When `material_type` is `IMAGE`, this field represents the image ID of the image. • When `material_type` is `AD_TEXT`, this field represents the ad text. • When `material_type` is `LANDING_PAGE_URL`, this field represents the landing page URL. |
| ↳↳ result_creation_time | string | The time when the pre-review result was generated, in the format of `YYYY-MM-DD HH:MM:SS` (UTC+0). ⏎ Example: `2025-01-01 00:00:01`. |
| ↳↳ result_expiration_time | string | The time when the pre-review result will expire, in the format of `YYYY-MM-DD HH:MM:SS` (UTC+0). ⏎ Example: `2025-01-01 00:00:01`. ⏎ Each pre-review result is valid for 180 days. |
| ↳↳ location_code | string | The code of the location to target. ⏎ Để xem danh sách giá trị enum, xem [List of values for `location_codes` or `location_code`](https://business-api.tiktok.com/portal/docs/get-the-result-of-a-creative-pre-review-task/v1.3#anchor-2-1). ⏎ Example: `US`. |
| ↳↳ is_ecommerce | boolean | Liệu creatives will be used in E-commerce ads including [GMV Max Campaigns](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1822009058467842) and Catalog Ads. ⏎ Các giá trị được hỗ trợ: `true`, `false`. |
| ↳↳ reject_info_list | object[] | The list of reasons for the rejection of the creatives. |
| ↳↳↳ reason | string | The specific reason provided for the rejection of the creative. |
| ↳↳↳ suggestion | string | The suggestion for resolving the rejection issues. |

## List of values for `location_codes` or `location_code`

Bảng sau đây liệt kê các giá trị enum cho tham số yêu cầu `location_codes` trong [/creative/pre_review/task/create/](35-creative-pre-review.md#doc-1874110632584577), [/file/video/ad/upload/](71-video.md#doc-1737587322856449), and [/file/image/ad/upload/](47-images.md#doc-1739067433456642), and the response parameter `location_code` in [/creative/pre_review/task/get/](35-creative-pre-review.md#doc-1874110636550082).

| Mã quốc gia (Location Code) | Tên quốc gia/vùng lãnh thổ |
|---|---|
| `AD` | Andorra |
| `AE` | United Arab Emirates |
| `AG` | Antigua and Barbuda |
| `AI` | Anguilla |
| `AL` | Albania |
| `AO` | Angola |
| `AR` | Argentina |
| `AT` | Austria |
| `AU` | Australia |
| `AW` | Aruba |
| `AZ` | Azerbaijan |
| `BA` | Bosnia and Herzegovina |
| `BB` | Barbados |
| `BD` | Bangladesh |
| `BE` | Belgium |
| `BG` | Bulgaria |
| `BH` | Bahrain |
| `BL` | Saint Barthélemy |
| `BM` | Bermuda |
| `BO` | Bolivia |
| `BQ` | Caribbean Netherlands |
| `BR` | Brazil |
| `BS` | The Bahamas |
| `BY` | Belarus |
| `BZ` | Belize |
| `CA` | Canada |
| `CD` | Democratic Republic of the Congo |
| `CH` | Switzerland |
| `CL` | Chile |
| `CO` | Colombia |
| `CR` | Costa Rica |
| `CU` | Cuba |
| `CV` | Cabo Verde |
| `CW` | Curaçao |
| `CY` | Cyprus |
| `CZ` | Czech Republic |
| `DE` | Germany |
| `DJ` | Djibouti |
| `DK` | Denmark |
| `DM` | Dominica |
| `DO` | Dominican Republic |
| `DZ` | Algeria |
| `EC` | Ecuador |
| `EE` | Estonia |
| `EG` | Egypt |
| `ER` | Eritrea |
| `ES` | Spain |
| `FI` | Finland |
| `FO` | Faroe Islands |
| `FR` | France |
| `GB` | United Kingdom |
| `GD` | Grenada |
| `GE` | Georgia |
| `GF` | French Guiana |
| `GG` | Bailiwick of Guernsey |
| `GI` | Gibraltar |
| `GL` | Greenland |
| `GN` | Guinea |
| `GP` | Guadeloupe |
| `GQ` | Equatorial Guinea |
| `GR` | Greece |
| `GT` | Guatemala |
| `GW` | Guinea-Bissau |
| `HK` | Hong Kong |
| `HN` | Honduras |
| `HR` | Croatia |
| `HT` | Haiti |
| `HU` | Hungary |
| `ID` | Indonesia |
| `IE` | Ireland |
| `IL` | Israel |
| `IM` | Isle of Man |
| `IN` | India |
| `IQ` | Iraq |
| `IS` | Iceland |
| `IT` | Italy |
| `JE` | Jersey |
| `JM` | Jamaica |
| `JO` | Jordan |
| `JP` | Japan |
| `KE` | Kenya |
| `KH` | Cambodia |
| `KM` | Comoros |
| `KN` | Saint Kitts and Nevis |
| `KR` | South Korea |
| `KW` | Kuwait |
| `KY` | Cayman Islands |
| `KZ` | Kazakhstan |
| `LB` | Lebanon |
| `LC` | Saint Lucia |
| `LI` | Liechtenstein |
| `LK` | Sri Lanka |
| `LT` | Lithuania |
| `LU` | Luxembourg |
| `LV` | Latvia |
| `LY` | Libya |
| `MA` | Morocco |
| `MC` | Monaco |
| `MD` | Moldova |
| `ME` | Montenegro |
| `MF` | Saint Martin |
| `MK` | North Macedonia |
| `MM` | Myanmar |
| `MO` | Macao |
| `MQ` | Martinique |
| `MR` | Mauritania |
| `MS` | Montserrat |
| `MT` | Malta |
| `MX` | Mexico |
| `MY` | Malaysia |
| `MZ` | Mozambique |
| `NG` | Nigeria |
| `NI` | Nicaragua |
| `NL` | Netherlands |
| `NO` | Norway |
| `NP` | Nepal |
| `NZ` | New Zealand |
| `OM` | Oman |
| `PA` | Panama |
| `PE` | Peru |
| `PF` | French Polynesia |
| `PH` | Philippines |
| `PK` | Pakistan |
| `PL` | Poland |
| `PM` | Saint Pierre and Miquelon |
| `PR` | Puerto Rico |
| `PS` | Palestine |
| `PT` | Portugal |
| `PY` | Paraguay |
| `QA` | Qatar |
| `RO` | Romania |
| `RS` | Serbia |
| `RU` | Russia |
| `SA` | Saudi Arabia |
| `SD` | Sudan |
| `SE` | Sweden |
| `SG` | Singapore |
| `SI` | Slovenia |
| `SJ` | Svalbard and Jan Mayen |
| `SK` | Slovakia |
| `SM` | San Marino |
| `SO` | Somalia |
| `SS` | South Sudan |
| `ST` | Sao Tome and Principe |
| `SV` | El Salvador |
| `SX` | Sint Maarten |
| `SY` | Syria |
| `TC` | Turks and Caicos Islands |
| `TD` | Chad |
| `TF` | French Southern and Antarctic Lands |
| `TH` | Thailand |
| `TN` | Tunisia |
| `TR` | Turkey |
| `TT` | Trinidad and Tobago |
| `TW` | Taiwan (Province of China) |
| `UA` | Ukraine |
| `US` | United States |
| `UY` | Uruguay |
| `UZ` | Uzbekistan |
| `VC` | Saint Vincent and the Grenadines |
| `VE` | Venezuela |
| `VG` | British Virgin Islands |
| `VI` | Virgin Islands of the United States |
| `VN` | Vietnam |
| `YE` | Yemen |
| `ZA` | South Africa |

## Ví dụ lệnh cURL (Example)
```http
// curl
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "pre_review_result_list": [
            {
                "is_ecommerce": false,
                "location_code": "US",
                "material_id": "{{material_id}}",
                "material_type": "VIDEO",
                "pre_review_status": "APPROVED",
                "reject_info_list": [],
                "result_creation_time": "{{result_creation_time}}",
                "result_expiration_time": "{{result_expiration_time}}"
            },
            {
                "is_ecommerce": false,
                "location_code": "US",
                "material_id": "{{material_id}}",
                "material_type": "IMAGE",
                "pre_review_status": "APPROVED",
                "reject_info_list": [],
                "result_creation_time": "{{result_creation_time}}",
                "result_expiration_time": "{{result_expiration_time}}"
            },
            {
                "is_ecommerce": false,
                "location_code": "US",
                "material_id": "{{material_id}}",
                "material_type": "AD_TEXT",
                "pre_review_status": "APPROVED",
                "reject_info_list": [],
                "result_creation_time": "{{result_creation_time}}",
                "result_expiration_time": "{{result_expiration_time}}"
            }
        ],
        "task_status": "SUCCESS"
    }
}
```
---

## Hướng dẫn thực hành Data Retrieval (Python & cURL)

Dưới đây là mã nguồn mẫu minh họa quy trình gọi API thực tế cho phân hệ **Tiền kiểm duyệt creative (Creative Pre-review)**:

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

