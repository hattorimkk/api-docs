# Báo cáo BC (BC Reporting)

Nhóm API Báo cáo Business Center (BC Reporting) cho phép doanh nghiệp và nhà phát triển tra cứu các thuộc tính tổng hợp về đơn vị tiền tệ và khu vực đăng ký của các tài khoản quảng cáo trong Business Center. Các giá trị thuộc tính này được sử dụng làm bộ lọc trong các báo cáo phân tích hiệu suất tổng hợp cấp Business Center.

| Endpoint | Method | Đường dẫn | Mục đích |
|---|---|---|---|
| Tổng quan báo cáo Business Center | - | - | Giới thiệu hệ thống báo cáo phân tích hiệu suất cấp Business Center |
| Lấy tiền tệ và khu vực đăng ký của tài khoản quảng cáo | `GET` | `/open_api/v1.3/bc/advertiser/attribute/` | Lấy danh sách mã tiền tệ và mã khu vực đăng ký để làm bộ lọc báo cáo |

---

## Tổng quan báo cáo Business Center (`BC Reporting`)
<a id="doc-1775752272288770"></a>
<!-- doc_id: 1775752272288770 -->

Business Center là trung tâm điều hành tập trung cho các tổ chức thuộc mọi quy mô nhằm kích hoạt các hoạt động tiếp thị và tiếp cận đối tượng mong muốn một cách cộng tác trên TikTok. Nhóm API BC Reporting cho phép bạn lấy các giá trị được hỗ trợ của các bộ lọc tiền tệ và nơi đăng ký có thể được sử dụng trong báo cáo Business Center cho một Business Center cụ thể.

Để tìm hiểu về các chiều dữ liệu (dimensions), chỉ số (metrics), bộ lọc và trường hợp sử dụng cho báo cáo Business Center, vui lòng tham khảo tài liệu [Báo cáo Business Center](../09-marketing-api/bao-cao-p3.md#doc-1775747432712194).

Nhóm này bao gồm endpoint:
- [Lấy tiền tệ và khu vực đăng ký của tài khoản quảng cáo](21-bc-reporting.md#doc-1775752357139457)

---

## Lấy tiền tệ và khu vực đăng ký của tài khoản quảng cáo (`Get currencies and registration areas for ad accounts`)
<a id="doc-1775752357139457"></a>
<!-- doc_id: 1775752357139457 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/bc/advertiser/attribute/`

**Mục đích**: Lấy danh sách các đơn vị tiền tệ và nơi đăng ký của tất cả các tài khoản quảng cáo thuộc một Business Center. Bạn có thể truyền các giá trị tiền tệ và khu vực đăng ký nhận được vào các trường lọc `registered_area` và `currency_of_account` trong [Báo cáo Business Center](../09-marketing-api/bao-cao-p4.md#doc-1775747484045313).

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Có | Mã truy cập đã được ủy quyền. Xem [Xác thực](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (GET: query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `bc_id` | string | Có | ID của Business Center. Để lấy danh sách các Business Center mà bạn có quyền truy cập, sử dụng [/bc/get/](12-bc-management.md#doc-1737115687501826). |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Giá trị `0` là thành công. Xem [Phụ lục mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Mã log định danh duy nhất của yêu cầu API. |
| `data` | object | Dữ liệu trả về. |
| ↳ `currencies` | string[] | Danh sách các mã tiền tệ của các tài khoản quảng cáo trong Business Center (ví dụ: `["USD", "VND"]`). |
| ↳ `region_codes` | string[] | Danh sách các mã vị trí quốc gia/khu vực đăng ký của các tài khoản quảng cáo trong Business Center (ví dụ: `["VN", "US", "SG"]`). |

### Ví dụ

#### cURL
```bash
curl -X GET "https://business-api.tiktok.com/open_api/v1.3/bc/advertiser/attribute/?bc_id=7123456789012345678" \
  -H "Access-Token: ACCESS_TOKEN"
```

#### Python
```python
import requests

ACCESS_TOKEN = "your_access_token"
BC_ID = "7123456789012345678"

url = "https://business-api.tiktok.com/open_api/v1.3/bc/advertiser/attribute/"
headers = {"Access-Token": ACCESS_TOKEN}
params = {"bc_id": BC_ID}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

#### Phản hồi mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202410231500000701111222333444555",
  "data": {
    "currencies": [
      "USD",
      "VND"
    ],
    "region_codes": [
      "VN",
      "US",
      "SG",
      "JP",
      "AU"
    ]
  }
}
```
