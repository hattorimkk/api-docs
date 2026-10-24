#!/usr/bin/env python3
"""
Từ điển các mệnh đề, câu hướng dẫn lặp lại tần suất cao trong u102.
"""

CORE_CLAUSES_RULES = [
    # Schedule & Budget conditions
    (r'\*\*Note\*\*: You can only set schedule_type to SCHEDULE_FROM_NOW in any of the following scenarios:\s*• Ở cấp chiến dịch, budget_mode là BUDGET_MODE_DYNAMIC_DAILY_BUDGET\s*• Ở cấp nhóm quảng cáo, budget_mode là BUDGET_MODE_DYNAMIC_DAILY_BUDGET',
     '**Lưu ý**: Bạn chỉ có thể đặt schedule_type thành SCHEDULE_FROM_NOW trong các trường hợp sau: • Ở cấp chiến dịch, budget_mode là BUDGET_MODE_DYNAMIC_DAILY_BUDGET • Ở cấp nhóm quảng cáo, budget_mode là BUDGET_MODE_DYNAMIC_DAILY_BUDGET'),

    (r'\*\*Note\*\*: You can only set schedule_type to SCHEDULE_START_END in any of the following scenarios:\s*• Ở cấp chiến dịch, budget_mode là BUDGET_MODE_TOTAL\s*• Ở cấp nhóm quảng cáo, budget_mode là BUDGET_MODE_TOTAL',
     '**Lưu ý**: Bạn chỉ có thể đặt schedule_type thành SCHEDULE_START_END trong các trường hợp sau: • Ở cấp chiến dịch, budget_mode là BUDGET_MODE_TOTAL • Ở cấp nhóm quảng cáo, budget_mode là BUDGET_MODE_TOTAL'),

    (r'• When rta_id is not specified:\s*• false or not specified\s*• When rta_id is specified, use any of the following configurations\s*:\s*• true\s*• false or not specified',
     '• Khi `rta_id` không được chỉ định: `false` hoặc không chỉ định. • Khi `rta_id` được chỉ định, dùng bất kỳ cấu hình nào sau đây: `true`, `false` hoặc không chỉ định.'),

    (r'• When budget_optimize_on is true or not specified, use any of the following values\s*:\s*• BUDGET_MODE_TOTAL\s*• BUDGET_MODE_DYNAMIC_DAILY_BUDGET\s*• When budget_optimize_on is false, use any of the following values:\s*• BUDGET_MODE_INFINITE\s*• BUDGET_MODE_DAY\s*• BUDGET_MODE_TOTAL',
     '• Khi `budget_optimize_on` là `true` hoặc không chỉ định, sử dụng: `BUDGET_MODE_TOTAL` hoặc `BUDGET_MODE_DYNAMIC_DAILY_BUDGET`. • Khi `budget_optimize_on` là `false`, sử dụng: `BUDGET_MODE_INFINITE`, `BUDGET_MODE_DAY` hoặc `BUDGET_MODE_TOTAL`.'),

    (r'• To set an automatic campaign budget, set this field to true or leave it unspecified\.\s*• To set a custom ad group budget, set this field to false\.',
     '• Để đặt ngân sách chiến dịch tự động, đặt trường này thành `true` hoặc để trống (không chỉ định). • Để đặt ngân sách nhóm quảng cáo tùy chỉnh, đặt trường này thành `false`.'),

    (r'• When Campaign budget strategy is Automatic campaign budget, specify any of the following modes:\s*• Daily\s*• Lifetime\s*• When Campaign budget strategy is Custom ad group budget, specify any of the following modes to determine the budget limit for all ad groups:\s*• No limit\s*• Daily\s*• Lifetime',
     '• Khi Chiến lược ngân sách chiến dịch là Ngân sách chiến dịch tự động, chỉ định một trong các chế độ: • Hàng ngày (Daily) • Trọn đời (Lifetime). • Khi Chiến lược ngân sách là Ngân sách nhóm quảng cáo tùy chỉnh, chỉ định giới hạn cho tất cả các nhóm quảng cáo: • Không giới hạn (No limit) • Hàng ngày (Daily) • Trọn đời (Lifetime).'),

    (r'Một trong các loại sau: • \*\*Automatic campaign budget\*\*: Your budget will be automatically allocated and optimized across ad groups\. All ad groups must share the same budget and optimization settings\.\s*• \*\*Custom ad group budget\*\*: Precisely control spend for each ad group, using different budget and optimization settings for each\.',
     'Một trong các loại sau: • **Ngân sách chiến dịch tự động (Automatic campaign budget)**: Ngân sách sẽ được tự động phân bổ và tối ưu hóa giữa các nhóm quảng cáo. Tất cả các nhóm quảng cáo phải dùng chung cài đặt ngân sách và tối ưu hóa. • **Ngân sách nhóm quảng cáo tùy chỉnh (Custom ad group budget)**: Kiểm soát chi tiêu chính xác cho từng nhóm quảng cáo với các cài đặt ngân sách và tối ưu hóa riêng biệt.'),

    # Targeting
    (r'You can use automatic targeting to leverage real-time data and machine learning to target audiences most likely to engage with your ads\.',
     'Bạn có thể sử dụng nhắm mục tiêu tự động để tận dụng dữ liệu thời gian thực và máy học nhằm tiếp cận các đối tượng có khả năng tương tác cao nhất với quảng cáo của bạn.'),

    (r'To learn about the supported targeting settings for each mode, see \[Available targeting settings for different targeting optimization modes\]\(([^\)]+)\)\.',
     r'Để tìm hiểu về các cài đặt nhắm mục tiêu được hỗ trợ cho từng chế độ, xem [Cài đặt nhắm mục tiêu khả dụng cho các chế độ tối ưu hóa nhắm mục tiêu khác nhau](\1).'),

    (r'Audience suggestions guide automatic targeting by choosing the audience you think is most likely to convert\. The system uses these suggestions to reach the right people and will expand beyond them if likely to find better performance\.',
     'Gợi ý đối tượng định hướng cho nhắm mục tiêu tự động bằng cách chọn nhóm đối tượng mà bạn cho rằng có nhiều khả năng chuyển đổi nhất. Hệ thống sử dụng các gợi ý này để tiếp cận đúng người và sẽ mở rộng ra ngoài phạm vi đó nếu nhận thấy có thể đạt hiệu suất tốt hơn.'),

    (r'Audience suggestions · Age \*\((Không bắt buộc|Optional)\)\*\s*\*\*Note\*\*: Audience suggestions guide automatic targeting by choosing the audience you think is most likely to convert\. The system uses these suggestions to reach the right people and will expand beyond them if likely to find better performance\.age_groupsSpecify valid values or not specified',
     '| Gợi ý đối tượng · Độ tuổi *(Không bắt buộc)* | Gợi ý đối tượng định hướng nhắm mục tiêu tự động bằng cách chọn độ tuổi bạn cho là có khả năng chuyển đổi cao nhất. Hệ thống sẽ mở rộng ngoài phạm vi nếu tìm thấy hiệu suất tốt hơn. | `age_groups` | Chỉ định các giá trị hợp lệ hoặc không chỉ định |'),

    # Placements
    (r'• The system will automatically configure placements for your Upgraded Smart\+ Ad Groups based on your other settings and select high-quality traffic from various placements to deliver better results\. Nếu được cung cấp, các tham số placement_type và placements sẽ bị bỏ qua\.\s*• To retrieve the exact placement setting of an Upgraded Smart\+ Ad Group, use (\[\/smart_plus\/adgroup\/get\/\]\([^\)]+\))\.\s*• To use specific placements, set placement_type to PLACEMENT_TYPE_NORMAL and specify one or more of the following placements in placements:\s*• PLACEMENT_TIKTOK\s*• PLACEMENT_PANGLE\s*• PLACEMENT_GLOBAL_APP_BUNDLE',
     r'• Hệ thống sẽ tự động cấu hình vị trí hiển thị cho Nhóm quảng cáo Upgraded Smart+ của bạn dựa trên các cài đặt khác và chọn lọc lưu lượng truy cập chất lượng cao từ nhiều vị trí khác nhau để mang lại kết quả tốt hơn. Nếu được cung cấp, các tham số placement_type và placements sẽ bị bỏ qua. • Để lấy cài đặt vị trí chính xác của Nhóm quảng cáo Upgraded Smart+, hãy sử dụng \1. • Để sử dụng các vị trí cụ thể, đặt placement_type thành PLACEMENT_TYPE_NORMAL và chỉ định một hoặc nhiều vị trí sau trong placements: • PLACEMENT_TIKTOK • PLACEMENT_PANGLE • PLACEMENT_GLOBAL_APP_BUNDLE'),

    (r'Một trong các loại sau: • \*\*Automatic Placement\*\* • \*\*Select specific placements\*\*:\s*• TikTok\s*• Global App Bundle\s*• Pangle',
     'Một trong các loại sau: • **Vị trí tự động (Automatic Placement)** • **Chọn các vị trí cụ thể (Select specific placements)**: • TikTok • Global App Bundle • Pangle'),

    (r'Một trong các loại sau: • \*\*Automatic Placement\*\* • \*\*Select Placement\*\* with TikTok placement or Pangle placement or both',
     'Một trong các loại sau: • **Vị trí tự động (Automatic Placement)** • **Chọn vị trí hiển thị (Select Placement)** với vị trí TikTok hoặc Pangle hoặc cả hai'),

    (r'Đặt placement_type thành PLACEMENT_TYPE_NORMAL, and only include PLACEMENT_TIKTOK or PLACEMENT_PANGLE or both in the value of placements',
     'Đặt placement_type thành PLACEMENT_TYPE_NORMAL, và chỉ bao gồm PLACEMENT_TIKTOK hoặc PLACEMENT_PANGLE hoặc cả hai trong giá trị của placements'),

    (r'DSA supports TikTok and Pangle placements\.', 'DSA hỗ trợ các vị trí hiển thị TikTok và Pangle.'),

    # Bidding & Deep Funnel
    (r'• To enable deep funnel optimization, set deep_funnel_optimization_status to ON and specify deep_funnel_event_source, deep_funnel_event_source_id, and deep_funnel_optimization_event\.\s*• To disable deep funnel optimization, set deep_funnel_optimization_status to OFF or leave deep_funnel_optimization_status unspecified\. Do not specify deep_funnel_event_source, deep_funnel_event_source_id, and deep_funnel_optimization_event\.\s*\*\*Note\*\*:\s*• Deep funnel optimization with CRM events is currently an allowlist-only feature\. Nếu bạn muốn truy cập tính năng này, vui lòng liên hệ với đại diện TikTok của bạn\.\s*• Deep funnel optimization with Pixel or Offline events is generally available\.',
     '• Để bật tối ưu hóa phễu sâu, đặt `deep_funnel_optimization_status` thành `ON` và chỉ định `deep_funnel_event_source`, `deep_funnel_event_source_id` cùng `deep_funnel_optimization_event`. • Để tắt tối ưu hóa phễu sâu, đặt `deep_funnel_optimization_status` thành `OFF` hoặc để trống không chỉ định. Không chỉ định `deep_funnel_event_source`, `deep_funnel_event_source_id` và `deep_funnel_optimization_event`. **Lưu ý**: • Tối ưu hóa phễu sâu với sự kiện CRM hiện là tính năng chỉ dành cho danh sách cho phép (allowlist). Nếu muốn truy cập tính năng này, vui lòng liên hệ với đại diện TikTok của bạn. • Tối ưu hóa phễu sâu với sự kiện Pixel hoặc sự kiện Ngoại tuyến được cung cấp rộng rãi.'),

    (r'The bid strategy can be any of the following: • Maximum Delivery\. • Cost Cap\. You need to specify a Target CPA at the same time\.',
     'Chiến lược giá thầu có thể là bất kỳ tùy chọn nào sau đây: • Phân phối tối đa (Maximum Delivery). • Giới hạn chi phí (Cost Cap). Bạn cần chỉ định CPA mục tiêu cùng lúc.'),

    (r'• If Goal is Conversion, the strategy can only be Maximum Delivery or Cost Cap\. • Đối với Giới hạn chi phí, bạn cần chỉ định CPA mục tiêu cùng lúc\.',
     '• Nếu Mục tiêu là Chuyển đổi, chiến lược chỉ có thể là Phân phối tối đa (Maximum Delivery) hoặc Giới hạn chi phí (Cost Cap). • Đối với Giới hạn chi phí, bạn cần chỉ định CPA mục tiêu cùng lúc.'),

    (r'Optimization and bidding · Goal • In-app event • We\'ll show your ads to the people who are most likely to perform a specific in-app event\.',
     'Tối ưu hóa và giá thầu · Mục tiêu • Sự kiện trong ứng dụng • Chúng tôi sẽ hiển thị quảng cáo cho những người có nhiều khả năng thực hiện một sự kiện cụ thể trong ứng dụng nhất.'),

    # Identities & Endpoints
    (r'To get the list of identities under your ad account, use (\[\/identity\/get\/\]\([^\)]+\))\.',
     r'Để lấy danh sách các danh tính thuộc tài khoản quảng cáo của bạn, sử dụng \1.'),

    (r'To obtain the list of Pixels within your ad account, use (\[\/pixel\/list\/\]\([^\)]+\))\.',
     r'Để lấy danh sách Pixel trong tài khoản quảng cáo của bạn, sử dụng \1.'),

    (r'To obtain the optimization events that have been configured for a Pixel, use (\[\/pixel\/list\/\]\([^\)]+\))\.',
     r'Để lấy các sự kiện tối ưu hóa đã được cấu hình cho Pixel, sử dụng \1.'),

    (r'To obtain the list of Apps under your ad account, use (\[\/app\/list\/\]\([^\)]+\))\.',
     r'Để lấy danh sách Ứng dụng thuộc tài khoản quảng cáo của bạn, sử dụng \1.'),

    (r'To get image IDs, use (\[\/file\/image\/ad\/upload\/\]\([^\)]+\))\.',
     r'Để lấy ID hình ảnh, hãy sử dụng \1.'),

    (r'To create an interactive add-on \(creative portfolio\), use (\[\/creative\/portfolio\/create\/\]\([^\)]+\))\.',
     r'Để tạo tiện ích bổ sung tương tác (danh mục sáng tạo), hãy sử dụng \1.'),

    (r'To learn about how to obtain the ID of a Display Card portfolio, see \[Cards\]\(([^\)]+)\)\.',
     r'Để tìm hiểu cách lấy ID danh mục Display Card, hãy xem [Cards](\1).'),

    # Creatives & Catalog
    (r'The catalog needs to contain at least two products supported in Catalog Carousel Ads\.',
     'Danh mục cần chứa ít nhất hai sản phẩm được hỗ trợ trong Quảng cáo xoay vòng danh mục.'),

    (r'Specify a piece of music supported in Catalog Carousel Ads\.',
     'Chỉ định một bài nhạc được hỗ trợ trong Quảng cáo xoay vòng danh mục.'),

    (r'Use specified video creatives to promote your products\.',
     'Sử dụng các mẫu quảng cáo video đã chỉ định để quảng bá sản phẩm của bạn.'),

    (r'Specify an end card image', 'Chỉ định một hình ảnh thẻ kết thúc (End card)'),
    (r'Specify additional videos or TikTok video posts', 'Chỉ định các video bổ sung hoặc bài viết video TikTok'),
    (r'Specify additional videos', 'Chỉ định các video bổ sung'),

    (r'Specify one to 50 ad creatives through creative_list\. Mẫu quảng cáo có thể là bất kỳ loại nào sau đây: • Videos • TikTok video posts • TikTok photo posts • Carousel To learn about configurations of the available ad creative combinations based on identity type, see \[Ad creative combinations by identity and ad type\]\(([^\)]+)\)\.',
     r'Chỉ định từ 1 đến 50 mẫu quảng cáo qua creative_list. Mẫu quảng cáo có thể là bất kỳ loại nào sau đây: • Video • Bài viết video TikTok • Bài viết ảnh TikTok • Thẻ xoay vòng (Carousel). Để tìm hiểu về cấu hình các tổ hợp mẫu quảng cáo khả dụng dựa trên loại danh tính, xem [Tổ hợp mẫu quảng cáo theo danh tính và loại quảng cáo](\1).'),

    (r'For a single ad, you can include one to \*\*50 ad creatives\*\* that can consist of the following types:\s*• Single Video\s*• Carousel',
     'Đối với một quảng cáo đơn lẻ, bạn có thể bao gồm từ 1 đến **50 mẫu quảng cáo**, bao gồm các loại sau: • Video đơn (Single Video) • Thẻ xoay vòng (Carousel)'),

    (r'Filter the pieces of music for Catalog Carousel Ads under an ad account by specifying music_scene as CATALOG_CAROUSEL in (\[\/file\/music\/get\/\]\([^\)]+\))\.',
     r'Lọc các bài nhạc cho Quảng cáo xoay vòng danh mục thuộc tài khoản quảng cáo bằng cách chỉ định music_scene là CATALOG_CAROUSEL trong \1.'),

    (r'Upload a piece of customized music for Catalog Carousel Ads to an ad account by using any of the following methods:\s*• Specify music_scene as CATALOG_CAROUSEL and pass music_file and music_signature in (\[\/file\/music\/upload\/\]\([^\)]+\))\.\s*• Specify music_scene as CATALOG_CAROUSEL, upload_type as UPLOAD_BY_FILE_ID, and pass file_id to (\[\/file\/music\/upload\/\]\([^\)]+\))\.',
     r'Tải lên một bài nhạc tùy chỉnh cho Quảng cáo xoay vòng danh mục vào tài khoản quảng cáo bằng bất kỳ phương thức nào sau đây: • Chỉ định music_scene là CATALOG_CAROUSEL và truyền music_file cùng music_signature trong \1. • Chỉ định music_scene là CATALOG_CAROUSEL, upload_type là UPLOAD_BY_FILE_ID, và truyền file_id trong \2.'),

    (r'If product_specific_type is set to CUSTOMIZED_PRODUCTS, you need to specify a maximum of 20 available catalog products through product_ids\. không cần product_set_id\.\s*• To retrieve the product ID \(product_id\) of each catalog product, use (\[\/catalog\/product\/get\/\]\([^\)]+\))\.',
     r'Nếu product_specific_type được đặt thành CUSTOMIZED_PRODUCTS, bạn cần chỉ định tối đa 20 sản phẩm danh mục khả dụng qua product_ids. Không cần product_set_id. • Để lấy ID sản phẩm (product_id) của từng sản phẩm trong danh mục, sử dụng \1.'),

    (r'To enable auto-selection of catalog creatives, set catalog_creative_toggle to true, specify a valid ([^\n]+)',
     r'Để bật tính năng tự động chọn mẫu quảng cáo danh mục, đặt catalog_creative_toggle thành true, chỉ định một \1'),

    (r'To disable auto-selection of catalog creatives, set catalog_creative_toggle to false\.',
     'Để tắt tính năng tự động chọn mẫu quảng cáo danh mục, đặt catalog_creative_toggle thành false.'),

    (r'\*\*Note\*\*: music_info is Bắt buộc khi catalog_creative_toggle is true\.',
     '**Lưu ý**: music_info là Bắt buộc khi catalog_creative_toggle là true.'),

    (r'Image Resolution: a maximum of 1242 x 2340 pixels or 2340 x 1242 pixels\.',
     'Độ phân giải hình ảnh: tối đa 1242 x 2340 pixel hoặc 2340 x 1242 pixel.'),

    (r'Aspect Ratio: a maximum of 9:20 or 20:9\.',
     'Tỷ lệ khung hình: tối đa 9:20 hoặc 20:9.'),

    (r'Bắt buộc khi optimization_goal is set to CONVERT\.',
     'Bắt buộc khi optimization_goal được đặt thành CONVERT.'),

    (r'The URL parameters will not be automatically appended to the landing_page_url_list upon ad delivery\.',
     'Các tham số URL sẽ không được tự động thêm vào landing_page_url_list khi phân phối quảng cáo.'),

    (r'You can verify this by checking the value of approved returned from (\[\/catalog\/overview\/\]\([^\)]+\))\.',
     r'Bạn có thể xác minh điều này bằng cách kiểm tra giá trị approved trả về từ \1.'),

    (r'At the campaign level, a lifetime campaign budget is set\.',
     'Ở cấp chiến dịch, ngân sách chiến dịch trọn đời đã được thiết lập.'),

    (r'The value of the parameter is_carousel_usable returned from (\[\/file\/image\/ad\/search\/\]\([^\)]+\)) must be true\.',
     r'Giá trị của tham số is_carousel_usable trả về từ \1 phải là true.'),

    (r'4\. \*\((Không bắt buộc|Optional)\)\* Create a product set using (\[\/catalog\/set\/create\/\]\([^\)]+\))\.',
     r'4. *(Không bắt buộc)* Tạo một bộ sản phẩm bằng cách sử dụng \1.'),

    (r'If optimization_goal is CONVERSATION, omit optimization_event or set optimization_event to MESSAGE\.',
     'Nếu optimization_goal là CONVERSATION, bỏ qua optimization_event hoặc đặt optimization_event thành MESSAGE.'),

    (r'one to 50 videos \(video_info\) with cover images \(image_info\) and one to five ad texts \(ad_text_list\)',
     '1 đến 50 video (video_info) kèm hình ảnh bìa (image_info) và 1 đến 5 văn bản quảng cáo (ad_text_list)'),

    (r'set ad_format to SINGLE_VIDEO', 'đặt ad_format thành SINGLE_VIDEO'),

    (r'Use these endpoints to manage Spark Ads\.', 'Sử dụng các endpoint này để quản lý Spark Ads.'),

    (r'- \*\*Identity information\*\*: Use the\[? \/identity\/info\/\]?\(([^\)]+)\) endpoint to gather details about a specific identity\.',
     r'- **Thông tin danh tính**: Sử dụng endpoint [/identity/info/](\1) để thu thập thông tin chi tiết về một danh tính cụ thể.'),

    (r'> There are no changes to these endpoints\.', '> Không có thay đổi nào đối với các endpoint này.'),
]
