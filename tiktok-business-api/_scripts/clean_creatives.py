import re

path = "docs/09-marketing-api/creatives.md"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

replacements = [
    ("| **01** | [**Video API**](creatives/01-video-api.md) | Upload video (Multipart/URL/Chunk), search, info, cover | `/file/video/ad/upload/`, `/file/video/ad/search/` |",
     "| **01** | [**Video API**](creatives/01-video-api.md) | Tải lên video (Multipart/URL/Chunk), tìm kiếm, thông tin chi tiết, ảnh bìa | `/file/video/ad/upload/`, `/file/video/ad/search/` |"),
    ("| **04** | [**Creative Tools API**](creatives/04-creative-tools-api.md) | AI Smart Video, Smart Soundtrack, Smart Fix, Smart Text, CTA | `/creative/smart_video/create/`, `/video/fix/task/create/` |",
     "| **04** | [**Creative Tools API**](creatives/04-creative-tools-api.md) | Video thông minh AI, Nhạc nền thông minh, Tự động sửa lỗi Smart Fix, Văn bản thông minh Smart Text, Gợi ý CTA | `/creative/smart_video/create/`, `/video/fix/task/create/` |"),
    ("# Call-to-action texts", "# Văn bản kêu gọi hành động (Call-to-action texts)"),
    ("# CTA portfolio", "# Danh mục CTA (CTA portfolio)"),
    ("# Recommended CTAs", "# Gợi ý nút CTA (Recommended CTAs)"),
    ("- For objectives `REACH`, `TRAFFIC`, `VIDEO_VIEWS`, `APP_PROMOTION`, `WEB_CONVERSIONS`, or `PRODUCT_SALES`:",
     "- Đối với các mục tiêu `REACH`, `TRAFFIC`, `VIDEO_VIEWS`, `APP_PROMOTION`, `WEB_CONVERSIONS`, hoặc `PRODUCT_SALES`:"),
    ("- For the objective `LEAD_GENERATION`:", "- Đối với mục tiêu `LEAD_GENERATION`:"),
    ("- At the ad group level:", "- Ở cấp nhóm quảng cáo:"),
    ("- `promotion_type` is `LEAD_GENERATION`", "- `promotion_type` là `LEAD_GENERATION`"),
    ("- At the ad level: `ad_format` is `SINGLE_VIDEO`", "- Ở cấp quảng cáo: `ad_format` là `SINGLE_VIDEO`"),
    ("1. Use [/creative/portfolio/create/](../12-api-reference/36-creative-portfolios.md#doc-1739091950439426) to create a Display Card portfolio.",
     "1. Sử dụng [/creative/portfolio/create/](../12-api-reference/36-creative-portfolios.md#doc-1739091950439426) để tạo portfolio Thẻ hiển thị hình ảnh (Display Card portfolio)."),
    ("- Set `creative_portfolio_type` to `CARD`.", "- Thiết lập `creative_portfolio_type` thành `CARD`."),
    ("- Set `card_type` to `IMAGE`.", "- Thiết lập `card_type` thành `IMAGE`."),
    ("2.  Use the portfolio in your ad.", "2. Sử dụng portfolio trong quảng cáo của bạn."),
    ("2. Use [/smart_plus/ad/create/](../12-api-reference/62-upgraded-smartplus-p5.md#doc-1843317390059522) or [/smart_plus/ad/update/](../12-api-reference/62-upgraded-smartplus-p6.md#doc-1843317411665921) to create or update your ad.",
     "2. Sử dụng [/smart_plus/ad/create/](../12-api-reference/62-upgraded-smartplus-p5.md#doc-1843317390059522) hoặc [/smart_plus/ad/update/](../12-api-reference/62-upgraded-smartplus-p6.md#doc-1843317411665921) để tạo hoặc cập nhật mẫu quảng cáo của bạn."),
    ("- Set `creative_portfolio_type` to `HOTEL_CARD` .", "- Thiết lập `creative_portfolio_type` thành `HOTEL_CARD`."),
    ("- Set `creative_portfolio_type` to `FLIGHT_CARD` .", "- Thiết lập `creative_portfolio_type` thành `FLIGHT_CARD`."),
    ("1. Use [/creative/portfolio/create/](../12-api-reference/36-creative-portfolios.md#doc-1739091950439426) to create a Destination Card portfolio.",
     "1. Sử dụng [/creative/portfolio/create/](../12-api-reference/36-creative-portfolios.md#doc-1739091950439426) để tạo portfolio Thẻ điểm đến (Destination Card portfolio)."),
    ("- Set `creative_portfolio_type` to `DESTINATION_CARD`.", "- Thiết lập `creative_portfolio_type` thành `DESTINATION_CARD`."),
    ("## Use Countdown Sticker", "## Sử dụng Nhãn dán đếm ngược (Use Countdown Sticker)"),
    ("1. Use [/creative/portfolio/create/](../12-api-reference/36-creative-portfolios.md#doc-1739091950439426) to create a Countdown Sticker portfolio.",
     "1. Sử dụng [/creative/portfolio/create/](../12-api-reference/36-creative-portfolios.md#doc-1739091950439426) để tạo portfolio Nhãn dán đếm ngược (Countdown Sticker portfolio)."),
    ("- Set `creative_portfolio_type` to `STICKER`.", "- Thiết lập `creative_portfolio_type` thành `STICKER`."),
    ("# Gift Code Sticker", "# Nhãn dán mã quà tặng (Gift Code Sticker)"),
    ("## Use Gift Code Sticker", "## Sử dụng Nhãn dán mã quà tặng (Use Gift Code Sticker)"),
    ("1. Use [/creative/portfolio/create/](../12-api-reference/36-creative-portfolios.md#doc-1739091950439426) to create a Gift Code Sticker portfolio.",
     "1. Sử dụng [/creative/portfolio/create/](../12-api-reference/36-creative-portfolios.md#doc-1739091950439426) để tạo portfolio Nhãn dán mã quà tặng (Gift Code Sticker portfolio)."),
    ("# Premium Add-ons", "# Tiện ích tương tác cao cấp (Premium Add-ons)"),
    ("# Use Pop-out Showcase", "# Sử dụng Hộp hiển thị bật nổi (Use Pop-out Showcase)"),
    ("1. Use [/creative/portfolio/create/](../12-api-reference/36-creative-portfolios.md#doc-1739091950439426) to create a Pop-out Showcase portfolio.",
     "1. Sử dụng [/creative/portfolio/create/](../12-api-reference/36-creative-portfolios.md#doc-1739091950439426) để tạo portfolio Hộp hiển thị bật nổi (Pop-out Showcase portfolio)."),
    ("- Set `creative_portfolio_type` to `PREMIUM_BADGE`.", "- Thiết lập `creative_portfolio_type` thành `PREMIUM_BADGE`."),
    ("- Set a call-to-action text via the `call_to_action_text` data field.", "- Thiết lập văn bản kêu gọi hành động qua trường dữ liệu `call_to_action_text`."),
    ("2. Use [/ad/create/](../12-api-reference/02-ads-p1.md#doc-1739953377508354) or [/ad/update/](../12-api-reference/02-ads-p2.md#doc-1739953405142018) to create or update your ad.",
     "2. Sử dụng [/ad/create/](../12-api-reference/02-ads-p1.md#doc-1739953377508354) hoặc [/ad/update/](../12-api-reference/02-ads-p2.md#doc-1739953405142018) để tạo hoặc cập nhật mẫu quảng cáo của bạn."),
    ("# Use Gesture", "# Sử dụng Cử chỉ tương tác (Use Gesture)"),
    ("1. Use [/creative/portfolio/create/](../12-api-reference/36-creative-portfolios.md#doc-1739091950439426) to create a Gesture portfolio.",
     "1. Sử dụng [/creative/portfolio/create/](../12-api-reference/36-creative-portfolios.md#doc-1739091950439426) để tạo portfolio Cử chỉ tương tác (Gesture portfolio)."),
    ("- Set `creative_portfolio_type` to `GESTURE`.", "- Thiết lập `creative_portfolio_type` thành `GESTURE`."),
    ("# Use Superlike", "# Sử dụng Nút thả tim đặc biệt (Use Superlike)"),
    ("1. Use [/creative/portfolio/create/](../12-api-reference/36-creative-portfolios.md#doc-1739091950439426) to create a Superlike portfolio.",
     "1. Sử dụng [/creative/portfolio/create/](../12-api-reference/36-creative-portfolios.md#doc-1739091950439426) để tạo portfolio Nút thả tim đặc biệt (Superlike portfolio)."),
    ("- Set `creative_portfolio_type` to `SUPER_LIKE`.", "- Thiết lập `creative_portfolio_type` thành `SUPER_LIKE`."),
    ("- [Instant Page Editor SDK](creatives.md#doc-1740307202170881): Use it to create instant pages.",
     "- [SDK Trình chỉnh sửa Trang tức thì (Instant Page Editor SDK)](creatives.md#doc-1740307202170881): Sử dụng công cụ này để tạo và chỉnh sửa các trang tức thì."),
    ("- [CTA Recommendations](creatives.md#doc-1740307296329730): Get standard or dynamic CTA recommendations. These CTAs can be used in ads.",
     "- [Gợi ý nút kêu gọi hành động (CTA Recommendations)](creatives.md#doc-1740307296329730): Nhận các đề xuất nút CTA tiêu chuẩn hoặc động để gắn vào mẫu quảng cáo."),
    ("- [Creative Fatigue Detection](creatives.md#doc-1767568085608450): Helps you identify fatigued ads.",
     "- [Phát hiện bão hòa sáng tạo (Creative Fatigue Detection)](creatives.md#doc-1767568085608450): Giúp nhận biết các quảng cáo bị bão hòa nội dung để kịp thời tối ưu."),
    ("- [Share creative assets](../12-api-reference/38-creative-tools.md#doc-1773192725768193): Share creative assets with other advertiser accounts.",
     "- [Chia sẻ tài nguyên sáng tạo](../12-api-reference/38-creative-tools.md#doc-1773192725768193): Chia sẻ tài nguyên sáng tạo với các tài khoản nhà quảng cáo khác."),
    ("| Field | Type | Description |", "| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |"),
    ("## Example complete HTML code", "## Ví dụ mã nguồn HTML hoàn chỉnh"),
    ("- [Get the Page ID](../12-api-reference/54-page.md#doc-1820826387779586)",
     "- [Lấy mã định danh trang (Get the Page ID)](../12-api-reference/54-page.md#doc-1820826387779586)"),
    ("- [Create a TIP Editor SDK access token](../12-api-reference/54-page.md#doc-1820826755283969)",
     "- [Tạo mã token truy cập TIP Editor SDK](../12-api-reference/54-page.md#doc-1820826755283969)"),
    ("- [Validate a TIP Editor SDK access token](../12-api-reference/54-page.md#doc-1820826826000385)",
     "- [Xác thực mã token truy cập TIP Editor SDK](../12-api-reference/54-page.md#doc-1820826826000385)"),
    ("- [Renew a TIP Editor SDK access token](../12-api-reference/54-page.md#doc-1820826847199234)",
     "- [Làm mới mã token truy cập TIP Editor SDK](../12-api-reference/54-page.md#doc-1820826847199234)"),
    ("**Test leads**", "**Khách hàng tiềm năng thử nghiệm (Test leads)**"),
    ("* [Create a test lead](../12-api-reference/48-leads.md#doc-1739047132614722)",
     "* [Tạo khách hàng tiềm năng thử nghiệm](../12-api-reference/48-leads.md#doc-1739047132614722)"),
    ("* [Get a test lead](../12-api-reference/48-leads.md#doc-1739048460493826)",
     "* [Lấy thông tin khách hàng tiềm năng thử nghiệm](../12-api-reference/48-leads.md#doc-1739048460493826)"),
    ("* [Delete a test lead](../12-api-reference/48-leads.md#doc-1739049313198081)",
     "* [Xóa khách hàng tiềm năng thử nghiệm](../12-api-reference/48-leads.md#doc-1739049313198081)"),
    ("**Download leads**", "**Tải xuống khách hàng tiềm năng (Download leads)**"),
    ("* [Create a lead download task](../12-api-reference/48-leads.md#doc-1739052936772610)",
     "* [Tạo tác vụ tải xuống khách hàng tiềm năng](../12-api-reference/48-leads.md#doc-1739052936772610)"),
    ("* [Download leads](../12-api-reference/48-leads.md#doc-1739053563877378)",
     "* [Tải xuống dữ liệu khách hàng tiềm năng](../12-api-reference/48-leads.md#doc-1739053563877378)"),
    ("**Subscribe to leads**", "**Đăng ký nhận dữ liệu khách hàng tiềm năng (Subscribe to leads)**"),
    ("* [Create a subscription](../12-api-reference/66-subscription.md#doc-1739092028876801)",
     "* [Tạo gói đăng ký webhook (Subscription)](../12-api-reference/66-subscription.md#doc-1739092028876801)"),
    ("* [Get subscription details](../12-api-reference/66-subscription.md#doc-1739093832125442)",
     "* [Lấy chi tiết gói đăng ký webhook](../12-api-reference/66-subscription.md#doc-1739093832125442)"),
    ("* [Cancel a subscription](../12-api-reference/66-subscription.md#doc-1739094758789122)",
     "* [Hủy gói đăng ký webhook](../12-api-reference/66-subscription.md#doc-1739094758789122)"),
    ("**Migrate leads**", "**Chuyển giao khách hàng tiềm năng (Migrate leads)**"),
    ("* [Migrate leads to a BC](../12-api-reference/48-leads.md#doc-1740029931324417)",
     "* [Chuyển giao khách hàng tiềm năng vào Business Center](../12-api-reference/48-leads.md#doc-1740029931324417)"),
    ("* [Get form libraries](../12-api-reference/48-leads.md#doc-1740029915327489)",
     "* [Lấy thư viện biểu mẫu](../12-api-reference/48-leads.md#doc-1740029915327489)"),
    ("**Others**", "**Các mục khác (Others)**"),
    ("* [Submit materials](../12-api-reference/41-deprecated-dynamic-scene.md#doc-1740317263937538)",
     "* [Gửi tài liệu phân cảnh](../12-api-reference/41-deprecated-dynamic-scene.md#doc-1740317263937538)"),
    ("* [Create an async task](../12-api-reference/41-deprecated-dynamic-scene.md#doc-1740317320231938)",
     "* [Tạo tác vụ bất đồng bộ](../12-api-reference/41-deprecated-dynamic-scene.md#doc-1740317320231938)"),
    ("* [Get task results](../12-api-reference/41-deprecated-dynamic-scene.md#doc-1740317337705473)",
     "* [Lấy kết quả tác vụ](../12-api-reference/41-deprecated-dynamic-scene.md#doc-1740317337705473)"),
    ("* [Get all videos](../12-api-reference/41-deprecated-dynamic-scene.md#doc-1740317360823297)",
     "* [Lấy danh sách tất cả video](../12-api-reference/41-deprecated-dynamic-scene.md#doc-1740317360823297)"),
    ("* [Run a report](../12-api-reference/41-deprecated-dynamic-scene.md#doc-1740317382510593)",
     "* [Chạy báo cáo hiệu suất phân cảnh](../12-api-reference/41-deprecated-dynamic-scene.md#doc-1740317382510593)"),
    ("1. Obtain a group of dynamic CTAs using [/creative/cta/recommend/](../12-api-reference/38-creative-tools.md#doc-1739362202742785).",
     "1. Lấy nhóm nút CTA động thông qua [/creative/cta/recommend/](../12-api-reference/38-creative-tools.md#doc-1739362202742785)."),
    ("**(Recommended) Option A: Using the updated version endpoint**",
     "**(Khuyến nghị) Tùy chọn A: Sử dụng endpoint phiên bản nâng cấp**"),
    ("- Set `new_version` to `true`.", "- Thiết lập `new_version` thành `true`."),
    ("- Omit `asset_type` and `content_type`.", "- Bỏ qua các trường `asset_type` và `content_type`."),
    ("- Set `creative_portfolio_type` to `CTA`.", "- Thiết lập `creative_portfolio_type` thành `CTA`."),
    ("3. Use the dynamic CTA portfolio in your ads.",
     "3. Sử dụng danh mục CTA động trong mẫu quảng cáo của bạn."),
    ("**Option B: Using the legacy version endpoint**",
     "**Tùy chọn B: Sử dụng endpoint phiên bản cũ**"),
    ("- Set `new_version` to `false`, or leave the field unspecified.",
     "- Thiết lập `new_version` thành `false`, hoặc để trống không truyền."),
    ("- Set `asset_type` to `CTA_AUTO_OPTIMIZED`.", "- Thiết lập `asset_type` thành `CTA_AUTO_OPTIMIZED`."),
    ("* `LOW_RESOLUTION`: Video resolution rate is lower than 540x960px, which doesn'\''t meet our requirements.",
     "* `LOW_RESOLUTION`: Độ phân giải video thấp hơn 540x960px, không đáp ứng yêu cầu kỹ thuật tối thiểu."),
    ("Smart Fix API's function is two-fold:",
     "Chức năng của Smart Fix API bao gồm hai khía cạnh:"),
    ("2. Use [/video/fix/task/get/ ](../12-api-reference/38-creative-tools.md#doc-1741469487859714) to get task results.",
     "2. Sử dụng [/video/fix/task/get/](../12-api-reference/38-creative-tools.md#doc-1741469487859714) để lấy kết quả tác vụ."),
    ("2. Use[ /video/fix/task/get/](../12-api-reference/38-creative-tools.md#doc-1741469487859714)  to get task results.",
     "2. Sử dụng [/video/fix/task/get/](../12-api-reference/38-creative-tools.md#doc-1741469487859714) để lấy kết quả tác vụ."),
    ("- [Smart Video Soundtrack](../12-api-reference/38-creative-tools.md#doc-1739089635852289)",
     "- [Nhạc nền video thông minh (Smart Video Soundtrack)](../12-api-reference/38-creative-tools.md#doc-1739089635852289)"),
    ("- [Quick Optimization](../12-api-reference/38-creative-tools.md#doc-1739355078757377)",
     "- [Tối ưu hóa nhanh (Quick Optimization)](../12-api-reference/38-creative-tools.md#doc-1739355078757377)"),
    ("- [Smart Video](../12-api-reference/38-creative-tools.md#doc-1739352294717441)",
     "- [Video thông minh (Smart Video)](../12-api-reference/38-creative-tools.md#doc-1739352294717441)"),
    ("# Creative Fatigue Detection", "# Phát hiện bão hòa sáng tạo (Creative Fatigue Detection)"),
    ("Creative Fatigue Detection is performed by considering the following aspects:",
     "Tính năng phát hiện bão hòa sáng tạo được thực hiện bằng cách đánh giá các khía cạnh sau:"),
    ("- Declining performance:", "- Hiệu suất sụt giảm:"),
    ("- Reduced reach to new audiences:", "- Phạm vi tiếp cận đối tượng mới suy giảm:"),
    ("1. **Create a campaign** using [/smart_plus/campaign/create/](../12-api-reference/62-upgraded-smartplus-p1.md#doc-1843312852800706).",
     "1. **Tạo chiến dịch** bằng cách gọi [/smart_plus/campaign/create/](../12-api-reference/62-upgraded-smartplus-p1.md#doc-1843312852800706)."),
    ("4. **Detect Creative Fatigue in creatives** using [/creative_fatigue/get/](../12-api-reference/38-creative-tools.md#doc-1767568466842626).",
     "4. **Phát hiện bão hòa sáng tạo** bằng cách gọi [/creative_fatigue/get/](../12-api-reference/38-creative-tools.md#doc-1767568466842626)."),
    ("- [Get Creative Fatigue Detection results](../12-api-reference/38-creative-tools.md#doc-1767568466842626)",
     "- [Lấy kết quả phát hiện bão hòa sáng tạo](../12-api-reference/38-creative-tools.md#doc-1767568466842626)"),
    ("# Obtain pre-review results for your creatives",
     "# Lấy kết quả tiền kiểm duyệt cho tài nguyên sáng tạo (Obtain pre-review results for your creatives)"),
    ("# Introduction\nCreative Pre-review API", "## Giới thiệu (Introduction)\nCreative Pre-review API"),
    ("# Prerequisites\n\n- Bạn đã có quyền", "## Điều kiện tiên quyết (Prerequisites)\n\n- Bạn đã có quyền"),
    ("# Steps\n\nĐể nhận kết quả", "## Các bước thực hiện (Steps)\n\nĐể nhận kết quả"),
    ("# Creative basic reports\n> Đường dẫn: Marketing API > Creatives > Guides > Creative reports > Creative basic reports",
     "# Báo cáo sáng tạo cơ bản (Creative basic reports)\n> Đường dẫn: Marketing API > Creatives > Guides > Creative reports > Creative basic reports"),
    ("# Video Insights reports\n> Đường dẫn: Marketing API > Creatives > Guides > Creative reports > Video Insights reports",
     "# Báo cáo chi tiết video (Video Insights reports)\n> Đường dẫn: Marketing API > Creatives > Guides > Creative reports > Video Insights reports"),
    ("# Creative insights\n> Đường dẫn: Marketing API > Creatives > Guides > Creative reports > Creative insights",
     "# Dữ liệu chi tiết sáng tạo (Creative insights)\n> Đường dẫn: Marketing API > Creatives > Guides > Creative reports > Creative insights"),
    ("# Benchmark data\nBạn có thể gọi", "## Dữ liệu đối sánh chuẩn ngành (Benchmark data)\nBạn có thể gọi"),
    ("# Second-level ad performance data\nBạn có thể gọi", "## Dữ liệu hiệu suất quảng cáo theo từng giây (Second-level ad performance data)\nBạn có thể gọi"),
    ("# Video Insights data\nBạn cũng có thể gọi", "## Dữ liệu chi tiết Video Insights\nBạn cũng có thể gọi"),
    ("* [Video](../12-api-reference/71-video.md#doc-1737587293087810)", "* [Video (Video API)](../12-api-reference/71-video.md#doc-1737587293087810)"),
]

