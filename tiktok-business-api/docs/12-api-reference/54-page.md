# Trang đích (Page)

> Phân hệ: apiref:Page.
> Tài liệu biên dịch kỹ thuật chi tiết theo chuẩn TikTok Business API v1.3.

---

## Mục lục điều hướng
- [1. Page (#doc-1737719918220290)](#doc-1737719918220290)
- [2. Get the Page ID (#doc-1820826387779586)](#doc-1820826387779586)
- [3. Create a TIP Editor SDK access token (#doc-1820826755283969)](#doc-1820826755283969)
- [4. Validate a TIP Editor SDK access token (#doc-1820826826000385)](#doc-1820826826000385)
- [5. Renew a TIP Editor SDK access token (#doc-1820826847199234)](#doc-1820826847199234)

---

<a id="doc-1737719918220290"></a>
<!-- doc_id: 1737719918220290 -->
<!-- doc_id: 1737719918220290 -->
# Page
> Đường dẫn: API Reference > Page
An instant page is a fast-loading lightweight web page that loads up to 11 times faster on TikTok than a standard web page. Page API enables you to retrieve the pages within an ad account, and create, validate or renew a TikTok Instant Page (TIP) Editor SDK access token. 

To learn more about different types of instant pages, see [Instant pages](../09-marketing-api/creatives.md#doc-1739953260466178). To learn about how to use the TIP Editor SDK, see [Instant Page Editor SDK](../09-marketing-api/creatives.md#doc-1740307202170881).

This group consists of the following endpoints:
- [Get the Page ID](54-page.md#doc-1820826387779586)
- [Create a TIP Editor SDK access token](54-page.md#doc-1820826755283969)
- [Validate a TIP Editor SDK access token](54-page.md#doc-1820826826000385)
- [Renew a TIP Editor SDK access token](54-page.md#doc-1820826847199234)

---

<a id="doc-1820826387779586"></a>
<!-- doc_id: 1820826387779586 -->
<!-- doc_id: 1820826387779586 -->
# Get the Page ID
> Đường dẫn: API Reference > Page > Get the Page ID
Sử dụng endpoint này để lấy thông tin the Page ID. After a page is created, you can get the page ID and then use the page ID in your ads.

## Yêu cầu gọi API (Request)
**Endpoint** https://business-api.tiktok.com/open_api/v1.3/page/get/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id **(Điều kiện)** | string | Either `advertiser_id` or `library_id` has to be set. ⏎ To get pages under an ad account, you must specify the ID tài khoản quảng cáo TikTok. |
| library_id **(Điều kiện)** | string | Either `advertiser_id` or `library_id` has to be set. ⏎ To get pages under a Business Center, you must specify the ID of the form library that contains the page and leads. You can migrate pages and leads from an ad account to a Business Center. |
| page | number | Current number of pages. ⏎ Giá trị mặc định: 1. Value range: ≥ 1. |
| page_size | number | Page size. ⏎ Giá trị mặc định: 10. Value range: 1-100. |
| status | string | Page status. ⏎ Các giá trị enum hỗ trợ: `EDITED` (draft), `PUBLISHED` (ready). |
| title | string | The page name for filtering results. ⏎ This filter supports exact matches. |
| update_time_range | object | Filter for pages updated in the specified time range. |
| ↳ start **(Điều kiện)** | string | Bắt buộc khi `update_time_range` is passed. ⏎ Start time in the format of `YYYY-MM-DD HH:MM:SS` (UTC time). ⏎ Example: `2024-01-01 00:00:00`. |
| ↳ end **(Điều kiện)** | string | Bắt buộc khi `update_time_range` is passed. ⏎ End time in the format of `YYYY-MM-DD HH:MM:SS` (UTC time). ⏎ Example: `2024-01-01 00:00:00`. |
| business_type | string | Page type. ⏎ Các giá trị enum hỗ trợ: `LEAD_GEN`(Instant Form), `STORE_FRONT`(Storefront Page), `APP_PROFILE_PAGE` (App Profile Page),`TIKTOK_INSTANT_PAGE` (Custom Page or Custom TikTok Instant Page), `SHOP_ADS_PLP` (Shop Ads Product List Page), `SHOP_ADS_PDP` (Shop Ads Product Detail Page), `POP_UP_FORM`(Direct Message Page). ⏎ Giá trị mặc định: `LEAD_GEN`. |
| business_types | string[] | Page types. ⏎ Các giá trị enum hỗ trợ: `LEAD_GEN`(Instant Form), `STORE_FRONT`(Storefront Page), `APP_PROFILE_PAGE` (App Profile Page),`TIKTOK_INSTANT_PAGE` (Custom Page or Custom TikTok Instant Page), `SHOP_ADS_PLP` (Shop Ads Product List Page), `SHOP_ADS_PDP` (Shop Ads Product Detail Page), `POP_UP_FORM`(Direct Message Page). ⏎ **Note**: If it is passed concurrently with `business_type`, the value of `business_type` will be ignored. |

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/page/get/?advertiser_id={{advertiser_id}}' \
--header 'Access-Token: {{Access-Token}}'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Mã trạng thái phản hồi (0: Thành công), see [Appendix-Return codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông điệp phản hồi từ máy chủ, see [Appendix-Return codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| data | object | Return data. |
| ↳ list | object[] | Page list. |
| ↳↳ page_id | string | Page ID. |
| ↳↳ status | string | Page status. ⏎ Các giá trị enum hỗ trợ: `EDITED` (draft), `PUBLISHED` (ready). |
| ↳↳ title | string | Title. |
| ↳↳ preview_url | string | Preview link of the page. The link is generated after the page is ready, and will be empty when the page is only a draft. |
| ↳↳ template_id | string | The ID for the page's template. It indicates the specific template type associated with this page. |
| ↳↳ template_name | string | The name of the template type that the page uses. |
| ↳↳ supported_objectives | string[] | Returned only when the following conditions are both met: • The page is associated with a `template_id`. • The corresponding template is compatible with certain objectives.A list of campaign objectives compatible with this page template. ⏎ Các giá trị enum hỗ trợ: `APP_PROMOTION`, `WEB_CONVERSIONS`, `LEAD_GENERATION`, `TRAFFIC`, `REACH`, `VIDEO_VIEWS`, `ENGAGEMENT`, `PRODUCT_SALES`, `RF_REACH`. ⏎ For a detailed explanation of enum values, see [Enumeration-Advertising Objective](https://business-api.tiktok.com/portal/docs/enumerations-appendix/v1.3#item-link-Advertising%20Objective). ⏎ **Note**: • Even with a supported objective, you can only use the page if it is compatible with all other campaign settings. |
| ↳↳ thumbnail | string | Page preview thumbnail image. |
| ↳↳ create_time | string | The Thời gian tạo of the page in the format of `YYYY-MM-DD HH:MM:SS` (UTC time). ⏎ Example: `2024-01-01 00:00:00`. |
| ↳↳ update_time | string | The time the page was last updated in the format of `YYYY-MM-DD HH:MM:SS` (UTC time). ⏎ Example: `2024-01-01 00:00:00`. |
| ↳↳ publish_time | string | The publishing time of the page in the format of `YYYY-MM-DD HH:MM:SS` (UTC time). ⏎ Example: `2024-01-01 00:00:00`. |
| ↳↳ app_id | string | Returned for all App Profile Pages and TikTok Instant Pages where an App is specified. ⏎ The ID of the App that is specified in the page. ⏎ To filter App Profile Pages, set `business_type` to `APP_PROFILE_PAGE` or set `business_types` to `["APP_PROFILE_PAGE"]` in the request. |
| ↳↳ has_cpp | boolean | Returned only for TikTok Instant Pages. ⏎ Liệu TikTok Instant Page contains [Custom Product Page](../09-marketing-api/quan-ly-chien-dich-tom-tat.md#doc-1798658439859202). ⏎ Các giá trị enum hỗ trợ: `true`, `false`. ⏎ To filter TikTok Instant Pages, set `business_type` to `TIKTOK_INSTANT_PAGE` or set `business_types` to `["TIKTOK_INSTANT_PAGE"]` in the request. |
| ↳↳ destination_urls | string[] | Returned when your `business_type` is`LEAD_GEN`(Instant Form), `APP_PROFILE_PAGE` (App Profile Page), or `TIKTOK_INSTANT_PAGE` (Custom Page or Custom TikTok Instant Page). ⏎ Destination URLs. |
| ↳↳ messaging_app_type | string | The type of instant messaging app associated with the TikTok Instant Page. ⏎ Các giá trị enum hỗ trợ: • `MESSENGER`: Messenger.  • `WHATSAPP`: WhatsApp.  • `IM_URL`: No instant messaging app is associated with the TikTok Instant Page. |
| ↳↳ messaging_app_account_id | string | The ID of the instant messaging app account associated with the TikTok Instant Page. ⏎ • When `messaging_app_type` is `MESSENGER`, this field represents the Facebook Page ID. • When `messaging_app_type` is `WHATSAPP`, this field represents the WhatsApp phone number. • When `messaging_app_type` is `IM_URL`, this field will be an empty string (`""`). |
| ↳↳ transfer_status | string | Liệu page has been transferred to Business Center. ⏎ Các giá trị enum hỗ trợ: `UNSET`, `TRANSFERRED` |
| ↳↳ user_id | string | ID of the user who created the page. |
| ↳↳ is_associated | boolean | Liệu Storefront Page has been associated with some ad (Storefront Page cannot be reused, and each page can only be associated with one ad). |
| ↳↳ duplicate_id | string | Duplicate source page ID. |
| ↳ page_info | object | Pagination information. |
| ↳↳ page | number | Current page. |
| ↳↳ page_size | number | Page size. |
| ↳↳ total_number | number | Tổng số kết quả tìm thấy. |
| ↳↳ total_page | number | Tổng số trang. |
| request_id | string | Log id of the request, uniquely identifying a request. |

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
                "create_time": "{{create_time}}",
                "destination_urls": [],
                "duplicate_id": "{{duplicate_id}}",
                "page_id": "{{page_id}}",
                "preview_url": "{{preview_url}}",
                "publish_time": "{{publish_time}}",
                "status": "PUBLISHED",
                "supported_objectives": [
                    "LEAD_GENERATION"
                ],
                "template_id": "{{template_id}}",
                "template_name": "{{template_name}}",
                "thumbnail": "{{thumbnail}}",
                "title": "{{title}}",
                "transfer_status": "UNSET",
                "update_time": "{{update_time}}",
                "user_id": "{{user_id}}"
            }
        ],
        "page_info": {
            "page": 1,
            "page_size": 10,
            "total_number": 1,
            "total_page": 1
        }
    }
}
```

---

<a id="doc-1820826755283969"></a>
<!-- doc_id: 1820826755283969 -->
<!-- doc_id: 1820826755283969 -->
# Create a TIP Editor SDK access token
> Đường dẫn: API Reference > Page > Create a TIP Editor SDK access token
Sử dụng endpoint này để tạo a TikTok Instant Page (TIP) Editor SDK access token. 

The TIP Editor SDK access token is required for loading the TIP Editor SDK. Once the token is generated, you can learn about how to [create Instant Pages using the TIP Editor SDK](../09-marketing-api/creatives.md#doc-1740307202170881).

Each TIP Editor SDK access token is valid for 24 hours. You can verify Liệu an SDK token expires using [/oauth2/access_token/tip_sdk/validate/](54-page.md#doc-1820826826000385) and renew the token using [/oauth2/access_token/tip_sdk/renew/](54-page.md#doc-1820826847199234) after the token expires.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/oauth2/access_token/tip_sdk/create/

**Method** POST

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). ⏎ Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type  ****(Bắt buộc)**** | string | Định dạng dữ liệu yêu cầu. ⏎ Allowed format: `application/json`. |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
| advertiser_id ***(Bắt buộc)*** | string | ID tài khoản quảng cáo TikTok. |

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location  --request POST 'https://business-api.tiktok.com/open_api/v1.3/oauth2/access_token/tip_sdk/create/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id": "{{advertiser_id}}"
}'
```
## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|code |number|Response code. For the complete list of response codes and descriptions, see [Appendix-Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message|string|Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|request_id |string|The log ID of a request, which uniquely identifies the request.  |
|data |object|Returned data.|
#| tip_sdk_access_token | string | The temporary TIP Editor SDK access token. <br><br>You can pass the token to the `ixAccessToken` parameter in the SDK function `InstantPage.start()` for invoking the TIP Editor. To learn about how to load the TIP SDK to create instant pages, see [Instant Page Editor SDK](../09-marketing-api/creatives.md#doc-1740307202170881).<br><br>The token is valid for 24 hours. After the token expires, you can either renew the token using [/oauth2/access_token/tip_sdk/renew/](54-page.md#doc-1820826847199234) or create a new token using [/oauth2/access_token/tip_sdk/create/](54-page.md#doc-1820826755283969).|

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "tip_sdk_access_token": "{{tip_sdk_access_token}}"
    }
}
```

---

<a id="doc-1820826826000385"></a>
<!-- doc_id: 1820826826000385 -->
<!-- doc_id: 1820826826000385 -->
# Validate a TIP Editor SDK access token
> Đường dẫn: API Reference > Page > Validate a TIP Editor SDK access token
Use this endpoint to verify Liệu a TikTok Instant Page (TIP) Editor SDK access token has expired.

Once you confirm a token has expired, you can renew the token using [/oauth2/access_token/tip_sdk/renew/](54-page.md#doc-1820826847199234).

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/oauth2/access_token/tip_sdk/validate/

**Method** POST

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). ⏎ Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type  ****(Bắt buộc)**** | string | Định dạng dữ liệu yêu cầu. ⏎ Allowed format: `application/json`. |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
| advertiser_id ***(Bắt buộc)*** | string | ID tài khoản quảng cáo TikTok. |
| tip_sdk_access_token ***(Bắt buộc)*** | string | A TIP Editor SDK access token.<br><br>If you want to create a new TIP Editor SDK access token, use [/oauth2/access_token/tip_sdk/create/](54-page.md#doc-1820826755283969).|

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location  --request POST 'https://business-api.tiktok.com/open_api/v1.3/oauth2/access_token/tip_sdk/validate/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id": "{{advertiser_id}}",
    "tip_sdk_access_token": "{{tip_sdk_access_token}}"
}'
```
## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|code |number|Response code. For the complete list of response codes and descriptions, see [Appendix-Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message|string|Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|request_id |string|The log ID of a request, which uniquely identifies the request.  |
|data |object|Returned data.|
#|is_valid| boolean |Liệu access token is valid. <br><br>Các giá trị được hỗ trợ: `true`, `false`.|

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "is_valid": true
    }
}
```

---

<a id="doc-1820826847199234"></a>
<!-- doc_id: 1820826847199234 -->
<!-- doc_id: 1820826847199234 -->
# Renew a TIP Editor SDK access token
> Đường dẫn: API Reference > Page > Renew a TIP Editor SDK access token
Use this endpoint to renew a TikTok Instant Page (TIP) Editor SDK access token. 

Once renewed, the same token will remain valid for another 24 hours.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/oauth2/access_token/tip_sdk/renew/

**Method** POST

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). ⏎ Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type  ****(Bắt buộc)**** | string | Định dạng dữ liệu yêu cầu. ⏎ Allowed format: `application/json`. |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
| advertiser_id ***(Bắt buộc)*** | string | ID tài khoản quảng cáo TikTok. |
| tip_sdk_access_token ***(Bắt buộc)*** | string | A TIP Editor SDK access token.<br><br>If you want to create a new TIP Editor SDK access token, use [/oauth2/access_token/tip_sdk/create/](54-page.md#doc-1820826755283969).|

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location  --request POST 'https://business-api.tiktok.com/open_api/v1.3/oauth2/access_token/tip_sdk/renew/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id": "{{advertiser_id}}",
    "tip_sdk_access_token": "{{tip_sdk_access_token}}"
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

## Hướng dẫn thực hành Data Retrieval (Python & cURL)

Dưới đây là mã nguồn mẫu minh họa quy trình gọi API thực tế cho phân hệ **Trang đích (Page)**:

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

