# Xác thực (Authentication)

Nhóm API Xác thực (Authentication) cho phép bạn khởi tạo, gia hạn và thu hồi access token (mã truy cập) để gọi các endpoint trong TikTok API for Business. Bạn có thể lấy **access token dài hạn** (long-term access token, không có thời hạn hết hạn) khi được ủy quyền từ tài khoản quảng cáo, Business Center hoặc TikTok One Creator Marketplace; hoặc lấy **access token ngắn hạn** (short-term access token, có hiệu lực 1 ngày) khi được ủy quyền từ tài khoản người dùng TikTok. Tài liệu này hướng dẫn chi tiết các endpoint xác thực, cấu trúc request, response và ví dụ triển khai.

## Mục lục các endpoint

| Endpoint | Phương thức | Mục đích |
|---|---|---|
| [/oauth2/access_token/](10-authentication.md#doc-1739965703387137) | `POST` | Lấy access token dài hạn qua JSON (`application/json`) |
| [/oauth/token/](10-authentication.md#doc-1739965703387137) | `POST` | Lấy access token dài hạn qua JSON hoặc `application/x-www-form-urlencoded` |
| [/oauth2/revoke_token/](10-authentication.md#doc-1739965949088770) | `POST` | Thu hồi access token dài hạn |
| [/tt_user/oauth2/token/](10-authentication.md#doc-1833997638479041) | `POST` | Lấy access token ngắn hạn (tài khoản TikTok) |
| [/tt_user/oauth2/refresh_token/](10-authentication.md#doc-1833997679342594) | `POST` | Gia hạn access token ngắn hạn bằng `refresh_token` |
| [/tt_user/oauth2/revoke/](10-authentication.md#doc-1833997665030145) | `POST` | Thu hồi access token ngắn hạn của tài khoản TikTok |

---

## Tổng quan về Xác thực (`Authentication`)
<a id="doc-1739965624038402"></a>
<!-- doc_id: 1739965624038402 -->

> Đường dẫn: API Reference > Authentication

Authentication API cho phép bạn tạo hoặc thu hồi access token dài hạn, đồng thời tạo, gia hạn hoặc thu hồi access token ngắn hạn.

Bạn có thể nhận access token dài hạn sau khi nhận được ủy quyền từ một tài khoản quảng cáo (ad account), tài khoản Business Center (BC), hoặc tài khoản TikTok One Creator Marketplace. Ngược lại, bạn cần nhận ủy quyền từ các tài khoản TikTok (TikTok accounts) để lấy access token ngắn hạn.

Để tìm hiểu về sự khác biệt trong quy trình ủy quyền và xác thực giữa các loại API khác nhau, hãy tham khảo [So sánh quy trình ủy quyền cho các API khác nhau](../04-get-started/bat-dau.md#doc-1781891256601602) và [So sánh quy trình xác thực cho các API khác nhau](../04-get-started/bat-dau.md#doc-1781892384100354).

Nhóm API này bao gồm các endpoint sau:
* [Lấy access token dài hạn (Obtain a long-term access token)](10-authentication.md#doc-1739965703387137)
* [Thu hồi access token dài hạn (Revoke a long-term access token)](10-authentication.md#doc-1739965949088770)
* [Lấy access token ngắn hạn (Obtain a short-term access token)](10-authentication.md#doc-1833997638479041)
* [Gia hạn access token ngắn hạn (Renew a short-term access token)](10-authentication.md#doc-1833997679342594)
* [Thu hồi access token ngắn hạn (Revoke a short-term access token)](10-authentication.md#doc-1833997665030145)

---

## Lấy access token dài hạn (`Obtain a long-term access token`)
<a id="doc-1739965703387137"></a>
<!-- doc_id: 1739965703387137 -->

> Đường dẫn: API Reference > Authentication > Obtain a long-term access token

Sử dụng một trong hai endpoint sau để tạo access token dài hạn: `/oauth2/access_token/` hoặc `/oauth/token/`.

Access token dài hạn (long-term access token) là loại mã truy cập nhận được sau khi tài khoản quảng cáo (ad account), tài khoản Business Center hoặc tài khoản TikTok One Creator Marketplace cấp quyền ủy quyền cho ứng dụng của bạn. Token này không có thời hạn hết hạn. Nếu bạn muốn thu hồi access token dài hạn, hãy sử dụng endpoint [/oauth2/revoke_token/](10-authentication.md#doc-1739965949088770).

> [!NOTE]
> `/oauth2/access_token/` chỉ hỗ trợ `Content-Type` là `application/json`, trong khi `/oauth/token/` hỗ trợ `Content-Type` là `application/json` hoặc `application/x-www-form-urlencoded`.

### 1. Endpoint `/oauth2/access_token/`

`POST` `https://business-api.tiktok.com/open_api/v1.3/oauth2/access_token/`

**Mục đích**: Lấy access token dài hạn không hết hạn cho ứng dụng với định dạng dữ liệu gửi lên là JSON.

#### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Content-Type` | string | Bắt buộc | Loại thông điệp request. Định dạng chấp nhận: `"application/json"`. |

#### Tham số (POST: JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `app_id` | string | Bắt buộc | ID ứng dụng nhà phát triển (developer app) của bạn.<br>Để lấy **App ID**, truy cập [My Apps](https://ads.tiktok.com/marketing_api/apps/) > **App Detail** > **Basic Information**. |
| `secret` | string | Bắt buộc | Secret của ứng dụng nhà phát triển của bạn.<br>Để lấy **Secret**, truy cập [My Apps](https://ads.tiktok.com/marketing_api/apps/) > **App Detail** > **Basic Information**. |
| `auth_code` | string | Bắt buộc | Mã ủy quyền (`auth_code`) được tạo ra từ **Advertiser authorization URL**.<br>Mã này có hiệu lực trong 1 giờ và chỉ có thể sử dụng một lần duy nhất.<br>Để biết cách lấy mã ủy quyền dựa theo loại API bạn dùng, xem hàng "Authorization URL" trong [Comparing authorization for different APIs](../04-get-started/bat-dau.md#doc-1781891256601602). |
| `return_advertiser_ids` | boolean | Không bắt buộc | Có trả về danh sách đầy đủ các tài khoản quảng cáo mà token vừa tạo có quyền truy cập qua trường `advertiser_ids` trong phản hồi hay không.<br>Giá trị hỗ trợ: `true`, `false`.<br>Giá trị mặc định: `true`.<br>**Lưu ý**: Nếu bạn có quyền truy cập vào hàng nghìn tài khoản quảng cáo trở lên, việc đặt trường này thành `false` sẽ giúp tránh nguy cơ timeout khi hệ thống truy xuất toàn bộ danh sách advertiser ID. |

#### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi (Return code). Danh sách đầy đủ xem tại [Return codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi. Chi tiết xem tại [Return codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `request_id` | string | ID duy nhất của request. |
| `data` | object | Dữ liệu trả về. |
| ↳ `access_token` | string | Access token dài hạn dùng để xác minh thẩm quyền truy cập API. |
| ↳ `advertiser_ids` | string[] | Danh sách ID các tài khoản quảng cáo mà token có quyền truy cập.<br>Khi `return_advertiser_ids` được đặt thành `false` trong request, trường này sẽ là mảng rỗng (`[]`). |
| ↳ `scope` | number[] | Phạm vi các quyền được cấp cho access token. |

#### Ví dụ gọi API

```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/oauth2/access_token/' \
--header 'Content-Type: application/json' \
--data '{
    "app_id": "1234567890123456789",
    "secret": "your_app_secret_here",
    "auth_code": "your_auth_code_here"
}'
```

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20231023120000010188059082001",
  "data": {
    "access_token": "act.abc123def456xyz789",
    "advertiser_ids": [
      "7000000000000000001",
      "7000000000000000002"
    ],
    "scope": [1, 2, 3]
  }
}
```

---

### 2. Endpoint `/oauth/token/`

`POST` `https://business-api.tiktok.com/open_api/v1.3/oauth/token/`

**Mục đích**: Lấy access token dài hạn không hết hạn, hỗ trợ cả `Content-Type: application/json` và `Content-Type: application/x-www-form-urlencoded`.

#### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Content-Type` | string | Bắt buộc | Loại thông điệp request. Giá trị hỗ trợ: `"application/json"` hoặc `"application/x-www-form-urlencoded"`. |

#### Tham số (POST: JSON body hoặc Form-urlencoded)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `client_id` | string | Bắt buộc | ID ứng dụng nhà phát triển (developer app) của bạn.<br>Để lấy **App ID**, truy cập [My Apps](https://ads.tiktok.com/marketing_api/apps/) > **App Detail** > **Basic Information**. |
| `client_secret` | string | Bắt buộc | Secret của ứng dụng nhà phát triển của bạn.<br>Để lấy **Secret**, truy cập [My Apps](https://ads.tiktok.com/marketing_api/apps/) > **App Detail** > **Basic Information**. |
| `grant_type` | string | Bắt buộc | Loại cấp quyền (grant type).<br>Giá trị enum: `authorization_code`. |
| `auth_code` | string | Bắt buộc | Mã ủy quyền (`auth_code`) được tạo ra từ **Advertiser authorization URL**.<br>Mã này có hiệu lực trong 1 giờ và chỉ có thể sử dụng một lần duy nhất.<br>Để biết cách lấy mã ủy quyền dựa theo loại API bạn dùng, xem hàng "Authorization URL" trong [Comparing authorization for different APIs](../04-get-started/bat-dau.md#doc-1781891256601602). |
| `return_advertiser_ids` | boolean | Không bắt buộc | Có trả về danh sách đầy đủ các tài khoản quảng cáo mà token vừa tạo có quyền truy cập qua trường `advertiser_ids` trong phản hồi hay không.<br>Giá trị hỗ trợ: `true`, `false`.<br>Giá trị mặc định: `true`. |

#### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Danh sách đầy đủ xem tại [Return codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi. Chi tiết xem tại [Return codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `request_id` | string | ID duy nhất của request. |
| `data` | object | Dữ liệu trả về. |
| ↳ `access_token` | string | Access token dài hạn dùng để xác minh thẩm quyền truy cập API. |
| ↳ `token_type` | string | Loại token.<br>Giá trị enum: `Bearer`. |
| ↳ `advertiser_ids` | string[] | Danh sách ID các tài khoản quảng cáo mà token có quyền truy cập.<br>Khi `return_advertiser_ids` được đặt thành `false` trong request, trường này sẽ là mảng rỗng (`[]`). |
| ↳ `scope` | number[] | Phạm vi các quyền được cấp cho access token. |

#### Ví dụ gọi API

```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/oauth/token/' \
--header 'Content-Type: application/json' \
--data '{
    "client_id": "1234567890123456789",
    "client_secret": "your_app_secret_here",
    "grant_type": "authorization_code",
    "auth_code": "your_auth_code_here"
}'
```

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20231023120000010188059082002",
  "data": {
    "access_token": "act.abc123def456xyz789",
    "token_type": "Bearer",
    "advertiser_ids": [
      "7000000000000000001"
    ],
    "scope": [1, 2, 3]
  }
}
```

---

## Thu hồi access token dài hạn (`Revoke a long-term access token`)
<a id="doc-1739965949088770"></a>
<!-- doc_id: 1739965949088770 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/oauth2/revoke_token/`

**Mục đích**: Thu hồi một access token dài hạn đã cấp. Đây là endpoint mới trong TikTok API for Business v1.3.

Access token dài hạn không tự hết hạn. Khi gọi endpoint này thành công, token sẽ bị vô hiệu hóa hoàn toàn và không thể tiếp tục gọi API.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Bắt buộc | Access token đã được ủy quyền cần thực hiện thao tác. Chi tiết xem tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (POST: JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `app_id` | string | Bắt buộc | ID ứng dụng nhà phát triển của bạn.<br>Để tìm **App ID**, truy cập [My Apps](https://ads.tiktok.com/marketing_api/apps/) > **App Detail** > **Basic Information**. |
| `secret` | string | Bắt buộc | Secret của ứng dụng nhà phát triển của bạn.<br>Để tìm **Secret**, truy cập [My Apps](https://ads.tiktok.com/marketing_api/apps/) > **App Detail** > **Basic Information**. |
| `access_token` | string | Bắt buộc | Access token dài hạn mà bạn muốn thu hồi.<br>Bạn có thể tạo access token mới thông qua [/oauth2/access_token/](10-authentication.md#doc-1739965703387137) hoặc [/oauth/token/](10-authentication.md#doc-1739965703387137). |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Chi tiết xem tại [Return codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi. Chi tiết xem tại [Return codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `request_id` | string | ID duy nhất của request. |
| `data` | object | Dữ liệu trả về (rút gọn). |
| ↳ `advertiser_ids` | string[] | Danh sách ID các tài khoản quảng cáo mà quyền truy cập của token vừa bị thu hồi. |

### Ví dụ gọi API

```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/oauth2/revoke_token/' \
--header 'Access-Token: your_authorized_access_token' \
--header 'Content-Type: application/json' \
--data '{
    "app_id": "1234567890123456789",
    "secret": "your_app_secret_here",
    "access_token": "token_to_revoke_here"
}'
```

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20231023120000010188059082003",
  "data": {
    "advertiser_ids": [
      "7000000000000000001"
    ]
  }
}
```

---

## Lấy access token ngắn hạn (`Obtain a short-term access token`)
<a id="doc-1833997638479041"></a>
<!-- doc_id: 1833997638479041 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/tt_user/oauth2/token/`

**Mục đích**: Lấy access token ngắn hạn sau khi nhận được ủy quyền từ tài khoản TikTok.

Access token ngắn hạn có hiệu lực trong 1 ngày (86.400 giây). Endpoint này cũng trả về `refresh_token` để bạn gia hạn access token khi hết hạn mà không cần người dùng ủy quyền lại.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Content-Type` | string | Bắt buộc | Loại thông điệp request. Định dạng cho phép: `application/json`. |

### Tham số (POST: JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `client_id` | string | Bắt buộc | ID ứng dụng nhà phát triển của bạn.<br>Để tìm **App ID**, truy cập [My Apps](https://ads.tiktok.com/marketing_api/apps/) > **App Detail** > **Basic Information**. |
| `client_secret` | string | Bắt buộc | Secret của ứng dụng nhà phát triển của bạn.<br>Để tìm **Secret**, truy cập [My Apps](https://ads.tiktok.com/marketing_api/apps/) > **App Detail** > **Basic Information**. |
| `auth_code` | string | Bắt buộc | Mã ủy quyền nhận được sau khi tài khoản TikTok hoàn tất ủy quyền.<br>Mã này có hiệu lực trong 10 phút và chỉ dùng được một lần. |
| `grant_type` | string | Bắt buộc | Loại cấp quyền.<br>Giá trị enum: `authorization_code`. |
| `redirect_uri` | string | Bắt buộc | Địa chỉ callback URI đã được cấu hình trong ứng dụng nhà phát triển của bạn tại TikTok Developer Portal. |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Chi tiết xem tại [Return codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi. Chi tiết xem tại [Return codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `request_id` | string | ID duy nhất định danh request. |
| `data` | object | Dữ liệu trả về. |
| ↳ `access_token` | string | Access token ngắn hạn dùng để xác thực quyền hạn. Token hết hạn sau 1 ngày. |
| ↳ `token_type` | string | Loại token.<br>Giá trị enum:<br>• `Bearer`: Bearer token. Bất kỳ ai nắm giữ token đều có thể dùng để truy cập tài nguyên liên kết. |
| ↳ `scope` | string | Phạm vi quyền hạn được cấp cho access token (các quyền phân tách bằng dấu phẩy). |
| ↳ `expires_in` | number | Thời gian còn lại cho đến khi access token hết hạn, tính bằng giây (86400). |
| ↳ `refresh_token` | string | Refresh token dùng để làm mới/gia hạn access token. Có hiệu lực trong 1 năm.<br>**Lưu ý**: Hãy lưu lại giá trị này để dùng khi gia hạn `access_token`. |
| ↳ `refresh_token_expires_in` | number | Thời gian còn lại cho đến khi refresh token hết hạn, tính bằng giây. |
| ↳ `open_id` | string | ID định danh duy nhất của tài khoản TikTok đối với ứng dụng này. |

### Ví dụ gọi API

```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/tt_user/oauth2/token/' \
--header 'Content-Type: application/json' \
--data '{
    "client_id": "1234567890123456789",
    "client_secret": "your_app_secret_here",
    "auth_code": "your_user_auth_code",
    "grant_type": "authorization_code",
    "redirect_uri": "https://example.com/callback"
}'
```

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20231023120000010188059082004",
  "data": {
    "access_token": "act.user_short_term_token_example",
    "expires_in": 86400,
    "open_id": "user_openid_12345",
    "refresh_token": "rft.user_refresh_token_example",
    "refresh_token_expires_in": 31536000,
    "scope": "user.info.basic,video.list",
    "token_type": "Bearer"
  }
}
```

---

## Gia hạn access token ngắn hạn (`Renew a short-term access token`)
<a id="doc-1833997679342594"></a>
<!-- doc_id: 1833997679342594 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/tt_user/oauth2/refresh_token/`

**Mục đích**: Gia hạn một access token ngắn hạn sắp hết hạn hoặc đã hết hạn bằng cách sử dụng `refresh_token`.

Access token ngắn hạn hết hạn sau 1 ngày. Bạn cần sử dụng `refresh_token` hợp lệ (có hiệu lực 1 năm) nhận được từ endpoint cấp token trước đó để lấy `access_token` mới mà không cần yêu cầu người dùng đăng nhập lại.

### Chuẩn bị trước khi gọi
Lấy `refresh_token` từ endpoint [/tt_user/oauth2/token/](10-authentication.md#doc-1833997638479041).

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Content-Type` | string | Bắt buộc | Loại thông điệp request. Định dạng cho phép: `application/json`. |

### Tham số (POST: JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `client_id` | string | Bắt buộc | ID ứng dụng nhà phát triển của bạn.<br>Để tìm **App ID**, truy cập [My Apps](https://ads.tiktok.com/marketing_api/apps/) > **App Detail** > **Basic Information**. |
| `client_secret` | string | Bắt buộc | Secret của ứng dụng nhà phát triển của bạn.<br>Để tìm **Secret**, truy cập [My Apps](https://ads.tiktok.com/marketing_api/apps/) > **App Detail** > **Basic Information**. |
| `grant_type` | string | Bắt buộc | Loại cấp quyền.<br>Giá trị enum: `refresh_token`. |
| `refresh_token` | string | Bắt buộc | Refresh token dùng để làm mới access token, nhận được từ [/tt_user/oauth2/token/](10-authentication.md#doc-1833997638479041). |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Chi tiết xem tại [Return codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi. Chi tiết xem tại [Return codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `request_id` | string | ID duy nhất định danh request. |
| `data` | object | Dữ liệu trả về. |
| ↳ `access_token` | string | Access token ngắn hạn mới dùng để xác thực quyền hạn. Hết hạn sau 1 ngày. |
| ↳ `token_type` | string | Loại token.<br>Giá trị enum:<br>• `Bearer`: Bearer token. |
| ↳ `scope` | string | Phạm vi các quyền được cấp cho access token. |
| ↳ `expires_in` | number | Thời gian còn lại cho đến khi access token mới hết hạn, tính bằng giây (86400). |
| ↳ `refresh_token` | string | Refresh token mới (hoặc được duy trì) dùng để tiếp tục gia hạn lần tiếp theo.<br>**Lưu ý**: Hãy cập nhật và lưu lại giá trị `refresh_token` mới này. |
| ↳ `refresh_token_expires_in` | number | Thời gian còn lại cho đến khi refresh token hết hạn, tính bằng giây. |
| ↳ `open_id` | string | ID duy nhất của tài khoản TikTok đối với ứng dụng này. |

### Ví dụ gọi API

```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/tt_user/oauth2/refresh_token/' \
--header 'Content-Type: application/json' \
--data '{
    "client_id": "1234567890123456789",
    "client_secret": "your_app_secret_here",
    "grant_type": "refresh_token",
    "refresh_token": "your_refresh_token_here"
}'
```

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20231023120000010188059082005",
  "data": {
    "access_token": "act.new_user_short_term_token_example",
    "expires_in": 86400,
    "open_id": "user_openid_12345",
    "refresh_token": "rft.new_refresh_token_example",
    "refresh_token_expires_in": 31536000,
    "scope": "user.info.basic,video.list",
    "token_type": "Bearer"
  }
}
```

---

## Thu hồi access token ngắn hạn (`Revoke a short-term access token`)
<a id="doc-1833997665030145"></a>
<!-- doc_id: 1833997665030145 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/tt_user/oauth2/revoke/`

**Mục đích**: Thu hồi một access token ngắn hạn của tài khoản TikTok.

Sau khi thu hồi thành công, access token hiện tại sẽ mất hiệu lực ngay lập tức. Để tiếp tục gọi API, bạn cần tạo access token mới qua endpoint [/tt_user/oauth2/token/](10-authentication.md#doc-1833997638479041) hoặc gia hạn qua [/tt_user/oauth2/refresh_token/](10-authentication.md#doc-1833997679342594) nếu `refresh_token` còn hợp lệ.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Content-Type` | string | Bắt buộc | Loại thông điệp request. Định dạng cho phép: `application/json`. |

### Tham số (POST: JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `client_id` | string | Bắt buộc | ID ứng dụng nhà phát triển của bạn.<br>Để tìm **App ID**, truy cập [My Apps](https://ads.tiktok.com/marketing_api/apps/) > **App Detail** > **Basic Information**. |
| `client_secret` | string | Bắt buộc | Secret của ứng dụng nhà phát triển của bạn.<br>Để tìm **Secret**, truy cập [My Apps](https://ads.tiktok.com/marketing_api/apps/) > **App Detail** > **Basic Information**. |
| `access_token` | string | Bắt buộc | Access token của tài khoản TikTok mà bạn muốn thu hồi.<br>Bạn có thể tạo access token mới qua [/tt_user/oauth2/token/](10-authentication.md#doc-1833997638479041) hoặc lấy lại qua [/tt_user/oauth2/refresh_token/](10-authentication.md#doc-1833997679342594). |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Chi tiết xem tại [Return codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi. Chi tiết xem tại [Return codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `request_id` | string | ID duy nhất định danh request. |
| `data` | object | Dữ liệu trả về (rỗng `{}`). |

### Ví dụ gọi API

```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/tt_user/oauth2/revoke/' \
--header 'Content-Type: application/json' \
--data '{
    "client_id": "1234567890123456789",
    "client_secret": "your_app_secret_here",
    "access_token": "token_to_revoke_here"
}'
```

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20231023120000010188059082006",
  "data": {}
}
```