# Card tables formatting
table_hotel_old = """**Card elements**
**Customizable during card creation?**
**Available options**
**Corresponding API field**
**Corresponding field value**

Ảnh chính❌ Ảnh chính (`image_url`) của sản phẩm khách sạn sẽ được sử dụng. Để lấy ảnh chính của sản phẩm khách sạn, gọi [/catalog/product/get/](https://business-api.tiktok.com/portal/docs/get-products/v1.3).
Văn bản chính✅Không: Không hiển thị văn bản chính phía trên tiêu đề. `primary_text`: `NONE`
Ưu đãi: Hiển thị nhãn "Ưu đãi" (Deals) làm văn bản chính phía trên tiêu đề: `DEALS`
Nhãn tùy chỉnh: Hiển thị nhãn tùy chỉnh đầu tiên được chỉ định cho sản phẩm làm văn bản chính phía trên tiêu đề: `CUSTOM_LABEL`. Để lấy nhãn tùy chỉnh đầu tiên của sản phẩm khách sạn, kiểm tra trường `custom_label_0` trả về từ [/catalog/product/get/](https://business-api.tiktok.com/portal/docs/get-products/v1.3).
Tiêu đề❌ Tiêu đề (`name`) của sản phẩm khách sạn sẽ được sử dụng. Để lấy tiêu đề của sản phẩm khách sạn, gọi [/catalog/product/get/](https://business-api.tiktok.com/portal/docs/get-products/v1.3).
Văn bản phụ✅Không: Không hiển thị văn bản phụ dưới tiêu đề. `secondary_text`: `NONE`
Đánh giá: Hiển thị thông tin xếp hạng (điểm tối đa, điểm thực tế và số lượt đánh giá) làm văn bản phụ dưới tiêu đề: `RATING`. Để lấy thông tin đánh giá, kiểm tra các trường `max_score`, `score` và `number_of_reviewers` trả về từ [/catalog/product/get/](https://business-api.tiktok.com/portal/docs/get-products/v1.3).
Nhãn tùy chỉnh: Hiển thị nhãn tùy chỉnh thứ hai của sản phẩm làm văn bản phụ dưới tiêu đề: `CUSTOM_LABEL`. Để lấy nhãn tùy chỉnh thứ hai, kiểm tra trường `custom_label_1` trả về từ [/catalog/product/get/](https://business-api.tiktok.com/portal/docs/get-products/v1.3).
Dùng AI tối ưu ảnh đại diện✅Bật: Sử dụng AI để tối ưu hóa ảnh đại diện (chuyển ảnh không vuông thành ảnh vuông). `image_optimization_enabled`: `true`
Tắt: Không sử dụng AI để tối ưu hóa ảnh đại diện: `false`
Giá (Hiển thị giá)✅Bật: Hiển thị mức giá ở phía dưới thẻ: `card_show_price`: `true`. Để lấy giá sản phẩm khách sạn, kiểm tra trường `price` trả về từ [/catalog/product/get/](https://business-api.tiktok.com/portal/docs/get-products/v1.3).
Tắt: Không hiển thị giá ở dưới đáy thẻ: `false`"""

