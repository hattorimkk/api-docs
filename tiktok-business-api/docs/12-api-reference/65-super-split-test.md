# Thử nghiệm phân tách Super Split Test (Super Split Test)

Tài liệu này cung cấp hướng dẫn và đặc tả kỹ thuật chi tiết cho nhóm API Thử nghiệm phân tách Super Split Test (A/B Testing) của TikTok for Business.

Super Split Test cho phép bạn so sánh hiệu suất giữa các nhóm quảng cáo (Ad Group level) hoặc các chiến dịch (Campaign level) với đối tượng khán giả được phân chia độc lập và không trùng lặp, nhằm xác định chiến lược nhắm mục tiêu, nội dung sáng tạo hoặc phương pháp đặt giá thầu mang lại kết quả tốt nhất.

Trước khi bắt đầu, vui lòng xem [điều kiện tiên quyết tạo split test](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1742668394531842) và [quy trình tạo split test](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1742668948278274).

## Danh sách endpoint trong tài liệu

| Phương thức | Endpoint | Mô tả |
|---|---|---|
| `POST` | `/open_api/v1.3/split_test/create/` | Tạo một nhóm thử nghiệm phân tách A/B mới |
| `POST` | `/open_api/v1.3/split_test/update/` | Cập nhật thời gian bắt đầu và kết thúc của thử nghiệm |
| `POST` | `/open_api/v1.3/split_test/end/` | Dừng (kết thúc) thử nghiệm phân tách đang chạy |
| `GET` | `/open_api/v1.3/split_test/result/get/` | Lấy kết quả thống kê và giá trị P-value của thử nghiệm |
| `POST` | `/open_api/v1.3/split_test/promote/` | Tiếp tục phân phối nhóm quảng cáo chiến thắng và nhân đôi ngân sách |

---

## Tổng quan về Super Split Test (Super Split Test Overview)
<a id="doc-1742666215544834"></a>
<!-- doc_id: 1742666215544834 -->

Thử nghiệm phân tách Super Split Test hỗ trợ 2 cấp độ:
- **Cấp độ nhóm quảng cáo (Ad group level)**: Ngân sách tổng sẽ được phân bổ đều cho từng nhóm quảng cáo tham gia thử nghiệm.
- **Cấp độ chiến dịch (Campaign level)**: Ngân sách tuân theo số tiền ngân sách đã thiết lập sẵn của từng chiến dịch.

Khán giả được hệ thống phân tách ngẫu nhiên và loại trừ lẫn nhau (mutually exclusive) để đảm bảo không có sự chồng chéo đối tượng giữa các nhánh thử nghiệm.

