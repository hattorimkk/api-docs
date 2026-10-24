# Tham Khảo API: Tài Chính & Quyết Toán (Payment & Escrow APIs)

Tài liệu này cung cấp chi tiết đặc tả kỹ thuật và câu lệnh **cURL** cho toàn bộ các API trong phân hệ Quyết toán, Đối soát doanh thu và Ví người bán của Shopee Open API v2.

---

## 1. Lấy Danh Sách Đơn Quyết Toán (Get Escrow List)

- **Tên Endpoint**: `v2.payment.get_escrow_list`
- **Đường dẫn**: `GET /api/v2/payment/get_escrow_list`
- **Loại API**: Shop API

### Tham số URL (Query Parameters):
| Tham Số | Kiểu Dữ Liệu | Bắt Buộc | Mô Tả |
| :--- | :--- | :--- | :--- |
| `release_time_from` | int64 | Có | Thời điểm giải ngân bắt đầu (Unix timestamp). |
| `release_time_to` | int64 | Có | Thời điểm giải ngân kết thúc (Unix timestamp). Khoảng cách $\le$ 15 ngày. |
| `page_size` | int32 | Có | Số lượng đơn hàng mỗi trang (tối đa 100). |
| `page_no` | int32 | Có | Số thứ tự trang (bắt đầu từ 1). |

### Lệnh cURL mẫu:
```bash
curl -X GET "https://partner.shopeemobile.com/api/v2/payment/get_escrow_list?partner_id=123456&timestamp=1700000000&access_token=c71a39d892ef65a43b1234567890abcd&shop_id=98765432&sign=calculated_sign_here&release_time_from=1698790400&release_time_to=1700000000&page_size=50&page_no=1" \
  -H "Content-Type: application/json"
```

### Phản hồi mẫu (JSON):
```json
{
  "error": "",
  "message": "",
  "request_id": "...",
  "response": {
    "escrow_list": [
      {
        "order_sn": "261023ABCD1234",
        "payout_amount": 218500.00
      }
    ],
    "more": false
  }
}
```

---

## 2. Bóc Tách Bảng Kê Tài Chính Chi Tiết Đơn Hàng (Get Escrow Detail)

- **Tên Endpoint**: `v2.payment.get_escrow_detail`
- **Đường dẫn**: `GET /api/v2/payment/get_escrow_detail`
- **Loại API**: Shop API

### Lệnh cURL mẫu:
```bash
curl -X GET "https://partner.shopeemobile.com/api/v2/payment/get_escrow_detail?partner_id=123456&timestamp=1700000000&access_token=c71a39d892ef65a43b1234567890abcd&shop_id=98765432&sign=calculated_sign_here&order_sn=261023ABCD1234" \
  -H "Content-Type: application/json"
```

### Phản hồi mẫu chi tiết (JSON):
```json
{
  "error": "",
  "message": "",
  "request_id": "...",
  "response": {
    "order_sn": "261023ABCD1234",
    "buyer_user_name": "khachhang_vip",
    "order_income": {
      "escrow_amount": 218500.00,
      "buyer_total_amount": 250000.00,
      "original_cost_of_goods_sold": 250000.00,
      "seller_discount": 10000.00,
      "shopee_discount": 0.00,
      "voucher_from_seller": 5000.00,
      "voucher_from_shopee": 20000.00,
      "commission_fee": 12000.00,
      "service_fee": 14500.00,
      "transaction_fee": 10000.00,
      "actual_shipping_fee": 18000.00,
      "shopee_shipping_rebate": 18000.00,
      "cross_border_tax": 0.00
    }
  }
}
```

---

## 3. Lấy Biến Động Số Dư Ví (Get Wallet Transaction List)

- **Tên Endpoint**: `v2.payment.get_wallet_transaction_list`
- **Đường dẫn**: `GET /api/v2/payment/get_wallet_transaction_list`
- **Loại API**: Shop API

### Lệnh cURL mẫu:
```bash
curl -X GET "https://partner.shopeemobile.com/api/v2/payment/get_wallet_transaction_list?partner_id=123456&timestamp=1700000000&access_token=c71a39d892ef65a43b1234567890abcd&shop_id=98765432&sign=calculated_sign_here&page_no=1&page_size=50&create_time_from=1698790400&create_time_to=1700000000" \
  -H "Content-Type: application/json"
```

---

## 4. Lấy Chi Tiết Lệnh Rút Tiền (Get Payout Detail)

- **Tên Endpoint**: `v2.payment.get_payout_detail`
- **Đường dẫn**: `GET /api/v2/payment/get_payout_detail`
- **Loại API**: Shop API

### Lệnh cURL mẫu:
```bash
curl -X GET "https://partner.shopeemobile.com/api/v2/payment/get_payout_detail?partner_id=123456&timestamp=1700000000&access_token=c71a39d892ef65a43b1234567890abcd&shop_id=98765432&sign=calculated_sign_here&payout_id=PO123456789" \
  -H "Content-Type: application/json"
```
