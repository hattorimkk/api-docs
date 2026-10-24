#!/usr/bin/env python3
"""
Từ điển mệnh đề mở rộng phần 2 cho u102.
"""

CLAUSES2_RULES = [
    # Catalog verification & music
    (r'You can verify this by checking the value of approved returned from (\[\/catalog\/overview\/\]\([^\)]+\))(?:, which should be at least two)?\.',
     r'Bạn có thể xác minh điều này bằng cách kiểm tra giá trị `approved` trả về từ \1 (phải có ít nhất hai sản phẩm).'),

    (r'To obtain a valid music ID, you can use any of the following methods:\s*• Filter the pieces of music for Catalog Carousel Ads under an ad account by specifying music_scene as CATALOG_CAROUSEL in (\[\/file\/music\/get\/\]\([^\)]+\))\.\s*• Upload a piece of customized music for Catalog Carousel Ads to an ad account by using any of the following methods:\s*• Specify music_scene as CATALOG_CAROUSEL and pass music_file and music_signature in (\[\/file\/music\/upload\/\]\([^\)]+\))\.\s*• Specify music_scene as CATALOG_CAROUSEL, upload_type as UPLOAD_BY_FILE_ID, and pass file_id to (\[\/file\/music\/upload\/\]\([^\)]+\))\.',
     r'Để lấy ID bài nhạc hợp lệ, bạn có thể sử dụng bất kỳ phương pháp nào sau đây: • Lọc các bài nhạc cho Quảng cáo xoay vòng danh mục thuộc tài khoản quảng cáo bằng cách chỉ định `music_scene` là `CATALOG_CAROUSEL` trong \1. • Tải lên một bài nhạc tùy chỉnh cho Quảng cáo xoay vòng danh mục vào tài khoản quảng cáo bằng bất kỳ phương thức nào sau đây: • Chỉ định `music_scene` là `CATALOG_CAROUSEL` và truyền `music_file` cùng `music_signature` trong \2. • Chỉ định `music_scene` là `CATALOG_CAROUSEL`, `upload_type` là `UPLOAD_BY_FILE_ID`, và truyền `file_id` vào \3.'),

    (r'To obtain a valid music ID, you can use any of the following methods:\s*• Lọc các bài nhạc cho Quảng cáo xoay vòng danh mục thuộc tài khoản quảng cáo bằng cách chỉ định music_scene là CATALOG_CAROUSEL trong (\[\/file\/music\/get\/\]\([^\)]+\))\.\s*• Tải lên một bài nhạc tùy chỉnh cho Quảng cáo xoay vòng danh mục vào tài khoản quảng cáo bằng bất kỳ phương thức nào sau đây:\s*• Chỉ định music_scene là CATALOG_CAROUSEL và truyền music_file cùng music_signature trong (\[\/file\/music\/upload\/\]\([^\)]+\))\.\s*• Chỉ định music_scene là CATALOG_CAROUSEL, upload_type là UPLOAD_BY_FILE_ID, và truyền file_id trong (\[\/file\/music\/upload\/\]\([^\)]+\))\.',
     r'Để lấy ID bài nhạc hợp lệ, bạn có thể sử dụng bất kỳ phương pháp nào sau đây: • Lọc các bài nhạc cho Quảng cáo xoay vòng danh mục thuộc tài khoản quảng cáo bằng cách chỉ định `music_scene` là `CATALOG_CAROUSEL` trong \1. • Tải lên bài nhạc tùy chỉnh cho Quảng cáo xoay vòng danh mục vào tài khoản quảng cáo bằng bất kỳ phương pháp nào sau: • Chỉ định `music_scene` là `CATALOG_CAROUSEL` và truyền `music_file` cùng `music_signature` trong \2. • Chỉ định `music_scene` là `CATALOG_CAROUSEL`, `upload_type` là `UPLOAD_BY_FILE_ID`, và truyền `file_id` trong \3.'),

    # Landing page URL & UTM params
    (r'If you set landing_page_url_list to a URL that already includes URL parameters, you can optionally specify utm_params at the same time to store the URL parameters used in the URL\.',
     'Nếu bạn đặt `landing_page_url_list` thành một URL đã bao gồm các tham số URL, bạn có thể tùy chọn chỉ định `utm_params` cùng lúc để lưu trữ các tham số URL được sử dụng trong URL.'),

    (r'Whenlanding_page_url_list is specified:\s*• Chỉ định các giá trị hợp lệ hoặc không chỉ định\.If you set landing_page_url_list to a URL that already includes URL parameters, you can optionally specify utm_params at the same time to store the URL parameters used in the URL\.',
     'Khi `landing_page_url_list` được chỉ định: • Chỉ định các giá trị hợp lệ hoặc không chỉ định. Nếu bạn đặt `landing_page_url_list` thành một URL đã bao gồm các tham số URL, bạn có thể tùy chọn chỉ định `utm_params` cùng lúc để lưu trữ các tham số URL được sử dụng trong URL.'),

    # Catalog creatives toggle
    (r'To enable catalog creative settings:\s*• Set catalog_creative_toggle to true\.\s*• Provide one to three of the following values in catalog_media_settings:\s*• (IMAGE|VIDEO|TEMPLATE_VIDEO)',
     r'Để bật cài đặt mẫu sáng tạo danh mục: • Đặt `catalog_creative_toggle` thành `true`. • Cung cấp từ một đến ba giá trị sau trong `catalog_media_settings`: • \1'),

    (r'To disable catalog creative settings:\s*• Set catalog_creative_toggle to false\.\s*• Leave catalog_media_settings unspecified\.',
     'Để tắt cài đặt mẫu sáng tạo danh mục: • Đặt `catalog_creative_toggle` thành `false`. • Để trống `catalog_media_settings` không chỉ định.'),

    (r'Set catalog_creative_toggle to false\.\s*• Leave catalog_media_settings unspecified\.',
     'Đặt `catalog_creative_toggle` thành `false`. • Để trống `catalog_media_settings` không chỉ định.'),

    (r'Set catalog_creative_toggle to true\.\s*• Provide one to (?:three|two) of the following values in catalog_media_settings:',
     'Đặt `catalog_creative_toggle` thành `true`. • Cung cấp từ một đến các giá trị sau trong `catalog_media_settings`:'),

    # Direct messages identity permissions
    (r'If you want to use an identity in TikTok Direct Messaging Ads, you need to have direct message permission for the identity\. To confirm this, call (\[\/identity\/get\/\]\([^\)]+\)) or (\[\/identity\/info\/\]\([^\)]+\)) and check Liệu returned can_manage_message is true\.',
     r'Nếu bạn muốn sử dụng một danh tính trong Quảng cáo tin nhắn trực tiếp TikTok, bạn cần có quyền gửi tin nhắn trực tiếp cho danh tính đó. Để xác nhận điều này, hãy gọi \1 hoặc \2 và kiểm tra xem `can_manage_message` trả về có phải là `true` không.'),

    (r'If the returned can_manage_message is false and identity_type is TT_USER, you can navigate to \[the ad account user setting page\]\(https:\/\/ads\.tiktok\.com\/ac\/page\/settings\)\. In the \*\*Profile\*\* section of the \*\*Personal Info\*\* tab, click \*\*Edit access\*\* to edit your permissions for the associated TikTok account\. Ensure that you have \*\*"Read and manage messages in your inbox"\*\* permission for the TikTok account\.',
     'Nếu `can_manage_message` trả về là `false` và `identity_type` là `TT_USER`, bạn có thể điều hướng đến [trang cài đặt người dùng của tài khoản quảng cáo](https://ads.tiktok.com/ac/page/settings). Trong phần **Hồ sơ (Profile)** của tab **Thông tin cá nhân (Personal Info)**, nhấp vào **Chỉnh sửa quyền truy cập (Edit access)** để sửa đổi quyền cho tài khoản TikTok liên kết. Đảm bảo bạn đã có quyền **"Đọc và quản lý tin nhắn trong hộp thư đến"** đối với tài khoản TikTok này.'),

    (r'If the returned can_manage_message is false and identity_type is BC_AUTH_TT, you can ask the Business Center admin to grant you direct message permission for the TikTok account associated with the identity by using (\[\/bc\/asset\/assign\/\]\([^\)]+\))\. Set asset_type to TT_ACCOUNT and ensure that the tt_account_roles value includes at least POST and DIRECT_MESSAGE\.',
     r'Nếu `can_manage_message` trả về là `false` và `identity_type` là `BC_AUTH_TT`, bạn có thể yêu cầu quản trị viên Business Center cấp quyền gửi tin nhắn trực tiếp cho tài khoản TikTok được liên kết với danh tính bằng cách sử dụng \1. Đặt `asset_type` thành `TT_ACCOUNT` và đảm bảo giá trị `tt_account_roles` chứa tối thiểu `POST` và `DIRECT_MESSAGE`.'),

    (r'\*\*Note\*\*: Selecting a TikTok account at the ad group level in TikTok Direct Messaging Ads is currently an allowlist-only feature\. (Nếu bạn muốn truy cập|If you would like to access)[^\n]+',
     '**Lưu ý**: Việc chọn tài khoản TikTok ở cấp nhóm quảng cáo trong Quảng cáo tin nhắn trực tiếp TikTok hiện là tính năng chỉ dành cho danh sách cho phép (allowlist-only). Nếu bạn muốn truy cập tính năng này, vui lòng liên hệ với đại diện TikTok của bạn.'),

    # Video templates & catalog products
    (r'To learn about how to create video templates on TikTok Ads Manager, see \[How to create video packages in a Catalog\]\(https:\/\/ads\.tiktok\.com\/help\/article\/how-to-create-video-packages-in-a-catalog\)\.',
     'Để tìm hiểu cách tạo mẫu video trên Trình quản lý quảng cáo TikTok, hãy xem [Cách tạo gói video trong Danh mục](https://ads.tiktok.com/help/article/how-to-create-video-packages-in-a-catalog).'),

    (r'If you want to add video URLs for your catalog products, use (\[\/catalog\/product\/update\/\]\([^\)]+\))\.',
     r'Nếu bạn muốn thêm URL video cho các sản phẩm trong danh mục của mình, hãy sử dụng \1.'),

    (r'To retrieve the product ID \(product_id\) of each catalog product, use (\[\/catalog\/product\/get\/\]\([^\)]+\))\.',
     r'Để lấy ID sản phẩm (`product_id`) của từng sản phẩm trong danh mục, hãy sử dụng \1.'),

    # General constraints
    (r'if specified, should be the same for ad groups within the same campaign',
     'nếu được chỉ định, phải giống nhau giữa các nhóm quảng cáo trong cùng một chiến dịch'),

    (r'When you select a campaign budget mode, this setting must be the same across ad groups\.',
     'Khi bạn chọn chế độ ngân sách chiến dịch, cài đặt này phải giống nhau giữa các nhóm quảng cáo.'),

    (r'this setting must be the same across ad groups',
     'cài đặt này phải giống nhau giữa các nhóm quảng cáo'),

    (r'this setting is not supported', 'cài đặt này không được hỗ trợ'),

    (r'The campaign will not be bound by \[Dedicated Campaign quota limits\]\(([^\)]+)\) and you will be able to retrieve \[Self Attribution Network \(SAN\) metrics\]\(([^\)]+)\) for the campaign\. However, you cannot retrieve \[SKAN reporting metrics\]\(([^\)]+)\) for the campaign\. Learn more about \[SAN integration\]\(([^\)]+)\)\.',
     r'Chiến dịch sẽ không bị ràng buộc bởi [Giới hạn hạn ngạch Chiến dịch chuyên dụng](\1) và bạn sẽ có thể truy xuất [Chỉ số Mạng tự phân bổ (SAN)](\2) cho chiến dịch. Tuy nhiên, bạn không thể truy xuất [Chỉ số báo cáo SKAN](\3) cho chiến dịch. Tìm hiểu thêm về [Tích hợp SAN](\4).'),

    (r'The campaign will be bound by \[Dedicated Campaign quota limits\]\(([^\)]+)\) and you will be able to retrieve \[SKAN metrics\]\(([^\)]+)\) for the campaign\.',
     r'Chiến dịch sẽ bị ràng buộc bởi [Giới hạn hạn ngạch Chiến dịch chuyên dụng](\1) và bạn sẽ có thể truy xuất [Chỉ số SKAN](\2) cho chiến dịch.'),

    (r'\*\*Note\*\*: Disabling SKAN attribution for Dedicated Campaigns is currently an allowlist-only feature\. Nếu bạn muốn truy cập tính năng này, vui lòng liên hệ với đại diện TikTok của bạn\.',
     '**Lưu ý**: Việc vô hiệu hóa phân bổ SKAN cho Chiến dịch chuyên dụng hiện là tính năng chỉ dành cho danh sách cho phép (allowlist-only). Nếu bạn muốn truy cập tính năng này, vui lòng liên hệ với đại diện TikTok của bạn.'),
]
