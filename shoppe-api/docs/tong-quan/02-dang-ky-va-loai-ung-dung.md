# 02. Đăng Ký Tài Khoản & Các Loại Ứng Dụng (App Types)

Tài liệu này hướng dẫn quy trình tạo tài khoản nhà phát triển trên Shopee Open Platform, phân loại các loại ứng dụng (App Types) và cách lấy thông tin xác thực (`partner_id`, `partner_key`).

---

## 1. Quy Trình Đăng Ký Tài Khoản Nhà Phát Triển

Để tích hợp API với Shopee, bạn cần thực hiện các bước đăng ký tại cổng [Shopee Open Platform Console](https://open.shopee.com):

1. **Truy cập trang đăng ký**: Vào `https://open.shopee.com` và chọn **Register / Đăng ký**.
2. **Chọn loại tài khoản nhà phát triển**:
   - **Cá nhân (Individual)**: Phù hợp cho việc thử nghiệm, phát triển đồ án hoặc cá nhân sở hữu 1 shop nhỏ.
   - **Doanh nghiệp (Corporate / Business)**: Yêu cầu cung cấp giấy phép đăng ký kinh doanh (ĐKKD) và mã số thuế. Bắt buộc nếu bạn phát triển phần mềm cho doanh nghiệp hoặc muốn xuất bản ứng dụng phục vụ nhiều người bán.
3. **Xác minh danh tính (KYC)**:
   - Điền thông tin người đại diện, số điện thoại, email công vụ.
   - Chờ Shopee xét duyệt thông tin (thường từ 1 - 3 ngày làm việc).

---

## 2. Phân Biệt Các Loại Ứng Dụng (App Types)

Khi tạo ứng dụng mới trong mục **App Management**, Shopee cung cấp 2 mô hình ứng dụng chính:

| Tiêu Chí | In-house App (Ứng dụng nội bộ) | Third-Party App (Ứng dụng Bên thứ ba / ISV) |
| :--- | :--- | :--- |
| **Mục đích** | Doanh nghiệp/Nhà bán hàng tự phát triển phần mềm (ERP/CRM nội bộ) để quản lý **chính các gian hàng của mình**. | Doanh nghiệp phần mềm (ISV) cung cấp dịch vụ quản lý bán hàng đa kênh cho **hàng nghìn nhà bán hàng khác nhau** trên thị trường. |
| **Quyền truy cập Shop** | Chỉ được phép kết nối với các Shop thuộc quyền sở hữu của công ty đăng ký ứng dụng. | Bất kỳ nhà bán hàng Shopee nào cũng có thể ủy quyền cho ứng dụng thông qua đường link OAuth. |
| **Xét duyệt Shopee** | Thủ tục xét duyệt nhanh chóng hơn. | Yêu cầu kiểm tra bảo mật khắt khe (Security Audit, Penetration Test Report) trước khi được cấp quyền Live. |
| **Yêu cầu IP Whitelist** | Khuyến nghị bắt buộc cấu hình dải IP cố định. | Bắt buộc cấu hình danh sách IP server để được phê duyệt truy cập dữ liệu nhạy cảm PII. |

---

## 3. Các Thông Tin Xác Thực Quan Trọng

Sau khi tạo Ứng dụng thành công trong Console, bạn sẽ được cấp các thông tin sau:

1. **`partner_id`**:
   - Là một số nguyên (Integer), ví dụ: `2004581`.
   - Được dùng công khai trong tất cả các request gửi đến Shopee.
2. **`partner_key`**:
   - Là một chuỗi mã bí mật (Secret String), ví dụ: `7466547a4b676a6b57717469796e62...`.
   > [!CAUTION]
   > `partner_key` tuyệt đối không được để lộ, không commit lên GitHub công khai, và không nhúng trực tiếp vào ứng dụng Mobile/Frontend. Mọi thao tác ký chữ ký số `sign` phải được thực hiện ở Backend Server của bạn.
3. **Redirect URL (Đường dẫn chuyển hướng OAuth)**:
   - URL trên máy chủ của bạn (phải có HTTPS), ví dụ: `https://api.yourdomain.com/v1/shopee/callback`.
   - Đây là nơi Shopee chuyển hướng người bán về kèm mã `code` sau khi họ đồng ý cấp quyền.

---

## 4. Quản Lý Quyền Hạn API (API Scopes)

Trong bảng điều khiển ứng dụng, Shopee quản lý quyền truy cập theo từng danh mục chức năng:
- **Order Management**: Quyền đọc và cập nhật đơn hàng.
- **Product Management**: Quyền xem, tạo và chỉnh sửa thông tin sản phẩm, giá bán, tồn kho.
- **Logistics Management**: Quyền cấu hình đơn vị vận chuyển, tạo vận đơn và in phiếu giao hàng.
- **Payment & Accounting**: Quyền trích xuất doanh thu, bảng kê tài chính và số dư ví.
- **Returns & Refunds**: Quyền xem và xử lý các khiếu nại hoàn tiền từ người mua.
- **Customer Service (Chat)**: Quyền gửi và nhận tin nhắn trò chuyện với khách hàng.

> [!TIP]
> Bạn nên bật đầy đủ các danh mục quyền cần thiết cho nghiệp vụ trích xuất dữ liệu trước khi gửi link ủy quyền cho Shop. Nếu sau này ứng dụng cần thêm quyền mới, người bán sẽ cần phải thực hiện ủy quyền lại một lần nữa.

