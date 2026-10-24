#!/usr/bin/env python3
"""
Từ điển các khối văn bản chuyên sâu phần 2 cho Unit u101
"""

BLOCKS2_RULES = [
    # 1. GMV Max targeting & settings
    (r'Targeting\s*⏎\s*·\s*Placements\s*\|\s*Automatic placement\s*\|\s*N/A\s*\|\s*N/A\s*⏎\s*Chiến dịch GMV Max \(GMV Max Campaigns\) use automated placement selection\.\s*The system will automatically configure placements based on your other settings and select high-quality traffic from various placements to deliver better results\.\s*To retrieve the exact placement setting of a GMV Max Campaign, use (\[/campaign/gmv_max/info/\]\([^\)]+\)) and check the returned `placements`\.',
     r'Nhắm mục tiêu ⏎ · Vị trí hiển thị | Vị trí tự động (Automatic placement) | K/D | K/D ⏎ Chiến dịch GMV Max sử dụng cơ chế chọn vị trí tự động. Hệ thống sẽ tự động cấu hình các vị trí dựa trên cài đặt khác của bạn và lựa chọn lưu lượng truy cập chất lượng cao từ nhiều vị trí khác nhau để mang lại kết quả tốt nhất. Để truy xuất cài đặt vị trí hiển thị chính xác của Chiến dịch GMV Max, sử dụng \1 và kiểm tra trường `placements` trả về.'),

    (r'Targeting\s*⏎\s*·\s*Location\s*\|\s*The country or region that you registered for your TikTok Shop\.\s*\|\s*N/A\s*\|\s*N/A\s*⏎\s*By default, Chiến dịch GMV Max \(GMV Max Campaigns\) will be delivered to the registered country or region of the TikTok Shop\.\s*To retrieve the exact location targeting setting of a GMV Max Campaign, use (\[/campaign/gmv_max/info/\]\([^\)]+\)) and check the returned `location_ids`\.',
     r'Nhắm mục tiêu ⏎ · Vị trí địa lý | Quốc gia hoặc khu vực bạn đã đăng ký cho TikTok Shop. | K/D | K/D ⏎ Theo mặc định, Chiến dịch GMV Max sẽ được phân phối đến quốc gia hoặc khu vực đã đăng ký của TikTok Shop. Để truy xuất cài đặt vị trí địa lý chính xác của Chiến dịch GMV Max, sử dụng \1 và kiểm tra trường `location_ids` trả về.'),

    (r'Targeting\s*⏎\s*·\s*Audience\s*\|\s*Users under 18 excluded\s*\|\s*N/A\s*\|\s*N/A\s*⏎\s*By default, Chiến dịch GMV Max \(GMV Max Campaigns\) will be delivered to all 18\+ age groups\.\s*To retrieve the exact age group targeting setting of a GMV Max Campaign, use (\[/campaign/gmv_max/info/\]\([^\)]+\)) and check the returned `age_groups`\.',
     r'Nhắm mục tiêu ⏎ · Đối tượng | Loại trừ người dùng dưới 18 tuổi | K/D | K/D ⏎ Theo mặc định, Chiến dịch GMV Max sẽ được phân phối đến tất cả các nhóm tuổi từ 18 trở lên. Để truy xuất cài đặt nhóm tuổi chính xác của Chiến dịch GMV Max, sử dụng \1 và kiểm tra trường `age_groups` trả về.'),

    (r'\| Optimization goal \| Gross revenue \| `optimization_goal` \| `VALUE` \|',
     '| Mục tiêu tối ưu hóa (Optimization goal) | Tổng doanh thu (Gross revenue) | `optimization_goal` | `VALUE` |'),

    (r'\| Product ROI target \| Specify a valid ROI target \| `roas_bid` \|\s*Truyền một giá trị hợp lệ\.\s*⏎\s*To obtain the recommended ROI target, use (\[/gmv_max/bid/recommend/\]\([^\)]+\)) and check the returned `roas_bid`\.',
     r'| Mục tiêu ROI sản phẩm | Chỉ định mục tiêu ROI hợp lệ | `roas_bid` | Truyền một giá trị hợp lệ. ⏎ Để lấy mục tiêu ROI khuyến nghị, sử dụng \1 và kiểm tra trường `roas_bid` trả về.'),

    (r'\| Target ROI budget \| Specify a valid budget \| `budget` \|\s*Truyền một giá trị hợp lệ\.\s*⏎\s*To obtain the recommended budget, use (\[/gmv_max/bid/recommend/\]\([^\)]+\)) and check the returned `budget`\.',
     r'| Ngân sách ROI mục tiêu | Chỉ định mức ngân sách hợp lệ | `budget` | Truyền một giá trị hợp lệ. ⏎ Để lấy mức ngân sách khuyến nghị, sử dụng \1 và kiểm tra trường `budget` trả về.'),

    (r'Creative mode\s*\|\s*Any of the following types:\s*•\s*Autoselect videos from up to three video sources \(authorized posts, affiliate posts, and customized posts\) and up to 20 TikTok accounts\s*•\s*Manually select up to 50 authorized posts, videos to be used in customized posts, or a combination of authorized posts and videos to be used in customized posts',
     'Chế độ sáng tạo (Creative mode) | Một trong các loại sau: • Tự động chọn video từ tối đa 3 nguồn video (bài đăng được ủy quyền, bài đăng affiliate và bài đăng tùy chỉnh) và tối đa 20 tài khoản TikTok • Chọn thủ công tối đa 50 bài đăng được ủy quyền, video dùng trong bài đăng tùy chỉnh, hoặc kết hợp cả hai'),

    # 2. Destination - Follow vs visits
    (r'Điểm đến chuyển hướng \(Destination\)\s*•\s*If optimization goal is specified as Follow at the ad group level, the destination is the TikTok account profile page\.\s*•\s*If optimization goal is specified as TikTok page visits at the ad group level, you can choose any of the following types:\s*•\s*Account profile\s*•\s*You don\'t need to provide a TikTok page URL or a TikTok Instant Page\.\s*•\s*Other TikTok page\s*•\s*You need to provide a TikTok page URL\.\s*•\s*TikTok Instant Page\s*•\s*You need to provide a Custom TikTok Instant Page\.',
     'Điểm đến chuyển hướng (Destination)\n• Nếu mục tiêu tối ưu hóa được chỉ định là Lượt theo dõi (Follow) ở cấp nhóm quảng cáo, đích đến là trang hồ sơ tài khoản TikTok. • Nếu mục tiêu tối ưu hóa được chỉ định là Lượt truy cập trang TikTok ở cấp nhóm quảng cáo, bạn có thể chọn một trong các loại sau: • Hồ sơ tài khoản (Account profile) • Bạn không cần cung cấp URL trang TikTok hoặc Trang tức thì TikTok. • Trang TikTok khác (Other TikTok page) • Bạn cần cung cấp URL trang TikTok. • Trang tức thì TikTok (TikTok Instant Page) • Bạn cần cung cấp Trang tức thì TikTok tùy chỉnh.'),

    (r'•\s*If optimization_goal is set to FOLLOWERS at the ad group level, you don\'t need to pass tiktok_page_category, landing_page_url and page_id\.\s*•\s*If optimization_goal is set to PAGE_VISIT at the ad group level, you need to pass tiktok_page_category to specify the exact destination:\s*•\s*If you want to set the Destination to Account profile, set tiktok_page_category to PROFILE_PAGE and don\'t pass landing_page_url and page_id\.\s*•\s*If you want to set the Destination to Other TikTok page, set tiktok_page_category to OTHER_TIKTOK_PAGE and pass the TikTok page URL of a Playlist Page, Hashtag Page, Music Page, or Branded Effect Page via landing_page_url\. Do not pass page_id\.\s*•\s*To obtain a TikTok page URL, tap on the top right corner of the TikTok page you want to promote within your TikTok app, and click to copy the URL\.\s*•\s*If you want to set the Destination to TikTok Instant Page, set tiktok_page_category to TIKTOK_INSTANT_PAGE and pass the ID of a TikTok Instant Page via page_id\. Do not pass landing_page_url\.\s*•\s*To obtain Custom TikTok Instant Pages within your ad account, use (\[/page/get/\]\([^\)]+\)) and set business_type to TIKTOK_INSTANT_PAGE\.',
     r'• Nếu optimization_goal được đặt thành FOLLOWERS ở cấp nhóm quảng cáo, bạn không cần truyền tiktok_page_category, landing_page_url và page_id. • Nếu optimization_goal được đặt thành PAGE_VISIT ở cấp nhóm quảng cáo, bạn cần truyền tiktok_page_category để chỉ định chính xác đích đến: • Nếu muốn đặt Đích đến là Hồ sơ tài khoản, đặt tiktok_page_category thành PROFILE_PAGE và không truyền landing_page_url cùng page_id. • Nếu muốn đặt Đích đến là Trang TikTok khác, đặt tiktok_page_category thành OTHER_TIKTOK_PAGE và truyền URL trang TikTok của Trang danh sách phát (Playlist Page), Trang hashtag, Trang âm nhạc hoặc Trang hiệu ứng thương hiệu qua landing_page_url. Không truyền page_id. • Để lấy URL trang TikTok, hãy nhấn vào góc trên bên phải của trang TikTok bạn muốn quảng bá trong ứng dụng TikTok và nhấp sao chép URL. • Nếu muốn đặt Đích đến là Trang tức thì TikTok, đặt tiktok_page_category thành TIKTOK_INSTANT_PAGE và truyền ID của Trang tức thì TikTok qua page_id. Không truyền landing_page_url. • Để lấy danh sách Trang tức thì TikTok tùy chỉnh trong tài khoản quảng cáo, hãy sử dụng \1 và đặt business_type thành TIKTOK_INSTANT_PAGE.'),

    (r'Call-to-action\s*•\s*If optimization goal is specified as Follow at the ad group level:\s*Disabled\.\s*•\s*If optimization goal is specified as TikTok page visits at the ad group level:\s*Specify a standard call-to-action or a dynamic call-to-action\.',
     'Lời kêu gọi hành động (Call to action)\n• Nếu mục tiêu tối ưu hóa được chỉ định là Lượt theo dõi (Follow) ở cấp nhóm quảng cáo: Tắt (Disabled). • Nếu mục tiêu tối ưu hóa được chỉ định là Lượt truy cập trang TikTok ở cấp nhóm quảng cáo: Chỉ định lời kêu gọi hành động tiêu chuẩn hoặc lời kêu gọi hành động động.'),

    # 3. Important Upgraded Smart+ notice
    (r'>\s*\*\*Important:\*\*\s*\n>\s*-\s*\*\*Upgraded Smart\+ API\*\*:\s*\n>\s*-\s*We are actively upgrading the Smart\+ API to deliver enhanced capabilities and performance\.\s*The new Upgraded Smart\+ API is already launched\.\s*Learn more about (\[(?:Chiến dịch )?Upgraded Smart\+\]\([^\)]+\)) and (\[available Upgraded Smart\+ API endpoints\]\([^\)]+\))\.',
     r'> [!IMPORTANT]\n> - **Upgraded Smart+ API**:\n>     - Chúng tôi đang tích cực nâng cấp Smart+ API để mang lại khả năng và hiệu suất vượt trội. Upgraded Smart+ API mới đã chính thức ra mắt. Tìm hiểu thêm về \1 và \2.'),

    # 4. Optimization event rules
    (r'•\s*Bắt buộc khi Goal is Conversion or Value\.\s*•\s*When Goal is Value, specify the optimization event as Complete Payment\.\s*•\s*When Goal is Conversion, specify any of the following:\s*•\s*Standard Event\s*•\s*Custom Conversion\s*•\s*Không hỗ trợ \(Not supported\) when Goal is Click or Lượt xem trang đích \(Landing page view\)\.\s*\*\*Note\*\*:\s*When you select a campaign budget mode, this setting, if specified, must be the same across ad group[s]? within the same campaign\.',
     '• Bắt buộc khi Mục tiêu là Chuyển đổi (Conversion) hoặc Giá trị (Value). • Khi Mục tiêu là Giá trị, hãy chỉ định sự kiện tối ưu hóa là Hoàn tất thanh toán (Complete Payment). • Khi Mục tiêu là Chuyển đổi, hãy chỉ định một trong các loại sau: • Sự kiện tiêu chuẩn (Standard Event) • Chuyển đổi tùy chỉnh (Custom Conversion) • Không hỗ trợ khi Mục tiêu là Lượt nhấp (Click) hoặc Lượt xem trang đích (Landing page view). **Lưu ý**: Khi bạn chọn chế độ ngân sách chiến dịch, cài đặt này (nếu được chỉ định) phải giống nhau trên tất cả các nhóm quảng cáo trong cùng một chiến dịch.'),

    # 5. Instant messaging app selection
    (r'Select your Instant messaging app or use a customized URL\s*Any of the following options:\s*•\s*Messenger with Facebook Page ID\s*•\s*WhatsApp with WhatsApp phone number\s*•\s*Zalo with Zalo phone number\s*•\s*LINE with LINE Business ID\s*•\s*Instant Messaging URL',
     'Chọn ứng dụng nhắn tin tức thì hoặc sử dụng URL tùy chỉnh\nMột trong các tùy chọn sau: • Messenger với ID Trang Facebook (Facebook Page ID) • WhatsApp với số điện thoại WhatsApp • Zalo với số điện thoại Zalo • LINE với ID Doanh nghiệp LINE (LINE Business ID) • URL ứng dụng nhắn tin tức thì (Instant Messaging URL)'),

    (r'•\s*To use the Instant messaging app Messenger:\s*•\s*Set messaging_app_type to MESSENGER\.\s*•\s*Specify a valid Facebook Page ID through messaging_app_account_id\.\s*•\s*Do not pass phone_region_code, phone_region_calling_code, and phone_number\.',
     '• Để sử dụng ứng dụng nhắn tin Messenger:\n• Đặt messaging_app_type thành MESSENGER.\n• Chỉ định ID Trang Facebook hợp lệ qua messaging_app_account_id.\n• Không truyền phone_region_code, phone_region_calling_code và phone_number.'),

    (r'•\s*To use the Instant messaging app WhatsApp:\s*•\s*Set messaging_app_type to WHATSAPP\.\s*•\s*Specify a valid WhatsApp phone number through phone_region_code, phone_region_calling_code, and phone_number\.\s*•\s*Do not pass messaging_app_account_id\.',
     '• Để sử dụng ứng dụng nhắn tin WhatsApp:\n• Đặt messaging_app_type thành WHATSAPP.\n• Chỉ định số điện thoại WhatsApp hợp lệ qua phone_region_code, phone_region_calling_code và phone_number.\n• Không truyền messaging_app_account_id.'),

    # 6. Destination - Website & Dynamic Destination
    (r'•\s*If Optimization location is Website, select any of the following options:\s*•\s*Dynamic destination\s*•\s*When Dynamic Destination is enabled, your audience will be directed to your landing page or an automatically created TikTok Instant Page, depending on what is most likely to generate the best results for your business\.\s*•\s*Website\s*•\s*Instant Product Page',
     '• Nếu Vị trí tối ưu hóa là Website, hãy chọn một trong các tùy chọn sau: • Đích đến động (Dynamic destination) • Khi Đích đến động được bật, đối tượng của bạn sẽ được chuyển hướng đến trang đích hoặc Trang tức thì TikTok được tạo tự động, tùy thuộc vào phương án có nhiều khả năng mang lại kết quả tốt nhất cho doanh nghiệp của bạn. • Website • Trang sản phẩm tức thì (Instant Product Page)'),

    # 7. GMV Max single product rule
    (r'Each product within a TikTok Shop can only be used in one enabled Product GMV Max Campaign at a time\.',
     'Mỗi sản phẩm trong một TikTok Shop chỉ có thể được sử dụng trong duy nhất một Chiến dịch Product GMV Max đang hoạt động tại một thời điểm.'),
    (r'-\s*For Product (?:Chiến dịch GMV Max \(GMV Max Campaigns\)|GMV Max Campaigns) that promote all products within a TikTok Shop, ensure that the TikTok Shop is only used in one enabled Product GMV Max Campaign\.',
     '- Đối với Chiến dịch Product GMV Max quảng bá tất cả sản phẩm trong TikTok Shop, hãy đảm bảo TikTok Shop đó chỉ được sử dụng trong một Chiến dịch Product GMV Max đang hoạt động duy nhất.'),
    (r'-\s*To confirm that no enabled Product (?:Chiến dịch GMV Max \(GMV Max Campaigns\)|GMV Max Campaigns) use all products within a TikTok Shop, call (\[/gmv_max/store/shop_ad_usage_check/\]\([^\)]+\)) and check the returned `promote_all_products_allowed`\.',
     r'- Để xác nhận không có Chiến dịch Product GMV Max nào đang hoạt động sử dụng tất cả sản phẩm trong TikTok Shop, hãy gọi \1 và kiểm tra trường `promote_all_products_allowed` trả về.'),

    # 8. LIVE GMV Max intro
    (r'LIVE (?:Chiến dịch GMV Max \(GMV Max Campaigns\)|GMV Max Campaigns) optimize liveroom traffic to get the highest gross revenue for your LIVE event\.',
     'Chiến dịch LIVE GMV Max tối ưu hóa lưu lượng truy cập phòng LIVE nhằm đạt tổng doanh thu cao nhất cho sự kiện phát trực tiếp (LIVE) của bạn.'),
    (r'\*\*You can use GMV Max API to create LIVE (?:Chiến dịch GMV Max \(GMV Max Campaigns\)|GMV Max Campaigns), and this helps streamline your campaign creation experience, and elevate operational efficiency and scalability\.\*\*',
     '**Bạn có thể sử dụng GMV Max API để tạo Chiến dịch LIVE GMV Max, giúp tối ưu hóa quy trình thiết lập chiến dịch, nâng cao hiệu quả vận hành và khả năng mở rộng quy mô.**'),
    (r'The following table lists the countries or regions where LIVE (?:Chiến dịch GMV Max \(GMV Max Campaigns\)|GMV Max Campaigns) are available\.',
     'Bảng sau liệt kê các quốc gia hoặc khu vực hỗ trợ Chiến dịch LIVE GMV Max.'),
]
