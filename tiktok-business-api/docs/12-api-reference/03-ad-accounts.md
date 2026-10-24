# Tài khoản quảng cáo (Ad Accounts)
<a id="doc-1738455259137026"></a>
<!-- doc_id: 1738455259137026 -->

Tài khoản nhà quảng cáo (advertiser account / ad account) là loại tài khoản cơ bản trên nền tảng TikTok For Business. Trước khi có thể tạo và quản lý quảng cáo với TikTok For Business, người dùng phải sở hữu một tài khoản nhà quảng cáo hoặc được các nhà quảng cáo cấp quyền quản trị để quản lý tài khoản và tài sản quảng cáo của họ.

> [!IMPORTANT]
> Endpoint `/oauth2/advertiser/get/` (lấy danh sách tài khoản quảng cáo được ủy quyền) và `/advertiser/info/` (lấy thông tin chi tiết tài khoản quảng cáo) là các API cốt lõi nhất để lấy `advertiser_id` và các thông tin cơ bản (múi giờ, đơn vị tiền tệ, trạng thái xét duyệt, số dư). Hầu hết các API khác trong bộ TikTok Business API đều yêu cầu tham số `advertiser_id` này.

Nhóm API này bao gồm các endpoint sau:
* [Lấy danh sách tài khoản quảng cáo được ủy quyền](03-ad-accounts.md#doc-1738455508553729)
* [Lấy thông tin chi tiết tài khoản quảng cáo](03-ad-accounts.md#doc-1739593083610113)

---

## Lấy danh sách tài khoản quảng cáo được ủy quyền (`Get authorized ad accounts`)
<a id="doc-1738455508553729"></a>
<!-- doc_id: 1738455508553729 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/oauth2/advertiser/get/`

**Mục đích**: Sử dụng endpoint này để lấy danh sách các tài khoản nhà quảng cáo (advertiser accounts) đã ủy quyền cho ứng dụng của bạn sau quá trình OAuth2. Đây là bước đầu tiên để lấy danh sách `advertiser_id` mà token có quyền truy cập.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền (access token). Xem chi tiết tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (GET query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| app_id | string | Bắt buộc | App ID của ứng dụng nhà phát triển, có thể lấy tại trang [Application Management](https://ads.tiktok.com/marketing_api/apps/). |
| secret | string | Bắt buộc | Khóa bí mật (secret key) của ứng dụng nhà phát triển, lấy tại trang [Application Management](https://ads.tiktok.com/marketing_api/apps/). |

### Ví dụ

#### cURL
```bash
curl --get -H "Access-Token: YOUR_ACCESS_TOKEN" --data-urlencode "secret=YOUR_APP_SECRET" --data-urlencode "app_id=YOUR_APP_ID" https://business-api.tiktok.com/open_api/v1.3/oauth2/advertiser/get/
```

#### Python
```python
import os
import requests

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", "YOUR_ACCESS_TOKEN")
APP_ID = os.environ.get("APP_ID", "YOUR_APP_ID")
APP_SECRET = os.environ.get("APP_SECRET", "YOUR_APP_SECRET")

url = "https://business-api.tiktok.com/open_api/v1.3/oauth2/advertiser/get/"
headers = {
    "Access-Token": ACCESS_TOKEN,
}
params = {
    "app_id": APP_ID,
    "secret": APP_SECRET,
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi từ hệ thống. Xem [Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | Mã nhật ký yêu cầu (request log ID) để định danh duy nhất cho mỗi lượt gọi API. |
| data | object | Dữ liệu trả về. |
| ↳ list | object[] | Danh sách thông tin các nhà quảng cáo đã ủy quyền. |
| ↳↳ advertiser_id | string | ID tài khoản nhà quảng cáo đã ủy quyền (Advertiser ID). |
| ↳↳ advertiser_name | string | Tên tài khoản nhà quảng cáo đã ủy quyền. |

### Ví dụ phản hồi

```json
{
  "code": 0,
  "message": "OK",
  "data": {
    "list": [
      {
        "advertiser_id": "7123456789012345678",
        "advertiser_name": "Tài khoản Quảng cáo TikTok VN"
      }
    ]
  },
  "request_id": "202603100820230101890492231E063EE3"
}
```

---

## Lấy thông tin chi tiết tài khoản quảng cáo (`Get ad account details`)
<a id="doc-1739593083610113"></a>
<!-- doc_id: 1739593083610113 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/advertiser/info/`

**Mục đích**: Sử dụng endpoint này để lấy thông tin chi tiết của một hoặc nhiều tài khoản nhà quảng cáo, bao gồm tên, múi giờ, đơn vị tiền tệ, trạng thái tài khoản, vai trò, số dư, thông tin liên hệ và giấy phép kinh doanh.

> [!NOTE]
> Để thêm đối tác và phân bổ tài khoản quảng cáo cho đối tác này, bạn có thể dùng endpoint [/bc/partner/add/](18-bc-partners.md#doc-1739662756510721), đặt `asset_type` là `ADVERTISER` và truyền danh sách ID nhà quảng cáo vào trường `asset_ids`. Bạn có thể lấy danh sách ID này từ trường phản hồi `advertiser_id` của `/advertiser/info/`.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền (access token). Xem chi tiết tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (GET query string)

Lưu ý: TikTok API yêu cầu các tham số kiểu mảng/đối tượng phải được truyền dưới dạng chuỗi JSON mã hóa URL.

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| advertiser_ids | string[] | Bắt buộc | Danh sách các ID nhà quảng cáo cần truy vấn thông tin (dưới dạng chuỗi JSON mảng).<br>Bạn có thể lấy danh sách Advertiser ID qua endpoint [/oauth2/advertiser/get/](03-ad-accounts.md#doc-1738455508553729). |
| fields | string[] | Không bắt buộc | Danh sách các trường thông tin cần trả về (dưới dạng chuỗi JSON mảng).<br>Nếu không chỉ định, mặc định hệ thống sẽ trả về tất cả thông tin ngoại trừ `company_name_editable`, `can_use_custom_identity`, và `ads_only_mode`.<br>Các giá trị được hỗ trợ: `telephone_number`, `contacter`, `currency`, `cellphone_number`, `timezone`, `advertiser_id`, `role`, `company`, `status`, `description`, `rejection_reason`, `address`, `name`, `language`, `industry`, `license_no`, `email`, `license_url`, `country`, `balance`, `create_time`, `display_timezone`, `owner_bc_id`, `company_name_editable`, `can_use_custom_identity`, và `ads_only_mode`.<br>> [!NOTE]<br>> Nếu bạn bao gồm `company_name_editable`, `can_use_custom_identity`, hoặc `ads_only_mode` trong tham số này, hệ thống sẽ chỉ trả về các trường đó cùng với `advertiser_id`, còn các trường khác sẽ bị bỏ qua. |

### Ví dụ

#### cURL
```bash
curl -G "https://business-api.tiktok.com/open_api/v1.3/advertiser/info/" -H "Access-Token: YOUR_ACCESS_TOKEN" --data-urlencode 'advertiser_ids=["7123456789012345678"]' --data-urlencode 'fields=["advertiser_id","name","status","currency","timezone","balance","role"]'
```

#### Python
```python
import json
import os
import requests

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", "YOUR_ACCESS_TOKEN")
ADVERTISER_ID = os.environ.get("ADVERTISER_ID", "7123456789012345678")

url = "https://business-api.tiktok.com/open_api/v1.3/advertiser/info/"
headers = {
    "Access-Token": ACCESS_TOKEN,
}
params = {
    "advertiser_ids": json.dumps([ADVERTISER_ID]),
    "fields": json.dumps(["advertiser_id", "name", "status", "currency", "timezone", "balance", "role"]),
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi từ hệ thống. Xem [Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | Mã nhật ký yêu cầu để truy vết lỗi. |
| data | object | Dữ liệu chi tiết trả về. |
| ↳ list | object[] | Danh sách thông tin chi tiết từng tài khoản quảng cáo. |
| ↳↳ advertiser_id | string | ID của tài khoản nhà quảng cáo (Advertiser ID). |
| ↳↳ name | string | Tên tài khoản quảng cáo. |
| ↳↳ status | string | Trạng thái của tài khoản quảng cáo. Xem [Account Status](../15-appendix/phu-luc-p1.md#doc-1737174886619138). Các giá trị gồm: `STATUS_ENABLE`, `STATUS_DISABLE`, `STATUS_PENDING_CONFIRM`, `STATUS_CONFIRM_FAIL`, `STATUS_CONFIRM_FAIL_END`, `STATUS_PENDING_VERIFIED`, `STATUS_CONFIRM_MODIFY`, `STATUS_LIMIT`. |
| ↳↳ role | string | Vai trò của tài khoản quảng cáo: `ROLE_ADVERTISER` (tài khoản độc lập), `ROLE_CHILD_ADVERTISER` (tài khoản con thuộc Business Center), `ROLE_CHILD_AGENT` (tài khoản đại lý con). |
| ↳↳ rejection_reason | string | Lý do tài khoản bị từ chối xét duyệt (nếu có). |
| ↳↳ description | string | Mô tả về tài khoản quảng cáo hoặc thương hiệu. |
| ↳↳ owner_bc_id | string | ID của Business Center sở hữu tài khoản quảng cáo này. |
| ↳↳ timezone | string | Múi giờ của tài khoản quảng cáo theo định dạng "Khu vực/Thành phố" (ví dụ: `Asia/Ho_Chi_Minh`, `Europe/London`). |
| ↳↳ display_timezone | string | Tên múi giờ hiển thị của tài khoản. |
| ↳↳ company | string | Tên công ty/doanh nghiệp đăng ký tài khoản quảng cáo. |
| ↳↳ company_name_editable | boolean | Cho biết tên công ty có thể chỉnh sửa qua API hay không. Nếu `true`, có thể dùng trường `company` trong [/advertiser/update/](15-bc-assets.md#doc-1739939050770434) để sửa. |
| ↳↳ can_use_custom_identity | boolean | Cho biết tài khoản có thể sử dụng Danh tính tùy chỉnh (Custom Identity) để tạo quảng cáo hay không. Xem [About changes coming to Custom Identity](https://ads.tiktok.com/help/article/about-changes-coming-to-custom-identity). |
| ↳↳ ads_only_mode | boolean | Cho biết tài khoản có bắt buộc áp dụng chế độ "Chỉ hiển thị qua quảng cáo" (Show through ads only) cho Spark Ads hay không. Khi giá trị là `true`, bạn chỉ có thể đặt `dark_post_status` thành `ON`. |
| ↳↳ industry | string | Mã danh mục ngành nghề của tài khoản quảng cáo. Xem mã danh mục tại **Industries** (ví dụ: `290303`). |
| ↳↳ address | string | Địa chỉ đăng ký của tài khoản quảng cáo. |
| ↳↳ country | string | Mã quốc gia đăng ký tài khoản (ví dụ: `VN`, `US`). |
| ↳↳ advertiser_account_type | string | Loại tài khoản quảng cáo: `AUCTION` (tài khoản đấu thầu) hoặc `RESERVATION` (tài khoản đặt trước chỗ). |
| ↳↳ currency | string | Đơn vị tiền tệ của tài khoản quảng cáo theo chuẩn ISO 4217 (ví dụ: `VND`, `USD`, `EUR`). |
| ↳↳ contacter | string | Tên người liên hệ phụ trách tài khoản (được làm mờ/mask để bảo mật). |
| ↳↳ email | string | Địa chỉ email liên hệ của tài khoản (được làm mờ). |
| ↳↳ cellphone_number | string | Số điện thoại di động người liên hệ (được làm mờ). |
| ↳↳ telephone_number | string | Số điện thoại cố định (được làm mờ). |
| ↳↳ language | string | Mã ngôn ngữ sử dụng của tài khoản quảng cáo (ví dụ: `vi`, `en`, `zh`). |
| ↳↳ license_no | string | Số giấy phép kinh doanh của doanh nghiệp. |
| ↳↳ license_url | string | URL xem trước bản chụp giấy phép kinh doanh. Liên kết có hiệu lực trong 1 giờ. |
| ↳↳ license_province | string | Tỉnh/thành phố cấp giấy phép kinh doanh (sắp ngừng hỗ trợ). |
| ↳↳ license_city | string | Quận/huyện nơi cấp giấy phép kinh doanh (sắp ngừng hỗ trợ). |
| ↳↳ promotion_area | string | Khu vực địa lý tập trung quảng cáo (sắp ngừng hỗ trợ). |
| ↳↳ promotion_center_province | string | Tỉnh/thành phố trung tâm hoạt động quảng bá (sắp ngừng hỗ trợ). |
| ↳↳ promotion_center_city | string | Thành phố trung tâm hoạt động quảng bá (sắp ngừng hỗ trợ). |
| ↳↳ brand | string | Tên thương hiệu của tài khoản quảng cáo (sắp ngừng hỗ trợ). |
| ↳↳ balance | float | Tổng số dư hiện tại của tài khoản quảng cáo (tính theo đơn vị `currency`).<br>Lưu ý: Trường này không phân tách chi tiết số dư. Để lấy số dư chi tiết (tiền mặt, phiếu giảm giá voucher, khả dụng, đóng băng), hãy sử dụng [/advertiser/balance/get/](13-bc-payments.md#doc-1739939106470913). |
| ↳↳ create_time | datetime | Thời gian tạo tài khoản quảng cáo, tính theo mốc thời gian Unix Epoch (giây). |

### Ví dụ phản hồi

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "2026060710032301011023224213552",
  "data": {
    "list": [
      {
        "advertiser_id": "7123456789012345678",
        "name": "Công ty TNHH Thời Trang Mùa Hè",
        "company": "Công ty TNHH Thời Trang Mùa Hè",
        "status": "STATUS_ENABLE",
        "role": "ROLE_ADVERTISER",
        "advertiser_account_type": "AUCTION",
        "currency": "VND",
        "timezone": "Asia/Ho_Chi_Minh",
        "display_timezone": "Asia/Ho_Chi_Minh",
        "country": "VN",
        "language": "vi",
        "industry": "290303",
        "balance": 15000000.0,
        "create_time": 1716500000,
        "owner_bc_id": "7000000000000000000",
        "contacter": "Ng********an",
        "email": "c*****@******.com",
        "cellphone_number": "+849*******",
        "telephone_number": null,
        "address": "Tầng 5, Tòa nhà Landmark, TP. Hồ Chí Minh",
        "license_no": "0123456789",
        "license_url": "https://sf16-ttm-va.ibytedtos.com/obj/business-license-preview",
        "rejection_reason": "",
        "description": "Thương hiệu thời trang giới trẻ"
      }
    ]
  }
}
```
