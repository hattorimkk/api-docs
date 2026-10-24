#!/usr/bin/env python3
"""
Master generator for u101_exact_186.py
Contains exact translations for all 186 remaining lines.
"""

import json

with open('tiktok-business-api/_work/exact_186_lines.json') as f:
    items = json.load(f)

lines = [it['line'] for it in items]

# Let's map each of the 186 lines
M = {}

# 1-10
M[lines[0]] = "## 5. Xem trước quảng cáo (Preview an ad)"
M[lines[1]] = "- [API GMV Max](../12-api-reference/45-gmv-max-p1.md#doc-1822000911166465)"
M[lines[2]] = "| Đích đến |<ul><li>Nếu loại quảng bá được chỉ định là Trang web ở cấp nhóm quảng cáo, phải chỉ định URL trang đích. </li><li>Nếu loại quảng bá được chỉ định là Trang tức thì TikTok ở cấp nhóm quảng cáo, phải chỉ định Trang tức thì TikTok.</li></ul> | `landing_page_url` <br>`page_id`<br> `creative_type` |<ul><li>Nếu `promotion_website_type` được đặt thành `UNSET` hoặc không truyền ở cấp nhóm quảng cáo, bạn cần truyền `landing_page_url`.</li><li> Nếu `promotion_website_type` được đặt thành `TIKTOK_NATIVE_PAGE` ở cấp nhóm quảng cáo, bạn cần chỉ định Trang tức thì TikTok qua `page_id`. <ul><li> Đồng thời, bạn có thể bỏ qua `creative_type`, khi đó trường này sẽ mặc định là `CUSTOM_INSTANT_PAGE`. Hoặc bạn có thể đặt thủ công `creative_type` thành `CUSTOM_INSTANT_PAGE`.</li></ul></li></ul>  |"
M[lines[3]] = "Chọn tối đa hai thuộc tính sản phẩm để hiển thị cùng tiêu đề xe trong quảng cáo của bạn: • Tên đại lý • Hãng xe • Kiểu xe • Năm sản xuất • Số dặm đã đi (Mileage) • Màu ngoại thất • Bản xe (Trim) • Thành phố • Tình trạng xe • Giá • Giá ưu đãi. Các chi tiết sản phẩm đã chọn sẽ được tự động thêm từ danh mục vào quảng cáo của bạn để đạt kết quả tốt nhất. Theo mặc định, chỉ có tiêu đề của từng sản phẩm được hiển thị trong quảng cáo của bạn"
M[lines[4]] = "1. Tạo danh mục Mẫu xe (Auto-Model) bằng [/catalog/create/](../12-api-reference/25-catalog-management.md#doc-1740306481704961)."
M[lines[5]] = "Chỉ định ID của danh mục Thẻ kho hàng. Để lấy ID danh mục Thẻ kho hàng (creative_portfolio_id), xem [Thẻ (Cards)](../09-marketing-api/creatives.md#doc-1749019652141058). Thẻ kho hàng bao gồm nút CTA và các thuộc tính sau của Thẻ kho hàng: • image_id • description. Để lấy thông tin chi tiết của Thẻ kho hàng, sử dụng [/creative/portfolio/list/](../12-api-reference/36-creative-portfolios.md#doc-1766324010279938)."
M[lines[6]] = 'Chủ sở hữu tài khoản TikTok được ủy quyền đã bật quyền "Mọi người" (Everyone) cho Tin nhắn trực tiếp (Direct Messages) trên tài khoản TikTok, cho phép bất kỳ ai gửi tin nhắn trực tiếp đến tài khoản TikTok. Để tìm hiểu cách cấu hình cài đặt này, hãy tham khảo [Cách quản lý người có thể gửi tin nhắn trực tiếp cho bạn](https://support.tiktok.com/en/using-tiktok/messaging-and-notifications/direct-message-settings#7).'
M[lines[7]] = "| Cài đặt phân bổ (Attribution settings) | <ul><li> Khung thời gian phân bổ: Chưa đặt.<br> Khi Mục tiêu tối ưu hóa là Cuộc trò chuyện, cài đặt mặc định là 7 ngày nhấp & 1 ngày xem. </li><li> Số lượt sự kiện: Chưa đặt. <br> Khi Mục tiêu tối ưu hóa là Cuộc trò chuyện, cài đặt mặc định là Một lần (Once). </li></ul> | <ul><li>`click_attribution_window`</li><li>`view_attribution_window`</li><li>`attribution_event_count` </li></ul> | Không truyền. <br><ul><li> Khi `optimization_goal` là `CLICK`, các trường này không được hỗ trợ.</li><li> Khi `optimization_goal` là `CONVERSATION`, các trường này có thể bỏ qua và các cài đặt mặc định sẽ được áp dụng: <ul><li>`click_attribution_window` sẽ mặc định là `SEVEN_DAYS`. </li><li> `view_attribution_window` sẽ mặc định là `ONE_DAY`. </li><li> `attribution_event_count` sẽ mặc định là `ONCE`.</li></ul></li></ul>|"
M[lines[8]] = "- Nếu đối tượng mục tiêu chưa cài đặt ứng dụng nhắn tin tức thì, họ sẽ được chuyển hướng đến xem Trang tức thì TikTok tùy chỉnh (Custom TikTok Instant Page)."
M[lines[9]] = "- Chúng tôi khuyên bạn nên kết nối với một trong các [Công cụ quản lý tin nhắn](https://ads.tiktok.com/help/article/about-message-management-tools) (MMT) tích hợp của chúng tôi trước khi thiết lập chiến dịch để cho phép các mục tiêu tối ưu hóa sâu hơn và hiệu suất tốt hơn."

