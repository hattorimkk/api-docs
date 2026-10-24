# Từ khóa loại trừ (Negative Keywords)
<a id="doc-1775103049049090"></a>
<!-- doc_id: 1775103049049090 -->

Từ khóa loại trừ (Negative Keywords) là tính năng giúp bạn tối ưu hóa việc phân phối Quảng cáo Tìm kiếm (Search Ads) bằng cách lọc bỏ các cụm từ tìm kiếm không liên quan hoặc các cụm từ có thể ảnh hưởng tiêu cực đến an toàn thương hiệu (brand safety). Nếu cụm từ tìm kiếm của người dùng khớp với từ khóa loại trừ mà bạn đã thiết lập cho nhóm quảng cáo hoặc chiến dịch, quảng cáo thuộc nhóm hoặc chiến dịch đó sẽ không được hiển thị.

Nhóm API này bao gồm các endpoint sau:
- [Lấy danh sách từ khóa loại trừ](53-negative-keywords.md#doc-1775104887052289)
- [Thêm từ khóa loại trừ](53-negative-keywords.md#doc-1775104895291393)
- [Cập nhật một từ khóa loại trừ](53-negative-keywords.md#doc-1775104902283266)
- [Xóa từ khóa loại trừ](53-negative-keywords.md#doc-1775104910010369)
- [Tải xuống danh sách từ khóa loại trừ](53-negative-keywords.md#doc-1775104916876290)

---

## Lấy danh sách từ khóa loại trừ (`Get negative keywords`)
<a id="doc-1775104887052289"></a>
<!-- doc_id: 1775104887052289 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/search_ad/negative_keyword/get/`

**Mục đích**: Sử dụng endpoint này để lấy danh sách các từ khóa loại trừ đã thiết lập cho chiến dịch hoặc nhóm quảng cáo tìm kiếm.

### Header

| Field | Data Type | Bắt buộc | Description |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Access token đã được cấp quyền. Chi tiết xem tại [Xác thực (Authentication)](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (Query string)

| Field | Data Type | Bắt buộc | Description |
|---|---|---|---|
| advertiser_id | string | Bắt buộc | ID nhà quảng cáo. |
| object_type | string | Bắt buộc | Loại đối tượng áp dụng. Chỉ định cấp độ bạn muốn lấy danh sách từ khóa loại trừ. Giá trị enum:<br>• `CAMPAIGN`: Chiến dịch.<br>• `ADGROUP`: Nhóm quảng cáo. |
| object_id | string | Bắt buộc | ID của đối tượng tương ứng với `object_type`:<br>• Nếu `object_type` là `CAMPAIGN`: Điền campaign_id.<br>• Nếu `object_type` là `ADGROUP`: Điền adgroup_id. |
| page | number | Không | Số trang cần lấy kết quả. Giá trị mặc định: `1`. Phạm vi: $\ge 1$. |
| page_size | number | Không | Số bản ghi trên mỗi trang. Giá trị mặc định: `10`. Phạm vi: `[1, 50]`. |

### Phản hồi

| Field | Data Type | Description |
|---|---|---|
| code | number | Mã phản hồi API. `0` thể hiện thành công. Xem [Mã trả về (Return Code)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. |
| request_id | string | Mã nhật ký định danh duy nhất của yêu cầu. |
| data | object | Dữ liệu trả về. Nếu không tìm thấy từ khóa loại trừ nào, một mảng rỗng sẽ được trả về. |
| ↳ keywords | object[] | Danh sách thông tin các từ khóa loại trừ (tối đa 1.000). |
| ↳↳ keyword_id | string | ID định danh của từ khóa loại trừ. |
| ↳↳ name | string | Nội dung từ khóa loại trừ. |
| ↳↳ match_type | string | Loại đối sánh của từ khóa loại trừ:<br>• `PRECISE_WORD`: Đối sánh chính xác (exact match).<br>• `PHRASE_WORD`: Đối sánh cụm từ (phrase match).<br>• `BROAD_WORD`: Đối sánh rộng (broad match). |
| ↳ page_info | object | Thông tin phân trang. |
| ↳↳ page | number | Số trang hiện tại. |
| ↳↳ page_size | number | Số bản ghi trên mỗi trang. |
| ↳↳ total_number | number | Tổng số bản ghi tìm được. |
| ↳↳ total_page | number | Tổng số trang. |

### Ví dụ

#### cURL
```bash
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/search_ad/negative_keyword/get/?advertiser_id=7123456789012345678&object_type=CAMPAIGN&object_id=1734945725409298&page=1&page_size=50' \
--header 'Access-Token: act.example123456789'
```

#### Python
```python
import requests

ACCESS_TOKEN = "act.example123456789"
ADVERTISER_ID = "7123456789012345678"
CAMPAIGN_ID = "1734945725409298"
url = "https://business-api.tiktok.com/open_api/v1.3/search_ad/negative_keyword/get/"

params = {
    "advertiser_id": ADVERTISER_ID,
    "object_type": "CAMPAIGN",
    "object_id": CAMPAIGN_ID,
    "page": 1,
    "page_size": 50
}

headers = {
    "Access-Token": ACCESS_TOKEN
}

response = requests.get(url, headers=headers, params=params)
data = response.json()

for kw in data.get("data", {}).get("keywords", []):
    print(f"Từ khóa: {kw.get('name')} | Loại đối sánh: {kw.get('match_type')} | ID: {kw.get('keyword_id')}")
```

#### Ví dụ phản hồi thành công

```json
{
    "code": 0,
    "message": "OK",
    "request_id": "20261023120000010245035048A1B2C3",
    "data": {
        "keywords": [
            {
                "keyword_id": "7198765432109876543",
                "name": "free",
                "match_type": "BROAD_WORD"
            },
            {
                "keyword_id": "7198765432109876544",
                "name": "crack",
                "match_type": "PRECISE_WORD"
            }
        ],
        "page_info": {
            "page": 1,
            "page_size": 50,
            "total_number": 2,
            "total_page": 1
        }
    }
}
```

---

## Thêm từ khóa loại trừ (`Create negative keywords`)
<a id="doc-1775104895291393"></a>
<!-- doc_id: 1775104895291393 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/search_ad/negative_keyword/add/`

**Mục đích**: Sử dụng endpoint này để thêm các từ khóa loại trừ cho Quảng cáo Tìm kiếm. Khi truy vấn tìm kiếm của người dùng khớp với từ khóa loại trừ, quảng cáo trong chiến dịch hoặc nhóm quảng cáo sẽ không hiển thị.

> [!NOTE]
> - Nếu cấu hình từ khóa loại trừ cho nhóm quảng cáo (`ADGROUP`), bạn cần đảm bảo nhóm quảng cáo đó đã bật Vị trí tìm kiếm tự động (Automatic Search Placement).
> - Nếu cấu hình cho chiến dịch (`CAMPAIGN`), bạn cần đảm bảo ít nhất một nhóm quảng cáo trong chiến dịch đã bật Vị trí tìm kiếm tự động.
> - Mỗi nhóm quảng cáo có thể cấu hình tối đa **10.000** từ khóa loại trừ.

### Header

| Field | Data Type | Bắt buộc | Description |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Access token đã được cấp quyền. Xem thêm [Xác thực](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type | string | Bắt buộc | Định dạng bản tin: `application/json`. |

### Tham số Body (Parameters)

| Field | Data Type | Bắt buộc | Description |
|---|---|---|---|
| advertiser_id | string | Bắt buộc | ID nhà quảng cáo. |
| object_type | string | Bắt buộc | Loại đối tượng muốn áp dụng từ khóa loại trừ: `CAMPAIGN` hoặc `ADGROUP`. |
| object_ids | string[] | Bắt buộc | Mảng chứa danh sách ID chiến dịch hoặc ID nhóm quảng cáo (tối đa 50 ID). |
| replace | boolean | Không | Có thay thế toàn bộ từ khóa loại trừ hiện có bằng danh sách mới trong `keywords` hay không:<br>• `true`: Thay thế toàn bộ từ khóa cũ.<br>• `false`: Thêm mới vào danh sách hiện tại.<br>Giá trị mặc định: `false`. |
| keywords | object[] | Bắt buộc | Danh sách từ khóa loại trừ muốn tạo (tối đa 1.000 từ khóa mỗi yêu cầu). |
| ↳ name | string | Bắt buộc | Nội dung từ khóa loại trừ. Độ dài tối đa: 80 ký tự. Không được chứa các ký tự đặc biệt: `!`, `@`, `%`, `^`, `(`, `)`, `=`, `{`, `}`, `;`, `~`, `` ` ``, `<`, `>`, `?`, `\`, `|`. Các từ khóa trùng tên sẽ tự động bị khử trùng lặp thành một. |
| ↳ match_type | string | Không | Loại đối sánh: `PRECISE_WORD`, `PHRASE_WORD`, `BROAD_WORD`. Mặc định: `BROAD_WORD`. |

### Phản hồi

| Field | Data Type | Description |
|---|---|---|
| code | number | Mã phản hồi API. `0` biểu thị thành công. Xem [Mã trả về (Return Code)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi (`OK`). |
| request_id | string | Mã nhật ký định danh duy nhất của yêu cầu. |
| data | object | Dữ liệu trả về (object rỗng `{}` khi thành công). |

### Ví dụ

#### cURL
```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/search_ad/negative_keyword/add/' \
--header 'Access-Token: act.example123456789' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id": "7123456789012345678",
    "object_type": "CAMPAIGN",
    "object_ids": ["1734945725409298"],
    "replace": false,
    "keywords": [
        {
            "name": "cheap",
            "match_type": "BROAD_WORD"
        },
        {
            "name": "crack download",
            "match_type": "PRECISE_WORD"
        }
    ]
}'
```

#### Python
```python
import requests

ACCESS_TOKEN = "act.example123456789"
ADVERTISER_ID = "7123456789012345678"
CAMPAIGN_ID = "1734945725409298"
url = "https://business-api.tiktok.com/open_api/v1.3/search_ad/negative_keyword/add/"

headers = {
    "Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}

payload = {
    "advertiser_id": ADVERTISER_ID,
    "object_type": "CAMPAIGN",
    "object_ids": [CAMPAIGN_ID],
    "replace": False,
    "keywords": [
        {
            "name": "cheap",
            "match_type": "BROAD_WORD"
        },
        {
            "name": "crack download",
            "match_type": "PRECISE_WORD"
        }
    ]
}

response = requests.post(url, headers=headers, json=payload)
data = response.json()
print("Kết quả thêm từ khóa loại trừ:", data.get("code"), data.get("message"))
```

---

## Cập nhật một từ khóa loại trừ (`Update a negative keyword`)
<a id="doc-1775104902283266"></a>
<!-- doc_id: 1775104902283266 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/search_ad/negative_keyword/update/`

**Mục đích**: Sử dụng endpoint này để chỉnh sửa nội dung tên hoặc loại đối sánh của một từ khóa loại trừ đã tồn tại.

### Header

| Field | Data Type | Bắt buộc | Description |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Access token đã được cấp quyền. Xem thêm [Xác thực](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type | string | Bắt buộc | Định dạng bản tin: `application/json`. |

### Tham số Body (Parameters)

| Field | Data Type | Bắt buộc | Description |
|---|---|---|---|
| advertiser_id | string | Bắt buộc | ID nhà quảng cáo. |
| object_type | string | Bắt buộc | Loại đối tượng: `CAMPAIGN` hoặc `ADGROUP`. |
| object_id | string | Bắt buộc | ID chiến dịch hoặc ID nhóm quảng cáo cần cập nhật từ khóa. |
| old_keyword_id | string | Bắt buộc | ID của từ khóa loại trừ cần cập nhật, lấy qua endpoint [/search_ad/negative_keyword/get/](53-negative-keywords.md#doc-1775104887052289). Nếu ID không tồn tại, hệ thống sẽ báo lỗi. |
| keyword | object | Bắt buộc | Thông tin cập nhật cho từ khóa gốc. |
| ↳ name | string | Bắt buộc | Tên mới của từ khóa loại trừ (tối đa 80 ký tự, không chứa ký tự đặc biệt cấm). Nếu chỉ muốn đổi loại đối sánh, hãy truyền lại tên cũ vào trường này. |
| ↳ match_type | string | Không | Loại đối sánh mới: `PRECISE_WORD`, `PHRASE_WORD`, `BROAD_WORD`. Mặc định: `BROAD_WORD`. |

### Phản hồi

| Field | Data Type | Description |
|---|---|---|
| code | number | Mã phản hồi API. `0` biểu thị thành công. Xem [Mã trả về (Return Code)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. |
| request_id | string | Mã nhật ký định danh duy nhất của yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ new_keyword_id | string | ID của từ khóa loại trừ sau khi cập nhật. |

### Ví dụ

#### cURL
```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/search_ad/negative_keyword/update/' \
--header 'Access-Token: act.example123456789' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id": "7123456789012345678",
    "object_type": "CAMPAIGN",
    "object_id": "1734945725409298",
    "old_keyword_id": "7198765432109876543",
    "keyword": {
        "name": "free trial",
        "match_type": "PRECISE_WORD"
    }
}'
```

#### Python
```python
import requests

ACCESS_TOKEN = "act.example123456789"
url = "https://business-api.tiktok.com/open_api/v1.3/search_ad/negative_keyword/update/"

headers = {
    "Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}

payload = {
    "advertiser_id": "7123456789012345678",
    "object_type": "CAMPAIGN",
    "object_id": "1734945725409298",
    "old_keyword_id": "7198765432109876543",
    "keyword": {
        "name": "free trial",
        "match_type": "PRECISE_WORD"
    }
}

response = requests.post(url, headers=headers, json=payload)
data = response.json()
print("ID từ khóa mới:", data.get("data", {}).get("new_keyword_id"))
```

---

## Xóa từ khóa loại trừ (`Delete negative keywords`)
<a id="doc-1775104910010369"></a>
<!-- doc_id: 1775104910010369 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/search_ad/negative_keyword/delete/`

**Mục đích**: Sử dụng endpoint này để xóa một hoặc nhiều từ khóa loại trừ đã cấu hình cho chiến dịch hoặc nhóm quảng cáo.

### Header

| Field | Data Type | Bắt buộc | Description |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Access token đã được cấp quyền. Xem thêm [Xác thực](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type | string | Bắt buộc | Định dạng bản tin: `application/json`. |

### Tham số Body (Parameters)

| Field | Data Type | Bắt buộc | Description |
|---|---|---|---|
| advertiser_id | string | Bắt buộc | ID nhà quảng cáo. |
| object_type | string | Bắt buộc | Loại đối tượng: `CAMPAIGN` hoặc `ADGROUP`. |
| object_id | string | Bắt buộc | ID chiến dịch hoặc ID nhóm quảng cáo cần xóa từ khóa loại trừ. |
| keyword_ids | string[] | Bắt buộc | Danh sách các ID từ khóa loại trừ cần xóa (tối đa 1.000 ID). Lấy ID qua [/search_ad/negative_keyword/get/](53-negative-keywords.md#doc-1775104887052289). Nếu bất kỳ ID nào không tồn tại, yêu cầu sẽ báo lỗi. |

### Phản hồi

| Field | Data Type | Description |
|---|---|---|
| code | number | Mã phản hồi API. `0` biểu thị thành công. Xem [Mã trả về (Return Code)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. |
| request_id | string | Mã nhật ký định danh duy nhất của yêu cầu. |
| data | object | Dữ liệu trả về (object rỗng `{}` khi thành công). |

### Ví dụ

#### cURL
```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/search_ad/negative_keyword/delete/' \
--header 'Access-Token: act.example123456789' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id": "7123456789012345678",
    "object_type": "CAMPAIGN",
    "object_id": "1734945725409298",
    "keyword_ids": ["7198765432109876543"]
}'
```

#### Python
```python
import requests

ACCESS_TOKEN = "act.example123456789"
url = "https://business-api.tiktok.com/open_api/v1.3/search_ad/negative_keyword/delete/"

headers = {
    "Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}

payload = {
    "advertiser_id": "7123456789012345678",
    "object_type": "CAMPAIGN",
    "object_id": "1734945725409298",
    "keyword_ids": ["7198765432109876543"]
}

response = requests.post(url, headers=headers, json=payload)
data = response.json()
print("Kết quả xóa từ khóa:", data.get("code"), data.get("message"))
```

---

## Tải xuống danh sách từ khóa loại trừ (`Download negative keywords`)
<a id="doc-1775104916876290"></a>
<!-- doc_id: 1775104916876290 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/search_ad/negative_keyword/download/`

**Mục đích**: Sử dụng endpoint này để xuất và tải xuống toàn bộ danh sách từ khóa loại trừ của một chiến dịch hoặc nhóm quảng cáo dưới dạng tệp tin Excel (.xlsx).

### Header

| Field | Data Type | Bắt buộc | Description |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Access token đã được cấp quyền. Xem thêm [Xác thực](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (Query string)

| Field | Data Type | Bắt buộc | Description |
|---|---|---|---|
| advertiser_id | string | Bắt buộc | ID nhà quảng cáo. |
| object_type | string | Bắt buộc | Loại đối tượng: `CAMPAIGN` hoặc `ADGROUP`. |
| object_id | string | Bắt buộc | ID chiến dịch hoặc ID nhóm quảng cáo cần tải danh sách từ khóa loại trừ. |

### Phản hồi

Nếu tải xuống thành công, API sẽ trả về luồng dữ liệu file nhị phân (binary stream) định dạng `.xlsx`. File tải về bao gồm 3 cột: ID từ khóa, tên từ khóa và loại đối sánh.

Nếu cuộc gọi thất bại, hệ thống sẽ trả về định dạng JSON lỗi chuẩn:

| Field | Data Type | Description |
|---|---|---|
| code | number | Mã lỗi phản hồi. Xem [Mã trả về (Return Code)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo lỗi chi tiết. |
| request_id | string | Mã nhật ký định danh duy nhất của yêu cầu. |
| data | object | Dữ liệu trả về. |

### Ví dụ

#### cURL
```bash
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/search_ad/negative_keyword/download/?advertiser_id=7123456789012345678&object_type=CAMPAIGN&object_id=1734945725409298' \
--header 'Access-Token: act.example123456789' \
--output negative_keywords.xlsx
```

#### Python
```python
import requests

ACCESS_TOKEN = "act.example123456789"
ADVERTISER_ID = "7123456789012345678"
CAMPAIGN_ID = "1734945725409298"
url = "https://business-api.tiktok.com/open_api/v1.3/search_ad/negative_keyword/download/"

params = {
    "advertiser_id": ADVERTISER_ID,
    "object_type": "CAMPAIGN",
    "object_id": CAMPAIGN_ID
}

headers = {
    "Access-Token": ACCESS_TOKEN
}

response = requests.get(url, headers=headers, params=params)

if response.status_code == 200 and "application/json" not in response.headers.get("Content-Type", ""):
    with open("negative_keywords.xlsx", "wb") as f:
        f.write(response.content)
    print("Đã tải thành công tệp negative_keywords.xlsx")
else:
    print("Tải thất bại:", response.json())
```
