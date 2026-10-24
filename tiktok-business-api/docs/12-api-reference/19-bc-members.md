# Thành viên BC (BC Members)

Nhóm API Thành viên Business Center (BC Members) cho phép bạn quản lý danh sách thành viên, phân quyền vai trò cơ bản (Admin, Standard) và vai trò tài chính nâng cao (Finance Manager, Finance Analyst) trong Business Center. Thông qua các endpoint này, quản trị viên có thể xem danh sách thành viên, mời thành viên mới qua email kèm phân quyền tài sản, cập nhật tên hoặc vai trò của thành viên, và xóa thành viên hoặc thu hồi lời mời tham gia.

| Endpoint | Method | Đường dẫn | Mục đích |
|---|---|---|---|
| Tổng quan thành viên Business Center | - | - | Giới thiệu hệ thống quản trị người dùng và phân quyền trong Business Center |
| Lấy danh sách thành viên Business Center | `GET` | `/open_api/v1.3/bc/member/get/` | Tra cứu danh sách thành viên và trạng thái lời mời tham gia |
| Mời thành viên vào Business Center | `POST` | `/open_api/v1.3/bc/member/invite/` | Gửi lời mời qua email và phân quyền tài sản ban đầu |
| Cập nhật thông tin thành viên | `POST` | `/open_api/v1.3/bc/member/update/` | Thay đổi tên hiển thị, vai trò cơ bản hoặc vai trò tài chính |
| Xóa thành viên hoặc thu hồi lời mời | `POST` | `/open_api/v1.3/bc/member/delete/` | Xóa thành viên khỏi Business Center hoặc hủy lời mời đang chờ |

---

## Tổng quan thành viên Business Center (`BC Members`)
<a id="doc-1739516035501058"></a>
<!-- doc_id: 1739516035501058 -->

Business Center là trung tâm điều hành tập trung cho các tổ chức thuộc mọi quy mô nhằm kích hoạt các hoạt động tiếp thị và tiếp cận đối tượng mong muốn một cách cộng tác trên TikTok. Nhóm API BC Members giúp bạn quản lý các thành viên trong một Business Center.

