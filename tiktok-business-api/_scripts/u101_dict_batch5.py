#!/usr/bin/env python3
"""
Batch 5: Dịch các cài đặt Bidding, Targeting, Schedule, Identity, Catalog, Tracking tần suất cao (Top 50-175)
"""

BATCH5_RULES = [
    # Top 50 settings
    (r'(?m)^Campaign budget mode$', 'Chế độ ngân sách chiến dịch (Campaign budget mode)'),
    (r'(?m)^Campaign budget strategy$', 'Chiến lược ngân sách chiến dịch (Campaign budget strategy)'),
    (r'(?m)^Campaign budget$', 'Ngân sách chiến dịch (Campaign budget)'),
    (r'(?m)^Ad group name$', 'Tên nhóm quảng cáo (Ad group name)'),
    (r'(?m)^Campaign name$', 'Tên chiến dịch (Campaign name)'),
    (r'(?m)^iOS 14 dedicated campaign$', 'Chiến dịch chuyên dụng iOS 14 (iOS 14 dedicated campaign)'),
    (r'(?m)^Audience targeting optimization mode$', 'Chế độ tối ưu hóa nhắm mục tiêu đối tượng'),
    (r'(?m)^Creative assets · Identity$', 'Tài sản sáng tạo · Danh tính đại diện (Identity)'),
    (r'(?m)^Creative assets · Ad creatives & Ad text$', 'Tài sản sáng tạo · Tài liệu quảng cáo & Văn bản quảng cáo'),
    (r'(?m)^Creative assets · Autoselect from catalog$', 'Tài sản sáng tạo · Tự động chọn từ danh mục'),
    (r'(?m)^Creative assets · Catalog creative settings$', 'Tài sản sáng tạo · Cài đặt tài liệu sáng tạo danh mục'),
    (r'(?m)^Optimization and bidding · Goal$', 'Tối ưu hóa và Đấu thầu · Mục tiêu (Goal)'),
    (r'(?m)^Optimization and bidding · Attribution settings$', 'Tối ưu hóa và Đấu thầu · Cài đặt phân bổ (Attribution settings)'),
    (r'(?m)^Optimization and bidding · Billing event$', 'Tối ưu hóa và Đấu thầu · Sự kiện tính phí (Billing event)'),
    (r'(?m)^Optimization and bidding · Delivery Type$', 'Tối ưu hóa và Đấu thầu · Loại phân phối (Delivery Type)'),
    (r'(?m)^Standard \(default\)$', 'Tiêu chuẩn (Mặc định)'),
    (r'(?m)^Budget and schedule · Budget$', 'Ngân sách và lịch trình · Ngân sách (Budget)'),
    (r'(?m)^Budget and schedule · Schedule$', 'Ngân sách và lịch trình · Lịch trình (Schedule)'),
    (r'(?m)^Budget and schedule · Add spend target per ad group · Daily minimum$', 'Ngân sách và lịch trình · Thêm mục tiêu chi tiêu cho mỗi nhóm quảng cáo · Tối thiểu hàng ngày'),
    (r'(?m)^Budget and schedule · Goal-based budget increase \(when Goal is Value\)$', 'Ngân sách và lịch trình · Tăng ngân sách theo mục tiêu (khi Mục tiêu là Giá trị)'),
    (r'(?m)^Budget mode$', 'Chế độ ngân sách (Budget mode)'),
    (r'(?m)^Product source details · Catalog$', 'Chi tiết nguồn sản phẩm · Danh mục (Catalog)'),
    (r'(?m)^Product source details · Products$', 'Chi tiết nguồn sản phẩm · Sản phẩm (Products)'),

    (r'(?m)^Placements and brand safety · Placement$', 'Vị trí hiển thị và An toàn thương hiệu · Vị trí hiển thị (Placement)'),
    (r'(?m)^Placements and brand safety · User comment$', 'Vị trí hiển thị và An toàn thương hiệu · Bình luận của người dùng'),
    (r'(?m)^Placements and brand safety · Allow video download$', 'Vị trí hiển thị và An toàn thương hiệu · Cho phép tải video xuống'),
    (r'(?m)^Placements and brand safety · Allow video sharing$', 'Vị trí hiển thị và An toàn thương hiệu · Cho phép chia sẻ video'),
    (r'(?m)^Placements and brand safety · Brand safety and suitability$', 'Vị trí hiển thị và An toàn thương hiệu · An toàn và mức độ phù hợp thương hiệu'),
    (r'(?m)^Placements and brand safety · Subplacement \(Optional when Placement includes TikTok\)$', 'Vị trí hiển thị và An toàn thương hiệu · Vị trí phụ (Tùy chọn khi vị trí bao gồm TikTok)'),
    (r'(?m)^Placements and brand safety · Pangle block list$', 'Vị trí hiển thị và An toàn thương hiệu · Danh sách chặn Pangle'),

    (r'(?m)^Tracking · Third-party tracking settings · Track viewability with third-party partner \*\((Không bắt buộc|Optional)\)\*$',
     'Theo dõi · Cài đặt theo dõi của bên thứ ba · Theo dõi khả năng xem với đối tác bên thứ ba *(Không bắt buộc)*'),
    (r'(?m)^Tracking · Third-party tracking settings · Measure brand safety with third-party partner \*\((Không bắt buộc|Optional)\)\*$',
     'Theo dõi · Cài đặt theo dõi của bên thứ ba · Đo lường an toàn thương hiệu với đối tác bên thứ ba *(Không bắt buộc)*'),
    (r'(?m)^Tracking · Third-party tracking settings · Impression tracking URL \*\((Không bắt buộc|Optional)\)\*$',
     'Theo dõi · Cài đặt theo dõi của bên thứ ba · URL theo dõi lượt hiển thị (Impression tracking URL) *(Không bắt buộc)*'),
    (r'(?m)^Tracking · Third-party tracking settings · Click tracking URL \*\((Không bắt buộc|Optional)\)\*$',
     'Theo dõi · Cài đặt theo dõi của bên thứ ba · URL theo dõi lượt nhấp (Click tracking URL) *(Không bắt buộc)*'),
    (r'(?m)^Tracking · TikTok events tracking · Website \*\((Không bắt buộc|Optional)\)\*$',
     'Theo dõi · Theo dõi sự kiện TikTok · Trang web (Website) *(Không bắt buộc)*'),
    (r'(?m)^Tracking · TikTok events tracking · Offline events \*\((Không bắt buộc|Optional)\)\*$',
     'Theo dõi · Theo dõi sự kiện TikTok · Sự kiện ngoại tuyến (Offline events) *(Không bắt buộc)*'),
    (r'(?m)^Tracking · TikTok events tracking · App events \*\((Không bắt buộc|Optional)\)\*$',
     'Theo dõi · Theo dõi sự kiện TikTok · Sự kiện ứng dụng (App events) *(Không bắt buộc)*'),

    (r'(?m)^Targeting optimization mode$', 'Chế độ tối ưu hóa nhắm mục tiêu (Targeting optimization mode)'),
    (r'(?m)^Available targeting setting$', 'Cài đặt nhắm mục tiêu khả dụng'),
    (r'(?m)^Automatic targeting \(targeting_optimization_mode as AUTOMATIC or not specified\)$',
     'Nhắm mục tiêu tự động (`targeting_optimization_mode` là `AUTOMATIC` hoặc không chỉ định)'),
    (r'(?m)^Audience controls · Location$', 'Kiểm soát đối tượng · Vị trí địa lý (Location)'),
    (r'(?m)^Audience controls · Minimum age$', 'Kiểm soát đối tượng · Độ tuổi tối thiểu (Minimum age)'),

    (r'(?m)^Include search results$', 'Bao gồm kết quả tìm kiếm (Include search results)'),
    (r'(?m)^Interactive add-on$', 'Tiện ích tương tác bổ sung (Interactive add-on)'),
    (r'(?m)^Custom User \(custom identity\)$', 'Người dùng tùy chỉnh (danh tính tùy chỉnh)'),
    (r'(?m)^Ad details - Dynamic format$', 'Chi tiết quảng cáo - Định dạng động (Dynamic format)'),
    (r'(?m)^Ad details - Ad format$', 'Chi tiết quảng cáo - Định dạng quảng cáo'),
    (r'(?m)^Ad details - Ad creative$', 'Chi tiết quảng cáo - Tài liệu quảng cáo'),
    (r'(?m)^Ad creative$', 'Tài liệu quảng cáo (Ad creative)'),
    (r'(?m)^Playable$', 'Quảng cáo tương tác (Playable)'),
    (r'(?m)^UNSET or do not pass the parameter$', 'UNSET hoặc không truyền tham số'),
    (r'(?m)^Use specified video creatives to promote your products\.$', 'Sử dụng các tài liệu sáng tạo video đã chỉ định để quảng bá sản phẩm của bạn.'),
    (r'(?m)^App install$', 'Lượt cài đặt ứng dụng (App install)'),
    (r'(?m)^Optimization and bidding · Select value \(when Goal is Value\)$', 'Tối ưu hóa và Đấu thầu · Chọn giá trị (khi Mục tiêu là Giá trị)'),
    (r'(?m)^Optimization and bidding · Time window of the bid strategy \(when Goal is Value\)$', 'Tối ưu hóa và Đấu thầu · Khung thời gian của chiến lược giá thầu (khi Mục tiêu là Giá trị)'),
    (r'(?m)^Optimization and bidding · App$', 'Tối ưu hóa và Đấu thầu · Ứng dụng (App)'),
    (r'(?m)^Optimization and bidding · Select in-app event \(when Goal is In-app event\)$', 'Tối ưu hóa và Đấu thầu · Chọn sự kiện trong ứng dụng (khi Mục tiêu là Sự kiện trong ứng dụng)'),
    (r'(?m)^Optimization and bidding · Attribution source \(for an eligible app\)$', 'Tối ưu hóa và Đấu thầu · Nguồn phân bổ (dành cho ứng dụng đủ điều kiện)'),
    (r'(?m)^Optimization and bidding · Data source \(for an eligible app\)$', 'Tối ưu hóa và Đấu thầu · Nguồn dữ liệu (dành cho ứng dụng đủ điều kiện)'),
    (r'(?m)^Optimization and bidding · Location$', 'Tối ưu hóa và Đấu thầu · Vị trí địa lý (Location)'),
    (r'(?m)^Optimization and bidding · Event · Data connection$', 'Tối ưu hóa và Đấu thầu · Sự kiện · Kết nối dữ liệu'),
    (r'(?m)^Destination URL$', 'URL đích (Destination URL)'),
    (r'(?m)^Set up a catalog campaign$', 'Thiết lập chiến dịch danh mục'),
    (r'(?m)^Catalog campaign$', 'Chiến dịch danh mục (Catalog campaign)'),
    (r'(?m)^To set up the catalog:$', 'Để thiết lập danh mục:'),
    (r'(?m)^Supported with allowlist$', 'Được hỗ trợ với danh sách cho phép (allowlist)'),
    (r'(?m)^Disclaimer$', 'Tuyên bố từ chối trách nhiệm (Disclaimer)'),
    (r'(?m)^Not supported$', 'Không hỗ trợ (Not supported)'),
    (r'(?m)^Specified$', 'Đã chỉ định'),
    (r'(?m)^Pass valid values$', 'Truyền các giá trị hợp lệ'),
    (r'(?m)^Pass a valid value$', 'Truyền một giá trị hợp lệ'),

    # Descriptions & Paragraphs
    (r'Select from the supported attribution setting options for the specific scenario\.',
     'Chọn từ các tùy chọn cài đặt phân bổ được hỗ trợ cho tình huống cụ thể.'),

    (r'Any of the following types: • \*\*Campaign budget\*\*: Your budget will be automatically allocated and optimized across ad groups\. All ad groups must share the same budget and optimization settings\. • \*\*Ad group budget\*\*: Precisely control spend for each ad group, using different budget and optimization settings for each\.',
     'Một trong các loại sau: • **Ngân sách chiến dịch (Campaign budget)**: Ngân sách của bạn sẽ được tự động phân bổ và tối ưu hóa trên các nhóm quảng cáo. Tất cả các nhóm quảng cáo phải dùng chung cài đặt ngân sách và tối ưu hóa. • **Ngân sách nhóm quảng cáo (Ad group budget)**: Kiểm soát chính xác chi tiêu cho từng nhóm quảng cáo, sử dụng cài đặt ngân sách và tối ưu hóa riêng biệt cho từng nhóm.'),

    (r'• When Campaign budget strategy is Campaign budget, specify any of the following modes: • Daily • Lifetime • When Campaign budget strategy is Ad group budget, specify any of the following modes to determine the budget limit for all ad groups: • No limit • Daily • Lifetime',
     '• Khi Chiến lược ngân sách chiến dịch là Ngân sách chiến dịch, hãy chỉ định một trong các chế độ sau: • Hàng ngày (Daily) • Trọn đời (Lifetime) • Khi Chiến lược ngân sách chiến dịch là Ngân sách nhóm quảng cáo, hãy chỉ định một trong các chế độ sau để xác định giới hạn ngân sách cho tất cả các nhóm quảng cáo: • Không giới hạn (No limit) • Hàng ngày (Daily) • Trọn đời (Lifetime)'),

    (r'• When budget_optimize_on is true or not specified, use any of the following values: • BUDGET_MODE_TOTAL • BUDGET_MODE_DYNAMIC_DAILY_BUDGET • When budget_optimize_on is false, use any of the following values: • BUDGET_MODE_INFINITE • BUDGET_MODE_DAY • BUDGET_MODE_TOTAL',
     '• Khi `budget_optimize_on` là `true` hoặc không chỉ định, hãy sử dụng một trong các giá trị sau: • `BUDGET_MODE_TOTAL` • `BUDGET_MODE_DYNAMIC_DAILY_BUDGET` • Khi `budget_optimize_on` là `false`, hãy sử dụng một trong các giá trị sau: • `BUDGET_MODE_INFINITE` • `BUDGET_MODE_DAY` • `BUDGET_MODE_TOTAL`'),

    (r'• When Campaign budget strategy is Campaign budget: • Specify a valid budget\. • When Campaign budget strategy is Ad group budget: • If the budget limit is No limit: • Disabled • If the budget limit is Daily or Lifetime limit: • Specify a valid budget',
     '• Khi Chiến lược ngân sách chiến dịch là Ngân sách chiến dịch: • Chỉ định một ngân sách hợp lệ. • Khi Chiến lược ngân sách chiến dịch là Ngân sách nhóm quảng cáo: • Nếu giới hạn ngân sách là Không giới hạn: • Tắt • Nếu giới hạn ngân sách là Hàng ngày hoặc Trọn đời: • Chỉ định một ngân sách hợp lệ'),

    (r'• When you select a campaign budget mode: • The ad group budget is disabled\. The campaign-level budget will be used as the ad group budget\. • When you select an ad group budget strategy: • If the ad group budget limit is No limit or Lifetime limit, you can use any of the following ad group budget modes: • Lifetime • Daily • If the ad group budget limit is Daily limit, you can use the following ad group budget mode: • Daily \*\*Note\*\*: The ad group budget mode, if specified, must be the same across ad groups within the same campaign\.',
     '• Khi bạn chọn chế độ ngân sách chiến dịch: • Ngân sách nhóm quảng cáo bị tắt. Ngân sách cấp chiến dịch sẽ được sử dụng làm ngân sách nhóm quảng cáo. • Khi bạn chọn chiến lược ngân sách nhóm quảng cáo: • Nếu giới hạn ngân sách nhóm là Không giới hạn hoặc Giới hạn trọn đời, bạn có thể sử dụng bất kỳ chế độ ngân sách nhóm quảng cáo nào sau đây: • Trọn đời • Hàng ngày • Nếu giới hạn ngân sách nhóm là Giới hạn hàng ngày, bạn có thể sử dụng chế độ ngân sách nhóm sau: • Hàng ngày **Lưu ý**: Chế độ ngân sách nhóm quảng cáo (nếu được chỉ định) phải giống nhau trên các nhóm quảng cáo trong cùng chiến dịch.'),

    (r'• When budget_optimize_on is true at the campaign level, budget_mode and budget are not supported\.\s*• When budget_optimize_on is false and budget_mode is BUDGET_MODE_INFINITE or BUDGET_MODE_TOTAL at the campaign level:\s*• Set budget_mode to BUDGET_MODE_TOTAL or BUDGET_MODE_DYNAMIC_DAILY_BUDGET\s*• Specify a valid budget via budget\s*• When budget_optimize_on is false and budget_mode is BUDGET_MODE_DAY at the campaign level:\s*• Set budget_mode to BUDGET_MODE_DYNAMIC_DAILY_BUDGET\s*• Specify a valid budget via budget\s*\*\*Note\*\*: The budget_mode, if specified, must be the same across ad groups within the same campaign\.',
     '• Khi `budget_optimize_on` là `true` ở cấp chiến dịch, `budget_mode` và `budget` không được hỗ trợ. • Khi `budget_optimize_on` là `false` và `budget_mode` là `BUDGET_MODE_INFINITE` hoặc `BUDGET_MODE_TOTAL` ở cấp chiến dịch: • Đặt `budget_mode` thành `BUDGET_MODE_TOTAL` hoặc `BUDGET_MODE_DYNAMIC_DAILY_BUDGET` • Chỉ định ngân sách hợp lệ qua `budget` • Khi `budget_optimize_on` là `false` và `budget_mode` là `BUDGET_MODE_DAY` ở cấp chiến dịch: • Đặt `budget_mode` thành `BUDGET_MODE_DYNAMIC_DAILY_BUDGET` • Chỉ định ngân sách hợp lệ qua `budget` **Lưu ý**: `budget_mode` (nếu được chỉ định) phải giống nhau trên các nhóm quảng cáo trong cùng chiến dịch.'),

    (r'• When budget_optimize_on is true or not specified:\s*• Specify a valid value\.\s*• When budget_optimize_on is false:\s*• If budget_mode is BUDGET_MODE_INFINITE:\s*• Not specified\s*• If budget_mode is BUDGET_MODE_DAY or BUDGET_MODE_TOTAL:\s*• Specify a valid value',
     '• Khi `budget_optimize_on` là `true` hoặc không chỉ định: • Chỉ định một giá trị hợp lệ. • Khi `budget_optimize_on` là `false`: • Nếu `budget_mode` là `BUDGET_MODE_INFINITE`: • Không chỉ định • Nếu `budget_mode` là `BUDGET_MODE_DAY` hoặc `BUDGET_MODE_TOTAL`: • Chỉ định một giá trị hợp lệ'),

    (r'• To have the system auto-generate the ad name, set this field to ""\(empty string\)\.\s*• To customize the ad name, specify a non-empty string value\.',
     '• Để hệ thống tự động tạo tên quảng cáo, hãy đặt trường này thành `""` (chuỗi rỗng). • Để tùy chỉnh tên quảng cáo, hãy chỉ định một chuỗi giá trị không rỗng.'),

    (r'• To set a campaign budget, set this field to true or leave it unspecified\.\s*• To set an ad group budget, set this field to false\.',
     '• Để thiết lập ngân sách chiến dịch, hãy đặt trường này thành `true` hoặc để trống. • Để thiết lập ngân sách nhóm quảng cáo, hãy đặt trường này thành `false`.'),

    (r'Any of the following options: • All products • Product set • Specific products with a maximum of 20 products',
     'Một trong các tùy chọn sau: • Tất cả sản phẩm • Nhóm sản phẩm • Sản phẩm cụ thể với tối đa 20 sản phẩm'),

    (r'You can also choose `advertiser_role` that you want to assign to the members invited\.',
     'Bạn cũng có thể chọn `advertiser_role` mà bạn muốn gán cho các thành viên được mời.'),

    (r'Make sure to specify `CATALOG` in the `asset_type` field and `ADMIN` in the `catalog_role` field\.',
     'Đảm bảo chỉ định `CATALOG` trong trường `asset_type` và `ADMIN` trong trường `catalog_role`.'),

    (r'Goal-based budget increase \(when Campaign budget strategy is Campaign budget and campaign budget mode is daily\)',
     'Tăng ngân sách theo mục tiêu (khi Chiến lược ngân sách chiến dịch là Ngân sách chiến dịch và chế độ ngân sách là hàng ngày)'),

    (r'Specify a valid value when identity_type is BC_AUTH_TT',
     'Chỉ định một giá trị hợp lệ khi `identity_type` là `BC_AUTH_TT`'),

    (r'Pass a valid value when identity_type is BC_AUTH_TT',
     'Truyền một giá trị hợp lệ khi `identity_type` là `BC_AUTH_TT`'),

    (r'Pass a valid value To get the list of identities under your ad account, use \[\/identity\/get\/\]\(([^\)]+)\)\.',
     r'Truyền một giá trị hợp lệ. Để lấy danh sách danh tính thuộc tài khoản quảng cáo của bạn, sử dụng [/identity/get/](\1).'),

    (r'Any of the following types: • Android App • iOS App \*\*Note\*\*: When you select a campaign budget mode, this setting must be the same across ad groups within the same campaign\.',
     'Một trong các loại sau: • Ứng dụng Android • Ứng dụng iOS **Lưu ý**: Khi bạn chọn chế độ ngân sách chiến dịch, cài đặt này phải giống nhau trên các nhóm quảng cáo trong cùng chiến dịch.'),

    (r'3\. Check the product handling results\.\s*- For CSV feed and JSON schema, use \[\/catalog\/product\/log\/\]\(([^\)]+)\)\.\s*- Pass in the `feed_log_id` obtained from Step 2\. If the field `error_affected_products` in the response is not null, examine the issue details and return to Step 2 to reupload the product\.\s*- For online feed, use \[\/catalog\/feed\/log\/\]\(([^\)]+)\)\.\s*- Pass in the `feed_id` obtained from Step 2\. If the field `error_count` in the response is not 0, examine your online feed and return to Step 2 to reupload the product\.',
     r'3. Kiểm tra kết quả xử lý sản phẩm. - Đối với nguồn cấp CSV và lược đồ JSON, sử dụng [/catalog/product/log/](\1). Truyền `feed_log_id` nhận được từ Bước 2. Nếu trường `error_affected_products` trong phản hồi khác null, hãy kiểm tra chi tiết sự cố và quay lại Bước 2 để tải lại sản phẩm lên. - Đối với nguồn cấp trực tuyến, sử dụng [/catalog/feed/log/](\2). Truyền `feed_id` nhận được từ Bước 2. Nếu trường `error_count` trong phản hồi khác 0, hãy kiểm tra nguồn cấp trực tuyến và quay lại Bước 2 để tải lại sản phẩm lên.'),

    (r'3\. Check the product handling results using \[\/catalog\/product\/log\/\]\(([^\)]+)\)\.',
     r'3. Kiểm tra kết quả xử lý sản phẩm bằng [/catalog/product/log/](\1).'),

    (r'Specify a piece of music supported in Catalog Carousel Ads\.',
     'Chỉ định một đoạn nhạc được hỗ trợ trong Quảng cáo Thẻ xoay vòng danh mục (Catalog Carousel Ads).'),

    (r'Generate a dynamic video based on information from the product catalog',
     'Tự động tạo video động dựa trên thông tin từ danh mục sản phẩm'),

    (r'Search campaign\*\*Disabled\*\*is_search_campaignfalse or not specified',
     '| Chiến dịch tìm kiếm | **Tắt (Disabled)** | `is_search_campaign` | `false` hoặc không chỉ định |'),
]
