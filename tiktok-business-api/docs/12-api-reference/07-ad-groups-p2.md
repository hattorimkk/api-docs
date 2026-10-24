# Nhóm quảng cáo (Ad Groups) — phần 2/3

Tài liệu này hướng dẫn chi tiết cách tạo nhóm quảng cáo (Ad Group) trên TikTok Business API v1.3. Ở cấp độ nhóm quảng cáo, bạn có thể thiết lập toàn diện các chiến lược phân phối (placements), nhắm mục tiêu đối tượng (targeting), ngân sách và lịch trình phân phối, cũng như các chiến lược đặt giá thầu và mục tiêu tối ưu hóa chiến dịch.

| Endpoint | Method | Đường dẫn | Mục đích |
|---|---|---|---|
| Tạo nhóm quảng cáo | `POST` | `/open_api/v1.3/adgroup/create/` | Tạo một nhóm quảng cáo mới với đầy đủ cấu hình vị trí, đối tượng, ngân sách, lịch chạy và giá thầu |

---

## Tạo nhóm quảng cáo (`Create an ad group`)
<a id="doc-1739499616346114"></a>
<!-- doc_id: 1739499616346114 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/adgroup/create/`

**Mục đích**: Tạo một nhóm quảng cáo mới. Ở cấp độ nhóm quảng cáo, bạn có thể định cấu hình vị trí hiển thị, thiết lập nhắm mục tiêu đối tượng (xem [Nhắm mục tiêu quảng cáo](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1745292439329793)), ngân sách, lịch trình chạy quảng cáo cũng như các tùy chọn đặt giá thầu và tối ưu hóa cho quảng cáo. Chi tiết quy trình và các trường dữ liệu cần thiết xem tại [Tạo nhóm quảng cáo](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1738857874837506).

> [!NOTE]
> - Trước khi di chuyển lệnh gọi API sang phiên bản v1.3, vui lòng tham khảo [Chuyển đổi các API quản lý chiến dịch](../02-overview/tong-quan-va-phien-ban.md#doc-1749537346290689) để nắm rõ các điểm khác biệt chính giữa v1.2 và v1.3.
> - Để xem bảng ánh xạ giữa các tính năng trên TikTok Ads Manager (TTAM) ở cấp chiến dịch, nhóm quảng cáo, quảng cáo và cấu hình API tương ứng, xem [Đối chiếu tính năng chiến dịch trên TTAM và cấu hình API](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1740673047618561).
> - Nếu chiến dịch có thiết lập `special_industries`, hãy đảm bảo các nhóm quảng cáo trong chiến dịch đáp ứng các yêu cầu nhắm mục tiêu nêu tại [Yêu cầu nhắm mục tiêu cho nhóm quảng cáo có danh mục đặc biệt](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1739381236849665).

### Nhóm quảng cáo cho chiến dịch chuyên dụng iOS 14 (`iOS 14 Dedicated Campaigns`)

Đối với chiến dịch chuyên dụng iOS 14, bạn có thể tạo tối đa 2 nhóm quảng cáo đang hoạt động. Để tạo nhóm quảng cáo cho chiến dịch chuyên dụng iOS 14, hãy đặt trường `ios14_targeting` thành `IOS14_PLUS` (đại diện cho các thiết bị đã áp dụng các bản cập nhật quyền riêng tư của iOS). Bạn có thể xem hướng dẫn về Chiến dịch chuyên dụng iOS 14 [tại đây](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1740029173531649).

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Có | Mã truy cập (access token) đã được ủy quyền. Xem chi tiết tại [Xác thực](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| `Content-Type` | string | Có | Định dạng nội dung yêu cầu. Giá trị cho phép: `application/json`. |

### Tham số (POST: JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | Có | ID của nhà quảng cáo TikTok. |
| `campaign_id` | string | Có | ID của chiến dịch quảng cáo mà nhóm quảng cáo này trực thuộc. |
| `adgroup_name` | string | Có | Tên nhóm quảng cáo. Giới hạn độ dài: tối đa 512 ký tự và không được chứa biểu tượng cảm xúc (emoji). |
| `request_id` | string | Không | Mã định danh yêu cầu cho phép tạo các nhóm quảng cáo trùng tên hoặc đảm bảo tính lũy thừa (idempotency) chống gửi lặp trong vòng 10 giây. Giá trị là chuỗi đại diện số nguyên 64-bit (ví dụ: `"123456789"`). Khác với `request_id` trả về trong phản hồi HTTP. |
| `shopping_ads_type` | string | Điều kiện | Bắt buộc và chỉ hợp lệ khi mục tiêu chiến dịch `objective_type` là `PRODUCT_SALES`.<br><br>**Enum**:<br>• `VIDEO`: Quảng cáo mua sắm dạng video (Video Shopping Ads). Xem [Video Shopping Ads](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1741942291730434).<br>• `LIVE`: Quảng cáo mua sắm phát trực tiếp (Live Shopping Ads). Xem [Live Shopping Ads](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1754162402455554).<br>• `PRODUCT_SHOPPING_ADS`: Quảng cáo mua sắm sản phẩm (Product Shopping Ads). Xem [Product Shopping Ads](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1785886237030401). |
| `identity_id` | string | Điều kiện | Bắt buộc và chỉ hợp lệ khi `shopping_ads_type` là `VIDEO` và `product_source` là `SHOWCASE`, hoặc khi `shopping_ads_type` là `LIVE`. ID của danh tính (Identity ID). |
| `identity_type` | string | Điều kiện | Bắt buộc và chỉ hợp lệ khi `shopping_ads_type` là `VIDEO` và `product_source` là `SHOWCASE`, hoặc khi `shopping_ads_type` là `LIVE`.<br><br>**Enum**:<br>• `AUTH_CODE`: Người dùng bài viết được ủy quyền.<br>• `TT_USER`: Người dùng tài khoản TikTok Business.<br>• `BC_AUTH_TT`: Tài khoản TikTok mà Business Center được ủy quyền truy cập.<br>Xem chi tiết tại [Danh tính](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1738958351620097). |
| `identity_authorized_bc_id` | string | Điều kiện | Bắt buộc khi `identity_type` là `BC_AUTH_TT`. ID của Business Center liên kết với tài khoản TikTok. |
| `product_source` | string | Điều kiện | Nguồn sản phẩm (bắt buộc cho Video Shopping Ads và Product Shopping Ads):<br><br>**Enum**:<br>• `CATALOG`: Danh mục sản phẩm (sử dụng với `catalog_id`).<br>• `STORE`: Cửa hàng TikTok Shop (sử dụng với `store_id`).<br>• `SHOWCASE`: Tủ trưng bày sản phẩm TikTok Shop. |
| `catalog_id` | string | Điều kiện | Bắt buộc khi `product_source` là `CATALOG` hoặc `STORE`. Bắt buộc khi `shopping_ads_type` là `PRODUCT_SHOPPING_ADS`. ID danh mục sản phẩm. |
| `catalog_authorized_bc_id` | string | Điều kiện | Bắt buộc khi `shopping_ads_type` là `VIDEO` và `product_source` là `CATALOG` hoặc `STORE`. ID Business Center được ủy quyền truy cập danh mục sản phẩm. |
| `store_id` | string | Điều kiện | ID cửa hàng TikTok Shop. Bắt buộc khi `shopping_ads_type` là `VIDEO` và `product_source` là `STORE`, hoặc khi `shopping_ads_type` là `LIVE`. |
| `store_authorized_bc_id` | string | Điều kiện | Bắt buộc khi truyền `store_id`. ID của Business Center được ủy quyền truy cập cửa hàng. |
| `promotion_type` | string | Điều kiện | Loại quảng bá (vị trí tối ưu hóa). Cần chỉ định khi mục tiêu chiến dịch yêu cầu.<br><br>**Enum**:<br>• `APP`: Ứng dụng di động.<br>• `WEBSITE`: Trang web bên ngoài.<br>• `LEAD_GENERATION`: Thu thập khách hàng tiềm năng (biểu mẫu tức thì / Instant Form).<br>• `LEAD_GEN_CLICK_TO_SOCIAL_MEDIA_APP_MESSAGE`: Nhắn tin qua ứng dụng mạng xã hội (Messenger, WhatsApp, Zalo, LINE).<br>• `TIKTOK_SHOP`: Cửa hàng TikTok Shop.<br>• `LIVE_SHOP`: Phòng phát trực tiếp TikTok Shop. |
| `promotion_target_type` | string | Không | Hợp lệ khi `objective_type` là `LEAD_GENERATION`. Loại mục tiêu quảng bá (`INSTANT_PAGE`: Trang tức thì TikTok). |
| `messaging_app_type` | string | Điều kiện | Bắt buộc khi `promotion_type` là `LEAD_GEN_CLICK_TO_SOCIAL_MEDIA_APP_MESSAGE`. Loại ứng dụng nhắn tin.<br><br>**Enum**:<br>• `MESSENGER`: Facebook Messenger.<br>• `WHATSAPP`: WhatsApp.<br>• `ZALO`: Zalo.<br>• `LINE`: LINE. |
| `messaging_app_account_id` | string | Điều kiện | Bắt buộc khi `messaging_app_type` là `MESSENGER` hoặc `LINE`. ID tài khoản ứng dụng nhắn tin. |
| `phone_region_code` | string | Điều kiện | Bắt buộc khi `messaging_app_type` là `WHATSAPP` hoặc `ZALO`. Mã vùng quốc gia hai chữ cái (ví dụ: `"VN"`). |
| `phone_region_calling_code` | string | Điều kiện | Bắt buộc khi `messaging_app_type` là `WHATSAPP` hoặc `ZALO`. Mã gọi quốc tế (ví dụ: `"+84"`). |
| `phone_number` | string | Điều kiện | Bắt buộc khi `messaging_app_type` là `WHATSAPP` hoặc `ZALO`. Số điện thoại liên hệ (không bao gồm mã vùng). |
| `promotion_website_type` | string | Điều kiện | Loại trang web tức thì (TikTok Instant Page) sử dụng trong nhóm quảng cáo.<br><br>**Enum**:<br>• `UNSET`: Không sử dụng Trang tức thì.<br>• `TIKTOK_NATIVE_PAGE`: Sử dụng Trang tức thì TikTok. |
| `app_id` | string | Điều kiện | ID của ứng dụng di động cần quảng bá. Lấy danh sách qua **/app/list/**. |
| `pixel_id` | string | Điều kiện | ID của TikTok Pixel dùng để theo dõi sự kiện chuyển đổi trên trang web. Bắt buộc khi `optimization_goal` là `CONVERT` hoặc `VALUE`. Lấy qua **/pixel/list/**. |
| `optimization_event` | string | Điều kiện | Sự kiện tối ưu hóa chuyển đổi khi sử dụng Pixel hoặc App ID. Chi tiết các giá trị enum xem tại [Sự kiện tối ưu hóa](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| `custom_conversion_id` | string | Không | ID của Sự kiện chuyển đổi tùy chỉnh (Custom Conversion) sử dụng trong nhóm quảng cáo. |
| `app_config` | object[] | Điều kiện | Cấu hình chi tiết ứng dụng khi mục tiêu chiến dịch `sales_destination` là `WEB_AND_APP`. |
| ↳ `app_id` | string | Điều kiện | ID ứng dụng cần quảng bá trong danh sách `app_config`. |
| `deep_funnel_optimization_status` | string | Không | Trạng thái tối ưu hóa phễu sâu (Deep Funnel Optimization) cho chiến dịch thu thập khách hàng tiềm năng (`ON`, `OFF`). Mặc định: `OFF`. |
| `deep_funnel_event_source` | string | Điều kiện | Bắt buộc khi `deep_funnel_optimization_status` là `ON`. Nguồn sự kiện phễu sâu (`PIXEL`, `OFFLINE`). |
| `deep_funnel_event_source_id` | string | Điều kiện | Bắt buộc khi `deep_funnel_optimization_status` là `ON`. ID nguồn sự kiện phễu sâu (ID Pixel hoặc ID bộ sự kiện ngoại tuyến). |
| `deep_funnel_optimization_event` | string | Điều kiện | Bắt buộc khi `deep_funnel_optimization_status` là `ON`. Sự kiện tối ưu hóa phễu sâu (ví dụ: `QUALIFIED_LEAD`, `CONVERTED_LEAD`). |
| `placement_type` | string | Không | Chiến lược vị trí hiển thị quảng cáo.<br><br>**Enum**:<br>• `PLACEMENT_TYPE_AUTOMATIC`: Tự động phân phối vị trí để đạt kết quả tối ưu.<br>• `PLACEMENT_TYPE_NORMAL`: Chọn vị trí hiển thị thủ công (khi đó phải chỉ định `placements`).<br>**Mặc định**: `PLACEMENT_TYPE_AUTOMATIC`. |
| `placements` | string[] | Điều kiện | Danh sách các vị trí hiển thị quảng cáo (bắt buộc khi `placement_type` là `PLACEMENT_TYPE_NORMAL`).<br><br>**Enum**:<br>• `PLACEMENT_TIKTOK`: Bảng tin TikTok.<br>• `PLACEMENT_PANGLE`: Mạng lưới ứng dụng đối tác Pangle.<br>• `PLACEMENT_GLOBAL_APP_BUNDLE`: Gói ứng dụng toàn cầu. |
| `tiktok_subplacements` | string[] | Không | Vị trí phụ trên TikTok khi mục tiêu chiến dịch là `REACH` hoặc `VIDEO_VIEW`. Enum: `TIKTOK_SEARCH` (Trang kết quả tìm kiếm TikTok). |
| `search_result_enabled` | boolean | Không | Bật hiển thị quảng cáo trên trang kết quả tìm kiếm của TikTok (Search Ads). Mặc định: `true`. |
| `automated_keywords_enabled` | boolean | Không | Bật tính năng từ khóa tự động cho Chiến dịch tìm kiếm (`is_search_campaign` = `true`). Mặc định: `true`. |
| `search_keywords` | object[] | Điều kiện | Danh sách từ khóa thủ công (bắt buộc khi `is_search_campaign` là `true` và `automated_keywords_enabled` là `false`). |
| ↳ `keyword` | string | Điều kiện | Từ khóa tìm kiếm. |
| ↳ `match_type` | string | Điều kiện | Loại khớp từ khóa (`BROAD`, `PHRASE`, `EXACT`). |
| ↳ `keyword_bid_type` | string | Không | Loại giá thầu cho từ khóa (`FOLLOW_ADGROUP`: Theo nhóm quảng cáo, `CUSTOM`: Tùy chỉnh). Mặc định: `FOLLOW_ADGROUP`. |
| ↳ `keyword_bid` | float | Điều kiện | Giá thầu tùy chỉnh cho từ khóa (bắt buộc khi `keyword_bid_type` là `CUSTOM`). |
| `comment_disabled` | boolean | Không | Tắt tính năng bình luận của người dùng trên quảng cáo trong nhóm. Mặc định: `false`. |
| `video_download_disabled` | boolean | Không | Tắt tính năng tải video quảng cáo về máy. Mặc định: `false`. |
| `share_disabled` | boolean | Không | Tắt tính năng chia sẻ quảng cáo sang các nền tảng bên thứ ba. Mặc định: `false`. |
| `blocked_pangle_app_ids` | string[] | Không | Danh sách ID gói chặn ứng dụng Pangle (Blocklist). Tra cứu qua **Get Pangle blocklist**. |
| `saved_audience_id` | string | Không | ID của tệp đối tượng đã lưu (Saved Audience). Sử dụng để áp dụng cấu hình nhắm mục tiêu đã lưu trước đó. |
| `auto_targeting_enabled` | boolean | Không | *(Sắp ngừng hỗ trợ)*. Bật tính năng nhắm mục tiêu tự động. Khuyến nghị sử dụng `smart_audience_enabled`. |
| `shopping_ads_retargeting_type` | string | Điều kiện | Bắt buộc khi `shopping_ads_type` là `VIDEO` và `product_source` là `CATALOG`.<br><br>**Enum**:<br>• `LAB1`: Nhắm mục tiêu lại người dùng đã xem hoặc thêm sản phẩm vào giỏ hàng nhưng chưa mua.<br>• `LAB2`: Nhắm mục tiêu lại người dùng đã mua sản phẩm để bán thêm/bán chéo.<br>• `LAB3`: Tùy chỉnh hành vi nhắm mục tiêu lại theo `included_custom_actions` và `excluded_custom_actions`. |
| `shopping_ads_retargeting_actions_days` | number | Điều kiện | Bắt buộc khi `shopping_ads_retargeting_type` là `LAB1` hoặc `LAB2`. Khoảng thời gian xem xét hành vi (số ngày, ví dụ: `14`, `30`). |
| `included_custom_actions` | object[] | Điều kiện | Danh sách hành động tùy chỉnh cần bao gồm (sử dụng khi `shopping_ads_retargeting_type` là `LAB3`). |
| ↳ `code` | string | Có | Mã hành động tùy chỉnh (`VIEW_PRODUCT`, `ADD_TO_CART`, `PURCHASE`). |
| ↳ `days` | integer | Có | Khung thời gian hoàn thành hành động (số ngày, từ 1 đến 180). |
| `excluded_custom_actions` | object[] | Điều kiện | Danh sách hành động tùy chỉnh cần loại trừ (sử dụng khi `shopping_ads_retargeting_type` là `LAB3`). |
| ↳ `code` | string | Có | Mã hành động loại trừ (`VIEW_PRODUCT`, `ADD_TO_CART`, `PURCHASE`). |
| ↳ `days` | integer | Có | Khung thời gian xét hành vi loại trừ (số ngày). |
| `shopping_ads_retargeting_custom_audience_relation` | string | Không | Quan hệ kết hợp giữa đối tượng tùy chỉnh và đối tượng tiếp thị lại mua sắm (`OR`, `AND`). Mặc định: `OR`. |
| `location_ids` | string[] | Điều kiện | Danh sách ID vị trí địa lý cần nhắm mục tiêu (quốc gia, khu vực, tỉnh/thành phố). Bạn phải chỉ định `location_ids` hoặc `zipcode_ids` hoặc cả hai. Tra cứu ID qua [Get Location IDs](70-tools-p1.md#doc-1737172880570369). |
| `zipcode_ids` | string[] | Điều kiện | Danh sách ID mã bưu chính (Zip code / Postal code) cần nhắm mục tiêu. |
| `languages` | string[] | Không | Danh sách mã ngôn ngữ nhắm mục tiêu. Chi tiết xem [Bảng mã ngôn ngữ](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| `gender` | string | Không | Giới tính nhắm mục tiêu.<br><br>**Enum**:<br>• `GENDER_UNLIMITED`: Không giới hạn giới tính (mặc định).<br>• `GENDER_MALE`: Nam giới.<br>• `GENDER_FEMALE`: Nữ giới. |
| `age_groups` | string[] | Không | Danh sách các nhóm tuổi nhắm mục tiêu.<br><br>**Enum**:<br>• `AGE_13_17`: 13 đến 17 tuổi.<br>• `AGE_18_24`: 18 đến 24 tuổi.<br>• `AGE_25_34`: 25 đến 34 tuổi.<br>• `AGE_35_44`: 35 đến 44 tuổi.<br>• `AGE_45_54`: 45 đến 54 tuổi.<br>• `AGE_55_100`: Từ 55 tuổi trở lên. |
| `spending_power` | string | Không | Khả năng chi tiêu của người dùng.<br><br>**Enum**:<br>• `ALL`: Tất cả người dùng (mặc định).<br>• `HIGH`: Người dùng có sức mua cao. |
| `household_income` | string[] | Không | Nhóm thu nhập hộ gia đình (áp dụng tại Hoa Kỳ).<br><br>**Enum**:<br>• `TOP5`: Top 5% thu nhập cao nhất.<br>• `TOP10`: Top 10%.<br>• `TOP10_25`: Top 10% đến 25%.<br>• `TOP25_50`: Top 25% đến 50%. |
| `audience_ids` | string[] | Không | Danh sách ID tệp đối tượng tùy chỉnh (Custom Audience) cần nhắm mục tiêu. Lấy danh sách ID qua **/dmp/custom_audience/list/**. |
| `smart_audience_enabled` | boolean | Không | Bật tính năng Đối tượng thông minh (Smart Audience) để hệ thống tự động mở rộng đối tượng mục tiêu khi cần thiết nhằm đạt hiệu quả tối ưu. Mặc định: `false`. |
| `excluded_audience_ids` | string[] | Không | Danh sách ID tệp đối tượng tùy chỉnh cần loại trừ khỏi nhóm quảng cáo. |
| `interest_category_ids` | string[] | Không | Danh sách ID danh mục sở thích chung của người dùng. Tra cứu danh mục qua [/tool/interest_category/](70-tools-p1.md#doc-1737172880570369). |
| `interest_keyword_ids` | string[] | Không | Danh sách ID từ khóa sở thích bổ sung của người dùng. Tra cứu qua [/tool/interest_keyword/](70-tools-p1.md#doc-1737172880570369). |
| `purchase_intention_keyword_ids` | string[] | Không | Danh sách ID danh mục ý định mua sắm của người dùng. |
| `actions` | object[] | Không | Danh sách cấu hình nhắm mục tiêu theo hành vi của người dùng trên nền tảng. |
| ↳ `action_scene` | string | Có | Bối cảnh hành vi.<br><br>**Enum**:<br>• `VIDEO_RELATED`: Tương tác với video.<br>• `CREATOR_RELATED`: Tương tác với người sáng tạo nội dung.<br>• `HASHTAG_RELATED`: Tương tác với hashtag. |
| ↳ `action_period` | number | Có | Khoảng thời gian xem xét hành vi tính theo số ngày (`0`: mọi lúc, `7`: 7 ngày qua, `15`: 15 ngày qua). |
| ↳ `video_user_actions` | string[] | Có | Các hành động cụ thể của người dùng (`WATCHED_TO_END`, `LIKED`, `COMMENTED`, `SHARED`). |
| ↳ `action_category_ids` | string[] | Có | Danh sách ID danh mục video mà người dùng đã thực hiện tương tác. |
| `smart_interest_behavior_enabled` | boolean | Không | Bật tính năng Sở thích & Hành vi thông minh (Smart Interests & Behaviors). Mặc định: `false`. |
| `included_pangle_audience_package_ids` | string[] | Không | Danh sách ID gói đối tượng Pangle cần nhắm mục tiêu (chỉ áp dụng cho vị trí Pangle). |
| `excluded_pangle_audience_package_ids` | string[] | Không | Danh sách ID gói đối tượng Pangle cần loại trừ (chỉ áp dụng cho vị trí Pangle). |
| `operating_systems` | string[] | Điều kiện | Hệ điều hành thiết bị cần nhắm mục tiêu (`ANDROID`, `IOS`). Bắt buộc cho các chiến dịch cài đặt ứng dụng. |
| `min_android_version` | string | Không | Phiên bản hệ điều hành Android tối thiểu (ví dụ: `"7.0"`). |
| `ios14_targeting` | string | Điều kiện | Bắt buộc và phải đặt là `IOS14_PLUS` khi chiến dịch là Chiến dịch chuyên dụng iOS 14 (`campaign_type` = `IOS14_CAMPAIGN`). |
| `min_ios_version` | string | Điều kiện | Bắt buộc khi có `ios14_targeting`. Phiên bản iOS tối thiểu (ví dụ: `"14.0"`). |
| `device_model_ids` | string[] | Không | Danh sách ID các dòng mẫu máy thiết bị cụ thể cần nhắm mục tiêu. Tra cứu qua [/tool/device_model/](70-tools-p1.md#doc-1737172880570369). |
| `network_types` | string[] | Không | Loại kết nối mạng (`WIFI`, `2G`, `3G`, `4G`, `5G`). |
| `carrier_ids` | string[] | Không | Danh sách ID nhà mạng viễn thông cần nhắm mục tiêu (phải tương thích với vị trí quốc gia chỉ định). |
| `isp_ids` | string[] | Không | Danh sách ID nhà cung cấp dịch vụ Internet (ISP). |
| `device_price_ranges` | number[] | Không | Khoảng giá thiết bị (tính theo USD, là bội số của 50, ví dụ `[100, 500]`, giá trị `10000` biểu thị trên $1.000). |
| `targeting_expansion` | object | Không | *(Sắp ngừng hỗ trợ)*. Cài đặt mở rộng nhắm mục tiêu đối tượng. |
| ↳ `expansion_enabled` | boolean | Có | Bật/tắt mở rộng nhắm mục tiêu. |
| ↳ `expansion_types` | string[] | Điều kiện | Bắt buộc khi `expansion_enabled` là `true`. Các loại mở rộng: `AGE`, `GENDER`, `INTEREST_AND_BEHAVIOR`, `TARGETING_AUDIENCE`. |
| `audience_type` | string | Điều kiện | Bắt buộc khi `app_promotion_type` là `APP_RETARGETING`. Loại đối tượng ứng dụng. |
| `audience_rule` | object | Không | Quy tắc nhắm mục tiêu nâng cao cho chiến dịch Lưu lượng truy cập (Traffic) hoặc Quảng bá ứng dụng (App Promotion). |
| `contextual_tag_ids` | string[] | Không | Danh sách ID thẻ ngữ cảnh nội dung video. Tra cứu qua [/tool/contextual_tag/get/](70-tools-p2.md#doc-1747747118654465). |
| `brand_safety_type` | string | Không | Cấp độ an toàn thương hiệu cho vị trí TikTok (`EXPANDED_INVENTORY`, `STANDARD_INVENTORY`, `LIMITED_INVENTORY`, `THIRD_PARTY`). Mặc định: `STANDARD_INVENTORY`. |
| `brand_safety_partner` | string | Điều kiện | Đối tác an toàn thương hiệu bên thứ ba khi `brand_safety_type` là `THIRD_PARTY` (`IAS`, `OPEN_SLATE`, `ZEFR`). |
| `category_exclusion_ids` | string[] | Không | Danh sách ID danh mục nội dung nhạy cảm cần loại trừ khỏi phân phối quảng cáo. |
| `vertical_sensitivity_id` | string | Không | ID mức độ nhạy cảm ngành nghề dọc theo tiêu chuẩn an toàn nội dung. |
| `budget_mode` | string | Có | Chế độ ngân sách của nhóm quảng cáo.<br><br>**Enum**:<br>• `BUDGET_MODE_DAY`: Ngân sách hàng ngày.<br>• `BUDGET_MODE_TOTAL`: Tổng ngân sách cho toàn bộ thời gian chạy.<br>*(Lưu ý: Nếu chiến dịch bật Tối ưu hóa ngân sách chiến dịch CBO, cài đặt ngân sách ở nhóm quảng cáo sẽ bị bỏ qua).* |
| `budget` | float | Có | Số tiền ngân sách cho nhóm quảng cáo. Nếu chiến dịch bật CBO, tham số này sẽ bị bỏ qua. |
| `schedule_type` | string | Có | Loại lịch chạy quảng cáo.<br><br>**Enum**:<br>• `SCHEDULE_START_END`: Chạy trong khoảng thời gian xác định có ngày bắt đầu và kết thúc.<br>• `SCHEDULE_FROM_NOW`: Bắt đầu chạy ngay (hoặc từ thời điểm xác định) và chạy liên tục không có ngày kết thúc. |
| `schedule_start_time` | datetime | Có | Thời gian bắt đầu chạy quảng cáo (múi giờ UTC+0), định dạng `"YYYY-MM-DD HH:MM:SS"`. Thời gian bắt đầu tối đa có thể lên tới 12 tiếng trong quá khứ hoặc tối đa 400 ngày trong tương lai. |
| `schedule_end_time` | datetime | Điều kiện | Thời gian kết thúc chạy quảng cáo (UTC+0), định dạng `"YYYY-MM-DD HH:MM:SS"`. Bắt buộc khi `schedule_type` là `SCHEDULE_START_END` hoặc `budget_mode` là `BUDGET_MODE_TOTAL`. |
| `dayparting` | string | Không | Lịch phân phối quảng cáo theo khung giờ trong tuần (Dayparting). Chuỗi gồm 48 x 7 = 336 ký tự (mỗi ký tự đại diện cho một khoảng 30 phút trong tuần, bắt đầu từ Thứ Hai 00:00 UTC). Ký tự `'1'` là phân phối, `'0'` là ngừng phân phối. |
| `optimization_goal` | string | Có | Mục tiêu tối ưu hóa của nhóm quảng cáo.<br><br>**Enum**:<br>• `CLICK`: Lượt nhấp vào quảng cáo.<br>• `PAGE_VISIT`: Lượt truy cập trang đích.<br>• `CONVERT`: Lượt chuyển đổi hành động trên trang.<br>• `INSTALL`: Lượt cài đặt ứng dụng.<br>• `IN_APP_EVENT`: Lượt kích hoạt sự kiện trong ứng dụng.<br>• `TRAFFIC_LANDING_PAGE_VIEW`: Lượt xem trang đích lưu lượng truy cập.<br>• `LEAD_GENERATION`: Lượt thu thập thông tin khách hàng tiềm năng.<br>• `CONVERSATION`: Bắt đầu cuộc trò chuyện tin nhắn.<br>• `FOLLOWERS`: Lượt người theo dõi mới.<br>• `VALUE`: Tối ưu hóa giá trị chuyển đổi (VBO).<br>• `AUTOMATIC_VALUE_OPTIMIZATION`: Tối ưu hóa giá trị tự động.<br>• `PRODUCT_CLICK_IN_LIVE`: Lượt nhấp vào sản phẩm trong livestream.<br>• `MT_LIVE_ROOM`: Lượt xem phòng livestream TikTok.<br>• `DESTINATION_VISIT`: Lượt ghé thăm đích đến.<br>• `SHOW`: Số lượt hiển thị quảng cáo.<br>• `REACH`: Số người tiếp cận độc nhất.<br>• `ENGAGED_VIEW`: Lượt xem video có tương tác (tối thiểu 6 giây).<br>• `ENGAGED_VIEW_FIFTEEN`: Lượt xem video có tương tác tối thiểu 15 giây. |
| `secondary_optimization_event` | string | Không | Mục tiêu tối ưu hóa thứ cấp khi mục tiêu chính là Cài đặt (`INSTALL`) hoặc Giá trị (`VALUE`). Ví dụ: `NEXT_DAY_OPEN` (mở ứng dụng ngày tiếp theo). |
| `message_event_set_id` | string | Điều kiện | ID bộ sự kiện tin nhắn. Bắt buộc khi `promotion_type` là `LEAD_GEN_CLICK_TO_SOCIAL_MEDIA_APP_MESSAGE` và `messaging_app_type` là `WHATSAPP` hoặc `ZALO`. |
| `frequency` | number | Điều kiện | Số lần hiển thị quảng cáo tối đa cho một người dùng (chỉ áp dụng cho mục tiêu `REACH`). |
| `frequency_schedule` | number | Điều kiện | Khoảng thời gian (số ngày) áp dụng giới hạn tần suất hiển thị (chỉ áp dụng cho mục tiêu `REACH`). |
| `bid_type` | string | Điều kiện | Chiến lược đặt giá thầu.<br><br>**Enum**:<br>• `BID_TYPE_CUSTOM`: Đặt giá thầu thủ công (Cost Cap hoặc Target Cost).<br>• `BID_TYPE_NO_BID`: Không đặt giá thầu (hệ thống tự động tối ưu hóa để đạt kết quả tối đa với ngân sách).<br>• `BID_TYPE_LOWEST_COST`: Chi phí thấp nhất (Lowest Cost). |
| `bid_price` | float | Điều kiện | Mức giá thầu thủ công (bắt buộc khi `bid_type` là `BID_TYPE_CUSTOM` và `billing_event` là `CPC`, `CPM`, hoặc `CPV`). |
| `conversion_bid_price` | float | Điều kiện | Giá thầu mục tiêu theo mỗi chuyển đổi CPA (bắt buộc khi `bid_type` là `BID_TYPE_CUSTOM` và `billing_event` là `OCPM`). |
| `deep_bid_type` | string | Điều kiện | Chiến lược đặt giá thầu cho sự kiện trong ứng dụng hoặc tối ưu hóa giá trị (VBO).<br><br>**Enum**:<br>• `DEFAULT`: Mặc định.<br>• `VO_MIN_ROAS`: Mục tiêu ROAS tối thiểu.<br>• `VO_HIGHEST_VALUE`: Giá trị cao nhất. |
| `roas_bid` | float | Điều kiện | Mục tiêu ROAS khi `deep_bid_type` là `VO_MIN_ROAS`. Giá trị là tỷ lệ số thực (ví dụ: `2.5` tương đương ROAS 250%). |
| `vbo_window` | string | Không | Cửa sổ thời gian áp dụng chiến lược đặt giá thầu VBO (`SEVEN_DAYS`, `ONE_DAY`, `ZERO_DAY`). |
| `bid_display_mode` | string | Điều kiện | Chế độ hiển thị giá thầu. Bắt buộc phải đặt là `CPV` (Cost per One View) khi mục tiêu là `VIDEO_VIEW`. |
| `next_day_retention` | float | Không | Tỷ lệ giữ chân người dùng ngày hôm sau mục tiêu (chỉ áp dụng cho vị trí Pangle khi `secondary_optimization_event` là `NEXT_DAY_OPEN`). |
| `click_attribution_window` | string | Không | Cửa sổ phân bổ lượt nhấp (Click-through Attribution Window).<br><br>**Enum**:<br>• `OFF`: Tắt.<br>• `ONE_DAY`: 1 ngày.<br>• `SEVEN_DAYS`: 7 ngày (mặc định).<br>• `FOURTEEN_DAYS`: 14 ngày.<br>• `TWENTY_EIGHT_DAYS`: 28 ngày. |
| `engaged_view_attribution_window` | string | Không | Cửa sổ phân bổ lượt xem có tương tác (Engaged View-through Attribution Window).<br><br>**Enum**:<br>• `OFF`: Tắt.<br>• `ONE_DAY`: 1 ngày (mặc định).<br>• `SEVEN_DAYS`: 7 ngày. |
| `view_attribution_window` | string | Không | Cửa sổ phân bổ lượt xem qua (View-through Attribution Window).<br><br>**Enum**:<br>• `OFF`: Tắt.<br>• `ONE_DAY`: 1 ngày (mặc định).<br>• `SEVEN_DAYS`: 7 ngày. |
| `attribution_event_count` | string | Không | Cách thức tính số lượng sự kiện phân bổ.<br><br>**Enum**:<br>• `EVERY`: Tính tất cả các lần hoàn thành sự kiện sau khi nhấp/xem quảng cáo.<br>• `ONCE`: Chỉ tính lần hoàn thành sự kiện đầu tiên. |
| `billing_event` | string | Có | Sự kiện dùng để tính phí quảng cáo.<br><br>**Enum**:<br>• `CPC`: Trả phí theo lượt nhấp chuột (Cost Per Click).<br>• `CPM`: Trả phí theo mỗi 1.000 lượt hiển thị (Cost Per Mille).<br>• `CPV`: Trả phí theo lượt xem video 6 giây (Cost Per View).<br>• `OCPM`: Đặt giá thầu tối ưu hóa theo lượt hiển thị (Optimized Cost Per Mille). |
| `pacing` | string | Có | Tốc độ chi tiêu ngân sách.<br><br>**Enum**:<br>• `PACING_MODE_SMOOTH`: Phân bổ ngân sách đồng đều trong suốt thời gian chạy (mặc định).<br>• `PACING_MODE_FAST`: Chi tiêu ngân sách càng nhanh càng tốt. |
| `statistic_type` | string | Không | Kiểu thống kê giá thầu chuyển đổi (`EVERYTIME`: Mỗi lần mua hàng, `NONE`: Lần mua hàng duy nhất). |
| `is_hfss` | boolean | Không | Khai báo nội dung quảng cáo có thuộc sản phẩm/thương hiệu HFSS (thực phẩm giàu chất béo, muối, đường) hay không. Mặc định: `false`. |
| `is_lhf_compliance` | boolean | Không | Khai báo nội dung quảng cáo có tuân thủ các quy định LHF (thực phẩm ít lành mạnh) hay không. Mặc định: `false`. |
| `operation_status` | string | Không | Trạng thái hoạt động của nhóm quảng cáo ngay khi được tạo thành công.<br><br>**Enum**:<br>• `ENABLE`: Kích hoạt nhóm quảng cáo ngay lập tức (mặc định).<br>• `DISABLE`: Tạo nhóm quảng cáo ở trạng thái tạm dừng. |
| `creative_material_mode` | string | Không | Chế độ phân phối tài liệu sáng tạo. Enum: `CUSTOM` (tùy chỉnh). Mặc định: `CUSTOM`. |
| `adgroup_app_profile_page_state` | string | Không | Bật hoặc tắt Trang hồ sơ ứng dụng (App Profile Page) cho quảng cáo ứng dụng (`ON`, `OFF`). |
| `conversion_window` | string | Không | *(Đã ngừng hỗ trợ - deprecated)*. Khung thời gian chuyển đổi cũ. Khuyến nghị sử dụng các trường phân bổ attribution window mới (`click_attribution_window`, `view_attribution_window`). |

### Bảng ánh xạ sự kiện tính phí theo mục tiêu tối ưu hóa

Khi bạn chỉ định một mục tiêu tối ưu hóa (`optimization_goal`) cho nhóm quảng cáo, bạn cần đồng thời chỉ định sự kiện tính phí (`billing_event`) tương ứng phù hợp theo bảng dưới đây:

| Giá trị `optimization_goal` | Giá trị `billing_event` tương ứng |
|---|---|
| `CLICK` | `CPC` |
| `PAGE_VISIT` | `CPC` |
| `CONVERT` | `OCPM` |
| `INSTALL` | `OCPM` |
| `IN_APP_EVENT` | `OCPM` |
| `TRAFFIC_LANDING_PAGE_VIEW` | `OCPM` |
| `LEAD_GENERATION` | `OCPM` |
| `CONVERSATION` | `OCPM` |
| `FOLLOWERS` | `OCPM` |
| `VALUE` | `OCPM` |
| `AUTOMATIC_VALUE_OPTIMIZATION` | `OCPM` |
| `PRODUCT_CLICK_IN_LIVE` | `OCPM` |
| `MT_LIVE_ROOM` | `OCPM` |
| `DESTINATION_VISIT` | `OCPM` |
| `SHOW` | `CPM` |
| `REACH` | `CPM` |
| `ENGAGED_VIEW` | `CPV` |
| `ENGAGED_VIEW_FIFTEEN` | `CPV` |

### Ví dụ yêu cầu

#### cURL: Tạo nhóm quảng cáo chuyển đổi trang web
```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/adgroup/create/" \
  -H "Access-Token: ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "advertiser_id": "6789012345678901234",
    "campaign_id": "1712345678901234",
    "adgroup_name": "Nhóm quảng cáo chuyển đổi mùa thu",
    "promotion_type": "WEBSITE",
    "placement_type": "PLACEMENT_TYPE_NORMAL",
    "placements": ["PLACEMENT_TIKTOK"],
    "video_download_disabled": false,
    "location_ids": ["6252001"],
    "gender": "GENDER_UNLIMITED",
    "operating_systems": ["ANDROID", "IOS"],
    "budget_mode": "BUDGET_MODE_DAY",
    "budget": 50.0,
    "schedule_type": "SCHEDULE_START_END",
    "schedule_start_time": "2024-11-01 00:00:00",
    "schedule_end_time": "2024-11-30 23:59:59",
    "optimization_goal": "CONVERT",
    "pixel_id": "C1234567890ABCDEF",
    "optimization_event": "COMPLETE_PAYMENT",
    "bid_type": "BID_TYPE_NO_BID",
    "billing_event": "OCPM",
    "pacing": "PACING_MODE_SMOOTH",
    "operation_status": "ENABLE"
  }'
