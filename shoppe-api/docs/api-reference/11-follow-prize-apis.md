# Tham Khảo API: Ưu Đãi Người Theo Dõi (Follow Prize APIs)

Tài liệu này cung cấp chi tiết đặc tả kỹ thuật và câu lệnh **cURL** cho các API trong phân hệ **Follow Prize (Ưu Đãi Người Theo Dõi)** của Shopee Open API v2.

---

## 1. Lấy Danh Sách Chiến Dịch (Get Follow Prize List)

- **Tên Endpoint**: `v2.follow_prize.get_follow_prize_list`
- **Đường dẫn**: `GET /api/v2/follow_prize/get_follow_prize_list`
- **Loại API**: Shop API

### Lệnh cURL mẫu:
```bash
curl -X GET "https://partner.shopeemobile.com/api/v2/follow_prize/get_follow_prize_list?partner_id=123456&timestamp=1700000000&access_token=c71a39d892ef65a43b1234567890abcd&shop_id=98765432&sign=calculated_sign_here&status=all&page_no=1&page_size=50" \
  -H "Content-Type: application/json"
```

---

## 2. Xem Chi Tiết Hiệu Quả Chiến Dịch (Get Follow Prize Detail)

- **Tên Endpoint**: `v2.follow_prize.get_follow_prize_detail`
- **Đường dẫn**: `GET /api/v2/follow_prize/get_follow_prize_detail`
- **Loại API**: Shop API

### Lệnh cURL mẫu:
```bash
curl -X GET "https://partner.shopeemobile.com/api/v2/follow_prize/get_follow_prize_detail?partner_id=123456&timestamp=1700000000&access_token=c71a39d892ef65a43b1234567890abcd&shop_id=98765432&sign=calculated_sign_here&campaign_id=88001122" \
  -H "Content-Type: application/json"
```

### Phản hồi mẫu (JSON):
```json
{
  "error": "",
  "message": "",
  "request_id": "...",
  "response": {
    "campaign_id": 88001122,
    "campaign_name": "Tặng Voucher 10K Cho Khách Mới Follow",
    "start_time": 1700000000,
    "end_time": 1702592000,
    "reward_type": 1,
    "usage_quantity": 500,
    "current_usage": 142,
    "min_basket_price": 150000.00,
    "discount_amount": 10000.00,
    "new_followers_count": 380
  }
}
```

---

## 3. Tạo Mới Chiến Dịch Follow Prize (Add Follow Prize)

- **Tên Endpoint**: `v2.follow_prize.add_follow_prize`
- **Đường dẫn**: `POST /api/v2/follow_prize/add_follow_prize`
- **Loại API**: Shop API

### Lệnh cURL mẫu:
```bash
curl -X POST "https://partner.shopeemobile.com/api/v2/follow_prize/add_follow_prize?partner_id=123456&timestamp=1700000000&access_token=c71a39d892ef65a43b1234567890abcd&shop_id=98765432&sign=calculated_sign_here" \
  -H "Content-Type: application/json" \
  -d '{
    "campaign_name": "Tặng Voucher 10K Cho Khách Mới Follow",
    "start_time": 1700000000,
    "end_time": 1702592000,
    "reward_type": 1,
    "usage_quantity": 1000,
    "min_basket_price": 150000.00,
    "discount_amount": 10000.00
  }'
```
