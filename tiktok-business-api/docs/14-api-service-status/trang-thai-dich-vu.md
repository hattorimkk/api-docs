# Trang trạng thái dịch vụ API (API Service Status Page)

> Phân hệ: Hướng dẫn chung > Trang trạng thái dịch vụ API.
> Hướng dẫn tra cứu tình trạng hoạt động thực tế, sự cố gián đoạn dịch vụ và lịch bảo trì của hệ thống TikTok Business API.

---

<a id="doc-1847461383861378"></a>
<!-- doc_id: 1847461383861378 -->
## 1. Tổng quan về Trang trạng thái dịch vụ API

Trang trạng thái dịch vụ API ([API Service Status Page](https://business-api.tiktok.com/portal/status)) là cổng thông tin chính thức giúp các nhà phát triển theo dõi tình trạng sẵn sàng của hệ thống TikTok Business API. 

Trang này hiển thị:
- **Tình trạng dịch vụ thời gian thực (Real-time Status):** Cho biết toàn bộ hệ thống API hay từng phân hệ cụ thể (Authentication, Campaign Management, Reporting, Webhooks, v.v.) đang hoạt động bình thường (`Operational`), bị suy giảm hiệu năng (`Degraded Performance`) hay gặp sự cố gián đoạn (`Service Outage`).
- **Thông báo sự cố (Incident Notifications):** Cập nhật tiến độ khắc phục sự cố kỹ thuật từ đội ngũ kỹ sư TikTok.
- **Lịch bảo trì định kỳ (Scheduled Maintenance):** Thông báo trước các khoảng thời gian hệ thống tiến hành nâng cấp hoặc bảo trì định kỳ để các đối tác chủ động điều chỉnh lịch trình gọi API và các tác vụ ETL tự động.

---

## 2. Các trạng thái dịch vụ

Hệ thống theo dõi và phân loại trạng thái theo 4 mức độ:

| Trạng thái | Biểu tượng / Màu sắc | Ý nghĩa | Hành động khuyến nghị |
|---|---|---|---|
| **Operational** | Xanh lá | Toàn bộ dịch vụ hoạt động bình thường, độ trễ và tỷ lệ lỗi nằm trong ngưỡng tiêu chuẩn. | Thực hiện các yêu cầu API bình thường. |
| **Degraded Performance** | Vàng | Dịch vụ vẫn khả dụng nhưng thời gian phản hồi có thể kéo dài hơn bình thường hoặc một số lượng nhỏ request bị timeout. | Tăng thời gian chờ (timeout) cho HTTP client và chuẩn bị cơ chế retry tự động. |
| **Partial Outage** | Cam | Một số endpoint hoặc tính năng cụ thể gặp sự cố (ví dụ: tạo chiến dịch bị lỗi nhưng truy vấn báo cáo vẫn hoạt động). | Kiểm tra chi tiết thông báo sự cố để biết phân hệ bị ảnh hưởng và tạm hoãn các tác vụ liên quan. |
| **Major Outage** | Đỏ | Sự cố gián đoạn nghiêm trọng trên quy mô lớn ảnh hưởng đến phần lớn các endpoint cốt lõi. | Tạm dừng các tác vụ tự động để tránh làm nghẽn hàng đợi (queue) và theo dõi thông tin cập nhật trên trang trạng thái. |

---

## 3. Cách thức theo dõi và đăng ký thông báo

1. **Truy cập trực tiếp:** Truy cập định kỳ cổng [TikTok Business API Status](https://business-api.tiktok.com/portal/status).
2. **Đăng ký nhận cảnh báo:** Bạn có thể đăng ký nhận email hoặc cấu hình Webhook để tự động nhận thông báo khi có sự cố phát sinh hoặc khi sự cố được giải quyết thành công.
3. **Chiến lược phục hồi trong hệ thống tích hợp:**
   - Khi phát hiện mã lỗi `500`, `502`, `503`, `504` liên tục, hãy kiểm tra Trang trạng thái dịch vụ trước khi gửi yêu cầu hỗ trợ (Support Ticket).
   - Tích hợp giải thuật Exponential Backoff với jitter trong các kịch bản gọi API để tự động thích ứng với các khoảng thời gian dịch vụ bị suy giảm hiệu năng.

