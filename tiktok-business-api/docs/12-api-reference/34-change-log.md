# Nhật ký thay đổi (Change Log)

> Phân hệ: apiref:Change Log.
> Tài liệu biên dịch kỹ thuật chi tiết theo chuẩn TikTok Business API v1.3.

---

## Mục lục điều hướng
- [1. Change Log (#doc-1738811145996290)](#doc-1738811145996290)
- [2. Create a change log download task (#doc-1738811219460097)](#doc-1738811219460097)
- [3. Check the status of a download task (#doc-1739916077352961)](#doc-1739916077352961)
- [4. Get the downloaded file (#doc-1739924165710849)](#doc-1739924165710849)

---

<a id="doc-1738811145996290"></a>
<!-- doc_id: 1738811145996290 -->
<!-- doc_id: 1738811145996290 -->
# Change Log
> Đường dẫn: API Reference > Change Log
The change logs show you the changes made to your ad account, campaigns, ad groups and ads. This is a great way for agencies and businesses to monitor changes made by team members. You can use the Change Log API to retrieve log data to track campaign changes and troubleshoot issues. You will be able to view the time when a change is made, the object that has been changed, the change details, and the Toán tử điều kiện who made specific changes to a campaign, ad group, or ad.

To get the change log file, you need to first create an asynchronous download task via [/changelog/task/create/](34-change-log.md#doc-1738811219460097), then use [/changelog/task/check/](34-change-log.md#doc-1739916077352961) to check Liệu task completes  (`status` = `SUCCESS`), and finally when the task completes, call [/changelog/task/download/](34-change-log.md#doc-1739924165710849) to download the change log file.

This group consists of the following endpoints:
- [Create a change log download task](34-change-log.md#doc-1738811219460097)
- [Check the status of a download task](34-change-log.md#doc-1739916077352961)
- [Get the downloaded file](34-change-log.md#doc-1739924165710849)

---

<a id="doc-1738811219460097"></a>
<!-- doc_id: 1738811219460097 -->
<!-- doc_id: 1738811219460097 -->
# Create a change log download task
> Đường dẫn: API Reference > Change Log > Create a change log download task
Use this endpoint to initiate a change log download task for an ad account based on the parameters that you specify. 

## Yêu cầu gọi API (Request)

**Endpoint**  
https://business-api.tiktok.com/open_api/v1.3/changelog/task/create/

**Method** POST

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|Access-Token ***(Bắt buộc)***|string|Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162).|
|Content-Type ***(Bắt buộc)***|string|Định dạng dữ liệu yêu cầu. <br data-tomark-pass> Allowed values: `"application/json"`. |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|advertiser_id ***(Bắt buộc)***|string| ID tài khoản quảng cáo TikTok |
|start_time |string| Query start time, in the format of `YYYY-MM-DD HH:MM:SS`.<br>Example: `2025-09-01 00:00:00`. |
|end_time |string| Query end time, in the format of `YYYY-MM-DD HH:MM:SS` <br>Example: `2025-09-01 00:00:00`.<br><p><span style="color:darkred"><b>Note</b></span>: The largest time gap allowed is 30 days, so please specify a date within 30 days after the start_time as end_time. |
|timezone |string| Timezone of returned value, refer to [Appendix-Time Zone](../15-appendix/phu-luc-p1.md#doc-1737586324313089) for optional values. |
|module |string| Module to be queried, optional values: <ul><li>`BIDDING_AND_OPTIMIZATION`</li> <li>`BUDGET`</li><li>`STATUS`</li><li>`TARGETING`</li></ul> |
|object_ids |string[]| Query object ID |
|object_type |string| Query object type, optional values: `AD`,`ADGROUP`,`ADVERTISER`,`CAMPAIGN`,`INSTANT_FORM`  |
|operation_types |string[]| Operation type, optional values: `CREATE`, `AUDIT`, `STATUS`, `UPDATE`, `DELETE`, `DOWNLOAD_LEADS`, `SUBSCRIBE_FORM`, `UNSUBSCRIBE_FORM` |
|order_fields |string[]| Order by fields |

### Ví dụ lệnh cURL (Example)

``` xcodeblock
(code curl http)
curl -H "Access-Token:xxx" -H "Content-Type:application/json" -X POST \
-d '{
    "order_type": "ORDER_TYPE", 
    "order_fields": "ORDER_FIELDS", 
    "operation_types": [
        "OPT_TYPES"
    ], 
    "start_time": "START_TIME", 
    "object_type": "OBJECT_TYPE", 
    "object_ids": [
        "OBJECT_IDS"
    ], 
    "module": "MODULE", 
    "advertiser_id": "ADVERTISER_ID", 
    "end_time": "END_TIME", 
    "timezone": "TIMEZONE", 
}' \
https://business-api.tiktok.com/open_api/v1.3/changelog/task/create/
(/code)
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|code |number|Mã trạng thái phản hồi (0: Thành công), see [Appendix-Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097) |
|message |string|Return messages, see [Appendix-Return information](../15-appendix/phu-luc-p1.md#doc-1737172488964097)|
|data |object|Return data|
#|task_id |string| Task ID |
|request_id |string|The log id of a request, which uniquely identifies the request.|

### Ví dụ lệnh cURL (Example)

``` xcodeblock
(code Success-Response http)
HTTPS/1.1 200 OK
{
  "code": 0,
  "data": {
    "task_id": "6917870916856709125"
  },
  "message": "OK"
}
(/code);
```

---

<a id="doc-1739916077352961"></a>
<!-- doc_id: 1739916077352961 -->
<!-- doc_id: 1739916077352961 -->
# Check the status of a download task
> Đường dẫn: API Reference > Change Log > Check the status of a download task
Sử dụng endpoint này để kiểm tra Liệu a change log download task has completed or not.

## Yêu cầu gọi API (Request)

**Endpoint**  
https://business-api.tiktok.com/open_api/v1.3/changelog/task/check/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|Access-Token ***(Bắt buộc)***|string|Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|advertiser_id ***(Bắt buộc)***|string| ID tài khoản quảng cáo TikTok. |
|task_id ***(Bắt buộc)***|string| Task ID. |

### Ví dụ lệnh cURL (Example)

``` xcodeblock
(code curl http)
curl --get -H "Access-Token:xxx" \
--data-urlencode "advertiser_id=ADVERTISER_ID" \
--data-urlencode "task_id=TASK_ID" \
https://business-api.tiktok.com/open_api/v1.3/changelog/task/check/
(/code)
```

## Dữ liệu phản hồi (Response)
| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|code |number|Mã trạng thái phản hồi (0: Thành công), see [Appendix-Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message |string|Return messages, see [Appendix-Return information](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|data |object|Return data|
#|status |string| Task status values: <ul><li>`PROCESSING`</li> <li>`SUCCESS`</li><li>`FAILED`</li></ul>|
|request_id |string|The log id of a request, which uniquely identifies the request.|

### Ví dụ lệnh cURL (Example)

``` xcodeblock
(code Success-Response http)
HTTPS/1.1 200 OK
{
    "message": "OK",
    "code": 0,
    "data": {
        "status": "SUCCESS"
    },
    "request_id": "2021011514371101023125009010565"
}
(/code);
```

---

<a id="doc-1739924165710849"></a>
<!-- doc_id: 1739924165710849 -->
<!-- doc_id: 1739924165710849 -->
# Get the downloaded file
> Đường dẫn: API Reference > Change Log > Get the downloaded file
Use this endpoint to download the change log file. 

## Yêu cầu gọi API (Request)

**Endpoint**  
https://business-api.tiktok.com/open_api/v1.3/changelog/task/download/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|Access-Token ***(Bắt buộc)***|string|Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|advertiser_id ***(Bắt buộc)***|string| ID tài khoản quảng cáo TikTok |
|task_id ***(Bắt buộc)***|string| Task ID |

### Ví dụ lệnh cURL (Example)

``` xcodeblock
(code curl http)
curl --get -H "Access-Token:xxx" \
--data-urlencode "advertiser_id=ADVERTISER_ID" \
--data-urlencode "task_id=TASK_ID" \
https://business-api.tiktok.com/open_api/v1.3/changelog/task/download/
(/code)
```

## Dữ liệu phản hồi (Response)
| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|code |number|Mã trạng thái phản hồi (0: Thành công), see【[Appendix-Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097)】 |
|message |string|Return messages, see【[Appendix-Return information](../15-appendix/phu-luc-p1.md#doc-1737172488964097)】|
|data |object|Return data|
#|status |string| Task status. Các giá trị enum hỗ trợ: <ul><li>`PROCESSING`</li> <li>`SUCCESS`</li><li>`FAILED`</li></ul>|
#|changelog |string| CSV file data of the log  |
|request_id |string|The log id of a request, which uniquely identifies the request.|

### Ví dụ lệnh cURL (Example)
``` xcodeblock
(code Success-Response CSV)
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "changelog": "{'file_data': b'Budget changes,2\\r\\nBid changes,0\\r\\nStatus changes,0\\r\\n\\r\\nTime,log_object_type,Object ID,Object,Toán tử điều kiện,Source,App ID,Activity details
    \\r\\n2024-10-04 15:20,Ad group,{{object_id}},Budget & Schedule,m**********t@gmail.com,Marketing API,{{app_id}},\"[{\"\"action\"\": \"\"Change \"\", \"\"name\"\": \"\"Budget\"\", \"\"before_after\"\": [{\"\"before\"\": \"\"b\\'50.00 USD\\'\"\", \"\"after\"\": \"\"b\\'20.00 USD\\'\"\"}]}]\"
    \\r\\n2024-10-04 15:21,Ad group,{{object_id}},On/Off Status,m**********t@gmail.com,Marketing API,{{app_id}},\"[{\"\"action\"\": \"\"Delete\"\", \"\"name\"\": \"\"Campaign\"\"}]\"
    \\r\\n2024-10-04 15:20,Ad group,{{object_id}},Ad group,m**********t@gmail.com,Marketing API,{{app_id}},\"[{\"\"action\"\": \"\"Create\"\", \"\"name\"\": \"\"Ad group\"\"}]\"
    \\r\\n2024-10-04 15:21,Ad group,{{object_id}},Settings,m**********t@gmail.com,Marketing API,{{app_id}},\"[{\"\"action\"\": \"\"Change \"\", \"\"name\"\": \"\"Name\"\", \"\"before_after\"\": [{\"\"before\"\": \"\"b\\'{{adgroup_name}}'\"\", \"\"after\"\": \"\"b\\'{{adgroup_name}}'\"\"}]}]\"
    \\r\\n2024-10-04 15:20,Ad group,{{object_id}},Ad group,m**********t@gmail.com,Marketing API,{{app_id}},\"[{\"\"action\"\": \"\"Create\"\", \"\"name\"\": \"\"Ad group\"\"}]\"
    \\r\\n2024-10-04 15:20,Ad group,{{object_id}},On/Off Status,m**********t@gmail.com,Marketing API,{{app_id}},\"[{\"\"action\"\": \"\"Delete\"\", \"\"name\"\": \"\"Ad group\"\"}]\"
    \\r\\n2024-10-04 15:20,Ad group,{{object_id}},Settings,m**********t@gmail.com,Marketing API,{{app_id}},\"[{\"\"action\"\": \"\"Change \"\", \"\"name\"\": \"\"Name\"\", \"\"before_after\"\": [{\"\"before\"\": \"\"b\\'{{adgroup_name}}'\"\", \"\"after\"\": \"\"b\\'{{adgroup_name}}'\"\"}]}]\"
    \\r\\n2024-10-04 15:21,Ad group,{{object_id}},On/Off Status,m**********t@gmail.com,Marketing API,{{app_id}},\"[{\"\"action\"\": \"\"Delete\"\", \"\"name\"\": \"\"Campaign\"\"}]\"\\r\\n2024-10-04 15:21,Ad group,{{object_id}},On/Off Status,m**********t@gmail.com,Marketing API,{{app_id}},\"[{\"\"action\"\": \"\"Delete\"\", \"\"name\"\": \"\"Ad group\"\"}]\"
    \\r\\n2024-10-04 15:21,Ad group,{{object_id}},Budget & Schedule,m**********t@gmail.com,Marketing API,{{app_id}},\"[{\"\"action\"\": \"\"Change \"\", \"\"name\"\": \"\"Budget\"\", \"\"before_after\"\": [{\"\"before\"\": \"\"b\\'50.00 USD\\'\"\", \"\"after\"\": \"\"b\\'20.00 USD\\'\"\"}]}]\"
    \\r\\n2024-10-04 15:20,Ad group,{{object_id}},Targeting,m**********t@gmail.com,Marketing API,{{app_id}},\"[{\"\"action\"\": \"\"Change \"\", \"\"name\"\": \"\"Smart audience\"\", \"\"before_after\"\": [{\"\"before\"\": \"\"b\\'On\\'\"\", \"\"after\"\": \"\"b\\'Off\\'\"\"}]}]\"\\r\\n', 
    'file_name': '{{file_name}}'}",
        "status": "SUCCESS"
    }
}
(/code);
```
---

## Hướng dẫn thực hành Data Retrieval (Python & cURL)

Dưới đây là mã nguồn mẫu minh họa quy trình gọi API thực tế cho phân hệ **Nhật ký thay đổi (Change Log)**:

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

