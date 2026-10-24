# Hóa đơn BC (BC Invoices)

Nhóm API Hóa đơn Business Center (BC Invoices) cho phép các tổ chức, đại lý (Agency) và doanh nghiệp trực tiếp (Direct Business Center) quản lý tập trung hóa đơn, số dư công nợ chưa thanh toán và tải xuống hóa đơn quảng cáo trên TikTok. Bạn có thể tra cứu chi tiết danh sách hóa đơn theo trạng thái và thời gian, xem tổng số tiền chưa thanh toán theo đơn vị tiền tệ, tải hóa đơn tức thì dưới định dạng PDF hoặc thiết lập các tác vụ tải xuống bất đồng bộ số lượng lớn (danh sách hóa đơn định dạng Excel hoặc gói tệp ZIP hóa đơn).

| Endpoint | Method | Đường dẫn | Mục đích |
|---|---|---|---|
| Tổng quan hóa đơn Business Center | - | - | Khái quát quy trình quản lý hóa đơn, công nợ và quyền tài chính trong Business Center |
| Lấy danh sách hóa đơn Business Center | `GET` | `/open_api/v1.3/bc/invoice/get/` | Tra cứu chi tiết hóa đơn theo loại, trạng thái thanh toán và khoảng thời gian |
| Lấy số tiền chưa thanh toán | `GET` | `/open_api/v1.3/bc/invoice/unpaid/get/` | Xem tổng số tiền công nợ chưa thanh toán theo loại tiền tệ |
| Tổng quan tải xuống hóa đơn | - | - | Giới thiệu các phương thức tải xuống hóa đơn đồng bộ và bất đồng bộ |
| Tải xuống hóa đơn đồng bộ | `GET` | `/open_api/v1.3/bc/invoice/download/` | Tải xuống trực tiếp luồng tệp PDF của một hóa đơn cụ thể |
| Tổng quan tải xuống bất đồng bộ | - | - | Giới thiệu quy trình tạo tác vụ và tải xuống gói hóa đơn lịch sử |
| Tạo tác vụ tải xuống bất đồng bộ | `POST` | `/open_api/v1.3/bc/invoice/task/create/` | Tạo tác vụ tải xuống danh sách hóa đơn, gói hóa đơn ZIP hoặc báo cáo giao dịch |
| Lấy thông tin tác vụ tải xuống bất đồng bộ | `GET` | `/open_api/v1.3/bc/invoice/task/get/` | Kiểm tra tiến độ và nhận luồng tệp Excel của tác vụ báo cáo thanh toán |
| Lấy danh sách tác vụ tải xuống bất đồng bộ | `GET` | `/open_api/v1.3/bc/invoice/task/list/` | Tra cứu danh sách các tác vụ tải xuống và lấy đường dẫn URL tải file |

---

## Tổng quan hóa đơn Business Center (`BC Invoices`)
<a id="doc-1740132803511297"></a>
<!-- doc_id: 1740132803511297 -->

Business Center là trung tâm điều hành tập trung cho các tổ chức thuộc mọi quy mô nhằm kích hoạt các hoạt động tiếp thị và tiếp cận đối tượng mong muốn một cách cộng tác trên TikTok. Nhóm API BC Invoices giúp bạn quản lý hóa đơn trong một Business Center. Cả Business Center dạng Đại lý (Agency) và Trực tiếp (Direct) đều có thể thực hiện các thao tác liên quan đến hóa đơn.

