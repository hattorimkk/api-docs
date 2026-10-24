# Tài khoản TikTok (Accounts) — phần 1/2

Tài liệu này hướng dẫn chi tiết các API thuộc nhóm Quản lý tài khoản TikTok (Accounts) — phần 1, bao gồm: kiểm tra phạm vi quyền hạn của tài khoản qua access token; xem dữ liệu chi tiết (Insights) của hồ sơ tài khoản, bài đăng, điểm chuẩn ngành hàng (benchmarks) và cài đặt quyền riêng tư bài đăng; quản lý toàn diện bình luận trên các video sở hữu (liệt kê, trả lời, tạo mới, tải ảnh, thích, ẩn, xóa bình luận); và xuất bản bài đăng video, bài đăng ảnh cũng như theo dõi trạng thái xuất bản bài đăng lên tài khoản TikTok.

| Endpoint | Method | Đường dẫn | Mục đích |
|---|---|---|---|
| Tổng quan tài khoản TikTok | - | - | Khái quát cấu trúc tài khoản TikTok và các phân nhóm API |
| Tổng quan kiểm tra token | - | - | Giới thiệu công cụ kiểm tra phạm vi quyền của access token |
| Lấy phạm vi quyền của tài khoản TikTok | `POST` | `/open_api/v1.3/tt_user/token_info/get/` | Lấy danh sách scope quyền được chủ tài khoản TikTok ủy quyền |
| Tổng quan dữ liệu chi tiết (Insights) | - | - | Giới thiệu nhóm API xem chỉ số tương tác và hồ sơ |
| Lấy dữ liệu hồ sơ tài khoản TikTok | `GET` | `/open_api/v1.3/business/get/` | Xem chỉ số tương tác hồ sơ, người theo dõi và nhân khẩu học |
| Lấy dữ liệu bài đăng video | `GET` | `/open_api/v1.3/business/video/list/` | Lấy danh sách video và các chỉ số tương tác, giữ chân người xem |
| Lấy điểm chuẩn theo ngành hàng | `GET` | `/open_api/v1.3/business/benchmark/` | Tra cứu các chỉ số đối sánh trung bình theo ngành kinh doanh |
| Lấy cài đặt quyền riêng tư bài đăng | `GET` | `/open_api/v1.3/business/video/settings/` | Kiểm tra quyền bình luận, Duet, Stitch và thời lượng video tối đa |
| Tổng quan quản lý bình luận | - | - | Giới thiệu nhóm API tương tác và quản trị bình luận video |
| Lấy danh sách bình luận trên video sở hữu | `GET` | `/open_api/v1.3/business/comment/list/` | Liệt kê các bình luận và câu trả lời trên video sở hữu |
| Lấy danh sách trả lời của bình luận | `GET` | `/open_api/v1.3/business/comment/reply/list/` | Xem tất cả các câu trả lời cho một bình luận cụ thể |
| Tạo bình luận mới trên video sở hữu | `POST` | `/open_api/v1.3/business/comment/create/` | Đăng bình luận mới (kèm văn bản hoặc ảnh) lên video sở hữu |
| Tải ảnh bình luận lên hệ thống | `POST` | `/open_api/v1.3/business/comment/image/upload/` | Tải file ảnh lên hệ thống để sử dụng trong bình luận |
| Trả lời một bình luận hiện có | `POST` | `/open_api/v1.3/business/comment/reply/create/` | Gửi câu trả lời cho một bình luận trên video sở hữu |
| Thích hoặc bỏ thích bình luận | `POST` | `/open_api/v1.3/business/comment/like/` | Thả tim hoặc hủy thả tim một bình luận trên video sở hữu |
| Ẩn hoặc bỏ ẩn bình luận | `POST` | `/open_api/v1.3/business/comment/hide/` | Thay đổi trạng thái hiển thị công khai hoặc ẩn bình luận |
| Xóa bình luận trên video sở hữu | `POST` | `/open_api/v1.3/business/comment/delete/` | Xóa vĩnh viễn một bình luận hoặc câu trả lời bình luận |
| Tổng quan xuất bản bài đăng | - | - | Giới thiệu luồng đăng tải video, ảnh lên tài khoản TikTok |
| Đăng bài viết video công khai | `POST` | `/open_api/v1.3/business/video/publish/` | Đăng video công khai hoặc lưu bản nháp lên tài khoản sở hữu |
| Đăng bài viết ảnh lên tài khoản | `POST` | `/open_api/v1.3/business/photo/publish/` | Đăng album ảnh lên tài khoản sở hữu kèm âm nhạc |
| Lấy trạng thái xuất bản bài đăng | `GET` | `/open_api/v1.3/business/publish/status/` | Tra cứu tiến độ xử lý và kết quả xuất bản bài đăng |

---

## Tổng quan tài khoản TikTok (`Accounts`)
<a id="doc-1737944775511041"></a>
<!-- doc_id: 1737944775511041 -->

Tài khoản TikTok là hồ sơ kỹ thuật số hợp nhất trên nền tảng TikTok cho phép các cá nhân, nhà sáng tạo và thương hiệu tạo nội dung đa phương tiện, tương tác với cộng đồng toàn cầu và tiến hành thương mại xã hội.

