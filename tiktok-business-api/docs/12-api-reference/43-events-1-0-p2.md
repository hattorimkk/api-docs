# Sự kiện 1.0 (Events 1.0) — phần 2/2

> Phân hệ API Reference > Events 1.0 > CRM Events & CTM Events.
> Tài liệu này hướng dẫn quản trị tập sự kiện CRM (Customer Relationship Management) phục vụ đối soát/phân bổ ngoại tuyến và tập sự kiện tin nhắn CTM (Click-to-Message) cho quảng cáo nhắn tin tức thời trên TikTok.

---

## Mục lục điều hướng
- [1. Lấy danh sách CRM Event Sets (`GET /open_api/v1.3/crm/list/`)](#1-lay-danh-sach-crm-event-sets)
- [2. Tạo CRM Event Set (`POST /open_api/v1.3/crm/create/`)](#2-tao-crm-event-set)
- [3. Tổng quan sự kiện CTM (Click-to-Message Events)](#3-tong-quan-su-kien-ctm)
- [4. Lấy tập sự kiện tin nhắn để tạo quảng cáo (`GET /open_api/v1.3/ctm/message_event_set/get/`)](#4-lay-tap-su-kien-tin-nhan-de-tao-quang-cao)
- [5. Mã nguồn mẫu Data Retrieval (Python & cURL)](#5-ma-nguon-mau-data-retrieval)

---

<a id="doc-1780896521680898"></a>
<!-- doc_id: 1780896521680898 -->
<a id="1-lay-danh-sach-crm-event-sets"></a>
## 1. Lấy danh sách CRM Event Sets

Endpoint này cho phép trích xuất danh sách các CRM Event Sets (tập hợp sự kiện Quản lý quan hệ khách hàng) trong tài khoản nhà quảng cáo. Bạn có thể lọc theo ID hoặc tên của Event Set.

> **Quan trọng:** Khi sử dụng các endpoint Events API, bạn đồng ý với [Điều khoản sản phẩm dữ liệu TikTok Business](https://ads.tiktok.com/i18n/official/policy/business-products-terms) và cam kết không chia sẻ dữ liệu nhạy cảm với TikTok.
> **Lưu ý:** Mỗi tài khoản quảng cáo được phép tạo tối đa 50 CRM Event Sets.

### Thông tin Request

- **Endpoint:** `https://business-api.tiktok.com/open_api/v1.3/crm/list/`
- **Method:** `GET`
- **Header:**
  - `Access-Token` (string, **Bắt buộc**): Token ủy quyền truy cập. Chi tiết tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162).

### Tham số Query (Parameters)

| Field | Data Type | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | **Bắt buộc** | ID tài khoản nhà quảng cáo. |
| `name` | string | Không | Tên CRM Event Set cần lọc. Hỗ trợ khớp chính xác (exact match). Độ dài 1-40 ký tự. Nếu không truyền, trả về toàn bộ CRM Event Sets. Nếu không khớp tên nào, kết quả trả về danh sách rỗng. |
| `event_set_ids` | string[] | Không | Danh sách ID CRM Event Set cần lọc (tối đa 50 ID, định dạng JSON chuỗi hoặc danh sách). Chỉ các Event Set có ID khớp mới được trả về. |

*Lưu ý:* Nếu truyền cả `event_set_ids` và `name`, kết quả trả về là Event Set thỏa mãn đồng thời cả tên và nằm trong danh sách ID, hoặc rỗng nếu không có đối tượng nào đáp ứng cả hai điều kiện.

### Cấu trúc phản hồi (Response)

| Field | Type | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi nghiệp vụ. `0` = thành công. Chi tiết tại [Mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi (ví dụ `OK`). Chi tiết tại [Mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `request_id` | string | ID duy nhất định danh request phục vụ tra cứu log. |
| `data` | object | Dữ liệu trả về. |
| ↳ `crm_event_sets` | object[] | Danh sách các CRM Event Sets thỏa mãn điều kiện lọc. |
| ↳↳ `event_set_id` | string | ID định danh của CRM Event Set. |
| ↳↳ `name` | string | Tên của CRM Event Set. |
| ↳↳ `create_time` | string | Thời gian tạo CRM Event Set theo chuẩn [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) (Ví dụ: `"2023-04-15T00:23:38Z"`). |

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202603231200000101",
  "data": {
    "crm_event_sets": [
      {
        "event_set_id": "7286811234567890123",
        "name": "CRM_Leads_Offline_2026",
        "create_time": "2026-01-15T08:30:00Z"
      }
    ]
  }
}
```

---

<a id="doc-1861366342223874"></a>
<!-- doc_id: 1861366342223874 -->
<a id="2-tao-crm-event-set"></a>
## 2. Tạo CRM Event Set

Endpoint tạo mới một tập sự kiện CRM (Customer Relationship Management) trong tài khoản quảng cáo. Mỗi tài khoản quảng cáo hỗ trợ tối đa 50 CRM Event Sets.

### Thông tin Request

- **Endpoint:** `https://business-api.tiktok.com/open_api/v1.3/crm/create/`
- **Method:** `POST`
- **Header:**
  - `Access-Token` (string, **Bắt buộc**): Token ủy quyền truy cập. Chi tiết tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162).
  - `Content-Type` (string, **Bắt buộc**): Định dạng `application/json`.

### Tham số Body (Parameters)

| Field | Data Type | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | **Bắt buộc** | ID tài khoản nhà quảng cáo. |
| `name` | string | **Bắt buộc** | Tên CRM Event Set cần tạo trong tài khoản quảng cáo. Giới hạn 40 ký tự. Khoảng trắng đầu và cuối sẽ được tự động loại bỏ. Không cho phép trùng tên với CRM Event Set đã tồn tại. |

### Cấu trúc phản hồi (Response)

| Field | Type | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi nghiệp vụ (`0` = thành công). Chi tiết tại [Mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi (`OK`). Chi tiết tại [Mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `request_id` | string | ID duy nhất phục vụ truy vết log request. |
| `data` | object | Dữ liệu CRM Event Set vừa tạo thành công. |
| ↳ `event_set_id` | string | ID của CRM Event Set vừa được khởi tạo. |
| ↳ `name` | string | Tên của CRM Event Set. |
| ↳ `create_time` | string | Thời gian tạo theo định dạng ISO-8601 (Ví dụ: `"2026-01-01T00:00:01Z"`). |

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202603231200000102",
  "data": {
    "event_set_id": "7286819999999999999",
    "name": "CRM_Store_Purchases_2026",
    "create_time": "2026-03-23T10:00:00Z"
  }
}
```

---

<a id="doc-1816986081880065"></a>
<!-- doc_id: 1816986081880065 -->
<a id="3-tong-quan-su-kien-ctm"></a>
## 3. Tổng quan sự kiện CTM (Click-to-Message Events)

> Đường dẫn: API Reference > Events 1.0 > CTM Events
> **Quan trọng:** Khi sử dụng các endpoint Events API, bạn đồng ý với [Điều khoản sản phẩm dữ liệu TikTok Business](https://ads.tiktok.com/i18n/official/policy/business-products-terms) và không chia sẻ dữ liệu nhạy cảm với TikTok.

Các sự kiện Click-to-message (CTM) như Hội thoại (Conversations) được sử dụng trong việc đo lường, báo cáo và tối ưu hóa cho chiến dịch [Quảng cáo nhắn tin tức thời TikTok (TikTok Instant Messaging Ads)](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1774482999036930).
Nhóm API sự kiện CTM cho phép bạn trích xuất các tập sự kiện tin nhắn khả dụng để sử dụng khi tạo quảng cáo.

Nhóm này bao gồm endpoint:
* [Lấy tập sự kiện tin nhắn để tạo quảng cáo (`/open_api/v1.3/ctm/message_event_set/get/`)](43-events-1-0-p2.md#doc-1816979158055937)

---

<a id="doc-1816979158055937"></a>
<!-- doc_id: 1816979158055937 -->
<a id="4-lay-tap-su-kien-tin-nhan-de-tao-quang-cao"></a>
## 4. Lấy tập sự kiện tin nhắn để tạo quảng cáo

Endpoint dùng để lấy các tập sự kiện tin nhắn (message event sets) khả dụng để cấu hình khi tạo chiến dịch [TikTok Instant Messaging Ads](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1774482999036930).

### Điều kiện tiên quyết
Đảm bảo bạn đã có message event set trong tài khoản quảng cáo. Nếu chưa có, bạn cần tạo message event set trước [trên TikTok Events Manager](https://ads.tiktok.com/help/article/how-to-create-message-events-on-tiktok-events-manager?lang=en).

### Thông tin Request

- **Endpoint:** `https://business-api.tiktok.com/open_api/v1.3/ctm/message_event_set/get/`
- **Method:** `GET`
- **Header:**
  - `Access-Token` (string, **Bắt buộc**): Token ủy quyền truy cập. Chi tiết tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162).

### Tham số Query (Parameters)

| Field | Data Type | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | **Bắt buộc** | ID tài khoản nhà quảng cáo. |
| `messaging_app_type` | string | **Bắt buộc** | Loại ứng dụng nhắn tin tức thời. Giá trị Enum:<ul><li>`MESSENGER`: Facebook Messenger.</li><li>`WHATSAPP`: WhatsApp.</li><li>`ZALO`: Zalo.</li></ul> |
| `messaging_app_account_id` | string | **Bắt buộc** | ID tài khoản ứng dụng nhắn tin:<ul><li>Nếu `messaging_app_type` là `MESSENGER`: Chỉ định Facebook Page ID (chỉ gồm các chữ số). Để lấy Page ID, vào Trang Facebook > Giới thiệu (About) > Tính minh bạch của Trang (Page transparency).</li><li>Nếu `messaging_app_type` là `WHATSAPP`: Số điện thoại WhatsApp theo chuẩn mã quốc gia + số điện thoại không có dấu hoặc ký tự đặc biệt (ví dụ mã vùng Mỹ +1, số (555) 555-1234 thì nhập `15555551234`).</li><li>Nếu `messaging_app_type` là `ZALO`: Nhập Zalo Official Account ID (OA ID).</li></ul> |
| `message_event_name` | string | Không | Tên message event set để lọc kết quả. Hỗ trợ khớp chính xác (exact match). |
| `message_event_set_ids` | string[] | Không | Danh sách ID message event sets cần lọc (tối đa 10 ID). |

### Cấu trúc phản hồi (Response)

| Field | Type | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi nghiệp vụ (`0` = thành công). Chi tiết tại [Mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi (`OK`). Chi tiết tại [Mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `request_id` | string | ID log duy nhất nhận diện request. |
| `data` | object | Dữ liệu trả về. |
| ↳ `message_event_set_list` | object[] | Danh sách các message event sets hiện có trong tài khoản quảng cáo. |
| ↳↳ `message_event_set_id` | string | ID của message event set. |
| ↳↳ `message_event_name` | string | Tên của message event set. |
| ↳↳ `create_time` | string | Thời gian tạo theo định dạng `YYYY-MM-DD HH:MM:SS` (Ví dụ: `"2024-01-01 00:00:01"`). |
| ↳ `matched_event_set` | object | Thông tin về message event set duy nhất liên kết với tài khoản ứng dụng nhắn tin (`messaging_app_account_id`). |
| ↳↳ `message_event_set_id` | string | ID của message event set được liên kết. |
| ↳↳ `message_event_name` | string | Tên của message event set. |
| ↳↳ `create_time` | string | Thời gian tạo (`YYYY-MM-DD HH:MM:SS`). |

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202603231200000103",
  "data": {
    "message_event_set_list": [
      {
        "message_event_set_id": "7359123456789012345",
        "create_time": "2026-02-18 14:25:28",
        "message_event_name": "Zalo_Chat_Conversions"
      }
    ],
    "matched_event_set": {
      "message_event_set_id": "7359123456789012345",
      "create_time": "2026-02-18 14:25:28",
      "message_event_name": "Zalo_Chat_Conversions"
    }
  }
}
```

---

<a id="5-ma-nguon-mau-data-retrieval"></a>
## 5. Mã nguồn mẫu Data Retrieval (Python & cURL)

### cURL trích xuất CRM Event Sets & CTM Event Sets
```bash
# 1. Lấy danh sách CRM Event Sets
curl -s -X GET "https://business-api.tiktok.com/open_api/v1.3/crm/list/?advertiser_id=YOUR_ADVERTISER_ID" \
  -H "Access-Token: YOUR_ACCESS_TOKEN"

# 2. Lấy CTM Message Event Sets cho Zalo OA
curl -s -X GET "https://business-api.tiktok.com/open_api/v1.3/ctm/message_event_set/get/?advertiser_id=YOUR_ADVERTISER_ID&messaging_app_type=ZALO&messaging_app_account_id=YOUR_ZALO_OA_ID" \
  -H "Access-Token: YOUR_ACCESS_TOKEN"
```

### Python script trích xuất dữ liệu tự động
```python
import requests
import json

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ADVERTISER_ID = "YOUR_ADVERTISER_ID"
BASE_URL = "https://business-api.tiktok.com/open_api/v1.3"

headers = {
    "Access-Token": ACCESS_TOKEN
}

def get_crm_event_sets(advertiser_id):
    """Trích xuất danh sách CRM Event Sets."""
    url = f"{BASE_URL}/crm/list/"
    params = {"advertiser_id": advertiser_id}
    res = requests.get(url, headers=headers, params=params).json()
    if res.get("code") == 0:
        event_sets = res.get("data", {}).get("crm_event_sets", [])
        print(f"Tìm thấy {len(event_sets)} CRM Event Sets:")
        for es in event_sets:
            print(f" - [{es.get(event_set_id)}] {es.get(name)} (Tạo lúc: {es.get(create_time)})")
        return event_sets
    else:
        print(f"Lỗi: {res.get(code)} - {res.get(message)}")
        return []

def get_ctm_event_sets(advertiser_id, app_type="ZALO", account_id=""):
    """Lấy danh sách tập sự kiện tin nhắn CTM."""
    url = f"{BASE_URL}/ctm/message_event_set/get/"
    params = {
        "advertiser_id": advertiser_id,
        "messaging_app_type": app_type,
        "messaging_app_account_id": account_id
    }
    res = requests.get(url, headers=headers, params=params).json()
    if res.get("code") == 0:
        matched = res.get("data", {}).get("matched_event_set")
        print(f"Matched Event Set cho {app_type} ({account_id}): {matched}")
        return res.get("data")
    else:
        print(f"Lỗi: {res.get(code)} - {res.get(message)}")
        return None

if __name__ == "__main__":
    get_crm_event_sets(ADVERTISER_ID)
```
