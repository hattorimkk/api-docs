<a id="3-lấy-chi-tiết-chuyển-đổi-tùy-chỉnh"></a>
<a id="4-tạo-chuyển-đổi-tùy-chỉnh"></a>
<a id="5-cập-nhật-chuyển-đổi-tùy-chỉnh"></a>
<a id="6-xóa-chuyển-đổi-tùy-chỉnh"></a>
# Chuyển đổi tùy chỉnh (Custom Conversions)

Tài liệu hướng dẫn và tham chiếu toàn diện về các API Chuyển đổi tùy chỉnh (Custom Conversions) trên TikTok Business API.

---

<a id="doc-1842225078560769"></a>
<!-- doc_id: 1842225078560769 -->
## 1. Tổng quan về Chuyển đổi tùy chỉnh (Custom Conversions Overview)

**Chuyển đổi tùy chỉnh (Custom Conversions)** là giải pháp tiên tiến của TikTok cho phép các nhà quảng cáo định nghĩa chính xác các mục tiêu chuyển đổi bằng cách tận dụng các tín hiệu sẵn có từ Pixel, Events API và ứng dụng (App). Tính năng này hỗ trợ cả Sự kiện tiêu chuẩn (Standard Events) và Sự kiện tùy chỉnh do nhà quảng cáo tự định nghĩa (Custom Events), đem lại sự linh hoạt tối đa để đảm bảo mục tiêu chiến dịch quảng cáo bám sát với kết quả kinh doanh thực tế.

Thông qua bộ API Custom Conversions, bạn có thể:
- Định nghĩa quy tắc chuyển đổi linh hoạt dựa trên URL trang web, giá trị đơn hàng, loại tiền tệ, danh mục sản phẩm, v.v.
- Tối ưu hóa phân phối chiến dịch quảng cáo dựa trên các chuyển đổi chuyên biệt mà không cần phải thay đổi mã nguồn trang web hoặc cập nhật SDK ứng dụng.
- Quản lý vòng đời chuyển đổi: truy vấn danh sách, xem chi tiết, tạo mới, chỉnh sửa tên/mô tả và xóa chuyển đổi tùy chỉnh.

