# Quảng cáo (Ads) — phần 2/2

Tài liệu này hướng dẫn chi tiết các endpoint cập nhật quảng cáo trong TikTok Business API v1.3, bao gồm:
* Cập nhật nội dung sáng tạo quảng cáo (`/ad/update/`)
* Cập nhật trạng thái hoạt động của quảng cáo (`/ad/status/update/`)

---

## Cập nhật quảng cáo (`Update ads`)
<a id="doc-1739953405142018"></a>
<!-- doc_id: 1739953405142018 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/ad/update/`

**Mục đích**: Sử dụng endpoint này để chỉnh sửa nội dung sáng tạo (creatives) của các quảng cáo thông thường, chẳng hạn như nút kêu gọi hành động (call-to-action), tên quảng cáo, văn bản quảng cáo, hình ảnh và video.

> [!IMPORTANT]
> Việc tạo quảng cáo không phải Spark Ads sử dụng Danh tính tùy chỉnh (Custom Identity) trong các nhóm quảng cáo phân phối tới Vị trí tự động (Automatic Placement) hoặc Chọn vị trí (Select Placement) có bao gồm TikTok hiện không còn được hỗ trợ cho các tài khoản quảng cáo hiện tại. Tất cả các tài khoản quảng cáo mới được tạo từ ngày 15 tháng 1 năm 2026 trở đi không thể tạo quảng cáo không phải Spark Ads bằng Custom Identity cho các vị trí này. Các quảng cáo hiện có không bị ảnh hưởng và vẫn có thể chỉnh sửa được. Các chiến dịch quảng cáo chỉ phân phối tới Pangle hoặc Global App Bundle không bị ảnh hưởng bởi việc ngừng hỗ trợ Custom Identity. Xem thêm chi tiết về [những thay đổi sắp tới đối với Danh tính tùy chỉnh (Custom Identity)](https://ads.tiktok.com/help/article/about-changes-coming-to-custom-identity) và [di chuyển sang Spark Ads](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1848048566169730).

> [!NOTE]
> Để cập nhật tài liệu sáng tạo cho quảng cáo Sáng tạo thông minh (Smart Creative ads), hãy sử dụng endpoint [/ad/aco/update/](60-smart-creative.md#doc-1739473077112833).
>
> Cập nhật từng phần (incremental updates / patch update) trong endpoint này chỉ được hỗ trợ cho các trường sau khi `patch_update` được đặt thành `true`:
> - `ad_name`
> - `identity_id`
> - `identity_type`
> - `identity_authorized_bc_id`
> - `video_id`
> - `image_ids`
> - `music_id`
> - `tiktok_item_id`
> - `ad_text`
> - `ad_texts`
>
> Đối với các trường khác, bạn chỉ có thể dùng chế độ cập nhật đầy đủ (full update) và truyền vào tất cả các tham số cần thiết để cập nhật quảng cáo. Nếu không, một số tham số có thể bị ghi đè thành giá trị null. Nếu bạn muốn hệ thống hỗ trợ cập nhật từng phần cho các trường khác, vui lòng liên hệ với đại diện TikTok của bạn.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền (access token). Xem chi tiết tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type | string | Bắt buộc | Định dạng nội dung yêu cầu. Giá trị hợp lệ: `application/json`. |

### Tham số (POST JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| advertiser_id | string | Bắt buộc | ID tài khoản quảng cáo (advertiser ID). |
| adgroup_id | string | Bắt buộc | ID nhóm quảng cáo (ad group ID). |
| patch_update | boolean | Không bắt buộc | Có sử dụng chế độ cập nhật từng phần (incremental update mode) hay không.<br>Các trường sau được hỗ trợ khi đặt trường này thành `true`: • `ad_name`<br>• `identity_id`<br>• `identity_type`<br>• `identity_authorized_bc_id`<br>• `video_id`<br>• `image_ids`<br>• `music_id`<br>• `tiktok_item_id`<br>• `ad_text`<br>• `ad_texts`.<br>Ví dụ: để cập nhật tên quảng cáo bằng chế độ cập nhật từng phần, bạn chỉ cần: cấu hình `patch_update` là `true`, đặt `ad_name` thành tên quảng cáo mới, và truyền các trường bắt buộc trong Header, `advertiser_id` và `ad_id`.<br>> [!IMPORTANT]<br>> Nếu bạn bật chế độ cập nhật từng phần bằng trường này, chúng tôi khuyến nghị bạn nên kiểm thử kỹ lưỡng để tránh gián đoạn luồng cập nhật quảng cáo hiện tại. |
| creatives | object[] | Bắt buộc | Danh sách nội dung sáng tạo quảng cáo. Kích thước tối đa: 20. |
| ↳ ad_id | string | Bắt buộc | ID quảng cáo cần cập nhật. |
| ↳ ad_name | string | Điều kiện | Bắt buộc khi `patch_update` không được đặt thành `true`.<br>Tên quảng cáo. Để hệ thống tự động tạo tên quảng cáo, hãy đặt trường này thành chuỗi rỗng `""`. Định dạng tên tự động tạo là ID quảng cáo (`ad_id`).<br>Giới hạn độ dài: tối đa 512 ký tự và không được chứa biểu tượng cảm xúc (emoji).<br>Lưu ý: Mỗi từ tiếng Trung hoặc tiếng Nhật tính là 2 ký tự, mỗi chữ cái tiếng Anh tính là 1 ký tự. |
| ↳ identity_id | string | Điều kiện | Bắt buộc khi `patch_update` không được đặt thành `true`.<br>ID danh tính (Identity ID). Nếu bạn không sử dụng Spark Ads, `identity_id` và `identity_type` (`CUSTOMIZED_USER`) có thể được dùng để quản lý thông tin quảng cáo tốt hơn. |
| ↳ identity_type | string | Điều kiện | Bắt buộc khi `patch_update` không được đặt thành `true` và bạn sử dụng Spark Ads.<br>Loại danh tính. Các giá trị enum: • `CUSTOMIZED_USER`: Danh tính tùy chỉnh.<br>• `AUTH_CODE`: Mã ủy quyền tài khoản TikTok.<br>• `TT_USER`: Tài khoản TikTok liên kết.<br>• `BC_AUTH_TT`: Tài khoản TikTok ủy quyền qua Business Center.<br>Xem chi tiết tại [Identities](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1738958351620097). |
| ↳ identity_authorized_bc_id | string | Điều kiện | Bắt buộc khi `identity_type` là `BC_AUTH_TT`.<br>ID của Business Center mà người dùng tài khoản TikTok liên kết tới. |
| ↳ product_specific_type | string | Không bắt buộc | Chỉ hợp lệ khi `shopping_ads_type` là `VIDEO` và `product_source` là `CATALOG`.<br>Chiều kích thước chọn sản phẩm cho Video Shopping Ads có nguồn danh mục (VSA for Catalog).<br>Các giá trị enum:<br>• `ALL`: Cho phép TikTok tự động chọn linh hoạt từ tất cả sản phẩm (không cần truyền `sku_ids`, `item_group_ids` và `product_set_id`).<br>• `PRODUCT_SET`: Chỉ định một bộ sản phẩm, TikTok sẽ tự động chọn sản phẩm từ bộ này (cần truyền `item_group_ids` hoặc `product_set_id`).<br>• `CUSTOMIZED_PRODUCTS`: Chỉ định số lượng sản phẩm tùy chỉnh (bắt buộc truyền `sku_ids`). |
| ↳ item_group_ids | string[] | Điều kiện | Nếu `product_specific_type` là `PRODUCT_SET`, bạn cần truyền `item_group_ids` hoặc `product_set_id`.<br>Danh sách ID SPU sản phẩm. Các sản phẩm phải thuộc cùng danh mục (`catalog_id`) chỉ định ở cấp nhóm quảng cáo. Kích thước tối đa: 20. |
| ↳ product_set_id | string | Điều kiện | Nếu `product_specific_type` là `PRODUCT_SET`, bạn cần truyền `item_group_ids` hoặc `product_set_id`.<br>ID bộ sản phẩm. Bộ sản phẩm phải bao gồm các sản phẩm thuộc cùng danh mục (`catalog_id`) chỉ định ở cấp nhóm quảng cáo. |
| ↳ sku_ids | string[] | Điều kiện | Bắt buộc khi `product_specific_type` là `CUSTOMIZED_PRODUCTS`.<br>Danh sách ID SKU sản phẩm thuộc cùng `catalog_id` ở cấp nhóm quảng cáo. Kích thước tối đa: 20.<br>Lưu ý: Không thể cập nhật thành mảng rỗng hoặc null. Chỉ hỗ trợ sản phẩm có sẵn (`AVAILABLE`) lấy từ [/catalog/product/get/](28-catalog-products-p2.md#doc-1740564136678402). Nếu là [VSA Carousel Ad](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1766217791987713) (`ad_format` là `CATALOG_CAROUSEL`), phải chỉ định ít nhất 2 sản phẩm. |
| ↳ ad_format | string | Điều kiện | Bắt buộc khi `patch_update` không được đặt thành `true`.<br>Định dạng quảng cáo. Các giá trị enum:<br>• `SINGLE_IMAGE`: Quảng cáo một hình ảnh.<br>• `SINGLE_VIDEO`: Quảng cáo một video.<br>• `LIVE_CONTENT`: Quảng cáo nội dung trực tiếp (Live Shopping Ads).<br>• `CAROUSEL_ADS`: Quảng cáo xoay vòng (không phải VSA).<br>• `CATALOG_CAROUSEL`: Quảng cáo xoay vòng danh mục sản phẩm (VSA Carousel Ads). |
| ↳ vertical_video_strategy | string | Không bắt buộc | Chiến lược video dạng dọc sử dụng cho kịch bản Bán sản phẩm (Product Sales).<br>Các giá trị enum:<br>• `UNSET`: Chưa thiết lập.<br>• `SINGLE_VIDEO`: Video đơn.<br>• `CATALOG_VIDEOS`: Video danh mục tạo từ mẫu video.<br>• `CATALOG_UPLOADED_VIDEOS`: Video danh mục từ video đã tải lên.<br>• `LIVE_STREAM`: Video phát trực tiếp. |
| ↳ dynamic_format | string | Không bắt buộc | Định dạng động. Enum: • `UNSET`: Chưa thiết lập.<br>• `DYNAMIC_CREATIVE`: Sáng tạo thông minh (ACO). |
| ↳ video_id | string | Điều kiện | ID video quảng cáo.<br>Bắt buộc khi `ad_format` là `SINGLE_VIDEO` hoặc `shopping_ads_type` là `LIVE` với `creative_type` là `SHORT_VIDEO_LIVE`.<br>Lưu ý: Nếu cập nhật ID video mới cho quảng cáo Carousel hoặc Spark Ads, quảng cáo sẽ được gửi lại để xét duyệt. |
| ↳ image_ids | string[] | Điều kiện | Danh sách ID hình ảnh.<br>Bắt buộc khi: `ad_format` là `SINGLE_IMAGE` (chỉ 1 ảnh), hoặc `CAROUSEL_ADS` (2 đến 35 ảnh), hoặc quảng cáo ô tô trong [Create Automotive Ads for Inventory](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1827752507854850) / [Automotive Ads for Models](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1829635758164994) (1 ảnh làm ảnh tóm tắt).<br>Xem thêm yêu cầu ảnh đơn tại [Create single image ads](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1777633230937090).<br>Lưu ý: Thay đổi ảnh sẽ đưa quảng cáo vào quy trình xét duyệt lại. |
| ↳ carousel_image_index | integer | Không bắt buộc | Áp dụng cho VSA Carousel Ads có cấu hình danh sách ảnh phụ (`additional_image_urls`) trong danh mục sản phẩm. Không hỗ trợ cho Automotive Carousel Ads.<br>Chỉ số xác định ảnh phụ được dùng trong quảng cáo xoay vòng. Khoảng giá trị: `[0, 9]`. Đại diện cho thứ tự ảnh trong mảng `additional_image_urls` của từng sản phẩm E-commerce catalog (truy xuất qua [/catalog/product/get/](28-catalog-products-p2.md#doc-1740564136678402)). |
| ↳ end_card_cta | string | Không bắt buộc | Nút kêu gọi hành động cho thẻ kết thúc (end card - `image_ids`) của quảng cáo ô tô xoay vòng (`ad_format` là `CATALOG_CAROUSEL`).<br>Các giá trị enum: • `SEARCH_INVENTORY` (Khuyến nghị)<br>• `LEARN_MORE`<br>• `SHOP_NOW`<br>• `SIGN_UP`<br>• `CONTACT_US`<br>• `BOOK_NOW`<br>• `READ_MORE`<br>• `VIEW_MORE`<br>• `ORDER_NOW`. |
| ↳ music_id | string | Không bắt buộc | ID của bản nhạc muốn sử dụng trong TikTok Carousel Ad. Xem chi tiết tại [Create Carousel Ads-Steps-Create an ad](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1766217791987713). Thay đổi nhạc sẽ khiến quảng cáo được xét duyệt lại. |
| ↳ tiktok_item_id | string | Điều kiện | Bắt buộc khi `identity_type` là `AUTH_CODE` hoặc `BC_AUTH_TT` để tạo Spark Ads (Spark Ads Pull). Không hỗ trợ khi `identity_type` là `CUSTOMIZED_USER`.<br>ID bài đăng TikTok dùng làm Spark Ad. Xem [Create Spark Ads](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1739470744631298), lấy từ [/tt_video/info/](64-spark-ads-using-authorized-posts.md#doc-1738376324021250). |
| ↳ promotional_music_disabled | boolean | Không bắt buộc | Có vô hiệu hóa việc sử dụng nhạc cho mục đích thương mại trong Spark Ad hay không. Mặc định: `true`. Đặt `false` nếu muốn cho phép người dùng duet và stitch video. Chỉ áp dụng cho bài đăng Spark Ads. |
| ↳ item_duet_status | string | Không bắt buộc | Cho phép người dùng duet với video Spark Ads hay không. Enum: • `ENABLE`<br>• `DISABLE`. |
| ↳ item_stitch_status | string | Không bắt buộc | Cho phép người dùng stitch video Spark Ads hay không. Enum: • `ENABLE`<br>• `DISABLE`. |
| ↳ dark_post_status | string | Không bắt buộc | Đặt bài đăng TikTok làm dark post (ẩn khỏi trang cá nhân tự nhiên). Enum: • `ON`<br>• `OFF`. |
| ↳ shopping_ads_video_package_id | string | Không bắt buộc | ID gói video cho Video Shopping Ads tự động tạo từ danh mục sản phẩm. |
| ↳ ad_text | string | Điều kiện | Văn bản quảng cáo hiển thị. Bắt buộc khi tạo hoặc cập nhật nội dung văn bản. Độ dài tối đa 100 ký tự (hoặc theo quy định vị trí). Không thể đặt chuỗi rỗng trừ khi dùng định dạng tự động. |
| ↳ ad_texts | string[] | Điều kiện | Danh sách các văn bản quảng cáo cho tính năng tối ưu hóa văn bản linh hoạt. |
| ↳ call_to_action | string | Điều kiện | Văn bản hiển thị trên nút kêu gọi hành động (Call To Action - CTA). Ví dụ: `LEARN_MORE`, `SHOP_NOW`, `SIGN_UP`, `CONTACT_US`, `DOWNLOAD_NOW`, `VIEW_NOW`, `BOOK_NOW`, v.v. |
| ↳ call_to_action_id | string | Điều kiện | ID nút CTA động lấy từ hệ thống. |
| ↳ card_id | string | Không bắt buộc | ID của thẻ tương tác (Interactive Add-on card). |
| ↳ landing_page_url | string | Điều kiện | URL trang đích khi người dùng nhấp vào quảng cáo. |
| ↳ utm_params | object[] | Không bắt buộc | Danh sách các tham số UTM gắn vào URL trang đích để theo dõi phân tích. |
| ↳↳ key | string | Điều kiện | Tên khóa tham số UTM (ví dụ `utm_source`). |
| ↳↳ value | string | Điều kiện | Giá trị tham số UTM (ví dụ `tiktok`). |
| ↳ page_id | number | Điều kiện | ID trang tức thì TikTok Instant Page hoặc biểu mẫu khách hàng tiềm năng. |
| ↳ cpp_url | string | Không bắt buộc | URL Custom Product Page trên iOS App Store. |
| ↳ deeplink | string | Không bắt buộc | Liên kết mở ứng dụng trực tiếp (deeplink). |
| ↳ deeplink_type | string | Không bắt buộc | Loại deeplink. Enum: • `NORMAL`<br>• `DEFERRED_DEEPLINK`. |
| ↳ shopping_ads_deeplink_type | string | Không bắt buộc | Loại deeplink cho Shopping Ads. Enum: • `NONE`<br>• `CUSTOM`<br>• `SHOPPING_ADS`. |
| ↳ deeplink_utm_params | object[] | Không bắt buộc | Danh sách tham số UTM gắn vào deeplink. |
| ↳↳ key | string | Điều kiện | Khóa tham số UTM deeplink. |
| ↳↳ value | string | Điều kiện | Giá trị tham số UTM deeplink. |
| ↳ shopping_ads_fallback_type | string | Điều kiện | Loại phương án dự phòng khi mở deeplink thất bại trong Shopping Ads. Enum: • `DEFAULT`<br>• `CUSTOM`. |
| ↳ fallback_type | string | Không bắt buộc | Loại điều hướng dự phòng nếu không mở được deeplink. Enum: • `APP_INSTALL`<br>• `WEBSITE`<br>• `UNSET`. |
| ↳ dynamic_destination | string | Không bắt buộc | Đích đến linh hoạt (Dynamic Destination). Enum: • `DLO`<br>• `UNSET`. |
| ↳ instant_product_page_used | boolean | Không bắt buộc | Có sử dụng Trang sản phẩm tức thì (Instant Product Page) hay không. |
| ↳ page_image_index | integer | Không bắt buộc | Chỉ số hình ảnh trên trang đích sản phẩm. |
| ↳ aigc_disclosure_type | string | Không bắt buộc | Loại khai báo nội dung do AI tạo (AIGC). Enum: • `NOT_DECLARED`<br>• `SELF_DECLARED`. |
| ↳ disclaimer_type | string | Không bắt buộc | Loại tuyên bố từ chối trách nhiệm. Enum: • `TEXT_LINK`<br>• `TEXT_ONLY`. |
| ↳ disclaimer_text | object | Điều kiện | Đối tượng chứa văn bản tuyên bố từ chối trách nhiệm dạng thuần văn bản. |
| ↳↳ text | string | Bắt buộc nếu có disclaimer_text | Nội dung văn bản tuyên bố từ chối trách nhiệm. |
| ↳ disclaimer_clickable_texts | object[] | Điều kiện | Danh sách các liên kết nhấp được trong phần tuyên bố từ chối trách nhiệm. |
| ↳↳ text | string | Bắt buộc | Văn bản hiển thị của liên kết. |
| ↳↳ url | string | Bắt buộc | URL đích khi người dùng nhấp vào liên kết. |
| ↳ tracking_pixel_id | number | Không bắt buộc | ID Pixel TikTok dùng để theo dõi sự kiện chuyển đổi ngoài trang web. |
| ↳ tracking_app_id | string | Không bắt buộc | ID ứng dụng được theo dõi qua các đối tác đo lường di động (MMP). |
| ↳ tracking_offline_event_set_ids | string[] | Không bắt buộc | Danh sách ID bộ sự kiện ngoại tuyến (Offline Event Set IDs). |
| ↳ vast_moat_enabled | boolean | Không bắt buộc | Có bật xác minh khả năng xem qua Moat không (khuyến nghị dùng `viewability_postbid_partner`). |
| ↳ viewability_postbid_partner | string | Không bắt buộc | Đối tác bên thứ ba đo lường khả năng hiển thị sau đấu thầu. Enum: • `UNSET`<br>• `MOAT`<br>• `DOUBLE_VERIFY`<br>• `IAS`<br>• `ZEFR`. |
| ↳ viewability_vast_url | string | Điều kiện | URL VAST của bên thứ ba để đo lường khả năng hiển thị (khi đối tác là `IAS`). |
| ↳ brand_safety_postbid_partner | string | Không bắt buộc | Đối tác đo lường an toàn thương hiệu sau đấu thầu. Enum: • `UNSET`<br>• `DOUBLE_VERIFY`<br>• `IAS`<br>• `ZEFR`. |
| ↳ brand_safety_vast_url | string | Điều kiện | URL VAST đo lường an toàn thương hiệu (khi đối tác là `IAS`). |
| ↳ impression_tracking_url | string | Không bắt buộc | URL bên thứ ba để theo dõi lượt hiển thị mặc định của quảng cáo. |
| ↳ click_tracking_url | string | Không bắt buộc | URL bên thứ ba để theo dõi lượt nhấp chuột vào quảng cáo. |
| ↳ video_view_tracking_url | string | Không bắt buộc | URL bên thứ ba giám sát lượt xem video quảng cáo. |
| ↳ playable_url | string | Không bắt buộc | URL tài nguyên quảng cáo tương tác (Playable ad), hỗ trợ trên Pangle và TikTok. Lấy qua endpoint [/playable/get/](56-playable-ads.md#doc-1737732758495234). |
| ↳ creative_type | string | Điều kiện | Loại nội dung sáng tạo cho Live Shopping Ads, Product Shopping Ads, App Pre-Registration, Automotive Ads.<br>Enum: • `SHORT_VIDEO_LIVE`<br>• `DIRECT_LIVE`<br>• `PSA`<br>• `CUSTOM_INSTANT_PAGE`<br>• `AUTO_INVENTORY_INSTANT_PAGE`. |
| ↳ app_name | string | Điều kiện | Tên ứng dụng hiển thị trên quảng cáo tải ứng dụng. Giới hạn: 1-40 ký tự. |
| ↳ display_name | string | Điều kiện | Tên thương hiệu hiển thị cho quảng cáo trang đích hoặc thuần nhận diện. Giới hạn: 1-40 ký tự tiếng Anh hoặc 1-20 ký tự tiếng Trung/Nhật/Hàn. |
| ↳ avatar_icon_web_uri | string | Không bắt buộc | URI ảnh đại diện (avatar) tải lên qua endpoint [Upload an image](47-images.md#doc-1739067433456642) (yêu cầu tỉ lệ 1:1). |
| ↳ creative_authorized | boolean | Không bắt buộc | Có cấp phép hiển thị quảng cáo trong TikTok For Business Creative Center hay không. Chỉ áp dụng cho nhà quảng cáo ngoài Hoa Kỳ, mặc định là `false`. Chỉ hỗ trợ quảng cáo video. |

### Ví dụ yêu cầu

```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/ad/update/' --header 'Access-Token: YOUR_ACCESS_TOKEN' --header 'Content-Type: application/json' --data '{
    "advertiser_id": "7123456789012345678",
    "adgroup_id": "1723456789012345",
    "patch_update": true,
    "creatives": [{
        "ad_id": "1734567890123456",
        "ad_name": "Quảng cáo cập nhật mới",
        "ad_text": "Khám phá bộ sưu tập mùa hè mới nhất ngay hôm nay!"
    }]
}'
```

```python
import json
import requests

