# Nguồn sự kiện Catalog (Catalog Event Sources)

Nhóm API Nguồn sự kiện Catalog (Catalog Event Sources) cho phép bạn quản lý việc liên kết và hủy liên kết giữa danh mục sản phẩm (Catalog) trong Business Center với các nguồn sự kiện (Pixel website hoặc sự kiện ứng dụng di động). Việc liên kết nguồn sự kiện giúp thuật toán TikTok theo dõi chính xác các hành vi của người dùng (như xem sản phẩm, thêm vào giỏ hàng, mua hàng), từ đó tối ưu hóa phân phối và triển khai các chiến dịch quảng cáo mua sắm động (Dynamic Showcase Ads) hoặc nhắm mục tiêu lại (Retargeting). Tài liệu này cung cấp chi tiết kỹ thuật cho toàn bộ các endpoint thuộc nhóm nguồn sự kiện Catalog trong phiên bản v1.3.

## Mục lục các endpoint

| Endpoint | Phương thức | Mục đích |
|---|---|---|
| [/catalog/eventsource/bind/](26-catalog-event-sources.md#doc-1740492491200513) | `POST` | Liên kết nguồn sự kiện (Pixel website hoặc App ID) với Catalog |
| [/catalog/eventsource/unbind/](26-catalog-event-sources.md#doc-1740492512449538) | `POST` | Hủy liên kết nguồn sự kiện khỏi Catalog |
| [/catalog/eventsource_bind/get/](26-catalog-event-sources.md#doc-1740492531343362) | `GET` | Lấy danh sách các nguồn sự kiện đang liên kết với Catalog |

---

## Tổng quan Nguồn sự kiện Catalog (`Catalog Event Sources`)
<a id="doc-1740132891438082"></a>
<!-- doc_id: 1740132891438082 -->

> Đường dẫn: API Reference > Catalog Event Sources

> [!IMPORTANT]
> Bằng việc sử dụng các endpoint của Catalog API, bạn đồng ý với [Điều khoản Danh mục sản phẩm (Product Catalog Terms)](https://ads.tiktok.com/i18n/official/article?aid=6765817026859499525) và xác nhận tuân thủ [Chính sách quảng cáo của TikTok (TikTok Advertising Policies)](https://ads.tiktok.com/help/article?aid=6685586866860720134). Vui lòng xem xét kỹ các chính sách này và đảm bảo rằng các sản phẩm tải lên danh mục không vi phạm quy định.

Danh mục sản phẩm (Catalog) là tài sản lưu trữ thông tin về các mặt hàng bạn muốn quảng bá trên TikTok. Sử dụng Catalog là giải pháp lý tưởng cho các nhà bán lẻ trực tuyến muốn tạo và quản lý quảng cáo cho nhiều mặt hàng cùng lúc một cách hiệu quả.

Nguồn sự kiện (Event Source) là sự kiện ứng dụng di động (App Event) hoặc sự kiện trang web (Website Pixel Event) mà bạn liên kết với một Catalog trong Business Center (BC). Nhóm Catalog Event Sources API hỗ trợ các chức năng:
- Liên kết nguồn sự kiện với Catalog.
- Hủy liên kết nguồn sự kiện khỏi Catalog.
- Tra cứu thông tin liên kết nguồn sự kiện của một Catalog.

Xem thêm [Tổng quan (Overview)](../09-marketing-api/catalog.md#doc-1754263078057986) và [Hướng dẫn (Guides)](../09-marketing-api/catalog.md#doc-1754263100123137) để tìm hiểu khái niệm, lợi ích và cách thức quản lý Catalog.

Nhóm tài liệu này bao gồm các endpoint sau:
* [Liên kết nguồn sự kiện với Catalog (Bind an event source to a catalog)](26-catalog-event-sources.md#doc-1740492491200513)
* [Hủy liên kết nguồn sự kiện khỏi Catalog (Unbind an event source from a catalog)](26-catalog-event-sources.md#doc-1740492512449538)
* [Lấy thông tin liên kết nguồn sự kiện của Catalog (Get event source binding info of a catalog)](26-catalog-event-sources.md#doc-1740492531343362)

---

## Liên kết nguồn sự kiện với Catalog (`Bind an event source to a catalog`)
<a id="doc-1740492491200513"></a>
<!-- doc_id: 1740492491200513 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/catalog/eventsource/bind/`

**Mục đích**: Liên kết sự kiện ứng dụng (App Event) hoặc sự kiện website (Pixel) với một Catalog thuộc Business Center.

Bạn có thể liên kết một mã Pixel, một App ID hoặc đồng thời cả hai vào cùng một Catalog.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Bắt buộc | Access token đã được cấp quyền. Chi tiết xem tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| `Content-Type` | string | Bắt buộc | Định dạng nội dung của request. Giá trị cho phép: `"application/json"`. |

### Tham số (POST: JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | Bắt buộc | ID tài khoản quảng cáo. |
| `bc_id` | string | Bắt buộc | ID của Business Center quản lý Catalog. |
| `catalog_id` | string | Bắt buộc | ID danh mục sản phẩm (Catalog ID). |
| `app_id` | string | Không bắt buộc | ID ứng dụng di động. Bạn có thể tìm thấy App ID bằng cách vào mục **Tài sản (Assets)** > **Sự kiện (Events)** > **Sự kiện ứng dụng (App Events)** trong TikTok Ads Manager. Bạn cần chỉ định ít nhất `app_id` hoặc `pixel_code`. |
| `pixel_code` | string | Không bắt buộc | Mã Pixel trang web. Bạn có thể tìm thấy mã Pixel bằng cách vào mục **Tài sản (Assets)** > **Sự kiện (Events)** > **Sự kiện web (Website Events)** trong TikTok Ads Manager. Bạn cần chỉ định ít nhất `app_id` hoặc `pixel_code`. |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Danh sách đầy đủ mã lỗi xem tại [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi. Chi tiết xem tại [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `request_id` | string | ID nhật ký duy nhất định danh request. |
| `data` | object | Dữ liệu trả về (mảng rỗng `{}`). |

### Ví dụ gọi API

#### cURL
```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/catalog/eventsource/bind/' \
--header 'Access-Token: your_access_token_here' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id": "7000000000000000001",
    "bc_id": "7100000000000000001",
    "catalog_id": "7200000000000000001",
    "pixel_code": "C1234567890ABCDEF"
}'
```

#### Python
```python
import requests

ACCESS_TOKEN = "your_access_token_here"

url = "https://business-api.tiktok.com/open_api/v1.3/catalog/eventsource/bind/"
headers = {
    "Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}
payload = {
    "advertiser_id": "7000000000000000001",
    "bc_id": "7100000000000000001",
    "catalog_id": "7200000000000000001",
    "pixel_code": "C1234567890ABCDEF"
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())
```

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20231023120000010188059082081",
  "data": {}
}
```

---

## Hủy liên kết nguồn sự kiện khỏi Catalog (`Unbind an event source from a catalog`)
<a id="doc-1740492512449538"></a>
<!-- doc_id: 1740492512449538 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/catalog/eventsource/unbind/`

**Mục đích**: Hủy liên kết một sự kiện ứng dụng hoặc sự kiện website khỏi một Catalog trong Business Center.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Bắt buộc | Access token đã được cấp quyền. Chi tiết xem tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| `Content-Type` | string | Bắt buộc | Định dạng nội dung của request. Giá trị cho phép: `"application/json"`. |

### Tham số (POST: JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | Bắt buộc | ID tài khoản quảng cáo. |
| `bc_id` | string | Bắt buộc | ID của Business Center quản lý Catalog. |
| `catalog_id` | string | Bắt buộc | ID danh mục sản phẩm (Catalog ID). |
| `app_id` | string | Không bắt buộc | ID ứng dụng di động muốn hủy liên kết. |
| `pixel_code` | string | Không bắt buộc | Mã Pixel trang web muốn hủy liên kết. |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Danh sách đầy đủ mã lỗi xem tại [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi. Chi tiết xem tại [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `request_id` | string | ID nhật ký duy nhất định danh request. |
| `data` | object | Dữ liệu trả về (mảng rỗng `{}`). |

### Ví dụ gọi API

#### cURL
```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/catalog/eventsource/unbind/' \
--header 'Access-Token: your_access_token_here' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id": "7000000000000000001",
    "bc_id": "7100000000000000001",
    "catalog_id": "7200000000000000001",
    "pixel_code": "C1234567890ABCDEF"
}'
```

#### Python
```python
import requests

ACCESS_TOKEN = "your_access_token_here"

url = "https://business-api.tiktok.com/open_api/v1.3/catalog/eventsource/unbind/"
headers = {
    "Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}
payload = {
    "advertiser_id": "7000000000000000001",
    "bc_id": "7100000000000000001",
    "catalog_id": "7200000000000000001",
    "pixel_code": "C1234567890ABCDEF"
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())
```

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20231023120000010188059082082",
  "data": {}
}
```

---

## Lấy thông tin liên kết nguồn sự kiện của Catalog (`Get event source binding info of a catalog`)
<a id="doc-1740492531343362"></a>
<!-- doc_id: 1740492531343362 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/catalog/eventsource_bind/get/`

**Mục đích**: Lấy thông tin về các nguồn sự kiện ứng dụng hoặc trang web đang được liên kết với một Catalog trong Business Center.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Bắt buộc | Access token đã được cấp quyền. Chi tiết xem tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| `Content-Type` | string | Không bắt buộc | Định dạng nội dung: `"application/json"`. |

### Tham số (GET: query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `bc_id` | string | Bắt buộc | ID của Business Center. |
| `catalog_id` | string | Bắt buộc | ID danh mục sản phẩm (Catalog ID). |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Chi tiết xem tại [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi. |
| `request_id` | string | ID duy nhất định danh request. |
| `data` | object | Dữ liệu trả về. |
| ↳ `catalog_id` | integer | ID của danh mục sản phẩm. |
| ↳ `event_sources` | object[] | Danh sách các nguồn sự kiện được liên kết. Mỗi nguồn sự kiện là một đối tượng. |
| ↳↳ `event_source_name` | string | Tên của nguồn sự kiện. |
| ↳↳ `app_id` | string | ID ứng dụng di động (nếu có). |
| ↳↳ `pixel_code` | string | Mã Pixel trang web (nếu có). |

### Ví dụ

#### cURL
```bash
curl -G --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/catalog/eventsource_bind/get/' \
--header 'Access-Token: your_access_token_here' \
--data-urlencode 'bc_id=7100000000000000001' \
--data-urlencode 'catalog_id=7200000000000000001'
```

#### Python
```python
import requests

ACCESS_TOKEN = "your_access_token_here"
BC_ID = "7100000000000000001"
CATALOG_ID = "7200000000000000001"

url = "https://business-api.tiktok.com/open_api/v1.3/catalog/eventsource_bind/get/"
headers = {"Access-Token": ACCESS_TOKEN}
params = {
    "bc_id": BC_ID,
    "catalog_id": CATALOG_ID
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20231023120000010188059082083",
  "data": {
    "catalog_id": "7200000000000000001",
    "event_sources": [
      {
        "app_id": "com.example.app",
        "event_source_name": "My_Ecom_App",
        "pixel_code": null
      },
      {
        "app_id": null,
        "event_source_name": "My_Web_Store_Pixel",
        "pixel_code": "C1234567890ABCDEF"
      }
    ]
  }
}
```
