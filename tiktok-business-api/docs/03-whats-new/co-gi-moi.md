# Có gì mới (What's New) — các thay đổi gần đây

Tài liệu này tổng hợp toàn bộ các cập nhật, tính năng mới, thay đổi về endpoint, tham số, sự kiện webhook và nâng cấp kỹ thuật mới nhất trong TikTok API for Business.

---

## Có gì mới (`What's New`)
<a id="doc-1740029165513730"></a>
<!-- doc_id: 1740029165513730 -->

> Đường dẫn: What's New

### Tổng quan tài liệu
- **Mục đích**: Cung cấp nhật ký thay đổi chính thức (changelog) của TikTok API for Business, giúp các kỹ sư tích hợp, nhà phát triển và đối tác quảng cáo kịp thời nắm bắt các tính năng mới, thay đổi về tham số, endpoint mới ra mắt, cũng như các lộ trình ngừng hỗ trợ (deprecation) để nâng cấp hệ thống kịp thời.
- **Khi nào dùng**: Tham khảo định kỳ hàng tuần hoặc hàng tháng khi lập kế hoạch phát triển tính năng mới, nâng cấp phiên bản API, hoặc tối ưu hóa hiệu quả các chiến dịch quảng cáo tự động hóa.
- **Các nhóm nghiệp vụ chính liên tục được cập nhật**:
  - **Chiến dịch thông minh nâng cấp (Upgraded Smart+ Campaigns)**: Mở rộng các kịch bản Tìm kiếm (Search Ads), định dạng thẻ xoay, quảng cáo Streaming (Multi-Show), hỗ trợ vị trí phụ Lemon8/PineDrama, quản lý thông tin sản phẩm (`product_info`) và tối ưu hóa ngân sách.
  - **Giao thức ngữ cảnh mô hình (MCP) & Agentic AI**: Ra mắt TikTok for Business MCP Server, các endpoint ủy quyền MCP, công cụ chẩn đoán Agent-to-Agent (`tiktok_ads_diagnosis_agent`) và hướng dẫn kết nối với các trợ lý AI hàng đầu (Claude, ChatGPT, Cursor).
  - **Quản lý danh mục (Catalog Management)**: Hỗ trợ loại danh mục chung (`GENERIC`) cho các sản phẩm/dịch vụ ngoài bán lẻ thương mại, bộ lọc phim ngắn drama series.
  - **Báo cáo & Phân tích (Reporting & Insights)**: Ra mắt API đăng ký thông báo báo cáo theo phút (Reporting Subscription API), bổ sung các chỉ số tăng trưởng tự nhiên (Native Growth), chỉ số tương tác phân tách giữa trả phí và tự nhiên, và các dimension chi tiết cho TikTok Minis.
  - **Tài khoản & Xác minh (Accounts & Verification)**: Ra mắt Verification API giúp số hóa quy trình xác minh tài khoản Business Center và Ad Account qua API, mở rộng độ dài bình luận từ 150 lên 1.200 ký tự và hỗ trợ gửi ảnh trong bình luận.
