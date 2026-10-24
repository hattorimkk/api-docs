# Nhóm tài sản BC (BC Asset Groups)

Tài liệu hướng dẫn và tham chiếu các API quản lý Nhóm tài sản (Asset Groups) trong Business Center trên TikTok Business API.

---

<a id="doc-1749001426121730"></a>
<!-- doc_id: 1749001426121730 -->
## 1. Tổng quan về Nhóm tài sản BC (Overview)

Business Center (BC) là trung tâm quản lý tập trung toàn diện dành cho các tổ chức, doanh nghiệp thuộc mọi quy mô nhằm triển khai các hoạt động tiếp thị và tiếp cận đối tượng mục tiêu trên TikTok một cách cộng tác.

**Nhóm tài sản (Asset Group)** là một tập hợp các tài sản (ví dụ: tài khoản quảng cáo - advertiser accounts) bên trong một Business Center. Bộ API BC Asset Groups cho phép bạn quản lý các Nhóm tài sản trong Business Center theo phương thức tự động và có hệ thống. Ví dụ: Người dùng Quản trị viên (Admin) của Business Center loại Đại lý (Agency) có thể sử dụng API này để gom các tài khoản quảng cáo vào cùng một Nhóm tài sản và phân quyền Nhóm tài sản cho các thành viên cụ thể chỉ trong một thao tác.

> **Lưu ý quan trọng:**
> - Hiện tại, API Asset Group chỉ hỗ trợ loại tài sản là tài khoản quảng cáo (`asset_type` = `ADVERTISER`).
> - Chỉ người dùng có vai trò Quản trị viên (`user_role` = `ADMIN`) trong Business Center mới có quyền tạo Nhóm tài sản và thêm tài sản vào nhóm.
> - Thành viên tiêu chuẩn (`user_role` = `STANDARD`) chỉ có thể xem các Nhóm tài sản mà họ được phân quyền tham gia.

