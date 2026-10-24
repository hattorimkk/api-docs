#!/usr/bin/env python3
"""
Batch 4: Dịch các thiết lập Nhắm mục tiêu chi tiết, Đề xuất đối tượng, Tài sản sáng tạo, Smart+ và Nguồn phân bổ ứng dụng
"""

BATCH4_RULES = [
    # Audience suggestions & Detailed targeting
    (r'Audience suggestions · Interests & behaviors · Interests \*\((Không bắt buộc|Optional)\)\*',
     'Đề xuất đối tượng · Sở thích & hành vi · Sở thích *(Không bắt buộc)*'),

    (r'Audience suggestions · Interests & behaviors · Purchase intention \*\((Không bắt buộc|Optional)\)\*',
     'Đề xuất đối tượng · Sở thích & hành vi · Ý định mua hàng *(Không bắt buộc)*'),

    (r'Audience suggestions · Interests & behaviors · Video interactions · Creator interactions · Hashtag interactions \*\((Không bắt buộc|Optional)\)\*',
     'Đề xuất đối tượng · Sở thích & hành vi · Tương tác video · Tương tác nhà sáng tạo · Tương tác hashtag *(Không bắt buộc)*'),

    (r'Detailed targeting · Interests & behaviors · Interests \*\((Không bắt buộc|Optional)\)\*',
     'Nhắm mục tiêu chi tiết · Sở thích & hành vi · Sở thích *(Không bắt buộc)*'),

    (r'Detailed targeting · Interests & behaviors · Purchase intention \*\((Không bắt buộc|Optional)\)\*',
     'Nhắm mục tiêu chi tiết · Sở thích & hành vi · Ý định mua hàng *(Không bắt buộc)*'),

    (r'Detailed targeting · Interests & behaviors · Video interactions · Creator interactions · Hashtag interactions \*\((Không bắt buộc|Optional)\)\*',
     'Nhắm mục tiêu chi tiết · Sở thích & hành vi · Tương tác video · Tương tác nhà sáng tạo · Tương tác hashtag *(Không bắt buộc)*'),

    (r'Creative assets · Playable \((Không bắt buộc|Optional) for the (?:Video đơn \(Single Video\)|Single Video) format\)',
     'Tài sản sáng tạo · Quảng cáo tương tác (Playable) *(Tùy chọn cho định dạng Video đơn)*'),

    # Smart+ Campaign disabled check
    (r'Disabled\s*(?:⏎|\n)\s*If you are not sure about Liệu campaign is Smart\+ Campaign, you can use the `is_smart_performance_campaign` field returned from (\[\/campaign\/get\/\]\([^\)]+\)) to check\.',
     r'Tắt. ⏎ Nếu bạn không chắc chắn liệu chiến dịch có phải là Chiến dịch Smart+ hay không, bạn có thể kiểm tra qua trường `is_smart_performance_campaign` trả về từ \1.'),

    (r'Disabled\s*(?:⏎|\n)\s*If you are not sure about whether a campaign is a Smart\+ Campaign, you can use the `is_smart_performance_campaign` field returned from (\[\/campaign\/get\/\]\([^\)]+\)) to check\.',
     r'Tắt. ⏎ Nếu bạn không chắc chắn liệu chiến dịch có phải là Chiến dịch Smart+ hay không, bạn có thể kiểm tra qua trường `is_smart_performance_campaign` trả về từ \1.'),

    # Ad format & carousel/video descriptions
    (r'\| Ad format \| Any of the following types:\s*• Single video\s*•\s*Carousel images \| `ad_format` \| Any of the following values:\s*• `SINGLE_VIDEO`\s*• `CAROUSEL_ADS`\s*•\s*Để tìm hiểu cách tạo Standard Carousel Ads, see \[Steps for creating Standard Carousel Ads\]\(([^\)]+)\)\. \|',
     r'| Định dạng quảng cáo | Một trong các loại sau: • Video đơn (Single video) • Hình ảnh thẻ xoay vòng (Carousel images) | `ad_format` | Một trong các giá trị sau: • `SINGLE_VIDEO` • `CAROUSEL_ADS` • Để tìm hiểu cách tạo Quảng cáo Thẻ xoay vòng Tiêu chuẩn, xem [Các bước tạo Quảng cáo Thẻ xoay vòng Tiêu chuẩn](\1). |'),

    (r'If you enable auto-selection of catalog creatives \(`catalog_creative_toggle` is `true`\), the system will automatically create ads using combinations of three possible formats: (?:Thẻ xoay vòng danh mục \(Catalog Carousel\)|Catalog Carousel), catalog video, and (?:Video đơn \(Single Video\)|Single Video)\.',
     'Nếu bạn bật tính năng tự động chọn tài liệu sáng tạo danh mục (`catalog_creative_toggle` là `true`), hệ thống sẽ tự động tạo quảng cáo bằng các cách kết hợp giữa ba định dạng khả dụng: Thẻ xoay vòng danh mục (Catalog Carousel), Video danh mục (Catalog Video), và Video đơn (Single Video).'),

    (r'The system will automatically select one of your video templates for each catalog product to generate the corresponding catalog video or use the video URL for the catalog product\.',
     'Hệ thống sẽ tự động chọn một trong các mẫu video của bạn cho từng sản phẩm danh mục để tạo video danh mục tương ứng hoặc sử dụng URL video cho sản phẩm danh mục đó.'),

    (r'•\s*Set catalog_id to ID of the same catalog specified at the ad group level\.\s*•\s*Set product_specific_type to ALL, PRODUCT_SET or CUSTOMIZED_PRODUCTS\.\s*•\s*If product_specific_type is set to ALL, you don\'t need to pass sku_ids , item_group_ids , and product_set_id\.\s*•\s*If product_specific_type is set to PRODUCT_SET, you need to pass either item_group_ids or product_set_id\. sku_ids is not needed\.\s*•\s*If product_specific_type is set to CUSTOMIZED_PRODUCTS, you need to pass a maximum of 20 products through sku_ids\. item_group_ids and product_set_id are not needed\.\s*\*\*Note\*\*: To determine Liệu an E-commerce catalog product can be used in ads, use (\[\/catalog\/product\/get\/\]\([^\)]+\))\.\s*If the returned ad_creation_eligible for the product is AVAILABLE, you can use the product in ads\.',
     r'• Đặt `catalog_id` thành ID của cùng danh mục được chỉ định ở cấp nhóm quảng cáo. • Đặt `product_specific_type` thành `ALL`, `PRODUCT_SET` hoặc `CUSTOMIZED_PRODUCTS`. • Nếu `product_specific_type` được đặt thành `ALL`, bạn không cần truyền `sku_ids`, `item_group_ids` và `product_set_id`. • Nếu `product_specific_type` được đặt thành `PRODUCT_SET`, bạn cần truyền `item_group_ids` hoặc `product_set_id`. Không cần `sku_ids`. • Nếu `product_specific_type` được đặt thành `CUSTOMIZED_PRODUCTS`, bạn cần truyền tối đa 20 sản phẩm qua `sku_ids`. Không cần `item_group_ids` và `product_set_id`. **Lưu ý**: Để xác định liệu sản phẩm danh mục thương mại điện tử có thể được sử dụng trong quảng cáo hay không, sử dụng \1. Nếu trường `ad_creation_eligible` trả về cho sản phẩm là `AVAILABLE`, bạn có thể sử dụng sản phẩm trong quảng cáo.'),

    # App attribution source & data source
    (r'For an eligible app: • Specify valid values or not specified • To confirm Liệu app_id is eligible for this setting, use\s*(\[\/app\/info\/\]\([^\)]+\)) and check Liệu returned is_attribution_flex_enable is true\.\s*• To retrieve the available values for this setting, use (\[\/tool\/available\/attribution_source\/\]\([^\)]+\))\.\s*\*\*Note\*\*:\s*• Attribution source and data source configuration for an app during Upgraded Smart\+ Ad Group creation is currently an allowlist-only feature\. If you would like to access it, please contact your TikTok representative\.\s*• When budget_optimize_on is true at the campaign level, the app_attribution_source, if specified, must be the same for ad groups within the same campaign\.',
     r'Đối với ứng dụng đủ điều kiện: • Chỉ định các giá trị hợp lệ hoặc không chỉ định • Để xác nhận liệu `app_id` có đủ điều kiện cho cài đặt này hay không, sử dụng \1 và kiểm tra xem trường `is_attribution_flex_enable` trả về có phải là `true` hay không. • Để truy xuất các giá trị khả dụng cho cài đặt này, sử dụng \2. **Lưu ý**: • Cấu hình nguồn phân bổ (attribution source) và nguồn dữ liệu (data source) cho ứng dụng trong quá trình tạo Nhóm quảng cáo Upgraded Smart+ hiện là tính năng chỉ dành cho danh sách cho phép (allowlist-only). Nếu bạn muốn truy cập, vui lòng liên hệ với đại diện TikTok của bạn. • Khi `budget_optimize_on` là `true` ở cấp chiến dịch, `app_attribution_source` (nếu được chỉ định) phải giống nhau đối với các nhóm quảng cáo trong cùng chiến dịch.'),

    (r'For an eligible app: • Specify valid values or not specified • To confirm Liệu app_id is eligible for this setting, use\s*(\[\/app\/info\/\]\([^\)]+\)) and check Liệu returned is_attribution_flex_enable is true\.\s*• To retrieve the available values for this setting, use (\[\/tool\/available\/attribution_source\/\]\([^\)]+\))\.\s*\*\*Note\*\*:\s*• Attribution source and data source configuration for an app during Upgraded Smart\+ Ad Group creation is currently an allowlist-only feature\. If you would like to access it, please contact your TikTok representative\.\s*• When budget_optimize_on is true at the campaign level, the app_data_source, if specified, must be the same for ad groups within the same campaign\.',
     r'Đối với ứng dụng đủ điều kiện: • Chỉ định các giá trị hợp lệ hoặc không chỉ định • Để xác nhận liệu `app_id` có đủ điều kiện cho cài đặt này hay không, sử dụng \1 và kiểm tra xem trường `is_attribution_flex_enable` trả về có phải là `true` hay không. • Để truy xuất các giá trị khả dụng cho cài đặt này, sử dụng \2. **Lưu ý**: • Cấu hình nguồn phân bổ (attribution source) và nguồn dữ liệu (data source) cho ứng dụng trong quá trình tạo Nhóm quảng cáo Upgraded Smart+ hiện là tính năng chỉ dành cho danh sách cho phép (allowlist-only). Nếu bạn muốn truy cập, vui lòng liên hệ với đại diện TikTok của bạn. • Khi `budget_optimize_on` là `true` ở cấp chiến dịch, `app_data_source` (nếu được chỉ định) phải giống nhau đối với các nhóm quảng cáo trong cùng chiến dịch.'),

    # Automotive & Models specific
    (r'- Creating Quảng cáo ô tô theo dòng xe \(Automotive Ads for Models\) requires setting up an Auto-Model catalog in Business Center first\.\s*To set up the catalog:\s*1\. Create an Auto-Model catalog using (\[\/catalog\/create\/\]\([^\)]+\))\.\s*2\. Upload products to the catalog using (\[\/catalog\/product\/upload\/\]\([^\)]+\))\.\s*3\. Check the product handling results using (\[\/catalog\/product\/log\/\]\([^\)]+\))\.\s*Pass in the `feed_log_id` obtained from Step 2\. If the field `warn_affected_products` in the response is not null, examine the issue details and return to Step 2 to reupload the product\.\s*4\. \(Không bắt buộc\) Create a product set using (\[\/catalog\/product_set\/create\/\]\([^\)]+\))\.\s*If you want to have products selected from a product set at the ad level, creating a product set is necessary\. Otherwise, you can skip this step\.\s*5\. \(Không bắt buộc\) Invite members to Business Center and grant the admin permission using (\[\/bc\/member\/invite\/\]\([^\)]+\))\.\s*You can also choose `advertiser_role` that you want to assign to the members invited\.\s*6\. \(Không bắt buộc\) Share a catalog with members and grant catalog management access using (\[\/bc\/asset\/assign\/\]\([^\)]+\))\.\s*Make sure to specify `CATALOG` in the `asset_type` field and `ADMIN` in the `catalog_role` field\.',
     r'- Việc tạo Quảng cáo ô tô theo dòng xe (Automotive Ads for Models) yêu cầu phải thiết lập danh mục Auto-Model trong Trung tâm doanh nghiệp (Business Center) trước. Để thiết lập danh mục: 1. Tạo danh mục Auto-Model bằng \1. 2. Tải sản phẩm lên danh mục bằng \2. 3. Kiểm tra kết quả xử lý sản phẩm bằng \3. Truyền `feed_log_id` nhận được từ Bước 2. Nếu trường `warn_affected_products` trong phản hồi khác null, hãy kiểm tra chi tiết sự cố và quay lại Bước 2 để tải lại sản phẩm lên. 4. *(Không bắt buộc)* Tạo nhóm sản phẩm bằng \4. Nếu bạn muốn các sản phẩm được chọn từ một nhóm sản phẩm ở cấp quảng cáo, việc tạo nhóm sản phẩm là cần thiết. Nếu không, bạn có thể bỏ qua bước này. 5. *(Không bắt buộc)* Mời thành viên vào Business Center và cấp quyền quản trị viên bằng \5. Bạn cũng có thể chọn `advertiser_role` mà bạn muốn gán cho thành viên được mời. 6. *(Không bắt buộc)* Chia sẻ danh mục với thành viên và cấp quyền quản lý danh mục bằng \6. Đảm bảo chỉ định `CATALOG` trong trường `asset_type` và `ADMIN` trong trường `catalog_role`.'),

    (r'Creating Travel Ads requires setting up a travel \(hotel, flight, or destination\) catalog in a Business Center first\.',
     'Việc tạo Quảng cáo Du lịch (Travel Ads) yêu cầu phải thiết lập trước danh mục du lịch (khách sạn, chuyến bay hoặc điểm đến) trong Trung tâm doanh nghiệp (Business Center).'),

    (r'Creating Smart\+ Streaming Ads requires setting up an entertainment catalog in Business Center first\.',
     'Việc tạo Quảng cáo Truyền phát Smart+ (Smart+ Streaming Ads) yêu cầu phải thiết lập trước danh mục giải trí trong Trung tâm doanh nghiệp (Business Center).'),

    (r'Creating an Upgraded Smart\+ TikTok Growth Max: Mini Dramas Catalog campaign requires setting up a mini series catalog in your Business Center first\.',
     'Việc tạo chiến dịch Upgraded Smart+ TikTok Growth Max: Mini Dramas Catalog yêu cầu phải thiết lập trước một danh mục phim ngắn tập (mini series catalog) trong Trung tâm doanh nghiệp (Business Center) của bạn.'),

    (r'Creating Smart\+ Quảng cáo danh mục \(Catalog Ads\) requires setting up an E-commerce catalog in your Business Center first\.',
     'Việc tạo Quảng cáo danh mục Smart+ (Catalog Ads) yêu cầu phải thiết lập trước một danh mục Thương mại điện tử trong Trung tâm doanh nghiệp (Business Center) của bạn.'),

    (r'Creating Upgraded Smart\+ E-commerce Quảng cáo danh mục \(Catalog Ads\) requires setting up an E-commerce catalog in your Business Center first\.',
     'Việc tạo Quảng cáo danh mục Thương mại điện tử Upgraded Smart+ (Catalog Ads) yêu cầu phải thiết lập trước một danh mục Thương mại điện tử trong Trung tâm doanh nghiệp (Business Center) của bạn.'),

    (r'Creating Upgraded Smart\+ Mini Series Quảng cáo danh mục \(Catalog Ads\) requires setting up a mini series catalog in your Business Center first\.',
     'Việc tạo Quảng cáo danh mục Phim ngắn tập Upgraded Smart+ (Catalog Ads) yêu cầu phải thiết lập trước một danh mục phim ngắn tập trong Trung tâm doanh nghiệp (Business Center) của bạn.'),

    (r'- Creating App Travel Quảng cáo danh mục \(Catalog Ads\) requires setting up a travel \(hotel, flight, or destination\) catalog in a Business Center first\.',
     '- Việc tạo Quảng cáo danh mục Du lịch Ứng dụng (App Travel Catalog Ads) yêu cầu phải thiết lập trước danh mục du lịch (khách sạn, chuyến bay hoặc điểm đến) trong Trung tâm doanh nghiệp (Business Center).'),
]
