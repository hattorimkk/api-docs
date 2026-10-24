#!/usr/bin/env python3
"""
u102_dict_batch6.py: Translation rules for link labels, squished rows, and residual lines in u102.
"""

BATCH6_RULES = [
    # 1. Search campaign squished rows
    (r'is_search_campaignfalse or not specified', '| `is_search_campaign` | `false` hoặc không chỉ định |'),
    (r'is_search_campaigntrue or not specified', '| `is_search_campaign` | `true` hoặc không chỉ định |'),

    # 2. Markdown link labels
    (r'\[Mẫu quảng cáo combinations by identity and ad type\]', '[Tổ hợp mẫu quảng cáo theo danh tính và loại quảng cáo]'),
    (r'\[Điểm đến and tracking message event set options for different scenarios\]', '[Các tùy chọn điểm đến và bộ sự kiện tin nhắn theo dõi cho các trường hợp khác nhau]'),
    (r'\[Create an Upgraded Smart\+ Catalog Search Ads Campaign for App\]', '[Tạo Chiến dịch quảng cáo tìm kiếm danh mục Upgraded Smart+ cho Ứng dụng]'),
    (r'\[Create an Upgraded Smart\+ Lead Generation Search Ads Campaign with optimization location as Instant Form\]', '[Tạo Chiến dịch quảng cáo tìm kiếm tìm kiếm khách hàng tiềm năng Upgraded Smart+ với vị trí tối ưu hóa là Biểu mẫu tức thì]'),
    (r'\[Create an Upgraded Smart\+ Lead Generation Search Ads Campaign with optimization location as Website\]', '[Tạo Chiến dịch quảng cáo tìm kiếm tìm kiếm khách hàng tiềm năng Upgraded Smart+ với vị trí tối ưu hóa là Trang web]'),
    (r'\[Create an Upgraded Smart\+ Lead Generation Search Ads Campaign with optimization location as TikTok direct messages\]', '[Tạo Chiến dịch quảng cáo tìm kiếm tìm kiếm khách hàng tiềm năng Upgraded Smart+ với vị trí tối ưu hóa là Tin nhắn trực tiếp TikTok]'),
    (r'\[Create Upgraded Smart\+ Quảng cáo tìm kiếm ô tô \(Quảng cáo tìm kiếm ô tô \(Automotive Search Ads\)\)\]', '[Tạo Quảng cáo tìm kiếm ô tô Upgraded Smart+]'),
    (r'\[Create an Upgraded Smart\+ Lead Generation Search Ads Campaign with optimization location as instant messaging apps\]', '[Tạo Chiến dịch quảng cáo tìm kiếm tìm kiếm khách hàng tiềm năng Upgraded Smart+ với vị trí tối ưu hóa là Ứng dụng nhắn tin tức thì]'),
    (r'\[Create an Upgraded Smart\+ Lead Generation Search Ads Campaign with optimization location as phone call\]', '[Tạo Chiến dịch quảng cáo tìm kiếm tìm kiếm khách hàng tiềm năng Upgraded Smart+ với vị trí tối ưu hóa là Cuộc gọi điện thoại]'),
    (r'\[Create Upgraded Smart\+ Automotive Ads for Inventory\]', '[Tạo Quảng cáo ô tô Upgraded Smart+ cho Kho hàng]'),
    (r'\[Create Upgraded Smart\+ Automotive Ads for Models\]', '[Tạo Quảng cáo ô tô Upgraded Smart+ cho Mẫu xe]'),
    (r'\[Create Upgraded Smart\+ Quảng cáo tìm kiếm ô tô \(Quảng cáo tìm kiếm ô tô \(Automotive Search Ads\)\) for Inventory\]', '[Tạo Quảng cáo tìm kiếm ô tô Upgraded Smart+ cho Kho hàng]'),
    (r'\[Create Upgraded Smart\+ Quảng cáo tìm kiếm ô tô \(Quảng cáo tìm kiếm ô tô \(Automotive Search Ads\)\) for Models\]', '[Tạo Quảng cáo tìm kiếm ô tô Upgraded Smart+ cho Mẫu xe]'),
    (r'\[Create Upgraded Smart\+ Catalog non-DC Ads for App\]', '[Tạo Quảng cáo danh mục không phải DC Upgraded Smart+ cho Ứng dụng]'),
    (r'\[Create Upgraded Smart\+ Catalog DC Ads for App\]', '[Tạo Quảng cáo danh mục DC Upgraded Smart+ cho Ứng dụng]'),
    (r'\[Create Upgraded Smart\+ Catalog Ads with Website and App Optimization\]', '[Tạo Quảng cáo danh mục Upgraded Smart+ với Tối ưu hóa Trang web và Ứng dụng]'),
    (r'\[Create Upgraded Smart\+ Non-Catalog Ads with Website and App Optimization\]', '[Tạo Quảng cáo không dùng danh mục Upgraded Smart+ với Tối ưu hóa Trang web và Ứng dụng]'),
    (r'\[Create an Upgraded Smart\+ Catalog Search Ads Campaign for Website and App\]', '[Tạo Chiến dịch quảng cáo tìm kiếm danh mục Upgraded Smart+ cho Trang web và Ứng dụng]'),
    (r'\[Create an Upgraded Smart\+ Non-Catalog Search Ads Campaign for Website and App\]', '[Tạo Chiến dịch quảng cáo tìm kiếm không dùng danh mục Upgraded Smart+ cho Trang web và Ứng dụng]'),
    (r'\[Create an Upgraded Smart\+ E-commerce Search Ads Campaign for Web\]', '[Tạo Chiến dịch quảng cáo tìm kiếm thương mại điện tử Upgraded Smart+ cho Web]'),
    (r'\[Create an Upgraded Smart\+ Travel Search Ads Campaign for Web\]', '[Tạo Chiến dịch quảng cáo tìm kiếm du lịch Upgraded Smart+ cho Web]'),
    (r'\[Create an Upgraded Smart\+ Streaming Search Ads Campaign for Web\]', '[Tạo Chiến dịch quảng cáo tìm kiếm truyền phát trực tuyến Upgraded Smart+ cho Web]'),
    (r'\[Available product information settings in Upgraded Smart\+ Campaigns\]', '[Cài đặt thông tin sản phẩm khả dụng trong Chiến dịch Upgraded Smart+]'),
    (r'\[Cài đặt nhắm mục tiêu có sẵns for different targeting optimization modes in Upgraded Smart\+ Catalog Search Ads Campaign for Web\]', '[Cài đặt nhắm mục tiêu có sẵn cho các chế độ tối ưu hóa nhắm mục tiêu khác nhau trong Chiến dịch quảng cáo tìm kiếm danh mục Upgraded Smart+ cho Web]'),
    (r'\[Cài đặt nhắm mục tiêu có sẵn cho different targeting optimization modes in Upgraded Smart\+ Catalog Search Ads Campaign for Web\]', '[Cài đặt nhắm mục tiêu có sẵn cho các chế độ tối ưu hóa nhắm mục tiêu khác nhau trong Chiến dịch quảng cáo tìm kiếm danh mục Upgraded Smart+ cho Web]'),

    # 3. Prerequisites & Intros
    (r'Creating Upgraded Smart\+ Catalog Ads for App requires setting up a catalog in your Business Center first\.',
     'Tạo Quảng cáo danh mục Upgraded Smart+ cho Ứng dụng yêu cầu thiết lập một danh mục trong Business Center của bạn trước tiên.'),
    (r'Pass in the `feed_log_id` obtained from Step 2\. Nếu trường `error_affected_products` trong phản hồi không phải là null, hãy kiểm tra chi tiết lỗi và quay lại Bước 2 để tải lại sản phẩm lên\.',
     'Truyền `feed_log_id` lấy được từ Bước 2. Nếu trường `error_affected_products` trong phản hồi không phải là null, hãy kiểm tra chi tiết lỗi và quay lại Bước 2 để tải lại sản phẩm lên.'),
    (r'Based on your preference for Có thực hiện use a catalog and optimization location, you can create an Upgraded Smart\+ Lead Generation Campaign with optimization location as Instant Form, Upgraded Smart\+ Lead Generation Campaign with optimization location as Website, Upgraded Smart\+ Lead Generation Campaign with optimization location as TikTok direct messages, Upgraded Smart\+ Lead Generation Campaign with optimization location as instant messaging apps, Upgraded Smart\+ Lead Generation Campaign with optimization location as phone call, Upgraded Smart\+ Automotive Ads, or Upgraded Smart\+ ([^\n\.]+)\.',
     r'Dựa trên tùy chọn của bạn về việc có sử dụng danh mục và vị trí tối ưu hóa hay không, bạn có thể tạo Chiến dịch Tìm kiếm khách hàng tiềm năng Upgraded Smart+ với vị trí tối ưu hóa là Biểu mẫu tức thì, Trang web, Tin nhắn trực tiếp TikTok, Ứng dụng nhắn tin tức thì, Cuộc gọi điện thoại, Quảng cáo ô tô Upgraded Smart+ hoặc \1.'),
    (r'An Upgraded Smart\+ Lead Generation Campaign with Location as Instant Form is an Upgraded Smart\+ Lead Generation Campaign with `promotion_target_type` set to `INSTANT_PAGE`\.',
     'Chiến dịch Tìm kiếm khách hàng tiềm năng Upgraded Smart+ với Vị trí là Biểu mẫu tức thì là Chiến dịch Tìm kiếm khách hàng tiềm năng Upgraded Smart+ với `promotion_target_type` được đặt thành `INSTANT_PAGE`.'),
    (r'An Upgraded Smart\+ Lead Generation Campaign with Location as Website is an Upgraded Smart\+ Lead Generation Campaign with `promotion_target_type` set to `EXTERNAL_WEBSITE`\.',
     'Chiến dịch Tìm kiếm khách hàng tiềm năng Upgraded Smart+ với Vị trí là Trang web là Chiến dịch Tìm kiếm khách hàng tiềm năng Upgraded Smart+ với `promotion_target_type` được đặt thành `EXTERNAL_WEBSITE`.'),

    # 4. RTA details
    (r'The available placements at the ad group level might vary based on your RTA setting\.',
     'Các vị trí hiển thị khả dụng ở cấp nhóm quảng cáo có thể khác nhau dựa trên cài đặt RTA của bạn.'),
    (r'Specify one of the RTA IDs associated with your ad account\. To obtain the list of RTA IDs associated with your ad account, contact your TikTok representative\.\s*\*\*Note\*\*: The available placement setting \(placement_type and placements\) at the ad group level might vary based on your rta_id configuration\.',
     'Chỉ định một trong các ID RTA liên kết với tài khoản quảng cáo của bạn. Để lấy danh sách các ID RTA liên kết với tài khoản quảng cáo của bạn, vui lòng liên hệ đại diện TikTok của bạn. **Lưu ý**: Cài đặt vị trí hiển thị khả dụng (`placement_type` và `placements`) ở cấp nhóm quảng cáo có thể thay đổi dựa trên cấu hình `rta_id` của bạn.'),
    (r'Specify \*\*a catalog with at least two approved products\*\* \*\*Note\*\*:\s*• When RTA is disabled at the campaign level, you can specify any of the following catalog types:\s*• E-commerce\s*• hotel\s*• flight\s*• destination\s*• entertainment\s*• generic\s*• When RTA is enabled at the campaign level, you can specify any of the following catalog types:\s*• E-commerce\s*• entertainment\s*• generic',
     'Chỉ định **một danh mục có ít nhất hai sản phẩm đã được phê duyệt** **Lưu ý**: • Khi RTA bị tắt ở cấp chiến dịch, bạn có thể chỉ định bất kỳ loại danh mục nào sau đây: • E-commerce (Thương mại điện tử) • hotel (khách sạn) • flight (chuyến bay) • destination (điểm đến) • entertainment (giải trí) • generic (chung) • Khi RTA được bật ở cấp chiến dịch, bạn có thể chỉ định bất kỳ loại danh mục nào sau đây: • E-commerce • entertainment • generic'),

    # 5. App & Tracking specifics
    (r'VALUE \(with optimization_event specified\)\s*• When you set this field to VALUE, specify the placement parameters \(placement_type or both placement_type and placements\) at the same time\.\s*• Tìm hiểu thêm về \[Tối ưu hóa dựa trên giá trị \(Value-Based Optimization\)\]\(([^\)]+)\)\.',
     r'VALUE (với `optimization_event` được chỉ định) • Khi bạn đặt trường này thành `VALUE`, hãy chỉ định đồng thời các tham số vị trí hiển thị (`placement_type` hoặc cả `placement_type` và `placements`). • Tìm hiểu thêm về [Tối ưu hóa dựa trên giá trị (Value-Based Optimization)](\1).'),
    (r'A Standard Event throughoptimization_event', 'Một Sự kiện tiêu chuẩn qua `optimization_event`'),
    (r'To confirm the eligibility of the Custom Conversion for ad group creation:\s*• Ensure the returned optimization_event matches the optimization_event specified during ad group creation\.\s*• Đảm bảo `activity_status` là `NO_RECENT_ACTIVITY` hoặc `ACTIVE`\.',
     'Để xác nhận tính đủ điều kiện của Chuyển đổi tùy chỉnh cho việc tạo nhóm quảng cáo: • Đảm bảo `optimization_event` trả về khớp với `optimization_event` được chỉ định trong quá trình tạo nhóm quảng cáo. • Đảm bảo `activity_status` là `NO_RECENT_ACTIVITY` hoặc `ACTIVE`.'),
    (r'If optimization_goal is CLICK, INSTALL, or IN_APP_EVENT:\s*• Đặt `bid_type` thành `BID_TYPE_CUSTOM` \(Giới hạn chi phí\) hoặc `BID_TYPE_NO_BID` \(Phân phối tối đa\)\. Không chỉ định deep_bid_type và roas_bid\.',
     'Nếu `optimization_goal` là `CLICK`, `INSTALL` hoặc `IN_APP_EVENT`: • Đặt `bid_type` thành `BID_TYPE_CUSTOM` (Giới hạn chi phí) hoặc `BID_TYPE_NO_BID` (Phân phối tối đa). Không chỉ định `deep_bid_type` và `roas_bid`.'),
    (r'Không chỉ định deep_bid_type và roas_bid\.', 'Không chỉ định `deep_bid_type` và `roas_bid`.'),
    (r'Không chỉ định conversion_bid_price và bid_price\.', 'Không chỉ định `conversion_bid_price` và `bid_price`.'),

    # 6. Messaging app accounts in Business Center
    (r'Tài sản sáng tạo · IdentityMột trong các tùy chọn sau: • Authorized User • TikTok User • TikTok Account User in Business Centeridentity_type',
     '| Tài sản sáng tạo · Danh tính (Identity) | Một trong các tùy chọn sau: • Người dùng được ủy quyền (Authorized User) • Người dùng TikTok (TikTok User) • Người dùng tài khoản TikTok trong Business Center | `identity_type` |'),
    (r'Message template \(Welcome message\)Bật Chào đón mọi người bằng tin nhắn tự động do tài khoản TikTok gửi',
     '| Mẫu tin nhắn (Tin nhắn chào mừng) | Bật | Chào đón mọi người bằng tin nhắn tự động do tài khoản TikTok gửi |'),
    (r'Message template \(Welcome message\)Bật', '| Mẫu tin nhắn (Tin nhắn chào mừng) | Bật |'),
    (r'Chi tiết nguồn sản phẩm · Sản phẩmMột trong các tùy chọn: • Tất cả sản phẩm • Bộ sản phẩm \(Product set\) • Sản phẩm cụ thể \(tối đa 20 sản phẩm\)',
     '| Chi tiết nguồn sản phẩm · Sản phẩm | Một trong các tùy chọn: • Tất cả sản phẩm • Bộ sản phẩm (Product set) • Sản phẩm cụ thể (tối đa 20 sản phẩm) |'),

    # 7. Add-on types: Countdown Sticker / Gift Code Sticker
    (r'Không chỉ định hoặc chỉ định tối đa một ID thuộc bất kỳ loại tiện ích bổ sung nào sau đây:\s*• Countdown Sticker\s*• Gift Code Sticker',
     'Không chỉ định hoặc chỉ định tối đa một ID thuộc bất kỳ loại tiện ích bổ sung nào sau đây: • Nhãn dán đếm ngược (Countdown Sticker) • Nhãn dán mã quà tặng (Gift Code Sticker)'),
    (r'Tắt hoặc bật \(Disabled hoặc Enabled\) with up to one add-on in any of the following types:\s*• Countdown Sticker\s*• Gift Code Sticker',
     'Tắt hoặc bật (Disabled hoặc Enabled) với tối đa một tiện ích bổ sung thuộc bất kỳ loại nào sau đây: • Nhãn dán đếm ngược (Countdown Sticker) • Nhãn dán mã quà tặng (Gift Code Sticker)'),
    (r'Tắt hoặc bật \(Disabled hoặc Enabled\) with up to one add-on in any of the following types:\s*• Display Card',
     'Tắt hoặc bật (Disabled hoặc Enabled) với tối đa một tiện ích bổ sung thuộc bất kỳ loại nào sau đây: • Thẻ hiển thị (Display Card)'),
    (r'Không chỉ định hoặc chỉ định tối đa một ID thuộc bất kỳ loại tiện ích bổ sung nào sau đây:\s*• Display Card',
     'Không chỉ định hoặc chỉ định tối đa một ID thuộc bất kỳ loại tiện ích bổ sung nào sau đây: • Thẻ hiển thị (Display Card)'),

    # 8. Product video URLs
    (r'Tắt hoặc bật \(Disabled hoặc Enabled\) with one to two\s+of the following types:\s*• \*\*Image\*\*\s*• \*\*Product video URL\*\*',
     'Tắt hoặc bật (Disabled hoặc Enabled) với một đến hai loại sau: • **Hình ảnh (Image)** • **URL video sản phẩm (Product video URL)**'),
    (r'Tắt hoặc bật \(Disabled hoặc Enabled\) with one to two\s+of the following types:\s*• \*\*Image\*\*\s*• \*\*Video\*\*',
     'Tắt hoặc bật (Disabled hoặc Enabled) với một đến hai loại sau: • **Hình ảnh (Image)** • **Video**'),
    (r'Chi tiết nguồn sản phẩm · CatalogSpecify an\*\*\s*E-commerce catalog with at least one approved product\*\*catalog_id catalog_authorized_bc_id',
     '| Chi tiết nguồn sản phẩm · Danh mục (Catalog) | Chỉ định **danh mục Thương mại điện tử có ít nhất một sản phẩm đã được phê duyệt** | `catalog_id`, `catalog_authorized_bc_id` |'),
    (r'Chi tiết nguồn sản phẩm · CatalogSpecify \*\*an entertainment catalog with at least one approved product\*\*catalog_id catalog_authorized_bc_id',
     '| Chi tiết nguồn sản phẩm · Danh mục (Catalog) | Chỉ định **một danh mục giải trí có ít nhất một sản phẩm đã được phê duyệt** | `catalog_id`, `catalog_authorized_bc_id` |'),

    # 9. Third-party tracking Android click
    (r'Third-party tracking settings · Click tracking URL for Android \*\((Không bắt buộc|Optional)\)\*Disabled or enabledapp_id app_type click_tracking_url',
     '| Cài đặt theo dõi bên thứ ba · URL theo dõi lượt nhấp cho Android *(Không bắt buộc)* | Bật hoặc tắt | `app_id`, `app_type`, `click_tracking_url` |'),
    (r'Third-party tracking settings · Impression tracking URL for Android \*\((Không bắt buộc|Optional)\)\*Disabled or enabledapp_id app_type impression_tracking_url',
     '| Cài đặt theo dõi bên thứ ba · URL theo dõi lượt hiển thị cho Android *(Không bắt buộc)* | Bật hoặc tắt | `app_id`, `app_type`, `impression_tracking_url` |'),
    (r'Third-party tracking settings · Click tracking URL for iOS \*\((Không bắt buộc|Optional)\)\*Disabled or enabledapp_id app_type click_tracking_url',
     '| Cài đặt theo dõi bên thứ ba · URL theo dõi lượt nhấp cho iOS *(Không bắt buộc)* | Bật hoặc tắt | `app_id`, `app_type`, `click_tracking_url` |'),
    (r'Third-party tracking settings · Impression tracking URL for iOS \*\((Không bắt buộc|Optional)\)\*Disabled or enabledapp_id app_type impression_tracking_url',
     '| Cài đặt theo dõi bên thứ ba · URL theo dõi lượt hiển thị cho iOS *(Không bắt buộc)* | Bật hoặc tắt | `app_id`, `app_type`, `impression_tracking_url` |'),
]