table_hotel_new = """| Thành phần thẻ | Tùy chỉnh khi tạo thẻ? | Các tùy chọn khả dụng | Trường API tương ứng | Giá trị trường tương ứng |
|---|---|---|---|---|
| Ảnh chính | ❌ Không | Ảnh chính (`image_url`) của sản phẩm khách sạn sẽ được sử dụng. Để lấy ảnh chính của sản phẩm khách sạn, gọi [/catalog/product/get/](https://business-api.tiktok.com/portal/docs/get-products/v1.3). | - | - |
| Văn bản chính | ✅ Có | • Không: Không hiển thị văn bản chính phía trên tiêu đề.<br>• Ưu đãi: Hiển thị nhãn "Ưu đãi" (Deals) làm văn bản chính phía trên tiêu đề.<br>• Nhãn tùy chỉnh: Hiển thị nhãn tùy chỉnh đầu tiên được chỉ định cho sản phẩm làm văn bản chính phía trên tiêu đề. Để lấy nhãn tùy chỉnh đầu tiên của sản phẩm khách sạn, kiểm tra trường `custom_label_0` trả về từ [/catalog/product/get/](https://business-api.tiktok.com/portal/docs/get-products/v1.3). | `primary_text` | • `NONE`<br>• `DEALS`<br>• `CUSTOM_LABEL` |
| Tiêu đề | ❌ Không | Tiêu đề (`name`) của sản phẩm khách sạn sẽ được sử dụng. Để lấy tiêu đề của sản phẩm khách sạn, gọi [/catalog/product/get/](https://business-api.tiktok.com/portal/docs/get-products/v1.3). | - | - |
| Văn bản phụ | ✅ Có | • Không: Không hiển thị văn bản phụ dưới tiêu đề.<br>• Đánh giá: Hiển thị thông tin xếp hạng (điểm tối đa, điểm thực tế và số lượt đánh giá) làm văn bản phụ dưới tiêu đề. Để lấy thông tin đánh giá, kiểm tra các trường `max_score`, `score` và `number_of_reviewers` trả về từ [/catalog/product/get/](https://business-api.tiktok.com/portal/docs/get-products/v1.3).<br>• Nhãn tùy chỉnh: Hiển thị nhãn tùy chỉnh thứ hai của sản phẩm làm văn bản phụ dưới tiêu đề. Để lấy nhãn tùy chỉnh thứ hai, kiểm tra trường `custom_label_1` trả về từ [/catalog/product/get/](https://business-api.tiktok.com/portal/docs/get-products/v1.3). | `secondary_text` | • `NONE`<br>• `RATING`<br>• `CUSTOM_LABEL` |
| Dùng AI tối ưu ảnh đại diện | ✅ Có | • Bật: Sử dụng AI để tối ưu hóa ảnh đại diện (chuyển ảnh không vuông thành ảnh vuông).<br>• Tắt: Không sử dụng AI để tối ưu hóa ảnh đại diện. | `image_optimization_enabled` | `true`<br>`false` |
| Giá (Hiển thị giá) | ✅ Có | • Bật: Hiển thị mức giá ở phía dưới thẻ. Để lấy giá sản phẩm khách sạn, kiểm tra trường `price` trả về từ [/catalog/product/get/](https://business-api.tiktok.com/portal/docs/get-products/v1.3).<br>• Tắt: Không hiển thị giá ở dưới đáy thẻ. | `card_show_price` | `true`<br>`false` |"""

