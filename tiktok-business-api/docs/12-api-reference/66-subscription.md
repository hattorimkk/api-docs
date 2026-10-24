# Đăng ký Webhook (Subscription)

Tài liệu này cung cấp hướng dẫn và đặc tả kỹ thuật chi tiết cho nhóm API Đăng ký Webhook (Subscription API) của TikTok for Business.

Subscription API cho phép ứng dụng nhà phát triển đăng ký nhận thông báo sự kiện theo thời gian thực (Webhook) từ TikTok khi có các thay đổi về trạng thái tài khoản quảng cáo, khách hàng tiềm năng mới (leads), trạng thái duyệt quảng cáo, tình trạng bão hòa nội dung sáng tạo (creative fatigue), hoặc dữ liệu báo cáo biến động.

Xem thêm [các loại đăng ký webhook](../08-use-cases/use-case-webhook.md#doc-1810521739537409) và [hướng dẫn đăng ký nhận lead](../08-use-cases/use-case-lead-generation.md#doc-1739289524101122).

## Danh sách endpoint trong tài liệu

| Phương thức | Endpoint | Mô tả |
|---|---|---|
| `POST` | `/open_api/v1.3/subscription/create/` | Tạo mới một đăng ký nhận thông báo webhook |
| `GET` | `/open_api/v1.3/subscription/get/` | Lấy chi tiết danh sách các đăng ký webhook của ứng dụng |
| `POST` | `/open_api/v1.3/subscription/unsubscribe/` | Hủy một đăng ký webhook |

---

## Tổng quan về Đăng ký Webhook (Subscription Overview)
<a id="doc-1739091185604609"></a>
<!-- doc_id: 1739091185604609 -->

Subscription API giúp bạn lắng nghe các sự kiện quan trọng trong hệ thống TikTok for Business:
- **Khách hàng tiềm năng (`LEAD`)**: Nhận dữ liệu tức thì khi người dùng điền biểu mẫu tức thì (Instant Form) trên quảng cáo tìm kiếm khách hàng tiềm năng.
- **Trạng thái tài khoản quảng cáo (`AD_ACCOUNT_SUSPENSION`)**: Nhận cảnh báo khi tài khoản bị tạm ngưng hoặc mở lại.
- **Trạng thái duyệt quảng cáo (`AD`, `AD_GROUP`)**: Cập nhật trạng thái phê duyệt hoặc từ chối của mẫu quảng cáo và nhóm quảng cáo.
- **Biến động dữ liệu báo cáo (`REPORT_DATA_CHANGE`)**: Theo dõi các thay đổi về số liệu chi tiêu (`spend`), lượt hiển thị (`impressions`), lượt nhấp (`clicks`), và lượt phát video.
- **Bão hòa nội dung sáng tạo (`CREATIVE_FATIGUE`)**: Nhận cảnh báo khi tần suất xem quảng cáo quá cao và hiệu suất bắt đầu suy giảm.
- **Sự cố dịch vụ API (`API_SERVICE_STATUS`)**: Theo dõi tình trạng hoạt động và gián đoạn của các sản phẩm API TikTok.

Các tài liệu liên kết trong nhóm:
* [Tạo đăng ký Webhook](66-subscription.md#doc-1739092028876801)
* [Lấy chi tiết đăng ký của ứng dụng nhà phát triển](66-subscription.md#doc-1739093832125442)
* [Hủy đăng ký Webhook](66-subscription.md#doc-1739094758789122)

---

## Tạo đăng ký Webhook (Create a subscription)
<a id="doc-1739092028876801"></a>
<!-- doc_id: 1739092028876801 -->

Sử dụng endpoint này để đăng ký nhận thông báo Webhook cho các sự kiện mong muốn. Khi sự kiện phát sinh, TikTok sẽ gửi một yêu cầu HTTP POST chứa payload JSON đến địa chỉ `callback_url` bạn đã chỉ định.

> **Lưu ý:**
> - Đăng ký thông báo biến động số liệu báo cáo (`REPORT_DATA_CHANGE`) và trạng thái tạm ngưng tài khoản (`AD_ACCOUNT_SUSPENSION`) yêu cầu tài khoản được đưa vào danh sách cho phép (allowlist).
> - Đối với sự kiện `LEAD`, việc đăng ký được quản lý theo mã định danh `subscription_id`, không phụ thuộc vào `page_id`. Một trang Instant Form có thể nằm trong nhiều đăng ký khác nhau.

### Yêu cầu (Request)

**Endpoint:** `https://business-api.tiktok.com/open_api/v1.3/subscription/create/`  
**Phương thức (Method):** `POST`

#### Header

| Field | Type | Description |
|---|---|---|
| `Content-Type` **(Bắt buộc)** | string | Định dạng nội dung yêu cầu. Giá trị: `"application/json"`. |

#### Tham số (Parameters)

| Field | Type | Description |
|---|---|---|
| `app_id` **(Bắt buộc)** | string | ID ứng dụng nhà phát triển của bạn (lấy tại **My Apps** > **App Detail** > **Basic Information**). |
| `secret` **(Bắt buộc)** | string | Khóa bí mật (Secret) của ứng dụng nhà phát triển. |
| `subscribe_entity` **(Bắt buộc)** | string | Đối tượng bạn muốn đăng ký nhận thông báo.<br>Enum: `REPORT_DATA_CHANGE`, `AD_ACCOUNT_SUSPENSION`, `LEAD`, `AD_GROUP`, `AD`, `TCM_VIDEOS`, `CREATIVE_FATIGUE`, `API_SERVICE_STATUS`. |
| `callback_url` **(Bắt buộc)** | string | Địa chỉ URL webhook nhận thông báo (yêu cầu hỗ trợ HTTPS và có phản hồi mã HTTP 200 trong vòng 3 giây). |
| `subscription_detail` **(Bắt buộc)** | object | Chi tiết thông tin cấu hình đăng ký. |
| `↳ access_token` **(Bắt buộc)** | string | Mã Access token được cấp quyền từ tài khoản quảng cáo hoặc Business Center. |
| `↳ product_filters` | string[] | Chỉ hợp lệ khi `subscribe_entity` là `API_SERVICE_STATUS`. Danh sách mã sản phẩm API muốn lọc. |
| `↳ lead_source` | string | Chỉ hợp lệ khi `subscribe_entity` là `LEAD`. Nguồn lead: `PAGE` (Trang Instant Form) hoặc `TIKTOK_SHOP`. |
| `↳ bc_id` {+Conditional} | string | ID của Business Center (bắt buộc khi `subscribe_entity` là `AD_ACCOUNT_SUSPENSION`). |
| `↳ advertiser_ids` {+Conditional} | string[] | Danh sách ID tài khoản quảng cáo (bắt buộc đối với `REPORT_DATA_CHANGE`). |
| `↳ notify_frequency` | string | Tần suất gửi thông báo khi `subscribe_entity` là `REPORT_DATA_CHANGE` (`HOURLY`, `DAILY`). |
| `↳ advertiser_id` {+Conditional} | string | ID tài khoản quảng cáo (bắt buộc đối với `AD`, `AD_GROUP`, hoặc `LEAD`). |
| `↳ library_id` {+Conditional} | string | ID thư viện biểu mẫu (Lead Library ID). |
| `↳ page_id` | string | ID của trang Instant Form khi `subscribe_entity` là `LEAD` và `lead_source` là `PAGE`. |
| `↳ adgroup_id` {+Conditional} | string | ID nhóm quảng cáo cụ thể cần theo dõi duyệt hoặc fatigue. |
| `↳ ad_id` {+Conditional} | string | ID mẫu quảng cáo cụ thể cần theo dõi duyệt hoặc fatigue. |
| `↳ tto_tcm_account_id` {+Conditional} | string | ID tài khoản TTO Creator Marketplace (bắt buộc khi `subscribe_entity` là `TCM_VIDEOS`). |

#### Ví dụ gọi API

##### cURL (Đăng ký nhận Lead mới)

```bash
curl -X POST 'https://business-api.tiktok.com/open_api/v1.3/subscription/create/' \
  -H 'Content-Type: application/json' \
  -d '{
    "app_id": "7123456789012345678",
    "secret": "your_app_secret_here",
    "subscribe_entity": "LEAD",
    "callback_url": "https://api.yourdomain.com/webhooks/tiktok/leads",
    "subscription_detail": {
      "access_token": "YOUR_AUTHORIZED_ACCESS_TOKEN",
      "advertiser_id": "7123456789012345678",
      "lead_source": "PAGE",
      "page_id": "1765432109876543"
    }
  }'
```

##### Python (requests) — Đăng ký và Xác thực chữ ký Webhook

```python
import hmac
import hashlib
import requests

# 1. Tạo đăng ký nhận Webhook
APP_ID = "7123456789012345678"
APP_SECRET = "your_app_secret_here"
url = "https://business-api.tiktok.com/open_api/v1.3/subscription/create/"

headers = {
    "Content-Type": "application/json"
}

payload = {
    "app_id": APP_ID,
    "secret": APP_SECRET,
    "subscribe_entity": "LEAD",
    "callback_url": "https://api.yourdomain.com/webhooks/tiktok/leads",
    "subscription_detail": {
        "access_token": "YOUR_AUTHORIZED_ACCESS_TOKEN",
        "advertiser_id": "7123456789012345678",
        "lead_source": "PAGE",
        "page_id": "1765432109876543"
    }
}

response = requests.post(url, headers=headers, json=payload)
print("Create Subscription Response:", response.json())

# 2. Mẫu hàm xác thực chữ ký (Signature Verification) khi nhận webhook từ TikTok
def verify_tiktok_webhook(payload_body: bytes, signature_header: str, secret: str) -> bool:
    """Xác thực chữ ký HMAC-SHA256 của Webhook gửi từ TikTok."""
    expected_signature = hmac.new(
        secret.encode("utf-8"),
        payload_body,
        hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(expected_signature, signature_header)
```

### Phản hồi (Response)

| Field | Type | Description |
|---|---|---|
| `code` | number | Mã phản hồi. `0` biểu thị thành công. Các mã khác xem tại [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi từ hệ thống. |
| `data` | object | Dữ liệu trả về. |
| `↳ subscription_id` | string | Mã ID duy nhất của đăng ký webhook vừa tạo. |
| `request_id` | string | Chuỗi log ID duy nhất xác định yêu cầu. |

#### Ví dụ phản hồi thành công

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "2024040112000001018905602824580D00",
  "data": {
    "subscription_id": "1765432109876543210"
  }
}
```

---

## Lấy chi tiết đăng ký của ứng dụng nhà phát triển (Get subscription details of a developer app)
<a id="doc-1739093832125442"></a>
<!-- doc_id: 1739093832125442 -->

Sử dụng endpoint này để tra cứu danh sách và thông tin chi tiết các webhook đang hoạt động của ứng dụng nhà phát triển.

### Yêu cầu (Request)

**Endpoint:** `https://business-api.tiktok.com/open_api/v1.3/subscription/get/`  
**Phương thức (Method):** `GET`

#### Tham số (Parameters)

| Field | Type | Description |
|---|---|---|
| `app_id` **(Bắt buộc)** | string | ID ứng dụng nhà phát triển của bạn. |
| `secret` **(Bắt buộc)** | string | Khóa bí mật (Secret) của ứng dụng nhà phát triển. |
| `subscribe_entity` | string | Lọc theo loại đối tượng đăng ký (`REPORT_DATA_CHANGE`, `AD_ACCOUNT_SUSPENSION`, `LEAD`, `AD_GROUP`, `AD`, `TCM_VIDEOS`, `CREATIVE_FATIGUE`, `API_SERVICE_STATUS`). |
| `page` | number | Trang hiện tại (mặc định: `1`). |
| `page_size` | number | Kích thước trang (mặc định: `10`, tối đa: `1000`). |

#### Ví dụ gọi API

##### cURL

```bash
curl -X GET 'https://business-api.tiktok.com/open_api/v1.3/subscription/get/?app_id=7123456789012345678&secret=your_app_secret_here&subscribe_entity=LEAD&page=1&page_size=10'
```

##### Python (requests)

```python
import requests

APP_ID = "7123456789012345678"
APP_SECRET = "your_app_secret_here"
url = "https://business-api.tiktok.com/open_api/v1.3/subscription/get/"

params = {
    "app_id": APP_ID,
    "secret": APP_SECRET,
    "subscribe_entity": "LEAD",
    "page": 1,
    "page_size": 10
}

response = requests.get(url, params=params)
print(response.status_code)
print(response.json())
```

### Phản hồi (Response)

| Field | Type | Description |
|---|---|---|
| `code` | number | Mã phản hồi. `0` biểu thị thành công. Các mã khác xem tại [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi từ hệ thống. |
| `data` | object | Dữ liệu trả về. |
| `↳ subscriptions` | object[] | Danh sách các webhook đăng ký. |
| `↳↳ subscription_id` | string | ID của đăng ký webhook. |
| `↳↳ subscribe_entity` | string | Đối tượng đã đăng ký. |
| `↳↳ callback_url` | string | Địa chỉ callback URL nhận webhook. |
| `↳↳ subscription_detail` | object | Chi tiết cấu hình đăng ký (`advertiser_id`, `advertiser_ids`, `bc_id`, `page_id`, `lead_source`, `adgroup_id`, `ad_id`, `tto_tcm_account_id`, `product_filters`, `notify_frequency`). |
| `↳ page_info` | object | Thông tin phân trang. |
| `↳↳ page` | number | Số trang hiện tại. |
| `↳↳ page_size` | number | Kích thước trang. |
| `↳↳ total_number` | number | Tổng số lượng đăng ký webhook. |
| `↳↳ total_page` | number | Tổng số trang kết quả. |
| `request_id` | string | Chuỗi log ID duy nhất xác định yêu cầu. |

#### Ví dụ phản hồi thành công

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "2024040112000001018905602824580D00",
  "data": {
    "subscriptions": [
      {
        "subscription_id": "1765432109876543210",
        "subscribe_entity": "LEAD",
        "callback_url": "https://api.yourdomain.com/webhooks/tiktok/leads",
        "subscription_detail": {
          "advertiser_id": "7123456789012345678",
          "lead_source": "PAGE",
          "page_id": "1765432109876543"
        }
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

---

## Hủy đăng ký Webhook (Cancel a subscription)
<a id="doc-1739094758789122"></a>
<!-- doc_id: 1739094758789122 -->

Sử dụng endpoint này để hủy bỏ một đăng ký webhook đã tạo trước đó. Sau khi hủy, hệ thống TikTok sẽ dừng gửi sự kiện đến địa chỉ `callback_url` tương ứng.

### Yêu cầu (Request)

**Endpoint:** `https://business-api.tiktok.com/open_api/v1.3/subscription/unsubscribe/`  
**Phương thức (Method):** `POST`

#### Header

| Field | Type | Description |
|---|---|---|
| `Content-Type` **(Bắt buộc)** | string | Định dạng nội dung yêu cầu. Giá trị: `application/json`. |

#### Tham số (Parameters)

| Field | Type | Description |
|---|---|---|
| `app_id` **(Bắt buộc)** | string | ID ứng dụng nhà phát triển của bạn. |
| `secret` **(Bắt buộc)** | string | Khóa bí mật (Secret) của ứng dụng nhà phát triển. |
| `subscription_id` **(Bắt buộc)** | string | ID của đăng ký webhook cần hủy. |

#### Ví dụ gọi API

##### cURL

```bash
curl -X POST 'https://business-api.tiktok.com/open_api/v1.3/subscription/unsubscribe/' \
  -H 'Content-Type: application/json' \
  -d '{
    "app_id": "7123456789012345678",
    "secret": "your_app_secret_here",
    "subscription_id": "1765432109876543210"
  }'
```

##### Python (requests)

```python
import requests

APP_ID = "7123456789012345678"
APP_SECRET = "your_app_secret_here"
SUBSCRIPTION_ID = "1765432109876543210"
url = "https://business-api.tiktok.com/open_api/v1.3/subscription/unsubscribe/"

headers = {
    "Content-Type": "application/json"
}

payload = {
    "app_id": APP_ID,
    "secret": APP_SECRET,
    "subscription_id": SUBSCRIPTION_ID
}

response = requests.post(url, headers=headers, json=payload)
print(response.status_code)
print(response.json())
```

### Phản hồi (Response)

| Field | Type | Description |
|---|---|---|
| `code` | number | Mã phản hồi. `0` biểu thị thành công. Các mã khác xem tại [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi từ hệ thống. |
| `data` | object | Dữ liệu trả về (đối tượng rỗng `{}` khi hủy thành công). |
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
