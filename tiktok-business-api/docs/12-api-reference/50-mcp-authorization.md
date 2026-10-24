# Ủy quyền MCP (MCP Authorization)
<a id="doc-1873496702070273"></a>
<!-- doc_id: 1873496702070273 -->

Giao thức Model Context Protocol (MCP) là một tiêu chuẩn mở cho phép bạn thiết lập các kết nối hai chiều an toàn giữa các ứng dụng trí tuệ nhân tạo (AI applications / agents) và các nguồn dữ liệu của TikTok for Business. Bộ API Ủy quyền MCP (MCP Authorization API) cho phép bạn kết nối một AI agent tùy chỉnh (custom agent) trực tiếp với máy chủ TikTok for Business MCP Server.

Để tìm hiểu chi tiết về cách thiết lập kết nối và triển khai toàn diện, xem thêm [Cách kết nối agent tùy chỉnh với TikTok for Business MCP Server](../05-mcp-server/mcp-server-tom-tat.md#doc-1873497625216513).

Nhóm API này bao gồm các endpoint sau:
- [Lấy siêu dữ liệu máy chủ ủy quyền](50-mcp-authorization.md#doc-1873496729194769)
- [Khám phá máy chủ ủy quyền](50-mcp-authorization.md#doc-1873496742612993)
- [Đăng ký ứng dụng client](50-mcp-authorization.md#doc-1873496757798466)
- [Yêu cầu ủy quyền từ người dùng](50-mcp-authorization.md#doc-1873496771526337)
- [Đổi mã ủy quyền MCP lấy token](50-mcp-authorization.md#doc-1873496785750401)
- [Làm mới access token MCP](50-mcp-authorization.md#doc-1873496870932225)
- [Thu hồi token MCP](50-mcp-authorization.md#doc-1873496798816274)
- [Sử dụng công cụ MCP](50-mcp-authorization.md#doc-1873496895169554)

---

## Lấy siêu dữ liệu máy chủ ủy quyền (`Get authorization server metadata`)
<a id="doc-1873496729194769"></a>
<!-- doc_id: 1873496729194769 -->

`GET` `https://business-api.tiktok.com/open_mcp/{server}/oauth/.well-known/openid-configuration/`

**Mục đích**: Sử dụng endpoint này để truy xuất siêu dữ liệu cấu hình OAuth của máy chủ ủy quyền TikTok for Business MCP, bao gồm các URL endpoint và các năng lực được hỗ trợ.

Việc truy xuất dữ liệu này giúp ứng dụng client của bạn tự động thích ứng với các thay đổi endpoint thay vì gắn cứng (hardcode) các URL trong mã nguồn.

### Tham số đường dẫn (Path parameters)

| Field | Data Type | Description |
|---|---|---|
| server | string | Bắt buộc. URL đường dẫn máy chủ TikTok for Business MCP cụ thể. Các giá trị enum: `tt-ads-mcp-flat`, `tt-ads-mcp-layer`. Xem thêm tại [Chọn URL máy chủ của bạn](https://business-api.tiktok.com/portal/docs/how-to-connect-a-custom-agent-to-tiktok-for-business-mcp-server/v1.3#anchor-3). |

### Ví dụ

#### cURL
```bash
curl --location --request GET 'https://business-api.tiktok.com/open_mcp/tt-ads-mcp-layer/oauth/.well-known/openid-configuration'
```

#### Python
```python
import requests

SERVER = "tt-ads-mcp-layer"
url = f"https://business-api.tiktok.com/open_mcp/{SERVER}/oauth/.well-known/openid-configuration"

response = requests.get(url)
metadata = response.json()
print("Authorization Endpoint:", metadata.get("authorization_endpoint"))
print("Token Endpoint:", metadata.get("token_endpoint"))
```

### Phản hồi

| Field | Data Type | Description |
|---|---|---|
| issuer | string | URL của đơn vị phát hành (issuer URL) của máy chủ ủy quyền. |
| authorization_endpoint | string | URL ủy quyền trên trình duyệt dùng để yêu cầu sự đồng ý (consent) của người dùng. |
| token_endpoint | string | URL endpoint dùng để yêu cầu hoặc làm mới access token. |
| registration_endpoint | string | URL endpoint dùng để đăng ký client động (dynamic client registration). |
| revocation_endpoint | string | URL endpoint dùng để thu hồi các token hiện có. |
| response_types_supported | string[] | Danh sách các loại phản hồi được hỗ trợ. Giá trị enum: • `code`: Nhận mã ủy quyền để đổi lấy token. Ví dụ: `["code"]`. |
| grant_types_supported | string[] | Danh sách các loại cấp quyền được hỗ trợ. Các giá trị enum: • `authorization_code`: Đổi mã ủy quyền lấy access token. • `refresh_token`: Lấy access token mới khi token cũ hết hạn. Ví dụ: `["authorization_code", "refresh_token"]`. |
| code_challenge_methods_supported | string[] | Danh sách các phương thức thử thách mã PKCE (Proof Key for Code Exchange) được hỗ trợ. Giá trị enum: • `S256`: Yêu cầu mã hóa băm SHA-256 để bảo vệ yêu cầu ủy quyền. Ví dụ: `["S256"]`. |
| token_endpoint_auth_methods_supported | string[] | Danh sách các phương thức xác thực client được hỗ trợ tại endpoint token. Giá trị enum: • `none`: Không yêu cầu cung cấp client secret hoặc thông tin xác thực bổ sung. Ví dụ: `["none"]`. |
| scopes_supported | string[] | Danh sách các phạm vi quyền (scopes) được hỗ trợ. Giá trị enum: • `mcp:tt4b`: Quyền cần thiết để truy cập các tính năng của TikTok for Business MCP Server. Ví dụ: `["mcp:tt4b"]`. |

### Ví dụ phản hồi

```json
{
  "issuer": "https://business-api.tiktok.com/open_mcp/tt-ads-mcp-layer/oauth",
  "authorization_endpoint": "https://business-api.tiktok.com/portal/mcp-tt4b-authorize",
  "token_endpoint": "https://business-api.tiktok.com/open_mcp/tt-ads-mcp-layer/oauth/token",
  "registration_endpoint": "https://business-api.tiktok.com/open_mcp/tt-ads-mcp-layer/oauth/register",
  "revocation_endpoint": "https://business-api.tiktok.com/open_mcp/tt-ads-mcp-layer/oauth/revoke",
  "response_types_supported": ["code"],
  "grant_types_supported": ["authorization_code", "refresh_token"],
  "code_challenge_methods_supported": ["S256"],
  "token_endpoint_auth_methods_supported": ["none"],
  "scopes_supported": ["mcp:tt4b"]
}
```

---

## Khám phá máy chủ ủy quyền (`Discover authorization servers`)
<a id="doc-1873496742612993"></a>
<!-- doc_id: 1873496742612993 -->

`GET` `https://business-api.tiktok.com/open_mcp/{server}/.well-known/oauth-protected-resource/`

**Mục đích**: Sử dụng endpoint này để truy xuất siêu dữ liệu tài nguyên được bảo vệ của MCP, bao gồm các máy chủ ủy quyền kiểm soát quyền truy cập vào tài nguyên đó.

### Tham số đường dẫn (Path parameters)

| Field | Data Type | Description |
|---|---|---|
| server | string | Bắt buộc. URL đường dẫn máy chủ MCP (`tt-ads-mcp-flat` hoặc `tt-ads-mcp-layer`). |

### Ví dụ

#### cURL
```bash
curl --location --request GET 'https://business-api.tiktok.com/open_mcp/tt-ads-mcp-layer/.well-known/oauth-protected-resource'
```

#### Python
```python
import requests

SERVER = "tt-ads-mcp-layer"
url = f"https://business-api.tiktok.com/open_mcp/{SERVER}/.well-known/oauth-protected-resource"

response = requests.get(url)
print(response.json())
```

### Phản hồi

| Field | Data Type | Description |
|---|---|---|
| resource | string | URL định danh tài nguyên được bảo vệ của máy chủ MCP. |
| authorization_servers | string[] | Danh sách các URL máy chủ ủy quyền có thẩm quyền cấp quyền truy cập vào tài nguyên này. |
| scopes_supported | string[] | Danh sách các phạm vi quyền được tài nguyên hỗ trợ (`["mcp:tt4b"]`). |
| bearer_methods_supported | string[] | Các phương thức gửi bearer token được hỗ trợ (ví dụ: `["header"]`). |

### Ví dụ phản hồi

```json
{
  "resource": "https://business-api.tiktok.com/open_mcp/tt-ads-mcp-layer",
  "authorization_servers": [
    "https://business-api.tiktok.com/open_mcp/tt-ads-mcp-layer/oauth"
  ],
  "scopes_supported": ["mcp:tt4b"],
  "bearer_methods_supported": ["header"]
}
```

---

## Đăng ký ứng dụng client (`Register a client application`)
<a id="doc-1873496757798466"></a>
<!-- doc_id: 1873496757798466 -->

`POST` `https://business-api.tiktok.com/open_mcp/{server}/oauth/register/`

**Mục đích**: Sử dụng endpoint này để thực hiện đăng ký client động (Dynamic Client Registration) với máy chủ ủy quyền và nhận mã `client_id`.

### Header

| Field | Data Type | Description |
|---|---|---|
| Content-Type | string | Bắt buộc. Định dạng nội dung yêu cầu. Sử dụng `application/json`. |

### Tham số đường dẫn (Path parameters)

| Field | Data Type | Description |
|---|---|---|
| server | string | Bắt buộc. Đường dẫn máy chủ MCP (`tt-ads-mcp-flat` hoặc `tt-ads-mcp-layer`). |

### Tham số thân (POST JSON body)

| Field | Data Type | Description |
|---|---|---|
| client_name | string | Bắt buộc. Tên dễ đọc của ứng dụng client của bạn. |
| redirect_uris | string[] | Bắt buộc. Danh sách các URI chuyển hướng hợp lệ cho client. Phải là HTTPS hoặc URL cục bộ hợp lệ. |
| grant_types | string[] | Không. Danh sách grant types yêu cầu (`["authorization_code", "refresh_token"]`). |
| response_types | string[] | Không. Danh sách response types yêu cầu (`["code"]`). |
| token_endpoint_auth_method | string | Không. Phương thức xác thực client tại token endpoint. Giá trị enum: `none`. |

### Ví dụ

#### cURL
```bash
curl --location --request POST 'https://business-api.tiktok.com/open_mcp/tt-ads-mcp-layer/oauth/register' \
--header 'Content-Type: application/json' \
--data-raw '{
    "client_name": "My Custom AI Agent",
    "redirect_uris": [
        "https://myagent.example.com/oauth/callback"
    ],
    "grant_types": [
        "authorization_code",
        "refresh_token"
    ],
    "response_types": [
        "code"
    ],
    "token_endpoint_auth_method": "none"
}'
```

#### Python
```python
import requests

SERVER = "tt-ads-mcp-layer"
url = f"https://business-api.tiktok.com/open_mcp/{SERVER}/oauth/register"
headers = {"Content-Type": "application/json"}
payload = {
    "client_name": "My Custom AI Agent",
    "redirect_uris": ["https://myagent.example.com/oauth/callback"],
    "grant_types": ["authorization_code", "refresh_token"],
    "response_types": ["code"],
    "token_endpoint_auth_method": "none"
}

response = requests.post(url, headers=headers, json=payload)
data = response.json()
print("Client ID vừa cấp:", data.get("client_id"))
```

### Phản hồi

| Field | Data Type | Description |
|---|---|---|
| client_id | string | Mã định danh client duy nhất được cấp cho ứng dụng của bạn. |
| client_id_issued_at | integer | Dấu thời gian Unix (tính bằng giây) biểu thị thời điểm `client_id` được phát hành. |
| client_name | string | Tên ứng dụng client đã đăng ký. |
| redirect_uris | string[] | Danh sách các URI chuyển hướng đã đăng ký. |
| grant_types | string[] | Danh sách grant types đã được phê duyệt. |
| response_types | string[] | Danh sách response types đã được phê duyệt. |
| token_endpoint_auth_method | string | Phương thức xác thực client (`none`). |

### Phản hồi lỗi

| Field | Data Type | Description |
|---|---|---|
| error | string | Mã lỗi (ví dụ: `invalid_client_metadata`, `invalid_redirect_uri`). |
| error_description | string | Mô tả chi tiết nguyên nhân lỗi. |

---

## Yêu cầu ủy quyền từ người dùng (`Request user authorization`)
<a id="doc-1873496771526337"></a>
<!-- doc_id: 1873496771526337 -->

`GET` `https://business-api.tiktok.com/portal/mcp-tt4b-authorize/`

**Mục đích**: Mở giao diện trang ủy quyền trên trình duyệt nơi người dùng đăng nhập tài khoản TikTok for Business và chấp thuận yêu cầu cấp quyền của AI agent.

Sau khi người dùng phê duyệt, máy chủ ủy quyền sẽ chuyển hướng trình duyệt về `redirect_uri` đã đăng ký kèm mã ủy quyền (`code`).

> [!NOTE]
> • Không gắn cứng (hardcode) URL ủy quyền này. Hãy luôn trích xuất động từ trường `authorization_endpoint` trong siêu dữ liệu máy chủ ủy quyền.<br>
> • Để đảm bảo an toàn, người dùng có thể được yêu cầu hoàn thành bước xác minh email.

### Tham số truy vấn (Query parameters)

| Field | Data Type | Description |
|---|---|---|
| response_type | string | Bắt buộc. Loại phản hồi yêu cầu. Giá trị enum: `code`. |
| resource | string | Bắt buộc. URL đường dẫn máy chủ MCP cụ thể (`https://business-api.tiktok.com/open_mcp/tt-ads-mcp-flat` hoặc `https://business-api.tiktok.com/open_mcp/tt-ads-mcp-layer`). |
| client_id | string | Bắt buộc. Mã `client_id` đã được cấp từ endpoint đăng ký client. |
| redirect_uri | string | Bắt buộc. URI chuyển hướng, phải khớp chính xác với một trong các URI đã đăng ký. |
| scope | string | Bắt buộc. Phạm vi quyền yêu cầu. Giá trị enum: `mcp:tt4b`. |
| state | string | Không. Chuỗi ngẫu nhiên do client sinh ra để chống tấn công CSRF. Máy chủ sẽ trả lại nguyên vẹn giá trị này trong URL redirect. |
| code_challenge | string | Bắt buộc. Chuỗi thử thách mã PKCE, được tạo bằng cách băm chuỗi bí mật ngẫu nhiên `code_verifier` qua thuật toán SHA-256 và mã hóa Base64-URL. |
| code_challenge_method | string | Bắt buộc. Thuật toán băm sử dụng cho PKCE. Giá trị enum: `S256`. |

### Ví dụ URL ủy quyền

```text
https://business-api.tiktok.com/portal/mcp-tt4b-authorize?response_type=code&resource=https://business-api.tiktok.com/open_mcp/tt-ads-mcp-layer&client_id=YOUR_CLIENT_ID&redirect_uri=https://myagent.example.com/oauth/callback&scope=mcp:tt4b&code_challenge=E9Melhoa2OwvFrEMTJguCHaoeK1t8URWbuGJSstw-cM&code_challenge_method=S256&state=xyz123
```

### Phản hồi khi chuyển hướng (Redirect response)

Khi người dùng chấp thuận, trình duyệt sẽ được chuyển hướng về `redirect_uri` với các tham số:

| Field | Data Type | Description |
|---|---|---|
| code | string | Mã ủy quyền (authorization code) được cấp để đổi lấy token. |
| state | string | Giá trị `state` được trả về nguyên vẹn như lúc gửi yêu cầu. |

### Ví dụ phản hồi chuyển hướng

```text
https://myagent.example.com/oauth/callback?code=AUTH_CODE_XYZ123&state=xyz123
```


---

## Đổi mã ủy quyền MCP lấy token (`Exchange an MCP authorization code for tokens`)
<a id="doc-1873496785750401"></a>
<!-- doc_id: 1873496785750401 -->

`POST` `https://business-api.tiktok.com/open_mcp/{server}/oauth/token/`

**Mục đích**: Sử dụng endpoint này để đổi mã ủy quyền (authorization code) lấy access token và refresh token. Yêu cầu cấp token này được liên kết trực tiếp với đường dẫn máy chủ MCP được chỉ định trong URL.

### Header

| Field | Data Type | Description |
|---|---|---|
| Content-Type | string | Bắt buộc. Định dạng bản tin yêu cầu: `application/x-www-form-urlencoded`. |

### Tham số đường dẫn (Path parameters)

| Field | Data Type | Description |
|---|---|---|
| server | string | Bắt buộc. Đường dẫn URL máy chủ TikTok for Business MCP cụ thể. Các giá trị enum: `tt-ads-mcp-flat`, `tt-ads-mcp-layer`. Để tìm hiểu thêm về sự khác biệt giữa các URL máy chủ này, xem [Chọn URL máy chủ của bạn](https://business-api.tiktok.com/portal/docs/how-to-connect-a-custom-agent-to-tiktok-for-business-mcp-server/v1.3#anchor-3). |

### Tham số body (Body parameters)

| Field | Data Type | Description |
|---|---|---|
| grant_type | string | Bắt buộc. Phương thức cấp quyền token. Giá trị enum:<br>• `authorization_code`: Để đổi mã ủy quyền lấy access token. |
| code | string | Bắt buộc. Mã ủy quyền được cấp cho bạn sau khi người dùng phê duyệt yêu cầu ủy quyền. |
| code_verifier | string | Bắt buộc. Chuỗi xác minh PKCE tương ứng với code challenge ban đầu.<br>Chuỗi ngẫu nhiên nguyên bản chưa băm đã dùng để tạo `code_challenge` trong [yêu cầu ủy quyền ban đầu](50-mcp-authorization.md#doc-1873496771526337). Máy chủ sẽ băm chuỗi xác minh này bằng thuật toán SHA-256 và so khớp với code challenge gốc của bạn. Nếu trùng khớp, máy chủ xác minh danh tính ứng dụng và cấp access token. |
| redirect_uri | string | Bắt buộc. URI chuyển hướng dùng để xác thực. Đảm bảo giá trị này khớp chính xác với redirect URI bạn đã dùng trong [yêu cầu ủy quyền ban đầu](50-mcp-authorization.md#doc-1873496771526337). |

### Ví dụ

> [!NOTE]
> Ví dụ dưới đây sử dụng `tt-ads-mcp-layer` cho giá trị `{server}`. Bạn có thể thay đổi bằng giá trị máy chủ bạn đã chọn.

#### cURL
```bash
curl --location --request POST 'https://business-api.tiktok.com/open_mcp/tt-ads-mcp-layer/oauth/token' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'grant_type=authorization_code' \
--data-urlencode 'code=AUTH_CODE_XYZ123' \
--data-urlencode 'code_verifier=dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk' \
--data-urlencode 'redirect_uri=https://myagent.example.com/oauth/callback'
```

#### Python
```python
import requests

SERVER = "tt-ads-mcp-layer"
url = f"https://business-api.tiktok.com/open_mcp/{SERVER}/oauth/token"

headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

data = {
    "grant_type": "authorization_code",
    "code": "AUTH_CODE_XYZ123",
    "code_verifier": "dBjftJeZ4CVP-mB92K27uhbUJU1p1r_wW1gFWFOEjXk",
    "redirect_uri": "https://myagent.example.com/oauth/callback"
}

response = requests.post(url, headers=headers, data=data)
print(response.json())
```

### Phản hồi

Đổi token thành công sẽ trả về HTTP `200 OK`.

| Field | Data Type | Description |
|---|---|---|
| access_token | string | Access token được cấp cho bạn. |
| refresh_token | string | Refresh token được cấp cho bạn để sử dụng cho các lần làm mới token trong tương lai. |
| token_type | string | Loại token được cấp. Giá trị enum:<br>• `bearer`: Bearer token chuẩn OAuth 2.0. |
| expires_in | integer | Thời gian hiệu lực còn lại của access token, tính bằng giây. |
| refresh_token_expires_in | integer | Thời gian hiệu lực còn lại của refresh token, tính bằng giây. |
| scope | string | Phạm vi quyền hạn cụ thể được cấp cho token của bạn. Giá trị enum:<br>• `mcp:tt4b`: các quyền cần thiết để truy cập tính năng máy chủ TikTok for Business MCP Server. |

#### Ví dụ phản hồi thành công

```json
{
    "access_token": "mcp_at_0123456789abcdef0123456789abcdef",
    "expires_in": 86399,
    "refresh_token": "mcp_rt_fedcba9876543210fedcba9876543210",
    "refresh_token_expires_in": 2591999,
    "scope": "mcp:tt4b",
    "token_type": "bearer"
}
```

### Phản hồi lỗi

Khi thất bại, máy chủ trả về HTTP `400 Bad Request`.

| Field | Data Type | Description |
|---|---|---|
| error | string | Mã lỗi. Xem danh sách chi tiết các lỗi có thể xảy ra bên dưới. |
| error_description | string | Mô tả chi tiết về lỗi bằng ngôn ngữ tự nhiên. |

#### Danh sách các lỗi có thể xảy ra

| error | error_description |
|---|---|
| `invalid_request` | `grant_type is required` |
| `invalid_request` | `code is required` |
| `invalid_request` | `code_verifier is required` |
| `invalid_request` | `redirect_uri is required` |
| `unsupported_grant_type` | `grant_type is not supported` |
| `invalid_grant` | `authorization code not found or expired` |
| `invalid_grant` | `redirect_uri does not match authorization request` |
| `invalid_grant` | `code_verifier does not match code_challenge` |
| `invalid_grant` | `token is bound to a different MCP server` |

---

## Làm mới access token MCP (`Refresh an MCP access token`)
<a id="doc-1873496870932225"></a>
<!-- doc_id: 1873496870932225 -->

`POST` `https://business-api.tiktok.com/open_mcp/{server}/oauth/token/`

**Mục đích**: Sử dụng endpoint này để đổi một refresh token hợp lệ lấy một access token mới. Bạn cần gọi endpoint này trước khi access token hiện tại hết hạn, sử dụng cùng token endpoint như khi đổi mã ủy quyền.

### Header

| Field | Data Type | Description |
|---|---|---|
| Content-Type | string | Bắt buộc. Định dạng bản tin yêu cầu: `application/x-www-form-urlencoded`. |

### Tham số đường dẫn (Path parameters)

| Field | Data Type | Description |
|---|---|---|
| server | string | Bắt buộc. Đường dẫn URL máy chủ TikTok for Business MCP cụ thể. Các giá trị enum: `tt-ads-mcp-flat`, `tt-ads-mcp-layer`. Để tìm hiểu thêm về sự khác biệt giữa các URL máy chủ này, xem [Chọn URL máy chủ của bạn](https://business-api.tiktok.com/portal/docs/how-to-connect-a-custom-agent-to-tiktok-for-business-mcp-server/v1.3#anchor-3). |

### Tham số body (Body parameters)

| Field | Data Type | Description |
|---|---|---|
| grant_type | string | Bắt buộc. Phương thức cấp quyền token. Giá trị enum:<br>• `refresh_token`: Để đổi refresh token lấy access token mới. |
| refresh_token | string | Bắt buộc. Refresh token đã được cấp cho bạn [khi nhận access token](50-mcp-authorization.md#doc-1873496785750401). |

### Ví dụ

> [!NOTE]
> Ví dụ dưới đây sử dụng `tt-ads-mcp-layer` cho giá trị `{server}`. Bạn có thể thay đổi bằng giá trị máy chủ bạn đã chọn.

#### cURL
```bash
curl --location --request POST 'https://business-api.tiktok.com/open_mcp/tt-ads-mcp-layer/oauth/token' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'grant_type=refresh_token' \
--data-urlencode 'refresh_token=mcp_rt_fedcba9876543210fedcba9876543210'
```

#### Python
```python
import requests

SERVER = "tt-ads-mcp-layer"
url = f"https://business-api.tiktok.com/open_mcp/{SERVER}/oauth/token"

headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

data = {
    "grant_type": "refresh_token",
    "refresh_token": "mcp_rt_fedcba9876543210fedcba9876543210"
}

response = requests.post(url, headers=headers, data=data)
print(response.json())
```

### Phản hồi

Làm mới token thành công trả về HTTP `200 OK`.

| Field | Data Type | Description |
|---|---|---|
| access_token | string | Access token mới được cấp cho bạn. |
| refresh_token | string | Refresh token được cấp cho các lần làm mới token tiếp theo. |
| token_type | string | Loại token được cấp. Giá trị enum:<br>• `bearer`: Bearer token OAuth 2.0. |
| expires_in | integer | Thời gian hiệu lực còn lại của access token, tính bằng giây. |
| refresh_token_expires_in | integer | Thời gian hiệu lực còn lại của refresh token, tính bằng giây. |
| scope | string | Phạm vi quyền hạn cụ thể được cấp cho token. Giá trị enum:<br>• `mcp:tt4b`: quyền truy cập các tính năng của máy chủ TikTok for Business MCP Server. |

#### Ví dụ phản hồi thành công

```json
{
    "access_token": "mcp_at_new_0123456789abcdef0123456789abcdef",
    "expires_in": 86399,
    "refresh_token": "mcp_rt_new_fedcba9876543210fedcba9876543210",
    "refresh_token_expires_in": 2591941,
    "scope": "mcp:tt4b",
    "token_type": "bearer"
}
```

### Phản hồi lỗi

Khi thất bại, máy chủ trả về HTTP `400 Bad Request`.

| Field | Data Type | Description |
|---|---|---|
| error | string | Mã lỗi. Xem danh sách chi tiết các lỗi có thể xảy ra bên dưới. |
| error_description | string | Mô tả chi tiết về lỗi bằng ngôn ngữ tự nhiên. |

#### Danh sách các lỗi có thể xảy ra

| error | error_description |
|---|---|
| `invalid_request` | `grant_type is required` |
| `invalid_request` | `refresh_token is required` |
| `unsupported_grant_type` | `grant_type is not supported` |
| `invalid_grant` | `refresh token not found` |
| `invalid_grant` | `refresh token revoked` |
| `invalid_grant` | `refresh token expired` |
| `invalid_grant` | `refresh token is bound to a different MCP server` |

---

## Thu hồi token MCP (`Revoke an MCP token`)
<a id="doc-1873496798816274"></a>
<!-- doc_id: 1873496798816274 -->

`POST` `https://business-api.tiktok.com/open_mcp/{server}/oauth/revoke/`

**Mục đích**: Sử dụng endpoint này để thu hồi một access token hoặc refresh token, cho phép bạn chủ động ngắt kết nối sớm. Endpoint này có tính chất bình thản (idempotent - gọi nhiều lần cùng cho một kết quả như nhau).

### Header

| Field | Data Type | Description |
|---|---|---|
| Content-Type | string | Bắt buộc. Định dạng bản tin yêu cầu: `application/x-www-form-urlencoded`. |

### Tham số đường dẫn (Path parameters)

| Field | Data Type | Description |
|---|---|---|
| server | string | Bắt buộc. Đường dẫn URL máy chủ TikTok for Business MCP cụ thể. Các giá trị enum: `tt-ads-mcp-flat`, `tt-ads-mcp-layer`. Để tìm hiểu thêm về sự khác biệt giữa các URL máy chủ này, xem [Chọn URL máy chủ của bạn](https://business-api.tiktok.com/portal/docs/how-to-connect-a-custom-agent-to-tiktok-for-business-mcp-server/v1.3#anchor-3). |

### Tham số body (Body parameters)

| Field | Data Type | Description |
|---|---|---|
| token | string | Bắt buộc. Chuỗi token bạn muốn thu hồi (có thể là access token hoặc refresh token). |
| token_type_hint | string | Không bắt buộc. Gợi ý loại token được gửi để thu hồi. Các giá trị: `access_token`, `refresh_token`. |

### Ví dụ

> [!NOTE]
> Ví dụ dưới đây sử dụng `tt-ads-mcp-layer` cho giá trị `{server}`. Bạn có thể thay đổi bằng giá trị máy chủ bạn đã chọn.

#### cURL
```bash
curl --location --request POST 'https://business-api.tiktok.com/open_mcp/tt-ads-mcp-layer/oauth/revoke' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'token=mcp_at_0123456789abcdef0123456789abcdef' \
--data-urlencode 'token_type_hint=access_token'
```

#### Python
```python
import requests

SERVER = "tt-ads-mcp-layer"
url = f"https://business-api.tiktok.com/open_mcp/{SERVER}/oauth/revoke"

headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

data = {
    "token": "mcp_at_0123456789abcdef0123456789abcdef",
    "token_type_hint": "access_token"
}

response = requests.post(url, headers=headers, data=data)
print(response.json())
```

### Phản hồi

Yêu cầu thành công trả về HTTP `200 OK`.

| Field | Data Type | Description |
|---|---|---|
| revoked | boolean | Cho biết yêu cầu thu hồi token của bạn có thành công hay không. Các giá trị hỗ trợ: `true`, `false`.<br>**Lưu ý**: Trường này sẽ trả về `true` ngay cả khi bạn gửi một token không xác định, không hợp lệ hoặc đã hết hạn từ trước. Điều này là do endpoint có tính idempotent. Nếu token đó dù sao cũng không thể sử dụng được nữa, máy chủ sẽ an toàn bỏ qua và xem như việc thu hồi đã thành công. |

#### Ví dụ phản hồi thành công

```json
{
    "revoked": true
}
```

### Phản hồi lỗi

Khi thất bại, máy chủ trả về HTTP `400 Bad Request`.

| Field | Data Type | Description |
|---|---|---|
| error | string | Mã lỗi. Xem danh sách chi tiết các lỗi có thể xảy ra bên dưới. |
| error_description | string | Mô tả chi tiết về lỗi bằng ngôn ngữ tự nhiên. |

#### Danh sách các lỗi có thể xảy ra

| error | error_description |
|---|---|
| `invalid_request` | `token is required.` |
| `invalid_request` | `token_type_hint invalid` |

---

## Sử dụng công cụ MCP (`Use MCP tools`)
<a id="doc-1873496895169554"></a>
<!-- doc_id: 1873496895169554 -->

`POST` `https://business-api.tiktok.com/open_mcp/{server}/`

**Mục đích**: Sử dụng endpoint này để gửi các yêu cầu giao thức MCP đến đường dẫn máy chủ bằng cách sử dụng bearer access token, đảm bảo token bạn cung cấp là hợp lệ cho đường dẫn máy chủ MCP cụ thể đó.

### Header

| Field | Data Type | Description |
|---|---|---|
| Authorization | string | Bắt buộc. Access token dưới định dạng `Bearer {{Access-Token}}`. Access token này phải hợp lệ với đường dẫn máy chủ `server` MCP cụ thể. |
| Content-Type | string | Bắt buộc. Định dạng bản tin: `application/json`. |

### Tham số đường dẫn (Path parameters)

| Field | Data Type | Description |
|---|---|---|
| server | string | Bắt buộc. URL đường dẫn máy chủ TikTok for Business MCP cụ thể. Các giá trị enum: `tt-ads-mcp-flat`, `tt-ads-mcp-layer`. Để tìm hiểu thêm về sự khác biệt giữa các URL máy chủ này, xem [Chọn URL máy chủ của bạn](https://business-api.tiktok.com/portal/docs/how-to-connect-a-custom-agent-to-tiktok-for-business-mcp-server/v1.3#anchor-3). |

### Tham số body (Body parameters)

| Field | Data Type | Description |
|---|---|---|
| jsonrpc | string | Bắt buộc. Phiên bản giao thức JSON-RPC bạn đang sử dụng. Giá trị enum: `2.0`. |
| id | integer | Bắt buộc. Mã định danh duy nhất do bạn tự gán cho yêu cầu. Bạn sẽ nhận lại chính ID này trong phản hồi để ánh xạ kết quả. |
| method | string | Bắt buộc. Phương thức MCP cụ thể bạn muốn sử dụng. Các giá trị enum:<br>• `tools/list`: Để lấy danh sách các công cụ hiện có.<br>• `tools/call`: Để thực thi một công cụ cụ thể. |
| params | object | Bắt buộc. Payload tham số bạn cung cấp cho phương thức.<br>• Khi `method` là `tools/list`: cung cấp một object rỗng (`{}`).<br>• Khi `method` là `tools/call`: cung cấp các đối số cụ thể cho công cụ cần gọi. |

### Ví dụ

> [!NOTE]
> Ví dụ dưới đây sử dụng `tt-ads-mcp-layer` cho giá trị `{server}`. Bạn có thể thay đổi bằng giá trị máy chủ bạn đã chọn.

#### 1. Lấy danh sách công cụ hiện có (`tools/list`)

##### cURL
```bash
curl --location --request POST 'https://business-api.tiktok.com/open_mcp/tt-ads-mcp-layer' \
--header 'Authorization: Bearer mcp_at_0123456789abcdef0123456789abcdef' \
--header 'Content-Type: application/json' \
--data '{
    "jsonrpc": "2.0",
    "id": 1,
    "method": "tools/list",
    "params": {}
}'
```

##### Python
```python
import requests

SERVER = "tt-ads-mcp-layer"
ACCESS_TOKEN = "mcp_at_0123456789abcdef0123456789abcdef"
url = f"https://business-api.tiktok.com/open_mcp/{SERVER}"

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

payload = {
    "jsonrpc": "2.0",
    "id": 1,
    "method": "tools/list",
    "params": {}
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())
```

#### 2. Thực thi một công cụ cụ thể (`tools/call`)

##### cURL
```bash
curl --location --request POST 'https://business-api.tiktok.com/open_mcp/tt-ads-mcp-layer' \
--header 'Authorization: Bearer mcp_at_0123456789abcdef0123456789abcdef' \
--header 'Content-Type: application/json' \
--data '{
    "jsonrpc": "2.0",
    "id": 2,
    "method": "tools/call",
    "params": {
        "name": "advertiser_info_get",
        "arguments": {
            "advertiser_ids": [
                "7123456789012345678"
            ],
            "fields": [
                "name",
                "status",
                "currency",
                "timezone"
            ]
        }
    }
}'
```

##### Python
```python
import requests

SERVER = "tt-ads-mcp-layer"
ACCESS_TOKEN = "mcp_at_0123456789abcdef0123456789abcdef"
url = f"https://business-api.tiktok.com/open_mcp/{SERVER}"

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

payload = {
    "jsonrpc": "2.0",
    "id": 2,
    "method": "tools/call",
    "params": {
        "name": "advertiser_info_get",
        "arguments": {
            "advertiser_ids": [
                "7123456789012345678"
            ],
            "fields": [
                "name",
                "status",
                "currency",
                "timezone"
            ]
        }
    }
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())
```

### Phản hồi

| Field | Data Type | Description |
|---|---|---|
| jsonrpc | string | Phiên bản của giao thức JSON-RPC. Giá trị enum: `2.0`. |
| id | integer | Mã định danh bạn đã gửi ban đầu, dùng để khớp phản hồi này với yêu cầu chính xác. |
| result | object | Kết quả xử lý yêu cầu của bạn. Chứa danh sách công cụ hoặc kết quả thực thi công cụ. |
| ↳ tools | object[] | Chỉ trả về khi `method` được đặt là `tools/list` trong yêu cầu.<br>Danh sách các công cụ bạn có thể truy cập trên máy chủ này. Bạn có thể kiểm tra `name`, `description` và `inputSchema` của từng công cụ để xây dựng các lệnh gọi thực thi tiếp theo. |
| ↳ content | object[] | Chỉ trả về khi `method` được đặt là `tools/call` trong yêu cầu.<br>Dữ liệu đầu ra do công cụ bạn gọi sinh ra. Bạn sẽ trích xuất kết quả chi tiết của công cụ từ mảng này. |

#### Ví dụ phản hồi danh sách công cụ (`tools/list`)

```json
{
    "jsonrpc": "2.0",
    "id": 1,
    "result": {
        "tools": [
            {
                "annotations": {
                    "readOnlyHint": true
                },
                "description": "Lấy thông tin chi tiết của tài khoản nhà quảng cáo",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "advertiser_ids": {
                            "description": "Danh sách ID nhà quảng cáo",
                            "items": {
                                "type": "string"
                            },
                            "type": "array"
                        },
                        "fields": {
                            "description": "Danh sách các trường cần lấy",
                            "items": {
                                "enum": [
                                    "telephone_number",
                                    "contacter",
                                    "currency",
                                    "cellphone_number",
                                    "timezone",
                                    "advertiser_id",
                                    "role",
                                    "company",
                                    "status",
                                    "description",
                                    "rejection_reason",
                                    "address",
                                    "name",
                                    "language",
                                    "industry",
                                    "license_no",
                                    "email",
                                    "license_url",
                                    "country",
                                    "balance",
                                    "create_time",
                                    "display_timezone",
                                    "owner_bc_id",
                                    "company_name_editable",
                                    "can_use_custom_identity",
                                    "ads_only_mode"
                                ],
                                "type": "string"
                            },
                            "type": "array"
                        }
                    },
                    "required": [
                        "advertiser_ids"
                    ]
                },
                "name": "advertiser_info_get"
            },
            {
                "annotations": {
                    "readOnlyHint": true
                },
                "description": "Lấy thông tin ứng dụng",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "advertiser_id": {
                            "description": "ID nhà quảng cáo",
                            "type": "string"
                        },
                        "app_id": {
                            "description": "ID ứng dụng",
                            "type": "string"
                        }
                    },
                    "required": [
                        "advertiser_id",
                        "app_id"
                    ]
                },
                "name": "app_info_get"
            }
        ]
    }
}
```

#### Ví dụ phản hồi thực thi công cụ (`tools/call`)

```json
{
    "jsonrpc": "2.0",
    "id": 2,
    "result": {
        "content": [
            {
                "type": "text",
                "text": "{\"data\":{\"list\":[{\"name\":\"Example Ad Account\",\"currency\":\"USD\",\"timezone\":\"Etc/GMT-8\",\"status\":\"STATUS_ENABLE\"}]},\"code\":0,\"message\":\"OK\",\"request_id\":\"20261023120000010245035048123456\"}"
            }
        ]
    }
}
```

### Phản hồi lỗi

Khi truy cập các công cụ MCP, các lỗi xác thực sẽ tuân theo ngữ nghĩa Bearer Token chuẩn OAuth 2.0 (RFC 6750). Máy chủ sẽ trả về header `WWW-Authenticate` chứa lý do chính xác gây ra lỗi:

| HTTP Status Code | Meaning | Note |
|---|---|---|
| `401` | Missing token (Thiếu token) | Trả về một challenge `WWW-Authenticate`. |
| `401` | Invalid, expired, or revoked token (Token không hợp lệ, hết hạn hoặc đã bị thu hồi) | Trả về `WWW-Authenticate: Bearer error="invalid_token"`. |
| `403` | Insufficient scope (Không đủ quyền) | Có thể trả về `WWW-Authenticate: Bearer error="insufficient_scope"`. |

---

## Mã trạng thái HTTP cho MCP Authorization API (`HTTP Status Codes for MCP Authorization API`)
<a id="doc-1873496914836802"></a>
<!-- doc_id: 1873496914836802 -->

Các endpoint trong nhóm MCP Authorization API sử dụng các mã trạng thái HTTP tiêu chuẩn sau để biểu thị tình trạng thành công hoặc thất bại của yêu cầu:

| HTTP Status Code | Meaning | Typical Causes |
|---|---|---|
| 400 | Bad Request | Lỗi phía client. Bao gồm: thiếu trường bắt buộc, siêu dữ liệu đăng ký không hợp lệ, phương thức cấp quyền (grant) không hợp lệ, redirect URI không khớp, xác minh PKCE không khớp hoặc máy chủ MCP không khớp. |
| 401 | Unauthorized | Thiếu hoặc access token không hợp lệ tại thời điểm gửi yêu cầu. Token có thể bị thiếu, không hợp lệ, đã hết hạn hoặc đã bị thu hồi. |
| 403 | Forbidden | Không đủ quyền hạn. Token không có phạm vi quyền (scope) cần thiết để thực hiện hành động được yêu cầu. |
| 500 | Internal Server Error | Phản hồi lỗi từ dịch vụ nội bộ phía dưới. Máy chủ nhận được phản hồi sai định dạng hoặc không đầy đủ từ dịch vụ xác thực nội bộ. |
| 503 | Service Unavailable | Dịch vụ ủy quyền hoặc một thành phần phụ thuộc cốt lõi tạm thời gián đoạn (ví dụ: lỗi đường truyền RPC). |
