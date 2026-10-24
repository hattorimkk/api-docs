# Mẫu video Catalog

> Phân hệ: apiref:Catalog Video Templates.
> Tài liệu biên dịch kỹ thuật chi tiết theo chuẩn TikTok Business API v1.3.

---

## Mục lục điều hướng
- [1. Catalog Video Templates (#doc-1740132982369282)](#doc-1740132982369282)
- [2. Get video packages (#doc-1740574099715073)](#doc-1740574099715073)
- [3. (Deprecated) Create a video package (#doc-1740665273039873)](#doc-1740665273039873)
- [4. (Deprecated) Update the name of a video package (#doc-1740665303669761)](#doc-1740665303669761)
- [5. (Deprecated) Delete a video package (#doc-1740665332455426)](#doc-1740665332455426)
- [6. (Deprecated) Upload a video template (#doc-1740665346584577)](#doc-1740665346584577)
- [7. (Deprecated) Preview video templates (#doc-1740665368159233)](#doc-1740665368159233)

---

<a id="doc-1740132982369282"></a>
<!-- doc_id: 1740132982369282 -->
<!-- doc_id: 1740132982369282 -->
# Catalog Video Templates
> Đường dẫn: API Reference > Catalog Video Templates
> **Important:** By using Catalog API endpoints, you agree to the [Product Catalog Terms](https://ads.tiktok.com/i18n/official/article?aid=6765817026859499525) and certify that you are abiding by the [TikTok Advertising Policies](https://ads.tiktok.com/help/article?aid=6685586866860720134). Please review these policies and ensure that the items you upload to your catalog don't breach them.

A catalog is an asset that allows you to store information about the products you want to promote on TikTok. Using a catalog is a great solution for anyone who is looking for an efficient way to create and manage ads that feature a variety of products, like an online retailer. Catalog Video Templates API enables you to retrieve catalog video packages in your Business Center.

This group consists of the following endpoints:
- [Get video packages](31-catalog-video-templates.md#doc-1740574099715073)

---

<a id="doc-1740574099715073"></a>
<!-- doc_id: 1740574099715073 -->
<!-- doc_id: 1740574099715073 -->
# Get video packages
> Đường dẫn: API Reference > Catalog Video Templates > Get video packages
Sử dụng endpoint này để lấy thông tin information about all catalog video packages, or a particular video package, under your Business Center. 

## Yêu cầu gọi API (Request)

**Endpoint** 
https://business-api.tiktok.com/open_api/v1.3/catalog/video_package/get/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|Access-Token ***(Bắt buộc)***|string|Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
| bc_id ***(Bắt buộc)*** | string | ID Business Center (BC ID). |
| catalog_id  ***(Bắt buộc)*** | string | ID danh mục sản phẩm. |
| shopping_ads_video_package_id|string|Catalog video package ID. |

### Ví dụ lệnh cURL (Example)

```http
// curl
curl -X GET -H "Access-Token:YOUR_ACCESS_TOKEN" \
--data-urlencode "bc_id=BC_ID" \
--data-urlencode "catalog_id=CATALOG_ID" \
--data-urlencode "shopping_ads_video_package_id=VIDEO_ID" \

https://business-api.tiktok.com/open_api/v1.3/catalog/video_package/get/
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Mã trạng thái phản hồi (0: Thành công), see [Appendix - Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông điệp phản hồi từ máy chủ, see [Appendix-Thông điệp phản hồi từ máy chủ](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | The log id of a request, which uniquely identifies the request. |
| data | object [] | Returned data. |
| ↳ shopping_ads_video_package_id | string | Catalog video package ID. |
| ↳ catalog_id | string | ID danh mục sản phẩm. |
| ↳ video_package_name | string | Catalog video package name. |
| ↳ create_time | string | Thời gian tạo. |
| ↳ update_time | string | Thời gian cập nhật gần nhất. |
| ↳ status | string | If the video package is available for use. Các giá trị enum hỗ trợ: `AVAILABLE`, `UNAVAILABLE`. |
| ↳ video_package_type | string | Video package type. Các giá trị enum hỗ trợ: `GREEN_SCREEN`, `TEMPLATE`, `DVG`. |
| ↳ audit | object | Audit information. |
| ↳↳ audit_status | string | Audit status. Các giá trị enum hỗ trợ: `PROCESSING`, `APPROVED`, `REJECTED`. |
| ↳↳ reject_info | object[] | Rejection information. Returned only when `audit_status` is `REJECTED`. |
| ↳↳↳ rejected_object | string | Object that was rejected. |
| ↳↳↳ reason | string | Reason for the rejection. |

### Ví dụ lệnh cURL (Example)

```http
// Success-Response
HTTPS/1.1 200 OK
{
    "message": "OK",
    "code": 0,
    "data": {
        "list": [
            {
                "audit": {
                    "audit_status": "PROCESSING"
                },
                "status": "AVAILABLE",
                "update_time": "2021-08-10 09:53:59",
                "video_package_name": "green screen generation",
                "shopping_ads_video_package_id": "21f62362-6afe-4d89-a83e-0f9713833dfa",
                "video_package_type": "GREEN_SCREEN",
                "create_time": "2021-08-10 09:42:09",
                "catalog_id": "6986901069595002626"
            },
            {
                "audit": {
                    "audit_status": "PROCESSING"
                },
                "status": "UNAVAILABLE",
                "update_time": "2021-08-06 09:00:43",
                "video_package_name": "GreenScreen_20210806_09:00",
                "shopping_ads_video_package_id": "25071f29-5d25-4ebe-8a50-f282e0847a87",
                "video_package_type": "GREEN_SCREEN",
                "create_time": "2021-08-06 09:00:43",
                "catalog_id": "6986901069595002626"
            },
            {
                "audit": {
                    "audit_status": "REJECTED",
                    "reject_info": [
                        {
                            "rejected_object": "Creative Video",
                            "reason": "The ad or video has no background audio or the background audio is incoherent/unclear."
                        }
                    ]
                },
                "status": "AVAILABLE",
                "update_time": "2021-08-07 00:42:06",
                "video_package_name": "GreenScreen_20210806_08:59",
                "shopping_ads_video_package_id": "ec23aa27-1ddf-497a-9777-05de58b1cc40",
                "video_package_type": "GREEN_SCREEN",
                "create_time": "2021-08-06 08:59:41",
                "catalog_id": "6986901069595002626"
            },
            ...
        ]
    },
    "request_id": "2021081012162001024506219218036157"
}
```

---

<a id="doc-1740665273039873"></a>
<!-- doc_id: 1740665273039873 -->
<!-- doc_id: 1740665273039873 -->
# (Deprecated) Create a video package
> Đường dẫn: API Reference > Catalog Video Templates > (Deprecated) Create a video package
Sử dụng endpoint này để tạo a video package.

## Yêu cầu gọi API (Request)

**Endpoint** `https://business-api.tiktok.com/open_api/v1.3/catalog/video_package/create/`

**Method** POST

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type  ****(Bắt buộc)**** | string | Request content type. ⏎ Allowed format: `"application/json"`. |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| bc_id  ****(Bắt buộc)**** | string | ID Business Center (BC ID). |
| catalog_id  ****(Bắt buộc)**** | string | ID danh mục sản phẩm. |
| video_package_type  ****(Bắt buộc)**** | string | Video package type. Currently, only `GREEN_SCREEEN` is supported. |
| videos {+conditional} | object[] | List of videos that will be used to create the video pakcage. This field is Bắt buộc khi `video_package_type` is `GREEEN_SCREEN`. |
| ↳ video_id {+conditional} | string | Video ID. This field is Bắt buộc khi `video_package_type` is `GREEEN_SCREEN`. |
| ↳ is_green_screen_video {+conditional} | boolean | Liệu this is a green screen video. In the list of videos, you need to and can only have one green screen video. This field is Bắt buộc khi `video_package_type` is `GREEEN_SCREEN`. |
| music_id {+conditional} | string | Music ID. This field is Bắt buộc khi `video_package_type` is `GREEEN_SCREEN`. |
| template_id {+conditional} | string | Template ID. This field is Bắt buộc khi when `video_package_type` is `GREEEN_SCREEN` |
| video_package_name | string | Name of the video package that you are about to create. If not specified, a name will be automatically generated in the format of `[VIDEO_TYPE]_[CREATE_TIME]`. For example, GreenScreenVideo_20210720_17:20. UTC+0 time will be used in generating video package names. |

### Ví dụ lệnh cURL (Example)

```cURL
// cURL
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/catalog/video_package/create/' \
--header 'Access-Token: xxxx \
--header 'Content-Type: application/json' \
--data-raw '{
    "bc_id": 6725320885500118022,
    "catalog_id": 6986901069595002626,
    "video_package_type": "GREEN_SCREEN",
    "videos": [
        {"video_id": "v07033g50000c38pjfoupb082t6ln5f0", "is_green_screen_video": false},
        {"video_id": "v10033g50000c4574b3c77uaa2tq5100", "is_green_screen_video": true},
        {"video_id": "v07033g50000c23ptb2h6o7cqvaadut0", "is_green_screen_video": false}  
    ],
    "template_id": "6992826957676134402",
    "video_package_name": "green screen generation",
    "music_id": "6904951200983285762"
}'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Response code. For the complete list of response codes and descriptions, see [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | The log id of a request, which uniquely identifies the request. |
| data | object | Returned data. |
| ↳ shopping_ads_video_package_id | string | ID of the video package that has just been created. |

### Ví dụ lệnh cURL (Example)
```JSON
// JSON
{
    "code": 0,
    "message": "OK",
    "request_id": "20210810121500010244053018340BC3B3",
    "data": {
        "shopping_ads_video_package_id": "4c703748-e408-4364-9798-44970f85be23"
    }
}
```

---

<a id="doc-1740665303669761"></a>
<!-- doc_id: 1740665303669761 -->
<!-- doc_id: 1740665303669761 -->
# (Deprecated) Update the name of a video package
> Đường dẫn: API Reference > Catalog Video Templates > (Deprecated) Update the name of a video package
Sử dụng endpoint này để cập nhật name of a video package.

## Yêu cầu gọi API (Request)

**Endpoint** `https://business-api.tiktok.com/open_api/v1.3/catalog/video_package/update/`

**Method** POST

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type  ****(Bắt buộc)**** | string | Request content type. Allowed format: `"application/json"` |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| bc_id  ****(Bắt buộc)**** | string | ID Business Center (BC ID). |
| catalog_id  ****(Bắt buộc)**** | string | ID danh mục sản phẩm. |
| shopping_ads_video_package_id  ****(Bắt buộc)**** | string | ID of the video package that you want to update. |
| video_package_name  ****(Bắt buộc)**** | string | Video package name. |

### Ví dụ lệnh cURL (Example)
```cURL
// cURL
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/catalog/video_package/update/' \
--header 'Access-Token: xxxx \
--header 'Content-Type: application/json' \
--data-raw '{
    "bc_id": 6725320885500118022,
    "catalog_id": 6986901069595002626,
    "shopping_ads_video_package_id": "651a86bc-580e-4f7f-85f6-35394af01a45",
    "video_package_name": "green screen rename template video 1"
}'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Response code. For the complete list of response codes and descriptions, see [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | The log id of a request, which uniquely identifies the request. |

### Ví dụ lệnh cURL (Example)

```JSON
// JSON
{
    "code": 0,
    "message": "OK",
    "request_id": "202108101227520102450631992F007842",
    "data": {}
}
```

---

<a id="doc-1740665332455426"></a>
<!-- doc_id: 1740665332455426 -->
<!-- doc_id: 1740665332455426 -->
# (Deprecated) Delete a video package
> Đường dẫn: API Reference > Catalog Video Templates > (Deprecated) Delete a video package
Sử dụng endpoint này để xóa a video package.

## Yêu cầu gọi API (Request)

**Endpoint** `https://business-api.tiktok.com/open_api/v1.3/catalog/video_package/delete/`

**Method** POST

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type  ****(Bắt buộc)**** | string | Request content type. ⏎ Allowed format: `"application/json"`. |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| bc_id  ****(Bắt buộc)**** | string | ID Business Center (BC ID). |
| catalog_id  ****(Bắt buộc)**** | string | ID danh mục sản phẩm. |
| shopping_ads_video_package_id  ****(Bắt buộc)**** | string | ID of the video package that you want to update. |

### Ví dụ lệnh cURL (Example)

```cURL
// cURL
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.2/catalog/video_package/delete/' \
--header 'Access-Token: xxxx \
--header 'Content-Type: application/json' \
--data-raw '{
    "bc_id": 6725320885500118022,
    "catalog_id": 6986901069595002626,
    "shopping_ads_video_package_id": "491e6b86-c5b4-441c-a390-365c47d29cfd"
}'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Response code. For the complete list of response codes and descriptions, see [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | The log id of a request, which uniquely identifies the request. |

### Ví dụ lệnh cURL (Example)

```JSON
// JSON
{
    "code": 0,
    "message": "OK",
    "request_id": "202108101230590102450160272100ABE0",
    "data": {}
}
```

---

<a id="doc-1740665346584577"></a>
<!-- doc_id: 1740665346584577 -->
<!-- doc_id: 1740665346584577 -->
# (Deprecated) Upload a video template
> Đường dẫn: API Reference > Catalog Video Templates > (Deprecated) Upload a video template
Sử dụng endpoint này để tải lên một custom video template to Busines Center and associate the template with a group of catalogs. 

To learn about how to design a custom video template, refer to [Custom Template Design Guidelines](https://bytedance.feishu.cn/docs/doccnGxGlxEVZVhvGWyq17QTKNe). In addition, in a custom video template, the image layers and text layers need to be named in formats that are supported by TikTok. Để biết chi tiết, xem [Layer Naming Guidelines](../09-marketing-api/catalog.md#doc-1739470990574594).

## Yêu cầu gọi API (Request)

**Endpoint** `https://business-api.tiktok.com/open_api/v1.3/catalog/template/upload/`

**Method** POST

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type  ****(Bắt buộc)**** | string | Định dạng dữ liệu yêu cầu ⏎ Allowed format: `multipart/form-data`. |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| bc_id  ****(Bắt buộc)**** | string | ID Business Center (BC ID). |
| catalog_ids  ****(Bắt buộc)**** | string[] | List of catalog IDs that you want to associate this catalog with. |
| file  ****(Bắt buộc)**** | file | Template file in ZIP. |

### Ví dụ lệnh cURL (Example)

```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/catalog/template/upload/' \
--header 'access-token: abcd' \
--form 'bc_id="abcd"' \
--form 'catalog_ids="[1234567890]"' \
--form 'file=@"/Users/admin/Downloads/Example.zip"'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | The response code. For the complete list of response codes and descriptions, see [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | The response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| template_id | string | Template ID. |
| catalog_upload_success | number[] | List of catalog IDs that have been successfully associated with this template. |
| request_id | string | The log id of a request, which uniquely identifies the request. |

---

<a id="doc-1740665368159233"></a>
<!-- doc_id: 1740665368159233 -->
<!-- doc_id: 1740665368159233 -->
# (Deprecated) Preview video templates
> Đường dẫn: API Reference > Catalog Video Templates > (Deprecated) Preview video templates
Use this endpoint to preview video templates.

An iframe code snippet with a link will be returned in the response. You can either click the link or embed the iframe code snippet in an HTML file. 

## Yêu cầu gọi API (Request)

**Endpoint** `https://business-api.tiktok.com/open_api/v1.3/catalog/template_preview/create/`

**Method** POST

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type  ****(Bắt buộc)**** | string | Định dạng dữ liệu yêu cầu. Allowed format: `"application/json"` |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| bc_id  ****(Bắt buộc)**** | string | ID Business Center (BC ID). |
| catalog_ids  ****(Bắt buộc)**** | string[] | Catalog IDs. |

### Ví dụ lệnh cURL (Example)
```cURL
// cURL
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/catalog/template_preview/create/' \
--header 'Access-Token: xxxx \
--header 'Content-Type: application/json' \
--data-raw '{
    "bc_id": "6725320885500118022",
    "catalog_ids": ["6986901069595002626"]
}'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Response code. For the complete list of response codes and descriptions, see [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| data | object | Returned data. |
| ↳ iframe | string | An iframe code snippet that includes the preview link. Click the link to preview the video or embed the iframe code to your HTML file. |
| request_id | string | The log id of a request, which uniquely identifies the request. |

### Ví dụ lệnh cURL (Example)

```JSON
// JSON
{
    "code": 0,
    "message": "OK",
    "request_id": "20210810121217010245016027560AC221",
    "data": {
        "iframe": "<iframe src=\"https://ads.tiktok.com/ad_preview_tool?ad_preview_id=34db6ab0f9d411eb89bb6b94305dff44\"></iframe>"
    }
}
```
---

## Hướng dẫn thực hành Data Retrieval (Python & cURL)

Dưới đây là mã nguồn mẫu minh họa quy trình gọi API thực tế cho phân hệ **Mẫu video Catalog**:

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

