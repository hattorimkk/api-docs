#!/usr/bin/env python3
"""
Cluster 5 translations: Upgraded Smart+ App, non-DC/DC, O2O Catalog, Travel Catalog, Growth Max
- 1843309449749698: Upgraded Smart+ Campaign overview
- 1843309500205058: Upgraded Smart+ App Campaigns overview
- 1853377390815233: Upgraded Smart+ non-DC App Campaign
- 1853377803841537: Upgraded Smart+ DC App Campaign
- 1875231879602658: Upgraded Smart+ App O2O Catalog Ads
- 1875231912916994: Upgraded Smart+ non-DC App O2O Catalog Ads
- 1875231953230418: Upgraded Smart+ DC App O2O Catalog Ads
- 1879220213492353: Upgraded Smart+ App Travel Catalog Ads
- 1868120855134226: Upgraded Smart+ TikTok Growth Max overview
- 1868121865281538: Upgraded Smart+ TikTok Growth Max: Mini Games
- 1853377811982657: Upgraded Smart+ TikTok Growth Max: Mini Dramas
- 1863331595515009: Upgraded Smart+ TikTok Growth Max: Drama Series
"""

CLUSTER5_RULES = [
    # Overview
    (r"Bài viết này hướng dẫn bạn từng bước để tạo an Chiến dịch Upgraded Smart\+\.",
     "Bài viết này hướng dẫn bạn từng bước để tạo một Chiến dịch Upgraded Smart+."),
     
    (r"The Chiến dịch Upgraded Smart\+ feature a new, unified workflow, known as the Upgraded Smart\+ experience\. This streamlined approach simplifies your campaign creation and management\.",
     "Chiến dịch Upgraded Smart+ sở hữu quy trình làm việc thống nhất, mới mẻ được gọi là trải nghiệm Upgraded Smart+. Cách tiếp cận tinh gọn này giúp đơn giản hóa việc tạo và quản lý chiến dịch của bạn."),
     
    (r"The Upgraded Smart\+ API supports an enhanced campaign structure with upgraded Smart\+ experience built-in campaign management capabilities, covering campaign creation, ad group configuration, ad creative setup, and campaign performance monitoring\.",
     "Upgraded Smart+ API hỗ trợ cấu trúc chiến dịch nâng cao với các khả năng quản lý chiến dịch tích hợp trải nghiệm Smart+ được nâng cấp, bao gồm tạo chiến dịch, cấu hình nhóm quảng cáo, thiết lập mẫu quảng cáo và giám sát hiệu suất chiến dịch."),
     
    (r"\*\*You can use Upgraded Smart\+ API to create an Chiến dịch Upgraded Smart\+, and this helps streamline your ad creation experience, and elevate operational efficiency and scalability\.\*\*",
     "**Bạn có thể sử dụng Upgraded Smart+ API để tạo một Chiến dịch Upgraded Smart+, giúp tối ưu hóa quy trình tạo quảng cáo cũng như nâng cao hiệu quả hoạt động và khả năng mở rộng.**"),
     
    (r"- To create an Chiến dịch Upgraded Smart\+ you need relevant permissions\. See \*\*API Reference\*\* to find out permissions required for endpoints \(including the endpoints listed in the \"Steps\" section\) and see \[Update app permissions\]\(\.\./04-get-started/bat-dau\.md#doc-1738855280338946\) to find out how to configure permissions\.",
     "- Để tạo một Chiến dịch Upgraded Smart+, bạn cần có các quyền liên quan. Xem **Tham khảo API (API Reference)** để biết các quyền cần thiết cho các endpoint (bao gồm các endpoint được liệt kê trong phần \"Các bước thực hiện\") và xem [Cập nhật quyền ứng dụng](../04-get-started/bat-dau.md#doc-1738855280338946) để biết cách cấu hình quyền."),
     
    (r"Based on your preference for the advertising objective and Liệu you want to capture search traffic, you can create Upgraded Smart\+ Campaigns as needed:",
     "Dựa trên sở thích của bạn đối với mục tiêu quảng cáo và liệu bạn có muốn tiếp cận lưu lượng tìm kiếm hay không, bạn có thể tạo các Chiến dịch Upgraded Smart+ theo nhu cầu:"),
     
    (r"- Để tìm hiểu cách tạo an Upgraded Smart\+ App Campaign, see \[Create Upgraded Smart\+ App Campaigns\]\(use-case-tao-chien-dich-p1\.md#doc-1843309500205058\)\.",
     "- Để tìm hiểu cách tạo một Chiến dịch Upgraded Smart+ App, xem [Tạo chiến dịch Upgraded Smart+ App](use-case-tao-chien-dich-p1.md#doc-1843309500205058)."),
     
    (r"- Để tìm hiểu cách tạo an Upgraded Smart\+ TikTok Growth Max campaign, see \[Create Upgraded Smart\+ Growth Max campaigns\]\(use-case-tao-chien-dich-p1\.md#doc-1868120855134226\)\.",
     "- Để tìm hiểu cách tạo một chiến dịch Upgraded Smart+ TikTok Growth Max, xem [Tạo chiến dịch Upgraded Smart+ Growth Max](use-case-tao-chien-dich-p1.md#doc-1868120855134226)."),
     
    (r"- Để tìm hiểu cách tạo an Upgraded Smart\+ Web Campaign, see \[Create Upgraded Smart\+ Web Campaigns\]\(use-case-tao-chien-dich-p1\.md#doc-1843309514567809\)\.",
     "- Để tìm hiểu cách tạo một Chiến dịch Upgraded Smart+ Web, xem [Tạo chiến dịch Upgraded Smart+ Web](use-case-tao-chien-dich-p1.md#doc-1843309514567809)."),
     
    (r"- Để tìm hiểu cách tạo an Upgraded Smart\+ Tìm kiếm khách hàng tiềm năng \(Lead Generation\) Campaign, see \[Create Upgraded Smart\+ Lead Generation Campaigns\]\(use-case-tao-chien-dich-p2\.md#doc-1843309531580417\)\.",
     "- Để tìm hiểu cách tạo một Chiến dịch Upgraded Smart+ Tìm kiếm khách hàng tiềm năng, xem [Tạo chiến dịch Upgraded Smart+ Tìm kiếm khách hàng tiềm năng](use-case-tao-chien-dich-p2.md#doc-1843309531580417)."),
     
    (r"- Để tìm hiểu cách tạo Upgraded Smart\+ Quảng cáo danh mục \(Catalog Ads\) for Apps or Upgraded Smart\+ Ads with Website and App Optimization, see \[Catalog Ads and Ads with Website and App Optimization\]\(use-case-tao-chien-dich-p2\.md#doc-1854823297753153\)\.",
     "- Để tìm hiểu cách tạo Upgraded Smart+ Quảng cáo danh mục (Catalog Ads) cho Ứng dụng hoặc Quảng cáo Upgraded Smart+ với Tối ưu hóa Trang web và Ứng dụng, xem [Quảng cáo danh mục và Quảng cáo tối ưu hóa Web & App](use-case-tao-chien-dich-p2.md#doc-1854823297753153)."),
     
    (r"- Để tìm hiểu cách tạo Upgraded Smart\+ Search Ads Campaigns, see \[Create Upgraded Smart\+ Search Ads Campaigns\]\(use-case-tao-chien-dich-p2\.md#doc-1851218290237505\)\.",
     "- Để tìm hiểu cách tạo Chiến dịch Upgraded Smart+ Search Ads, xem [Tạo chiến dịch Upgraded Smart+ Search Ads](use-case-tao-chien-dich-p2.md#doc-1851218290237505)."),
     
    # App Campaigns Overview
    (r"Bài viết này hướng dẫn bạn từng bước để tạo Upgraded Smart\+ App Campaigns using the App Promotion objective\.",
     "Bài viết này hướng dẫn bạn từng bước để tạo Chiến dịch Upgraded Smart+ App bằng mục tiêu Quảng bá ứng dụng (App Promotion)."),
     
    (r"Depending on your iOS 14 Dedicated Campaign \(DC\) requirements and Liệu you plan to leverage a catalog, you can build a new campaign with one of the following setups:",
     "Tùy theo yêu cầu về Chiến dịch chuyên dụng iOS 14 (Dedicated Campaign - DC) và liệu bạn có dự định tận dụng danh mục hay không, bạn có thể xây dựng chiến dịch mới với một trong các thiết lập sau:"),
     
    (r"- To create an Upgraded Smart\+ non-DC App Campaign without a catalog, see \[Create an Upgraded Smart\+ non-DC App Campaign\]\(use-case-tao-chien-dich-p1\.md#doc-1853377390815233\)\.",
     "- Để tạo Chiến dịch Upgraded Smart+ non-DC App không có danh mục, xem [Tạo chiến dịch Upgraded Smart+ non-DC App](use-case-tao-chien-dich-p1.md#doc-1853377390815233)."),
     
    (r"- To create an Upgraded Smart\+ DC App Campaign without a catalog, see \[Create an Upgraded Smart\+ DC App Campaign\]\(use-case-tao-chien-dich-p1\.md#doc-1853377803841537\)\.",
     "- Để tạo Chiến dịch Upgraded Smart+ DC App không có danh mục, xem [Tạo chiến dịch Upgraded Smart+ DC App](use-case-tao-chien-dich-p1.md#doc-1853377803841537)."),
     
    (r"- To create an Upgraded Smart\+ App Campaign powered by an O2O catalog, see \[Create Upgraded Smart\+ App O2O Quảng cáo danh mục \(Catalog Ads\)\]\(use-case-tao-chien-dich-p1\.md#doc-1875231879602658\)\.",
     "- Để tạo Chiến dịch Upgraded Smart+ App sử dụng danh mục O2O, xem [Tạo Upgraded Smart+ App O2O Quảng cáo danh mục](use-case-tao-chien-dich-p1.md#doc-1875231879602658)."),
     
    (r"- To create an Upgraded Smart\+ App Campaign powered by a travel catalog, see \[Create Upgraded Smart\+ App Travel Quảng cáo danh mục \(Catalog Ads\)\]\(use-case-tao-chien-dich-p1\.md#doc-1879220213492353\)\.",
     "- Để tạo Chiến dịch Upgraded Smart+ App sử dụng danh mục du lịch, xem [Tạo Upgraded Smart+ App Travel Quảng cáo danh mục](use-case-tao-chien-dich-p1.md#doc-1879220213492353)."),
     
    # Non-DC App
    (r"An Upgraded Smart\+ non-DC App Campaign is an Upgraded Smart\+ App Campaign with iOS 14 dedicated campaign setting disabled\.",
     "Chiến dịch Upgraded Smart+ non-DC App là Chiến dịch Upgraded Smart+ App đã tắt cài đặt chiến dịch chuyên dụng iOS 14."),
     
    (r"## Các bước thực hiện \(Steps\) for App Install Campaigns",
     "## Các bước thực hiện (Steps) cho Chiến dịch Cài đặt ứng dụng (App Install)"),
     
    (r"An App Install Campaign is an App Campaign that gets people to install and use your app\. For such campaigns, you need to set `app_promotion_type` to `APP_INSTALL`\.",
     "Chiến dịch Cài đặt ứng dụng là một chiến dịch ứng dụng giúp thu hút mọi người cài đặt và sử dụng ứng dụng của bạn. Đối với các chiến dịch như vậy, bạn cần đặt `app_promotion_type` thành `APP_INSTALL`."),
     
    (r"Search campaign\*\*Disabled\*\* Để tìm hiểu cách tạo an Chiến dịch Upgraded Smart\+ with Search campaign setting enabled, see",
     "Chiến dịch tìm kiếm (Search campaign) **Đã tắt** Để tìm hiểu cách tạo Chiến dịch Upgraded Smart+ có bật cài đặt chiến dịch tìm kiếm, xem"),
     
    (r"\*\*Disabled\*\* Để tìm hiểu cách tạo an Upgraded Smart\+ App Campaign with iOS 14 Dedicated Campaign enabled, see \[Create an Upgraded Smart\+ DC App Campaign\]\(use-case-tao-chien-dich-p1\.md#doc-1853377803841537\)\.",
     "**Đã tắt** Để tìm hiểu cách tạo Chiến dịch Upgraded Smart+ App có bật Chiến dịch chuyên dụng iOS 14, xem [Tạo chiến dịch Upgraded Smart+ DC App](use-case-tao-chien-dich-p1.md#doc-1853377803841537)."),
     
    (r"Disabled or enabled \*\*Note\*\*: This setting is only supported for advertisers who are registered in the US or Canada\.",
     "Đã tắt hoặc đã bật **Lưu ý**: Cài đặt này chỉ được hỗ trợ cho các nhà quảng cáo đã đăng ký tại Hoa Kỳ hoặc Canada."),
     
    (r"Not specified or specify a valid value", "Không chỉ định hoặc chỉ định giá trị hợp lệ"),
    
    (r"Any of the following types: • \*\*Campaign budget\*\*: Your budget will be automatically allocated and optimized across ad groups within the campaign\. • \*\*Ad group budget\*\*: Your budget will be allocated to individual ad groups\.",
     "Bất kỳ loại nào sau đây: • **Ngân sách chiến dịch**: Ngân sách của bạn sẽ được tự động phân bổ và tối ưu hóa giữa các nhóm quảng cáo trong chiến dịch. • **Ngân sách nhóm quảng cáo**: Ngân sách của bạn sẽ được phân bổ cho từng nhóm quảng cáo riêng lẻ."),
     
    (r"• To set a campaign budget, set this field to true or leave it unspecified\. • To set an ad group budget, set this field to false\.",
     "• Để đặt ngân sách chiến dịch, hãy đặt trường này thành true hoặc để trống. • Để đặt ngân sách nhóm quảng cáo, hãy đặt trường này thành false."),
     
    (r"• When Campaign budget strategy is Campaign budget, specify any of the following modes: • Daily • Lifetime • When Campaign budget strategy is Ad group budget, do not specify budget_mode\.",
     "• Khi Chiến lược ngân sách chiến dịch là Ngân sách chiến dịch, hãy chỉ định bất kỳ chế độ nào sau đây: • Hàng ngày (Daily) • Trọn đời (Lifetime) • Khi Chiến lược ngân sách chiến dịch là Ngân sách nhóm quảng cáo, không chỉ định budget_mode."),
     
    (r"• When budget_optimize_on is true or not specified, use any of the following values: • BUDGET_MODE_TOTAL • BUDGET_MODE_DAY • When budget_optimize_on is false, do not pass budget_mode\.",
     "• Khi budget_optimize_on là true hoặc không được chỉ định, sử dụng bất kỳ giá trị nào sau đây: • BUDGET_MODE_TOTAL • BUDGET_MODE_DAY • Khi budget_optimize_on là false, không truyền budget_mode."),
     
    (r"Goal-based budget increase \(when Campaign budget strategy is Campaign budget and campaign budget mode is daily\)",
     "Tăng ngân sách theo mục tiêu (Goal-based budget increase - khi Chiến lược ngân sách chiến dịch là Ngân sách chiến dịch và chế độ ngân sách là hàng ngày)"),
     
    # DC App
    (r"An Upgraded Smart\+ DC App Campaign is an Upgraded Smart\+ App Campaign with iOS 14 dedicated campaign setting enabled\.",
     "Chiến dịch Upgraded Smart+ DC App là Chiến dịch Upgraded Smart+ App có bật cài đặt chiến dịch chuyên dụng iOS 14."),
     
    (r"Disabled or enabled \*\*Note\*\*: If you enable this setting, you need to specify an App Profile Page at the ad group level\.",
     "Đã tắt hoặc đã bật **Lưu ý**: Nếu bạn bật cài đặt này, bạn cần chỉ định Trang hồ sơ ứng dụng (App Profile Page) ở cấp nhóm quảng cáo."),
     
    (r"OFF \(or not specified\) or ON", "OFF (hoặc không chỉ định) hoặc ON"),
    
    (r"• If optimization_goal is INSTALL or IN_APP_EVENTand bid_type is BID_TYPE_CUSTOM, specify conversion_bid at the same time\.",
     "• Nếu optimization_goal là INSTALL hoặc IN_APP_EVENT và bid_type là BID_TYPE_CUSTOM, hãy chỉ định conversion_bid cùng lúc."),
     
    (r"• If optimization_goal is CLICK and bid_type is BID_TYPE_CUSTOM, specify bid_price at the same time\.",
     "• Nếu optimization_goal là CLICK và bid_type là BID_TYPE_CUSTOM, hãy chỉ định bid_price cùng lúc."),
     
    (r"• When optimization_goal is VALUE , use any of the following values: • SEVEN_DAYS • ZERO_DAYFor example, SEVEN_DAYS represents that the bid price is calculated for a seven-day window\.",
     "• Khi optimization_goal là VALUE, sử dụng bất kỳ giá trị nào sau đây: • SEVEN_DAYS • ZERO_DAY. Ví dụ: SEVEN_DAYS thể hiện rằng giá thầu được tính toán cho khung thời gian 7 ngày."),
     
    (r'• When the "Use app profile page to optimize delivery" is enabled at the campaign level, Destination can only be TikTok Instant Page\.',
     '• Khi cài đặt "Sử dụng trang hồ sơ ứng dụng để tối ưu hóa phân phối" được bật ở cấp chiến dịch, Đích đến chỉ có thể là Trang tức thì TikTok (TikTok Instant Page).'),
     
    (r"• When campaign_app_profile_page_state at the campaign level is ON, you need to specify an App Profile Page at the ad group level, so you must set landing_page_type to TIKTOK_NATIVE_PAGE\.",
     "• Khi campaign_app_profile_page_state ở cấp chiến dịch là ON, bạn cần chỉ định Trang hồ sơ ứng dụng ở cấp nhóm quảng cáo, vì vậy bạn phải đặt landing_page_type thành TIKTOK_NATIVE_PAGE."),
     
    # App O2O Catalog Ads & Travel Catalog Ads
    (r"\*\*Purchase value\*\* \(also known as VBO IAP, which is short for Value-Based Optimization for in-app purchases\)",
     "**Giá trị mua hàng (Purchase value)** (còn được gọi là VBO IAP, viết tắt của Tối ưu hóa dựa trên giá trị cho giao dịch mua hàng trong ứng dụng)"),
     
    (r"When optimization_goal is VALUE: ACTIVE_PAY \. \*\*Note\*\*: When budget_optimize_on is true at the campaign level, specify the same promotion_type, data_source_id, and optimization_event across ad groups\.",
     "Khi optimization_goal là VALUE: ACTIVE_PAY . **Lưu ý**: Khi budget_optimize_on là true ở cấp chiến dịch, hãy chỉ định cùng promotion_type, data_source_id, và optimization_event giữa các nhóm quảng cáo."),
     
    (r"\*\*Online-to-offline \(O2O\)\*\*", "**Trực tuyến sang ngoại tuyến (Online-to-offline - O2O)**"),
    
    (r"Specify \*\*a travel \(hotel, flight, or destination\) catalog with at least one approved product\*\*",
     "Chỉ định **một danh mục du lịch (khách sạn, chuyến bay hoặc điểm đến) có ít nhất một sản phẩm đã được phê duyệt**"),
     
    (r"Placements · Eligible placements", "Vị trí vị trí quảng cáo · Vị trí vị trí đủ điều kiện (Eligible placements)"),
    (r"Placements · Subplacement \(Optional when Placement includes TikTok\)", "Vị trí vị trí quảng cáo · Vị trí phụ (Không bắt buộc khi Vị trí bao gồm TikTok)"),
    (r"Placements · User comment", "Vị trí vị trí quảng cáo · Bình luận của người dùng (User comment)"),
    
    (r"These settings only apply to ads appearing in TikTok feeds, search results, and Lemon8\. Any previous settings for Pangle will be ignored\.",
     "Các cài đặt này chỉ áp dụng cho quảng cáo xuất hiện trong bảng tin TikTok, kết quả tìm kiếm và Lemon8. Mọi cài đặt trước đây cho Pangle sẽ bị bỏ qua."),
     
    (r"Disabled or enabled with a Hotel Card \(for hotel catalogs only\),  Flight Card \(for flight catalogs only\), or Destination Card \(for destination catalogs only\)",
     "Đã tắt hoặc đã bật với Thẻ khách sạn (Hotel Card - chỉ dành cho danh mục khách sạn), Thẻ chuyến bay (Flight Card - chỉ dành cho danh mục chuyến bay), hoặc Thẻ điểm đến (Destination Card - chỉ dành cho danh mục điểm đến)"),
     
    (r"Specify one of the RTA IDs associated with your ad account\. To obtain the list of RTA IDs associated with your ad account, use \[/rta/get/\]\(\.\./12-api-reference/53-rta\.md#doc-1740860431448065\)\.",
     "Chỉ định một trong các ID RTA được liên kết với tài khoản quảng cáo của bạn. Để lấy danh sách các ID RTA được liên kết với tài khoản quảng cáo của bạn, sử dụng [/rta/get/](../12-api-reference/53-rta.md#doc-1740860431448065)."),
     
    (r"• When RTA is disabled, this setting is not supported\. • When RTA is enabled, you can either enable or disable RTA bid\. If you choose to enable RTA bid, your bid will be calculated by TikTok based on RTA response\.",
     "• Khi RTA bị tắt, cài đặt này không được hỗ trợ. • Khi RTA được bật, bạn có thể bật hoặc tắt giá thầu RTA. Nếu bạn chọn bật giá thầu RTA, giá thầu của bạn sẽ do TikTok tính toán dựa trên phản hồi RTA."),
     
    (r"• When the promoted App is an Android App: Google Play or TikTok Instant Page • When the promoted App is an iOS App: App Store or TikTok Instant Page",
     "• Khi ứng dụng được quảng bá là Ứng dụng Android: Google Play hoặc Trang tức thì TikTok • Khi ứng dụng được quảng bá là Ứng dụng iOS: App Store hoặc Trang tức thì TikTok"),
     
    (r"• When promotion_type at the ad group level is APP_ANDROID, you can set the Destination to Google Play or TikTok Instant Page • When promotion_type at the ad group level is APP_IOS, you can set the Destination to App Store or TikTok Instant Page",
     "• Khi promotion_type ở cấp nhóm quảng cáo là APP_ANDROID, bạn có thể đặt Đích đến là Google Play hoặc Trang tức thì TikTok • Khi promotion_type ở cấp nhóm quảng cáo là APP_IOS, bạn có thể đặt Đích đến là App Store hoặc Trang tức thì TikTok"),
     
    (r"When the promoted App is an iOS App: • Disabled or enabled with a valid custom product page\.",
     "Khi ứng dụng được quảng bá là Ứng dụng iOS: • Đã tắt hoặc đã bật với một trang sản phẩm tùy chỉnh hợp lệ."),
     
    (r"When promotion_type at the ad group level is APP_IOS: Not specified or specify a custom product page ID\. To obtain the custom product page IDs configured for your app, use \[/app/custom_product_page/get/\]\(\.\./12-api-reference/43-events-1-0-p1\.md#doc-1785536417646593\)\.",
     "Khi promotion_type ở cấp nhóm quảng cáo là APP_IOS: Không chỉ định hoặc chỉ định ID trang sản phẩm tùy chỉnh. Để lấy các ID trang sản phẩm tùy chỉnh đã định cấu hình cho ứng dụng của bạn, sử dụng [/app/custom_product_page/get/](../12-api-reference/43-events-1-0-p1.md#doc-1785536417646593)."),
     
    (r"Disabled or enabled with a valid deeplink\. A deeplink is a URL that takes people to a specific location within your app\.",
     "Đã tắt hoặc đã bật với một deeplink hợp lệ. Deeplink là một URL đưa mọi người đến một vị trí cụ thể bên trong ứng dụng của bạn."),
     
    (r"Fallback destination", "Đích đến dự phòng (Fallback destination)"),
    (r"If audiences don't have your app installed, you can choose to send them to another destination as fallback\.",
     "Nếu đối tượng mục tiêu chưa cài đặt ứng dụng của bạn, bạn có thể chọn chuyển hướng họ đến một đích đến khác làm phương án dự phòng."),
     
    # Growth Max Overview & Subtypes
    (r"Upgraded Smart\+ TikTok Growth Max is an AI-driven campaign solution that helps mini games, mini dramas, and drama series advertisers acquire new users and boost revenue on TikTok with optimal performance and seamless integration\.",
     "Upgraded Smart+ TikTok Growth Max là giải pháp chiến dịch do AI điều khiển, giúp các nhà quảng cáo trò chơi nhỏ (mini games), kịch ngắn (mini dramas) và phim bộ (drama series) thu hút người dùng mới và tăng doanh thu trên TikTok với hiệu suất tối ưu và tích hợp liền mạch."),
     
    (r"Depending on the type of product you promote, you can create Upgraded Smart\+ TikTok Growth Max campaigns as needed:",
     "Tùy theo loại sản phẩm bạn quảng bá, bạn có thể tạo các chiến dịch Upgraded Smart+ TikTok Growth Max theo nhu cầu:"),
     
    (r"- To learn how to create an Upgraded Smart\+ Growth Max campaign for Mini Games, see \[Create Upgraded Smart\+ Growth Max campaigns: Mini Games\]\(use-case-tao-chien-dich-p1\.md#doc-1868121865281538\)\.",
     "- Để tìm hiểu cách tạo chiến dịch Upgraded Smart+ Growth Max cho Mini Game, xem [Tạo chiến dịch Upgraded Smart+ Growth Max: Mini Game](use-case-tao-chien-dich-p1.md#doc-1868121865281538)."),
     
    (r"- To learn how to create an Upgraded Smart\+ Growth Max campaign for Mini Dramas, see \[Create Upgraded Smart\+ Growth Max campaigns: Mini Dramas\]\(use-case-tao-chien-dich-p1\.md#doc-1853377811982657\)\.",
     "- Để tìm hiểu cách tạo chiến dịch Upgraded Smart+ Growth Max cho Kịch ngắn, xem [Tạo chiến dịch Upgraded Smart+ Growth Max: Kịch ngắn](use-case-tao-chien-dich-p1.md#doc-1853377811982657)."),
     
    (r"- To learn how to create an Upgraded Smart\+ Growth Max campaign for Drama Series, see \[Create Upgraded Smart\+ Growth Max campaigns: Drama Series\]\(use-case-tao-chien-dich-p1\.md#doc-1863331595515009\)\.",
     "- Để tìm hiểu cách tạo chiến dịch Upgraded Smart+ Growth Max cho Phim bộ, xem [Tạo chiến dịch Upgraded Smart+ Growth Max: Phim bộ](use-case-tao-chien-dich-p1.md#doc-1863331595515009)."),
     
    (r"Upgraded Smart\+ TikTok Growth Max for Mini Games is a campaign type that drives in-app purchases, ad views, and user engagement for mini games within the TikTok ecosystem\.",
     "Upgraded Smart+ TikTok Growth Max cho Mini Game là loại chiến dịch thúc đẩy giao dịch mua trong ứng dụng (IAP), lượt xem quảng cáo (IAA) và mức độ tương tác của người dùng cho các mini game trong hệ sinh thái TikTok."),
     
    (r"Upgraded Smart\+ TikTok Growth Max for Mini Dramas is a campaign type that drives engagement and revenue for mini drama content on TikTok\.",
     "Upgraded Smart+ TikTok Growth Max cho Kịch ngắn là loại chiến dịch thúc đẩy mức độ tương tác và doanh thu cho nội dung kịch ngắn trên TikTok."),
     
    (r"Upgraded Smart\+ TikTok Growth Max for Drama Series is a campaign type that drives engagement and revenue for drama series content on TikTok\.",
     "Upgraded Smart+ TikTok Growth Max cho Phim bộ là loại chiến dịch thúc đẩy mức độ tương tác và doanh thu cho nội dung phim bộ trên TikTok."),
]
