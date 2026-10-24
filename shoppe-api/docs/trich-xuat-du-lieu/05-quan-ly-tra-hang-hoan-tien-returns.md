# 05. Hướng Dẫn Quản Lý Trả Hàng & Hoàn Tiền (Returns & Refunds)

Tài liệu này hướng dẫn cách trích xuất danh sách khiếu nại, lý do khách trả hàng, hình ảnh bằng chứng và xử lý hoàn tiền trên Shopee Open Platform.

---

## 1. Cơ Chế Khiếu Nại Trả Hàng Trên Shopee

- **Mã định danh khiếu nại (`return_sn`)**:
  - Khi người mua gửi yêu cầu trả hàng, hệ thống Shopee sinh ra một mã định danh duy nhất gọi là `return_sn`.
  - **Lưu ý**: Một đơn hàng (`order_sn`) có thể có nhiều `return_sn` nếu khách hàng yêu cầu trả nhiều sản phẩm khác nhau ở các thời điểm khác nhau hoặc yêu cầu trả hàng một phần (`is_partial_quantity_return = true`).

---

## 2. Quy Trình Trích Xuất Dữ Liệu Khiếu Nại

### Bước 1: Lấy danh sách các yêu cầu trả hàng (`get_return_list`)
- **API**: `GET /api/v2/returns/get_return_list`
- **Lệnh cURL mẫu**:
```bash
curl -X GET "https://partner.shopeemobile.com/api/v2/returns/get_return_list?partner_id=123456&timestamp=1700000000&access_token=your_token&shop_id=98765432&sign=calculated_sign_here&page_no=1&page_size=50&status=REQUESTED" \
  -H "Content-Type: application/json"
```

#### Các trạng thái khiếu nại chính:
- `REQUESTED`: Khách vừa tạo yêu cầu, chờ Shop phản hồi.
- `ACCEPTED`: Shop hoặc Shopee đã chấp thuận cho khách hoàn hàng.
- `CANCELLED`: Người mua đã chủ động rút yêu cầu hoàn tiền.
- `JUDGING`: Shopee đang thụ lý bằng chứng và phân xử khiếu nại.
- `REFUND_PAID`: Tiền đã hoàn lại cho tài khoản người mua.
- `CLOSED`: Quy trình khiếu nại đã đóng hoàn tất.

---

### Bước 2: Xem chi tiết nguyên nhân và bằng chứng (`get_return_detail`)
- **API**: `GET /api/v2/returns/get_return_detail`
- **Lệnh cURL mẫu**:
```bash
curl -X GET "https://partner.shopeemobile.com/api/v2/returns/get_return_detail?partner_id=123456&timestamp=1700000000&access_token=your_token&shop_id=98765432&sign=calculated_sign_here&return_sn=261023RET00123" \
  -H "Content-Type: application/json"
```

#### Dữ liệu chi tiết trả về:
- `reason`: Lý do khiếu nại chuẩn (Hàng lỗi, Giao sai mẫu, Hàng bể vỡ, Hàng giả/nhái, Không nhận được hàng).
- `text_reason`: Lời mô tả giải thích thêm từ người mua.
- `image`: Danh sách các URL hình ảnh do người mua chụp chụp tải lên làm bằng chứng.
- `videos`: Danh sách video quay cảnh mở hộp / kiểm tra sản phẩm.
- `refund_amount`: Số tiền người mua yêu cầu hoàn lại.
- `is_partial_quantity_return`: Cờ đánh dấu có phải trả hàng một phần số lượng hay không.
- `tracking_number`: Mã vận đơn gửi trả hàng ngược về kho của Shop.

---

## 3. Các API Thao Tác Phản Hồi Khiếu Nại (Actions)

1. **Đồng ý hoàn tiền (`v2.returns.confirm`)**:
   - Nếu lỗi thuộc về Shop hoặc đồng ý hỗ trợ người mua, gọi API này để hệ thống tự động hoàn tiền cho khách.
2. **Từ chối và khiếu nại lên Shopee (`v2.returns.dispute`)**:
   - Nếu khách hàng gian lận, tráo hàng, hoặc hàng gửi về không còn nguyên vẹn, Shop gửi lý do khiếu nại kèm hình ảnh/video bằng chứng đóng gói để Shopee can thiệp bồi thường.

