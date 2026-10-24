# Tham Khảo API: Đánh Giá Sản Phẩm & Phản Hồi Khách Hàng (Reviews & Comments)

Tài liệu này cung cấp chi tiết đặc tả kỹ thuật và câu lệnh **cURL** cho các API thuộc phân hệ Đánh giá sản phẩm (`v2.product.get_comment`, `v2.product.reply_comment`) trong Shopee Open API v2.

---

## 1. Lấy Danh Sách Đánh Giá & Bình Luận Sản Phẩm (Get Comment)

Endpoint này dùng để trích xuất toàn bộ đánh giá của người mua (số sao 1-5 sao, bình luận chi tiết, hình ảnh, video đính kèm) theo gian hàng hoặc từng sản phẩm cụ thể.

- **Tên Endpoint**: `v2.product.get_comment`
- **Đường dẫn**: `GET /api/v2/product/get_comment`
- **Loại API**: Shop API

### Tham số Query String:
| Tham số | Kiểu dữ liệu | Bắt buộc | Mô tả |
| :--- | :--- | :--- | :--- |
| `partner_id` | int | Có | ID đối tác ứng dụng |
| `timestamp` | int | Có | Unix timestamp hiện tại |
| `access_token` | string | Có | Shop Access Token còn hiệu lực |
| `shop_id` | int | Có | ID Shop trên Shopee |
| `sign` | string | Có | Chữ ký HMAC-SHA256 |
| `item_id` | int | Không | Lọc theo ID sản phẩm cụ thể. Bỏ trống để lấy toàn bộ đánh giá của shop |
| `comment_id` | int | Không | Lọc theo ID bình luận cụ thể |
| `cursor` | string | Không | Con trỏ phân trang (lấy từ `next_cursor` của lần gọi trước) |
| `page_size` | int | Có | Số lượng đánh giá mỗi trang (tối đa 100) |

### Lệnh cURL mẫu:
```bash
curl -X GET "https://partner.shopeemobile.com/api/v2/product/get_comment?partner_id=123456&timestamp=1700000000&access_token=c71a39d892ef65a43b1234567890abcd&shop_id=98765432&sign=calculated_sign_here&page_size=50" \
  -H "Content-Type: application/json"
```

### Phản hồi mẫu (JSON):
```json
{
  "error": "",
  "message": "",
  "request_id": "84a7e93fbc21019d",
  "response": {
    "item_comment_list": [
      {
        "comment_id": 99887766,
        "comment": "Chất vải thun cotton dày dặn, mặc mát và thấm hút mồ hôi tốt. Giao hàng rất nhanh, đóng gói cẩn thận 5 sao!",
        "buyer_username": "nguyenvana_buyer",
        "order_sn": "261023ABCD1234",
        "item_id": 1122334455,
        "model_id": 55667788,
        "rating_star": 5,
        "editable": "UNEDITABLE",
        "create_time": 1700018500,
        "status": "NORMAL",
        "comment_image_list": [
          "https://cf.shopee.vn/file/vn-11134207-7r98o-comment1.jpg"
        ],
        "comment_video_list": [],
        "reply": {
          "comment": "Cảm ơn bạn đã tin tưởng và ủng hộ gian hàng! Chúc bạn có trải nghiệm tuyệt vời với sản phẩm ạ.",
          "create_time": 1700021000
        }
      }
    ],
    "more": true,
    "next_cursor": "eyJvZmZzZXQiOjUwfQ=="
  }
}
```

---

## 2. Phản Hồi Bình Luận Của Khách Hàng (Reply Comment)

Endpoint này cho phép người bán hoặc hệ thống CSKH tự động gửi phản hồi lời cảm ơn hoặc giải đáp thắc mắc đối với đánh giá của người mua.

- **Tên Endpoint**: `v2.product.reply_comment`
- **Đường dẫn**: `POST /api/v2/product/reply_comment`
- **Loại API**: Shop API

### Tham số Request Body (JSON):
| Tham số | Kiểu dữ liệu | Bắt buộc | Mô tả |
| :--- | :--- | :--- | :--- |
| `reply_list` | array | Có | Danh sách các bình luận cần phản hồi |
| `reply_list[].comment_id` | int | Có | ID của bình luận cần phản hồi |
| `reply_list[].comment` | string | Có | Nội dung phản hồi từ Shop |

### Lệnh cURL mẫu:
```bash
curl -X POST "https://partner.shopeemobile.com/api/v2/product/reply_comment?partner_id=123456&timestamp=1700000000&access_token=c71a39d892ef65a43b1234567890abcd&shop_id=98765432&sign=calculated_sign_here" \
  -H "Content-Type: application/json" \
  -d '{
    "reply_list": [
      {
        "comment_id": 99887766,
        "comment": "Dạ Shop xin cảm ơn bạn rất nhiều! Rất hy vọng được tiếp tục phục vụ bạn trong những đơn hàng tiếp theo ạ ❤️"
      }
    ]
  }'
```

### Phản hồi mẫu (JSON):
```json
{
  "error": "",
  "message": "",
  "request_id": "55bb39dfaa11029e",
  "response": {
    "result_list": [
      {
        "comment_id": 99887766,
        "fail_error": "",
        "fail_message": ""
      }
    ]
  }
}
```

