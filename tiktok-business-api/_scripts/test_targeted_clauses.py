#!/usr/bin/env python3
"""
Test applying sentence and clause translations to eliminate mixed lines outside tables.
"""
import re

TEST_RULES = [
    # General recurring clauses
    (r"\bwhen you select a campaign budget mode:?\s*•?\s*the ad group budget is disabled\. The campaign-level budget will be automatically allocated and optimized across ad groups\.?\s*•?\s*when you select an ad group budget mode, specify an ad group budget\.",
     "• Khi bạn chọn chế độ ngân sách chiến dịch: Ngân sách nhóm quảng cáo sẽ bị tắt. Ngân sách cấp chiến dịch sẽ được tự động phân bổ và tối ưu hóa giữa các nhóm quảng cáo. • Khi bạn chọn chế độ ngân sách nhóm quảng cáo, hãy chỉ định ngân sách nhóm quảng cáo.", re.IGNORECASE),
     
    (r"•\s*When budget_optimize_on is true at the campaign level, budget_mode and budget are not supported\.\s*•\s*When budget_optimize_on is false, specify budget_mode and budget\.",
     "• Khi budget_optimize_on là true ở cấp chiến dịch, budget_mode và budget không được hỗ trợ. • Khi budget_optimize_on là false, hãy chỉ định budget_mode và budget."),
     
    (r"•\s*To set start time and run the ad group continuously, set schedule_type to SCHEDULE_FROM_NOW and specify schedule_start_time\.\s*•\s*To set start and end time, set schedule_type to SCHEDULE_START_END and specify schedule_start_time and schedule_end_time\.",
     "• Để đặt thời gian bắt đầu và chạy nhóm quảng cáo liên tục, hãy đặt schedule_type thành SCHEDULE_FROM_NOW và chỉ định schedule_start_time. • Để đặt thời gian bắt đầu và kết thúc, hãy đặt schedule_type thành SCHEDULE_START_END và chỉ định schedule_start_time và schedule_end_time."),
     
    (r"When you select a campaign budget mode, this setting, if specified, must be the same across all ad groups within the campaign\.",
     "Khi bạn chọn chế độ ngân sách chiến dịch, cài đặt này, nếu được chỉ định, phải giống nhau giữa tất cả các nhóm quảng cáo trong chiến dịch."),
     
    (r"When you select a campaign budget mode, this setting must be the same across all ad groups within the campaign\.",
     "Khi bạn chọn chế độ ngân sách chiến dịch, cài đặt này phải giống nhau giữa tất cả các nhóm quảng cáo trong chiến dịch."),
     
    (r"When you select a campaign budget mode, the billing event must be the same across ad groups within the campaign\.",
     "Khi bạn chọn chế độ ngân sách chiến dịch, sự kiện tính phí phải giống nhau giữa các nhóm quảng cáo trong chiến dịch."),
     
    (r"must be the same across all ad groups within the campaign\.",
     "phải giống nhau giữa tất cả các nhóm quảng cáo trong chiến dịch."),
     
    (r"must be the same across ad groups within the campaign\.",
     "phải giống nhau giữa các nhóm quảng cáo trong chiến dịch."),
     
    (r"must be the same for ad groups within the campaign\.",
     "phải giống nhau cho các nhóm quảng cáo trong chiến dịch."),
     
    (r"must be the same across ad groups within the same campaign\.",
     "phải giống nhau giữa các nhóm quảng cáo trong cùng chiến dịch."),
     
    (r"must be the same for ad groups within the same campaign\.",
     "phải giống nhau cho các nhóm quảng cáo trong cùng chiến dịch."),
     
    (r"within the same campaign\.",
     "trong cùng chiến dịch."),
     
    (r"is currently an allowlist-only feature\. If you want to use this feature, contact your TikTok representative\.",
     "hiện là tính năng chỉ dành cho danh sách cho phép (allowlist). Nếu bạn muốn sử dụng tính năng này, hãy liên hệ với đại diện TikTok của bạn."),
     
    (r"is currently an allowlist-only feature\. If you would like to use this feature, contact your TikTok representative\.",
     "hiện là tính năng chỉ dành cho danh sách cho phép (allowlist). Nếu bạn muốn sử dụng tính năng này, hãy liên hệ với đại diện TikTok của bạn."),
     
    (r"Disable or enabled with any of the following partners: • DoubleVerify • IAS with IAS wrapped tag • Zefr \*\*Lưu ý:\*\* When you configure brand safety settings, you need to configure post-bid third-party brand safety measurement\.",
     "Đã tắt hoặc đã bật với bất kỳ đối tác nào sau đây: • DoubleVerify • IAS với thẻ bọc IAS (wrapped tag) • Zefr **Lưu ý:** Khi bạn cấu hình cài đặt an toàn thương hiệu, bạn cần cấu hình đo lường an toàn thương hiệu bên thứ ba sau đấu thầu."),
     
    (r"Một trong các loại sau: • Set start time and run ad group continuously • Set start and end time \*\*Lưu ý:\*\* You can only choose \"Set start time and run ad group continuously\" when campaign budget mode is Daily\.",
     "Một trong các loại sau: • Đặt thời gian bắt đầu và chạy nhóm quảng cáo liên tục • Đặt thời gian bắt đầu và kết thúc **Lưu ý:** Bạn chỉ có thể chọn \"Đặt thời gian bắt đầu và chạy nhóm quảng cáo liên tục\" khi chế độ ngân sách chiến dịch là Hàng ngày (Daily)."),
     
    (r"Đã tắt hoặc đã bật with one or more of the following options: • Lemon8 • PineDrama \*\*Lưu ý:\*\*  • Using the Lemon8 or PineDrama subplacement is currently an allowlist-only feature\. If you want to use this feature, contact your TikTok representative\.",
     "Đã tắt hoặc đã bật với một hoặc nhiều tùy chọn sau: • Lemon8 • PineDrama **Lưu ý:** • Việc sử dụng vị trí phụ Lemon8 hoặc PineDrama hiện là tính năng chỉ dành cho danh sách cho phép (allowlist). Nếu bạn muốn sử dụng tính năng này, hãy liên hệ với đại diện TikTok của bạn."),
     
    (r"location_ids or zipcode_ids or both",
     "location_ids hoặc zipcode_ids hoặc cả hai"),
     
    (r"Một trong các tùy chọn sau: • Dynamic • Standard \*\*Lưu ý:\*\* When you use a Spark Ads identity, you can only use a standard call-to-action\.",
     "Một trong các tùy chọn sau: • Động (Dynamic) • Tiêu chuẩn (Standard) **Lưu ý:** Khi sử dụng danh tính Spark Ads, bạn chỉ có thể sử dụng lời kêu gọi hành động tiêu chuẩn."),
     
    (r"Bật hoặc tắt \(Enabled hoặc Disabled\) \*\*Lưu ý:\*\* When at the campaign level Realtime API is enabled, this setting is not supported\.",
     "Bật hoặc tắt (Enabled hoặc Disabled) **Lưu ý:** Khi API thời gian thực (Realtime API) được bật ở cấp chiến dịch, cài đặt này không được hỗ trợ."),
     
    (r"Specify valid values or not specified \*\*Lưu ý:\*\* When at the campaign level rta_id is specified, this setting is not supported\.",
     "Chỉ định các giá trị hợp lệ hoặc không chỉ định **Lưu ý:** Khi rta_id được chỉ định ở cấp chiến dịch, cài đặt này không được hỗ trợ."),
     
    (r"Một trong các giá trị sau: • CUSTOMIZED_USER • AUTH_CODE • TT_USER • BC_AUTH_TT \*\*Lưu ý:\*\* • For non-Spark Ads identities, set this field to CUSTOMIZED_USER\. • For Spark Ads identities, set this field to AUTH_CODE, TT_USER, or BC_AUTH_TT\.",
     "Một trong các giá trị sau: • CUSTOMIZED_USER • AUTH_CODE • TT_USER • BC_AUTH_TT **Lưu ý:** • Đối với danh tính non-Spark Ads, đặt trường này thành CUSTOMIZED_USER. • Đối với danh tính Spark Ads, đặt trường này thành AUTH_CODE, TT_USER, hoặc BC_AUTH_TT."),
     
    (r"Một trong các loại sau: • Standard Event • Custom Conversion \*\*Lưu ý:\*\* When you select a campaign budget mode, this setting must be the same across all ad groups within the campaign\.",
     "Một trong các loại sau: • Sự kiện tiêu chuẩn (Standard Event) • Chuyển đổi tùy chỉnh (Custom Conversion) **Lưu ý:** Khi bạn chọn chế độ ngân sách chiến dịch, cài đặt này phải giống nhau giữa tất cả các nhóm quảng cáo trong chiến dịch."),
     
    (r"When placement_type is PLACEMENT_TYPE_NORMAL and placements includes PLACEMENT_TIKTOK: • Not specified or specify any of the following: • Lemon8 • PineDrama • When placement_type is not PLACEMENT_TYPE_NORMAL or placements does not include PLACEMENT_TIKTOK: • Not specified",
     "Khi placement_type là PLACEMENT_TYPE_NORMAL và placements bao gồm PLACEMENT_TIKTOK: • Không chỉ định hoặc chỉ định bất kỳ giá trị nào sau đây: • Lemon8 • PineDrama • Khi placement_type không phải là PLACEMENT_TYPE_NORMAL hoặc placements không bao gồm PLACEMENT_TIKTOK: • Không chỉ định"),
     
    (r"• Để sử dụng lời kêu gọi hành động động, hãy chỉ định call_to_action_id\. • To use standard call to action, specify call_to_action\.",
     "• Để sử dụng lời kêu gọi hành động động, hãy chỉ định call_to_action_id. • Để sử dụng lời kêu gọi hành động tiêu chuẩn, hãy chỉ định call_to_action."),
     
    (r"Not specified or specify any of the following values: • DOUBLE_VERIFY • IAS • ZEFR \*\*Lưu ý:\*\* When you configure brand safety settings, you need to configure post-bid third-party brand safety measurement\.",
     "Không chỉ định hoặc chỉ định bất kỳ giá trị nào sau đây: • DOUBLE_VERIFY • IAS • ZEFR **Lưu ý:** Khi bạn cấu hình cài đặt an toàn thương hiệu, bạn cần cấu hình đo lường an toàn thương hiệu bên thứ ba sau đấu thầu."),
     
    (r"Specify a valid value when viewability_postbid_partner is IAS\. \*\*Lưu ý:\*\* If you set both brand_safety_postbid_partner and viewability_postbid_partner to IAS, you only need to pass ias_option_wrapped_tag once\.",
     "Chỉ định một giá trị hợp lệ khi viewability_postbid_partner là IAS. **Lưu ý:** Nếu bạn đặt cả brand_safety_postbid_partner và viewability_postbid_partner thành IAS, bạn chỉ cần truyền ias_option_wrapped_tag một lần."),
     
    (r"Specify a valid value when brand_safety_postbid_partner is IAS\. \*\*Lưu ý:\*\* If you set both brand_safety_postbid_partner and viewability_postbid_partner to IAS, you only need to pass ias_option_wrapped_tag once\.",
     "Chỉ định một giá trị hợp lệ khi brand_safety_postbid_partner là IAS. **Lưu ý:** Nếu bạn đặt cả brand_safety_postbid_partner và viewability_postbid_partner thành IAS, bạn chỉ cần truyền ias_option_wrapped_tag một lần."),
     
    (r"Một trong các loại sau: • Android App • iOS App \*\*Lưu ý:\*\* When you select a campaign budget mode, this setting must be the same across all ad groups within the campaign\.",
     "Một trong các loại sau: • Ứng dụng Android • Ứng dụng iOS **Lưu ý:** Khi bạn chọn chế độ ngân sách chiến dịch, cài đặt này phải giống nhau giữa tất cả các nhóm quảng cáo trong chiến dịch."),
     
    (r"Bật hoặc tắt \(Enabled hoặc Disabled\) \*\*Lưu ý:\*\* This setting is only supported for advertisers who are registered in the US or Canada\.",
     "Bật hoặc tắt (Enabled hoặc Disabled) **Lưu ý:** Cài đặt này chỉ được hỗ trợ cho các nhà quảng cáo đã đăng ký tại Hoa Kỳ hoặc Canada."),
     
    (r"When Mục tiêu là Giá trị, use the following type: • \*\*Giá trị mua hàng \(Purchase value\)\*\* \(còn được gọi là VBO IAP, viết tắt của Tối ưu hóa dựa trên giá trị cho giao dịch mua hàng trong ứng dụng\)",
     "Khi Mục tiêu tối ưu hóa là Giá trị, sử dụng loại sau: • **Giá trị mua hàng (Purchase value)** (còn được gọi là VBO IAP, viết tắt của Tối ưu hóa dựa trên giá trị cho giao dịch mua hàng trong ứng dụng)"),
     
    (r"When Mục tiêu là Giá trị, use any of the following types: • Day 7 ROAS or Highest Value • Day 0 ROAS or Highest Value",
     "Khi Mục tiêu tối ưu hóa là Giá trị, sử dụng bất kỳ loại nào sau đây: • ROAS Ngày 7 hoặc Giá trị cao nhất • ROAS Ngày 0 hoặc Giá trị cao nhất"),
     
    (r"Use any of the following values: • AUTO_BUDGET_INCREASE: To enable Goal-based budget increase\. Allow your budget to increase automatically by up to 20% on days when the ad group is expected to produce more results\.",
     "Sử dụng bất kỳ giá trị nào sau đây: • AUTO_BUDGET_INCREASE: Để bật Tăng ngân sách theo mục tiêu. Cho phép ngân sách của bạn tự động tăng tối đa 20% vào những ngày nhóm quảng cáo dự kiến mang lại nhiều kết quả hơn."),
     
    (r"oCPM \*\*Lưu ý:\*\* When you select a campaign budget mode, the billing event must be the same across ad groups within the campaign\.",
     "oCPM **Lưu ý:** Khi bạn chọn chế độ ngân sách chiến dịch, sự kiện tính phí phải giống nhau giữa các nhóm quảng cáo trong chiến dịch."),
     
    (r"When budget_optimize_on is true hoặc không chỉ định and budget_mode is BUDGET_MODE_DYNAMIC_DAILY_BUDGET: • To enable dynamic daily budget, set this field to true\.",
     "Khi budget_optimize_on là true hoặc không chỉ định và budget_mode là BUDGET_MODE_DYNAMIC_DAILY_BUDGET: • Để bật ngân sách hàng ngày động, hãy đặt trường này thành true."),
     
    (r"• Khi Mục tiêu là Chuyển đổi hoặc Giá trị, hãy chỉ định một Pixel hợp lệ\. • When Goal is Click or Lượt xem trang đích, do not pass pixel_id\.",
     "• Khi Mục tiêu là Chuyển đổi hoặc Giá trị, hãy chỉ định một Pixel hợp lệ. • Khi Mục tiêu là Lượt nhấp hoặc Lượt xem trang đích, không truyền pixel_id."),
     
    (r"With the Tương tác cộng đồng \(Community Interaction\) objective, you can build and nurture your connections with one of the most valuable communities that exists today - the TikTok community\. This objective allows you to drive follower growth or increase traffic to different landing pages on TikTok\.",
     "Với mục tiêu Tương tác cộng đồng (Community Interaction), bạn có thể xây dựng và nuôi dưỡng kết nối với một trong những cộng đồng giá trị nhất hiện nay - cộng đồng TikTok. Mục tiêu này cho phép bạn thúc đẩy tăng trưởng người theo dõi hoặc tăng lưu lượng truy cập đến các trang đích khác nhau trên TikTok."),
     
    (r"• If optimization_goal is set to FOLLOWERS at the ad group level, do not pass call_to_action and call_to_action_id\. • If optimization_goal is set to PAGE_VISIT at the ad group level, specify a standard call-to-action via call_to_action or a dynamic call-to-action via call_to_action_id\.\s+• Để tìm hiểu về the supported values for call_to_action, see \[Enumeration - Call-to-action\]\(\.\./15-appendix/phu-luc-p1\.md#doc-1737174886619138\)\.\s+• Để tìm hiểu về how to obtain a call_to_action_id, see \[Dynamic CTAs\]\(\.\./09-marketing-api/creatives\.md#doc-1740307296329730\)\.",
     "• Nếu optimization_goal được đặt thành FOLLOWERS ở cấp nhóm quảng cáo, không truyền call_to_action và call_to_action_id. • Nếu optimization_goal được đặt thành PAGE_VISIT ở cấp nhóm quảng cáo, hãy chỉ định lời kêu gọi hành động tiêu chuẩn qua call_to_action hoặc lời kêu gọi hành động động qua call_to_action_id. • Để tìm hiểu về các giá trị được hỗ trợ cho call_to_action, xem [Liệt kê - Lời kêu gọi hành động](../15-appendix/phu-luc-p1.md#doc-1737174886619138). • Để tìm hiểu về cách lấy call_to_action_id, xem [CTA động](../09-marketing-api/creatives.md#doc-1740307296329730)."),
     
    (r"Đã tắt hoặc đã bật with the following type: • Reminder Countdown Sticker \*\*Lưu ý:\*\* If you specify the TikTok subplacement Search feed at the ad group level, you cannot use Reminder Countdown Sticker\.",
     "Đã tắt hoặc đã bật với loại sau: • Nhãn dán đếm ngược nhắc nhở (Reminder Countdown Sticker) **Lưu ý:** Nếu bạn chỉ định vị trí phụ Bảng tin tìm kiếm TikTok ở cấp nhóm quảng cáo, bạn không thể sử dụng Nhãn dán đếm ngược nhắc nhở."),
     
    (r"Not passed or specify the ID of the following creative portfolio type: • Reminder Countdown Sticker \(sticker_type as REMINDER_COUNTDOWN\) \*\*Lưu ý:\*\* To create a Reminder Countdown Sticker creative portfolio, use \[/creative/portfolio/create/\]\(\.\./12-api-reference/36-creative-portfolios\.md#doc-1739091950439426\)\.",
     "Không truyền hoặc chỉ định ID của loại danh mục mẫu quảng cáo sau: • Nhãn dán đếm ngược nhắc nhở (Reminder Countdown Sticker - sticker_type là REMINDER_COUNTDOWN) **Lưu ý:** Để tạo danh mục mẫu quảng cáo Nhãn dán đếm ngược nhắc nhở, sử dụng [/creative/portfolio/create/](../12-api-reference/36-creative-portfolios.md#doc-1739091950439426)."),
     
    (r"Đăng ký trước ứng dụng \(App Pre-Registration\) is a type of app promotion that encourages users to register ahead of a game's launch, allowing for automatic downloads of the app on launch day\. By leveraging Đăng ký trước ứng dụng \(App Pre-Registration\), you can build a user base for the game ahead of its launch, generate publicity and awareness, and build momentum to create a vibrant community on the TikTok platform\.",
     "Đăng ký trước ứng dụng (App Pre-Registration) là một loại hình quảng bá ứng dụng khuyến khích người dùng đăng ký trước khi trò chơi ra mắt, cho phép tự động tải xuống ứng dụng vào ngày ra mắt. Bằng cách tận dụng Đăng ký trước ứng dụng (App Pre-Registration), bạn có thể xây dựng cơ sở người dùng cho trò chơi trước khi ra mắt, tạo độ nhận diện và nhận thức, đồng thời tạo đà phát triển một cộng đồng sôi động trên nền tảng TikTok."),
]

