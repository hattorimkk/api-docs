# Quản lý Skill và MCP

Bộ tài liệu này hướng dẫn toàn diện quy trình quản lý, cấu hình và phân phối các AI Skill cũng như máy chủ MCP (Model Context Protocol) trên nền tảng TikTok for Business Developers. Bạn sẽ tìm hiểu từ các bước chuẩn bị điều kiện tiên quyết, định dạng tệp và biểu mẫu đăng ký, quy trình xét duyệt của TikTok, cho đến việc quản lý vòng đời, cập nhật phiên bản và xử lý sự cố. Thông qua Agentic Hub, các giải pháp AI của bạn có thể tiếp cận trực tiếp mạng lưới nhà quảng cáo toàn cầu trên TikTok.

## Quản lý Skill và MCP (`Skill and MCP management`)
<a id="doc-1869387171836930"></a>
<!-- doc_id: 1869387171836930 -->

> Đường dẫn: Skill and MCP management

Phân hệ **My Agentic Hub** trên cổng TikTok for Business Developers cung cấp không gian làm việc tập trung để quản lý và phân phối các AI Skill cũng như máy chủ MCP (Model Context Protocol). Từ phân hệ này, bạn có thể tải lên Skill hoặc đăng ký máy chủ MCP, theo dõi trạng thái xét duyệt và xuất bản chúng lên [**TikTok for Business Agentic Hub**](https://ads.tiktok.com/help/article/how-to-access-the-tiktok-for-business-agentic-hub) — thị trường tập trung nơi các nhà quảng cáo và nhà phát triển khám phá, tải xuống và quản lý các giải pháp ứng dụng AI phục vụ tự động hóa quảng cáo trên TikTok.

### Tại sao nên xuất bản lên Agentic Hub? (Why publish to Agentic Hub?)

Việc xuất bản Skill hoặc máy chủ MCP mang lại những lợi ích kinh doanh rõ ràng:
- **Tiếp cận tức thì mạng lưới nhà quảng cáo toàn cầu:** Agentic Hub kết nối bạn trực tiếp với cộng đồng nhà quảng cáo TikTok trên toàn thế giới đang chủ động tìm kiếm các công cụ tự động hóa dựa trên AI. Bạn không cần tốn chi phí và công sức xây dựng kênh phân phối riêng — Skill của bạn sẽ nhận được sự chú ý ngay từ ngày đầu tiên.
- **Lộ trình mở rộng quy mô cho các sáng kiến AI độc quyền:** Việc đưa Skill hoặc máy chủ MCP lên nền tảng ngay hôm nay giúp bạn xác lập vị thế trong một hệ sinh thái đang phát triển nhanh chóng. Khi các tình huống sử dụng quảng cáo mới xuất hiện và khả năng của tác nhân (agent) ngày càng mở rộng, việc sớm gia nhập sẽ giúp bạn nắm bắt nhu cầu trước các đối thủ cạnh tranh.
- **Tiềm năng tạo nguồn doanh thu bền vững trong tương lai:** TikTok áp dụng các chính sách thị trường công bằng, minh bạch và trao thưởng cho các nhà phát triển đầu tư vào những giải pháp chất lượng cao. Các nguyên tắc rõ ràng, việc thực thi nhất quán và nhu cầu ngày càng tăng của nhà quảng cáo sẽ tạo ra môi trường mang lại lợi ích lâu dài cho các Skill hoặc máy chủ MCP vượt trội.

### Vòng đời của Skill (Skill lifecycle)

Mỗi Skill tuân theo một vòng đời xác định từ khi tải lên cho đến khi xuất bản trên thị trường. Việc nắm rõ vòng đời này giúp bạn lên kế hoạch quy trình làm việc và chuẩn bị cho các bước tiếp theo.

| Stage | Status | Description |
|---|---|---|
| 1. Upload | Pending Review | Bạn gửi tệp Skill và siêu dữ liệu (metadata). Skill được đưa vào hàng đợi xét duyệt. |
| 2. Review | Pending Review | Đội ngũ TikTok đánh giá Skill về chất lượng, tính tuân thủ và chức năng hoạt động. Quá trình xét duyệt thường kéo dài từ 5–7 ngày làm việc. |
| 3a. Approved | Approved | Skill vượt qua xét duyệt. Bạn có thể xuất bản ngay lập tức hoặc dời lại sau. |
| 3b. Rejected | Rejected | Quá trình xét duyệt phát hiện các vấn đề cần khắc phục. Bạn nhận được phản hồi hữu ích và có thể gửi lại. |
| 4. Publish | Published | Skill đã chính thức hoạt động trên Agentic Hub và hiển thị với các nhà quảng cáo. |
| 5. Manage | Published / Unpublished | Bạn có thể cập nhật phiên bản, chỉnh sửa metadata, kiểm soát khả năng hiển thị hoặc xóa Skill. |

### Vòng đời của MCP server (MCP server lifecycle)

Mỗi máy chủ MCP tuân theo một vòng đời xác định từ khi đăng ký cho đến khi xuất bản trên thị trường. Việc hiểu rõ vòng đời giúp bạn chủ động kế hoạch triển khai.

| Stage | Status | Description |
|---|---|---|
| 1. Upload | Pending Review | Bạn gửi thông tin chi tiết về MCP server. Máy chủ MCP được đưa vào hàng đợi xét duyệt. |
| 2. Review | Pending Review | Đội ngũ TikTok đánh giá MCP server về chất lượng, tính tuân thủ và tính năng hoạt động. |
| 3a. Approved | Approved | MCP server vượt qua xét duyệt. Máy chủ sẽ tự động hoạt động trực tiếp trên Agentic Hub và hiển thị với các nhà quảng cáo. |
| 3b. Rejected | Rejected | Quá trình xét duyệt phát hiện vấn đề. Bạn nhận được phản hồi chi tiết để khắc phục và gửi lại. |
| 4. Manage | Published | Bạn có thể cập nhật phiên bản, kiểm soát khả năng hiển thị hoặc xóa MCP server. |

### Khái niệm cốt lõi (Key concepts)

- **AI Skills (Skills):** Tập hợp các bộ chỉ dẫn cấp cao trang bị cho các tác nhân AI (AI agents) tri thức để tự chủ thực hiện những mục tiêu kinh doanh cụ thể. Một Skill có thể hướng dẫn tác nhân quy trình làm quen (onboarding) cho nhà quảng cáo mới từ đầu đến cuối, luân chuyển nội dung sáng tạo quảng cáo khi mức độ tương tác giảm, hoặc phân bổ lại ngân sách chiến dịch để tối đa hóa ROAS. Skill có thể là **bên thứ nhất** (do TikTok xây dựng) hoặc **bên thứ ba** (do nhà phát triển và đối tác xây dựng), cho phép các tác nhân thực thi quy trình làm việc gồm nhiều bước mà thông thường cần sự giám sát thủ công.
- **Agentic Hub:** Thị trường tập trung trên TikTok Ads, nơi các nhà quảng cáo khám phá, cài đặt và quản lý các Skill cũng như máy chủ MCP tích hợp AI phục vụ tự động hóa quảng cáo.
- **Tiêu chuẩn SKILL.md (SKILL.md standard):** Định dạng mở dùng để đóng gói AI Skills — bao gồm tệp ZIP chứa tệp `SKILL.md` (có metadata YAML ở phần đầu và hướng dẫn Markdown) cùng các tệp hỗ trợ tùy chọn, tương thích với các nền tảng AI agent phổ biến.
- **Model Context Protocol (MCP):** Giao thức mở chuẩn hóa cách các AI agent khám phá, kết nối và tương tác với các nền tảng và dịch vụ bên ngoài. Có thể xem MCP như một bộ chuyển đổi đa năng: bất kỳ tác nhân tương thích nào cũng có thể tự động khám phá và sử dụng các công cụ MCP mà không cần lập trình tích hợp riêng. Giao thức xử lý xác thực, khám phá tính năng và giao tiếp có cấu trúc giữa tác nhân và máy chủ.
- **Máy chủ MCP (MCP server):** Dịch vụ phụ trợ do nhà phát triển tự lưu trữ (developer-hosted backend service) triển khai giao thức Model Context Protocol. Dịch vụ này đóng vai trò cầu nối bảo mật giữa các AI agent và các nền tảng bên ngoài (chẳng hạn như CRM, công cụ phân tích hoặc bộ công cụ sáng tạo), mở ra khả năng tiếp cận nền tảng của bạn dưới dạng các công cụ chuẩn hóa mà tác nhân có thể hiểu được. Khi được đưa lên Agentic Hub, MCP server cho phép các tác nhân của nhà quảng cáo tương tác liền mạch với dữ liệu và tính năng của nền tảng trong quy trình tự động hóa.
- **Công cụ MCP (MCP tools):** Các hàm riêng biệt do MCP Server cung cấp đại diện cho các thao tác quảng cáo cụ thể, chẳng hạn như "tạo chiến dịch", "lấy báo cáo hiệu suất", "cập nhật nhắm mục tiêu đối tượng" hoặc "tạm dừng nhóm quảng cáo". Các tác nhân gọi những công cụ này khi cần để thực hiện hành động, kết hợp chúng theo trình tự để hoàn thành các quy trình phức tạp.

### Tìm hiểu thêm (Learn more)

- Khám phá các chủ đề sau để bắt đầu với quản lý Skill:
  - [Bắt đầu với quản lý Skill](skill-va-mcp.md#doc-1869392848734209): Thiết lập tài khoản nhà phát triển và chuẩn bị tệp Skill.
  - [Tải lên Skill mới](https://business-api.tiktok.com/portal/docs/upload-and-publish-skills/v1.3#item-link-Upload%20a%20new%20Skill): Đi qua toàn bộ quy trình tải lên và gửi xét duyệt.
  - [Tìm hiểu quy trình xét duyệt](https://business-api.tiktok.com/portal/docs/upload-and-publish-skills/v1.3#item-link-Understand%20the%20review%20process): Tìm hiểu những gì diễn ra sau khi gửi và cách theo dõi trạng thái.
  - [Xuất bản Skill đã được phê duyệt](https://business-api.tiktok.com/portal/docs/upload-and-publish-skills/v1.3#item-link-Publish%20an%20approved%20Skill): Đưa Skill hoạt động trực tiếp trên Agentic Hub.
  - [Tải lên phiên bản mới](https://business-api.tiktok.com/portal/docs/manage-published-skills/v1.3#item-link-Upload%20a%20new%20version): Cập nhật Skill đã xuất bản bằng một bản phát hành mới.
  - [Chỉnh sửa metadata của Skill](https://business-api.tiktok.com/portal/docs/manage-published-skills/v1.3#item-link-Edit%20Skill%20metadata): Cập nhật mô tả, danh mục hoặc ngành nghề mà không cần xét duyệt lại.
  - [Kiểm soát hiển thị trên Agentic Hub](https://business-api.tiktok.com/portal/docs/manage-published-skills/v1.3#item-link-Control%20visibility%20on%20Agentic%20Hub): Tạm thời ẩn hoặc hiện Skill của bạn.
  - [Xóa Skill](https://business-api.tiktok.com/portal/docs/manage-published-skills/v1.3#item-link-Delete%20a%20Skill): Xóa vĩnh viễn Skill khỏi tài khoản của bạn.
  - [Gửi lại Skill bị từ chối](https://business-api.tiktok.com/portal/docs/troubleshooting-skills-management/v1.3#item-link-Resubmit%20a%20rejected%20Skill): Khắc phục các vấn đề dựa trên phản hồi và gửi xét duyệt lại.
- Khám phá các chủ đề sau để bắt đầu với quản lý MCP server:
  - [Bắt đầu với quản lý MCP server](skill-va-mcp.md#doc-1879106319214594): Thiết lập tài khoản nhà phát triển và chuẩn bị hạ tầng MCP server.
  - [Đăng ký MCP server mới](https://business-api.tiktok.com/portal/docs/register-mcp-servers/v1.3#anchor-0-2): Đi qua toàn bộ quy trình gửi thông tin máy chủ.
  - [Tìm hiểu quy trình xét duyệt](https://business-api.tiktok.com/portal/docs/register-mcp-servers/v1.3#anchor-0-3): Tìm hiểu những gì diễn ra sau khi nộp và cách theo dõi tiến trình.
  - [Tải lên phiên bản mới](https://business-api.tiktok.com/portal/docs/manage-published-mcp-servers/v1.3#anchor-0-1): Cập nhật MCP server đã xuất bản bằng bản phát hành mới.
  - [Kiểm soát hiển thị trên Agentic Hub](https://business-api.tiktok.com/portal/docs/manage-published-mcp-servers/v1.3#anchor-0-2): Tạm thời ẩn hoặc hiện MCP server.
  - [Xóa MCP server](https://business-api.tiktok.com/portal/docs/manage-published-mcp-servers/v1.3#anchor-0-3): Xóa vĩnh viễn MCP server khỏi tài khoản.
  - [Gửi lại MCP server bị từ chối](https://business-api.tiktok.com/portal/docs/troubleshoot-mcp-server-issues/v1.3#anchor-0-1): Xử lý phản hồi và gửi xét duyệt lại.

## Bắt đầu với quản lý Skill (`Get started with Skill management`)
<a id="doc-1869392848734209"></a>
<!-- doc_id: 1869392848734209 -->

> Đường dẫn: Skill and MCP management > Get started with Skill management

Hãy hoàn thành các điều kiện tiên quyết trong bài viết này trước khi tải lên Skill đầu tiên của bạn.

### Điều kiện tiên quyết (Prerequisites)

Trước khi tải Skill lên cổng TikTok for Business Developers, bạn phải:
1. [Tạo tài khoản TikTok for Business](../04-get-started/bat-dau.md#doc-1738855099573250): Cung cấp quyền truy cập vào hệ sinh thái TikTok for Business.
2. [Đăng ký làm nhà phát triển](../04-get-started/bat-dau.md#doc-1738855176671234): Mở khóa phân hệ **My Agentic Hub** và khả năng tải lên Skill.

> [!NOTE]
> Nếu bạn đã từng sử dụng bất kỳ endpoint nào của TikTok API for Business, bạn đã đáp ứng cả hai điều kiện tiên quyết và có thể chuyển thẳng sang bước chuẩn bị tệp Skill.

### Chuẩn bị tệp Skill hợp lệ (Prepare an eligible Skill file)

Trước khi tải Skill lên, hãy đảm bảo tệp Skill của bạn tuân thủ các yêu cầu về định dạng và cấu trúc của nền tảng. Một tệp có cấu trúc tốt sẽ vượt qua khâu xét duyệt nhanh hơn và mang lại trải nghiệm tốt hơn cho các tác nhân sử dụng chỉ dẫn của bạn.

#### Yêu cầu tệp (File requirements)

| Category | Requirement |
|---|---|
| Format | Tệp nén dạng `.zip` chứa cả hai tệp `SKILL.md` và `README.md` (phân biệt chữ hoa chữ thường). <br> Tệp `SKILL.md` phải được đặt trực tiếp tại thư mục gốc của tệp nén. |
| Size | Kích thước tệp tối đa: 50 MB (sau khi nén). |
| Naming | Chỉ sử dụng chữ thường, số và dấu gạch nối. Không sử dụng dấu cách, chữ in hoa hoặc ký tự đặc biệt. <br> Tên phải mang tính mô tả và hướng hành động (ví dụ: `launch-app-campaign`). Tránh các tên chung chung như `skill1`. <br> Định dạng đặt tên tệp .zip: `Company name-skill goals-Version number` (chỉ dùng tiếng Anh). Với các lần cập nhật tiếp theo, chỉ thay đổi số phiên bản. Ví dụ: `a3-company-budget-optimization-skill-v1`. <br> Trường `name` trong phần YAML frontmatter của tệp `SKILL.md` phải khớp chính xác với trường Skill Name bạn cung cấp trong biểu mẫu tải lên trên cổng nhà phát triển. |
| Frontmatter | Định dạng YAML hợp lệ (phân tách bằng `---`) với hai trường `name` và `description`. <br> Sau phần frontmatter phải là phần nội dung Markdown (Markdown body). |
| Description | Nêu rõ Skill làm nhiệm vụ gì và khi nào nên sử dụng. <br> Bắt đầu bằng trường hợp sử dụng chính (primary use case). <br> Độ dài khuyến nghị: trong vòng 1.536 ký tự. |
| Body | Hướng dẫn tác nhân rõ ràng, mang tính hành động. <br> Độ dài khuyến nghị: từ 15.000 đến 20.000 ký tự. <br> Đặt các tài liệu tham khảo dài trong thư mục `reference/`. |

#### Cấu trúc gói (Package structure)

Skill của bạn phải được đóng gói dưới dạng tệp nén .zip tuân theo định dạng có cấu trúc được thiết kế cho các AI agent tiếp nhận. Cấu trúc tệp nén như sau:

```
launch-app-campaign/
├── SKILL.md              # Tệp kỹ năng chính (bắt buộc)
├── README.md             # Tài liệu hướng dẫn cho người dùng (bắt buộc)
├── reference/            # Các tệp tài liệu tham khảo hỗ trợ (tùy chọn)
│   ├── optimization-rules.md
│   ├── benchmarks.json
│   └── templates/
│       └── report-template.md
├── scripts/              # Các tập lệnh tự động hóa (tùy chọn)
│   └── data-processing.py
└── config.json           # Lược đồ cấu hình (tùy chọn)
```

**Chi tiết các thành phần:**
- **SKILL.md**: Chứa YAML frontmatter (metadata như name, description, version, author và permissions) theo sau là các chỉ dẫn chi tiết hướng dẫn tác nhân AI thực thi quy trình công việc.
- **README.md**: Tài liệu dành cho người dùng giải thích chức năng của Skill, các điều kiện tiên quyết và cách sử dụng. Giống như tệp SKILL.md, tệp này bắt buộc phải đặt tại thư mục gốc của tệp nén (phân biệt chữ hoa chữ thường).
- **reference/**: Các tài liệu bổ trợ mà tác nhân có thể tham khảo trong quá trình thực thi, chẳng hạn như quy tắc tối ưu hóa, dữ liệu đối chuẩn (benchmarks) hoặc mẫu báo cáo.
- **scripts/**: Các tập lệnh thực thi mà tác nhân có thể gọi để xử lý dữ liệu, gọi API hoặc thực hiện các tác vụ tự động khác.
- **config.json**: Lược đồ định nghĩa các tham số có thể cấu hình, cho phép nhà quảng cáo tùy biến hành vi của Skill mà không cần chỉnh sửa chỉ dẫn cốt lõi.

#### Ví dụ tệp SKILL.md (Example SKILL.md)

Dưới đây là một tệp SKILL.md mẫu có cấu trúc chuẩn mực với YAML frontmatter hợp lệ và phần nội dung Markdown chứa các chỉ dẫn rõ ràng, mang tính hành động:

```yaml
---
name: "campaign-performance-optimizer"        # Tên Skill (bắt buộc), phải khớp với trường Skill Name khi tải lên
description: "Use this Skill when you need to evaluate campaign performance and take optimization actions. It analyzes performance data, identifies underperforming ad groups, and generates actionable recommendations."
version: "1.0.0"
author: "Developer Company Name"
use_case: "Ads Management"
permissions:
  - campaign_management
  - reporting_analytics
---

# Campaign Performance Optimizer

## Description
This Skill helps you monitor and optimize TikTok ad campaign performance. Provide a date range and target CPA, and the Skill will identify underperforming ad groups and suggest specific optimization actions.

## Process
1. Pull campaign performance data for the specified date range
2. Identify ad groups where CPA exceeds target by 20%+
3. Generate optimization recommendations
...
```

#### Viết trường `description` hiệu quả (Write an effective `description`)

Trường `description` là trường quan trọng nhất. Tác nhân AI dựa vào trường này để quyết định xem Skill có liên quan đến yêu cầu hiện tại hay không. Hãy viết mô tả để thể hiện cả khả năng của Skill lẫn các cách diễn đạt bằng ngôn ngữ tự nhiên mà người dùng có thể sử dụng.

Ví dụ tốt:
```yaml
description: Launches a TikTok catalog ads campaign end to end. Use when the user wants product sales, catalog remarketing, or to promote a product feed.
```

Ví dụ yếu (quá chung chung để tác nhân có thể đối sánh chính xác):
```yaml
description: Helps with ads.
```

#### Viết phần thân (body) hiệu quả (Write an effective body)

- Nêu rõ **cần phải làm gì**, tránh những đoạn tường thuật dài dòng về quy trình hoặc lý do. Một khi đã được tải vào ngữ cảnh (context), phần thân sẽ tồn tại liên tục trong bộ nhớ, do đó mỗi dòng đều làm tăng chi phí token.
- Giữ dung lượng `SKILL.md` trong khoảng **15.000–20.000 ký tự**. Chuyển các tài liệu tham khảo dài hơn vào các tệp hỗ trợ.
- Đưa vào các **bước xác nhận rõ ràng** trước bất kỳ thao tác ghi dữ liệu hoặc tiêu tốn ngân sách nào.
- Chỉ định **định dạng đầu ra chính xác** bạn mong muốn (bảng biểu, JSON, bản tóm tắt) để đảm bảo kết quả đồng nhất.
- Xử lý các trường hợp kết quả rỗng và lỗi (nếu không có dữ liệu trả về, hãy nêu rõ ràng).

#### Yêu cầu đối với README.md (README.md requirements)

Mỗi gói Skill phải bao gồm một tệp `README.md` giải thích cách sử dụng Skill trong thực tế.

##### Các thành phần bắt buộc (Required elements)

| Element | Description |
|---|---|
| Project name and one-line summary | Tên dự án và tóm tắt một dòng về chức năng cũng như vấn đề mà Skill giải quyết. |
| Quick Start | Ví dụ cài đặt và khởi chạy đơn giản nhất. |
| Target platform | Bất kỳ hạn chế nào về nền tảng (nêu rõ nếu có). <br> Các nền tảng mục tiêu bao gồm: ChatGPT, Claude, Gemini, v.v. |
| Prerequisites / Dependencies | Môi trường runtime, các yêu cầu về quyền, gói phụ thuộc và việc có sử dụng MCP hoặc agent nào khác ngoài TikTok for Business MCP hay không (nếu có, cần nêu rõ cách thức). |
| Configuration | Những gì có thể cấu hình và các giá trị mặc định tương ứng. |

##### Các thành phần khuyến nghị (Recommended elements)

| Element | Description |
|---|---|
| Common errors and troubleshooting | Cách tự chẩn đoán và xử lý khi phát sinh sự cố. |
| Limitations and caveats | Các trường hợp biên (edge cases) và các sự cố đã biết. |
| Contact information | Đơn vị duy trì và cách thức báo cáo sự cố. |

### Các bước tiếp theo (Next steps)

Sau khi tệp Skill đã sẵn sàng, hãy chuyển sang bước [Tải lên và xuất bản Skill](skill-va-mcp.md#doc-1869392851504145).

## Tải lên và xuất bản Skill (`Upload and publish Skills`)
<a id="doc-1869392851504145"></a>
<!-- doc_id: 1869392851504145 -->

> Đường dẫn: Skill and MCP management > Get started with Skill management > Upload and publish Skills

Bài viết này bao quát toàn bộ quy trình từ lúc tải lên một Skill mới cho đến khi Skill hoạt động chính thức trên Agentic Hub.

### Điều hướng đến My Agentic Hub (Navigate to My Agentic Hub)

Mọi tác vụ quản lý Skill đều bắt đầu từ trang **My Agentic Hub**. Để truy cập:

1. Truy cập [cổng TikTok for Business Developers](https://business-api.tiktok.com/portal) và nhấn **Log in** ở góc trên cùng bên phải.

![Nhấn Log in ở góc trên bên phải](https://images.ctfassets.net/5jqet0ab9qci/2LdMpEwuCM0s9mSv7SoKtY/755c2e351c4eaf9c9685cd682d2c68a4/My_skills_EN-1.png)

2. Nhấn vào **My Agentic Hub** ở thanh điều hướng trên cùng bên phải để mở trang quản lý Skill.

![Nhấn My Agentic Hub](https://images.ctfassets.net/5jqet0ab9qci/5WDc5fqbBKfUN8tAI4YeQO/9c1e46c1248390c856b0e33c618d41cc/Click_My_Agentic_Hub.png)

> [!NOTE]
> Tất cả các quy trình trong tài liệu này đều giả định rằng bạn đã đăng nhập và đang xem trang **My Agentic Hub**. Các bước điều hướng này sẽ không được nhắc lại trong các phần tiếp theo.

### Tải lên Skill mới (Upload a new Skill)

Tải lên AI Skill của bạn để quản lý tập trung, tối ưu hóa quy trình xét duyệt và phân phối các giải pháp đến các nhà quảng cáo thông qua TikTok for Business Agentic Hub.

**Các bước thực hiện:**

1. Trên trang My Agentic Hub, nhấn **Upload New** ở góc trên bên trái và chọn **Upload skill**.

![Nhấn Upload New](https://images.ctfassets.net/5jqet0ab9qci/3AkknZRsFCb6SD5Kc8LzPT/408ffa122910900064cf2f5057115a0a/click_Upload_New.png)

![Chọn Upload skill](https://images.ctfassets.net/5jqet0ab9qci/6752UOKeAlzwgeUXlC8Sie/7e66efe50a08556248029d86dcc7204f/select_Upload_skill.png)

2. Điền đầy đủ thông tin vào biểu mẫu tải lên với các trường bắt buộc sau:

| Field | Description |
|---|---|
| Skill Name | Tên duy nhất, mang tính mô tả cho Skill của bạn. Trường này là cố định vĩnh viễn và không thể thay đổi sau khi tải lên. |
| Detailed Description | Giải thích rõ ràng về những gì Skill thực hiện, các trường hợp sử dụng mục tiêu và giá trị mà Skill mang lại cho nhà quảng cáo. |
| Version | Số phiên bản theo định dạng ngữ nghĩa (SemVer) cho bản phát hành này (ví dụ: 1.0.0). |
| Skill File Upload | Tệp Skill dạng .zip đã chuẩn bị của bạn. Xem [Prepare an eligible Skill file](https://business-api.tiktok.com/portal/docs/get-started-for-skills-management/v1.3#item-link-Prepare%20an%20eligible%20Skill%20file) để biết các yêu cầu định dạng. |
| Skill Category | Danh mục chức năng mô tả phù hợp nhất cho Skill của bạn. |
| Industry | Ngành hàng mà Skill của bạn được thiết kế để phục vụ. |
| Showcase prompts | Các câu lệnh mẫu (prompts) minh họa cách nhà quảng cáo có thể gọi và sử dụng Skill của bạn. |
| Developer Contact Email | Địa chỉ email để đội ngũ TikTok có thể liên hệ với bạn khi cần hỗ trợ hoặc giải đáp. |
| Legal Disclaimer / Privacy Policy | Các liên kết dẫn đến tài liệu tuyên bố miễn trừ trách nhiệm pháp lý và chính sách quyền riêng tư của bạn. |
| Does this skill require API key or MCP from a third-party service? | Tuyên bố xác nhận xem Skill của bạn có yêu cầu API key hoặc máy chủ MCP từ dịch vụ bên thứ ba hay không. |
| Provide the testing account information or API key | (Bắt buộc nếu trả lời "Có" cho câu hỏi về phụ thuộc bên thứ ba ở trên) <br> Thông tin đăng nhập tài khoản thử nghiệm hoặc API key giúp quản trị viên TikTok đánh giá Skill trong quá trình xét duyệt. Thông tin đăng nhập được mã hóa an toàn và không bao giờ hiển thị trên các trang công khai. |
| Does the MCP/API require any paid subscription to the service? | (Bắt buộc nếu trả lời "Có" cho câu hỏi về phụ thuộc bên thứ ba ở trên) <br> Tuyên bố xác nhận xem API hoặc MCP của bên thứ ba có yêu cầu gói đăng ký trả phí hay không. |
| Countries | Các thị trường quốc gia nơi Skill của bạn sẽ được phát hành. |

> [!IMPORTANT]
> Hãy cân nhắc kỹ lưỡng khi đặt tên cho **Skill Name**. Sau khi đã gửi, trường này không thể chỉnh sửa. Nếu muốn đổi tên sau này, bạn buộc phải xóa Skill cũ và tạo một Skill hoàn toàn mới.
> Nếu bạn cung cấp video trình diễn cho Skill qua trường **Screencast Video**, video bắt buộc phải có thuyết minh tiếng Anh hoặc phụ đề tiếng Anh. Các video không sử dụng tiếng Anh sẽ không được chấp nhận.

![Tải lên Skill mới](https://images.ctfassets.net/5jqet0ab9qci/3htQUAbzZokEyVYOKFQLQ8/bf66bc4c2ee0792675cf35595ebd8f7d/Upload_a_new_Skill.png)

![Tải lên Skill mới biểu mẫu](https://images.ctfassets.net/5jqet0ab9qci/3Cr9r2LwnPqwutQ5l1WPXH/a8ed9436ce26b6f7f65f22ebeb37e8b2/Upload_a_new_Skill__2_.png)

![Tải lên Skill mới danh mục](https://images.ctfassets.net/5jqet0ab9qci/6HvBzVkCLLSISS1dGN6wJ4/ad7fbd01a4d7bae71dcd748182cdde3a/Upload_a_new_Skill__3_.png)

![Tải lên Skill mới thông tin pháp lý](https://images.ctfassets.net/5jqet0ab9qci/5eUYaz7NqaHLQeTj3fXbXi/5b66c80059561797c848cb6fc1ff4908/Upload_a_new_Skill__4_.png)

![Tải lên Skill mới hoàn tất](https://images.ctfassets.net/5jqet0ab9qci/273EfTjCysyCMEloOEay0W/f12cef6f09724c5bb0ca71680b1b3f40/Upload_a_new_Skill__5_.png)

3. Lựa chọn tùy chọn xuất bản:
   - **Xuất bản ngay lập tức:** Bật công tắc **Publish to Agentic Hub**. Sau khi được phê duyệt, Skill sẽ tự động xuất bản lên marketplace.
   - **Hoãn xuất bản:** Tắt công tắc **Publish to Agentic Hub**. Skill sẽ được xét duyệt nhưng không xuất bản cho đến khi bạn chủ động kích hoạt thủ công. Xem mục "**Xuất bản Skill đã được phê duyệt**" bên dưới.
4. Đọc kỹ các điều khoản và điều kiện pháp lý, sau đó đánh dấu vào ô đồng ý.
5. Nhấn **Create Skill** để hoàn tất việc gửi.

> [!NOTE]
> Nền tảng không giới hạn số lượng Skill bạn có thể tải lên. Bạn có thể lặp lại quy trình này cho từng Skill mới.

### Tìm hiểu quy trình xét duyệt (Understand the review process)

Sau khi gửi, Skill của bạn sẽ đi vào quy trình xét duyệt. Đội ngũ TikTok sẽ đánh giá Skill về chất lượng, tính tuân thủ chính sách marketplace và độ hoàn thiện về mặt chức năng. Quá trình xét duyệt thường hoàn tất trong vòng **5 đến 7 ngày làm việc**.

Bạn có thể theo dõi tiến trình từ trang **My Agentic Hub** qua cột **Status**:

| Status | Meaning |
|---|---|
| Pending Review | Skill của bạn đang nằm trong hàng đợi xét duyệt và chờ đội ngũ TikTok đánh giá. |
| Approved | Skill của bạn đã vượt qua khâu xét duyệt và đủ điều kiện xuất bản. Xem mục "Xuất bản Skill đã được phê duyệt" bên dưới. |
| Rejected | Quá trình xét duyệt phát hiện các vấn đề cần xử lý. Hãy xem phản hồi và gửi lại. Xem [Resubmit a rejected Skill](https://business-api.tiktok.com/portal/docs/troubleshooting-skills-management/v1.3#item-link-Resubmit%20a%20rejected%20Skill). |
| Published | Skill của bạn đã hoạt động trên Agentic Hub và hiển thị với các nhà quảng cáo. |
| Unpublished | Skill của bạn bị ẩn khỏi mục khám phá. Những người dùng đã cài đặt sẽ thấy trạng thái "unavailable" (không khả dụng). Xem [Control visibility on Agentic Hub](https://business-api.tiktok.com/portal/docs/manage-published-skills/v1.3#item-link-Control%20visibility%20on%20Agentic%20Hub). |

![Kiểm tra cột Status](https://images.ctfassets.net/5jqet0ab9qci/RCUWmi1JGEgchoQVmLn2y/2677fa1eaca3e402dd5799435b3a409d/Check_the_Status_column.png)

### Xuất bản Skill đã được phê duyệt (Publish an approved Skill)

Khi Skill vượt qua xét duyệt, trạng thái của nó sẽ chuyển thành **Approved** — biểu thị Skill đã đáp ứng đầy đủ các tiêu chuẩn chất lượng và tính tuân thủ. Nếu bạn tắt nút **Publish to Agentic Hub** trong lúc tải lên, Skill sẽ ở trạng thái sẵn sàng nhưng chưa xuất bản cho đến khi bạn thực hiện thao tác kích hoạt.

Việc xuất bản sẽ đưa Skill hiển thị công khai tới tất cả các nhà quảng cáo đủ điều kiện trên TikTok for Business Agentic Hub.

**Các bước thực hiện:**

1. Trên trang My Agentic Hub, tìm Skill hiển thị trạng thái **Approved** và nhấn **Manage**.

![Tìm Skill có trạng thái Approved và nhấn Manage](https://images.ctfassets.net/5jqet0ab9qci/4lhUzS4IUEs39kBAiE11dl/980cb3f00a370e1b1c36750163f2a6d2/locate_the_Skill_displaying_an_Approved_status_and_click_Manage.png)

2. Trên trang chi tiết Skill, nhấn **Publish Skill**.

![Nhấn Publish Skill](https://images.ctfassets.net/5jqet0ab9qci/1EfoKoaPdeUYtiI3qtktLF/049aa5ee06366cb9778b737f4318ac4d/click_Publish_Skill.png)

3. Xem lại hộp thoại xác nhận và nhấn **Confirm** để hoàn tất.

![Nhấn Confirm để hoàn tất](https://images.ctfassets.net/5jqet0ab9qci/1TSimO7VjMAmSFul6oarUC/dab24c9ded1e18ba654f2f08a393e779/click_Confirm_to_finalize.png)

4. Skill của bạn hiện đã ở trạng thái **Published** — chính thức hoạt động trên Agentic Hub và hiển thị với các nhà quảng cáo.

### Các bước tiếp theo (Next steps)

**Các hành động bạn có thể thực hiện tiếp theo:**
- [Tải lên phiên bản mới](https://business-api.tiktok.com/portal/docs/manage-published-skills/v1.3#item-link-Upload%20a%20new%20version) để nâng cấp Skill theo thời gian.
- [Chỉnh sửa metadata](https://business-api.tiktok.com/portal/docs/manage-published-skills/v1.3#item-link-Edit%20Skill%20metadata) như mô tả, danh mục hoặc ngành nghề mà không cần xét duyệt lại.
- [Kiểm soát hiển thị](https://business-api.tiktok.com/portal/docs/manage-published-skills/v1.3#item-link-Control%20visibility%20on%20Agentic%20Hub) để tạm thời ẩn Skill khi cần thiết.


## Quản lý Skill đã xuất bản (`Manage published Skills`)
<a id="doc-1869392854803490"></a>
<!-- doc_id: 1869392854803490 -->

> Đường dẫn: Skill and MCP management > Get started with Skill management > Manage published Skills

Khi Skill của bạn đã hoạt động trên Agentic Hub, bạn có thể tiếp tục lặp lại các cải tiến, điều chỉnh siêu dữ liệu (metadata), kiểm soát khả năng hiển thị trên thị trường hoặc xóa hoàn toàn. Phần này hướng dẫn toàn bộ các tác vụ quản lý định kỳ.

### Tải lên phiên bản mới (Upload a new version)

Khi năng lực AI của bạn phát triển, hãy duy trì các Skill đã xuất bản luôn cập nhật bằng cách tải lên các phiên bản mới. Các bản cập nhật phiên bản sẽ trải qua quy trình xét duyệt tiêu chuẩn, nhưng phiên bản đã xuất bản hiện tại của bạn vẫn hoạt động bình thường trong suốt quá trình này, đảm bảo không có thời gian gián đoạn đối với các nhà quảng cáo đang sử dụng Skill.

**Các bước thực hiện:**

1. Trên trang My Agentic Hub, tìm Skill có trạng thái **Published** và nhấn **Manage**.

![Tìm Skill có trạng thái Published và nhấn Manage](https://images.ctfassets.net/5jqet0ab9qci/158Vaq49AgjkYpgBhywaBp/f4b058e46749b569ac39381f345066f1/locate_the_Skill_with_a_Published_status_and_click_Manage.png)

2. Trên trang chi tiết Skill, nhấn **Upload New Version**.

![Nhấn Upload New Version](https://images.ctfassets.net/5jqet0ab9qci/5h4qeTu6tjGtZjE39dwGsi/4cca1c4be1b38ddfec915f11072d7a4b/click_Upload_New_Version.png)

3. Điền vào biểu mẫu tải lên với các trường bắt buộc sau:
- **Detailed Description**: cập nhật để phản ánh những thay đổi trong phiên bản mới.
- **Version**: phải cao hơn phiên bản hiện đang xuất bản (ví dụ nếu phiên bản xuất bản hiện tại là 1.0.0, bạn phải dùng 1.1.0 hoặc cao hơn).
- **Skill File Upload**: tệp Skill đã được cập nhật của bạn.
- **Skill Category**
- **Industry**
- **Showcase prompts**
- **Developer Contact Email**
- **Legal Disclaimer / Privacy Policy**
- **Does this skill require API key or MCP from a third-party service?**
- **Provide the testing account information or API key** (Bắt buộc nếu bạn trả lời "Có" cho câu hỏi phụ thuộc bên thứ ba ở trên)
- **Does the MCP/API require any paid subscription to the service?** (Bắt buộc nếu bạn trả lời "Có" cho câu hỏi phụ thuộc bên thứ ba ở trên)
- **Countries**

> [!IMPORTANT]
> **Skill Name** là trường cố định và không thể thay đổi.
> Nếu bạn cung cấp video trình diễn qua trường **Screencast Video**, hãy chắc chắn video có thuyết minh tiếng Anh hoặc phụ đề tiếng Anh. Video không có tiếng Anh sẽ không được chấp nhận.

![Điền biểu mẫu tải lên với các trường bắt buộc](https://images.ctfassets.net/5jqet0ab9qci/2WDy9N3vYINX4kPKfzCOxF/bbda29404281f2e03703d5a4610304dd/Upload_a_new_version_EN_3.png)

4. Xem lại và chấp nhận các điều khoản và điều kiện.
5. Nhấn **Submit Version** để hoàn tất gửi phiên bản.

![Nhấn Submit Version để hoàn tất](https://images.ctfassets.net/5jqet0ab9qci/1rWqHlSGpeOQRH0wjb1Z1s/53fa834e3e6f3a6f669721dfaa171764/Click_Submit_Version_to_finalize.png)

**Kết quả xét duyệt phiên bản:**

Sau khi gửi, phiên bản mới sẽ vào hàng đợi xét duyệt (thường từ **5 đến 7 ngày làm việc**). Khi quá trình xét duyệt hoàn tất, bạn có thể xem kết quả trên trang chi tiết Skill:
- **Approved:** Phiên bản mới sẽ tự động thay thế phiên bản cũ.
- **Rejected:** Phiên bản hiện đang xuất bản vẫn tiếp tục hoạt động mà không bị ảnh hưởng. Phiên bản mới hiển thị trạng thái **Rejected** trên trang chi tiết cùng với phản hồi từ người xét duyệt. Xem [Handle a rejected version update](https://business-api.tiktok.com/portal/docs/troubleshooting-skills-management/v1.3#item-link-Handle%20a%20rejected%20version%20update) để biết các bước khắc phục.

![Phiên bản mới hiển thị trạng thái Rejected](https://images.ctfassets.net/5jqet0ab9qci/4zeTbjaLM4Sx80ZX0XqOmz/28a98ae40af561a3d6a807e040075934/The_new_version_shows_a_Rejected_status.png)

### Chỉnh sửa metadata của Skill (Edit Skill metadata)

Chỉnh sửa siêu dữ liệu của Skill để giữ thông tin luôn chính xác và phân loại hợp lý mà không cần phải trải qua chu kỳ xét duyệt mới. Các chỉnh sửa metadata có hiệu lực ngay lập tức sau khi xác nhận, giúp danh sách Skill của bạn luôn được cập nhật dễ dàng.

**Các trường có thể chỉnh sửa:**

| Field | When to update |
|---|---|
| Detailed Description | Tinh chỉnh thông điệp, nêu bật các tính năng mới hoặc nâng cao độ rõ ràng dựa trên phản hồi của nhà quảng cáo. |
| Skill Category | Phân loại lại Skill nếu chức năng chính có sự thay đổi hoặc khi có danh mục phù hợp hơn. |
| Industry | Điều chỉnh ngành hàng mục tiêu khi bạn mở rộng hoặc thu hẹp định hướng phục vụ của Skill. |

> [!NOTE]
> Bạn có thể chỉnh sửa Skill bất kể trạng thái hiện tại là gì (Pending Review, Approved, Rejected, Published hoặc Unpublished). Để sửa các trường khác như tệp Skill, số phiên bản hoặc Skill Name, bạn cần tải lên phiên bản mới hoặc xóa đi và tạo lại Skill.

**Các bước thực hiện:**

1. Trên trang My Agentic Hub, tìm Skill bạn muốn chỉnh sửa và nhấn **Manage**.

![Tìm Skill muốn sửa và nhấn Manage](https://images.ctfassets.net/5jqet0ab9qci/jHKOet4hGJmi6U5zb1955/0bf9c8e40afddb70b7e095a249535d38/locate_the_Skill_you_want_to_edit_and_click_Manage.png)

2. Trên trang chi tiết Skill, nhấn **Edit**.

![Nhấn Edit](https://images.ctfassets.net/5jqet0ab9qci/2ABtjmAaN5v7ewDH8UTgK6/883175f6f1459507834bb9beb0e14972/click_Edit.png)

3. Cập nhật các trường mong muốn (Detailed Description, Skill Category và Industry), sau đó nhấn **Confirm**.

![Nhấn Confirm](https://images.ctfassets.net/5jqet0ab9qci/6qdA1KFTXdycHy3kpalgxV/352aa03d41914c8c04e3cdf551b26f91/click_Confirm.png)

4. Các thay đổi của bạn được lưu và có hiệu lực ngay lập tức. Không yêu cầu xét duyệt lại.

![Thay đổi được lưu và có hiệu lực ngay](https://images.ctfassets.net/5jqet0ab9qci/306wcdFWxPeKsULiBQ5owi/f04795918270059046303a614f0f8b9d/Your_changes_are_saved_and_take_effect_immediately.png)

### Kiểm soát hiển thị trên Agentic Hub (Control visibility on Agentic Hub)

Quản lý sự hiện diện của Skill trên thị trường bằng công tắc chuyển đổi chế độ hiển thị (visibility toggle). Tính năng này cho phép bạn tạm thời ẩn Skill khỏi marketplace Agentic Hub mà không cần xóa, bảo toàn toàn bộ cấu hình, lịch sử xét duyệt và lượng người dùng đã cài đặt để sẵn sàng hiển thị lại khi cần.

**Khi nào nên dùng công tắc hiển thị:**
- **Bảo trì theo kế hoạch:** Ẩn Skill trong khi triển khai các thay đổi có khả năng gây lỗi (breaking changes), sau đó bật lại khi hệ thống ổn định.
- **Chiến dịch theo mùa vụ:** Tạm thời ẩn các Skill dành riêng cho ngành hàng ngoài các khoảng thời gian cao điểm.
- **Tạm dừng do tuân thủ:** Nhanh chóng rút Skill khỏi các trang khám phá trong khi giải quyết các thắc mắc về chính sách hoặc quy định.
- **Chuẩn bị trước khi phát hành:** Tắt khả năng hiển thị đối với Skill đã được phê duyệt nếu bạn chưa sẵn sàng quảng bá công khai.

**Các trạng thái hiển thị (Visibility states):**

| State | Discovery behavior | Existing installs |
|---|---|---|
| Available (on) | Xuất hiện trên các trang Discovery và More Skills. Các nhà quảng cáo có thể tìm thấy và truy cập. | Hoạt động đầy đủ chức năng. |
| Hidden (off) | Bị gỡ khỏi tất cả các trang khám phá. Không thể tìm kiếm bởi các nhà quảng cáo mới. | Hiển thị trạng thái "unpublished". Chức năng có thể bị giới hạn. |

**Các bước thực hiện:**

1. Trên trang My Agentic Hub, tìm Skill có trạng thái **Approved** hoặc **Published** và nhấn **Manage**.

![Tìm Skill có trạng thái Approved hoặc Published và nhấn Manage](https://images.ctfassets.net/5jqet0ab9qci/6PuBnn1Pc9lq4m70ivnKuN/75b3eae3d4daed6128d0bd35dc464ccb/locate_a_Skill_with_an_Approved_or_Published_status_and_click_Manage.png)

2. Trên trang chi tiết Skill, điều chỉnh thiết lập **Toggle Visibility**:
- Đặt thành **on** để Skill hiển thị và có thể truy cập trên Agentic Hub.
- Đặt thành **off** để ẩn Skill khỏi tất cả các trang khám phá.

![Điều chỉnh thiết lập Toggle Visibility](https://images.ctfassets.net/5jqet0ab9qci/3lm2Cyqn6WF1GNQmNT2UnN/98639bfefa659bf18b093caddf664fe9/adjust_the_Toggle_Visibility_setting.png)

3. Xác minh trạng thái đã cập nhật trên trang My Agentic Hub: Cột **Visibility** sẽ hiển thị **Available** (hiển thị) hoặc **Hidden** (không hiển thị).

> [!NOTE]
> Thay đổi trạng thái hiển thị có hiệu lực ngay lập tức và không cần xét duyệt lại. Bạn có thể bật tắt chế độ hiển thị bất kỳ lúc nào khi cần.

### Xóa Skill (Delete a Skill)

Xóa vĩnh viễn một Skill khi bạn cần ngừng cung cấp giải pháp hoàn toàn. Các lý do phổ biến bao gồm ngừng phát triển sản phẩm, tái định vị thương hiệu với một Skill Name mới, hoặc xóa một bản thử nghiệm không còn cần thiết.

> [!IMPORTANT]
> Thao tác xóa là vĩnh viễn và không thể khôi phục. Khi đã xóa:
> • Skill sẽ bị xóa hoàn toàn khỏi tài khoản của bạn.
> • Những nhà quảng cáo đã cài đặt Skill sẽ mất quyền truy cập ngay lập tức.
> • Bạn không thể phục hồi hoặc khôi phục lại Skill đã xóa.
> Nếu bạn chỉ muốn tạm thời gỡ Skill khỏi marketplace mà không xóa bỏ dữ liệu, hãy sử dụng công tắc hiển thị ở mục **"Kiểm soát hiển thị trên Agentic Hub"** ở trên.

**Các bước thực hiện:**

1. Trên trang My Agentic Hub, tìm Skill bạn muốn xóa và nhấn **Manage**.

![Tìm Skill muốn xóa và nhấn Manage](https://images.ctfassets.net/5jqet0ab9qci/6xf8mCDWviarg01vhSESzC/3eecda3de73f97fbb37b17971ed35744/locate_the_Skill_you_want_to_delete_and_click_Manage.png)

2. Trên trang chi tiết Skill, nhấn **Delete Skill**.

![Nhấn Delete Skill](https://images.ctfassets.net/5jqet0ab9qci/6jB5clp3IaAKTn1CWGdko3/855912dce576be8cc290eb626f277231/click_Delete_Skill.png)

3. Trong hộp thoại xác nhận, nhấn **Confirm** để xóa vĩnh viễn Skill.

![Nhấn Confirm để xóa vĩnh viễn](https://images.ctfassets.net/5jqet0ab9qci/4PZEXrT40SSXMV2AFhWgC2/3ee252811795bf2ad0f1b9d28933d464/click_Confirm_to_permanently_delete_the_Skill.png)

4. Skill đã được xóa vĩnh viễn và không còn xuất hiện trên trang My Agentic Hub nữa.

## Xử lý sự cố với Skill (`Troubleshoot Skill issues`)
<a id="doc-1869392857565186"></a>
<!-- doc_id: 1869392857565186 -->

> Đường dẫn: Skill and MCP management > Get started with Skill management > Troubleshoot Skill issues

Bài viết này bao quát các quy trình xử lý và khắc phục đối với các sự cố thường gặp trong vòng đời của Skill.

### Gửi lại Skill bị từ chối (Resubmit a rejected Skill)

Nếu Skill của bạn bị từ chối trong quá trình xét duyệt ban đầu, đội ngũ TikTok sẽ cung cấp phản hồi cụ thể, rõ ràng giải thích nguyên nhân. Hãy xử lý các điểm phản hồi, cập nhật Skill và gửi lại cho một chu kỳ đánh giá mới. Việc giải quyết triệt để tất cả các vấn đề được nêu sẽ giảm thiểu nguy cơ tiếp tục bị từ chối.

**Các bước thực hiện:**

1. Trên trang My Agentic Hub, tìm Skill hiển thị trạng thái **Rejected** và nhấn **Manage**.

![Tìm Skill hiển thị trạng thái Rejected và nhấn Manage](https://images.ctfassets.net/5jqet0ab9qci/35Zlfya2uYfSpvFRKpd6QR/6d35a6449bd9c4cd9e35cb28f472067d/locate_the_Skill_displaying_a_Rejected_status_and_click_Manage.png)

2. Trên trang chi tiết Skill, xem xét kỹ lưỡng các lý do từ chối do đội ngũ xét duyệt TikTok cung cấp. Mỗi phản hồi từ chối đều đi kèm thông tin chi tiết cụ thể.

![Xem xét kỹ lưỡng lý do từ chối](https://images.ctfassets.net/5jqet0ab9qci/2i2CAJyh6LALi7iwDQR1SU/2ee7042b21a8890028c2281aa4346ce0/carefully_review_the_rejection_reasons.png)

3. Nhấn **Resubmit for Review** để mở lại biểu mẫu tải lên.
4. Cập nhật các trường liên quan để khắc phục các phản hồi. Tất cả các trường sau đều có thể chỉnh sửa:
- **Detailed Description**
- **Version**
- **Skill File Upload**
- **Skill Category**
- **Industry**
- **Showcase prompts**
- **Developer Contact Email**
- **Legal Disclaimer / Privacy Policy**
- **Countries**

> [!IMPORTANT]
> Trường **Skill Name** là vĩnh viễn và không thể chỉnh sửa sau lần tải lên ban đầu. Nếu lý do từ chối liên quan đến tên Skill của bạn, bạn phải xóa Skill đó và tạo một Skill mới với tên mong muốn. Xem [Upload a new Skill](https://business-api.tiktok.com/portal/docs/upload-and-publish-skills/v1.3#item-link-Upload%20a%20new%20Skill).

![Cập nhật các trường thông tin liên quan](https://images.ctfassets.net/5jqet0ab9qci/3ktRIP7VOnW04s7WQvB2bq/2887a26457852b4e6ba4f9fcff175dbd/Resubmit_a_rejected_Skill_EN_3.png)

5. Xem lại và chấp nhận các điều khoản và điều kiện.
6. Nhấn **Submit Version** để hoàn tất việc gửi lại.

![Nhấn Submit Version để gửi lại](https://images.ctfassets.net/5jqet0ab9qci/6LgyRQxgDFZoPWfCC2hJD0/6df15bd4cdd8f5357f3fcf8b02496a43/Click_Submit_Version_to_finalize_your_resubmission..png)

**Điều gì xảy ra tiếp theo:**

Skill của bạn sẽ vào lại hàng đợi xét duyệt. Quá trình xét duyệt thường hoàn tất trong vòng **5 đến 7 ngày làm việc**. Theo dõi trạng thái từ trang **My Agentic Hub**. Nếu Skill được chấp thuận, bạn có thể xuất bản ngay lập tức hoặc dời lại sau.

### Xử lý bản cập nhật phiên bản bị từ chối (Handle a rejected version update)

Khi bạn tải lên một phiên bản mới cho một Skill đã xuất bản và phiên bản mới đó bị từ chối, phiên bản đã xuất bản hiện tại của bạn vẫn hoạt động bình thường mà không bị ảnh hưởng. Trải nghiệm của nhà quảng cáo sẽ không bị gián đoạn.

**Cách nhận biết bản cập nhật phiên bản bị từ chối:**
- Trên trang My Agentic Hub, Skill của bạn tiếp tục hiển thị trạng thái **Published** (do phiên bản gốc vẫn đang hoạt động).

![Skill tiếp tục hiển thị trạng thái Published](https://images.ctfassets.net/5jqet0ab9qci/4wCxsELIJ7QnFQLGiwvbhR/ef8c588fadcbf177544b65021f2cdd4b/your_Skill_continues_to_display_a_Published_status.png)

- Trên trang chi tiết Skill, phiên bản mới hiển thị trạng thái **Rejected** cùng với phản hồi từ người xét duyệt.

![Phiên bản mới hiển thị trạng thái Rejected kèm phản hồi](https://images.ctfassets.net/5jqet0ab9qci/73xFB72sZHAKpKlijiF5ws/7237a1692b64fb1f6ee23fc899c7c959/the_new_version_displays_a_Rejected_status.png)

**Các bước khắc phục:**

1. Trên trang My Agentic Hub, tìm Skill và nhấn **Manage**.
2. Trên trang chi tiết Skill, xem lại phản hồi từ chối cho phiên bản mới.
3. Nhấn **Resubmit for Review** để mở lại biểu mẫu tải lên.

![Nhấn Resubmit for Review để mở lại biểu mẫu](https://images.ctfassets.net/5jqet0ab9qci/Khmb4nwUHrbeY3eMuKOSR/021b969e4373f6052492b57486b0870a/Click_Resubmit_for_Review_to_re-open_the_upload_form.png)

4. Khắc phục các vấn đề đã nêu bằng cách cập nhật các trường liên quan:
- **Detailed Description**
- **Version**: phải luôn cao hơn phiên bản hiện đang xuất bản
- **Skill File Upload**
- **Skill Category**
- **Industry**
- **Showcase prompts**
- **Developer Contact Email**
- **Legal Disclaimer / Privacy Policy**
- **Countries**
5. Chấp nhận các điều khoản và điều kiện.
6. Nhấn **Submit Version** để gửi lại.

Sau khi gửi, phiên bản mới sẽ vào hàng đợi xét duyệt (thường từ **5 đến 7 ngày làm việc**).

## Bắt đầu với quản lý máy chủ MCP (`Get started with MCP server management`)
<a id="doc-1879106319214594"></a>
<!-- doc_id: 1879106319214594 -->

> Đường dẫn: Skill and MCP management > Get started with MCP server management

Bài viết này phác thảo các nội dung bạn cần chuẩn bị để đảm bảo quá trình đăng ký máy chủ Model Context Protocol (MCP) trên cổng nhà phát triển diễn ra suôn sẻ và thuận lợi.

### Điều kiện tiên quyết (Prerequisites)

Trước khi có thể đăng ký các máy chủ MCP trên cổng TikTok for Business Developers, bạn cần:
1. [Tạo tài khoản TikTok for Business](../04-get-started/bat-dau.md#doc-1738855099573250): Cung cấp quyền truy cập vào hệ sinh thái TikTok for Business.
2. [Đăng ký làm nhà phát triển](../04-get-started/bat-dau.md#doc-1738855176671234): Mở khóa phân hệ **My Agentic Hub** và tính năng đăng ký máy chủ MCP.

> [!NOTE]
> Nếu bạn đã từng sử dụng bất kỳ endpoint nào của TikTok API for Business trước đây, bạn đã đáp ứng cả hai điều kiện tiên quyết và có thể chuyển thẳng sang bước chuẩn bị hạ tầng cho máy chủ MCP.

### Chuẩn bị hạ tầng máy chủ MCP của bạn (Prepare your MCP server infrastructure)

Để tránh chậm trễ trong quá trình xét duyệt, chúng tôi đặc biệt khuyến nghị bạn chuẩn bị sẵn sàng bốn thành phần sau trước khi bắt đầu điền biểu mẫu đăng ký:

| Category | What you need | Action required |
|---|---|---|
| Endpoint and network configuration | Một URL máy chủ MCP từ xa sử dụng giao thức truyền tải Streamable HTTP. | Đảm bảo bạn đã thiết lập URL máy chủ MCP từ xa sử dụng giao thức truyền tải Streamable HTTP transport. |
| Tools configuration CSV | Một tệp CSV hoàn chỉnh ánh xạ tất cả các công cụ mà máy chủ của bạn cung cấp. Tải xuống tệp mẫu chính thức [Tools Configuration Template](https://bytedance.my.larkoffice.com/sheets/AIgpsEGB8hPxbmt1tO0mWtC4yHh). | Đưa vào đầy đủ các thông tin sau cho từng công cụ đơn lẻ: <br> • `tool_name` và `tool_signature` chính xác (ví dụ: `get_order_summary(store_id: string)`). <br> • Một `display_title` rõ ràng và một `description` dễ hiểu cho con người. <br> • Trường `safety_annotation`, bắt buộc phải được viết chính xác là `readOnlyHint`, `writeHint` hoặc `destructiveHint`. <br> • Một `example_prompt` và `expected_tool_sequence`. |
| Authentication setup | Quyết định dứt khoát về cách máy chủ xử lý bảo mật người dùng. | • Nếu các công cụ chỉ cung cấp dữ liệu công khai, hãy chọn "No authentication". <br> • Nếu các công cụ truy cập dữ liệu của nhà quảng cáo cụ thể, hãy thiết lập OAuth 2.0/2.1 với PKCE. Giữ Authorization URL luôn sẵn sàng vì trường này là bắt buộc trong biểu mẫu đăng ký. Ngoài ra, bạn phải đưa URI chuyển hướng của TikTok (https://business.tiktok.com/agentic/oauth/callback) vào danh sách cho phép (allowlist) trong cài đặt nhà cung cấp danh tính của bạn để đảm bảo quá trình bắt tay OAuth thành công. |
| Test account credentials | Tài khoản thử nghiệm chuyên dụng được định cấu hình riêng cho đội ngũ xét duyệt của TikTok. | Tạo môi trường thử nghiệm an toàn chứa dữ liệu mẫu mang tính đại diện. Ghi chép chính xác thông tin đăng nhập và hướng dẫn từng bước để kiểm thử các công cụ. Thông tin xác thực thử nghiệm bị thiếu hoặc không hợp lệ là nguyên nhân phổ biến nhất dẫn đến chậm trễ xét duyệt. |
| Legal and support documentation | • Documentation URL: URL dẫn đến trang tài liệu kỹ thuật chính thức cho máy chủ MCP của bạn. <br> • Privacy policy URL: Liên kết dẫn đến tài liệu chính sách quyền riêng tư cho máy chủ MCP. <br> • Terms of service URL: Liên kết dẫn đến tài liệu điều khoản dịch vụ cho máy chủ MCP. <br> • Support channel: URL hoặc địa chỉ email tới bộ phận hỗ trợ kỹ thuật, diễn đàn cộng đồng hoặc hộp thư hỗ trợ chuyên trách. | • Đảm bảo tài liệu chính thức có thể truy cập công khai và giải thích rõ ràng cách sử dụng các công cụ của máy chủ. <br> • Chính sách quyền riêng tư phải đang hoạt động và mô tả chính xác các quy trình xử lý dữ liệu. <br> • Cung cấp liên kết hợp lệ dẫn đến các điều khoản dịch vụ chi phối việc sử dụng máy chủ MCP. <br> • Thiết lập một kênh hỗ trợ rõ ràng để các nhà quảng cáo có thể liên hệ khi cần trợ giúp kỹ thuật. |

### Các bước tiếp theo (Next steps)

Sau khi hạ tầng máy chủ MCP đã sẵn sàng, hãy chuyển sang bước [Đăng ký máy chủ MCP](skill-va-mcp.md#doc-1879106374962178).


## Đăng ký máy chủ MCP (`Register MCP servers`)
<a id="doc-1879106374962178"></a>
<!-- doc_id: 1879106374962178 -->

> Đường dẫn: Skill and MCP management > Get started with MCP server management > Register MCP servers

Bài viết này bao quát toàn bộ quy trình từ lúc đăng ký một máy chủ MCP mới cho đến khi xuất bản trực tiếp trên Agentic Hub.

### Điều hướng đến My Agentic Hub (Navigate to My Agentic Hub)

Tất cả các tác vụ quản lý máy chủ MCP đều bắt đầu từ trang **My Agentic Hub**. Để truy cập:

1. Truy cập [cổng TikTok for Business Developers](https://business-api.tiktok.com/portal) và nhấn **Log in** ở góc trên bên phải.

![Nhấn Log in ở góc trên bên phải](https://images.ctfassets.net/5jqet0ab9qci/2EjQ1uz4t9uaoueIej0FLb/3f7fc70471c35aba30f68f36b5520a35/WnUib8PjXo4BlxxIMbdmpPZOyNd.png)

2. Nhấn vào **My Agentic Hub** ở thanh điều hướng trên cùng bên phải để mở trang quản lý máy chủ MCP.

![Nhấn My Agentic Hub ở thanh điều hướng](https://images.ctfassets.net/5jqet0ab9qci/5dr7cAwmjRCTPnypjpyoxL/a24a2563461a600a0e11dca2e06916e4/DhshbO9vKoS1eoxdf4dmpmBryKT.png)

> [!NOTE]
> Tất cả các quy trình trong tài liệu này đều giả định rằng bạn đã đăng nhập và đang xem trang My Agentic Hub. Các bước điều hướng này sẽ không được nhắc lại trong các phần tiếp theo.

### Đăng ký máy chủ MCP mới (Register a new MCP server)

Đăng ký máy chủ MCP của bạn để quản lý tập trung, tối ưu hóa quy trình xét duyệt và phân phối các giải pháp đến nhà quảng cáo thông qua TikTok for Business Agentic Hub.

**Các bước thực hiện:**

1. Trên trang My Agentic Hub, nhấn **Upload New** ở góc trên cùng bên trái và chọn **Register MCP server**.

![Nhấn Upload New](https://images.ctfassets.net/5jqet0ab9qci/1ZJUL3XMSH8NEmO96Am2dM/4655b9255e33d08cf97e1d4d219088e3/Pt6WbNbHqoUMUhxu9M2m5H9fykc.png)

![Chọn Register MCP server](https://images.ctfassets.net/5jqet0ab9qci/31pEH3u6uOFkEMAnryvpBD/a1c2041e38ce4037c5fe29b120e3280c/LMuxbEtproev1AxUG6EmdgQvyPo.png)

2. Điền đầy đủ thông tin vào biểu mẫu tải lên với các trường bắt buộc sau:

> [!IMPORTANT]
> Hãy cân nhắc kỹ lưỡng khi chọn **Server name**. Sau khi gửi, trường này không thể chỉnh sửa. Nếu muốn đổi tên sau này, bạn bắt buộc phải xóa máy chủ MCP và đăng ký một máy chủ mới.

#### Biểu mẫu đăng ký máy chủ MCP (Registration form fields)

**1. Submission & attestation (Thông tin gửi & Chứng nhận)**
- **Submitter email**: Địa chỉ email chính được sử dụng cho tất cả các liên lạc liên quan đến bản đăng ký này (ví dụ: `name@partner.com`).
- **I am authorized to submit this information on behalf of my company and am the designated point of contact for updates or modifications.**: Xác nhận bắt buộc rằng bạn là đại diện kỹ thuật hoặc sản phẩm chính thức được ủy quyền đại diện cho tổ chức của mình trong suốt quá trình xét duyệt.
- **I agree to the TikTok for Business Agentic Hub Terms of Service and the processing of the submitted information.**: Xác nhận bắt buộc rằng bản đăng ký của bạn tuân thủ đầy đủ **Điều khoản dịch vụ của Agentic Hub** và chấp thuận việc xử lý các thông tin đã gửi.

**2. Company information (Thông tin công ty)**
- **Primary contact name**: Họ tên cá nhân được chỉ định làm đầu mối liên hệ cho bản đăng ký này.
- **Primary contact email**: Địa chỉ email của người liên hệ chính. Email này sẽ hiển thị công khai trên danh sách Agentic Hub dưới dạng thông tin liên hệ của nhà phát triển.
- **Secondary technical contact name**: Người liên hệ kỹ thuật dự phòng được chỉ định trong trường hợp không thể liên lạc với người liên hệ chính.
- **Secondary technical contact email**: Địa chỉ email của người liên hệ dự phòng. Email này phải khác với email liên hệ chính.

**3. Server identity & listing copy (Danh tính máy chủ & Nội dung hiển thị)**
- **Server name**: Tên hiển thị của máy chủ MCP trên Agentic Hub. Hãy đảm bảo tên tập trung vào thương hiệu và tránh dùng các từ trùng lặp như "MCP" hoặc "Server".
- **Version (SemVer)**: Phiên bản ngữ nghĩa ban đầu của máy chủ MCP theo định dạng X.Y.Z (ví dụ: `1.0.0`), dùng để theo dõi phiên bản nghiêm ngặt.
- **Server logo**: Hình ảnh biểu trưng (logo) chính thức cho máy chủ MCP. Tỷ lệ khung hình khuyến nghị: 1:1 (vuông). Định dạng tệp: ưu tiên SVG, chấp nhận PNG (dung lượng tối đa 10 MB).
- **Screenshots**: Ảnh chụp màn hình làm nổi bật giá trị mà máy chủ MCP mang lại (như sơ đồ kiến trúc, luồng dữ liệu hoặc hình ảnh giới thiệu). Cho phép tối đa 3 ảnh. Định dạng hỗ trợ: .PNG/.JPG/.WebP. Dung lượng tối đa mỗi ảnh: 10 MB.
- **Tagline**: Câu định vị giá trị ngắn gọn, súc tích chỉ trong một dòng cho người dùng biết ngay máy chủ của bạn làm được những gì. Giới hạn độ dài: tối đa 55 ký tự. Thông tin này xuất hiện trên danh sách Agentic Hub dưới dạng phụ đề thẻ (card subtitle).
- **Short description**: Bản tóm tắt ngắn nêu bật các trường hợp sử dụng cốt lõi và lợi ích. Giới hạn độ dài: 100 từ; độ dài yêu cầu: từ 50 đến 100 từ. Thông tin này xuất hiện trên Agentic Hub ở phần thân thẻ (card body) và trang chi tiết.
- **Long description**: Bản mô tả chi tiết, toàn diện về năng lực của máy chủ, danh sách công cụ hỗ trợ và các điều kiện tiên quyết. Không giới hạn độ dài. Xuất hiện trên trang chi tiết của Agentic Hub.
- **Category**: Danh mục chức năng mô tả phù hợp nhất máy chủ MCP của bạn.
- **Industries**: Các ngành hàng mà máy chủ MCP được thiết kế để phục vụ.
- **Countries / availability**: Các thị trường nơi bạn muốn cung cấp máy chủ MCP. Danh sách trên Agentic Hub sẽ bị ẩn đối với người dùng ngoài các khu vực này.
- **Documentation URL**: Đường dẫn URL trực tiếp đến tài liệu kỹ thuật chính thức của máy chủ MCP.
- **Requires paid subscription?**: Làm rõ việc người dùng có cần gói tài khoản trả phí, mã bản quyền hoặc cấp tài khoản đặc thù trên nền tảng của bạn để sử dụng thành công máy chủ MCP hay không.

**4. Endpoint & transport (Endpoint & Phương thức truyền tải)**
- **Remote MCP server URL**: Đường dẫn URL máy chủ từ xa đang hoạt động, có thể truy cập công khai nơi máy chủ của bạn được lưu trữ. Chỉ cung cấp duy nhất một URL cho mỗi lần đăng ký.
- **Transport: Streamable HTTP is supported — the server URL is verified as a Streamable HTTP endpoint at pre-check.**: Xác nhận hạ tầng của bạn triển khai đúng giao thức HTTP streaming theo yêu cầu của đặc tả kỹ thuật MCP.
- **Our infrastructure accepts inbound requests from TikTok's published gateway egress IP ranges.**: Xác nhận bạn đồng ý cấu hình WAF (Web Application Firewall) hoặc nhóm bảo mật để cho phép lưu lượng truy cập từ dải địa chỉ IP cổng ra chính thức của TikTok trong tương lai (không chặn nền tảng qua tường lửa).

**5. Capability declaration (Khai báo tính năng)**
- **Tools — at least 1 required**: Tệp CSV hoàn chỉnh định nghĩa chữ ký công cụ, tiêu đề, mô tả và chú thích an toàn. Tải xuống tệp mẫu chính thức [Tools Configuration Template](https://bytedance.my.larkoffice.com/sheets/AIgpsEGB8hPxbmt1tO0mWtC4yHh). Tệp phải liệt kê đầy đủ từng công cụ mà máy chủ cung cấp. Quy trình kiểm tra trước (pre-check) sẽ đối chiếu sự khác biệt giữa các tính năng khai báo trong CSV và máy chủ thực tế.
- **Read/Write capability**: Phân loại quyền truy cập cấp cao phù hợp với các chú thích an toàn trong tệp CSV:
  - Nếu `safety_annotation` của tất cả các công cụ là `readOnlyHint`, chọn **Read only**.
  - Nếu `safety_annotation` của tất cả các công cụ là `destructiveHint` hoặc `writeHint`, chọn **Write only**.
  - Nếu `safety_annotation` có sự kết hợp giữa `readOnlyHint` và `destructiveHint`/`writeHint`, chọn **Read + write**.
- **All tools have user-friendly titles and semantic annotations.**: Xác nhận rằng tên công cụ và mô tả đã được tối ưu hóa cho mô hình ngôn ngữ lớn (LLM) hiểu. Các chú thích ngữ nghĩa chất lượng đóng vai trò như các lời nhắc hệ thống (system prompts), giúp AI hiểu chính xác khi nào và làm thế nào để gọi công cụ.
- **Safety annotations are accurately applied to every tool — readOnlyHint or destructiveHint / writeHint on each, not only mutative ones.**: Xác nhận bạn đã gắn cờ chính xác cho từng hành động thay đổi dữ liệu (mutative) và không thay đổi dữ liệu (non-mutative) trên mọi công cụ.
- **Tool specifications conform to MCP guidelines.**: Xác nhận rằng đặc tả công cụ tuân thủ nghiêm ngặt [hướng dẫn chính thức của MCP](https://modelcontextprotocol.io/specification/2025-11-25/server/tools).

**6. Authentication (Xác thực)**
- **Authentication type**: Phương thức xác thực cho máy chủ MCP (yêu cầu OAuth tiêu chuẩn để truy cập dữ liệu người dùng cụ thể, hoặc không yêu cầu xác thực).
- **Dynamic Client Registration (DCR / CIMD)**: (Bắt buộc nếu sử dụng OAuth) Xác nhận máy chủ MCP hỗ trợ Đăng ký máy khách động (Dynamic Client Registration). Điều này cho phép tác nhân tự động đăng ký và lấy OAuth client ID/secret theo chương trình, loại bỏ việc cấu hình thủ công trên cổng nhà phát triển.
- **Authorization URL**: (Bắt buộc nếu sử dụng OAuth) URL ủy quyền nơi người dùng được chuyển hướng để cấp quyền truy cập. Ví dụ: `https://auth.partner.com/oauth/authorize`. URL này phải trỏ về miền công ty đã được xác minh để phòng chống giả mạo (phishing).
- **TikTok's redirect URI (shown in-form) is allowlisted on our OAuth provider: https://business.tiktok.com/agentic/oauth/callback**: (Bắt buộc nếu sử dụng OAuth) Xác nhận bạn đã thêm URI chuyển hướng chính thức của TikTok vào danh sách URI được ủy quyền trong cài đặt nhà cung cấp danh tính, đảm bảo quá trình bắt tay OAuth diễn ra thành công.

**7. Data handling & disclosure (Xử lý & Công bố dữ liệu)**
- **Data handling attestations**: Xác nhận về quy trình quản lý vòng đời dữ liệu. Hãy đánh dấu chọn tất cả các điều khoản áp dụng:
  - Máy chủ chỉ truy cập dữ liệu được người dùng yêu cầu rõ ràng.
  - Không lưu trữ dữ liệu vượt quá yêu cầu của phiên làm việc.
  - Mọi quá trình truyền tải đều được mã hóa an toàn (HTTPS/TLS).
  - Tuân thủ quy định GDPR khi áp dụng.
- **Third-party access**: Tuyên bố về bất kỳ mối quan hệ phụ thuộc truy cập bên thứ ba nào mà máy chủ MCP của bạn yêu cầu.

**8. Review access (Quyền truy cập phục vụ xét duyệt)**
- **Test account credentials**: Thông tin xác thực tài khoản thử nghiệm chuyên dụng được cung cấp an toàn cho đội ngũ xét duyệt TikTok kiểm tra bản đăng ký. **Thông tin xác thực phải bao quát toàn bộ luồng OAuth và từng công cụ đã khai báo. Nếu không, quá trình xét duyệt sẽ bị đình chỉ.**
- **Test account setup instructions**: Hướng dẫn từng bước giải thích cách người xét duyệt đăng nhập, kích hoạt các tính năng cụ thể và điều hướng môi trường chạy thử (staging).
- **The test account includes representative sample data.**: Xác nhận tài khoản thử nghiệm đã có sẵn dữ liệu mẫu mang tính đại diện (như chiến dịch, báo cáo phân tích hoặc tài sản mẫu) để đội ngũ xét duyệt có thể thử nghiệm thành công các luồng đọc/ghi.
- **All declared tools can be exercised with that data.**: Xác nhận không có lỗi về quyền truy cập hay tính năng bị khóa nào ngăn cản đội ngũ xét duyệt kiểm thử toàn diện mọi công cụ được liệt kê trong CSV.

**9. Launch readiness & legal (Pháp lý & Sẵn sàng phát hành)**
- **GA date**: Ngày máy chủ MCP phát hành rộng rãi (General Availability) theo định dạng YYYY-MM-DD.
- **Privacy policy URL**: Đường dẫn trực tiếp đến tài liệu chính sách quyền riêng tư của máy chủ MCP.
- **Terms of service URL**: Đường dẫn trực tiếp đến tài liệu điều khoản dịch vụ của máy chủ MCP.
- **Support channel**: URL hoặc địa chỉ email chuyển hướng người dùng đến bộ phận hỗ trợ kỹ thuật, diễn đàn cộng đồng hoặc hộp thư chuyên trách.

![Thông tin gửi và chứng nhận](https://images.ctfassets.net/5jqet0ab9qci/bZ7jx9txNF1eY5TR4QTSJ/3f23c920a6657774c923f92f712d4368/LZoNbjmOxonAW6x1sOemP2tyyVF.png)

![Thông tin công ty](https://images.ctfassets.net/5jqet0ab9qci/1ZJUL3XMSH8NEmO96Am2dM/4655b9255e33d08cf97e1d4d219088e3/Pt6WbNbHqoUMUhxu9M2m5H9fykc.png)

![Thông tin máy chủ 1](https://images.ctfassets.net/5jqet0ab9qci/54I05auACoC9AlkkzjzINh/ce7dc23f2461314e364fd7bb20ac2546/Server_info_1.png)

![Thông tin máy chủ 2](https://images.ctfassets.net/5jqet0ab9qci/3vCQGB9p2MvMO282HYHXMM/f4c4a2bfeb680fb4dd8d0d735f9549ae/Server_info_2.png)

![Endpoint và truyền tải](https://images.ctfassets.net/5jqet0ab9qci/54VgMKRLnzRTF0hsU09j2D/8b7363a1a3e937fc7b41fd7f884b935f/Endpoint___transport.png)

![Khai báo tính năng](https://images.ctfassets.net/5jqet0ab9qci/1tn469gouQGoKPh6w021k7/d5c4e843ba46f12d4c8705e3d6c49359/Capability_declaration.png)

![Xử lý dữ liệu và công bố](https://images.ctfassets.net/5jqet0ab9qci/fCbZQ7eG2brEHbT3YmSLw/c7799c64ac6f261ee377a4db4ff9d7b4/Data_handling___disclosure.png)

![Quyền truy cập xét duyệt](https://images.ctfassets.net/5jqet0ab9qci/5lZqCQ8FznjyzsurixavGt/3637815d1068312d8eea40134c5a1359/Review_access.png)

3. Nhấn **Submit for review** để hoàn tất việc gửi đăng ký.

> [!NOTE]
> Không có giới hạn về số lượng máy chủ MCP bạn có thể đăng ký. Bạn có thể lặp lại quy trình này cho từng máy chủ MCP mới.

![Nhấn Submit Version](https://images.ctfassets.net/5jqet0ab9qci/2AYvFncEpkr8aYSgRAXAu1/f9e2ed5b659421df425d4d47aa5d5d5a/Click_Submit_Version.png)

### Tìm hiểu quy trình xét duyệt (Understand the review process)

Sau khi gửi, máy chủ MCP của bạn sẽ đi vào quy trình xét duyệt. Đội ngũ TikTok sẽ đánh giá máy chủ về chất lượng, tính tuân thủ chính sách marketplace và độ hoàn thiện chức năng.

Trong quá trình này, đội ngũ xét duyệt sẽ:
- Xác minh xem URL máy chủ có thể tiếp cận được hay không.
- Thực hiện chạy thử nghiệm thiết lập OAuth để đảm bảo người dùng có thể ủy quyền thành công.
- Xác thực tệp CSV để khẳng định mọi công cụ đều được chú thích đúng quy chuẩn.
- Sử dụng tài khoản thử nghiệm của bạn để kiểm chứng các công cụ hoạt động chính xác với dữ liệu mẫu.

Theo dõi tiến trình từ trang **My Agentic Hub** qua cột **Status**:

| Status | Meaning |
|---|---|
| Pending Review | Máy chủ MCP của bạn đang ở trong hàng đợi xét duyệt và chờ đội ngũ TikTok đánh giá. |
| Published | Máy chủ MCP của bạn đã vượt qua khâu xét duyệt và đã được xuất bản chính thức. |
| Rejected | Quá trình xét duyệt phát hiện các vấn đề cần xử lý. Hãy xem phản hồi và gửi lại. Xem [Resubmit a rejected MCP server](https://business-api.tiktok.com/portal/docs/troubleshoot-mcp-server-issues/v1.3#anchor-0-1). |

![Theo dõi tiến trình qua cột Status](https://images.ctfassets.net/5jqet0ab9qci/1FABlub6i6G106jeolinkr/0afc7642daf61b5ed21a2eb9e692f1ee/Monitor_progress_by_checking_the_Status_column.png)

### Các bước tiếp theo (Next steps)

**Các thao tác bạn có thể thực hiện tiếp theo:**
- [Tải lên phiên bản mới](https://business-api.tiktok.com/portal/docs/manage-published-mcp-servers/v1.3#anchor-0-1) để nâng cấp máy chủ MCP theo thời gian.
- [Kiểm soát hiển thị](https://business-api.tiktok.com/portal/docs/manage-published-mcp-servers/v1.3#anchor-0-2) để tạm thời ẩn máy chủ MCP khi cần thiết.
- [Xóa máy chủ MCP](https://business-api.tiktok.com/portal/docs/manage-published-mcp-servers/v1.3#anchor-0-3) nếu bạn muốn loại bỏ hoàn toàn máy chủ MCP khỏi tài khoản.

## Quản lý máy chủ MCP đã xuất bản (`Manage published MCP servers`)
<a id="doc-1879106378631233"></a>
<!-- doc_id: 1879106378631233 -->

> Đường dẫn: Skill and MCP management > Get started with MCP server management > Manage published MCP servers

Khi máy chủ MCP của bạn đã hoạt động trên Agentic Hub, bạn có thể tiếp tục lặp lại các cải tiến, kiểm soát khả năng hiển thị trên thị trường hoặc xóa bỏ hoàn toàn. Phần này hướng dẫn toàn bộ các tác vụ quản lý định kỳ.

### Tải lên phiên bản mới (Upload a new version)

Khi năng lực AI phát triển, hãy duy trì máy chủ MCP đã xuất bản luôn cập nhật bằng cách tải lên các phiên bản mới. Các bản cập nhật phiên bản sẽ trải qua quy trình xét duyệt tiêu chuẩn, nhưng phiên bản đã xuất bản hiện tại của bạn vẫn hoạt động bình thường trong suốt quá trình này, đảm bảo không có thời gian gián đoạn đối với các nhà quảng cáo đang sử dụng máy chủ MCP của bạn.

**Các bước thực hiện:**

1. Trên trang My Agentic Hub, tìm máy chủ MCP có trạng thái **Published** và nhấn **Manage**.

![Tìm máy chủ MCP có trạng thái Published và nhấn Manage](https://images.ctfassets.net/5jqet0ab9qci/aBZyg8AEZkv0wEjEXrUZ9/54b0c0a3f34faec7b349f1e4277c2b6e/locate_a_Skill_with_a_Published_status_and_click_Manage.png)

2. Trên trang chi tiết máy chủ MCP, nhấn **Upload New Manifest**.

![Nhấn Upload New Manifest](https://images.ctfassets.net/5jqet0ab9qci/4QmMEunnExZSUm2UUliRzZ/010dcb9bff0c83d50ff44b7b4aa1aecf/click_Upload_New_Manifest.png)

3. Hoàn thành biểu mẫu tải lên với các thông tin chi tiết mới nhất của bạn.

Đảm bảo số phiên bản mới trong trường **Version (SemVer)** cao hơn phiên bản hiện đang xuất bản. Ví dụ nếu phiên bản hiện tại là 1.0.0, hãy dùng 1.1.0 hoặc cao hơn.

> [!IMPORTANT]
> **Server name** không thể thay đổi trong quá trình cập nhật phiên bản.

![Điền biểu mẫu tải lên 1](https://images.ctfassets.net/5jqet0ab9qci/6tNGZZnl9aM0Mhw4q4jVCT/cf57a9e8d984310f99dc3315c59ba595/Complete_the_upload_form_with_your_latest_details_1.png)

![Điền biểu mẫu tải lên 2](https://images.ctfassets.net/5jqet0ab9qci/6ZZ9dTlUHXTQdVVTbKcJ6f/0d525e39ca70c90fe5918c0c15d564b9/Complete_the_upload_form_with_your_latest_details_2.png)

4. Nhấn **Submit Version** để hoàn tất việc gửi phiên bản.

![Nhấn Submit Version](https://images.ctfassets.net/5jqet0ab9qci/2AYvFncEpkr8aYSgRAXAu1/f9e2ed5b659421df425d4d47aa5d5d5a/Click_Submit_Version.png)

**Kết quả xét duyệt phiên bản:**

Sau khi gửi, phiên bản mới sẽ vào hàng đợi xét duyệt. Khi quá trình hoàn tất, bạn có thể xem kết quả trên trang chi tiết máy chủ MCP:
- **Approved:** Phiên bản mới sẽ tự động thay thế phiên bản cũ.
- **Rejected:** Phiên bản đang xuất bản hiện tại vẫn hoạt động bình thường. Phiên bản mới hiển thị trạng thái **Rejected** trên trang chi tiết máy chủ MCP kèm theo phản hồi của người xét duyệt. Xem [Handle a rejected version update](https://business-api.tiktok.com/portal/docs/troubleshoot-mcp-server-issues/v1.3#anchor-0-2) để biết các bước xử lý.

![Phiên bản mới hiển thị trạng thái Rejected](https://images.ctfassets.net/5jqet0ab9qci/5mhjaOo5qD5mrchu8gQlZG/f48479c7c365b7f1e6dcdc399d7e99f7/The_new_version_shows_a_Rejected_status.png)

### Kiểm soát hiển thị trên Agentic Hub (Control visibility on Agentic Hub)

Quản lý sự hiện diện của máy chủ MCP trên thị trường bằng công tắc chuyển đổi chế độ hiển thị (visibility toggle). Tính năng này cho phép bạn tạm thời ẩn máy chủ MCP khỏi marketplace Agentic Hub mà không cần xóa, bảo toàn toàn bộ cấu hình, lịch sử xét duyệt và lượng người dùng đã cài đặt để sẵn sàng xuất bản lại khi cần.

**Khi nào nên dùng công tắc hiển thị:**
- **Bảo trì theo kế hoạch:** Ẩn máy chủ MCP trong khi triển khai các thay đổi có khả năng gây lỗi, sau đó kích hoạt lại khi hệ thống ổn định.
- **Chiến dịch theo mùa vụ:** Tạm thời ẩn các máy chủ MCP theo ngành hàng cụ thể ngoài các khoảng thời gian cao điểm.
- **Tạm dừng do tuân thủ:** Nhanh chóng rút máy chủ MCP khỏi các trang khám phá trong khi giải quyết các vấn đề về chính sách hoặc quy định.
- **Chuẩn bị trước khi phát hành:** Tắt khả năng hiển thị đối với máy chủ MCP đã được phê duyệt nếu bạn chưa sẵn sàng quảng bá rộng rãi.

**Các trạng thái hiển thị (Visibility states):**

| State | Discovery behavior | Existing installs |
|---|---|---|
| Available (on) | Xuất hiện trên các trang Khám phá (Discovery). Các nhà quảng cáo có thể tìm thấy và truy cập. | Hoạt động đầy đủ chức năng. |
| Hidden (off) | Bị gỡ khỏi tất cả các trang khám phá. Không thể tìm kiếm bởi các nhà quảng cáo mới. | Hiển thị trạng thái "unpublished". Chức năng có thể bị giới hạn. |

**Các bước thực hiện:**

1. Trên trang My Agentic Hub, tìm máy chủ MCP có trạng thái **Published** và nhấn **Manage**.

![Tìm máy chủ MCP có trạng thái Published và nhấn Manage](https://images.ctfassets.net/5jqet0ab9qci/aBZyg8AEZkv0wEjEXrUZ9/54b0c0a3f34faec7b349f1e4277c2b6e/locate_a_Skill_with_a_Published_status_and_click_Manage.png)

2. Trên trang chi tiết máy chủ MCP, điều chỉnh thiết lập **Toggle Visibility**:
- Đặt thành **on** để máy chủ MCP hiển thị và có thể truy cập trên Agentic Hub.
- Đặt thành **off** để ẩn máy chủ MCP khỏi tất cả các trang khám phá.

![Điều chỉnh thiết lập Toggle Visibility](https://images.ctfassets.net/5jqet0ab9qci/2hIyPDGKWiAXEGpblAIUaB/d5ea38792cd7660b6e889a5f8e64cbaf/adjust_the_Toggle_Visibility_setting.png)

3. Xác minh trạng thái đã cập nhật trên trang My Agentic Hub:
- Cột **Visibility** sẽ hiển thị **Available** (hiển thị) hoặc **Hidden** (không hiển thị).

> [!NOTE]
> Thay đổi trạng thái hiển thị có hiệu lực ngay lập tức và không cần xét duyệt lại. Bạn có thể bật tắt chế độ hiển thị bất kỳ lúc nào khi cần.

### Xóa máy chủ MCP (Delete an MCP server)

Xóa vĩnh viễn một máy chủ MCP khi bạn cần ngừng cung cấp dịch vụ hoàn toàn. Các lý do phổ biến bao gồm ngừng phát triển sản phẩm, tái định vị thương hiệu với tên máy chủ MCP mới, hoặc xóa bản thử nghiệm không còn cần thiết.

> [!IMPORTANT]
> Thao tác xóa là vĩnh viễn và không thể đảo ngược. Khi đã xóa:
> • Máy chủ MCP sẽ bị xóa vĩnh viễn khỏi tài khoản của bạn.
> • Những nhà quảng cáo đã cài đặt máy chủ MCP sẽ mất quyền truy cập ngay lập tức.
> • Bạn không thể phục hồi hoặc khôi phục lại máy chủ MCP đã xóa.
> Nếu bạn chỉ muốn tạm thời gỡ máy chủ MCP khỏi marketplace mà không xóa bỏ cấu hình, hãy sử dụng công tắc hiển thị ở mục **"Kiểm soát hiển thị trên Agentic Hub"** ở trên.

**Các bước thực hiện:**

1. Trên trang My Agentic Hub, tìm máy chủ MCP bạn muốn xóa và nhấn **Manage**.

![Tìm máy chủ MCP muốn xóa và nhấn Manage](https://images.ctfassets.net/5jqet0ab9qci/6GO2ei5KOcv9kxBT8iejYj/d293285b4d1cd555086ebd403d2be5dd/locate_the_MCP_server_you_want_to_delete_and_click_Manage.png)

2. Trên trang chi tiết máy chủ MCP, nhấn **Delete Server**.

![Nhấn Delete Server](https://images.ctfassets.net/5jqet0ab9qci/2Htopg6ik8ikcY3IzHDBD1/a6da930bb1a937a30b300b3ff814f700/click_Delete_Server.png)

3. Trong hộp thoại xác nhận, nhấn **Confirm** để xóa vĩnh viễn máy chủ MCP.

![Nhấn Confirm để xóa vĩnh viễn máy chủ MCP](https://images.ctfassets.net/5jqet0ab9qci/4xVwlGLfoDQDFvYZu2HBJj/2385b8e227e567e923587593522dda85/click_Confirm_to_permanently_delete_the_MCP_server.png)

4. Máy chủ MCP đã bị xóa vĩnh viễn và không còn xuất hiện trên trang My Agentic Hub nữa.

## Xử lý sự cố với máy chủ MCP (`Troubleshoot MCP server issues`)
<a id="doc-1879106382373633"></a>
<!-- doc_id: 1879106382373633 -->

> Đường dẫn: Skill and MCP management > Get started with MCP server management > Troubleshoot MCP server issues

Phần này bao quát các quy trình xử lý và khắc phục đối với các sự cố thường gặp trong vòng đời đăng ký máy chủ MCP.

### Gửi lại MCP server bị từ chối (Resubmit a rejected MCP server)

Nếu máy chủ MCP của bạn bị từ chối trong quá trình xét duyệt ban đầu, đội ngũ TikTok sẽ cung cấp phản hồi cụ thể, rõ ràng giải thích nguyên nhân. Hãy xử lý các điểm phản hồi, cập nhật máy chủ MCP và gửi lại cho một chu kỳ đánh giá mới. Việc giải quyết triệt để tất cả các vấn đề được nêu sẽ giảm thiểu nguy cơ tiếp tục bị từ chối.

**Các bước thực hiện:**

1. Trên trang My Agentic Hub, tìm máy chủ MCP hiển thị trạng thái **Rejected** và nhấn **Manage**.

![Tìm máy chủ MCP hiển thị trạng thái Rejected và nhấn Manage](https://images.ctfassets.net/5jqet0ab9qci/6Fk04a9Pd2MkxUT1WuSbAm/5a4a8950ff96b7c528323e239a546b5e/locate_the_MCP_server_displaying_a_Rejected_status_and_click_Manage.png)

2. Trên trang chi tiết máy chủ MCP, xem xét cẩn thận các lý do từ chối do đội ngũ xét duyệt TikTok cung cấp. Mỗi phản hồi từ chối đều đi kèm thông tin chi tiết cụ thể.

![Xem xét kỹ lưỡng lý do từ chối](https://images.ctfassets.net/5jqet0ab9qci/69UA2xRhLxLBBNF9OvGSMG/f3a035cdd7d71c20a5339ffaf735ee53/carefully_review_the_rejection_reasons.png)

3. Nhấn **Resubmit for Review** để mở lại biểu mẫu tải lên.
4. Cập nhật các trường thông tin liên quan để khắc phục các phản hồi.

![Cập nhật các trường liên quan](https://images.ctfassets.net/5jqet0ab9qci/6MsyRy4DHGPkYDIL8M1bOV/8e7684a0919d3c3a918226035b52efd4/Update_the_relevant_fields.png)

> [!IMPORTANT]
> Trường **Server name** là cố định vĩnh viễn và không thể chỉnh sửa sau lần tải lên ban đầu. Nếu phản hồi từ chối liên quan đến Server name của bạn, bạn phải xóa máy chủ và đăng ký một máy chủ mới với tên mong muốn. Xem [Register a new MCP server](https://business-api.tiktok.com/portal/docs/register-mcp-servers/v1.3#anchor-0-2).

5. Nhấn **Submit Version** để hoàn tất việc gửi lại.

![Nhấn Submit Version để gửi lại](https://images.ctfassets.net/5jqet0ab9qci/6YMubldABNagC5O0e9xdEA/fa60091dea278ce75963e0342e68c76f/Click_Submit_Version_for_resubmission.png)

**Điều gì xảy ra tiếp theo:**

Máy chủ MCP của bạn sẽ vào lại hàng đợi xét duyệt. Bạn có thể theo dõi trạng thái từ trang **My Agentic Hub**.

### Xử lý bản cập nhật phiên bản bị từ chối (Handle a rejected version update)

Khi bạn tải lên phiên bản mới cho một máy chủ MCP đã xuất bản và phiên bản mới đó bị từ chối, phiên bản đã xuất bản hiện tại của bạn vẫn hoạt động bình thường mà không bị ảnh hưởng. Các nhà quảng cáo sẽ không gặp phải bất kỳ sự gián đoạn nào.

**Cách nhận biết bản cập nhật phiên bản bị từ chối:**
- Trên trang **My Agentic Hub**, máy chủ MCP của bạn tiếp tục hiển thị trạng thái **Published** (do phiên bản gốc vẫn đang hoạt động).

![Máy chủ MCP tiếp tục hiển thị trạng thái Published](https://images.ctfassets.net/5jqet0ab9qci/1RkTl0RqxcBEFt8yCw56BU/dfc740e66de5f67417bf1f52534329bb/your_MCP_server_continues_to_display_a_Published_status.png)

- Trên trang chi tiết máy chủ MCP, phiên bản mới hiển thị trạng thái **Rejected** cùng với phản hồi từ người xét duyệt.

![Phiên bản mới hiển thị trạng thái Rejected](https://images.ctfassets.net/5jqet0ab9qci/5mhjaOo5qD5mrchu8gQlZG/f48479c7c365b7f1e6dcdc399d7e99f7/The_new_version_shows_a_Rejected_status.png)

**Các bước khắc phục:**

1. Trên trang My Agentic Hub, tìm máy chủ MCP và nhấn **Manage**.
2. Trên trang chi tiết máy chủ MCP, xem xét kỹ lưỡng phản hồi từ chối cho phiên bản mới.
3. Nhấn **Resubmit for Review** để mở lại biểu mẫu tải lên.

![Nhấn Resubmit for Review để mở lại biểu mẫu](https://images.ctfassets.net/5jqet0ab9qci/6nLaPVroX941TthO6jvE3E/3d790e2ad8159e171fc271abb7a6c019/Click_Resubmit_for_Review_to_re-open_the_upload_form.png)

4. Khắc phục các vấn đề đã nêu bằng cách cập nhật các trường liên quan.
5. Nhấn **Submit Version** để gửi lại.

Sau khi gửi, phiên bản mới sẽ vào hàng đợi xét duyệt.