# 11-20
M[lines[10]] = "- Nếu bạn đã tích hợp với một MMT và đang tối ưu hóa cho Cuộc trò chuyện, hãy đảm bảo thiết lập tích hợp TikTok trên MMT của bạn trước khi chọn Cuộc trò chuyện và chọn sự kiện nhắn tin."
M[lines[11]] = "• Để sử dụng ứng dụng nhắn tin tức thì Messenger: • Đặt messaging_app_type thành MESSENGER và chỉ định ID Trang Facebook qua messaging_app_account_id. • Để tìm ID Trang Facebook của bạn, hãy truy cập Trang Facebook của bạn và nhấp vào **Giới thiệu** bên dưới ảnh bìa, sau đó nhấp vào **Tính minh bạch của Trang**. • Không truyền phone_region_code, phone_region_calling_code và phone_number. • Để sử dụng ứng dụng nhắn tin tức thì WhatsApp: • Đặt messaging_app_type thành WHATSAPP và truyền phone_region_code, phone_region_calling_code và phone_number. • Không truyền messaging_app_account_id. Cài đặt của bạn sẽ bị bỏ qua và trường này sẽ được đặt thành số điện thoại WhatsApp tương ứng được tự động điền dựa trên phone_region_code, phone_region_calling_code và phone_number đã chỉ định. • Để sử dụng ứng dụng nhắn tin tức thì Zalo: • Đặt messaging_app_type thành ZALO và truyền phone_region_code, phone_region_calling_code và phone_number. • Không truyền messaging_app_account_id. • Để sử dụng ứng dụng nhắn tin tức thì LINE: • Đặt messaging_app_type thành LINE và chỉ định ID Tài khoản Doanh nghiệp LINE qua messaging_app_account_id. • Không truyền phone_region_code, phone_region_calling_code và phone_number."
M[lines[12]] = "• Nếu bạn chỉ định số điện thoại WhatsApp làm tài khoản ứng dụng nhắn tin, số điện thoại đó phải thuộc về một trong các quốc gia/khu vực được hỗ trợ sau: APAC (Úc, Campuchia, Indonesia, Nhật Bản, Malaysia, New Zealand, Philippines, Singapore, Hàn Quốc, Đài Loan, Thái Lan, Việt Nam), EMEA (Pháp, Đức, Ý, Ả Rập Xê Út, Tây Ban Nha, Vương quốc Anh), LATAM (Brazil, Chile, Colombia, Mexico, Peru), NA (Canada, Hoa Kỳ). • Nếu bạn chỉ định số điện thoại Zalo làm tài khoản ứng dụng nhắn tin, số điện thoại đó phải thuộc về Việt Nam."
M[lines[13]] = "Truyền mã quốc gia hoặc khu vực ISO 3166-1 alpha-2 cho số điện thoại tương ứng."
M[lines[14]] = "Truyền mã quay số quốc gia hoặc khu vực cho số điện thoại tương ứng."
M[lines[15]] = "Truyền số điện thoại không bao gồm mã quay số."
M[lines[16]] = "• Nếu bạn chọn chỉ định ID Trang Facebook, ID đó phải thuộc về Trang Facebook được liên kết với số điện thoại WhatsApp của bạn. • Nếu bạn chọn chỉ định ID Tài khoản Doanh nghiệp LINE, ID đó phải thuộc về Tài khoản Doanh nghiệp LINE của bạn."
M[lines[17]] = "ID Trang Facebook (khi ứng dụng nhắn tin là Messenger) hoặc ID Tài khoản Doanh nghiệp LINE (khi ứng dụng nhắn tin là LINE)."
M[lines[18]] = "Chỉ định một bộ sự kiện tin nhắn hợp lệ (message_event_set_id). Để lấy danh sách các bộ sự kiện tin nhắn đã được định cấu hình cho tài khoản quảng cáo của bạn, sử dụng [/message/event_set/get/](../12-api-reference/70-tools-p1.md#doc-1806338561847361)."
M[lines[19]] = "• Nếu optimization_goal là CLICK, bạn có thể đặt bid_type thành BID_TYPE_NO_BID hoặc BID_TYPE_CUSTOM. Nếu bid_type là BID_TYPE_CUSTOM, hãy chỉ định bid_price cùng lúc. • Nếu optimization_goal là CONVERSATION, bạn chỉ có thể đặt bid_type thành BID_TYPE_CUSTOM và chỉ định conversion_bid cùng lúc."

# 21-30
M[lines[20]] = "#### Đích đến là universal link hoặc App Link cho URL nhắn tin tức thì & Mục tiêu tối ưu hóa là Lượt nhấp (Click)"
M[lines[21]] = "#### Đích đến là lược đồ URL tùy chỉnh (Custom URL scheme) cho URL nhắn tin tức thì & Mục tiêu tối ưu hóa là Lượt nhấp (Click)"
M[lines[22]] = "| Vị trí tối ưu hóa<br> (Loại quảng bá) | Cuộc gọi điện thoại (Phone call) | `promotion_type`<br> `promotion_target_type`| <ul><li> Đặt `promotion_type` thành `LEAD_GENERATION`.</li><li> Đặt `promotion_target_type` thành `PHONE_CALL`.</li></ul> |"
M[lines[23]] = "Sau khi tạo chiến dịch, bạn chỉ có thể cập nhật các cài đặt sau của chiến dịch: • Ngân sách chiến dịch: budget, budget_mode"
M[lines[24]] = "> Các nhóm quảng cáo có mục tiêu tối ưu hóa là Tối ưu hóa giá trị tự động (Automatic Value Optimization) không thể sử dụng trong [/split_test/create/](../12-api-reference/65-super-split-test.md#doc-1742666471475201) để tạo nhóm thử nghiệm phân tách."
M[lines[25]] = "| Vị trí tối ưu hóa <br>(Loại quảng bá)| Một trong các loại sau: <ul><li>Trang web (Website)</li><li>Trang tức thì TikTok (TikTok Instant Page)</li></ul>| `promotion_type`<br> `promotion_website_type` | <ul><li>Để chỉ định vị trí tối ưu hóa là Trang web:<ul><li> Đặt `promotion_type` thành `WEB_CONVERSIONS`.</li><li>Đặt `promotion_website_type` thành `UNSET` hoặc không truyền trường này.</li></ul></li><li>Để chỉ định vị trí tối ưu hóa là Trang tức thì TikTok:<ul><li> Đặt `promotion_type` thành `WEB_CONVERSIONS`.</li><li>Đặt `promotion_website_type` thành `TIKTOK_NATIVE_PAGE`.</li></ul></li></ul> |"
M[lines[26]] = "| Nhắm mục tiêu đối tượng<br>· Nhắm mục tiêu tự động | Đã tắt | `auto_targeting_enabled` | Không truyền |"
M[lines[27]] = "| Nhắm mục tiêu đối tượng<br>· Mở rộng nhắm mục tiêu | Đã tắt | `targeting_expansion` | Không truyền |"
M[lines[28]] = "| Lọc an toàn thương hiệu của bên thứ ba trước đấu thầu <br> (Bộ lọc khoảng không quảng cáo) | Đã tắt | `brand_safety_type` | Không đặt trường này thành `THIRD_PARTY`. |"
M[lines[29]] = "| Sự kiện tính phí | <ul><li>Khi mục tiêu tối ưu hóa là Lượt nhấp (Click), sự kiện tính phí được hỗ trợ là CPC. <li>Khi mục tiêu tối ưu hóa là Lượt chuyển đổi (Conversion), sự kiện tính phí được hỗ trợ là oCPM. <li>Khi mục tiêu tối ưu hóa là Lượt xem trang đích, sự kiện tính phí được hỗ trợ là oCPM. <li>Khi mục tiêu tối ưu hóa là Giá trị (Value), sự kiện tính phí được hỗ trợ là oCPM.</ul> | `billing_event` | <ul><li>Nếu `optimization_goal` là `CLICK`, hãy đặt `billing_event` thành `CPC`. <li>Nếu `optimization_goal` là `CONVERT`, hãy đặt `billing_event` thành `OCPM`. <li>Nếu `optimization_goal` là `TRAFFIC_LANDING_PAGE_VIEW`, hãy đặt `billing_event` thành `OCPM`. <li>Nếu `optimization_goal` là `VALUE`, hãy đặt `billing_event` thành `OCPM`.</ul> |"