### Danh sách các Endpoint trong nhóm:
- [Tạo nhóm tài sản (Create an Asset Group)](#2-tạo-nhóm-tài-sản-create-an-asset-group): `POST /open_api/v1.3/bc/asset_group/create/`
- [Cập nhật nhóm tài sản (Update an Asset Group)](#3-cập-nhật-nhóm-tài-sản-update-an-asset-group): `POST /open_api/v1.3/bc/asset_group/update/`
- [Lấy danh sách nhóm tài sản (Get all Asset Groups)](#4-lấy-danh-sách-nhóm-tài-sản-get-all-asset-groups): `GET /open_api/v1.3/bc/asset_group/list/`
- [Lấy chi tiết nhóm tài sản (Get the details of an Asset Group)](#5-lấy-chi-tiết-nhóm-tài-sản-get-the-details-of-an-asset-group): `GET /open_api/v1.3/bc/asset_group/get/`
- [Xóa nhóm tài sản (Delete Asset Groups)](#6-xóa-nhóm-tài-sản-delete-asset-groups): `POST /open_api/v1.3/bc/asset_group/delete/`

---

<a id="doc-1749001658583105"></a>
<!-- doc_id: 1749001658583105 -->
## 2. Tạo nhóm tài sản (Create an Asset Group)

Sử dụng endpoint này để tạo một Nhóm tài sản mới trong Business Center của bạn. Bạn cần có quyền Quản trị viên (Admin) của Business Center.

### Thông tin Endpoint
- **URL:** `https://business-api.tiktok.com/open_api/v1.3/bc/asset_group/create/`
- **Phương thức:** `POST`

### Header
| Header | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Có | Access Token được cấp quyền xác thực. Xem thêm phần Xác thực. |
| Content-Type | string | Có | Kiểu nội dung của yêu cầu. Giá trị cố định: `application/json`. |

### Tham số Body (Request Body)
| Tham số | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `bc_id` | string | Có | ID của Business Center. |
| `asset_group_name` | string | Có | Tên của Nhóm tài sản. |
| `assets` | object[] | Có | Danh sách tài sản bạn muốn thêm vào Nhóm tài sản. Tối đa 200 tài sản. |
| ↳ `asset_id` | string | Có | ID của tài sản. Khi loại tài sản (`asset_type`) là `ADVERTISER`, đây chính là ID tài khoản quảng cáo (advertiser ID). |
| ↳ `asset_type` | string | Không | Loại tài sản. Hiện tại loại duy nhất được hỗ trợ là `ADVERTISER`. Trường này là tùy chọn vì hệ thống mặc định gán là `ADVERTISER`. |
| `members` | object[] | Có | Danh sách thành viên trong Business Center bạn muốn cấp quyền truy cập vào Nhóm tài sản. Tối đa 50 thành viên. |
| ↳ `member_id` | string | Có | ID của thành viên Business Center. |
| ↳ `asset_roles` | map<string, string> | Không | Vai trò bạn muốn chỉ định cho thành viên theo từng loại tài sản.<br>Khóa (Key): Loại tài sản, giá trị enum: `ADVERTISER`.<br>Giá trị (Value): Vai trò được chỉ định, các giá trị enum:<br>• `ADVERTISER_ROLE_ADMIN`: Quản lý toàn diện tài khoản quảng cáo (cài đặt tài khoản, tài chính, phân quyền), quản lý chiến dịch và xem báo cáo hiệu suất.<br>• `ADVERTISER_ROLE_OPERATOR`: Quản lý chiến dịch quảng cáo (tạo và chỉnh sửa quảng cáo) và xem báo cáo hiệu suất.<br>• `ADVERTISER_ROLE_ANALYST`: Chỉ xem báo cáo hiệu suất và dữ liệu quảng cáo.<br>Giá trị mặc định: `{"ADVERTISER": "ADVERTISER_ROLE_ADMIN"}`. |

### Tham số Response
| Trường | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi từ hệ thống. `0` thể hiện thao tác thành công. |
| `message` | string | Thông báo phản hồi đi kèm. |
| `request_id` | string | ID duy nhất định danh yêu cầu gửi lên hệ thống. |
| `data` | object | Dữ liệu trả về. |
| ↳ `asset_group_id` | string | ID của Nhóm tài sản vừa được tạo thành công. |

### Ví dụ cURL
```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/bc/asset_group/create/" \
  -H "Access-Token: YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "bc_id": "7012345678901234567",
    "asset_group_name": "Agency Client Group A",
    "assets": [
      {
        "asset_id": "7112345678901234567",
        "asset_type": "ADVERTISER"
      }
    ],
    "members": [
      {
        "member_id": "7098765432109876543",
        "asset_roles": {
          "ADVERTISER": "ADVERTISER_ROLE_ADMIN"
        }
      }
    ]
  }'
```

### Ví dụ Python
```python
import requests

url = "https://business-api.tiktok.com/open_api/v1.3/bc/asset_group/create/"
headers = {
    "Access-Token": "YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}
payload = {
    "bc_id": "7012345678901234567",
    "asset_group_name": "Agency Client Group A",
    "assets": [
        {
            "asset_id": "7112345678901234567",
            "asset_type": "ADVERTISER"
        }
    ],
    "members": [
        {
            "member_id": "7098765432109876543",
            "asset_roles": {
                "ADVERTISER": "ADVERTISER_ROLE_ADMIN"
            }
        }
    ]
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())
```

### Phản hồi thành công mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202610231200000101",
  "data": {
    "asset_group_id": "7200001234567890123"
  }
}
```

---

<a id="doc-1749001662156801"></a>
<!-- doc_id: 1749001662156801 -->
## 3. Cập nhật nhóm tài sản (Update an Asset Group)

Sử dụng endpoint này để cập nhật danh sách tài sản, thành viên hoặc đổi tên Nhóm tài sản. Bạn cần có quyền Quản trị viên (Admin) của Business Center.

### Thông tin Endpoint
- **URL:** `https://business-api.tiktok.com/open_api/v1.3/bc/asset_group/update/`
- **Phương thức:** `POST`

### Header
| Header | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Có | Access Token được cấp quyền xác thực. |
| Content-Type | string | Có | Kiểu nội dung yêu cầu: `application/json`. |

### Tham số Body (Request Body)
| Tham số | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `bc_id` | string | Có | ID của Business Center. |
| `asset_group_id` | string | Có | ID của Nhóm tài sản bạn muốn cập nhật. |
| `update_entity` | string | Có | Thực thể bạn muốn cập nhật. Các giá trị enum khả dụng: `ASSET`, `MEMBER`, `NAME`. |
| `asset_group_name` | string | Điều kiện | Tên mới của Nhóm tài sản. Bắt buộc khi `update_entity` là `NAME`. |
| `action` | string | Điều kiện | Loại hành động cần thực hiện. Các giá trị enum: `ADD` (thêm vào), `DELETE` (xóa bớt). Bắt buộc khi `update_entity` là `ASSET` hoặc `MEMBER`. |
| `assets` | object[] | Điều kiện | Danh sách tài sản cần cập nhật. Tối đa 200 tài sản. Bắt buộc khi `update_entity` là `ASSET`. |
| ↳ `asset_id` | string | Có | ID của tài sản (ID tài khoản quảng cáo khi `asset_type` là `ADVERTISER`). |
| ↳ `asset_type` | string | Không | Loại tài sản. Hiện tại chỉ hỗ trợ `ADVERTISER`. Mặc định là `ADVERTISER`. |
| `members` | object[] | Điều kiện | Danh sách thành viên cần cập nhật. Tối đa 50 thành viên. Bắt buộc khi `update_entity` là `MEMBER`. |
| ↳ `member_id` | string | Có | ID của thành viên Business Center. |
| ↳ `asset_roles` | map<string, string> | Không | Phân quyền vai trò cho thành viên theo loại tài sản.<br>Khóa: `ADVERTISER`.<br>Giá trị: `ADVERTISER_ROLE_ADMIN`, `ADVERTISER_ROLE_OPERATOR`, `ADVERTISER_ROLE_ANALYST`. Mặc định: `{"ADVERTISER": "ADVERTISER_ROLE_ADMIN"}`. |

### Tham số Response
| Trường | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi từ hệ thống. `0` thể hiện thành công. |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Log ID định danh yêu cầu. |
| `data` | object | Dữ liệu trả về (thường là rỗng khi cập nhật thành công). |

### Ví dụ cURL
```bash
# Thêm tài sản vào Nhóm tài sản
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/bc/asset_group/update/" \
  -H "Access-Token: YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "bc_id": "7012345678901234567",
    "asset_group_id": "7200001234567890123",
    "update_entity": "ASSET",
    "action": "ADD",
    "assets": [
      {
        "asset_id": "7112345678909876543",
        "asset_type": "ADVERTISER"
      }
    ]
  }'
```

### Ví dụ Python
```python
import requests

url = "https://business-api.tiktok.com/open_api/v1.3/bc/asset_group/update/"
headers = {
    "Access-Token": "YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}
payload = {
    "bc_id": "7012345678901234567",
    "asset_group_id": "7200001234567890123",
    "update_entity": "NAME",
    "asset_group_name": "Agency Client Group A - Q4 Updated"
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())
```

### Phản hồi thành công mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202610231200000102",
  "data": {}
}
```

---

<a id="doc-1749001665910786"></a>
<!-- doc_id: 1749001665910786 -->
## 4. Lấy danh sách nhóm tài sản (Get all Asset Groups)

Sử dụng endpoint này để lấy toàn bộ danh sách các Nhóm tài sản trong Business Center của bạn. Bạn cần có quyền Quản trị viên (Admin) của Business Center.

### Thông tin Endpoint
- **URL:** `https://business-api.tiktok.com/open_api/v1.3/bc/asset_group/list/`
- **Phương thức:** `GET`

### Header
| Header | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Có | Access Token được cấp quyền xác thực. |
| Content-Type | string | Có | Kiểu nội dung yêu cầu: `application/json`. |

### Tham số Query (Query Parameters)
| Tham số | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `bc_id` | string | Có | ID của Business Center. |
| `filtering` | object | Không | Điều kiện lọc danh sách nhóm tài sản. |
| ↳ `keyword` | string | Không | Từ khóa tìm kiếm. Hiện tại chỉ hỗ trợ khớp chính xác tên nhóm (`asset_group_name`) hoặc mã nhóm (`asset_group_id`). |
| `page` | number | Không | Số trang hiện tại. Mặc định: `1`. |
| `page_size` | number | Không | Số lượng kết quả trên mỗi trang. Giá trị mặc định: `10`. Tối đa: `50`. |

### Tham số Response
| Trường | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi hệ thống. `0` thể hiện thành công. |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Log ID của yêu cầu. |
| `data` | object | Dữ liệu trả về từ hệ thống. |
| ↳ `asset_groups` | object[] | Danh sách thông tin các Nhóm tài sản. |
| ↳↳ `asset_group_id` | string | ID của Nhóm tài sản. |
| ↳↳ `asset_group_name` | string | Tên của Nhóm tài sản. |
| ↳ `page_info` | object | Thông tin phân trang. |
| ↳↳ `page` | number | Số trang hiện tại. |
| ↳↳ `page_size` | number | Số lượng bản ghi trên một trang. |
| ↳↳ `total_number` | number | Tổng số lượng kết quả tìm thấy. |
| ↳↳ `total_page` | number | Tổng số trang kết quả. |

### Ví dụ cURL
```bash
curl -X GET "https://business-api.tiktok.com/open_api/v1.3/bc/asset_group/list/?bc_id=7012345678901234567&page=1&page_size=10" \
  -H "Access-Token: YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json"
```

### Ví dụ Python
```python
import requests

url = "https://business-api.tiktok.com/open_api/v1.3/bc/asset_group/list/"
headers = {
    "Access-Token": "YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}
params = {
    "bc_id": "7012345678901234567",
    "page": 1,
    "page_size": 10
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

### Phản hồi thành công mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202610231200000103",
  "data": {
    "asset_groups": [
      {
        "asset_group_id": "7200001234567890123",
        "asset_group_name": "Agency Client Group A"
      },
      {
        "asset_group_id": "7200001234567890124",
        "asset_group_name": "Retail E-Commerce Accounts"
      }
    ],
    "page_info": {
      "page": 1,
      "page_size": 10,
      "total_number": 2,
      "total_page": 1
    }
  }
}
```

---

<a id="doc-1749001669670913"></a>
<!-- doc_id: 1749001669670913 -->
## 5. Lấy chi tiết nhóm tài sản (Get the details of an Asset Group)

Sử dụng endpoint này để truy vấn danh sách tài sản hoặc danh sách thành viên thuộc về một Nhóm tài sản cụ thể trong Business Center. Bạn cần có quyền Quản trị viên (Admin) của Business Center.

### Thông tin Endpoint
- **URL:** `https://business-api.tiktok.com/open_api/v1.3/bc/asset_group/get/`
- **Phương thức:** `GET`

### Header
| Header | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Có | Access Token được cấp quyền xác thực. |
| Content-Type | string | Có | Kiểu nội dung yêu cầu: `application/json`. |

### Tham số Query (Query Parameters)
| Tham số | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `bc_id` | string | Có | ID của Business Center. |
| `asset_group_id` | string | Có | ID của Nhóm tài sản cần truy vấn chi tiết. |
| `query_entity` | string | Có | Thực thể mà bạn muốn truy vấn thông tin.<br>Các giá trị enum: `ASSET` (lấy danh sách tài sản), `MEMBER` (lấy danh sách thành viên). |
| `filtering` | object | Không | Điều kiện lọc danh sách kết quả. |
| ↳ `keyword` | string | Không | Từ khóa tìm kiếm:<br>• Nếu `query_entity` là `ASSET`: Bạn có thể tìm kiếm gần đúng bằng tên tài sản (`asset_name`) hoặc tìm chính xác theo mã tài sản (`asset_id`).<br>• Nếu `query_entity` là `MEMBER`: Bạn có thể tìm kiếm gần đúng theo tên người dùng (`user_name`) hoặc tìm chính xác theo email người dùng (`user_email`). |
| `page` | number | Không | Số trang kết quả cần lấy. Giá trị mặc định: `1`. |
| `page_size` | number | Không | Số lượng kết quả trên mỗi trang. Giá trị mặc định: `10`. |

### Tham số Response
| Trường | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi từ hệ thống. `0` là thành công. |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Log ID định danh yêu cầu. |
| `data` | object | Dữ liệu trả về chi tiết. |
| ↳ `asset_group` | object[] | Mảng chứa thông tin Nhóm tài sản. |
| ↳↳ `asset_group_name` | string | Tên của Nhóm tài sản. |
| ↳↳ `asset_group_id` | string | ID của Nhóm tài sản. |
| ↳↳ `assets` | object[] | Danh sách tài sản. Chỉ trả về khi `query_entity` là `ASSET`. |
| ↳↳↳ `asset_type` | string | Loại tài sản (ví dụ: `ADVERTISER`). |
| ↳↳↳ `asset_id` | string | ID tài sản (ID tài khoản quảng cáo). |
| ↳↳ `members` | object[] | Danh sách thành viên. Chỉ trả về khi `query_entity` là `MEMBER`. |
| ↳↳↳ `member_id` | string | ID thành viên Business Center. |
| ↳↳↳ `asset_roles` | map | Vai trò được phân quyền cho thành viên theo từng loại tài sản. |
| ↳ `page_info` | object | Thông tin phân trang. |
| ↳↳ `page` | number | Trang hiện tại. |
| ↳↳ `page_size` | number | Kích thước trang. |
| ↳↳ `total_number` | number | Tổng số lượng kết quả. |
| ↳↳ `total_page` | number | Tổng số trang. |

### Ví dụ cURL
```bash
# Truy vấn danh sách tài sản trong nhóm
curl -X GET "https://business-api.tiktok.com/open_api/v1.3/bc/asset_group/get/?bc_id=7012345678901234567&asset_group_id=7200001234567890123&query_entity=ASSET&page=1&page_size=10" \
  -H "Access-Token: YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json"
```

### Ví dụ Python
```python
import requests

url = "https://business-api.tiktok.com/open_api/v1.3/bc/asset_group/get/"
headers = {
    "Access-Token": "YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}
params = {
    "bc_id": "7012345678901234567",
    "asset_group_id": "7200001234567890123",
    "query_entity": "MEMBER",
    "page": 1,
    "page_size": 10
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

### Phản hồi thành công mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202610231200000104",
  "data": {
    "asset_group": [
      {
        "asset_group_id": "7200001234567890123",
        "asset_group_name": "Agency Client Group A",
        "assets": [
          {
            "asset_id": "7112345678901234567",
            "asset_type": "ADVERTISER"
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

<a id="doc-1749001673406466"></a>
<!-- doc_id: 1749001673406466 -->
## 6. Xóa nhóm tài sản (Delete Asset Groups)

Sử dụng endpoint này để xóa các Nhóm tài sản khỏi Business Center của bạn. Bạn cần có vai trò Quản trị viên (Admin) của Business Center.

> **Lưu ý:** Thao tác xóa Nhóm tài sản sẽ chỉ thu hồi quyền truy cập của các thành viên đối với những tài sản nằm trong Nhóm tài sản đó. Bản thân các tài sản (tài khoản quảng cáo) và người dùng/thành viên trong Business Center sẽ **không** bị xóa khỏi hệ thống.

### Thông tin Endpoint
- **URL:** `https://business-api.tiktok.com/open_api/v1.3/bc/asset_group/delete/`
- **Phương thức:** `POST`

### Header
| Header | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Có | Access Token được cấp quyền xác thực. |
| Content-Type | string | Có | Kiểu nội dung yêu cầu: `application/json`. |

### Tham số Body (Request Body)
| Tham số | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `bc_id` | string | Có | ID của Business Center. |
| `asset_group_ids` | string[] | Có | Danh sách ID các Nhóm tài sản muốn xóa. Hiện tại hệ thống chỉ cho phép truyền vào tối đa 1 ID trong danh sách. |

### Tham số Response
| Trường | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi từ hệ thống. `0` thể hiện thành công. |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Log ID định danh yêu cầu. |
| `data` | object | Dữ liệu trả về sau khi xóa thành công (rỗng). |

### Ví dụ cURL
```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/bc/asset_group/delete/" \
  -H "Access-Token: YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "bc_id": "7012345678901234567",
    "asset_group_ids": [
      "7200001234567890123"
    ]
  }'
```

### Ví dụ Python
```python
import requests

url = "https://business-api.tiktok.com/open_api/v1.3/bc/asset_group/delete/"
headers = {
    "Access-Token": "YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}
payload = {
    "bc_id": "7012345678901234567",
    "asset_group_ids": [
        "7200001234567890123"
    ]
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())
```

### Phản hồi thành công mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202610231200000105",
  "data": {}
}
```
