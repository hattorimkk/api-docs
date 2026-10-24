# Danh mục creative (Creative Portfolios)

Nhóm API Danh mục Creative (Creative Portfolios) cung cấp các công cụ tạo lập, tra cứu, quản lý và xóa các thành phần tương tác bổ sung (Interactive Add-ons) trong quảng cáo TikTok. Các thành phần tương tác này bao gồm: văn bản kêu gọi hành động (CTA), thẻ hiển thị (Display Card), thẻ du lịch (Hotel/Flight/Destination Card), thẻ tải ứng dụng (Download Card), thẻ thông tin trang web (Website Info Card), thẻ hàng tồn kho/xe cộ (Inventory Card), thẻ sản phẩm (Product Card), ô sản phẩm (Product Tiles), nhãn dán đếm ngược/mã quà tặng (Countdown & Gift Code Stickers), huy hiệu giới thiệu dạng bật lên (Pop-up Showcase), cử chỉ tương tác (Gestures) và hiệu ứng Superlike.

| Endpoint | Method | Đường dẫn | Mục đích |
|---|---|---|---|
| Tổng quan danh mục creative | - | - | Khái quát hệ thống tiện ích sáng tạo tương tác bổ sung (Interactive Add-ons) |
| Tạo danh mục creative | `POST` | `/open_api/v1.3/creative/portfolio/create/` | Tạo mới một tiện ích tương tác sáng tạo (Display Card, Sticker, Gesture, Superlike...) |
| Lấy thông tin danh mục creative theo ID | `GET` | `/open_api/v1.3/creative/portfolio/get/` | Tra cứu chi tiết cấu hình của một tiện ích sáng tạo theo mã định danh |
| Lấy danh sách danh mục creative của tài khoản | `GET` | `/open_api/v1.3/creative/portfolio/list/` | Lấy danh sách tiện ích sáng tạo theo loại hoặc bộ lọc ID |
| Xóa danh mục creative | `POST` | `/open_api/v1.3/creative/portfolio/delete/` | Xóa hàng loạt các tiện ích sáng tạo theo danh sách ID |

---

## Tổng quan danh mục creative (`Creative Portfolios`)
<a id="doc-1739091934311426"></a>
<!-- doc_id: 1739091934311426 -->

Nhóm API Creative Portfolios hỗ trợ nhà quảng cáo quản lý các gói tiện ích sáng tạo và thành phần tương tác (interactive add-ons) nhằm tối ưu hóa tỷ lệ chuyển đổi, kích thích hành vi khám phá và tăng cường tương tác trực quan cho video quảng cáo trên TikTok.

