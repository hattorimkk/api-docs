#!/usr/bin/env python3
"""
Cluster 4 translations: Reach & Frequency, GMV Max, Product/LIVE GMV Max, Legacy Smart+ (Lead Gen, Web, App)
- 1758528372513794: Reach & Frequency campaigns
- 1822009058467842: GMV Max Campaigns
- 1822009220448257: Product GMV Max Campaigns
- 1822009242546258: LIVE GMV Max Campaigns
- 1768006268820546: Legacy Smart+ Campaign overview
- 1827645480080385: Legacy Smart+ Lead Generation
- 1814122471133186: Legacy Smart+ Web
- 1814122492598274: Legacy Smart+ App
"""

CLUSTER4_RULES = [
    # R&F
    (r"R&F is a campaign buying type that enables predictable reach, controlled frequency and guaranteed delivery with a more flexible and transparent ad experience\. If you want to control the audiences you reach and the number of times they are exposed to your ad messaging before delivery, you can create a R&F campaign\.",
     "R&F là loại hình mua chiến dịch cho phép đạt được phạm vi tiếp cận có thể dự đoán trước, tần suất được kiểm soát và lượt phân phối đảm bảo với trải nghiệm quảng cáo minh bạch, linh hoạt hơn. Nếu bạn muốn kiểm soát đối tượng tiếp cận và số lần họ nhìn thấy thông điệp quảng cáo của bạn trước khi phân phối, bạn có thể tạo chiến dịch R&F."),
    
    (r"\*\*You can use Campaign Management API to create R&F ads, and this helps streamline your ad creation experience, and elevate operational efficiency and scalability\.\*\*",
     "**Bạn có thể sử dụng Campaign Management API để tạo quảng cáo R&F, giúp tối ưu hóa quy trình tạo quảng cáo cũng như nâng cao hiệu quả hoạt động và khả năng mở rộng.**"),
    
    (r"- To use R&F endpoints, you need relevant permissions\. See \*\*API Reference\*\* to find out permissions required for endpoints \(including the endpoints listed in the \"Steps\" section\) and see \[Update app permissions\]\(\.\./04-get-started/bat-dau\.md#doc-1738855280338946\) to find out how to configure permissions\.",
     "- Để sử dụng các endpoint R&F, bạn cần các quyền liên quan. Xem **Tham khảo API (API Reference)** để biết các quyền cần thiết cho endpoint (bao gồm các endpoint được liệt kê trong phần \"Các bước thực hiện\") và xem [Cập nhật quyền ứng dụng](../04-get-started/bat-dau.md#doc-1738855280338946) để biết cách cấu hình quyền."),
    
    (r"- The Reach and Frequency feature is in GA\. Developers can build integrations with this feature\. However, the integations would only work if the ad accounts are allowlisted for this feature\. To have your ad accounts allowlisted, please reach out to your TikTok representative, and sign a Commercial Contract for Branding\.",
     "- Tính năng Tiếp cận và Tần suất (Reach and Frequency) hiện đã phát hành rộng rãi (GA). Các nhà phát triển có thể xây dựng tích hợp với tính năng này. Tuy nhiên, việc tích hợp chỉ hoạt động nếu tài khoản quảng cáo được đưa vào danh sách cho phép (allowlist) của tính năng này. Để đưa tài khoản quảng cáo vào danh sách cho phép, vui lòng liên hệ với đại diện TikTok của bạn và ký Hợp đồng thương mại cho Xây dựng thương hiệu (Branding)."),
    
    (r"- Currently, only `RF_REACH` advertising objective is available for R&F type ads\.",
     "- Hiện tại, chỉ có mục tiêu quảng cáo `RF_REACH` khả dụng cho quảng cáo loại R&F."),
    
    (r"1\. Create a R&F campaign\.", "1. Tạo chiến dịch R&F."),
    (r"2\. Obtain estimated available ad inventory\.", "2. Lấy thông tin kho khoảng không quảng cáo ước tính khả dụng."),
    (r"3\. \[Optional\] Create a budget & impression or budget & reach chart\.", "3. [Không bắt buộc] Tạo biểu đồ ngân sách & lượt hiển thị hoặc ngân sách & phạm vi tiếp cận."),
    (r"4\. Create an ad group\.", "4. Tạo nhóm quảng cáo."),
    (r"5\. Create ads\.", "5. Tạo quảng cáo."),
    
    # GMV Max Overview
    (r"GMV Max is an automated ad campaign type that optimizes total channel ROI for your TikTok Shop\.",
     "GMV Max là loại chiến dịch quảng cáo tự động giúp tối ưu hóa tổng ROI của kênh cho TikTok Shop của bạn."),
    
    (r"- \*\*Product GMV Max Campaign\*\*: Automatically chooses the products, creative assets and placement options that are most likely to encourage people to buy your products\.",
     "- **Chiến dịch Product GMV Max**: Tự động chọn các sản phẩm, tài sản mẫu quảng cáo và tùy chọn vị trí có khả năng khuyến khích mọi người mua sản phẩm của bạn nhất."),
    
    (r"- \*\*LIVE GMV Max Campaign\*\*: Optimizes liveroom traffic to get the highest gross revenue for your LIVE event\.",
     "- **Chiến dịch LIVE GMV Max**: Tối ưu hóa lưu lượng truy cập phòng live để mang lại tổng doanh thu cao nhất cho sự kiện LIVE của bạn."),
    
    (r"\*\*You can use GMV Max API to create Chiến dịch GMV Max \(GMV Max Campaigns\), and this helps streamline your ad creation experience, and elevate operational efficiency and scalability\.\*\*",
     "**Bạn có thể sử dụng GMV Max API để tạo Chiến dịch GMV Max (GMV Max Campaigns), giúp tối ưu hóa quy trình tạo quảng cáo cũng như nâng cao hiệu quả hoạt động và khả năng mở rộng.**"),
    
    (r"For a comprehensive introduction to and unique values for GMV Max API, consult \[API for Business Playbook - GMV Max\]\(https://bytedance\.sg\.larkoffice\.com/file/WxJ5bQMnhoz6l3xEbdVl8TyPgwg\)\.",
     "Để biết phần giới thiệu toàn diện và các giá trị độc đáo của GMV Max API, hãy tham khảo [API for Business Playbook - GMV Max](https://bytedance.sg.larkoffice.com/file/WxJ5bQMnhoz6l3xEbdVl8TyPgwg)."),
    
    (r"# Mutual exclusion rules for Chiến dịch GMV Max \(GMV Max Campaigns\)",
     "# Các quy tắc loại trừ lẫn nhau cho Chiến dịch GMV Max (GMV Max Campaigns)"),
     
    (r"Chiến dịch GMV Max \(GMV Max Campaigns\) operate under specific exclusion rules to ensure optimal performance and accurate delivery\. These rules include:",
     "Chiến dịch GMV Max (GMV Max Campaigns) hoạt động theo các quy tắc loại trừ cụ thể để đảm bảo hiệu suất tối ưu và phân phối chính xác. Các quy tắc này bao gồm:"),
     
    (r"## Ad account exclusive authorization",
     "## Ủy quyền độc quyền tài khoản quảng cáo (Ad account exclusive authorization)"),
     
    (r"TikTok Shop implements a single ad account authorization model for Chiến dịch GMV Max \(GMV Max Campaigns\):",
     "TikTok Shop áp dụng mô hình ủy quyền tài khoản quảng cáo đơn lẻ cho Chiến dịch GMV Max (GMV Max Campaigns):"),
     
    (r"- Each TikTok Shop can authorize only one ad account for GMV Max Campaign creation\.",
     "- Mỗi TikTok Shop chỉ có thể ủy quyền cho một tài khoản quảng cáo để tạo Chiến dịch GMV Max."),
     
    (r"- When you grant GMV Max exclusive authorization to a new ad account:",
     "- Khi bạn cấp ủy quyền độc quyền GMV Max cho một tài khoản quảng cáo mới:"),
     
    (r"- The previous ad account loses access to Chiến dịch GMV Max \(GMV Max Campaigns\) that use the same TikTok Shop\.",
     "- Tài khoản quảng cáo trước đó sẽ mất quyền truy cập vào các Chiến dịch GMV Max sử dụng cùng TikTok Shop."),
     
    (r"- All existing Chiến dịch GMV Max \(GMV Max Campaigns\) that use the same TikTok Shop in the previous ad account are automatically paused\.",
     "- Tất cả các Chiến dịch GMV Max hiện có sử dụng cùng TikTok Shop trong tài khoản quảng cáo trước đó sẽ tự động bị tạm dừng."),
     
    (r"## Product usage in Chiến dịch GMV Max \(GMV Max Campaigns\)",
     "## Sử dụng sản phẩm trong Chiến dịch GMV Max (Product usage in GMV Max Campaigns)"),
     
    (r"Products must adhere to single-campaign usage rules:",
     "Sản phẩm phải tuân thủ các quy tắc sử dụng trong một chiến dịch duy nhất:"),
     
    (r"- Each product within a TikTok Shop can only be used in one enabled Product GMV Max Campaign at a time\.",
     "- Mỗi sản phẩm trong một TikTok Shop chỉ có thể được sử dụng trong một Chiến dịch Product GMV Max đang bật tại một thời điểm."),
     
    (r"- To use a product in a new Product GMV Max Campaign, first disable or delete its existing Product GMV Max Campaign\.",
     "- Để sử dụng một sản phẩm trong Chiến dịch Product GMV Max mới, trước tiên hãy tắt hoặc xóa Chiến dịch Product GMV Max hiện có của sản phẩm đó."),
     
    (r"- For Product Chiến dịch GMV Max \(GMV Max Campaigns\) that promote all products within a TikTok Shop, ensure that the TikTok Shop doesn't have other enabled Product GMV Max Campaigns that use the same shop, as this will lead to conflict\.",
     "- Đối với các Chiến dịch Product GMV Max quảng bá tất cả sản phẩm trong một TikTok Shop, hãy đảm bảo rằng TikTok Shop không có các Chiến dịch Product GMV Max đang bật khác sử dụng cùng shop, vì điều này sẽ dẫn đến xung đột."),
     
    (r"Campaign configuration guidelines:", "Hướng dẫn cấu hình chiến dịch:"),
    
    (r"- If you want to promote specific products or product sets, choose to promote specific products and add the products you want to promote to the campaign\.",
     "- Nếu bạn muốn quảng bá các sản phẩm hoặc bộ sản phẩm cụ thể, hãy chọn quảng bá các sản phẩm cụ thể và thêm các sản phẩm bạn muốn quảng bá vào chiến dịch."),
     
    (r"- If you want to promote all products within a TikTok Shop, ensure that the TikTok Shop doesn't have other enabled Product GMV Max Campaigns that use the same shop\.",
     "- Nếu bạn muốn quảng bá tất cả sản phẩm trong TikTok Shop, hãy đảm bảo rằng TikTok Shop không có Chiến dịch Product GMV Max đang bật nào khác sử dụng cùng shop."),
     
    (r"## Campaign type compatibility",
     "## Tính tương thích giữa các loại chiến dịch (Campaign type compatibility)"),
     
    (r"The following exclusion rules apply across campaign types:",
     "Các quy tắc loại trừ sau đây áp dụng giữa các loại chiến dịch:"),
     
    (r"### Shop level", "### Cấp Shop (Shop level)"),
    (r"### Identity level", "### Cấp danh tính (Identity level)"),
    
    (r"- If you create an enabled Live GMV Max Campaign by using an identity associated with the official TikTok account of a TikTok Shop, any existing enabled Live Shopping Ad Groups using the same identity will be paused or impacted, regardless of which ad account the Live Shopping Ad Groups were created in\.",
     "- Nếu bạn tạo một Chiến dịch Live GMV Max đang bật bằng cách sử dụng danh tính liên kết với tài khoản TikTok chính thức của TikTok Shop, bất kỳ Nhóm quảng cáo Live Shopping đang bật hiện có nào sử dụng cùng danh tính sẽ bị tạm dừng hoặc bị ảnh hưởng, bất kể Nhóm quảng cáo Live Shopping đó được tạo trong tài khoản quảng cáo nào."),
     
    (r"- If an enabled Live Shopping Ad Group has occupied an identity associated with a TikTok account that is not an official TikTok account of a TikTok Shop, you cannot use the identity in an enabled LIVE GMV Max Campaign\. You will need to manually pause the existing enabled Live Shopping Ad Group using the same identity first\.",
     "- Nếu một Nhóm quảng cáo Live Shopping đang bật đã chiếm danh tính liên kết với tài khoản TikTok không phải là tài khoản chính thức của TikTok Shop, bạn không thể sử dụng danh tính đó trong Chiến dịch LIVE GMV Max đang bật. Bạn sẽ cần phải tạm dừng thủ công Nhóm quảng cáo Live Shopping đang bật hiện có dùng cùng danh tính trước."),
     
    (r"- If an identity has been occupied by an enabled Live GMV Max Campaign, you can no longer create new enabled Live Shopping Ad Groups that use the same identity\.",
     "- Nếu một danh tính đã bị chiếm bởi một Chiến dịch Live GMV Max đang bật, bạn không thể tạo thêm Nhóm quảng cáo Live Shopping đang bật mới sử dụng cùng danh tính đó nữa."),
     
    (r"- Promoting all products from a TikTok Shop in a Product GMV Max Campaign will automatically pause or impact any existing enabled Video Shopping Ad Groups or Product Shopping Ad Groups using the same shop, regardless of which ad account the Video Shopping Ad Groups or Product Shopping Ad Groups were created in\.",
     "- Việc quảng bá tất cả sản phẩm từ một TikTok Shop trong Chiến dịch Product GMV Max sẽ tự động tạm dừng hoặc ảnh hưởng đến bất kỳ Nhóm quảng cáo Video Shopping hoặc Nhóm quảng cáo Product Shopping đang bật hiện có nào dùng cùng shop, bất kể các nhóm quảng cáo đó được tạo trong tài khoản quảng cáo nào."),
     
    (r"\*\*ii\. Confirm that the products are not occupied by an enabled Product GMV Max Campaign\.\*\*",
     "**ii. Xác nhận rằng các sản phẩm không bị chiếm bởi một Chiến dịch Product GMV Max đang bật.**"),
     
    # Product GMV Max
    (r"\*\*You can use GMV Max API to create Product Chiến dịch GMV Max \(GMV Max Campaigns\), and this helps streamline your campaign creation experience, and elevate operational efficiency and scalability\.\*\*",
     "**Bạn có thể sử dụng GMV Max API để tạo Chiến dịch Product GMV Max (GMV Max Campaigns), giúp tối ưu hóa quy trình tạo chiến dịch cũng như nâng cao hiệu quả hoạt động và khả năng mở rộng.**"),
     
    (r"The following table lists the countries or regions where Product Chiến dịch GMV Max \(GMV Max Campaigns\) are available\.",
     "Bảng sau đây liệt kê các quốc gia hoặc khu vực nơi Chiến dịch Product GMV Max (GMV Max Campaigns) khả dụng."),
     
    (r"- Creating a GMV Max Campaign requires setting up a TikTok Shop in Business Center first\.",
     "- Việc tạo Chiến dịch GMV Max yêu cầu thiết lập TikTok Shop trong Business Center trước."),
     
    (r"## 2\. Create a Product GMV Max Campaign",
     "## 2. Tạo Chiến dịch Product GMV Max"),
     
    (r"Create a Product GMV Max Campaign by using \[/campaign/gmv_max/create/\]\(\.\./12-api-reference/45-gmv-max-p1\.md#doc-1822000988713089\)\. Note that the following requirements must be met\.",
     "Tạo Chiến dịch Product GMV Max bằng cách sử dụng [/campaign/gmv_max/create/](../12-api-reference/45-gmv-max-p1.md#doc-1822000988713089). Lưu ý rằng phải đáp ứng các yêu cầu sau."),
     
    (r"#### Promote all products in TikTok Shop & autoselect videos from authorized posts, affiliate posts and creative assets",
     "#### Quảng bá tất cả sản phẩm trong TikTok Shop & tự động chọn video từ các bài đăng được ủy quyền, bài đăng tiếp thị liên kết (affiliate) và tài sản mẫu quảng cáo"),
     
    (r"#### Promote specific products in TikTok Shop & manually select videos",
     "#### Quảng bá các sản phẩm cụ thể trong TikTok Shop & chọn video thủ công"),
     
    (r"- \[GMV Max API\]\(\.\./12-api-reference/45-gmv-max-p1\.md#doc-1822000911166465\)",
     "- [API GMV Max](../12-api-reference/45-gmv-max-p1.md#doc-1822000911166465)"),
     
    # Live GMV Max
    (r"LIVE Chiến dịch GMV Max \(GMV Max Campaigns\) optimize liveroom traffic to get the highest gross revenue for your LIVE event\.",
     "Chiến dịch LIVE GMV Max (GMV Max Campaigns) tối ưu hóa lưu lượng truy cập phòng live để mang lại tổng doanh thu cao nhất cho sự kiện LIVE của bạn."),
     
    (r"\*\*You can use GMV Max API to create LIVE Chiến dịch GMV Max \(GMV Max Campaigns\), and this helps streamline your campaign creation experience, and elevate operational efficiency and scalability\.\*\*",
     "**Bạn có thể sử dụng GMV Max API để tạo Chiến dịch LIVE GMV Max (GMV Max Campaigns), giúp tối ưu hóa quy trình tạo chiến dịch cũng như nâng cao hiệu quả hoạt động và khả năng mở rộng.**"),
     
    (r"The following table lists the countries or regions where LIVE Chiến dịch GMV Max \(GMV Max Campaigns\) are available\.",
     "Bảng sau đây liệt kê các quốc gia hoặc khu vực nơi Chiến dịch LIVE GMV Max (GMV Max Campaigns) khả dụng."),
     
    (r"## 2\. Create a LIVE GMV Max Campaign",
     "## 2. Tạo Chiến dịch LIVE GMV Max"),
     
    (r"Create a LIVE GMV Max Campaign by using \[/campaign/gmv_max/create/\]\(\.\./12-api-reference/45-gmv-max-p1\.md#doc-1822000988713089\)\. Note that the following requirements must be met\.",
     "Tạo Chiến dịch LIVE GMV Max bằng cách sử dụng [/campaign/gmv_max/create/](../12-api-reference/45-gmv-max-p1.md#doc-1822000988713089). Lưu ý rằng phải đáp ứng các yêu cầu sau."),
     
    (r"#### Maximize gross revenue & Set start time and end time",
     "#### Tối đa hóa tổng doanh thu (Maximize gross revenue) & Đặt thời gian bắt đầu và kết thúc"),
     
    (r"#### Target minimum ROAS & Run continuously after start time",
     "#### Nhắm mục tiêu ROAS tối thiểu & Chạy liên tục sau thời gian bắt đầu"),
     
    # Legacy Smart+ Overview & Lead Gen
    (r"# \(To be deprecated\) Create a Chiến dịch Legacy Smart\+",
     "# (Sắp ngừng hỗ trợ) Tạo Chiến dịch Legacy Smart+"),
     
    (r"> Đường dẫn: Use Cases > Campaign creation > \(To be deprecated\) Create a Chiến dịch Legacy Smart\+",
     "> Đường dẫn: Tình huống sử dụng > Tạo chiến dịch > (Sắp ngừng hỗ trợ) Tạo Chiến dịch Legacy Smart+"),
     
    (r"Smart\+ Campaigns leverage machine learning to optimize the entire campaign creation and delivery process, helping advertisers maximize results with minimal manual effort\.",
     "Chiến dịch Smart+ tận dụng máy học để tối ưu hóa toàn bộ quy trình tạo và phân phối chiến dịch, giúp nhà quảng cáo tối đa hóa kết quả với nỗ lực thủ công tối thiểu."),
     
    (r"- To learn how to create a Smart\+ Web Campaign, see \[Create Legacy Smart\+ Web Campaigns\]\(use-case-tao-chien-dich-p1\.md#doc-1814122471133186\)\.",
     "- Để tìm hiểu cách tạo Chiến dịch Smart+ Web, xem [Tạo chiến dịch Legacy Smart+ Web](use-case-tao-chien-dich-p1.md#doc-1814122471133186)."),
     
    (r"- To learn how to create a Smart\+ App Campaign, see \[Create Legacy Smart\+ App Campaigns\]\(use-case-tao-chien-dich-p1\.md#doc-1814122492598274\)\.",
     "- Để tìm hiểu cách tạo Chiến dịch Smart+ App, xem [Tạo chiến dịch Legacy Smart+ App](use-case-tao-chien-dich-p1.md#doc-1814122492598274)."),
     
    (r"- To learn how to create a Smart\+ Lead Generation Campaign, see \[Create a Legacy Smart\+ Lead Generation Campaign\]\(use-case-tao-chien-dich-p1\.md#doc-1827645480080385\)\.",
     "- Để tìm hiểu cách tạo Chiến dịch Smart+ Tìm kiếm khách hàng tiềm năng, xem [Tạo chiến dịch Legacy Smart+ Tìm kiếm khách hàng tiềm năng](use-case-tao-chien-dich-p1.md#doc-1827645480080385)."),
     
    (r"# Create a Smart\+ Tìm kiếm khách hàng tiềm năng \(Lead Generation\) Campaign with optimization location as Biểu mẫu tức thì \(Instant Form\)",
     "# Tạo chiến dịch Smart+ Tìm kiếm khách hàng tiềm năng (Lead Generation) với vị trí tối ưu hóa là Biểu mẫu tức thì (Instant Form)"),
     
    (r"Ensure that you have an existing Biểu mẫu tức thì \(Instant Form\) within your ad account\.",
     "Đảm bảo rằng bạn đã có sẵn một Biểu mẫu tức thì (Instant Form) trong tài khoản quảng cáo của mình."),
     
    (r"- To create an Biểu mẫu tức thì \(Instant Form\), use \[Instant Page Editor SDK\]\(\.\./09-marketing-api/creatives\.md#doc-1740306122606626\)\.",
     "- Để tạo Biểu mẫu tức thì (Instant Form), hãy sử dụng [SDK Trình chỉnh sửa trang tức thì](../09-marketing-api/creatives.md#doc-1740306122606626)."),
     
    (r"N/A Campaigns created through \[/campaign/spc/create/\]\(\.\./12-api-reference/61-to-be-deprecated-legacy-smartplus\.md#doc-1767334204047362\) are Smart\+ Campaigns\.",
     "N/A Các chiến dịch được tạo qua [/campaign/spc/create/](../12-api-reference/61-to-be-deprecated-legacy-smartplus.md#doc-1767334204047362) là các Chiến dịch Smart+."),
     
    (r"N/A \*\*Note\*\*: CBO is enabled by default for Smart\+ Campaigns\.",
     "N/A **Lưu ý**: CBO được bật theo mặc định cho các Chiến dịch Smart+."),
     
    (r"N/A \*\*Note\*\*: If you retrieve Smart\+ Campaigns via \[/campaign/get/\]\(\.\./12-api-reference/24-campaign\.md#doc-1739315828649986\), the returned budget_optimize_on will be true\.",
     "N/A **Lưu ý**: Nếu bạn truy xuất các Chiến dịch Smart+ qua [/campaign/get/](../12-api-reference/24-campaign.md#doc-1739315828649986), trường budget_optimize_on trả về sẽ là true."),
     
    (r"Bật hoặc tắt \(Enabled hoặc Disabled\) With deep funnel optimization, you can select a secondary event alongside the primary event to optimize for high-quality leads\.",
     "Bật hoặc tắt (Enabled hoặc Disabled) Với tính năng tối ưu hóa phễu sâu (deep funnel optimization), bạn có thể chọn một sự kiện thứ cấp cùng với sự kiện chính để tối ưu hóa cho khách hàng tiềm năng chất lượng cao."),
     
    (r"• To enable deep funnel optimization, set deep_funnel_optimization_status to ON and pass deep_funnel_event_source, deep_funnel_optimization_event, and deep_funnel_bid\.",
     "• Để bật tối ưu hóa phễu sâu, đặt deep_funnel_optimization_status thành ON và truyền deep_funnel_event_source, deep_funnel_optimization_event, và deep_funnel_bid."),
     
    (r"• To disable deep funnel optimization, set deep_funnel_optimization_status to OFF or do not pass deep_funnel_optimization_status\.",
     "• Để tắt tối ưu hóa phễu sâu, đặt deep_funnel_optimization_status thành OFF hoặc không truyền deep_funnel_optimization_status."),
     
    (r'\["PLACEMENT_TIKTOK"\] \*\*Note\*\*: The \[Automatic Search Placement\]\(\.\./09-marketing-api/quan-ly-chien-dich-p2\.md#doc-1771747806140417\) feature is enabled by default for Smart\+ Campaigns\. Therefore, ads created in a Smart\+ Campaign can be displayed both in TikTok feeds and TikTok search results\.',
     '["PLACEMENT_TIKTOK"] **Lưu ý**: Tính năng [Vị trí tìm kiếm tự động](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1771747806140417) được bật theo mặc định cho các Chiến dịch Smart+. Do đó, các quảng cáo được tạo trong Chiến dịch Smart+ có thể hiển thị cả trong bảng tin TikTok và kết quả tìm kiếm TikTok.'),
     
    (r"Supported with allowlist \*\*Note\*\*: Gender targeting in Smart\+ Campaigns is currently an allowlist-only feature\. If you want to use this feature, contact your TikTok representative\.",
     "Được hỗ trợ theo danh sách cho phép **Lưu ý**: Nhắm mục tiêu theo giới tính trong Chiến dịch Smart+ hiện là tính năng chỉ dành cho danh sách cho phép (allowlist). Nếu bạn muốn sử dụng tính năng này, hãy liên hệ với đại diện TikTok của bạn."),
     
    (r"Any of the following options: • 18\+ • 25\+",
     "Bất kỳ tùy chọn nào sau đây: • 18+ • 25+"),
     
    (r"Any of the following values: • 18\+ • 25\+",
     "Bất kỳ giá trị nào sau đây: • 18+ • 25+"),
     
    (r"Any of the following types: • Run campaign continuously after the scheduled start time • Run campaign between the scheduled start time and scheduled end time",
     "Bất kỳ loại nào sau đây: • Chạy chiến dịch liên tục sau thời gian bắt đầu đã lên lịch • Chạy chiến dịch giữa thời gian bắt đầu và thời gian kết thúc đã lên lịch"),
     
    # Legacy Smart+ Web
    (r"Based on your preference for the specific type of web campaign, you can create regular Smart\+ Web Campaigns, Smart\+ Quản cáo danh mục \(Catalog Ads\), and Smart\+ Web Campaigns with Website and App Optimization\.",
     "Tùy theo sở thích của bạn đối với loại chiến dịch web cụ thể, bạn có thể tạo Chiến dịch Smart+ Web thông thường, Smart+ Quảng cáo danh mục (Catalog Ads), và Chiến dịch Smart+ Web có Tối ưu hóa trang web và ứng dụng."),
     
    (r"Smart Performance Web Campaigns will be deprecated in the next API version\. To ensure a smooth API integration, we recommend that you upgrade to Smart\+ Web Campaigns as soon as possible\. Smart\+ Web Campaigns are a new AI-powered automation solution that leverages machine learning to drive business outcomes for advertisers\.",
     "Chiến dịch Smart Performance Web sẽ ngừng hỗ trợ trong phiên bản API tiếp theo. Để đảm bảo tích hợp API suôn sẻ, chúng tôi khuyên bạn nên nâng cấp lên Chiến dịch Smart+ Web càng sớm càng tốt. Chiến dịch Smart+ Web là giải pháp tự động hóa mới được hỗ trợ bởi AI, tận dụng máy học để thúc đẩy kết quả kinh doanh cho nhà quảng cáo."),
     
    (r"A regular Smart\+ Web Campaign is a Smart\+ Web Campaign that doesn't use catalog products to deliver ads\. For such campaigns, you need to set `catalog_enabled` to `false` \(or do not pass `catalog_enabled`\) at the campaign level\.",
     "Chiến dịch Smart+ Web thông thường là Chiến dịch Smart+ Web không sử dụng sản phẩm trong danh mục để phân phối quảng cáo. Đối với các chiến dịch như vậy, bạn cần đặt `catalog_enabled` thành `false` (hoặc không truyền `catalog_enabled`) ở cấp chiến dịch."),
     
    (r"Regular Smart\+ Web ad groups cannot be used in \[/split_test/create/\]\(\.\./12-api-reference/65-super-split-test\.md#doc-1742666471475201\) to create split test groups\.",
     "Các nhóm quảng cáo Smart+ Web thông thường không thể sử dụng trong [/split_test/create/](../12-api-reference/65-super-split-test.md#doc-1742666471475201) để tạo nhóm thử nghiệm phân tách."),
     
    (r"N/A CBO is enabled by default for Smart\+ Web Campaigns\.",
     "N/A CBO được bật theo mặc định cho các Chiến dịch Smart+ Web."),
     
    (r"N/A \*\*Note\*\*: If you retrieve Smart\+ Web Campaigns via \[/campaign/get/\]\(\.\./12-api-reference/24-campaign\.md#doc-1739315828649986\), the returned budget_optimize_on will be true\.",
     "N/A **Lưu ý**: Nếu bạn truy xuất các Chiến dịch Smart+ Web qua [/campaign/get/](../12-api-reference/24-campaign.md#doc-1739315828649986), trường budget_optimize_on trả về sẽ là true."),
     
    (r"Product source details · Use Catalog", "Chi tiết nguồn sản phẩm · Sử dụng danh mục (Use Catalog)"),
    (r"UNSET or not passed", "UNSET hoặc không truyền"),
    
    (r"• Bắt buộc khi optimization goal is Conversion or Value\. • Not supported when optimization goal is Click or Lượt xem trang đích \(Landing page view\)\.",
     "• Bắt buộc khi mục tiêu tối ưu hóa là Conversion hoặc Value. • Không hỗ trợ khi mục tiêu tối ưu hóa là Click hoặc Lượt xem trang đích (Landing page view)."),
     
    (r"• Bắt buộc khi optimization_goal is set to CONVERT or VALUE\. • Not supported when optimization_goal is set to CLICK or TRAFFIC_LANDING_PAGE_VIEW\.",
     "• Bắt buộc khi optimization_goal được đặt thành CONVERT hoặc VALUE. • Không hỗ trợ khi optimization_goal được đặt thành CLICK hoặc TRAFFIC_LANDING_PAGE_VIEW."),
     
    (r"• Bắt buộc khi optimization goal is Conversion or Value\. • When optimization goal is Value, specify the optimization event as Purchase \(COMPLETE_PAYMENT\)\.",
     "• Bắt buộc khi mục tiêu tối ưu hóa là Conversion hoặc Value. • Khi mục tiêu tối ưu hóa là Value, chỉ định sự kiện tối ưu hóa là Mua hàng (Purchase - COMPLETE_PAYMENT)."),
     
    (r"• Bắt buộc khi optimization_goal is set to CONVERT or VALUE\. • To obtain the optimization events that have been configured for the Pixel, use \[/pixel/get/\]\(\.\./12-api-reference/42-events-2-0\.md#doc-1771100910008322\)\. • When optimization_goal is VALUE, set optimization_event to COMPLETE_PAYMENT\.",
     "• Bắt buộc khi optimization_goal được đặt thành CONVERT hoặc VALUE. • Để lấy các sự kiện tối ưu hóa đã được cấu hình cho Pixel, sử dụng [/pixel/get/](../12-api-reference/42-events-2-0.md#doc-1771100910008322). • Khi optimization_goal là VALUE, đặt optimization_event thành COMPLETE_PAYMENT."),
     
    # Legacy Smart+ App
    (r"Call \[/campaign/spc/create/\]\(\.\./12-api-reference/61-to-be-deprecated-legacy-smartplus\.md#doc-1767334204047362\) to create Smart\+ App Campaigns \(`objective_type` = `APP_PROMOTION`\)\.",
     "Gọi [/campaign/spc/create/](../12-api-reference/61-to-be-deprecated-legacy-smartplus.md#doc-1767334204047362) để tạo Chiến dịch Smart+ App (`objective_type` = `APP_PROMOTION`)."),
     
    (r"> Smart Performance App Campaigns have been automatically upgraded to Smart\+ App Campaigns\.",
     "> Các Chiến dịch Smart Performance App đã được tự động nâng cấp lên Chiến dịch Smart+ App."),
     
    (r"The following table lists only some related parameters\. To find a complete list of parameters, refer to the \[/campaign/spc/create/\]\(\.\./12-api-reference/61-to-be-deprecated-legacy-smartplus\.md#doc-1767334204047362\) endpoint article and the following code example\.",
     "Bảng sau đây chỉ liệt kê một số tham số liên quan. Để tìm danh sách đầy đủ các tham số, hãy tham khảo bài viết về endpoint [/campaign/spc/create/](../12-api-reference/61-to-be-deprecated-legacy-smartplus.md#doc-1767334204047362) và ví dụ mã dưới đây."),
     
    (r"• For Android Apps, use \*\*Automatic Placement\*\*\. • For iOS Apps, use \*\*Automatic Placement\*\*\.",
     "• Đối với Ứng dụng Android, sử dụng **Vị trí tự động (Automatic Placement)**. • Đối với Ứng dụng iOS, sử dụng **Vị trí tự động (Automatic Placement)**."),
     
    (r"• If `promotion_type` is `APP_ANDROID`, and do not pass `placement_type` and `placements`\.",
     "• Nếu `promotion_type` là `APP_ANDROID`, không truyền `placement_type` và `placements`."),
     
    (r"• The system will automatically configure placements for your Smart\+ Android App Campaigns based on your other settings and select high-quality traffic from various placements to deliver better results\. If provided, the parameters `placement_type` and `placements` will be ignored overwritten as `PLACEMENT_TYPE_AUTOMATIC` and `\[\"PLACEMENT_TIKTOK\",\"PLACEMENT_PANGLE\"\]` separately\.",
     "• Hệ thống sẽ tự động định cấu hình vị trí cho Chiến dịch Smart+ Android App của bạn dựa trên các cài đặt khác và chọn lưu lượng truy cập chất lượng cao từ các vị trí khác nhau để mang lại kết quả tốt hơn. Nếu được cung cấp, các tham số `placement_type` và `placements` sẽ bị bỏ qua và được ghi đè tương ứng thành `PLACEMENT_TYPE_AUTOMATIC` và `[\"PLACEMENT_TIKTOK\",\"PLACEMENT_PANGLE\"]`."),
     
    (r"• To retrieve the exact placement setting of a Smart\+ App Campaign, use \[/campaign/spc/get/\]\(\.\./12-api-reference/61-to-be-deprecated-legacy-smartplus\.md#doc-1767334299811842\)\.",
     "• Để truy xuất cài đặt vị trí chính xác của Chiến dịch Smart+ App, hãy sử dụng [/campaign/spc/get/](../12-api-reference/61-to-be-deprecated-legacy-smartplus.md#doc-1767334299811842)."),
     
    (r"• If `promotion_type` is `APP_IOS`, do not pass `placement_type` and `placements`\.",
     "• Nếu `promotion_type` là `APP_IOS`, không truyền `placement_type` và `placements`."),
     
    (r"• Starting June 30th, 2025, the system will automatically configure placements for your Smart\+ iOS App Campaigns based on your other settings and select high-quality traffic from various placements to deliver better results\. If provided after June 30th, 2025, the parameters `placement_type` and `placements` will be ignored overwritten as `PLACEMENT_TYPE_AUTOMATIC` and `\[\"PLACEMENT_TIKTOK\",\"PLACEMENT_PANGLE\"\]` separately\.",
     "• Bắt đầu từ ngày 30 tháng 6 năm 2025, hệ thống sẽ tự động định cấu hình vị trí cho Chiến dịch Smart+ iOS App của bạn dựa trên các cài đặt khác và chọn lưu lượng truy cập chất lượng cao từ các vị trí khác nhau để mang lại kết quả tốt hơn. Nếu được cung cấp sau ngày 30 tháng 6 năm 2025, các tham số `placement_type` và `placements` sẽ bị bỏ qua và ghi đè tương ứng thành `PLACEMENT_TYPE_AUTOMATIC` và `[\"PLACEMENT_TIKTOK\",\"PLACEMENT_PANGLE\"]`."),
]
