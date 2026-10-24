#!/usr/bin/env python3
"""
u102_dict_clauses_deep.py: Comprehensive translation rules for all remaining recurring and composite patterns in u102.
"""

DEEP_RULES = [
    # SKAN & Attribution
    (r'Phân bổ SKAN \*\((Không bắt buộc|Optional)\)\*Disabled or enableddisable_skan_campaign',
     r'| Phân bổ SKAN *(Không bắt buộc)* | Tắt hoặc bật | `disable_skan_campaign` |'),
    (r'To disable Phân bổ SKAN\.', 'Để tắt Phân bổ SKAN.'),
    (r'To enable Phân bổ SKAN\.', 'Để bật Phân bổ SKAN.'),
    (r'\*\*Note\*\*: Disabling Phân bổ SKAN for Dedicated Campaigns is currently an allowlist-only feature\.',
     '**Lưu ý**: Tắt Phân bổ SKAN cho Chiến dịch chuyên dụng hiện là tính năng chỉ dành cho danh sách cho phép (allowlist-only).'),
    (r'Disabling Phân bổ SKAN for Dedicated Campaigns is currently an allowlist-only feature\.',
     'Tắt Phân bổ SKAN cho Chiến dịch chuyên dụng hiện là tính năng chỉ dành cho danh sách cho phép (allowlist-only).'),
    (r'Disabled or enableddisable_skan_campaign', 'Tắt hoặc bật | `disable_skan_campaign` |'),

    # Viewability & Brand safety
    (r'\*\*Note\*\*: When you configure both brand_safety_postbid_partner and viewability_postbid_partner:\s*• If you set either of these two fields to IAS, you need to set both to IAS, and assign the same value \(the wrapped VAST URL that you obtain from the measurement partner IAS\) to brand_safety_vast_url and viewability_vast_url\.',
     '**Lưu ý**: Khi bạn cấu hình cả `brand_safety_postbid_partner` và `viewability_postbid_partner`: • Nếu bạn đặt một trong hai trường này thành `IAS`, bạn cần đặt cả hai thành `IAS` và gán cùng một giá trị (URL VAST được bọc nhận từ đối tác đo lường IAS) cho `brand_safety_vast_url` và `viewability_vast_url`.'),
    (r'\*\*Note\*\*: When you configure brand_safety_postbid_partner and viewability_postbid_partner:\s*• If you set either of these two fields to IAS, you need to specify both to IAS, and assign the same value \(the wrapped VAST URL that you obtain from the measurement partner IAS\) to brand_safety_vast_url and viewability_vast_url\.',
     '**Lưu ý**: Khi bạn cấu hình cả `brand_safety_postbid_partner` và `viewability_postbid_partner`: • Nếu bạn đặt một trong hai trường này thành `IAS`, bạn cần chỉ định cả hai thành `IAS` và gán cùng một giá trị (URL VAST được bọc nhận từ đối tác đo lường IAS) cho `brand_safety_vast_url` và `viewability_vast_url`.'),

    # Spark Ads & Call to action
    (r'\*\*Note\*\*: When you use a Spark Ads video creative, you cannot customize the call to action\.',
     '**Lưu ý**: Khi bạn sử dụng mẫu quảng cáo video Spark Ads, bạn không thể tùy chỉnh lời kêu gọi hành động.'),
    (r'\*\*Note\*\*: When you use a Spark Ads identity, you can only use dynamic call to action\.',
     '**Lưu ý**: Khi bạn sử dụng danh tính Spark Ads, bạn chỉ có thể sử dụng lời kêu gọi hành động động (dynamic call to action).'),
    (r'\*\*Note\*\*: If you set identity_type within the creative_info object to TT_USER, BC_AUTH_TT, or AUTH_CODE, call_to_action_id is required\.',
     '**Lưu ý**: Nếu bạn đặt `identity_type` trong đối tượng `creative_info` thành `TT_USER`, `BC_AUTH_TT` hoặc `AUTH_CODE`, thì `call_to_action_id` là bắt buộc.'),
    (r'• For Spark Ads Pull \(Kéo bài viết\) \(Kéo bài viết\), specify additional TikTok video posts via tiktok_item_id\.\s*• For Spark Ads Push \(Đẩy bài viết\) \(Đẩy bài viết\), specify additional videos via video_info and cover images via image_info\.',
     '• Đối với Spark Ads Pull (Kéo bài viết), hãy chỉ định các bài viết video TikTok bổ sung qua `tiktok_item_id`. • Đối với Spark Ads Push (Đẩy bài viết), hãy chỉ định các video bổ sung qua `video_info` và ảnh bìa qua `image_info`.'),
    (r'For Spark Ads Pull \(Kéo bài viết\) \(Kéo\), hãy chỉ định bài viết video\.',
     'Đối với Spark Ads Pull (Kéo bài viết), hãy chỉ định bài viết video.'),
    (r'For Spark Ads Push \(Đẩy bài viết\) \(Đẩy\), hãy chỉ định video kèm ảnh bìa\.',
     'Đối với Spark Ads Push (Đẩy bài viết), hãy chỉ định video kèm ảnh bìa.'),
    (r'For Spark Ads Pull \(Kéo bài viết\), specify additional TikTok video posts via tiktok_item_id\.',
     'Đối với Spark Ads Pull (Kéo bài viết), chỉ định các bài viết video TikTok bổ sung qua `tiktok_item_id`.'),
    (r'For Spark Ads Push \(Đẩy bài viết\), specify additional videos via video_info and cover images via image_info\.',
     'Đối với Spark Ads Push (Đẩy bài viết), chỉ định các video bổ sung qua `video_info` và ảnh bìa qua `image_info`.'),
    (r'one to 50 TikTok video posts through tiktok_item_id\. Do not pass video_info, image_info, and ad_text_list\.',
     'từ 1 đến 50 bài viết video TikTok qua `tiktok_item_id`. Không truyền `video_info`, `image_info` và `ad_text_list`.'),
    (r'1-50 TikTok video posts', '1-50 bài viết video TikTok'),

    # Instant Page & Destination
    (r'When at the ad group level, promotion_target_type is INSTANT_PAGE:\s*• Chỉ định một giá trị hợp lệ hoặc không chỉ định',
     'Khi ở cấp nhóm quảng cáo, `promotion_target_type` là `INSTANT_PAGE`: • Chỉ định một giá trị hợp lệ hoặc không chỉ định'),
    (r'When at the ad group level, promotion_target_type is EXTERNAL_WEBSITE:\s*• Không chỉ định',
     'Khi ở cấp nhóm quảng cáo, `promotion_target_type` là `EXTERNAL_WEBSITE`: • Không chỉ định'),
    (r'The page_list cần khớp với cùng thông tin ứng dụng nhắn tin tức thì ở cấp nhóm quảng cáo\.',
     '`page_list` cần khớp với cùng thông tin ứng dụng nhắn tin tức thì ở cấp nhóm quảng cáo.'),
    (r'To confirm Liệu page_list matches the same instant messaging app information at the ad group level, use (\[/page/get/\]\([^\)]+\)) và kiểm tra `messaging_app_type` cùng `messaging_app_account_id` được trả về\.',
     r'Để xác nhận xem `page_list` có khớp với cùng thông tin ứng dụng nhắn tin tức thì ở cấp nhóm quảng cáo hay không, sử dụng \1 và kiểm tra `messaging_app_type` cùng `messaging_app_account_id` được trả về.'),

    # Products & Services labels
    (r'\*\*Other products or services\*\*', '**Sản phẩm hoặc dịch vụ khác (Other products or services)**'),
    (r'Audience suggestions guide automatic targeting by choosing additional audience settings\. These serve as suggestions only, and delivery to those audiences is not guaranteed\.',
     'Gợi ý đối tượng hướng dẫn tính năng nhắm mục tiêu tự động bằng cách chọn các cài đặt đối tượng bổ sung. Các mục này chỉ đóng vai trò là gợi ý và không đảm bảo phân phối đến những đối tượng đó.'),
    (r'Additional charges for using the WhatsApp Business API will be collected by your MMT and passed back to Meta\.',
     'Các khoản phụ phí khi sử dụng WhatsApp Business API sẽ do MMT của bạn thu và chuyển lại cho Meta.'),
    (r'To retrieve the product ID \(product_id\) of each generic product or service, use (\[/catalog/product/get/\]\([^\)]+\))\.',
     r'Để lấy ID sản phẩm (`product_id`) của từng sản phẩm hoặc dịch vụ chung, sử dụng \1.'),

    # Bidding combos in text
    (r'When budget_optimize_on is true at the campaign level, the bid_price or conversion_bid_price, nếu được chỉ định, phải giống nhau giữa các nhóm quảng cáo trong cùng một chiến dịch\.',
     'Khi `budget_optimize_on` là `true` ở cấp chiến dịch, `bid_price` hoặc `conversion_bid_price`, nếu được chỉ định, phải giống nhau giữa các nhóm quảng cáo trong cùng một chiến dịch.'),
    (r'When budget_optimize_on is true or not specified at the campaign level, specify the same optimization_event for ad groups within the same campaign\.',
     'Khi `budget_optimize_on` là `true` hoặc không chỉ định ở cấp chiến dịch, hãy chỉ định cùng một `optimization_event` cho các nhóm quảng cáo trong cùng một chiến dịch.'),
    (r'You can only choose "Set start and end time" in any of the following scenarios:\s*• Ở cấp chiến dịch, ngân sách chiến dịch trọn đời đã được thiết lập\.\s*• At the ad group level, a lifetime ad group budget is set\.',
     'Bạn chỉ có thể chọn "Đặt thời gian bắt đầu và kết thúc" trong bất kỳ trường hợp nào sau đây: • Ở cấp chiến dịch, ngân sách chiến dịch trọn đời đã được thiết lập. • Ở cấp nhóm quảng cáo, ngân sách nhóm quảng cáo trọn đời đã được thiết lập.'),
    (r'At the ad group level, a lifetime ad group budget is set\.', 'Ở cấp nhóm quảng cáo, ngân sách nhóm quảng cáo trọn đời đã được thiết lập.'),

    # Catalog & Creative variations
    (r'If you enable auto-selection of catalog creatives \(catalog_creative_toggle is true\) in your Upgraded Smart\+ Automotive Ads, the system will automatically create ads using combinations of two possible formats: catalog carousel, and single video\.',
     'Nếu bạn bật tính năng tự động chọn mẫu quảng cáo danh mục (`catalog_creative_toggle` là `true`) trong Quảng cáo ô tô Upgraded Smart+, hệ thống sẽ tự động tạo quảng cáo bằng các tổ hợp của hai định dạng có thể: thẻ xoay vòng danh mục và video đơn lẻ.'),
    (r'To learn about how to create an danh mục Mẫu xe ô tô \(danh mục Mẫu xe ô tô \(Auto-Model catalog\)\), see Prerequisite\.',
     'Để tìm hiểu về cách tạo danh mục Mẫu xe ô tô (Auto-Model catalog), xem phần Điều kiện tiên quyết.'),
    (r'To learn about how to create an danh mục Kho xe ô tô \(danh mục Kho xe ô tô \(Auto-Inventory catalog\)\), see Prerequisite\.',
     'Để tìm hiểu về cách tạo danh mục Kho xe ô tô (Auto-Inventory catalog), xem phần Điều kiện tiên quyết.'),
    (r'Enabled with one of the following options:\s*• Search inventory \(Recommended\)\s*• Learn more\s*• Shop now\s*• Sign up\s*• Contact us\s*• Book now\s*• Read more\s*• View now\s*• Order now',
     'Bật với một trong các tùy chọn sau: • Tìm kiếm kho hàng (Search inventory - Khuyến nghị) • Tìm hiểu thêm (Learn more) • Mua ngay (Shop now) • Đăng ký (Sign up) • Liên hệ với chúng tôi (Contact us) • Đặt ngay (Book now) • Đọc thêm (Read more) • Xem ngay (View now) • Đặt hàng ngay (Order now)'),
    (r'Enabled with any of the following values:\s*• SEARCH_INVENTORY \(Recommended\)\s*• LEARN_MORE\s*• SHOP_NOW\s*• SIGN_UP\s*• CONTACT_US\s*• BOOK_NOW\s*• READ_MORE\s*• VIEW_MORE\s*• ORDER_NOW',
     'Bật với bất kỳ giá trị nào sau đây: • `SEARCH_INVENTORY` (Khuyến nghị) • `LEARN_MORE` • `SHOP_NOW` • `SIGN_UP` • `CONTACT_US` • `BOOK_NOW` • `READ_MORE` • `VIEW_MORE` • `ORDER_NOW`'),
    (r'• Khi cài đặt "Tự động chọn từ danh mục" được bật:\s*• Enabled\. Chọn ảnh cuối cùng xuất hiện trong thẻ xoay vòng để khuyến khích mọi người duyệt toàn bộ kho hàng của bạn\.\s*• Khi cài đặt "Tự động chọn từ danh mục" bị tắt:\s*• Disabled',
     '• Khi cài đặt "Tự động chọn từ danh mục" được bật: • Bật (Enabled). Chọn ảnh cuối cùng xuất hiện trong thẻ xoay vòng để khuyến khích mọi người duyệt toàn bộ kho hàng của bạn. • Khi cài đặt "Tự động chọn từ danh mục" bị tắt: • Tắt (Disabled)'),
    (r'• Khi cài đặt "Tự động chọn từ danh mục" được bật:\s*• Tắt hoặc bật \(Disabled hoặc Enabled\) with up to two product attributes to show details on your product card preview:',
     '• Khi cài đặt "Tự động chọn từ danh mục" được bật: • Tắt hoặc bật với tối đa hai thuộc tính sản phẩm để hiển thị chi tiết trên bản xem trước thẻ sản phẩm của bạn:'),
    (r'• Khi cài đặt "Tự động chọn từ danh mục" được bật:\s*• Tắt hoặc bật \(Disabled hoặc Enabled\) with up to four product attributes to display:',
     '• Khi cài đặt "Tự động chọn từ danh mục" được bật: • Tắt hoặc bật với tối đa bốn thuộc tính sản phẩm để hiển thị:'),
    (r'with up to two product attributes to show details on your product card preview:',
     'với tối đa hai thuộc tính sản phẩm để hiển thị chi tiết trên bản xem trước thẻ sản phẩm của bạn:'),
    (r'with up to four product attributes to display:', 'với tối đa bốn thuộc tính sản phẩm để hiển thị:'),
    (r'for best results\.', 'để có kết quả tốt nhất.'),
    (r'for best results', 'để có kết quả tốt nhất'),

    # Customize ad format link patterns
    (r'For detailed configuration options and requirements, see \[Customize the ad format combinations in Upgraded Smart\+ ([^\]]+)\]\(([^\)]+)\)\.',
     r'Để biết các tùy chọn cấu hình chi tiết và yêu cầu, xem [Tùy chỉnh kết hợp định dạng quảng cáo trong Upgraded Smart+ \1](\2).'),
    (r'For detailed configuration options and requirements, see \[Customize the ad format combinations for Upgraded Smart\+ ([^\]]+)\]\(([^\)]+)\)\.',
     r'Để biết các tùy chọn cấu hình chi tiết và yêu cầu, xem [Tùy chỉnh kết hợp định dạng quảng cáo cho Upgraded Smart+ \1](\2).'),
    (r'For detailed configuration options and requirements, see \[Customize the ad format combinations in ([^\]]+)\]\(([^\)]+)\)\.',
     r'Để biết các tùy chọn cấu hình chi tiết và yêu cầu, xem [Tùy chỉnh kết hợp định dạng quảng cáo trong \1](\2).'),

    # Catalog Requirements & Disabled clauses
    (r'• Disabled • Hình ảnh và video trong danh mục sẽ không được sử dụng để tự động tạo Quảng cáo danh mục được tối ưu hóa ở tất cả các định dạng cho sản phẩm của bạn\.\s*Hệ thống sẽ tự động tạo quảng cáo video đơn bằng nội dung bạn đã chỉ định\.\s*• Requirements:',
     '• Tắt (Disabled) • Hình ảnh và video trong danh mục sẽ không được sử dụng để tự động tạo Quảng cáo danh mục được tối ưu hóa ở tất cả các định dạng cho sản phẩm của bạn. Hệ thống sẽ tự động tạo quảng cáo video đơn bằng nội dung bạn đã chỉ định. • Yêu cầu:'),
    (r'• Disabled • Hình ảnh và video trong danh mục sẽ không được sử dụng để tự động tạo Quảng cáo danh mục được tối ưu hóa ở tất cả các định dạng cho sản phẩm của bạn\.\s*Hệ thống sẽ tự động tạo quảng cáo video đơn bằng nội dung bạn đã chỉ định\.\s*• Yêu cầu:',
     '• Tắt (Disabled) • Hình ảnh và video trong danh mục sẽ không được sử dụng để tự động tạo Quảng cáo danh mục được tối ưu hóa ở tất cả các định dạng cho sản phẩm của bạn. Hệ thống sẽ tự động tạo quảng cáo video đơn bằng nội dung bạn đã chỉ định. • Yêu cầu:'),

    # Deeplink & UTM rules
    (r'When deeplink_type is DEFERRED_DEEPLINK:', 'Khi `deeplink_type` là `DEFERRED_DEEPLINK`:'),
    (r'When Deferred deeplink is disabled, cài đặt này không được hỗ trợ', 'Khi Deferred deeplink bị tắt, cài đặt này không được hỗ trợ'),
    (r'When deeplink_type is DEFERRED_DEEPLINK, use any of the following configurations',
     'Khi `deeplink_type` là `DEFERRED_DEEPLINK`, hãy sử dụng bất kỳ cấu hình nào sau đây'),
    (r'A deferred deeplink sends the user to a specific page when they open your app for the first time\.',
     'Deferred deeplink sẽ chuyển hướng người dùng đến một trang cụ thể khi họ mở ứng dụng của bạn lần đầu tiên.'),
    (r'If you set deeplink to a URL that includes URL parameters, you can optionally specify deeplink_utm_params at the same time to store URL parameters used in the URL\.',
     'Nếu bạn đặt `deeplink` thành một URL đã bao gồm các tham số URL, bạn có thể tùy chọn chỉ định `deeplink_utm_params` cùng lúc để lưu trữ các tham số URL được sử dụng trong URL.'),
    (r'In such cases, you need to ensure that deeplink_utm_params exactly matches the URL parameters used\.',
     'Trong những trường hợp như vậy, bạn cần đảm bảo rằng `deeplink_utm_params` khớp chính xác với các tham số URL đã sử dụng.'),
    (r'The URL parameters will not be automatically appended to the deeplink upon ad delivery\.',
     'Các tham số URL sẽ không được tự động gắn thêm vào `deeplink` khi phân phối quảng cáo.'),

    # Flexible Attribution & Data sources
    (r'Tối ưu hóa và giá thầu · Nguồn phân bổ \(for an eligible app\)Enabled or disabledapp_attribution_sourceFor an eligible app:',
     '| Tối ưu hóa và giá thầu · Nguồn phân bổ (đối với ứng dụng đủ điều kiện) | Bật hoặc tắt | `app_attribution_source` | Đối với ứng dụng đủ điều kiện: |'),
    (r'Tối ưu hóa và giá thầu · Nguồn dữ liệu \(for an eligible app\)Enabled or disabledapp_data_sourceFor an eligible app:',
     '| Tối ưu hóa và giá thầu · Nguồn dữ liệu (đối với ứng dụng đủ điều kiện) | Bật hoặc tắt | `app_data_source` | Đối với ứng dụng đủ điều kiện: |'),
    (r'To obtain the active optimization events for an app, use (\[/app/optimization_event/\]\([^\)]+\))\.',
     r'Để lấy các sự kiện tối ưu hóa đang hoạt động cho ứng dụng, sử dụng \1.'),

    # Search campaign overview & headers
    (r'Search campaign\*\*Disabled\*\* To learn about how to create an Upgraded Smart\+ Campaign with Search campaign setting enabled, see ([^\n]+)',
     r'Chiến dịch tìm kiếm (Search campaign) **Tắt (Disabled)** Để tìm hiểu cách tạo Chiến dịch Upgraded Smart+ khi bật cài đặt Chiến dịch tìm kiếm, xem \1'),
    (r'The catalog solution for Upgraded Smart\+ TikTok Direct Messaging Ads requires setting up an \*\*([^\*]+)\*\*',
     r'Giải pháp danh mục cho Quảng cáo tin nhắn trực tiếp TikTok Upgraded Smart+ yêu cầu thiết lập một **\1**'),
    (r'Creating Automotive Ads for Inventory requires setting up an \*\*([^\*]+)\*\*',
     r'Tạo Quảng cáo ô tô cho Kho hàng yêu cầu thiết lập một **\1**'),
    (r'To ensure certain ad formats are available in the catalog solution for Upgraded Smart\+ TikTok Direct Messaging Ads,',
     'Để đảm bảo một số định dạng quảng cáo nhất định khả dụng trong giải pháp danh mục cho Quảng cáo tin nhắn trực tiếp TikTok Upgraded Smart+,'),
    (r'Bài viết này hướng dẫn bạn từng bước để tạo Upgraded Smart\+ Catalog Ads for App using the Sales objective with the catalog specified at the campaign level',
     'Bài viết này hướng dẫn bạn từng bước để tạo Quảng cáo danh mục Upgraded Smart+ cho Ứng dụng bằng mục tiêu Doanh số với danh mục được chỉ định ở cấp chiến dịch'),
    (r'## Điều kiện tiên quyết for creating Upgraded Smart\+ Catalog DC Ads for App',
     '## Điều kiện tiên quyết để tạo Quảng cáo danh mục Upgraded Smart+ DC cho Ứng dụng'),
    (r'By leveraging Search Ads Campaigns for App, you can effectively grow your user base through two primary strategies: acquiring new users \(Prospecting\) and re-engaging your existing audience \(Retargeting\)\.',
     'Bằng cách tận dụng Chiến dịch quảng cáo tìm kiếm cho Ứng dụng, bạn có thể phát triển tệp người dùng của mình một cách hiệu quả thông qua hai chiến lược chính: thu hút người dùng mới (Prospecting) và tương tác lại với đối tượng khán giả hiện tại của bạn (Retargeting).'),
    (r'To configure this campaign type, set `sales_destination` to `APP` and `catalog_type` to `TRAVEL_ENTERTAINMENT` at the campaign level',
     'Để định cấu hình loại chiến dịch này, hãy đặt `sales_destination` thành `APP` và `catalog_type` thành `TRAVEL_ENTERTAINMENT` ở cấp chiến dịch'),
    (r'As TikTok posts come in diversified forms, they tend to have higher retention rates\.',
     'Vì các bài viết TikTok có hình thức đa dạng nên chúng thường có tỷ lệ giữ chân người xem cao hơn.'),
]
