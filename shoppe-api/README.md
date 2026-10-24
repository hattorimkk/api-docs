# Bộ Tài Liệu Tiếng Việt: Shopee Open Platform API v2.0 (`shoppe api`)

Chào mừng bạn đến với bộ tài liệu tiếng Việt chi tiết và đầy đủ nhất dành cho **Shopee Open Platform (phiên bản Open API v2.0)**. 

Bộ tài liệu này được biên soạn bám sát tài liệu chính thức từ [Shopee Open Platform Developer Guide (Guide 4)](https://open.shopee.com/developer-guide/4) và toàn bộ các phân hệ API v2.0 của Shopee, với mục tiêu giúp các kỹ sư dữ liệu (Data Engineers), lập trình viên Backend và các nhà phát triển giải pháp thương mại điện tử nhanh chóng làm chủ hệ thống, tích hợp thành công và **trích xuất toàn bộ dữ liệu sạch: Đơn hàng, Chi tiết sản phẩm, Biến thể SKU, Tồn kho khả dụng, Doanh thu đối soát (Escrow), Trạng thái vận chuyển và Khiếu nại trả hàng**.

---

## 📌 Mục Lục Nhanh

1. [Cấu Trúc Bộ Tài Liệu](#-cấu-trúc-bộ-tài-liệu)
2. [Kiến Trúc & Khái Niệm Cốt Lõi](#-kiến-trúc--khái-niệm-cốt-lõi)
3. [Hướng Dẫn Nhanh: Trích Xuất Dữ Liệu Bằng cURL (Quickstart)](#-hướng-dẫn-nhanh-trích-xuất-dữ-liệu-bằng-curl-quickstart)
   - [Bước 1: Khai báo biến môi trường](#bước-1-khai-báo-biến-môi-trường)
   - [Bước 2: Tạo URL ủy quyền Shop](#bước-2-tạo-url-ủy-quyền-shop)
   - [Bước 3: Đổi mã Code lấy Access Token & Refresh Token](#bước-3-đổi-mã-code-lấy-access-token--refresh-token)
   - [Bước 4: Trích xuất thông tin Shop](#bước-4-trích-xuất-thông-tin-shop)
   - [Bước 5: Trích xuất danh sách và chi tiết đơn hàng](#bước-5-trích-xuất-danh-sách-và-chi-tiết-đơn-hàng)
   - [Bước 6: Trích xuất danh mục sản phẩm & tồn kho SKU](#bước-6-trích-xuất-danh-mục-sản-phẩm--tồn-kho-sku)
   - [Bước 7: Trích xuất đối soát tài chính & doanh thu thực nhận](#bước-7-trích-xuất-đối-soát-tài-chính--doanh-thu-thực-nhận)
   - [Bước 8: Trích xuất lịch sử Chat & Tin nhắn CSKH](#bước-8-trích-xuất-lịch-sử-chat--tin-nhắn-cskh)
4. [Các Quy Tắc Kỹ Thuật "Sống Còn" Cần Nhớ](#-các-quy-tắc-kỹ-thuật-sống-còn-cần-nhớ)
5. [Mục Lục Chi Tiết Toàn Bộ Phân Hệ Tài Liệu](#-mục-lục-chi-tiết-toàn-bộ-phân-hệ-tài-liệu)

---

## 📂 Cấu Trúc Bộ Tài Liệu

Bộ tài liệu được thiết kế bài bản theo cấu trúc thư mục module hóa:

```text
shoppe-api/
├── README.md                                  # (Tài liệu này) Tổng quan, Quickstart cURL & Mục lục chính
├── scripts/                                   # Bộ mã nguồn Python hoàn chỉnh, sẵn sàng chạy ngay
│   ├── shopee_client.py                       # Client SDK (Ký HMAC-SHA256, tự động refresh token, retry)
│   ├── sync_orders.py                         # Tool trích xuất toàn bộ đơn hàng chi tiết ra JSON/CSV
│   ├── sync_products.py                       # Tool trích xuất catalog, biến thể SKU và tồn kho
│   ├── sync_escrow.py                         # Tool đối soát tài chính, doanh thu thực nhận và phí sàn
│   ├── sync_chat.py                           # Tool trích xuất lịch sử hội thoại & tin nhắn CSKH
│   ├── sync_marketing.py                      # Tool trích xuất Voucher, Discount và Follow Prize
│   ├── export_to_sql.py                       # Tool nạp tự động vào Cơ sở dữ liệu SQLite/PostgreSQL
│   └── webhook_server.py                      # Server nhận sự kiện Shopee Push Webhook thời gian thực
└── docs/
    ├── tong-quan/                             # Khái niệm nền tảng, loại tài khoản, môi trường, rate limit
    │   ├── 01-gioi-thieu-va-kien-truc.md      # Kiến trúc 3 bên: Partner - Shop - Shopee Gateway
    │   ├── 02-dang-ky-va-loai-ung-dung.md     # Ứng dụng nội bộ vs Ứng dụng ISV, Partner ID & Key
    │   ├── 03-moi-truong-sandbox-va-live.md   # Thử nghiệm Sandbox vs Sản xuất Live, IP Whitelist
    │   ├── 04-chinh-sach-bao-ve-du-lieu-pii.md# Che mờ dữ liệu khách (Masked PII) & điều kiện mở quyền
    │   └── 05-gioi-han-tan-suat-rate-limit-va-ma-loi.md # Bảng mã lỗi & xử lý Rate limit (50 QPS)
    ├── xac-thuc-va-uy-quyen/                  # OAuth 2.0, Chữ ký số HMAC-SHA256 & Vòng đời Token
    │   ├── 01-thuat-toan-chu-ky-sign.md       # Công thức ký HMAC-SHA256 chuẩn cho mọi loại API
    │   ├── 02-quy-trinh-uy-quyen-shop.md      # Luồng OAuth lấy code, đổi access_token & refresh_token
    │   ├── 03-quan-ly-va-refresh-token.md     # Cơ chế xoay vòng Token Rotation (4 giờ / 30 ngày)
    │   └── 04-uy-quyen-merchant-cnsc.md       # Dành cho tài khoản tổng bán hàng xuyên biên giới (CNSC)
    ├── trich-xuat-du-lieu/                    # Hướng dẫn chuyên sâu các bài toán trích xuất dữ liệu
    │   ├── 01-dong-bo-don-hang-order.md       # Chiến lược 2 bước: get_order_list + get_order_detail
    │   ├── 02-dong-bo-san-pham-va-ton-kho.md  # Bóc tách item_id, tier variations, model_sku & stock
    │   ├── 03-doi-soat-tai-chinh-doanh-thu-escrow.md # Bóc tách doanh thu thực nhận và các loại phí sàn
    │   ├── 04-theo-doi-van-chuyen-logistics.md# Tracking hành trình vận đơn & in phiếu giao hàng AWB
    │   ├── 05-quan-ly-tra-hang-hoan-tien-returns.md # Quản lý khiếu nại, lý do và bằng chứng hoàn tiền
    │   ├── 06-trich-xuat-lich-su-chat-va-cskh.md    # Trích xuất hội thoại & đo lường chất lượng chat
    │   ├── 07-trich-xuat-chuong-trinh-marketing.md  # Đo lường hiệu quả Voucher & Flash Sale
    │   ├── 08-data-pipeline-database-warehouse.md   # Thiết kế Data Warehouse Star Schema & DDL SQL
    │   └── 09-trich-xuat-danh-gia-san-pham-va-sentiment.md # Bóc tách đánh giá 1-5 sao & phân tích cảm xúc
    ├── api-reference/                         # Đặc tả chi tiết từng Endpoint kèm cURL mẫu
    │   ├── 01-auth-va-public-apis.md          # Các API xác thực, sinh token và hủy quyền
    │   ├── 02-shop-apis.md                    # Lấy thông tin shop, hồ sơ và trạng thái ủy quyền
    │   ├── 03-order-apis.md                   # get_order_list, get_order_detail, handle_cancellation
    │   ├── 04-product-apis.md                 # get_item_list, get_item_base_info, get_model_list
    │   ├── 05-logistics-apis.md               # get_channel_list, ship_order, get_tracking_info, AWB
    │   ├── 06-payment-escrow-apis.md          # get_escrow_list, get_escrow_detail, get_wallet
    │   ├── 07-returns-apis.md                 # get_return_list, get_return_detail, confirm, dispute
    │   ├── 08-marketing-discount-apis.md      # get_discount_list, get_voucher_list, bundle deals
    │   ├── 09-media-space-apis.md             # upload_image, init_video_upload, upload chunk video
    │   ├── 10-customer-service-chat-apis.md   # get_conversation_list, get_message, send_message
    │   ├── 11-follow-prize-apis.md            # get_follow_prize_list, get_follow_prize_detail
    │   ├── 12-push-config-apis.md             # get_app_push_config, set_app_push_config
    │   ├── 13-global-product-cnsc-apis.md     # get_global_item_list, create_publish_task
    │   ├── 14-danh-gia-san-pham-reviews-comments.md # get_comment, reply_comment
    │   ├── 15-shop-category-va-flash-sale.md  # Shop Categories & In-shop Flash Sale
    │   ├── 16-kho-shopee-fulfillment-sbs.md   # Fulfillment by Shopee (FBS) & Kho SBS
    │   ├── 17-suc-khoe-tai-khoan-account-health.md # Tỷ lệ hủy, giao trễ, điểm phạt sao quả tạ
    │   ├── 18-shopee-ads-va-affiliate-marketing.md # Shopee Ads & Tiếp thị liên kết AMS
    │   └── 19-livestream-va-shopee-video.md   # Phiên live Shopee Live & Video ngắn Shopee Video
    └── webhook-push-mechanism/                # Tự động hóa cập nhật dữ liệu Realtime qua Webhook
        ├── 01-co-che-push-mechanism.md        # Tại sao phải dùng Webhook thay vì Polling liên tục
        ├── 02-danh-sach-su-kien-push-codes.md # Tra cứu Code 1, 2, 3 (Đơn hàng), 4 (Vận đơn), 6, 8...
        └── 03-xac-thuc-chu-ky-va-xu-ly-webhook.md # Xác thực header Authorization & chống trùng event
```

---

## 🏛️ Kiến Trúc & Khái Niệm Cốt Lõi

1. **Hệ thống xác thực Chữ ký số (HMAC-SHA256)**:
   Mọi request gửi tới Shopee API đều phải có chữ ký `sign` được mã hóa từ chuỗi cơ sở (`base_string`) sử dụng `partner_key`:
   - **Public API**: `partner_id + api_path + timestamp`
   - **Shop API**: `partner_id + api_path + timestamp + access_token + shop_id`
   - **Merchant API**: `partner_id + api_path + timestamp + access_token + merchant_id`

2. **Cơ chế Token Rotation**:
   - `access_token` có hiệu lực trong **4 giờ (14.400s)**.
   - `refresh_token` có hiệu lực trong **30 ngày**.
   - Mỗi lần refresh token, Shopee cấp lại **CẢ `access_token` MỚI VÀ `refresh_token` MỚI**. Bạn phải cập nhật cả hai vào Database để không bị mất quyền truy cập.

3. **Môi trường Gateway**:
   - **Sản xuất (Live)**: `https://partner.shopeemobile.com`
   - **Kiểm thử (Sandbox)**: `https://partner.test-stable.shopeemobile.com`

---

## 🚀 Hướng Dẫn Nhanh: Trích Xuất Dữ Liệu Bằng cURL (Quickstart)

Dưới đây là quy trình thực thi hoàn chỉnh bằng lệnh **cURL** trực tiếp trên Terminal để bạn có thể kiểm thử và lấy dữ liệu ngay lập tức.

### Bước 1: Khai báo biến môi trường
Mở Terminal và gán các thông tin định danh:
```bash
PARTNER_ID="123456"
PARTNER_KEY="your_partner_secret_key"
SHOP_ID="98765432"
BASE_URL="https://partner.shopeemobile.com"
```

### Bước 2: Tạo URL ủy quyền Shop
Tạo đường link để chủ Shop đăng nhập cấp quyền:
```bash
API_PATH="/api/v2/shop/auth_partner"
TIMESTAMP=$(date +%s)
REDIRECT_URL="https://your-domain.com/callback"

# Tính sign HMAC-SHA256
BASE_STRING="${PARTNER_ID}${API_PATH}${TIMESTAMP}"
SIGN=$(printf "%s" "$BASE_STRING" | openssl dgst -sha256 -hmac "$PARTNER_KEY" | awk '{print $2}')
REDIRECT_ENCODED=$(python3 -c "import urllib.parse; print(urllib.parse.quote('$REDIRECT_URL', safe=''))")

AUTH_URL="${BASE_URL}${API_PATH}?partner_id=${PARTNER_ID}&timestamp=${TIMESTAMP}&sign=${SIGN}&redirect=${REDIRECT_ENCODED}"
echo "Mở link sau trên trình duyệt để ủy quyền:"
echo "$AUTH_URL"
```

### Bước 3: Đổi mã Code lấy Access Token & Refresh Token
Sau khi chủ Shop đồng ý, Shopee chuyển hướng về Callback URL kèm `?code=...`. Chạy lệnh cURL sau để nhận Token:
```bash
CODE="auth_code_nhan_duoc_tu_callback"
API_PATH="/api/v2/auth/token/get"
TIMESTAMP=$(date +%s)
BASE_STRING="${PARTNER_ID}${API_PATH}${TIMESTAMP}"
SIGN=$(printf "%s" "$BASE_STRING" | openssl dgst -sha256 -hmac "$PARTNER_KEY" | awk '{print $2}')

curl -X POST "${BASE_URL}${API_PATH}?partner_id=${PARTNER_ID}&timestamp=${TIMESTAMP}&sign=${SIGN}" \
  -H "Content-Type: application/json" \
  -d "{
    \"code\": \"${CODE}\",
    \"partner_id\": ${PARTNER_ID},
    \"shop_id\": ${SHOP_ID}
  }"
```
*Gán biến `ACCESS_TOKEN` từ kết quả JSON trả về để thực hiện các bước tiếp theo.*

### Bước 4: Trích xuất thông tin Shop
```bash
ACCESS_TOKEN="your_access_token"
API_PATH="/api/v2/shop/get_shop_info"
TIMESTAMP=$(date +%s)
BASE_STRING="${PARTNER_ID}${API_PATH}${TIMESTAMP}${ACCESS_TOKEN}${SHOP_ID}"
SIGN=$(printf "%s" "$BASE_STRING" | openssl dgst -sha256 -hmac "$PARTNER_KEY" | awk '{print $2}')

curl -X GET "${BASE_URL}${API_PATH}?partner_id=${PARTNER_ID}&timestamp=${TIMESTAMP}&access_token=${ACCESS_TOKEN}&shop_id=${SHOP_ID}&sign=${SIGN}" \
  -H "Content-Type: application/json"
```

### Bước 5: Trích xuất danh sách và chi tiết đơn hàng
#### 5.1. Quét danh sách mã đơn (`get_order_list`):
```bash
API_PATH="/api/v2/order/get_order_list"
TIMESTAMP=$(date +%s)
TIME_FROM=$((TIMESTAMP - 14 * 86400)) # 14 ngày trước
BASE_STRING="${PARTNER_ID}${API_PATH}${TIMESTAMP}${ACCESS_TOKEN}${SHOP_ID}"
SIGN=$(printf "%s" "$BASE_STRING" | openssl dgst -sha256 -hmac "$PARTNER_KEY" | awk '{print $2}')

curl -X GET "${BASE_URL}${API_PATH}?partner_id=${PARTNER_ID}&timestamp=${TIMESTAMP}&access_token=${ACCESS_TOKEN}&shop_id=${SHOP_ID}&sign=${SIGN}&time_range_field=create_time&time_from=${TIME_FROM}&time_to=${TIMESTAMP}&page_size=50" \
  -H "Content-Type: application/json"
```

#### 5.2. Lấy chi tiết đơn hàng (`get_order_detail`):
```bash
ORDER_SN="261023ABCD1234"
API_PATH="/api/v2/order/get_order_detail"
TIMESTAMP=$(date +%s)
BASE_STRING="${PARTNER_ID}${API_PATH}${TIMESTAMP}${ACCESS_TOKEN}${SHOP_ID}"
SIGN=$(printf "%s" "$BASE_STRING" | openssl dgst -sha256 -hmac "$PARTNER_KEY" | awk '{print $2}')

curl -X GET "${BASE_URL}${API_PATH}?partner_id=${PARTNER_ID}&timestamp=${TIMESTAMP}&access_token=${ACCESS_TOKEN}&shop_id=${SHOP_ID}&sign=${SIGN}&order_sn_list=${ORDER_SN}&response_optional_fields=buyer_user_id,recipient_address,item_list,payment_method,actual_shipping_fee,note" \
  -H "Content-Type: application/json"
```

### Bước 6: Trích xuất danh mục sản phẩm & tồn kho SKU
```bash
API_PATH="/api/v2/product/get_item_list"
TIMESTAMP=$(date +%s)
BASE_STRING="${PARTNER_ID}${API_PATH}${TIMESTAMP}${ACCESS_TOKEN}${SHOP_ID}"
SIGN=$(printf "%s" "$BASE_STRING" | openssl dgst -sha256 -hmac "$PARTNER_KEY" | awk '{print $2}')

curl -X GET "${BASE_URL}${API_PATH}?partner_id=${PARTNER_ID}&timestamp=${TIMESTAMP}&access_token=${ACCESS_TOKEN}&shop_id=${SHOP_ID}&sign=${SIGN}&offset=0&page_size=50&item_status=NORMAL" \
  -H "Content-Type: application/json"
```

### Bước 7: Trích xuất đối soát tài chính & doanh thu thực nhận
```bash
API_PATH="/api/v2/payment/get_escrow_detail"
TIMESTAMP=$(date +%s)
BASE_STRING="${PARTNER_ID}${API_PATH}${TIMESTAMP}${ACCESS_TOKEN}${SHOP_ID}"
SIGN=$(printf "%s" "$BASE_STRING" | openssl dgst -sha256 -hmac "$PARTNER_KEY" | awk '{print $2}')

curl -X GET "${BASE_URL}${API_PATH}?partner_id=${PARTNER_ID}&timestamp=${TIMESTAMP}&access_token=${ACCESS_TOKEN}&shop_id=${SHOP_ID}&sign=${SIGN}&order_sn=${ORDER_SN}" \
  -H "Content-Type: application/json"
```

### Bước 8: Trích xuất lịch sử Chat & Tin nhắn CSKH
#### 8.1. Lấy danh sách cuộc hội thoại khách hàng (`get_conversation_list`):
```bash
API_PATH="/api/v2/sellerchat/get_conversation_list"
TIMESTAMP=$(date +%s)
BASE_STRING="${PARTNER_ID}${API_PATH}${TIMESTAMP}${ACCESS_TOKEN}${SHOP_ID}"
SIGN=$(printf "%s" "$BASE_STRING" | openssl dgst -sha256 -hmac "$PARTNER_KEY" | awk '{print $2}')

curl -X GET "${BASE_URL}${API_PATH}?partner_id=${PARTNER_ID}&timestamp=${TIMESTAMP}&access_token=${ACCESS_TOKEN}&shop_id=${SHOP_ID}&sign=${SIGN}&type=all&direction=latest&page_size=20" \
  -H "Content-Type: application/json"
```

#### 8.2. Lấy nội dung chi tiết tin nhắn chat (`get_message`):
```bash
CONVERSATION_ID="conv_98765432_12345678"
API_PATH="/api/v2/sellerchat/get_message"
TIMESTAMP=$(date +%s)
BASE_STRING="${PARTNER_ID}${API_PATH}${TIMESTAMP}${ACCESS_TOKEN}${SHOP_ID}"
SIGN=$(printf "%s" "$BASE_STRING" | openssl dgst -sha256 -hmac "$PARTNER_KEY" | awk '{print $2}')

curl -X GET "${BASE_URL}${API_PATH}?partner_id=${PARTNER_ID}&timestamp=${TIMESTAMP}&access_token=${ACCESS_TOKEN}&shop_id=${SHOP_ID}&sign=${SIGN}&conversation_id=${CONVERSATION_ID}&direction=older&page_size=50" \
  -H "Content-Type: application/json"
```

---

## 🛠️ Bộ Công Cụ Tự Động Hóa (Tùy Chọn Trong Thư Mục `scripts/`)

Nếu muốn tự động hóa toàn diện bằng mã nguồn Python (ETL dữ liệu hàng loạt vào Cơ sở dữ liệu), bạn có thể chạy trực tiếp:
- [`scripts/sync_orders.py`](scripts/sync_orders.py): Tự động quét toàn bộ đơn hàng phân trang theo con trỏ và lưu ra JSON/CSV.
- [`scripts/sync_products.py`](scripts/sync_products.py): Tự động tải danh mục sản phẩm, biến thể và tồn kho khả dụng.
- [`scripts/sync_escrow.py`](scripts/sync_escrow.py): Tự động đối soát doanh thu thực nhận và các loại phí sàn.
- [`scripts/sync_chat.py`](scripts/sync_chat.py): Tự động trích xuất lịch sử tin nhắn CSKH.
- [`scripts/sync_marketing.py`](scripts/sync_marketing.py): Tự động trích xuất Voucher và chương trình giảm giá.
- [`scripts/export_to_sql.py`](scripts/export_to_sql.py): Tự động nạp dữ liệu sạch vào Database SQLite / PostgreSQL theo chuẩn Star Schema.
- [`scripts/webhook_server.py`](scripts/webhook_server.py): Server tiếp nhận thông báo Webhook thời gian thực.

---

## ⚠️ Các Quy Tắc Kỹ Thuật "Sống Còn" Cần Nhớ

> [!IMPORTANT]
> 1. **Tham số bảo mật luôn nằm trên URL Query**: Ngay cả đối với các request `POST`, các tham số `partner_id`, `timestamp`, `access_token`, `shop_id`, `sign` **bắt buộc phải truyền trên URL Query String**. Request Body JSON chỉ chứa các tham số nghiệp vụ.
> 2. **Độ lệch thời gian không quá 5 phút**: Máy chủ của bạn phải đồng bộ giờ qua NTP. Nếu thời gian trên máy chủ lệch quá 300 giây so với máy chủ Shopee, tất cả các request sẽ bị từ chối với lỗi `Wrong sign`.
> 3. **Giới hạn thời gian 15 ngày trên API Đơn Hàng**: Endpoint `get_order_list` chỉ cho phép khoảng cách giữa `time_from` và `time_to` tối đa là 15 ngày. Muốn quét dữ liệu lịch sử nhiều tháng, bạn phải chia nhỏ thành các khung 14 ngày (đã được tự động xử lý trong `sync_orders.py`).
> 4. **Bảo tồn Raw Request Body khi nhận Webhook**: Khi xác thực chữ ký Webhook ở header `Authorization`, tuyệt đối không dùng body đã bị format lại bởi parser JSON. Phải sử dụng trực tiếp chuỗi byte nguyên bản của request.

---

## 📚 Mục Lục Chi Tiết Toàn Bộ Phân Hệ Tài Liệu

### 1. Tổng Quan & Nền Tảng
- [01. Giới thiệu & Kiến trúc nền tảng](docs/tong-quan/01-gioi-thieu-va-kien-truc.md)
- [02. Đăng ký tài khoản & Phân loại ứng dụng (Nội bộ vs ISV)](docs/tong-quan/02-dang-ky-va-loai-ung-dung.md)
- [03. Môi trường Sandbox (Thử nghiệm) & Môi trường Live](docs/tong-quan/03-moi-truong-sandbox-va-live.md)
- [04. Chính sách bảo vệ dữ liệu PII & Cơ chế che mờ thông tin](docs/tong-quan/04-chinh-sach-bao-ve-du-lieu-pii.md)
- [05. Giới hạn tần suất (Rate Limit 50 QPS) & Bảng tra cứu mã lỗi](docs/tong-quan/05-gioi-han-tan-suat-rate-limit-va-ma-loi.md)

### 2. Xác Thực, Chữ Ký & Vòng Đời Token
- [01. Thuật toán tạo chữ ký số HMAC-SHA256 (Sign)](docs/xac-thuc-va-uy-quyen/01-thuat-toan-chu-ky-sign.md)
- [02. Quy trình ủy quyền gian hàng (Shop Authorization Flow)](docs/xac-thuc-va-uy-quyen/02-quy-trinh-uy-quyen-shop.md)
- [03. Quản lý vòng đời & Tự động làm mới Token (Token Rotation)](docs/xac-thuc-va-uy-quyen/03-quan-ly-va-refresh-token.md)
- [04. Quy trình ủy quyền tài khoản tổng Merchant (CNSC - Bán hàng xuyên biên giới)](docs/xac-thuc-va-uy-quyen/04-uy-quyen-merchant-cnsc.md)

### 3. Hướng Dẫn Trích Xuất Dữ Liệu Chuyên Sâu
- [01. Hướng dẫn trích xuất & đồng bộ đơn hàng (Order Data Extraction)](docs/trich-xuat-du-lieu/01-dong-bo-don-hang-order.md)
- [02. Hướng dẫn trích xuất sản phẩm, biến thể & tồn kho (Product & Stock)](docs/trich-xuat-du-lieu/02-dong-bo-san-pham-va-ton-kho.md)
- [03. Hướng dẫn đối soát tài chính, doanh thu & phí sàn (Escrow & Accounting)](docs/trich-xuat-du-lieu/03-doi-soat-tai-chinh-doanh-thu-escrow.md)
- [04. Hướng dẫn theo dõi vận chuyển & in phiếu giao hàng (Logistics & AWB)](docs/trich-xuat-du-lieu/04-theo-doi-van-chuyen-logistics.md)
- [05. Hướng dẫn quản lý trả hàng & hoàn tiền (Returns & Refunds)](docs/trich-xuat-du-lieu/05-quan-ly-tra-hang-hoan-tien-returns.md)
- [06. Hướng dẫn trích xuất lịch sử chat & chất lượng dịch vụ CSKH](docs/trich-xuat-du-lieu/06-trich-xuat-lich-su-chat-va-cskh.md)
- [07. Hướng dẫn trích xuất & đo lường hiệu quả khuyến mãi Marketing](docs/trich-xuat-du-lieu/07-trich-xuat-chuong-trinh-marketing.md)
- [08. Thiết kế Data Pipeline & Kho dữ liệu Data Warehouse Star Schema](docs/trich-xuat-du-lieu/08-data-pipeline-database-warehouse.md)
- [09. Hướng dẫn trích xuất đánh giá sản phẩm & phân tích cảm xúc khách hàng](docs/trich-xuat-du-lieu/09-trich-xuat-danh-gia-san-pham-va-sentiment.md)

### 4. Tài Liệu Tham Khảo Chi Tiết Từng Endpoint (API Reference)
- [01. Phân hệ Xác thực & Public APIs](docs/api-reference/01-auth-va-public-apis.md)
- [02. Phân hệ Thông tin & Hồ sơ Shop](docs/api-reference/02-shop-apis.md)
- [03. Phân hệ Quản lý Đơn hàng (Order APIs)](docs/api-reference/03-order-apis.md)
- [04. Phân hệ Quản lý Sản phẩm (Product & Item APIs)](docs/api-reference/04-product-apis.md)
- [05. Phân hệ Hậu cần & Vận chuyển (Logistics APIs)](docs/api-reference/05-logistics-apis.md)
- [06. Phân hệ Tài chính & Quyết toán (Payment & Escrow APIs)](docs/api-reference/06-payment-escrow-apis.md)
- [07. Phân hệ Khiếu nại Trả hàng (Returns APIs)](docs/api-reference/07-returns-apis.md)
- [08. Phân hệ Khuyến mãi & Voucher (Marketing APIs)](docs/api-reference/08-marketing-discount-apis.md)
- [09. Phân hệ Media Space - Upload Ảnh & Video Mảnh](docs/api-reference/09-media-space-apis.md)
- [10. Phân hệ Chăm sóc khách hàng & Chat (Seller Chat APIs)](docs/api-reference/10-customer-service-chat-apis.md)
- [11. Phân hệ Ưu đãi người theo dõi (Follow Prize APIs)](docs/api-reference/11-follow-prize-apis.md)
- [12. Phân hệ Cấu hình Webhook qua API (Push Config APIs)](docs/api-reference/12-push-config-apis.md)
- [13. Phân hệ Sản phẩm toàn cầu Merchant CNSC (Global Product APIs)](docs/api-reference/13-global-product-cnsc-apis.md)
- [14. Phân hệ Đánh giá sản phẩm & Phản hồi bình luận (Reviews & Comments)](docs/api-reference/14-danh-gia-san-pham-reviews-comments.md)
- [15. Phân hệ Danh mục shop & Flash Sale gian hàng (Shop Category & Flash Sale)](docs/api-reference/15-shop-category-va-flash-sale.md)
- [16. Phân hệ Kho hàng Shopee & Hoàn tất đơn hàng (Fulfillment FBS / SBS)](docs/api-reference/16-kho-shopee-fulfillment-sbs.md)
- [17. Phân hệ Sức khỏe tài khoản & Chỉ số vận hành (Account Health)](docs/api-reference/17-suc-khoe-tai-khoan-account-health.md)
- [18. Phân hệ Quảng cáo Shopee & Tiếp thị liên kết (Shopee Ads & AMS)](docs/api-reference/18-shopee-ads-va-affiliate-marketing.md)
- [19. Phân hệ Livestream & Video ngắn (Shopee Live & Video)](docs/api-reference/19-livestream-va-shopee-video.md)

### 5. Cơ Chế Nhận Dữ Liệu Thời Gian Thực (Push Mechanism / Webhooks)
- [01. Tổng quan cơ chế Push Mechanism & Cấu hình Callback URL](docs/webhook-push-mechanism/01-co-che-push-mechanism.md)
- [02. Bảng tra cứu các mã sự kiện Push Codes (Code 1, 2, 3, 4, 6, 8, 10, 15...)](docs/webhook-push-mechanism/02-danh-sach-su-kien-push-codes.md)
- [03. Xác thực chữ ký Authorization Header & Xử lý Idempotency](docs/webhook-push-mechanism/03-xac-thuc-chu-ky-va-xu-ly-webhook.md)
