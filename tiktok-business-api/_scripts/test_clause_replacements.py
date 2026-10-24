#!/usr/bin/env python3
import json, re

with open('tiktok-business-api/_work/unique_outside_table_mixed.json') as f:
    items = json.load(f)

lines = [it['line'] for it in items]

CLAUSE_REPLACEMENTS = [
    # Notes & allowlists
    (r"is currently an allowlist-only feature\. If you (?:want|would like) to use this feature, contact your TikTok representative\.",
     "hiện là tính năng chỉ dành cho danh sách cho phép (allowlist). Nếu bạn muốn sử dụng tính năng này, hãy liên hệ với đại diện TikTok của bạn."),
    (r"is currently an allowlist-only feature and is invitation-only because this catalog type is under development\.",
     "hiện là tính năng chỉ dành cho danh sách cho phép (allowlist) và chỉ theo lời mời vì loại danh mục này đang được phát triển."),
    (r"Gender targeting in Smart\+ Campaigns is currently an allowlist-only feature\. If you want to use this feature, contact your TikTok representative\.",
     "Nhắm mục tiêu theo giới tính trong Chiến dịch Smart+ hiện là tính năng chỉ dành cho danh sách cho phép (allowlist). Nếu bạn muốn sử dụng tính năng này, hãy liên hệ với đại diện TikTok của bạn."),
    (r"Using the Lemon8 or PineDrama subplacement is currently an allowlist-only feature\. If you want to use this feature, contact your TikTok representative\.",
     "Việc sử dụng vị trí phụ Lemon8 hoặc PineDrama hiện là tính năng chỉ dành cho danh sách cho phép (allowlist). Nếu bạn muốn sử dụng tính năng này, hãy liên hệ với đại diện TikTok của bạn."),
    (r"Using the Lemon8 subplacement \(LEMON8\) in your ad group is currently an allowlist-only feature\. If you want to use this feature, contact your TikTok representative\.",
     "Việc sử dụng vị trí phụ Lemon8 (LEMON8) trong nhóm quảng cáo của bạn hiện là tính năng chỉ dành cho danh sách cho phép (allowlist). Nếu bạn muốn sử dụng tính năng này, hãy liên hệ với đại diện TikTok của bạn."),
     
    # Budget clauses
    (r"When you select a campaign budget mode: • The ad group budget is disabled\. The campaign-level budget will be automatically allocated and optimized across ad groups\. • When you select an ad group budget mode, specify an ad group budget\.",
     "Khi bạn chọn chế độ ngân sách chiến dịch: • Ngân sách nhóm quảng cáo sẽ bị tắt. Ngân sách cấp chiến dịch sẽ được tự động phân bổ và tối ưu hóa giữa các nhóm quảng cáo. • Khi bạn chọn chế độ ngân sách nhóm quảng cáo, hãy chỉ định ngân sách nhóm quảng cáo."),
    (r"When you select a campaign budget mode, this setting, if specified, must be the same across all ad groups within the campaign\.",
     "Khi bạn chọn chế độ ngân sách chiến dịch, cài đặt này, nếu được chỉ định, phải giống nhau giữa tất cả các nhóm quảng cáo trong chiến dịch."),
    (r"When you select a campaign budget mode, this setting must be the same across all ad groups within the campaign\.",
     "Khi bạn chọn chế độ ngân sách chiến dịch, cài đặt này phải giống nhau giữa tất cả các nhóm quảng cáo trong chiến dịch."),
    (r"When you select a campaign budget mode, the billing event must be the same across ad groups within the campaign\.",
     "Khi bạn chọn chế độ ngân sách chiến dịch, sự kiện tính phí phải giống nhau giữa các nhóm quảng cáo trong chiến dịch."),
    (r"When you select a campaign budget mode, this setting, if specified, must be the same across ad groups within the same campaign\.",
     "Khi bạn chọn chế độ ngân sách chiến dịch, cài đặt này, nếu được chỉ định, phải giống nhau giữa các nhóm quảng cáo trong cùng chiến dịch."),
    (r"When you select a campaign budget mode, this setting must be the same across ad groups within the same campaign\.",
     "Khi bạn chọn chế độ ngân sách chiến dịch, cài đặt này phải giống nhau giữa các nhóm quảng cáo trong cùng chiến dịch."),
    (r"When you select a campaign budget mode, this setting, if specified, must be the same for ad groups within the same campaign\.",
     "Khi bạn chọn chế độ ngân sách chiến dịch, cài đặt này, nếu được chỉ định, phải giống nhau cho các nhóm quảng cáo trong cùng chiến dịch."),
    (r"When you select a campaign budget mode, this setting must be the same for ad groups within the same campaign\.",
     "Khi bạn chọn chế độ ngân sách chiến dịch, cài đặt này phải giống nhau cho các nhóm quảng cáo trong cùng chiến dịch."),
    (r"must be the same across all ad groups within the campaign\.", "phải giống nhau giữa tất cả các nhóm quảng cáo trong chiến dịch."),
    (r"must be the same across ad groups within the campaign\.", "phải giống nhau giữa các nhóm quảng cáo trong chiến dịch."),
    (r"must be the same across ad groups within the same campaign\.", "phải giống nhau giữa các nhóm quảng cáo trong cùng chiến dịch."),
    (r"must be the same for ad groups within the same campaign\.", "phải giống nhau cho các nhóm quảng cáo trong cùng chiến dịch."),
    (r"for ad groups within the same campaign\.", "cho các nhóm quảng cáo trong cùng chiến dịch."),
    (r"across ad groups within the same campaign\.", "giữa các nhóm quảng cáo trong cùng chiến dịch."),
    (r"within the same campaign\.", "trong cùng chiến dịch."),
    (r"within the campaign\.", "trong chiến dịch."),
    
    # Schedule clauses
    (r"Set start time and run ad group continuously", "Đặt thời gian bắt đầu và chạy nhóm quảng cáo liên tục"),
    (r"Set start and end time", "Đặt thời gian bắt đầu và kết thúc"),
    (r'You can only choose "Set start time and run ad group continuously" when campaign budget mode is Daily\.',
     'Bạn chỉ có thể chọn "Đặt thời gian bắt đầu và chạy nhóm quảng cáo liên tục" khi chế độ ngân sách chiến dịch là Hàng ngày (Daily).'),
    (r'You can only set this setting to SCHEDULE_FROM_NOW when campaign budget mode is Daily\.',
     'Bạn chỉ có thể đặt cài đặt này thành SCHEDULE_FROM_NOW khi chế độ ngân sách chiến dịch là Hàng ngày (Daily).'),
     
    # Realtime API / RTA
    (r"When at the campaign level Realtime API is enabled, this setting is not supported\.",
     "Khi API thời gian thực (Realtime API) được bật ở cấp chiến dịch, cài đặt này không được hỗ trợ."),
    (r"When at the campaign level rta_id is specified, this setting is not supported\.",
     "Khi rta_id được chỉ định ở cấp chiến dịch, cài đặt này không được hỗ trợ."),
    (r"When Realtime API \(RTA\) is enabled at the campaign level, this setting is not supported\.",
     "Khi API thời gian thực (RTA) được bật ở cấp chiến dịch, cài đặt này không được hỗ trợ."),
    (r"When rta_id is specified at the campaign level, this setting is not supported\.",
     "Khi rta_id được chỉ định ở cấp chiến dịch, cài đặt này không được hỗ trợ."),
     
    # Brand safety
    (r"When you configure brand safety settings, you need to configure post-bid third-party brand safety measurement\.",
     "Khi bạn cấu hình cài đặt an toàn thương hiệu, bạn cần cấu hình đo lường an toàn thương hiệu bên thứ ba sau đấu thầu."),
    (r"If you set both brand_safety_postbid_partner and viewability_postbid_partner to IAS, you only need to pass ias_option_wrapped_tag once\.",
     "Nếu bạn đặt cả brand_safety_postbid_partner và viewability_postbid_partner thành IAS, bạn chỉ cần truyền ias_option_wrapped_tag một lần."),
    (r"IAS with IAS wrapped tag", "IAS với thẻ bọc IAS (wrapped tag)"),
    (r"Disable or enabled with any of the following partners:", "Đã tắt hoặc đã bật với bất kỳ đối tác nào sau đây:"),
    (r"Not specified or specify any of the following values:", "Không chỉ định hoặc chỉ định bất kỳ giá trị nào sau đây:"),
    (r"Specify a valid value when viewability_postbid_partner is IAS\.", "Chỉ định giá trị hợp lệ khi viewability_postbid_partner là IAS."),
    (r"Specify a valid value when brand_safety_postbid_partner is IAS\.", "Chỉ định giá trị hợp lệ khi brand_safety_postbid_partner là IAS."),
     
    # Subplacements
    (r"with one or more of the following options: • Lemon8 • PineDrama", "với một hoặc nhiều tùy chọn sau: • Lemon8 • PineDrama"),
    (r"with the following option: • Lemon8", "với tùy chọn sau: • Lemon8"),
    (r"Not specified or specify one or more of the following values: • LEMON8 • PINE_DRAMA", "Không chỉ định hoặc chỉ định một hoặc nhiều giá trị sau: • LEMON8 • PINE_DRAMA"),
    (r"Not specified or specify the following value: • LEMON8", "Không chỉ định hoặc chỉ định giá trị sau: • LEMON8"),
     
    # Spark ads & Identity
    (r"When you use a Spark Ads identity, you can only use a standard call-to-action\.",
     "Khi bạn sử dụng danh tính Spark Ads, bạn chỉ có thể sử dụng lời kêu gọi hành động tiêu chuẩn."),
    (r"When you use a Spark Ads identity, you can only specify a standard call-to-action via call_to_action\.",
     "Khi bạn sử dụng danh tính Spark Ads, bạn chỉ có thể chỉ định lời kêu gọi hành động tiêu chuẩn qua call_to_action."),
    (r"For non-Spark Ads identities, set this field to CUSTOMIZED_USER\.", "Đối với danh tính non-Spark Ads, hãy đặt trường này thành CUSTOMIZED_USER."),
    (r"For Spark Ads identities, set this field to AUTH_CODE, TT_USER, or BC_AUTH_TT\.", "Đối với danh tính Spark Ads, hãy đặt trường này thành AUTH_CODE, TT_USER, hoặc BC_AUTH_TT."),
    (r"For Spark Ads identities, specify the TikTok account you want to use through identity_id\.", "Đối với danh tính Spark Ads, hãy chỉ định tài khoản TikTok bạn muốn sử dụng qua identity_id."),
    (r"For non-Spark Ads identities, do not pass identity_id\.", "Đối với danh tính non-Spark Ads, không truyền identity_id."),
     
    # CTA
    (r"To use standard call to action, specify call_to_action\.", "Để sử dụng lời kêu gọi hành động tiêu chuẩn, hãy chỉ định call_to_action."),
    (r"To use dynamic call to action, specify call_to_action_id\.", "Để sử dụng lời kêu gọi hành động động, hãy chỉ định call_to_action_id."),
     
    # Regional
    (r"This setting is only supported for advertisers who are registered in the US or Canada\.",
     "Cài đặt này chỉ được hỗ trợ cho các nhà quảng cáo đã đăng ký tại Hoa Kỳ hoặc Canada."),
    (r"Agreeing to the Compliance Assurance Policy for Gaming Advertisers is required for advertisers who want to deliver ads in Taiwan\.",
     "Việc đồng ý với Chính sách đảm bảo tuân thủ cho nhà quảng cáo game là bắt buộc đối với nhà quảng cáo muốn phân phối quảng cáo tại Đài Loan."),
]

en_word_re = re.compile(r'\b(the|to|in|of|and|is|you|for|can|with|on|this|that|be|are|by|an|as|or|from|will|must|use|see|refer|note|set|when|if|not|only|all|have|has|do|does|at|under|into|before|after|between|each|other|more|such|any|which|about)\b', re.IGNORECASE)

still_mixed = []
for l in lines:
    cur = l
    for pat, rep in CLAUSE_REPLACEMENTS:
        cur = re.sub(pat, rep, cur)
    matches = en_word_re.findall(cur)
    if len(matches) >= 2:
        still_mixed.append(cur)

print(f"Before: {len(lines)} lines")
print(f"After clause replacements: {len(still_mixed)} lines")
