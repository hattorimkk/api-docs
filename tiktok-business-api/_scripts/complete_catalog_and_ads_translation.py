#!/usr/bin/env python3
"""
Biên dịch các khối danh mục sản phẩm, sáng tạo, và lịch trình còn lại.
"""

import re
import os

REPLACEMENTS = [
    # Catalog steps
    (r'3\. Check the product handling results\.', '3. Kiểm tra kết quả xử lý sản phẩm.'),
    (r'- For CSV feed and JSON schema, use (\[\/catalog\/product\/log\/\]\([^\)]+\))\.',
     r'- Đối với nguồn cấp dữ liệu CSV và JSON schema, sử dụng \1.'),
    (r'- Pass in the `feed_log_id` obtained from Step 2\. If the field `error_affected_products` in the response is not null, examine the issue details and return to Step 2 to reupload the product\.',
     r'- Truyền `feed_log_id` lấy từ Bước 2. Nếu trường `error_affected_products` trong phản hồi khác null, hãy kiểm tra chi tiết lỗi và quay lại Bước 2 để tải lại sản phẩm.'),
    (r'- For online feed, use (\[\/catalog\/feed\/log\/\]\([^\)]+\))\.',
     r'- Đối với nguồn cấp trực tuyến (online feed), sử dụng \1.'),
    (r'- Pass in the `feed_id` obtained from Step 2\. If the field `error_count` in the response is not 0, examine your online feed and return to Step 2 to reupload the product\.',
     r'- Truyền `feed_id` lấy từ Bước 2. Nếu trường `error_count` trong phản hồi khác 0, hãy kiểm tra nguồn cấp trực tuyến của bạn và quay lại Bước 2 để tải lại sản phẩm.'),
    (r'5\. \*\((Không bắt buộc|Optional)\)\* Invite members to Business Center and grant the admin permission using (\[\/bc\/member\/invite\/\]\([^\)]+\))\.',
     r'5. *(Không bắt buộc)* Mời thành viên vào Business Center và cấp quyền quản trị viên bằng cách gọi endpoint \2.'),
    (r'6\. \*\((Không bắt buộc|Optional)\)\* Share a catalog with members and grant catalog management access using (\[\/bc\/asset\/assign\/\]\([^\)]+\))\.',
     r'6. *(Không bắt buộc)* Chia sẻ danh mục sản phẩm cho các thành viên và cấp quyền quản lý danh mục bằng cách gọi endpoint \2.'),
    (r'You can also choose `advertiser_role` that you want to assign to the members invited\.',
     'Bạn cũng có thể chọn `advertiser_role` mà bạn muốn gán cho các thành viên được mời.'),
    (r'Make sure to specify `CATALOG` in the `asset_type` field and `ADMIN` in the `catalog_role` field\.',
     'Đảm bảo chỉ định `CATALOG` trong trường `asset_type` và `ADMIN` trong trường `catalog_role`.'),
    (r'To set up the catalog:', 'Để thiết lập danh mục sản phẩm:'),

    # Creative assets Identity variations
    (r'Creative assets · IdentityAny of the following options: • Authorized User • TikTok User • TikTok Account User in Business Centeridentity_typeAny of the following values: • AUTH_CODE • TT_USER • BC_AUTH_TT \*\*Note\*\*: • For Spark Ads identities, specify values to identity_type and identity_id within the creative_info object\.',
     '| Tài sản sáng tạo · Danh tính (Identity) | Một trong các tùy chọn: • Người dùng ủy quyền (Authorized User) • Người dùng TikTok (TikTok User) • Tài khoản TikTok trong Business Center | `identity_type` | Một trong các giá trị: `AUTH_CODE`, `TT_USER`, `BC_AUTH_TT`. **Lưu ý**: Đối với danh tính Spark Ads, chỉ định giá trị cho `identity_type` và `identity_id` bên trong đối tượng `creative_info`. |'),

    # Creative list
    (r'creative_list video_info image_info music_info ad_text_list tiktok_item_idSpecify one to 50 ad creatives through creative_list\.\s*The ad creatives can be any of the following: • Videos • TikTok video posts • TikTok photo posts • Carousel To learn about configurations of the available ad creative combinations based on identity type, see (\[Ad creative combinations by identity and ad type\]\([^\)]+\))\.',
     r'| `creative_list`, `video_info`, `image_info`, `music_info`, `ad_text_list`, `tiktok_item_id` | Chỉ định từ 1 đến 50 tài liệu sáng tạo qua `creative_list` (Video, Bài đăng video TikTok, Bài đăng ảnh TikTok, Thẻ xoay vòng). Xem chi tiết tại \1. | - | - |'),

    # Audience targeting optimization mode Custom targeting
    (r'Audience targeting optimization mode\*\*Custom targeting\*\* • You can use custom targeting settings to precisely control who sees your ads\.\s*This may limit delivery and impact campaign performance\.\s*To learn about the supported targeting settings, see (\[[^\]]+\]\([^\)]+\))\.targeting_optimization_modeMANUAL To learn about the supported targeting settings, see (\[[^\]]+\]\([^\)]+\))\.',
     r'| Chế độ tối ưu hóa nhắm mục tiêu đối tượng | **Nhắm mục tiêu tùy chỉnh (Custom targeting)**: Kiểm soát chính xác đối tượng xem quảng cáo của bạn. | `targeting_optimization_mode` | `MANUAL`. Xem chi tiết cài đặt nhắm mục tiêu được hỗ trợ tại \1. |'),

    # Budget and schedule Schedule single-line variation
    (r'Budget and schedule · ScheduleAny of the following types: • Set start time and run ad group continuously • Set start and end time \*\*Note\*\*: You can only choose "Set start time and run ad group continuously" in any of the following scenarios: • At the campaign level, a daily campaign budget is set\. • At the ad group level, a daily ad group budget is set\.schedule_type schedule_start_time schedule_end_time • To set start time and run the ad group continuously, set schedule_type to SCHEDULE_FROM_NOW and specify schedule_start_time\. Do not specify schedule_end_time\. • To run the ad group between the scheduled start time and end time, set schedule_type to SCHEDULE_START_END and specify both schedule_start_time and schedule_end_time\.\s*\*\*Note\*\*: You can only set schedule_type to SCHEDULE_FROM_NOW in any of the following scenarios: • At the campaign level, budget_mode is BUDGET_MODE_DYNAMIC_DAILY_BUDGET • At the ad group level, budget_mode is BUDGET_MODE_DYNAMIC_DAILY_BUDGET',
     '| Ngân sách và lịch trình · Lịch trình | Một trong các loại: • Chạy liên tục từ thời điểm bắt đầu • Chạy trong khoảng thời gian xác định | `schedule_type`, `schedule_start_time`, `schedule_end_time` | • Để chạy liên tục: Đặt `schedule_type` là `SCHEDULE_FROM_NOW` và truyền `schedule_start_time`. • Để chạy có thời hạn: Đặt `schedule_type` là `SCHEDULE_START_END` và truyền cả `schedule_start_time` và `schedule_end_time`. |'),

    # Attribution setting
    (r'Select from the supported attribution setting options for the specific scenario\.',
     'Chọn từ các tùy chọn cài đặt phân bổ được hỗ trợ cho kịch bản cụ thể.'),
    (r'To learn about the supported attribution setting options for different scenarios, see (\[[^\]]+\]\([^\)]+\))\.',
     r'Để tìm hiểu về các tùy chọn cài đặt phân bổ được hỗ trợ cho các kịch bản khác nhau, xem \1.'),

    # Product source details Products
    (r'(?m)^Product source details · Products$', 'Chi tiết nguồn sản phẩm · Danh sách sản phẩm (Products)'),
    (r'Any of the following options: • All products • Product set • Specific products with a maximum of 20 products',
     'Một trong các tùy chọn: • Tất cả sản phẩm • Bộ sản phẩm (Product set) • Sản phẩm cụ thể (tối đa 20 sản phẩm)'),

    (r'(?m)^Product source details · Catalog$', 'Chi tiết nguồn sản phẩm · Danh mục (Catalog)'),
    (r'Specify \*\*a generic catalog with at least one approved product\*\*',
     'Chỉ định **danh mục chung có ít nhất một sản phẩm đã được phê duyệt**'),
    (r'Specify \*\*an E-commerce catalog with at least one approved product\*\*',
     'Chỉ định **danh mục Thương mại điện tử có ít nhất một sản phẩm đã được phê duyệt**'),
    (r'Specify \*\*a travel catalog with at least one approved product\*\*',
     'Chỉ định **danh mục Du lịch có ít nhất một sản phẩm đã được phê duyệt**'),
    (r'Specify \*\*a streaming catalog with at least one approved product\*\*',
     'Chỉ định **danh mục Truyền phát trực tuyến có ít nhất một sản phẩm đã được phê duyệt**'),
    (r'Specify \*\*an automotive catalog with at least one approved product\*\*',
     'Chỉ định **danh mục Ô tô có ít nhất một sản phẩm đã được phê duyệt**'),

    # Disclaimer
    (r'(?m)^Disclaimer \*\((Không bắt buộc|Optional)\)\*$', 'Tuyên bố từ chối trách nhiệm *(Không bắt buộc)*'),
    (r'(?m)^Disclaimer \(Optional\)$', 'Tuyên bố từ chối trách nhiệm *(Không bắt buộc)*'),

    # Goal-based budget increase
    (r'Budget and schedule · Goal-based budget increase \(when Bid Strategy is Target CPA\)',
     'Ngân sách và lịch trình · Tăng ngân sách theo mục tiêu (Khi chiến lược giá thầu là CPA mục tiêu)'),
    (r'Goal-based budget increase \(when Campaign budget strategy is Campaign budget and campaign budget mode is daily\)',
     'Tăng ngân sách theo mục tiêu (Khi chiến lược là Ngân sách chiến dịch và chế độ ngân sách là hàng ngày)'),
]

def run():
    path = 'tiktok-business-api/docs/08-use-cases/use-case-tao-chien-dich-p2.md'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    parts = content.split('```')
    new_parts = []
    for idx, part in enumerate(parts):
        if idx % 2 == 1:
            new_parts.append(part)
        else:
            text = part
            for pat, rep in REPLACEMENTS:
                text = re.sub(pat, rep, text)
            new_parts.append(text)

    new_content = '```'.join(new_parts)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Updated catalog and ads sections successfully.")

if __name__ == '__main__':
    run()
