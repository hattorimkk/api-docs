# Sản phẩm Catalog — phần 1/3

Tài liệu này bao gồm hướng dẫn và đặc tả API quản lý sản phẩm trong danh mục sản phẩm (Catalog Products) của TikTok Business API:
- Tổng quan về sản phẩm Catalog (`Catalog Products`)
- Tải lên sản phẩm qua URL tệp (`Upload products via a file URL`)
- Tải lên sản phẩm qua JSON schema (`Upload products via a JSON schema` - phần đầu)

---

## Tổng quan về sản phẩm Catalog (`Catalog Products`)
<a id="doc-1740132940622850"></a>
<!-- doc_id: 1740132940622850 -->

> **Đường dẫn**: API Reference > Catalog Products

> [!IMPORTANT]
> **Quan trọng**: Bằng việc sử dụng các endpoint của Catalog API, bạn đồng ý với [Điều khoản Danh mục sản phẩm (Product Catalog Terms)](https://ads.tiktok.com/i18n/official/article?aid=6765817026859499525) và xác nhận rằng bạn tuân thủ [Chính sách quảng cáo của TikTok (TikTok Advertising Policies)](https://ads.tiktok.com/help/article?aid=6685586866860720134). Vui lòng xem kỹ các chính sách này và đảm bảo các mặt hàng bạn tải lên danh mục không vi phạm chính sách.

Danh mục sản phẩm (catalog) là tài sản cho phép bạn lưu trữ thông tin về các sản phẩm bạn muốn quảng bá trên TikTok. Sử dụng catalog là giải pháp tối ưu cho bất kỳ ai muốn tạo và quản lý hiệu quả các quảng cáo chứa nhiều loại sản phẩm, chẳng hạn như nhà bán lẻ trực tuyến (online retailer). API Catalog Products cho phép bạn quản lý các sản phẩm trong một catalog thuộc Business Center của bạn.

Xem [Tổng quan (Overview)](../09-marketing-api/catalog.md#doc-1754263078057986) và [Hướng dẫn (Guides)](../09-marketing-api/catalog.md#doc-1754263100123137) để tìm hiểu các khái niệm và lợi ích của catalog, cũng như cách tạo và quản lý sản phẩm trong catalog.

Nhóm API này bao gồm các endpoint sau:
* [Tải lên sản phẩm qua URL tệp (Upload products via a file URL)](28-catalog-products-p1.md#doc-1740496787164161)
* [Tải lên sản phẩm qua JSON schema (Upload products via a JSON schema)](28-catalog-products-p1.md#doc-1740497429681153)
* [Cập nhật sản phẩm (Update products)](28-catalog-products-p2.md#doc-1740562287852546)
* [Xóa sản phẩm (Remove products)](28-catalog-products-p2.md#doc-1740562489236481)
* [Lấy thông tin sản phẩm (Get products)](28-catalog-products-p2.md#doc-1740564136678402)
* [Lấy nhật ký xử lý sản phẩm (Get the product handling log)](28-catalog-products-p3.md#doc-1740570027173889)

> [!NOTE]
> **Giới hạn tốc độ gọi (Rate Limit)**:
> Nếu bạn sử dụng 4 endpoint dưới đây để thao tác trên **cùng một catalog**, bạn có thể thực hiện tối đa 1.000 truy vấn mỗi giờ. Đối với các yêu cầu vượt quá giới hạn, bạn sẽ nhận được mã lỗi. Bạn cần chờ đến giờ tiếp theo trước khi có thể gửi các yêu cầu API mới.
> • [/catalog/product/file/](28-catalog-products-p1.md#doc-1740496787164161)
> • [/catalog/product/upload/](28-catalog-products-p1.md#doc-1740497429681153)
> • [/catalog/product/update/](28-catalog-products-p2.md#doc-1740562287852546)
> • [/catalog/product/delete/](28-catalog-products-p2.md#doc-1740562489236481)

---

## Tải lên sản phẩm qua URL tệp (`Upload products via a file URL`)
<a id="doc-1740496787164161"></a>
<!-- doc_id: 1740496787164161 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/catalog/product/file/`

> **Đường dẫn**: API Reference > Catalog Products > Upload products via a file URL

**Mục đích**: Sử dụng endpoint này để tải lên các sản phẩm thông qua URL của tệp dữ liệu. Các sản phẩm sẽ được thêm hoặc cập nhật vào catalog theo cơ chế bất đồng bộ.

Trong phản hồi, bạn sẽ nhận được mã ID tác vụ xử lý `feed_log_id`. Với ID này, bạn có thể kiểm tra trạng thái xử lý và kết quả cuối cùng của tác vụ thông qua endpoint [/catalog/product/log/](28-catalog-products-p3.md#doc-1740570027173889).

Sử dụng endpoint này thay vì [/catalog/product/upload/](28-catalog-products-p1.md#doc-1740497429681153) khi bạn tải lên sản phẩm lần đầu tiên vào catalog, hoặc tải lên toàn bộ sản phẩm định kỳ vào catalog với tần suất cập nhật một lần mỗi ngày.

**Hiện tại, API chỉ hỗ trợ định dạng tệp CSV cho Catalog Feeds.** Các mẫu CSV Catalog Feed có sẵn cho từng loại catalog cụ thể như sau:
- [Mẫu cho catalog E-commerce](https://bytedance.feishu.cn/sheets/shtcnZ3VnFbOO64OiFNZRhlz8Db)
- [Mẫu cho catalog khách sạn (hotel)](https://bytedance.feishu.cn/sheets/FJNUsA17Xhp540t41Kecq8ZInCf)
- [Mẫu cho catalog chuyến bay (flight)](https://bytedance.feishu.cn/sheets/SII0sykCGhEObgtJaENcPSDpnyc)
- [Mẫu cho catalog điểm đến du lịch (destination)](https://bytedance.feishu.cn/sheets/OvJIsVlNfhl30ttKs7MciksInPh)
- [Mẫu cho catalog giải trí (entertainment)](https://bytedance.feishu.cn/sheets/MrBAsQuGchn0pQtRRiyc47lynyg)
- [Mẫu cho catalog xe có sẵn (Auto-Inventory)](https://bytedance.sg.larkoffice.com/sheets/QuGIs2PgjhXLtOtDLaBceZnVnVg)
- [Mẫu cho catalog mẫu xe (Auto-Model)](https://bytedance.sg.larkoffice.com/sheets/RjwhsCwlIhepPHtOq1SlD868g8b)
- [Mẫu cho catalog phim ngắn nhiều tập (mini series)](https://bytedance.sg.larkoffice.com/sheets/SmHxs8C4oh0mKWtenOslDZ0Sg6b)
- [Mẫu cho catalog chung (generic)](https://bytedance.sg.larkoffice.com/sheets/I4uXsH0G4hvUHGtsUZSlcOFCg7c)
- [Mẫu cho catalog trực tuyến đến ngoại tuyến (online-to-offline)](https://bytedance.sg.larkoffice.com/sheets/Cj78sxAd8h2UDItyxmFlNmtIg5e)

Hình ảnh sản phẩm (`image_link`) phải có kích thước tối thiểu từ 500x500 px trở lên. Nếu không đạt kích thước này, sản phẩm sẽ không được phê duyệt. Để biết chi tiết, xem [Yêu cầu hình ảnh sản phẩm (Product Image Requirements)](../09-marketing-api/catalog.md#doc-1739578479392770).

> [!NOTE]
> • Catalog giải trí (Entertainment) và catalog phim ngắn tập (Mini series) hiện là các tính năng trong danh sách cho phép (allowlist-only) và chỉ mở theo lời mời trong giai đoạn thử nghiệm. Nếu bạn muốn truy cập, vui lòng liên hệ đại diện TikTok của bạn. Tuy nhiên, việc tham gia thử nghiệm không được đảm bảo trước.<br>
> • Mã SKU là duy nhất trong cùng một catalog sản phẩm và chỉ thuộc về một feed nhất định. Mọi thao tác đối với một SKU cần được thực hiện dưới feed mà nó trực thuộc.<br>
> • Một feed chỉ có thể xử lý một tác vụ tệp tại một thời điểm, và tác vụ mới sẽ thất bại nếu tác vụ tệp hiện tại chưa hoàn thành. Vui lòng đợi tác vụ hiện tại hoàn tất trước khi gửi tác vụ tiếp theo. Tốc độ xử lý sản phẩm khoảng 5 triệu mục mỗi giờ, tùy thuộc vào tải của hệ thống.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Có | Access token được ủy quyền. Chi tiết xem [Xác thực (Authentication)](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type | string | Có | Loại nội dung của yêu cầu. Giá trị hợp lệ: `"application/json"`. |

### Tham số (JSON body)

| Field | Data Type | Description |
|---|---|---|
| bc_id | string | **Bắt buộc**. ID của Business Center. |
| catalog_id | string | **Bắt buộc**. ID của Catalog. |
| feed_id | string | ID của Feed. |
| file_url | string | **Bắt buộc**. Địa chỉ tải xuống của tệp CSV. Số lượng dòng sản phẩm trong tệp phải ít hơn 20 triệu dòng.<br>• Hiện tại, API chỉ cho phép định dạng tệp CSV cho Catalog Feeds.<br>• Để tìm hiểu các tham số chi tiết của từng sản phẩm catalog, xem phần mảng đối tượng [`products`](28-catalog-products-p1.md#doc-1740497429681153).<br>• Để hiểu cách một trường và giá trị tương ứng trong định dạng JSON được biểu diễn trong mẫu CSV, xem [So sánh tham số sản phẩm Catalog dạng JSON & mẫu CSV](https://bytedance.sg.larkoffice.com/sheets/F7CGsxjuahfnAYt7GzTlR5X5ghb?sheet=gJ73Xi).<br>• Hình ảnh sản phẩm (`image_link`) phải có kích thước từ 500 x 500 pixel trở lên.<br>**Lưu ý**:<br>• Để tải lên các tập phim ngắn nhắm mục tiêu nhiều khu vực vào catalog phim ngắn, hãy gọi [/catalog/product/file/](28-catalog-products-p1.md#doc-1740496787164161) nhiều lần với cùng `series_id` và các cài đặt `country` khác nhau. Sau khi tải lên, truy cập cài đặt nhắm mục tiêu hợp nhất qua `target_config` và `additional_product_list` trong [/catalog/product/get/](28-catalog-products-p2.md#doc-1740564136678402).<br>• Ví dụ: các lần tải lên riêng biệt với `country` đặt thành `US` và `VN` sẽ dẫn đến `list.target_config.region_code` là `US` và `list.additional_product_list.region_code` là `VN` trong `/catalog/product/get/`.<br>• Nếu URL hình ảnh bổ sung của bạn chứa dấu phẩy (,), hãy URL-encode chúng bằng cách thay thế bằng `%2C` trước khi thêm vào trường này. Ví dụ: `["https://img.example.com/product.jpg?width=800&height=600&quality=85&format=webp","https://img.example.com/product_800x600%2Cq85%2Cwebp.jpg"]`. |
| update_mode | string | Chế độ cập nhật. Chế độ này là một lần duy nhất và chỉ áp dụng cho yêu cầu hiện tại.<br>Giá trị enum:<br>• `OVERWRITE`: Ở chế độ này, tất cả các sản phẩm trong catalog sẽ bị thay thế bởi các sản phẩm trong tệp bạn chỉ định.<br>• `INCREMENTAL`: Ở chế độ này, các sản phẩm trong tệp bạn chỉ định sẽ được thêm vào catalog. Lưu ý nếu bạn tải lên một sản phẩm đã có trong catalog với SKU ID trùng lặp, dữ liệu của sản phẩm đó trong catalog sẽ bị thay thế.<br>Giá trị mặc định: `INCREMENTAL`.<br>**Lưu ý**: Nếu bạn truyền `feed_id`, chế độ cập nhật bạn chỉ định qua trường này sẽ không ảnh hưởng đến chế độ cập nhật mặc định của feed. |

### Trường bí danh cho catalog khách sạn (Alias fields for hotel catalogs)
Bảng dưới đây phác thảo các trường bí danh (alias) có sẵn và tên trường hiện tại tương ứng trong catalog khách sạn. Ví dụ, nếu bạn đưa vào `image[0].url`, trường này sẽ tự động ánh xạ liền mạch tới `image_link`.

| Existing Field | Corresponding Alias Field |
|---|---|
| `name` | `hotel_name` |
| `image_link` | `image[0].url` |
| `video_link` | `video[0].url` |
| `address` | `addr1`<br>`address.addr1` |
| `secondary_address` | `addr2`<br>`address.addr2` |
| `tertiary_address` | `addr3`<br>`address.addr3` |
| `neighborhood` | `neighborhood[0]` |
| `rating_system` | `guest_rating[0].rating_system` |
| `max_score` | `guest_rating[0].max_score` |
| `guest_ratings.score` | `guest_rating[0].score` |
| `guest_ratings.number_of_reviewers` | `guest_rating[0].number_of_reviewers` |
| `price` | `base_price` |
| `link` | `url` |
| `ios_url` | `applink.ios_url` |
| `ios_app_store_id` | `applink.ios_app_store_id` |
| `ios_app_name` | `applink.ios_app_name` |
| `android_url` | `applink.android_url` |
| `android_package` | `applink.android_package` |
| `android_app_name` | `applink.android_app_name` |
| `internal_label[0]` | `product_tags[0]`<br>`internal_label` |
| `internal_label[1]` | `product_tags[1]` |

### Trường bí danh cho catalog chuyến bay (Alias fields for flight catalogs)
Bảng dưới đây phác thảo các trường bí danh có sẵn và tên trường hiện tại tương ứng trong catalog chuyến bay. Ví dụ: nếu bạn đưa vào `image[0].url`, trường này sẽ tự động ánh xạ tới `image_link`.

| Existing Field | Corresponding Alias Field |
|---|---|
| `image_link` | `image[0].url` |
| `video_link` | `video[0].url` |
| `link` | `url` |
| `ios_url` | `applink.ios_url` |
| `ios_app_store_id` | `applink.ios_app_store_id` |
| `ios_app_name` | `applink.ios_app_name` |
| `android_url` | `applink.android_url` |
| `android_package` | `applink.android_package` |
| `android_app_name` | `applink.android_app_name` |
| `internal_label[0]` | `product_tags[0]` |
| `internal_label[1]` | `product_tags[1]` |

### Phản hồi

| Field | Type | Description |
|---|---|---|
| code | number | Mã phản hồi. Xem [Phụ lục mã phản hồi (return code)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông điệp phản hồi. Xem [Phụ lục mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | ID bản ghi của yêu cầu, định danh duy nhất cho mỗi yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ feed_log_id | string | ID nhật ký xử lý catalog (catalog handling log ID). |

### Ví dụ

#### cURL
```bash
curl -X POST 'https://business-api.tiktok.com/open_api/v1.3/catalog/product/file/' \
  -H 'Access-Token: YOUR_ACCESS_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{
    "bc_id": "7123456789012345678",
    "catalog_id": "7234567890123456789",
    "feed_id": "7345678901234567890",
    "file_url": "https://example.com/catalog_products_feed.csv",
    "update_mode": "INCREMENTAL"
  }'
```

#### Python
```python
import requests

url = "https://business-api.tiktok.com/open_api/v1.3/catalog/product/file/"
headers = {
    "Access-Token": "YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}
payload = {
    "bc_id": "7123456789012345678",
    "catalog_id": "7234567890123456789",
    "file_url": "https://example.com/catalog_products_feed.csv",
    "update_mode": "INCREMENTAL"
}

response = requests.post(url, headers=headers, json=payload)
data = response.json()
print("Code:", data.get("code"))
print("Feed Log ID:", data.get("data", {}).get("feed_log_id"))
```

#### Ví dụ phản hồi thành công
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202312151025400102422470530400B1A2",
  "data": {
    "feed_log_id": "7312345678901234567"
  }
}
```

---

## Tải lên sản phẩm qua JSON schema (`Upload products via a JSON schema`)
<a id="doc-1740497429681153"></a>
<!-- doc_id: 1740497429681153 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/catalog/product/upload/`

> **Đường dẫn**: API Reference > Catalog Products > Upload products via a JSON schema

**Mục đích**: Sử dụng endpoint này để tải lên các sản phẩm vào catalog theo lô (batch) và bạn có thể tải lên tối đa 5.000 sản phẩm trong một lần gọi. Hệ thống sẽ tiếp nhận các sản phẩm được chỉ định trong yêu cầu theo cơ chế bất đồng bộ, đồng thời trả về một mã ID tác vụ xử lý là `feed_log_id`. Với ID này, bạn có thể kiểm tra trạng thái xử lý thông qua endpoint [/catalog/product/log/](28-catalog-products-p3.md#doc-1740570027173889).

Khác với [/catalog/product/file/](28-catalog-products-p1.md#doc-1740496787164161), endpoint này chủ yếu được dùng để tải lên số lượng sản phẩm nhỏ và cập nhật một số trường cụ thể. Đối với các catalog sản phẩm có tần suất cập nhật cao (nhiều hơn một lần mỗi ngày), khuyến nghị sử dụng endpoint này để tải lên sản phẩm.

> [!NOTE]
> • Mã SKU là duy nhất trong cùng một catalog E-commerce và chỉ thuộc về một feed nhất định. Mọi thao tác đối với một SKU cần được thực hiện dưới feed mà nó trực thuộc.<br>
> • Bạn có thể thực hiện tối đa 1.000 yêu cầu mỗi giờ cho mỗi catalog sản phẩm.<br>
> • Với endpoint này, các sản phẩm được cập nhật theo cơ chế tăng dần (incremental). Dữ liệu của các sản phẩm hiện có sẽ không bị thay thế trừ khi bạn tải lên lại cùng sản phẩm đó.<br>
> • Hình ảnh sản phẩm phải có kích thước tối thiểu từ 500x500 px trở lên. Nếu không, sản phẩm sẽ không được phê duyệt. Chi tiết xem [Yêu cầu hình ảnh sản phẩm (Product Image Requirements)](../09-marketing-api/catalog.md#doc-1739578479392770).

### Header

| Field | Type | Description |
|---|---|---|
| Access-Token | string | **Bắt buộc**. Access token được ủy quyền. Chi tiết xem [Xác thực (Authentication)](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type | string | **Bắt buộc**. Loại thông điệp yêu cầu. Giá trị hợp lệ: `application/json`. |

### Tham số chính (JSON body)

| Field | Data Type | Description |
|---|---|---|
| bc_id | string | **Bắt buộc**. ID của Business Center. |
| catalog_id | string | **Bắt buộc**. ID của Catalog. |
| feed_id | string | ID của Catalog feeds. |
| products | object[] | **Bắt buộc**. Danh sách các sản phẩm. Đối với các trường dữ liệu trong mảng này, xem mục **"Tham số mảng đối tượng `products`"** bên dưới. Tối đa 5.000 sản phẩm mỗi yêu cầu. |

### Tham số mảng đối tượng `products` (`products` object array parameters)
Các tham số trong mảng đối tượng `products` thay đổi tùy theo loại catalog mà bạn muốn tải sản phẩm lên. Bạn có thể xác định loại của catalog dựa trên trường `catalog_type` trả về từ [/catalog/get/](25-catalog-management.md#doc-1740315452868610). Hiện tại, chúng tôi hỗ trợ các loại catalog sau: E-commerce, Khách sạn (Hotel), Chuyến bay (Flight), Điểm đến (Destination), Giải trí (Entertainment), Xe có sẵn (Auto-Inventory), Mẫu xe (Auto-Model), Phim ngắn tập (Mini series), Chung (Generic), và Trực tuyến đến ngoại tuyến (Online-to-offline). Tham khảo các danh sách tham số chi tiết bên dưới.

Để tìm hiểu các bước tải lên sản phẩm cho các loại catalog khác nhau bằng JSON schema, xem [tại đây](../09-marketing-api/catalog.md#doc-1766862002851842).

#### Tham số mảng đối tượng `products` cho catalog E-commerce

| Field | Data Type | Description |
|---|---|---|
| products | object[] | **Bắt buộc**. Danh sách các sản phẩm bạn muốn tải lên. Số lượng tối đa: 5.000 sản phẩm. |
| ↳ sku_id | string | **Bắt buộc**. ID duy nhất cho sản phẩm, chẳng hạn như SKU. Nếu có nhiều bản ghi trùng ID, các bản ghi sau sẽ bị bỏ qua. Bạn cần dùng cùng một ID để thay thế cùng sản phẩm trong feed dữ liệu gốc khi cập nhật. Chỉ sử dụng ký tự Unicode hợp lệ, tránh ký tự điều khiển/hàm. Giới hạn độ dài: 100 ký tự và không chứa emoji. Ví dụ: `TikTok_item_1234`. Không hỗ trợ trùng SKU ID. |
| ↳ title | string | **Bắt buộc**. Tiêu đề của sản phẩm. Chỉ sử dụng ký tự Unicode hợp lệ. Không bao gồm văn bản quảng cáo như "miễn phí vận chuyển, chất lượng cao, bán buôn". Giới hạn: 500 ký tự và không chứa emoji. Ví dụ: `T-Shirt (Unisex)`. |
| ↳ description | string | **Bắt buộc**. Mô tả ngắn về sản phẩm. Giới hạn độ dài: 10.000 ký tự. Ví dụ: `A vibrant crewneck for all shapes and sizes. Made from 100% cotton.` |
| ↳ availability | string | **Bắt buộc**. Tình trạng còn hàng hiện tại của sản phẩm trong cửa hàng của bạn.<br>Giá trị enum:<br>• `IN_STOCK`: còn hàng.<br>• `AVAILABLE_FOR_ORDER`: có sẵn để đặt hàng.<br>• `PREORDER`: đặt hàng trước.<br>• `OUT_OF_STOCK`: hết hàng.<br>• `DISCONTINUED`: ngừng sản xuất/kinh doanh. Ví dụ: `IN_STOCK`. |
| ↳ brand | string | **Bắt buộc**. Tên thương hiệu của sản phẩm. Giới hạn: 150 ký tự. Ví dụ: `TikTok`. |
| ↳ image_url | string | **Bắt buộc**. URL của hình ảnh sản phẩm. Hình ảnh phải có kích thước từ 500x500 px trở lên, định dạng JPG hoặc PNG. Chi tiết xem [Yêu cầu hình ảnh sản phẩm](../09-marketing-api/catalog.md#doc-1739578479392770). Ví dụ: `https://www.tiktok.com/t_shirt_image_001.jpg`. |
| ↳ additional_image_urls | string[] | Danh sách URL hình ảnh bổ sung cho sản phẩm. Tối đa: 10 hình ảnh. Kích thước tối thiểu 500x500 px, định dạng JPG hoặc PNG. Nếu URL chứa dấu phẩy (,), hãy URL-encode thành `%2C`. Ví dụ: `["https://www.tiktok.com/t_shirt_image_002.jpg","https://www.tiktok.com/t_shirt_image_003.jpg"]`. |
| ↳ video_url | string | URL của video sử dụng trong quảng cáo của bạn. Tỷ lệ khung hình khuyến nghị 9:16 (dọc); độ phân giải khuyến nghị: ≥720*1280; bitrate khuyến nghị: ≥516kbps; âm thanh: bật kèm phụ đề. Ví dụ: `https://www.tiktok.com/tiktok_t_shirt`. |
| ↳ item_group_id | string | SPU ID của sản phẩm. Cung cấp cùng `item_group_id` cho tất cả các sản phẩm là biến thể của một sản phẩm cụ thể (ví dụ: áo polo đỏ là biến thể của áo polo). Ví dụ: `TikTok_1234_sample`. |
| ↳ google_product_category | string | Giá trị cài đặt sẵn từ hệ thống phân loại danh mục sản phẩm của Google (Google product taxonomy). Chỉ hỗ trợ tối đa 3 cấp. Ví dụ: `Apparel & Accessories > Clothing > Shirts`. |
| ↳ global_trade_item_number | string | Mã số thương phẩm toàn cầu (GTIN) của sản phẩm. Ví dụ: `3234567890126`. |
| ↳ manufacturer_part_number | string | Mã số bộ phận của nhà sản xuất (MPN) của sản phẩm. Ví dụ: `12433`. |
| ↳ product_detail | object | **Bắt buộc**. Thông tin chi tiết khác của sản phẩm. |
| ↳↳ condition | string | **Bắt buộc**. Tình trạng hiện tại của sản phẩm. Giá trị enum: `NEW` (mới), `REFURBISHED` (tân trang), `USED` (đã qua sử dụng). Ví dụ: `NEW`. |
| ↳↳ age_group | string | Nhóm độ tuổi của sản phẩm.<br>Giá trị enum:<br>• `NEW_BORN`: sơ sinh (0-3 tháng tuổi).<br>• `INFANT`: trẻ nhỏ (3-12 tháng tuổi).<br>• `TODDLER`: trẻ tập đi (1-5 tuổi).<br>• `KIDS`: trẻ em (5-13 tuổi).<br>• `ADULT`: người lớn (từ 13 tuổi trở lên). Ví dụ: `ADULT`. |
| ↳↳ color | string | Màu sắc của sản phẩm. Giới hạn: 100 ký tự. Ví dụ: `blue`. |
| ↳↳ gender | string | Giới tính mục tiêu của sản phẩm. Giá trị enum: `MALE`, `FEMALE`, `UNISEX`. Ví dụ: `UNISEX`. |
| ↳↳ material | string | Chất liệu tạo nên sản phẩm (cotton, denim, da...). Giới hạn: 200 ký tự. Ví dụ: `cotton`. |
| ↳↳ pattern | string | Họa tiết hoặc hình in trên sản phẩm. Giới hạn: 100 ký tự. Ví dụ: `stripes1`. |
| ↳↳ product_category | string | Danh mục của sản phẩm. Chỉ yêu cầu 3 cấp đầu tiên. Ví dụ: `Apparel & Accessories > Clothing > Shirts`. |
| ↳↳ shipping | string | Loại hình và chi phí vận chuyển. Định dạng khuyến nghị: `COUNTRY:STATE:SHIPPING_TYPE:PRICE`. Ví dụ: `US:CA:Ground:9.99 USD`. |
| ↳↳ shipping_weight | string | Trọng lượng vận chuyển của sản phẩm. Đơn vị được phép: `lb`, `oz`, `g`, `kg`. Ví dụ: `1 oz`, `1 kg`. |
| ↳↳ size | string | Kích thước của sản phẩm. Ví dụ: `Small`, `Large`, `Extra Large`. |
| ↳↳ tax | string | Mức thuế áp dụng cho sản phẩm. |
| ↳ price_info | object | **Bắt buộc**. Thông tin giá sản phẩm. |
| ↳↳ price | float | **Bắt buộc**. Giá cơ sở của sản phẩm. Ví dụ: `30`. |
| ↳↳ currency | string | Đơn vị tiền tệ. Nếu chỉ định, phải theo quốc gia mục tiêu của catalog. Nếu không chỉ định, đơn vị tiền tệ mặc định của catalog sẽ được áp dụng. Ví dụ: `USD`. |
| ↳↳ sale_price | float | Giá khuyến mãi giảm giá của sản phẩm nếu đang giảm giá. Ví dụ: `20`. |
| ↳↳ sale_price_effective_date | string | Thời gian bắt đầu và kết thúc giảm giá, định dạng `YYYY-MM-DDT23:59+00:00/YYYY-MM-DDT23:59+00:00`. Ngày bắt đầu phải trước ngày kết thúc. Không truyền trường này nếu giá giảm áp dụng vô thời hạn. Ví dụ: `2023-12-11T23:59+00:00/2023-12-15T23:59+00:00`. |
| ↳ landing_page | object | **Bắt buộc**. Thông tin trang đích (landing page). |
| ↳↳ landing_page_url | string | **Bắt buộc**. URL của trang đích nơi người dùng có thể xem và mua sản phẩm. Ví dụ: `https://www.tiktok.com/tiktok_t_shirt`. |
| ↳↳ ios_url | string | Custom scheme URL cho ứng dụng iOS. Ví dụ: `iOS://electronic`. |
| ↳↳ ios_app_store_id | string | App Store ID cho ứng dụng iOS. Ví dụ: `1234`. |
| ↳↳ ios_app_name | string | Tên ứng dụng iOS hiển thị. Ví dụ: `Electronic iOS`. |
| ↳↳ iphone_app_store_id | string | App Store ID cho ứng dụng iPhone. Ví dụ: `1234`. |
| ↳↳ iphone_app_name | string | Tên ứng dụng iPhone hiển thị. Ví dụ: `Electronic iOS`. |
| ↳↳ ipad_app_store_id | string | App Store ID cho ứng dụng iPad. Ví dụ: `1234`. |
| ↳↳ ipad_app_name | string | Tên ứng dụng iPad hiển thị. Ví dụ: `Electronic iOS`. |
| ↳↳ android_url | string | Custom scheme URL cho ứng dụng Android. Ví dụ: `android://electronic`. |
| ↳↳ android_package | string | Tên gói Android (package name). Ví dụ: `com.electronic`. |
| ↳↳ android_app_name | string | Tên ứng dụng Android hiển thị. Ví dụ: `Electronic Android`. |
| ↳ extra_info | object | Thông tin bổ sung. |
| ↳↳ custom_label_0 | string | Thông tin bổ sung tùy chỉnh về sản phẩm. Không giới hạn độ dài. |
| ↳↳ custom_label_1 | string | Thông tin bổ sung tùy chỉnh về sản phẩm. Không giới hạn độ dài. |
| ↳↳ custom_label_2 | string | Thông tin bổ sung tùy chỉnh về sản phẩm. Không giới hạn độ dài. |
| ↳↳ custom_label_3 | string | Thông tin bổ sung tùy chỉnh về sản phẩm. Không giới hạn độ dài. |
| ↳↳ custom_label_4 | string | Thông tin bổ sung tùy chỉnh về sản phẩm. Không giới hạn độ dài. |

#### Tham số mảng đối tượng `products` cho catalog khách sạn (hotel)

| Field | Data Type | Description |
|---|---|---|
| products | object[] | **Bắt buộc**. Danh sách các sản phẩm (phòng khách sạn) bạn muốn tải lên. Tối đa: 5.000. |
| ↳ hotel_id | string | **Bắt buộc**. ID duy nhất cho khách sạn. Giới hạn độ dài: 100 ký tự. |
| ↳ name | string | **Bắt buộc**. Tên của khách sạn. Giới hạn độ dài: 150 ký tự. |
| ↳ description | string | Mô tả ngắn về phòng khách sạn. Giới hạn: 10.000 ký tự. Ví dụ: `Free Wifi, Free Breakfast, Free Cancellation`. |
| ↳ availability | string | Tình trạng phòng hiện tại. Giá trị enum: `IN_STOCK` (có sẵn để đặt), `OUT_OF_STOCK` (hết phòng). Ví dụ: `IN_STOCK`. |
| ↳ brand | string | **Bắt buộc**. Tên thương hiệu khách sạn. Giới hạn: 150 ký tự. |
| ↳ image_url | string | **Bắt buộc**. URL hình ảnh phòng khách sạn. Kích thước tối thiểu 500x500 px, định dạng JPG hoặc PNG. Chi tiết xem [Yêu cầu hình ảnh](../09-marketing-api/catalog.md#doc-1739578479392770). Ví dụ: `https://www.tiktok.com/hotel_room_image_001.jpg`. |
| ↳ additional_image_urls | string[] | Danh sách URL hình ảnh bổ sung. Tối đa: 20 URL. Kích thước tối thiểu 500x500 px. Nếu URL chứa dấu phẩy, mã hóa thành `%2C`. Ví dụ: `["https://www.tiktok.com/hotel_room_image_002.jpg","https://www.tiktok.com/hotel_room_image_003.jpg"]`. |
| ↳ video_url | string | URL video sử dụng trong quảng cáo. Tỷ lệ khuyến nghị 9:16 (dọc); độ phân giải: ≥720*1280; bitrate: ≥516kbps; âm thanh kèm phụ đề. Ví dụ: `https://www.tiktok.com/hotel.mp4`. |
| ↳ hotel_category | string[] | Danh mục khách sạn. Tối đa: 3 giá trị. Xem bảng giá trị cho `hotel_category` bên dưới. |
| ↳ hotel_retailer_id | string | ID duy nhất cho nhà bán lẻ/đại lý khách sạn. Giới hạn: 100 ký tự. |
| ↳ address | object | **Bắt buộc**. Thông tin địa chỉ khách sạn. |
| ↳↳ address | string | **Bắt buộc**. Tên đầy đủ của địa chỉ đường phố chính của khách sạn. Giới hạn: 150 ký tự. |
| ↳↳ secondary_address | string | Địa chỉ đường phố phụ của khách sạn. Giới hạn: 150 ký tự. |
| ↳↳ tertiary_address | string | Địa chỉ đường phố cấp 3 của khách sạn. Giới hạn: 150 ký tự. |
| ↳↳ city | string | **Bắt buộc**. Thành phố nơi khách sạn tọa lạc. Giới hạn: 150 ký tự. |
| ↳↳ region | string | Khu vực (bang/tỉnh) nơi khách sạn tọa lạc. Giới hạn: 150 ký tự. |
| ↳↳ country | string | **Bắt buộc**. Quốc gia nơi khách sạn tọa lạc. Giới hạn: 150 ký tự. |
| ↳ neighborhood | string | Khu vực lân cận/khu phố nơi khách sạn tọa lạc. Giới hạn: 100 ký tự. Ví dụ: `Bangkok Old Town`. |
| ↳ postal_code | string | Mã bưu chính hoặc mã zip của khách sạn. Giới hạn: 150 ký tự. |
| ↳ latitude | float | Vĩ độ vị trí khách sạn. Phạm vi: [-90, 90]. Ví dụ: `37.484100`. |
| ↳ longitude | float | Kinh độ vị trí khách sạn. Phạm vi: [-180, 180]. Ví dụ: `-122.148252`. |
| ↳ margin_level | integer | Tỷ lệ phần trăm trên giá cơ sở (`price`) mà khách sạn thu làm tiền đặt cọc. Phạm vi: [1, 10]. Ví dụ: 10 nghĩa là đặt cọc 10%. |
| ↳ loyalty_program | string | Chương trình khách hàng thân thiết của khách sạn. Xem bảng giá trị cho `loyalty_program` bên dưới. |
| ↳ guest_ratings | object[] | Thông tin đánh giá của khách lưu trú. Tối đa: 1 đối tượng. |
| ↳↳ rating_system | string | Hệ thống đánh giá khách sạn. Giới hạn: 150 ký tự. Ví dụ: `Expedia`, `Tripadvisor`. |
| ↳↳ max_score | integer | Điểm số cao nhất của hệ thống đánh giá. Phạm vi: [0, 100]. |
| ↳↳ score | float | Điểm số thực tế của khách sạn. Phạm vi: ≥ 0. |
| ↳↳ number_of_reviewers | integer | Số lượng khách đã gửi đánh giá. Phạm vi: ≥ 0. |
| ↳ star_rating | integer | Số sao khách sạn được xếp hạng bởi tổ chức chuyên nghiệp (thường tối đa 5 sao). |
| ↳ room_type | string[] | Các loại phòng khách sạn. Tối đa: 3 giá trị. Xem bảng giá trị cho `room_type` bên dưới. |
| ↳ priority | integer | Thứ tự ưu tiên của khách sạn. Phạm vi: 0-5. Mặc định: 0. Giá trị cao hơn thể hiện mức độ ưu tiên cao hơn. |
| ↳ price_info | object | **Bắt buộc**. Thông tin giá phòng. |
| ↳↳ price | float | **Bắt buộc**. Giá cơ sở cho một đêm phòng khách sạn. Ví dụ: `30`. |
| ↳↳ currency | string | Đơn vị tiền tệ. Theo quốc gia mục tiêu của catalog. Mặc định là tiền tệ của catalog nếu không truyền. Ví dụ: `USD`. |
| ↳↳ sale_price | float | Giá khuyến mãi giảm giá cho một đêm phòng. Phải nhỏ hơn `price`. Ví dụ: `20`. |
| ↳ landing_page | object | Thông tin trang đích. |
| ↳↳ landing_page_url | string | URL trang đích nơi người dùng có thể xem và đặt phòng. Ví dụ: `https://www.tiktok.com/tiktok_hotel`. |
| ↳↳ ios_url | string | Custom scheme URL cho ứng dụng iOS. Ví dụ: `iOS://electronic`. |
| ↳↳ ios_app_store_id | string | App Store ID cho iOS. Ví dụ: `1234`. |
| ↳↳ ios_app_name | string | Tên ứng dụng iOS hiển thị. Ví dụ: `Electronic iOS`. |
| ↳↳ android_url | string | Custom scheme URL cho Android. Ví dụ: `android://electronic`. |
| ↳↳ android_package | string | Tên gói Android. Ví dụ: `com.electronic`. |
| ↳↳ android_app_name | string | Tên ứng dụng Android hiển thị. Ví dụ: `Electronic Android`. |
| ↳ extra_info | object | Thông tin bổ sung. |
| ↳↳ custom_label_0 | string | Nhãn tùy chỉnh bổ sung về sản phẩm. Không giới hạn độ dài. |
| ↳↳ custom_label_1 | string | Nhãn tùy chỉnh bổ sung về sản phẩm. Không giới hạn độ dài. |
| ↳↳ custom_label_2 | string | Nhãn tùy chỉnh bổ sung về sản phẩm. Không giới hạn độ dài. |
| ↳↳ custom_label_3 | string | Nhãn tùy chỉnh bổ sung về sản phẩm. Không giới hạn độ dài. |
| ↳↳ custom_label_4 | string | Nhãn tùy chỉnh bổ sung về sản phẩm. Không giới hạn độ dài. |
| ↳↳ internal_label_0 | string | Nhãn nội bộ gán cho khách sạn, dùng để lọc khi tạo bộ sản phẩm (product sets). Chỉ bạn nhìn thấy nhãn này. Khác với custom label, internal label có thể sửa đổi mà không cần xét duyệt lại. Giới hạn: 100 ký tự. |
| ↳↳ internal_label_1 | string | Nhãn nội bộ gán cho khách sạn thứ hai. Giới hạn: 100 ký tự. |

##### Danh sách giá trị cho `hotel_category`

| Value | Description |
|---|---|
| `ACCOMMODATION` | Nơi lưu trú (Accommodation) |
| `APARTMENT` | Căn hộ (Apartment) |
| `BEACH_HOTEL` | Khách sạn bãi biển (Beach Hotel) |
| `BED_BREAKFAST` | Phòng nghỉ kèm bữa sáng (Bed & Breakfast) |
| `BOAT` | Thuyền (Boats) |
| `CABIN` | Nhà gỗ (Cabin) |
| `CAMPING` | Cắm trại (Camping) |
| `CAPSULE_HOTEL` | Khách sạn con nhộng (Capsule Hotel) |
| `CASTLE` | Lâu đài (Castle) |
| `CHALET` | Nhà nghỉ vùng núi (Chalet) |
| `CONDO` | Chung cư (Condo) |
| `CONDO_RESORT` | Resort chung cư (Condo Resort) |
| `COTTAGE` | Nhà tranh/nhà thôn quê (Cottage) |
| `COUNTRY_HOUSE` | Nhà đồng quê (Country House) |
| `CRUISE` | Du thuyền (Cruise) |
| `FAMILY_HOTEL` | Khách sạn gia đình (Family Hotel) |
| `FARM` | Nông trại (Farm) |
| `FARM_STAYS` | Nông trại nghỉ dưỡng (Farm Stays) |
| `GUEST_HOUSE` | Nhà khách (Guest House) |
| `HOLIDAY_PARK` | Công viên nghỉ dưỡng (Holiday Park) |
| `HOSTAL` | Nhà trọ bình dân (Hostal) |
| `HOSTEL` | Nhà trọ thanh niên (Hostel) |
| `HOSTEL_BACKPACKER_ACCOMMODATION` | Nhà trọ du lịch bụi (Hostel/Backpacker) |
| `HOTEL` | Khách sạn (Hotel) |
| `HOUSEBOAT` | Nhà thuyền (Houseboat) |
| `INN` | Quán trọ ven đường (Inn) |
| `LODGE` | Nhà nghỉ sinh thái (Lodge) |
| `LOVE_HOTELS` | Khách sạn tình nhân (Love Hotels) |
| `LUXURY_TENT` | Lều sang trọng (Luxury tents) |
| `MOTEL` | Nhà nghỉ ven xa lộ (Motel) |
| `PALACE` | Cung điện (Palace) |
| `PENSION` | Nhà trọ gia đình (Pension) |
| `POUSADA` | Nhà nghỉ truyền thống (Pousada) |
| `PRIVATE_VACATION_HOME` | Biệt thự nghỉ dưỡng riêng (Private Vacation Home) |
| `RANCH` | Trang trại chăn nuôi (Ranch) |
| `RESIDENCE` | Khu dân cư nghỉ dưỡng (Residence) |
| `RESORT` | Khu nghỉ dưỡng (Resort) |
| `RESORT_VILLAGES` | Làng nghỉ dưỡng (Resort Villages) |
| `RIAD` | Nhà truyền thống Ma-rốc (Riad) |
| `RYOKAN` | Lữ quán truyền thống Nhật Bản (Ryokan) |
| `SAFARI` | Khu nghỉ dưỡng Safari |
| `SERVICED_APARTMENT` | Căn hộ dịch vụ (Serviced Apartment) |
| `TOWNHOUSE` | Nhà phố liền kề (Townhouse) |
| `TREE_HOUSE` | Nhà trên cây (Tree House) |
| `VILLA` | Biệt thự (Villa) |

##### Danh sách giá trị cho `loyalty_program`

| Value | Description |
|---|---|
| `ACCOR_LIVE_LIMITLESS_ALL` | Accor Live Limitless (ALL) |
| `AMAN_CLUB` | Aman Club |
| `BANYAN_TREE_DISCOVERY` | Banyan Tree DISCOVERY |
| `BEST_WESTERN_REWARDS` | Best Western Rewards |
| `CHOICE_PRIVILEGES` | Choice Privileges |
| `FOUR_SEASONS_LOYALTY_PROGRAM` | Four Seasons Loyalty Program |
| `HILTON_HONORS` | Hilton Honors |
| `IHG_REWARDS_CLUB` | IHG Rewards Club |
| `KIMPTON_KARMA_REWARDS` | Kimpton Karma Rewards |
| `LEADERS_CLUB_THE_LEADING_HOTELS_OF_THE_WORLD` | Leaders Club (The Leading Hotels of the World) |
| `LOEWS_LOVES_YOU` | Loews Loves You |
| `MARRIOTT_BONVOY` | Marriott Bonvoy |
| `MOTEL_6_MY6` | Motel 6 My6 |
| `RADISSON_REWARDS` | Radisson Rewards |
| `SCANDIC_FRIENDS` | Scandic Friends |
| `SONESTA_TRAVEL_PASS` | Sonesta Travel Pass |
| `TRUMP_CARD` | Trump Card |
| `WORLD_OF_HYATT` | World of Hyatt |
| `WYNDHAM_REWARDS` | Wyndham Rewards |

##### Danh sách giá trị cho `room_type`

| Value | Description |
|---|---|
| `ACCESSIBLE_ROOM` | Phòng hỗ trợ tiếp cận (Accessible Room) |
| `ALLERGY_FREE_ROOM` | Phòng chống dị ứng (Allergy-Free Room) |
| `APARTMENT_ROOM` | Phòng dạng căn hộ (Apartment Room) |
| `APARTMENT_SUITE` | Suite căn hộ (Apartment Suite) |
| `ARTIST_ROOM` | Phòng nghệ sĩ (Artist Room) |
| `BEACHFRONT_ROOM` | Phòng mặt biển (Beachfront Room) |
| `BUSINESS_ROOM` | Phòng thương gia (Business Room) |
| `CABIN_ROOM` | Phòng nhà gỗ (Cabin Room) |
| `DELUXE_ROOM` | Phòng Deluxe |
| `DOUBLE_ROOM` | Phòng giường đôi (Double Room) |
| `DUPLEX_SUITE` | Suite thông tầng (Duplex Suite) |
| `ECO_ROOM` | Phòng sinh thái (Eco Room) |
| `EXECUTIVE_ROOM` | Phòng Executive |
| `EXECUTIVE_SUITE` | Suite Executive |
| `FAMILY_ROOM` | Phòng gia đình (Family Room) |
| `FITNESS_ROOM` | Phòng tập thể hình (Fitness Room) |
| `FLOATING_ROOM` | Phòng nổi (Floating Room) |
| `GARDEN_SUITE` | Suite hướng vườn (Garden Suite) |
| `GARDEN_VIEW_ROOM` | Phòng nhìn ra vườn (Garden View Room) |
| `GLAMPING_TENT` | Lều cắm trại cao cấp (Glamping Tent) |
| `GRAND_SUITE` | Grand Suite |
| `HISTORICAL_ROOM` | Phòng phong cách lịch sử (Historical Room) |
| `HONEYMOON_SUITE` | Suite trăng mật (Honeymoon Suite) |
| `JACUZZI_ROOM` | Phòng có bồn sục Jacuzzi |
| `JUNIOR_SUITE` | Junior Suite |
| `LOFT_ROOM` | Phòng gác mái (Loft Room) |
| `LOFT_SUITE` | Suite gác mái (Loft Suite) |
| `LUXURY_SUITE` | Suite sang trọng (Luxury Suite) |
| `MOUNTAIN_CHALET` | Nhà nghỉ trên núi (Mountain Chalet) |
| `MOUNTAIN_LODGE` | Nhà nghỉ dưỡng trên núi (Mountain Lodge) |
| `MOUNTAIN_VIEW_ROOM` | Phòng nhìn ra núi (Mountain View Room) |
| `PENTHOUSE_SUITE` | Suite tầng thượng (Penthouse Suite) |
| `PET_FRIENDLY_ROOM` | Phòng cho phép mang thú cưng (Pet-Friendly Room) |
| `POOL_VILLA_ROOM` | Biệt thự có hồ bơi (Pool Villa Room) |
| `POOLSIDE_ROOM` | Phòng cạnh hồ bơi (Poolside Room) |
| `PRESIDENTIAL_SUITE` | Phòng Tổng thống (Presidential Suite) |
| `PRIVATE_VILLA_ROOM` | Biệt thự riêng biệt (Private Villa Room) |
| `ROMANTIC_SUITE` | Suite lãng mạn (Romantic Suite) |
| `RUSTIC_ROOM` | Phòng mộc mạc (Rustic Room) |
| `SEA_VIEW_ROOM` | Phòng nhìn ra biển (Sea View Room) |
| `SINGLE_ROOM` | Phòng đơn (Single Room) |
| `SKI_IN_SKI_OUT_ROOM` | Phòng trượt tuyết trực tiếp (Ski-in/Ski-out Room) |
| `SKI_ROOM` | Phòng trượt tuyết (Ski Room) |
| `SOUNDPROOF_ROOM` | Phòng cách âm (Soundproof Room) |
| `STUDIO_APARTMENT` | Căn hộ Studio |
| `STUDIO_ROOM` | Phòng Studio |
| `SUITE` | Phòng Suite |
| `TERRACE_ROOM` | Phòng có sân hiên (Terrace Room) |
| `TREEHOUSE_ROOM` | Phòng trên cây (Treehouse Room) |
| `TWIN_ROOM` | Phòng 2 giường đơn (Twin Room) |
| `WATER_SUITE` | Suite trên mặt nước (Water Suite) |
| `WELLNESS_ROOM` | Phòng chăm sóc sức khỏe (Wellness Room) |

#### Tham số mảng đối tượng `products` cho catalog chuyến bay (flight)

| Field | Data Type | Description |
|---|---|---|
| products | object[] | **Bắt buộc**. Danh sách các sản phẩm (chuyến bay) bạn muốn tải lên. Tối đa: 5.000. |
| ↳ origin_airport | string | **Bắt buộc**. Sân bay xuất phát của chuyến bay, định dạng mã 3 chữ cái IATA. Ví dụ: `AAR`. Không được chỉ định trùng cặp sân bay xuất phát và đích đến trong cùng một catalog. |
| ↳ destination_airport | string | **Bắt buộc**. Sân bay đích đến của chuyến bay, định dạng mã 3 chữ cái IATA. Ví dụ: `ABD`. Không được chỉ định trùng cặp sân bay xuất phát và đích đến trong cùng một catalog. |
| ↳ origin_city | string | Tên thành phố xuất phát. Giới hạn: 150 ký tự. |
| ↳ destination_city | string | Tên thành phố đích đến. Giới hạn: 150 ký tự. |
| ↳ description | string | Mô tả ngắn về chuyến bay. Giới hạn: 10.000 ký tự. |
| ↳ cabin_class | string | Hạng ghế/khoang hành khách của chuyến bay.<br>Giá trị enum:<br>• `FIRST_CLASS`: Hạng nhất (First Class).<br>• `FIRST_CLASS_SUITE`: Suite hạng nhất.<br>• `BUSINESS_CLASS`: Hạng thương gia (Business Class).<br>• `BUSINESS_CLASS_SUITE`: Suite hạng thương gia.<br>• `COMFORT_CLASS`: Hạng tiện nghi (Comfort Class).<br>• `ECONOMY_CLASS`: Hạng phổ thông (Economy Class).<br>• `BASIC_ECONOMY`: Phổ thông tiết kiệm (Basic Economy).<br>• `STANDARD_ECONOMY`: Phổ thông tiêu chuẩn (Standard Economy).<br>• `PREMIUM_ECONOMY`: Phổ thông đặc biệt (Premium Economy).<br>• `LIE_FLAT_SEAT`: Ghế nằm phẳng (Lie Flat Seat).<br>• `CHARTER_CLASS`: Chuyến bay thuê chuyến (Charter Class).<br>• `ELITE_CLASS`: Hạng ưu tú (Elite Class).<br>• `QUIET_CLASS`: Khoang yên tĩnh (Quiet Class). |
| ↳ airline_company | string | Tên hãng hàng không vận hành chuyến bay.<br>Giá trị enum: `AEROFLOT`, `AIR_FRANCE_KLM_GROUP`, `ALASKA_AIRLINES`, `ANA`, `AMERICAN_AIRLINES`, `BRITISH_AIRWAYS`, `CATHAY_PACIFIC`, `CHINA_SOUTHERN_AIRLINES`, `CHINA_EASTERN_AIRLINES`, `DELTA_AIR_LINES`, `EMIRATES`, `JAPAN_AIRLINES`, `JETBLUE_AIRWAYS`, `KLM_ROYAL_DUTCH_AIRLINES`, `LUFTHANSA_GROUP`, `QANTAS_AIRWAYS`, `QATAR_AIRWAYS`, `SINGAPORE_AIRLINES`, `SOUTHWEST_AIRLINES`, `TURKISH_AIRLINES`, `UNITED_AIRLINES`, `VIRGIN_ATLANTIC`. |
| ↳ image_url | string | **Bắt buộc**. URL hình ảnh chuyến bay. Kích thước tối thiểu 500x500 px, định dạng JPG hoặc PNG. Ví dụ: `https://www.tiktok.com/flight_image_001.jpg`. |
| ↳ additional_image_urls | string[] | Danh sách URL hình ảnh bổ sung. Tối đa: 20 URL. Kích thước ≥ 500x500 px. Nếu có dấu phẩy, thay bằng `%2C`. Ví dụ: `["https://www.tiktok.com/flight_image_002.jpg","https://www.tiktok.com/flight_image_003.jpg"]`. |
| ↳ video_url | string | URL video sử dụng trong quảng cáo. Khuyến nghị: 9:16 (dọc), ≥720*1280, ≥516kbps, có âm thanh và phụ đề. Ví dụ: `https://www.tiktok.com/flight.mp4`. |
| ↳ priority | integer | Độ ưu tiên của chuyến bay. Phạm vi: 0-5. Mặc định: 0. |
| ↳ price_info | object | Thông tin giá chuyến bay. |
| ↳↳ price | float | Giá cơ sở của chuyến bay. Ví dụ: `3000`. |
| ↳↳ currency | string | Đơn vị tiền tệ. Theo quốc gia mục tiêu của catalog. Ví dụ: `USD`. |
| ↳↳ sale_price | float | Giá khuyến mãi giảm giá của chuyến bay. Phải nhỏ hơn `price`. Ví dụ: `2500`. |
| ↳ landing_page | object | Thông tin trang đích. |
| ↳↳ landing_page_url | string | URL trang đích nơi người dùng có thể đặt vé máy bay. Ví dụ: `https://www.tiktok.com/tiktok_flight`. |
| ↳↳ ios_url | string | Custom scheme URL cho iOS. Ví dụ: `iOS://electronic`. |
| ↳↳ ios_app_store_id | string | App Store ID cho iOS. Ví dụ: `1234`. |
| ↳↳ ios_app_name | string | Tên ứng dụng iOS. Ví dụ: `Electronic iOS`. |
| ↳↳ android_url | string | Custom scheme URL cho Android. Ví dụ: `android://electronic`. |
| ↳↳ android_package | string | Tên gói Android. Ví dụ: `com.electronic`. |
| ↳↳ android_app_name | string | Tên ứng dụng Android. Ví dụ: `Electronic Android`. |
| ↳ extra_info | object | Thông tin bổ sung. |
| ↳↳ custom_label_0 | string | Nhãn tùy chỉnh bổ sung về chuyến bay. Không giới hạn độ dài. |
| ↳↳ custom_label_1 | string | Nhãn tùy chỉnh bổ sung về chuyến bay. Không giới hạn độ dài. |
| ↳↳ custom_label_2 | string | Nhãn tùy chỉnh bổ sung về chuyến bay. Không giới hạn độ dài. |
| ↳↳ custom_label_3 | string | Nhãn tùy chỉnh bổ sung về chuyến bay. Không giới hạn độ dài. |
| ↳↳ custom_label_4 | string | Nhãn tùy chỉnh bổ sung về chuyến bay. Không giới hạn độ dài. |
| ↳↳ internal_label_0 | string | Nhãn nội bộ gán cho chuyến bay để lọc khi tạo bộ sản phẩm. Giới hạn: 100 ký tự. |
| ↳↳ internal_label_1 | string | Nhãn nội bộ thứ hai gán cho chuyến bay. Giới hạn: 100 ký tự. |

#### Tham số mảng đối tượng `products` cho catalog điểm đến du lịch (destination)

| Field | Data Type | Description |
|---|---|---|
| products | object[] | **Bắt buộc**. Danh sách các sản phẩm (điểm đến du lịch) bạn muốn tải lên. Tối đa: 5.000. |
| ↳ destination_id | string | **Bắt buộc**. ID duy nhất cho điểm đến du lịch. Giới hạn độ dài: 100 ký tự. |
| ↳ destination_name | string | **Bắt buộc**. Tên của điểm đến du lịch. Giới hạn độ dài: 150 ký tự. |
| ↳ description | string | **Bắt buộc**. Mô tả ngắn về điểm đến. Giới hạn: 10.000 ký tự. Ví dụ: `A visit to one of the most famous sights in London.` |
| ↳ image_url | string | **Bắt buộc**. URL hình ảnh của điểm đến. Kích thước tối thiểu 500x500 px, định dạng JPG hoặc PNG. Ví dụ: `https://www.tiktok.com/destination_image_001.jpg`. |
| ↳ additional_image_urls | string[] | Danh sách URL hình ảnh bổ sung. Tối đa: 10 URL. Kích thước ≥ 500x500 px. Nếu URL chứa dấu phẩy, mã hóa thành `%2C`. Ví dụ: `["https://www.tiktok.com/destination_image_002.jpg","https://www.tiktok.com/destination_image_003.jpg"]`. |
| ↳ video_url | string | URL video sử dụng trong quảng cáo. Khuyến nghị: 9:16 (dọc), ≥720*1280, ≥516kbps, có âm thanh kèm phụ đề. Ví dụ: `https://www.tiktok.com/destination.mp4`. |
| ↳ address | object | **Bắt buộc**. Thông tin địa chỉ điểm đến. |
| ↳↳ address | string | **Bắt buộc**. Địa chỉ đường phố của điểm đến. Giới hạn: 150 ký tự. |
| ↳↳ city | string | **Bắt buộc**. Thành phố nơi điểm đến tọa lạc. Giới hạn: 150 ký tự. |
| ↳↳ region | string | **Bắt buộc**. Khu vực (bang/tỉnh) nơi điểm đến tọa lạc. Giới hạn: 150 ký tự. |
| ↳↳ country | string | **Bắt buộc**. Quốc gia nơi điểm đến tọa lạc. Giới hạn: 150 ký tự. |
| ↳ neighborhood | string | Khu vực lân cận của điểm đến. Giới hạn: 100 ký tự. Ví dụ: `Bangkok Old Town`. |
| ↳ postal_code | string | Mã bưu chính hoặc mã zip của điểm đến. |
| ↳ latitude | float | Vĩ độ của điểm đến. Phạm vi: [-90, 90]. Ví dụ: `37.484100`. |
| ↳ longitude | float | Kinh độ của điểm đến. Phạm vi: [-180, 180]. Ví dụ: `-122.148252`. |
| ↳ types | string[] | **Bắt buộc**. Loại hoặc các loại điểm đến du lịch. Có thể chỉ định một hoặc nhiều loại mô tả điểm đến (ví dụ với New York có thể truyền `["city","sightseeing"]`). Tối đa: 20 loại. |
| ↳ price_info | object | Thông tin giá điểm đến. |
| ↳↳ price | float | Giá trung bình hoặc thấp nhất cho điểm đến. Ví dụ: `30`. |
| ↳↳ currency | string | Đơn vị tiền tệ. Theo quốc gia mục tiêu của catalog. Ví dụ: `USD`. |
| ↳↳ sale_price | float | Giá khuyến mãi giảm giá cho điểm đến. Ví dụ: `20`. |
| ↳ landing_page | object | Thông tin trang đích. |
| ↳↳ landing_page_url | string | URL trang đích nơi người dùng có thể xem thông tin chi tiết về điểm đến. Ví dụ: `https://www.tiktok.com/tiktok_destination`. |
| ↳↳ ios_url | string | Custom scheme URL cho iOS. Ví dụ: `iOS://electronic`. |
| ↳↳ ios_app_store_id | string | App Store ID cho iOS. Ví dụ: `1234`. |
| ↳↳ ios_app_name | string | Tên ứng dụng iOS. Ví dụ: `Electronic iOS`. |
| ↳↳ android_url | string | Custom scheme URL cho Android. Ví dụ: `android://electronic`. |
| ↳↳ android_package | string | Tên gói ứng dụng Android. Ví dụ: `com.electronic`. |
| ↳↳ android_app_name | string | Tên ứng dụng Android. Ví dụ: `Electronic Android`. |
| ↳ extra_info | object | Thông tin bổ sung. |
| ↳↳ custom_label_0 | string | Nhãn tùy chỉnh bổ sung về điểm đến. Không giới hạn độ dài. |
| ↳↳ custom_label_1 | string | Nhãn tùy chỉnh bổ sung về điểm đến. Không giới hạn độ dài. |
| ↳↳ custom_label_2 | string | Nhãn tùy chỉnh bổ sung về điểm đến. Không giới hạn độ dài. |
| ↳↳ custom_label_3 | string | Nhãn tùy chỉnh bổ sung về điểm đến. Không giới hạn độ dài. |
| ↳↳ custom_label_4 | string | Nhãn tùy chỉnh bổ sung về điểm đến. Không giới hạn độ dài. |

#### Tham số mảng đối tượng `products` cho catalog giải trí (entertainment)

> [!NOTE]
> Catalog giải trí hiện là tính năng thử nghiệm trong danh sách cho phép (allowlist-only) và chỉ mở theo thư mời. Vui lòng liên hệ đại diện TikTok nếu muốn tiếp cận.

| Field | Data Type | Description |
|---|---|---|
| products | object[] | **Bắt buộc**. Danh sách các sản phẩm (tựa phương tiện giải trí) bạn muốn tải lên. Tối đa: 5.000. |
| ↳ media_title_id | string | **Bắt buộc**. ID duy nhất cho mục tựa phương tiện (phim, chương trình TV, âm nhạc, trận đấu thể thao...). Giới hạn: 100 ký tự. Ví dụ: `TIKTOKLIVE001`. |
| ↳ title | string | **Bắt buộc**. Tên của tựa phương tiện. Chỉ sử dụng ký tự Unicode hợp lệ. Giới hạn: 150 ký tự. Ví dụ: `TikTok LIVE Series`. |
| ↳ description | string | Mô tả ngắn về tựa phương tiện. Giới hạn: 10.000 ký tự. |
| ↳ image_url | string | **Bắt buộc**. URL hình ảnh của tựa phương tiện. Kích thước tối thiểu 500x500 px, định dạng JPG hoặc PNG. Ví dụ: `https://www.tiktok.com/entertainment_image_001.jpg`. |
| ↳ video_url | string | URL video sử dụng trong quảng cáo. Khuyến nghị: 9:16 (dọc), ≥720x1280, ≥516kbps, có âm thanh và phụ đề. Ví dụ: `https://www.tiktok.com/tiktok_live_series`. |
| ↳ additional_image_urls | string[] | Danh sách URL hình ảnh bổ sung. Tối đa: 20 URL. Kích thước ≥ 500x500 px. Nếu có dấu phẩy, mã hóa thành `%2C`. Ví dụ: `["https://www.tiktok.com/entertainment_image_002.jpg","https://www.tiktok.com/entertainment_image_003.jpg"]`. |
| ↳ genres | string[] | Thể loại của tựa phương tiện. Tối đa: 2 thể loại. Xem danh sách giá trị cho `genres` bên dưới. Ví dụ: `TEEN`. |
| ↳ qid | string | QID (hoặc mã số Q), mã định danh duy nhất của tựa phương tiện trên Wikidata (bắt đầu bằng "Q" theo sau là chữ số). Giới hạn: 150 ký tự. Ví dụ: `Q48938223`. |
| ↳ price_info | object | Thông tin giá của tựa phương tiện. |
| ↳↳ price | float | Giá của tựa phương tiện. Ví dụ: `30`. |
| ↳↳ currency | string | Đơn vị tiền tệ. Theo quốc gia mục tiêu của catalog. Ví dụ: `USD`. |
| ↳ landing_page | object | Thông tin trang đích. |
| ↳↳ landing_page_url | string | URL trang đích nơi người dùng có thể xem và mua tựa phương tiện. Ví dụ: `https://www.tiktok.com/tiktok_entertainment`. |
| ↳↳ ios_url | string | Custom scheme URL cho iOS. Ví dụ: `iOS://electronic`. |
| ↳↳ ios_app_store_id | string | App Store ID cho iOS. Ví dụ: `1234`. |
| ↳↳ ios_app_name | string | Tên ứng dụng iOS. Ví dụ: `Electronic iOS`. |
| ↳↳ android_url | string | Custom scheme URL cho Android. Ví dụ: `android://electronic`. |
| ↳↳ android_package | string | Tên gói Android. Ví dụ: `com.electronic`. |
| ↳↳ android_app_name | string | Tên ứng dụng Android. Ví dụ: `Electronic Android`. |
| ↳ extra_info | object | Thông tin bổ sung. |
| ↳↳ custom_label_0 | string | Nhãn tùy chỉnh bổ sung. Không giới hạn độ dài. |
| ↳↳ custom_label_1 | string | Nhãn tùy chỉnh bổ sung. Không giới hạn độ dài. |
| ↳↳ custom_label_2 | string | Nhãn tùy chỉnh bổ sung. Không giới hạn độ dài. |
| ↳↳ custom_label_3 | string | Nhãn tùy chỉnh bổ sung. Không giới hạn độ dài. |
| ↳↳ custom_label_4 | string | Nhãn tùy chỉnh bổ sung. Không giới hạn độ dài. |

##### Danh sách giá trị cho `genres` (thể loại giải trí)

| Value | Description |
|---|---|
| `ACTION` | Phim hành động (action) |
| `ADULT_ANIMATION` | Hoạt hình người lớn (adult animation) |
| `ADVENTURE` | Phiêu lưu (adventure) |
| `ANIMATION` | Hoạt hình (animation) |
| `BIOGRAPHICAL` | Tiểu sử (biographical) |
| `BLACK_COMEDY` | Hài đen (black comedy) |
| `BUDDY` | Tình bạn/chiến hữu (buddy) |
| `COMEDY` | Hài kịch (comedy) |
| `COMIC` | Truyện tranh (comic) |
| `COOKING_SHOW` | Chương trình ẩm thực (cooking show) |
| `CRIME` | Tội phạm/hình sự (crime) |
| `DISASTER` | Thảm họa (disaster) |
| `DOCUMENTARY` | Phim tài liệu (documentary) |
| `DRAMA` | Tâm lý xã hội/chính kịch (drama) |
| `FAMILY` | Gia đình (family) |
| `FANTASY` | Giả tưởng/kỳ ảo (fantasy) |
| `GAME_SHOW` | Trò chơi truyền hình (game show) |
| `HISTORY` | Lịch sử (history) |
| `HORROR` | Kinh dị (horror) |
| `LGBT` | Đề tài LGBT |
| `MARTIAL_ARTS` | Võ thuật (martial arts) |
| `MILITARY` | Quân sự (military) |
| `MUSIC` | Âm nhạc (music) |
| `POLICE` | Cảnh sát (police) |
| `POLICE_PROCEDURAL` | Điều tra phá án (police procedural) |
| `POLITIC` | Chính trị (politic) |
| `REALITY_TV` | Truyền hình thực tế (reality TV) |
| `ROAD` | Phim đường trường (road) |
| `ROMANCE` | Tình cảm/lãng mạn (romance) |
| `SATIRE` | Châm biếm (satire) |
| `SCIENCE_FICTION` | Khoa học viễn tưởng (science fiction) |
| `SITCOM` | Hài kịch tình huống (sitcom) |
| `SOAP_OPERA` | Phim truyền hình dài tập (soap opera) |
| `SPORT` | Thể thao (sport) |
| `SPY` | Điệp viên/gián điệp (spy) |
| `STEAMPUNK` | Khoa học giả tưởng hơi nước (steampunk) |
| `SUPERHERO` | Siêu anh hùng (superhero) |
| `TALK_SHOW` | Chương trình trò chuyện (talk show) |
| `TEEN` | Tuổi thiếu niên (teen) |
| `THRILLER` | Giật gân/hồi hộp (thriller) |
| `TIME_TRAVEL` | Du hành thời gian (time travel) |
| `VAMPIRE` | Ma cà rồng (vampire) |
| `WAR` | Chiến tranh (war) |
| `WESTERN` | Miền Tây (western) |
| `ZOMBIE` | Xác sống (zombie) |

#### Tham số mảng đối tượng `products` cho catalog xe có sẵn (Auto-Inventory)

| Field | Data Type | Description |
|---|---|---|
| products | object[] | **Bắt buộc**. Danh sách các xe có sẵn bạn muốn tải lên. Tối đa: 5.000 xe. |
| ↳ vehicle_id | string | **Bắt buộc**. ID duy nhất cho xe. Giới hạn: 100 ký tự. Ví dụ: `TIKTOKMOTORSSEDAN001`. |
| ↳ title | string | **Bắt buộc**. Tên của xe. Chỉ dùng ký tự Unicode hợp lệ. Giới hạn: 500 ký tự. Ví dụ: `TikTok Motors Sedan`. |
| ↳ description | string | **Bắt buộc**. Mô tả ngắn về xe. Giới hạn: 5.000 ký tự. Ví dụ: `Experience the ultimate luxury and performance with the TikTok Motors Sedan.` |
| ↳ availability | string | Tình trạng có sẵn của xe. Giá trị enum: `AVAILABLE` (có sẵn để đặt hàng), `NOT_AVAILABLE` (không có sẵn). Ví dụ: `AVAILABLE`. |
| ↳ image_url | string | **Bắt buộc**. URL hình ảnh của xe (định dạng `http://` hoặc `https://`). Kích thước tối thiểu 500x500 px, định dạng JPG hoặc PNG. Ví dụ: `https://www.tiktok.com/auto_vehicle_image_001.jpg`. |
| ↳ additional_image_urls | string[] | Danh sách URL hình ảnh bổ sung của xe. Tối đa: 20 URL. Kích thước ≥ 500x500 px. Nếu có dấu phẩy, mã hóa thành `%2C`. Ví dụ: `["https://www.tiktok.com/auto_vehicle_image_002.jpg","https://www.tiktok.com/auto_vehicle_image_003.jpg"]`. |
| ↳ video_url | string | URL video sử dụng trong quảng cáo. Khuyến nghị: 9:16 (dọc), ≥720*1280, ≥516kbps, có âm thanh kèm phụ đề. Hỗ trợ định dạng .mp4, .mov, .avi, tối đa 100MB, thời lượng 15-60s. Ví dụ: `https://www.tiktok.com/auto_inventory.mp4`. |
| ↳ product_detail | object | Thông tin chi tiết bổ sung về xe. |
| ↳↳ condition | string | Tình trạng hiện tại của xe. Giá trị enum: `EXCELLENT` (xuất sắc), `GOOD` (tốt), `FAIR` (chấp nhận được), `POOR` (kém), `OTHER` (khác). Ví dụ: `GOOD`. |
| ↳↳ offer_type | string | Loại ưu đãi/chào bán. Giới hạn: 100 ký tự.<br>Giá trị khuyến nghị:<br>• `CASH`: Mua đứt trả thẳng bằng tiền mặt, người mua trả toàn bộ giá trước và sở hữu xe ngay lập tức. Xác định giá bằng `amount_price`.<br>• `LEASE`: Thuê xe dài hạn theo tháng trong một thời hạn nhất định. Chỉ định thời hạn, tiền hàng tháng và tiền đặt cọc bằng `term_length`, `offer_term_qualifier`, `amount_price`, `amount_qualifier`, `downpayment`, `downpayment_qualifier`.<br>• `FINANCE`: Vay tài chính mua xe trả góp theo kỳ hạn cố định kèm lãi suất. Chỉ định kỳ hạn, giá và lãi suất phần trăm năm (APR) bằng `term_length`, `offer_term_qualifier`, `amount_price`, `amount_percentage`, `amount_qualifier`. |
| ↳↳ term_length | string | Thời hạn áp dụng ưu đãi (kết hợp với `offer_term_qualifier`). Giới hạn: 100 ký tự. Ví dụ: `3`. |
| ↳↳ offer_term_qualifier | string | Đơn vị thời hạn ưu đãi. Giá trị khuyến nghị: `months`, `years`. Giới hạn: 100 ký tự. |
| ↳↳ amount_price | string | Số tiền ưu đãi (tiền trả góp/tháng cho cash/lease hoặc tổng giá vay cho finance). Tiền tệ theo catalog. Ví dụ: `100`. |
| ↳↳ amount_percentage | string | Tỷ lệ phần trăm lãi suất năm (APR) cho hình thức finance. Ví dụ: `1.1%`. |
| ↳↳ amount_qualifier | string | Định từ bổ nghĩa cho `amount_price` hoặc `amount_percentage`. Ví dụ: `month` (mỗi tháng), `APR` (lãi suất hàng năm). |
| ↳↳ downpayment | string | Tiền trả trước/đặt cọc tại thời điểm mua hoặc thuê xe. Ví dụ: `3000`. |
| ↳↳ downpayment_qualifier | string | Định từ bổ nghĩa cho khoản trả trước. Ví dụ: `due at signing` (thanh toán khi ký hợp đồng). Giới hạn: 100 ký tự. |
| ↳↳ offer_disclaimer | string | Toàn văn tuyên bố từ chối trách nhiệm ưu đãi hiển thị trong cửa sổ pop-up trong ứng dụng. Giới hạn: 5.000 ký tự. |
| ↳↳ offer_disclaimer_url | string | URL chuyển hướng người dùng đến thông tin chi tiết liên quan đến tuyên bố từ chối trách nhiệm ưu đãi. Ví dụ: `https://www.tiktok.com/tiktok_auto_inventory_disclaimer`. |
| ↳↳ emission_disclaimer | string | Toàn văn tuyên bố từ chối trách nhiệm về mức phát thải. Giới hạn: 5.000 ký tự. |
| ↳↳ emission_disclaimer_url | string | URL dẫn đến thông tin bổ sung về tuyên bố từ chối trách nhiệm phát thải. Ví dụ: `https://www.tiktok.com/tiktok_auto_inventory_emission_disclaimer`. |
| ↳↳ emission_overlay_disclaimer | string | Văn bản ngắn của tuyên bố phát thải hiển thị trên banner màn hình. Giới hạn: 500 ký tự. |
| ↳↳ emission_image_link | string | Đường dẫn hình ảnh hiển thị mức phát thải. Kích thước ≥ 450x450 px, tối đa 4MB. Ví dụ: `https://www.tiktok.com/tiktok_auto_inventory_emission_image.jpg`. |
| ↳ state_of_vehicle | string | **Bắt buộc**. Tình trạng xe.<br>Giá trị enum:<br>• `NEW`: xe mới.<br>• `USED`: xe đã qua sử dụng.<br>• `CPO`: xe đã qua sử dụng có chứng nhận chính hãng (certified pre-owned). Ví dụ: `USED`. |
| ↳ vehicle_type | string | Loại phương tiện.<br>Giá trị enum: `BOAT` (thuyền), `CAR_TRUCK` (xe hơi hoặc xe tải), `COMMERCIAL` (xe thương mại), `MOTORCYCLE` (xe máy), `POWERSPORT` (xe thể thao mạo hiểm), `RV_CAMPER` (nhà xe di động), `TRAILER` (xe rơ-moóc), `OTHER` (khác). |
| ↳ make | string | **Bắt buộc**. Hãng sản xuất xe (thương hiệu). Giới hạn: 100 ký tự. Ví dụ: `TikTok Motors`. |
| ↳ model | string | **Bắt buộc**. Dòng/mẫu xe. Giới hạn: 100 ký tự. Ví dụ: `X`. |
| ↳ trim | string | Phiên bản/gói cấu hình đặc trưng của mẫu xe (trim). Giới hạn: 50 ký tự. Ví dụ: `Long Range`. |
| ↳ year | integer | **Bắt buộc**. Năm ra mắt của xe, định dạng `YYYY`. Phạm vi: 1801-2999. Ví dụ: `2023`. |
| ↳ vin | string | Số nhận dạng xe (VIN) gồm 17 ký tự chữ và số theo chuẩn ISO 3779. Giới hạn: 17 ký tự. Ví dụ: `1TIKT0K5TAR123456`. |
| ↳ mileage | object | **Bắt buộc**. Quãng đường đã chạy của xe (số odo). |
| ↳↳ value | integer | **Bắt buộc**. Giá trị quãng đường đã đi. Phạm vi: ≥ 0. |
| ↳↳ unit | string | **Bắt buộc**. Đơn vị đo quãng đường. Giá trị enum: `MILE` (dặm), `KILOMETER` (km). |
| ↳ body_style | string | **Bắt buộc**. Kiểu dáng thân xe.<br>Giá trị enum: `CONVERTIBLE` (mui trần), `COUPE` (xe 2 cửa thể thao), `CROSSOVER`, `HATCHBACK`, `MINIVAN`, `SMALL_CAR`, `SEDAN`, `SUV`, `TRUCK` (bán tải), `VAN`, `WAGON`, `OTHER`. |
| ↳ exterior_color | string | **Bắt buộc**. Màu sơn ngoại thất xe. Giới hạn: 100 ký tự. |
| ↳ interior_color | string | Màu nội thất xe. Giới hạn: 100 ký tự. |
| ↳ transmission | string | Loại hộp số xe. Giá trị enum: `AUTOMATIC` (tự động), `MANUAL` (số sàn). |
| ↳ drivetrain | string | Hệ dẫn động của xe.<br>Giá trị enum: `4X2` (dẫn động 2 bánh trên xe 4 bánh), `4X4` (dẫn động 4 bánh bán thời gian), `AWD` (dẫn động 4 bánh toàn thời gian), `FWD` (dẫn động cầu trước), `RWD` (dẫn động cầu sau), `OTHER` (khác). |
| ↳ fuel_type | string | Loại nhiên liệu.<br>Giá trị enum: `DIESEL` (dầu diesel), `ELECTRIC` (thuần điện), `FLEX` (nhiên liệu linh hoạt ethanol/xăng), `GASOLINE` (xăng), `HYBRID` (hybrid), `OTHER`. |
| ↳ address | object | **Bắt buộc**. Thông tin địa chỉ đại lý bán xe (dealership). Quốc gia mặc định là quốc gia mục tiêu của catalog. |
| ↳↳ address | string | **Bắt buộc**. Địa chỉ đường phố của đại lý. Giới hạn: 150 ký tự. |
| ↳↳ city | string | **Bắt buộc**. Thành phố nơi đại lý tọa lạc. Giới hạn: 150 ký tự. |
| ↳↳ region | string | **Bắt buộc**. Bang/tỉnh nơi đại lý tọa lạc. Giới hạn: 150 ký tự. |
| ↳↳ postal_code | string | **Bắt buộc**. Mã bưu chính của đại lý. Giới hạn: 150 ký tự. |
| ↳ latitude | float | **Bắt buộc**. Vĩ độ của đại lý xe. Phạm vi: [-90, 90]. Ví dụ: `37.484100`. |
| ↳ longitude | float | **Bắt buộc**. Kinh độ của đại lý xe. Phạm vi: [-180, 180]. Ví dụ: `-122.148252`. |
| ↳ dealer | object | Thông tin chi tiết về đại lý xe. |
| ↳↳ dealer_id | string | ID duy nhất của đại lý xe. Giới hạn: 100 ký tự. |
| ↳↳ dealer_name | string | Tên đại lý xe. Giới hạn: 100 ký tự. |
| ↳↳ dealer_phone | string | Số điện thoại đại lý (bao gồm mã quốc gia). Giới hạn: 15 ký tự. |
| ↳↳ stock_number | string | Mã số kho/lô gán cho xe khi xe thực tế về tới bãi đại lý. Giới hạn: 100 ký tự. Ví dụ: `T12345`. |
| ↳ date_first_on_lot | string | Ngày đầu tiên xe có mặt thực tế tại bãi của đại lý, định dạng `YYYY-MM-DD`. Ví dụ: `2023-12-01`. |
| ↳ days_on_lot | integer | Số ngày xe nằm tại bãi đại lý (tính từ `date_first_on_lot` đến hiện tại). Không tự động tăng hàng ngày nên khuyến nghị cập nhật mỗi ngày. Mặc định: 0. Ví dụ: `13`. |
| ↳ price_info | object | **Bắt buộc**. Thông tin giá xe. |
| ↳↳ price | float | **Bắt buộc**. Giá bán của xe. Ví dụ: `9.9`. |
| ↳↳ currency | string | Đơn vị tiền tệ. Theo catalog. Ví dụ: `USD`. |
| ↳↳ sale_price | float | Giá khuyến mãi giảm giá của xe. Phải nhỏ hơn `price`. Ví dụ: `9.9`. |
| ↳↳ sale_price_effective_date | string | Thời gian áp dụng giá khuyến mãi, định dạng `YYYY-MM-DDT23:59+00:00/YYYY-MM-DDT23:59+00:00`. Ví dụ: `2023-12-11T23:59+00:00/2023-12-15T23:59+00:00`. |
| ↳ landing_page | object | **Bắt buộc**. Thông tin trang đích. |
| ↳↳ landing_page_url | string | **Bắt buộc**. URL trang đích xem và mua xe. Ví dụ: `https://www.tiktok.com/tiktok_auto_inventory`. |
| ↳↳ ios_url | string | Custom scheme URL cho iOS. Ví dụ: `iOS://electronic`. |
| ↳↳ android_url | string | Custom scheme URL cho Android. Ví dụ: `android://electronic`. |
| ↳ extra_info | object | Thông tin bổ sung. |
| ↳↳ custom_label_0 | string | Nhãn tùy chỉnh bổ sung về xe. |
| ↳↳ custom_label_1 | string | Nhãn tùy chỉnh bổ sung về xe. |
| ↳↳ custom_label_2 | string | Nhãn tùy chỉnh bổ sung về xe. |
| ↳↳ custom_label_3 | string | Nhãn tùy chỉnh bổ sung về xe. |
| ↳↳ custom_label_4 | string | Nhãn tùy chỉnh bổ sung về xe. |

#### Tham số mảng đối tượng `products` cho catalog mẫu xe (Auto-Model)

| Field | Data Type | Description |
|---|---|---|
| products | object[] | **Bắt buộc**. Danh sách các mẫu xe bạn muốn tải lên. Tối đa: 5.000 xe. |
| ↳ vehicle_id | string | **Bắt buộc**. ID duy nhất cho mẫu xe. Giới hạn: 100 ký tự. Ví dụ: `TIKTOKMOTORSX001`. |
| ↳ title | string | **Bắt buộc**. Tên mẫu xe bao gồm hãng, dòng xe, phiên bản và năm sản xuất. Giới hạn: 128 ký tự (khuyến nghị dưới 40 ký tự). Ví dụ: `2025 TikTok Motors X Long Range`. |
| ↳ image_url | string | **Bắt buộc**. URL hình ảnh của mẫu xe (`http://` hoặc `https://`). Kích thước tối thiểu 450x450 px, định dạng JPG, PNG hoặc JPEG. Dung lượng dưới 4MB. Ví dụ: `https://www.tiktok.com/auto_model_image_001.jpg`. |
| ↳ video_url | string | URL video sử dụng trong quảng cáo. Khuyến nghị: 9:16 (dọc), ≥ 720*1280, ≥ 516kbps, có âm thanh và phụ đề. Tối đa 100MB, 15-60 giây. Ví dụ: `https://www.tiktok.com/auto_model.mp4`. |
| ↳ make | string | **Bắt buộc**. Hãng sản xuất xe. Giới hạn: 100 ký tự. Ví dụ: `TikTok Motors`. |
| ↳ model | string | **Bắt buộc**. Dòng/mẫu xe. Giới hạn: 100 ký tự. Ví dụ: `X`. |
| ↳ trim | string | Phiên bản cấu hình xe. Giới hạn: 50 ký tự. Ví dụ: `Long Range`. |
| ↳ year | integer | **Bắt buộc**. Năm ra mắt xe, định dạng `YYYY`. Ví dụ: `2025`. |
| ↳ exterior_color | string | **Bắt buộc**. Màu sơn ngoại thất xe. Giới hạn: 100 ký tự. Ví dụ: `Black`. |
| ↳ product_detail | object | Thông tin chi tiết bổ sung về mẫu xe. |
| ↳↳ offer_type | string | Loại ưu đãi: `CASH`, `LEASE`, `FINANCE`. Xem giải thích chi tiết trong phần Auto-Inventory. |
| ↳↳ term_length | string | Thời hạn áp dụng ưu đãi. Giới hạn: 100 ký tự. Ví dụ: `3`. |
| ↳↳ offer_term_qualifier | string | Đơn vị thời hạn ưu đãi: `months`, `years`. |
| ↳↳ amount_price | string | Số tiền ưu đãi. Ví dụ: `100`. Tiền tệ theo catalog. |
| ↳↳ amount_percentage | string | Tỷ lệ APR cho hình thức finance. Ví dụ: `1.1%`. |
| ↳↳ amount_qualifier | string | Định từ: `month` hoặc `APR`. |
| ↳↳ downpayment | string | Tiền trả trước. Ví dụ: `3000`. |
| ↳↳ downpayment_qualifier | string | Định từ tiền trả trước: `due at signing`. |
| ↳↳ offer_disclaimer | string | Toàn văn tuyên bố miễn trừ ưu đãi. Giới hạn: 5.000 ký tự. |
| ↳↳ offer_disclaimer_url | string | URL chi tiết tuyên bố miễn trừ ưu đãi. Ví dụ: `https://www.tiktok.com/tiktok_auto_model_disclaimer`. |
| ↳↳ emission_disclaimer | string | Toàn văn tuyên bố miễn trừ phát thải. Giới hạn: 5.000 ký tự. |
| ↳↳ emission_disclaimer_url | string | URL tuyên bố miễn trừ phát thải. |
| ↳↳ emission_overlay_disclaimer | string | Văn bản ngắn tuyên bố phát thải trên banner. Giới hạn: 500 ký tự. |
| ↳↳ emission_image_link | string | Đường dẫn hình ảnh mức phát thải. Kích thước ≥ 500x500 px, tối đa 4MB. |
| ↳ landing_page | object | **Bắt buộc**. Thông tin trang đích. |
| ↳↳ landing_page_url | string | **Bắt buộc**. URL trang đích xem danh sách xe. Ví dụ: `https://www.tiktok.com/tiktok_auto_model`. |

#### Tham số mảng đối tượng `products` cho catalog phim ngắn nhiều tập (mini series)

> [!NOTE]
> Catalog phim ngắn nhiều tập (mini series) hiện là tính năng danh sách cho phép (allowlist-only) trong giai đoạn thử nghiệm và chỉ mở theo thư mời. Vui lòng liên hệ đại diện TikTok nếu muốn truy cập.

| Field | Data Type | Description |
|---|---|---|
| products | object[] | **Bắt buộc**. Danh sách các bộ phim ngắn nhiều tập bạn muốn tải lên. Tối đa: 5.000. |
| ↳ series_id | string | **Bắt buộc**. ID duy nhất tự định nghĩa cho bộ phim ngắn. Giới hạn: 100 ký tự. |
| ↳ series_name | string | **Bắt buộc**. Tên của bộ phim ngắn. Giới hạn: 100 ký tự. |
| ↳ target_config | object | Chi tiết nhắm mục tiêu cho bộ phim ngắn.<br>**Lưu ý**:<br>• Để tải lên các bộ phim nhắm mục tiêu nhiều khu vực, gọi [/catalog/product/upload/](28-catalog-products-p1.md#doc-1740497429681153) nhiều lần với cùng `series_id` và các cài đặt `target_config` khác nhau. Sau khi tải lên, truy cập cài đặt hợp nhất qua `target_config` và `additional_product_list` trong [/catalog/product/get/](28-catalog-products-p2.md#doc-1740564136678402).<br>• Ví dụ: các lần tải lên riêng biệt với `{"region_code": "US"}` và `{"region_code": "VN"}` sẽ tạo thành `list.target_config.region_code` là `US` và `list.additional_product_list.region_code` là `VN` trong `/catalog/product/get/`. |
| ↳↳ region_code | string | Mã của khu vực nhắm mục tiêu cho bộ phim ngắn (tập con của các khu vực mục tiêu của catalog). Lấy danh sách khu vực qua [/catalog/get/](25-catalog-management.md#doc-1740315452868610). Ví dụ: `US`. |
| ↳ image_url | string | **Bắt buộc**. URL ảnh áp phích (poster) của bộ phim. Kích thước tối thiểu 500x500 px, định dạng JPG hoặc PNG. Ví dụ: `https://www.tiktok.com/short_drama_series_image_001.jpg`. |
| ↳ video_url | string | URL video sử dụng trong quảng cáo. Khuyến nghị: 9:16 (dọc), ≥ 720*1280, ≥ 516 kbps, có âm thanh kèm phụ đề. Hỗ trợ .mp4, .mov, .avi, tối đa 100MB, 15-60s. Ví dụ: `https://www.tiktok.com/short_drama_series.mp4`. |
| ↳ recharge | object[] | **Bắt buộc**. Thông tin nạp tiền/thanh toán để xem bộ phim ngắn. |
| ↳↳ type | string | **Bắt buộc**. Loại nạp tiền/thanh toán.<br>Giá trị enum:<br>• `BY_TIERS`: Nạp tiền theo các gói/bậc (tiers).<br>• `SUBSCRIPTION`: Trả phí theo gói thuê bao định kỳ.<br>• `BY_EPISODES`: Mua theo từng tập phim. |
| ↳↳ purchase_unit | string[] | **Bắt buộc**. Đơn vị thanh toán.<br>• Khi `recharge_type` là `BY_TIERS`: `TIER_1`, `TIER_2`, `TIER_3`, `TIER_4`, `TIER_5`.<br>• Khi `recharge_type` là `SUBSCRIPTION`: `WEEKLY` (hàng tuần), `MONTHLY` (hàng tháng), `QUARTERLY` (hàng quý), `YEARLY` (hàng năm).<br>• Khi `recharge_type` là `BY_EPISODES`: Một hoặc nhiều chuỗi số thể hiện số tập (không vượt quá tổng số tập). |
| ↳↳ cost | float[] | **Bắt buộc**. Mức giá tương ứng cho các bậc, chu kỳ thuê bao hoặc số tập phim. |
| ↳ product_detail | object | **Bắt buộc**. Thông tin chi tiết bổ sung về bộ phim ngắn. |
| ↳↳ company_type | string | Loại hình công ty của bộ phim. Giá trị enum: `COPYRIGHT_HOLDER` (chủ sở hữu bản quyền), `DISTRIBUTOR` (nhà phân phối). |
| ↳↳ copyright_holder_name | string | Bắt buộc khi chỉ định `company_type`. Tên công ty sở hữu bản quyền. Giới hạn: 100 ký tự. |
| ↳↳ app_id | string | Bắt buộc phải chỉ định ít nhất một trong hai: `app_id` hoặc `minis_id` (hoặc cả hai). App ID của ứng dụng cần quảng bá. Lấy danh sách App ID qua [/app/list/](43-events-1-0-p1.md#doc-1740859313270786). |
| ↳↳ minis_id | string | Bắt buộc phải chỉ định ít nhất một trong hai: `app_id` hoặc `minis_id`. Mã định danh của chương trình nhỏ (mini program ID) trên TikTok Open Platform. |
| ↳↳ total_episodes | number | **Bắt buộc**. Tổng số tập của bộ phim ngắn. Phạm vi: 1-9.999. |
| ↳↳ initial_paid_episodes | number | **Bắt buộc**. Số thứ tự tập bắt đầu yêu cầu trả phí để tiếp tục xem (ví dụ: bắt đầu thu phí từ tập 11 thì truyền 11). Phạm vi: 1-9.999. Phải nhỏ hơn `total_episodes`. |
| ↳↳ per_episode_duration | number | Thời lượng trung bình của mỗi tập (phút). Phạm vi: 0-15. |
| ↳↳ spoken_language | string | **Bắt buộc**. Ngôn ngữ thoại của các diễn viên trong bản gốc phim.<br>Giá trị enum: `ar`, `de`, `cs`, `en`, `es`, `fr`, `he`, `hi`, `id`, `it`, `ja`, `ko`, `ms`, `pl`, `pt`, `ro`, `ru`, `ta`, `th`, `tr`, `vi` (tiếng Việt), `zh`, `zh-hant`. |
| ↳↳ subtitle_language | string | **Bắt buộc**. Ngôn ngữ phụ đề trong phim ngắn.<br>Giá trị enum: `ar`, `de`, `cs`, `en`, `es`, `fr`, `he`, `hi`, `id`, `it`, `ja`, `ko`, `ms`, `pl`, `pt`, `ro`, `ru`, `ta`, `th`, `tr`, `vi` (tiếng Việt), `zh`, `zh-hant`. |
| ↳↳ production_type | string | **Bắt buộc**. Loại hình sản xuất: `LOCAL` (phim sản xuất tại địa phương với diễn viên và ngôn ngữ bản địa), `TRANSLATION` (phim chuyển ngữ xuất khẩu với phụ đề, lồng tiếng sang ngôn ngữ khác). |
| ↳↳ target_audience | string | **Bắt buộc**. Đối tượng khán giả mục tiêu.<br>Giá trị enum:<br>• `MALE`: Khán giả nam giới (thường theo góc nhìn nam chính, đề tài quyền lực, làm giàu, tăng cường thực lực).<br>• `FEMALE`: Khán giả nữ giới (thường theo góc nhìn nữ chính, yếu tố lãng mạn, tình cảm).<br>• `NEUTRAL`: Trung tính, không hướng tới giới tính cụ thể. |
| ↳↳ characters | string[] | **Bắt buộc**. Danh sách các hình mẫu nhân vật trong phim. Tối đa: 3. Xem bảng giá trị cho `characters` bên dưới. |
| ↳↳ genres | string[] | **Bắt buộc**. Thể loại của bộ phim ngắn theo cốt truyện chính. Tối đa: 3. Xem bảng giá trị cho mini series `genres` bên dưới. |
| ↳↳ historical_context | string[] | Bối cảnh lịch sử hoặc không gian thời gian của phim. Tối đa: 3. Xem bảng giá trị cho `historical_context` bên dưới. |
| ↳↳ actors | string[] | Tên các diễn viên tham gia. Tối đa: 20 tên. Giới hạn mỗi tên: 100 ký tự. |

##### Danh sách giá trị cho `characters` (hình mẫu nhân vật phim ngắn)

| Value | Type | Description |
|---|---|---|
| `ALPHA_MALE` | alpha male | Nam chính quyền lực, giàu có đứng đầu giới kinh doanh, vừa thống trị vừa quyến rũ. |
| `ATHLETE` | athlete | Vận động viên thể thao, thể hiện kỷ luật và sức mạnh thể chất. |
| `BABIES` | babies | Yếu tố liên quan đến trẻ sơ sinh/trẻ nhỏ, mang lại nét ấm áp hoặc hài hước. |
| `BADBOY` | badboy | Nhân vật nam nổi loạn, vẻ ngoài lạnh lùng nhưng nội tâm ấm áp. |
| `CHEF` | chef | Đầu bếp, nghệ thuật ẩm thực hoặc bối cảnh nhà hàng. |
| `DOCTOR` | doctor | Bác sĩ, chuyên gia y tế trong các tình huống kịch tính hoặc giàu cảm xúc. |
| `DRAGON_KING` | dragon king | Long Vương, nhân vật kỳ ảo phương Đông (Long thần hoặc Chiến thần). |
| `ELITE_PROFESSION` | elite profession | Nghề nghiệp tinh hoa (cảnh sát, luật sư, phi công, quân nhân...). |
| `EMPEROR` | emperor | Hoàng đế, người cai trị tối cao với quyền lực chính trị tuyệt đối. |
| `EXTRAORDINARY_TALENT` | extraordinary talent | Nhân vật có siêu năng lực vượt giới hạn con người (thần giao cách cảm, dịch chuyển đồ vật...). |
| `GANG_MAFIA` | gang/mafia | Nhân vật trong giới tội phạm có tổ chức, tàn nhẫn và nghĩa khí phức tạp. |
| `HEIRESS` | heiress | Thiên kim tiểu thư, người thừa kế gia tộc giàu có danh giá. |
| `HEROINE` | heroine | Nữ chính độc lập, bản lĩnh, kiên cường và quyết đoán. |
| `HIDDEN_IDENTITY` | hidden identity | Giấu thân phận thật sau vỏ bọc bình thường, tạo nút thắt bí ẩn. |
| `HOUSE_WIFE` | house wife | Người nội trợ tập trung chăm lo gia đình. |
| `IDOL` | idol | Thần tượng, người nổi tiếng trong giới giải trí biểu diễn. |
| `KUNG_FU_MASTER` | kung fu master | Cao thủ võ thuật truyền thống, đề cao kỷ luật và danh dự. |
| `LIVE_IN_SON_IN_LAW` | live-in son in law | Chàng rể ở rể (ở nhà vợ), thường chịu định kiến rồi trỗi dậy khẳng định bản thân. |
| `MODERN_MOMS` | modern moms | Người mẹ hiện đại với thiên chức nuôi dạy con cái. |
| `NOBODY` | nobody | Người bình thường không quyền thế, tạo sự gần gũi và tương phản. |
| `PRINCESS_CONSORT` | princess consort | Vương phi/thái tử phi trong cung đình quý tộc. |
| `PSYCHO_SWEETHEART` | psycho sweetheart | Nhân vật ngoài mặt ngọt ngào nhưng có xu hướng chiếm hữu cực đoan. |
| `QUEEN` | queen | Nữ hoàng/hoàng hậu quyền quý và bản lĩnh chính trị. |
| `SPIRIT_CULTIVATOR` | spirit cultivator | Người tu chân, tu tiên để đạt cảnh giới trường sinh hoặc sức mạnh kỳ ảo. |
| `SUBSTITUTE` | substitute | Thế thân, người mạo danh hoặc thay thế người khác. |
| `TEENS` | teens | Thanh thiếu niên với cuộc sống học đường, tình bạn và rung động đầu đời. |
| `VAMPIRE` | vampire | Ma cà rồng bất tử với sức mạnh siêu nhiên. |
| `WARLORD` | warlord | Chiến thần, thủ lĩnh quân sự lẫy lừng trên chiến trường. |
| `WEREWOLF` | werewolf | Người sói hóa thú dưới trăng tròn, cấu trúc bầy đàn với thủ lĩnh Alpha. |
| `OTHERS` | others | Các hình mẫu nhân vật khác tùy biến theo câu chuyện. |

##### Danh sách giá trị cho mini series `genres` (thể loại phim ngắn)

| Value | Type | Description |
|---|---|---|
| `ACTION` | action | Hành động kịch tính, nhịp độ nhanh. |
| `AFFAIR` | affair | Ngoại tình, mối quan hệ ngoài hôn nhân đầy mâu thuẫn. |
| `AGE_GAP_ROMANCE` | age gap romance | Tình yêu chênh lệch tuổi tác. |
| `BITTER_LOVE` | bitter love | Tình yêu cay đắng, đau đớn và hiểu lầm. |
| `BUILD_FROM_SCRATCH` | build from scratch | Khởi nghiệp từ hai bàn tay trắng làm giàu. |
| `CHILDHOOD_SWEETHEARTS` | childhood sweethearts | Thanh mai trúc mã, gắn bó từ thơ ấu. |
| `CHINESE_FANTASY` | Chinese fantasy | Tiên hiệp/huyền huyễn Trung Hoa, thần tiên ma quái. |
| `COME_UPPANCE_RETRIBUTION` | comeuppance retribution | Nhân vật phản diện bị trừng phạt đích đáng, báo ứng thích đáng. |
| `COMEBACK` | comeback | Sự trở lại ngoạn mục của kẻ mạnh để đòi lại công lý. |
| `COMEDY` | comedy | Hài hước, nhẹ nhàng vui nhộn. |
| `CONSPIRACY` | conspiracy | Âm mưu toan tính, cạm bẫy đen tối. |
| `CONTRACT_LOVE` | contract love | Hợp đồng tình ái/hôn nhân hợp đồng rồi nảy sinh tình cảm thật. |
| `COUGAR_CUB_DYNAMIC` | cougar-cub dynamic | Tình cảm nữ lớn tuổi hơn nam (chị em). |
| `CRIME` | crime | Tội phạm, điều tra phá án và pháp luật. |
| `DISASTER` | disaster | Thảm họa tự nhiên hoặc nhân tạo. |
| `DISGUISE` | disguise | Cải trang che giấu danh tính để thực thi kế hoạch. |
| `DRAGON_TIGER_PACT` | dragon-tiger pact | Long hổ hội ngộ, các bên hùng mạnh liên thủ vì mục tiêu chung. |
| `DRAMA` | drama | Tâm lý tình cảm xã hội sâu sắc, xung đột nội tâm. |
| `ENEMIES_TO_LOVERS` | enemies-to-lovers | Oan gia ngõ hẹp từ ghét chuyển thành yêu. |
| `FAMILY_BOUNDS` | family bonds | Tình cảm gia đình gắn kết và mâu thuẫn ruột thịt. |
| `FAMILY_ETHICS` | family ethics | Đạo đức gia phong, mâu thuẫn luân thường đạo lý. |
| `FANTASY_ROMANCE` | fantasy romance | Lãng mạn kỳ ảo trong thế giới phép thuật. |
| `FEMALE_GROWTH` | female growth | Nữ chủ tự cường, hành trình trưởng thành tự khẳng định mình. |
| `FIGHT_BULLYING` | fight bullying | Vươn lên chống lại áp bức, bắt nạt. |
| `FLASH_MARRIED` | flash married | Cưới trước yêu sau, kết hôn chớp nhoáng. |
| `GANG_FIGHTS` | gang fights | Băng đảng tranh đấu, thanh trừng giang hồ. |
| `HARD_WIN_LOVE` | hard-win love | Theo đuổi tình yêu gian nan, chuộc lại lỗi lầm để giành lại trái tim. |
| `HORRORS_AND_THRILLERS` | horrors and thrillers | Kinh dị giật gân, rùng rợn. |
| `INDULGENT_LOVE` | indulgent love | Tình yêu ngọt ngào, cưng chiều hết mực. |
| `INVINCIBLE` | invincible | Nhân vật chính vô địch thiên hạ, sức mạnh vượt trội. |
| `LIFE_TRANSFORMATION` | life transformation | Nghịch chuyển số phận, từ đáy xã hội bước lên đỉnh cao danh vọng. |
| `LOVE_AFTER_MARRIAGE` | love after marriage | Tình yêu sau hôn nhân, cùng vượt sóng gió để hiểu nhau. |
| `LOVE_AT_FIRST_SIGHT` | love at first sight | Tình yêu sét đánh từ cái nhìn đầu tiên. |
| `LOVE_IN_WEALTHY_FAMILIES` | love in wealthy families | Hào môn thế gia, dâu hào môn, liên minh gia tộc giàu có. |
| `LOVE_ON_CAMPUS` | love on campus | Tình yêu vườn trường học đường trong sáng. |
| `LOVE_TRIANGLE` | love triangle | Tình tay ba phức tạp, rối rắm. |
| `ONE_NIGHT_STAND` | one night stand | Tình một đêm ngẫu nhiên mở ra chuỗi duyên nợ. |
| `PALACE_FIGHT` | palace fight | Cung đấu cung đình thâm hiểm tranh giành sủng ái vị thế. |
| `POWER_CALCULUS` | power calculus | Đấu trí quyền lực, mưu lược chính trường. |
| `PREGNANCY_ESCAPE` | pregnancy escape | Mang thai rồi bỏ trốn (đới cầu bào), chia cắt rồi tái ngộ. |
| `RECONCILIATION_AFTER_BREAKUP` | reconciliation after breakup | Gương vỡ lại lành sau chia tay. |
| `REDEMPTION` | redemption | Chuộc lỗi và tìm lại sự cứu rỗi bản thân. |
| `RETURN_FOR_REVENGE` | return for revenge | Trọng sinh/trở về báo thù rửa hận kẻ phản bội. |
| `REVERSE_HAREM` | reverse harem | Một nữ chính được nhiều nam thần vây quanh tranh giành tình cảm. |
| `SECRET_CRUSH_COME_TRUE` | secret crush come true | Yêu thầm thành hiện thực sau bao năm ấp ủ. |
| `SPY` | spy | Điệp viên ngầm, tình báo cài cắm. |
| `SUSPENSE` | suspense | Bí ẩn ly kỳ, bất ngờ đến phút chót. |
| `SWAPPED_HEIRESSES` | swapped heiresses | Hoán đổi thân phận thiên kim tiểu thư thật giả. |
| `TABOO_RELATIONSHIP` | taboo relationship | Mối tình vượt giới hạn cấm kỵ xã hội. |
| `TEAR_JERKERS` | tear-jerkers | Phim lấy nước mắt, bi thương cảm động. |
| `WORKPLACE_ROMANCE` | workplace romance | Tình yêu công sở, tình công sở sếp và nhân viên. |

##### Danh sách giá trị cho `historical_context` (bối cảnh lịch sử)

| Value | Type | Description |
|---|---|---|
| `ANCIENT_SETTING` | ancient setting | Bối cảnh thời cổ đại phương Đông hoặc phương Tây. |
| `BOOK_TRANSMIGRATION` | book transmigration | Xuyên không vào thế giới trong sách tiểu thuyết. |
| `FICTIONAL` | fictional | Bối cảnh không gian thời gian hư cấu, tưởng tượng. |
| `MODERN` | modern | Bối cảnh thế giới hiện đại ngày nay. |
| `PERIOD_IN_60_80S` | period in 60-80s | Bối cảnh thời kỳ thập niên 1960 - 1980. |
| `REPUBLIC_OF_CHINA` | Republic of China | Bối cảnh thời kỳ Dân quốc. |
| `SECOND_CHANCE` | second chance | Trọng sinh, làm lại cuộc đời, tái sinh sau cái chết dùng ký ức kiếp trước đổi mệnh. |
| `TIME_SPACE_TRAVEL` | time/space travel | Xuyên không qua không gian và thời gian. |

#### Tham số mảng đối tượng `products` cho catalog chung (generic)

| Field | Data Type | Description |
|---|---|---|
| products | object[] | **Bắt buộc**. Danh sách các sản phẩm/dịch vụ bạn muốn tải lên. Tối đa: 5.000. |
| ↳ item_id | string | **Bắt buộc**. ID duy nhất tự định nghĩa cho sản phẩm hoặc dịch vụ. Giới hạn: 100 ký tự. Sử dụng ký tự Unicode hợp lệ. |
| ↳ title | string | **Bắt buộc**. Tên sản phẩm hoặc dịch vụ. Giới hạn: 500 ký tự. |
| ↳ description | string | Mô tả chi tiết về sản phẩm hoặc dịch vụ. Giới hạn: 5.000 ký tự. |
| ↳ availability | string | Tình trạng tồn kho hiện tại.<br>Giá trị enum: `IN_STOCK` (còn hàng), `AVAILABLE` (có sẵn), `PREORDER` (đặt trước), `OUT_OF_STOCK` (hết hàng), `DISCONTINUED` (ngừng kinh doanh), `UNAVAILABLE` (không khả dụng). |
| ↳ image_url | string | **Bắt buộc**. URL dẫn đến hình ảnh chính của sản phẩm/dịch vụ (bắt đầu bằng `http://` hoặc `https://`, liên kết trực tiếp tới file ảnh). Kích thước từ 500×500 đến 1290×2790 px. Tỷ lệ khuyến nghị 1:1. |
| ↳ video_url | string | Đường dẫn video sản phẩm/dịch vụ. Khuyến nghị: 9:16 (dọc), ≥720*1280, ≥516 kbps, có âm thanh và phụ đề. |
| ↳ additional_image_urls | string[] | Danh sách URL hình ảnh bổ sung. Tối đa 20 liên kết, định dạng JPG hoặc PNG, kích thước 500x500 đến 1290x2790 px. Ví dụ: `["https://www.example.com/products/images/headphones-side.jpg", "https://www.example.com/products/images/headphones-box.jpg"]`. |
| ↳ address | object | Thông tin địa chỉ cung cấp sản phẩm/dịch vụ. |
| ↳↳ street | string | Địa chỉ đường phố nơi đặt sản phẩm/dịch vụ. Giới hạn: 150 ký tự. Ví dụ: `1143 coleman Avenue`. |
| ↳↳ city | string | Thành phố nơi đặt sản phẩm/dịch vụ. Giới hạn: 150 ký tự. Ví dụ: `San Jose`. |
| ↳↳ region | string | Bang/tỉnh/khu vực hành chính. Giới hạn: 150 ký tự. Ví dụ: `California`. |
| ↳↳ postal_code | string | Mã bưu chính hoặc mã zip. Giới hạn: 150 ký tự. Ví dụ: `95050`. |
| ↳ longitude | double | Kinh độ của địa điểm. Phạm vi: [-180, 180]. Ví dụ: `100.5`. |
| ↳ latitude | double | Vĩ độ của địa điểm. Phạm vi: [-90, 90]. Ví dụ: `-25.5`. |
| ↳ product_detail | object | Thông tin chi tiết khác của sản phẩm/dịch vụ. |
| ↳↳ rating | double | Điểm đánh giá của người dùng. Phạm vi: 0.0 - 5.0. |
| ↳↳ availability_type | string | Phương thức định nghĩa vùng địa lý nơi sản phẩm có thể bán hoặc dịch vụ được cung cấp.<br>Giá trị enum:<br>• `REGION`: Khu vực/địa điểm hành chính. Thiết lập qua `availability_region`.<br>• `DMA`: Vùng thị trường chỉ định (DMA). Thiết lập qua `availability_dma`.<br>• `RADIUS`: Bán kính hình tròn. Thiết lập qua `availability_circle_radius` và `availability_circle_radius_unit`.<br>• `POSTAL_CODE`: Mã bưu chính. Thiết lập qua `availability_postal_codes`.<br>**Lưu ý**: Tránh dùng endpoint này để đặt các trường khả dụng về null; hãy sử dụng [/catalog/product/file/](28-catalog-products-p1.md#doc-1740496787164161) thay thế. |
| ↳↳ availability_region | string[][] | Bắt buộc khi `availability_type` là `REGION`. Mảng các mảng chuỗi biểu diễn tối đa 998 địa điểm (mỗi mảng con gồm tối đa 2 chuỗi biểu diễn cấp hành chính L1 và L2 theo đúng thứ tự). Đối với Hoa Kỳ, dùng định dạng `["State", "City"]`. Ví dụ: `[["Arizona","Peoria"],["Alabama","Birmingham"]]`. |
| ↳↳ availability_dma | string[] | Bắt buộc khi `availability_type` là `DMA`. Danh sách số DMA 3 chữ số, tối đa 500 mã. Chỉ áp dụng cho catalog nhắm mục tiêu Hoa Kỳ (`US`). Ví dụ: `["501","803"]`. |
| ↳↳ availability_circle_radius | string | Bắt buộc khi `availability_type` là `RADIUS`. Bán kính khả dụng hình tròn. Khi đơn vị là km: > 0 và ≤ 40; khi đơn vị là dặm (mile): > 0 và ≤ 25. Chỉ áp dụng cho catalog nhắm tới Indonesia, Malaysia, Thái Lan hoặc Việt Nam (`TH`, `ID`, `MY`, `VN`). Ví dụ: `20`. |
| ↳↳ availability_circle_radius_unit | string | Bắt buộc khi `availability_type` là `RADIUS`. Đơn vị bán kính: `KM` (kilômét) hoặc `MI` (dặm). Chỉ áp dụng cho `TH`, `ID`, `MY`, `VN`. |
| ↳↳ availability_postal_codes | string[] | Bắt buộc khi `availability_type` là `POSTAL_CODE`. Danh sách mã bưu chính, tối đa 500 mã (mỗi mã tối đa 20 ký tự). Chỉ áp dụng cho catalog nhắm tới `US` hoặc `CA`. Ví dụ: `["10001", "90001"]`. |
| ↳↳ custom_number_0 | double | Thuộc tính số tùy chỉnh cho quản lý sản phẩm. |
| ↳↳ custom_number_1 | double | Thuộc tính số tùy chỉnh cho quản lý sản phẩm. |
| ↳↳ custom_number_2 | double | Thuộc tính số tùy chỉnh cho quản lý sản phẩm. |
| ↳↳ custom_number_3 | double | Thuộc tính số tùy chỉnh cho quản lý sản phẩm. |
| ↳↳ custom_number_4 | double | Thuộc tính số tùy chỉnh cho quản lý sản phẩm. |
| ↳ price_info | object | Thông tin giá. |
| ↳↳ price | double | Giá của một đơn vị sản phẩm hoặc dịch vụ. Đơn vị tiền tệ mặc định theo quốc gia catalog. Ví dụ: `9.99`. |
| ↳↳ currency | string | Đơn vị tiền tệ. Ví dụ: `USD`. |
| ↳↳ sale_price | double | Giá khuyến mãi giảm giá. Phải thấp hơn `price` để hiển thị cả 2 giá trên quảng cáo. Ví dụ: `4.99`. |
| ↳ landing_page | object | Thông tin trang đích. |
| ↳↳ landing_page_url | string | Liên kết trang đích trực tiếp của sản phẩm/dịch vụ (bắt đầu bằng `http://` hoặc `https://`). |
| ↳↳ ios_url | string | URL ứng dụng iOS. Ví dụ: `iOS://electronic`. |
| ↳↳ ios_app_store_id | string | App Store ID của ứng dụng iOS. |
| ↳↳ ios_app_name | string | Tên ứng dụng iOS. |
| ↳↳ android_url | string | URL ứng dụng Android. Ví dụ: `android://electronic`. |
| ↳↳ android_package | string | Tên gói Android package name. |
| ↳↳ android_app_name | string | Tên ứng dụng Android. |
| ↳ extra_info | object | Thông tin nhãn tùy chỉnh bổ sung. |
| ↳↳ custom_label_0 | string | Nhãn tùy chỉnh bổ sung. Giới hạn: 500 ký tự. |
| ↳↳ custom_label_1 | string | Nhãn tùy chỉnh bổ sung. Giới hạn: 500 ký tự. |
| ↳↳ custom_label_2 | string | Nhãn tùy chỉnh bổ sung. Giới hạn: 500 ký tự. |
| ↳↳ custom_label_3 | string | Nhãn tùy chỉnh bổ sung. Giới hạn: 500 ký tự. |
| ↳↳ custom_label_4 | string | Nhãn tùy chỉnh bổ sung. Giới hạn: 500 ký tự. |
| ↳↳ custom_label_5 | string | Nhãn tùy chỉnh bổ sung. Giới hạn: 500 ký tự. |
| ↳↳ custom_label_6 | string | Nhãn tùy chỉnh bổ sung. Giới hạn: 500 ký tự. |

#### Tham số mảng đối tượng `products` cho catalog trực tuyến đến ngoại tuyến (online-to-offline)

| Field | Data Type | Description |
|---|---|---|
| products | object[] | **Bắt buộc**. Danh sách các sản phẩm/dịch vụ bạn muốn tải lên. Tối đa: 5.000. |
| ↳ listing_id | string | **Bắt buộc**. ID duy nhất cho danh mục niêm yết (listing). Không giới hạn độ dài. |
| ↳ title | string | **Bắt buộc**. Tên của niêm yết. Độ dài khuyến nghị: 25 ký tự. Ví dụ: `Big Mac`. |
| ↳ description | string | **Bắt buộc**. Mô tả về niêm yết. Giới hạn: 5.000 ký tự (khuyến nghị 40 ký tự). Ví dụ: `Nice burger!`. |
| ↳ availability | string | **Bắt buộc**. Tình trạng khả dụng của niêm yết. Giá trị enum: `IN_STOCK`, `AVAILABLE_FOR_ORDER`, `PREORDER`, `OUT_OF_STOCK`, `DISCONTINUED`. |
| ↳ image_url | string | **Bắt buộc**. URL hình ảnh chính của niêm yết (bắt đầu bằng `http://` hoặc `https://`, định dạng JPG, JPEG hoặc PNG, kích thước từ 500×500 đến 1290×2790 px). Ví dụ: `https://www.tiktok.com/tiktok_service_001.jpg`. |
| ↳ brand | string | Tên thương hiệu của niêm yết. Giới hạn: 150 ký tự. |
| ↳ google_product_category | string | Phân loại danh mục theo Google product taxonomy (tối đa 3 cấp). Chi tiết xem [Google product category](https://support.google.com/merchants/answer/6324436). Ví dụ: `Apparel & Accessories > Clothing > Dresses`. |
| ↳ item_group_id | string | SPU ID dùng chung cho các biến thể của sản phẩm. Ví dụ: `TikTok_1234`. |
| ↳ additional_image_urls | string[] | Danh sách URL hình ảnh bổ sung (tối đa 20 URL, định dạng JPG/JPEG/PNG, 500x500 đến 1290x2790 px). Ví dụ: `https://www.tiktok.com/tiktok_service_002.jpg`. |
| ↳ global_trade_item_number | string | Mã số thương phẩm toàn cầu (GTIN) của mặt hàng (8, 12, 13 hoặc 14 chữ số). Ví dụ: `323456789012`. |
| ↳ address | object | Thông tin địa chỉ cửa hàng/địa điểm cung cấp. |
| ↳↳ street | string | Địa chỉ đường phố nơi đặt sản phẩm/dịch vụ. Giới hạn: 150 ký tự. Ví dụ: `1143 coleman Avenue`. |
| ↳↳ city | string | Thành phố. Giới hạn: 150 ký tự. Ví dụ: `San Jose`. |
| ↳↳ region | string | Bang/tỉnh/khu vực hành chính. Giới hạn: 150 ký tự. Ví dụ: `California`. |
| ↳↳ postal_code | string | Mã bưu chính hoặc mã ZIP. Giới hạn: 150 ký tự. Ví dụ: `95050`. |
| ↳ longitude | float | Kinh độ địa điểm. Phạm vi: [-180, 180]. Ví dụ: `100.5`. |
| ↳ latitude | float | Vĩ độ địa điểm. Phạm vi: [-90, 90]. Ví dụ: `-25.5`. |
| ↳ product_detail | object | Thông tin chi tiết khác của niêm yết. |
| ↳↳ product_category | string | Danh mục sản phẩm/dịch vụ thuộc về. Ví dụ: `Thai food`. |
| ↳↳ rating | double | Điểm đánh giá của người dùng. Phạm vi: 0.0 - 5.0. |
| ↳↳ condition | string | Tình trạng của mặt hàng: `NEW`, `USED`, `REFURBISHED`. |
| ↳↳ color | string | Màu sắc. Ví dụ: `blue`. |
| ↳↳ size | string | Kích thước. Ví dụ: `small`. |
| ↳↳ material | string | Chất liệu chính. Ví dụ: `cotton`. |
| ↳↳ pattern | string | Họa tiết hoặc hình in. Ví dụ: `stripes1`. |
| ↳↳ tax | string | Mức thuế áp dụng. Sử dụng tiền tệ mặc định của catalog. |
| ↳↳ age_group | string | Độ tuổi mục tiêu: `NEW_BORN`, `INFANT`, `TODDLER`, `KIDS`, `ADULT`. |
| ↳↳ gender | string | Giới tính mục tiêu: `MALE`, `FEMALE`, `UNISEX`. |
| ↳↳ availability_circle_radius | string | Bán kính hoàn thành dịch vụ hình tròn (km: > 0 và ≤ 40; dặm: > 0 và ≤ 25). Ví dụ: `20`. |
| ↳↳ availability_circle_radius_unit | string | Đơn vị bán kính: `KM` hoặc `MI`. |
| ↳↳ custom_number_0 | double | Thuộc tính số tùy chỉnh cho quản lý sản phẩm. |
| ↳↳ custom_number_1 | double | Thuộc tính số tùy chỉnh cho quản lý sản phẩm. |
| ↳↳ custom_number_2 | double | Thuộc tính số tùy chỉnh cho quản lý sản phẩm. |
| ↳↳ custom_number_3 | double | Thuộc tính số tùy chỉnh cho quản lý sản phẩm. |
| ↳↳ custom_number_4 | double | Thuộc tính số tùy chỉnh cho quản lý sản phẩm. |
| ↳ price_info | object | Thông tin giá niêm yết. |
| ↳↳ price | float | Giá của một mặt hàng niêm yết. Đảm bảo khớp với giá trên trang đích và trang thanh toán. Ví dụ: `9.99`. |
| ↳↳ sale_price | float | Giá khuyến mãi giảm giá của mặt hàng. Ví dụ: `4.99`. |
| ↳↳ sale_price_effective_date | string | Khoảng thời gian áp dụng giá khuyến mãi theo giờ UTC, định dạng `YYYY-MM-DDT23:59+00:00/YYYY-MM-DDT23:59+00:00`. Ngày bắt đầu phải trước ngày kết thúc. Ví dụ: `2026-12-11T23:59+00:00/2026-12-15T23:59+00:00`. |
| ↳ landing_page | object | Thông tin trang đích. |
| ↳↳ landing_page_url | string | URL trang đích của niêm yết (bắt đầu bằng `http://` hoặc `https://`). Nếu dùng deeplink ứng dụng, hãy dùng `ios_url` hoặc `android_url`. Ví dụ: `https://www.tiktok.com/tiktok_service`. |
| ↳↳ ios_url | string | URL ứng dụng iOS. Ví dụ: `iOS://electronic`. |
| ↳↳ ios_app_store_id | string | App Store ID cho iOS. |
| ↳↳ ios_app_name | string | Tên ứng dụng iOS. |
| ↳↳ android_url | string | URL ứng dụng Android. Ví dụ: `android://electronic`. |
| ↳↳ android_package | string | Tên gói Android package name. |
| ↳↳ android_app_name | string | Tên ứng dụng Android. |
| ↳ extra_info | object | Thông tin nhãn tùy chỉnh bổ sung. |
| ↳↳ custom_label_0 | string | Nhãn tùy chỉnh bổ sung. |
| ↳↳ custom_label_1 | string | Nhãn tùy chỉnh bổ sung. |
| ↳↳ custom_label_2 | string | Nhãn tùy chỉnh bổ sung. |
| ↳↳ custom_label_3 | string | Nhãn tùy chỉnh bổ sung. |
| ↳↳ custom_label_4 | string | Nhãn tùy chỉnh bổ sung. |

### Phản hồi

| Field | Data Type | Description |
|---|---|---|
| code | number | Mã phản hồi. Để xem danh sách đầy đủ các mã và mô tả, xem [Phụ lục - Mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông điệp phản hồi. Xem [Phụ lục - Mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | ID bản ghi của yêu cầu, định danh duy nhất cho mỗi yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ feed_log_id | string | ID nhật ký xử lý catalog (catalog handling log ID). |

### Ví dụ

#### cURL
```bash
curl -X POST 'https://business-api.tiktok.com/open_api/v1.3/catalog/product/upload/' \
  -H 'Access-Token: YOUR_ACCESS_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{
    "bc_id": "7123456789012345678",
    "catalog_id": "7234567890123456789",
    "feed_id": "7345678901234567890",
    "products": [
      {
        "sku_id": "TikTok_item_1234",
        "title": "T-Shirt (Unisex)",
        "description": "A vibrant crewneck for all shapes and sizes. Made from 100% cotton.",
        "availability": "IN_STOCK",
        "image_url": "https://www.tiktok.com/t_shirt_image_001.jpg",
        "brand": "TikTok",
        "additional_image_urls": [
          "https://www.tiktok.com/t_shirt_image_002.jpg",
          "https://www.tiktok.com/t_shirt_image_003.jpg"
        ],
        "item_group_id": "TikTok_1234_sample",
        "google_product_category": "Apparel & Accessories > Clothing > Shirts",
        "global_trade_item_number": "3234567890126",
        "manufacturer_part_number": "12433",
        "product_detail": {
          "condition": "NEW",
          "age_group": "ADULT",
          "color": "blue",
          "gender": "UNISEX",
          "material": "cotton",
          "pattern": "stripes1",
          "product_category": "Apparel & Accessories > Clothing > Shirts",
          "shipping": "US:CA:Ground:9.99 USD",
          "size": "Medium",
          "tax": "0.08"
        },
        "price_info": {
          "price": 30.0,
          "currency": "USD",
          "sale_price": 20.0,
          "sale_price_effective_date": "2023-12-11T23:59+00:00/2023-12-15T23:59+00:00"
        },
        "landing_page": {
          "landing_page_url": "https://www.tiktok.com/tiktok_t_shirt"
        },
        "extra_info": {
          "custom_label_0": "Summer Collection",
          "custom_label_1": "Best Seller"
        }
      }
    ]
  }'
```

#### Python
```python
import requests

url = "https://business-api.tiktok.com/open_api/v1.3/catalog/product/upload/"
headers = {
    "Access-Token": "YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}
payload = {
    "bc_id": "7123456789012345678",
    "catalog_id": "7234567890123456789",
    "feed_id": "7345678901234567890",
    "products": [
        {
            "sku_id": "TikTok_item_1234",
            "title": "T-Shirt (Unisex)",
            "description": "A vibrant crewneck for all shapes and sizes. Made from 100% cotton.",
            "availability": "IN_STOCK",
            "image_url": "https://www.tiktok.com/t_shirt_image_001.jpg",
            "brand": "TikTok",
            "product_detail": {
                "condition": "NEW",
                "age_group": "ADULT",
                "gender": "UNISEX"
            },
            "price_info": {
                "price": 30.0,
                "currency": "USD"
            },
            "landing_page": {
                "landing_page_url": "https://www.tiktok.com/tiktok_t_shirt"
            }
        }
    ]
}

response = requests.post(url, headers=headers, json=payload)
data = response.json()
print("Code:", data.get("code"))
print("Feed Log ID:", data.get("data", {}).get("feed_log_id"))
```

#### Ví dụ phản hồi thành công
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202312151030200102422470530400B987",
  "data": {
    "feed_log_id": "7312345678901234567"
  }
}
```