Nhóm này bao gồm các endpoint sau:
- [Tạo danh mục creative](36-creative-portfolios.md#doc-1739091950439426): Tạo tiện ích tương tác mới (Display Card, Sticker, Gesture, Superlike, CTA...).
- [Lấy thông tin danh mục creative theo ID](36-creative-portfolios.md#doc-1739092113671170): Xem cấu hình chi tiết của một tiện ích theo `creative_portfolio_id`.
- [Lấy danh sách danh mục creative của tài khoản](36-creative-portfolios.md#doc-1766324010279938): Lấy danh sách tiện ích sáng tạo đã tạo trong tài khoản quảng cáo.
- [Xóa danh mục creative](36-creative-portfolios.md#doc-1834560049625089): Xóa các tiện ích sáng tạo không còn sử dụng.

---

## Tạo danh mục creative (`Create a portfolio`)
<a id="doc-1739091950439426"></a>
<!-- doc_id: 1739091950439426 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/creative/portfolio/create/`

**Mục đích**: Tạo một tiện ích sáng tạo tương tác bổ sung (creative portfolio / interactive add-on). Mỗi lần gọi API, bạn chỉ có thể tạo một tiện ích duy nhất.

> [!NOTE]
> - **Quy tắc sử dụng tiện ích theo mục tiêu quảng cáo**:
>   - **Thẻ thông tin trang web (`WEB_INFO_CARD`)**: Chỉ dùng cho quảng cáo đấu giá với mục tiêu chuyển đổi trang web `WEB_CONVERSIONS` hoặc lưu lượng truy cập `TRAFFIC` (với `promotion_type` là `WEBSITE`).
>   - **Thẻ xe cộ/hàng tồn kho (`INVENTORY_CARD`)**: Chỉ dùng cho quảng cáo ô tô (Automotive Ads).
>   - **Thẻ sản phẩm (`PRODUCT_CARD`)**: Chỉ dùng cho quảng cáo mua sắm qua video (Video Shopping Ads).
>   - **Khung ô sản phẩm (`PRODUCT_TILE`)**: Chỉ dùng cho Video Shopping Ads có nguồn sản phẩm từ danh mục (Catalog) chứa tối thiểu 4 sản phẩm đã được phê duyệt (`approved`). Tính năng này yêu cầu nằm trong danh sách cho phép (allowlist).
>   - **Nhãn dán đếm ngược (`STICKER` loại đếm ngược)**: Dùng cho các mục tiêu `REACH`, `TRAFFIC`, `VIDEO_VIEW`, `APP_PROMOTION`, `LEAD_GENERATION`, `WEB_CONVERSIONS`, `PRODUCT_SALES` hoặc `RF_REACH`. Trong quảng cáo Tìm kiếm khách hàng tiềm năng, cần chọn vị trí tối ưu hóa là Trang web (`Website`).
>   - **Nhãn dán mã quà tặng (`STICKER` loại quà tặng)**: Dùng để khuyến khích khách hàng mới và tri ân khách hàng cũ bằng mã đổi quà tặng hoặc mã giảm giá.
>   - **Cử chỉ tương tác (`GESTURE`)**: Tạo trải nghiệm chạm (`TAP`), vuốt thẳng (`STRAIGHT_SLIDE`) hoặc vuốt cong (`CURVED_SLIDE`) trên màn hình video kèm hiệu ứng âm thanh tương tác.
>   - **Hiệu ứng Superlike (`SUPER_LIKE`)**: Thu hút người xem bằng hiệu ứng hình ảnh trái tim hoặc biểu tượng tùy chỉnh nổi bồng bềnh bất ngờ khi người xem bấm thích (like) hoặc chạm đúp vào video quảng cáo.

### Tiêu đề HTTP (Header)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Có | Mã truy cập đã được ủy quyền. Xem [Xác thực](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| `Content-Type` | string | Có | Định dạng nội dung yêu cầu. Giá trị cho phép: `application/json`. |

### Tham số (POST: JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | Có | ID của tài khoản nhà quảng cáo TikTok. |
| `creative_portfolio_type` | string | Không | Loại tiện ích sáng tạo tương tác muốn tạo.<br><br>**Enum**:<br>• `CTA`: Văn bản nút kêu gọi hành động (mặc định).<br>• `CARD`: Thẻ hiển thị hình ảnh (Display Card).<br>• `HOTEL_CARD`: Thẻ khách sạn (App Travel Catalog Ads).<br>• `FLIGHT_CARD`: Thẻ chuyến bay (App Travel Catalog Ads).<br>• `DESTINATION_CARD`: Thẻ điểm đến du lịch (App Travel Catalog Ads).<br>• `WEB_INFO_CARD`: Thẻ thông tin trang web.<br>• `DOWNLOAD_CARD`: Thẻ tải ứng dụng.<br>• `INVENTORY_CARD`: Thẻ hàng tồn kho/xe cộ.<br>• `PRODUCT_CARD`: Thẻ sản phẩm.<br>• `PRODUCT_TILE`: Khung ô sản phẩm.<br>• `STICKER`: Nhãn dán đếm ngược hoặc mã quà tặng.<br>• `PREMIUM_BADGE`: Huy hiệu pop-out nổi bật.<br>• `GESTURE`: Cử chỉ chạm hoặc vuốt tương tác.<br>• `SUPER_LIKE`: Hiệu ứng thả tim đặc biệt Superlike. |
| `portfolio_content` | object[] | Điều kiện | Danh sách cấu hình nội dung cho tiện ích loại `CTA`. |
| ↳ `asset_content` | string | Có | Nội dung văn bản hiển thị trên nút kêu gọi hành động (ví dụ: `"Tìm hiểu thêm"` hoặc mã enum tương ứng). |
| ↳ `asset_ids` | string[] | Có | Danh sách ID tài sản liên kết với CTA (ví dụ: `["201781", "201535"]`). |
| `card_type` | string | Điều kiện | Loại thẻ khi `creative_portfolio_type` là `CARD`. Enum: `IMAGE_CARD` (Thẻ hình ảnh hiển thị). |
| `primary_text` | string | Điều kiện | Tiêu đề chính trên thẻ du lịch (`HOTEL_CARD`, `FLIGHT_CARD`, `DESTINATION_CARD`). Giá trị: `NONE`, `DEALS`, `CUSTOM_LABEL`. |
| `secondary_text` | string | Điều kiện | Tiêu đề phụ trên thẻ du lịch. Giá trị: `NONE`, `RATING`, `CUSTOM_LABEL`. |
| `card_show_price` | boolean | Điều kiện | Có hiển thị giá tiền của sản phẩm danh mục trên thẻ hay không (`PRODUCT_CARD`, `HOTEL_CARD`, `FLIGHT_CARD`). |
| `image_optimization_enabled` | boolean | Không | Bật tính năng AI tự động chuyển đổi ảnh không vuông thành ảnh vuông cho thẻ du lịch. |
| `display_price_enabled` | boolean | Không | Bật hiển thị thông tin giá tiền cho thẻ điểm đến (`DESTINATION_CARD`). |
| `gesture_type` | string | Điều kiện | Loại cử chỉ tương tác khi `creative_portfolio_type` là `GESTURE`.<br><br>**Enum**:<br>• `TAP`: Cử chỉ chạm.<br>• `STRAIGHT_SLIDE`: Cử chỉ vuốt thẳng.<br>• `CURVED_SLIDE`: Cử chỉ vuốt cong. |
| `image_id` | string | Điều kiện | ID hình ảnh sử dụng trên thẻ (`CARD`, `WEB_INFO_CARD`, `INVENTORY_CARD`) hoặc biểu tượng Superlike. |
| `pop_up_window_image_id` | string | Điều kiện | ID hình ảnh thẻ bật lên sau khi người dùng hoàn thành cử chỉ tương tác hoặc cửa sổ pop-up của Superlike. |
| `title` | string | Điều kiện | Tiêu đề cho thẻ thông tin trang web (`WEB_INFO_CARD`) hoặc nhãn dán (`STICKER`). |
| `selling_points` | string[] | Điều kiện | Danh sách các điểm nổi bật bán hàng trên thẻ Web Info Card (tối đa 3 điểm bán hàng). |
| `call_to_action_text` | string | Điều kiện | Văn bản kêu gọi hành động hiển thị trên thẻ hoặc cử chỉ. |
| `badge_show_time` | integer | Điều kiện | Thời điểm xuất hiện huy hiệu Pop-out Showcase tính bằng mili giây kể từ khi video bắt đầu phát. |
| `badge_position` | object | Điều kiện | Tọa độ điểm đặt của biểu tượng cử chỉ hoặc huy hiệu Pop-out Showcase. |
| ↳ `position_x` | float | Có | Tọa độ X tương đối (từ 0.0 đến 1.0) so với góc trên bên trái màn hình. |
| ↳ `position_y` | float | Có | Tọa độ Y tương đối (từ 0.0 đến 1.0) so với góc trên bên trái màn hình. |
| `angle` | number | Điều kiện | Góc xoay của biểu tượng vuốt cử chỉ hoặc huy hiệu Pop-out Showcase (từ 0 đến 360 độ; khuyến nghị 30-150 hoặc 210-330 cho vuốt cử chỉ). |
| `badge_image_info` | object | Điều kiện | Cấu hình tệp hình ảnh huy hiệu Pop-out Showcase. |
| ↳ `image_id` | string | Có | ID hình ảnh huy hiệu (yêu cầu: kích thước chính xác 448 x 448 pixels, định dạng JPG/JPEG/PNG, dung lượng không quá 1 MB). |
| `slide_length` | number | Điều kiện | Độ dài đường vuốt thẳng khi `gesture_type` là `STRAIGHT_SLIDE`. |
| `slide_dimension` | object | Điều kiện | Kích thước đường vuốt cong khi `gesture_type` là `CURVED_SLIDE`. |
| ↳ `dimension_width` | number | Có | Chiều rộng đường vuốt cong. |
| ↳ `dimension_height` | number | Có | Chiều cao đường vuốt cong. |
| `interactive_music_id` | string | Điều kiện | URL tệp âm thanh nền cho cử chỉ tương tác (yêu cầu định dạng MP3, dung lượng tệp dưới 1 MB, thời lượng khuyến nghị 6 giây). Tải lên qua [/file/music/upload/](52-music.md#doc-1740052650395650). Khuyến nghị dùng âm thanh trùng với nhạc nền video. |
| `layouts` | string[] | Điều kiện | Loại bố cục của thẻ tải ứng dụng (`DOWNLOAD_CARD`).<br><br>**Enum**:<br>• `TYPE_1`: Hiển thị mô tả ứng dụng.<br>• `TYPE_2`: Không hiển thị mô tả ứng dụng.<br>*(Có thể truyền cả `["TYPE_1", "TYPE_2"]` để tạo đồng thời hai mẫu thẻ tải).* |
| `description` | string | Điều kiện | Mô tả ứng dụng trên Download Card (bắt buộc khi `layouts` có `TYPE_1`) hoặc văn bản mô tả trên thẻ xe cộ `INVENTORY_CARD` (giới hạn tối đa 40 ký tự). |
| `tags` | string[] | Điều kiện | Các nhãn thông tin hiển thị trên Download Card.<br><br>**Enum**:<br>• `CATEGORIES`: Danh mục ứng dụng.<br>• `FILESIZE`: Dung lượng tệp ứng dụng.<br>• `RATING`: Đánh giá sao của ứng dụng.<br>• `RANKING`: Thứ hạng ứng dụng trên bảng xếp hạng.<br>• `COMMENT_VOLUME`: Số lượng nhận xét đánh giá.<br>*(Lưu ý độ ưu tiên hiển thị: `CATEGORIES` > `FILESIZE` > `RATING` > `RANKING` > `COMMENT_VOLUME`).* |
| `category_label` | string | Điều kiện | Tên danh mục ứng dụng (bắt buộc khi `tags` chứa `CATEGORIES`). Xem [Danh mục quản lý sáng tạo](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| `app_id` | string | Điều kiện | ID của ứng dụng cần quảng bá trên Download Card (lấy từ Events Manager). |
| `profile_image` | string | Điều kiện | URL hình ảnh đại diện/biểu tượng ứng dụng trên Download Card. |
| `call_to_action` | string | Điều kiện | Văn bản hiển thị trên nút hành động của thẻ tải ứng dụng. |
| `mobile_app_id` | string | Điều kiện | ID ứng dụng di động liên kết cho thẻ thông tin trang web (`WEB_INFO_CARD`). |
| `country_code` | string[] | Điều kiện | Danh sách mã quốc gia áp dụng hiển thị thẻ tải ứng dụng. |
| `sticker_param` | object | Điều kiện | Cấu hình tham số chi tiết cho nhãn dán tương tác (`STICKER`). |
| ↳ `sticker_type` | string | Có | Loại nhãn dán.<br><br>**Enum**:<br>• `COUNTDOWN`: Nhãn dán đếm ngược không nhắc nhở.<br>• `REMINDER_COUNTDOWN`: Nhãn dán đếm ngược có tính năng nhắc nhở cho sự kiện thông thường.<br>• `LIVE_REMINDER_COUNTDOWN`: Nhãn dán đếm ngược có tính năng nhắc nhở cho sự kiện livestream.<br>• `GIFTCODE`: Nhãn dán mã quà tặng/mã giảm giá nhằm thu hút khách hàng mới và kích thích mua hàng. |
| ↳ `title` | string | Có | Tiêu đề hiển thị trên nhãn dán (đối với Countdown Sticker tối đa 54 byte UTF-8 và không hỗ trợ dấu `#`; đối với Gift Code Sticker tối đa 20 byte). |
| ↳ `giftcode` | string | Điều kiện | Mã quà tặng hiển thị (bắt buộc khi `sticker_type` là `GIFTCODE`, tối đa 10 byte). |
| ↳ `cutoff_time` | string | Điều kiện | Thời điểm kết thúc đếm ngược hoặc thời điểm bắt đầu livestream, định dạng `"YYYY-MM-DD HH:MM:SS"` theo múi giờ UTC+0. |
| ↳ `color` | string | Có | Màu sắc nền của nhãn dán.<br>• Countdown Sticker: `ORANGE`, `BLACK`, `RED`, `BLUE`.<br>• Gift Code Sticker: `BLACK`, `BLUE`. |
| ↳ `display_angle` | integer | Có | Góc nghiêng hiển thị nhãn dán (từ -180 đến +180 độ, ví dụ `+90` xoay thuận chiều kim đồng hồ 90 độ). |
| ↳ `predefined_placement` | string | Điều kiện | Vị trí đặt sẵn của nhãn dán trên khung hình video. Nếu không truyền trường này, bạn phải truyền cả 3 trường `position_x`, `position_y` và `size`. Chi tiết xem bảng vị trí đặt sẵn bên dưới. |
| ↳ `position_x` | integer | Điều kiện | Tọa độ điểm đặt X (tính theo pixel) so với góc trên bên trái màn hình. |
| ↳ `position_y` | integer | Điều kiện | Tọa độ điểm đặt Y (tính theo pixel) so với góc trên bên trái màn hình. |
| ↳ `size` | string | Điều kiện | Tỷ lệ kích thước nhãn dán đếm ngược. Enum: `0.6` (60%), `0.7` (70%), `0.8` (80%), `0.9` (90%), `1` (100%), `1.1` (110%). |
| ↳ `opacity` | string | Điều kiện | Độ mờ đục của nhãn dán đếm ngược (`0.7`, `0.8`, `0.9`, `1`). Giá trị càng thấp nhãn dán càng trong suốt. |
| ↳ `reminder_time` | string | Điều kiện | Thời điểm gửi thông báo nhắc nhở đếm ngược:<br>• Sự kiện phi livestream (`REMINDER_COUNTDOWN`): `ONE_MINUTE_EARLIER`, `ONE_HOUR_EARLIER`, `ONE_DAY_EARLIER`.<br>• Sự kiện livestream (`LIVE_REMINDER_COUNTDOWN`): `ONE_MINUTE_AFTER`, `FIVE_MINUTES_AFTER`, `TEN_MINUTES_AFTER`. |
| ↳ `landing_page_url` | string | Điều kiện | URL trang đích được chuyển hướng tới khi người dùng nhấp vào thông báo nhắc nhở sau khi đếm ngược kết thúc. |
| ↳ `live_tiktok_user_id` | string | Điều kiện | ID người dùng TikTok của người chủ trì livestream (dùng cho `LIVE_REMINDER_COUNTDOWN`). |
| `product_source` | string | Điều kiện | Nguồn sản phẩm (`CATALOG`, `STORE`, `SHOWCASE`). |
| `identity_id` | string | Điều kiện | ID danh tính liên kết. |
| `identity_type` | string | Điều kiện | Loại danh tính (`AUTH_CODE`, `TT_USER`, `BC_AUTH_TT`). |
| `identity_authorized_bc_id` | string | Điều kiện | ID Business Center liên kết danh tính. |
| `catalog_id` | string | Điều kiện | ID danh mục sản phẩm. |
| `catalog_authorized_bc_id` | string | Điều kiện | ID Business Center được ủy quyền danh mục sản phẩm. |
| `store_id` | string | Điều kiện | ID cửa hàng TikTok Shop. |
| `store_authorized_bc_id` | string | Điều kiện | ID Business Center được ủy quyền cửa hàng. |
| `product_specific_type` | string | Điều kiện | Cách thức lựa chọn sản phẩm cho thẻ sản phẩm: `ALL` (tất cả sản phẩm), `PRODUCT_SET` (theo bộ sản phẩm), `CUSTOMIZED` (tùy chỉnh sản phẩm cụ thể). |
| `product_set_id` | string | Điều kiện | ID của bộ sản phẩm (bắt buộc khi `product_specific_type` là `PRODUCT_SET`). |
| `item_group_ids` | string[] | Điều kiện | Danh sách ID nhóm mặt hàng sản phẩm (SPU ID). |
| `sku_ids` | string[] | Điều kiện | Danh sách ID SKU sản phẩm cụ thể. |
| `dynamic_format` | string | Điều kiện | Định dạng động cho thẻ sản phẩm. |
| `vertical_video_strategy` | string | Điều kiện | Chiến lược video dọc cho thẻ sản phẩm. |
| `ad_text` | string | Không | Đoạn văn bản quảng cáo kèm theo thẻ sản phẩm. |
| `card_tags` | string[] | Không | Danh sách các nhãn đính kèm trên thẻ sản phẩm. |
| `card_image_index` | integer | Không | Chỉ số thứ tự của hình ảnh hiển thị trên thẻ sản phẩm. |
| `showcase_products` | object[] | Điều kiện | Danh sách sản phẩm trưng bày cho khung ô sản phẩm (`PRODUCT_TILE`). Tối thiểu 4 sản phẩm đã được kiểm duyệt duyệt thành công. |
| ↳ `item_group_id` | string | Có | ID nhóm sản phẩm (SPU ID). |
| ↳ `store_id` | string | Không | ID cửa hàng TikTok Shop chứa sản phẩm. |
| ↳ `catalog_id` | string | Không | ID danh mục sản phẩm chứa sản phẩm. |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Giá trị `0` là thành công. Xem [Phụ lục mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Mã log định danh duy nhất của yêu cầu API. |
| `data` | object | Dữ liệu trả về. |
| ↳ `creative_portfolio_id` | string | ID duy nhất của tiện ích sáng tạo tương tác vừa được tạo. |

### Bảng vị trí đặt sẵn (`Predefined Placements`)

Bảng dưới đây liệt kê các giá trị enum của trường `predefined_placement` và vị trí hiển thị tương ứng trên màn hình video:

#### Vị trí đặt sẵn cho Nhãn dán đếm ngược (`Countdown Sticker`)

| Giá trị enum | Vị trí hiển thị mẫu |
|---|---|
| `196x148x0.8` | Góc trên bên phải (Top right, kích thước 80%) |
| `57x148x0.8` | Góc trên bên trái (Top left, kích thước 80%) |
| `196x564x0.8` | Góc dưới bên phải (Bottom right, kích thước 80%) |
| `57x564x0.8` | Góc dưới bên trái (Bottom left, kích thước 80%) |
| `129x370x0.8` | Chính giữa màn hình (Center, kích thước 80%) |
| `55x143x0.9` | Tọa độ X=55, Y=143, tỷ lệ 90% |
| `157x141x0.9` | Tọa độ X=157, Y=141, tỷ lệ 90% |
| `110x236x0.9` | Tọa độ X=110, Y=236, tỷ lệ 90% |
| `112x327x0.9` | Tọa độ X=112, Y=327, tỷ lệ 90% |
| `105x533x0.9` | Tọa độ X=105, Y=533, tỷ lệ 90% |
| `53x533x0.9` | Tọa độ X=53, Y=533, tỷ lệ 90% |
| `143x533x0.9` | Tọa độ X=143, Y=533, tỷ lệ 90% |

#### Vị trí đặt sẵn cho Nhãn dán mã quà tặng (`Gift Code Sticker`)

| Giá trị enum | Vị trí hiển thị mẫu |
|---|---|
| `141x176` | Góc trên bên phải (Top right) |
| `86x176` | Góc trên bên trái (Top left) |
| `141x678` | Góc dưới bên phải (Bottom right) |
| `86x678` | Góc dưới bên trái (Bottom left) |
| `112x432` | Chính giữa màn hình (Center) |
| `86x179` | Tọa độ X=86, Y=179 |
| `113x179` | Tọa độ X=113, Y=179 |
| `113x308` | Tọa độ X=113, Y=308 |
| `113x462` | Tọa độ X=113, Y=462 |
| `113x676` | Tọa độ X=113, Y=676 |
| `88x676` | Tọa độ X=88, Y=676 |
| `138x676` | Tọa độ X=138, Y=676 |

### Ví dụ yêu cầu

#### cURL: Tạo nhãn dán đếm ngược (Countdown Sticker)
```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/creative/portfolio/create/" \
  -H "Access-Token: ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "advertiser_id": "6789012345678901234",
    "creative_portfolio_type": "STICKER",
    "sticker_param": {
      "sticker_type": "COUNTDOWN",
      "title": "Ưu đãi siêu hội mua sắm",
      "cutoff_time": "2024-11-11 23:59:59",
      "color": "ORANGE",
      "display_angle": 0,
      "predefined_placement": "196x148x0.8",
      "opacity": "1.00"
    }
  }'
```

#### cURL: Tạo thẻ hiển thị (Display Card)
```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/creative/portfolio/create/" \
  -H "Access-Token: ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "advertiser_id": "6789012345678901234",
    "creative_portfolio_type": "CARD",
    "card_type": "IMAGE_CARD",
    "image_id": "image_portfolio_12345",
    "primary_text": "Giảm ngay 50% hôm nay",
    "secondary_text": "Áp dụng cho mọi đơn hàng thời trang",
    "call_to_action_text": "Mua ngay"
  }'
```

#### cURL: Tạo khung ô sản phẩm (Product Tiles) cho Video Shopping Ads
```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/creative/portfolio/create/" \
  -H "Access-Token: ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "advertiser_id": "6789012345678901234",
    "creative_portfolio_type": "PRODUCT_TILE",
    "product_source": "CATALOG",
    "catalog_id": "7123456789012345678",
    "catalog_authorized_bc_id": "6789012345678901234",
    "showcase_products": [
      {"item_group_id": "SPU_001", "catalog_id": "7123456789012345678"},
      {"item_group_id": "SPU_002", "catalog_id": "7123456789012345678"},
      {"item_group_id": "SPU_003", "catalog_id": "7123456789012345678"},
      {"item_group_id": "SPU_004", "catalog_id": "7123456789012345678"}
    ]
  }'
```

#### Phản hồi mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202410231500000901111222333444555",
  "data": {
    "creative_portfolio_id": "7123456789012345688"
  }
}
```
---

## Lấy thông tin danh mục creative theo ID (`Get a portfolio by ID`)
<a id="doc-1739092113671170"></a>
<!-- doc_id: 1739092113671170 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/creative/portfolio/get/`

**Mục đích**: Lấy thông tin cấu hình chi tiết của một tiện ích sáng tạo tương tác cụ thể bằng mã `creative_portfolio_id`. Bạn có thể tra cứu thông tin của bất kỳ tiện ích nào đã tạo thông qua endpoint [/creative/portfolio/create/](36-creative-portfolios.md#doc-1739091950439426).

### Tiêu đề HTTP (Header)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Có | Mã truy cập đã được ủy quyền. Xem chi tiết tại [Xác thực](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (GET: query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | Có | ID của tài khoản nhà quảng cáo. |
| `creative_portfolio_id` | string | Có | ID của tiện ích sáng tạo cần tra cứu (nhận được từ phản hồi tạo tiện ích). |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Giá trị `0` là thành công. Xem [Phụ lục mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Mã log định danh duy nhất của yêu cầu API. |
| `data` | object | Dữ liệu chi tiết của tiện ích sáng tạo tương tác. |
| ↳ `creative_portfolio_id` | string | ID duy nhất của tiện ích sáng tạo tương tác. |
| ↳ `creative_portfolio_type` | string | Loại tiện ích sáng tạo (`CTA`, `CARD`, `HOTEL_CARD`, `FLIGHT_CARD`, `DESTINATION_CARD`, `WEB_INFO_CARD`, `DOWNLOAD_CARD`, `INVENTORY_CARD`, `PRODUCT_CARD`, `PRODUCT_TILE`, `STICKER`, `PREMIUM_BADGE`, `GESTURE`, `SUPER_LIKE`). |
| ↳ `portfolio_content` | object[] | Danh sách cấu hình nội dung (trả về khi tiện ích là loại `CTA`). |
| ↳↳ `asset_content` | string | Nội dung văn bản nút kêu gọi hành động (ví dụ: `"Tìm hiểu thêm"`). |
| ↳↳ `asset_ids` | string[] | Danh sách ID tài sản liên kết với CTA. |
| ↳ `card_type` | string | Loại thẻ hiển thị (`IMAGE_CARD`: Thẻ hình ảnh hiển thị). |
| ↳ `primary_text` | string | *(Trả về cho thẻ du lịch HOTEL_CARD, FLIGHT_CARD, DESTINATION_CARD)*. Tiêu đề chính (`NONE`, `DEALS`, `CUSTOM_LABEL`). |
| ↳ `secondary_text` | string | *(Trả về cho thẻ du lịch)*. Tiêu đề phụ (`NONE`, `RATING`, `CUSTOM_LABEL`). |
| ↳ `card_show_price` | boolean | *(Trả về cho PRODUCT_CARD, HOTEL_CARD, FLIGHT_CARD)*. Cho biết có hiển thị giá sản phẩm trên thẻ hay không (`true`, `false`). |
| ↳ `image_optimization_enabled` | boolean | Trạng thái bật tối ưu hóa hình ảnh AI cho thẻ du lịch (`true`, `false`). |
| ↳ `display_price_enabled` | boolean | Trạng thái hiển thị thông tin giá cho thẻ điểm đến (`DESTINATION_CARD`). |
| ↳ `gesture_type` | string | *(Trả về khi loại tiện ích là GESTURE)*. Loại cử chỉ tương tác (`TAP`: Chạm, `STRAIGHT_SLIDE`: Vuốt thẳng, `CURVED_SLIDE`: Vuốt cong). |
| ↳ `image_id` | string | ID hình ảnh đính kèm trên thẻ (`CARD`, `WEB_INFO_CARD`, `INVENTORY_CARD`) hoặc biểu tượng Superlike. |
| ↳ `pop_up_window_image_id` | string | ID hình ảnh thẻ bật lên sau khi hoàn thành cử chỉ tương tác hoặc cửa sổ bật lên sau khi hiệu ứng Superlike kết thúc. |
| ↳ `title` | string | Tiêu đề hiển thị trên thẻ thông tin trang web (`WEB_INFO_CARD`). |
| ↳ `selling_points` | string[] | Danh sách các điểm bán hàng/tính năng nổi bật trên thẻ Web Info Card. |
| ↳ `content_url` | string | Đường dẫn URL nội dung trang web đích liên kết trên thẻ. |
| ↳ `thumbnail_id` | string | ID hình ảnh thu nhỏ đại diện cho tiện ích. |
| ↳ `call_to_action_text` | string | Văn bản kêu gọi hành động hiển thị trên thẻ hoặc tiện ích cử chỉ. |
| ↳ `badge_show_time` | integer | Thời điểm xuất hiện huy hiệu Pop-out Showcase tính theo mili giây. |
| ↳ `badge_position` | object | Tọa độ vị trí hiển thị huy hiệu hoặc cử chỉ trên màn hình. |
| ↳↳ `position_x` | float | Tọa độ X tương đối (từ 0.0 đến 1.0). |
| ↳↳ `position_y` | float | Tọa độ Y tương đối (từ 0.0 đến 1.0). |
| ↳ `angle` | number | Góc xoay hiển thị của biểu tượng cử chỉ hoặc huy hiệu. |
| ↳ `badge_image_info` | object | Cấu hình tệp hình ảnh huy hiệu Pop-out Showcase. |
| ↳↳ `image_id` | string | ID hình ảnh huy hiệu kích thước 448x448 pixels. |
| ↳ `slide_length` | number | Chiều dài cử chỉ vuốt thẳng (`STRAIGHT_SLIDE`). |
| ↳ `slide_dimension` | object | Kích thước cử chỉ vuốt cong (`CURVED_SLIDE`). |
| ↳↳ `dimension_width` | number | Chiều rộng cử chỉ vuốt cong. |
| ↳↳ `dimension_height` | number | Chiều cao cử chỉ vuốt cong. |
| ↳ `interactive_music_id` | string | URL tệp âm thanh nền cho cử chỉ tương tác. |
| ↳ `layouts` | string[] | Danh sách loại bố cục của thẻ tải ứng dụng (`TYPE_1`, `TYPE_2`). |
| ↳ `description` | string | Mô tả ứng dụng trên Download Card hoặc văn bản mô tả trên thẻ xe cộ Inventory Card. |
| ↳ `tags` | string[] | Danh sách nhãn hiển thị trên Download Card (`CATEGORIES`, `FILESIZE`, `RATING`, `RANKING`, `COMMENT_VOLUME`). |
| ↳ `category_label` | string | Tên danh mục ứng dụng trên Download Card. |
| ↳ `app_id` | string | ID ứng dụng di động trong Events Manager được quảng bá. |
| ↳ `profile_image` | string | URL hình ảnh biểu tượng của ứng dụng. |
| ↳ `call_to_action` | string | Văn bản nút kêu gọi hành động trên Download Card hoặc Product Card. |
| ↳ `mobile_app_id` | string | ID ứng dụng di động cho Web Info Card. |
| ↳ `country_code` | string[] | Danh sách mã quốc gia áp dụng thẻ tải ứng dụng. |
| ↳ `sticker_param` | object | Cấu hình tham số chi tiết của nhãn dán tương tác (Sticker). |
| ↳↳ `sticker_type` | string | Loại nhãn dán (`COUNTDOWN`, `REMINDER_COUNTDOWN`, `LIVE_REMINDER_COUNTDOWN`, `GIFTCODE`). |
| ↳↳ `title` | string | Tiêu đề của nhãn dán. |
| ↳↳ `giftcode` | string | Mã quà tặng (áp dụng cho `GIFTCODE`). |
| ↳↳ `cutoff_time` | string | Thời gian kết thúc đếm ngược (UTC+0). |
| ↳↳ `color` | string | Màu nền nhãn dán (`ORANGE`, `BLACK`, `RED`, `BLUE`). |
| ↳↳ `display_angle` | integer | Góc nghiêng hiển thị của nhãn dán. |
| ↳↳ `predefined_placement` | string | Mã vị trí đặt sẵn của nhãn dán. |
| ↳↳ `position_x` | integer | Tọa độ X điểm đặt nhãn dán. |
| ↳↳ `position_y` | integer | Tọa độ Y điểm đặt nhãn dán. |
| ↳↳ `size` | string | Tỷ lệ kích thước nhãn dán (`0.6` đến `1.1`). |
| ↳↳ `opacity` | string | Độ mờ đục nhãn dán (`0.7` đến `1`). |
| ↳↳ `reminder_time` | string | Thời điểm gửi thông báo nhắc nhở. |
| ↳↳ `landing_page_url` | string | URL trang đích liên kết khi nhấp vào thông báo nhắc nhở. |
| ↳↳ `live_tiktok_user_id` | string | ID người dùng chủ phòng livestream. |
| ↳ `product_source` | string | Nguồn sản phẩm (`CATALOG`, `STORE`, `SHOWCASE`). |
| ↳ `catalog_id` | string | ID danh mục sản phẩm liên kết. |
| ↳ `store_id` | string | ID cửa hàng TikTok Shop liên kết. |
| ↳ `showcase_products` | object[] | Danh sách sản phẩm trưng bày cho khung ô sản phẩm (`PRODUCT_TILE`). |
| ↳↳ `item_group_id` | string | ID nhóm sản phẩm (SPU ID). |
| ↳↳ `store_id` | string | ID cửa hàng chứa sản phẩm. |
| ↳↳ `catalog_id` | string | ID danh mục chứa sản phẩm. |

### Ví dụ

#### cURL
```bash
curl -X GET "https://business-api.tiktok.com/open_api/v1.3/creative/portfolio/get/?advertiser_id=6789012345678901234&creative_portfolio_id=7123456789012345688" \
  -H "Access-Token: ACCESS_TOKEN"
```

#### Python
```python
import requests

ACCESS_TOKEN = "your_access_token"
ADVERTISER_ID = "6789012345678901234"
PORTFOLIO_ID = "7123456789012345688"

url = "https://business-api.tiktok.com/open_api/v1.3/creative/portfolio/get/"
headers = {"Access-Token": ACCESS_TOKEN}
params = {
    "advertiser_id": ADVERTISER_ID,
    "creative_portfolio_id": PORTFOLIO_ID
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

#### Phản hồi mẫu: Tiện ích nhãn dán đếm ngược (Countdown Sticker)
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20241023150000090444555666777888",
  "data": {
    "creative_portfolio_id": "7123456789012345688",
    "creative_portfolio_type": "STICKER",
    "sticker_param": {
      "color": "ORANGE",
      "cutoff_time": "2024-11-11 23:59:59",
      "display_angle": 0,
      "opacity": "1",
      "position_x": 100,
      "position_y": 200,
      "predefined_placement": "196x148x0.8",
      "size": "0.8",
      "sticker_type": "COUNTDOWN",
      "title": "Ưu đãi siêu hội mua sắm"
    }
  }
}
```

#### Phản hồi mẫu: Tiện ích nút kêu gọi hành động (CTA)
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20241023150000090444555666777889",
  "data": {
    "creative_portfolio_id": "7123456789012345689",
    "creative_portfolio_type": "CTA",
    "portfolio_content": [
      {
        "asset_content": "Tìm hiểu thêm",
        "asset_ids": [
          "201781",
          "201535"
        ]
      },
      {
        "asset_content": "Tải ngay",
        "asset_ids": [
          "201902",
          "201404"
        ]
      }
    ]
  }
}
```
---

## Lấy danh sách danh mục creative của tài khoản (`Get portfolios within an ad account`)
<a id="doc-1766324010279938"></a>
<!-- doc_id: 1766324010279938 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/creative/portfolio/list/`

**Mục đích**: Lấy danh sách các tiện ích sáng tạo tương tác đã được tạo trong một tài khoản quảng cáo. Bạn có thể lọc danh sách kết quả theo loại tiện ích hoặc danh sách các mã ID cụ thể.

> [!NOTE]
> - Endpoint này hỗ trợ truy xuất hầu hết các loại tiện ích sáng tạo: Thẻ hiển thị (Display Card), Thẻ khách sạn (Hotel Card), Thẻ chuyến bay (Flight Card), Thẻ điểm đến (Destination Card), Thẻ thông tin trang web (Website Info Card), Thẻ tải ứng dụng (Download Card), Thẻ xe cộ (Inventory Card), Thẻ sản phẩm (Product Card), Khung ô sản phẩm (Product Tiles), Nhãn dán đếm ngược (Countdown Sticker), Nhãn dán mã quà tặng (Gift Code Sticker), Huy hiệu Pop-out Showcase, Cử chỉ tương tác (Gesture) và Hiệu ứng Superlike.
> - Tiện ích văn bản kêu gọi hành động (`CTA`) không hỗ trợ lọc qua endpoint này.
> - Bạn không thể sử dụng `creative_portfolio_types` để lọc Thẻ sản phẩm (`PRODUCT_CARD`) và Khung ô sản phẩm (`PRODUCT_TILE`); để lọc hai loại này, hãy chỉ định danh sách ID trong `creative_portfolio_ids`.

### Tiêu đề HTTP (Header)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Có | Mã truy cập đã được ủy quyền. Xem chi tiết tại [Xác thực](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (GET: query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | Có | ID của tài khoản nhà quảng cáo TikTok. |
| `filtering` | object | Không | Điều kiện lọc danh mục creative. Nếu không chỉ định, API trả về tất cả các loại tiện ích (ngoại trừ CTA). |
| ↳ `creative_portfolio_types` | string[] | Không | Danh sách các loại tiện ích sáng tạo cần lọc (`CARD`, `HOTEL_CARD`, `FLIGHT_CARD`, `DESTINATION_CARD`, `WEB_INFO_CARD`, `DOWNLOAD_CARD`, `INVENTORY_CARD`, `PRODUCT_CARD`, `PRODUCT_TILE`, `COUNTDOWN_STICKER`, `REMINDER_COUNTDOWN_STICKER`, `LIVE_REMINDER_COUNTDOWN_STICKER`, `GIFTCODE_STICKER`, `PREMIUM_BADGE`, `GESTURE`, `SUPER_LIKE`). |
| ↳ `creative_portfolio_ids` | string[] | Không | Danh sách ID tiện ích sáng tạo cụ thể cần lọc. Tối đa 100 ID. |
| `page` | integer | Không | Số trang dữ liệu hiện tại (giá trị ≥ 1). Mặc định: `1`. |
| `page_size` | integer | Không | Số lượng bản ghi mỗi trang (từ `1` đến `100`). Mặc định: `10`. |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Giá trị `0` là thành công. Xem [Phụ lục mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Mã log định danh duy nhất của yêu cầu API. |
| `data` | object | Dữ liệu trả về. |
| ↳ `creative_portfolios` | object[] | Danh sách các tiện ích sáng tạo tương tác. |
| ↳↳ `creative_portfolio_id` | string | ID duy nhất của tiện ích sáng tạo. |
| ↳↳ `creative_portfolio_type` | string | Loại tiện ích sáng tạo. |
| ↳↳ `creative_portfolio_preview_url` | string | Đường dẫn URL xem trước giao diện hiển thị của tiện ích tương tác trên ứng dụng TikTok. |
| ↳↳ `card_type` | string | Loại thẻ hiển thị (`IMAGE_CARD`, `SLIDE_CARD`). |
| ↳↳ `primary_text` | string | Tiêu đề chính của thẻ. |
| ↳↳ `secondary_text` | string | Tiêu đề phụ của thẻ. |
| ↳↳ `card_show_price` | boolean | Trạng thái hiển thị giá trên thẻ. |
| ↳↳ `image_optimization_enabled` | boolean | Bật tối ưu hóa hình ảnh cho thẻ du lịch. |
| ↳↳ `display_price_enabled` | boolean | Bật hiển thị giá cho thẻ điểm đến. |
| ↳↳ `gesture_type` | string | Loại cử chỉ tương tác (`TAP`, `STRAIGHT_SLIDE`, `CURVED_SLIDE`). |
| ↳↳ `image_id` | string | ID hình ảnh đính kèm trên tiện ích. |
| ↳↳ `pop_up_window_image_id` | string | ID hình ảnh cửa sổ pop-up của cử chỉ hoặc Superlike. |
| ↳↳ `title` | string | Tiêu đề hiển thị trên tiện ích. |
| ↳↳ `selling_points` | string[] | Danh sách điểm nổi bật bán hàng. |
| ↳↳ `content_url` | string | URL trang web đích liên kết. |
| ↳↳ `thumbnail_id` | string | ID hình ảnh thu nhỏ. |
| ↳↳ `call_to_action_text` | string | Văn bản nút kêu gọi hành động. |
| ↳↳ `badge_show_time` | integer | Thời điểm xuất hiện huy hiệu (mili giây). |
| ↳↳ `badge_position` | object | Tọa độ vị trí hiển thị huy hiệu hoặc cử chỉ. |
| ↳↳ `angle` | number | Góc xoay hiển thị của biểu tượng cử chỉ hoặc huy hiệu. |
| ↳↳ `badge_image_info` | object | Thông tin tệp hình ảnh huy hiệu. |
| ↳↳ `slide_length` | number | Chiều dài cử chỉ vuốt thẳng. |
| ↳↳ `slide_dimension` | object | Kích thước cử chỉ vuốt cong. |
| ↳↳ `interactive_music_id` | string | URL âm thanh nền cho cử chỉ. |
| ↳↳ `layouts` | string[] | Bố cục thẻ tải ứng dụng (`TYPE_1`, `TYPE_2`). |
| ↳↳ `description` | string | Mô tả ứng dụng hoặc xe cộ. |
| ↳↳ `tags` | string[] | Danh sách nhãn trên Download Card. |
| ↳↳ `category_label` | string | Nhãn danh mục ứng dụng. |
| ↳↳ `app_id` | string | ID ứng dụng được quảng bá. |
| ↳↳ `profile_image` | string | URL ảnh biểu tượng ứng dụng. |
| ↳↳ `call_to_action` | string | Văn bản kêu gọi hành động. |
| ↳↳ `mobile_app_id` | string | ID ứng dụng di động cho Web Info Card. |
| ↳↳ `country_code` | string[] | Danh sách mã quốc gia áp dụng. |
| ↳↳ `sticker_param` | object | Cấu hình tham số chi tiết của nhãn dán tương tác (loại, tiêu đề, mã quà tặng, thời gian, màu sắc, vị trí, kích thước, độ mờ). |
| ↳↳ `product_source` | string | Nguồn sản phẩm (`CATALOG`, `STORE`, `SHOWCASE`). |
| ↳↳ `catalog_id` | string | ID danh mục sản phẩm. |
| ↳↳ `store_id` | string | ID cửa hàng TikTok Shop. |
| ↳↳ `showcase_products` | object[] | Danh sách sản phẩm trưng bày cho khung ô sản phẩm. |
| ↳ `page_info` | object | Thông tin phân trang. |
| ↳↳ `page` | number | Trang hiện tại. |
| ↳↳ `page_size` | number | Số lượng bản ghi mỗi trang. |
| ↳↳ `total_number` | number | Tổng số lượng tiện ích sáng tạo. |
| ↳↳ `total_page` | number | Tổng số trang kết quả. |

### Ví dụ

#### cURL
```bash
curl -X GET "https://business-api.tiktok.com/open_api/v1.3/creative/portfolio/list/?advertiser_id=6789012345678901234&page=1&page_size=10" \
  -H "Access-Token: ACCESS_TOKEN"
```

#### Python
```python
import json
import requests

ACCESS_TOKEN = "your_access_token"
ADVERTISER_ID = "6789012345678901234"

url = "https://business-api.tiktok.com/open_api/v1.3/creative/portfolio/list/"
headers = {"Access-Token": ACCESS_TOKEN}
params = {
    "advertiser_id": ADVERTISER_ID,
    "page": 1,
    "page_size": 10,
    "filtering": json.dumps({"creative_portfolio_types": ["STICKER", "CARD"]})
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

#### Phản hồi mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20241023150000090222333444555666",
  "data": {
    "creative_portfolios": [
      {
        "call_to_action_text": "Mua ngay",
        "creative_portfolio_id": "7123456789012345688",
        "creative_portfolio_preview_url": "https://ads.tiktok.com/preview/portfolio/7123456789012345688",
        "creative_portfolio_type": "STICKER",
        "title": "Ưu đãi siêu hội mua sắm"
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

## Xóa danh mục creative (`Delete portfolios`)
<a id="doc-1834560049625089"></a>
<!-- doc_id: 1834560049625089 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/creative/portfolio/delete/`

**Mục đích**: Xóa hàng loạt các tiện ích sáng tạo tương tác bổ sung (interactive add-ons) khỏi tài khoản quảng cáo.

> [!NOTE]
> - Endpoint này **không hỗ trợ** xóa các tiện ích loại Thẻ sản phẩm (`PRODUCT_CARD`), Khung ô sản phẩm (`PRODUCT_TILE`) hoặc Kêu gọi hành động (`CTA`).
> - Nếu bất kỳ ID tiện ích nào trong danh sách không hợp lệ (không tồn tại hoặc đã bị xóa trước đó), toàn bộ yêu cầu xóa sẽ thất bại.

### Tiêu đề HTTP (Header)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Có | Mã truy cập đã được ủy quyền. Xem chi tiết tại [Xác thực](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| `Content-Type` | string | Có | Định dạng nội dung yêu cầu. Giá trị cho phép: `application/json`. |

### Tham số (POST: JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | Có | ID của tài khoản nhà quảng cáo. |
| `creative_portfolio_ids` | string[] | Có | Danh sách ID các tiện ích sáng tạo cần xóa (tối đa 100 ID). Tra cứu danh sách ID qua [/creative/portfolio/list/](36-creative-portfolios.md#doc-1766324010279938). |

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
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/creative/portfolio/delete/" \
  -H "Access-Token: ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "advertiser_id": "6789012345678901234",
    "creative_portfolio_ids": [
      "7123456789012345688",
      "7123456789012345689"
    ]
  }'
```

#### Phản hồi mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20241023150000090333444555666777",
  "data": {}
}
```
