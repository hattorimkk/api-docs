# Nhóm thanh toán BC (BC Billing Groups)

Business Center (BC) là trung tâm kinh doanh một điểm đến (one-stop hub) cho các tổ chức thuộc mọi quy mô nhằm kích hoạt các hoạt động tiếp thị và tiếp cận đối tượng mong muốn trên TikTok. Nhóm thanh toán (Billing Group) là tập hợp các tài khoản quảng cáo có chung cài đặt hóa đơn và thanh toán. Bộ API Nhóm thanh toán BC (BC Billing Groups API) cho phép bạn quản lý các nhóm thanh toán trong Business Center.

---

## Tổng quan về Nhóm thanh toán BC (`BC Billing Groups`)
<a id="doc-1738458086823938"></a>
<!-- doc_id: 1738458086823938 -->

> Đường dẫn: API Reference > BC Billing Groups

Nhóm thanh toán (Billing Group) là một nhóm các tài khoản quảng cáo chia sẻ chung cài đặt thanh toán và xuất hóa đơn. Cả Business Center đại lý (Agency) và Business Center trực tiếp (Direct) đều có thể thực hiện các thao tác liên quan đến nhóm thanh toán.

Nhóm API này bao gồm các endpoint sau:
* [Tạo nhóm thanh toán (Create a Billing Group)](17-bc-billing-groups.md#doc-1738947780033537)
* [Cập nhật nhóm thanh toán (Update a Billing Group)](17-bc-billing-groups.md#doc-1738947843447809)
* [Lấy danh sách nhóm thanh toán (Get Billing Groups)](17-bc-billing-groups.md#doc-1738944324279297)
* [Lấy danh sách nhà quảng cáo của nhóm thanh toán (Get the advertiser list of a Billing Group)](17-bc-billing-groups.md#doc-1738458108705794)

---

## Tạo nhóm thanh toán (`Create a Billing Group`)
<a id="doc-1738947780033537"></a>
<!-- doc_id: 1738947780033537 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/bc/billing_group/create/`

**Mục đích**: Tạo một nhóm thanh toán mới trong Business Center.

> [!NOTE]
> Chỉ người dùng có quyền Quản lý tài chính (Finance Manager) hoặc Phân tích tài chính (Finance Analyst) mới có thể quản lý các khoản thanh toán và hóa đơn trong Business Center. Bạn có thể sử dụng [/bc/member/invite/](19-bc-members.md#doc-1739939455765505) và [/bc/member/update/](19-bc-members.md#doc-1739696704424961) để cấu hình hoặc cập nhật quyền truy cập cho các thành viên.

### Header
| Field | Data Type | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập ủy quyền (Authorized access token). Xem [Xác thực](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type | string | Bắt buộc | Kiểu nội dung yêu cầu. Giá trị cho phép: `"application/json"`. |

### Tham số (POST: JSON body)
| Field | Data Type | Bắt buộc | Mô tả |
|---|---|---|---|
| bc_id | string | Bắt buộc | ID của Business Center. |
| billing_group_name | string | Bắt buộc | Tên của nhóm thanh toán. |
| advertiser_ids | string[] | Bắt buộc | Danh sách ID tài khoản quảng cáo mà bạn muốn thêm vào nhóm thanh toán.<br>**Lưu ý**: Nếu muốn tạo nhóm thanh toán cho tài khoản quảng cáo Đấu thầu (`Auction`), bạn nên thêm tất cả tài khoản Đấu thầu vào cùng một nhóm thanh toán, ngoại trừ các tài khoản đăng ký tại Pháp, Brazil hoặc Mexico. Nếu muốn tạo nhóm thanh toán cho tài khoản Đặt trước (`Reservation`), bạn chỉ thêm một tài khoản Đặt trước vào một nhóm thanh toán. |
| billing_group_emails | string[] | Không | Danh sách địa chỉ email nhận thông báo của nhóm thanh toán. |
| is_primary | bool | Không | Có đặt nhóm thanh toán này làm nhóm thanh toán mặc định cho Business Center hay không. |
| billing_group_type | string | Không | Loại hình quảng cáo của các tài khoản trong nhóm thanh toán. Cài đặt này không thể chỉnh sửa sau khi tạo.<br>Giá trị enum: `AUCTION`, `RESERVATION` (sắp ngừng hỗ trợ).<br>**Lưu ý**: Từ ngày 31/03/2024, quy trình quản lý chiến dịch thương hiệu được chuyển trực tiếp sang TikTok Ads Manager. API Business Center sẽ không còn hỗ trợ tạo và quản lý tài khoản hoặc nhóm thanh toán đặt trước (`reservation`). |

### Phản hồi
| Field | Data Type | Mô tả |
|---|---|---|
| code | number | Mã phản hồi. Giá trị `0` biểu thị thành công. Xem chi tiết tại [Mã trả về (Return Codes)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. |
| data | object | Dữ liệu trả về. |
| ↳ billing_group_id | string | ID của nhóm thanh toán vừa được tạo. |
| request_id | string | ID định danh duy nhất của yêu cầu để theo dõi log. |

### Ví dụ

#### cURL
```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/bc/billing_group/create/" \
  -H "Access-Token: YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "bc_id": "123456789012345678",
    "billing_group_name": "Nhóm thanh toán Đấu thầu Q4",
    "advertiser_ids": ["7123456789012345678", "7123456789012345679"],
    "billing_group_emails": ["billing@example.com"],
    "is_primary": true,
    "billing_group_type": "AUCTION"
  }'
```

#### Phản hồi
```json
{
  "code": 0,
  "message": "OK",
  "data": {
    "billing_group_id": "1738947780033537"
  },
  "request_id": "2026102315000001025108614416C7CC00"
}
```

---

## Cập nhật nhóm thanh toán (`Update a Billing Group`)
<a id="doc-1738947843447809"></a>
<!-- doc_id: 1738947843447809 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/bc/billing_group/update/`

**Mục đích**: Cập nhật cài đặt của một nhóm thanh toán hiện có trong Business Center.

> [!NOTE]
> Chỉ người dùng có quyền Quản lý tài chính (Finance Manager) hoặc Phân tích tài chính (Finance Analyst) mới có thể thực hiện thao tác này.

### Header
| Field | Data Type | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập ủy quyền (Authorized access token). Xem [Xác thực](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type | string | Bắt buộc | Kiểu nội dung yêu cầu. Giá trị cho phép: `"application/json"`. |

### Tham số (POST: JSON body)
| Field | Data Type | Bắt buộc | Mô tả |
|---|---|---|---|
| bc_id | string | Bắt buộc | ID của Business Center. |
| billing_group_id | string | Bắt buộc | ID của nhóm thanh toán bạn muốn chỉnh sửa. |
| new_billing_group_name | string | Không | Tên mới cho nhóm thanh toán. |
| new_billing_group_emails | string[] | Không | Danh sách địa chỉ email mới cho nhóm thanh toán. Nếu truyền trường này, danh sách email mới sẽ ghi đè toàn bộ danh sách email hiện tại của nhóm. |
| add_advertiser_ids | string[] | Không | Danh sách ID tài khoản quảng cáo bạn muốn thêm vào nhóm thanh toán này. |
| delete_advertiser_ids | string[] | Không | Danh sách ID tài khoản quảng cáo bạn muốn xóa khỏi nhóm thanh toán này. |
| is_primary | boolean | Không | Có đặt nhóm thanh toán này làm nhóm thanh toán mặc định cho Business Center hay không. |

### Phản hồi
| Field | Data Type | Mô tả |
|---|---|---|
| code | number | Mã phản hồi. Xem chi tiết tại [Mã trả về (Return Codes)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. |
| data | object | Dữ liệu trả về (rỗng nếu thành công). |
| request_id | string | ID định danh duy nhất của yêu cầu để theo dõi log. |

### Ví dụ

#### cURL
```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/bc/billing_group/update/`" \
  -H "Access-Token: YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "bc_id": "123456789012345678",
    "billing_group_id": "1738947780033537",
    "new_billing_group_name": "Nhóm thanh toán Đấu thầu 2026",
    "new_billing_group_emails": ["finance@example.com"],
    "add_advertiser_ids": ["7123456789012345680"],
    "delete_advertiser_ids": ["7123456789012345678"],
    "is_primary": true
  }'
```

#### Phản hồi
```json
{
  "code": 0,
  "message": "OK",
  "data": {},
  "request_id": "2026102315050001025108614416C7CC01"
}
```

---

## Lấy danh sách nhóm thanh toán (`Get Billing Groups`)
<a id="doc-1738944324279297"></a>
<!-- doc_id: 1738944324279297 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/bc/billing_group/get/`

**Mục đích**: Lấy danh sách tất cả các nhóm thanh toán trong Business Center cùng với thông tin chi tiết của từng nhóm.

### Header
| Field | Data Type | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập ủy quyền (Authorized access token). Xem [Xác thực](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (GET: query string)
| Field | Data Type | Bắt buộc | Mô tả |
|---|---|---|---|
| bc_id | string | Bắt buộc | ID của Business Center. |
| filtering | object | Không | Điều kiện lọc nhóm thanh toán (truyền dưới dạng chuỗi JSON đã URL-encode). |
| ↳ status | string | Không | Trạng thái nhóm thanh toán cần lọc. Giá trị enum: `VALID` (hợp lệ), `INVALID` (không hợp lệ). |
| ↳ invoice_group_by | string | Không | Cách thức xử lý hóa đơn trong nhóm thanh toán.<br>Giá trị enum:<br>• `ACCOUNT`: Hóa đơn của các tài khoản trong nhóm được gộp chung.<br>• `ADVERTISER`: Hóa đơn của từng tài khoản trong nhóm được xử lý riêng rẽ. |
| ↳ billed_to_type | string | Không | Đối tượng thanh toán được thể hiện trên hóa đơn.<br>Giá trị enum:<br>• `ACCOUNT`: Hóa đơn xuất cho đại lý (agency).<br>• `ADVERTISER`: Hóa đơn xuất cho nhà quảng cáo. |
| ↳ billing_group_id | string | Không | Lọc theo ID nhóm thanh toán cụ thể. |
| ↳ billing_group_name | string | Không | Lọc theo tên nhóm thanh toán. |
| ↳ billing_group_type | string | Không | Loại hình quảng cáo của các tài khoản trong nhóm. Giá trị enum: `AUCTION`, `RESERVATION`. |
| page | number | Không | Số trang. Giá trị mặc định: `1`. |
| page_size | number | Không | Số lượng bản ghi mỗi trang, phạm vi từ 1–50. Giá trị mặc định: `10`. |

### Phản hồi
| Field | Data Type | Mô tả |
|---|---|---|
| code | number | Mã phản hồi. Giá trị `0` biểu thị thành công. Xem [Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. |
| data | object | Dữ liệu trả về. |
| ↳ list | object[] | Danh sách các nhóm thanh toán. |
| ↳↳ status | string | Trạng thái nhóm thanh toán. Giá trị enum: `VALID`, `INVALID`. |
| ↳↳ billing_group_id | string | ID của nhóm thanh toán. |
| ↳↳ billing_group_name | string | Tên của nhóm thanh toán. |
| ↳↳ invoice_object_name | string | Tên đối tượng nhận hóa đơn. |
| ↳↳ is_primary | bool | Có phải là nhóm thanh toán mặc định của Business Center hay không. |
| ↳↳ advertisers | object[] | Danh sách tài khoản quảng cáo thuộc nhóm thanh toán này. |
| ↳↳↳ advertiser_id | string | ID tài khoản quảng cáo. |
| ↳↳↳ advertiser_name | string | Tên tài khoản quảng cáo. |
| ↳↳ billing_group_emails | string[] | Danh sách email nhận thông báo của nhóm thanh toán. |
| ↳↳ invoice_group_by | string | Phương thức gộp hóa đơn (`ACCOUNT` hoặc `ADVERTISER`). |
| ↳↳ billed_to_type | string | Đối tượng nhận hóa đơn (`ACCOUNT` hoặc `ADVERTISER`). |
| ↳↳ billing_group_type | string | Loại hình quảng cáo (`AUCTION`, `RESERVATION`). |
| ↳ page_info | object | Thông tin phân trang. |
| ↳↳ page | number | Trang hiện tại. |
| ↳↳ page_size | number | Số bản ghi trên mỗi trang. |
| ↳↳ total_number | number | Tổng số bản ghi kết quả. |
| ↳↳ total_page | number | Tổng số trang. |
| request_id | string | ID định danh duy nhất của yêu cầu để theo dõi log. |

### Ví dụ

#### cURL
```bash
curl -X GET "https://business-api.tiktok.com/open_api/v1.3/bc/billing_group/get/?bc_id=123456789012345678&page=1&page_size=10" \
  -H "Access-Token: YOUR_ACCESS_TOKEN"
```

#### Python
```python
import os
import requests

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", "YOUR_ACCESS_TOKEN")
BC_ID = os.environ.get("BC_ID", "123456789012345678")

url = "https://business-api.tiktok.com/open_api/v1.3/bc/billing_group/get/"
headers = {
    "Access-Token": ACCESS_TOKEN,
}
params = {
    "bc_id": BC_ID,
    "page": 1,
    "page_size": 10,
}

response = requests.get(url, headers=headers, params=params)
data = response.json()

if data.get("code") == 0:
    billing_groups = data.get("data", {}).get("list", [])
    for bg in billing_groups:
        print(f"Billing Group: {bg.get('billing_group_name')} (ID: {bg.get('billing_group_id')})")
        print(f"  Trạng thái: {bg.get('status')} | Mặc định: {bg.get('is_primary')}")
        for adv in bg.get("advertisers", []):
            print(f"  - Tài khoản: {adv.get('advertiser_name')} (ID: {adv.get('advertiser_id')})")
else:
    print(f"Lỗi: {data.get('message')} (code: {data.get('code')})")
```

#### Phản hồi
```json
{
  "code": 0,
  "message": "OK",
  "data": {
    "list": [
      {
        "status": "VALID",
        "billing_group_id": "1738947780033537",
        "billing_group_name": "Nhóm thanh toán Đấu thầu 2026",
        "invoice_object_name": "Công ty TNHH Quảng Cáo Mẫu",
        "is_primary": true,
        "advertisers": [
          {
            "advertiser_id": "7123456789012345679",
            "advertiser_name": "Tài khoản Quảng cáo Brand 1"
          }
        ],
        "billing_group_emails": ["billing@example.com"],
        "invoice_group_by": "ACCOUNT",
        "billed_to_type": "ACCOUNT",
        "billing_group_type": "AUCTION"
      }
    ],
    "page_info": {
      "page": 1,
      "page_size": 10,
      "total_number": 1,
      "total_page": 1
    }
  },
  "request_id": "2026102315100001025108614416C7CC02"
}
```

---

## Lấy danh sách nhà quảng cáo của nhóm thanh toán (`Get the advertiser list of a Billing Group`)
<a id="doc-1738458108705794"></a>
<!-- doc_id: 1738458108705794 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/bc/billing_group/advertiser/list/`

**Mục đích**: Lấy danh sách các tài khoản nhà quảng cáo đang được liên kết với một nhóm thanh toán cụ thể trong Business Center.

### Header
| Field | Data Type | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập ủy quyền (Authorized access token). Xem [Xác thực](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (GET: query string)
| Field | Data Type | Bắt buộc | Mô tả |
|---|---|---|---|
| bc_id | string | Bắt buộc | ID của Business Center. |
| billing_group_id | string | Bắt buộc | ID của nhóm thanh toán. |
| page | number | Không | Số trang. Giá trị mặc định: `1`. |
| page_size | number | Không | Số lượng bản ghi mỗi trang, phạm vi từ 1–50. Giá trị mặc định: `10`. |

### Phản hồi
| Field | Data Type | Mô tả |
|---|---|---|
| code | number | Mã phản hồi. Giá trị `0` biểu thị thành công. Xem [Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. |
| data | object | Dữ liệu trả về. |
| ↳ list | object[] | Danh sách các nhà quảng cáo. |
| ↳↳ advertiser_id | string | ID tài khoản quảng cáo. |
| ↳ page_info | object | Thông tin phân trang. |
| ↳↳ page | number | Trang hiện tại. |
| ↳↳ page_size | number | Số lượng bản ghi trên trang. |
| ↳↳ total_number | number | Tổng số bản ghi kết quả. |
| ↳↳ total_page | number | Tổng số trang. |
| request_id | string | ID định danh duy nhất của yêu cầu để theo dõi log. |

### Ví dụ

#### cURL
```bash
curl -X GET "https://business-api.tiktok.com/open_api/v1.3/bc/billing_group/advertiser/list/?bc_id=123456789012345678&billing_group_id=1738947780033537&page=1&page_size=10" \
  -H "Access-Token: YOUR_ACCESS_TOKEN"
```

#### Python
```python
import os
import requests

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", "YOUR_ACCESS_TOKEN")
BC_ID = os.environ.get("BC_ID", "123456789012345678")
BILLING_GROUP_ID = os.environ.get("BILLING_GROUP_ID", "1738947780033537")

url = "https://business-api.tiktok.com/open_api/v1.3/bc/billing_group/advertiser/list/"
headers = {
    "Access-Token": ACCESS_TOKEN,
}
params = {
    "bc_id": BC_ID,
    "billing_group_id": BILLING_GROUP_ID,
    "page": 1,
    "page_size": 10,
}

response = requests.get(url, headers=headers, params=params)
data = response.json()

if data.get("code") == 0:
    advertisers = data.get("data", {}).get("list", [])
    print(f"Tổng số tài khoản trong nhóm thanh toán: {len(advertisers)}")
    for adv in advertisers:
        print(f"- Advertiser ID: {adv.get('advertiser_id')}")
else:
    print(f"Lỗi: {data.get('message')} (code: {data.get('code')})")
```

#### Phản hồi
```json
{
  "code": 0,
  "message": "OK",
  "data": {
    "list": [
      {
        "advertiser_id": "7123456789012345679"
      },
      {
        "advertiser_id": "7123456789012345680"
      }
    ],
    "page_info": {
      "page": 1,
      "page_size": 10,
      "total_number": 2,
      "total_page": 1
    }
  },
  "request_id": "2026102315150001025108614416C7CC03"
}
```
