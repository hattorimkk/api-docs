# Tham Khảo API: Chăm Sóc Khách Hàng & Chat (Seller Chat APIs)

Tài liệu này cung cấp chi tiết đặc tả kỹ thuật và câu lệnh **cURL** cho phân hệ **Seller Chat** của Shopee Open API v2.

---

## 1. Lấy Danh Sách Cuộc Hội Thoại (Get Conversation List)

- **Tên Endpoint**: `v2.sellerchat.get_conversation_list`
- **Đường dẫn**: `GET /api/v2/sellerchat/get_conversation_list`
- **Loại API**: Shop API

### Lệnh cURL mẫu:
```bash
curl -X GET "https://partner.shopeemobile.com/api/v2/sellerchat/get_conversation_list?partner_id=123456&timestamp=1700000000&access_token=c71a39d892ef65a43b1234567890abcd&shop_id=98765432&sign=calculated_sign_here&type=all&direction=latest&page_size=20" \
  -H "Content-Type: application/json"
```

### Phản hồi mẫu (JSON):
```json
{
  "error": "",
  "message": "",
  "request_id": "...",
  "response": {
    "conversations": [
      {
        "conversation_id": "conv_98765432_12345678",
        "to_id": 12345678,
        "to_name": "nguyenvana_buyer",
        "unread_count": 2,
        "pinned": false,
        "last_message_timestamp": 1700019200000000000,
        "last_message_content": {
          "text": "Shop ơi cho mình hỏi áo này size L còn màu đen không ạ?"
        }
      }
    ],
    "page_result": {
      "page_size": 20,
      "next_timestamp_nano": 1700018500000000000,
      "more": true
    }
  }
}
```

---

## 2. Lấy Lịch Sử Tin Nhắn Chi Tiết (Get Message)

- **Tên Endpoint**: `v2.sellerchat.get_message`
- **Đường dẫn**: `GET /api/v2/sellerchat/get_message`
- **Loại API**: Shop API

### Lệnh cURL mẫu:
```bash
curl -X GET "https://partner.shopeemobile.com/api/v2/sellerchat/get_message?partner_id=123456&timestamp=1700000000&access_token=c71a39d892ef65a43b1234567890abcd&shop_id=98765432&sign=calculated_sign_here&conversation_id=conv_98765432_12345678&direction=older&page_size=50" \
  -H "Content-Type: application/json"
```

---

## 3. Gửi Tin Nhắn Cho Người Mua (Send Message)

- **Tên Endpoint**: `v2.sellerchat.send_message`
- **Đường dẫn**: `POST /api/v2/sellerchat/send_message`
- **Loại API**: Shop API

### Lệnh cURL mẫu:
```bash
curl -X POST "https://partner.shopeemobile.com/api/v2/sellerchat/send_message?partner_id=123456&timestamp=1700000000&access_token=c71a39d892ef65a43b1234567890abcd&shop_id=98765432&sign=calculated_sign_here" \
  -H "Content-Type: application/json" \
  -d '{
    "to_id": 12345678,
    "message_type": "text",
    "content": {
      "text": "Chào bạn, áo thun này là vải 100% Cotton co giãn 4 chiều cực kỳ thoáng mát ạ!"
    }
  }'
```

---

## 4. Đánh Dấu Đã Đọc Tin Nhắn (Read Conversation)

- **Tên Endpoint**: `v2.sellerchat.read_conversation`
- **Đường dẫn**: `POST /api/v2/sellerchat/read_conversation`
- **Loại API**: Shop API

### Lệnh cURL mẫu:
```bash
curl -X POST "https://partner.shopeemobile.com/api/v2/sellerchat/read_conversation?partner_id=123456&timestamp=1700000000&access_token=c71a39d892ef65a43b1234567890abcd&shop_id=98765432&sign=calculated_sign_here" \
  -H "Content-Type: application/json" \
  -d '{
    "conversation_id": "conv_98765432_12345678",
    "last_read_message_id": "msg_9900112233"
  }'
```
