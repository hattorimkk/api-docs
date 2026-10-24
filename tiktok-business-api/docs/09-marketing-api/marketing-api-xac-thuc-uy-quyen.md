# Marketing API — bắt đầu, xác thực và ủy quyền

Tài liệu này cung cấp hướng dẫn đầy đủ về quy trình bắt đầu, ủy quyền (Authorization) và xác thực (Authentication) cho TikTok Marketing API. Bạn sẽ tìm hiểu từng bước thiết lập ứng dụng nhà phát triển, quy trình lấy mã ủy quyền (`auth_code`), đổi lấy mã truy cập dài hạn (`access_token`), giải đáp các câu hỏi thường gặp và xử lý các lỗi xác thực phổ biến.

## Bắt đầu (`Get started`)
<a id="doc-1781891830241281"></a>
<!-- doc_id: 1781891830241281 -->

> Đường dẫn: Marketing API > Get started

Chào mừng bạn đến với Marketing API! Chúng tôi thiết kế hệ thống API thân thiện để nhà phát triển có thể tiếp cận và sử dụng một cách dễ dàng nhất. Chỉ cần một vài bước đơn giản, bạn có thể nhận quyền truy cập và bắt đầu quản lý các sản phẩm tiếp thị TikTok của mình. **Dưới đây là các bước cần thực hiện trước khi thực hiện lệnh gọi API đầu tiên và các tài nguyên hữu ích giúp bạn nhanh chóng tích hợp với Marketing API.**

### Quy trình từng bước (Step-by-step workflow)