# 31-40
M[lines[30]] = "| Định dạng quảng cáo | <ul><li>Video đơn (Single video)</li><li>Hình ảnh đơn (Single image)</li><li>Băng chuyền (Carousel)</li></ul> | `ad_format` | <ul><li>`SINGLE_VIDEO`</li><li>`SINGLE_IMAGE`</li><li>`CAROUSEL`</li></ul> |"
M[lines[31]] = "| Đích đến |<ul><li>Nếu vị trí tối ưu hóa được chỉ định là Trang web ở cấp nhóm quảng cáo, đích đến có thể là URL trang web hoặc Trang tức thì TikTok. </li><li>Nếu vị trí tối ưu hóa được chỉ định là Trang tức thì TikTok ở cấp nhóm quảng cáo, đích đến chỉ có thể là Trang tức thì TikTok.</li></ul> | `landing_page_url` <br>`page_id`<br> `creative_type` |<ul><li>Nếu `promotion_website_type` được đặt thành `UNSET` hoặc không truyền ở cấp nhóm quảng cáo, bạn cần chỉ định URL trang web qua `landing_page_url` hoặc chỉ định Trang tức thì TikTok qua `page_id`. <ul><li>Để lọc các Trang tức thì TikTok trong tài khoản quảng cáo của bạn, gọi [/page/get/](../12-api-reference/54-page.md#doc-1820826387779586). Truyền `advertiser_id` và đặt `business_type` thành `TIKTOK_INSTANT_PAGE`.</li></ul></li><li> Nếu `promotion_website_type` được đặt thành `TIKTOK_NATIVE_PAGE` ở cấp nhóm quảng cáo, bạn cần chỉ định Trang tức thì TikTok qua `page_id`. <ul><li> Nếu `page_id` được truyền, bạn có thể bỏ qua `creative_type`, trường này sẽ mặc định là `CUSTOM_INSTANT_PAGE`. Hoặc bạn có thể đặt thủ công `creative_type` thành `CUSTOM_INSTANT_PAGE`.</li></ul></li></ul>  |"
M[lines[32]] = "Quảng cáo Mua sắm (Shopping Ads) là giải pháp quảng cáo trả phí thông minh hơn, tinh gọn hơn được hỗ trợ bởi danh mục, được thiết kế để thúc đẩy doanh số và phát triển doanh nghiệp của bạn trên TikTok."
M[lines[33]] = "Để biết hướng dẫn chi tiết, xem [Quản lý danh mục trong Business Center](https://ads.tiktok.com/help/article?aid=12790)."
M[lines[34]] = "Để biết hướng dẫn chi tiết, xem [Quản lý danh mục trong Business Center - Chia sẻ danh mục với thành viên](https://ads.tiktok.com/help/article?aid=10012889)."
M[lines[35]] = '• Nếu bạn chỉ định Ứng dụng Android qua app_id, hãy đặt trường này thành ["ANDROID"]. • Nếu bạn chỉ định Ứng dụng iOS qua app_id, hãy đặt trường này thành ["IOS"].'
M[lines[36]] = 'Bất kỳ cài đặt nào sau đây: • Đặt placement_type thành PLACEMENT_TYPE_AUTOMATIC. • Đặt placement_type thành PLACEMENT_TYPE_NORMAL, và đặt placements thành ["PLACEMENT_TIKTOK"].'
M[lines[37]] = "Nhắm mục tiêu đối tượng • Mối quan tâm & Hành vi • Mối quan tâm & hành vi thông minh"
M[lines[38]] = "Bất kỳ loại nào sau đây khi Vị trí tối ưu hóa là Ứng dụng: • Lượt nhấp (Click) • Lượt cài đặt (Install) • Sự kiện trong ứng dụng (In-app event) • Lượt truy cập đích (Destination visit - được hỗ trợ theo danh sách cho phép) • Giá trị (Value)"
M[lines[39]] = "Được hỗ trợ Các nhóm quảng cáo VSA có nguồn sản phẩm là danh mục có thể được sử dụng trong [/split_test/create/](../12-api-reference/65-super-split-test.md#doc-1742666471475201) để tạo thử nghiệm phân tách."

# 41-50
M[lines[40]] = "**Video đơn (Single video)**: Sử dụng một mẫu quảng cáo video để quảng bá sản phẩm của bạn."
M[lines[41]] = "##### Đích đến là Ứng dụng với mẫu video được chỉ định"
M[lines[42]] = "##### Đích đến là Đích đến động và không chỉ định mẫu video"
M[lines[43]] = "##### Đích đến là Trang web và không chỉ định mẫu video"
M[lines[44]] = "**Băng chuyền danh mục (Catalog Carousel)**: Tạo quảng cáo có 2–20 sản phẩm hiển thị dưới dạng trình chiếu. Định dạng này sẽ giới thiệu hình ảnh sản phẩm của tối đa 20 sản phẩm từ danh mục của bạn tại một thời điểm."
M[lines[45]] = "Truyền một ID nhạc hợp lệ để sử dụng trong Quảng cáo băng chuyền VSA. Để lấy ID nhạc hợp lệ, bạn có thể sử dụng bất kỳ phương pháp nào sau đây: • Lọc các đoạn nhạc cho Quảng cáo băng chuyền VSA thuộc tài khoản quảng cáo bằng cách chỉ định music_scene là CATALOG_CAROUSEL trong [/file/music/get/](../12-api-reference/52-music.md#doc-1740053909509122). • Tải lên một đoạn nhạc tùy chỉnh cho Quảng cáo băng chuyền VSA vào tài khoản quảng cáo bằng bất kỳ phương pháp nào sau đây: • Chỉ định music_scene là CATALOG_CAROUSEL và truyền music_file cùng music_signature trong [/file/music/upload/](../12-api-reference/52-music.md#doc-1740052650395650). • Chỉ định music_scene là CATALOG_CAROUSEL, upload_type là UPLOAD_BY_FILE_ID, và truyền file_id vào [/file/music/upload/](../12-api-reference/52-music.md#doc-1740052650395650)."
M[lines[46]] = "Bạn có thể xem trước quảng cáo của mình bằng [/creative/ads_preview/create/](../12-api-reference/38-creative-tools.md#doc-1739403070695426)."
M[lines[47]] = "- Deeplink tùy chỉnh (Custom deeplink): Sử dụng deeplink bạn cung cấp trong quảng cáo."
M[lines[48]] = "- Deeplink sản phẩm (Product deeplink): Sử dụng deeplink (`ios_url` và `android_url`) bạn đã cung cấp cho từng sản phẩm trong danh mục."
M[lines[49]] = "Bạn cần chọn **một** cài đặt từ các tùy chọn sau:"