url = "https://business-api.tiktok.com/open_api/v1.3/ad/update/"
headers = {
    "Access-Token": "YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json",
}
payload = {
    "advertiser_id": "7123456789012345678",
    "adgroup_id": "1723456789012345",
    "patch_update": True,
    "creatives": [
        {
            "ad_id": "1734567890123456",
            "ad_name": "Quảng cáo cập nhật mới",
            "ad_text": "Khám phá bộ sưu tập mùa hè mới nhất ngay hôm nay!",
        }
    ],
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())
```

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. |
| request_id | string | Mã nhật ký (log ID) định danh duy nhất cho mỗi yêu cầu. |
| data | object | Dữ liệu chi tiết trả về sau khi cập nhật. |
| ↳ ad_ids | string[] | Danh sách các ID quảng cáo đã được cập nhật thành công. |
| ↳ creatives | object[] | Danh sách chi tiết các quảng cáo sau khi cập nhật. |
| ↳↳ advertiser_id | string | ID tài khoản quảng cáo. |
| ↳↳ campaign_id | string | ID chiến dịch. |
| ↳↳ campaign_name | string | Tên chiến dịch. |
| ↳↳ adgroup_id | string | ID nhóm quảng cáo. |
| ↳↳ adgroup_name | string | Tên nhóm quảng cáo. |
| ↳↳ ad_id | string | ID quảng cáo. |
| ↳↳ ad_name | string | Tên quảng cáo. |
| ↳↳ create_time | string | Thời gian tạo quảng cáo (định dạng `YYYY-MM-DD HH:MM:SS`). |
| ↳↳ modify_time | string | Thời gian chỉnh sửa quảng cáo gần nhất. |
| ↳↳ identity_id | string | ID danh tính sử dụng cho quảng cáo. |
| ↳↳ identity_type | string | Loại danh tính: `CUSTOMIZED_USER`, `AUTH_CODE`, `TT_USER`, `BC_AUTH_TT`. |
| ↳↳ identity_authorized_bc_id | string | ID của Business Center liên kết nếu danh tính là `BC_AUTH_TT`. |
| ↳↳ catalog_id | string | ID danh mục sản phẩm được liên kết với quảng cáo. |
| ↳↳ product_specific_type | string | Chiều kích thước chọn sản phẩm: `ALL`, `PRODUCT_SET`, `CUSTOMIZED_PRODUCTS`. |
| ↳↳ item_group_ids | string[] | Danh sách ID SPU sản phẩm. |
| ↳↳ product_set_id | string | ID bộ sản phẩm. |
| ↳↳ sku_ids | string[] | Danh sách ID SKU sản phẩm. |
| ↳↳ vehicle_ids | string[] | Danh sách ID xe trong quảng cáo Automotive Ads. |
| ↳↳ showcase_products | object[] | Danh sách sản phẩm trưng bày trong quảng cáo. |
| ↳↳↳ item_group_id | string | ID SPU của sản phẩm. |
| ↳↳↳ store_id | string | ID cửa hàng chứa sản phẩm. |
| ↳↳↳ catalog_id | string | ID danh mục sản phẩm chứa mặt hàng. |
| ↳↳ ad_format | string | Định dạng quảng cáo: `SINGLE_IMAGE`, `SINGLE_VIDEO`, `LIVE_CONTENT`, `CAROUSEL_ADS`, `CATALOG_CAROUSEL`. |
| ↳↳ vertical_video_strategy | string | Chiến lược video dọc: `UNSET`, `SINGLE_VIDEO`, `CATALOG_VIDEOS`, `CATALOG_UPLOADED_VIDEOS`, `LIVE_STREAM`. |
| ↳↳ dynamic_format | string | Định dạng động: `UNSET`, `DYNAMIC_CREATIVE`. |
| ↳↳ video_id | string | ID video quảng cáo. |
| ↳↳ image_ids | string[] | Danh sách ID hình ảnh sử dụng trong quảng cáo. |
| ↳↳ carousel_image_index | integer | Chỉ số ảnh phụ sử dụng cho carousel. |
| ↳↳ end_card_cta | string | Nút kêu gọi hành động thẻ kết thúc của quảng cáo ô tô. |
| ↳↳ auto_disclaimer_types | string[] | Danh sách các loại tuyên bố từ chối trách nhiệm áp dụng tự động. |
| ↳↳ product_display_field_list | string[] | Danh sách các trường hiển thị thông tin sản phẩm. |
| ↳↳ music_id | string | ID bản nhạc sử dụng trong quảng cáo. |
| ↳↳ tiktok_item_id | string | ID bài đăng TikTok (dành cho Spark Ads). |
| ↳↳ promotional_music_disabled | boolean | Trạng thái vô hiệu hóa nhạc thương mại. |
| ↳↳ item_duet_status | string | Trạng thái bật/tắt duet: `ENABLE`, `DISABLE`. |
| ↳↳ item_stitch_status | string | Trạng thái bật/tắt stitch: `ENABLE`, `DISABLE`. |
| ↳↳ dark_post_status | string | Trạng thái bài đăng ẩn: `ON`, `OFF`. |
| ↳↳ branded_content_disabled | boolean | Trạng thái vô hiệu hóa gắn nhãn nội dung thương hiệu. |
| ↳↳ shopping_ads_video_package_id | string | ID gói video cho Shopping Ads. |
| ↳↳ ad_text | string | Văn bản quảng cáo. |
| ↳↳ ad_texts | string | Danh sách các văn bản quảng cáo. |
| ↳↳ call_to_action | string | Nút kêu gọi hành động (CTA). |
| ↳↳ call_to_action_id | string | ID nút kêu gọi hành động. |
| ↳↳ card_id | string | ID thẻ tương tác. |
| ↳↳ landing_page_url | string | URL trang đích. |
| ↳↳ utm_params | object[] | Danh sách các tham số UTM theo dõi trang đích. |
| ↳↳↳ key | string | Tên tham số UTM. |
| ↳↳↳ value | string | Giá trị tham số UTM. |
| ↳↳ page_id | number | ID trang tức thì TikTok Instant Page. |
| ↳↳ cpp_url | string | URL Custom Product Page trên iOS. |
| ↳↳ tiktok_page_category | string | Phân loại danh mục trang TikTok. |
| ↳↳ phone_region_code | string | Mã quốc gia cho số điện thoại (ví dụ: `US`, `VN`). |
| ↳↳ phone_region_calling_code | string | Mã vùng gọi điện thoại quốc tế (ví dụ: `+84`, `+1`). |
| ↳↳ phone_number | string | Số điện thoại liên hệ. |
| ↳↳ creative_auto_enhancement_strategy_list | string[] | Danh sách chiến lược tự động nâng cao chất lượng nội dung sáng tạo. |
| ↳↳ deeplink | string | Liên kết sâu (deeplink) mở ứng dụng. |
| ↳↳ deeplink_type | string | Loại deeplink: `NORMAL`, `DEFERRED_DEEPLINK`. |
| ↳↳ deeplink_format_type | string | Định dạng deeplink. |
| ↳↳ shopping_ads_deeplink_type | string | Loại deeplink cho Shopping Ads: `NONE`, `CUSTOM`, `SHOPPING_ADS`. |
| ↳↳ deeplink_utm_params | object[] | Tham số UTM gắn vào deeplink. |
| ↳↳↳ key | string | Khóa tham số UTM. |
| ↳↳↳ value | string | Giá trị tham số UTM. |
| ↳↳ shopping_ads_fallback_type | string | Phương án dự phòng mở deeplink cho Shopping Ads: `DEFAULT`, `CUSTOM`. |
| ↳↳ fallback_type | string | Loại điều hướng dự phòng: `APP_INSTALL`, `WEBSITE`, `UNSET`. |
| ↳↳ dynamic_destination | string | Đích đến linh hoạt: `DLO`, `UNSET`. |
| ↳↳ auto_message_id | string | ID tin nhắn phản hồi tự động trong Instant Messaging Ad. |
| ↳↳ aigc_disclosure_type | string | Loại công bố nội dung AI: `NOT_DECLARED`, `SELF_DECLARED`. |
| ↳↳ disclaimer_type | string | Loại tuyên bố từ chối trách nhiệm: `TEXT_LINK`, `TEXT_ONLY`. |
| ↳↳ disclaimer_text | object | Nội dung tuyên bố từ chối trách nhiệm dạng chữ. |
| ↳↳↳ text | string | Nội dung văn bản tuyên bố. |
| ↳↳ disclaimer_clickable_texts | object[] | Danh sách các liên kết có thể nhấp trong tuyên bố. |
| ↳↳↳ text | string | Văn bản liên kết. |
| ↳↳↳ url | string | Địa chỉ URL liên kết. |
| ↳↳ tracking_pixel_id | number | ID Pixel TikTok theo dõi sự kiện trang web. |
| ↳↳ tracking_app_id | string | ID ứng dụng theo dõi sự kiện di động. |
| ↳↳ tracking_offline_event_set_ids | string[] | Danh sách ID bộ sự kiện ngoại tuyến. |
| ↳↳ tracking_message_event_set_id | string | ID bộ sự kiện tin nhắn trong Instant Messaging Ad. |
| ↳↳ vast_moat_enabled | boolean | Trạng thái kích hoạt Moat Viewability Verification. |
| ↳↳ viewability_postbid_partner | string | Đối tác đo lường khả năng xem sau đấu thầu: `UNSET`, `MOAT`, `DOUBLE_VERIFY`, `IAS`, `ZEFR`. |
| ↳↳ viewability_vast_url | string | URL VAST đo lường khả năng xem (đối tác IAS). |
| ↳↳ brand_safety_postbid_partner | string | Đối tác đo lường an toàn thương hiệu: `UNSET`, `DOUBLE_VERIFY`, `IAS`, `ZEFR`. |
| ↳↳ brand_safety_vast_url | string | URL VAST đo lường an toàn thương hiệu (đối tác IAS). |
| ↳↳ impression_tracking_url | string | URL bên thứ ba theo dõi lượt hiển thị mặc định. |
| ↳↳ click_tracking_url | string | URL bên thứ ba theo dõi lượt nhấp. |
| ↳↳ playable_url | string | URL tài nguyên quảng cáo tương tác. |
| ↳↳ operation_status | string | Trạng thái hoạt động của quảng cáo: `ENABLE` (đang bật), `DISABLE` (tắt/tạm dừng), `FROZEN` (bị đóng băng). |
| ↳↳ secondary_status | string | Trạng thái phụ của quảng cáo. Xem [Secondary Status](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳↳ creative_type | string | Loại nội dung sáng tạo: `SHOP_PDP`, `SHOP_PLP`, `SHORT_VIDEO_LIVE`, `DIRECT_LIVE`, `PSA`, `CUSTOM_INSTANT_PAGE`, `AUTO_INVENTORY_INSTANT_PAGE`. |
| ↳↳ app_name | string | Tên ứng dụng hiển thị trong quảng cáo tải app. |
| ↳↳ display_name | string | Tên hiển thị thương hiệu của trang đích. |
| ↳↳ profile_image_url | string | URL ảnh đại diện hiển thị. |
| ↳↳ creative_authorized | boolean | Trạng thái ủy quyền hiển thị quảng cáo trong Creative Center. |
| ↳↳ is_aco | boolean | Cho biết quảng cáo có phải là quảng cáo tự động (Smart Creative) hay không. `true` nếu là ACO, `false` nếu không. |
| ↳↳ is_new_structure | boolean | Cho biết chiến dịch có sử dụng cấu trúc mới hay không. |
| ↳↳ optimization_event | string | Sự kiện tối ưu hóa chuyển đổi của nhóm quảng cáo. Xem chi tiết tại [Conversion events](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1739361474981889). |
| ↳ page_info | object | Thông tin phân trang. |
| ↳↳ page | number | Số trang hiện tại. |
| ↳↳ page_size | number | Số bản ghi trên mỗi trang. |
| ↳↳ total_number | number | Tổng số bản ghi kết quả. |
| ↳↳ total_page | number | Tổng số trang kết quả. |

### Ví dụ phản hồi

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "2023060710032301011023224213552",
  "data": {
    "ad_ids": [
      "1734567890123456"
    ],
    "creatives": [
      {
        "advertiser_id": "7123456789012345678",
        "campaign_id": "1720000000000001",
        "campaign_name": "Chiến dịch Mùa hè 2026",
        "adgroup_id": "1723456789012345",
        "adgroup_name": "Nhóm quảng cáo Hà Nội",
        "ad_id": "1734567890123456",
        "ad_name": "Quảng cáo cập nhật mới",
        "create_time": "2026-05-01 10:00:00",
        "modify_time": "2026-06-07 10:03:23",
        "identity_id": "123456789",
        "identity_type": "CUSTOMIZED_USER",
        "ad_format": "SINGLE_VIDEO",
        "video_id": "v0901234567890",
        "ad_text": "Khám phá bộ sưu tập mùa hè mới nhất ngay hôm nay!",
        "call_to_action": "SHOP_NOW",
        "landing_page_url": "https://example.com/summer-sale",
        "operation_status": "ENABLE",
        "secondary_status": "AD_STATUS_DELIVERY_OK",
        "is_aco": false,
        "is_new_structure": true
      }
    ],
    "page_info": {
      "page": 1,
      "page_size": 1,
      "total_number": 1,
      "total_page": 1
    }
  }
}
```

