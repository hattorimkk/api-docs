# Khách hàng tiềm năng (Leads)
<a id="doc-1739047069984834"></a>
<!-- doc_id: 1739047069984834 -->

Tạo khách hàng tiềm năng (Lead generation) là quy trình xác định và thu hút các khách hàng tiềm năng cho sản phẩm hoặc dịch vụ của doanh nghiệp. Quá trình này được thực hiện khi khách hàng tiềm năng gửi thông tin liên hệ của họ cho doanh nghiệp thông qua Biểu mẫu tức thì (Instant Form) hoặc Tin nhắn trực tiếp (Direct Message) trên TikTok. 

Bộ Leads API cho phép bạn thực hiện kiểm thử toàn trình (end-to-end testing) cho tính năng tạo khách hàng tiềm năng, tải xuống danh sách khách hàng tiềm năng, đăng ký nhận webhook thông báo real-time, di chuyển dữ liệu khách hàng tiềm năng vào Business Center và trích xuất danh sách các trường của biểu mẫu.

Xem thêm [Lead generation](../08-use-cases/use-case-lead-generation.md#doc-1739289524101122) để tìm hiểu cách tải xuống khách hàng tiềm năng cũng như tạo và kiểm thử đăng ký webhook.

Nhóm API này bao gồm các endpoint sau:

**Kiểm thử khách hàng tiềm năng (Testing leads)**
* [Tạo khách hàng tiềm năng thử nghiệm](48-leads.md#doc-1739047132614722)
* [Lấy thông tin khách hàng tiềm năng thử nghiệm](48-leads.md#doc-1739048460493826)
* [Xóa khách hàng tiềm năng thử nghiệm](48-leads.md#doc-1739049313198081)

**Tải xuống khách hàng tiềm năng (Downloading leads)**
* [Tạo tác vụ tải xuống khách hàng tiềm năng](48-leads.md#doc-1739052936772610)
* [Tải xuống danh sách khách hàng tiềm năng](48-leads.md#doc-1739053563877378)

**Di chuyển dữ liệu (Leads migration)**
* [Di chuyển khách hàng tiềm năng vào Business Center](48-leads.md#doc-1740029931324417)
* [Lấy danh sách thư viện biểu mẫu](48-leads.md#doc-1740029915327489)

**Trích xuất trường và dữ liệu khách hàng tiềm năng (Get fields or leads)**
* [Lấy các trường của Biểu mẫu tức thì](48-leads.md#doc-1739054080455681)
* [Lấy các trường của Biểu mẫu tức thì hoặc tin nhắn trực tiếp](48-leads.md#doc-1832112377641026)
* [Lấy khách hàng tiềm năng từ Biểu mẫu tức thì hoặc tin nhắn trực tiếp](48-leads.md#doc-1832112833212434)

---

## Tạo khách hàng tiềm năng thử nghiệm (`Create a test lead`)
<a id="doc-1739047132614722"></a>
<!-- doc_id: 1739047132614722 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/page/lead/mock/create/`

**Mục đích**: Sử dụng endpoint này để thực hiện kiểm thử toàn trình (end-to-end) cho tính năng thu thập khách hàng tiềm năng mà không cần tạo quảng cáo thực tế.

> [!NOTE]
> Đối với mỗi Biểu mẫu tức thì (Instant Form), bạn chỉ có thể tạo một khách hàng tiềm năng thử nghiệm tại một thời điểm. Nếu cần tạo khách hàng tiềm năng thử nghiệm mới, bạn phải xóa khách hàng tiềm năng thử nghiệm hiện có bằng [/page/lead/mock/delete/](48-leads.md#doc-1739049313198081) trước. Nếu chỉ muốn lấy thông tin các trường của biểu mẫu, hãy gọi [/page/field/get/](48-leads.md#doc-1739054080455681) trực tiếp.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền (access token). Xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type | string | Bắt buộc | Loại nội dung của yêu cầu. Sử dụng `application/json`. |

### Tham số (POST JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| lead_source | string | Không | Nguồn của khách hàng tiềm năng. Các giá trị enum:<br>• `INSTANT_FORM`: Khách hàng tiềm năng được tạo qua Biểu mẫu tức thì.<br>• `DIRECT_MESSAGE`: Khách hàng tiềm năng thu thập từ tin nhắn trực tiếp của Tài khoản doanh nghiệp liên kết.<br>Giá trị mặc định: `INSTANT_FORM`. |
| advertiser_id | string | Có điều kiện | Bắt buộc khi muốn tạo khách hàng tiềm năng thử nghiệm thuộc tài khoản quảng cáo. ID nhà quảng cáo (Advertiser ID).<br>**Lưu ý**: Bạn phải là Quản trị viên (Admin) của tài khoản quảng cáo. Để lấy danh sách tài khoản bạn có quyền Admin, gọi [/bc/asset/get/](15-bc-assets.md#doc-1739432717798401) với `asset_type` là `ADVERTISER`. |
| library_id | string | Có điều kiện | Bắt buộc khi muốn tạo khách hàng tiềm năng thử nghiệm trong thư viện biểu mẫu của Business Center. ID thư viện biểu mẫu. Lấy danh sách qua [/page/library/get/](48-leads.md#doc-1740029915327489). |
| page_id | string | Có điều kiện | • Bắt buộc khi `lead_source` là `INSTANT_FORM` hoặc không chỉ định.<br>• Không hỗ trợ khi `lead_source` là `DIRECT_MESSAGE`.<br>ID trang của Biểu mẫu tức thì. Lấy danh sách qua [/page/get/](54-page.md#doc-1820826387779586) với `business_type`=`LEAD_GEN`. |

### Ví dụ

#### cURL
```bash
curl -H "Access-Token: YOUR_ACCESS_TOKEN" \
     -H "Content-Type: application/json" \
     -X POST \
     -d '{
       "advertiser_id": "7123456789012345678",
       "page_id": "6856667798307864597",
       "lead_source": "INSTANT_FORM"
     }' \
     https://business-api.tiktok.com/open_api/v1.3/page/lead/mock/create/
```

#### Python
```python
import os
import requests

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", "YOUR_ACCESS_TOKEN")
ADVERTISER_ID = os.environ.get("ADVERTISER_ID", "7123456789012345678")
PAGE_ID = "6856667798307864597"

url = "https://business-api.tiktok.com/open_api/v1.3/page/lead/mock/create/"
headers = {
    "Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}
payload = {
    "advertiser_id": ADVERTISER_ID,
    "page_id": PAGE_ID,
    "lead_source": "INSTANT_FORM"
}

response = requests.post(url, headers=headers, json=payload)
data = response.json()
print("Lead ID:", data.get("data", {}).get("meta_data", {}).get("lead_id"))
```

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi. Giá trị `0` biểu thị thành công. Xem [Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi từ hệ thống. |
| request_id | string | Mã log duy nhất định danh cho yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ lead_data | object | Dữ liệu chi tiết của khách hàng tiềm năng (chứa các câu trả lời dựa trên biểu mẫu). |
| ↳ meta_data | object | Siêu dữ liệu về khách hàng tiềm năng. |
| ↳↳ lead_source | string | Nguồn khách hàng tiềm năng (`INSTANT_FORM` hoặc `DIRECT_MESSAGE`). |
| ↳↳ lead_id | string | ID khách hàng tiềm năng thử nghiệm. |
| ↳↳ advertiser_id | string | ID nhà quảng cáo. |
| ↳↳ library_id | string | ID thư viện biểu mẫu. |
| ↳↳ page_id | string | ID trang của Biểu mẫu tức thì. |
| ↳↳ campaign_id | string | ID chiến dịch (nếu có). |
| ↳↳ campaign_name | string | Tên chiến dịch (nếu có). |
| ↳↳ adgroup_id | string | ID nhóm quảng cáo (nếu có). |
| ↳↳ adgroup_name | string | Tên nhóm quảng cáo (nếu có). |
| ↳↳ ad_id | string | ID quảng cáo (nếu có). |
| ↳↳ ad_name | string | Tên quảng cáo (nếu có). |
| ↳↳ create_time | string | Thời gian tạo lead, định dạng `YYYY-MM-DD HH:MM:SS` (giờ UTC+0). |

### Ví dụ phản hồi

```json
{
  "code": 0,
  "message": "OK",
  "data": {
    "lead_data": {
      "email": "test@example.com",
      "name": "Nguyễn Văn A",
      "phone_number": "+84901234567"
    },
    "meta_data": {
      "ad_id": "0",
      "ad_name": "Test Ad",
      "adgroup_id": "0",
      "adgroup_name": "Test Ad Group",
      "advertiser_id": "7123456789012345678",
      "campaign_id": "0",
      "campaign_name": "Test Campaign",
      "create_time": "2026-03-20 08:30:00",
      "lead_id": "6864523782069944581",
      "lead_source": "INSTANT_FORM",
      "page_id": "6856667798307864597"
    }
  },
  "request_id": "202603200830000101890492231E063EE3"
}
```

---

## Lấy thông tin khách hàng tiềm năng thử nghiệm (`Get a test lead`)
<a id="doc-1739048460493826"></a>
<!-- doc_id: 1739048460493826 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/page/lead/mock/get/`

**Mục đích**: Sử dụng endpoint này để truy vấn lại thông tin của khách hàng tiềm năng thử nghiệm đã tạo trước đó.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền (access token). Xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (GET query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| lead_source | string | Không | Nguồn của lead (`INSTANT_FORM` hoặc `DIRECT_MESSAGE`). Mặc định: `INSTANT_FORM`. |
| advertiser_id | string | Có điều kiện | Bắt buộc nếu lead thuộc tài khoản quảng cáo. ID nhà quảng cáo. |
| library_id | string | Có điều kiện | Bắt buộc nếu lead thuộc thư viện biểu mẫu của Business Center. ID thư viện biểu mẫu. |
| page_id | string | Có điều kiện | • Bắt buộc khi `lead_source` là `INSTANT_FORM`.<br>• Không hỗ trợ khi `lead_source` là `DIRECT_MESSAGE`.<br>ID trang của Biểu mẫu tức thì. |

### Ví dụ

#### cURL
```bash
curl --get -H "Access-Token: YOUR_ACCESS_TOKEN" \
  --data-urlencode "advertiser_id=7123456789012345678" \
  --data-urlencode "page_id=6856667798307864597" \
  --data-urlencode "lead_source=INSTANT_FORM" \
  https://business-api.tiktok.com/open_api/v1.3/page/lead/mock/get/
```

#### Python
```python
import os
import requests

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", "YOUR_ACCESS_TOKEN")
ADVERTISER_ID = os.environ.get("ADVERTISER_ID", "7123456789012345678")
PAGE_ID = "6856667798307864597"

url = "https://business-api.tiktok.com/open_api/v1.3/page/lead/mock/get/"
headers = {"Access-Token": ACCESS_TOKEN}
params = {
    "advertiser_id": ADVERTISER_ID,
    "page_id": PAGE_ID,
    "lead_source": "INSTANT_FORM"
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi. Giá trị `0` biểu thị thành công. |
| message | string | Thông báo phản hồi. |
| request_id | string | Mã log định danh yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ lead_data | object | Dữ liệu chi tiết của khách hàng tiềm năng. |
| ↳ meta_data | object | Siêu dữ liệu về khách hàng tiềm năng. |
| ↳↳ lead_source | string | Nguồn khách hàng tiềm năng. |
| ↳↳ lead_id | string | ID khách hàng tiềm năng. |
| ↳↳ advertiser_id | string | ID nhà quảng cáo. |
| ↳↳ library_id | string | ID thư viện biểu mẫu. |
| ↳↳ page_id | string | ID trang của Biểu mẫu tức thì. |
| ↳↳ campaign_id | string | ID chiến dịch. |
| ↳↳ campaign_name | string | Tên chiến dịch. |
| ↳↳ adgroup_id | string | ID nhóm quảng cáo. |
| ↳↳ adgroup_name | string | Tên nhóm quảng cáo. |
| ↳↳ ad_id | string | ID quảng cáo. |
| ↳↳ ad_name | string | Tên quảng cáo. |
| ↳↳ create_time | string | Thời gian tạo lead, định dạng `YYYY-MM-DD HH:MM:SS` (UTC+0). |

---

## Xóa khách hàng tiềm năng thử nghiệm (`Delete a test lead`)
<a id="doc-1739049313198081"></a>
<!-- doc_id: 1739049313198081 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/page/lead/mock/delete/`

**Mục đích**: Sử dụng endpoint này để xóa một khách hàng tiềm năng thử nghiệm hiện có nhằm giải phóng biểu mẫu để thực hiện các bài kiểm thử tiếp theo.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền (access token). |
| Content-Type | string | Bắt buộc | Loại nội dung. Sử dụng `application/json`. |

### Tham số (POST JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| lead_id | string | Bắt buộc | ID của khách hàng tiềm năng thử nghiệm cần xóa. |
| advertiser_id | string | Có điều kiện | Bắt buộc nếu lead thuộc tài khoản quảng cáo. ID nhà quảng cáo. |
| library_id | string | Có điều kiện | Bắt buộc nếu lead thuộc thư viện biểu mẫu của Business Center. ID thư viện biểu mẫu. |

### Ví dụ

#### cURL
```bash
curl -H "Access-Token: YOUR_ACCESS_TOKEN" \
     -H "Content-Type: application/json" \
     -X POST \
     -d '{
       "advertiser_id": "7123456789012345678",
       "lead_id": "6864523782069944581"
     }' \
     https://business-api.tiktok.com/open_api/v1.3/page/lead/mock/delete/
```

#### Python
```python
import os
import requests

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", "YOUR_ACCESS_TOKEN")
ADVERTISER_ID = os.environ.get("ADVERTISER_ID", "7123456789012345678")
LEAD_ID = "6864523782069944581"

url = "https://business-api.tiktok.com/open_api/v1.3/page/lead/mock/delete/"
headers = {
    "Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}
payload = {
    "advertiser_id": ADVERTISER_ID,
    "lead_id": LEAD_ID
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())
```

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi. Giá trị `0` biểu thị thành công. |
| message | string | Thông báo phản hồi. |
| request_id | string | Mã log định danh yêu cầu. |
| data | object | Đối tượng rỗng khi xóa thành công. |

---

## Tạo tác vụ tải xuống khách hàng tiềm năng (`Create a lead download task`)
<a id="doc-1739052936772610"></a>
<!-- doc_id: 1739052936772610 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/page/lead/task/` hoặc `GET` `https://business-api.tiktok.com/open_api/v1.3/page/lead/task/`

**Mục đích**: 
- Dùng phương thức **POST** để tạo tác vụ xuất danh sách khách hàng tiềm năng cho `page_id` hoặc `ad_id` cụ thể.
- Dùng phương thức **GET** để kiểm tra trạng thái và tiến độ hoàn thành của tác vụ tải xuống.

> [!NOTE]
> Chỉ Quản trị viên (Admin) của tài khoản quảng cáo hoặc Business Center mới có quyền tạo và truy vấn tác vụ tải xuống khách hàng tiềm năng.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền. |

### Tham số POST (Tạo tác vụ)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| advertiser_id | string | Có điều kiện | Bắt buộc nếu lead thuộc tài khoản quảng cáo. ID nhà quảng cáo. |
| library_id | string | Có điều kiện | Bắt buộc nếu lead thuộc thư viện biểu mẫu của Business Center. ID thư viện biểu mẫu. |
| page_id | string | Có điều kiện | ID trang của Biểu mẫu tức thì. |
| ad_id | string | Có điều kiện | ID quảng cáo cần tải danh sách lead. |

### Tham số GET (Kiểm tra trạng thái tác vụ)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| advertiser_id | string | Có điều kiện | ID nhà quảng cáo. |
| library_id | string | Có điều kiện | ID thư viện biểu mẫu. |
| task_id | string | Bắt buộc | ID của tác vụ tải xuống cần kiểm tra trạng thái. |

### Ví dụ

#### cURL (Tạo tác vụ)
```bash
curl -H "Access-Token: YOUR_ACCESS_TOKEN" \
     -H "Content-Type: application/json" \
     -X POST \
     -d '{
       "advertiser_id": "7123456789012345678",
       "page_id": "6856667798307864597"
     }' \
     https://business-api.tiktok.com/open_api/v1.3/page/lead/task/
```

#### cURL (Kiểm tra trạng thái tác vụ)
```bash
curl --get -H "Access-Token: YOUR_ACCESS_TOKEN" \
  --data-urlencode "advertiser_id=7123456789012345678" \
  --data-urlencode "task_id=7012345678901234567" \
  https://business-api.tiktok.com/open_api/v1.3/page/lead/task/
```

#### Python
```python
import os
import requests

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", "YOUR_ACCESS_TOKEN")
ADVERTISER_ID = os.environ.get("ADVERTISER_ID", "7123456789012345678")
PAGE_ID = "6856667798307864597"

headers = {"Access-Token": ACCESS_TOKEN}

# 1. Tạo tác vụ tải xuống
create_url = "https://business-api.tiktok.com/open_api/v1.3/page/lead/task/"
res = requests.post(create_url, headers=headers, json={"advertiser_id": ADVERTISER_ID, "page_id": PAGE_ID})
task_id = res.json().get("data", {}).get("task_id")
print("Đã tạo task:", task_id)

# 2. Kiểm tra trạng thái tác vụ
status_res = requests.get(create_url, headers=headers, params={"advertiser_id": ADVERTISER_ID, "task_id": task_id})
status_data = status_res.json().get("data", {})
print("Trạng thái task:", status_data.get("status"), "| Tệp:", status_data.get("file_name"))
```

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi API (`0` là thành công). |
| message | string | Thông báo phản hồi. |
| request_id | string | Mã nhật ký định danh yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ task_id | string | ID của tác vụ tải xuống. |
| ↳ status | string | Trạng thái tác vụ: `PROCESSING`, `RUNNING`, `SUCCEED`, `FAILED`. |
| ↳ file_name | string | Tên tệp dữ liệu lead (chỉ trả về khi `status` là `SUCCEED`). |
| ↳ file_type | string | Định dạng tệp dữ liệu (`csv` hoặc `zip`, chỉ trả về khi `status`=`SUCCEED`). |

---

## Tải xuống danh sách khách hàng tiềm năng (`Download leads`)
<a id="doc-1739053563877378"></a>
<!-- doc_id: 1739053563877378 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/page/lead/task/download/`

**Mục đích**: Sử dụng endpoint này để tải về tệp dữ liệu khách hàng tiềm năng thực tế sau khi tác vụ tải xuống đã hoàn thành thành công (`status` = `SUCCEED`).

> [!IMPORTANT]
> **Quy định về khu vực dữ liệu (Data Residency Headers)**:
> - **Khu vực Châu Âu (EEA / CH / UK)**: Sử dụng URL `https://business-api.tiktok.com/open_api/v1.3/page/lead/task/download/` và bắt buộc thêm header `x-lead-region: eu`.
> - **Khu vực Hoa Kỳ (US)**: Sử dụng URL trên với header `x-lead-region: us`.
> - **Các quốc gia và khu vực khác**: Gọi trực tiếp tới URL tiêu chuẩn mà không cần chỉ định header khu vực.
>
> Nếu cuộc gọi thành công, dữ liệu trả về ở định dạng CSV nhị phân trực tiếp (tối đa 10MB) hoặc tệp ZIP nén. Nếu xảy ra lỗi, phản hồi sẽ trả về định dạng JSON chứa mã lỗi.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền. |
| x-lead-region | string | Có điều kiện | Chỉ định khu vực dữ liệu: `eu` hoặc `us`. |

### Tham số (GET query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| task_id | string | Bắt buộc | ID tác vụ tải xuống đã hoàn tất thành công. |
| advertiser_id | string | Có điều kiện | Bắt buộc nếu lead thuộc tài khoản quảng cáo. |
| library_id | string | Có điều kiện | Bắt buộc nếu lead thuộc thư viện biểu mẫu của Business Center. |

### Ví dụ

#### cURL
```bash
curl --get \
  -H "Access-Token: YOUR_ACCESS_TOKEN" \
  -H "x-lead-region: eu" \
  --data-urlencode "advertiser_id=7123456789012345678" \
  --data-urlencode "task_id=7012345678901234567" \
  --output leads_data.csv \
  https://business-api.tiktok.com/open_api/v1.3/page/lead/task/download/
```

#### Python
```python
import os
import requests

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", "YOUR_ACCESS_TOKEN")
ADVERTISER_ID = os.environ.get("ADVERTISER_ID", "7123456789012345678")
TASK_ID = "7012345678901234567"

url = "https://business-api.tiktok.com/open_api/v1.3/page/lead/task/download/"
headers = {
    "Access-Token": ACCESS_TOKEN,
    # "x-lead-region": "eu" # Thêm nếu tải dữ liệu lead khu vực Châu Âu
}
params = {
    "advertiser_id": ADVERTISER_ID,
    "task_id": TASK_ID
}

response = requests.get(url, headers=headers, params=params, stream=True)

if response.status_code == 200 and "application/json" not in response.headers.get("Content-Type", ""):
    output_filename = "downloaded_leads.csv"
    with open(output_filename, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    print(f"Tải tệp lead thành công: {output_filename}")
else:
    print("Lỗi tải tệp:", response.json())
```

### Ví dụ phản hồi

**Khi thành công (Nội dung tệp CSV):**
```csv
lead id,created_time,ad_id,ad_name,adgroup_id,adgroup_name,campaign_id,campaign_name,form_id,form_name,Name,Phone number,Email
6864523782069944581,2026-03-20 08:30:11(UTC+00:00),1674635134905355,Ad_01,1674635100000000,AdGroup_01,1674635000000000,Campaign_01,6856667798307864597,Form Đăng Ký,Nguyễn Văn A,+84901234567,nguyenvana@example.com
```

**Khi thất bại (JSON Error):**
```json
{
  "code": 40000,
  "message": "failed to download.",
  "data": {}
}
```


---

## Lấy danh sách thư viện biểu mẫu (`Get form libraries`)
<a id="doc-1740029915327489"></a>
<!-- doc_id: 1740029915327489 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/page/library/get/`

**Mục đích**: Sử dụng endpoint này để lấy danh sách các thư viện biểu mẫu (form libraries) mà bạn có quyền truy cập. Thư viện biểu mẫu là vùng chứa dữ liệu khách hàng tiềm năng thuộc một Business Center.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền. |

### Tham số (GET query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| page | number | Không | Số trang cần lấy. Mặc định: `1`. |
| page_size | number | Không | Số bản ghi trên mỗi trang. Mặc định: `10`. |

### Ví dụ

#### cURL
```bash
curl --get -H "Access-Token: YOUR_ACCESS_TOKEN" \
  --data-urlencode "page=1" \
  --data-urlencode "page_size=20" \
  https://business-api.tiktok.com/open_api/v1.3/page/library/get/
```

#### Python
```python
import os
import requests

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", "YOUR_ACCESS_TOKEN")

url = "https://business-api.tiktok.com/open_api/v1.3/page/library/get/"
headers = {"Access-Token": ACCESS_TOKEN}
params = {"page": 1, "page_size": 20}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi API. |
| message | string | Thông báo phản hồi. |
| request_id | string | Mã log yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ list | object[] | Danh sách các thư viện biểu mẫu. |
| ↳↳ library_id | string | ID thư viện biểu mẫu. |
| ↳↳ library_name | string | Tên thư viện biểu mẫu. |
| ↳↳ advertiser_id | string | ID nhà quảng cáo sở hữu. |
| ↳↳ create_time | string | Thời gian tạo thư viện (`YYYY-MM-DD HH:MM:SS`). |
| ↳↳ update_time | string | Thời gian cập nhật gần nhất. |

---

## Di chuyển khách hàng tiềm năng vào Business Center (`Migrate leads to a BC`)
<a id="doc-1740029931324417"></a>
<!-- doc_id: 1740029931324417 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/page/library/transfer/`

**Mục đích**: Sử dụng endpoint này để di chuyển dữ liệu khách hàng tiềm năng từ một tài khoản nhà quảng cáo vào một Business Center. Trong quá trình di chuyển, hệ thống sẽ tự động tạo một thư viện biểu mẫu mới trong Business Center để lưu trữ các khách hàng tiềm năng này.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền. |
| Content-Type | string | Bắt buộc | Loại nội dung. Sử dụng `application/json`. |

### Tham số (POST JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| advertiser_id | string | Bắt buộc | ID của nhà quảng cáo sở hữu dữ liệu khách hàng tiềm năng. |
| bc_id | string | Bắt buộc | ID của Business Center đích mà bạn muốn di chuyển khách hàng tiềm năng vào. |

### Ví dụ

#### cURL
```bash
curl -H "Access-Token: YOUR_ACCESS_TOKEN" \
     -H "Content-Type: application/json" \
     -X POST \
     -d '{
       "advertiser_id": "7123456789012345678",
       "bc_id": "7012345678901234567"
     }' \
     https://business-api.tiktok.com/open_api/v1.3/page/library/transfer/
```

#### Python
```python
import os
import requests

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", "YOUR_ACCESS_TOKEN")
ADVERTISER_ID = os.environ.get("ADVERTISER_ID", "7123456789012345678")
BC_ID = "7012345678901234567"

url = "https://business-api.tiktok.com/open_api/v1.3/page/library/transfer/"
headers = {
    "Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}
payload = {
    "advertiser_id": ADVERTISER_ID,
    "bc_id": BC_ID
}

response = requests.post(url, headers=headers, json=payload)
data = response.json()
print("Thư viện biểu mẫu mới tạo:", data.get("data", {}).get("library_id"))
```

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi API. |
| message | string | Thông báo phản hồi. |
| request_id | string | Mã log yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ library_id | string | ID của thư viện biểu mẫu vừa được tạo ra trong Business Center. |

---

## Lấy các trường của Biểu mẫu tức thì (`Get the fields of an Instant Form`)
<a id="doc-1739054080455681"></a>
<!-- doc_id: 1739054080455681 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/page/field/get/`

**Mục đích**: Sử dụng endpoint này để trích xuất danh sách các trường câu hỏi và thông tin trong một Biểu mẫu tức thì (Instant Form).

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền. |
| Content-Type | string | Bắt buộc | `application/json`. |

### Tham số (GET query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| page_id | string | Bắt buộc | ID trang của Biểu mẫu tức thì. |
| advertiser_id | string | Không | ID nhà quảng cáo. |

### Ví dụ

#### cURL
```bash
curl --get -H "Access-Token: YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  --data-urlencode "advertiser_id=7123456789012345678" \
  --data-urlencode "page_id=6856667798307864597" \
  https://business-api.tiktok.com/open_api/v1.3/page/field/get/
```

#### Python
```python
import os
import requests

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", "YOUR_ACCESS_TOKEN")
ADVERTISER_ID = os.environ.get("ADVERTISER_ID", "7123456789012345678")
PAGE_ID = "6856667798307864597"

url = "https://business-api.tiktok.com/open_api/v1.3/page/field/get/"
headers = {
    "Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}
params = {
    "advertiser_id": ADVERTISER_ID,
    "page_id": PAGE_ID
}

response = requests.get(url, headers=headers, params=params)
data = response.json()
print("Tên form:", data.get("data", {}).get("meta_data", {}).get("page_name"))
print("Danh sách trường câu hỏi:", data.get("data", {}).get("fields"))
```

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi API. |
| message | string | Thông báo phản hồi. |
| request_id | string | Mã log định danh yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ fields | object[] | Danh sách các trường dữ liệu được thu thập trong biểu mẫu. |
| ↳ meta_data | object | Siêu dữ liệu về biểu mẫu. |
| ↳↳ page_id | string | ID trang của Biểu mẫu tức thì. |
| ↳↳ page_name | string | Tên của Biểu mẫu tức thì. |
| ↳↳ page_url | string | Đường dẫn URL của biểu mẫu. |
| ↳↳ create_time | string | Thời gian tạo biểu mẫu (`YYYY-MM-DD HH:MM:SS`). |

---

## Lấy các trường của Biểu mẫu tức thì hoặc tin nhắn trực tiếp (`Get fields of an Instant Form or direct message leads`)
<a id="doc-1832112377641026"></a>
<!-- doc_id: 1832112377641026 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/lead/field/get/`

**Mục đích**: Endpoint thế hệ mới cho phép trích xuất các trường thông tin được định nghĩa trong Biểu mẫu tức thì hoặc trong luồng thu thập khách hàng tiềm năng qua Tin nhắn trực tiếp (Direct Message).

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền. |

### Tham số (GET query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| lead_source | string | Bắt buộc | Nguồn của lead (`INSTANT_FORM` hoặc `DIRECT_MESSAGE`). |
| advertiser_id | string | Có điều kiện | Bắt buộc nếu lead thuộc tài khoản quảng cáo. ID nhà quảng cáo. |
| library_id | string | Có điều kiện | Bắt buộc nếu lead thuộc thư viện biểu mẫu Business Center. |
| page_id | string | Có điều kiện | • Bắt buộc khi `lead_source` là `INSTANT_FORM`.<br>• Không hỗ trợ khi `lead_source` là `DIRECT_MESSAGE`.<br>ID trang của Biểu mẫu tức thì. |

### Ví dụ

#### cURL
```bash
curl --get -H "Access-Token: YOUR_ACCESS_TOKEN" \
  --data-urlencode "lead_source=INSTANT_FORM" \
  --data-urlencode "advertiser_id=7123456789012345678" \
  --data-urlencode "page_id=6856667798307864597" \
  https://business-api.tiktok.com/open_api/v1.3/lead/field/get/
```

#### Python
```python
import os
import requests

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", "YOUR_ACCESS_TOKEN")
ADVERTISER_ID = os.environ.get("ADVERTISER_ID", "7123456789012345678")
PAGE_ID = "6856667798307864597"

url = "https://business-api.tiktok.com/open_api/v1.3/lead/field/get/"
headers = {"Access-Token": ACCESS_TOKEN}
params = {
    "lead_source": "INSTANT_FORM",
    "advertiser_id": ADVERTISER_ID,
    "page_id": PAGE_ID
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi API. |
| message | string | Thông báo phản hồi. |
| request_id | string | Mã log định danh yêu cầu. |
| data | object | Dữ liệu trả về chứa danh sách định nghĩa trường. |

---

## Lấy khách hàng tiềm năng từ Biểu mẫu tức thì hoặc tin nhắn trực tiếp (`Get an Instant Form lead or a direct message lead`)
<a id="doc-1832112833212434"></a>
<!-- doc_id: 1832112833212434 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/lead/get/`

**Mục đích**: Sử dụng endpoint này để lấy trực tiếp dữ liệu chi tiết của khách hàng tiềm năng từ Biểu mẫu tức thì hoặc Tin nhắn trực tiếp theo thời gian thực.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền. |

### Tham số (GET query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| lead_source | string | Bắt buộc | Nguồn của lead (`INSTANT_FORM` hoặc `DIRECT_MESSAGE`). |
| advertiser_id | string | Có điều kiện | Bắt buộc nếu lead thuộc tài khoản quảng cáo. ID nhà quảng cáo. |
| library_id | string | Có điều kiện | Bắt buộc nếu lead thuộc thư viện biểu mẫu Business Center. |
| page_id | string | Có điều kiện | • Bắt buộc khi `lead_source` là `INSTANT_FORM`.<br>• Không hỗ trợ khi `lead_source` là `DIRECT_MESSAGE`.<br>ID trang của Biểu mẫu tức thì. |

### Ví dụ

#### cURL (Lấy lead từ Biểu mẫu tức thì)
```bash
curl --get -H "Access-Token: YOUR_ACCESS_TOKEN" \
  --data-urlencode "lead_source=INSTANT_FORM" \
  --data-urlencode "advertiser_id=7123456789012345678" \
  --data-urlencode "page_id=6856667798307864597" \
  https://business-api.tiktok.com/open_api/v1.3/lead/get/
```

#### cURL (Lấy lead từ Tin nhắn trực tiếp)
```bash
curl --get -H "Access-Token: YOUR_ACCESS_TOKEN" \
  --data-urlencode "lead_source=DIRECT_MESSAGE" \
  --data-urlencode "advertiser_id=7123456789012345678" \
  https://business-api.tiktok.com/open_api/v1.3/lead/get/
```

#### Python
```python
import os
import requests

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", "YOUR_ACCESS_TOKEN")
ADVERTISER_ID = os.environ.get("ADVERTISER_ID", "7123456789012345678")
PAGE_ID = "6856667798307864597"

url = "https://business-api.tiktok.com/open_api/v1.3/lead/get/"
headers = {"Access-Token": ACCESS_TOKEN}
params = {
    "lead_source": "INSTANT_FORM",
    "advertiser_id": ADVERTISER_ID,
    "page_id": PAGE_ID
}

response = requests.get(url, headers=headers, params=params)
data = response.json()
print("Lead Data:", data.get("data", {}).get("lead_data"))
print("Metadata:", data.get("data", {}).get("meta_data"))
```

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi API. |
| message | string | Thông báo phản hồi. |
| request_id | string | Mã log định danh yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ lead_data | object | Dữ liệu chi tiết do khách hàng cung cấp (email, name, phone_number, v.v.). |
| ↳ meta_data | object | Siêu dữ liệu liên kết với khách hàng tiềm năng. |
| ↳↳ lead_source | string | Nguồn (`INSTANT_FORM` hoặc `DIRECT_MESSAGE`). |
| ↳↳ lead_id | string | ID khách hàng tiềm năng. |
| ↳↳ page_id | string | ID trang của Biểu mẫu tức thì (chỉ trả về khi `lead_source`=`INSTANT_FORM`). |
| ↳↳ campaign_id | string | ID chiến dịch quảng cáo. |
| ↳↳ campaign_name | string | Tên chiến dịch quảng cáo. |
| ↳↳ adgroup_id | string | ID nhóm quảng cáo. |
| ↳↳ adgroup_name | string | Tên nhóm quảng cáo. |
| ↳↳ ad_id | string | ID quảng cáo. |
| ↳↳ ad_name | string | Tên quảng cáo. |
| ↳↳ create_time | string | Thời gian tạo lead (`YYYY-MM-DD HH:MM:SS` UTC+0). |

### Ví dụ phản hồi

```json
{
  "code": 0,
  "message": "OK",
  "data": {
    "lead_data": {
      "email": "customer@example.com",
      "name": "Trần Thị B",
      "phone_number": "+84912345678"
    },
    "meta_data": {
      "ad_id": "1674635134905355",
      "ad_name": "Summer Promotion Ad",
      "adgroup_id": "1674635100000000",
      "adgroup_name": "Summer Audience",
      "campaign_id": "1674635000000000",
      "campaign_name": "Summer Campaign",
      "create_time": "2026-03-20 09:15:30",
      "lead_id": "6864523782069944582",
      "lead_source": "INSTANT_FORM",
      "page_id": "6856667798307864597"
    }
  },
  "request_id": "202603200915300101890492231E063EE4"
}
```