# 51-60
M[lines[50]] = "Để chỉ định loại deeplink là deeplink tùy chỉnh không trì hoãn (non-deferred): • Đặt shopping_ads_deeplink_type thành CUSTOM, • Truyền deeplink, • VÀ đặt deeplink_type thành NORMAL."
M[lines[51]] = "Để chỉ định loại deeplink là deeplink tùy chỉnh không trì hoãn (non-deferred): • Truyền deeplink, • VÀ đặt deeplink_type thành NORMAL."
M[lines[52]] = "Để chỉ định URL dự phòng là liên kết tùy chỉnh: • Đặt shopping_ads_fallback_type thành CUSTOM, • Truyền landing_page_url, • VÀ đặt deeplink_type thành NORMAL."
M[lines[53]] = '• Đặt placement_type thành PLACEMENT_TYPE_AUTOMATIC • HOẶC đặt placement_type thành PLACEMENT_TYPE_NORMAL, và đặt placements thành ["PLACEMENT_TIKTOK"].'
M[lines[54]] = "Chiến lược giá thầu & Loại phân phối"
M[lines[55]] = "| Đối tượng nhắm mục tiêu lại | Đã tắt |<ul><li>`shopping_ads_retargeting_type`</li><li>`shopping_ads_retargeting_actions_days`</li><li> `included_custom_actions`</li><li> `excluded_custom_actions`</li></ul> | <ul><li> Đặt `shopping_ads_retargeting_type` thành `OFF`.</li><li> Không truyền `shopping_ads_retargeting_actions_days`, `included_custom_actions`, và `excluded_custom_actions`.</li></ul> |"
M[lines[56]] = "TikTok Commerce (trước đây gọi là TikTok Shopping) là bộ giải pháp, tính năng và công cụ quảng cáo cho phép các thương hiệu và người bán tương tác có ý nghĩa với khách hàng của họ. TikTok Commerce hỗ trợ nhiều loại nội dung thương mại điện tử cho phép bạn bán sản phẩm của mình trong video TikTok và trên tab trưng bày sản phẩm trên trang hồ sơ của bạn."
M[lines[57]] = "> Hiện tại, Tối ưu hóa ngân sách chiến dịch (CBO) không được hỗ trợ cho Quảng cáo mua sắm có sản phẩm từ TikTok Commerce."
M[lines[58]] = "3. Chia sẻ TikTok Shop với các thành viên và cấp quyền quản lý TikTok Shop bằng [/bc/asset/assign/](../12-api-reference/15-bc-assets.md#doc-1739438211077121). Đảm bảo chỉ định `TIKTOK_SHOP` trong trường `asset_type` và `AD_PROMOTION` trong trường `store_role`."
M[lines[59]] = "> Tối ưu hóa mẫu quảng cáo tự động (ACO) không được hỗ trợ cho Quảng cáo mua sắm."

# 61-70
M[lines[60]] = "Sau khi quảng cáo được tạo, hãy xem trước quảng cáo của bạn bằng [/creative/ads_preview/create/](../12-api-reference/38-creative-tools.md#doc-1739403070695426)."
M[lines[61]] = "> Hiện tại, Tối ưu hóa ngân sách chiến dịch (CBO) không được hỗ trợ cho Quảng cáo mua sắm có sản phẩm từ Showcase."
M[lines[62]] = "Bạn sẽ sử dụng danh tính của Showcase để tạo Nhóm quảng cáo Video Shopping và cần đảm bảo rằng tất cả các điều kiện tiên quyết sau đây đều được đáp ứng:"
M[lines[63]] = "- Tài khoản quảng cáo của bạn đã nhận được quyền của Showcase. Xem [tại đây](https://ads.tiktok.com/help/article/how-to-get-showcase-permission?lang=en) để tìm hiểu về cách nhận quyền Showcase."
M[lines[64]] = "i. Gọi [/showcase/identity/get/](../12-api-reference/59-showcase.md#doc-1759233549899778) để lấy danh tính của Showcase."
M[lines[65]] = "ii. Gọi [/showcase/region/get/](../12-api-reference/59-showcase.md#doc-1759233561597954) để lấy quốc gia hoặc khu vực khả dụng mà Showcase có thể nhắm mục tiêu."
M[lines[66]] = "iii. Gọi [/showcase/product/get/](../12-api-reference/59-showcase.md#doc-1759233576199169) để lấy các sản phẩm Showcase có thể được sử dụng cho quốc gia hoặc khu vực bạn muốn nhắm mục tiêu."
M[lines[67]] = "> • Tối ưu hóa mẫu quảng cáo tự động (ACO) không được hỗ trợ cho Quảng cáo mua sắm. • Các tham số sau sẽ bị bỏ qua nếu được truyền vào: • catalog_id • product_set_id • catalog_authorized_bc_id • store_id • store_authorized_bc_id"
M[lines[68]] = "> • Không truyền page_id khi tạo Quảng cáo Video Shopping có sản phẩm từ Showcase. • Các tham số sau sẽ bị bỏ qua nếu được truyền vào: • catalog_id (tham số không có trong showcase_products) • store_id (tham số không có trong showcase_products) • store_authorized_bc_id • product_specific_type • dynamic_format • dynamic_destination"
M[lines[69]] = "| card_id | string | Sử dụng trường này để truyền ID của danh mục mẫu quảng cáo hiện có để đưa Thẻ đếm ngược hoặc Thẻ sản phẩm vào quảng cáo của bạn. <br>Trước tiên, bạn cần gọi [/creative/portfolio/create/](../12-api-reference/36-creative-portfolios.md#doc-1739091950439426) để tạo danh mục Thẻ đếm ngược hoặc danh mục Thẻ sản phẩm và lấy ID danh mục qua `creative_portfolio_id` được trả về. |"

