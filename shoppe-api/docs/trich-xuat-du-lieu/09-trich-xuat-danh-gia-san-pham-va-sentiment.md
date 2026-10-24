# 09. Hướng Dẫn Trích Xuất Đánh Giá Sản Phẩm & Phân Tích Cảm Xúc (Reviews & Sentiment)

Tài liệu này hướng dẫn kỹ thuật quét toàn bộ đánh giá 1-5 sao của khách hàng từ Shopee Open API v2, bóc tách nội dung phàn nàn và tích hợp vào hệ thống phân tích dữ liệu phục vụ cải tiến chất lượng sản phẩm.

---

## 1. Mục Đích & Giá Trị Nghiệp Vụ

1. **Phát hiện lỗi sản phẩm theo thời gian thực**: Tự động lọc các đánh giá 1 sao hoặc 2 sao để cảnh báo ngay cho bộ phận Quản lý chất lượng (QC) và Đóng gói.
2. **Phân tích cảm xúc người mua (Sentiment Analysis)**: Dùng mô hình NLP/LLM để phân loại bình luận theo các chủ đề: Vải/Độ bền, Size chật/rộng, Đóng gói móp méo, Thái độ shipper.
3. **Chăm sóc khách hàng tự động**: Tự động phản hồi cảm ơn khách 5 sao bằng `v2.product.reply_comment`, và tạo ticket cho nhân viên CSKH liên hệ xử lý bồi thường đối với khách hàng đánh giá tiêu cực.

---

## 2. Chiến Lược Thu Thập Toàn Bộ Đánh Giá Của Gian Hàng

Endpoint `v2.product.get_comment` sử dụng con trỏ phân trang (`cursor` / `next_cursor`).

```
[Khởi tạo cursor = ""]
       │
       ▼
Gọi GET /api/v2/product/get_comment?page_size=100&cursor={cursor}
       │
       ├── Lưu danh sách item_comment_list vào Database
       │
       └── Kiểm tra response.more == true?
              ├── ĐÚNG: Gán cursor = response.next_cursor -> Lặp lại
              └── SAI: Hoàn tất trích xuất
```

### Lệnh cURL mẫu trích xuất đánh giá:
```bash
PARTNER_ID="123456"
PARTNER_KEY="your_partner_secret_key"
SHOP_ID="98765432"
ACCESS_TOKEN="your_access_token"
API_PATH="/api/v2/product/get_comment"
TIMESTAMP=$(date +%s)

BASE_STRING="${PARTNER_ID}${API_PATH}${TIMESTAMP}${ACCESS_TOKEN}${SHOP_ID}"
SIGN=$(printf "%s" "$BASE_STRING" | openssl dgst -sha256 -hmac "$PARTNER_KEY" | awk '{print $2}')

curl -X GET "https://partner.shopeemobile.com${API_PATH}?partner_id=${PARTNER_ID}&timestamp=${TIMESTAMP}&access_token=${ACCESS_TOKEN}&shop_id=${SHOP_ID}&sign=${SIGN}&page_size=100" \
  -H "Content-Type: application/json"
```

---

## 3. Cấu Trúc Dữ Liệu Bảng Đánh Giá Sản Phẩm Trong Kho Dữ Liệu (SQL Schema)

Bổ sung bảng `dim_product_reviews` vào Star Schema:

```sql
CREATE TABLE IF NOT EXISTS dim_product_reviews (
    comment_id BIGINT PRIMARY KEY,
    order_sn VARCHAR(64) NOT NULL,
    item_id BIGINT NOT NULL,
    model_id BIGINT,
    buyer_username VARCHAR(100),
    rating_star INT NOT NULL,
    comment_text TEXT,
    has_image BOOLEAN DEFAULT FALSE,
    has_video BOOLEAN DEFAULT FALSE,
    reply_text TEXT,
    created_at TIMESTAMP NOT NULL,
    sentiment_label VARCHAR(20) -- POSITIVE, NEUTRAL, NEGATIVE
);
```

