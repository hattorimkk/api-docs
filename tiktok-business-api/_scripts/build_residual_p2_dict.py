#!/usr/bin/env python3
"""
Generate translation rules for residual_p2.json (Docs 1-27).
"""
import json, re

with open('tiktok-business-api/_work/residual_p2.json') as f:
    items = json.load(f)

# Translation dictionary mapping exact English string or regex pattern to Vietnamese
TRANS_MAP = [
    # Common across multiple docs
    (r"Disabled You cannot use \[/campaign/spc/create/\]\(\.\./12-api-reference/61-to-be-deprecated-legacy-smartplus\.md#doc-1767334204047362\) to create Smart\+ ([^.]+)\.",
     r"Đã tắt Bạn không thể sử dụng [/campaign/spc/create/](../12-api-reference/61-to-be-deprecated-legacy-smartplus.md#doc-1767334204047362) để tạo Smart+ \1."),
     
    (r"Disabled You cannot use \[/campaign/spc/create/\]\(\.\./12-api-reference/61-to-be-deprecated-legacy-smartplus\.md#doc-1767334204047362\) to create Smart Creative ([^.]+)\.",
     r"Đã tắt Bạn không thể sử dụng [/campaign/spc/create/](../12-api-reference/61-to-be-deprecated-legacy-smartplus.md#doc-1767334204047362) để tạo Smart Creative \1."),
     
    (r"Disabled ([A-Za-z\s]+) cannot be used in \[/split_test/create/\]\(\.\./12-api-reference/65-super-split-test\.md#doc-1742666471475201\) to create split test groups\.",
     r"Đã tắt \1 không thể sử dụng trong [/split_test/create/](../12-api-reference/65-super-split-test.md#doc-1742666471475201) để tạo các nhóm thử nghiệm phân tách."),
     
    (r"Pass in the `feed_log_id` obtained from Step ii\. If the field `warn_affected_products` in the response is not null, examine your CSV file or JSON schema\.",
     r"Truyền `feed_log_id` thu được từ Bước ii. Nếu trường `warn_affected_products` trong phản hồi không phải null, hãy kiểm tra tệp CSV hoặc giản đồ JSON của bạn."),
     
    (r"1\. Create a catalog in TikTok Business Center\.",
     r"1. Tạo danh mục trong TikTok Business Center."),
     
    (r"For detailed instructions, see \[Manage Catalog in Business Center\]\(https://ads\.tiktok\.com/help/article\?aid=10006734\)\.",
     r"Để biết hướng dẫn chi tiết, xem [Quản lý danh mục trong Business Center](https://ads.tiktok.com/help/article?aid=10006734)."),
     
    (r"For detailed instructions, see \[Add Users to TikTok Business Center\]\(https://ads\.tiktok\.com/help/article\?aid=10006716\)\.",
     r"Để biết hướng dẫn chi tiết, xem [Thêm người dùng vào TikTok Business Center](https://ads.tiktok.com/help/article?aid=10006716)."),
     
    (r"For detailed instructions, see \[Manage Catalog in Business Center - Share Catalog with a Member\]\(https://ads\.tiktok\.com/help/article\?aid=10006734\)\.",
     r"Để biết hướng dẫn chi tiết, xem [Quản lý danh mục trong Business Center - Chia sẻ danh mục với thành viên](https://ads.tiktok.com/help/article?aid=10006734)."),
     
    (r"• Specified when Optimization location is App • Not specified when Optimization location is Website",
     r"• Được chỉ định khi Vị trí tối ưu hóa là Ứng dụng • Không chỉ định khi Vị trí tối ưu hóa là Trang web"),
     
    (r"Select up to two product attributes to display alongside the vehicle title in your ads: • Dealer name • Make • Model • Year",
     r"Chọn tối đa hai thuộc tính sản phẩm để hiển thị cùng tiêu đề xe trong quảng cáo của bạn: • Tên đại lý (Dealer name) • Hãng xe (Make) • Kiểu xe (Model) • Năm sản xuất (Year)"),
     
    (r"1\. Create an Auto-Model catalog using \[/catalog/create/\]\(\.\./12-api-reference/25-catalog-management\.md#doc-1740306481755138\)\.",
     r"1. Tạo danh mục Mẫu xe (Auto-Model) bằng [/catalog/create/](../12-api-reference/25-catalog-management.md#doc-1740306481755138)."),
     
    (r"An Auto-Model catalog with \*\*at least one approved product\*\*",
     r"Một danh mục Mẫu xe (Auto-Model) có **ít nhất một sản phẩm đã được phê duyệt**"),
     
    (r"Specify the ID of an Inventory Card portfolio\. To get the Inventory Card portfolio ID \(creative_portfolio_id\), call \[/creative/portfolio/create/\]\(\.\./12-api-reference/36-creative-portfolios\.md#doc-1739091950439426\)\.",
     r"Chỉ định ID của danh mục Thẻ kho hàng (Inventory Card portfolio). Để lấy ID danh mục Thẻ kho hàng (creative_portfolio_id), hãy gọi [/creative/portfolio/create/](../12-api-reference/36-creative-portfolios.md#doc-1739091950439426)."),
     
    (r'The owner of the authorized TikTok account has enabled the "Everyone" permission for Direct Messages in TikTok App Settings\.',
     r'Chủ sở hữu tài khoản TikTok được ủy quyền đã bật quyền "Mọi người" (Everyone) cho Tin nhắn trực tiếp (Direct Messages) trong Cài đặt ứng dụng TikTok.'),
     
    (r"- If the audience has installed the instant messaging app \(such as WhatsApp\), they can send a message to you by tapping your ad\.",
     r"- Nếu đối tượng mục tiêu đã cài đặt ứng dụng nhắn tin tức thì (như WhatsApp), họ có thể gửi tin nhắn cho bạn bằng cách nhấn vào quảng cáo của bạn."),
     
    (r"- If the audience hasn't installed the instant messaging app, they will be directed to view a Custom Instant Page where you can provide relevant info and call-to-action buttons to prompt app installation\.",
     r"- Nếu đối tượng mục tiêu chưa cài đặt ứng dụng nhắn tin tức thì, họ sẽ được chuyển hướng đến xem Trang tức thì tùy chỉnh, nơi bạn có thể cung cấp thông tin liên quan và nút kêu gọi hành động để nhắc cài đặt ứng dụng."),
     
    (r"- We recommend connecting to one of our integrated \[Message Management Tools\]\(https://ads\.tiktok\.com/help/article/tiktok-messaging-ads\?lang=en#heading-8\) \(MMTs\)\. MMTs offer customer support, automation, and conversational AI capabilities, helping you streamline ad campaign setup and scale message handling efficiently\.",
     r"- Chúng tôi khuyên bạn nên kết nối với một trong các [Công cụ quản lý tin nhắn](https://ads.tiktok.com/help/article/tiktok-messaging-ads?lang=en#heading-8) (MMT) tích hợp của chúng tôi. MMT cung cấp các tính năng hỗ trợ khách hàng, tự động hóa và AI đàm thoại, giúp bạn hợp lý hóa việc thiết lập chiến dịch quảng cáo và mở rộng quy mô xử lý tin nhắn hiệu quả."),
     
    (r"- If you've already integrated with an MMT and are optimizing for Conversations, make sure to set up webhooks to automatically forward message events to TikTok for conversion tracking\.",
     r"- Nếu bạn đã tích hợp với một MMT và đang tối ưu hóa cho Cuộc trò chuyện, hãy đảm bảo thiết lập webhook để tự động chuyển tiếp các sự kiện tin nhắn đến TikTok nhằm theo dõi chuyển đổi."),
     
    (r"- If you are using WhatsApp, you will need to use a unique phone number for the WhatsApp Business API that is not registered with other WhatsApp apps\.",
     r"- Nếu bạn đang sử dụng WhatsApp, bạn sẽ cần sử dụng số điện thoại duy nhất cho WhatsApp Business API chưa được đăng ký với các ứng dụng WhatsApp khác."),
     
    (r"- Some MMTs, such as Pancake, may require you to add to your wallet before you can reply to customer messages\.",
     r"- Một số MMT, chẳng hạn như Pancake, có thể yêu cầu bạn nạp tiền vào ví trước khi có thể trả lời tin nhắn của khách hàng."),
     
    (r"• To use the Instant messaging app Messenger: • Set messaging_app_type to MESSENGER and specify a Facebook Page ID through messaging_app_account_id\.",
     r"• Để sử dụng ứng dụng nhắn tin tức thì Messenger: • Đặt messaging_app_type thành MESSENGER và chỉ định ID Trang Facebook qua messaging_app_account_id."),
     
    (r"\*\*Select Placement\*\* with TikTok placement",
     r"**Chọn vị trí (Select Placement)** với vị trí TikTok"),
     
    (r"The available targeting regions are as follows: • APAC: Australia, Cambodia, Indonesia, Japan, Malaysia, New Zealand, Philippines, Singapore, South Korea, Taiwan, Thailand, Vietnam • EMEA: France, Germany, Italy, Saudi Arabia, Spain, United Kingdom • LATAM: Brazil, Chile, Colombia, Mexico, Peru • NA: Canada, United States",
     r"Các khu vực nhắm mục tiêu khả dụng như sau: • APAC: Úc, Campuchia, Indonesia, Nhật Bản, Malaysia, New Zealand, Philippines, Singapore, Hàn Quốc, Đài Loan, Thái Lan, Việt Nam • EMEA: Pháp, Đức, Ý, Ả Rập Xê Út, Tây Ban Nha, Vương quốc Anh • LATAM: Brazil, Chile, Colombia, Mexico, Peru • NA: Canada, Hoa Kỳ"),
     
    (r"Pass the IDs of locations within the following regions: • APAC: Australia, Cambodia, Indonesia, Japan, Malaysia, New Zealand, Philippines, Singapore, South Korea, Taiwan, Thailand, Vietnam • EMEA: France, Germany, Italy, Saudi Arabia, Spain, United Kingdom • LATAM: Brazil, Chile, Colombia, Mexico, Peru • NA: Canada, United States",
     r"Truyền ID của các vị trí thuộc các khu vực sau: • APAC: Úc, Campuchia, Indonesia, Nhật Bản, Malaysia, New Zealand, Philippines, Singapore, Hàn Quốc, Đài Loan, Thái Lan, Việt Nam • EMEA: Pháp, Đức, Ý, Ả Rập Xê Út, Tây Ban Nha, Vương quốc Anh • LATAM: Brazil, Chile, Colombia, Mexico, Peru • NA: Canada, Hoa Kỳ"),
     
    (r"• If optimization_goal is CLICK, do not pass optimization_event\. • If optimization_goal is CONVERSATION, pass optimization_event with the value of MESSAGING_CONVERSATION\.",
     r"• Nếu optimization_goal là CLICK, không truyền optimization_event. • Nếu optimization_goal là CONVERSATION, truyền optimization_event với giá trị là MESSAGING_CONVERSATION."),
     
    (r"Specify a valid message event set when the following conditions are met: • Optimization goal is set to CONVERSATION • Messaging app is set to WhatsApp or Zalo • Conversion tracking using an MMT is enabled",
     r"Chỉ định một tập sự kiện tin nhắn hợp lệ khi đáp ứng các điều kiện sau: • Mục tiêu tối ưu hóa được đặt thành CONVERSATION • Ứng dụng nhắn tin được đặt thành WhatsApp hoặc Zalo • Bật theo dõi chuyển đổi bằng MMT"),
     
    (r"Any of the following values for bid_type: • BID_TYPE_NO_BID • BID_TYPE_CUSTOM • If bid_type is BID_TYPE_CUSTOM, specify conversion_bid at the same time\.",
     r"Bất kỳ giá trị nào sau đây cho bid_type: • BID_TYPE_NO_BID • BID_TYPE_CUSTOM • Nếu bid_type là BID_TYPE_CUSTOM, hãy chỉ định conversion_bid cùng lúc."),
     
    (r">  • If you specify a TikTok Shop, sales of products belonging to the TikTok Shop will be reported\.  • If you specify a showcase, sales of products from other TikTok Shops will not be reported\.",
     r"> • Nếu bạn chỉ định một TikTok Shop, doanh số của các sản phẩm thuộc TikTok Shop sẽ được báo cáo. • Nếu bạn chỉ định một showcase, doanh số của các sản phẩm từ TikTok Shop khác sẽ không được báo cáo."),
     
    (r"Select the TikTok account that you'll use to go LIVE as your identity\. Your ad will start running when a LIVE session starts\.",
     r"Chọn tài khoản TikTok bạn sẽ sử dụng để phát LIVE làm danh tính của mình. Quảng cáo của bạn sẽ bắt đầu chạy khi phiên LIVE bắt đầu."),
     
    (r"Specify the TikTok account that you'll use to go LIVE\. To get the list of identities under an ad account, use \[/identity/video/get/\]\(\.\./12-api-reference/47-identity\.md#doc-1740939523953666\)\.",
     r"Chỉ định tài khoản TikTok bạn sẽ sử dụng để phát LIVE. Để lấy danh sách danh tính thuộc tài khoản quảng cáo, sử dụng [/identity/video/get/](../12-api-reference/47-identity.md#doc-1740939523953666)."),
     
    (r"Unset\. The default setting is LIVE content\.",
     r"Chưa đặt. Cài đặt mặc định là nội dung LIVE."),
     
    (r"Audience targeting  • Interests & Behaviors  • Smart interests & behaviors",
     r"Nhắm mục tiêu đối tượng • Mối quan tâm & Hành vi • Mối quan tâm & hành vi thông minh"),
     
    (r"Define a schedule that closely aligns with the actual live duration to ensure optimal ad delivery\. Note that ads will only be delivered while the live session is active\.",
     r"Xác định lịch trình sát với thời lượng phát live thực tế để đảm bảo phân phối quảng cáo tối ưu. Lưu ý rằng quảng cáo sẽ chỉ được phân phối khi phiên live đang hoạt động."),
     
    (r"Specify a schedule that closely aligns with the actual live duration",
     r"Chỉ định lịch trình sát với thời lượng phát live thực tế"),
     
    (r"> After you create a Product Shopping campaign, you can only update the following settings of the campaign: • Budget: budget, budget_mode",
     r"> Sau khi tạo chiến dịch Product Shopping, bạn chỉ có thể cập nhật các cài đặt sau của chiến dịch: • Ngân sách: budget, budget_mode"),
     
    (r"## 2\. Create and manage TikTok Shops",
     r"## 2. Tạo và quản lý TikTok Shop"),
     
    (r"TikTok Commerce \(formerly known as TikTok Shopping\) offers TikTok Shops for brands and sellers who want to sell directly on TikTok\.",
     r"TikTok Commerce (trước đây gọi là TikTok Shopping) cung cấp TikTok Shop cho các thương hiệu và người bán muốn bán hàng trực tiếp trên TikTok."),
     
    (r"- iii\. Share a TikTok Shop with members and grant the TikTok Shop management access using \[/bc/asset/assign/\]\(\.\./12-api-reference/12-bc-assets\.md#doc-1740855276535809\)\.",
     r"- iii. Chia sẻ TikTok Shop với các thành viên và cấp quyền quản lý TikTok Shop bằng cách sử dụng [/bc/asset/assign/](../12-api-reference/12-bc-assets.md#doc-1740855276535809)."),
     
    (r"> After you create a Product Shopping ad group, you can only update the following settings of the ad group: • Status: operation_status • Budget: budget • Schedule: schedule_end_time",
     r"> Sau khi tạo nhóm quảng cáo Product Shopping, bạn chỉ có thể cập nhật các cài đặt sau của nhóm quảng cáo: • Trạng thái: operation_status • Ngân sách: budget • Lịch trình: schedule_end_time"),
     
    (r"TikTok Shop with the targeting location as any of the following regions:  • Indonesia • Malaysia • Singapore • Philippines • Thailand • Vietnam",
     r"TikTok Shop có vị trí nhắm mục tiêu là bất kỳ khu vực nào sau đây: • Indonesia • Malaysia • Singapore • Philippines • Thái Lan • Việt Nam"),
     
    (r"Specify the ID of the catalog that is bound to the TikTok Shop\. You can use \[/store/list/\]\(\.\./12-api-reference/45-gmv-max-p2\.md#doc-1822001097240578\) to get the catalog ID \(catalog_id\)\.",
     r"Chỉ định ID của danh mục được liên kết với TikTok Shop. Bạn có thể sử dụng [/store/list/](../12-api-reference/45-gmv-max-p2.md#doc-1822001097240578) để lấy ID danh mục (catalog_id)."),
     
    (r"The following table outlines the impact by TikTok Shop Ads types and their corresponding configurations:",
     r"Bảng sau đây phác thảo tác động theo từng loại Quảng cáo TikTok Shop và các cấu hình tương ứng:"),
     
    (r"Type of TikTok Shop Ad", r"Loại Quảng cáo TikTok Shop"),
    
    (r"This ad can't be turned on because custom shop ads are no longer available",
     r"Không thể bật quảng cáo này vì quảng cáo shop tùy chỉnh không còn khả dụng nữa"),
     
    (r"This ad can't be edited because custom shop ads are no longer available",
     r"Không thể chỉnh sửa quảng cáo này vì quảng cáo shop tùy chỉnh không còn khả dụng nữa"),
     
    (r"## What actions you should take", r"## Những hành động bạn nên thực hiện"),
    (r"# What actions you should take", r"## Những hành động bạn nên thực hiện"),
    (r"## Why GMV Max API\?", r"## Tại sao nên dùng GMV Max API?"),
    
    (r"- \*\*Automation at scale\*\*: Increase the effectiveness of your Shop Ads Campaigns at scale\. The GMV Max API automates product selection, creative optimization, and bidding strategies, allowing you to run complex campaigns with minimal manual effort\.",
     r"- **Tự động hóa trên quy mô lớn**: Nâng cao hiệu quả của các Chiến dịch Shop Ads trên quy mô lớn. GMV Max API tự động hóa việc lựa chọn sản phẩm, tối ưu hóa mẫu quảng cáo và chiến lược giá thầu, cho phép bạn chạy các chiến dịch phức tạp với nỗ lực thủ công tối thiểu."),
     
    (r"- \*\*Deep customization\*\*: Build tailored advertising solutions that fit your unique advertising needs\. The GMV Max API allows you to customize campaign parameters, fine-tune ROI targets, and adapt strategies dynamically based on real-time performance\.",
     r"- **Tùy chỉnh sâu sắc**: Xây dựng các giải pháp quảng cáo phù hợp với nhu cầu quảng cáo độc đáo của bạn. GMV Max API cho phép bạn tùy chỉnh các tham số chiến dịch, tinh chỉnh mục tiêu ROI và điều chỉnh chiến lược linh hoạt dựa trên hiệu suất theo thời gian thực."),
     
    (r"- \*\*Seamless API integration\*\*: Connect directly to the TikTok Shop ecosystem with robust, developer-friendly endpoints, ensuring smooth operational transitions and minimal disruption to your advertising workflows\.",
     r"- **Tích hợp API liền mạch**: Kết nối trực tiếp với hệ sinh thái TikTok Shop bằng các endpoint mạnh mẽ, thân thiện với nhà phát triển, đảm bảo quá trình chuyển đổi hoạt động suôn sẻ và ít gián đoạn quy trình quảng cáo nhất."),
]

with open('tiktok-business-api/_scripts/u101_trans_residual_part2.py', 'w', encoding='utf-8') as f:
    f.write('''#!/usr/bin/env python3
"""
Residual Part 2 translations: Docs 1-27
"""

RESIDUAL_PART2_RULES = [
''')
    for pat, rep in TRANS_MAP:
        f.write(f'    ({repr(pat)},\n     {repr(rep)}),\n')
    f.write(']\n')

print("Created tiktok-business-api/_scripts/u101_trans_residual_part2.py")
