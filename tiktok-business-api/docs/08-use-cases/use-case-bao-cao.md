# Use case: Báo cáo

Tài liệu này hướng dẫn các bước khởi chạy báo cáo hiệu suất đồng bộ (synchronous) hoặc bất đồng bộ (asynchronous) bằng Reporting API của TikTok. Bạn sẽ tìm hiểu về điều kiện tiên quyết, phân quyền truy cập, danh sách cho phép (allowlist) và quy trình gọi các endpoint để trích xuất dữ liệu đa chiều phục vụ nhu cầu phân tích và xây dựng bảng điều khiển (dashboard) doanh nghiệp.

## Báo cáo (`Reporting`)
<a id="doc-1758528841973762"></a>
<!-- doc_id: 1758528841973762 -->

> Đường dẫn: Use Cases > Reporting

Bài viết này hướng dẫn bạn từng bước chạy báo cáo đồng bộ (synchronous report) hoặc báo cáo bất đồng bộ (asynchronous report).

### Giới thiệu (Introduction)

Đôi khi việc tích hợp dữ liệu phân mảnh từ nhiều tài khoản quảng cáo khác nhau có thể gặp nhiều khó khăn. Reporting API cho phép bạn lấy dữ liệu hiệu suất của các tài khoản quảng cáo theo những chiều dữ liệu (dimensions) và độ chi tiết (granularities) tùy chỉnh. Bạn có thể khởi chạy báo cáo đồng bộ hoặc bất đồng bộ trên các loại báo cáo khác nhau.

**Bạn có thể sử dụng Reporting API để trích xuất các dữ liệu quan trọng nhằm tạo bảng điều khiển (dashboard) tùy chỉnh theo nhu cầu doanh nghiệp. Việc trích xuất báo cáo bằng API mang lại hiệu quả cao hơn và độ linh hoạt vượt trội.**

### Điều kiện tiên quyết (Prerequisites)

- Bạn đã được cấp quyền truy cập TikTok API for Business. Xem chi tiết tại [Bắt đầu - Quy trình từng bước](../04-get-started/bat-dau.md#doc-1735713609895937).
  - Để chạy báo cáo, bạn cần có các quyền liên quan. Xem **Tham chiếu API (API Reference)** để biết quyền cần thiết cho từng endpoint và xem [Cập nhật quyền ứng dụng](../04-get-started/bat-dau.md#doc-1738855280338946) để biết cách định cấu hình quyền.
- Báo cáo bất đồng bộ (asynchronous report) hiện là tính năng chỉ dành cho danh sách cho phép (allowlist-only). Nếu muốn truy cập tính năng này, vui lòng nộp đơn đăng ký thông qua trang [Quản lý danh sách cho phép (Allowlist Management)](https://ads.tiktok.com/marketing_api/blog/detail/7102266224578396162).

### Các bước thực hiện (Steps)

1. Sử dụng endpoint [/report/integrated/get/](../12-api-reference/58-reporting.md#doc-1740302848100353) để chạy báo cáo đồng bộ. Xem [Chạy báo cáo đồng bộ](../09-marketing-api/bao-cao-p1.md#doc-1738864778664961) để biết các bước chi tiết.

> [!NOTE]
> Các loại báo cáo khác nhau hỗ trợ các chiều dữ liệu (dimensions), chỉ số (metrics) và bộ lọc (filters) khác nhau; bạn có thể xem các bài viết tương ứng trong mục Loại báo cáo (Report types) để biết chi tiết.

Dưới đây là một ví dụ về việc truy vấn tổng mức tiêu chi phí của nhà quảng cáo trong một khoảng thời gian nhất định.

2. Sử dụng các endpoint [/report/task/create/](../12-api-reference/58-reporting.md#doc-1740302766489602), [/report/task/check/](../12-api-reference/58-reporting.md#doc-1740302781443073) và [/report/task/download/](../12-api-reference/58-reporting.md#doc-1740302808815618) để chạy báo cáo bất đồng bộ. Xem [Chạy báo cáo bất đồng bộ](../09-marketing-api/bao-cao-p1.md#doc-1738864800380930) để biết các bước chi tiết.

> [!NOTE]
> Các loại báo cáo khác nhau hỗ trợ các chiều dữ liệu, chỉ số và bộ lọc khác nhau; bạn có thể xem các bài viết tương ứng trong mục Loại báo cáo (Report types) để biết chi tiết.

Dưới đây là một ví dụ về việc truy vấn lượt nhấp (clicks) của một quảng cáo được nhóm theo giờ trong một khoảng thời gian nhất định.

### Tài liệu liên quan (Related docs)

- [Reporting API](../12-api-reference/58-reporting.md#doc-1740302665828417)
- [Hướng dẫn Báo cáo (Reporting Guide)](../09-marketing-api/bao-cao-p1.md#doc-1738864739862530)
  - [Độ trễ dữ liệu cho báo cáo (Data latency for reports)](../09-marketing-api/bao-cao-p4.md#doc-1738864894606337)
  - [Các thực hành tốt nhất để giảm lỗi quá thời gian trong báo cáo đồng bộ (Best practices to reduce timeouts in synchronous reports)](../09-marketing-api/bao-cao-p4.md#doc-1738864817670145)
