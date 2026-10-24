# Lượt nhắc (Mentions)

> Phân hệ: apiref:Mentions.
> Tài liệu biên dịch kỹ thuật chi tiết theo chuẩn TikTok Business API v1.3.

---

## Mục lục điều hướng
- [1. Lượt nhắc (Mentions) (#doc-1825107837430850)](#doc-1825107837430850)
- [2. Lấy top 1000 bài đăng được nhắc đến (#doc-1825107955294402)](#doc-1825107955294402)
- [3. Lấy thông tin chi tiết bài đăng được nhắc đến từ webhook (#doc-1831359360477185)](#doc-1831359360477185)
- [4. Lấy từ khóa thường dùng trong top 1000 bài đăng được nhắc đến (#doc-1825107971247170)](#doc-1825107971247170)
- [5. Lấy hashtag thường dùng trong top 1000 bài đăng được nhắc đến (#doc-1825107978583042)](#doc-1825107978583042)
- [6. Lấy nội dung lượt nhắc cho top 1000 bài đăng hashtag thương hiệu (#doc-1825108001123522)](#doc-1825108001123522)
- [7. Lấy danh sách hashtag thương hiệu hợp lệ cho tài khoản TikTok (#doc-1833862470219842)](#doc-1833862470219842)
- [8. Kích hoạt hashtag thương hiệu cho tài khoản TikTok (#doc-1833831427732481)](#doc-1833831427732481)
- [9. Lấy danh sách hashtag thương hiệu đã kích hoạt cho tài khoản TikTok (#doc-1833832557996034)](#doc-1833832557996034)
- [10. Xóa hashtag thương hiệu đã kích hoạt cho tài khoản TikTok (#doc-1833833401871362)](#doc-1833833401871362)
- [11. Lấy top 1000 lượt nhắc trong bình luận bài đăng (#doc-1825107985360898)](#doc-1825107985360898)
- [12. Lấy thông tin chi tiết lượt nhắc bình luận từ webhook (#doc-1831358502098946)](#doc-1831358502098946)
- [13. Phản hồi lượt nhắc trong bình luận (#doc-1825107991945218)](#doc-1825107991945218)
- [14. Tạo cấu hình Webhook cho Mentions (#doc-1825108008121346)](#doc-1825108008121346)
- [15. Lấy cấu hình Webhook cho Mentions (#doc-1825108014565442)](#doc-1825108014565442)
- [16. Xóa cấu hình Webhook cho Mentions (#doc-1825108021550082)](#doc-1825108021550082)

---

<a id="doc-1825107837430850"></a>
<!-- doc_id: 1825107837430850 -->
<!-- doc_id: 1825107837430850 -->
# Lượt nhắc (Mentions)
> Đường dẫn: API Reference > Mentions
Mentions API là bộ công cụ giám sát lượt nhắc đến và phân tích các cuộc trò chuyện của cộng đồng về doanh nghiệp của bạn trên TikTok. Bằng cách cung cấp những hiểu biết sâu sắc về thảo luận cộng đồng, phản hồi của khách hàng và các xu hướng mạng xã hội, Mentions API giúp bạn cải thiện chiến lược tiếp thị và củng cố sự hiện diện thương hiệu trên nền tảng TikTok.

Bạn có thể tham khảo [Hướng dẫn](../10-organic-api/mentions-api.md#doc-1825103402321025) để tìm hiểu thêm về quy trình ủy quyền, xác thực tài khoản, giới hạn tần suất gọi API và nhiều thông tin khác.

## Cấu hình Webhook (Webhook Configuration)
- [Tạo cấu hình Webhook cho Mentions](51-mentions.md#doc-1825108008121346)
- [Lấy cấu hình Webhook cho Mentions](51-mentions.md#doc-1825108014565442)
- [Xóa cấu hình Webhook cho Mentions](51-mentions.md#doc-1825108021550082)

## Xử lý lượt nhắc (Handle mentions)
- [Lấy top 1000 bài đăng được nhắc đến](51-mentions.md#doc-1825107955294402)
- [Lấy thông tin chi tiết bài đăng được nhắc đến từ webhook](51-mentions.md#doc-1831359360477185)
- [Lấy các hashtag phổ biến trong top 1000 bài đăng được nhắc đến](51-mentions.md#doc-1825107971247170)
- [Lấy các từ khóa phổ biến trong top 1000 bài đăng được nhắc đến](51-mentions.md#doc-1825107978583042)
- [Lấy top 1000 lượt nhắc trong bình luận bài đăng](51-mentions.md#doc-1825107985360898)
- [Lấy thông tin chi tiết lượt nhắc bình luận từ webhook](51-mentions.md#doc-1831358502098946)
- [Phản hồi lượt nhắc trong bình luận](51-mentions.md#doc-1825107991945218)

## Lượt nhắc hashtag thương hiệu (Brand hashtag mentions)
- [Lấy danh sách hashtag thương hiệu hợp lệ cho tài khoản TikTok](51-mentions.md#doc-1833862470219842)
- [Kích hoạt hashtag thương hiệu cho tài khoản TikTok](51-mentions.md#doc-1833831427732481)
- [Lấy toàn bộ hashtag thương hiệu đã kích hoạt cho tài khoản TikTok](51-mentions.md#doc-1833832557996034)
- [Lấy nội dung lượt nhắc cho top 1000 bài đăng hashtag thương hiệu](51-mentions.md#doc-1825108001123522)
- [Xóa hashtag thương hiệu đã kích hoạt cho tài khoản TikTok](51-mentions.md#doc-1833833401871362)

---

<a id="doc-1825107955294402"></a>
<!-- doc_id: 1825107955294402 -->
<!-- doc_id: 1825107955294402 -->
# Lấy top 1000 bài đăng được nhắc đến (Get top 1000 mentioned posts)
> Đường dẫn: API Reference > Lượt nhắc > Lấy top 1000 bài đăng được nhắc đến
Sử dụng endpoint này để truy xuất danh sách tối đa 1.000 bài đăng có gắn thẻ (nhắc đến) tài khoản TikTok trong chú thích bài đăng. 

Theo mặc định, danh sách tối đa 1.000 bài đăng trả về sẽ được sắp xếp theo số lượt thích cao nhất trong số tất cả các bài đăng nhắc đến tên người dùng (handle) của doanh nghiệp. Mỗi yêu cầu có thể lấy tối đa 100 bài đăng. Nếu cần nhiều kết quả hơn, bạn có thể thực hiện nhiều yêu cầu phân trang bằng con trỏ (cursor). Ngoài ra, bạn có thể linh hoạt thiết lập thứ tự sắp xếp bằng các tham số `sort_field` và `sort_type`. 

Lưu ý rằng danh sách bài đăng trả về chỉ giới hạn ở mức 1.000 bài đăng hàng đầu, ngay cả khi thực tế có hơn 1.000 bài đăng nhắc đến tên tài khoản doanh nghiệp.

Để xuất hiện trong kết quả tìm kiếm, một bài đăng phải đáp ứng các tiêu chí sau:
- Trạng thái hiển thị: Bài đăng phải ở chế độ công khai.
- Lượt nhắc: Bài đăng phải nhắc trực tiếp (@) tên người dùng của doanh nghiệp trong phần chú thích.
- Khung thời gian tra cứu: Bài đăng phải được đăng trong vòng 90 ngày qua.
- Độ tuổi người dùng: Bài đăng không thuộc về người dùng chưa đủ tuổi hoặc không xác định độ tuổi. Đối với người dùng ở Châu Âu, độ tuổi từ 17 trở xuống được coi là chưa đủ tuổi, trong khi đối với người dùng ở Hoa Kỳ và các quốc gia hoặc khu vực khác, độ tuổi từ 12 trở xuống được coi là chưa đủ tuổi.

## Điều kiện tiên quyết trước khi bắt đầu
- Đảm bảo tài khoản TikTok là Tài khoản TikTok có Quyền truy cập Nâng cao hoặc Tài khoản Doanh nghiệp Đã xác minh (VBA). Tìm hiểu thêm [về quyền hạn tài khoản TikTok](https://ads.tiktok.com/resources/help/article/about-tiktok-account-entitlements). Để xác nhận điều này, sử dụng [/business/get/](01-accounts-p1.md#doc-1762228399168514) và kiểm tra xem tham số phản hồi `has_advanced_access` có phải là `true` đối với tài khoản TikTok hay không.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/business/mention/video/list/

**Method** GET

**Required permission scope**: `biz.brand.insights`

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền bởi tài khoản TikTok (Access Token). ⏎ Để lấy access token, hãy sử dụng [/tt_user/oauth2/token/](../10-organic-api/accounts-api.md#doc-1738084387220481). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
|business_id ***(Bắt buộc)***|string|Mã định danh duy nhất của tài khoản TikTok đối với ứng dụng cụ thể.<br><br>Bạn có thể lấy mã này qua trường `open_id` trả về từ [/tt_user/oauth2/token/](../10-organic-api/accounts-api.md#doc-1738084387220481).|
|fields|string[]|Requested fields. <br>If `fields` is not set, only the <b>default</b> fields will be returned.<br><br>Giá trị mặc định: `["item_id","caption"]`. <br><br><b>Supported fields</b>:<ul><li>`item_id`: Mã định danh duy nhất của bài đăng.</li><li>`create_time`: Thời điểm bài đăng được xuất bản (định dạng Unix timestamp UTC).</li><li>`video_link`: Đường dẫn URL chung tới bài đăng trên TikTok.</li><li>`caption`: Nội dung chú thích (caption) của bài đăng.</li><li>`likes`: Tổng số lượt thích của bài đăng.</li><li>`comments`: Tổng số lượt bình luận của bài đăng.</li><li>`shares`: Tổng số lượt chia sẻ bài đăng.</li><li>`thumbnail_url`: Đường dẫn URL hình ảnh thu nhỏ (thumbnail) của bài đăng.</li><li>`views`: Tổng số lượt xem bài đăng.</li><li>`reach`: Tổng số người xem duy nhất (reach) đã xem bài đăng.</li><li>`creator_handle_name`: Tên người dùng (handle name) của nhà sáng tạo đã xuất bản bài đăng.</li></ul>|
|sort_field|string|Trường dùng để sắp xếp kết quả.<br><br>Các giá trị enum hỗ trợ: <ul><li>`CREATE_TIME`: The field `create_time`.</li><li>`LIKES`: The field `likes`.</li><li>`COMMENTS`: The field `comments`.</li><li>`SHARES`: The field `shares`.</li></ul>Giá trị mặc định: `CREATE_TIME`.|
|sort_type|string|Thứ tự sắp xếp kết quả.<br><br>Các giá trị enum hỗ trợ: <ul><li>`ASC`: Ascending.</li><li>`DESC`: Descending.</li></ul>Giá trị mặc định: `DESC`.|
|number_of_days|number|Khoảng thời gian tra cứu dữ liệu quá khứ, tính theo số ngày.<br><br>Value range: 1-90.<br>Giá trị mặc định: 90.<br><br>For instance, if you set this field to 90, the results for the last 90 days will be retrieved.|
|regions|string[]|Khu vực của các bài đăng được nhắc đến mà bạn muốn lọc kết quả.<br><br><ul><li>If you specify this field, only the mentioned posts published by TikTok users registered in the specified regions will be returned.</li><li>If this field is not specified, all mentioned posts will be returned.</li></ul><br>To learn about the allowed values for this field, refer to [List of values for `regions`](../10-organic-api/mentions-api.md#doc-1825107519114241).|
|cursor|integer|Con trỏ phục vụ phân trang (cursor). Vị trí của kết quả bạn muốn bắt đầu lấy dữ liệu.<br><br>For instance, setting `cursor` to 10 means you want to retrieve the next page of results after the 10th position.<br><br>If the response parameter `has_more` is `true`, pass the returned cursor in this parameter in the subsequent request to receive the next page of results.<br><br>Giá trị mặc định: 0.|
|max_count|integer|Số lượng bình luận tối đa được trả về trên mỗi trang dữ liệu.<br><br>Giá trị mặc định: 100.<br>Value range: 1-100.<br><br><p><span style="color:darkred"><b>Note</b></span>: Due to our trust and safety policies, it is possible that the endpoint returns less than the `max_count` number of comments even if the response parameter `has_more` is `true`.|

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/business/mention/video/list/?business_id={{business_id}}&fields=["item_id", "video_link", "caption", "likes", "comments", "shares", "create_time","thumbnail_url","views","reach","creator_handle_name"]&sort_field=SHARES&sort_type=DESC&number_of_days=90&regions=["US"]' \
--header 'Access-Token: {{Access-Token}}' \
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|code |number|Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Phụ lục - Mã trạng thái phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message|string|Thông báo phản hồi từ hệ thống. Xem [Phụ lục - Mã lỗi trả về](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|request_id |string|Mã nhật ký yêu cầu (request log ID) để định danh duy nhất cho mỗi lượt gọi API.  |
|data|object|Dữ liệu trả về.|
#|videos|object[]|Information about the mentioned posts.|
##|item_id|string|Mã định danh duy nhất của bài đăng.<br><br>Example: `6995316737801538821`.|
##|create_time|string|Unix/epoch date-time when the post was posted, in UTC timezone.<br><br>Example: `1628461703`.|
##|video_link|string|URL chung của bài đăng, có định dạng `https://www.tiktok.com/@/video/&#123;item_id&#125;`.<br><br>Example: `https://www.tiktok.com/@/video/7231234123412341234`.|
##|caption|string|Post description.<br><br>Example: `Nuki: me and me casa 🏠 #cat #kitten #britishshorthair`.|
##|likes|number|Tổng số lượt thích của bài đăng.<br><br>Example: 243.|
##|comments|number|Tổng số lượt bình luận của bài đăng.<br><br>Example: 10.|
##|shares|number|Tổng số lượt chia sẻ bài đăng.<br><br>Example: 10.|
##|thumbnail_url|string|Đường dẫn URL hình ảnh thu nhỏ (thumbnail) của bài đăng.<br><br>Thời hạn hiệu lực: 48 giờ.<br>Thời gian hết hạn được đưa vào URL sau tham số `x-expires`, theo định dạng dấu thời gian Epoch/Unix tính bằng giây.<br><br>Example: `https://p16-sign-sg.tiktokcdn.com/tos-maliva-p-0068/1f9a445423844b82bd79317b42b9953f~c5_300x400.webp?x-expires=1614034800&x-signature=qChosOGafzBcTctPm9zYiF8Y2MA%3D`.<br><br><p><span style="color:darkred"><b>Lưu ý</b></span>: Đối với bài đăng ảnh trên TikTok, giá trị của trường này sẽ là một chuỗi rỗng (`""`).|
##|creator_handle_name|string|Tên người dùng (handle name) của nhà sáng tạo đã xuất bản bài đăng.|
##|views|number|Tổng số lượt xem bài đăng.<br><br><p><span style="color:darkred"><b>Note</b></span>: If the number of views the post has received is less than 1,000, the value of this field will be null.|
##|reach|number|Tổng số người xem duy nhất (reach) đã xem bài đăng.<br><br><p><span style="color:darkred"><b>Note</b></span>: If the number of unique viewers who viewed the post is less than 1,000, the value of this field will be null.|
#|cursor|number|Cursor for the next page of results, to be passed in the `cursor` query parameter of the subsequent API request.|
#|has_more|boolean|Cho biết có còn trang dữ liệu tiếp theo hay không (`true` nếu còn, `false` nếu hết).|

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "has_more": false,
        "cursor": 100,
        "videos": [
            {
                "video_link": "{{video_link}}",
                "likes": 50,
                "item_id": "{{item_id}}",
                "create_time": "1689481495",
                "shares": 253,
                "comments": 101,
                "caption": "{{caption}}",
                "thumbnail_url": "{{thumbnail_url}}",
                "views": 2000,
                "reach": 2000,
                "creator_handle_name": "{{creator_handle_name}}"
            },
            {
                "video_link": "{{video_link}}",
                "likes": 100,
                "item_id": "{{item_id}}",
                "create_time": "1689481495",
                "shares": 53,
                "comments": 151,
                "caption": "{{caption}}",
                "thumbnail_url": "{{thumbnail_url}}",
                "views": null,
                "reach": null,
                "creator_handle_name": "{{creator_handle_name}}"
            }
        ]
    }
}
```

---

<a id="doc-1831359360477185"></a>
<!-- doc_id: 1831359360477185 -->
<!-- doc_id: 1831359360477185 -->
# Lấy thông tin chi tiết bài đăng được nhắc đến từ webhook (Get details of mentioned post)
> Đường dẫn: API Reference > Lượt nhắc > Lấy thông tin chi tiết bài đăng được nhắc đến từ webhook
Sử dụng endpoint này để truy xuất the details of a mentioned post obtained from [the mentions webhook](../08-use-cases/use-case-webhook.md#doc-1825113658431489), enabling real-time monitoring of business mentions within post captions. A mentioned post refers to any post that mentions a business in the post caption.  

> **Note:** 
> Hãy truy xuất thông tin chi tiết trong vòng 48 giờ kể từ khi nhận được webhook để đảm bảo tính khả dụng của dữ liệu.

## Điều kiện tiên quyết trước khi bắt đầu
- Đảm bảo tài khoản TikTok là Tài khoản TikTok có Quyền truy cập Nâng cao hoặc Tài khoản Doanh nghiệp Đã xác minh (VBA). Tìm hiểu thêm [về quyền hạn tài khoản TikTok](https://ads.tiktok.com/resources/help/article/about-tiktok-account-entitlements). Để xác nhận điều này, sử dụng [/business/get/](01-accounts-p1.md#doc-1762228399168514) và kiểm tra xem tham số phản hồi `has_advanced_access` có phải là `true` đối với tài khoản TikTok hay không.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/business/mention/video/get/

**Method** GET

**Required permission scope**: `biz.brand.insights`

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền bởi tài khoản TikTok (Access Token). ⏎ Để lấy access token, hãy sử dụng [/tt_user/oauth2/token/](../10-organic-api/accounts-api.md#doc-1738084387220481). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
|business_id ***(Bắt buộc)***|string|Mã định danh duy nhất của tài khoản TikTok đối với ứng dụng cụ thể.<br><br>Bạn có thể lấy mã này qua trường `open_id` trả về từ [/tt_user/oauth2/token/](../10-organic-api/accounts-api.md#doc-1738084387220481).|
|item_id***(Bắt buộc)***|string|ID của bài đăng mà bình luận được đăng tải.<br><br>Pass the post ID as obtained from `video_id` within the [`content` of the mentions webhook event](../08-use-cases/use-case-webhook.md#doc-1825113658431489).|
|fields|string[]|Requested fields. <br>If `fields` is not set, only the <b>default</b> fields will be returned.<br><br>Giá trị mặc định: `["item_id","caption"]`. <br><br><b>Supported fields</b>:<ul><li>`item_id`: Mã định danh duy nhất của bài đăng.</li><li>`create_time`: Thời điểm bài đăng được xuất bản (định dạng Unix timestamp UTC).</li><li>`video_link`: Đường dẫn URL chung tới bài đăng trên TikTok.</li><li>`caption`: Nội dung chú thích (caption) của bài đăng.</li><li>`likes`: Tổng số lượt thích của bài đăng.</li><li>`comments`: Tổng số lượt bình luận của bài đăng.</li><li>`shares`: Tổng số lượt chia sẻ bài đăng.</li><li>`thumbnail_url`: Đường dẫn URL hình ảnh thu nhỏ (thumbnail) của bài đăng.</li><li>`views`: Tổng số lượt xem bài đăng.</li><li>`reach`: Tổng số người xem duy nhất (reach) đã xem bài đăng.</li><li>`creator_handle_name`: Tên người dùng (handle name) của nhà sáng tạo đã xuất bản bài đăng.</li></ul>|

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/business/mention/video/get/?business_id={{business_id}}&fields=["item_id", "video_link", "caption", "likes", "comments", "shares", "create_time","thumbnail_url","views","reach","creator_handle_name"]' \
--header 'Access-Token: {{Access-Token}}' \
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|code |number|Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Phụ lục - Mã trạng thái phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message|string|Thông báo phản hồi từ hệ thống. Xem [Phụ lục - Mã lỗi trả về](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|request_id |string|Mã nhật ký yêu cầu (request log ID) để định danh duy nhất cho mỗi lượt gọi API.  |
|data|object|Dữ liệu trả về.|
#|video|object[]|Information about the mentioned post.|
##|item_id|string|Mã định danh duy nhất của bài đăng.<br><br>Example: `6995316737801538821`.|
##|create_time|string|Unix/epoch date-time when the post was posted, in UTC timezone.<br><br>Example: `1628461703`.|
##|video_link|string|URL chung của bài đăng, có định dạng `https://www.tiktok.com/@/video/&#123;item_id&#125;`.<br><br>Example: `https://www.tiktok.com/@/video/7231234123412341234`.|
##|caption|string|Post description.<br><br>Example: `Nuki: me and me casa 🏠 #cat #kitten #britishshorthair`.|
##|likes|number|Tổng số lượt thích của bài đăng.<br><br>Example: 243.|
##|comments|number|Tổng số lượt bình luận của bài đăng.<br><br>Example: 10.|
##|shares|number|Tổng số lượt chia sẻ bài đăng.<br><br>Example: 10.|
##|thumbnail_url|string|Đường dẫn URL hình ảnh thu nhỏ (thumbnail) của bài đăng.<br><br>Thời hạn hiệu lực: 48 giờ.<br>Thời gian hết hạn được đưa vào URL sau tham số `x-expires`, theo định dạng dấu thời gian Epoch/Unix tính bằng giây.<br><br>Example: `https://p16-sign-sg.tiktokcdn.com/tos-maliva-p-0068/1f9a445423844b82bd79317b42b9953f~c5_300x400.webp?x-expires=1614034800&x-signature=qChosOGafzBcTctPm9zYiF8Y2MA%3D`.<br><br><p><span style="color:darkred"><b>Lưu ý</b></span>: Đối với bài đăng ảnh trên TikTok, giá trị của trường này sẽ là một chuỗi rỗng (`""`).|
##|creator_handle_name|string|Tên người dùng (handle name) của nhà sáng tạo đã xuất bản bài đăng.|
##|views|number|Tổng số lượt xem bài đăng.<br><br><p><span style="color:darkred"><b>Note</b></span>: If the number of views the post has received is less than 1,000, the value of this field will be null.|
##|reach|number|Tổng số người xem duy nhất (reach) đã xem bài đăng.<br><br><p><span style="color:darkred"><b>Note</b></span>: If the number of unique viewers who viewed the post is less than 1,000, the value of this field will be null.|

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "video": 
            {
                "video_link": "{{video_link}}",
                "likes": 50,
                "item_id": "{{item_id}}",
                "create_time": "1689481495",
                "shares": 253,
                "comments": 101,
                "caption": "{{caption}}",
                "thumbnail_url": "{{thumbnail_url}}",
                "views": 2000,
                "reach": 2000,
                "creator_handle_name": "{{creator_handle_name}}"
            },
            {
                "video_link": "{{video_link}}",
                "likes": 100,
                "item_id": "{{item_id}}",
                "create_time": "1689481495",
                "shares": 53,
                "comments": 151,
                "caption": "{{caption}}",
                "thumbnail_url": "{{thumbnail_url}}",
                "views": null,
                "reach": null,
                "creator_handle_name": "{{creator_handle_name}}"
            }
    }
}
```

---

<a id="doc-1825107971247170"></a>
<!-- doc_id: 1825107971247170 -->
<!-- doc_id: 1825107971247170 -->
# Lấy từ khóa thường dùng trong top 1000 bài đăng được nhắc đến (Get frequent keywords)
> Đường dẫn: API Reference > Lượt nhắc > Lấy từ khóa thường dùng trong top 1000 bài đăng được nhắc đến
Sử dụng endpoint này để truy xuất 20 từ khóa hàng đầu trong chú thích của các bài đăng được nhắc đến. 

Để xuất hiện trong kết quả tìm kiếm, từ khóa phải đáp ứng các yêu cầu sau:
- Loại tài khoản: Tài khoản TikTok phải là Tài khoản TikTok có Quyền truy cập Nâng cao hoặc Tài khoản Doanh nghiệp Đã xác minh (VBA). Tìm hiểu thêm [về quyền hạn tài khoản TikTok](https://ads.tiktok.com/resources/help/article/about-tiktok-account-entitlements). Để xác nhận điều này, sử dụng [/business/get/](01-accounts-p1.md#doc-1762228399168514) và kiểm tra xem tham số phản hồi `has_advanced_access` có phải là `true` đối với tài khoản TikTok hay không.
- Post: The keyword appears in a post that is public, explicitly mentions (@) the business in the caption, and has been posted within the past 90 days. Additionally, the user who posted the post is not underage or of an unknown age. Đối với người dùng ở Châu Âu, độ tuổi từ 17 trở xuống được coi là chưa đủ tuổi, trong khi đối với người dùng ở Hoa Kỳ và các quốc gia hoặc khu vực khác, độ tuổi từ 12 trở xuống được coi là chưa đủ tuổi.
- Tần suất: Từ khóa là một trong 20 từ khóa được nhắc đến nhiều nhất trong chú thích của các bài đăng được nhắc đến. 

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/business/mention/top_word/list/

**Method** GET

**Required permission scope**: `biz.brand.insights`

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền bởi tài khoản TikTok (Access Token). ⏎ Để lấy access token, hãy sử dụng [/tt_user/oauth2/token/](../10-organic-api/accounts-api.md#doc-1738084387220481). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
|business_id ***(Bắt buộc)***|string|Mã định danh duy nhất của tài khoản TikTok đối với ứng dụng cụ thể.<br><br>Bạn có thể lấy mã này qua trường `open_id` trả về từ [/tt_user/oauth2/token/](../10-organic-api/accounts-api.md#doc-1738084387220481).|
|regions|string[]|Khu vực của các bài đăng được nhắc đến mà bạn muốn lọc kết quả.<br><br><ul><li>If you specify this field, only the top keywords in mentioned posts posted by TikTok users registered in the specified regions will be returned.</li><li>If this field is not specified, the top keywords in all mentioned posts will be returned.</li></ul><br>To learn about the allowed values for this field, refer to [List of values for `regions`](../10-organic-api/mentions-api.md#doc-1825107519114241).|

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/business/mention/top_word/list/?business_id={{business_id}}&regions=["US"]' \
--header 'Access-Token: {{Access-Token}}' \
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|code |number|Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Phụ lục - Mã trạng thái phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message|string|Thông báo phản hồi từ hệ thống. Xem [Phụ lục - Mã lỗi trả về](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|request_id |string|Mã nhật ký yêu cầu (request log ID) để định danh duy nhất cho mỗi lượt gọi API.  |
|data |object|Dữ liệu trả về.|
#|results| object[] |Kết quả 20 từ khóa hàng đầu trong các bài đăng được nhắc đến.|
##|word| string |A word or phrase that appears frequently in the captions of mentioned posts.<br><br>Example: `fashion`.|
##|count| number |Tần suất xuất hiện của từ hoặc cụm từ.|

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "results": [
            {
                "word": "{{word}}",
                "count": 72
            },
            {
                "word": "{{word}}",
                "count": 31
            },
            {
                "word": "{{word}}",
                "count": 24
            },
            {
                "word": "{{word}}",
                "count": 17
            },
            {
                "word": "{{word}}",
                "count": 13
            }
        ]
    }
}
```

---

<a id="doc-1825107978583042"></a>
<!-- doc_id: 1825107978583042 -->
<!-- doc_id: 1825107978583042 -->
# Lấy hashtag thường dùng trong top 1000 bài đăng được nhắc đến (Get frequent hashtags)
> Đường dẫn: API Reference > Lượt nhắc > Lấy hashtag thường dùng trong top 1000 bài đăng được nhắc đến
Sử dụng endpoint này để truy xuất 20 hashtag hàng đầu trong chú thích của các bài đăng được nhắc đến. 

Để xuất hiện trong kết quả tìm kiếm, hashtag phải đáp ứng các yêu cầu sau:
- Loại tài khoản: Tài khoản TikTok phải là Tài khoản TikTok có Quyền truy cập Nâng cao hoặc Tài khoản Doanh nghiệp Đã xác minh (VBA). Tìm hiểu thêm [về quyền hạn tài khoản TikTok](https://ads.tiktok.com/resources/help/article/about-tiktok-account-entitlements). Để xác nhận điều này, sử dụng [/business/get/](01-accounts-p1.md#doc-1762228399168514) và kiểm tra xem tham số phản hồi `has_advanced_access` có phải là `true` đối với tài khoản TikTok hay không.
- Post: The hashtag appears in a post that is public, explicitly mentions (@) the business in the caption, and has been posted within the past 90 days. Additionally, the user who posted the post is not underage or of an unknown age. Đối với người dùng ở Châu Âu, độ tuổi từ 17 trở xuống được coi là chưa đủ tuổi, trong khi đối với người dùng ở Hoa Kỳ và các quốc gia hoặc khu vực khác, độ tuổi từ 12 trở xuống được coi là chưa đủ tuổi.
- Tần suất: Hashtag là một trong 20 hashtag được sử dụng nhiều nhất trong chú thích của các bài đăng được nhắc đến. 

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/business/mention/top_hashtag/list/

**Method** GET

**Required permission scope**: `biz.brand.insights`

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền bởi tài khoản TikTok (Access Token). ⏎ Để lấy access token, hãy sử dụng [/tt_user/oauth2/token/](../10-organic-api/accounts-api.md#doc-1738084387220481). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
|business_id ***(Bắt buộc)***|string|Mã định danh duy nhất của tài khoản TikTok đối với ứng dụng cụ thể.<br><br>Bạn có thể lấy mã này qua trường `open_id` trả về từ [/tt_user/oauth2/token/](../10-organic-api/accounts-api.md#doc-1738084387220481).|
|regions|string[]|Khu vực của các bài đăng được nhắc đến mà bạn muốn lọc kết quả.<br><br><ul><li>If you specify this field, only the top hashtags in mentioned posts posted by TikTok users registered in the specified regions will be returned.</li><li>If this field is not specified, the top hashtags in all mentioned posts will be returned.</li></ul><br>To learn about the allowed values for this field, refer to [List of values for `regions`](../10-organic-api/mentions-api.md#doc-1825107519114241).|

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/business/mention/top_hashtag/list/?business_id={{business_id}}&regions=["US"]' \
--header 'Access-Token: {{Access-Token}}' \
```
## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|code |number|Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Phụ lục - Mã trạng thái phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message|string|Thông báo phản hồi từ hệ thống. Xem [Phụ lục - Mã lỗi trả về](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|request_id |string|Mã nhật ký yêu cầu (request log ID) để định danh duy nhất cho mỗi lượt gọi API.  |
|data |object|Dữ liệu trả về.|
#|results| object[] |Kết quả 20 hashtag hàng đầu trong các bài đăng được nhắc đến.|
##|hashtag| string |A hashtag that appears frequently in the captions of mentioned posts.<br><br>Example: `fashion`.|
##|count| number |Tần suất xuất hiện của hashtag.|

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "results": [
            {
                "count": 72,
                "hashtag": "{{hashtag}}"
            },
            {
                "count": 31,
                "hashtag": "{{hashtag}}"
            },
            {
                "count": 24,
                "hashtag": "{{hashtag}}"
            },
            {
                "count": 17,
                "hashtag": "{{hashtag}}"
            },
            {
                "count": 13,
                "hashtag": "{{hashtag}}"
            }
        ]
    }
}
```

---

<a id="doc-1825108001123522"></a>
<!-- doc_id: 1825108001123522 -->
<!-- doc_id: 1825108001123522 -->
# Lấy nội dung lượt nhắc cho top 1000 bài đăng hashtag thương hiệu (Get mention content)
> Đường dẫn: API Reference > Lượt nhắc > Lấy nội dung lượt nhắc cho top 1000 bài đăng hashtag thương hiệu
Sử dụng endpoint này để truy xuất up to 1,000 posts containing one or more brand hashtags, hashtags you’ve enabled for your business (up to 50, managed via [/business/mention/hashtag/verify/list/](51-mentions.md#doc-1833862470219842) and [/business/mention/hashtag/add/](51-mentions.md#doc-1833831427732481)). If more than 1,000 posts contain brand hashtags, only the 1,000 posts with the most likes are returned. You can use this endpoint either to get the top 1,000 posts across all your enabled hashtags combined, or to get the top 1,000 posts for a specific enabled hashtag.

Để xuất hiện trong kết quả tìm kiếm, bài đăng phải đáp ứng các yêu cầu sau:
- Trạng thái hiển thị: Bài đăng phải ở chế độ công khai.
- Hashtag thương hiệu: Chú thích bài đăng chứa một hoặc nhiều hashtag thương hiệu đã được kích hoạt. 
- Khung thời gian tra cứu: Bài đăng phải được đăng trong vòng 90 ngày qua.
- Độ tuổi người dùng: Bài đăng không thuộc về người dùng chưa đủ tuổi hoặc không xác định độ tuổi. Đối với người dùng ở Châu Âu, độ tuổi từ 17 trở xuống được coi là chưa đủ tuổi, trong khi đối với người dùng ở Hoa Kỳ và các quốc gia hoặc khu vực khác, độ tuổi từ 12 trở xuống được coi là chưa đủ tuổi.

## Điều kiện tiên quyết trước khi bắt đầu
- Đảm bảo tài khoản TikTok là Tài khoản TikTok có Quyền truy cập Nâng cao hoặc Tài khoản Doanh nghiệp Đã xác minh (VBA). Tìm hiểu thêm [về quyền hạn tài khoản TikTok](https://ads.tiktok.com/resources/help/article/about-tiktok-account-entitlements). Để xác nhận điều này, sử dụng [/business/get/](01-accounts-p1.md#doc-1762228399168514) và kiểm tra xem tham số phản hồi `has_advanced_access` có phải là `true` đối với tài khoản TikTok hay không.

## Yêu cầu gọi API (Request)

**Endpoint**  https://business-api.tiktok.com/open_api/v1.3/business/mention/hashtag/video/list/

**Method**  GET

**Required permission scopes**: `biz.brand.insights`

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền bởi tài khoản TikTok (Access Token). ⏎ Để lấy access token, hãy sử dụng [/tt_user/oauth2/token/](../10-organic-api/accounts-api.md#doc-1738084387220481). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| business_id  ****(Bắt buộc)**** | string | Application specific unique identifier for the TikTok account. ⏎ You can get the ID through the `open_id` field returned by [/tt_user/oauth2/token/](https://business-api.tiktok.com/portal/docs/mentions-api-authentication/v1.3#anchor-1). |
| hashtag | string | Hashtag cần lấy top 1.000 bài đăng trong 90 ngày qua. ⏎ Specify one hashtag from the TikTok account's enabled hashtags. ⏎ If this field is omitted, the response will include the top posts across all of the TikTok account's enabled hashtags. ⏎ To retrieve the list of hashtags enabled for the TikTok account, use [/business/mention/hashtag/manage/list/](51-mentions.md#doc-1833832557996034). ⏎ **Note**: The hashtag is case-sensitive and requires an exact match with an enabled hashtag for the TikTok account. |
| fields | string[] | Các trường yêu cầu. Nếu không đặt `fields`, chỉ các trường **mặc định** được trả về. ⏎ Giá trị mặc định: `["item_id","caption"]`. ⏎ **Supported fields**: • `item_id`: Mã định danh duy nhất của bài đăng. • `create_time`: Thời điểm bài đăng được xuất bản (định dạng Unix timestamp UTC). • `video_link`: Đường dẫn URL chung tới bài đăng trên TikTok. • `caption`: Nội dung chú thích (caption) của bài đăng. • `likes`: Tổng số lượt thích của bài đăng. • `comments`: Tổng số lượt bình luận của bài đăng. • `shares`: Tổng số lượt chia sẻ bài đăng. • `thumbnail_url`: Đường dẫn URL hình ảnh thu nhỏ (thumbnail) của bài đăng. • `matched_hashtags`: A list of brand hashtags in the post caption that match the hashtags configured for the business. |
| sort_field | string | Trường dùng để sắp xếp kết quả. ⏎ Các giá trị enum hỗ trợ: • `CREATE_TIME`: The field `create_time`. • `LIKES`: The field `likes`. • `COMMENTS`: The field `comments`. • `SHARES`: The field `shares`.Giá trị mặc định: `CREATE_TIME`. |
| sort_order | string | Thứ tự sắp xếp kết quả. ⏎ Các giá trị enum hỗ trợ: • `ASC`: Ascending. • `DESC`: Descending.Giá trị mặc định: `DESC`. |
| number_of_days | number | Khoảng thời gian tra cứu dữ liệu quá khứ, tính theo số ngày. ⏎ Value range: 1-90. ⏎ Giá trị mặc định: 90. ⏎ For instance, if you set this field to 90, the results for the last 90 days will be retrieved. |
| regions | string[] | Khu vực của các bài đăng mà bạn muốn lọc kết quả. ⏎ • If you specify this field, only posts posted by TikTok users registered in the specified regions will be returned. • If this field is not specified, all relevant posts that contain brand hashtags will be returned. ⏎ To learn about the allowed values for this field, refer to [List of values for `regions`](../10-organic-api/mentions-api.md#doc-1825107519114241). |
| cursor | number | Con trỏ phục vụ phân trang (cursor). Vị trí của kết quả bạn muốn bắt đầu lấy dữ liệu. ⏎ For instance, setting `cursor` to 10 means you want to retrieve the next page of results after the 10th position. ⏎ If the response parameter `has_more` is `true`, pass the returned cursor in this parameter in the subsequent request to receive the next page of results. ⏎ Giá trị mặc định: 0. |
| max_count | number | Số lượng hashtag tối đa được trả về cho mỗi trang dữ liệu. ⏎ Giá trị mặc định: 10. ⏎ **Note**: Due to our trust and safety policies, it is possible that the endpoint returns less than the `max_count` number of hashtags even if the response parameter `has_more` is `true`. |

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/business/mention/hashtag/video/list/?business_id={{business_id}}&fields=["item_id","video_link","caption","likes","comments","shares","create_time","thumbnail_url","matched_hashtags"]&sort_field=LIKES&sort_order=ASC' \
--header 'Access-Token: {{Access-Token}}'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Phụ lục - Mã trạng thái phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi từ hệ thống. Xem [Phụ lục - Mã lỗi trả về](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | Mã nhật ký yêu cầu (request log ID) để định danh duy nhất cho mỗi lượt gọi API. |
| data | object | Dữ liệu trả về. |
| ↳ videos | object[] | Thông tin chi tiết về các bài đăng. |
| ↳↳ item_id | string | Mã định danh duy nhất của bài đăng. ⏎ Example: `6995316737801538821`. |
| ↳↳ create_time | string | Unix/epoch date-time when the post was posted, in UTC timezone. ⏎ Example: `1628461703`. |
| ↳↳ video_link | string | The generic URL of the post, in the format of `https://www.tiktok.com/@/video/{item_id}`. ⏎ Example: `https://www.tiktok.com/@/video/7231234123412341234`. |
| ↳↳ caption | string | Post description. ⏎ Example: `Nuki: me and me casa 🏠 #cat #kitten #britishshorthair`. |
| ↳↳ likes | number | Tổng số lượt thích của bài đăng. ⏎ Example: 243. |
| ↳↳ comments | number | Tổng số lượt bình luận của bài đăng. ⏎ Example: 10. |
| ↳↳ shares | number | Tổng số lượt chia sẻ bài đăng. ⏎ Example: 10. |
| ↳↳ thumbnail_url | string | Đường dẫn URL hình ảnh thu nhỏ (thumbnail) của bài đăng. ⏎ Thời hạn hiệu lực: 48 giờ. ⏎ Thời gian hết hạn được đưa vào URL sau tham số `x-expires`, theo định dạng dấu thời gian Epoch/Unix tính bằng giây. ⏎ Example: `https://p16-sign-sg.tiktokcdn.com/tos-maliva-p-0068/1f9a445423844b82bd79317b42b9953f~c5_300x400.webp?x-expires=1614034800&x-signature=qChosOGafzBcTctPm9zYiF8Y2MA%3D`. |
| ↳↳ matched_hashtags | string[] | A list of brand hashtags in the post caption that match the hashtags configured for the business. ⏎ Example: `[\"tiktok\", \"tiktokrunning\"]`. ⏎ **Note**: If a specific hashtag is passed in the request, this field will return an empty array `[]`, as the response is filtered to only include posts for the requested hashtag. |
| ↳ cursor | number | Cursor for the next page of results, to be passed in the `cursor` query parameter of the subsequent API request. |
| ↳ has_more | boolean | Cho biết có còn trang dữ liệu tiếp theo hay không (`true` nếu còn, `false` nếu hết). |

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "cursor": 10,
        "has_more": true,
        "videos": [
            {
                "video_link": "{{video_link}}",
                "item_id": "{{item_id}}",
                "comments": 0,
                "caption": "{{caption}}",
                "create_time": "1699537820",
                "shares": 1,
                "thumbnail_url": "{{thumbnail_url}}",
                "matched_hashtags": [
                    "{{matched_hashtag}}",
                    "{{matched_hashtag}}"
                ],
                "likes": 132
            },
            {
                "video_link": "{{video_link}}",
                "item_id": "{{item_id}}",
                "comments": 3,
                "caption": "{{caption}}",
                "create_time": "1699617820",
                "shares": 0,
                "thumbnail_url": "{{thumbnail_url}}",
                "matched_hashtags": [
                    "{{matched_hashtag}}",
                    "{{matched_hashtag}}"
                ],
                "likes": 132
            },
            {
                "video_link": "{{video_link}}",
                "item_id": "{{item_id}}",
                "comments": 180,
                "caption": "{{caption}}",
                "create_time": "1694736000",
                "shares": 200,
                "thumbnail_url": "{{thumbnail_url}}",
                "matched_hashtags": [
                    "{{matched_hashtag}}",
                    "{{matched_hashtag}}"
                ],
                "likes": 170
            },
            {
                "video_link": "{{video_link}}",
                "item_id": "{{item_id}}",
                "comments": 10,
                "caption": "{{caption}}",
                "create_time": "1699627820",
                "shares": 4,
                "thumbnail_url": "{{thumbnail_url}}",
                "matched_hashtags": [
                    "{{matched_hashtag}}",
                    "{{matched_hashtag}}"
                ],
                "likes": 460
            },
            {
                "video_link": "{{video_link}}",
                "item_id": "{{item_id}}",
                "comments": 10,
                "caption": "{{caption}}",
                "create_time": "1699241347",
                "shares": 5,
                "thumbnail_url": "{{thumbnail_url}}",
                "matched_hashtags": [
                    "{{matched_hashtag}}",
                    "{{matched_hashtag}}"
                ],
                "likes": 1161
            },
            {
                "video_link": "{{video_link}}",
                "item_id": "{{item_id}}",
                "comments": 14,
                "caption": "{{caption}}",
                "create_time": "1695495795",
                "shares": 1380,
                "thumbnail_url": "{{thumbnail_url}}",
                "matched_hashtags": [
                    "{{matched_hashtag}}",
                    "{{matched_hashtag}}"
                ],
                "likes": 1396
            },
            {
                "video_link": "{{video_link}}",
                "item_id": "{{item_id}}",
                "comments": 20,
                "caption": "{{caption}}",
                "create_time": "1696097179",
                "shares": 5,
                "thumbnail_url": "{{thumbnail_url}}",
                "matched_hashtags": [
                    "{{matched_hashtag}}",
                    "{{matched_hashtag}}"
                ],
                "likes": 1422
            },
            {
                "video_link": "{{video_link}}",
                "item_id": "{{item_id}}",
                "comments": 261,
                "caption": "{{caption}}",
                "create_time": "1698616575",
                "shares": 134,
                "thumbnail_url": "{{thumbnail_url}}",
                "matched_hashtags": [
                    "{{matched_hashtag}}",
                    "{{matched_hashtag}}"
                ],
                "likes": 1702
            },
            {
                "video_link": "{{video_link}}",
                "item_id": "{{item_id}}",
                "comments": 10,
                "caption": "{{caption}}",
                "create_time": "1699637820",
                "shares": 83,
                "thumbnail_url": "{{thumbnail_url}}",
                "matched_hashtags": [
                    "{{matched_hashtag}}",
                    "{{matched_hashtag}}"
                ],
                "likes": 2049
            },
            {
                "video_link": "{{video_link}}",
                "item_id": "{{item_id}}",
                "comments": 37,
                "caption": "{{caption}}",
                "create_time": "1697493375",
                "shares": 440,
                "thumbnail_url": "{{thumbnail_url}}",
                "matched_hashtags": [
                    "{{matched_hashtag}}",
                    "{{matched_hashtag}}"
                ],
                "likes": 3492
            }
        ]
    }
}
```

---

<a id="doc-1833862470219842"></a>
<!-- doc_id: 1833862470219842 -->
<!-- doc_id: 1833862470219842 -->
# Lấy danh sách hashtag thương hiệu hợp lệ cho tài khoản TikTok (Get valid brand hashtags)
> Đường dẫn: API Reference > Lượt nhắc > Lấy danh sách hashtag thương hiệu hợp lệ cho tài khoản TikTok
Sử dụng endpoint này để truy xuất danh sách các hashtag hợp lệ mà bạn có thể kích hoạt cho một tài khoản TikTok. The results will include up to 100 top hashtags related to the TikTok account.  

Để hợp lệ với hashtag của tài khoản TikTok, hashtag phải đáp ứng các yêu cầu sau:
- The hashtag is used in at least 3 post captions, published either by the TikTok account or in a post that mentions the TikTok account Handle.

Bạn có thể bật các hashtag hợp lệ cho tài khoản TikTok bằng [/business/mention/hashtag/add/](51-mentions.md#doc-1833831427732481). Sau khi bật, các hashtag sẽ được tính vào kết quả của [/business/mention/hashtag/video/list/](51-mentions.md#doc-1825108001123522). 

> **Note:** 
Endpoint này được thiết kế cho các tài khoản có nhiều lượt đề cập organic. Tài khoản thử nghiệm hoặc tài khoản mới tạo có thể không trả về hashtag hợp lệ và không nên dùng để kiểm chứng. Để có kết quả kiểm thử chính xác, bạn cần dùng tài khoản production nhận được các lượt đề cập organic thực tế.

## Điều kiện tiên quyết trước khi bắt đầu
- Đảm bảo tài khoản TikTok là Tài khoản TikTok có Quyền truy cập Nâng cao hoặc Tài khoản Doanh nghiệp Đã xác minh (VBA). Tìm hiểu thêm [về quyền hạn tài khoản TikTok](https://ads.tiktok.com/resources/help/article/about-tiktok-account-entitlements). Để xác nhận điều này, sử dụng [/business/get/](01-accounts-p1.md#doc-1762228399168514) và kiểm tra xem tham số phản hồi `has_advanced_access` có phải là `true` đối với tài khoản TikTok hay không.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/business/mention/hashtag/verify/list/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền bởi tài khoản TikTok (Access Token). ⏎ Để lấy access token, hãy sử dụng [/tt_user/oauth2/token/](../10-organic-api/accounts-api.md#doc-1738084387220481). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
|business_id ***(Bắt buộc)***|string|Mã định danh duy nhất của tài khoản TikTok đối với ứng dụng cụ thể.<br><br>Bạn có thể lấy mã này qua trường `open_id` trả về từ [/tt_user/oauth2/token/](../10-organic-api/accounts-api.md#doc-1738084387220481).|
| username ***(Bắt buộc)***  | string | Tên người dùng (handle) của tài khoản TikTok. |

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location  --request GET 'https://business-api.tiktok.com/open_api/v1.3/business/mention/hashtag/verify/list/?business_id={{business_id}}&username={{username}}' \
--header 'Access-Token: {{Access-Token}}'
```
## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|code |number|Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Phụ lục - Mã trạng thái phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message|string|Thông báo phản hồi từ hệ thống. Xem [Phụ lục - Mã lỗi trả về](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|request_id |string|Mã nhật ký yêu cầu (request log ID) để định danh duy nhất cho mỗi lượt gọi API.  |
|data |object|Dữ liệu trả về.|
#| hashtag_list | object[] | Danh sách các hashtag hợp lệ mà bạn có thể kích hoạt cho tài khoản TikTok.|
##| hashtag | string | A valid hashtag that you can enable for the TikTok account.|
##| post_count | number | Tổng số bài đăng chứa hashtag trong chú thích bài đăng trong 90 ngày qua.|
##| like_count | number | Tổng số lượt thích trên các bài đăng chứa hashtag trong chú thích bài đăng trong 90 ngày qua.|
##| mention_post_rank | number | The rank of the hashtag among all the valid hashtags for the TikTok account.|

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "hashtag_list": [
            {
                "create_date": "2025-05-21",
                "hashtag": "{{hashtag}}"
            },
            {
                "create_date": "2025-05-21",
                "hashtag": "{{hashtag}}"
            }
        ]
    }
}
```

---

<a id="doc-1833831427732481"></a>
<!-- doc_id: 1833831427732481 -->
<!-- doc_id: 1833831427732481 -->
# Kích hoạt hashtag thương hiệu cho tài khoản TikTok (Enable brand hashtags)
> Đường dẫn: API Reference > Lượt nhắc > Kích hoạt hashtag thương hiệu cho tài khoản TikTok
Dùng endpoint này để bật hashtag cho tài khoản TikTok. 

Sau khi bật, các hashtag sẽ được tính vào kết quả của [/business/mention/hashtag/video/list/](51-mentions.md#doc-1825108001123522).  

TikTok accounts can either use hashtags returned from [/business/mention/hashtag/verify/list/](51-mentions.md#doc-1833862470219842) or use hashtags that include the full handle name. You can enable a maximum of 50 hashtags for a brand, with a limit of 10 hashtags per request.

> **Note:** 
> - Khi đã kích hoạt một hashtag cho thương hiệu, bạn không thể gỡ bỏ nó trong vòng 7 ngày tiếp theo.
> - The brand mentions data for the newly enabled  hashtags will be included in [/business/mention/hashtag/video/list/](51-mentions.md#doc-1825108001123522) 24 hours after you enable these hashtags for a brand.

## Điều kiện tiên quyết trước khi bắt đầu
- Đảm bảo tài khoản TikTok là Tài khoản TikTok có Quyền truy cập Nâng cao hoặc Tài khoản Doanh nghiệp Đã xác minh (VBA). Tìm hiểu thêm [về quyền hạn tài khoản TikTok](https://ads.tiktok.com/resources/help/article/about-tiktok-account-entitlements). Để xác nhận điều này, sử dụng [/business/get/](01-accounts-p1.md#doc-1762228399168514) và kiểm tra xem tham số phản hồi `has_advanced_access` có phải là `true` đối với tài khoản TikTok hay không.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/business/mention/hashtag/add/

**Method** POST

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền bởi tài khoản TikTok (Access Token). ⏎ Để lấy access token, hãy sử dụng [/tt_user/oauth2/token/](../10-organic-api/accounts-api.md#doc-1738084387220481). |
| Content-Type  ****(Bắt buộc)**** | string | Định dạng dữ liệu yêu cầu. ⏎ Allowed value: `application/json`. |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
|business_id ***(Bắt buộc)***|string|Mã định danh duy nhất của tài khoản TikTok đối với ứng dụng cụ thể.<br><br>Bạn có thể lấy mã này qua trường `open_id` trả về từ [/tt_user/oauth2/token/](../10-organic-api/accounts-api.md#doc-1738084387220481).|
| username ***(Bắt buộc)***  | string | Tên người dùng (handle) của tài khoản TikTok. |
| hashtags***(Bắt buộc)*** | string[] | Danh sách các hashtag cần kích hoạt cho thương hiệu.<br><br>You can include hashtags from [/business/mention/hashtag/verify/list/](51-mentions.md#doc-1833862470219842) or include the full TikTok account handle as a substring of the hashtag.<br><br>For example, if the TikTok account handle is `@TikTok`, the hashtag `#drinktiktok` would be valid.<br><br>Kích thước tối đa: 10. |

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location  --request POST 'https://business-api.tiktok.com/open_api/v1.3/business/mention/hashtag/add/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "business_id":"{{business_id}}",
    "username":"{{username}}",
    "hashtags":["{{hashtag}}","{{hashtag}}"]
}'
```
## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|code |number|Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Phụ lục - Mã trạng thái phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message|string|Thông báo phản hồi từ hệ thống. Xem [Phụ lục - Mã lỗi trả về](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|request_id |string|Mã nhật ký yêu cầu (request log ID) để định danh duy nhất cho mỗi lượt gọi API.  |
|data |object|Dữ liệu trả về.|
#|hashtag_list | object[] | Danh sách các hashtag đã kích hoạt cho tài khoản TikTok (thương hiệu). |
##|hashtag | string | A hashtag that has been enabled for the TikTok account. |
##|create_date | string | The date when the hashtag was enabled for the brand, in the format of `YYYY-MM-DD` (UTC+0 time).<br><br>Example: `2025-01-01`. |

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "hashtag_list": [
            {
                "create_date": "2025-05-21",
                "hashtag": "{{hashtag}}"
            },
            {
                "create_date": "2025-05-21",
                "hashtag": "{{hashtag}}"
            }
        ]
    }
}
```

---

<a id="doc-1833832557996034"></a>
<!-- doc_id: 1833832557996034 -->
<!-- doc_id: 1833832557996034 -->
# Lấy danh sách hashtag thương hiệu đã kích hoạt cho tài khoản TikTok (Get enabled hashtags)
> Đường dẫn: API Reference > Lượt nhắc > Lấy danh sách hashtag thương hiệu đã kích hoạt
Sử dụng endpoint này để truy xuất các hashtag đã được kích hoạt cho tài khoản TikTok.

## Điều kiện tiên quyết trước khi bắt đầu
- Đảm bảo tài khoản TikTok là Tài khoản TikTok có Quyền truy cập Nâng cao hoặc Tài khoản Doanh nghiệp Đã xác minh (VBA). Tìm hiểu thêm [về quyền hạn tài khoản TikTok](https://ads.tiktok.com/resources/help/article/about-tiktok-account-entitlements). Để xác nhận điều này, sử dụng [/business/get/](01-accounts-p1.md#doc-1762228399168514) và kiểm tra xem tham số phản hồi `has_advanced_access` có phải là `true` đối với tài khoản TikTok hay không.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/business/mention/hashtag/manage/list/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền bởi tài khoản TikTok (Access Token). ⏎ Để lấy access token, hãy sử dụng [/tt_user/oauth2/token/](../10-organic-api/accounts-api.md#doc-1738084387220481). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
|business_id ***(Bắt buộc)***|string|Mã định danh duy nhất của tài khoản TikTok đối với ứng dụng cụ thể.<br><br>Bạn có thể lấy mã này qua trường `open_id` trả về từ [/tt_user/oauth2/token/](../10-organic-api/accounts-api.md#doc-1738084387220481).|
| username ***(Bắt buộc)***  | string | Tên người dùng (handle) của tài khoản TikTok. |

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location  --request GET 'https://business-api.tiktok.com/open_api/v1.3/business/mention/hashtag/manage/list/?business_id={{business_id}}&username={{username}}' \
--header 'Access-Token: {{Access-Token}}'
```
## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|code |number|Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Phụ lục - Mã trạng thái phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message|string|Thông báo phản hồi từ hệ thống. Xem [Phụ lục - Mã lỗi trả về](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|request_id |string|Mã nhật ký yêu cầu (request log ID) để định danh duy nhất cho mỗi lượt gọi API.  |
|data |object|Dữ liệu trả về.|
#| hashtag_list | object[] | Danh sách các hashtag đã kích hoạt cho tài khoản TikTok (thương hiệu). |
##| hashtag | string | A hashtag enabled for the TikTok account. |
##| create_date | string | The date when the hashtag was enabled for the TikTok account, in the format of `YYYY-MM-DD` (UTC+0 time).<br><br>Example: `2025-01-01`. |

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "hashtag_list": [
            {
                "create_date": "2025-05-21",
                "hashtag": "{{hashtag}}"
            },
            {
                "create_date": "2025-05-21",
                "hashtag": "{{hashtag}}"
            }
        ]
    }
}
```

---

<a id="doc-1833833401871362"></a>
<!-- doc_id: 1833833401871362 -->
<!-- doc_id: 1833833401871362 -->
# Xóa hashtag thương hiệu đã kích hoạt cho tài khoản TikTok (Delete an enabled brand hashtag)
> Đường dẫn: API Reference > Lượt nhắc > Xóa hashtag thương hiệu đã kích hoạt
Sử dụng endpoint này để xóa enabled hashtags for a TikTok account.

## Điều kiện tiên quyết trước khi bắt đầu
- Đảm bảo tài khoản TikTok là Tài khoản TikTok có Quyền truy cập Nâng cao hoặc Tài khoản Doanh nghiệp Đã xác minh (VBA). Tìm hiểu thêm [về quyền hạn tài khoản TikTok](https://ads.tiktok.com/resources/help/article/about-tiktok-account-entitlements). Để xác nhận điều này, sử dụng [/business/get/](01-accounts-p1.md#doc-1762228399168514) và kiểm tra xem tham số phản hồi `has_advanced_access` có phải là `true` đối với tài khoản TikTok hay không.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/business/mention/hashtag/remove/

**Method** POST

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền bởi tài khoản TikTok (Access Token). ⏎ Để lấy access token, hãy sử dụng [/tt_user/oauth2/token/](../10-organic-api/accounts-api.md#doc-1738084387220481). |
| Content-Type  ****(Bắt buộc)**** | string | Định dạng dữ liệu yêu cầu. ⏎ Allowed value: `application/json`. |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
|business_id ***(Bắt buộc)***|string|Mã định danh duy nhất của tài khoản TikTok đối với ứng dụng cụ thể.<br><br>Bạn có thể lấy mã này qua trường `open_id` trả về từ [/tt_user/oauth2/token/](../10-organic-api/accounts-api.md#doc-1738084387220481).|
| username ***(Bắt buộc)***  | string | Tên người dùng (handle) của tài khoản TikTok. |
| hashtag ***(Bắt buộc)***  | string | Hashtag cần xóa.<br><br>To obtain a list of existing enabled hashtags for the brand, use [/business/mention/hashtag/manage/list/](51-mentions.md#doc-1833832557996034).<br><br><p><span style="color:darkred"><b>Note</b></span>: You can only delete hashtags that were enabled at least seven days ago. To ensure this, check the returned `create_date` for the hashtags from [/business/mention/hashtag/manage/list/](51-mentions.md#doc-1833832557996034). |

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location  --request POST 'https://business-api.tiktok.com/open_api/v1.3/business/mention/hashtag/remove/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "business_id":"{{business_id}}",
    "username":"{{username}}",
    "hashtag":"{{hashtag}}"
}'
```
## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|code |number|Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Phụ lục - Mã trạng thái phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message|string|Thông báo phản hồi từ hệ thống. Xem [Phụ lục - Mã lỗi trả về](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|request_id |string|Mã nhật ký yêu cầu (request log ID) để định danh duy nhất cho mỗi lượt gọi API.  |
|data |object|Dữ liệu trả về.|

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {}
}
```

---

<a id="doc-1825107985360898"></a>
<!-- doc_id: 1825107985360898 -->
<!-- doc_id: 1825107985360898 -->
# Lấy top 1000 lượt nhắc trong bình luận bài đăng (Get top 1000 comment mentions)
> Đường dẫn: API Reference > Lượt nhắc > Lấy top 1000 lượt nhắc trong bình luận
Sử dụng endpoint này để truy xuất a list of up to 1,000 post comments or replies that mention a business's handle.

If more than 1,000 post comments or replies mention the business's handle, the top 1,000 with the highest number of comment likes will be returned. Note that comments or replies that solely consist of the mention (@) without additional text will be deprioritized.

Để xuất hiện trong kết quả tìm kiếm, bình luận hoặc phản hồi phải đáp ứng các yêu cầu sau:
- Loại tài khoản: Tài khoản TikTok phải là Tài khoản TikTok có Quyền truy cập Nâng cao hoặc Tài khoản Doanh nghiệp Đã xác minh (VBA). Tìm hiểu thêm [về quyền hạn tài khoản TikTok](https://ads.tiktok.com/resources/help/article/about-tiktok-account-entitlements). Để xác nhận điều này, sử dụng [/business/get/](01-accounts-p1.md#doc-1762228399168514) và kiểm tra xem tham số phản hồi `has_advanced_access` có phải là `true` đối với tài khoản TikTok hay không.
- Trạng thái hiển thị bài đăng: Bình luận hoặc câu trả lời được đăng trên một bài đăng công khai.
- Lượt nhắc: Bình luận hoặc phản hồi có nhắc trực tiếp (@) đến handle của doanh nghiệp trong nội dung bình luận.
- Khung thời gian tra cứu: Bài đăng phải được đăng trong vòng 90 ngày qua.
- Độ tuổi người dùng: Bài đăng không thuộc về người dùng chưa đủ tuổi hoặc không xác định độ tuổi. Đối với người dùng ở Châu Âu, độ tuổi từ 17 trở xuống được coi là chưa đủ tuổi, trong khi đối với người dùng ở Hoa Kỳ và các quốc gia hoặc khu vực khác, độ tuổi từ 12 trở xuống được coi là chưa đủ tuổi.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/business/mention/comment/list/

**Method** GET

**Required permission scopes**: `biz.brand.insights`, `comment.list`

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền bởi tài khoản TikTok (Access Token). ⏎ Để lấy access token, hãy sử dụng [/tt_user/oauth2/token/](../10-organic-api/accounts-api.md#doc-1738084387220481). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
|business_id ***(Bắt buộc)***|string|Mã định danh duy nhất của tài khoản TikTok đối với ứng dụng cụ thể.<br><br>Bạn có thể lấy mã này qua trường `open_id` trả về từ [/tt_user/oauth2/token/](../10-organic-api/accounts-api.md#doc-1738084387220481).|
|fields|string[]|Các trường yêu cầu. Nếu không đặt `fields`, chỉ các trường <b>mặc định</b> được trả về.<br><br>Giá trị mặc định: `["comment_id","comment_text"]`.<br><br><b>Supported fields</b>:<ul><li>`item_id`: Mã định danh duy nhất của bài đăng.</li><li>`video_link`: Đường dẫn URL chung tới bài đăng trên TikTok.</li><li>`caption`: The description of the post.</li><li>`video_likes`: Tổng số lượt thích của bài đăng.</li><li>`thumbnail_url`: Đường dẫn URL hình ảnh thu nhỏ (thumbnail) của bài đăng.</li><li>`commenter_display_name`: Tên handle của người dùng đã để lại bình luận.</li><li>`comment_id`: Mã định danh duy nhất của bình luận.</li><li>`comment_type`: Loại bình luận.</li><li>`comment_text`: The comment text that mentions the business's handle.</li><li>`comment_create_time`: The time when the comment was posted.</li><li>`comment_likes`: Total number of likes for the comment.</li></ul>|
|sort_field|string|Trường dùng để sắp xếp kết quả.<br><br>Các giá trị enum hỗ trợ: <ul><li>`VIDEO_LIKES`: The field `video_likes`.</li><li>`COMMENT_CREATE_TIME`: The field `comment_create_time`.</li><li>`COMMENT_LIKES`: The field `comment_likes`.</li></ul>Giá trị mặc định: `COMMENT_CREATE_TIME`.|
|sort_type|string|Thứ tự sắp xếp kết quả.<br><br>Các giá trị enum hỗ trợ: <ul><li>`ASC`: Ascending.</li><li>`DESC`: Descending.</li></ul>Giá trị mặc định: `DESC`.|
|number_of_days|number|Khoảng thời gian tra cứu dữ liệu quá khứ, tính theo số ngày.<br><br>Value range: 1-90.<br>Giá trị mặc định: 90.<br><br>For instance, if you set this field to 90, the results for the last 90 days will be retrieved.|
|regions|string[]|Khu vực của các bài đăng mà bạn muốn lọc kết quả.<br><br><ul><li>If you specify this field, only comments on posts posted by TikTok users registered in the specified regions will be returned.</li><li>If this field is not specified, comments on all relevant posts will be returned.</li></ul><br>To learn about the allowed values for this field, refer to [List of values for `regions`](../10-organic-api/mentions-api.md#doc-1825107519114241).|
|cursor|integer|Con trỏ phục vụ phân trang (cursor). Vị trí của kết quả bạn muốn bắt đầu lấy dữ liệu.<br><br>For instance, setting `cursor` to 10 means you want to retrieve the next page of results after the 10th position.<br><br>If the response parameter `has_more` is true, pass the returned cursor in this parameter in the subsequent request to receive the next page of results.<br><br>Giá trị mặc định: 0.|
|max_count|integer|Số lượng bình luận tối đa được trả về trên mỗi trang dữ liệu.<br><br>Giá trị mặc định: 10.<br>Value range: 1-100.<br><br><span style="color:darkred"><b>Note</b></span>: Due to our trust and safety policies, it is possible that the endpoint returns less than the `max_count` number of comments even if the response parameter `has_more` is `true`.|

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location  --request GET 'https://business-api.tiktok.com/open_api/v1.3/business/mention/comment/list/?business_id={{business_id}}&fields=["item_id","video_link","caption","video_likes","thumbnail_url","commenter_display_name","comment_id","comment_type","comment_text","comment_create_time","comment_likes"]&sort_field=COMMENT_LIKES&sort_type=ASC' \
--header 'Access-Token: {{Access-Token}}' \
```
## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|code |number|Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Phụ lục - Mã trạng thái phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message|string|Thông báo phản hồi từ hệ thống. Xem [Phụ lục - Mã lỗi trả về](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|request_id |string|Mã nhật ký yêu cầu (request log ID) để định danh duy nhất cho mỗi lượt gọi API.  |
|data |object|Dữ liệu trả về.|
#|comments|object[]|Information about the mentions in comments.|
##|item_id|string|Mã định danh duy nhất của bài đăng.<br><br>Example: `6995316737801538821`.|
##|video_link|string|URL chung của bài đăng, có định dạng https://www.tiktok.com/@/video/&#123;item_id&#125;.<br><br>Example: `https://www.tiktok.com/@/video/7231234123412341234`.|
##|caption|string|Post description.<br><br>Example: `Nuki: me and me casa 🏠 #cat #kitten #britishshorthair`.|
##|video_likes|number|Tổng số lượt thích của bài đăng.<br><br>Example: 243.|
##|thumbnail_url|string|Đường dẫn URL hình ảnh thu nhỏ (thumbnail) của bài đăng.<br><br>Thời hạn hiệu lực: 48 giờ.<br>Thời gian hết hạn được đưa vào URL sau tham số `x-expires`, theo định dạng dấu thời gian Epoch/Unix tính bằng giây.<br><br>Example: `https://p16-sign-sg.tiktokcdn.com/tos-maliva-p-0068/1f9a445423844b82bd79317b42b9953f~c5_300x400.webp?x-expires=1614034800&x-signature=qChosOGafzBcTctPm9zYiF8Y2MA%3D"`.<br><br><span style="color:darkred"><b>Note</b></span>: For TikTok photo posts, the value of this field will be an empty string (`""`).|
##|commenter_display_name|string|Tên handle của người dùng đã để lại bình luận.<br><br>Example: `angely`.|
##|comment_id|string|Mã định danh duy nhất của bình luận.<br><br>Example: `6990565363377392901`.|
##|comment_type|string|Loại bình luận.<br><br>Các giá trị enum hỗ trợ: <ul><li>`COMMENT`: Top-level comment.</li><li>`REPLY`: Comment reply.</li></ul>|
##|comment_text|string|Nội dung bình luận nhắc đến handle của thương hiệu.<br><br>Example: `This is a comment #comment 🙂`.|
##|comment_create_time|string|Unix/epoch date-time when the comment was posted, in UTC timezone.<br><br>Example: `1628461703`.|
##|comment_likes|number|Total number of likes for the comment.<br><br>Example: 243.|
#|cursor|number|Cursor for the next page of results, to be passed in the cursor query parameter of the subsequent API request.|
#|has_more|boolean|Cho biết có còn trang dữ liệu tiếp theo hay không (`true` nếu còn, `false` nếu hết).|

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
HTTPS/1.1 200 OK

{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "cursor": 10,
        "has_more": true,
        "comments": [
            {
                "video_link": "{{video_link}}",
                "item_id": "{{item_id}}",
                "video_likes": 101,
                "caption": "{{caption}}",
                "thumbnail_url": "{{thumbnail_url}}",
                "commenter_display_name": "{{commenter_display_name}}",
                "comment_id": "{{comment_id}}",
                "comment_likes": 0,
                "comment_text": "{{comment_text}}",
                "comment_create_time": "1698616575",
                "comment_type": "COMMENT"
            },
            {
                "video_link": "{{video_link}}",
                "item_id": "{{item_id}}",
                "video_likes": 104,
                "caption": "{{caption}}",
                "thumbnail_url": "{{thumbnail_url}}",
                "commenter_display_name": "{{commenter_display_name}}",
                "comment_id": "{{comment_id}}",
                "comment_likes": 0,
                "comment_text": "{{comment_text}}",
                "comment_create_time": "1695495795",
                "comment_type": "COMMENT"
            },
            {
                "video_link": "{{video_link}}",
                "item_id": "{{item_id}}",
                "video_likes": 105,
                "caption": "{{caption}}",
                "thumbnail_url": "{{thumbnail_url}}",
                "commenter_display_name": "{{commenter_display_name}}",
                "comment_id": "{{comment_id}}",
                "comment_likes": 0,
                "comment_text": "{{comment_text}}",
                "comment_create_time": "1696097179",
                "comment_type": "COMMENT"
            },
            {
                "video_link": "{{video_link}}",
                "item_id": "{{item_id}}",
                "video_likes": 110,
                "caption": "{{caption}}",
                "thumbnail_url": "{{thumbnail_url}}",
                "commenter_display_name": "{{commenter_display_name}}",
                "comment_id": "{{comment_id}}",
                "comment_likes": 0,
                "comment_text": "{{comment_text}}",
                "comment_create_time": "1699537820",
                "comment_type": "COMMENT"
            },
            {
                "video_link": "{{video_link}}",
                "item_id": "{{item_id}}",
                "video_likes": 103,
                "caption": "{{caption}}",
                "thumbnail_url": "{{thumbnail_url}}",
                "commenter_display_name": "{{commenter_display_name}}",
                "comment_id": "{{comment_id}}",
                "comment_likes": 0,
                "comment_text": "{{comment_text}}",
                "comment_create_time": "1697493375",
                "comment_type": "REPLY"
            },
            {
                "video_link": "{{video_link}}",
                "item_id": "{{item_id}}",
                "video_likes": 107,
                "caption": "{{caption}}",
                "thumbnail_url": "{{thumbnail_url}}",
                "commenter_display_name": "{{commenter_display_name}}",
                "comment_id": "{{comment_id}}",
                "comment_likes": 0,
                "comment_text": "{{comment_text}}",
                "comment_create_time": "1699637820",
                "comment_type": "REPLY"
            },
            {
                "video_link": "{{video_link}}",
                "item_id": "{{item_id}}",
                "video_likes": 106,
                "caption": "{{caption}}",
                "thumbnail_url": "{{thumbnail_url}}",
                "commenter_display_name": "{{commenter_display_name}}",
                "comment_id": "{{comment_id}}",
                "comment_likes": 0,
                "comment_text": "{{comment_text}}",
                "comment_create_time": "1699241347",
                "comment_type": "COMMENT"
            },
            {
                "video_link": "{{video_link}}",
                "item_id": "{{item_id}}",
                "video_likes": 102,
                "caption": "{{caption}}",
                "thumbnail_url": "{{thumbnail_url}}",
                "commenter_display_name": "{{commenter_display_name}}",
                "comment_id": "{{comment_id}}",
                "comment_likes": 0,
                "comment_text": "{{comment_text}}",
                "comment_create_time": "1698011775",
                "comment_type": "COMMENT"
            },
            {
                "video_link": "{{video_link}}",
                "item_id": "{{item_id}}",
                "video_likes": 109,
                "caption": "{{caption}}",
                "thumbnail_url": "{{thumbnail_url}}",
                "commenter_display_name": "{{commenter_display_name}}",
                "comment_id": "{{comment_id}}",
                "comment_likes": 1,
                "comment_text": "{{comment_text}}",
                "comment_create_time": "1699617820",
                "comment_type": "COMMENT"
            },
            {
                "video_link": "{{video_link}}",
                "item_id": "{{item_id}}",
                "video_likes": 108,
                "caption": "{{caption}}",
                "thumbnail_url": "{{thumbnail_url}}",
                "commenter_display_name": "{{commenter_display_name}}",
                "comment_id": "{{comment_id}}",
                "comment_likes": 16,
                "comment_text": "{{comment_text}}",
                "comment_create_time": "1699627820",
                "comment_type": "COMMENT"
            }
        ]
    }
}
```

---

<a id="doc-1831358502098946"></a>
<!-- doc_id: 1831358502098946 -->
<!-- doc_id: 1831358502098946 -->
# Lấy thông tin chi tiết lượt nhắc bình luận từ webhook (Get comment mention details)
> Đường dẫn: API Reference > Lượt nhắc > Lấy chi tiết lượt nhắc bình luận từ webhook
Sử dụng endpoint này để truy xuất the details of a mention in a comment obtained from [the mentions webhook](../08-use-cases/use-case-webhook.md#doc-1825113658431489), enabling real-time monitoring of business mentions in comment threads. The mention can originate from a post comment or reply that mentions a business's handle.

> **Note:** 
> Hãy truy xuất thông tin chi tiết trong vòng 48 giờ kể từ khi nhận được webhook để đảm bảo tính khả dụng của dữ liệu.

## Điều kiện tiên quyết trước khi bắt đầu
- Đảm bảo tài khoản TikTok là Tài khoản TikTok có Quyền truy cập Nâng cao hoặc Tài khoản Doanh nghiệp Đã xác minh (VBA). Tìm hiểu thêm [về quyền hạn tài khoản TikTok](https://ads.tiktok.com/resources/help/article/about-tiktok-account-entitlements). Để xác nhận điều này, sử dụng [/business/get/](01-accounts-p1.md#doc-1762228399168514) và kiểm tra xem tham số phản hồi `has_advanced_access` có phải là `true` đối với tài khoản TikTok hay không.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/business/mention/comment/get/

**Method** GET

**Required permission scopes**: `biz.brand.insights`, `comment.list`

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền bởi tài khoản TikTok (Access Token). ⏎ Để lấy access token, hãy sử dụng [/tt_user/oauth2/token/](../10-organic-api/accounts-api.md#doc-1738084387220481). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
|business_id ***(Bắt buộc)***|string|Mã định danh duy nhất của tài khoản TikTok đối với ứng dụng cụ thể.<br><br>Bạn có thể lấy mã này qua trường `open_id` trả về từ [/tt_user/oauth2/token/](../10-organic-api/accounts-api.md#doc-1738084387220481).|
|comment_id***(Bắt buộc)***|string|ID của bình luận hoặc phản hồi có nhắc đến doanh nghiệp trong nội dung bình luận.<br><br>Pass the `comment_id` as obtained from `comment_id` within the [`content` of the mentions webhook event](../08-use-cases/use-case-webhook.md#doc-1825113658431489).|
|item_id***(Bắt buộc)***|string|ID của bài đăng mà bình luận được đăng tải.<br><br>Pass the post ID as obtained from `video_id` within the [`content` of the mentions webhook event](../08-use-cases/use-case-webhook.md#doc-1825113658431489).|
|fields|string[]|Các trường yêu cầu.<br> Nếu không đặt `fields`, chỉ các trường <b>mặc định</b> được trả về.<br><br>Giá trị mặc định: `["comment_id","comment_text"]`.<br><br><b>Supported fields</b>:<ul><li>`item_id`: Mã định danh duy nhất của bài đăng.</li><li>`video_link`: Đường dẫn URL chung tới bài đăng trên TikTok.</li><li>`video_likes`: Tổng số lượt thích của bài đăng.</li><li>`thumbnail_url`: Đường dẫn URL hình ảnh thu nhỏ (thumbnail) của bài đăng.</li><li>`commenter_handle_name`: Tên handle của người dùng đã để lại bình luận.</li><li>`comment_id`: Mã định danh duy nhất của bình luận.</li><li>`comment_type`: Loại bình luận.</li><li>`comment_text`: The comment text that mentions the business's handle.</li><li>`comment_create_time`: The time when the comment was posted.</li><li>`comment_likes`: Total number of likes for the comment.</li></ul>|

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location  --request GET 'https://business-api.tiktok.com/open_api/v1.3/business/mention/comment/get/?business_id={{business_id}}&comment_id={{comment_id}}&item_id={{item_id}}&fields=["item_id","video_link","caption","video_likes","thumbnail_url","commenter_handle_name","comment_id","comment_type","comment_text","comment_create_time","comment_likes"]' \
--header 'Access-Token: {{Access-Token}}' \
```
## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|code |number|Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Phụ lục - Mã trạng thái phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message|string|Thông báo phản hồi từ hệ thống. Xem [Phụ lục - Mã lỗi trả về](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|request_id |string|Mã nhật ký yêu cầu (request log ID) để định danh duy nhất cho mỗi lượt gọi API.  |
|data |object|Dữ liệu trả về.|
#|comment|object|Information about the mention in the comment.|
##|item_id|string|Mã định danh duy nhất của bài đăng.<br><br>Example: `6995316737801538821`.|
##|video_link|string|URL chung của bài đăng, có định dạng https://www.tiktok.com/@/video/&#123;item_id&#125;.<br><br>Example: `https://www.tiktok.com/@/video/7231234123412341234`.|
##|video_likes|number|Tổng số lượt thích của bài đăng.<br><br>Example: 243.|
##|thumbnail_url|string|Đường dẫn URL hình ảnh thu nhỏ (thumbnail) của bài đăng.<br><br>Thời hạn hiệu lực: 48 giờ.<br>Thời gian hết hạn được đưa vào URL sau tham số `x-expires`, theo định dạng dấu thời gian Epoch/Unix tính bằng giây.<br><br>Example: `https://p16-sign-sg.tiktokcdn.com/tos-maliva-p-0068/1f9a445423844b82bd79317b42b9953f~c5_300x400.webp?x-expires=1614034800&x-signature=qChosOGafzBcTctPm9zYiF8Y2MA%3D"`.<br><br><span style="color:darkred"><b>Note</b></span>: For TikTok photo posts, the value of this field will be an empty string (`""`).|
##|commenter_handle_name|string|Tên handle của người dùng đã để lại bình luận.<br><br>Example: `angely`.|
##|comment_id|string|Mã định danh duy nhất của bình luận.<br><br>Example: `6990565363377392901`.|
##|comment_type|string|Loại bình luận.<br><br>Các giá trị enum hỗ trợ: <ul><li>`COMMENT`: Top-level comment.</li><li>`REPLY`: Comment reply.</li></ul>|
##|comment_text|string|Nội dung bình luận nhắc đến handle của thương hiệu.<br><br>Example: `This is a comment #comment 🙂`.|
##|comment_create_time|string|Unix/epoch date-time when the comment was posted, in UTC timezone.<br><br>Example: `2025-04-01 06:49:10 +0000 UTC`.|
##|comment_likes|number|Total number of likes for the comment.<br><br>Example: 243.|

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "comment":
            {
                "video_link": "{{video_link}}",
                "item_id": "{{item_id}}",
                "video_likes": 101,
                "thumbnail_url": "{{thumbnail_url}}",
                "commenter_handle_name": "{{commenter_handle_name}}",
                "comment_id": "{{comment_id}}",
                "comment_likes": 0,
                "comment_text": "{{comment_text}}",
                "comment_create_time": "2025-04-29 06:11:59 +0000 UTC",
                "comment_type": "COMMENT"
            }
    }
}
```

---

<a id="doc-1825107991945218"></a>
<!-- doc_id: 1825107991945218 -->
<!-- doc_id: 1825107991945218 -->
# Phản hồi lượt nhắc trong bình luận (Reply to a mention in comments)
> Đường dẫn: API Reference > Lượt nhắc > Phản hồi lượt nhắc trong bình luận
Dùng endpoint này để phản hồi bình luận hoặc phản hồi video có đề cập đến handle của doanh nghiệp.

## Điều kiện tiên quyết trước khi bắt đầu
- Đảm bảo tài khoản TikTok là Tài khoản TikTok có Quyền truy cập Nâng cao hoặc Tài khoản Doanh nghiệp Đã xác minh (VBA). Tìm hiểu thêm [về quyền hạn tài khoản TikTok](https://ads.tiktok.com/resources/help/article/about-tiktok-account-entitlements). Để xác nhận điều này, sử dụng [/business/get/](01-accounts-p1.md#doc-1762228399168514) và kiểm tra xem tham số phản hồi `has_advanced_access` có phải là `true` đối với tài khoản TikTok hay không.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/business/comment/reply/create/

**Method** POST

**Required permission scope**: `comment.list.manage`

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền bởi tài khoản TikTok (Access Token). ⏎ Để lấy access token, hãy sử dụng [/tt_user/oauth2/token/](../10-organic-api/accounts-api.md#doc-1738084387220481). |
| Content-Type  ****(Bắt buộc)**** | string | Định dạng dữ liệu yêu cầu. ⏎ Allowed format: `application/json`. |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|business_id ***(Bắt buộc)***|string|Mã định danh duy nhất của tài khoản TikTok đối với ứng dụng cụ thể.<br><br>Bạn có thể lấy mã này qua trường `open_id` trả về từ [/tt_user/oauth2/token/](../10-organic-api/accounts-api.md#doc-1738084387220481).|
|video_id ***(Bắt buộc)***|string|Unique identifier for the video on which you want to create a reply.<br><br>You can get the `video_id` from the `item_id` field returned by [/business/mention/comment/list/](51-mentions.md#doc-1825107985360898).|
|comment_id ***(Bắt buộc)***|string|Unique identifier for the comment to which you want to create a reply.<br><br>You can get the`comment_id` from the `comment_id` field returned by [/business/mention/comment/list/](51-mentions.md#doc-1825107985360898).|
|text ***(Bắt buộc)***|string|Nội dung văn bản của phản hồi bạn muốn tạo.<br><br>Giới hạn độ dài: 1,200 characters (UTF-8 encoding).<br><br>Example: `This is a comment #comment 🙂`.|

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location  --request POST 'https://business-api.tiktok.com/open_api/v1.3/business/comment/reply/create/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "business_id" : "{{business_id}}",
    "video_id": "{{video_id}}",
    "comment_id" : "{{comment_id}}",
    "text": "{{text}}"
}'
```
## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|code |number|Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Phụ lục - Mã trạng thái phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message|string|Thông báo phản hồi từ hệ thống. Xem [Phụ lục - Mã lỗi trả về](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|request_id |string|Mã nhật ký yêu cầu (request log ID) để định danh duy nhất cho mỗi lượt gọi API.  |
|data |object|Dữ liệu trả về.|
#|comment_id|string|Unique identifier for the newly created reply.<br><br>Example: `6990565363377392901`.|
#|parent_comment_id|string|Unique identifier for the comment to which the reply was created.<br><br>Example: `6990565363377392901`.|
#|video_id|string|Unique identifier for the video where the reply was created.<br><br>Example: `6990565363377392901`.|
#|user_id|string|Developer application and TikTok account scoped unique identifier for the user that made the reply.<br><br>Example: `ce9b7be629b0447af777a0ad9455783f61b7f790982b49fbda04a23b4722eaffe`.|
#|create_time|integer|Unix/Epoch date-time when the reply was created, in UTC timezone.<br><br>Example: 1627617835.|
#|text|string|Nội dung văn bản của phản hồi.<br><br>Example: `This is a comment #comment 🙂`.|

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
HTTPS/1.1 200 OK

{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "video_id": "{{video_id}}",
        "parent_comment_id": "{{parent_comment_id}}",
        "comment_id": "{{comment_id}}",
        "create_time": "1701334608",
        "text": "{{text}}",
        "user_id": "{{user_id}}"
    }
}
```

---

<a id="doc-1825108008121346"></a>
<!-- doc_id: 1825108008121346 -->
<!-- doc_id: 1825108008121346 -->
# Tạo cấu hình Webhook cho Mentions (Create a Mentions Webhook configuration)
> Đường dẫn: API Reference > Lượt nhắc > Tạo cấu hình Webhook cho Mentions
Sử dụng endpoint này để tạo cấu hình cho các sự kiện Nhắc đến liên quan đến tài khoản TikTok của bạn ở cấp ứng dụng nhà phát triển.

Để tìm hiểu thêm về cách tạo cấu hình cho các sự kiện Webhook này, xem [Subscribe to Mentions Webhook events via Webhooks API](../08-use-cases/use-case-webhook.md#doc-1825113658431489).

Nếu không muốn nhận thông báo nữa, bạn có thể xóa cấu hình Webhook bằng [/business/webhook/delete/](51-mentions.md#doc-1825108021550082).

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/business/webhook/update/

**Method** POST

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Content-Type  ****(Bắt buộc)**** | string | Định dạng dữ liệu yêu cầu. ⏎ Allowed format: `application/json`. |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|app_id ***(Bắt buộc)***|string|ID của ứng dụng nhà phát triển (App ID).<br><br>You can find the <strong>App ID</strong> by navigating to <strong>[My Apps](https://ads.tiktok.com/marketing_api/apps/)</strong> > <strong>App Detail</strong> > <strong>Basic Information</strong>. |
|secret ***(Bắt buộc)***|string|Khóa bí mật của ứng dụng nhà phát triển (Secret).<br><br>You can find the <strong>Secret</strong> by navigating to <strong>[My Apps](https://ads.tiktok.com/marketing_api/apps/)</strong> > <strong>App Detail</strong> > <strong>Basic Information</strong>. |
|event_type ***(Bắt buộc)***|string|Loại sự kiện Webhook mà bạn muốn đăng ký.<br><br>Các giá trị enum hỗ trợ: <ul><li>`BRAND_MENTION`: Mentions events. To learn more about the schema and sample payload of the events within this event category, see [Webhook schema](../08-use-cases/use-case-webhook.md#doc-1825113658431489).</li></ul>|
|callback_url ***(Bắt buộc)***|string|Đường dẫn URL gọi lại (Callback URL).|

### Ví dụ lệnh cURL (Example)
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
## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|code |number|Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Phụ lục - Mã trạng thái phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message|string|Thông báo phản hồi từ hệ thống. Xem [Phụ lục - Mã lỗi trả về](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|request_id |string|Mã nhật ký yêu cầu (request log ID) để định danh duy nhất cho mỗi lượt gọi API.  |
|data |object|Dữ liệu trả về.|
#|app_id|string|ID của ứng dụng nhà phát triển (App ID).|
#|event_type|string|Loại cấu hình sự kiện Webhook.<br><br>Các giá trị enum hỗ trợ: <ul><li>`BRAND_MENTION`: Mentions events. To learn more about the schema and sample payload of the events within this event category, see [Webhook schema](../08-use-cases/use-case-webhook.md#doc-1825113658431489).</li></ul>|
#|callback_url|string|Đường dẫn URL gọi lại (Callback URL).|

### Ví dụ lệnh cURL (Example)
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

---

<a id="doc-1825108014565442"></a>
<!-- doc_id: 1825108014565442 -->
<!-- doc_id: 1825108014565442 -->
# Lấy cấu hình Webhook cho Mentions (Get a Mentions Webhook configuration)
> Đường dẫn: API Reference > Lượt nhắc > Lấy cấu hình Webhook cho Mentions
Sử dụng endpoint này để truy xuất cấu hình hiện có cho các sự kiện Webhook Nhắc đến ở cấp ứng dụng nhà phát triển.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/business/webhook/list/

**Method** GET

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
| app_id ***(Bắt buộc)*** | string | ID của ứng dụng nhà phát triển (App ID). <br><br>You can find the <strong>App ID</strong> by navigating to <strong>[My Apps](https://ads.tiktok.com/marketing_api/apps/)</strong> > <strong>App Detail</strong> > <strong>Basic Information</strong>. |
| secret ***(Bắt buộc)*** | string | Khóa bí mật của ứng dụng nhà phát triển (Secret). <br><br>You can find the <strong>Secret</strong> by navigating to <strong>[My Apps](https://ads.tiktok.com/marketing_api/apps/)</strong> > <strong>App Detail</strong> > <strong>Basic Information</strong>. |
| event_type ***(Bắt buộc)*** | string |Loại sự kiện Webhook mà bạn muốn đăng ký.<br><br>Các giá trị enum hỗ trợ: <ul><li>`BRAND_MENTION`: Mentions events. To learn more about the schema and sample payload of the events within this event category, see [Webhook schema](../08-use-cases/use-case-webhook.md#doc-1825113658431489).</li></ul>|
### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location  --request GET 'https://business-api.tiktok.com/open_api/v1.3/business/webhook/list/?app_id={{app_id}}&secret={{secret}}&event_type=DIRECT_MESSAGE'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|code |number|Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Phụ lục - Mã trạng thái phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message|string|Thông báo phản hồi từ hệ thống. Xem [Phụ lục - Mã lỗi trả về](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|request_id |string|Mã nhật ký yêu cầu (request log ID) để định danh duy nhất cho mỗi lượt gọi API.  |
|data |object|Dữ liệu trả về.|
#| app_id | string | ID của ứng dụng nhà phát triển (App ID). |
#| event_type| string |Loại cấu hình sự kiện Webhook.<br><br>Các giá trị enum hỗ trợ: <ul><li>`BRAND_MENTION`: Mentions events. To learn more about the schema and sample payload of the events within this event category, see [Webhook schema](../08-use-cases/use-case-webhook.md#doc-1825113658431489).</li></ul>|
#| callback_url | string | Returned only when the corresponding event configuration exists for your developer app.<br><br>Đường dẫn URL gọi lại (Callback URL).<br><br> For example, if `event_type` is `BRAND_MENTION` and `callback_url` is not returned in the response, your developer app doesn't have an existing Mentions Webhook configuration.|

### Ví dụ lệnh cURL (Example)
#### Truy xuất cấu hình Webhook hiện có (Retrieve existing Webhook configuration)
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

#### Truy xuất cấu hình Webhook trống (Retrieve empty Webhook configuration)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "app_id": "{{app_id}}",
        "event_type": "BRAND_MENTION"
    }
}
```

---

<a id="doc-1825108021550082"></a>
<!-- doc_id: 1825108021550082 -->
<!-- doc_id: 1825108021550082 -->
# Xóa cấu hình Webhook cho Mentions (Delete a Mentions Webhook configuration)
> Đường dẫn: API Reference > Lượt nhắc > Xóa cấu hình Webhook cho Mentions
Sử dụng endpoint này để xóa cấu hình hiện có cho các sự kiện Webhook Nhắc đến ở cấp ứng dụng nhà phát triển.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/business/webhook/delete/

**Method** POST

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Content-Type  ****(Bắt buộc)**** | string | Định dạng dữ liệu yêu cầu. ⏎ Allowed format: `application/json`. |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
| app_id ***(Bắt buộc)*** | string | ID của ứng dụng nhà phát triển (App ID). <br><br>You can find the <strong>App ID</strong> by navigating to <strong>[My Apps](https://ads.tiktok.com/marketing_api/apps/)</strong> > <strong>App Detail</strong> > <strong>Basic Information</strong>. |
| secret ***(Bắt buộc)*** | string | Khóa bí mật của ứng dụng nhà phát triển (Secret). <br><br>You can find the <strong>Secret</strong> by navigating to <strong>[My Apps](https://ads.tiktok.com/marketing_api/apps/)</strong> > <strong>App Detail</strong> > <strong>Basic Information</strong>. |
|event_type ***(Bắt buộc)***|string|Loại sự kiện Webhook mà bạn muốn đăng ký.<br><br>Các giá trị enum hỗ trợ: <ul><li>`BRAND_MENTION`: Mentions events. To learn more about the schema and sample payload of the events within this event category, see [Webhook schema](../08-use-cases/use-case-webhook.md#doc-1825113658431489).</li></ul>|

### Ví dụ lệnh cURL (Example)

```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/business/webhook/delete/' \
--header 'Content-Type: application/json' \
--data '{
    "app_id": "{{app_id}}",
    "secret": "{{secret}}",
    "event_type": "BRAND_MENTION"
}'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|code |number|Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem [Phụ lục - Mã trạng thái phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message|string|Thông báo phản hồi từ hệ thống. Xem [Phụ lục - Mã lỗi trả về](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|request_id |string|Mã nhật ký yêu cầu (request log ID) để định danh duy nhất cho mỗi lượt gọi API.  |
|data |object|Dữ liệu trả về.|
#| app_id | string | ID của ứng dụng nhà phát triển (App ID). |
#| event_type| string |Loại cấu hình sự kiện Webhook.<br><br>Các giá trị enum hỗ trợ: <ul><li>`BRAND_MENTION`: Mentions events. To learn more about the schema and sample payload of the events within this event category, see [Webhook schema](../08-use-cases/use-case-webhook.md#doc-1825113658431489).</li></ul>|

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "app_id": "{{app_id}}",
        "event_type": "VIDEO"
    }
}
```
---

## Hướng dẫn thực hành Data Retrieval (Python & cURL)

Dưới đây là mã nguồn mẫu minh họa quy trình gọi API thực tế cho phân hệ **Lượt nhắc (Mentions)**:

### cURL mẫu
```bash
curl -s -X GET "https://business-api.tiktok.com/open_api/v1.3/example/get/?advertiser_id=YOUR_ADVERTISER_ID" \
  -H "Access-Token: YOUR_ACCESS_TOKEN"
```

### Python script mẫu
```python
import requests
import json

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ADVERTISER_ID = "YOUR_ADVERTISER_ID"
BASE_URL = "https://business-api.tiktok.com/open_api/v1.3"

headers = {
    "Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}

def execute_request():
    url = f"{BASE_URL}/example/get/"
    params = {"advertiser_id": ADVERTISER_ID}
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    if data.get("code") == 0:
        print("Truy vấn thành công:", data.get("data"))
        return data.get("data")
    else:
        print(f"Lỗi: {data.get('code')} - {data.get('message')}")
        return None

if __name__ == "__main__":
    execute_request()
```