with open('tiktok-business-api/docs/08-use-cases/use-case-tao-chien-dich-p1.md') as f:
    text = f.read()

parts = text.split("```")
for i in range(0, len(parts), 2):
    p = parts[i]
    for r in TEST_RULES:
        pattern, repl = r[0], r[1]
        flags = r[2] if len(r) > 2 else 0
        p = re.sub(pattern, repl, p, flags=flags)
    parts[i] = p

new_text = "```".join(parts)

# Scan remaining outside tables
prose_parts = [parts[i] for i in range(0, len(parts), 2)]
en_word_re = re.compile(r'\b(the|to|in|of|and|is|you|for|can|with|on|this|that|be|are|by|an|as|or|from|will|must|use|see|refer|note|set|when|if|not|only|all|have|has|do|does|at|under|into|before|after|between|each|other|more|such|any|which|about)\b', re.IGNORECASE)

outside_table_mixed = []
for p in prose_parts:
    for line in p.splitlines():
        line_str = line.strip()
        if not line_str or line_str.startswith('<a id=') or line_str.startswith('<!-- doc_id:') or line_str.startswith('|'):
            continue
        matches = en_word_re.findall(line_str)
        if len(matches) >= 2:
            outside_table_mixed.append(line_str)

print(f"Remaining mixed lines outside tables: {len(outside_table_mixed)} (was 1279)")
