# Quản lý Business Center (BC Management)
<a id="doc-1737115635521538"></a>
<!-- doc_id: 1737115635521538 -->

TikTok Business Center (BC) là trung tâm quản lý tập trung toàn diện dành cho các tổ chức, doanh nghiệp và đại lý thuộc mọi quy mô, hỗ trợ triển khai các hoạt động tiếp thị, cộng tác làm việc và tiếp cận tệp khách hàng mục tiêu trên TikTok. Bộ API Quản lý Business Center cho phép bạn truy vấn danh sách các tài khoản Business Center mà người dùng có quyền truy cập, cũng như theo dõi nhật ký hoạt động (activity log) chi tiết trong Business Center.

Nhóm API này bao gồm các endpoint sau:
* [Lấy danh sách Business Center](12-bc-management.md#doc-1737115687501826)
* [Lấy nhật ký hoạt động của Business Center](12-bc-management.md#doc-1820767460168705)

---

## Lấy danh sách Business Center (`Get Business Centers`)
<a id="doc-1737115687501826"></a>
<!-- doc_id: 1737115687501826 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/bc/get/`

**Mục đích**: Sử dụng endpoint này để lấy danh sách các Business Center mà người dùng được cấp quyền truy cập, bao gồm ID Business Center, tên, công ty, tiền tệ thanh toán, múi giờ, trạng thái tài khoản và vai trò của người dùng.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền (access token). Xem chi tiết tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (GET query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| bc_id | string | Không bắt buộc | ID Business Center. Nếu không truyền, hệ thống sẽ trả về toàn bộ danh sách Business Center của người dùng. Nếu truyền, chỉ trả về Business Center được chỉ định. |
| page | number | Không bắt buộc | Số trang hiện tại. Khoảng giá trị: ≥ 1. Mặc định: 1. |
| page_size | number | Không bắt buộc | Số bản ghi mỗi trang. Khoảng giá trị: 1-50. Mặc định: 10. |

### Ví dụ

#### cURL
```bash
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/bc/get/?page=1&page_size=50' --header 'Access-Token: YOUR_ACCESS_TOKEN'
```

#### Python
```python
import os
import requests

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", "YOUR_ACCESS_TOKEN")

url = "https://business-api.tiktok.com/open_api/v1.3/bc/get/"
headers = {
    "Access-Token": ACCESS_TOKEN,
}
params = {
    "page": 1,
    "page_size": 10,
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Appendix-Return codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. |
| request_id | string | Mã định danh duy nhất của yêu cầu để theo dõi nhật ký. |
| data | object | Dữ liệu trả về. |
| ↳ list | object[] | Danh sách các Business Center. |
| ↳↳ bc_info | object | Thông tin chi tiết Business Center. |
| ↳↳↳ bc_id | string | ID Business Center. |
| ↳↳↳ name | string | Tên Business Center. |
| ↳↳↳ company | string | Tên công ty đăng ký Business Center. |
| ↳↳↳ currency | string | Đơn vị tiền tệ thanh toán của Business Center. Xem [Appendix-Currency](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1737585839634433). |
| ↳↳↳ registered_area | string | Mã vùng đăng ký kinh doanh của Business Center. Xem [Appendix-Location code](../15-appendix/phu-luc-p1.md#doc-1737585867307010). |
| ↳↳↳ status | string | Trạng thái Business Center: `REVIEWING` (đang xét duyệt), `DENY` (bị từ chối), `ENABLE` (đang hoạt động), `PUNISH` (bị xử phạt/vô hiệu hóa). Xem [Enumeration-Business Center Status](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳↳↳ timezone | string | Múi giờ đặt Business Center. Xem [Appendix-Time Zone](../15-appendix/phu-luc-p1.md#doc-1737586324313089). |
| ↳↳↳ type | string | Loại Business Center: `NORMAL` (thông thường), `DIRECT` (trực tiếp không tự phục vụ), `AGENCY` (đại lý không tự phục vụ), `SELF_SERVICE` (trực tiếp tự phục vụ), `SELF_SERVICE_AGENCY` (đại lý tự phục vụ). |
| ↳↳↳ verification_status | string | Trạng thái xác minh doanh nghiệp của Business Center: `NOT_SUBMITTED`, `REVIEWING`, `VERIFIED`, `FAILED`, `EXPIRED`. |
| ↳↳ user_role | string | Vai trò cơ bản của người dùng trong Business Center: `ADMIN` (quản trị viên), `STANDARD` (thành viên tiêu chuẩn). |
| ↳↳ ext_user_role | object | Vai trò nâng cao mở rộng của người dùng. |
| ↳↳↳ finance_role | string | Vai trò tài chính của người dùng: `MANAGER` (Quản lý tài chính - Finance Manager), `ANALYST` (Chuyên viên phân tích tài chính - Finance Analyst). |
| ↳ page_info | object | Thông tin phân trang. |
| ↳↳ page | number | Số trang hiện tại. |
| ↳↳ page_size | number | Kích thước trang. |
| ↳↳ total_number | number | Tổng số Business Center. |
| ↳↳ total_page | number | Tổng số trang. |

### Ví dụ phản hồi

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202605210639490102360430824C1AE673",
  "data": {
    "list": [
      {
        "bc_info": {
          "bc_id": "7000000000000000000",
          "name": "TikTok Marketing Agency VN",
          "company": "Công ty Cổ phần Truyền thông Số",
          "currency": "VND",
          "registered_area": "VN",
          "status": "ENABLE",
          "timezone": "Asia/Ho_Chi_Minh",
          "type": "AGENCY",
          "verification_status": "VERIFIED"
        },
        "user_role": "ADMIN",
        "ext_user_role": {
          "finance_role": "MANAGER"
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

## Lấy nhật ký hoạt động của Business Center (`Get the activity log of a Business Center`)
<a id="doc-1820767460168705"></a>
<!-- doc_id: 1820767460168705 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/changelog/get/`

**Mục đích**: Sử dụng endpoint này để lấy nhật ký theo dõi các thay đổi và hoạt động quản trị trong Business Center (chẳng hạn như thêm/xóa thành viên, tạo tài khoản quảng cáo, phân bổ quyền truy cập, liên kết TikTok Shop, chia sẻ đối tác).

> [!NOTE]
> Chỉ người dùng có vai trò Quản trị viên (`ADMIN`) trong Business Center mới có quyền truy cập endpoint này.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền (access token). Xem chi tiết tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (GET query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| bc_id | string | Bắt buộc | ID của Business Center cần truy vấn nhật ký. |
| filtering | object | Bắt buộc | Bộ lọc hoạt động (chuỗi JSON đối tượng). |
| ↳ start_date | string | Bắt buộc | Ngày bắt đầu truy vấn nhật ký (`YYYY-MM-DD`). Khoảng thời gian tối đa: 180 ngày trước ngày hiện tại. |
| ↳ end_date | string | Bắt buộc | Ngày kết thúc truy vấn nhật ký (`YYYY-MM-DD`). Khoảng cách giữa `start_date` và `end_date` tối đa 180 ngày. |
| ↳ activity_type | string | Bắt buộc | Loại hoạt động: `ALL` (tất cả), `USER` (thành viên), `ACCOUNT` (tài khoản quảng cáo), `ASSET` (tài sản), `BUSINESS` (cài đặt BC). |
| ↳ operator_ids | string[] | Không bắt buộc | Danh sách ID người thực hiện thao tác. |
| lang | string | Không bắt buộc | Ngôn ngữ mô tả chi tiết nhật ký. Mặc định: `en`. Các mã ngôn ngữ hỗ trợ xem bảng bên dưới. |
| sort_field | string | Không bắt buộc | Trường sắp xếp. Giá trị: `operation_time` (sắp xếp theo thời gian hoạt động). Mặc định: `operation_time`. |
| sort_type | string | Không bắt buộc | Thứ tự sắp xếp: `DESC` (mới nhất trước, mặc định), `ASC` (cũ nhất trước). |
| page | integer | Không bắt buộc | Số trang hiện tại. Khoảng giá trị: ≥ 1. Mặc định: 1. |
| page_size | integer | Không bắt buộc | Số bản ghi mỗi trang. Khoảng giá trị: 1-50. Mặc định: 10. |

### Bảng giá trị ngôn ngữ (`lang`)

| Mã | Ngôn ngữ |
|---|---|
| `vi` | Tiếng Việt |
| `en` | Tiếng Anh (English) |
| `zh` | Tiếng Trung (Chinese) |
| `ja` | Tiếng Nhật (Japanese) |
| `ko` | Tiếng Hàn (Korean) |
| `id` | Tiếng Indonesia |
| `th` | Tiếng Thái |
| `fr` | Tiếng Pháp |
| `de` | Tiếng Đức |
| `es` | Tiếng Tây Ban Nha |
| `pt` | Tiếng Bồ Đào Nha |
| `ru` | Tiếng Nga |

### Ví dụ

#### cURL
```bash
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/changelog/get/?bc_id=7000000000000000000&filtering={"start_date":"2026-05-01","end_date":"2026-05-30","activity_type":"ALL"}&page_size=50' --header 'Access-Token: YOUR_ACCESS_TOKEN'
```

#### Python
```python
import json
import os
import requests

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", "YOUR_ACCESS_TOKEN")
BC_ID = os.environ.get("BC_ID", "7000000000000000000")

url = "https://business-api.tiktok.com/open_api/v1.3/changelog/get/"
headers = {
    "Access-Token": ACCESS_TOKEN,
}
params = {
    "bc_id": BC_ID,
    "filtering": json.dumps({
        "start_date": "2026-05-01",
        "end_date": "2026-05-30",
        "activity_type": "ALL",
    }),
    "page": 1,
    "page_size": 20,
    "lang": "vi",
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Appendix-Return Code](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi từ hệ thống. |
| request_id | string | Mã nhật ký định danh yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ changelog_list | object[] | Danh sách các bản ghi nhật ký thay đổi. |
| ↳↳ time | string | Thời gian diễn ra hoạt động (UTC+0), định dạng `YYYY-MM-DD HH:MM:SS`. |
| ↳↳ activity_type | string | Phân loại hoạt động: `USER`, `ACCOUNT`, `ASSET`, `BUSINESS`. |
| ↳↳ operator_id | string | ID người dùng thực hiện thao tác. |
| ↳↳ activity_log | string | Nội dung mô tả chi tiết hoạt động thay đổi. |
| ↳ page_info | object | Thông tin phân trang. |
| ↳↳ page | number | Trang hiện tại. |
| ↳↳ page_size | number | Kích thước trang. |
| ↳↳ total_number | number | Tổng số bản ghi hoạt động. |
| ↳↳ total_page | number | Tổng số trang. |

### Ví dụ phản hồi

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202605210639490102360430824C1AE673",
  "data": {
    "changelog_list": [
      {
        "activity_type": "USER",
        "activity_log": "Người dùng A đã mời thành viên B vào Business Center với vai trò Standard.",
        "operator_id": "6912345678901234567",
        "time": "2026-05-15 10:20:00"
      },
      {
        "activity_type": "ACCOUNT",
        "activity_log": "Tạo tài khoản quảng cáo mới: Thời Trang Mùa Hè.",
        "operator_id": "6912345678901234567",
        "time": "2026-05-16 14:30:00"
      }
    ],
    "page_info": {
      "total_number": 2,
      "page_size": 20,
      "total_page": 1,
      "page": 1
    }
  }
}
```