```

#### Python: Tạo nhóm quảng cáo chuyển đổi trang web
```python
import requests

ACCESS_TOKEN = "your_access_token"
ADVERTISER_ID = "6789012345678901234"
CAMPAIGN_ID = "1712345678901234"

url = "https://business-api.tiktok.com/open_api/v1.3/adgroup/create/"
headers = {
    "Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}
payload = {
    "advertiser_id": ADVERTISER_ID,
    "campaign_id": CAMPAIGN_ID,
    "adgroup_name": "Nhóm quảng cáo chuyển đổi mùa thu",
    "promotion_type": "WEBSITE",
    "placement_type": "PLACEMENT_TYPE_NORMAL",
    "placements": ["PLACEMENT_TIKTOK"],
    "video_download_disabled": False,
    "location_ids": ["6252001"],
    "gender": "GENDER_UNLIMITED",
    "operating_systems": ["ANDROID", "IOS"],
    "budget_mode": "BUDGET_MODE_DAY",
    "budget": 50.0,
    "schedule_type": "SCHEDULE_START_END",
    "schedule_start_time": "2024-11-01 00:00:00",
    "schedule_end_time": "2024-11-30 23:59:59",
    "optimization_goal": "CONVERT",
    "pixel_id": "C1234567890ABCDEF",
    "optimization_event": "COMPLETE_PAYMENT",
    "bid_type": "BID_TYPE_NO_BID",
    "billing_event": "OCPM",
    "pacing": "PACING_MODE_SMOOTH",
    "operation_status": "ENABLE"
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())
```

#### cURL: Tạo nhóm quảng cáo tìm kiếm khách hàng tiềm năng (Lead Generation)
```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/adgroup/create/" \
  -H "Access-Token: ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "advertiser_id": "6789012345678901234",
    "campaign_id": "1712345678901235",
    "adgroup_name": "Nhóm quảng cáo Lead Gen Instant Form",
    "promotion_type": "LEAD_GENERATION",
    "promotion_target_type": "INSTANT_PAGE",
    "placement_type": "PLACEMENT_TYPE_NORMAL",
    "placements": ["PLACEMENT_TIKTOK"],
    "location_ids": ["6252001"],
    "gender": "GENDER_UNLIMITED",
    "budget_mode": "BUDGET_MODE_DAY",
    "budget": 30.0,
    "schedule_type": "SCHEDULE_START_END",
    "schedule_start_time": "2024-11-01 00:00:00",
    "schedule_end_time": "2024-11-15 23:59:59",
    "optimization_goal": "LEAD_GENERATION",
    "billing_event": "OCPM",
    "bid_type": "BID_TYPE_NO_BID",
    "pacing": "PACING_MODE_SMOOTH",
    "operation_status": "ENABLE"
  }'
