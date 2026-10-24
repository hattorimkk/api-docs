#!/usr/bin/env python3
"""
u102_dict_batch4.py: Comprehensive translation rules for remaining documentation sentences, lead gen settings, and placements.
"""

BATCH4_RULES = [
    # Budget increase variations
    (r'Allow your budget to automatically increase when your ads are performing well and target CPA, Day 0 target ROAS, and budget requirements are met\.',
     'Cho phép ngân sách của bạn tự động tăng khi quảng cáo hoạt động tốt và đáp ứng các yêu cầu về CPA mục tiêu, ROAS mục tiêu Ngày 0 cùng các yêu cầu về ngân sách.'),
    (r'Your daily budget will be allowed to automatically increase by 20%, up to 10 times per day, when your budget utilization reaches 90% or more\.',
     'Ngân sách hàng ngày của bạn sẽ được phép tự động tăng 20%, tối đa 10 lần mỗi ngày, khi mức sử dụng ngân sách đạt từ 90% trở lên.'),

    # Destinations App Store / Google Play
    (r'When promotion_type at the ad group level is APP_IOS, you can only set the Điểm đến as App Store\.',
     'Khi `promotion_type` ở cấp nhóm quảng cáo là `APP_IOS`, bạn chỉ có thể đặt Điểm đến là App Store.'),
    (r'When promotion_type at the ad group level is APP_ANDROID, you can only set the Điểm đến as Google Play\.',
     'Khi `promotion_type` ở cấp nhóm quảng cáo là `APP_ANDROID`, bạn chỉ có thể đặt Điểm đến là Google Play.'),

    # Vehicle Card CTA & landing page
    (r'The Vehicle Cards showcase the following attributes of the vehicle as defined in the catalog, and a CTA button, which will direct users to the third-party landing page\.',
     'Thẻ xe giới thiệu các thuộc tính sau của xe như đã xác định trong danh mục cùng một nút CTA, chuyển hướng người dùng đến trang đích của bên thứ ba.'),
    (r'CTA button "Search Inventory", which directs the audience to an auto-generated Instant Product Page',
     'Nút CTA "Tìm kiếm kho hàng", chuyển hướng khán giả đến Trang sản phẩm tức thì được tạo tự động'),
    (r'Users will be directed to your product links, TikTok Instant Page, or the specified link depending on where they’re most likely to convert\.',
     'Người dùng sẽ được chuyển hướng đến liên kết sản phẩm, Trang tức thì TikTok hoặc liên kết đã chỉ định tùy thuộc vào nơi họ có nhiều khả năng chuyển đổi nhất.'),

    # Creative catalog toggles
    (r'Enable "Product video URL" in your catalog creative settings, allowing the system to use videos from your catalogs in the ad\.',
     'Bật "URL video sản phẩm" trong cài đặt nội dung sáng tạo danh mục của bạn, cho phép hệ thống sử dụng video từ danh mục của bạn trong quảng cáo.'),
    (r'Enable "Image" in your catalog creative settings, allowing the system to use images from your catalogs in the ad\.',
     'Bật "Hình ảnh" trong cài đặt nội dung sáng tạo danh mục của bạn, cho phép hệ thống sử dụng hình ảnh từ danh mục của bạn trong quảng cáo.'),
    (r'If you enable auto-selection of catalog creatives \(catalog_creative_toggle is true\), the system will automatically create ads using combinations of three possible formats: catalog carousel, catalog video, and single video\.',
     'Nếu bạn bật tính năng tự động chọn mẫu quảng cáo danh mục (`catalog_creative_toggle` là `true`), hệ thống sẽ tự động tạo quảng cáo bằng các tổ hợp của ba định dạng có thể: thẻ xoay vòng danh mục, video danh mục và video đơn lẻ.'),

    # Smart+ placements description
    (r'The system will automatically configure placements for your Upgraded Smart\+ Ad Groups based on your other settings and select high-quality traffic from various placements to deliver better results\.',
     'Hệ thống sẽ tự động định cấu hình vị trí hiển thị cho Nhóm quảng cáo Upgraded Smart+ dựa trên các cài đặt khác của bạn và chọn lưu lượng truy cập chất lượng cao từ các vị trí hiển thị khác nhau để mang lại kết quả tốt hơn.'),
    (r'To retrieve the exact placement setting of an Upgraded Smart\+ Ad Group, use (\[/smart_plus/adgroup/get/\]\([^\)]+\))\.',
     r'Để lấy cài đặt vị trí hiển thị chính xác của Nhóm quảng cáo Upgraded Smart+, sử dụng \1.'),
    (r'To use specific placements, set placement_type to PLACEMENT_TYPE_NORMAL and specify one or more of the following placements in placements:',
     'Để sử dụng các vị trí hiển thị cụ thể, hãy đặt `placement_type` thành `PLACEMENT_TYPE_NORMAL` và chỉ định một hoặc nhiều vị trí hiển thị sau trong `placements`:'),

    # Product-level targeting
    (r'\*\*Note\*\*: Your selected catalog includes product-level targeting\.',
     '**Lưu ý**: Danh mục đã chọn của bạn bao gồm tính năng nhắm mục tiêu ở cấp sản phẩm.'),
    (r'If a product\'s targeting conflicts with your ad group settings, ads won\'t be delivered for that product\.',
     'Nếu tính năng nhắm mục tiêu của sản phẩm xung đột với cài đặt nhóm quảng cáo của bạn, quảng cáo sẽ không được phân phối cho sản phẩm đó.'),

    # Instant Forms & Lead Gen
    (r'Specify the page ID of an Instant Form\.', 'Chỉ định ID trang của một Biểu mẫu tức thì.'),
    (r'To obtain the page IDs of Instant Forms within your ad account, use (\[/page/get/\]\([^\)]+\)) and set business_type to LEAD_GEN\.',
     r'Để lấy ID trang của các Biểu mẫu tức thì trong tài khoản quảng cáo của bạn, sử dụng \1 và đặt `business_type` thành `LEAD_GEN`.'),
    (r'To create an Instant Form, use (\[Instant Page Editor SDK\]\([^\)]+\)) and set businessType to 1\.',
     r'Để tạo một Biểu mẫu tức thì, sử dụng \1 và đặt `businessType` thành 1.'),
    (r'Conversion \*\*Note\*\*: When you use the Website engagements goal, deep funnel optimization is not supported\.',
     'Chuyển đổi (Conversion) **Lưu ý**: Khi bạn sử dụng mục tiêu Tương tác trên trang web (Website engagements), tính năng tối ưu hóa phễu sâu (deep funnel optimization) không được hỗ trợ.'),
    (r'CONVERT \*\*Note\*\*: When you use the WEBSITE_ENGAGEMENT goal, deep funnel optimization parameters \(deep_funnel_optimization_status, deep_funnel_event_source , deep_funnel_event_source_id,deep_funnel_optimization_event\) are not supported\.',
     'CONVERT **Lưu ý**: Khi bạn sử dụng mục tiêu WEBSITE_ENGAGEMENT, các tham số tối ưu hóa phễu sâu (`deep_funnel_optimization_status`, `deep_funnel_event_source`, `deep_funnel_event_source_id`, `deep_funnel_optimization_event`) không được hỗ trợ.'),

    # Messaging and Phone Call specifics
    (r'The system will automatically populate landing_page_url_list based on your instant messaging app setting at the ad group level\.',
     'Hệ thống sẽ tự động điền `landing_page_url_list` dựa trên cài đặt ứng dụng tin nhắn tức thì của bạn ở cấp nhóm quảng cáo.'),
    (r'Manually specify the Instant messaging URL and do not pass page_list\.',
     'Chỉ định thủ công URL tin nhắn tức thì và không truyền `page_list`.'),
    (r'\*\*Note\*\*: To verify Liệu a URL is a valid Apple’s universal link or Android App Link, or Custom URL scheme, pass the URL to the parameter url in (\[/tool/url_validate/\]\([^\)]+\))\.',
     r'**Lưu ý**: Để xác minh xem một URL có phải là Universal Link của Apple, Android App Link hoặc URL scheme tùy chỉnh hợp lệ hay không, hãy truyền URL vào tham số `url` trong \1.'),
    (r'This enables the ad audience to directly reach out to you \(the advertiser\) via phone by clicking the call-to-action button within the ad, or be directed to view a Custom TikTok Instant Page\.',
     'Điều này cho phép khán giả quảng cáo liên hệ trực tiếp với bạn (nhà quảng cáo) qua điện thoại bằng cách nhấp vào nút kêu gọi hành động trong quảng cáo, hoặc được chuyển hướng đến xem Trang tức thì TikTok tùy chỉnh.'),
    (r'\*\*Note\*\*: To obtain the region code \(phone_region_code\) and region calling code \(phone_region_calling_code\) for the region of a specific phone number, use (\[/tool/phone_region_code/\]\([^\)]+\))\.',
     r'**Lưu ý**: Để lấy mã vùng (`phone_region_code`) và mã gọi vùng (`phone_region_calling_code`) cho khu vực của một số điện thoại cụ thể, sử dụng \1.'),

    # Multi-destinations Lead Gen
    (r'Tối ưu hóa và giá thầu · Vị trí tối ưu hóasSelect at least two of the following destinations:',
     '| Tối ưu hóa và giá thầu · Vị trí tối ưu hóa | Chọn ít nhất hai trong các điểm đến sau:'),
    (r'To learn about the valid values, see Available optimization location combinations for multiple location selection\.',
     'Để tìm hiểu các giá trị hợp lệ, xem [Các tổ hợp vị trí tối ưu hóa khả dụng khi chọn nhiều vị trí].'),
    (r'The possible optimization location combinations for your ad group with multiple location selection are illustrated in the following table\.',
     'Các tổ hợp vị trí tối ưu hóa có thể có cho nhóm quảng cáo của bạn khi chọn nhiều vị trí được minh họa trong bảng sau.'),
    (r'Instant formGet people to fill out a custom form on TikTok\.optimization_locations\.promotion_typeLEAD_GENRATION',
     '| Biểu mẫu tức thì (Instant form) | Thu hút mọi người điền vào biểu mẫu tùy chỉnh trên TikTok. | `optimization_locations.promotion_type` | `LEAD_GENRATION` |'),
    (r'TikTok direct messagesGet people to direct message you on TikTok\.optimization_locations\.promotion_typeLEAD_GEN_CLICK_TO_TT_DIRECT_MESSAGE',
     '| Tin nhắn trực tiếp TikTok | Thu hút mọi người gửi tin nhắn trực tiếp cho bạn trên TikTok. | `optimization_locations.promotion_type` | `LEAD_GEN_CLICK_TO_TT_DIRECT_MESSAGE` |'),
    (r'WebsiteGet people to visit your website\. A data connection is required\.optimization_locations\.promotion_target_type',
     '| Trang web (Website) | Thu hút mọi người truy cập trang web của bạn. Yêu cầu kết nối dữ liệu. | `optimization_locations.promotion_target_type` |'),
    (r'multi_dest_list\.landing_page_urlSpecify the landing page URL of the website that has the Website Form via landing_page_url',
     '| `multi_dest_list.landing_page_url` | Chỉ định URL trang đích của trang web có Biểu mẫu trang web qua `landing_page_url` |'),
    (r'optimization_locations\.optimization_eventSpecify any of the following values:',
     '| `optimization_locations.optimization_event` | Chỉ định bất kỳ giá trị nào sau đây:'),
    (r'Ví dụ, if you want to set your optimization location combination to Website and Instant form, pass the following parameters:',
     'Ví dụ: nếu bạn muốn đặt tổ hợp vị trí tối ưu hóa thành Trang web và Biểu mẫu tức thì, hãy truyền các tham số sau:'),

    # Subplacements
    (r'Vị trí hiển thị và an toàn thương hiệu · Vị trí phụ \(Optional when Placement includes TikTok\)Tắt hoặc bật \(Disabled hoặc Enabled\) with the following option:',
     '| Vị trí hiển thị và an toàn thương hiệu · Vị trí phụ (Không bắt buộc khi Vị trí hiển thị bao gồm TikTok) | Tắt hoặc bật với tùy chọn sau:'),
    (r'Nếu muốn truy cập, vui lòng liên hệ với đại diện TikTok của bạn\.tiktok_subplacementsWhen placement_type is PLACEMENT_TYPE_NORMAL and placements includes PLACEMENT_TIKTOK:',
     'Nếu muốn truy cập, vui lòng liên hệ với đại diện TikTok của bạn. | `tiktok_subplacements` | Khi `placement_type` là `PLACEMENT_TYPE_NORMAL` và `placements` bao gồm `PLACEMENT_TIKTOK`: |'),

    # Additional UI squished rows
    (r'The possible ad format combinations for your Upgraded Smart\+ ([^\n]+) are illustrated in the following table\.',
     r'Các tổ hợp định dạng quảng cáo có thể có cho Upgraded Smart+ \1 được minh họa trong bảng sau.'),
    (r'To ensure certain ad formats are available in Upgraded Smart\+ ([^\n]+), follow the instructions in the following table\.',
     r'Để đảm bảo các định dạng quảng cáo nhất định khả dụng trong Upgraded Smart+ \1, hãy làm theo hướng dẫn trong bảng sau.'),
]
