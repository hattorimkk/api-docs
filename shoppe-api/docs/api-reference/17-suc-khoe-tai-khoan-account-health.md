# Tham Khảo API: Sức Khỏe Tài Khoản & Chỉ Số Vận Hành (Account Health)

Tài liệu này cung cấp chi tiết đặc tả kỹ thuật và câu lệnh **cURL** cho phân hệ **Sức Khỏe Tài Khoản & Điểm Phạt Gian Hàng (`v2.account_health`)** trong Shopee Open API v2.

---

## 1. Tầm Quan Trọng Của Account Health Trong Vận Hành

Theo quy chuẩn của Shopee, gian hàng phải duy trì các chỉ số vận hành trên mức chuẩn để không bị tính **Điểm Phạt Sao Quả Tạ (Penalty Points)** và không bị giới hạn số lượng sản phẩm đăng bán:
1. **Tỷ Lệ Đơn Hàng Không Thành Công (Non-fulfillment Rate - NFR)**: Mục tiêu `< 10%`.
2. **Tỷ Lệ Giao Hàng Trễ (Late Shipment Rate - LSR)**: Mục tiêu `< 10%`.
3. **Tỷ Lệ Phản Hồi Chat (Chat Response Rate - CRR)**: Mục tiêu `> 85%`.
4. **Thời Gian Phản Hồi Chat Trung Bình**: Dưới 12 giờ.

---

## 2. Lấy Chỉ Số Sức Khỏe Tài Khoản (Get Shop Performance)

- **Tên Endpoint**: `v2.account_health.shop_performance`
- **Đường dẫn**: `GET /api/v2/account_health/shop_performance`
- **Loại API**: Shop API

### Lệnh cURL mẫu:
```bash
curl -X GET "https://partner.shopeemobile.com/api/v2/account_health/shop_performance?partner_id=123456&timestamp=1700000000&access_token=c71a39d892ef65a43b1234567890abcd&shop_id=98765432&sign=calculated_sign_here" \
  -H "Content-Type: application/json"
```

### Phản hồi mẫu (JSON):
```json
{
  "error": "",
  "message": "",
  "request_id": "9933ccaa22110099",
  "response": {
    "metric_list": [
      {
        "metric_id": "non_fulfillment_rate",
        "metric_name": "Tỷ lệ đơn không hoàn tất",
        "current_value": "1.8%",
        "target_value": "< 10.0%",
        "status": "GOOD"
      },
      {
        "metric_id": "late_shipment_rate",
        "metric_name": "Tỷ lệ giao hàng trễ",
        "current_value": "2.1%",
        "target_value": "< 10.0%",
        "status": "GOOD"
      },
      {
        "metric_id": "chat_response_rate",
        "metric_name": "Tỷ lệ phản hồi chat",
        "current_value": "98.5%",
        "target_value": ">= 85.0%",
        "status": "EXCELLENT"
      },
      {
        "metric_id": "overall_review_rating",
        "metric_name": "Đánh giá trung bình shop",
        "current_value": "4.92",
        "target_value": ">= 4.5",
        "status": "EXCELLENT"
      }
    ]
  }
}
```

---

## 3. Lấy Danh Sách Điểm Phạt Sao Quả Tạ (Shop Penalty Points)

- **Tên Endpoint**: `v2.account_health.shop_penalty`
- **Đường dẫn**: `GET /api/v2/account_health/shop_penalty`
- **Loại API**: Shop API

### Lệnh cURL mẫu:
```bash
curl -X GET "https://partner.shopeemobile.com/api/v2/account_health/shop_penalty?partner_id=123456&timestamp=1700000000&access_token=c71a39d892ef65a43b1234567890abcd&shop_id=98765432&sign=calculated_sign_here" \
  -H "Content-Type: application/json"
```

### Phản hồi mẫu (JSON):
```json
{
  "error": "",
  "message": "",
  "request_id": "44aa882200ff9911",
  "response": {
    "penalty_points": 0,
    "penalty_tier": 0,
    "punishment_list": []
  }
}
```