1. [Tạo tài khoản TikTok For Business](../04-get-started/bat-dau.md#doc-1738855099573250).
2. [Đăng ký làm nhà phát triển](../04-get-started/bat-dau.md#doc-1738855176671234).
3. [Tạo ứng dụng nhà phát triển](../04-get-started/bat-dau.md#doc-1738855242728450).
4. [Ủy quyền (Authorization)](marketing-api-xac-thuc-uy-quyen.md#doc-1738373141733378).
5. [Xác thực (Authentication)](marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162).
6. Thực hiện lệnh gọi API đầu tiên của bạn: Bạn có thể sử dụng [bộ sưu tập Postman TikTok API for Business](https://www.postman.com/tiktok/workspace/tiktok-api-for-business/folder/23207567-9c73b718-e802-40f0-a70d-db8524ed2494) để dễ dàng **kiểm thử** tích hợp mà không ảnh hưởng đến tài khoản TikTok for Business thực tế của bạn.

### Tài nguyên hữu ích (Useful resources)

Để khám phá các tài nguyên hữu ích khác hỗ trợ quá trình bắt đầu, chẳng hạn như giới hạn tốc độ gọi (rate limits), quyền ứng dụng (app permissions) và môi trường sandbox, vui lòng tham khảo [Hướng dẫn Bắt đầu toàn diện](../04-get-started/bat-dau.md#doc-1735713609895937).

## Ủy quyền (`Authorization`)
<a id="doc-1738373141733378"></a>
<!-- doc_id: 1738373141733378 -->

> Đường dẫn: Marketing API > Get started > Authorization

Trước khi sử dụng Marketing API, bạn (nhà phát triển) trước tiên cần nhận được sự ủy quyền từ nhà quảng cáo để quản lý tài khoản của họ.

### Điều kiện tiên quyết (Prerequisites)

* Bạn đã tạo tài khoản TikTok For Business. Xem chi tiết tại [Tạo tài khoản TikTok For Business](../04-get-started/bat-dau.md#doc-1738855099573250).
* Bạn đã đăng ký làm nhà phát triển. Xem chi tiết tại [Đăng ký làm nhà phát triển](../04-get-started/bat-dau.md#doc-1738855176671234).
* Bạn đã tạo ứng dụng nhà phát triển. Xem chi tiết tại [Tạo ứng dụng nhà phát triển](../04-get-started/bat-dau.md#doc-1738855242728450).

### Các bước thực hiện (Steps)

1. Trên cổng TikTok API For Business, điều hướng tới **My Apps**, và nhấp vào ứng dụng bạn muốn yêu cầu ủy quyền. Trong phần **Basic Information**, tìm trường **Advertiser authorization URL**. Gửi URL này cho nhà quảng cáo của bạn để họ phê duyệt ủy quyền.

> [!NOTE]
> Bạn có thể cấu hình tối đa 10 URL chuyển hướng nhà quảng cáo (redirect URLs), bao gồm cả `localhost`. Khi thêm một redirect URL mới, bạn có thể tạo một URL ủy quyền nhà quảng cáo mới.

2. Nhà quảng cáo nhập URL ủy quyền vào trình duyệt. Họ sẽ được chuyển hướng đến danh sách các quyền hạn mà bạn đã chọn khi tạo ứng dụng nhà phát triển.
3. Nhà quảng cáo xem xét các quyền hạn, đồng ý với Thỏa thuận Dịch vụ Nền tảng (Platform Service Agreement) và nhấn **Confirm**.
4. Nhà quảng cáo nhấn **Send Code** để nhận thông báo mã xác minh gửi tới địa chỉ email liên kết với tài khoản quảng cáo của họ.
5. Nhà quảng cáo xác minh danh tính bằng cách nhập mã xác minh và nhấn **Confirm**.

> [!NOTE]
> - Việc xác minh cho một tài khoản quảng cáo đã từng ủy quyền cho ứng dụng nhà phát triển trước đó sẽ có hiệu lực trong 48 giờ. Trong khoảng thời gian này, các yêu cầu ủy quyền lặp lại từ cùng một ứng dụng nhà phát triển sẽ không yêu cầu xác minh bổ sung.
> - Tuy nhiên, nếu tài khoản quảng cáo tìm cách ủy quyền cho một ứng dụng nhà phát triển khác, quy trình xác minh mới sẽ là bắt buộc, bất kể việc xác minh gần đây có liên quan đến ứng dụng khác hay không.

> [!NOTE]
> Trong trường hợp hệ thống phát hiện yêu cầu của bạn có dấu hiệu bất thường, một thông báo nhanh (toast message) báo lỗi ủy quyền thất bại sẽ xuất hiện. Vui lòng thử lại sau. Nếu bạn tin rằng yêu cầu của mình hợp lệ, hãy gửi yêu cầu hỗ trợ qua [Cổng Hỗ trợ Nhà phát triển (Developer Ticket Platform)](https://ads.tiktok.com/athena/requester/boards?identify_key=b25033ef7782d41050cbac74f751d547e9d8ad35a39a541a0f0efbbd51fe722f) để được kiểm tra thêm.

6. Khi quá trình xác minh hoàn tất, nhà quảng cáo sẽ được chuyển hướng tới URL chuyển hướng (redirect URL) mà bạn đã chỉ định khi tạo ứng dụng nhà phát triển. Mã ủy quyền (`auth_code`) được gắn vào cuối redirect URL.

Ví dụ: `https://business-api.tiktok.com/portal/docs？state=your_custom_params&code=3c6dc21d2db289199737bcb8c006c23aaf000a1e&auth_code=1234c21d2db289199737bcb8c006c23aaf000a1e&id=1701890905779201`

7. Nhà phát triển cần triển khai một endpoint phía máy chủ khớp với `redirect_uri` đã chỉ định. Endpoint này sẽ nhận mã ủy quyền (`auth_code`) từ các tham số truy vấn (query parameters) của redirect URL. Ví dụ: nếu redirect URL là `https://business-api.tiktok.com/portal/docs？state=your_custom_params&code=3c6dc21d2db289199737bcb8c006c23aaf000a1e&auth_code=1234c21d2db289199737bcb8c006c23aaf000a1e&id=1701890905779201`, endpoint của bạn phải được định cấu hình để trích xuất mã ủy quyền từ giá trị `auth_code`.

### Các bước tiếp theo (Next steps)

Sau khi nhận được mã ủy quyền (`auth_code`), bạn có thể tiếp tục với bước [Xác thực (Authentication)](marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162) để lấy mã truy cập (`access_token`).

## Câu hỏi thường gặp về Ủy quyền (`Authorization FAQs`)
<a id="doc-1766037914914818"></a>
<!-- doc_id: 1766037914914818 -->

> Đường dẫn: Marketing API > Get started > Authorization > FAQs

Bài viết này tổng hợp một số câu hỏi thường gặp và thông báo lỗi phổ biến về quy trình ủy quyền.

### Các câu hỏi (Questions)

**URL ủy quyền, thời gian hết hạn mã ủy quyền, endpoint xác thực và thời gian hết hạn access token cho Marketing API là gì?**

Bảng dưới đây liệt kê URL ủy quyền, thời hạn mã ủy quyền, endpoint xác thực và thời hạn access token cho Marketing API, Accounts API, Mentions API, TikTok Creator Marketplace API, TikTok One (TTO) API, Discovery API và Spark Ads Recommendation API:

- **Marketing API:**
  - *Mô tả:* Ủy quyền qua tài khoản nhà quảng cáo TikTok For Business.
  - *URL ủy quyền:* URL ủy quyền nhà quảng cáo trên [My Apps](https://business-api.tiktok.com/portal/apps). Xem [Ủy quyền - Bước 1](marketing-api-xac-thuc-uy-quyen.md#doc-1738373141733378).
  - *Thời hạn mã ủy quyền:* Có hiệu lực trong 1 giờ và chỉ sử dụng được 1 lần. Khi `auth_code` hết hạn, bạn phải thực hiện lại quy trình ủy quyền từ đầu.
  - *Endpoint xác thực:* [/oauth2/access_token/](marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162) (Access token nhà quảng cáo).
  - *Thời hạn access token:* Access token nhà quảng cáo không bao giờ hết hạn. Để hủy hiệu lực token, sử dụng [/oauth2/revoke_token/](../12-api-reference/10-authentication.md#doc-1739965949088770).
- **Accounts API / Mentions API:**
  - *Mô tả:* Ủy quyền qua tài khoản TikTok tự nhiên (organic account).
  - *URL ủy quyền:* URL ủy quyền chủ tài khoản TikTok trên [My Apps](https://ads.tiktok.com/i18n/login?redirect=https%3A%2F%2Fads.tiktok.com%2Fmarketing_api%2Fapps%2F). Xem [Accounts - Authorization](../10-organic-api/accounts-api.md#doc-1738083939371009).
  - *Thời hạn mã ủy quyền:* Có hiệu lực trong 10 phút và chỉ sử dụng được 1 lần. Khi hết hạn, phải thực hiện lại từ đầu.
  - *Endpoint xác thực:* [/tt_user/oauth2/token/](../10-organic-api/accounts-api.md#doc-1738084387220481) (Access token tài khoản TikTok).
  - *Thời hạn access token:* Access token tài khoản TikTok có hiệu lực trong 1 ngày. Khi hết hạn, gia hạn token qua [/tt_user/oauth2/refresh_token/](../10-organic-api/accounts-api.md#doc-1738084387220481).
- **TikTok Creator Marketplace (TTCM) API:**
  - *Mô tả:* Ủy quyền qua tài khoản TTCM và tài khoản TikTok tự nhiên. (*Lưu ý: Đang trong giai đoạn thử nghiệm beta đóng, cần đăng ký quyền truy cập*).
  - *URL ủy quyền:* • Ủy quyền tài khoản TTCM: URL ủy quyền nhà quảng cáo trên [My Apps](https://business-api.tiktok.com/portal/apps), xem [TTCM Authorization](https://business-api.tiktok.com/portal/docs?id=1781189065082881). • Ủy quyền nhà sáng tạo: URL ủy quyền chủ tài khoản TikTok trên My Apps, xem [Ủy quyền Creator](../10-organic-api/tiktok-one-api.md#doc-1768506960432130).
  - *Thời hạn mã ủy quyền:* Mã TTCM có hiệu lực 1 giờ (dùng 1 lần); mã Creator có hiệu lực 10 phút (dùng 1 lần).
  - *Endpoint xác thực:* • TTCM: [/oauth2/access_token/](marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). • Creator: **/tt_user/oauth2/token/**.
  - *Thời hạn access token:* Token TTCM không hết hạn; token Creator có hiệu lực 1 ngày (gia hạn qua [/tt_user/oauth2/refresh_token/](../12-api-reference/68-tiktok-one-p1.md#doc-1768493902119937)).
- **TikTok One (TTO) API:**
  - *Mô tả:* Ủy quyền qua tài khoản TTO Creator Marketplace.
  - *URL ủy quyền:* URL ủy quyền nhà quảng cáo trên My Apps. Xem [Ủy quyền TTO](../10-organic-api/tiktok-one-api.md#doc-1825117875361793).
  - *Thời hạn mã ủy quyền:* Có hiệu lực 1 giờ, dùng 1 lần.
  - *Endpoint xác thực:* [/oauth2/access_token/](marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162).
  - *Thời hạn access token:* Không hết hạn (hủy hiệu lực qua [/oauth2/revoke_token/](../12-api-reference/10-authentication.md#doc-1739965949088770)).
- **Discovery API:**
  - *Mô tả:* Ủy quyền qua nhà quảng cáo TikTok For Business hoặc tài khoản TikTok tự nhiên.
  - *URL ủy quyền:* • Khi liên quan đến hashtags: URL ủy quyền nhà quảng cáo trên My Apps (xem [Ủy quyền Marketing API](#doc-1738373141733378)). • Khi liên quan đến bài nhạc (tracks): URL ủy quyền chủ tài khoản TikTok trên My Apps (xem [Ủy quyền Accounts API](../10-organic-api/accounts-api.md#doc-1738083939371009)).
  - *Thời hạn mã ủy quyền:* Mã nhà quảng cáo 1 giờ; mã người dùng TikTok 10 phút.
  - *Endpoint xác thực:* [/oauth2/access_token/](marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162) hoặc [/tt_user/oauth2/token/](../10-organic-api/accounts-api.md#doc-1738084387220481).
  - *Thời hạn access token:* Token nhà quảng cáo không hết hạn; token tài khoản TikTok có hiệu lực 1 ngày.
- **Spark Ads Recommendation API:**
  - *Mô tả:* Ủy quyền qua tài khoản TTCM hoặc tài khoản TikTok tự nhiên.
  - *URL ủy quyền:* • Cho [/spark_ad/recommend/](../12-api-reference/63-spark-ads-recommendation.md#doc-1825128700959746): URL ủy quyền nhà quảng cáo (xem [TTCM Authorization](https://business-api.tiktok.com/portal/docs?id=1781189065082881)). • Cho [/business/video/recommend/](../12-api-reference/63-spark-ads-recommendation.md#doc-1825128684907522): URL ủy quyền chủ tài khoản TikTok (xem [Ủy quyền Accounts API](../10-organic-api/accounts-api.md#doc-1738083939371009)).
  - *Thời hạn mã ủy quyền:* TTCM 1 giờ; TikTok account 10 phút.
  - *Endpoint xác thực:* [/oauth2/access_token/](marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162) hoặc [/tt_user/oauth2/token/](../10-organic-api/accounts-api.md#doc-1738084387220481).
  - *Thời hạn access token:* TTCM không hết hạn; TikTok account có hiệu lực 1 ngày.

**Tôi có thể tìm khóa bí mật (secret key) của ứng dụng nhà phát triển ở đâu?**

Khóa bí mật có thể được tìm thấy trong phần Basic Information của ứng dụng tại trang [My Apps](https://ads.tiktok.com/i18n/login?redirect=https%3A%2F%2Fads.tiktok.com%2Fmarketing_api%2Fapps%2F).

**Tại sao mã xác thực (auth_code) bị thiếu khi nhà quảng cáo của tôi được chuyển hướng tới URL chuyển hướng?**

URL chuyển hướng mà bạn cung cấp đang bị chuyển hướng tiếp (redirect loop/chain). Ví dụ: `ABC.com/auth_code=123` bị chuyển hướng sang `abc.com/`. Vui lòng sử dụng URL khác làm redirect URL hoặc liên hệ với quản trị viên trang web của bạn để khắc phục vấn đề này.

**Vai trò của địa chỉ callback trong quy trình ủy quyền là gì?**

Sau khi nhận được URL ủy quyền từ nhà phát triển, nhà quảng cáo nhập URL vào trình duyệt. Họ sẽ được điều hướng tới trang xem xét các quyền hạn do nhà phát triển yêu cầu. Sau khi nhấn **Confirm** để cấp quyền, một trang mới sẽ mở ra. URL của trang đó chính là địa chỉ callback được gắn thêm mã ủy quyền, theo định dạng `...&auth_code=`.

**Làm thế nào để thiết lập địa chỉ callback?**

Địa chỉ callback phải là địa chỉ mạng internet bên ngoài (extranet). Các địa chỉ mạng nội bộ như `http://localhost:0001` sẽ không hoạt động trên môi trường production. Bạn có thể sử dụng URL trang web công ty hoặc các liên kết web công khai khác. Khi có yêu cầu gửi tới địa chỉ này, mã của bạn có thể bóc tách và lấy mã ủy quyền.

**Làm thế nào để thu hồi quyền truy cập của nhà phát triển đối với các tài khoản quảng cáo mà người dùng TikTok For Business đã ủy quyền?**

Để thu hồi quyền truy cập của nhà phát triển đối với tài khoản quảng cáo, bạn có thể thực hiện như sau:
- Nếu bạn là nhà quảng cáo (người dùng TikTok For Business) muốn hủy quyền quản lý của nhà phát triển, hãy truy cập [trang cài đặt ủy quyền TikTok For Business](https://ads.tiktok.com/ac/page/authorizations). Tại đây, nhấp vào **Remove** để thu hồi ủy quyền đã cấp cho nhà phát triển cụ thể.
- Nếu bạn là nhà phát triển muốn hủy quyền thay cho nhà quảng cáo, bạn có thể sử dụng endpoint [/oauth2/revoke_token/](../12-api-reference/10-authentication.md#doc-1739965949088770) để thu hồi access token liên kết với ủy quyền đó.

### Các thông báo lỗi phổ biến (Common error messages)

| Thông báo lỗi | Nguyên nhân | Giải pháp |
|---|---|---|
| "Advertiser does not grant you the permission for xxx" (xxx là tên endpoint) | Nhà quảng cáo (người dùng TikTok for Business) được gửi liên kết xác thực đã không cấp quyền truy cập vào endpoint đó. | Chọn các quyền bạn cần và yêu cầu nhà quảng cáo ủy quyền lại. Xem [Cập nhật quyền ứng dụng](../04-get-started/bat-dau.md#doc-1738855280338946) và [Ủy quyền](marketing-api-xac-thuc-uy-quyen.md#doc-1738373141733378) để biết các bước chi tiết. |
| "Redirect Url Not Match" khi nhà quảng cáo truy cập URL ủy quyền | Tham số `redirect_url` trong URL ủy quyền không khớp với địa chỉ callback ứng dụng nhà phát triển đã cấu hình. | Đảm bảo phần `redirect_url` trong URL ủy quyền hoàn toàn trùng khớp với địa chỉ callback đã cấu hình cho ứng dụng nhà phát triển. |
| Lỗi hiển thị trên trang được chuyển hướng sau khi hoàn tất ủy quyền | Địa chỉ callback không phải địa chỉ internet hợp lệ hoặc dùng địa chỉ mạng nội bộ (như `https://localhost:port_number/`). | Đảm bảo địa chỉ callback là địa chỉ hợp lệ và có thể truy cập công khai trên internet. |
| "Invalid auth code" khi lấy access token dài hạn | `auth_code` đã hết hạn. Mã này chỉ có hiệu lực trong 1 giờ (hoặc 10 phút tùy loại) sau khi được tạo. | Bạn cần thực hiện lại quy trình ủy quyền. Gửi URL ủy quyền cho nhà quảng cáo để họ phê duyệt lại, sau đó dùng `auth_code` mới để lấy access token. |
| "You don't have permission to operate advertiser xxxx" hoặc "Insufficient advertiser permission: Please ask the BC admin with resource permission to grant access to the advertisers (adv_id:xxxx)." | Nhà quảng cáo ủy quyền access token không có quyền truy cập vào tài khoản quảng cáo tương ứng trong Business Center hoặc không phải chủ sở hữu tài khoản. | • Liên hệ quản trị viên Business Center để [thêm quyền cho nhà quảng cáo](https://ads.tiktok.com/help/article/add-users-tiktok-business-center?lang=en). <br> • [Hoặc] Xin ủy quyền từ người dùng mới có quyền truy cập vào tài khoản quảng cáo đó. |

## Xác thực (`Authentication`)
<a id="doc-1738373164380162"></a>
<!-- doc_id: 1738373164380162 -->

> Đường dẫn: Marketing API > Get started > Authentication

Với mã `auth_code` nhận được sau khi nhà quảng cáo [ủy quyền](marketing-api-xac-thuc-uy-quyen.md#doc-1738373141733378), bạn có thể gửi yêu cầu đến endpoint dưới đây để nhận mã `access_token` phục vụ cho các yêu cầu API tiếp theo.

### Tạo mã truy cập (Generate an access token)

Nếu bạn muốn chỉ định `Content-Type` là `application/json` để lấy access token dài hạn, bạn có thể gửi yêu cầu POST tới endpoint `/oauth2/access_token/`. Chỉ định `app_id`, `auth_code` và `secret` trong yêu cầu. Trong phản hồi, danh sách các ID nhà quảng cáo mà mã token này có thể truy cập, cùng với phạm vi quyền hạn (scope) của access token, cũng sẽ được trả về.

Mã `auth_code` có giá trị trong vòng 1 giờ và chỉ có thể được sử dụng duy nhất một lần. Sau khi `auth_code` hết hạn, bạn cần bắt đầu lại và thực hiện lại các bước ủy quyền.

Nếu bạn muốn chỉ định `Content-Type` là `application/x-www-form-urlencoded` để lấy access token dài hạn, bạn cần gọi endpoint [/oauth/token/](../12-api-reference/10-authentication.md#doc-1739965703387137) thay thế.

> [!NOTE]
> Nếu access token bị mất, vui lòng thông báo cho nhà quảng cáo hủy ủy quyền hoặc liên hệ với quản trị viên vận hành.

#### Yêu cầu (Request)

**Endpoint:** `POST https://business-api.tiktok.com/open_api/v1.3/oauth2/access_token/`

**Header:**

| Field | Data Type | Description |
|---|---|---|
| Content-Type | string | Loại thông điệp yêu cầu (bắt buộc). <br> Định dạng được chấp nhận: `"application/json"` |

**Parameters:**

| Field | Data Type | Description |
|---|---|---|
| app_id | string | ID ứng dụng nhà phát triển của bạn (bắt buộc). <br> Để tìm **App ID**, điều hướng đến [My Apps](https://ads.tiktok.com/marketing_api/apps/) > **App Detail** > **Basic Information**. |
| secret | string | Khóa bí mật của ứng dụng nhà phát triển (bắt buộc). <br> Để tìm **Secret**, điều hướng đến [My Apps](https://ads.tiktok.com/marketing_api/apps/) > **App Detail** > **Basic Information**. |
| auth_code | string | Mã ủy quyền (`auth_code`) được tạo ra từ **URL ủy quyền nhà quảng cáo** của bạn (bắt buộc). <br> Mã có hiệu lực trong 1 giờ và chỉ dùng được 1 lần. <br> Để biết cách lấy mã ủy quyền theo từng loại API, xem dòng "Authorization URL" trong [So sánh ủy quyền cho các API khác nhau](../04-get-started/bat-dau.md#doc-1781891256601602). |

#### Ví dụ (Example)

```http
// curl
curl --location -request POST 'https://business-api.tiktok.com/open_api/v1.3/oauth2/access_token/' \
--header 'Content-Type: application/json' \
--data '{
    "app_id": "{{app_id}}",
    "secret": "{{secret}}",
    "auth_code": "{{auth_code}}"
}'
```

#### Phản hồi (Response)

| Field | Type | Description |
|---|---|---|
| code | number | Mã trả về, xem [Phụ lục - Mã trả về (Return codes)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông điệp trả về, xem [Phụ lục - Mã trả về (Return codes)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | ID duy nhất của yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ access_token | string | Mã truy cập dài hạn (long-term access token) dùng để xác minh quyền hạn. |
| ↳ advertiser_ids | string[] | Danh sách các tài khoản quảng cáo mà token này có quyền truy cập. |
| ↳ scope | number[] | Phạm vi quyền hạn được cấp cho access token. <br> Xem [Phạm vi quyền (Permission scope)](../15-appendix/phu-luc-p1.md#doc-1753986142651394) để biết quyền hạn tương ứng với từng scope ID (giá trị của `scope`). |

#### Ví dụ phản hồi (Example response)

```http
// Success-Response
HTTPS/1.1 200 OK
{
  "message": "OK",
  "code": 0,
  "data": {
    "access_token": "xxxxxxxxxxxxx",
    "scope": [
      4
    ],
    "advertiser_ids": [
      "123456789",
      "123456781"
    ]
  },
  "request_id": "2020042715295501023125104093250"
}
```

### Hủy hiệu lực mã truy cập (Invalidate an access token)

Access token dài hạn không tự hết hạn, nhưng nó sẽ mất hiệu lực nếu nhà quảng cáo hủy ủy quyền. Bạn cũng có thể sử dụng endpoint [/oauth2/revoke_token/](../12-api-reference/10-authentication.md#doc-1739965949088770) để chủ động vô hiệu hóa access token.

Với access token, bạn có thể truy cập các endpoint theo những quyền hạn đã được nhà quảng cáo chấp thuận, chứ không phải các quyền bạn đã đăng ký khi tạo ứng dụng nhà phát triển.

Để lấy danh sách đầy đủ các tài khoản nhà quảng cáo có thể truy cập bằng access token, hãy sử dụng endpoint `/oauth2/advertiser/get/`.

### Các bước tiếp theo (Next steps)

Thực hiện yêu cầu API đầu tiên của bạn:
- Tham khảo **Tham chiếu API (API Reference)** để xem danh sách đầy đủ các endpoint API.
- Sử dụng [bộ sưu tập Postman](../04-get-started/bat-dau.md#doc-1747849403155521) để tiến hành kiểm thử API.
- Sử dụng [tài khoản sandbox](../04-get-started/bat-dau.md#doc-1738855331457026) để kiểm tra việc tích hợp mà không ảnh hưởng đến tài khoản TikTok For Business thực tế của bạn.

## Câu hỏi thường gặp về Xác thực (`Authentication FAQs`)
<a id="doc-1766041812130817"></a>
<!-- doc_id: 1766041812130817 -->

> Đường dẫn: Marketing API > Get started > Authentication > FAQs

Bài viết này tổng hợp một số câu hỏi phổ biến và thông báo lỗi về xác thực.

### Các câu hỏi (Questions)

**Đối với một access token hiện có, nó có tự động khả dụng cho các tài khoản nhà quảng cáo mới khi các tài khoản này được tạo hay không, hay tôi cần tạo mã xác thực mới và access token mới mỗi lần có tài khoản mới được tạo?**

Nếu người dùng xác thực nhận được quyền truy cập vào một tài khoản quảng cáo mới, bạn sẽ không cần phải xác thực lại và tạo lại access token. Ứng dụng nhà phát triển sẽ tự động có quyền truy cập dữ liệu từ tài khoản quảng cáo mới này.

### Các thông báo lỗi phổ biến (Common error messages)

| Thông báo lỗi phổ biến | Nguyên nhân | Giải pháp |
|---|---|---|
| "Access token is invalid, when you call access_token or refresh_token api, old token will become invalid". | Access token đã hết hạn hoặc không tồn tại. | Đảm bảo bạn đang sử dụng access token mới nhất và access token được nhập chính xác. |
| "Advertiser xxxx doesn't exist or has been deleted." | Tài khoản quảng cáo không tồn tại hoặc đã bị xóa. | Đảm bảo rằng bạn nhập đúng ID nhà quảng cáo. |
| "No access to operation advertiser xxx". | Access token không khớp với ID nhà quảng cáo. | Đảm bảo rằng bạn nhập đúng access token tương ứng với ID nhà quảng cáo đó. |