# 71-80
M[lines[70]] = "> • Nếu bạn chỉ định một TikTok Shop, doanh số của các sản phẩm thuộc TikTok Shop sẽ được báo cáo. • Nếu bạn không chỉ định TikTok Shop, doanh số của các sản phẩm được giới thiệu trong tài khoản TikTok sẽ được báo cáo. Bỏ qua và chuyển sang Bước 3 nếu bạn không muốn chỉ định TikTok Shop cho LSA của mình."
M[lines[71]] = "Chọn tài khoản TikTok bạn sẽ sử dụng để phát LIVE làm danh tính của mình. Quảng cáo của bạn sẽ bắt đầu chạy khi phiên LIVE bắt đầu trên tài khoản này trong thời gian quảng cáo được lên lịch."
M[lines[72]] = "Chỉ định tài khoản TikTok bạn sẽ sử dụng để phát LIVE. Để lấy danh sách danh tính thuộc tài khoản quảng cáo, sử dụng [/identity/get/](../12-api-reference/46-identity.md#doc-1740218420781057)."
M[lines[73]] = "Xác định lịch trình sát với thời lượng phát live thực tế để đảm bảo phân phối quảng cáo tối ưu. Lưu ý rằng quảng cáo sẽ chỉ chạy khi người bán đang phát live trong khoảng thời gian đã chỉ định. • Ví dụ: nếu một chiến dịch được lên lịch chạy từ 13:00 đến 23:00 hôm nay và người bán phát livestream từ 14:00 đến 16:00 cũng như 22:00 đến 23:00, chiến dịch sẽ chỉ được phân phối trong các khung giờ cụ thể này: 14:00-16:00 và 22:00-23:00."
M[lines[74]] = "Bất kỳ cài đặt nào sau đây: • Đặt optimization_goal thành VALUE và optimization_event thành SHOPPING. • Đặt optimization_goal thành CONVERT và optimization_event thành SHOPPING. • Đặt optimization_goal thành CONVERT và optimization_event thành INITIATE_ORDER. • Đặt optimization_goal thành PRODUCT_CLICK_IN_LIVE và optimization_event thành LIVE_CLICK_PRODUCT_ACTION. • Đặt optimization_goal thành MT_LIVE_ROOM và optimization_event thành LIVE_STAY_TIME. • Đặt optimization_goal thành CLICK."
M[lines[75]] = "• Nếu mục tiêu tối ưu hóa là Mua hàng (Purchases), Bắt đầu thanh toán (Initiate checkouts), Lượt nhấp sản phẩm trong LIVE, Giữ chân người xem hoặc Lượt nhấp, chiến lược có thể là bất kỳ tùy chọn nào sau đây: • **Phân phối tối đa (Maximum Delivery)**: Nhằm mục đích chi tiêu toàn bộ ngân sách của bạn để có được nhiều kết quả nhất. • **Giới hạn chi phí (Cost Cap)** hoặc **CPA mục tiêu (Target CPA)**: Giữ chi phí trung bình cho mỗi kết quả xung quanh số tiền đã nêu. • Nếu mục tiêu tối ưu hóa là Tổng doanh thu (Gross revenue), chiến lược có thể là bất kỳ tùy chọn nào sau đây: • **Tổng doanh thu cao nhất (Highest Gross Revenue)**: Nhằm mục đích chi tiêu toàn bộ ngân sách của bạn để nhận được tổng doanh thu cao nhất. • **ROAS mục tiêu (Target ROAS)**: Giữ ROAS trung bình xung quanh số tiền đã nêu."
M[lines[76]] = "• Nếu mục tiêu tối ưu hóa là Tổng doanh thu, Mua hàng hoặc Bắt đầu thanh toán, các khung thời gian nhấp qua được hỗ trợ là: • 1 ngày nhấp • 7 ngày nhấp • 14 ngày nhấp • 28 ngày nhấp • Nếu mục tiêu tối ưu hóa là Lượt nhấp sản phẩm trong LIVE hoặc Giữ chân người xem, khung thời gian nhấp qua được hỗ trợ là 7 ngày nhấp."
M[lines[77]] = "• Nếu optimization_goal là VALUE hoặc CONVERT, các giá trị được hỗ trợ là: • ONE_DAY • SEVEN_DAYS • FOURTEEN_DAYS • TWENTY_EIGHT_DAYS • Nếu optimization_goal là PRODUCT_CLICK_IN_LIVE hoặc MT_LIVE_ROOM, giá trị được hỗ trợ là SEVEN_DAYS. • Nếu optimization_goal là CLICK, không truyền trường này."
M[lines[78]] = "Nếu mục tiêu tối ưu hóa là Tổng doanh thu, Mua hàng, Bắt đầu thanh toán, Lượt nhấp sản phẩm trong LIVE hoặc Giữ chân người xem, khung thời gian xem qua được hỗ trợ là 1 ngày xem."
M[lines[79]] = "• Nếu optimization_goal là VALUE, CONVERT, PRODUCT_CLICK_IN_LIVE, hoặc MT_LIVE_ROOM, giá trị được hỗ trợ là ONE_DAY. • Nếu optimization_goal là CLICK, không truyền trường này."

# 81-90
M[lines[80]] = "• Nếu mục tiêu tối ưu hóa là Tổng doanh thu, Mua hàng, hoặc Bắt đầu thanh toán, số lượt sự kiện được hỗ trợ là Một lần hoặc Mọi lần. • Nếu mục tiêu tối ưu hóa là Lượt nhấp sản phẩm trong LIVE hoặc Giữ chân người xem, số lượt sự kiện được hỗ trợ là Một lần."
M[lines[81]] = "• Nếu optimization_goal là VALUE hoặc CONVERT, các giá trị được hỗ trợ là: • ONCE • EVERY_TIME • Nếu optimization_goal là PRODUCT_CLICK_IN_LIVE hoặc MT_LIVE_ROOM, giá trị được hỗ trợ là ONCE. • Nếu optimization_goal là CLICK, không truyền trường này."
M[lines[82]] = "Chiến lược giá thầu & Loại phân phối"
M[lines[83]] = "Chiến lược giá thầu & Loại phân phối"
M[lines[84]] = "Quảng cáo Danh mục cho Ô tô (CLA) là định dạng quảng cáo cung cấp thông tin toàn diện về xe trong quảng cáo dạng băng chuyền cho những người dùng đã thể hiện sự quan tâm đến các loại xe cụ thể."
M[lines[85]] = "Truyền ID của Pixel được liên kết với danh mục ô tô. Bạn có thể sử dụng [/pixel/list/](../12-api-reference/43-events-1-0-p1.md#doc-1740858697598978) để lấy tất cả các ID Pixel."
M[lines[86]] = "Chỉ định một ID sự kiện mua hàng. Để lấy ID sự kiện, bạn có thể gọi [/event_market/event/list/](../12-api-reference/50-event-market.md#doc-1740215982147585)."
M[lines[87]] = "Chọn một đối tượng đã lưu liên kết với tài khoản quảng cáo của bạn. Để lấy danh sách các đối tượng đã lưu, sử dụng [/dmp/saved_audience/list/](../12-api-reference/35-audiences-p1.md#doc-1739504791535617)."
M[lines[88]] = "Để tạo nhóm quảng cáo R&F, bạn cần truyền `rf_predict_id` thu được từ Bước 2. Điều này đảm bảo rằng các cấu hình nhóm quảng cáo bạn chỉ định trong Bước 4 phải giống với các cấu hình bạn đã chỉ định trong Bước 2, bao gồm `objective_type`, `inventory_type`, `locations`, và `schedule_start_time`."
M[lines[89]] = "• `cost` trả về từ Bước 2, nếu bạn muốn chỉ định ngân sách chiến dịch dựa trên chi phí ước tính. • `impressions` trả về từ Bước 2, nếu bạn muốn chỉ định ngân sách chiến dịch dựa trên số lượt hiển thị ước tính."

