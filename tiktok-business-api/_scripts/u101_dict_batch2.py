#!/usr/bin/env python3
"""
Batch 2: Dịch các cài đặt Bidding, Targeting, Catalog, Creative, Tracking lặp lại trong u101
"""

BATCH2_RULES = [
    # Bidding & Pacing
    (r'• If Bid Strategy is set to Cost Cap, you can set Delivery Type to Standard or Accelerated\.\s*• If Bid Strategy is set to Maximum Delivery, you can only set Delivery Type to Standard\.',
     '• Nếu Chiến lược giá thầu là Giới hạn chi phí (Cost Cap), bạn có thể đặt Loại phân phối thành Tiêu chuẩn (Standard) hoặc Tăng tốc (Accelerated). • Nếu Chiến lược giá thầu là Phân phối tối đa (Maximum Delivery), bạn chỉ có thể đặt Loại phân phối thành Tiêu chuẩn (Standard).'),

    (r'• If Bid strategy is set to Cost Cap, you can set Delivery type to Standard or Accelerated\.\s*• If Bid strategy is set to Maximum Delivery, you can only set Delivery type to Standard\.',
     '• Nếu Chiến lược giá thầu là Giới hạn chi phí (Cost Cap), bạn có thể đặt Loại phân phối thành Tiêu chuẩn (Standard) hoặc Tăng tốc (Accelerated). • Nếu Chiến lược giá thầu là Phân phối tối đa (Maximum Delivery), bạn chỉ có thể đặt Loại phân phối thành Tiêu chuẩn (Standard).'),

    (r'• If Bid Strategy is set to Cost Cap, you can set Delivery Type to Standard or Accelerated\.\s*• If Bid Strategy is set to Maximum Delivery, Highest Value or Minimum ROAS, you can only set Delivery Type to Standard\.',
     '• Nếu Chiến lược giá thầu là Giới hạn chi phí (Cost Cap), bạn có thể đặt Loại phân phối thành Tiêu chuẩn (Standard) hoặc Tăng tốc (Accelerated). • Nếu Chiến lược giá thầu là Phân phối tối đa (Maximum Delivery), Giá trị cao nhất (Highest Value) hoặc ROAS tối thiểu (Minimum ROAS), bạn chỉ có thể đặt Loại phân phối thành Tiêu chuẩn (Standard).'),

    (r'• If you specify `bid_type` as `BID_TYPE_CUSTOM`, you can set `pacing` to `PACING_MODE_SMOOTH` or `PACING_MODE_FAST`\.\s*• If you specify `bid_type` as `BID_TYPE_NO_BID`, you can only set `pacing` to `PACING_MODE_SMOOTH`\.',
     '• Nếu bạn chỉ định `bid_type` là `BID_TYPE_CUSTOM`, bạn có thể đặt `pacing` thành `PACING_MODE_SMOOTH` hoặc `PACING_MODE_FAST`. • Nếu bạn chỉ định `bid_type` là `BID_TYPE_NO_BID`, bạn chỉ có thể đặt `pacing` thành `PACING_MODE_SMOOTH`.'),

    (r'• If you specify bid_type as BID_TYPE_CUSTOM, you can set pacing to PACING_MODE_SMOOTH or PACING_MODE_FAST\.\s*• If you specify bid_type as BID_TYPE_NO_BID, you can only set pacing to PACING_MODE_SMOOTH\.',
     '• Nếu bạn chỉ định `bid_type` là `BID_TYPE_CUSTOM`, bạn có thể đặt `pacing` thành `PACING_MODE_SMOOTH` hoặc `PACING_MODE_FAST`. • Nếu bạn chỉ định `bid_type` là `BID_TYPE_NO_BID`, bạn chỉ có thể đặt `pacing` thành `PACING_MODE_SMOOTH`.'),

    (r'• If bid_type is BID_TYPE_CUSTOM, you can set pacing to PACING_MODE_SMOOTH or PACING_MODE_FAST\.\s*• If bid_type is BID_TYPE_NO_BID, you can only set pacing to PACING_MODE_SMOOTH\.',
     '• Nếu `bid_type` là `BID_TYPE_CUSTOM`, bạn có thể đặt `pacing` thành `PACING_MODE_SMOOTH` hoặc `PACING_MODE_FAST`. • Nếu `bid_type` là `BID_TYPE_NO_BID`, bạn chỉ có thể đặt `pacing` thành `PACING_MODE_SMOOTH`.'),

    (r'Set bid_type to BID_TYPE_CUSTOM or BID_TYPE_NO_BID\.\s*•\s*If bid_type is BID_TYPE_CUSTOM, pass conversion_bid_price at the same time\.',
     'Đặt `bid_type` thành `BID_TYPE_CUSTOM` hoặc `BID_TYPE_NO_BID`. • Nếu `bid_type` là `BID_TYPE_CUSTOM`, hãy truyền `conversion_bid_price` cùng lúc.'),

    (r'Any of the following types: • Daily budget • Lifetime budget • Infinite budget',
     'Một trong các loại sau: • Ngân sách hàng ngày (Daily budget) • Ngân sách trọn đời (Lifetime budget) • Ngân sách không giới hạn (Infinite budget)'),

    (r'Any of the following values: • BUDGET_MODE_DAY • BUDGET_MODE_DYNAMIC_DAILY_BUDGET',
     'Một trong các giá trị sau: • `BUDGET_MODE_DAY` • `BUDGET_MODE_DYNAMIC_DAILY_BUDGET`'),

    # Billing & Optimization goals
    (r'\| Billing event \| oCPM \| `billing_event` \| `OCPM` \|', '| Sự kiện tính phí | oCPM | `billing_event` | `OCPM` |'),
    (r'\| Billing event \| CPC \| `billing_event` \| `CPC` \|', '| Sự kiện tính phí | CPC | `billing_event` | `CPC` |'),
    (r'\| Optimization goal \| Click \| `optimization_goal` \| `CLICK` \|', '| Mục tiêu tối ưu hóa | Lượt nhấp (Click) | `optimization_goal` | `CLICK` |'),
    (r'\| Optimization goal \| Conversions \| `optimization_goal` \| `CONVERT` \|', '| Mục tiêu tối ưu hóa | Lượt chuyển đổi (Conversions) | `optimization_goal` | `CONVERT` |'),

    (r'• If Optimization goal is set to Conversions, set Billing event to oCPM\.\s*• If Optimization goal is set to Click, set Billing event to CPC\.',
     '• Nếu Mục tiêu tối ưu hóa được đặt thành Chuyển đổi (Conversions), hãy đặt Sự kiện tính phí thành oCPM. • Nếu Mục tiêu tối ưu hóa được đặt thành Lượt nhấp (Click), hãy đặt Sự kiện tính phí thành CPC.'),

    (r'• If optimization_goal is set to CLICK, specify billing_event as CPC\.\s*•\s*If optimization_goal is set to CONVERT, specify billing_event as OCPM\.',
     '• Nếu `optimization_goal` được đặt thành `CLICK`, chỉ định `billing_event` là `CPC`. • Nếu `optimization_goal` được đặt thành `CONVERT`, chỉ định `billing_event` là `OCPM`.'),

    (r'• If optimization_goal is CONVERT, pass in pixel_id and optimization_event at the same time\.\s*• If optimization_goal is CLICK, do not pass in pixel_id and optimization_event\.\s*To obtain Pixels with their associated optimization events, use \[\/pixel\/list\/\]\(([^\)]+)\)\.',
     r'• Nếu `optimization_goal` là `CONVERT`, hãy truyền cả `pixel_id` và `optimization_event` cùng lúc. • Nếu `optimization_goal` là `CLICK`, không truyền `pixel_id` và `optimization_event`. Để lấy danh sách Pixel cùng các sự kiện tối ưu hóa liên kết, sử dụng [/pixel/list/](\1).'),

    (r'Attribution settings \(supported only if Optimization goal is Conversions\)',
     'Cài đặt phân bổ (chỉ hỗ trợ nếu Mục tiêu tối ưu hóa là Chuyển đổi)'),

    (r'\| Attribution settings \| <ul><li> Attribution window: Unset\.\s*<br>\s*The default setting is 7-day click & 1-day view <\/li><li> Event count: Unset\.<br> The default setting is Once\.<\/li><\/ul> \| <ul><li>`click_attribution_window`<\/li><li>`view_attribution_window`<\/li><li>`attribution_event_count` <\/li><\/ul>\| Not passed\.\s*<br>\s*<br>\s*<ul><li>`click_attribution_window` will default to `SEVEN_DAYS`\.\s*<\/li><li>`view_attribution_window` will default to `ONE_DAY`\.<\/li><li>`attribution_event_count` will default to `ONCE`\.<\/li><\/ul> \|',
     '| Cài đặt phân bổ (Attribution settings) | <ul><li> Khung phân bổ: Chưa đặt. Mặc định là nhấp 7 ngày & xem 1 ngày </li><li> Đếm sự kiện: Chưa đặt. Mặc định là Một lần (Once).</li></ul> | <ul><li>`click_attribution_window`</li><li>`view_attribution_window`</li><li>`attribution_event_count`</li></ul> | Không truyền. <br><br><ul><li>`click_attribution_window` sẽ mặc định là `SEVEN_DAYS`.</li><li>`view_attribution_window` sẽ mặc định là `ONE_DAY`.</li><li>`attribution_event_count` sẽ mặc định là `ONCE`.</li></ul> |'),

    # Audience targeting rows
    (r'Audience targeting · Demographics - Location', 'Nhắm mục tiêu đối tượng · Nhân khẩu học - Vị trí địa lý (Location)'),
    (r'Audience targeting · Demographics - zip code targeting', 'Nhắm mục tiêu đối tượng · Nhân khẩu học - Nhắm mục tiêu theo mã zip'),
    (r'Audience targeting · Demographics - Age', 'Nhắm mục tiêu đối tượng · Nhân khẩu học - Độ tuổi (Age)'),
    (r'Audience targeting · Demographics - Spending power', 'Nhắm mục tiêu đối tượng · Nhân khẩu học - Sức chi tiêu (Spending power)'),
    (r'Audience targeting · Interests & Behaviors - Purchase intention', 'Nhắm mục tiêu đối tượng · Sở thích & Hành vi - Ý định mua hàng (Purchase intention)'),
    (r'Audience targeting · Saved audience', 'Nhắm mục tiêu đối tượng · Đối tượng đã lưu (Saved audience)'),
    (r'Audience targeting · Retarget audience', 'Nhắm mục tiêu đối tượng · Nhắm mục tiêu lại đối tượng (Retarget audience)'),
    (r'Audience targeting\s*•\s*Pangle audience packages', 'Nhắm mục tiêu đối tượng · Gói đối tượng Pangle (Pangle audience packages)'),
    (r'Audience targeting\s*•\s*Targeting expansion', 'Nhắm mục tiêu đối tượng · Mở rộng nhắm mục tiêu (Targeting expansion)'),
    (r'Content exclusions - Inventory filter', 'Loại trừ nội dung - Bộ lọc khoảng không quảng cáo (Inventory filter)'),

    (r'IDs of locations that match or are a subset of the targeting location of catalog_id\.',
     'ID của các vị trí khớp hoặc là tập con của vị trí nhắm mục tiêu của `catalog_id`.'),

    (r'Supported when the targeting location of your catalog is in the United States\.',
     'Được hỗ trợ khi vị trí nhắm mục tiêu của danh mục ở Hoa Kỳ.'),

    (r'Supported when the targeting location of catalog_id is in the United States\.',
     'Được hỗ trợ khi vị trí nhắm mục tiêu của `catalog_id` ở Hoa Kỳ.'),

    (r'The targeted locations should match or be the subset of the targeting locations of your TikTok Mini\.',
     'Các vị trí được nhắm mục tiêu phải khớp hoặc là tập con của các vị trí nhắm mục tiêu của TikTok Mini của bạn.'),

    (r'Specify IDs of locations that match or are the subset of the targeting locations of the specified minis_id\. To obtain the targeting locations of a TikTok Mini, use \[\/minis\/get\/\]\(([^\)]+)\) and check the returned region_codes\.',
     r'Chỉ định ID của các vị trí khớp hoặc là tập con của các vị trí nhắm mục tiêu của `minis_id` được chỉ định. Để lấy vị trí nhắm mục tiêu của TikTok Mini, sử dụng [/minis/get/](\1) và kiểm tra `region_codes` trả về.'),

    (r'Specify a valid value\. Specify IDs of locations that match or are a subset of the targeting location of catalog_id\. To obtain the targeting location of a catalog, use \[\/catalog\/get\/\]\(https:\/\/business-api\.tiktok\.com\/portal\/docs\/get-catalogs\/v1\.3\) and check the returned country\.',
     'Chỉ định một giá trị hợp lệ. Chỉ định ID của các vị trí khớp hoặc là tập con của vị trí nhắm mục tiêu của `catalog_id`. Để lấy vị trí nhắm mục tiêu của danh mục, sử dụng [/catalog/get/](https://business-api.tiktok.com/portal/docs/get-catalogs/v1.3) và kiểm tra trường `country` trả về.'),

    # Demographics location targeting table cell
    (r'\| Demographics - Location targeting \| The available targeting regions are as follows: <ul><li>APAC: Australia, Cambodia, Indonesia, Japan, Malaysia, New Zealand, the Philippines, Singapore, South Korea, Thailand, Vietnam<\/li><li>LATAM: Brazil, Chile, Colombia, Ecuador, Mexico, Peru<\/li><\/ul>Note that advertisers registered with the Chinese mainland \(`CN`\) cannot target locations in Australia and Indonesia\. \| `location_ids` \| Pass the IDs of locations within the following regions: <ul><li>APAC: Australia, Cambodia, Indonesia, Japan, Malaysia, New Zealand, the Philippines, Singapore, South Korea, Thailand, Vietnam<\/li><li>LATAM: Brazil, Chile, Colombia, Ecuador, Mexico, Peru<\/li><\/ul>Note that advertisers registered with the Chinese mainland \(`CN`\) cannot target locations in Australia and Indonesia\.<br><br>To obtain the available targeting locations, use \[\/tool\/targeting\/search\/\]\(([^\)]+)\) or \[\/tool\/region\/\]\(([^\)]+)\)\. \|',
     r'| Nhân khẩu học - Nhắm mục tiêu vị trí | Các khu vực nhắm mục tiêu khả dụng như sau: <ul><li>APAC: Úc, Campuchia, Indonesia, Nhật Bản, Malaysia, New Zealand, Philippines, Singapore, Hàn Quốc, Thái Lan, Việt Nam</li><li>LATAM: Brazil, Chile, Colombia, Ecuador, Mexico, Peru</li></ul>Lưu ý rằng nhà quảng cáo đăng ký tại Trung Quốc đại lục (`CN`) không thể nhắm mục tiêu vị trí tại Úc và Indonesia. | `location_ids` | Truyền ID các vị trí trong các khu vực sau: <ul><li>APAC: Úc, Campuchia, Indonesia, Nhật Bản, Malaysia, New Zealand, Philippines, Singapore, Hàn Quốc, Thái Lan, Việt Nam</li><li>LATAM: Brazil, Chile, Colombia, Ecuador, Mexico, Peru</li></ul>Lưu ý rằng nhà quảng cáo đăng ký tại Trung Quốc đại lục (`CN`) không thể nhắm mục tiêu vị trí tại Úc và Indonesia.<br><br>Để lấy các vị trí nhắm mục tiêu khả dụng, sử dụng [/tool/targeting/search/](\1) hoặc [/tool/region/](\2). |'),

    # Placements table rows
    (r'\| Placement \| <strong>Select Placement<\/strong> with TikTok placement\| `placement_type`<br> `placements` \| <ul><li> Set `placement_type` to `PLACEMENT_TYPE_NORMAL`<\/li><li> AND set `placements` to ` \["PLACEMENT_TIKTOK"\]`\.<\/li><\/ul>\|',
     '| Vị trí hiển thị | <strong>Chọn vị trí hiển thị</strong> với vị trí TikTok | `placement_type`<br> `placements` | <ul><li> Đặt `placement_type` thành `PLACEMENT_TYPE_NORMAL`</li><li> VÀ đặt `placements` thành `["PLACEMENT_TIKTOK"]`.</li></ul> |'),

    (r'\| Placements \| <strong>Select Placement<\/strong> with only TikTok placement \|  <ul><li>`placement_type`<\/li><li> `placements` <\/li><\/ul>\| Set `placement_type` to `PLACEMENT_TYPE_NORMAL`, and set `placements` to ` \["PLACEMENT_TIKTOK"\]` \|',
     '| Vị trí hiển thị | <strong>Chọn vị trí hiển thị</strong> chỉ với vị trí TikTok | <ul><li>`placement_type`</li><li>`placements`</li></ul> | Đặt `placement_type` thành `PLACEMENT_TYPE_NORMAL`, và đặt `placements` thành `["PLACEMENT_TIKTOK"]` |'),

    (r'TikTok placement including search result or Automatic placement',
     'Vị trí TikTok bao gồm kết quả tìm kiếm hoặc Vị trí tự động (Automatic placement)'),

    (r'TikTok placement including search result', 'Vị trí TikTok bao gồm kết quả tìm kiếm'),

    (r'\["PLACEMENT_TIKTOK"\] \*\*Note\*\*: The \[Automatic Search Placement\]\(([^\)]+)\) is enabled by default\.',
     r'`["PLACEMENT_TIKTOK"]` **Lưu ý**: [Vị trí tìm kiếm tự động (Automatic Search Placement)](\1) được bật theo mặc định.'),

    # Destination & Page IDs
    (r'\| Destination - Deeplink type \| Non-deferred deeplinks \| `deeplink_type` \| `NORMAL` or not passed \|',
     '| Điểm đến - Loại liên kết sâu | Liên kết sâu không trì hoãn (Non-deferred deeplinks) | `deeplink_type` | `NORMAL` hoặc không truyền |'),

    (r'\| TikTok Instant Page \| Disabled \| `page_id` \| Not passed \|',
     '| Trang tức thì TikTok | Tắt | `page_id` | Không truyền |'),

    (r'Disabled or enabled with a message event set \(tracking_message_event_set_id\) to measure\.',
     'Tắt hoặc bật với một bộ sự kiện tin nhắn (`tracking_message_event_set_id`) để đo lường.'),

    (r'Specify a TikTok Instant Page via page_id and do not pass landing_page_url, deeplink, deeplink_type, and fallback_type\. The page_id needs to match the same instant messaging app information at the ad group level\.',
     'Chỉ định Trang tức thì TikTok qua `page_id` và không truyền `landing_page_url`, `deeplink`, `deeplink_type` cùng `fallback_type`. `page_id` cần phải khớp với thông tin ứng dụng nhắn tin tức thì ở cấp nhóm quảng cáo.'),

    (r'• To set Destination as Website URL, specify your own URL via landing_page_url\.\s*• To set Destination as Vehicle Inventory Page, do not pass landing_page_url\. An auto-generated Instant Product Page will be returned through the response parameter page_id\.',
     '• Để đặt Điểm đến là URL trang web, chỉ định URL riêng của bạn qua `landing_page_url`. • Để đặt Điểm đến là Trang kho xe (Vehicle Inventory Page), không truyền `landing_page_url`. Một Trang sản phẩm tức thì (Instant Product Page) tự động tạo sẽ được trả về qua tham số phản hồi `page_id`.'),

    (r'• To set Destination as Website URL, specify your own URL via landing_page_url\.\s*• To set Destination as Vehicle Inventory Page, do not pass landing_page_url\.\s*An auto-generated Instant Product Page will be returned through the response parameter page_id\.',
     '• Để đặt Điểm đến là URL trang web, chỉ định URL riêng của bạn qua `landing_page_url`. • Để đặt Điểm đến là Trang kho xe (Vehicle Inventory Page), không truyền `landing_page_url`. Một Trang sản phẩm tức thì (Instant Product Page) tự động tạo sẽ được trả về qua tham số phản hồi `page_id`.'),

    # Automotive Models / Products
    (r'Set product_specific_type to ALL, PRODUCT_SET or CUSTOMIZED_PRODUCTS\.\s*• If product_specific_type is set to ALL, you don\'t need to pass product_set_id and vehicle_ids\.\s*• If product_specific_type is set to PRODUCT_SET, you need to pass product_set_id\.\s*• If product_specific_type is set to CUSTOMIZED_PRODUCTS, you need to pass a maximum of 20 products through vehicle_ids\.',
     'Đặt `product_specific_type` thành `ALL`, `PRODUCT_SET` hoặc `CUSTOMIZED_PRODUCTS`. • Nếu `product_specific_type` được đặt thành `ALL`, bạn không cần truyền `product_set_id` và `vehicle_ids`. • Nếu `product_specific_type` được đặt thành `PRODUCT_SET`, bạn cần truyền `product_set_id`. • Nếu `product_specific_type` được đặt thành `CUSTOMIZED_PRODUCTS`, bạn cần truyền tối đa 20 sản phẩm qua `vehicle_ids`.'),

    (r'• Set catalog_id to ID of the same catalog specified at the ad group level\.\s*• Carousel image selection scope: The product images for products in a catalog \(catalog_id\) will be dynamically chosen as images in the delivering Carousel Ads\. You can specify the scope of product images to choose from using the product_specific_type parameter:\s*• To have the Carousel images dynamically chosen from all products in the catalog, set product_specific_type to ALL, and do not pass product_set_id and vehicle_ids\. The catalog \(catalog_id\) needs to include at least \*\*one\*\* available product\.\s*• To have the Carousel images dynamically chosen from products in a product set, set product_specific_type to PRODUCT_SET, pass product_set_id, and do not pass vehicle_ids\. The specified product_set_id needs to include at least \*\*one\*\* available product\.\s*• To have the images dynamically chosen from a customized product range consisting of up to 20 products, set product_specific_type to CUSTOMIZED_PRODUCTS, pass vehicle_ids, and do not pass product_set_id\. The specified vehicle_ids needs to include at least \*\*one\*\* available product\.\s*• Carousel image type:\s*• Use the main images of the products: By default, the main image URLs of the dynamically selected catalog products will be used as Carousel images\.',
     '• Đặt `catalog_id` thành ID của cùng danh mục được chỉ định ở cấp nhóm quảng cáo. • Phạm vi chọn hình ảnh thẻ xoay vòng: Hình ảnh sản phẩm trong danh mục (`catalog_id`) sẽ được chọn động làm hình ảnh trong Quảng cáo Thẻ xoay vòng đang phân phối. Bạn có thể chỉ định phạm vi hình ảnh sản phẩm để chọn bằng tham số `product_specific_type`: • Để hình ảnh Thẻ xoay vòng được chọn động từ tất cả sản phẩm trong danh mục, đặt `product_specific_type` thành `ALL`, và không truyền `product_set_id` cùng `vehicle_ids`. Danh mục (`catalog_id`) cần bao gồm ít nhất **một** sản phẩm khả dụng. • Để hình ảnh Thẻ xoay vòng được chọn động từ các sản phẩm trong nhóm sản phẩm, đặt `product_specific_type` thành `PRODUCT_SET`, truyền `product_set_id`, và không truyền `vehicle_ids`. Nhóm sản phẩm `product_set_id` được chỉ định cần bao gồm ít nhất **một** sản phẩm khả dụng. • Để hình ảnh được chọn động từ phạm vi sản phẩm tùy chỉnh gồm tối đa 20 sản phẩm, đặt `product_specific_type` thành `CUSTOMIZED_PRODUCTS`, truyền `vehicle_ids`, và không truyền `product_set_id`. `vehicle_ids` được chỉ định cần bao gồm ít nhất **một** sản phẩm khả dụng. • Loại hình ảnh Thẻ xoay vòng: • Sử dụng hình ảnh chính của sản phẩm: Theo mặc định, URL hình ảnh chính của các sản phẩm danh mục được chọn động sẽ được sử dụng làm hình ảnh Thẻ xoay vòng.'),

    (r'Specify one end card through image_ids\. The end card will be displayed at the end of the carousel\. You can get image IDs by using \[\/file\/image\/ad\/upload\/\]\(([^\)]+)\) and \[\/file\/image\/ad\/search\/\]\(([^\)]+)\)\. The image should meet the following requirements at the same time: • Specifications: • File Type: JPG, JPEG, or PNG\. • Image Resolution: a maximum of 1242 x 2340 pixels or 2340 x 1242 pixels\. • Aspect Ratio: a maximum of 9:20 or 20:9\. • File Size: below 50 MB\. • The value of the parameter is_carousel_usable returned from \[\/file\/image\/ad\/search\/\]\(([^\)]+)\) for the image is true\.',
     r'Chỉ định một thẻ kết thúc (end card) qua `image_ids`. Thẻ kết thúc sẽ hiển thị ở cuối thẻ xoay vòng. Bạn có thể lấy ID hình ảnh bằng cách sử dụng [/file/image/ad/upload/](\1) và [/file/image/ad/search/](\2). Hình ảnh phải đáp ứng đồng thời các yêu cầu sau: • Thông số kỹ thuật: • Loại tệp: JPG, JPEG hoặc PNG. • Độ phân giải ảnh: tối đa 1242 x 2340 pixel hoặc 2340 x 1242 pixel. • Tỷ lệ khung hình: tối đa 9:20 hoặc 20:9. • Kích thước tệp: dưới 50 MB. • Giá trị của tham số `is_carousel_usable` trả về từ [/file/image/ad/search/](\3) cho hình ảnh phải là `true`.'),

    # Automotive CTA
    (r'Any of the following options: • Search inventory \(Recommended\) • Learn more • Shop now • Sign up • Contact us • Book now • Read more • View now • Order now',
     'Một trong các tùy chọn sau: • Tìm kiếm kho hàng (Khuyến nghị) • Tìm hiểu thêm • Mua ngay • Đăng ký • Liên hệ với chúng tôi • Đặt ngay • Đọc thêm • Xem ngay • Đặt hàng ngay'),

    (r'Any of the following values: • SEARCH_INVENTORY \(Recommended\) • LEARN_MORE • SHOP_NOW • SIGN_UP • CONTACT_US • BOOK_NOW • READ_MORE • VIEW_MORE • ORDER_NOW',
     'Một trong các giá trị sau: • `SEARCH_INVENTORY` (Khuyến nghị) • `LEARN_MORE` • `SHOP_NOW` • `SIGN_UP` • `CONTACT_US` • `BOOK_NOW` • `READ_MORE` • `VIEW_MORE` • `ORDER_NOW`'),

    # Endpoints note and shop
    (r'- You\'ve gained access to Tiktok API for Business\. See \[Get Started - Step by step workflow\]\(([^\)]+)\) for details\.',
     r'- Bạn đã được cấp quyền truy cập TikTok API for Business. Xem [Bắt đầu - Quy trình từng bước](\1) để biết chi tiết.'),

    (r'Starting Q3, 2025, you cannot use these endpoints to create or update any impacted TikTok Shop Ads types\.',
     'Bắt đầu từ Quý 3 năm 2025, bạn không thể sử dụng các endpoint này để tạo hoặc cập nhật bất kỳ loại Quảng cáo TikTok Shop nào bị ảnh hưởng.'),

    (r'Starting Q3, 2025, you cannot use this endpoint to change the statuses of any impacted TikTok Shop Ads types\.',
     'Bắt đầu từ Quý 3 năm 2025, bạn không thể sử dụng endpoint này để thay đổi trạng thái của bất kỳ loại Quảng cáo TikTok Shop nào bị ảnh hưởng.'),

    (r'Create and manage catalogs using Catalog APIs or TikTok Business Center\.',
     'Tạo và quản lý danh mục bằng API Danh mục hoặc TikTok Business Center.'),

    (r'TikTok Commerce offers TikTok Shops for brands and sellers who want to sell their products directly on their TikTok account\.',
     'TikTok Commerce cung cấp TikTok Shop cho các thương hiệu và người bán muốn bán sản phẩm trực tiếp trên tài khoản TikTok của họ.'),

    (r'Create a campaign using `\/campaign\/create\/`\. The following table only lists the parameters related to Shopping Ads\. To find out the other parameters required for creating campaigns, refer to \[\/campaign\/create\/\]\(([^\)]+)\)\.',
     r'Tạo chiến dịch bằng `/campaign/create/`. Bảng sau chỉ liệt kê các tham số liên quan đến Quảng cáo Mua sắm (Shopping Ads). Để tìm hiểu các tham số khác cần thiết cho việc tạo chiến dịch, hãy tham khảo [/campaign/create/](\1).'),

    (r'Create an ad group using `\/adgroup\/create\/`\.\s*The following table only lists the parameters related to Shopping Ads\. To find out the other parameters required for creating ad groups, refer to \[\/adgroup\/create\/\]\(([^\)]+)\)\.',
     r'Tạo nhóm quảng cáo bằng `/adgroup/create/`. Bảng sau chỉ liệt kê các tham số liên quan đến Quảng cáo Mua sắm (Shopping Ads). Để tìm hiểu các tham số khác cần thiết cho việc tạo nhóm quảng cáo, hãy tham khảo [/adgroup/create/](\1).'),

    (r'Create an ad using `\/ad\/create\/`\. The following table only lists the parameters related to Shopping Ads\. To find out the other parameters required for creating ads, refer to \[\/ad\/create\/\]\(([^\)]+)\)\.',
     r'Tạo mẫu quảng cáo bằng `/ad/create/`. Bảng sau chỉ liệt kê các tham số liên quan đến Quảng cáo Mua sắm (Shopping Ads). Để tìm hiểu các tham số khác cần thiết cho việc tạo quảng cáo, hãy tham khảo [/ad/create/](\1).'),

    # Smart+ common
    (r'N\/A Campaigns created through \[\/campaign\/spc\/create\/\]\(([^\)]+)\) are all Smart\+ Campaigns\.',
     r'K/D. Các chiến dịch được tạo qua [/campaign/spc/create/](\1) đều là Chiến dịch Smart+.'),

    (r'N\/A \*\*Note\*\*: CBO is enabled by default for Smart\+ Campaigns\.',
     'K/D. **Lưu ý**: CBO được bật theo mặc định cho các Chiến dịch Smart+.'),

    (r'N\/A \*\*Note\*\*: If you retrieve Smart\+ Campaigns via \[\/campaign\/get\/\]\(([^\)]+)\), the returned budget_optimize_on will be true\.',
     r'K/D. **Lưu ý**: Nếu bạn truy xuất Chiến dịch Smart+ qua [/campaign/get/](\1), trường `budget_optimize_on` trả về sẽ là `true`.'),

    (r'N\/A CBO is enabled by default for Smart\+ Web Campaigns\.',
     'K/D. CBO được bật theo mặc định cho Chiến dịch Smart+ Web.'),

    (r'N\/A \*\*Note\*\*: If you retrieve Smart\+ Web Campaigns via \[\/campaign\/get\/\]\(([^\)]+)\), the returned budget_optimize_on will be true\.',
     r'K/D. **Lưu ý**: Nếu bạn truy xuất Chiến dịch Smart+ Web qua [/campaign/get/](\1), trường `budget_optimize_on` trả về sẽ là `true`.'),

    (r'Product source details · Use Catalog', 'Chi tiết nguồn sản phẩm · Sử dụng danh mục (Use Catalog)'),

    (r'Any of the following: • Google Play \(for Android\)  • App Store \(for iOS\)',
     'Một trong các lựa chọn sau: • Google Play (dành cho Android) • App Store (dành cho iOS)'),

    (r'Enable "Video templates" in your catalog creative settings, allowing the system to use video templates from your catalogs in the ad\.',
     'Bật "Mẫu video" (Video templates) trong cài đặt tài liệu sáng tạo của danh mục, cho phép hệ thống sử dụng các mẫu video từ danh mục của bạn trong quảng cáo.'),

    (r'Ensure TEMPLATE_VIDEO is included in the catalog_media_settings value\.',
     'Đảm bảo `TEMPLATE_VIDEO` được đưa vào giá trị `catalog_media_settings`.'),

    (r'The catalog must have at least one video template\.\s*• If you select a video template, the video template will be used to automatically generate the catalog video for each catalog product\.\s*• If you don\'t select the video template, the system will automatically select one of your video templates for each catalog product to generate the corresponding catalog video\.',
     'Danh mục phải có ít nhất một mẫu video. • Nếu bạn chọn một mẫu video, mẫu video đó sẽ được sử dụng để tự động tạo video danh mục cho từng sản phẩm danh mục. • Nếu bạn không chọn mẫu video, hệ thống sẽ tự động chọn một trong các mẫu video của bạn cho từng sản phẩm danh mục để tạo video danh mục tương ứng.'),

    (r'To set up the mini series catalog:', 'Để thiết lập danh mục phim ngắn tập (mini series catalog):'),

    (r'1\. Create a \*\*mini series\*\* catalog using \[\/catalog\/create\/\]\(([^\)]+)\)\.',
     r'1. Tạo một danh mục **phim ngắn tập (mini series)** bằng cách sử dụng [/catalog/create/](\1).'),

    (r'Catalog carousel and catalog video', 'Thẻ xoay vòng danh mục và video danh mục (Catalog carousel and catalog video)'),

    (r'Is the catalog video format available\?', 'Định dạng video danh mục có sẵn không?'),

    (r'• one to 50 videos with cover images • one to five ad texts',
     '• 1 đến 50 video có ảnh bìa • 1 đến 5 văn bản quảng cáo'),

    (r'• Specify one to 50 videos \(video_info\) with cover images \(image_info\) • Specify one to five ad texts \(ad_text_list\) • Do not specify music_info and tiktok_item_id',
     '• Chỉ định 1 đến 50 video (`video_info`) kèm ảnh bìa (`image_info`) • Chỉ định 1 đến 5 văn bản quảng cáo (`ad_text_list`) • Không chỉ định `music_info` và `tiktok_item_id`'),
]
