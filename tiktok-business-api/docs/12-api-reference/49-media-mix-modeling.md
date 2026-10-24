# Media Mix Modeling (MMM)
<a id="doc-1825299463225345"></a>
<!-- doc_id: 1825299463225345 -->

Media Mix Modeling (MMM - Mô hình hóa phối thức truyền thông) là một kỹ thuật đo lường sử dụng mô hình chuỗi thời gian (time-series modeling) để hiểu rõ tác động kinh doanh của tất cả các điểm chạm tiếp thị truyền thống và kỹ thuật số. Bằng cách tính đến các yếu tố vận hành như định giá, các yếu tố môi trường bên ngoài và các chỉ số kinh tế vĩ mô, MMM giúp định lượng lợi tức đầu tư (ROI) trên toàn bộ các kênh truyền thông của nhà quảng cáo và cung cấp thông tin chuyên sâu để lập kế hoạch chi tiêu truyền thông trong tương lai.

Để tìm hiểu quy trình truy cập dữ liệu Media Mix Modeling thông qua API, xem thêm [Yêu cầu dữ liệu Media Mix Modeling](../08-use-cases/use-case-mmm.md#doc-1825298892472513).

Nhóm API này bao gồm các endpoint sau:
- [Tạo yêu cầu dữ liệu MMM](49-media-mix-modeling.md#doc-1825299567855617)
- [Kiểm tra trạng thái yêu cầu dữ liệu MMM](49-media-mix-modeling.md#doc-1825299576698882)
- [Lấy URL tải xuống dữ liệu MMM](49-media-mix-modeling.md#doc-1825299584678017)
- [Lấy lịch sử yêu cầu dữ liệu MMM](49-media-mix-modeling.md#doc-1825299591414850)

---

## Tạo yêu cầu dữ liệu MMM (`Create an MMM data request`)
<a id="doc-1825299567855617"></a>
<!-- doc_id: 1825299567855617 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/mmm/api/create/`

**Mục đích**: Sử dụng endpoint này để gửi yêu cầu trích xuất dữ liệu Media Mix Modeling (MMM).

> [!NOTE]
> Sau khi tạo yêu cầu dữ liệu, hệ thống cần tối đa 24 giờ để xử lý và tổng hợp dữ liệu. Sau thời gian này, bạn hãy sử dụng endpoint [/mmm/api/check/](49-media-mix-modeling.md#doc-1825299576698882) để kiểm tra trạng thái của yêu cầu.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền. Xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type | string | Bắt buộc | Định dạng nội dung yêu cầu. Sử dụng `application/json`. |

### Tham số (POST JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| advertiser_ids | string[] | Bắt buộc | Danh sách ID các nhà quảng cáo cần yêu cầu dữ liệu MMM. Khuyến nghị giới hạn tối đa 5 `advertiser_id` mỗi lần yêu cầu. Lấy danh sách qua [/bc/asset/get/](15-bc-assets.md#doc-1739432717798401). |
| request_info | object | Bắt buộc | Thông tin chi tiết cấu hình yêu cầu dữ liệu. |
| ↳ targets | object[] | Bắt buộc | Danh sách cấu hình chi tiết tài khoản quảng cáo và chiến dịch tương ứng với `advertiser_ids`. |
| ↳↳ advertiser_id | string | Bắt buộc | ID nhà quảng cáo. |
| ↳↳ campaign_ids | string[] | Không | Danh sách ID chiến dịch cần lọc. Nếu không chỉ định, dữ liệu của tất cả chiến dịch thuộc tài khoản sẽ được trả về. |
| ↳↳ brand | string | Không | Tên thương hiệu để phân loại dữ liệu trong tệp xuất. |
| ↳↳ sub_brand | string | Không | Tên thương hiệu phụ (sub-brand). |
| ↳ from_date | string | Bắt buộc | Ngày bắt đầu, định dạng `YYYY-MM-DD` (giờ UTC+0). Không được sớm hơn 4 năm trước. |
| ↳ to_date | string | Bắt buộc | Ngày kết thúc, định dạng `YYYY-MM-DD` (giờ UTC+0). |
| ↳ country_code | string[] | Không | Mã quốc gia/khu vực 2 chữ cái (ví dụ: `US`, `VN`, `JP`). Nếu không chỉ định, dữ liệu của tất cả quốc gia sẽ được trả về. |
| ↳ media_type | string | Không | Loại truyền thông. Các giá trị enum:<br>• `All` (Khuyến nghị): Cả truyền thông trả phí và lan tỏa.<br>• `Paid`: Truyền thông trả phí (Paid media).<br>• `Earned`: Truyền thông lan tỏa tự nhiên (Earned media).<br>Giá trị mặc định: `All`. |
| email | string | Không | Địa chỉ email nhận thông báo khi dữ liệu sẵn sàng để tải xuống. |

### Ví dụ

#### cURL
```bash
curl -H "Access-Token: YOUR_ACCESS_TOKEN" \
     -H "Content-Type: application/json" \
     -X POST \
     -d '{
       "advertiser_ids": ["7123456789012345678"],
       "request_info": {
         "targets": [
           {
             "advertiser_id": "7123456789012345678",
             "brand": "MyBrand"
           }
         ],
         "from_date": "2025-01-01",
         "to_date": "2025-12-31",
         "country_code": ["VN", "US"],
         "media_type": "All"
       },
       "email": "analytics@example.com"
     }' \
     https://business-api.tiktok.com/open_api/v1.3/mmm/api/create/
```

#### Python
```python
import os
import requests

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", "YOUR_ACCESS_TOKEN")
ADVERTISER_ID = os.environ.get("ADVERTISER_ID", "7123456789012345678")

url = "https://business-api.tiktok.com/open_api/v1.3/mmm/api/create/"
headers = {
    "Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}
payload = {
    "advertiser_ids": [ADVERTISER_ID],
    "request_info": {
        "targets": [{"advertiser_id": ADVERTISER_ID}],
        "from_date": "2025-01-01",
        "to_date": "2025-12-31",
        "media_type": "All"
    },
    "email": "analytics@example.com"
}

response = requests.post(url, headers=headers, json=payload)
data = response.json()
print("Mã yêu cầu MMM (mmm_request_id):", data.get("data", {}).get("mmm_request_id"))
```

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi API (`0` là thành công). |
| message | string | Thông báo phản hồi. |
| request_id | string | Mã nhật ký định danh yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ mmm_request_id | string | Mã định danh duy nhất của yêu cầu dữ liệu MMM. Lưu mã này để kiểm tra trạng thái và lấy link tải. |

---

## Kiểm tra trạng thái yêu cầu dữ liệu MMM (`Check the status of an MMM data request`)
<a id="doc-1825299576698882"></a>
<!-- doc_id: 1825299576698882 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/mmm/api/check/`

**Mục đích**: Sử dụng endpoint này để kiểm tra tiến độ xử lý của yêu cầu dữ liệu MMM dựa vào `mmm_request_id`.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền. |

### Tham số (GET query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| mmm_request_id | string | Bắt buộc | Mã định danh duy nhất của yêu cầu dữ liệu MMM đã tạo. |

### Ví dụ

#### cURL
```bash
curl --get -H "Access-Token: YOUR_ACCESS_TOKEN" \
  --data-urlencode "mmm_request_id=MMM_REQ_123456" \
  https://business-api.tiktok.com/open_api/v1.3/mmm/api/check/
```

#### Python
```python
import os
import requests

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", "YOUR_ACCESS_TOKEN")
MMM_REQUEST_ID = "MMM_REQ_123456"

url = "https://business-api.tiktok.com/open_api/v1.3/mmm/api/check/"
headers = {"Access-Token": ACCESS_TOKEN}
params = {"mmm_request_id": MMM_REQUEST_ID}

response = requests.get(url, headers=headers, params=params)
data = response.json()
print("Trạng thái MMM:", data.get("data", {}).get("status"))
```

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi API. |
| message | string | Thông báo phản hồi. |
| request_id | string | Mã log định danh yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ status | string | Trạng thái xử lý dữ liệu:<br>• `request received`: Đã nhận yêu cầu.<br>• `in progress`: Đang xử lý.<br>• `completed - ready for download`: Hoàn thành, sẵn sàng tải xuống.<br>• `failed`: Xử lý thất bại. |

---

## Lấy URL tải xuống dữ liệu MMM (`Obtain the download URL for MMM data`)
<a id="doc-1825299584678017"></a>
<!-- doc_id: 1825299584678017 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/mmm/api/download/`

**Mục đích**: Sử dụng endpoint này để lấy liên kết tải xuống tệp dữ liệu MMM sau khi trạng thái yêu cầu đạt `completed - ready for download`.

> [!NOTE]
> Đường dẫn tải xuống (`download_url`) có hiệu lực trong vòng 7 ngày. Khi liên kết hết hạn, bạn chỉ cần gọi lại endpoint này để tạo một URL tải xuống mới.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền. |

### Tham số (GET query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| mmm_request_id | string | Bắt buộc | Mã định danh duy nhất của yêu cầu dữ liệu MMM. |

### Ví dụ

#### cURL
```bash
curl --get -H "Access-Token: YOUR_ACCESS_TOKEN" \
  --data-urlencode "mmm_request_id=MMM_REQ_123456" \
  https://business-api.tiktok.com/open_api/v1.3/mmm/api/download/
```

#### Python (Tải tệp dữ liệu MMM tự động)
```python
import os
import requests

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", "YOUR_ACCESS_TOKEN")
MMM_REQUEST_ID = "MMM_REQ_123456"

# 1. Lấy link tải xuống
download_meta_url = "https://business-api.tiktok.com/open_api/v1.3/mmm/api/download/"
headers = {"Access-Token": ACCESS_TOKEN}
params = {"mmm_request_id": MMM_REQUEST_ID}

res = requests.get(download_meta_url, headers=headers, params=params)
download_url = res.json().get("data", {}).get("download_url")
print("Download URL:", download_url)

# 2. Tải tệp CSV nén về máy
if download_url:
    file_res = requests.get(download_url, stream=True)
    filename = f"mmm_data_{MMM_REQUEST_ID}.zip"
    with open(filename, "wb") as f:
        for chunk in file_res.iter_content(chunk_size=8192):
            f.write(chunk)
    print(f"Đã tải thành công tệp MMM về: {filename}")
```

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi API. |
| message | string | Thông báo phản hồi. |
| request_id | string | Mã log định danh yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ download_url | string | Đường dẫn URL tải xuống tệp dữ liệu CSV nén của MMM (có hiệu lực trong 7 ngày). |

---

## Lấy lịch sử yêu cầu dữ liệu MMM (`Get the MMM data request history`)
<a id="doc-1825299591414850"></a>
<!-- doc_id: 1825299591414850 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/mmm/api/history/`

**Mục đích**: Sử dụng endpoint này để truy vấn danh sách và chi tiết các yêu cầu dữ liệu Media Mix Modeling (MMM) đã gửi trong quá khứ.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền. |

### Tham số (GET query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| from_date | string | Bắt buộc | Ngày bắt đầu khoảng thời gian truy vấn, định dạng `YYYY-MM-DD` (UTC+0). Không sớm hơn 4 năm trước. |
| end_date | string | Bắt buộc | Ngày kết thúc khoảng thời gian truy vấn, định dạng `YYYY-MM-DD` (UTC+0). |

### Ví dụ

#### cURL
```bash
curl --get -H "Access-Token: YOUR_ACCESS_TOKEN" \
  --data-urlencode "from_date=2025-01-01" \
  --data-urlencode "end_date=2025-12-31" \
  https://business-api.tiktok.com/open_api/v1.3/mmm/api/history/
```

#### Python
```python
import os
import json
import requests

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", "YOUR_ACCESS_TOKEN")

url = "https://business-api.tiktok.com/open_api/v1.3/mmm/api/history/"
headers = {"Access-Token": ACCESS_TOKEN}
params = {
    "from_date": "2025-01-01",
    "end_date": "2025-12-31"
}

response = requests.get(url, headers=headers, params=params)
data = response.json()
for item_str in data.get("data", {}).get("historical_requests", []):
    item = json.loads(item_str)
    print("Request ID:", item.get("RequestID"), "| Status:", item.get("Status"), "| Created:", item.get("CreateTime"))
```

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi API. |
| message | string | Thông báo phản hồi. |
| request_id | string | Mã nhật ký định danh yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ historical_requests | string[] | Mảng các chuỗi định dạng JSON thể hiện thông tin chi tiết của từng yêu cầu trong quá khứ.<br>**Quy đổi giá trị:**<br>• `media_type`: `0` -> `All`, `1` -> `Earned`, `2` -> `Paid`.<br>• `Status`: `1` -> `request received`, `3` -> `in progress`, `5` -> `completed - ready for download`, `2` hoặc `4` -> `failed`. |
