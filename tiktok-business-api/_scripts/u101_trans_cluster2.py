#!/usr/bin/env python3
"""
Cluster 2 translations:
- 1739470742024193: Create Lead Generation ads
- 1774482920012801: Create Lead Gen ad with Instant Form
- 1774482976097281: Create Lead Gen ad with Website
- 1827752507854850: Create Automotive Ads for Inventory
- 1829635758164994: Create Automotive Ads for Models
- 1774482992153601: Create Lead Gen ad with TikTok direct messages
- 1774482999036930: Create Lead Gen ad with instant messaging apps
- 1774482936048641: Create Lead Gen ad with phone call
- 1775548501843970: Create Website Conversions ads
"""

CLUSTER2_RULES = [
    # Lead Gen Overview (1739470742024193)
    (r'Bài viết này hướng dẫn bạn từng bước để tạo Tìm kiếm khách hàng tiềm năng \(Lead Generation\) ads\.',
     'Bài viết này hướng dẫn bạn từng bước để tạo quảng cáo Tìm kiếm khách hàng tiềm năng (Lead Generation ads).'),
    (r'Tìm kiếm khách hàng tiềm năng \(Lead Generation\) is an ad objective through which advertisers can drive sales and generate high-intent leads\.',
     'Tìm kiếm khách hàng tiềm năng (Lead Generation) là một mục tiêu quảng cáo giúp các nhà quảng cáo thúc đẩy doanh số và thu hút khách hàng tiềm năng có ý định cao.'),
    (r'\*\*You can use Campaign Management API to create Tìm kiếm khách hàng tiềm năng \(Lead Generation\) ads, and this helps streamline your ad creation workflow and manage ads at scale\.\*\*',
     '**Bạn có thể sử dụng Campaign Management API để tạo quảng cáo Tìm kiếm khách hàng tiềm năng (Lead Generation ads), giúp tối ưu hóa quy trình tạo quảng cáo và quản lý quảng cáo trên quy mô lớn.**'),
    (r'The endpoints for lead generation ads can be divided into several categories:',
     'Các endpoint dành cho quảng cáo tìm kiếm khách hàng tiềm năng có thể được chia thành các danh mục sau:'),
    (r'\*\*Downloading leads\*\*', '**Tải xuống khách hàng tiềm năng (Downloading leads)**'),
    (r'\*\*Subscribing to leads\*\*', '**Đăng ký nhận khách hàng tiềm năng (Subscribing to leads)**'),
    (r'> To protect customer information, only ad account admins can create and query lead download tasks or download the leads\.',
     '> Để bảo vệ thông tin khách hàng, chỉ quản trị viên tài khoản quảng cáo mới có thể tạo và truy vấn các tác vụ tải xuống khách hàng tiềm năng hoặc tải xuống khách hàng tiềm năng.'),
    (r'- Để tìm hiểu về how to obtain leads from lead generation ads, see \[Obtain leads as advertisers\]\(([^\)]+)\)\.',
     r'- Để tìm hiểu cách nhận khách hàng tiềm năng từ quảng cáo tìm kiếm khách hàng tiềm năng, xem [Nhận khách hàng tiềm năng với tư cách là nhà quảng cáo](\1).'),

    # Lead Gen Instant Form (1774482920012801)
    (r'Bài viết này giới thiệu cách thức tạo a Tìm kiếm khách hàng tiềm năng \(Lead Generation\) ad with optimization location as Biểu mẫu tức thì \(Instant Form\)\.',
     'Bài viết này giới thiệu cách thức tạo quảng cáo Tìm kiếm khách hàng tiềm năng (Lead Generation ad) với vị trí tối ưu hóa là Biểu mẫu tức thì (Instant Form).'),
    (r'1\. Create an Biểu mẫu tức thì \(Instant Form\)\.\s*To create an Biểu mẫu tức thì \(Instant Form\), use \[Instant Page Editor SDK\]\(([^\)]+)\) or TikTok Ads Manager\.',
     r'1. Tạo Biểu mẫu tức thì (Instant Form). Để tạo Biểu mẫu tức thì, sử dụng [Instant Page Editor SDK](\1) hoặc TikTok Ads Manager.'),
    (r'2\. Call \[\/page\/get\/\]\(([^\)]+)\) to get the page ID via `page_id`\.',
     r'2. Gọi [/page/get/](\1) để lấy ID trang qua `page_id`.'),

    # Lead Gen Website (1774482976097281)
    (r'Bài viết này giới thiệu cách thức tạo a Tìm kiếm khách hàng tiềm năng \(Lead Generation\) ad with optimization location as Website\.',
     'Bài viết này giới thiệu cách tạo quảng cáo Tìm kiếm khách hàng tiềm năng (Lead Generation ad) với vị trí tối ưu hóa là Trang web (Website).'),
    (r'Based on your preference for using a catalog to promote car inventory or models, you have the flexibility to create three types of lead generation ads with website as the optimization location:',
     'Dựa trên sở thích sử dụng danh mục để quảng bá kho xe hoặc các dòng xe, bạn có thể linh hoạt tạo ba loại quảng cáo tìm kiếm khách hàng tiềm năng với vị trí tối ưu hóa là trang web:'),
    (r'- Standard Tìm kiếm khách hàng tiềm năng \(Lead Generation\) ads: This type of Tìm kiếm khách hàng tiềm năng \(Lead Generation\) ad requires manual input of vehicle information\.',
     '- Quảng cáo Tìm kiếm khách hàng tiềm năng Tiêu chuẩn (Standard Lead Generation ads): Loại quảng cáo này yêu cầu nhập thủ công thông tin phương tiện xe.'),
    (r'- Quảng cáo ô tô theo kho hàng \(Automotive Ads for Inventory\): This type of Tìm kiếm khách hàng tiềm năng \(Lead Generation\) ad automatically promotes all or selected vehicles based on the Auto-Inventory catalog\.',
     '- Quảng cáo ô tô theo kho hàng (Automotive Ads for Inventory): Loại quảng cáo này tự động quảng bá tất cả hoặc các phương tiện đã chọn dựa trên danh mục Auto-Inventory.'),
    (r'- Quảng cáo ô tô theo dòng xe \(Automotive Ads for Models\): This type of Tìm kiếm khách hàng tiềm năng \(Lead Generation\) ad automatically promotes car models based on the Auto-Model catalog\.',
     '- Quảng cáo ô tô theo dòng xe (Automotive Ads for Models): Loại quảng cáo này tự động quảng bá các dòng xe dựa trên danh mục Auto-Model.'),
    (r'# Create a Standard Tìm kiếm khách hàng tiềm năng \(Lead Generation\) ad with optimization location as Website',
     '## Tạo quảng cáo Tìm kiếm khách hàng tiềm năng Tiêu chuẩn với vị trí tối ưu hóa là Trang web'),

    # Automotive Inventory (1827752507854850)
    (r'Bài viết này hướng dẫn bạn từng bước để tạo Quảng cáo ô tô theo kho hàng \(Automotive Ads for Inventory\)\.',
     'Bài viết này hướng dẫn bạn từng bước để tạo Quảng cáo ô tô theo kho hàng (Automotive Ads for Inventory).'),
    (r'Quảng cáo ô tô theo kho hàng \(Automotive Ads for Inventory\) leverage the vehicle and dealership information stored in your Auto-Inventory catalog to automatically create and deliver ads showcasing specific car inventory, such as used or new cars\.',
     'Quảng cáo ô tô theo kho hàng (Automotive Ads for Inventory) tận dụng thông tin phương tiện và đại lý được lưu trữ trong danh mục Auto-Inventory của bạn để tự động tạo và phân phối quảng cáo giới thiệu kho xe cụ thể, chẳng hạn như xe đã qua sử dụng hoặc xe mới.'),
    (r'\*\*You can use Campaign Management API to create Quảng cáo ô tô theo kho hàng \(Automotive Ads for Inventory\), and this helps you streamline your ad creation workflow and manage ads at scale\.\*\*',
     '**Bạn có thể sử dụng Campaign Management API để tạo Quảng cáo ô tô theo kho hàng (Automotive Ads for Inventory), giúp tối ưu hóa quy trình tạo quảng cáo và quản lý quảng cáo trên quy mô lớn.**'),
    (r'Quảng cáo ô tô theo kho hàng \(Automotive Ads for Inventory\) with Single Video format',
     'Quảng cáo ô tô theo kho hàng (Automotive Ads for Inventory) với định dạng Video đơn (Single Video)'),
    (r'Quảng cáo ô tô theo kho hàng \(Automotive Ads for Inventory\) with Catalog Carousel format',
     'Quảng cáo ô tô theo kho hàng (Automotive Ads for Inventory) với định dạng Thẻ xoay vòng danh mục (Catalog Carousel)'),
    (r'- Creating Quảng cáo ô tô theo kho hàng \(Automotive Ads for Inventory\) requires setting up an Auto-Inventory catalog in Business Center first\.',
     '- Việc tạo Quảng cáo ô tô theo kho hàng (Automotive Ads for Inventory) yêu cầu phải thiết lập trước danh mục Auto-Inventory trong Trung tâm doanh nghiệp (Business Center).'),

    # Automotive Models (1829635758164994)
    (r'Bài viết này hướng dẫn bạn từng bước để tạo Quảng cáo ô tô theo dòng xe \(Automotive Ads for Models\)\.',
     'Bài viết này hướng dẫn bạn từng bước để tạo Quảng cáo ô tô theo dòng xe (Automotive Ads for Models).'),
    (r'Quảng cáo ô tô theo dòng xe \(Automotive Ads for Models\) leverage the model and offer information stored in your Auto-Model catalog to automatically create and deliver ads showcasing car models along with specific offers, such as incentives and discounts\.',
     'Quảng cáo ô tô theo dòng xe (Automotive Ads for Models) tận dụng thông tin dòng xe và ưu đãi được lưu trữ trong danh mục Auto-Model của bạn để tự động tạo và phân phối quảng cáo giới thiệu các dòng xe cùng với các ưu đãi cụ thể, chẳng hạn như chương trình khuyến mãi và giảm giá.'),
    (r'\*\*You can use Campaign Management API to create Quảng cáo ô tô theo dòng xe \(Automotive Ads for Models\), and this helps streamline your ad creation workflow and manage ads at scale\.\*\*',
     '**Bạn có thể sử dụng Campaign Management API để tạo Quảng cáo ô tô theo dòng xe (Automotive Ads for Models), giúp tối ưu hóa quy trình tạo quảng cáo và quản lý quảng cáo trên quy mô lớn.**'),

    # Lead Gen TikTok DM (1774482992153601)
    (r'Bài viết này giới thiệu cách thức tạo a Tìm kiếm khách hàng tiềm năng \(Lead Generation\) ad with optimization location as Tin nhắn trực tiếp TikTok \(TikTok direct messages\)\.',
     'Bài viết này giới thiệu cách tạo quảng cáo Tìm kiếm khách hàng tiềm năng (Lead Generation ad) với vị trí tối ưu hóa là Tin nhắn trực tiếp TikTok (TikTok direct messages).'),
    (r'>\s*• Creating a Tìm kiếm khách hàng tiềm năng \(Lead Generation\) ad with Tin nhắn trực tiếp TikTok \(Direct Messages\) as your optimization location is currently an allowlist-only feature\. If you would like to access it, please contact your TikTok representative\.',
     '> • Việc tạo quảng cáo Tìm kiếm khách hàng tiềm năng với Tin nhắn trực tiếp TikTok (Direct Messages) làm vị trí tối ưu hóa hiện là tính năng chỉ dành cho danh sách cho phép (allowlist-only). Nếu bạn muốn truy cập, vui lòng liên hệ với đại diện TikTok của bạn.'),
    (r'The owner of the authorized TikTok account has enabled the "Everyone" permission for Direct Messages in their TikTok app\. For detailed instructions, see \[Direct Messages on TikTok\]\(https:\/\/support\.tiktok\.com\/en\/using-tiktok\/messaging-and-notifications\/direct-messages\)\.',
     'Chủ sở hữu của tài khoản TikTok được ủy quyền đã bật quyền "Mọi người" (Everyone) cho Tin nhắn trực tiếp trong ứng dụng TikTok của họ. Để biết hướng dẫn chi tiết, xem [Tin nhắn trực tiếp trên TikTok](https://support.tiktok.com/en/using-tiktok/messaging-and-notifications/direct-messages).'),

    # Lead Gen Instant Messaging Apps (1774482999036930)
    (r'Bài viết này giới thiệu cách thức tạo a Tìm kiếm khách hàng tiềm năng \(Lead Generation\) ad with optimization location as Ứng dụng nhắn tin tức thì \(instant messaging apps\)\.',
     'Bài viết này giới thiệu cách tạo quảng cáo Tìm kiếm khách hàng tiềm năng (Lead Generation ad) với vị trí tối ưu hóa là Ứng dụng nhắn tin tức thì (instant messaging apps).'),
    (r'- If the audience has installed the instant messaging app \(such as WhatsApp\), they can send a message to start a conversation with the advertiser upon clicking the ad\'s CTA button\.',
     '- Nếu đối tượng mục tiêu đã cài đặt ứng dụng nhắn tin tức thì (chẳng hạn như WhatsApp), họ có thể gửi tin nhắn để bắt đầu cuộc trò chuyện với nhà quảng cáo khi nhấp vào nút CTA của quảng cáo.'),
    (r'- If the audience hasn\'t installed the instant messaging app, they will be directed to view a Custom Instant Page to get the phone number upon clicking the ad\'s CTA button\.',
     '- Nếu đối tượng mục tiêu chưa cài đặt ứng dụng nhắn tin tức thì, họ sẽ được chuyển hướng đến xem Trang tức thì tùy chỉnh (Custom Instant Page) để lấy số điện thoại khi nhấp vào nút CTA của quảng cáo.'),
    (r'>\s*• Creating a Tìm kiếm khách hàng tiềm năng \(Lead Generation\) ad with optimization location as Ứng dụng nhắn tin tức thì \(Instant Messaging Apps\) is currently an allowlist-only feature\. If you would like to access it, please contact your TikTok representative\.',
     '> • Việc tạo quảng cáo Tìm kiếm khách hàng tiềm năng với vị trí tối ưu hóa là Ứng dụng nhắn tin tức thì (Instant Messaging Apps) hiện là tính năng chỉ dành cho danh sách cho phép (allowlist-only). Nếu bạn muốn truy cập, vui lòng liên hệ với đại diện TikTok của bạn.'),
    (r'- We recommend connecting to one of our integrated \[Message Management Tools\]\(https:\/\/ads\.tiktok\.com\/help\/article\/lead-generation-with-instant-messaging-apps-faqs\) \(MMTs\) to manage customer queries at scale\.',
     '- Chúng tôi khuyến nghị bạn nên kết nối với một trong các [Công cụ quản lý tin nhắn (Message Management Tools)](https://ads.tiktok.com/help/article/lead-generation-with-instant-messaging-apps-faqs) (MMT) tích hợp của chúng tôi để quản lý các câu hỏi của khách hàng trên quy mô lớn.'),
    (r'- If you\'ve already integrated with an MMT and are optimizing for Conversations, make sure to set up message event sets and upload events to TikTok\.',
     '- Nếu bạn đã tích hợp với một MMT và đang tối ưu hóa cho Cuộc trò chuyện (Conversations), hãy đảm bảo thiết lập các bộ sự kiện tin nhắn và tải sự kiện lên TikTok.'),

    # Lead Gen Phone Call (1774482936048641)
    (r'Bài viết này giới thiệu cách thức tạo a Tìm kiếm khách hàng tiềm năng \(Lead Generation\) ad with optimization location as Cuộc gọi điện thoại \(phone call\)\.',
     'Bài viết này giới thiệu cách tạo quảng cáo Tìm kiếm khách hàng tiềm năng (Lead Generation ad) với vị trí tối ưu hóa là Cuộc gọi điện thoại (phone call).'),
    (r'> Creating a Tìm kiếm khách hàng tiềm năng \(Lead Generation\) ad with optimization location as Cuộc gọi điện thoại \(phone call\) is currently an allowlist-only feature\. If you would like to access it, please contact your TikTok representative\.',
     '> Việc tạo quảng cáo Tìm kiếm khách hàng tiềm năng với vị trí tối ưu hóa là Cuộc gọi điện thoại (phone call) hiện là tính năng chỉ dành cho danh sách cho phép (allowlist-only). Nếu bạn muốn truy cập, vui lòng liên hệ với đại diện TikTok của bạn.'),

    # Website Conversions (1775548501843970)
    (r'Bài viết này hướng dẫn bạn từng bước để tạo Chuyển đổi trên trang web \(Website Conversions\) ads\.',
     'Bài viết này hướng dẫn bạn từng bước để tạo quảng cáo Chuyển đổi trên trang web (Website Conversions ads).'),
    (r'The Web conversions campaign  empowers you to drive conversions on your website or TikTok Instant Page\.',
     'Chiến dịch Chuyển đổi trên trang web (Web conversions) giúp bạn thúc đẩy chuyển đổi trên trang web của mình hoặc Trang tức thì TikTok (TikTok Instant Page).'),
    (r'\*\*You can use Campaign Management API to create Chuyển đổi trên trang web \(Website Conversions\) ads, and this helps streamline your ad creation workflow and manage ads at scale\.\*\*',
     '**Bạn có thể sử dụng Campaign Management API để tạo quảng cáo Chuyển đổi trên trang web (Website Conversions ads), giúp tối ưu hóa quy trình tạo quảng cáo và quản lý quảng cáo trên quy mô lớn.**'),
    (r'For a comprehensive introduction to and best practices for Web Conversions ads, consult \[API for Business - Web Conversions Tutorial\]\(https:\/\/ads\.tiktok\.com\/marketing_api\/docs\?id=1738769164954626\)\.',
     'Để có phần giới thiệu toàn diện và các phương pháp hay nhất cho quảng cáo Chuyển đổi trên web, hãy tham khảo [API for Business - Hướng dẫn chuyển đổi trên web](https://ads.tiktok.com/marketing_api/docs?id=1738769164954626).'),
]
