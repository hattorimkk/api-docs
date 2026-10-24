# Feed Catalog (Catalog Feeds)

Nguồn cấp dữ liệu danh mục (Catalog Feeds) cho phép bạn tự động hóa việc đồng bộ và cập nhật thông tin sản phẩm từ cơ sở dữ liệu hoặc hệ thống máy chủ của bạn vào Catalog trong Business Center trên TikTok. Thông qua việc thiết lập lịch định kỳ (hàng giờ, hàng ngày, hàng tháng) với các giao thức phổ biến như HTTP, HTTPS, FTP hoặc SFTP, hệ thống sẽ tự động quét tệp dữ liệu sản phẩm (CSV, TSV, XML) và cập nhật số lượng tồn kho, giá bán cũng như trạng thái sản phẩm theo thời gian thực. Tài liệu này cung cấp chi tiết kỹ thuật cho toàn bộ các endpoint thuộc nhóm quản lý Feed Catalog trong phiên bản API v1.3.

## Mục lục các endpoint

| Endpoint | Phương thức | Mục đích |
|---|---|---|
| [/catalog/feed/create/](27-catalog-feeds.md#doc-1740665161957377) | `POST` | Khởi tạo một nguồn cấp dữ liệu (feed) mới kèm cấu hình lịch chạy |
| [/catalog/feed/get/](27-catalog-feeds.md#doc-1740665183073281) | `GET` | Lấy thông tin chi tiết một feed hoặc danh sách tất cả feed của Catalog |
| [/catalog/feed/update/](27-catalog-feeds.md#doc-1740665197662210) | `POST` | Chỉnh sửa tên, chế độ cập nhật, đường dẫn tệp và lịch đồng bộ của feed |
| [/catalog/feed/delete/](27-catalog-feeds.md#doc-1740665210863617) | `POST` | Xóa một nguồn cấp dữ liệu khỏi Catalog |
| [/catalog/feed/log/](27-catalog-feeds.md#doc-1740665225631810) | `GET` | Lấy nhật ký lịch sử 10 lần đồng bộ gần nhất của feed |
| [/catalog/feed/switch/](27-catalog-feeds.md#doc-1750349624999937) | `POST` | Bật hoặc tắt trạng thái kích hoạt lịch chạy tự động của feed |

---

## Tổng quan Feed Catalog (`Catalog Feeds`)
<a id="doc-1740132921913346"></a>
<!-- doc_id: 1740132921913346 -->

> Đường dẫn: API Reference > Catalog Feeds

> [!IMPORTANT]
> Bằng việc sử dụng các endpoint của Catalog API, bạn đồng ý với [Điều khoản Danh mục sản phẩm (Product Catalog Terms)](https://ads.tiktok.com/i18n/official/article?aid=6765817026859499525) và xác nhận tuân thủ [Chính sách quảng cáo của TikTok (TikTok Advertising Policies)](https://ads.tiktok.com/help/article?aid=6685586866860720134). Vui lòng xem xét kỹ các chính sách này và đảm bảo rằng các sản phẩm tải lên danh mục không vi phạm quy định.

Danh mục sản phẩm (Catalog) là tài sản lưu trữ thông tin về các mặt hàng bạn muốn quảng bá trên TikTok. Sử dụng Catalog là giải pháp lý tưởng cho các nhà bán lẻ trực tuyến muốn tạo và quản lý quảng cáo cho nhiều mặt hàng cùng lúc một cách hiệu quả.

Bạn có thể sử dụng feed để tự động nạp thông tin sản phẩm từ cơ sở dữ liệu và cập nhật danh mục trong Business Center. Nhóm Catalog Feeds API cho phép bạn quản lý vòng đời của các feed thuộc Catalog trong Business Center của bạn:
- Xem thêm [Tổng quan (Overview)](../09-marketing-api/catalog.md#doc-1754263078057986) và [Hướng dẫn (Guides)](../09-marketing-api/catalog.md#doc-1754263100123137) để tìm hiểu các khái niệm, lợi ích và cách tạo, quản lý Catalog.

Nhóm chức năng này bao gồm các endpoint sau:
* [Tạo feed (Create a feed)](27-catalog-feeds.md#doc-1740665161957377)
* [Lấy danh sách feed (Get feeds)](27-catalog-feeds.md#doc-1740665183073281)
* [Cập nhật feed (Update a feed)](27-catalog-feeds.md#doc-1740665197662210)
* [Xóa feed (Delete a feed)](27-catalog-feeds.md#doc-1740665210863617)
* [Lấy nhật ký feed (Get the log of a feed)](27-catalog-feeds.md#doc-1740665225631810)
* [Cập nhật trạng thái lịch chạy của feed (Update the schedule status of a feed)](27-catalog-feeds.md#doc-1750349624999937)

---

## Tạo feed (`Create a feed`)
<a id="doc-1740665161957377"></a>
<!-- doc_id: 1740665161957377 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/catalog/feed/create/`

**Mục đích**: Tạo mới một nguồn cấp dữ liệu (feed) để tự động hóa việc nhập và cập nhật sản phẩm vào Catalog.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Bắt buộc | Access token đã được cấp quyền. Chi tiết xem tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| `Content-Type` | string | Bắt buộc | Định dạng nội dung của request: `"application/json"`. |

### Tham số (POST: JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `bc_id` | string | Bắt buộc | ID của Business Center. |
| `catalog_id` | string | Bắt buộc | ID danh mục sản phẩm (Catalog ID). |
| `feed_name` | string | Bắt buộc | Tên của nguồn cấp dữ liệu (feed). |
| `update_mode` | string | Bắt buộc | Chế độ cập nhật dữ liệu.<br>Giá trị enum:<br>• `OVERWRITE`: Chế độ ghi đè toàn bộ danh mục. Những sản phẩm không xuất hiện trong tệp feed mới sẽ bị xóa khỏi danh mục; sản phẩm mới được tạo thêm; sản phẩm đã có sẽ được cập nhật.<br>• `INCREMENTAL`: Chế độ cập nhật bổ sung. Sản phẩm mới được tạo thêm và sản phẩm đã có được cập nhật thông tin; không xóa sản phẩm cũ. |
| `schedule_param` | object | Không bắt buộc | Thông số cấu hình lịch trình cập nhật tự động. |
| ↳ `source` | object | Bắt buộc | Nguồn lưu trữ tệp dữ liệu feed. |
| ↳↳ `uri` | string | Điều kiện | Bắt buộc nếu truyền `interval_type` hoặc `timezone`. Đường dẫn URL nơi lưu trữ tệp dữ liệu feed. Phải bắt đầu bằng `http`, `https`, `ftp` hoặc `sftp`. Tệp có thể có dung lượng tối đa 8 GB với các định dạng hỗ trợ: CSV, TSV hoặc XML (RSS/ATOM).<br>**Lưu ý**: Nếu URL hình ảnh phụ trong tệp chứa dấu phẩy (,), hãy mã hóa URL bằng `%2C`. |
| ↳↳ `username` | string | Không bắt buộc | Tên đăng nhập xác thực nếu tệp feed được bảo vệ bằng mật khẩu (HTTP Basic Auth hoặc SFTP). |
| ↳↳ `password` | string | Không bắt buộc | Mật khẩu xác thực nếu tệp feed được bảo vệ bằng mật khẩu. |
| ↳ `interval_type` | string | Điều kiện | Bắt buộc nếu truyền `uri` hoặc `timezone`. Chu kỳ lặp lại của lịch cập nhật.<br>Giá trị enum: `HOURLY` (hàng giờ), `DAILY` (hàng ngày), `MONTHLY` (hàng tháng). |
| ↳ `interval_count` | number | Không bắt buộc | Số khoảng chu kỳ giữa hai lần chạy feed liên tiếp.<br>• Nếu `interval_type` là `HOURLY`: giá trị cho phép từ 1-23.<br>• Nếu `interval_type` là `DAILY`: giá trị cho phép từ 1-30.<br>• Nếu `interval_type` là `MONTHLY`: giá trị cho phép từ 1-12. |
| ↳ `timezone` | string | Điều kiện | Bắt buộc nếu truyền `uri` hoặc `interval_type`. Múi giờ áp dụng cho lịch chạy (ví dụ: `Asia/Singapore`). Danh sách múi giờ xem tại [Appendix-Time Zone](../15-appendix/phu-luc-p1.md#doc-1737586324313089). |
| ↳ `day_of_month` | number | Không bắt buộc | Ngày trong tháng để chạy feed (áp dụng khi `interval_type` là `MONTHLY`). |
| ↳ `hour` | number | Không bắt buộc | Giờ trong ngày để chạy feed. Khoảng giá trị: `0-23`. Mặc định: `0`. |
| ↳ `minute` | number | Không bắt buộc | Phút trong giờ để chạy feed. Khoảng giá trị: `0-59`. Mặc định: `0`. |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Chi tiết xem tại [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi. |
| `request_id` | string | ID duy nhất định danh request. |
| `data` | object | Dữ liệu trả về. |
| ↳ `feed_id` | string | ID nguồn cấp dữ liệu vừa được tạo. |
| ↳ `feed_name` | string | Tên nguồn cấp dữ liệu. |
| ↳ `status` | string | Trạng thái lịch chạy của feed (`ON`: đang kích hoạt lịch chạy tự động, `OFF`: đang tắt hoặc không có lịch). |
| ↳ `last_update_param` | object | Thông tin tham số cấu hình cập nhật của feed. |
| ↳↳ `uri` | string | Đường dẫn URL tệp dữ liệu. |
| ↳↳ `update_mode` | string | Chế độ cập nhật (`OVERWRITE` hoặc `INCREMENTAL`). |
| ↳↳ `timezone` | string | Múi giờ cấu hình. |
| ↳↳ `interval_type` | string | Loại chu kỳ lặp lại (`HOURLY`, `DAILY`, `MONTHLY`). |
| ↳↳ `interval_count` | number | Số chu kỳ lặp lại. |
| ↳↳ `day_of_month` | number | Ngày trong tháng chạy feed. |
| ↳↳ `hour` | number | Giờ chạy feed. |
| ↳↳ `minute` | number | Phút chạy feed. |
| ↳ `next_update_time` | string | Ngày giờ dự kiến chạy cập nhật tiếp theo (ví dụ: `"2023-10-24 02:00:00"`). |
| ↳ `number_of_products` | number | Số lượng sản phẩm hiện có trong feed. |

### Ví dụ gọi API

#### cURL
```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/catalog/feed/create/' \
--header 'Access-Token: your_access_token_here' \
--header 'Content-Type: application/json' \
--data '{
    "bc_id": "7100000000000000001",
    "catalog_id": "7200000000000000001",
    "feed_name": "Daily_Product_Feed_VN",
    "update_mode": "INCREMENTAL",
    "schedule_param": {
        "source": {
            "uri": "https://example.com/feeds/products_vn.csv"
        },
        "interval_type": "HOURLY",
        "interval_count": 2,
        "timezone": "Asia/Ho_Chi_Minh",
        "minute": 15
    }
}'
```

#### Python
```python
import requests

ACCESS_TOKEN = "your_access_token_here"

url = "https://business-api.tiktok.com/open_api/v1.3/catalog/feed/create/"
headers = {
    "Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}
payload = {
    "bc_id": "7100000000000000001",
    "catalog_id": "7200000000000000001",
    "feed_name": "Daily_Product_Feed_VN",
    "update_mode": "INCREMENTAL",
    "schedule_param": {
        "source": {
            "uri": "https://example.com/feeds/products_vn.csv"
        },
        "interval_type": "HOURLY",
        "interval_count": 2,
        "timezone": "Asia/Ho_Chi_Minh",
        "minute": 15
    }
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())
```

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20231023120000010188059082090",
  "data": {
    "feed_id": "8000000000000000001",
    "feed_name": "Daily_Product_Feed_VN",
    "status": "ON",
    "next_update_time": "2023-10-23 18:15:00",
    "number_of_products": 0,
    "last_update_param": {
      "uri": "https://example.com/feeds/products_vn.csv",
      "update_mode": "INCREMENTAL",
      "timezone": "Asia/Ho_Chi_Minh",
      "interval_type": "HOURLY",
      "interval_count": 2,
      "minute": 15
    }
  }
}
```

---

## Lấy danh sách feed (`Get feeds`)
<a id="doc-1740665183073281"></a>
<!-- doc_id: 1740665183073281 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/catalog/feed/get/`

**Mục đích**: Lấy thông tin chi tiết về một nguồn cấp dữ liệu cụ thể hoặc tất cả các feed thuộc về một Catalog.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Bắt buộc | Access token đã được cấp quyền. Chi tiết xem tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (GET: query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `bc_id` | string | Bắt buộc | ID của Business Center. |
| `catalog_id` | string | Bắt buộc | ID danh mục sản phẩm (Catalog ID). |
| `feed_id` | string | Không bắt buộc | ID của feed muốn lấy thông tin. Nếu không chỉ định, hệ thống sẽ trả về tất cả các feed của Catalog. |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Chi tiết xem tại [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi. |
| `request_id` | string | ID duy nhất định danh request. |
| `data` | object | Dữ liệu trả về. |
| ↳ `feed_list` | object[] | Danh sách các nguồn cấp dữ liệu (feed). |
| ↳↳ `feed_id` | string | ID của feed. |
| ↳↳ `feed_name` | string | Tên của feed. |
| ↳↳ `status` | string | Trạng thái kích hoạt lịch chạy (`ON` hoặc `OFF`). |
| ↳↳ `last_update_param` | object | Thông tin tham số cấu hình cập nhật. |
| ↳↳↳ `uri` | string | Đường dẫn URL lưu trữ tệp feed. |
| ↳↳↳ `update_mode` | string | Chế độ cập nhật (`OVERWRITE` hoặc `INCREMENTAL`). |
| ↳↳↳ `timezone` | string | Múi giờ áp dụng cho lịch chạy. |
| ↳↳↳ `interval_type` | string | Chu kỳ lặp lại (`HOURLY`, `DAILY`, `MONTHLY`). |
| ↳↳↳ `interval_count` | number | Số chu kỳ lặp lại. |
| ↳↳↳ `day_of_month` | number | Ngày trong tháng chạy feed. |
| ↳↳↳ `hour` | number | Giờ chạy feed. |
| ↳↳↳ `minute` | number | Phút chạy feed. |
| ↳↳ `next_update_time` | string | Thời gian chạy cập nhật tiếp theo. |
| ↳↳ `number_of_products` | number | Số lượng sản phẩm hiện có trong feed. |

### Ví dụ

#### cURL
```bash
curl -G --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/catalog/feed/get/' \
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

url = "https://business-api.tiktok.com/open_api/v1.3/catalog/feed/get/"
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
  "request_id": "20231023120000010188059082091",
  "data": {
    "feed_list": [
      {
        "feed_id": "8000000000000000001",
        "feed_name": "Daily_Product_Feed_VN",
        "status": "ON",
        "next_update_time": "2023-10-23 18:15:00",
        "number_of_products": 1500,
        "last_update_param": {
          "uri": "https://example.com/feeds/products_vn.csv",
          "update_mode": "INCREMENTAL",
          "timezone": "Asia/Ho_Chi_Minh",
          "interval_type": "HOURLY",
          "interval_count": 2,
          "minute": 15
        }
      }
    ]
  }
}
```


---

## Cập nhật feed (`Update a feed`)
<a id="doc-1740665197662210"></a>
<!-- doc_id: 1740665197662210 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/catalog/feed/update/`

**Mục đích**: Chỉnh sửa thông tin cấu hình, chế độ cập nhật, đường dẫn tệp dữ liệu hoặc lịch trình đồng bộ của một feed đã tồn tại.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Bắt buộc | Access token đã được cấp quyền. Chi tiết xem tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| `Content-Type` | string | Bắt buộc | Loại thông điệp request: `"application/json"`. |

### Tham số (POST: JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `bc_id` | string | Bắt buộc | ID của Business Center. |
| `catalog_id` | string | Bắt buộc | ID danh mục sản phẩm (Catalog ID). |
| `feed_id` | string | Bắt buộc | ID nguồn cấp dữ liệu (feed) cần cập nhật. |
| `feed_name` | string | Không bắt buộc | Tên mới cho nguồn cấp dữ liệu. |
| `update_mode` | string | Bắt buộc | Chế độ cập nhật dữ liệu.<br>Giá trị enum:<br>• `OVERWRITE`: Ghi đè toàn bộ danh mục sản phẩm.<br>• `INCREMENTAL`: Cập nhật bổ sung sản phẩm mới và sửa đổi sản phẩm đã có. |
| `schedule_param` | object | Không bắt buộc | Cấu hình lịch đồng bộ mới. |
| ↳ `source` | object | Bắt buộc | Nguồn lưu trữ tệp dữ liệu feed. |
| ↳↳ `uri` | string | Điều kiện | Bắt buộc nếu truyền `interval_type` hoặc `timezone`. Đường dẫn URL mới nơi lưu trữ tệp feed (hỗ trợ `http`, `https`, `ftp`, `sftp`). Dung lượng tối đa 8 GB. |
| ↳↳ `username` | string | Không bắt buộc | Tên đăng nhập xác thực tài khoản lưu trữ tệp feed. |
| ↳↳ `password` | string | Không bắt buộc | Mật khẩu xác thực tài khoản lưu trữ tệp feed. |
| ↳ `interval_type` | string | Điều kiện | Bắt buộc nếu truyền `uri` hoặc `timezone`. Chu kỳ cập nhật mới (`HOURLY`, `DAILY`, `MONTHLY`). |
| ↳ `interval_count` | number | Không bắt buộc | Số khoảng chu kỳ giữa hai lần chạy feed. |
| ↳ `timezone` | string | Điều kiện | Bắt buộc nếu truyền `uri` hoặc `interval_type`. Múi giờ áp dụng cho lịch chạy (ví dụ: `Asia/Ho_Chi_Minh`). Xem danh sách tại [Appendix-Time Zone](../15-appendix/phu-luc-p1.md#doc-1737586324313089). |
| ↳ `day_of_month` | number | Không bắt buộc | Ngày trong tháng chạy feed (khi `interval_type` là `MONTHLY`). |
| ↳ `hour` | number | Không bắt buộc | Giờ trong ngày chạy feed (0-23). Mặc định: 0. |
| ↳ `minute` | number | Không bắt buộc | Phút trong giờ chạy feed (0-59). Mặc định: 0. |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Chi tiết xem tại [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi. |
| `request_id` | string | ID duy nhất định danh request. |
| `data` | object | Dữ liệu trả về. |
| ↳ `feed_id` | string | ID nguồn cấp dữ liệu vừa được cập nhật. |
| ↳ `feed_name` | string | Tên nguồn cấp dữ liệu. |
| ↳ `status` | string | Trạng thái kích hoạt lịch chạy (`ON` hoặc `OFF`). |
| ↳ `last_update_param` | object | Thông tin tham số cấu hình cập nhật mới nhất. |
| ↳↳ `uri` | string | Đường dẫn URL lưu trữ tệp feed. |
| ↳↳ `update_mode` | string | Chế độ cập nhật (`OVERWRITE` hoặc `INCREMENTAL`). |
| ↳↳ `timezone` | string | Múi giờ lịch trình. |
| ↳↳ `interval_type` | string | Chu kỳ lặp lại (`HOURLY`, `DAILY`, `MONTHLY`). |
| ↳↳ `interval_count` | number | Số chu kỳ lặp lại. |
| ↳↳ `day_of_month` | number | Ngày trong tháng. |
| ↳↳ `hour` | number | Giờ chạy feed. |
| ↳↳ `minute` | number | Phút chạy feed. |
| ↳ `next_update_time` | string | Thời gian chạy cập nhật dự kiến tiếp theo. |
| ↳ `number_of_products` | number | Số lượng sản phẩm hiện có trong feed. |

### Ví dụ gọi API

```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/catalog/feed/update/' \
--header 'Access-Token: your_access_token_here' \
--header 'Content-Type: application/json' \
--data '{
    "bc_id": "7100000000000000001",
    "catalog_id": "7200000000000000001",
    "feed_id": "8000000000000000001",
    "update_mode": "INCREMENTAL",
    "schedule_param": {
        "source": {
            "uri": "https://example.com/feeds/products_vn_updated.csv"
        },
        "interval_type": "DAILY",
        "interval_count": 1,
        "timezone": "Asia/Ho_Chi_Minh",
        "hour": 3,
        "minute": 0
    }
}'
```

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20231023120000010188059082092",
  "data": {
    "feed_id": "8000000000000000001",
    "feed_name": "Daily_Product_Feed_VN",
    "status": "ON",
    "next_update_time": "2023-10-24 03:00:00",
    "number_of_products": 1520,
    "last_update_param": {
      "uri": "https://example.com/feeds/products_vn_updated.csv",
      "update_mode": "INCREMENTAL",
      "timezone": "Asia/Ho_Chi_Minh",
      "interval_type": "DAILY",
      "interval_count": 1,
      "hour": 3,
      "minute": 0
    }
  }
}
```

---

## Xóa feed (`Delete a feed`)
<a id="doc-1740665210863617"></a>
<!-- doc_id: 1740665210863617 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/catalog/feed/delete/`

**Mục đích**: Xóa một nguồn cấp dữ liệu (feed) khỏi Catalog trong Business Center.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Bắt buộc | Access token đã được cấp quyền. Chi tiết xem tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| `Content-Type` | string | Bắt buộc | Loại thông điệp request: `"application/json"`. |

### Tham số (POST: JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `bc_id` | string | Bắt buộc | ID của Business Center. |
| `catalog_id` | string | Bắt buộc | ID danh mục sản phẩm (Catalog ID). |
| `feed_id` | string | Bắt buộc | ID của nguồn cấp dữ liệu (feed) cần xóa. |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Chi tiết xem tại [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi. |
| `request_id` | string | ID nhật ký duy nhất định danh request. |
| `data` | object | Dữ liệu trả về (mảng rỗng `{}`). |

### Ví dụ gọi API

```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/catalog/feed/delete/' \
--header 'Access-Token: your_access_token_here' \
--header 'Content-Type: application/json' \
--data '{
    "bc_id": "7100000000000000001",
    "catalog_id": "7200000000000000001",
    "feed_id": "8000000000000000001"
}'
```

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20231023120000010188059082093",
  "data": {}
}
```

---

## Lấy nhật ký feed (`Get the log of a feed`)
<a id="doc-1740665225631810"></a>
<!-- doc_id: 1740665225631810 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/catalog/feed/log/`

**Mục đích**: Lấy thông tin nhật ký chi tiết về 10 lần thực hiện đồng bộ gần nhất của một feed, bao gồm số lượng sản phẩm được thêm, sửa, xóa, lỗi và cảnh báo.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Bắt buộc | Access token đã được cấp quyền. Chi tiết xem tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (GET: query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `bc_id` | string | Bắt buộc | ID của Business Center. |
| `catalog_id` | string | Bắt buộc | ID danh mục sản phẩm (Catalog ID). |
| `feed_id` | string | Bắt buộc | ID của nguồn cấp dữ liệu muốn tra cứu nhật ký. |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Chi tiết xem tại [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi. |
| `request_id` | string | ID duy nhất định danh request. |
| `data` | object | Dữ liệu trả về. |
| ↳ `feed_logs` | object[] | Danh sách các bản ghi nhật ký chạy feed. |
| ↳↳ `update_status` | object | Dữ liệu trạng thái và số lượng sản phẩm xử lý. |
| ↳↳↳ `add_count` | number | Số lượng sản phẩm mới được thêm thành công. |
| ↳↳↳ `update_count` | number | Số lượng sản phẩm đã có được cập nhật thành công. |
| ↳↳↳ `remove_count` | number | Số lượng sản phẩm bị xóa khỏi danh mục. |
| ↳↳↳ `error_count` | number | Số lượng sản phẩm gặp lỗi khi thêm, cập nhật hoặc xóa. |
| ↳↳↳ `warn_count` | number | Số lượng cảnh báo phát sinh trong quá trình xử lý. |
| ↳↳↳ `process_status` | string | Trạng thái của thao tác cập nhật.<br>Giá trị enum: `PROCESSING` (đang xử lý), `SUCCESS` (thành công), `FAILED` (thất bại), `WAITING` (đang chờ xử lý). |
| ↳↳ `update_time` | object | Thông tin thời gian xử lý đồng bộ. |
| ↳↳↳ `start_time` | string | Thời điểm bắt đầu chạy đồng bộ (ví dụ: `"2023-10-23 03:00:00"`). |
| ↳↳↳ `end_time` | string | Thời điểm kết thúc chạy đồng bộ (ví dụ: `"2023-10-23 03:02:15"`). |

### Ví dụ

#### cURL
```bash
curl -G --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/catalog/feed/log/' \
--header 'Access-Token: your_access_token_here' \
--data-urlencode 'bc_id=7100000000000000001' \
--data-urlencode 'catalog_id=7200000000000000001' \
--data-urlencode 'feed_id=8000000000000000001'
```

#### Python
```python
import requests

ACCESS_TOKEN = "your_access_token_here"
BC_ID = "7100000000000000001"
CATALOG_ID = "7200000000000000001"
FEED_ID = "8000000000000000001"

url = "https://business-api.tiktok.com/open_api/v1.3/catalog/feed/log/"
headers = {"Access-Token": ACCESS_TOKEN}
params = {
    "bc_id": BC_ID,
    "catalog_id": CATALOG_ID,
    "feed_id": FEED_ID
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20231023120000010188059082094",
  "data": {
    "feed_logs": [
      {
        "update_status": {
          "add_count": 50,
          "update_count": 120,
          "remove_count": 2,
          "error_count": 0,
          "warn_count": 1,
          "process_status": "SUCCESS"
        },
        "update_time": {
          "start_time": "2023-10-23 03:00:00",
          "end_time": "2023-10-23 03:02:15"
        }
      }
    ]
  }
}
```

---

## Cập nhật trạng thái lịch chạy của feed (`Update the schedule status of a feed`)
<a id="doc-1750349624999937"></a>
<!-- doc_id: 1750349624999937 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/catalog/feed/switch/`

**Mục đích**: Bật hoặc tắt trạng thái kích hoạt của lịch chạy tự động định kỳ đối với một nguồn cấp dữ liệu (feed).

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Bắt buộc | Access token đã được cấp quyền. Chi tiết xem tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| `Content-Type` | string | Bắt buộc | Loại thông điệp request: `"application/json"`. |

### Tham số (POST: JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `bc_id` | string | Bắt buộc | ID của Business Center. |
| `catalog_id` | string | Bắt buộc | ID danh mục sản phẩm (Catalog ID). |
| `feed_id` | string | Bắt buộc | ID nguồn cấp dữ liệu muốn cập nhật trạng thái lịch chạy. |
| `status` | string | Bắt buộc | Trạng thái lịch chạy mới của feed.<br>Giá trị enum:<br>• `ON`: Bật lịch trình đồng bộ tự động.<br>• `OFF`: Tắt lịch trình đồng bộ tự động. |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Chi tiết xem tại [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi. |
| `request_id` | string | ID nhật ký duy nhất định danh request. |
| `data` | object | Dữ liệu trả về (mảng rỗng `{}`). |

### Ví dụ gọi API

```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/catalog/feed/switch/' \
--header 'Access-Token: your_access_token_here' \
--header 'Content-Type: application/json' \
--data '{
    "bc_id": "7100000000000000001",
    "catalog_id": "7200000000000000001",
    "feed_id": "8000000000000000001",
    "status": "OFF"
}'
```

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20231023120000010188059082095",
  "data": {}
}
```
