# Use case: đăng ký Webhook

Tài liệu này cung cấp hướng dẫn toàn diện về việc đăng ký và quản lý các sự kiện Webhook trong hệ sinh thái TikTok for Business. Bạn sẽ tìm hiểu cách nhận thông báo thời gian thực khi xuất bản video, cập nhật bình luận, lượt nhắc đến thương hiệu (mentions), các sự kiện nhắn tin doanh nghiệp (Business Messaging), cũng như các thay đổi về số liệu báo cáo, khách hàng tiềm năng, trạng thái xét duyệt và bão hòa quảng cáo, trạng thái đình chỉ tài khoản và tình trạng vận hành của dịch vụ API.

## Đăng ký Webhook (`Webhook subscription`)
<a id="doc-1810521709205505"></a>
<!-- doc_id: 1810521709205505 -->

> Đường dẫn: Use Cases > Webhook subscription

Chương này bao gồm các tình huống sử dụng sau:
- [Đăng ký sự kiện Webhook của tài khoản TikTok qua Webhooks API](use-case-webhook.md#doc-1810521730276354)
- [Đăng ký lượt nhắc đến qua Webhooks API](use-case-webhook.md#doc-1825113658431489)
- [Đăng ký sự kiện Business Messaging Webhook qua Webhooks API](use-case-webhook.md#doc-1832190670631937)
- [Đăng ký sự kiện Webhook của tài khoản quảng cáo qua Subscription API](use-case-webhook.md#doc-1810521739537409)

## Đăng ký sự kiện Webhook của tài khoản TikTok qua Webhooks API (`Subscribe to TikTok account Webhook events via Webhooks API`)
<a id="doc-1810521730276354"></a>
<!-- doc_id: 1810521730276354 -->

> Đường dẫn: Use Cases > Webhook subscription > Subscribe to TikTok account Webhook events via Webhooks API

Bài viết này hướng dẫn bạn từng bước nhận thông báo về trạng thái xuất bản bài đăng và các cập nhật bình luận trên tài khoản TikTok thông qua Webhook.

### Giới thiệu (Introduction)

Webhook là các lệnh gọi lại HTTP tự động được kích hoạt khi các sự kiện cụ thể diễn ra trong nền tảng TikTok, cho phép gửi thông báo theo thời gian thực đến URL gọi lại (callback URL) mà bạn chỉ định. Cơ chế này loại bỏ nhu cầu phải liên tục gọi API thăm dò (polling) để lấy thông tin về các sự kiện bất đồng bộ. Thay vào đó, TikTok chủ động gửi dữ liệu sự kiện đến hệ thống của bạn ngay khi sẵn sàng. Các thông báo này được gửi qua HTTPS POST dưới định dạng JSON tới URL gọi lại đã định cấu hình. Bạn có thể sử dụng thông tin thời gian thực này để cập nhật hệ thống hoặc kích hoạt các quy trình nghiệp vụ cụ thể, đảm bảo ứng dụng luôn đồng bộ với các sự kiện trên TikTok một cách hiệu quả và kịp thời.

**Bạn có thể đăng ký nhận Webhook của tài khoản TikTok để theo dõi vòng đời nội dung đã đăng, cũng như giám sát và phản hồi tương tác của người dùng qua bình luận.**

### Điều kiện tiên quyết (Prerequisites)

Bạn đã được cấp quyền truy cập TikTok API for Business. Đảm bảo bạn đã hoàn thành các bước sau:
1. [Tạo tài khoản TikTok For Business](../04-get-started/bat-dau.md#doc-1738855099573250).
2. [Đăng ký làm nhà phát triển](../04-get-started/bat-dau.md#doc-1738855176671234).
3. [Tạo ứng dụng nhà phát triển](../04-get-started/bat-dau.md#doc-1738855242728450).
4. [Ủy quyền Accounts API](../10-organic-api/accounts-api.md#doc-1738083939371009).

- Nếu muốn đăng ký sự kiện xuất bản bài đăng, hãy đảm bảo bạn đã chọn quyền **TikTok Accounts** > **Business Content** cho ứng dụng nhà phát triển.
- Nếu muốn đăng ký sự kiện cập nhật bình luận, hãy đảm bảo bạn đã chọn quyền **TikTok Accounts** > **Business Comment** cho ứng dụng nhà phát triển.

### Các bước thực hiện (Steps)

#### Đăng ký sự kiện xuất bản bài đăng (Subscribe to post publishing events)

Để đăng ký sự kiện xuất bản bài đăng cho ứng dụng nhà phát triển, hãy gọi endpoint [/business/webhook/update/](../12-api-reference/01-accounts-p2.md#doc-1810521279479810). Trong yêu cầu, hãy cung cấp App ID (`app_id`) và Secret (`secret`) của ứng dụng, nhập URL gọi lại vào trường `callback_url` và chỉ định `VIDEO` trong trường `event_type`.

**Ví dụ:**

Yêu cầu (Request)
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/business/webhook/update/' \
--header 'Content-Type: application/json' \
--data '{
    "app_id": "{{app_id}}",
    "secret": "{{secret}}",
    "event_type": "VIDEO",
    "callback_url": "{{callback_url}}"
}'
```

Phản hồi (Response)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "app_id": "{{app_id}}",
        "callback_url": "{{callback_url}}",
        "event_type": "VIDEO"
    }
}
```

Sau khi cấu hình thành công, URL gọi lại đã chỉ định sẽ nhận thông báo theo thời gian thực về các thay đổi trạng thái của bài đăng được xuất bản qua [/business/video/publish/](../12-api-reference/01-accounts-p1.md#doc-1762228496095234) hoặc [/business/photo/publish/](../12-api-reference/01-accounts-p1.md#doc-1803630424390658). Để tìm hiểu về lược đồ và mã mẫu của phản hồi Webhook cho danh mục sự kiện này, xem [Sự kiện xuất bản bài đăng](../10-organic-api/accounts-api.md#doc-1810515090228226).

#### Đăng ký sự kiện cập nhật bình luận (Subscribe to the comment update event)

Để đăng ký sự kiện cập nhật bình luận cho ứng dụng nhà phát triển, hãy gọi endpoint [/business/webhook/update/](../12-api-reference/01-accounts-p2.md#doc-1810521279479810). Trong yêu cầu, cung cấp `app_id`, `secret`, nhập URL gọi lại vào trường `callback_url` và chỉ định `COMMENT` trong trường `event_type`. Tùy chọn, bạn có thể chỉ định các bài đăng TikTok cụ thể muốn nhận thông báo qua trường `item_list`.

**Ví dụ:**

##### Đăng ký sự kiện cập nhật bình luận cho tất cả bài đăng
Yêu cầu (Request)
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/business/webhook/update/' \
--header 'Content-Type: application/json' \
--data '{
    "app_id": "{{app_id}}",
    "secret": "{{secret}}",
    "event_type": "COMMENT",
    "callback_url": "{{callback_url}}"
}'
```

Phản hồi (Response)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "app_id": "{{app_id}}",
        "callback_url": "{{callback_url}}",
        "event_type": "COMMENT"
    }
}
```

##### Đăng ký sự kiện cập nhật bình luận cho các bài đăng cụ thể
Yêu cầu (Request)
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/business/webhook/update/' \
--header 'Content-Type: application/json' \
--data '{
    "app_id": "{{app_id}}",
    "secret": "{{secret}}",
    "event_type": "COMMENT",
    "callback_url": "{{callback_url}}",
    "item_list": ["{{item_id}}","{{item_id}}"]
}'
```

Phản hồi (Response)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "app_id": "{{app_id}}",
        "callback_url": "{{callback_url}}",
        "event_type": "COMMENT",
        "item_list": [
            "{{item_id}}",
            "{{item_id}}"
        ]
    }
}
```

Sau khi cấu hình thành công, URL gọi lại của bạn sẽ nhận thông báo thời gian thực khi bình luận hoặc câu trả lời được tạo hoặc bị xóa, hoặc khi cài đặt chế độ hiển thị bình luận/câu trả lời bị thay đổi trên bất kỳ video công khai nào thuộc tài khoản TikTok sở hữu. Xem chi tiết tại [Sự kiện cập nhật bình luận](../10-organic-api/accounts-api.md#doc-1810515104773122).

### Tài liệu liên quan (Related docs)

- [Webhooks](../10-organic-api/accounts-api.md#doc-1759977800177665)
- [Các loại sự kiện Webhook (Webhook event types)](../10-organic-api/accounts-api.md#doc-1759978319341570)
- [Webhooks API](../12-api-reference/01-accounts-p2.md#doc-1810521243195393)

## Đăng ký lượt nhắc đến qua Webhooks API (`Subscribe to mentions via Webhooks API`)
<a id="doc-1825113658431489"></a>
<!-- doc_id: 1825113658431489 -->

> Đường dẫn: Use Cases > Webhook subscription > Subscribe to mentions via Webhooks API

Hướng dẫn này giúp bạn từng bước nhận thông báo khi doanh nghiệp của bạn được nhắc đến (@mention) trong chú thích bài đăng hoặc bình luận qua Webhook.

### Giới thiệu (Introduction)

Webhook là các lệnh gọi lại HTTP tự động được kích hoạt khi sự kiện cụ thể diễn ra trên TikTok, cho phép gửi thông báo thời gian thực đến URL gọi lại của bạn mà không cần gọi API thăm dò liên tục. Thông báo được gửi dưới dạng HTTPS POST JSON.

**Bạn có thể đăng ký nhận Webhook lượt nhắc đến (Mentions Webhooks) để kịp thời nắm bắt các lượt nhắc đến doanh nghiệp, phản hồi bình luận nhanh chóng và duy trì tương tác tích cực với cộng đồng.**

> [!NOTE]
> Độ trễ của Mentions Webhooks có thể lên đến 2 hoặc 3 giờ.

### Điều kiện tiên quyết (Prerequisites)

Bạn đã được cấp quyền truy cập TikTok API for Business và hoàn thành:
1. [Tạo tài khoản TikTok For Business](../04-get-started/bat-dau.md#doc-1738855099573250).
2. [Đăng ký làm nhà phát triển](../04-get-started/bat-dau.md#doc-1738855176671234).
3. [Tạo ứng dụng nhà phát triển](../04-get-started/bat-dau.md#doc-1738855242728450).
4. [Ủy quyền Mentions API](../10-organic-api/mentions-api.md#doc-1825103730490434).
- Đảm bảo bạn đã chọn quyền **Mentions** cho ứng dụng nhà phát triển.

### Các bước thực hiện (Steps)

Để đăng ký sự kiện Mentions cho ứng dụng nhà phát triển, hãy gọi endpoint [/business/webhook/update/](../12-api-reference/51-mentions.md#doc-1825108008121346). Cung cấp App ID (`app_id`) và Secret (`secret`) của ứng dụng, nhập URL gọi lại vào `callback_url` và chỉ định `BRAND_MENTION` trong trường `event_type`.

**Ví dụ:**

Yêu cầu (Request)
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/business/webhook/update/' \
--header 'Content-Type: application/json' \
--data '{
    "app_id": "{{app_id}}",
    "secret": "{{secret}}",
    "event_type": "BRAND_MENTION",
    "callback_url": "{{callback_url}}"
}'
```

Phản hồi (Response)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "app_id": "{{app_id}}",
        "callback_url": "{{callback_url}}",
        "event_type": "BRAND_MENTION"
    }
}
```

Sau khi cấu hình thành công, URL gọi lại sẽ nhận thông báo trong vòng 2 đến 3 giờ sau khi người dùng nhắc đến doanh nghiệp trong chú thích bài đăng hoặc bình luận.

Xem thêm về xác minh Webhook tại [Xác minh Webhook (Webhook verification)](../10-organic-api/accounts-api.md#doc-1759978341579777).

### Lược đồ Webhook (Webhook schema)

Khi đăng ký thành công, chúng tôi sẽ gửi thông báo theo lược đồ sau:

| Field | Data Type | Description |
|---|---|---|
| client_key | string | ID ứng dụng nhà phát triển trên cổng TikTok API for Business, tìm thấy trong [My Apps](https://ads.tiktok.com/marketing_api/apps/). <br> Ví dụ: `bwo1m23456a7k89`. |
| content | string | Chuỗi JSON đã tuần tự hóa chứa thông tin sự kiện. <br> Xem chi tiết tại mục [Nội dung sự kiện `content`](#noi-dung-su-kien-content). |
| create_time | integer | Thời gian xảy ra sự kiện, định dạng Epoch/Unix timestamp (UTC) tính bằng giây. <br> Ví dụ: 1615338610. |
| event | string | Tên loại sự kiện. <br> Giá trị enum: `brand.mention.event`: Sự kiện nhắc đến thương hiệu. |
| user_openid | string | ID duy nhất theo ứng dụng của tài khoản TikTok được nhắc đến, lấy từ trường `open_id` của endpoint [/tt_user/oauth2/token/](../10-organic-api/mentions-api.md#doc-1825105003772930) và dùng làm tham số `business_id` trong các yêu cầu Mentions API. <br> Ví dụ: `1234a567-8912-3456-b7cd-8efg9h123ad4`. |

**Tải trọng mẫu (Example payload):**
```json
{
    "client_key": "{{client_key}}",
    "content": "{\"type_of_event\": \"CREATE\",\"mention_type\": \"VIDEO MENTION\",\"video_id\": \"{{video_id}}\",\"video_create_time\":1732150245,\"open_id_of_mentioned_user\": \"{{open_id_of_mentioned_user}}\",\"unique_name_of_mentioned_user\": \"{{unique_name_of_mentioned_user}}\",\"unique_identifier\": \"{{unique_identifier}}\",\"share_url\": \"{{share_url}}\",\"video_caption\": \"{{video_caption}}\",\"comment_id\": \"0\"}",
    "create_time": 1732150252,
    "event": "brand.mention.event",
    "user_openid": "{{user_openid}}"
}
```

#### <a id="noi-dung-su-kien-content"></a>Nội dung sự kiện `content` (Event `content`)

| Field | Data Type | Description |
|---|---|---|
| type_of_event | string | Loại sự kiện. <br> Giá trị enum: `CREATE`: Tạo lượt nhắc đến; `EDIT`: Chỉnh sửa lượt nhắc đến; `PRIVACY_CHANGE`: Thay đổi cài đặt quyền riêng tư của bài đăng. |
| mention_type | string | Loại lượt nhắc đến. <br> Giá trị enum: `COMMENT`: Bình luận hoặc câu trả lời nhắc đến (@) tên người dùng của doanh nghiệp trong nội dung bình luận; `VIDEO_MENTION`: Bài đăng nhắc đến (@) tên người dùng của doanh nghiệp trong phần chú thích. |
| video_id | string | Mã định danh duy nhất của bài đăng TikTok. |
| video_create_time | integer | Thời gian video được tạo, theo Epoch/Unix timestamp (giây). <br> Ví dụ: 1615338610. |
| open_id_of_mentioned_user | string | ID duy nhất theo ứng dụng của tài khoản TikTok được nhắc đến. |
| unique_name_of_mentioned_user | string | Tên người dùng (username) của tài khoản TikTok được nhắc đến. |
| unique_identifier | string | Mã định danh duy nhất toàn cầu gán cho mỗi người dùng bình luận, nhất quán giữa các API. <br> Ví dụ: `abcdefg+GUH12wq34==`. |
| share_url | string | URL có thể chia sẻ cho bài đăng TikTok. |
| video_caption | string | Chú thích của bài đăng TikTok. |
| comment_id | string | Mã định danh duy nhất của bình luận. Khi `mention_type` là `VIDEO_MENTION`, trường này có giá trị `"0"`. |

```json
"content": {
    "type_of_event": "CREATE",
    "mention_type": "VIDEO MENTION",
    "video_id": "{{video_id}}",
    "video_create_time": 1615338610,
    "open_id_of_mentioned_user": "{{open_id_of_mentioned_user}}",
    "unique_name_of_mentioned_user": "{{unique_name_of_mentioned_user}}",
    "unique_identifier": "{{unique_identifier}}",
    "share_url": "{{share_url}}",
    "video_caption": "{{video_caption}}",
    "comment_id": "0"
}
```


## Đăng ký sự kiện Business Messaging Webhook qua Webhooks API (`Subscribe to Business Messaging Webhook events via Webhooks API`)
<a id="doc-1832190670631937"></a>
<!-- doc_id: 1832190670631937 -->

> Đường dẫn: Use Cases > Webhook subscription > Subscribe to Business Messaging Webhook events via Webhooks API

Hướng dẫn này giúp bạn từng bước nhận thông báo về các sự kiện Nhắn tin Doanh nghiệp (Business Messaging), chẳng hạn như gửi và nhận tin nhắn trực tiếp hoặc các cập nhật về cài đặt tin nhắn tự động thông qua Webhook.

### Giới thiệu (Introduction)

Webhook là các lệnh gọi lại HTTP tự động được kích hoạt khi các sự kiện cụ thể diễn ra trong nền tảng TikTok, cho phép gửi thông báo theo thời gian thực đến URL gọi lại mà bạn chỉ định. Cơ chế này loại bỏ nhu cầu phải liên tục gọi API thăm dò (polling). Thay vào đó, TikTok chủ động gửi dữ liệu sự kiện đến hệ thống của bạn ngay khi sẵn sàng qua HTTPS POST dưới định dạng JSON.

**Bạn có thể đăng ký nhận Webhook tin nhắn doanh nghiệp (Business Message Webhooks) để cập nhật liên tục các hoạt động tin nhắn trực tiếp và tin nhắn tự động cho doanh nghiệp. Điều này giúp phản hồi tin nhắn kịp thời và duy trì các cuộc trò chuyện có ý nghĩa với cộng đồng.**

### Điều kiện tiên quyết (Prerequisites)

Bạn đã được cấp quyền truy cập TikTok API for Business và hoàn thành:
1. [Tạo tài khoản TikTok For Business](../04-get-started/bat-dau.md#doc-1738855099573250).
2. [Đăng ký làm nhà phát triển](../04-get-started/bat-dau.md#doc-1738855176671234).
3. [Tạo ứng dụng nhà phát triển](../04-get-started/bat-dau.md#doc-1738855242728450).
4. [Ủy quyền Business Messaging API](../11-business-messaging-api/business-messaging-api.md#doc-1832184159540418).
- Đảm bảo đã chọn quyền **Business Messaging** cho ứng dụng nhà phát triển.
5. Để đảm bảo thông báo webhook hoạt động trơn tru, vui lòng nhắc doanh nghiệp **thiết lập tài khoản TikTok chấp nhận tin nhắn trực tiếp từ mọi người** trong ứng dụng TikTok trước khi ủy quyền cho ứng dụng nhà phát triển quản lý tin nhắn. Nếu không, chủ tài khoản TikTok sẽ phải chấp nhận yêu cầu tin nhắn từ người dùng theo cách thủ công trong ứng dụng TikTok trước khi nhận được webhook.

### Các bước thực hiện (Steps)

Nhà phát triển cần đăng ký Business Messaging Webhook ở cấp độ ứng dụng sau khi nhận được ủy quyền từ doanh nghiệp. Sau khi hoàn tất cấu hình, bạn sẽ nhận được thông báo Webhook cho tất cả các doanh nghiệp đã ủy quyền cho ứng dụng mà không cần phải đăng ký lại cho từng doanh nghiệp mới.

Để đăng ký sự kiện Business Messaging Webhook cho ứng dụng nhà phát triển, hãy gọi endpoint [/business/webhook/update/](../12-api-reference/23-business-messaging.md#doc-1832184470423554). Cung cấp `app_id`, `secret`, nhập URL gọi lại vào `callback_url` và chỉ định `DIRECT_MESSAGE` trong trường `event_type`.

**Ví dụ:**

Yêu cầu (Request)
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/business/webhook/update/' \
--header 'Content-Type: application/json' \
--data '{
    "app_id": "{{app_id}}",
    "secret": "{{secret}}",
    "event_type": "DIRECT_MESSAGE",
    "callback_url": "{{callback_url}}"
}'
```

Phản hồi (Response)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "app_id": "{{app_id}}",
        "callback_url": "{{callback_url}}",
        "event_type": "DIRECT_MESSAGE"
    }
}
```

Xem chi tiết về cách xác minh Webhook tại [Xác minh Webhook](../10-organic-api/accounts-api.md#doc-1759978341579777).

### Lược đồ Webhook (Webhook schema)

Sau khi đăng ký thành công, chúng tôi sẽ thông báo cho bạn theo các lược đồ sau tùy theo từng loại sự kiện:

#### 1. Sự kiện gửi tin nhắn (`im_send_msg`)

| Field | Data Type | Description |
|---|---|---|
| client_key | string | ID ứng dụng nhà phát triển của bạn trên cổng TikTok API for Business. |
| event | string | Tên sự kiện: `im_send_msg` (nhận thông báo thời gian thực khi bạn gửi tin nhắn cho người dùng). |
| create_time | integer | Thời gian gửi thông báo sự kiện, theo Epoch/Unix timestamp (giây). |
| user_openid | string | ID duy nhất của tài khoản TikTok theo ứng dụng, lấy từ trường `open_id` của [/tt_user/oauth2/token/](../11-business-messaging-api/business-messaging-api.md#doc-1832184175482945). |
| content | string | Chuỗi JSON chứa thông tin chi tiết sự kiện `im_send_msg`. |

**Lược đồ `content` cho `im_send_msg`:**

| Field | Data Type | Description |
|---|---|---|
| from | string | Tên người dùng TikTok của người gửi tin nhắn. |
| to | string | Tên người dùng TikTok của người nhận tin nhắn. |
| unique_identifier | string | ID duy nhất của người dùng TikTok trong cuộc trò chuyện (nhất quán giữa các API). |
| from_user | object | Thông tin người dùng của người gửi. |
| ↳ role | string | Loại tài khoản người gửi (`business_account` hoặc `personal_account`). |
| ↳ id | string | Mã định danh người gửi (`business_id` hoặc `unique_identifier`). |
| to_user | object | Thông tin người dùng của người nhận. |
| ↳ role | string | Loại tài khoản người nhận (`business_account` hoặc `personal_account`). |
| ↳ id | string | Mã định danh người nhận (`business_id` hoặc `unique_identifier`). |
| referenced_message_info | object | Thông tin về tin nhắn gốc được trả lời. |
| ↳ referenced_message_id | string | ID của tin nhắn gốc được trả lời. |
| conversation_id | string | ID cuộc trò chuyện (dùng giá trị này để gửi tin nhắn). |
| message_id | string | ID tin nhắn. |
| timestamp | integer | Thời gian gửi tin nhắn, theo Epoch/Unix timestamp tính bằng mili giây. |
| text | object | Thông tin văn bản (khi `type` là `text`). |
| ↳ body | string | Nội dung văn bản. |
| image | object | Thông tin hình ảnh (khi `type` là `image`). |
| ↳ media_id | string | ID hình ảnh. |
| share_post | object | Thông tin bài đăng được chia sẻ (khi `type` là `share_post`). |
| ↳ embed_url | string | Liên kết nhúng bài đăng TikTok. |
| ↳ video_id | string | ID của bài đăng TikTok. |
| reaction | object[] | Danh sách biểu cảm (reactions) phản hồi tin nhắn. |
| ↳ operation | string | Thao tác: `ADD` (thêm cảm xúc) hoặc `REMOVE` (hủy cảm xúc). |
| ↳ type | string | Loại cảm xúc: `EMOJI` hoặc `AI_EMOJI`. |
| ↳ emoji | string | Nội dung emoji văn bản. |
| ↳ ai_emoji_url | string | URL hình ảnh AI emoji. |
| ↳ unique_identifier | string | Mã định danh người gửi cảm xúc. |
| ↳ timestamp | integer | Thời gian thả cảm xúc (mili giây). |
| ↳ original_msg_id | string | ID tin nhắn nhận cảm xúc. |
| sticker | object | Thông tin nhãn dán (khi `type` là `sticker`). Chứa `url`. |
| emoji | object | Thông tin biểu tượng cảm xúc (khi `type` là `emoji`). Chứa `url`. |
| video | object | Thông tin video (khi `type` là `video`). Chứa `media_id`. |
| template | object | Chi tiết mẫu tin nhắn (khi `type` là `template`). |
| ↳ type | string | Loại mẫu tin nhắn: `qa_button_card` hoặc `qa_link_card`. |
| ↳ elements | object[] | Thẻ nội dung trong mẫu tin nhắn. |
| ↳↳ title | string | Câu hỏi cài đặt sẵn trên thẻ. |
| ↳↳ buttons | object[] | Danh sách nút hoặc liên kết câu trả lời. |
| ↳↳↳ text | string | Nội dung văn bản nút/liên kết. |
| ↳↳↳ type | string | Loại nút: `REPLY`. |
| ↳↳↳ id | string | ID tự định nghĩa cho nút/liên kết. |
| type | string | Loại tin nhắn: `text`, `image`, `share_post`, `video`, `emoji`, `sticker`, `reaction`, `template`. |
| auto_message_type | string | Loại tin nhắn tự động: `WELCOME_MESSAGE`, `SUGGESTED_QUESTION`, `AUTO_REPLY`. |
| scene_type | integer | Loại ngữ cảnh (mặc định là 0). |
| is_follower | boolean | Người dùng tài khoản cá nhân có theo dõi tài khoản doanh nghiệp không (`true`/`false`). |
| message_tag | object | Thông tin bổ sung về tin nhắn. |
| ↳ source | string | Nguồn gửi tin nhắn: `APP`, `WEB`, `API`, `OTHERS`, `UNKNOWN_SOURCE`. |

#### 2. Sự kiện nhận tin nhắn (`im_receive_msg`)

Sự kiện `im_receive_msg` được kích hoạt khi nhận tin nhắn từ người dùng ngoài Khu vực Kinh tế Châu Âu (EEA), Thụy Sĩ hoặc Vương quốc Anh. (Nếu người dùng thuộc EEA, Thụy Sĩ hoặc Vương quốc Anh, bạn sẽ nhận sự kiện `im_receive_msg_eu`).

| Field | Data Type | Description |
|---|---|---|
| client_key | string | ID ứng dụng nhà phát triển. |
| event | string | Tên sự kiện: `im_receive_msg`. |
| create_time | integer | Thời gian thông báo gửi đi (giây). |
| user_openid | string | ID duy nhất của tài khoản TikTok theo ứng dụng (`open_id`). |
| content | string | Chuỗi JSON chứa chi tiết sự kiện `im_receive_msg`. |

**Lược đồ `content` cho `im_receive_msg`:**
Tương tự như `im_send_msg`, bao gồm các trường: `from`, `to`, `unique_identifier`, `from_user`, `to_user`, `referenced_message_info`, `conversation_id`, `message_id`, `timestamp`, `text`, `image`, `share_post`, `reaction`, `sticker`, `emoji`, `video`, `template`, `type`, `auto_message_type`, `scene_type`, `is_follower`, `message_tag`, cùng với:
- `reply_source_payload` (object): Chi tiết phản hồi tự động kích hoạt bởi nút trên thẻ Q&A.
  - `↳ reply_source_msg_id` (string): ID tin nhắn gửi vào cuộc trò chuyện thay cho người dùng.
  - `↳ reply_source_unique_id` (string): ID do chủ tài khoản định nghĩa cho nút hoặc liên kết Q&A.

#### 3. Sự kiện nhận tin nhắn từ người dùng Châu Âu (`im_receive_msg_eu`)

| Field | Data Type | Description |
|---|---|---|
| client_key | string | ID ứng dụng nhà phát triển. |
| event | string | Tên sự kiện: `im_receive_msg_eu`. |
| create_time | integer | Thời gian xảy ra sự kiện (giây). |
| user_openid | string | ID duy nhất của tài khoản TikTok theo ứng dụng. |
| content | string | Chuỗi JSON chứa chi tiết sự kiện. |

**Lược đồ `content` cho `im_receive_msg_eu`:**

| Field | Data Type | Description |
|---|---|---|
| to | string | Tên người dùng TikTok của người nhận tin nhắn. |
| to_user | object | Thông tin người nhận tin nhắn. |
| ↳ role | string | Loại tài khoản: `business_account`. |
| ↳ id | string | Mã định danh người nhận (`business_id`). |
| timestamp | integer | Thời gian của sự kiện (mili giây). |

#### 4. Sự kiện tin nhắn chuyển tiếp (`im_referral_msg`)

Sự kiện `im_referral_msg` được kích hoạt khi người dùng tham gia cuộc trò chuyện từ một nguồn chuyển tiếp (chẳng hạn như quảng cáo Click-to-Message hoặc liên kết TikTok.me).

| Field | Data Type | Description |
|---|---|---|
| client_key | string | ID ứng dụng nhà phát triển. |
| event | string | Tên sự kiện: `im_referral_msg`. |
| create_time | integer | Thời gian gửi thông báo sự kiện (giây). |
| user_openid | string | ID duy nhất của tài khoản TikTok theo ứng dụng. |
| content | string | Chuỗi JSON chứa chi tiết sự kiện `im_referral_msg`. |

**Lược đồ `content` cho `im_referral_msg`:**

| Field | Data Type | Description |
|---|---|---|
| from | string | Tên người dùng TikTok của người gửi. |
| to | string | Tên người dùng TikTok của người nhận. |
| unique_identifier | string | ID duy nhất của người dùng TikTok trong cuộc trò chuyện. |
| from_user | object | Thông tin người dùng của người gửi (`role`, `id`). |
| to_user | object | Thông tin người dùng của người nhận (`role`, `id`). |
| conversation_id | string | ID cuộc trò chuyện. |
| timestamp | integer | Thời gian người dùng vào cuộc trò chuyện (mili giây). |
| is_follower | boolean | Người dùng có theo dõi tài khoản doanh nghiệp không (`true`/`false`). |
| referral | object | Thông tin nguồn chuyển tiếp. |
| ↳ source | string | Nguồn chuyển tiếp: `ad` (từ quảng cáo Click-to-Message) hoặc `short_link` (từ liên kết TikTok.me). |
| ↳ ad | object | Thông tin quảng cáo (khi `source` là `ad`). |
| ↳↳ advertiser_id | string | ID tài khoản nhà quảng cáo liên kết với quảng cáo. |
| ↳↳ ad_id | string | ID của quảng cáo chuyển tiếp (quảng cáo thủ công, Smart+ Campaign hoặc Upgraded Smart+ Ad). |
| ↳↳ timestamp | integer | Thời gian người dùng nhấp vào quảng cáo (mili giây). |
| ↳↳ ad_name | string | Tên quảng cáo liên quan. |
| ↳↳ embed_url | string | Liên kết nhúng video quảng cáo. |
| ↳↳ message_material_id | string | ID tài liệu sáng tạo trong Upgraded Smart+ Ads. |
| ↳ short_link | object | Thông tin liên kết TikTok.me (khi `source` là `short_link`). |
| ↳↳ ref | string | Tham số chuyển tiếp (`ref`) cấu hình trong liên kết TikTok.me. |
| ↳↳ prefilled_message | string | Tin nhắn điền sẵn cấu hình trong liên kết TikTok.me. |
| ↳↳ prefilled_message_audit_status | string | Trạng thái xét duyệt tin nhắn điền sẵn (`PASS` hoặc `REJECT`). |

#### 5. Sự kiện đánh dấu đã đọc tin nhắn (`im_mark_read_msg`)

Được kích hoạt khi người dùng tài khoản cá nhân đánh dấu đã đọc tất cả tin nhắn trong phiên trò chuyện.

| Field | Data Type | Description |
|---|---|---|
| client_key | string | ID ứng dụng nhà phát triển. |
| event | string | Tên sự kiện: `im_mark_read_msg`. |
| create_time | integer | Thời gian thông báo (giây). |
| user_openid | string | ID duy nhất của tài khoản TikTok theo ứng dụng. |
| content | string | Chuỗi JSON chứa chi tiết sự kiện. |

**Lược đồ `content` cho `im_mark_read_msg`:**

| Field | Data Type | Description |
|---|---|---|
| from | string | Tên người dùng gửi. |
| to | string | Tên người dùng nhận. |
| unique_identifier | string | ID duy nhất của người dùng TikTok. |
| from_user | object | Người gửi (`role` là `personal_account`, `id` là `unique_identifier`). |
| to_user | object | Người nhận (`role` là `business_account`, `id` là `business_id`). |
| conversation_id | string | ID cuộc trò chuyện. |
| timestamp | integer | Thời điểm người dùng đánh dấu đã đọc (mili giây). |
| read | object | Thông tin hành động đánh dấu đã đọc. |
| ↳ last_read_timestamp | integer | Thời điểm tin nhắn cuối cùng được đọc (mili giây). |

#### 6. Sự kiện cập nhật cấu hình tin nhắn tự động (`im_auto_message_config_update`)

Được kích hoạt trong vòng 5 phút khi tin nhắn tự động được tạo, xóa, cập nhật, bật hoặc tắt.

| Field | Data Type | Description |
|---|---|---|
| client_key | string | ID ứng dụng nhà phát triển. |
| event | string | Tên sự kiện: `im_auto_message_config_update`. |
| create_time | integer | Thời gian thông báo (giây). |
| user_openid | string | ID duy nhất của tài khoản TikTok theo ứng dụng. |
| content | string | Chuỗi JSON chứa chi tiết sự kiện. |

**Lược đồ `content` cho `im_auto_message_config_update`:**

| Field | Data Type | Description |
|---|---|---|
| auto_message_id | string | ID của tin nhắn tự động. |
| auto_message_type | string | Loại tin nhắn tự động: `WELCOME_MESSAGE`, `SUGGESTED_QUESTION`, `CHAT_PROMPT`. |
| auto_message_action | string | Hành động: `CREATE`, `UPDATE`, `DELETE`, `ENABLE`, `DISABLE`. |
| timestamp | number | Thời điểm hành động diễn ra (mili giây). |
| welcome_message | object | Thông tin tin nhắn chào mừng (khi `auto_message_type` là `WELCOME_MESSAGE`). |
| ↳ content | string | Nội dung văn bản của tin nhắn chào mừng. |
| suggested_question | object | Thông tin câu hỏi gợi ý (khi `auto_message_type` là `SUGGESTED_QUESTION`). |
| ↳ question | string | Câu hỏi thường gặp để người dùng bắt đầu cuộc trò chuyện. |
| ↳ answer | string | Câu trả lời cài sẵn tự động gửi khi chọn câu hỏi. |
| chat_prompt | object | Thông tin nút gợi ý trò chuyện (khi `auto_message_type` là `CHAT_PROMPT`). |
| ↳ title | string | Tên nút hiển thị phía trên hộp nhập tin nhắn. |
| ↳ content | string | Câu hỏi tương ứng hệ thống tạo ra khi người dùng chạm vào prompt. |

#### 7. Sự kiện cập nhật trạng thái xét duyệt tin nhắn tự động (`im_auto_message_audit_update`)

Kích hoạt trong vòng 5 phút khi tin nhắn tự động được phê duyệt hoặc bị từ chối.

| Field | Data Type | Description |
|---|---|---|
| client_key | string | ID ứng dụng nhà phát triển. |
| event | string | Tên sự kiện: `im_auto_message_audit_update`. |
| create_time | integer | Thời gian gửi thông báo (giây). |
| user_openid | string | ID duy nhất của tài khoản TikTok theo ứng dụng. |
| content | string | Chuỗi JSON chứa chi tiết sự kiện. |

**Lược đồ `content` cho `im_auto_message_audit_update`:**

| Field | Data Type | Description |
|---|---|---|
| auto_message_id | string | ID của tin nhắn tự động. |
| auto_message_type | string | Loại tin nhắn tự động: `WELCOME_MESSAGE`, `SUGGESTED_QUESTION`, `CHAT_PROMPT`. |
| audit_status | string | Trạng thái xét duyệt: `APPROVED` (đã duyệt) hoặc `REJECTED` (bị từ chối). |
| timestamp | number | Thời điểm xét duyệt (mili giây). |

#### 8. Sự kiện nhận bình luận có ý định mua hàng cao (`im_receive_high_intent_comment`)

Kích hoạt khi người dùng để lại bình luận thể hiện ý định mua hàng hoặc tìm hiểu thông tin rõ ràng trên video.

| Field | Data Type | Description |
|---|---|---|
| client_key | string | ID ứng dụng nhà phát triển. |
| event | string | Tên sự kiện: `im_receive_high_intent_comment`. |
| create_time | integer | Thời gian gửi thông báo (giây). |
| user_openid | string | ID duy nhất của tài khoản TikTok theo ứng dụng. |
| content | string | Chuỗi JSON chứa chi tiết sự kiện. |

**Lược đồ `content` cho `im_receive_high_intent_comment`:**

| Field | Data Type | Description |
|---|---|---|
| from | string | Tên người dùng gửi bình luận. |
| to | string | Tên người dùng nhận bình luận. |
| timestamp | number | Thời gian sự kiện (mili giây). |
| unique_identifier | string | ID duy nhất của người dùng TikTok trong cuộc trò chuyện. |
| from_user | object | Người gửi (`role`: `business_account`/`personal_account`, `id`). |
| to_user | object | Người nhận (`role`: `business_account`/`personal_account`, `id`). |
| comment_id | string | ID duy nhất của bình luận. |
| comment_text | string | Nội dung văn bản của bình luận. |
| is_follower | boolean | Người dùng có theo dõi tài khoản không (`true`/`false`). |

### Bước tiếp theo (Next step)

Xem thêm [Xác thực cho Business Messaging API](../11-business-messaging-api/business-messaging-api.md#doc-1832184175482945).


## Đăng ký sự kiện Webhook của tài khoản quảng cáo qua Subscription API (`Subscribe to ad account Webhook events via Subscription API`)
<a id="doc-1810521739537409"></a>
<!-- doc_id: 1810521739537409 -->

> Đường dẫn: Use Cases > Webhook subscription > Subscribe to ad account Webhook events via Subscription API

Bài viết này hướng dẫn bạn từng bước đăng ký nhận thông báo Webhook cho các sự kiện ở cấp tài khoản quảng cáo bằng Subscription API.

### Giới thiệu (Introduction)

Subscription API cho phép bạn đăng ký nhận thông báo thời gian thực khi có các thay đổi hoặc sự kiện diễn ra đối với tài khoản quảng cáo, bao gồm:
- Thay đổi dữ liệu chỉ số báo cáo (Reporting metric data changes).
- Khách hàng tiềm năng mới (Leads).
- Trạng thái xét duyệt quảng cáo (Ad review status).
- Trạng thái suy giảm/bão hòa quảng cáo (Ad fatigue status).
- Liên kết video TikTok với chiến dịch TikTok One (TTO).
- Trạng thái đình chỉ của tài khoản quảng cáo (Ad account suspension status).
- Sự cố dịch vụ API (API service incident).

### Điều kiện tiên quyết (Prerequisites)

- Bạn đã được cấp quyền truy cập TikTok API for Business và có các quyền tương ứng cho các thực thể đăng ký.
- Cấu hình endpoint webhook của bạn sẵn sàng nhận các yêu cầu HTTPS POST với mã phản hồi 200 OK.
- Đảm bảo xác thực tải trọng (payload) bằng HMAC-SHA256 với Secret của ứng dụng. Xem **Xác thực payload Webhook**.

### Các bước thực hiện (Steps)

#### 1. Đăng ký thay đổi dữ liệu chỉ số báo cáo (Subscribe to reporting metric data changes)

Để nhận thông báo khi các chỉ số báo cáo quảng cáo có sự thay đổi đáng kể, hãy gọi endpoint [/subscription/subscribe/](../12-api-reference/66-subscription.md#doc-1739092028876801) với `subscribe_entity` đặt là `METRIC`.

**Ví dụ yêu cầu:**
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/subscription/subscribe/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "app_id": "{{app_id}}",
    "secret": "{{secret}}",
    "subscribe_entity": "METRIC",
    "callback_url": "{{callback_url}}",
    "subscription_detail": {
        "advertiser_id": "{{advertiser_id}}",
        "access_token": "{{access_token}}"
    }
}'
```

**Lược đồ tải trọng sự kiện chỉ số:**

| Field | Data Type | Description |
|---|---|---|
| request_id | string | ID duy nhất của yêu cầu. |
| object | string | Đối tượng đăng ký: `METRIC`. |
| time | integer | Thời gian sự kiện (Epoch/Unix timestamp). |
| entry | object[] | Danh sách các thay đổi chỉ số. |
| ↳ date | string | Ngày ghi nhận dữ liệu chỉ số. |
| ↳ data_level | string | Cấp độ dữ liệu (`AUCTION_ADVERTISER`, `AUCTION_CAMPAIGN`, `AUCTION_ADGROUP`, `AUCTION_AD`). |
| ↳ advertiser_id | string | ID tài khoản nhà quảng cáo. |
| ↳ advertiser_name | string | Tên tài khoản nhà quảng cáo. |
| ↳ campaign_id | string | ID chiến dịch (nếu có). |
| ↳ adgroup_id | string | ID nhóm quảng cáo (nếu có). |
| ↳ ad_id | string | ID quảng cáo (nếu có). |
| ↳ changed_metrics_values | object | Giá trị các chỉ số đã thay đổi. |

#### 2. Đăng ký nhận khách hàng tiềm năng (Subscribe to leads)

Để nhận thông báo tức thì khi có lead mới từ Biểu mẫu tức thì (Instant Form) hoặc Tin nhắn trực tiếp (Direct Message), hãy gọi [/subscription/subscribe/](../12-api-reference/66-subscription.md#doc-1739092028876801) với `subscribe_entity` đặt là `LEAD`.

**Ví dụ yêu cầu:**
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/subscription/subscribe/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "app_id": "{{app_id}}",
    "secret": "{{secret}}",
    "subscribe_entity": "LEAD",
    "callback_url": "{{callback_url}}",
    "subscription_detail": {
        "advertiser_id": "{{advertiser_id}}",
        "page_id": "{{page_id}}",
        "access_token": "{{access_token}}"
    }
}'
```

**Lược đồ tải trọng sự kiện lead:**

| Field | Data Type | Description |
|---|---|---|
| id | string | ID của khách hàng tiềm năng (Lead ID). |
| lead_source | string | Nguồn khách hàng tiềm năng: `INSTANT_FORM` hoặc `DIRECT_MESSAGE`. |
| page_id | number | ID trang của Biểu mẫu tức thì. |
| page_name | string | Tên trang của Biểu mẫu tức thì. |
| advertiser_id | number | ID nhà quảng cáo. |
| advertiser_name | string | Tên nhà quảng cáo. |
| library_id | number | ID của thư viện biểu mẫu. |
| campaign_id | number | ID chiến dịch quảng cáo. |
| campaign_name | string | Tên chiến dịch quảng cáo. |
| adgroup_id | number | ID nhóm quảng cáo. |
| adgroup_name | string | Tên nhóm quảng cáo. |
| ad_id | number | ID quảng cáo. |
| ad_name | string | Tên quảng cáo. |
| create_time | number | Thời gian tạo lead (Epoch/Unix timestamp giây). |
| changes | object[] | Mảng các trường thông tin thay đổi trong biểu mẫu hoặc tin nhắn trực tiếp. |
| ↳ field | string | Tên trường thông tin (ví dụ: `phone_number`, `email`, `name`). |
| ↳ value | object | Giá trị của trường thông tin. |

#### 3. Đăng ký trạng thái xét duyệt quảng cáo (Subscribe to the review status of your ad)

Để nhận thông báo khi quảng cáo được duyệt hoặc bị từ chối, hãy gọi [/subscription/subscribe/](../12-api-reference/66-subscription.md#doc-1739092028876801) với `subscribe_entity` đặt là `AD_AUDIT`.

**Lược đồ tải trọng sự kiện xét duyệt quảng cáo:**

| Field | Data Type | Description |
|---|---|---|
| log_id | string | ID nhật ký xét duyệt. |
| adv_id | number | ID tài khoản nhà quảng cáo (`advertiser_id`). |
| campaign_id | number | ID chiến dịch. |
| campaign_name | string | Tên chiến dịch. |
| adgroup_id | number | ID nhóm quảng cáo. |
| adgroup_name | string | Tên nhóm quảng cáo. |
| ad_id | number | ID quảng cáo. |
| ad_name | string | Tên quảng cáo. |
| status | string | Trạng thái xét duyệt mới của quảng cáo. |
| status_change_time | string | Thời điểm thay đổi trạng thái xét duyệt. |
| reject_reason | string[] | Danh sách lý do từ chối xét duyệt quảng cáo (nếu bị từ chối). |

#### 4. Đăng ký trạng thái bão hòa quảng cáo (Subscribe to the fatigue status of your ad)

Nhận thông báo khi hệ thống phát hiện các quảng cáo bị suy giảm hiệu quả hoặc bão hòa sáng tạo (creative fatigue). Sử dụng `subscribe_entity` là `AD_FATIGUE`.

**Lược đồ tải trọng sự kiện bão hòa:**

| Field | Data Type | Description |
|---|---|---|
| ad_ids | string[] | Danh sách các ID quảng cáo bị bão hòa. |
| adgroup_ids | string[] | Danh sách các ID nhóm quảng cáo chứa quảng cáo bị bão hòa. |
| message | string | Thông điệp mô tả chi tiết cảnh báo bão hòa quảng cáo. |
| event_type | string | Loại sự kiện thông báo bão hòa. |

#### 5. Đăng ký liên kết video TikTok với chiến dịch TTO (Subscribe to the linking of a TikTok video to a TTO campaign)

Nhận thông báo khi video TikTok được liên kết thành công với đơn hàng/chiến dịch trên TikTok One (TTO). Sử dụng `subscribe_entity` là `TTO_CAMPAIGN`.

**Lược đồ tải trọng:**

| Field | Data Type | Description |
|---|---|---|
| tto_campaign_event_type | string | Loại sự kiện chiến dịch TTO (ví dụ liên kết video). |
| tto_tcm_account_id | string | ID tài khoản TCM trên nền tảng TTO. |
| campaign_id | string | ID chiến dịch TTO. |
| video_id | string | ID video TikTok được liên kết. |
| event_time | string | Thời gian diễn ra sự kiện. |

#### 6. Đăng ký trạng thái đình chỉ của tài khoản quảng cáo (Subscribe to the suspension statuses of ad accounts)

Nhận thông báo tự động khi một tài khoản quảng cáo trong Business Center bị đình chỉ hoạt động do vi phạm chính sách hoặc các vấn đề an toàn. Sử dụng `subscribe_entity` là `ADVERTISER_SUSPENSION`.

**Lược đồ tải trọng sự kiện đình chỉ:**

| Field | Data Type | Description |
|---|---|---|
| owner_bc_id | string | ID của Business Center sở hữu tài khoản quảng cáo. |
| advertiser_id | string | ID tài khoản quảng cáo bị đình chỉ. |
| status | string | Trạng thái tài khoản (`SUSPENDED`). |
| suspension_reason | string | Lý do tài khoản bị đình chỉ. |
| handle_name | string | Tên người dùng hoặc đầu mối xử lý liên quan. |
| event_time | string | Thời gian diễn ra sự kiện đình chỉ. |

#### 7. Đăng ký trạng thái sự cố dịch vụ API (Subscribe to API service status)

Nhận cảnh báo sớm về các sự cố kỹ thuật hoặc bảo trì hệ thống API của TikTok for Business. Sử dụng `subscribe_entity` là `SERVICE_INCIDENT`.

**Lược đồ sự cố dịch vụ:**

| Field | Data Type | Description |
|---|---|---|
| incident_id | string | Mã định danh sự cố dịch vụ. |
| incident_event_type | string | Loại sự kiện sự cố (ví dụ: khởi phát, cập nhật, giải quyết). |
| incident_level | string | Mức độ nghiêm trọng của sự cố. |
| incident_title | string | Tiêu đề ngắn gọn về sự cố. |
| incident_detail | string | Chi tiết nguyên nhân và phạm vi ảnh hưởng của sự cố. |
| incident_products | string[] | Danh sách các sản phẩm và dịch vụ API bị ảnh hưởng. |
| incident_start_time | string | Thời điểm sự cố bắt đầu phát sinh. |
| incident_resolve_time | string | Thời điểm sự cố được giải quyết hoàn toàn. |

### Quản lý các gói đăng ký Webhook (Manage Webhook subscriptions)

- **Lấy danh sách các đăng ký hiện có:** Sử dụng endpoint [/subscription/get/](../12-api-reference/66-subscription.md#doc-1739093832125442). Giá trị trả về chứa thông tin `subscription_id` cho từng gói đăng ký.
- **Hủy gói đăng ký Webhook:** Sử dụng endpoint [/subscription/unsubscribe/](../12-api-reference/66-subscription.md#doc-1739094758789122) và truyền `subscription_id` cần hủy.

### Tài liệu liên quan (Related docs)

- **Subscription API**
- **Xác thực tải trọng Webhook (Validate webhook payloads)**
