#!/usr/bin/env python3
"""
Batch 3: Dịch các mẫu câu điều kiện, ghi chú Note, định vị đối tượng, danh tính và cài đặt chiến dịch
"""

BATCH3_RULES = [
    # Ghi chú allowlist và điều kiện chung
    (r'Specify valid values or not specified \*\*Note\*\*: When at the campaign level rta_id is specified, this setting is not supported\.',
     'Chỉ định các giá trị hợp lệ hoặc không chỉ định. **Lưu ý**: Khi `rta_id` được chỉ định ở cấp chiến dịch, cài đặt này không được hỗ trợ.'),

    (r'Optimization location \(Promotion type\)', 'Vị trí tối ưu hóa (Loại quảng bá)'),
    (r'Optimization location<br>\(Promotion type\)', 'Vị trí tối ưu hóa<br>(Loại quảng bá)'),

    (r'Any of the following types: • Standard Event • Custom Conversion \*\*Note\*\*: When you select a campaign budget mode, this setting, if specified, must be the same across ad group within the same campaign\.',
     'Một trong các loại sau: • Sự kiện tiêu chuẩn (Standard Event) • Chuyển đổi tùy chỉnh (Custom Conversion) **Lưu ý**: Khi bạn chọn chế độ ngân sách chiến dịch, cài đặt này (nếu được chỉ định) phải giống nhau trên các nhóm quảng cáo trong cùng chiến dịch.'),

    (r'Any of the following types: • Standard Event • Custom Conversion \*\*Note\*\*: When you select a campaign budget mode, this setting, if specified, must be the same across ad groups within the same campaign\.',
     'Một trong các loại sau: • Sự kiện tiêu chuẩn (Standard Event) • Chuyển đổi tùy chỉnh (Custom Conversion) **Lưu ý**: Khi bạn chọn chế độ ngân sách chiến dịch, cài đặt này (nếu được chỉ định) phải giống nhau trên các nhóm quảng cáo trong cùng chiến dịch.'),

    (r'Disable or enabled with any of the following partners: • DoubleVerify • IAS with IAS wrapped tag • Zefr \*\*Note\*\*: When you configure both the "Track viewability with third-party partner" and "Measure brand safety with third-party partner" settings: • Nếu bạn đặt một trong hai cài đặt này là IAS, bạn phải đặt cả hai là IAS và chỉ định cùng một thẻ bọc IAS\. • Nếu bạn đặt một trong hai cài đặt này là Zefr, bạn phải đặt cả hai là Zefr\.',
     'Tắt hoặc bật với bất kỳ đối tác nào sau đây: • DoubleVerify • IAS với thẻ bọc IAS • Zefr **Lưu ý**: Khi bạn định cấu hình cả cài đặt "Theo dõi khả năng xem với đối tác bên thứ ba" và "Đo lường an toàn thương hiệu với đối tác bên thứ ba": • Nếu bạn đặt một trong hai cài đặt này là IAS, bạn phải đặt cả hai là IAS và chỉ định cùng một thẻ bọc IAS. • Nếu bạn đặt một trong hai cài đặt này là Zefr, bạn phải đặt cả hai là Zefr.'),

    (r'- Bạn đã được cấp quyền truy cập TikTok API for Business\. Xem chi tiết tại \[Get Started - Step by step workflow\]\(([^\)]+)\)\.',
     r'- Bạn đã được cấp quyền truy cập TikTok API for Business. Xem chi tiết tại [Bắt đầu - Quy trình từng bước](\1).'),

    (r'Any of the following options: • Người dùng được ủy quyền \(Authorized User\) • Người dùng TikTok \(TikTok User\) • Người dùng tài khoản TikTok trong Business Center',
     'Một trong các tùy chọn sau: • Người dùng được ủy quyền (Authorized User) • Người dùng TikTok (TikTok User) • Người dùng tài khoản TikTok trong Trung tâm doanh nghiệp (Business Center)'),

    (r'Bật hoặc tắt \(Enabled hoặc Disabled\) \*\*Note\*\*: When at the campaign level Realtime API is enabled, this setting is not supported\.',
     'Bật hoặc tắt (Enabled hoặc Disabled) **Lưu ý**: Khi Realtime API được bật ở cấp chiến dịch, cài đặt này không được hỗ trợ.'),

    (r'Bật hoặc tắt \(Enabled hoặc Disabled\) \*\*Note\*\*: This setting is only supported for advertisers who are registered in the US or Canada\.',
     'Bật hoặc tắt (Enabled hoặc Disabled) **Lưu ý**: Cài đặt này chỉ được hỗ trợ cho các nhà quảng cáo đã đăng ký tại Hoa Kỳ hoặc Canada.'),

    (r'Bật hoặc tắt \(Enabled hoặc Disabled\)\. Để bật cài đặt này, các điều kiện sau đây phải được đáp ứng: • At the campaign level: CBO is disabled\. • At the ad group level: • Ad group budget is Daily • Goal is Value • Bid Strategy is Target ROAS • Time window of the bid strategy is Day 0 ROAS',
     'Bật hoặc tắt (Enabled hoặc Disabled). Để bật cài đặt này, các điều kiện sau đây phải được đáp ứng: • Ở cấp chiến dịch: CBO bị tắt. • Ở cấp nhóm quảng cáo: • Ngân sách nhóm quảng cáo là Hàng ngày • Mục tiêu là Giá trị • Chiến lược giá thầu là ROAS mục tiêu • Khung thời gian của chiến lược giá thầu là ROAS Ngày 0'),

    (r'• Để sử dụng lời kêu gọi hành động động, hãy chỉ định call_to_action_id\. • To use standard call to action, specify call_to_action_list\. \*\*Note\*\*: If you set identity_type within the creative_info object to TT_USER, BC_AUTH_TT, or AUTH_CODE, call_to_action_id is required\.',
     '• Để sử dụng lời kêu gọi hành động động, hãy chỉ định `call_to_action_id`. • Để sử dụng lời kêu gọi hành động tiêu chuẩn, chỉ định `call_to_action_list`. **Lưu ý**: Nếu bạn đặt `identity_type` trong đối tượng `creative_info` thành `TT_USER`, `BC_AUTH_TT` hoặc `AUTH_CODE`, thì `call_to_action_id` là bắt buộc.'),

    (r'Truyền một giá trị hợp lệ To get the list of identities under your ad account, use \[\/identity\/get\/\]\(([^\)]+)\)\.',
     r'Truyền một giá trị hợp lệ. Để lấy danh sách danh tính thuộc tài khoản quảng cáo của bạn, sử dụng [/identity/get/](\1).'),

    (r'\| Advertising objective \| Tìm kiếm khách hàng tiềm năng \(Lead Generation\) \| `objective_type` \| `LEAD_GENERATION` \|',
     '| Mục tiêu quảng cáo | Tìm kiếm khách hàng tiềm năng (Lead Generation) | `objective_type` | `LEAD_GENERATION` |'),

    (r'Note that the following requirements must be met\. Để xem danh sách đầy đủ tất cả các tham số, xem \[\/campaign\/spc\/create\/\]\(([^\)]+)\)\.',
     r'Lưu ý rằng các yêu cầu sau đây phải được đáp ứng. Để xem danh sách đầy đủ tất cả các tham số, xem [/campaign/spc/create/](\1).'),

    (r'Khi Mục tiêu là Giá trị, hãy sử dụng loại sau: • \*\*Giá trị mua hàng \(Purchase value\)\*\* \(còn gọi là VBO IAP, viết tắt của Tối ưu hóa theo giá trị cho mua hàng trong ứng dụng\) • Maximize your revenue from in-app purchases\. • \*\*Ad revenue value\*\* \(also known as VBO IAA, which is short for Value-Based Optimization for in-app advertising\) • Optimize your revenue from in-app advertising\. \*\*Note\*\*: When you select a campaign budget mode, this setting, if specified, must be the same across ad group within the same campaign\.',
     'Khi Mục tiêu là Giá trị, hãy sử dụng loại sau: • **Giá trị mua hàng (Purchase value)** (còn gọi là VBO IAP, viết tắt của Tối ưu hóa theo giá trị cho mua hàng trong ứng dụng) • Tối đa hóa doanh thu từ mua hàng trong ứng dụng. • **Giá trị doanh thu quảng cáo (Ad revenue value)** (còn gọi là VBO IAA, viết tắt của Tối ưu hóa theo giá trị cho quảng cáo trong ứng dụng) • Tối ưu hóa doanh thu từ quảng cáo trong ứng dụng. **Lưu ý**: Khi bạn chọn chế độ ngân sách chiến dịch, cài đặt này (nếu được chỉ định) phải giống nhau trên các nhóm quảng cáo trong cùng chiến dịch.'),

    (r'When budget_optimize_on is true hoặc không chỉ định and budget_mode is BUDGET_MODE_DYNAMIC_DAILY_BUDGET: • To enable the setting, use the following value: • AUTO_BUDGET_INCREASE\. Allow your budget to automatically increase when your ads are performing well and target CPA, Day 0 target ROAS, and budget requirements are met\. Your daily budget will be allowed to automatically increase by 20%, up to 10 times per day, when your budget utilization reaches 90% or more\. Your daily budget will reset to your original daily budget each day\. • To disable the setting: • Not specified \*\*Note\*\*: Enabling Goal-based budget increase is currently an allowlist-only feature\. If you would like to access it, please contact your TikTok representative\.',
     'Khi `budget_optimize_on` là `true` hoặc không chỉ định và `budget_mode` là `BUDGET_MODE_DYNAMIC_DAILY_BUDGET`: • Để bật cài đặt, sử dụng giá trị: • `AUTO_BUDGET_INCREASE`. Cho phép ngân sách của bạn tự động tăng khi quảng cáo đang hoạt động tốt và đáp ứng các yêu cầu về CPA mục tiêu, ROAS mục tiêu Ngày 0 và ngân sách. Ngân sách hàng ngày của bạn sẽ được phép tự động tăng 20%, tối đa 10 lần mỗi ngày, khi tỷ lệ sử dụng ngân sách đạt 90% trở lên. Ngân sách hàng ngày sẽ được đặt lại về ngân sách ban đầu mỗi ngày. • Để tắt cài đặt: • Không chỉ định. **Lưu ý**: Bật Tăng ngân sách dựa trên mục tiêu hiện là tính năng chỉ dành cho danh sách cho phép (allowlist-only). Nếu bạn muốn truy cập, vui lòng liên hệ với đại diện TikTok của bạn.'),

    (r'Để tìm hiểu về the supported attribution setting options for different scenarios, see \[Attribution window and event count - Website conversions\]\(([^\)]+)\)\.',
     r'Để tìm hiểu về các tùy chọn cài đặt phân bổ được hỗ trợ cho các tình huống khác nhau, xem [Khung phân bổ và số lượng sự kiện - Chuyển đổi trên trang web](\1).'),

    (r'Để tìm hiểu về the supported attribution setting options for different scenarios, see \[Attribution window and event count - App promotion\]\(([^\)]+)\)\.',
     r'Để tìm hiểu về các tùy chọn cài đặt phân bổ được hỗ trợ cho các tình huống khác nhau, xem [Khung phân bổ và số lượng sự kiện - Quảng bá ứng dụng](\1).'),

    (r'Audience controls · Exclude audience \*\((Không bắt buộc|Optional)\)\*',
     'Kiểm soát đối tượng · Loại trừ đối tượng *(Không bắt buộc)*'),

    (r'• Bắt buộc khi optimization_goal is set to CONVERT or VALUE\.\s*• Để lấy danh sách Pixel trong tài khoản quảng cáo của bạn, sử dụng (\[\/pixel\/list\/\]\([^\)]+\))\.',
     r'• Bắt buộc khi `optimization_goal` được đặt thành `CONVERT` hoặc `VALUE`. • Để lấy danh sách Pixel trong tài khoản quảng cáo của bạn, sử dụng \1.'),

    (r'> Starting Q3, 2025, \[GMV Max\]\(([^\)]+)\) will be the default and only supported campaign type for TikTok Shop Ads\. If you create ads using the Product Sales objective and TikTok Shop as your sales destination, you will no longer be able to use the API to create, edit, or duplicate \[LIVE Shopping Ads\]\(([^\)]+)\), \[Quảng cáo mua sắm sản phẩm \(Product Shopping Ads\)\]\(([^\)]+)\), or \[Quảng cáo mua sắm qua video \(Video Shopping Ads\)\]\(([^\)]+)\)\. Please migrate to the \[GMV Max API\]\(([^\)]+)\) as early as possible\. If you have questions or need support, please contact your TikTok representative\.\s*Learn more about \[the detailed changes by ad type and endpoint\]\(([^\)]+)\)\.',
     r'> Bắt đầu từ Quý 3 năm 2025, [GMV Max](\1) sẽ là loại chiến dịch mặc định và duy nhất được hỗ trợ cho Quảng cáo TikTok Shop. Nếu bạn tạo quảng cáo bằng mục tiêu Bán sản phẩm (Product Sales) và TikTok Shop làm điểm đến bán hàng, bạn sẽ không còn có thể sử dụng API để tạo, chỉnh sửa hoặc nhân bản [Quảng cáo mua sắm qua LIVE (LIVE Shopping Ads)](\2), [Quảng cáo mua sắm sản phẩm (Product Shopping Ads)](\3), hoặc [Quảng cáo mua sắm qua video (Video Shopping Ads)](\4). Vui lòng chuyển đổi sang [GMV Max API](\5) càng sớm càng tốt. Nếu bạn có thắc mắc hoặc cần hỗ trợ, vui lòng liên hệ với đại diện TikTok của bạn. Tìm hiểu thêm về [các thay đổi chi tiết theo loại quảng cáo và endpoint](\6).'),

    (r'Được hỗ trợ với danh sách cho phép \(allowlist\) \*\*Note\*\*: Gender targeting in Smart\+ Campaigns is currently an allowlist-only feature\. If you would like to access it, please contact your TikTok representative\.',
     'Được hỗ trợ với danh sách cho phép (allowlist). **Lưu ý**: Nhắm mục tiêu theo giới tính trong Chiến dịch Smart+ hiện là tính năng chỉ dành cho danh sách cho phép (allowlist-only). Nếu bạn muốn truy cập, vui lòng liên hệ với đại diện TikTok của bạn.'),

    (r'Chỉ định các video bổ sung via video_info and cover images via image_info\.',
     'Chỉ định các video bổ sung qua `video_info` và hình ảnh bìa qua `image_info`.'),

    (r'• Để thiết lập ngân sách chiến dịch, hãy đặt trường này thành true hoặc không chỉ định\.\s*• Để thiết lập ngân sách nhóm quảng cáo, hãy đặt trường này thành false\.',
     '• Để thiết lập ngân sách chiến dịch, hãy đặt trường này thành `true` hoặc không chỉ định. • Để thiết lập ngân sách nhóm quảng cáo, hãy đặt trường này thành `false`.'),

    (r'Tiện ích tương tác bổ sung \(Interactive add-ons\) \*\((Không bắt buộc|Optional)\)\* \(When the ad creatives include videos\)',
     'Tiện ích tương tác bổ sung (Interactive add-ons) *(Không bắt buộc)* (Khi tài liệu quảng cáo bao gồm video)'),

    (r'Deferred deeplink \*\((Không bắt buộc|Optional)\)\* \(When Destination is Google Play\/App Store\)',
     'Liên kết sâu trì hoãn (Deferred deeplink) *(Không bắt buộc)* (Khi Điểm đến là Google Play/App Store)'),

    (r'Optimization and bidding ·\s*Bid Strategy and \*\((Không bắt buộc|Optional)\)\* Target ROAS',
     'Tối ưu hóa và Đấu thầu · Chiến lược giá thầu và *(Không bắt buộc)* ROAS mục tiêu'),

    (r'• Bắt buộc khi Goal is Conversion or Value\.\s*• When Goal is Value, specify the optimization event as purchase value \(ACTIVE_PAY\)\.',
     '• Bắt buộc khi Mục tiêu là Chuyển đổi hoặc Giá trị. • Khi Mục tiêu là Giá trị, hãy chỉ định sự kiện tối ưu hóa là Giá trị mua hàng (`ACTIVE_PAY`).'),

    (r'• Bắt buộc khi Goal is Conversion or Value\.\s*• Khi Goal is Value, chỉ định sự kiện tối ưu hóa là giá trị mua hàng \(ACTIVE_PAY\)\.',
     '• Bắt buộc khi Mục tiêu là Chuyển đổi hoặc Giá trị. • Khi Mục tiêu là Giá trị, hãy chỉ định sự kiện tối ưu hóa là Giá trị mua hàng (`ACTIVE_PAY`).'),

    # Gaming Compliance
    (r'Any of the following options: • Agreed • By agreeing to the policy, you confirm and attest that any gaming application, product or service \(game\) you desire to advertise on TikTok, including any associated URL\(s\), \(a\) complies with all applicable laws and regulations of the jurisdictions where the game can be accessed or played, and upon request, can provide supporting documentation as evidence of why the game is not considered illegal gambling or lottery; and \(b\) has not been and is not part of any investigation or lawsuit regarding the game\'s legality or regulatory compliance\. • Not agreed',
     'Một trong các tùy chọn sau: • Đồng ý (Agreed) • Bằng việc đồng ý với chính sách này, bạn xác nhận và chứng thực rằng bất kỳ ứng dụng trò chơi, sản phẩm hoặc dịch vụ nào (trò chơi) mà bạn muốn quảng cáo trên TikTok, bao gồm mọi URL liên quan, (a) tuân thủ tất cả các luật và quy định hiện hành của các khu vực tài phán nơi trò chơi có thể được truy cập hoặc chơi, và theo yêu cầu, có thể cung cấp tài liệu hỗ trợ làm bằng chứng về lý do tại sao trò chơi không bị coi là cờ bạc hoặc xổ số bất hợp pháp; và (b) chưa từng và không tham gia vào bất kỳ cuộc điều tra hoặc vụ kiện nào liên quan đến tính hợp pháp hoặc tuân thủ quy định của trò chơi. • Không đồng ý (Not agreed)'),

    (r'Any of the following values: • true • false \*\*Note\*\*: Agreeing to the Compliance Assurance Policy for Gaming Advertisers on TikTok is currently an allowlist-only feature\. If you would like to access it, please contact your TikTok representative\.',
     'Một trong các giá trị sau: • `true` • `false` **Lưu ý**: Đồng ý với Chính sách đảm bảo tuân thủ cho các nhà quảng cáo trò chơi trên TikTok hiện là tính năng chỉ dành cho danh sách cho phép (allowlist-only). Nếu bạn muốn truy cập, vui lòng liên hệ với đại diện TikTok của bạn.'),

    # Destination & Product link
    (r'Website - Product link', 'Trang web - Liên kết sản phẩm (Website - Product link)'),
    (r'Instant Product Page', 'Trang sản phẩm tức thì (Instant Product Page)'),

    (r'SHOPPING_ADS \*\*Note\*\*: shopping_ads_fallback_type cannot be set to SHOPPING_ADS in any of the following scenarios:\s*• ad_format is set to SINGLE_VIDEO and vertical_video_strategy is set to SINGLE_VIDEO\.\s*•\s*ad_format is set to CATALOG_CAROUSEL\.',
     '`SHOPPING_ADS` **Lưu ý**: Không thể đặt `shopping_ads_fallback_type` thành `SHOPPING_ADS` trong bất kỳ trường hợp nào sau đây: • `ad_format` được đặt thành `SINGLE_VIDEO` và `vertical_video_strategy` được đặt thành `SINGLE_VIDEO`. • `ad_format` được đặt thành `CATALOG_CAROUSEL`.'),

    (r'Event count: Once\.', 'Đếm sự kiện: Một lần (Once).'),

    # Shop setup & BC member permissions
    (r'1\. Add the TikTok Shop to the Business Center\. You can either \[create a TikTok Shop in Seller Center\]\(([^\)]+)\) and \[add a TikTok Shop to the Business Center as Shop admin\]\(([^\)]+)\) or\[ request access to the others\' TikTok Shop in Business Center\]\(([^\)]+)\)\.',
     r'1. Thêm TikTok Shop vào Trung tâm doanh nghiệp (Business Center). Bạn có thể [tạo TikTok Shop trong Seller Center](\1) và [thêm TikTok Shop vào Business Center với tư cách là quản trị viên Shop](\2) hoặc [yêu cầu quyền truy cập vào TikTok Shop của người khác trong Business Center](\3).'),

    (r'- If the returned `user_role` for the Business Center is `STANDARD`, you are a standard member of the Business Center\. Ask one admin for the Business Center to update your permission for the Business Center to admin using \[\/bc\/member\/update\/\]\(([^\)]+)\)\.',
     r'- Nếu `user_role` trả về cho Business Center là `STANDARD`, bạn là thành viên tiêu chuẩn của Business Center. Hãy yêu cầu một quản trị viên của Business Center cập nhật quyền của bạn thành quản trị viên (admin) bằng cách sử dụng [/bc/member/update/](\1).'),

    (r'If the returned `store_role` for the TikTok Shop is not `AD_PROMOTION`, you don\'t have management access to the TikTok Shop\. Ask one admin for the Business Center to share the TikTok Shop with you and grant the TikTok Shop management access using \[\/bc\/asset\/assign\/\]\(([^\)]+)\)\. The Business Center admin needs to specify `asset_type` as `TIKTOK_SHOP` and `store_role` as `AD_PROMOTION`\.',
     r'Nếu `store_role` trả về cho TikTok Shop không phải là `AD_PROMOTION`, bạn không có quyền quản lý TikTok Shop đó. Hãy yêu cầu quản trị viên của Business Center chia sẻ TikTok Shop với bạn và cấp quyền quản lý TikTok Shop bằng [/bc/asset/assign/](\1). Quản trị viên Business Center cần chỉ định `asset_type` là `TIKTOK_SHOP` và `store_role` là `AD_PROMOTION`.'),

    (r'- \[GMV Max Guidelines\]\(https:\/\/ads\.tiktok\.com\/help\/article\/gmv-max-guidelines\)',
     '- [Hướng dẫn GMV Max (GMV Max Guidelines)](https://ads.tiktok.com/help/article/gmv-max-guidelines)'),

    (r'Any of the following values: • AUTH_CODE • TT_USER • BC_AUTH_TT \*\*Note\*\*: Pass values to identity_type and identity_id within the media_info object\.',
     'Một trong các giá trị sau: • `AUTH_CODE` • `TT_USER` • `BC_AUTH_TT` **Lưu ý**: Truyền các giá trị cho `identity_type` và `identity_id` bên trong đối tượng `media_info`.'),

    (r'For Spark Ads identities, pass values to identity_type and identity_id within the media_info object\.',
     'Đối với danh tính Spark Ads, truyền các giá trị cho `identity_type` và `identity_id` bên trong đối tượng `media_info`.'),

    # Creatives list
    (r'Specify one to 50 ad creatives through creative_list\. The ad creatives can be any of the following:\s*• (?:Single Video|Video đơn)\s*• (?:Catalog Video|Video danh mục)\s*• (?:Catalog Carousel|Thẻ xoay vòng danh mục)',
     'Chỉ định từ 1 đến 50 tài liệu quảng cáo sáng tạo qua `creative_list`. Các tài liệu quảng cáo có thể là bất kỳ loại nào sau đây: • Video đơn (Single Video) • Video danh mục (Catalog Video) • Thẻ xoay vòng danh mục (Catalog Carousel)'),
]