- **Lưu ý quan trọng**: TikTok API for Business liên tục cập nhật theo chu kỳ hàng tuần. Khi xây dựng ứng dụng, hãy luôn kiểm tra nhật ký thay đổi này để đảm bảo sử dụng các tham số mới nhất và tránh các trường hợp sử dụng các trường sắp ngừng hỗ trợ.
- **Tài liệu đầy đủ**: Xem chi tiết toàn bộ lịch sử thay đổi tại [TikTok for Business Portal — Doc 1740029165513730](https://business-api.tiktok.com/portal/docs?id=1740029165513730).

---

### Nhật ký thay đổi nổi bật năm 2026

#### Tháng 10 năm 2026

| Ngày | Loại thay đổi | Danh mục API | Nội dung chi tiết |
|---|---|---|---|
| 09/10/2026 | Cải tiến tài liệu | MCP | Ra mắt bộ hướng dẫn tích hợp chi tiết từng bước để kết nối TikTok for Business MCP Server với các nền tảng AI phổ biến: [Claude](../05-mcp-server/mcp-server-tom-tat.md#doc-1876677898348545), [ChatGPT](../05-mcp-server/mcp-server-tom-tat.md#doc-1876678063526450), và [Cursor](../05-mcp-server/mcp-server-tom-tat.md#doc-1876678103250945), giúp tiết kiệm thời gian cấu hình và đưa trợ lý AI vào vận hành ngay lập tức. |

---

#### Tháng 9 năm 2026

| Ngày | Loại thay đổi | Danh mục API | Nội dung chi tiết |
|---|---|---|---|
| 25/09/2026 | Nâng cấp sản phẩm | Accounts | Bổ sung tham số phản hồi `post_count` vào endpoint [/business/hashtag/suggestion/](../12-api-reference/01-accounts-p2.md#doc-1762228503821314) để lấy tổng số bài đăng liên kết với hashtag được gợi ý. Hashtag gợi ý hiện được sắp xếp theo số lượng bài viết, phản ánh trải nghiệm thực tế trong ứng dụng. |
| 18/09/2026 | Nâng cấp sản phẩm | Quản lý chiến dịch | Mở rộng tính năng của Upgraded Smart+ Campaigns bằng việc hỗ trợ Chiến dịch tìm kiếm (Search Ads) cho mục tiêu Doanh số (Sales). Tham số yêu cầu `creative_campaign_type` được tích hợp vào [/smart_plus/campaign/get/](../12-api-reference/62-upgraded-smartplus-p1.md#doc-1843312818332930) để lọc các chiến dịch tìm kiếm. |
| 04/09/2026 | Nâng cấp sản phẩm | Quản lý chiến dịch | Hỗ trợ Upgraded Smart+ Generic Catalog Ads bằng cách bổ sung giá trị enum `GENERIC` cho tham số `catalog_type` trên các endpoint [/smart_plus/campaign/create/](../12-api-reference/62-upgraded-smartplus-p1.md#doc-1843312852800706), [/smart_plus/campaign/update/](../12-api-reference/62-upgraded-smartplus-p1.md#doc-1843312876001282), và [/smart_plus/campaign/get/](../12-api-reference/62-upgraded-smartplus-p1.md#doc-1843312818332930), phục vụ các nhà quảng cáo quản lý kho hàng không thuộc lĩnh vực thương mại bán lẻ. |
| 04/09/2026 | Nâng cấp sản phẩm | Công cụ (Tools) | Ra mắt 2 endpoint mới: [/report/bid_protection/status/get/](../12-api-reference/70-tools-p2.md#doc-1874392512912449) và [/report/bid_protection/detail/get/](../12-api-reference/70-tools-p3.md#doc-1874392516418561) để truy xuất trạng thái bảo vệ giá thầu hiện tại, lịch sử bảo vệ giá thầu và hạn mức tín dụng quảng cáo trong 60 ngày gần nhất cho các chiến dịch/nhóm quảng cáo Upgraded Smart+. |
| 04/09/2026 | Nâng cấp sản phẩm | Business Center | Bổ sung các giá trị enum `PUBLISH_VIDEO_ADS_ONLY`, `PUBLISH_VIDEO_SHOW_ON_TT_PROFILE_AND_ADS`, `SHOWCASE`, và `SERIES` vào tham số `tt_account_roles` trên các endpoint phân quyền tài sản: [/bc/asset/assign/](../12-api-reference/15-bc-assets.md#doc-1739438211077121), [/bc/asset/get/](../12-api-reference/15-bc-assets.md#doc-1739432717798401), và [/bc/asset/admin/get/](../12-api-reference/15-bc-assets.md#doc-1739433007779841). |
| 04/09/2026 | Nâng cấp sản phẩm | Quản lý danh mục | Bổ sung tham số yêu cầu `series_ids` và các bộ lọc phim ngắn khác vào [/catalog/product/get/](../12-api-reference/28-catalog-products-p2.md#doc-1740564136678402) để hỗ trợ lọc phim ngắn theo ID sê-ri, tên phim... |
| 04/09/2026 | Nâng cấp sản phẩm | TikTok One | Tinh chỉnh tên quyền hạn cho các endpoint TikTok One để đảm bảo tính nhất quán và rõ ràng trên toàn hệ thống. |
| 04/09/2026 | Nâng cấp sản phẩm | TikTok One | Chuyển tham số `handle_names` thành không bắt buộc trong [/tto/tcm/campaign/create/](../12-api-reference/68-tiktok-one-p1.md#doc-1815693549459458), cho phép tạo chiến dịch mở rộng và hỗ trợ thêm gia tăng tới 20.000 creator qua tham số này. |

---

#### Tháng 8 năm 2026

| Ngày | Loại thay đổi | Danh mục API | Nội dung chi tiết |
|---|---|---|---|
| 28/08/2026 | Nâng cấp sản phẩm | MCP | Ra mắt nhóm endpoint [Xác thực và ủy quyền MCP (MCP Authorization)](../12-api-reference/50-mcp-authorization.md#doc-1873496702070273), cho phép kết nối các agent tùy chỉnh trực tiếp với TikTok for Business MCP Server. |
| 28/08/2026 | Nâng cấp sản phẩm | MCP | Ra mắt công cụ tương tác giữa các Agent (Agent-to-Agent - A2A) đầu tiên: `tiktok_ads_diagnosis_agent`. Agent lưu trữ của bạn có thể gọi công cụ này để chẩn đoán các vấn đề hiệu suất cho tài khoản quảng cáo không phải GMV Max và nhận thông tin phân tích chuyên sâu bằng ngôn ngữ tự nhiên từ các mô hình chẩn đoán chính thức của TikTok. |
| 28/08/2026 | Nâng cấp sản phẩm | Quản lý danh mục | Hỗ trợ loại catalog chung (`GENERIC`) qua tham số `catalog_type` trong [/catalog/create/](../12-api-reference/25-catalog-management.md#doc-1740306481704961) và [/catalog/get/](../12-api-reference/25-catalog-management.md#doc-1740315452868610). Cho phép quản lý sản phẩm thông qua tệp CSV hoặc JSON schema. |
| 21/08/2026 | Nâng cấp sản phẩm | Quản lý chiến dịch | Mở rộng tính năng Upgraded Smart+ Campaigns hỗ trợ Chiến dịch tìm kiếm cho mục tiêu Quảng bá ứng dụng (`APP_PROMOTION`) và Tạo khách hàng tiềm năng (`LEAD_GENERATION`). Tích hợp các tham số `is_search_campaign`, `automated_keywords_enabled`, `search_keywords` và `thumbnail_mode`. |
| 21/08/2026 | Nâng cấp sản phẩm | Quản lý chiến dịch | Bổ sung tham số phản hồi `smart_plus_creative_id` vào các endpoint Upgraded Smart+ Ad ([/smart_plus/ad/create/](../12-api-reference/62-upgraded-smartplus-p5.md#doc-1843317390059522), [/smart_plus/ad/update/](../12-api-reference/62-upgraded-smartplus-p6.md#doc-1843317411665921), [/smart_plus/ad/get/](../12-api-reference/62-upgraded-smartplus-p4.md#doc-1843317378982914)) để lấy ID của từng tài liệu sáng tạo bên trong quảng cáo. |
| 21/08/2026 | Nâng cấp sản phẩm | Quản lý chiến dịch | Bổ sung tham số yêu cầu `material_name` vào Upgraded Smart+ Ad để tùy biến đặt tên cho bộ thẻ xoay (carousel). |
| 21/08/2026 | Nâng cấp sản phẩm | Sáng tạo (Creatives) | Ra mắt quy trình tiền kiểm duyệt nội dung sáng tạo (Creative Pre-review) thông qua các endpoint mới [/creative/pre_review/task/create/](../12-api-reference/35-creative-pre-review.md#doc-1874110632584577) và [/creative/pre_review/task/get/](../12-api-reference/35-creative-pre-review.md#doc-1874110636550082), đồng thời hỗ trợ tham số `pre_review_enabled` khi tải lên video hoặc hình ảnh. |
| 14/08/2026 | Nâng cấp sản phẩm | Báo cáo | Bổ sung các chỉ số thuộc tính `smart_plus_creative_id`, `smart_plus_creative_name`, `adgroup_name`, và `campaign_name` vào [Báo cáo tổng quan sáng tạo Upgraded Smart+](../12-api-reference/62-upgraded-smartplus-p6.md#doc-1843317489576961). |
| 07/08/2026 | Nâng cấp sản phẩm | Quản lý chiến dịch | Bổ sung giá trị enum `CATEGORY` và `SEASONAL` cho tham số phản hồi `content_lineup_type` trong [/tool/contextual_tag/get/](../12-api-reference/70-tools-p2.md#doc-1747747118654465) và [/tool/contextual_tag/info/](../12-api-reference/70-tools-p2.md#doc-1747747180830722) để phân loại ngữ cảnh quảng cáo TikTok Pulse. |
| 07/08/2026 | Nâng cấp sản phẩm | Accounts & Bình luận | Mở rộng giới hạn độ dài văn bản của tham số `text` khi tạo hoặc trả lời bình luận trong [/business/comment/create/](../12-api-reference/01-accounts-p1.md#doc-1762228442072066) và [/business/comment/reply/create/](../12-api-reference/01-accounts-p1.md#doc-1762228448779266) từ 150 ký tự lên 1.200 ký tự. |

---

#### Tháng 7 năm 2026

| Ngày | Loại thay đổi | Danh mục API | Nội dung chi tiết |
|---|---|---|---|
| 31/07/2026 | Nâng cấp sản phẩm | Quản lý chiến dịch | Hỗ trợ tính năng tự động thêm các tài sản mới tạo vào quảng cáo tin nhắn tức thì Upgraded Smart+ (với Messenger và WhatsApp) thông qua tham số `creative_auto_add_toggle` trong [/smart_plus/ad/create/](../12-api-reference/62-upgraded-smartplus-p5.md#doc-1843317390059522). |
| 24/07/2026 | Nâng cấp sản phẩm | Quản lý chiến dịch | Bổ sung tham số yêu cầu `app_attribution_source` và `app_data_source` vào các endpoint Upgraded Smart+ Ad Group để kiểm soát chính xác nguồn quy kết dữ liệu và nguồn dữ liệu ưu tiên khi phân phối. Ra mắt endpoint [/tool/available/attribution_source/](../12-api-reference/70-tools-p2.md#doc-1870952425111618). |
| 24/07/2026 | Nâng cấp sản phẩm | Xác minh tài khoản | Ra mắt bộ API Xác minh tài khoản (Verification API) với 4 endpoint mới: [/account/verification/filetype/](../12-api-reference/72-verification.md#doc-1870687810081794), [/account/verification/upload/](../12-api-reference/72-verification.md#doc-1870687812502530), [/account/verification/submit/](../12-api-reference/72-verification.md#doc-1870687936881281), và [/account/verification/status/](../12-api-reference/72-verification.md#doc-1870687815670786), thay thế hoàn toàn quy trình xác minh thủ công bằng giao diện trước đây. |
| 24/07/2026 | Nâng cấp sản phẩm | Accounts | Ra mắt endpoint [/business/publish/location/](../12-api-reference/01-accounts-p2.md#doc-1870580030749698) và bổ sung tham số `location_id`, `location_name` khi xuất bản video/ảnh lên tài khoản TikTok sở hữu. |
| 17/07/2026 | Nâng cấp sản phẩm | Báo cáo | Nâng cấp báo cáo cơ bản để các chỉ số tăng trưởng tự nhiên (Native Growth metrics) có thể nhóm theo 1 chiều ID hoặc kết hợp với `stat_time_day`. |
| 17/07/2026 | Nâng cấp sản phẩm | Sáng tạo | Bổ sung tham số yêu cầu `sort_field` vào [/file/video/ad/search/](../12-api-reference/71-video.md#doc-1740050472224769) cho phép sắp xếp video theo thời gian cập nhật gần nhất. |
| 10/07/2026 | Nâng cấp sản phẩm | Báo cáo & TikTok One | Mở rộng truy vấn chỉ số Native Growth theo `ad_id` và `ad_id_v2`. Bổ sung các tham số `favorites`, `favorites_organic`, và `favorites_paid` vào báo cáo video TikTok One TCM. |
| 03/07/2026 | Nâng cấp sản phẩm | Quản lý chiến dịch | Ra mắt chiến dịch Upgraded Smart+ TikTok Growth Max dành cho Series phim ngắn (Drama Series). |
| 03/07/2026 | Nâng cấp sản phẩm | MCP & Kỹ năng | Chính thức giới thiệu [TikTok for Business MCP Server](../05-mcp-server/mcp-server.md#doc-1869388085523458) kết nối trực tiếp AI agent với nền tảng quảng cáo; đồng thời ra mắt mô-đun **My Skills** trên cổng thông tin nhà phát triển để phân phối giải pháp tự động hóa lên Agentic Hub. |

---

#### Tháng 6 năm 2026

| Ngày | Loại thay đổi | Danh mục API | Nội dung chi tiết |
|---|---|---|---|
| 26/06/2026 | Nâng cấp sản phẩm | Quản lý chiến dịch | Mở rộng vị trí hiển thị cho Upgraded Smart+ Ad Groups với tham số mới `tiktok_subplacements`, cho phép quảng cáo phân phối trên nền tảng Lemon8 và PineDrama. |
| 26/06/2026 | Nâng cấp sản phẩm | Quản lý chiến dịch | Bổ sung tham số `playable_list` hỗ trợ định dạng quảng cáo có thể chơi (Playable Ads) trong Upgraded Smart+ Ads. |
| 26/06/2026 | Nâng cấp sản phẩm | Quản lý chiến dịch | Bổ sung tham số `product_card_type` cấu hình kiểu hiển thị thẻ sản phẩm cho Upgraded Smart+ E-commerce Catalog Ads. Bổ sung `call_to_action_id` vào endpoint xem trước quảng cáo [/smart_plus/ad/preview/](../12-api-reference/62-upgraded-smartplus-p6.md#doc-1843317445798914). |
| 18/06/2026 | Nâng cấp sản phẩm | TikTok One & Webhook | Bổ sung các chỉ số phân tích lượt thích, bình luận, chia sẻ tách bạch giữa tự nhiên và trả phí (`likes_organic`, `likes_paid`...) trong [/tto/tcm/report/](../12-api-reference/68-tiktok-one-p2.md#doc-1815693573340162). Đưa nội dung bình luận trực tiếp vào sự kiện webhook [comment.update](../10-organic-api/accounts-api.md#doc-1810515104773122). |
| 12/06/2026 | Nâng cấp sản phẩm | Quản lý chiến dịch | Ra mắt 2 endpoint sao chép chiến dịch bất đồng bộ cho Upgraded Smart+: [/smart_plus/campaign/copy/task/create/](../12-api-reference/62-upgraded-smartplus-p1.md#doc-1866528879472641) và [/smart_plus/campaign/copy/task/check/](../12-api-reference/62-upgraded-smartplus-p1.md#doc-1866529943741441). |
| 12/06/2026 | Nâng cấp sản phẩm | Quản lý chiến dịch | Hỗ trợ định dạng Multi-Show (bộ thẻ video tự động phát từ catalog) cho Upgraded Smart+ Streaming Ads thông qua giá trị enum `MULTI_SHOW` của tham số `catalog_media_settings`. |
| 12/06/2026 | Nâng cấp sản phẩm | Báo cáo | Bổ sung chiều dữ liệu `minis_id` và các chỉ số `minis_name`, `optimization_event` vào báo cáo cơ bản đồng bộ để theo dõi riêng biệt quảng cáo VBO IAP và VBO IAA cho TikTok Minis. |
| 05/06/2026 | Nâng cấp sản phẩm | Quản lý chiến dịch | Hỗ trợ đo lường khả năng hiển thị và an toàn thương hiệu sau đấu thầu từ đối tác bên thứ ba thông qua các tham số `viewability_postbid_partner`, `viewability_vast_url`, `brand_safety_postbid_partner`, `brand_safety_vast_url`. |

---

#### Tháng 5 năm 2026

| Ngày | Loại thay đổi | Danh mục API | Nội dung chi tiết |
|---|---|---|---|
| 29/05/2026 | Nâng cấp sản phẩm | Quản lý chiến dịch | Ra mắt 4 endpoint quản lý bài đăng TikTok tùy chỉnh gắn liên kết sản phẩm cấp Shop cho GMV Max: [/gmv_max/creation/custom_anchor_video_list/create/](../12-api-reference/45-gmv-max-p2.md#doc-1866513154013585), [/gmv_max/creation/custom_anchor_video_list/get/](../12-api-reference/45-gmv-max-p2.md#doc-1866513156712449), [/gmv_max/creation/custom_anchor_video_list/delete/](../12-api-reference/45-gmv-max-p2.md#doc-1866513159202306), và [/gmv_max/creation/shop_video/video_anchors/](../12-api-reference/45-gmv-max-p2.md#doc-1866513161692161). |
| 22/05/2026 | Nâng cấp sản phẩm | Khác | Bổ sung hai tham số phản hồi `template_name` và `supported_objectives` vào [/page/get/](../12-api-reference/54-page.md#doc-1820826387779586) để xác định mục tiêu chiến dịch hỗ trợ cho mẫu trang tức thì. |
| 15/05/2026 | Nâng cấp sản phẩm | Accounts | Bổ sung trường `is_ad` vào [/business/video/list/](../12-api-reference/01-accounts-p1.md#doc-1762228421622786) để kiểm tra xem một bài đăng có đang được quảng bá làm quảng cáo hay không. |
| 08/05/2026 | Nâng cấp sản phẩm | Quản lý chiến dịch | Hỗ trợ mục tiêu tối ưu hóa tỷ lệ xem qua 6 giây (View+) cho nhóm quảng cáo TikTok Pulse (`cpv_video_duration = SIX_SECONDS`) và chiến lược phân phối tối ưu hóa lượt xem `VIEW_OPTIMIZE` trong `delivery_mode`. |

---

#### Tháng 4 năm 2026

| Ngày | Loại thay đổi | Danh mục API | Nội dung chi tiết |
|---|---|---|---|
| 24/04/2026 | Nâng cấp sản phẩm | Quản lý chiến dịch & Báo cáo | Hỗ trợ tiện ích bổ trợ tương tác (`interactive_add_on_list`) cho Upgraded Smart+ Web & Catalog Ads. Bổ sung các chỉ số xã hội về đối tượng cân nhắc: `cost_per_consideration`, `new_consideration_rate`, `new_consideration_size`. |
| 24/04/2026 | Nâng cấp sản phẩm | Công cụ | Mở rộng khám phá từ khóa qua [/tool/search_keyword/keyword_idea/](../12-api-reference/70-tools-p1.md#doc-1855460985594881) tại 11 khu vực mới (bao gồm Anh, Pháp, Canada). |
| 17/04/2026 | Nâng cấp sản phẩm | Quản lý chiến dịch | Mở rộng nhắm mục tiêu tuổi 13–17 (`AGE_13_17` và `spc_audience_age = ALL`) cho các chiến dịch Upgraded Smart+ Cài đặt và Nhắm lại ứng dụng. |
| 17/04/2026 | Nâng cấp sản phẩm | Quản lý chiến dịch | Mở rộng nhắm lại đối tượng tùy chỉnh cho Quảng cáo danh mục ứng dụng và TMĐT (`shopping_ads_retargeting_type`, `included_custom_actions`...). |
| 10/04/2026 | Nâng cấp sản phẩm | Quản lý chiến dịch | Tích hợp đo lường sự kiện ngoại tuyến và pixel vào chiến dịch App Install / App Retargeting qua các tham số `tracking_pixel_id` và `tracking_offline_event_set_ids`. |
| 03/04/2026 | Nâng cấp sản phẩm | Quản lý chiến dịch & Báo cáo | Ra mắt endpoint [/campaign/gmv_max/creative/update/](../12-api-reference/45-gmv-max-p2.md#doc-1861260625563202) quản lý thêm/xóa tài liệu sáng tạo trong chiến dịch GMV Max. Cập nhật liên kết tài liệu theo hướng ngữ nghĩa, thân thiện hơn. |

---

#### Tháng 3 năm 2026

| Ngày | Loại thay đổi | Danh mục API | Nội dung chi tiết |
|---|---|---|---|
| 27/03/2026 | Nâng cấp sản phẩm | Quản lý chiến dịch | Bổ sung các tham số thông tin sản phẩm và ưu đãi: `product_titles`, `product_image_list`, `catalog_tag_list`, `promo_info_list`, `product_info_enabled` vào các endpoint Upgraded Smart+ Ad ([/smart_plus/ad/create/](../12-api-reference/62-upgraded-smartplus-p5.md#doc-1843317390059522), [/smart_plus/ad/update/](../12-api-reference/62-upgraded-smartplus-p6.md#doc-1843317411665921), [/smart_plus/ad/get/](../12-api-reference/62-upgraded-smartplus-p4.md#doc-1843317378982914)). |
| 27/03/2026 | Nâng cấp sản phẩm | Báo cáo | Nâng cấp báo cáo đối tượng đồng bộ với các dimension `bucket_id`, `stat_time_hour` và chỉ số `cost` để hỗ trợ tối ưu giá thầu Real-Time API. |
| 20/03/2026 | Nâng cấp sản phẩm | Báo cáo | Ra mắt **Reporting Subscription API** cho phép theo dõi thay đổi chỉ số báo cáo (`spend`, `impressions`, `clicks`, `video_play_actions`) và nhận thông báo biến động ở cấp độ phút. |
| 20/03/2026 | Nâng cấp sản phẩm | Business Center | Bổ sung tham số `payment_portfolio_id` vào [/bc/balance/get/](../12-api-reference/13-bc-payments.md#doc-1739939128198145) và [/bc/transfer/](../12-api-reference/13-bc-payments.md#doc-1739939095321601), hỗ trợ phân biệt danh mục thanh toán nâng cao và tiêu chuẩn. |
| 13/03/2026 | Nâng cấp sản phẩm | Quản lý chiến dịch | Hỗ trợ kiểm soát chế độ Spark Ads Push qua `ads_only_mode` trong [/identity/get/](../12-api-reference/46-identity.md#doc-1740218420781057), [/identity/info/](../12-api-reference/46-identity.md#doc-1740218453385217), và [/advertiser/info/](../12-api-reference/03-ad-accounts.md#doc-1739593083610113) nhằm ngăn chặn đăng bài ngẫu nhiên lên hồ sơ TikTok. |
| 13/03/2026 | Nâng cấp sản phẩm | Quản lý chiến dịch | Hỗ trợ Spark Ads cho danh mục thương mại điện tử với `catalog_creative_info`, `identity_authorized_bc_id`, và các danh tính mới `TT_USER`, `BC_AUTH_TT`. |
| 06/03/2026 | Nâng cấp sản phẩm | Quản lý chiến dịch | Mở rộng số lượng tối đa của `item_group_ids` từ 50 lên 400 trong [/campaign/gmv_max/create/](../12-api-reference/45-gmv-max-p1.md#doc-1822000988713089); bổ sung trường số lượng sản phẩm `quantity` trong [/store/product/get/](../12-api-reference/69-tiktok-store.md#doc-1793482248880130); hỗ trợ tham số `accelerate_testing_for_new_videos` để đẩy nhanh thử nghiệm video mới trong GMV Max. |

---

#### Tháng 2 năm 2026

| Ngày | Loại thay đổi | Danh mục API | Nội dung chi tiết |
|---|---|---|---|
| 27/02/2026 | Nâng cấp sản phẩm | Quản lý chiến dịch | Hỗ trợ giá trị enum `BUDGET_MODE_DAY` và `BUDGET_MODE_TOTAL` cho tham số `budget_mode` trong các chiến dịch Upgraded Smart+ không sử dụng tính năng Tối ưu hóa ngân sách chiến dịch (CBO). |
| 13/02/2026 | Nâng cấp sản phẩm | Accounts & Tin nhắn | Ra mắt endpoint tải ảnh bình luận [/business/comment/image/upload/](../12-api-reference/01-accounts-p1.md#doc-1856212334897154) và cho phép bình luận bằng hình ảnh qua các tham số `image_uri`, `image_width`, `image_height`. Bổ sung `original_msg_id` vào webhook Business Messaging để nhận diện tin nhắn gốc khi có tương tác cảm xúc. |
| 06/02/2026 | Nâng cấp sản phẩm | Quản lý chiến dịch | Bổ sung tham số `disclaimer` cấu hình điều khoản miễn trừ trách nhiệm (dạng văn bản hoặc liên kết nhấp chuột) cho Upgraded Smart+ Ads. Bổ sung `creative_auto_add_toggle` và danh sách chiến lược tự động cải thiện nội dung sáng tạo `creative_auto_enhancement_strategy_list`. |
