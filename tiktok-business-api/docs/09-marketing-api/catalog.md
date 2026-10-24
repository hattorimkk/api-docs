# Hướng dẫn quản lý Catalog

Tài liệu này hướng dẫn toàn diện về quy trình khởi tạo, cấu hình và quản lý danh mục sản phẩm (Catalog) trên nền tảng TikTok Marketing API. Bạn sẽ tìm hiểu cách kết nối nguồn cấp dữ liệu (data feed), tải lên sản phẩm thủ công hoặc qua tệp CSV/JSON, tạo các bộ sản phẩm (product sets), liên kết nguồn sự kiện Pixel/App, chẩn đoán lỗi danh mục và tối ưu hóa quảng cáo mua sắm (Shopping Ads). Các hướng dẫn và bảng ánh xạ chi tiết giúp lập trình viên và nhà quảng cáo dễ dàng đối chiếu giữa giao diện Catalog Manager và các tham số gọi API.

## Quản lý Catalog (`Catalog Management`)
<a id="doc-1739578433846274"></a>
<!-- doc_id: 1739578433846274 -->

> Đường dẫn: Marketing API > Catalog Management

Nếu bạn sở hữu số lượng lớn sản phẩm thay đổi liên tục, bạn nên sử dụng Catalog API để quản lý. Với công cụ này, nhà quảng cáo có thể tạo, cập nhật và xóa nhiều sản phẩm chỉ trong một yêu cầu HTTP duy nhất.

