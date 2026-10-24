# 04. Chính Sách Bảo Vệ Dữ Liệu Khách Hàng (Buyer PII Protection & Data Masking)

Tài liệu này giải thích chi tiết cơ chế bảo vệ thông tin định danh cá nhân của người mua (Personally Identifiable Information - PII) trên Shopee Open Platform và các quy định pháp lý kỹ thuật liên quan.

---

## 1. Cơ Chế Che Mờ Dữ Liệu Mặc Định (Default Data Masking)

Theo quy định bảo vệ dữ liệu người dùng quốc tế (GDPR, PDPA) và Nghị định 13/2023/NĐ-CP về bảo vệ dữ liệu cá nhân tại Việt Nam, Shopee **mặc định che mờ (masking) toàn bộ thông tin nhạy cảm của người mua** khi trả về qua Open API v2.

### Các trường dữ liệu bị ảnh hưởng:
- **Tên người nhận hàng (`recipient_address.name`)**: Bị che thành ký tự sao, ví dụ: `Ngu*** V** A**`.
- **Số điện thoại (`recipient_address.phone`)**: Bị che một phần, ví dụ: `090*****89`.
- **Địa chỉ chi tiết (`recipient_address.full_address`)**: Bị che số nhà, tên đường chi tiết, ví dụ: `Số ** đường **, Phường Bến Nghé, Quận 1, TP. Hồ Chí Minh`.

### Các API trả về dữ liệu bị che mờ:
1. `GET /api/v2/order/get_order_detail`: Chi tiết thông tin giao nhận đơn hàng.
2. `GET /api/v2/returns/get_return_detail`: Địa chỉ gửi trả hàng của người mua.
3. `GET /api/v2/logistics/get_tracking_info`: Thông tin người nhận trong lịch trình vận chuyển.

---

## 2. Tác Động Đến Bài Toán Trích Xuất Dữ Liệu (Data Extraction Impact)

> [!TIP]
> **Tin vui cho các kỹ sư dữ liệu (Data Engineers & BI Analysts):**
> Nếu mục tiêu của bạn là xây dựng hệ thống **Báo cáo kinh doanh (BI Dashboard), Phân tích doanh thu, Hiệu suất sản phẩm (SKU Performance), Đối soát dòng tiền (Escrow Reconciliation) hoặc Đồng bộ tồn kho (Inventory Sync)**, việc dữ liệu PII bị che mờ **HOÀN TOÀN KHÔNG ẢNH HƯỞNG** đến công việc của bạn!
>
> Toàn bộ các thông số quan trọng sau **vẫn được trả về 100% đầy đủ, chính xác**:
> - Mã đơn hàng (`order_sn`), Trạng thái đơn (`order_status`), Thời gian tạo/hoàn thành.
> - Danh sách sản phẩm mua (`item_id`, `item_name`, `item_sku`), Số lượng, Đơn giá.
> - Tổng giá trị đơn hàng, Phí vận chuyển thực tế, Giảm giá của Shop, Giảm giá của Shopee.
> - Tỉnh/Thành phố (`city`), Quận/Huyện (`district`) để phân tích biểu đồ nhiệt địa lý.
> - Doanh thu ròng, Phí sàn chi tiết (Hoa hồng, Dịch vụ, Phí thanh toán).

---

## 3. Quy Trình Xin Cấp Quyền Đọc Dữ Liệu PII Đầy Đủ (Unmasked PII)

Chỉ những ứng dụng có nghiệp vụ vận hành thực tế bắt buộc (ví dụ: Hệ thống ERP tự in tem phiếu vận chuyển ngoài, Đội xe giao hàng nội bộ) mới được phép xin mở quyền đọc PII rõ nét.

Quy trình phê duyệt gồm 4 bước nghiêm ngặt trên Console:
1. **Khai báo tính cấp thiết (PII Necessity Declaration)**:
   - Nêu rõ lý do nghiệp vụ tại sao cần đọc số điện thoại và địa chỉ đầy đủ của người mua.
2. **Khai báo IP tĩnh cố định (Server IP Whitelist)**:
   - Chỉ cho phép các máy chủ được định danh IP tĩnh gửi request lấy PII.
3. **Nộp Báo cáo Kiểm thử Xâm nhập (Penetration Test Report)**:
   - Ứng dụng phải được một đơn vị an ninh mạng độc lập bên thứ ba (đạt chứng chỉ quốc tế như CREST, OSCP) thực hiện kiểm thử xâm nhập (PenTest) toàn diện hệ thống máy chủ, cơ sở dữ liệu và API trong vòng 12 tháng gần nhất.
   - Nộp toàn bộ biên bản kiểm thử và chứng minh đã vá 100% các lỗ hổng bảo mật mức độ Cao (High) và Nghiêm trọng (Critical).
4. **Cam kết Tuân thủ Bảo mật & Lưu trữ (Data Retention SLA)**:
   - Dữ liệu PII của người mua chỉ được lưu trữ tối đa trong thời gian xử lý đơn hàng (thường không quá 30 ngày).
   - Sau khi đơn hàng hoàn tất, hệ thống của bạn phải tự động xóa hoặc mã hóa dữ liệu PII cá nhân.
   - Định kỳ Shopee sẽ quét ngẫu nhiên và có quyền thu hồi chứng chỉ API nếu phát hiện ứng dụng làm rò rỉ dữ liệu người dùng.

