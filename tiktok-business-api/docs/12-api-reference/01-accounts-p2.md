# Tài khoản TikTok (Accounts) — phần 2/2

Tài liệu này hướng dẫn chi tiết các API thuộc nhóm Quản lý tài khoản TikTok (Accounts) — phần 2, bao gồm các chức năng nâng cao phục vụ vận hành và tích hợp tài khoản: gợi ý hashtag và tìm kiếm thẻ vị trí khi xuất bản bài viết; quản lý ủy quyền bài viết TikTok làm quảng cáo Spark Ads (Ad authorization); thêm và xác minh quyền sở hữu thuộc tính URL (URL properties); cùng với hệ thống Webhook ở cấp độ ứng dụng nhà phát triển để nhận thông báo sự kiện theo thời gian thực.

| Endpoint | Method | Đường dẫn | Mục đích |
|---|---|---|---|
| Gợi ý hashtag cho tài khoản TikTok | `GET` | `/open_api/v1.3/business/hashtag/suggestion/` | Gợi ý danh sách hashtag phù hợp dựa trên từ khóa |
| Lấy danh sách thẻ vị trí | `GET` | `/open_api/v1.3/business/publish/location/` | Tìm kiếm thẻ vị trí để gắn vào bài đăng video hoặc ảnh |
| Tổng quan ủy quyền quảng cáo bài viết | - | - | Giới thiệu luồng ủy quyền bài viết làm quảng cáo Spark Ads |
| Bật/tắt ủy quyền quảng cáo | `POST` | `/open_api/v1.3/business/post/authorize/setting/` | Bật hoặc tắt cài đặt ủy quyền quảng cáo cho bài viết TikTok |
| Gia hạn hiệu lực ủy quyền bài viết | `POST` | `/open_api/v1.3/business/post/authorize/` | Gia hạn thời gian ủy quyền hoặc tạo mã ủy quyền mới |
| Lấy trạng thái ủy quyền bài viết | `GET` | `/open_api/v1.3/business/post/authorize/status/` | Tra cứu trạng thái và thông tin mã ủy quyền của bài viết |
| Xóa mã ủy quyền bài viết | `POST` | `/open_api/v1.3/business/post/authorize/delete/` | Xóa mã ủy quyền (auth code) của bài viết TikTok |
| Tổng quan thuộc tính URL | - | - | Giới thiệu quy trình xác minh quyền sở hữu tên miền/tiền tố URL |
| Thêm thuộc tính URL vào tài khoản quảng cáo | `POST` | `/open_api/v1.3/business/property/add/` | Thêm tên miền hoặc tiền tố URL để chuẩn bị xác minh |
| Kiểm tra kết quả xác minh thuộc tính URL | `POST` | `/open_api/v1.3/business/property/verify/` | Kiểm tra kết quả xác minh quyền sở hữu thuộc tính URL |
| Xóa quyền sở hữu thuộc tính URL | `POST` | `/open_api/v1.3/business/property/delete/` | Xóa quyền sở hữu đã xác minh của thuộc tính URL |
| Danh sách thuộc tính URL đã thêm | `GET` | `/open_api/v1.3/business/property/list/` | Lấy danh sách thuộc tính URL đã thêm vào tài khoản |
| Tổng quan Webhook tài khoản TikTok | - | - | Giới thiệu hệ thống nhận sự kiện thời gian thực qua Webhook |
| Tạo hoặc cập nhật cấu hình Webhook | `POST` | `/open_api/v1.3/business/webhook/update/` | Cấu hình URL callback và danh sách bài viết theo dõi |
| Lấy danh sách cấu hình Webhook | `GET` | `/open_api/v1.3/business/webhook/list/` | Tra cứu cấu hình Webhook hiện có của ứng dụng |
| Xóa cấu hình Webhook | `POST` | `/open_api/v1.3/business/webhook/delete/` | Xóa toàn bộ cấu hình Webhook hoặc gỡ bỏ bài viết theo dõi |

---

## Gợi ý hashtag cho tài khoản TikTok (`Get recommended hashtags for TikTok accounts`)
<a id="doc-1762228503821314"></a>
<!-- doc_id: 1762228503821314 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/business/hashtag/suggestion/`

**Mục đích**: Chỉ định một từ khóa để nhận danh sách các hashtag được gợi ý sử dụng cho video trên tài khoản TikTok của bạn. Tên hashtag trả về (`name`) có thể được dùng trong trường `caption` khi đăng video lên tài khoản thông qua [/business/video/publish/](01-accounts-p1.md#doc-1762228496095234).

> [!NOTE]
> - Đây là endpoint mới trong phiên bản API v1.3.
> - Nếu không có gợi ý hashtag nào phù hợp với `keyword` bạn chỉ định, API sẽ trả về chính từ khóa đó trong trường `name`, đồng thời `post_count` sẽ bằng `0`.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Có | Access token được ủy quyền bởi người sáng tạo TikTok. Để lấy mã truy cập này, sử dụng [/tt_user/oauth2/token/](10-authentication.md#doc-1833997638479041). |

### Tham số (GET: query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `business_id` | string | Có | Mã định danh duy nhất theo ứng dụng của tài khoản TikTok. Truyền giá trị trường `open_id` nhận được trong phản hồi của [/tt_user/oauth2/token/](10-authentication.md#doc-1833997638479041) vào trường này. |
| `keyword` | string | Có | Từ khóa bạn muốn lấy danh sách hashtag gợi ý. |
| `language` | string | Không | Ngôn ngữ của từ khóa. Ngôn ngữ của các hashtag gợi ý sẽ khớp với ngôn ngữ của từ khóa.<br><br>**Giá trị mặc định**: `en` (tiếng Anh).<br><br>**Các giá trị enum**:<br>• `en`: Tiếng Anh<br>• `ar`: Tiếng Ả Rập<br>• `bn-IN`: Tiếng Bengali<br>• `ceb-PH`: Tiếng Cebuano<br>• `cs-CZ`: Tiếng Séc<br>• `de-DE`: Tiếng Đức<br>• `el-GR`: Tiếng Hy Lạp<br>• `es`: Tiếng Tây Ban Nha<br>• `fi-FI`: Tiếng Phần Lan<br>• `fil-PH`: Tiếng Filipino<br>• `fr`: Tiếng Pháp<br>• `he-IL`: Tiếng Hebrew<br>• `hi-IN`: Tiếng Hindi<br>• `hu-HU`: Tiếng Hungary<br>• `id-ID`: Tiếng Indonesia<br>• `it-IT`: Tiếng Ý<br>• `ja-JP`: Tiếng Nhật<br>• `jv-ID`: Tiếng Java<br>• `km-KH`: Tiếng Khmer<br>• `ko-KR`: Tiếng Hàn<br>• `ms-MY`: Tiếng Mã Lai<br>• `my-MM`: Tiếng Miến Điện<br>• `nl-NL`: Tiếng Hà Lan<br>• `pl-PL`: Tiếng Ba Lan<br>• `pt-BR`: Tiếng Bồ Đào Nha<br>• `ro-RO`: Tiếng Romania<br>• `ru-RU`: Tiếng Nga<br>• `sv-SE`: Tiếng Thụy Điển<br>• `th-TH`: Tiếng Thái<br>• `tr-TR`: Tiếng Thổ Nhĩ Kỳ<br>• `uk-UA`: Tiếng Ukraina<br>• `ur`: Tiếng Urdu<br>• `vi-VN`: Tiếng Việt<br>• `zh-Hans`: Tiếng Trung (giản thể)<br>• `zh-Hant-TW`: Tiếng Trung (phồn thể) |

### Header phản hồi

Các header quan trọng cần ghi lại để hỗ trợ xử lý sự cố:
- `Date`: Thời gian nhận phản hồi (GMT), ví dụ: `Fri, 13 Aug 2021 08:04:42 GMT`.
- `X-Tt-Logid`: Mã định danh duy nhất của yêu cầu API (quan trọng để tra cứu log).

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Xem danh sách chi tiết tại [Phụ lục mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). Giá trị `0` là thành công. |
| `message` | string | Thông báo phản hồi. Chi tiết xem [Phụ lục thông tin phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `request_id` | string | Mã định danh duy nhất cho yêu cầu API. Vui lòng ghi lại trường này cho mọi yêu cầu để tra cứu khi gặp sự cố. |
| `data` | object | Dữ liệu trả về. |
| ↳ `suggestions` | object[] | Danh sách hashtag gợi ý. Tối đa 10 hashtag gợi ý được cung cấp, được sắp xếp ưu tiên theo khớp chính xác trước, sau đó sắp xếp theo số lượng bài đăng (`post_count`). |
| ↳↳ `name` | string | Tên của hashtag gợi ý. |
| ↳↳ `view_count` | number | Số lượt xem mà hashtag gợi ý đã nhận được. *(Lưu ý: Trường này ngừng hỗ trợ trước ngày 09/10/2026).* |
| ↳↳ `post_count` | number | Tổng số bài đăng đã sử dụng hashtag gợi ý này. |

### Ví dụ

#### cURL
```bash
curl -X GET "https://business-api.tiktok.com/open_api/v1.3/business/hashtag/suggestion/?business_id=6789012345678901234&keyword=summer&language=en" \
  -H "Access-Token: ACCESS_TOKEN"
