# Chẩn đoán Catalog

> Phân hệ: apiref:Catalog Diagnostics.
> Tài liệu biên dịch kỹ thuật chi tiết theo chuẩn TikTok Business API v1.3.

---

## Mục lục điều hướng
- [1. Chẩn đoán danh mục (Catalog Diagnostics) (#doc-1771117054564354)](#doc-1771117054564354)
- [2. Lấy thông tin chẩn đoán sản phẩm danh mục đồng bộ (Get synchronous catalog product diagnostic information) (#doc-1771117232728066)](#doc-1771117232728066)
- [3. Tạo tác vụ tải xuống bất đồng bộ cho thông tin chẩn đoán sản phẩm danh mục (Create an asynchronous download task for catalog product diagnostic information) (#doc-1771117279175682)](#doc-1771117279175682)
- [4. Tải xuống thông tin chẩn đoán sản phẩm danh mục bất đồng bộ (Download asynchronous catalog product diagnostic information) (#doc-1771117294731266)](#doc-1771117294731266)
- [5. Lấy thông tin chẩn đoán nguồn sự kiện danh mục (Get catalog event source diagnostic information) (#doc-1780799405041665)](#doc-1780799405041665)
- [6. Lấy xu hướng sự kiện danh mục và tỷ lệ khớp (Get catalog event trends and match rate) (#doc-1780802101608450)](#doc-1780802101608450)

---

<a id="doc-1771117054564354"></a>
<!-- doc_id: 1771117054564354 -->
<!-- doc_id: 1771117054564354 -->
# Chẩn đoán danh mục (Catalog Diagnostics)
> Đường dẫn: API Reference > Catalog Diagnostics
> **Quan trọng:** Khi sử dụng các endpoint Catalog API, bạn đồng ý với [Điều khoản Danh mục Sản phẩm](https://ads.tiktok.com/i18n/official/article?aid=6765817026859499525) và cam kết tuân thủ [Chính sách Quảng cáo của TikTok](https://ads.tiktok.com/help/article?aid=6685586866860720134). Vui lòng xem lại các chính sách này và đảm bảo các sản phẩm bạn tải lên danh mục không vi phạm quy định.

Danh mục (Catalog) là tài sản cho phép bạn lưu trữ thông tin về các sản phẩm bạn muốn quảng bá trên TikTok. Sử dụng danh mục là giải pháp tối ưu cho những nhà quảng cáo muốn tạo và quản lý quảng cáo cho nhiều sản phẩm một cách hiệu quả, chẳng hạn như nhà bán lẻ trực tuyến. Catalog Diagnostics API cho phép bạn lấy thông tin chẩn đoán danh mục cho sản phẩm hoặc nguồn sự kiện.

Xem [Tổng quan](../09-marketing-api/catalog.md#doc-1754263078057986) và [Hướng dẫn](../09-marketing-api/catalog.md#doc-1754263100123137) để tìm hiểu khái niệm, lợi ích của danh mục và cách tạo, quản lý danh mục. Để biết các bước sử dụng Chẩn đoán Danh mục, xem [Khắc phục sự cố danh mục bằng chẩn đoán](../09-marketing-api/catalog.md#doc-1780803490136066) và [Ánh xạ giữa tính năng Chẩn đoán Danh mục trên Trình quản lý Danh mục với cấu hình API](../09-marketing-api/catalog.md#doc-1780803525320706).

Nhóm API này bao gồm các endpoint sau:

* [Lấy thông tin chẩn đoán sản phẩm danh mục đồng bộ](32-catalog-diagnostics.md#doc-1771117232728066)
* [Tạo tác vụ tải xuống bất đồng bộ cho thông tin chẩn đoán sản phẩm danh mục](32-catalog-diagnostics.md#doc-1771117279175682)
* [Tải xuống thông tin chẩn đoán sản phẩm danh mục bất đồng bộ](32-catalog-diagnostics.md#doc-1771117294731266)
* [Lấy thông tin chẩn đoán nguồn sự kiện danh mục](32-catalog-diagnostics.md#doc-1780799405041665)
* [Lấy xu hướng sự kiện danh mục và tỷ lệ khớp](32-catalog-diagnostics.md#doc-1780802101608450)

---

<a id="doc-1771117232728066"></a>
<!-- doc_id: 1771117232728066 -->
<!-- doc_id: 1771117232728066 -->
# Lấy thông tin chẩn đoán sản phẩm danh mục đồng bộ (Get synchronous catalog product diagnostic information)
> Đường dẫn: API Reference > Catalog Diagnostics > Get synchronous catalog product diagnostic information
Sử dụng endpoint này để truy xuất thông tin chẩn đoán đồng bộ cho các sản phẩm trong danh mục của bạn.
- Nếu phát hiện sự cố trong danh mục của bạn, thông tin chẩn đoán gần nhất có thể được tạo cho ngày hôm trước. Sự chậm trễ này là do độ trễ một ngày trong dữ liệu chẩn đoán danh mục, tính theo giờ UTC+0.
- Nếu không phát hiện sự cố nào trong danh mục của bạn, thông tin chẩn đoán trả về sẽ để trống.

Để tạo tác vụ tải xuống bất đồng bộ thông tin chẩn đoán sản phẩm danh mục, hãy sử dụng [/diagnostic/catalog/product/task/create/](32-catalog-diagnostics.md#doc-1771117279175682). Lưu ý rằng thông tin chẩn đoán do tác vụ tải xuống bất đồng bộ cung cấp ít chi tiết hơn so với thông tin từ endpoint này. Tác vụ tải xuống bất đồng bộ chỉ trả về ID sản phẩm (`product_id`), ID SKU (`sku_id` / `hotel_id` / `flight_id` / `destination_id`), Tiêu đề mục (`title`), Tiêu đề sự cố (`issue_title`), Mức độ nghiêm trọng (`issue_level`) và Nguồn (tên nguồn cấp dữ liệu) cho từng sự cố.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/diagnostic/catalog/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
| catalog_id ***(Bắt buộc)*** | string | ID của danh mục mà bạn có quyền truy cập. |
| bc_id ***(Bắt buộc)*** | string | ID của Business Center sở hữu danh mục hoặc đã được cấp quyền truy cập danh mục như một tài sản. |
| feed_id | string | ID nguồn cấp dữ liệu (Feed ID). <br>Nếu không chỉ định, ID của nguồn cấp dữ liệu mặc định cho danh mục sẽ được sử dụng. <br>Để truy xuất chẩn đoán cho tất cả nguồn cấp dữ liệu của danh mục, hãy đặt trường này thành `ALL`. <br>Để lấy ID nguồn cấp dữ liệu cho danh mục, sử dụng [/catalog/feed/get/](27-catalog-feeds.md#doc-1740665183073281). |
| filtering | object | Điều kiện lọc dữ liệu. |
| ↳ issue_level | string | Mức độ nghiêm trọng của sự cố để lọc kết quả. <br>Các giá trị enum hỗ trợ: <ul><li> `CRITICAL`: Lọc các sự cố nghiêm trọng cần xử lý ngay lập tức. </li><li>`WARNING`: Lọc các sự cố cảnh báo có đề xuất để tối ưu hóa cài đặt sản phẩm. </li></ul>|
| ↳ issue_category | string | Phân loại sự cố để lọc kết quả. <br>Các giá trị enum hỗ trợ: <ul><li>`PRODUCT_ATTRIBUTES`: Sự cố thuộc tính sản phẩm. </li><li>`PRODUCT_REVIEW`: Sự cố phê duyệt sản phẩm. </li><li>`CATALOG`: Sự cố danh mục.</li><li>`PIXEL_OR_EVENT`: Sự cố Pixel hoặc sự kiện.</li><li>`FILE_UPLOAD_OR_FEED`: Sự cố tải tệp hoặc nguồn cấp dữ liệu. </li></ul> |
| lang | string | Ngôn ngữ bạn muốn đặt cho `issue_title` và `reason_and_suggestion` trả về. <br>Giá trị mặc định: `en`. <br>Để tra cứu các giá trị enum, xem mục <a href="#item-link-Enum values for lang">Giá trị enum cho `lang`</a> bên dưới. |
| page | integer | Số trang hiện tại cần lấy dữ liệu. <br>Giá trị mặc định: 1. <br>Phạm vi giá trị: ≥1. |
| page_size | integer | Số lượng kết quả trên mỗi trang. <br>Giá trị mặc định: 10. <br>Phạm vi giá trị: [1, 20]. |
### Giá trị enum cho `lang` (Enum values for `lang`)

| Giá trị (Value) | Mô tả (Description) |
|---|---|
| `ar` | Tiếng Ả Rập |
| `cs-CZ` | Tiếng Séc |
| `de` | Tiếng Đức |
| `en` | Tiếng Anh |
| `es` | Tiếng Tây Ban Nha |
| `fil` | Tiếng Filipino |
| `fr` | Tiếng Pháp |
| `id` | Tiếng Indonesia |
| `it` | Tiếng Ý |
| `ja` | Tiếng Nhật |
| `ko` | Tiếng Hàn |
| `ms` | Tiếng Mã Lai |
| `pl-PL` | Tiếng Ba Lan |
| `pt` | Tiếng Bồ Đào Nha (Brazil) |
| `ru` | Tiếng Nga |
| `sv-SE` | Tiếng Thụy Điển |
| `th` | Tiếng Thái |
| `tr` | Tiếng Thổ Nhĩ Kỳ |
| `vi` | Tiếng Việt |
| `zh` | Tiếng Trung |

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/diagnostic/catalog/?catalog_id={{catalog_id}}&bc_id={{bc_id}}&filtering={"issue_level":"CRITICAL"}&lang=en&page=1&page_size=20' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json'
```
## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|-|-|-|
| code | number | Mã phản hồi (Response code). Để biết danh sách mã phản hồi và mô tả đầy đủ, xem [Phụ lục - Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. Để biết chi tiết, xem [Phụ lục - Mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | Mã nhật ký (Log ID) của yêu cầu, định danh duy nhất cho mỗi yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ diagnostic_date | string | Ngày (theo giờ UTC+0) thông tin chẩn đoán được tạo, theo định dạng `"YYYY-MM-DD"`. <br>Ví dụ: `"2023-06-15"`. |
| ↳ issues | object[] | Thông tin chẩn đoán về các sự cố phát hiện trong danh mục. |
| ↳↳ issue_id | string | ID sự cố. <br>Một số ID sự cố có thể được truyền vào endpoint [/diagnostic/catalog/product/task/create/](32-catalog-diagnostics.md#doc-1771117279175682) để tạo tác vụ tải xuống bất đồng bộ cho thông tin chẩn đoán sự cố đó. |
| ↳↳ issue_title | string | Tiêu đề sự cố, cung cấp bản tóm tắt về sự cố. |
| ↳↳ reason_and_suggestion | string | Nguyên nhân và đề xuất khắc phục. <br>Trường này chứa mô tả sự cố và đề xuất hướng xử lý. |
| ↳↳ issue_level | string | Mức độ nghiêm trọng của sự cố. <br>Các giá trị enum hỗ trợ: <ul><li>`CRITICAL`: Sự cố nghiêm trọng cần xử lý ngay lập tức. </li><li>`WARNING`: Sự cố cảnh báo có kèm đề xuất để tối ưu cài đặt sản phẩm. </li></ul>|
| ↳↳ issue_category | string | Phân loại sự cố. <br>Các giá trị enum hỗ trợ: <ul><li>`PRODUCT_ATTRIBUTES`: Sự cố thuộc tính sản phẩm. </li><li>`PRODUCT_REVIEW`: Sự cố phê duyệt sản phẩm. </li><li>`CATALOG`: Sự cố danh mục. </li><li>`PIXEL_OR_EVENT`: Sự cố Pixel hoặc sự kiện. </li><li>`FILE_UPLOAD_OR_FEED`: Sự cố tải tệp hoặc nguồn cấp dữ liệu.</li></ul>|
| ↳↳ issue_product_field | string | Trường sản phẩm bị phát hiện sự cố. |
| ↳↳ affected_product_count | integer | Số lượng sản phẩm trong danh mục bị phát hiện sự cố. |
| ↳↳ affected_product_percentage | number | Tỷ lệ phần trăm sản phẩm trong danh mục bị phát hiện sự cố. <br>Phạm vi giá trị: [0,100]. |
| ↳↳ example_affected_products | object[] | Được trả về khi giá trị của `affected_product_count` lớn hơn 0. <br><br>Mảng đối tượng chứa tối đa 10 sản phẩm mẫu trong danh mục bị phát hiện sự cố. Bạn có thể sử dụng các trường trong mảng này để phân tích chi tiết. <br><br>Cấu trúc của mảng đối tượng này tương tự tham số `list` trong phản hồi của [/catalog/product/get/](28-catalog-products-p2.md#doc-1740564136678402). Lưu ý rằng các trường cụ thể trả về sẽ tùy thuộc vào loại sản phẩm. Ví dụ, `hotel_id` chỉ trả về cho sản phẩm danh mục khách sạn. |
| ↳ page_info | object | Thông tin phân trang. |
| ↳↳ page | number | Số trang hiện tại. |
| ↳↳ page_size | number | Số lượng kết quả trên mỗi trang. |
| ↳↳ total_number | number | Tổng số kết quả tìm thấy. |
| ↳↳ total_page | number | Tổng số trang kết quả. |
### Ví dụ lệnh cURL (Example)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "issues": [
            {
                "affected_product_percentage": 0.06253552657278164,
                "example_affected_products": [],
                "issue_id": "2002",
                "issue_level": "CRITICAL",
                "affected_product_count": 714,
                "issue_product_field": "",
                "issue_category": "PRODUCT_ATTRIBUTES",
                "reason_and_suggestion": "Check and update the link to an image that is at least 500x500 pixels",
                "issue_title": "Image is less than 500x500 pixels"
            },
            {
                "affected_product_percentage": 0.21221790040035,
                "example_affected_products": [],
                "issue_id": "3001",
                "issue_level": "CRITICAL",
                "affected_product_count": 2423,
                "issue_product_field": "",
                "issue_category": "PRODUCT_REVIEW",
                "reason_and_suggestion": "Update product info and appeal to continue. For approval, make sure newly updated products follow our Ad Policy.",
                "issue_title": "Product was disapproved due to prohibited content"
            },
            {
                "affected_product_percentage": 0.026363016104211864,
                "example_affected_products": [],
                "issue_id": "2004",
                "issue_level": "CRITICAL",
                "affected_product_count": 301,
                "issue_product_field": "",
                "issue_category": "PRODUCT_ATTRIBUTES",
                "reason_and_suggestion": "Check and update the image link. It must end with .jpeg or .png.",
                "issue_title": "Image link is invalid and can't be downloaded"
            },
            {
                "affected_product_percentage": 0.0053426710377306435,
                "example_affected_products": [],
                "issue_id": "2003",
                "issue_level": "CRITICAL",
                "affected_product_count": 61,
                "issue_product_field": "",
                "issue_category": "PRODUCT_ATTRIBUTES",
                "reason_and_suggestion": "Check the feed link and upload a file that is in CSV, XML, TSV, or GZIP format.",
                "issue_title": "Incorrect feed file or link format"
            },
            {
                "affected_product_percentage": 0.002539958362199814,
                "example_affected_products": [],
                "issue_id": "2001",
                "issue_level": "CRITICAL",
                "affected_product_count": 29,
                "issue_product_field": "",
                "issue_category": "PRODUCT_ATTRIBUTES",
                "reason_and_suggestion": "Check that the image hosting site doesn't block TikTok's server from fetching information.",
                "issue_title": "TikTok doesn't have permissions to access the image information hosted on your server"
            },
            {
                "affected_product_percentage": 6.694191640734276,
                "example_affected_products": [
                    {
                        "brand": "{{brand}}",
                        "product_version": "{{product_version}}",
                        "product_id": "{{product_id}}",
                        "item_group_id": "{{item_group_id}}",
                        "description": "{{description}}",
                        "title": "{{title}}",
                        "image_status": "SUCCESS",
                        "availability": "IN_STOCK",
                        "sku_id": "{{sku_id}}",
                        "profession": {
                            "condition": "NEW"
                        },
                        "image": [
                            {
                                "url": "{{url}}"
                            }
                        ],
                        "google_product_category": "",
                        "price": {
                            "sale_price": 0,
                            "price": 104.18,
                            "sale_price_effective_date": []
                        },
                        "audit": {
                            "audit_status": "approved"
                        },
                        "active_status": "ACTIVATED",
                        "image_url": "{{image_url}}",
                        "additional_image_urls": [],
                        "video_url": "",
                        "global_trade_item_number": "",
                        "manufacturer_part_number": "",
                        "landing_page": {
                            "android_url": "",
                            "ios_app_store_id": "",
                            "android_app_name": "",
                            "ios_app_name": "",
                            "iphone_app_name": "",
                            "ipad_app_store_id": "",
                            "ipad_app_name": "",
                            "android_package": "",
                            "ios_url": "",
                            "url": "{{url}}",
                            "iphone_app_store_id": "",
                            "landing_page_url": "{{landing_page_url}}"
                        },
                        "extra_info": {
                            "custom_label_4": "{{custom_label_4}}",
                            "custom_label_1": null,
                            "custom_label_3": null,
                            "custom_label_0": null,
                            "custom_label_2": null
                        }
                    },
                    {
                        "brand": "{{brand}}",
                        "product_version": "{{product_version}}",
                        "product_id": "{{product_id}}",
                        "item_group_id": "{{item_group_id}}",
                        "description": "{{description}}",
                        "title": "{{title}}",
                        "image_status": "SUCCESS",
                        "availability": "IN_STOCK",
                        "sku_id": "{{sku_id}}",
                        "profession": {
                            "condition": "NEW"
                        },
                        "image": [
                            {
                                "url": "{{url}}"
                            }
                        ],
                        "google_product_category": "",
                        "price": {
                            "sale_price": 0,
                            "price": 103.46,
                            "sale_price_effective_date": []
                        },
                        "audit": {
                            "audit_status": "approved"
                        },
                        "active_status": "ACTIVATED",
                        "image_url": "{{image_url}}",
                        "additional_image_urls": [],
                        "video_url": "",
                        "global_trade_item_number": "",
                        "manufacturer_part_number": "",
                        "landing_page": {
                            "android_url": "",
                            "ios_app_store_id": "",
                            "android_app_name": "",
                            "ios_app_name": "",
                            "iphone_app_name": "",
                            "ipad_app_store_id": "",
                            "ipad_app_name": "",
                            "android_package": "",
                            "ios_url": "",
                            "url": "{{url}}",
                            "iphone_app_store_id": "",
                            "landing_page_url": "{{landing_page_url}}"
                        },
                        "extra_info": {
                            "custom_label_4": "{{custom_label_4}}",
                            "custom_label_1": null,
                            "custom_label_3": null,
                            "custom_label_0": null,
                            "custom_label_2": null
                        }
                    }   
                ],
                "issue_id": "4003",
                "issue_level": "CRITICAL",
                "affected_product_count": 76431,
                "issue_product_field": "",
                "issue_category": "PRODUCT_ATTRIBUTES",
                "reason_and_suggestion": "Update the product price.",
                "issue_title": "Prices on the product and landing page don't match."
            }
        ],
        "page_info": {
            "total_page": 1,
            "page_size": 20,
            "page": 1,
            "total_number": 6
        },
        "diagnostic_date": "2023-07-05"
    }
}
```

---

<a id="doc-1771117279175682"></a>
<!-- doc_id: 1771117279175682 -->
<!-- doc_id: 1771117279175682 -->
# Tạo tác vụ tải xuống bất đồng bộ cho thông tin chẩn đoán sản phẩm danh mục (Create an asynchronous download task for catalog product diagnostic information)
> Đường dẫn: API Reference > Catalog Diagnostics > Create an asynchronous download task for catalog product diagnostic information
Sử dụng endpoint này để tạo tác vụ tải xuống bất đồng bộ cho thông tin chẩn đoán sản phẩm danh mục.

Sau khi tác vụ được tạo, hãy sử dụng [/diagnostic/catalog/product/task/get/](32-catalog-diagnostics.md#doc-1771117294731266) để tải xuống tệp CSV kết quả. Lưu ý rằng thông tin chẩn đoán do tác vụ tải xuống bất đồng bộ cung cấp ít chi tiết hơn so với thông tin chẩn đoán đồng bộ từ endpoint /diagnostic/catalog/. Tác vụ tải xuống bất đồng bộ chỉ trả về ID sản phẩm (`product_id`), ID SKU (`sku_id` / `hotel_id` / `flight_id` / `destination_id`), Tiêu đề mục (`title`), Tiêu đề sự cố (`issue_title`), Mức độ nghiêm trọng (`issue_level`) và Nguồn (tên nguồn cấp dữ liệu) cho từng sự cố.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/diagnostic/catalog/product/task/create/ 

**Method** POST

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type  ****(Bắt buộc)**** | string | Định dạng dữ liệu yêu cầu. ⏎ Định dạng cho phép: `application/json`. |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
| catalog_id ***(Bắt buộc)*** | string | ID của danh mục mà bạn có quyền truy cập. |
| bc_id ***(Bắt buộc)*** | string | ID của Business Center sở hữu danh mục hoặc đã được cấp quyền truy cập danh mục như một tài sản. |
| feed_id | string | ID nguồn cấp dữ liệu (Feed ID). <br>Nếu không chỉ định, ID của nguồn cấp dữ liệu mặc định cho danh mục sẽ được sử dụng. <br>Để truy xuất chẩn đoán cho tất cả nguồn cấp dữ liệu của danh mục, hãy đặt trường này thành `ALL`. <br>Để lấy ID nguồn cấp dữ liệu cho danh mục, sử dụng [/catalog/feed/get/](27-catalog-feeds.md#doc-1740665183073281). |
| lang | string | Ngôn ngữ bạn muốn đặt cho thông tin chẩn đoán danh mục trả về. <br>Giá trị mặc định: `en`. <br>Để tra cứu các giá trị enum, xem mục <a href="#item-link-Enum values for lang">Giá trị enum cho `lang`</a> bên dưới. |
| issue_id | string | ID của sự cố bạn muốn tải xuống thông tin chẩn đoán.<br>Bạn cần chỉ định ID của một sự cố có thể tải xuống, chọn từ bảng <a href="#item-link-Downloadable issues">Các sự cố có thể tải xuống</a> bên dưới.<br>Nếu không chỉ định, kết quả chẩn đoán cho toàn bộ các sự cố phát hiện được sẽ được trả về. |

### Giá trị enum cho `lang` (Enum values for `lang`)

| Giá trị (Value) | Mô tả (Description) |
|---|---|
| `ar` | Tiếng Ả Rập |
| `cs-CZ` | Tiếng Séc |
| `de` | Tiếng Đức |
| `en` | Tiếng Anh |
| `es` | Tiếng Tây Ban Nha |
| `fil` | Tiếng Filipino |
| `fr` | Tiếng Pháp |
| `id` | Tiếng Indonesia |
| `it` | Tiếng Ý |
| `ja` | Tiếng Nhật |
| `ko` | Tiếng Hàn |
| `ms` | Tiếng Mã Lai |
| `pl-PL` | Tiếng Ba Lan |
| `pt` | Tiếng Bồ Đào Nha (Brazil) |
| `ru` | Tiếng Nga |
| `sv-SE` | Tiếng Thụy Điển |
| `th` | Tiếng Thái |
| `tr` | Tiếng Thổ Nhĩ Kỳ |
| `vi` | Tiếng Việt |
| `zh` | Tiếng Trung |

### Các sự cố có thể tải xuống (Downloadable issues)
Nếu bạn muốn tải xuống chẩn đoán cho một sự cố cụ thể, hãy truyền một trong các ID sự cố ở bảng bên dưới vào tham số `issue_id`.

| issue_id | Mô tả (Description) |
|---|---|
| `1101` | Thiếu trường thuộc tính sản phẩm bắt buộc. |
| `1102` | Nhập giá trị không hợp lệ cho trường bắt buộc. |
| `1103` | Trùng lặp ID sản phẩm (chẳng hạn như SKU ID). |
| `1105` | Nhập giá trị không hợp lệ cho trường tùy chọn. |
| `1106` | Thiếu trường tùy chọn nhưng được khuyến nghị. |
| `1107` | Số lượng cột của một mục trên nguồn cấp dữ liệu hoặc tệp không khớp với số lượng cột ở hàng đầu tiên. |
| `1108` | Chỉ sử dụng chữ in hoa cho giá trị trường. |
| `1109` | Số lượng liên kết hình ảnh bổ sung vượt quá giới hạn tối đa là 10. |
| `1110` | Định dạng URL tùy chọn không hợp lệ. |
| `1111` | Định dạng URL bắt buộc không hợp lệ. |
| `1112` | Sử dụng bộ ký tự không phải UTF-8. |
| `1113` | Sử dụng biểu tượng cảm xúc (emoji) hoặc ký tự điều khiển. |
| `2001` | Tải xuống hình ảnh thất bại do sự cố máy chủ. |
| `2002` | Kích thước hình ảnh nhỏ hơn 500 x 500 pixel. |
| `2003` | Định dạng tệp nguồn cấp dữ liệu hoặc liên kết không hợp lệ. |
| `2004` | Liên kết hình ảnh không hợp lệ, không thể tải xuống thông tin hình ảnh. |
| `3001` | Sản phẩm bị từ chối phê duyệt do vi phạm chính sách nội dung cấm. |
| `4001` | Liên kết sản phẩm không hợp lệ. |
| `4002` | Không thể truy cập liên kết sản phẩm. |
| `4003` | Giá sản phẩm trên danh mục và trang đích không khớp nhau. |
| `4005` | Trường Item Group ID chưa được điền. |
| `4006` | Trường liên kết hình ảnh bổ sung của sản phẩm chưa được điền. |
| `4007` | Trường Product Type chưa được điền. |
| `4008` | Trường Google Product Category chưa được điền. |
| `4009` | Trường Global Trade Item Number (GTIN) chưa được điền. |

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/diagnostic/catalog/product/task/create/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "catalog_id":"{{catalog_id}}",
    "bc_id":"{{bc_id}}"
}'
```
## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|-|-|-|
| code | number | Mã phản hồi từ API. Để biết danh sách mã phản hồi và mô tả đầy đủ, xem [Phụ lục - Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message|string|Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
| request_id | string | Mã nhật ký (Log ID) của yêu cầu, định danh duy nhất cho mỗi yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ task_id | string | ID của tác vụ tải xuống thông tin chẩn đoán danh mục. |
### Ví dụ lệnh cURL (Example)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "task_id": "{{task_id}}"
    }
}
```

---

<a id="doc-1771117294731266"></a>
<!-- doc_id: 1771117294731266 -->
<!-- doc_id: 1771117294731266 -->
# Tải xuống thông tin chẩn đoán sản phẩm danh mục bất đồng bộ (Download asynchronous catalog product diagnostic information)
> Đường dẫn: API Reference > Catalog Diagnostics > Download asynchronous catalog product diagnostic information
Sử dụng endpoint này để tải xuống tệp CSV chứa thông tin chẩn đoán sản phẩm danh mục.

Lưu ý rằng tệp CSV chỉ trả về ID sản phẩm (`product_id`), ID SKU (`sku_id` / `hotel_id` / `flight_id` / `destination_id`), Tiêu đề mục (`title`), Tiêu đề sự cố (`issue_title`), Mức độ nghiêm trọng (`issue_level`) và Nguồn (tên nguồn cấp dữ liệu) cho từng sự cố. Để lấy thông tin chẩn đoán danh mục đồng bộ chi tiết hơn, hãy sử dụng [/diagnostic/catalog/](32-catalog-diagnostics.md#doc-1771117232728066).

## Điều kiện tiên quyết trước khi bắt đầu
Bạn cần đảm bảo đã tạo tác vụ tải xuống thông tin chẩn đoán sản phẩm danh mục bằng cách sử dụng [/diagnostic/catalog/product/task/create/](32-catalog-diagnostics.md#doc-1771117279175682).

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/diagnostic/catalog/product/task/get/  

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
| catalog_id ***(Bắt buộc)*** | string | ID danh mục sản phẩm bạn đã dùng để tạo tác vụ tải xuống thông tin chẩn đoán danh mục. |
| bc_id ***(Bắt buộc)*** | string | ID Business Center (BC ID) bạn đã dùng để tạo tác vụ tải xuống thông tin chẩn đoán danh mục. |
| task_id ***(Bắt buộc)*** | string | ID của tác vụ tải xuống thông tin chẩn đoán danh mục. <br>Để lấy ID này, sử dụng [/diagnostic/catalog/product/task/create/](32-catalog-diagnostics.md#doc-1771117279175682). |
### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/diagnostic/catalog/product/task/get/?catalog_id={{catalog_id}}&bc_id={{bc_id}}&task_id={{task_id}}' \
--header 'Access-Token: {{Access-Token}}'
```
## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|-|-|-|
| code | number | Mã phản hồi từ API. Để biết danh sách mã phản hồi và mô tả đầy đủ, xem [Phụ lục - Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message|string|Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
| request_id | string | Mã nhật ký (Log ID) của yêu cầu, định danh duy nhất cho mỗi yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ status | string | Trạng thái của tác vụ tải xuống thông tin chẩn đoán danh mục. <br>Các giá trị enum hỗ trợ: <ul><li>`SUCCEED`: Tác vụ thành công. Bạn có thể tải tệp thông tin chẩn đoán danh mục qua URL trả về trong trường `diagnostic_file_url`. </li><li>`PROCESSING`: Tác vụ đang được xử lý.</li><li>`FAILED`: Tác vụ thất bại.</li></ul>|
| ↳ diagnostic_file_url | string | URL tải xuống tệp CSV chứa thông tin chẩn đoán danh mục. <br><p><span style="color:darkred"><b>Lưu ý</b></span>: URL này không có thời hạn hết hạn. |
### Ví dụ lệnh cURL (Example)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "status": "SUCCEED",
        "diagnostic_file_url": "{{diagnostic_file_url}}"
    }
}
```

---

<a id="doc-1780799405041665"></a>
<!-- doc_id: 1780799405041665 -->
<!-- doc_id: 1780799405041665 -->
# Lấy thông tin chẩn đoán nguồn sự kiện danh mục (Get catalog event source diagnostic information)
> Đường dẫn: API Reference > Catalog Diagnostics > Get catalog event source diagnostic information
Sử dụng endpoint này để truy xuất thông tin chẩn đoán cho các nguồn sự kiện được liên kết với danh mục của bạn.

## Điều kiện tiên quyết trước khi bắt đầu
Đảm bảo bạn đã liên kết một nguồn sự kiện với danh mục trong Business Center bằng [/catalog/eventsource/bind/](26-catalog-event-sources.md#doc-1740492491200513) hoặc trên Trình quản lý quảng cáo TikTok Ads Manager. Để tìm hiểu thêm về cách liên kết nguồn sự kiện với danh mục trên TikTok Ads Manager, xem [Cách tạo và quản lý danh mục - Kết nối nguồn sự kiện](https://ads.tiktok.com/help/article/create-manage-catalogs?lang=en#anchor-18).

Để xác nhận xem nguồn sự kiện đã được liên kết với danh mục hay chưa, sử dụng [/catalog/eventsource_bind/get/](26-catalog-event-sources.md#doc-1740492531343362).

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/diagnostic/catalog/eventsource/issue/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
| bc_id ***(Bắt buộc)*** | string | ID Business Center (BC ID). <br><br>Để lấy danh sách Business Center mà bạn có quyền truy cập, sử dụng [/bc/get/](12-bc-management.md#doc-1737115687501826). |
| catalog_id ***(Bắt buộc)*** | string | ID danh mục sản phẩm. <br><br>Để lấy các danh mục thuộc một Business Center, sử dụng [/catalog/get/](25-catalog-management.md#doc-1740315452868610). |
| event_source_type ***(Bắt buộc)*** | string | Loại nguồn sự kiện. <br><br>Các giá trị enum hỗ trợ: <ul><li>`APP`: Ứng dụng. Truyền đồng thời `app_id`. </li><li>`PIXEL`: Pixel. Truyền đồng thời `pixel_code`. </li></ul>|
| app_id **(Điều kiện)** | string | Bắt buộc khi `event_source_type` được đặt là `APP`. <br><br>ID ứng dụng (App ID). <br><br>Để truy xuất các App ID được liên kết với danh mục (`catalog_id`), sử dụng [/catalog/eventsource_bind/get/](26-catalog-event-sources.md#doc-1740492531343362). |
| pixel_code **(Điều kiện)** | string | Bắt buộc khi `event_source_type` được đặt là `PIXEL`. <br><br>Mã Pixel. <br><br>Để truy xuất các mã Pixel được liên kết với danh mục (`catalog_id`), sử dụng [/catalog/eventsource_bind/get/](26-catalog-event-sources.md#doc-1740492531343362). |
| event_type | string | Loại sự kiện bạn muốn truy xuất dữ liệu. <br><br>Các giá trị enum hỗ trợ: <ul><li>`VIEW_CONTENT`: Xem nội dung (View Content).</li><li>`ADD_TO_CART`: Thêm vào giỏ hàng (Add to Cart).</li><li>`PURCHASE`: Hoàn tất thanh toán (Purchase / Complete Payment).</li></ul><br>Giá trị mặc định: `VIEW_CONTENT`. |
| time_range | string | Khoảng thời gian muốn truy xuất dữ liệu. <br><br>Các giá trị enum hỗ trợ: <ul><li>`YESTERDAY`: Hôm qua. </li><li>`LAST_7_DAYS`: 7 ngày qua. </li><li>`LAST_30_DAYS`: 30 ngày qua. </li></ul><br>Giá trị mặc định: `LAST_7_DAYS`. |
### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/diagnostic/catalog/eventsource/issue/?bc_id={{bc_id}}&catalog_id={{catalog_id}}&event_source_type=PIXEL&pixel_code={{pixel_code}}&event_type=VIEW_CONTENT&time_range=LAST_30_DAYS' \
--header 'Access-Token: {{Access-Token}}' \
```
## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|-|-|-|
| code | number | Mã phản hồi từ API. Để biết danh sách mã phản hồi và mô tả đầy đủ, xem [Phụ lục - Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message|string|Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
| request_id | string | Mã nhật ký (Log ID) của yêu cầu, định danh duy nhất cho mỗi yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ list | object[] | Danh sách dữ liệu trả về. |
| ↳↳ diagnostic_result | string | Sự cố được phát hiện từ chẩn đoán. <br><br>Nếu không phát hiện sự cố, giá trị trường này sẽ là "No Issues Found".<br><br>Ví dụ: `"You have fewer View Content events than Add to Cart events." ` <br><br>Để tìm hiểu về các sự cố có thể phát hiện, xem <a href="#item-link-Detectable catalog event source issues">Các sự cố nguồn sự kiện danh mục có thể phát hiện</a>. |
| ↳↳ level | string | Mức độ nghiêm trọng của sự cố. <br><br>Giá trị enum: <ul><li>`ERROR`: Lỗi. Sự cố này ảnh hưởng đến phân phối quảng cáo và cần được giải quyết. </li><li>`WARNING`: Cảnh báo. Sự cố này có thể ảnh hưởng đến phân phối quảng cáo và cần được xem xét.</li><li>`INFO`: Không có sự cố.</li></ul>|
| ↳↳ diagnostic_solution | string | Giải pháp đề xuất cho sự cố. <br><br>Nếu không phát hiện sự cố nào, giá trị trường này sẽ để trống. |

### Các sự cố nguồn sự kiện danh mục có thể phát hiện (Detectable catalog event source issues)

Bảng dưới đây liệt kê các sự cố có thể được nhận diện thông qua tính năng chẩn đoán nguồn sự kiện danh mục.

| Sự cố ⏎ (diagnostic_result) | Mức độ ⏎ (level) | Giải pháp đề xuất ⏎ (diagnostic_solution) |
|---|---|---|
| `No Issues Found. ` | `INFO` | Không phát hiện sự cố nào. |
| `Less than 80% of events received have content IDs that match the catalog's SKU IDs or item group ID. ` | `WARNING` | Xuất danh sách content ID không khớp với sản phẩm trong danh mục này. |
| `You have fewer View Content events than Add to Cart events. ` | `WARNING` | Số lượng sự kiện tầng trên phễu thường phải cao hơn tầng dưới. Khuyến nghị kiểm tra lại thiết lập nguồn sự kiện và đảm bảo sự kiện kích hoạt chính xác. |
| `You have fewer Add to Cart events than Purchase events. ` | `WARNING` | Số lượng sự kiện tầng trên phễu thường phải cao hơn tầng dưới. Khuyến nghị kiểm tra lại thiết lập nguồn sự kiện và đảm bảo sự kiện kích hoạt chính xác. |
| `The total number of events received, with or without content ID matches, is less than 100k. ` | `ERROR` | Đảm bảo nguồn sự kiện được cài đặt chuẩn xác và sự kiện có thể kích hoạt trên trang sản phẩm của bạn. |
| `Less than 90% of events received have content IDs. ` | `ERROR` | Xuất danh sách các sự kiện không có content ID. |
| `Less than 100k events were received with content IDs. ` | `ERROR` | Xuất danh sách các sự kiện không có content ID. |
| `Less than 100k events were received with content IDs that match the catalog's SKU IDs or item group IDs. ` | `ERROR` | Xuất danh sách content ID không khớp với SKU ID hoặc item group ID trong danh mục này. |

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "list": [
            {
                "diagnostic_result": "Less than 100k events were received with content IDs that match the catalog's SKU IDs or item group IDs.",
                "diagnostic_solution": "Export content IDs that don't match the products in this catalog.",
                "level": "ERROR"
            }
        ]
    }
}
```

---

<a id="doc-1780802101608450"></a>
<!-- doc_id: 1780802101608450 -->
<!-- doc_id: 1780802101608450 -->
# Lấy xu hướng sự kiện danh mục và tỷ lệ khớp (Get catalog event trends and match rate)
> Đường dẫn: API Reference > Catalog Diagnostics > Get catalog event trends and match rate
Sử dụng endpoint này để truy xuất xu hướng các sự kiện ứng dụng hoặc Pixel nhận được, xác định số lượng sự kiện khả dụng cho retargeting và lấy tỷ lệ khớp danh mục (catalog match rate) của danh mục.

## Điều kiện tiên quyết trước khi bắt đầu
Đảm bảo bạn đã liên kết một nguồn sự kiện với danh mục trong Business Center bằng [/catalog/eventsource/bind/](26-catalog-event-sources.md#doc-1740492491200513) hoặc trên Trình quản lý quảng cáo TikTok Ads Manager. Để tìm hiểu thêm về cách liên kết nguồn sự kiện với danh mục trên TikTok Ads Manager, xem [Cách tạo và quản lý danh mục - Kết nối nguồn sự kiện](https://ads.tiktok.com/help/article/create-manage-catalogs?lang=en#anchor-18).

Để xác nhận xem nguồn sự kiện đã được liên kết với danh mục hay chưa, sử dụng [/catalog/eventsource_bind/get/](26-catalog-event-sources.md#doc-1740492531343362).

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/diagnostic/catalog/eventsource/metric/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
| bc_id ***(Bắt buộc)*** | string | ID Business Center (BC ID). <br><br>Để lấy danh sách Business Center mà bạn có quyền truy cập, sử dụng [/bc/get/](12-bc-management.md#doc-1737115687501826). |
| catalog_id ***(Bắt buộc)*** | string | ID danh mục sản phẩm. <br><br>Để lấy các danh mục thuộc một Business Center, sử dụng [/catalog/get/](25-catalog-management.md#doc-1740315452868610). |
| event_source_type ***(Bắt buộc)*** | string | Loại nguồn sự kiện. <br><br>Các giá trị enum hỗ trợ: <ul><li>`APP`: Ứng dụng. Truyền đồng thời `app_id`. </li><li>`PIXEL`: Pixel. Truyền đồng thời `pixel_code`. </li></ul>|
| app_id **(Điều kiện)** | string | Bắt buộc khi `event_source_type` được đặt là `APP`. <br><br>ID ứng dụng (App ID). <br><br>Để truy xuất các App ID được liên kết với danh mục (`catalog_id`), sử dụng [/catalog/eventsource_bind/get/](26-catalog-event-sources.md#doc-1740492531343362). |
| pixel_code **(Điều kiện)** | string | Bắt buộc khi `event_source_type` được đặt là `PIXEL`. <br><br>Mã Pixel. <br><br>Để truy xuất các mã Pixel được liên kết với danh mục (`catalog_id`), sử dụng [/catalog/eventsource_bind/get/](26-catalog-event-sources.md#doc-1740492531343362). |
| event_type | string | Loại sự kiện bạn muốn truy xuất dữ liệu. <br><br>Các giá trị enum hỗ trợ: <ul><li>`VIEW_CONTENT`: Xem nội dung (View Content).</li><li>`ADD_TO_CART`: Thêm vào giỏ hàng (Add to Cart).</li><li>`PURCHASE`: Hoàn tất thanh toán (Purchase / Complete Payment).</li></ul><br>Giá trị mặc định: `VIEW_CONTENT`. |
| time_range | string | Khoảng thời gian muốn truy xuất dữ liệu. <br><br>Các giá trị enum hỗ trợ: <ul><li>`YESTERDAY`: Hôm qua. </li><li>`LAST_7_DAYS`: 7 ngày qua. </li><li>`LAST_30_DAYS`: 30 ngày qua. </li></ul><br>Giá trị mặc định: `LAST_7_DAYS`. |
### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/diagnostic/catalog/eventsource/metric/?bc_id={{bc_id}}&catalog_id={{catalog_id}}&event_source_type=PIXEL&pixel_code={{pixel_code}}&time_range=LAST_7_DAYS&event_type=PURCHASE' \
--header 'Access-Token: {{Access-Token}}' \
```
## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|-|-|-|
| code | number | Mã phản hồi từ API. Để biết danh sách mã phản hồi và mô tả đầy đủ, xem [Phụ lục - Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message|string|Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
| request_id | string | Mã nhật ký (Log ID) của yêu cầu, định danh duy nhất cho mỗi yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ list | object[] | Thông tin về xu hướng sự kiện nhận được và số lượng sự kiện khả dụng cho retargeting. |
| ↳↳ available_type | string | Các phân loại sự kiện khả dụng. <br><br>Các giá trị enum hỗ trợ: <ul><li>`EVENT_RECEIVED`: Toàn bộ sự kiện nhận được. </li><li>`EVENT_WITH_CONTENT_ID`: Các sự kiện có mã nội dung (content ID).</li><li>`EVENT_WITH_CONTENT_ID_MATCHING_INVENTORY`: Các sự kiện khớp mã nội dung với kho hàng sản phẩm (Events with content IDs that match inventory).</li></ul>|
| ↳↳ event_details | object[] | Chi tiết về phân loại sự kiện (`available_type`). |
| ↳↳↳ date | string | Ngày, theo định dạng `"YYYY-MM-DD"`.<br><br>Ví dụ: `"2023-12-30"`. |
| ↳↳↳ count | string | Số lượng sự kiện thuộc phân loại sự kiện được nhận vào ngày đó. <br><br>Ví dụ: `"245076"`. <br><br>Ví dụ khi `available_type` là `EVENT_WITH_CONTENT_ID_MATCHING_INVENTORY`, giá trị `"245076"` của trường này đại diện cho 245.076 sự kiện có content ID khớp với sản phẩm (SKU ID) trong danh mục của bạn được nhận trong ngày. |
| ↳↳↳ percentage | string | Tỷ lệ phần trăm sự kiện thuộc phân loại sự kiện nhận được trong ngày so với tổng số sự kiện nhận được. <br><br>Khi `available_type` là `EVENT_WITH_CONTENT_ID_MATCHING_INVENTORY`, giá trị trường này đại diện cho tỷ lệ khớp danh mục (catalog match rate), được tính bằng số sự kiện tín hiệu khớp sản phẩm trong danh mục chia cho tổng số sự kiện tín hiệu chia sẻ với TikTok. <br>Khuyến nghị duy trì mức tỷ lệ khớp trên 90% để đảm bảo hiệu suất tối ưu cho Quảng cáo mua sắm dạng video (Video Shopping Ads). <br><br>Ví dụ: `"100"`. <br><br><p><span style="color:darkred"><b>Lưu ý</b></span>: Khi `available_type` là `EVENT_RECEIVED`, giá trị trường này luôn là `"100"`. |

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "list": [
            {
                "available_type": "EVENT_RECEIVED",
                "event_details": [
                    {
                        "date": "2023-10-04",
                        "percentage": "100",
                        "count": "4086"
                    },
                    {
                        "date": "2023-10-05",
                        "percentage": "100",
                        "count": "4372"
                    },
                    {
                        "date": "2023-10-06",
                        "percentage": "100",
                        "count": "3939"
                    },
                    {
                        "date": "2023-10-07",
                        "percentage": "100",
                        "count": "3017"
                    },
                    {
                        "date": "2023-10-08",
                        "percentage": "100",
                        "count": "2853"
                    },
                    {
                        "date": "2023-10-09",
                        "percentage": "100",
                        "count": "5197"
                    },
                    {
                        "date": "2023-10-10",
                        "percentage": "100",
                        "count": "5050"
                    }
                ]
            },
            {
                "available_type": "EVENT_WITH_CONTENT_ID",
                "event_details": [
                    {
                        "date": "2023-10-04",
                        "percentage": "96",
                        "count": "3960"
                    },
                    {
                        "date": "2023-10-05",
                        "percentage": "97",
                        "count": "4259"
                    },
                    {
                        "date": "2023-10-06",
                        "percentage": "97",
                        "count": "3847"
                    },
                    {
                        "date": "2023-10-07",
                        "percentage": "96",
                        "count": "2899"
                    },
                    {
                        "date": "2023-10-08",
                        "percentage": "95",
                        "count": "2728"
                    },
                    {
                        "date": "2023-10-09",
                        "percentage": "96",
                        "count": "5035"
                    },
                    {
                        "date": "2023-10-10",
                        "percentage": "97",
                        "count": "4908"
                    }
                ]
            },
            {
                "available_type": "EVENT_WITH_CONTENT_ID_MATCHING_INVENTORY",
                "event_details": [
                    {
                        "date": "2023-10-04",
                        "percentage": "37",
                        "count": "1535"
                    },
                    {
                        "date": "2023-10-05",
                        "percentage": "35",
                        "count": "1572"
                    },
                    {
                        "date": "2023-10-06",
                        "percentage": "36",
                        "count": "1450"
                    },
                    {
                        "date": "2023-10-07",
                        "percentage": "33",
                        "count": "1019"
                    },
                    {
                        "date": "2023-10-08",
                        "percentage": "28",
                        "count": "819"
                    },
                    {
                        "date": "2023-10-09",
                        "percentage": "37",
                        "count": "1946"
                    },
                    {
                        "date": "2023-10-10",
                        "percentage": "36",
                        "count": "1867"
                    }
                ]
            }
        ]
    }
}
```
---

## Hướng dẫn thực hành Data Retrieval (Python & cURL)

Dưới đây là mã nguồn mẫu minh họa quy trình gọi API thực tế cho phân hệ **Chẩn đoán Catalog**:

### cURL mẫu
```bash
curl -s -X GET "https://business-api.tiktok.com/open_api/v1.3/example/get/?advertiser_id=YOUR_ADVERTISER_ID" \
  -H "Access-Token: YOUR_ACCESS_TOKEN"
```

### Python script mẫu
```python
import requests
import json

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ADVERTISER_ID = "YOUR_ADVERTISER_ID"
BASE_URL = "https://business-api.tiktok.com/open_api/v1.3"

headers = {
    "Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}

def execute_request():
    url = f"{BASE_URL}/example/get/"
    params = {"advertiser_id": ADVERTISER_ID}
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    if data.get("code") == 0:
        print("Truy vấn thành công:", data.get("data"))
        return data.get("data")
    else:
        print(f"Lỗi: {data.get('code')} - {data.get('message')}")
        return None

if __name__ == "__main__":
    execute_request()
```

