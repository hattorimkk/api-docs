# Tham Khảo API: Marketing & Khuyến Mãi (Discount & Promotion APIs)

Tài liệu này cung cấp chi tiết đặc tả kỹ thuật và câu lệnh **cURL** cho các API quản lý chương trình khuyến mãi, mã giảm giá và combo ưu đãi của Shopee Open API v2.

---

## 1. Quản Lý Chương Trình Giảm Giá Của Shop (Shop Discount)

### Lấy danh sách chương trình giảm giá (`get_discount_list`):
```bash
curl -X GET "https://partner.shopeemobile.com/api/v2/discount/get_discount_list?partner_id=123456&timestamp=1700000000&access_token=c71a39d892ef65a43b1234567890abcd&shop_id=98765432&sign=calculated_sign_here&discount_status=ALL&page_no=1&page_size=50" \
  -H "Content-Type: application/json"
```

### Lấy chi tiết sản phẩm trong chương trình (`get_discount`):
```bash
curl -X GET "https://partner.shopeemobile.com/api/v2/discount/get_discount?partner_id=123456&timestamp=1700000000&access_token=c71a39d892ef65a43b1234567890abcd&shop_id=98765432&sign=calculated_sign_here&discount_id=998877" \
  -H "Content-Type: application/json"
```

---

## 2. Quản Lý Mã Giảm Giá Của Shop (Voucher)

### Lấy danh sách Voucher của shop (`get_voucher_list`):
```bash
curl -X GET "https://partner.shopeemobile.com/api/v2/voucher/get_voucher_list?partner_id=123456&timestamp=1700000000&access_token=c71a39d892ef65a43b1234567890abcd&shop_id=98765432&sign=calculated_sign_here&status=ALL&page_no=1&page_size=50" \
  -H "Content-Type: application/json"
```

### Phản hồi mẫu (JSON):
```json
{
  "error": "",
  "message": "",
  "request_id": "...",
  "response": {
    "voucher_list": [
      {
        "voucher_id": 12345678,
        "voucher_code": "ANTIGRAV10K",
        "voucher_name": "Giảm 10K Đơn Từ 150K",
        "voucher_type": 1,
        "reward_type": 1,
        "discount_amount": 10000.00,
        "min_basket_price": 150000.00,
        "usage_quantity": 500,
        "current_usage": 89,
        "start_time": 1700000000,
        "end_time": 1702592000
      }
    ],
    "more": false
  }
}
```

---

## 3. Quản Lý Combo Khuyến Mãi (Bundle Deal)

### Lấy danh sách combo mua kèm giảm sâu:
```bash
curl -X GET "https://partner.shopeemobile.com/api/v2/bundle_deal/get_bundle_deal_list?partner_id=123456&timestamp=1700000000&access_token=c71a39d892ef65a43b1234567890abcd&shop_id=98765432&sign=calculated_sign_here&page_size=50&time_status=ALL" \
  -H "Content-Type: application/json"
```