```

#### Python
```python
import requests

ACCESS_TOKEN = "your_access_token"
BUSINESS_ID = "6789012345678901234"

url = "https://business-api.tiktok.com/open_api/v1.3/business/hashtag/suggestion/"
headers = {"Access-Token": ACCESS_TOKEN}
params = {
    "business_id": BUSINESS_ID,
    "keyword": "summer",
    "language": "en"
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

#### Phản hồi mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202410231500000101111222333444555",
  "data": {
    "suggestions": [
      {
        "name": "summer",
        "post_count": 65296335,
        "view_count": 570706039722
      },
      {
        "name": "summervibes",
        "post_count": 8,
        "view_count": 61002
      },
      {
        "name": "summertime",
        "post_count": 4787632,
        "view_count": 31235450501
      },
      {
        "name": "summeroutfit",
        "post_count": 2245117,
        "view_count": 22769671766
      }
    ]
  }
}
```

---

## Lấy danh sách thẻ vị trí cho tài khoản TikTok (`Get the location tags for a TikTok account`)
<a id="doc-1870580030749698"></a>
<!-- doc_id: 1870580030749698 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/business/publish/location/`

**Mục đích**: Lấy danh sách các thẻ vị trí (location tags) khả dụng cho tài khoản TikTok theo từ khóa tìm kiếm. Bạn có thể đính kèm các thẻ vị trí này khi đăng bài video hoặc ảnh để hiển thị vị trí trên bài đăng, giúp tiếp cận đối tượng người xem địa phương và nâng cao mức độ tương tác.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Có | Access token được ủy quyền bởi người sáng tạo TikTok. Để lấy mã truy cập, sử dụng [/tt_user/oauth2/token/](10-authentication.md#doc-1833997638479041). |

### Tham số (GET: query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `business_id` | string | Có | Mã định danh duy nhất theo ứng dụng của tài khoản TikTok. Truyền giá trị trường `open_id` nhận được từ phản hồi của [/tt_user/oauth2/token/](10-authentication.md#doc-1833997638479041) vào trường này. |
| `search_query` | string | Có | Chuỗi truy vấn bạn cung cấp để tìm kiếm địa điểm có thể thêm vào bài đăng TikTok. Giới hạn độ dài: tối đa 100 ký tự. |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Xem chi tiết tại [Phụ lục mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông báo phản hồi. Xem chi tiết tại [Phụ lục mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `request_id` | string | Log ID của yêu cầu, dùng để định danh duy nhất mỗi yêu cầu API. |
| `data` | object | Dữ liệu trả về. |
| ↳ `locations` | object[] | Danh sách các vị trí tìm thấy. Tối đa 20 vị trí được trả về. |
| ↳↳ `location_name` | string | Tên của địa điểm/vị trí. |
| ↳↳ `location_id` | string | ID của thẻ vị trí. Bạn có thể truyền ID này kèm theo `location_name` vào [/business/video/publish/](01-accounts-p1.md#doc-1762228496095234) hoặc [/business/photo/publish/](01-accounts-p1.md#doc-1803630424390658) để hiển thị vị trí liên kết trên bài đăng đã xuất bản. |
| ↳↳ `location_address` | string | Thông tin địa chỉ bổ sung liên kết với vị trí. Nội dung nhận được có thể bao gồm nhưng không giới hạn ở: chỉ quốc gia (`United Kingdom`), bang/vùng + quốc gia (`Florida, United States`), thành phố + quốc gia (`Cairo, Egypt`), hoặc địa chỉ đường phố đầy đủ (`300 West 47th Street, New York, New York 10036, USA`). |

### Ví dụ

#### cURL
```bash
curl -X GET "https://business-api.tiktok.com/open_api/v1.3/business/publish/location/?business_id=6789012345678901234&search_query=new" \
  -H "Access-Token: ACCESS_TOKEN"
```

#### Python
```python
import requests

ACCESS_TOKEN = "your_access_token"
BUSINESS_ID = "6789012345678901234"

url = "https://business-api.tiktok.com/open_api/v1.3/business/publish/location/"
headers = {"Access-Token": ACCESS_TOKEN}
params = {
    "business_id": BUSINESS_ID,
    "search_query": "new"
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

#### Phản hồi mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20241023150000010222333444555666",
  "data": {
    "locations": [
      {
        "location_address": "New York, United States",
        "location_id": "22535865208931252",
        "location_name": "New City"
      },
      {
        "location_address": "Doğanay, Ordu Cd. No:39, 35160 Karabağlar/İzmir, Türkiye",
        "location_id": "22535865260174927",
        "location_name": "New York City"
      }
    ]
  }
}
```

---

## Tổng quan ủy quyền quảng cáo bài viết TikTok (`Ad authorization`)
<a id="doc-1815051698931714"></a>
<!-- doc_id: 1815051698931714 -->

Nhóm API này cho phép bạn quản lý cài đặt ủy quyền quảng cáo (Ad authorization) cho các bài viết tự nhiên (organic posts) trên tài khoản TikTok nhằm phục vụ quảng cáo Spark Ads. Thông qua các endpoint này, người sáng tạo hoặc chủ tài khoản TikTok có thể cho phép sử dụng bài viết của mình làm nội dung sáng tạo quảng cáo, lấy mã ủy quyền (video code / auth code), gia hạn thời gian hiệu lực, hoặc hủy ủy quyền.

Nhóm API bao gồm các endpoint sau:
- [Bật hoặc tắt cài đặt ủy quyền quảng cáo cho bài viết TikTok](01-accounts-p2.md#doc-1815051741912066): Bật hoặc tắt trạng thái ủy quyền cho một bài viết cụ thể và tạo mã ủy quyền ban đầu.
- [Gia hạn thời gian hiệu lực ủy quyền bài viết TikTok](01-accounts-p2.md#doc-1815051784582210): Kéo dài thời gian hiệu lực của mã ủy quyền hiện có hoặc tạo lại mã mới nếu mã trước đó đã bị xóa.
- [Lấy trạng thái ủy quyền của bài viết TikTok](01-accounts-p2.md#doc-1815051801257986): Tra cứu thông tin mã ủy quyền, ngày bắt đầu, ngày hết hạn và trạng thái hiện tại.
- [Xóa mã ủy quyền của bài viết TikTok](01-accounts-p2.md#doc-1815051817073665): Xóa mã ủy quyền nhằm ngăn chặn việc sử dụng bài viết trong các chiến dịch quảng cáo mới.

> [!IMPORTANT]
> - Để sử dụng các endpoint trong nhóm này, access token của tài khoản TikTok phải có phạm vi quyền `biz.spark.auth`. Bạn có thể kiểm tra scope thông qua [/tt_user/token_info/get/](01-accounts-p1.md#doc-1765927978092545).
> - Trước khi xóa mã ủy quyền hoặc tắt ủy quyền quảng cáo, bạn bắt buộc phải tạm dừng tất cả các chiến dịch quảng cáo hoặc nhóm quảng cáo đang hoạt động có sử dụng bài viết đó.

---

## Bật hoặc tắt cài đặt ủy quyền quảng cáo cho bài viết TikTok (`Enable or disable the ad authorization setting for a TikTok post`)
<a id="doc-1815051741912066"></a>
<!-- doc_id: 1815051741912066 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/business/post/authorize/setting/`

**Mục đích**: Bật hoặc tắt cài đặt "Ủy quyền quảng cáo" (Ad authorization) cho một bài viết trên tài khoản TikTok. Để tìm hiểu thêm về cách quản lý cài đặt ủy quyền quảng cáo cho bài viết TikTok, xem [Quản lý ủy quyền quảng cáo bài viết TikTok](../10-organic-api/accounts-api.md#doc-1815124785075201).

> [!NOTE]
> - Khi bật "Ad authorization", bạn xác nhận rằng đã đọc và đồng ý với [Điều khoản dịch vụ nội dung quảng cáo](https://ads.tiktok.com/i18n/official/policy/advertising-terms), đồng thời cho phép quảng bá bài viết này trên TikTok. Khi cài đặt được bật, trạng thái quyền riêng tư của bài viết sẽ chuyển thành "Available for Ads" để đội ngũ xét duyệt quảng cáo có thể duyệt bài. Ngoài TikTok, bài viết cũng có thể xuất hiện dưới dạng quảng cáo trên các nền tảng bên thứ ba.
> - Để xóa mã ủy quyền (video code) hoặc tắt ủy quyền quảng cáo, bạn phải tạm dừng mọi chiến dịch hoặc quảng cáo đang hoạt động có liên kết với video này.
> - Để gia hạn thời gian ủy quyền, hãy sử dụng [/business/post/authorize/](01-accounts-p2.md#doc-1815051784582210).

### Chuẩn bị trước khi bắt đầu

Lấy access token của tài khoản TikTok có phạm vi quyền `biz.spark.auth` và mã định danh duy nhất theo ứng dụng của tài khoản TikTok theo hướng dẫn trong [Ủy quyền](../10-organic-api/accounts-api.md#doc-1738083939371009) và [Xác thực](../10-organic-api/accounts-api.md#doc-1738084387220481).
- Để kiểm tra xem access token đã có quyền `biz.spark.auth` hay chưa, gọi endpoint [/tt_user/token_info/get/](01-accounts-p1.md#doc-1765927978092545) và kiểm tra trường `scope` trả về.
- Nếu chưa có quyền `biz.spark.auth`, hãy yêu cầu chủ tài khoản TikTok cấp quyền quản lý mã ủy quyền Spark Ads qua luồng Ủy quyền.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Có | Access token được ủy quyền bởi người sáng tạo TikTok. Dùng [/tt_user/oauth2/token/](10-authentication.md#doc-1833997638479041) để lấy token. |
| `Content-Type` | string | Có | Định dạng nội dung yêu cầu. Giá trị cho phép: `application/json`. |

### Tham số (POST: JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `business_id` | string | Có | Mã định danh duy nhất theo ứng dụng của tài khoản TikTok. Truyền giá trị trường `open_id` nhận được từ [/tt_user/oauth2/token/](10-authentication.md#doc-1833997638479041). |
| `item_id` | string | Có | ID của bài viết TikTok. Để lấy danh sách bài viết công khai của tài khoản, sử dụng [/business/video/list/](01-accounts-p1.md#doc-1762228421622786). Ví dụ: `7123456789123456789`. |
| `is_ad_promotable` | boolean | Có | Xác định bật hay tắt cài đặt "Ad authorization" để cho phép quảng bá bài viết.<br><br>**Giá trị hỗ trợ**:<br>• `true`: Bật cài đặt ủy quyền quảng cáo.<br>• `false`: Tắt cài đặt ủy quyền quảng cáo.<br><br>> [!NOTE]<br>> Nếu bài viết TikTok đang được sử dụng trong Spark Ads, bạn không thể tắt cài đặt ủy quyền quảng cáo (`is_ad_promotable` = `false`). |
| `authorization_days` | number | Không | Thời hạn hiệu lực ủy quyền tính theo số ngày.<br><br>**Giá trị hỗ trợ**: `7`, `30`, `60`, `180`, `365`.<br>**Giá trị mặc định**: `30`. |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Xem chi tiết tại [Phụ lục mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Mã log duy nhất định danh yêu cầu. |
| `data` | object | Dữ liệu trả về. |
| ↳ `item_id` | string | ID của bài viết TikTok. |
| ↳ `auth_code` | string | *(Chỉ trả về khi `is_ad_promotable` = `true`)*. Mã ủy quyền của bài viết TikTok (dùng để tạo quảng cáo Spark Ads). Ví dụ: `#1Ea2bcde3fUM/ghijEk/L4mOceft5deFRq6za7JsgnAJ8PB9n1XIr1rC1b/5Rw4=`. |
| ↳ `auth_code_start_time` | string | *(Chỉ trả về khi `is_ad_promotable` = `true`)*. Thời điểm mã ủy quyền bắt đầu có hiệu lực, theo định dạng `YYYY-MM-DD HH:MM:SS` (UTC+0). |
| ↳ `auth_code_end_time` | string | *(Chỉ trả về khi `is_ad_promotable` = `true`)*. Thời điểm mã ủy quyền hết hạn, theo định dạng `YYYY-MM-DD HH:MM:SS` (UTC+0). |
| ↳ `authorization_days` | number | *(Chỉ trả về khi `is_ad_promotable` = `true`)*. Thời hạn hiệu lực ủy quyền tính theo số ngày. |
| ↳ `auth_code_status` | string | *(Chỉ trả về khi `is_ad_promotable` = `true`)*. Trạng thái của mã ủy quyền.<br><br>**Enum**:<br>• `NOT_USED`: Mã ủy quyền đã được tạo nhưng chưa được sử dụng trong quảng cáo.<br>• `IN_USE`: Mã ủy quyền đang được sử dụng trong quảng cáo.<br>• `EXPIRED`: Mã ủy quyền đã hết hạn. |
| ↳ `is_ad_promotable` | boolean | *(Chỉ trả về khi `is_ad_promotable` được đặt là `false` trong yêu cầu)*. Giá trị trả về là `false` biểu thị cài đặt ủy quyền quảng cáo đã bị tắt. |

### Ví dụ

#### cURL: Bật cài đặt ủy quyền quảng cáo
```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/business/post/authorize/setting/" \
  -H "Access-Token: ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "business_id": "6789012345678901234",
    "item_id": "7123456789123456789",
    "is_ad_promotable": true,
    "authorization_days": 365
  }'
```

#### cURL: Tắt cài đặt ủy quyền quảng cáo
```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/business/post/authorize/setting/" \
  -H "Access-Token: ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "business_id": "6789012345678901234",
    "item_id": "7123456789123456789",
    "is_ad_promotable": false
  }'
```

#### Phản hồi mẫu khi bật thành công
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20241023150000010333444555666777",
  "data": {
    "auth_code": "#1Ea2bcde3fUM/ghijEk/L4mOceft5deFRq6za7JsgnAJ8PB9n1XIr1rC1b/5Rw4=",
    "auth_code_end_time": "2025-10-23 15:00:00",
    "auth_code_start_time": "2024-10-23 15:00:00",
    "auth_code_status": "NOT_USED",
    "authorization_days": 365,
    "item_id": "7123456789123456789"
  }
}
```

#### Phản hồi mẫu khi tắt thành công
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20241023150000010333444555666888",
  "data": {
    "is_ad_promotable": false,
    "item_id": "7123456789123456789"
  }
}
```

---

## Gia hạn thời gian hiệu lực ủy quyền bài viết TikTok (`Extend the authorization validity period of a TikTok post`)
<a id="doc-1815051784582210"></a>
<!-- doc_id: 1815051784582210 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/business/post/authorize/`

**Mục đích**: Gia hạn thời gian hiệu lực của mã ủy quyền hiện có cho một bài viết trên TikTok. Nếu mã ủy quyền của bài viết đã bị xóa trước đó, bạn có thể sử dụng endpoint này để tạo lại một mã ủy quyền mới cho bài viết.

> [!NOTE]
> Nếu mã ủy quyền của một bài viết TikTok đã bị xóa, việc gọi endpoint này sẽ tự động tạo một mã ủy quyền mới cho bài viết đó.

### Chuẩn bị trước khi bắt đầu

Đảm bảo rằng cài đặt "Ad authorization" đã được bật cho bài viết TikTok; nếu chưa, API sẽ báo lỗi. Để bật cài đặt ủy quyền quảng cáo, sử dụng [/business/post/authorize/setting/](01-accounts-p2.md#doc-1815051741912066) và đặt `is_ad_promotable` thành `true`.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Có | Access token được ủy quyền bởi người sáng tạo TikTok. Dùng [/tt_user/oauth2/token/](10-authentication.md#doc-1833997638479041) để lấy token. |
| `Content-Type` | string | Có | Định dạng nội dung yêu cầu. Giá trị cho phép: `application/json`. |

### Tham số (POST: JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `business_id` | string | Có | Mã định danh duy nhất theo ứng dụng của tài khoản TikTok. Truyền giá trị trường `open_id` nhận được từ [/tt_user/oauth2/token/](10-authentication.md#doc-1833997638479041). |
| `item_id` | string | Có | ID của bài viết TikTok. Để lấy danh sách bài viết, sử dụng [/business/video/list/](01-accounts-p1.md#doc-1762228421622786). Ví dụ: `7123456789123456789`. |
| `authorization_days` | number | Không | Thời gian gia hạn hiệu lực ủy quyền tính theo số ngày:<br>• Nếu bài viết đã có mã ủy quyền, trường này đại diện cho khoảng thời gian cộng thêm vào thời hạn ủy quyền hiện tại. Ví dụ: thời hạn hiện tại là 180 ngày và bạn đặt trường này là `180`, thời hạn hiệu lực mới sẽ là 360 ngày.<br>• Nếu mã ủy quyền đã bị xóa, trường này đại diện cho thời gian hiệu lực của mã ủy quyền mới.<br><br>**Giá trị hỗ trợ**: `7`, `30`, `60`, `180`, `365`.<br>**Giá trị mặc định**: `30`. |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Xem chi tiết tại [Phụ lục mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Mã log duy nhất định danh yêu cầu. |
| `data` | object | Dữ liệu trả về. |
| ↳ `item_id` | string | ID của bài viết TikTok. |
| ↳ `auth_code` | string | Mã ủy quyền của bài viết TikTok. |
| ↳ `auth_code_start_time` | string | Thời điểm mã ủy quyền bắt đầu có hiệu lực, theo định dạng `YYYY-MM-DD HH:MM:SS` (UTC+0). |
| ↳ `auth_code_end_time` | string | Thời điểm mã ủy quyền hết hạn sau khi gia hạn, theo định dạng `YYYY-MM-DD HH:MM:SS` (UTC+0). |
| ↳ `authorization_days` | number | Tổng thời hạn hiệu lực ủy quyền tính theo số ngày. |

### Ví dụ

#### cURL
```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/business/post/authorize/" \
  -H "Access-Token: ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "business_id": "6789012345678901234",
    "item_id": "7123456789123456789",
    "authorization_days": 180
  }'
```

#### Phản hồi mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20241023150000010444555666777888",
  "data": {
    "auth_code": "#1Ea2bcde3fUM/ghijEk/L4mOceft5deFRq6za7JsgnAJ8PB9n1XIr1rC1b/5Rw4=",
    "auth_code_end_time": "2025-10-31 12:58:42",
    "auth_code_start_time": "2024-11-05 12:58:42",
    "authorization_days": 360,
    "item_id": "7123456789123456789"
  }
}
```

---

## Lấy trạng thái ủy quyền của bài viết TikTok (`Get the authorization status of a TikTok post`)
<a id="doc-1815051801257986"></a>
<!-- doc_id: 1815051801257986 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/business/post/authorize/status/`

**Mục đích**: Lấy thông tin trạng thái ủy quyền và chi tiết mã ủy quyền của một bài viết trên TikTok.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Có | Access token được ủy quyền bởi người sáng tạo TikTok. Dùng [/tt_user/oauth2/token/](10-authentication.md#doc-1833997638479041). |

### Tham số (GET: query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `business_id` | string | Có | Mã định danh duy nhất theo ứng dụng của tài khoản TikTok (`open_id`). |
| `item_id` | string | Có | ID của bài viết TikTok. |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Xem chi tiết tại [Phụ lục mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Mã log duy nhất của yêu cầu. |
| `data` | object | Dữ liệu trả về. |
| ↳ `item_id` | string | ID của bài viết TikTok. Ví dụ: `7123456789123456789`. |
| ↳ `auth_code` | string | Mã ủy quyền của bài viết TikTok. |
| ↳ `auth_code_start_time` | string | Thời điểm mã ủy quyền bắt đầu có hiệu lực, định dạng `YYYY-MM-DD HH:MM:SS` (UTC+0). |
| ↳ `auth_code_end_time` | string | Thời điểm mã ủy quyền hết hiệu lực, định dạng `YYYY-MM-DD HH:MM:SS` (UTC+0). |
| ↳ `authorization_days` | number | Thời hạn hiệu lực ủy quyền tính theo số ngày. Ví dụ: `30`. |
| ↳ `auth_code_status` | string | Trạng thái của mã ủy quyền.<br><br>**Enum**:<br>• `NOT_USED`: Mã ủy quyền đã tạo nhưng chưa được sử dụng.<br>• `IN_USE`: Mã ủy quyền đang được sử dụng trong quảng cáo.<br>• `EXPIRED`: Mã ủy quyền đã hết hạn. |

### Ví dụ

#### cURL
```bash
curl -X GET "https://business-api.tiktok.com/open_api/v1.3/business/post/authorize/status/?business_id=6789012345678901234&item_id=7123456789123456789" \
  -H "Access-Token: ACCESS_TOKEN"
```

#### Python
```python
import requests

ACCESS_TOKEN = "your_access_token"
BUSINESS_ID = "6789012345678901234"
ITEM_ID = "7123456789123456789"

url = "https://business-api.tiktok.com/open_api/v1.3/business/post/authorize/status/"
headers = {"Access-Token": ACCESS_TOKEN}
params = {
    "business_id": BUSINESS_ID,
    "item_id": ITEM_ID
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

#### Phản hồi mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20241023150000010555666777888999",
  "data": {
    "auth_code": "#1Ea2bcde3fUM/ghijEk/L4mOceft5deFRq6za7JsgnAJ8PB9n1XIr1rC1b/5Rw4=",
    "auth_code_end_time": "2024-12-07 00:21:37",
    "auth_code_start_time": "2024-10-31 00:21:37",
    "auth_code_status": "NOT_USED",
    "authorization_days": 37,
    "item_id": "7123456789123456789"
  }
}
```

---

## Xóa mã ủy quyền của bài viết TikTok (`Delete the authorization code of a TikTok post`)
<a id="doc-1815051817073665"></a>
<!-- doc_id: 1815051817073665 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/business/post/authorize/delete/`

**Mục đích**: Xóa mã ủy quyền của một bài viết trên TikTok. Khi mã ủy quyền bị xóa, bài viết sẽ không thể được sử dụng để tạo quảng cáo Spark Ads mới.

> [!NOTE]
> - Nếu bài viết TikTok không có mã ủy quyền (chưa từng tạo hoặc đã bị xóa trước đó), API sẽ báo lỗi.
> - Trước khi xóa mã ủy quyền, bạn bắt buộc phải tạm dừng mọi chiến dịch hoặc quảng cáo đang hoạt động có liên kết với video này.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Có | Access token được ủy quyền bởi người sáng tạo TikTok. Dùng [/tt_user/oauth2/token/](10-authentication.md#doc-1833997638479041). |
| `Content-Type` | string | Có | Định dạng nội dung yêu cầu. Giá trị cho phép: `application/json`. |

### Tham số (POST: JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `business_id` | string | Có | Mã định danh duy nhất theo ứng dụng của tài khoản TikTok (`open_id`). |
| `item_id` | string | Có | ID của bài viết TikTok cần xóa mã ủy quyền. |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Xem chi tiết tại [Phụ lục mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Mã log định danh duy nhất của yêu cầu. |
| `data` | object | Dữ liệu trả về. |
| ↳ `item_id` | string | ID của bài viết TikTok. |
| ↳ `auth_code_status` | string | Trạng thái của mã ủy quyền.<br><br>**Enum**:<br>• `DELETED`: Mã ủy quyền đã được xóa thành công. |

### Ví dụ

#### cURL
```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/business/post/authorize/delete/" \
  -H "Access-Token: ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "business_id": "6789012345678901234",
    "item_id": "7123456789123456789"
  }'
```

#### Phản hồi mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20241023150000010666777888999000",
  "data": {
    "auth_code_status": "DELETED",
    "item_id": "7123456789123456789"
  }
}
```

---

## Tổng quan thuộc tính URL (`URL properties`)
<a id="doc-1769325247778818"></a>
<!-- doc_id: 1769325247778818 -->

Nhóm API thuộc tính URL (URL properties) cho phép nhà quảng cáo thêm và xác minh quyền sở hữu trang web (tên miền domain hoặc tiền tố URL prefix) dưới tài khoản quảng cáo TikTok. Việc xác minh quyền sở hữu trang web giúp nâng cao độ tin cậy của tài khoản, bảo vệ thương hiệu và kích hoạt các tính năng đo lường, phân phối quảng cáo nâng cao.

Nhóm API này bao gồm các endpoint:
- [Thêm thuộc tính URL vào tài khoản quảng cáo](01-accounts-p2.md#doc-1769325280876545): Đăng ký tên miền hoặc tiền tố URL để tạo chuỗi chữ ký xác minh và file xác minh.
- [Kiểm tra kết quả xác minh thuộc tính URL](01-accounts-p2.md#doc-1769325308162050): Kiểm tra xem việc tải file xác minh lên máy chủ web đã thành công và quyền sở hữu đã được công nhận hay chưa.
- [Xóa quyền sở hữu đã xác minh của thuộc tính URL](01-accounts-p2.md#doc-1769325351919617): Hủy quyền sở hữu của một thuộc tính URL đã xác minh khỏi tài khoản quảng cáo.
- [Lấy danh sách thuộc tính URL đã thêm vào tài khoản quảng cáo](01-accounts-p2.md#doc-1769325368603650): Tra cứu tất cả các thuộc tính URL đã đăng ký và trạng thái xác minh tương ứng.

> [!IMPORTANT]
> - Bắt đầu từ ngày **15/10/2025**, bạn bắt buộc phải cung cấp bí mật ứng dụng (`secret`) của ứng dụng nhà phát triển khi gọi tất cả các endpoint trong nhóm này.
> - Xem hướng dẫn chi tiết quy trình xác minh trang web tại [Quản lý thuộc tính URL](../10-organic-api/accounts-api.md#doc-1769324038780930).

---

## Thêm thuộc tính URL vào tài khoản quảng cáo (`Add a URL property to an ad account`)
<a id="doc-1769325280876545"></a>
<!-- doc_id: 1769325280876545 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/business/property/add/`

**Mục đích**: Thêm một thuộc tính URL (tên miền domain hoặc tiền tố URL prefix) mà bạn muốn xác minh quyền sở hữu vào tài khoản quảng cáo. Để tìm hiểu quy trình thêm và xác minh thuộc tính URL, xem [Quản lý thuộc tính URL](../10-organic-api/accounts-api.md#doc-1769324038780930).

> [!IMPORTANT]
> Bắt đầu từ ngày 15/10/2025, bạn bắt buộc phải cung cấp mã bí mật ứng dụng nhà phát triển (`secret`) để gọi endpoint này.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Content-Type` | string | Có | Định dạng nội dung yêu cầu. Giá trị cho phép: `application/json`. |

### Tham số (POST: JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `app_id` | string | Có | ID của ứng dụng nhà phát triển. Để tìm **App ID**, truy cập **[My Apps](https://business-api.tiktok.com/portal/apps)** > **App Detail** > **Basic Information**. |
| `secret` | string | Có | Bí mật (secret) của ứng dụng nhà phát triển. Để tìm **Secret**, truy cập [My Apps](https://ads.tiktok.com/marketing_api/apps/) > **App Detail** > **Basic Information**. |
| `url_property_meta` | object | Có | Thông tin về thuộc tính URL mà bạn muốn thêm và xác minh quyền sở hữu. |
| ↳ `property_type` | integer | Có | Loại thuộc tính URL.<br><br>**Enum**:<br>• `1`: Tên miền (Domain).<br>• `2`: Tiền tố URL (URL prefix). |
| ↳ `url` | string | Có | URL bạn sở hữu muốn thêm vào tài khoản. Truyền giá trị URL phù hợp theo `property_type` đã chọn:<br>• Nếu `property_type` là `1`: Chỉ định tên miền gốc (ví dụ: `example.com`) hoặc tên miền phụ (ví dụ: `subdomain.example.com`).<br>• Nếu `property_type` là `2`: Chỉ định tiền tố URL bao gồm `https://` + host (phải là tên miền) + đường dẫn + `/`, và không được chứa chuyển hướng URL. Ví dụ trong `https://www.example.com/folder/`, host là `www.example.com` và đường dẫn là `/folder`. |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Xem chi tiết tại [Phụ lục mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Mã log định danh duy nhất của yêu cầu. |
| `data` | object | Dữ liệu trả về. |
| ↳ `url_property_info` | object | Thông tin về thuộc tính URL đã thêm và đang chờ xác minh quyền sở hữu. |
| ↳↳ `property_type` | integer | Loại thuộc tính URL.<br><br>**Enum**:<br>• `1`: Domain.<br>• `2`: URL prefix. |
| ↳↳ `url` | string | URL sở hữu đã thêm và đang chờ xác minh quyền sở hữu. |
| ↳↳ `property_status` | integer | Trạng thái xác minh của thuộc tính URL.<br><br>**Enum**:<br>• `0`: Đang chờ xác minh (Pending for verification). |
| ↳↳ `signature` | string | Chuỗi chữ ký sử dụng trong quy trình xác minh quyền sở hữu. |
| ↳↳ `file_name` | string | Tên file chữ ký sử dụng trong quy trình xác minh quyền sở hữu (dùng để lưu file và tải lên máy chủ web). |

### Ví dụ

#### cURL
```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/business/property/add/" \
  -H "Content-Type: application/json" \
  -d '{
    "app_id": "your_app_id",
    "secret": "your_app_secret",
    "url_property_meta": {
      "url": "example.com",
      "property_type": 1
    }
  }'
```

#### Phản hồi mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20241023150000010777888999000111",
  "data": {
    "url_property_info": {
      "file_name": "tiktok-verification-xyz.txt",
      "property_status": 0,
      "property_type": 1,
      "signature": "tiktok-property-verification-signature-token-12345",
      "url": "example.com"
    }
  }
}
```

---

## Kiểm tra kết quả xác minh thuộc tính URL (`Check the URL property verification result`)
<a id="doc-1769325308162050"></a>
<!-- doc_id: 1769325308162050 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/business/property/verify/`

**Mục đích**: Kiểm tra kết quả xác minh quyền sở hữu của thuộc tính URL (tên miền domain hoặc tiền tố URL prefix). Để tìm hiểu thêm về quy trình thêm và xác minh thuộc tính URL, xem [Quản lý thuộc tính URL](../10-organic-api/accounts-api.md#doc-1769324038780930).

> [!IMPORTANT]
> Bắt đầu từ ngày 15/10/2025, bạn bắt buộc phải chỉ định bí mật ứng dụng (`secret`) để gọi endpoint này.

> [!NOTE]
> Để tránh việc xác minh tiền tố URL thất bại, hãy kiểm tra kỹ các chi tiết sau trước khi kiểm tra kết quả xác minh:
> - File xác minh có thể truy cập công khai trên mạng sau khi được tải lên máy chủ web.
> - Tên file tải lên phải khớp chính xác với giá trị tham số `file_name`. Nếu tên file bị gán thêm đuôi mở rộng thành ".txt.txt", hãy xóa đuôi thừa để tên file chỉ có duy nhất một phần mở rộng ".txt".

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Content-Type` | string | Có | Định dạng nội dung yêu cầu. Giá trị cho phép: `application/json`. |

### Tham số (POST: JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `app_id` | string | Có | ID của ứng dụng nhà phát triển. Để tìm **App ID**, truy cập **[My Apps](https://business-api.tiktok.com/portal/apps)** > **App Detail** > **Basic Information**. |
| `secret` | string | Có | Bí mật (secret) của ứng dụng nhà phát triển. Để tìm **Secret**, truy cập [My Apps](https://ads.tiktok.com/marketing_api/apps/) > **App Detail** > **Basic Information**. |
| `url_property_meta` | object | Có | Thông tin về thuộc tính URL mà bạn muốn kiểm tra kết quả xác minh quyền sở hữu. |
| ↳ `property_type` | integer | Có | Loại thuộc tính URL.<br><br>**Enum**:<br>• `1`: Domain.<br>• `2`: URL prefix. |
| ↳ `url` | string | Có | URL sở hữu muốn kiểm tra kết quả xác minh. Truyền vào URL phù hợp với `property_type` đã chỉ định.<br>• Nếu `property_type` là `1`: Chỉ định domain gốc hoặc subdomain.<br>• Nếu `property_type` là `2`: Chỉ định tiền tố URL đầy đủ `https://host/path/`.<br><br>> [!NOTE]<br>> Truyền vào trường này thuộc tính URL mà bạn đã thêm vào tài khoản quảng cáo thông qua [/business/property/add/](01-accounts-p2.md#doc-1769325280876545). Nếu chưa thêm, API sẽ báo lỗi. Lưu ý rằng các tên miền phụ (subdomain) của một tên miền đã xác minh không cần xác minh riêng vì chúng được tự động coi là đã xác minh. |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Xem chi tiết tại [Phụ lục mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Mã log định danh duy nhất của yêu cầu. |
| `data` | object | Dữ liệu trả về. |
| ↳ `url_property_info` | object | Thông tin về kết quả xác minh quyền sở hữu của thuộc tính URL. |
| ↳↳ `property_type` | integer | Loại thuộc tính URL.<br><br>**Enum**:<br>• `1`: Domain.<br>• `2`: URL prefix. |
| ↳↳ `url` | string | URL sở hữu được chỉ định. |
| ↳↳ `property_status` | integer | Trạng thái xác minh của thuộc tính URL.<br><br>**Enum**:<br>• `1`: Đã xác minh thành công (Verified).<br>• `2`: Chưa xác minh do lượt thử xác minh thất bại. Bạn cần kiểm tra lại file cấu hình và thực hiện xác minh lại. |
| ↳↳ `signature` | string | Chuỗi chữ ký sử dụng trong quy trình xác minh. |
| ↳↳ `file_name` | string | Tên file chữ ký sử dụng trong quy trình xác minh. |

### Ví dụ

#### cURL
```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/business/property/verify/" \
  -H "Content-Type: application/json" \
  -d '{
    "app_id": "your_app_id",
    "secret": "your_app_secret",
    "url_property_meta": {
      "url": "example.com",
      "property_type": 1
    }
  }'
```

#### Phản hồi mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20241023150000010888999000111222",
  "data": {
    "url_property_info": {
      "file_name": "tiktok-verification-xyz.txt",
      "property_status": 1,
      "property_type": 1,
      "signature": "tiktok-property-verification-signature-token-12345",
      "url": "example.com"
    }
  }
}
```

---

## Xóa quyền sở hữu đã xác minh của thuộc tính URL (`Delete the verified ownership of a URL property`)
<a id="doc-1769325351919617"></a>
<!-- doc_id: 1769325351919617 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/business/property/delete/`

**Mục đích**: Xóa quyền sở hữu đã xác minh của một thuộc tính URL (tên miền domain hoặc tiền tố URL prefix) khỏi tài khoản quảng cáo. Sau khi xóa, thuộc tính URL này sẽ không còn liên kết với tài khoản quảng cáo nữa. Xem thêm tại [Quản lý thuộc tính URL](../10-organic-api/accounts-api.md#doc-1769324038780930).

> [!IMPORTANT]
> Bắt đầu từ ngày 15/10/2025, bạn bắt buộc phải cung cấp bí mật ứng dụng (`secret`) của ứng dụng nhà phát triển khi sử dụng endpoint này.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Content-Type` | string | Có | Định dạng nội dung yêu cầu. Giá trị cho phép: `application/json`. |

### Tham số (POST: JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `app_id` | string | Có | ID của ứng dụng nhà phát triển. Để tìm **App ID**, truy cập **[My Apps](https://business-api.tiktok.com/portal/apps)** > **App Detail** > **Basic Information**. |
| `secret` | string | Có | Bí mật (secret) của ứng dụng nhà phát triển. Để tìm **Secret**, truy cập [My Apps](https://ads.tiktok.com/marketing_api/apps/) > **App Detail** > **Basic Information**. |
| `url_property_meta` | object | Có | Thông tin về thuộc tính URL mà bạn muốn xóa quyền sở hữu đã xác minh. |
| ↳ `property_type` | integer | Có | Loại thuộc tính URL.<br><br>**Enum**:<br>• `1`: Domain.<br>• `2`: URL prefix. |
| ↳ `url` | string | Có | URL sở hữu bạn muốn xóa quyền sở hữu đã xác minh. Truyền URL phù hợp theo `property_type` đã chỉ định. |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Xem chi tiết tại [Phụ lục mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Mã log định danh duy nhất của yêu cầu. |
| `data` | object | Dữ liệu trả về. Đối tượng rỗng (`{}`) khi thực hiện thao tác thành công. |

### Ví dụ

#### cURL
```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/business/property/delete/" \
  -H "Content-Type: application/json" \
  -d '{
    "app_id": "your_app_id",
    "secret": "your_app_secret",
    "url_property_meta": {
      "property_type": 1,
      "url": "example.com"
    }
  }'
```

#### Phản hồi mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20241023150000010999000111222333",
  "data": {}
}
```

---

## Lấy danh sách thuộc tính URL đã thêm vào tài khoản quảng cáo (`Get the list of added URL properties under an ad account`)
<a id="doc-1769325368603650"></a>
<!-- doc_id: 1769325368603650 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/business/property/list/`

**Mục đích**: Lấy danh sách các thuộc tính URL (tên miền domain hoặc tiền tố URL prefix) đã được thêm vào tài khoản quảng cáo cùng với trạng thái xác minh tương ứng. Xem thêm tại [Quản lý thuộc tính URL](../10-organic-api/accounts-api.md#doc-1769324038780930).

> [!IMPORTANT]
> Bắt đầu từ ngày 15/10/2025, bạn bắt buộc phải cung cấp bí mật ứng dụng (`secret`) của ứng dụng nhà phát triển trong query string khi gọi endpoint này.

> [!NOTE]
> Mặc dù các tên miền phụ (subdomain) của một tên miền đã xác minh được tự động coi là đã xác minh, chúng sẽ không được liệt kê trong danh sách trả về của endpoint này trừ khi đã được thêm cụ thể vào tài khoản quảng cáo thông qua [/business/property/add/](01-accounts-p2.md#doc-1769325280876545).

### Tham số (GET: query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `app_id` | string | Có | ID của ứng dụng nhà phát triển. Để tìm **App ID**, truy cập **[My Apps](https://business-api.tiktok.com/portal/apps)** > **App Detail** > **Basic Information**. |
| `secret` | string | Có | Bí mật (secret) của ứng dụng nhà phát triển. Để tìm **Secret**, truy cập [My Apps](https://ads.tiktok.com/marketing_api/apps/) > **App Detail** > **Basic Information**. |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Xem chi tiết tại [Phụ lục mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Mã log định danh duy nhất của yêu cầu. |
| `data` | object | Dữ liệu trả về. |
| ↳ `url_property_info_list` | object[] | Danh sách thông tin về các thuộc tính URL đã thêm vào tài khoản quảng cáo. |
| ↳↳ `property_type` | integer | Loại thuộc tính URL.<br><br>**Enum**:<br>• `1`: Domain.<br>• `2`: URL prefix. |
| ↳↳ `url` | string | URL sở hữu đã thêm vào tài khoản. |
| ↳↳ `property_status` | integer | Trạng thái xác minh của thuộc tính URL.<br><br>**Enum**:<br>• `0`: Đang chờ xác minh (Pending for verification).<br>• `1`: Đã xác minh thành công (Verified).<br>• `2`: Chưa xác minh do lượt thử trước thất bại (cần xác minh lại). |
| ↳↳ `signature` | string | Chuỗi chữ ký sử dụng trong quy trình xác minh quyền sở hữu. |
| ↳↳ `file_name` | string | Tên file chữ ký sử dụng trong quy trình xác minh quyền sở hữu. |

### Ví dụ

#### cURL
```bash
curl -X GET "https://business-api.tiktok.com/open_api/v1.3/business/property/list/?app_id=your_app_id&secret=your_app_secret"
```

#### Python
```python
import requests

APP_ID = "your_app_id"
SECRET = "your_app_secret"

url = "https://business-api.tiktok.com/open_api/v1.3/business/property/list/"
params = {
    "app_id": APP_ID,
    "secret": SECRET
}

response = requests.get(url, params=params)
print(response.json())
```

#### Phản hồi mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20241023150000011000111222333444",
  "data": {
    "url_property_info_list": [
      {
        "file_name": "tiktok-verification-xyz.txt",
        "property_status": 1,
        "property_type": 1,
        "signature": "tiktok-property-verification-signature-token-12345",
        "url": "example.com"
      },
      {
        "file_name": "tiktok-verification-folder.txt",
        "property_status": 0,
        "property_type": 2,
        "signature": "tiktok-property-verification-signature-token-67890",
        "url": "https://www.example.com/folder/"
      }
    ]
  }
}
```

---

## Tổng quan Webhook tài khoản TikTok (`Webhooks`)
<a id="doc-1810521243195393"></a>
<!-- doc_id: 1810521243195393 -->

Hệ thống Webhook cho tài khoản TikTok cho phép ứng dụng của nhà phát triển nhận thông báo thời gian thực khi có các sự kiện phát sinh liên quan đến hoạt động của tài khoản TikTok đã ủy quyền. Cơ chế Webhook hoạt động ở cấp độ ứng dụng nhà phát triển (`app_id`), giúp bạn tự động hóa việc theo dõi tình trạng xuất bản video và quản lý bình luận trên các bài đăng.

Nhóm API này bao gồm các endpoint:
- [Tạo hoặc cập nhật cấu hình Webhook tài khoản TikTok](01-accounts-p2.md#doc-1810521279479810): Đăng ký địa chỉ URL nhận callback cho các loại sự kiện xuất bản (`VIDEO`) hoặc sự kiện bình luận (`COMMENT`), kèm theo danh sách các bài viết cụ thể cần theo dõi.
- [Lấy danh sách cấu hình Webhook tài khoản TikTok](01-accounts-p2.md#doc-1810521289122818): Tra cứu cấu hình Webhook hiện có và danh sách bài viết đang được theo dõi thông báo.
- [Xóa cấu hình Webhook tài khoản TikTok](01-accounts-p2.md#doc-1810521297052673): Xóa toàn bộ cấu hình Webhook cho một loại sự kiện hoặc gỡ bỏ các bài viết cụ thể khỏi danh sách theo dõi bình luận.

> [!NOTE]
> Để tìm hiểu chi tiết về cấu trúc dữ liệu gửi qua Webhook (payload schema), xem hướng dẫn [Đăng ký sự kiện Webhook tài khoản TikTok qua Webhooks API](../08-use-cases/use-case-webhook.md#doc-1810521730276354), [Sự kiện đăng bài](../10-organic-api/accounts-api.md#doc-1810515090228226) và [Sự kiện cập nhật bình luận](../10-organic-api/accounts-api.md#doc-1810515104773122).

---

## Tạo hoặc cập nhật cấu hình Webhook tài khoản TikTok (`Create or update a TikTok account Webhook configuration`)
<a id="doc-1810521279479810"></a>
<!-- doc_id: 1810521279479810 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/business/webhook/update/`

**Mục đích**: Tạo mới hoặc cập nhật cấu hình cho các sự kiện Webhook liên quan đến hoạt động của tài khoản TikTok ở cấp độ ứng dụng nhà phát triển. Để tìm hiểu thêm cách thiết lập cấu hình cho các sự kiện Webhook này, xem [Đăng ký sự kiện Webhook tài khoản TikTok qua Webhooks API](../08-use-cases/use-case-webhook.md#doc-1810521730276354). Nếu không muốn nhận thông báo nữa, bạn có thể xóa cấu hình Webhook bằng [/business/webhook/delete/](01-accounts-p2.md#doc-1810521297052673).

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Content-Type` | string | Có | Định dạng nội dung yêu cầu. Giá trị cho phép: `application/json`. |

### Tham số (POST: JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `app_id` | string | Có | ID của ứng dụng nhà phát triển. Để tìm **App ID**, truy cập **[My Apps](https://ads.tiktok.com/marketing_api/apps/)** > **App Detail** > **Basic Information**. |
| `secret` | string | Có | Bí mật (secret) của ứng dụng nhà phát triển. Để tìm **Secret**, truy cập **[My Apps](https://ads.tiktok.com/marketing_api/apps/)** > **App Detail** > **Basic Information**. |
| `event_type` | enum | Có | Loại sự kiện Webhook mà bạn muốn đăng ký theo dõi.<br><br>**Enum**:<br>• `VIDEO`: Các sự kiện xuất bản bài đăng (Post publishing events), cung cấp cập nhật trạng thái thời gian thực về nội dung được xuất bản qua các endpoint TikTok API cụ thể. Chi tiết về schema và payload mẫu xem tại [Sự kiện đăng bài](../10-organic-api/accounts-api.md#doc-1810515090228226).<br>• `COMMENT`: Sự kiện cập nhật bình luận (Comment update event), bao gồm sự kiện `comment.update`. Chi tiết về schema và payload mẫu xem tại [Sự kiện cập nhật bình luận](../10-organic-api/accounts-api.md#doc-1810515104773122). |
| `callback_url` | string | Có | Địa chỉ URL nhận callback khi có sự kiện phát sinh. |
| `item_list` | string[] | Không | Danh sách ID các bài viết TikTok cụ thể mà bạn muốn nhận thông báo sự kiện cập nhật bình luận.<br><br>**Quy tắc sử dụng**:<br>• Chỉ có hiệu lực khi `event_type` là `COMMENT`.<br>• Bị bỏ qua khi `event_type` là `DEFAULT` hoặc `VIDEO`.<br>• Kích thước tối đa: 100 ID bài viết.<br>• Để lấy ID bài viết thuộc tài khoản TikTok, sử dụng [/business/video/list/](01-accounts-p1.md#doc-1762228421622786).<br><br>**Hành vi khi `event_type` = `COMMENT`**:<br>1. *Khi truyền `item_list`*:<br>- Nếu ứng dụng (`app_id`) chưa từng được cấu hình `item_list` trước đó: bạn sẽ chỉ nhận thông báo `comment.update` cho các bài viết được chỉ định trong `item_list`.<br>- Nếu ứng dụng đã từng được cấu hình `item_list` trước đó: bạn sẽ nhận thông báo `comment.update` cho tất cả các bài viết đã cấu hình trước đó cộng thêm các bài viết mới chỉ định trong `item_list`.<br>2. *Khi không truyền `item_list`*:<br>- Nếu ứng dụng chưa từng cấu hình `item_list` trước đó: bạn sẽ nhận thông báo `comment.update` cho tất cả các bài viết thuộc tài khoản TikTok đã ủy quyền ứng dụng.<br>- Nếu ứng dụng đã từng cấu hình `item_list` trước đó: bạn sẽ tiếp tục nhận thông báo cho tất cả các bài viết đã cấu hình trước đó. Xem lại danh sách bài viết cụ thể qua trường `item_list` trong phản hồi. |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Xem chi tiết tại [Phụ lục mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Mã log định danh duy nhất của yêu cầu. |
| `data` | object | Dữ liệu trả về. |
| ↳ `app_id` | string | ID của ứng dụng nhà phát triển. |
| ↳ `callback_url` | string | Địa chỉ URL callback đã được cấu hình. |
| ↳ `event_type` | string | Loại sự kiện Webhook đã cấu hình (`VIDEO` hoặc `COMMENT`). |
| ↳ `item_list` | string[] | *(Chỉ trả về khi `event_type` là `COMMENT` và `item_list` được cấu hình)*. Danh sách ID các bài viết TikTok hiện đang được nhận thông báo sự kiện bình luận. |

### Ví dụ

#### cURL: Đăng ký sự kiện xuất bản bài đăng (VIDEO)
```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/business/webhook/update/" \
  -H "Content-Type: application/json" \
  -d '{
    "app_id": "your_app_id",
    "secret": "your_app_secret",
    "event_type": "VIDEO",
    "callback_url": "https://example.com/tiktok-webhook/video"
  }'
```

#### cURL: Đăng ký sự kiện bình luận (COMMENT) cho tất cả bài viết
```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/business/webhook/update/" \
  -H "Content-Type: application/json" \
  -d '{
    "app_id": "your_app_id",
    "secret": "your_app_secret",
    "event_type": "COMMENT",
    "callback_url": "https://example.com/tiktok-webhook/comment"
  }'
```

#### cURL: Đăng ký sự kiện bình luận (COMMENT) cho bài viết cụ thể
```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/business/webhook/update/" \
  -H "Content-Type: application/json" \
  -d '{
    "app_id": "your_app_id",
    "secret": "your_app_secret",
    "event_type": "COMMENT",
    "callback_url": "https://example.com/tiktok-webhook/comment",
    "item_list": [
      "7123456789123456789",
      "7123456789123456790"
    ]
  }'
```

#### Phản hồi mẫu (VIDEO)
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20241023150000011111222333444555",
  "data": {
    "app_id": "your_app_id",
    "callback_url": "https://example.com/tiktok-webhook/video",
    "event_type": "VIDEO"
  }
}
```

#### Phản hồi mẫu (COMMENT với danh sách bài viết)
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20241023150000011111222333444666",
  "data": {
    "app_id": "your_app_id",
    "callback_url": "https://example.com/tiktok-webhook/comment",
    "event_type": "COMMENT",
    "item_list": [
      "7123456789123456789",
      "7123456789123456790"
    ]
  }
}
```

---

## Lấy danh sách cấu hình Webhook tài khoản TikTok (`Get TikTok account Webhook configurations`)
<a id="doc-1810521289122818"></a>
<!-- doc_id: 1810521289122818 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/business/webhook/list/`

**Mục đích**: Lấy thông tin cấu hình hiện tại của các sự kiện Webhook liên quan đến tài khoản TikTok ở cấp độ ứng dụng nhà phát triển.

### Tham số (GET: query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `app_id` | string | Có | ID của ứng dụng nhà phát triển. Tìm tại **[My Apps](https://ads.tiktok.com/marketing_api/apps/)** > **App Detail** > **Basic Information**. |
| `secret` | string | Có | Bí mật (secret) của ứng dụng nhà phát triển. Tìm tại **[My Apps](https://ads.tiktok.com/marketing_api/apps/)** > **App Detail** > **Basic Information**. |
| `event_type` | enum | Có | Loại sự kiện Webhook muốn tra cứu cấu hình.<br><br>**Enum**:<br>• `VIDEO`: Sự kiện xuất bản bài đăng (xem chi tiết schema tại [Sự kiện đăng bài](../10-organic-api/accounts-api.md#doc-1810515090228226)).<br>• `COMMENT`: Sự kiện cập nhật bình luận (xem chi tiết schema tại [Sự kiện cập nhật bình luận](../10-organic-api/accounts-api.md#doc-1810515104773122)). |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Xem chi tiết tại [Phụ lục mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Mã log định danh duy nhất của yêu cầu. |
| `data` | object | Dữ liệu trả về. |
| ↳ `app_id` | string | ID của ứng dụng nhà phát triển. |
| ↳ `event_type` | string | Loại sự kiện Webhook đăng ký theo dõi (`VIDEO` hoặc `COMMENT`). |
| ↳ `callback_url` | string | *(Chỉ trả về khi sự kiện tương ứng đã được cấu hình cho ứng dụng)*. Địa chỉ URL callback. Nếu trường này không xuất hiện trong phản hồi, ứng dụng của bạn chưa có cấu hình Webhook cho loại sự kiện đó. |
| ↳ `item_list` | string[] | *(Chỉ trả về khi `event_type` là `COMMENT` và `item_list` đã được cấu hình)*. Danh sách ID bài viết TikTok đang nhận thông báo cập nhật bình luận. |

### Ví dụ

#### cURL
```bash
curl -X GET "https://business-api.tiktok.com/open_api/v1.3/business/webhook/list/?app_id=your_app_id&secret=your_app_secret&event_type=VIDEO"
```

#### Python
```python
import requests

APP_ID = "your_app_id"
SECRET = "your_app_secret"

url = "https://business-api.tiktok.com/open_api/v1.3/business/webhook/list/"
params = {
    "app_id": APP_ID,
    "secret": SECRET,
    "event_type": "VIDEO"
}

response = requests.get(url, params=params)
print(response.json())
```

#### Phản hồi mẫu khi đã có cấu hình
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20241023150000011222333444555666",
  "data": {
    "app_id": "your_app_id",
    "callback_url": "https://example.com/tiktok-webhook/video",
    "event_type": "VIDEO"
  }
}
```

#### Phản hồi mẫu khi chưa có cấu hình
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20241023150000011222333444555777",
  "data": {
    "app_id": "your_app_id",
    "event_type": "VIDEO"
  }
}
```

---

## Xóa cấu hình Webhook tài khoản TikTok (`Delete a TikTok account Webhook configuration`)
<a id="doc-1810521297052673"></a>
<!-- doc_id: 1810521297052673 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/business/webhook/delete/`

**Mục đích**: Xóa cấu hình sự kiện Webhook của tài khoản TikTok ở cấp độ ứng dụng nhà phát triển, hoặc gỡ bỏ các bài viết TikTok cụ thể khỏi danh sách nhận thông báo sự kiện bình luận.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Content-Type` | string | Có | Định dạng nội dung yêu cầu. Giá trị cho phép: `application/json`. |

### Tham số (POST: JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `app_id` | string | Có | ID của ứng dụng nhà phát triển. Tìm tại **[My Apps](https://ads.tiktok.com/marketing_api/apps/)** > **App Detail** > **Basic Information**. |
| `secret` | string | Có | Bí mật (secret) của ứng dụng nhà phát triển. Tìm tại **[My Apps](https://ads.tiktok.com/marketing_api/apps/)** > **App Detail** > **Basic Information**. |
| `event_type` | enum | Có | Loại cấu hình sự kiện Webhook bạn muốn xóa.<br><br>**Enum**:<br>• `VIDEO`: Xóa cấu hình sự kiện đăng bài (xem chi tiết tại [Sự kiện đăng bài](../10-organic-api/accounts-api.md#doc-1810515090228226)).<br>• `COMMENT`: Xóa cấu hình hoặc bài viết khỏi sự kiện cập nhật bình luận (xem chi tiết tại [Sự kiện cập nhật bình luận](../10-organic-api/accounts-api.md#doc-1810515104773122)). |
| `item_list` | string[] | Không | *(Chỉ áp dụng khi `event_type` là `COMMENT`)*. Danh sách ID các bài viết TikTok cụ thể mà bạn không còn muốn nhận thông báo bình luận nữa. Kích thước tối đa: 100 ID.<br><br>Để lấy danh sách bài viết hiện có trong cấu hình, dùng [/business/webhook/list/](01-accounts-p2.md#doc-1810521289122818).<br><br>**Quy tắc thực hiện**:<br>• *Nếu có cung cấp `item_list`*: Bạn sẽ ngừng nhận thông báo sự kiện `comment.update` cho **chính xác các bài viết được chỉ định**.<br>• *Nếu không cung cấp `item_list`*: Bạn sẽ ngừng nhận thông báo sự kiện `comment.update` cho **tất cả bài viết** thuộc các tài khoản TikTok đã ủy quyền cho ứng dụng (`app_id`). |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Xem chi tiết tại [Phụ lục mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Mã log định danh duy nhất của yêu cầu. |
| `data` | object | Dữ liệu trả về. |
| ↳ `app_id` | string | ID của ứng dụng nhà phát triển. |
| ↳ `event_type` | string | Loại cấu hình sự kiện Webhook (`VIDEO` hoặc `COMMENT`). |
| ↳ `item_list` | string[] | *(Chỉ trả về khi `event_type` là `COMMENT` và vẫn còn bài viết được cấu hình sau khi xóa)*. Danh sách ID các bài viết TikTok còn lại vẫn sẽ tiếp tục nhận thông báo sự kiện bình luận. Ví dụ: trước đây bạn cấu hình danh sách gồm bài viết 1 và 2, sau đó bạn gửi yêu cầu xóa bài viết 1 qua `item_list`, trường này trong phản hồi sẽ trả về danh sách chứa bài viết 2. |

### Ví dụ

#### cURL: Xóa cấu hình Webhook sự kiện đăng bài (VIDEO)
```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/business/webhook/delete/" \
  -H "Content-Type: application/json" \
  -d '{
    "app_id": "your_app_id",
    "secret": "your_app_secret",
    "event_type": "VIDEO"
  }'
```

#### cURL: Gỡ bài viết cụ thể khỏi sự kiện bình luận (COMMENT)
```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/business/webhook/delete/" \
  -H "Content-Type: application/json" \
  -d '{
    "app_id": "your_app_id",
    "secret": "your_app_secret",
    "event_type": "COMMENT",
    "item_list": [
      "7123456789123456789"
    ]
  }'
```

#### Phản hồi mẫu khi xóa cấu hình VIDEO
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20241023150000011333444555666777",
  "data": {
    "app_id": "your_app_id",
    "event_type": "VIDEO"
  }
}
```

#### Phản hồi mẫu khi gỡ bài viết khỏi cấu hình COMMENT
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20241023150000011333444555666888",
  "data": {
    "app_id": "your_app_id",
    "event_type": "COMMENT",
    "item_list": [
      "7123456789123456790"
    ]
  }
}
```
