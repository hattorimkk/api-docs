# Hướng dẫn quản lý Audience

Tài liệu này cung cấp hướng dẫn toàn diện về Quản lý Tệp đối tượng (Audience Management) trên TikTok for Business. Tệp đối tượng (Audience) là một tùy chọn nhắm mục tiêu quảng cáo quan trọng, cho phép nhà quảng cáo tiếp cận hoặc loại trừ các nhóm người dùng cụ thể khi thiết lập chiến dịch quảng cáo.

Nội dung tài liệu bao gồm:
- [Tổng quan quản lý Audience (Audience Management)](audience.md#doc-1739566496956417)
- [Tổng quan & Lợi ích (Overview)](audience.md#doc-1746998266963969)
- [Hướng dẫn chung (Guides)](audience.md#doc-1746998271267841)
- [Các loại Audience (Audience types)](audience.md#doc-1746998648212482)
- [Giới thiệu về Streaming API (About Streaming API)](audience.md#doc-1739566528222210)
- [Nguyên tắc chuẩn hóa mã định danh (Guidelines for identifier normalization)](audience.md#doc-1850030360880129)
- [Tạo Audience (Create an audience)](audience.md#doc-1746998676042753)
- [Tạo Custom Audience (Create a Custom Audience)](audience.md#doc-1747012172250114)
- [Tạo Customer File Audience (Create a Customer File Audience)](audience.md#doc-1747012327159809)
- [Tạo Audience theo quy tắc (Create an audience by rule)](audience.md#doc-1739566532187138)
- [Tạo Lookalike Audience (Create a Lookalike Audience)](audience.md#doc-1747012174934018)
- [Tạo Saved Audience (Create a Saved Audience)](audience.md#doc-1780156510696449)
- [Quản lý Audience (Manage audiences)](audience.md#doc-1746998678415361)
- [Câu hỏi thường gặp (FAQs)](audience.md#doc-1746998681953281)
- [Danh mục API tham chiếu (API reference)](audience.md#doc-1739566530595841)

---

## Quản lý Audience (`Audience Management`)
<a id="doc-1739566496956417"></a>
<!-- doc_id: 1739566496956417 -->

> Đường dẫn: Marketing API > Audience Management

Audience là một tùy chọn nhắm mục tiêu quảng cáo cho phép các nhà quảng cáo trên TikTok For Business nhắm tới hoặc loại trừ người dùng cụ thể khi thiết lập quảng cáo.
- Để tìm hiểu phần giới thiệu và lợi ích của Audience API, xem [Tổng quan (Overview)](audience.md#doc-1746998266963969).
- Để tìm hiểu về các loại audience khác nhau cũng như cách tạo và quản lý tệp đối tượng, xem [Hướng dẫn (Guides)](audience.md#doc-1746998271267841):
  - [Audience types](audience.md#doc-1746998648212482): Giới thiệu các loại audience và các API liên quan.
  - [About Streaming API](audience.md#doc-1739566528222210): Giới thiệu Streaming API cùng sự khác biệt giữa Customer File API và Streaming API, cũng như quy trình làm việc giữa hai dịch vụ API này.
    - Để tìm hiểu cách chuẩn hóa mã định danh khi tạo audience, xem [Guidelines for identifier normalization](audience.md#doc-1850030360880129).
  - [Create an audience](audience.md#doc-1746998676042753): Hướng dẫn cách tạo audience bằng cách sử dụng Audience API.
  - [Manage audiences](audience.md#doc-1746998678415361): Hướng dẫn cách quản lý audience, bao gồm lấy thông tin, cập nhật, xóa, chia sẻ audience, áp dụng audience cho nhiều nhóm quảng cáo, v.v.
  - [FAQs](audience.md#doc-1746998681953281): Tổng hợp các câu hỏi thường gặp về Audience Management API.
- Để biết các API khả dụng cho việc quản lý audience, xem [API reference](audience.md#doc-1739566530595841).

---

## Tổng quan (`Overview`)
<a id="doc-1746998266963969"></a>
<!-- doc_id: 1746998266963969 -->

> Đường dẫn: Marketing API > Audience Management > Overview

Phần này giới thiệu Audience Management API và các lợi ích mà nó mang lại.

Audience là một nhóm người dùng có thể nhìn thấy quảng cáo của bạn. Việc chọn đúng tệp đối tượng có thể giúp bạn cải thiện hiệu suất quảng cáo đáng kể. Bạn có thể tạo, cập nhật và quản lý Custom Audience (Tệp đối tượng tùy chỉnh) và Lookalike Audience (Tệp đối tượng tương tự) thông qua Audience API để liên tục duy trì tệp đối tượng cập nhật nhất cho việc nhắm mục tiêu.

> [!IMPORTANT]
> Khi sử dụng các endpoint của Audience API, bạn đồng ý với [Điều khoản TikTok Custom Audiences (Customer File)](https://ads.tiktok.com/i18n/official/policy/custom-audience-terms).

> [!NOTE]
> Để đăng ký quyền truy cập Streaming API (trước đây gọi là Segment API), hãy sử dụng tính năng [Quản lý danh sách cho phép (Allowlist Management)](https://ads.tiktok.com/marketing_api/blog/detail/7102266224578396162) trên Developer Portal bằng cách chọn "Streaming API" từ menu thả xuống. TikTok sẽ xem xét các đơn đăng ký theo định kỳ.

### Lợi ích của Audience API

* **Tối đa hóa lợi tức chi tiêu quảng cáo (ROAS)**: Lên lịch cập nhật và tạo Custom Audience định kỳ để liên tục duy trì tệp đối tượng cập nhật nhất được nhắm mục tiêu.
* **Tự động hóa quy trình quản lý**: Tự động hóa việc quản lý trình tạo Custom Audience thông qua các endpoint API. Tự động hóa quá trình tải file CSV lên mà không cần thao tác thủ công, giúp giảm thiểu rủi ro vi phạm dữ liệu cá nhân.
* **Tối đa hóa mức độ ảnh hưởng thương hiệu**: Cập nhật động tệp đối tượng để mở rộng hồ sơ đối tượng và xây dựng Lookalike Audience nhằm tìm kiếm những người dùng tương tự trên TikTok.

---

## Hướng dẫn chung (`Guides`)
<a id="doc-1746998271267841"></a>
<!-- doc_id: 1746998271267841 -->

> Đường dẫn: Marketing API > Audience Management > Guides

Hướng dẫn này sẽ trình bày cho bạn các loại audience khác nhau và các bước để tạo cũng như quản lý audience thông qua các API liên quan:
- [Audience types](audience.md#doc-1746998648212482): Giới thiệu các loại audience và các API liên quan.
- [About Streaming API](audience.md#doc-1739566528222210): Giới thiệu Streaming API cũng như sự khác biệt giữa Customer File API và Streaming API.
- [Create audiences](audience.md#doc-1746998676042753): Giới thiệu cách tạo audience bằng Audience API.
- [Manage audiences](audience.md#doc-1746998678415361): Giới thiệu cách quản lý audience, bao gồm lấy thông tin, cập nhật, xóa, chia sẻ và sử dụng audience trong quảng cáo.
- [FAQs](audience.md#doc-1746998681953281): Tổng hợp các câu hỏi thường gặp về Audience Management API.

---

## Các loại Audience (`Audience types`)
<a id="doc-1746998648212482"></a>
<!-- doc_id: 1746998648212482 -->

> Đường dẫn: Marketing API > Audience Management > Guides > Audience types

TikTok API for Business hỗ trợ tạo **Custom Audiences** (Tệp đối tượng tùy chỉnh) và **Lookalike Audiences** (Tệp đối tượng tương tự).
* **Custom Audience** là tùy chọn nhắm mục tiêu cho phép bạn tìm những người đã biết hoặc đã tương tác với doanh nghiệp của bạn. Bạn có thể tạo custom audience theo quy tắc (by rule) để định nghĩa đối tượng Tương tác (Engagement), Hoạt động ứng dụng (App Activity) hoặc Lưu lượng truy cập trang web (Website Traffic). Bạn cũng có thể tận dụng Customer File API để xây dựng tệp đối tượng từ tệp khách hàng có sẵn.
* Nếu bạn là đối tác dữ liệu hỗ trợ các nhà quảng cáo kích hoạt audience trên TikTok, hãy tham khảo [Streaming API](audience.md#doc-1739566528222210) — công cụ xử lý theo lô theo thời gian thực để đáp ứng nhu cầu thông lượng cao.
* Để tìm tệp đối tượng có cùng đặc điểm với đối tượng hiện tại, bạn có thể tạo **Lookalike Audience** dựa trên Custom Audience đã có.

### Bảng so sánh các loại Audience

| Loại Audience | Phương thức tạo | Thời gian xử lý | Kích thước tối thiểu | Tần suất cập nhật |
|---|---|---|---|---|
| Customer File Audience | Tải file danh sách khách hàng lên qua [Customer File API](../12-api-reference/09-audience.md#doc-1739940501023746) hoặc [Streaming API](../12-api-reference/09-audience.md#doc-1739940504185857). | Khoảng 24-48 giờ để hoàn tất đối soát và kích hoạt. | Tối thiểu 1.000 người dùng trùng khớp để có thể nhắm mục tiêu. | Cập nhật định kỳ thông qua API cập nhật tệp hoặc đẩy luồng theo thời gian thực. |
| Engagement Audience | Tạo theo quy tắc dựa trên tương tác với quảng cáo (lượt xem video, nhấp chuột, tương tác trang). | Khoảng 24 giờ để tích lũy dữ liệu. | Tối thiểu 1.000 người dùng. | Tự động cập nhật liên tục theo cửa sổ thời gian (lookback window). |
| App Activity Audience | Tạo theo quy tắc dựa trên sự kiện ứng dụng được ghi nhận qua đối tác đo lường di động (MMP). | Khoảng 24 giờ. | Tối thiểu 1.000 người dùng. | Tự động làm mới theo cửa sổ lưu giữ dữ liệu đã chọn. |
| Website Traffic Audience | Tạo theo quy tắc dựa trên sự kiện theo dõi qua TikTok Pixel trên trang web. | Khoảng 24 giờ. | Tối thiểu 1.000 người dùng. | Tự động làm mới theo quy tắc sự kiện Pixel. |
| Lead Generation Audience | Tạo theo quy tắc dựa trên hành động mở hoặc gửi biểu mẫu tìm kiếm khách hàng tiềm năng (Instant Form). | Khoảng 24 giờ. | Tối thiểu 1.000 người dùng. | Tự động làm mới theo quy tắc biểu mẫu. |
| Business Account Audience | Tạo theo quy tắc dựa trên tương tác với tài khoản TikTok Business (follow, xem hồ sơ, xem video tự nhiên). | Khoảng 24 giờ. | Tối thiểu 1.000 người dùng. | Tự động làm mới liên tục. |
| Lookalike Audience | Mở rộng từ tệp nguồn Custom Audience thông qua [/dmp/custom_audience/lookalike/create/](../12-api-reference/09-audience.md#doc-1739940511844353). | Khoảng 24-48 giờ. | Tệp nguồn tối thiểu 100 người dùng (khuyến nghị trên 1.000). | Cần làm mới thủ công hoặc gọi API làm mới khi tệp nguồn thay đổi lớn. |
| Saved Audience | Lưu lại cấu hình nhắm mục tiêu (nhân khẩu học, sở thích, hành vi, thiết bị) để tái sử dụng. | Khả dụng ngay lập tức. | Không yêu cầu kích thước tối thiểu. | Cố định theo cấu hình đã lưu. |

---

## Giới thiệu về Streaming API (`About Streaming API`)
<a id="doc-1739566528222210"></a>
<!-- doc_id: 1739566528222210 -->

> Đường dẫn: Marketing API > Audience Management > Guides > About Streaming API

Streaming API (trước đây gọi là Segment API) là giải pháp phân đoạn đối tượng theo thời gian thực được thiết kế riêng cho các đối tác dữ liệu và nhà quảng cáo có nhu cầu xử lý lượng dữ liệu khách hàng lớn với tốc độ cao.

### So sánh giữa Customer File API và Streaming API

| Đặc điểm | Customer File API | Streaming API |
|---|---|---|
| **Mục đích sử dụng** | Phù hợp cho nhà quảng cáo tải lên các tệp danh sách khách hàng tĩnh (file CSV/TXT) theo từng đợt định kỳ. | Dành cho các đối tác dữ liệu hoặc nền tảng dữ liệu khách hàng (CDP) cần đồng bộ luồng dữ liệu thời gian thực hoặc gần thời gian thực với thông lượng lớn. |
| **Quyền hạn truy cập** | Khả dụng mặc định cho tất cả các tài khoản quảng cáo đã được ủy quyền. | Yêu cầu phải đăng ký và được đưa vào danh sách cho phép (allowlist) thông qua Developer Portal. |
| **Cơ chế tải dữ liệu** | Tải file lên bộ nhớ tạm qua [/dmp/custom_audience/file/upload/](../12-api-reference/09-audience.md#doc-1739940567842818) rồi tạo audience từ đường dẫn file. | Tạo phân đoạn đối tượng (`segment`) trước qua [/segment/audience/](../12-api-reference/09-audience.md#doc-1739940583739393), sau đó gửi ánh xạ các ID người dùng theo lô qua [/segment/mapping/](../12-api-reference/09-audience.md#doc-1739940585975809). |
| **Hỗ trợ đa tài khoản** | Tải file riêng biệt cho từng tài khoản quảng cáo (`advertiser_id`). | Một lần ủy quyền ở cấp Business Account có thể tạo và ánh xạ phân đoạn cho nhiều tài khoản quảng cáo thuộc cùng Business Account. |

### Quy trình làm việc của Customer File API
1. Sử dụng [/dmp/custom_audience/file/upload/](../12-api-reference/09-audience.md#doc-1739940567842818) để tải lên tệp dữ liệu khách hàng và nhận đường dẫn tệp duy nhất trên toàn cầu (`file_path`).
2. Sử dụng `file_path` trong [/dmp/custom_audience/create/](../12-api-reference/09-audience.md#doc-1739940570793985) để tạo Custom Audience từ file. Phản hồi sẽ trả về mã định danh đối tượng tùy chỉnh duy nhất (`custom_audience_id`).
3. Sử dụng `custom_audience_id` trong [/dmp/custom_audience/update/](../12-api-reference/09-audience.md#doc-1739940572667906) để thực hiện các thao tác cập nhật theo lô (`Append`, `Remove`, `Replace`) cho từng đối tượng tùy chỉnh riêng biệt.

### Quy trình làm việc của Streaming API
1. Sử dụng [/segment/audience/](../12-api-reference/09-audience.md#doc-1739940583739393) để tạo các phân đoạn đối tượng. Bạn sẽ nhận được `audience_id` duy nhất trong phản hồi.
2. Sử dụng `audience_id` trong [/segment/mapping/](../12-api-reference/09-audience.md#doc-1739940585975809) để thực hiện ánh xạ phân đoạn theo lô cho các tài khoản quảng cáo khác nhau thuộc cùng một Business Account.
3. Nếu muốn xóa ánh xạ phân đoạn, hãy sử dụng [/segment/mapping/](../12-api-reference/09-audience.md#doc-1739940585975809) theo các quy tắc sau:
   - Đặt `action` là `delete`.
   - Truyền `data` khi muốn xóa ánh xạ ID đơn lẻ (một audience ID trên mỗi người dùng hoặc thiết bị), hoặc truyền `batch_data` khi muốn xóa ánh xạ nhiều ID (nhiều audience ID trên mỗi người dùng hoặc thiết bị).
4. Nếu muốn xóa hoàn toàn một audience, thực hiện theo các bước sau (lưu ý audience phải được ngắt kết nối khỏi tất cả nhóm quảng cáo trước khi xóa):
   1. Dùng [/dmp/custom_audience/apply/log/](../12-api-reference/09-audience.md#doc-1758615737388033) để kiểm tra những nhóm quảng cáo nào đang liên kết với audience cần xóa (truyền `advertiser_id` và `custom_audience_ids` để lấy danh sách `adgroup_id`).
   2. Dùng [/dmp/custom_audience/apply/](../12-api-reference/09-audience.md#doc-1758615097524225) để ngắt kết nối audience khỏi nhóm quảng cáo (truyền `advertiser_id`, `custom_audience_id`, `adgroup_ids`, và đặt `action_mode` thành `disconnect`).
   3. Sau khi đã ngắt kết nối, dùng [/segment/audience/](../12-api-reference/09-audience.md#doc-1739940583739393) để xóa audience (truyền `advertiser_id`, `delete_audience_id`, và đặt `action` thành `delete`).

### Lưu ý quan trọng cho Streaming API
- **Nhiều nhà quảng cáo gắn với một Business Account**: Một Business Account có thể liên kết với nhiều tài khoản quảng cáo. Bạn chỉ cần nhận access token ủy quyền một lần từ Business Account là có thể thao tác với dữ liệu của tất cả tài khoản quảng cáo trực thuộc.
- **Loại mã định danh được hỗ trợ**: Streaming API hỗ trợ mặc định nhiều loại mã định danh (Email, Phone, GAID, IDFA).

---

## Nguyên tắc chuẩn hóa mã định danh (`Guidelines for identifier normalization`)
<a id="doc-1850030360880129"></a>
<!-- doc_id: 1850030360880129 -->

> Đường dẫn: Marketing API > Audience Management > Guides > About Streaming API > Guidelines for identifier normalization

Bảng dưới đây nêu rõ các nguyên tắc chuẩn hóa mã định danh được sử dụng để xây dựng tệp đối tượng với [Customer File API](../12-api-reference/09-audience.md#doc-1739940501023746) hoặc [Streaming API](../12-api-reference/09-audience.md#doc-1739940504185857).

| Loại ID (`ID Type`) | Tiêu đề bắt buộc cho Customer File | Định dạng khuyến nghị - Giá trị gốc | Định dạng khuyến nghị - Đã băm (Hashed) | Định dạng hỗ trợ khác (chỉ băm) | Ví dụ giá trị gốc | Ví dụ giá trị đã băm |
|---|---|---|---|---|---|---|
| **Email** | `Email_SHA256` | • Loại bỏ khoảng trắng.<br>• Chuyển toàn bộ về chữ thường. | • Loại bỏ khoảng trắng.<br>• Chuyển toàn bộ ký tự về chữ thường.<br>• Băm bằng thuật toán SHA-256. | Không | `johndoe@gmail.com` | Chuẩn hóa: `janedoe@gmail.com`<br>Băm: `d6117306485ed0e50afab3ac871e98f81699151f30281527d63ff5f233656c69` |
| **Phone** (Số điện thoại) | `Phone_SHA256` | • Định dạng chuẩn quốc tế E.164: `+`[mã quốc gia][số điện thoại]. | • Định dạng E.164: `+`[mã quốc gia][số điện thoại].<br>• Băm bằng thuật toán SHA-256. | • Không có dấu `+`.<br>• Không có dấu `+` và không có mã quốc gia. | • US: `+16577770000`<br>• Quốc tế: `+37493828222` | Chuẩn hóa: `+16577770000`<br>Băm: `65b7e6dcf6f4310f8d7cbfbd78289a753062fb054d6664fb9aaac5df66a422d4` |
| **MAID** (Mã quảng cáo di động) | `MAID` hoặc `MAID_MD5` hoặc `MAID_SHA256` | • Sử dụng GAID (Android) hoặc IDFA (iOS).<br>• Toàn bộ viết hoa hoặc toàn bộ viết thường.<br>• Loại bỏ khoảng trắng ở đầu và cuối chuỗi. | • Toàn bộ viết hoa hoặc viết thường.<br>• Loại bỏ khoảng trắng ở đầu/cuối.<br>• Băm bằng thuật toán SHA-256 hoặc MD5. | Không | `aece52e7-03ee-455a-b3c4-e57283966239` | Chuẩn hóa: `5f3a2b18-9c4d-4e7f-b8e2-17d3a1e69b25`<br>Băm: `83dc3f5f32b9472613b0f038d36f22585a609d018af6f6067f50da318bf354bd` |

---

## Tạo Audience (`Create an audience`)
<a id="doc-1746998676042753"></a>
<!-- doc_id: 1746998676042753 -->

> Đường dẫn: Marketing API > Audience Management > Guides > Create an audience

Chủ đề này thảo luận về cách tạo các tệp đối tượng bằng cách sử dụng [Audience API](../12-api-reference/09-audience.md#doc-1739940398505986):
- **Custom Audience** (Tệp đối tượng tùy chỉnh): Bạn có thể tạo Custom Audience bằng [tệp khách hàng (file)](audience.md#doc-1747012327159809) hoặc [quy tắc (rules)](audience.md#doc-1739566532187138). Kích thước đối tượng tối thiểu là **1.000 người dùng** để có thể nhắm mục tiêu trong một nhóm quảng cáo.
- **Lookalike Audience** (Tệp đối tượng tương tự): Bạn có thể sử dụng một đối tượng hiện có để [tạo Lookalike Audience](audience.md#doc-1747012174934018) nhằm mục đích tiếp thị lại hoặc mở rộng tệp khách hàng tiềm năng.
- **Saved Audience** (Tệp đối tượng đã lưu): Bạn có thể [tạo Saved Audience](audience.md#doc-1780156510696449) và sau đó áp dụng cấu hình này vào các nhóm quảng cáo của mình một cách nhanh chóng.

---

## Tạo Custom Audience (`Create a Custom Audience`)
<a id="doc-1747012172250114"></a>
<!-- doc_id: 1747012172250114 -->

> Đường dẫn: Marketing API > Audience Management > Guides > Create an audience > Create a Custom Audience

Chủ đề này giới thiệu cách tạo các tệp đối tượng tùy chỉnh (Custom Audiences):
- [Create a Customer File Audience](audience.md#doc-1747012327159809): Tạo đối tượng từ tệp dữ liệu khách hàng có sẵn.
- [Create an audience by rules](audience.md#doc-1739566532187138): Tạo đối tượng tự động dựa trên các quy tắc tương tác, lưu lượng web hoặc ứng dụng.

---

## Tạo Customer File Audience (`Create a Customer File Audience`)
<a id="doc-1747012327159809"></a>
<!-- doc_id: 1747012327159809 -->

> Đường dẫn: Marketing API > Audience Management > Guides > Create an audience > Create a Custom Audience > Create a Customer File Audience

Bài viết này hướng dẫn cách tạo **Customer File Audiences** bằng Customer File API và Streaming API.

### Sử dụng Customer File API
1. Sử dụng [/dmp/custom_audience/file/upload/](../12-api-reference/09-audience.md#doc-1739940567842818) để tải lên tệp dữ liệu và nhận một `file_path` duy nhất trên toàn cầu.

Bạn có thể tải lên một tệp có một hoặc nhiều loại ID. Để tải tệp có nhiều loại ID, `calculate_type` phải được đặt thành `MULTIPLE_TYPES` và các hàng tiêu đề (header) là bắt buộc. Các tiêu đề được hỗ trợ gồm: `"MAID"`, `"phone_SHA256"`, `"email_SHA256"`, `"MAID_SHA256"`, `"MAID_MD5"` (không phân biệt chữ hoa, chữ thường). Số lượng trường trong mỗi dòng dữ liệu phải khớp với số lượng cột tiêu đề.

**Mẫu tệp có một loại ID (không cần tiêu đề):**
```text
9f5326721cb782c
9f5326721cb782c
```

**Mẫu tệp có nhiều loại ID (bắt buộc có tiêu đề):**
| email_SHA256 | phone_SHA256 | MAID |
|---|---|---|
| 9f5326721cb782c | 9f5326721cb782c | 9f5326721cb782c |
| 9f5326721cb782c | 9f5326721cb782c | 9f5326721cb782c |

2. Sử dụng [/dmp/custom_audience/create/](../12-api-reference/09-audience.md#doc-1739940570793985) để tạo audience từ file, truyền vào `file_path` đã nhận được ở bước trước. Khi cuộc gọi thành công, phản hồi trả về `custom_audience_id` để bạn sử dụng trong việc cập nhật, lấy thông tin hoặc xóa audience.

### Sử dụng Streaming API
1. Sử dụng [/segment/audience/](../12-api-reference/09-audience.md#doc-1739940583739393) để tạo phân đoạn audience và nhận `audience_id`.
2. Sử dụng `audience_id` trong [/segment/mapping/](../12-api-reference/09-audience.md#doc-1739940585975809) để thực hiện ánh xạ phân đoạn hàng loạt cho các tài khoản quảng cáo thuộc cùng Business Account.

---

## Tạo Audience theo quy tắc (`Create an audience by rule`)
<a id="doc-1739566532187138"></a>
<!-- doc_id: 1739566532187138 -->

> Đường dẫn: Marketing API > Audience Management > Guides > Create an audience > Create a Custom Audience > Create an audience by rule

Bạn có thể chỉ định các quy tắc để tạo các loại đối tượng tùy chỉnh bao gồm: **Engagement Audience (Đối tượng tương tác), App Activity Audience (Đối tượng hoạt động ứng dụng), Website Traffic Audience (Đối tượng lưu lượng web), Lead Generation Audience (Đối tượng tạo khách hàng tiềm năng), Shop Activity Audience (Đối tượng hoạt động trên Shop), hoặc Business Account Audience (Đối tượng tương tác tài khoản doanh nghiệp)**. Ví dụ: bạn có thể tạo đối tượng gồm những người dùng đã nhấp vào quảng cáo trong 7 ngày qua, hoặc những người đã thêm sản phẩm vào giỏ hàng nhưng chưa hoàn tất mua hàng trong 14 ngày qua.

Sử dụng [/dmp/custom_audience/rule/create/](../12-api-reference/09-audience.md#doc-1739940509849601) để xác định tập hợp quy tắc bao gồm (`inclusion_rule_set`) và tùy chọn thêm tập hợp quy tắc loại trừ (`exclusion_rule_set`). Nếu gọi thành công, phản hồi trả về `custom_audience_id`.

Cấu trúc quy tắc (`rule_spec`) gồm các tầng lồng nhau như sau:
- Một đặc tả quy tắc audience chứa hai bộ quy tắc (`inclusion_rule_set` và `exclusion_rule_set`).
- Mỗi bộ quy tắc chứa danh sách các quy tắc (`rules`) và một toán tử (`operator`).
- Mỗi quy tắc chứa các bộ lọc (`filter_set`) và số ngày lưu giữ đối tượng (`retention_days`).
- Mỗi bộ lọc chứa các điều kiện lọc (`filters`) và một toán tử (`operator`).

> [!NOTE]
> • Tệp đối tượng mới tạo cần khoảng 1 giờ để hệ thống phân tích và xử lý dữ liệu trước khi chuyển sang trạng thái hoạt động.<br>• Dùng [/dmp/custom_audience/get/](../12-api-reference/09-audience.md#doc-1739940507792385) để kiểm tra trạng thái tệp đối tượng. Chỉ những tệp khả dụng (`is_valid` = `true`) mới có thể thao tác hoặc sử dụng trong nhóm quảng cáo.

### Định dạng quy tắc Audience (Audience rule format)

| Field | Type | Description |
|---|---|---|
| `inclusion_rule_set` **(Bắt buộc)** | object | Một tập hợp đối tượng quy tắc bao gồm. Số lượng: từ 1 đến 5, không trùng lặp. Định dạng xem bảng "Định dạng bộ quy tắc" bên dưới. |
| `exclusion_rule_set` | object | Một tập hợp đối tượng quy tắc loại trừ. Số lượng: từ 0 đến 5, không trùng lặp. Định dạng xem bảng "Định dạng bộ quy tắc" bên dưới. |

### Định dạng bộ quy tắc (Rule set format)

| Field | Type | Description |
|---|---|---|
| `operator` **(Bắt buộc)** | object | Toán tử logic giữa các quy tắc. `AND` yêu cầu thỏa mãn cả hai quy tắc; `OR` yêu cầu thỏa mãn một trong các quy tắc. Hiện tại hệ thống chỉ hỗ trợ `OR`. |
| `rules` **(Bắt buộc)** | object[] | Mảng các đối tượng quy tắc bao gồm/loại trừ. Định dạng xem bảng "Định dạng quy tắc" bên dưới. |

### Định dạng quy tắc (Rule format)

| Field | Type | Description |
|---|---|---|
| `event_source_ids` | string[] | Danh sách ID nguồn sự kiện của quy tắc. Bắt buộc khi `audience_type` không phải là `ENGAGEMENT` hoặc `LEAD_GENERATION`.<br>• Đối với Engagement Audience: dùng ID nhóm quảng cáo làm ID nguồn sự kiện. Nếu không truyền, tất cả ID nguồn khả dụng sẽ được sử dụng.<br>• Đối với Pixel Audience: dùng Pixel ID.<br>• Đối với App Activity Audience: dùng App ID của ứng dụng.<br>• Đối với Lead Generation Audience: không truyền trường này. Nếu không truyền, tất cả ID biểu mẫu khả dụng sẽ được dùng.<br>• Đối với Shop Activity Audience: dùng Store ID của cửa hàng (lấy qua [/store/list/](../12-api-reference/69-tiktok-store.md#doc-1752267762718722)).<br>• Đối với Business Account Audience: dùng ID người dùng chính của nhà quảng cáo (lấy qua **/user/info/**).<br>• Đối với Organic Engagement Audience: dùng ID video tự nhiên (tối đa 10 ID, lấy qua [/identity/live/get/](../12-api-reference/46-identity.md#doc-1740218475032577)).<br>• Đối với Live Engagement Audience: dùng ID video live (tối đa 10 ID).<br>• Đối với Offline Activity Audience: dùng ID bộ sự kiện ngoại tuyến (Offline Event set IDs, lấy qua [/offline/get/](../12-api-reference/43-events-1-0-p1.md#doc-1765596808589313)). |
| `retention_days` **(Bắt buộc)** | number | Số ngày lưu giữ người dùng trong tệp đối tượng. Xem enum tại [Enumerations - Lookback window](../15-appendix/phu-luc-p1.md#doc-1737174886619138).<br>> [!NOTE]<br>> • Nếu `audience_type` = `BUSINESS_ACCOUNT`, và `value` trong `filters` không phải là `BUSINESS ACCOUNT PROFILE FOLLOW`, thì `retention_days` phải là `7`, `14`, hoặc `30`.<br>> • Nếu `audience_type` là `ENGAGEMENT_LIVE_VIDEO` hoặc `ENGAGEMENT_ORGANIC_VIDEO`, `retention_days` phải là `7`, `14`, hoặc `30`. |
| `filter_set` **(Bắt buộc)** | object | Danh sách các giá trị bộ lọc. Định dạng xem bảng "Định dạng bộ lọc" bên dưới. |

### Định dạng bộ lọc (Filter set format)

| Field | Type | Description |
|---|---|---|
| `operator` **(Bắt buộc)** | string | Toán tử giữa các bộ lọc. `AND` yêu cầu thỏa mãn cả hai; `OR` yêu cầu thỏa mãn một trong các bộ lọc. Hiện tại chỉ hỗ trợ `OR`. |
| `filters` **(Bắt buộc)** | object[] | Danh sách các bộ lọc. Hiện tại chỉ có thể truyền một giá trị duy nhất. Định dạng xem bảng "Định dạng chi tiết bộ lọc" bên dưới. |

### Định dạng chi tiết bộ lọc (Filter format)

| Field | Type | Description |
|---|---|---|
| `field` **(Bắt buộc)** | string | Trường lọc. Hiện tại chỉ hỗ trợ `EVENT`. |
| `operator` **(Bắt buộc)** | string | Toán tử lọc giữa trường lọc và giá trị lọc. Giá trị enum: `EQ` (bằng), `GT` (lớn hơn), `LT` (nhỏ hơn). Hiện tại chỉ hỗ trợ `EQ`. |
| `value` **(Bắt buộc)** | string | Giá trị trường lọc sự kiện. Danh sách enum xem tại [Enumeration - Filter Value](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |

### Ví dụ JSON cấu hình quy tắc (`rule_spec`)
```json
{
    "inclusion_rule_set": {
        "operator": "OR",
        "rules": [
            {
                "event_source_ids": ["1723456789012345"],
                "retention_days": 30,
                "filter_set": {
                    "operator": "OR",
                    "filters": [
                        {
                            "field": "EVENT",
                            "operator": "EQ",
                            "value": "CLICK"
                        }
                    ]
                }
            }
        ]
    }
}
```


---

## Tạo Lookalike Audience (`Create a Lookalike Audience`)
<a id="doc-1747012174934018"></a>
<!-- doc_id: 1747012174934018 -->

> Đường dẫn: Marketing API > Audience Management > Guides > Create an audience > Create a Lookalike Audience

Sử dụng endpoint [/dmp/custom_audience/lookalike/create/](../12-api-reference/09-audience.md#doc-1739940511844353) để tạo tệp đối tượng tương tự (Lookalike Audience) dựa trên một tệp đối tượng tùy chỉnh (Custom Audience) hiện có. Khi cuộc gọi thành công, phản hồi trả về `custom_audience_id` của Lookalike Audience mới.

> [!NOTE]
> • Tệp Lookalike Audience mới tạo mất khoảng **24 đến 48 giờ** để hệ thống phân tích và xử lý mô hình trước khi chuyển sang trạng thái hoạt động.<br>• Các Lookalike Audience tạo trước ngày 15 tháng 11 năm 2021 có thể được làm mới thông qua endpoint [/dmp/custom_audience/lookalike/update/](../12-api-reference/09-audience.md#doc-1758616888158209).

---

## Tạo Saved Audience (`Create a Saved Audience`)
<a id="doc-1780156510696449"></a>
<!-- doc_id: 1780156510696449 -->

> Đường dẫn: Marketing API > Audience Management > Guides > Create an audience > Create a Saved Audience

Bài viết này giới thiệu cách tạo và quản lý **Saved Audience** (Tệp đối tượng đã lưu).

### Khái niệm Saved Audience

Saved Audience cho phép bạn lưu trữ các thiết lập nhắm mục tiêu (targeting settings) thường dùng và tái sử dụng chúng để tạo các nhóm quảng cáo trong tương lai. Bằng cách loại bỏ các bước thiết lập lặp đi lặp lại khi xây dựng đối tượng mục tiêu, Saved Audience giúp bạn tiết kiệm thời gian và tối ưu trải nghiệm vận hành chiến dịch.

Hiện tại, các cài đặt bạn có thể lưu trong Saved Audience bao gồm: thông tin nhân khẩu học (demographics), tệp đối tượng (audience), sở thích (interests), hành vi (behaviors) và thiết bị (devices). Chi tiết xem tại endpoint [/dmp/saved_audience/create/](../12-api-reference/09-audience.md#doc-1780154541898754). Tuy nhiên, các tùy chọn liên quan đến thu nhập hộ gia đình (`household_income`), sức mua (`spending_power`), các ngành đặc thù (`special_industries`), và gói đối tượng Pangle (`included_pangle_audience_package_ids`, `excluded_pangle_audience_package_ids`) hiện chưa được hỗ trợ.

> [!IMPORTANT]
> Trước khi sử dụng Saved Audience trong nhóm quảng cáo của bạn, hãy đảm bảo cấu hình chiến dịch và nhóm quảng cáo thỏa mãn đồng thời các điều kiện sau:
> 1. Danh mục ngành nghề đặc thù Nhà ở, Việc làm hoặc Tín dụng (`special_industries`) **KHÔNG** được chọn trong chiến dịch.
> 2. **VÀ** mục tiêu quảng cáo (`objective_type`) **KHÔNG** đặt thành Bán hàng sản phẩm (`PRODUCT_SALES`).
> 3. **VÀ** vị trí hiển thị TikTok được chọn trong nhóm quảng cáo (nghĩa là `placement_type` đặt thành `PLACEMENT_TYPE_AUTOMATIC` **hoặc** `placement_type` là `PLACEMENT_TYPE_NORMAL` và có chứa `PLACEMENT_TIKTOK` trong danh sách `placements`).
> 4. **VÀ** tính năng nhắm mục tiêu tự động **KHÔNG** được bật trong nhóm quảng cáo (`auto_targeting_enabled` không đặt là `true`).
> 5. Ngoài ra, chiến dịch Smart+ (Smart+ Campaign) và quảng cáo Reach & Frequency (R&F) **không** thể sử dụng Saved Audience.

### Cách tạo Saved Audience
Sử dụng endpoint [/dmp/saved_audience/create/](../12-api-reference/09-audience.md#doc-1780154541898754) để tạo Saved Audience. Khi gọi thành công, phản hồi trả về `saved_audience_id`, có thể dùng để tạo hoặc cập nhật nhóm quảng cáo.

- Để xem chi tiết các Saved Audience đã tạo, dùng [/dmp/saved_audience/list/](../12-api-reference/09-audience.md#doc-1780154619404290).
- Để xóa Saved Audience, dùng [/dmp/saved_audience/delete/](../12-api-reference/09-audience.md#doc-1780154666312706).

> [!NOTE]
> Hiện tại, hệ thống không cho phép chỉnh sửa cấu hình của một Saved Audience đã tạo. Nếu cần thay đổi, bạn phải xóa và tạo Saved Audience mới.

### Áp dụng Saved Audience vào nhóm quảng cáo
1. Tạo chiến dịch qua [/campaign/create/](../12-api-reference/24-campaign.md#doc-1739318962329602).
2. Tạo nhóm quảng cáo qua [/adgroup/create/](../12-api-reference/07-ad-groups-p2.md#doc-1739499616346114).

Bạn áp dụng Saved Audience bằng cách điền `saved_audience_id` vào yêu cầu tạo nhóm quảng cáo. ID nhà quảng cáo (`advertiser_id`) của Saved Audience phải trùng khớp với `advertiser_id` của nhóm quảng cáo.

> [!WARNING]
> Khi tạo nhóm quảng cáo bằng `saved_audience_id`, bạn **không được** thiết lập đồng thời các tùy chọn nhắm mục tiêu (như `gender`, `age_groups`...) cùng lúc trong yêu cầu tạo nhóm quảng cáo nếu các tùy chọn đó đã tồn tại trong Saved Audience. Việc truyền trùng lặp sẽ gây ra lỗi xung đột.

Trong phản hồi của API tạo nhóm quảng cáo, hệ thống sẽ trả về cả `saved_audience_id` và các tùy chọn nhắm mục tiêu tương ứng đã được áp dụng từ Saved Audience.

3. Tạo quảng cáo qua [/ad/create/](../12-api-reference/02-ads-p1.md#doc-1739953377508354).

#### Ví dụ áp dụng Saved Audience vào nhóm quảng cáo (curl)
```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/adgroup/create/' \
--header 'Access-Token: act.example12345abcdef' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id": "7123456789012345678",
    "campaign_id": "1723456789012345",
    "adgroup_name": "AdGroup_Using_Saved_Audience",
    "placement_type": "PLACEMENT_TYPE_AUTOMATIC",
    "app_id": "123456",
    "app_name": "DemoApp",
    "optimization_goal": "INSTALL",
    "optimization_event": "ACTIVE",
    "billing_event": "OCPM",
    "bid_type": "BID_TYPE_CUSTOM",
    "bid_price": 1.0,
    "budget_mode": "BUDGET_MODE_TOTAL",
    "budget": 50.0,
    "schedule_type": "SCHEDULE_START_END",
    "schedule_start_time": "2025-01-01 00:00:00",
    "schedule_end_time": "2025-01-02 23:59:59",
    "saved_audience_id": "1723456789099999"
}'
```

---

## Quản lý Audience (`Manage audiences`)
<a id="doc-1746998678415361"></a>
<!-- doc_id: 1746998678415361 -->

> Đường dẫn: Marketing API > Audience Management > Guides > Manage audiences

Chủ đề này giới thiệu các hoạt động quản lý đối tượng sau khi đã tạo:

### 1. Lấy danh sách và chi tiết tệp đối tượng
- Sử dụng [/dmp/custom_audience/list/](../12-api-reference/09-audience.md#doc-1739940506015746) để lấy danh sách tất cả các Custom Audience trong một tài khoản quảng cáo.
- Sử dụng [/dmp/custom_audience/get/](../12-api-reference/09-audience.md#doc-1739940507792385) để lấy thông tin chi tiết của một hoặc nhiều Custom Audience cụ thể, bao gồm kích thước ước tính (`cover_num`), trạng thái khả dụng (`is_valid`), trạng thái hết hạn (`is_expiring`) và ngày hết hạn (`expired_time`).

### 2. Cập nhật tệp đối tượng (Customer File Audience)
Sử dụng [/dmp/custom_audience/update/](../12-api-reference/09-audience.md#doc-1739940572667906) để cập nhật nội dung của tệp đối tượng tùy chỉnh theo tệp:
- `Append`: Thêm các bản ghi người dùng mới vào tệp đối tượng hiện tại.
- `Remove`: Xóa bớt các bản ghi người dùng được chỉ định khỏi tệp đối tượng hiện tại.
- `Replace`: Thay thế toàn bộ tệp đối tượng hiện tại bằng dữ liệu mới. Lưu ý: mỗi tệp đối tượng chỉ được phép thực hiện thao tác `Replace` tối đa 1 lần mỗi ngày.

### 3. Xóa tệp đối tượng
Sử dụng [/dmp/custom_audience/delete/](../12-api-reference/09-audience.md#doc-1739940539757569) để xóa tệp đối tượng.
> [!IMPORTANT]
> Tệp đối tượng chỉ có thể bị xóa sau khi đã ngắt kết nối hoàn toàn khỏi tất cả các nhóm quảng cáo đang sử dụng nó. Dùng [/dmp/custom_audience/apply/log/](../12-api-reference/09-audience.md#doc-1758615737388033) để kiểm tra các nhóm quảng cáo liên kết và dùng [/dmp/custom_audience/apply/](../12-api-reference/09-audience.md#doc-1758615097524225) với `action_mode` = `disconnect` để ngắt kết nối trước khi gọi API xóa.

### 4. Chia sẻ tệp đối tượng giữa các tài khoản
- Chia sẻ tệp: Dùng [/dmp/custom_audience/share/](../12-api-reference/09-audience.md#doc-1740245803888706) để chia sẻ Custom Audience của bạn cho các tài khoản quảng cáo khác trong cùng Business Center hoặc tổ chức.
- Hủy chia sẻ: Dùng [/dmp/custom_audience/share/cancel/](../12-api-reference/09-audience.md#doc-1740245829978113) để thu hồi quyền truy cập đối tượng đã chia sẻ.
- Lịch sử chia sẻ: Dùng [/dmp/custom_audience/share/log/](../12-api-reference/09-audience.md#doc-1740245827044354) để tra cứu nhật ký chia sẻ của tệp đối tượng.

### 5. Áp dụng đối tượng vào nhiều nhóm quảng cáo
- Dùng [/dmp/custom_audience/apply/](../12-api-reference/09-audience.md#doc-1758615097524225) để liên kết hoặc ngắt kết nối tệp đối tượng với hàng loạt nhóm quảng cáo.
- Dùng [/dmp/custom_audience/apply/log/](../12-api-reference/09-audience.md#doc-1758615737388033) để xem nhật ký và trạng thái liên kết đối tượng với các nhóm quảng cáo.

### 6. Phân tích đối tượng (Audience Insights)
- Phân tích tệp đối tượng tiềm năng: Dùng [/audience/insight/potential/](../12-api-reference/09-audience.md#doc-1797016593782785) để khám phá hành vi, sở thích và thông tin nhân khẩu học của nhóm đối tượng mục tiêu tiềm năng.
- Phân tích độ trùng lặp (Audience Overlap): Dùng [/audience/insight/overlap/](../12-api-reference/09-audience.md#doc-1797023590780930) để đo lường mức độ trùng lặp người dùng giữa tệp đối tượng chuẩn (benchmark audience) và các tệp đối tượng so sánh khác.

---

## Câu hỏi thường gặp (`FAQs`)
<a id="doc-1746998681953281"></a>
<!-- doc_id: 1746998681953281 -->

> Đường dẫn: Marketing API > Audience Management > Guides > FAQs

Dưới đây là các câu hỏi thường gặp liên quan đến Audience Management API:

1. **Làm thế nào để tải lên các tệp đối tượng khách hàng?**
   Bạn có thể tạo tệp đối tượng thông qua API hoặc trực tiếp trên giao diện TikTok Ads Manager. Bạn cũng có thể phối hợp cả hai: tạo tệp đối tượng trên TikTok Ads Manager và bổ sung tệp dữ liệu thông qua API. Cả hai kênh đều hỗ trợ tải lên nhiều tệp liên tiếp. Chi tiết xem tại [Customer File](https://ads.tiktok.com/help/article?aid=9609). Với API, sử dụng [/dmp/custom_audience/file/upload/](../12-api-reference/09-audience.md#doc-1739940567842818) và [/dmp/custom_audience/create/](../12-api-reference/09-audience.md#doc-1739940570793985).

2. **Dung lượng tệp tải lên tối đa là bao nhiêu?**
   Dung lượng tối đa cho mỗi tệp tải lên qua API là **250MB**, và qua giao diện TikTok Ads Manager là **1GB**.

3. **Những chuẩn mã hóa nào được chấp nhận cho tệp đối tượng?**
   Các thuật toán băm được hỗ trợ gồm SHA-256 và MD5. Xem chi tiết tại [Enumeration - Encryption Types](../15-appendix/phu-luc-p1.md#doc-1737174886619138). Toàn bộ nội dung chuỗi (email, số điện thoại, ID quảng cáo) phải được chuyển về chữ thường hoặc chữ hoa đồng nhất và loại bỏ khoảng trắng trước khi thực hiện băm.

4. **Giới hạn tốc độ gọi (QPS) và hạn ngạch tạo đối tượng là gì?**
   - Đối với API tạo đối tượng từ file ([/dmp/custom_audience/create/](../12-api-reference/09-audience.md#doc-1739940570793985)): bạn có thể tạo tối đa **400 tệp đối tượng** cho mỗi tài khoản quảng cáo. Nếu vượt quá giới hạn này, bạn phải xóa các tệp cũ không còn dùng trước khi tạo tệp mới.
   - Đối với API cập nhật đối tượng ([/dmp/custom_audience/update/](../12-api-reference/09-audience.md#doc-1739940572667906)): mỗi tệp đối tượng có hạn ngạch tối đa **24 thao tác cập nhật** (`Append`, `Remove`, `Replace`) mỗi ngày. Thao tác thay thế toàn bộ (`Replace`) chỉ được thực hiện **1 lần/ngày** cho mỗi đối tượng. Vui lòng đợi thao tác trước hoàn tất xử lý trước khi gửi yêu cầu tiếp theo.
   - Thông tin giới hạn tần suất chung xem tại [Rate limits](../04-get-started/bat-dau.md#doc-1740029171730433).

5. **Có môi trường sandbox để kiểm thử API không?**
   Có. Bạn có thể sử dụng môi trường sandbox sau khi đăng ký ứng dụng nhà phát triển. Xem chi tiết tại [Sandbox accounts](../04-get-started/bat-dau.md#doc-1738855331457026).

6. **Sau khi tạo, bao lâu thì tệp đối tượng có thể sử dụng được?**
   Tệp đối tượng mới tạo thường mất khoảng **1 giờ** để hệ thống phân tích, đối soát dữ liệu và chuyển sang trạng thái hoạt động (`is_valid` = `true`).

7. **Chính sách hết hạn của tệp đối tượng như thế nào?**
   Tệp đối tượng sẽ hết hạn sau **1 năm** nếu không được sử dụng trong bất kỳ chiến dịch nào hoặc không được làm mới dữ liệu. Xem chi tiết tại [Chính sách hết hạn của đối tượng](https://ads.tiktok.com/help/article?aid=10001592). Bạn có thể kiểm tra trường `is_expiring` và `expired_time` trong phản hồi của [/dmp/custom_audience/get/](../12-api-reference/09-audience.md#doc-1739940507792385) để biết thời hạn cụ thể.

---

## Danh mục API (`API reference`)
<a id="doc-1739566530595841"></a>
<!-- doc_id: 1739566530595841 -->

> Đường dẫn: Marketing API > Audience Management > API reference

Nhóm API Audience Management gồm các endpoint sau:

* **Tệp khách hàng (Customer file)**
  - [Upload an audience file](../12-api-reference/09-audience.md#doc-1739940567842818): Tải file dữ liệu khách hàng lên máy chủ.
  - [Create an audience by file](../12-api-reference/09-audience.md#doc-1739940570793985): Tạo tệp đối tượng từ file đã tải lên.
* **Phân đoạn đối tượng thời gian thực (Audience segment - Streaming API)**
  - [Create/Delete an audience segment](../12-api-reference/09-audience.md#doc-1739940583739393): Tạo hoặc xóa phân đoạn đối tượng.
  - [Map audience segments](../12-api-reference/09-audience.md#doc-1739940585975809): Ánh xạ ID người dùng vào phân đoạn.
* **Cập nhật đối tượng**: [Update an audience](../12-api-reference/09-audience.md#doc-1739940572667906).
* **Truy vấn đối tượng**:
  - [Get all audiences](../12-api-reference/09-audience.md#doc-1739940506015746): Lấy danh sách tất cả tệp đối tượng trong tài khoản.
  - [Get audience details](../12-api-reference/09-audience.md#doc-1739940507792385): Lấy chi tiết thông tin và kích thước tệp đối tượng.
* **Tạo đối tượng theo quy tắc**: [Create an audience by rule](../12-api-reference/09-audience.md#doc-1739940509849601).
* **Đối tượng tương tự (Lookalike Audience)**:
  - [Create a lookalike audience](../12-api-reference/09-audience.md#doc-1739940511844353): Tạo tệp đối tượng tương tự.
  - [Refresh a lookalike audience](../12-api-reference/09-audience.md#doc-1758616888158209): Làm mới tệp đối tượng tương tự.
* **Xóa đối tượng**: [Delete audiences](../12-api-reference/09-audience.md#doc-1739940539757569).
* **Chia sẻ đối tượng**:
  - [Share audiences](../12-api-reference/09-audience.md#doc-1740245803888706): Chia sẻ tệp đối tượng cho tài khoản khác.
  - [Cancel the sharing of an audience](../12-api-reference/09-audience.md#doc-1740245829978113): Hủy chia sẻ tệp đối tượng.
  - [Get the sharing log of an audience](../12-api-reference/09-audience.md#doc-1740245827044354): Xem nhật ký chia sẻ đối tượng.
* **Áp dụng đối tượng vào nhóm quảng cáo**:
  - [Apply audiences to ad groups](../12-api-reference/09-audience.md#doc-1758615097524225): Liên kết hoặc ngắt liên kết đối tượng với nhóm quảng cáo.
  - [Get the application log of audiences](../12-api-reference/09-audience.md#doc-1758615737388033): Xem nhật ký áp dụng đối tượng.
* **Tệp đối tượng đã lưu (Saved Audience)**:
  - [Create a Saved Audience](../12-api-reference/09-audience.md#doc-1780154541898754): Tạo Saved Audience.
  - [Get details of Saved Audiences](../12-api-reference/09-audience.md#doc-1780154619404290): Xem chi tiết các Saved Audience.
  - [Delete Saved Audiences](../12-api-reference/09-audience.md#doc-1780154666312706): Xóa Saved Audience.
* **Thông tin chuyên sâu về đối tượng (Audience Insights)**:
  - [Get details of potential audiences](../12-api-reference/09-audience.md#doc-1797016593782785): Phân tích đặc điểm đối tượng tiềm năng.
  - [Get details of audience overlap](../12-api-reference/09-audience.md#doc-1797023590780930): Phân tích mức độ trùng lặp giữa các tệp đối tượng.
