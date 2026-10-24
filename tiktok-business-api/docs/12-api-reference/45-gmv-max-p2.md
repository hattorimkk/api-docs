# GMV Max — phần 2/3

> Phân hệ: apiref:GMV Max.
> Tài liệu biên dịch kỹ thuật chi tiết theo chuẩn TikTok Business API v1.3.

---

## Mục lục điều hướng
- [1. Get TikTok Shops for GMV Max Campaigns (#doc-1822001044479041)](#doc-1822001044479041)
- [2. Check the availability of a TikTok Shop for Product GMV Max Campaigns (#doc-1822001084174338)](#doc-1822001084174338)
- [3. Get identities for GMV Max Campaigns (#doc-1822001101474882)](#doc-1822001101474882)
- [4. Check the occupancy of identities or products in Shopping Ads (#doc-1822001136924674)](#doc-1822001136924674)
- [5. Get posts for a Product GMV Max Campaign (#doc-1822001168512129)](#doc-1822001168512129)
- [6. (To be deprecated) Get details of videos in customized posts (#doc-1830215925061633)](#doc-1830215925061633)
- [7. Remove or add back creatives in a GMV Max Campaign (#doc-1861260625563202)](#doc-1861260625563202)
- [8. Create shop-level customized TikTok posts (#doc-1866513154013585)](#doc-1866513154013585)
- [9. Get customized TikTok posts (#doc-1866513156712449)](#doc-1866513156712449)
- [10. Delete customized TikTok posts (#doc-1866513159202306)](#doc-1866513159202306)
- [11. Get product linkage details of videos in customized posts (#doc-1866513161692161)](#doc-1866513161692161)
- [12. Get the TikTok Shop exclusive authorization status of an ad account (#doc-1822001184635905)](#doc-1822001184635905)
- [13. Grant an ad account exclusive authorization for a TikTok Shop (#doc-1822001200356354)](#doc-1822001200356354)
- [14. Run a GMV Max Campaign report (#doc-1824721673497601)](#doc-1824721673497601)

---

<a id="doc-1822001044479041"></a>
<!-- doc_id: 1822001044479041 -->
<!-- doc_id: 1822001044479041 -->
# Get TikTok Shops for GMV Max Campaigns
> Đường dẫn: API Reference > GMV Max > Get TikTok Shops for GMV Max Campaigns
Dùng endpoint này để lấy danh sách TikTok Shop mà tài khoản quảng cáo có quyền truy cập và cho biết liệu các TikTok Shop đó có thể dùng để tạo chiến dịch GMV Max hay không.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/gmv_max/store/list/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). ⏎ Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
| advertiser_id ***(Bắt buộc)*** | string | ID tài khoản quảng cáo TikTok. |

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location  --request GET 'https://business-api.tiktok.com/open_api/v1.3/gmv_max/store/list/?advertiser_id={{advertiser_id}}' \
--header 'Access-Token: {{Access-Token}}'
```
## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|code |number|Response code. For the complete list of response codes and descriptions, see [Appendix-Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message|string|Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|request_id |string|The log ID of a request, which uniquely identifies the request.  |
|data |object|Returned data.|
#| store_list | object[] | The list of TikTok Shops that the ad account has access to. |
##| store_id | string | ID of the TikTok Shop. |
##| is_gmv_max_available | boolean | Liệu TikTok Shop is available for GMV Max Campaigns. <br><br> Các giá trị được hỗ trợ: <ul><li>`true`: available.</li><li>`false`: unavailable. </li></ul>|
##| store_authorized_bc_id | string | ID of the Business Center that is authorized to access the TikTok Shop (`store_id`). |
##| is_owner_bc | boolean | Liệu Business Center (`store_authorized_bc_id`) owns the TikTok Shop (`store_id`). <br><br>Các giá trị được hỗ trợ: <ul><li>`true`: The Business Center owns the TikTok Shop.</li><li> `false`: The Business Center is a Partner Business Center that has access to the TikTok Shop and does not own the TikTok Shop.</li></ul>|
##| store_authorized_bc_info | object | Information about the Business Center that is authorized to access the TikTok Shop. |
###| bc_id | string | The ID of the Business Center. |
###| bc_profile_image | string | The profile image URL of the Business Center. |
###| bc_name | string | The name of the Business Center. |
###| user_role| string | The role of the user (member) within the Business Center.<br><br> Các giá trị enum hỗ trợ: <ul><li>`ADMIN`: Admin. Admins have full access to all features in Business Center. </li><li>`STANDARD`: Standard. Standard members can only work on accounts they've been assigned to.</li></ul>|
##| thumbnail_url | string | The thumbnail URL of the TikTok Shop. |
##| store_name | string | The name of the TikTok Shop. |
##| store_code| string | The shop code of the TikTok Shop. |
##| targeting_region_codes | string[] | The codes of the regions that the TikTok Shop can target. <br><br>  To find out the region that a region code corresponds to, see [Appendix-Location code](../15-appendix/phu-luc-p1.md#doc-1737585867307010). <br><br> For example, `VN` corresponds to Vietnam. |
##| store_status | string | The status of the TikTok Shop. <br><br> Các giá trị enum hỗ trợ: <ul><li>`ACTIVE`: active. </li><li>`INACTIVE`: inactive.</li><li>`NEW_CREATE`: newly created.</li></ul>|
##| store_role | string | Business Center user's permission to the TikTok Shop.<br><br>Các giá trị enum hỗ trợ: <ul><li>`AD_PROMOTION`: Ad promotion. Create ads promoting products from this TikTok Shop.</li><li>`MANAGER`: Manager. Manage stores and related catalogs and view data insights in Store Manager.</li><li>`UNSET`: Unset.</li></ul>|
##| exclusive_authorized_advertiser_info | object | Information about the GMV Max exclusive authorization of the TikTok Shop. |
###| advertiser_id | string | The ID of the only ad account that is authorized to create GMV Max Campaigns for the TikTok Shop. |
###| advertiser_name | string | The name of the only ad account that is authorized to create GMV Max Campaigns for the TikTok Shop. |
###| advertiser_status | string | The status of the only ad account that is authorized to create GMV Max Campaign for the TikTok Shop. <br><br> Các giá trị enum hỗ trợ: <ul><li>`STATUS_ENABLE`: Approved.</li><li>`STATUS_CONFIRM_FAIL`: Not approved.</li><li>`STATUS_PENDING_CONFIRM`: In review.</li><li>`STATUS_LIMIT`: Suspended.</li><li>`STATUS_CONTRACT_PENDING`: Contract has not taken effect.</li><li>`STATUS_DISABLE`: Disabled.</li><li>`STATUS_PENDING_CONFIRM_MODIFY`: Modifications pending review.</li><li>`STATUS_PENDING_VERIFIED`: Pending verification.</li><li>`STATUS_SELF_SERVICE_UNAUDITED`: Pending verification of qualifications for the self-service account.</li><li> `STATUS_WAIT_FOR_BPM_AUDIT`: Pending CRM system review.</li><li>`STATUS_CONFIRM_FAIL_END`: CRM system review failed.</li><li>`STATUS_CONFIRM_MODIFY_FAIL`: Review of modifications failed. </li></ul>|

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "store_list": [
            {
                "exclusive_authorized_advertiser_info": {
                    "advertiser_id": "{{advertiser_id}}",
                    "advertiser_name": "{{advertiser_name}}",
                    "advertiser_status": "STATUS_ENABLE"
                },
                "is_gmv_max_available": false,
                "is_owner_bc": true,
                "store_authorized_bc_id": "{{store_authorized_bc_id}}",
                "store_authorized_bc_info": {
                    "bc_id": "{{bc_id}}",
                    "bc_name": "{{bc_name}}",
                    "bc_profile_image": "{{bc_profile_image}}",
                    "user_role": "ADMIN"
                },
                "store_code": "{{store_code}}",
                "store_id": "{{store_id}}",
                "store_name": "{{store_name}}",
                "store_role": "AD_PROMOTION",
                "store_status": "ACTIVE",
                "targeting_region_codes": [
                    "ID"
                ],
                "thumbnail_url": "{{thumbnail_url}}"
            },
            {
                "exclusive_authorized_advertiser_info": {
                    "advertiser_id": "{{advertiser_id}}",
                    "advertiser_name": "{{advertiser_name}}",
                    "advertiser_status": "STATUS_ENABLE"
                },
                "is_gmv_max_available": true,
                "is_owner_bc": true,
                "store_authorized_bc_id": "{{store_authorized_bc_id}}",
                "store_authorized_bc_info": {
                    "bc_id": "{{bc_id}}",
                    "bc_name": "{{bc_name}}",
                    "bc_profile_image": "{{bc_profile_image}}",
                    "user_role": "ADMIN"
                },
                "store_code": "{{store_code}}",
                "store_id": "{{store_id}}",
                "store_name": "{{store_name}}",
                "store_role": "AD_PROMOTION",
                "store_status": "ACTIVE",
                "targeting_region_codes": [
                    "ID"
                ],
                "thumbnail_url": "{{thumbnail_url}}"
            },
            {
                "exclusive_authorized_advertiser_info": {
                    "advertiser_id": "{{advertiser_id}}",
                    "advertiser_name": "{{advertiser_name}}",
                    "advertiser_status": "STATUS_ENABLE"
                },
                "is_gmv_max_available": true,
                "is_owner_bc": false,
                "store_authorized_bc_id": "{{store_authorized_bc_id}}",
                "store_authorized_bc_info": {
                    "bc_id": "{{bc_id}}",
                    "bc_name": "{{bc_name}}",
                    "bc_profile_image": "{{bc_profile_image}}",
                    "user_role": "ADMIN"
                },
                "store_code": "{{store_code}}",
                "store_id": "{{store_id}}",
                "store_name": "{{store_name}}",
                "store_role": "AD_PROMOTION",
                "store_status": "ACTIVE",
                "targeting_region_codes": [
                    "MY"
                ],
                "thumbnail_url": "{{thumbnail_url}}"
            },
            {
                "exclusive_authorized_advertiser_info": {
                    "advertiser_id": "{{advertiser_id}}",
                    "advertiser_name": "{{advertiser_name}}",
                    "advertiser_status": "STATUS_ENABLE"
                },
                "is_gmv_max_available": false,
                "is_owner_bc": false,
                "store_authorized_bc_id": "{{store_authorized_bc_id}}",
                "store_authorized_bc_info": {
                    "bc_id": "{{bc_id}}",
                    "bc_name": "{{bc_name}}",
                    "bc_profile_image": "{{bc_profile_image}}",
                    "user_role": "ADMIN"
                },
                "store_code": "{{store_code}}",
                "store_id": "{{store_id}}",
                "store_name": "{{store_name}}",
                "store_role": "AD_PROMOTION",
                "store_status": "ACTIVE",
                "targeting_region_codes": [
                    "ID"
                ],
                "thumbnail_url": "{{thumbnail_url}}"
            }
        ]
    }
}
```

---

<a id="doc-1822001084174338"></a>
<!-- doc_id: 1822001084174338 -->
<!-- doc_id: 1822001084174338 -->
# Check the availability of a TikTok Shop for Product GMV Max Campaigns
> Đường dẫn: API Reference > GMV Max > Check the availability of a TikTok Shop for Product GMV Max Campaigns
Sử dụng endpoint này để kiểm tra Liệu a TikTok Shop has been occupied by enabled[ Video Shopping Ads](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1750361719059457) or [Product Shopping Ads](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1785886237030401), and Liệu TikTok Shop can be used to create Product GMV Max Campaigns by promoting all products in the TikTok Shop.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/gmv_max/store/shop_ad_usage_check/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). ⏎ Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
| advertiser_id ***(Bắt buộc)*** | string | ID tài khoản quảng cáo TikTok. |
| store_id ***(Bắt buộc)*** | string | The ID of the TikTok Shop.<br><br> To obtain a TikTok Shop that is available for GMV Max Campaigns, use [/gmv_max/store/list/](45-gmv-max-p2.md#doc-1822001044479041) and confirm that the returned `is_gmv_max_available` is `true`. |

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location  --request GET 'https://business-api.tiktok.com/open_api/v1.3/gmv_max/store/shop_ad_usage_check/?advertiser_id={{advertiser_id}}&store_id={{store_id}}' \
--header 'Access-Token: {{Access-Token}}'
```
## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|code |number|Response code. For the complete list of response codes and descriptions, see [Appendix-Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message|string|Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|request_id |string|The log ID of a request, which uniquely identifies the request.  |
|data |object|Returned data.|
#| promote_all_products_allowed | boolean | Liệu TikTok Shop can be used to create Product GMV Max Campaigns by promoting all products in the TikTok Shop. <br> <br>Các giá trị được hỗ trợ: `true`, `false`. |
#| is_running_custom_shop_ads | boolean| Liệu TikTok Shop is being used in enabled Video Shopping Ads or Product Shopping Ads. <br> <br>Các giá trị được hỗ trợ: `true`, `false`. |

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "is_running_custom_shop_ads": true,
        "promote_all_products_allowed": false
    }
}
```

---

<a id="doc-1822001101474882"></a>
<!-- doc_id: 1822001101474882 -->
<!-- doc_id: 1822001101474882 -->
# Get identities for GMV Max Campaigns
> Đường dẫn: API Reference > GMV Max > Get identities for GMV Max Campaigns
Dùng endpoint này để lấy danh sách danh tính gắn với một TikTok Shop và cho biết liệu các danh tính đó có khả dụng cho chiến dịch GMV Max hay không.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/gmv_max/identity/get/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). ⏎ Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
| advertiser_id ***(Bắt buộc)*** | string | ID tài khoản quảng cáo TikTok. |
| store_id ***(Bắt buộc)*** | string | The ID of the TikTok Shop.<br><br> To obtain a TikTok Shop that is available for GMV Max Campaigns, use [/gmv_max/store/list/](45-gmv-max-p2.md#doc-1822001044479041) and confirm that the returned `is_gmv_max_available` is `true`. |
| store_authorized_bc_id ***(Bắt buộc)*** | string | ID of the Business Center that is authorized to access the TikTok Shop (`store_id`). |

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location  --request GET 'https://business-api.tiktok.com/open_api/v1.3/gmv_max/identity/get/?advertiser_id={{advertiser_id}}&store_id={{store_id}}&store_authorized_bc_id={{store_authorized_bc_id}}' \
--header 'Access-Token: {{Access-Token}}'
```
## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|code |number|Response code. For the complete list of response codes and descriptions, see [Appendix-Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message|string|Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|request_id |string|The log ID of a request, which uniquely identifies the request.  |
|data |object|Returned data.|
#| identity_list | object[] | The list of identities associated with the TikTok Shop. |
##| identity_id | string | Identity ID. |
##| identity_type | string | Identity type. <br><br>Các giá trị enum hỗ trợ: <ul><li>`AUTH_CODE`: Authorized User. This type of identity is created when you use the authorization code to access a TikTok account or a TikTok post.</li><li>`TT_USER`: TikTok User. This type of identity is created when you bind your TikTok For Business account with your TikTok Business Account, or when you bind your TikTok For Business account with your regular TikTok account and then upgrade the account to Business Account.</li><li>`BC_AUTH_TT`: TikTok Account User in Business Center. This type of identity is created when you add a TikTok account to your Business Center, and the TikTok account owner approves your request. </li><li>`TTS_TT`: TikTok Account User for TikTok Shop. This type of identity is created when you set an official TikTok account for the TikTok Shop.</li></ul> |
##|identity_authorized_bc_id | string | Returned only when `identity_type` is `BC_AUTH_TT`. <br><br>The ID of the Business Center that a TikTok Account User in Business Center identity is associated with. |
##| identity_authorized_shop_id | string | Returned for some `BC_AUTH_TT` identities. <br><br>The ID of the TikTok Shop that the TikTok Account User in Business Center identity is associated with. |
##| store_id | string | Returned only when `identity_type` is `TTS_TT`. <br><br>The ID of the TikTok Shop that a TikTok Account User for TikTok Shop identity is associated with. |
##| profile_image | string | Temporary profile image URL for the TikTok account that is associated with the identity. <br><br>Validity period: around 48 hours. The expiration time is included in the URL after the `x-expires` parameter, in the format of an Epoch/Unix timestamp in seconds. <br><br>Once the URL expires, you need to call [/gmv_max/identity/get/](45-gmv-max-p2.md#doc-1822001101474882) to obtain a new URL. |
##| display_name | string | The display name of the TikTok account that is associated with the identity. |
##| user_name | string | The username of the TikTok account that is associated with the identity. |
##| is_running_custom_shop_ads | bool | Liệu identity is being used in enabled Video Shopping Ads, Product Shopping Ads or Live Shopping Ads. <br><br>Các giá trị được hỗ trợ: `true`, `false`. |
##| product_gmv_max_available | boolean | Liệu identity is available for use in Product GMV Max Campaigns. <br><br>Các giá trị được hỗ trợ: `true`, `false`. |
##| live_gmv_max_available | boolean | Liệu identity is available for use in LIVE GMV Max Campaigns. <br><br>Các giá trị được hỗ trợ: `true`, `false`. |
##| unavailable_reason | string | Returned only when `live_gmv_max_available` is `false`.<br><br>The reason why the identity is not available for LIVE GMV Max Campaigns. <br><br>Các giá trị enum hỗ trợ: <ul><li>`OCCUPIED`: The identity has been occupied by an enabled LIVE GMV Max Campaign.</li><li>`UNAUTHORIZED`: The identity is not authorized for use in LIVE GMV Max Campaigns.</li></ul>|

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
HTTPS/1.1 200 OK
{
  "code": 0,
  "message": "OK",
  "request_id": "{{request_id}}",
  "data": {
    "identity_list": [
      {
        "display_name": "{{display_name}}",
        "identity_authorized_bc_id": "{{identity_authorized_bc_id}}",
        "identity_id": "{{identity_id}}",
        "identity_type": "BC_AUTH_TT",
        "is_running_custom_shop_ads": false,
        "live_gmv_max_available": false,
        "product_gmv_max_available": true,
        "profile_image": "{{profile_image}}",
        "unavailable_reason": "OCCUPIED",
        "user_name": "{{user_name}}"
      },
      {
        "display_name": "{{display_name}}",
        "identity_authorized_bc_id": "{{identity_authorized_bc_id}}",
        "identity_id": "{{identity_id}}",
        "identity_type": "BC_AUTH_TT",
        "is_running_custom_shop_ads": false,
        "live_gmv_max_available": false,
        "product_gmv_max_available": true,
        "profile_image": "{{profile_image}}",
        "unavailable_reason": "UNAUTHORIZED",
        "user_name": "{{user_name}}"
      },
      {
        "display_name": "{{display_name}}",
        "identity_authorized_bc_id": "{{identity_authorized_bc_id}}",
        "identity_id": "{{identity_id}}",
        "identity_type": "BC_AUTH_TT",
        "is_running_custom_shop_ads": false,
        "live_gmv_max_available": false,
        "product_gmv_max_available": true,
        "profile_image": "{{profile_image}}",
        "unavailable_reason": "OCCUPIED",
        "user_name": "{{user_name}}"
      },
      {
        "display_name": "{{display_name}}",
        "identity_authorized_bc_id": "{{identity_authorized_bc_id}}",
        "identity_id": "{{identity_id}}",
        "identity_type": "BC_AUTH_TT",
        "is_running_custom_shop_ads": false,
        "live_gmv_max_available": true,
        "product_gmv_max_available": true,
        "profile_image": "{{profile_image}}",
        "user_name": "{{user_name}}"
      },
      {
        "display_name": "{{display_name}}",
        "identity_authorized_bc_id": "{{identity_authorized_bc_id}}",
        "identity_id": "{{identity_id}}",
        "identity_type": "BC_AUTH_TT",
        "is_running_custom_shop_ads": false,
        "live_gmv_max_available": false,
        "product_gmv_max_available": true,
        "profile_image": "{{profile_image}}",
        "unavailable_reason": "OCCUPIED",
        "user_name": "{{user_name}}"
      },
      {
        "identity_id": "{{identity_id}}",
        "identity_type": "TTS_TT",
        "is_running_custom_shop_ads": false,
        "live_gmv_max_available": false,
        "product_gmv_max_available": false,
        "store_id": "{{store_id}}",
        "unavailable_reason": "UNAUTHORIZED"
      },
      {
        "display_name": "{{display_name}}",
        "identity_id": "{{identity_id}}",
        "identity_type": "TT_USER",
        "is_running_custom_shop_ads": false,
        "live_gmv_max_available": false,
        "product_gmv_max_available": false,
        "profile_image": "{{profile_image}}",
        "unavailable_reason": "UNAUTHORIZED",
        "user_name": "{{user_name}}"
      }
    ]
  }
}
```

---

<a id="doc-1822001136924674"></a>
<!-- doc_id: 1822001136924674 -->
<!-- doc_id: 1822001136924674 -->
# Check the occupancy of identities or products in Shopping Ads
> Đường dẫn: API Reference > GMV Max > Check the occupancy of identities or products in Shopping Ads
Sử dụng endpoint này để kiểm tra Liệu an identity or a product has been occupied by enabled Shopping Ads ([Video Shopping Ads](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1750361719059457), [Product Shopping Ads](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1785886237030401) or [Live Shopping Ads](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1754162402455554)).

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/gmv_max/occupied_custom_shop_ads/list/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). ⏎ Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
| advertiser_id ***(Bắt buộc)*** | string | ID tài khoản quảng cáo TikTok. |
| store_id ***(Bắt buộc)*** | string | The ID of the TikTok Shop.<br><br> To obtain a TikTok Shop that is available for GMV Max Campaigns, use [/gmv_max/store/list/](45-gmv-max-p2.md#doc-1822001044479041) and confirm that the returned `is_gmv_max_available` is `true`. |
| occupied_asset_type ***(Bắt buộc)*** | string | The type of asset that you want to check for occupancy in enabled Video Shopping Ads, Product Shopping Ads, or Live Shopping Ads.<br><br>Các giá trị enum hỗ trợ: <ul><li>`IDENTITY_TT_USER`: TikTok User (`TT_USER`) identity.</li><li>`IDENTITY_BC_AUTH_TT`: TikTok Account User in Business Center (`BC_AUTH_TT`) identity.</li><li>`IDENTITY_TTS_TT`: TikTok Account User for TikTok Shop (`TTS_TT`) identity.</li><li>`SPU`: SPU.</li></ul>|
| asset_ids ***(Bắt buộc)*** | string[] | The asset IDs. <br><br>Kích thước tối đa: 1. <br><br><ul><li>When `occupied_asset_type` is `IDENTITY_TT_USER`, specify one `TT_USER` identity ID via this field.</li><li>When `occupied_asset_type` is `IDENTITY_BC_AUTH_TT`, specify one `BC_AUTH_TT` identity ID via this field.</li><li>When `occupied_asset_type` is `IDENTITY_TTS_TT`, specify one `TTS_TT` identity ID via this field. </li><li>When `occupied_asset_type` is `SPU`, specify the SPU ID of a product within the TikTok Shop via this field. </li></ul><br><ul><li>To obtain a list of identities, use [/gmv_max/identity/get/](45-gmv-max-p2.md#doc-1822001101474882).</li><li>To obtain the list of SPU IDs for products within a TikTok Shop, use [/store/product/get/](69-tiktok-store.md#doc-1793482248880130). Set `ad_creation_eligible` to `GMV_MAX` and check the returned `item_group_id`.</li></ul>|

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location  --request GET 'https://business-api.tiktok.com/open_api/v1.3/gmv_max/occupied_custom_shop_ads/list/?advertiser_id={{advertiser_id}}&store_id={{store_id}}&occupied_asset_type=IDENTITY_BC_AUTH_TT&asset_ids=["{{asset_id}}"]' \
--header 'Access-Token: {{Access-Token}}'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|code |number|Response code. For the complete list of response codes and descriptions, see [Appendix-Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message|string|Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|request_id |string|The log ID of a request, which uniquely identifies the request.  |
|data |object|Returned data.|
#| occupied_custom_shop_ads| object[] | The list of enabled Shopping Ads that are currently using the assets. |
##| advertiser_id | string | ID tài khoản quảng cáo TikTok. |
##| campaign_id | string | ID chiến dịch quảng cáo. |
##| adgroup_id | string | ID nhóm quảng cáo. |
##| ad_id | string | ID mẫu quảng cáo. |
##| create_time | string | The time when the ad group or ad was created, in the format of `YYYY-MM-DD HH:MM:SS` (UTC+0). <br><br><ul><li>When `campaign_id` and `adgroup_id` are returned, this field represents the time when the ad group was created.</li><li> When `adgroup_id` and `ad_id` are returned, this field represents the time when the ad was created.</li></ul>|

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "occupied_custom_shop_ads": []
    }
}
```

---

<a id="doc-1822001168512129"></a>
<!-- doc_id: 1822001168512129 -->
<!-- doc_id: 1822001168512129 -->
# Get posts for a Product GMV Max Campaign
> Đường dẫn: API Reference > GMV Max > Get posts for a Product GMV Max Campaign
Sử dụng endpoint này để truy xuất the list of TikTok posts that are available for a Product GMV Max campaign using a specific TikTok Shop.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/gmv_max/video/get/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). ⏎ Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
| advertiser_id ***(Bắt buộc)*** | string | ID tài khoản quảng cáo TikTok. |
| store_id ***(Bắt buộc)*** | string | The ID of the TikTok Shop.<br><br> To obtain a TikTok Shop that is available for GMV Max Campaigns, use [/gmv_max/store/list/](45-gmv-max-p2.md#doc-1822001044479041) and confirm that the returned `is_gmv_max_available` is `true`. |
| store_authorized_bc_id ***(Bắt buộc)*** | string | ID of the Business Center that is authorized to access the TikTok Shop (`store_id`). |
| spu_id_list  | string[] | A list of Product SPU (standard product unit) IDs to filter the results by.<br><br> <ul><li>If you want to promote all products from the TikTok Shop in the Product GMV Max Campaign using authorized posts, you don't need to pass `spu_id_list` and `custom_posts_eligible`.</li><li>If you want to promote specific products from the TikTok Shop in the Product GMV Max Campaign using authorized posts, specify these products via `spu_id_list` and do not specify `custom_posts_eligible`.</li><li>If you want to promote a specific product from the TikTok Shop in the Product GMV Max Campaign using customized posts, specify the product via `spu_id_list` and set `custom_posts_eligible` to `true`.</li></ul><br>Kích thước tối đa: <ul><li>When `custom_posts_eligible` is `false` or not specified: 50.</li><li>When `custom_posts_eligible` is `true`: 1.</li></ul><br>To obtain the list of SPU IDs for products within a TikTok Shop, use [/store/product/get/](69-tiktok-store.md#doc-1793482248880130). Set `ad_creation_eligible` to `GMV_MAX` and select `item_group_id` values where `status` is `AVAILABLE` and `gmv_max_ads_status` is `UNOCCUPIED`. |
| custom_posts_eligible | boolean | Có thực hiện query videos that can be used in customized posts promoting a specific product.<br><br>If you set this field to `true`, you need to specify one product using `spu_id_list` simultaneously.<br><br>Các giá trị được hỗ trợ: `true`,`false`.<br>Giá trị mặc định: `false`. |
| sort_field | string | Chỉ hợp lệ khi `custom_posts_eligible` is `false` or not provided.<br><br>The sorting field for videos available for authorized posts.<br><br>Các giá trị enum hỗ trợ: <ul><li>`GMV`: GMV.</li><li>`POST_TIME`: Post time.</li><li>`VIDEO_VIEWS`: Video views.</li><li>`VIDEO_LIKES`: Video likes.</li><li>`CLICK_THROUGH_RATE`: Click-through Rate (CTR).</li><li>`PRODUCT_CLICKS`: Product clicks.</li></ul>Giá trị mặc định: `GMV`. |
| sort_type | string | The Thứ tự sắp xếp kết quả for videos available for authorized posts or customized posts.<br><br>Các giá trị enum hỗ trợ: <ul><li>`ASC`: ascending.</li><li>`DESC`: descending.</li></ul>Giá trị mặc định: `DESC`.<br><br><ul><li>If `custom_posts_eligible` is `false` or not specified, you can sort the videos available for authorized posts by specifying both `sort_field` and `sort_type`.</li><li>If `custom_posts_eligible` is `true`, you don't need to specify `sort_field`. In this case, videos available for customized posts are sorted by default in Sắp xếp giảm dần (DESC) of post time, with the latest posts appearing first. If you prefer to sort posts in Sắp xếp tăng dần (ASC) (earliest posts first), set `sort_type` to `ASC`. </li></ul><br>|
| keyword | string | A search keyword to filter posts (videos).<br><br>You can specify a post ID or caption.<ul><li>To search by post caption (`text`), provide a text string. This search type supports multiple-language searches and fuzzy matches.<br>Example: `summer`.</li><li> To search by post ID (`item_id`), provide a numeric string with at least 19 characters. This search type supports exact matches.<br>Example: `1234567891234567891`.</li></ul> |
| need_auth_code_video| boolean| Có thực hiện include posts associated with `AUTH_CODE` identities in the results.<br><br> Các giá trị được hỗ trợ: `true`, `false`.<br>Giá trị mặc định: `false`.<br><br><p><span style="color:darkred"><b>Note</b></span>: If `need_auth_code_video` is `false` or not passed and `identity_list` is not specified, you will retrieve an empty post list. |
| identity_list  | object[] | A list of `TT_USER`, `BC_AUTH_TT`, or `TTS_TT` identities to filter the results by.<br><br>To obtain a list of identities available for Product GMV Max Campaigns, use [/gmv_max/identity/get/](45-gmv-max-p2.md#doc-1822001101474882) and select identities with `product_gmv_max_available` as `true`.<br><br>Kích thước tối đa: 20.<br><br><p><span style="color:darkred"><b>Note</b></span>: If `need_auth_code_video` is `false` or not passed and `identity_list` is not specified, you will retrieve an empty post list. |
#| identity_id  | string | Identity ID. |
#| identity_type  | string |  Identity type. <br><br>Các giá trị enum hỗ trợ: <ul><li>`TT_USER`: TikTok User. This type of identity is created when you bind your TikTok For Business account with your TikTok Business Account, or when you bind your TikTok For Business account with your regular TikTok account and then upgrade the account to Business Account.</li><li>`BC_AUTH_TT`: TikTok Account User in Business Center. This type of identity is created when you add a TikTok account to your Business Center, and the TikTok account owner approves your request. </li><li>`TTS_TT`: TikTok Account User for TikTok Shop. This type of identity is created when you set an official TikTok account for the TikTok Shop.</li></ul> |
#| identity_authorized_bc_id {+Conditional} | string | Bắt buộc khi `identity_type` is `BC_AUTH_TT`. <br><br> The ID of the Business Center that a TikTok Account User in Business Center identity is associated with. |
#| identity_authorized_shop_id {+Conditional} | string | Required only when `dentity_type` is `BC_AUTH_TT` and `identity_authorized_shop_id` is returned for the identity from [/gmv_max/identity/get/](45-gmv-max-p2.md#doc-1822001101474882). <br><br> The ID of the TikTok Shop that a TikTok Account User in Business Center identity is associated with. |
#| store_id {+Conditional} | string | Bắt buộc khi `identity_type` is `TTS_TT`. <br><br>The ID of the TikTok Shop that a TikTok Account User for TikTok Shop identity is associated with. |
| page | number | Current Số trang cần lấy dữ liệu.<br><br> Value range: ≥ 1. <br>Giá trị mặc định: 1. |
| page_size | number | Page size.<br><br> Value range: 1-50.<br>Giá trị mặc định: 10. |

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/gmv_max/video/get/?advertiser_id={{advertiser_id}}&store_id={{store_id}}&store_authorized_bc_id={{store_authorized_bc_id}}&need_auth_code_video=true&identity_list=[{ "identity_type": "BC_AUTH_TT","identity_id": "{{identity_id}}","identity_authorized_bc_id": "{{identity_authorized_bc_id}}"}]&page=1&page_size=50' \
--header 'Access-Token: {{Access-Token}}'
```
## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|code |number|Response code. For the complete list of response codes and descriptions, see [Appendix-Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message|string|Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|request_id |string|The log ID of a request, which uniquely identifies the request.  |
|data |object|Returned data.<br><br><p><span style="color:darkred"><b>Note</b></span>: If this field is an empty list, follow these steps to authorize posts with product links to the ad account:<br>1. Authorize posts to the ad account using [/tt_video/authorize/](64-spark-ads-using-authorized-posts.md#doc-1738376435339265).<br>2. Check Liệu posts contain product information (`spu_id`, `spu_name`, and `store_id`) using [/tt_video/info/](64-spark-ads-using-authorized-posts.md#doc-1738376324021250) or [/tt_video/list/](64-spark-ads-using-authorized-posts.md#doc-1738376465972226).|
#| item_list| object[] | A list of TikTok videos (posts) available for Product GMV Max campaigns using the specified TikTok Shop. |
##| item_id | string | The ID of the TikTok post. |
##| text | string | The caption of the TikTok post. |
##| spu_id_list| string[] | The list of Product SPU IDs that the TikTok post is associated with.<br><br><p><span style="color:darkred"><b>Note</b></span>: This field is not included in the response for videos with no product anchor link. |
##| can_change_anchor | boolean | Liệu you can change the product anchor link in this video.<br><br>Các giá trị được hỗ trợ: <ul><li>`true`: You can add a product anchor link to create a customized post.</li><li>`false`: You cannot use the video to create a customized post.</li></ul><br><p><span style="color:darkred"><b>Note</b></span>: If `can_change_anchor` is `false`, you cannot pass the video to `custom_anchor_video_list` or `item_list` in [/campaign/gmv_max/create/](45-gmv-max-p1.md#doc-1822000988713089) or [/campaign/gmv_max/update/](45-gmv-max-p1.md#doc-1822001009002497) to create customized posts. |
##| identity_info | object | Information about the identity associated with the TikTok post. |
###| identity_id | string | Identity ID. |
###| identity_type | string | Identity type. <br><br>Các giá trị enum hỗ trợ: <ul><li>`AUTH_CODE`: Authorized User. This type of identity is created when you use the authorization code to access a TikTok account or a TikTok post.</li><li>`TT_USER`: TikTok User. This type of identity is created when you bind your TikTok For Business account with your TikTok Business Account, or when you bind your TikTok For Business account with your regular TikTok account and then upgrade the account to Business Account.</li><li>`BC_AUTH_TT`: TikTok Account User in Business Center. This type of identity is created when you add a TikTok account to your Business Center, and the TikTok account owner approves your request. </li><li>`TTS_TT`: TikTok Account User for TikTok Shop. This type of identity is created when you set an official TikTok account for the TikTok Shop.</li></ul> |
###| identity_authorized_bc_id | string | Returned only when `identity_type` is `BC_AUTH_TT`. <br><br>The ID of the Business Center that a TikTok Account User in Business Center identity is associated with. |
###| identity_authorized_shop_id | string | Returned for some `BC_AUTH_TT` identities. <br><br>The ID of the TikTok Shop that the TikTok Account User in Business Center identity is associated with. |
###| store_id | string | Returned only when `identity_type` is `TTS_TT`. <br><br>The ID of the TikTok Shop that a TikTok Account User for TikTok Shop identity is associated with. |
###| profile_image | string | Temporary profile image URL for the TikTok account that is associated with the identity. <br><br>Validity period: around 48 hours. The expiration time is included in the URL after the `x-expires` parameter, in the format of an Epoch/Unix timestamp in seconds.<br><br>Once the URL expires, you need to call [/gmv_max/video/get/](45-gmv-max-p2.md#doc-1822001168512129) to obtain a new URL. |
###| display_name| string | The display name of the TikTok account that is associated with the identity. |
##| video_info | object | Details of the video in the post. |
###| video_id | string | The ID of the video. |
###| video_cover_url | string | Temporary URL for the video cover.<br><br>Validity period: around 24 hours. The expiration time is included in the URL after the `x-expires` parameter, in the format of an Epoch/Unix timestamp in seconds. <br><br>Once the URL expires, you need to call [/gmv_max/video/get/](45-gmv-max-p2.md#doc-1822001168512129) to obtain a new URL. |
###| preview_url | string | Temporary preview URL for the video. <br><br>Validity period: six hours.<br><br>Once the URL expires, you need to call [/gmv_max/video/get/](45-gmv-max-p2.md#doc-1822001168512129) to obtain a new URL. |
###| height | number | The height of the video in pixels. <br><br> Example: 1920. |
###| width | number | The width of the video in pixels.<br><br>Example: 1080. |
###| bit_rate | number | The bit rate of the video in bps. <br><br>Example: 8500323. |
###| duration | number | The duration of the video in seconds. <br><br>Example: 3.669. |
###| size | number | The size of the video in bytes. <br><br>Example: 3898461. |
###| signature | string | The MD5 of the video. <br><br>Example: `ab1cd2345e678fghi91jkl23b456m7no`. |
###| format | string | The format of the video.<br><br>Example: `mp4`. |
###| definition | string | The definition of the video.<br><br> Example: `1080p`. |
###| fps | number | The frames per second (FPS) of the video. <br><br>Example: 27. |
#| page_info | object | Pagination information. |
##| page | number | Current Số trang cần lấy dữ liệu. |
##| page_size | number | Page size. |
##| total_number | number | Tổng số kết quả tìm thấy. |
##| total_page | number | Total pages of results. |

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "item_list": [
            {
                "identity_info": {
                    "display_name": "{{display_name}}",
                    "identity_id": "{{identity_id}}",
                    "identity_type": "AUTH_CODE",
                    "profile_image": "{{profile_image}}"
                },
                "item_id": "{{item_id}}",
                "spu_id_list": [
                    "{{spu_id}}"
                ],
                "text": "{{text}}",
                "video_info": {
                    "bit_rate": 8500323,
                    "definition": "1080p",
                    "duration": 3.669,
                    "format": "mp4",
                    "fps": 30,
                    "height": 1920,
                    "preview_url": "{{preview_url}}",
                    "signature": "{{signature}}",
                    "size": 3898461,
                    "video_cover_url": "{{video_cover_url}}",
                    "video_id": "{{video_id}}",
                    "width": 1080
                }
            },
            {
                "identity_info": {
                    "display_name": "{{display_name}}",
                    "identity_id": "{{identity_id}}",
                    "identity_type": "AUTH_CODE",
                    "profile_image": "{{profile_image}}"
                },
                "item_id": "{{item_id}}",
                "spu_id_list": [
                    "{{spu_id}}"
                ],
                "text": "{{text}}",
                "video_info": {
                    "bit_rate": 109400,
                    "definition": "540p",
                    "duration": 5.256,
                    "format": "mp4",
                    "fps": 27,
                    "height": 1024,
                    "preview_url": "{{preview_url}}",
                    "signature": "{{signature}}",
                    "size": 71876,
                    "video_cover_url": "{{video_cover_url}}",
                    "video_id": "{{video_id}}",
                    "width": 576
                }
            },
            {
                "identity_info": {
                    "display_name": "{{display_name}}",
                    "identity_authorized_bc_id": "{{identity_authorized_bc_id}}",
                    "identity_id": "{{identity_id}}",
                    "identity_type": "BC_AUTH_TT",
                    "profile_image": "{{profile_image}}"
                },
                "item_id": "{{item_id}}",
                "spu_id_list": [
                    "{{spu_id}}"
                ],
                "text": "{{text}}",
                "video_info": {
                    "bit_rate": 164638,
                    "definition": "540p",
                    "duration": 5,
                    "format": "mp4",
                    "fps": 30,
                    "height": 1024,
                    "preview_url": "{{preview_url}}",
                    "signature": "{{signature}}",
                    "size": 107982,
                    "video_cover_url": "{{video_cover_url}}",
                    "video_id": "{{video_id}}",
                    "width": 576
                }
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

<a id="doc-1830215925061633"></a>
<!-- doc_id: 1830215925061633 -->
<!-- doc_id: 1830215925061633 -->
# (To be deprecated) Get details of videos in customized posts
> Đường dẫn: API Reference > GMV Max > (To be deprecated) Get details of videos in customized posts
Sử dụng endpoint này để truy xuất the details of videos that have been used in the customized post collection for a Product GMV Max Campaign.

> **Important:** 
> This endpoint will be deprecated in the next API version. To ensure a seamless integration, retrieve the details of videos used in customized posts using [/gmv_max/creation/custom_anchor_video_list/get/](45-gmv-max-p2.md#doc-1866513156712449) and [/gmv_max/creation/shop_video/video_anchors/](45-gmv-max-p2.md#doc-1866513161692161).

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/gmv_max/custom_anchor_video_list/get/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
| advertiser_id  ***(Bắt buộc)***| string | ID tài khoản quảng cáo TikTok. |
| campaign_id ***(Bắt buộc)*** | string | The ID of a GMV Max Campaign.<br><br>To filter existing GMV Max Campaigns within your ad account, use [/gmv_max/campaign/get/](45-gmv-max-p1.md#doc-1826463372290177).<br><br><p><span style="color:darkred"><b>Important</b></span>: Starting April 30th, 2026, this parameter will be required to enhance security. To ensure a smooth API integration, we recommend that you update your integration to specify this parameter in all future calls.</p> |
| campaign_custom_anchor_video_id ***(Bắt buộc)***| string | The ID of the collection of customized posts created in a Product GMV Max Campaign.<br><br>To obtain the customized post collection associated with a Product GMV Max Campaign, use [/campaign/gmv_max/info/](45-gmv-max-p1.md#doc-1822000968821762) and check the returned `campaign_custom_anchor_video_id`. |
| custom_anchor_video_list ***(Bắt buộc)*** | object[] | The list of videos with customized product links (custom anchor videos) to filter the results by.<br><br>Kích thước tối đa: 20.<br><br>To obtain the customized posts associated with a Product GMV Max Campaign, use [/campaign/gmv_max/info/](45-gmv-max-p1.md#doc-1822000968821762) and check the returned `custom_anchor_video_list`. |
#| item_id  {Required}| string |  The ID of the TikTok video. |
#| identity_info  {Required}| object | Information about the identity associated with the post. |
##|identity_id  {Required}| string | Identity ID.|
##|identity_type {Required} | string | Identity type.<br><br>Các giá trị enum hỗ trợ: <ul><li>`AUTH_CODE`: Authorized User. This type of identity is created when you use the authorization code to access a TikTok account or a TikTok post.</li><li>`TT_USER`: TikTok User. This type of identity is created when you bind your TikTok For Business account with your TikTok Business Account, or when you bind your TikTok For Business account with your regular TikTok account and then upgrade the account to Business Account.</li><li>`BC_AUTH_TT`: TikTok Account User in Business Center. This type of identity is created when you add a TikTok account to your Business Center, and the TikTok account owner approves your request.</li><li>`TTS_TT`: TikTok Account User for TikTok Shop. This type of identity is created when you set an official TikTok account for the TikTok Shop.</li></ul> |
##|identity_authorized_bc_id {+Conditional} | string | Bắt buộc khi `identity_type` is `BC_AUTH_TT`.<br><br>The ID of the Business Center that a TikTok Account User in Business Center identity is associated with. |
##|identity_authorized_shop_id  {+Conditional}| string | Required only when `identity_type` is `BC_AUTH_TT` and `identity_authorized_shop_id` is returned for the identity from [/gmv_max/identity/get/](45-gmv-max-p2.md#doc-1822001101474882).<br><br>The ID of the TikTok Shop that a TikTok Account User in Business Center identity is associated with. |
##|store_id {+Conditional}| string |  Bắt buộc khi `identity_type` is `TTS_TT`.<br><br>The ID of the TikTok Shop that a TikTok Account User for TikTok Shop identity is associated with. |
#| spu_id_list | string[] | The SPU IDs of the products associated with the customized product anchor link in the TikTok video.<br><br>Kích thước tối đa: 1.<br><br>If you want to have `spu_id_list` included in the response, specify `spu_id_list` in the request. |

### Ví dụ lệnh cURL (Example)
#### Include `spu_id_list` in the response
```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/gmv_max/custom_anchor_video_list/get/?advertiser_id={{advertiser_id}}&campaign_id={{campaign_id}}&campaign_custom_anchor_video_id={{campaign_custom_anchor_video_id}}&custom_anchor_video_list=[{"item_id":"{{item_id}}","identity_info":{"identity_id":"{{identity_id}}","identity_type":"TT_USER"},"spu_id_list":["{{spu_id}}"]}]'
--header 'Access-Token: {{Access-Token}}'
```
#### Exclude `spu_id_list` from the response
```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/gmv_max/custom_anchor_video_list/get/?advertiser_id={{advertiser_id}}&campaign_id={{campaign_id}}&campaign_custom_anchor_video_id={{campaign_custom_anchor_video_id}}&custom_anchor_video_list=[{"item_id":"{{item_id}}","identity_info":{"identity_id":"{{identity_id}}","identity_type":"TT_USER"}}]'
--header 'Access-Token: {{Access-Token}}'
```
## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|code |number|Response code. For the complete list of response codes and descriptions, see [Appendix-Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message|string|Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|request_id |string|The log ID of a request, which uniquely identifies the request.  |
|data |object|Returned data.|
#|  custom_anchor_video_list | object[] | The list of custom anchor videos. |
##| item_id | string | The ID of the TikTok video.<br><br>Example: `1234567891234567891`. |
##| text | string | The caption of the TikTok post.<br><br>Example: `summer`. |
##| spu_id_list |  string[]| Returned only when `spu_id_list` is specified in the request.<br><br>The list of Product SPU IDs that the TikTok post is associated with. |
##| identity_info | object | Information about the identity associated with the TikTok post. |
###| identity_id | string | Identity ID.<br><br>Example: `identity_12345`. |
###| identity_type | string | Identity type.<br><br>Các giá trị enum hỗ trợ: <ul><li>`AUTH_CODE`: Authorized User. This type of identity is created when you use the authorization code to access a TikTok account or a TikTok post.</li><li>`TT_USER`: TikTok User. This type of identity is created when you bind your TikTok For Business account with your TikTok Business Account, or when you bind your TikTok For Business account with your regular TikTok account and then upgrade the account to Business Account.</li><li>`BC_AUTH_TT`: TikTok Account User in Business Center. This type of identity is created when you add a TikTok account to your Business Center, and the TikTok account owner approves your request.</li><li>`TTS_TT`: TikTok Account User for TikTok Shop. This type of identity is created when you set an official TikTok account for the TikTok Shop.</li></ul> |
###| identity_authorized_bc_id | string | Returned only when `identity_type` is `BC_AUTH_TT`.<br><br>The ID of the Business Center that a TikTok Account User in Business Center identity is associated with. |
###| identity_authorized_shop_id | string | Returned for some `BC_AUTH_TT` identities.<br><br>The ID of the TikTok Shop that the TikTok Account User in Business Center identity is associated with. |
###| store_id | string | Returned only when `identity_type` is `TTS_TT`.<br><br>The ID of the TikTok Shop that a TikTok Account User for TikTok Shop identity is associated with. |
###| profile_image | string | Temporary profile image URL for the TikTok account that is associated with the identity.<br><br>Validity period: around 48 hours. The expiration time is included in the URL after the `x-expires` parameter, in the format of an Epoch/Unix timestamp in seconds.<br><br>Once the URL expires, you need to call [/gmv_max/custom_anchor_video_list/get/](45-gmv-max-p2.md#doc-1830215925061633) to obtain a new URL. |
###| user_name | string | The username of the TikTok account that is associated with the identity. |
##| video_info | object | Details of the video in the post. |
###| video_id | string | The ID of the video.<br><br>Example: `video_12345`. |
###| video_cover_url | string | Temporary URL for the video cover.<br><br>Validity period: around 24 hours. The expiration time is included in the URL after the `x-expires` parameter, in the format of an Epoch/Unix timestamp in seconds.<br><br>Once the URL expires, you need to call [/gmv_max/custom_anchor_video_list/get/](45-gmv-max-p2.md#doc-1830215925061633) to obtain a new URL. |
###| preview_url | string | Temporary preview URL for the video.<br><br>Validity period: six hours.<br><br>Once the URL expires, you need to call [/gmv_max/custom_anchor_video_list/get/](45-gmv-max-p2.md#doc-1830215925061633) to obtain a new URL. |
###| height | number | The height of the video in pixels.<br><br>Example: 1920. |
###| width | number | The width of the video in pixels.<br><br>Example: 1080. |
###| bit_rate | number | The bit rate of the video in bps.<br><br>Example: 8500323. |
###| duration | number | The duration of the video in seconds.<br><br>Example: 3.669. |
###| size | number | The size of the video in bytes.<br><br>Example: 3898461. |
###| signature | string | The MD5 of the video.<br><br>Example: `ab1cd2345e678fghi91jkl23b456m7no`. |
###| format | string | The format of the video.<br><br>Example: `mp4`. |
###| definition | string | The definition of the video.<br><br>Example: `1080p`. |
###| fps | number | The frames per second (FPS) of the video.<br><br>Example: 27. |

### Ví dụ lệnh cURL (Example)
#### Include `spu_id_list` in the response
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "custom_anchor_video_list": [
            {
                "identity_info": {
                    "identity_id": "{{identity_id}}",
                    "identity_type": "TT_USER",
                    "profile_image": "{{profile_image}}",
                    "user_name": "{{user_name}}"
                },
                "item_id": "{{item_id}}",
                "spu_id_list": [
                    "{{spu_id}}"
                ],
                "text": "{{text}}",
                "video_info": {
                    "bit_rate": 824497,
                    "definition": "540p",
                    "duration": 10.444,
                    "format": "mp4",
                    "fps": 30,
                    "height": 960,
                    "preview_url": "{{preview_url}}",
                    "signature": "{{signature}}",
                    "size": 1076382,
                    "video_cover_url": "{{video_cover_url}}",
                    "video_id": "{{video_id}}",
                    "width": 540
                }
            }
        ]
    }
}
```
#### Exclude `spu_id_list` from the response
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "custom_anchor_video_list": [
            {
                "identity_info": {
                    "identity_id": "{{identity_id}}",
                    "identity_type": "TT_USER",
                    "profile_image": "{{profile_image}}",
                    "user_name": "{{user_name}}"
                },
                "item_id": "{{item_id}}",
                "text": "{{text}}",
                "video_info": {
                    "bit_rate": 824497,
                    "definition": "540p",
                    "duration": 10.444,
                    "format": "mp4",
                    "fps": 30,
                    "height": 960,
                    "preview_url": "{{preview_url}}",
                    "signature": "{{signature}}",
                    "size": 1076382,
                    "video_cover_url": "{{video_cover_url}}",
                    "video_id": "{{video_id}}",
                    "width": 540
                }
            }
        ]
    }
}
```

---

<a id="doc-1861260625563202"></a>
<!-- doc_id: 1861260625563202 -->
<!-- doc_id: 1861260625563202 -->
# Remove or add back creatives in a GMV Max Campaign
> Đường dẫn: API Reference > GMV Max > Remove or add back creatives in a GMV Max Campaign
Dùng endpoint này để xóa creative (video) khỏi chiến dịch Product hoặc Live GMV Max, hoặc khôi phục các creative đã bị xóa trước đó.

## Yêu cầu gọi API (Request)
**Endpoint** https://business-api.tiktok.com/open_api/v1.3/campaign/gmv_max/creative/update/

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
| campaign_id  ****(Bắt buộc)**** | string | ID chiến dịch quảng cáo. ⏎ **Note**: • The campaign must be in an active status. To retrieve active GMV Max Campaigns in your ad account, use [/gmv_max/report/get/](45-gmv-max-p2.md#doc-1824721673497601) with `filtering` set to `{"campaign_statuses":["STATUS_DELIVERY_OK"]}`. • If the campaign is a Product GMV Max Campaign, the `product_video_specific_type` of the campaign must be `AUTO_SELECTION`. |
| action  ****(Bắt buộc)**** | string | The type of action to perform. ⏎ Các giá trị enum hỗ trợ: • `REMOVE`: To remove creatives from a GMV Max Campaign. • `ADD`: To add previously removed creatives back into a GMV Max Campaign. ⏎ **Note**: • Once the action is performed, wait 20 minutes before verifying the updated statuses using [/gmv_max/report/get/](45-gmv-max-p2.md#doc-1824721673497601). • If a creative is successfully removed from a Product GMV Max Campaign, its `creative_delivery_status` in [/gmv_max/report/get/](45-gmv-max-p2.md#doc-1824721673497601) will be `EXCLUDED`. |
| item_list  ****(Bắt buộc)**** | object[] | The list of TikTok posts (videos) to be operated on. ⏎ Kích thước tối đa: 400. ⏎ **Note**: • This endpoint allows for the removal of up to 10,000 posts from a GMV Max Campaign created via API and up to 2,500 posts from a GMV Max Campaign created via TikTok Ads Manager, with a limit of 400 posts per request. • For example, if you need to exclude 800 posts, send a first request with 400 posts in this field, followed by a second request with the remaining 400. |
| ↳ item_id  ****(Bắt buộc)**** | string | The ID of the TikTok post to operate on. • When `action` is `REMOVE`, use [/gmv_max/report/get/](45-gmv-max-p2.md#doc-1824721673497601) with `filtering` set to `{"creative_delivery_statuses":["IN_QUEUE","LEARNING","DELIVERING","NOT_DELIVERYING","UNAVAILABLE","NOT_ACTIVE"]}` to retrieve eligible creatives. • When `action` is `ADD`, use [/gmv_max/report/get/](45-gmv-max-p2.md#doc-1824721673497601) with `filtering` set to `{"creative_delivery_statuses":["EXCLUDED"]}` to retrieve previously removed creatives. ⏎ **Note**: Currently, you can only obtain the `item_id` of TikTok posts in Live GMV Max Campaigns on TikTok Ads Manager. |
| ↳ spu_id_list **(Điều kiện)** | string[] | Required for a Product GMV Max Campaign. ⏎ The list of Product SPU IDs that the TikTok post is associated with. ⏎ To obtain the list of Product SPU IDs associated with a TikTok post in a Product GMV Max Campaign, use [/campaign/gmv_max/info/](45-gmv-max-p1.md#doc-1822000968821762). |

### Ví dụ lệnh cURL (Example)
#### Remove creatives
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/campaign/gmv_max/creative/update/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id": "{{advertiser_id}}",
    "campaign_id": "{{campaign_id}}",
    "item_list": [
        {
            "item_id": "{{item_id}}",
            "spu_id_list": ["{{spu_id}}"]
        },
        {
            "item_id": "{{item_id}}",
            "spu_id_list": ["{{spu_id}}"]
        }
    ],
    "action": "REMOVE"
}'
```

#### Add back creatives
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/campaign/gmv_max/creative/update/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id": "{{advertiser_id}}",
    "campaign_id": "{{campaign_id}}",
    "item_list": [
        {
            "item_id": "{{item_id}}",
            "spu_id_list": ["{{spu_id}}"]
        },
        {
            "item_id": "{{item_id}}",
            "spu_id_list": ["{{spu_id}}"]
        }
    ],
    "action": "ADD"
}'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| - | - | - |
| code | number | Response code. For the complete list of response codes and descriptions, see [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | The log ID of the request, which uniquely identifies a request. |
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

<a id="doc-1866513154013585"></a>
<!-- doc_id: 1866513154013585 -->
<!-- doc_id: 1866513154013585 -->
# Create shop-level customized TikTok posts
> Đường dẫn: API Reference > GMV Max > Create shop-level customized TikTok posts
Sử dụng endpoint này để tạo shop-level customized TikTok posts.

Shop-level customized TikTok posts are generated by directly linking your TikTok videos to a product at the TikTok Shop level. If the linked product is part of an active campaign, the video linked to that product will be automatically added to that campaign.

## Yêu cầu gọi API (Request)
**Endpoint** https://business-api.tiktok.com/open_api/v1.3/gmv_max/creation/custom_anchor_video_list/create/

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
| store_id  ****(Bắt buộc)**** | string | The ID of a TikTok Shop. ⏎ To obtain a TikTok Shop that is available for GMV Max Campaigns, use [/gmv_max/store/list/](45-gmv-max-p2.md#doc-1822001044479041) and confirm that the returned `is_gmv_max_available` is `true`. |
| store_authorized_bc_id  ****(Bắt buộc)**** | string | The ID of the Business Center that is authorized to access the TikTok Shop (`store_id`). ⏎ To obtain the ID, check the `store_authorized_bc_id` for the `store_id` returned from [/gmv_max/store/list/](45-gmv-max-p2.md#doc-1822001044479041). |
| custom_anchor_video_list  ****(Bắt buộc)**** | object[] | The details of your videos and the products you want to link them to. ⏎ By linking videos to a product at the TikTok Shop level, you can generate shop-level customized TikTok posts. The system will automatically add these shop-level customized TikTok posts to your Product GMV Max Campaign (with `shopping_ads_type` set to `PRODUCT`) if you use the Autoselect creative mode (with `product_video_specific_type` as `AUTO_SELECTION`) and your campaign includes the linked product. ⏎ Kích thước tối đa: 200. |
| ↳ item_id  ****(Bắt buộc)**** | string | The ID of the TikTok video you intend to use in the customized post. ⏎ To retrieve eligible videos, use [/gmv_max/video/get/](45-gmv-max-p2.md#doc-1822001168512129) with `custom_posts_eligible` set to `true`. |
| ↳ identity_info  ****(Bắt buộc)**** | object | Information about the identity (TikTok account) associated with the TikTok video. ⏎ To find the identity details associated with the provided TikTok video (`item_id`), review the `identity_info` corresponding to the `item_id` returned by [/gmv_max/video/get/](45-gmv-max-p2.md#doc-1822001168512129). |
| ↳↳ identity_id  ****(Bắt buộc)**** | string | Identity ID. |
| ↳↳ identity_type  ****(Bắt buộc)**** | string | Identity type. ⏎ Các giá trị enum hỗ trợ: • `AUTH_CODE`: Authorized User. This type of identity is created when you use the authorization code to access a TikTok account or a TikTok post. • `TT_USER`: TikTok User. This type of identity is created when you bind your TikTok For Business account with your TikTok Business Account, or when you bind your TikTok For Business account with your regular TikTok account and then upgrade the account to Business Account. • `BC_AUTH_TT`: TikTok Account User in Business Center. This type of identity is created when you add a TikTok account to your Business Center, and the TikTok account owner approves your request. • `TTS_TT`: TikTok Account User for TikTok Shop. This type of identity is created when you set an official TikTok account for the TikTok Shop. |
| ↳↳ identity_authorized_bc_id **(Điều kiện)** | string | Bắt buộc khi `identity_type` is `BC_AUTH_TT`. ⏎ The ID of the Business Center that a TikTok Account User in Business Center identity is associated with. |
| ↳↳ identity_authorized_shop_id **(Điều kiện)** | string | Required only when `identity_type` is `BC_AUTH_TT` and `identity_authorized_shop_id` is returned for the identity from [/gmv_max/video/get/](45-gmv-max-p2.md#doc-1822001168512129). ⏎ The ID of the TikTok Shop that a TikTok Account User in Business Center identity is associated with. |
| ↳↳ store_id **(Điều kiện)** | string | Bắt buộc khi `identity_type` is `TTS_TT`. ⏎ The ID of the TikTok Shop that a TikTok Account User for TikTok Shop identity is associated with. |
| ↳ spu_id_list  ****(Bắt buộc)**** | string[] | The SPU IDs of the products to link to the video. ⏎ Kích thước tối đa: 1. ⏎ To obtain the list of SPU IDs for products within a TikTok Shop, use [/store/product/get/](69-tiktok-store.md#doc-1793482248880130). Set `ad_creation_eligible` to `GMV_MAX` and select `item_group_id` values where `status` is `AVAILABLE` and `gmv_max_ads_status` is `UNOCCUPIED`. |

### Ví dụ lệnh cURL (Example)
Request
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/gmv_max/creation/custom_anchor_video_list/create/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id": "{{advertiser_id}}",
    "store_id": "{{store_id}}",
    "store_authorized_bc_id": "{{store_authorized_bc_id}}",
    "custom_anchor_video_list": [
        {
            "identity_info": {
                "identity_authorized_bc_id": "{{identity_authorized_bc_id}}",
                "identity_id": "{{identity_id}}",
                "identity_type": "BC_AUTH_TT"
            },
            "item_id": "{{item_id}}",
            "spu_id_list": ["{{spu_id}}"]
        },
        {
            "identity_info": {
                "identity_id": "{{identity_id}}",
                "identity_type": "TT_USER"
            },
            "item_id": "{{item_id}}",
            "spu_id_list": ["{{spu_id}}"]
        }
    ]
}'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| - | - | - |
| code | number | Response code. For the complete list of response codes and descriptions, see [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | The log ID of the request, which uniquely identifies a request. |
| data | object | Returned data. |
| ↳ failure_list | object | The list of shop-level customized TikTok posts that could not be successfully created. |
| ↳↳ item_id | object[] | The ID of a TikTok video you intended to use in the customized post. |
| ↳↳ identity_info | string[] | Information about the identity (TikTok account) associated with the TikTok video. |
| ↳↳↳ identity_id | object | Identity ID. |
| ↳↳↳ identity_type | string | Identity type. ⏎ Các giá trị enum hỗ trợ: • `AUTH_CODE`: Authorized User. This type of identity is created when you use the authorization code to access a TikTok account or a TikTok post. • `TT_USER`: TikTok User. This type of identity is created when you bind your TikTok For Business account with your TikTok Business Account, or when you bind your TikTok For Business account with your regular TikTok account and then upgrade the account to Business Account. • `BC_AUTH_TT`: TikTok Account User in Business Center. This type of identity is created when you add a TikTok account to your Business Center, and the TikTok account owner approves your request. • `TTS_TT`: TikTok Account User for TikTok Shop. This type of identity is created when you set an official TikTok account for the TikTok Shop. |
| ↳↳↳ identity_authorized_bc_id | string | The ID of the Business Center that a TikTok Account User in Business Center identity is associated with. |
| ↳↳↳ identity_authorized_shop_id | string | The ID of the TikTok Shop that a TikTok Account User in Business Center identity is associated with. |
| ↳↳↳ store_id | string | The ID of the TikTok Shop that a TikTok Account User for TikTok Shop identity is associated with. |
| ↳↳ spu_id_list | string | The SPU IDs of the products to link to the video. |
| ↳↳ reason | string | The reason for the failure. ⏎ Các giá trị enum hỗ trợ: • `IDENTITY_NO_PERMISSION`: You do not have the required permissions for this identity. • `INVALID_PARAMETER`: Invalid parameters are submitted. • `AUTH_CODE_CAN_NOT_CHANGE_ANCHOR`: The anchor in the video cannot be changed without user permission. • `ITEM_NOT_FOUND`: The TikTok video cannot be found. • `NATIVE_ANCHOR_EXISTS`: The product link you want to add is the same as the product link already present in the video. |
| ↳↳ error_message | string | The detailed error message. |

### Ví dụ lệnh cURL (Example)
```http
// curl
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "failure_list": []
    }
}
```

---

<a id="doc-1866513156712449"></a>
<!-- doc_id: 1866513156712449 -->
<!-- doc_id: 1866513156712449 -->
# Get customized TikTok posts
> Đường dẫn: API Reference > GMV Max > Get customized TikTok posts
Sử dụng endpoint này để truy xuất a list of shop-level and campaign-level customized TikTok posts created from an ad account for a specific TikTok Shop.

Shop-level customized TikTok posts are generated by directly linking your TikTok videos to a product at the TikTok Shop level. If the linked product is part of an active campaign, the video linked to that product will be automatically added to that campaign. In contrast, campaign-level customized TikTok posts are generated by linking your TikTok videos to a product during the Product GMV Max Campaign creation process and are exclusive to the campaign.

## Yêu cầu gọi API (Request)
**Endpoint** https://business-api.tiktok.com/open_api/v1.3/gmv_max/creation/custom_anchor_video_list/get/

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
| store_id  ****(Bắt buộc)**** | string | The ID of a TikTok Shop. ⏎ To obtain a TikTok Shop that is available for GMV Max Campaigns, use [/gmv_max/store/list/](45-gmv-max-p2.md#doc-1822001044479041) and confirm that the returned `is_gmv_max_available` is `true`. |
| store_authorized_bc_id  ****(Bắt buộc)**** | string | The ID of the Business Center that is authorized to access the TikTok Shop (`store_id`). ⏎ To obtain the ID, check the `store_authorized_bc_id` for the `store_id` returned from [/gmv_max/store/list/](45-gmv-max-p2.md#doc-1822001044479041). |
| creative_source  ****(Bắt buộc)**** | string | Creative source type. ⏎ Enum value: • `CUSTOMIZED`: customized post. |
| spu_id_list | string[] | A list of Product SPU (standard product unit) IDs to filter the results by. ⏎ To obtain the list of SPU IDs for products within a TikTok Shop, use [/store/product/get/](69-tiktok-store.md#doc-1793482248880130). Set `ad_creation_eligible` to `GMV_MAX` and select `item_group_id` values where `status` is `AVAILABLE` and `gmv_max_ads_status` is `UNOCCUPIED`. |
| sort_field | string | The sorting field. ⏎ Các giá trị enum hỗ trợ: • `GMV`: GMV. • `POST_TIME`: Post time. • `VIDEO_VIEWS`: Video views. • `VIDEO_LIKES`: Video likes. • `CLICK_THROUGH_RATE`: Click-through Rate (CTR). • `PRODUCT_CLICKS`: Product clicks. ⏎ Giá trị mặc định: `GMV`. |
| sort_type | string | The Thứ tự sắp xếp kết quả. ⏎ Các giá trị enum hỗ trợ: • `ASC`: ascending. • `DESC`: descending. |
| keyword | string | A search keyword to filter posts (videos). ⏎ You can specify a post ID or caption. • To search by post caption (`text`), provide a text string. This search type supports multiple-language searches and fuzzy matches. ⏎ Example: `summer`. • To search by post ID (`item_id`), provide a numeric string with at least 19 characters. This search type supports exact matches. ⏎ Example: `1234567891234567891`. |
| need_auth_code_video | boolean | Có thực hiện include posts associated with `AUTH_CODE` identities in the results. ⏎ Các giá trị được hỗ trợ: `true`, `false`. ⏎ Giá trị mặc định: `false`. ⏎ **Note**: If `need_auth_code_video` is `false` or not passed and `identity_list` is not specified, you will retrieve an empty post list. |
| identity_list | object[] | A list of `TT_USER`, `BC_AUTH_TT`, or `TTS_TT` identities to filter the results by. ⏎ To obtain a list of identities available for Product GMV Max Campaigns, use [/gmv_max/identity/get/](45-gmv-max-p2.md#doc-1822001101474882) and select identities with `product_gmv_max_available` as `true`. ⏎ Kích thước tối đa: 20. ⏎ **Note**: If `need_auth_code_video` is `false` or not passed and `identity_list` is not specified, you will retrieve an empty post list. |
| ↳ identity_id | string | Identity ID. |
| ↳ identity_type | string | Identity type. ⏎ Các giá trị enum hỗ trợ: • `TT_USER`: TikTok User. This type of identity is created when you bind your TikTok For Business account with your TikTok Business Account, or when you bind your TikTok For Business account with your regular TikTok account and then upgrade the account to Business Account. • `BC_AUTH_TT`: TikTok Account User in Business Center. This type of identity is created when you add a TikTok account to your Business Center, and the TikTok account owner approves your request. • `TTS_TT`: TikTok Account User for TikTok Shop. This type of identity is created when you set an official TikTok account for the TikTok Shop. |
| ↳ identity_authorized_bc_id | string | Bắt buộc khi `identity_type` is `BC_AUTH_TT`. ⏎ The ID of the Business Center that a TikTok Account User in Business Center identity is associated with. |
| ↳ identity_authorized_shop_id | string | Required only when `dentity_type` is `BC_AUTH_TT` and `identity_authorized_shop_id` is returned for the identity from [/gmv_max/identity/get/](45-gmv-max-p2.md#doc-1822001101474882). ⏎ The ID of the TikTok Shop that a TikTok Account User in Business Center identity is associated with. |
| ↳ store_id | string | Bắt buộc khi `identity_type` is `TTS_TT`. ⏎ The ID of the TikTok Shop that a TikTok Account User for TikTok Shop identity is associated with. |
| campaign_id | string | The ID of a Product GMV Max Campaign to filter the returns by. ⏎ You can use this field to filter campaign-level customized posts. If this field is not specified, the results will only include shop-level customized posts. ⏎ To retrieve existing Product GMV Max Campaigns within your ad account, use [/gmv_max/campaign/get/](45-gmv-max-p1.md#doc-1826463372290177) and set `filtering` to `{"gmv_max_promotion_types":["PRODUCT_GMV_MAX"]}`. |
| page | number | Current Số trang cần lấy dữ liệu. ⏎ Value range: ≥ 1. ⏎ Giá trị mặc định: 1. |
| page_size | number | Page size. ⏎ Value range: 1-50. ⏎ Giá trị mặc định: 10. |

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/gmv_max/creation/custom_anchor_video_list/get/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id": "{{advertiser_id}}",
    "store_id": "{{store_id}}",
    "store_authorized_bc_id": "{{store_authorized_bc_id}}",
    "spu_id_list": ["{{spu_id}}"],
    "identity_list": [
        {
            "identity_authorized_bc_id": "{{identity_authorized_bc_id}}",
            "identity_id": "{{identity_id}}",
            "identity_type": "BC_AUTH_TT"
        },
        {
            "identity_id": "{{identity_id}}",
            "identity_type": "TTS_TT",
            "store_id": "{{store_id}}"
        },
        {
            "identity_id": "{{identity_id}}",
            "identity_type": "TT_USER"
        }
    ],
    "need_auth_code_video": true,
    "creative_source": "CUSTOMIZED",
    "page": 1,
    "page_size": 20
}'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| - | - | - |
| code | number | Response code. For the complete list of response codes and descriptions, see [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | The log ID of the request, which uniquely identifies a request. |
| data | object | Returned data. |
| ↳ item_list | object[] | A list of TikTok videos (posts) available for Product GMV Max campaigns using the specified TikTok Shop. |
| ↳↳ item_id | string | The ID of the TikTok post. |
| ↳↳ text | string | The caption of the TikTok post. |
| ↳↳ spu_id_list | string[] | The list of Product SPU IDs that the TikTok post is associated with. ⏎ **Note**: This field is not included in the response for videos with no product anchor link. |
| ↳↳ can_change_anchor | boolean | Liệu you can change the product anchor link in this video. ⏎ Các giá trị được hỗ trợ: • `true`: You can add a product anchor link to create a customized post. • `false`: You cannot use the video to create a customized post. ⏎ **Note**: If `can_change_anchor` is `false`, you cannot pass the video to `custom_anchor_video_list` or `item_list` in [/campaign/gmv_max/create/](45-gmv-max-p1.md#doc-1822000988713089) or [/campaign/gmv_max/update/](45-gmv-max-p1.md#doc-1822001009002497) to create customized posts. |
| ↳↳ identity_info | object | Information about the identity associated with the TikTok post. |
| ↳↳↳ identity_id | string | Identity ID. |
| ↳↳↳ identity_type | string | Identity type. ⏎ Các giá trị enum hỗ trợ: • `AUTH_CODE`: Authorized User. This type of identity is created when you use the authorization code to access a TikTok account or a TikTok post. • `TT_USER`: TikTok User. This type of identity is created when you bind your TikTok For Business account with your TikTok Business Account, or when you bind your TikTok For Business account with your regular TikTok account and then upgrade the account to Business Account. • `BC_AUTH_TT`: TikTok Account User in Business Center. This type of identity is created when you add a TikTok account to your Business Center, and the TikTok account owner approves your request. • `TTS_TT`: TikTok Account User for TikTok Shop. This type of identity is created when you set an official TikTok account for the TikTok Shop. |
| ↳↳↳ identity_authorized_bc_id | string | Returned only when `identity_type` is `BC_AUTH_TT`. ⏎ The ID of the Business Center that a TikTok Account User in Business Center identity is associated with. |
| ↳↳↳ identity_authorized_shop_id | string | Returned for some `BC_AUTH_TT` identities. ⏎ The ID of the TikTok Shop that the TikTok Account User in Business Center identity is associated with. |
| ↳↳↳ store_id | string | Returned only when `identity_type` is `TTS_TT`. ⏎ The ID of the TikTok Shop that a TikTok Account User for TikTok Shop identity is associated with. |
| ↳↳↳ profile_image | string | Temporary profile image URL for the TikTok account that is associated with the identity. ⏎ Validity period: around 48 hours. The expiration time is included in the URL after the `x-expires` parameter, in the format of an Epoch/Unix timestamp in seconds. ⏎ Once the URL expires, you need to call [/gmv_max/video/get/](45-gmv-max-p2.md#doc-1822001168512129) to obtain a new URL. |
| ↳↳↳ display_name | string | The display name of the TikTok account that is associated with the identity. |
| ↳↳ video_info | object | Details of the video in the post. |
| ↳↳↳ video_id | string | The ID of the video. |
| ↳↳↳ video_cover_url | string | Temporary URL for the video cover. ⏎ Validity period: around 24 hours. The expiration time is included in the URL after the `x-expires` parameter, in the format of an Epoch/Unix timestamp in seconds. ⏎ Once the URL expires, you need to call [/gmv_max/video/get/](45-gmv-max-p2.md#doc-1822001168512129) to obtain a new URL. |
| ↳↳↳ preview_url | string | Temporary preview URL for the video. ⏎ Validity period: six hours. ⏎ Once the URL expires, you need to call [/gmv_max/video/get/](45-gmv-max-p2.md#doc-1822001168512129) to obtain a new URL. |
| ↳↳↳ height | number | The height of the video in pixels. ⏎ Example: 1920. |
| ↳↳↳ width | number | The width of the video in pixels. ⏎ Example: 1080. |
| ↳↳↳ bit_rate | number | The bit rate of the video in bps. ⏎ Example: 8500323. |
| ↳↳↳ duration | number | The duration of the video in seconds. ⏎ Example: 3.669. |
| ↳↳↳ size | number | The size of the video in bytes. ⏎ Example: 3898461. |
| ↳↳↳ signature | string | The MD5 of the video. ⏎ Example: `ab1cd2345e678fghi91jkl23b456m7no`. |
| ↳↳↳ format | string | The format of the video. ⏎ Example: `mp4`. |
| ↳↳↳ definition | string | The definition of the video. ⏎ Example: `1080p`. |
| ↳↳↳ fps | number | The frames per second (FPS) of the video. ⏎ Example: 27. |
| ↳ page_info | object | Pagination information. |
| ↳↳ page | number | Current Số trang cần lấy dữ liệu. |
| ↳↳ page_size | number | Page size. |
| ↳↳ total_number | number | Tổng số kết quả tìm thấy. |
| ↳↳ total_page | number | Total pages of results. |

### Ví dụ lệnh cURL (Example)
```http
// curl
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "item_list": [
            {
                "can_change_anchor": true,
                "identity_info": {
                    "avatar_url": "{{avatar_url}}",
                    "display_name": "{{display_name}}",
                    "identity_authorized_bc_id": "{{identity_authorized_bc_id}}",
                    "identity_id": "{{identity_id}}",
                    "identity_type": "BC_AUTH_TT"
                },
                "item_id": "{{item_id}}",
                "text": "{{text}}",
                "video_info": {
                    "bit_rate": {{bit_rate}},
                    "definition": "720p",
                    "duration": {{duration}},
                    "format": "mp4",
                    "fps": {{fps}},
                    "height": {{height}},
                    "preview_url": "{{preview_url}}",
                    "signature": "{{signature}}",
                    "size": {{size}},
                    "video_cover_url": "{{video_cover_url}}",
                    "video_id": "{{video_id}}",
                    "width": {{width}}
                }
            },
            {
                "can_change_anchor": true,
                "identity_info": {
                    "avatar_url": "{{avatar_url}}",
                    "display_name": "{{display_name}}",
                    "identity_id": "{{identity_id}}",
                    "identity_type": "TT_USER"
                },
                "item_id": "{{item_id}}",
                "text": "{{text}}",
                "video_info": {
                    "bit_rate": {{bit_rate}},
                    "definition": "720p",
                    "duration": {{duration}},
                    "format": "mp4",
                    "fps": {{fps}},
                    "height": {{height}},
                    "preview_url": "{{preview_url}}",
                    "signature": "{{signature}}",
                    "size": {{size}},
                    "video_cover_url": "{{video_cover_url}}",
                    "video_id": "{{video_id}}",
                    "width": {{width}}
                }
            }
        ],
        "page_info": {
            "page": 1,
            "page_size": 20,
            "total_number": 2,
            "total_page": 1
        }
    }
}
```

---

<a id="doc-1866513159202306"></a>
<!-- doc_id: 1866513159202306 -->
<!-- doc_id: 1866513159202306 -->
# Delete customized TikTok posts
> Đường dẫn: API Reference > GMV Max > Delete customized TikTok posts
Sử dụng endpoint này để xóa shop-level or campaign-level customized TikTok posts.

Shop-level customized TikTok posts are generated by directly linking your TikTok videos to a product at the TikTok Shop level. If the linked product is part of an active campaign, the video linked to that product will be automatically added to that campaign. In contrast, campaign-level customized TikTok posts are generated by linking your TikTok videos to a product during the Product GMV Max Campaign creation process and are exclusive to the campaign.

## Yêu cầu gọi API (Request)
**Endpoint** https://business-api.tiktok.com/open_api/v1.3/gmv_max/creation/custom_anchor_video_list/delete/

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
| store_id  ****(Bắt buộc)**** | string | The ID of a TikTok Shop. ⏎ To obtain a TikTok Shop that is available for GMV Max Campaigns, use [/gmv_max/store/list/](45-gmv-max-p2.md#doc-1822001044479041) and confirm that the returned `is_gmv_max_available` is `true`. |
| store_authorized_bc_id  ****(Bắt buộc)**** | string | The ID of the Business Center that is authorized to access the TikTok Shop (`store_id`). ⏎ To obtain the ID, check the `store_authorized_bc_id` for the `store_id` returned from [/gmv_max/store/list/](45-gmv-max-p2.md#doc-1822001044479041). |
| custom_anchor_video_list  ****(Bắt buộc)**** | object[] | The details of the videos and the products you want to unlink from them. ⏎ Kích thước tối đa: 200. |
| ↳ item_id  ****(Bắt buộc)**** | string | The ID of the TikTok video you no longer want to use in a customized post. ⏎ To retrieve TikTok videos currently used in customized posts, use [/gmv_max/creation/custom_anchor_video_list/get/](45-gmv-max-p2.md#doc-1866513156712449). |
| ↳ spu_id_list  ****(Bắt buộc)**** | string[] | The Product SPU (standard product unit) ID of the product you want to unlink from the video. ⏎ To retrieve the products linked to a TikTok video used in customized posts, use [/gmv_max/creation/custom_anchor_video_list/get/](45-gmv-max-p2.md#doc-1866513156712449). |
| campaign_id **(Điều kiện)** | string | Bắt buộc khi the specified TikTok videos (`item_id`) have been used in a campaign to create campaign-level customized posts. ⏎ The ID of a Product GMV Max Campaign. ⏎ To retrieve existing Product GMV Max Campaigns within your ad account, use [/gmv_max/campaign/get/](45-gmv-max-p1.md#doc-1826463372290177) and set `filtering` to `{"gmv_max_promotion_types":["PRODUCT_GMV_MAX"]}`. |

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/gmv_max/creation/custom_anchor_video_list/delete/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id": "{{advertiser_id}}",
    "store_id": "{{store_id}}",
    "store_authorized_bc_id": "{{store_authorized_bc_id}}",
    "custom_anchor_video_list": [
        {
            "item_id": "{{item_id}}",
            "spu_id_list": ["{{spu_id}}"]
        },
        {
            "item_id": "{{item_id}}",
            "spu_id_list": ["{{spu_id}}"]
        }
    ]
}'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| - | - | - |
| code | number | Response code. For the complete list of response codes and descriptions, see [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | The log ID of the request, which uniquely identifies a request. |
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

<a id="doc-1866513161692161"></a>
<!-- doc_id: 1866513161692161 -->
<!-- doc_id: 1866513161692161 -->
# Get product linkage details of videos in customized posts
> Đường dẫn: API Reference > GMV Max > Get product linkage details of videos in customized posts
Sử dụng endpoint này để truy xuất the shop-level or campaign-level product linkage details for videos in customized posts.

Shop-level customized TikTok posts are generated by directly linking your TikTok videos to a product at the TikTok Shop level. If the linked product is part of an active campaign, the video linked to that product will be automatically added to that campaign. In contrast, campaign-level customized TikTok posts are generated by linking your TikTok videos to a product during the Product GMV Max Campaign creation process and are exclusive to the campaign.

## Yêu cầu gọi API (Request)
**Endpoint** https://business-api.tiktok.com/open_api/v1.3/gmv_max/creation/shop_video/video_anchors/

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
| store_id  ****(Bắt buộc)**** | string | The ID of a TikTok Shop. ⏎ To obtain a TikTok Shop that is available for GMV Max Campaigns, use [/gmv_max/store/list/](45-gmv-max-p2.md#doc-1822001044479041) and confirm that the returned `is_gmv_max_available` is `true`. |
| store_authorized_bc_id  ****(Bắt buộc)**** | string | The ID of the Business Center that is authorized to access the TikTok Shop (`store_id`). ⏎ To obtain the ID, check the `store_authorized_bc_id` for the `store_id` returned from [/gmv_max/store/list/](45-gmv-max-p2.md#doc-1822001044479041). |
| item_ids  ****(Bắt buộc)**** | string[] | The list of TikTok videos for which you want to retrieve product linkage information. ⏎ To retrieve TikTok videos used in customized posts, use [/gmv_max/creation/custom_anchor_video_list/get/](45-gmv-max-p2.md#doc-1866513156712449). ⏎ Kích thước tối đa: 20. |
| campaign_id **(Điều kiện)** | string | Bắt buộc khi the specified TikTok videos have been used in a campaign to create campaign-level customized posts. ⏎ The ID of a Product GMV Max Campaign. ⏎ To retrieve existing Product GMV Max Campaigns within your ad account, use [/gmv_max/campaign/get/](45-gmv-max-p1.md#doc-1826463372290177) and set `filtering` to `{"gmv_max_promotion_types":["PRODUCT_GMV_MAX"]}`. |

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/gmv_max/creation/shop_video/video_anchors/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id": "{{advertiser_id}}",
    "store_id": "{{store_id}}",
    "store_authorized_bc_id": "{{store_authorized_bc_id}}",
    "item_id_list": [
        "{{item_id}}"
    ]
}'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| - | - | - |
| code | number | Response code. For the complete list of response codes and descriptions, see [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | The log ID of the request, which uniquely identifies a request. |
| data | object | Returned data. |
| ↳ video_list | object | The product linkage details for the specified videos. |
| ↳↳ item_id | string | The ID of the TikTok video. |
| ↳↳ product_list | object | The list of products that the video is linked to. |
| ↳↳↳ spu_id | string | The SPU ID of the product linked to the TikTok video. |
| ↳↳↳ title | string | The title of the product. |
| ↳↳↳ picture | string | The URL of the product image. |
| ↳↳↳ anchor_source | string | The source of the product anchor in the video. ⏎ Các giá trị enum hỗ trợ: • `CUSTOM`: custom anchor. The product anchor was added to the video through [Shop Creative Hub for GMV Max](https://ads.tiktok.com/help/article/about-shop-creative-hub-for-gmv-max). The linked product will appear in ads traffic. • `ORGANIC`: organic anchor. The product anchor was added to the video through the TikTok app. The linked product will appear in both ads and organic traffic. |

### Ví dụ lệnh cURL (Example)
```http
// curl
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "video_list": [
            {
                "item_id": "{{item_id}}",
                "product_list": [
                    {
                        "anchor_source": "CUSTOM",
                        "picture": "{{picture}}",
                        "spu_id": "{{spu_id}}",
                        "title": "{{title}}"
                    },
                    {
                        "anchor_source": "ORGANIC",
                        "picture": "{{picture}}",
                        "spu_id": "{{spu_id}}",
                        "title": "{{title}}"
                    }
                ]
            }
        ]
    }
}
```

---

<a id="doc-1822001184635905"></a>
<!-- doc_id: 1822001184635905 -->
<!-- doc_id: 1822001184635905 -->
# Get the TikTok Shop exclusive authorization status of an ad account
> Đường dẫn: API Reference > GMV Max > Get the TikTok Shop exclusive authorization status of an ad account
Sử dụng endpoint này để kiểm tra Liệu an ad account is exclusively authorized to create GMV Max Campaigns for a specific TikTok Shop.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/gmv_max/exclusive_authorization/get/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). ⏎ Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
| store_id ***(Bắt buộc)*** | string | The ID of the TikTok Shop.<br><br> To obtain a TikTok Shop that is available for GMV Max Campaigns, use [/gmv_max/store/list/](45-gmv-max-p2.md#doc-1822001044479041) and confirm that the returned `is_gmv_max_available` is `true`. |
|store_authorized_bc_id ***(Bắt buộc)*** | string | ID of the Business Center that is authorized to access the TikTok Shop (`store_id`). |
| advertiser_id ***(Bắt buộc)*** | string | ID of the ad account that you want to check the GMV Max exclusive authorization status for. |

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/gmv_max/exclusive_authorization/get/?store_id={{store_id}}&store_authorized_bc_id={{store_authorized_bc_id}}&advertiser_id={{advertiser_id}}' \
--header 'Access-Token:{{Access-Token}}'
```
## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|code |number|Response code. For the complete list of response codes and descriptions, see [Appendix-Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message|string|Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|request_id |string|The log ID of a request, which uniquely identifies the request.  |
|data |object|Returned data.|
#| store_id | string | The ID of the TikTok Shop. |
#| advertiser_id | string | The ID of the ad account. |
#| authorization_status | string | The status of exclusive authorization for the ad account to create GMV Max ads for the TikTok Shop.<br><br>Các giá trị enum hỗ trợ: <ul><li>`EFFECTIVE`: The ad account is currently granted exclusive GMV Max authorization.</li><li>`INEFFECTIVE`: The ad account was granted exclusive GMV Max authorization but the authorization has been cancelled.</li><li>`UNAUTHORIZED`: The ad account has never been granted GMV Max exclusive authorization.</li></ul>|
#| advertiser_name | string | The name of the ad account.  <br><br><p><span style="color:darkred"><b>Note</b></span>: When `authorization_status` is `UNAUTHORIZED`, this field is not returned. |
#| advertiser_status | string | The status of the ad account.  <br><br> Các giá trị enum hỗ trợ: <ul><li>`STATUS_ENABLE`: Approved.</li><li>`STATUS_CONFIRM_FAIL`: Not approved.</li><li>`STATUS_PENDING_CONFIRM`: In review.</li><li>`STATUS_LIMIT`: Suspended.</li><li>`STATUS_CONTRACT_PENDING`: Contract has not taken effect.</li><li>`STATUS_DISABLE`: Disabled.</li><li>`STATUS_PENDING_CONFIRM_MODIFY`: Modifications pending review.</li><li>`STATUS_PENDING_VERIFIED`: Pending verification.</li><li>`STATUS_SELF_SERVICE_UNAUDITED`: Pending verification of qualifications for the self-service account.</li><li> `STATUS_WAIT_FOR_BPM_AUDIT`: Pending CRM system review.</li><li>`STATUS_CONFIRM_FAIL_END`: CRM system review failed.</li><li>`STATUS_CONFIRM_MODIFY_FAIL`: Review of modifications failed. </li></ul><br><p><span style="color:darkred"><b>Note</b></span>: When `authorization_status` is `UNAUTHORIZED`, this field is not returned. |
#| identity_id | string | Returned only when an official TikTok account is set for the TikTok Shop. <br><br> The ID of the identity associated with the official TikTok account for the TikTok Shop. |

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
        "advertiser_name": "{{advertiser_name}}",
        "advertiser_status": "STATUS_ENABLE",
        "authorization_status": "EFFECTIVE",
        "identity_id": "{{identity_id}}",
        "store_id": "{{store_id}}"
    }
}
```

---

<a id="doc-1822001200356354"></a>
<!-- doc_id: 1822001200356354 -->
<!-- doc_id: 1822001200356354 -->
# Grant an ad account exclusive authorization for a TikTok Shop
> Đường dẫn: API Reference > GMV Max > Grant an ad account exclusive authorization for a TikTok Shop
Dùng endpoint này để ủy quyền cho tài khoản quảng cáo tạo chiến dịch GMV Max cho một TikTok Shop cụ thể.

For each TikTok Shop, only one ad account can be authorized to create GMV Max Campaigns using the TikTok Shop for optimized revenue and sales campaigns. 

> **Important:** 
> By using the endpoint, you agree to and acknowledge the potential impacts listed in the [GMV Max Guidelines](https://ads.tiktok.com/help/article/gmv-max-guidelines). 

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/gmv_max/exclusive_authorization/create/

**Method** POST

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). ⏎ Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type  ****(Bắt buộc)**** | string | Định dạng dữ liệu yêu cầu. ⏎ Allowed format: `application/json`. |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
| store_id ***(Bắt buộc)*** | string | The ID of the TikTok Shop.<br><br> To obtain a TikTok Shop that is available for GMV Max Campaigns, use [/gmv_max/store/list/](45-gmv-max-p2.md#doc-1822001044479041) and confirm that the returned `is_gmv_max_available` is `true`. |
| store_authorized_bc_id ***(Bắt buộc)*** | string | ID of the Business Center that owns the TikTok Shop (`store_id`).<br><br>To confirm that a Business Center owns a TikTok Shop, use [/gmv_max/store/list/](45-gmv-max-p2.md#doc-1822001044479041) and check Liệu returned `is_owner_bc` for the ID in `store_authorized_bc_id` is `true`. |
| advertiser_id ***(Bắt buộc)*** | string | The ID of the ad account that you want to exclusively authorize to create GMV Max Campaigns for the TikTok Shop.<br><br>To obtain the list of ad accounts within a Business Center, use [/bc/asset/get/](15-bc-assets.md#doc-1739432717798401) and set `asset_type` to `ADVERTISER`. |

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location  --request POST 'https://business-api.tiktok.com/open_api/v1.3/gmv_max/exclusive_authorization/create/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "store_id": "{{store_id}}",
    "store_authorized_bc_id":"{{bc_id}}",
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

<a id="doc-1824721673497601"></a>
<!-- doc_id: 1824721673497601 -->
<!-- doc_id: 1824721673497601 -->
# Run a GMV Max Campaign report
> Đường dẫn: API Reference > GMV Max > Run a GMV Max Campaign report
Dùng endpoint này để chạy báo cáo cho chiến dịch GMV Max.

> **Note:** 
> By default, the response only includes undeleted campaigns.

## Rate limits
Giới hạn tốc độ của endpoint này thay đổi theo cấp giới hạn tốc độ của ứng dụng nhà phát triển. Tìm hiểu thêm về [rate limits](../04-get-started/bat-dau.md#doc-1740029171730433).

| Rate limit level | Query per second (QPS) | Query per minute (QPM) | Query per day (QPD） |
|---|---|---|---|
| Basic | 8 | 240 | 80,000 |
| Advanced | 12 | 360 | 120,000 |
| Premium | 20 | 600 | 200,000 |
| Ultimate | 20 | 600 | 200,000 |

## Điều kiện tiên quyết trước khi bắt đầu
Đảm bảo bạn có các quyền cần thiết tùy theo loại chiến dịch GMV Max và [the level of metrics](45-gmv-max-p3.md#doc-1824722485971009) bạn muốn truy cập. Xem các điều kiện tiên quyết của [Product GMV Max Campaigns](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1822009220448257) or [LIVE GMV Max Campaigns](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1822009242546258) để xác nhận quyền của bạn.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/gmv_max/report/get/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
| advertiser_id ***(Bắt buộc)*** | string | ID tài khoản quảng cáo TikTok. |
| store_ids ***(Bắt buộc)*** | string[] | A list of TikTok Shop IDs. <br><br>Kích thước tối đa: 1. <br><br>To obtain TikTok Shops that are available for GMV Max Campaigns, use [/gmv_max/store/list/](45-gmv-max-p2.md#doc-1822001044479041) and confirm that the returned `is_gmv_max_available` is `true`. |
| start_date ***(Bắt buộc)*** | string | Query start date (closed interval) in the format of `YYYY-MM-DD`. The date is based on the ad account time zone.<br><br>Example: `2025-01-01`. |
| end_date ***(Bắt buộc)*** | string | Query end date (closed interval) in the format of `YYYY-MM-DD`. The date is based on the ad account time zone. <br><br>Example: `2025-02-01`. <br><br><ul><li>If you don't include `stat_time_day` or `stat_time_hour` in the value of the dimensions field, the time range defined by `start_date` and `end_date` can be up to <b>365</b> days.</li><li> If you include `stat_time_day` in the value of the dimensions field to query daily breakdown data, the time range defined by `start_date` and `end_date` can be up to <b>30</b> days.</li><li>If you include `stat_time_hour` in the value of the dimensions field to query hourly breakdown data, the time range defined by `start_date` and `end_date` can be up to <b>one</b> day.</li></ul> |
| metrics ***(Bắt buộc)*** | string[] | Metrics to query.  <br><br>To learn about the different types of metrics that you can query for all GMV Max Campaigns, for Product GMV Max Campaigns, or for LIVE GMV Max Campaigns, see [Metrics in GMV Max Campaign reports](45-gmv-max-p3.md#doc-1824722485971009). |
| enable_total_metrics | boolean | Có thực hiện enable the total added-up data for your requested metrics. When `enable_total_metrics` is enabled, we will provide the aggregate data for all pages as you query different pages.<br><br>Các giá trị được hỗ trợ: `true`, `false`. <br>Giá trị mặc định: `false`. |
| dimensions ***(Bắt buộc)*** | string[] | Dimension groupings. <br><br>Các giá trị enum hỗ trợ: <ul><li>`advertiser_id`: Group by ID tài khoản quảng cáo TikTok.</li><li>`campaign_id`: Group by ID chiến dịch quảng cáo.</li><li>`stat_time_day`: Group by day.</li><li>`stat_time_hour`: Group by hour.</li><li>`item_group_id`: Group by SPU ID.</li><li>`item_id`: Group by post ID.</li><li>`room_id`: Group by room ID. </li><li>`duration`: Group by duration.</li></ul><br>For example, `&#91;"campaign_id", "stat_time_day"&#93;` indicates that both `campaign_id` and `stat_time_day` (days) are grouped. <br><br> The available dimension groupings vary based on the type of metrics that you want to query. To learn about the available dimension groupings for your desired metrics type, see [Metrics in GMV Max Campaign reports](45-gmv-max-p3.md#doc-1824722485971009). |
| filtering | object | Điều kiện lọc dữ liệu.<br><br> To learn about the available filters for your desired metrics type, see [Metrics in GMV Max Campaign reports](45-gmv-max-p3.md#doc-1824722485971009). |
#| gmv_max_promotion_types | string[] | Filter by the GMV Max Campaign type.<br><br>Các giá trị enum hỗ trợ: <ul><li>`PRODUCT`: Product GMV Max Campaign.</li><li>`LIVE`: LIVE GMV Max Campaign.</li></ul>
#| campaign_ids | string[] | Filter by a list of GMV Max Campaign IDs. <br><br>Kích thước tối đa: 100. |
#| campaign_name | string | Filter by a GMV Max Campaign name. <br><br>Fuzzy match is supported. |
#| campaign_statuses | string[] | Filter by campaign statuses. <br><br>Các giá trị enum hỗ trợ: <ul><li>`STATUS_DELIVERY_OK`: Active.</li><li>`STATUS_DISABLE`: Inactive. </li><li>`STATUS_DELETE`: Deleted.</li><li>`STATUS_NOT_DELIVERY`: Not delivering.</li><li>`STATUS_ALL`: All statuses.</li></ul> <br><p><span style="color:darkred"><b>Note</b></span>: By default, the response only includes undeleted campaigns.|
#| item_group_ids | string[] | Filter by a list of product SPU IDs. <br><br>Kích thước tối đa: 100. |
#| creative_types {-to-be-deprecated}| string[] | <ul><li>Bắt buộc khi you filter one SPU ID using `campaign_ids` and `item_group_ids`.</li><li>Not supported when you specify multiple IDs in the `campaign_ids` filter or `item_group_ids` filter or both, or specify multiple ID dimensions.</li></ul><br>Filter by creative types. <br><br>Các giá trị enum hỗ trợ: <ul><li> `ADS_AND_ORGANIC`: Ads and organic. This type contains all creatives that are authorized and in use for ads. The total gross revenue from videos in this type includes sales from both ads and organic videos.</li><li>`ORGANIC`: Organic only. This type contains videos that are used in organic traffic only. The total gross revenue from videos in this type includes sales from organic videos only. </li><li>`REMOVED`: Removed. This type contains automatically selected videos that have been manually removed from your campaign.</li></ul><br> Kích thước tối đa: 1. |
#|creative_delivery_statuses|string[]|<ul><li>You can only use this filter in any of the following scenarios: <ul><li>When you specify multiple IDs in the `campaign_ids` filter or `item_group_ids` filter or both</li><li>When you specify one ID in the `campaign_ids` filter or `item_group_ids` filter or both</li><li>When you specify multiple ID dimensions</li></ul></li><li>This filter cannot be used together with `creative_types`.</li></ul><br>Filter by creative statuses.<br><br>Các giá trị enum hỗ trợ: <ul><li>`IN_QUEUE`: In queue. Post is ready to be tested for its conversion-driving potential.</li><li>`LEARNING`: Learning. Post is being tested for its conversion-driving potential.</li><li>`DELIVERING`: Delivering. Post is being regularly promoted as part of your campaign.</li><li>`NOT_DELIVERYING`: Not delivering. Post didn't show strong conversion potential during testing and will not be regularly promoted as part of your campaign.</li><li>`AUTHORIZATION_NEEDED`: Authorization needed. This video hasn't been authorized for use in ads. You can authorize your own videos from your TikTok account or request authorization from other creators. This status will be updated here within 20 minutes of authorization.</li><li>`EXCLUDED`: Excluded. Post was manually removed and will not be regularly promoted as part of your campaign. You can add this post back to your campaign at any time.</li><li>`UNAVAILABLE`: Unavailable. Private videos, rejected videos, deleted videos, or videos from suspended TikTok accounts can't be used in ads. In some cases, you may observe cost from unavailable videos because videos that are rejected by TikTok’s content review process part-way through the campaign may still be delivered.</li><li>`REJECTED`: Rejected. The video has been rejected by the content moderation team. If you've appealed a rejection, the video status will be "rejected" until the appeal has been reviewed.</li><li>`NOT_ACTIVE`: Not active. This post has been deprioritized because it was uploaded more than 30 days ago and hasn't earned any gross revenue in the past 30 days.</li></ul> |
#| search_word | string | Filter by a search keyword, such as a video title, TikTok post ID, or TikTok account name. <br><br> Fuzzy match is supported. |
#| room_ids | string[] | Filter by a list of Livestream room IDs.<br><br> Kích thước tối đa: 100. |
| sort_field | string | Sorting field. <br><br>Not sorted by default. <br><br>We recommend using a sorting field to ensure the results are sorted in a logical order. To find the available fields, see <a href="#item-link-Supported sorting fields">Supported sorting fields</a>. |
| sort_type | string | Thứ tự sắp xếp kết quả. <br><br>Các giá trị enum hỗ trợ: `ASC`, `DESC`.<br> Giá trị mặc định: `DESC`. |
| page | integer | Current Số trang cần lấy dữ liệu. <br><br>Value range: ≥1. <br>Giá trị mặc định: 1. |
| page_size | integer | Page size. <br><br>Value range: 1-1,000.<br> Giá trị mặc định: 10. |
### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request GET https://business-api.tiktok.com/open_api/v1.3/gmv_max/report/get/?advertiser_id={{advertiser_id}}&store_ids=["{{store_id}}"]&start_date=2025-07-03&end_date=2025-07-03&metrics=["creative_delivery_status","cost","orders","cost_per_order","gross_revenue","roi","product_impressions","product_clicks","product_click_rate","ad_click_rate","ad_conversion_rate","ad_video_view_rate_2s","ad_video_view_rate_6s","ad_video_view_rate_p25","ad_video_view_rate_p50","ad_video_view_rate_p75","ad_video_view_rate_p100"]&dimensions=["item_id"]&filtering={"campaign_ids":["{{campaign_id}}"],"item_group_ids":["{{item_group_id_1}}","{{item_group_id_2}}"]}&page=1&page_size=1000
--header 'Access-Token: {{Access-Token}}'
```

### Supported sorting fields
Các bảng sau liệt kê riêng các trường sắp xếp khả dụng cho chiến dịch Product GMV Max và LIVE GMV Max.

#### For Product GMV Max Campaigns
|Field|Description|
|---|---|
| cost | Cost |
| net_cost | Net cost |
| orders | Orders (SKU) |
| cost_per_order | Cost per order |
| gross_revenue | Gross revenue |
| roi | ROI |
| product_impressions | Product ad impressions |
| product_clicks | Product ad clicks |
| product_click_rate | Product ad click rate |
| ad_click_rate | Ad click rate |
| ad_conversion_rate | Ad conversion rate |
| ad_video_view_rate_2s | 2-second ad video view rate |
| ad_video_view_rate_6s | 6-second ad video view rate |
| ad_video_view_rate_p25 | 25% ad video view rate |
| ad_video_view_rate_p50 | 50% ad video view rate |
| ad_video_view_rate_p75 | 75% ad video view rate |
| ad_video_view_rate_p100 | 100% ad video view rate |

#### For LIVE GMV Max Campaigns

|Field|Description|
|---|---|
| cost | Cost |
| net_cost | Net cost |
| orders | Orders |
| cost_per_order | Cost per order |
| gross_revenue | Gross revenue |
| roi | ROI |
| live_views | LIVE views |
| cost_per_live_view | Cost per LIVE view |
| 10_second_live_views | 10-second LIVE views |
| cost_per_10_second_live_view | Cost per 10-second LIVE view |
| live_follows | LIVE follows |

### Ví dụ lệnh cURL (Example)
Để xem các ví dụ mã đầy đủ về chạy báo cáo chiến dịch GMV Max, xem [Metrics in GMV Max Campaign reports](45-gmv-max-p3.md#doc-1824722485971009).

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|code |number|Response code. For the complete list of response codes and descriptions, see [Appendix-Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message|string|Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|request_id |string|The log ID of a request, which uniquely identifies the request.  |
|data |object|Returned data.|
#| total_metrics | object | Returned only when `enable_total_metrics` is set to `true` in the request. <br><br>The total added-up data for your requested metrics. |
##| &#123;metric_name&#125; | string | Returned metrics, which are determined by the `metrics` field specified in your request. |
#| list | object[] | Data list. |
##| dimensions | object | All requested dimension data. |
###| &#123;dimension_name&#125;  | string | Returned dimensions, which are determined by the `dimensions` field specified in your request. |
##| metrics | object | All requested metric data. |
###| &#123;metric_name&#125;  | string | Returned metrics, which are determined by the `metrics` field specified in your request. |
#| page_info | object | Pagination information. |
##| page | integer | Current Số trang cần lấy dữ liệu. |
##| page_size| integer | Page size. |
##| total_number | integer | Tổng số kết quả tìm thấy. |
##| total_page| integer | Total pages of results. |

### Ví dụ lệnh cURL (Example)
```xcodeblock 
(code Success-Response http)
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "list": [
            {
                "dimensions": {
                    "item_id": "{{item_id}}"
                },
                "metrics": {
                    "ad_click_rate": "16.67",
                    "ad_conversion_rate": "0.00",
                    "ad_video_view_rate_2s": "40.00",
                    "ad_video_view_rate_6s": "40.00",
                    "ad_video_view_rate_p100": "20.00",
                    "ad_video_view_rate_p25": "40.00",
                    "ad_video_view_rate_p50": "20.00",
                    "ad_video_view_rate_p75": "20.00",
                    "cost": "0.01",
                    "cost_per_order": "0.00",
                    "creative_delivery_status": "UNAVAILABLE",
                    "currency": "USD",
                    "gross_revenue": "0.00",
                    "orders": "0",
                    "product_click_rate": "16.67",
                    "product_clicks": "1",
                    "product_impressions": "6",
                    "roi": "0.00"
                }
            },
            {
                "dimensions": {
                    "item_id": "{{item_id}}"
                },
                "metrics": {
                    "ad_click_rate": "0.00",
                    "ad_conversion_rate": "0.00",
                    "ad_video_view_rate_2s": "0.00",
                    "ad_video_view_rate_6s": "0.00",
                    "ad_video_view_rate_p100": "0.00",
                    "ad_video_view_rate_p25": "0.00",
                    "ad_video_view_rate_p50": "0.00",
                    "ad_video_view_rate_p75": "0.00",
                    "cost": "0.00",
                    "cost_per_order": "0.00",
                    "creative_delivery_status": "UNAVAILABLE",
                    "currency": "USD",
                    "gross_revenue": "0.00",
                    "orders": "0",
                    "product_click_rate": "0.00",
                    "product_clicks": "0",
                    "product_impressions": "0",
                    "roi": "0.00"
                }
            }
        ],
        "page_info": {
            "page": 1,
            "page_size": 1000,
            "total_number": 246,
            "total_page": 1
        }
    }
}
(/code)
```
---

## Hướng dẫn thực hành Data Retrieval (Python & cURL)

Dưới đây là mã nguồn mẫu minh họa quy trình gọi API thực tế cho phân hệ **GMV Max — phần 2/3**:

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

