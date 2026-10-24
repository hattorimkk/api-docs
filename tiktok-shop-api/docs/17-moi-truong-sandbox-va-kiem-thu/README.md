# 17. Môi Trường Sandbox 2.0 & Công Cụ Kiểm Thử (Testing & Tools)

Để đảm bảo phần mềm hoạt động trơn tru trước khi chạy thực tế trên các cửa hàng kinh doanh thật, TikTok Shop cung cấp môi trường giả lập **Sandbox 2.0** cùng bộ công cụ kiểm thử tự động, tài khoản người mua và người bán thử nghiệm.

---

## 1. Môi Trường Sandbox 2.0 (TikTok Shop Sandbox)

- **Cổng đăng nhập Sandbox**: [https://partner.tiktokshop.com](https://partner.tiktokshop.com) > Chọn menu **Developer Tools** > **Sandbox**.
- **Đặc điểm nổi bật**:
  - Tách biệt 100% với môi trường Production, không sợ ảnh hưởng đến tồn kho hoặc số dư tiền tệ thật.
  - Cho phép tạo các shop bán hàng ảo tại nhiều khu vực (US, UK, VN, SEA).
  - Tự động sinh tài khoản người mua thử nghiệm (Test Buyer Accounts).
  - Cho phép mô phỏng đặt hàng, thanh toán giả lập và tự kích hoạt các trạng thái đơn hàng (từ `UNPAID` sang `AWAITING_SHIPMENT` hoặc hủy đơn) chỉ bằng một nút bấm.

---

## 2. Công Cụ Trực Tuyến & Bộ Công Cụ Hỗ Trợ

### 2.1. TikTok Shop API Testing Tool (API Explorer)
- Nằm trực tiếp trên thanh điều hướng Partner Center.
- Hỗ trợ chọn nhanh từng Endpoint, tự động điền các Header, tính sẵn chữ ký `sign` theo thời gian thực giúp bạn kiểm tra phản hồi API mà không cần tự viết mã.

### 2.2. Bộ Sưu Tập Postman (Postman Collection)
TikTok Shop cung cấp file cấu hình Postman chính thức kèm pre-request script tự động tính HMAC-SHA256 signature trước mỗi lần gửi request.
- Tải file Collection và Environment từ trang tài liệu Partner Center.
- Nhập vào Postman, điền `app_key` và `app_secret` trong Environment Variables là có thể kiểm thử toàn bộ 344 endpoints ngay lập tức.

### 2.3. Bộ SDK Mã Nguồn Mở Chính Thức (Official SDKs)
TikTok phát hành các bộ SDK giúp đóng gói sẵn việc tạo chữ ký và quản lý token:
- **Python**: `tiktok-shop-api-sdk`
- **Node.js**: `@tiktok-shop/api-sdk`
- **Golang**: `github.com/tiktokshop/open-sdk-go`
- **Java**: `com.tiktok.shop:open-sdk-java`

