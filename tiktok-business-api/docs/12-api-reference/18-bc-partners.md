# Đối tác BC (BC Partners)

Nhóm API Đối tác Business Center (BC Partners) cho phép bạn quản lý các quan hệ đối tác giữa các Business Center và các tài sản được chia sẻ giữa các đối tác trên nền tảng TikTok. Thông qua các endpoint này, quản trị viên (Admin) của Business Center có thể tra cứu danh sách đối tác, thiết lập quan hệ đối tác mới, phân quyền chia sẻ tài sản (tài khoản quảng cáo, tài khoản TikTok, danh mục sản phẩm, pixel, tệp khách hàng tiềm năng), hủy chia sẻ tài sản hoặc xóa đối tác.

| Endpoint | Method | Đường dẫn | Mục đích |
|---|---|---|---|
| Tổng quan đối tác Business Center | - | - | Giới thiệu hệ sinh thái đối tác và quản lý tài sản chia sẻ trong Business Center |
| Lấy danh sách đối tác của Business Center | `GET` | `/open_api/v1.3/bc/partner/get/` | Tra cứu danh sách các Business Center đối tác |
| Thêm đối tác vào Business Center | `POST` | `/open_api/v1.3/bc/partner/add/` | Thiết lập quan hệ đối tác và phân quyền chia sẻ tài sản |
| Xóa đối tác khỏi Business Center | `POST` | `/open_api/v1.3/bc/partner/delete/` | Xóa liên kết đối tác khỏi Business Center |
| Hủy chia sẻ tài sản với đối tác | `POST` | `/open_api/v1.3/bc/partner/asset/delete/` | Thu hồi quyền truy cập tài sản đã chia sẻ với đối tác |
| Lấy danh sách tài sản của đối tác | `GET` | `/open_api/v1.3/bc/partner/asset/get/` | Tra cứu các tài sản đã chia sẻ cho đối tác hoặc nhận từ đối tác |

---

## Tổng quan đối tác Business Center (`BC Partners`)
<a id="doc-1739432611975170"></a>
<!-- doc_id: 1739432611975170 -->

Business Center là trung tâm điều hành tập trung dành cho các doanh nghiệp và tổ chức thuộc mọi quy mô, giúp triển khai các hoạt động tiếp thị và tiếp cận đối tượng mục tiêu một cách cộng tác trên TikTok. Nhóm API BC Partners giúp bạn quản lý các đối tác và các tài sản mà bạn chia sẻ với đối tác trong Business Center.