---

## Cập nhật trạng thái quảng cáo (`Update the statuses of ads`)
<a id="doc-1739953422970882"></a>
<!-- doc_id: 1739953422970882 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/ad/status/update/`

**Mục đích**: Sử dụng endpoint này để bật (enable), tạm dừng/vô hiệu hóa (disable) hoặc xóa (delete) một hoặc nhiều quảng cáo.

> [!NOTE]
> Trạng thái hoạt động của một quảng cáo đã bị xóa hoặc một quảng cáo nằm trong nhóm quảng cáo / chiến dịch đã bị xóa không thể chỉnh sửa được. Bạn có thể sử dụng [/campaign/get/](24-campaign.md#doc-1739315828649986), [/adgroup/get/](07-ad-groups-p1.md#doc-1739314558673922), hoặc [/ad/get/](02-ads-p1.md#doc-1735735588640770) để kiểm tra trạng thái hoạt động hiện tại thông qua trường `operation_status`.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền (access token). Xem chi tiết tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type | string | Bắt buộc | Định dạng nội dung yêu cầu. Giá trị hợp lệ: `application/json`. |

### Tham số (POST JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| advertiser_id | string | Bắt buộc | ID tài khoản quảng cáo (advertiser ID). |
| operation_status | string | Bắt buộc | Thao tác cập nhật trạng thái muốn thực hiện.<br>Các giá trị enum:<br>• `ENABLE`: Bật quảng cáo.<br>• `DISABLE`: Tạm dừng / vô hiệu hóa quảng cáo.<br>• `DELETE`: Xóa quảng cáo.<br>Lưu ý: Không thể thay đổi trạng thái của quảng cáo đã bị xóa hoặc nằm trong nhóm/chiến dịch đã bị xóa. |
| ad_ids | string[] | Điều kiện | Danh sách ID quảng cáo cần cập nhật. Số lượng cho phép: từ 1 đến 20 ID. Phải truyền một trong hai trường `ad_ids` hoặc `aco_ad_ids`. |
| aco_ad_ids | string[] | Điều kiện | Danh sách ID quảng cáo ACO (Smart Creative). Đối với quảng cáo ACO chỉ hỗ trợ trạng thái `ENABLE` và `DISABLE`. Số lượng cho phép: từ 1 đến 20 ID. Phải truyền một trong hai trường `ad_ids` hoặc `aco_ad_ids`. |

### Ví dụ yêu cầu

```bash
curl -H "Access-Token: YOUR_ACCESS_TOKEN" -H "Content-Type: application/json" -X POST -d '{
    "advertiser_id": "7123456789012345678",
    "operation_status": "ENABLE",
    "ad_ids": [
        "1734567890123456",
        "1734567890123457"
    ]
}' https://business-api.tiktok.com/open_api/v1.3/ad/status/update/
```

```python
import requests

url = "https://business-api.tiktok.com/open_api/v1.3/ad/status/update/"
headers = {
    "Access-Token": "YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json",
}
payload = {
    "advertiser_id": "7123456789012345678",
    "operation_status": "ENABLE",
    "ad_ids": [
        "1734567890123456",
        "1734567890123457"
    ],
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())
```

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi từ API. Xem [Appendix-Return Code](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. Xem [Appendix-Return information](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | Mã định danh duy nhất của yêu cầu để theo dõi lỗi. |
| data | object | Dữ liệu kết quả thực hiện. |
| ↳ ad_ids | string[] | Danh sách các ID quảng cáo thông thường đã được cập nhật trạng thái. |
| ↳ aco_ad_ids | string[] | Danh sách các ID quảng cáo ACO đã được cập nhật trạng thái. |
| ↳ status | string | Thao tác trạng thái đã được thực thi thành công. Các giá trị enum: `DELETE`, `DISABLE`, `ENABLE`. |

### Ví dụ phản hồi

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "2026091810032301011023224213552",
  "data": {
    "status": "ENABLE",
    "ad_ids": [
      "1734567890123456",
      "1734567890123457"
    ],
    "aco_ad_ids": []
  }
}
```
