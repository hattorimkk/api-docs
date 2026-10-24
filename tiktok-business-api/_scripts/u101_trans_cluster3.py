#!/usr/bin/env python3
"""
Cluster 3 translations: Shopping Ads, GMV Max Migration, VSA, Catalog Ads, Showcase, LIVE Shopping
- 1741942179356738: Create Shopping Ads
- 1837161048383489: Migrate to GMV Max Campaigns
- 1741942291730434: Create Video Shopping Ads
- 1750361698613249: Create Catalog Ads
- 1774519076905985: Configure destination and deeplink settings for website-promoting Video Shopping Ads
- 1775099621140482: Optimize Landing page view in Video Shopping Ads
- 1782087855154177: Optimize Destination visit in Video Shopping Ads
- 1750361719059457: (To-be-deprecated) Create Video Shopping Ads with products from TikTok Commerce
- 1759232259360770: Create Video Shopping Ads with products from Showcase
- 1754162402455554: Create Live Shopping Ads
- 1785886237030401: (To-be-deprecated) Create Product Shopping Ads
- 1754726939130882: Migrate to Video Shopping Ads
- 1742003478618114: (To be deprecated) Create Catalog Listing Ads
"""

CLUSTER3_RULES = [
    # Shopping Ads Overview (1741942179356738)
    (r'Bài viết này hướng dẫn bạn từng bước để tạo Shopping Ads\.',
     'Bài viết này hướng dẫn bạn từng bước để tạo Quảng cáo Mua sắm (Shopping Ads).'),
    (r'Shopping Ads is a catalog powered, smarter, and simplified paid advertising solution designed to drive sales on TikTok\.',
     'Quảng cáo Mua sắm (Shopping Ads) là giải pháp quảng cáo trả phí thông minh, đơn giản hóa dựa trên danh mục sản phẩm, được thiết kế để thúc đẩy doanh số trên TikTok.'),
    (r'Shopping Ads consolidates the following major functions into one simple buying objective — \*\*Product Sales\*\*:',
     'Quảng cáo Mua sắm hợp nhất các chức năng chính sau đây vào một mục tiêu mua hàng đơn giản duy nhất — **Bán sản phẩm (Product Sales)**:'),
    (r'\* \*\*Quảng cáo mua sắm qua video \(Video Shopping Ads\) \(for Catalog or for TikTok Shop\)\*\*: A smart, catalog-powered video shopping solution to maximize conversion on TikTok\.',
     '* **Quảng cáo mua sắm qua video (Video Shopping Ads) (dành cho Danh mục hoặc TikTok Shop)**: Giải pháp mua sắm qua video thông minh dựa trên danh mục nhằm tối đa hóa tỷ lệ chuyển đổi trên TikTok.'),

    # GMV Max Migration (1837161048383489)
    (r'\*\*If you are creating TikTok Shop Ads, read this document to find out the changes and actions you should take\.\*\*',
     '**Nếu bạn đang tạo Quảng cáo TikTok Shop, hãy đọc tài liệu này để tìm hiểu các thay đổi và hành động bạn cần thực hiện.**'),
    (r'## Background', '## Bối cảnh (Background)'),
    (r'# Background', '## Bối cảnh (Background)'),
    (r'## What\'s changing', '## Những thay đổi (What\'s changing)'),
    (r'# What\'s changing', '## Những thay đổi (What\'s changing)'),
    (r'### Impact by TikTok Shop Ads types', '### Tác động theo loại Quảng cáo TikTok Shop'),
    (r'The following table outlines the impact by TikTok Shop Ads types and their corresponding configurations:',
     'Bảng sau đây nêu rõ tác động theo từng loại Quảng cáo TikTok Shop và các cấu hình tương ứng:'),

    # VSA Overview (1741942291730434)
    (r'You can create Quảng cáo mua sắm qua video \(Video Shopping Ads\) with products from catalogs, TikTok Shop, or Showcase\.',
     'Bạn có thể tạo Quảng cáo mua sắm qua video (Video Shopping Ads) với các sản phẩm từ danh mục, TikTok Shop hoặc Showcase.'),
    (r'Use the following resources to learn more about how to create Quảng cáo mua sắm qua video \(Video Shopping Ads\):',
     'Sử dụng các tài nguyên sau để tìm hiểu thêm về cách tạo Quảng cáo mua sắm qua video (Video Shopping Ads):'),
    (r'\* \[Create Quảng cáo danh mục \(Catalog Ads\)\]', '* [Tạo Quảng cáo danh mục (Create Catalog Ads)]'),
    (r'\* \[Configure destination and deeplink settings for website-promoting Quảng cáo mua sắm qua video \(Video Shopping Ads\)\]',
     '* [Cấu hình cài đặt điểm đến và liên kết sâu cho Quảng cáo mua sắm qua video quảng bá trang web]'),
    (r'\* \[Optimize Lượt xem trang đích \(Landing page view\) in Quảng cáo mua sắm qua video \(Video Shopping Ads\)\]',
     '* [Tối ưu hóa Lượt xem trang đích trong Quảng cáo mua sắm qua video]'),
    (r'\* \[Optimize Destination visit in Quảng cáo mua sắm qua video \(Video Shopping Ads\)\]',
     '* [Tối ưu hóa Lượt truy cập đích trong Quảng cáo mua sắm qua video]'),
    (r'\* \[\(Sắp ngừng hỗ trợ\) Tạo Quảng cáo mua sắm qua video \(Video Shopping Ads\) với sản phẩm từ TikTok Commerce\]',
     '* [(Sắp ngừng hỗ trợ) Tạo Quảng cáo mua sắm qua video với sản phẩm từ TikTok Commerce]'),
    (r'\* \[Tạo Quảng cáo mua sắm qua video \(Video Shopping Ads\) với sản phẩm từ Showcase\]',
     '* [Tạo Quảng cáo mua sắm qua video với sản phẩm từ Showcase]'),

    # Catalog Ads (1750361698613249)
    (r'Bài viết này giới thiệu cách thức tạo Quảng cáo danh mục \(Catalog Ads\) \(formerly known as Quảng cáo mua sắm qua video \(Video Shopping Ads\) with products from catalog\)\.',
     'Bài viết này giới thiệu cách tạo Quảng cáo danh mục (Catalog Ads) (trước đây gọi là Quảng cáo mua sắm qua video với các sản phẩm từ danh mục).'),
    (r'> Quảng cáo danh mục \(Catalog Ads\) are currently an allowlist-only feature for Commerce App advertisers\. If you would like to access it, please contact your TikTok representative\.',
     '> Quảng cáo danh mục (Catalog Ads) hiện là tính năng chỉ dành cho danh sách cho phép (allowlist-only) đối với các nhà quảng cáo Ứng dụng Thương mại. Nếu bạn muốn truy cập, vui lòng liên hệ với đại diện TikTok của bạn.'),

    # VSA Destination & Deeplink (1774519076905985)
    (r'This article introduces how to configure specific destination and deeplink settings for Quảng cáo mua sắm qua video \(Video Shopping Ads\) that promote websites\.',
     'Bài viết này giới thiệu cách định cấu hình cài đặt điểm đến và liên kết sâu (deeplink) cụ thể cho Quảng cáo mua sắm qua video (Video Shopping Ads) quảng bá trang web.'),
    (r'>\s*• Using deeplink in Shopping Ads that promote websites is currently an allowlist-only feature\. If you would like to access it, please contact your TikTok representative\.',
     '> • Sử dụng liên kết sâu (deeplink) trong Quảng cáo Mua sắm quảng bá trang web hiện là tính năng chỉ dành cho danh sách cho phép (allowlist-only). Nếu bạn muốn truy cập, vui lòng liên hệ với đại diện TikTok của bạn.'),
    (r'1\. \*\*Create a campaign\*\* using \[\/campaign\/create\/\]\(([^\)]+)\)\.',
     r'1. **Tạo chiến dịch** bằng cách sử dụng [/campaign/create/](\1).'),
    (r'The parameter requirements listed in the section \[Create Quảng cáo mua sắm qua video \(Video Shopping Ads\)\]\(([^\)]+)\) also apply here\.',
     r'Các yêu cầu về tham số được liệt kê trong phần [Tạo Quảng cáo mua sắm qua video (Video Shopping Ads)](\1) cũng áp dụng tại đây.'),
    (r'2\. \*\*Create and manage catalogs\.\*\* Follow the steps outlined in the section \[Create Quảng cáo mua sắm qua video \(Video Shopping Ads\)\]\(([^\)]+)\)\.',
     r'2. **Tạo và quản lý danh mục.** Làm theo các bước được phác thảo trong phần [Tạo Quảng cáo mua sắm qua video (Video Shopping Ads)](\1).'),

    # VSA LPV & Destination Visit (1775099621140482 & 1782087855154177)
    (r'Bài viết này giới thiệu cách thức tạo Quảng cáo mua sắm qua video \(Video Shopping Ads\) with optimization goal as Lượt xem trang đích \(Landing page view\)\.',
     'Bài viết này giới thiệu cách tạo Quảng cáo mua sắm qua video (Video Shopping Ads) với mục tiêu tối ưu hóa là Lượt xem trang đích (Landing page view).'),
    (r'Bài viết này giới thiệu cách thức tạo Quảng cáo mua sắm qua video \(Video Shopping Ads\) with optimization goal as Lượt truy cập đích \(Destination Visit\)\.',
     'Bài viết này giới thiệu cách tạo Quảng cáo mua sắm qua video (Video Shopping Ads) với mục tiêu tối ưu hóa là Lượt truy cập đích (Destination Visit).'),

    # TikTok Commerce (1750361719059457)
    (r'TikTok Commerce \(formerly known as TikTok Shopping\) is a suite of solutions, features, and advertising tools that gives brands the opportunity to tap into the power of commerce on TikTok\.',
     'TikTok Commerce (trước đây gọi là TikTok Shopping) là một bộ giải pháp, tính năng và công cụ quảng cáo mang đến cho các thương hiệu cơ hội khai thác sức mạnh của thương mại trên TikTok.'),
    (r'Bài viết này giới thiệu cách thức tạo Quảng cáo mua sắm qua video \(Video Shopping Ads\) with products from TikTok Commerce\.',
     'Bài viết này giới thiệu cách tạo Quảng cáo mua sắm qua video (Video Shopping Ads) với các sản phẩm từ TikTok Commerce.'),
    (r'> The flags of `Required`\/ `Conditional` in the following parameter tables are only applicable for Quảng cáo mua sắm qua video \(Video Shopping Ads\)\. If you want to configure other settings, refer to the related API reference\.',
     '> Các cờ `Bắt buộc`/`Có điều kiện` trong các bảng tham số sau chỉ áp dụng cho Quảng cáo mua sắm qua video (Video Shopping Ads). Nếu bạn muốn định cấu hình các cài đặt khác, hãy tham khảo tài liệu API liên quan.'),

    # Showcase (1759232259360770)
    (r'Showcase is a feature on TikTok that allows customers to shop directly from a seller’s or a creator’s account\.',
     'Showcase là một tính năng trên TikTok cho phép khách hàng mua sắm trực tiếp từ tài khoản của người bán hoặc người sáng tạo.'),
    (r'Bài viết này giới thiệu cách thức tạo Quảng cáo mua sắm qua video \(Video Shopping Ads\) with products from Showcase\.',
     'Bài viết này giới thiệu cách tạo Quảng cáo mua sắm qua video (Video Shopping Ads) với các sản phẩm từ Showcase.'),

    # Live Shopping Ads (1754162402455554)
    (r'Bài viết này giới thiệu cách thức tạo Quảng cáo mua sắm qua LIVE \(Live Shopping Ads\) \(LSA\)\.',
     'Bài viết này giới thiệu cách tạo Quảng cáo mua sắm qua LIVE (Live Shopping Ads - LSA).'),
    (r'Please see the table below for the available countries or regions that you can use Quảng cáo mua sắm qua LIVE \(Live Shopping Ads\):',
     'Vui lòng xem bảng dưới đây để biết các quốc gia hoặc khu vực khả dụng mà bạn có thể sử dụng Quảng cáo mua sắm qua LIVE (Live Shopping Ads):'),

    # Product Shopping Ads (1785886237030401)
    (r'Bài viết này hướng dẫn bạn từng bước để tạo Quảng cáo mua sắm sản phẩm \(Product Shopping Ads\) \(PSA\)\.',
     'Bài viết này hướng dẫn bạn từng bước để tạo Quảng cáo mua sắm sản phẩm (Product Shopping Ads - PSA).'),
    (r'> Audience size estimation is not available for PSA\.',
     '> Tính năng ước tính quy mô đối tượng không khả dụng cho PSA.'),

    # Migration to VSA (1754726939130882)
    (r'\*\*If you have created Collection Ads or Dynamic Showcase Ads before Feb\.16, 2023, please read this document to understand the migration to Quảng cáo mua sắm qua video \(Video Shopping Ads\)\.\*\*',
     '**Nếu bạn đã tạo Quảng cáo bộ sưu tập (Collection Ads) hoặc Dynamic Showcase Ads trước ngày 16 tháng 2 năm 2023, vui lòng đọc tài liệu này để hiểu quy trình chuyển đổi sang Quảng cáo mua sắm qua video (Video Shopping Ads).**'),
    (r'Starting from Feb\.16, 2023, you can no longer create Collection Ads or Dynamic Showcase Ads\.',
     'Kể từ ngày 16 tháng 2 năm 2023, bạn không thể tạo Quảng cáo bộ sưu tập hoặc Dynamic Showcase Ads nữa.'),
    (r'\* Existing Commerce catalog-based solutions, Dynamic Showcase Ads and Collection Ads, will be sunset\.',
     '* Các giải pháp dựa trên danh mục thương mại hiện tại, Dynamic Showcase Ads và Quảng cáo bộ sưu tập, sẽ ngừng hoạt động.'),
    (r'\* Core functionalities and benefits of Collection Ads or Dynamic Showcase Ads have been incorporated into Quảng cáo mua sắm qua video \(Video Shopping Ads\)\.',
     '* Các chức năng cốt lõi và lợi ích của Quảng cáo bộ sưu tập hoặc Dynamic Showcase Ads đã được tích hợp vào Quảng cáo mua sắm qua video (Video Shopping Ads).'),
    (r'\* At the end of this process, Quảng cáo mua sắm qua video \(Video Shopping Ads\) will be the dedicated ads solution\.',
     '* Khi quá trình này kết thúc, Quảng cáo mua sắm qua video (Video Shopping Ads) sẽ là giải pháp quảng cáo chuyên dụng duy nhất.'),

    # Catalog Listing Ads (1742003478618114)
    (r'Bài viết này giới thiệu cách thức tạo Quảng cáo danh sách danh mục \(Catalog Listing Ads\)\.',
     'Bài viết này giới thiệu cách tạo Quảng cáo danh sách danh mục (Catalog Listing Ads - CLA).'),
    (r'> \[!NOTE\] We are ending our Quảng cáo danh sách danh mục \(Catalog Listing Ads\) \(CLA\) soon and closing creation on June 18, 2024\.',
     '> [!NOTE] Chúng tôi sẽ sớm dừng hỗ trợ Quảng cáo danh sách danh mục (Catalog Listing Ads - CLA) và ngừng tính năng tạo mới vào ngày 18 tháng 6 năm 2024.'),
]
