#!/usr/bin/env python3
"""
u102_dict_batch2.py: Exact translations for items 1-82 (frequency == 2) in u102.
"""

BATCH2_RULES = [
    # 1, 2, 3: Bidding & CBO rules
    (r'the bid_price or conversion_bid_price, nếu được chỉ định, phải giống nhau giữa các nhóm quảng cáo trong cùng một chiến dịch\.',
     r'`bid_price` hoặc `conversion_bid_price`, nếu được chỉ định, phải giống nhau giữa các nhóm quảng cáo trong cùng một chiến dịch.'),
    (r'Whenbudget_optimize_on is true or not specified at the campaign level, the conversion_bid_price or bid_price, nếu được chỉ định, phải giống nhau giữa các nhóm quảng cáo trong cùng một chiến dịch\.',
     r'Khi `budget_optimize_on` là `true` hoặc không chỉ định ở cấp chiến dịch, `conversion_bid_price` hoặc `bid_price`, nếu được chỉ định, phải giống nhau giữa các nhóm quảng cáo trong cùng một chiến dịch.'),
    (r'When budget_optimize_on is true or not specified at the campaign level, the conversion_bid_price or bid_price, nếu được chỉ định, phải giống nhau giữa các nhóm quảng cáo trong cùng một chiến dịch\.',
     r'Khi `budget_optimize_on` là `true` hoặc không chỉ định ở cấp chiến dịch, `conversion_bid_price` hoặc `bid_price`, nếu được chỉ định, phải giống nhau giữa các nhóm quảng cáo trong cùng một chiến dịch.'),
    (r'• Bạn chỉ có thể đặt bid_type thành BID_TYPE_CUSTOM trong bất kỳ trường hợp nào sau đây: • Ở cấp chiến dịch, budget_mode là BUDGET_MODE_DYNAMIC_DAILY_BUDGET\s*• Ở cấp nhóm quảng cáo, budget_mode là BUDGET_MODE_DYNAMIC_DAILY_BUDGET',
     r'• Bạn chỉ có thể đặt `bid_type` thành `BID_TYPE_CUSTOM` trong bất kỳ trường hợp nào sau đây: • Ở cấp chiến dịch, `budget_mode` là `BUDGET_MODE_DYNAMIC_DAILY_BUDGET` • Ở cấp nhóm quảng cáo, `budget_mode` là `BUDGET_MODE_DYNAMIC_DAILY_BUDGET`'),

    # 5: Product card attributes
    (r'Product description', 'Mô tả sản phẩm (Product description)'),
    (r'Locations or regions', 'Địa điểm hoặc khu vực (Locations or regions)'),
    (r'Street address', 'Địa chỉ đường phố (Street address)'),
    (r'• Khi cài đặt "Tự động chọn từ danh mục" bị tắt:\s*• Disabled',
     '• Khi cài đặt "Tự động chọn từ danh mục" bị tắt: • Tắt (Disabled)'),
    (r'• Khi cài đặt "Tự động chọn từ danh mục" được bật:\s*• Tắt hoặc bật với tối đa hai thuộc tính sản phẩm để hiển thị chi tiết trên bản xem trước thẻ sản phẩm của bạn:',
     '• Khi cài đặt "Tự động chọn từ danh mục" được bật: • Tắt hoặc bật với tối đa hai thuộc tính sản phẩm để hiển thị chi tiết trên bản xem trước thẻ sản phẩm của bạn:'),
    (r'• When the "Autoselect from catalog" setting is enabled:\s*• Tắt hoặc bật \(Disabled hoặc Enabled\) with up to four product attributes to display:',
     '• Khi cài đặt "Tự động chọn từ danh mục" được bật: • Tắt hoặc bật với tối đa bốn thuộc tính sản phẩm để hiển thị:'),

    # 6 & 8: Title displayed alongside specified attributes
    (r'The title of your product or service will be automatically displayed alongside the specified attributes in your ads\. Ví dụ, if you set this field to \["RATING","DESCRIPTION"\], the title, rating and description of your product or service will be displayed in your ads\. Theo mặc định, chỉ tiêu đề của từng sản phẩm hoặc dịch vụ sẽ được hiển thị trong quảng cáo của bạn\.',
     'Tiêu đề của sản phẩm hoặc dịch vụ sẽ được tự động hiển thị cùng với các thuộc tính đã chỉ định trong quảng cáo của bạn. Ví dụ: nếu bạn đặt trường này thành ["RATING","DESCRIPTION"], tiêu đề, xếp hạng và mô tả của sản phẩm hoặc dịch vụ sẽ được hiển thị trong quảng cáo. Theo mặc định, chỉ tiêu đề của từng sản phẩm hoặc dịch vụ sẽ được hiển thị trong quảng cáo của bạn.'),
    (r'\*\*Note\*\*: The maximum number of attributes you can specify depends on your selection:\s*• Max size 3: Allowed only if your selection includes both GENERIC_PRICE and GENERIC_SALE_PRICE \(for example, the two price attributes and one other attribute\)\.\s*• Max size 2: Allowed for all other combinations\.',
     '**Lưu ý**: Số lượng thuộc tính tối đa bạn có thể chỉ định phụ thuộc vào lựa chọn của bạn: • Kích thước tối đa 3: Chỉ được phép nếu lựa chọn của bạn bao gồm cả `GENERIC_PRICE` và `GENERIC_SALE_PRICE` (ví dụ: hai thuộc tính giá và một thuộc tính khác). • Kích thước tối đa 2: Được phép cho tất cả các kết hợp khác.'),

    # 9, 10, 11: Creating catalog ads for app prerequisites
    (r'Creating Upgraded Smart\+ Catalog Ads for App requires setting up a catalog in your Business Center for your app and binding the catalog to your advertiser account\.',
     'Tạo Quảng cáo danh mục Upgraded Smart+ cho Ứng dụng yêu cầu thiết lập một danh mục trong Business Center cho ứng dụng của bạn và liên kết danh mục đó với tài khoản nhà quảng cáo của bạn.'),
    (r'Pass in the `feed_log_id` obtained from Step 2\. If the field `error_affected_products` in the response is 0, the products have been successfully imported into the catalog\.',
     'Truyền `feed_log_id` lấy được từ Bước 2. Nếu trường `error_affected_products` trong phản hồi là 0, các sản phẩm đã được nhập thành công vào danh mục.'),
    (r'Search campaign\*\*Disabled\*\* Để tìm hiểu cách tạo Chiến dịch Upgraded Smart\+ khi bật cài đặt Chiến dịch tìm kiếm, xem',
     'Chiến dịch tìm kiếm (Search campaign) **Tắt (Disabled)** Để tìm hiểu cách tạo Chiến dịch Upgraded Smart+ khi bật cài đặt Chiến dịch tìm kiếm, xem'),

    # 12-16: Campaign budget modes & values
    (r'• When Campaign budget strategy is Automatic campaign budget, specify any of the following modes:\s*•',
     '• Khi Chiến lược ngân sách chiến dịch là Ngân sách chiến dịch tự động, hãy chỉ định bất kỳ chế độ nào sau đây: •'),
    (r'• When budget_optimize_on is true or not specified, use any of the following values\s*:\s*• BUDGET_MODE_',
     '• Khi `budget_optimize_on` là `true` hoặc không chỉ định, hãy sử dụng bất kỳ giá trị nào sau đây: • BUDGET_MODE_'),
    (r'When budget_optimize_on is true or not specified and budget_mode is BUDGET_MODE_DYNAMIC_DAILY_BUDGET at the campaign level, you can optionally set goal-based budget increase via auto_budget_increase_setting\.',
     'Khi `budget_optimize_on` là `true` hoặc không chỉ định và `budget_mode` là `BUDGET_MODE_DYNAMIC_DAILY_BUDGET` ở cấp chiến dịch, bạn có thể tùy chọn thiết lập tăng ngân sách dựa trên mục tiêu qua `auto_budget_increase_setting`.'),
    (r'• When Campaign budget strategy is Automatic campaign budget, specify a valid budget\s*• Khi Chiến lược ngân sách chiến dịch là Ngân sách nhóm quảng cáo tùy chỉnh, không chỉ định',
     '• Khi Chiến lược ngân sách chiến dịch là Ngân sách chiến dịch tự động, hãy chỉ định một ngân sách hợp lệ • Khi Chiến lược ngân sách chiến dịch là Ngân sách nhóm quảng cáo tùy chỉnh, không chỉ định'),
    (r'• When budget_optimize_on is true or not specified, specify a valid value\.\s*• Khi `budget_optimize_on` là `false`, không chỉ định',
     '• Khi `budget_optimize_on` là `true` hoặc không chỉ định, hãy chỉ định một giá trị hợp lệ. • Khi `budget_optimize_on` là `false`, không chỉ định'),

    # 17: Placements note
    (r'Bật hoặc tắt \(Enabled hoặc Disabled\) \*\*Note\*\*: The available placements at the ad group level might vary depending on whether the setting is enabled or disabled\.',
     'Bật hoặc tắt (Enabled hoặc Disabled) **Lưu ý**: Các vị trí hiển thị khả dụng ở cấp nhóm quảng cáo có thể khác nhau tùy thuộc vào việc cài đặt này được bật hay tắt.'),

    # 18-20: RTA & Catalogs
    (r'Specify one of the RTA IDs associated with your ad account\. To obtain the list of RTA IDs associated with your ad account, use (\[/rta/get/\]\([^\)]+\))\.',
     r'Chỉ định một trong các ID RTA liên kết với tài khoản quảng cáo của bạn. Để lấy danh sách các ID RTA liên kết với tài khoản quảng cáo của bạn, sử dụng \1.'),
    (r'Use RTA to automatically select products \*\((Không bắt buộc|Optional)\)\*',
     'Sử dụng RTA để tự động chọn sản phẩm *(Không bắt buộc)*'),
    (r'Specify \*\*a catalog with at least two approved products\*\* \*\*Note\*\*:\s*• When RTA is disabled at the campaign level, the catalog_type of the catalog needs to be APP\.\s*• When RTA is enabled at the campaign level, the catalog_type of the catalog needs to be APP_RTA\.',
     'Chỉ định **một danh mục có ít nhất hai sản phẩm đã được phê duyệt** **Lưu ý**: • Khi RTA bị tắt ở cấp chiến dịch, `catalog_type` của danh mục phải là `APP`. • Khi RTA được bật ở cấp chiến dịch, `catalog_type` của danh mục phải là `APP_RTA`.'),

    # 21-25: Goals, App events, ROAS
    (r'Một trong các giá trị sau: • CLICK • INSTALL \(with optimization_event as ACTIVE\) • Để sử dụng INSTALL,',
     'Một trong các giá trị sau: • `CLICK` • `INSTALL` (với `optimization_event` là `ACTIVE`) • Để sử dụng `INSTALL`,'),
    (r'When optimization_goal is IN_APP_EVENT, specify any of the following:\s*• A Standard Event through\s*optimization_event\s*• An In-App Event through in_app_event\s*• A Custom Conversion along with the associated conversion event through custom_conversion_id and optimization_event',
     'Khi `optimization_goal` là `IN_APP_EVENT`, hãy chỉ định bất kỳ tùy chọn nào sau đây: • Một Sự kiện tiêu chuẩn qua `optimization_event` • Một Sự kiện trong ứng dụng qua `in_app_event` • Một Chuyển đổi tùy chỉnh cùng với sự kiện chuyển đổi liên kết qua `custom_conversion_id` và `optimization_event`'),
    (r'• If optimization_goal is CLICK, INSTALL, or IN_APP_EVENT:\s*• Đặt `bid_type` thành `BID_TYPE_CUSTOM` \(Cost Cap\) hoặc `BID_TYPE_NO_BID`\s*\(Maximum Delivery\)\.\s*• Nếu `bid_type` là `BID_TYPE_CUSTOM`, chỉ định `conversion_bid_price` cùng lúc\.',
     '• Nếu `optimization_goal` là `CLICK`, `INSTALL` hoặc `IN_APP_EVENT`: • Đặt `bid_type` thành `BID_TYPE_CUSTOM` (Giới hạn chi phí) hoặc `BID_TYPE_NO_BID` (Phân phối tối đa). • Nếu `bid_type` là `BID_TYPE_CUSTOM`, hãy chỉ định `conversion_bid_price` cùng lúc.'),
    (r'Bật hoặc tắt \(Enabled hoặc Disabled\) To enable this setting, the following conditions should be met:\s*• At the campaign level: CBO is disabled\.\s*• At the ad group level:\s*• Ad group budget is Daily\s*• Goal is Value\s*• Bid Strategy is Target ROAS\s*• Time window of the bid strategy is Day 0 ROAS',
     'Bật hoặc tắt (Enabled hoặc Disabled) Để bật cài đặt này, các điều kiện sau cần được đáp ứng: • Ở cấp chiến dịch: CBO bị tắt. • Ở cấp nhóm quảng cáo: • Ngân sách nhóm quảng cáo là Hàng ngày • Mục tiêu là Giá trị • Chiến lược giá thầu là ROAS mục tiêu • Khung thời gian của chiến lược giá thầu là ROAS Ngày 0'),
    (r'• At the ad group level:\s*• budget_mode is BUDGET_MODE_DYNAMIC_DAILY_BUDGET\.\s*• optimization_goal is VALUE\.\s*• deep_bid_type is VO_MIN_ROAS\.\s*• vbo_window is ZERO_DAY\.',
     '• Ở cấp nhóm quảng cáo: • `budget_mode` là `BUDGET_MODE_DYNAMIC_DAILY_BUDGET`. • `optimization_goal` là `VALUE`. • `deep_bid_type` là `VO_MIN_ROAS`. • `vbo_window` là `ZERO_DAY`.'),

    # 26-30: Targeting, RTA options
    (r'To learn about the supported targeting settings for each mode, see Cài đặt nhắm mục tiêu có sẵns for different targeting optimization modes in Upgraded Smart\+ Catalog Ads for App\.',
     'Để tìm hiểu các cài đặt nhắm mục tiêu được hỗ trợ cho từng chế độ, xem [Cài đặt nhắm mục tiêu có sẵn cho các chế độ tối ưu hóa nhắm mục tiêu khác nhau trong Quảng cáo danh mục Upgraded Smart+ cho Ứng dụng].'),
    (r'Nhắm lại mục tiêu · Đối tượng tùy chỉnh · Include · Target anyone in catalog or custom audiences \(Optional when both a Catalog Include Audience and a custom audience are specified\)',
     'Nhắm lại mục tiêu · Đối tượng tùy chỉnh · Bao gồm (Include) · Nhắm mục tiêu bất kỳ ai trong danh mục hoặc đối tượng tùy chỉnh (Không bắt buộc khi đã chỉ định cả Đối tượng bao gồm trong danh mục và đối tượng tùy chỉnh)'),
    (r'• When "Use RTA to automatically select products" is enabled at the campaign level: Tất cả sản phẩm\s*• When "Use RTA to automatically select products" is disabled, use any of the following options:\s*• Tất cả sản phẩm\s*• Product set\s*• Specific products with a maximum of 20 products',
     '• Khi "Sử dụng RTA để tự động chọn sản phẩm" được bật ở cấp chiến dịch: Tất cả sản phẩm • Khi "Sử dụng RTA để tự động chọn sản phẩm" bị tắt, hãy sử dụng bất kỳ tùy chọn nào sau đây: • Tất cả sản phẩm • Bộ sản phẩm (Product set) • Sản phẩm cụ thể (tối đa 20 sản phẩm)'),
    (r'• When rta_product_selection_enabled is true at the campaign level: ALL\s*• When rta_product_selection_enabled is false hoặc không chỉ định at the campaign level, set product_specific_type to ALL, PRODUCT_SET or CUSTOMIZED_PRODUCTS\.',
     '• Khi `rta_product_selection_enabled` là `true` ở cấp chiến dịch: `ALL` • Khi `rta_product_selection_enabled` là `false` hoặc không chỉ định ở cấp chiến dịch, hãy đặt `product_specific_type` thành `ALL`, `PRODUCT_SET` hoặc `CUSTOMIZED_PRODUCTS`.'),

    # 31-36: Catalogs creative toggle & iOS App Store
    (r'• When the App is an iOS App: App Store', '• Khi Ứng dụng là Ứng dụng iOS: App Store'),
    (r'• When promotion_type at the ad group level is APP_ANDROID, you can only set the Điểm đến to Download URL',
     '• Khi `promotion_type` ở cấp nhóm quảng cáo là `APP_ANDROID`, bạn chỉ có thể đặt Điểm đến thành URL tải xuống (Download URL)'),
    (r'If you enable auto-selection of catalog creatives \(catalog_creative_toggle is true\), the system will automatically create ads using combinations of two possible formats: catalog carousel, and single video\.',
     'Nếu bạn bật tính năng tự động chọn mẫu quảng cáo danh mục (`catalog_creative_toggle` là `true`), hệ thống sẽ tự động tạo quảng cáo bằng các tổ hợp của hai định dạng có thể: thẻ xoay vòng danh mục và video đơn lẻ.'),
    (r'Tắt hoặc bật \(Disabled hoặc Enabled\) with one to two\s+of the following types:\s*• \*\*Image\*\*\s*• \*\*Video\*\*',
     'Tắt hoặc bật (Disabled hoặc Enabled) với một đến hai loại sau: • **Hình ảnh (Image)** • **Video**'),
    (r'When a generic catalog is specified via catalog_id at the ad group level:\s*• Để tắt cài đặt mẫu sáng tạo danh mục:',
     'Khi một danh mục chung được chỉ định qua `catalog_id` ở cấp nhóm quảng cáo: • Để tắt cài đặt mẫu sáng tạo danh mục:'),

    # 41-45: Conversion strategy & Deeplinks
    (r'• If Goal is Conversion, the strategy can only be Maximum Delivery or Cost Cap\.\s*• Đối với',
     '• Nếu Mục tiêu là Chuyển đổi, chiến lược chỉ có thể là Phân phối tối đa (Maximum Delivery) hoặc Giới hạn chi phí (Cost Cap). • Đối với'),
    (r'• Nếu optimization_goal là CLICK, hãy đặt trường này thành CPC\.\s*• If optimization_goal is CONVERT, specify billing_event as OCPM\.',
     '• Nếu `optimization_goal` là `CLICK`, hãy đặt trường này thành `CPC`. • Nếu `optimization_goal` là `CONVERT`, hãy chỉ định `billing_event` là `OCPM`.'),
    (r'Bật với liên kết sâu \(deeplink\) tùy chỉnh\. The deeplink format can be an Universal Link của Apple hoặc Android App Link bắt đầu bằng http:// hoặc https://',
     'Bật với liên kết sâu (deeplink) tùy chỉnh. Định dạng deeplink có thể là Universal Link của Apple hoặc Android App Link bắt đầu bằng http:// hoặc https://'),
    (r'Specify a deeplink in the format of an Universal Link của Apple hoặc Android App Link bắt đầu bằng http:// hoặc https://',
     'Chỉ định một deeplink theo định dạng Universal Link của Apple hoặc Android App Link bắt đầu bằng http:// hoặc https://'),

    # 49-55: UTM, Destination, Messages
    (r'• When the "Use app profile page to optimize delivery" is enabled at the campaign level:',
     '• Khi "Sử dụng trang hồ sơ ứng dụng để tối ưu hóa phân phối" được bật ở cấp chiến dịch:'),
    (r'Chi tiết nguồn sản phẩm · CatalogChỉ định một \*\*danh mục Auto-Inventory có ít nhất một sản phẩm đã được phê duyệt\*\*',
     '| Chi tiết nguồn sản phẩm · Danh mục (Catalog) | Chỉ định một **danh mục Auto-Inventory có ít nhất một sản phẩm đã được phê duyệt** |'),
    (r'Tham số UTM \(Không bắt buộc đối với URL trang web\)Enabled or disabledutm_paramsWhenlanding_page_url_list',
     '| Tham số UTM (Không bắt buộc đối với URL trang web) | Bật hoặc tắt | `utm_params` | Khi `landing_page_url_list`'),
    (r'Theo dõi · Theo dõi sự kiện TikTok · Trang web \(Optional when Optimization Location is Instant Form\)',
     'Theo dõi · Theo dõi sự kiện TikTok · Trang web (Không bắt buộc khi Vị trí tối ưu hóa là Biểu mẫu tức thì)'),
    (r'Message template \(Welcome message\)Bật Chào đón mọi người bằng tin nhắn tự động do tài khoản của bạn gửi',
     '| Mẫu tin nhắn (Tin nhắn chào mừng) | Bật | Chào đón mọi người bằng tin nhắn tự động do tài khoản của bạn gửi'),
    (r'Tài sản sáng tạo · Disclaimer \*\((Không bắt buộc|Optional)\)\*\s*• Khi cài đặt "Tự động chọn từ danh mục"',
     '| Tài sản sáng tạo · Tuyên bố từ chối trách nhiệm (Disclaimer) *(Không bắt buộc)* | • Khi cài đặt "Tự động chọn từ danh mục"'),

    # 56-65: Destinations & Catalogs
    (r'Điểm đến URLEnabledlanding_page_url_listSpecify a valid URL\. Users will be directed to your website\.',
     '| URL Điểm đến | Bật | `landing_page_url_list` | Chỉ định một URL hợp lệ. Người dùng sẽ được chuyển hướng đến trang web của bạn. |'),
    (r'Tối ưu hóa và giá thầu · Bid Strategy or \*\((Không bắt buộc|Optional)\)\* Target CPAThe strategy can be Cost Cap or Maximum Delivery\.',
     '| Tối ưu hóa và giá thầu · Chiến lược giá thầu hoặc *(Không bắt buộc)* CPA mục tiêu | Chiến lược có thể là Giới hạn chi phí (Cost Cap) hoặc Phân phối tối đa (Maximum Delivery). |'),
    (r'Chi tiết nguồn sản phẩm · CatalogChỉ định \*\*danh mục Thương mại điện tử có ít nhất một sản phẩm đã được phê duyệt\*\*',
     '| Chi tiết nguồn sản phẩm · Danh mục (Catalog) | Chỉ định **danh mục Thương mại điện tử có ít nhất một sản phẩm đã được phê duyệt** |'),
    (r'Deferred deeplink \*\((Không bắt buộc|Optional)\)\* \(When Điểm đến is Google Play/App Store\)Tắt hoặc bật',
     '| Deferred deeplink *(Không bắt buộc)* (Khi Điểm đến là Google Play/App Store) | Tắt hoặc bật |'),
    (r'Build URL parameters \*\((Không bắt buộc|Optional)\)\* • Khi Deferred deeplink bị tắt, cài đặt này không được hỗ trợ',
     '| Tạo tham số URL *(Không bắt buộc)* | • Khi Deferred deeplink bị tắt, cài đặt này không được hỗ trợ |'),
    (r'Interactive add-ons \(Optional when the ad creatives include videos or video posts \)Tắt hoặc bật',
     '| Tiện ích bổ sung tương tác (Không bắt buộc khi mẫu quảng cáo bao gồm video hoặc bài viết video) | Tắt hoặc bật |'),
    (r'The catalog needs to be bound to at least one video template or a video URL needs to be configured for each catalog product\.',
     'Danh mục cần được liên kết với ít nhất một mẫu video hoặc URL video cần được định cấu hình cho từng sản phẩm trong danh mục.'),
    (r'Chi tiết nguồn sản phẩm · CatalogSpecify \*\*a catalog with at least one approved product\*\*\.',
     '| Chi tiết nguồn sản phẩm · Danh mục (Catalog) | Chỉ định **một danh mục có ít nhất một sản phẩm đã được phê duyệt**. |'),
    (r'Chi tiết nguồn sản phẩm · CatalogSpecify \*\*an entertainment catalog with at least one approved product\*\*\.',
     '| Chi tiết nguồn sản phẩm · Danh mục (Catalog) | Chỉ định **một danh mục giải trí có ít nhất một sản phẩm đã được phê duyệt**. |'),
    (r'Điểm đến · Fallback destinationMột trong các tùy chọn sau: • App Store/Google Play • Custom link',
     '| Điểm đến · Điểm đến dự phòng (Fallback destination) | Một trong các tùy chọn sau: • App Store/Google Play • Liên kết tùy chỉnh (Custom link) |'),
    (r'Điểm đến · Fallback destinationMột trong các tùy chọn sau: • App Store • Custom link',
     '| Điểm đến · Điểm đến dự phòng (Fallback destination) | Một trong các tùy chọn sau: • App Store • Liên kết tùy chỉnh (Custom link) |'),
    (r'Tài sản sáng tạo · Cài đặt mẫu sáng tạo danh mụcDisabled or enabled with one to two of the following types:',
     '| Tài sản sáng tạo · Cài đặt mẫu sáng tạo danh mục | Tắt hoặc bật với một đến hai loại sau:'),
    (r'Tài sản sáng tạo · Cài đặt mẫu sáng tạo danh mụcDisabled or enabled with the following type:',
     '| Tài sản sáng tạo · Cài đặt mẫu sáng tạo danh mục | Tắt hoặc bật với loại sau:'),

    # 71-82: Demographics, Placements, HFSS
    (r'Tối ưu hóa và giá thầu · Android & iOSChỉ định bất kỳ mục nào sau đây: • an Android app • an iOS app',
     '| Tối ưu hóa và giá thầu · Android & iOS | Chỉ định bất kỳ mục nào sau đây: • một ứng dụng Android • một ứng dụng iOS |'),
    (r'Tối ưu hóa và giá thầu · Chiến lược giá thầu và \*\((Không bắt buộc|Optional)\)\* CPA mục tiêuMột trong các giá trị sau:',
     '| Tối ưu hóa và giá thầu · Chiến lược giá thầu và *(Không bắt buộc)* CPA mục tiêu | Một trong các giá trị sau:'),
    (r'Nhân khẩu học · Sản phẩm/Thương hiệu HFSSEnabled or disabled • You can enable this setting when your targeting locations include locations in the UK\.',
     '| Nhân khẩu học · Sản phẩm/Thương hiệu HFSS | Bật hoặc tắt • Bạn có thể bật cài đặt này khi các địa điểm nhắm mục tiêu của bạn bao gồm các địa điểm tại Vương quốc Anh. |'),
    (r'Added URL parameters \*\((Không bắt buộc|Optional)\)\*Enabled or disabledutm_paramsChỉ định các giá trị hợp lệ hoặc không chỉ định',
     '| Tham số URL bổ sung *(Không bắt buộc)* | Bật hoặc tắt | `utm_params` | Chỉ định các giá trị hợp lệ hoặc không chỉ định |'),
    (r'Tài sản sáng tạo · IdentityMột trong các tùy chọn sau: • Authorized User • TikTok User • Custom User',
     '| Tài sản sáng tạo · Danh tính (Identity) | Một trong các tùy chọn sau: • Người dùng được ủy quyền (Authorized User) • Người dùng TikTok (TikTok User) • Người dùng tùy chỉnh (Custom User) |'),
    (r'Chỉ định một giá trị hợp lệ khi budget_mode is any of the following values:\s*• BUDGET_MODE_',
     'Chỉ định một giá trị hợp lệ khi `budget_mode` là bất kỳ giá trị nào sau đây: • BUDGET_MODE_'),
    (r'Một trong các tùy chọn sau: • \*\*Automatic Placement\*\* • \*\*Select Placement\*\* with any of the following placements:',
     'Một trong các tùy chọn sau: • **Vị trí tự động (Automatic Placement)** • **Chọn vị trí (Select Placement)** với bất kỳ vị trí nào sau đây:'),
    (r'Không chỉ định hoặc chỉ định ID của một trong các loại danh mục sáng tạo sau: • Product Card • Display Card',
     'Không chỉ định hoặc chỉ định ID của một trong các loại danh mục sáng tạo sau: • Thẻ sản phẩm (Product Card) • Thẻ hiển thị (Display Card)'),
    (r'\bON, or OFF \(or not passed\)', '`ON` hoặc `OFF` (hoặc không truyền)'),
]
