# Tham Khảo API: Trả Hàng & Hoàn Tiền (Returns APIs)

Tài liệu này cung cấp chi tiết đặc tả kỹ thuật và câu lệnh **cURL** cho các API quản lý và xử lý khiếu nại Trả hàng / Hoàn tiền của Shopee Open API v2.

---

## 1. Lấy Danh Sách Khiếu Nại Trả Hàng (Get Return List)

- **Tên Endpoint**: `v2.returns.get_return_list`
- **Đường dẫn**: `GET /api/v2/returns/get_return_list`
- **Loại API**: Shop API

### Lệnh cURL mẫu:
```bash
curl -X GET "https://partner.shopeemobile.com/api/v2/returns/get_return_list?partner_id=123456&timestamp=1700000000&access_token=c71a39d892ef65a43b1234567890abcd&shop_id=98765432&sign=calculated_sign_here&page_no=1&page_size=50&status=REQUESTED" \
  -H "Content-Type: application/json"
```

### Phản hồi mẫu (JSON):
```json
{
  "error": "",
  "message": "",
  "request_id": "...",
  "response": {
    "return": [
      {
        "return_sn": "261023RET00123",
        "order_sn": "261023ABCD1234",
        "status": "REQUESTED",
        "refund_amount": 350000.00,
        "currency": "VND",
        "create_time": 1700015000
      }
    ],
    "more": false
  }
}
```

---

## 2. Lấy Chi Tiết Khiếu Nại & Bằng Chứng Ảnh/Video (Get Return Detail)

- **Tên Endpoint**: `v2.returns.get_return_detail`
- **Đường dẫn**: `GET /api/v2/returns/get_return_detail`
- **Loại API**: Shop API

### Lệnh cURL mẫu:
```bash
curl -X GET "https://partner.shopeemobile.com/api/v2/returns/get_return_detail?partner_id=123456&timestamp=1700000000&access_token=c71a39d892ef65a43b1234567890abcd&shop_id=98765432&sign=calculated_sign_here&return_sn=261023RET00123" \
  -H "Content-Type: application/json"
```

### Phản hồi mẫu (JSON):
```json
{
  "error": "",
  "message": "",
  "request_id": "...",
  "response": {
    "return_sn": "261023RET00123",
    "order_sn": "261023ABCD1234",
    "reason": "DAMAGED",
    "text_reason": "Bình giữ nhiệt bị móp nắp trong quá trình vận chuyển",
    "image": [
      "https://down-vn.img.susercontent.com/file/evidence_photo_1.jpg"
    ],
    "status": "REQUESTED",
    "refund_amount": 350000.00,
    "is_partial_quantity_return": false
  }
}
```

---

## 3. Chấp Thuận Hoàn Tiền (Confirm Return)

- **Tên Endpoint**: `v2.returns.confirm`
- **Đường dẫn**: `POST /api/v2/returns/confirm`
- **Loại API**: Shop API

### Lệnh cURL mẫu:
```bash
curl -X POST "https://partner.shopeemobile.com/api/v2/returns/confirm?partner_id=123456&timestamp=1700000000&access_token=c71a39d892ef65a43b1234567890abcd&shop_id=98765432&sign=calculated_sign_here" \
  -H "Content-Type: application/json" \
  -d '{
    "return_sn": "261023RET00123"
  }'
```

---

## 4. Khiếu Nại Tranh Chấp Lên Sàn Shopee (Dispute Return)

- **Tên Endpoint**: `v2.returns.dispute`
- **Đường dẫn**: `POST /api/v2/returns/dispute`
- **Loại API**: Shop API

### Lệnh cURL mẫu:
```bash
curl -X POST "https://partner.shopeemobile.com/api/v2/returns/dispute?partner_id=123456&timestamp=1700000000&access_token=c71a39d892ef65a43b1234567890abcd&shop_id=98765432&sign=calculated_sign_here" \
  -H "Content-Type: application/json" \
  -d '{
    "return_sn": "261023RET00123",
    "email": "cskh@yourbrand.vn",
    "dispute_reason": "NON_RECEIPT",
    "dispute_text_reason": "Shop đã đóng hàng đúng mẫu có camera kiểm tra. Khách gửi hàng hoàn về không đúng sản phẩm của Shop.",
    "image": [
      "https://your-domain.com/packing_proof_1.jpg"
    ]
  }'
```
