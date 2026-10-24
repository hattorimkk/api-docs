#!/usr/bin/env python3
import json

with open('tiktok-business-api/_work/mapped_186.json') as f:
    M = json.load(f)

with open('tiktok-business-api/_work/exact_186_lines.json') as f:
    items = json.load(f)

lines = [it['line'] for it in items]
unmapped = [l for l in lines if l not in M]

for u in unmapped:
    if "When Campaign budget strategy is Automatic campaign budget, specify a valid" in u:
        M[u] = "• Khi Chiến lược ngân sách chiến dịch là Ngân sách chiến dịch tự động, hãy chỉ định một ngân sách hợp lệ. • Khi Chiến lược ngân sách chiến dịch là Ngân sách nhóm quảng cáo tùy chỉnh: • Đã tắt"
    elif "Optimization and bidding · Event ·· Optimization event" in u:
        M[u] = "Tối ưu hóa và đặt giá thầu · Sự kiện ·· Sự kiện tối ưu hóa"
    elif "Retarget · Custom audience · Include · Target anyone in catalog or custom audiences" in u:
        M[u] = "Nhắm mục tiêu lại · Đối tượng tùy chỉnh · Bao gồm · Nhắm mục tiêu bất kỳ ai trong danh mục hoặc đối tượng tùy chỉnh (Không bắt buộc khi chỉ định cả Đối tượng bao gồm trong danh mục và đối tượng tùy chỉnh)"
    elif "When you enable **Video templates,** select one of the following video template" in u:
        M[u] = "Khi bạn bật **Mẫu video (Video templates)**, hãy chọn một trong các cài đặt mẫu video sau: • Tất cả mẫu video và URL video • Một mẫu video cụ thể"
    elif "When TEMPLATE_VIDEO is included in the catalog_media_settings value: • To select" in u:
        M[u] = "Khi TEMPLATE_VIDEO có trong giá trị catalog_media_settings: • Để chọn tùy chọn \"Tất cả mẫu video và URL video\", hãy để trống trường này. • Để chọn một mẫu video cụ thể, hãy chỉ định một giá trị hợp lệ."
    elif "Enable \"Video\" in your catalog creative settings, allowing the system to use vid" in u:
        M[u] = "Bật \"Video\" trong cài đặt mẫu quảng cáo danh mục của bạn, cho phép hệ thống sử dụng video từ danh mục của bạn trong quảng cáo."
    elif "Ensure that a video URL (video_url) has been configured for each catalog product" in u:
        M[u] = "Đảm bảo rằng URL video (video_url) đã được định cấu hình cho mỗi sản phẩm trong danh mục. • Để đảm bảo URL video đã được định cấu hình cho từng sản phẩm trong danh mục, sử dụng [/catalog/product/get/](../12-api-reference/28-catalog-products-p2.md#doc-1740564136678402) và kiểm tra video_url được trả về. • Nếu bạn muốn thêm URL video cho các sản phẩm danh mục của mình, sử dụng [/catalog/product/update/](../12-api-reference/28-catalog-products-p2.md#doc-1740562287852546)."
    elif "The possible ad format combinations for your Upgraded Smart+ Travel Ads are illu" in u:
        M[u] = "Các kết hợp định dạng quảng cáo có thể có cho Upgraded Smart+ Travel Ads của bạn được minh họa trong bảng sau."
    elif "To ensure certain ad formats are available in Upgraded Smart+ Travel Ads, follow" in u:
        M[u] = "Để đảm bảo các định dạng quảng cáo nhất định khả dụng trong Upgraded Smart+ Travel Ads, hãy làm theo hướng dẫn trong bảng sau."
    elif "1. Create an entertainment catalog using [/catalog/create/](../12-api-reference/" in u:
        M[u] = "1. Tạo danh mục giải trí bằng [/catalog/create/](../12-api-reference/25-catalog-management.md#doc-1740306481704961)."
    elif "Specify a valid URL. Users will be directed to your product links, TikTok Instan" in u:
        M[u] = "Chỉ định một URL hợp lệ. Người dùng sẽ được chuyển hướng đến liên kết sản phẩm, Trang tức thì TikTok hoặc liên kết được chỉ định tùy thuộc vào nơi họ có nhiều khả năng chuyển đổi nhất."
    elif "The possible ad format combinations for your Upgraded Smart+ Streaming Ad are il" in u:
        M[u] = "Các kết hợp định dạng quảng cáo có thể có cho Upgraded Smart+ Streaming Ad của bạn được minh họa trong bảng sau."
    elif "To ensure certain ad formats are available in Upgraded Smart+ Streaming Ads, fol" in u:
        M[u] = "Để đảm bảo các định dạng quảng cáo nhất định khả dụng trong Upgraded Smart+ Streaming Ads, hãy làm theo hướng dẫn trong bảng sau."
    elif "Ensure that the catalog (catalog_id) contains at least four approved media title" in u:
        M[u] = "Đảm bảo rằng danh mục (catalog_id) chứa ít nhất bốn mục tiêu đề phương tiện đã được phê duyệt, mỗi mục có một URL video hợp lệ. Để biết các yêu cầu cụ thể về cài đặt Ảnh bìa, Tiêu đề và Phụ đề cho các mục tiêu đề phương tiện của bạn, xem Yêu cầu quy cách cho cài đặt Multi-Show. Bạn có thể xác minh cấu hình này bằng cách kiểm tra video_url được trả về cho các mục tiêu đề phương tiện qua endpoint [/catalog/product/get/](https://business-api.tiktok.com/portal/docs/get-products/v1.3). Phải có URL video hợp lệ cho ít nhất bốn mục tiêu đề phương tiện đã được phê duyệt."
    elif "Specify one available mini series catalog product (a mini series). • To retrieve" in u:
        M[u] = "Chỉ định một sản phẩm danh mục phim bộ ngắn khả dụng (một bộ phim). • Để truy xuất ID sản phẩm (product_id) của từng sản phẩm danh mục phim bộ ngắn, sử dụng [/catalog/product/get/](../12-api-reference/28-catalog-products-p2.md#doc-1740564136678402) và chọn một sản phẩm có audit_status là approved."

print(f"Total mapped after final 15: {len(M)} / {len(lines)}")
assert len(M) == len(lines), "All lines must be mapped!"

with open('tiktok-business-api/_work/mapped_186.json', 'w', encoding='utf-8') as f:
    json.dump(M, f, ensure_ascii=False, indent=2)

# Write out u101_exact_186.py
with open('tiktok-business-api/_scripts/u101_exact_186.py', 'w', encoding='utf-8') as f:
    f.write('''#!/usr/bin/env python3
"""
Exact 186 translations dictionary.
"""
EXACT_186_MAP = {
''')
    for k, v in M.items():
        f.write(f'    {repr(k)}:\n        {repr(v)},\n')
    f.write('}\n')

print("Generated tiktok-business-api/_scripts/u101_exact_186.py successfully!")
