#!/usr/bin/env python3
"""
Cluster 1 translations:
- 1758526151905281: Campaign creation
- 1782086026530817: Create Traffic ads
- 1782086241778690: Optimize Destination Visit in Traffic ads
- 1808164002093058: Create Community Interaction ads
- 1772549012687873: Create App Pre-Registration ads
"""

CLUSTER1_RULES = [
    # TOC & Intro Doc 1
    (r'This chapter consists of the following use cases:', 'Chương này bao gồm các tình huống sử dụng (use case) sau:'),
    (r'- \[Create Lưu lượng truy cập \(Traffic\) ads\]', '- [Tạo quảng cáo Lưu lượng truy cập (Create Traffic ads)]'),
    (r'- \[Create Tương tác cộng đồng \(Community Interaction\) ads\]', '- [Tạo quảng cáo Tương tác cộng đồng (Create Community Interaction ads)]'),
    (r'- \[Create Đăng ký trước ứng dụng \(App Pre-Registration\) ads\]', '- [Tạo quảng cáo Đăng ký trước ứng dụng (Create App Pre-Registration ads)]'),
    (r'- \[Create Tìm kiếm khách hàng tiềm năng \(Lead Generation\) ads\]', '- [Tạo quảng cáo Tìm kiếm khách hàng tiềm năng (Create Lead Generation ads)]'),
    (r'- \[Create Website conversions ads\]', '- [Tạo quảng cáo Chuyển đổi trên trang web (Create Website Conversions ads)]'),
    (r'- \[Create Shopping Ads\]', '- [Tạo quảng cáo Mua sắm (Create Shopping Ads)]'),
    (r'- \[Set up Tiếp cận & Tần suất \(Reach & Frequency\) campaigns\]', '- [Thiết lập chiến dịch Tiếp cận & Tần suất (Set up Reach & Frequency campaigns)]'),
    (r'- \[Create Chiến dịch GMV Max \(GMV Max Campaigns\)\]', '- [Tạo chiến dịch GMV Max (Create GMV Max Campaigns)]'),
    (r'- \[Create Smart\+ Campaigns\]', '- [Tạo chiến dịch Smart+ (Create Smart+ Campaigns)]'),
    (r'- \[Create Upgraded Smart\+ Campaigns\]', '- [Tạo chiến dịch Upgraded Smart+ (Create Upgraded Smart+ Campaigns)]'),

    # Traffic Ads (1782086026530817 & 1782086241778690)
    (r'Bài viết này hướng dẫn bạn từng bước để tạo Lưu lượng truy cập \(Traffic\) ads\.',
     'Bài viết này hướng dẫn bạn từng bước để tạo quảng cáo Lưu lượng truy cập (Traffic ads).'),
    (r'Bài viết này hướng dẫn bạn từng bước để tạo a Lưu lượng truy cập \(Traffic\) ad with optimization goal Lượt truy cập đích \(Destination Visit\)\.',
     'Bài viết này hướng dẫn bạn từng bước để tạo quảng cáo Lưu lượng truy cập (Traffic ad) với mục tiêu tối ưu hóa là Lượt truy cập đích (Destination Visit).'),
    (r'Lưu lượng truy cập \(Traffic\) is an ad objective that drives people to a destination\. For instance, you can send people to your website, an event page, or your app\'s download page\.',
     'Lưu lượng truy cập (Traffic) là một mục tiêu quảng cáo giúp điều hướng người dùng đến một điểm đích. Ví dụ: bạn có thể đưa người dùng đến trang web của mình, một trang sự kiện hoặc trang tải xuống ứng dụng của bạn.'),
    (r'\*\*You can use Campaign Management API to create Lưu lượng truy cập \(Traffic\) ads, and this helps you streamline your ad creation workflow and manage ads at scale\.\*\*',
     '**Bạn có thể sử dụng Campaign Management API để tạo quảng cáo Lưu lượng truy cập (Traffic ads), giúp tối ưu hóa quy trình tạo quảng cáo và quản lý quảng cáo trên quy mô lớn.**'),
    (r'Để tạo Lưu lượng truy cập \(Traffic\) ads, bạn cần được cấp các quyền hạn tương ứng\. Xem \*\*API Reference\*\* trong tài liệu để biết thêm chi tiết\.',
     'Để tạo quảng cáo Lưu lượng truy cập (Traffic ads), bạn cần được cấp các quyền hạn tương ứng. Xem phần **API Reference** để biết thêm chi tiết.'),
    (r'The optimization goal Lượt truy cập đích \(Destination Visit\) is currently an allowlist-only feature\. If you would like to access it, please contact your TikTok representative\.',
     'Mục tiêu tối ưu hóa Lượt truy cập đích (Destination Visit) hiện là tính năng chỉ dành cho danh sách cho phép (allowlist-only). Nếu bạn muốn truy cập, vui lòng liên hệ với đại diện TikTok của bạn.'),
    (r'The optimization goal Lượt truy cập đích \(Destination Visit\) requires deeplinks at the ad level\.',
     'Mục tiêu tối ưu hóa Lượt truy cập đích (Destination Visit) yêu cầu liên kết sâu (deeplink) ở cấp mẫu quảng cáo.'),

    # Community Interaction Ads (1808164002093058)
    (r'Bài viết này hướng dẫn bạn từng bước để tạo Tương tác cộng đồng \(Community Interaction\) ads\.',
     'Bài viết này hướng dẫn bạn từng bước để tạo quảng cáo Tương tác cộng đồng (Community Interaction ads).'),
    (r'With the Tương tác cộng đồng \(Community Interaction\) objective, you can build and nurture your connections with one of the most engaged online communities in the world\.',
     'Với mục tiêu Tương tác cộng đồng (Community Interaction), bạn có thể xây dựng và nuôi dưỡng mối liên kết của mình với một trong những cộng đồng trực tuyến gắn kết nhất trên thế giới.'),
    (r'\*\*You can use Campaign Management API to create Tương tác cộng đồng \(Community Interaction\) ads, and this helps you streamline your ad creation workflow and manage ads at scale\.\*\*',
     '**Bạn có thể sử dụng Campaign Management API để tạo quảng cáo Tương tác cộng đồng (Community Interaction ads), giúp tối ưu hóa quy trình tạo quảng cáo và quản lý quảng cáo trên quy mô lớn.**'),
    (r'Để tạo Tương tác cộng đồng \(Community Interaction\) ads, bạn cần được cấp các quyền hạn tương ứng\. Xem \*\*API Reference\*\* trong tài liệu để biết thêm chi tiết\.',
     'Để tạo quảng cáo Tương tác cộng đồng (Community Interaction ads), bạn cần được cấp các quyền hạn tương ứng. Xem phần **API Reference** để biết thêm chi tiết.'),
    (r'• If optimization goal is specified as Follow at the ad group level, the destination is the TikTok account profile page\.',
     '• Nếu mục tiêu tối ưu hóa được chỉ định là Lượt theo dõi (Follow) ở cấp nhóm quảng cáo, điểm đến sẽ là trang hồ sơ tài khoản TikTok.'),
    (r'• If optimization_goal is set to FOLLOWERS at the ad group level, you don\'t need to pass tiktok_page_category, landing_page_url, and landing_page_url_list\.',
     '• Nếu `optimization_goal` được đặt thành `FOLLOWERS` ở cấp nhóm quảng cáo, bạn không cần truyền `tiktok_page_category`, `landing_page_url` và `landing_page_url_list`.'),
    (r'• If optimization goal is specified as Follow at the ad group level: Disabled\.\s*• If optimization goal is specified as Tiền thưởng lượt truy cập hồ sơ \(Profile visit\) at the ad group level: Disabled or enabled with the following type: • Reminder Countdown Sticker',
     '• Nếu mục tiêu tối ưu hóa là Lượt theo dõi (Follow) ở cấp nhóm quảng cáo: Tắt. • Nếu mục tiêu tối ưu hóa là Lượt truy cập hồ sơ (Profile visit) ở cấp nhóm quảng cáo: Tắt hoặc bật với loại sau: • Nhãn dán đếm ngược nhắc nhở (Reminder Countdown Sticker)'),
    (r'• If optimization_goal is set to FOLLOWERS at the ad group level, do not pass call_to_action and call_to_action_id\.\s*• If optimization_goal is set to PROFILE_VIEWS at the ad group level, specify call_to_action or call_to_action_id\.',
     '• Nếu `optimization_goal` được đặt thành `FOLLOWERS` ở cấp nhóm quảng cáo, không truyền `call_to_action` và `call_to_action_id`. • Nếu `optimization_goal` được đặt thành `PROFILE_VIEWS` ở cấp nhóm quảng cáo, hãy chỉ định `call_to_action` hoặc `call_to_action_id`.'),
    (r'Disabled or enabled with the following type: • Reminder Countdown Sticker \*\*Note\*\*: If you specify the TikTok subplacement \(PINE_DRAMA\), interactive add-on is not supported\.',
     'Tắt hoặc bật với loại sau: • Nhãn dán đếm ngược nhắc nhở (Reminder Countdown Sticker) **Lưu ý**: Nếu bạn chỉ định vị trí phụ TikTok (`PINE_DRAMA`), tiện ích tương tác bổ sung sẽ không được hỗ trợ.'),
    (r'Not passed or specify the ID of the following creative portfolio type: • Reminder Countdown Sticker \(sticker_type as REMINDER_COUNTDOWN_STICKER\)',
     'Không truyền hoặc chỉ định ID của loại danh mục sáng tạo sau: • Nhãn dán đếm ngược nhắc nhở (`sticker_type` là `REMINDER_COUNTDOWN_STICKER`)'),

    # App Pre-Registration Ads (1772549012687873)
    (r'Bài viết này hướng dẫn bạn từng bước để tạo Đăng ký trước ứng dụng \(App Pre-Registration\) ads\.',
     'Bài viết này hướng dẫn bạn từng bước để tạo quảng cáo Đăng ký trước ứng dụng (App Pre-Registration ads).'),
    (r'Đăng ký trước ứng dụng \(App Pre-Registration\) is a type of app promotion that encourages users to register ahead of a game release\. Upon the launch of the game, registered users will be notified so they can download the game immediately\.',
     'Đăng ký trước ứng dụng (App Pre-Registration) là một hình thức quảng bá ứng dụng khuyến khích người dùng đăng ký trước khi trò chơi phát hành. Khi trò chơi ra mắt, người dùng đã đăng ký sẽ nhận được thông báo để có thể tải trò chơi xuống ngay lập tức.'),
    (r'\*\*You can use Campaign Management API to create Đăng ký trước ứng dụng \(App Pre-Registration\) ads, and this helps streamline your ad creation workflow and manage ads at scale\.\*\*',
     '**Bạn có thể sử dụng Campaign Management API để tạo quảng cáo Đăng ký trước ứng dụng (App Pre-Registration ads), giúp tối ưu hóa quy trình tạo quảng cáo và quản lý quảng cáo trên quy mô lớn.**'),
    (r'Để tạo Đăng ký trước ứng dụng \(App Pre-Registration\) Ads, bạn cần được cấp các quyền hạn tương ứng\. Xem \*\*API Reference\*\* trong tài liệu để biết thêm chi tiết\.',
     'Để tạo quảng cáo Đăng ký trước ứng dụng (App Pre-Registration ads), bạn cần được cấp các quyền hạn tương ứng. Xem phần **API Reference** để biết thêm chi tiết.'),
    (r'Đăng ký trước ứng dụng \(App Pre-Registration\) is currently an allowlist-only feature\. If you would like to access it, please contact your TikTok representative\.',
     'Đăng ký trước ứng dụng (App Pre-Registration) hiện là tính năng chỉ dành cho danh sách cho phép (allowlist-only). Nếu bạn muốn truy cập, vui lòng liên hệ với đại diện TikTok của bạn.'),
]
