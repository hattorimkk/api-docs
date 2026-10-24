# TikTok for Business MCP Server (Tóm tắt)

Tài liệu này tổng hợp các hướng dẫn cốt lõi về việc kết nối, cấu hình, tối ưu hóa và danh mục các công cụ khả dụng trong TikTok for Business Model Context Protocol (MCP) Server. Bản tóm tắt giúp bạn nhanh chóng nắm bắt các kiến trúc kết nối (agent dựng sẵn như Claude, ChatGPT, Cursor hoặc agent tùy chỉnh), phương thức xác thực và cách thức vận hành tối ưu trước khi tham khảo chi tiết tài liệu chính thức.

---

## Cách kết nối agent dựng sẵn với TikTok for Business MCP Server (`How to connect a ready-made agent to TikTok for Business MCP Server`)
<a id="doc-1869389950974978"></a>
<!-- doc_id: 1869389950974978 -->

- **Mục đích**: Hướng dẫn tích hợp các nền tảng AI thương mại tương thích với MCP (như Claude, ChatGPT, Cursor...) trực tiếp với nền tảng quảng cáo TikTok Ads mà không đòi hỏi bất kỳ dòng mã lập trình nào. Nền tảng AI sẽ tự động xử lý các luồng kết nối và ủy quyền để thực thi các tác vụ quảng cáo thông qua các công cụ MCP chuẩn hóa.
- **Khi nào dùng**: Khi các nhà tiếp thị, agency hoặc doanh nghiệp muốn sử dụng ngay các trợ lý AI có sẵn trên thị trường để quản lý chiến dịch, phân tích chỉ số hiệu suất hoặc tối ưu hóa nội dung sáng tạo trên TikTok một cách nhanh chóng.
- **URL máy chủ liên quan**: 
  - Máy chủ dạng phẳng (Flat server): `https://business-api.tiktok.com/open_mcp/tt-ads-mcp-flat` (phù hợp với các agent có cửa sổ ngữ cảnh lớn).
  - Máy chủ dạng phân tầng (Layered server): `https://business-api.tiktok.com/open_mcp/tt-ads-mcp-layer` (khuyến nghị khi nền tảng AI có giới hạn số lượng công cụ nạp sẵn).
- **Quy trình kết nối**:
  1. Chuẩn bị tài khoản TikTok for Business (không cần tài khoản nhà phát triển hay đăng ký ứng dụng developer).
  2. Cấu hình URL máy chủ MCP trong phần cài đặt của nền tảng AI.
  3. Hoàn tất xác thực và ủy quyền trên trang đăng nhập TikTok For Business.
  4. Bắt đầu ra lệnh bằng ngôn ngữ tự nhiên để agent thực thi thao tác quảng cáo.
