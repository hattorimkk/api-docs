#!/usr/bin/env python3
"""
Từ điển câu và mệnh đề chi tiết (Granular Sentences & Clauses) cho Unit u101
"""

GRANULAR_RULES = [
    # 1. Bidding & Goal sentences
    (r'•\s*If Goal is Click or Conversion, the strategy can be Maximum Delivery or Cost Cap\.',
     '• Nếu Mục tiêu là Lượt nhấp hoặc Chuyển đổi, chiến lược có thể là Phân phối tối đa (Maximum Delivery) hoặc Giới hạn chi phí (Cost Cap).'),
    (r'•\s*If Goal is Click, Install, or In-app event, the strategy can only be \*\*Maximum Delivery\*\* or \*\*Cost Cap\*\*\.',
     '• Nếu Mục tiêu là Lượt nhấp, Cài đặt hoặc Sự kiện trong ứng dụng, chiến lược chỉ có thể là **Phân phối tối đa (Maximum Delivery)** hoặc **Giới hạn chi phí (Cost Cap)**.'),
    (r'•\s*If Goal is Click, Install, or In-app event, the strategy can only be Maximum Delivery or Cost Cap\s*\.',
     '• Nếu Mục tiêu là Lượt nhấp, Cài đặt hoặc Sự kiện trong ứng dụng, chiến lược chỉ có thể là Phân phối tối đa hoặc Giới hạn chi phí.'),
    (r'•\s*If Goal is Click, Conversion, or Lượt xem trang đích \(Landing page view\), the strategy can be Maximum Delivery or Cost Cap\.',
     '• Nếu Mục tiêu là Lượt nhấp, Chuyển đổi hoặc Lượt xem trang đích, chiến lược có thể là Phân phối tối đa hoặc Giới hạn chi phí.'),
    (r'•\s*If Goal is In-app event, the strategy can only be Maximum Delivery or Cost Cap\.',
     '• Nếu Mục tiêu là Sự kiện trong ứng dụng, chiến lược chỉ có thể là Phân phối tối đa hoặc Giới hạn chi phí.'),
    (r'•\s*For Cost Cap, you need to specify a Target CPA at the same time\.',
     '• Đối với Giới hạn chi phí, bạn cần đồng thời chỉ định CPA mục tiêu (Target CPA).'),
    (r'•\s*If Goal is Lượt xem trang đích \(Landing page view\), the strategy can only be Maximum Delivery\.',
     '• Nếu Mục tiêu là Lượt xem trang đích, chiến lược chỉ có thể là Phân phối tối đa (Maximum Delivery).'),
    (r'•\s*If Goal is Value, the strategy can be (?:Highest value|\*\*Highest value\*\*) or (?:Minimum ROAS|\*\*Minimum ROAS\*\*)\.',
     '• Nếu Mục tiêu là Giá trị, chiến lược có thể là **Giá trị cao nhất (Highest value)** hoặc **ROAS tối thiểu (Minimum ROAS)**.'),
    (r'•\s*For Minimum ROAS, you need to specify a Target ROAS at the same time\.',
     '• Đối với ROAS tối thiểu, bạn cần đồng thời chỉ định ROAS mục tiêu (Target ROAS).'),
    (r'•\s*The bid strategy must be the same across ad groups within the same campaign\.',
     '• Chiến lược giá thầu phải giống nhau trên tất cả các nhóm quảng cáo trong cùng chiến dịch.'),
    (r'•\s*When you select a campaign budget mode, the Target CPA or Target ROAS, if specified, must be the same across ad groups within the same campaign\.',
     '• Khi bạn chọn chế độ ngân sách chiến dịch, CPA mục tiêu hoặc ROAS mục tiêu (nếu được chỉ định) phải giống nhau trên tất cả các nhóm quảng cáo trong cùng một chiến dịch.'),
    (r'•\s*When you select a campaign budget mode, the Target CPA, if specified, must be the same across ad groups within the same campaign\.',
     '• Khi bạn chọn chế độ ngân sách chiến dịch, CPA mục tiêu (nếu được chỉ định) phải giống nhau trên tất cả các nhóm quảng cáo trong cùng một chiến dịch.'),
    (r'•\s*Target CPA or Target ROAS is only available when your campaign or ad group budget mode is set to daily\.',
     '• CPA mục tiêu hoặc ROAS mục tiêu chỉ khả dụng khi chế độ ngân sách chiến dịch hoặc nhóm quảng cáo được đặt thành hàng ngày (daily).'),
    (r'•\s*Target CPA is only available when your campaign or ad group budget mode is set to daily\.',
     '• CPA mục tiêu chỉ khả dụng khi chế độ ngân sách chiến dịch hoặc nhóm quảng cáo được đặt thành hàng ngày (daily).'),

    # 2. Goal descriptions
    (r'•\s*Click\s*•\s*We\'ll deliver your ads to the people most likely to click on your ad\.',
     '• Lượt nhấp (Click) • Chúng tôi sẽ phân phối quảng cáo đến những người có nhiều khả năng nhấp vào quảng cáo của bạn nhất.'),
    (r'•\s*Install\s*•\s*We\'ll show your ads to the people who are most likely to install your app\.',
     '• Cài đặt (Install) • Chúng tôi sẽ hiển thị quảng cáo cho những người có nhiều khả năng cài đặt ứng dụng của bạn nhất.'),
    (r'•\s*In-app event\s*•\s*We\'ll show your ads to the people who are most likely to (?:perform certain actions within|take a specific action in) your app\.',
     '• Sự kiện trong ứng dụng (In-app event) • Chúng tôi sẽ hiển thị quảng cáo cho những người có nhiều khả năng thực hiện hành động cụ thể trong ứng dụng của bạn nhất.'),
    (r'•\s*Value\s*•\s*We\'ll deliver your ads to users that are more likely to make a purchase in order to maximize your total purchase value\.',
     '• Giá trị (Value) • Chúng tôi sẽ phân phối quảng cáo đến người dùng có nhiều khả năng mua hàng nhất nhằm tối đa hóa tổng giá trị mua hàng của bạn.'),
    (r'•\s*In Upgraded Smart\+ non-DC App Campaigns, this Goal is only available for Android Apps\.',
     '• Trong Chiến dịch Smart+ non-DC App nâng cấp, Mục tiêu này chỉ khả dụng cho ứng dụng Android.'),
    (r'•\s*If you want to enable the Value goal for an iOS App, (\[Create an Upgraded Smart\+ DC App Campaign\]\([^\)]+\))\.',
     r'• Nếu bạn muốn bật mục tiêu Giá trị cho ứng dụng iOS, xem \1.'),
    (r'\*\*Note\*\*:\s*When you select a campaign budget mode, this setting must be the same across ad groups within the same campaign\.',
     '**Lưu ý**: Khi bạn chọn chế độ ngân sách chiến dịch, cài đặt này phải giống nhau trên tất cả các nhóm quảng cáo trong cùng một chiến dịch.'),

    # 3. Autoselect from catalog
    (r'•\s*Enabled \(Recommended\)\s*•\s*Images in your catalog will be used to automatically generate optimized (?:Quảng cáo danh mục \(Catalog Ads\)|Catalog Ads) in all formats for your products\.',
     '• Bật (Khuyến nghị) • Hình ảnh trong danh mục sẽ được sử dụng để tự động tạo Quảng cáo danh mục tối ưu hóa ở tất cả các định dạng cho sản phẩm của bạn.'),
    (r'•\s*Multiple ad format combinations are supported\.\s*For detailed configuration options and requirements, see (?:\[?Customize the ad format combinations in Upgraded Smart\+ App O2O (?:Quảng cáo danh mục \(Catalog Ads\)|Catalog Ads)\]?\(?[^\)\n]*\)?)\.',
     '• Hỗ trợ nhiều tổ hợp định dạng quảng cáo. Để biết các tùy chọn cấu hình và yêu cầu chi tiết, xem Tùy chỉnh tổ hợp định dạng quảng cáo trong Quảng cáo danh mục App O2O Smart+ nâng cấp.'),
    (r'•\s*Disabled\s*•\s*Images in your catalog will not be used to automatically generate optimized (?:Quảng cáo danh mục \(Catalog Ads\)|Catalog Ads) in all formats for your products\.The system will automatically create (?:Video đơn \(Single Video\)|Single Video) ads using your specified content\.',
     '• Tắt • Hình ảnh trong danh mục sẽ không được sử dụng để tự động tạo Quảng cáo danh mục. Hệ thống sẽ tự động tạo quảng cáo Video đơn bằng nội dung bạn chỉ định.'),
    (r'•\s*Requirements:\s*•\s*Specify a total of 1 to 50 items, either as individual videos with cover images, video posts, or a combination of both\.',
     '• Yêu cầu: • Chỉ định tổng cộng từ 1 đến 50 mục, có thể là các video riêng lẻ kèm ảnh bìa, bài đăng video hoặc kết hợp cả hai.'),
    (r'•\s*\*\*Note\*\*:\s*Not using a catalog for creatives might restrict your ad performance potential\.',
     '• **Lưu ý**: Việc không sử dụng danh mục cho nội dung sáng tạo có thể hạn chế tiềm năng hiệu suất quảng cáo của bạn.'),

    # 4. Products selection scope in catalogs
    (r'•\s*Carousel image selection scope:\s*The product images of all products in the catalog or product set selected at the ad group level will be displayed in the carousel\.',
     '• Phạm vi chọn ảnh xoay vòng: Hình ảnh của tất cả sản phẩm trong danh mục hoặc bộ sản phẩm được chọn ở cấp nhóm quảng cáo sẽ được hiển thị trong thẻ xoay vòng.'),
    (r'•\s*To promote all products in the catalog:\s*•\s*Set product_specific_type to ALL\.\s*•\s*Do not specify item_group_ids, product_set_id, and sku_ids\.',
     '• Để quảng bá tất cả sản phẩm trong danh mục: • Đặt product_specific_type thành ALL. • Không chỉ định item_group_ids, product_set_id và sku_ids.'),
    (r'•\s*To promote a product set:\s*•\s*Set product_specific_type to PRODUCT_SET\.\s*•\s*Specify product_set_id\.\s*•\s*Do not specify item_group_ids and sku_ids\.',
     '• Để quảng bá một bộ sản phẩm: • Đặt product_specific_type thành PRODUCT_SET. • Chỉ định product_set_id. • Không chỉ định item_group_ids và sku_ids.'),
    (r'•\s*To promote specific products:\s*•\s*Set product_specific_type to CUSTOMIZED\.\s*•\s*Specify item_group_ids or sku_ids\.\s*•\s*Do not specify product_set_id\.',
     '• Để quảng bá các sản phẩm cụ thể: • Đặt product_specific_type thành CUSTOMIZED. • Chỉ định item_group_ids hoặc sku_ids. • Không chỉ định product_set_id.'),

    # 5. Ad format options
    (r'Any of the following options:\s*•\s*Single video\s*•\s*Single image\s*•\s*Carousel images',
     'Một trong các tùy chọn sau: • Video đơn (Single video) • Ảnh đơn (Single image) • Thẻ ảnh xoay vòng (Carousel images)'),
    (r'•\s*To set ad format to single image, you need to specify the placement as \*\*Select Placement\*\* with Pangle only at the ad group level\.',
     '• Để đặt định dạng quảng cáo thành ảnh đơn, bạn cần chỉ định vị trí hiển thị là **Chọn vị trí thủ công** chỉ với Pangle ở cấp nhóm quảng cáo.'),
    (r'•\s*To set ad format to Carousel images, you need to specify the placement as \*\*Select Placement\*\* with TikTok only at the ad group level\.',
     '• Để đặt định dạng quảng cáo thành thẻ ảnh xoay vòng, bạn cần chỉ định vị trí hiển thị là **Chọn vị trí thủ công** chỉ với TikTok ở cấp nhóm quảng cáo.'),

    # 6. GMV Max Product level
    (r'###\s*Product level', '### Cấp độ sản phẩm (Product level)'),
    (r'-\s*If you create an enabled Product GMV Max Campaign by promoting specific products from a TikTok Shop, any existing (?:Quảng cáo mua sắm qua video \(Video Shopping Ads\)|Video Shopping Ads) and (?:Quảng cáo mua sắm sản phẩm \(Product Shopping Ads\)|Product Shopping Ads) promoting the same products will be automatically disabled\.',
     '- Nếu bạn tạo một Chiến dịch Product GMV Max đang bật bằng cách quảng bá các sản phẩm cụ thể từ TikTok Shop, mọi Video Shopping Ads và Product Shopping Ads hiện có đang quảng bá cùng những sản phẩm đó sẽ tự động bị tắt.'),
    (r'-\s*If you want to enable a (?:Quảng cáo mua sắm qua video \(Video Shopping Ads\)|Video Shopping Ads) or (?:Quảng cáo mua sắm sản phẩm \(Product Shopping Ads\)|Product Shopping Ads) that promotes products included in an enabled Product GMV Max Campaign, you will first need to pause the Product GMV Max Campaign, or remove those products from the Product GMV Max Campaign\.',
     '- Nếu bạn muốn bật Video Shopping Ads hoặc Product Shopping Ads quảng bá các sản phẩm đang nằm trong Chiến dịch Product GMV Max đang hoạt động, trước tiên bạn cần tạm dừng Chiến dịch Product GMV Max đó hoặc xóa các sản phẩm đó khỏi Chiến dịch Product GMV Max.'),

    # 7. Promotion type parameter table
    (r'Promotion type and you can decide where you\'d like to promote your products using this field\. You need to specify the field when advertising objective \(`objective_type`\) for your campaign is NOT set as `REACH`, `VIDEO_VIEWS`, or `ENGAGEMENT`\.',
     'Loại hình quảng bá, bạn có thể quyết định nơi muốn quảng bá sản phẩm thông qua trường này. Bạn cần chỉ định trường này khi mục tiêu quảng cáo (`objective_type`) của chiến dịch KHÔNG được đặt là `REACH`, `VIDEO_VIEWS` hoặc `ENGAGEMENT`.'),
    (r'Use `VIDEO_SHOPPING` for (?:Quảng cáo mua sắm qua video \(Video Shopping Ads\)|Video Shopping Ads)\.',
     'Sử dụng `VIDEO_SHOPPING` cho Quảng cáo mua sắm qua video (Video Shopping Ads).'),
    (r'The placement strategy that decides where your ads will be shown\.\s*⏎\s*Các giá trị enum hỗ trợ:\s*•\s*`PLACEMENT_TYPE_AUTOMATIC`:\s*Automatic placement\.\s*TikTok\'s ad system will use smart calculations to give you the best combination of ad placements across all apps\.\s*•\s*`PLACEMENT_TYPE_NORMAL`:\s*Select placement\.\s*By selecting your placement manually, you\'ll be able to choose the apps to deliver your ads on\.\s*⏎\s*Giá trị mặc định:\s*`PLACEMENT_TYPE_NORMAL`\.',
     'Chiến lược vị trí hiển thị quyết định nơi quảng cáo sẽ xuất hiện. ⏎ Các giá trị enum hỗ trợ: • `PLACEMENT_TYPE_AUTOMATIC`: Vị trí tự động (Automatic placement). Hệ thống quảng cáo của TikTok sẽ sử dụng thuật toán thông minh để mang lại tổ hợp vị trí quảng cáo tối ưu trên tất cả ứng dụng. • `PLACEMENT_TYPE_NORMAL`: Chọn vị trí thủ công (Select placement). Bằng việc chọn vị trí thủ công, bạn có thể chọn các ứng dụng cụ thể để phân phối quảng cáo. ⏎ Giá trị mặc định: `PLACEMENT_TYPE_NORMAL`.'),
    (r'Pangle placement \(`PLACEMENT_PANGLE`\) for (?:Quảng cáo mua sắm qua video \(Video Shopping Ads\)|Video Shopping Ads) for Shop \(`product_source` as `STORE` or `SHOWCASE`\) is currently an allowlist-only feature\.\s*If you would like to access it, please contact your TikTok representative\.\s*Once you are allowlisted, you will also need to select \*\*Showcase\*\* as the catalog type for Video Shopping Ads for Shop to deliver on Pangle\.',
     'Vị trí Pangle (`PLACEMENT_PANGLE`) cho Video Shopping Ads dành cho Cửa hàng (`product_source` là `STORE` hoặc `SHOWCASE`) hiện là tính năng chỉ dành cho danh sách cho phép (allowlist-only). Nếu bạn muốn truy cập, vui lòng liên hệ với đại diện TikTok của bạn. Sau khi được đưa vào danh sách cho phép, bạn cũng cần chọn **Showcase** làm loại danh mục cho Video Shopping Ads dành cho Cửa hàng để phân phối trên Pangle.'),

    # 8. CBO requirements & App Install VBO
    (r'You can no longer create non-CBO \(Campaign Budget Optimization\) App Install VBO \(Value-Based Optimization\) campaigns via the API\.',
     'Bạn không thể tạo các chiến dịch App Install VBO (Tối ưu hóa theo giá trị) không dùng CBO (Tối ưu hóa ngân sách chiến dịch) qua API nữa.'),
    (r'This restriction applies to the campaign level \(`budget_optimize_on` as `false`\) and is being made because these configurations have demonstrated significantly weaker delivery performance compared to their CBO counterparts\.',
     'Hạn chế này áp dụng ở cấp chiến dịch (`budget_optimize_on` là `false`) do các cấu hình này có hiệu suất phân phối kém hơn đáng kể so với cấu hình dùng CBO tương ứng.'),
    (r'This change applies to new campaign creation only and does not affect existing campaigns\.',
     'Thay đổi này chỉ áp dụng cho việc tạo chiến dịch mới và không ảnh hưởng đến các chiến dịch hiện có.'),
    (r'To ensure smooth API integration, we recommend that you enable the CBO \(`budget_optimize_on` as `true`\) setting for your App Install VBO campaigns at the campaign level\.',
     'Để đảm bảo tích hợp API suôn sẻ, chúng tôi khuyến nghị bạn bật cài đặt CBO (`budget_optimize_on` là `true`) cho các chiến dịch App Install VBO ở cấp chiến dịch.'),

    # 9. Pixel list & tracking options
    (r'To obtain the list of Pixels within your ad account, use (\[/pixel/list/\]\([^\)]+\))\.',
     r'Để lấy danh sách Pixel trong tài khoản quảng cáo của bạn, sử dụng \1.'),
    (r'When Goal is Conversion or Value, specify a valid Pixel\.',
     'Khi Mục tiêu là Chuyển đổi hoặc Giá trị, hãy chỉ định một Pixel hợp lệ.'),
    (r'When Goal is Click or Lượt xem trang đích \(Landing page view\), you don\'t need to specify a Pixel\.',
     'Khi Mục tiêu là Lượt nhấp hoặc Lượt xem trang đích, bạn không cần chỉ định Pixel.'),

    # 10. Call to action dynamic vs standard
    (r'To use dynamic call to action, specify call_to_action_id\.',
     'Để sử dụng lời kêu gọi hành động động, hãy chỉ định call_to_action_id.'),
    (r'To use standard call to action, specify call_to_action\.',
     'Để sử dụng lời kêu gọi hành động tiêu chuẩn, hãy chỉ định call_to_action.'),
    (r'To use dynamic call to action, pass call_to_action_id\.',
     'Để sử dụng lời kêu gọi hành động động, hãy truyền call_to_action_id.'),
    (r'To use standard call to action, pass call_to_action_list\.',
     'Để sử dụng lời kêu gọi hành động tiêu chuẩn, hãy truyền call_to_action_list.'),

    # 11. Third party partners tracking IAS Zefr DoubleVerify
    (r'If you set either of these two settings to IAS, you need to set both to IAS, and specify the same IAS wrapped tag\.',
     'Nếu bạn đặt một trong hai cài đặt này là IAS, bạn phải đặt cả hai là IAS và chỉ định cùng một thẻ bọc IAS.'),
    (r'If you set either of these two settings to Zefr, you need to set both to Zefr\.',
     'Nếu bạn đặt một trong hai cài đặt này là Zefr, bạn phải đặt cả hai là Zefr.'),

    # 12. GMV Max Q3 2025 note
    (r'Starting Q3, 2025, (\[GMV Max\]\([^\)]+\)) will be the default and only supported campaign type for TikTok Shop\.',
     r'Bắt đầu từ Quý 3 năm 2025, \1 sẽ là loại chiến dịch mặc định và duy nhất được hỗ trợ cho TikTok Shop.'),
    (r'If you create ads using the Product Sales objective and your sales destination is TikTok Shop, use the API endpoints under GMV Max API instead of using the endpoints under LIVE Shopping Ads, Product Shopping Ads, or Video Shopping Ads\.',
     'Nếu bạn tạo quảng cáo bằng mục tiêu Doanh số sản phẩm (Product Sales) và đích bán hàng là TikTok Shop, hãy sử dụng các endpoint trong GMV Max API thay vì các endpoint trong LIVE Shopping Ads, Product Shopping Ads hoặc Video Shopping Ads.'),
    (r'If you have questions, please contact your TikTok representative\.',
     'Nếu bạn có bất kỳ thắc mắc nào, vui lòng liên hệ với đại diện TikTok của bạn.'),
    (r'Learn more about the detailed changes to the campaign type and endpoint deprecation schedule in (\[Migrate to GMV Max Campaigns\]\([^\)]+\))\.',
     r'Tìm hiểu thêm về các thay đổi chi tiết đối với loại chiến dịch và lộ trình ngừng hỗ trợ endpoint tại \1.'),
]
