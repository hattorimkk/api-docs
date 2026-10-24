# Organic API — TikTok One API

> Phân hệ: guide:Organic API/TikTok One API.
> Tài liệu biên dịch kỹ thuật chi tiết theo chuẩn TikTok Business API v1.3.

---

## Mục lục điều hướng
- [1. TikTok One API (#doc-1735827019995138)](#doc-1735827019995138)
- [2. Tổng quan (Overview) (#doc-1763402336271362)](#doc-1763402336271362)
- [3. Hướng dẫn (Guides) (#doc-1763403737310209)](#doc-1763403737310209)
- [4. Bắt đầu với TTO API (Get started for TTO API) (#doc-1825117808886785)](#doc-1825117808886785)
- [5. Lấy ủy quyền và xác thực từ tài khoản TTO Creator Marketplace (#doc-1825117875361793)](#doc-1825117875361793)
- [6. Lấy ủy quyền từ Creator (Get authorization from Creators) (#doc-1768506960432130)](#doc-1768506960432130)
- [7. Lấy thông tin phân tích chi tiết của Creator (Get Creator insights) (#doc-1763404664004609)](#doc-1763404664004609)
- [8. Liên kết nội dung TTO Creator Marketplace (Content Linking) (#doc-1830337139853313)](#doc-1830337139853313)
- [9. Tạo và quản lý chiến dịch TTO Creator Marketplace (#doc-1828929329184770)](#doc-1828929329184770)
- [10. Lấy ủy quyền Spark Ads (Get Spark Ads authorization) (#doc-1740027794580481)](#doc-1740027794580481)
- [11. Giới hạn tần suất gọi cho TTO API (Rate limits for TTO API) (#doc-1825117901366274)](#doc-1825117901366274)
- [12. Danh mục API tham chiếu (API reference) (#doc-1740302141934593)](#doc-1740302141934593)

---

<a id="doc-1735827019995138"></a>
<!-- doc_id: 1735827019995138 -->
<!-- doc_id: 1735827019995138 -->
# TikTok One API
> Đường dẫn: Organic API > TikTok One API
[TikTok One (TTO)](https://ads.tiktok.com/creative) là nền tảng sáng tạo tập trung tất cả trong một của TikTok, nơi bạn có thể tiếp cận hàng triệu nhà sáng tạo nội dung (creator), kết nối với các đối tác sản xuất và khám phá các thông tin chuyên sâu về sáng tạo — tất cả tại một nơi duy nhất.

TTO API cho phép bạn truy cập dữ liệu nhà sáng tạo trên TTO Creator Marketplace và tìm kiếm các nhà sáng tạo phù hợp để hợp tác sản xuất các video nội dung gắn thẻ thương hiệu (Branded Content videos).

Khám phá tài liệu:
- Bắt đầu
  - [Tổng quan](tiktok-one-api.md#doc-1763402336271362): Tìm hiểu về lợi ích và các khái niệm cốt lõi của TTO API.
  - [Bắt đầu với TTO API](tiktok-one-api.md#doc-1825117808886785): Nắm bắt quy trình tích hợp và triển khai chung của TTO API.
- Triển khai kỹ thuật
  - [Giới hạn tần suất gọi cho TTO API](tiktok-one-api.md#doc-1825117901366274): Làm quen với các quy định về giới hạn tốc độ gọi (rate limits) áp dụng riêng cho TTO API.
  - [Danh mục API tham chiếu](tiktok-one-api.md#doc-1740302141934593): Khám phá danh mục tài liệu kỹ thuật toàn diện cho tất cả các endpoint TTO API hiện có.

> **Quan trọng:**
> Kể từ ngày 30 tháng 6 năm 2025, bạn sẽ không thể sử dụng các endpoint cũ của TikTok Creator Marketplace. Các endpoint này đã được thay thế bằng các endpoint TikTok One API mới nhằm mang đến trải nghiệm thị trường nhà sáng tạo tối ưu và liền mạch hơn. Để đảm bảo quá trình tích hợp diễn ra trơn tru, chúng tôi khuyến nghị bạn chuyển đổi sang các endpoint TikTok One càng sớm càng tốt.

---

<a id="doc-1763402336271362"></a>
<!-- doc_id: 1763402336271362 -->
<!-- doc_id: 1763402336271362 -->
# Tổng quan (Overview)
> Đường dẫn: Organic API > TikTok One API > Overview
[TikTok One (TTO)](https://ads.tiktok.com/creative) là nền tảng sáng tạo toàn diện của TikTok, nơi bạn có thể kết nối với hàng triệu nhà sáng tạo, tìm kiếm đối tác sản xuất và khai thác những hiểu biết sâu sắc về nội dung sáng tạo. Để tìm hiểu thêm về nền tảng TikTok One, hãy xem [Giới thiệu về TikTok One](https://ads.tiktok.com/creative/creatormarketplace/help/10039883/10021904). TTO Creator Marketplace mang đến cho các thương hiệu cơ hội hợp tác với các nhà sáng tạo trong các chiến dịch nội dung thương hiệu và truy cập báo cáo chi tiết về hiệu suất tiếp thị qua nhà sáng tạo.

TTO API cho phép bạn truy xuất dữ liệu nhà sáng tạo trên TTO Creator Marketplace và khám phá những nhà sáng tạo tiềm năng để hợp tác sản xuất video Branded Content.

## Lợi ích của TTO API
- **Khám phá và tương tác với đúng nhà sáng tạo**: Tự động hóa quá trình chọn lọc nhà sáng tạo có lượng khán giả tương tác cao phù hợp với mục tiêu chiến dịch của bạn.
- **Quản lý và thực thi chiến dịch**: Dễ dàng tạo và theo dõi chiến dịch tại một nơi duy nhất, đồng thời tinh gọn hóa quy trình làm việc giữa thương hiệu và nhà sáng tạo.
- **Báo cáo chi tiết theo thời gian thực (First-party data)**: Nhanh chóng nắm bắt hiệu suất chiến dịch; giảm thiểu rủi ro và thúc đẩy kết quả nhanh hơn nhờ thông tin chuyên sâu sáng tạo nâng cao.
- **Tạo quảng cáo Spark Ads theo phương thức lập trình**: Nhận đề xuất và khuếch đại tiếng nói thương hiệu bằng cách mở rộng phạm vi tiếp cận và mức độ hiển thị thông qua việc tạo Spark Ads từ nội dung của nhà sáng tạo một cách tự động.

## Vai trò và khái niệm cốt lõi
- **Creator (Nhà sáng tạo)**: Bất kỳ nhà sáng tạo nào trên TikTok (loại Tài khoản Cá nhân - Personal Account, không phải Tài khoản Doanh nghiệp - Business Account) có thể được nhà quảng cáo mời tạo video để quảng bá sản phẩm hoặc thương hiệu.
- **Advertiser (Nhà quảng cáo)**: Thương hiệu hoặc đại lý muốn quảng bá sản phẩm/thương hiệu trên TikTok và sử dụng TikTok Creator Marketplace để tìm kiếm nhà sáng tạo hợp tác.
- **Developer (Nhà phát triển)**: Cá nhân nhà phát triển hoặc đối tác kỹ thuật hỗ trợ nhà quảng cáo tích hợp API. Trừ khi được chỉ định rõ một vai trò cụ thể, mọi thao tác đều do nhà phát triển thực hiện. Từ "Bạn" trong hầu hết các trường hợp cũng nhằm chỉ nhà phát triển.
- **TTO Official Video (Video chính thức TTO)**: Video TikTok đã được liên kết với một chiến dịch TTO Creator Marketplace.
- **Invite link (Liên kết mời)**: Liên kết mà nhà sáng tạo có thể sử dụng để gắn thẻ video thành Video chính thức TTO trước khi đăng tải hoặc gắn thẻ hồi tố. Liên kết này có thể được tạo qua endpoint [/tto/tcm/campaign/create/](../12-api-reference/68-tiktok-one-p1.md#doc-1815693549459458).
  - **Campaign-level invite link (Liên kết mời cấp chiến dịch)**: Loại liên kết mời cụ thể nhằm liên kết video với một chiến dịch nhất định.
  - **Brand-level invite link (Liên kết mời cấp thương hiệu)**: Loại liên kết mời khác dùng để tổng hợp nội dung dưới tài khoản thương hiệu vô thời hạn.
- **Linking request (Yêu cầu liên kết)**: Thông báo trong ứng dụng được gửi trực tiếp đến hộp thư của nhà sáng tạo, nhắc họ gắn thẻ video hồi tố.

---

<a id="doc-1763403737310209"></a>
<!-- doc_id: 1763403737310209 -->
<!-- doc_id: 1763403737310209 -->
# Hướng dẫn (Guides)
> Đường dẫn: Organic API > TikTok One API > Guides
Các tài liệu hướng dẫn này sẽ dẫn dắt bạn qua quy trình làm việc và các chức năng tổng thể của TikTok One (TTO) API.
- [Bắt đầu với TTO API](tiktok-one-api.md#doc-1825117808886785)
- [Lấy ủy quyền và xác thực từ tài khoản TTO Creator Marketplace của bạn](tiktok-one-api.md#doc-1825117875361793)
- [Lấy ủy quyền từ Creator](tiktok-one-api.md#doc-1768506960432130)
- [Lấy thông tin phân tích chi tiết của Creator](tiktok-one-api.md#doc-1763404664004609)
- [Liên kết nội dung TTO Creator Marketplace (Content Linking)](tiktok-one-api.md#doc-1830337139853313)
- [Tạo và quản lý chiến dịch TTO Creator Marketplace](tiktok-one-api.md#doc-1828929329184770)
- [Lấy ủy quyền Spark Ads](tiktok-one-api.md#doc-1740027794580481)
- [Giới hạn tần suất gọi cho TTO API](tiktok-one-api.md#doc-1825117901366274)

---

<a id="doc-1825117808886785"></a>
<!-- doc_id: 1825117808886785 -->
<!-- doc_id: 1825117808886785 -->
# Bắt đầu với TTO API (Get started for TTO API)
> Đường dẫn: Organic API > TikTok One API > Guides > Get started for TTO API
Được thiết kế tối ưu cho nhà phát triển, quy trình truy cập và sử dụng API của chúng tôi rất nhanh chóng và thuận tiện. **Dưới đây là các bước bạn cần hoàn thành trước khi thực hiện lượt gọi API đầu tiên, cùng các tài nguyên hữu ích hỗ trợ tích hợp TTO API.**

## Quy trình tích hợp từng bước (Step-by-step onboarding workflow)
Để bắt đầu với TTO API, hãy làm theo các bước sau:
1. Thiết lập ứng dụng nhà phát triển TikTok for Business:
	1. [Tạo tài khoản TikTok For Business](../04-get-started/bat-dau.md#doc-1738855099573250).
	2. [Đăng ký tài khoản nhà phát triển](../04-get-started/bat-dau.md#doc-1738855176671234).
	3. [Tạo ứng dụng nhà phát triển](../04-get-started/bat-dau.md#doc-1738855242728450). Sau khi ứng dụng được phê duyệt, hãy liên hệ với Quản lý đối tác (Partner Manager) của bạn kèm theo App ID để yêu cầu quyền truy cập vào các endpoint TTO.
2. Cấu hình tài khoản TTO Creator Marketplace:
	1. Đăng ký tài khoản [TTO Creator Marketplace](https://ads.tiktok.com/creative/creatormarketplace).
	2. [Lấy ủy quyền và xác thực từ tài khoản TTO Creator Marketplace của bạn](tiktok-one-api.md#doc-1825117875361793).
3. Hợp tác với các nhà sáng tạo:
	1. Tạo chiến dịch và yêu cầu ủy quyền Spark Ads mặc định cho các video TikTok được tải lên chiến dịch bằng cách gọi [/tto/tcm/campaign/create/](../12-api-reference/68-tiktok-one-p1.md#doc-1815693549459458).
	2. Chia sẻ liên kết mời (invite link) với nhà sáng tạo.
	3. Nhà sáng tạo sử dụng liên kết mời để tải video lên TikTok.
4. Giám sát hiệu suất:
	- Theo dõi hiệu suất video bằng endpoint [/tto/tcm/report/](../12-api-reference/68-tiktok-one-p2.md#doc-1815693573340162).
5. [Tạo quảng cáo Spark Ads](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1739470744631298) sử dụng các video TikTok đã được tải lên và liên kết thành công.

---

<a id="doc-1825117875361793"></a>
<!-- doc_id: 1825117875361793 -->
<!-- doc_id: 1825117875361793 -->
# Lấy ủy quyền và xác thực từ tài khoản TTO Creator Marketplace
> Đường dẫn: Organic API > TikTok One API > Guides > Obtain authorization and authentication from a TTO Creator Marketplace account
Tài liệu này mô tả chi tiết quy trình lấy quyền ủy quyền và xác thực từ tài khoản TikTok One (TTO) Creator Marketplace dành cho nhà phát triển. Mục đích của quy trình này là đảm bảo quyền truy cập an toàn, thiết lập các phạm vi quyền hạn và xác minh danh tính của nhà phát triển khi tương tác với tài khoản TTO Creator Marketplace. Đối tác phải đảm bảo mọi chiến dịch TTO Creator Marketplace đều được tạo từ tài khoản TTO Creator Marketplace của chính đối tác.

## Lấy ủy quyền từ tài khoản TTO Creator Marketplace
Để lấy ủy quyền từ tài khoản TTO Creator Marketplace:
1. Tìm **URL ủy quyền nhà quảng cáo (Advertiser authorization URL)** bằng cách truy cập [My Apps](https://business-api.tiktok.com/portal/apps) > **App Detail** > **Basic Information**.  
URL này được sử dụng để cấp quyền cho cả tài khoản nhà quảng cáo lẫn tài khoản TTO Creator Marketplace. Hãy yêu cầu chủ sở hữu tài khoản đăng nhập vào cả [tài khoản TTO Creator Marketplace](https://ads.tiktok.com/creative/creatormarketplace) và [tài khoản TikTok Ads Manager](https://ads.tiktok.com/i18n/home) tương ứng.
2. Chia sẻ **URL ủy quyền nhà quảng cáo** với chủ tài khoản TTO Creator Marketplace để nhận mã ủy quyền (authorization code).
3. Chủ tài khoản TTO Creator Marketplace tiến hành cấp quyền cho Ứng dụng nhà phát triển qua **URL ủy quyền nhà quảng cáo** (phải chọn cấp quyền cho TTO Creator Marketplace).
4. Sau khi hoàn tất ủy quyền, chủ tài khoản sẽ được chuyển hướng về Redirect URL của Ứng dụng, và bạn cần trích xuất mã `auth_code` từ URL đó. Lưu ý rằng `auth_code` chỉ có hiệu lực trong 1 giờ và chỉ sử dụng được 1 lần.

## Lấy token xác thực từ tài khoản TTO Creator Marketplace
Để tạo mã truy cập (access token) cho TTO Creator Marketplace, hãy gọi endpoint [/oauth2/access_token/](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). Phản hồi API sẽ không chứa ID tài khoản TTO Creator Marketplace nhưng sẽ chứa access token. Mã token này không bao giờ hết hạn trừ khi người dùng chủ động thu hồi quyền truy cập.

### Ví dụ lệnh cURL (Example)
```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/oauth2/access_token/' --header 'Content-Type: application/json' --data '{
    "app_id" : "YOUR_APP_ID",
    "auth_code" : "YOUR_AUTH_CODE",
    "secret" : "YOUR_APP_SECRET"
}'
```

Lưu ý: Để tạo các chiến dịch TTO Creator Marketplace, bạn cần cung cấp đồng thời cả access token và ID tài khoản TTO Creator Marketplace. Bạn có thể tra cứu ID tài khoản TTO Creator Marketplace thông qua trường `tto_tcm_account_ids` được trả về từ [/tto/oauth2/tcm/](../12-api-reference/68-tiktok-one-p1.md#doc-1815693478150146).

---

<a id="doc-1768506960432130"></a>
<!-- doc_id: 1768506960432130 -->
<!-- doc_id: 1768506960432130 -->
# Lấy ủy quyền từ Creator (Get authorization from Creators)
> Đường dẫn: Organic API > TikTok One API > Guides > Get authorization from Creators

## Các bước thực hiện
1. Chia sẻ **URL ủy quyền cho chủ tài khoản TikTok (TikTok account holder authorization URL)** với Creator.
2. Creator tiến hành phê duyệt và cấp quyền cho Ứng dụng nhà phát triển của bạn.
3. Gọi API để lấy mã truy cập (access token).
4. Khi access token hết hạn, sử dụng refresh token để lấy access token mới. Access token có hiệu lực trong 24 giờ và refresh token có hiệu lực trong 1 năm.
5. [Tùy chọn] Thu hồi access token khi không còn nhu cầu sử dụng.

### Bước 1: Chia sẻ URL ủy quyền với Creator
Xác định **URL ủy quyền cho chủ tài khoản TikTok** của Ứng dụng nhà phát triển và gửi cho Creator. Đường dẫn này có thể được tìm thấy tại [**My Apps**](https://ads.tiktok.com/marketing_api/apps/) > **App Detail** > **Basic Information** > **TikTok account holder authorization URL**.

Để đảm bảo người dùng có thể cấp quyền cho ứng dụng mà không gặp lỗi, bạn bắt buộc phải tải lên hình ảnh **Logo ứng dụng (App logo)** để người dùng nhìn thấy trong giao diện cấp quyền. Nếu chưa có logo, bạn cần tải lên hình ảnh định dạng JPG, JPEG hoặc PNG với kích thước tối đa 512 * 512px.

Nếu không tải logo ứng dụng lên, người dùng sẽ gặp trang báo lỗi khi thực hiện ủy quyền.

#### Quy tắc định dạng cho URL chuyển hướng (Redirect URL)
> **Lưu ý:**
> Bạn có thể cấu hình tối đa 10 Redirect URL cho chủ tài khoản TikTok trên mỗi ứng dụng nhà phát triển. Mỗi Redirect URL được kích hoạt sẽ tự động tạo một URL ủy quyền tương ứng. Hệ thống duy trì một URL đang kích hoạt tại một thời điểm (được đánh dấu màu đỏ). Khi chỉ có một Redirect URL, nó sẽ tự động kích hoạt theo mặc định. Với nhiều URL, hãy nhấp vào URL bạn muốn kích hoạt.

Khi thiết lập **TikTok account holder redirect URL** cho ứng dụng của bạn, hãy tuân thủ các quy tắc định dạng sau để đảm bảo hoạt động chính xác:

| STT | Quy tắc | Ví dụ đúng | Ví dụ sai |
|---|---|---|---|
| 1 | URL phải là tuyệt đối và kết thúc bằng `/`. | `https://dev.example.com/auth/callback/` | • `https://dev.example.com/auth/callback` (thiếu dấu `/` ở cuối)<br>• `/auth/callback/` (thiếu giao thức và tên miền) |
| 2 | URL phải là tĩnh, tham số truy vấn bị từ chối và sẽ bị bỏ qua. | `https://dev.example.com/auth/callback/` | • `https://dev.example.com/auth/callback/?id=1` (chứa tham số query `?id=1`) |
| 3 | URL không được chứa ký tự neo `#`. | `https://dev.example.com/auth/callback/` | • `https://dev.example.com/auth/callback/#1` (chứa thẻ neo `#1`) |
| 4 | URL phải bắt đầu bằng giao thức `https://`. | `https://dev.example.com/auth/callback/` | • `http://dev.example.com/auth/callback/` (sử dụng `http` thay vì `https`) |
| 5 | URL không được chỉ định cổng (port). | `https://dev.example.com/auth/callback/` | • `https://dev.example.com:3000/auth/callback/` (chứa cổng `:3000`) |
| 6 | Độ dài của URI đăng ký phải nằm trong khoảng từ 10 đến 512 ký tự. | N/A | N/A |

Nếu không tuân thủ các quy tắc trên, hệ thống sẽ trả về thông báo lỗi và bạn cần chỉnh sửa lại Redirect URL tương ứng.

### Bước 2: Creator cấp quyền ủy quyền
Khi mở URL ủy quyền, Creator sẽ được nhắc phê duyệt ứng dụng nhà phát triển của bạn. Sau khi nhấp vào nút **Authorize (Ủy quyền)**, Creator sẽ được chuyển hướng về Redirect URL của ứng dụng. URL chuyển hướng lúc này sẽ đính kèm tham số `code=`, chính là giá trị `auth_code` cần thiết để đổi lấy access token.

> **Quan trọng:**
> `auth_code` chỉ có giá trị sử dụng trong vòng 10 phút và chỉ dùng được một lần duy nhất. Sau khi `auth_code` hết hạn, bạn phải thực hiện lại quy trình ủy quyền từ đầu.

Trong quá trình ủy quyền, hãy đảm bảo Creator đã phê duyệt các phạm vi quyền hạn (scope) sau:
- `biz.creator.insights`
- `user.insights.creator`
- `biz.creator.info`

### Bước 3: Lấy mã truy cập (access token)
Gọi endpoint **/tt_user/oauth2/token/** với `grant_type` là `authorization_code`, truyền vào `auth_code` và `redirect_uri`. App ID và Secret của ứng dụng nhà phát triển có thể lấy tại trang cài đặt ứng dụng.

#### Ví dụ lệnh cURL (Example)
```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/tt_user/oauth2/token/' --header 'Content-Type: application/json' --data-raw '{
 "grant_type" : "authorization_code",
 "auth_code" : "YOUR_AUTH_CODE",
 "client_secret": "YOUR_CLIENT_SECRET",
 "client_id": "YOUR_CLIENT_ID",
 "redirect_uri": "https://dev.example.com/auth/callback/"
}'
```

Dữ liệu phản hồi sẽ bao gồm các trường quan trọng sau đây, bạn cần lưu trữ an toàn `access_token`, `open_id` và `refresh_token`:
- `access_token`: Mã truy cập API.
- `scope`: Danh sách phạm vi quyền hạn được cấp.
- `expires_in`: Thời gian hiệu lực của access token (tính bằng giây).
- `refresh_token`: Mã làm mới token.
- `refresh_token_expires_in`: Thời gian hiệu lực của refresh token (giây).
- `open_id`: Mã định danh duy nhất của người dùng tài khoản TikTok đối với ứng dụng.

### Bước 4: Làm mới mã truy cập (Renew access token)
Gọi endpoint **/tt_user/oauth2/refresh_token/**. Sử dụng `refresh_token` nhận được từ Bước 3 để đổi lấy một `access_token` mới.

#### Ví dụ lệnh cURL (Example)
```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/tt_user/oauth2/refresh_token/' --header 'Content-Type: application/json' --data-raw '{
 "grant_type" : "refresh_token",
 "refresh_token" : "YOUR_REFRESH_TOKEN",
 "client_secret": "YOUR_CLIENT_SECRET",
 "client_id": "YOUR_CLIENT_ID"
}'
```

### Bước 5: [Tùy chọn] Thu hồi mã truy cập (Revoke access token)
Nếu muốn chủ động thu hồi mã truy cập, hãy gọi endpoint [/tt_user/oauth2/revoke/](../12-api-reference/68-tiktok-one-p1.md#doc-1768493902119937).

#### Ví dụ lệnh cURL (Example)
```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/tt_user/oauth2/revoke/' --header 'Content-Type: application/json' --data '{
    "client_id": "YOUR_CLIENT_ID",
    "client_secret": "YOUR_CLIENT_SECRET",
    "access_token": "YOUR_ACCESS_TOKEN"
}'
```

---

<a id="doc-1763404664004609"></a>
<!-- doc_id: 1763404664004609 -->
<!-- doc_id: 1763404664004609 -->
# Lấy thông tin phân tích chi tiết của Creator (Get Creator insights)
> Đường dẫn: Organic API > TikTok One API > Guides > Get Creator insights
Các endpoint sau đây hỗ trợ truy xuất thông tin chi tiết về nhà sáng tạo trong hệ thống TikTok One (TTO) Creator Marketplace:

## Tìm kiếm và khám phá (Search and Discovery)
- [Khám phá Creator TTO (Discover TTO Creators)](../12-api-reference/68-tiktok-one-p1.md#doc-1825017307843585): Sử dụng endpoint này để tìm kiếm các nhà sáng tạo dựa trên các tiêu chí lọc cụ thể (ngành hàng, người theo dõi, tương tác,...).

## Thông tin phân tích có ủy quyền (Authorized Insights)
- [Lấy thông tin tài khoản TTO được ủy quyền (Get Authorized TTO Account Insights)](../12-api-reference/68-tiktok-one-p1.md#doc-1834913529338882): Sử dụng endpoint này để lấy các chỉ số phân tích chuyên sâu cấp tài khoản (Account Level insights) của nhà sáng tạo đã cấp quyền.
- [Lấy thông tin video TTO được ủy quyền (Get Authorized TTO Media Insights)](../12-api-reference/68-tiktok-one-p1.md#doc-1834913554657282): Sử dụng endpoint này để lấy các chỉ số phân tích chi tiết cấp video (Video Level insights) của nhà sáng tạo đã cấp quyền.

## Thông tin phân tích công khai (Public Insights)
- [Lấy thông tin tài khoản công khai TTO (Get TTO Public Account Insights)](../12-api-reference/68-tiktok-one-p1.md#doc-1828185358712897): Sử dụng endpoint này để lấy thông tin hồ sơ cơ bản công khai của một nhà sáng tạo trên TTO Creator Marketplace.
- [Lấy thông tin video công khai TTO (Get TTO Public Media Insights)](../12-api-reference/68-tiktok-one-p1.md#doc-1828185411810305): Sử dụng endpoint này để lấy thông tin công khai về các video của nhà sáng tạo trên TTO Creator Marketplace.

---

<a id="doc-1830337139853313"></a>
<!-- doc_id: 1830337139853313 -->
<!-- doc_id: 1830337139853313 -->
# Liên kết nội dung TTO Creator Marketplace (Content Linking)
> Đường dẫn: Organic API > TikTok One API > Guides > TTO Creator Marketplace Content Linking
Liên kết nội dung (Content Linking) là một tính năng mạnh mẽ của TikTok One (TTO) API được thiết kế nhằm tối ưu hóa việc theo dõi hiệu suất cho các video tự nhiên (organic) của nhà sáng tạo trên TikTok. Tính năng này giúp tinh gọn việc giao tiếp giữa nhà quảng cáo và nhà sáng tạo thông qua nền tảng sáng tạo chính thức của TikTok. Bằng cách sử dụng Content Linking, nhà quảng cáo có thể truy cập các báo cáo phân tích nâng cao, nhận ủy quyền chạy Spark Ads và khai phóng nhiều lợi ích khác nhằm tối đa hóa tác động của nội dung tự nhiên.

## Các loại liên kết nội dung (Types of Content Links)
Hai hình thức liên kết nội dung chính bao gồm **liên kết mời (invite links)** và **yêu cầu liên kết (linking requests)**. Mỗi hình thức phục vụ các mục đích riêng biệt và mang lại lợi ích cụ thể cho nhà quảng cáo cũng như nhà sáng tạo.

### Liên kết mời (Invite links)
Liên kết mời là các URL mà nhà sáng tạo sử dụng để liên kết nội dung mới tạo, tải lên bản nháp hoặc liên kết các video sẵn có trực tiếp trong ứng dụng TikTok. Thương hiệu hoặc đối tác có thể gửi liên kết này trực tiếp qua email, tin nhắn,... Rất phù hợp cho cả nhu cầu liên kết trước khi đăng tải hoặc liên kết hồi tố.

Chiến dịch TTO Creator Marketplace hỗ trợ cấu hình liên kết mời ở hai cấp độ: cấp chiến dịch (campaign-level) hoặc cấp thương hiệu (brand-level).

#### Liên kết mời cấp chiến dịch (Campaign-level invite link)
Cấu hình liên kết mời ở cấp chiến dịch để liên kết các video với một chiến dịch cụ thể. Cấu hình này rất lý tưởng cho các chiến dịch có khung thời gian xác định hoặc theo sự kiện cần theo dõi và báo cáo rõ ràng.

- **Giới hạn**:
  - Bạn có thể mời tối đa 500 nhà sáng tạo vào một chiến dịch duy nhất bằng liên kết mời cấp chiến dịch.
  - Một nhà sáng tạo có thể tải video lên cùng một liên kết mời cấp chiến dịch tối đa 500 lần (tính cả video đã tải lên và video đã xóa).
  - Một liên kết mời cấp chiến dịch có thể lưu trữ tối đa 250.000 video từ tất cả các nhà sáng tạo được mời.
- **Tình huống sử dụng thực tế**:
  - Các chương trình khuyến mãi theo mùa (ví dụ: Black Friday).
  - Sự kiện ra mắt sản phẩm mới với khung thời gian cố định.

Để tạo chiến dịch sử dụng liên kết mời cấp chiến dịch, hãy gọi [/tto/tcm/campaign/create/](../12-api-reference/68-tiktok-one-p1.md#doc-1815693549459458) và đặt `campaign_type` là `CAMPAIGN` hoặc để trống tham số `campaign_type`.

#### Liên kết mời cấp thương hiệu (Brand-level invite link)
Cấu hình liên kết mời ở cấp thương hiệu để liên kết video liên tục và lâu dài với tài khoản thương hiệu của bạn. Đây là lựa chọn hoàn hảo cho việc tổng hợp nội dung dài hạn (evergreen).

- **Giới hạn**:
  - Không giới hạn số lượng nhà sáng tạo có thể mời vào chiến dịch qua liên kết mời cấp thương hiệu.
  - Một nhà sáng tạo có thể tải lên số lượng video không giới hạn qua cùng một liên kết mời cấp thương hiệu.
  - Không giới hạn tổng số lượng video được lưu trữ.
- **Tình huống sử dụng thực tế**:
  - Xây dựng thư viện nội dung do người dùng tạo (UGC) cho thương hiệu.
  - Hợp tác tiếp thị người ảnh hưởng dài hạn.

Để tạo chiến dịch sử dụng liên kết mời cấp thương hiệu, hãy gọi [/tto/tcm/campaign/create/](../12-api-reference/68-tiktok-one-p1.md#doc-1815693549459458) và đặt `campaign_type` là `BRAND_LINK`.

### Bảng so sánh giữa hai loại liên kết mời

Bảng dưới đây so sánh liên kết mời cấp chiến dịch và liên kết mời cấp thương hiệu giúp bạn chọn giải pháp phù hợp nhất:

| Feature | Liên kết mời cấp chiến dịch | Liên kết mời cấp thương hiệu |
|---|---|---|
| Creator limit | Tối đa 500 nhà sáng tạo | Không giới hạn |
| Video limit per Creator | 500 video (bao gồm cả video đã xóa) | Không giới hạn |
| Total video limit | 250.000 video trên tất cả nhà sáng tạo | Không giới hạn |
| Best for | Chiến dịch có thời hạn cụ thể | Quảng bá thương hiệu dài hạn (Evergreen) |

### Yêu cầu liên kết (Linking requests)
Yêu cầu liên kết là các thông báo trong ứng dụng được gửi trực tiếp vào hộp thư của nhà sáng tạo, nhắc họ gắn thẻ cho video của mình. Các thông báo này được hiển thị dưới dạng push notification trong ứng dụng và chỉ áp dụng cho việc liên kết hồi tố các video đã đăng.

Để gửi yêu cầu liên kết, hãy sử dụng endpoint [/tto/tcm/campaign/link/](../12-api-reference/68-tiktok-one-p1.md#doc-1824449956282370) với các tham số tương ứng theo nhu cầu:
- Để gắn thẻ video với thương hiệu:
  - Đặt tham số `action` thành `LINK`.
  - Chỉ định chiến dịch có liên kết mời cấp thương hiệu thông qua tham số `campaign_id`.
- Để gắn thẻ video với chiến dịch:
  - Đặt tham số `action` thành `LINK`.
  - Chỉ định chiến dịch có liên kết mời cấp chiến dịch thông qua tham số `campaign_id`.

---

<a id="doc-1828929329184770"></a>
<!-- doc_id: 1828929329184770 -->
<!-- doc_id: 1828929329184770 -->
# Tạo và quản lý chiến dịch TTO Creator Marketplace
> Đường dẫn: Organic API > TikTok One API > Guides > Create and manage a TTO Creator Marketplace campaign
Tài liệu này hướng dẫn cách tạo và quản lý các chiến dịch TikTok One (TTO) Creator Marketplace thông qua API.

Để khởi tạo chiến dịch qua API, tất cả các Đối tác API phải sử dụng tài khoản TTO của chính mình. Nếu có bất kỳ thắc mắc nào, hãy liên hệ với Quản lý đối tác TikTok của bạn.

## Các bước thực hiện
### 1. Tạo chiến dịch TTO Creator Marketplace
Sau khi xác định danh sách nhà sáng tạo bạn muốn mời tham gia chiến dịch, hãy gọi endpoint [/tto/tcm/campaign/create/](../12-api-reference/68-tiktok-one-p1.md#doc-1815693549459458) để tạo chiến dịch cho các nhà sáng tạo.

Bạn có thể tạo chiến dịch kèm theo một trong các loại liên kết mời sau:
- [Liên kết mời cấp chiến dịch](tiktok-one-api.md#doc-1830337139853313) để gắn kết video với một chiến dịch cụ thể.
- [Liên kết mời cấp thương hiệu](tiktok-one-api.md#doc-1830337139853313) để gắn kết video với tài khoản thương hiệu của bạn.

> **Lưu ý:**
> - Nếu bạn truyền tham số `default_spark_ads_requested_authorization_days`, cài đặt số ngày ủy quyền này sẽ tự động áp dụng cho tất cả các video được tải lên thông qua liên kết mời.

### 2. Chia sẻ liên kết mời cấp chiến dịch hoặc cấp thương hiệu với nhà sáng tạo
Nhà sáng tạo phải sử dụng liên kết mời cấp chiến dịch hoặc cấp thương hiệu khi tải video lên TikTok. Sau khi video được liên kết thành công, hệ thống sẽ bắt đầu ghi nhận và xuất báo cáo hiệu suất.

### 3. Truy xuất thông tin chiến dịch
Sau khi tạo chiến dịch TTO Creator Marketplace, nhà phát triển có thể sử dụng endpoint [/tto/tcm/campaign/](../12-api-reference/68-tiktok-one-p1.md#doc-1815693562720258) để truy xuất thông tin chi tiết của chiến dịch. Khi video đã được liên kết với chiến dịch, endpoint `/tto/tcm/campaign/` sẽ trả về `video_id` tương ứng.

### 4. Truy cập báo cáo hiệu suất
Sau khi video được tải lên và liên kết với chiến dịch TTO Creator Marketplace, hãy sử dụng endpoint [/tto/tcm/report/](../12-api-reference/68-tiktok-one-p2.md#doc-1815693573340162) để lấy dữ liệu phân tích hiệu suất của video.

---

<a id="doc-1740027794580481"></a>
<!-- doc_id: 1740027794580481 -->
<!-- doc_id: 1740027794580481 -->
# Lấy ủy quyền Spark Ads (Get Spark Ads authorization)
> Đường dẫn: Organic API > TikTok One API > Guides > Get Sparks Ads authorization
Tài liệu này hướng dẫn cách sử dụng TikTok One (TTO) API để yêu cầu ủy quyền chạy Spark Ads đối với bài đăng của nhà sáng tạo.

## Các bước thực hiện
1. Nhà quảng cáo yêu cầu ủy quyền Spark Ads trong lúc tạo chiến dịch hoặc sau khi chiến dịch đã tạo.
2. Nhà quảng cáo sử dụng endpoint [/tcm/tt_video/status/](../12-api-reference/68-tiktok-one-p2.md#doc-1751098935842817) để kiểm tra trạng thái phê duyệt và lấy mã ủy quyền (`auth_code`).
3. Nhà quảng cáo sử dụng endpoint [/tt_video/authorize/](../12-api-reference/64-spark-ads-using-authorized-posts.md#doc-1738376435339265) để thêm video vào tài khoản nhà quảng cáo.
4. Nhà quảng cáo sử dụng endpoint [/tt_video/info/](../12-api-reference/64-spark-ads-using-authorized-posts.md#doc-1738376324021250) để lấy thông tin chi tiết của video và trạng thái ủy quyền của bài đăng Spark Ads.

### Bước 1: Yêu cầu ủy quyền
#### Cách 1: Trong khi tạo chiến dịch
Khi tạo chiến dịch TTO Creator Marketplace bằng [/tto/tcm/campaign/create/](../12-api-reference/68-tiktok-one-p1.md#doc-1815693549459458), hãy truyền tham số `default_spark_ads_requested_authorization_days` để yêu cầu số ngày ủy quyền Spark Ads cho toàn bộ video được tải lên chiến dịch. Khi nhà sáng tạo tham gia và đăng tải video vào chiến dịch, bạn sẽ tự động được cấp quyền Spark Ads cho các video đó.

#### Cách 2: Sau khi tạo chiến dịch
Sau khi nhà sáng tạo đã đăng video, hãy gọi endpoint [/tcm/tt_video/apply/](../12-api-reference/68-tiktok-one-p2.md#doc-1751098904942594) để gửi yêu cầu ủy quyền. Khi gọi endpoint này, một thông báo sẽ được gửi trực tiếp đến ứng dụng của nhà sáng tạo để yêu cầu họ xác nhận cấp quyền.

### Bước 2: Lấy mã ủy quyền (auth_code)
Để xác nhận trạng thái của yêu cầu ủy quyền, hãy gọi endpoint [/tcm/tt_video/status/](../12-api-reference/68-tiktok-one-p2.md#doc-1751098935842817). Sau khi nhà sáng tạo chấp thuận yêu cầu, giá trị `auth_code` sẽ được trả về trong phản hồi API.

### Bước 3: Ủy quyền tài khoản quảng cáo để tạo Spark Ads
Gọi endpoint [/tt_video/authorize/](../12-api-reference/64-spark-ads-using-authorized-posts.md#doc-1738376435339265) và truyền vào `auth_code` để cấp quyền cho tài khoản quảng cáo sử dụng video đó làm tư liệu quảng cáo Spark Ads.

### Bước 4: Lấy thông tin video và dữ liệu ủy quyền
Nhà phát triển có thể sử dụng endpoint [/tt_video/info/](../12-api-reference/64-spark-ads-using-authorized-posts.md#doc-1738376324021250) để kiểm tra trạng thái ủy quyền của video trong tài khoản quảng cáo. Dữ liệu phản hồi bao gồm thông tin chi tiết về video cũng như thời gian bắt đầu và kết thúc của quyền ủy quyền.

## Các bước tiếp theo
Bạn có thể lấy giá trị `item_id` nhận được từ Bước 4 và truyền vào tham số `tiktok_item_id` trong endpoint [/smart_plus/ad/create/](../12-api-reference/62-upgraded-smartplus-p5.md#doc-1843317390059522) để tiến hành tạo mẫu quảng cáo.

Để xem hướng dẫn chi tiết từng bước về cách tạo Spark Ads, vui lòng tham khảo [tại đây](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1739470744631298).

---

<a id="doc-1825117901366274"></a>
<!-- doc_id: 1825117901366274 -->
<!-- doc_id: 1825117901366274 -->
# Giới hạn tần suất gọi cho TTO API (Rate limits for TTO API)
> Đường dẫn: Organic API > TikTok One API > Guides > Rate limits for TTO API

## Tổng quan
Nhằm hỗ trợ sự phát triển bền vững của hệ sinh thái nhà sáng tạo TikTok và đảm bảo hiệu năng tối ưu của hệ thống, chúng tôi áp dụng những cập nhật quan trọng về giới hạn tần suất gọi API (rate limits) cho TikTok One API (TTO API). Những điều chỉnh này được thiết kế nhằm phân bổ tài nguyên công bằng và đem lại trải nghiệm ổn định, chất lượng cao cho toàn bộ nhà sáng tạo, thương hiệu và đối tác.

## Giới hạn tần suất gọi đặc thù của TTO API
Ngày có hiệu lực: 26 tháng 9 năm 2025, 00:00 (GMT+0)

**Các giới hạn tốc độ đặc thù áp dụng cho danh sách các endpoint TTO API sau:**

| Endpoint | Gói Cơ bản (Basic) - QPS | QPM | QPD | Gói Nâng cao (Advanced) - QPS | QPM | QPD | Gói Cao cấp (Premium) - QPS | QPM | QPD |
|---|---|---|---|---|---|---|---|---|---|
| [/tto/creator/authorized/](../12-api-reference/68-tiktok-one-p1.md#doc-1834913529338882) | 10 | 20 | 50 | 20 | 1,200 | 10,000 | 30 | 1,800 | 300,000 |
| [/tto/creator/authorized/video/list/](../12-api-reference/68-tiktok-one-p1.md#doc-1834913554657282) | 10 | 20 | 50 | 20 | 1,200 | 10,000 | 30 | 1,800 | 300,000 |
| [/tto/tcm/creator/public/](../12-api-reference/68-tiktok-one-p1.md#doc-1828185358712897) | 10 | 20 | 50 | 20 | 1,200 | 10,000 | 30 | 1,800 | 150,000 |
| [/tto/tcm/creator/public/video/list/](../12-api-reference/68-tiktok-one-p1.md#doc-1828185411810305) | 10 | 20 | 50 | 20 | 1,200 | 10,000 | 30 | 1,800 | 500,000 |
| [/tto/tcm/rank/](../12-api-reference/68-tiktok-one-p1.md#doc-1816378813274113) | 10 | 20 | 50 | 20 | 1,200 | 10,000 | 30 | 1,800 | 150,000 |
| [/tto/tcm/creator/discover/](../12-api-reference/68-tiktok-one-p1.md#doc-1825017307843585) | 10 | 20 | 50 | 20 | 1,200 | 10,000 | 30 | 1,800 | 100,000 |

> **Lưu ý:**
> Giới hạn tốc độ toàn cục (Global rate limits) sẽ áp dụng cho các endpoint TTO API khác không nằm trong danh sách trên. Để tìm hiểu thêm về giới hạn tần suất toàn cục cho ứng dụng nhà phát triển, vui lòng tham khảo [Giới hạn tần suất gọi - Toàn cục](../04-get-started/bat-dau.md#doc-1740029171730433).

**Các cấp hạn mức tốc độ gọi:**
- **Cấp độ Cơ bản (Basic Level)**: Mọi ứng dụng nhà phát triển mặc định áp dụng giới hạn ở cấp Basic.
- **Cấp độ Nâng cao (Advanced Level)**: Nhà phát triển có thể đạt điều kiện lên cấp Advanced nếu trong một quý dương lịch, họ quản lý ít nhất 300 bài đăng nội dung thương hiệu được liên kết với bất kỳ Chiến dịch TikTok One nào được tạo thông qua endpoint [/tto/tcm/campaign/create/](../12-api-reference/68-tiktok-one-p1.md#doc-1815693549459458).
- **Cấp độ Cao cấp (Premium Level)**: Nhà phát triển có thể đạt điều kiện lên cấp Premium nếu trong một quý dương lịch, họ đáp ứng đủ số lượng bài đăng nội dung thương hiệu liên kết với chiến dịch TikTok One tạo qua [/tto/tcm/campaign/create/](../12-api-reference/68-tiktok-one-p1.md#doc-1815693549459458). Đối với các nhà phát triển không cung cấp phần mềm dạng dịch vụ (non-SaaS), ngưỡng yêu cầu là 1.000 bài đăng; đối với nhà phát triển dạng SaaS, ngưỡng cụ thể sẽ do đội ngũ Vận hành Sáng tạo của TikTok (TikTok Creative Operations) chỉ định.

> **Lưu ý:**
> Việc nâng hạn mức gọi phụ thuộc vào sự đánh giá và phê duyệt từ đội ngũ Vận hành Sáng tạo TikTok. Những nhà phát triển không tuân thủ các tiêu chuẩn bắt buộc hoặc lạm dụng API có thể bị hạ cấp xuống Advanced hoặc Basic.

## Đăng ký nâng hạn mức giới hạn tốc độ TTO API
- **Nhà phát triển được quản lý (Managed Developers)**: Nếu bạn là Đối tác Sáng tạo (Creative Partner) hoặc nhà phát triển có quản lý tài khoản riêng, vui lòng liên hệ trực tiếp với đại diện TikTok phụ trách của bạn để kết nối với đội ngũ TikTok Creative Operations.
- **Nhà phát triển tự phục vụ (Self-Serve Developers)**: Nếu bạn là nhà phát triển tự phục vụ và đáp ứng các tiêu chí của cấp Advanced hoặc Premium, bạn có thể nộp [Đơn đăng ký nâng hạn mức TTO API](https://bytedance.sg.larkoffice.com/share/base/form/shrlgphNGDoW1eLAEE8EP0pNwWh). Đội ngũ TikTok Creative Operations sẽ xem xét và phản hồi các bước tiếp theo. Nếu đơn đăng ký không được chấp thuận, ứng dụng của bạn sẽ tiếp tục áp dụng mức giới hạn Basic.

---

<a id="doc-1740302141934593"></a>
<!-- doc_id: 1740302141934593 -->
<!-- doc_id: 1740302141934593 -->
# Danh mục API tham chiếu (API reference)
> Đường dẫn: Organic API > TikTok One API > API reference
Nhóm này bao gồm các danh mục endpoint sau:

## Xác thực và ủy quyền (Authentication)
* [Lấy, làm mới hoặc thu hồi token truy cập của Creator](../12-api-reference/68-tiktok-one-p1.md#doc-1768493902119937)
* [Lấy danh sách các quyền hạn Creator đã ủy quyền](../12-api-reference/68-tiktok-one-p1.md#doc-1765926674648065)
* [Lấy danh sách tài khoản TTO Creator Marketplace được ủy quyền](../12-api-reference/68-tiktok-one-p1.md#doc-1815693478150146)
* [Kiểm tra trạng thái Creator TTO](../12-api-reference/68-tiktok-one-p1.md#doc-1837799887531010)
* [Lấy thông tin chi tiết tài khoản TTO Creator Marketplace](../12-api-reference/68-tiktok-one-p1.md#doc-1831975745134593)

## Khám phá và phân tích Creator (Creator insights and discovery)
* [Lấy thông tin tài khoản công khai TTO](../12-api-reference/68-tiktok-one-p1.md#doc-1828185358712897)
* [Lấy thông tin video công khai TTO](../12-api-reference/68-tiktok-one-p1.md#doc-1828185411810305)
* [Lấy thông tin phân tích Creator TTO được ủy quyền](../12-api-reference/68-tiktok-one-p1.md#doc-1834913529338882)
* [Lấy thông tin phân tích video TTO được ủy quyền](../12-api-reference/68-tiktok-one-p1.md#doc-1834913554657282)
* [Lấy nhãn xếp hạng hoặc nhãn tìm kiếm Creator TTO](../12-api-reference/68-tiktok-one-p1.md#doc-1816372654109698)
* [Lấy bảng xếp hạng Creator TTO hàng đầu](../12-api-reference/68-tiktok-one-p1.md#doc-1816378813274113)
* [Khám phá Creator TTO](../12-api-reference/68-tiktok-one-p1.md#doc-1825017307843585)

## Quản lý chiến dịch TTO (TTO campaign management)
* [Tạo hồ sơ thương hiệu (Brand Profile) cho tài khoản TTO](../12-api-reference/68-tiktok-one-p1.md#doc-1830335387914241)
* [Lấy danh sách hồ sơ thương hiệu cho tài khoản TTO](../12-api-reference/68-tiktok-one-p1.md#doc-1830335437705217)
* [Tạo hoặc cập nhật chiến dịch TTO Creator Marketplace](../12-api-reference/68-tiktok-one-p1.md#doc-1815693549459458)
* [Cập nhật chiến dịch TTO Creator Marketplace](../12-api-reference/68-tiktok-one-p1.md#doc-1830338948169794)
* [Lấy danh sách chiến dịch TTO Creator Marketplace](../12-api-reference/68-tiktok-one-p1.md#doc-1815693562720258)
* [Gửi hoặc thu hồi yêu cầu liên kết video TTO](../12-api-reference/68-tiktok-one-p1.md#doc-1824449956282370)
* [Lấy danh sách yêu cầu liên kết video TTO dưới vai trò thương hiệu](../12-api-reference/68-tiktok-one-p1.md#doc-1824450033584129)
* [Báo cáo phân tích video TTO Creator Marketplace](../12-api-reference/68-tiktok-one-p2.md#doc-1815693573340162)
* [Đăng ký nhận sự kiện liên kết video TikTok với chiến dịch TTO](../08-use-cases/use-case-webhook.md#doc-1810521739537409)

## Ủy quyền Spark Ads (Spark Ads Authorization)
* [Đăng ký yêu cầu ủy quyền Spark Ads](../12-api-reference/68-tiktok-one-p2.md#doc-1751098904942594)
* [Lấy trạng thái ủy quyền Spark Ads](../12-api-reference/68-tiktok-one-p2.md#doc-1751098935842817)

## Quản lý neo TTO (TTO anchor management)
* [Tạo điểm neo trang web (webpage anchor)](../12-api-reference/68-tiktok-one-p2.md#doc-1826564934723585)
* [Lấy danh sách điểm neo trang web](../12-api-reference/68-tiktok-one-p2.md#doc-1826564965840066)
* [Xóa điểm neo bản nháp](../12-api-reference/68-tiktok-one-p2.md#doc-1826564985760770)

## Quản lý Creator TTO (TTO creator management)
* [Tham gia chiến dịch TTO Creator Marketplace dưới vai trò Creator](../12-api-reference/68-tiktok-one-p2.md#doc-1836584318657537)
* [Liên kết video vào chiến dịch TTO Creator Marketplace dưới vai trò Creator](../12-api-reference/68-tiktok-one-p2.md#doc-1836584551347201)
* [Lấy danh sách yêu cầu liên kết video TTO dưới vai trò Creator](../12-api-reference/68-tiktok-one-p2.md#doc-1837247726007298)
* [Phê duyệt hoặc từ chối yêu cầu liên kết video TTO dưới vai trò Creator](../12-api-reference/68-tiktok-one-p2.md#doc-1837247744649345)

---

## Hướng dẫn thực hành Data Retrieval (Python & cURL)

Dưới đây là mã nguồn mẫu minh họa quy trình gọi API thực tế cho phân hệ **Organic API — TikTok One API**:

### cURL mẫu
```bash
curl -s -X GET "https://business-api.tiktok.com/open_api/v1.3/example/get/?advertiser_id=YOUR_ADVERTISER_ID"   -H "Access-Token: YOUR_ACCESS_TOKEN"
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
