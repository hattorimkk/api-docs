# Sản phẩm Catalog — phần 2/3

Tài liệu này bao gồm các đặc tả API quản lý sản phẩm trong danh mục sản phẩm (Catalog Products) của TikTok Business API:
- Cập nhật sản phẩm (`Update products`)
- Xóa sản phẩm (`Remove products`)
- Lấy thông tin sản phẩm (`Get products`)

---

## Cập nhật sản phẩm (`Update products`)
<a id="doc-1740562287852546"></a>
<!-- doc_id: 1740562287852546 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/catalog/product/update/`

> **Đường dẫn**: API Reference > Catalog Products > Update products

**Mục đích**: Sử dụng endpoint này để cập nhật hàng loạt sản phẩm trong catalog, tối đa 5.000 sản phẩm trong một lần gọi. Các sản phẩm được chỉ định trong yêu cầu sẽ được cập nhật bất đồng bộ, và bạn sẽ nhận được một ID tác vụ xử lý là `feed_log_id`. Với ID này, bạn có thể kiểm tra trạng thái xử lý thông qua endpoint [/catalog/product/log/](28-catalog-products-p3.md#doc-1740570027173889).

Khác với [/catalog/product/file/](28-catalog-products-p1.md#doc-1740496787164161), endpoint này chủ yếu được dùng để cập nhật số lượng sản phẩm nhỏ và cập nhật một số trường dữ liệu nhất định.

> [!NOTE]
> • Mã SKU là duy nhất trong cùng một catalog E-commerce và chỉ thuộc về một feed nhất định. Mọi thao tác đối với SKU cần được thực hiện dưới feed mà nó trực thuộc.<br>
> • Bạn có thể thực hiện tối đa 1.000 yêu cầu mỗi giờ cho mỗi catalog sản phẩm.<br>
> • Hỗ trợ cập nhật tăng dần (incremental updates).

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
| products | object[] | **Bắt buộc**. Danh sách các sản phẩm cần cập nhật. Đối với các trường dữ liệu trong mảng này, xem mục **"Tham số mảng đối tượng `products`"** bên dưới. Tối đa 5.000 sản phẩm mỗi yêu cầu. |

### Tham số mảng đối tượng `products` (`products` object array parameters)
Các tham số trong mảng đối tượng `products` thay đổi tùy theo loại catalog bạn muốn cập nhật. Bạn có thể xác định loại của catalog dựa trên `catalog_type` trả về từ [/catalog/get/](25-catalog-management.md#doc-1740315452868610). Tham khảo các danh sách tham số chi tiết cho từng loại catalog bên dưới.

#### Tham số mảng đối tượng `products` cho catalog E-commerce

| Field | Data Type | Description |
|---|---|---|
| products | object[] | **Bắt buộc**. Danh sách các sản phẩm bạn muốn cập nhật. Tối đa: 5.000. |
| ↳ sku_id | string | **Bắt buộc**. ID duy nhất cho sản phẩm, chẳng hạn như SKU. Sử dụng cùng ID để cập nhật đúng sản phẩm trong feed ban đầu. Giới hạn: 100 ký tự và không chứa emoji. Ví dụ: `TikTok_item_1234`. Không hỗ trợ trùng SKU ID. |
| ↳ title | string | Tiêu đề của sản phẩm. Sử dụng ký tự Unicode hợp lệ. Không chứa nội dung quảng cáo như "miễn phí vận chuyển, chất lượng cao, bán buôn". Giới hạn: 500 ký tự và không chứa emoji. Ví dụ: `T-Shirt (Unisex)`. |
| ↳ description | string | Mô tả ngắn về sản phẩm. Giới hạn: 10.000 ký tự. Ví dụ: `A vibrant crewneck for all shapes and sizes. Made from 100% cotton.` |
| ↳ availability | string | Tình trạng tồn kho hiện tại của sản phẩm.<br>Giá trị enum:<br>• `IN_STOCK`: còn hàng.<br>• `AVAILABLE_FOR_ORDER`: có sẵn để đặt hàng.<br>• `PREORDER`: đặt trước.<br>• `OUT_OF_STOCK`: hết hàng.<br>• `DISCONTINUED`: ngừng kinh doanh. Ví dụ: `IN_STOCK`. |
| ↳ brand | string | Tên thương hiệu của sản phẩm. Giới hạn: 150 ký tự. Ví dụ: `TikTok`. |
| ↳ image_url | string | URL hình ảnh sản phẩm. Kích thước tối thiểu 500x500 px, định dạng JPG hoặc PNG. Chi tiết xem [Yêu cầu hình ảnh sản phẩm](../09-marketing-api/catalog.md#doc-1739578479392770). Ví dụ: `https://www.tiktok.com/t_shirt_image_001.jpg`. |
| ↳ additional_image_urls | string[] | Danh sách URL hình ảnh bổ sung. Tối đa: 10 URL. Kích thước tối thiểu 500x500 px. Nếu URL chứa dấu phẩy (,), hãy mã hóa URL thành `%2C`. Ví dụ: `["https://www.tiktok.com/t_shirt_image_002.jpg","https://www.tiktok.com/t_shirt_image_003.jpg"]`. |
| ↳ video_url | string | URL video sử dụng trong quảng cáo. Khuyến nghị: tỷ lệ 9:16 (dọc), độ phân giải ≥720*1280, bitrate ≥516kbps, có âm thanh kèm phụ đề. Ví dụ: `https://www.tiktok.com/tiktok_t_shirt`. |
| ↳ item_group_id | string | SPU ID của sản phẩm. Dùng chung `item_group_id` cho các biến thể của cùng một sản phẩm. Ví dụ: `TikTok_1234_sample`. |
| ↳ google_product_category | string | Danh mục sản phẩm theo Google product taxonomy (tối đa 3 cấp). Ví dụ: `Apparel & Accessories > Clothing > Shirts`. |
| ↳ global_trade_item_number | string | Mã số thương phẩm toàn cầu (GTIN) của sản phẩm. Ví dụ: `3234567890126`. |
| ↳ manufacturer_part_number | string | Mã số bộ phận của nhà sản xuất (MPN). Ví dụ: `12433`. |
| ↳ product_detail | object | Thông tin chi tiết khác của sản phẩm. |
| ↳↳ condition | string | Tình trạng hiện tại của sản phẩm. Giá trị enum: `NEW` (mới), `REFURBISHED` (tân trang), `USED` (đã qua sử dụng). Ví dụ: `NEW`. |
| ↳↳ age_group | string | Độ tuổi mục tiêu của sản phẩm.<br>Giá trị enum: `NEW_BORN`, `INFANT`, `TODDLER`, `KIDS`, `ADULT`. Ví dụ: `ADULT`. |
| ↳↳ color | string | Màu sắc sản phẩm. Giới hạn: 100 ký tự. Ví dụ: `blue`. |
| ↳↳ gender | string | Giới tính mục tiêu. Giá trị enum: `MALE`, `FEMALE`, `UNISEX`. Ví dụ: `UNISEX`. |
| ↳↳ material | string | Chất liệu sản phẩm (cotton, denim, leather...). Giới hạn: 200 ký tự. Ví dụ: `cotton`. |
| ↳↳ pattern | string | Họa tiết hoặc hình in. Giới hạn: 100 ký tự. Ví dụ: `stripes1`. |
| ↳↳ product_category | string | Danh mục sản phẩm (yêu cầu 3 cấp đầu tiên). Ví dụ: `Apparel & Accessories > Clothing > Shirts`. |
| ↳↳ shipping | string | Thông tin vận chuyển. Định dạng khuyến nghị: `COUNTRY:STATE:SHIPPING_TYPE:PRICE`. Ví dụ: `US:CA:Ground:9.99 USD`. |
| ↳↳ shipping_weight | string | Trọng lượng vận chuyển. Đơn vị hợp lệ: `lb`, `oz`, `g`, `kg`. Ví dụ: `1 oz`, `1 kg`. |
| ↳↳ size | string | Kích thước sản phẩm. Ví dụ: `Small`, `Large`, `Extra Large`. |
| ↳↳ tax | string | Mức thuế của sản phẩm. |
| ↳ price_info | object | Thông tin giá sản phẩm. |
| ↳↳ price | float | Giá cơ sở của sản phẩm. Ví dụ: `30`. |
| ↳↳ currency | string | Đơn vị tiền tệ. Theo quốc gia mục tiêu của catalog. Ví dụ: `USD`. |
| ↳↳ sale_price | float | Giá khuyến mãi giảm giá của sản phẩm nếu đang giảm giá. Ví dụ: `20`. |
| ↳↳ sale_price_effective_date | string | Thời gian áp dụng giá khuyến mãi, định dạng `YYYY-MM-DDT23:59+00:00/YYYY-MM-DDT23:59+00:00`. Ví dụ: `2023-12-11T23:59+00:00/2023-12-15T23:59+00:00`. |
| ↳ landing_page | object | Thông tin trang đích. |
| ↳↳ landing_page_url | string | URL của trang đích xem và mua sản phẩm. Ví dụ: `https://www.tiktok.com/tiktok_t_shirt`. |
| ↳↳ ios_url | string | Custom scheme URL cho iOS. Ví dụ: `iOS://electronic`. |
| ↳↳ ios_app_store_id | string | App Store ID cho iOS. Ví dụ: `1234`. |
| ↳↳ ios_app_name | string | Tên ứng dụng iOS. Ví dụ: `Electronic iOS`. |
| ↳↳ iphone_app_store_id | string | App Store ID cho iPhone. Ví dụ: `1234`. |
| ↳↳ iphone_app_name | string | Tên ứng dụng iPhone. Ví dụ: `Electronic iOS`. |
| ↳↳ ipad_app_store_id | string | App Store ID cho iPad. Ví dụ: `1234`. |
| ↳↳ ipad_app_name | string | Tên ứng dụng iPad. Ví dụ: `Electronic iOS`. |
| ↳↳ android_url | string | Custom scheme URL cho Android. Ví dụ: `android://electronic`. |
| ↳↳ android_package | string | Tên gói Android package name. Ví dụ: `com.electronic`. |
| ↳↳ android_app_name | string | Tên ứng dụng Android. Ví dụ: `Electronic Android`. |
| ↳ extra_info | object | Thông tin bổ sung. |
| ↳↳ custom_label_0 | string | Nhãn tùy chỉnh bổ sung. Không giới hạn độ dài. |
| ↳↳ custom_label_1 | string | Nhãn tùy chỉnh bổ sung. Không giới hạn độ dài. |
| ↳↳ custom_label_2 | string | Nhãn tùy chỉnh bổ sung. Không giới hạn độ dài. |
| ↳↳ custom_label_3 | string | Nhãn tùy chỉnh bổ sung. Không giới hạn độ dài. |
| ↳↳ custom_label_4 | string | Nhãn tùy chỉnh bổ sung. Không giới hạn độ dài. |

#### Tham số mảng đối tượng `products` cho catalog khách sạn (hotel)