Các tài liệu liên kết trong nhóm:
* [Tạo thử nghiệm phân tách](65-super-split-test.md#doc-1742666471475201)
* [Cập nhật thời gian thử nghiệm phân tách](65-super-split-test.md#doc-1742666501911553)
* [Kết thúc thử nghiệm phân tách](65-super-split-test.md#doc-1742666522399746)
* [Lấy kết quả thử nghiệm phân tách](65-super-split-test.md#doc-1742666557045761)
* [Chạy nhóm quảng cáo chiến thắng](65-super-split-test.md#doc-1742666543736834)

---

## Tạo thử nghiệm phân tách (Create a split test)
<a id="doc-1742666471475201"></a>
<!-- doc_id: 1742666471475201 -->

Sử dụng endpoint này để khởi tạo một nhóm thử nghiệm phân tách A/B mới.

### Yêu cầu (Request)

**Endpoint:** `https://business-api.tiktok.com/open_api/v1.3/split_test/create/`  
**Phương thức (Method):** `POST`

#### Header

| Field | Data Type | Description |
|---|---|---|
| `Access-Token` **(Bắt buộc)** | string | Mã token truy cập được cấp quyền. Xem thêm [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| `Content-Type` **(Bắt buộc)** | string | Định dạng nội dung yêu cầu. Giá trị: `"application/json"`. |

#### Tham số (Parameters)

| Field | Data Type | Description |
|---|---|---|
| `advertiser_id` **(Bắt buộc)** | string | ID của nhà quảng cáo. |
| `split_test_level` **(Bắt buộc)** | string | Cấp độ thử nghiệm phân tách. Enum: `ADGROUP` (cấp nhóm quảng cáo), `CAMPAIGN` (cấp chiến dịch). |
| `object_ids` | string[] | Danh sách ID các nhóm quảng cáo liên kết với thử nghiệm. Đối với cấp `ADGROUP`, chỉ định chính xác 2 ID nhóm quảng cáo; không được dùng trường này khi `split_test_level` là `CAMPAIGN`. |
| `cells` {+Conditional} | object[] | Bắt buộc khi `split_test_level` là `CAMPAIGN`. Danh sách các ô thử nghiệm (cells). Mỗi cell chứa mảng `object_ids` (chính xác 1 campaign ID cho mỗi cell, tổng cộng 2–3 cells). |
| `↳ object_ids` | string[] | Mảng chứa ID chiến dịch hoặc ID nhóm quảng cáo trong từng ô cell. |
| `test_variable` **(Bắt buộc)** | string | Biến số thử nghiệm phân tách. Trường này không ảnh hưởng đến thuật toán phân tách đối tượng nhưng giúp gắn nhãn phân loại. Enum: `TARGETING` (Đối tượng mục tiêu), `BID_OPTIMIZATION` (Giá thầu & Tối ưu hóa), `CREATIVE` (Nội dung sáng tạo). |
| `key_metric` **(Bắt buộc)** | string | Chỉ số đo lường chính để xác định nhánh chiến thắng. Enum: `COST_PER_RESULT` (Chi phí trên mỗi kết quả), `CPA` (Chi phí trên mỗi hành động), `CPC` (Chi phí trên mỗi lượt nhấp), `CPM` (Chi phí trên mỗi nghìn lượt hiển thị). |
| `budget` {+Conditional} | float | Bắt buộc khi `split_test_level` là `ADGROUP`. Ngân sách tổng của thử nghiệm phân tách cấp nhóm quảng cáo. Bị bỏ qua ở cấp `CAMPAIGN`. |
| `start_time` **(Bắt buộc)** | string | Thời gian bắt đầu thử nghiệm định dạng `YYYY-MM-DD HH:MM:SS` theo múi giờ tài khoản. |
| `end_time` **(Bắt buộc)** | string | Thời gian kết thúc thử nghiệm định dạng `YYYY-MM-DD HH:MM:SS`. Thời lượng thử nghiệm phải từ 2 đến 30 ngày. |

#### Ví dụ gọi API

##### cURL

```bash
curl -X POST 'https://business-api.tiktok.com/open_api/v1.3/split_test/create/' \
  -H 'Access-Token: YOUR_ACCESS_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{
    "advertiser_id": "7123456789012345678",
    "split_test_level": "ADGROUP",
    "object_ids": [
      "1765432109876588",
      "1765432109876589"
    ],
    "test_variable": "CREATIVE",
    "key_metric": "COST_PER_RESULT",
    "budget": 200.0,
    "start_time": "2024-04-01 00:00:00",
    "end_time": "2024-04-08 00:00:00"
  }'
```

##### Python (requests)

```python
import requests

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ADVERTISER_ID = "7123456789012345678"
url = "https://business-api.tiktok.com/open_api/v1.3/split_test/create/"

headers = {
    "Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}

payload = {
    "advertiser_id": ADVERTISER_ID,
    "split_test_level": "ADGROUP",
    "object_ids": [
        "1765432109876588",
        "1765432109876589"
    ],
    "test_variable": "CREATIVE",
    "key_metric": "COST_PER_RESULT",
    "budget": 200.0,
    "start_time": "2024-04-01 00:00:00",
    "end_time": "2024-04-08 00:00:00"
}

response = requests.post(url, headers=headers, json=payload)
print(response.status_code)
print(response.json())
```

### Phản hồi (Response)

| Field | Data Type | Description |
|---|---|---|
| `code` | number | Mã phản hồi. `0` biểu thị thành công. Các mã khác xem tại [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi từ hệ thống. |
| `data` | object | Dữ liệu trả về. |
| `↳ split_test_group_id` | string | ID của nhóm thử nghiệm phân tách vừa tạo. |
| `request_id` | string | Chuỗi log ID duy nhất xác định yêu cầu. |

#### Ví dụ phản hồi thành công

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "2024040112000001018905602824580D00",
  "data": {
    "split_test_group_id": "1765432109876500"
  }
}
```

---

## Cập nhật thời gian thử nghiệm phân tách (Update the time of a split test)
<!-- doc_id: 1740859218541569_dummy_skip -->
<a id="doc-1742666501911553"></a>
<!-- doc_id: 1742666501911553 -->

Sử dụng endpoint này để điều chỉnh thời gian bắt đầu (`start_time`) và thời gian kết thúc (`end_time`) của một nhóm thử nghiệm phân tách.

### Yêu cầu (Request)

**Endpoint:** `https://business-api.tiktok.com/open_api/v1.3/split_test/update/`  
**Phương thức (Method):** `POST`

#### Header

| Field | Data Type | Description |
|---|---|---|
| `Access-Token` **(Bắt buộc)** | string | Mã token truy cập được cấp quyền. Xem thêm [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| `Content-Type` **(Bắt buộc)** | string | Định dạng nội dung yêu cầu. Giá trị: `"application/json"`. |

#### Tham số (Parameters)

| Field | Data Type | Description |
|---|---|---|
| `advertiser_id` **(Bắt buộc)** | string | ID của nhà quảng cáo. |
| `split_test_group_id` **(Bắt buộc)** | string | ID của nhóm thử nghiệm phân tách cần cập nhật. |
| `start_time` **(Bắt buộc)** | string | Thời gian bắt đầu mới định dạng `YYYY-MM-DD HH:MM:SS`. |
| `end_time` **(Bắt buộc)** | string | Thời gian kết thúc mới định dạng `YYYY-MM-DD HH:MM:SS`. |

#### Ví dụ gọi API

##### cURL

```bash
curl -X POST 'https://business-api.tiktok.com/open_api/v1.3/split_test/update/' \
  -H 'Access-Token: YOUR_ACCESS_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{
    "advertiser_id": "7123456789012345678",
    "split_test_group_id": "1765432109876500",
    "start_time": "2024-04-01 00:00:00",
    "end_time": "2024-04-10 00:00:00"
  }'
```

##### Python (requests)

```python
import requests

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ADVERTISER_ID = "7123456789012345678"
url = "https://business-api.tiktok.com/open_api/v1.3/split_test/update/"

headers = {
    "Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}

payload = {
    "advertiser_id": ADVERTISER_ID,
    "split_test_group_id": "1765432109876500",
    "start_time": "2024-04-01 00:00:00",
    "end_time": "2024-04-10 00:00:00"
}

response = requests.post(url, headers=headers, json=payload)
print(response.status_code)
print(response.json())
```

### Phản hồi (Response)

| Field | Data Type | Description |
|---|---|---|
| `code` | number | Mã phản hồi. `0` biểu thị thành công. Các mã khác xem tại [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi từ hệ thống. |
| `data` | object | Dữ liệu trả về (đối tượng rỗng `{}` khi cập nhật thành công). |
| `request_id` | string | Chuỗi log ID duy nhất xác định yêu cầu. |

#### Ví dụ phản hồi thành công

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "2024040112000001018905602824580D00",
  "data": {}
}
```

---

## Kết thúc thử nghiệm phân tách (End a split test)
<a id="doc-1742666522399746"></a>
<!-- doc_id: 1742666522399746 -->

Sử dụng endpoint này để dừng một thử nghiệm phân tách đang chạy ở cấp độ nhóm quảng cáo hoặc cấp độ chiến dịch.
- Ở cấp **nhóm quảng cáo**: Khi thử nghiệm bị dừng, trạng thái của cả hai nhóm quảng cáo sẽ chuyển sang không hoạt động (`INACTIVE`).
- Ở cấp **chiến dịch**: Khi thử nghiệm dừng lại, các chiến dịch và nhóm quảng cáo vẫn tiếp tục chạy theo lịch trình riêng độc lập với thử nghiệm.
- Nếu bạn dừng thử nghiệm cấp chiến dịch trước giờ bắt đầu, trạng thái `split_test_status` sẽ chuyển thành `CANCELED`.

### Yêu cầu (Request)

**Endpoint:** `https://business-api.tiktok.com/open_api/v1.3/split_test/end/`  
**Phương thức (Method):** `POST`

#### Header

| Field | Data Type | Description |
|---|---|---|
| `Access-Token` **(Bắt buộc)** | string | Mã token truy cập được cấp quyền. Xem thêm [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| `Content-Type` **(Bắt buộc)** | string | Định dạng nội dung yêu cầu. Giá trị: `"application/json"`. |

#### Tham số (Parameters)

| Field | Data Type | Description |
|---|---|---|
| `advertiser_id` **(Bắt buộc)** | string | ID của nhà quảng cáo. |
| `split_test_group_id` **(Bắt buộc)** | string | ID của nhóm thử nghiệm phân tách cần dừng. |

#### Ví dụ gọi API

##### cURL

```bash
curl -X POST 'https://business-api.tiktok.com/open_api/v1.3/split_test/end/' \
  -H 'Access-Token: YOUR_ACCESS_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{
    "advertiser_id": "7123456789012345678",
    "split_test_group_id": "1765432109876500"
  }'
```

##### Python (requests)

```python
import requests

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ADVERTISER_ID = "7123456789012345678"
url = "https://business-api.tiktok.com/open_api/v1.3/split_test/end/"

headers = {
    "Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}

payload = {
    "advertiser_id": ADVERTISER_ID,
    "split_test_group_id": "1765432109876500"
}

response = requests.post(url, headers=headers, json=payload)
print(response.status_code)
print(response.json())
```

### Phản hồi (Response)

| Field | Data Type | Description |
|---|---|---|
| `code` | number | Mã phản hồi. `0` biểu thị thành công. Các mã khác xem tại [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi từ hệ thống. |
| `data` | object | Dữ liệu trả về (đối tượng rỗng `{}` khi kết thúc thành công). |
| `request_id` | string | Chuỗi log ID duy nhất xác định yêu cầu. |

#### Ví dụ phản hồi thành công

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "2024040112000001018905602824580D00",
  "data": {}
}
```

---

## Lấy kết quả thử nghiệm phân tách (Get the results of a split test)
<a id="doc-1742666557045761"></a>
<!-- doc_id: 1742666557045761 -->

Sử dụng endpoint này ít nhất **24 giờ sau khi thử nghiệm kết thúc** để truy xuất kết quả thử nghiệm, bao gồm giá trị p-value cho từng chỉ số đo lường.

### Yêu cầu (Request)

**Endpoint:** `https://business-api.tiktok.com/open_api/v1.3/split_test/result/get/`  
**Phương thức (Method):** `GET`

#### Header

| Field | Data Type | Description |
|---|---|---|
| `Access-Token` **(Bắt buộc)** | string | Mã token truy cập được cấp quyền. Xem thêm [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

#### Tham số (Parameters)

| Field | Data Type | Description |
|---|---|---|
| `advertiser_id` **(Bắt buộc)** | string | ID của nhà quảng cáo. |
| `split_test_group_id` **(Bắt buộc)** | string | ID của nhóm thử nghiệm phân tách. |

#### Ví dụ gọi API

##### cURL

```bash
curl -X GET 'https://business-api.tiktok.com/open_api/v1.3/split_test/result/get/?advertiser_id=7123456789012345678&split_test_group_id=1765432109876500' \
  -H 'Access-Token: YOUR_ACCESS_TOKEN'
```

##### Python (requests)

```python
import requests

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ADVERTISER_ID = "7123456789012345678"
SPLIT_TEST_ID = "1765432109876500"
url = "https://business-api.tiktok.com/open_api/v1.3/split_test/result/get/"

headers = {
    "Access-Token": ACCESS_TOKEN
}

params = {
    "advertiser_id": ADVERTISER_ID,
    "split_test_group_id": SPLIT_TEST_ID
}

response = requests.get(url, headers=headers, params=params)
print(response.status_code)
print(response.json())
```

### Phản hồi (Response)

| Field | Data Type | Description |
|---|---|---|
| `code` | number | Mã phản hồi. `0` biểu thị thành công. Các mã khác xem tại [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi từ hệ thống. |
| `data` | object | Dữ liệu kết quả trả về. |
| `↳ split_test_status` | string | Trạng thái của thử nghiệm (`COMPLETED`, `RUNNING`, `CANCELED`). |
| `↳ split_test_level` | string | Cấp độ thử nghiệm (`ADGROUP`, `CAMPAIGN`). |
| `↳ object_info` | object[] | Danh sách thông tin về các nhóm quảng cáo tham gia thử nghiệm. |
| `↳↳ adgroup_id` | string | ID của nhóm quảng cáo. |
| `↳↳ adgroup_name` | string | Tên của nhóm quảng cáo. |
| `↳↳ optimization_goal` | string | Mục tiêu tối ưu hóa của nhóm quảng cáo. |
| `↳ cells` | object[] | Danh sách các ô thử nghiệm cell. |
| `↳↳ object_ids` | string[] | Danh sách ID chiến dịch hoặc ID nhóm quảng cáo trong ô cell. |
| `↳ test_variable` | string | Biến số thử nghiệm (`TARGETING`, `BID_OPTIMIZATION`, `CREATIVE`). |
| `↳ key_metric` | string | Chỉ số đo lường chính đã chọn khi tạo thử nghiệm. |
| `↳ start_time` | string | Thời gian bắt đầu thử nghiệm. |
| `↳ end_time` | string | Thời gian kết thúc thử nghiệm. |
| `↳ p_value_info` | object[] | Thông tin kết quả thống kê và giá trị P-value. |
| `↳↳ metric` | string | Tên chỉ số đo lường (`COST_PER_RESULT`, `CPA`, `CPC`, `CPM`, v.v.). |
| `↳↳ p_value` | float | Giá trị p-value thống kê. Sẽ có nhánh chiến thắng rõ ràng khi p_value <= 0.1 (độ tin cậy 90%). |
| `request_id` | string | Chuỗi log ID duy nhất xác định yêu cầu. |

#### Ví dụ phản hồi thành công

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "2024040112000001018905602824580D00",
  "data": {
    "split_test_status": "COMPLETED",
    "split_test_level": "ADGROUP",
    "test_variable": "CREATIVE",
    "key_metric": "COST_PER_RESULT",
    "object_info": [
      {
        "adgroup_id": "1765432109876588",
        "adgroup_name": "Creative_Variation_A"
      },
      {
        "adgroup_id": "1765432109876589",
        "adgroup_name": "Creative_Variation_B"
      }
    ],
    "p_value_info": [
      {
        "metric": "COST_PER_RESULT",
        "p_value": 0.04
      }
    ]
  }
}
```

---

## Chạy nhóm quảng cáo chiến thắng (Run the winning ad group)
<a id="doc-1742666543736834"></a>
<!-- doc_id: 1742666543736834 -->

Sử dụng endpoint này để tiếp tục chạy nhóm quảng cáo chiến thắng trong thử nghiệm phân tách cấp nhóm quảng cáo. Sau khi gọi endpoint này, nhóm quảng cáo còn lại trong thử nghiệm sẽ bị tạm dừng và không hoạt động, đồng thời ngân sách của nhóm quảng cáo chiến thắng sẽ được nhân đôi.

Trước khi bắt đầu, sử dụng [/split_test/result/get/](65-super-split-test.md#doc-1742666557045761) để lấy `metric` và `p_value`. Sẽ có một nhóm quảng cáo chiến thắng được xác định khi `p_value` <= 0.1.

> **Lưu ý:** Hiện tại endpoint này không hỗ trợ thử nghiệm phân tách cấp chiến dịch (`CAMPAIGN`).

### Yêu cầu (Request)

**Endpoint:** `https://business-api.tiktok.com/open_api/v1.3/split_test/promote/`  
**Phương thức (Method):** `POST`

#### Header

| Field | Data Type | Description |
|---|---|---|
| `Access-Token` **(Bắt buộc)** | string | Mã token truy cập được cấp quyền. Xem thêm [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| `Content-Type` **(Bắt buộc)** | string | Định dạng nội dung yêu cầu. Giá trị: `"application/json"`. |

#### Tham số (Parameters)

| Field | Data Type | Description |
|---|---|---|
| `advertiser_id` **(Bắt buộc)** | string | ID của nhà quảng cáo. |
| `split_test_group_id` **(Bắt buộc)** | string | ID của nhóm thử nghiệm phân tách. |
| `winning_object_id` **(Bắt buộc)** | string | ID của nhóm quảng cáo chiến thắng. Sử dụng [/split_test/result/get/](65-super-split-test.md#doc-1742666557045761) để xác định ID này. |

#### Ví dụ gọi API

##### cURL

```bash
curl -X POST 'https://business-api.tiktok.com/open_api/v1.3/split_test/promote/' \
  -H 'Access-Token: YOUR_ACCESS_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{
    "advertiser_id": "7123456789012345678",
    "split_test_group_id": "1765432109876500",
    "winning_object_id": "1765432109876588"
  }'
```

##### Python (requests)

```python
import requests

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ADVERTISER_ID = "7123456789012345678"
url = "https://business-api.tiktok.com/open_api/v1.3/split_test/promote/"

headers = {
    "Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}

payload = {
    "advertiser_id": ADVERTISER_ID,
    "split_test_group_id": "1765432109876500",
    "winning_object_id": "1765432109876588"
}

response = requests.post(url, headers=headers, json=payload)
print(response.status_code)
print(response.json())
```

### Phản hồi (Response)

| Field | Data Type | Description |
|---|---|---|
| `code` | number | Mã phản hồi. `0` biểu thị thành công. Các mã khác xem tại [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi từ hệ thống. |
| `data` | object | Dữ liệu trả về (đối tượng rỗng `{}` khi kích hoạt thành công). |
| `request_id` | string | Chuỗi log ID duy nhất xác định yêu cầu. |

#### Ví dụ phản hồi thành công

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "2024040112000001018905602824580D00",
  "data": {}
}
```
