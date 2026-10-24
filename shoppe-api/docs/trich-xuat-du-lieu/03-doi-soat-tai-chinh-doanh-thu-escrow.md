# 03. Hướng Dẫn Đối Soát Tài Chính & Doanh Thu (Escrow & Accounting)

Tài liệu này hướng dẫn cách trích xuất dữ liệu dòng tiền, doanh thu thực nhận và các khoản phí khấu trừ từ Shopee để phục vụ công tác kế toán và đối soát tài chính.

---

## 1. Cơ Chế Thanh Toán Ký Quỹ (Shopee Escrow Mechanism)

Shopee áp dụng cơ chế thanh toán ký quỹ (**Escrow**):
- Khi người mua thanh toán tiền hàng, Shopee sẽ giữ khoản tiền này tại tài khoản ký quỹ trung gian.
- Tiền **chỉ được giải ngân về Ví người bán (Seller Balance / Wallet)** sau khi đơn hàng chuyển sang trạng thái `COMPLETED` và người mua không phát sinh khiếu nại Trả hàng/Hoàn tiền trong thời hạn quy định.
- Khi tiền được giải ngân, một bản ghi **Escrow Record** được tạo ra kèm theo thời điểm giải ngân (`release_time`).

---

## 2. Công Thức Tính Doanh Thu Thực Nhận Của Shop

Số tiền thực tế người bán nhận về Ví (`escrow_amount`) được Shopee tính toán theo công thức:

$$\text{Doanh Thu Thực Nhận} = \text{Tổng Tiền Hàng Ban Đầu} - \text{Voucher/Giảm Giá Của Shop} - \text{Các Loại Phí Sàn} - \text{Phí Vận Chuyển Chênh Lệch} \pm \text{Điều Chỉnh}$$

### Bảng Giải Thích Các Loại Phí Khấu Trừ Từ Shopee:
| Tên Phí | Mã Trường JSON | Ý Nghĩa Nghiệp Vụ |
| :--- | :--- | :--- |
| **Phí Hoa Hồng (Commission Fee)** | `commission_fee` | Phí phần trăm tính trên giá trị đơn hàng áp dụng cho gian hàng Shopee Mall hoặc người bán thường theo chính sách sàn. |
| **Phí Dịch Vụ (Service Fee)** | `service_fee` | Phí tham gia các gói hỗ trợ bán hàng của Shopee như **Freeship Xtra**, **Hoàn Xu Xtra**, Live Voucher. |
| **Phí Thanh Toán (Transaction Fee)** | `transaction_fee` | Phí xử lý giao dịch thanh toán (thường từ 3% đến 5% tổng giá trị người mua trả). |
| **Phí Ship Thực Tế (Actual Shipping Fee)** | `actual_shipping_fee` | Cước vận chuyển do đơn vị giao hàng tính dựa trên cân nặng thực tế khi cân tại bưu cục. |
| **Trợ Giá Ship Từ Shopee (Shipping Rebate)** | `shopee_shipping_rebate` | Khoản Shopee hỗ trợ lại cho shop đối với các đơn hàng áp mã freeship. |

---

## 3. Quy Trình Trích Xuất Dữ Liệu Đối Soát

### Bước 1: Lấy danh sách các đơn đã giải ngân (`get_escrow_list`)
- **API**: `GET /api/v2/payment/get_escrow_list`
- **Lệnh cURL mẫu**:
```bash
curl -X GET "https://partner.shopeemobile.com/api/v2/payment/get_escrow_list?partner_id=123456&timestamp=1700000000&access_token=your_token&shop_id=98765432&sign=calculated_sign_here&release_time_from=1698790400&release_time_to=1700000000&page_size=100&page_no=1" \
  -H "Content-Type: application/json"
```

Phản hồi trả về danh sách các `order_sn` đã được giải ngân tiền trong khoảng thời gian chỉ định.

---

### Bước 2: Bóc tách bảng kê tài chính chi tiết (`get_escrow_detail`)
- **API**: `GET /api/v2/payment/get_escrow_detail`
- **Lệnh cURL mẫu**:
```bash
curl -X GET "https://partner.shopeemobile.com/api/v2/payment/get_escrow_detail?partner_id=123456&timestamp=1700000000&access_token=your_token&shop_id=98765432&sign=calculated_sign_here&order_sn=261023ABCD1234" \
  -H "Content-Type: application/json"
```

#### Cấu trúc đối tượng tài chính phản hồi (`response`):
```json
{
  "order_sn": "261023ABCD1234",
  "buyer_user_name": "khachhang_shopee",
  "order_income": {
    "escrow_amount": 218500,
    "buyer_total_amount": 250000,
    "cost_of_goods_sold": 250000,
    "seller_discount": 10000,
    "voucher_from_seller": 5000,
    "voucher_from_shopee": 20000,
    "commission_fee": 12000,
    "service_fee": 14500,
    "transaction_fee": 10000,
    "actual_shipping_fee": 18000,
    "shopee_shipping_rebate": 18000
  }
}
```

Trong ví dụ trên:
- Khách mua hàng thanh toán: **250.000 VNĐ**
- Tiền thực nhận về tài khoản người bán (`escrow_amount`): **218.500 VNĐ**
- Tổng phí sàn Shopee đã khấu trừ: **36.500 VNĐ** (gồm 12.000 phí hoa hồng + 14.500 phí dịch vụ + 10.000 phí thanh toán).

---

## 4. Kiểm Tra Lịch Sử Biến Động Số Dư Ví (`get_wallet_transaction_list`)

Để đối soát số tiền rút về tài khoản ngân hàng của doanh nghiệp:
- **API**: `GET /api/v2/payment/get_wallet_transaction_list`
- **Lệnh cURL mẫu**:
```bash
curl -X GET "https://partner.shopeemobile.com/api/v2/payment/get_wallet_transaction_list?partner_id=123456&timestamp=1700000000&access_token=your_token&shop_id=98765432&sign=calculated_sign_here&page_no=1&page_size=50&create_time_from=1698790400&create_time_to=1700000000" \
  -H "Content-Type: application/json"
```

