# Sự kiện 1.0 (Events 1.0) — phần 1/2

Tài liệu này cung cấp hướng dẫn và đặc tả kỹ thuật chi tiết cho các API Sự kiện 1.0 (Events API 1.0) của TikTok for Business — Phần 1/2.

Events API cho phép bạn gửi dữ liệu sự kiện từ các kênh web, ứng dụng di động (app), ngoại tuyến (offline) và CRM trực tiếp đến TikTok nhằm tối ưu hóa phân phối quảng cáo, đo lường chuyển đổi và xây dựng tệp đối tượng tùy chỉnh (Custom Audiences).

> **Lưu ý quan trọng về chuyển đổi phiên bản:**
> 6 endpoint thuộc Events API 1.0 sau đây sẽ dừng hoạt động (sunset):
> - `/pixel/track/` và `/pixel/batch/`
> - `/offline/track/` và `/offline/batch/`
> - `/app/track/` và `/app/batch/`
>
> TikTok khuyến nghị chuyển đổi sớm sang **Events API 2.0** (`/event/track/` - [xem tài liệu](42-events-2-0.md#doc-1771101303285761)), nơi cung cấp một cấu trúc schema thống nhất cho mọi nguồn dữ liệu (web, app, offline, CRM).

> **Điều khoản bảo vệ dữ liệu:**
> Khi sử dụng các endpoint của Events API, bạn đồng ý tuân thủ [TikTok Business Products (Data) Terms](https://ads.tiktok.com/i18n/official/policy/business-products-terms) và cam kết không chia sẻ dữ liệu nhạy cảm với TikTok.

---

## Danh sách endpoint trong tài liệu

| Phân nhóm | Phương thức | Endpoint | Mô tả |
|---|---|---|---|
| **App Events** | `POST` | `/open_api/v1.3/app/track/` | Báo cáo một sự kiện ứng dụng |
| **App Events** | `POST` | `/open_api/v1.3/app/batch/` | Báo cáo sự kiện ứng dụng hàng loạt (tối đa 1.000 sự kiện) |
| **App Events** | `GET` | `/open_api/v1.3/app/info/` | Lấy thông tin chi tiết của một ứng dụng |
| **App Events** | `POST` | `/open_api/v1.3/app/create/` | Tạo mới một ứng dụng di động |
| **App Events** | `POST` | `/open_api/v1.3/app/update/` | Cập nhật thông tin ứng dụng |
| **App Events** | `GET` | `/open_api/v1.3/app/list/` | Lấy danh sách ứng dụng thuộc tài khoản |
| **App Events** | `GET` | `/open_api/v1.3/app/optimization_event/` | Lấy danh sách sự kiện chuyển đổi ứng dụng |
| **App Events** | `GET` | `/open_api/v1.3/app/optimization_event/retargeting/` | Lấy danh sách sự kiện retargeting ứng dụng |
| **Pixel Events** | `POST` | `/open_api/v1.3/pixel/track/` | Báo cáo một sự kiện Web Pixel |
| **Pixel Events** | `POST` | `/open_api/v1.3/pixel/batch/` | Báo cáo sự kiện Web Pixel hàng loạt |
| **Pixel Events** | `GET` | `/open_api/v1.3/pixel/list/` | Lấy danh sách Pixels và cấu hình sự kiện |
| **Pixel Events** | `POST` | `/open_api/v1.3/pixel/create/` | Tạo một Pixel mới |
| **Pixel Events** | `POST` | `/open_api/v1.3/pixel/update/` | Cập nhật thông tin tên Pixel |
| **Pixel Events** | `POST` | `/open_api/v1.3/pixel/event/create/` | Tạo sự kiện Pixel |
| **Pixel Events** | `POST` | `/open_api/v1.3/pixel/event/update/` | Cập nhật tên và giá trị chuyển đổi sự kiện |
| **Pixel Events** | `POST` | `/open_api/v1.3/pixel/event/delete/` | Xóa sự kiện Pixel |
| **Pixel Events** | `GET` | `/open_api/v1.3/pixel/instant_page/event/` | Lấy danh sách sự kiện hỗ trợ cho Instant Page |
| **Pixel Events** | `GET` | `/open_api/v1.3/pixel/event/stats/` | Lấy số liệu thống kê sự kiện Pixel |
| **Offline Events** | `POST` | `/open_api/v1.3/offline/create/` | Tạo mới bộ sự kiện ngoại tuyến (Offline Event set) |
| **Offline Events** | `POST` | `/open_api/v1.3/offline/update/` | Cập nhật bộ sự kiện ngoại tuyến |
| **Offline Events** | `POST` | `/open_api/v1.3/offline/delete/` | Xóa bộ sự kiện ngoại tuyến |
| **Offline Events** | `GET` | `/open_api/v1.3/offline/get/` | Lấy danh sách các bộ sự kiện ngoại tuyến |
| **Offline Events** | `POST` | `/open_api/v1.3/offline/track/` | Báo cáo một sự kiện ngoại tuyến |
| **Offline Events** | `POST` | `/open_api/v1.3/offline/batch/` | Báo cáo sự kiện ngoại tuyến hàng loạt |
| **CRM Events** | `POST` | `/open_api/v1.3/crm/event_set/create/` | Tạo mới bộ sự kiện CRM |
| **CRM Events** | `GET` | `/open_api/v1.3/crm/event_set/get/` | Lấy danh sách các bộ sự kiện CRM |

---

## Tổng quan về Events 1.0 (Events 1.0 Overview)
<a id="doc-1739657891856385"></a>
<!-- doc_id: 1739657891856385 -->

API Sự kiện 1.0 (Events API 1.0) bao gồm 4 nhóm chức năng cốt lõi:
1. **App Events API**: Kết nối và báo cáo hành vi người dùng trên ứng dụng di động (Android / iOS) như mở app (`LAUNCH_APP`), cài đặt (`INSTALLAPP`), mua sắm trong ứng dụng (`PURCHASE`), v.v.
2. **Pixel Events API (Web Events)**: Đo lường hành động của khách truy cập trên trang web (Xem nội dung, Thêm vào giỏ, Mua hàng), quản lý Pixel và cấu hình quy tắc đo lường.
3. **Offline Events API**: Ghi nhận các giao dịch và tương tác trực tiếp tại cửa hàng thực tế, qua tổng đài hoặc tại quầy bán lẻ để kết nối với chiến dịch quảng cáo TikTok.
4. **CRM Events API**: Tích hợp luồng khách hàng tiềm năng (Leads) từ biểu mẫu quảng cáo TikTok trực tiếp về hệ thống CRM của doanh nghiệp.

Các tài liệu liên kết trong nhóm:
* [Báo cáo sự kiện ứng dụng](43-events-1-0-p1.md#doc-1740859196043266)
* [Báo cáo sự kiện ứng dụng hàng loạt](43-events-1-0-p1.md#doc-1740859218541569)
* [Lấy thông tin ứng dụng](43-events-1-0-p1.md#doc-1740859272887297)
* [Tạo ứng dụng](43-events-1-0-p1.md#doc-1740859280958466)
* [Cập nhật ứng dụng](43-events-1-0-p1.md#doc-1740859300069378)
* [Lấy danh sách ứng dụng](43-events-1-0-p1.md#doc-1740859313270786)
* [Lấy sự kiện chuyển đổi ứng dụng](43-events-1-0-p1.md#doc-1740859338750977)
* [Lấy sự kiện Retargeting ứng dụng](43-events-1-0-p1.md#doc-1740859371033601)
* [Báo cáo sự kiện Web](43-events-1-0-p1.md#doc-1740858531237890)
* [Báo cáo sự kiện Web hàng loạt](43-events-1-0-p1.md#doc-1740858565852225)
* [Lấy danh sách Pixel](43-events-1-0-p1.md#doc-1740858697598978)
* [Tạo Pixel](43-events-1-0-p1.md#doc-1740858779758593)
* [Cập nhật Pixel](43-events-1-0-p1.md#doc-1740858799524865)
* [Tạo sự kiện Pixel](43-events-1-0-p1.md#doc-1740858807646209)
* [Cập nhật sự kiện Pixel](43-events-1-0-p1.md#doc-1740858823774210)
* [Xóa sự kiện Pixel](43-events-1-0-p1.md#doc-1740858862104578)
* [Lấy sự kiện Instant Page](43-events-1-0-p1.md#doc-1740898639412226)
* [Thống kê sự kiện Pixel](43-events-1-0-p1.md#doc-1740858904557570)
* [Tạo bộ sự kiện ngoại tuyến](43-events-1-0-p1.md#doc-1758427576470529)
* [Cập nhật bộ sự kiện ngoại tuyến](43-events-1-0-p1.md#doc-1765596741157889)
* [Xóa bộ sự kiện ngoại tuyến](43-events-1-0-p1.md#doc-1765596790860802)
* [Lấy các bộ sự kiện ngoại tuyến](43-events-1-0-p1.md#doc-1765596808589313)
* [Báo cáo sự kiện ngoại tuyến](43-events-1-0-p1.md#doc-1758428013689857)
* [Báo cáo sự kiện ngoại tuyến hàng loạt](43-events-1-0-p1.md#doc-1758428053652482)

---

## Sự kiện ứng dụng (App Events)
<a id="doc-1740857868662786"></a>
<!-- doc_id: 1740857868662786 -->

Nhóm API Sự kiện ứng dụng (App Events API) hỗ trợ đo lường các tương tác của người dùng diễn ra bên trong ứng dụng di động (Android / iOS). Thông qua việc gửi dữ liệu sự kiện lên TikTok, hệ thống học máy có thể tối ưu phân phối cho các chiến dịch App Promotion (Cài đặt ứng dụng hoặc Tái gắn kết).

> **Lưu ý:**
> Tính năng Events API - App yêu cầu đưa vào danh sách cho phép (allowlist). Vui lòng liên hệ đại diện TikTok nếu bạn có nhu cầu kích hoạt tài khoản trước khi gửi sự kiện qua endpoint `/v1.3/app/track/` hoặc `/v1.3/app/batch/`.

Các endpoint trong nhóm App Events:
* [Báo cáo một sự kiện ứng dụng (Report an App Event)](43-events-1-0-p1.md#doc-1740859196043266)
* [Báo cáo sự kiện ứng dụng hàng loạt (Report App Events in bulk)](43-events-1-0-p1.md#doc-1740859218541569)
* [Lấy thông tin chi tiết ứng dụng (Get info of an app)](43-events-1-0-p1.md#doc-1740859272887297)
* [Tạo mới ứng dụng (Create an app)](43-events-1-0-p1.md#doc-1740859280958466)
* [Cập nhật ứng dụng (Update an app)](43-events-1-0-p1.md#doc-1740859300069378)
* [Lấy danh sách ứng dụng (Get the app list)](43-events-1-0-p1.md#doc-1740859313270786)
* [Lấy sự kiện chuyển đổi ứng dụng (Get App Conversion Events)](43-events-1-0-p1.md#doc-1740859338750977)
* [Lấy sự kiện retargeting ứng dụng (Get App Retargeting Events)](43-events-1-0-p1.md#doc-1740859371033601)

---

## Báo cáo một sự kiện ứng dụng (Report an App Event)
<a id="doc-1740859196043266"></a>
<!-- doc_id: 1740859196043266 -->

Sử dụng endpoint này để báo cáo một sự kiện ứng dụng di động (Android / iOS) riêng lẻ (ví dụ: `INSTALLAPP`, `LAUNCH_APP`, `PURCHASE`, `ADD_TO_CART`) về cho TikTok.

### Yêu cầu (Request)

**Endpoint:** `https://business-api.tiktok.com/open_api/v1.3/app/track/`  
**Phương thức (Method):** `POST`

#### Header

| Field | Data Type | Description |
|---|---|---|
| `Access-Token` **(Bắt buộc)** | string | Mã token truy cập được cấp quyền. Xem thêm [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| `Content-Type` **(Bắt buộc)** | string | Định dạng nội dung yêu cầu. Giá trị: `"application/json"`. |

#### Tham số (Parameters)

| Field | Data Type | Description |
|---|---|---|
| `tiktok_app_id` **(Bắt buộc)** | string | TikTok App ID duy nhất được tạo trong Trình quản lý sự kiện TikTok (TikTok Ads Manager). Nhà quảng cáo có thể liên kết nhiều TikTok App ID với cùng một ứng dụng di động. Xem [TikTok App ID](https://ads.tiktok.com/help/article?aid=10001060). |
| `event` | string | Tên sự kiện ứng dụng. Ví dụ: `INSTALLAPP`, `PURCHASE`. Xem danh sách sự kiện được hỗ trợ tại [Supported event types](../09-marketing-api/do-luong-quang-cao-p2.md#doc-1739585574120449). |
| `timestamp` | string | Dấu thời gian diễn ra sự kiện theo định dạng ISO 8601 (ví dụ: `2023-05-20T00:00:00Z`). |
| `context` **(Bắt buộc)** | object | Thông tin kết nối dữ liệu quảng cáo và thông tin người dùng / thiết bị theo định dạng JSON. Xem chi tiết bên dưới. |
| `properties` | object | Các thuộc tính chi tiết đính kèm sự kiện (doanh thu, tiền tệ, nội dung mua sắm) theo định dạng JSON. Xem chi tiết bên dưới. |

#### Đối tượng Context (`context`)

| Field | Data Type | Description |
|---|---|---|
| `context` **(Bắt buộc)** | object | Đối tượng chứa thông tin ngữ cảnh thiết bị, người dùng và dữ liệu phân bổ. |
| `↳ app` **(Bắt buộc)** | object | Chi tiết về ứng dụng gửi báo cáo sự kiện. |
| `↳↳ id` **(Bắt buộc)** | string | ID ứng dụng di động (ví dụ: App Store ID hoặc Google Play package). |
| `↳↳ name` | string | Tên của ứng dụng. |
| `↳↳ namespace` | string | Android package name hoặc iOS Bundle ID. Ví dụ: `com.rovio.angrybirds`. |
| `↳↳ version` | string | Phiên bản ứng dụng (ví dụ: `3.0.2`). |
| `↳↳ build` | string | Số bản dựng (build number) của ứng dụng (ví dụ: `122`). |
| `↳ device` | object | Dữ liệu thiết bị để khớp định danh người dùng. |
| `↳↳ platform` | string | Hệ điều hành của thiết bị (`ANDROID` hoặc `IOS`). |
| `↳↳ idfa` | string | IDFA của thiết bị iOS. Đối với iOS 14+, đảm bảo tuân thủ thu thập iDFA theo chính sách ATT. |
| `↳↳ idfv` | string | IDFV của thiết bị iOS. |
| `↳↳ gaid` | string | Google Advertising ID (GAID). Hỗ trợ cả định dạng gốc và chuỗi băm SHA-256. |
| `↳↳ att_status` | string | Trạng thái cho phép theo dõi App Tracking Transparency (ATT) trên iOS. |
| `↳ locale` | string | Mã ngôn ngữ/địa phương của người dùng (ví dụ: `zh-CN`, `en-US`, `vi-VN`). |
| `↳ ip` | string | Địa chỉ IP của người dùng tại thời điểm phát sinh sự kiện. |
| `↳ user_agent` | string | Chuỗi User Agent từ thiết bị người dùng. |
| `↳ user` | object | Dữ liệu cá nhân của người dùng để khớp danh tính. |
| `↳↳ external_id` | string | ID người dùng ngoại bộ trong hệ thống của bạn, bắt buộc băm bằng SHA-256. |
| `↳↳ phone_number` | string | Số điện thoại của người dùng theo chuẩn E.164, bắt buộc băm bằng SHA-256. |
| `↳↳ email` | string | Địa chỉ email của người dùng, bắt buộc chuẩn hóa viết thường và băm bằng SHA-256 trên phía máy khách. |
| `↳ library` | object | Thông tin phiên bản SDK TikTok được tích hợp. |
| `↳↳ name` | string | Tên thư viện SDK. Ví dụ: `bytedance/tiktok-business-sdk-for-android`. |
| `↳↳ version` | string | Phiên bản SDK (ví dụ: `1.2.0`). |
| `↳ ori_attribution_partner` | string | Tên đối tác đo lường di động (MMP) nếu sự kiện được phân bổ từ MMP (ví dụ: AppsFlyer, Adjust, Singular, Branch). |
| `↳ ad` | object | Thông tin quảng cáo liên quan để phân bổ. |
| `↳↳ callback` | string | Thông tin tham số callback giúp phân bổ sự kiện. |
| `↳↳ campaign_id` | string | ID của chiến dịch quảng cáo. |
| `↳↳ ad_id` | string | ID của nhóm quảng cáo (ad group ID). |
| `↳↳ creative_id` | string | ID của mẫu quảng cáo (ad ID). |
| `↳↳ isRetargeting` | boolean | Cho biết người dùng có phải thuộc chiến dịch retargeting hay không. |
| `↳↳ attributed` | boolean | Cho biết sự kiện đã được phân bổ thành công cho quảng cáo hay chưa. |
| `↳↳ attributionType` | string | Loại phân bổ (click-through, view-through). |
| `↳↳ attribution_provider` | string | Nhà cung cấp phân bổ. |
| `↳ location` | object | Thông tin vị trí địa lý của người dùng. |
| `↳↳ country` | string | Mã quốc gia hoặc khu vực (ví dụ: `VN`, `US`). |
| `↳↳ city` | string | Tên thành phố của người dùng. |

#### Đối tượng Properties (`properties`)

| Field | Data Type | Description |
|---|---|---|
| `properties` | object | Các thuộc tính chi tiết về giao dịch/hành động của sự kiện. |
| `↳ contents` | object[] | Danh sách các sản phẩm/mặt hàng liên quan trong sự kiện (ví dụ: sản phẩm đã mua). |
| `↳↳ price` | double | Đơn giá của từng mặt hàng. |
| `↳↳ quantity` | number | Số lượng của từng mặt hàng. |
| `↳↳ content_type` | string | Loại mặt hàng sản phẩm (ví dụ: `product`, `service`). |
| `↳↳ content_id` | string | Mã định danh duy nhất của sản phẩm trong hệ thống của bạn (SKU hoặc item ID). |
| `↳↳ brand` | string | Thương hiệu của sản phẩm. |
| `↳ currency` | string | Mã tiền tệ theo tiêu chuẩn ISO 4217 (ví dụ: `USD`, `VND`, `EUR`, `JPY`). |
| `↳ value` | double | Tổng giá trị đơn hàng hoặc tổng số tiền của sự kiện. |
| `↳ description` | string | Mô tả chi tiết về sự kiện ứng dụng. |
| `↳ query` | string | Từ khóa tìm kiếm nếu sự kiện liên quan đến thao tác tìm kiếm (`SEARCH`). |

#### Ví dụ gọi API

##### cURL

```bash
curl -X POST 'https://business-api.tiktok.com/open_api/v1.3/app/track/' \
  -H 'Access-Token: YOUR_ACCESS_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{
    "tiktok_app_id": "1765432109876543",
    "event": "PURCHASE",
    "timestamp": "2023-05-20T12:00:00Z",
    "context": {
      "app": {
        "id": "com.example.app",
        "name": "Example App",
        "namespace": "com.example.app",
        "version": "1.0.0",
        "build": "100"
      },
      "device": {
        "platform": "ANDROID",
        "gaid": "38400000-8cf0-11bd-b23e-10b96e40000d"
      },
      "user": {
        "email": "f660ab912ec121d1b1e928a0bb4bc61b15f5ad44d5efdc4e1c92a25e99b8e44a"
      }
    },
    "properties": {
      "currency": "USD",
      "value": 49.99,
      "contents": [
        {
          "content_id": "SKU-12345",
          "content_type": "product",
          "price": 49.99,
          "quantity": 1
        }
      ]
    }
  }'
```

##### Python (requests)

```python
import requests

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
url = "https://business-api.tiktok.com/open_api/v1.3/app/track/"

headers = {
    "Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}

payload = {
    "tiktok_app_id": "1765432109876543",
    "event": "PURCHASE",
    "timestamp": "2023-05-20T12:00:00Z",
    "context": {
      "app": {
        "id": "com.example.app",
        "name": "Example App",
        "namespace": "com.example.app",
        "version": "1.0.0",
        "build": "100"
      },
      "device": {
        "platform": "ANDROID",
        "gaid": "38400000-8cf0-11bd-b23e-10b96e40000d"
      },
      "user": {
        "email": "f660ab912ec121d1b1e928a0bb4bc61b15f5ad44d5efdc4e1c92a25e99b8e44a"
      }
    },
    "properties": {
      "currency": "USD",
      "value": 49.99,
      "contents": [
        {
          "content_id": "SKU-12345",
          "content_type": "product",
          "price": 49.99,
          "quantity": 1
        }
      ]
    }
}

response = requests.post(url, headers=headers, json=payload)
print(response.status_code)
print(response.json())
```

### Phản hồi (Response)

| Field | Data Type | Description |
|---|---|---|
| `code` | number | Mã phản hồi. `0` biểu thị thành công. Các mã khác xem tại [Appendix-Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi từ máy chủ. |
| `request_id` | string | Chuỗi log id duy nhất xác định yêu cầu. |
| `data` | object | Dữ liệu trả về (đối tượng rỗng `{}` khi thành công). |

#### Ví dụ phản hồi thành công

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "2023052210032301011023224213562",
  "data": {}
}
```

---

## Báo cáo sự kiện ứng dụng hàng loạt (Report App Events in bulk)
<a id="doc-1740859218541569"></a>
<!-- doc_id: 1740859218541569 -->

Sử dụng endpoint này để báo cáo sự kiện ứng dụng hàng loạt (batch) nhằm giảm tải tần suất gọi đến TikTok Marketing API. Bạn có thể gửi tối đa **1.000 sự kiện** trong một yêu cầu duy nhất. Nếu vượt quá 1.000 sự kiện, toàn bộ yêu cầu sẽ bị từ chối.

### Yêu cầu (Request)

**Endpoint:** `https://business-api.tiktok.com/open_api/v1.3/app/batch/`  
**Phương thức (Method):** `POST`

#### Header

| Field | Data Type | Description |
|---|---|---|
| `Access-Token` **(Bắt buộc)** | string | Mã token truy cập được cấp quyền. Xem thêm [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| `Content-Type` **(Bắt buộc)** | string | Định dạng nội dung yêu cầu. Giá trị: `"application/json"`. |

#### Tham số (Parameters)

| Field | Data Type | Description |
|---|---|---|
| `tiktok_app_id` **(Bắt buộc)** | string | TikTok App ID được tạo trong Trình quản lý sự kiện và liên kết với ứng dụng di động. |
| `batch` **(Bắt buộc)** | object[] | Mảng chứa các sự kiện ứng dụng cần gửi theo đợt. Số lượng phần tử phải từ 2 đến 1.000. |
| `↳ type` **(Bắt buộc)** | string | Loại sự kiện ứng dụng. Hiện tại chỉ hỗ trợ giá trị `track`. |
| `↳ event` | string | Tên sự kiện ứng dụng (ví dụ: `INSTALLAPP`, `PURCHASE`). |
| `↳ timestamp` | string | Dấu thời gian diễn ra sự kiện theo định dạng ISO 8601. |
| `↳ context` **(Bắt buộc)** | object | Thông tin ngữ cảnh thiết bị, người dùng và dữ liệu phân bổ (cấu trúc giống endpoint `/app/track/`). |
| `↳ properties` | object | Các thuộc tính chi tiết đính kèm sự kiện (doanh thu, tiền tệ, nội dung mua sắm). |

#### Đối tượng Context trong mảng Batch (`context`)

| Field | Data Type | Description |
|---|---|---|
| `context` **(Bắt buộc)** | object | Thông tin kết nối dữ liệu quảng cáo và định danh người dùng. |
| `↳ app` **(Bắt buộc)** | object | Chi tiết về ứng dụng di động. |
| `↳↳ id` **(Bắt buộc)** | string | ID ứng dụng di động. |
| `↳↳ name` | string | Tên ứng dụng. |
| `↳↳ namespace` | string | Android package name hoặc iOS Bundle ID. |
| `↳↳ version` | string | Số phiên bản ứng dụng (ví dụ: `3.0.2`). |
| `↳↳ build` | string | Số bản dựng (ví dụ: `122`). |
| `↳ device` | object | Dữ liệu thiết bị để khớp người dùng. |
| `↳↳ platform` | string | Hệ điều hành thiết bị (`ANDROID` hoặc `IOS`). |
| `↳↳ idfa` | string | iOS IDFA. |
| `↳↳ idfv` | string | iOS IDFV. |
| `↳↳ gaid` | string | Google Advertising ID (GAID). |
| `↳↳ att_status` | string | Trạng thái cho phép theo dõi người dùng theo chính sách ATT của Apple. |
| `↳ locale` | string | Ngôn ngữ/vùng của người dùng (ví dụ: `zh-CN`, `en-US`). |
| `↳ ip` | string | Địa chỉ IP của người dùng. |
| `↳ user_agent` | string | User agent của thiết bị. |
| `↳ user` | object | Dữ liệu cá nhân của người dùng. |
| `↳↳ external_id` | string | ID người dùng ngoại bộ, bắt buộc băm SHA-256. |
| `↳↳ phone_number` | string | Số điện thoại người dùng, bắt buộc băm SHA-256. |
| `↳↳ email` | string | Email người dùng, bắt buộc băm SHA-256 trên phía máy khách. |
| `↳ library` | object | Thông tin thư viện SDK. |
| `↳↳ name` | string | Tên thư viện SDK. |
| `↳↳ version` | string | Phiên bản thư viện SDK. |
| `↳ ori_attribution_partner` | string | Đối tác phân bổ di động (MMP) nếu sự kiện được phân bổ từ MMP. |
| `↳ ad` | object | Dữ liệu quảng cáo phục vụ phân bổ. |
| `↳↳ callback` | string | Tham số callback hỗ trợ phân bổ sự kiện. |
| `↳↳ campaign_id` | string | ID chiến dịch quảng cáo. |
| `↳↳ ad_id` | string | ID nhóm quảng cáo (ad group ID). |
| `↳↳ creative_id` | string | ID mẫu quảng cáo (ad ID). |
| `↳↳ isRetargeting` | boolean | Người dùng có thuộc tệp tiếp thị lại (retargeting) hay không. |
| `↳↳ attributed` | boolean | Sự kiện có được phân bổ cho quảng cáo hay không. |
| `↳↳ attributionType` | string | Loại phân bổ. |
| `↳↳ attribution_provider` | string | Đơn vị cung cấp phân bổ. |
| `↳ location` | object | Vị trí địa lý của người dùng. |
| `↳↳ country` | string | Quốc gia hoặc vùng lãnh thổ. |
| `↳↳ city` | string | Thành phố. |

#### Đối tượng Properties trong mảng Batch (`properties`)

| Field | Data Type | Description |
|---|---|---|
| `properties` | object | Các thuộc tính giao dịch gắn kèm sự kiện. |
| `↳ contents` | object[] | Danh sách các mặt hàng liên quan trong sự kiện. |
| `↳↳ price` | double | Đơn giá mặt hàng. |
| `↳↳ quantity` | number | Số lượng mặt hàng. |
| `↳↳ content_type` | string | Loại sản phẩm/dịch vụ. |
| `↳↳ content_id` | string | Mã định danh sản phẩm trong hệ thống của bạn. |
| `↳↳ brand` | string | Tên thương hiệu của sản phẩm. |
| `↳ currency` | string | Mã tiền tệ ISO 4217 (ví dụ: `USD`, `VND`). |
| `↳ value` | double | Tổng giá trị đơn hàng hoặc tổng giá trị sự kiện. |
| `↳ description` | string | Mô tả sự kiện ứng dụng. |
| `↳ query` | string | Chuỗi văn bản người dùng tìm kiếm. |

#### Ví dụ gọi API

##### cURL

```bash
curl -X POST 'https://business-api.tiktok.com/open_api/v1.3/app/batch/' \
  -H 'Access-Token: YOUR_ACCESS_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{
    "tiktok_app_id": "1765432109876543",
    "batch": [
      {
        "type": "track",
        "event": "LAUNCH_APP",
        "timestamp": "2023-05-20T12:00:00Z",
        "context": {
          "app": {
            "id": "com.example.app",
            "name": "Example App",
            "namespace": "com.example.app"
          },
          "device": {
            "platform": "ANDROID",
            "gaid": "38400000-8cf0-11bd-b23e-10b96e40000d"
          }
        }
      },
      {
        "type": "track",
        "event": "PURCHASE",
        "timestamp": "2023-05-20T12:05:00Z",
        "context": {
          "app": {
            "id": "com.example.app",
            "name": "Example App",
            "namespace": "com.example.app"
          },
          "device": {
            "platform": "ANDROID",
            "gaid": "38400000-8cf0-11bd-b23e-10b96e40000d"
          }
        },
        "properties": {
          "currency": "USD",
          "value": 19.99
        }
      }
    ]
  }'
```

##### Python (requests)

```python
import requests

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
url = "https://business-api.tiktok.com/open_api/v1.3/app/batch/"

headers = {
    "Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}

payload = {
    "tiktok_app_id": "1765432109876543",
    "batch": [
      {
        "type": "track",
        "event": "LAUNCH_APP",
        "timestamp": "2023-05-20T12:00:00Z",
        "context": {
          "app": {
            "id": "com.example.app",
            "name": "Example App",
            "namespace": "com.example.app"
          },
          "device": {
            "platform": "ANDROID",
            "gaid": "38400000-8cf0-11bd-b23e-10b96e40000d"
          }
        }
      },
      {
        "type": "track",
        "event": "PURCHASE",
        "timestamp": "2023-05-20T12:05:00Z",
        "context": {
          "app": {
            "id": "com.example.app",
            "name": "Example App",
            "namespace": "com.example.app"
          },
          "device": {
            "platform": "ANDROID",
            "gaid": "38400000-8cf0-11bd-b23e-10b96e40000d"
          }
        },
        "properties": {
          "currency": "USD",
          "value": 19.99
        }
      }
    ]
}

response = requests.post(url, headers=headers, json=payload)
print(response.status_code)
print(response.json())
```

### Phản hồi (Response)

| Field | Data Type | Description |
|---|---|---|
| `code` | number | Mã phản hồi. `0` biểu thị thành công. Các mã khác xem tại [Appendix-Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi từ máy chủ. |
| `request_id` | string | Chuỗi log id duy nhất của yêu cầu. |
| `data` | object | Dữ liệu trả về. |
| `↳ partial_failure` | boolean | Cho biết việc báo cáo sự kiện có bị thất bại một phần hay không (`true`/`false`). |
| `↳ failed_events` | object[] | Danh sách chi tiết các sự kiện bị lỗi trong trường hợp thất bại một phần. |
| `↳↳ order_in_batch` | number | Vị trí thứ tự của sự kiện bị lỗi trong mảng `batch` gửi lên (bắt đầu từ 0). |
| `↳↳ error` | string | Thông điệp mô tả chi tiết lỗi phát sinh đối với sự kiện tương ứng. |

#### Ví dụ phản hồi thành công

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "2023052210032301011023224213562",
  "data": {
    "partial_failure": false,
    "failed_events": []
  }
}
```


---

## Lấy thông tin ứng dụng (Get info of an app)
<a id="doc-1740859272887297"></a>
<!-- doc_id: 1740859272887297 -->

Sử dụng endpoint này để lấy thông tin chi tiết của một ứng dụng di động đã đăng ký trong tài khoản quảng cáo.

### Yêu cầu (Request)

**Endpoint:** `https://business-api.tiktok.com/open_api/v1.3/app/info/`  
**Phương thức (Method):** `GET`

#### Header

| Field | Data Type | Description |
|---|---|---|
| `Access-Token` **(Bắt buộc)** | string | Mã token truy cập được cấp quyền. Xem thêm [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

#### Tham số (Parameters)

| Field | Data Type | Description |
|---|---|---|
| `advertiser_id` **(Bắt buộc)** | string | ID của nhà quảng cáo. |
| `app_id` **(Bắt buộc)** | string | ID của ứng dụng di động trên hệ thống TikTok. |

#### Ví dụ gọi API

##### cURL

```bash
curl -X GET 'https://business-api.tiktok.com/open_api/v1.3/app/info/?advertiser_id=7123456789012345678&app_id=1765432109876543' \
  -H 'Access-Token: YOUR_ACCESS_TOKEN'
```

##### Python (requests)

```python
import requests

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ADVERTISER_ID = "7123456789012345678"
APP_ID = "1765432109876543"
url = "https://business-api.tiktok.com/open_api/v1.3/app/info/"

headers = {
    "Access-Token": ACCESS_TOKEN
}

params = {
    "advertiser_id": ADVERTISER_ID,
    "app_id": APP_ID
}

response = requests.get(url, headers=headers, params=params)
print(response.status_code)
print(response.json())
```

### Phản hồi (Response)

| Field | Data Type | Description |
|---|---|---|
| `code` | number | Mã phản hồi. `0` biểu thị thành công. Các mã khác xem tại [Appendix-Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi từ hệ thống. |
| `request_id` | string | Chuỗi log id duy nhất xác định yêu cầu. |
| `data` | object | Dữ liệu trả về. |
| `↳ app` | object | Chi tiết thông tin ứng dụng di động. |
| `↳↳ advertiser_id` | string | ID của nhà quảng cáo sở hữu ứng dụng. |
| `↳↳ app_platform_id` | string | ID nền tảng ứng dụng (App Store ID hoặc Google Play package). |
| `↳↳ app_name` | string | Tên của ứng dụng. |
| `↳↳ self_attribution_enabled` | boolean | Cho biết tính năng tự phân bổ (Self-Attribution - SAN), thay vì phân bổ bên thứ ba, có được bật hay không (`true`/`false`). |
| `↳↳ skan_allowed` | string | Cho biết ứng dụng có thể dùng để tạo chiến dịch iOS 14 Dedicated Campaign nhắm tới thiết bị iOS 14.5+ hay không. Enum: `ALLOWED`, `NOT_ALLOWED`. |
| `↳↳ advanced_dedicated_campaign_allowed` | boolean | Cho biết ứng dụng có thể sử dụng trong Advanced Dedicated Campaigns hay không. Xem [Create Advanced Dedicated Campaigns](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1797011827608577). Giá trị: `true`, `false`. |
| `↳↳ is_attribution_flex_enable` | boolean | Cho biết ứng dụng có đủ điều kiện cấu hình nguồn phân bổ và nguồn dữ liệu linh hoạt khi tạo Upgraded Smart+ Ad Group hay không. Giá trị: `true`, `false`. |
| `↳↳ download_url` | string | Đường dẫn tải ứng dụng trên App Store / Google Play. |
| `↳↳ icon` | object | Thông tin biểu tượng (icon) ứng dụng. |
| `↳↳↳ height` | number | Chiều cao biểu tượng (pixels). |
| `↳↳↳ web_uri` | string | URI/ID hình ảnh biểu tượng. |
| `↳↳↳ width` | number | Chiều rộng biểu tượng (pixels). |
| `↳↳ app_id` | string | ID ứng dụng trên TikTok. |
| `↳↳ package_name` | string | Tên package ứng dụng. |
| `↳↳ tiktok_apps` | object[] | Danh sách thông tin TikTok App ID liên kết. |
| `↳↳↳ tiktok_app_id` | string | TikTok App ID. Chỉ trả về nếu MMP theo dõi được hỗ trợ. |
| `↳↳ partner` | object | Thông tin đối tác đo lường bên thứ ba (MMP). |
| `↳↳↳ partner_id` | string | ID đối tác. |
| `↳↳↳ partner_logo` | string | URI biểu trưng (logo) của đối tác. |
| `↳↳↳ partner_name` | string | Tên đối tác đo lường. |
| `↳↳ platform` | string | Nền tảng ứng dụng. Enum: `ANDROID`, `IOS`. |
| `↳↳ enable_retargeting` | string | Cho biết có bật phân bổ tiếp thị lại hay không. Enum: `RETARGETING`, `NON_RETARGETING`. |
| `↳↳ tracking_url` | object | Các liên kết theo dõi từ đối tác thứ ba. |
| `↳↳↳ click_url` | string | Liên kết theo dõi lượt nhấp (Click tracking URL). |
| `↳↳↳ impression_url` | string | Liên kết theo dõi lượt hiển thị mặc định (Impression tracking URL). |
| `↳↳↳ retargeting_click_url` | string | Liên kết theo dõi lượt nhấp cho chiến dịch tiếp thị lại. |
| `↳↳↳ retargeting_impression_url` | string | Liên kết theo dõi lượt hiển thị cho chiến dịch tiếp thị lại. |
| `↳↳ create_time` | string | Thời gian tạo ứng dụng trên hệ thống. |

#### Ví dụ phản hồi thành công

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "2026011307510301018905602824580D00",
  "data": {
    "app": {
      "advanced_dedicated_campaign_allowed": false,
      "advertiser_id": "7123456789012345678",
      "app_id": "1765432109876543",
      "app_name": "Example Game",
      "app_platform_id": "com.example.game",
      "create_time": "2026-01-13T07:51:03Z",
      "download_url": "https://play.google.com/store/apps/details?id=com.example.game",
      "enable_retargeting": "RETARGETING",
      "icon": {
        "height": 180,
        "web_uri": "tos-maliva-p-0000/icon_example",
        "width": 180
      },
      "is_attribution_flex_enable": true,
      "package_name": "com.example.game",
      "partner": {
        "partner_id": "1",
        "partner_logo": "https://example.com/logo.png",
        "partner_name": "AppsFlyer"
      },
      "platform": "ANDROID",
      "self_attribution_enabled": true,
      "skan_allowed": "ALLOWED",
      "tiktok_apps": [
        {
          "tiktok_app_id": "7123456789012345678"
        }
      ],
      "tracking_url": {
        "click_url": "https://app.appsflyer.com/com.example.game?pid=tiktok_int",
        "impression_url": "",
        "retargeting_click_url": "",
        "retargeting_impression_url": ""
      }
    }
  }
}
```

---

## Tạo ứng dụng (Create an app)
<a id="doc-1740859280958466"></a>
<!-- doc_id: 1740859280958466 -->

Sử dụng endpoint này để đăng ký một ứng dụng di động mới trên TikTok Ads Manager. Ứng dụng sau khi tạo có thể được sử dụng để tạo nhóm quảng cáo và chiến dịch App Promotion.

### Yêu cầu (Request)

**Endpoint:** `https://business-api.tiktok.com/open_api/v1.3/app/create/`  
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
| `download_url` **(Bắt buộc)** | url | Đường dẫn tải ứng dụng trên App Store hoặc Google Play. |
| `partner` | string | Đối tác đo lường bên thứ ba (MMP).<br>Enum: `AdBrix`, `Adjust`, `AppLink`, `AppsFlyer`, `DoubleClick`, `FlashTalking`, `Kochava`, `Other`, `ServingsSys`, `Singular`, `Tenjin`, `TlnkIo`. Xem thêm [Third Party Monitoring Partner](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| `tracking_url` {+Conditional} | object | Bắt buộc trong các trường hợp: `partner` là `Adjust`, hoặc đối tác chưa bật mạng tự phân bổ (SAN). Đối tượng chứa các liên kết theo dõi. |
| `↳ click_url` {+Conditional} | url | Liên kết theo dõi lượt nhấp do đối tác MMP cung cấp. |
| `↳ impression_url` | url | Liên kết theo dõi lượt hiển thị mặc định do đối tác MMP cung cấp. |

#### Ví dụ gọi API

##### cURL

```bash
curl -X POST 'https://business-api.tiktok.com/open_api/v1.3/app/create/' \
  -H 'Access-Token: YOUR_ACCESS_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{
    "advertiser_id": "7123456789012345678",
    "download_url": "https://play.google.com/store/apps/details?id=com.example.game",
    "partner": "AppsFlyer",
    "tracking_url": {
      "click_url": "https://app.appsflyer.com/com.example.game?pid=tiktok_int"
    }
  }'
```

##### Python (requests)

```python
import requests

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ADVERTISER_ID = "7123456789012345678"
url = "https://business-api.tiktok.com/open_api/v1.3/app/create/"

headers = {
    "Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}

payload = {
    "advertiser_id": ADVERTISER_ID,
    "download_url": "https://play.google.com/store/apps/details?id=com.example.game",
    "partner": "AppsFlyer",
    "tracking_url": {
        "click_url": "https://app.appsflyer.com/com.example.game?pid=tiktok_int"
    }
}

response = requests.post(url, headers=headers, json=payload)
print(response.status_code)
print(response.json())
```

### Phản hồi (Response)

| Field | Data Type | Description |
|---|---|---|
| `code` | number | Mã phản hồi. `0` biểu thị thành công. Các mã khác xem tại [Appendix-Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi từ hệ thống. |
| `data` | object | Dữ liệu trả về. |
| `↳ app_id` | string | ID của ứng dụng di động mới được tạo trên TikTok. |
| `request_id` | string | Chuỗi log id duy nhất xác định yêu cầu. |

#### Ví dụ phản hồi thành công

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "2020032412242801018905602824580D00",
  "data": {
    "app_id": "6734587012554160000"
  }
}
```

---

## Cập nhật ứng dụng (Update an app)
<a id="doc-1740859300069378"></a>
<!-- doc_id: 1740859300069378 -->

Sử dụng endpoint này để cập nhật thông tin ứng dụng di động đã tạo, chẳng hạn như đường dẫn tải về (`download_url`) và các liên kết theo dõi bên thứ ba (`tracking_url`).

### Yêu cầu (Request)

**Endpoint:** `https://business-api.tiktok.com/open_api/v1.3/app/update/`  
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
| `app_id` **(Bắt buộc)** | string | ID của ứng dụng di động cần cập nhật. |
| `download_url` | url | Đường dẫn tải ứng dụng mới. |
| `platform` {+Conditional} | string | Nền tảng ứng dụng. Enum: `ANDROID`, `IOS`. Bắt buộc truyền khi cập nhật trường `download_url`. |
| `partner` | string | Đối tác đo lường bên thứ ba (MMP). Enum: `AdBrix`, `Adjust`, `AppLink`, `AppsFlyer`, `DoubleClick`, `FlashTalking`, `Kochava`, `Other`, `ServingsSys`, `Singular`, `Tenjin`, `TlnkIo`. |
| `tracking_url` {+Conditional} | object | Cấu hình liên kết theo dõi bên thứ ba. Bắt buộc khi `partner` là `Adjust` hoặc chưa bật mạng tự phân bổ (SAN). |
| `↳ click_url` {+Conditional} | url | Liên kết theo dõi lượt nhấp do đối tác cung cấp. |
| `↳ impression_url` | url | Liên kết theo dõi lượt hiển thị mặc định. |
| `enable_retargeting` | string | Tùy chọn bật phân bổ tiếp thị lại. Enum: `RETARGETING`, `NON_RETARGETING`.<br>**Lưu ý:** Hiện tại để bật tính năng này, bạn cần truy cập trực tiếp Events Manager trên giao diện web. |

#### Ví dụ gọi API

##### cURL

```bash
curl -X POST 'https://business-api.tiktok.com/open_api/v1.3/app/update/' \
  -H 'Access-Token: YOUR_ACCESS_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{
    "advertiser_id": "7123456789012345678",
    "app_id": "6734587012554160000",
    "download_url": "https://play.google.com/store/apps/details?id=com.example.game",
    "platform": "ANDROID",
    "partner": "AppsFlyer",
    "tracking_url": {
      "click_url": "https://app.appsflyer.com/com.example.game?pid=tiktok_int",
      "impression_url": "https://app.appsflyer.com/com.example.game?pid=tiktok_int_imp"
    }
  }'
```

##### Python (requests)

```python
import requests

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ADVERTISER_ID = "7123456789012345678"
url = "https://business-api.tiktok.com/open_api/v1.3/app/update/"

headers = {
    "Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}

payload = {
    "advertiser_id": ADVERTISER_ID,
    "app_id": "6734587012554160000",
    "download_url": "https://play.google.com/store/apps/details?id=com.example.game",
    "platform": "ANDROID",
    "partner": "AppsFlyer",
    "tracking_url": {
        "click_url": "https://app.appsflyer.com/com.example.game?pid=tiktok_int",
        "impression_url": "https://app.appsflyer.com/com.example.game?pid=tiktok_int_imp"
    }
}

response = requests.post(url, headers=headers, json=payload)
print(response.status_code)
print(response.json())
```

### Phản hồi (Response)

| Field | Data Type | Description |
|---|---|---|
| `code` | number | Mã phản hồi. `0` biểu thị thành công. Các mã khác xem tại [Appendix-Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi từ hệ thống. |
| `data` | object | Dữ liệu trả về (đối tượng rỗng `{}` khi cập nhật thành công). |
| `request_id` | string | Chuỗi log id duy nhất xác định yêu cầu. |

#### Ví dụ phản hồi thành công

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "2020032412242801018905602824580D00",
  "data": {}
}
```

---

## Lấy danh sách ứng dụng (Get the app list)
<a id="doc-1740859313270786"></a>
<!-- doc_id: 1740859313270786 -->

Sử dụng endpoint này để lấy danh sách các ứng dụng di động đã được tạo dưới tài khoản quảng cáo.

### Yêu cầu (Request)

**Endpoint:** `https://business-api.tiktok.com/open_api/v1.3/app/list/`  
**Phương thức (Method):** `GET`

#### Header

| Field | Data Type | Description |
|---|---|---|
| `Access-Token` **(Bắt buộc)** | string | Mã token truy cập được cấp quyền. Xem thêm [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

#### Tham số (Parameters)

| Field | Data Type | Description |
|---|---|---|
| `advertiser_id` **(Bắt buộc)** | string | ID của nhà quảng cáo. |
| `app_platform_ids` | string[] | Danh sách ID nền tảng ứng dụng (App platform IDs) dùng để lọc kết quả. Định dạng chuỗi JSON mã hóa URL. |

#### Ví dụ gọi API

##### cURL

```bash
curl -X GET 'https://business-api.tiktok.com/open_api/v1.3/app/list/?advertiser_id=7123456789012345678' \
  -H 'Access-Token: YOUR_ACCESS_TOKEN'
```

##### Python (requests)

```python
import requests

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ADVERTISER_ID = "7123456789012345678"
url = "https://business-api.tiktok.com/open_api/v1.3/app/list/"

headers = {
    "Access-Token": ACCESS_TOKEN
}

params = {
    "advertiser_id": ADVERTISER_ID
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
| `request_id` | string | Chuỗi log id duy nhất xác định yêu cầu. |
| `data` | object | Dữ liệu trả về. |
| `↳ apps` | object[] | Danh sách các ứng dụng di động thuộc tài khoản. |
| `↳↳ advertiser_id` | string | ID của nhà quảng cáo sở hữu ứng dụng. |
| `↳↳ app_platform_id` | string | ID nền tảng ứng dụng. |
| `↳↳ app_name` | string | Tên của ứng dụng. |
| `↳↳ app_id` | string | ID ứng dụng trên TikTok. |
| `↳↳ package_name` | string | Tên package của ứng dụng. |
| `↳↳ platform` | string | Nền tảng ứng dụng (`ANDROID` hoặc `IOS`). |
| `↳↳ download_url` | string | Đường dẫn tải ứng dụng. |
| `↳↳ self_attribution_enabled` | boolean | Cho biết tính năng tự phân bổ có được bật hay không. |
| `↳↳ skan_allowed` | string | Khả năng chạy chiến dịch iOS 14 Dedicated Campaign (`ALLOWED`, `NOT_ALLOWED`). |
| `↳↳ advanced_dedicated_campaign_allowed` | boolean | Khả năng tham gia Advanced Dedicated Campaigns (`true`/`false`). |
| `↳↳ is_attribution_flex_enable` | boolean | Khả năng cấu hình nguồn phân bổ linh hoạt. |
| `↳↳ icon` | object | Thông tin biểu tượng ứng dụng (`height`, `width`, `web_uri`). |
| `↳↳ partner` | object | Thông tin đối tác đo lường MMP (`partner_id`, `partner_name`, `partner_logo`). |
| `↳↳ tiktok_apps` | object[] | Danh sách thông tin TikTok App ID (`tiktok_app_id`). |
| `↳↳ tracking_url` | object | Các liên kết theo dõi (`click_url`, `impression_url`, `retargeting_click_url`, `retargeting_impression_url`). |
| `↳↳ enable_retargeting` | string | Tùy chọn tiếp thị lại (`RETARGETING`, `NON_RETARGETING`). |
| `↳↳ create_time` | string | Thời điểm tạo ứng dụng. |

#### Ví dụ phản hồi thành công

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "2026070915300801018905602824580D00",
  "data": {
    "apps": [
      {
        "advanced_dedicated_campaign_allowed": false,
        "advertiser_id": "7123456789012345678",
        "app_id": "6734587012554160000",
        "app_name": "Example App iOS",
        "app_platform_id": "id1234567890",
        "create_time": "2026-07-09T15:30:08Z",
        "download_url": "https://apps.apple.com/app/id1234567890",
        "enable_retargeting": "RETARGETING",
        "package_name": "com.example.app",
        "platform": "IOS",
        "self_attribution_enabled": true,
        "skan_allowed": "ALLOWED"
      }
    ]
  }
}
```

---

## Lấy sự kiện chuyển đổi ứng dụng (Get App Conversion Events)
<a id="doc-1740859338750977"></a>
<!-- doc_id: 1740859338750977 -->

Sử dụng endpoint này để lấy thông tin về các sự kiện chuyển đổi của ứng dụng di động nhằm phục vụ thiết lập mục tiêu tối ưu hóa (`optimization_goal`) và giá thầu trong nhóm quảng cáo.

### Yêu cầu (Request)

**Endpoint:** `https://business-api.tiktok.com/open_api/v1.3/app/optimization_event/`  
**Phương thức (Method):** `GET`

#### Header

| Field | Data Type | Description |
|---|---|---|
| `Access-Token` **(Bắt buộc)** | string | Mã token truy cập được cấp quyền. Xem thêm [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

#### Tham số (Parameters)

| Field | Data Type | Description |
|---|---|---|
| `advertiser_id` **(Bắt buộc)** | string | ID của nhà quảng cáo. |
| `app_id` **(Bắt buộc)** | string | ID ứng dụng trên TikTok. |
| `placement_type` | string | Chiến lược vị trí phân phối quảng cáo. Enum: `PLACEMENT_TYPE_AUTOMATIC` (Tự động), `PLACEMENT_TYPE_NORMAL` (Tự chọn). Mặc định: `PLACEMENT_TYPE_NORMAL`. |
| `placement` {+Conditional} | string[] | Mảng các ứng dụng muốn phân phối quảng cáo đến. Bắt buộc khi `placement_type` là `PLACEMENT_TYPE_NORMAL`. Enum: `PLACEMENT_TIKTOK`, `PLACEMENT_PANGLE`, `PLACEMENT_GLOBAL_APP_BUNDLE`. Không sử dụng `PLACEMENT_TOPBUZZ` hoặc `PLACEMENT_HELO` (đã lỗi thời). Xem [Enumeration - Placement](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| `optimization_goal` **(Bắt buộc)** | string | Mục tiêu tối ưu hóa. Enum xem tại [Enumeration-Optimization Goal](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| `objective` **(Bắt buộc)** | string | Mục tiêu chiến dịch quảng cáo (Advertising Objective). Enum xem tại [Enumeration-Advertising Objective](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| `app_promotion_type` {+Conditional} | string | Loại quảng bá ứng dụng. Bắt buộc khi `objective` là `APP_PROMOTION`. Enum: `APP_INSTALL` (cài đặt ứng dụng), `APP_RETARGETING` (tái tương tác). |
| `available_only` | boolean | Chỉ trả về các sự kiện chuyển đổi khả dụng hay không. Mặc định: `true`. |
| `is_skan` | boolean | Cho biết ứng dụng có sử dụng tính năng SKAdNetwork (SKAN) hay không. |

#### Ví dụ gọi API

##### cURL

```bash
curl -X GET 'https://business-api.tiktok.com/open_api/v1.3/app/optimization_event/?advertiser_id=7123456789012345678&app_id=6734587012554160000&objective=APP_PROMOTION&optimization_goal=INSTALL&available_only=true' \
  -H 'Access-Token: YOUR_ACCESS_TOKEN'
```

##### Python (requests)

```python
import requests

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ADVERTISER_ID = "7123456789012345678"
url = "https://business-api.tiktok.com/open_api/v1.3/app/optimization_event/"

headers = {
    "Access-Token": ACCESS_TOKEN
}

params = {
    "advertiser_id": ADVERTISER_ID,
    "app_id": "6734587012554160000",
    "objective": "APP_PROMOTION",
    "optimization_goal": "INSTALL",
    "available_only": True
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
| `data` | object | Dữ liệu trả về. |
| `↳ optimization_events` | object[] | Danh sách sự kiện hành động bên ngoài (external action list). |
| `↳↳ optimization_event` | string | Tên sự kiện chuyển đổi bạn muốn đo lường. Xem [Appendix-Conversion Events-App Event Type](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1739361474981889). |
| `↳↳ statistic_type` | string | Loại thống kê đặt giá thầu: `EVERYTIME` (Mỗi lượt mua) hoặc `NONE` (Lượt mua duy nhất). |
| `↳↳ availability_status` | string | Trạng thái khả dụng của sự kiện. Enum: `INACTIVE` (không khả dụng), `INSUFFICIENT_POSTBACK` (chưa đủ dữ liệu postback), `READY` (khả dụng). |
| `↳↳ conversions` | number | Số lượng sự kiện chuyển đổi postback ghi nhận trong 30 ngày qua. |
| `↳↳ unlock_threshold` | number | Ngưỡng số lượng chuyển đổi cần thiết để sự kiện mở khóa từ `INSUFFICIENT_POSTBACK` sang `READY`. |
| `↳↳ is_beta` | boolean | Cho biết sự kiện có đang trong giai đoạn thử nghiệm beta hay không. |
| `↳↳ bid_type_availability` | object | Tính khả dụng của các loại giá thầu và giá thầu sâu (deep bid types). |
| `↳↳↳ no_bid_enabled` | boolean | Sự kiện có hỗ trợ `bid_type` = `BID_TYPE_NO_BID` (Phân phối tối đa) hay không. |
| `↳↳↳ auto_bid_enabled` | boolean | Sự kiện có hỗ trợ `deep_bid_type` = `PACING` (đặt thầu tự động) hay không. |
| `↳↳↳ multi_bid_enabled` | boolean | Sự kiện có hỗ trợ `deep_bid_type` = `MIN` (đa thầu) hay không. |
| `↳↳ deep_optimization_events` | object | Thông tin sự kiện chuyển đổi sâu (deep conversion events). |
| `↳↳↳ optimization_event` | string | Tên sự kiện chuyển đổi sâu. |
| `↳↳↳ statistic_type` | string | Loại thống kê đặt thầu chuyển đổi sâu. |
| `↳↳↳ availability_status` | string | Trạng thái khả dụng của sự kiện chuyển đổi sâu (`INACTIVE`, `INSUFFICIENT_POSTBACK`, `READY`). |
| `↳↳↳ conversions` | number | Lượt chuyển đổi sâu trong 30 ngày qua. |
| `↳↳↳ unlock_threshold` | number | Ngưỡng chuyển đổi sâu để mở khóa. |
| `request_id` | string | Chuỗi log id duy nhất xác định yêu cầu. |

#### Ví dụ phản hồi thành công

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "2020052214483801023125009011089",
  "data": {
    "optimization_events": [
      {
        "optimization_event": "INSTALL",
        "statistic_type": "EVERYTIME",
        "availability_status": "READY",
        "conversions": 1500,
        "unlock_threshold": 20,
        "is_beta": false,
        "bid_type_availability": {
          "no_bid_enabled": true,
          "auto_bid_enabled": true,
          "multi_bid_enabled": false
        }
      }
    ]
  }
}
```

---

## Lấy sự kiện Retargeting ứng dụng (Get App Retargeting Events)
<a id="doc-1740859371033601"></a>
<!-- doc_id: 1740859371033601 -->

Sử dụng endpoint này để lấy danh sách sự kiện tiếp thị lại (retargeting) của ứng dụng, phục vụ định nghĩa Quy tắc đối tượng (Audience Rules) để xây dựng tệp đối tượng tùy chỉnh. Xem [Audience rules](../09-marketing-api/audience.md#doc-1739566532187138).

### Yêu cầu (Request)

**Endpoint:** `https://business-api.tiktok.com/open_api/v1.3/app/optimization_event/retargeting/`  
**Phương thức (Method):** `GET`

#### Header

| Field | Data Type | Description |
|---|---|---|
| `Access-Token` **(Bắt buộc)** | string | Mã token truy cập được cấp quyền. Xem thêm [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

#### Tham số (Parameters)

| Field | Data Type | Description |
|---|---|---|
| `advertiser_id` **(Bắt buộc)** | string | ID của nhà quảng cáo. |
| `app_id` **(Bắt buộc)** | string | ID của ứng dụng di động trên TikTok. |

#### Ví dụ gọi API

##### cURL

```bash
curl -X GET 'https://business-api.tiktok.com/open_api/v1.3/app/optimization_event/retargeting/?advertiser_id=7123456789012345678&app_id=6734587012554160000' \
  -H 'Access-Token: YOUR_ACCESS_TOKEN'
```

##### Python (requests)

```python
import requests

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ADVERTISER_ID = "7123456789012345678"
url = "https://business-api.tiktok.com/open_api/v1.3/app/optimization_event/retargeting/"

headers = {
    "Access-Token": ACCESS_TOKEN
}

params = {
    "advertiser_id": ADVERTISER_ID,
    "app_id": "6734587012554160000"
}

response = requests.get(url, headers=headers, params=params)
print(response.status_code)
print(response.json())
```

### Phản hồi (Response)

| Field | Data Type | Description |
|---|---|---|
| `code` | number | Mã phản hồi. `0` biểu thị thành công. Các mã khác xem tại [Appendix-Return code](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi từ hệ thống. |
| `data` | object | Dữ liệu trả về. |
| `↳ optimization_events` | string[] | Danh sách tên các sự kiện retargeting ứng dụng dùng để thiết lập quy tắc tệp đối tượng tùy chỉnh. Xem [Audience rules](../09-marketing-api/audience.md#doc-1739566532187138) và [Appendix-Conversion events-App event types](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1739361474981889). |
| `request_id` | string | Chuỗi log id duy nhất xác định yêu cầu. |

#### Ví dụ phản hồi thành công

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "2020052214483801023125009011089",
  "data": {
    "optimization_events": [
      "ACTIVE",
      "LOGIN",
      "LAUNCH_APP"
    ]
  }
}
```


---

## Sự kiện Pixel (Pixel Events)
<a id="doc-1740857881469954"></a>
<!-- doc_id: 1740857881469954 -->

Nhóm API Sự kiện Pixel (Pixel Events API / Web Events) cho phép bạn báo cáo các hành vi của khách truy cập trên trang web (chẳng hạn như Xem nội dung, Thêm vào giỏ hàng, Hoàn tất đơn hàng) trực tiếp từ máy chủ web về TikTok.

Dữ liệu sự kiện web được sử dụng để:
- Đo lường và báo cáo hiệu quả chiến dịch quảng cáo TikTok.
- Tối ưu hóa thuật toán phân phối theo mục tiêu chuyển đổi (Conversions / ROAS).
- Xây dựng tệp đối tượng tùy chỉnh (Custom Audiences) từ lưu lượng truy cập web để tái tiếp thị (Retargeting) hoặc tìm kiếm khách hàng tương tự (Lookalike).

Các endpoint trong nhóm Pixel Events:
* [Báo cáo sự kiện Web (Report a Web Event)](43-events-1-0-p1.md#doc-1740858531237890)
* [Báo cáo sự kiện Web hàng loạt (Report Web Events in bulk)](43-events-1-0-p1.md#doc-1740858565852225)
* [Lấy danh sách Pixel (Get pixels)](43-events-1-0-p1.md#doc-1740858697598978)
* [Tạo Pixel (Create a pixel)](43-events-1-0-p1.md#doc-1740858779758593)
* [Cập nhật Pixel (Update a pixel)](43-events-1-0-p1.md#doc-1740858799524865)
* [Tạo sự kiện Pixel (Create Pixel Events)](43-events-1-0-p1.md#doc-1740858807646209)
* [Cập nhật sự kiện Pixel (Update a Pixel Event)](43-events-1-0-p1.md#doc-1740858823774210)
* [Xóa sự kiện Pixel (Delete a Pixel Event)](43-events-1-0-p1.md#doc-1740858862104578)
* [Lấy sự kiện Instant Page (Get Instant Page events)](43-events-1-0-p1.md#doc-1740898639412226)
* [Thống kê sự kiện Pixel (Get Pixel Event statistics)](43-events-1-0-p1.md#doc-1740858904557570)

---

## Báo cáo sự kiện Web (Report a Web Event)
<a id="doc-1740858531237890"></a>
<!-- doc_id: 1740858531237890 -->

Sử dụng endpoint này để báo cáo một sự kiện Web đơn lẻ từ máy chủ của bạn lên TikTok.

### Các sự kiện Web được hỗ trợ

Sự kiện web là các hành động mà khách truy cập thực hiện nhằm đạt được mục tiêu kinh doanh trên website. TikTok chia sự kiện web thành hai nhóm:
- **Sự kiện tiêu chuẩn (Standard Events)**: Các hành động có tên định sẵn do TikTok định nghĩa, được hỗ trợ đầy đủ trên tất cả các công cụ phân bổ, tối ưu hóa chuyển đổi và tạo tệp đối tượng. Tên sự kiện có phân biệt chữ hoa chữ thường (case-sensitive).
- **Sự kiện tùy chỉnh (Custom Events)**: Các hành động do nhà quảng cáo tự đặt tên ngoài danh mục tiêu chuẩn. Sự kiện tùy chỉnh chỉ hỗ trợ cho mục đích báo cáo và tạo tệp đối tượng (chưa hỗ trợ tối ưu hóa giá thầu chuyển đổi).

Bảng 18 sự kiện Web tiêu chuẩn của TikTok:

| Event | Event Type in Events Manager | Description | Recommended fields in properties object |
|---|---|---|---|
| `ViewContent` | View Content | Khi người dùng xem một trang chi tiết nội dung/sản phẩm. | `content_type`, `quantity`, `description`, `content_id`, `currency`, `value` |
| `Search` | Search | Khi người dùng thực hiện tìm kiếm trên website. | `query` |
| `AddToWishlist` | Add to Wishlist | Khi người dùng thêm sản phẩm vào danh sách yêu thích. | `content_id`, `content_type`, `currency`, `value` |
| `AddToCart` | Add to Cart | Khi người dùng thêm sản phẩm vào giỏ hàng. | `content_type`, `quantity`, `description`, `content_id`, `currency`, `value` |
| `ApplicationApproval` | Application Approval | Khi đơn xin duyệt/hồ sơ đăng ký được phê duyệt. | `currency`, `value` |
| `InitiateCheckout` | Initiate Checkout | Khi người dùng bắt đầu quy trình thanh toán (checkout). | `content_type`, `quantity`, `content_id`, `currency`, `value` |
| `AddPaymentInfo` | Add Payment Info | Khi người dùng thêm thông tin thanh toán trong luồng thanh toán. | `currency`, `value` |
| `Purchase` | Purchase | Khi giao dịch mua hàng hoặc thanh toán hoàn tất thành công. | `content_type`, `quantity`, `description`, `content_id`, `currency`, `value` |
| `Contact` | Contact | Khi người dùng liên hệ hoặc yêu cầu tư vấn. | |
| `Download` | Download | Khi người dùng nhấp nút để tải tệp hoặc ứng dụng. | |
| `Lead` | Submit Form | Khi người dùng gửi biểu mẫu thông tin khách hàng tiềm năng. | `currency`, `value` |
| `CompleteRegistration` | Complete Registration | Khi người dùng hoàn tất đăng ký tài khoản. | |
| `StartTrial` | Start Trial | Khi người dùng bắt đầu dùng thử miễn phí sản phẩm hoặc dịch vụ. | `currency`, `value` |
| `SubmitApplication` | Submit Application | Khi người dùng nộp đơn đăng ký (ví dụ: hồ sơ vay, tuyển dụng). | |
| `Subscribe` | Subscribe | Khi người dùng đăng ký gói dịch vụ trả phí định kỳ. | `currency`, `value` |
| `CustomizeProduct` | Customize Product | Khi người dùng tùy chỉnh thông số cấu hình của sản phẩm. | `content_id`, `content_type` |
| `FindLocation` | Find Location | Khi người dùng tìm kiếm địa điểm chi nhánh hoặc cửa hàng thực tế. | |
| `Schedule` | Schedule | Khi người dùng đặt lịch hẹn trao đổi với doanh nghiệp. | |

### Yêu cầu (Request)

**Endpoint:** `https://business-api.tiktok.com/open_api/v1.3/pixel/track/`  
**Phương thức (Method):** `POST`

#### Header

| Field | Data Type | Description |
|---|---|---|
| `Access-Token` **(Bắt buộc)** | string | Mã token truy cập được cấp quyền. Xem thêm [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| `Content-Type` **(Bắt buộc)** | string | Định dạng nội dung yêu cầu. Giá trị: `"application/json"`. |

#### Tham số (Parameters)

| Field | Data Type | Description |
|---|---|---|
| `pixel_code` **(Bắt buộc)** | string | Mã định danh Pixel ID lấy trong Trình quản lý sự kiện (Events Manager). |
| `event` **(Bắt buộc)** | string | Tên sự kiện chuyển đổi (Sự kiện tiêu chuẩn như `ViewContent`, `AddToCart`, `Purchase` hoặc tên sự kiện tùy chỉnh). |
| `event_id` | string | Mã định danh duy nhất của sự kiện (UUID hoặc chuỗi băm) phục vụ loại trừ trùng lặp (deduplication) khi báo cáo đồng thời qua Pixel SDK và Server-side API. |
| `timestamp` | string | Dấu thời gian diễn ra sự kiện theo định dạng ISO 8601 (ví dụ: `2023-05-20T12:00:00Z`). |
| `context` **(Bắt buộc)** | object | Thông tin khách hàng, phiên duyệt web và dữ liệu nhấp chuột quảng cáo phục vụ phân bổ. |
| `properties` | object | Các thuộc tính chi tiết về giao dịch, sản phẩm, doanh thu và tiền tệ. |

#### Đối tượng Context (`context`)

| Field | Data Type | Description |
|---|---|---|
| `context` | object | Đối tượng chứa toàn bộ thông tin nhận diện người dùng và phiên truy cập. |
| `↳ ad` | object | Dữ liệu quảng cáo phục vụ phân bổ. |
| `↳↳ callback` | string | TikTok Click ID (`ttclid`) thu thập được từ URL khi người dùng nhấp vào quảng cáo TikTok. |
| `↳ page` | object | Thông tin trang web nơi sự kiện diễn ra. |
| `↳↳ url` | string | URL của trang web tại thời điểm phát sinh sự kiện. Ví dụ: `"https://example.com/products/item1"`. |
| `↳↳ referrer` | string | URL của trang giới thiệu trước đó (referrer). |
| `↳ user` | object | Dữ liệu định danh cá nhân của khách hàng. |
| `↳↳ external_id` | string | ID khách hàng ngoại bộ trong hệ thống của nhà quảng cáo (Customer ID, Loyalty ID), băm SHA-256. |
| `↳↳ email` | string | Địa chỉ email của khách hàng, bắt buộc chuẩn hóa viết thường và băm SHA-256. |
| `↳↳ phone_number` | string | Số điện thoại khách hàng theo chuẩn quốc tế E.164, bắt buộc băm SHA-256. |
| `↳↳ ttp` | string | TikTok Cookie ID (`_ttp`) được lưu trong cookie trình duyệt của người dùng. |
| `↳ ip` | string | Địa chỉ IP công khai (IPv4 hoặc IPv6 không băm) của trình duyệt người dùng. |
| `↳ user_agent` | string | Chuỗi User Agent gốc (không băm) từ trình duyệt thiết bị của người dùng. |

#### Đối tượng Properties (`properties`)

| Field | Data Type | Description |
|---|---|---|
| `properties` | object | Các thuộc tính chi tiết đính kèm sự kiện theo định dạng JSON. |
| `↳ content_type` | string | Loại nội dung được đo lường: `product` hoặc `product_group`. |
| `↳ contents` | object[] | Danh sách các đối tượng đại diện cho sản phẩm liên quan trong sự kiện. |
| `↳↳ price` | double | Đơn giá của từng mặt hàng đơn lẻ. |
| `↳↳ quantity` | number | Số lượng của mặt hàng. |
| `↳↳ content_id` | string | Mã định danh duy nhất của sản phẩm (SKU ID hoặc Product ID). |
| `↳↳ content_category` | string | Danh mục sản phẩm hoặc danh mục trang. |
| `↳↳ content_name` | string | Tên hiển thị của sản phẩm hoặc trang. |
| `↳↳ brand` | string | Tên thương hiệu của sản phẩm. |
| `↳ currency` | string | Mã tiền tệ theo tiêu chuẩn ISO 4217 (ví dụ: `USD`, `VND`, `EUR`, `JPY`). |
| `↳ value` | double | Tổng giá trị đơn hàng hoặc tổng số tiền giao dịch của sự kiện. Bắt buộc để đo lường ROAS. |
| `↳ query` | string | Từ khóa tìm kiếm do người dùng nhập trên website. |
| `↳ description` | string | Mô tả chi tiết về sản phẩm hoặc trang web. |
| `↳ status` | string | Trạng thái của đơn hàng, mặt hàng hoặc dịch vụ. |

#### Ví dụ gọi API

##### cURL

```bash
curl -X POST 'https://business-api.tiktok.com/open_api/v1.3/pixel/track/' \
  -H 'Access-Token: YOUR_ACCESS_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{
    "pixel_code": "C1234567890ABCDEF",
    "event": "Purchase",
    "event_id": "order_uuid_987654321",
    "timestamp": "2023-05-20T12:00:00Z",
    "context": {
      "ad": {
        "callback": "123456789"
      },
      "page": {
        "url": "https://example.com/checkout/success",
        "referrer": "https://example.com/cart"
      },
      "user": {
        "email": "f660ab912ec121d1b1e928a0bb4bc61b15f5ad44d5efdc4e1c92a25e99b8e44a",
        "ttp": "ab12cd34ef56"
      },
      "ip": "203.0.113.195",
      "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
    },
    "properties": {
      "content_type": "product",
      "currency": "USD",
      "value": 99.98,
      "contents": [
        {
          "content_id": "SKU_001",
          "content_name": "Wireless Headphones",
          "price": 49.99,
          "quantity": 2
        }
      ]
    }
  }'
```

##### Python (requests)

```python
import requests

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
PIXEL_CODE = "C1234567890ABCDEF"
url = "https://business-api.tiktok.com/open_api/v1.3/pixel/track/"

headers = {
    "Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}

payload = {
    "pixel_code": PIXEL_CODE,
    "event": "Purchase",
    "event_id": "order_uuid_987654321",
    "timestamp": "2023-05-20T12:00:00Z",
    "context": {
        "ad": {
            "callback": "123456789"
        },
        "page": {
            "url": "https://example.com/checkout/success",
            "referrer": "https://example.com/cart"
        },
        "user": {
            "email": "f660ab912ec121d1b1e928a0bb4bc61b15f5ad44d5efdc4e1c92a25e99b8e44a",
            "ttp": "ab12cd34ef56"
        },
        "ip": "203.0.113.195",
        "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
    },
    "properties": {
        "content_type": "product",
        "currency": "USD",
        "value": 99.98,
        "contents": [
            {
                "content_id": "SKU_001",
                "content_name": "Wireless Headphones",
                "price": 49.99,
                "quantity": 2
            }
        ]
    }
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
| `request_id` | string | Chuỗi log id duy nhất xác định yêu cầu. |
| `data` | object | Thông tin chi tiết về lỗi nếu có. |

#### Ví dụ phản hồi thành công

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "2023052210032301011023224213562",
  "data": {}
}
```

---

## Báo cáo sự kiện Web hàng loạt (Report Web Events in bulk)
<a id="doc-1740859565852225"></a>
<!-- doc_id: 1740859565852225 -->

> **Đính chính marker:**
<a id="doc-1740858565852225"></a>
<!-- doc_id: 1740858565852225 -->

Sử dụng endpoint này để báo cáo sự kiện Web hàng loạt (batch) nhằm giảm tải lưu lượng mạng và số lượng yêu cầu gọi đến TikTok for Business API. Bạn có thể gửi tối đa **1.000 sự kiện** trong một yêu cầu duy nhất. Nếu vượt quá 1.000 sự kiện, toàn bộ yêu cầu sẽ bị từ chối.

### Yêu cầu (Request)

**Endpoint:** `https://business-api.tiktok.com/open_api/v1.3/pixel/batch/`  
**Phương thức (Method):** `POST`

#### Header

| Field | Data Type | Description |
|---|---|---|
| `Access-Token` **(Bắt buộc)** | string | Mã token truy cập được cấp quyền. Xem thêm [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| `Content-Type` **(Bắt buộc)** | string | Định dạng nội dung yêu cầu. Giá trị: `"application/json"`. |

#### Tham số (Parameters)

| Field | Data Type | Description |
|---|---|---|
| `pixel_code` **(Bắt buộc)** | string | Mã định danh Pixel ID trong Trình quản lý sự kiện. |
| `batch` | object[] | Mảng chứa danh sách các sự kiện web cần gửi theo đợt (tối đa 1.000 sự kiện). |
| `↳ type` | string | Loại thao tác sự kiện. Hiện tại chỉ chấp nhận giá trị `track`. |
| `↳ event` | string | Tên sự kiện chuyển đổi (Sự kiện tiêu chuẩn hoặc tùy chỉnh). |
| `↳ event_id` | string | Mã định danh duy nhất của từng sự kiện để loại trừ trùng lặp (deduplication). |
| `↳ timestamp` | string | Dấu thời gian diễn ra sự kiện theo định dạng ISO 8601. |
| `↳ context` | object | Thông tin khách hàng, phiên duyệt web và dữ liệu nhấp chuột quảng cáo. |
| `↳ properties` | object | Các thuộc tính chi tiết về giao dịch, sản phẩm, doanh thu và tiền tệ. |

#### Đối tượng Context trong Batch (`context`)

| Field | Data Type | Description |
|---|---|---|
| `context` | object | Chứa toàn bộ thông tin tham số khách hàng. |
| `↳ ad` | object | Dữ liệu quảng cáo phục vụ phân bổ. |
| `↳↳ callback` | string | TikTok Click ID (`ttclid`). |
| `↳ page` | object | Thông tin trang web. |
| `↳↳ url` | string | URL trang web khi sự kiện diễn ra. |
| `↳↳ referrer` | string | URL trang web giới thiệu. |
| `↳ user` | object | Thông tin định danh cá nhân của người dùng. |
| `↳↳ external_id` | string | ID người dùng ngoại bộ, băm SHA-256. |
| `↳↳ email` | string | Email khách hàng, băm SHA-256. |
| `↳↳ phone_number` | string | Số điện thoại khách hàng, băm SHA-256. |
| `↳↳ ttp` | string | Cookie ID `_ttp` của trình duyệt. |
| `↳ ip` | string | Địa chỉ IP trình duyệt không băm. |
| `↳ user_agent` | string | User agent của thiết bị không băm. |

#### Đối tượng Properties trong Batch (`properties`)

| Field | Data Type | Description |
|---|---|---|
| `properties` | object | Các thuộc tính chi tiết đính kèm sự kiện. |
| `↳ content_type` | string | Loại nội dung (`product` hoặc `product_group`). |
| `↳ contents` | object[] | Danh sách sản phẩm liên quan trong sự kiện. |
| `↳↳ price` | double | Đơn giá của từng mặt hàng. |
| `↳↳ quantity` | number | Số lượng của từng mặt hàng. |
| `↳↳ content_id` | string | Mã định danh duy nhất của sản phẩm (SKU). |
| `↳↳ content_category` | string | Danh mục sản phẩm hoặc trang. |
| `↳↳ content_name` | string | Tên sản phẩm hoặc trang. |
| `↳↳ brand` | string | Tên thương hiệu của sản phẩm. |
| `↳ currency` | string | Mã tiền tệ ISO 4217 (ví dụ: `USD`, `VND`). |
| `↳ value` | double | Tổng giá trị đơn hàng hoặc giao dịch. Bắt buộc đối với ROAS. |
| `↳ query` | string | Chuỗi tìm kiếm do người dùng nhập. |
| `↳ description` | string | Mô tả sản phẩm hoặc trang. |
| `↳ status` | string | Trạng thái đơn hàng hoặc mặt hàng. |

#### Ví dụ gọi API

##### cURL

```bash
curl -X POST 'https://business-api.tiktok.com/open_api/v1.3/pixel/batch/' \
  -H 'Access-Token: YOUR_ACCESS_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{
    "pixel_code": "C1234567890ABCDEF",
    "batch": [
      {
        "type": "track",
        "event": "ViewContent",
        "event_id": "view_event_001",
        "timestamp": "2023-05-20T12:00:00Z",
        "context": {
          "page": {
            "url": "https://example.com/products/item1"
          },
          "ip": "203.0.113.195",
          "user_agent": "Mozilla/5.0"
        }
      },
      {
        "type": "track",
        "event": "Purchase",
        "event_id": "purchase_event_002",
        "timestamp": "2023-05-20T12:05:00Z",
        "context": {
          "user": {
            "email": "f660ab912ec121d1b1e928a0bb4bc61b15f5ad44d5efdc4e1c92a25e99b8e44a"
          },
          "ip": "203.0.113.195",
          "user_agent": "Mozilla/5.0"
        },
        "properties": {
          "currency": "USD",
          "value": 49.99
        }
      }
    ]
  }'
```

##### Python (requests)

```python
import requests

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
PIXEL_CODE = "C1234567890ABCDEF"
url = "https://business-api.tiktok.com/open_api/v1.3/pixel/batch/"

headers = {
    "Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}

payload = {
    "pixel_code": PIXEL_CODE,
    "batch": [
        {
            "type": "track",
            "event": "ViewContent",
            "event_id": "view_event_001",
            "timestamp": "2023-05-20T12:00:00Z",
            "context": {
                "page": {
                    "url": "https://example.com/products/item1"
                },
                "ip": "203.0.113.195",
                "user_agent": "Mozilla/5.0"
            }
        },
        {
            "type": "track",
            "event": "Purchase",
            "event_id": "purchase_event_002",
            "timestamp": "2023-05-20T12:05:00Z",
            "context": {
                "user": {
                    "email": "f660ab912ec121d1b1e928a0bb4bc61b15f5ad44d5efdc4e1c92a25e99b8e44a"
                },
                "ip": "203.0.113.195",
                "user_agent": "Mozilla/5.0"
            },
            "properties": {
                "currency": "USD",
                "value": 49.99
            }
        }
    ]
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
| `request_id` | string | Chuỗi log id duy nhất xác định yêu cầu. |
| `data` | object | Dữ liệu phản hồi chi tiết lỗi nếu có. |
| `↳ partial_failure` | boolean | Cho biết việc báo cáo sự kiện có bị thất bại một phần hay không. |
| `↳ failed_events` | object[] | Danh sách chi tiết các sự kiện bị lỗi trong trường hợp thất bại một phần. |
| `↳↳ order_in_batch` | number | Thứ tự vị trí của sự kiện bị lỗi trong mảng `batch` gửi lên. |
| `↳↳ error` | string | Thông điệp mô tả chi tiết lỗi phát sinh đối với sự kiện. |

#### Ví dụ phản hồi thành công

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "2023052210032301011023224213562",
  "data": {
    "partial_failure": false,
    "failed_events": []
  }
}
```


---

## Lấy danh sách Pixel (Get pixels)
<a id="doc-1740858697598978"></a>
<!-- doc_id: 1740858697598978 -->

Sử dụng endpoint này để lấy danh sách thông tin Pixel đã tạo trong tài khoản quảng cáo. Danh sách trả về bao gồm thông tin cấu hình và danh sách sự kiện Pixel (`Pixel Event`).

### Yêu cầu (Request)

**Endpoint:** `https://business-api.tiktok.com/open_api/v1.3/pixel/list/`  
**Phương thức (Method):** `GET`

#### Header

| Field | Data Type | Description |
|---|---|---|
| `Access-Token` **(Bắt buộc)** | string | Mã token truy cập được cấp quyền. Xem thêm [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

#### Tham số (Parameters)

| Field | Data Type | Description |
|---|---|---|
| `advertiser_id` **(Bắt buộc)** | string | ID của nhà quảng cáo. |
| `code` | string | Mã Pixel Code để lọc kết quả. |
| `pixel_id` | string | ID Pixel để lọc kết quả. |
| `name` | string | Tên Pixel (hỗ trợ tìm kiếm khớp mờ). |
| `filtering` | object | Bộ lọc nâng cao theo định dạng JSON. Hỗ trợ lọc theo `asset_ownership`, `owner_bc_id`, `order_by`, `pixel_category`, `asset_relation_status`, `pixel_setup_mode`. |
| `order_by` | string | Thứ tự sắp xếp kết quả trả về. |
| `page` | number | Số trang kết quả (mặc định: 1). |
| `page_size` | number | Kích thước trang kết quả (mặc định: 10, tối đa: 50). |

#### Ví dụ gọi API

##### cURL

```bash
curl -X GET 'https://business-api.tiktok.com/open_api/v1.3/pixel/list/?advertiser_id=7123456789012345678&page=1&page_size=10' \
  -H 'Access-Token: YOUR_ACCESS_TOKEN'
```

##### Python (requests)

```python
import requests

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ADVERTISER_ID = "7123456789012345678"
url = "https://business-api.tiktok.com/open_api/v1.3/pixel/list/"

headers = {
    "Access-Token": ACCESS_TOKEN
}

params = {
    "advertiser_id": ADVERTISER_ID,
    "page": 1,
    "page_size": 10
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
| `request_id` | string | Chuỗi log id duy nhất xác định yêu cầu. |
| `data` | object | Dữ liệu trả về. |
| `↳ pixels` | object[] | Danh sách các Pixel thuộc tài khoản. |
| `↳↳ pixel_id` | string | ID duy nhất của Pixel. |
| `↳↳ pixel_name` | string | Tên của Pixel. |
| `↳↳ pixel_code` | string | Mã định danh Pixel Code. |
| `↳↳ create_time` | string | Thời điểm tạo Pixel. |
| `↳↳ pixel_script` | string | Đoạn mã JavaScript của Pixel để chèn vào website. |
| `↳↳ pixel_category` | string | Danh mục của Pixel (ví dụ: `ECOMMERCE`, `LEADS`). |
| `↳↳ advanced_matching_fields` | object | Các trường so khớp nâng cao thủ công (`email`, `phone_number`, `external_id`, `address`). |
| `↳↳ automatic_advanced_matching_fields` | object | Các trường so khớp nâng cao tự động. |
| `↳↳ enable_first_party_cookies` | boolean | Cho biết cookie bên thứ nhất (First-party cookies) có được bật hay không. |
| `↳↳ enable_expanded_data_sharing` | boolean | Cho biết tính năng chia sẻ dữ liệu mở rộng có được bật hay không. |
| `↳↳ owner_bc_id` | string | ID Business Center sở hữu Pixel. |
| `↳↳ asset_ownership` | string | Quyền sở hữu tài sản Pixel. |
| `↳↳ ownership_status` | string | Trạng thái quyền sở hữu tài sản. |
| `↳↳ asset_relation_status` | string | Trạng thái quan hệ tài sản giữa tài khoản quảng cáo và Pixel. |
| `↳↳ available_for_catalog_only` | boolean | Cho biết Pixel có chỉ dành riêng cho danh mục sản phẩm (Catalog) hay không. |
| `↳↳ pixel_setup_mode` | string | Chế độ cài đặt Pixel (`MANUAL`, `PARTNER`). |
| `↳↳ updated_at` | string | Thời điểm cập nhật Pixel gần nhất. |
| `↳↳ events` | object[] | Danh sách các sự kiện Pixel được định cấu hình. |
| `↳↳↳ event_id` | string | ID sự kiện Pixel. |
| `↳↳↳ event_type` | string | Loại sự kiện Pixel tiêu chuẩn. |
| `↳↳↳ custom_event_type` | string | Tên sự kiện Pixel tùy chỉnh. |
| `↳↳↳ event_code` | string | Mã code sự kiện. |
| `↳↳↳ currency` | string | Đơn vị tiền tệ của sự kiện. |
| `↳↳↳ currency_value` | number | Giá trị chuyển đổi cố định của sự kiện. |
| `↳↳↳ statistic_type` | string | Loại thống kê đo lường (`EVERYTIME` hoặc `NONE`). |
| `↳↳↳ deprecated` | boolean | Cho biết sự kiện có bị xem là lỗi thời hay không. |
| `↳↳↳ rules` | object[] | Quy tắc kích hoạt sự kiện. |
| `↳↳↳↳ variable` | string | Biến kiểm tra điều kiện quy tắc (ví dụ: `PAGE_URL`). |
| `↳↳↳↳ operator` | string | Toán tử so sánh (ví dụ: `CONTAINS`, `EQUALS`). |
| `↳↳↳↳ trigger` | string | Giá trị kích hoạt điều kiện. |
| `↳↳↳ partner_name` | string | Tên đối tác nền tảng (ví dụ: Shopify, WooCommerce). |
| `↳↳↳ optimization_event` | string | Tên sự kiện tối ưu hóa (`optimization_event`) tương ứng dùng khi tạo nhóm quảng cáo qua [/adgroup/create/](07-ad-groups-p2.md#doc-1739499616346114). Xem [Supported Pixel events - Pixel events](../09-marketing-api/do-luong-quang-cao-p2.md#doc-1739585696931842). |
| `↳ page_info` | object | Thông tin phân trang. |
| `↳↳ page` | number | Số trang hiện tại. |
| `↳↳ page_size` | number | Số lượng kết quả trên mỗi trang. |
| `↳↳ total_number` | number | Tổng số lượng Pixel. |
| `↳↳ total_page` | number | Tổng số trang. |

#### Ví dụ phản hồi thành công

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "2023052210032301011023224213562",
  "data": {
    "pixels": [
      {
        "pixel_id": "1765432109876543",
        "pixel_name": "My Shopify Pixel",
        "pixel_code": "C1234567890ABCDEF",
        "create_time": "2023-01-10 08:30:00",
        "pixel_category": "ECOMMERCE",
        "enable_first_party_cookies": true,
        "events": [
          {
            "event_id": "987654321",
            "event_type": "PURCHASE",
            "optimization_event": "PURCHASE",
            "statistic_type": "EVERYTIME"
          }
        ]
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

## Tạo Pixel (Create a pixel)
<a id="doc-1740858779758593"></a>
<!-- doc_id: 1740858779758593 -->

Sử dụng endpoint này để tạo một Pixel mới và lấy mã cài đặt để triển khai lên website. Tham khảo [Installing Pixel](https://ads.tiktok.com/help/article?aid=717665906670358459).

### Yêu cầu (Request)

**Endpoint:** `https://business-api.tiktok.com/open_api/v1.3/pixel/create/`  
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
| `pixel_name` **(Bắt buộc)** | string | Tên của Pixel (khuyến nghị tương ứng với tên miền website, độ dài tối đa 40 ký tự). |
| `pixel_category` | string | Danh mục Pixel (ví dụ: `ECOMMERCE`, `LEADS`). |
| `partner_name` | string | Tên đối tác tích hợp (ví dụ: Shopify, Google Tag Manager). |
| `advanced_matching_fields` | object | Cấu hình các trường so khớp nâng cao thủ công (`email`, `phone_number`, `external_id`, `address`). |
| `automatic_advanced_matching_fields` | object | Cấu hình các trường so khớp nâng cao tự động. |
| `enable_first_party_cookies` | boolean | Cho phép sử dụng cookie bên thứ nhất để cải thiện độ chính xác phân bổ. |
| `enable_expanded_data_sharing` | boolean | Bật tính năng chia sẻ dữ liệu mở rộng. |

#### Ví dụ gọi API

##### cURL

```bash
curl -X POST 'https://business-api.tiktok.com/open_api/v1.3/pixel/create/' \
  -H 'Access-Token: YOUR_ACCESS_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{
    "advertiser_id": "7123456789012345678",
    "pixel_name": "Ecommerce Website Pixel",
    "enable_first_party_cookies": true
  }'
```

##### Python (requests)

```python
import requests

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ADVERTISER_ID = "7123456789012345678"
url = "https://business-api.tiktok.com/open_api/v1.3/pixel/create/"

headers = {
    "Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}

payload = {
    "advertiser_id": ADVERTISER_ID,
    "pixel_name": "Ecommerce Website Pixel",
    "enable_first_party_cookies": True
}

response = requests.post(url, headers=headers, json=payload)
print(response.status_code)
print(response.json())
```

### Phản hồi (Response)

| Field | Data Type | Description |
|---|---|---|
| `code` | number | Mã phản hồi. `0` biểu thị thành công. Các mã khác xem tại [Appendix-Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi từ hệ thống. |
| `request_id` | string | Chuỗi log id duy nhất xác định yêu cầu. |
| `data` | object | Dữ liệu trả về. |
| `↳ pixel_id` | string | ID của Pixel mới được tạo. |
| `↳ pixel_code` | string | Mã Pixel Code để tích hợp vào website. |

#### Ví dụ phản hồi thành công

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "2023052210032301011023224213562",
  "data": {
    "pixel_id": "1765432109876543",
    "pixel_code": "C1234567890ABCDEF"
  }
}
```

---

## Cập nhật Pixel (Update a pixel)
<a id="doc-1740858799524865"></a>
<!-- doc_id: 1740858799524865 -->

Sử dụng endpoint này để cập nhật tên Pixel và cấu hình so khớp nâng cao. Tên Pixel nên tương ứng với tên miền của bạn và không vượt quá 40 ký tự.

### Yêu cầu (Request)

**Endpoint:** `https://business-api.tiktok.com/open_api/v1.3/pixel/update/`  
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
| `pixel_id` **(Bắt buộc)** | string | ID của Pixel cần cập nhật. |
| `pixel_name` | string | Tên mới của Pixel. |
| `advanced_matching_fields` | object | Các trường so khớp nâng cao (`email`, `phone_number`, `external_id`, `address`). |
| `automatic_advanced_matching_fields` | object | Các trường so khớp nâng cao tự động. |
| `enable_first_party_cookies` | boolean | Bật/tắt cookie bên thứ nhất. |
| `enable_expanded_data_sharing` | boolean | Bật/tắt chia sẻ dữ liệu mở rộng. |

#### Ví dụ gọi API

##### cURL

```bash
curl -X POST 'https://business-api.tiktok.com/open_api/v1.3/pixel/update/' \
  -H 'Access-Token: YOUR_ACCESS_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{
    "advertiser_id": "7123456789012345678",
    "pixel_id": "1765432109876543",
    "pixel_name": "Updated Ecommerce Pixel",
    "enable_first_party_cookies": true
  }'
```

##### Python (requests)

```python
import requests

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ADVERTISER_ID = "7123456789012345678"
url = "https://business-api.tiktok.com/open_api/v1.3/pixel/update/"

headers = {
    "Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}

payload = {
    "advertiser_id": ADVERTISER_ID,
    "pixel_id": "1765432109876543",
    "pixel_name": "Updated Ecommerce Pixel",
    "enable_first_party_cookies": True
}

response = requests.post(url, headers=headers, json=payload)
print(response.status_code)
print(response.json())
```

### Phản hồi (Response)

| Field | Data Type | Description |
|---|---|---|
| `code` | number | Mã phản hồi. `0` biểu thị thành công. Các mã khác xem tại [Appendix-Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi từ hệ thống. |
| `data` | object | Dữ liệu trả về (đối tượng rỗng `{}` khi thành công). |
| `request_id` | string | Chuỗi log id duy nhất xác định yêu cầu. |

#### Ví dụ phản hồi thành công

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "2023052210032301011023224213562",
  "data": {}
}
```

---

## Tạo sự kiện Pixel (Create Pixel Events)
<a id="doc-1740858807646209"></a>
<!-- doc_id: 1740858807646209 -->

Sử dụng endpoint này để tạo các sự kiện Pixel (Pixel Events). Sự kiện Pixel giúp bạn đo lường các hành động khách hàng thực hiện trên trang web.

### Yêu cầu (Request)

**Endpoint:** `https://business-api.tiktok.com/open_api/v1.3/pixel/event/create/`  
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
| `pixel_id` **(Bắt buộc)** | string | ID của Pixel. |
| `pixel_events` **(Bắt buộc)** | object[] | Danh sách các sự kiện Pixel cần tạo. |
| `↳ event_name` **(Bắt buộc)** | string | Tên sự kiện (ví dụ: `Purchase`, `AddToCart`). |
| `↳ event_type` | string | Loại sự kiện (tiêu chuẩn hoặc tùy chỉnh). |
| `↳ currency` | string | Đơn vị tiền tệ mặc định (ví dụ: `USD`, `VND`). |
| `↳ currency_value` | number | Giá trị chuyển đổi mặc định của sự kiện. |
| `↳ statistic_type` | string | Loại thống kê đặt giá thầu (`EVERYTIME` hoặc `NONE`). |
| `↳ rules` | object[] | Các quy tắc điều kiện kích hoạt sự kiện. |
| `↳↳ variable` | string | Biến kiểm tra (ví dụ: `PAGE_URL`). |
| `↳↳ operator` | string | Toán tử so sánh (`CONTAINS`, `EQUALS`). |
| `↳↳ trigger` | string | Giá trị kích hoạt (`trigger` / `Trigger`). |

#### Ví dụ gọi API

##### cURL

```bash
curl -X POST 'https://business-api.tiktok.com/open_api/v1.3/pixel/event/create/' \
  -H 'Access-Token: YOUR_ACCESS_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{
    "advertiser_id": "7123456789012345678",
    "pixel_id": "1765432109876543",
    "pixel_events": [
      {
        "event_name": "Purchase",
        "event_type": "PURCHASE",
        "currency": "USD",
        "currency_value": 50,
        "statistic_type": "EVERYTIME",
        "rules": [
          {
            "variable": "PAGE_URL",
            "operator": "CONTAINS",
            "trigger": "thank-you"
          }
        ]
      }
    ]
  }'
```

##### Python (requests)

```python
import requests

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ADVERTISER_ID = "7123456789012345678"
url = "https://business-api.tiktok.com/open_api/v1.3/pixel/event/create/"

headers = {
    "Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}

payload = {
    "advertiser_id": ADVERTISER_ID,
    "pixel_id": "1765432109876543",
    "pixel_events": [
        {
            "event_name": "Purchase",
            "event_type": "PURCHASE",
            "currency": "USD",
            "currency_value": 50,
            "statistic_type": "EVERYTIME",
            "rules": [
                {
                    "variable": "PAGE_URL",
                    "operator": "CONTAINS",
                    "trigger": "thank-you"
                }
            ]
        }
    ]
}

response = requests.post(url, headers=headers, json=payload)
print(response.status_code)
print(response.json())
```

### Phản hồi (Response)

| Field | Data Type | Description |
|---|---|---|
| `code` | number | Mã phản hồi. `0` biểu thị thành công. Các mã khác xem tại [Appendix-Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi từ hệ thống. |
| `data` | object | Dữ liệu trả về. |
| `↳ event_id` | string | ID của sự kiện Pixel vừa tạo. |
| `↳ event_code` | string | Mã code sự kiện. |
| `request_id` | string | Chuỗi log id duy nhất xác định yêu cầu. |

#### Ví dụ phản hồi thành công

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "2023052210032301011023224213562",
  "data": {
    "event_id": "1765432109876588",
    "event_code": "EVT_PURCHASE_001"
  }
}
```

---

## Cập nhật sự kiện Pixel (Update a Pixel Event)
<a id="doc-1740858823774210"></a>
<!-- doc_id: 1740858823774210 -->

Sử dụng endpoint này để cập nhật tên sự kiện Pixel (`event_name`) và giá trị chuyển đổi (`currency_value`, `currency`).

### Yêu cầu (Request)

**Endpoint:** `https://business-api.tiktok.com/open_api/v1.3/pixel/event/update/`  
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
| `event_id` **(Bắt buộc)** | string | ID của sự kiện Pixel cần cập nhật. |
| `event_name` | string | Tên mới của sự kiện Pixel. |
| `currency` | string | Mã tiền tệ ISO 4217 (ví dụ: `USD`, `VND`). |
| `currency_value` | number | Giá trị chuyển đổi mới. |

#### Ví dụ gọi API

##### cURL

```bash
curl -X POST 'https://business-api.tiktok.com/open_api/v1.3/pixel/event/update/' \
  -H 'Access-Token: YOUR_ACCESS_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{
    "advertiser_id": "7123456789012345678",
    "event_id": "1765432109876588",
    "event_name": "Completed Order",
    "currency": "USD",
    "currency_value": 75
  }'
```

##### Python (requests)

```python
import requests

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ADVERTISER_ID = "7123456789012345678"
url = "https://business-api.tiktok.com/open_api/v1.3/pixel/event/update/"

headers = {
    "Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}

payload = {
    "advertiser_id": ADVERTISER_ID,
    "event_id": "1765432109876588",
    "event_name": "Completed Order",
    "currency": "USD",
    "currency_value": 75
}

response = requests.post(url, headers=headers, json=payload)
print(response.status_code)
print(response.json())
```

### Phản hồi (Response)

| Field | Data Type | Description |
|---|---|---|
| `code` | number | Mã phản hồi. `0` biểu thị thành công. Các mã khác xem tại [Appendix-Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi từ hệ thống. |
| `data` | object | Dữ liệu trả về (đối tượng rỗng `{}` khi cập nhật thành công). |
| `request_id` | string | Chuỗi log id duy nhất xác định yêu cầu. |

#### Ví dụ phản hồi thành công

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "2023052210032301011023224213562",
  "data": {}
}
```

---

## Xóa sự kiện Pixel (Delete a Pixel Event)
<a id="doc-1740858862104578"></a>
<!-- doc_id: 1740858862104578 -->

Sử dụng endpoint này để xóa một sự kiện Pixel khỏi cấu hình.

> **Lưu ý:** Không thể xóa sự kiện Pixel đang được liên kết với nhóm quảng cáo đang hoạt động.

### Yêu cầu (Request)

**Endpoint:** `https://business-api.tiktok.com/open_api/v1.3/pixel/event/delete/`  
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
| `event_id` **(Bắt buộc)** | string | ID của sự kiện Pixel cần xóa. |

#### Ví dụ gọi API

##### cURL

```bash
curl -X POST 'https://business-api.tiktok.com/open_api/v1.3/pixel/event/delete/' \
  -H 'Access-Token: YOUR_ACCESS_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{
    "advertiser_id": "7123456789012345678",
    "event_id": "1765432109876588"
  }'
```

##### Python (requests)

```python
import requests

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ADVERTISER_ID = "7123456789012345678"
url = "https://business-api.tiktok.com/open_api/v1.3/pixel/event/delete/"

headers = {
    "Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}

payload = {
    "advertiser_id": ADVERTISER_ID,
    "event_id": "1765432109876588"
}

response = requests.post(url, headers=headers, json=payload)
print(response.status_code)
print(response.json())
```

### Phản hồi (Response)

| Field | Data Type | Description |
|---|---|---|
| `code` | number | Mã phản hồi. `0` biểu thị thành công. Các mã khác xem tại [Appendix-Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi từ hệ thống. |
| `data` | object | Dữ liệu trả về (đối tượng rỗng `{}` khi xóa thành công). |
| `request_id` | string | Chuỗi log id duy nhất xác định yêu cầu. |

#### Ví dụ phản hồi thành công

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "2023052210032301011023224213562",
  "data": {}
}
```

---

## Lấy sự kiện Instant Page (Get Instant Page events)
<a id="doc-1740898639412226"></a>
<!-- doc_id: 1740898639412226 -->

Sử dụng endpoint này để lấy danh sách các sự kiện được hỗ trợ trên Instant Page (Trang tức thì của TikTok) dựa trên loại mục tiêu (`objective_type`) và mục tiêu tối ưu hóa (`optimization_goal`).

### Yêu cầu (Request)

**Endpoint:** `https://business-api.tiktok.com/open_api/v1.3/pixel/instant_page/event/`  
**Phương thức (Method):** `GET`

#### Header

| Field | Data Type | Description |
|---|---|---|
| `Access-Token` **(Bắt buộc)** | string | Mã token truy cập được cấp quyền. Xem thêm [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

#### Tham số (Parameters)

| Field | Data Type | Description |
|---|---|---|
| `advertiser_id` **(Bắt buộc)** | string | ID của nhà quảng cáo. |
| `objective_type` **(Bắt buộc)** | string | Loại mục tiêu chiến dịch quảng cáo (`CONVERSIONS` hoặc `APP_PROMOTION`). |
| `optimization_goal` **(Bắt buộc)** | string | Mục tiêu tối ưu hóa của nhóm quảng cáo. |

#### Ví dụ gọi API

##### cURL

```bash
curl -X GET 'https://business-api.tiktok.com/open_api/v1.3/pixel/instant_page/event/?advertiser_id=7123456789012345678&objective_type=CONVERSIONS&optimization_goal=CLICK' \
  -H 'Access-Token: YOUR_ACCESS_TOKEN'
```

##### Python (requests)

```python
import requests

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ADVERTISER_ID = "7123456789012345678"
url = "https://business-api.tiktok.com/open_api/v1.3/pixel/instant_page/event/"

headers = {
    "Access-Token": ACCESS_TOKEN
}

params = {
    "advertiser_id": ADVERTISER_ID,
    "objective_type": "CONVERSIONS",
    "optimization_goal": "CLICK"
}

response = requests.get(url, headers=headers, params=params)
print(response.status_code)
print(response.json())
```

### Phản hồi (Response)

| Field | Data Type | Description |
|---|---|---|
| `code` | number | Mã phản hồi. `0` biểu thị thành công. Các mã khác xem tại [Appendix-Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi từ hệ thống. |
| `data` | object | Dữ liệu trả về. |
| `↳ instant_page_events` | object[] | Danh sách sự kiện Instant Page được hỗ trợ. |
| `↳↳ list` | object[] | Danh sách các sự kiện chi tiết. |
| `↳↳ optimization_events` | string[] | Tên các sự kiện tối ưu hóa. |
| `↳↳ business_type` | string | Loại hình kinh doanh hỗ trợ. |
| `↳↳ is_retargeting` | boolean | Hỗ trợ đối tượng tiếp thị lại hay không. |
| `↳↳ objective_types` | string[] | Danh sách các loại mục tiêu chiến dịch được áp dụng. |
| `↳↳ optimization_goals` | string[] | Danh sách các mục tiêu tối ưu hóa được áp dụng. |
| `request_id` | string | Chuỗi log id duy nhất xác định yêu cầu. |

#### Ví dụ phản hồi thành công

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "2023052210032301011023224213562",
  "data": {
    "instant_page_events": [
      {
        "optimization_events": [
          "PAGE_VIEW",
          "BUTTON_CLICK"
        ],
        "business_type": "GENERAL",
        "is_retargeting": false
      }
    ]
  }
}
```

---

## Thống kê sự kiện Pixel (Get Pixel Event statistics)
<a id="doc-1740858904557570"></a>
<!-- doc_id: 1740858904557570 -->

Sử dụng endpoint này để xem số liệu thống kê dữ liệu sự kiện theo khoảng thời gian. Kết quả trả về bao gồm số lượng sự kiện phân bổ cho quảng cáo (`attributed_count`), số lượng sự kiện tạo từ bản xem trước (`preview_count`) và tổng số sự kiện nhận từ trình duyệt và máy chủ (`browser_event_total_count`, `server_event_total_count`, `total_count`).

### Yêu cầu (Request)

**Endpoint:** `https://business-api.tiktok.com/open_api/v1.3/pixel/event/stats/`  
**Phương thức (Method):** `GET`

#### Header

| Field | Data Type | Description |
|---|---|---|
| `Access-Token` **(Bắt buộc)** | string | Mã token truy cập được cấp quyền. Xem thêm [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

#### Tham số (Parameters)

| Field | Data Type | Description |
|---|---|---|
| `advertiser_id` **(Bắt buộc)** | string | ID của nhà quảng cáo. |
| `pixel_id` | string | ID của Pixel cần xem thống kê. |
| `pixel_ids` | string[] | Danh sách ID Pixel (dưới dạng mảng JSON mã hóa URL). |
| `date_range` | object | Khoảng thời gian truy vấn theo định dạng JSON. |
| `start_date` | string | Ngày bắt đầu định dạng `YYYY-MM-DD`. |
| `end_date` | string | Ngày kết thúc định dạng `YYYY-MM-DD`. |

#### Ví dụ gọi API

##### cURL

```bash
curl -X GET 'https://business-api.tiktok.com/open_api/v1.3/pixel/event/stats/?advertiser_id=7123456789012345678&pixel_id=1765432109876543&start_date=2023-05-01&end_date=2023-05-20' \
  -H 'Access-Token: YOUR_ACCESS_TOKEN'
```

##### Python (requests)

```python
import requests

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ADVERTISER_ID = "7123456789012345678"
url = "https://business-api.tiktok.com/open_api/v1.3/pixel/event/stats/"

headers = {
    "Access-Token": ACCESS_TOKEN
}

params = {
    "advertiser_id": ADVERTISER_ID,
    "pixel_id": "1765432109876543",
    "start_date": "2023-05-01",
    "end_date": "2023-05-20"
}

response = requests.get(url, headers=headers, params=params)
print(response.status_code)
print(response.json())
```

### Phản hồi (Response)

| Field | Data Type | Description |
|---|---|---|
| `code` | number | Mã phản hồi. `0` biểu thị thành công. Các mã khác xem tại [Appendix-Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi từ hệ thống. |
| `data` | object | Dữ liệu trả về. |
| `↳ statistics` | object[] | Danh sách các đối tượng thống kê sự kiện. |
| `↳↳ list` | object[] | Chi tiết các mục thống kê sự kiện. |
| `↳↳ pixel_id` | string | ID của Pixel. |
| `↳↳ pixel_event_type` | string | Loại sự kiện Pixel tiêu chuẩn. |
| `↳↳ custom_event_type` | string | Tên sự kiện tùy chỉnh. |
| `↳↳ browser_event_total_count` | number | Tổng số sự kiện nhận từ Pixel trên trình duyệt web. |
| `↳↳ server_event_total_count` | number | Tổng số sự kiện nhận qua Events API từ phía máy chủ. |
| `↳↳ total_count` | number | Tổng số sự kiện nhận được từ mọi nguồn. |
| `↳↳ attributed_count` | number | Số lượng sự kiện được phân bổ trực tiếp cho các quảng cáo TikTok. |
| `↳↳ preview_count` | number | Số lượng sự kiện phát sinh từ chế độ xem trước quảng cáo (preview). |
| `request_id` | string | Chuỗi log id duy nhất xác định yêu cầu. |

#### Ví dụ phản hồi thành công

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "2023052210032301011023224213562",
  "data": {
    "statistics": [
      {
        "pixel_id": "1765432109876543",
        "pixel_event_type": "PURCHASE",
        "browser_event_total_count": 3200,
        "server_event_total_count": 2800,
        "total_count": 6000,
        "attributed_count": 450,
        "preview_count": 12
      }
    ]
  }
}
```


---

## Sự kiện ngoại tuyến (Offline Events)
<a id="doc-1758427539356673"></a>
<!-- doc_id: 1758427539356673 -->

Sự kiện ngoại tuyến (Offline Events) cho phép bạn đo lường các hành động ngoại tuyến (mua sắm trực tiếp tại cửa hàng, gọi điện thoại qua tổng đài, ký hợp đồng dịch vụ) từ những khách hàng đã xem hoặc tương tác với quảng cáo TikTok của bạn.

Thông qua việc kết nối dữ liệu ngoại tuyến, hệ thống TikTok có thể:
- Xác định và phân bổ chính xác thời điểm các chuyển đổi ngoại tuyến diễn ra.
- Tối ưu hóa hiệu quả chi phí cho các chiến dịch quảng cáo hướng tới mục tiêu bán hàng tại điểm bán thực tế.
- Tải lên từng sự kiện đơn lẻ hoặc hàng loạt thông qua các bộ sự kiện ngoại tuyến (Offline Event set).

Xem thêm [hướng dẫn tạo và quản lý bộ sự kiện ngoại tuyến](../09-marketing-api/do-luong-quang-cao-p1.md#doc-1758051319816193).

Các endpoint trong nhóm Offline Events:
* [Tạo bộ sự kiện ngoại tuyến (Create an Offline Event set)](43-events-1-0-p1.md#doc-1758427576470529)
* [Cập nhật bộ sự kiện ngoại tuyến (Update an Offline Event set)](43-events-1-0-p1.md#doc-1765596741157889)
* [Xóa bộ sự kiện ngoại tuyến (Delete an Offline Event set)](43-events-1-0-p1.md#doc-1765596790860802)
* [Lấy danh sách các bộ sự kiện ngoại tuyến (Get Offline Event sets)](43-events-1-0-p1.md#doc-1765596808589313)
* [Báo cáo sự kiện ngoại tuyến (Report an Offline Event)](43-events-1-0-p1.md#doc-1758428013689857)
* [Báo cáo sự kiện ngoại tuyến hàng loạt (Report Offline Events in bulk)](43-events-1-0-p1.md#doc-1758428053652482)

---

## Tạo bộ sự kiện ngoại tuyến (Create an Offline Event set)
<a id="doc-1758427576470529"></a>
<!-- doc_id: 1758427576470529 -->

Sử dụng endpoint này để tạo một bộ sự kiện ngoại tuyến (Offline Event set) mới dưới tài khoản nhà quảng cáo.

### Yêu cầu (Request)

**Endpoint:** `https://business-api.tiktok.com/open_api/v1.3/offline/create/`  
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
| `event_set_name` **(Bắt buộc)** | string | Tên của bộ sự kiện ngoại tuyến (độ dài tối đa 128 ký tự). |
| `auto_tracking` | boolean | Bật tính năng theo dõi tự động cho tất cả các chiến dịch đang hoạt động và chiến dịch mới hay không. Mặc định: `false`. |

#### Ví dụ gọi API

##### cURL

```bash
curl -X POST 'https://business-api.tiktok.com/open_api/v1.3/offline/create/' \
  -H 'Access-Token: YOUR_ACCESS_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{
    "advertiser_id": "7123456789012345678",
    "event_set_name": "In-Store Purchases Event Set",
    "auto_tracking": true
  }'
```

##### Python (requests)

```python
import requests

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ADVERTISER_ID = "7123456789012345678"
url = "https://business-api.tiktok.com/open_api/v1.3/offline/create/"

headers = {
    "Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}

payload = {
    "advertiser_id": ADVERTISER_ID,
    "event_set_name": "In-Store Purchases Event Set",
    "auto_tracking": True
}

response = requests.post(url, headers=headers, json=payload)
print(response.status_code)
print(response.json())
```

### Phản hồi (Response)

| Field | Data Type | Description |
|---|---|---|
| `code` | number | Mã phản hồi. `0` biểu thị thành công. Các mã khác xem tại [Appendix-Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi từ hệ thống. |
| `data` | object | Dữ liệu trả về. |
| `↳ event_set_id` | string | ID của bộ sự kiện ngoại tuyến vừa được tạo. |
| `request_id` | string | Chuỗi log id duy nhất xác định yêu cầu. |

#### Ví dụ phản hồi thành công

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "2023052210032301011023224213562",
  "data": {
    "event_set_id": "7057103914977558530"
  }
}
```

---

## Cập nhật bộ sự kiện ngoại tuyến (Update an Offline Event set)
<a id="doc-1765596741157889"></a>
<!-- doc_id: 1765596741157889 -->

Sử dụng endpoint này để cập nhật tên (`event_set_name`) hoặc cài đặt tự động theo dõi (`auto_tracking`) của một bộ sự kiện ngoại tuyến.

### Yêu cầu (Request)

**Endpoint:** `https://business-api.tiktok.com/open_api/v1.3/offline/update/`  
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
| `event_set_id` **(Bắt buộc)** | string | ID của bộ sự kiện ngoại tuyến cần cập nhật. |
| `event_set_name` | string | Tên mới cho bộ sự kiện ngoại tuyến. |
| `auto_tracking` | boolean | Cập nhật trạng thái tự động theo dõi (`true`/`false`). |

#### Ví dụ gọi API

##### cURL

```bash
curl -X POST 'https://business-api.tiktok.com/open_api/v1.3/offline/update/' \
  -H 'Access-Token: YOUR_ACCESS_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{
    "advertiser_id": "7123456789012345678",
    "event_set_id": "7057103914977558530",
    "event_set_name": "Updated Retail Event Set",
    "auto_tracking": true
  }'
```

##### Python (requests)

```python
import requests

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ADVERTISER_ID = "7123456789012345678"
url = "https://business-api.tiktok.com/open_api/v1.3/offline/update/"

headers = {
    "Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}

payload = {
    "advertiser_id": ADVERTISER_ID,
    "event_set_id": "7057103914977558530",
    "event_set_name": "Updated Retail Event Set",
    "auto_tracking": True
}

response = requests.post(url, headers=headers, json=payload)
print(response.status_code)
print(response.json())
```

### Phản hồi (Response)

| Field | Data Type | Description |
|---|---|---|
| `code` | number | Mã phản hồi. `0` biểu thị thành công. Các mã khác xem tại [Appendix-Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi từ hệ thống. |
| `data` | object | Dữ liệu trả về (đối tượng rỗng `{}` khi cập nhật thành công). |
| `request_id` | string | Chuỗi log id duy nhất xác định yêu cầu. |

#### Ví dụ phản hồi thành công

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "2023052210032301011023224213562",
  "data": {}
}
```

---

## Xóa bộ sự kiện ngoại tuyến (Delete an Offline Event set)
<a id="doc-1765596790860802"></a>
<!-- doc_id: 1765596790860802 -->

Sử dụng endpoint này để xóa một bộ sự kiện ngoại tuyến dưới tài khoản nhà quảng cáo.

### Yêu cầu (Request)

**Endpoint:** `https://business-api.tiktok.com/open_api/v1.3/offline/delete/`  
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
| `event_set_id` **(Bắt buộc)** | string | ID của bộ sự kiện ngoại tuyến cần xóa. |

#### Ví dụ gọi API

##### cURL

```bash
curl -X POST 'https://business-api.tiktok.com/open_api/v1.3/offline/delete/' \
  -H 'Access-Token: YOUR_ACCESS_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{
    "advertiser_id": "7123456789012345678",
    "event_set_id": "7057103914977558530"
  }'
```

##### Python (requests)

```python
import requests

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ADVERTISER_ID = "7123456789012345678"
url = "https://business-api.tiktok.com/open_api/v1.3/offline/delete/"

headers = {
    "Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}

payload = {
    "advertiser_id": ADVERTISER_ID,
    "event_set_id": "7057103914977558530"
}

response = requests.post(url, headers=headers, json=payload)
print(response.status_code)
print(response.json())
```

### Phản hồi (Response)

| Field | Data Type | Description |
|---|---|---|
| `code` | number | Mã phản hồi. `0` biểu thị thành công. Các mã khác xem tại [Appendix-Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi từ hệ thống. |
| `data` | object | Dữ liệu trả về (đối tượng rỗng `{}` khi xóa thành công). |
| `request_id` | string | Chuỗi log id duy nhất xác định yêu cầu. |

#### Ví dụ phản hồi thành công

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "2023052210032301011023224213562",
  "data": {}
}
```

---

## Lấy danh sách bộ sự kiện ngoại tuyến (Get Offline Event sets)
<a id="doc-1765596808589313"></a>
<!-- doc_id: 1765596808589313 -->

Sử dụng endpoint này để lấy danh sách các bộ sự kiện ngoại tuyến thuộc tài khoản nhà quảng cáo. Hỗ trợ lọc theo danh sách ID hoặc tên bộ sự kiện.

### Yêu cầu (Request)

**Endpoint:** `https://business-api.tiktok.com/open_api/v1.3/offline/get/`  
**Phương thức (Method):** `GET`

#### Header

| Field | Data Type | Description |
|---|---|---|
| `Access-Token` **(Bắt buộc)** | string | Mã token truy cập được cấp quyền. Xem thêm [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

#### Tham số (Parameters)

| Field | Data Type | Description |
|---|---|---|
| `advertiser_id` **(Bắt buộc)** | string | ID của nhà quảng cáo. |
| `event_set_ids` | string[] | Danh sách ID bộ sự kiện ngoại tuyến để lọc kết quả. Định dạng chuỗi JSON mã hóa URL. |
| `event_set_name` | string | Tên bộ sự kiện ngoại tuyến để lọc. |
| `page` | number | Số trang kết quả (mặc định: 1). |
| `page_size` | number | Kích thước trang (mặc định: 10, tối đa: 50). |

#### Ví dụ gọi API

##### cURL

```bash
curl -X GET 'https://business-api.tiktok.com/open_api/v1.3/offline/get/?advertiser_id=7123456789012345678&page=1&page_size=10' \
  -H 'Access-Token: YOUR_ACCESS_TOKEN'
```

##### Python (requests)

```python
import requests

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ADVERTISER_ID = "7123456789012345678"
url = "https://business-api.tiktok.com/open_api/v1.3/offline/get/"

headers = {
    "Access-Token": ACCESS_TOKEN
}

params = {
    "advertiser_id": ADVERTISER_ID,
    "page": 1,
    "page_size": 10
}

response = requests.get(url, headers=headers, params=params)
print(response.status_code)
print(response.json())
```

### Phản hồi (Response)

| Field | Data Type | Description |
|---|---|---|
| `code` | number | Mã phản hồi. `0` biểu thị thành công. Các mã khác xem tại [Appendix-Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi từ hệ thống. |
| `data` | object | Dữ liệu trả về. |
| `↳ event_sets` | object[] | Danh sách các bộ sự kiện ngoại tuyến. |
| `↳↳ event_set_id` | string | ID bộ sự kiện ngoại tuyến. |
| `↳↳ event_set_name` | string | Tên bộ sự kiện ngoại tuyến. |
| `↳↳ auto_tracking` | boolean | Trạng thái tự động theo dõi. |
| `↳↳ create_time` | string | Thời điểm tạo bộ sự kiện ngoại tuyến. |
| `↳ page_info` | object | Thông tin phân trang. |
| `↳↳ page` | number | Số trang hiện tại. |
| `↳↳ page_size` | number | Số lượng kết quả mỗi trang. |
| `↳↳ total_number` | number | Tổng số lượng bộ sự kiện. |
| `↳↳ total_page` | number | Tổng số trang. |
| `request_id` | string | Chuỗi log id duy nhất xác định yêu cầu. |

#### Ví dụ phản hồi thành công

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "2023052210032301011023224213562",
  "data": {
    "event_sets": [
      {
        "event_set_id": "7057103914977558530",
        "event_set_name": "In-Store Purchases",
        "auto_tracking": true,
        "create_time": "2023-01-15 10:00:00"
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

## Báo cáo một sự kiện ngoại tuyến (Report an Offline Event)
<a id="doc-1758428013689857"></a>
<!-- doc_id: 1758428013689857 -->

Sử dụng endpoint này để báo cáo một sự kiện ngoại tuyến đơn lẻ (ví dụ: khách mua hàng tại cửa hàng bán lẻ, gọi điện đặt dịch vụ) vào bộ sự kiện ngoại tuyến đã tạo.

### Yêu cầu (Request)

**Endpoint:** `https://business-api.tiktok.com/open_api/v1.3/offline/track/`  
**Phương thức (Method):** `POST`

#### Header

| Field | Data Type | Description |
|---|---|---|
| `Access-Token` **(Bắt buộc)** | string | Mã token truy cập được cấp quyền. Xem thêm [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| `Content-Type` **(Bắt buộc)** | string | Định dạng nội dung yêu cầu. Giá trị: `"application/json"`. |

#### Tham số (Parameters)

| Field | Data Type | Description |
|---|---|---|
| `event_set_id` **(Bắt buộc)** | string | ID của bộ sự kiện ngoại tuyến tiếp nhận dữ liệu. |
| `event` **(Bắt buộc)** | string | Tên loại sự kiện ngoại tuyến (ví dụ: `Purchase`, `Contact`, `CompleteRegistration`). |
| `event_id` | string | Giá trị mã định danh duy nhất của từng sự kiện để tránh ghi nhận trùng lặp. |
| `timestamp` **(Bắt buộc)** | datetime | Dấu thời gian phát sinh sự kiện ngoại tuyến theo định dạng ISO 8601 (ví dụ: `2023-05-20T12:00:00Z`). |
| `event_channel` | string | Kênh diễn ra sự kiện ngoại tuyến. Enum: `email`, `website`, `phone`, `crm`, `other`. |
| `context` **(Bắt buộc)** | object | Thông tin ngữ cảnh nhận diện khách hàng và điểm bán. |
| `properties` **(Bắt buộc)** | object | Các thuộc tính chi tiết về giao dịch, sản phẩm, doanh thu và đơn hàng. |

#### Đối tượng Context (`context`)

| Field | Data Type | Description |
|---|---|---|
| `context` **(Bắt buộc)** | object | Từ điển thông tin nhận diện người dùng và vị trí cửa hàng. |
| `user` **(Bắt buộc)** | object | Dữ liệu cá nhân của khách hàng. |
| `↳ phone_numbers` | string[] | Mảng số điện thoại khách hàng (chuẩn hóa E.164, bắt buộc băm SHA-256). |
| `↳ emails` | string[] | Mảng địa chỉ email khách hàng (viết thường, bắt buộc băm SHA-256). |
| `order_id` | string | Mã định danh đơn hàng tại cửa hàng/hệ thống POS. |
| `shop_id` | string | Mã định danh chi nhánh hoặc cửa hàng cụ thể. |

#### Đối tượng Properties (`properties`)

| Field | Data Type | Description |
|---|---|---|
| `properties` **(Bắt buộc)** | object | Chi tiết thông số giao dịch ngoại tuyến. |
| `contents` | object[] | Mảng danh sách các sản phẩm/mặt hàng trong đơn hàng. |
| `↳ content_name` | string | Tên của sản phẩm. |
| `↳ content_type` | string | Loại sản phẩm (`product`). |
| `↳ content_category` | string | Danh mục sản phẩm (ví dụ: `Men's clothing`). |
| `↳ content_id` | string | Mã định danh sản phẩm (SKU). |
| `↳ quantity` | number | Số lượng mua. |
| `↳ price` | number | Đơn giá sản phẩm. |
| `↳ brand` | string | Tên thương hiệu sản phẩm. |
| `currency` {+Conditional} | string | Mã tiền tệ ISO 4217 (bắt buộc khi báo cáo doanh thu). |
| `value` {+Conditional} | number | Tổng doanh thu/giá trị đơn hàng (bắt buộc khi báo cáo doanh thu). |
| `event_channel` | string | Kênh phát sinh sự kiện (`email`, `website`, `phone`, `crm`, `other`). |

#### Ví dụ gọi API

##### cURL

```bash
curl -X POST 'https://business-api.tiktok.com/open_api/v1.3/offline/track/' \
  -H 'Access-Token: YOUR_ACCESS_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{
    "event_set_id": "7057103914977558530",
    "event": "Purchase",
    "event_id": "offline_order_12345",
    "timestamp": "2023-05-20T12:00:00Z",
    "event_channel": "website",
    "context": {
      "user": {
        "emails": [
          "f660ab912ec121d1b1e928a0bb4bc61b15f5ad44d5efdc4e1c92a25e99b8e44a"
        ],
        "phone_numbers": [
          "91e0a2e7c4f4a38b69829f074d081f9a764d8a27299a4fb1d23479be963c6c06"
        ]
      },
      "order_id": "POS_ORD_001",
      "shop_id": "STORE_HANOI_01"
    },
    "properties": {
      "currency": "USD",
      "value": 125.05,
      "event_channel": "website",
      "contents": [
        {
          "content_id": "230222800",
          "content_name": "Leather Shoes",
          "content_type": "product",
          "content_category": "Men Footwear",
          "price": 125.05,
          "quantity": 1
        }
      ]
    }
  }'
```

##### Python (requests)

```python
import requests

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
url = "https://business-api.tiktok.com/open_api/v1.3/offline/track/"

headers = {
    "Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}

payload = {
    "event_set_id": "7057103914977558530",
    "event": "Purchase",
    "event_id": "offline_order_12345",
    "timestamp": "2023-05-20T12:00:00Z",
    "event_channel": "website",
    "context": {
        "user": {
            "emails": [
                "f660ab912ec121d1b1e928a0bb4bc61b15f5ad44d5efdc4e1c92a25e99b8e44a"
            ],
            "phone_numbers": [
                "91e0a2e7c4f4a38b69829f074d081f9a764d8a27299a4fb1d23479be963c6c06"
            ]
        },
        "order_id": "POS_ORD_001",
        "shop_id": "STORE_HANOI_01"
    },
    "properties": {
        "currency": "USD",
        "value": 125.05,
        "event_channel": "website",
        "contents": [
            {
                "content_id": "230222800",
                "content_name": "Leather Shoes",
                "content_type": "product",
                "content_category": "Men Footwear",
                "price": 125.05,
                "quantity": 1
            }
        ]
    }
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
| `request_id` | string | Chuỗi log id duy nhất xác định yêu cầu. |
| `data` | object | Chi tiết lỗi nếu có. |

#### Ví dụ phản hồi thành công

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "2023052210032301011023224213562",
  "data": {}
}
```

---

## Báo cáo sự kiện ngoại tuyến hàng loạt (Report Offline Events in bulk)
<a id="doc-1758428053652482"></a>
<!-- doc_id: 1758428053652482 -->

Sử dụng endpoint này để báo cáo sự kiện ngoại tuyến hàng loạt nhằm giảm tải lưu lượng mạng. Khuyến nghị gửi **không quá 100 sự kiện** trong mỗi yêu cầu với tổng kích thước dữ liệu dưới 10 MB.

### Yêu cầu (Request)

**Endpoint:** `https://business-api.tiktok.com/open_api/v1.3/offline/batch/`  
**Phương thức (Method):** `POST`

#### Header

| Field | Data Type | Description |
|---|---|---|
| `Access-Token` **(Bắt buộc)** | string | Mã token truy cập được cấp quyền. Xem thêm [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| `Content-Type` **(Bắt buộc)** | string | Định dạng nội dung yêu cầu. Giá trị: `"application/json"`. |

#### Tham số (Parameters)

| Field | Data Type | Description |
|---|---|---|
| `event_set_id` **(Bắt buộc)** | string | ID của bộ sự kiện ngoại tuyến tiếp nhận dữ liệu. |
| `batch` | object[] | Mảng chứa danh sách các sự kiện ngoại tuyến cần gửi (khuyến nghị tối đa 100 sự kiện). |
| `↳ event` **(Bắt buộc)** | string | Loại sự kiện ngoại tuyến (ví dụ: `Purchase`). |
| `↳ event_id` | string | Giá trị mã định danh duy nhất của từng sự kiện để loại trừ trùng lặp. |
| `↳ context` **(Bắt buộc)** | object | Thông tin khách hàng và điểm bán. |
| `↳ properties` **(Bắt buộc)** | object | Các thuộc tính chi tiết về giao dịch, đơn hàng và sản phẩm. |
| `↳ timestamp` **(Bắt buộc)** | datetime | Dấu thời gian diễn ra sự kiện theo chuẩn ISO 8601. |

#### Đối tượng Context trong Batch (`context`)

| Field | Data Type | Description |
|---|---|---|
| `user` **(Bắt buộc)** | object | Dữ liệu nhận diện người dùng. |
| `↳ phone_numbers` | string[] | Danh sách số điện thoại băm SHA-256. |
| `↳ emails` | string[] | Danh sách email băm SHA-256. |
| `order_id` | string | Mã định danh đơn hàng tại quầy POS. |
| `shop_id` | string | Mã định danh cửa hàng bán lẻ. |

#### Đối tượng Properties trong Batch (`properties`)

| Field | Data Type | Description |
|---|---|---|
| `contents` | object[] | Danh sách các sản phẩm trong giao dịch. |
| `↳ content_name` | string | Tên sản phẩm. |
| `↳ content_type` | string | Loại sản phẩm (`product`). |
| `↳ content_category` | string | Danh mục sản phẩm. |
| `↳ content_id` | string | Mã sản phẩm (SKU). |
| `↳ quantity` | number | Số lượng. |
| `↳ price` | number | Giá sản phẩm. |
| `↳ brand` | string | Thương hiệu sản phẩm. |
| `currency` {+Conditional} | string | Mã tiền tệ ISO 4217. |
| `value` {+Conditional} | number | Tổng giá trị đơn hàng. |
| `event_channel` | string | Kênh diễn ra sự kiện (`email`, `website`, `phone`, `crm`, `other`). |

#### Ví dụ gọi API

##### cURL

```bash
curl -X POST 'https://business-api.tiktok.com/open_api/v1.3/offline/batch/' \
  -H 'Access-Token: YOUR_ACCESS_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{
    "event_set_id": "7057103914977558530",
    "batch": [
      {
        "event": "Purchase",
        "event_id": "batch_order_001",
        "timestamp": "2023-05-20T12:00:00Z",
        "context": {
          "user": {
            "emails": [
              "f660ab912ec121d1b1e928a0bb4bc61b15f5ad44d5efdc4e1c92a25e99b8e44a"
            ],
            "phone_numbers": [
              "91e0a2e7c4f4a38b69829f074d081f9a764d8a27299a4fb1d23479be963c6c06"
            ]
          },
          "order_id": "POS_001",
          "shop_id": "STORE_01"
        },
        "properties": {
          "currency": "USD",
          "value": 150.0,
          "event_channel": "website",
          "contents": [
            {
              "content_id": "SKU_SHOE_01",
              "content_name": "Running Shoes",
              "content_type": "product",
              "content_category": "Footwear",
              "price": 150.0,
              "quantity": 1
            }
          ]
        }
      }
    ]
  }'
```

##### Python (requests)

```python
import requests

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
url = "https://business-api.tiktok.com/open_api/v1.3/offline/batch/"

headers = {
    "Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}

payload = {
    "event_set_id": "7057103914977558530",
    "batch": [
        {
            "event": "Purchase",
            "event_id": "batch_order_001",
            "timestamp": "2023-05-20T12:00:00Z",
            "context": {
                "user": {
                    "emails": [
                        "f660ab912ec121d1b1e928a0bb4bc61b15f5ad44d5efdc4e1c92a25e99b8e44a"
                    ],
                    "phone_numbers": [
                        "91e0a2e7c4f4a38b69829f074d081f9a764d8a27299a4fb1d23479be963c6c06"
                    ]
                },
                "order_id": "POS_001",
                "shop_id": "STORE_01"
            },
            "properties": {
                "currency": "USD",
                "value": 150.0,
                "event_channel": "website",
                "contents": [
                    {
                        "content_id": "SKU_SHOE_01",
                        "content_name": "Running Shoes",
                        "content_type": "product",
                        "content_category": "Footwear",
                        "price": 150.0,
                        "quantity": 1
                    }
                ]
            }
        }
    ]
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
| `request_id` | string | Chuỗi log id duy nhất xác định yêu cầu. |
| `data` | object | Thông tin lỗi chi tiết nếu có. |

#### Ví dụ phản hồi thành công

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "2023052210032301011023224213562",
  "data": {}
}
```

---

## Sự kiện CRM (CRM Events)
<a id="doc-1780896481480706"></a>
<!-- doc_id: 1780896481480706 -->

Tích hợp CRM (Quản trị quan hệ khách hàng) cho phép chuyển giao trực tiếp khách hàng tiềm năng (Leads) phát sinh từ các mẫu quảng cáo tìm kiếm khách hàng tiềm năng (Lead Generation) trên TikTok về hệ thống CRM của nhà quảng cáo.

Bằng cách postback thông tin chất lượng lead (ví dụ: lead đã liên hệ, lead đủ điều kiện, hợp đồng đã ký kết) qua CRM Events, bạn giúp mô hình tối ưu hóa quảng cáo của TikTok nhận diện chính xác các khách hàng tiềm năng có tỷ lệ chuyển đổi cao hơn nhằm tối đa hóa ROI.

Nhóm API Sự kiện CRM cho phép bạn quản lý các bộ sự kiện CRM trong tài khoản quảng cáo:
- Tạo mới bộ sự kiện CRM ([Create a CRM Event Set](43-events-1-0-p2.md#doc-1861366342223874))
- Lấy danh sách bộ sự kiện CRM ([Get CRM Event Sets](43-events-1-0-p2.md#doc-1780896521680898))