```

#### cURL: Tạo nhóm quảng cáo mua sắm qua video (Video Shopping Ads)
```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/adgroup/create/" \
  -H "Access-Token: ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "advertiser_id": "6789012345678901234",
    "campaign_id": "1712345678901236",
    "adgroup_name": "Nhóm quảng cáo Video Shopping Ads",
    "shopping_ads_type": "VIDEO",
    "product_source": "CATALOG",
    "catalog_id": "7123456789012345",
    "catalog_authorized_bc_id": "6789012345678901234",
    "identity_id": "7123456789012346",
    "identity_type": "BC_AUTH_TT",
    "identity_authorized_bc_id": "6789012345678901234",
    "placement_type": "PLACEMENT_TYPE_NORMAL",
    "placements": ["PLACEMENT_TIKTOK"],
    "location_ids": ["6252001"],
    "budget_mode": "BUDGET_MODE_DAY",
    "budget": 100.0,
    "schedule_type": "SCHEDULE_START_END",
    "schedule_start_time": "2024-11-01 00:00:00",
    "schedule_end_time": "2024-11-30 23:59:59",
    "optimization_goal": "CONVERT",
    "billing_event": "OCPM",
    "bid_type": "BID_TYPE_CUSTOM",
    "conversion_bid_price": 5.0,
    "pacing": "PACING_MODE_SMOOTH",
    "operation_status": "ENABLE"
  }'