### Danh mục các Endpoint trong nhóm:
1. [Lấy danh sách chuyển đổi tùy chỉnh theo nguồn sự kiện](#2-lấy-danh-sách-chuyển-đổi-tùy-chỉnh-theo-nguồn-sự-kiện): `GET /open_api/v1.3/custom_conversion/list/`
2. [Lấy chi tiết chuyển đổi tùy chỉnh](#3-lấy-chi-tiết-chuyển-đổi-tùy-chỉnh): `GET /open_api/v1.3/custom_conversion/get/`
3. [Tạo chuyển đổi tùy chỉnh](#4-tạo-chuyển-đổi-tùy-chỉnh): `POST /open_api/v1.3/custom_conversion/create/`
4. [Cập nhật chuyển đổi tùy chỉnh](#5-cập-nhật-chuyển-đổi-tùy-chỉnh): `POST /open_api/v1.3/custom_conversion/update/`
5. [Xóa chuyển đổi tùy chỉnh](#6-xóa-chuyển-đổi-tùy-chỉnh): `POST /open_api/v1.3/custom_conversion/delete/`

---

<a id="doc-1842225174460673"></a>
<!-- doc_id: 1842225174460673 -->
<a id="2-lấy-danh-sách-chuyển-đổi-tùy-chỉnh-theo-nguồn-sự-kiện"></a>
## 2. Lấy danh sách chuyển đổi tùy chỉnh theo nguồn sự kiện

Sử dụng endpoint này để truy xuất danh sách các Chuyển đổi tùy chỉnh gắn liền với một nguồn sự kiện cụ thể (mã Pixel hoặc Ứng dụng).

### Thông tin Endpoint
- **URL:** `https://business-api.tiktok.com/open_api/v1.3/custom_conversion/list/`
- **Phương thức:** `GET`

### Header
| Header | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Có | Access Token được cấp quyền xác thực. Xem thêm phần Xác thực. |

### Tham số Query (Query Parameters)
| Tham số | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | Có | ID của tài khoản quảng cáo. |
| `event_source_type` | string | Có | Loại nguồn sự kiện. Các giá trị enum:<ul><li>`PIXEL`: Nguồn sự kiện từ Pixel web.</li><li>`APP`: Nguồn sự kiện từ ứng dụng di động.</li></ul> |
| `event_source_id` | string | Có | ID của nguồn sự kiện:<ul><li>Khi `event_source_type` là `PIXEL`: Chỉ định `pixel_id` (lấy qua endpoint `/pixel/list/`).</li><li>Khi `event_source_type` là `APP`: Chỉ định mã nền tảng ứng dụng `app_platform_id` của một Self Attribution Network (SAN) App (lấy qua `/app/list/` với `self_attribution_enabled` = `true`).</li></ul> |
| `search_keyword` | string | Không | Từ khóa tìm kiếm chuyển đổi tùy chỉnh theo tên (tìm gần đúng - fuzzy match) hoặc theo ID chuyển đổi (tìm chính xác - exact match). |
| `sort_field` | string | Không | Trường dùng để sắp xếp kết quả. Các giá trị enum:<ul><li>`CREATE_TIME`: Thời gian tạo chuyển đổi tùy chỉnh (mặc định).</li><li>`TOTAL_COUNT`: Tổng số lượt chuyển đổi ghi nhận được.</li></ul> |
| `sort_type` | string | Không | Chiều sắp xếp: `DESC` (giảm dần, mặc định), `ASC` (tăng dần). |
| `page` | number | Không | Số trang hiện tại. Dải giá trị: ≥ 1. Mặc định: `1`. |
| `page_size` | number | Không | Kích thước trang. Dải giá trị: 1 - 1.000. Mặc định: `10`. |

### Tham số Response
| Trường | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi từ API (`0` là thành công). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Log ID định danh duy nhất của yêu cầu hệ thống. |
| `data` | object | Dữ liệu trả về. |
| ↳ `custom_conversions` | object[] | Danh sách các chuyển đổi tùy chỉnh. |
| ↳↳ `custom_conversion_id` | string | ID của chuyển đổi tùy chỉnh. |
| ↳↳ `name` | string | Tên chuyển đổi tùy chỉnh. |
| ↳↳ `description` | string | Mô tả chi tiết về chuyển đổi tùy chỉnh. |
| ↳↳ `event_source_type` | string | Loại nguồn sự kiện (`PIXEL` hoặc `APP`). |
| ↳↳ `event_source_id` | string | ID của nguồn sự kiện. |
| ↳↳ `optimization_event` | string | Sự kiện tiêu chuẩn (Standard Event) được ánh xạ để tối ưu hóa. |
| ↳↳ `custom_event_type` | string | Sự kiện tùy chỉnh (Custom Event) nếu có cấu hình. |
| ↳↳ `rules` | object[] | Danh sách các quy tắc lọc chuyển đổi. |
| ↳↳↳ `parameter` | string | Tham số kiểm tra (ví dụ: `URL`, `VALUE`, `CURRENCY`, `CONTENT_TYPE`...). |
| ↳↳↳ `operator` | string | Toán tử so sánh (ví dụ: `CONTAIN`, `EQUAL`, `GTE`...). |
| ↳↳↳ `values` | string[] | Mảng các giá trị điều kiện. |
| ↳↳ `total_conversion_count` | number | Tổng số lượt chuyển đổi đã ghi nhận được. |
| ↳↳ `create_time` | string | Thời gian tạo (định dạng UTC). |
| ↳ `page_info` | object | Thông tin phân trang (`page`, `page_size`, `total_number`, `total_page`). |

### Ví dụ cURL
```bash
curl -X GET "https://business-api.tiktok.com/open_api/v1.3/custom_conversion/list/?advertiser_id=7112345678901234567&event_source_type=PIXEL&event_source_id=C712345678901234567&page=1&page_size=10" \
  -H "Access-Token: YOUR_ACCESS_TOKEN"
```

### Ví dụ Python
```python
import requests

url = "https://business-api.tiktok.com/open_api/v1.3/custom_conversion/list/"
headers = {
    "Access-Token": "YOUR_ACCESS_TOKEN"
}
params = {
    "advertiser_id": "7112345678901234567",
    "event_source_type": "PIXEL",
    "event_source_id": "C712345678901234567",
    "sort_field": "CREATE_TIME",
    "sort_type": "DESC",
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
  "request_id": "202610231300000101",
  "data": {
    "custom_conversions": [
      {
        "custom_conversion_id": "7300001234567890123",
        "name": "High Value Thank You Page",
        "description": "Purchases over 100 USD on confirmation page",
        "event_source_type": "PIXEL",
        "event_source_id": "C712345678901234567",
        "optimization_event": "SHOPPING",
        "rules": [
          {
            "parameter": "URL",
            "operator": "CONTAIN",
            "values": ["/checkout/success", "/thank-you"]
          },
          {
            "parameter": "VALUE",
            "operator": "GTE",
            "values": ["100.00"]
          }
        ],
        "total_conversion_count": 142,
        "create_time": "2026-10-15 08:30:00"
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

<a id="doc-1842225206555074"></a>
<!-- doc_id: 1842225206555074 -->
## 3. Lấy chi tiết chuyển đổi tùy chỉnh

Sử dụng endpoint này để xem cấu hình chi tiết và các quy tắc của một Chuyển đổi tùy chỉnh gắn liền với Pixel hoặc Ứng dụng.

### Thông tin Endpoint
- **URL:** `https://business-api.tiktok.com/open_api/v1.3/custom_conversion/get/`
- **Phương thức:** `GET`

### Header
| Header | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Có | Access Token được cấp quyền xác thực. |

### Tham số Query (Query Parameters)
| Tham số | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | Có | ID của tài khoản quảng cáo. |
| `custom_conversion_id` | string | Có | ID của chuyển đổi tùy chỉnh cần xem chi tiết (lấy từ endpoint danh sách `/custom_conversion/list/`). |
| `event_source_type` | string | Có | Loại nguồn sự kiện: `PIXEL` hoặc `APP`. |
| `event_source_id` | string | Có | ID nguồn sự kiện (`pixel_id` hoặc `app_platform_id`). |

### Tham số Response
| Trường | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi từ API (`0` là thành công). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Log ID định danh duy nhất của yêu cầu. |
| `data` | object | Thông tin chi tiết của chuyển đổi tùy chỉnh. |
| ↳ `custom_conversion_id` | string | ID chuyển đổi tùy chỉnh. |
| ↳ `name` | string | Tên chuyển đổi tùy chỉnh. |
| ↳ `description` | string | Mô tả chuyển đổi tùy chỉnh. |
| ↳ `event_source_type` | string | Loại nguồn sự kiện (`PIXEL` hoặc `APP`). |
| ↳ `event_source_id` | string | ID nguồn sự kiện tương ứng. |
| ↳ `optimization_event` | string | Sự kiện tiêu chuẩn liên kết. |
| ↳ `custom_event_type` | string | Tên sự kiện tùy chỉnh nếu áp dụng. |
| ↳ `rules` | object[] | Danh sách các quy tắc chuyển đổi chi tiết. |
| ↳↳ `parameter` | string | Tên tham số quy tắc. |
| ↳↳ `operator` | string | Toán tử logic. |
| ↳↳ `values` | string[] | Mảng các giá trị so sánh. |
| ↳ `total_conversion_count` | number | Tổng số chuyển đổi đã ghi nhận. |
| ↳ `create_time` | string | Thời điểm tạo chuyển đổi. |

### Ví dụ cURL
```bash
curl -X GET "https://business-api.tiktok.com/open_api/v1.3/custom_conversion/get/?advertiser_id=7112345678901234567&custom_conversion_id=7300001234567890123&event_source_type=PIXEL&event_source_id=C712345678901234567" \
  -H "Access-Token: YOUR_ACCESS_TOKEN"
```

### Ví dụ Python
```python
import requests

url = "https://business-api.tiktok.com/open_api/v1.3/custom_conversion/get/"
headers = {
    "Access-Token": "YOUR_ACCESS_TOKEN"
}
params = {
    "advertiser_id": "7112345678901234567",
    "custom_conversion_id": "7300001234567890123",
    "event_source_type": "PIXEL",
    "event_source_id": "C712345678901234567"
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

### Phản hồi thành công mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202610231301000101",
  "data": {
    "custom_conversion_id": "7300001234567890123",
    "name": "High Value Thank You Page",
    "description": "Purchases over 100 USD on confirmation page",
    "event_source_type": "PIXEL",
    "event_source_id": "C712345678901234567",
    "optimization_event": "SHOPPING",
    "rules": [
      {
        "parameter": "URL",
        "operator": "CONTAIN",
        "values": ["/checkout/success"]
      },
      {
        "parameter": "VALUE",
        "operator": "GTE",
        "values": ["100.00"]
      }
    ],
    "total_conversion_count": 142,
    "create_time": "2026-10-15 08:30:00"
  }
}
```

---

<a id="doc-1842225226006530"></a>
<!-- doc_id: 1842225226006530 -->
## 4. Tạo chuyển đổi tùy chỉnh (Create a Custom Conversion)

Sử dụng endpoint này để tạo mới một Chuyển đổi tùy chỉnh cho Pixel hoặc Ứng dụng.

> **Hạn ngạch và lưu ý:**
> - Bạn có thể tạo tối đa 1.000 Chuyển đổi tùy chỉnh trong một tài khoản quảng cáo.
> - Đối với mỗi Pixel hoặc mỗi Ứng dụng, bạn có thể tạo tối đa 100 Chuyển đổi tùy chỉnh.
> - Tên chuyển đổi không được trùng lặp trong cùng tài khoản quảng cáo và không được đặt trùng tên sự kiện tiêu chuẩn.

### Thông tin Endpoint
- **URL:** `https://business-api.tiktok.com/open_api/v1.3/custom_conversion/create/`
- **Phương thức:** `POST`

### Header
| Header | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Có | Access Token được cấp quyền xác thực. |
| Content-Type | string | Có | Kiểu nội dung yêu cầu: `application/json`. |

### Tham số Body (Request Body)
| Tham số | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | Có | ID của tài khoản quảng cáo. |
| `name` | string | Có | Tên của chuyển đổi tùy chỉnh. Bắt đầu bằng chữ cái, có thể chứa chữ cái, chữ số, dấu cách, dấu gạch dưới hoặc gạch nối. Chiều dài tối đa: 50 ký tự, không chứa emoji. Không trùng tên sự kiện tiêu chuẩn. |
| `description` | string | Không | Mô tả mục đích của chuyển đổi tùy chỉnh. Tối đa 500 ký tự, không chứa emoji. |
| `event_source_type` | string | Có | Loại nguồn sự kiện: `PIXEL` hoặc `APP`. |
| `event_source_id` | string | Có | ID nguồn sự kiện: `pixel_id` hoặc mã nền tảng ứng dụng SAN `app_platform_id`. |
| `optimization_event` | string | Điều kiện | Sự kiện tiêu chuẩn được ánh xạ để tối ưu hóa chiến dịch quảng cáo. Bắt buộc khi `event_source_type` là `PIXEL`. Xem bảng danh sách sự kiện bên dưới. |
| `custom_event_type` | string | Không | Tên sự kiện tùy chỉnh được gắn kèm nếu nguồn sự kiện đã cấu hình sự kiện tùy chỉnh đó. |
| `rules` | object[] | Có | Mảng chi tiết các điều kiện quy tắc chuyển đổi (tối đa từ 1 đến 10 quy tắc). Chỉ các hành động người dùng thỏa mãn toàn bộ các điều kiện này mới được ghi nhận là chuyển đổi tùy chỉnh. |
| ↳ `parameter` | string | Có | Tham số kiểm tra điều kiện. Các giá trị enum: `BRAND`, `CONTENT_CATEGORY`, `CONTENT_ID`, `CONTENT_NAME`, `CONTENT_TYPE`, `CURRENCY`, `DESCRIPTION`, `EVENT_ID`, `NUM_ITEMS`, `PRICE`, `SEARCH_STRING`, `STATUS`, `URL`, `VALUE`. |
| ↳ `operator` | string | Có | Toán tử kiểm tra:<ul><li>Đối với tham số chuỗi (`URL`, `BRAND`, `CONTENT_CATEGORY`, `CONTENT_ID`, `CONTENT_NAME`, `CONTENT_TYPE`, `DESCRIPTION`, `EVENT_ID`, `SEARCH_STRING`, `STATUS`): `CONTAIN` (chứa), `NOT_CONTAIN` (không chứa), `START_WITH` (bắt đầu bằng), `EQUAL` (bằng), `NOT_EQUAL` (khác).</li><li>Đối với số lượng và giá trị (`NUM_ITEMS`, `PRICE`, `VALUE`): `EQUAL` (=), `NOT_EQUAL` (≠), `LT` (<), `GT` (>), `LTE` (≤), `GTE` (≥).</li><li>Đối với loại tiền tệ (`CURRENCY`): `EQUAL`, `NOT_EQUAL`.</li></ul> |
| ↳ `values` | string[] | Có | Mảng giá trị kiểm tra. Đối với chuỗi, mảng chứa tối đa 100 mục, mỗi mục tối đa 100 ký tự. Đối với `NUM_ITEMS`, là số nguyên từ 0 đến 1.000.000.000. Đối với `PRICE`, `VALUE`, là số thực làm tròn 2 chữ số thập phân từ 0.00 đến 1.000.000.000.00. Đối với `CURRENCY`, chọn từ danh sách tiền tệ hợp lệ (như `USD`, `VND`, `EUR`...). |

### Bảng giá trị sự kiện tối ưu hóa (`optimization_event`):

| Loại nguồn sự kiện (`event_source_type`) | Tên sự kiện thực tế | Giá trị enum `optimization_event` |
|---|---|---|
| `PIXEL` | Add Payment Info | `ADD_BILLING` |
| `PIXEL` | Add to Cart | `ON_WEB_CART` |
| `PIXEL` | Add to Wishlist | `ON_WEB_ADD_TO_WISHLIST` |
| `PIXEL` | Complete Registration | `ON_WEB_REGISTER` |
| `PIXEL` | Initiate Checkout | `INITIATE_ORDER` |
| `PIXEL` | Page View | `PAGE_VIEW` |
| `PIXEL` | Place an Order | `ON_WEB_ORDER` |
| `PIXEL` | Purchase (Hoàn tất thanh toán) | `SHOPPING` |
| `PIXEL` | Search | `ON_WEB_SEARCH` |
| `PIXEL` | Submit Application | `SUBMIT_APPLICATION` |
| `PIXEL` | Subscribe | `ON_WEB_SUBSCRIBE` |
| `PIXEL` | View Content | `ON_WEB_DETAIL` |
| `APP` | Add Payment Info | `ADD_PAYMENT_INFO` |
| `APP` | Add to Cart | `IN_APP_CART` |
| `APP` | Checkout | `IN_APP_ORDER` |
| `APP` | Install (Cài đặt ứng dụng) | `INSTALL` |
| `APP` | Launch App | `LAUNCH_APP` |
| `APP` | Login | `LOGIN` |
| `APP` | Purchase | `ACTIVE_PAY` |
| `APP` | Registration | `ACTIVE_REGISTER` |
| `APP` | Subscribe | `SUBSCRIBE` |
| `APP` | View Content | `IN_APP_DETAIL_UV` |

### Bảng một số loại tiền tệ hỗ trợ (`CURRENCY`):
| Currency Value | Currency Name |
|---|---|
| `VND` | Vietnamese Dong |
| `USD` | US Dollar |
| `EUR` | Euro |
| `GBP` | British Pound |
| `SGD` | Singapore Dollar |
| `THB` | Thai Baht |
| `IDR` | Indonesian Rupiah |
| `MYR` | Malaysian Ringgit |
| `PHP` | Philippine Peso |
| `JPY` | Japanese Yen |
| `KRW` | South Korean Won |
| `CNY` | Chinese Yuan Renminbi |
| `AUD` | Australian Dollar |
| `CAD` | Canadian Dollar |
| `BRL` | Brazilian Real |
| `MXN` | Mexican Peso |

### Tham số Response
| Trường | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi từ API (`0` thể hiện thành công). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Log ID định danh duy nhất của yêu cầu. |
| `data` | object | Dữ liệu trả về. |
| ↳ `custom_conversion_id` | string | ID của chuyển đổi tùy chỉnh vừa được khởi tạo thành công. |

### Ví dụ cURL
```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/custom_conversion/create/" \
  -H "Access-Token: YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "advertiser_id": "7112345678901234567",
    "name": "VIP Purchase Over 100 USD",
    "description": "High value customers purchasing on web",
    "event_source_type": "PIXEL",
    "event_source_id": "C712345678901234567",
    "optimization_event": "SHOPPING",
    "rules": [
      {
        "parameter": "URL",
        "operator": "CONTAIN",
        "values": ["/checkout/thankyou"]
      },
      {
        "parameter": "VALUE",
        "operator": "GTE",
        "values": ["100.00"]
      },
      {
        "parameter": "CURRENCY",
        "operator": "EQUAL",
        "values": ["USD"]
      }
    ]
  }'
```

### Ví dụ Python
```python
import requests

url = "https://business-api.tiktok.com/open_api/v1.3/custom_conversion/create/"
headers = {
    "Access-Token": "YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}
payload = {
    "advertiser_id": "7112345678901234567",
    "name": "VIP Purchase Over 100 USD",
    "description": "High value customers purchasing on web",
    "event_source_type": "PIXEL",
    "event_source_id": "C712345678901234567",
    "optimization_event": "SHOPPING",
    "rules": [
        {
            "parameter": "URL",
            "operator": "CONTAIN",
            "values": ["/checkout/thankyou"]
        },
        {
            "parameter": "VALUE",
            "operator": "GTE",
            "values": ["100.00"]
        },
        {
            "parameter": "CURRENCY",
            "operator": "EQUAL",
            "values": ["USD"]
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
  "request_id": "202610231302000101",
  "data": {
    "custom_conversion_id": "7300001234567890123"
  }
}
```

---

<a id="doc-1842225247176705"></a>
<!-- doc_id: 1842225247176705 -->
## 5. Cập nhật chuyển đổi tùy chỉnh (Update a Custom Conversion)

Sử dụng endpoint này để chỉnh sửa tên hoặc mô tả của một Chuyển đổi tùy chỉnh đã tạo.

### Thông tin Endpoint
- **URL:** `https://business-api.tiktok.com/open_api/v1.3/custom_conversion/update/`
- **Phương thức:** `POST`

### Header
| Header | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Có | Access Token được cấp quyền xác thực. |
| Content-Type | string | Có | Kiểu nội dung yêu cầu: `application/json`. |

### Tham số Body (Request Body)
| Tham số | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | Có | ID của tài khoản quảng cáo. |
| `custom_conversion_id` | string | Có | ID của chuyển đổi tùy chỉnh cần cập nhật. |
| `name` | string | Không | Tên mới của chuyển đổi tùy chỉnh. Bắt đầu bằng chữ cái, tối đa 50 ký tự, không chứa emoji và không trùng lặp. |
| `description` | string | Không | Mô tả mới của chuyển đổi tùy chỉnh (tối đa 500 ký tự). |

### Tham số Response
| Trường | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi từ API (`0` là thành công). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Log ID định danh duy nhất của yêu cầu. |
| `data` | object | Dữ liệu trả về (rỗng). |

### Ví dụ cURL
```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/custom_conversion/update/" \
  -H "Access-Token: YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "advertiser_id": "7112345678901234567",
    "custom_conversion_id": "7300001234567890123",
    "name": "High Value Thank You Orders - Q4",
    "description": "Updated description for Q4 holiday campaigns"
  }'
```

### Ví dụ Python
```python
import requests

url = "https://business-api.tiktok.com/open_api/v1.3/custom_conversion/update/"
headers = {
    "Access-Token": "YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}
payload = {
    "advertiser_id": "7112345678901234567",
    "custom_conversion_id": "7300001234567890123",
    "name": "High Value Thank You Orders - Q4",
    "description": "Updated description for Q4 holiday campaigns"
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())
```

### Phản hồi thành công mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202610231303000101",
  "data": {}
}
```

---

<a id="doc-1842225270315074"></a>
<!-- doc_id: 1842225270315074 -->
## 6. Xóa chuyển đổi tùy chỉnh (Delete a Custom Conversion)

Sử dụng endpoint này để xóa một Chuyển đổi tùy chỉnh khi không còn nhu cầu sử dụng.

### Thông tin Endpoint
- **URL:** `https://business-api.tiktok.com/open_api/v1.3/custom_conversion/delete/`
- **Phương thức:** `POST`

### Header
| Header | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Có | Access Token được cấp quyền xác thực. |
| Content-Type | string | Có | Kiểu nội dung yêu cầu: `application/json`. |

### Tham số Body (Request Body)
| Tham số | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | Có | ID của tài khoản quảng cáo. |
| `custom_conversion_id` | string | Có | ID của chuyển đổi tùy chỉnh cần xóa. |

### Tham số Response
| Trường | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi từ API (`0` là thành công). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Log ID định danh duy nhất của yêu cầu. |
| `data` | object | Dữ liệu trả về (rỗng). |

### Ví dụ cURL
```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/custom_conversion/delete/" \
  -H "Access-Token: YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "advertiser_id": "7112345678901234567",
    "custom_conversion_id": "7300001234567890123"
  }'
```

### Ví dụ Python
```python
import requests

url = "https://business-api.tiktok.com/open_api/v1.3/custom_conversion/delete/"
headers = {
    "Access-Token": "YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}
payload = {
    "advertiser_id": "7112345678901234567",
    "custom_conversion_id": "7300001234567890123"
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())
```

### Phản hồi thành công mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202610231304000101",
  "data": {}
}
```
