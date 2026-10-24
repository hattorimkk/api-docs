# Pangle

> Phân hệ: apiref:Pangle.
> Tài liệu biên dịch kỹ thuật chi tiết theo chuẩn TikTok Business API v1.3.

---

## Mục lục điều hướng
- [1. Pangle (#doc-1739091153164290)](#doc-1739091153164290)
- [2. Get the Pangle block list (#doc-1740039957181441)](#doc-1740039957181441)
- [3. Update the Pangle block list (#doc-1740040139110466)](#doc-1740040139110466)
- [4. Get the Pangle audience packages (#doc-1740040177229826)](#doc-1740040177229826)

---

<a id="doc-1739091153164290"></a>
<!-- doc_id: 1739091153164290 -->
<!-- doc_id: 1739091153164290 -->
# Pangle
> Đường dẫn: API Reference > Pangle
Pangle is the audience network of TikTok For Business. It is the go-to-place for monetizing apps, attracting users, and pushing boundaries of creativity. Established as the leading mobile advertising platform in Asia, Pangle enables global app developers to maximize earnings through exclusive TikTok For Business demand, and advertisers to reach out to a massive audience. To learn more about Pangle, see [https://www.pangleglobal.com/](https://www.pangleglobal.com/).

This group consists of the following endpoints:
* [Get the Pangle block list](55-pangle.md#doc-1740039957181441)
* [Update the Pangle block list](55-pangle.md#doc-1740040139110466)
* [Get the Pangle audience packages](55-pangle.md#doc-1740040177229826)

---

<a id="doc-1740039957181441"></a>
<!-- doc_id: 1740039957181441 -->
<!-- doc_id: 1740039957181441 -->
# Get the Pangle block list
> Đường dẫn: API Reference > Pangle > Get the Pangle block list
Sử dụng endpoint này để lấy thông tin the Pangle block list of an ad account.

## Yêu cầu gọi API (Request)

**Endpoint**
https://business-api.tiktok.com/open_api/v1.3/pangle_block_list/get/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id  ****(Bắt buộc)**** | string | ID tài khoản quảng cáo TikTok. |

### Ví dụ lệnh cURL (Example)

```http
// curl
curl --get -H "Access-Token:xxx" \
--data-urlencode "advertiser_id=ADVERTISER_ID" \
https://ads.tiktok.com/open_api/v1.3/pangle_block_list/get/
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Mã trạng thái phản hồi (0: Thành công). For the complete list of response codes and descriptions, see [Appendix-Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Return messages. Để biết chi tiết, xem [Appendix-Return information](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| data | object | Returned data. |
| ↳ app_list | string[] | App block list. iTunes ID for iOS app and package name for Android apps. |
| ↳ app_package_id | string | App block list ID. |
| ↳ modify_time | string | The time when the App block list was last updated, in [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) format. ⏎ Example: "2024-01-01T00:00:01+00:00". |
| request_id | string | The log id of a request, which uniquely identifies the request. |

### Ví dụ lệnh cURL (Example)

```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "modify_time": "2024-01-30T01:57:34+00:00",
        "app_package_id": "{{app_package_id}}",
        "app_list": [
            "android.package.name"
        ]
    }
}
```

---

<a id="doc-1740040139110466"></a>
<!-- doc_id: 1740040139110466 -->
<!-- doc_id: 1740040139110466 -->
# Update the Pangle block list
> Đường dẫn: API Reference > Pangle > Update the Pangle block list
Sử dụng endpoint này để cập nhật Pangle block list.
      
## Yêu cầu gọi API (Request)

**Endpoint**
https://business-api.tiktok.com/open_api/v1.3/pangle_block_list/update/

**Method** POST

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type  ****(Bắt buộc)**** | string | Định dạng dữ liệu yêu cầu ⏎ Allowed format: `"application/json"`. |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id  ****(Bắt buộc)**** | string | ID tài khoản quảng cáo TikTok. |
| add_app_list | string[] | Apps to add in the block list. iTunes ID for iOS app and package name for Android apps. |
| delete_app_list | string[] | Apps to delete in the block list. iTunes ID for iOS app and package name for Android apps. |
| clear_old_app | boolean | Có thực hiện clear the original App block list, Giá trị mặc định: `False`. If `False`, the corresponding App will be deleted and added based on the original list; if `True`, the original list will be cleared and the corresponding App will be added. |

### Ví dụ lệnh cURL (Example)
```http
// curl
curl -H "Access-Token:xxx" -H "Content-Type:application/json" -X POST \
-d '{
    "advertiser_id": "ADVERTISER_ID", 
    "clear_old_app": "CLEAR_OLD_APP", 
    "add_app_list": [
        "ADD_APP_LIST"
    ], 
    "delete_app_list": [
        "DELETE_APP_LIST"
    ]
}' \
https://ads.tiktok.com/open_api/v1.3/pangle_block_list/update/
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Mã trạng thái phản hồi (0: Thành công). For the complete list of response codes and descriptions, see [Appendix-Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Return messages. Để biết chi tiết, xem [Appendix-Return information](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| data | object | Returned data. |
| ↳ success_count | number | The number of apps that have been sucessfully added to the block list. The success count will not include deletion, regardless of Liệu deletion is successful or not. |
| request_id | string | The log id of a request, which uniquely identifies the request. |

### Ví dụ lệnh cURL (Example)

```http
// Success-Response
HTTPS/1.1 200 OK
{
    "message": "OK",
    "code": 0,
    "data": {
        "success_count": 2
    },
    "request_id": "2020082611320501023125009013028"
}
```

---

<a id="doc-1740040177229826"></a>
<!-- doc_id: 1740040177229826 -->
<!-- doc_id: 1740040177229826 -->
# Get the Pangle audience packages
> Đường dẫn: API Reference > Pangle > Get the Pangle audience packages
Sử dụng endpoint này để lấy thông tin the Pangle audience packages that are available to an advertiser. 

This audience package is only available for Pangle ad placement, and will not affect traffic for other placements. The audience package will be applied alongside any other targeting settings you select. Audience packages can help you more effectively reach your target audience, while narrowing down the scope for delivery.

## Yêu cầu gọi API (Request)
**Endpoint**
https://business-api.tiktok.com/open_api/v1.3/pangle_audience_package/get/

**Method** GET

**Header**

| Field | Data Type | Desciption |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id  ****(Bắt buộc)**** | string | ID tài khoản quảng cáo TikTok. |

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --get -H "Access-Token:xxx" \
--data-urlencode "advertiser_id=ADVERTISER_ID" \
https://ads.tiktok.com/open_api/v1.3/pangle_audience_package/get/
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Mã trạng thái phản hồi (0: Thành công). For the complete list of response codes and descriptions, see [Appendix-Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông điệp phản hồi từ máy chủ. Để biết chi tiết, xem [Appendix-Return information](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| data | object | Returned data. |
| ↳ packages | object[] | Pangle audience package list. |
| ↳↳ bind_type | string | Pangle audience package type. Các giá trị enum hỗ trợ: `EXCLUDE`, `INCLUDE`. |
| ↳↳ package_id | string | Pangle audience package ID. |
| ↳↳ package_name | string | Pangle audience package name. |
| request_id | string | The log id of a request, which uniquely identifies the request. |

### Ví dụ lệnh cURL (Example)

```http
// Success-Response
HTTPS/1.1 200 OK
{
    "message": "OK",
    "code": 0,
    "data": {
        "packages": [
            {
                "bind_type": "INCLUDE",
                "package_name": "AudiencePackage0",
                "package_id": 3
            },
            {
                "bind_type": "EXCLUDE",
                "package_name": "AudiencePackage1",
                "package_id": 14
            },
            {
                "bind_type": "INCLUDE",
                "package_name": "AudiencePackage2",
                "package_id": 5
            }
        ]
    },
    "request_id": "2020101209435901023125009012611"
}
```
---

## Hướng dẫn thực hành Data Retrieval (Python & cURL)

Dưới đây là mã nguồn mẫu minh họa quy trình gọi API thực tế cho phân hệ **Pangle**:

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

