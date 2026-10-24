#!/usr/bin/env python3
"""
Mở rộng biên dịch chi tiết cho toàn bộ các mẫu câu, bảng tham số và cài đặt trong u102.
"""

import re
import os

MORE_REPLACEMENTS = [
    # Request / Response đơn lẻ
    (r'(?m)^Request$', 'Yêu cầu (Request)'),
    (r'(?m)^Response$', 'Phản hồi (Response)'),
    (r'(?m)^\*\*Example\*\*$', '**Ví dụ mẫu (Example)**'),
    (r'(?m)^\*\*Request\*\*$', '**Yêu cầu (Request)**'),
    (r'(?m)^\*\*Response\*\*$', '**Phản hồi (Response)**'),
    (r'(?m)^# Request Header$', '## Tiêu đề yêu cầu (Request Header)'),
    (r'(?m)^\*\*Request Header\*\*$', '**Tiêu đề yêu cầu (Request Header)**'),
    (r'(?m)^\*\*Header\*\*$', '**Tiêu đề (Header)**'),
    (r'(?m)^\*\*Parameters\*\*$', '**Danh sách tham số (Parameters)**'),

    # Header bảng targeting
    (r'Targeting optimization modeAvailable targeting settingRequirementParameterHow to configure the parameter',
     '| Chế độ tối ưu hóa nhắm mục tiêu | Cài đặt mục tiêu có sẵn | Yêu cầu (Requirement) | Tham số (Parameter) | Hướng dẫn cấu hình tham số |\n|---|---|---|---|---|'),

    # Nhắm mục tiêu nhân khẩu học (Demographics)
    (r'Demographics · LocationThe location should match the targeting countries\/regions of the catalog\.locationSpecify valid values\.',
     '| Nhân khẩu học · Địa điểm (Location) | Địa điểm phải khớp với quốc gia/khu vực nhắm mục tiêu của danh mục sản phẩm | `location` | Chỉ định các giá trị hợp lệ. |'),
    (r'Demographics · LocationThe location should match the targeting countries\/regions of the catalog\.locationSpecify a valid value\.',
     '| Nhân khẩu học · Địa điểm (Location) | Địa điểm phải khớp với quốc gia/khu vực nhắm mục tiêu của danh mục sản phẩm | `location` | Chỉ định một giá trị hợp lệ. |'),
    (r'Demographics · LocationThe location should match the targeting countries\/regions of the app or website\.locationSpecify valid values\.',
     '| Nhân khẩu học · Địa điểm (Location) | Địa điểm phải khớp với quốc gia/khu vực nhắm mục tiêu của ứng dụng hoặc trang web | `location` | Chỉ định các giá trị hợp lệ. |'),
    (r'Demographics · Age \*\((Không bắt buộc|Optional)\)\*Enabled or disabledage_groupsSpecify valid values or not specified',
     '| Nhân khẩu học · Độ tuổi *(Không bắt buộc)* | Bật hoặc tắt | `age_groups` | Chỉ định các giá trị hợp lệ hoặc không chỉ định |'),
    (r'Demographics · Gender \*\((Không bắt buộc|Optional)\)\*Enabled or disabledgenderSpecify valid values or not specified',
     '| Nhân khẩu học · Giới tính *(Không bắt buộc)* | Bật hoặc tắt | `gender` | Chỉ định giá trị hợp lệ hoặc không chỉ định |'),
    (r'Demographics · Languages \*\((Không bắt buộc|Optional)\)\*Enabled or disabledlanguagesSpecify valid values or not specified',
     '| Nhân khẩu học · Ngôn ngữ *(Không bắt buộc)* | Bật hoặc tắt | `languages` | Chỉ định các giá trị hợp lệ hoặc không chỉ định |'),

    # Đối tượng tùy chỉnh (Custom Audience)
    (r'Custom audience · Include audience \*\((Không bắt buộc|Optional)\)\*Enabled or disabledaudience_idsSpecify valid values or not specified',
     '| Đối tượng tùy chỉnh · Bao gồm đối tượng *(Không bắt buộc)* | Bật hoặc tắt | `audience_ids` | Chỉ định các giá trị hợp lệ hoặc không chỉ định |'),
    (r'Custom audience · Exclude audience \*\((Không bắt buộc|Optional)\)\*Enabled or disabledexcluded_audience_idsSpecify valid values or not specified',
     '| Đối tượng tùy chỉnh · Loại trừ đối tượng *(Không bắt buộc)* | Bật hoặc tắt | `excluded_audience_ids` | Chỉ định các giá trị hợp lệ hoặc không chỉ định |'),
    (r'Use saved audience \*\((Không bắt buộc|Optional)\)\*Enabled or disabledsaved_audience_idSpecify valid values or not specified',
     '| Sử dụng đối tượng đã lưu *(Không bắt buộc)* | Bật hoặc tắt | `saved_audience_id` | Chỉ định giá trị hợp lệ hoặc không chỉ định |'),

    # Nhắm mục tiêu chi tiết (Detailed targeting)
    (r'Detailed targeting · Spending power \*\((Không bắt buộc|Optional)\)\*Enabled or disabledspending_powerSpecify valid values or not specified',
     '| Nhắm mục tiêu chi tiết · Sức chi tiêu *(Không bắt buộc)* | Bật hoặc tắt | `spending_power` | Chỉ định giá trị hợp lệ hoặc không chỉ định |'),
    (r'Detailed targeting · Household income \*\((Không bắt buộc|Optional)\)\*Enabled or disabledhousehold_incomeSpecify valid values or not specified',
     '| Nhắm mục tiêu chi tiết · Thu nhập hộ gia đình *(Không bắt buộc)* | Bật hoặc tắt | `household_income` | Chỉ định các giá trị hợp lệ hoặc không chỉ định |'),

    # Thiết bị (Device)
    (r'Device · Operating system \*\((Không bắt buộc|Optional)\)\*Enabled or disabledoperating_systemsSpecify valid values or not specified',
     '| Thiết bị · Hệ điều hành *(Không bắt buộc)* | Bật hoặc tắt | `operating_systems` | Chỉ định các giá trị hợp lệ hoặc không chỉ định |'),
    (r'Device · OS versions \*\((Không bắt buộc|Optional)\)\*Enabled or disabledmin_android_version min_ios_versionSpecify valid values or not specified',
     '| Thiết bị · Phiên bản HĐH *(Không bắt buộc)* | Bật hoặc tắt | `min_android_version`, `min_ios_version` | Chỉ định các giá trị hợp lệ hoặc không chỉ định |'),
    (r'Device · Device model \*\((Không bắt buộc|Optional)\)\*Enabled or disableddevice_model_idsSpecify valid values or not specified',
     '| Thiết bị · Mẫu thiết bị *(Không bắt buộc)* | Bật hoặc tắt | `device_model_ids` | Chỉ định các giá trị hợp lệ hoặc không chỉ định |'),
    (r'Device · Connection type \*\((Không bắt buộc|Optional)\)\*Enabled or disablednetwork_typesSpecify valid values or not specified',
     '| Thiết bị · Loại kết nối mạng *(Không bắt buộc)* | Bật hoặc tắt | `network_types` | Chỉ định các giá trị hợp lệ hoặc không chỉ định |'),
    (r'Device · Carriers \*\((Không bắt buộc|Optional)\)\*Enabled or disabledcarrier_idsSpecify valid values or not specified',
     '| Thiết bị · Nhà mạng *(Không bắt buộc)* | Bật hoặc tắt | `carrier_ids` | Chỉ định các giá trị hợp lệ hoặc không chỉ định |'),
    (r'Device · Internet service provider \*\((Không bắt buộc|Optional)\)\*Enabled or disabledisp_idsSpecify valid values or not specified',
     '| Thiết bị · Nhà cung cấp dịch vụ Internet *(Không bắt buộc)* | Bật hoặc tắt | `isp_ids` | Chỉ định các giá trị hợp lệ hoặc không chỉ định |'),
    (r'Device · Device price \*\((Không bắt buộc|Optional)\)\*Enabled or disableddevice_price_rangesSpecify valid values or not specified',
     '| Thiết bị · Khoảng giá thiết bị *(Không bắt buộc)* | Bật hoặc tắt | `device_price_ranges` | Chỉ định các giá trị hợp lệ hoặc không chỉ định |'),

    # Ngân sách và lịch trình bảng ghép
    (r'Budget and schedule · Dayparting \*\((Không bắt buộc|Optional)\)\*Any of the following types: • All day \(default\) • Select specific timedaypartingAny of the following configurations: • Specify an all-1 value, or do not specify this field • Specify a value that contains 0 to indicate non-delivery',
     '| Ngân sách và lịch trình · Phân bổ theo khung giờ *(Không bắt buộc)* | Một trong các loại: • Cả ngày (Mặc định) • Chọn thời gian cụ thể | `dayparting` | Một trong các cấu hình: • Chuỗi toàn 1 (hoặc không chỉ định) • Chuỗi chứa ký tự 0 biểu thị không phân phối |'),

    (r'Budget and schedule · ScheduleAny of the following types: • Set start time and run ad group continuously • Set start and end time \*\*Note\*\*: You can only choose "Set start time and run ad group continuously" in any of the following scenarios: • At the campaign level, a daily campaign budget is set\. • At the ad group level, a daily ad group budget is set\.schedule_type schedule_start_time schedule_end_time• To set start time and run the ad group continuously, set schedule_type to SCHEDULE_FROM_NOW and specify schedule_start_time\. Do not specify schedule_end_time\. • To run the ad group between the scheduled start time and end time, set schedule_type to SCHEDULE_START_END and specify both schedule_start_time and schedule_end_time\.\s*\*\*Note\*\*: You can only set schedule_type to SCHEDULE_FROM_NOW in any of the following scenarios: • At the campaign level, budget_mode is BUDGET_MODE_DYNAMIC_DAILY_BUDGET • At the ad group level, budget_mode is BUDGET_MODE_DYNAMIC_DAILY_BUDGET',
     '| Ngân sách và lịch trình · Lịch trình | Một trong các loại: • Chạy liên tục từ thời điểm bắt đầu • Chạy trong khoảng thời gian xác định | `schedule_type`, `schedule_start_time`, `schedule_end_time` | • Để chạy liên tục, đặt `schedule_type` là `SCHEDULE_FROM_NOW` và truyền `schedule_start_time`. • Để chạy có thời hạn, đặt `schedule_type` là `SCHEDULE_START_END` và truyền cả `schedule_start_time` và `schedule_end_time`. |'),

    (r'Budget and schedule · Budget • When you select an ad group budget strategy: • If the ad group budget limit is No limit or Lifetime limit, you can use any of the following ad group budget modes: • Lifetime • Daily • If the ad group budget limit is Daily limit, you can use the following ad group budget mode: • Daily \*\*Note\*\*: The ad group budget mode must be the same across ad groups within the same campaign\.budget_mode budget • When budget_optimize_on is false and budget_mode is BUDGET_MODE_INFINITE or BUDGET_MODE_TOTAL at the campaign level: • Set budget_mode to BUDGET_MODE_TOTAL or BUDGET_MODE_DYNAMIC_DAILY_BUDGET • Specify a valid budget via budget • When budget_optimize_on is false and budget_mode is BUDGET_MODE_DAY at the campaign level: • Set budget_mode to BUDGET_MODE_DYNAMIC_DAILY_BUDGET • Specify a valid budget via budget \*\*Note\*\*: The budget_mode must be the same across ad groups within the same campaign\.',
     '| Ngân sách và lịch trình · Ngân sách | Khi chọn chiến lược ngân sách nhóm quảng cáo: Có thể đặt chế độ Trọn đời hoặc Hàng ngày | `budget_mode`, `budget` | Khi `budget_optimize_on` là `false` ở cấp chiến dịch, thiết lập `budget_mode` thành `BUDGET_MODE_DYNAMIC_DAILY_BUDGET` hoặc `BUDGET_MODE_TOTAL` và truyền giá trị ngân sách qua `budget`. |'),

    # Search Keywords bảng ghép
    (r'Search keywords · Keywords\*\*Specify a list of 1 to 1,000 valid search keywords\*\*keyword match_typeSpecify a list of 1 to 1,000 valid search keywords along with the corresponding match types via keyword and match_type\.\s*• To obtain recommended search keywords with predicted monthly searches, use \[\/tool\/search_keyword\/recommend\/\]\([^\)]+\)\.\s*• To discover new keywords based on your search query, use \[\/tool\/search_keyword\/keyword_idea\/\]\([^\)]+\)\.\s*• To obtain the review result for search keywords, call \[\/smart_plus\/adgroup\/get\/\]\([^\)]+\) and check the audit_status within the search_keywords object array\.',
     '| Từ khóa tìm kiếm · Từ khóa (Keywords) | **Chỉ định danh sách 1 đến 1.000 từ khóa tìm kiếm hợp lệ** | `keyword`, `match_type` | Chỉ định danh sách từ khóa hợp lệ cùng kiểu đối sánh qua `keyword` và `match_type`. Xem đề xuất qua endpoint `/tool/search_keyword/recommend/`, khám phá từ khóa qua `/tool/search_keyword/keyword_idea/`, và kiểm tra trạng thái duyệt qua `/smart_plus/adgroup/get/`. |'),

    # Tracking & Brand safety bảng ghép
    (r'Tracking · Third-party integrations · Track viewability with third-party partner \*\((Không bắt buộc|Optional)\)\*Disabled or enabledviewability_postbid_partner viewability_vast_urlSpecify valid values or not specified',
     '| Theo dõi · Tích hợp bên thứ ba · Khả năng xem *(Không bắt buộc)* | Tắt hoặc bật | `viewability_postbid_partner`, `viewability_vast_url` | Chỉ định các giá trị hợp lệ hoặc không chỉ định |'),
    (r'viewability_vast_urlSpecify a valid value when viewability_postbid_partner is IAS \*\*Note\*\*: If you specify viewability_postbid_partner, viewability_vast_url is required\.',
     '| `viewability_vast_url` | Bắt buộc chỉ định giá trị hợp lệ khi `viewability_postbid_partner` là `IAS`. | - | - |'),
    (r'Tracking · Third-party integrations · Measure brand safety with third-party partner \*\((Không bắt buộc|Optional)\)\*Disabled or enabledbrand_safety_postbid_partner brand_safety_vast_urlSpecify valid values or not specified',
     '| Theo dõi · Tích hợp bên thứ ba · An toàn thương hiệu *(Không bắt buộc)* | Tắt hoặc bật | `brand_safety_postbid_partner`, `brand_safety_vast_url` | Chỉ định các giá trị hợp lệ hoặc không chỉ định |'),
    (r'brand_safety_vast_urlSpecify a valid value when brand_safety_postbid_partner is IAS \*\*Note\*\*: If you specify brand_safety_postbid_partner, brand_safety_vast_url is required\.',
     '| `brand_safety_vast_url` | Bắt buộc chỉ định giá trị hợp lệ khi `brand_safety_postbid_partner` là `IAS`. | - | - |'),

    # Placements and brand safety · Brand safety and suitability
    (r'Placements and brand safety · Brand safety and suitabilityThese settings only apply to TikTok feeds, search results, Lemon8, and Global App Bundle\. Any previous account-level settings in the brand safety hub will apply to your campaign\.N\/AN\/A To retrieve the ad account-level brand safety and suitability settings in the brand safety hub, use \[\/tiktok_inventory_filters\/get\/\]\([^\)]+\)\.\s*To configure or update the ad account-level brand safety and suitability settings in the brand safety hub, use \[\/tiktok_inventory_filters\/update\/\]\([^\)]+\)\.',
     '| Vị trí hiển thị và an toàn thương hiệu · An toàn và mức độ phù hợp thương hiệu | Thiết lập này áp dụng cho Bảng tin TikTok, Kết quả tìm kiếm, Lemon8 và Global App Bundle. Cài đặt cấp tài khoản trong trung tâm an toàn thương hiệu sẽ được áp dụng. | N/A | N/A. Để tra cứu cài đặt an toàn thương hiệu, dùng endpoint `/tiktok_inventory_filters/get/`. Để cập nhật, dùng `/tiktok_inventory_filters/update/`. |'),

    (r'Placements and brand safety · Allow commentsEnabled or disabledcomment_disabledSpecify valid values or not specified',
     '| Cho phép bình luận | Bật hoặc tắt | `comment_disabled` | Chỉ định các giá trị hợp lệ hoặc không chỉ định |'),
    (r'Placements and brand safety · Pangle block listDisabledN\/AN\/A',
     '| Danh sách chặn Pangle | Tắt (Disabled) | N/A | N/A |'),

    # Creative assets Identity bảng ghép
    (r'Creative assets · IdentityAny of the following options: • Authorized User • TikTok User • TikTok Account • Custom Identity • Identity within the same Business Centeridentity_type identity_id identity_authorized_bc_id• To use an Authorized User, set identity_type to AUTH_CODE and specify identity_id\.\s*• To use a TikTok User, set identity_type to TT_USER and specify identity_id\.\s*• To use a TikTok Account, set identity_type to BC_AUTH_TT and specify identity_id\.\s*• To use a Custom Identity, set identity_type to CUSTOMIZED_USER and specify identity_id\.\s*• To use an Identity within the same Business Center, set identity_type to BC_AUTH_TT, specify identity_id, and specify identity_authorized_bc_id\.',
     '| Tài sản sáng tạo · Danh tính (Identity) | Một trong các tùy chọn: • Người dùng ủy quyền (Authorized User) • Người dùng TikTok (TikTok User) • Tài khoản TikTok (TikTok Account) • Danh tính tùy chỉnh (Custom Identity) • Danh tính trong Business Center | `identity_type`, `identity_id`, `identity_authorized_bc_id` | • Dùng Authorized User: đặt `identity_type` là `AUTH_CODE`, truyền `identity_id`. • Dùng TikTok User: đặt `identity_type` là `TT_USER`, truyền `identity_id`. • Dùng TikTok Account: đặt `identity_type` là `BC_AUTH_TT`, truyền `identity_id`. • Dùng Custom Identity: đặt `identity_type` là `CUSTOMIZED_USER`, truyền `identity_id`. • Dùng danh tính cùng Business Center: đặt `identity_type` là `BC_AUTH_TT`, truyền cả `identity_id` và `identity_authorized_bc_id`. |'),

    (r'Creative assets · Video thumbnail mode \(When the ad creatives include videos\)Any of the following options: • Auto • Customvideo_cover_timestamp• To use an auto-generated thumbnail, do not specify video_cover_timestamp\.\s*• To customize the video thumbnail, specify a valid value for video_cover_timestamp\.',
     '| Tài sản sáng tạo · Ảnh bìa video (Thumbnail) | Tự động hoặc tùy chỉnh | `video_cover_timestamp` | • Dùng ảnh bìa tự động: Không chỉ định `video_cover_timestamp`. • Tùy chỉnh ảnh bìa: Chỉ định mốc thời gian hợp lệ cho `video_cover_timestamp`. |'),

    # Các câu đoạn văn phổ biến về Campaign Budget Strategy
    (r'Any of the following types: • \*\*Campaign budget\*\*: Your budget will be automatically allocated and optimized across ad groups\. All ad groups must share the same budget and optimization settings\.\s*• \*\*Ad group budget\*\*: Precisely control spend for each ad group, using different budget and optimization settings for each\.',
     'Một trong các loại sau: • **Ngân sách chiến dịch (Campaign budget)**: Ngân sách sẽ được tự động phân bổ và tối ưu hóa giữa các nhóm quảng cáo. Tất cả nhóm quảng cáo phải dùng chung cài đặt ngân sách và tối ưu hóa. • **Ngân sách nhóm quảng cáo (Ad group budget)**: Kiểm soát chi tiêu chính xác cho từng nhóm quảng cáo với các cài đặt ngân sách và tối ưu hóa riêng biệt.'),
    (r'• To set a campaign budget, set this field to true or leave it unspecified\.\s*• To set an ad group budget, set this field to false\.',
     '• Để đặt ngân sách cấp chiến dịch, đặt trường này thành `true` hoặc để trống (không chỉ định). • Để đặt ngân sách cấp nhóm quảng cáo, đặt trường này thành `false`.'),
    (r'• When Campaign budget strategy is Campaign budget, specify any of the following modes: • Daily • Lifetime\s*• When Campaign budget strategy is Ad group budget, specify any of the following modes to determine the budget limit for all ad groups: • No limit • Daily • Lifetime',
     '• Khi chiến lược là Ngân sách chiến dịch: Chỉ định chế độ Hàng ngày (Daily) hoặc Trọn đời (Lifetime). • Khi chiến lược là Ngân sách nhóm: Chỉ định giới hạn cho tất cả các nhóm là Không giới hạn (No limit), Hàng ngày (Daily), hoặc Trọn đời (Lifetime).'),
    (r'• When budget_optimize_on is true or not specified, use any of the following values: • BUDGET_MODE_TOTAL • BUDGET_MODE_DYNAMIC_DAILY_BUDGET\s*• When budget_optimize_on is false, use any of the following values: • BUDGET_MODE_INFINITE • BUDGET_MODE_DAY • BUDGET_MODE_TOTAL',
     '• Khi `budget_optimize_on` là `true` hoặc không chỉ định, dùng: `BUDGET_MODE_TOTAL` hoặc `BUDGET_MODE_DYNAMIC_DAILY_BUDGET`. • Khi `budget_optimize_on` là `false`, dùng: `BUDGET_MODE_INFINITE`, `BUDGET_MODE_DAY` hoặc `BUDGET_MODE_TOTAL`.'),
    (r'• When Campaign budget strategy is Campaign budget:\s*• Specify a valid budget\.\s*• When Campaign budget strategy is Ad group budget:\s*• If the budget limit is No limit:\s*• Disabled\s*• If the budget limit is Daily or Lifetime limit:\s*• Specify a valid budget',
     '• Khi chiến lược là Ngân sách chiến dịch: Chỉ định mức ngân sách hợp lệ. • Khi chiến lược là Ngân sách nhóm: Nếu giới hạn là Không giới hạn (No limit) thì Tắt (Disabled); nếu là Hàng ngày hoặc Trọn đời thì chỉ định mức ngân sách hợp lệ.'),
    (r'• When budget_optimize_on is true or not specified:\s*• Specify a valid value\.\s*• When budget_optimize_on is false:\s*• If budget_mode is BUDGET_MODE_INFINITE:\s*• Not specified\s*• If budget_mode is BUDGET_MODE_DAY or BUDGET_MODE_TOTAL:\s*• Specify a valid value',
     '• Khi `budget_optimize_on` là `true` hoặc không chỉ định: Chỉ định một giá trị hợp lệ. • Khi `budget_optimize_on` là `false`: Nếu `budget_mode` là `BUDGET_MODE_INFINITE` thì không chỉ định; nếu là `BUDGET_MODE_DAY` hoặc `BUDGET_MODE_TOTAL` thì chỉ định giá trị hợp lệ.'),
]

def apply_more(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    parts = content.split('```')
    translated_parts = []
    for idx, part in enumerate(parts):
        if idx % 2 == 1:
            translated_parts.append(part)
        else:
            text = part
            for pat, rep in MORE_REPLACEMENTS:
                text = re.sub(pat, rep, text)
            translated_parts.append(text)

    new_content = '```'.join(translated_parts)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Applied more replacements successfully.")

if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    target = os.path.join(base_dir, 'docs/08-use-cases/use-case-tao-chien-dich-p2.md')
    apply_more(target)