replacements.append((table_hotel_old, table_hotel_new))

table_flight_old = """**Card elements**
**Customizable during card creation?**
**Available options**
**Corresponding API field**
**Corresponding field value**

Ảnh chính❌ Ảnh chính (`image_url`) của sản phẩm vé máy bay sẽ được sử dụng. Để lấy ảnh chính, gọi [/catalog/product/get/](https://business-api.tiktok.com/portal/docs/get-products/v1.3).
Văn bản chính✅Không: Không hiển thị văn bản chính phía trên thành phố đi và đến: `primary_text`: `NONE`
Ưu đãi: Hiển thị nhãn "Ưu đãi" (Deals) phía trên thành phố đi và đến: `DEALS`
Nhãn tùy chỉnh: Hiển thị nhãn tùy chỉnh đầu tiên làm văn bản chính: `CUSTOM_LABEL`. Để lấy nhãn tùy chỉnh đầu tiên của chuyến bay, kiểm tra `custom_label_0` trả về từ [/catalog/product/get/](https://business-api.tiktok.com/portal/docs/get-products/v1.3).
Thành phố khởi hành & Đến❌ Thành phố đi (`origin_city`) và đến (`destination_city`) sẽ được lấy từ dữ liệu chuyến bay qua [/catalog/product/get/](https://business-api.tiktok.com/portal/docs/get-products/v1.3).
Văn bản phụ✅Không: Không hiển thị văn bản phụ dưới tiêu đề. `secondary_text`: `NONE`
Nhãn tùy chỉnh: Hiển thị nhãn tùy chỉnh thứ hai của sản phẩm làm văn bản phụ: `CUSTOM_LABEL`. Để lấy nhãn tùy chỉnh thứ hai, kiểm tra trường `custom_label_1` từ [/catalog/product/get/](https://business-api.tiktok.com/portal/docs/get-products/v1.3).
Dùng AI tối ưu ảnh đại diện✅Bật: Sử dụng AI để tối ưu hóa ảnh đại diện (chuyển ảnh không vuông thành ảnh vuông). `image_optimization_enabled`: `true`
Tắt: Không sử dụng AI để tối ưu hóa ảnh đại diện: `false`
Giá (Hiển thị giá)✅Bật: Hiển thị giá vé dưới đáy thẻ: `card_show_price`: `true`. Để lấy giá vé chuyến bay, kiểm tra `price` trả về từ [/catalog/product/get/](https://business-api.tiktok.com/portal/docs/get-products/v1.3).
Tắt: Không hiển thị giá ở dưới đáy thẻ: `false`"""