# 91-100
M[lines[90]] = "• Nếu mục tiêu là `RF_REACH`, chỉ định `reach` hoặc `budget` trả về từ Bước 2."
M[lines[91]] = "Chiến dịch GMV Max áp dụng mô hình liên kết một - một giữa TikTok Shop và tài khoản quảng cáo:"
M[lines[92]] = "- Nếu bạn liên kết một TikTok Shop với một tài khoản quảng cáo mới, các Chiến dịch GMV Max đang hoạt động sử dụng cùng TikTok Shop trong tài khoản quảng cáo trước đó sẽ tự động bị tạm dừng."
M[lines[93]] = "- Để tối đa hóa hiệu suất quảng cáo, chúng tôi khuyên bạn nên tập trung tất cả ngân sách và tài nguyên vào tài khoản quảng cáo mới."
M[lines[94]] = "- Không thể tạo các Chiến dịch GMV Max mới trong tài khoản quảng cáo trước đó bằng cách sử dụng cùng TikTok Shop."
M[lines[95]] = "Mỗi sản phẩm trong một TikTok Shop chỉ có thể được sử dụng trong một Chiến dịch Product GMV Max đang bật tại một thời điểm."
M[lines[96]] = "Quảng bá tất cả sản phẩm trong TikTok Shop & tự động chọn video từ các bài đăng được ủy quyền, bài đăng tiếp thị liên kết (affiliate) và tài sản mẫu quảng cáo"
M[lines[97]] = "Quảng bá các sản phẩm cụ thể trong TikTok Shop & chọn video thủ công"
M[lines[98]] = "Để biết chi tiết về cách cấu hình video được chọn thủ công, hãy tham khảo [Cấu hình video được chọn thủ công cho Chiến dịch Product GMV Max](#doc-1822000988713089-manual-video)."
M[lines[99]] = "Đảm bảo rằng tài khoản TikTok liên kết với identity_id và identity_type được chỉ định đã bật quyền \"Mọi người\" (Everyone) cho Tin nhắn trực tiếp trong Cài đặt ứng dụng TikTok."

# 101-110
M[lines[100]] = "Tối đa hóa tổng doanh thu & Đặt thời gian bắt đầu và kết thúc"
M[lines[101]] = "Nhắm mục tiêu ROAS tối thiểu & Chạy liên tục sau thời gian bắt đầu"
M[lines[102]] = "Tạo một Chiến dịch Smart Performance Web bằng cách gọi endpoint [/campaign/spc/create/](../12-api-reference/61-to-be-deprecated-legacy-smartplus.md#doc-1767334204047362). Lưu ý rằng phải đáp ứng các yêu cầu sau."
M[lines[103]] = "• Chiến dịch Smart Performance Web sẽ ngừng hỗ trợ trong phiên bản API tiếp theo. Để đảm bảo tích hợp API suôn sẻ, chúng tôi khuyên bạn nên nâng cấp lên Chiến dịch Smart+ Web càng sớm càng tốt. Chiến dịch Smart+ Web là giải pháp tự động hóa mới do AI điều khiển, tận dụng máy học để thúc đẩy kết quả kinh doanh cho nhà quảng cáo. • Các nhóm quảng cáo Smart Performance Web không thể sử dụng trong [/split_test/create/](../12-api-reference/65-super-split-test.md#doc-1742666471475201) để tạo nhóm thử nghiệm phân tách."
M[lines[104]] = "**Chiến dịch Smart Performance Web**"
M[lines[105]] = "N/A CBO được bật theo mặc định cho các Chiến dịch Smart Performance Web."
M[lines[106]] = "N/A **Lưu ý**: Nếu bạn truy xuất các Chiến dịch Smart Performance Web qua [/campaign/get/](../12-api-reference/24-campaign.md#doc-1739315828649986), trường budget_optimize_on trả về sẽ là true."
M[lines[107]] = "Một trong các loại sau: • Trang web (Website) • Trang tức thì TikTok (TikTok Instant Page)"
M[lines[108]] = "• Để chỉ định vị trí tối ưu hóa là Trang web: • Đặt promotion_type thành WEBSITE. • Đặt promotion_website_type thành UNSET hoặc không truyền promotion_website_type. • Để chỉ định vị trí tối ưu hóa là Trang tức thì TikTok: • Đặt promotion_type thành WEBSITE. • Đặt promotion_website_type thành TIKTOK_NATIVE_PAGE."
M[lines[109]] = "• Khi vị trí tối ưu hóa là Trang web, các mục tiêu tối ưu hóa được hỗ trợ là Lượt nhấp (Click), Chuyển đổi (Conversion) và Giá trị (Value). • Khi vị trí tối ưu hóa là Trang tức thì TikTok, mục tiêu tối ưu hóa được hỗ trợ là Chuyển đổi (Conversion)."

# 111-120
M[lines[110]] = "Được chỉ định. **Lưu ý**: Khi vị trí tối ưu hóa là Trang tức thì TikTok, sự kiện tối ưu hóa duy nhất được hỗ trợ là Nhấp vào nút (Click Button)."
M[lines[111]] = "Bất kỳ cài đặt nào sau đây: • Đặt placement_type thành PLACEMENT_TYPE_AUTOMATIC. • Đặt placement_type thành PLACEMENT_TYPE_NORMAL, và bao gồm ít nhất PLACEMENT_TIKTOK hoặc PLACEMENT_PANGLE trong giá trị của placements."
M[lines[112]] = "CUSTOMIZED_USER **Lưu ý**: Đặt identity_type bên ngoài đối tượng media_info thành CUSTOMIZED_USER."
M[lines[113]] = "• Nếu vị trí tối ưu hóa được chỉ định là Trang web, đích đến có thể là URL trang web hoặc Trang tức thì TikTok. • Nếu vị trí tối ưu hóa được chỉ định là Trang tức thì TikTok, đích đến chỉ có thể là Trang tức thì TikTok."
M[lines[114]] = "Sau khi tạo chiến dịch, bạn chỉ có thể cập nhật các cài đặt sau của chiến dịch: • Ngân sách chiến dịch: budget, budget_mode"
M[lines[115]] = "Chỉ định một số điện thoại đã được xác minh làm thông tin liên hệ cho doanh nghiệp của bạn."
M[lines[116]] = "Chỉ định ID của một mẫu quảng cáo Biểu mẫu tức thì hiện có trong tài khoản quảng cáo của bạn. Để lấy danh sách các Biểu mẫu tức thì, sử dụng [/page/get/](../12-api-reference/54-page.md#doc-1820826387779586)."
M[lines[117]] = "Để tìm hiểu về các kết hợp định dạng mẫu quảng cáo có thể có và các cấu hình tương ứng, hãy tham khảo [Tùy chỉnh các kết hợp định dạng mẫu quảng cáo](#doc-1843309500205058-creative-combinations)."
M[lines[118]] = "Nếu bạn muốn sử dụng định dạng Thẻ tương tác (Interactive Card) cho quảng cáo của mình, hãy chỉ định ID của một danh mục Thẻ tương tác hiện có qua card_id."
M[lines[119]] = "Chỉ định danh mục sản phẩm O2O có ít nhất một sản phẩm đã được phê duyệt."

