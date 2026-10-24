#!/usr/bin/env python3
"""
Bộ biên dịch toàn diện u102: Áp dụng tất cả nhãn UI, mệnh đề lặp lại, định dạng bảng và các cụm từ tiếng Anh.
"""

import re, os, json, sys

sys.path.insert(0, os.path.abspath('tiktok-business-api/_scripts'))
sys.path.insert(0, os.path.abspath('tiktok-business-api/_work'))

from u102_dict_ui_labels import UI_LABELS_RULES
from u102_dict_core_clauses import CORE_CLAUSES_RULES
from u102_dict_clauses2 import CLAUSES2_RULES
from u102_batch_translator import BATCH_A_RULES

PHRASE_RULES = [
    # Top phrases from embedded phrases analysis
    (r'For detailed configuration options and requirements, see Customize the ad format combinations in ([^\n\.]+)\.',
     r'Để biết các tùy chọn cấu hình chi tiết và yêu cầu, xem Tùy chỉnh kết hợp định dạng quảng cáo trong \1.'),
    (r'For detailed configuration options and requirements, see Customize the ad format combinations in ([^\n\.]+)',
     r'Để biết các tùy chọn cấu hình chi tiết và yêu cầu, xem Tùy chỉnh kết hợp định dạng quảng cáo trong \1'),
    (r'To learn about the supported targeting settings for each mode, see \[Cài đặt nhắm mục tiêu có sẵns for different targeting optimization modes in ([^\]]+)\]\(([^\)]+)\)\.',
     r'Để tìm hiểu các cài đặt nhắm mục tiêu được hỗ trợ cho từng chế độ, xem [Cài đặt nhắm mục tiêu có sẵn cho các chế độ tối ưu hóa nhắm mục tiêu khác nhau trong \1](\2).'),
    (r'To learn about the supported targeting settings for each mode, see \[Cài đặt nhắm mục tiêu có sẵns for different targeting optimization modes\]\(([^\)]+)\)\.',
     r'Để tìm hiểu các cài đặt nhắm mục tiêu được hỗ trợ cho từng chế độ, xem [Cài đặt nhắm mục tiêu có sẵn cho các chế độ tối ưu hóa nhắm mục tiêu khác nhau](\1).'),
    (r'To learn about the supported targeting settings for each mode, see \[Available targeting settings for different targeting optimization modes\]\(([^\)]+)\)\.',
     r'Để tìm hiểu các cài đặt nhắm mục tiêu được hỗ trợ cho từng chế độ, xem [Cài đặt nhắm mục tiêu có sẵn cho các chế độ tối ưu hóa nhắm mục tiêu khác nhau](\1).'),
    (r'see Customize the ad format combinations in ([^\n\.]+)',
     r'xem Tùy chỉnh kết hợp định dạng quảng cáo trong \1'),
    (r'see Create an Upgraded Smart\+ ([^\n\.]+)',
     r'xem Tạo chiến dịch Upgraded Smart+ \1'),
    (r'see Create Upgraded Smart\+ ([^\n\.]+)',
     r'xem Tạo chiến dịch Upgraded Smart+ \1'),

    # Targeting modes in text
    (r'• \*\*Automatic targeting\*\*', '• **Nhắm mục tiêu tự động (Automatic targeting)**'),
    (r'• Automatic targeting\b', '• Nhắm mục tiêu tự động (Automatic targeting)'),
    (r'• \*\*Custom targeting\*\*', '• **Nhắm mục tiêu tùy chỉnh (Custom targeting)**'),
    (r'• Custom targeting\b', '• Nhắm mục tiêu tùy chỉnh (Custom targeting)'),
    (r'Custom targeting \(targeting_optimization_mode as MANUAL\)', 'Nhắm mục tiêu tùy chỉnh (targeting_optimization_mode là MANUAL)'),
    (r'Automatic targeting \(targeting_optimization_mode as AUTOMATIC or not specified\)', 'Nhắm mục tiêu tự động (targeting_optimization_mode là AUTOMATIC hoặc không chỉ định)'),

    # Automotive and catalogs
    (r'Auto-Model catalog', 'danh mục Mẫu xe ô tô (Auto-Model catalog)'),
    (r'Auto-Inventory catalog', 'danh mục Kho xe ô tô (Auto-Inventory catalog)'),
    (r'Before using any type of disclaimer, ensure that you have specified the necessary disclaimer details for each vehicle in the Auto-Model catalog\.',
     'Trước khi sử dụng bất kỳ loại tuyên bố từ chối trách nhiệm nào, hãy đảm bảo rằng bạn đã chỉ định các chi tiết tuyên bố từ chối trách nhiệm cần thiết cho từng mẫu xe trong danh mục Auto-Model.'),
    (r'emission disclaimer', 'tuyên bố từ chối trách nhiệm về khí thải (emission disclaimer)'),
    (r'offer disclaimer', 'tuyên bố từ chối trách nhiệm về ưu đãi (offer disclaimer)'),
    (r'Countdown Sticker or Gift Code Sticker portfolio, see \[Stickers\]\(([^\)]+)\)\.',
     r'danh mục Nhãn dán đếm ngược hoặc Nhãn dán mã quà tặng, xem [Nhãn dán (Stickers)](\1).'),
    (r'To learn about how to obtain the ID of a Countdown Sticker or Gift Code Sticker portfolio, see \[Stickers\]\(([^\)]+)\)\.',
     r'Để tìm hiểu cách lấy ID của danh mục Nhãn dán đếm ngược hoặc Nhãn dán mã quà tặng, xem [Nhãn dán (Stickers)](\1).'),

    # Search Ads availability
    (r'To learn about the available locations by objective, see \[Search Ads Campaign Availability\]\(([^\)]+)\)\.',
     r'Để tìm hiểu các vị trí khả dụng theo từng mục tiêu, xem [Khả dụng của Chiến dịch quảng cáo tìm kiếm](\1).'),
    (r'Travel Search Ads Campaigns for App', 'Chiến dịch quảng cáo tìm kiếm du lịch cho Ứng dụng'),
    (r'Streaming Search Ads Campaigns for App', 'Chiến dịch quảng cáo tìm kiếm truyền phát trực tuyến cho Ứng dụng'),
    (r'Catalog Search Ads Campaigns for Website and App', 'Chiến dịch quảng cáo tìm kiếm danh mục cho cả Trang web và Ứng dụng'),
    (r'Web Generic Catalog Ads', 'Quảng cáo danh mục chung trên web (Web Generic Catalog Ads)'),
    (r'Lead Generic Catalog Ads', 'Quảng cáo danh mục chung tìm kiếm khách hàng tiềm năng (Lead Generic Catalog Ads)'),
    (r'Automotive Search Ads', 'Quảng cáo tìm kiếm ô tô (Automotive Search Ads)'),

    # File attributes
    (r'File Type:\s*JPG,\s*JPEG,\s*PNG', 'Loại tệp: JPG, JPEG, PNG'),
    (r'File Size:\s*100\s*MB or less', 'Kích thước tệp: 100 MB trở xuống'),
    (r'File Size:\s*(\d+)\s*MB or less', r'Kích thước tệp: \1 MB trở xuống'),
    (r'The value of the parameter is_carousel_usable returned from (\[\/file\/image\/ad\/search\/\]\([^\)]+\)) for the image is true',
     r'Giá trị của tham số `is_carousel_usable` trả về từ \1 cho hình ảnh phải là `true`'),

    # Video templates & catalog creatives
    (r'To ensure that at least one video template\s+is bound to your catalog',
     'Để đảm bảo có ít nhất một mẫu video được liên kết với danh mục của bạn'),
    (r'To retrieve video templates for your catalog via (\[\/catalog\/video_template\/get\/\]\([^\)]+\))\.',
     r'Để lấy các mẫu video cho danh mục của bạn qua \1.'),
    (r'the system will automatically select one of your video templates for each catalog product to generate the corresponding catalog video',
     'hệ thống sẽ tự động chọn một trong các mẫu video của bạn cho từng sản phẩm trong danh mục để tạo video danh mục tương ứng'),
    (r'By using interactive add-ons, your ad will no longer display product cards',
     'Khi sử dụng tiện ích bổ sung tương tác, quảng cáo của bạn sẽ không còn hiển thị thẻ sản phẩm'),

    # Welcome messages & messaging apps
    (r'To obtain a list of welcome messages within your ad account, use (\[\/creative\/welcome_message\/get\/\]\([^\)]+\))\.',
     r'Để lấy danh sách tin nhắn chào mừng trong tài khoản quảng cáo của bạn, sử dụng \1.'),
    (r'match any existing message event set', 'khớp với bất kỳ bộ sự kiện tin nhắn hiện có nào'),
    (r'To learn about event set types and tracking message event set options for different scenarios, see \[Events - Message Event Set\]\(([^\)]+)\)\.',
     r'Để tìm hiểu về các loại bộ sự kiện và tùy chọn theo dõi bộ sự kiện tin nhắn cho các trường hợp khác nhau, xem [Sự kiện - Bộ sự kiện tin nhắn](\1).'),
    (r'needs to match the same instant messaging app information at the ad group level\.',
     'cần khớp với cùng thông tin ứng dụng nhắn tin tức thì ở cấp nhóm quảng cáo.'),
    (r'and check the returned messaging_app_type and messaging_app_account_id\.',
     'và kiểm tra `messaging_app_type` cùng `messaging_app_account_id` được trả về.'),

    # Identity & Spark Ads
    (r'When using a non-Spark Ad identity:', 'Khi sử dụng danh tính không phải Spark Ads:'),
    (r'When using a Spark Ad identity:', 'Khi sử dụng danh tính Spark Ads:'),
    (r'Spark Ad identity', 'danh tính Spark Ads'),
    (r'Spark Ads Pull', 'Spark Ads Pull (Kéo bài viết)'),
    (r'Spark Ads Push', 'Spark Ads Push (Đẩy bài viết)'),
    (r'Custom User \(custom identity\)', 'Người dùng tùy chỉnh (danh tính tùy chỉnh)'),

    # Call to action & end cards
    (r'To get the enum values, see \[Enumerations - Call-to-action\]\(([^\)]+)\)\.',
     r'Để lấy các giá trị enum, xem [Enum - Lời kêu gọi hành động](\1).'),
    (r'Truyền một hình ảnh thẻ kết thúc hợp lệ để sử dụng trong Quảng cáo xoay vòng danh mục ô tô qua image_info\.',
     'Truyền một hình ảnh thẻ kết thúc hợp lệ để sử dụng trong Quảng cáo xoay vòng danh mục ô tô qua `image_info`.'),

    # Creative lists & formats
    (r'For a single ad, you can include one to \*\*50 ad creatives\*\*\s*that can consist of the following types:\s*• Videos\s*• TikTok video posts\s*• TikTok photo posts\s*• Carousel\s*To learn about the combination of available ad creatives based on identity type, see \[Mẫu quảng cáo combinations by identity and ad type\]\(([^\)]+)\)\.',
     r'Đối với một quảng cáo đơn lẻ, bạn có thể bao gồm từ 1 đến **50 mẫu quảng cáo**, bao gồm các loại sau: • Video • Bài viết video TikTok • Bài viết ảnh TikTok • Thẻ xoay vòng (Carousel). Để tìm hiểu sự kết hợp của các mẫu quảng cáo khả dụng dựa trên loại danh tính, xem [Tổ hợp mẫu quảng cáo theo danh tính và loại quảng cáo](\1).'),
    (r'For a single ad, you can include one to \*\*50 ad creatives\*\*\s*that can consist of the following types:\s*• Videos\s*• TikTok video posts\s*• TikTok photo posts\s*• Carousel\s*To learn about configurations of the available ad creative combinations based on identity type, see \[Mẫu quảng cáo combinations by identity and ad type\]\(([^\)]+)\)\.',
     r'Đối với một quảng cáo đơn lẻ, bạn có thể bao gồm từ 1 đến **50 mẫu quảng cáo**, bao gồm các loại sau: • Video • Bài viết video TikTok • Bài viết ảnh TikTok • Thẻ xoay vòng (Carousel). Để tìm hiểu cấu hình các tổ hợp mẫu quảng cáo khả dụng dựa trên loại danh tính, xem [Tổ hợp mẫu quảng cáo theo danh tính và loại quảng cáo](\1).'),
    (r'Specify one to 50 ad creatives through creative_list\. Mẫu quảng cáo có thể là bất kỳ loại nào sau đây:\s*• Videos\s*• TikTok video posts\s*• TikTok photo posts\s*• Carousel\s*To learn about configurations of the available ad creative combinations based on identity type, see \[Mẫu quảng cáo combinations by identity and ad type\]\(([^\)]+)\)\.',
     r'Chỉ định từ 1 đến 50 mẫu quảng cáo qua `creative_list`. Mẫu quảng cáo có thể là bất kỳ loại nào sau đây: • Video • Bài viết video TikTok • Bài viết ảnh TikTok • Thẻ xoay vòng (Carousel). Để tìm hiểu cấu hình các tổ hợp mẫu quảng cáo khả dụng dựa trên loại danh tính, xem [Tổ hợp mẫu quảng cáo theo danh tính và loại quảng cáo](\1).'),

    # Auto selection rules
    (r'• When the "Autoselect from catalog" setting is enabled:\s*• Tắt hoặc bật \(Disabled hoặc Enabled\) with up to four products',
     '• Khi cài đặt "Tự động chọn từ danh mục" được bật: • Tắt hoặc bật với tối đa bốn sản phẩm'),
    (r'• Khi cài đặt "Tự động chọn từ danh mục" được bật:\s*• Tắt hoặc bật \(Disabled hoặc Enabled\) with up to two products',
     '• Khi cài đặt "Tự động chọn từ danh mục" được bật: • Tắt hoặc bật với tối đa hai sản phẩm'),
    (r'• Khi cài đặt "Tự động chọn từ danh mục" được bật:\s*• Tắt hoặc bật \(Disabled hoặc Enabled\) with up to four products',
     '• Khi cài đặt "Tự động chọn từ danh mục" được bật: • Tắt hoặc bật với tối đa bốn sản phẩm'),

    # General phrases
    (r'\bBy default\b', 'Theo mặc định'),
    (r'\bFor example\b', 'Ví dụ'),
    (r'Sale price', 'Giá ưu đãi (Sale price)'),
    (r'Custom label', 'Nhãn tùy chỉnh (Custom label)'),
    (r'All products', 'Tất cả sản phẩm'),
    (r'Universal Link or Android App Link starting with http:\/\/ or https:\/\/', 'Universal Link hoặc Android App Link bắt đầu bằng http:// hoặc https://'),
    (r'Apple’s universal link or Android App Link starting with http:\/\/ or https:\/\/', 'Universal Link của Apple hoặc Android App Link bắt đầu bằng http:// hoặc https://'),

    # Specific squished rows
    (r'Danh tính · Chọn tài khoản TikTokSelect a valid TikTok accountidentity_typeMột trong các giá trị sau',
     '| Danh tính · Chọn tài khoản TikTok | Chọn một tài khoản TikTok hợp lệ | `identity_type` | Một trong các giá trị sau'),
    (r'Ngân sách và lịch trình · Lịch trìnhMột trong các loại sau:',
     '| Ngân sách và lịch trình · Lịch trình | Một trong các loại sau:'),
]

MASTER_RULES = UI_LABELS_RULES + CORE_CLAUSES_RULES + CLAUSES2_RULES + BATCH_A_RULES + PHRASE_RULES

def run():
    target = 'tiktok-business-api/docs/08-use-cases/use-case-tao-chien-dich-p2.md'
    with open(target, 'r', encoding='utf-8') as f:
        content = f.read()

    parts = content.split('```')
    new_parts = []
    for idx, part in enumerate(parts):
        if idx % 2 == 1:
            new_parts.append(part)
        else:
            text = part
            for pat, rep in MASTER_RULES:
                try:
                    text = re.sub(pat, rep, text)
                except Exception:
                    pass
            new_parts.append(text)

    output = '```'.join(new_parts)
    with open(target, 'w', encoding='utf-8') as f:
        f.write(output)

    print(f"Applied {len(MASTER_RULES)} master rules to {target} successfully.")

if __name__ == '__main__':
    run()