```
---

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Giá trị `0` là thành công. Xem [Phụ lục mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Mã log định danh duy nhất của yêu cầu API. |
| `data` | object | Dữ liệu chi tiết của nhóm quảng cáo được tạo. |
| ↳ `advertiser_id` | string | ID tài khoản nhà quảng cáo. |
| ↳ `campaign_id` | string | ID chiến dịch quảng cáo trực thuộc. |
| ↳ `campaign_name` | string | Tên của chiến dịch quảng cáo. |
| ↳ `adgroup_id` | string | ID duy nhất của nhóm quảng cáo vừa được tạo. |
| ↳ `adgroup_name` | string | Tên của nhóm quảng cáo. |
| ↳ `create_time` | string | Thời điểm tạo nhóm quảng cáo theo định dạng `YYYY-MM-DD HH:MM:SS` (UTC+0). |
| ↳ `modify_time` | string | Thời điểm cập nhật nhóm quảng cáo gần nhất. |
| ↳ `shopping_ads_type` | string | Loại quảng cáo mua sắm (`VIDEO`, `LIVE`, `PRODUCT_SHOPPING_ADS`). |
| ↳ `identity_id` | string | ID của danh tính liên kết. |
| ↳ `identity_type` | string | Loại danh tính (`AUTH_CODE`, `TT_USER`, `BC_AUTH_TT`). |
| ↳ `identity_authorized_bc_id` | string | ID Business Center liên kết với danh tính tài khoản TikTok. |
| ↳ `product_source` | string | Nguồn sản phẩm (`CATALOG`, `STORE`, `SHOWCASE`). |
| ↳ `catalog_id` | string | ID danh mục sản phẩm. |
| ↳ `catalog_authorized_bc_id` | string | ID Business Center được ủy quyền danh mục sản phẩm. |
| ↳ `store_id` | string | ID cửa hàng TikTok Shop. |
| ↳ `store_authorized_bc_id` | string | ID Business Center được ủy quyền cửa hàng. |
| ↳ `promotion_type` | string | Loại mục tiêu quảng bá (`APP`, `WEBSITE`, `LEAD_GENERATION`, `LEAD_GEN_CLICK_TO_SOCIAL_MEDIA_APP_MESSAGE`, `TIKTOK_SHOP`, `LIVE_SHOP`). |
| ↳ `promotion_target_type` | string | Loại mục tiêu phụ (`INSTANT_PAGE`). |
| ↳ `messaging_app_type` | string | Loại ứng dụng nhắn tin (`MESSENGER`, `WHATSAPP`, `ZALO`, `LINE`). |
| ↳ `messaging_app_account_id` | string | ID tài khoản ứng dụng nhắn tin Messenger hoặc LINE. |
| ↳ `phone_region_code` | string | Mã vùng quốc gia của số điện thoại WhatsApp/Zalo. |
| ↳ `phone_region_calling_code` | string | Mã gọi quốc tế của số điện thoại WhatsApp/Zalo. |
| ↳ `phone_number` | string | Số điện thoại WhatsApp/Zalo nhận tin nhắn từ quảng cáo. |
| ↳ `promotion_website_type` | string | Loại trang web tức thì (`UNSET`, `TIKTOK_NATIVE_PAGE`). |
| ↳ `app_id` | string | ID của ứng dụng di động được quảng bá. |
| ↳ `app_type` | string | Loại ứng dụng di động (`APP_ANDROID`, `APP_IOS`). |
| ↳ `app_download_url` | string | Đường dẫn tải ứng dụng trên Google Play hoặc App Store. |
| ↳ `pixel_id` | string | ID TikTok Pixel liên kết. |
| ↳ `optimization_event` | string | Sự kiện tối ưu hóa chuyển đổi. |
| ↳ `custom_conversion_id` | string | ID sự kiện chuyển đổi tùy chỉnh. |
| ↳ `app_config` | object[] | Cấu hình ứng dụng khi mục tiêu là web và app. |
| ↳↳ `app_id` | string | ID ứng dụng trong danh sách cấu hình. |
| ↳ `deep_funnel_optimization_status` | string | Trạng thái tối ưu hóa phễu sâu (`ON`, `OFF`). |
| ↳ `deep_funnel_event_source` | string | Nguồn sự kiện phễu sâu (`PIXEL`, `OFFLINE`). |
| ↳ `deep_funnel_event_source_id` | string | ID nguồn sự kiện phễu sâu. |
| ↳ `deep_funnel_optimization_event` | string | Sự kiện phễu sâu được tối ưu hóa. |
| ↳ `placement_type` | string | Chiến lược vị trí (`PLACEMENT_TYPE_AUTOMATIC`, `PLACEMENT_TYPE_NORMAL`). |
| ↳ `placements` | string[] | Danh sách vị trí hiển thị (`PLACEMENT_TIKTOK`, `PLACEMENT_PANGLE`, `PLACEMENT_GLOBAL_APP_BUNDLE`). |
| ↳ `tiktok_subplacements` | string[] | Danh sách vị trí phụ trên TikTok (`TIKTOK_SEARCH`). |
| ↳ `search_result_enabled` | boolean | Trạng thái hiển thị quảng cáo trong kết quả tìm kiếm. |
| ↳ `automated_keywords_enabled` | boolean | Trạng thái bật từ khóa tự động trong Search Ads. |
| ↳ `search_keywords` | object[] | Danh sách từ khóa tìm kiếm đã thiết lập. |
| ↳↳ `keyword` | string | Từ khóa tìm kiếm. |
| ↳↳ `match_type` | string | Loại khớp (`BROAD`, `PHRASE`, `EXACT`). |
| ↳↳ `keyword_bid_type` | string | Loại giá thầu từ khóa (`FOLLOW_ADGROUP`, `CUSTOM`). |
| ↳↳ `keyword_bid` | float | Giá thầu của từ khóa. |
| ↳↳ `audit_status` | string | Trạng thái kiểm duyệt của từ khóa (`AUDIT_PASS`, `AUDIT_REJECT`, `AUDIT_PROCESSING`). |
| ↳↳ `reject_info` | object[] | Thông tin chi tiết khi từ khóa bị từ chối kiểm duyệt. |
| ↳↳↳ `forbidden_location` | string | Khu vực cấm từ khóa. |
| ↳↳↳ `reject_reasons` | object[] | Danh sách các lý do từ chối. |
| ↳↳↳↳ `reason` | string | Lý do cụ thể khiến từ khóa bị từ chối. |
| ↳ `comment_disabled` | boolean | Trạng thái vô hiệu hóa bình luận. |
| ↳ `video_download_disabled` | boolean | Trạng thái vô hiệu hóa tải video. |
| ↳ `share_disabled` | boolean | Trạng thái vô hiệu hóa chia sẻ quảng cáo. |
| ↳ `blocked_pangle_app_ids` | string[] | Danh sách ID gói ứng dụng Pangle bị chặn. |
| ↳ `audience_rule` | object | Cấu hình quy tắc nhắm đối tượng mục tiêu nâng cao. |
| ↳ `audience_type` | string | Loại đối tượng ứng dụng cho tiếp thị lại. |
| ↳ `saved_audience_id` | string | ID đối tượng đã lưu được áp dụng. |
| ↳ `auto_targeting_enabled` | boolean | Trạng thái bật nhắm mục tiêu tự động. |
| ↳ `shopping_ads_retargeting_type` | string | Loại nhắm mục tiêu lại mua sắm (`LAB1`, `LAB2`, `LAB3`). |
| ↳ `shopping_ads_retargeting_actions_days` | number | Khung thời gian hành vi tiếp thị lại mua sắm. |
| ↳ `included_custom_actions` | object[] | Hành vi tùy chỉnh bao gồm. |
| ↳↳ `code` | string | Mã hành động (`VIEW_PRODUCT`, `ADD_TO_CART`, `PURCHASE`). |
| ↳↳ `days` | integer | Số ngày xét hành vi. |
| ↳ `excluded_custom_actions` | object[] | Hành vi tùy chỉnh loại trừ. |
| ↳↳ `code` | string | Mã hành động loại trừ. |
| ↳↳ `days` | integer | Số ngày xét hành vi loại trừ. |
| ↳ `shopping_ads_retargeting_custom_audience_relation` | string | Quan hệ kết hợp đối tượng tiếp thị lại (`OR`, `AND`). |
| ↳ `location_ids` | string[] | Danh sách ID vị trí địa lý được nhắm mục tiêu. |
| ↳ `zipcode_ids` | string[] | Danh sách ID mã bưu chính được nhắm mục tiêu. |
| ↳ `languages` | string[] | Danh sách mã ngôn ngữ được nhắm mục tiêu. |
| ↳ `gender` | string | Giới tính nhắm mục tiêu (`GENDER_MALE`, `GENDER_FEMALE`, `GENDER_UNLIMITED`). |
| ↳ `age_groups` | string[] | Danh sách nhóm tuổi được nhắm mục tiêu. |
| ↳ `spending_power` | string | Khả năng chi tiêu của đối tượng (`ALL`, `HIGH`). |
| ↳ `household_income` | string[] | Nhóm thu nhập hộ gia đình (`TOP5`, `TOP10`, `TOP10_25`, `TOP25_50`). |
| ↳ `audience_ids` | string[] | Danh sách ID tệp đối tượng tùy chỉnh bao gồm. |
| ↳ `smart_audience_enabled` | boolean | Trạng thái bật Đối tượng thông minh. |
| ↳ `excluded_audience_ids` | string[] | Danh sách ID tệp đối tượng tùy chỉnh bị loại trừ. |
| ↳ `interest_category_ids` | string[] | Danh sách ID danh mục sở thích chung. |
| ↳ `interest_keyword_ids` | string[] | Danh sách ID từ khóa sở thích bổ sung. |
| ↳ `purchase_intention_keyword_ids` | string[] | Danh sách ID danh mục ý định mua sắm. |
| ↳ `actions` | object[] | Danh sách cấu hình nhắm mục tiêu theo hành vi. |
| ↳↳ `action_scene` | string | Bối cảnh hành vi (`VIDEO_RELATED`, `CREATOR_RELATED`, `HASHTAG_RELATED`). |
| ↳↳ `action_period` | number | Khung thời gian hành vi (`0`, `7`, `15` ngày). |
| ↳↳ `video_user_actions` | string[] | Danh sách hành động cụ thể trên video (`WATCHED_TO_END`, `LIKED`, `COMMENTED`, `SHARED`). |
| ↳↳ `action_category_ids` | string[] | Danh mục video tương tác. |
| ↳ `smart_interest_behavior_enabled` | boolean | Trạng thái bật Sở thích & Hành vi thông minh. |
| ↳ `included_pangle_audience_package_ids` | string[] | Danh sách gói đối tượng Pangle bao gồm. |
| ↳ `excluded_pangle_audience_package_ids` | string[] | Danh sách gói đối tượng Pangle loại trừ. |
| ↳ `operating_systems` | string[] | Hệ điều hành thiết bị (`ANDROID`, `IOS`). |
| ↳ `min_android_version` | string | Phiên bản Android tối thiểu. |
| ↳ `ios14_targeting` | string | Cấu hình nhắm mục tiêu iOS 14 (`IOS14_PLUS`, `UNSET`). |
| ↳ `min_ios_version` | string | Phiên bản iOS tối thiểu. |
| ↳ `ios14_quota_type` | string | Trạng thái hạn mức nhóm quảng cáo iOS 14 (`OCCUPIED`, `UNOCCUPIED`). |
| ↳ `device_model_ids` | string[] | Danh sách ID dòng mẫu máy thiết bị. |
| ↳ `network_types` | string[] | Loại kết nối mạng (`WIFI`, `2G`, `3G`, `4G`, `5G`). |
| ↳ `carrier_ids` | string[] | Danh sách ID nhà mạng viễn thông. |
| ↳ `isp_ids` | string[] | Danh sách ID nhà cung cấp dịch vụ Internet. |
| ↳ `device_price_ranges` | number[] | Khoảng giá thiết bị. |
| ↳ `targeting_expansion` | object | Cấu hình mở rộng nhắm mục tiêu. |
| ↳↳ `expansion_enabled` | boolean | Trạng thái bật mở rộng nhắm mục tiêu. |
| ↳↳ `expansion_types` | string[] | Danh sách loại đối tượng được mở rộng (`AGE`, `GENDER`, `INTEREST_AND_BEHAVIOR`, `TARGETING_AUDIENCE`). |
| ↳ `contextual_tag_ids` | string[] | Danh sách ID thẻ ngữ cảnh nội dung. |
| ↳ `brand_safety_type` | string | Cấp độ an toàn thương hiệu (`EXPANDED_INVENTORY`, `STANDARD_INVENTORY`, `LIMITED_INVENTORY`, `THIRD_PARTY`). |
| ↳ `brand_safety_partner` | string | Đối tác an toàn thương hiệu bên thứ ba (`IAS`, `OPEN_SLATE`, `ZEFR`). |
| ↳ `inventory_filter_enabled` | boolean | Cho biết bộ lọc kho nội dung an toàn thương hiệu có được kích hoạt hay không. |
| ↳ `category_exclusion_ids` | string[] | Danh mục nội dung nhạy cảm bị loại trừ. |
| ↳ `vertical_sensitivity_id` | string | Mức độ nhạy cảm ngành nghề dọc. |
| ↳ `budget_mode` | string | Chế độ ngân sách (`BUDGET_MODE_DAY`, `BUDGET_MODE_TOTAL`). |
| ↳ `budget` | float | Ngân sách nhóm quảng cáo. |
| ↳ `scheduled_budget` | float | Ngân sách theo lịch trình đã lên kế hoạch. |
| ↳ `schedule_type` | string | Loại lịch chạy (`SCHEDULE_START_END`, `SCHEDULE_FROM_NOW`). |
| ↳ `schedule_start_time` | datetime | Thời điểm bắt đầu chạy quảng cáo (UTC+0). |
| ↳ `schedule_end_time` | datetime | Thời điểm kết thúc chạy quảng cáo (UTC+0). |
| ↳ `delivery_mode` | string | Chế độ phân phối của nhóm quảng cáo. |
| ↳ `dayparting` | string | Chuỗi 336 ký tự phân phối theo khung giờ trong tuần. |
| ↳ `optimization_goal` | string | Mục tiêu tối ưu hóa được thiết lập cho nhóm quảng cáo. |
| ↳ `secondary_optimization_event` | string | Mục tiêu tối ưu hóa thứ cấp. |
| ↳ `message_event_set_id` | string | ID bộ sự kiện tin nhắn. |
| ↳ `frequency` | number | Số lần hiển thị giới hạn theo tần suất. |
| ↳ `frequency_schedule` | number | Chu kỳ ngày giới hạn tần suất. |
| ↳ `bid_type` | string | Chiến lược đặt giá thầu (`BID_TYPE_CUSTOM`, `BID_TYPE_NO_BID`, `BID_TYPE_LOWEST_COST`). |
| ↳ `bid_price` | float | Mức giá thầu thủ công đã cấu hình. |
| ↳ `conversion_bid_price` | float | Giá thầu mục tiêu CPA. |
| ↳ `deep_bid_type` | string | Chiến lược giá thầu sự kiện trong ứng dụng (`DEFAULT`, `VO_MIN_ROAS`, `VO_HIGHEST_VALUE`). |
| ↳ `roas_bid` | float | Mục tiêu ROAS tối thiểu cho VBO. |
| ↳ `vbo_window` | string | Cửa sổ thời gian áp dụng VBO (`SEVEN_DAYS`, `ONE_DAY`, `ZERO_DAY`). |
| ↳ `bid_display_mode` | string | Chế độ hiển thị giá thầu (`CPV`). |
| ↳ `deep_cpa_bid` | float | Mức giá thầu CPA cho sự kiện phễu sâu. |
| ↳ `cpv_video_duration` | string | Thời lượng video tính cho lượt xem CPV (`SIX_SECONDS`, `TWO_SECONDS`). |
| ↳ `next_day_retention` | float | Tỷ lệ giữ chân người dùng ngày tiếp theo mục tiêu. |
| ↳ `click_attribution_window` | string | Cửa sổ phân bổ lượt nhấp (`OFF`, `ONE_DAY`, `SEVEN_DAYS`, `FOURTEEN_DAYS`, `TWENTY_EIGHT_DAYS`). |
| ↳ `engaged_view_attribution_window` | string | Cửa sổ phân bổ lượt xem có tương tác (`OFF`, `ONE_DAY`, `SEVEN_DAYS`). |
| ↳ `view_attribution_window` | string | Cửa sổ phân bổ lượt xem qua (`OFF`, `ONE_DAY`, `SEVEN_DAYS`). |
| ↳ `attribution_event_count` | string | Kiểu đếm sự kiện phân bổ (`EVERY`, `ONCE`). |
| ↳ `billing_event` | string | Sự kiện tính phí quảng cáo (`CPC`, `CPM`, `CPV`, `OCPM`). |
| ↳ `pacing` | string | Tốc độ chi tiêu (`PACING_MODE_SMOOTH`, `PACING_MODE_FAST`). |
| ↳ `operation_status` | string | Trạng thái vận hành (`ENABLE`, `DISABLE`). |
| ↳ `secondary_status` | string | Trạng thái phụ phản ánh lý do không phân phối (nếu có). |
| ↳ `statistic_type` | string | Kiểu thống kê giá thầu chuyển đổi (`EVERYTIME`, `NONE`). |
| ↳ `is_hfss` | boolean | Cờ đánh dấu sản phẩm HFSS. |
| ↳ `is_lhf_compliance` | boolean | Cờ tuân thủ quy định LHF. |
| ↳ `creative_material_mode` | string | Chế độ tài liệu sáng tạo (`CUSTOM`). |
| ↳ `adgroup_app_profile_page_state` | string | Trạng thái Trang hồ sơ ứng dụng (`ON`, `OFF`). |
| ↳ `rf_purchased_type` | string | Loại mua tiếp cận và tần suất (Reach & Frequency). |
| ↳ `purchased_impression` | number | Số lượt hiển thị đã mua trước cho nhóm R&F. |
| ↳ `purchased_reach` | number | Lượng tiếp cận đã mua trước cho nhóm R&F. |
| ↳ `rf_estimated_cpr` | number | Chi phí ước tính trên mỗi lượt tiếp cận (Cost per Reach) cho nhóm R&F. |
| ↳ `rf_estimated_frequency` | number | Tần suất hiển thị ước tính cho nhóm R&F. |
| ↳ `is_new_structure` | boolean | Cho biết nhóm quảng cáo có sử dụng cấu trúc chiến dịch mới hay không. |
| ↳ `skip_learning_phase` | boolean | Cho biết nhóm quảng cáo có bỏ qua giai đoạn máy học (learning phase) hay không. |
| ↳ `conversion_window` | string | *(Đã ngừng hỗ trợ - deprecated)*. Khung thời gian chuyển đổi cũ. |
| ↳ `page_info` | object | Thông tin phân trang (nếu có). |
| ↳↳ `page` | number | Trang dữ liệu hiện tại. |
| ↳↳ `page_size` | number | Số lượng bản ghi mỗi trang. |
| ↳↳ `total_number` | number | Tổng số lượng bản ghi thỏa mãn điều kiện. |
| ↳↳ `total_page` | number | Tổng số trang dữ liệu. |

### Ví dụ phản hồi

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20241023150000030111222333444555",
  "data": {
    "adgroup_id": "1712345678901235",
    "adgroup_name": "Nhóm quảng cáo chuyển đổi mùa thu",
    "advertiser_id": "6789012345678901234",
    "campaign_id": "1712345678901234",
    "campaign_name": "Chiến dịch bán hàng mùa thu",
    "create_time": "2024-10-23 15:00:00",
    "modify_time": "2024-10-23 15:00:00",
    "budget": 50.0,
    "budget_mode": "BUDGET_MODE_DAY",
    "schedule_type": "SCHEDULE_START_END",
    "schedule_start_time": "2024-11-01 00:00:00",
    "schedule_end_time": "2024-11-30 23:59:59",
    "optimization_goal": "CONVERT",
    "billing_event": "OCPM",
    "bid_type": "BID_TYPE_NO_BID",
    "pacing": "PACING_MODE_SMOOTH",
    "operation_status": "ENABLE",
    "placement_type": "PLACEMENT_TYPE_NORMAL",
    "placements": [
      "PLACEMENT_TIKTOK"
    ],
    "location_ids": [
      "6252001"
    ],
    "gender": "GENDER_UNLIMITED",
    "operating_systems": [
      "ANDROID",
      "IOS"
    ],
    "pixel_id": "C1234567890ABCDEF",
    "optimization_event": "COMPLETE_PAYMENT",
    "click_attribution_window": "SEVEN_DAYS",
    "engaged_view_attribution_window": "ONE_DAY",
    "view_attribution_window": "ONE_DAY",
    "attribution_event_count": "EVERY",
    "comment_disabled": false,
    "video_download_disabled": false,
    "share_disabled": false,
    "is_hfss": false,
    "is_lhf_compliance": false,
    "skip_learning_phase": false,
    "is_new_structure": true
  }
}
```