Bạn có thể tham khảo [Hướng dẫn](../10-organic-api/accounts-api.md#doc-1760334514340866) để tìm hiểu thêm về quy trình ủy quyền (authorization), xác thực (authentication) và các giới hạn tốc độ gọi (rate limits) cho Accounts API.

Nhóm API Tài khoản TikTok bao gồm các phân nhóm sau:

### 1. Kiểm tra mã truy cập (`Access token inspector`)
Cung cấp công cụ tra cứu thông tin token và kiểm tra các phạm vi quyền hạn (scopes) mà chủ tài khoản TikTok đã cấp cho ứng dụng của bạn:
- [Lấy phạm vi quyền của tài khoản TikTok qua access token](01-accounts-p1.md#doc-1765927978092545)

### 2. Dữ liệu chi tiết (`Insights`)
> [!NOTE]
> Để xem dữ liệu chi tiết và phân tích, chủ sở hữu tài khoản TikTok cần đăng ít nhất một video, sau đó nhấn nút "Bật" (Turn On) trên trang Phân tích (Analytics) của ứng dụng di động TikTok. Xem thêm chi tiết tại [hướng dẫn bật Analytics](https://www.tiktok.com/feedback?id=7133058093574806018&lang=en&type=).

Bao gồm các endpoint:
- [Lấy dữ liệu hồ sơ tài khoản TikTok](01-accounts-p1.md#doc-1762228399168514)
- [Lấy dữ liệu bài đăng video của tài khoản TikTok](01-accounts-p1.md#doc-1762228421622786)
- [Lấy điểm chuẩn theo ngành hàng](01-accounts-p1.md#doc-1822388944791617)
- [Lấy cài đặt quyền riêng tư bài đăng của tài khoản TikTok](01-accounts-p1.md#doc-1816387951979521)

### 3. Quản lý bình luận (`Comments`)
Bao gồm các endpoint tương tác và kiểm duyệt bình luận:
- [Lấy danh sách bình luận trên video sở hữu](01-accounts-p1.md#doc-1760232109619202)
- [Lấy danh sách trả lời của một bình luận](01-accounts-p1.md#doc-1762228430145538)
- [Tạo bình luận mới trên video sở hữu](01-accounts-p1.md#doc-1762228442072066)
- [Tải ảnh bình luận lên hệ thống](01-accounts-p1.md#doc-1856212334897154)
- [Trả lời một bình luận hiện có trên video sở hữu](01-accounts-p1.md#doc-1762228448779266)
- [Thích hoặc bỏ thích bình luận trên video sở hữu](01-accounts-p1.md#doc-1762228456608770)
- [Ẩn hoặc bỏ ẩn bình luận trên video sở hữu](01-accounts-p1.md#doc-1762228474532865)
- [Xóa bình luận trên video sở hữu](01-accounts-p1.md#doc-1762228483080193)

### 4. Xuất bản bài đăng (`Posts`)
Bao gồm các endpoint đăng tải nội dung:
- [Đăng bài viết video công khai lên tài khoản sở hữu](01-accounts-p1.md#doc-1762228496095234)
- [Đăng bài viết ảnh lên tài khoản sở hữu](01-accounts-p1.md#doc-1803630424390658)
- [Lấy trạng thái xuất bản bài đăng TikTok](01-accounts-p1.md#doc-1816387106635778)
- [Gợi ý hashtag cho tài khoản TikTok](01-accounts-p2.md#doc-1762228503821314)
- [Lấy danh sách thẻ vị trí cho tài khoản TikTok](01-accounts-p2.md#doc-1870580030749698)

### 5. Các nhóm khác (phần 2)
- **Ủy quyền quảng cáo (`Ad authorization`)**: Bật/tắt ủy quyền bài viết làm quảng cáo Spark Ads, gia hạn, kiểm tra trạng thái và xóa mã ủy quyền.
- **Thuộc tính URL (`URL properties`)**: Thêm tên miền/tiền tố URL, kiểm tra kết quả xác minh, xóa quyền sở hữu đã xác minh và liệt kê danh sách thuộc tính URL.
- **Hệ thống Webhook (`Webhooks`)**: Đăng ký nhận thông báo sự kiện đăng bài và bình luận theo thời gian thực.

---

## Tổng quan kiểm tra token (`Access token inspector`)
<a id="doc-1769113205729282"></a>
<!-- doc_id: 1769113205729282 -->

Nhóm API này cung cấp công cụ kiểm tra thông tin chi tiết và xác thực các phạm vi quyền hạn (permission scopes) mà tài khoản TikTok đã cấp cho ứng dụng của bạn thông qua access token.

Nhóm này bao gồm endpoint:
- [Lấy phạm vi quyền của tài khoản TikTok qua access token](01-accounts-p1.md#doc-1765927978092545)

---

## Lấy phạm vi quyền của tài khoản TikTok qua access token (`Get the authorized TikTok account permission scopes via access token`)
<a id="doc-1765927978092545"></a>
<!-- doc_id: 1765927978092545 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/tt_user/token_info/get/`

**Mục đích**: Lấy danh sách các phạm vi quyền (permission scopes) của tài khoản TikTok đã được người dùng chủ tài khoản ủy quyền cho ứng dụng của bạn. 

Nếu bạn muốn lấy danh sách phạm vi quyền của tài khoản người sáng tạo TikTok (TikTok Personal Account) được ủy quyền bởi người sáng tạo trên TikTok Creator Marketplace, xem hướng dẫn [tại đây](68-tiktok-one-p1.md#doc-1765926674648065).

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Content-Type` | string | Có | Định dạng nội dung yêu cầu. Giá trị cho phép: `application/json`. |

### Tham số (POST: JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `app_id` | string | Có | ID của ứng dụng nhà phát triển. Bạn có thể tìm thấy **App ID** bằng cách truy cập **[My Apps](https://ads.tiktok.com/marketing_api/apps/)** > **App Detail** > **Basic Information**. |
| `access_token` | string | Có | Access token được ủy quyền bởi tài khoản TikTok. Chi tiết xem tại [Xác thực](../10-organic-api/accounts-api.md#doc-1738084387220481). |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Xem chi tiết tại [Phụ lục mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). Giá trị `0` là thành công. |
| `message` | string | Thông báo phản hồi. Chi tiết xem [Phụ lục mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `request_id` | string | Mã log định danh duy nhất của yêu cầu API. |
| `data` | object | Dữ liệu trả về. |
| ↳ `app_id` | string | ID của ứng dụng nhà phát triển. |
| ↳ `scope` | string | Danh sách các phạm vi quyền (scopes) được cấp cho access token chỉ định, cách nhau bởi dấu phẩy. Ví dụ: `"user.info.basic,video.list"`. |
| ↳ `creator_id` | string | Mã định danh duy nhất theo ứng dụng của tài khoản TikTok.<br><br>> [!NOTE]<br>> Bạn có thể truyền giá trị của trường này vào tham số `business_id` trong các yêu cầu gọi [Accounts API](01-accounts-p1.md#doc-1737944775511041). |

### Ví dụ

#### cURL
```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/tt_user/token_info/get/" \
  -H "Content-Type: application/json" \
  -d '{
    "app_id": "your_app_id",
    "access_token": "your_access_token"
  }'
```

#### Phản hồi mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202410231500000201111222333444555",
  "data": {
    "app_id": "your_app_id",
    "creator_id": "6789012345678901234",
    "scope": "video.publish,user.info.basic,video.list,user.insights,user.insights.creator,tcm.order.update,comment.list.manage,video.insights,comment.list"
  }
}
```

---

## Tổng quan dữ liệu chi tiết (`Insights`)
<a id="doc-1769113237682177"></a>
<!-- doc_id: 1769113237682177 -->

Nhóm API Dữ liệu chi tiết (Insights) cho phép nhà phát triển truy cập các số liệu thống kê hiệu suất chuyên sâu của tài khoản TikTok: từ chỉ số hồ sơ, tăng trưởng người theo dõi, nhân khẩu học người xem, cho đến hiệu suất chi tiết của từng bài đăng video, số liệu đối sánh ngành (benchmarks) và cấu hình quyền riêng tư khi đăng tải.

Nhóm này bao gồm các endpoint:
- [Lấy dữ liệu hồ sơ tài khoản TikTok](01-accounts-p1.md#doc-1762228399168514): Truy cập dữ liệu phân tích hồ sơ và người theo dõi.
- [Lấy dữ liệu bài đăng video của tài khoản TikTok](01-accounts-p1.md#doc-1762228421622786): Lấy danh sách video và chỉ số tương tác, giữ chân người xem.
- [Lấy điểm chuẩn theo ngành hàng](01-accounts-p1.md#doc-1822388944791617): Lấy các chỉ số trung bình theo danh mục ngành để so sánh hiệu suất.
- [Lấy cài đặt quyền riêng tư bài đăng của tài khoản TikTok](01-accounts-p1.md#doc-1816387951979521): Kiểm tra các tùy chọn hiển thị và quyền tương tác khả dụng khi đăng bài.
---

## Lấy dữ liệu hồ sơ tài khoản TikTok (`Get profile data of a TikTok account`)
<a id="doc-1762228399168514"></a>
<!-- doc_id: 1762228399168514 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/business/get/`

**Mục đích**: Truy cập các dữ liệu phân tích chi tiết và thông tin chi tiết (insights) về lượng người theo dõi, tương tác hồ sơ, hiệu suất video tổng thể và đặc điểm nhân khẩu học của một tài khoản TikTok.

> [!IMPORTANT]
> - Để đảm bảo việc sử dụng Accounts API đúng quy định, bắt đầu từ ngày 20/03/2026 lúc 00:00 (GMT+0), nhà phát triển bắt buộc phải hoàn thành [Biểu mẫu đăng ký quyền truy cập Accounts API](https://bytedance.sg.larkoffice.com/share/base/form/shrlgu4WEvtSXpEDLcCw56u4Rfc) trước khi gửi ứng dụng mới hoặc yêu cầu mở rộng phạm vi quyền hạn bao gồm phạm vi "TikTok Accounts". Vui lòng xem thêm tại tài liệu [Accounts API](../10-organic-api/accounts-api.md#doc-1737944384433218).

> [!NOTE]
> - **Độ trễ dữ liệu**: Có độ trễ từ 24 đến 48 giờ đối với một số chỉ số cấp hồ sơ. Chi tiết về độ trễ dữ liệu có thể xem trong bảng mô tả phản hồi hoặc tại [Bảng tham chiếu độ trễ dữ liệu Accounts Insights](../10-organic-api/accounts-api.md#doc-1746624508278786).
> - **Điều kiện hiển thị dữ liệu**: Dữ liệu lấy được phụ thuộc vào dữ liệu TikTok Analytics tương ứng hiển thị trong ứng dụng và tại `https://www.tiktok.com/analytics`. Nếu số liệu bị thiếu trong TikTok Analytics, API sẽ không trả về số liệu đó. Chủ tài khoản TikTok cần đăng ít nhất một video và kích hoạt tính năng Analytics bằng cách bấm nút "Bật" trong ứng dụng di động TikTok.
> - **Chỉ số lượt xem video**: Trường `video_views` là chỉ số tổng hợp, bao gồm cả lượt xem tự nhiên (organic) và lượt xem từ quảng cáo trả phí (paid).

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Có | Access token được ủy quyền bởi người sáng tạo TikTok. Để lấy mã truy cập, sử dụng [/tt_user/oauth2/token/](10-authentication.md#doc-1833997638479041). |

### Tham số (GET: query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `business_id` | string | Có | Mã định danh duy nhất theo ứng dụng của tài khoản TikTok. Truyền giá trị trường `open_id` nhận được từ [/tt_user/oauth2/token/](10-authentication.md#doc-1833997638479041). |
| `start_date` | string | Không | Ngày bắt đầu truy vấn (khoảng đóng), định dạng `YYYY-MM-DD` theo múi giờ UTC. Ví dụ: `2021-06-01`. Nếu không chỉ định, mặc định là `[ngày hiện tại - 7 ngày]`. Khoảng thời gian tra cứu tối đa là 60 ngày. |
| `end_date` | string | Không | Ngày kết thúc truy vấn (khoảng đóng), định dạng `YYYY-MM-DD` theo múi giờ UTC. Ví dụ: `2021-06-01`. Nếu không chỉ định, mặc định là `[ngày hiện tại - 1 ngày]`. |
| `fields` | string[] | Không | Danh sách các trường cần lấy trong phản hồi. Nếu không đặt, API chỉ trả về các trường mặc định: `["display_name", "profile_image"]`.<br><br>Để truy xuất một số trường đặc thù, bạn phải có quyền tương ứng trong scope token (kiểm tra qua [/tt_user/token_info/get/](01-accounts-p1.md#doc-1765927978092545)). Lưu ý: Khi gọi qua query string, trường này cần được truyền dưới dạng mảng JSON (ví dụ: `fields=["display_name","profile_image","metrics"]`).<br><br>**Các trường hỗ trợ**:<br>• `is_business_account`: Tài khoản doanh nghiệp TikTok đã xác minh (cần quyền `user.account.type`).<br>• `has_advanced_access`: Tài khoản có quyền truy cập nâng cao Advanced Access (cần quyền `user.account.type`).<br>• `profile_image`: URL tạm thời của ảnh đại diện (cần quyền `user.info.basic`).<br>• `username`: Tên người dùng tài khoản TikTok (cần quyền `user.info.username`).<br>• `profile_deep_link`: Liên kết sâu đến trang hồ sơ (cần quyền `user.info.profile`).<br>• `display_name`: Tên hiển thị của tài khoản (cần quyền `user.info.basic`).<br>• `bio_description`: Tiểu sử tài khoản (cần quyền `user.info.profile`).<br>• `is_verified`: Trạng thái có huy hiệu xác minh (cần quyền `user.info.profile`).<br>• `following_count`: Số tài khoản đang theo dõi (cần quyền `user.info.stats`).<br>• `followers_count`: Tổng số người theo dõi (cần quyền `user.info.stats`).<br>• `total_likes`: Tổng lượt thích các video (cần quyền `user.info.stats`).<br>• `videos_count`: Số lượng video công khai đã đăng (cần quyền `user.info.stats`).<br>• `metrics`: Danh sách các chỉ số phân tích hàng ngày (cần quyền `user.insights`).<br>• `audience_activity`: Hoạt động người xem theo giờ (cần quyền `user.insights`).<br>• `engaged_audience`: Số lượng khán giả đã tương tác (cần quyền `user.insights`).<br>• `audience_ages`: Phân bố độ tuổi của người theo dõi (cần quyền `user.insights`).<br>• `audience_genders`: Phân bố giới tính của người theo dõi (cần quyền `user.insights`).<br>• `audience_countries`: Phân bố quốc gia của người theo dõi (cần quyền `user.insights`).<br>• `audience_cities`: Phân bố thành phố của người theo dõi (cần quyền `user.insights`). |

### Header phản hồi

- `Date`: Thời gian GMT nhận được phản hồi, ví dụ: `Fri, 13 Aug 2021 08:04:42 GMT`.
- `X-Tt-Logid`: Mã định danh duy nhất của yêu cầu API (cần ghi lại để tra cứu và gỡ lỗi).

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Xem chi tiết tại [Phụ lục mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). Giá trị `0` là thành công. |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Mã log định danh duy nhất của yêu cầu API. |
| `data` | object | Dữ liệu trả về. |
| ↳ `is_business_account` | boolean | Cho biết tài khoản TikTok có phải là Tài khoản doanh nghiệp đã xác minh (Verified Business Account) hay không. |
| ↳ `has_advanced_access` | boolean | Cho biết tài khoản TikTok có quyền truy cập nâng cao (TikTok Account with Advanced Access) hay không. |
| ↳ `profile_image` | string | URL tạm thời của ảnh đại diện hồ sơ. Thời gian hết hạn được chỉ định trong tham số `x-expires` theo định dạng Epoch/Unix timestamp. Cập nhật theo thời gian thực. |
| ↳ `username` | string | Tên người dùng (handle) của tài khoản TikTok. Cập nhật theo thời gian thực. |
| ↳ `profile_deep_link` | string | Liên kết dẫn đến trang hồ sơ của tài khoản TikTok. Cập nhật theo thời gian thực. |
| ↳ `display_name` | string | Tên hiển thị (biệt danh) của tài khoản TikTok. Cập nhật theo thời gian thực. |
| ↳ `bio_description` | string | Mô tả tiểu sử (bio) của tài khoản TikTok. Nếu chưa đặt tiểu sử, giá trị trả về là chuỗi rỗng (`""`). |
| ↳ `is_verified` | boolean | Cho biết tài khoản đã được cấp huy hiệu xác minh từ TikTok hay chưa. |
| ↳ `following_count` | integer | Tổng số lượng tài khoản mà tài khoản TikTok này đang theo dõi. |
| ↳ `followers_count` | integer | Tổng số lượng người theo dõi của tài khoản TikTok. |
| ↳ `total_likes` | integer | Tổng số lượt thích mà các video đã xuất bản của tài khoản nhận được. |
| ↳ `videos_count` | integer | Tổng số lượng video công khai đã đăng của tài khoản TikTok. |
| ↳ `metrics` | object[] | Danh sách các chỉ số phân tích hàng ngày được yêu cầu. Dữ liệu chỉ trả về cho các ngày sau khi tài khoản được tạo và có độ trễ 24–48 giờ. |
| ↳↳ `date` | string | Ngày của tập chỉ số hàng ngày, định dạng `YYYY-MM-DD` theo múi giờ UTC. |
| ↳↳ `video_views` | integer | Số lượt xem video hàng ngày (tính khi thời lượng phát lại > 0 và là lần phát đầu tiên trong một phiên hiển thị). Nguồn dữ liệu: TikTok Studio. |
| ↳↳ `unique_video_views` | integer | Số lượng người tiếp cận hàng ngày (số người dùng duy nhất đã xem nội dung ít nhất một lần). Nguồn dữ liệu: Business Analytics. *(Chỉ áp dụng cho tài khoản có Advanced Access hoặc Verified Business Account).* |
| ↳↳ `profile_views` | integer | Số lượt xem hồ sơ trong ngày. |
| ↳↳ `likes` | integer | Số lượt thích nhận được trong ngày. |
| ↳↳ `comments` | integer | Số lượt bình luận nhận được trong ngày. |
| ↳↳ `shares` | integer | Số lượt chia sẻ nhận được trong ngày. |
| ↳↳ `phone_number_clicks` | integer | Số lượt nhấp vào số điện thoại trên hồ sơ trong ngày. |
| ↳↳ `lead_submissions` | integer | Số lượt gửi biểu mẫu khách hàng tiềm năng nhận được trong ngày. |
| ↳↳ `app_download_clicks` | integer | Số lượt nhấp vào liên kết tải ứng dụng trong ngày. |
| ↳↳ `bio_link_clicks` | integer | Số lượt nhấp vào liên kết trang web trong tiểu sử (bio) trong ngày. |
| ↳↳ `email_clicks` | integer | Số lượt nhấp vào nút email trong ngày. |
| ↳↳ `address_clicks` | integer | Số lượt nhấp vào địa chỉ doanh nghiệp trong ngày. |
| ↳↳ `daily_total_followers` | integer | Tổng số người theo dõi của tài khoản vào ngày tương ứng. |
| ↳↳ `daily_new_followers` | integer | Số người theo dõi mới nhận được trong ngày. |
| ↳↳ `daily_lost_followers` | integer | Số người theo dõi đã hủy theo dõi trong ngày. |
| ↳ `audience_activity` | object[] | Dữ liệu hoạt động trực tuyến của người theo dõi theo từng khung giờ trong ngày. |
| ↳↳ `hour` | string | Khung giờ trong ngày (từ `0` đến `23` theo múi giờ UTC). |
| ↳↳ `count` | integer | Số lượng người theo dõi hoạt động trực tuyến trong khung giờ đó. |
| ↳ `engaged_audience` | integer | Tổng số lượng người dùng đã tương tác với hồ sơ hoặc nội dung trong khoảng thời gian đã chọn. |
| ↳ `audience_ages` | object[] | Phân bố độ tuổi của người theo dõi. |
| ↳↳ `age` | string | Nhóm tuổi (ví dụ: `18-24`, `25-34`, `35-44`, `45-54`, `55+`). |
| ↳↳ `percentage` | float | Tỷ lệ phần trăm người theo dõi thuộc nhóm tuổi (từ `0` đến `1`). |
| ↳ `audience_genders` | object[] | Phân bố giới tính của người theo dõi. |
| ↳↳ `gender` | string | Giới tính (`Female`, `Male`, `Other`). |
| ↳↳ `percentage` | float | Tỷ lệ phần trăm người theo dõi thuộc giới tính tương ứng. |
| ↳ `audience_countries` | object[] | Phân bố người theo dõi theo quốc gia. |
| ↳↳ `country` | string | Mã hoặc tên quốc gia. |
| ↳↳ `percentage` | float | Tỷ lệ phần trăm người theo dõi từ quốc gia tương ứng. |
| ↳ `audience_cities` | object[] | Phân bố người theo dõi theo thành phố. |
| ↳↳ `city_name` | string | Tên thành phố. |
| ↳↳ `percentage` | float | Tỷ lệ phần trăm người theo dõi từ thành phố tương ứng. |

### Ví dụ

#### cURL
```bash
curl -X GET "https://business-api.tiktok.com/open_api/v1.3/business/get/?business_id=6789012345678901234&start_date=2024-10-01&end_date=2024-10-07&fields=%5B%22display_name%22%2C%22followers_count%22%2C%22metrics%22%5D" \
  -H "Access-Token: ACCESS_TOKEN"
```

#### Python
```python
import json
import requests

ACCESS_TOKEN = "your_access_token"
BUSINESS_ID = "6789012345678901234"

url = "https://business-api.tiktok.com/open_api/v1.3/business/get/"
headers = {"Access-Token": ACCESS_TOKEN}
params = {
    "business_id": BUSINESS_ID,
    "start_date": "2024-10-01",
    "end_date": "2024-10-07",
    "fields": json.dumps(["display_name", "followers_count", "metrics"])
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

#### Phản hồi mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20241023150000020222333444555666",
  "data": {
    "display_name": "TikTok Shop Vietnam",
    "followers_count": 524000,
    "following_count": 12,
    "is_business_account": true,
    "is_verified": true,
    "profile_image": "https://p16-sign-va.tiktokcdn.com/tos-maliva-avt-0068/75dec21d63500917fb6ec8bc59415156~c5_300x300.jpeg?x-expires=1730000000",
    "total_likes": 12500000,
    "username": "tiktokshop_vn",
    "videos_count": 320,
    "metrics": [
      {
        "date": "2024-10-01",
        "video_views": 154200,
        "unique_video_views": 112000,
        "profile_views": 4200,
        "likes": 8500,
        "comments": 620,
        "shares": 340,
        "daily_total_followers": 523500,
        "daily_new_followers": 650,
        "daily_lost_followers": 150
      }
    ]
  }
}
```
---

## Lấy dữ liệu bài đăng video của tài khoản TikTok (`Get post data of a TikTok account`)
<a id="doc-1762228421622786"></a>
<!-- doc_id: 1762228421622786 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/business/video/list/`

**Mục đích**: Lấy danh sách các bài đăng video công khai của tài khoản TikTok cùng với các chỉ số hiệu suất chi tiết (lượt xem, tương tác, thời lượng xem, tỷ lệ xem hết, giữ chân người xem và nguồn hiển thị).

> [!NOTE]
> - **Độ trễ dữ liệu**: Một số chỉ số cấp độ video có độ trễ từ 24 đến 48 giờ. Xem chi tiết tại [Bảng tham chiếu độ trễ dữ liệu](../10-organic-api/accounts-api.md#doc-1746624508278786).
> - Để xem dữ liệu chi tiết của video, chủ sở hữu tài khoản TikTok cần kích hoạt tính năng Analytics trong ứng dụng TikTok.
> - Số liệu `video_views` là tổng lượt xem bao gồm cả lượt xem tự nhiên (organic) và trả phí (paid).

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Có | Access token được ủy quyền bởi người sáng tạo TikTok. Dùng [/tt_user/oauth2/token/](10-authentication.md#doc-1833997638479041). |

### Tham số (GET: query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `business_id` | string | Có | Mã định danh duy nhất theo ứng dụng của tài khoản TikTok (`open_id`). |
| `fields` | string[] | Không | Danh sách các trường cần lấy cho mỗi video. Nếu không chỉ định, trả về các trường mặc định: `["item_id"]`.<br><br>Khi gọi qua query string, truyền dưới dạng chuỗi mảng JSON (ví dụ: `fields=["item_id","caption","likes","video_views"]`).<br><br>**Các trường hỗ trợ**:<br>• Thông tin cơ bản: `item_id`, `media_type`, `is_ad`, `thumbnail_url`, `share_url`, `embed_url`, `caption`, `video_duration`, `create_time`.<br>• Tương tác: `likes`, `comments`, `shares`, `favorites`.<br>• Hiệu suất video: `reach`, `video_views`, `total_time_watched`, `average_time_watched`, `full_video_watched_rate`, `new_followers`, `profile_views`.<br>• Lượt nhấp hành động: `website_clicks`, `phone_number_clicks`, `lead_submissions`, `app_download_clicks`, `email_clicks`, `address_clicks`.<br>• Biểu đồ chuyên sâu: `video_view_retention`, `impression_sources`, `audience_genders`, `audience_countries`, `audience_cities`, `audience_types`, `engagement_likes`. |
| `filters` | object | Không | Bộ lọc dữ liệu bài đăng. Truyền dưới dạng chuỗi JSON object.<br><br>**Các trường con**:<br>• ↳ `video_ids` (string[]): Danh sách ID bài đăng video cụ thể cần lọc. Tối đa 50 ID.<br>• ↳ `ad_post_only` (boolean): Lọc bài đăng chỉ quảng cáo (Spark Ads) hay bài đăng tự nhiên. |
| `cursor` | integer | Không | Con trỏ phân trang. Truyền giá trị `cursor` nhận được từ trang trước để lấy trang kết quả tiếp theo. Mặc định: `0`. |
| `max_count` | integer | Không | Số lượng bài đăng tối đa trả về trên mỗi trang. Giá trị từ `1` đến `50`. Mặc định: `20`. |

### Header phản hồi

- `Date`: Thời gian nhận phản hồi (GMT).
- `X-Tt-Logid`: Mã định danh duy nhất của yêu cầu API.

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Xem chi tiết tại [Phụ lục mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). Giá trị `0` là thành công. |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Mã log định danh duy nhất của yêu cầu API. |
| `data` | object | Dữ liệu trả về. |
| ↳ `videos` | object[] | Danh sách các video và chỉ số chi tiết. |
| ↳↳ `item_id` | string | ID duy nhất của bài đăng TikTok. |
| ↳↳ `media_type` | string | Loại nội dung đa phương tiện (`VIDEO` hoặc `PHOTO`). |
| ↳↳ `is_ad` | boolean | Cho biết bài đăng có đang được quảng cáo hay không. |
| ↳↳ `thumbnail_url` | string | URL ảnh thu nhỏ của video (có thời hạn hết hạn). |
| ↳↳ `share_url` | string | URL liên kết chia sẻ công khai của video trên TikTok. |
| ↳↳ `embed_url` | string | URL mã nhúng (embed) video. |
| ↳↳ `caption` | string | Nội dung tiêu đề/chú thích của bài đăng (bao gồm cả hashtag). |
| ↳↳ `video_duration` | float | Thời lượng của video tính bằng giây. |
| ↳↳ `create_time` | string | Thời điểm đăng video theo định dạng `YYYY-MM-DD HH:MM:SS` (UTC). |
| ↳↳ `likes` | integer | Tổng số lượt thích video. |
| ↳↳ `comments` | integer | Tổng số bình luận trên video. |
| ↳↳ `shares` | integer | Tổng số lượt chia sẻ video. |
| ↳↳ `favorites` | integer | Tổng số lượt thêm video vào danh sách yêu thích. |
| ↳↳ `reach` | integer | Số lượng tài khoản duy nhất đã xem video ít nhất một lần. |
| ↳↳ `video_views` | integer | Tổng số lượt xem video (bao gồm organic và paid). |
| ↳↳ `total_time_watched` | float | Tổng thời gian người xem đã xem video tính bằng giây. |
| ↳↳ `average_time_watched` | float | Thời gian xem trung bình của mỗi lượt xem tính bằng giây. |
| ↳↳ `full_video_watched_rate` | float | Tỷ lệ người xem xem hết toàn bộ video (từ `0` đến `1`). |
| ↳↳ `new_followers` | integer | Số lượng người theo dõi mới có được trực tiếp từ video này. |
| ↳↳ `profile_views` | integer | Số lượt truy cập hồ sơ bắt nguồn từ video này. |
| ↳↳ `website_clicks` | integer | Số lượt nhấp vào liên kết trang web. |
| ↳↳ `phone_number_clicks` | integer | Số lượt nhấp vào số điện thoại liên hệ. |
| ↳↳ `lead_submissions` | integer | Số lượng biểu mẫu khách hàng tiềm năng gửi từ video. |
| ↳↳ `app_download_clicks` | integer | Số lượt nhấp vào liên kết tải ứng dụng. |
| ↳↳ `email_clicks` | integer | Số lượt nhấp gửi email. |
| ↳↳ `address_clicks` | integer | Số lượt nhấp xem địa chỉ. |
| ↳↳ `video_view_retention` | object[] | Dữ liệu tỷ lệ giữ chân người xem theo từng giây của video (`second`: giây, `percentage`: tỷ lệ phần trăm còn xem). |
| ↳↳ `impression_sources` | object[] | Phân bố nguồn hiển thị video (`impression_source`: nguồn như For You, Following, Profile, Sound; `percentage`: tỷ lệ). |
| ↳↳ `audience_genders` | object[] | Phân bố giới tính người xem video (`gender`, `percentage`). |
| ↳↳ `audience_countries` | object[] | Phân bố quốc gia của người xem video (`country`, `percentage`). |
| ↳↳ `audience_cities` | object[] | Phân bố thành phố của người xem video (`city_name`, `percentage`). |
| ↳↳ `audience_types` | object[] | Phân bố loại khán giả (`type`: Người theo dõi mới hoặc Người theo dõi cũ, `percentage`). |
| ↳↳ `engagement_likes` | object[] | Thời điểm người xem bấm thích video theo từng mốc giây (`second`, `percentage`). |
| ↳ `cursor` | integer | Con trỏ phân trang cho trang kế tiếp. |
| ↳ `has_more` | boolean | Cho biết còn dữ liệu ở các trang tiếp theo hay không. |

### Ví dụ

#### cURL
```bash
curl -X GET "https://business-api.tiktok.com/open_api/v1.3/business/video/list/?business_id=6789012345678901234&max_count=10&fields=%5B%22item_id%22%2C%22caption%22%2C%22likes%22%2C%22video_views%22%5D" \
  -H "Access-Token: ACCESS_TOKEN"
```

#### Python
```python
import json
import requests

ACCESS_TOKEN = "your_access_token"
BUSINESS_ID = "6789012345678901234"

url = "https://business-api.tiktok.com/open_api/v1.3/business/video/list/"
headers = {"Access-Token": ACCESS_TOKEN}
params = {
    "business_id": BUSINESS_ID,
    "max_count": 10,
    "fields": json.dumps(["item_id", "caption", "likes", "video_views"])
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

#### Phản hồi mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20241023150000020333444555666777",
  "data": {
    "cursor": 10,
    "has_more": true,
    "videos": [
      {
        "caption": "Khai trương cửa hàng mới! #khaitruong #tiktokshop",
        "comments": 45,
        "create_time": "2024-10-15 10:30:00",
        "favorites": 120,
        "is_ad": false,
        "item_id": "7123456789123456789",
        "likes": 2300,
        "media_type": "VIDEO",
        "share_url": "https://www.tiktok.com/@tiktokshop_vn/video/7123456789123456789",
        "shares": 80,
        "thumbnail_url": "https://p16-sign-va.tiktokcdn.com/tos-maliva-p/thumb.jpeg",
        "video_duration": 45.2,
        "video_views": 35000
      }
    ]
  }
}
```

---

## Lấy điểm chuẩn theo ngành hàng (`Get benchmarks for a business category`)
<a id="doc-1822388944791617"></a>
<!-- doc_id: 1822388944791617 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/business/benchmark/`

**Mục đích**: Lấy các số liệu đối sánh điểm chuẩn (benchmarks) trung bình theo danh mục ngành nghề kinh doanh. Sau khi nhận được điểm chuẩn ngành, bạn có thể so sánh với dữ liệu hồ sơ từ [/business/get/](01-accounts-p1.md#doc-1762228399168514) của [Tài khoản doanh nghiệp đã xác minh](https://ads.tiktok.com/resources/help/article/how-to-register-a-business-account) để đánh giá hiệu suất so với tiêu chuẩn ngành.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Có | Access token được ủy quyền bởi người sáng tạo TikTok. Dùng [/tt_user/oauth2/token/](10-authentication.md#doc-1833997638479041). |

### Tham số (GET: query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `business_id` | string | Có | Mã định danh duy nhất theo ứng dụng của tài khoản TikTok (`open_id`). |
| `business_category` | string | Có | Danh mục kinh doanh cần tra cứu điểm chuẩn. Ví dụ: `ART_AND_CRAFTS`.<br><br>**Các giá trị enum**:<br>• `ART_AND_CRAFTS`: Nghệ thuật & Thủ công<br>• `AUTOMOTIVE_AND_TRANSPORTATION`: Ô tô & Vận tải<br>• `BABY`: Mẹ & Bé<br>• `BEAUTY`: Sắc đẹp<br>• `CLOTHING_AND_ACCESSORIES`: Quần áo & Phụ kiện thời trang<br>• `EDUCATION_AND_TRAINING`: Giáo dục & Đào tạo<br>• `ELECTRONICS`: Điện tử & Công nghệ<br>• `FINANCE_AND_INVESTING`: Tài chính & Đầu tư<br>• `FOOD_AND_BEVERAGE`: Thực phẩm & Đồ uống<br>• `GAMING`: Trò chơi điện tử (Gaming)<br>• `HEALTH_AND_WELLNESS`: Sức khỏe & Thể chất<br>• `HOME_FURNITURE_AND_APPLIANCES`: Nhà cửa, Nội thất & Đồ gia dụng<br>• `MACHINERY_AND_EQUIPMENT`: Máy móc & Thiết bị<br>• `MEDIA_AND_ENTERTAINMENT`: Truyền thông & Giải trí<br>• `PERSONAL_BLOG`: Blog cá nhân<br>• `PETS`: Thú cưng<br>• `PROFESSIONAL_SERVICES`: Dịch vụ chuyên nghiệp<br>• `PUBLIC_ADMINISTRATION`: Hành chính công<br>• `REAL_ESTATE`: Bất động sản<br>• `RESTAURANTS_AND_BARS`: Nhà hàng & Quán bar<br>• `SHOPPING_AND_RETAIL`: Mua sắm & Bán lẻ<br>• `SOFTWARE_AND_APPS`: Phần mềm & Ứng dụng<br>• `SPORTS_FITNESS_AND_OUTDOORS`: Thể thao, Thể hình & Dã ngoại<br>• `TRAVEL_AND_TOURISM`: Du lịch & Khách sạn<br>• `OTHERS`: Ngành nghề khác |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Xem chi tiết tại [Phụ lục mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Mã log định danh duy nhất của yêu cầu API. |
| `data` | object | Dữ liệu trả về. |
| ↳ `business_category` | string | Tên danh mục kinh doanh (ví dụ: `Art & Crafts`). Giá trị hiển thị này có định dạng đẹp hơn giá trị enum trong yêu cầu. |
| ↳ `average_likes` | double | Số lượt thích trung bình trên các video thuộc các Tài khoản doanh nghiệp đã xác minh trong ngành. |
| ↳ `average_comments` | double | Số lượng bình luận trung bình trên các video trong ngành. |
| ↳ `average_shares` | double | Số lượt chia sẻ trung bình trên các video trong ngành. |
| ↳ `average_video_count` | double | Số lượng video trung bình được đăng tải bởi các tài khoản trong ngành. |
| ↳ `average_follower_count` | double | Số lượng người theo dõi trung bình của các tài khoản trong ngành. |
| ↳ `average_follower_growth` | double | Mức tăng trưởng người theo dõi trung bình trong 30 ngày qua của các tài khoản trong ngành. |
| ↳ `average_engagement_rate` | double | Tỷ lệ tương tác trung bình (engagement rate) của các tài khoản trong ngành. |
| ↳ `average_video_views` | double | Số lượt xem video trung bình của các tài khoản trong ngành. |

### Ví dụ

#### cURL
```bash
curl -X GET "https://business-api.tiktok.com/open_api/v1.3/business/benchmark/?business_id=6789012345678901234&business_category=ART_AND_CRAFTS" \
  -H "Access-Token: ACCESS_TOKEN"
```

#### Python
```python
import requests

ACCESS_TOKEN = "your_access_token"
BUSINESS_ID = "6789012345678901234"

url = "https://business-api.tiktok.com/open_api/v1.3/business/benchmark/"
headers = {"Access-Token": ACCESS_TOKEN}
params = {
    "business_id": BUSINESS_ID,
    "business_category": "ART_AND_CRAFTS"
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

#### Phản hồi mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20241023150000020444555666777888",
  "data": {
    "average_comments": 625.6003,
    "average_engagement_rate": 0.0449,
    "average_follower_count": 1592.5344,
    "average_follower_growth": 24.9218,
    "average_likes": 22618.7106,
    "average_shares": 1161.3881,
    "average_video_count": 138.9494,
    "average_video_views": 353527.9227,
    "business_category": "Art & Crafts"
  }
}
```

---

## Lấy cài đặt quyền riêng tư bài đăng của tài khoản TikTok (`Get the post privacy settings of a TikTok account`)
<a id="doc-1816387951979521"></a>
<!-- doc_id: 1816387951979521 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/business/video/settings/`

**Mục đích**: Lấy các thiết lập quyền riêng tư áp dụng cho bài đăng của tài khoản TikTok, bao gồm các tùy chọn phạm vi hiển thị, trạng thái bật/tắt bình luận, tính năng Duet, tính năng Stitch và thời lượng video tối đa được phép xuất bản.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Có | Access token được ủy quyền bởi người sáng tạo TikTok. Dùng [/tt_user/oauth2/token/](10-authentication.md#doc-1833997638479041). |

### Tham số (GET: query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `business_id` | string | Có | Mã định danh duy nhất theo ứng dụng của tài khoản TikTok (`open_id`). |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Xem chi tiết tại [Phụ lục mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Mã log định danh duy nhất của yêu cầu API. |
| `data` | object | Dữ liệu trả về. |
| ↳ `privacy_level_options` | string[] | Danh sách các tùy chọn mức độ riêng tư khả dụng khi đăng bài của tài khoản:<br>• Nếu là tài khoản công khai: `PUBLIC_TO_EVERYONE` (Mọi người), `MUTUAL_FOLLOW_FRIENDS` (Bạn bè theo dõi lẫn nhau), `SELF_ONLY` (Chỉ mình tôi).<br>• Nếu là tài khoản riêng tư: `FOLLOWER_OF_CREATOR` (Người theo dõi), `MUTUAL_FOLLOW_FRIENDS` (Bạn bè), `SELF_ONLY` (Chỉ mình tôi). |
| ↳ `comment_disabled` | boolean | Cho biết cài đặt "Cho phép bình luận" có bị vô hiệu hóa hay không.<br>• `true`: Bị vô hiệu hóa. Bạn không thể bật bình luận khi đăng bài (do tài khoản đang cài đặt chặn bình luận từ mọi người).<br>• `false`: Khả dụng. Bạn có thể tự do bật hoặc tắt bình luận cho bài đăng. |
| ↳ `duet_disabled` | boolean | Cho biết cài đặt "Cho phép Duet" có bị vô hiệu hóa hay không.<br>• `true`: Bị vô hiệu hóa (nếu tài khoản là riêng tư hoặc cài đặt Duet là "Chỉ mình tôi").<br>• `false`: Khả dụng. |
| ↳ `stitch_disabled` | boolean | Cho biết cài đặt "Cho phép Stitch" có bị vô hiệu hóa hay không.<br>• `true`: Bị vô hiệu hóa (nếu tài khoản là riêng tư hoặc cài đặt Stitch là "Chỉ mình tôi").<br>• `false`: Khả dụng. |
| ↳ `max_video_post_duration_sec` | number | Thời lượng tối đa (tính bằng giây) cho bài đăng video mà tài khoản có thể xuất bản. Nếu cố gắng xuất bản video dài hơn thời lượng này qua [/business/video/publish/](01-accounts-p1.md#doc-1762228496095234), yêu cầu sẽ thất bại. |

### Ví dụ

#### cURL
```bash
curl -X GET "https://business-api.tiktok.com/open_api/v1.3/business/video/settings/?business_id=6789012345678901234" \
  -H "Access-Token: ACCESS_TOKEN"
```

#### Python
```python
import requests

ACCESS_TOKEN = "your_access_token"
BUSINESS_ID = "6789012345678901234"

url = "https://business-api.tiktok.com/open_api/v1.3/business/video/settings/"
headers = {"Access-Token": ACCESS_TOKEN}
params = {"business_id": BUSINESS_ID}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

#### Phản hồi mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20241023150000020555666777888999",
  "data": {
    "comment_disabled": false,
    "duet_disabled": false,
    "max_video_post_duration_sec": 600,
    "privacy_level_options": [
      "PUBLIC_TO_EVERYONE",
      "MUTUAL_FOLLOW_FRIENDS",
      "SELF_ONLY"
    ],
    "stitch_disabled": false
  }
}
```
---

## Tổng quan quản lý bình luận (`Comments`)
<a id="doc-1769113255352322"></a>
<!-- doc_id: 1769113255352322 -->

Nhóm API Bình luận (Comments) cung cấp các công cụ toàn diện giúp doanh nghiệp và nhà phát triển quản lý, theo dõi và tương tác với các bình luận trên những video tự nhiên thuộc tài khoản TikTok sở hữu:
- [Lấy danh sách bình luận trên video sở hữu](01-accounts-p1.md#doc-1760232109619202): Liệt kê bình luận cấp cao nhất hoặc kèm câu trả lời.
- [Lấy danh sách trả lời của một bình luận](01-accounts-p1.md#doc-1762228430145538): Tra cứu tất cả các câu trả lời trực tiếp cho một bình luận cụ thể.
- [Tạo bình luận mới trên video sở hữu](01-accounts-p1.md#doc-1762228442072066): Đăng bình luận mới bằng văn bản hoặc hình ảnh.
- [Tải ảnh bình luận lên hệ thống](01-accounts-p1.md#doc-1856212334897154): Tải ảnh lên máy chủ TikTok để lấy mã URI dùng cho bình luận ảnh.
- [Trả lời một bình luận hiện có trên video sở hữu](01-accounts-p1.md#doc-1762228448779266): Gửi phản hồi cho một bình luận cụ thể.
- [Thích hoặc bỏ thích bình luận trên video sở hữu](01-accounts-p1.md#doc-1762228456608770): Tương tác thích/bỏ thích với vai trò chủ sở hữu video.
- [Ẩn hoặc bỏ ẩn bình luận trên video sở hữu](01-accounts-p1.md#doc-1762228474532865): Quản lý hiển thị công khai hoặc ẩn bình luận khỏi người xem khác.
- [Xóa bình luận trên video sở hữu](01-accounts-p1.md#doc-1762228483080193): Xóa vĩnh viễn bình luận hoặc câu trả lời bình luận.

---

## Lấy danh sách bình luận trên video sở hữu (`Get comments on an owned video`)
<a id="doc-1760232109619202"></a>
<!-- doc_id: 1760232109619202 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/business/comment/list/`

**Mục đích**: Truy cập tất cả các bình luận hoặc các bình luận được chỉ định cụ thể (kèm thông tin liên quan) — bao gồm cả bình luận công khai và bình luận bị ẩn — đã được tạo trên một video tự nhiên thuộc tài khoản TikTok sở hữu.

> [!NOTE]
> - Bạn có thể xác định xem `comment_id` trả về là bình luận cấp cao hay câu trả lời bằng cách kiểm tra trường `parent_comment_id`. Trường này chỉ xuất hiện đối với các câu trả lời bình luận.
> - Các bình luận bị ẩn trả về có thể bao gồm: bình luận bị chủ sở hữu video ẩn, hoặc bình luận bị ẩn do hệ thống kiểm duyệt, cài đặt quyền riêng tư của người dùng hoặc các bộ lọc an toàn của nền tảng.
> - Bạn có thể đăng ký sự kiện Webhook [comment.update](../10-organic-api/accounts-api.md#doc-1810515104773122) để nhận thông báo tự động trong vòng 5 phút khi có bình luận mới, bình luận bị xóa hoặc thay đổi trạng thái ẩn/hiển thị. Chi tiết xem tại [Đăng ký sự kiện cập nhật bình luận](../08-use-cases/use-case-webhook.md#doc-1810521730276354).

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Có | Access token được ủy quyền bởi người sáng tạo TikTok. Dùng [/tt_user/oauth2/token/](10-authentication.md#doc-1833997638479041). |

### Tham số (GET: query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `business_id` | string | Có | Mã định danh duy nhất theo ứng dụng của tài khoản TikTok (`open_id`). |
| `video_id` | string | Có | ID duy nhất của video TikTok sở hữu cần lấy bình luận. Có thể lấy qua [/business/video/list/](01-accounts-p1.md#doc-1762228421622786) (`item_id`). |
| `comment_ids` | string[] | Không | Danh sách ID các bình luận hoặc câu trả lời bình luận muốn lọc kết quả. Truyền dưới dạng mảng chuỗi JSON trong query string. Tối đa 30 ID. |
| `include_replies` | boolean | Không | Có bao gồm tối đa 3 câu trả lời cho mỗi bình luận cấp cao nhất hay không. Mặc định: `false`. Để lấy toàn bộ câu trả lời của bình luận, dùng [/business/comment/reply/list/](01-accounts-p1.md#doc-1762228430145538). |
| `status` | string | Không | Trạng thái hiển thị của bình luận cần lọc:<br>• `PUBLIC`: Các bình luận hiển thị công khai cho mọi người dùng.<br>• `ALL`: Bao gồm cả bình luận bị ẩn và bình luận công khai.<br>**Mặc định**: `ALL`. |
| `sort_field` | string | Không | Trường dùng để sắp xếp bình luận:<br>• `likes`: Sắp xếp theo số lượt thích.<br>• `replies`: Sắp xếp theo số lượng câu trả lời.<br>• `create_time`: Sắp xếp theo thời gian tạo.<br>*(Lưu ý: Nếu số lượng bình luận vượt quá 500, 500 bình luận đầu tiên sắp xếp theo tiêu chí này, các bình luận còn lại sắp xếp theo lượt thích và có thể xuất hiện trùng lặp).* |
| `sort_order` | string | Không | Thứ tự sắp xếp:<br>• `asc`: Tăng dần.<br>• `desc`: Giảm dần.<br>• `smart`: Sắp xếp thông minh bằng thuật toán gợi ý của TikTok.<br>**Mặc định**: `smart`. |
| `cursor` | integer | Không | Con trỏ phân trang cho lần gọi tiếp theo nếu `has_more` là `true`. Mặc định: `0`. |
| `max_count` | integer | Không | Số lượng bình luận tối đa trả về mỗi trang (từ `1` đến `30`). Mặc định: `20`. |

### Header phản hồi

- `Date`: Thời gian nhận phản hồi (GMT).
- `X-Tt-Logid`: Mã log định danh duy nhất của yêu cầu API.

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Xem chi tiết tại [Phụ lục mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). Giá trị `0` là thành công. |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Mã log định danh duy nhất của yêu cầu API. |
| `data` | object | Dữ liệu trả về. |
| ↳ `comments` | object[] | Danh sách bình luận hoặc câu trả lời trên video trong trang hiện tại. |
| ↳↳ `comment_id` | string | ID duy nhất của bình luận hoặc câu trả lời bình luận. |
| ↳↳ `video_id` | string | ID video chứa bình luận. |
| ↳↳ `user_id` | string | *(Sắp ngừng hỗ trợ)*. Mã định danh người dùng trong phạm vi ứng dụng. Khuyến nghị chuyển sang dùng `unique_identifier`. |
| ↳↳ `unique_identifier` | string | Mã định danh người bình luận duy nhất trên toàn cầu, giữ nguyên nhất quán giữa các API khác nhau. |
| ↳↳ `create_time` | string | Thời điểm tạo bình luận theo Unix/Epoch timestamp. |
| ↳↳ `text` | string | Nội dung văn bản của bình luận. |
| ↳↳ `likes` | integer | Số lượt thích bình luận nhận được. |
| ↳↳ `replies` | integer | Số lượng câu trả lời của bình luận này. |
| ↳↳ `owner` | boolean | Cho biết bình luận có phải do chính chủ sở hữu video viết hay không. |
| ↳↳ `liked` | boolean | Cho biết chủ sở hữu video đã thích bình luận này hay chưa. |
| ↳↳ `pinned` | boolean | Cho biết chủ sở hữu video đã ghim bình luận này hay chưa. |
| ↳↳ `status` | string | Trạng thái hiển thị (`PUBLIC`: công khai, `HIDDEN`: bị ẩn). |
| ↳↳ `username` | string | Tên người dùng TikTok của người đã bình luận. |
| ↳↳ `display_name` | string | Tên hiển thị của người đã bình luận. |
| ↳↳ `profile_image` | string | URL tạm thời ảnh đại diện của người bình luận (kèm thời hạn `x-expires`). |
| ↳↳ `parent_comment_id` | string | ID của bình luận cha (chỉ trả về cho câu trả lời bình luận). |
| ↳↳ `image_url` | string | URL hình ảnh đính kèm trong bình luận (nếu có, liên kết này không hết hạn). |
| ↳↳ `reply_list` | object[] | *(Chỉ trả về khi `include_replies` = `true`)*. Danh sách tối đa 3 câu trả lời đầu tiên cho bình luận. Bao gồm các trường con: `comment_id`, `video_id`, `parent_comment_id`, `user_id`, `unique_identifier`, `create_time`, `text`, `likes`, `owner`, `liked`, `status`, `username`, `display_name`, `profile_image`. |
| ↳ `cursor` | integer | Con trỏ cho trang kế tiếp. |
| ↳ `has_more` | boolean | Cho biết còn dữ liệu ở các trang tiếp theo hay không. |

### Ví dụ

#### cURL
```bash
curl -X GET "https://business-api.tiktok.com/open_api/v1.3/business/comment/list/?business_id=6789012345678901234&video_id=7123456789123456789&include_replies=true&max_count=20" \
  -H "Access-Token: ACCESS_TOKEN"
```

#### Python
```python
import requests

ACCESS_TOKEN = "your_access_token"
BUSINESS_ID = "6789012345678901234"
VIDEO_ID = "7123456789123456789"

url = "https://business-api.tiktok.com/open_api/v1.3/business/comment/list/"
headers = {"Access-Token": ACCESS_TOKEN}
params = {
    "business_id": BUSINESS_ID,
    "video_id": VIDEO_ID,
    "include_replies": "true",
    "max_count": 20
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

#### Phản hồi mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20241023150000020666777888999000",
  "data": {
    "cursor": 20,
    "has_more": true,
    "comments": [
      {
        "comment_id": "7198765432198765432",
        "create_time": "1729000000",
        "display_name": "Nguyen Van A",
        "liked": true,
        "likes": 12,
        "owner": false,
        "pinned": false,
        "profile_image": "https://p16-sign-va.tiktokcdn.com/tos-maliva-avt-0068/abc.jpeg?x-expires=1730000000",
        "replies": 2,
        "status": "PUBLIC",
        "text": "Sản phẩm này tuyệt vời quá!",
        "unique_identifier": "+ABc1D2/E0fGhijklMNOrD34vDW/zDiZUNRH5Jyahue6OcA7b8ZpwnqXV9u1Uh+k",
        "username": "nguyenvana",
        "video_id": "7123456789123456789"
      }
    ]
  }
}
```

---

## Lấy danh sách trả lời của một bình luận (`Get all replies to a comment`)
<a id="doc-1762228430145538"></a>
<!-- doc_id: 1762228430145538 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/business/comment/reply/list/`

**Mục đích**: Lấy toàn bộ các câu trả lời trực tiếp cho một bình luận cụ thể (kèm thông tin chi tiết liên quan) trên video tự nhiên thuộc tài khoản TikTok sở hữu.

> [!NOTE]
> - Endpoint này hiện tại chưa hỗ trợ lấy câu trả lời của một bình luận đang ở trạng thái bị ẩn (`HIDDEN`).
> - Sự kiện Webhook [comment.update](../10-organic-api/accounts-api.md#doc-1810515104773122) sẽ thông báo trong vòng 5 phút khi có câu trả lời mới, bị xóa hoặc bị thay đổi trạng thái ẩn/hiện. Xem [Đăng ký sự kiện cập nhật bình luận](../08-use-cases/use-case-webhook.md#doc-1810521730276354).

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Có | Access token được ủy quyền bởi người sáng tạo TikTok. Dùng [/tt_user/oauth2/token/](10-authentication.md#doc-1833997638479041). |

### Tham số (GET: query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `business_id` | string | Có | Mã định danh duy nhất theo ứng dụng của tài khoản TikTok (`open_id`). |
| `video_id` | string | Có | ID duy nhất của video sở hữu (`item_id` từ [/business/video/list/](01-accounts-p1.md#doc-1762228421622786)). |
| `comment_id` | string | Có | ID của bình luận cha cần lấy danh sách câu trả lời (`comment_id` từ [/business/comment/list/](01-accounts-p1.md#doc-1760232109619202)). |
| `status` | string | Không | Trạng thái hiển thị của câu trả lời bình luận:<br>• `PUBLIC`: Chỉ lấy các câu trả lời công khai.<br>• `ALL`: Lấy cả câu trả lời công khai và bị ẩn.<br>**Mặc định**: `ALL`. |
| `sort_field` | string | Không | Trường sắp xếp (`likes`: theo lượt thích, `replies`: theo số câu trả lời con, `create_time`: theo thời gian tạo). Mặc định sắp xếp ngẫu nhiên. |
| `sort_order` | string | Không | Thứ tự sắp xếp (`asc`: tăng dần, `desc`: giảm dần). Mặc định sắp xếp theo ngữ nghĩa thuật toán. |
| `cursor` | integer | Không | Con trỏ phân trang cho lần gọi tiếp theo nếu `has_more` là `true`. Mặc định: `0`. |
| `max_count` | integer | Không | Số lượng câu trả lời tối đa trả về mỗi trang (từ `0` đến `30`). Mặc định: `20`. |

### Header phản hồi

- `Date`: Thời gian GMT nhận được phản hồi.
- `X-Tt-Logid`: Mã log định danh duy nhất của yêu cầu API.

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Xem chi tiết tại [Phụ lục mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). Giá trị `0` là thành công. |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Mã log định danh duy nhất của yêu cầu API. |
| `data` | object | Dữ liệu trả về. |
| ↳ `comments` | object[] | Danh sách các câu trả lời cho bình luận chỉ định trên video. |
| ↳↳ `comment_id` | string | ID duy nhất của câu trả lời. |
| ↳↳ `parent_comment_id` | string | ID của bình luận cha mà câu trả lời này hướng tới. |
| ↳↳ `video_id` | string | ID của video chứa bình luận. |
| ↳↳ `user_id` | string | *(Sắp ngừng hỗ trợ)*. Mã định danh người dùng trong phạm vi ứng dụng. Khuyến nghị dùng `unique_identifier`. |
| ↳↳ `unique_identifier` | string | Mã định danh toàn cầu duy nhất cho người dùng bình luận. |
| ↳↳ `create_time` | string | Thời điểm tạo câu trả lời (Unix timestamp). |
| ↳↳ `text` | string | Nội dung văn bản của câu trả lời. |
| ↳↳ `likes` | integer | Số lượt thích câu trả lời nhận được. |
| ↳↳ `replies` | integer | Số lượt phản hồi tiếp theo cho câu trả lời này. |
| ↳↳ `owner` | boolean | Cho biết câu trả lời có phải do chủ sở hữu video viết hay không. |
| ↳↳ `liked` | boolean | Cho biết chủ sở hữu video đã thích câu trả lời này chưa. |
| ↳↳ `pinned` | boolean | Cho biết chủ sở hữu video đã ghim câu trả lời này chưa. |
| ↳↳ `status` | string | Trạng thái hiển thị (`PUBLIC` hoặc `HIDDEN`). |
| ↳↳ `username` | string | Tên người dùng TikTok của người trả lời. |
| ↳↳ `display_name` | string | Tên hiển thị của người trả lời. |
| ↳↳ `profile_image` | string | URL tạm thời của ảnh đại diện người trả lời. |
| ↳↳ `image_url` | string | URL hình ảnh đính kèm trong câu trả lời (nếu có, không hết hạn). |
| ↳ `cursor` | integer | Con trỏ cho trang kế tiếp. |
| ↳ `has_more` | boolean | Cho biết còn dữ liệu ở các trang tiếp theo hay không. |

### Ví dụ

#### cURL
```bash
curl -X GET "https://business-api.tiktok.com/open_api/v1.3/business/comment/reply/list/?business_id=6789012345678901234&video_id=7123456789123456789&comment_id=7198765432198765432" \
  -H "Access-Token: ACCESS_TOKEN"
```

#### Python
```python
import requests

ACCESS_TOKEN = "your_access_token"
BUSINESS_ID = "6789012345678901234"
VIDEO_ID = "7123456789123456789"
COMMENT_ID = "7198765432198765432"

url = "https://business-api.tiktok.com/open_api/v1.3/business/comment/reply/list/"
headers = {"Access-Token": ACCESS_TOKEN}
params = {
    "business_id": BUSINESS_ID,
    "video_id": VIDEO_ID,
    "comment_id": COMMENT_ID
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

#### Phản hồi mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20241023150000020777888999000111",
  "data": {
    "cursor": 1,
    "has_more": false,
    "comments": [
      {
        "comment_id": "7198765432198765499",
        "create_time": "1729000500",
        "display_name": "TikTok Shop Vietnam",
        "liked": false,
        "likes": 5,
        "owner": true,
        "parent_comment_id": "7198765432198765432",
        "pinned": false,
        "profile_image": "https://p16-sign-va.tiktokcdn.com/tos-maliva-avt-0068/shop.jpeg",
        "status": "PUBLIC",
        "text": "Cảm ơn bạn đã ủng hộ shop nhé!",
        "unique_identifier": "+ABc1D2/ShopUniqueId12345",
        "username": "tiktokshop_vn",
        "video_id": "7123456789123456789"
      }
    ]
  }
}
```
---

## Tạo bình luận mới trên video sở hữu (`Create a new comment on an owned video`)
<a id="doc-1762228442072066"></a>
<!-- doc_id: 1762228442072066 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/business/comment/create/`

**Mục đích**: Đăng một bình luận mới (bằng văn bản hoặc hình ảnh) lên một video tự nhiên được đăng bởi tài khoản TikTok sở hữu.

> [!NOTE]
> - Để tránh việc bình luận bị hệ thống gắn cờ là spam và tự động ẩn, hãy tránh đăng số lượng lớn bình luận có nội dung tương tự nhau trong thời gian ngắn. Nếu bình luận bị đánh dấu spam, bạn sẽ không nhận được sự kiện Webhook [comment.update](../10-organic-api/accounts-api.md#doc-1810515104773122) với hành động `set_to_public`.
> - Sự kiện Webhook [comment.update](../10-organic-api/accounts-api.md#doc-1810515104773122) cho phép bạn nhận thông báo trong vòng 5 phút khi bình luận được tạo trên video công khai. Xem [Đăng ký sự kiện cập nhật bình luận](../08-use-cases/use-case-webhook.md#doc-1810521730276354).

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Có | Access token được ủy quyền bởi người sáng tạo TikTok. Dùng [/tt_user/oauth2/token/](10-authentication.md#doc-1833997638479041). |
| `Content-Type` | string | Có | Định dạng nội dung yêu cầu. Giá trị cho phép: `application/json`. |

### Tham số (POST: JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `business_id` | string | Có | Mã định danh duy nhất theo ứng dụng của tài khoản TikTok (`open_id`). |
| `video_id` | string | Có | ID duy nhất của video TikTok sở hữu cần bình luận (`item_id` từ [/business/video/list/](01-accounts-p1.md#doc-1762228421622786)). |
| `text` | string | Điều kiện | Nội dung văn bản của bình luận. Bắt buộc phải chỉ định một trong hai: `text` hoặc `image_uri`. Giới hạn độ dài: tối đa 1.200 ký tự (mã hóa UTF-8). |
| `image_uri` | string | Điều kiện | Mã định danh URI của ảnh đính kèm trong bình luận. Bắt buộc phải chỉ định `text` hoặc `image_uri`. Để lấy mã URI này, gọi endpoint [/business/comment/image/upload/](01-accounts-p1.md#doc-1856212334897154) trước. |
| `image_width` | integer | Điều kiện | Chiều rộng của ảnh (bắt buộc khi truyền `image_uri`). Lấy từ phản hồi của [/business/comment/image/upload/](01-accounts-p1.md#doc-1856212334897154). |
| `image_height` | integer | Điều kiện | Chiều cao của ảnh (bắt buộc khi truyền `image_uri`). Lấy từ phản hồi của [/business/comment/image/upload/](01-accounts-p1.md#doc-1856212334897154). |

### Header phản hồi

- `Date`: Thời gian GMT nhận được phản hồi.
- `X-Tt-Logid`: Mã log định danh duy nhất của yêu cầu API.

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Xem chi tiết tại [Phụ lục mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). Giá trị `0` là thành công. |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Mã log định danh duy nhất của yêu cầu API. |
| `data` | object | Dữ liệu trả về. |
| ↳ `comment_id` | string | ID duy nhất của bình luận vừa được tạo. |
| ↳ `video_id` | string | ID của video được đăng bình luận. |
| ↳ `user_id` | string | *(Sắp ngừng hỗ trợ)*. Mã định danh người dùng trong phạm vi ứng dụng. |
| ↳ `unique_identifier` | string | Mã định danh người dùng duy nhất toàn cầu. |
| ↳ `create_time` | string | Thời điểm tạo bình luận (Unix timestamp). |
| ↳ `text` | string | Nội dung văn bản của bình luận (trả về nếu bình luận bằng văn bản). |
| ↳ `image_url` | string | URL hình ảnh đính kèm trong bình luận (trả về nếu bình luận bằng hình ảnh). |

### Ví dụ

#### cURL: Bình luận bằng văn bản
```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/business/comment/create/" \
  -H "Access-Token: ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "business_id": "6789012345678901234",
    "video_id": "7123456789123456789",
    "text": "Cảm ơn các bạn đã theo dõi video!"
  }'
```

#### Phản hồi mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20241023150000020888999000111222",
  "data": {
    "comment_id": "7198765432198765500",
    "create_time": "1729000600",
    "text": "Cảm ơn các bạn đã theo dõi video!",
    "unique_identifier": "+ABc1D2/OwnerId12345",
    "user_id": "ce9b7be629b0447af777a0ad945783f61b7f790982b49fbda04a23b4722eaffe",
    "video_id": "7123456789123456789"
  }
}
```

---

## Tải ảnh bình luận lên hệ thống (`Upload a comment image`)
<a id="doc-1856212334897154"></a>
<!-- doc_id: 1856212334897154 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/business/comment/image/upload/`

**Mục đích**: Tải tệp hình ảnh lên hệ thống để nhận về mã `image_uri` cùng kích thước ảnh (`width`, `height`), sử dụng cho việc đăng bình luận hoặc trả lời bình luận bằng hình ảnh qua [/business/comment/create/](01-accounts-p1.md#doc-1762228442072066) hoặc [/business/comment/reply/create/](01-accounts-p1.md#doc-1762228448779266).

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Có | Access token được ủy quyền bởi người sáng tạo TikTok. |
| `Content-Type` | string | Có | Định dạng nội dung yêu cầu. Giá trị cho phép: `multipart/form-data`. |

### Tham số (POST: multipart/form-data)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `image_file` | file | Có | Tệp hình ảnh tải lên để sử dụng trong bình luận.<br><br>**Yêu cầu kỹ thuật**:<br>• Dung lượng tối đa: 5 MB.<br>• Độ phân giải tối đa: 1080 x 1920 pixels hoặc 1920 x 1080 pixels.<br>• Độ phân giải tối thiểu: 360 x 360 pixels.<br>• Định dạng hỗ trợ: JPG, JPEG, WebP, hoặc PNG. |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Xem chi tiết tại [Phụ lục mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). Giá trị `0` là thành công. |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Mã log định danh duy nhất của yêu cầu API. |
| `data` | object | Dữ liệu trả về. |
| ↳ `image_uri` | string | Mã định danh URI của hình ảnh đã tải lên thành công. Dùng giá trị này để truyền vào `image_uri` khi tạo bình luận. |
| ↳ `width` | integer | Chiều rộng thực tế của hình ảnh tính bằng pixels (ví dụ: `720`). |
| ↳ `height` | integer | Chiều cao thực tế của hình ảnh tính bằng pixels (ví dụ: `900`). |

### Ví dụ

#### cURL
```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/business/comment/image/upload/" \
  -H "Access-Token: ACCESS_TOKEN" \
  -F "business_id=6789012345678901234" \
  -F "image_file=@/path/to/comment_image.png"
```

#### Phản hồi mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20241023150000020999000111222333",
  "data": {
    "height": 900,
    "image_uri": "54ccb875ae0c4368b94037d03a95b633",
    "width": 720
  }
}
```

---

## Trả lời một bình luận hiện có trên video sở hữu (`Reply to an existing comment on an owned video`)
<a id="doc-1762228448779266"></a>
<!-- doc_id: 1762228448779266 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/business/comment/reply/create/`

**Mục đích**: Gửi một câu trả lời (bằng văn bản hoặc hình ảnh) cho một bình luận đã có trên video tự nhiên thuộc tài khoản TikTok sở hữu.

> [!NOTE]
> - Tránh gửi số lượng lớn câu trả lời có nội dung trùng lặp trong thời gian ngắn để không bị hệ thống kiểm duyệt đánh dấu spam.
> - Sự kiện Webhook [comment.update](../10-organic-api/accounts-api.md#doc-1810515104773122) sẽ thông báo trong vòng 5 phút khi câu trả lời được tạo trên video công khai.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Có | Access token được ủy quyền bởi người sáng tạo TikTok. Dùng [/tt_user/oauth2/token/](10-authentication.md#doc-1833997638479041). |
| `Content-Type` | string | Có | Định dạng nội dung yêu cầu. Giá trị cho phép: `application/json`. |

### Tham số (POST: JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `business_id` | string | Có | Mã định danh duy nhất theo ứng dụng của tài khoản TikTok (`open_id`). |
| `video_id` | string | Có | ID duy nhất của video sở hữu (`item_id` từ [/business/video/list/](01-accounts-p1.md#doc-1762228421622786)). |
| `comment_id` | string | Có | ID của bình luận hiện có mà bạn muốn trả lời (`comment_id` từ [/business/comment/list/](01-accounts-p1.md#doc-1760232109619202)). |
| `text` | string | Điều kiện | Nội dung văn bản của câu trả lời. Bắt buộc phải chỉ định một trong hai: `text` hoặc `image_uri`. Độ dài tối đa: 1.200 ký tự (mã hóa UTF-8). |
| `image_uri` | string | Điều kiện | Mã định danh URI của ảnh câu trả lời (lấy từ [/business/comment/image/upload/](01-accounts-p1.md#doc-1856212334897154)). |
| `image_width` | integer | Điều kiện | Chiều rộng của ảnh (bắt buộc khi có `image_uri`). |
| `image_height` | integer | Điều kiện | Chiều cao của ảnh (bắt buộc khi có `image_uri`). |
| `reply_image_url` | string | Không | Đường dẫn URL hình ảnh được sử dụng để trả lời (nếu có, URL phải thuộc tên miền đã được xác minh quyền sở hữu). |

### Header phản hồi

- `Date`: Thời gian GMT nhận phản hồi.
- `X-Tt-Logid`: Mã log định danh duy nhất của yêu cầu API.

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Xem chi tiết tại [Phụ lục mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). Giá trị `0` là thành công. |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Mã log định danh duy nhất của yêu cầu API. |
| `data` | object | Dữ liệu trả về. |
| ↳ `comment_id` | string | ID duy nhất của câu trả lời vừa được tạo. |
| ↳ `parent_comment_id` | string | ID của bình luận cha mà câu trả lời này hướng tới. |
| ↳ `video_id` | string | ID của video sở hữu chứa bình luận. |
| ↳ `user_id` | string | *(Sắp ngừng hỗ trợ)*. Mã định danh người dùng trong phạm vi ứng dụng. |
| ↳ `unique_identifier` | string | Mã định danh người dùng duy nhất toàn cầu. |
| ↳ `create_time` | string | Thời điểm tạo câu trả lời theo Unix timestamp. |
| ↳ `text` | string | Nội dung văn bản câu trả lời (trả về nếu người dùng trả lời bằng văn bản). |
| ↳ `image_url` | string | URL hình ảnh trong câu trả lời (trả về nếu người dùng trả lời bằng hình ảnh). |

### Ví dụ

#### cURL
```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/business/comment/reply/create/" \
  -H "Access-Token: ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "business_id": "6789012345678901234",
    "video_id": "7123456789123456789",
    "comment_id": "7198765432198765432",
    "text": "Dạ shop đã gửi tin nhắn riêng cho bạn rồi ạ!"
  }'
```

#### Phản hồi mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20241023150000021000111222333444",
  "data": {
    "comment_id": "7198765432198765501",
    "create_time": "1729000700",
    "parent_comment_id": "7198765432198765432",
    "text": "Dạ shop đã gửi tin nhắn riêng cho bạn rồi ạ!",
    "unique_identifier": "+ABc1D2/OwnerUniqueId",
    "user_id": "ce9b7be629b0447af777a0ad945783f61b7f790982b49fbda04a23b4722eaffe",
    "video_id": "7123456789123456789"
  }
}
```

---

## Thích hoặc bỏ thích bình luận trên video sở hữu (`Like/unlike an existing comment on an owned video`)
<a id="doc-1762228456608770"></a>
<!-- doc_id: 1762228456608770 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/business/comment/like/`

**Mục đích**: Thực hiện hành động thích (`LIKE`) hoặc bỏ thích (`UNLIKE`) đối với một bình luận hoặc câu trả lời bình luận trên video tự nhiên thuộc tài khoản TikTok sở hữu.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Có | Access token được ủy quyền bởi người sáng tạo TikTok. Dùng [/tt_user/oauth2/token/](10-authentication.md#doc-1833997638479041). |
| `Content-Type` | string | Có | Định dạng nội dung yêu cầu. Giá trị cho phép: `application/json`. |

### Tham số (POST: JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `business_id` | string | Có | Mã định danh duy nhất theo ứng dụng của tài khoản TikTok (`open_id`). |
| `comment_id` | string | Có | ID duy nhất của bình luận hoặc câu trả lời bình luận cần thích/bỏ thích (`comment_id` từ [/business/comment/list/](01-accounts-p1.md#doc-1760232109619202)). |
| `action` | string | Có | Hành động cần thực hiện đối với bình luận.<br><br>**Enum**:<br>• `LIKE`: Thích bình luận.<br>• `UNLIKE`: Bỏ thích bình luận. |

### Header phản hồi

- `Date`: Thời gian GMT nhận phản hồi.
- `X-Tt-Logid`: Mã log định danh duy nhất của yêu cầu API.

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Xem chi tiết tại [Phụ lục mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). Giá trị `0` là thành công. |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Mã log định danh duy nhất của yêu cầu API. |
| `data` | object | Dữ liệu trả về. Đối tượng rỗng (`{}`) khi thao tác thành công. |

### Ví dụ

#### cURL
```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/business/comment/like/" \
  -H "Access-Token: ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "business_id": "6789012345678901234",
    "comment_id": "7198765432198765432",
    "action": "LIKE"
  }'
```

#### Phản hồi mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20241023150000021111222333444555",
  "data": {}
}
```

---

## Ẩn hoặc bỏ ẩn bình luận trên video sở hữu (`Hide/unhide an existing comment on an owned video`)
<a id="doc-1762228474532865"></a>
<!-- doc_id: 1762228474532865 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/business/comment/hide/`

**Mục đích**: Ẩn (`HIDE`) hoặc bỏ ẩn (`UNHIDE`) một bình luận hoặc câu trả lời bình luận trên video tự nhiên thuộc tài khoản TikTok sở hữu.

> [!NOTE]
> - Việc bỏ ẩn bình luận (`UNHIDE`) có thể không có hiệu lực nếu bình luận đó bị ẩn do hệ thống kiểm duyệt, cài đặt quyền riêng tư của tác giả hoặc bộ lọc an toàn của TikTok. Trong trường hợp đó, bình luận vẫn sẽ ở trạng thái ẩn. Bạn có thể kiểm tra trạng thái thực tế qua trường `status` của endpoint [/business/comment/list/](01-accounts-p1.md#doc-1760232109619202).
> - Sự kiện Webhook [comment.update](../10-organic-api/accounts-api.md#doc-1810515104773122) sẽ thông báo trong vòng 5 phút khi bình luận bị ẩn hoặc được hiển thị lại.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Có | Access token được ủy quyền bởi người sáng tạo TikTok. Dùng [/tt_user/oauth2/token/](10-authentication.md#doc-1833997638479041). |
| `Content-Type` | string | Có | Định dạng nội dung yêu cầu. Giá trị cho phép: `application/json`. |

### Tham số (POST: JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `business_id` | string | Có | Mã định danh duy nhất theo ứng dụng của tài khoản TikTok (`open_id`). |
| `video_id` | string | Có | ID duy nhất của video sở hữu chứa bình luận (`item_id` từ [/business/video/list/](01-accounts-p1.md#doc-1762228421622786)). |
| `comment_id` | string | Có | ID duy nhất của bình luận hoặc câu trả lời bình luận cần ẩn/bỏ ẩn. |
| `action` | string | Có | Thao tác cần thực hiện:<br><br>**Enum**:<br>• `HIDE`: Ẩn bình luận khỏi chế độ xem công khai.<br>• `UNHIDE`: Bỏ ẩn bình luận để người dùng khác có thể xem lại. |

### Header phản hồi

- `Date`: Thời gian GMT nhận phản hồi.
- `X-Tt-Logid`: Mã log định danh duy nhất của yêu cầu API.

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Xem chi tiết tại [Phụ lục mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). Giá trị `0` là thành công. |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Mã log định danh duy nhất của yêu cầu API. |
| `data` | object | Dữ liệu trả về. Đối tượng rỗng (`{}`) khi thực hiện thành công. |

### Ví dụ

#### cURL
```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/business/comment/hide/" \
  -H "Access-Token: ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "business_id": "6789012345678901234",
    "video_id": "7123456789123456789",
    "comment_id": "7198765432198765432",
    "action": "HIDE"
  }'
```

#### Phản hồi mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20241023150000021222333444555666",
  "data": {}
}
```

---

## Xóa bình luận trên video sở hữu (`Delete an existing comment on an owned video`)
<a id="doc-1762228483080193"></a>
<!-- doc_id: 1762228483080193 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/business/comment/delete/`

**Mục đích**: Xóa vĩnh viễn một **bình luận thuộc sở hữu của chính bạn** (bình luận do chính tài khoản tạo ra) trên video tự nhiên của tài khoản TikTok sở hữu.

> [!NOTE]
> - Bình luận do người dùng khác tạo ra không thể bị xóa bởi endpoint này; bạn chỉ có thể ẩn chúng bằng [/business/comment/hide/](01-accounts-p1.md#doc-1762228474532865).
> - Sự kiện Webhook [comment.update](../10-organic-api/accounts-api.md#doc-1810515104773122) sẽ thông báo trong vòng 5 phút khi bình luận bị xóa.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Có | Access token được ủy quyền bởi người sáng tạo TikTok. Dùng [/tt_user/oauth2/token/](10-authentication.md#doc-1833997638479041). |
| `Content-Type` | string | Có | Định dạng nội dung yêu cầu. Giá trị cho phép: `application/json`. |

### Tham số (POST: JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `business_id` | string | Có | Mã định danh duy nhất theo ứng dụng của tài khoản TikTok (`open_id`). |
| `comment_id` | string | Có | ID duy nhất của bình luận sở hữu cần xóa (`comment_id` từ [/business/comment/list/](01-accounts-p1.md#doc-1760232109619202)). |

### Header phản hồi

- `Date`: Thời gian GMT nhận phản hồi.
- `X-Tt-Logid`: Mã log định danh duy nhất của yêu cầu API.

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Xem chi tiết tại [Phụ lục mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). Giá trị `0` là thành công. |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Mã log định danh duy nhất của yêu cầu API. |
| `data` | object | Dữ liệu trả về. Đối tượng rỗng (`{}`) khi xóa thành công. |

### Ví dụ

#### cURL
```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/business/comment/delete/" \
  -H "Access-Token: ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "business_id": "6789012345678901234",
    "comment_id": "7198765432198765500"
  }'
```

#### Phản hồi mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20241023150000021333444555666777",
  "data": {}
}
```
---

## Tổng quan xuất bản bài đăng (`Posts`)
<a id="doc-1769113361610753"></a>
<!-- doc_id: 1769113361610753 -->

Nhóm API Xuất bản bài đăng (Posts) cho phép các thương hiệu và nhà sáng tạo tự động hóa quy trình đăng tải nội dung đa phương tiện lên tài khoản TikTok:
- [Đăng bài viết video công khai lên tài khoản sở hữu](01-accounts-p1.md#doc-1762228496095234): Đăng video hoặc lưu vào bản nháp với đầy đủ tùy chọn thương hiệu, cài đặt bình luận, Duet, Stitch, vị trí và âm thanh.
- [Đăng bài viết ảnh lên tài khoản sở hữu](01-accounts-p1.md#doc-1803630424390658): Đăng chuỗi ảnh (photo carousel / photo post) lên tài khoản kèm nhạc thương mại.
- [Lấy trạng thái xuất bản bài đăng TikTok](01-accounts-p1.md#doc-1816387106635778): Theo dõi tiến trình tải lên, mã hóa và đăng bài thông qua mã `publish_id`.
- [Gợi ý hashtag cho tài khoản TikTok](01-accounts-p2.md#doc-1762228503821314): Gợi ý các hashtag liên quan dựa trên từ khóa.
- [Lấy danh sách thẻ vị trí cho tài khoản TikTok](01-accounts-p2.md#doc-1870580030749698): Tìm kiếm địa điểm để gắn thẻ vào bài đăng.

---

## Đăng bài viết video công khai lên tài khoản sở hữu (`Publish a public video post to an owned account`)
<a id="doc-1762228496095234"></a>
<!-- doc_id: 1762228496095234 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/business/video/publish/`

**Mục đích**: Xuất bản một bài đăng video công khai hoặc lưu vào bản nháp của tài khoản TikTok sở hữu từ một đường dẫn URL video công khai.

> [!NOTE]
> - Đây là thao tác bất đồng bộ (asynchronous). Sau khi gọi endpoint thành công, API sẽ trả về một mã `publish_id`. Bạn cần dùng mã này để truy vấn trạng thái xử lý video thông qua [/business/publish/status/](01-accounts-p1.md#doc-1816387106635778).
> - Để đảm bảo tuân thủ chính sách, bạn bắt buộc phải khai báo tính chất thương mại của bài đăng qua hai trường `is_brand_organic` và `is_branded_content`.
> - **Yêu cầu kỹ thuật tệp video**: Định dạng hỗ trợ MP4, MOV, WebM; thời lượng tối thiểu 3 giây và không vượt quá `max_video_post_duration_sec` (tra cứu qua [/business/video/settings/](01-accounts-p1.md#doc-1816387951979521)); độ phân giải tối thiểu 360p.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Có | Access token được ủy quyền bởi người sáng tạo TikTok. Dùng [/tt_user/oauth2/token/](10-authentication.md#doc-1833997638479041). |
| `Content-Type` | string | Có | Định dạng nội dung yêu cầu. Giá trị cho phép: `application/json`. |

### Tham số (POST: JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `business_id` | string | Có | Mã định danh duy nhất theo ứng dụng của tài khoản TikTok (`open_id`). |
| `video_url` | string | Có | Đường dẫn URL công khai có thể tải về trực tiếp của tệp video bạn muốn xuất bản. Đường dẫn phải có thể truy cập được bởi máy chủ TikTok mà không cần xác thực bổ sung. |
| `custom_thumbnail_url` | string | Không | Đường dẫn URL công khai của hình ảnh thu nhỏ tùy chỉnh (custom thumbnail) cho video. |
| `post_info` | object | Có | Thông tin cấu hình chi tiết cho bài đăng video. |
| ↳ `caption` | string | Không | Tiêu đề và nội dung mô tả của video (bao gồm cả hashtag). Độ dài tối đa: 2.200 ký tự. |
| ↳ `is_brand_organic` | boolean | Có | Khai báo bài đăng có quảng bá thương hiệu hoặc doanh nghiệp của chính bạn hay không. |
| ↳ `is_branded_content` | boolean | Có | Khai báo bài đăng có phải là nội dung trả phí hợp tác quảng bá cho bên thứ ba (Branded Content) hay không. |
| ↳ `tto_invite_link` | string | Không | Liên kết mời chiến dịch từ nền tảng TikTok One (nếu có). |
| ↳ `disable_comment` | boolean | Không | Vô hiệu hóa tính năng bình luận trên video này. Mặc định: `false`. |
| ↳ `disable_duet` | boolean | Không | Vô hiệu hóa tính năng Duet trên video này. Mặc định: `false`. |
| ↳ `disable_stitch` | boolean | Không | Vô hiệu hóa tính năng Stitch trên video này. Mặc định: `false`. |
| ↳ `thumbnail_offset` | integer | Không | Khoảng thời gian (tính bằng mili giây) từ đầu video để chọn một khung hình làm ảnh bìa thu nhỏ. |
| ↳ `is_ai_generated` | boolean | Không | Khai báo video được tạo bởi trí tuệ nhân tạo (AI-generated content). Mặc định: `false`. |
| ↳ `upload_to_draft` | boolean | Không | Lưu video vào thư mục bản nháp (Drafts) trong ứng dụng TikTok thay vì xuất bản công khai ngay lập tức. Mặc định: `false`. |
| ↳ `location_id` | string | Không | ID của thẻ vị trí (lấy từ [/business/publish/location/](01-accounts-p2.md#doc-1870580030749698)). |
| ↳ `location_name` | string | Điều kiện | Tên địa điểm tương ứng với `location_id` (bắt buộc khi truyền `location_id`). |
| ↳ `is_ads_only` | boolean | Không | Đăng tải video dưới dạng chỉ phục vụ quảng cáo (Dark post / Ads-only post), không hiển thị trên bảng tin hồ sơ công khai. |
| ↳ `music_sound_info` | object | Không | Thông tin âm thanh thương mại đính kèm video. |
| ↳↳ `music_sound_id` | string | Điều kiện | ID của bài hát thương mại được cấp phép sử dụng. |

### Header phản hồi

- `Date`: Thời gian GMT nhận phản hồi.
- `X-Tt-Logid`: Mã log định danh duy nhất của yêu cầu API.

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Xem chi tiết tại [Phụ lục mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). Giá trị `0` là thành công. |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Mã log định danh duy nhất của yêu cầu API. |
| `data` | object | Dữ liệu trả về. |
| ↳ `publish_id` | string | Mã định danh tiến trình xuất bản bài đăng. Sử dụng mã này để tra cứu trạng thái xuất bản qua [/business/publish/status/](01-accounts-p1.md#doc-1816387106635778). |

### Ví dụ

#### cURL
```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/business/video/publish/" \
  -H "Access-Token: ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "business_id": "6789012345678901234",
    "video_url": "https://example.com/videos/product-intro.mp4",
    "post_info": {
      "caption": "Khám phá bộ sưu tập mới mùa thu này! #autumn #fashion",
      "disable_comment": false,
      "disable_duet": false,
      "disable_stitch": false,
      "is_ai_generated": false,
      "is_brand_organic": true,
      "is_branded_content": false
    }
  }'
```

#### Phản hồi mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20241023150000021444555666777888",
  "data": {
    "publish_id": "v_pub_7123456789012345678"
  }
}
```

---

## Đăng bài viết ảnh lên tài khoản sở hữu (`Publish a photo post to an owned account`)
<a id="doc-1803630424390658"></a>
<!-- doc_id: 1803630424390658 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/business/photo/publish/`

**Mục đích**: Xuất bản một bài đăng định dạng chuỗi ảnh (photo post carousel) hoặc lưu vào bản nháp của tài khoản TikTok sở hữu từ các đường dẫn hình ảnh công khai.

> [!NOTE]
> - **Yêu cầu hình ảnh**: Danh sách `photo_images` phải chứa từ 2 đến 35 hình ảnh công khai. Định dạng hỗ trợ: JPG, JPEG, PNG, WebP. Độ phân giải tối đa: 1080 x 1920 hoặc 1920 x 1080 pixels; dung lượng mỗi ảnh tối đa 10 MB.
> - Sau khi gửi yêu cầu thành công, API trả về `publish_id` để theo dõi tiến độ qua [/business/publish/status/](01-accounts-p1.md#doc-1816387106635778).

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Có | Access token được ủy quyền bởi người sáng tạo TikTok. Dùng [/tt_user/oauth2/token/](10-authentication.md#doc-1833997638479041). |
| `Content-Type` | string | Có | Định dạng nội dung yêu cầu. Giá trị cho phép: `application/json`. |

### Tham số (POST: JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `business_id` | string | Có | Mã định danh duy nhất theo ứng dụng của tài khoản TikTok (`open_id`). |
| `photo_images` | string[] | Có | Mảng chứa danh sách URL công khai của các hình ảnh muốn xuất bản (tối thiểu 2 ảnh, tối đa 35 ảnh). Các ảnh sẽ xuất hiện theo đúng thứ tự mảng. |
| `photo_cover_index` | number | Không | Chỉ số (bắt đầu từ 1) của hình ảnh được chọn làm ảnh bìa cho bài đăng ảnh. Mặc định: `1`. |
| `post_info` | object | Có | Thông tin cấu hình chi tiết cho bài đăng ảnh. |
| ↳ `privacy_level` | string | Có | Mức độ hiển thị của bài đăng ảnh.<br><br>**Enum**:<br>• `PUBLIC_TO_EVERYONE`: Công khai cho mọi người.<br>• `MUTUAL_FOLLOW_FRIENDS`: Bạn bè theo dõi lẫn nhau.<br>• `SELF_ONLY`: Chỉ mình tôi.<br>• `FOLLOWER_OF_CREATOR`: Người theo dõi (dành cho tài khoản riêng tư). |
| ↳ `title` | string | Không | Tiêu đề của bài đăng ảnh. Độ dài tối đa: 90 ký tự. |
| ↳ `caption` | string | Không | Chú thích mô tả của bài đăng ảnh (kèm hashtag). Độ dài tối đa: 2.200 ký tự. |
| ↳ `auto_add_music` | boolean | Không | Tự động thêm bài nhạc nền thịnh hành phù hợp nếu không chỉ định `music_sound_info`. Mặc định: `false`. |
| ↳ `is_brand_organic` | boolean | Có | Khai báo nội dung quảng bá cho thương hiệu/doanh nghiệp của bạn. |
| ↳ `is_branded_content` | boolean | Có | Khai báo nội dung tài trợ quảng bá cho bên thứ ba. |
| ↳ `is_draft` | boolean | Không | Lưu bài viết dưới dạng bản nháp trong ứng dụng TikTok thay vì xuất bản ngay. Mặc định: `false`. |
| ↳ `disable_comment` | boolean | Không | Vô hiệu hóa tính năng bình luận cho bài đăng ảnh này. Mặc định: `false`. |
| ↳ `music_sound_info` | object | Không | Cấu hình nhạc nền đính kèm cho chuỗi ảnh. |
| ↳↳ `music_sound_id` | string | Điều kiện | ID bản nhạc thương mại. |
| ↳ `location_id` | string | Không | ID thẻ vị trí (lấy từ [/business/publish/location/](01-accounts-p2.md#doc-1870580030749698)). |
| ↳ `location_name` | string | Điều kiện | Tên vị trí (bắt buộc khi truyền `location_id`). |

### Header phản hồi

- `Date`: Thời gian GMT nhận phản hồi.
- `X-Tt-Logid`: Mã log định danh duy nhất của yêu cầu API.

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Xem chi tiết tại [Phụ lục mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). Giá trị `0` là thành công. |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Mã log định danh duy nhất của yêu cầu API. |
| `data` | object | Dữ liệu trả về. |
| ↳ `publish_id` | string | Mã định danh tiến trình xuất bản bài đăng ảnh. Dùng mã này để kiểm tra kết quả qua [/business/publish/status/](01-accounts-p1.md#doc-1816387106635778). |

### Ví dụ

#### cURL
```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/business/photo/publish/" \
  -H "Access-Token: ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "business_id": "6789012345678901234",
    "photo_images": [
      "https://example.com/photos/item-front.jpg",
      "https://example.com/photos/item-side.jpg"
    ],
    "photo_cover_index": 1,
    "post_info": {
      "title": "Áo Thun Unisex Mới",
      "caption": "Mẫu áo thun cao cấp mới về hàng hôm nay! #ootd #fashion",
      "privacy_level": "PUBLIC_TO_EVERYONE",
      "is_brand_organic": true,
      "is_branded_content": false,
      "auto_add_music": true
    }
  }'
```

#### Phản hồi mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20241023150000021555666777888999",
  "data": {
    "publish_id": "p_pub_7123456789012345679"
  }
}
```

---

## Lấy trạng thái xuất bản bài đăng TikTok (`Get the publishing status of a TikTok post`)
<a id="doc-1816387106635778"></a>
<!-- doc_id: 1816387106635778 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/business/publish/status/`

**Mục đích**: Tra cứu tiến độ xử lý và kết quả xuất bản của một bài đăng video hoặc ảnh trên tài khoản TikTok dựa trên mã `publish_id` nhận được từ lệnh đăng bài.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Có | Access token được ủy quyền bởi người sáng tạo TikTok. Dùng [/tt_user/oauth2/token/](10-authentication.md#doc-1833997638479041). |

### Tham số (GET: query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `business_id` | string | Có | Mã định danh duy nhất theo ứng dụng của tài khoản TikTok (`open_id`). |
| `publish_id` | string | Có | Mã định danh tiến trình xuất bản bài đăng nhận được từ [/business/video/publish/](01-accounts-p1.md#doc-1762228496095234) hoặc [/business/photo/publish/](01-accounts-p1.md#doc-1803630424390658). |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Xem chi tiết tại [Phụ lục mã phản hồi](../15-appendix/phu-luc-p1.md#doc-1737172488964097). Giá trị `0` là thành công. |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Mã log định danh duy nhất của yêu cầu API. |
| `data` | object | Dữ liệu trả về. |
| ↳ `status` | string | Trạng thái hiện tại của quá trình xuất bản bài đăng.<br><br>**Enum**:<br>• `PROCESSING`: Đang trong quá trình tải xuống, mã hóa và xử lý nội dung.<br>• `SUCCESS`: Bài đăng đã được xuất bản công khai thành công.<br>• `FAILED`: Xuất bản bài đăng thất bại. |
| ↳ `post_ids` | string[] | Danh sách ID của các bài đăng đã xuất bản thành công trên TikTok (chỉ trả về khi `status` là `SUCCESS`). |
| ↳ `reason` | string | Lý do chi tiết khiến việc xuất bản thất bại (chỉ trả về khi `status` là `FAILED`). |

### Ví dụ

#### cURL
```bash
curl -X GET "https://business-api.tiktok.com/open_api/v1.3/business/publish/status/?business_id=6789012345678901234&publish_id=v_pub_7123456789012345678" \
  -H "Access-Token: ACCESS_TOKEN"
```

#### Python
```python
import requests

ACCESS_TOKEN = "your_access_token"
BUSINESS_ID = "6789012345678901234"
PUBLISH_ID = "v_pub_7123456789012345678"

url = "https://business-api.tiktok.com/open_api/v1.3/business/publish/status/"
headers = {"Access-Token": ACCESS_TOKEN}
params = {
    "business_id": BUSINESS_ID,
    "publish_id": PUBLISH_ID
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

#### Phản hồi mẫu khi thành công
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20241023150000021666777888999000",
  "data": {
    "post_ids": [
      "7123456789123456789"
    ],
    "status": "SUCCESS"
  }
}
```

#### Phản hồi mẫu khi đang xử lý
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20241023150000021666777888999111",
  "data": {
    "status": "PROCESSING"
  }
}
```
