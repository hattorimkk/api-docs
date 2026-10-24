#!/usr/bin/env python3
"""
Hoàn thiện biên dịch triệt để các khối văn bản, cài đặt, và giải thích trong u102.
"""

import re
import os

FINALIZE_REPLACEMENTS = [
    # Video thumbnail mode
    (r'Creative assets · Video thumbnail mode \(When the ad creatives include videos\)Any of the following options: • Smart thumbnail • Manualthumbnail_modeWhen video_info is specified, use any of the following values: • AUTOMATIC • MANUAL',
     '| Tài sản sáng tạo · Ảnh bìa video (Thumbnail) | Một trong các tùy chọn: • Ảnh bìa thông minh • Thủ công | `thumbnail_mode` | Khi `video_info` được chỉ định, dùng: `AUTOMATIC` hoặc `MANUAL` |'),

    # Bid Strategy & Target CPA
    (r'Optimization and bidding · Bid Strategy, \*\((Không bắt buộc|Optional)\)\* Target CPAAny of the following types: • \*\*Maximum Delivery\*\* • \*\*Cost Cap\*\* • For Cost Cap, you need to specify a Target CPA at the same time\.bid_type bid_price conversion_bid_price deep_bid_type roas_bidSet bid_type to BID_TYPE_CUSTOM \(Cost Cap\) or BID_TYPE_NO_BID \(Maximum Delivery\)\. Do not specify bid_price, deep_bid_type and roas_bid\. • If bid_type is BID_TYPE_CUSTOM, specify conversion_bid_price at the same time\.',
     '| Tối ưu hóa và giá thầu · Chiến lược giá thầu, *(Không bắt buộc)* CPA mục tiêu | Một trong các loại: • **Phân phối tối đa (Maximum Delivery)** • **Giới hạn chi phí (Cost Cap)** | `bid_type`, `conversion_bid_price` | Đặt `bid_type` là `BID_TYPE_CUSTOM` (Cost Cap) hoặc `BID_TYPE_NO_BID` (Maximum Delivery). Nếu chọn `BID_TYPE_CUSTOM`, bắt buộc truyền `conversion_bid_price`. |'),

    # Search Health Diagnosis
    (r'After creating the Search Ads Campaign, you can retrieve health diagnoses for your ad groups or ads within the campaign using (\[\/tool\/diagnosis\/search\/health\/\]\([^\)]+\))\.\s*It provides insights on search volume, keyword relevance, as well as bid and budget recommendations\.',
     r'Sau khi tạo Chiến dịch quảng cáo tìm kiếm, bạn có thể truy xuất chẩn đoán tình trạng sức khỏe cho các nhóm quảng cáo hoặc mẫu quảng cáo trong chiến dịch bằng cách gọi endpoint \1. Endpoint này cung cấp thông tin chi tiết về lượng tìm kiếm, mức độ liên quan của từ khóa, cũng như các khuyến nghị về giá thầu và ngân sách.'),

    # Promotion target type
    (r'promotion_target_typeNot specified', '| `promotion_target_type` | Không chỉ định (Not specified) | - | - |'),
    (r'location_ids or zipcode_ids or both', '`location_ids` hoặc `zipcode_ids` hoặc cả hai'),

    # Tracking App events
    (r'Tracking · TikTok events tracking · App events \*\((Không bắt buộc|Optional)\)\*',
     'Theo dõi · Theo dõi sự kiện TikTok · Sự kiện ứng dụng *(Không bắt buộc)*'),
    (r'Tracking · TikTok events tracking · Pixel events \*\((Không bắt buộc|Optional)\)\*',
     'Theo dõi · Theo dõi sự kiện TikTok · Sự kiện Pixel *(Không bắt buộc)*'),
    (r'Tracking · TikTok events tracking · Offline Event Tracking \*\((Không bắt buộc|Optional)\)\*',
     'Theo dõi · Theo dõi sự kiện TikTok · Theo dõi sự kiện ngoại tuyến *(Không bắt buộc)*'),

    # Định dạng ad format description
    (r'catalog carouselDisplay 2–20 products in a slideshow format\.\s*This format will showcase product images and product information \(such as product title and product price\) that are retrieved from the product catalog\.',
     'Thẻ xoay vòng danh mục (Catalog carousel): Hiển thị 2–20 sản phẩm dưới dạng trình chiếu, giới thiệu hình ảnh và thông tin sản phẩm (như tiêu đề và giá) được lấy tự động từ danh mục sản phẩm.'),
    (r'Single video: Use a video creative to promote your products\.',
     'Video đơn (Single video): Sử dụng một tài liệu video sáng tạo để quảng bá sản phẩm của bạn.'),
    (r'Catalog video: Generate a dynamic video based on information from the product catalog\.',
     'Video danh mục (Catalog video): Tự động tạo video động dựa trên thông tin từ danh mục sản phẩm.'),
    (r'Catalog carousel: Display 2–20 products in a slideshow format\.',
     'Thẻ xoay vòng danh mục (Catalog carousel): Hiển thị 2–20 sản phẩm dưới dạng trình chiếu.'),

    # Bật hoặc tắt kèm điều kiện
    (r'Bật hoặc tắt \(Enabled hoặc Disabled\) To enable this setting, the following conditions should be met: • At the campaign level: CBO is disabled\. • At the ad group level: • Ad group budget is Daily • Bid Strategy is Target CPA',
     'Bật hoặc tắt (Enabled hoặc Disabled). Để bật thiết lập này, các điều kiện sau phải được đáp ứng: • Ở cấp chiến dịch: CBO bị tắt. • Ở cấp nhóm quảng cáo: Ngân sách nhóm là Hàng ngày và Chiến lược giá thầu là CPA mục tiêu (Target CPA).'),

    # Các từ khóa đơn lẻ thường gặp trong cột yêu cầu
    (r'(?m)^Sales$', 'Doanh số (Sales)'),
    (r'(?m)^Lead generation$', 'Tìm kiếm khách hàng tiềm năng (Lead generation)'),
    (r'(?m)^Website conversions$', 'Chuyển đổi trên trang web (Website conversions)'),
    (r'(?m)^App promotion$', 'Quảng bá ứng dụng (App promotion)'),
    (r'(?m)^Traffic$', 'Lưu lượng truy cập (Traffic)'),
    (r'(?m)^Destination$', 'Điểm đến chuyển hướng (Destination)'),
    (r'(?m)^Standard \(default\)$', 'Tiêu chuẩn (Mặc định)'),
    (r'(?m)^Automatic targeting$', 'Nhắm mục tiêu tự động (Automatic targeting)'),
    (r'(?m)^Custom targeting$', 'Nhắm mục tiêu tùy chỉnh (Custom targeting)'),
    (r'(?m)^Dynamic$', 'Động (Dynamic)'),
    (r'(?m)^Standard$', 'Tiêu chuẩn (Standard)'),
    (r'(?m)^Specify a valid Pixel$', 'Chỉ định một TikTok Pixel hợp lệ'),
    (r'(?m)^Website and app$', 'Trang web và ứng dụng (Website and app)'),
    (r'(?m)^Website$', 'Trang web (Website)'),
    (r'(?m)^App$', 'Ứng dụng (App)'),
    (r'(?m)^TikTok Instant Page$', 'Trang tức thì TikTok (TikTok Instant Page)'),
    (r'(?m)^Instant Form$', 'Biểu mẫu tức thì (Instant Form)'),

    # Prerequisite sentence
    (r'Creating ([^\n]+) requires setting up a ([^\n]+) catalog in your Business Center first\.',
     r'Việc tạo \1 yêu cầu bạn phải thiết lập danh mục \2 trong Trung tâm doanh nghiệp (Business Center) trước.'),
    (r'To gain access to ([^\n]+), please contact your TikTok representative\.',
     r'Để được cấp quyền truy cập \1, vui lòng liên hệ với đại diện TikTok của bạn.'),
    (r'This feature is currently an allowlist-only feature\.\s*If you would like to access it, please contact your TikTok representative\.',
     'Tính năng này hiện chỉ dành cho danh sách cho phép (allowlist-only). Nếu bạn muốn truy cập, vui lòng liên hệ với đại diện TikTok của bạn.'),

    # Bảng format combinations
    (r'(?m)^Is the catalog carousel format available\?$', 'Định dạng thẻ xoay vòng danh mục có sẵn?'),
    (r'(?m)^Is the catalog video format available\?$', 'Định dạng video danh mục có sẵn?'),
    (r'(?m)^Is the single video format available\?$', 'Định dạng video đơn có sẵn?'),
    (r'(?m)^Is the image carousel format available\?$', 'Định dạng thẻ xoay vòng ảnh có sẵn?'),
    (r'(?m)^Catalog carousel only$', 'Chỉ thẻ xoay vòng danh mục'),
    (r'(?m)^Catalog carousel and single video$', 'Thẻ xoay vòng danh mục và video đơn'),
    (r'(?m)^Catalog carousel and catalog video$', 'Thẻ xoay vòng danh mục và video danh mục'),
    (r'(?m)^Catalog carousel, catalog video, and single video$', 'Thẻ xoay vòng danh mục, video danh mục và video đơn'),

    # Shopping Ads retargeting
    (r'\|Shopping Ads Retargeting Type\|Description\|Settings for other fields\|',
     '| Loại nhắm lại mục tiêu (Retargeting Type) | Mô tả chi tiết | Cài đặt cho các trường khác |'),
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
            for pat, rep in FINALIZE_REPLACEMENTS:
                text = re.sub(pat, rep, text)
            new_parts.append(text)

    new_content = '```'.join(new_parts)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Finalized replacements successfully.")

if __name__ == '__main__':
    run()
