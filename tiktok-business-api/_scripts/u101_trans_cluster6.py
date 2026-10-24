#!/usr/bin/env python3
"""
Cluster 6 translations: Upgraded Smart+ Web, Travel Ads, Streaming Ads, Mini Series Catalog Ads
- 1843309514567809: Upgraded Smart+ Web Campaigns overview
- 1847302878676994: Regular Upgraded Smart+ Web Campaign
- 1847302895272962: Upgraded Smart+ E-commerce Catalog Ads
- 1847302908327938: Upgraded Smart+ Travel Ads
- 1847302920924306: Upgraded Smart+ Streaming Ads
- 1847302935967746: Upgraded Smart+ Mini Series Catalog Ads
"""

CLUSTER6_RULES = [
    # Overview & Regular Web
    (r"Specify valid values or not specified\. If you set landing_page_url_list to a URL that already includes UTM parameters, you need to set custom_params to an empty string",
     "Chỉ định các giá trị hợp lệ hoặc không chỉ định. Nếu bạn đặt landing_page_url_list thành một URL đã bao gồm các tham số UTM, bạn cần đặt custom_params thành chuỗi rỗng"),
     
    (r"Specify an\*\* E-commerce catalog with at least two approved products\*\*",
     "Chỉ định **một danh mục Thương mại điện tử có ít nhất hai sản phẩm đã được phê duyệt**"),
     
    (r"Specify valid locations\. If a catalog is specified, the location should match or be the subset of the targeting location of your catalog\.",
     "Chỉ định các vị trí hợp lệ. Nếu danh mục được chỉ định, vị trí phải trùng khớp hoặc là tập con của vị trí nhắm mục tiêu của danh mục của bạn."),
     
    (r"Retarget · Custom audience \(Optional when an E-commerce catalog is used\)",
     "Nhắm mục tiêu lại · Đối tượng tùy chỉnh (Không bắt buộc khi sử dụng danh mục Thương mại điện tử)"),
     
    (r"Retarget · Custom audience · Include · Target anyone in catalog or custom audiences \(Optional when both an E-commerce catalog and custom audience are used\)",
     "Nhắm mục tiêu lại · Đối tượng tùy chỉnh · Bao gồm · Nhắm mục tiêu bất kỳ ai trong danh mục hoặc đối tượng tùy chỉnh (Không bắt buộc khi sử dụng cả danh mục Thương mại điện tử và đối tượng tùy chỉnh)"),
     
    (r"Disabled or enabled with one to three of the following types: • \*\*Video\*\* • \*\*Image\*\* • \*\*Video templates\*\*",
     "Đã tắt hoặc đã bật với một đến ba loại sau: • **Video** • **Hình ảnh (Image)** • **Mẫu video (Video templates)**"),
     
    (r"When you enable \*\*Video templates,\*\* select one of the following video template settings: • All video templates • Specific video templates",
     "Khi bạn bật **Mẫu video (Video templates)**, hãy chọn một trong các cài đặt mẫu video sau: • Tất cả mẫu video • Mẫu video cụ thể"),
     
    (r"When TEMPLATE_VIDEO is included in the catalog_media_settings value: • To select the \"All video templates\" option, do not pass catalog_template_id_list or set catalog_template_id_list to an empty array\. • To select the \"Specific video templates\" option, pass one to three video template IDs in catalog_template_id_list\.",
     "Khi TEMPLATE_VIDEO có trong giá trị catalog_media_settings: • Để chọn tùy chọn \"Tất cả mẫu video\", không truyền catalog_template_id_list hoặc đặt catalog_template_id_list thành mảng rỗng. • Để chọn tùy chọn \"Mẫu video cụ thể\", hãy truyền từ một đến ba ID mẫu video vào catalog_template_id_list."),
     
    (r"Use videos from your catalog to promote your products\.",
     "Sử dụng video từ danh mục của bạn để quảng bá sản phẩm."),
     
    (r"Enable \"Video\" in your catalog creative settings, allowing the system to use videos from your catalog\.",
     "Bật \"Video\" trong cài đặt mẫu quảng cáo danh mục của bạn, cho phép hệ thống sử dụng video từ danh mục của bạn."),
     
    (r"Ensure VIDEO is included in the catalog_media_settings value\.",
     "Đảm bảo VIDEO có trong giá trị catalog_media_settings."),
     
    (r"You need to configure a video URL for each catalog product\.",
     "Bạn cần cấu hình một URL video cho mỗi sản phẩm trong danh mục."),
     
    (r"Ensure that a video URL \(video_url\) has been configured for each catalog product\. • To ensure a video URL is configured for each product, configure the video URL for products when uploading products to your catalog through \[/catalog/product/upload/\]\(\.\./12-api-reference/28-catalog-products-p1\.md#doc-1740569766952962\)\.",
     "Đảm bảo rằng URL video (video_url) đã được cấu hình cho mỗi sản phẩm trong danh mục. • Để đảm bảo URL video được định cấu hình cho mỗi sản phẩm, hãy định cấu hình URL video cho sản phẩm khi tải sản phẩm lên danh mục của bạn qua [/catalog/product/upload/](../12-api-reference/28-catalog-products-p1.md#doc-1740569766952962)."),
     
    # Travel Ads
    (r"Upgraded Smart\+ Travel Ads are Upgraded Smart\+ Web Campaigns that use catalog products from travel \(hotel, flight, or destination\) catalogs to deliver ads\.",
     "Upgraded Smart+ Travel Ads là Chiến dịch Upgraded Smart+ Web sử dụng các sản phẩm từ danh mục du lịch (khách sạn, chuyến bay hoặc điểm đến) để phân phối quảng cáo."),
     
    (r"Specify \*\*a travel \(hotel, flight, or destination\) catalog with at least two approved products\*\*",
     "Chỉ định **một danh mục du lịch (khách sạn, chuyến bay hoặc điểm đến) có ít nhất hai sản phẩm đã được phê duyệt**"),
     
    (r"### Customize the ad format combinations in Upgraded Smart\+ Travel Ads",
     "### Tùy chỉnh kết hợp định dạng quảng cáo trong Upgraded Smart+ Travel Ads"),
     
    (r"The possible ad format combinations for your Upgraded Smart\+ Travel Ads are illustrated in the following diagram:",
     "Các kết hợp định dạng quảng cáo có thể có cho Upgraded Smart+ Travel Ads của bạn được minh họa trong sơ đồ sau:"),
     
    (r"Ad format combination for your Upgraded Smart\+ Travel Ads",
     "Kết hợp định dạng quảng cáo cho Upgraded Smart+ Travel Ads của bạn"),
     
    (r"To ensure certain ad formats are available in Upgraded Smart\+ Travel Ads, follow the instructions in the table below:",
     "Để đảm bảo các định dạng quảng cáo nhất định khả dụng trong Upgraded Smart+ Travel Ads, hãy làm theo hướng dẫn trong bảng dưới đây:"),
     
    # Streaming Ads
    (r"Upgraded Smart\+ Streaming Ads are Upgraded Smart\+ Web Campaigns that use catalog products from entertainment catalogs to deliver ads\.",
     "Upgraded Smart+ Streaming Ads là Chiến dịch Upgraded Smart+ Web sử dụng các sản phẩm từ danh mục giải trí để phân phối quảng cáo."),
     
    (r"1\. Create an entertainment catalog using \[/catalog/create/\]\(\.\./12-api-reference/25-catalog-management\.md#doc-1740306481755138\)\.",
     "1. Tạo một danh mục giải trí bằng cách sử dụng [/catalog/create/](../12-api-reference/25-catalog-management.md#doc-1740306481755138)."),
     
    (r"\*\s+If you want to use the Single Video or Catalog Video ad format, ensure the catalog contains at least one available catalog product\.",
     "* Nếu bạn muốn sử dụng định dạng quảng cáo Single Video hoặc Catalog Video, hãy đảm bảo danh mục chứa ít nhất một sản phẩm danh mục khả dụng."),
     
    (r"\*\s+If you want to use the Catalog Carousel ad format, ensure the catalog contains at least two available catalog products\.",
     "* Nếu bạn muốn sử dụng định dạng quảng cáo Catalog Carousel, hãy đảm bảo danh mục chứa ít nhất hai sản phẩm danh mục khả dụng."),
     
    (r"## Specification requirements for Multi-Show settings",
     "## Yêu cầu quy cách cho cài đặt Multi-Show (Specification requirements for Multi-Show settings)"),
     
    (r"The following table outlines the exact specification requirements for your Multi-Show settings\.",
     "Bảng sau đây phác thảo các yêu cầu quy cách chính xác cho cài đặt Multi-Show của bạn."),
     
    (r"Specify \*\*an entertainment catalog with at least two approved products\*\*",
     "Chỉ định **một danh mục giải trí có ít nhất hai sản phẩm đã được phê duyệt**"),
     
    (r"Specify a valid URL\. Users will be directed to your product links, TikTok Instant Page , or the specified website\.",
     "Chỉ định một URL hợp lệ. Người dùng sẽ được chuyển hướng đến liên kết sản phẩm của bạn, Trang tức thì TikTok hoặc trang web được chỉ định."),
     
    (r"### Customize the ad format combinations in Upgraded Smart\+ Streaming Ads",
     "### Tùy chỉnh kết hợp định dạng quảng cáo trong Upgraded Smart+ Streaming Ads"),
     
    (r"The possible ad format combinations for your Upgraded Smart\+ Streaming Ad are illustrated in the following diagram:",
     "Các kết hợp định dạng quảng cáo có thể có cho Upgraded Smart+ Streaming Ad của bạn được minh họa trong sơ đồ sau:"),
     
    (r"Is the multi-show format available\?", "Định dạng multi-show có khả dụng không?"),
    (r"Ad format combination for your Upgraded Smart\+ Streaming Ad", "Kết hợp định dạng quảng cáo cho Upgraded Smart+ Streaming Ad của bạn"),
    (r"Multi-show only", "Chỉ multi-show"),
    (r"Multi-show and catalog video", "Multi-show và video danh mục (catalog video)"),
    
    (r"To ensure certain ad formats are available in Upgraded Smart\+ Streaming Ads, follow the instructions in the table below:",
     "Để đảm bảo các định dạng quảng cáo nhất định khả dụng trong Upgraded Smart+ Streaming Ads, hãy làm theo hướng dẫn trong bảng dưới đây:"),
     
    (r"Display four video tiles in an auto-play video carousel",
     "Hiển thị bốn ô video trong băng chuyền video tự động phát"),
     
    (r"The catalog needs to contain at least four videos\.",
     "Danh mục cần chứa ít nhất bốn video."),
     
    (r"Ensure that the catalog \(catalog_id\) contains at least four approved media title items, each featuring a valid video\.",
     "Đảm bảo rằng danh mục (catalog_id) chứa ít nhất bốn mục tiêu đề phương tiện đã được phê duyệt, mỗi mục có một video hợp lệ."),
     
    # Mini Series
    (r"For such campaigns, you need to set `catalog_enabled` to `true` and `catalog_type` to `MINI_SERIES` at the campaign level\.",
     "Đối với các chiến dịch như vậy, bạn cần đặt `catalog_enabled` thành `true` và `catalog_type` thành `MINI_SERIES` ở cấp chiến dịch."),
     
    (r"\*\*Mini series\*\*", "**Phim bộ ngắn (Mini series)**"),
    
    (r"Specify \*\*a mini series catalog with at least one approved product\*\*",
     "Chỉ định **một danh mục phim bộ ngắn có ít nhất một sản phẩm đã được phê duyệt**"),
     
    (r"Select one mini series", "Chọn một bộ phim ngắn (Select one mini series)"),
    
    (r"Specify one available mini series catalog product \(a mini series\)\. • To retrieve the product ID \(product_id\) of an approved mini series, use \[/catalog/product/get/\]\(\.\./12-api-reference/28-catalog-products-p2\.md#doc-1740570008581121\)\.",
     "Chỉ định một sản phẩm danh mục phim bộ ngắn khả dụng (một bộ phim). • Để truy xuất ID sản phẩm (product_id) của phim bộ ngắn đã được phê duyệt, sử dụng [/catalog/product/get/](../12-api-reference/28-catalog-products-p2.md#doc-1740570008581121)."),
     
    (r"The following table outlines the various combinations of ad creative combinations based on identity and ad types\.",
     "Bảng sau đây phác thảo các cách kết hợp mẫu quảng cáo khác nhau dựa trên danh tính và loại quảng cáo."),
     
    (r"Custom User \(identity_type in the ad_configuration object is CUSTOMIZED_USER\)",
     "Người dùng tùy chỉnh (Custom User - identity_type trong đối tượng ad_configuration là CUSTOMIZED_USER)"),
     
    (r"Video posts only creatives", "Mẫu quảng cáo chỉ dùng bài đăng video (Video posts only creatives)"),
]
