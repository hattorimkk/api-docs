# Tham Khảo API: Cấu Hình Webhook Tự Động (Push Config APIs)

Tài liệu này cung cấp chi tiết đặc tả kỹ thuật và câu lệnh **cURL** cho các API quản lý và lập trình cấu hình Webhook (Push Mechanism) trên Shopee Open Platform.

---

## 1. Xem Cấu Hình Webhook Hiện Tại (Get App Push Config)

- **Tên Endpoint**: `v2.push.get_app_push_config`
- **Đường dẫn**: `GET /api/v2/push/get_app_push_config`
- **Loại API**: Public API

### Lệnh cURL mẫu:
```bash
curl -X GET "https://partner.shopeemobile.com/api/v2/push/get_app_push_config?partner_id=123456&timestamp=1700000000&sign=calculated_sign_here" \
  -H "Content-Type: application/json"
```

### Phản hồi mẫu (JSON):
```json
{
  "error": "",
  "message": "",
  "request_id": "...",
  "response": {
    "callback_url": "https://api.yourbrand.vn/webhook/shopee",
    "status": 1,
    "push_service": [
      { "code": 1, "name": "shop_authorization_push", "status": 1 },
      { "code": 2, "name": "shop_deauthorization_push", "status": 1 },
      { "code": 3, "name": "order_status_push", "status": 1 },
      { "code": 4, "name": "tracking_no_push", "status": 1 },
      { "code": 6, "name": "banned_item_push", "status": 1 },
      { "code": 8, "name": "reserved_stock_change_push", "status": 1 },
      { "code": 10, "name": "open_api_authorization_expiry_push", "status": 1 },
      { "code": 15, "name": "return_updates_push", "status": 1 }
    ]
  }
}
```

---

## 2. Cập Nhật Cấu Hình Webhook (Set App Push Config)

- **Tên Endpoint**: `v2.push.set_app_push_config`
- **Đường dẫn**: `POST /api/v2/push/set_app_push_config`
- **Loại API**: Public API

### Lệnh cURL mẫu:
```bash
curl -X POST "https://partner.shopeemobile.com/api/v2/push/set_app_push_config?partner_id=123456&timestamp=1700000000&sign=calculated_sign_here" \
  -H "Content-Type: application/json" \
  -d '{
    "callback_url": "https://api.yourbrand.vn/webhook/shopee",
    "push_service": [
      { "code": 1, "status": 1 },
      { "code": 2, "status": 1 },
      { "code": 3, "status": 1 },
      { "code": 4, "status": 1 },
      { "code": 6, "status": 1 },
      { "code": 8, "status": 1 },
      { "code": 10, "status": 1 },
      { "code": 15, "status": 1 }
    ]
  }'
```