Nhóm này bao gồm các endpoint sau:
- [Lấy danh sách đối tác của Business Center](18-bc-partners.md#doc-1739662727395330): Lấy danh sách các đối tác hiện có.
- [Thêm đối tác vào Business Center](18-bc-partners.md#doc-1739662756510721): Thêm một đối tác mới và tùy chọn chia sẻ tài sản.
- [Xóa đối tác khỏi Business Center](18-bc-partners.md#doc-1739662779301890): Xóa hoàn toàn quan hệ đối tác.
- [Hủy chia sẻ tài sản với đối tác](18-bc-partners.md#doc-1739662800930817): Hủy quyền truy cập của đối tác vào các tài sản cụ thể.
- [Lấy danh sách tài sản của đối tác](18-bc-partners.md#doc-1739662828320769): Xem danh sách tài sản bạn chia sẻ với đối tác hoặc đối tác chia sẻ cho bạn.

> [!NOTE]
> Bạn phải có vai trò Quản trị viên (`Admin`) của Business Center để thực hiện các thao tác quản lý đối tác và chia sẻ tài sản.

---

## Lấy danh sách đối tác của Business Center (`Get the partners of a BC`)
<a id="doc-1739662727395330"></a>
<!-- doc_id: 1739662727395330 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/bc/partner/get/`

**Mục đích**: Lấy danh sách các đối tác của một Business Center. Bạn cần là Quản trị viên (`Admin`) của Business Center.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Có | Mã truy cập đã được ủy quyền. Xem [Xác thực](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (GET: query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `bc_id` | string | Có | ID của Business Center. |
| `page` | number | Không | Số trang dữ liệu hiện tại. Mặc định: `1`. |
| `page_size` | number | Không | Số lượng bản ghi mỗi trang. Mặc định: `10`. |
| `filtering` | object | Không | Bộ lọc theo tên đối tác. Truyền dưới dạng chuỗi JSON object (ví dụ: `filtering={"name":"Agency"}`). |
| ↳ `name` | string | Không | Từ khóa tên đối tác để lọc kết quả. |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Giá trị `0` là thành công. Xem [Phụ lục mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Mã log định danh duy nhất của yêu cầu API. |
| `data` | object | Dữ liệu trả về. |
| ↳ `list` | object[] | Danh sách các đối tác. |
| ↳↳ `bc_id` | string | ID của Business Center đối tác. |
| ↳↳ `bc_name` | string | Tên của Business Center đối tác. |
| ↳ `page_info` | object | Thông tin phân trang. |
| ↳↳ `page` | number | Trang hiện tại. |
| ↳↳ `page_size` | number | Số lượng bản ghi mỗi trang. |
| ↳↳ `total_number` | number | Tổng số lượng đối tác. |
| ↳↳ `total_page` | number | Tổng số trang. |

### Ví dụ

#### cURL
```bash
curl -X GET "https://business-api.tiktok.com/open_api/v1.3/bc/partner/get/?bc_id=7123456789012345678&page=1&page_size=10&filtering=%7B%22name%22%3A%22Agency%22%7D" \
  -H "Access-Token: ACCESS_TOKEN"
```

#### Python
```python
import json
import requests

ACCESS_TOKEN = "your_access_token"
BC_ID = "7123456789012345678"

url = "https://business-api.tiktok.com/open_api/v1.3/bc/partner/get/"
headers = {"Access-Token": ACCESS_TOKEN}
params = {
    "bc_id": BC_ID,
    "page": 1,
    "page_size": 10,
    "filtering": json.dumps({"name": "Agency"})
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

#### Phản hồi mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202410231500000401111222333444555",
  "data": {
    "list": [
      {
        "bc_id": "7123456789012345679",
        "bc_name": "Đối tác Tiếp thị Toàn cầu"
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

## Thêm đối tác vào Business Center (`Add a partner to a BC`)
<a id="doc-1739662756510721"></a>
<!-- doc_id: 1739662756510721 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/bc/partner/add/`

**Mục đích**: Thêm một đối tác mới vào Business Center và tùy chọn chia sẻ tài sản của bạn cho đối tác đó. Business Center chỉ có thể chia sẻ các tài sản thuộc quyền sở hữu của mình. Bạn cần có vai trò Quản trị viên (`Admin`) của Business Center.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Có | Mã truy cập đã được ủy quyền. Xem [Xác thực](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| `Content-Type` | string | Có | Định dạng nội dung yêu cầu. Giá trị cho phép: `application/json`. |

### Tham số (POST: JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `bc_id` | string | Có | ID của Business Center của bạn. |
| `partner_id` | string | Có | ID của Business Center cần thêm làm đối tác. |
| `asset_type` | string | Không | Loại tài sản muốn chia sẻ với đối tác. Enum: `ADVERTISER` (tài khoản quảng cáo). |
| `asset_ids` | string[] | Không | Danh sách ID tài sản muốn chia sẻ với đối tác. Tối đa 50 ID. |
| `advertiser_role` | string | Không | Vai trò tài khoản quảng cáo gán cho đối tác (chỉ áp dụng khi `asset_type` là `ADVERTISER`).<br><br>**Enum**:<br>• `ADMIN`: Quản trị viên (quản lý tài chính, cài đặt, quyền, tạo và sửa chiến dịch, xem báo cáo).<br>• `OPERATOR`: Nhà vận hành (quản lý tài chính, tạo và sửa chiến dịch, xem báo cáo).<br>• `ANALYST`: Nhà phân tích (chỉ xem quảng cáo và dữ liệu hiệu suất).<br>**Mặc định**: `ANALYST`. |

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
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/bc/partner/add/" \
  -H "Access-Token: ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "bc_id": "7123456789012345678",
    "partner_id": "7123456789012345679",
    "asset_type": "ADVERTISER",
    "asset_ids": ["6789012345678901234"],
    "advertiser_role": "OPERATOR"
  }'
```

#### Phản hồi mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20241023150000040222333444555666",
  "data": {}
}
```

---

## Xóa đối tác khỏi Business Center (`Delete a partner from a BC`)
<a id="doc-1739662779301890"></a>
<!-- doc_id: 1739662779301890 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/bc/partner/delete/`

**Mục đích**: Xóa một đối tác khỏi Business Center. Toàn bộ các tài sản được chia sẻ giữa hai bên sẽ ngừng hiệu lực. Bạn cần có vai trò Quản trị viên (`Admin`) của Business Center.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Có | Mã truy cập đã được ủy quyền. Xem [Xác thực](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| `Content-Type` | string | Có | Định dạng nội dung yêu cầu. Giá trị cho phép: `application/json`. |

### Tham số (POST: JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `bc_id` | string | Có | ID của Business Center. |
| `partner_id` | string | Có | ID của Business Center đối tác cần xóa. |

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
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/bc/partner/delete/" \
  -H "Access-Token: ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "bc_id": "7123456789012345678",
    "partner_id": "7123456789012345679"
  }'
```

#### Phản hồi mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20241023150000040333444555666777",
  "data": {}
}
```

---

## Hủy chia sẻ tài sản với đối tác (`Cancel the sharing of assets`)
<a id="doc-1739662800930817"></a>
<!-- doc_id: 1739662800930817 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/bc/partner/asset/delete/`

**Mục đích**: Hủy quyền truy cập hoặc thu hồi các tài sản cụ thể mà bạn đã chia sẻ với một đối tác trong Business Center. Bạn cần có vai trò Quản trị viên (`Admin`) của Business Center.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Có | Mã truy cập đã được ủy quyền. Xem [Xác thực](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| `Content-Type` | string | Có | Định dạng nội dung yêu cầu. Giá trị cho phép: `application/json`. |

### Tham số (POST: JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `bc_id` | string | Có | ID của Business Center. |
| `partner_id` | string | Có | ID của Business Center đối tác. |
| `asset_type` | string | Có | Loại tài sản cần hủy chia sẻ.<br><br>**Enum**:<br>• `ADVERTISER`: Tài khoản quảng cáo.<br>• `TT_ACCOUNT`: Tài khoản TikTok (tương ứng với danh tính `BC_AUTH_TT`). Xem [Danh tính](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1738958351620097).<br>• `TIKTOK_SHOP`: Cửa hàng TikTok Shop.<br>• `CATALOG`: Danh mục sản phẩm.<br>• `LEAD`: Thư viện biểu mẫu khách hàng tiềm năng.<br>• `PIXEL`: TikTok Pixel.<br>• `STOREFRANT`: *(Đã ngừng hỗ trợ)*. |
| `asset_ids` | string[] | Có | Danh sách ID tài sản muốn hủy chia sẻ:<br>• Nếu `asset_type` là `ADVERTISER`: Danh sách ID tài khoản quảng cáo (`advertiser_id`).<br>• Nếu `asset_type` là `TT_ACCOUNT`: Danh sách ID tài khoản TikTok trong Business Center.<br>• Nếu `asset_type` là `TIKTOK_SHOP`: Danh sách ID TikTok Shop.<br>• Nếu `asset_type` là `CATALOG`: Danh sách ID danh mục sản phẩm.<br>• Nếu `asset_type` là `LEAD`: Danh sách ID thư viện biểu mẫu (hiện tại chỉ hỗ trợ 1 ID; tra cứu qua [/page/library/get/](48-leads.md#doc-1740029915327489)).<br>• Nếu `asset_type` là `PIXEL`: Danh sách ID Pixel. |

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
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/bc/partner/asset/delete/" \
  -H "Access-Token: ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "bc_id": "7123456789012345678",
    "partner_id": "7123456789012345679",
    "asset_type": "ADVERTISER",
    "asset_ids": ["6789012345678901234"]
  }'
```

#### Phản hồi mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20241023150000040444555666777888",
  "data": {}
}
```

---

## Lấy danh sách tài sản của đối tác (`Get the assets of a partner`)
<a id="doc-1739662828320769"></a>
<!-- doc_id: 1739662828320769 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/bc/partner/asset/get/`

**Mục đích**: Lấy danh sách các tài sản mà bạn đã chia sẻ cho đối tác hoặc các tài sản mà đối tác đã chia sẻ cho bạn trong Business Center. Bạn cần có vai trò Quản trị viên (`Admin`) của Business Center.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Có | Mã truy cập đã được ủy quyền. Xem [Xác thực](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (GET: query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `bc_id` | string | Có | ID của Business Center. |
| `partner_id` | string | Có | ID của Business Center đối tác. |
| `asset_type` | string | Có | Loại tài sản cần tra cứu.<br><br>**Enum**:<br>• `ADVERTISER`: Tài khoản quảng cáo.<br>• `CATALOG`: Danh mục sản phẩm. |
| `share_type` | string | Có | Hướng chia sẻ tài sản.<br><br>**Enum**:<br>• `SHARED`: Tài sản mà đối tác chia sẻ cho bạn.<br>• `SHARING`: Tài sản mà bạn chia sẻ cho đối tác. |
| `filtering` | object | Không | Bộ lọc tìm kiếm theo từ khóa. Truyền dưới dạng chuỗi JSON object (ví dụ: `filtering={"keyword":"Campaign"}`). |
| ↳ `keyword` | string | Không | Từ khóa tên tài sản cần lọc. |
| `page` | number | Không | Số trang dữ liệu hiện tại. Mặc định: `1`. |
| `page_size` | number | Không | Số lượng bản ghi mỗi trang. Mặc định: `10`. |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Giá trị `0` là thành công. Xem [Phụ lục mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Mã log định danh duy nhất của yêu cầu API. |
| `data` | object | Dữ liệu trả về. |
| ↳ `list` | object[] | Danh sách tài sản đối tác. |
| ↳↳ `asset_id` | string | ID của tài sản (nếu `asset_type` là `ADVERTISER` thì đây là ID nhà quảng cáo; nếu là `CATALOG` thì đây là ID danh mục). |
| ↳↳ `asset_type` | string | Loại tài sản (`ADVERTISER`, `CATALOG`). |
| ↳↳ `asset_name` | string | Tên của tài sản. |
| ↳↳ `advertiser_role` | string | *(Chỉ trả về khi `asset_type` là `ADVERTISER`)*. Vai trò tài khoản quảng cáo (`ADMIN`, `OPERATOR`, `ANALYST`). |
| ↳↳ `advertiser_account_type` | string | Loại tài khoản quảng cáo (`RESERVATION`: tài khoản đặt chỗ trước, `AUCTION`: tài khoản đấu giá). |
| ↳↳ `catalog_role` | string | *(Chỉ trả về khi `asset_type` là `CATALOG`)*. Quyền hạn trên danh mục sản phẩm (`ADMIN`: quyền quản trị, `AD_PROMOTE`: chỉ dùng để quảng bá). |
| ↳ `page_info` | object | Thông tin phân trang. |
| ↳↳ `page` | number | Trang hiện tại. |
| ↳↳ `page_size` | number | Số lượng bản ghi mỗi trang. |
| ↳↳ `total_number` | number | Tổng số lượng tài sản. |
| ↳↳ `total_page` | number | Tổng số trang kết quả. |

### Ví dụ

#### cURL
```bash
curl -X GET "https://business-api.tiktok.com/open_api/v1.3/bc/partner/asset/get/?bc_id=7123456789012345678&partner_id=7123456789012345679&asset_type=ADVERTISER&share_type=SHARING&page=1&page_size=10" \
  -H "Access-Token: ACCESS_TOKEN"
```

#### Python
```python
import requests

ACCESS_TOKEN = "your_access_token"
BC_ID = "7123456789012345678"
PARTNER_ID = "7123456789012345679"

url = "https://business-api.tiktok.com/open_api/v1.3/bc/partner/asset/get/"
headers = {"Access-Token": ACCESS_TOKEN}
params = {
    "bc_id": BC_ID,
    "partner_id": PARTNER_ID,
    "asset_type": "ADVERTISER",
    "share_type": "SHARING",
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
  "request_id": "20241023150000040555666777888999",
  "data": {
    "list": [
      {
        "advertiser_account_type": "AUCTION",
        "advertiser_role": "OPERATOR",
        "asset_id": "6789012345678901234",
        "asset_name": "Tài khoản Quảng cáo TikTok Shop VN",
        "asset_type": "ADVERTISER"
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
