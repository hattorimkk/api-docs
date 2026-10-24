#!/usr/bin/env python3
"""
Common residual translations across u101 docs:
- Table headers and setting names
- Reusable bullet clauses and descriptions
- Status tags and format labels
"""

COMMON_RESIDUAL_RULES = [
    # Table headers & labels (carefully bounded by pipes or line edges so col 1 params are never broken)
    (r"\|\s*Requirement\s*\|", "| Yêu cầu (Requirement) |"),
    (r"\|\s*Setting\s*\|", "| Cài đặt (Setting) |"),
    (r"\|\s*Parameters?\s*\|", "| Tham số (Parameters) |"),
    (r"\|\s*Products?\s*\|", "| Sản phẩm (Products) |"),
    (r"\|\s*Placement\s*\|", "| Vị trí vị trí quảng cáo (Placement) |"),
    (r"\|\s*Bid Strategy\s*\|", "| Chiến lược giá thầu (Bid Strategy) |"),
    (r"\|\s*Delivery Type\s*\|", "| Loại phân phối (Delivery Type) |"),
    (r"\|\s*Schedule type\s*\|", "| Loại lịch trình (Schedule type) |"),
    (r"\|\s*Catalog type\s*\|", "| Loại danh mục (Catalog type) |"),
    (r"\|\s*Contextual Targeting\s*\|", "| Nhắm mục tiêu ngữ cảnh (Contextual Targeting) |"),
    (r"\|\s*Frequency cap\s*\|", "| Giới hạn tần suất (Frequency cap) |"),
    (r"\|\s*Ad text\s*\|", "| Văn bản quảng cáo (Ad text) |"),
    (r"\|\s*Custom link\s*\|", "| Liên kết tùy chỉnh (Custom link) |"),
    (r"\|\s*Custom deeplink\s*\|", "| Deeplink tùy chỉnh (Custom deeplink) |"),
    (r"\|\s*Product sales\s*\|", "| Doanh số sản phẩm (Product sales) |"),
    (r"\|\s*Website conversions\s*\|", "| Lượt chuyển đổi trên trang web (Website conversions) |"),
    (r"\|\s*Sales\s*\|", "| Doanh số (Sales) |"),
    (r"\|\s*Lead generation\s*\|", "| Tìm kiếm khách hàng tiềm năng (Lead generation) |"),
    (r"\|\s*App promotion\s*\|", "| Quảng bá ứng dụng (App promotion) |"),
    (r"\|\s*Video sharing\s*\|", "| Chia sẻ video (Video sharing) |"),
    (r"\|\s*Dynamic\s*\|", "| Động (Dynamic) |"),
    (r"\|\s*Dynamic daily budget\s*\|", "| Ngân sách hàng ngày động (Dynamic daily budget) |"),
    (r"\|\s*Smart Creative\s*\|", "| Mẫu quảng cáo thông minh (Smart Creative) |"),
    (r"\|\s*Single [Vv]ideo\s*\|", "| Video đơn (Single video) |"),
    (r"\|\s*Catalog Carousel\s*\|", "| Băng chuyền danh mục (Catalog Carousel) |"),
    (r"\|\s*Catalog carousel only\s*\|", "| Chỉ băng chuyền danh mục |"),
    (r"\|\s*Single video only\s*\|", "| Chỉ video đơn |"),
    (r"\|\s*Catalog video only\s*\|", "| Chỉ video danh mục |"),
    (r"\|\s*Ad creative - images\s*\|", "| Mẫu quảng cáo - hình ảnh (Ad creative - images) |"),
    (r"\|\s*Ad creative - Music\s*\|", "| Mẫu quảng cáo - Âm nhạc (Ad creative - Music) |"),
    (r"\|\s*Ad creative - Video\s*\|", "| Mẫu quảng cáo - Video (Ad creative - Video) |"),
    (r"\|\s*Ad creative - Text\s*\|", "| Mẫu quảng cáo - Văn bản (Ad creative - Text) |"),
    (r"\|\s*End card\s*\|", "| Thẻ kết thúc (End card) |"),
    (r"\|\s*Product link\s*\|", "| Liên kết sản phẩm (Product link) |"),
    (r"\|\s*Website URL\s*\|", "| URL trang web (Website URL) |"),
    (r"\|\s*Brand safety\s*\|", "| An toàn thương hiệu (Brand safety) |"),
    (r"\|\s*Specific series\s*\|", "| Phim bộ cụ thể (Specific series) |"),
    (r"\|\s*Conversations \(CONVERSATION\)\s*\|", "| Cuộc trò chuyện (CONVERSATION) |"),
    (r"\|\s*Click \(CLICK\)\s*\|", "| Lượt nhấp (CLICK) |"),
    (r"\|\s*Demographics · Location\s*\|", "| Nhân khẩu học · Vị trí (Demographics · Location) |"),
    (r"\|\s*Tracking\s*\|", "| Theo dõi (Tracking) |"),
    (r"\|\s*Identity Type\s*\|", "| Loại danh tính (Identity Type) |"),
    (r"\|\s*Ad Type\s*\|", "| Loại quảng cáo (Ad Type) |"),
    (r"\|\s*Available creative combination\s*\|", "| Kết hợp mẫu quảng cáo khả dụng (Available creative combination) |"),
    (r"\|\s*Details\s*\|", "| Chi tiết (Details) |"),
    (r"\|\s*Configurations\s*\|", "| Cấu hình (Configurations) |"),
    (r"\|\s*Ad format description\s*\|", "| Mô tả định dạng quảng cáo (Ad format description) |"),
    
    # Ad format bold text
    (r"\*\*Ad format\*\*", "**Định dạng quảng cáo (Ad format)**"),
    (r"\*\*Ad format description\*\*", "**Mô tả định dạng quảng cáo (Ad format description)**"),
    (r"\*\*Disabled\*\*", "**Đã tắt (Disabled)**"),
    (r"\*\*Enabled\*\*", "**Đã bật (Enabled)**"),
    (r"Disabled or enabled", "Đã tắt hoặc đã bật"),
    
    # Headings
    (r"^# 1\. Create a campaign\b", "## 1. Tạo chiến dịch (Create a campaign)"),
    (r"^# 4\. Create an ad\b", "## 4. Tạo quảng cáo (Create an ad)"),
    (r"^# 5\. Preview an ad\b", "## 5. Xem trước quảng cáo (Preview an ad)"),
    (r"^# Next steps\b", "## Các bước tiếp theo (Next steps)"),
    
    # Links & references
    (r"For all catalog APIs, see \[here\]\(\.\./09-marketing-api/catalog\.md#doc-1739578477445121\)\.",
     "Để biết tất cả các API danh mục, xem [tại đây](../09-marketing-api/catalog.md#doc-1739578477445121)."),
     
    # Country table rows
    (r"\|\s*`PH`\s*\|\s*the Philippines\s*\|", "| `PH` | Philippines |"),
    (r"\|\s*`VN`\s*\|\s*Vietnam\s*\|", "| `VN` | Việt Nam |"),
    (r"\|\s*`ID`\s*\|\s*Indonesia\s*\|", "| `ID` | Indonesia |"),
    (r"\|\s*`MY`\s*\|\s*Malaysia\s*\|", "| `MY` | Malaysia |"),
    (r"\|\s*`SG`\s*\|\s*Singapore\s*\|", "| `SG` | Singapore |"),
    (r"\|\s*`TH`\s*\|\s*Thailand\s*\|", "| `TH` | Thái Lan |"),
    (r"\|\s*`US`\s*\|\s*the United States\s*\|", "| `US` | Hoa Kỳ |"),
    
    # Targeting bullets
    (r"Audience targeting • Saved audience", "Nhắm mục tiêu đối tượng • Đối tượng đã lưu (Saved audience)"),
    (r"Audience targeting • Retarget audience", "Nhắm mục tiêu đối tượng • Đối tượng nhắm mục tiêu lại (Retarget audience)"),
    (r"Audience targeting • Demographics - Spending power", "Nhắm mục tiêu đối tượng • Nhân khẩu học - Khả năng chi tiêu (Spending power)"),
    (r"Audience targeting • Interests & Behaviors - Purchase intention", "Nhắm mục tiêu đối tượng • Mối quan tâm & Hành vi - Ý định mua hàng (Purchase intention)"),
    
    # Clauses
    (r"Specify a valid value\. If a catalog is specified, the location should match or be the subset of the targeting location of your catalog\.",
     "Chỉ định giá trị hợp lệ. Nếu danh mục được chỉ định, vị trí phải trùng khớp hoặc là tập con của vị trí nhắm mục tiêu của danh mục của bạn."),
     
    (r"- If you want to use the Single Video or Catalog Video ad format, ensure the catalog contains at least one available catalog product\.",
     "- Nếu bạn muốn sử dụng định dạng quảng cáo Single Video hoặc Catalog Video, hãy đảm bảo danh mục chứa ít nhất một sản phẩm danh mục khả dụng."),
     
    (r"- If you want to use the Catalog Carousel ad format, ensure the catalog contains at least two available catalog products\.",
     "- Nếu bạn muốn sử dụng định dạng quảng cáo Catalog Carousel, hãy đảm bảo danh mục chứa ít nhất hai sản phẩm danh mục khả dụng."),
     
    (r"• one to 35 images \(image_info\), one piece of music \(music_info\), and one to five ad texts \(title_list\)\. Do not pass video_info and tiktok_item_id\.",
     "• từ 1 đến 35 hình ảnh (image_info), một đoạn nhạc (music_info), và từ 1 đến 5 văn bản quảng cáo (title_list). Không truyền video_info và tiktok_item_id."),
     
    (r"• Specify one website URL through landing_page_urls\. • Do not pass page_list\.",
     "• Chỉ định một URL trang web thông qua landing_page_urls. • Không truyền page_list."),
     
    (r"To obtain a list of App IDs, use \[/app/list/\]\(\.\./12-api-reference/43-events-1-0-p1\.md#doc-1740859313270786\)\.",
     "Để lấy danh sách các ID ứng dụng (App ID), sử dụng [/app/list/](../12-api-reference/43-events-1-0-p1.md#doc-1740859313270786)."),
     
    (r"The catalog needs to contain at least two images supported in Catalog Carousel Ads\.",
     "Danh mục cần chứa ít nhất hai hình ảnh được hỗ trợ trong Quảng cáo băng chuyền danh mục (Catalog Carousel Ads)."),
]