Nhóm này bao gồm các endpoint sau:
- [Lấy danh sách hóa đơn Business Center](20-bc-invoices.md#doc-1740295890332674): Tra cứu chi tiết các hóa đơn phát hành.
- [Lấy số tiền chưa thanh toán](20-bc-invoices.md#doc-1740295904843777): Lấy tổng số tiền nợ chưa thanh toán của tài khoản Business Center.
- [Tổng quan tải xuống hóa đơn](20-bc-invoices.md#doc-1740295923474433): Tải xuống hóa đơn qua phương thức đồng bộ hoặc bất đồng bộ.
  - [Tải xuống hóa đơn đồng bộ](20-bc-invoices.md#doc-1754000198430722): Tải xuống trực tiếp một hóa đơn cá nhân.
  - [Tổng quan tải xuống bất đồng bộ](20-bc-invoices.md#doc-1754000224141313):
    - [Tạo tác vụ tải xuống bất đồng bộ](20-bc-invoices.md#doc-1754000448122882)
    - [Lấy thông tin tác vụ tải xuống bất đồng bộ](20-bc-invoices.md#doc-1754000480307265)
    - [Lấy danh sách tác vụ tải xuống bất đồng bộ](20-bc-invoices.md#doc-1754000504437762)

> [!NOTE]
> Chỉ những người dùng có quyền Quản lý tài chính (`Finance Manager`) hoặc Chuyên viên phân tích tài chính (`Finance Analyst`) mới có thể quản lý các khoản thanh toán và hóa đơn trong Business Center. Bạn có thể sử dụng [/bc/member/invite/](19-bc-members.md#doc-1739939455765505) và [/bc/member/update/](19-bc-members.md#doc-1739696704424961) để phân quyền thành viên.

---

## Lấy danh sách hóa đơn Business Center (`Get the invoices of a BC`)
<a id="doc-1740295890332674"></a>
<!-- doc_id: 1740295890332674 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/bc/invoice/get/`

**Mục đích**: Lấy danh sách các hóa đơn của tài khoản Business Center, bao gồm hóa đơn tín dụng, hóa đơn đối soát hoặc hóa đơn thanh toán tự động.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Có | Mã truy cập đã được ủy quyền. Xem [Xác thực](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (GET: query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `bc_id` | string | Có | ID của Business Center. |
| `invoice_id` | string | Không | ID hóa đơn cụ thể cần tra cứu. |
| `invoice_title` | string | Không | Tiêu đề hóa đơn cần tìm kiếm. |
| `invoice_types` | string[] | Có | Danh sách loại hóa đơn cần lọc. Truyền dưới dạng mảng JSON trong query string.<br><br>**Enum**:<br>• `RECON`: Hóa đơn đối soát (Reconciliation Invoice).<br>• `CREDIT`: Hóa đơn tín dụng (Credit Invoice).<br>• `AUTO_PAY`: Hóa đơn thanh toán tự động (Automatic Payment Invoice). *(Lưu ý: `AUTO_PAY` không thể dùng chung với các loại hóa đơn khác, phải truyền độc lập `["AUTO_PAY"]`).* |
| `pay_statuses` | string[] | Không | Trạng thái thanh toán của hóa đơn (`UNPAID`: Chưa thanh toán, `PAID`: Đã thanh toán, `PARTIAL_PAID`: Thanh toán một phần, `NO_NEED`: Không cần thanh toán). |
| `start_time` | string | Không | Thời gian bắt đầu phát hành hóa đơn, định dạng `"YYYY-MM-DD HH:MM:SS"`. Ví dụ: `"2024-01-01 00:00:00"`. Phải cung cấp cả `start_time` và `end_time` hoặc không chỉ định cả hai. |
| `end_time` | string | Không | Thời gian kết thúc phát hành hóa đơn, định dạng `"YYYY-MM-DD HH:MM:SS"`. |
| `page` | number | Không | Số trang dữ liệu. Mặc định: `1`. |
| `page_size` | number | Không | Số lượng bản ghi mỗi trang (từ `1` đến `50`). Mặc định: `10`. |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Giá trị `0` là thành công. Xem [Phụ lục mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Mã log định danh duy nhất của yêu cầu API. |
| `data` | object | Dữ liệu trả về. |
| ↳ `list` | object[] | Danh sách hóa đơn. |
| ↳↳ `invoice_id` | string | ID của hóa đơn. |
| ↳↳ `serial_number` | string | Số sê-ri hóa đơn. |
| ↳↳ `subject_id` | number | ID chủ thể hợp đồng. |
| ↳↳ `send_date` | string | Ngày phát hành hóa đơn (`YYYY-MM-DD`). |
| ↳↳ `currency_code` | string | Đơn vị tiền tệ của hóa đơn (ví dụ: `USD`, `VND`). |
| ↳↳ `status` | string | Trạng thái phê duyệt hóa đơn (`CREATED`, `SUBMITTED`, `APPROVED`, `DELETED`). |
| ↳↳ `due_date` | string | Hạn chót thanh toán hóa đơn. |
| ↳↳ `invoice_type` | string | Loại hóa đơn (`RECON`, `CREDIT`, `AUTO_PAY`). |
| ↳↳ `entity_serials` | string[] | Danh sách số sê-ri thực thể liên kết với hóa đơn. |
| ↳↳ `negative_invoice_ids` | object[] | ID và số sê-ri của các hóa đơn điều chỉnh giảm (negative invoices) liên kết đã được phê duyệt. |
| ↳↳↳ `invoice_id` | string | ID hóa đơn điều chỉnh giảm. |
| ↳↳↳ `serial_number` | string | Số sê-ri hóa đơn điều chỉnh giảm. |
| ↳↳ `positive_invoice_ids` | object[] | ID và số sê-ri của các hóa đơn gốc (positive invoices) liên kết. |
| ↳↳↳ `invoice_id` | string | ID hóa đơn gốc. |
| ↳↳↳ `serial_number` | string | Số sê-ri hóa đơn gốc. |
| ↳↳ `billing_group_id` | string | ID nhóm lập hóa đơn (Billing Group ID). |
| ↳↳ `account_name` | string | Tên tài khoản. |
| ↳↳ `invoice_title` | string | Tiêu đề hóa đơn. |
| ↳↳ `country_code` | string | Mã quốc gia lập hóa đơn. |
| ↳↳ `address` | string | Địa chỉ thanh toán của tài khoản. |
| ↳↳ `emails` | string[] | Danh sách email nhận thông báo thanh toán hóa đơn. |
| ↳↳ `tax_id1` | string | Mã số thuế thứ nhất. |
| ↳↳ `tax_id2` | string | Mã số thuế thứ hai. |
| ↳↳ `amount` | number | Tổng số tiền bao gồm thuế. |
| ↳↳ `amount_excluding_tax` | number | Tổng số tiền chưa bao gồm thuế. |
| ↳↳ `total_tax_amount` | number | Tổng số tiền thuế. |
| ↳↳ `tax_type1` | string | Loại thuế thứ nhất. |
| ↳↳ `tax_rate1` | number | Thuế suất thứ nhất. |
| ↳↳ `tax_amount1` | number | Tiền thuế thứ nhất. |
| ↳↳ `tax_type2` | string | Loại thuế thứ hai. |
| ↳↳ `tax_rate2` | number | Thuế suất thứ hai. |
| ↳↳ `tax_amount2` | number | Tiền thuế thứ hai. |
| ↳↳ `pay_status` | string | Trạng thái thanh toán của hóa đơn. |
| ↳↳ `overdue_status` | string | Trạng thái quá hạn (`INITIALIZED`, `YES`, `NO`). |
| ↳↳ `unpaid_amount` | number | Số tiền còn nợ chưa thanh toán. |
| ↳ `page_info` | object | Thông tin phân trang. |
| ↳↳ `page` | number | Trang hiện tại. |
| ↳↳ `page_size` | number | Số bản ghi mỗi trang. |
| ↳↳ `total_number` | number | Tổng số lượng hóa đơn. |
| ↳↳ `total_page` | number | Tổng số trang. |

### Ví dụ

#### cURL
```bash
curl -X GET "https://business-api.tiktok.com/open_api/v1.3/bc/invoice/get/?bc_id=7123456789012345678&invoice_types=%5B%22CREDIT%22%5D&page_size=20" \
  -H "Access-Token: ACCESS_TOKEN"
```

#### Python
```python
import json
import requests

ACCESS_TOKEN = "your_access_token"
BC_ID = "7123456789012345678"

url = "https://business-api.tiktok.com/open_api/v1.3/bc/invoice/get/"
headers = {"Access-Token": ACCESS_TOKEN}
params = {
    "bc_id": BC_ID,
    "invoice_types": json.dumps(["CREDIT"]),
    "page_size": 20
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

#### Phản hồi mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202410231500000601111222333444555",
  "data": {
    "list": [
      {
        "account_name": "Công ty TNHH Tiếp thị Toàn cầu",
        "address": "Tầng 10, Tòa nhà ABC, Hà Nội",
        "amount": 293.5,
        "amount_excluding_tax": 293.5,
        "billing_group_id": "7123456789012345000",
        "country_code": "VN",
        "currency_code": "USD",
        "entity_serials": ["ES12345678"],
        "invoice_id": "INV123456789",
        "invoice_title": "Công ty TNHH Tiếp thị Toàn cầu",
        "invoice_type": "CREDIT",
        "overdue_status": "NO",
        "pay_status": "UNPAID",
        "serial_number": "SN-2024-001",
        "status": "APPROVED",
        "unpaid_amount": 293.5
      }
    ],
    "page_info": {
      "page": 1,
      "page_size": 20,
      "total_number": 1,
      "total_page": 1
    }
  }
}
```

---

## Lấy số tiền chưa thanh toán (`Get the unpaid amount of a BC`)
<a id="doc-1740295904843777"></a>
<!-- doc_id: 1740295904843777 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/bc/invoice/unpaid/get/`

**Mục đích**: Lấy tổng số tiền nợ chưa thanh toán của tài khoản Business Center theo loại tiền tệ.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Có | Mã truy cập đã được ủy quyền. Xem [Xác thực](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (GET: query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `bc_id` | string | Có | ID của Business Center. |
| `invoice_type` | string | Có | Loại hóa đơn. Enum: `RECON` (Hóa đơn đối soát). |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Giá trị `0` là thành công. Xem [Phụ lục mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Mã log định danh duy nhất của yêu cầu API. |
| `data` | object | Dữ liệu trả về. |
| ↳ `result` | object | Kết quả số tiền chưa thanh toán và mã loại tiền tệ tương ứng. |
| ↳↳ `currency_code` | string | Mã đơn vị tiền tệ (ví dụ: `USD`, `VND`). |
| ↳↳ `amount` | number | Tổng số tiền nợ chưa thanh toán theo loại tiền tệ này. |

### Ví dụ

#### cURL
```bash
curl -X GET "https://business-api.tiktok.com/open_api/v1.3/bc/invoice/unpaid/get/?bc_id=7123456789012345678&invoice_type=RECON" \
  -H "Access-Token: ACCESS_TOKEN"
```

#### Python
```python
import requests

ACCESS_TOKEN = "your_access_token"
BC_ID = "7123456789012345678"

url = "https://business-api.tiktok.com/open_api/v1.3/bc/invoice/unpaid/get/"
headers = {"Access-Token": ACCESS_TOKEN}
params = {
    "bc_id": BC_ID,
    "invoice_type": "RECON"
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

#### Phản hồi mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20241023150000060222333444555666",
  "data": {
    "result": {
      "amount": 1540.5,
      "currency_code": "USD"
    }
  }
}
```

---

## Tổng quan tải xuống hóa đơn (`Download the invoices of a BC`)
<a id="doc-1740295923474433"></a>
<!-- doc_id: 1740295923474433 -->

Nhóm API này cung cấp các phương thức để tải xuống hóa đơn quảng cáo của Business Center:
- **Tải xuống đồng bộ**: Tải xuống tức thì một tệp hóa đơn cụ thể (định dạng PDF) qua [Tải xuống hóa đơn đồng bộ](20-bc-invoices.md#doc-1754000198430722).
- **Tải xuống bất đồng bộ**: Dành cho việc xuất số lượng lớn hóa đơn lịch sử hoặc báo cáo giao dịch chi tiết qua [Tổng quan tải xuống bất đồng bộ](20-bc-invoices.md#doc-1754000224141313).

---

## Tải xuống hóa đơn đồng bộ (`Download synchronously`)
<a id="doc-1754000198430722"></a>
<!-- doc_id: 1754000198430722 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/bc/invoice/download/`

**Mục đích**: Tải xuống trực tiếp luồng dữ liệu tệp PDF của một hóa đơn cụ thể trong Business Center theo phương thức đồng bộ.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Có | Mã truy cập đã được ủy quyền. Xem [Xác thực](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (GET: query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `bc_id` | string | Có | ID của Business Center. |
| `invoice_id` | string | Có | ID của hóa đơn cần tải xuống (tra cứu qua [/bc/invoice/get/](20-bc-invoices.md#doc-1740295890332674)). |

### Phản hồi

Khi thành công, API trả về luồng dữ liệu tệp nhị phân PDF (`application/pdf`). Trong trường hợp yêu cầu thất bại, API sẽ trả về JSON chứa mã lỗi:

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã lỗi phản hồi. Xem [Phụ lục mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông báo lỗi chi tiết. |
| `request_id` | string | Mã log định danh duy nhất của yêu cầu API. |

### Ví dụ

#### cURL
```bash
curl -X GET "https://business-api.tiktok.com/open_api/v1.3/bc/invoice/download/?bc_id=7123456789012345678&invoice_id=INV123456789" \
  -H "Access-Token: ACCESS_TOKEN" \
  --output invoice_INV123456789.pdf
```

#### Python
```python
import requests

ACCESS_TOKEN = "your_access_token"
BC_ID = "7123456789012345678"
INVOICE_ID = "INV123456789"

url = "https://business-api.tiktok.com/open_api/v1.3/bc/invoice/download/"
headers = {"Access-Token": ACCESS_TOKEN}
params = {
    "bc_id": BC_ID,
    "invoice_id": INVOICE_ID
}

response = requests.get(url, headers=headers, params=params)
if response.status_code == 200 and "application/pdf" in response.headers.get("Content-Type", ""):
    with open(f"invoice_{INVOICE_ID}.pdf", "wb") as f:
        f.write(response.content)
    print("Tải hóa đơn PDF thành công!")
else:
    print("Lỗi tải hóa đơn:", response.json())
```
---

## Tổng quan tải xuống bất đồng bộ (`Download asynchronously`)
<a id="doc-1754000224141313"></a>
<!-- doc_id: 1754000224141313 -->

Tải xuống bất đồng bộ cho phép xuất số lượng lớn hóa đơn lịch sử hoặc báo cáo giao dịch chi tiết mà không làm nghẽn luồng xử lý của hệ thống. Quy trình gồm 3 bước:
1. [Tạo tác vụ tải xuống bất đồng bộ](20-bc-invoices.md#doc-1754000448122882): Khởi tạo tác vụ và nhận mã `task_id`.
2. [Lấy thông tin tác vụ tải xuống bất đồng bộ](20-bc-invoices.md#doc-1754000480307265): Kiểm tra tiến độ xử lý và lấy luồng tệp Excel trực tiếp cho báo cáo thanh toán.
3. [Lấy danh sách tác vụ tải xuống bất đồng bộ](20-bc-invoices.md#doc-1754000504437762): Xem danh sách các tác vụ đã tạo và lấy đường dẫn URL để tải tệp hóa đơn về máy.

---

## Tạo tác vụ tải xuống bất đồng bộ (`Create an asynchronous download task`)
<a id="doc-1754000448122882"></a>
<!-- doc_id: 1754000448122882 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/bc/invoice/task/create/`

**Mục đích**: Tạo một tác vụ tải xuống hóa đơn hoặc báo cáo giao dịch bất đồng bộ. Sau khi tạo tác vụ thành công, API sẽ trả về `task_id`.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Có | Mã truy cập đã được ủy quyền. Xem [Xác thực](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| `Content-Type` | string | Có | Định dạng nội dung yêu cầu. Giá trị cho phép: `application/json`. |

### Tham số (POST: JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `bc_id` | string | Có | ID của Business Center. |
| `download_type` | string | Có | Loại tải xuống.<br><br>**Enum**:<br>• `INVOICE_LIST`: Danh sách hóa đơn định dạng Excel (tối đa 100 hóa đơn).<br>• `INVOICE_BATCH`: Gói tải xuống nhiều hóa đơn định dạng nén ZIP (chứa các tệp hóa đơn PDF).<br>• `BILLING_REPORT`: Báo cáo chi tiết các giao dịch thanh toán định dạng Excel. |
| `invoice_id` | string | Điều kiện | Bắt buộc khi `download_type` là `BILLING_REPORT`. Tùy chọn lọc khi `download_type` là `INVOICE_LIST` hoặc `INVOICE_BATCH`. ID hóa đơn. |
| `filtering` | object | Không | Điều kiện lọc danh sách hóa đơn cần xuất. |
| ↳ `invoice_title` | string | Không | Tiêu đề hóa đơn cần lọc. |
| ↳ `serial_number` | string | Không | Số sê-ri hóa đơn. |
| ↳ `billing_group_id` | string | Không | ID nhóm lập hóa đơn. Tra cứu qua [/bc/billing_group/get/](17-bc-billing-groups.md#doc-1738944324279297). |
| ↳ `pay_statuses` | string[] | Không | Danh sách trạng thái thanh toán (`UNPAID`, `PAID`, `PARTIAL_PAID`, `NO_NEED`). |
| ↳ `start_time` | string | Không | Ngày bắt đầu phát hành hóa đơn (`YYYY-MM-DD` theo UTC+0). |
| ↳ `end_time` | string | Không | Ngày kết thúc phát hành hóa đơn (`YYYY-MM-DD` theo UTC+0). |
| ↳ `campaign_id` | string | Không | Chỉ áp dụng khi `download_type` là `INVOICE_LIST` hoặc `INVOICE_BATCH`. ID chiến dịch quảng cáo. |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Giá trị `0` là thành công. Xem [Phụ lục mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Mã log định danh duy nhất của yêu cầu API. |
| `data` | object | Dữ liệu trả về. |
| ↳ `task_id` | string | ID của tác vụ tải xuống bất đồng bộ vừa được tạo. |

### Ví dụ

#### cURL
```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/bc/invoice/task/create/" \
  -H "Access-Token: ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "bc_id": "7123456789012345678",
    "download_type": "INVOICE_BATCH",
    "filtering": {
      "pay_statuses": ["UNPAID", "PAID"],
      "start_time": "2024-10-01",
      "end_time": "2024-10-31"
    }
  }'
```

#### Phản hồi mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20241023150000060333444555666777",
  "data": {
    "task_id": "task_1234567890abcdef"
  }
}
```

---

## Lấy thông tin tác vụ tải xuống bất đồng bộ (`Get asynchronous download tasks`)
<a id="doc-1754000480307265"></a>
<!-- doc_id: 1754000480307265 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/bc/invoice/task/get/`

**Mục đích**: Kiểm tra xem tác vụ xuất báo cáo giao dịch `BILLING_REPORT` đã hoàn thành hay chưa. Nếu tác vụ hoàn tất thành công, API sẽ trả về trực tiếp luồng tệp Excel (`.xlsx`).

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Có | Mã truy cập đã được ủy quyền. Xem [Xác thực](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (GET: query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `bc_id` | string | Có | ID của Business Center. |
| `task_id` | string | Có | ID của tác vụ tải xuống (lấy từ [/bc/invoice/task/create/](20-bc-invoices.md#doc-1754000480307265)). |

### Phản hồi

Nếu tác vụ hoàn thành thành công, API trả về luồng tệp Excel (.xlsx). Nếu tác vụ đang chạy hoặc gặp lỗi, API trả về JSON:

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Giá trị `0` là thành công. Xem [Phụ lục mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Mã log định danh duy nhất của yêu cầu API. |
| `data` | object | Dữ liệu trả về. |
| ↳ `status` | string | Trạng thái tác vụ bất đồng bộ (`CREATED`, `RUNNING`, `SUCCEED`, `FAILED`, `POLLING`). |
| ↳ `download_url` | string | URL tải tệp kết quả (nếu có). |
| ↳ `error_msg` | string | Thông báo lỗi chi tiết nếu tác vụ thất bại. |

### Ví dụ

#### cURL
```bash
curl -X GET "https://business-api.tiktok.com/open_api/v1.3/bc/invoice/task/get/?bc_id=7123456789012345678&task_id=task_1234567890abcdef" \
  -H "Access-Token: ACCESS_TOKEN" \
  --output billing_report.xlsx
```

#### Python
```python
import requests

ACCESS_TOKEN = "your_access_token"
BC_ID = "7123456789012345678"
TASK_ID = "task_1234567890abcdef"

url = "https://business-api.tiktok.com/open_api/v1.3/bc/invoice/task/get/"
headers = {"Access-Token": ACCESS_TOKEN}
params = {
    "bc_id": BC_ID,
    "task_id": TASK_ID
}

response = requests.get(url, headers=headers, params=params)
if response.status_code == 200 and "application/vnd.openxmlformats" in response.headers.get("Content-Type", ""):
    with open("billing_report.xlsx", "wb") as f:
        f.write(response.content)
    print("Tải tệp Excel thành công!")
else:
    print("Thông tin trạng thái tác vụ:", response.json())
```

---

## Lấy danh sách tác vụ tải xuống bất đồng bộ (`Get asynchronous download task list`)
<a id="doc-1754000504437762"></a>
<!-- doc_id: 1754000504437762 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/bc/invoice/task/list/`

**Mục đích**: Lấy danh sách các tác vụ tải xuống bất đồng bộ thuộc các loại `BILLING_REPORT`, `INVOICE_LIST` và `INVOICE_BATCH`. Khi tác vụ đã hoàn thành, bạn có thể tải tệp trực tiếp từ đường dẫn `download_url` trả về trong phản hồi.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Có | Mã truy cập đã được ủy quyền. Xem [Xác thực](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (GET: query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `bc_id` | string | Có | ID của Business Center. |
| `page` | number | Không | Số trang dữ liệu. Mặc định: `1`. |
| `page_size` | number | Không | Số lượng tác vụ mỗi trang (từ `1` đến `50`). Mặc định: `10`. |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Giá trị `0` là thành công. Xem [Phụ lục mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Mã log định danh duy nhất của yêu cầu API. |
| `data` | object | Dữ liệu trả về. |
| ↳ `list` | object[] | Danh sách các tác vụ tải xuống. |
| ↳↳ `bc_id` | string | ID của Business Center. |
| ↳↳ `task_id` | string | ID của tác vụ tải xuống. |
| ↳↳ `status` | string | Trạng thái của tác vụ (`RUNNING`: Đang chạy, `SUCCEED`: Thành công, `FAILED`: Thất bại). |
| ↳↳ `create_time` | string | Thời điểm tạo tác vụ. |
| ↳↳ `update_time` | string | Thời điểm cập nhật trạng thái tác vụ gần nhất. |
| ↳↳ `download_url` | string | Đường dẫn URL để tải tệp hóa đơn/báo cáo về máy (chỉ xuất hiện khi `status` là `SUCCEED`). |
| ↳↳ `download_type` | string | Loại tệp tải xuống (`INVOICE_LIST`, `INVOICE_BATCH`, `BILLING_REPORT`). |
| ↳ `page_info` | object | Thông tin phân trang. |
| ↳↳ `page` | number | Trang hiện tại. |
| ↳↳ `page_size` | number | Số lượng bản ghi mỗi trang. |
| ↳↳ `total_number` | number | Tổng số lượng tác vụ. |
| ↳↳ `total_page` | number | Tổng số trang kết quả. |

### Ví dụ

#### cURL
```bash
curl -X GET "https://business-api.tiktok.com/open_api/v1.3/bc/invoice/task/list/?bc_id=7123456789012345678&page=1&page_size=10" \
  -H "Access-Token: ACCESS_TOKEN"
```

#### Python
```python
import requests

ACCESS_TOKEN = "your_access_token"
BC_ID = "7123456789012345678"

url = "https://business-api.tiktok.com/open_api/v1.3/bc/invoice/task/list/"
headers = {"Access-Token": ACCESS_TOKEN}
params = {
    "bc_id": BC_ID,
    "page": 1,
    "page_size": 10
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

#### Phản hồi mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20241023150000060444555666777888",
  "data": {
    "list": [
      {
        "bc_id": "7123456789012345678",
        "create_time": "1729000000",
        "download_type": "INVOICE_BATCH",
        "download_url": "https://tiktok-business-downloads.s3.amazonaws.com/invoices/batch_123.zip",
        "status": "SUCCEED",
        "task_id": "task_1234567890abcdef",
        "update_time": "1729000300"
      }
    ],
    "page_info": {
      "page": 1,
      "page_size": 10,
      "total_number": 1,
      "total_page": 1
    }
  }
}
```
