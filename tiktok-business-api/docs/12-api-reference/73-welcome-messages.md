# Tin nhắn chào mừng (Welcome Messages)

> Phân hệ: apiref:Welcome Messages.
> Tài liệu biên dịch kỹ thuật chi tiết theo chuẩn TikTok Business API v1.3.

---

## Mục lục điều hướng
- [1. Welcome Messages (#doc-1822106064917506)](#doc-1822106064917506)
- [2. Create a welcome message within an ad account (#doc-1822106113771521)](#doc-1822106113771521)
- [3. Get welcome messages within an ad account (#doc-1822106498804738)](#doc-1822106498804738)

---

<a id="doc-1822106064917506"></a>
<!-- doc_id: 1822106064917506 -->
<!-- doc_id: 1822106064917506 -->
# Welcome Messages
> Đường dẫn: API Reference > Welcome Messages
Welcome messages are messages that are automatically sent to welcome people to the conversation after they tap on your ad. Welcome Messages API enables you to create and retrieve welcome messages within your ad account.

To learn more about how to create TikTok Direct Messaging Ads with welcome messages, see [Create a Lead Generation ad with optimization location as TikTok direct messages](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1774482992153601).

This group consists of the following endpoints:
- [Create a welcome message within an ad account](73-welcome-messages.md#doc-1822106113771521)
- [Get welcome messages within an ad account](73-welcome-messages.md#doc-1822106498804738)

---

<a id="doc-1822106113771521"></a>
<!-- doc_id: 1822106113771521 -->
<!-- doc_id: 1822106113771521 -->
# Create a welcome message within an ad account
> Đường dẫn: API Reference > Welcome Messages > Create a welcome message within an ad account
Sử dụng endpoint này để tạo a welcome message in your ad account.

Each welcome message will be saved in the welcome message library of the ad account for future use in [TikTok Direct Messaging Ads](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1774482992153601).

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/creative/auto_message/create/

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
| auto_message_type ***(Bắt buộc)*** | string | The type of automatic message to greet people with when they start a conversation with you.<br><br>Enum value: <ul><li>`WELCOME_MESSAGE`: welcome message. A welcome message is a message that is automatically sent to welcome people to the conversation after they tap on your ad.</li></ul>|
| welcome_message **(Điều kiện)** | object | Bắt buộc khi `auto_message_type` is `WELCOME_MESSAGE`. <br><br> Information about the welcome message. |
#| title {+Conditional} | string | Bắt buộc khi `welcome_message` is passed.<br><br> The name of the welcome message. <br> You can specify a unique name to distinguish between different welcome messages within the welcome message library of your ad account. |
#| content {+Conditional} | string | Bắt buộc khi `welcome_message` is passed. <br><br> The greeting within the welcome message. <br><br> Giới hạn độ dài: 200 characters. <br><br> Example: `Hi, thanks for contacting us. How can we help you?` |
#| suggested_questions {+Conditional} | object[] | Bắt buộc khi `welcome_message` is passed. <br><br>A list of suggested questions for customers to tap. <br>A suggested question is a frequently asked question displayed at the beginning of a chat. When the user selects a suggested question, the user will automatically receive the corresponding preset answer.<br><br> Size range: 1-3. |
##| question {+Conditional} | string | Bắt buộc khi `welcome_message` is passed.<br><br> A frequently asked question to help users start a conversation. <br><br> Giới hạn độ dài: 70 characters. |
##| answer {+Conditional} | string | Bắt buộc khi `welcome_message` is passed.<br><br>The preset answer that will be automatically sent when a user selects the question. <br><br>Giới hạn độ dài: 500 characters. |

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/creative/auto_message/create/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id":"{{advertiser_id}}",
    "auto_message_type":"WELCOME_MESSAGE", 
    "welcome_message": {
        "title": "{{title}}",
        "content": "{{content}}",
        "suggested_questions": [
            {
                "question": "{{question}}",
                "answer": "{{answer}}"
                
            },
            {
                "question": "{{question}}",
                "answer": "{{answer}}"
                
            },
            {
                "question": "{{question}}",
                "answer": "{{answer}}"
            }
        ]             
    }
}'
```
## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|code |number|Response code. For the complete list of response codes and descriptions, see [Appendix-Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message|string|Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|request_id |string|The log ID of a request, which uniquely identifies the request.  |
|data |object|Returned data.|
# |auto_message_id|string| The ID of the automatic message.|

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "auto_message_id": "{{auto_message_id}}"
    }
}
```

---

<a id="doc-1822106498804738"></a>
<!-- doc_id: 1822106498804738 -->
<!-- doc_id: 1822106498804738 -->
# Get welcome messages within an ad account
> Đường dẫn: API Reference > Welcome Messages > Get welcome messages within an ad account
Sử dụng endpoint này để truy xuất the welcome messages within the welcome message library of your ad account.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/creative/auto_message/get/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
| advertiser_id ***(Bắt buộc)*** | string | ID tài khoản quảng cáo TikTok. |
| auto_message_type ***(Bắt buộc)*** | string | The type of automatic message to greet people with when they start a conversation with you.<br><br>Enum value: <ul><li>`WELCOME_MESSAGE`: welcome message. A welcome message is a message that is automatically sent to welcome people to the conversation after they tap on your ad.</li></ul>|
| auto_message_id | string | The ID of the automatic message. <br><br>When `auto_message_type` is `WELCOME_MESSAGE`, you can specify the ID of a welcome message via this field to filter the results. <br><br> If this field is not passed, all messages that belong to the specified automatic message type will be returned. |
| page | number | Current Số trang cần lấy dữ liệu.<br><br> Value range: ≥ 1.<br>Giá trị mặc định: 1. |
| page_size| number | Page size.<br><br> Value range: 1-100.<br>Giá trị mặc định: 10. |

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/creative/auto_message/get/?advertiser_id={{advertiser_id}}&auto_message_type=WELCOME_MESSAGE&page=1&page_size=100' \
--header 'Access-Token: {{Access-Token}}'
```
## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|code |number|Response code. For the complete list of response codes and descriptions, see [Appendix-Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message|string|Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|request_id |string|The log ID of a request, which uniquely identifies the request.  |
|data |object|Returned data.|
#| list | object[] | The list of automatic messages within the ad account. |
##| auto_message_id | string | The ID of the automatic message. |
##| auto_message_type | string |The type of automatic message to greet people with when they start a conversation with you.<br><br>Enum value: <ul><li>`WELCOME_MESSAGE`: welcome message. A welcome message is a message that is automatically sent to welcome people to the conversation after they tap on your ad.</li></ul>|
##| welcome_message | string | Information about the welcome message. |
###| title | string | The name of the welcome message.<br><br>You can use the name to distinguish between different welcome messages within the welcome message library of your ad account. |
###| content | string | The greeting within the welcome message. <br><br> Example: `Hi, thanks for contacting us. How can we help you?` |
###| suggested_questions | object[] | A list of suggested questions for customers to tap.<br>A suggested question is a frequently asked question displayed at the beginning of a chat. When the user selects a suggested question, the user will automatically receive the corresponding preset answer.Suggested questions. |
####| question | string | A frequently asked question to help users start a conversation. |
####| answer | string | The preset answer that will be automatically sent when a user selects the question. |
##| audit_status| string | The review status of the automatic message. <br><br>Các giá trị enum hỗ trợ: <ul><li>`AUDITING`: The automatic message is pending review.</li><li>`PASS`: The automatic message has been approved.</li><li>`REJECTED`: The automatic message has been rejected. </li></ul>|
##| create_time | string | The time when the automatic message was created, in the format of `YYYY-MM-DD HH:MM:SS` (UTC+0). <br><br> Example: `2025-01-01 00:00:01`. |
#| page_info | object | Pagination information.<br><br><p><span style="color:darkred"><b>Note</b></span>: If `auto_message_id` is specified in the request, `page_info` will not be returned. |
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
        "auto_message_list": [
            {
                "audit_status": "PASS",
                "auto_message_id": "{{auto_message_id}}",
                "auto_message_type": "WELCOME_MESSAGE",
                "create_time": "{{create_time}}",
                "welcome_message": {
                    "content": "{{content}}",
                    "suggested_questions": [
                        {
                            "answer": "{{answer}}",
                            "question": "{{question}}"
                        },
                        {
                            "answer": "{{answer}}",
                            "question": "{{question}}"
                        },
                        {
                            "answer": "{{answer}}",
                            "question": "{{question}}"
                        }
                    ],
                    "title": "{{title}}"
                }
            }
        ]
    }
}
```
---

## Hướng dẫn thực hành Data Retrieval (Python & cURL)

Dưới đây là mã nguồn mẫu minh họa quy trình gọi API thực tế cho phân hệ **Tin nhắn chào mừng (Welcome Messages)**:

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

