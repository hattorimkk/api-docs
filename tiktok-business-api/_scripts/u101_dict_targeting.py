#!/usr/bin/env python3
"""
Từ điển cho phần Nhắm mục tiêu, Đối tượng & Vị trí hiển thị (Targeting, Audience & Placements)
"""

TARGETING_RULES = [
    (r'Optimization and bidding · Location', 'Tối ưu hóa và Đấu thầu · Vị trí địa lý (Location)'),
    (r'Audience targeting · Age', 'Nhắm mục tiêu đối tượng · Độ tuổi (Age)'),
    (r'Disabled or enabled with a valid deeplink\. A deferred deeplink sends the user to a specific page when they open your app for the first time\.',
     'Tắt hoặc bật với một liên kết sâu (deeplink) hợp lệ. Liên kết sâu trì hoãn (deferred deeplink) sẽ điều hướng người dùng đến một trang cụ thể khi họ mở ứng dụng của bạn lần đầu tiên.'),
    (r'Not specified or specify one or more of the following values: • LEMON8 • PINE_DRAMA \*\*Note\*\*:  • Using the Lemon8 subplacement is an allowlist-only feature\. If you would like to access it, please contact your TikTok representative\.',
     'Không chỉ định hoặc chỉ định một hoặc nhiều giá trị sau: • LEMON8 • PINE_DRAMA **Lưu ý**: • Việc sử dụng vị trí phụ Lemon8 là tính năng chỉ dành cho danh sách cho phép (allowlist-only). Nếu bạn muốn truy cập, vui lòng liên hệ với đại diện TikTok của bạn.'),
    (r'\| Age targeting \| Audiences younger than 18 years old can\'t be targeted\. \| `age_groups` \| Do not pass the value `AGE_13_17`\.',
     '| Nhắm mục tiêu theo độ tuổi | Không thể nhắm mục tiêu đến đối tượng dưới 18 tuổi. | `age_groups` | Không truyền giá trị `AGE_13_17`.'),
    (r'\*\*Select Placement\*\* with TikTok placement only',
     '**Chọn vị trí hiển thị** chỉ với vị trí TikTok'),
    (r'Audiences younger than 18 years old can\'t be targeted\.',
     'Không thể nhắm mục tiêu đến đối tượng dưới 18 tuổi.'),
    (r'Do not pass the value AGE_13_17\.', 'Không truyền giá trị AGE_13_17.'),
    (r'Pangle block list', 'Danh sách chặn Pangle (Pangle block list)'),
    (r'Audience targeting • Automatic targeting', 'Nhắm mục tiêu đối tượng · Nhắm mục tiêu tự động'),
    (r'Any of the following types: • \*\*Automatic Placement\*\* • \*\*Select specific placements\*\*: • TikTok • Global App Bundle • Pangle',
     'Một trong các loại sau: • **Vị trí tự động (Automatic Placement)** • **Chọn vị trí cụ thể (Select specific placements)**: • TikTok • Global App Bundle • Pangle'),
    (r'When placement_type is PLACEMENT_TYPE_NORMAL and placements includes PLACEMENT_TIKTOK: • Not specified or specify one or more of the following values: • LEMON8 • PINE_DRAMA \*\*Note\*\*:  • Using the Lemon8 subplacement is an allowlist-only feature\. If you would like to access it, please contact your TikTok representative\.',
     'Khi placement_type là PLACEMENT_TYPE_NORMAL và placements bao gồm PLACEMENT_TIKTOK: • Không chỉ định hoặc chỉ định một hoặc nhiều giá trị sau: • LEMON8 • PINE_DRAMA **Lưu ý**: • Sử dụng vị trí phụ Lemon8 là tính năng chỉ dành cho danh sách cho phép (allowlist-only). Nếu bạn muốn truy cập, vui lòng liên hệ với đại diện TikTok của bạn.'),
    (r'Custom targeting \(targeting_optimization_mode as MANUAL\)',
     'Nhắm mục tiêu tùy chỉnh (targeting_optimization_mode là MANUAL)'),
    (r'Placements · Allow video download', 'Vị trí hiển thị · Cho phép tải xuống video'),
    (r'Placements · Allow video sharing', 'Vị trí hiển thị · Cho phép chia sẻ video'),
    (r'• To use Automatic Placement, do not specify placement_type and placements\. • The system will automatically configure placements to get you the best results\. • To select specific placements, specify placement_type and placements\.',
     '• Để sử dụng Vị trí tự động, không chỉ định placement_type và placements. • Hệ thống sẽ tự động cấu hình các vị trí để mang lại kết quả tốt nhất cho bạn. • Để chọn vị trí cụ thể, hãy chỉ định placement_type và placements.'),
    (r'Gender targeting in Smart\+ Campaigns is an allowlist-only feature\. If you would like to access it, please contact your TikTok representative\.',
     'Nhắm mục tiêu theo giới tính trong Chiến dịch Smart+ là tính năng chỉ dành cho danh sách cho phép (allowlist-only). Nếu bạn muốn sử dụng, vui lòng liên hệ với đại diện TikTok của bạn.'),
    (r'The location should match or be the subset of the targeting location of your catalog\.',
     'Vị trí địa lý phải khớp hoặc là tập con của vị trí nhắm mục tiêu trong danh mục sản phẩm của bạn.'),
]
