import re
import os
import sys

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(_SCRIPT_DIR)

from test_engine import new_text

TEMPLATE_RULES = [
    # Common prefixes & clauses
    (r'Any of the following types:\s*', 'Một trong các loại sau: '),
    (r'Any of the following options:\s*', 'Một trong các tùy chọn sau: '),
    (r'Any of the following values:\s*', 'Một trong các giá trị sau: '),
    (r'Any of the following configurations:\s*', 'Một trong các cấu hình sau: '),
    (r'One of the following types:\s*', 'Một trong các loại sau: '),
    (r'One of the following options:\s*', 'Một trong các tùy chọn sau: '),
    (r'One of the following values:\s*', 'Một trong các giá trị sau: '),

    (r'\bSet start time and run ad group continuously\b', 'Đặt thời gian bắt đầu và chạy nhóm quảng cáo liên tục'),
    (r'\bSet start and end time\b', 'Đặt thời gian bắt đầu và kết thúc'),
    (r'\bRun campaign continuously after the scheduled start time\b', 'Chạy chiến dịch liên tục sau thời gian bắt đầu đã lên lịch'),
    (r'\bRun campaign between the scheduled start time and end time\b', 'Chạy chiến dịch trong khoảng thời gian từ lúc bắt đầu đến lúc kết thúc theo lịch trình'),

    (r'\bTo learn about how to create\b', 'Để tìm hiểu cách tạo'),
    (r'\bTo learn more about\b', 'Để tìm hiểu thêm về'),
    (r'\bTo learn about\b', 'Để tìm hiểu về'),
    (r'\bTo find out how to\b', 'Để biết cách'),
    (r'\bTo find out\b', 'Để tìm hiểu'),
    (r'\bFor details about\b', 'Để biết chi tiết về'),
    (r'\bFor details, see\b', 'Để biết chi tiết, xem'),
    (r'\bFor more details, see\b', 'Để biết thêm chi tiết, xem'),
    (r'\bFor detailed instructions on how to create TikTok Shops, see\b', 'Để biết hướng dẫn chi tiết về cách tạo TikTok Shop, xem'),
    (r'\bFor detailed explanation of enum values, see\b', 'Để xem giải thích chi tiết về các giá trị enum, xem'),

    (r'\bTo retrieve the ad account-level brand safety and suitability settings in the brand safety hub, use\b',
     'Để truy xuất các cài đặt an toàn và phù hợp thương hiệu ở cấp tài khoản quảng cáo trong trung tâm an toàn thương hiệu, hãy sử dụng'),
    (r'\bTo retrieve the ad account-level brand safety and suitability settings in the brand safety and suitability center, use\b',
     'Để truy xuất các cài đặt an toàn và phù hợp thương hiệu ở cấp tài khoản quảng cáo trong trung tâm an toàn và phù hợp thương hiệu, hãy sử dụng'),

    (r'\bUsing the Lemon8 subplacement is an allowlist-only feature\. If you would like to access it, please contact your TikTok representative\.',
     'Sử dụng vị trí phụ Lemon8 là tính năng chỉ dành cho danh sách cho phép (allowlist-only). Nếu bạn muốn truy cập, vui lòng liên hệ với đại diện TikTok của bạn.'),
    (r'\bUsing the PineDrama subplacement is an allowlist-only feature\. If you would like to access it, please contact your TikTok representative\.',
     'Sử dụng vị trí phụ PineDrama là tính năng chỉ dành cho danh sách cho phép (allowlist-only). Nếu bạn muốn truy cập, vui lòng liên hệ với đại diện TikTok của bạn.'),

    (r'\bWhen placement_type is PLACEMENT_TYPE_NORMAL and placements includes PLACEMENT_TIKTOK:\b',
     'Khi placement_type là PLACEMENT_TYPE_NORMAL và placements bao gồm PLACEMENT_TIKTOK:'),
    (r'\bNot specified or specify one or more of the following values:\b',
     'Không chỉ định hoặc chỉ định một hoặc nhiều giá trị sau:'),
    (r'\bNot specified or specify any of the following values:\b',
     'Không chỉ định hoặc chỉ định bất kỳ giá trị nào sau đây:'),
    (r'\bSpecify valid values or not specified\b', 'Chỉ định các giá trị hợp lệ hoặc không chỉ định'),
    (r'\bSpecify a valid value or not specified\b', 'Chỉ định một giá trị hợp lệ hoặc không chỉ định'),
    (r'\bPass valid values or not passed\b', 'Truyền các giá trị hợp lệ hoặc không truyền'),
    (r'\bPass a valid value or not passed\b', 'Truyền một giá trị hợp lệ hoặc không truyền'),

    (r'\bWhen you use a daily campaign budget, you can enable or disable this setting\.\b',
     'Khi bạn sử dụng ngân sách chiến dịch hàng ngày, bạn có thể bật hoặc tắt cài đặt này.'),
    (r'\bWhen you use a lifetime campaign budget, you cannot enable this setting\.\b',
     'Khi bạn sử dụng ngân sách chiến dịch trọn đời, bạn không thể bật cài đặt này.'),

    (r'\bWhen at the campaign level Realtime API is enabled, this setting is disabled\.\b',
     'Khi Realtime API được bật ở cấp chiến dịch, cài đặt này sẽ bị tắt.'),
    (r'\bWhen at the campaign level rta_id is specified, this setting is not supported\.\b',
     'Khi rta_id được chỉ định ở cấp chiến dịch, cài đặt này không được hỗ trợ.'),
    (r'\bWhen at the campaign level rta_id is specified, you cannot specify this field\.\b',
     'Khi rta_id được chỉ định ở cấp chiến dịch, bạn không thể chỉ định trường này.'),

    (r'\bWhen you use a Spark Ads identity, you can only set this setting to Standard\.\b',
     'Khi bạn sử dụng danh tính Spark Ads, bạn chỉ có thể đặt cài đặt này thành Tiêu chuẩn (Standard).'),
    (r'\bWhen you use a Spark Ads identity, you can only use dynamic call to action\.\b',
     'Khi bạn sử dụng danh tính Spark Ads, bạn chỉ có thể sử dụng lời kêu gọi hành động động.'),

    (r'\bFor non-Spark Ads identities, specify values to identity_type and identity_id at the ad group level\.\b',
     'Đối với danh tính Non-Spark Ads, hãy chỉ định giá trị cho identity_type và identity_id ở cấp nhóm quảng cáo.'),
    (r'\bFor Spark Ads identities, specify values to identity_type and identity_id within the media_info object at the ad level\.\b',
     'Đối với danh tính Spark Ads, hãy chỉ định giá trị cho identity_type và identity_id bên trong đối tượng media_info ở cấp quảng cáo.'),

    (r'\bTo obtain a valid music ID, you can follow any of the following methods:\b',
     'Để lấy ID âm nhạc hợp lệ, bạn có thể thực hiện theo các phương thức sau:'),
    (r'\bTo obtain a valid music ID, you can use\b', 'Để lấy ID âm nhạc hợp lệ, bạn có thể sử dụng'),

    (r'\bDisplay Card\b', 'Thẻ hiển thị (Display Card)'),
    (r'\bCountdown Sticker\b', 'Nhãn đếm ngược (Countdown Sticker)'),
    (r'\bGift Code Sticker\b', 'Nhãn mã quà tặng (Gift Code Sticker)'),
    (r'\bReminder Countdown Sticker\b', 'Nhãn đếm ngược nhắc nhở (Reminder Countdown Sticker)'),
]

# Apply to new_text
t = new_text
for p, r in TEMPLATE_RULES:
    t = re.sub(p, r, t)

new_parts = t.split("```")
new_prose = "\n".join([new_parts[k] for k in range(0, len(new_parts), 2)])
en_words = re.findall(r"\b[A-Za-z]{4,}\b", new_prose)
allowed = {
    "tiktok", "curl", "post", "json", "http", "https", "true", "false", "null", "none",
    "objective_type", "campaign_type", "budget_mode", "budget", "advertiser_id", "campaign_name",
    "adgroup_name", "optimization_goal", "billing_event", "bid_type", "bid_price", "pixel_id"
}
untrans = [w for w in en_words if w.lower() not in allowed]
print(f"Untranslated words after template rules: {len(untrans)} (from 54,686)")