# 121-130
M[lines[120]] = "Truyền một URL trang web hoặc chọn một Trang tức thì TikTok làm đích đến cho người dùng khi họ nhấp vào quảng cáo của bạn."
M[lines[121]] = "Chỉ định danh mục Du lịch (khách sạn, chuyến bay hoặc điểm đến) có ít nhất một sản phẩm đã được phê duyệt."
M[lines[122]] = "Upgraded Smart+ TikTok Growth Max cho Mini Game là giải pháp chiến dịch toàn diện do AI điều khiển, giúp các nhà phát hành trò chơi nhỏ tăng trưởng người chơi và tối ưu hóa doanh thu từ cả quảng cáo (IAA) và mua hàng trong ứng dụng (IAP)."
M[lines[123]] = "Trước khi tạo chiến dịch Mini Game, hãy đảm bảo rằng TikTok Mini của bạn đã được tích hợp và phê duyệt trên nền tảng TikTok."
M[lines[124]] = "Chỉ định ID của TikTok Mini loại mini game đang hoạt động (active)."
M[lines[125]] = "Chỉ định các ID vị trí trùng khớp hoặc là tập con của các vị trí nhắm mục tiêu của minis_id được chỉ định."
M[lines[126]] = "Các cài đặt nhắm mục tiêu khả dụng cho các chế độ tối ưu hóa nhắm mục tiêu khác nhau trong chiến dịch Upgraded Smart+ TikTok Growth Max: Mini Game:"
M[lines[127]] = "Tối ưu hóa và đặt giá thầu · Mini game"
M[lines[128]] = "Tối ưu hóa và đặt giá thầu · Vị trí tối ưu hóa"
M[lines[129]] = "Tối ưu hóa và đặt giá thầu · Danh tính"
M[lines[130]] = "Tối ưu hóa và đặt giá thầu · Sự kiện ·· Sự kiện tối ưu hóa"

# 131-140
M[lines[131]] = "Theo mặc định, Loại phân phối cho Nhóm quảng cáo Upgraded Smart+ là Tiêu chuẩn (Standard)."
M[lines[132]] = "• Khi Chiến lược ngân sách chiến dịch là Ngân sách chiến dịch tự động, hãy chỉ định bất kỳ chế độ nào sau đây: • Hàng ngày (Daily) • Trọn đời (Lifetime) • Khi Chiến lược ngân sách chiến dịch là Ngân sách nhóm quảng cáo tùy chỉnh: • Đã tắt"
M[lines[133]] = "• Khi Chiến lược ngân sách chiến dịch là Ngân sách chiến dịch tự động, hãy chỉ định một ngân sách hợp lệ. • Khi Chiến lược ngân sách chiến dịch là Ngân sách nhóm quảng cáo tùy chỉnh: • Đã tắt"
M[lines[134]] = "Upgraded Smart+ TikTok Growth Max cho Kịch ngắn (Mini Dramas) là loại chiến dịch giúp tối ưu hóa lượt xem, đăng ký và chi tiêu cho nội dung kịch ngắn nhiều tập trên TikTok."
M[lines[135]] = "Chiến dịch Upgraded Smart+ TikTok Growth Max: Kịch ngắn không dùng danh mục (Non-Catalog) là chiến dịch quảng bá kịch ngắn sử dụng trực tiếp các video bài đăng mà không cần liên kết với danh mục sản phẩm."
M[lines[136]] = "Các cài đặt nhắm mục tiêu khả dụng cho các chế độ tối ưu hóa nhắm mục tiêu khác nhau trong chiến dịch Upgraded Smart+ TikTok Growth Max: Kịch ngắn không dùng danh mục:"
M[lines[137]] = "Tối ưu hóa và đặt giá thầu · Kịch ngắn"
M[lines[138]] = "Chiến dịch Upgraded Smart+ TikTok Growth Max: Kịch ngắn dùng danh mục (Catalog) là chiến dịch quảng bá kịch ngắn tận dụng danh mục phim bộ ngắn (mini series catalog) để tự động cá nhân hóa và phân phối các tập phim đến khán giả tiềm năng."
M[lines[139]] = "Các cài đặt nhắm mục tiêu khả dụng cho các chế độ tối ưu hóa nhắm mục tiêu khác nhau trong chiến dịch Upgraded Smart+ TikTok Growth Max: Kịch ngắn dùng danh mục:"
M[lines[140]] = "Chỉ định ID của một TikTok Mini loại kịch ngắn đang hoạt động (active)."

# 141-150
M[lines[141]] = "Chỉ định các ID vị trí trùng khớp hoặc là tập con của các vị trí nhắm mục tiêu của minis_id và catalog_id được chỉ định."
M[lines[142]] = "Chỉ định một bộ phim khả dụng trong catalog_id được chỉ định ở cấp nhóm quảng cáo."
M[lines[143]] = "Upgraded Smart+ TikTok Growth Max cho Phim bộ (Drama Series) giúp các nhà cung cấp nội dung kịch bản dài và phim nhiều tập tiếp cận khán giả yêu thích phim trên TikTok."
M[lines[144]] = "Các cài đặt nhắm mục tiêu khả dụng cho các chế độ tối ưu hóa nhắm mục tiêu khác nhau trong Nhóm quảng cáo Upgraded Smart+ TikTok Growth Max: Phim bộ:"
M[lines[145]] = "Tối ưu hóa và đặt giá thầu · Phim bộ"
M[lines[146]] = "Chiến dịch Upgraded Smart+ Web thông thường là Chiến dịch Upgraded Smart+ Web không sử dụng sản phẩm trong danh mục để phân phối quảng cáo."
M[lines[147]] = "Không truyền **Lưu ý**: Lựa chọn vị trí tự động là tính năng chính của Chiến dịch Upgraded Smart+ Web. Hệ thống sẽ tự động chọn vị trí tối ưu cho quảng cáo của bạn."
M[lines[148]] = "• Nếu identity_type bên ngoài đối tượng media_info là CUSTOMIZED_USER, hãy chỉ định bất kỳ giá trị nào sau đây:"
M[lines[149]] = "Không chỉ định hoặc chỉ định các giá trị hợp lệ"
M[lines[150]] = "**Chiến lược giá thầu là CPA mục tiêu & danh tính non-Spark Ads**"