- **Lưu ý quan trọng**: Quyền ủy quyền của người dùng có hiệu lực trong vòng 30 ngày. Sau thời gian này, bạn chỉ cần thực hiện ủy quyền lại bằng cùng tài khoản TikTok for Business để duy trì hoạt động. Nếu gặp giới hạn số lượng công cụ hiển thị (ví dụ trên Claude), hãy chuyển sang URL máy chủ phân tầng (`tt-ads-mcp-layer`).
- **Tài liệu đầy đủ**: Xem chi tiết tại [TikTok for Business Portal — Doc 1869389950974978](https://business-api.tiktok.com/portal/docs?id=1869389950974978).

---

## Cách kết nối Claude với TikTok for Business MCP Server (`How to connect Claude to TikTok for Business MCP Server`)
<a id="doc-1876677898348545"></a>
<!-- doc_id: 1876677898348545 -->

- **Mục đích**: Hướng dẫn chi tiết từng bước tích hợp tài khoản Claude (Claude Desktop hoặc giao diện web) với TikTok Ads thông qua giao thức MCP, biến các quy trình tiếp thị hàng ngày thành khả năng tương tác tự nhiên.
- **Khi nào dùng**: Dành cho người dùng Claude (yêu cầu tài khoản trả phí như Claude Pro hoặc Claude Max) có nhu cầu quản lý chiến dịch, tạo hàng loạt quảng cáo hoặc tự động hóa tối ưu danh mục sản phẩm TikTok.
- **Phương thức kết nối**:
  - *Lựa chọn 1 (Khuyến nghị)*: Kết nối qua Thư mục kết nối Claude (Claude Connector Directory). Thiết lập nhanh chóng chỉ với một cú nhấp chuột và đăng nhập ủy quyền.
  - *Lựa chọn 2*: Thêm thủ công bằng cách chỉ định trực tiếp URL máy chủ MCP (`https://business-api.tiktok.com/open_mcp/tt-ads-mcp-layer` hoặc `tt-ads-mcp-flat`).
- **Quy trình thực hiện**: Mở giao diện cài đặt kết nối của Claude, tìm kiếm hoặc dán URL máy chủ TikTok Ads MCP, tiến hành đăng nhập bằng tài khoản TikTok for Business để cấp quyền truy cập, sau đó bắt đầu hội thoại bằng câu lệnh tiếng Việt hoặc tiếng Anh.
- **Lưu ý quan trọng**: Phương thức qua Connector Directory mang lại sự tiện lợi tối đa nhưng sẽ bị loại trừ một số công cụ quản trị tài chính nhạy cảm so với phương thức thêm thủ công. Thời hạn ủy quyền kết nối kéo dài 30 ngày.
- **Tài liệu đầy đủ**: Xem chi tiết tại [TikTok for Business Portal — Doc 1876677898348545](https://business-api.tiktok.com/portal/docs?id=1876677898348545).

---

## Các công cụ không khả dụng trong MCP Server trên Claude Connector Directory (`Unavailable tools in the TikTok for Business MCP Server on Claude Connector Directory`)
<a id="doc-1876678060056257"></a>
<!-- doc_id: 1876678060056257 -->

- **Mục đích**: Liệt kê danh sách các công cụ MCP bị giới hạn và không khả dụng khi người dùng kết nối Claude thông qua Claude Connector Directory so với phương thức cấu hình URL thủ công.
- **Khi nào dùng**: Cần tra cứu khi thiết kế quy trình tự động hóa cho Claude, nhằm xác định xem phương thức kết nối qua Connector Directory có đáp ứng đầy đủ yêu cầu nghiệp vụ hay cần chuyển sang cấu hình máy chủ thủ công.
- **Các nhóm công cụ bị loại trừ**:
  - *Nhóm Nhà quảng cáo (Advertiser)*: Các công cụ truy vấn giao dịch tài chính và lấy danh sách nhà quảng cáo được ủy quyền như `advertiser_transaction_get` và `auth_advertiser_get`.
  - *Nhóm Business Center (BC)*: Hầu hết các công cụ truy vấn chi phí, lịch sử ngân sách và giao dịch của tổ chức như `bc_account_budget_changelog_get`, `bc_account_cost_get`, `bc_account_transaction_get`, cũng như các công cụ xác minh và gửi thông tin UnionPay (`bc_advertiser_unionpay_info_check`, `bc_advertiser_unionpay_info_submit`).
- **Lưu ý quan trọng**: Nếu công việc của bạn chỉ tập trung vào việc tạo chiến dịch, tối ưu nội dung sáng tạo, điều chỉnh ngân sách quảng cáo và đọc báo cáo hiệu suất, kết nối qua Connector Directory là hoàn toàn đủ đáp ứng. Nếu cần quản trị tài chính chuyên sâu và cấu hình Business Center, bạn bắt buộc phải sử dụng phương thức thêm máy chủ thủ công.
- **Tài liệu đầy đủ**: Xem chi tiết tại [TikTok for Business Portal — Doc 1876678060056257](https://business-api.tiktok.com/portal/docs?id=1876678060056257).

---

## Cách kết nối ChatGPT với TikTok for Business MCP Server (`How to connect ChatGPT to TikTok for Business MCP Server`)
<a id="doc-1876678063526450"></a>
<!-- doc_id: 1876678063526450 -->

- **Mục đích**: Hướng dẫn cấu hình kết nối trực tiếp tài khoản ChatGPT với nền tảng TikTok Ads thông qua TikTok for Business MCP Server.
- **Khi nào dùng**: Dành cho người dùng ChatGPT (hỗ trợ các gói Pro, Plus, Business, Enterprise và Education trên nền tảng web) muốn tận dụng năng lực phân tích và suy luận của GPT để quản lý quảng cáo TikTok.
- **Quy trình kết nối**:
  1. Đăng nhập vào giao diện ChatGPT trên web.
  2. Điều hướng tới phần quản lý MCP / Actions hoặc ứng dụng kết nối ngoài.
  3. Nhập URL máy chủ TikTok Ads MCP (`https://business-api.tiktok.com/open_mcp/tt-ads-mcp-flat` hoặc bản `layer`).
  4. Thực hiện xác thực ủy quyền OAuth với tài khoản TikTok for Business của bạn.
  5. Bắt đầu tương tác bằng các câu lệnh quản lý chiến dịch, tra cứu dữ liệu hoặc tối ưu hóa.
- **Lưu ý quan trọng**: Đảm bảo tài khoản TikTok for Business được sử dụng đã được phân quyền quản lý các tài khoản quảng cáo mục tiêu. Thời hạn hiệu lực của phiên ủy quyền là 30 ngày.
- **Tài liệu đầy đủ**: Xem chi tiết tại [TikTok for Business Portal — Doc 1876678063526450](https://business-api.tiktok.com/portal/docs?id=1876678063526450).

---

## Cách kết nối Cursor với TikTok for Business MCP Server (`How to connect Cursor to TikTok for Business MCP Server`)
<a id="doc-1876678103250945"></a>
<!-- doc_id: 1876678103250945 -->

- **Mục đích**: Hướng dẫn tích hợp môi trường phát triển Cursor IDE với TikTok for Business MCP Server, giúp các kỹ sư công nghệ và lập trình viên tương tác với hệ sinh thái quảng cáo TikTok trực tiếp từ trình soạn thảo mã nguồn.
- **Khi nào dùng**: Thích hợp cho các nhà phát triển đang xây dựng ứng dụng, kịch bản thử nghiệm hoặc muốn trực tiếp quản lý, kiểm tra dữ liệu chiến dịch quảng cáo và tài sản sáng tạo ngay trong luồng công việc lập trình hàng ngày.
- **Quy trình kết nối**:
  1. Trong Cursor, truy cập **Settings > Features > MCP Servers**.
  2. Nhấp vào nút thêm máy chủ MCP mới (`Add new MCP server`).
  3. Thiết lập thông tin kết nối máy chủ (sử dụng giao thức SSE kèm URL máy chủ TikTok Ads MCP thích hợp).
  4. Hoàn tất quá trình xác thực và ủy quyền tài khoản TikTok for Business trên trình duyệt khi được nhắc.
  5. Sử dụng tính năng Cursor Composer hoặc Cursor Chat để yêu cầu thực thi các tác vụ quảng cáo thông qua công cụ MCP.
- **Lưu ý quan trọng**: Cần quản lý chặt chẽ ngữ cảnh hội thoại để tránh việc nạp quá nhiều công cụ làm tăng chi phí token trong quá trình code.
- **Tài liệu đầy đủ**: Xem chi tiết tại [TikTok for Business Portal — Doc 1876678103250945](https://business-api.tiktok.com/portal/docs?id=1876678103250945).

---

## Cách kết nối agent tùy chỉnh với TikTok for Business MCP Server (`How to connect a custom agent to TikTok for Business MCP Server`)
<a id="doc-1873497625216513"></a>
<!-- doc_id: 1873497625216513 -->

- **Mục đích**: Hướng dẫn toàn diện về kiến trúc và quy trình lập trình để kết nối một AI agent tự phát triển (custom agent) với TikTok for Business MCP Server theo chuẩn giao thức Model Context Protocol.
- **Khi nào dùng**: Khi doanh nghiệp tự xây dựng hệ thống agent nội bộ, nền tảng quảng cáo độc lập hoặc phần mềm trung gian tự động hóa cần quyền truy cập có cấu trúc và có thể mở rộng vào tài nguyên quảng cáo TikTok.
- **Hai lộ trình triển khai**:
  - *Lộ trình 1: Sử dụng MCP access token*: Thực hiện luồng OAuth 2.0 PKCE hoàn chỉnh. Bao gồm 7 bước: (1) Khám phá cấu hình OAuth; (2) Đăng ký agent client; (3) Yêu cầu sự chấp thuận của người dùng (user consent); (4) Đổi mã authorization code lấy bộ token; (5) Gọi công cụ MCP (truy vấn danh sách công cụ và thực thi lệnh); (6) Làm mới token (refresh token); (7) Thu hồi token khi cần (`/oauth2/revoke_token/`).
  - *Lộ trình 2: Sử dụng API access token*: Sử dụng mã token đã được cấp sẵn từ TikTok Marketing API để gọi thẳng các công cụ MCP mà không cần qua luồng PKCE.
- **Lưu ý quan trọng**: Mỗi URL phân vùng máy chủ MCP (`tt-ads-mcp-layer` hoặc `tt-ads-mcp-flat`) phát hành token có phạm vi hoàn toàn độc lập. Token của máy chủ này không thể dùng để xác thực trên máy chủ khác.
- **Tài liệu đầy đủ**: Xem chi tiết tại [TikTok for Business Portal — Doc 1873497625216513](https://business-api.tiktok.com/portal/docs?id=1873497625216513).

---

## Xác thực yêu cầu MCP Server bằng API access token trong agent tùy chỉnh (`Authenticate MCP Server requests with an API access token in a custom agent`)
<a id="doc-1878653463547282"></a>
<!-- doc_id: 1878653463547282 -->

- **Mục đích**: Hướng dẫn cách thức tái sử dụng mã truy cập API Marketing hiện có (Marketing API access token) để xác thực các lệnh gọi công cụ trên TikTok for Business MCP Server trong một agent tùy chỉnh.
- **Khi nào dùng**: Cực kỳ phù hợp cho các nhà phát triển và tổ chức đã có hệ thống tích hợp sẵn với TikTok Marketing API, muốn triển khai nhanh chóng các tính năng agentic MCP mà không phải xây dựng thêm cơ chế quản lý OAuth 2.0 cho MCP.
- **Lợi ích then chốt**:
  - *Ủy quyền dài hạn*: Khắc phục hạn mức 30 ngày của token MCP thông thường; API access token có hiệu lực vô thời hạn cho tới khi bị thu hồi thủ công.
  - *Kiểm soát quyền hạn chi tiết (Granular scope)*: Cho phép lựa chọn chính xác các phạm vi quyền cần thiết khi tạo token, tránh nguy cơ cấp thừa quyền.
  - *Hạn mức tốc độ gọi cao hơn*: Được áp dụng hạn mức rate limit của ứng dụng nhà phát triển (từ 10 đến 50 QPS tùy cấp độ Basic, Advanced, Premium, Ultimate) thay vì giới hạn cố định 6 QPS của người dùng MCP tiêu chuẩn.
- **Cấu hình**: Truyền token thông qua HTTP header: `Access-Token: <API_ACCESS_TOKEN>`. Endpoint lấy token: `/open_api/v1.3/oauth2/access_token/`. Thu hồi token qua `/open_api/v1.3/oauth2/revoke_token/`.
- **Tài liệu đầy đủ**: Xem chi tiết tại [TikTok for Business Portal — Doc 1878653463547282](https://business-api.tiktok.com/portal/docs?id=1878653463547282).

---

## Tối ưu hóa việc sử dụng công cụ trong agent tùy chỉnh (`Optimize tool usage in a custom agent`)
<a id="doc-1879095943307394"></a>
<!-- doc_id: 1879095943307394 -->

- **Mục đích**: Hướng dẫn các giải pháp kỹ thuật tốt nhất nhằm giảm thiểu mức tiêu hao token và tăng độ chính xác của mô hình khi tích hợp thư viện công cụ lớn từ TikTok MCP Server vào agent tùy chỉnh.
- **Khi nào dùng**: Khi agent gặp tình trạng chi phí token tăng cao, tốc độ suy luận chậm, hoặc mô hình ngôn ngữ lớn (LLM) bị nhầm lẫn khi phải lựa chọn giữa hàng trăm công cụ có định nghĩa và tham số tương tự nhau.
- **Nguồn tiêu thụ token chính**:
  - Định nghĩa công cụ (Tool definitions): Nạp trước toàn bộ schema của 400 công cụ vào ngữ cảnh.
  - Kết quả trả về (Tool results): Các đối tượng JSON phản hồi lớn, chứa nhiều trường thông tin không cần thiết.
  - Lịch sử hội thoại (Agent history): Duy trì toàn bộ chuỗi tương tác và dữ liệu thô qua nhiều lượt hội thoại kéo dài.
- **Các giải pháp khắc phục**:
  1. *Tìm kiếm và nạp công cụ động (Tool search & dynamic loading)*: Duy trì danh mục công cụ tập trung và sử dụng tìm kiếm lai (hybrid search kết hợp từ khóa và embedding ngữ nghĩa) để chỉ nạp các schema công cụ thực sự cần thiết cho tác vụ hiện tại.
  2. *Nén kết quả công cụ (Compress tool results)*: Lọc bỏ các trường dữ liệu thừa, chỉ giữ lại các trường mà agent cần trước khi đưa vào context của LLM.
  3. *Cắt tỉa và thu gọn ngữ cảnh (Context pruning & compaction)*: Tóm tắt các bước trung gian và loại bỏ các phản hồi thô sau khi đã hoàn thành tác vụ.
- **Tài liệu đầy đủ**: Xem chi tiết tại [TikTok for Business Portal — Doc 1879095943307394](https://business-api.tiktok.com/portal/docs?id=1879095943307394).

---

## Các công cụ khả dụng trong TikTok for Business MCP Server (`Available tools in TikTok for Business MCP Server`)
<a id="doc-1869389953319233"></a>
<!-- doc_id: 1869389953319233 -->

- **Mục đích**: Giới thiệu tổng quan cấu trúc danh mục khoảng 400 công cụ MCP hiện có trên TikTok for Business MCP Server, giúp người dùng và nhà phát triển nắm được phạm vi năng lực tự động hóa có thể thực hiện.
- **Khi nào dùng**: Tra cứu khi xây dựng kịch bản tương tác, soạn thảo prompt hoặc lập kế hoạch tích hợp tính năng quảng cáo TikTok vào hệ sinh thái AI của doanh nghiệp.
- **Phân loại công cụ**:
  - *Công cụ dựa trên endpoint TikTok API for Business*: Đóng gói trực tiếp các endpoint quen thuộc thành công cụ MCP, bao gồm các nhóm: Quảng cáo (`ad_create`, `ad_get`, `ad_update`...), Nhóm quảng cáo (`adgroup_create`, `adgroup_get`...), Chiến dịch (`campaign_create`, `campaign_get`...), Báo cáo đo lường, Danh mục sản phẩm, Tệp đối tượng và Quản trị Business Center.
  - *Công cụ chuyên biệt độc lập*: Các công cụ Agent-to-Agent (A2A) thông minh không phụ thuộc trực tiếp vào endpoint đơn lẻ, tiêu biểu là `tiktok_ads_creative_testing_agent` (thử nghiệm nội dung sáng tạo tự động) và `tiktok_ads_diagnosis_agent` (chẩn đoán hiệu suất và đưa ra khuyến nghị).
- **Lưu ý quan trọng**: Khi thao tác với các công cụ tạo hoặc cập nhật quảng cáo Upgraded Smart+ Ads (`smart_plus_ad_create`, `smart_plus_ad_update`, `smart_plus_ad_status_update`), cần tuân thủ giới hạn đồng thời: tối đa 1 thao tác mỗi 5 giây cho cùng một quảng cáo để tránh lỗi xung đột hệ thống.
- **Tài liệu đầy đủ**: Xem chi tiết tại [TikTok for Business Portal — Doc 1869389953319233](https://business-api.tiktok.com/portal/docs?id=1869389953319233).
