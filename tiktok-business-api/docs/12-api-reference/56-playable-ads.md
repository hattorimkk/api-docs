# Quảng cáo Playable (Playable Ads)

> Phân hệ: apiref:Playable Ads.
> Tài liệu biên dịch kỹ thuật chi tiết theo chuẩn TikTok Business API v1.3.

---

## Mục lục điều hướng
- [1. Playable Ads (#doc-1737730803189826)](#doc-1737730803189826)
- [2. Upload a playable asset (#doc-1737730926765057)](#doc-1737730926765057)
- [3. Check the status of a playable asset (#doc-1737732054892545)](#doc-1737732054892545)
- [4. Save a playable asset (#doc-1737732203851777)](#doc-1737732203851777)
- [5. Get playable assets (#doc-1737732758495234)](#doc-1737732758495234)
- [6. Delete a playable asset (#doc-1737733368940546)](#doc-1737733368940546)

---

<a id="doc-1737730803189826"></a>
<!-- doc_id: 1737730803189826 -->
<!-- doc_id: 1737730803189826 -->
# Playable Ads
> Đường dẫn: API Reference > Playable Ads
Playable Ad is an interactive ad format that provides a short, engaging experience attracting users and getting them to download your app or game. With playable ads, users experience an app or game before they decide to download. This ad format is an effective way to optimize cost per impression (CPM) by gamifying your ad and getting the most out of each impression.

To learn about the benefits of and design best practices for Playable Ads, see [Playble Ads](https://ads.tiktok.com/help/article/playable-ads).

To learn about how to upload playables for ad creation, see [Upload playables](../09-marketing-api/creatives.md#doc-1868153086739601).

This group consists of the following endpoints:
* [Upload a playable asset](56-playable-ads.md#doc-1737730926765057)
* [Check the status of a playable asset](56-playable-ads.md#doc-1737732054892545)
* [Save a playable asset](56-playable-ads.md#doc-1737732203851777)
* [Get playable assets](56-playable-ads.md#doc-1737732758495234)
* [Delete a playable asset](56-playable-ads.md#doc-1737733368940546)

---

<a id="doc-1737730926765057"></a>
<!-- doc_id: 1737730926765057 -->
<!-- doc_id: 1737730926765057 -->
# Upload a playable asset
> Đường dẫn: API Reference > Playable Ads > Upload a playable asset
Sử dụng endpoint này để tải lên một playable asset.

## Yêu cầu gọi API (Request)

**Endpoint**
https://business-api.tiktok.com/open_api/v1.3/playable/upload/

**Method** POST

**Header**
| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token ***(Bắt buộc)*** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162).|
| Content-Type ***(Bắt buộc)*** | string | Định dạng dữ liệu yêu cầu <br> Allowable value:`"multipart/form-data"` |
**Parameters**
| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id ***(Bắt buộc)*** | string | ID tài khoản quảng cáo TikTok. |
| upload_type | string | The way you upload your playable assets. <br><br>Các giá trị enum hỗ trợ: `UPLOAD_BY_FILE`, `UPLOAD_BY_FILE_ID`.<br>Giá trị mặc định: `UPLOAD_BY_FILE`. |
| playable_package **(Điều kiện)** | file |Bắt buộc khi `upload_type` is `UPLOAD_BY_FILE`.<br><br> The playable asset file. <br><br> Specification requirements:<br> 1. The format is ZIP, and the size is no more than 5 MB. <br> 2. Playable JS-SDK has been accessed, and the calling method is `window.openAppStore();`<br> 3. The main HTML file needs to be named `index.html` and located in the primary directory. <br> 4. The `playable_orientation` field should be stored in the `config.json` file and located in the first directory, with a value of 0 (`BOTH`), 1 (`PORTRAIT`), or 2 (`LANDSCAPE`). Example: `&#123; "playable_orientation": 0, &#125;`.<br> 5. File names only support uppercase and lowercase letters, numbers, minus signs and underscores. <br> 6. The `mraid.js` format is not allowed in the file. <br>7. The file is not allowed to load dynamic material over an external network. <br> 8. JS redirection is not allowed in the file. <br>9. The file does not allow an HTTP request. <br> 10. A file with empty content is not allowed. |
|file_id**(Điều kiện)**| string | Bắt buộc khi `upload_type` is `UPLOAD_BY_FILE_ID`.<br><br>The `file_id` of the file that you want to upload. This field is for files that are uploaded to the file repository. <br>You can get `file_id` via the [Files](44-files.md#doc-1737719988918274) endpoints. |
### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/playable/upload/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: multipart/form-data' \
--form 'advertiser_id="{{advertiser_id}}"' \
--form 'upload_type="UPLOAD_BY_FILE"' \
--form 'playable_package=@"{{playable_package}}"'
```

## Dữ liệu phản hồi (Response)
| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|code |number|Mã trạng thái phản hồi (0: Thành công). For the complete list of response codes and descriptions, see [Appendix-Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097).  |
|message |string|Thông điệp phản hồi từ máy chủ. Để biết chi tiết, xem [Appendix-Return information](../15-appendix/phu-luc-p1.md#doc-1737172488964097).  |
| request_id | string | The log id of a request, which uniquely identifies the request.|
|data |object|Returned data|
#| playable_id | string | Playable asset ID. |
### Ví dụ lệnh cURL (Example)
``` xcodeblock
(code Success-Response http)
HTTPS / 1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "playable_id": "{{playable_id}}"
    }
}
(/code);
```

---

<a id="doc-1737732054892545"></a>
<!-- doc_id: 1737732054892545 -->
<!-- doc_id: 1737732054892545 -->
# Check the status of a playable asset
> Đường dẫn: API Reference > Playable Ads > Check the status of a playable asset
Sử dụng endpoint này để kiểm tra the validation and audit status of the uploaded playable asset.

## Yêu cầu gọi API (Request)
**Endpoint** https://business-api.tiktok.com/open_api/v1.3/playable/validate/

**Method** GET

**Header**
| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token ***(Bắt buộc)*** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162).|
**Parameters**
| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id ***(Bắt buộc)*** | string | ID tài khoản quảng cáo TikTok. |
| playable_id ***(Bắt buộc)*** | string | Playable asset ID. |

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/playable/validate/?advertiser_id={{advertiser_id}}&playable_id={{playable_id}}' \
--header 'Access-Token: {{Access-Token}}'
```

## Dữ liệu phản hồi (Response)
| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|code |number|Mã trạng thái phản hồi (0: Thành công). For the complete list of response codes and descriptions, see [Appendix-Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097).  |
|message |string|Thông điệp phản hồi từ máy chủ. Để biết chi tiết, xem [Appendix-Return information](../15-appendix/phu-luc-p1.md#doc-1737172488964097).  |
| request_id | string | The log id of a request, which uniquely identifies the request.|
|data |object|Returned data|
# | playable_id | string | Playable asset ID. |
# | playable_url | string | Playable asset URL. |
# | playable_orientation | string | Playable asset orientation.<br><br>Các giá trị enum hỗ trợ: <ul><li>`BOTH`: vertical or horizontal.</li><li>`LANDSCAPE`: horizontal.</li><li>`PORTRAIT`: vertical.</li></ul> |
# | status | string | Playable asset status. <br><br>Các giá trị enum hỗ trợ: `AUDIT_FAIL`,`AUDIT_SUCCESS`, `VALIDATE_FAIL`, `VALIDATE_SUCCESS`,`VALIDATING`. |
# | fail_message | string | An error message indicating the cause of failure. |

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "playable_id": "{{playable_id}}",
        "playable_orientation": "BOTH",
        "playable_url": "{{playable_url}}",
        "status": "VALIDATE_SUCCESS"
    }
}
```

---

<a id="doc-1737732203851777"></a>
<!-- doc_id: 1737732203851777 -->
<!-- doc_id: 1737732203851777 -->
# Save a playable asset
> Đường dẫn: API Reference > Playable Ads > Save a playable asset
Use this endpoint to save a playable asset.

## Yêu cầu gọi API (Request)
**Endpoint** https://business-api.tiktok.com/open_api/v1.3/playable/save/

**Method** POST

**Header**
| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token ***(Bắt buộc)*** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162).|
| Content-Type ***(Bắt buộc)*** | string | Định dạng dữ liệu yêu cầu <br> Allowable value: `application/json` |
**Parameters**
| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id {required} | string | ID tài khoản quảng cáo TikTok. |
| playable_id {required} | string | Playable asset ID. |
| playable_name {required} | string | Playable asset name. |

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/playable/save/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id": "{{advertiser_id}}",
    "playable_id": "{{playable_id}}",
    "playable_name": "{{playable_name}}"
}'
```

## Dữ liệu phản hồi (Response)
| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|code |number|Mã trạng thái phản hồi (0: Thành công). For the complete list of response codes and descriptions, see [Appendix-Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097).  |
|message |string|Thông điệp phản hồi từ máy chủ. Để biết chi tiết, xem [Appendix-Return information](../15-appendix/phu-luc-p1.md#doc-1737172488964097).  |
| request_id | string | The log id of a request, which uniquely identifies the request. |
|data |object|Returned data.|
#| playable_id | string | Playable asset ID. |
#| playable_url | string | Playable URL. |
#| playable_name | string | Playable asset name. |
#| playable_orientation | string | Playable asset orientation.<br><br>Các giá trị enum hỗ trợ: <ul><li>`BOTH`: vertical or horizontal.</li><li>`LANDSCAPE`: horizontal.</li><li>`PORTRAIT`: vertical.</li></ul>|
#| status | string | Playable asset status. <br><br>Các giá trị enum hỗ trợ: `AUDIT_FAIL`,`AUDIT_SUCCESS`, `VALIDATE_FAIL`, `VALIDATE_SUCCESS`, `VALIDATING`. |

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "playable_id": "{{playable_id}}",
        "playable_name": "{{playable_name}}",
        "playable_orientation": "BOTH",
        "playable_url": "{{playable_url}}",
        "status": "VALIDATE_SUCCESS"
    }
}
```

---

<a id="doc-1737732758495234"></a>
<!-- doc_id: 1737732758495234 -->
<!-- doc_id: 1737732758495234 -->
# Get playable assets
> Đường dẫn: API Reference > Playable Ads > Get playable assets
Sử dụng endpoint này để lấy thông tin a list of playable assets.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/playable/get/

**Method** GET

**Header**
| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token ***(Bắt buộc)*** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162).|
**Parameters**
| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id {required} | string | ID tài khoản quảng cáo TikTok. |
|playable_id|string|Playable asset ID to filter the results by.|
|playable_name|string|Playable asset name to filter the results by.|
|playable_url|string|Playable URL.|
|status|string|Playable asset status .<br><br>Các giá trị enum hỗ trợ: `AUDIT_FAIL`, `AUDIT_SUCCESS`,`VALIDATE_FAIL`,`VALIDATE_SUCCESS`,`VALIDATING`.|
|operation_status|string|Playable asset Trạng thái hoạt động.<br><br>Các giá trị enum hỗ trợ: `UPLOADED`,`SAVED`,`DELETED`.<br>Giá trị mặc định: `SAVED`.|
|page|number|Current number of pages.<br><br> Value range: ≥ 1.<br> Giá trị mặc định: 1.|
|page_size|number|Page size. <br><br>Value range: 1-100.<br>Giá trị mặc định: 10. |

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/playable/get/?advertiser_id={{advertiser_id}}&page=1&page_size=100' \
--header 'Access-Token: {{Access-Token}}'
```

## Dữ liệu phản hồi (Response)
| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|code |number|Mã trạng thái phản hồi (0: Thành công). For the complete list of response codes and descriptions, see [Appendix-Return codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).  |
|message |string|Thông điệp phản hồi từ máy chủ. Để biết chi tiết, xem [Appendix-Return codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).  |
| request_id | string |The log id of a request, which uniquely identifies the request.|
|data |object|Returned data.|
#|list|object []|Playable asset list.|
##|advertiser_id|string|ID tài khoản quảng cáo TikTok.|
##|playable_id|string|Playable asset ID.|
##|playable_url|string|Playable URL.|
##|playable_name|string|Playable asset name.|
##|playable_orientation|string|Playable asset orientation .<br><br>Các giá trị enum hỗ trợ: <ul><li>`BOTH`: vertical or horizontal.</li><li>`LANDSCAPE`: horizontal.</li><li>`PORTRAIT`: vertical.</li></ul>|
##|status|string|Playable asset status.<br><br>Các giá trị enum hỗ trợ: `AUDIT_FAIL`,`AUDIT_SUCCESS`, `VALIDATE_FAIL`, `VALIDATE_SUCCESS`,`VALIDATING`.|
##|operation_status|string|Playable asset Trạng thái hoạt động.<br><br>Các giá trị enum hỗ trợ: `UPLOADED`,`SAVED`,`DELETED`.|
#|page_info |object | Pagination information. |
##|page |number | Current Số trang cần lấy dữ liệu. |
##|page_size |number | Page size. |
##|total_number |number | Tổng số kết quả tìm thấy. |
##|total_page |number |Total pages of results. |
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
                "advertiser_id": "{{advertiser_id}}",
                "operation_status": "SAVED",
                "playable_id": "{{playable_id}}",
                "playable_name": "{{playable_name}}",
                "playable_orientation": "BOTH",
                "playable_url": "{{playable_url}}",
                "status": "VALIDATE_SUCCESS"
            }
        ],
        "page_info": {
            "page": 1,
            "page_size": 100,
            "total_number": 1,
            "total_page": 1
        }
    }
}
```

---

<a id="doc-1737733368940546"></a>
<!-- doc_id: 1737733368940546 -->
<!-- doc_id: 1737733368940546 -->
# Delete a playable asset
> Đường dẫn: API Reference > Playable Ads > Delete a playable asset
Sử dụng endpoint này để xóa a playable asset. 

Only saved playable assets can be deleted. You can use [/playable/save/](56-playable-ads.md#doc-1737732203851777) to save a playable asset.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/playable/delete/

**Method** POST

**Header**
| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token ***(Bắt buộc)*** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162).|
**Parameters**
| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id ***(Bắt buộc)*** | string | ID tài khoản quảng cáo TikTok. |
| playable_id ***(Bắt buộc)*** | string | Playable asset ID. |

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/playable/delete/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id": "{{advertiser_id}}",
    "playable_id": "{{playable_id}}"
}'
```

## Dữ liệu phản hồi (Response)
| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|code |number|Mã trạng thái phản hồi (0: Thành công). For the complete list of response codes and descriptions, see [Appendix-Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097).  |
|message |string|Thông điệp phản hồi từ máy chủ. Để biết chi tiết, xem [Appendix-Return information](../15-appendix/phu-luc-p1.md#doc-1737172488964097).  |
| request_id | string |The log id of a request, which uniquely identifies the request. |
|data |object|Returned data.|
#| playable_id | string | Playable asset ID. |

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "playable_id": "{{playable_id}}"
    }
}
```
---

## Hướng dẫn thực hành Data Retrieval (Python & cURL)

Dưới đây là mã nguồn mẫu minh họa quy trình gọi API thực tế cho phân hệ **Quảng cáo Playable (Playable Ads)**:

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

