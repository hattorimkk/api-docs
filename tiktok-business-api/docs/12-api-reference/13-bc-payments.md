# Thanh toán Business Center (BC Payments)
<a id="doc-1739939078695937"></a>
<!-- doc_id: 1739939078695937 -->

Bộ API Thanh toán Business Center (BC Payments) cung cấp các giải pháp quản lý tài chính và dòng tiền toàn diện trên TikTok Business Center. Cả Business Center dạng Đại lý (Agency) và Trực tiếp (Direct) đều có thể sử dụng các API này để:
* Nạp tiền hoặc khấu trừ tiền giữa Business Center và các tài khoản quảng cáo trực thuộc.
* Tăng hoặc giảm hạn mức tín dụng (credit balance) của Business Center.
* Tra cứu số dư chi tiết (tiền mặt, phiếu giảm giá voucher/grant, tín dụng, số dư đóng băng) và ngân sách của các tài khoản quảng cáo.
* Tra cứu số dư của Business Center.
* Truy vấn lịch sử giao dịch nạp/rút/chuyển tiền ở cấp độ Business Center và tài khoản quảng cáo.
* Xem lịch sử thay đổi ngân sách và báo cáo ghi nhận chi phí (cost records) cùng các khoản thuế ước tính.

> [!NOTE]
> Chỉ người dùng có vai trò Quản lý tài chính (Finance Manager) trong Business Center mới có quyền thực hiện các thao tác chuyển tiền, nạp tiền và khấu trừ. Bạn có thể sử dụng **/bc/member/invite/** để mời thành viên và cấp quyền tài chính.

Nhóm API này bao gồm các endpoint sau:
* [Thực hiện thanh toán / chuyển tiền](13-bc-payments.md#doc-1739939095321601)
* [Lấy số dư và ngân sách của tài khoản quảng cáo](13-bc-payments.md#doc-1739939106470913)
* [Lấy số dư của Business Center](13-bc-payments.md#doc-1739939128198145)
* [Lấy lịch sử giao dịch của BC hoặc tài khoản quảng cáo](13-bc-payments.md#doc-1792849810925569)
* [Lấy lịch sử giao dịch của tài khoản quảng cáo](13-bc-payments.md#doc-1739939116353538)
* [Lấy lịch sử giao dịch của Business Center](13-bc-payments.md#doc-1739939140408322)
* [Lấy lịch sử thay đổi ngân sách của tài khoản quảng cáo](13-bc-payments.md#doc-1830173979548674)
* [Lấy bản ghi chi phí của BC và tài khoản quảng cáo](13-bc-payments.md#doc-1829079287639041)

---

## Thực hiện thanh toán / chuyển tiền (`Process a payment`)
<a id="doc-1739939095321601"></a>
<!-- doc_id: 1739939095321601 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/bc/transfer/`

**Mục đích**: Sử dụng endpoint này để nạp tiền vào hoặc khấu trừ tiền từ tài khoản quảng cáo thuộc Business Center, hoặc để tăng / giảm số dư hạn mức tín dụng của Business Center.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền (access token). Xem chi tiết tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type | string | Bắt buộc | Định dạng nội dung yêu cầu. Giá trị: `application/json`. |

### Tham số (POST JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| bc_id | string | Bắt buộc | ID của Business Center thực hiện giao dịch. |
| transfer_level | string | Không bắt buộc | Cấp độ chuyển tiền. Các giá trị enum:<br>• `ADVERTISER`: Nạp hoặc rút tiền đối với tài khoản quảng cáo.<br>• `BC`: Tăng hoặc giảm hạn mức tín dụng của Business Center.<br>Mặc định: `ADVERTISER`. |
| advertiser_id | string | Điều kiện | ID tài khoản quảng cáo. Bắt buộc khi `transfer_level` là `ADVERTISER`. |
| payment_portfolio_id | string | Điều kiện | ID danh mục thanh toán (Payment Portfolio). Bắt buộc nếu Business Center có nhiều Payment Portfolio và liên kết với tài khoản quảng cáo. |
| transfer_type | string | Bắt buộc | Loại thao tác xử lý thanh toán:<br>• `RECHARGE`: Nạp tiền vào tài khoản quảng cáo hoặc tăng hạn mức tín dụng BC.<br>• `DEDUCT`: Rút/khấu trừ tiền từ tài khoản quảng cáo hoặc giảm hạn mức tín dụng BC. |
| amount_info | object | Điều kiện | Thông tin chi tiết số tiền cần xử lý theo từng loại số dư (chỉ áp dụng khi `transfer_level` là `ADVERTISER`). Cần chỉ định một trong hai cách: dùng `amount_info` hoặc dùng các trường số tiền riêng lẻ (`cash_amount`, `grant_amount`). |
| ↳ cash_amount | number | Không bắt buộc | Số tiền mặt muốn xử lý. |
| ↳ grant_amount | number | Không bắt buộc | Số tiền phiếu ưu đãi / voucher muốn xử lý. |
| ↳ credit_amount | number | Không bắt buộc | Số tiền tín dụng muốn xử lý. |
| cash_amount | number | Điều kiện | Số tiền mặt muốn nạp hoặc trừ. |
| grant_amount | number | Điều kiện | Số tiền voucher muốn nạp hoặc trừ. |
| request_id | string | Không bắt buộc | Mã định danh yêu cầu duy nhất để đảm bảo tính bất biến (idempotency), tránh lặp giao dịch khi gửi lại yêu cầu. |

### Ví dụ

```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/bc/transfer/' --header 'Access-Token: YOUR_ACCESS_TOKEN' --header 'Content-Type: application/json' --data-raw '{
  "bc_id": "7000000000000000000",
  "transfer_level": "ADVERTISER",
  "advertiser_id": "7123456789012345678",
  "transfer_type": "RECHARGE",
  "cash_amount": 500.0,
  "request_id": "req_transfer_202605210001"
}'
```

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Appendix-Return codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. |
| request_id | string | Mã nhật ký định danh yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ bc_id | number | ID Business Center. |
| ↳ advertiser_id | number | ID tài khoản quảng cáo. |
| ↳ transaction_infos | object[] | Chi tiết các giao dịch chuyển tiền được thực hiện. |
| ↳↳ transaction_id | string | ID giao dịch chuyển tiền. |
| ↳↳ transaction_type | string | Loại giao dịch: `CASH` (tiền mặt), `GRANT` (voucher), `CREDIT` (tín dụng). |
| ↳↳ payee_account | object | Thông tin tài khoản thụ hưởng (nhận tiền). |
| ↳↳↳ account_type | string | Loại tài khoản: `BC` (Business Center), `ADVERTISER` (tài khoản quảng cáo). |
| ↳↳↳ account_id | string | ID của tài khoản thụ hưởng. |
| ↳↳ remitter_account | object | Thông tin tài khoản chuyển tiền (nguồn tiền). |
| ↳↳↳ account_type | string | Loại tài khoản: `BC`, `ADVERTISER`. |
| ↳↳↳ account_id | string | ID tài khoản chuyển tiền. |

---

## Lấy số dư và ngân sách của tài khoản quảng cáo (`Get the balance and budget of ad accounts`)
<a id="doc-1739939106470913"></a>
<!-- doc_id: 1739939106470913 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/advertiser/balance/get/`

**Mục đích**: Sử dụng endpoint này để lấy số dư chi tiết (số dư khả dụng, tiền mặt, voucher, tín dụng, số dư đóng băng) và ngân sách của các tài khoản quảng cáo thuộc Business Center.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền (access token). Xem chi tiết tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (GET query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| bc_id | string | Bắt buộc | ID Business Center. |
| fields | string[] | Không bắt buộc | Danh sách các trường thông tin bổ sung cần trả về trong phản hồi. Giá trị hỗ trợ: `account_open_days`, `balance_reminder`, `transfer_balance`, `valid_account_balance`, `frozen_balance`, `cash_balance`, `grant_balance`, `credit_balance`, `budget_mode`, `budget`, `payment_portfolio_id`, `payment_portfolio_name`. |
| filtering | object | Không bắt buộc | Bộ lọc tài khoản quảng cáo (chuỗi JSON đối tượng). |
| ↳ keyword | string | Không bắt buộc | Từ khóa tìm kiếm theo tên hoặc ID tài khoản quảng cáo. |
| ↳ advertiser_status | string[] | Không bắt buộc | Trạng thái hiển thị tài khoản: `SHOW_ACCOUNT_STATUS_NOT_APPROVED`, `SHOW_ACCOUNT_STATUS_APPROVED`, `SHOW_ACCOUNT_STATUS_PUNISHED`, v.v. |
| ↳ payment_portfolio_id | string | Không bắt buộc | Lọc theo ID danh mục thanh toán (Payment Portfolio). |
| page | number | Không bắt buộc | Số trang hiện tại. Khoảng giá trị: ≥ 1. Mặc định: 1. |
| page_size | number | Không bắt buộc | Số bản ghi mỗi trang. Khoảng giá trị: 1-50. Mặc định: 10. |

### Ví dụ

#### cURL
```bash
curl --get -H "Access-Token: YOUR_ACCESS_TOKEN" --data-urlencode "bc_id=7000000000000000000" --data-urlencode 'fields=["cash_balance","grant_balance","valid_account_balance","budget"]' --data-urlencode "page=1" --data-urlencode "page_size=10" https://business-api.tiktok.com/open_api/v1.3/advertiser/balance/get/
```

#### Python
```python
import json
import os
import requests

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", "YOUR_ACCESS_TOKEN")
BC_ID = os.environ.get("BC_ID", "7000000000000000000")

url = "https://business-api.tiktok.com/open_api/v1.3/advertiser/balance/get/"
headers = {
    "Access-Token": ACCESS_TOKEN,
}
params = {
    "bc_id": BC_ID,
    "fields": json.dumps(["cash_balance", "grant_balance", "valid_account_balance", "budget"]),
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
| ↳ advertiser_account_list | object[] | Danh sách thông tin tài khoản quảng cáo và số dư. |
| ↳↳ advertiser_id | string | ID tài khoản quảng cáo. |
| ↳↳ advertiser_name | string | Tên tài khoản quảng cáo. |
| ↳↳ advertiser_status | string | Trạng thái hiển thị tài khoản. |
| ↳↳ advertiser_type | string | Loại tài khoản: `AUCTION`, `RESERVATION`. |
| ↳↳ timezone | string | Múi giờ tài khoản quảng cáo. |
| ↳↳ currency | string | Đơn vị tiền tệ của tài khoản quảng cáo. |
| ↳↳ account_open_days | number | Số ngày kể từ khi mở tài khoản. |
| ↳↳ balance_reminder | boolean | Cảnh báo số dư chạm ngưỡng giới hạn. |
| ↳↳ transfer_balance | number | Số dư có thể chuyển nhượng. |
| ↳↳ valid_account_balance | number | Tổng số dư hợp lệ hiện tại của tài khoản. |
| ↳↳ frozen_balance | number | Số dư đang bị đóng băng. |
| ↳↳ cash_balance | number | Số dư tiền mặt. |
| ↳↳ grant_balance | number | Số dư phiếu giảm giá (voucher / grant). |
| ↳↳ credit_balance | number | Số dư tín dụng. |
| ↳↳ budget_mode | string | Chế độ ngân sách tài khoản: `INFINITE` (không giới hạn), `TOTAL` (ngân sách tổng). |
| ↳↳ budget | number | Mức ngân sách tài khoản thiết lập. |
| ↳↳ payment_portfolio_id | string | ID danh mục thanh toán liên kết. |
| ↳↳ payment_portfolio_name | string | Tên danh mục thanh toán liên kết. |
| ↳ page_info | object | Thông tin phân trang. |
| ↳↳ page | number | Số trang hiện tại. |
| ↳↳ page_size | number | Kích thước trang. |
| ↳↳ total_number | number | Tổng số tài khoản. |
| ↳↳ total_page | number | Tổng số trang. |

---

## Lấy số dư của Business Center (`Get the balance of a BC`)
<a id="doc-1739939128198145"></a>
<!-- doc_id: 1739939128198145 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/bc/balance/get/`

**Mục đích**: Sử dụng endpoint này để lấy số dư chi tiết của chính Business Center, bao gồm số dư tiền mặt hợp lệ, số dư voucher khả dụng, hạn mức tín dụng và số dư chuyển nhượng.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền (access token). Xem chi tiết tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (GET query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| bc_id | string | Bắt buộc | ID của Business Center cần tra cứu số dư. |

### Ví dụ

#### cURL
```bash
curl --get -H "Access-Token: YOUR_ACCESS_TOKEN" --data-urlencode "bc_id=7000000000000000000" https://business-api.tiktok.com/open_api/v1.3/bc/balance/get/
```

#### Python
```python
import os
import requests

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", "YOUR_ACCESS_TOKEN")
BC_ID = os.environ.get("BC_ID", "7000000000000000000")

url = "https://business-api.tiktok.com/open_api/v1.3/bc/balance/get/"
headers = {
    "Access-Token": ACCESS_TOKEN,
}
params = {
    "bc_id": BC_ID,
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
| ↳ bc_id | string | ID Business Center. |
| ↳ bc_name | string | Tên Business Center. |
| ↳ currency | string | Đơn vị tiền tệ của Business Center. |
| ↳ balance_info | object | Thông tin chi tiết các loại số dư. |
| ↳↳ valid_cash_balance | number | Số dư tiền mặt hợp lệ có thể sử dụng. |
| ↳↳ valid_grant_balance | number | Số dư voucher hợp lệ có thể sử dụng. |
| ↳↳ valid_credit_balance | number | Số dư tín dụng hợp lệ có thể sử dụng. |
| ↳↳ transfer_balance | number | Tổng số dư khả dụng có thể chuyển sang tài khoản quảng cáo. |
| ↳↳ grant_balance | number | Tổng số dư voucher của Business Center. |
| ↳↳ credit_balance | number | Tổng số dư tín dụng khả dụng. |
| ↳↳ credit_limit | number | Tổng hạn mức tín dụng được cấp cho Business Center. |
| ↳↳ total_grant_balance | number | Tổng số tiền voucher đã nhận. |
| ↳↳ frozen_balance | number | Số dư đang bị đóng băng. |

---

## Lấy lịch sử giao dịch của BC hoặc tài khoản quảng cáo (`Get the transaction records of a BC or ad accounts`)
<a id="doc-1792849810925569"></a>
<!-- doc_id: 1792849810925569 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/bc/account/transaction/get/`

**Mục đích**: Sử dụng endpoint này để truy vấn toàn bộ lịch sử các giao dịch nạp, rút, điều chỉnh số dư của Business Center hoặc các tài khoản quảng cáo trực thuộc trong khoảng thời gian chỉ định.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền (access token). Xem chi tiết tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (GET query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| bc_id | string | Bắt buộc | ID của Business Center. |
| transaction_level | string | Bắt buộc | Cấp độ giao dịch cần truy vấn: `ADVERTISER` (tài khoản quảng cáo) hoặc `BC` (Business Center). |
| filtering | object | Không bắt buộc | Điều kiện lọc giao dịch (chuỗi JSON đối tượng). |
| ↳ start_date | string | Không bắt buộc | Ngày bắt đầu khoảng thời gian giao dịch (`YYYY-MM-DD`). |
| ↳ end_date | string | Không bắt buộc | Ngày kết thúc khoảng thời gian giao dịch (`YYYY-MM-DD`). |
| ↳ transaction_type | string[] | Không bắt buộc | Loại giao dịch: `RECHARGE`, `DEDUCT`, `REFUND`, `TRANSFER`. |
| ↳ advertiser_ids | string[] | Không bắt buộc | Danh sách ID tài khoản quảng cáo cần lọc. |
| ↳ operator_ids | string[] | Không bắt buộc | Danh sách ID người thực hiện giao dịch. |
| page | number | Không bắt buộc | Số trang hiện tại. Mặc định: 1. |
| page_size | number | Không bắt buộc | Số bản ghi mỗi trang. Khoảng giá trị: 1-50. Mặc định: 10. |

### Ví dụ

#### cURL
```bash
curl --get -H "Access-Token: YOUR_ACCESS_TOKEN" --data-urlencode "bc_id=7000000000000000000" --data-urlencode "transaction_level=ADVERTISER" --data-urlencode 'filtering={"start_date":"2026-05-01","end_date":"2026-05-30"}' --data-urlencode "page=1" --data-urlencode "page_size=20" https://business-api.tiktok.com/open_api/v1.3/bc/account/transaction/get/
```

#### Python
```python
import json
import os
import requests

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", "YOUR_ACCESS_TOKEN")
BC_ID = os.environ.get("BC_ID", "7000000000000000000")

url = "https://business-api.tiktok.com/open_api/v1.3/bc/account/transaction/get/"
headers = {
    "Access-Token": ACCESS_TOKEN,
}
params = {
    "bc_id": BC_ID,
    "transaction_level": "ADVERTISER",
    "filtering": json.dumps({"start_date": "2026-05-01", "end_date": "2026-05-30"}),
    "page": 1,
    "page_size": 20,
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
| ↳ transaction_list | object[] | Danh sách các bản ghi giao dịch. |
| ↳↳ transaction_id | string | Mã định danh giao dịch. |
| ↳↳ transaction_type | string | Loại giao dịch: `RECHARGE`, `DEDUCT`, `REFUND`. |
| ↳↳ amount | number | Tổng số tiền giao dịch. |
| ↳↳ cash_amount | number | Số tiền mặt trong giao dịch. |
| ↳↳ grant_amount | number | Số tiền voucher trong giao dịch. |
| ↳↳ credit_amount | number | Số tiền tín dụng trong giao dịch. |
| ↳↳ create_time | string | Thời gian thực hiện giao dịch (UTC+0). |
| ↳↳ operator | string | Tên hoặc ID người dùng thực hiện giao dịch. |
| ↳↳ remitter_account | object | Tài khoản nguồn (chuyển đi). |
| ↳↳↳ account_id | string | ID tài khoản nguồn. |
| ↳↳↳ account_name | string | Tên tài khoản nguồn. |
| ↳↳↳ account_type | string | Loại tài khoản nguồn (`BC` hoặc `ADVERTISER`). |
| ↳↳ payee_account | object | Tài khoản đích (nhận tiền). |
| ↳↳↳ account_id | string | ID tài khoản nhận tiền. |
| ↳↳↳ account_name | string | Tên tài khoản nhận tiền. |
| ↳↳↳ account_type | string | Loại tài khoản nhận tiền (`BC` hoặc `ADVERTISER`). |
| ↳ page_info | object | Thông tin phân trang. |
| ↳↳ page | number | Trang hiện tại. |
| ↳↳ page_size | number | Kích thước trang. |
| ↳↳ total_number | number | Tổng số giao dịch. |
| ↳↳ total_page | number | Tổng số trang. |

---

## Lấy lịch sử giao dịch của tài khoản quảng cáo (`Get the transaction records of ad accounts`)
<a id="doc-1739939116353538"></a>
<!-- doc_id: 1739939116353538 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/advertiser/transaction/get/`

**Mục đích**: Sử dụng endpoint này để lấy lịch sử giao dịch cụ thể của các tài khoản quảng cáo thuộc Business Center.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền (access token). Xem chi tiết tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (GET query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| bc_id | string | Bắt buộc | ID của Business Center. |
| filtering | object | Không bắt buộc | Bộ lọc giao dịch tài khoản quảng cáo. |
| ↳ start_date | string | Không bắt buộc | Ngày bắt đầu truy vấn (`YYYY-MM-DD`). |
| ↳ end_date | string | Không bắt buộc | Ngày kết thúc truy vấn (`YYYY-MM-DD`). |
| ↳ transaction_type | string[] | Không bắt buộc | Loại giao dịch: `TRANSFER_IN`, `TRANSFER_OUT`. |
| ↳ keyword | string | Không bắt buộc | Từ khóa tìm kiếm theo tên hoặc ID tài khoản quảng cáo. |
| page | number | Không bắt buộc | Số trang hiện tại. Mặc định: 1. |
| page_size | number | Không bắt buộc | Số bản ghi mỗi trang. Mặc định: 10. |

### Ví dụ

#### cURL
```bash
curl --get -H "Access-Token: YOUR_ACCESS_TOKEN" --data-urlencode "bc_id=7000000000000000000" --data-urlencode 'filtering={"start_date":"2026-05-01","end_date":"2026-05-30"}' --data-urlencode "page=1" --data-urlencode "page_size=10" https://business-api.tiktok.com/open_api/v1.3/advertiser/transaction/get/
```

#### Python
```python
import json
import os
import requests

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", "YOUR_ACCESS_TOKEN")
BC_ID = os.environ.get("BC_ID", "7000000000000000000")

url = "https://business-api.tiktok.com/open_api/v1.3/advertiser/transaction/get/"
headers = {
    "Access-Token": ACCESS_TOKEN,
}
params = {
    "bc_id": BC_ID,
    "filtering": json.dumps({"start_date": "2026-05-01", "end_date": "2026-05-30"}),
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
| ↳ list | object[] | Danh sách giao dịch tài khoản quảng cáo. |
| ↳↳ advertiser_id | string | ID tài khoản quảng cáo. |
| ↳↳ advertiser_name | string | Tên tài khoản quảng cáo. |
| ↳↳ transaction_id | string | ID giao dịch. |
| ↳↳ amount | number | Số tiền giao dịch. |
| ↳↳ transaction_type | string | Loại giao dịch. |
| ↳↳ create_time | string | Thời gian thực hiện giao dịch. |
| ↳ page_info | object | Thông tin phân trang. |
| ↳↳ page | number | Số trang hiện tại. |
| ↳↳ page_size | number | Kích thước trang. |
| ↳↳ total_number | number | Tổng số bản ghi. |
| ↳↳ total_page | number | Tổng số trang. |

---

## Lấy lịch sử giao dịch của Business Center (`Get the transaction records of a BC`)
<a id="doc-1739939140408322"></a>
<!-- doc_id: 1739939140408322 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/bc/transaction/get/`

**Mục đích**: Sử dụng endpoint này để lấy lịch sử các giao dịch tài chính ở cấp độ chính Business Center (ví dụ: cấp hạn mức, hoàn tiền, điều chỉnh tiền mặt).

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền (access token). Xem chi tiết tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (GET query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| bc_id | string | Bắt buộc | ID của Business Center. |
| start_date | string | Bắt buộc | Ngày bắt đầu khoảng thời gian cần lấy lịch sử giao dịch (`YYYY-MM-DD`). |
| end_date | string | Bắt buộc | Ngày kết thúc khoảng thời gian cần lấy lịch sử giao dịch (`YYYY-MM-DD`). |
| page | number | Không bắt buộc | Số trang hiện tại. Giá trị: ≥ 1. Mặc định: 1. |
| page_size | number | Không bắt buộc | Số bản ghi mỗi trang. Khoảng giá trị: 1-50. Mặc định: 10. |

### Ví dụ

#### cURL
```bash
curl --get -H "Access-Token: YOUR_ACCESS_TOKEN" --data-urlencode "bc_id=7000000000000000000" --data-urlencode "start_date=2026-05-01" --data-urlencode "end_date=2026-05-30" --data-urlencode "page=1" --data-urlencode "page_size=10" https://business-api.tiktok.com/open_api/v1.3/bc/transaction/get/
```

#### Python
```python
import os
import requests

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", "YOUR_ACCESS_TOKEN")
BC_ID = os.environ.get("BC_ID", "7000000000000000000")

url = "https://business-api.tiktok.com/open_api/v1.3/bc/transaction/get/"
headers = {
    "Access-Token": ACCESS_TOKEN,
}
params = {
    "bc_id": BC_ID,
    "start_date": "2026-05-01",
    "end_date": "2026-05-30",
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
| ↳ transaction_list | object[] | Danh sách các giao dịch của Business Center. |
| ↳↳ transaction_id | string | ID giao dịch. |
| ↳↳ transaction_type | string | Loại giao dịch: `RECHARGE`, `DEDUCT`, `REFUND`. |
| ↳↳ amount | number | Số tiền giao dịch. |
| ↳↳ cash_amount | number | Số tiền mặt. |
| ↳↳ grant_amount | number | Số tiền voucher. |
| ↳↳ create_time | string | Thời gian giao dịch. |
| ↳ page_info | object | Thông tin phân trang. |
| ↳↳ page | number | Số trang hiện tại. |
| ↳↳ page_size | number | Kích thước trang. |
| ↳↳ total_number | number | Tổng số giao dịch. |
| ↳↳ total_page | number | Tổng số trang. |

---

## Lấy lịch sử thay đổi ngân sách của tài khoản quảng cáo (`Get the budget change history of an ad account`)
<a id="doc-1830173979548674"></a>
<!-- doc_id: 1830173979548674 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/bc/account/budget/changelog/get/`

**Mục đích**: Sử dụng endpoint này để theo dõi toàn bộ lịch sử các lần điều chỉnh ngân sách của một tài khoản quảng cáo cụ thể, bao gồm số tiền trước và sau khi thay đổi, chế độ ngân sách và người thực hiện thao tác.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền (access token). Xem chi tiết tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (GET query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| bc_id | string | Bắt buộc | ID của Business Center. |
| advertiser_id | string | Bắt buộc | ID của tài khoản quảng cáo cần kiểm tra lịch sử ngân sách. |
| filtering | object | Không bắt buộc | Bộ lọc thời gian thay đổi ngân sách. |
| ↳ start_date | string | Không bắt buộc | Ngày bắt đầu truy vấn (`YYYY-MM-DD`). |
| ↳ end_date | string | Không bắt buộc | Ngày kết thúc truy vấn (`YYYY-MM-DD`). |
| page | integer | Không bắt buộc | Số trang hiện tại. Khoảng giá trị: ≥ 1. Mặc định: 1. |
| page_size | integer | Không bắt buộc | Số bản ghi mỗi trang. Khoảng giá trị: 1-50. Mặc định: 10. |

### Ví dụ

#### cURL
```bash
curl --get -H "Access-Token: YOUR_ACCESS_TOKEN" --data-urlencode "bc_id=7000000000000000000" --data-urlencode "advertiser_id=7123456789012345678" --data-urlencode 'filtering={"start_date":"2026-05-01","end_date":"2026-05-30"}' --data-urlencode "page=1" --data-urlencode "page_size=10" https://business-api.tiktok.com/open_api/v1.3/bc/account/budget/changelog/get/
```

#### Python
```python
import json
import os
import requests

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", "YOUR_ACCESS_TOKEN")
BC_ID = os.environ.get("BC_ID", "7000000000000000000")
ADVERTISER_ID = os.environ.get("ADVERTISER_ID", "7123456789012345678")

url = "https://business-api.tiktok.com/open_api/v1.3/bc/account/budget/changelog/get/"
headers = {
    "Access-Token": ACCESS_TOKEN,
}
params = {
    "bc_id": BC_ID,
    "advertiser_id": ADVERTISER_ID,
    "filtering": json.dumps({"start_date": "2026-05-01", "end_date": "2026-05-30"}),
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
| ↳ changelog_list | object[] | Danh sách lịch sử thay đổi ngân sách. |
| ↳↳ operation_time | string | Thời gian thực hiện thay đổi ngân sách (`YYYY-MM-DD HH:MM:SS`). |
| ↳↳ activity_type | string | Loại thay đổi: `RESET` (đặt lại ngân sách dùng 1 lần), `INCREASE` (tăng ngân sách), `DECREASE` (giảm ngân sách). |
| ↳↳ previous_budget | float | Mức ngân sách của tài khoản trước khi thay đổi. |
| ↳↳ previous_budget_mode | string | Chế độ ngân sách trước khi thay đổi: `INFINITE`, `TOTAL`. |
| ↳↳ current_budget | float | Mức ngân sách hiện tại sau khi thay đổi. |
| ↳↳ current_budget_mode | string | Chế độ ngân sách hiện tại: `INFINITE`, `TOTAL`. |
| ↳↳ currency | string | Đơn vị tiền tệ của ngân sách. |
| ↳↳ operator_id | string | ID người dùng thực hiện thay đổi. |
| ↳↳ operator_name | string | Tên người dùng thực hiện thay đổi. |
| ↳ page_info | object | Thông tin phân trang. |
| ↳↳ page | integer | Số trang hiện tại. |
| ↳↳ page_size | integer | Kích thước trang. |
| ↳↳ total_number | integer | Tổng số bản ghi. |
| ↳↳ total_page | integer | Tổng số trang. |

---

## Lấy bản ghi chi phí của BC và tài khoản quảng cáo (`Get the cost records of a BC and ad accounts`)
<a id="doc-1829079287639041"></a>
<!-- doc_id: 1829079287639041 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/bc/account/cost/get/`

**Mục đích**: Sử dụng endpoint này để lấy dữ liệu chi phí quảng cáo (tiền mặt, voucher credit, thuế ước tính) phát sinh của từng nhà quảng cáo và tổng chi phí của cả Business Center trong một khoảng thời gian.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền (access token). Xem chi tiết tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (GET query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| bc_id | string | Bắt buộc | ID của Business Center. |
| filtering | object | Không bắt buộc | Bộ lọc chi phí (chuỗi JSON đối tượng). |
| ↳ keyword | string | Không bắt buộc | Từ khóa tìm kiếm theo tên hoặc ID nhà quảng cáo (hỗ trợ khớp mờ). |
| ↳ start_date | string | Không bắt buộc | Ngày bắt đầu thống kê chi phí (`YYYY-MM-DD`). |
| ↳ end_date | string | Không bắt buộc | Ngày kết thúc thống kê chi phí (`YYYY-MM-DD`). |
| page | integer | Không bắt buộc | Số trang hiện tại. Khoảng giá trị: ≥ 1. Mặc định: 1. |
| page_size | integer | Không bắt buộc | Số bản ghi mỗi trang. Khoảng giá trị: 1-50. Mặc định: 10. |

### Ví dụ

#### cURL
```bash
curl --get -H "Access-Token: YOUR_ACCESS_TOKEN" --data-urlencode "bc_id=7000000000000000000" --data-urlencode 'filtering={"start_date":"2026-05-01","end_date":"2026-05-30"}' --data-urlencode "page=1" --data-urlencode "page_size=10" https://business-api.tiktok.com/open_api/v1.3/bc/account/cost/get/
```

#### Python
```python
import json
import os
import requests

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", "YOUR_ACCESS_TOKEN")
BC_ID = os.environ.get("BC_ID", "7000000000000000000")

url = "https://business-api.tiktok.com/open_api/v1.3/bc/account/cost/get/"
headers = {
    "Access-Token": ACCESS_TOKEN,
}
params = {
    "bc_id": BC_ID,
    "filtering": json.dumps({"start_date": "2026-05-01", "end_date": "2026-05-30"}),
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
| data | object | Dữ liệu chi phí trả về. |
| ↳ cost_list | object[] | Danh sách bản ghi chi phí cho từng tài khoản quảng cáo. |
| ↳↳ advertiser_id | string | ID nhà quảng cáo. |
| ↳↳ advertiser_name | string | Tên nhà quảng cáo. |
| ↳↳ amount | number | Tổng chi phí tiêu thụ của nhà quảng cáo. |
| ↳↳ cash_amount | number | Chi phí tiêu thụ từ tiền mặt. |
| ↳↳ grant_amount | number | Chi phí tiêu thụ từ voucher ưu đãi. |
| ↳↳ tax_amount | number | Thuế ước tính của nhà quảng cáo. |
| ↳↳ currency | string | Đơn vị tiền tệ của nhà quảng cáo. |
| ↳ transaction_summary | object | Bản tóm tắt tổng hợp chi phí của toàn bộ Business Center. |
| ↳↳ amount | number | Tổng chi phí tiêu thụ của toàn bộ Business Center. |
| ↳↳ cash_amount | number | Tổng chi phí tiền mặt của Business Center. |
| ↳↳ grant_amount | number | Tổng chi phí voucher của Business Center. |
| ↳↳ tax_amount | number | Tổng số tiền thuế ước tính của Business Center. |
| ↳↳ currency | string | Đơn vị tiền tệ của Business Center. |
| ↳ page_info | object | Thông tin phân trang. |
| ↳↳ page | integer | Số trang hiện tại. |
| ↳↳ page_size | integer | Kích thước trang. |
| ↳↳ total_number | integer | Tổng số bản ghi. |
| ↳↳ total_page | integer | Tổng số trang. |

### Ví dụ phản hồi

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202605210639490102360430824C1AE673",
  "data": {
    "cost_list": [
      {
        "advertiser_id": "7123456789012345678",
        "advertiser_name": "Tài khoản Quảng cáo 1",
        "amount": -1376616.0,
        "cash_amount": -1376616.0,
        "currency": "VND",
        "grant_amount": 0.0,
        "tax_amount": -68831.0
      }
    ],
    "transaction_summary": {
      "amount": -1376616.0,
      "cash_amount": -1376616.0,
      "currency": "VND",
      "grant_amount": 0.0,
      "tax_amount": -68831.0
    },
    "page_info": {
      "page": 1,
      "page_size": 10,
      "total_number": 1,
      "total_page": 1
    }
  }
}
```