| Field | Data Type | Description |
|---|---|---|
| products | object[] | **Bắt buộc**. Danh sách các sản phẩm (phòng khách sạn) bạn muốn cập nhật. Tối đa: 5.000. |
| ↳ hotel_id | string | **Bắt buộc**. ID duy nhất cho khách sạn. Giới hạn: 100 ký tự. |
| ↳ name | string | Tên của khách sạn. Giới hạn: 150 ký tự. |
| ↳ description | string | Mô tả ngắn về phòng khách sạn. Giới hạn: 10.000 ký tự. Ví dụ: `Free Wifi, Free Breakfast, Free Cancellation`. |
| ↳ availability | string | Tình trạng phòng hiện tại: `IN_STOCK` (có sẵn để đặt), `OUT_OF_STOCK` (hết phòng). Ví dụ: `IN_STOCK`. |
| ↳ brand | string | Tên thương hiệu khách sạn. Giới hạn: 150 ký tự. |
| ↳ image_url | string | URL hình ảnh phòng khách sạn. Kích thước tối thiểu 500x500 px, định dạng JPG hoặc PNG. Chi tiết xem [Yêu cầu hình ảnh](../09-marketing-api/catalog.md#doc-1739578479392770). Ví dụ: `https://www.tiktok.com/hotel_room_image_001.jpg`. |
| ↳ additional_image_urls | string[] | Danh sách URL hình ảnh bổ sung. Tối đa: 20 URL. Kích thước ≥ 500x500 px. Nếu có dấu phẩy, mã hóa thành `%2C`. Ví dụ: `["https://www.tiktok.com/hotel_room_image_002.jpg","https://www.tiktok.com/hotel_room_image_003.jpg"]`. |
| ↳ video_url | string | URL video sử dụng trong quảng cáo. Khuyến nghị: 9:16 (dọc), ≥720*1280, ≥516kbps, có âm thanh kèm phụ đề. Ví dụ: `https://www.tiktok.com/hotel.mp4`. |
| ↳ hotel_category | string[] | Danh mục khách sạn. Tối đa: 3 giá trị. Xem bảng giá trị cho `hotel_category` bên dưới. |
| ↳ hotel_retailer_id | string | ID duy nhất cho nhà bán lẻ/đại lý khách sạn. Giới hạn: 100 ký tự. |
| ↳ address | object | Thông tin địa chỉ khách sạn. |
| ↳↳ address | string | Tên đầy đủ của địa chỉ đường phố chính của khách sạn. Giới hạn: 150 ký tự. |
| ↳↳ secondary_address | string | Địa chỉ đường phố phụ của khách sạn. Giới hạn: 150 ký tự. |
| ↳↳ tertiary_address | string | Địa chỉ đường phố cấp 3 của khách sạn. Giới hạn: 150 ký tự. |
| ↳↳ city | string | Thành phố nơi khách sạn tọa lạc. Giới hạn: 150 ký tự. |
| ↳↳ region | string | Khu vực (bang/tỉnh) nơi khách sạn tọa lạc. Giới hạn: 150 ký tự. |
| ↳↳ country | string | Quốc gia nơi khách sạn tọa lạc. Giới hạn: 150 ký tự. |
| ↳ neighborhood | string | Khu vực lân cận của khách sạn. Giới hạn: 100 ký tự. Ví dụ: `Bangkok Old Town`. |
| ↳ postal_code | string | Mã bưu chính hoặc mã zip của khách sạn. Giới hạn: 150 ký tự. |
| ↳ latitude | float | Vĩ độ vị trí khách sạn. Phạm vi: [-90, 90]. Ví dụ: `37.484100`. |
| ↳ longitude | float | Kinh độ vị trí khách sạn. Phạm vi: [-180, 180]. Ví dụ: `-122.148252`. |
| ↳ margin_level | integer | Tỷ lệ phần trăm trên giá cơ sở (`price`) mà khách sạn thu làm tiền đặt cọc. Phạm vi: [1, 10]. |
| ↳ loyalty_program | string | Chương trình khách hàng thân thiết của khách sạn. Xem bảng giá trị cho `loyalty_program` bên dưới. |
| ↳ guest_ratings | object[] | Thông tin đánh giá của khách lưu trú. Tối đa: 1 đối tượng. |
| ↳↳ rating_system | string | Hệ thống đánh giá khách sạn. Giới hạn: 150 ký tự. Ví dụ: `Expedia`, `Tripadvisor`. |
| ↳↳ max_score | integer | Điểm số cao nhất của hệ thống đánh giá. Phạm vi: [0, 100]. |
| ↳↳ score | float | Điểm số thực tế của khách sạn. Phạm vi: ≥ 0. |
| ↳↳ number_of_reviewers | integer | Số lượng khách đã gửi đánh giá. Phạm vi: ≥ 0. |
| ↳ star_rating | integer | Số sao khách sạn được xếp hạng bởi tổ chức chuyên nghiệp (thường tối đa 5 sao). |
| ↳ room_type | string[] | Các loại phòng khách sạn. Tối đa: 3 giá trị. Xem bảng giá trị cho `room_type` bên dưới. |
| ↳ priority | integer | Thứ tự ưu tiên của khách sạn. Phạm vi: 0-5. Mặc định: 0. |
| ↳ price_info | object | Thông tin giá phòng. |
| ↳↳ price | float | Giá cơ sở cho một đêm phòng khách sạn. Ví dụ: `30`. |
| ↳↳ currency | string | Đơn vị tiền tệ. Theo catalog. Ví dụ: `USD`. |
| ↳↳ sale_price | float | Giá khuyến mãi giảm giá cho một đêm phòng. Phải nhỏ hơn `price`. Ví dụ: `20`. |
| ↳ landing_page | object | Thông tin trang đích. |
| ↳↳ landing_page_url | string | URL trang đích xem và đặt phòng. Ví dụ: `https://www.tiktok.com/tiktok_hotel`. |
| ↳↳ ios_url | string | Custom scheme URL cho iOS. Ví dụ: `iOS://electronic`. |
| ↳↳ ios_app_store_id | string | App Store ID cho iOS. Ví dụ: `1234`. |
| ↳↳ ios_app_name | string | Tên ứng dụng iOS. Ví dụ: `Electronic iOS`. |
| ↳↳ android_url | string | Custom scheme URL cho Android. Ví dụ: `android://electronic`. |
| ↳↳ android_package | string | Tên gói Android. Ví dụ: `com.electronic`. |
| ↳↳ android_app_name | string | Tên ứng dụng Android. Ví dụ: `Electronic Android`. |
| ↳ extra_info | object | Thông tin bổ sung. |
| ↳↳ custom_label_0 | string | Nhãn tùy chỉnh bổ sung về sản phẩm. Không giới hạn độ dài. |
| ↳↳ custom_label_1 | string | Nhãn tùy chỉnh bổ sung về sản phẩm. Không giới hạn độ dài. |
| ↳↳ custom_label_2 | string | Nhãn tùy chỉnh bổ sung về sản phẩm. Không giới hạn độ dài. |
| ↳↳ custom_label_3 | string | Nhãn tùy chỉnh bổ sung về sản phẩm. Không giới hạn độ dài. |
| ↳↳ custom_label_4 | string | Nhãn tùy chỉnh bổ sung về sản phẩm. Không giới hạn độ dài. |
| ↳↳ internal_label_0 | string | Nhãn nội bộ gán cho khách sạn, dùng để lọc khi tạo bộ sản phẩm. Giới hạn: 100 ký tự. |
| ↳↳ internal_label_1 | string | Nhãn nội bộ thứ hai gán cho khách sạn. Giới hạn: 100 ký tự. |

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
| `COTTAGE` | Nhà thôn quê (Cottage) |
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
| products | object[] | **Bắt buộc**. Danh sách các chuyến bay bạn muốn cập nhật. Tối đa: 5.000. |
| ↳ origin_airport | string | **Bắt buộc**. Sân bay xuất phát của chuyến bay (mã 3 chữ cái IATA). Ví dụ: `AAR`. Không trùng cặp xuất phát/đích trong cùng catalog. |
| ↳ destination_airport | string | **Bắt buộc**. Sân bay đích đến của chuyến bay (mã 3 chữ cái IATA). Ví dụ: `ABD`. Không trùng cặp xuất phát/đích trong cùng catalog. |
| ↳ origin_city | string | Tên thành phố xuất phát. Giới hạn: 150 ký tự. |
| ↳ destination_city | string | Tên thành phố đích đến. Giới hạn: 150 ký tự. |
| ↳ description | string | Mô tả ngắn về chuyến bay. Giới hạn: 10.000 ký tự. |
| ↳ cabin_class | string | Hạng ghế chuyến bay: `FIRST_CLASS`, `FIRST_CLASS_SUITE`, `BUSINESS_CLASS`, `BUSINESS_CLASS_SUITE`, `COMFORT_CLASS`, `ECONOMY_CLASS`, `BASIC_ECONOMY`, `STANDARD_ECONOMY`, `PREMIUM_ECONOMY`, `LIE_FLAT_SEAT`, `CHARTER_CLASS`, `ELITE_CLASS`, `QUIET_CLASS`. |
| ↳ airline_company | string | Tên hãng hàng không vận hành: `AEROFLOT`, `AIR_FRANCE_KLM_GROUP`, `ALASKA_AIRLINES`, `ANA`, `AMERICAN_AIRLINES`, `BRITISH_AIRWAYS`, `CATHAY_PACIFIC`, `CHINA_SOUTHERN_AIRLINES`, `CHINA_EASTERN_AIRLINES`, `DELTA_AIR_LINES`, `EMIRATES`, `JAPAN_AIRLINES`, `JETBLUE_AIRWAYS`, `KLM_ROYAL_DUTCH_AIRLINES`, `LUFTHANSA_GROUP`, `QANTAS_AIRWAYS`, `QATAR_AIRWAYS`, `SINGAPORE_AIRLINES`, `SOUTHWEST_AIRLINES`, `TURKISH_AIRLINES`, `UNITED_AIRLINES`, `VIRGIN_ATLANTIC`. |
| ↳ image_url | string | URL hình ảnh chuyến bay. Kích thước tối thiểu 500x500 px, định dạng JPG hoặc PNG. Ví dụ: `https://www.tiktok.com/flight_image_001.jpg`. |
| ↳ additional_image_urls | string[] | Danh sách URL hình ảnh bổ sung. Tối đa: 20 URL. Kích thước ≥ 500x500 px. Nếu có dấu phẩy, mã hóa thành `%2C`. Ví dụ: `["https://www.tiktok.com/flight_image_002.jpg","https://www.tiktok.com/flight_image_003.jpg"]`. |
| ↳ video_url | string | URL video sử dụng trong quảng cáo. Khuyến nghị: 9:16 (dọc), ≥720*1280, ≥516kbps, có âm thanh và phụ đề. Ví dụ: `https://www.tiktok.com/flight.mp4`. |
| ↳ priority | integer | Độ ưu tiên của chuyến bay. Phạm vi: 0-5. Mặc định: 0. |
| ↳ price_info | object | Thông tin giá chuyến bay. |
| ↳↳ price | float | Giá cơ sở của chuyến bay. Ví dụ: `3000`. |
| ↳↳ currency | string | Đơn vị tiền tệ. Theo catalog. Ví dụ: `USD`. |
| ↳↳ sale_price | float | Giá khuyến mãi giảm giá. Phải nhỏ hơn `price`. Ví dụ: `2500`. |
| ↳ landing_page | object | Thông tin trang đích. |
| ↳↳ landing_page_url | string | URL trang đích đặt vé máy bay. Ví dụ: `https://www.tiktok.com/tiktok_flight`. |
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
| ↳↳ internal_label_0 | string | Nhãn nội bộ gán cho chuyến bay để lọc khi tạo bộ sản phẩm. Giới hạn: 100 ký tự. |
| ↳↳ internal_label_1 | string | Nhãn nội bộ thứ hai gán cho chuyến bay. Giới hạn: 100 ký tự. |

#### Tham số mảng đối tượng `products` cho catalog điểm đến du lịch (destination)

| Field | Data Type | Description |
|---|---|---|
| products | object[] | **Bắt buộc**. Danh sách các điểm đến du lịch bạn muốn cập nhật. Tối đa: 5.000. |
| ↳ destination_id | string | **Bắt buộc**. ID duy nhất cho điểm đến du lịch. Giới hạn: 100 ký tự. |
| ↳ destination_name | string | Tên của điểm đến du lịch. Giới hạn: 150 ký tự. |
| ↳ description | string | Mô tả ngắn về điểm đến. Giới hạn: 10.000 ký tự. Ví dụ: `A visit to one of the most famous sights in London.` |
| ↳ image_url | string | URL hình ảnh của điểm đến. Kích thước tối thiểu 500x500 px, định dạng JPG hoặc PNG. Ví dụ: `https://www.tiktok.com/destination_image_001.jpg`. |
| ↳ additional_image_urls | string[] | Danh sách URL hình ảnh bổ sung. Tối đa: 10 URL. Kích thước ≥ 500x500 px. Nếu có dấu phẩy, mã hóa thành `%2C`. Ví dụ: `["https://www.tiktok.com/destination_image_002.jpg","https://www.tiktok.com/destination_image_003.jpg"]`. |
| ↳ video_url | string | URL video sử dụng trong quảng cáo. Khuyến nghị: 9:16 (dọc), ≥720*1280, ≥516kbps, có âm thanh và phụ đề. Ví dụ: `https://www.tiktok.com/destination.mp4`. |
| ↳ address | object | Thông tin địa chỉ điểm đến. |
| ↳↳ address | string | Địa chỉ đường phố của điểm đến. Giới hạn: 150 ký tự. |
| ↳↳ city | string | Thành phố nơi điểm đến tọa lạc. Giới hạn: 150 ký tự. |
| ↳↳ region | string | Khu vực (bang/tỉnh) nơi điểm đến tọa lạc. Giới hạn: 150 ký tự. |
| ↳↳ country | string | Quốc gia nơi điểm đến tọa lạc. Giới hạn: 150 ký tự. |
| ↳ neighborhood | string | Khu vực lân cận của điểm đến. Giới hạn: 100 ký tự. Ví dụ: `Bangkok Old Town`. |
| ↳ postal_code | string | Mã bưu chính hoặc mã zip của điểm đến. |
| ↳ latitude | float | Vĩ độ của điểm đến. Phạm vi: [-90, 90]. Ví dụ: `37.484100`. |
| ↳ longitude | float | Kinh độ của điểm đến. Phạm vi: [-180, 180]. Ví dụ: `-122.148252`. |
| ↳ types | string[] | Loại hoặc các loại điểm đến du lịch (ví dụ: `["city","sightseeing"]`). Tối đa: 20 loại. |
| ↳ price_info | object | Thông tin giá điểm đến. |
| ↳↳ price | float | Giá trung bình hoặc thấp nhất cho điểm đến. Ví dụ: `30`. |
| ↳↳ currency | string | Đơn vị tiền tệ. Theo catalog. Ví dụ: `USD`. |
| ↳↳ sale_price | float | Giá khuyến mãi giảm giá cho điểm đến. Ví dụ: `20`. |
| ↳ landing_page | object | Thông tin trang đích. |
| ↳↳ landing_page_url | string | URL trang đích xem chi tiết điểm đến. Ví dụ: `https://www.tiktok.com/tiktok_destination`. |
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

#### Tham số mảng đối tượng `products` cho catalog giải trí (entertainment)

> [!NOTE]
> Catalog giải trí hiện là tính năng thử nghiệm trong danh sách cho phép (allowlist-only) và chỉ mở theo thư mời. Vui lòng liên hệ đại diện TikTok nếu muốn tiếp cận.

| Field | Data Type | Description |
|---|---|---|
| products | object[] | **Bắt buộc**. Danh sách các tựa phương tiện bạn muốn cập nhật. Tối đa: 5.000. |
| ↳ media_title_id | string | **Bắt buộc**. ID duy nhất cho mục tựa phương tiện (phim, TV show, âm nhạc...). Giới hạn: 100 ký tự. Ví dụ: `TIKTOKLIVE001`. |
| ↳ title | string | Tên của tựa phương tiện. Giới hạn: 150 ký tự. Ví dụ: `TikTok LIVE Series`. |
| ↳ description | string | Mô tả ngắn về tựa phương tiện. Giới hạn: 10.000 ký tự. |
| ↳ image_url | string | URL hình ảnh của tựa phương tiện. Kích thước tối thiểu 500x500 px, định dạng JPG hoặc PNG. Ví dụ: `https://www.tiktok.com/entertainment_image_001.jpg`. |
| ↳ video_url | string | URL video sử dụng trong quảng cáo. Khuyến nghị: 9:16 (dọc), ≥720x1280, ≥516kbps, có âm thanh và phụ đề. Ví dụ: `https://www.tiktok.com/tiktok_live_series`. |
| ↳ additional_image_urls | string[] | Danh sách URL hình ảnh bổ sung. Tối đa: 20 URL. Kích thước ≥ 500x500 px. Nếu có dấu phẩy, mã hóa thành `%2C`. Ví dụ: `["https://www.tiktok.com/entertainment_image_002.jpg","https://www.tiktok.com/entertainment_image_003.jpg"]`. |
| ↳ genres | string[] | Thể loại của tựa phương tiện. Tối đa: 2 thể loại. Xem danh sách giá trị cho `genres` bên dưới. Ví dụ: `TEEN`. |
| ↳ qid | string | QID (mã số Q trên Wikidata). Giới hạn: 150 ký tự. Ví dụ: `Q48938223`. |
| ↳ price_info | object | Thông tin giá của tựa phương tiện. |
| ↳↳ price | float | Giá của tựa phương tiện. Ví dụ: `30`. |
| ↳↳ currency | string | Đơn vị tiền tệ. Theo catalog. Ví dụ: `USD`. |
| ↳ landing_page | object | Thông tin trang đích. |
| ↳↳ landing_page_url | string | URL trang đích xem và mua tựa phương tiện. Ví dụ: `https://www.tiktok.com/tiktok_entertainment`. |
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
| products | object[] | **Bắt buộc**. Danh sách các xe có sẵn bạn muốn cập nhật. Tối đa: 5.000. |
| ↳ vehicle_id | string | **Bắt buộc**. ID duy nhất cho xe. Giới hạn: 100 ký tự. Ví dụ: `TIKTOKMOTORSSEDAN001`. |
| ↳ title | string | Tên của xe. Chỉ dùng ký tự Unicode hợp lệ. Giới hạn: 500 ký tự. Ví dụ: `TikTok Motors Sedan`. |
| ↳ description | string | Mô tả ngắn về xe. Giới hạn: 5.000 ký tự. Ví dụ: `Experience the ultimate luxury and performance with the TikTok Motors Sedan.` |
| ↳ availability | string | Tình trạng có sẵn của xe: `AVAILABLE` (có sẵn để đặt hàng), `NOT_AVAILABLE` (không có sẵn). Ví dụ: `AVAILABLE`. |
| ↳ image_url | string | URL hình ảnh của xe (định dạng `http://` hoặc `https://`). Kích thước tối thiểu 500x500 px, định dạng JPG hoặc PNG. Ví dụ: `https://www.tiktok.com/auto_vehicle_image_001.jpg`. |
| ↳ additional_image_urls | string[] | Danh sách URL hình ảnh bổ sung của xe. Tối đa: 20 URL. Kích thước ≥ 500x500 px. Nếu có dấu phẩy, mã hóa thành `%2C`. Ví dụ: `["https://www.tiktok.com/auto_vehicle_image_002.jpg","https://www.tiktok.com/auto_vehicle_image_003.jpg"]`. |
| ↳ video_url | string | URL video sử dụng trong quảng cáo. Khuyến nghị: 9:16 (dọc), ≥720*1280, ≥516kbps, có âm thanh kèm phụ đề. Hỗ trợ .mp4, .mov, .avi, tối đa 100MB, 15-60s. Ví dụ: `https://www.tiktok.com/auto_inventory.mp4`. |
| ↳ product_detail | object | Thông tin chi tiết bổ sung về xe. |
| ↳↳ condition | string | Tình trạng hiện tại của xe: `EXCELLENT`, `GOOD`, `FAIR`, `POOR`, `OTHER`. Ví dụ: `GOOD`. |
| ↳↳ offer_type | string | Loại ưu đãi: `CASH`, `LEASE`, `FINANCE`. |
| ↳↳ term_length | string | Thời hạn áp dụng ưu đãi. Giới hạn: 100 ký tự. Ví dụ: `3`. |
| ↳↳ offer_term_qualifier | string | Đơn vị thời hạn ưu đãi: `months`, `years`. |
| ↳↳ amount_price | string | Số tiền ưu đãi (tiền trả góp/tháng cho cash/lease hoặc tổng giá vay cho finance). Ví dụ: `100`. |
| ↳↳ amount_percentage | string | Tỷ lệ phần trăm lãi suất năm (APR) cho hình thức finance. Ví dụ: `1.1%`. |
| ↳↳ amount_qualifier | string | Định từ bổ nghĩa: `month` hoặc `APR`. |
| ↳↳ downpayment | string | Tiền trả trước/đặt cọc. Ví dụ: `3000`. |
| ↳↳ downpayment_qualifier | string | Định từ khoản trả trước: `due at signing`. |
| ↳↳ offer_disclaimer | string | Toàn văn tuyên bố miễn trừ ưu đãi. Giới hạn: 5.000 ký tự. |
| ↳↳ offer_disclaimer_url | string | URL chi tiết tuyên bố miễn trừ ưu đãi. Ví dụ: `https://www.tiktok.com/tiktok_auto_inventory_disclaimer`. |
| ↳↳ emission_disclaimer | string | Toàn văn tuyên bố miễn trừ mức phát thải. Giới hạn: 5.000 ký tự. |
| ↳↳ emission_disclaimer_url | string | URL dẫn đến thông tin tuyên bố phát thải. Ví dụ: `https://www.tiktok.com/tiktok_auto_inventory_emission_disclaimer`. |
| ↳↳ emission_overlay_disclaimer | string | Văn bản ngắn tuyên bố phát thải trên banner. Giới hạn: 500 ký tự. |
| ↳↳ emission_image_link | string | Đường dẫn hình ảnh hiển thị mức phát thải. Kích thước ≥ 450x450 px, tối đa 4MB. Ví dụ: `https://www.tiktok.com/tiktok_auto_inventory_emission_image.jpg`. |
| ↳ state_of_vehicle | string | Tình trạng xe: `NEW` (xe mới), `USED` (xe đã qua sử dụng), `CPO` (xe có chứng nhận chính hãng). Ví dụ: `USED`. |
| ↳ vehicle_type | string | Loại phương tiện: `BOAT`, `CAR_TRUCK`, `COMMERCIAL`, `MOTORCYCLE`, `POWERSPORT`, `RV_CAMPER`, `TRAILER`, `OTHER`. |
| ↳ make | string | Hãng sản xuất xe (thương hiệu). Giới hạn: 100 ký tự. Ví dụ: `TikTok Motors`. |
| ↳ model | string | Dòng/mẫu xe. Giới hạn: 100 ký tự. Ví dụ: `X`. |
| ↳ trim | string | Phiên bản/gói cấu hình xe. Giới hạn: 50 ký tự. Ví dụ: `Long Range`. |
| ↳ year | integer | Năm ra mắt xe, định dạng `YYYY`. Phạm vi: 1801-2999. Ví dụ: `2023`. |
| ↳ vin | string | Số nhận dạng xe (VIN) gồm 17 ký tự theo chuẩn ISO 3779. Ví dụ: `1TIKT0K5TAR123456`. |
| ↳ mileage | object | Quãng đường đã chạy của xe (odo). |
| ↳↳ value | integer | Giá trị quãng đường đã đi. Phạm vi: ≥ 0. |
| ↳↳ unit | string | Đơn vị đo: `MILE` (dặm), `KILOMETER` (km). |
| ↳ body_style | string | Kiểu dáng thân xe: `CONVERTIBLE`, `COUPE`, `CROSSOVER`, `HATCHBACK`, `MINIVAN`, `SMALL_CAR`, `SEDAN`, `SUV`, `TRUCK`, `VAN`, `WAGON`, `OTHER`. |
| ↳ exterior_color | string | Màu sơn ngoại thất xe. Giới hạn: 100 ký tự. |
| ↳ interior_color | string | Màu nội thất xe. Giới hạn: 100 ký tự. |
| ↳ transmission | string | Loại hộp số xe: `AUTOMATIC`, `MANUAL`. |
| ↳ drivetrain | string | Hệ dẫn động: `4X2`, `4X4`, `AWD`, `FWD`, `RWD`, `OTHER`. |
| ↳ fuel_type | string | Loại nhiên liệu: `DIESEL`, `ELECTRIC`, `FLEX`, `GASOLINE`, `HYBRID`, `OTHER`. |
| ↳ address | object | Thông tin địa chỉ đại lý bán xe (dealership). |
| ↳↳ address | string | Địa chỉ đường phố của đại lý. Giới hạn: 150 ký tự. |
| ↳↳ city | string | Thành phố nơi đại lý tọa lạc. Giới hạn: 150 ký tự. |
| ↳↳ region | string | Bang/tỉnh nơi đại lý tọa lạc. Giới hạn: 150 ký tự. |
| ↳↳ postal_code | string | Mã bưu chính của đại lý. Giới hạn: 150 ký tự. |
| ↳ latitude | float | Vĩ độ của đại lý xe. Phạm vi: [-90, 90]. Ví dụ: `37.484100`. |
| ↳ longitude | float | Kinh độ của đại lý xe. Phạm vi: [-180, 180]. Ví dụ: `-122.148252`. |
| ↳ dealer | object | Thông tin chi tiết về đại lý xe. |
| ↳↳ dealer_id | string | ID duy nhất của đại lý xe. Giới hạn: 100 ký tự. |
| ↳↳ dealer_name | string | Tên đại lý xe. Giới hạn: 100 ký tự. |
| ↳↳ dealer_phone | string | Số điện thoại đại lý. Giới hạn: 15 ký tự. |
| ↳↳ stock_number | string | Mã số kho/lô gán cho xe. Giới hạn: 100 ký tự. Ví dụ: `T12345`. |
| ↳ date_first_on_lot | string | Ngày đầu tiên xe có mặt tại bãi, định dạng `YYYY-MM-DD`. Ví dụ: `2023-12-01`. |
| ↳ days_on_lot | integer | Số ngày xe nằm tại bãi đại lý. Mặc định: 0. Ví dụ: `13`. |
| ↳ price_info | object | Thông tin giá xe. |
| ↳↳ price | float | Giá bán của xe. Ví dụ: `9.9`. |
| ↳↳ currency | string | Đơn vị tiền tệ. Theo catalog. Ví dụ: `USD`. |
| ↳↳ sale_price | float | Giá khuyến mãi giảm giá của xe. Phải nhỏ hơn `price`. Ví dụ: `9.9`. |
| ↳↳ sale_price_effective_date | string | Thời gian áp dụng giá khuyến mãi, định dạng `YYYY-MM-DDT23:59+00:00/YYYY-MM-DDT23:59+00:00`. Ví dụ: `2023-12-11T23:59+00:00/2023-12-15T23:59+00:00`. |
| ↳ landing_page | object | Thông tin trang đích. |
| ↳↳ landing_page_url | string | URL trang đích xem và mua xe. Ví dụ: `https://www.tiktok.com/tiktok_auto_inventory`. |
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
| products | object[] | **Bắt buộc**. Danh sách các mẫu xe bạn muốn cập nhật. Tối đa: 5.000. |
| ↳ vehicle_id | string | **Bắt buộc**. ID duy nhất cho mẫu xe. Giới hạn: 100 ký tự. Ví dụ: `TIKTOKMOTORSX001`. |
| ↳ title | string | Tên mẫu xe bao gồm hãng, dòng xe, phiên bản và năm sản xuất. Giới hạn: 128 ký tự. Ví dụ: `2025 TikTok Motors X Long Range`. |
| ↳ image_url | string | URL hình ảnh của mẫu xe (`http://` hoặc `https://`). Kích thước tối thiểu 450x450 px, định dạng JPG, PNG hoặc JPEG. Dung lượng dưới 4MB. Ví dụ: `https://www.tiktok.com/auto_model_image_001.jpg`. |
| ↳ video_url | string | URL video sử dụng trong quảng cáo. Khuyến nghị: 9:16 (dọc), ≥ 720*1280, ≥ 516 kbps, có âm thanh và phụ đề. Tối đa 100MB, 15-60 giây. Ví dụ: `https://www.tiktok.com/auto_model.mp4`. |
| ↳ make | string | Hãng sản xuất xe. Giới hạn: 100 ký tự. Ví dụ: `TikTok Motors`. |
| ↳ model | string | Dòng/mẫu xe. Giới hạn: 100 ký tự. Ví dụ: `X`. |
| ↳ trim | string | Phiên bản cấu hình xe. Giới hạn: 50 ký tự. Ví dụ: `Long Range`. |
| ↳ year | integer | Năm ra mắt xe, định dạng `YYYY`. Ví dụ: 2025. |
| ↳ exterior_color | string | Màu sơn ngoại thất xe. Giới hạn: 100 ký tự. Ví dụ: `Black`. |
| ↳ product_detail | object | Thông tin chi tiết bổ sung về mẫu xe. |
| ↳↳ offer_type | string | Loại ưu đãi: `CASH`, `LEASE`, `FINANCE`. |
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
| ↳ landing_page | object | Thông tin trang đích. |
| ↳↳ landing_page_url | string | URL trang đích xem danh sách xe. Ví dụ: `https://www.tiktok.com/tiktok_auto_model`. |

#### Tham số mảng đối tượng `products` cho catalog phim ngắn nhiều tập (mini series)

> [!NOTE]
> Catalog phim ngắn nhiều tập (mini series) hiện là tính năng danh sách cho phép (allowlist-only) trong giai đoạn thử nghiệm và chỉ mở theo thư mời. Vui lòng liên hệ đại diện TikTok nếu muốn truy cập.

| Field | Data Type | Description |
|---|---|---|
| products | object[] | **Bắt buộc**. Danh sách các bộ phim ngắn bạn muốn cập nhật. Tối đa: 5.000. |
| ↳ series_id | string | **Bắt buộc**. ID duy nhất tự định nghĩa cho bộ phim ngắn. Giới hạn: 100 ký tự. |
| ↳ series_name | string | Tên của bộ phim ngắn. Giới hạn: 100 ký tự. |
| ↳ target_config | object | Chi tiết nhắm mục tiêu cho bộ phim ngắn.<br>**Lưu ý**: Để cập nhật bộ phim nhắm mục tiêu nhiều khu vực, gọi [/catalog/product/update/](28-catalog-products-p2.md#doc-1740562287852546) nhiều lần với cùng `series_id` và các cài đặt `target_config` khác nhau. Sau khi cập nhật, truy cập cài đặt hợp nhất qua `target_config` và `additional_product_list` trong [/catalog/product/get/](28-catalog-products-p2.md#doc-1740564136678402). |
| ↳↳ region_code | string | Mã của khu vực nhắm mục tiêu cho bộ phim ngắn. Ví dụ: `US`. |
| ↳ image_url | string | URL ảnh áp phích (poster) của bộ phim. Kích thước tối thiểu 500x500 px, định dạng JPG hoặc PNG. Ví dụ: `https://www.tiktok.com/short_drama_series_image_001.jpg`. |
| ↳ video_url | string | URL video sử dụng trong quảng cáo. Khuyến nghị: 9:16 (dọc), ≥ 720*1280, ≥ 516 kbps, có âm thanh kèm phụ đề. Ví dụ: `https://www.tiktok.com/short_drama_series.mp4`. |
| ↳ recharge | object[] | Thông tin nạp tiền/thanh toán để xem bộ phim ngắn. |
| ↳↳ type | string | Loại nạp tiền/thanh toán: `BY_TIERS`, `SUBSCRIPTION`, `BY_EPISODES`. |
| ↳↳ purchase_unit | string[] | Đơn vị thanh toán:<br>• `BY_TIERS`: `TIER_1` đến `TIER_5`.<br>• `SUBSCRIPTION`: `WEEKLY`, `MONTHLY`, `QUARTERLY`, `YEARLY`.<br>• `BY_EPISODES`: Chuỗi số thể hiện số tập. |
| ↳↳ cost | float[] | Mức giá tương ứng cho các bậc, chu kỳ thuê bao hoặc số tập phim. |
| ↳ product_detail | object | Thông tin chi tiết bổ sung về bộ phim ngắn. |
| ↳↳ company_type | string | Loại hình công ty của bộ phim: `COPYRIGHT_HOLDER`, `DISTRIBUTOR`. |
| ↳↳ copyright_holder_name | string | Tên công ty sở hữu bản quyền. Giới hạn: 100 ký tự. |
| ↳↳ app_id | string | App ID của ứng dụng cần quảng bá. Lấy danh sách App ID qua [/app/list/](43-events-1-0-p1.md#doc-1740859313270786). |
| ↳↳ minis_id | string | Mã định danh chương trình nhỏ (mini program ID) trên TikTok Open Platform. |
| ↳↳ total_episodes | number | Tổng số tập của bộ phim ngắn. Phạm vi: 1-9.999. |
| ↳↳ initial_paid_episodes | number | Số thứ tự tập bắt đầu yêu cầu trả phí để tiếp tục xem. Phạm vi: 1-9.999. |
| ↳↳ per_episode_duration | number | Thời lượng trung bình mỗi tập (phút). Phạm vi: 0-15. |
| ↳↳ spoken_language | string | Ngôn ngữ thoại của các diễn viên trong bản gốc phim: `ar`, `de`, `cs`, `en`, `es`, `fr`, `he`, `hi`, `id`, `it`, `ja`, `ko`, `ms`, `pl`, `pt`, `ro`, `ru`, `ta`, `th`, `tr`, `vi`, `zh`, `zh-hant`. |
| ↳↳ subtitle_language | string | Ngôn ngữ phụ đề trong phim ngắn: `ar`, `de`, `cs`, `en`, `es`, `fr`, `he`, `hi`, `id`, `it`, `ja`, `ko`, `ms`, `pl`, `pt`, `ro`, `ru`, `ta`, `th`, `tr`, `vi`, `zh`, `zh-hant`. |
| ↳↳ production_type | string | Loại hình sản xuất: `LOCAL`, `TRANSLATION`. |
| ↳↳ target_audience | string | Đối tượng khán giả mục tiêu: `MALE`, `FEMALE`, `NEUTRAL`. |
| ↳↳ characters | string[] | Danh sách các hình mẫu nhân vật trong phim. Tối đa: 3. Xem bảng giá trị cho `characters` bên dưới. |
| ↳↳ genres | string[] | Thể loại của bộ phim ngắn theo cốt truyện chính. Tối đa: 3. Xem bảng giá trị cho mini series `genres` bên dưới. |
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
| products | object[] | **Bắt buộc**. Danh sách các sản phẩm/dịch vụ bạn muốn cập nhật. Tối đa: 5.000. |
| ↳ item_id | string | **Bắt buộc**. ID duy nhất tự định nghĩa cho sản phẩm hoặc dịch vụ. Giới hạn: 100 ký tự. |
| ↳ title | string | Tên sản phẩm hoặc dịch vụ. Giới hạn: 500 ký tự. |
| ↳ description | string | Mô tả chi tiết về sản phẩm hoặc dịch vụ. Giới hạn: 5.000 ký tự. |
| ↳ availability | string | Tình trạng tồn kho hiện tại: `IN_STOCK`, `AVAILABLE`, `PREORDER`, `OUT_OF_STOCK`, `DISCONTINUED`, `UNAVAILABLE`. |
| ↳ image_url | string | URL dẫn đến hình ảnh chính của sản phẩm/dịch vụ. Kích thước từ 500×500 đến 1290×2790 px. Tỷ lệ khuyến nghị 1:1. |
| ↳ video_url | string | Đường dẫn video sản phẩm/dịch vụ. Khuyến nghị: 9:16 (dọc), ≥720*1280, ≥516 kbps, có âm thanh và phụ đề. |
| ↳ additional_image_urls | string[] | Danh sách URL hình ảnh bổ sung. Tối đa 20 liên kết, định dạng JPG/PNG, kích thước 500x500 đến 1290x2790 px. Ví dụ: `["https://www.example.com/products/images/headphones-side.jpg", "https://www.example.com/products/images/headphones-box.jpg"]`. |
| ↳ address | object | Thông tin địa chỉ cung cấp sản phẩm/dịch vụ. |
| ↳↳ street | string | Địa chỉ đường phố nơi đặt sản phẩm/dịch vụ. Giới hạn: 150 ký tự. Ví dụ: `1143 coleman Avenue`. |
| ↳↳ city | string | Thành phố nơi đặt sản phẩm/dịch vụ. Giới hạn: 150 ký tự. Ví dụ: `San Jose`. |
| ↳↳ region | string | Bang/tỉnh/khu vực hành chính. Giới hạn: 150 ký tự. Ví dụ: `California`. |
| ↳↳ postal_code | string | Mã bưu chính hoặc mã zip. Giới hạn: 150 ký tự. Ví dụ: `95050`. |
| ↳ longitude | double | Kinh độ của địa điểm. Phạm vi: [-180, 180]. Ví dụ: `100.5`. |
| ↳ latitude | double | Vĩ độ của địa điểm. Phạm vi: [-90, 90]. Ví dụ: `-25.5`. |
| ↳ product_detail | object | Thông tin chi tiết khác của sản phẩm/dịch vụ. |
| ↳↳ rating | double | Điểm đánh giá của người dùng. Phạm vi: 0.0 - 5.0. |
| ↳↳ availability_type | string | Phương thức định nghĩa vùng địa lý khả dụng: `REGION`, `DMA`, `RADIUS`, `POSTAL_CODE`. |
| ↳↳ availability_region | string[][] | Danh sách khu vực (mảng các mảng chuỗi biểu diễn L1, L2). Tối đa 998 địa điểm. Ví dụ: `[["Arizona","Peoria"],["Alabama","Birmingham"]]`. |
| ↳↳ availability_dma | string[] | Danh sách số DMA 3 chữ số, tối đa 500 mã. Chỉ áp dụng cho catalog `US`. Ví dụ: `["501","803"]`. |
| ↳↳ availability_circle_radius | string | Bán kính khả dụng hình tròn (km: > 0 và ≤ 40; dặm: > 0 và ≤ 25). Chỉ áp dụng cho `TH`, `ID`, `MY`, `VN`. Ví dụ: `20`. |
| ↳↳ availability_circle_radius_unit | string | Đơn vị bán kính: `KM` hoặc `MI`. Chỉ áp dụng cho `TH`, `ID`, `MY`, `VN`. |
| ↳↳ availability_postal_codes | string[] | Danh sách mã bưu chính, tối đa 500 mã. Chỉ áp dụng cho `US` hoặc `CA`. Ví dụ: `["10001", "90001"]`. |
| ↳↳ custom_number_0 | double | Thuộc tính số tùy chỉnh cho quản lý sản phẩm. |
| ↳↳ custom_number_1 | double | Thuộc tính số tùy chỉnh cho quản lý sản phẩm. |
| ↳↳ custom_number_2 | double | Thuộc tính số tùy chỉnh cho quản lý sản phẩm. |
| ↳↳ custom_number_3 | double | Thuộc tính số tùy chỉnh cho quản lý sản phẩm. |
| ↳↳ custom_number_4 | double | Thuộc tính số tùy chỉnh cho quản lý sản phẩm. |
| ↳ price_info | object | Thông tin giá. |
| ↳↳ price | double | Giá của một đơn vị sản phẩm hoặc dịch vụ. Ví dụ: `9.99`. |
| ↳↳ currency | string | Đơn vị tiền tệ. Ví dụ: `USD`. |
| ↳↳ sale_price | double | Giá khuyến mãi giảm giá. Phải thấp hơn `price`. Ví dụ: `4.99`. |
| ↳ landing_page | object | Thông tin trang đích. |
| ↳↳ landing_page_url | string | Liên kết trang đích trực tiếp của sản phẩm/dịch vụ. |
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
| products | object[] | **Bắt buộc**. Danh sách các sản phẩm/dịch vụ bạn muốn cập nhật. Tối đa: 5.000. |
| ↳ listing_id | string | **Bắt buộc**. ID duy nhất cho danh mục niêm yết (listing). Không giới hạn độ dài. |
| ↳ title | string | Tên của niêm yết. Độ dài khuyến nghị: 25 ký tự. Ví dụ: `Big Mac`. |
| ↳ description | string | Mô tả về niêm yết. Giới hạn: 5.000 ký tự. Ví dụ: `Nice burger!`. |
| ↳ availability | string | Tình trạng khả dụng của niêm yết: `IN_STOCK`, `AVAILABLE_FOR_ORDER`, `PREORDER`, `OUT_OF_STOCK`, `DISCONTINUED`. |
| ↳ image_url | string | URL hình ảnh chính của niêm yết (JPG, JPEG hoặc PNG, 500×500 đến 1290×2790 px). Ví dụ: `https://www.tiktok.com/tiktok_service_001.jpg`. |
| ↳ brand | string | Tên thương hiệu của niêm yết. Giới hạn: 150 ký tự. |
| ↳ google_product_category | string | Phân loại danh mục theo Google product taxonomy (tối đa 3 cấp). Ví dụ: `Apparel & Accessories > Clothing > Dresses`. |
| ↳ item_group_id | string | SPU ID dùng chung cho các biến thể của sản phẩm. Ví dụ: `TikTok_1234`. |
| ↳ additional_image_urls | string[] | Danh sách URL hình ảnh bổ sung (tối đa 20 URL, 500x500 đến 1290x2790 px). Ví dụ: `https://www.tiktok.com/tiktok_service_002.jpg`. |
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
| ↳↳ price | float | Giá của một mặt hàng niêm yết. Đảm bảo khớp với giá trên trang đích. Ví dụ: `9.99`. |
| ↳↳ sale_price | float | Giá khuyến mãi giảm giá của mặt hàng. Ví dụ: `4.99`. |
| ↳↳ sale_price_effective_date | string | Khoảng thời gian áp dụng giá khuyến mãi theo giờ UTC, định dạng `YYYY-MM-DDT23:59+00:00/YYYY-MM-DDT23:59+00:00`. Ví dụ: `2026-12-11T23:59+00:00/2026-12-15T23:59+00:00`. |
| ↳ landing_page | object | Thông tin trang đích. |
| ↳↳ landing_page_url | string | URL trang đích của niêm yết. Ví dụ: `https://www.tiktok.com/tiktok_service`. |
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
curl -X POST 'https://business-api.tiktok.com/open_api/v1.3/catalog/product/update/' \
  -H 'Access-Token: YOUR_ACCESS_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{
    "bc_id": "7123456789012345678",
    "catalog_id": "7234567890123456789",
    "feed_id": "7345678901234567890",
    "products": [
      {
        "sku_id": "TikTok_item_1234",
        "title": "T-Shirt (Unisex) - Updated",
        "availability": "IN_STOCK",
        "price_info": {
          "price": 35.0,
          "currency": "USD",
          "sale_price": 25.0
        }
      }
    ]
  }'
```

#### Python
```python
import requests

url = "https://business-api.tiktok.com/open_api/v1.3/catalog/product/update/"
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
            "title": "T-Shirt (Unisex) - Updated",
            "availability": "IN_STOCK",
            "price_info": {
                "price": 35.0,
                "currency": "USD",
                "sale_price": 25.0
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
  "request_id": "202312151040150102422470530400C321",
  "data": {
    "feed_log_id": "7312345678901234567"
  }
}
```

---

## Xóa sản phẩm (`Remove products`)
<a id="doc-1740562489236481"></a>
<!-- doc_id: 1740562489236481 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/catalog/product/delete/`

> **Đường dẫn**: API Reference > Catalog Products > Remove products

**Mục đích**: Sử dụng endpoint này để xóa hàng loạt sản phẩm khỏi danh mục sản phẩm (catalog).

Trong phản hồi, bạn sẽ nhận được mã ID tác vụ xử lý `feed_log_id`. Với ID này, bạn có thể kiểm tra trạng thái xử lý và kết quả cuối cùng của tác vụ xóa thông qua endpoint [/catalog/product/log/](28-catalog-products-p3.md#doc-1740570027173889).

> [!NOTE]
> • Mã SKU là duy nhất trong cùng một Catalog, và thao tác tải lại một SKU chỉ có thể được thực hiện dưới feed mà SKU đó trực thuộc.<br>
> • Đối với mỗi catalog, bạn có thể thực hiện tối đa 1.000 yêu cầu mỗi giờ. Nếu giới hạn này không đáp ứng đủ nhu cầu, vui lòng liên hệ đại diện TikTok của bạn.<br>
> • Đối với mỗi catalog, bạn chỉ có thể gửi một yêu cầu tại một thời điểm. Giới hạn này áp dụng cho cả thao tác tải lên và xóa. Nếu bạn gửi hai yêu cầu cùng một lúc, yêu cầu sau sẽ thất bại. Khuyến nghị gửi một yêu cầu trước và chờ yêu cầu đó hoàn thành rồi mới gửi tiếp yêu cầu sau.

### Header

| Field | Data Type | Description |
|---|---|---|
| Access-Token | string | **Bắt buộc**. Access token được ủy quyền. Chi tiết xem [Xác thực (Authentication)](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type | string | **Bắt buộc**. Loại nội dung yêu cầu. Giá trị được chấp nhận: `"application/json"`. |

### Tham số (JSON body)

| Field | Type | Description |
|---|---|---|
| bc_id | string | **Bắt buộc**. ID của Business Center. Để lấy danh sách Business Center bạn có quyền truy cập, sử dụng [/bc/get/](12-bc-management.md#doc-1737115687501826). |
| catalog_id | string | **Bắt buộc**. ID của Catalog. Để lấy danh sách catalog bạn có quyền truy cập, sử dụng [/bc/asset/get/](15-bc-assets.md#doc-1739432717798401) và đặt `asset_type` thành `CATALOG`. |
| sku_ids | string[] | **Bắt buộc có điều kiện** (đối với sản phẩm trong catalog E-commerce). Danh sách SKU ID của các sản phẩm E-commerce bạn muốn xóa. Tối đa: 1.000. Giới hạn độ dài: 100 ký tự cho mỗi SKU ID và không chứa emoji. Để lấy SKU ID, dùng [/catalog/product/get/](28-catalog-products-p2.md#doc-1740564136678402). Không hỗ trợ trùng SKU ID. |
| hotel_ids | string[] | **Bắt buộc có điều kiện** (đối với sản phẩm trong catalog khách sạn). Danh sách Hotel ID của các khách sạn bạn muốn xóa. Tối đa: 1.000. Giới hạn: 100 ký tự mỗi ID. Để lấy Hotel ID, dùng [/catalog/product/get/](28-catalog-products-p2.md#doc-1740564136678402). Không hỗ trợ trùng ID. |
| flight_ids | string[] | **Bắt buộc có điều kiện** (đối với sản phẩm trong catalog chuyến bay). Danh sách Flight ID của các chuyến bay bạn muốn xóa. Tối đa: 1.000. Giới hạn: 150 ký tự mỗi ID. Để lấy Flight ID, dùng [/catalog/product/get/](28-catalog-products-p2.md#doc-1740564136678402). Không hỗ trợ trùng ID. |
| destination_ids | string[] | **Bắt buộc có điều kiện** (đối với sản phẩm trong catalog điểm đến du lịch). Danh sách Destination ID của các điểm đến bạn muốn xóa. Tối đa: 1.000. Giới hạn: 100 ký tự mỗi ID. Để lấy Destination ID, dùng [/catalog/product/get/](28-catalog-products-p2.md#doc-1740564136678402). Không hỗ trợ trùng ID. |
| vehicle_ids | string[] | **Bắt buộc có điều kiện** (đối với sản phẩm trong catalog Auto-Inventory hoặc Auto-Model). Danh sách ID của các xe bạn muốn xóa. Tối đa: 1.000. Giới hạn: 100 ký tự mỗi ID và không chứa emoji. Để lấy Vehicle ID, dùng [/catalog/product/get/](28-catalog-products-p2.md#doc-1740564136678402). Không hỗ trợ trùng ID. |
| series_ids | string[] | **Bắt buộc có điều kiện** (đối với sản phẩm trong catalog phim ngắn tập). Danh sách ID của các bộ phim ngắn bạn muốn xóa. Tối đa: 1.000. Giới hạn: 100 ký tự mỗi ID. Để lấy ID phim ngắn, dùng [/catalog/product/get/](28-catalog-products-p2.md#doc-1740564136678402). Không hỗ trợ trùng ID. |
| item_ids | string[] | **Bắt buộc có điều kiện** (đối với sản phẩm hoặc dịch vụ trong catalog chung generic). Danh sách ID của các sản phẩm hoặc dịch vụ bạn muốn xóa. Tối đa: 10.000. Để lấy ID, dùng [/catalog/product/get/](28-catalog-products-p2.md#doc-1740564136678402). Không hỗ trợ trùng ID. |
| listing_ids | string[] | **Bắt buộc có điều kiện** (đối với danh mục niêm yết trong catalog trực tuyến đến ngoại tuyến O2O). Danh sách Listing ID bạn muốn xóa. Tối đa: 10.000. Để lấy Listing ID, dùng [/catalog/product/get/](28-catalog-products-p2.md#doc-1740564136678402). Không hỗ trợ trùng ID. |
| feed_id | string | ID của Feed. Nếu giá trị trường này để trống, catalog mặc định sẽ được xử lý. |

### Phản hồi

| Field | Type | Description |
|---|---|---|
| code | number | Mã phản hồi. Xem [Phụ lục mã phản hồi (return code)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông điệp phản hồi. Xem [Phụ lục mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | ID bản ghi của yêu cầu, định danh duy nhất cho mỗi yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ feed_log_id | string | ID nhật ký xử lý sản phẩm (Product handling log ID). |

### Ví dụ

#### cURL
```bash
curl -X POST 'https://business-api.tiktok.com/open_api/v1.3/catalog/product/delete/' \
  -H 'Access-Token: YOUR_ACCESS_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{
    "bc_id": "7123456789012345678",
    "catalog_id": "7234567890123456789",
    "feed_id": "7345678901234567890",
    "sku_ids": [
      "TikTok_item_1234",
      "TikTok_item_5678"
    ]
  }'
```

#### Python
```python
import requests

url = "https://business-api.tiktok.com/open_api/v1.3/catalog/product/delete/"
headers = {
    "Access-Token": "YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}
payload = {
    "bc_id": "7123456789012345678",
    "catalog_id": "7234567890123456789",
    "feed_id": "7345678901234567890",
    "sku_ids": ["TikTok_item_1234"]
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
  "request_id": "2020091405212201023125321410665",
  "data": {
    "feed_log_id": "73474"
  }
}
```

---

<a id="doc-1740564136678402"></a>
<!-- doc_id: 1740564136678402 -->
# Get products
> Đường dẫn: API Reference > Catalog Products > Get products
Use this endpoint to get the list of products in your product catalog.

You can filter the products you want to get by specifying product IDs, SKU IDs, product set IDs or by using custom conditions (`conditions`). You can also order the results by product availability or custom conditions.

## Request
**Endpoint** https://business-api.tiktok.com/open_api/v1.3/catalog/product/get/

**Method** GET

**Header**

| Field | Data Type | Description |
|---|---|---|
| Access-Token  **(Required)** | string | Authorized access token. For details, see [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Field | Type | Description |
|--- |--- |--- |
| bc_id *(Required)* | string | Business Center ID. |
| catalog_id *(Required)* | string | Catalog ID. |
| page | number | Current page number.<br><br><p><span style="color:darkred"><b>Note</b></span>: Only 10,000 results can be returned at most. You need to ensure that `page` multiplied by `page_size` is no more than 10,000. |
| page_size | number | Page size. <br><br>Default value: 10.<br>Value range: within 500.|
| product_ids | string[] | IDs of the products that you want to get. <br><br>Max size: 1,000. <br><br><p><span style="color:darkred"><b>Note</b></span>:  <ul><li>`product_ids` and `sku_ids` cannot be specified at the same time. </li><li>For mini series catalogs, the only supported filter is `product_ids`.</li></ul>|
|sku_ids| string[]| IDs of the SKUs that you want to get information for. Max size: 1000.<br>Length limit: 100 characters for each SKU ID and cannot contain emojis.<br><p><span style="color:darkred"><b>Note</b></span>:<ul><li>Duplicate SKU IDs are not supported. </li><li>`product_ids` and `sku_ids` cannot be specified at the same time.</li></ul>|
|series_ids|string[]|IDs of the short drama series that you want to filter.<br><br>Max size: 1,000.<br><br>Length limit: 100 characters for each short drama series ID.<br><br><p><span style="color:darkred"><b>Note</b></span>: <ul><li>Duplicate short drama series IDs are not supported.</li><li>`product_ids` and `series_ids` cannot be specified at the same time.</li><li>`conditions` and `series_ids` cannot be specified at the same time.</li></ul>|
|product_set_ids|string[]| IDs of the product sets that you want to get. Max size: 100.|
|product_available_type|string|Valid only when an Ecommerce or online-to-offline catalog is specified through `catalog_id`.<br><br>The type of products to retrieve.<br><br>Enum values:<ul><li>`AVAILABLE`: To retrieve products that are available for ad creation.</li><li>`ALL`: To retrieve all products.</li></ul><br>Default value: `ALL`.|
|order|object|Ordering settings. When `product_ids` or `sku_ids` is specified, this field will be ignored.|
#|order_condition|string| Order-by condition. Currently, the only supported value is `PRODUCT_AVAILABILITY`. Do not pass in this field and `custom_order` at the same time. |
#|custom_order|object[]|Custom ordering / sorting conditions. Do not pass in this field and `order_condition` at the same time.|
##|field|string|Data field that you want to order your products by. For supported ordering-by fields, see the Supported fields section below.|
##|type|string|Ordering / sorting type. Enum values: `ASC` (ascending order), `DES` (descending).|
|conditions|object|Filtering conditions. <br>When you specify a filtering condition, all data fields in this object are required except `case_senstive`. <br>When `product_ids`, `sku_ids`, or `series_ids` is specified, this field will be ignored.|
#|and / or| object[]| Logic operator for the conditions. Either `and` or `or`.|
##|field|string| Data field to filter by. For the supported fields, see the <a href="#item-link-anchor-0-2-1">Supported fields</a>  section below.|
##|operator|string|Filter operator. Enum values: `EQ`, `NE`, `GT`, `GTE`,  `LT`,  `LTE`,  `RNG`,  `WILDCARD`, `NOT_WILDCARD`,  `PREFIX`, `EXIST`, `IN`,  `NOT_IN`.|
##|values|string[]| Filter values. Multiple values are allowed when `operator` is `RNG`, `IN`, or `NOT_IN`.|
##|case_senstive|boolean|Whether it is case-sensitive.|

### Supported fields

#### For E-commerce catalog products

| Data Field | Supports ordering-by? | Can be used as field under conditions? | Case-sensitive? |
|---|---|---|---|
| sku_id | Yes | Yes | No |
| product_id | Yes | Yes | Yes |
| audit_status | No | Yes | Yes |
| title | Yes | Yes | No |
| description | Yes | Yes | No |
| brand | Yes | Yes | No |
| item_group_id | Yes | Yes | No |
| google_product_category | Yes | Yes | No |
| price_info | Yes | Yes | Yes |
| sale_price | Yes | Yes | Yes |
| sale_price_effective_start_date | Yes | Yes | Yes |
| sale_price_effective_end_date | Yes | Yes | Yes |
| condition | No | Yes | Yes |
| age_group | No | Yes | Yes |
| color | Yes | Yes | No |
| gender | No | Yes | Yes |
| size | Yes | Yes | No |
| material | Yes | Yes | No |
| pattern | Yes | Yes | No |
| product_category | Yes | Yes | No |
| custom_label_0 | Yes | Yes | No |
| custom_label_1 | Yes | Yes | No |
| custom_label_2 | Yes | Yes | No |
| custom_label_3 | Yes | Yes | No |
| custom_label_4 | Yes | Yes | No |
| active_status | No | Yes | Yes |

#### For flight catalog products

| Data Field | Supports ordering-by? | Can be used as field under conditions? | Case-sensitive? |
|---|---|---|---|
| flight_id | Yes | Yes | No |
| origin_airport | Yes | Yes | No |
| destination_airport | Yes | Yes | No |
| origin_city | Yes | Yes | No |
| destination_city | Yes | Yes | No |
| description | Yes | Yes | Yes |
| cabin_class | Yes | Yes | No |
| airline_company | Yes | Yes | No |
| price | Yes | Yes | No |
| custom_label_0 | Yes | Yes | No |
| custom_label_1 | Yes | Yes | No |
| custom_label_2 | Yes | Yes | No |
| custom_label_3 | Yes | Yes | No |
| custom_label_4 | Yes | Yes | No |

#### For entertainment catalog products

| Data Field | Can be used as field under conditions? |
|---|---|
| media_title_id | Yes |
| product_id | Yes |
| audit_status | Yes |
| title | Yes |
| description | Yes |
| availability | Yes |
| timeline | Yes |
| genres | Yes |

#### For Auto-Inventory catalog products

| Data Field | Supports ordering-by? | Can be used as field under conditions? | Case-sensitive? |
|---|---|---|---|
| vehicle_id | Yes | Yes | Yes |
| title | Yes | Yes | Yes |
| description | Yes | Yes | Yes |
| availability | No | Yes | No |
| condition | No | Yes | No |
| state_of_vehicle | No | Yes | No |
| make | Yes | Yes | Yes |
| model | Yes | Yes | Yes |
| trim | Yes | Yes | Yes |
| year | Yes | Yes | No |
| vin | Yes | Yes | Yes |
| mileage | Yes | Yes | No |
| body_style | No | Yes | No |
| drivetrain | No | Yes | No |
| fuel_type | No | Yes | No |
| city | Yes | No | Yes |

#### For Auto-Model catalog products

| Data Field | Supports ordering-by? | Can be used as field under conditions? | Case-sensitive? |
|---|---|---|---|
| vehicle_id | Yes | Yes | Yes |
| title | Yes | Yes | Yes |
| make | Yes | Yes | Yes |
| model | Yes | Yes | Yes |
| year | Yes | Yes | Yes |
| trim | Yes | Yes | Yes |

#### For short drama series

| Data Field | Supports ordering-by? | Can be used as field under conditions? | Case-sensitive? |
|---|---|---|---|
| series_id | Yes | Yes | No |
| series_name | Yes | Yes | No |
| product_detail.genres | Yes | Yes | Yes |
| product_detail.characters | Yes | Yes | Yes |
| product_detail.historical_context | Yes | Yes | Yes |

#### For generic catalog products or services

| Data Field | Supports ordering-by? | Can be used as field under conditions? | Case-sensitive? |
|---|---|---|---|
| title | Yes | Yes | No |
| item_id | Yes | Yes | Yes |
| price_info.price | Yes | Yes | Yes |
| price_info.sale_price | Yes | Yes | Yes |
| availability | Yes | Yes | Yes |
| rating | Yes | Yes | Yes |
| address.region | Yes | Yes | No |
| address.city | Yes | Yes | No |
| address.street | Yes | Yes | Yes |
| extra_info.custom_label_0 | Yes | Yes | No |
| extra_info.custom_label_1 | Yes | Yes | No |
| extra_info.custom_label_2 | Yes | Yes | No |
| extra_info.custom_label_3 | Yes | Yes | No |
| extra_info.custom_label_4 | Yes | Yes | No |
| extra_info.custom_label_5 | Yes | Yes | No |
| extra_info.custom_label_6 | Yes | Yes | No |
| product_detail.custom_number_0 | Yes | Yes | No |
| product_detail.custom_number_1 | Yes | Yes | No |
| product_detail.custom_number_2 | Yes | Yes | No |
| product_detail.custom_number_3 | Yes | Yes | No |
| product_detail.custom_number_4 | Yes | Yes | No |

#### For online-to-offline products

| Data Field | Supports ordering-by? | Can be used as field under conditions? | Case-sensitive? |
|---|---|---|---|
| listing_id | Yes | Yes | No |
| title | Yes | Yes | No |
| availability | Yes | Yes | No |
| brand | Yes | Yes | No |
| product_detail.rating | Yes | Yes | No |
| condition | Yes | Yes | No |
| age_group | Yes | Yes | No |
| gender | Yes | Yes | No |
| google_product_category | Yes | Yes | Yes |
| item_group_id | Yes | Yes | No |
| price_info.price | Yes | Yes | No |
| price_info.sale_price | Yes | Yes | No |
| address.region | Yes | Yes | Yes |
| address.city | Yes | Yes | Yes |
| product_detail.custom_number_0 | Yes | Yes | No |
| product_detail.custom_number_1 | Yes | Yes | No |
| product_detail.custom_number_2 | Yes | Yes | No |
| product_detail.custom_number_3 | Yes | Yes | No |
| product_detail.custom_number_4 | Yes | Yes | No |
| extra_info.custom_label_0 | Yes | Yes | No |
| extra_info.custom_label_1 | Yes | Yes | No |
| extra_info.custom_label_2 | Yes | Yes | No |
| extra_info.custom_label_3 | Yes | Yes | No |
| extra_info.custom_label_4 | Yes | Yes | No |

### Example
```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/catalog/product/get/' \
--header 'Access-Token: xxxx' \
--header 'Content-Type: application/json' \
--data-raw '{
    "bc_id": 123456,
    "catalog_id": 123456
}'
```

## Response

| Field | Data Type | Description |
|---|---|---|
| - | - | - |
| code | number | Response code. For the complete list of response codes and descriptions, see [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Response message. For details, see [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | The log ID of the request, which uniquely identifies a request. |
| data | object | Returned data. |
| ↳ list | object[] | Product list. |
| ↳↳ audit | object | Audit information. |
| ↳↳↳ audit_status | string | Ad audit status. It indicates if the ad promoting the product can be deployed. ⏎ Enum values: `approved`, `rejected`, `processing`. |
| ↳↳↳ rejected_info | object[] | Returned only when `audit_status` is `rejected`. ⏎ List of rejection reasons. |
| ↳↳↳↳ reason | string | Rejection reason. |
| ↳↳↳↳ suggestion | string | Suggestions about how to revise to be approved. |
| ↳↳↳↳ affected_placement | string[] | List of placements affected by the rejection. |
| ↳↳↳↳ affected_country | string[] | List of countries or regions affected by the rejection. |
| ↳↳ available | boolean | Returned only for E-commerce and online-to-offline products. ⏎ Whether the product is available for ad creation. ⏎ Supported values: `true`, `false`. |
| ↳↳ ad_creation_eligible | string | Returned only for E-commerce catalog products. ⏎ Whether the E-commerce catalog product can be used to create ads. ⏎ Enum values: `AVAILABLE`, `NOT_AVAILABLE`. ⏎ The `ad_creation_eligible` of an E-commerce catalog product will be `AVAILABLE` only when the following conditions are met:  • `audit_status` is `approved`.  •  `active_status` is `ACTIVATED`.  •  `availability` is `IN_STOCK`, `AVAILABLE_FOR_ORDER`, or `PREORDER`. |
| ↳↳ active_status | string | Whether the product is activated. ⏎ Enum values: `ACTIVATED`, `DEACTIVATED`. ⏎ This field represents the advertiser-controlled online or offline status of the product. However, it does not necessarily imply that the product can be used to create ads. |
| ↳↳ sku_id | string | Advertiser-defined product ID. |
| ↳↳ product_id | string | Product ID. |
| ↳↳ title | string | Product title. |
| ↳↳ description | string | Product description. |
| ↳↳ availability | string | Inventory status. ⏎ • For E-commerce and online-to-offline catalog products, the enum values are:  • `IN_STOCK`: in stock.  • `AVAILABLE_FOR_ORDER`: available for order.  • `PREORDER`: available for pre-order. • `OUT_OF_STOCK`: out of stock. •  `DISCONTINUED`: discontinued. • For hotel catalog products, the enum values are: • `IN_STOCK`: available for booking.  • `OUT_OF_STOCK`: unavailable for booking. • For entertainment catalog products, the enum values are: • `AVAILABLE` • `SUBSCRIBERS_ONLY`  • `ON_DEMAND` • `NOT_AVAILABLE` • For  Auto-Inventory catalog products, the enum values are: • `AVAILABLE`: available for order. • `NOT_AVAILABLE`: Not available for order. • For products or services in a generic catalog, the enum values are: • `IN_STOCK`: in stock. • `AVAILABLE`: available. • `PREORDER`: pre-order. • `OUT_OF_STOCK`: out of stock. • `DISCONTINUED`: discontinued. • `UNAVAILABLE`: unavailable. |
| ↳↳ image_url | string | The URL for the product image. |
| ↳↳ video_url | string | Ad video link. |
| ↳↳ brand | string | Brand information. |
| ↳↳ additional_image_urls | string[] | Additional image URLs for the product. |
| ↳↳ item_group_id | string | Product SPU ID. |
| ↳↳ google_product_category | string | Category information. |
| ↳↳ global_trade_item_number | string | The Global Trade Item Number (GTIN) for the product. |
| ↳↳ manufacturer_part_number | string | The Manufacturer Part Number (MPN) for the product. |
| ↳↳ hotel_id | string | A unique ID for the hotel. |
| ↳↳ name | string | The name of the hotel. |
| ↳↳ hotel_category | string[] | The categories of the hotel. ⏎ For enum values, see [List of values for `hotel_category`](https://business-api.tiktok.com/portal/docs?id=1740497429681153#item-link-List of values for hotel_category). |
| ↳↳ hotel_retailer_id | string | A unique ID for the hotel retailer. |
| ↳↳ address | object | Address information. |
| ↳↳↳ address | string | The address of the hotel, destination, or the dealership. |
| ↳↳↳ street | string | The street address where the product or service is located. |
| ↳↳↳ secondary_address | string | The secondary street address of the hotel. |
| ↳↳↳ tertiary_address | string | The tertiary street address of the hotel. |
| ↳↳↳ city | string | The city where the hotel, destination, or the dealership is located, or the city where the product or service is located. |
| ↳↳↳ region | string | The region (state/province) where the hotel, destination, or the dealership is located, or the state, province, or administrative region where the product or service is located. |
| ↳↳↳ country | string | The country where the hotel or destination is located. |
| ↳↳↳ postal_code | string | The postal code for the dealership's address, or postal or zip code of the product or service location. |
| ↳↳ neighborhood | string | The neighborhood where the hotel or destination is located. ⏎ Example: `Bangkok Old Town`. |
| ↳↳ postal_code | string | The postal code or zip code of the hotel. |
| ↳↳ latitude | float | The latitude of the hotel, destination, or the dealership's location, or the product or service location. ⏎ Example: 37.484100 |
| ↳↳ longitude | float | The longitude of the hotel, destination, or the dealership's location, or the product or service location. ⏎ Example: -122.148252 |
| ↳↳ series_id | string | A unique self-defined ID for the short drama series. |
| ↳↳ series_name | string | The name of the short drama series. |
| ↳↳ target_config | object | Details of the primary targeting region for the short drama series. |
| ↳↳↳ region_code | string | The region code of the primary targeting region for the short drama series. ⏎ Example: `US`. |
| ↳↳↳ currency | string | Currency for the primary targeting region for the short drama series. ⏎ For supported currencies, see the **Code** column in [Budget verification ratio and precision of each currency](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1737585839634433). ⏎ Example: `USD`. |
| ↳↳ recharge | object[] | Information about the recharge for the short drama series. |
| ↳↳↳ type | string | Recharge type for the short drama series. ⏎ Enum values: • `BY_TIERS`: Recharge by tiers. • `SUBSCRIPTION`: Recharge by subscription fee for a time period. • `BY_EPISODES`: Recharge by episodes. |
| ↳↳↳ purchase_unit | string[] | Units for the recharge. ⏎ When `recharge_type` is `BY_TIERS`, the enum values are: • `TIER 1`: tier 1. • `TIER_2`: tier 2. • `TIER 3`: tier 3. • `TIER 4`: tier 4. • `TIER 5`: tier 5.When `recharge_type` is `SUBSCRIPTION`, the enum values are: • `WEEKLY`: weekly. • `MONTHLY`: monthly. • `QUARTERLY`: quarterly. • `YEARLY`: yearly.When `recharge_type` is `BY_EPISODES`, specify one or more numeric strings that represent numbers no more than the total episode count. |
| ↳↳↳ cost | float[] | The prices for the tiers, subscription periods, or episodes. |
| ↳↳ margin_level | string | The percentage of the base price (`price`) for a hotel room that the hotel charges as deposit. ⏎ For instance, a value of 10 means the hotel charges 10 percent of the base price for a hotel room as deposit. |
| ↳↳ loyalty_program | string | The loyalty program offered by the hotel. ⏎ For enum values, see [List of values for `loyalty_program`](https://business-api.tiktok.com/portal/docs?id=1740497429681153#item-link-List of values for loyalty_program). |
| ↳↳ guest_ratings | object[] | Information about guest ratings for the hotel. |
| ↳↳↳ rating_system | string | The rating system for the hotel. |
| ↳↳↳ max_score | integer | The highest score that the hotel has received. |
| ↳↳↳ score | float | The average score of the hotel. |
| ↳↳↳ number_of_reviewers | integer | The number of guests who have reviewed the hotel. |
| ↳↳ star_rating | float | Hotel star rating that is assigned by professional organizations or travel review agencies based on a set of criteria. The highest possible rating is usually 5 stars. Uploading it might help increase Page View Rate. |
| ↳↳ room_type | string[] | The hotel room types. ⏎ For enum values, see [List of values for `room_type`](https://business-api.tiktok.com/portal/docs?id=1740497429681153#item-link-List of values for room_type). |
| ↳↳ priority | integer | The priority of the hotel or flight. ⏎ Value range: 0-5. ⏎ A higher value indicates a higher priority. |
| ↳↳ flight_id | string | A unique ID for the flight. ⏎ The ID will be automatically generated by the system. |
| ↳↳ origin_airport | string | The origin airport of the flight, in the format of a three-letter IATA (International Air Transport Association) code. ⏎ Example: `AAR`. |
| ↳↳ destination_airport | string | The destination airport of the flight, in the format of a three-letter IATA code. ⏎ Example: `ABD`. |
| ↳↳ origin_city | string | The name of the origin city. |
| ↳↳ destination_city | string | The name of the destination city. |
| ↳↳ cabin_class | string | The cabin class of the flight. ⏎ Enum values: • `FIRST_CLASS`: First Class. Premium service with luxurious amenities and private spaces. • `FIRST_CLASS_SUITE`: First Class Suite. Private suites offering luxury and exclusivity. • `BUSINESS_CLASS`: Business Class. Enhanced comfort and amenities for business and leisure travelers. • `BUSINESS_CLASS_SUITE`: Business Class Suite. Spacious and private cabins in business class. • `COMFORT_CLASS`: Comfort Class. Improved seating and service between premium and economy. • `ECONOMY_CLASS`: Economy Class. Standard travel option with basic amenities at an affordable price. • `BASIC_ECONOMY`: Basic Economy. Budget-friendly option with limited services and restrictions. • `STANDARD_ECONOMY`: Standard Economy. Typical economy service with basic features and pricing. • `PREMIUM_ECONOMY`: Premium Economy. Extra legroom and better in-flight services compared to standard economy. • `LIE_FLAT_SEAT`: Lie Flat Seat. Fully reclining seats for optimal comfort on long flights. • `CHARTER_CLASS`: Charter Class. Custom private aircraft hire for tailored travel experiences. • `ELITE_CLASS`: Elite Class. Top-tier service combining the best features of first and business classes. • `QUIET_CLASS`: Quiet Class. Noise-reduced area for a serene travel experience. |
| ↳↳ airline_company | string | The name of the airline company operating the flight. ⏎ Enum values: • `AEROFLOT`: Aeroflot. • `AIR_FRANCE_KLM_GROUP`: Air France-KLM Group. • `ALASKA_AIRLINES`: Alaska Airlines. • `ANA`: ANA. • `AMERICAN_AIRLINES`: American Airlines. • `BRITISH_AIRWAYS`: British Airways. • `CATHAY_PACIFIC`: Cathay Pacific. • `CHINA_SOUTHERN_AIRLINES`: China Southern Airlines. • `CHINA_EASTERN_AIRLINES`: China Eastern Airlines. • `DELTA_AIR_LINES`: Delta Air Lines. • `EMIRATES`: Emirates. • `JAPAN_AIRLINES`: Japan Airlines. • `JETBLUE_AIRWAYS`: JetBlue Airways. • `KLM_ROYAL_DUTCH_AIRLINES`: KLM Royal Dutch Airlines. • `LUFTHANSA_GROUP`: Lufthansa Group. • `QANTAS_AIRWAYS`: Qantas Airways. • `QATAR_AIRWAYS`: Qatar Airways. • `SINGAPORE_AIRLINES`: Singapore Airlines. • `SOUTHWEST_AIRLINES`: Southwest Airlines. • `TURKISH_AIRLINES`: Turkish Airlines. • `UNITED_AIRLINES`: United Airlines. • `VIRGIN_ATLANTIC`: Virgin Atlantic. |
| ↳↳ destination_id | string | A unique ID for the destination. |
| ↳↳ destination_name | string | The name of the destination. |
| ↳↳ postal_code | string | Postal code or zip code for the destination. |
| ↳↳ types | string[] | The type or types of destination. |
| ↳↳ media_title_id | string | A unique ID for the media title item. ⏎ A media title item is a media product that is available for distribution or consumption, such as a movie, TV show, music, or sports game. |
| ↳↳ timeline | string | The timeline for the media title item. ⏎ Enum values:  • `COMING_SOON`: The media title item is not available now, but will be released soon. •  `ONLINE`: The media title item is currently available for purchase or view. • `EXPIRE_SOON`: The media title item will no longer be available for purchase or view soon. |
| ↳↳ category | string | The category of the media title item. ⏎ Enum values:  • `MOVIE`: movie. • `MUSIC`: music. •  `TV_SHOW`: TV show. •  `TV_SERIES`: TV series. • `SPORTS_GAME`: sports game. •  `LIVE_EVENT`: live event. |
| ↳↳ genres | string[] | The genres of the media title item. ⏎ To find out the allowed values for this field, refer to the " List of values for `genres`  " section below. |
| ↳↳ qid | string | QID (or Q number), the unique identifier of the media title item on Wikidata, which consists of the letter "Q" followed by one or more digits. |
| ↳↳ vehicle_id | string | A unique ID for the vehicle. |
| ↳↳ state_of_vehicle | string | The state of the vehicle. ⏎ Enum values: • `NEW`: new. • `USED`: used. • `CPO`: CPO (certified pre-owned). CPO vehicles are used vehicles that have undergone thorough inspection and are typically newer, have lower mileage, and come with additional warranty coverage compared to regular used cars.Example: `USED`. |
| ↳↳ vehicle_type | string | The type of the vehicle. ⏎ Enum values: • `BOAT`: boat. • `CAR_TRUCK`: car or truck. • `COMMERCIAL`: A vehicle used for commercial purposes, such as a delivery truck. • `MOTORCYCLE`: motorcycle. • `POWERSPORT`: powersport. Recreational vehicles that are designed for outdoor activities and adventure, such as a snowmobile. • `RV_CAMPER`: recreational vehicle or camper designed for travel and camping purposes. • `TRAILER`: trailer. • `OTHER`: Any other vehicle type not covered above. |
| ↳↳ make | string | The make (brand) of the vehicle. |
| ↳↳ model | string | The model of the vehicle. |
| ↳↳ trim | string | The trim of the vehicle. The trim represents the distinctive specification package of the vehicle, tailored specifically to that model. |
| ↳↳ year | integer | The year when the vehicle was launched, in the format of `YYYY`. |
| ↳↳ vin | string | The VIN (Vehicle Identification Number) of the vehicle. |
| ↳↳ mileage | object | The mileage of the vehicle. |
| ↳↳↳ value | integer | Mileage value. |
| ↳↳↳ unit | string | Mileage unit. ⏎ Enum values: • `MILE`: mile. • `KILOMETER`: kilometer. |
| ↳↳ body_style | string | The body style of the vehicle. ⏎ Enum values: • `CONVERTIBLE`: convertible. • `COUPE`: coupe. • `CROSSOVER`: crossover. • `HATCHBACK`: hatchback. • `MINIVAN`: minivan. • `SMALL_CAR`: small car. • `SEDAN`: sedan. • `SUV`: SUV. • `TRUCK`: truck. • `VAN`: van. • `WAGON`: wagon. • `OTHER`: other. |
| ↳↳ exterior_color | string | The exterior color of the vehicle. |
| ↳↳ interior_color | string | The interior color of the vehicle. |
| ↳↳ transmission | string | The transmission type of the vehicle. ⏎ Enum values: • `AUTOMATIC`: automatic. • `MANUAL`: manual. |
| ↳↳ drivetrain | string | The drivetrain type of the vehicle. ⏎ Enum values: • `4X2`: four-wheel drive vehicle with two wheel drive (2WD). The drivetrain delivers power to either the front wheels or the rear wheels. • `4X4`: four-wheel drive vehicle with four wheel drive. The drivetrain delivers power to all four wheels. • `AWD`: all-wheel drive. The drivetrain delivers power to all wheels continuously. • `FWD`: front-wheel drive. The drivetrain delivers power to the front wheels only. • `RWD`: rear-wheel drive. The drivetrain delivers power to the rear wheels only. • `OTHER`: any other drivetrain type not covered above, such as electric vehicles with unique drivetrain styles. |
| ↳↳ fuel_type | string | The fuel type of the vehicle. ⏎ Enum values: • `DIESEL`: diesel. • `ELECTRIC`: electric. • `FLEX`: flex fuel, a blend of gasoline and ethanol. • `GASOLINE`: gasoline. • `HYBRID`: hybrid. • `OTHER`: other. |
| ↳↳ dealer | object | Detailed information about the dealership. |
| ↳↳↳ dealer_id | string | A unique ID for the dealership. |
| ↳↳↳ dealer_name | string | The name of the dealership. |
| ↳↳↳ dealer_phone | string | The phone number of the dealership. |
| ↳↳↳ stock_number | string | The stock number assigned to the vehicle by the dealership. The stock number is usually assigned when the vehicle physically arrives at the dealership's lot. |
| ↳↳ date_first_on_lot | string | The date when the vehicle physically arrives at the dealership's lot, in the format of `YYYY-MM-DD`. |
| ↳↳ days_on_lot | integer | The number of days the vehicle has been on the dealership's lot. |
| ↳↳ item_id | string | A unique, self-defined ID for the product or service. |
| ↳↳ listing_id | string | A unique ID for the listing. |
| ↳↳ profession | object | Product other information. |
| ↳↳↳ age_group | string | Age group of products. ⏎ Enum values:`NEW_BORN`, `INFANT`, `TODDLER`, `KIDS`, `ADULT`. ⏎ Example: `ADULT`. |
| ↳↳↳ color | string | Color of products. |
| ↳↳↳ condition | string | Current status of products. ⏎ • For E-commerce and online-to-offline catalog products, the enum values are `NEW`, `REFURBISHED`, and `USED`.  • For entertainment catalog products, the enum values are `NEW`  and `USED`. • For Auto-Inventory catalog products, the enum values are:  • `EXCELLENT`: excellent. • `GOOD`: good. • `FAIR`: fair. • `POOR`: poor. • `OTHER`: other. |
| ↳↳↳ gender | string | The targeted gender for the product. The accuracy of this field is important to ensure products are delivered to the intended gender group.  Enum values: `MALE`, `FEMALE`, `UNISEX`. |
| ↳↳↳ material | string | Materials used in products, such as cotton, denim or leather. |
| ↳↳↳ pattern | string | Pattern or graphic printing on a product. |
| ↳↳↳ product_category | string | The category that the product belongs to. ⏎ Only the first three levels are required. |
| ↳↳↳ shipping | string | The type of shipping for the product. ⏎ Recommended format: `COUNTRY:STATE:SHIPPING_TYPE: PRICE`. ⏎ Use ";" to separate different regions. ⏎ Example: `US:CA:Ground:9.99 USD`. |
| ↳↳↳ shipping_weight | string | The shipping weight of the product. ⏎ The allowed units are `lb`, `oz`, `g`, `kg`. ⏎ Example: 1 oz, 1 kg. |
| ↳↳↳ size | string | Size of the item. |
| ↳↳↳ tax | string | Product tax. |
| ↳↳↳ offer_type | string | The type of offer. |
| ↳↳↳ term_length | string | The duration for which the offer applies. |
| ↳↳↳ offer_term_qualifier | string | The unit for term of the offer. |
| ↳↳↳ amount_price | string | The amount of the offer. |
| ↳↳↳ amount_percentage | string | The percentage for the APR in a finance offer. |
| ↳↳↳ amount_qualifier | string | The qualifier for the `amount_price` or `amount_percentage`. |
| ↳↳↳ downpayment | string | The downpayment at the time of purchase or lease. |
| ↳↳↳ downpayment_qualifier | string | Qualifier for the downpayment. |
| ↳↳↳ offer_disclaimer | string | The full text of the offer disclaimer to appear in the in-app pop-up. |
| ↳↳↳ offer_disclaimer_url | string | A URL that directs users to additional information related to the offer disclaimer, in the format of `http://xxx` or `https://xxx`. |
| ↳↳↳ emission_disclaimer | string | The text of the emission disclaimer to appear within the in-app pop-up. |
| ↳↳↳ emission_disclaimer_url | string | A URL that directs users to additional information related to the emission disclaimer, in the format of `http://xxx` or `https://xxx`. |
| ↳↳↳ emission_overlay_disclaimer | string | The short text of the disclaimer to appear on-screen in the disclaimer banner. |
| ↳↳↳ emission_image_link | string | The link to an image showing the emission level, in the format of `http://xxx` or `https://xxx`. |
| ↳↳↳ company_type | string | The company type for the short drama series. ⏎ Enum values: • `COPYRIGHT_HOLDER`: copyright holder. • `DISTRIBUTOR`: distributor. |
| ↳↳↳ copyright_holder_name | string | The name of the copyright holder company. |
| ↳↳↳ app_id | string | The App ID of the app to promote in your ads. ⏎ To obtain a list of App IDs within your ad account, use [/app/list/](43-events-1-0-p1.md#doc-1740859313270786). |
| ↳↳↳ minis_id | string | Mini program ID. |
| ↳↳↳ total_episodes | number | The number of episodes in the short drama series. |
| ↳↳↳ initial_paid_episodes | number | The episode number at which viewers are required to pay to continue watching the short drama series. |
| ↳↳↳ per_episode_duration | number | The average duration of each episode in minutes. |
| ↳↳↳ spoken_language | string | The language that actors in the original short drama series speak. ⏎ Enum values: • `ar`: Arabic. • `de`: German. • `cs`: Czech. • `en`: English. • `es`: Spanish. • `fr`: French. • `he`: Hebrew. • `hi`: Hindi. • `id`: Indonesian. • `it`: Italian. • `ja`: Japanese. • `ko`: Korean. • `ms`: Malay. • `pl`: Polish. • `pt`: Portuguese. • `ro`: Romanian. • `ru`: Russian. • `ta`: Tamil. • `th`: Thai. • `tr`: Turkish. • `vi`: Vietnamese. • `zh`: Simplified Chinese. • `zh-hant`: Traditional Chinese. |
| ↳↳↳ subtitle_language | string | The language used for the subtitles in the short drama series. ⏎ Enum values: • `ar`: Arabic. • `de`: German. • `cs`: Czech. • `en`: English. • `es`: Spanish. • `fr`: French. • `he`: Hebrew. • `hi`: Hindi. • `id`: Indonesian. • `it`: Italian. • `ja`: Japanese. • `ko`: Korean. • `ms`: Malay. • `pl`: Polish. • `pt`: Portuguese. • `ro`: Romanian. • `ru`: Russian. • `ta`: Tamil. • `th`: Thai. • `tr`: Turkish. • `vi`: Vietnamese. • `zh`: Simplified Chinese. • `zh-hant`: Traditional Chinese. |
| ↳↳↳ production_type | string | Production type, whether the short drama series is locally produced or translated for export. ⏎ Enum values: • `LOCAL`: Local drama. The short drama features local actors, and the language for actors, narration, and subtitles is the local official language. • `TRANSLATION`: Translated drama. The short drama is packaged for international distribution with added subtitles, narration, and dubbing in another language. |
| ↳↳↳ target_audience | string | The target audience for the short drama series. ⏎ Enum values: • `MALE`: Male. The short drama is primarily targeted at male audiences, often centered around a male protagonist or narrated from a male perspective. Themes typically include the accumulation of power, wealth, and prestige, the enhancement of abilities, and strategic planning. • `FEMALE`: Female. The short drama is primarily targeted at female audiences, often centered around a female protagonist or narrated from a female perspective. These dramas usually contain elements of romance and love. • `NEUTRAL`: Neutral. The short drama doesn't have a specific gender target audience. |
| ↳↳↳ characters | string[] | The list of characters in the short drama series. ⏎ For enum values, see [List of values for `characters`](28-catalog-products-p1.md#doc-1740497429681153). |
| ↳↳↳ genres | string[] | The genres of the short drama series as indicated by the main storyline or plot. ⏎ For enum values, see [List of values for mini series `genres`](28-catalog-products-p1.md#doc-1740497429681153). |
| ↳↳↳ historical_context | string[] | The historical background or setting of the short drama series. ⏎ For enum values, see [List of values for `historical_context`](28-catalog-products-p1.md#doc-1740497429681153). |
| ↳↳↳ actors | string[] | The names of the actors in the short drama series. |
| ↳↳↳ rating | double | The user rating for the product or service or the listing. |
| ↳↳↳ availability_type | string | The method used to define the geographic areas where the product can be sold or the service can be provided. ⏎ This determines which availability field will take effect during ad delivery. ⏎ Enum values: • `REGION`: Locations or regions. Set locations or regions where your product or service is available via `availability_region`. • `DMA`: DMAs. Set DMAs where your product or service is available via `availability_dma`. • `RADIUS`: Radius range. Set a custom radius around where your product or service is available via `availability_circle_radius` and `availability_circle_radius_unit`. • `POSTAL_CODE`: Postal code. Set specific postal codes or zip codes where your product or service is available via `availability_postal_codes`. |
| ↳↳↳ availability_region | string[][] | Returned when `availability_type` is `REGION`. ⏎ A list of regions where the product can be sold or the service can be provided. ⏎ This field is an array of string arrays, where each string array represents a specific location. ⏎ Example: `[["Arizona","Maricopa","Peoria"],["Alabama","Jefferson","Birmingham"]]` is a valid array containing two location arrays, each with 3 strings under the 499-character limit. |
| ↳↳↳ availability_dma | string[] | Returned when `availability_type` is `DMA`. ⏎ A list of DMAs where the product can be sold or the service can be provided. ⏎ Example: `["501","803"]` (New York and Los Angeles) |
| ↳↳↳ availability_circle_radius | string | Returned for an online-to-offline product or when `availability_type` is `RADIUS`. ⏎ The circle radius of the product or service defining a circular availability area. ⏎ Example: 20. |
| ↳↳↳ availability_circle_radius_unit | string | Returned for an online-to-offline product or when `availability_type` is `RADIUS`. ⏎ The unit for `availability_circle_radius`. ⏎ Enum values: • `KM`: kilometer. • `MI`: mile. |
| ↳↳↳ availability_postal_codes | string[] | Returned when `availability_type` is `POSTAL_CODE`. ⏎ A list of postal codes representing the areas where the product can be sold or the service can be provided. ⏎ Example: `["10001", "90001"]`. |
| ↳↳↳ custom_number_0 | double | A custom numeric attribute for product management. |
| ↳↳↳ custom_number_1 | double | A custom numeric attribute for product management. |
| ↳↳↳ custom_number_2 | double | A custom numeric attribute for product management. |
| ↳↳↳ custom_number_3 | double | A custom numeric attribute for product management. |
| ↳↳↳ custom_number_4 | double | A custom numeric attribute for product management. |
| ↳↳ price | object | Price information. |
| ↳↳↳ price | float | The base price. ⏎ For destination catalog products, this field represents the average or lowest price for the destination. The `description` field may provide information on whether this is the average price or the lowest price. ⏎ For generic catalogs, this field represents the price of a single product or service unit. |
| ↳↳↳ currency | string | Unit of currency that must match the unit of currency of catalog's target country. If you do not provide it, we will use the default unit of currency of the catalog's target country. |
| ↳↳↳ sale_price | float | The discounted price. |
| ↳↳↳ sale_price_effective_date | string[] | Start and end date and time of sale. |
| ↳↳ landing_page | object | Landing page information. |
| ↳↳↳ landing_page_url | string | URL of the landing page where you can view or purchase the product. |
| ↳↳↳ ios_url | string | Custom scheme for iOS apps as URL. For iOS, provide both iPhone & iPad app information if they are different from the regular iOS app. |
| ↳↳↳ ios_app_store_id | string | App Store ID for the iOS app. |
| ↳↳↳ ios_app_name | string | The iOS App name to display. |
| ↳↳↳ iphone_app_store_id | string | App Store ID for the iPhone app. |
| ↳↳↳ iphone_app_name | string | The iphone App name to display. |
| ↳↳↳ ipad_app_store_id | string | App Store ID for the iPad app. |
| ↳↳↳ ipad_app_name | string | The iPad App name to display. |
| ↳↳↳ android_url | string | Custom scheme for Android apps as URL. |
| ↳↳↳ android_package | string | The Android package name. |
| ↳↳↳ android_app_name | string | The Android App name to display. |
| ↳↳ extra_info | object | Additional information. |
| ↳↳↳ custom_label_0 | string | Additional information about the products you want to include. |
| ↳↳↳ custom_label_1 | string | Additional information about the products you want to include. |
| ↳↳↳ custom_label_2 | string | Additional information about the products you want to include. |
| ↳↳↳ custom_label_3 | string | Additional information about the products you want to include. |
| ↳↳↳ custom_label_4 | string | Additional information about the products you want to include. |
| ↳↳↳ custom_label_5 | string | Additional information about the products you want to include. |
| ↳↳↳ custom_label_6 | string | Additional information about the products you want to include. |
| ↳↳↳ internal_label_0 | string | An internal label assigned to the hotel or flight. You can use internal labels to filter items while creating product sets. These labels are exclusively visible to you. ⏎ Length Limit: 100 characters. ⏎ If you are using custom labels (`custom_label_0` to `custom_label_4`) for filtering items during product set creation, consider switching to internal labels. Unlike custom labels, internal labels can be added or modified as needed without the need for submitting items for review each time, avoiding potential interruptions in ad delivery. |
| ↳↳↳ internal_label_1 | string | An internal label assigned to the hotel or flight. You can use internal labels to filter items while creating product sets. These labels are exclusively visible to you. ⏎ Length Limit: 100 characters. ⏎ If you are using custom labels (`custom_label_0` to `custom_label_4`) for filtering items during product set creation, consider switching to internal labels. Unlike custom labels, internal labels can be added or modified as needed without the need for submitting items for review each time, avoiding potential interruptions in ad delivery. |
| ↳↳ image_status | string | Storage status of the product image. Enum values: • `PROCESSING`: The image is being stored.   • `SUCCESS`: The image is stored successfully.  • `FAIL`: The image is not stored successfully.  • `FILTERED`: The image was stored successfully but cannot be used because it does not meet the size requirements (must be equal to or larger than 500 px). For such images, the product audit status (`audit_status`) will stay at `processing` until you upload a new image. • `NOT_SUPPORTED`: The image format is not supported. • `NO_FOUND`: Cannot find the resource via the URL. Please ensure the URL is valid, and the file is publicly accessible. |
| ↳↳ additional_product_list | object[] | Returned when you have configured additional targeting regions for the short drama series. ⏎ A list of additional targeting region settings for the short drama series of the same `series_id`. |
| ↳↳↳ audit | object | Audit information. |
| ↳↳↳↳ audit_status | string | Ad audit status. It indicates if the ad promoting the product can be deployed. ⏎ Enum values: `approved`, `rejected`, `processing`. |
| ↳↳↳ rejected_info | object[] | Returned only when `audit_status` is `rejected`. ⏎ List of rejection reasons. |
| ↳↳↳↳ reason | string | Rejection reason. |
| ↳↳↳↳ suggestion | string | Suggestions about how to revise to be approved. |
| ↳↳↳↳ affected_placement | string[] | List of placements affected by the rejection. |
| ↳↳↳↳ affected_country | string[] | List of countries or regions affected by the rejection. |
| ↳↳↳ active_status | string | Whether the product is activated. ⏎ Enum values: `ACTIVATED`, `DEACTIVATED`. ⏎ This field represents the advertiser-controlled online or offline status of the product. However, it does not necessarily imply that the product can be used to create ads. |
| ↳↳↳ image_status | string | Storage status of the product image. ⏎ Enum values: • `PROCESSING`: The image is being stored. • `SUCCESS`: The image is stored successfully. • `FAIL`: The image is not stored successfully. • `FILTERED`: The image was stored successfully but cannot be used because it does not meet the size requirements (must be equal to or larger than 500 px). For such images, the product audit status (`audit_status`) will stay at `processing` until you upload a new image. • `NOT_SUPPORTED`: The image format is not supported. • `NO_FOUND`: Cannot find the resource via the URL. Please ensure the URL is valid, and the file is publicly accessible. |
| ↳↳↳ product_id | string | Product ID. |
| ↳↳↳ series_id | string | A unique self-defined ID for the short drama series. |
| ↳↳↳ series_name | string | The name of the short drama series. |
| ↳↳↳ target_config | object | Details of the additional targeting region for the short drama series. |
| ↳↳↳↳ region_code | string | The region code of the additional targeting region for the short drama series. ⏎ Example: `US`. |
| ↳↳↳↳ currency | string | Currency for the additional targeting region for the short drama series. ⏎ For supported currencies, see the **Code** column in [Budget verification ratio and precision of each currency](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1737585839634433). ⏎ Example: `USD`. |
| ↳↳↳ image_url | string | The URL for the short drama series poster image. |
| ↳↳↳ recharge | object[] | Information about the recharge for the short drama series. |
| ↳↳↳↳ type | string | Recharge type for the short drama series. ⏎ Enum values: • `BY_TIERS`: Recharge by tiers. • `SUBSCRIPTION`: Recharge by subscription fee for a time period. • `BY_EPISODES`: Recharge by episodes. |
| ↳↳↳↳ purchase_unit | string[] | Units for the recharge. ⏎ When `recharge_type` is `BY_TIERS`, the enum values are: • `TIER 1`: tier 1. • `TIER_2`: tier 2. • `TIER 3`: tier 3. • `TIER 4`: tier 4. • `TIER 5`: tier 5.When `recharge_type` is `SUBSCRIPTION`, the enum values are: • `WEEKLY`: weekly. • `MONTHLY`: monthly. • `QUARTERLY`: quarterly. • `YEARLY`: yearly.When `recharge_type` is `BY_EPISODES`, specify one or more numeric strings that represent numbers no more than the total episode count. |
| ↳↳↳↳ cost | float[] | The prices for the tiers, subscription periods, or episodes. |
| ↳↳↳ profession | object | Product other information. |
| ↳↳↳↳ company_type | string | The company type for the short drama series. ⏎ Enum values: • `COPYRIGHT_HOLDER`: copyright holder. • `DISTRIBUTOR`: distributor. |
| ↳↳↳↳ copyright_holder_name | string | The name of the copyright holder company. |
| ↳↳↳↳ app_id | string | The App ID of the app to promote in your ads. ⏎ To obtain a list of App IDs within your ad account, use [/app/list/](43-events-1-0-p1.md#doc-1740859313270786). |
| ↳↳↳↳ minis_id | string | Mini program ID. |
| ↳↳↳↳ total_episodes | number | The number of episodes in the short drama series. |
| ↳↳↳↳ initial_paid_episodes | number | The episode number at which viewers are required to pay to continue watching the short drama series. |
| ↳↳↳↳ per_episode_duration | number | The average duration of each episode in minutes. |
| ↳↳↳↳ spoken_language | string | The language that actors in the original short drama series speak. ⏎ Enum values: • `ar`: Arabic. • `de`: German. • `cs`: Czech. • `en`: English. • `es`: Spanish. • `fr`: French. • `he`: Hebrew. • `hi`: Hindi. • `id`: Indonesian. • `it`: Italian. • `ja`: Japanese. • `ko`: Korean. • `ms`: Malay. • `pl`: Polish. • `pt`: Portuguese. • `ro`: Romanian. • `ru`: Russian. • `ta`: Tamil. • `th`: Thai. • `tr`: Turkish. • `vi`: Vietnamese. • `zh`: Simplified Chinese. • `zh-hant`: Traditional Chinese. |
| ↳↳↳↳ subtitle_language | string | The language used for the subtitles in the short drama series. ⏎ Enum values: • `ar`: Arabic. • `de`: German. • `cs`: Czech. • `en`: English. • `es`: Spanish. • `fr`: French. • `he`: Hebrew. • `hi`: Hindi. • `id`: Indonesian. • `it`: Italian. • `ja`: Japanese. • `ko`: Korean. • `ms`: Malay. • `pl`: Polish. • `pt`: Portuguese. • `ro`: Romanian. • `ru`: Russian. • `ta`: Tamil. • `th`: Thai. • `tr`: Turkish. • `vi`: Vietnamese. • `zh`: Simplified Chinese. • `zh-hant`: Traditional Chinese. |
| ↳↳↳↳ production_type | string | Production type, whether the short drama series is locally produced or translated for export. ⏎ Enum values: • `LOCAL`: Local drama. The short drama features local actors, and the language for actors, narration, and subtitles is the local official language. • `TRANSLATION`: Translated drama. The short drama is packaged for international distribution with added subtitles, narration, and dubbing in another language. |
| ↳↳↳↳ target_audience | string | The target audience for the short drama series. ⏎ Enum values: • `MALE`: Male. The short drama is primarily targeted at male audiences, often centered around a male protagonist or narrated from a male perspective. Themes typically include the accumulation of power, wealth, and prestige, the enhancement of abilities, and strategic planning. • `FEMALE`: Female. The short drama is primarily targeted at female audiences, often centered around a female protagonist or narrated from a female perspective. These dramas usually contain elements of romance and love. • `NEUTRAL`: Neutral. The short drama doesn't have a specific gender target audience. |
| ↳↳↳↳ characters | string[] | The list of characters in the short drama series. ⏎ For enum values, see [List of values for `characters`](28-catalog-products-p1.md#doc-1740497429681153). |
| ↳↳↳↳ genres | string[] | The genres of the short drama series as indicated by the main storyline or plot. ⏎ For enum values, see [List of values for mini series `genres`](28-catalog-products-p1.md#doc-1740497429681153). |
| ↳↳↳↳ historical_context | string[] | The historical background or setting of the short drama series. ⏎ For enum values, see [List of values for `historical_context`](28-catalog-products-p1.md#doc-1740497429681153). |
| ↳↳↳↳ actors | string[] | The names of the actors in the short drama series. |
| ↳↳↳ video_url | string | Ad video link. |
| ↳↳↳ additional_image_urls | string[] | Additional image URLs for the product. ⏎ **Note**: The value of this field will be null. |
| ↳↳↳ global_trade_item_number | string | The Global Trade Item Number (GTIN) for the product. ⏎ **Note**: The value of this field will be null. |
| ↳↳↳ manufacturer_part_number | string | The Manufacturer Part Number (MPN) for the product. ⏎ **Note**: The value of this field will be null. |
| ↳↳↳ landing_page | object | Landing page information. ⏎ **Note**: The value of this field will be null. |
| ↳↳↳↳ landing_page_url | string | URL of the landing page where you can view or purchase the product. |
| ↳↳↳ extra_info | object | Additional information. ⏎ **Note**: The value of this field will be null. |
| ↳↳↳↳ custom_label_0 | string | Additional information about the products you want to include. |
| ↳↳↳↳ custom_label_1 | string | Additional information about the products you want to include. |
| ↳↳↳↳ custom_label_2 | string | Additional information about the products you want to include. |
| ↳↳↳↳ custom_label_3 | string | Additional information about the products you want to include. |
| ↳↳↳↳ custom_label_4 | string | Additional information about the products you want to include. |
| ↳ page_info | object | Pagination information. |
| ↳↳ page | number | Current page number. |
| ↳↳ page_size | number | Page size. |
| ↳↳ total_number | number | Total number of results. |
| ↳↳ total_page | number | Total pages of results. |

#### List of values for `genres`

| Value | Description |
|---|---|
| `ACTION` | action |
| `ADULT_ANIMATION` | adult animation |
| `ADVENTURE` | adventure |
| `ANIMATION` | animation |
| `BIOGRAPHICAL` | biographical |
| `BLACK_COMEDY` | black comedy |
| `BUDDY` | buddy |
| `COMEDY` | comedy |
| `COMIC` | comic |
| `COOKING_SHOW` | cooking show |
| `CRIME` | crime |
| `DISASTER` | disaster |
| `DOCUMENTARY` | documentary |
| `DRAMA` | drama |
| `FAMILY` | family |
| `FANTASY` | fantasy |
| `GAME_SHOW` | game show |
| `HISTORY` | history |
| `HORROR` | horror |
| `LGBT` | LGBT |
| `MARTIAL_ARTS` | martial arts |
| `MILITARY` | military |
| `MUSIC` | music |
| `POLICE` | police |
| `POLICE_PROCEDURAL` | police procedural |
| `POLITIC` | politic |
| `REALITY_TV` | reality TV |
| `ROAD` | road |
| `ROMANCE` | romance |
| `SATIRE` | satire |
| `SCIENCE_FICTION` | science fiction |
| `SITCOM` | sitcom |
| `SOAP_OPERA` | soap opera |
| `SPORT` | sport |
| `SPY` | spy |
| `STEAMPUNK` | steampunk |
| `SUPERHERO` | superhero |
| `TALK_SHOW` | talk show |
| `TEEN` | teen |
| `THRILLER` | thriller |
| `TIME_TRAVEL` | time travel |
| `VAMPIRE` | vampire |
| `WAR` | war |
| `WESTERN` | western |
| `ZOMBIE` | zombie |

### Example
```http
// curl
HTTPS/1.1 200 OK
{
"message": "OK",
"code": 0,
"data": {
    "page_info": {
        "total_number": 2,
        "page": 1,
        "page_size": 100,
        "total_page": 1
    },
    "list": [
        {
            "audit": {
                    "audit_status": "rejected",
                    "rejected_info": [
                        {
                            "reason": "The product/service promoted on the ad/landing page belongs to a prohibited industry in your ad targeting location(s) as taking our own business evaluation, users' experience and value of advertisement impact, etc into consideration.",
                            "suggestion": "Please change the promoted product/service in your ad or change the targeting location in your ad group settings according to our policy. https://ads.tiktok.com/help/article?aid=6685586866860720134 Learn More.",
                            "affected_placement": [
                                "PLACEMENT_TIKTOK",
                                "PLACEMENT_PANGLE"
                            ],
                            "affected_country": [
                                "US"
                            ]
                        }
                    ]
                },
            "sku_id": "tiktok_item_12423",
            "product_id": "6872175464299923205",
            "title": "qgs test product",
            "manufacturer_part_number": "",
            "profession": {
                "product_category": "Apparel & Accessories > Clothing > Shirts",
                "color": "red",
                "pattern": "stripes1",
                "material": "cotton",
                "tax": "xxx",
                "shipping_weight": "1 kg",
                "shipping": "US:CA:Ground:9.99 USD",
                "condition": "USED",
                "size": "L"
            },
            "brand": "xiaoru",
            "landing_page": {
                "ios_app_store_id": "https://ios_app_store.com",
                "iphone_app_name": "iphone_app_name",
                "android_package": "a.b.com",
                "iphone_app_store_id": "https://iphone_app_store.com",
                "ios_app_name": "ios_app_name",
                "ipad_app_name": "ipad_app_name",
                "landing_page_url": "https://ads.tiktok.com",
                "android_app_name": "android_app_name",
                "android_url": "https://www.android.com",
                "ios_url": "https://www.ios.com",
                "ipad_app_store_id": "https://ipad_app_store.com"
            },
            "image_url": "http://p1.ipstatp.com/origin/ad-site-i18n/201912265d0d606810c7e88e46248eef",
            "additional_image_urls": [
                "http://p1.ipstatp.com/origin/ad-site-i18n/201912265d0d606810c7e88e46248eef",
                "http://p1.ipstatp.com/origin/ad-site-i18n/201912265d0d606810c7e88e46248eef"
            ],
            "extra_info": {
                "custom_label_1": "b",
                "custom_label_0": "a",
                "custom_label_4": "e"
            },
            "global_trade_item_number": "",
            "video_url": "ad-site-i18n/201911045d0db9f0eb2f8cc14bb4ae1a",
            "google_product_category": "2.22",
            "price": {
                "sale_price_effective_date": [
                    "2017-12-11 04:36",
                    "2017-12-31 12:06"
                ],
                "currency": "USD",
                "price": 100.0,
                "sale_price": 30.0
            },
            "availability": "AVAILABLE_FOR_ORDER",
            "item_group_id": "1.11",
            "description": "qgs test product description"
        },
        {
            "audit": {
                    "audit_status": "processing"
                },
            "sku_id": "tiktok_item_12424",
            "product_id": "6872175464299939589",
            "title": "qgs test product",
            "manufacturer_part_number": "4.44",
            "product_detail": {
                "color": "red",
                "material": "cotton",
                "tax": "xxx",
                "shipping": "US:CA:Ground:9.99 USD",
                "condition": "USED",
                "size": "L"
            },
            "brand": "xiaoru",
            "landing_page": {
                "ios_app_store_id": "https://ios_app_store.com",
                "iphone_app_name": "iphone_app_name",
                "android_package": "a.b.com",
                "iphone_app_store_id": "https://iphone_app_store.com",
                "ios_app_name": "ios_app_name",
                "ipad_app_name": "ipad_app_name",
                "landing_page_url": "https://ads.tiktok.com",
                "android_app_name": "android_app_name",
                "android_url": "https://www.android.com",
                "ios_url": "https://www.ios.com",
                "ipad_app_store_id": "https://ipad_app_store.com"
            },
            "image_url": "http://p1.ipstatp.com/origin/ad-site-i18n/201912265d0d606810c7e88e46248eef",
            "additional_image_urls": [],
            "extra_info": {},
            "global_trade_item_number": "3.33",
            "video_url": "ad-site-i18n/201911045d0db9f0eb2f8cc14bb4ae1a",
            "google_product_category": "2.22",
            "price_info": {
                "sale_price_effective_date": [],
                "currency": "USD",
                "price": 100.0,
                "sale_price": 0.0
            },
            "availability": "AVAILABLE_FOR_ORDER",
            "item_group_id": "1.11",
            "description": "qgs test product description"
        }
    ]
},
"request_id": "2020091405213901023125321411850"
}
```

### Mã nguồn Python mẫu trích xuất danh sách sản phẩm Catalog (GET /catalog/product/get/)
```python
import requests
import json

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
BC_ID = "YOUR_BC_ID"
CATALOG_ID = "YOUR_CATALOG_ID"
BASE_URL = "https://business-api.tiktok.com/open_api/v1.3"

headers = {
    "Access-Token": ACCESS_TOKEN
}

def get_catalog_products(bc_id, catalog_id, page=1, page_size=100):
    """Trích xuất danh sách sản phẩm trong Catalog kèm phân trang."""
    url = f"{BASE_URL}/catalog/product/get/"
    params = {
        "bc_id": bc_id,
        "catalog_id": catalog_id,
        "page": page,
        "page_size": page_size,
        "product_available_type": "AVAILABLE"
    }
    
    res = requests.get(url, headers=headers, params=params).json()
    if res.get("code") == 0:
        data = res.get("data", {})
        products = data.get("list", [])
        page_info = data.get("page_info", {})
        print(f"Lấy thành công trang {page}/{page_info.get(total_page)} ({len(products)} sản phẩm)")
        for p in products:
            print(f" - [{p.get(product_id)}] SKU: {p.get(sku_id)} | Title: {p.get(title)} | Price: {p.get(price_info, {}).get(price)}")
        return products
    else:
        print(f"Lỗi truy vấn: {res.get(code)} - {res.get(message)}")
        return []

if __name__ == "__main__":
    get_catalog_products(BC_ID, CATALOG_ID)
```
