# Từ khóa bị chặn trong bình luận (Blocked Words)
<a id="doc-1739029198660609"></a>
<!-- doc_id: 1739029198660609 -->

Từ khóa bị chặn (blocked words) được sử dụng để tự động ẩn các bình luận không mong muốn. Nếu một bình luận chứa từ khóa nằm trong danh sách bị chặn, bình luận đó sẽ bị ẩn với tất cả mọi người, ngoại trừ chính người dùng đã đăng bình luận đó.

Mỗi tài khoản quảng cáo có thể thiết lập tối đa 500 từ khóa bị chặn.

Nhóm API này bao gồm các endpoint sau:
* [Tạo từ khóa bị chặn](05-ad-comments-blocked-words.md#doc-1739029218470913)
* [Cập nhật từ khóa bị chặn](05-ad-comments-blocked-words.md#doc-1739029234526209)
* [Kiểm tra trạng thái của các từ khóa](05-ad-comments-blocked-words.md#doc-1739029247961089)
* [Lấy danh sách từ khóa bị chặn](05-ad-comments-blocked-words.md#doc-1739029260837889)
* [Xóa từ khóa bị chặn](05-ad-comments-blocked-words.md#doc-1739029277346817)
* [Tạo tác vụ xuất từ khóa bị chặn](05-ad-comments-blocked-words.md#doc-1739029296119809)
* [Kiểm tra trạng thái tác vụ xuất từ khóa bị chặn](05-ad-comments-blocked-words.md#doc-1739029311687681)
* [Tải về dữ liệu đã xuất](05-ad-comments-blocked-words.md#doc-1739029325203457)

---

## Tạo từ khóa bị chặn (`Create blocked words`)
<a id="doc-1739029218470913"></a>
<!-- doc_id: 1739029218470913 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/blockedword/create/`

**Mục đích**: Sử dụng endpoint này để thêm các từ khóa vào danh sách từ khóa bị chặn của tài khoản quảng cáo. Mỗi tài khoản quảng cáo có thể có tối đa 500 từ khóa bị chặn.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền (access token). Xem chi tiết tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type | string | Bắt buộc | Định dạng nội dung yêu cầu. Giá trị: `application/json`. |

### Tham số (POST JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| advertiser_id | string | Bắt buộc | ID tài khoản quảng cáo (advertiser ID). |
| blocked_words | string[] | Bắt buộc | Danh sách các từ khóa muốn chặn. |

### Ví dụ

```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/blockedword/create/' --header 'Access-Token: YOUR_ACCESS_TOKEN' --header 'Content-Type: application/json' --data-raw '{
  "advertiser_id": "7123456789012345678",
  "blocked_words": ["lừa đảo", "hàng giả", "kém chất lượng"]
}'
```

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. Xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | Mã nhật ký định danh duy nhất của yêu cầu. |
| data | object | Dữ liệu trả về (đối tượng rỗng khi thành công). |

### Ví dụ phản hồi

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202605210639490102360430824C1AE673",
  "data": {}
}
```

---

## Cập nhật từ khóa bị chặn (`Update a blocked word`)
<a id="doc-1739029234526209"></a>
<!-- doc_id: 1739029234526209 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/blockedword/update/`

**Mục đích**: Sử dụng endpoint này để thay thế một từ khóa bị chặn cũ bằng một từ khóa bị chặn mới trong danh sách.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền (access token). Xem chi tiết tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type | string | Bắt buộc | Định dạng nội dung yêu cầu. Giá trị: `application/json`. |

### Tham số (POST JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| advertiser_id | string | Bắt buộc | ID tài khoản quảng cáo (advertiser ID). |
| old_word | string | Bắt buộc | Từ khóa bị chặn cũ cần thay thế. |
| new_word | string | Bắt buộc | Từ khóa bị chặn mới thay thế cho từ cũ. |

### Ví dụ

```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/blockedword/update/' --header 'Access-Token: YOUR_ACCESS_TOKEN' --header 'Content-Type: application/json' --data-raw '{
  "advertiser_id": "7123456789012345678",
  "old_word": "hàng giả",
  "new_word": "hàng nhái"
}'
```

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. Xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | Mã nhật ký định danh duy nhất của yêu cầu. |

### Ví dụ phản hồi

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202605210639490102360430824C1AE673",
  "data": {}
}
```

---

## Kiểm tra trạng thái của các từ khóa (`Check the statuses of words`)
<a id="doc-1739029247961089"></a>
<!-- doc_id: 1739029247961089 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/blockedword/check/`

**Mục đích**: Sử dụng endpoint này để kiểm tra xem một danh sách các từ khóa cụ thể đã có trong danh sách bị chặn của tài khoản quảng cáo hay chưa.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền (access token). Xem chi tiết tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (GET query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| advertiser_id | string | Bắt buộc | ID tài khoản quảng cáo (advertiser ID). |
| blocked_words | string[] | Bắt buộc | Danh sách các từ khóa cần kiểm tra (truyền dưới dạng chuỗi JSON mảng). |

### Ví dụ

#### cURL
```bash
curl --get -H "Access-Token: YOUR_ACCESS_TOKEN" --data-urlencode "advertiser_id=7123456789012345678" --data-urlencode 'blocked_words=["lừa đảo","uy tín"]' https://business-api.tiktok.com/open_api/v1.3/blockedword/check/
```

#### Python
```python
import json
import os
import requests

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", "YOUR_ACCESS_TOKEN")
ADVERTISER_ID = os.environ.get("ADVERTISER_ID", "7123456789012345678")

url = "https://business-api.tiktok.com/open_api/v1.3/blockedword/check/"
headers = {
    "Access-Token": ACCESS_TOKEN,
}
params = {
    "advertiser_id": ADVERTISER_ID,
    "blocked_words": json.dumps(["lừa đảo", "uy tín"]),
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. Xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | Mã nhật ký định danh duy nhất của yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ results | object[] | Danh sách kết quả kiểm tra cho từng từ khóa. |
| ↳↳ word | string | Từ khóa được kiểm tra. |
| ↳↳ blocked | boolean | Cho biết từ khóa có bị chặn hay không: `True` (bị chặn) hoặc `False` (không bị chặn). |

### Ví dụ phản hồi

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202605210639490102360430824C1AE673",
  "data": {
    "results": [
      {
        "word": "lừa đảo",
        "blocked": true
      },
      {
        "word": "uy tín",
        "blocked": false
      }
    ]
  }
}
```

---

## Lấy danh sách từ khóa bị chặn (`Get blocked words`)
<a id="doc-1739029260837889"></a>
<!-- doc_id: 1739029260837889 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/blockedword/list/`

**Mục đích**: Sử dụng endpoint này để lấy toàn bộ danh sách các từ khóa đang bị chặn trong tài khoản quảng cáo kèm theo phân trang.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền (access token). Xem chi tiết tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (GET query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| advertiser_id | string | Bắt buộc | ID tài khoản quảng cáo (advertiser ID). |
| page_info | object | Không bắt buộc | Thông tin phân trang (truyền dưới dạng chuỗi JSON đối tượng). |
| ↳ page | number | Không bắt buộc | Số trang hiện tại. Giá trị: ≥ 1. Mặc định: 1. |
| ↳ page_size | number | Không bắt buộc | Số bản ghi mỗi trang. Khoảng giá trị: [1, 500]. Mặc định: 10. |

### Ví dụ

#### cURL
```bash
curl --get -H "Access-Token: YOUR_ACCESS_TOKEN" --data-urlencode "advertiser_id=7123456789012345678" --data-urlencode 'page_info={"page":1,"page_size":20}' https://business-api.tiktok.com/open_api/v1.3/blockedword/list/
```

#### Python
```python
import json
import os
import requests

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", "YOUR_ACCESS_TOKEN")
ADVERTISER_ID = os.environ.get("ADVERTISER_ID", "7123456789012345678")

url = "https://business-api.tiktok.com/open_api/v1.3/blockedword/list/"
headers = {
    "Access-Token": ACCESS_TOKEN,
}
params = {
    "advertiser_id": ADVERTISER_ID,
    "page_info": json.dumps({"page": 1, "page_size": 20}),
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. Xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | Mã nhật ký định danh duy nhất của yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ list | object[] | Danh sách các từ khóa bị chặn. |
| ↳↳ bw_content | string | Nội dung từ khóa bị chặn. |
| ↳ page_info | object | Thông tin phân trang. |
| ↳↳ page | number | Số trang hiện tại. |
| ↳↳ page_size | number | Kích thước trang. |
| ↳↳ total_number | number | Tổng số từ khóa bị chặn tìm thấy. |
| ↳↳ total_page | number | Tổng số trang kết quả. |

### Ví dụ phản hồi

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202605210639490102360430824C1AE673",
  "data": {
    "list": [
      {
        "bw_content": "lừa đảo"
      },
      {
        "bw_content": "hàng giả"
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

## Xóa từ khóa bị chặn (`Delete blocked words`)
<a id="doc-1739029277346817"></a>
<!-- doc_id: 1739029277346817 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/blockedword/delete/`

**Mục đích**: Sử dụng endpoint này để xóa một hoặc nhiều từ khóa ra khỏi danh sách bị chặn. Khi một từ khóa bị xóa, các bình luận chứa từ khóa này sẽ trở lại trạng thái công khai thay vì chỉ hiển thị với người đăng.

> [!NOTE]
> Nếu bạn cố gắng xóa một từ khóa không có trong danh sách từ khóa bị chặn, hệ thống sẽ bỏ qua và không báo lỗi.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền (access token). Xem chi tiết tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type | string | Bắt buộc | Định dạng nội dung yêu cầu. Giá trị: `application/json`. |

### Tham số (POST JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| advertiser_id | string | Bắt buộc | ID tài khoản quảng cáo (advertiser ID). |
| blocked_words | string[] | Bắt buộc | Danh sách các từ khóa bị chặn muốn xóa. |

### Ví dụ

```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/blockedword/delete/' --header 'Access-Token: YOUR_ACCESS_TOKEN' --header 'Content-Type: application/json' --data-raw '{
  "advertiser_id": "7123456789012345678",
  "blocked_words": ["hàng giả", "hàng nhái"]
}'
```

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. Xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | Mã nhật ký định danh duy nhất của yêu cầu. |
| data | object | Dữ liệu trả về (đối tượng rỗng khi thành công). |

### Ví dụ phản hồi

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202605210639490102360430824C1AE673",
  "data": {}
}
```

---

## Tạo tác vụ xuất từ khóa bị chặn (`Create an export task (blocked words)`)
<a id="doc-1739029296119809"></a>
<!-- doc_id: 1739029296119809 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/blockedword/task/create/`

**Mục đích**: Sử dụng endpoint này để khởi tạo tác vụ xuất danh sách từ khóa bị chặn dưới dạng tệp. Sau khi tạo tác vụ, bạn dùng [/blockedword/task/check/](05-ad-comments-blocked-words.md#doc-1739029311687681) để kiểm tra tiến độ và [/blockedword/task/download/](05-ad-comments-blocked-words.md#doc-1739029325203457) để tải về tệp hoàn chỉnh.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền (access token). Xem chi tiết tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type | string | Bắt buộc | Định dạng nội dung yêu cầu. Giá trị: `application/json`. |

### Tham số (POST JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| advertiser_id | string | Bắt buộc | ID tài khoản quảng cáo (advertiser ID). |
| blocked_words | string[] | Không bắt buộc | Danh sách các từ khóa bị chặn muốn xuất. Nếu không chỉ định, toàn bộ từ khóa bị chặn sẽ được xuất.<br>Lưu ý: Các từ không bị chặn nếu truyền vào trường này sẽ bị bỏ qua. |
| lang | string | Không bắt buộc | Ngôn ngữ tiêu đề của tệp dữ liệu xuất ra. Các giá trị: `EN`, `JA`, `ZH`. Mặc định: `EN`. |

### Ví dụ

```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/blockedword/task/create/' --header 'Access-Token: YOUR_ACCESS_TOKEN' --header 'Content-Type: application/json' --data-raw '{
  "advertiser_id": "7123456789012345678",
  "lang": "EN"
}'
```

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. Xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | Mã nhật ký định danh duy nhất của yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ task_id | string | ID của tác vụ xuất dữ liệu vừa tạo. |

### Ví dụ phản hồi

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202605210639490102360430824C1AE673",
  "data": {
    "task_id": "bw_task_987654321"
  }
}
```

---

## Kiểm tra trạng thái tác vụ xuất từ khóa bị chặn (`Check the status of an export task (blocked words)`)
<a id="doc-1739029311687681"></a>
<!-- doc_id: 1739029311687681 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/blockedword/task/check/`

**Mục đích**: Sử dụng endpoint này để kiểm tra trạng thái xử lý của tác vụ xuất dữ liệu từ khóa bị chặn. Khi tác vụ hoàn tất, bạn gọi [/blockedword/task/download/](05-ad-comments-blocked-words.md#doc-1739029325203457) để tải tệp về.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền (access token). Xem chi tiết tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (GET query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| advertiser_id | string | Bắt buộc | ID tài khoản quảng cáo (advertiser ID). |
| task_id | string | Bắt buộc | ID tác vụ xuất dữ liệu cần kiểm tra. |

### Ví dụ

#### cURL
```bash
curl --get -H "Access-Token: YOUR_ACCESS_TOKEN" --data-urlencode "advertiser_id=7123456789012345678" --data-urlencode "task_id=bw_task_987654321" https://business-api.tiktok.com/open_api/v1.3/blockedword/task/check/
```

#### Python
```python
import os
import requests

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", "YOUR_ACCESS_TOKEN")
ADVERTISER_ID = os.environ.get("ADVERTISER_ID", "7123456789012345678")

url = "https://business-api.tiktok.com/open_api/v1.3/blockedword/task/check/"
headers = {
    "Access-Token": ACCESS_TOKEN,
}
params = {
    "advertiser_id": ADVERTISER_ID,
    "task_id": "bw_task_987654321",
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Appendix-Return Code](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. Xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | Mã nhật ký định danh duy nhất của yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ task_id | string | ID tác vụ xuất dữ liệu. |
| ↳ status | string | Trạng thái hiện tại của tác vụ: • `RUNNING` (đang xử lý), • `SUCCEED` (thành công), • `FAILED` (thất bại). |

### Ví dụ phản hồi

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202605210639490102360430824C1AE673",
  "data": {
    "task_id": "bw_task_987654321",
    "status": "SUCCEED"
  }
}
```

---

## Tải về dữ liệu đã xuất (`Download exported data`)
<a id="doc-1739029325203457"></a>
<!-- doc_id: 1739029325203457 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/blockedword/task/download/`

**Mục đích**: Sử dụng endpoint này để tải về tệp dữ liệu từ khóa bị chặn sau khi tác vụ xuất dữ liệu đã hoàn thành. Tệp tải về ở định dạng CSV.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền (access token). Xem chi tiết tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (GET query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| advertiser_id | string | Bắt buộc | ID tài khoản quảng cáo (advertiser ID). |
| task_id | string | Bắt buộc | ID tác vụ xuất dữ liệu đã hoàn thành. |

### Ví dụ

#### cURL
```bash
curl --get -H "Access-Token: YOUR_ACCESS_TOKEN" --data-urlencode "advertiser_id=7123456789012345678" --data-urlencode "task_id=bw_task_987654321" https://business-api.tiktok.com/open_api/v1.3/blockedword/task/download/
```

#### Python
```python
import os
import requests

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", "YOUR_ACCESS_TOKEN")
ADVERTISER_ID = os.environ.get("ADVERTISER_ID", "7123456789012345678")

url = "https://business-api.tiktok.com/open_api/v1.3/blockedword/task/download/"
headers = {
    "Access-Token": ACCESS_TOKEN,
}
params = {
    "advertiser_id": ADVERTISER_ID,
    "task_id": "bw_task_987654321",
}

response = requests.get(url, headers=headers, params=params)
with open("blocked_words.csv", "wb") as f:
    f.write(response.content)
print("Đã tải tệp blocked_words.csv thành công!")
```

### Phản hồi

Nội dung phản hồi là tệp định dạng CSV chứa danh sách các từ khóa bị chặn được xuất ra.
