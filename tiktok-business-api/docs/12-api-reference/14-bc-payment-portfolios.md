# Danh mục thanh toán Business Center (BC Payment Portfolios)
<a id="doc-1839151483689986"></a>
<!-- doc_id: 1839151483689986 -->

Danh mục thanh toán (Payment Portfolio) là tính năng nâng cao trong TikTok Business Center cho phép gom nhóm các tài khoản quảng cáo và chia sẻ hạn mức tín dụng hoặc số dư tiền mặt chung. Tính năng này giúp các doanh nghiệp và đại lý phân bổ ngân sách linh hoạt, giới hạn rủi ro tài chính theo từng nhóm khách hàng hoặc dự án, đồng thời quản lý quyền truy cập của người dùng đối với nguồn tiền một cách an toàn và minh bạch.

Các loại Danh mục thanh toán chính:
* `SHARED_CASH`: Danh mục thanh toán chia sẻ tiền mặt.
* `ADVANCED`: Danh mục thanh toán nâng cao (hỗ trợ phân bổ tỷ lệ hạn mức tín dụng).

Nhóm API này bao gồm các endpoint sau:
* [Lấy danh sách danh mục thanh toán](14-bc-payment-portfolios.md#doc-1839151931301954)
* [Tạo danh mục thanh toán](14-bc-payment-portfolios.md#doc-1839151986039809)
* [Liên kết tài khoản quảng cáo với danh mục thanh toán](14-bc-payment-portfolios.md#doc-1839151992566081)
* [Phân bổ hạn mức tín dụng cho danh mục thanh toán](14-bc-payment-portfolios.md#doc-1839151998450754)
* [Lấy danh sách tài khoản quảng cáo liên kết với danh mục thanh toán](14-bc-payment-portfolios.md#doc-1839152005599234)
* [Lấy danh sách người dùng được ủy quyền cho danh mục thanh toán](14-bc-payment-portfolios.md#doc-1839152031645121)

---

## Lấy danh sách danh mục thanh toán (`Get Payment Portfolios`)
<a id="doc-1839151931301954"></a>
<!-- doc_id: 1839151931301954 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/payment_portfolio/get/`

**Mục đích**: Sử dụng endpoint này để lấy danh sách các danh mục thanh toán trong Business Center, bao gồm ID, tên, loại danh mục, số lượng tài khoản quảng cáo và người dùng liên kết, số dư tiền mặt và thông tin phân bổ hạn mức tín dụng.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền (access token). Xem chi tiết tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (GET query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| bc_id | string | Bắt buộc | ID của Business Center cần lấy danh mục thanh toán. |
| filtering | object | Không bắt buộc | Điều kiện lọc danh mục thanh toán (chuỗi JSON đối tượng). |
| ↳ payment_portfolio_ids | string[] | Không bắt buộc | Danh sách ID danh mục thanh toán cần lọc. Kích thước tối đa: 50. |
| ↳ payment_portfolio_type | string | Không bắt buộc | Loại danh mục thanh toán: `SHARED_CASH`, `ADVANCED`. |
| ↳ bc_related | boolean | Không bắt buộc | Có chỉ trả về các danh mục thanh toán được liên kết trực tiếp với Business Center này hay không. |
| page | integer | Không bắt buộc | Số trang hiện tại. Giá trị: ≥ 1. Mặc định: 1. |
| page_size | integer | Không bắt buộc | Số bản ghi mỗi trang. Khoảng giá trị: 1-50. Mặc định: 10. |

### Ví dụ

#### cURL
```bash
curl --get -H "Access-Token: YOUR_ACCESS_TOKEN" --data-urlencode "bc_id=7000000000000000000" --data-urlencode "page=1" --data-urlencode "page_size=10" https://business-api.tiktok.com/open_api/v1.3/payment_portfolio/get/
```

#### Python
```python
import os
import requests

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", "YOUR_ACCESS_TOKEN")
BC_ID = os.environ.get("BC_ID", "7000000000000000000")

url = "https://business-api.tiktok.com/open_api/v1.3/payment_portfolio/get/"
headers = {
    "Access-Token": ACCESS_TOKEN,
}
params = {
    "bc_id": BC_ID,
    "page": 1,
    "page_size": 10,
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. |
| request_id | string | Mã nhật ký định danh yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ payment_portfolio_list | object[] | Danh sách các danh mục thanh toán. |
| ↳↳ payment_portfolio_id | string | ID danh mục thanh toán. |
| ↳↳ payment_portfolio_name | string | Tên danh mục thanh toán. |
| ↳↳ payment_portfolio_type | string | Loại danh mục thanh toán: `SHARED_CASH`, `ADVANCED`. |
| ↳↳ linked_advertiser_account_count | number | Số lượng tài khoản quảng cáo liên kết với danh mục. |
| ↳↳ user_count | number | Số lượng người dùng có quyền truy cập vào danh mục. |
| ↳↳ cash_balance_list | object[] | Danh sách số dư tiền mặt trong danh mục thanh toán. |
| ↳↳↳ currency | string | Đơn vị tiền tệ. |
| ↳↳↳ amount | number | Số dư tiền mặt theo đơn vị tiền tệ đó. |
| ↳↳ credit_line_allocation | object | Chi tiết phân bổ hạn mức tín dụng cho danh mục thanh toán. |
| ↳↳↳ allocated_amount | number | Tổng hạn mức tín dụng được phân bổ. |
| ↳↳↳ used_amount | number | Hạn mức tín dụng đã sử dụng. |
| ↳↳↳ available_amount | number | Hạn mức tín dụng khả dụng còn lại (`allocated_amount - used_amount`). |
| ↳↳↳ min_allocation_percentage | number | Tỷ lệ phân bổ tối thiểu bắt buộc (lấy 4 chữ số thập phân). |
| ↳ page_info | object | Thông tin phân trang. |
| ↳↳ page | number | Trang hiện tại. |
| ↳↳ page_size | number | Kích thước trang. |
| ↳↳ total_number | number | Tổng số danh mục thanh toán. |
| ↳↳ total_page | number | Tổng số trang. |

---

## Tạo danh mục thanh toán (`Create a Payment Portfolio`)
<a id="doc-1839151986039809"></a>
<!-- doc_id: 1839151986039809 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/payment_portfolio/create/`

**Mục đích**: Sử dụng endpoint này để khởi tạo một Danh mục thanh toán mới và liên kết các tài khoản quảng cáo ban đầu vào danh mục đó.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền (access token). Xem chi tiết tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type | string | Bắt buộc | Định dạng nội dung yêu cầu. Giá trị: `application/json`. |

### Tham số (POST JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| payment_portfolio_name | string | Bắt buộc | Tên danh mục thanh toán muốn tạo. |
| advertiser_ids | string[] | Bắt buộc | Danh sách ID các tài khoản quảng cáo cần đưa vào danh mục thanh toán này. |
| payment_portfolio_type | string | Không bắt buộc | Loại danh mục thanh toán. Các giá trị enum: `SHARED_CASH`, `ADVANCED`. Mặc định: `SHARED_CASH`. |

### Ví dụ

```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/payment_portfolio/create/' --header 'Access-Token: YOUR_ACCESS_TOKEN' --header 'Content-Type: application/json' --data-raw '{
  "payment_portfolio_name": "Danh mục Nhãn hàng A",
  "payment_portfolio_type": "SHARED_CASH",
  "advertiser_ids": [
    "7123456789012345678",
    "7123456789012345679"
  ]
}'
```

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. |
| request_id | string | Mã nhật ký định danh yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ payment_portfolio_id | string | ID của danh mục thanh toán vừa được tạo thành công. |
| ↳ payment_portfolio_name | string | Tên danh mục thanh toán vừa tạo. |
| ↳ payment_portfolio_type | string | Loại danh mục thanh toán (`SHARED_CASH` hoặc `ADVANCED`). |

### Ví dụ phản hồi

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202605210639490102360430824C1AE673",
  "data": {
    "payment_portfolio_id": "portfolio_123456789",
    "payment_portfolio_name": "Danh mục Nhãn hàng A",
    "payment_portfolio_type": "SHARED_CASH"
  }
}
```

---

## Liên kết tài khoản quảng cáo với danh mục thanh toán (`Link ad accounts to a Payment Portfolio`)
<a id="doc-1839151992566081"></a>
<!-- doc_id: 1839151992566081 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/payment_portfolio/advertiser/update/`

**Mục đích**: Sử dụng endpoint này để liên kết thêm các tài khoản quảng cáo vào một Danh mục thanh toán nâng cao (`ADVANCED`) đã có sẵn.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền (access token). Xem chi tiết tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type | string | Bắt buộc | Định dạng nội dung yêu cầu. Giá trị: `application/json`. |

### Tham số (POST JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| payment_portfolio_id | string | Bắt buộc | ID của Danh mục thanh toán nâng cao cần liên kết. |
| advertiser_ids | string[] | Bắt buộc | Danh sách ID các tài khoản quảng cáo muốn gắn vào danh mục thanh toán. |

### Ví dụ

```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/payment_portfolio/advertiser/update/' --header 'Access-Token: YOUR_ACCESS_TOKEN' --header 'Content-Type: application/json' --data-raw '{
  "payment_portfolio_id": "portfolio_123456789",
  "advertiser_ids": ["7123456789012345680"]
}'
```

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. |
| request_id | string | Mã nhật ký định danh yêu cầu. |
| data | object | Dữ liệu trả về (đối tượng rỗng khi thành công). |

---

## Phân bổ hạn mức tín dụng cho danh mục thanh toán (`Allocate the credit line to Payment Portfolios`)
<a id="doc-1839151998450754"></a>
<!-- doc_id: 1839151998450754 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/payment_portfolio/credit_line/update/`

**Mục đích**: Sử dụng endpoint này để điều chỉnh hoặc phân bổ tỷ lệ phần trăm hạn mức tín dụng của Business Center cho các Danh mục thanh toán nâng cao (`ADVANCED`).

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền (access token). Xem chi tiết tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type | string | Bắt buộc | Định dạng nội dung yêu cầu. Giá trị: `application/json`. |

### Tham số (POST JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| allocation_details | object[] | Bắt buộc | Danh sách chi tiết phân bổ hạn mức tín dụng. Kích thước tối đa: 10 đối tượng. |
| ↳ payment_portfolio_id | string | Bắt buộc | ID của Danh mục thanh toán nâng cao. |
| ↳ allocation_percentage | number | Bắt buộc | Tỷ lệ phần trăm hạn mức tín dụng phân bổ cho danh mục (giá trị phần trăm, ví dụ `25.5` ứng với 25.5%). |

### Ví dụ

```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/payment_portfolio/credit_line/update/' --header 'Access-Token: YOUR_ACCESS_TOKEN' --header 'Content-Type: application/json' --data-raw '{
  "allocation_details": [
    {
      "payment_portfolio_id": "portfolio_123456789",
      "allocation_percentage": 50.0
    },
    {
      "payment_portfolio_id": "portfolio_987654321",
      "allocation_percentage": 30.0
    }
  ]
}'
```

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. |
| request_id | string | Mã nhật ký định danh yêu cầu. |
| data | object | Dữ liệu trả về (đối tượng rỗng khi thành công). |

---

## Lấy danh sách tài khoản quảng cáo liên kết với danh mục thanh toán (`Get ad accounts linked to a Payment Portfolio`)
<a id="doc-1839152005599234"></a>
<!-- doc_id: 1839152005599234 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/payment_portfolio/advertiser/get/`

**Mục đích**: Sử dụng endpoint này để lấy danh sách toàn bộ các tài khoản quảng cáo đang được liên kết vào một Danh mục thanh toán cụ thể.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền (access token). Xem chi tiết tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (GET query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| payment_portfolio_id | string | Bắt buộc | ID của Danh mục thanh toán cần tra cứu tài khoản quảng cáo. |
| page | integer | Không bắt buộc | Số trang hiện tại. Khoảng giá trị: ≥ 1. Mặc định: 1. |
| page_size | integer | Không bắt buộc | Số bản ghi mỗi trang. Khoảng giá trị: 1-50. Mặc định: 10. |

### Ví dụ

#### cURL
```bash
curl --get -H "Access-Token: YOUR_ACCESS_TOKEN" --data-urlencode "payment_portfolio_id=portfolio_123456789" --data-urlencode "page=1" --data-urlencode "page_size=10" https://business-api.tiktok.com/open_api/v1.3/payment_portfolio/advertiser/get/
```

#### Python
```python
import os
import requests

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", "YOUR_ACCESS_TOKEN")

url = "https://business-api.tiktok.com/open_api/v1.3/payment_portfolio/advertiser/get/"
headers = {
    "Access-Token": ACCESS_TOKEN,
}
params = {
    "payment_portfolio_id": "portfolio_123456789",
    "page": 1,
    "page_size": 10,
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. |
| request_id | string | Mã nhật ký định danh yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ advertiser_list | object[] | Danh sách các tài khoản quảng cáo liên kết. |
| ↳↳ advertiser_id | string | ID tài khoản quảng cáo. |
| ↳↳ advertiser_name | string | Tên tài khoản quảng cáo. |
| ↳ page_info | object | Thông tin phân trang. |
| ↳↳ page | number | Trang hiện tại. |
| ↳↳ page_size | number | Kích thước trang. |
| ↳↳ total_number | number | Tổng số tài khoản liên kết. |
| ↳↳ total_page | number | Tổng số trang. |

---

## Lấy danh sách người dùng được ủy quyền cho danh mục thanh toán (`Get authorized users for a Payment Portfolio`)
<a id="doc-1839152031645121"></a>
<!-- doc_id: 1839152031645121 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/payment_portfolio/user/get/`

**Mục đích**: Sử dụng endpoint này để lấy danh sách tất cả người dùng trong Business Center được cấp quyền truy cập và sử dụng nguồn tiền của một Danh mục thanh toán.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền (access token). Xem chi tiết tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (GET query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| payment_portfolio_id | string | Bắt buộc | ID của Danh mục thanh toán cần tra cứu người dùng. |
| page | integer | Không bắt buộc | Số trang hiện tại. Khoảng giá trị: ≥ 1. Mặc định: 1. |
| page_size | integer | Không bắt buộc | Số bản ghi mỗi trang. Khoảng giá trị: 1-50. Mặc định: 10. |

### Ví dụ

#### cURL
```bash
curl --get -H "Access-Token: YOUR_ACCESS_TOKEN" --data-urlencode "payment_portfolio_id=portfolio_123456789" --data-urlencode "page=1" --data-urlencode "page_size=10" https://business-api.tiktok.com/open_api/v1.3/payment_portfolio/user/get/
```

#### Python
```python
import os
import requests

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", "YOUR_ACCESS_TOKEN")

url = "https://business-api.tiktok.com/open_api/v1.3/payment_portfolio/user/get/"
headers = {
    "Access-Token": ACCESS_TOKEN,
}
params = {
    "payment_portfolio_id": "portfolio_123456789",
    "page": 1,
    "page_size": 10,
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. |
| request_id | string | Mã nhật ký định danh yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ users | object[] | Danh sách người dùng được ủy quyền trong danh mục thanh toán. |
| ↳↳ user_id | string | ID người dùng TikTok Business Center. |
| ↳↳ user_name | string | Tên người dùng. |
| ↳ page_info | object | Thông tin phân trang. |
| ↳↳ page | number | Trang hiện tại. |
| ↳↳ page_size | number | Kích thước trang. |
| ↳↳ total_number | number | Tổng số người dùng. |
| ↳↳ total_page | number | Tổng số trang. |

### Ví dụ phản hồi

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202605210639490102360430824C1AE673",
  "data": {
    "users": [
      {
        "user_id": "6912345678901234567",
        "user_name": "nguyenvana"
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
