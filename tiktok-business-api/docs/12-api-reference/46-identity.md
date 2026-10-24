# Danh tính (Identity)

> Phân hệ: apiref:Identity.
> Tài liệu biên dịch kỹ thuật chi tiết theo chuẩn TikTok Business API v1.3.

---

## Mục lục điều hướng
- [1. Tổng quan Danh tính (Identity) (#doc-1740133137507393)](#doc-1740133137507393)
- [2. Tạo danh tính tùy chỉnh (Create an identity) (#doc-1740654203526146)](#doc-1740654203526146)
- [3. Xóa danh tính tùy chỉnh (Delete an identity) (#doc-1759155939236865)](#doc-1759155939236865)
- [4. Lấy danh sách danh tính (Get the identity list) (#doc-1740218420781057)](#doc-1740218420781057)
- [5. Lấy thông tin chi tiết danh tính (Get info about an identity) (#doc-1740218453385217)](#doc-1740218453385217)
- [6. Lấy danh sách bài đăng theo danh tính (Get posts under an identity) (#doc-1740218475032577)](#doc-1740218475032577)
- [7. Lấy video phát trực tiếp theo danh tính (Get live videos under an identity) (#doc-1785238052792321)](#doc-1785238052792321)
- [8. Kiểm tra thông tin ủy quyền âm nhạc của video (#doc-1740218495869954)](#doc-1740218495869954)
- [9. Lấy thông tin chi tiết bài đăng TikTok (Get info about TikTok posts) (#doc-1740218522178562)](#doc-1740218522178562)

---

<a id="doc-1740133137507393"></a>
<!-- doc_id: 1740133137507393 -->
<!-- doc_id: 1740133137507393 -->
# Tổng quan Danh tính (Identity)
> Đường dẫn: API Reference > Identity
Tính năng Danh tính (Identity) cho phép bạn lựa chọn cách thức hiển thị thương hiệu và doanh nghiệp của mình trong các mẫu quảng cáo TikTok. Identity API cho phép bạn tạo hoặc xóa danh tính tùy chỉnh (Custom User identity), lấy danh sách danh tính trực thuộc tài khoản quảng cáo, lấy bài đăng theo danh tính và truy vấn thông tin chi tiết của danh tính hoặc bài đăng TikTok. 

Xem [Danh tính (Identities)](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1738958351620097) để tìm hiểu thêm về các loại danh tính được ủy quyền trên TikTok.

Nhóm API này bao gồm các endpoint sau:
* [Create an identity](46-identity.md#doc-1740654203526146)
* [Delete an identity](46-identity.md#doc-1759155939236865)
* [Get the identity list](46-identity.md#doc-1740218420781057)
* [Get info about an identity](46-identity.md#doc-1740218453385217)
* [Get posts under an identity](46-identity.md#doc-1740218475032577)
* [Get live videos under an identity](46-identity.md#doc-1785238052792321)
* [Get music authorization info of a video](46-identity.md#doc-1740218495869954)
* [Get info about TikTok posts](46-identity.md#doc-1740218522178562)

---

<a id="doc-1740654203526146"></a>
<!-- doc_id: 1740654203526146 -->
<!-- doc_id: 1740654203526146 -->
# Tạo danh tính tùy chỉnh (Create an identity)
> Đường dẫn: API Reference > Identity > Create an identity
Sử dụng endpoint này để tạo a Custom User (`CUSTOMIZED_USER`) identity.

## Yêu cầu gọi API (Request)

**Endpoint**

https://business-api.tiktok.com/open_api/v1.3/identity/create/

**Method** POST

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|Access-Token***(Bắt buộc)***|string|Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162).|
|Content-Type***(Bắt buộc)***|string|Định dạng dữ liệu của yêu cầu. <br>Giá trị hợp lệ: `application/json`.|

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id ***(Bắt buộc)*** | string | ID tài khoản quảng cáo TikTok. |
| display_name ***(Bắt buộc)*** | string | Tên hiển thị của danh tính. <br><br>Độ dài tối đa 100 ký tự. |
| image_uri  | string |Mã `image_id` của hình ảnh đại diện cho danh tính. <br><br>Tỷ lệ khung hình bắt buộc là 1:1. <br><br>Để lấy mã ảnh đại diện, bạn có thể tải ảnh lên bằng [/file/image/ad/upload/](47-images.md#doc-1739067433456642). <br><br>Nếu không chỉ định, hình ảnh mặc định sẽ được dùng làm ảnh đại diện.|

### Ví dụ lệnh cURL (Example)

```http
// curl
curl -H "Access-Token:xxx" -H "Content-Type:application/json" -X POST \
-d '{
    "advertiser_id": "ADVERTISER_ID",
    "image_uri": "IMAGE_URI",
    "display_name": "DISPLAY_NAME"
}' \
https://business-api.tiktok.com/open_api/v1.3/identity/create/
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|code |number | Response code. For the complete list of response codes and descriptions, see [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|message |string | Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|data |object| Returned data. |
#|identity_id|string|Identity ID.|
|request_id|string|The log id of the request, which uniquely identifies a request. |

### Ví dụ lệnh cURL (Example)

```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "LOG_ID",
    "data": {
        "identity_id": "IDENTITY_ID"
    }
}
```

---

<a id="doc-1759155939236865"></a>
<!-- doc_id: 1759155939236865 -->
<!-- doc_id: 1759155939236865 -->
# Xóa danh tính tùy chỉnh (Delete an identity)
> Đường dẫn: API Reference > Identity > Delete an identity
Sử dụng endpoint này để xóa a customized user identity (`identity_type` = `CUSTOMIZED_USER`). If you want to edit an identity, you need to first delete the identity using this endpoint, and then create a new one using [/v1.3/identity/create/](46-identity.md#doc-1740654203526146).

## Yêu cầu gọi API (Request)

**Endpoint**

https://business-api.tiktok.com/open_api/v1.3/identity/delete/ 

**Method** POST

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|Access-Token***(Bắt buộc)***|string|Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162).|
|Content-Type***(Bắt buộc)***|string|Định dạng dữ liệu của yêu cầu. <br>Giá trị hợp lệ: `application/json`.|

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id ***(Bắt buộc)*** | string | ID tài khoản quảng cáo TikTok. |
| identity_id  ***(Bắt buộc)*** | string | Identity ID.
| identity_type  ***(Bắt buộc)*** | string | Identity type. Currently, this field only supports `CUSTOMIZED_USER`. 

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location  --request POST 'https://business-api.tiktok.com/open_api/v1.3/identity/delete/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id":"{{advertiser_id}}",
    "identity_id":"{{identity_id}}",
    "identity_type":"CUSTOMIZED_USER"
}'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|code |number | Response code. For the complete list of response codes and descriptions, see [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|message |string | Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|data |object| Returned data. |
|request_id|string|The log ID of the request, which uniquely identifies a request. |

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

<a id="doc-1740218420781057"></a>
<!-- doc_id: 1740218420781057 -->
<!-- doc_id: 1740218420781057 -->
# Lấy danh sách danh tính (Get the identity list)
> Đường dẫn: API Reference > Identity > Get the identity list
Sử dụng endpoint này để lấy thông tin a list of identities under an ad account. You can filter results by identity type or display name.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/identity/get/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|Access-Token***(Bắt buộc)***|string|Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162).|

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id ***(Bắt buộc)*** | string | ID tài khoản quảng cáo TikTok. |
| identity_type | string | Identity type.<br><br> Các giá trị enum hỗ trợ: `CUSTOMIZED_USER`, `AUTH_CODE`, `TT_USER`, `BC_AUTH_TT`. See [Identities](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1738958351620097) for details.<br><br>If this field is not specified, all identities will be returned. <br><br><p><span style="color:darkred"><b>Note</b></span>: If you set this field to `BC_AUTH_TT` and specify `identity_authorized_bc_id`, all identities linked to the ad account (`advertiser_id`) will be returned.</p>|
| identity_authorized_bc_id **(Điều kiện)**| string |Bắt buộc khi `identity_type` is `BC_AUTH_TT`. <br><br>ID of the Business Center that a TikTok Account User in Business Center identity is associated with.  |
|filtering|object|Điều kiện lọc dữ liệu.<br><br><p><span style="color:darkred"><b>Note</b></span><br>This field is Chỉ hợp lệ khi `identity_type` = `CUSTOMIZED_USER` or when `identity_type` is not specified.|
#|keyword|string|Keyword to filter by. <br><br>When `identity_type` = `CUSTOMIZED_USER`, you can use fuzzy matching by specifying display name to this field.|
| page | number | Current Số trang cần lấy dữ liệu.<br><br>Giá trị mặc định: 1.|
| page_size | number | Page size..<br><br>Value range: 1-100.<br><br>Giá trị mặc định: 20.|

### Ví dụ lệnh cURL (Example)

```http
// curl
curl --location  --request GET 'https://business-api.tiktok.com/open_api/v1.3/identity/get/?advertiser_id={{advertiser_id}}&identity_type=TT_USER' \
--header 'Access-Token: {{Access-Token}}'
```
## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|code |number | Response code. For the complete list of response codes and descriptions, see [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|message |string | Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|request_id|string|The log id of the request, which uniquely identifies a request. |
|data |object| Returned data. |
#| identity_list | object[] | List of identities. |
##| identity_id | string | Identity ID. |
##| identity_type | string | Identity type. |
##| identity_authorized_bc_id | string |ID of the Business Center that a TikTok Account User in Business Center identity is associated with.|
##| ads_only_mode | boolean | Liệu "Show through ads only" mode is enabled for the identity.<br><br>Các giá trị được hỗ trợ: `true`, `false`.<br>This field returns a non-null value when `identity_type` is `BC_AUTH_TT`.<br><br>When this field is `true`, you cannot set `dark_post_status` to `OFF` while creating ads (through [/smart_plus/ad/create/](62-upgraded-smartplus-p5.md#doc-1843317390059522), [/ad/create/](02-ads-p1.md#doc-1739953377508354), or [/campaign/spc/create/](61-to-be-deprecated-legacy-smartplus.md#doc-1767334204047362)) or updating ads (through [/smart_plus/ad/update/](62-upgraded-smartplus-p6.md#doc-1843317411665921), [/ad/update/](02-ads-p2.md#doc-1739953405142018), or [/campaign/spc/update/](61-to-be-deprecated-legacy-smartplus.md#doc-1767334250066945)) to allow your post to appear on your TikTok profile and be eligible to receive organic traffic. |
##| username | string | The username (handle name) of the identity. |
##|is_gpppa|boolean|Liệu TikTok account is a [Government, Politician, and Political Party Account](https://support.tiktok.com/en/using-tiktok/growing-your-audience/government-politician-and-political-party-accounts) (GPPPA).<br><br>Các giá trị được hỗ trợ: `true`, `false`.<br><br>When this field is `true`, the TikTok account cannot be used to [create Spark Ads](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1739470744631298).|
##| can_push_video | boolean | Liệu `BC_AUTH_TT` or `TT_USER` identity can create or edit videos. <br><br> Các giá trị được hỗ trợ: `true`, `false`.|
##| can_pull_video | boolean | Liệu `BC_AUTH_TT` or `TT_USER` identity can get all videos under the TikTok account. <br><br> Các giá trị được hỗ trợ: `true`, `false`.|
##| can_use_live_ads | boolean | Liệu `BC_AUTH_TT`or `TT_USER` identity can access the live room. <br><br> Các giá trị được hỗ trợ: `true`, `false`.|
##| can_manage_message | boolean | Liệu `BC_AUTH_TT` or `TT_USER` identity can manage direct messages.<br><br> Các giá trị được hỗ trợ: `true`, `false`.|
##|can_use_showcase|boolean|Liệu `BC_AUTH_TT` or `TT_USER` identity can access products from Showcase.<br><br>Các giá trị được hỗ trợ: `true`, `false`.|
##|can_use_series|boolean|Liệu `BC_AUTH_TT` or `TT_USER` identity can access TikTok Series.<br><br>Các giá trị được hỗ trợ: `true`, `false`.|
##| display_name | string | Display name. |
##| available_status | string | Availability of the identity. Only valid for `TT_USER` and `BC_AUTH_TT` type of identities. Các giá trị enum hỗ trợ: `AVAILABLE`, `NO_VALID_BIND_ACCOUNT`, `SCOPE_UNAVAILABLE`,` IS_PRIVATE_ACCOUNT`, `NOT_BUSINESS_ACCOUNT`. |
##| profile_image | string | Profile image URL. |
#| page_info | object | Pagination information. <br><br><p><span style="color:darkred"><b>Note</b></span>: Correct pagination info is available only when you have specified `identity_type` in the request.|
##| page | number | Current Số trang cần lấy dữ liệu. |
##| total_page | number | Tổng số trang. |
##| total_number | number | Tổng số kết quả tìm thấy. |
##| page_size | number | Số lượng kết quả trên mỗi trang. |

### Ví dụ lệnh cURL (Example)

```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "page_info": {
            "total_number": 1,
            "page_size": 20,
            "total_page": 1,
            "page": 1
        },
        "identity_list": [
            {
                "ads_only_mode": null,
				        "profile_image": "{{profile_image}}",
                "identity_type": "TT_USER",
                "identity_id": "{{identity_id}}",
                "can_pull_video": true,
                "display_name": "{{display_name}}",
                "identity_authorized_bc_id": null,
                "can_push_video": true,
                "can_use_live_ads": true,
                "can_manage_message": true,
                "can_use_series": true,
                "can_use_showcase": true,
                "available_status": "AVAILABLE",
                "is_gpppa": false,
                "username": "{{username}}"
            }
        ]
    }
}
```

---

<a id="doc-1740218453385217"></a>
<!-- doc_id: 1740218453385217 -->
<!-- doc_id: 1740218453385217 -->
# Lấy thông tin chi tiết danh tính (Get info about an identity)
> Đường dẫn: API Reference > Identity > Get info about an identity
Sử dụng endpoint này để truy xuất details about an identity.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/identity/info/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|Access-Token***(Bắt buộc)***|string|Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162).|

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id ***(Bắt buộc)*** | string | ID tài khoản quảng cáo TikTok. |
| identity_id ***(Bắt buộc)*** | string | Identity ID. |
| identity_type***(Bắt buộc)***  | string | Identity type. Các giá trị enum hỗ trợ: `CUSTOMIZED_USER`, `AUTH_CODE`, `TT_USER`, `BC_AUTH_TT`. See [Identities](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1738958351620097) for details. |
| identity_authorized_bc_id **(Điều kiện)**| string |ID of the Business Center that a TikTok Account User in Business Center identity is associated with. Bắt buộc khi `identity_type` is `BC_AUTH_TT`. |

### Ví dụ lệnh cURL (Example)

```http
// curl
curl --location  --request GET 'https://business-api.tiktok.com/open_api/v1.3/identity/info/?advertiser_id={{advertiser_id}}&identity_type=TT_USER&identity_id={{identity_id}}' \
--header 'Access-Token: {{Access-Token}}'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|code |number | Response code. For the complete list of response codes and descriptions, see [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|message |string | Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|data |object| Returned data. |
#| identity_info | object | Identity information. |
##| identity_id | string | Identity ID. |
##| identity_type | string | Identity type. Các giá trị enum hỗ trợ: `CUSTOMIZED_USER`, `AUTH_CODE`, `TT_USER`, `BC_AUTH_TT`. See [Identities](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1738958351620097)  for details. |
##| identity_authorized_bc_id | string | ID of the Business Center that a TikTok Account User in Business Center identity is associated with.|
##|ads_only_mode|boolean|Returned only when `identity_type` is `BC_AUTH_TT`.<br><br>Liệu "Show through ads only" mode is enabled for the identity.<br><br>Các giá trị được hỗ trợ: `true`, `false`.<br><br>When this field is `true`, you cannot set `dark_post_status` to `OFF` while creating ads (through [/smart_plus/ad/create/](62-upgraded-smartplus-p5.md#doc-1843317390059522), [/ad/create/](02-ads-p1.md#doc-1739953377508354), or [/campaign/spc/create/](61-to-be-deprecated-legacy-smartplus.md#doc-1767334204047362)) or updating ads (through [/smart_plus/ad/update/](62-upgraded-smartplus-p6.md#doc-1843317411665921), [/ad/update/](02-ads-p2.md#doc-1739953405142018), or [/campaign/spc/update/](61-to-be-deprecated-legacy-smartplus.md#doc-1767334250066945)) to allow your post to appear on your TikTok profile and be eligible to receive organic traffic.</p>|
##| username | string | The username (handle name) of the identity. |
##|is_gpppa|boolean|Liệu TikTok account is a [Government, Politician, and Political Party Account](https://support.tiktok.com/en/using-tiktok/growing-your-audience/government-politician-and-political-party-accounts) (GPPPA).<br><br>Các giá trị được hỗ trợ: `true`, `false`.<br><br>When this field is `true`, the TikTok account cannot be used to [create Spark Ads](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1739470744631298).|
##| can_push_video | boolean | Liệu `BC_AUTH_TT` or `TT_USER` identity can create or edit videos. <br><br> Các giá trị được hỗ trợ: `true`, `false`.|
##| can_pull_video | boolean | Liệu `BC_AUTH_TT` or `TT_USER` identity can get all videos under the TikTok account. <br><br> Các giá trị được hỗ trợ: `true`, `false`.|
##| can_use_live_ads | boolean | Liệu `BC_AUTH_TT`or `TT_USER` identity can access the live room. <br><br> Các giá trị được hỗ trợ: `true`, `false`.|
##| can_manage_message | boolean | Liệu `BC_AUTH_TT` or `TT_USER` identity can manage direct messages.<br><br> Các giá trị được hỗ trợ: `true`, `false`.|
##|can_use_showcase|boolean|Liệu `BC_AUTH_TT` or `TT_USER` identity can access products from Showcase.<br><br>Các giá trị được hỗ trợ: `true`, `false`.|
##|can_use_series|boolean|Liệu `BC_AUTH_TT` or `TT_USER` identity can access TikTok Series.<br><br>Các giá trị được hỗ trợ: `true`, `false`.|
##| display_name | string | Display name. |
##| profile_image_url | string | Profile image URL. |
##| available_status | string | Availability of the identity. Only valid for `TT_USER` and `BC_AUTH_TT` type of identities. Các giá trị enum hỗ trợ: `AVAILABLE`, `NO_VALID_BIND_ACCOUNT`, `SCOPE_UNAVAILABLE`, `IS_PRIVATE_ACCOUNT`, `NOT_BUSINESS_ACCOUNT`. |
|request_id|string|The log id of the request, which uniquely identifies a request. |

### Ví dụ lệnh cURL (Example)

```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "identity_info": {
			"available_status": "AVAILABLE",
            "can_manage_message": true,
            "can_pull_video": true,
            "can_push_video": true,
            "can_use_live_ads": true,
            "can_use_series": true,
            "can_use_showcase": true,
            "display_name": "{{display_name}}",
            "identity_id": "{{identity_id}}",
            "identity_type": "TT_USER",
            "profile_image_url": "{{profile_image_url}}",
            "is_gpppa": false,
            "username": "{{username}}"
        }
    }
}
```

---

<a id="doc-1740218475032577"></a>
<!-- doc_id: 1740218475032577 -->
<!-- doc_id: 1740218475032577 -->
# Lấy danh sách bài đăng theo danh tính (Get posts under an identity)
> Đường dẫn: API Reference > Identity > Get posts under an identity
Sử dụng endpoint này để lấy thông tin all posts under an identity.

## Yêu cầu gọi API (Request)

**Endpoint**

https://business-api.tiktok.com/open_api/v1.3/identity/video/get/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|Access-Token***(Bắt buộc)***|string|Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162).|

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id ***(Bắt buộc)*** | string | ID tài khoản quảng cáo TikTok. |
| identity_id ***(Bắt buộc)*** | string | Identity ID.|
| identity_type ***(Bắt buộc)*** | string | Identity type. Các giá trị enum hỗ trợ: `AUTH_CODE`, `TT_USER`, `BC_AUTH_TT`. See [Identities](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1738958351620097) for details. |
| identity_authorized_bc_id**(Điều kiện)** | string | ID of the Business Center that a TikTok Account User in Business Center identity is associated with. Bắt buộc khi `identity_type` is `BC_AUTH_TT`.  |
| item_type | string | The type of TikTok posts that you want to retrieve. <br><br>Các giá trị enum hỗ trợ: <ul><li> `VIDEO`: video post. </li><li>`CAROUSEL`: photo post. </li></ul><br>Giá trị mặc định: `VIDEO`. |
|keyword|string| Chỉ hợp lệ khi `identity_type` is set to `AUTH_CODE`. Otherwise, an error will occur.<br><br>The text or TikTok post ID as a keyword to search TikTok posts by.<br><br><ul><li>If you want to search for TikTok posts based on text, provide a text string with a maximum length of 500 characters. This search type supports searching in multiple languages and fuzzy matches.<br> Example: "summer".</li><li> If you want to search for TikTok posts based on `item_id`, provide a numeric string with a minimum length of 19 characters. This search type supports exact matches.<br>  Example: "1234567891234567891" |
|exclude_adsonly|boolean|Có thực hiện exclude ads only posts from the results.<br>Ads-only posts are those you publish from a TikTok account as ads, which remain hidden from the public on the account's profile page.<br><br>Các giá trị được hỗ trợ: <ul><li>`false`: To retrieve both organic and ads only posts.</li><li>`true`: To retrieve a maximum of 500 most recent organic posts.</li></ul><br>Giá trị mặc định: `false`.|
| cursor | integer | Cursor for pagination.|
| count | number | Number of TikTok posts you want to get. <br><br>Value range: 1-20.<br>If you specify a value greater than 20, this field will be ignored and a maximum of 20 TikTok posts associated with the identity will be returned.|

### Ví dụ lệnh cURL (Example)

```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/identity/video/get/?advertiser_id={{advertiser_id}}&identity_type=TT_USER&identity_id={{identity_id}}' \
--header 'Access-Token: {{Access-Token}}'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|code |number | Response code. For the complete list of response codes and descriptions, see [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|message |string | Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|data |object| Returned data. |
#| cursor | string | Timestamp cursor or cursor for pagination.<ul><li>If `identity_type` is `TT_USER` or `BC_AUTH_TT` :<ul><li>When `exclude_adsonly` is `false` in the request, `cursor` is the time value of the last item returned according to the current request. You need to use this cursor value in your subsequent request to get the next posts.</li><li>When `exclude_adsonly` is `true` in the request, `cursor` is the cursor for pagination. If `has_more` in the response is `true`, you need to use the returned `cursor` in the subsequent request to receive the next page of results.</li></ul></li><li>If `identity_type` is `AUTH_CODE`, `cursor` is the cursor for pagination. If `has_more` in the response is `true`, you need to use the returned `cursor` in the subsequent request to receive the next page of results.</li></ul> |
#| has_more | bool | Liệu more data is available. |
#| video_list | object[] | List of posts. |
##| item_type | string | The type of TikTok post. <br><br>Các giá trị enum hỗ trợ: <ul><li> `VIDEO`: video post. </li><li>`CAROUSEL`: photo post. </li></ul>|
##| item_id | string | TikTok post ID. |
##| status | string | Status of the TikTok post. <br><br>Các giá trị enum hỗ trợ: <ul><li> `ITEM_STATUS_HESITATE_RECOMMEND`: visible to all. </li><li>`STATUS_ONLY_FRIEND_SEE`: visible to friends.</li><li>`ITEM_STATUS_ONLY_AUTHOR_SEE`: private.</li></ul>  |
##| text | string | Text for the TikTok post. |
##| auth_info | object | Authorization Information. |
###| ad_auth_status | string | Authorization status. |
###| auth_end_time | string | Time when the authorization code is valid from (UTC+0), in the format of 2017-01-01 00:00:00. |
###| auth_start_time | string | Time when the authorization code is valid from (time zone: UTC+0), in the format of 2017-01-01 00:00:00. |
###| invite_start_time| string | The time when the authorization starts (UTC+0), in the format of 2017-01-01 00:00:00. |
##| anchor_list | object | Information about anchors. |
###| anchor_id | string | Anchor ID. |
###| title | string | Anchor title. |
###| status | string | Anchor status. Các giá trị enum hỗ trợ: `CHECK_ING`, `CHECK_FAILED`, `CHECK_SUCCESS`. |
###| url | string | Anchor URL. |
###| product_regions | string[] | Regions that the ad can be delivered to. This is a list of country or region codes. For example, `["DE"]`. |
##| video_info | object | Information about the video post.<br><br><p><span style="color:darkred"><b>Note</b></span>: When `item_type` is `CAROUSEL`, the value of this field will be null. |
###| bit_rate | integer| Bit rates, in bps. |
###| duration | float | Duration of the video, in seconds. |
###| size | integer | Video size, in bytes. |
###| height | integer | Video height. |
###| width | integer| Video width. |
###| poster_url | string | URL to the video poster. <br>The expiration time is included in the URL after the `x-expires` parameter, in the format of an Epoch/Unix timestamp in seconds.  <br>When it expires, you need to call this endpoint to get a new URL. |
###| signature | string | MD5 for the video file. |
###| url | string | Video preview link. <br> It is valid for an hour.  <br>When it expires, you need to call the endpoint again to get a new URL. |
###| format | string | Format of the video. |
##| carousel_info | object | Information about the photo post. <br> <br><p><span style="color:darkred"><b>Note</b></span>: When `item_type` is `VIDEO`, the value of this field will be null. |
###| image_info | object[] | Information about the images used in the photo post. <br> <br>The images are returned in the same order as they are shown in the photo post. |
####| image_id | string | Image ID. |
####| image_url | string | The URL of the image. <br> <br>Validity period: 90 days. |
####| image_height | integer | The height of the image, measured in pixels. |
####| image_width | integer| The width of the image, measured in pixels. |
###| music_info | object | Information about the music used in the photo post. <br> <br><p><span style="color:darkred"><b>Note</b></span>: If the photo post is directly published in the TikTok App without music, the value of this field will be null.   |
####| music_id | string | Music ID. |
####|music_url | string | The URL of the music. <br> <br>Validity period: 90 days. |
####| music_duration |integer | The duration of the music, in seconds. |
|request_id|string|The log id of the request, which uniquely identifies a request. |

### Ví dụ lệnh cURL (Example)

```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "cursor": "1780432720000",
        "has_more": true,
        "video_list": [
            {
                "anchor_list": null,
                "auth_info": null,
                "carousel_info": null,
                "item_id": "{{item_id}}",
                "item_type": "VIDEO",
                "status": "ITEM_STATUS_HESITATE_RECOMMEND",
                "text": "{{text}}",
                "video_info": {
                    "bit_rate": 15184988,
                    "duration": 13.8,
                    "format": "mp4",
                    "height": 1920,
                    "poster_url": "{{poster_url}}",
                    "signature": "{{signature}}",
                    "size": 26194106,
                    "url": "{{url}}",
                    "width": 1080
                }
            },
            {
                "anchor_list": null,
                "auth_info": null,
                "carousel_info": null,
                "item_id": "{{item_id}}",
                "item_type": "VIDEO",
                "status": "ITEM_STATUS_HESITATE_RECOMMEND",
                "text": "{{text}}",
                "video_info": {
                    "bit_rate": 990999,
                    "duration": 16,
                    "format": "mp4",
                    "height": 1280,
                    "poster_url": "{{poster_url}}",
                    "signature": "{{signature}}",
                    "size": 1981998,
                    "url": "{{url}}",
                    "width": 720
                }
            }
        ]
    }
}
```

---

<a id="doc-1785238052792321"></a>
<!-- doc_id: 1785238052792321 -->
<!-- doc_id: 1785238052792321 -->
# Lấy danh sách video phát trực tiếp theo danh tính (Get live videos under an identity)
> Đường dẫn: API Reference > Identity > Get live videos under an identity
Sử dụng endpoint này để lấy thông tin live videos under an identity. 

## Yêu cầu gọi API (Request)

**Endpoint**

https://business-api.tiktok.com/open_api/v1.3/identity/live/get/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|Access-Token***(Bắt buộc)***|string|Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162).|
|Content-Type***(Bắt buộc)***|string|Định dạng dữ liệu yêu cầu. <br>Allowed value: `application/json`.|

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id ***(Bắt buộc)*** | string | ID tài khoản quảng cáo TikTok.  |
| identity_id ***(Bắt buộc)*** | string | Identity ID. |
| identity_type ***(Bắt buộc)*** | string | Identity type.  Các giá trị enum hỗ trợ: `TT_USER`, `BC_AUTH_TT`. See Identities for details. |
| identity_authorized_bc_id **(Điều kiện)** | string | Bắt buộc khi `identity_type` is `BC_AUTH_TT`. ID of the Business Center that a TikTok Account User in Business Center identity is associated with.  |
| cursor | number | Timestamp cursor.  Live videos before the timestamp will be returned in reverse-chronological order.  In the initial request, you can set it to `0`. The response will include a `has_more` flag and a `cursor`. If `has_more` is `true`, use the returned `cursor` in your subsequent request to obtain the following page of data. |

### Ví dụ lệnh cURL (Example)

```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/identity/live/get/?advertiser_id={{advertiser_id}}&identity_type=TT_USER&identity_id={{identity_id}' \
--header 'Access-Token: {{Access-Token}}'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Response code. For the complete list of response codes and descriptions, see [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
| message | string | Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | The log ID of a request, which uniquely identifies the request. |
| data | object | Returned data. |
#| cursor | string | Timestamp cursor. The time value of the last item returned according to the current request. You need to use this cursor value in your subsequent request to get the next live videos. |
#| has_more | bool | Liệu more data is available.  |
#| live_list | object[] | List of live videos.  |
##| live_id | string | Live video ID. |
##| finish_timestamp | string | Finish timestamp for a live video.  Example: `2023-12-07 08:13:44`. |

### Ví dụ lệnh cURL (Example)

```http
// curl
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "live_list": [
            {
                "live_id": "{{live_id}}",
                "finish_timestamp": "2023-12-07 12:41:27"
            }
        ],
        "cursor": "1686195429",
        "has_more": true
    }
}
```

---

<a id="doc-1740218495869954"></a>
<!-- doc_id: 1740218495869954 -->
<!-- doc_id: 1740218495869954 -->
# Kiểm tra thông tin ủy quyền âm nhạc của video (Get music authorization info)
> Đường dẫn: API Reference > Identity > Get music authorization info of a video
Sử dụng endpoint này để lấy thông tin music authorization information for videos under an identity.

## Yêu cầu gọi API (Request)

**Endpoint**

https://business-api.tiktok.com/open_api/v1.3/identity/music/authorization/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|Access-Token***(Bắt buộc)***|string|Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162).|

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id ***(Bắt buộc)*** | string | Ad account ID. |
| item_id ***(Bắt buộc)*** | string | Tiktok post ID. |
| identity_id***(Bắt buộc)*** | string | Identity ID. |
| identity_type ***(Bắt buộc)***| string | Identity type. Các giá trị enum hỗ trợ: `AUTH_CODE` (Authorized Post User), `TT_USER` (TikTok Business Account User), `BC_AUTH_TT`  (TheTikTok account that a Business Center is authorized to access). See [Identities](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1738958351620097)  for details. |
| identity_authorized_bc_id **(Điều kiện)**| string | ID of the Business Center that a TikTok Account User in Business Center identity is associated with. Bắt buộc khi `identity_type` is `BC_AUTH_TT`. |
| locations ***(Bắt buộc)*** | string[] | List of targeting locations. You must use the same set of locations as when you create the ad. |
| start_time ***(Bắt buộc)*** | string | Ad deployment start time (UTC), in the format of "YYYY-MM-DD HH:MM:SS". |
| end_time ***(Bắt buộc)*** | string | Ad deployment end time (UTC), in the format of "YYYY-MM-DD HH:MM:SS". |

### Ví dụ lệnh cURL (Example)

```http
// curl
curl --get -H "Access-Token:xxx" \
--data-urlencode "advertiser_id=ADVERTISER_ID" \
--data-urlencode "item_id=ITEM_ID" \
--data-urlencode "identity_id=IDENTITY_ID" \
--data-urlencode "identity_type=IDENTITY_TYPE" \
--data-urlencode "identity_authorized_bc_id=IDENTITY_AUTHORIZED_BC_ID" \
--data-urlencode "locations=[\"LOCATIONS\"]" \
--data-urlencode "start_time=START_TIME" \
--data-urlencode "end_time=END_TIME" \
https://business-api.tiktok.com/open_api/v1.3/identity/music/authorization/
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|code |number | Response code. For the complete list of response codes and descriptions, see [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|message |string | Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|data |object| Returned data. |
#| music_authorization | object[] | Music authorization information for TikTok posts.|
##| item_id | string | TikTok post ID.|
##| music_status | string | The aggregated authorization status for all the music in the TikTok post. Các giá trị enum hỗ trợ: `WITHOUT_SONG_ID`,  `AUTHORIZATION_MISSING`, `WITH_FULL_AUTHORIZATION`. |
##| authorization_infos | object[] |Authorization information for each music. |
###| music_id | string |Song ID. |
###| author | string |Performer.|
###| title | string |Song title. |
###| labels | string[] |Labels (tags) for this song. |
###| lyricist | string |Lyricist.|
###| composer | string | Music composer.|
###| publisher | string | Music publisher.|
###| authorization_type | string |Authorization type. Các giá trị enum hỗ trợ: `NOT_AUTHORIZED`, `AUTHORIZED`. |
|request_id|string|The log id of the request, which uniquely identifies a request. |

### Ví dụ lệnh cURL (Example)

```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "202208101819310102510031480D2B9AA4",
    "data": {
        "music_authorization": [
            {
                "music_status": MUSIC_STATUS,
                "item_id": "ITEM_ID",
                "authorization_infos": [
                    {
                        "title": "TITLE",
                        "composer":" COMPOSER",
                        "author": "AUTHOR,
                        "publisher": PUBLISHER,
                        "lyricist": "LYRICIST",
                        "labels": ["LABELS"],
                        "authorization_type": "AUTHORIZED",
                        "music_id": "MUSIC_ID"
                    }
                ]
            }
        ]
    }
}
```

---

<a id="doc-1740218522178562"></a>
<!-- doc_id: 1740218522178562 -->
<!-- doc_id: 1740218522178562 -->
# Lấy thông tin chi tiết bài đăng TikTok (Get info about TikTok posts)
> Đường dẫn: API Reference > Identity > Get info about TikTok posts
Sử dụng endpoint này để lấy thông tin the information about one or more TikTok posts that you published using the `AUTH_CODE`, `TT_USER` or `BC_AUTH_TT` identity.

## Yêu cầu gọi API (Request)

**Endpoint**

https://business-api.tiktok.com/open_api/v1.3/identity/video/info/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|Access-Token***(Bắt buộc)***|string|Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162).|

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id ***(Bắt buộc)*** | string | ID tài khoản quảng cáo TikTok. |
| identity_type ***(Bắt buộc)*** | string | Loại danh tính. <br><br>Các giá trị enum hỗ trợ: `AUTH_CODE`, `TT_USER`, `BC_AUTH_TT`. <br><br>See [Identities](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1738958351620097) for details. |
| identity_id ***(Bắt buộc)*** | string | Identity ID. <br><br>To get the identities within an ad account, use [/identity/get/](46-identity.md#doc-1740218420781057).|
| identity_authorized_bc_id **(Điều kiện)** | string | Bắt buộc khi `identity_type` is `BC_AUTH_TT`. <br><br> ID of the Business Center that a TikTok Account User in Business Center identity is associated with. |
| item_id**(Điều kiện)** | string | Either `item_id` or `item_ids` must be specified. <br><br><ul><li>If you want to retrieve the information for a single TikTok post, pass `item_id`. </li><li>If you want to retrieve the information for multiple TikTok posts, pass `item_ids`.</li></ul> <br> The TikTok post ID that is associated with the provided Identity ID (`identity_id`). <br><br> To get the TikTok posts associated with an identity, use [/identity/video/get/](46-identity.md#doc-1740218475032577) and extract the TikTok post ID (`item_id`) from the response. |
| item_ids **(Điều kiện)** | string[] | Either `item_id` or `item_ids` must be specified.<br><br><ul><li>If you want to retrieve the information for a single TikTok post, pass `item_id`. </li><li>If you want to retrieve the information for multiple TikTok posts, pass `item_ids`.</li></ul> <br> A list of TikTok post IDs that are associated with the provided Identity ID (`identity_id`). <br><br>Kích thước tối đa: 20. <br><br>To get the TikTok posts associated with an identity, use [/identity/video/get/](46-identity.md#doc-1740218475032577) and extract the TikTok post ID (`item_id`) from the response. |

### Ví dụ lệnh cURL (Example)
#### Get info about one TikTok post associated with a `TT_USER` identity
```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/identity/video/info/?advertiser_id={{advertiser_id}}&identity_type=TT_USER&identity_id={{identity_id}}&item_id={{item_id}}' \
--header 'Access-Token: {{Access-Token}}'
```

#### Get info about one TikTok post associated with a `AUTH_CODE` identity
```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/identity/video/info/?advertiser_id={{advertiser_id}}&identity_type=AUTH_CODE&identity_id={{identity_id}}&item_ids=["{{item_id}}"]' \
--header 'Access-Token: {{Access-Token}}'
```

#### Get info about multiple TikTok posts associated with a `BC_AUTH_TT` identity
```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/identity/video/info/?advertiser_id={{advertiser_id}}&identity_type=BC_AUTH_TT&identity_id={{identity_id}}&identity_authorized_bc_id={{identity_authorized_bc_id}}&item_ids=["{{item_id}}","{{item_id}}"]' \
--header 'Access-Token: {{Access-Token}}'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|code |number | Response code. For the complete list of response codes and descriptions, see [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|message |string | Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|request_id|string|The log id of the request, which uniquely identifies a request. |
|data |object| Returned data. |
#| video_detail | object | Returned when `item_id` is passed in the request.<br><br>Information about the TikTok post. |
##| item_type | string | The type of TikTok post. <br><br>Các giá trị enum hỗ trợ: <ul><li> `VIDEO`: video post. </li><li>`CAROUSEL`: photo post. </li></ul>|
##| item_id | string | TikTok post ID. |
##| status | string | Visibility status of the TikTok post. <br><br>Các giá trị enum hỗ trợ: <ul><li>`ITEM_STATUS_HESITATE_RECOMMEND`: visible to all. </li><li>`STATUS_ONLY_FRIEND_SEE`: visible to friends.</li><li>`ITEM_STATUS_ONLY_AUTHOR_SEE`: private.</li></ul> |
##| text | string | Text for the TikTok post. |
##| anchor_list | object[] | Anchor information. |
###| anchor_id | string | Anchor ID. |
###| title | string | Anchor title. |
###| status | string | Anchor status. <br><br>Các giá trị enum hỗ trợ: `CHECKING`, `CHECK_FAILED`, `CHECK_SUCCESS`. |
###| url | string | Anchor URL. |
###| product_regions | string[] | Countries and regions that the ad can be delivered to. This is a list of country or region codes. For example, ` ["DE"]`. |
##| auth_info | object | Returned only when `identity_type` is set to `AUTH_CODE` in the request. <br><br>Authorization status. |
###| ad_auth_status | string | The authorization status. |
###| auth_start_time | string | Time when the authorization code is valid from (UTC+0), in the format of `"YYYY-MM-DD HH:MM:SS"`. |
###| auth_end_time | string | Time when the authorization code expires (UTC+0), in the format of `"YYYY-MM-DD HH:MM:SS"`. |
###| invite_start_time_stamp | string | The time when the authorization starts (UTC+0), in the format of `"YYYY-MM-DD HH:MM:SS"`. |
##| video_info | object | Information about the video post.<br><br><p><span style="color:darkred"><b>Note</b></span>: When `item_type` is `CAROUSEL`, the value of this field will be null.  |
###| bit_rate | integer| Bit rates, in bps. |
###| duration | float| The duration of the video, in seconds. |
###| size | integer | The size of the video, in bytes. |
###| height | integer | The height of the video. |
###| width | integer | The width of the video. |
###| poster_url | string | The URL to the video poster. <br>The expiration time is included in the URL after the `x-expires` parameter, in the format of an Epoch/Unix timestamp in seconds.  <br>When it expires, you need to call this endpoint to get a new URL. |
###| signature | string |The MD5 for the video file. |
###| url | string | Video preview link. <br><br>Validity period: an hour. When it expires, you need to call the endpoint again to get a new URL. |
##| carousel_info | object | Information about the photo post. <br> <br><p><span style="color:darkred"><b>Note</b></span>: When `item_type` is `VIDEO`, the value of this field will be null. |
###| image_info | object[] | Information about the images used in the photo post. <br> <br>The images are returned in the same order as they are shown in the photo post. |
####| image_id | string | Image ID. |
####| image_url | string | The URL of the image. <br> <br>Validity period: 90 days. |
####| image_height | integer | The height of the image, measured in pixels. |
####| image_width | integer | The width of the image, measured in pixels. |
###| music_info | object | Information about the music used in the photo post. <br> <br><p><span style="color:darkred"><b>Note</b></span>: If the photo post is directly published in the TikTok App without music, the value of this field will be null.   |
####| music_id | string | Music ID. |
####|music_url | string | The URL of the music. <br> <br>Validity period: 90 days. |
####| music_duration | integer | The duration of the music, in seconds. |
#| video_details | object[] | Returned when `item_ids` is passed in the request. <br><br>Information about the TikTok posts. |
##| item_type | string | The type of TikTok post. <br><br>Các giá trị enum hỗ trợ: <ul><li> `VIDEO`: video post. </li><li>`CAROUSEL`: photo post. </li></ul>|
##| item_id | string | TikTok post ID. |
##| status | string | Visibility status of the TikTok post. <br><br>Các giá trị enum hỗ trợ: <ul><li>`ITEM_STATUS_HESITATE_RECOMMEND`: visible to all. </li><li>`ITEM_STATUS_ONLY_AUTHOR_SEE`: visible to friends.</li><li>`STATUS_ONLY_FRIEND_SEE`: private.</li></ul> |
##| text | string | Text for the TikTok post. |
##| auth_info | object | Returned only when `identity_type` is set to `AUTH_CODE` in the request. <br><br>Authorization status. |
###| ad_auth_status | string | The authorization status. |
###| auth_start_time | string | Time when the authorization code is valid from (UTC+0), in the format of `"YYYY-MM-DD HH:MM:SS"`. |
###| auth_end_time | string | Time when the authorization code expires (UTC+0), in the format of `"YYYY-MM-DD HH:MM:SS"`. |
###| invite_start_time_stamp | string | The time when the authorization starts (UTC+0), in the format of `"YYYY-MM-DD HH:MM:SS"`. |
##| video_info | object | Information about the video post.<br><br><p><span style="color:darkred"><b>Note</b></span>: When `item_type` is `CAROUSEL`, the value of this field will be null.  |
###| bit_rate | integer | Bit rates, in bps. |
###| duration | float | The duration of the video, in seconds. |
###| size | integer | The size of the video, in bytes. |
###| height | integer | The height of the video. |
###| width | integer | Width of the video. |
###| poster_url | string | URL to the video poster. <br>The expiration time is included in the URL after the `x-expires` parameter, in the format of an Epoch/Unix timestamp in seconds.  <br>When it expires, you need to call this endpoint to get a new URL. |
###| signature | string | The MD5 for the video file. |
###| url | string | Video preview link. <br><br>Validity period: an hour. When it expires, you need to call the endpoint again to get a new URL. |
##| carousel_info | object | Information about the photo post. <br> <br><p><span style="color:darkred"><b>Note</b></span>: When `item_type` is `VIDEO`, the value of this field will be null. |
###| image_info | object[] | Information about the images used in the photo post. <br> <br>The images are returned in the same order as they are shown in the photo post. |
####| image_id | string | Image ID. |
####| image_url | string | The URL of the image. <br> <br>Validity period: 90 days. |
####| image_height | integer | The height of the image, measured in pixels. |
####| image_width | integer | The width of the image, measured in pixels. |
###| music_info | object | Information about the music used in the photo post. <br> <br><p><span style="color:darkred"><b>Note</b></span>: If the photo post is directly published in the TikTok App without music, the value of this field will be null.   |
####| music_id | string | Music ID. |
####|music_url | string | The URL of the music. <br> <br>Validity period: 90 days. |
####| music_duration |integer | The duration of the music, in seconds. |

### Ví dụ lệnh cURL (Example)
#### Get info about one TikTok post associated with a `TT_USER` identity
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "video_detail": {
            "auth_info": null,
            "anchor_list": null,
            "item_id": "{{item_id}}",
            "text": "",
            "status": "ITEM_STATUS_HESITATE_RECOMMEND",
            "video_info": {
                "duration": 1.6,
                "width": 720,
                "url": "{{url}}",
                "size": 244797,
                "bit_rate": 1223985,
                "height": 1280,
                "poster_url": "{{poster_url}}",
                "format": "mp4",
                "signature": "{{signature}}"
            }
        }
    }
}
```

#### Get info about one TikTok post associated with an `AUTH_CODE` identity
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "video_details": [
            {
                "item_type": "VIDEO",
                "anchor_list": null,
                "item_id": "{{item_id}}",
                "carousel_info": null,
                "status": "ITEM_STATUS_HESITATE_RECOMMEND",
                "text": "{{text}}",
                "auth_info": {
                    "auth_end_time": "2025-05-20T11:40:50Z",
                    "ad_auth_status": "AUTHORIZED",
                    "auth_start_time": "2024-05-20T11:40:50Z",
                    "invite_start_time": "2024-05-20T11:43:00Z"
                },
                "video_info": {
                    "height": 1920,
                    "width": 1080,
                    "url": "{{url}}",
                    "signature": "{{signature}}",
                    "size": 8119495,
                    "bit_rate": 9897296,
                    "format": "mp4",
                    "poster_url": "{{poster_url}}",
                    "duration": 6.563
                }
            }
        ]
    }
}
```

#### Get info about multiple TikTok posts associated with a `BC_AUTH_TT` identity
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "video_details": [
            {
                "text": "{{text}}",
                "anchor_list": null,
                "status": "ITEM_STATUS_HESITATE_RECOMMEND",
                "auth_info": null,
                "video_info": {
                    "url": "{{url}}",
                    "height": 1024,
                    "format": "mp4",
                    "signature": "{{signature}}",
                    "width": 576,
                    "poster_url": "{{poster_url}}",
                    "duration": 8.474,
                    "size": 774110,
                    "bit_rate": 730809
                },
                "item_id": "{{item_id}}"
            },
            {
                "text": "",
                "anchor_list": null,
                "status": "ITEM_STATUS_HESITATE_RECOMMEND",
                "auth_info": null,
                "video_info": {
                    "url": "{{url}}",
                    "height": 1024,
                    "format": "mp4",
                    "signature": "{{signature}}",
                    "width": 576,
                    "poster_url": "{{poster_url}}",
                    "duration": 6.245,
                    "size": 913323,
                    "bit_rate": 1169989
                },
                "item_id": "{{item_id}}"
            }
        ]
    }
}
```
---

## Hướng dẫn thực hành Data Retrieval bằng cURL

Dưới đây là các ví dụ lệnh **cURL** chuẩn để truy vấn và quản lý Danh tính (Identity):

### 1. Lấy danh sách danh tính được ủy quyền (Get Identities)
```bash
curl -s -X GET "https://business-api.tiktok.com/open_api/v1.3/identity/get/?advertiser_id=YOUR_ADVERTISER_ID&identity_type=AUTH_CODE&page_size=20" \
  -H "Access-Token: YOUR_ACCESS_TOKEN"
```

### 2. Tạo danh tính tùy chỉnh mới (Create Custom Identity)
```bash
curl -s -X POST "https://business-api.tiktok.com/open_api/v1.3/identity/create/" \
  -H "Access-Token: YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "advertiser_id": "YOUR_ADVERTISER_ID",
    "display_name": "My Brand Official",
    "image_uri": "YOUR_AVATAR_IMAGE_ID"
  }'
```

### 3. Lấy danh sách bài đăng theo danh tính (Get Posts Under Identity)
```bash
curl -s -X GET "https://business-api.tiktok.com/open_api/v1.3/identity/video/get/?advertiser_id=YOUR_ADVERTISER_ID&identity_type=CUSTOMIZED_USER&identity_id=YOUR_IDENTITY_ID&count=10" \
  -H "Access-Token: YOUR_ACCESS_TOKEN"
```