table_flight_new = """| Thành phần thẻ | Tùy chỉnh khi tạo thẻ? | Các tùy chọn khả dụng | Trường API tương ứng | Giá trị trường tương ứng |
|---|---|---|---|---|
| Ảnh chính | ❌ Không | Ảnh chính (`image_url`) của sản phẩm vé máy bay sẽ được sử dụng. Để lấy ảnh chính, gọi [/catalog/product/get/](https://business-api.tiktok.com/portal/docs/get-products/v1.3). | - | - |
| Văn bản chính | ✅ Có | • Không: Không hiển thị văn bản chính phía trên thành phố đi và đến.<br>• Ưu đãi: Hiển thị nhãn "Ưu đãi" (Deals) phía trên thành phố đi và đến.<br>• Nhãn tùy chỉnh: Hiển thị nhãn tùy chỉnh đầu tiên làm văn bản chính. Để lấy nhãn tùy chỉnh đầu tiên của chuyến bay, kiểm tra `custom_label_0` trả về từ [/catalog/product/get/](https://business-api.tiktok.com/portal/docs/get-products/v1.3). | `primary_text` | • `NONE`<br>• `DEALS`<br>• `CUSTOM_LABEL` |
| Thành phố khởi hành & Đến | ❌ Không | Thành phố đi (`origin_city`) và đến (`destination_city`) sẽ được lấy từ dữ liệu chuyến bay qua [/catalog/product/get/](https://business-api.tiktok.com/portal/docs/get-products/v1.3). | - | - |
| Văn bản phụ | ✅ Có | • Không: Không hiển thị văn bản phụ dưới tiêu đề.<br>• Nhãn tùy chỉnh: Hiển thị nhãn tùy chỉnh thứ hai của sản phẩm làm văn bản phụ. Để lấy nhãn tùy chỉnh thứ hai, kiểm tra trường `custom_label_1` từ [/catalog/product/get/](https://business-api.tiktok.com/portal/docs/get-products/v1.3). | `secondary_text` | • `NONE`<br>• `CUSTOM_LABEL` |
| Dùng AI tối ưu ảnh đại diện | ✅ Có | • Bật: Sử dụng AI để tối ưu hóa ảnh đại diện (chuyển ảnh không vuông thành ảnh vuông).<br>• Tắt: Không sử dụng AI để tối ưu hóa ảnh đại diện. | `image_optimization_enabled` | `true`<br>`false` |
| Giá (Hiển thị giá) | ✅ Có | • Bật: Hiển thị giá vé dưới đáy thẻ. Để lấy giá vé chuyến bay, kiểm tra `price` trả về từ [/catalog/product/get/](https://business-api.tiktok.com/portal/docs/get-products/v1.3).<br>• Tắt: Không hiển thị giá ở dưới đáy thẻ. | `card_show_price` | `true`<br>`false` |"""

replacements.append((table_flight_old, table_flight_new))

for old, new in replacements:
    if old in text:
        text = text.replace(old, new)
    else:
        print("NOT FOUND:", old[:60])

with open(path, "w", encoding="utf-8") as f:
    f.write(text)
print("Updated creatives.md successfully!")
