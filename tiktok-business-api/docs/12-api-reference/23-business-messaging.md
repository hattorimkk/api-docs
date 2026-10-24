# Tin nhắn doanh nghiệp (Business Messaging)
<a id="doc-1832184349193282"></a>
<!-- doc_id: 1832184349193282 -->

TikTok Business Messaging API cung cấp các giải pháp giao tiếp và tương tác trực tiếp với khách hàng trên TikTok. Doanh nghiệp có thể nhận và gửi tin nhắn trực tiếp (Direct Messages), thiết lập webhook thông báo theo thời gian thực, và cấu hình các tin nhắn tự động (tin nhắn chào mừng, câu hỏi gợi ý, câu trả lời nhanh).

> [!IMPORTANT]
> Do tính chất nhạy cảm của dữ liệu tin nhắn trực tiếp, TikTok áp dụng quy trình kiểm duyệt bảo mật nghiêm ngặt. Trước khi gọi API, nhà phát triển cần hoàn thành đánh giá bảo mật quyền riêng tư và [được cấp quyền truy cập Business Messaging API](../11-business-messaging-api/business-messaging-api.md#doc-1832184145137922). Đồng thời, tài khoản TikTok phải là Tài khoản nâng cao (Advanced Access) hoặc Tài khoản doanh nghiệp đã xác minh (Verified Business Account).

Tài liệu này bao gồm 3 phân nhóm chính:
1. [Tin nhắn trực tiếp (Direct messages)](#tin-nhắn-trực-tiếp-direct-messages)
2. [Webhooks](#webhooks)
3. [Tin nhắn tự động (Automatic messages)](#tin-nhắn-tự-động-automatic-messages)

---

## Tin nhắn trực tiếp (`Direct messages`)
<a id="doc-1832184367408130"></a>
<!-- doc_id: 1832184367408130 -->

Nhóm API Tin nhắn trực tiếp cho phép doanh nghiệp gửi và nhận tin nhắn, quản lý danh sách cuộc hội thoại, tải lên/tải về tệp phương tiện đa phương tiện (hình ảnh, video), kiểm tra quyền năng nhắn tin và kích hoạt tính năng chuyển đổi bình luận thành tin nhắn trực tiếp.

Các endpoint trong nhóm:
* [Gửi tin nhắn đến cuộc hội thoại](23-business-messaging.md#doc-1832184403754242)
* [Lấy danh sách cuộc hội thoại](23-business-messaging.md#doc-1832184415059970)
* [Lấy danh sách tin nhắn](23-business-messaging.md#doc-1832184425841170)
* [Tải lên hình ảnh](23-business-messaging.md#doc-1832184437720193)
* [Tải về hình ảnh hoặc video từ tin nhắn](23-business-messaging.md#doc-1832184455450626)
* [Kiểm tra khả năng gửi tin nhắn của tài khoản TikTok](23-business-messaging.md#doc-1836061597865986)
* [Bật/tắt tính năng Chuyển bình luận thành tin nhắn](23-business-messaging.md#doc-1843697551083522)
* [Lấy cài đặt Chuyển bình luận thành tin nhắn](23-business-messaging.md#doc-1843697576682497)

---

## Gửi tin nhắn đến cuộc hội thoại (`Send a message to a conversation`)
<a id="doc-1832184403754242"></a>
<!-- doc_id: 1832184403754242 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/business/message/send/`

**Mục đích**: Sử dụng endpoint này để gửi tin nhắn (văn bản, hình ảnh, bài đăng TikTok, thẻ mẫu tương tác hoặc chỉ báo thao tác người gửi) đến một cuộc hội thoại cụ thể với người dùng TikTok.

> [!NOTE]
> - **Cửa sổ nhắn tin 48 giờ**: Bạn có thể gửi tối đa 10 tin nhắn trong vòng 48 giờ kể từ khi nhận được tin nhắn từ người dùng TikTok. Mỗi khi người dùng gửi một tin nhắn mới, cửa sổ 48 giờ sẽ được làm mới lại.
> - Một tin nhắn không thể chứa đồng thời cả văn bản và hình ảnh.

### Điều kiện tiên quyết
- Ứng dụng đã hoàn tất đánh giá bảo mật dữ liệu và được cấp quyền truy cập Business Messaging API.
- Tài khoản TikTok sở hữu quyền truy cập nâng cao (`has_advanced_access` là `true` khi gọi qua [/business/get/](01-accounts-p1.md#doc-1762228399168514)).
- Chủ tài khoản TikTok phải từ 18 tuổi trở lên.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập ngắn hạn được chủ tài khoản TikTok ủy quyền. Xem chi tiết tại [Authentication](../11-business-messaging-api/business-messaging-api.md#doc-1832184175482945). |
| Content-Type | string | Bắt buộc | Định dạng nội dung yêu cầu. Giá trị hợp lệ: `application/json`. |

### Tham số (POST JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| business_id | string | Bắt buộc | Mã định danh duy nhất của tài khoản TikTok (chính là giá trị `open_id` nhận được khi gọi OAuth2 token qua [/tt_user/oauth2/token/](../11-business-messaging-api/business-messaging-api.md#doc-1832184175482945)). |
| recipient_type | string | Điều kiện | Loại người nhận. Bắt buộc khi không dùng `direct_reply`. Hiện tại chỉ hỗ trợ giá trị `CONVERSATION`. |
| recipient | string | Điều kiện | Người nhận. Bắt buộc khi không dùng `direct_reply`. Khi `recipient_type` là `CONVERSATION`, truyền ID cuộc hội thoại (`conversation_id`) lấy từ [/business/message/conversation/list/](23-business-messaging.md#doc-1832184415059970). |
| message_type | string | Bắt buộc | Loại tin nhắn muốn gửi:<br>• `TEXT`: Tin nhắn văn bản.<br>• `IMAGE`: Tin nhắn hình ảnh.<br>• `SHARE_POST`: Tin nhắn chia sẻ bài đăng TikTok.<br>• `TEMPLATE`: Thẻ tin nhắn mẫu tương tác.<br>• `SENDER_ACTION`: Thao tác người gửi (trả về ID rỗng `""` vì không có nội dung tin nhắn thực sự). |
| text | object | Điều kiện | Thông tin tin nhắn văn bản (bắt buộc khi `message_type` là `TEXT`). |
| ↳ body | string | Điều kiện | Nội dung văn bản tin nhắn. Giới hạn: tối đa 6.000 ký tự (bao gồm khoảng trắng và emoji). |
| image | object | Điều kiện | Thông tin hình ảnh (bắt buộc khi `message_type` là `IMAGE`). |
| ↳ media_id | string | Điều kiện | ID hình ảnh nhận được sau khi tải ảnh lên qua endpoint [/business/message/media/upload/](23-business-messaging.md#doc-1832184437720193). |
| share_post | object | Điều kiện | Thông tin bài đăng chia sẻ (bắt buộc khi `message_type` là `SHARE_POST`). |
| ↳ item_id | string | Điều kiện | ID bài đăng TikTok muốn chia sẻ. Lấy ID bài đăng thuộc tài khoản qua [/business/video/list/](01-accounts-p1.md#doc-1762228421622786). Hiện tại chỉ có thể chia sẻ bài đăng của chính tài khoản. |
| template | object | Điều kiện | Chi tiết thẻ mẫu tin nhắn (bắt buộc khi `message_type` là `TEMPLATE`). |
| ↳ type | string | Điều kiện | Loại thẻ mẫu:<br>• `QA_BUTTON_CARD`: Thẻ hỏi đáp dạng nút bấm.<br>• `QA_LINK_CARD`: Thẻ hỏi đáp dạng liên kết chữ tương tác. |
| ↳ title | string | Điều kiện | Câu hỏi đặt trước trên thẻ. Tối đa 40 ký tự. |
| ↳ buttons | object[] | Điều kiện | Danh sách nút bấm hoặc liên kết câu trả lời (từ 1 đến 3 nút). |
| ↳↳ type | string | Điều kiện | Loại nút bấm: `REPLY`. Khi người dùng nhấp vào, nội dung sẽ được gửi như tin nhắn trả lời thay cho người dùng. |
| ↳↳ title | string | Điều kiện | Văn bản hiển thị trên nút (tối đa 20 ký tự cho nút bấm, 40 ký tự cho liên kết chữ). |
| ↳↳ id | string | Không bắt buộc | Mã định danh tự đặt cho nút (tối đa 40 ký tự). |
| sender_action | string | Điều kiện | Thao tác người gửi (khi `message_type` là `SENDER_ACTION`):<br>• `TYPING`: Hiển thị chỉ báo "Đang soạn tin nhắn..." trong 5 giây.<br>• `MARK_READ`: Đánh dấu đã đọc toàn bộ tin nhắn trong cuộc hội thoại. |
| referenced_message_info | object | Không bắt buộc | Thông tin tin nhắn gốc khi gửi tin nhắn dạng trả lời (quote reply). |
| ↳ referenced_message_id | string | Điều kiện | ID tin nhắn gốc cần trích dẫn trả lời (tin nhắn gốc có thể là văn bản, ảnh hoặc bài đăng). Khi dùng trường này, bắt buộc đặt `message_type` là `TEXT`. |
| direct_reply | object | Điều kiện | Chi tiết trả lời trực tiếp bình luận (Comment-to-Message). Áp dụng cho tài khoản đăng ký tại Việt Nam, Indonesia, Thái Lan. |
| ↳ reply_type | string | Điều kiện | Loại trả lời: `COMMENT_REPLY`. |
| ↳ comment_reply | object | Điều kiện | Chi tiết phản hồi bình luận. |
| ↳↳ comment_id | string | Điều kiện | ID bình luận có ý định mua hàng cao (high-intent comment) nhận từ webhook `im_receive_high_intent_comment`. |

### Ví dụ yêu cầu

#### Gửi tin nhắn văn bản (cURL)
```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/business/message/send/' --header 'Access-Token: YOUR_ACCESS_TOKEN' --header 'Content-Type: application/json' --data '{
    "business_id": "7123456789012345678",
    "recipient_type": "CONVERSATION",
    "recipient": "conv_123456789",
    "message_type": "TEXT",
    "text": {
        "body": "Xin chào! Cảm ơn bạn đã quan tâm đến sản phẩm của chúng tôi."
    }
}'
```

#### Python
```python
import os
import requests

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", "YOUR_ACCESS_TOKEN")
BUSINESS_ID = os.environ.get("BUSINESS_ID", "7123456789012345678")

url = "https://business-api.tiktok.com/open_api/v1.3/business/message/send/"
headers = {
    "Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json",
}
payload = {
    "business_id": BUSINESS_ID,
    "recipient_type": "CONVERSATION",
    "recipient": "conv_123456789",
    "message_type": "TEXT",
    "text": {
        "body": "Xin chào! Chúng tôi có thể hỗ trợ gì cho bạn hôm nay?",
    },
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())
```

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi từ hệ thống. |
| request_id | string | Mã nhật ký định danh yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ message | object | Thông tin tin nhắn vừa gửi. |
| ↳↳ message_id | string | ID định danh duy nhất của tin nhắn vừa gửi. |

### Ví dụ phản hồi

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202605210639490102360430824C1AE673",
  "data": {
    "message": {
      "message_id": "msg_9876543210123456"
    }
  }
}
```

---

## Lấy danh sách cuộc hội thoại (`Get a list of conversations`)
<a id="doc-1832184415059970"></a>
<!-- doc_id: 1832184415059970 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/business/message/conversation/list/`

**Mục đích**: Sử dụng endpoint này để lấy danh sách các cuộc hội thoại tin nhắn của tài khoản TikTok theo thứ tự cập nhật mới nhất.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền (access token). Xem chi tiết tại [Authentication](../11-business-messaging-api/business-messaging-api.md#doc-1832184175482945). |

### Tham số (GET query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| business_id | string | Bắt buộc | ID định danh của tài khoản TikTok (`open_id`). |
| conversation_type | string | Bắt buộc | Loại cuộc hội thoại muốn lấy. Giá trị enum: `ALL` (toàn bộ cuộc hội thoại), `PRIMARY` (hộp thư chính). |
| limit | integer | Không bắt buộc | Số cuộc hội thoại trên mỗi trang. Giá trị mặc định: 20. Khoảng giá trị: 1-100. |
| cursor | integer | Không bắt buộc | Con trỏ phân trang (mốc thời gian tính bằng microgiây của cuộc hội thoại cuối cùng ở trang trước). |

### Ví dụ

#### cURL
```bash
curl --get -H "Access-Token: YOUR_ACCESS_TOKEN" --data-urlencode "business_id=7123456789012345678" --data-urlencode "conversation_type=PRIMARY" --data-urlencode "limit=20" https://business-api.tiktok.com/open_api/v1.3/business/message/conversation/list/
```

#### Python
```python
import os
import requests

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", "YOUR_ACCESS_TOKEN")
BUSINESS_ID = os.environ.get("BUSINESS_ID", "7123456789012345678")

url = "https://business-api.tiktok.com/open_api/v1.3/business/message/conversation/list/"
headers = {
    "Access-Token": ACCESS_TOKEN,
}
params = {
    "business_id": BUSINESS_ID,
    "conversation_type": "PRIMARY",
    "limit": 20,
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. |
| request_id | string | Mã nhật ký định danh yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ conversations | object[] | Danh sách các cuộc hội thoại. |
| ↳↳ conversation_id | string | ID cuộc hội thoại. |
| ↳↳ update_time | integer | Thời gian cập nhật gần nhất của cuộc hội thoại (mốc thời gian Unix timestamp tính bằng giây). |
| ↳↳ referral | object | Nguồn dẫn người dùng đến cuộc hội thoại (ví dụ: từ quảng cáo hoặc bình luận). |
| ↳ has_more | boolean | Cho biết còn dữ liệu ở các trang tiếp theo hay không. |
| ↳ cursor | integer | Con trỏ để lấy trang tiếp theo. |

### Ví dụ phản hồi

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202605210639490102360430824C1AE673",
  "data": {
    "conversations": [
      {
        "conversation_id": "conv_123456789",
        "update_time": 1716500000,
        "referral": {}
      }
    ],
    "has_more": false,
    "cursor": 0
  }
}
```

---

## Lấy danh sách tin nhắn (`Get a list of messages`)
<a id="doc-1832184425841170"></a>
<!-- doc_id: 1832184425841170 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/business/message/content/list/`

**Mục đích**: Sử dụng endpoint này để lấy lịch sử tin nhắn chi tiết bên trong một cuộc hội thoại cụ thể, bao gồm văn bản, hình ảnh, bài đăng chia sẻ, nhãn dán, biểu tượng cảm xúc, phản ứng (reactions) và thông tin người tham gia.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền (access token). Xem chi tiết tại [Authentication](../11-business-messaging-api/business-messaging-api.md#doc-1832184175482945). |

### Tham số (GET query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| business_id | string | Bắt buộc | ID tài khoản TikTok (`open_id`). |
| conversation_id | string | Bắt buộc | ID cuộc hội thoại cần lấy danh sách tin nhắn. |

### Ví dụ

#### cURL
```bash
curl --get -H "Access-Token: YOUR_ACCESS_TOKEN" --data-urlencode "business_id=7123456789012345678" --data-urlencode "conversation_id=conv_123456789" https://business-api.tiktok.com/open_api/v1.3/business/message/content/list/
```

#### Python
```python
import os
import requests

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", "YOUR_ACCESS_TOKEN")
BUSINESS_ID = os.environ.get("BUSINESS_ID", "7123456789012345678")

url = "https://business-api.tiktok.com/open_api/v1.3/business/message/content/list/"
headers = {
    "Access-Token": ACCESS_TOKEN,
}
params = {
    "business_id": BUSINESS_ID,
    "conversation_id": "conv_123456789",
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. |
| request_id | string | Mã nhật ký định danh yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ messages | object[] | Danh sách các tin nhắn trong cuộc hội thoại. |
| ↳↳ message_id | string | ID tin nhắn. |
| ↳↳ conversation_id | string | ID cuộc hội thoại chứa tin nhắn. |
| ↳↳ sender | string | ID người gửi tin nhắn. |
| ↳↳ recipient | string | ID người nhận tin nhắn. |
| ↳↳ timestamp | integer | Mốc thời gian gửi tin nhắn (giây). |
| ↳↳ message_type | string | Loại tin nhắn: `TEXT`, `IMAGE`, `SHARE_POST`, `STICKER`, `EMOJI`, `VIDEO`, `TEMPLATE`. |
| ↳↳ auto_message_type | string | Loại tin nhắn tự động (nếu là tin nhắn tự động gửi). |
| ↳↳ text | object | Nội dung tin nhắn văn bản. |
| ↳↳ image | object | Thông tin hình ảnh đính kèm. |
| ↳↳ share_post | object | Thông tin bài đăng TikTok được chia sẻ. |
| ↳↳ reactions | object[] | Các phản ứng (thích, thả tim) đối với tin nhắn. |
| ↳↳ sticker | object | Thông tin nhãn dán sticker. |
| ↳↳ emoji | object | Thông tin biểu tượng cảm xúc. |
| ↳↳ video | object | Thông tin video đính kèm. |
| ↳↳ template | object | Chi tiết thẻ mẫu tin nhắn. |
| ↳↳ from_user | object | Thông tin người gửi. |
| ↳↳ to_user | object | Thông tin người nhận. |
| ↳↳ referenced_message_info | object | Thông tin tin nhắn gốc được trích dẫn trả lời. |
| ↳↳ message_tag | object | Nhãn phân loại tin nhắn. |
| ↳ participants | object[] | Danh sách thông tin các thành viên tham gia cuộc hội thoại. |
| ↳↳ id | string | ID thành viên. |
| ↳↳ role | string | Vai trò: `BUSINESS` (doanh nghiệp) hoặc `USER` (người dùng). |
| ↳↳ display_name | string | Tên hiển thị của thành viên. |
| ↳↳ profile_image | string | URL ảnh đại diện của thành viên. |
| ↳↳ is_follower | boolean | Cho biết người dùng có đang theo dõi tài khoản TikTok hay không. |

---

## Tải lên hình ảnh (`Upload an image`)
<a id="doc-1832184437720193"></a>
<!-- doc_id: 1832184437720193 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/business/message/media/upload/`

**Mục đích**: Sử dụng endpoint này để tải lên tệp hình ảnh trước khi gửi ảnh qua tin nhắn trực tiếp. API sẽ trả về `media_id` dùng để truyền vào tham số `image.media_id` khi gọi endpoint gửi tin nhắn.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền (access token). Xem chi tiết tại [Authentication](../11-business-messaging-api/business-messaging-api.md#doc-1832184175482945). |
| Content-Type | string | Bắt buộc | Định dạng nội dung: `multipart/form-data`. |

### Tham số (POST form-data)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| business_id | string | Bắt buộc | ID định danh của tài khoản TikTok (`open_id`). |
| file | file | Bắt buộc | Tệp hình ảnh nhị phân cần tải lên (hỗ trợ JPG, PNG, WEBP). |
| media_type | string | Bắt buộc | Loại phương tiện truyền thông. Giá trị: `IMAGE`. |

### Ví dụ

```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/business/message/media/upload/' --header 'Access-Token: YOUR_ACCESS_TOKEN' --form 'business_id="7123456789012345678"' --form 'media_type="IMAGE"' --form 'file=@"/path/to/product_image.png"'
```

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. |
| request_id | string | Mã nhật ký định danh yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ media_id | string | ID của hình ảnh vừa tải lên thành công, dùng để gửi tin nhắn ảnh. |

---

## Tải về hình ảnh hoặc video từ tin nhắn (`Download an image or a video from a message`)
<a id="doc-1832184455450626"></a>
<!-- doc_id: 1832184455450626 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/business/message/media/download/`

**Mục đích**: Sử dụng endpoint này để lấy đường dẫn tải về (download URL) có chữ ký an toàn của hình ảnh hoặc video đính kèm trong tin nhắn trực tiếp.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền (access token). Xem chi tiết tại [Authentication](../11-business-messaging-api/business-messaging-api.md#doc-1832184175482945). |
| Content-Type | string | Bắt buộc | Định dạng nội dung: `application/json`. |

### Tham số (POST JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| business_id | string | Bắt buộc | ID tài khoản TikTok (`open_id`). |
| conversation_id | string | Bắt buộc | ID cuộc hội thoại chứa tệp phương tiện. |
| message_id | string | Bắt buộc | ID tin nhắn chứa tệp phương tiện. |
| media_id | string | Bắt buộc | ID tệp phương tiện cần tải về. |
| media_type | string | Bắt buộc | Loại tệp phương tiện: `IMAGE` (hình ảnh), `VIDEO` (video). |

### Ví dụ

```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/business/message/media/download/' --header 'Access-Token: YOUR_ACCESS_TOKEN' --header 'Content-Type: application/json' --data '{
    "business_id": "7123456789012345678",
    "conversation_id": "conv_123456789",
    "message_id": "msg_987654321",
    "media_id": "media_555666777",
    "media_type": "IMAGE"
}'
```

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. |
| request_id | string | Mã nhật ký định danh yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ download_url | string | URL tạm thời có chữ ký để tải về tệp hình ảnh hoặc video. |
---

## Kiểm tra khả năng gửi tin nhắn của tài khoản TikTok (`Check the capability of a TikTok account`)
<a id="doc-1836061597865986"></a>
<!-- doc_id: 1836061597865986 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/business/message/capabilities/get/`

**Mục đích**: Sử dụng endpoint này để kiểm tra xem tài khoản TikTok có khả năng gửi tệp đính kèm đa phương tiện (như hình ảnh) đến người dùng trong cuộc hội thoại hay không (do tính khả dụng của tính năng này phụ thuộc vào vị trí địa lý của cả người gửi và người nhận).

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền (access token). Xem chi tiết tại [Authentication](../11-business-messaging-api/business-messaging-api.md#doc-1832184175482945). |

### Tham số (GET query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| business_id | string | Bắt buộc | ID định danh của tài khoản TikTok (`open_id`). |
| capability_types | string[] | Bắt buộc | Danh sách các khả năng cần kiểm tra (chuỗi JSON mảng). Giá trị hỗ trợ: `["CAN_SEND_IMAGE"]`. |
| conversation_id | string | Điều kiện | ID cuộc hội thoại cụ thể muốn kiểm tra. |
| conversation_type | string | Điều kiện | Loại cuộc hội thoại. |

### Ví dụ

#### cURL
```bash
curl --get -H "Access-Token: YOUR_ACCESS_TOKEN" --data-urlencode "business_id=7123456789012345678" --data-urlencode 'capability_types=["CAN_SEND_IMAGE"]' --data-urlencode "conversation_id=conv_123456789" https://business-api.tiktok.com/open_api/v1.3/business/message/capabilities/get/
```

#### Python
```python
import json
import os
import requests

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", "YOUR_ACCESS_TOKEN")
BUSINESS_ID = os.environ.get("BUSINESS_ID", "7123456789012345678")

url = "https://business-api.tiktok.com/open_api/v1.3/business/message/capabilities/get/"
headers = {
    "Access-Token": ACCESS_TOKEN,
}
params = {
    "business_id": BUSINESS_ID,
    "capability_types": json.dumps(["CAN_SEND_IMAGE"]),
    "conversation_id": "conv_123456789",
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. |
| request_id | string | Mã nhật ký định danh yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ capability_infos | object[] | Danh sách kết quả kiểm tra khả năng nhắn tin. |
| ↳↳ capability_type | string | Loại khả năng: `CAN_SEND_IMAGE`. |
| ↳↳ capability_result | boolean | Kết quả: `true` (có thể gửi), `false` (không thể gửi). |

---

## Bật/tắt tính năng Chuyển bình luận thành tin nhắn (`Enable or disable Comment-to-Message for a TikTok account`)
<a id="doc-1843697551083522"></a>
<!-- doc_id: 1843697551083522 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/business/message/direct_reply/update/`

**Mục đích**: Sử dụng endpoint này để bật (`ENABLE`) hoặc tắt (`DISABLE`) tính năng Chuyển bình luận thành tin nhắn trực tiếp (Comment-to-Message) cho tài khoản TikTok. Tính năng này cho phép tài khoản nhắn tin riêng phản hồi lại các bình luận thể hiện ý định mua hàng cao trên video TikTok.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền (access token). Xem chi tiết tại [Authentication](../11-business-messaging-api/business-messaging-api.md#doc-1832184175482945). |
| Content-Type | string | Bắt buộc | Định dạng nội dung yêu cầu. Giá trị: `application/json`. |

### Tham số (POST JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| business_id | string | Bắt buộc | ID tài khoản TikTok (`open_id`). |
| direct_reply_type | string | Bắt buộc | Loại phản hồi trực tiếp. Giá trị: `COMMENT_REPLY`. |
| operation_status | string | Bắt buộc | Trạng thái thao tác muốn cập nhật: `ENABLE` (bật tính năng), `DISABLE` (tắt tính năng). |

### Ví dụ

```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/business/message/direct_reply/update/' --header 'Access-Token: YOUR_ACCESS_TOKEN' --header 'Content-Type: application/json' --data '{
    "business_id": "7123456789012345678",
    "direct_reply_type": "COMMENT_REPLY",
    "operation_status": "ENABLE"
}'
```

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. |
| request_id | string | Mã nhật ký định danh yêu cầu. |
| data | object | Dữ liệu trả về (đối tượng rỗng khi thành công). |

---

## Lấy cài đặt Chuyển bình luận thành tin nhắn (`Get the Comment-to-Message setting of a TikTok account`)
<a id="doc-1843697576682497"></a>
<!-- doc_id: 1843697576682497 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/business/message/direct_reply/get/`

**Mục đích**: Sử dụng endpoint này để kiểm tra trạng thái kích hoạt hiện tại của tính năng Chuyển bình luận thành tin nhắn trực tiếp đối với một tài khoản TikTok.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền (access token). Xem chi tiết tại [Authentication](../11-business-messaging-api/business-messaging-api.md#doc-1832184175482945). |

### Tham số (GET query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| business_id | string | Bắt buộc | ID định danh của tài khoản TikTok (`open_id`). |
| direct_reply_type | string | Bắt buộc | Loại phản hồi trực tiếp cần tra cứu: `COMMENT_REPLY`. |

### Ví dụ

#### cURL
```bash
curl --get -H "Access-Token: YOUR_ACCESS_TOKEN" --data-urlencode "business_id=7123456789012345678" --data-urlencode "direct_reply_type=COMMENT_REPLY" https://business-api.tiktok.com/open_api/v1.3/business/message/direct_reply/get/
```

#### Python
```python
import os
import requests

ACCESS_TOKEN = os.environ.get("ACCESS_TOKEN", "YOUR_ACCESS_TOKEN")
BUSINESS_ID = os.environ.get("BUSINESS_ID", "7123456789012345678")

url = "https://business-api.tiktok.com/open_api/v1.3/business/message/direct_reply/get/"
headers = {
    "Access-Token": ACCESS_TOKEN,
}
params = {
    "business_id": BUSINESS_ID,
    "direct_reply_type": "COMMENT_REPLY",
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. |
| request_id | string | Mã nhật ký định danh yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ direct_reply_type | string | Loại phản hồi trực tiếp: `COMMENT_REPLY`. |
| ↳ operation_status | string | Trạng thái hiện tại: `ENABLE` (đang bật), `DISABLE` (đang tắt). |

---

## Webhooks
<a id="doc-1832184379532289"></a>
<!-- doc_id: 1832184379532289 -->

Nhóm API Webhooks cho phép nhà phát triển đăng ký URL callback để nhận các sự kiện tin nhắn thời gian thực từ TikTok, bao gồm khi nhận tin nhắn mới từ khách hàng, khi người dùng đọc tin nhắn, khi có phản ứng/tương tác, hoặc khi phát hiện bình luận có ý định mua hàng cao.

Các endpoint trong nhóm Webhook:
* [Tạo hoặc cập nhật cấu hình Webhook](23-business-messaging.md#doc-1832184470423554)
* [Lấy danh sách cấu hình Webhook](23-business-messaging.md#doc-1832184488625234)
* [Xóa cấu hình Webhook](23-business-messaging.md#doc-1832184497985537)

---

## Tạo hoặc cập nhật cấu hình Webhook (`Create a Business Messaging Webhook configuration`)
<a id="doc-1832184470423554"></a>
<!-- doc_id: 1832184470423554 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/business/webhook/update/`

**Mục đích**: Sử dụng endpoint này để đăng ký hoặc cập nhật URL callback của ứng dụng để nhận các sự kiện tin nhắn doanh nghiệp tương ứng.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Content-Type | string | Bắt buộc | Định dạng nội dung yêu cầu. Giá trị: `application/json`. |

### Tham số (POST JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| app_id | string | Bắt buộc | App ID của ứng dụng nhà phát triển, lấy tại trang [Application Management](https://ads.tiktok.com/marketing_api/apps/). |
| secret | string | Bắt buộc | Khóa bí mật (App Secret) của ứng dụng nhà phát triển. |
| event_type | string | Bắt buộc | Loại sự kiện webhook muốn đăng ký:<br>• `IM_RECEIVE`: Nhận tin nhắn từ người dùng.<br>• `IM_SEND`: Tin nhắn được gửi đi.<br>• `IM_READ`: Tin nhắn được đọc.<br>• `IM_MESSAGE_ACTION`: Hành động tương tác tin nhắn.<br>• `IM_HIGH_INTENT_COMMENT`: Phát hiện bình luận có ý định mua hàng cao. |
| callback_url | string | Bắt buộc | Địa chỉ URL an toàn (HTTPS) của máy chủ nhận thông báo webhook. |

### Ví dụ

```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/business/webhook/update/' --header 'Content-Type: application/json' --data '{
    "app_id": "YOUR_APP_ID",
    "secret": "YOUR_APP_SECRET",
    "event_type": "IM_RECEIVE",
    "callback_url": "https://api.yourdomain.com/tiktok/webhook"
}'
```

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. |
| request_id | string | Mã nhật ký định danh yêu cầu. |
| data | object | Dữ liệu trả về (chứa `app_id`, `event_type`, `callback_url`). |

---

## Lấy cấu hình Webhook (`Get a Business Messaging Webhook configuration`)
<a id="doc-1832184488625234"></a>
<!-- doc_id: 1832184488625234 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/business/webhook/list/`

**Mục đích**: Sử dụng endpoint này để truy vấn danh sách các webhook đã đăng ký cho ứng dụng của bạn.

### Tham số (GET query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| app_id | string | Bắt buộc | App ID của ứng dụng nhà phát triển. |
| secret | string | Bắt buộc | Khóa bí mật (App Secret) của ứng dụng nhà phát triển. |
| event_type | string | Bắt buộc | Loại sự kiện webhook muốn tra cứu (ví dụ: `IM_RECEIVE`). |

### Ví dụ

#### cURL
```bash
curl --get --data-urlencode "app_id=YOUR_APP_ID" --data-urlencode "secret=YOUR_APP_SECRET" --data-urlencode "event_type=IM_RECEIVE" https://business-api.tiktok.com/open_api/v1.3/business/webhook/list/
```

#### Python
```python
import os
import requests

APP_ID = os.environ.get("APP_ID", "YOUR_APP_ID")
APP_SECRET = os.environ.get("APP_SECRET", "YOUR_APP_SECRET")

url = "https://business-api.tiktok.com/open_api/v1.3/business/webhook/list/"
params = {
    "app_id": APP_ID,
    "secret": APP_SECRET,
    "event_type": "IM_RECEIVE",
}

response = requests.get(url, params=params)
print(response.json())
```

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. |
| request_id | string | Mã nhật ký định danh yêu cầu. |
| data | object | Dữ liệu trả về chứa danh sách cấu hình webhook đã đăng ký. |

---

## Xóa cấu hình Webhook (`Delete a Business Messaging Webhook configuration`)
<a id="doc-1832184497985537"></a>
<!-- doc_id: 1832184497985537 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/business/webhook/delete/`

**Mục đích**: Sử dụng endpoint này để hủy đăng ký và xóa URL callback webhook cho một loại sự kiện nhất định.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Content-Type | string | Bắt buộc | Định dạng nội dung yêu cầu: `application/json`. |

### Tham số (POST JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| app_id | string | Bắt buộc | App ID của ứng dụng nhà phát triển. |
| secret | string | Bắt buộc | Khóa bí mật (App Secret) của ứng dụng nhà phát triển. |
| event_type | string | Bắt buộc | Loại sự kiện webhook cần xóa (ví dụ: `IM_RECEIVE`). |

### Ví dụ

```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/business/webhook/delete/' --header 'Content-Type: application/json' --data '{
    "app_id": "YOUR_APP_ID",
    "secret": "YOUR_APP_SECRET",
    "event_type": "IM_RECEIVE"
}'
```

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. |
| request_id | string | Mã nhật ký định danh yêu cầu. |
| data | object | Dữ liệu trả về (đối tượng rỗng khi thành công). |
---

## Tin nhắn tự động (`Automatic messages`)
<a id="doc-1832184391220417"></a>
<!-- doc_id: 1832184391220417 -->

Tính năng Tin nhắn tự động (Automatic messages) cho phép tài khoản TikTok tự động phản hồi khách hàng thông qua các hình thức:
* **Tin nhắn chào mừng (Welcome message)**: Tự động gửi lời chào khi người dùng bắt đầu mở cuộc hội thoại.
* **Câu hỏi gợi ý (Suggested questions)**: Hiển thị danh sách các câu hỏi thường gặp kèm câu trả lời tự động để khách hàng chọn.
* **Gợi ý trò chuyện (Chat prompts)**: Hiển thị các chủ đề gợi ý trò chuyện.
* **Chào mừng người theo dõi mới (Follow welcome)**: Tin nhắn gửi đến người dùng mới theo dõi tài khoản.

Nhóm API này bao gồm các endpoint sau:
* [Tạo tin nhắn tự động](23-business-messaging.md#doc-1832184584869890)
* [Cập nhật tin nhắn tự động](23-business-messaging.md#doc-1832184596566017)
* [Bật/tắt tin nhắn tự động](23-business-messaging.md#doc-1832184607786242)
* [Lấy danh sách tin nhắn tự động](23-business-messaging.md#doc-1832184619749377)
* [Xóa tin nhắn tự động](23-business-messaging.md#doc-1832184630106386)
* [Sắp xếp thứ tự tin nhắn tự động](23-business-messaging.md#doc-1832184641212433)

---

## Tạo tin nhắn tự động (`Create an automatic message for a TikTok account`)
<a id="doc-1832184584869890"></a>
<!-- doc_id: 1832184584869890 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/business/message/auto_message/create/`

**Mục đích**: Sử dụng endpoint này để tạo cấu hình tin nhắn tự động mới cho tài khoản TikTok (chẳng hạn như tin nhắn chào mừng hoặc các câu hỏi thường gặp).

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền (access token). Xem chi tiết tại [Authentication](../11-business-messaging-api/business-messaging-api.md#doc-1832184175482945). |
| Content-Type | string | Bắt buộc | Định dạng nội dung yêu cầu. Giá trị: `application/json`. |

### Tham số (POST JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| business_id | string | Bắt buộc | ID tài khoản TikTok (`open_id`). |
| auto_message_type | string | Bắt buộc | Loại tin nhắn tự động: `WELCOME_MESSAGE`, `SUGGESTED_QUESTION`, `CHAT_PROMPT`, `FOLLOW_WELCOME`. |
| welcome_message | object | Điều kiện | Cấu hình tin nhắn chào mừng (khi `auto_message_type` là `WELCOME_MESSAGE`). |
| ↳ content | string | Điều kiện | Nội dung lời chào mừng hiển thị cho người dùng. |
| suggested_question | object | Điều kiện | Cấu hình câu hỏi gợi ý (khi `auto_message_type` là `SUGGESTED_QUESTION`). |
| ↳ question | string | Điều kiện | Nội dung câu hỏi thường gặp gợi ý cho người dùng bấm chọn. |
| ↳ answer | string | Điều kiện | Câu trả lời tự động tương ứng khi người dùng bấm vào câu hỏi. |
| chat_prompt | object | Điều kiện | Cấu hình gợi ý bắt đầu trò chuyện (khi `auto_message_type` là `CHAT_PROMPT`). |
| ↳ title | string | Điều kiện | Tiêu đề gợi ý trò chuyện. |
| ↳ content | string | Điều kiện | Nội dung chi tiết của gợi ý trò chuyện. |
| follow_welcome | object | Điều kiện | Cấu hình tin nhắn gửi cho người theo dõi mới (khi `auto_message_type` là `FOLLOW_WELCOME`). |
| ↳ message | string | Điều kiện | Lời nhắn gửi đến người theo dõi mới. |
| ↳ interaction | string | Không bắt buộc | Hình thức tương tác. |
| ↳ quick_reply_text | string | Không bắt buộc | Văn bản câu trả lời nhanh. |
| ↳ quick_action_type | string | Không bắt buộc | Loại hành động nhanh. |

### Ví dụ

```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/business/message/auto_message/create/' --header 'Access-Token: YOUR_ACCESS_TOKEN' --header 'Content-Type: application/json' --data '{
    "business_id": "7123456789012345678",
    "auto_message_type": "WELCOME_MESSAGE",
    "welcome_message": {
        "content": "Xin chào! Cảm ơn bạn đã nhắn tin cho chúng tôi. Chúng tôi sẽ phản hồi trong giây lát!"
    }
}'
```

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. |
| request_id | string | Mã nhật ký định danh yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ auto_message | object | Đối tượng tin nhắn tự động vừa tạo. |
| ↳↳ auto_message_id | string | ID của tin nhắn tự động vừa tạo. |

---

## Cập nhật tin nhắn tự động (`Update the automatic message for a TikTok account`)
<a id="doc-1832184596566017"></a>
<!-- doc_id: 1832184596566017 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/business/message/auto_message/update/`

**Mục đích**: Sử dụng endpoint này để chỉnh sửa nội dung của một tin nhắn tự động đã tồn tại.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền (access token). Xem chi tiết tại [Authentication](../11-business-messaging-api/business-messaging-api.md#doc-1832184175482945). |
| Content-Type | string | Bắt buộc | Định dạng nội dung yêu cầu. Giá trị: `application/json`. |

### Tham số (POST JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| business_id | string | Bắt buộc | ID tài khoản TikTok (`open_id`). |
| auto_message_id | string | Bắt buộc | ID tin nhắn tự động cần chỉnh sửa. |
| auto_message_type | string | Bắt buộc | Loại tin nhắn tự động: `WELCOME_MESSAGE`, `SUGGESTED_QUESTION`, `CHAT_PROMPT`, `FOLLOW_WELCOME`. |
| welcome_message | object | Điều kiện | Nội dung tin nhắn chào mừng mới. |
| ↳ content | string | Điều kiện | Văn bản chào mừng mới. |
| suggested_question | object | Điều kiện | Cấu hình câu hỏi gợi ý mới. |
| ↳ question | string | Điều kiện | Câu hỏi mới. |
| ↳ answer | string | Điều kiện | Câu trả lời mới. |
| chat_prompt | object | Điều kiện | Cấu hình gợi ý chat mới. |
| ↳ title | string | Điều kiện | Tiêu đề mới. |
| ↳ content | string | Điều kiện | Nội dung mới. |
| follow_welcome | object | Điều kiện | Cấu hình chào mừng người theo dõi mới. |
| ↳ message | string | Điều kiện | Nội dung tin nhắn mới. |
| ↳ interaction | string | Không bắt buộc | Hình thức tương tác mới. |
| ↳ quick_reply_text | string | Không bắt buộc | Văn bản trả lời nhanh. |
| ↳ quick_action_type | string | Không bắt buộc | Loại hành động nhanh. |

### Ví dụ

```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/business/message/auto_message/update/' --header 'Access-Token: YOUR_ACCESS_TOKEN' --header 'Content-Type: application/json' --data '{
    "business_id": "7123456789012345678",
    "auto_message_id": "auto_msg_123456789",
    "auto_message_type": "WELCOME_MESSAGE",
    "welcome_message": {
        "content": "Chào mừng bạn đã quay lại với chúng tôi!"
    }
}'
```

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. |
| request_id | string | Mã nhật ký định danh yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ auto_message | object | Thông tin tin nhắn tự động sau khi cập nhật. |
| ↳↳ auto_message_id | string | ID tin nhắn tự động. |

---

## Bật/tắt tin nhắn tự động (`Turn on or turn off an automatic message for a TikTok account`)
<a id="doc-1832184607786242"></a>
<!-- doc_id: 1832184607786242 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/business/message/auto_message/status/update/`

**Mục đích**: Sử dụng endpoint này để bật hoặc tắt hoạt động của một loại tin nhắn tự động cụ thể cho tài khoản TikTok.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền (access token). Xem chi tiết tại [Authentication](../11-business-messaging-api/business-messaging-api.md#doc-1832184175482945). |
| Content-Type | string | Bắt buộc | Định dạng nội dung yêu cầu. Giá trị: `application/json`. |

### Tham số (POST JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| business_id | string | Bắt buộc | ID tài khoản TikTok (`open_id`). |
| auto_message_type | string | Bắt buộc | Loại tin nhắn tự động: `WELCOME_MESSAGE`, `SUGGESTED_QUESTION`, `CHAT_PROMPT`, `FOLLOW_WELCOME`. |
| operation_status | string | Bắt buộc | Trạng thái hoạt động: `ENABLE` (bật), `DISABLE` (tắt). |

### Ví dụ

```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/business/message/auto_message/status/update/' --header 'Access-Token: YOUR_ACCESS_TOKEN' --header 'Content-Type: application/json' --data '{
    "business_id": "7123456789012345678",
    "auto_message_type": "WELCOME_MESSAGE",
    "operation_status": "ENABLE"
}'
```

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. |
| request_id | string | Mã nhật ký định danh yêu cầu. |
| data | object | Dữ liệu trả về (đối tượng rỗng khi thành công). |

---

## Lấy danh sách tin nhắn tự động (`Get the automatic messages for a TikTok account`)
<a id="doc-1832184619749377"></a>
<!-- doc_id: 1832184619749377 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/business/message/auto_message/get/`

**Mục đích**: Sử dụng endpoint này để lấy danh sách các tin nhắn tự động đang được cấu hình trên tài khoản TikTok, kèm theo trạng thái xét duyệt và nội dung chi tiết.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền (access token). Xem chi tiết tại [Authentication](../11-business-messaging-api/business-messaging-api.md#doc-1832184175482945). |
| Content-Type | string | Bắt buộc | Định dạng nội dung yêu cầu. Giá trị: `application/json`. |

### Tham số (POST JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| business_id | string | Bắt buộc | ID tài khoản TikTok (`open_id`). |
| auto_message_type | string | Bắt buộc | Loại tin nhắn tự động muốn lấy: `WELCOME_MESSAGE`, `SUGGESTED_QUESTION`, `CHAT_PROMPT`, `FOLLOW_WELCOME`. |
| auto_message_id | string | Không bắt buộc | ID tin nhắn tự động cụ thể (nếu muốn lấy chi tiết một tin nhắn). |

### Ví dụ

```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/business/message/auto_message/get/' --header 'Access-Token: YOUR_ACCESS_TOKEN' --header 'Content-Type: application/json' --data '{
    "business_id": "7123456789012345678",
    "auto_message_type": "WELCOME_MESSAGE"
}'
```

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. |
| request_id | string | Mã nhật ký định danh yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ business_id | string | ID tài khoản TikTok. |
| ↳ operation_status | string | Trạng thái bật/tắt của loại tin nhắn tự động này (`ENABLE` hoặc `DISABLE`). |
| ↳ auto_messages | object[] | Danh sách các cấu hình tin nhắn tự động. |
| ↳↳ auto_message_id | string | ID tin nhắn tự động. |
| ↳↳ auto_message_type | string | Loại tin nhắn tự động. |
| ↳↳ audit_status | string | Trạng thái xét duyệt: `AUDITING` (đang duyệt), `APPROVED` (đã duyệt), `REJECTED` (bị từ chối). |
| ↳↳ welcome_message | object | Chi tiết tin nhắn chào mừng. |
| ↳↳ suggested_question | object | Chi tiết câu hỏi gợi ý. |
| ↳↳ chat_prompt | object | Chi tiết gợi ý trò chuyện. |
| ↳↳ follow_welcome | object | Chi tiết chào mừng người theo dõi. |

---

## Xóa tin nhắn tự động (`Delete the automatic message for a TikTok account`)
<a id="doc-1832184630106386"></a>
<!-- doc_id: 1832184630106386 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/business/message/auto_message/delete/`

**Mục đích**: Sử dụng endpoint này để xóa một cấu hình tin nhắn tự động đã thiết lập trước đó khỏi tài khoản TikTok.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền (access token). Xem chi tiết tại [Authentication](../11-business-messaging-api/business-messaging-api.md#doc-1832184175482945). |
| Content-Type | string | Bắt buộc | Định dạng nội dung yêu cầu. Giá trị: `application/json`. |

### Tham số (POST JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| business_id | string | Bắt buộc | ID tài khoản TikTok (`open_id`). |
| auto_message_type | string | Bắt buộc | Loại tin nhắn tự động: `WELCOME_MESSAGE`, `SUGGESTED_QUESTION`, `CHAT_PROMPT`, `FOLLOW_WELCOME`. |
| auto_message_id | string | Bắt buộc | ID của tin nhắn tự động cần xóa. |

### Ví dụ

```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/business/message/auto_message/delete/' --header 'Access-Token: YOUR_ACCESS_TOKEN' --header 'Content-Type: application/json' --data '{
    "business_id": "7123456789012345678",
    "auto_message_type": "WELCOME_MESSAGE",
    "auto_message_id": "auto_msg_123456789"
}'
```

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. |
| request_id | string | Mã nhật ký định danh yêu cầu. |
| data | object | Dữ liệu trả về (đối tượng rỗng khi thành công). |

---

## Sắp xếp thứ tự tin nhắn tự động (`Sort the automatic message for a TikTok account`)
<a id="doc-1832184641212433"></a>
<!-- doc_id: 1832184641212433 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/business/message/auto_message/sort/`

**Mục đích**: Sử dụng endpoint này để sắp xếp lại thứ tự hiển thị của các câu hỏi gợi ý (`SUGGESTED_QUESTION`) hoặc gợi ý trò chuyện trong giao diện tin nhắn của người dùng.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Mã truy cập được ủy quyền (access token). Xem chi tiết tại [Authentication](../11-business-messaging-api/business-messaging-api.md#doc-1832184175482945). |
| Content-Type | string | Bắt buộc | Định dạng nội dung yêu cầu. Giá trị: `application/json`. |

### Tham số (POST JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| business_id | string | Bắt buộc | ID tài khoản TikTok (`open_id`). |
| auto_message_type | string | Bắt buộc | Loại tin nhắn tự động cần sắp xếp: `SUGGESTED_QUESTION`, `CHAT_PROMPT`. |
| auto_message_ids | string[] | Bắt buộc | Danh sách ID các tin nhắn tự động theo đúng thứ tự hiển thị mong muốn (từ trên xuống dưới). |

### Ví dụ

```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/business/message/auto_message/sort/' --header 'Access-Token: YOUR_ACCESS_TOKEN' --header 'Content-Type: application/json' --data '{
    "business_id": "7123456789012345678",
    "auto_message_type": "SUGGESTED_QUESTION",
    "auto_message_ids": [
        "auto_msg_001",
        "auto_msg_002",
        "auto_msg_003"
    ]
}'
```

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| code | number | Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. |
| request_id | string | Mã nhật ký định danh yêu cầu. |
| data | object | Dữ liệu trả về (đối tượng rỗng khi thành công). |

### Ví dụ phản hồi

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202605210639490102360430824C1AE673",
  "data": {}
}
```
