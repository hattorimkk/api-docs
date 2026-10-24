#!/usr/bin/env python3
import json, re

with open('tiktok-business-api/_work/genuine_mixed_lines.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

lines = [it['line'] for it in items]

RULES = [
    # Budget clauses
    (r'• When you select a campaign budget mode: • The ad group budget is disabled\. The campaign-level budget will be used as the ad group budget\. • When you select an ad group budget strategy: • If the ad group budget limit is No limit or Lifetime limit, you can use any of the following ad group budget modes: • Lifetime • Daily • If the ad group budget limit is Daily limit, you can use the following ad group budget mode: • Daily \*\*Lưu ý:\*\* The ad group budget mode, if specified, must be the same across ad groups within the same campaign\.',
     '• Khi bạn chọn chế độ ngân sách chiến dịch: • Ngân sách nhóm quảng cáo sẽ bị tắt. Ngân sách cấp chiến dịch sẽ được sử dụng làm ngân sách nhóm quảng cáo. • Khi bạn chọn chiến lược ngân sách nhóm quảng cáo: • Nếu giới hạn ngân sách nhóm quảng cáo là Không giới hạn hoặc Giới hạn trọn đời, bạn có thể sử dụng bất kỳ chế độ ngân sách nhóm quảng cáo nào sau đây: • Trọn đời (Lifetime) • Hàng ngày (Daily) • Nếu giới hạn ngân sách nhóm quảng cáo là Giới hạn hàng ngày, bạn có thể sử dụng chế độ ngân sách nhóm quảng cáo sau: • Hàng ngày (Daily) **Lưu ý:** Chế độ ngân sách nhóm quảng cáo, nếu được chỉ định, phải giống nhau giữa các nhóm quảng cáo trong cùng chiến dịch.'),

    (r'• When budget_optimize_on is true at the campaign level, budget_mode and budget are not supported\. • When budget_optimize_on is false and budget_mode is BUDGET_MODE_INFINITE or BUDGET_MODE_TOTAL at the campaign level: • Set budget_mode to BUDGET_MODE_TOTAL or BUDGET_MODE_DYNAMIC_DAILY_BUDGET • Specify a valid budget via budget • When budget_optimize_on is false and budget_mode is BUDGET_MODE_DAY at the campaign level: • Set budget_mode to BUDGET_MODE_DYNAMIC_DAILY_BUDGET • Specify a valid budget via budget \*\*Lưu ý:\*\* The budget_mode, if specified, must be the same across ad groups within the same campaign\.',
     '• Khi budget_optimize_on là true ở cấp chiến dịch, budget_mode và budget không được hỗ trợ. • Khi budget_optimize_on là false và budget_mode là BUDGET_MODE_INFINITE hoặc BUDGET_MODE_TOTAL ở cấp chiến dịch: • Đặt budget_mode thành BUDGET_MODE_TOTAL hoặc BUDGET_MODE_DYNAMIC_DAILY_BUDGET • Chỉ định ngân sách hợp lệ qua budget • Khi budget_optimize_on là false và budget_mode là BUDGET_MODE_DAY ở cấp chiến dịch: • Đặt budget_mode thành BUDGET_MODE_DYNAMIC_DAILY_BUDGET • Chỉ định ngân sách hợp lệ qua budget **Lưu ý:** Trường budget_mode, nếu được chỉ định, phải giống nhau giữa các nhóm quảng cáo trong cùng chiến dịch.'),

    (r'• To set start time and run the ad group continuously, set schedule_type to SCHEDULE_FROM_NOW and specify schedule_start_time\. Do not specify schedule_end_time\. • To run the ad group between the scheduled start time and end time, set schedule_type to SCHEDULE_START_END and specify both schedule_start_time and schedule_end_time\. \*\*Lưu ý:\*\* You can only set schedule_type to SCHEDULE_FROM_NOW in any of the following scenarios: • Ở cấp chiến dịch, `budget_mode` là `BUDGET_MODE_DYNAMIC_DAILY_BUDGET` • Ở cấp nhóm quảng cáo, `budget_mode` là `BUDGET_MODE_DYNAMIC_DAILY_BUDGET`',
     '• Để đặt thời gian bắt đầu và chạy nhóm quảng cáo liên tục, hãy đặt schedule_type thành SCHEDULE_FROM_NOW và chỉ định schedule_start_time. Không chỉ định schedule_end_time. • Để chạy nhóm quảng cáo giữa thời gian bắt đầu và kết thúc đã lên lịch, hãy đặt schedule_type thành SCHEDULE_START_END và chỉ định cả schedule_start_time lẫn schedule_end_time. **Lưu ý:** Bạn chỉ có thể đặt schedule_type thành SCHEDULE_FROM_NOW trong bất kỳ trường hợp nào sau đây: • Ở cấp chiến dịch, `budget_mode` là `BUDGET_MODE_DYNAMIC_DAILY_BUDGET` • Ở cấp nhóm quảng cáo, `budget_mode` là `BUDGET_MODE_DYNAMIC_DAILY_BUDGET`'),

    (r'Disable or enabled with any of the following partners: • DoubleVerify • IAS with IAS wrapped tag • Zefr \*\*Lưu ý:\*\* When you configure both the "Track viewability with third-party partner" and "Measure brand safety with third-party partner" settings: • Nếu bạn đặt một trong hai cài đặt này là IAS, bạn phải đặt cả hai là IAS và chỉ định cùng một thẻ bọc IAS\. • Nếu bạn đặt một trong hai cài đặt này là Zefr, bạn phải đặt cả hai là Zefr\.',
     'Đã tắt hoặc đã bật với bất kỳ đối tác nào sau đây: • DoubleVerify • IAS với thẻ bọc IAS (wrapped tag) • Zefr **Lưu ý:** Khi bạn cấu hình cả hai cài đặt "Theo dõi khả năng xem với đối tác bên thứ ba" và "Đo lường an toàn thương hiệu với đối tác bên thứ ba": • Nếu bạn đặt một trong hai cài đặt này là IAS, bạn phải đặt cả hai là IAS và chỉ định cùng một thẻ bọc IAS. • Nếu bạn đặt một trong hai cài đặt này là Zefr, bạn phải đặt cả hai là Zefr.'),

    (r'Một trong các loại sau: • Set start time and run ad group continuously • Set start and end time \*\*Lưu ý:\*\* You can only choose "Set start time and run ad group continuously" in any of the following scenarios: • At the campaign level, a daily campaign budget is set\. • At the ad group level, a daily ad group budget is set\.',
     'Một trong các loại sau: • Đặt thời gian bắt đầu và chạy nhóm quảng cáo liên tục • Đặt thời gian bắt đầu và kết thúc **Lưu ý:** Bạn chỉ có thể chọn "Đặt thời gian bắt đầu và chạy nhóm quảng cáo liên tục" trong bất kỳ trường hợp nào sau đây: • Ở cấp chiến dịch, ngân sách chiến dịch hàng ngày được thiết lập. • Ở cấp nhóm quảng cáo, ngân sách nhóm quảng cáo hàng ngày được thiết lập.'),

    (r'Đã tắt hoặc đã bật with one or more of the following options: • Lemon8 • PineDrama \*\*Lưu ý:\*\*  • Using the Lemon8 subplacement \(LEMON8\) in your ad group is currently an allowlist-only feature\. Nếu bạn muốn truy cập, vui lòng liên hệ với đại diện TikTok của bạn\. • Using the PineDrama subplacement \(PINE_DRAMA\) in your ad group is currently an allowlist-only feature\. Nếu bạn muốn truy cập, vui lòng liên hệ với đại diện TikTok của bạn\.',
     'Đã tắt hoặc đã bật với một hoặc nhiều tùy chọn sau: • Lemon8 • PineDrama **Lưu ý:** • Việc sử dụng vị trí phụ Lemon8 (LEMON8) trong nhóm quảng cáo của bạn hiện là tính năng chỉ dành cho danh sách cho phép (allowlist). Nếu bạn muốn truy cập, vui lòng liên hệ với đại diện TikTok của bạn. • Việc sử dụng vị trí phụ PineDrama (PINE_DRAMA) trong nhóm quảng cáo của bạn hiện là tính năng chỉ dành cho danh sách cho phép (allowlist). Nếu bạn muốn truy cập, vui lòng liên hệ với đại diện TikTok của bạn.'),

    (r'location_ids or zipcode_ids or both', 'location_ids hoặc zipcode_ids hoặc cả hai'),

    (r'Một trong các tùy chọn sau: • Dynamic • Standard \*\*Lưu ý:\*\* When you use a Spark Ads identity, you can only use dynamic call to action\.',
     'Một trong các tùy chọn sau: • Động (Dynamic) • Tiêu chuẩn (Standard) **Lưu ý:** Khi sử dụng danh tính Spark Ads, bạn chỉ có thể sử dụng lời kêu gọi hành động động.'),

    (r'Bật hoặc tắt \(Enabled hoặc Disabled\) \*\*Lưu ý:\*\* When at the campaign level Realtime API is enabled, this setting is not supported\.',
     'Bật hoặc tắt (Enabled hoặc Disabled) **Lưu ý:** Khi Realtime API được bật ở cấp chiến dịch, cài đặt này không được hỗ trợ.'),

    (r'Specify valid values or not specified \*\*Lưu ý:\*\* When at the campaign level rta_id is specified, this setting is not supported\.',
     'Chỉ định các giá trị hợp lệ hoặc không chỉ định **Lưu ý:** Khi rta_id được chỉ định ở cấp chiến dịch, cài đặt này không được hỗ trợ.'),

    (r'Một trong các giá trị sau: • CUSTOMIZED_USER • AUTH_CODE • TT_USER • BC_AUTH_TT \*\*Lưu ý:\*\* • For non-Spark Ads identities \(CUSTOMIZED_USER\), specify values to identity_type and identity_id in the ad_configuration object\. • For Spark Ads identities, specify values to identity_type and identity_id within the creative_info object\.',
     'Một trong các giá trị sau: • CUSTOMIZED_USER • AUTH_CODE • TT_USER • BC_AUTH_TT **Lưu ý:** • Đối với danh tính không phải Spark Ads (CUSTOMIZED_USER), hãy chỉ định giá trị cho identity_type và identity_id trong đối tượng ad_configuration. • Đối với danh tính Spark Ads, hãy chỉ định giá trị cho identity_type và identity_id trong đối tượng creative_info.'),
]

cur_lines = list(lines)
for pat, rep in RULES:
    cur_lines = [re.sub(pat, rep, l) for l in cur_lines]

def count_en(l):
    s = re.sub(r'\`[^\`]+\`', '', l)
    s = re.sub(r'\]\([^\)]+\)', ']', s)
    s = re.sub(r'\b[Aa]n\s+toàn\b', '', s)
    s = re.sub(r'\b[Ll]ý\s+do\b', '', s)
    s = re.sub(r'\b[Dd]o\s+(?:đó|vậy)\b', '', s)
    s = re.sub(r'\b[Ss]o\s+với\b', '', s)
    en_word_re = re.compile(r'\b(the|to|in|of|and|is|you|for|can|with|on|this|that|be|are|by|an|as|or|from|will|must|use|see|refer|note|set|when|if|not|only|all|have|has|do|does|at|under|into|before|after|between|each|other|more|such|any|which|about)\b', re.IGNORECASE)
    return len(en_word_re.findall(s))

rem = [l for l in cur_lines if count_en(l) >= 2]
print(f'Before: {len(lines)}')
print(f'After just 11 rules: {len(rem)} remaining')