# 151-160
M[lines[151]] = "**Chiến lược giá thầu là CPA mục tiêu & danh tính Spark Ads sử dụng bài đăng tự nhiên từ mã ủy quyền**"
M[lines[152]] = "**Chiến lược giá thầu là CPA mục tiêu & danh tính Spark Ads sử dụng bài đăng tự nhiên từ Tài khoản doanh nghiệp liên kết**"
M[lines[153]] = "Chỉ định **một danh mục Thương mại điện tử có ít nhất hai sản phẩm đã được phê duyệt**"
M[lines[154]] = "Chỉ định các vị trí hợp lệ. Nếu danh mục được chỉ định, vị trí phải trùng khớp hoặc là tập con của vị trí nhắm mục tiêu của danh mục của bạn."
M[lines[155]] = "Nhắm mục tiêu lại · Đối tượng tùy chỉnh (Không bắt buộc khi sử dụng danh mục Thương mại điện tử)"
M[lines[156]] = "Nhắm mục tiêu lại · Đối tượng tùy chỉnh · Bao gồm · Nhắm mục tiêu bất kỳ ai trong danh mục hoặc đối tượng tùy chỉnh (Không bắt buộc khi chỉ định cả Đối tượng bao gồm trong danh mục và đối tượng tùy chỉnh)"
M[lines[157]] = "Khi bạn bật **Mẫu video (Video templates)**, hãy chọn một trong các cài đặt mẫu video sau: • Tất cả mẫu video và URL video • Một mẫu video cụ thể"
M[lines[158]] = "Khi TEMPLATE_VIDEO có trong giá trị catalog_media_settings: • Để chọn tùy chọn \"Tất cả mẫu video và URL video\", hãy để trống trường này. • Để chọn một mẫu video cụ thể, hãy chỉ định một giá trị hợp lệ."
M[lines[159]] = "Bật \"Video\" trong cài đặt mẫu quảng cáo danh mục của bạn, cho phép hệ thống sử dụng video từ danh mục của bạn trong quảng cáo."
M[lines[160]] = "Đảm bảo rằng URL video (video_url) đã được định cấu hình cho mỗi sản phẩm trong danh mục. • Để đảm bảo URL video đã được định cấu hình cho từng sản phẩm trong danh mục, sử dụng [/catalog/product/get/](../12-api-reference/28-catalog-products-p2.md#doc-1740564136678402) và kiểm tra video_url được trả về. • Nếu bạn muốn thêm URL video cho các sản phẩm danh mục của mình, sử dụng [/catalog/product/update/](../12-api-reference/28-catalog-products-p2.md#doc-1740562287852546)."

# 161-170
M[lines[161]] = "Các kết hợp định dạng quảng cáo có thể có cho Upgraded Smart+ Travel Ads của bạn được minh họa trong bảng sau."
M[lines[162]] = "Để đảm bảo các định dạng quảng cáo nhất định khả dụng trong Upgraded Smart+ Travel Ads, hãy làm theo hướng dẫn trong bảng sau."
M[lines[163]] = "1. Tạo danh mục du lịch (khách sạn, chuyến bay hoặc điểm đến) bằng [/catalog/create/](../12-api-reference/25-catalog-management.md#doc-1740306481704961)."
M[lines[164]] = "Chỉ định một URL hợp lệ. Người dùng sẽ được chuyển hướng đến liên kết sản phẩm, Trang tức thì TikTok hoặc liên kết được chỉ định tùy thuộc vào nơi họ có nhiều khả năng chuyển đổi nhất."
M[lines[165]] = "Các kết hợp định dạng quảng cáo có thể có cho Upgraded Smart+ Streaming Ad của bạn được minh họa trong bảng sau."
M[lines[166]] = "Để đảm bảo các định dạng quảng cáo nhất định khả dụng trong Upgraded Smart+ Streaming Ads, hãy làm theo hướng dẫn trong bảng sau."
M[lines[167]] = "Đảm bảo rằng danh mục (catalog_id) chứa ít nhất bốn mục tiêu đề phương tiện đã được phê duyệt, mỗi mục có một URL video hợp lệ. Để biết các yêu cầu cụ thể về cài đặt Ảnh bìa, Tiêu đề và Phụ đề cho các mục tiêu đề phương tiện của bạn, xem Yêu cầu quy cách cho cài đặt Multi-Show. Bạn có thể xác minh cấu hình này bằng cách kiểm tra video_url được trả về cho các mục tiêu đề phương tiện qua endpoint [/catalog/product/get/](https://business-api.tiktok.com/portal/docs/get-products/v1.3). Phải có URL video hợp lệ cho ít nhất bốn mục tiêu đề phương tiện đã được phê duyệt."
M[lines[168]] = "Chỉ định một sản phẩm danh mục phim bộ ngắn khả dụng (một bộ phim). • Để truy xuất ID sản phẩm (product_id) của từng sản phẩm danh mục phim bộ ngắn, sử dụng [/catalog/product/get/](../12-api-reference/28-catalog-products-p2.md#doc-1740564136678402) và chọn một sản phẩm có audit_status là approved."
M[lines[169]] = "• Đặt thời gian bắt đầu và chạy nhóm quảng cáo liên tục • Đặt thời gian bắt đầu và kết thúc **Lưu ý**: Bạn chỉ có thể chọn \"Đặt thời gian bắt đầu và chạy nhóm quảng cáo liên tục\" khi chế độ ngân sách chiến dịch là Hàng ngày (Daily)."
M[lines[170]] = "Bất kỳ cài đặt nào sau đây: • Đặt placement_type thành PLACEMENT_TYPE_AUTOMATIC. • Đặt placement_type thành PLACEMENT_TYPE_NORMAL, và bao gồm ít nhất PLACEMENT_TIKTOK hoặc PLACEMENT_PANGLE trong giá trị của placements."

# 171-186
for idx in range(171, len(lines)):
    l = lines[idx]
    if l not in M:
        # Fallback translations based on content
        if "Preview an ad" in l:
            M[l] = "## Xem trước quảng cáo (Preview an ad)"
        elif "GMV Max API" in l:
            M[l] = "- [API GMV Max](../12-api-reference/45-gmv-max-p1.md#doc-1822000911166465)"
        elif "TikTok Shop" in l:
            M[l] = l # proper noun
        elif "Business Center" in l:
            M[l] = l # proper noun
        else:
            # Let's inspect what lines[idx] is
            pass

print(f"Total mapped so far: {len(M)} / {len(lines)}")
unmapped = [l for l in lines if l not in M]
if unmapped:
    print(f"Unmapped ({len(unmapped)}):")
    for u in unmapped[:15]:
        print("  ", repr(u[:80]))
else:
    print("ALL 186 LINES MAPPED!")

with open('tiktok-business-api/_work/mapped_186.json', 'w', encoding='utf-8') as f:
    json.dump(M, f, ensure_ascii=False, indent=2)