Nhóm này bao gồm các endpoint sau:
- [Lấy danh sách thành viên Business Center](19-bc-members.md#doc-1739939404802049): Lấy danh sách thành viên và người được mời.
- [Mời thành viên vào Business Center](19-bc-members.md#doc-1739939455765505): Mời thành viên mới tham gia Business Center.
- [Cập nhật thông tin thành viên](19-bc-members.md#doc-1739696704424961): Sửa vai trò và thông tin thành viên.
- [Xóa thành viên hoặc thu hồi lời mời](19-bc-members.md#doc-1739939482851329): Xóa người dùng hoặc hủy lời mời đang chờ.

> [!NOTE]
> Bạn cần có vai trò Quản trị viên (`Admin`) của Business Center để thực hiện các thao tác quản lý thành viên.

---

## Lấy danh sách thành viên Business Center (`Get the members of a BC`)
<a id="doc-1739939404802049"></a>
<!-- doc_id: 1739939404802049 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/bc/member/get/`

**Mục đích**: Lấy danh sách thành viên trong một Business Center cùng với thông tin vai trò, trạng thái liên kết và quyền tài chính. Bạn cần có vai trò Quản trị viên (`Admin`) của Business Center. Nếu cần lấy danh sách tài sản được gán cho một thành viên, sử dụng [/bc/asset/get/](15-bc-assets.md#doc-1739432717798401).

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Có | Mã truy cập đã được ủy quyền. Xem [Xác thực](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (GET: query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `bc_id` | string | Có | ID của Business Center. |
| `page` | number | Không | Trang dữ liệu hiện tại. Mặc định: `1`. |
| `page_size` | number | Không | Số lượng bản ghi mỗi trang (tối đa 20 bản ghi). Mặc định: `10`. |
| `filtering` | object | Không | Điều kiện lọc danh sách thành viên. Truyền dưới dạng chuỗi JSON object. |
| ↳ `keyword` | string | Không | Từ khóa tìm kiếm theo tên hoặc email thành viên. |
| ↳ `user_role` | string | Không | Vai trò cơ bản trong Business Center (`ADMIN`: Quản trị viên, `STANDARD`: Thành viên tiêu chuẩn). |
| ↳ `relation_status` | string | Không | Trạng thái liên kết của thành viên với Business Center (`BOUND`: Đã tham gia, `PENDING`: Đang chờ chấp nhận lời mời, `REJECTED`: Đã từ chối lời mời). |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Giá trị `0` là thành công. Xem [Phụ lục mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Mã log định danh duy nhất của yêu cầu API. |
| `data` | object | Dữ liệu trả về. |
| ↳ `list` | object[] | Danh sách thông tin thành viên. |
| ↳↳ `user_id` | string | ID của người dùng. |
| ↳↳ `user_name` | string | Tên của người dùng. |
| ↳↳ `user_email` | string | Địa chỉ email của người dùng (có thể được che bớt ký tự để bảo vệ thông tin cá nhân, ví dụ: `u**r@example.com`). |
| ↳↳ `user_role` | string | Vai trò cơ bản trong Business Center (`ADMIN`, `STANDARD`). |
| ↳↳ `relation_status` | string | Trạng thái lời mời/tham gia (`BOUND`, `PENDING`, `REJECTED`). |
| ↳↳ `ext_user_role` | object | Vai trò nâng cao khác ngoài vai trò cơ bản. |
| ↳↳↳ `finance_role` | string | Vai trò tài chính (`MANAGER`: Quản lý tài chính, `ANALYST`: Nhà phân tích tài chính). |
| ↳ `page_info` | object | Thông tin phân trang. |
| ↳↳ `page` | number | Trang hiện tại. |
| ↳↳ `page_size` | number | Số lượng bản ghi mỗi trang. |
| ↳↳ `total_number` | number | Tổng số lượng thành viên. |
| ↳↳ `total_page` | number | Tổng số trang. |

### Ví dụ

#### cURL
```bash
curl -X GET "https://business-api.tiktok.com/open_api/v1.3/bc/member/get/?bc_id=7123456789012345678&page=1&page_size=10" \
  -H "Access-Token: ACCESS_TOKEN"
```

#### Python
```python
import requests

ACCESS_TOKEN = "your_access_token"
BC_ID = "7123456789012345678"

url = "https://business-api.tiktok.com/open_api/v1.3/bc/member/get/"
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
  "request_id": "202410231500000501111222333444555",
  "data": {
    "list": [
      {
        "ext_user_role": {
          "finance_role": "MANAGER"
        },
        "relation_status": "BOUND",
        "user_email": "a**n@company.com",
        "user_id": "7123456789012345671",
        "user_name": "Nguyen Van Admin",
        "user_role": "ADMIN"
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

## Mời thành viên vào Business Center (`Invite members to a BC`)
<a id="doc-1739939455765505"></a>
<!-- doc_id: 1739939455765505 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/bc/member/invite/`

**Mục đích**: Gửi lời mời qua email cho các thành viên mới tham gia Business Center, gán vai trò cơ bản, vai trò tài chính và tùy chọn chia sẻ tài sản tài khoản quảng cáo ban đầu. Bạn cần có vai trò Quản trị viên (`Admin`) của Business Center.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Có | Mã truy cập đã được ủy quyền. Xem [Xác thực](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| `Content-Type` | string | Có | Định dạng nội dung yêu cầu. Giá trị cho phép: `application/json`. |

### Tham số (POST: JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `bc_id` | string | Có | ID của Business Center. |
| `emails` | string[] | Có | Danh sách địa chỉ email nhận lời mời tham gia Business Center (tối đa 20 email). |
| `user_role` | string | Có | Vai trò cơ bản gán cho thành viên.<br><br>**Enum**:<br>• `ADMIN`: Quản trị viên (quản lý thành viên và tài sản).<br>• `STANDARD`: Thành viên tiêu chuẩn (chỉ làm việc trên các tài khoản được phân quyền). |
| `ext_user_role` | object | Không | Vai trò tài chính nâng cao gán cho thành viên. |
| ↳ `finance_role` | string | Không | Vai trò tài chính (`MANAGER`: Quản lý tài chính, `ANALYST`: Chuyên viên phân tích tài chính). |
| `asset_ids` | string[] | Không | Danh sách ID tài khoản quảng cáo muốn phân quyền ngay khi mời thành viên. |
| `advertiser_role` | string | Không | Vai trò trên tài khoản quảng cáo gán cho thành viên (`ADMIN`, `OPERATOR`, `ANALYST`). Mặc định: `ANALYST`. |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Giá trị `0` là thành công. Xem [Phụ lục mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Mã log định danh duy nhất của yêu cầu API. |
| `data` | object | Dữ liệu trả về (đối tượng rỗng `{}` khi thành công). |

### Ví dụ

#### cURL
```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/bc/member/invite/" \
  -H "Access-Token: ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "bc_id": "7123456789012345678",
    "emails": ["member1@example.com", "member2@example.com"],
    "user_role": "STANDARD",
    "ext_user_role": {
      "finance_role": "ANALYST"
    },
    "asset_ids": ["6789012345678901234"],
    "advertiser_role": "OPERATOR"
  }'
```

#### Phản hồi mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20241023150000050222333444555666",
  "data": {}
}
```

---

## Cập nhật thông tin thành viên (`Update info of a BC member`)
<a id="doc-1739696704424961"></a>
<!-- doc_id: 1739696704424961 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/bc/member/update/`

**Mục đích**: Cập nhật thông tin tên hiển thị, vai trò cơ bản hoặc vai trò tài chính của một thành viên trong Business Center. Bạn cần có vai trò Quản trị viên (`Admin`) của Business Center.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Có | Mã truy cập đã được ủy quyền. Xem [Xác thực](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| `Content-Type` | string | Có | Định dạng nội dung yêu cầu. Giá trị cho phép: `application/json`. |

### Tham số (POST: JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `bc_id` | string | Có | ID của Business Center. |
| `user_id` | string | Có | ID người dùng của thành viên cần cập nhật. |
| `user_name` | string | Không | Tên hiển thị mới của người dùng trong Business Center. |
| `user_role` | string | Không | Vai trò cơ bản mới của thành viên (`ADMIN` hoặc `STANDARD`). |
| `ext_user_role` | object | Không | Cấu hình vai trò tài chính nâng cao mới. |
| ↳ `finance_role` | string | Không | Vai trò tài chính mới (`MANAGER`, `ANALYST`). |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Giá trị `0` là thành công. Xem [Phụ lục mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Mã log định danh duy nhất của yêu cầu API. |
| `data` | object | Dữ liệu trả về (đối tượng rỗng `{}` khi thành công). |

### Ví dụ

#### cURL
```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/bc/member/update/" \
  -H "Access-Token: ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "bc_id": "7123456789012345678",
    "user_id": "7123456789012345671",
    "user_name": "Tran Thi B",
    "user_role": "ADMIN",
    "ext_user_role": {
      "finance_role": "MANAGER"
    }
  }'
```

#### Phản hồi mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20241023150000050333444555666777",
  "data": {}
}
```

---

## Xóa thành viên hoặc thu hồi lời mời (`Delete a member from a BC or revoke a member invitation`)
<a id="doc-1739939482851329"></a>
<!-- doc_id: 1739939482851329 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/bc/member/delete/`

**Mục đích**: Xóa một thành viên hiện có khỏi Business Center hoặc thu hồi lời mời tham gia đang chờ duyệt. Bạn cần có vai trò Quản trị viên (`Admin`) của Business Center.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Có | Mã truy cập đã được ủy quyền. Xem [Xác thực](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| `Content-Type` | string | Có | Định dạng nội dung yêu cầu. Giá trị cho phép: `application/json`. |

### Tham số (POST: JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `bc_id` | string | Có | ID của Business Center. |
| `user_id` | string | Điều kiện | Bắt buộc khi muốn xóa một thành viên hiện có. ID người dùng của thành viên (tra cứu qua [/bc/member/get/](19-bc-members.md#doc-1739939404802049)). |
| `user_email` | string | Điều kiện | Bắt buộc khi muốn thu hồi lời mời tham gia của một người dùng. Địa chỉ email của người dùng được mời (tra cứu qua [/bc/member/get/](19-bc-members.md#doc-1739939404802049)). |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Giá trị `0` là thành công. Xem [Phụ lục mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Mã log định danh duy nhất của yêu cầu API. |
| `data` | object | Dữ liệu trả về (đối tượng rỗng `{}` khi thành công). |

### Ví dụ

#### cURL: Xóa thành viên hiện có bằng user_id
```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/bc/member/delete/" \
  -H "Access-Token: ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "bc_id": "7123456789012345678",
    "user_id": "7123456789012345671"
  }'
```

#### cURL: Thu hồi lời mời bằng user_email
```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/bc/member/delete/" \
  -H "Access-Token: ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "bc_id": "7123456789012345678",
    "user_email": "pending_user@example.com"
  }'
```

#### Phản hồi mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20241023150000050444555666777888",
  "data": {}
}
```