> [!IMPORTANT]
> Khi sử dụng các endpoint của Catalog API, bạn đồng ý với [Điều khoản Danh mục Sản phẩm (Product Catalog Terms)](https://ads.tiktok.com/i18n/official/article?aid=6765817026859499525) và chứng nhận rằng bạn tuân thủ [Chính sách Quảng cáo của TikTok (TikTok Advertising Policies)](https://ads.tiktok.com/help/article?aid=6685586866860720134). Vui lòng xem lại các chính sách này và đảm bảo rằng các mặt hàng bạn tải lên danh mục không vi phạm quy định.

- Để tìm hiểu về các khái niệm và lợi ích của danh mục sản phẩm, xem [Tổng quan (Overview)](catalog.md#doc-1754263078057986).
- Để tìm hiểu cách tạo và quản lý danh mục cũng như một số tình huống sử dụng liên quan, xem [Hướng dẫn quy trình (Guides)](catalog.md#doc-1754263100123137):
  - [Ánh xạ giữa tính năng Catalog Manager và cấu hình API](catalog.md#doc-1782141580104705): Phác thảo bảng đối chiếu giữa các tính năng quản lý danh mục trong giao diện Catalog Manager và cấu hình API tương ứng.
  - [Tạo danh mục và thêm sản phẩm](catalog.md#doc-1754263112945665): Giới thiệu cách tạo danh mục, tải lên sản phẩm, cập nhật sản phẩm, tạo bộ sản phẩm (product set) và liên kết nguồn sự kiện với danh mục.
  - [Xử lý sự cố danh mục bằng tính năng chẩn đoán](catalog.md#doc-1780803490136066): Hướng dẫn chẩn đoán lỗi sản phẩm và nguồn sự kiện, bao gồm Tỷ lệ khớp danh mục (Catalog Match Rate) bằng Catalog Diagnostics.
    - [Ánh xạ giữa tính năng chẩn đoán Catalog Manager và cấu hình API](catalog.md#doc-1780803525320706): Bảng đối chiếu giữa các tính năng chẩn đoán sản phẩm, nguồn sự kiện trong Catalog Manager và các cấu hình API tương ứng.
  - [Lấy thông tin chi tiết về sản phẩm trong danh mục](catalog.md#doc-1805642743426050): Hướng dẫn cách lấy các sản phẩm đang thịnh hành trong danh mục của bạn và danh mục sản phẩm thịnh hành trên TikTok.
    - [Ánh xạ tính năng thông tin chi tiết sản phẩm và cấu hình API](catalog.md#doc-1805642902406145): Bảng đối chiếu giữa các tính năng Product Insights trong Catalog Manager và cấu hình API tương ứng.
  - [Tải lên video danh mục liên kết với sản phẩm](catalog.md#doc-1803654904260674): Hướng dẫn tải lên và quản lý video trong danh mục sản phẩm của bạn.
  - [Quản lý danh mục trong Business Center](catalog.md#doc-1738964064361474): Giới thiệu cách quản lý danh mục dưới dạng tài sản của Business Center, bao gồm di chuyển danh mục sang Business Center và quản lý sau di chuyển.
  - [Sử dụng danh mục khi tạo Quảng cáo Mua sắm (Shopping Ads)](catalog.md#doc-1754263154550786): Hướng dẫn sử dụng danh mục sản phẩm để tạo Shopping Ads.
- Để tra cứu các API khả dụng cho việc quản lý danh mục, xem [Tham chiếu API (API reference)](catalog.md#doc-1739578477445121).

## Tổng quan (`Overview`)
<a id="doc-1754263078057986"></a>
<!-- doc_id: 1754263078057986 -->

> Đường dẫn: Marketing API > Catalog Management > Overview

Danh mục sản phẩm (Catalog) là một tài sản cho phép bạn lưu trữ thông tin về các sản phẩm mà bạn muốn quảng bá trên TikTok. Khi tạo danh mục, bạn có thể tạo các quảng cáo giới thiệu những sản phẩm cụ thể với thông tin luôn được cập nhật mới nhất, chẳng hạn như giá bán, tình trạng còn hàng, kích cỡ và nhiều thông tin khác. Danh mục là yêu cầu bắt buộc trong quy trình thiết lập giải pháp quảng cáo bán lẻ của chúng tôi: [Quảng cáo Mua sắm (Shopping Ads)](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1741942179356738).

> [!IMPORTANT]
> Khi sử dụng các endpoint Catalog API, bạn đồng ý với [Điều khoản Danh mục Sản phẩm (Product Catalog Terms)](https://ads.tiktok.com/i18n/official/article?aid=6765817026859499525) và chứng nhận rằng bạn tuân thủ [Hướng dẫn Quảng cáo của TikTok (TikTok Advertising Guideline)](https://ads.tiktok.com/help/article?aid=6685586866860720134). Vui lòng xem lại các chính sách này và đảm bảo rằng các mặt hàng tải lên không vi phạm.

Việc tạo danh mục mang lại cho bạn khả năng:
- Tải lên trực tiếp các thông tin cốt lõi về sản phẩm, bao gồm tên gọi, mô tả, giá cả, hình ảnh, video và các thuộc tính khác.
- Quản lý sản phẩm bằng cách tạo các bộ sản phẩm (product sets) để tùy biến thông tin và nhóm các sản phẩm theo nhu cầu quảng bá.
- Tải lên video danh mục để sử dụng trong Quảng cáo Mua sắm Video (Video Shopping Ads - VSA) cho Catalog hoặc tự động tạo video tùy chỉnh cho tất cả sản phẩm bằng Mẫu Video (Video Template) của chúng tôi.

## Hướng dẫn quy trình (`Guides`)
<a id="doc-1754263100123137"></a>
<!-- doc_id: 1754263100123137 -->

> Đường dẫn: Marketing API > Catalog Management > Guides

Hướng dẫn này hướng dẫn bạn cách tạo và quản lý danh mục sản phẩm cũng như một số tình huống sử dụng liên quan:
- [Ánh xạ giữa tính năng Catalog Manager và cấu hình API](catalog.md#doc-1782141580104705): Phác thảo sự tương ứng giữa tính năng trên giao diện Catalog Manager và cấu hình API.
- [Tạo danh mục và thêm sản phẩm](catalog.md#doc-1754263112945665): Giới thiệu cách tạo danh mục, tải lên sản phẩm, cập nhật sản phẩm, tạo bộ sản phẩm và liên kết nguồn sự kiện.
- [Xử lý sự cố danh mục bằng tính năng chẩn đoán](catalog.md#doc-1780803490136066): Hướng dẫn chẩn đoán lỗi sản phẩm và nguồn sự kiện bằng Catalog Diagnostics.
  - [Ánh xạ giữa tính năng chẩn đoán Catalog Manager và cấu hình API](catalog.md#doc-1780803525320706): Đối chiếu tính năng chẩn đoán và cấu hình API.
- [Lấy thông tin chi tiết về sản phẩm trong danh mục](catalog.md#doc-1805642743426050): Hướng dẫn nhận thông tin sản phẩm thịnh hành trong danh mục và ngành hàng trên TikTok.
  - [Ánh xạ tính năng thông tin chi tiết sản phẩm và cấu hình API](catalog.md#doc-1805642902406145): Bảng đối chiếu tính năng Product Insights và cấu hình API.
- [Tải lên video danh mục liên kết với sản phẩm](catalog.md#doc-1803654904260674): Hướng dẫn tải lên và quản lý video danh mục.
- [Quản lý danh mục trong Business Center](catalog.md#doc-1738964064361474): Hướng dẫn di chuyển và quản lý danh mục dưới dạng tài sản Business Center.
- [Sử dụng danh mục khi tạo Quảng cáo Mua sắm (Shopping Ads)](catalog.md#doc-1754263154550786): Hướng dẫn tạo Shopping Ads từ danh mục.

## Ánh xạ giữa tính năng Catalog Manager và cấu hình API (`Mapping between Catalog Management features in Catalog Manager and API configurations`)
<a id="doc-1782141580104705"></a>
<!-- doc_id: 1782141580104705 -->

> Đường dẫn: Marketing API > Catalog Management > Guides > Mapping between Catalog Management features in Catalog Manager and API configurations

Bài viết này cung cấp bảng đối chiếu chi tiết giữa các tính năng quản lý danh mục trong giao diện Catalog Manager (thuộc TikTok Ads Manager) và các cấu hình API tương ứng. Nếu bạn đang sử dụng Catalog Manager và muốn tích hợp thông qua TikTok API for Business, hãy tham khảo các bảng dưới đây.

### 1. Quản lý danh mục (Catalogs)

| Phân hệ Catalog Manager | Tính năng Catalog Manager | Tham chiếu UI | Endpoint API | Cấu hình API |
|---|---|---|---|---|
| Trang Product Catalog | Tạo danh mục • Catalog Name | Tên danh mục | [/catalog/create/](../12-api-reference/25-catalog-management.md#doc-1740306481704961) | Tham số yêu cầu: `name` |
| Trang Product Catalog | Tạo danh mục • Tài khoản Business Center | Business Center | [/catalog/create/](../12-api-reference/25-catalog-management.md#doc-1740306481704961) | Tham số yêu cầu: `bc_id` |
| Trang Product Catalog | Tạo danh mục • Industry | Ngành hàng | [/catalog/create/](../12-api-reference/25-catalog-management.md#doc-1740306481704961) | Tham số yêu cầu: `catalog_type` |
| Trang Product Catalog | Tạo danh mục • Default location | Vị trí mặc định | [/catalog/create/](../12-api-reference/25-catalog-management.md#doc-1740306481704961) | Tham số yêu cầu: `region_code` |
| Trang Product Catalog | Tạo danh mục • Default Currency | Tiền tệ mặc định | [/catalog/create/](../12-api-reference/25-catalog-management.md#doc-1740306481704961) | Tham số yêu cầu: `currency` |
| Cài đặt (Settings) | Cập nhật tên danh mục | Catalog Name • Update | [/catalog/update/](../12-api-reference/25-catalog-management.md#doc-1740306544966657) | Cập nhật thông tin danh mục |
| Trang Product Catalog | Xóa danh mục | Catalog • Delete | [/catalog/delete/](../12-api-reference/25-catalog-management.md#doc-1740310064588801) | Xóa danh mục |
| Danh sách danh mục | Xem danh sách danh mục | Catalog List | [/catalog/get/](../12-api-reference/25-catalog-management.md#doc-1740315452868610) | Lấy danh sách danh mục |
| Trang Product Catalog | Chuyển danh mục sang Business Center | Transfer catalog to Business Center | [/catalog/capitalize/](../12-api-reference/25-catalog-management.md#doc-1740490222539778) | Chuyển giao danh mục |

### 2. Quản lý sản phẩm (Products)

| Phân hệ Catalog Manager | Tính năng Catalog Manager | Endpoint API | Cấu hình API |
|---|---|---|---|
| Products | Thêm sản phẩm thủ công • Ảnh chính (Main image) | [/catalog/product/upload/](../12-api-reference/28-catalog-products-p1.md#doc-1740497429681153) | Tham số yêu cầu: `image_url` |
| Products | Thêm sản phẩm thủ công • Video URL (Tùy chọn) | [/catalog/product/upload/](../12-api-reference/28-catalog-products-p1.md#doc-1740497429681153) | Tham số yêu cầu: `video_url` |
| Products | Thêm thủ công • Tiêu đề (Title) | [/catalog/product/upload/](../12-api-reference/28-catalog-products-p1.md#doc-1740497429681153) | Tham số yêu cầu: `title` |
| Products | Thêm thủ công • SKU ID | [/catalog/product/upload/](../12-api-reference/28-catalog-products-p1.md#doc-1740497429681153) | Tham số yêu cầu: `sku_id` |
| Products | Thêm thủ công • Mô tả (Description) | [/catalog/product/upload/](../12-api-reference/28-catalog-products-p1.md#doc-1740497429681153) | Tham số yêu cầu: `description` |
| Products | Thêm thủ công • Thương hiệu (Brand) | [/catalog/product/upload/](../12-api-reference/28-catalog-products-p1.md#doc-1740497429681153) | Tham số yêu cầu: `brand` |
| Products | Thêm thủ công • Liên kết trang đích (Landing Page Link) | [/catalog/product/upload/](../12-api-reference/28-catalog-products-p1.md#doc-1740497429681153) | Tham số yêu cầu: `landing_page_url` |
| Products | Thêm thủ công • Tình trạng (Condition) | [/catalog/product/upload/](../12-api-reference/28-catalog-products-p1.md#doc-1740497429681153) | Tham số yêu cầu: `condition` |
| Products | Thêm thủ công • Tình trạng còn hàng (Availability) | [/catalog/product/upload/](../12-api-reference/28-catalog-products-p1.md#doc-1740497429681153) | Tham số yêu cầu: `availability` |
| Products | Thêm thủ công • Giá (Price) | [/catalog/product/upload/](../12-api-reference/28-catalog-products-p1.md#doc-1740497429681153) | Tham số yêu cầu: `price` |
| Products | Liên kết ứng dụng • Android URL | [/catalog/product/upload/](../12-api-reference/28-catalog-products-p1.md#doc-1740497429681153) | Tham số yêu cầu: `android_url` |
| Products | Liên kết ứng dụng • Android Package ID | [/catalog/product/upload/](../12-api-reference/28-catalog-products-p1.md#doc-1740497429681153) | Tham số yêu cầu: `android_package` |
| Products | Liên kết ứng dụng • Android App Name | [/catalog/product/upload/](../12-api-reference/28-catalog-products-p1.md#doc-1740497429681153) | Tham số yêu cầu: `android_app_name` |
| Products | Liên kết ứng dụng • iOS URL | [/catalog/product/upload/](../12-api-reference/28-catalog-products-p1.md#doc-1740497429681153) | Tham số yêu cầu: `ios_url` |
| Products | Liên kết ứng dụng • iOS App Store ID | [/catalog/product/upload/](../12-api-reference/28-catalog-products-p1.md#doc-1740497429681153) | Tham số yêu cầu: `ios_app_store_id` |
| Products | Liên kết ứng dụng • iOS App Name | [/catalog/product/upload/](../12-api-reference/28-catalog-products-p1.md#doc-1740497429681153) | Tham số yêu cầu: `ios_app_name` |
| Products | Lập lịch Data Feed • Tên nguồn cấp dữ liệu | [/catalog/feed/create/](../12-api-reference/27-catalog-feeds.md#doc-1740665161957377) | Tham số yêu cầu: `feed_name` |
| Products | Lập lịch Data Feed • URL nguồn cấp dữ liệu | [/catalog/feed/create/](../12-api-reference/27-catalog-feeds.md#doc-1740665161957377) | Tham số yêu cầu: `uri` |
| Products | Lập lịch Data Feed • Tên người dùng | [/catalog/feed/create/](../12-api-reference/27-catalog-feeds.md#doc-1740665161957377) | Tham số yêu cầu: `username` |
| Products | Lập lịch Data Feed • Mật khẩu | [/catalog/feed/create/](../12-api-reference/27-catalog-feeds.md#doc-1740665161957377) | Tham số yêu cầu: `password` |
| Products | Lập lịch Data Feed • Tự động tải lên | [/catalog/feed/create/](../12-api-reference/27-catalog-feeds.md#doc-1740665161957377) | Tham số: `interval_type`, `interval_count`, `timezone`, `day_of_month`, `hour`, `minute` |
| Products | Lập lịch Data Feed • Phương thức cập nhật | [/catalog/feed/create/](../12-api-reference/27-catalog-feeds.md#doc-1740665161957377) | Tham số: `update_mode` |
| Products | Lập lịch Data Feed • Cập nhật nguồn cấp hiện có | [/catalog/feed/update/](../12-api-reference/27-catalog-feeds.md#doc-1740665197662210) | Cập nhật Data Feed |
| Product Sources | Danh sách nguồn sản phẩm | [/catalog/feed/get/](../12-api-reference/27-catalog-feeds.md#doc-1740665183073281) | Lấy danh sách Feed |
| Product Sources | Xóa nguồn sản phẩm | [/catalog/feed/delete/](../12-api-reference/27-catalog-feeds.md#doc-1740665210863617) | Xóa Feed |
| Product Sources | Bật/tắt lịch trình Feed | [/catalog/feed/switch/](../12-api-reference/27-catalog-feeds.md#doc-1750349624999937) | Chuyển đổi lịch trình |
| Products | Tải tệp sản phẩm lên | [/catalog/product/file/](../12-api-reference/28-catalog-products-p1.md#doc-1740496787164161) | Tải tệp CSV |
| Products | Chỉnh sửa sản phẩm | [/catalog/product/update/](../12-api-reference/28-catalog-products-p2.md#doc-1740562287852546) | Cập nhật sản phẩm |
| Products | Xóa sản phẩm | [/catalog/product/delete/](../12-api-reference/28-catalog-products-p2.md#doc-1740562489236481) | Xóa sản phẩm |
| Products | Danh sách sản phẩm | [/catalog/product/get/](../12-api-reference/28-catalog-products-p2.md#doc-1740564136678402) | Lấy danh sách sản phẩm |
| Product Sources | Nhật ký tải lên | [/catalog/product/log/](../12-api-reference/28-catalog-products-p3.md#doc-1740570027173889) | Xem trạng thái xử lý feed |

### 3. Bộ sản phẩm (Product sets)

| Phân hệ Catalog Manager | Tính năng Catalog Manager | Endpoint API | Cấu hình API |
|---|---|---|---|
| Product Sets | Tạo bộ sản phẩm • Tên bộ sản phẩm | [/catalog/set/create/](../12-api-reference/29-catalog-product-sets.md#doc-1740572891104257) | Tham số yêu cầu: `product_set_name` |
| Product Sets | Tạo bộ sản phẩm • Quy tắc lọc (Filter rules) | [/catalog/set/create/](../12-api-reference/29-catalog-product-sets.md#doc-1740572891104257) | Tham số yêu cầu: `conditions` |
| Product Sets | Chỉnh sửa bộ sản phẩm | [/catalog/set/update/](../12-api-reference/29-catalog-product-sets.md#doc-1740572974725122) | Cập nhật Product Set |
| Product Sets | Xóa bộ sản phẩm | [/catalog/set/delete/](../12-api-reference/29-catalog-product-sets.md#doc-1740573143966722) | Xóa Product Set |
| Product Sets | Danh sách bộ sản phẩm | [/catalog/set/get/](../12-api-reference/29-catalog-product-sets.md#doc-1740570556295169) | Lấy danh sách Product Sets |
| Product Sets | Danh sách sản phẩm trong bộ sản phẩm | [/catalog/set/product/get/](../12-api-reference/29-catalog-product-sets.md#doc-1740571478441986) | Lấy danh sách sản phẩm thuộc Set |

### 4. Nguồn sự kiện (Event Sources)

| Phân hệ Catalog Manager | Tính năng Catalog Manager | Endpoint API |
|---|---|---|
| Event Sources | Kết nối Nguồn sự kiện App / Pixel | [/catalog/eventsource/bind/](../12-api-reference/26-catalog-event-sources.md#doc-1740492491200513) |
| Event Sources | Ngắt kết nối Nguồn sự kiện App / Pixel | [/catalog/eventsource/unbind/](../12-api-reference/26-catalog-event-sources.md#doc-1740492512449538) |
| Event Sources | Danh sách nguồn sự kiện đã kết nối | [/catalog/eventsource_bind/get/](../12-api-reference/26-catalog-event-sources.md#doc-1740492531343362) |

### 5. Video

| Phân hệ Catalog Manager | Tính năng Catalog Manager | Endpoint API |
|---|---|---|
| Videos | Tải mẫu tùy chỉnh & phông chữ lên | [/catalog/template/upload/](../12-api-reference/31-catalog-video-templates.md#doc-1740665346584577) |
| Videos | Tạo gói video từ mẫu | [/catalog/video_package/create/](../12-api-reference/31-catalog-video-templates.md#doc-1740665273039873) |
| Videos | Đổi tên gói video | [/catalog/video_package/update/](../12-api-reference/31-catalog-video-templates.md#doc-1740665303669761) |
| Videos | Xóa gói video | [/catalog/video_package/delete/](../12-api-reference/31-catalog-video-templates.md#doc-1740665332455426) |
| Videos | Xem trước mẫu video | [/catalog/template_preview/create/](../12-api-reference/31-catalog-video-templates.md#doc-1740665368159233) |
| Videos | Danh sách gói video | [/catalog/video_package/get/](../12-api-reference/31-catalog-video-templates.md#doc-1740574099715073) |

## Tạo danh mục và thêm sản phẩm (`Create catalogs and add products`)
<a id="doc-1754263112945665"></a>
<!-- doc_id: 1754263112945665 -->

> Đường dẫn: Marketing API > Catalog Management > Guides > Create catalogs and add products

Bài viết này hướng dẫn cách tạo danh mục và thêm sản phẩm vào danh mục thông qua Catalog API.

### Tạo danh mục (Create a catalog)

Sử dụng endpoint [/catalog/create/](../12-api-reference/25-catalog-management.md#doc-1740306481704961) để tạo danh mục sản phẩm mới.

### Thêm sản phẩm vào danh mục (Add products to a catalog)

Sau khi tạo danh mục, bạn cần thêm sản phẩm vào đó. Bạn có thể thêm sản phẩm bằng JSON schema, tệp tải lên hoặc luồng dữ liệu (data feed):

- **Thêm sản phẩm qua lược đồ JSON (JSON schema):** Sử dụng endpoint [/catalog/product/upload/](../12-api-reference/28-catalog-products-p1.md#doc-1740497429681153) để tải sản phẩm lên. Endpoint này chủ yếu dùng để tải lên số lượng nhỏ sản phẩm và cập nhật một số trường cụ thể. Hệ thống sẽ tiếp nhận sản phẩm bất đồng bộ và trả về một mã định danh xử lý tác vụ là `feed_log_id`. Với ID này, bạn có thể kiểm tra trạng thái xử lý thông qua endpoint [/catalog/product/log/](../12-api-reference/28-catalog-products-p3.md#doc-1740570027173889). Để tìm hiểu các bước tải sản phẩm lên các loại danh mục khác nhau bằng JSON schema, xem [hướng dẫn tại đây](catalog.md#doc-1766862002851842).

> [!NOTE]
> Hình ảnh sản phẩm phải có kích thước từ 500x500 px trở lên. Nếu không đáp ứng, sản phẩm sẽ không được phê duyệt. Xem chi tiết tại [Yêu cầu hình ảnh sản phẩm](catalog.md#doc-1739578479392770).

- **Thêm sản phẩm qua tệp (File upload):** Sử dụng endpoint [/catalog/product/file/](../12-api-reference/28-catalog-products-p1.md#doc-1740496787164161) để tải sản phẩm lên. Endpoint này chủ yếu phục vụ lần tải lên đầu tiên hoặc tải toàn bộ danh mục sản phẩm. Hiện tại, API chỉ hỗ trợ nguồn cấp dữ liệu tệp dạng CSV. Hệ thống tiếp nhận sản phẩm bất đồng bộ và trả về `feed_log_id` để theo dõi tiến trình qua [/catalog/product/log/](../12-api-reference/28-catalog-products-p3.md#doc-1740570027173889).

> [!NOTE]
> Hình ảnh sản phẩm phải có kích thước từ 500x500 px trở lên. Xem chi tiết tại [Yêu cầu hình ảnh sản phẩm](catalog.md#doc-1739578479392770).

- **Thêm sản phẩm qua nguồn cấp dữ liệu (Data feed):** Sử dụng endpoint [/catalog/feed/create/](../12-api-reference/27-catalog-feeds.md#doc-1740665161957377) để tạo data feed. Nguồn cấp dữ liệu cho phép bạn kết nối danh mục với một URL nguồn cấp, hệ thống sẽ tự động quét định kỳ để lấy thông tin sản phẩm và cập nhật danh mục. Bạn có thể chọn phương thức cập nhật là `OVERWRITE` (ghi đè toàn bộ) hoặc `INCREMENTAL` (cập nhật gia tăng).

### Cập nhật sản phẩm trong danh mục (Update products in a catalog)

Sử dụng endpoint [/catalog/product/update/](../12-api-reference/28-catalog-products-p2.md#doc-1740562287852546) để cập nhật sản phẩm. Phương thức cập nhật gia tăng được hỗ trợ. Hệ thống xử lý bất đồng bộ và trả về `feed_log_id` để kiểm tra qua [/catalog/product/log/](../12-api-reference/28-catalog-products-p3.md#doc-1740570027173889).

### Tạo bộ sản phẩm (Create a product set)

Sử dụng endpoint [/catalog/set/create/](../12-api-reference/29-catalog-product-sets.md#doc-1740572891104257) để tạo bộ sản phẩm. Bộ sản phẩm là tập hợp các sản phẩm cụ thể trong danh mục của bạn, giúp bạn xây dựng các nhóm quảng cáo nhắm mục tiêu vào các sản phẩm được chọn lọc thay vì toàn bộ danh mục.

### Liên kết nguồn sự kiện với danh mục (Bind an event source to a catalog)

Việc liên kết danh mục với nguồn sự kiện ứng dụng (app event source) hoặc Pixel trang web cho phép bạn tiếp thị lại (retargeting) tới những người đã tương tác với sản phẩm trên ứng dụng hoặc trang web của bạn, đồng thời phân phối các sản phẩm phổ biến nhất tới đối tượng phù hợp nhất. Quảng cáo sẽ hiển thị động dựa trên hành vi tương tác thực tế của người dùng.

Sử dụng endpoint [/catalog/eventsource/bind/](../12-api-reference/26-catalog-event-sources.md#doc-1740492491200513) để liên kết nguồn sự kiện với danh mục. Bạn cần chỉ định `app_id` cho sự kiện ứng dụng hoặc `pixel_code` cho sự kiện trang web.


## Tải sản phẩm lên các loại danh mục khác nhau qua lược đồ JSON (`Upload products to different catalog types via JSON schema`)
<a id="doc-1766862002851842"></a>
<!-- doc_id: 1766862002851842 -->

> Đường dẫn: Marketing API > Catalog Management > Guides > Create catalogs and add products > Upload products to different catalog types via JSON schema

Bài viết này hướng dẫn bạn từng bước tải sản phẩm lên các loại danh mục sản phẩm khác nhau bằng cách sử dụng lược đồ JSON (JSON schema).

### Giới thiệu (Introduction)

Danh mục sản phẩm (Catalog) là tài sản cho phép bạn lưu trữ thông tin về các mặt hàng bạn muốn quảng bá trên TikTok. 

**Bằng cách tận dụng Catalog Management API và Catalog Products API, bạn có thể tải lên sản phẩm một cách hiệu quả, nâng cao năng lực vận hành và khả năng mở rộng quy mô.**

### Điều kiện tiên quyết (Prerequisites)

- Bạn đã được cấp quyền truy cập TikTok API for Business. Xem chi tiết tại [Bắt đầu - Quy trình từng bước](../04-get-started/bat-dau.md#doc-1735713609895937).
- Để tải sản phẩm lên danh mục, bạn cần các quyền liên quan. Xem **Tham chiếu API (API Reference)** để biết quyền cần thiết cho từng endpoint và xem [Cập nhật quyền ứng dụng](../04-get-started/bat-dau.md#doc-1738855280338946) để cấu hình quyền.

### Các bước thực hiện (Steps)

#### 1. Tạo danh mục (Create a catalog)

Tạo danh mục bằng endpoint [/catalog/create/](../12-api-reference/25-catalog-management.md#doc-1740306481704961). Chỉ định giá trị `catalog_type` tương ứng với loại danh mục bạn muốn khởi tạo.

> [!NOTE]
> - Danh mục giải trí (Entertainment catalogs) hiện là tính năng chỉ dành cho danh sách cho phép (allowlist-only) và theo diện thư mời do đang trong giai đoạn thử nghiệm Alpha. Vui lòng liên hệ đại diện TikTok nếu muốn đăng ký.
> - Danh mục phim ngắn tập (Mini series catalog) hiện là tính năng chỉ dành cho danh sách cho phép (allowlist-only) và theo diện thư mời do đang trong giai đoạn thử nghiệm.

##### Ví dụ tạo danh mục theo từng loại

###### Tạo danh mục Thương mại điện tử (E-commerce)
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/catalog/create/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "bc_id": "{{bc_id}}",
    "name": "{{name}}",
    "catalog_type": "ECOM",
    "catalog_conf": {
        "region_code": "US",
        "currency": "USD"
    }
}'
```

###### Tạo danh mục Khách sạn (Hotel)
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/catalog/create/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "bc_id": "{{bc_id}}",
    "name": "{{name}}",
    "catalog_type": "HOTEL",
    "catalog_conf": {
        "region_code": "US",
        "currency": "USD"
    }
}'
```

###### Tạo danh mục Chuyến bay (Flight)
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/catalog/create/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "bc_id": "{{bc_id}}",
    "name": "{{name}}",
    "catalog_type": "FLIGHT",
    "catalog_conf": {
        "region_code": "US",
        "currency": "USD"
    }
}'
```

###### Tạo danh mục Điểm đến (Destination)
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/catalog/create/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "bc_id": "{{bc_id}}",
    "name": "{{name}}",
    "catalog_type": "DESTINATION",
    "catalog_conf": {
        "region_code": "US",
        "currency": "USD"
    }
}'
```

###### Tạo danh mục Giải trí (Entertainment)
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/catalog/create/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "bc_id": "{{bc_id}}",
    "name": "{{name}}",
    "catalog_type": "ENTERTAINMENT",
    "catalog_conf": {
        "region_code": "US",
        "currency": "USD"
    }
}'
```

###### Tạo danh mục Kho xe ô tô (Auto-Inventory)
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/catalog/create/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "bc_id": "{{bc_id}}",
    "name": "{{name}}",
    "catalog_type": "AUTO_VEHICLE",
    "catalog_conf": {
        "region_code": "US",
        "currency": "USD"
    }
}'
```

###### Tạo danh mục Mẫu xe ô tô (Auto-Model)
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/catalog/create/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "bc_id": "{{bc_id}}",
    "name": "{{name}}",
    "catalog_type": "AUTO_MODEL",
    "catalog_conf": {
        "region_code": "US",
        "currency": "USD"
    }
}'
```

###### Tạo danh mục Phim ngắn tập (Mini series)
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/catalog/create/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "bc_id": "{{bc_id}}",
    "name": "{{name}}",
    "catalog_type": "MINI_SERIES",
    "catalog_conf": {
        "region_code": "US",
        "currency": "USD"
    }
}'
```

###### Tạo danh mục Chung (Generic)
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/catalog/create/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "bc_id": "{{bc_id}}",
    "name": "{{name}}",
    "catalog_type": "GENERIC",
    "catalog_conf": {
        "region_code": "US",
        "currency": "USD"
    }
}'
```

###### Tạo danh mục Trực tuyến đến ngoại tuyến (Online-to-offline - O2O)
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/catalog/create/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "bc_id": "{{bc_id}}",
    "name": "{{name}}",
    "catalog_type": "ONLINE_TO_OFFLINE",
    "catalog_conf": {
        "region_code": "ID",
        "currency": "IDR"
    }
}'
```

##### Phản hồi tạo danh mục (Response)
```json
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "catalog_id": "{{catalog_id}}"
    }
}
```

#### 2. Tải sản phẩm lên (Upload products)

Tải sản phẩm lên bằng endpoint [/catalog/product/upload/](../12-api-reference/28-catalog-products-p1.md#doc-1740497429681153). Truyền vào `catalog_id` nhận được từ Bước 1 và chỉ định mảng đối tượng `products` dựa trên loại danh mục bạn muốn tải sản phẩm lên.

##### Tải sản phẩm lên danh mục E-commerce
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/catalog/product/upload/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "bc_id": "{{bc_id}}",
    "catalog_id": "{{catalog_id}}",
    "products": [
        {
            "sku_id": "{{sku_id}}",
            "title": "{{title}}",
            "description": "{{description}}",
            "availability": "IN_STOCK",
            "image_url": "{{image_url}}",            
            "brand": "{{brand}}",
            "additional_image_urls": ["{{additional_image_url}}", "{{additional_image_url}}"],
            "item_group_id": "{{item_group_id}}",
            "google_product_category": "{{google_product_category}}",
            "global_trade_item_number": "{{global_trade_item_number}}",
            "manufacturer_part_number": "{{manufacturer_part_number}}",
            "product_detail": {
                "condition": "NEW",
                "age_group": "ADULT",
                "color": "{{color}}",
                "gender": "UNISEX",
                "material": "{{material}}",
                "pattern": "{{pattern}}",
                "product_category": "{{product_category}}",
                "shipping": "US:CA:Ground:9.99 USD",
                "size": "{{size}}",
                "tax": "{{tax}}"
            },
            "price_info": {
                "price": {{price}},
                "currency":"USD",
                "sale_price": {{sale_price}},
                "sale_price_effective_date": "2023-12-11T23:59+00:00/2023-12-15T23:59+00:00"
            },
            "landing_page": {
                "landing_page_url": "{{landing_page_url}}"
            },
            "extra_info": {
                "custom_label_0": "{{custom_label_0}}",
                "custom_label_1": "{{custom_label_1}}",
                "custom_label_2": "{{custom_label_2}}",
                "custom_label_3": "{{custom_label_3}}",
                "custom_label_4": "{{custom_label_4}}"
            }
        }
    ]
}'
```

##### Tải sản phẩm lên danh mục Khách sạn (Hotel)
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/catalog/product/upload/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "bc_id": "{{bc_id}}",
    "catalog_id": "{{catalog_id}}",
    "products": [
        {
            "hotel_id": "{{hotel_id}}",
            "name": "{{name}}",
            "description": "{{description}}",
            "availability": "IN_STOCK",
            "image_url": "{{image_url}}",            
            "brand": "{{brand}}",
            "additional_image_urls": ["{{additional_image_url}}", "{{additional_image_url}}"],
            "hotel_retailer_id": "{{hotel_retailer_id}}",
            "address": {
                "address": "{{address}}",
                "city": "{{city}}",
                "region": "{{region}}",
                "country": "{{country}}"
            },
            "latitude": {{latitude}},
            "longitude": {{longitude}},
            "phone": "{{phone}}",
            "margin_level": {{margin_level}},
            "loyalty_program": "{{loyalty_program}}",
            "cancellation_policy": "{{cancellation_policy}}",
            "guest_ratings": [
                {
                    "rating_system": "{{rating_system}}",
                    "max_score": {{max_score}},
                    "score": {{score}},
                    "number_of_reviewers": {{number_of_reviewers}}
                }
            ],
            "star_rating": {{star_rating}},
            "hotel_room_id": "{{hotel_room_id}}",
            "room_type": "{{room_type}}",
            "meal_policy": "{{meal_policy}}",
            "price_info": {
                "price": {{price}},
                "currency":"USD",
                "sale_price": {{sale_price}},
                "total_price": {{total_price}}
            },
            "landing_page": {
                "landing_page_url": "{{landing_page_url}}"
            },
            "extra_info": {
                "custom_label_0": "{{custom_label_0}}",
                "custom_label_1": "{{custom_label_1}}",
                "custom_label_2": "{{custom_label_2}}",
                "custom_label_3": "{{custom_label_3}}",
                "custom_label_4": "{{custom_label_4}}"
            }
        }
    ]
}'
```

##### Tải sản phẩm lên danh mục Chuyến bay (Flight)
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/catalog/product/upload/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "bc_id": "{{bc_id}}",
    "catalog_id": "{{catalog_id}}",
    "products": [
        {
            "flight_id": "{{flight_id}}",
            "origin_airport": "AAR",
            "destination_airport": "ABD",
            "origin_city": "{{origin_city}}",
            "destination_city": "{{destination_city}}",
            "description": "{{description}}",
            "availability": "IN_STOCK",
            "cabin_class": "{{cabin_class}}",
            "airline_company": "{{airline_company}}",
            "airline_id": "{{airline_id}}",           
            "image_url": "{{image_url}}",            
            "additional_image_urls": ["{{additional_image_url}}", "{{additional_image_url}}"],
            "price_info": {
                "price": {{price}},
                "currency":"USD",
                "sale_price": {{sale_price}},
                "total_price": {{total_price}}
            },
            "landing_page": {
                "landing_page_url": "{{landing_page_url}}"
            },
            "extra_info": {
                "custom_label_0": "{{custom_label_0}}",
                "custom_label_1": "{{custom_label_1}}",
                "custom_label_2": "{{custom_label_2}}",
                "custom_label_3": "{{custom_label_3}}",
                "custom_label_4": "{{custom_label_4}}"
            }
        }
    ]
}'
```

##### Tải sản phẩm lên danh mục Điểm đến (Destination)
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/catalog/product/upload/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "bc_id": "{{bc_id}}",
    "catalog_id": "{{catalog_id}}",
    "products": [
        {
            "destination_id": "{{destination_id}}",
            "destination_name": "{{destination_name}}",
            "description": "{{description}}",
            "image_url": "{{image_url}}",
            "additional_image_urls": [
                "{{additional_image_url}}",
                "{{additional_image_url}}"
            ],    
            "address": {
                "address": "{{address}}",
                "city": "{{city}}",
                "region": "{{region}}",
                "country": "{{country}}"
            },
            "postal_code": "{{postal_code}}",          
            "latitude": {{latitude}},
            "longitude": {{longitude}},
            "types": [
                "{{type}}",
                "{{type}}"
            ],
            "price_info": {
                "price": {{price}},
                "sale_price": {{sale_price}}
            },
            "landing_page": {
                "landing_page_url": "{{landing_page_url}}"
            },
            "extra_info": {
                "custom_label_0": "{{custom_label_0}}",
                "custom_label_1": "{{custom_label_1}}",
                "custom_label_2": "{{custom_label_2}}",
                "custom_label_3": "{{custom_label_3}}",
                "custom_label_4": "{{custom_label_4}}"
            }
        }
    ]
}'
```

##### Tải sản phẩm lên danh mục Giải trí (Entertainment)
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/catalog/product/upload/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "bc_id": "{{bc_id}}",
    "catalog_id": "{{catalog_id}}",
    "products": [
        {  
            "media_title_id": "{{media_title_id}}",
            "title": "{{title}}",
            "description": "{{description}}",
            "availability": "AVAILABLE",
            "image_url": "{{image_url}}",
            "video_url": "{{video_url}}",
            "additional_image_urls": [
                "{{additional_image_url}}", "{{additional_image_url}}"
            ],
            "product_detail": {
                "condition": "USED"
            },
            "star_rating": 5.2,
            "timeline": "COMING_SOON",
            "category": "LIVE_EVENT",
            "genres": [
                "TEEN",
                "SITCOM"
            ],
            "qid": "{{qid}}",
            "price_info": {
                "price": {{price}},
                "currency": "USD"
            },
            "landing_page":{
                "landing_page_url": "{{landing_page_url}}"
            },
            "extra_info": {
                "custom_label_0": "{{custom_label_0}}",
                "custom_label_1": "{{custom_label_1}}",
                "custom_label_2": "{{custom_label_2}}",
                "custom_label_3": "{{custom_label_3}}",
                "custom_label_4": "{{custom_label_4}}"
            }
        }   
    ]
}'
```


##### Tải sản phẩm lên danh mục Kho xe ô tô (Auto-Inventory)
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/catalog/product/upload/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "bc_id": "{{bc_id}}",
    "catalog_id": "{{catalog_id}}",
    "products": [
        {
            "vehicle_id": "{{vehicle_id}}",
            "title": "{{title}}",
            "description": "{{description}}",
            "availability": "AVAILABLE",     
            "image_url": "{{image_url}}",            
            "additional_image_urls": ["{{additional_image_url}}", "{{additional_image_url}}"],
            "product_detail":{"condition":"EXCELLENT"},
            "state_of_vehicle":"USED",
            "vehicle_type":"CAR_TRUCK",
            "make":"{{make}}",
            "model":"{{model}}",
            "trim":"{{trim}}",
            "year":"{{year}}",
            "vin":"{{vin}}",
            "mileage":{"value":"{{value}}","unit":"MILE"},
            "body_style":"CONVERTIBLE",
            "exterior_color":"{{exterior_color}}",
            "interior_color":"{{interior_color}}",
            "transmission":"AUTOMATIC",
            "drivetrain":"4X4",
            "fuel_type":"ELECTRIC",
            "address": {
                "address": "{{address}}",
                "city": "{{city}}",
                "region": "{{region}}",
                "postal_code": "{{postal_code}}"
            },
            "latitude":{{latitude}},
            "longitude":{{longitude}},
            "dealer":{"dealer_id":"{{dealer_id}}","dealer_name":"{{dealer_name}}","dealer_phone":"{{dealer_phone}}","stock_number":"{{stock_number}}"},
            "date_first_on_lot":"{{date_first_on_lot}}",         
            "price_info": {
                "price": {{price}},
                "sale_price":{{sale_price}},
                "sale_price_effective_date":"{{sale_price_effective_date}}"
            },
            "landing_page": {
                "landing_page_url": "{{landing_page_url}}",
                "ios_url": "{{ios_url}}",
                "android_url": "{{android_url}}"
            },
            "extra_info": {
                "custom_label_0": "{{custom_label_0}}",
                "custom_label_1": "{{custom_label_1}}",
                "custom_label_2": "{{custom_label_2}}",
                "custom_label_3": "{{custom_label_3}}",
                "custom_label_4": "{{custom_label_4}}"
            }
        }
    ]
}'
```

##### Tải sản phẩm lên danh mục Mẫu xe ô tô (Auto-Model)
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/catalog/product/upload/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "bc_id": "{{bc_id}}",
    "catalog_id": "{{catalog_id}}",
    "products": [
        {
            "vehicle_id": "{{vehicle_id}}",
            "title": "{{title}}",
            "image_url": "{{image_url}}",
            "make": "{{make}}",
            "model": "{{model}}",
            "trim": "{{trim}}",
            "year": 2025,
            "exterior_color": "{{exterior_color}}",
            "product_detail": {
                "offer_type": "LEASE",
                "term_length": "{{term_length}}",
                "offer_term_qualifier": "years",
                "amount_price": "{{amount_price}}",
                "amount_qualifier": "month",
                "downpayment": "{{downpayment}}",
                "downpayment_qualifier": "due at signing",
                "offer_disclaimer": "{{offer_disclaimer}}",
                "offer_disclaimer_url": "{{offer_disclaimer_url}}",
                "emission_disclaimer": "{{emission_disclaimer}}",
                "emission_disclaimer_url": "{{emission_disclaimer_url}}",
                "emission_overlay_disclaimer": "{{emission_overlay_disclaimer}}",
                "emission_image_link": "{{emission_image_link}}"
            },
            "landing_page": {
                "landing_page_url": "{{landing_page_url}}"
            }
        }
    ]
}'
```

##### Tải sản phẩm lên danh mục Phim ngắn tập (Mini series)
```http
// curl
curl --location  --request POST 'https://business-api.tiktok.com/open_api/v1.3/catalog/product/upload/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "bc_id": "{{bc_id}}",
    "catalog_id": "{{catalog_id}}",
    "products": [
        {
            "series_id": "{{series_id}}",
            "series_name": "{{series_name}}",
            "image_url": "{{image_url}}",
            "recharge": [
                {
                    "type": "BY_TIERS",
                    "purchase_unit": ["TIER_1", "TIER_2", "TIER_3", "TIER_4", "TIER_5"],
                    "cost": ["{{cost}}", "{{cost}}", "{{cost}}"]
                },
                {
                    "type": "BY_EPISODES",
                    "purchase_unit": ["1", "10", "60"],
                    "cost": ["{{cost}}", "{{cost}}", "{{cost}}"]
                },
                {
                    "type": "SUBSCRIPTION",
                    "purchase_unit": ["WEEKLY", "MONTHLY", "QUARTERLY", "YEARLY"],
                    "cost": ["{{cost}}", "{{cost}}", "{{cost}}", "{{cost}}"]
                }
            ],
            "product_detail": {
                "company_type": "COPYRIGHT_HOLDER",
                "copyright_holder_name": "{{copyright_holder_name}}",
                "app_id": "{{app_id}}",
                "minis_id": "{{minis_id}}",
                "total_episodes": 60,
                "initial_paid_episodes": 10,
                "per_episode_duration": 3,
                "spoken_language": "zh",
                "subtitle_language": "en",
                "production_type": "TRANSLATION",
                "target_audience": "FEMALE",
                "characters": ["ALPHA_MALE", "EXTRAORDINARY_TALENT"],
                "genres": ["LOVE_IN_WEALTHY_FAMILIES", "INDULGENT_LOVE", "LOVE_AFTER_MARRIAGE"],
                "historical_context": ["ANCIENT_SETTING", "SECOND_CHANCE", "FICTIONAL"],
                "actors": ["{{actor}}", "{{actor}}", "{{actor}}"]
            }
        }
    ]
}'
```

##### Tải sản phẩm lên danh mục Chung (Generic)
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/catalog/product/upload/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "bc_id": "{{bc_id}}",
    "catalog_id": "{{catalog_id}}",
    "products": [
        {
            "item_id": "{{item_id}}",
            "title": "{{title}}",
            "description": "{{description}}",
            "availability": "IN_STOCK",
            "image_url": "{{image_url}}",
            "video_url": "{{video_url}}",
            "additional_image_urls": [
                "{{additional_image_url}}",
                "{{additional_image_url}}"
            ],
            "address": {
                "street": "1143 Coleman Avenue",
                "city": "San Jose",
                "region": "California",
                "postal_code": "95050"
            },
            "longitude": -121.8863,
            "latitude": 37.3382,
            "product_detail": {
                "rating": 4.8,
                "availability_type": "REGION",
                "availability_region": [
                    [
                        "Arizona",
                        "Peoria"
                    ],
                    [
                        "Alabama",
                        "Birmingham"
                    ]
                ],
                "custom_number_0": 4.8,
                "custom_number_1": 5,
                "custom_number_2": 30,
                "custom_number_3": 9.99,
                "custom_number_4": 250
            },
            "price_info": {
                "price": 129.99,
                "sale_price": 99.99
            },
            "landing_page": {
                "landing_page_url": "{{landing_page_url}}",
                "ios_url": "{{ios_url}}",
                "ios_app_store_id": "{{ios_app_store_id}}",
                "ios_app_name": "{{ios_app_name}}",
                "android_url": "{{android_url}}",
                "android_package": "{{android_package}}",
                "android_app_name": "{{android_app_name}}"
            },
            "extra_info": {
                "custom_label_0": "{{custom_label_0}}",
                "custom_label_1": "{{custom_label_1}}",
                "custom_label_2": "{{custom_label_2}}",
                "custom_label_3": "{{custom_label_3}}",
                "custom_label_4": "{{custom_label_4}}"
            }
        }
    ]
}'
```

##### Tải sản phẩm lên danh mục Trực tuyến đến ngoại tuyến (Online-to-offline - O2O)
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/catalog/product/upload/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "bc_id": "{{bc_id}}",
    "catalog_id": "{{catalog_id}}",
    "products": [
        {
            "listing_id": "{{listing_id}}",
            "title": "{{title}}",
            "description": "{{description}}",
            "availability": "IN_STOCK",
            "image_url": "{{image_url}}",
            "brand": "{{brand}}",
            "google_product_category": "{{google_product_category}}",
            "item_group_id": "{{item_group_id}}",
            "additional_image_urls": [
                "{{additional_image_url}}"
            ],
            "global_trade_item_number": "{{global_trade_item_number}}",
            "address": {
                "street": "{{street}}",
                "city": "{{city}}",
                "region": "{{region}}",
                "postal_code": "{{postal_code}}"
            },
            "longitude": {{longitude}},
            "latitude": {{latitude}},
            "product_detail": {
                "product_category": "{{product_category}}",
                "rating": 4.8,
                "condition": "NEW",
                "color": "{{color}}",
                "size": "{{size}}",
                "material": "{{material}}",
                "pattern": "{{patternl}}",
                "tax": "{{tax}}",
                "age_group": "ADULT",
                "gender": "UNISEX",
                "availability_circle_radius": "5",
                "availability_circle_radius_unit": "KM",
                "custom_number_0": 4.8,
                "custom_number_1": 5,
                "custom_number_2": 30,
                "custom_number_3": 9.99,
                "custom_number_4": 250
            },
            "price_info": {
                "price": {{price}},
                "sale_price": {{sale_price}},
                "sale_price_effective_date": "{{sale_price_effective_date}}"
            },
            "landing_page": {
                "landing_page_url": "{{landing_page_url}}",
                "ios_url": "{{ios_url}}",
                "ios_app_store_id": "{{ios_app_store_id}}",
                "ios_app_name": "{{ios_app_name}}",
                "android_url": "{{android_url}}",
                "android_package": "{{android_package}}",
                "android_app_name": "{{android_app_name}}"
            },
            "extra_info": {
                "custom_label_0": "{{custom_label_0}}",
                "custom_label_1": "{{custom_label_1}}",
                "custom_label_2": "{{custom_label_2}}",
                "custom_label_3": "{{custom_label_3}}",
                "custom_label_4": "{{custom_label_4}}"
            }
        }
    ]
}'
```

##### Phản hồi tải sản phẩm (Response)
```json
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "feed_log_id": "{{feed_log_id}}"
    }
}
```

#### 3. Kiểm tra kết quả xử lý sản phẩm (Check the product handling results)

Kiểm tra kết quả xử lý sản phẩm bằng endpoint [/catalog/product/log/](../12-api-reference/28-catalog-products-p3.md#doc-1740570027173889). Truyền vào `feed_log_id` nhận được từ Bước 2. Nếu trường `error_affected_products` trong phản hồi không phải là null, hãy xem xét kỹ chi tiết lỗi phát sinh và quay lại Bước 2 để tải lại sản phẩm đã được sửa đổi.

##### Yêu cầu (Request)
```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/catalog/product/log/?bc_id={{bc_id}}&catalog_id={{catalog_id}}&feed_log_id={{feed_log_id}}' \
--header 'Access-Token: {{Access-Token}}'
```

##### Phản hồi khi xử lý có cảnh báo/lỗi (Unsuccessful product handling results)
```json
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "product_feed_log": {
            "warn_count": 1,
            "feed_id": "{{feed_id}}",
            "error_count": 0,
            "update_count": 0,
            "process_status": "SUCCESS",
            "delete_count": 0,
            "add_count": 1,
            "end_time": "2023-05-22 07:53:08",
            "start_time": "2023-05-22 07:53:07",
            "update_mode": "INCREASE",
            "feed_log_data": {
                "warn_affected_products": [
                    {
                        "field": "shipping",
                        "suggestion": "The \"shipping\" field is using an invalid value. Please follow the format: US:CA:Ground:9.99 USD",
                        "affected_product_count": 1,
                        "affected_product_item_list": [
                            {
                                "title": "{{title}}",
                                "product_url": "{{product_url}}",
                                "sku_id": "{{sku_id}}",
                                "value": "US: CA: Ground: 9.99 USD: Standard",
                                "index": 2,
                                "description": "{{description}}"
                            }
                        ],
                        "issue": "Invalid value: shipping"
                    },
                    {
                        "field": "sale_price_effective_date",
                        "suggestion": "The \"sales_price_effective_date\" field is using an invalid value. Please follow the format: YYYY-MM-DDT23:59+00:00/YYYY-MM-DDT23:59+00:00",
                        "affected_product_count": 1,
                        "affected_product_item_list": [
                            {
                                "title": "{{title}}",
                                "product_url": "{{product_url}}",
                                "sku_id": "{{sku_id}}",
                                "value": "2017-12-01T0: 00/2017-12-31T0: 00",
                                "index": 2,
                                "description": "{{description}}"
                            }
                        ],
                        "issue": "Invalid value: sale_price_effective_date"
                    }
                ],
                "error_affected_products": null,
                "download_path": {
                    "id": "{{download_path}}",
                    "zh-CN": "{{download_path}}",
                    "vi": "{{download_path}}",
                    "hi-IN": "{{download_path}}",
                    "it": "{{download_path}}",
                    "fr": "{{download_path}}",
                    "en": "{{download_path}}",
                    "ms": "{{download_path}}",
                    "tr": "{{download_path}}",
                    "es": "{{download_path}}",
                    "ja-JP": "{{download_path}}",
                    "ko": "{{download_path}}",
                    "th": "{{download_path}}",
                    "de": "{{download_path}}"
                }
            },
            "catalog_id": "{{catalog_id}}"
        }
    }
}
```

##### Phản hồi khi xử lý thành công hoàn toàn (Successful product handling results)
```json
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "product_feed_log": {
            "warn_count": 0,
            "delete_count": 0,
            "end_time": "2023-05-22 07:58:05",
            "catalog_id": "{{catalog_id}}",
            "feed_log_data": {
                "warn_affected_products": null,
                "error_affected_products": null,
                "download_path": {}
            },
            "feed_id": "{{feed_id}}",
            "add_count": 0,
            "update_count": 1,
            "update_mode": "INCREASE",
            "error_count": 0,
            "process_status": "SUCCESS",
            "start_time": "2023-05-22 07:58:05"
        }
    }
}
```

### Tài liệu liên quan (Related docs)

- [Catalog Management API](../12-api-reference/25-catalog-management.md#doc-1740132866693122)
- [Catalog Products API](../12-api-reference/28-catalog-products-p1.md#doc-1740132940622850)
- [Catalog Product Sets API](../12-api-reference/29-catalog-product-sets.md#doc-1740132953884673)
- [Tạo Quảng cáo Mua sắm Video với sản phẩm từ danh mục](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1750361698613249)
- [Tạo Quảng cáo Ô tô cho Kho xe (Automotive Ads for Inventory)](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1827752507854850)
- [Tạo Quảng cáo Ô tô cho Mẫu xe (Automotive Ads for Models)](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1829635758164994)

## Yêu cầu hình ảnh sản phẩm (`Product image requirements`)
<a id="doc-1739578479392770"></a>
<!-- doc_id: 1739578479392770 -->

> Đường dẫn: Marketing API > Catalog Management > Guides > Create catalogs and add products > Product image requirements

Khi bạn tải lên hoặc cập nhật sản phẩm, hình ảnh sản phẩm phải có kích thước bằng hoặc lớn hơn 500x500 px. Nếu không, hình ảnh sẽ bị lọc bỏ và sản phẩm sẽ không được phê duyệt.

Sử dụng endpoint [/catalog/product/get/](../12-api-reference/28-catalog-products-p2.md#doc-1740564136678402) để kiểm tra xem hình ảnh của sản phẩm có bị lọc bỏ hay không. Trong phản hồi, hãy kiểm tra giá trị của trường `image_status`.

Các giá trị enum cho trường `image_status` bao gồm:
* `PROCESSING`: Hình ảnh đang được lưu trữ.
* `SUCCESS`: Hình ảnh đã được lưu trữ thành công.
* `FAIL`: Lưu trữ hình ảnh không thành công.
* `FILTERED`: Hình ảnh đã được lưu trữ nhưng không thể sử dụng do không đáp ứng yêu cầu kích thước (phải từ 500 px trở lên).
* `NOT_SUPPORTED`: Định dạng hình ảnh không được hỗ trợ.
* `NOT_FOUND`: Không tìm thấy tài nguyên qua URL. Vui lòng đảm bảo URL hợp lệ và tệp có thể truy cập công khai.

Đối với hình ảnh không đáp ứng yêu cầu kích thước (`image_status` là `FILTERED`), trạng thái kiểm duyệt sản phẩm (`audit_status`) sẽ giữ ở mức `processing`. Bạn có thể tìm thấy hướng dẫn hành động trong trường `suggestion`. Ví dụ:

```json
"audit": {
    "audit_status": "processing",
    "suggestion": "Please upload an image that is at least 500*500 pixels."
},
"image_status": "FILTERED"
```

Trong trường hợp này, bạn cần tải hình ảnh đạt chuẩn lên máy chủ của mình và gọi lại cùng endpoint đó để tải lên hoặc cập nhật lại sản phẩm. Hãy nhớ thay thế liên kết cũ bằng liên kết dẫn đến hình ảnh đạt chuẩn mới.

Đối với hình ảnh lưu trữ không thành công (`image_status` là `FAIL`), trạng thái kiểm duyệt của sản phẩm cũng sẽ ở mức `processing` và trường `suggestion` tương ứng sẽ được cung cấp. Ví dụ:

```json
"audit": {
    "audit_status": "processing",
    "suggestion": "Retrieving image failed. Please upload the image again."
},
"image_status": "FAIL"
```


## Toán tử và trường của bộ sản phẩm (`Product set operators and fields`)
<a id="doc-1740673108747265"></a>
<!-- doc_id: 1740673108747265 -->

> Đường dẫn: Marketing API > Catalog Management > Guides > Create catalogs and add products > Product set operators and fields

Bài viết này liệt kê các toán tử và trường bộ lọc mà bạn có thể truyền tương ứng vào tham số `operation` và `field` khi gọi endpoint [/catalog/set/create/](../12-api-reference/29-catalog-product-sets.md#doc-1740572891104257) hoặc [/catalog/set/update/](../12-api-reference/29-catalog-product-sets.md#doc-1740572974725122).

### Toán tử (Operators)

| Operator | Definition | Details |
|---|---|---|
| EQUAL | Bằng với (Equal to) | Chỉ có thể sử dụng với một giá trị duy nhất (string, int/long, float). |
| NOT_EQUAL | Không bằng với (Not equal to) | Chỉ có thể sử dụng với một giá trị duy nhất (string, int/long, float). |
| GT | Lớn hơn (Greater than) | Chỉ có thể sử dụng với một giá trị duy nhất (string, int/long, float). |
| LT | Nhỏ hơn (Less than) | Chỉ có thể sử dụng với một giá trị duy nhất (string, int/long, float). |
| GTE | Lớn hơn hoặc bằng (Greater than or equal) | Chỉ có thể sử dụng với một giá trị duy nhất (string, int/long, float). |
| LTE | Nhỏ hơn hoặc bằng (Less than or equal) | Chỉ có thể sử dụng với một giá trị duy nhất (string, int/long, float). |
| CONTAIN | Chứa một giá trị trong danh sách (phân biệt hoa thường) | Có thể sử dụng với nhiều giá trị trong một danh sách. |
| I_CONTAIN | Chứa một giá trị trong danh sách (không phân biệt hoa thường) | Có thể sử dụng với nhiều giá trị trong một danh sách. |
| EXCLUDE | Không bằng bất kỳ giá trị nào trong danh sách (phân biệt hoa thường) | Có thể sử dụng với nhiều giá trị trong một danh sách. |
| I_EXCLUDE | Không bằng bất kỳ giá trị nào trong danh sách (không phân biệt hoa thường) | Có thể sử dụng với nhiều giá trị trong một danh sách. |
| WILDCARD | Chứa chuỗi con (phân biệt hoa thường) | Bạn có thể chỉ định một giá trị hoặc nhiều giá trị. Khi chỉ định nhiều giá trị, bộ lọc sẽ tìm các chuỗi chứa bất kỳ giá trị nào trong danh sách. |
| I_WILDCARD | Chứa chuỗi con (không phân biệt hoa thường) | Bạn có thể chỉ định một giá trị hoặc nhiều giá trị. Khi chỉ định nhiều giá trị, bộ lọc tìm chuỗi chứa bất kỳ giá trị nào trong danh sách. |
| NOT_WILDCARD | Không chứa bất kỳ chuỗi con nào (phân biệt hoa thường) | Bạn có thể chỉ định một giá trị hoặc nhiều giá trị. Khi chỉ định nhiều giá trị, bộ lọc tìm chuỗi không chứa bất kỳ giá trị nào trong danh sách. |
| I_NOT_WILDCARD | Không chứa bất kỳ chuỗi con nào (không phân biệt hoa thường) | Bạn có thể chỉ định một hoặc nhiều giá trị. |
| PREFIX | Bắt đầu bằng một giá trị tiền tố (phân biệt hoa thường) | Bạn có thể chỉ định một giá trị hoặc nhiều giá trị. |
| I_PREFIX | Bắt đầu bằng một giá trị tiền tố (không phân biệt hoa thường) | Bạn có thể chỉ định một giá trị hoặc nhiều giá trị. |

### Các trường bộ lọc (Filter fields)

#### Cho bộ sản phẩm danh mục E-commerce (For E-commerce catalog product sets)

| Field | Description | Supported operators | Additional information |
|---|---|---|---|
| title | Tiêu đề sản phẩm. Có thể bao gồm các từ như "đang giảm giá". | EQUAL <br> NOT_EQUAL <br> WILDCARD <br> I_WILDCARD <br> NOT_WILDCARD <br> I_NOT_WILDCARD <br> PREFIX <br> I_PREFIX | |
| description | Mô tả sản phẩm. | EQUAL <br> NOT_EQUAL <br> WILDCARD <br> I_WILDCARD <br> NOT_WILDCARD <br> I_NOT_WILDCARD <br> PREFIX <br> I_PREFIX | |
| availability | Trạng thái tồn kho sản phẩm. | EQUAL <br> NOT_EQUAL | Giá trị hỗ trợ: • `IN_STOCK` • `AVAILABLE_FOR_ORDER` • `PREORDER` • `OUT_OF_STOCK` • `DISCONTINUED` |
| brand | Thương hiệu sản phẩm. | CONTAIN <br> I_CONTAIN <br> EXCLUDE <br> I_EXCLUDE <br> WILDCARD <br> I_WILDCARD <br> NOT_WILDCARD <br> I_NOT_WILDCARD <br> PREFIX <br> I_PREFIX <br> NOT_EQUAL | |
| item_group_id | ID SPU của sản phẩm. | CONTAIN <br> I_CONTAIN <br> EXCLUDE <br> I_EXCLUDE <br> WILDCARD <br> I_WILDCARD <br> NOT_WILDCARD <br> I_NOT_WILDCARD <br> PREFIX <br> I_PREFIX | Ví dụ: `tiktok_1234_shirts` |
| google_product_category | Danh mục sản phẩm theo Google taxonomy. | CONTAIN <br> I_CONTAIN <br> EXCLUDE <br> I_EXCLUDE <br> WILDCARD <br> I_WILDCARD <br> NOT_WILDCARD <br> I_NOT_WILDCARD <br> PREFIX <br> I_PREFIX | Ví dụ: `Apparel & Accessories > Clothing > Shirts` |
| condition | Tình trạng sản phẩm trong cửa hàng. | EQUAL <br> NOT_EQUAL | Giá trị hỗ trợ: • `NEW` • `REFURBISHED` • `USED` |
| age_group | Nhóm tuổi đối tượng mục tiêu. | EQUAL <br> NOT_EQUAL | Giá trị hỗ trợ: • `NEW_BORN` • `INFANT` • `TODDLER` • `KIDS` • `ADULT` |
| color | Màu sắc sản phẩm. | EQUAL <br> NOT_EQUAL <br> WILDCARD <br> I_WILDCARD <br> NOT_WILDCARD <br> I_NOT_WILDCARD <br> PREFIX <br> I_PREFIX | |
| gender | Giới tính mục tiêu của sản phẩm. | EQUAL <br> NOT_EQUAL | Giá trị hỗ trợ: • `MALE` • `FEMALE` • `UNISEX` |
| material | Chất liệu cấu thành sản phẩm. | EQUAL <br> NOT_EQUAL <br> WILDCARD <br> I_WILDCARD <br> NOT_WILDCARD <br> I_NOT_WILDCARD <br> PREFIX <br> I_PREFIX | |
| pattern | Hoa văn hoặc họa tiết trên sản phẩm. | EQUAL <br> NOT_EQUAL <br> WILDCARD <br> I_WILDCARD <br> NOT_WILDCARD <br> I_NOT_WILDCARD <br> PREFIX <br> I_PREFIX | |
| product_type | Loại sản phẩm (chỉ cần 3 cấp đầu tiên). | CONTAIN <br> I_CONTAIN <br> EXCLUDE <br> I_EXCLUDE <br> WILDCARD <br> I_WILDCARD <br> NOT_WILDCARD <br> I_NOT_WILDCARD <br> PREFIX <br> I_PREFIX | Ví dụ: `Apparel & Accessories > Clothing > Shirts` |
| size | Kích thước sản phẩm. | EQUAL <br> NOT_EQUAL <br> WILDCARD <br> I_WILDCARD <br> NOT_WILDCARD <br> I_NOT_WILDCARD <br> PREFIX <br> I_PREFIX | Ví dụ: `small`, `L`, `XL` |
| price | Giá gốc của sản phẩm. | GT <br> GTE <br> LT <br> LTE <br> EQUAL | |
| sale_price | Giá khuyến mãi của sản phẩm. | GT <br> GTE <br> LT <br> LTE <br> EQUAL | |
| sale_price_effective_start_date | Thời điểm bắt đầu chương trình giảm giá. | GT <br> GTE <br> LT <br> LTE <br> EQUAL | Định dạng: `2017-12-31T0:00` |
| sale_price_effective_end_date | Thời điểm kết thúc chương trình giảm giá. | GT <br> GTE <br> LT <br> LTE <br> EQUAL | Định dạng: `2017-12-31T0:00` |
| custom_label_0 <br> custom_label_1 <br> custom_label_2 <br> custom_label_3 <br> custom_label_4 | Nhãn tùy chỉnh để lọc sản phẩm. | CONTAIN <br> I_CONTAIN <br> EXCLUDE <br> I_EXCLUDE <br> WILDCARD <br> I_WILDCARD <br> NOT_WILDCARD <br> I_NOT_WILDCARD <br> PREFIX <br> I_PREFIX <br> NOT_EQUAL | |

#### Cho bộ sản phẩm danh mục khách sạn (For hotel catalog product sets)

| Field | Description | Supported operators | Additional information |
|---|---|---|---|
| hotel_id | ID duy nhất cho khách sạn. | CONTAIN <br> I_CONTAIN <br> NOT_EQUAL <br> WILDCARD <br> I_WILDCARD <br> NOT_WILDCARD <br> I_NOT_WILDCARD <br> PREFIX <br> I_PREFIX | |
| availability | Tình trạng phòng còn trống của khách sạn. | EQUAL <br> NOT_EQUAL | Giá trị hỗ trợ: • `IN_STOCK`: Có sẵn để đặt phòng • `OUT_OF_STOCK`: Hết phòng |
| hotel_category | Hạng mục khách sạn. | EQUAL <br> NOT_EQUAL | Giá trị hỗ trợ: • `HOTEL` • `APARTMENT` • `BOAT` • `CAMPSITE` • `CAPSULE_HOTEL` • `GUESTHOUSE` • `HOMESTAY` • `HOSTEL` • `LUXURY_TENT` • `RESORT` • `VILLA` |
| brand | Tên thương hiệu khách sạn. | NOT_EQUAL <br> CONTAIN | |
| star_rating | Xếp hạng sao của khách sạn. | GT <br> GTE <br> LT <br> LTE <br> EQUAL | |
| price | Giá cơ bản của phòng khách sạn. | GT <br> GTE <br> LT <br> LTE <br> EQUAL | |
| sale_price | Giá khuyến mãi của phòng khách sạn. | GT <br> GTE <br> LT <br> LTE <br> EQUAL | |
| margin_level | Mức lợi nhuận của khách sạn. | GT <br> GTE <br> LT <br> LTE <br> EQUAL | |
| guest_rating_score | Điểm đánh giá của khách hàng. | GT <br> GTE <br> LT <br> LTE <br> EQUAL | |
| guest_rating_number_of_reviewers | Số lượng người đánh giá khách sạn. | GT <br> GTE <br> LT <br> LTE <br> EQUAL | |
| city | Thành phố nơi khách sạn tọa lạc. | CONTAIN <br> I_CONTAIN <br> NOT_EQUAL <br> WILDCARD <br> I_WILDCARD <br> NOT_WILDCARD <br> I_NOT_WILDCARD <br> PREFIX <br> I_PREFIX | |
| region | Khu vực (tiểu bang/tỉnh) nơi khách sạn tọa lạc. | NOT_EQUAL <br> CONTAIN | |
| custom_label_0 <br> custom_label_1 <br> custom_label_2 <br> custom_label_3 <br> custom_label_4 | Thông tin nhãn tùy chỉnh bổ sung. | CONTAIN <br> I_CONTAIN <br> NOT_EQUAL <br> EXCLUDE <br> I_EXCLUDE <br> WILDCARD <br> I_WILDCARD <br> NOT_WILDCARD <br> I_NOT_WILDCARD <br> PREFIX <br> I_PREFIX | |

#### Cho bộ sản phẩm danh mục chuyến bay (For flight catalog product sets)

| Field | Description | Supported operators | Additional information |
|---|---|---|---|
| availability | Tình trạng chuyến bay còn chỗ. | EQUAL <br> NOT_EQUAL | Giá trị hỗ trợ: • `IN_STOCK`: Còn chỗ đặt • `OUT_OF_STOCK`: Hết chỗ |
| origin_airport | Sân bay khởi hành (mã IATA 3 chữ cái). | CONTAIN <br> I_CONTAIN <br> NOT_EQUAL <br> WILDCARD <br> I_WILDCARD <br> NOT_WILDCARD <br> I_NOT_WILDCARD <br> PREFIX <br> I_PREFIX | Ví dụ: `AAR` |
| destination_airport | Sân bay điểm đến (mã IATA 3 chữ cái). | CONTAIN <br> I_CONTAIN <br> NOT_EQUAL <br> WILDCARD <br> I_WILDCARD <br> NOT_WILDCARD <br> I_NOT_WILDCARD <br> PREFIX <br> I_PREFIX | Ví dụ: `ABD` |
| origin_city | Thành phố khởi hành. | CONTAIN <br> I_CONTAIN <br> NOT_EQUAL <br> WILDCARD <br> I_WILDCARD <br> NOT_WILDCARD <br> I_NOT_WILDCARD <br> PREFIX <br> I_PREFIX | |
| destination_city | Thành phố điểm đến. | CONTAIN <br> I_CONTAIN <br> NOT_EQUAL <br> WILDCARD <br> I_WILDCARD <br> NOT_WILDCARD <br> I_NOT_WILDCARD <br> PREFIX <br> I_PREFIX | |
| airline_company | Tên hãng hàng không khai thác. | CONTAIN <br> I_CONTAIN <br> NOT_EQUAL <br> WILDCARD <br> I_WILDCARD <br> NOT_WILDCARD <br> I_NOT_WILDCARD <br> PREFIX <br> I_PREFIX | |
| price | Giá vé cơ bản cho chuyến bay. | GT <br> GTE <br> LT <br> LTE <br> EQUAL | |
| custom_label_0 <br> custom_label_1 <br> custom_label_2 <br> custom_label_3 <br> custom_label_4 | Nhãn tùy chỉnh bổ sung. | CONTAIN <br> I_CONTAIN <br> NOT_EQUAL <br> EXCLUDE <br> I_EXCLUDE <br> WILDCARD <br> I_WILDCARD <br> NOT_WILDCARD <br> I_NOT_WILDCARD <br> PREFIX <br> I_PREFIX | |

#### Cho bộ sản phẩm danh mục điểm đến (For destination catalog product sets)

| Field | Description | Supported operators | Additional information |
|---|---|---|---|
| destination_id | ID duy nhất cho điểm đến. | CONTAIN <br> I_CONTAIN <br> EQUAL <br> NOT_EQUAL <br> PREFIX <br> I_PREFIX | |
| city | Thành phố nơi có điểm đến. | CONTAIN <br> I_CONTAIN <br> NOT_EQUAL <br> WILDCARD <br> I_WILDCARD <br> NOT_WILDCARD <br> I_NOT_WILDCARD <br> PREFIX <br> I_PREFIX | |
| region | Khu vực (tiểu bang/tỉnh) của điểm đến. | NOT_EQUAL <br> CONTAIN | |
| price | Giá trung bình hoặc thấp nhất của điểm đến. | GT <br> GTE <br> LT <br> LTE <br> EQUAL | |
| custom_label_0 <br> custom_label_1 <br> custom_label_2 <br> custom_label_3 <br> custom_label_4 | Nhãn tùy chỉnh bổ sung. | CONTAIN <br> I_CONTAIN <br> NOT_EQUAL <br> EXCLUDE <br> I_EXCLUDE <br> WILDCARD <br> I_WILDCARD <br> NOT_WILDCARD <br> I_NOT_WILDCARD <br> PREFIX <br> I_PREFIX | |

#### Cho bộ sản phẩm danh mục giải trí (For entertainment catalog product sets)

| Field | Description | Supported operators | Additional information |
|---|---|---|---|
| title | Tên của tiêu đề phương tiện truyền thông. | EQUAL <br> NOT_EQUAL <br> WILDCARD <br> I_WILDCARD <br> NOT_WILDCARD <br> I_NOT_WILDCARD <br> PREFIX <br> I_PREFIX | |
| availability | Tình trạng khả dụng của sản phẩm media. | EQUAL <br> NOT_EQUAL | Giá trị: • `AVAILABLE` • `SUBSCRIBERS_ONLY` • `ON_DEMAND` • `NOT_AVAILABLE` |
| condition | Tình trạng sản phẩm media. | EQUAL <br> NOT_EQUAL | Giá trị: • `NEW` • `USED` |
| timeline | Tiến trình phát hành. | EQUAL <br> NOT_EQUAL | Giá trị: • `COMING_SOON` • `ONLINE` • `EXPIRE_SOON` |
| category | Thể loại phát hành media. | EQUAL <br> NOT_EQUAL | Giá trị: • `MOVIE` • `MUSIC` • `TV_SHOW` • `TV_SERIES` • `SPORTS_GAME` • `LIVE_EVENT` |
| genres | Thể loại nội dung media. | CONTAIN <br> I_CONTAIN <br> EXCLUDE <br> I_EXCLUDE <br> WILDCARD <br> I_WILDCARD <br> NOT_WILDCARD <br> I_NOT_WILDCARD <br> PREFIX <br> I_PREFIX | Xem bảng danh sách các giá trị của `genres` bên dưới. |
| price | Giá của sản phẩm media. | GT <br> GTE <br> LT <br> LTE <br> EQUAL | |
| custom_label_0 <br> custom_label_1 <br> custom_label_2 <br> custom_label_3 <br> custom_label_4 | Nhãn tùy chỉnh bổ sung. | CONTAIN <br> I_CONTAIN <br> EXCLUDE <br> I_EXCLUDE <br> WILDCARD <br> I_WILDCARD <br> NOT_WILDCARD <br> I_NOT_WILDCARD <br> PREFIX <br> I_PREFIX | |

##### Danh sách các giá trị thể loại (`genres`)

`ACTION`, `ADULT_ANIMATION`, `ADVENTURE`, `ANIMATION`, `BIOGRAPHICAL`, `BLACK_COMEDY`, `BUDDY`, `COMEDY`, `COMIC`, `COOKING_SHOW`, `CRIME`, `DISASTER`, `DOCUMENTARY`, `DRAMA`, `FAMILY`, `FANTASY`, `GAME_SHOW`, `HISTORY`, `HORROR`, `LGBT`, `MARTIAL_ARTS`, `MILITARY`, `MUSIC`, `POLICE`, `POLICE_PROCEDURAL`, `POLITIC`, `REALITY_TV`, `ROAD`, `ROMANCE`, `SATIRE`, `SCIENCE_FICTION`, `SITCOM`, `SOAP_OPERA`, `SPORT`, `SPY`, `STEAMPUNK`, `SUPERHERO`, `TALK_SHOW`, `TEEN`, `THRILLER`, `TIME_TRAVEL`, `VAMPIRE`, `WAR`, `WESTERN`, `ZOMBIE`.

#### Cho bộ sản phẩm danh mục Kho xe ô tô (For Auto-Inventory catalog product sets)

| Field | Description | Supported operators | Additional information |
|---|---|---|---|
| vehicle_id | ID duy nhất cho xe. | CONTAIN <br> I_CONTAIN <br> EXCLUDE <br> I_EXCLUDE <br> WILDCARD <br> I_WILDCARD <br> NOT_WILDCARD <br> I_NOT_WILDCARD <br> PREFIX <br> I_PREFIX | |
| title | Tên hoặc tiêu đề của xe. | EQUAL <br> NOT_EQUAL <br> WILDCARD <br> I_WILDCARD <br> NOT_WILDCARD <br> I_NOT_WILDCARD <br> PREFIX <br> I_PREFIX | |
| availability | Tình trạng có sẵn của xe. | EQUAL <br> NOT_EQUAL <br> CONTAIN <br> I_CONTAIN <br> EXCLUDE <br> I_EXCLUDE | Giá trị: • `AVAILABLE` • `NOT_AVAILABLE` |
| condition | Tình trạng hiện tại của xe. | EQUAL <br> NOT_EQUAL <br> CONTAIN <br> I_CONTAIN <br> EXCLUDE <br> I_EXCLUDE | Giá trị: • `EXCELLENT` • `GOOD` • `FAIR` • `POOR` • `OTHER` |
| state_of_vehicle | Trạng thái xe. | CONTAIN <br> I_CONTAIN <br> EXCLUDE <br> I_EXCLUDE | Giá trị: • `NEW` • `USED` • `CPO` (xe đã qua sử dụng có chứng nhận) |
| vehicle_type | Loại phương tiện. | CONTAIN <br> I_CONTAIN <br> EXCLUDE <br> I_EXCLUDE | Giá trị: • `BOAT` • `CAR_TRUCK` • `COMMERCIAL` • `MOTORCYCLE` • `POWERSPORT` • `RV_CAMPER` • `TRAILER` • `OTHER` |
| make | Hãng sản xuất xe (brand). | CONTAIN <br> I_CONTAIN <br> EXCLUDE <br> I_EXCLUDE <br> WILDCARD <br> I_WILDCARD <br> NOT_WILDCARD <br> I_NOT_WILDCARD <br> PREFIX <br> I_PREFIX | |
| model | Dòng xe (model). | CONTAIN <br> I_CONTAIN <br> EXCLUDE <br> I_EXCLUDE <br> WILDCARD <br> I_WILDCARD <br> NOT_WILDCARD <br> I_NOT_WILDCARD <br> PREFIX <br> I_PREFIX | |
| trim | Phiên bản trang bị (trim) của xe. | CONTAIN <br> I_CONTAIN <br> EXCLUDE <br> I_EXCLUDE <br> WILDCARD <br> I_WILDCARD <br> NOT_WILDCARD <br> I_NOT_WILDCARD <br> PREFIX <br> I_PREFIX | |
| year | Năm ra mắt của xe (định dạng `YYYY`). | GT <br> GTE <br> LT <br> LTE <br> EQUAL | |
| vin | Số khung nhận dạng xe (VIN). | CONTAIN <br> I_CONTAIN <br> EXCLUDE <br> I_EXCLUDE <br> WILDCARD <br> I_WILDCARD <br> NOT_WILDCARD <br> I_NOT_WILDCARD <br> PREFIX <br> I_PREFIX | |
| body_style | Kiểu dáng thân xe. | CONTAIN <br> I_CONTAIN <br> EXCLUDE <br> I_EXCLUDE | Giá trị: • `CONVERTIBLE` • `COUPE` • `CROSSOVER` • `HATCHBACK` • `MINIVAN` • `SMALL_CAR` • `SEDAN` • `SUV` • `TRUCK` • `VAN` • `WAGON` • `OTHER` |
| exterior_color | Màu ngoại thất của xe. | CONTAIN <br> I_CONTAIN <br> EXCLUDE <br> I_EXCLUDE <br> WILDCARD <br> I_WILDCARD <br> NOT_WILDCARD <br> I_NOT_WILDCARD <br> PREFIX <br> I_PREFIX | |
| interior_color | Màu nội thất của xe. | CONTAIN <br> I_CONTAIN <br> EXCLUDE <br> I_EXCLUDE <br> WILDCARD <br> I_WILDCARD <br> NOT_WILDCARD <br> I_NOT_WILDCARD <br> PREFIX <br> I_PREFIX | |
| transmission | Loại hộp số của xe. | CONTAIN <br> I_CONTAIN <br> EXCLUDE <br> I_EXCLUDE | Giá trị: • `AUTOMATIC` • `MANUAL` |
| drivetrain | Hệ dẫn động của xe. | CONTAIN <br> I_CONTAIN <br> EXCLUDE <br> I_EXCLUDE | Giá trị: • `4X2` • `4X4` • `AWD` • `FWD` • `RWD` • `OTHER` |
| fuel_type | Loại nhiên liệu của xe. | CONTAIN <br> I_CONTAIN <br> EXCLUDE <br> I_EXCLUDE | Giá trị: • `DIESEL` • `ELECTRIC` • `FLEX` • `GASOLINE` • `HYBRID` • `OTHER` |
| city | Thành phố nơi đại lý tọa lạc. | CONTAIN <br> I_CONTAIN <br> EXCLUDE <br> I_EXCLUDE <br> WILDCARD <br> I_WILDCARD <br> NOT_WILDCARD <br> I_NOT_WILDCARD <br> PREFIX <br> I_PREFIX | |
| region | Khu vực (tỉnh/bang) nơi đại lý tọa lạc. | CONTAIN <br> I_CONTAIN <br> EXCLUDE <br> I_EXCLUDE <br> WILDCARD <br> I_WILDCARD <br> NOT_WILDCARD <br> I_NOT_WILDCARD <br> PREFIX <br> I_PREFIX | |
| dealer_id | ID duy nhất của đại lý bán xe. | CONTAIN <br> I_CONTAIN <br> EXCLUDE <br> I_EXCLUDE <br> WILDCARD <br> I_WILDCARD <br> NOT_WILDCARD <br> I_NOT_WILDCARD <br> PREFIX <br> I_PREFIX | |
| dealer_name | Tên của đại lý. | CONTAIN <br> I_CONTAIN <br> EXCLUDE <br> I_EXCLUDE <br> WILDCARD <br> I_WILDCARD <br> NOT_WILDCARD <br> I_NOT_WILDCARD <br> PREFIX <br> I_PREFIX | |
| stock_number | Mã số kho do đại lý gán cho xe. | CONTAIN <br> I_CONTAIN <br> EXCLUDE <br> I_EXCLUDE <br> WILDCARD <br> I_WILDCARD <br> NOT_WILDCARD <br> I_NOT_WILDCARD <br> PREFIX <br> I_PREFIX | |
| date_first_on_lot | Ngày xe về tới bãi đại lý (`YYYY-MM-DD`). | GT <br> GTE <br> LT <br> LTE <br> EQUAL | |
| days_on_lot | Số ngày xe nằm tại bãi đại lý. | GT <br> GTE <br> LT <br> LTE <br> EQUAL | |
| price | Giá xe. | GT <br> GTE <br> LT <br> LTE <br> EQUAL | |
| sale_price | Giá ưu đãi của xe. | GT <br> GTE <br> LT <br> LTE <br> EQUAL | |
| custom_label_0 <br> custom_label_1 <br> custom_label_2 <br> custom_label_3 <br> custom_label_4 | Nhãn tùy chỉnh bổ sung. | CONTAIN <br> I_CONTAIN <br> EXCLUDE <br> I_EXCLUDE <br> WILDCARD <br> I_WILDCARD <br> NOT_WILDCARD <br> I_NOT_WILDCARD <br> PREFIX <br> I_PREFIX | |

#### Cho bộ sản phẩm danh mục Mẫu xe ô tô (For Auto-Model catalog product sets)

| Field | Description | Supported operators | Additional information |
|---|---|---|---|
| vehicle_id | ID duy nhất cho xe. | CONTAIN <br> I_CONTAIN <br> EXCLUDE <br> I_EXCLUDE <br> WILDCARD <br> I_WILDCARD <br> NOT_WILDCARD <br> I_NOT_WILDCARD <br> PREFIX <br> I_PREFIX | |
| title | Tên của mẫu xe. | EQUAL <br> NOT_EQUAL <br> WILDCARD <br> I_WILDCARD <br> NOT_WILDCARD <br> I_NOT_WILDCARD <br> PREFIX <br> I_PREFIX | |
| make | Thương hiệu của xe. | CONTAIN <br> I_CONTAIN <br> EXCLUDE <br> I_EXCLUDE <br> WILDCARD <br> I_WILDCARD <br> NOT_WILDCARD <br> I_NOT_WILDCARD <br> PREFIX <br> I_PREFIX | |
| model | Dòng xe. | CONTAIN <br> I_CONTAIN <br> EXCLUDE <br> I_EXCLUDE <br> WILDCARD <br> I_WILDCARD <br> NOT_WILDCARD <br> I_NOT_WILDCARD <br> PREFIX <br> I_PREFIX | |
| trim | Phiên bản trang bị (trim). | CONTAIN <br> I_CONTAIN <br> EXCLUDE <br> I_EXCLUDE <br> WILDCARD <br> I_WILDCARD <br> NOT_WILDCARD <br> I_NOT_WILDCARD <br> PREFIX <br> I_PREFIX | |
| year | Năm ra mắt (`YYYY`). | GT <br> GTE <br> LT <br> LTE <br> EQUAL | |
| exterior_color | Màu sắc của xe. | CONTAIN <br> I_CONTAIN <br> EXCLUDE <br> I_EXCLUDE <br> WILDCARD <br> I_WILDCARD <br> NOT_WILDCARD <br> I_NOT_WILDCARD <br> PREFIX <br> I_PREFIX | |

#### Cho bộ sản phẩm danh mục Chung (For generic catalog product sets)

| Field | Description | Supported operators | Additional information |
|---|---|---|---|
| item_id | ID duy nhất tự định nghĩa cho sản phẩm hoặc dịch vụ. | CONTAIN <br> I_CONTAIN <br> EXCLUDE <br> I_EXCLUDE <br> WILDCARD <br> I_WILDCARD <br> NOT_WILDCARD <br> I_NOT_WILDCARD <br> PREFIX <br> I_PREFIX | |
| title | Tên của sản phẩm hoặc dịch vụ. | EQUAL <br> NOT_EQUAL <br> WILDCARD <br> I_WILDCARD <br> NOT_WILDCARD <br> I_NOT_WILDCARD <br> PREFIX <br> I_PREFIX | |
| availability | Trạng thái tồn kho hiện tại. | EQUAL <br> NOT_EQUAL | Giá trị: • `IN_STOCK` • `AVAILABLE` • `PREORDER` • `OUT_OF_STOCK` • `DISCONTINUED` • `UNAVAILABLE` |
| address.street | Địa chỉ đường nơi đặt sản phẩm/dịch vụ. | EQUAL <br> NOT_EQUAL <br> WILDCARD <br> I_WILDCARD <br> NOT_WILDCARD <br> I_NOT_WILDCARD <br> PREFIX <br> I_PREFIX | |
| address.city | Thành phố nơi đặt sản phẩm/dịch vụ. | EQUAL <br> NOT_EQUAL <br> WILDCARD <br> I_WILDCARD <br> NOT_WILDCARD <br> I_NOT_WILDCARD <br> PREFIX <br> I_PREFIX | |
| address.region | Tiểu bang/tỉnh/khu vực hành chính nơi đặt sản phẩm/dịch vụ. | EQUAL <br> NOT_EQUAL <br> WILDCARD <br> I_WILDCARD <br> NOT_WILDCARD <br> I_NOT_WILDCARD <br> PREFIX <br> I_PREFIX | |
| rating | Đánh giá của người dùng cho sản phẩm hoặc dịch vụ. | GT <br> GTE <br> LT <br> LTE <br> EQUAL | |
| price | Giá của một đơn vị sản phẩm/dịch vụ. | GT <br> GTE <br> LT <br> LTE <br> EQUAL | |
| sale_price | Giá chiết khấu của một đơn vị sản phẩm/dịch vụ. | GT <br> GTE <br> LT <br> LTE <br> EQUAL | |
| custom_label_ | Nhãn tùy chỉnh bổ sung thông tin sản phẩm (`custom_label_0` đến `custom_label_6`). | CONTAIN <br> I_CONTAIN <br> EXCLUDE <br> I_EXCLUDE <br> WILDCARD <br> I_WILDCARD <br> NOT_WILDCARD <br> I_NOT_WILDCARD <br> PREFIX <br> I_PREFIX | |
| custom_number_ | Thuộc tính số tùy chỉnh cho quản lý sản phẩm (`custom_number_0` đến `custom_number_4`). | GT <br> GTE <br> LT <br> LTE <br> EQUAL | |

#### Cho sản phẩm trực tuyến đến ngoại tuyến (For online-to-offline products)

| Field | Description | Supported operators | Additional information |
|---|---|---|---|
| availability | Trạng thái có sẵn của mặt hàng. | EQUAL <br> NOT_EQUAL | Giá trị: • `IN_STOCK` • `AVAILABLE_FOR_ORDER` • `PREORDER` • `OUT_OF_STOCK` • `DISCONTINUED` |
| brand | Tên thương hiệu. | CONTAIN <br> I_CONTAIN <br> EXCLUDE <br> I_EXCLUDE <br> WILDCARD <br> I_WILDCARD <br> NOT_WILDCARD <br> I_NOT_WILDCARD <br> PREFIX <br> I_PREFIX | Ví dụ: `McDonald’s` |
| google_product_category | Danh mục phân loại sản phẩm Google. | CONTAIN <br> I_CONTAIN <br> EXCLUDE <br> I_EXCLUDE <br> WILDCARD <br> I_WILDCARD <br> NOT_WILDCARD <br> I_NOT_WILDCARD <br> PREFIX <br> I_PREFIX | Ví dụ: `Food, Beverages & Tobacco > Food Items > Prepared Foods` |
| age_group | Nhóm tuổi mục tiêu. | EQUAL <br> NOT_EQUAL | Giá trị: • `NEW_BORN` • `INFANT` • `TODDLER` • `KIDS` • `ADULT` |
| gender | Giới tính mục tiêu. | EQUAL <br> NOT_EQUAL | Giá trị: • `MALE` • `FEMALE` • `UNISEX` |
| item_group_id | ID SPU dùng chung cho tất cả các biến thể của sản phẩm. | CONTAIN <br> I_CONTAIN <br> EXCLUDE <br> I_EXCLUDE <br> WILDCARD <br> I_WILDCARD <br> NOT_WILDCARD <br> I_NOT_WILDCARD <br> PREFIX <br> I_PREFIX | Ví dụ: `tiktok_1234_shirts` |
| region | Bang/tỉnh/khu vực đặt sản phẩm/dịch vụ. | CONTAIN <br> I_CONTAIN <br> EXCLUDE <br> I_EXCLUDE <br> WILDCARD <br> I_WILDCARD <br> NOT_WILDCARD <br> I_NOT_WILDCARD <br> PREFIX <br> I_PREFIX | Ví dụ: `California` |
| city | Thành phố nơi đặt sản phẩm/dịch vụ. | CONTAIN <br> I_CONTAIN <br> EXCLUDE <br> I_EXCLUDE <br> WILDCARD <br> I_WILDCARD <br> NOT_WILDCARD <br> I_NOT_WILDCARD <br> PREFIX <br> I_PREFIX | Ví dụ: `San Jose` |
| custom_label_0 <br> custom_label_1 <br> custom_label_2 <br> custom_label_3 <br> custom_label_4 | Nhãn tùy chỉnh dùng để thêm thông tin mặt hàng. | CONTAIN <br> I_CONTAIN <br> EXCLUDE <br> I_EXCLUDE <br> WILDCARD <br> I_WILDCARD <br> NOT_WILDCARD <br> I_NOT_WILDCARD <br> PREFIX <br> I_PREFIX | |
| custom_number_0 <br> custom_number_1 <br> custom_number_2 <br> custom_number_3 <br> custom_number_4 | Thuộc tính số tùy chỉnh cho quản lý sản phẩm. | GT <br> GTE <br> LT <br> LTE <br> EQUAL | Ví dụ: `1`, `2.5` |
| rating | Đánh giá của người dùng. | GT <br> GTE <br> LT <br> LTE <br> EQUAL | Dải giá trị: `0.0 - 5.0` |
| price | Giá của một mặt hàng. | GT <br> GTE <br> LT <br> LTE <br> EQUAL | |
| condition | Tình trạng hiện tại của mặt hàng. | EQUAL <br> NOT_EQUAL | Giá trị: • `NEW` • `USED` • `REFURBISHED` |


## Tham số nguồn cấp CSV cho danh mục chung (`Generic catalog CSV feed parameters`)
<a id="doc-1873323074102273"></a>
<!-- doc_id: 1873323074102273 -->

> Đường dẫn: Marketing API > Catalog Management > Guides > Create catalogs and add products > Generic catalog CSV feed parameters

Bảng dưới đây liệt kê các tham số bạn có thể cấu hình cho danh mục chung (generic catalog) khi truyền tệp CSV vào tham số `file_url` trong endpoint [/catalog/product/file/](../12-api-reference/28-catalog-products-p1.md#doc-1740496787164161).

| Field | Data Type | Description |
|---|---|---|
| item_id | string | ID duy nhất tự định nghĩa cho sản phẩm hoặc dịch vụ (bắt buộc). <br> Giới hạn độ dài: 100 ký tự. Đảm bảo sử dụng các ký tự Unicode hợp lệ. |
| title | string | Tên sản phẩm hoặc dịch vụ (bắt buộc). <br> Bạn có thể sử dụng cùng tiêu đề sản phẩm từ trang đích. <br> Giới hạn độ dài: 500 ký tự. |
| description | string | Mô tả chi tiết về sản phẩm hoặc dịch vụ. <br> Giới hạn độ dài: 5.000 ký tự. |
| availability | string | Trạng thái tồn kho hiện tại. <br> Giá trị enum: • `in stock` • `available` • `preorder` • `out of stock` • `discontinued` • `unavailable` |
| image_link | string | URL hình ảnh chính của sản phẩm/dịch vụ (bắt buộc). <br> Yêu cầu: • URL truy cập trực tiếp có domain xác minh, bắt đầu bằng `http://` hoặc `https://`. • Định dạng JPG hoặc PNG. • Kích thước tối thiểu 500 × 500 px, tối đa 1290 × 2790 px. Tỷ lệ khuyến nghị 1:1. |
| video_link | string | Đường dẫn video sản phẩm/dịch vụ. • Bắt đầu bằng `http://` hoặc `https://`. • Tỷ lệ khuyến nghị 9:16 (dọc). • Độ phân giải: ≥ 720×1280. • Bitrate: ≥ 516 kbps. • Âm thanh: bật kèm phụ đề. |
| link | string | Liên kết đến trang đích của sản phẩm/dịch vụ. Bắt đầu bằng `http://` hoặc `https://`. |
| rating | double | Đánh giá của người dùng. Dải giá trị: 0.0 - 5.0. |
| price | double | Giá của một đơn vị sản phẩm hoặc dịch vụ. Hệ thống sử dụng đơn vị tiền tệ mặc định của quốc gia mục tiêu. Ví dụ: `9.99`. |
| additional_image_link | string | Danh sách URL hình ảnh bổ sung (tối đa 20 liên kết, phân tách bằng dấu phẩy). |
| sale_price | double | Giá khuyến mãi của sản phẩm/dịch vụ. Để hiển thị cả hai giá trên quảng cáo, hãy giữ `sale_price` thấp hơn `price`. Ví dụ: `4.99`. |
| availability_type | string | Phương thức xác định khu vực địa lý có thể bán sản phẩm hoặc cung cấp dịch vụ. <br> Giá trị enum: • `region` (khu vực/địa điểm) • `dma` (DMA - Hoa Kỳ) • `radius` (bán kính) • `postal_code` (mã bưu điện). |
| availability_region | string[][] | Bắt buộc khi `availability_type` là `region`. Mảng chứa các cặp địa điểm [L1, L2]. Ví dụ: `[["Arizona","Peoria"],["Alabama","Birmingham"]]`. |
| availability_dma | string[] | Bắt buộc khi `availability_type` là `dma`. Danh sách mã DMA phân tách bằng dấu phẩy (chỉ dành cho Hoa Kỳ). |
| availability_circle_radius | string | Bắt buộc khi `availability_type` là `radius`. Bán kính phục vụ (km: > 0 và ≤ 40; dặm: > 0 và ≤ 25). Chỉ áp dụng cho ID, MY, TH, VN. |
| availability_circle_radius_unit | string | Bắt buộc khi `availability_type` là `radius`. Đơn vị bán kính: `km` hoặc `mi`. |
| availability_postal_codes | string[] | Bắt buộc khi `availability_type` là `postal_code`. Danh sách tối đa 500 mã bưu điện (chỉ dành cho US và CA). |
| address_street | string | Địa chỉ đường nơi đặt sản phẩm/dịch vụ (tối đa 150 ký tự). |
| address_city | string | Thành phố nơi đặt sản phẩm/dịch vụ (tối đa 150 ký tự). |
| address_region | string | Bang/tỉnh/khu vực hành chính nơi đặt sản phẩm/dịch vụ (tối đa 150 ký tự). |
| address_postal_code | string | Mã bưu điện của địa điểm sản phẩm/dịch vụ (tối đa 150 ký tự). |
| address_longitude | double | Kinh độ địa điểm [-180, 180]. Ví dụ: `100.5`. |
| address_latitude | double | Vĩ độ địa điểm [-90, 90]. Ví dụ: `-25.5`. |
| ios_url | string | URL ứng dụng iOS (deeplink). |
| ios_app_store_id | string | ID App Store của ứng dụng iOS. |
| ios_app_name | string | Tên ứng dụng iOS. |
| android_url | string | URL ứng dụng Android (deeplink). |
| android_package | string | Tên gói Android (package name). |
| android_app_name | string | Tên ứng dụng Android. |
| custom_label_0 | string | Nhãn tùy chỉnh 0 (tối đa 500 ký tự). |
| custom_label_1 | string | Nhãn tùy chỉnh 1 (tối đa 500 ký tự). |
| custom_label_2 | string | Nhãn tùy chỉnh 2 (tối đa 500 ký tự). |
| custom_label_3 | string | Nhãn tùy chỉnh 3 (tối đa 500 ký tự). |
| custom_label_4 | string | Nhãn tùy chỉnh 4 (tối đa 500 ký tự). |
| custom_label_5 | string | Nhãn tùy chỉnh 5 (tối đa 500 ký tự). |
| custom_label_6 | string | Nhãn tùy chỉnh 6 (tối đa 500 ký tự). |
| custom_number_0 | double | Thuộc tính số tùy chỉnh 0. |
| custom_number_1 | double | Thuộc tính số tùy chỉnh 1. |
| custom_number_2 | double | Thuộc tính số tùy chỉnh 2. |
| custom_number_3 | double | Thuộc tính số tùy chỉnh 3. |
| custom_number_4 | double | Thuộc tính số tùy chỉnh 4. |

## Tạo danh mục chung (`Create a generic catalog`)
<a id="doc-1873323143235585"></a>
<!-- doc_id: 1873323143235585 -->

> Đường dẫn: Marketing API > Catalog Management > Guides > Create catalogs and add products > Create a generic catalog

Bài viết này hướng dẫn cách tạo danh mục sản phẩm/dịch vụ chung (Generic catalog) và tải lên các mặt hàng thông qua Catalog API.

### Giới thiệu (Introduction)

Danh mục chung (Generic Catalog) được thiết kế cho các ngành hàng đa dạng hoặc dịch vụ không thuộc các danh mục chuyên biệt (như khách sạn, chuyến bay, ô tô). Bạn có thể định cấu hình các trường vị trí địa lý, xếp hạng, giá bán và liên kết sâu vào ứng dụng di động.

### Các bước thực hiện (Steps)

1. **Tạo danh mục chung:** Gọi endpoint [/catalog/create/](../12-api-reference/25-catalog-management.md#doc-1740306481704961) với `catalog_type` đặt là `GENERIC`.
2. **Tải sản phẩm/dịch vụ lên:**
   - Qua tệp CSV: Sử dụng [/catalog/product/file/](../12-api-reference/28-catalog-products-p1.md#doc-1740496787164161) và cấu hình các trường theo bảng tham số nguồn cấp CSV ở trên.
   - Qua JSON schema: Sử dụng [/catalog/product/upload/](../12-api-reference/28-catalog-products-p1.md#doc-1740497429681153) với payload tương ứng cho loại danh mục `GENERIC`.
3. **Kiểm tra trạng thái xử lý:** Sử dụng [/catalog/product/log/](../12-api-reference/28-catalog-products-p3.md#doc-1740570027173889) để xem `feed_log_id` và khắc phục các mặt hàng bị lỗi (nếu có).
4. **Liên kết nguồn sự kiện:** Gọi [/catalog/eventsource/bind/](../12-api-reference/26-catalog-event-sources.md#doc-1740492491200513) để gắn kết Pixel hoặc sự kiện ứng dụng phục vụ nhắm mục tiêu động.

## Tham số nguồn cấp CSV cho danh mục O2O (`O2O catalog CSV feed parameters`)
<a id="doc-1874599038216210"></a>
<!-- doc_id: 1874599038216210 -->

> Đường dẫn: Marketing API > Catalog Management > Guides > Create catalogs and add products > O2O catalog CSV feed parameters

Bảng dưới đây liệt kê các tham số có thể cấu hình cho danh mục trực tuyến đến ngoại tuyến (Online-to-Offline - O2O) khi truyền tệp CSV vào tham số `file_url` trong [/catalog/product/file/](../12-api-reference/28-catalog-products-p1.md#doc-1740496787164161).

| Field | Data Type | Description |
|---|---|---|
| listing_id | string | ID duy nhất cho mặt hàng (bắt buộc). |
| title | string | Tên mặt hàng (bắt buộc, độ dài khuyến nghị: 25 ký tự). Ví dụ: `Big Mac`. |
| description | string | Mô tả mặt hàng (bắt buộc, tối đa 5.000 ký tự). Ví dụ: `Nice burger!`. |
| availability | string | Trạng thái sẵn có (bắt buộc). Giá trị: `in stock`, `available for order`, `preorder`, `out of stock`, `discontinued`. |
| image_link | string | URL hình ảnh chính (bắt buộc, tối thiểu 500 × 500 px, tối đa 1290 × 2790 px). |
| link | string | URL trang đích web của mặt hàng. Bắt đầu bằng `http://` hoặc `https://`. |
| brand | string | Tên thương hiệu (tối đa 150 ký tự). |
| product_type | string | Danh mục sản phẩm/dịch vụ. Ví dụ: `Thai food`. |
| rating | double | Đánh giá của người dùng (0.0 - 5.0). |
| condition | string | Tình trạng mặt hàng: `new`, `refurbished`, `used`. |
| price | double | Giá của một mặt hàng niêm yết. Ví dụ: `9.99`. |
| google_product_category | string | Danh mục theo Google taxonomy (hỗ trợ tối đa 3 cấp). |
| item_group_id | string | ID SPU dùng chung cho các biến thể của sản phẩm. Ví dụ: `TikTok_1234`. |
| additional_image_link | string | Các URL hình ảnh bổ sung (tối đa 20 liên kết, ngăn cách bằng dấu phẩy). |
| color | string | Màu sắc của mặt hàng. |
| size | string | Kích thước mặt hàng. |
| material | string | Chất liệu chính của mặt hàng. |
| pattern | string | Họa tiết hoặc hoa văn in trên mặt hàng. |
| sale_price | double | Giá khuyến mãi của mặt hàng. Ví dụ: `4.99`. |
| sale_price_effective_date | string | Khoảng thời gian áp dụng giá khuyến mãi (`YYYY-MM-DDTHH:MM+00:00/YYYY-MM-DDTHH:MM+00:00`). |
| gtin | string | Mã số thương phẩm toàn cầu (GTIN: 8, 12, 13 hoặc 14 chữ số). |
| tax | string | Thuế suất áp dụng cho mặt hàng. |
| age_group | string | Nhóm tuổi mục tiêu: `newborn`, `infant`, `toddler`, `kids`, `adult`. |
| gender | string | Giới tính mục tiêu: `male`, `female`, `unisex`. |
| availability_circle_radius | string | Bán kính vòng tròn phục vụ tính từ điểm gốc (km: > 0 và ≤ 40; dặm: > 0 và ≤ 25). |
| availability_circle_radius_unit | string | Đơn vị bán kính: `km` hoặc `mi`. |
| address_street | string | Địa chỉ đường nơi đặt cửa hàng/dịch vụ (tối đa 150 ký tự). |
| address_city | string | Thành phố nơi đặt cửa hàng/dịch vụ (tối đa 150 ký tự). |
| address_region | string | Bang/tỉnh nơi đặt cửa hàng/dịch vụ (tối đa 150 ký tự). |
| address_postal_code | string | Mã bưu điện nơi đặt cửa hàng/dịch vụ (tối đa 150 ký tự). |
| address_longitude | double | Kinh độ của địa điểm [-180, 180]. |
| address_latitude | double | Vĩ độ của địa điểm [-90, 90]. |
| ios_url | string | URL ứng dụng iOS (deeplink). |
| ios_app_store_id | string | ID App Store của ứng dụng iOS. |
| ios_app_name | string | Tên ứng dụng iOS. |
| android_url | string | URL ứng dụng Android (deeplink). |
| android_package | string | Tên gói ứng dụng Android. |
| android_app_name | string | Tên ứng dụng Android. |
| custom_label_0 | string | Nhãn tùy chỉnh 0 (tối đa 500 ký tự). |
| custom_label_1 | string | Nhãn tùy chỉnh 1 (tối đa 500 ký tự). |
| custom_label_2 | string | Nhãn tùy chỉnh 2 (tối đa 500 ký tự). |
| custom_label_3 | string | Nhãn tùy chỉnh 3 (tối đa 500 ký tự). |
| custom_label_4 | string | Nhãn tùy chỉnh 4 (tối đa 500 ký tự). |
| custom_number_0 | double | Thuộc tính số tùy chỉnh 0. |
| custom_number_1 | double | Thuộc tính số tùy chỉnh 1. |
| custom_number_2 | double | Thuộc tính số tùy chỉnh 2. |
| custom_number_3 | double | Thuộc tính số tùy chỉnh 3. |
| custom_number_4 | double | Thuộc tính số tùy chỉnh 4. |

## Tạo danh mục trực tuyến đến ngoại tuyến (`Create an online-to-offline catalog`)
<a id="doc-1874599078452225"></a>
<!-- doc_id: 1874599078452225 -->

> Đường dẫn: Marketing API > Catalog Management > Guides > Create catalogs and add products > Create an online-to-offline catalog

Bài viết này hướng dẫn cách tạo danh mục trực tuyến đến ngoại tuyến (Online-to-Offline - O2O) và tải sản phẩm/dịch vụ lên thông qua Catalog API.

### Giới thiệu (Introduction)

Mô hình Online-to-Offline (O2O) kết nối các hoạt động quảng cáo trực tuyến với trải nghiệm mua sắm hoặc sử dụng dịch vụ tại cửa hàng thực tế (chẳng hạn như chuỗi nhà hàng, bán lẻ địa phương). Danh mục O2O hỗ trợ xác định bán kính phục vụ (`availability_circle_radius`), tọa độ địa lý và thông tin cửa hàng thực tế.

### Các bước thực hiện (Steps)

1. **Tạo danh mục O2O:** Gọi endpoint [/catalog/create/](../12-api-reference/25-catalog-management.md#doc-1740306481704961) với `catalog_type` đặt là `ONLINE_TO_OFFLINE`.
2. **Tải dữ liệu mặt hàng lên:**
   - Qua tệp CSV: Sử dụng [/catalog/product/file/](../12-api-reference/28-catalog-products-p1.md#doc-1740496787164161) và cung cấp các trường theo bảng tham số nguồn cấp O2O.
   - Qua JSON schema: Sử dụng [/catalog/product/upload/](../12-api-reference/28-catalog-products-p1.md#doc-1740497429681153) với payload tương ứng.
3. **Theo dõi kết quả xử lý:** Sử dụng [/catalog/product/log/](../12-api-reference/28-catalog-products-p3.md#doc-1740570027173889) để xem tiến trình xử lý và sửa lỗi nếu có.
4. **Liên kết nguồn sự kiện và tạo chiến dịch:** Liên kết Pixel hoặc App event source và sử dụng bộ sản phẩm để chạy các chiến dịch quảng cáo định hướng khách hàng đến cửa hàng.


## Xử lý sự cố danh mục bằng tính năng chẩn đoán (`Troubleshoot catalogs with diagnostics`)
<a id="doc-1780803490136066"></a>
<!-- doc_id: 1780803490136066 -->

> Đường dẫn: Marketing API > Catalog Management > Guides > Troubleshoot catalogs with diagnostics

Bài viết này cung cấp hướng dẫn từng bước về việc xử lý sự cố sản phẩm và nguồn sự kiện của danh mục, bao gồm Tỷ lệ khớp danh mục (Catalog Match Rate) bằng cách sử dụng Catalog Diagnostics. Tính năng này giúp bạn xác định và khắc phục các vấn đề liên quan đến sản phẩm và nguồn sự kiện được liên kết với danh mục của bạn.

Để xem bảng ánh xạ giữa tính năng chẩn đoán trên giao diện Catalog Manager và cấu hình API tương ứng, hãy xem [Ánh xạ giữa tính năng chẩn đoán Catalog Manager và cấu hình API](catalog.md#doc-1780803525320706).

### Xử lý sự cố sản phẩm trong danh mục (Troubleshoot catalog products)

#### Điều kiện tiên quyết (Prerequisites)
Đảm bảo bạn đã thêm sản phẩm vào danh mục của mình. Xem chi tiết tại [Tạo danh mục và thêm sản phẩm](catalog.md#doc-1754263112945665).

#### Các bước thực hiện (Steps)
1. Lấy thông tin chẩn đoán cho sản phẩm danh mục theo một trong hai chế độ:
   - **Chế độ đồng bộ (Synchronous mode):** Sử dụng [/diagnostic/catalog/](../12-api-reference/32-catalog-diagnostics.md#doc-1771117232728066) để truy xuất thông tin chẩn đoán danh mục chi tiết theo thời gian thực.
   - **Chế độ bất đồng bộ (Asynchronous mode):**
     - Sử dụng [/diagnostic/catalog/product/task/create/](../12-api-reference/32-catalog-diagnostics.md#doc-1771117279175682) để tạo tác vụ tải xuống tệp chẩn đoán.
     - Sau đó sử dụng [/diagnostic/catalog/product/task/get/](../12-api-reference/32-catalog-diagnostics.md#doc-1771117294731266) để tải tệp CSV chứa thông tin chẩn đoán.
2. Nếu phát hiện sự cố với các sản phẩm trong danh mục, sử dụng endpoint [/catalog/product/update/](../12-api-reference/28-catalog-products-p2.md#doc-1740562287852546) để cập nhật sản phẩm và khắc phục lỗi.

### Xử lý sự cố nguồn sự kiện và Tỷ lệ khớp danh mục (Catalog Match Rate)

**Tỷ lệ khớp danh mục (Catalog Match Rate)** thể hiện tỷ lệ phần trăm các sự kiện tín hiệu được chia sẻ có thể khớp chính xác với SKU ID trong danh mục thông qua thuộc tính Content ID. Việc duy trì Tỷ lệ khớp trên 90% là tiêu chuẩn khuyến nghị để đạt hiệu suất tối ưu cho Quảng cáo Mua sắm Video (Video Shopping Ads). Khi không thể khớp chính xác giữa Content ID và SKU ID, hệ thống sẽ xem xét các thuộc tính danh mục khác để phân phối nội dung quảng cáo.

#### Điều kiện tiên quyết (Prerequisites)
Đảm bảo bạn đã liên kết nguồn sự kiện với danh mục trong Business Center bằng [/catalog/eventsource/bind/](../12-api-reference/26-catalog-event-sources.md#doc-1740492491200513) hoặc trên TikTok Ads Manager.
Để kiểm tra xem nguồn sự kiện đã được liên kết với danh mục hay chưa, hãy sử dụng endpoint [/catalog/eventsource_bind/get/](../12-api-reference/26-catalog-event-sources.md#doc-1740492531343362).

#### Các bước thực hiện (Steps)
1. Lấy thông tin chẩn đoán cho các nguồn sự kiện (Apps hoặc Pixels) đã liên kết bằng endpoint [/diagnostic/catalog/eventsource/issue/](../12-api-reference/32-catalog-diagnostics.md#doc-1780799405041665).
   - Nếu phát hiện vấn đề với nguồn sự kiện, chi tiết sẽ được trả về trong trường `diagnostic_result`. Bạn có thể làm theo các gợi ý trong trường `diagnostic_solution` để giải quyết.
2. Truy xuất Tỷ lệ khớp danh mục bằng endpoint [/diagnostic/catalog/eventsource/metric/](../12-api-reference/32-catalog-diagnostics.md#doc-1780802101608450).
   - Tỷ lệ khớp sẽ được trả về qua trường `percentage` khi `available_type` là `EVENT_WITH_CONTENT_ID_MATCHING_INVENTORY`. Lưu ý rằng nếu nguồn sự kiện mới được kết nối lần đầu, tỷ lệ này cần vài ngày để ổn định.
3. Khi không phát hiện vấn đề nào và Tỷ lệ khớp đạt trên 90%, bạn có thể tự tin sử dụng danh mục để tạo [Quảng cáo Mua sắm Video](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1750361698613249) và tiếp thị lại những đối tượng đã tương tác với sản phẩm.

## Ánh xạ giữa tính năng chẩn đoán Catalog Manager và cấu hình API (`Mapping between Catalog Diagnostics features in Catalog Manager and API configurations`)
<a id="doc-1780803525320706"></a>
<!-- doc_id: 1780803525320706 -->

> Đường dẫn: Marketing API > Catalog Management > Guides > Troubleshoot catalogs with diagnostics > Mapping between Catalog Diagnostics features in Catalog Manager and API configurations

Bảng dưới đây liệt kê các tính năng chẩn đoán danh mục sản phẩm và nguồn sự kiện trong giao diện Catalog Manager cùng các cấu hình API tương ứng:

### Chẩn đoán sản phẩm danh mục (Diagnostics for catalog products)

| Phân hệ Catalog Manager | Tính năng | Endpoint API | Cấu hình API |
|---|---|---|---|
| Diagnostics > Overview | Tải báo cáo tóm tắt danh mục (Export Summary Report) | [/diagnostic/catalog/](../12-api-reference/32-catalog-diagnostics.md#doc-1771117232728066) | Chế độ đồng bộ |
| Diagnostics > Overview | Tạo tác vụ tải tệp chẩn đoán chi tiết | [/diagnostic/catalog/product/task/create/](../12-api-reference/32-catalog-diagnostics.md#doc-1771117279175682) | Chế độ bất đồng bộ |
| Diagnostics > Overview | Tải tệp CSV chẩn đoán sản phẩm | [/diagnostic/catalog/product/task/get/](../12-api-reference/32-catalog-diagnostics.md#doc-1771117294731266) | Tải kết quả CSV |

### Chẩn đoán nguồn sự kiện danh mục (Diagnostics for event sources)

| Phân hệ Catalog Manager | Tính năng | Endpoint API | Cấu hình API |
|---|---|---|---|
| Diagnostics > Event Sources | Danh sách vấn đề nguồn sự kiện | [/diagnostic/catalog/eventsource/issue/](../12-api-reference/32-catalog-diagnostics.md#doc-1780799405041665) | Kết quả qua `diagnostic_result` và `diagnostic_solution` |
| Diagnostics > Event Sources | Tỷ lệ khớp danh mục (Catalog Match Rate) | [/diagnostic/catalog/eventsource/metric/](../12-api-reference/32-catalog-diagnostics.md#doc-1780802101608450) | `available_type` = `EVENT_WITH_CONTENT_ID_MATCHING_INVENTORY` |

## Lấy thông tin chi tiết về sản phẩm trong danh mục (`Obtain Catalog Product Insights`)
<a id="doc-1805642743426050"></a>
<!-- doc_id: 1805642743426050 -->

> Đường dẫn: Marketing API > Catalog Management > Guides > Obtain Catalog Product Insights

Tính năng Product Insights giúp bạn nắm bắt xu hướng các sản phẩm bán chạy hoặc được quan tâm nhiều nhất trong danh mục của bạn, cũng như các danh mục ngành hàng đang thịnh hành trên toàn bộ nền tảng TikTok.

### Các bước thực hiện (Steps)

1. **Lấy danh sách sản phẩm thịnh hành trong danh mục:** Gọi endpoint [/catalog/insight/product/get/](../12-api-reference/33-catalog-insights.md#doc-1805640886872066). Bạn có thể lọc theo danh mục (`category_ids`), thương hiệu (`brands`) hoặc tình trạng còn hàng (`availabilities`).
2. **Lấy danh sách ngành hàng thịnh hành trên TikTok:** Gọi endpoint [/catalog/insight/category/get/](../12-api-reference/33-catalog-insights.md#doc-1805640900563969) để xem mức độ phổ biến của các danh mục ngành hàng, số lượng sản phẩm phù hợp trong danh mục của bạn (`total_products_count`) và tỷ lệ sẵn có (`product_availability_rate`).

## Ánh xạ giữa tính năng Catalog Product Insights và cấu hình API (`Mapping between Catalog Product Insights features in Catalog Manager and API configurations`)
<a id="doc-1805642902406145"></a>
<!-- doc_id: 1805642902406145 -->

> Đường dẫn: Marketing API > Catalog Management > Guides > Obtain Catalog Product Insights > Mapping between Catalog Product Insights features in Catalog Manager and API configurations

Bảng dưới đây đối chiếu các tính năng trong phân hệ Insights của Catalog Manager với các cấu hình API tương ứng:

| Phân hệ Catalog Manager | Tính năng | Endpoint API | Cấu hình API |
|---|---|---|---|
| Insights > Your trending products | Bộ lọc Danh mục (Category filter) | [/catalog/insight/product/get/](../12-api-reference/33-catalog-insights.md#doc-1805640886872066) | Tham số yêu cầu: `category_ids` |
| Insights > Your trending products | Bộ lọc Thương hiệu (Brand filter) | [/catalog/insight/product/get/](../12-api-reference/33-catalog-insights.md#doc-1805640886872066) | Tham số yêu cầu: `brands` |
| Insights > Your trending products | Bộ lọc Tồn kho (Availability filter) | [/catalog/insight/product/get/](../12-api-reference/33-catalog-insights.md#doc-1805640886872066) | Tham số yêu cầu: `availabilities` |
| Insights > Your trending products | Thứ hạng (Rank) | [/catalog/insight/product/get/](../12-api-reference/33-catalog-insights.md#doc-1805640886872066) | Vị trí trong mảng `product_insights` phản hồi |
| Insights > Your trending products | Thông tin sản phẩm (Product) | [/catalog/insight/product/get/](../12-api-reference/33-catalog-insights.md#doc-1805640886872066) | Trường phản hồi: `image_url`, `description`, `sku_id`, `price` |
| Insights > Trending categories on TikTok | Thứ hạng danh mục (Rank) | [/catalog/insight/category/get/](../12-api-reference/33-catalog-insights.md#doc-1805640900563969) | Vị trí trong mảng `category_insights` phản hồi |
| Insights > Trending categories on TikTok | Chi tiết danh mục | [/catalog/insight/category/get/](../12-api-reference/33-catalog-insights.md#doc-1805640900563969) | Trường phản hồi: `category_id`, `level_info` |
| Insights > Trending categories on TikTok | Số sản phẩm khớp của bạn (Your matching products) | [/catalog/insight/category/get/](../12-api-reference/33-catalog-insights.md#doc-1805640900563969) | Trường phản hồi: `total_products_count` |
| Insights > Trending categories on TikTok | Tỷ lệ sẵn có (Available now) | [/catalog/insight/category/get/](../12-api-reference/33-catalog-insights.md#doc-1805640900563969) | Trường phản hồi: `product_availability_rate` |

## Tải lên video danh mục để liên kết với sản phẩm danh mục (`Upload catalog videos to associate with catalog products`)
<a id="doc-1803654904260674"></a>
<!-- doc_id: 1803654904260674 -->

> Đường dẫn: Marketing API > Catalog Management > Guides > Upload catalog videos to associate with catalog products

Tính năng Video danh mục tải lên cho phép bạn liên kết một video với tối đa 20 sản phẩm trong danh mục E-commerce. Sau khi liên kết, bạn có thể sử dụng các video này trong Quảng cáo Mua sắm Video (VSA cho Catalog) để tự động hiển thị sản phẩm tương ứng trong quảng cáo.

### Lợi ích chính (Key benefits)
- Liên kết video với các sản phẩm danh mục cụ thể, giúp video tự động giới thiệu các mặt hàng liên quan trong Video Shopping Ads.
- Quản lý thư viện video danh mục dễ dàng và tự động hóa thông qua các endpoint API.

### Các bước thực hiện (Steps)

1. **Tải lên video danh mục:** Sử dụng endpoint [/catalog/video/file/](../12-api-reference/30-catalog-videos.md#doc-1803655037415489) để tải video lên thông qua tệp mẫu CSV feed. Bạn có thể liên kết mỗi video với tối đa 20 sản phẩm trong danh mục E-commerce.
2. **Kiểm tra kết quả tải lên:** Xác minh kết quả xử lý bằng endpoint [/catalog/video/log/](../12-api-reference/30-catalog-videos.md#doc-1803655061642242) với tham số `feed_log_id`. Nếu trường `error_affected_products` không phải là null, hãy kiểm tra lỗi và tải lại video.
3. **Tạo Quảng cáo Mua sắm Video (VSA):** Thiết lập `promotion_type` là `WEBSITE` ở cấp nhóm quảng cáo và `vertical_video_strategy` là `CATALOG_UPLOADED_VIDEOS` ở cấp quảng cáo.
4. **Quản lý video đã tải lên (Tùy chọn):**
   - Lấy thông tin video danh mục: Sử dụng [/catalog/video/get/](../12-api-reference/30-catalog-videos.md#doc-1803655082498050).
   - Xóa video danh mục: Sử dụng [/catalog/video/delete/](../12-api-reference/30-catalog-videos.md#doc-1803655103069185).


## (Đã ngừng hỗ trợ) Tạo video danh mục bằng mẫu tùy chỉnh (`(Deprecated) Create catalog videos using custom templates`)
<a id="doc-1754263135747073"></a>
<!-- doc_id: 1754263135747073 -->

> Đường dẫn: Marketing API > Catalog Management > Guides > (Deprecated) Create catalog videos using custom templates

Video danh mục có thể là video mẫu giới thiệu các sản phẩm được liệt kê trong danh mục của nhà quảng cáo. Bài viết này hướng dẫn cách tạo và quản lý video danh mục bằng cách sử dụng các mẫu tùy chỉnh.

1. Sử dụng endpoint [/catalog/template/upload/](../12-api-reference/31-catalog-video-templates.md#doc-1740665346584577) để tải mẫu video tùy chỉnh lên và liên kết với danh mục. Xem [Hướng dẫn thiết kế mẫu tùy chỉnh](https://bytedance.feishu.cn/docs/doccnGxGlxEVZVhvGWyq17QTKNe) để tìm hiểu cách thiết kế mẫu video. Trong mẫu video tùy chỉnh, các lớp hình ảnh và lớp văn bản cần được đặt tên theo định dạng được TikTok hỗ trợ. Xem chi tiết tại [Hướng dẫn đặt tên lớp](catalog.md#doc-1739470990574594).
2. Sử dụng endpoint [/catalog/video_package/create/](../12-api-reference/31-catalog-video-templates.md#doc-1740665273039873) để tạo gói video loại phông xanh (green screen). Gói video là nhóm các video bạn có thể sử dụng trực tiếp trong quảng cáo, chẳng hạn như Shopping Ads. Xem [Tạo gói video](catalog.md#doc-1739470992872450) để biết các tài liệu cần thiết và các bước cụ thể. Mã `shopping_ads_video_template_id` sẽ được trả về trong phản hồi.
3. Nếu bạn muốn sử dụng video danh mục để tạo quảng cáo, hãy sử dụng endpoint [/ad/create/](../12-api-reference/02-ads-p1.md#doc-1739953377508354) và truyền giá trị `shopping_ads_video_template_id` nhận được từ Bước 2 vào trường `shopping_ads_video_package_id`.
4. Nếu bạn muốn quản lý video danh mục, bạn có thể sử dụng các endpoint sau:
   - Để lấy thông tin về tất cả video danh mục thuộc Business Center, sử dụng [/catalog/video_package/get/](../12-api-reference/31-catalog-video-templates.md#doc-1740574099715073).
   - Để cập nhật tên gói video, sử dụng [/catalog/video_package/update/](../12-api-reference/31-catalog-video-templates.md#doc-1740665303669761).
   - Để xóa gói video, sử dụng [/catalog/video_package/delete/](../12-api-reference/31-catalog-video-templates.md#doc-1740665332455426).

## (Đã ngừng hỗ trợ) Tạo gói video (`(Deprecated) Create a video package`)
<a id="doc-1739470992872450"></a>
<!-- doc_id: 1739470992872450 -->

> Đường dẫn: Marketing API > Catalog Management > Guides > (Deprecated) Create catalog videos using custom templates > (Deprecated) Create a video package

Gói video là một nhóm các video mà bạn có thể sử dụng trực tiếp trong quảng cáo của mình (ví dụ Shopping Ads). Bạn có thể tạo gói video loại phông xanh bằng TikTok API for Business.

### Tài nguyên cần chuẩn bị (Materials needed)

Để tạo gói video phông xanh, bạn cần chuẩn bị các tài nguyên sau:
* Một video phông xanh (green screen video).
* Một vài video thông thường.
* Một mẫu video (video template).
* Một tệp nhạc nền.

Bạn sẽ cần ID của các tài nguyên này (`video_id`, `template_id` và `music_id`) để tạo gói video:
* Sử dụng endpoint [/file/video/ad/upload/](../12-api-reference/71-video.md#doc-1737587322856449) để tải video lên.
* Sử dụng endpoint **/catalog/template/upload/** để tải mẫu video lên.
* Sử dụng endpoint [/file/music/upload/](../12-api-reference/52-music.md#doc-1740052650395650) để tải nhạc lên.

### Thông số kỹ thuật của tài nguyên (Specifications of the materials)

* Bạn chỉ được phép có duy nhất một video phông xanh.
* Thời lượng tối đa của video phông xanh là 20 giây.
* Video phông xanh phải dài hơn mẫu video.
* Thời lượng của tệp nhạc phải dài hơn độ dài của video kết hợp.
* Độ phân giải tối đa cho mẫu video là 720×1280.
* Đối với phần phông xanh trong video, giá trị R và B trong mô hình màu RGB phải nhỏ hơn 120, và giá trị G phải lớn hơn 150. Giá trị sắc độ (hue) trong không gian màu HSV phải lớn hơn 70 và nhỏ hơn 154 (ví dụ: RGB 50, 217, 70).

### Tạo gói video (Creating a video package)

Gửi yêu cầu POST tới endpoint [/catalog/video_package/create/](../12-api-reference/31-catalog-video-templates.md#doc-1740665273039873) với các thiết lập:
* Đặt `video_package_type` thành `GREEN_SCREEN`.
* Truyền giá trị cho `template_id` và `music_id`.
* Bao gồm dữ liệu về các video trong một đối tượng. Thứ tự của các video trong đối tượng sẽ quyết định thứ tự xuất hiện trong gói video tạo ra.
* Đối với video phông xanh duy nhất, đặt `is_green_screen_video` thành `true`. Đối với các video còn lại, đặt thành `false`.

Sau khi gói video được tạo, bạn có thể cập nhật tên, xem trước hoặc xóa nó.

## (Đã ngừng hỗ trợ) Hướng dẫn đặt tên lớp (`(Deprecated) Layer naming guidelines`)
<a id="doc-1739470990574594"></a>
<!-- doc_id: 1739470990574594 -->

> Đường dẫn: Marketing API > Catalog Management > Guides > (Deprecated) Create catalog videos using custom templates > (Deprecated) Layer naming guidelines

Bài viết này mô tả cách đặt tên cho các lớp (layers) trong mẫu tùy chỉnh cho video quảng cáo (chẳng hạn như Shopping Ads).

Hình ảnh và văn bản trong mẫu video sẽ được thay thế bằng thông tin sản phẩm thực tế (như giá bán hoặc ảnh sản phẩm) khi quảng cáo được triển khai. Nếu sử dụng mẫu video tùy chỉnh, người thiết kế cần xác định phần nào có thể thay thế và đặt tên các lớp hình ảnh, lớp văn bản trong Adobe After Effects theo định dạng được TikTok hỗ trợ.

### Các lớp hình ảnh (Image layers)

Tên lớp hình ảnh có định dạng `product_image_x`, trong đó `x` là số biểu thị thứ tự hình ảnh. TikTok sẽ thay thế `product_image_1` bằng ảnh chính của sản phẩm. Các hình ảnh bổ sung sẽ thay thế tuần tự các lớp tiếp theo (`product_image_2`, `product_image_3`...).

| Từ khóa sản phẩm | Tên lớp Adobe After Effects |
|---|---|
| Product image 1 | `product_image_1` |
| Product image 2 | `product_image_2` |
| product_image_3 | `product_image_3` |
| product_image_4 | `product_image_4` |

### Các lớp văn bản (Text layers)

Có các từ khóa chính trong danh mục cần được đặt tên lớp tương ứng để TikTok nhận diện và thay thế bằng dữ liệu thực tế:

| Từ khóa sản phẩm | Tên lớp Adobe After Effects |
|---|---|
| Price | `price` |
| Sale Price | `sale_price` |
| Product Name | `product_name` |
| description | `description` |
| brand | `brand` |
| custom_label_0 | `custom_label_0` |
| custom_label_1 | `custom_label_1` |
| custom_label_2 | `custom_label_2` |
| custom_label_3 | `custom_label_3` |
| custom_label_4 | `custom_label_4` |

## Quản lý danh mục trong Business Center (`Manage catalogs in a Business Center`)
<a id="doc-1738964064361474"></a>
<!-- doc_id: 1738964064361474 -->

> Đường dẫn: Marketing API > Catalog Management > Guides > Manage catalogs in a Business Center

Bài viết này thảo luận về cách quản lý danh mục sản phẩm dưới dạng tài sản thuộc Business Center.

Hiện tại, danh mục được quản lý như một tài sản trong Business Center. Để quản lý danh mục, các nhà phát triển cần đảm bảo rằng các danh mục đã được di chuyển vào Business Center. Nếu chưa, nhà phát triển cần di chuyển danh mục vào Business Center trước, sau đó quản lý chúng qua các endpoint Catalog API.

### Các tình huống phổ biến (Common scenarios)

#### Tình huống 1: Nhà phát triển muốn quản lý danh mục của chính mình (danh mục tạo dưới tài khoản quảng cáo của họ)
- **Danh mục đã chuyển sang Business Center chưa?**
  - **Đã chuyển:** Sử dụng trực tiếp các endpoint Catalog API để tạo/sửa/xóa/lấy danh mục.
  - **Chưa chuyển:** Di chuyển danh mục sang Business Center, sau đó bắt đầu quản lý. Xem quy trình di chuyển bên dưới.

#### Tình huống 2: Nhà phát triển muốn quản lý danh mục của người khác (tạo dưới tài khoản quảng cáo khác)
1. Yêu cầu chủ sở hữu danh mục di chuyển danh mục sang Business Center.
2. Yêu cầu Quản trị viên (Admin) của Business Center thêm nhà phát triển vào Business Center này.
3. Yêu cầu Quản trị viên Business Center phân quyền quản lý danh mục cho nhà phát triển qua giao diện Business Center hoặc gọi endpoint [/bc/asset/assign/](../12-api-reference/15-bc-assets.md#doc-1739438211077121).
4. Quản lý danh mục dưới dạng tài sản Business Center.

#### Tình huống 3: Nhà phát triển muốn quản lý danh mục của mình nhưng không phải Admin của Business Center
- Nếu nhà phát triển được chỉ định làm Admin của Business Center, họ có thể di chuyển và quản lý danh mục như Tình huống 1.
- Nếu không thể trở thành Admin của Business Center đó, nhà phát triển nên tạo Business Center riêng của mình và di chuyển danh mục vào đó.

### Di chuyển danh mục vào Business Center (Migrate catalogs to a Business Center)

#### Điều kiện tiên quyết:
* Bạn là Quản trị viên (Admin) của Business Center.
* Bạn là chủ sở hữu của tài khoản quảng cáo mà danh mục sản phẩm đang thuộc về.

#### Quy trình di chuyển:
1. Sử dụng endpoint [/catalog/capitalize/](../12-api-reference/25-catalog-management.md#doc-1740490222539778) để chuyển đổi danh mục sản phẩm (bao gồm sản phẩm, bộ sản phẩm và mẫu video) thành tài sản thuộc Business Center của bạn.
2. Sử dụng [/bc/asset/get/](../12-api-reference/15-bc-assets.md#doc-1739432717798401) để xác minh dữ liệu danh mục đã được di chuyển thành công (đặt `asset_type` thành `CATALOG`).

### Quản lý danh mục sau khi di chuyển

* **Lấy tất cả danh mục trong Business Center:** Sử dụng [/bc/asset/get/](../12-api-reference/15-bc-assets.md#doc-1739432717798401) và đặt `asset_type` thành `CATALOG`.
* **Thực hiện các thao tác quản trị:** Các endpoint API không thay đổi, điểm khác biệt duy nhất là bạn cần truyền thêm tham số `bc_id` trong yêu cầu.
* **Tra cứu quốc gia/khu vực danh mục có thể phân phối:** Sử dụng [/catalog/available_countries/get/](../12-api-reference/25-catalog-management.md#doc-1740491257516034) và chỉ định `bc_id`.
* **Xem trước quảng cáo:** Chỉ định `bc_id` khi xem trước quảng cáo có gắn danh mục bằng [/creative/ads_preview/create/](../12-api-reference/38-creative-tools.md#doc-1739403070695426).
* **Tạo hoặc cập nhật nhóm quảng cáo:** Chỉ định `catalog_authorized_bc_id` trong [/adgroup/create/](../12-api-reference/07-ad-groups-p2.md#doc-1739499616346114) hoặc [/adgroup/update/](../12-api-reference/07-ad-groups-p3.md#doc-1739586761631745).

## Sử dụng danh mục khi tạo Quảng cáo Mua sắm (`Use catalogs when creating Shopping Ads`)
<a id="doc-1754263154550786"></a>
<!-- doc_id: 1754263154550786 -->

> Đường dẫn: Marketing API > Catalog Management > Guides > Use catalogs when creating Shopping Ads

Quảng cáo Mua sắm (Shopping Ads) là giải pháp quảng cáo trả phí được vận hành dựa trên danh mục sản phẩm, giúp tối ưu hóa hiệu quả thúc đẩy doanh số thông qua mục tiêu mua hàng duy nhất — Doanh số sản phẩm (Product Sales).

**Quy trình từng bước:**

1. Tạo chiến dịch quảng cáo bằng [/campaign/create/](../12-api-reference/24-campaign.md#doc-1739318962329602).
2. Tạo và quản lý danh mục bằng Catalog API:
   - Tạo danh mục bằng [/catalog/create/](../12-api-reference/25-catalog-management.md#doc-1740306481704961).
   - Tải sản phẩm lên danh mục bằng [/catalog/product/file/](../12-api-reference/28-catalog-products-p1.md#doc-1740496787164161) hoặc [/catalog/product/upload/](../12-api-reference/28-catalog-products-p1.md#doc-1740497429681153).
   - Mời thành viên vào Business Center và cấp quyền quản trị bằng [/bc/member/invite/](../12-api-reference/19-bc-members.md#doc-1739939455765505).
   - Chia sẻ danh mục cho thành viên và cấp quyền quản lý bằng [/bc/asset/assign/](../12-api-reference/15-bc-assets.md#doc-1739438211077121) (`asset_type` là `CATALOG`, `catalog_role` là `ADMIN`).
3. Tạo nhóm quảng cáo bằng [/adgroup/create/](../12-api-reference/07-ad-groups-p2.md#doc-1739499616346114).
4. Tạo quảng cáo bằng [/ad/create/](../12-api-reference/02-ads-p1.md#doc-1739953377508354).
5. Xem trước quảng cáo sau khi tạo bằng [/creative/ads_preview/create/](../12-api-reference/38-creative-tools.md#doc-1739403070695426).

## Tham chiếu API (`API reference`)
<a id="doc-1739578477445121"></a>
<!-- doc_id: 1739578477445121 -->

> Đường dẫn: Marketing API > Catalog Management > API reference

Catalog API bao gồm các nhóm endpoint sau:

### Quản lý danh mục (Catalog Management)
* [Tạo danh mục (Create a catalog)](../12-api-reference/25-catalog-management.md#doc-1740306481704961)
* [Cập nhật tên danh mục (Update the name of a catalog)](../12-api-reference/25-catalog-management.md#doc-1740306544966657)
* [Xóa danh mục (Delete a catalog)](../12-api-reference/25-catalog-management.md#doc-1740310064588801)
* [Lấy danh sách danh mục (Get catalogs)](../12-api-reference/25-catalog-management.md#doc-1740315452868610)
* [Lấy danh sách từ điển danh mục (Get the lexicon list for a catalog)](../12-api-reference/25-catalog-management.md#doc-1740488375815169)
* [Di chuyển danh mục sang Business Center (Migrate a catalog to a BC)](../12-api-reference/25-catalog-management.md#doc-1740490222539778)
* [Lấy các khu vực khả dụng (Get available regions)](../12-api-reference/25-catalog-management.md#doc-1740491257516034)
* [Lấy địa điểm và tiền tệ (Get locations and currencies)](../12-api-reference/25-catalog-management.md#doc-1740491571747841)
* [Lấy tổng quan về danh mục (Get the overview of a catalog)](../12-api-reference/25-catalog-management.md#doc-1740492470201345)

### Nguồn sự kiện danh mục (Catalog Event Sources)
* [Liên kết nguồn sự kiện với danh mục (Bind an event source to a catalog)](../12-api-reference/26-catalog-event-sources.md#doc-1740492491200513)
* [Hủy liên kết nguồn sự kiện khỏi danh mục (Unbind an event source from a catalog)](../12-api-reference/26-catalog-event-sources.md#doc-1740492512449538)
* [Lấy thông tin liên kết nguồn sự kiện của danh mục (Get event source binding info of a catalog)](../12-api-reference/26-catalog-event-sources.md#doc-1740492531343362)

### Nguồn cấp dữ liệu danh mục (Catalog Feeds)
* [Tạo nguồn cấp dữ liệu (Create a feed)](../12-api-reference/27-catalog-feeds.md#doc-1740665161957377)
* [Lấy danh sách nguồn cấp dữ liệu (Get feeds)](../12-api-reference/27-catalog-feeds.md#doc-1740665183073281)
* [Cập nhật nguồn cấp dữ liệu (Update a feed)](../12-api-reference/27-catalog-feeds.md#doc-1740665197662210)
* [Xóa nguồn cấp dữ liệu (Delete a feed)](../12-api-reference/27-catalog-feeds.md#doc-1740665210863617)
* [Lấy nhật ký nguồn cấp dữ liệu (Get the log of a feed)](../12-api-reference/27-catalog-feeds.md#doc-1740665225631810)
* [Cập nhật trạng thái lịch trình nguồn cấp dữ liệu (Update the schedule status of a feed)](../12-api-reference/27-catalog-feeds.md#doc-1750349624999937)

### Video danh mục (Catalog Videos)
* [Tải lên video danh mục qua URL tệp (Upload catalog videos via a file URL)](../12-api-reference/30-catalog-videos.md#doc-1803655037415489)
* [Lấy nhật ký xử lý video danh mục (Get the catalog video handling log)](../12-api-reference/30-catalog-videos.md#doc-1803655061642242)
* [Lấy danh sách video danh mục đã tải lên (Get the uploaded catalog videos within a catalog)](../12-api-reference/30-catalog-videos.md#doc-1803655082498050)
* [Xóa video danh mục đã tải lên (Delete uploaded catalog videos)](../12-api-reference/30-catalog-videos.md#doc-1803655103069185)

### Mẫu video danh mục (Catalog Video Templates)
* [Lấy danh sách gói video (Get video packages)](../12-api-reference/31-catalog-video-templates.md#doc-1740574099715073)

### Bộ sản phẩm (Product Sets)
* [Lấy danh sách bộ sản phẩm (Get product sets)](../12-api-reference/29-catalog-product-sets.md#doc-1740570556295169)
* [Lấy danh sách sản phẩm trong bộ sản phẩm (Get products in product set)](../12-api-reference/29-catalog-product-sets.md#doc-1740571478441986)
* [Tạo bộ sản phẩm theo điều kiện (Create a product set by conditions)](../12-api-reference/29-catalog-product-sets.md#doc-1740572891104257)
* [Tạo bộ sản phẩm theo tệp (Create a product set by file)](../12-api-reference/29-catalog-product-sets.md#doc-1846770644217858)
* [Cập nhật bộ sản phẩm (Update a product set)](../12-api-reference/29-catalog-product-sets.md#doc-1740572974725122)
* [Xóa bộ sản phẩm (Delete product sets)](../12-api-reference/29-catalog-product-sets.md#doc-1740573143966722)

### Sản phẩm (Products)
* [Tải lên sản phẩm qua URL tệp CSV (Upload products via a file URL)](../12-api-reference/28-catalog-products-p1.md#doc-1740496787164161)
* [Tải lên sản phẩm qua lược đồ JSON (Upload products via a JSON schema)](../12-api-reference/28-catalog-products-p1.md#doc-1740497429681153)
* [Cập nhật sản phẩm (Update products)](../12-api-reference/28-catalog-products-p2.md#doc-1740562287852546)
* [Xóa sản phẩm (Remove products)](../12-api-reference/28-catalog-products-p2.md#doc-1740562489236481)
* [Lấy danh sách sản phẩm (Get products)](../12-api-reference/28-catalog-products-p2.md#doc-1740564136678402)
* [Lấy nhật ký xử lý sản phẩm (Get the product handling log)](../12-api-reference/28-catalog-products-p3.md#doc-1740570027173889)

### Chẩn đoán danh mục (Catalog Diagnostics)
* [Lấy thông tin chẩn đoán danh mục đồng bộ (Get synchronous catalog diagnostic information)](../12-api-reference/32-catalog-diagnostics.md#doc-1771117232728066)
* [Tạo tác vụ tải tệp chẩn đoán danh mục bất đồng bộ (Create an asynchronous download task for catalog diagnostic information)](../12-api-reference/32-catalog-diagnostics.md#doc-1771117279175682)
* [Tải xuống thông tin chẩn đoán danh mục bất đồng bộ (Download asynchronous catalog diagnostic information)](../12-api-reference/32-catalog-diagnostics.md#doc-1771117294731266)

### Thông tin chi tiết danh mục (Catalog Insights)
* [Lấy bộ lọc cho thông tin chi tiết sản phẩm danh mục (Get filters for catalog product insights)](../12-api-reference/33-catalog-insights.md#doc-1805640864553985)
* [Lấy sản phẩm danh mục đang thịnh hành (Get trending catalog products)](../12-api-reference/33-catalog-insights.md#doc-1805640886872066)
* [Lấy danh mục sản phẩm thịnh hành (Get trending catalog product categories)](../12-api-reference/33-catalog-insights.md#doc-1805640900563969)
