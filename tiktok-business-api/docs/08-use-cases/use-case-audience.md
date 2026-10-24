# Use case: tích hợp Audience

Tài liệu này hướng dẫn chi tiết quy trình tích hợp tệp đối tượng (Audience) với TikTok API for Business. Bạn sẽ tìm hiểu cách chuẩn bị điều kiện tiên quyết, khởi tạo tệp đối tượng tùy chỉnh (Custom Audience) hoặc tệp đối tượng tương tự (Lookalike Audience), và áp dụng hoặc loại trừ chúng vào các nhóm quảng cáo đơn lẻ hoặc hàng loạt.

## Tích hợp tệp đối tượng (`Audience integration`)
<a id="doc-1758526010304514"></a>
<!-- doc_id: 1758526010304514 -->

> Đường dẫn: Use Cases > Audience integration

Bài viết này hướng dẫn bạn từng bước tích hợp tệp đối tượng (audience integration).

### Giới thiệu (Introduction)

Tệp đối tượng (Audience) là một tùy chọn nhắm mục tiêu quảng cáo cho phép nhà quảng cáo TikTok For Business nhắm mục tiêu (target) hoặc loại trừ (exclude) những người dùng cụ thể khi thiết lập quảng cáo. TikTok API for Business hỗ trợ nhiều [loại tệp đối tượng](../09-marketing-api/audience.md#doc-1746998648212482) khác nhau. Tệp đối tượng tùy chỉnh (Custom Audience) là tùy chọn nhắm mục tiêu giúp bạn tiếp cận những người đã biết hoặc từng tương tác với doanh nghiệp của bạn, trong khi Tệp đối tượng tương tự (Lookalike Audience) được xây dựng dựa trên các tệp đối tượng tùy chỉnh hiện có. **Bạn có thể sử dụng Audience API để tự động hóa việc tải lên tệp CSV mà không cần thao tác thủ công, hoặc tạo Lookalike Audience để tìm kiếm những người dùng tương tự trên TikTok.**

### Điều kiện tiên quyết (Prerequisites)

- Bạn đã được cấp quyền truy cập TikTok API for Business. Xem chi tiết tại [Bắt đầu - Quy trình từng bước](../04-get-started/bat-dau.md#doc-1735713609895937).
  - Để tích hợp tệp đối tượng, bạn cần các quyền liên quan. Xem **Tham chiếu API (API Reference)** để biết quyền cần thiết cho từng endpoint (bao gồm các endpoint trong mục "Các bước thực hiện") và xem [Cập nhật quyền ứng dụng](../04-get-started/bat-dau.md#doc-1738855280338946) để biết cách cấu hình quyền.
- Khi sử dụng các endpoint của Audience API, bạn đồng ý với [Điều khoản Tệp đối tượng tùy chỉnh (Tệp khách hàng) của TikTok (TikTok Custom Audiences (Customer File) Terms)](https://ads.tiktok.com/i18n/official/policy/custom-audience-terms).

### Các bước thực hiện (Steps)

1. Tạo tệp đối tượng bằng một trong các phương thức sau. ID của tệp đối tượng vừa tạo sẽ được trả về trong phản hồi (response):
   - Nếu bạn có sẵn danh sách đối tượng, bạn có thể sử dụng Customer File API để tải lên tệp đối tượng. Xem chi tiết các bước tại [Tạo tệp đối tượng bằng tệp khách hàng - Customer File API](../09-marketing-api/audience.md#doc-1747012327159809).
   - Nếu bạn muốn gửi luồng dữ liệu (stream) để tạo tệp đối tượng cho nhiều nhà quảng cáo cùng lúc, bạn có thể sử dụng Streaming API. Xem chi tiết các bước tại [Tạo tệp đối tượng bằng tệp khách hàng - Streaming API](../09-marketing-api/audience.md#doc-1747012327159809).

> [!NOTE]
> Để đăng ký quyền truy cập Streaming API (trước đây gọi là Segment API), hãy sử dụng tính năng Quản lý danh sách cho phép (Allowlist Management) trên Cổng thông tin nhà phát triển bằng cách chọn "Streaming API" từ menu thả xuống. Đơn đăng ký được xét duyệt liên tục.

   - Nếu bạn muốn tạo tệp đối tượng theo quy tắc (rules), ví dụ: những người đã nhấp vào quảng cáo trong 7 ngày qua hoặc người đã thêm sản phẩm vào giỏ hàng nhưng chưa mua trong 14 ngày qua, hãy xem chi tiết tại [Tạo tệp đối tượng theo quy tắc](../09-marketing-api/audience.md#doc-1739566532187138). Tệp đối tượng tương tác (Engagement Audiences), Tệp đối tượng hoạt động ứng dụng (App Activity Audiences), Tệp đối tượng lưu lượng trang web (Website Traffic Audiences) hoặc Tệp đối tượng thu thập khách hàng tiềm năng (Lead Generation Audiences) được tạo theo cách này.
   - Nếu bạn muốn tạo tệp đối tượng tương tự với tệp đối tượng sẵn có, bạn có thể tạo Lookalike Audience. Xem chi tiết tại [Tạo tệp đối tượng tương tự (Lookalike Audiences)](../09-marketing-api/audience.md#doc-1747012174934018).

2. Sau khi tạo tệp đối tượng, bạn có thể đưa vào hoặc loại trừ đối tượng trong **một** nhóm quảng cáo (ad group), hoặc áp dụng / hủy liên kết đối tượng trên **nhiều** nhóm quảng cáo:
   - Trong [/adgroup/create/](../12-api-reference/07-ad-groups-p2.md#doc-1739499616346114) hoặc [/adgroup/update/](../12-api-reference/07-ad-groups-p3.md#doc-1739586761631745), đưa vào/loại trừ tệp đối tượng trong **một** nhóm quảng cáo đơn lẻ:
     - Để nhắm mục tiêu (đưa vào) tệp đối tượng trong nhóm quảng cáo, hãy truyền các ID tệp đối tượng vào trường `audience_ids`.
     - Để loại trừ tệp đối tượng khỏi nhóm quảng cáo, hãy truyền các ID tệp đối tượng vào trường `excluded_audience_ids`.
   - Trong [/dmp/custom_audience/apply/](../12-api-reference/09-audience.md#doc-1758615097524225), áp dụng hoặc ngắt kết nối tệp đối tượng trên **nhiều** nhóm quảng cáo:
     - Để áp dụng tệp đối tượng cho các nhóm quảng cáo, hãy đặt `action_mode` là `Apply`. Bạn có thể chọn đưa vào hay loại trừ đối tượng khỏi nhóm quảng cáo bằng cách chỉ định `usage_mode` là `Include` hoặc `Exclude`.
     - Để ngắt kết nối tệp đối tượng khỏi các nhóm quảng cáo, hãy đặt `action_mode` là `Disconnect`. Bạn có thể ngắt kết nối tệp đối tượng đang được đưa vào hoặc loại trừ khỏi các nhóm quảng cáo của mình.

### Tài liệu liên quan (Related docs)

- [Audience API](../12-api-reference/09-audience.md#doc-1739940398505986)
- [Audience Management Guide](../09-marketing-api/audience.md#doc-1739566496956417)
