# Bắt đầu: Khái niệm, quy trình, rate limit, sandbox

Chào mừng bạn đến với TikTok For Business Developers! Bộ tài liệu này hướng dẫn chi tiết các bước cần thiết để bạn bắt đầu tích hợp với TikTok API for Business, hiểu rõ cấu trúc tài khoản, quản lý ủy quyền và xác thực, nắm vững các giới hạn tốc độ gọi (rate limits) cũng như cách sử dụng môi trường sandbox để kiểm thử trước khi đưa vào sản xuất.

---

## Bắt đầu (`Get Started`)
<a id="doc-1735713609895937"></a>
<!-- doc_id: 1735713609895937 -->

> Đường dẫn: Get Started

Chào mừng bạn đến với TikTok For Business Developers! Được thiết kế tối ưu cho các nhà phát triển, chúng tôi giúp việc tiếp cận và sử dụng API For Business trở nên vô cùng dễ dàng. Bạn chỉ cần thực hiện vài bước đơn giản để có quyền truy cập và bắt đầu quản lý quảng cáo. **Dưới đây là các bước cần thực hiện trước khi thực hiện lệnh gọi API đầu tiên cùng các tài nguyên hữu ích giúp bạn nhanh chóng tích hợp với TikTok API for Business.**

### Quy trình từng bước (`Step-by-step workflow`)

> [!NOTE]
> Các bước cụ thể cần thiết cho [ủy quyền](bat-dau.md#doc-1781891256601602) và [xác thực](bat-dau.md#doc-1781892384100354) sẽ thay đổi tùy thuộc vào loại API bạn đang sử dụng.

1. [Tạo tài khoản TikTok For Business](bat-dau.md#doc-1738855099573250).
2. [Đăng ký trở thành nhà phát triển](bat-dau.md#doc-1738855176671234).
3. [Tạo ứng dụng nhà phát triển](bat-dau.md#doc-1738855242728450).
4. [Ủy quyền](bat-dau.md#doc-1781891256601602).
5. [Xác thực](bat-dau.md#doc-1781892384100354).
6. Thực hiện lệnh gọi API đầu tiên: Bạn có thể sử dụng [bộ sưu tập Postman của TikTok API for Business](https://www.postman.com/tiktok/workspace/tiktok-api-for-business/folder/23207567-9c73b718-e802-40f0-a70d-db8524ed2494) để dễ dàng **kiểm thử** tích hợp mà không ảnh hưởng đến tài khoản TikTok for Business thực tế của bạn.

> [!NOTE]
> Bạn có thể sử dụng các endpoint API hoặc SDK để thực hiện các lệnh gọi đầu tiên. Xem [SDK](../16-sdk/sdk.md#doc-1764231376750658) để biết thêm chi tiết.

### Các endpoint API (`API endpoints`)
Để tìm hiểu về tất cả các endpoint hiện có, hãy xem **Tài liệu tham khảo API**.

### SDK
Để tìm hiểu về SDK, hãy xem [SDK](../16-sdk/sdk.md#doc-1764231376750658). Để tìm mã nguồn SDK, hãy xem liên kết [GitHub này](https://github.com/tiktok/tiktok-business-api-sdk).

### Giới hạn tốc độ gọi (`Rate limits`)
Để tìm hiểu về giới hạn tốc độ gọi toàn cục và theo từng endpoint cụ thể, xem [tại đây](bat-dau.md#doc-1740029171730433).

### Cập nhật quyền ứng dụng (`Update app permissions`)
Để tìm hiểu cách cập nhật quyền cho ứng dụng nhà phát triển của bạn, xem [tại đây](bat-dau.md#doc-1738855280338946).

### Bộ sưu tập Postman (`Postman collection`)
Để tìm hiểu về bộ sưu tập Postman cho các endpoint API của chúng tôi, xem [tại đây](bat-dau.md#doc-1747849403155521).

### Tài khoản Sandbox (`Sandbox accounts`)
Để kiểm thử tích hợp mà không làm ảnh hưởng đến tài khoản TikTok For Business thực tế, xem [tại đây](bat-dau.md#doc-1738855331457026).

### Các khái niệm (`Concepts`)
Để tìm hiểu về các khái niệm phổ biến dùng trong tài liệu TikTok API For Business, xem [tại đây](bat-dau.md#doc-1738928364967937).

### Cấu trúc tài khoản (`Account structure`)
Để tìm hiểu về cấu trúc tài khoản cũng như mối quan hệ giữa tài khoản quảng cáo và tài khoản nhà phát triển, xem [tại đây](bat-dau.md#doc-1740029179343874).

### Thời gian tích hợp ước tính (`Estimated Integration time`)
Để tìm hiểu về thời gian tích hợp ước tính cho một số trường hợp sử dụng API phổ biến, xem **tại đây**.

### Mã lỗi (`Error codes`)
Để tìm hiểu về mã phản hồi cho các lệnh gọi không thành công, xem [tại đây](../15-appendix/phu-luc-p1.md#doc-1737172488964097).

---

## Các khái niệm (`Concepts`)
<a id="doc-1738928364967937"></a>
<!-- doc_id: 1738928364967937 -->

> Đường dẫn: Get Started > Concepts

Bài viết này giải thích các khái niệm được sử dụng xuyên suốt API For Business.

### Nền tảng (`Platform`)

| Concepts | Định nghĩa |
|---|---|
| TikTok for Business | TikTok for Business là một nền tảng toàn cầu cung cấp các sản phẩm và giải pháp giúp các thương hiệu thuộc mọi quy mô thúc đẩy tác động kinh doanh. Truy cập [trang web](https://www.tiktok.com/business/en-US) để tìm hiểu thêm. |
| TikTok Creator Marketplace | TikTok Creator Marketplace (TTCM) là nền tảng cho phép các nền tảng influencer và công ty đại diện (agency) đẩy mạnh sự phát triển của cơ hội hợp tác sáng tạo và nội dung có thương hiệu trên TikTok. Truy cập [trang web](https://creatormarketplace.tiktok.com/ad#/dashboard) để tìm hiểu thêm. |
| TikTok Ads Manager | TikTok Ads Manager (Trình quản lý quảng cáo TikTok) là nền tảng quảng cáo nơi các nhà quảng cáo có thể tạo và quản lý các chiến dịch quảng cáo TikTok cùng nội dung sáng tạo quảng cáo, cũng như xem và phân tích các báo cáo hiệu quả quảng cáo. Truy cập [trang web](https://ads.tiktok.com/i18n/login/?redirect=https%3A%2F%2Fads.tiktok.com%2Fi18n%2Fdashboard%3Faadvid%3D72391499277%26is_new_connect%3D0%26is_new_user%3D0) để tìm hiểu thêm. |
| TikTok Business Center | TikTok Business Center là trung tâm kinh doanh một điểm dừng (one-stop hub) cho phép các tổ chức tập trung quản lý tài sản, phân bổ quyền hạn, đồng thời cho phép nhà quảng cáo quản lý nhiều tài khoản quảng cáo TikTok giữa nhiều người dùng một cách an toàn và hiệu quả. Truy cập [trang web](https://business.tiktok.com/) để tìm hiểu thêm. |
| TikTok Business Account | TikTok Business Account (Tài khoản doanh nghiệp TikTok) là loại tài khoản TikTok đặc thù dành cho các doanh nghiệp trên TikTok. Tài khoản cung cấp bộ tính năng mở rộng phục vụ nhu cầu quảng bá và thương mại. Truy cập [trang web](https://www.tiktok.com/business/en/solutions/business-account) để tìm hiểu thêm. |
| TikTok Personal Account | TikTok Personal Account (Tài khoản cá nhân TikTok) là loại tài khoản TikTok dành cho người dùng thông thường trên TikTok. |

### Nền tảng API (`API Platform`)

| Concepts | Định nghĩa |
|---|---|
| TikTok API for Business | TikTok API for Business là chuỗi dịch vụ giao diện được TikTok for Business cung cấp cho các nhà phát triển. Thông qua tích hợp và gọi giao diện TikTok API for Business, nhà phát triển có thể tận dụng giao diện này để tương tác với các tính năng của TikTok Ads Manager, TikTok Business Center và TikTok Creator Marketplace. Các công ty công nghệ (Technology Company), nhà quảng cáo trực tiếp (Direct Advertiser) và Agency đều có thể tận dụng TikTok API for Business để tạo và quản lý chiến dịch. |
| TikTok for Developers | TikTok for Developers cung cấp công cụ cho nhà sáng tạo và nhà nghiên cứu. Nền tảng này cung cấp các tính năng bao gồm Login Kit, Video Kit, Embeded Videos và Greenscreen Kit. Truy cập [https://developers.tiktok.com/](https://developers.tiktok.com/) để tìm hiểu thêm. |

### Ủy quyền (`Authorization`)

| Concepts | Định nghĩa |
|---|---|
| app_id | Định danh ứng dụng (Application identifier) được sử dụng khi thực hiện các lệnh gọi API. Để lấy `app_id`, hãy làm theo hướng dẫn trong [Bắt đầu - Tạo ứng dụng nhà phát triển](bat-dau.md#doc-1738855242728450). |
| secret | Mỗi ứng dụng có một khóa bí mật (secret key) duy nhất. Cặp `app_id` và `secret` nhận được cùng lúc khi ứng dụng của bạn được phê duyệt. |
| callback address | Mỗi ứng dụng có một địa chỉ callback (địa chỉ gọi lại) được kích hoạt khi ủy quyền hoàn tất thành công. Sau khi ứng dụng được ủy quyền thành công, địa chỉ callback sẽ được tải và mã ủy quyền `auth_code` cùng `state` sẽ xuất hiện trên URL.<br>**Lưu ý**: Hãy đảm bảo địa chỉ callback có thể nhận thông tin callback từ Internet thành công. Ví dụ về URL ủy quyền: `https://ads.tiktok.com/marketing_api/auth?app_id=XXX&state=xxx&scope=xxx&redirect_uri=Callback_address`. |
| scope | Phạm vi quyền hạn ủy quyền. Nếu scope không được xác định rõ trong URL ủy quyền, tất cả các quyền trong ứng dụng hiện tại sẽ được cấp khi hoàn tất ủy quyền. |
| redirect URL | Dùng để truyền địa chỉ callback khi thiết lập URL ủy quyền. Tham số này xuất hiện dưới dạng `redirect_url` trong URL ủy quyền. Giá trị phải hoàn toàn giống với địa chỉ callback. |
| auth_code | Sau khi ủy quyền thành công, nhà phát triển sẽ nhận được mã ủy quyền `auth_code` thông qua địa chỉ callback. Mã này có thể dùng để [Tạo access token](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162).<br>**Lưu ý**: `auth_code` chỉ có hiệu lực trong 1 giờ và chỉ dùng được một lần duy nhất. |
| access token | Access token (mã truy cập) là thông tin xác thực đã được ủy quyền để truy cập giao diện API. Máy chủ sử dụng mã này để xác thực các yêu cầu API. Bạn có thể lấy token qua endpoint [Tạo access token](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| core_user_id | ID người dùng TikTok for Business của nhà phát triển ứng dụng. Bạn có thể lấy ID này qua endpoint **/user/info/**. |

### Chiến dịch (`Campaign`)

| Concepts | Định nghĩa |
|---|---|
| advertiser_id | ID của nhà quảng cáo đã ủy quyền cho ứng dụng của nhà phát triển. Bạn có thể sử dụng [/oauth2/advertiser/get/](../12-api-reference/03-ad-accounts.md#doc-1738455508553729) để lấy danh sách các tài khoản nhà quảng cáo đã ủy quyền cho ứng dụng. |
| campaign_id | ID chiến dịch (Campaign ID). Được dùng trong các hoạt động liên quan đến chiến dịch dưới dạng định danh duy nhất. |
| adgroup_id | ID nhóm quảng cáo (Ad group ID). Được dùng trong các hoạt động liên quan đến nhóm quảng cáo dưới dạng định danh duy nhất của một nhóm quảng cáo. |
| ad_id | ID quảng cáo (Ad ID). Được dùng trong các hoạt động liên quan đến quảng cáo dưới dạng định danh duy nhất của một quảng cáo. |

### Nội dung sáng tạo (`Creatives`)

| Concepts | Định nghĩa |
|---|---|
| tiktok_item_id | ID bài đăng TikTok dùng khi tạo [Spark Ads](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1739470744631298). Bạn có thể lấy ID này thông qua trường `item_id` từ phản hồi của endpoint [/identity/video/get/](../12-api-reference/46-identity.md#doc-1740218475032577). |
| video_id | ID video. Video là một loại tài sản sáng tạo mà bạn có thể sử dụng để tạo quảng cáo không phải Spark Ads hoặc Spark Ads ([bằng cách đẩy quảng cáo video đến Tài khoản Doanh nghiệp được liên kết](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1739470744631298)). Xem [tại đây](../09-marketing-api/creatives.md#doc-1738963828459521) để biết cách tải video lên. |
| image_id | ID hình ảnh. Hình ảnh là một loại tài sản sáng tạo mà bạn có thể dùng để tạo quảng cáo. Xem [tại đây](../09-marketing-api/creatives.md#doc-1738963828459521) để biết cách tải hình ảnh lên. |
| music_id | ID âm nhạc. Âm nhạc là một loại tài sản sáng tạo mà bạn có thể dùng để tạo quảng cáo. Xem [tại đây](../09-marketing-api/creatives.md#doc-1738963828459521) để biết cách tải âm nhạc lên. |
| file_id | ID của tệp mà bạn đã tải lên. Bạn có thể tải các tệp video, hình ảnh và âm nhạc lên kho lưu trữ tệp tạm thời của TikTok. Xem [tại đây](../09-marketing-api/creatives.md#doc-1738963828459521) để biết cách tải tệp lên. |
| page_id | ID trang (Instant Form - Biểu mẫu tức thì, Custom TikTok Instant Page - Trang tức thì tùy chỉnh, App Profile Page - Trang hồ sơ ứng dụng, hoặc Storefront page - Trang cửa hàng). Trang là một loại tài sản sáng tạo bạn có thể dùng để tạo quảng cáo. Bạn có thể lấy page ID qua endpoint [/page/get/](../12-api-reference/54-page.md#doc-1820826387779586). |
| creative_portfolio_id | ID của danh mục nội dung sáng tạo (creative portfolio) bạn muốn lấy. Bạn có thể lấy portfolio id (`creative_portfolio_id`) qua endpoint [/creative/portfolio/create/](../12-api-reference/36-creative-portfolios.md#doc-1739091950439426). |
| card_id | ID thẻ tương tác (Display Card, Premium Badge, Countdown Sticker hoặc Download Card). Thẻ là một loại tài sản sáng tạo bạn có thể dùng để tạo quảng cáo. Xem [tại đây](../09-marketing-api/creatives.md#doc-1749019605861377) để tìm hiểu cách lấy và sử dụng card ID. |
| call_to_action_id | ID của danh mục Kêu gọi hành động (Call-to-action - CTA). Danh mục CTA là một nhóm các CTA được tự động tối ưu hóa mà bạn muốn sử dụng trong quảng cáo. Xem [tại đây](../09-marketing-api/creatives.md#doc-1749018853745665) để biết cách lấy và sử dụng `call_to_action_id`. |

---

## Cấu trúc tài khoản (`Account structure`)
<a id="doc-1740029179343874"></a>
<!-- doc_id: 1740029179343874 -->

> Đường dẫn: Get Started > Concepts > Account structure

Một tài khoản nhà phát triển có thể sở hữu tối đa 5 ứng dụng nhà phát triển (developer apps). Các ứng dụng nhà phát triển này có thể phục vụ các tài khoản quảng cáo khác nhau.

Tài khoản nhà quảng cáo (advertiser account) là tài khoản cơ bản trên nền tảng TikTok For Business. Trước khi có thể tạo và quản lý quảng cáo bằng TikTok For Business, nhà quảng cáo phải sở hữu một tài khoản nhà quảng cáo hoặc được các nhà quảng cáo khác cấp quyền quản lý tài khoản và tài sản quảng cáo của họ. Mối quan hệ giữa các ứng dụng nhà phát triển và tài khoản nhà quảng cáo là quan hệ nhiều-nhiều (many-to-many). Khi hoàn tất ủy quyền, phạm vi các tài khoản nhà quảng cáo có thể được xem hoặc quản lý bởi ứng dụng nhà phát triển phụ thuộc vào mối quan hệ giữa nhà quảng cáo và tài khoản nhà quảng cáo.

> [!NOTE]
> • Tài khoản Agency Business Center có thể tạo và chỉnh sửa tài khoản quảng cáo. Để biết chi tiết, xem [Tạo tài khoản quảng cáo](../12-api-reference/15-bc-assets.md#doc-1739939020318721) và [Cập nhật tài khoản quảng cáo](../12-api-reference/15-bc-assets.md#doc-1739939050770434).<br>
> • Đối với các tài khoản quảng cáo do agency tạo trong Business Center, mối quan hệ giữa người dùng và tài khoản quảng cáo có thể được quản lý thông qua các endpoint API sau:<br>
> - [Lấy tài sản](../12-api-reference/15-bc-assets.md#doc-1739432717798401)<br>
> - [Lấy tài sản với tư cách quản trị viên](../12-api-reference/15-bc-assets.md#doc-1739433007779841)<br>
> - [Gán tài sản](../12-api-reference/15-bc-assets.md#doc-1739438211077121)<br>
> - [Hủy gán tài sản](../12-api-reference/15-bc-assets.md#doc-1739448126749698)

---

## Quy trình từng bước (`Step-by-step workflow`)
<a id="doc-1781888800300034"></a>
<!-- doc_id: 1781888800300034 -->

> Đường dẫn: Get Started > Step-by-step workflow

Dưới đây là các bước bạn cần thực hiện trước khi tạo lệnh gọi API đầu tiên.

> [!NOTE]
> Các bước cụ thể cần thiết cho [ủy quyền](bat-dau.md#doc-1781891256601602) và [xác thực](bat-dau.md#doc-1781892384100354) sẽ thay đổi tùy thuộc vào loại API bạn đang sử dụng.

1. [Tạo tài khoản TikTok for Business](bat-dau.md#doc-1738855099573250).
2. [Đăng ký trở thành nhà phát triển](bat-dau.md#doc-1738855176671234).
3. [Tạo ứng dụng nhà phát triển](bat-dau.md#doc-1738855242728450).
4. [Ủy quyền](bat-dau.md#doc-1781891256601602).
5. [Xác thực](bat-dau.md#doc-1781892384100354).
6. Thực hiện lệnh gọi API đầu tiên: Bạn có thể sử dụng [bộ sưu tập Postman TikTok API for Business](https://www.postman.com/tiktok/workspace/tiktok-api-for-business/folder/23207567-9c73b718-e802-40f0-a70d-db8524ed2494) để dễ dàng **kiểm thử** tích hợp mà không ảnh hưởng đến tài khoản TikTok for Business thực tế của bạn.

> [!NOTE]
> Bạn có thể sử dụng các endpoint API hoặc SDK để thực hiện các lệnh gọi đầu tiên. **TikTok API for Business SDK hiện đang trong giai đoạn open beta. Xem [tại đây](../16-sdk/sdk.md#doc-1764231376750658) để biết thêm chi tiết.**

### Video hướng dẫn (`Video tutorial`)

---

## Tạo tài khoản TikTok for Business (`Create a TikTok for Business account`)
<a id="doc-1738855099573250"></a>
<!-- doc_id: 1738855099573250 -->

> Đường dẫn: Get Started > Step-by-step workflow > Create a TikTok for Business account

Trước khi có thể sử dụng TikTok API for Business hoặc TikTok for Business MCP Server, bạn cần đăng ký tại cổng thông tin TikTok for Business Developers. Hãy hoàn tất các bước sau để tạo tài khoản TikTok for Business.

### Các bước thực hiện (`Steps`)

1. Truy cập [trang chủ TikTok for Business Developers](https://business-api.tiktok.com/portal) và nhấp vào nút đăng ký.

![Trang chủ TikTok for Business Developers](https://images.ctfassets.net/5jqet0ab9qci/7wbdK20AnTkjL5N4jPpYZv/fdf20905f7e5f8fb872cdac9c9a13191/TikTok_for_Business_Developers_homepage-EN.png)

2. Trên trang hiển thị, điền địa chỉ email (hoặc số điện thoại), mật khẩu, tích chọn vào ô đồng ý với các điều khoản, điều kiện và chính sách quyền riêng tư, sau đó nhấp vào **Sign Up**.
   - Đối với email, chúng tôi khuyên bạn nên sử dụng bí danh (alias) như `developers+tiktok@company.com` và chia sẻ thông tin đăng nhập với tất cả các nhà phát triển trong nhóm sau khi đăng ký để đảm bảo mọi người đều có quyền truy cập vào tài khoản TikTok for Business.

![Đăng ký tài khoản TikTok for Business](https://images.ctfassets.net/5jqet0ab9qci/1qJr2jKz9ztYNRGxEYIi77/019d8aac217f3b0fb9b4b4b370120994/TikTok_for_Business_account_signup-EN.png)

3. Nhập mã xác minh được gửi tới số điện thoại hoặc email của bạn. Tài khoản của bạn hiện đã được tạo thành công.

![Xác minh đăng ký tài khoản TikTok for Business](https://images.ctfassets.net/5jqet0ab9qci/4oEFDIhjj8RvkGgxw2wvy6/47db488fb4918e682a448183916e4ac6/TikTok_for_Business_account_signup_verification-EN.png)

### Bước tiếp theo (`Next step`)
- Đối với người dùng TikTok API for Business: Bạn cần [đăng ký trở thành nhà phát triển](bat-dau.md#doc-1738855176671234).
- Đối với người dùng TikTok for Business MCP Server: Bạn có thể trực tiếp [kết nối tới TikTok for Business MCP Server](../05-mcp-server/mcp-server-tom-tat.md#doc-1869389950974978). Bạn không cần [đăng ký tài khoản nhà phát triển](bat-dau.md#doc-1738855176671234) hay [tạo ứng dụng nhà phát triển](bat-dau.md#doc-1738855242728450) để thiết lập kết nối này.

---

## Đăng ký trở thành nhà phát triển (`Register as a developer`)
<a id="doc-1738855176671234"></a>
<!-- doc_id: 1738855176671234 -->

> Đường dẫn: Get Started > Step-by-step workflow > Register as a developer

Trước khi có thể tạo ứng dụng và bắt đầu phát triển, bạn cần đăng ký làm nhà phát triển. Hoàn thành các bước sau để đăng ký:

### Các bước thực hiện (`Steps`)

1. Đăng nhập vào [Cổng thông tin TikTok for Business Developers](https://business-api.tiktok.com/portal). Nhấp vào **Become a Developer**.

2. Điền tên của bạn và email liên lạc. Đối với email, chúng tôi khuyên bạn nên sử dụng bí danh như `developers+tiktok@company.com` và chia sẻ thông tin đăng nhập với tất cả các nhà phát triển trong nhóm của bạn để đảm bảo mọi người đều có quyền truy cập vào tài khoản nhà phát triển.<br>
   Lưu ý rằng email liên lạc bắt buộc phải là email **tên miền công ty** đã được xác minh. Hồ sơ sẽ bị từ chối nếu bạn sử dụng email cá nhân hoặc email tạm thời. Trong trường hợp đó, hãy sửa đổi thông tin và nộp lại đơn đăng ký.

3. Nhấp vào **Send Code** để gửi mã xác minh tới địa chỉ email của bạn. Sao chép mã xác minh và dán vào ô nhập liệu Verification Code.

4. Chọn loại người dùng mô tả chính xác nhất doanh nghiệp của bạn, sau đó nhấp vào **Next** để chuyển sang bước tiếp theo. Hãy đảm bảo loại hình được chọn phù hợp với thông tin bạn cung cấp, nếu không hồ sơ có thể bị từ chối:
   - Technology Company (Công ty công nghệ)
   - Direct Advertiser (Nhà quảng cáo trực tiếp)
   - Agency (Đại lý / Công ty truyền thông)

5. Điền tên công ty của bạn. Tên công ty phải:
   - Là tên thương hiệu hợp lệ hoặc tên pháp nhân hợp pháp.
   - Có liên quan đến tên miền email hoặc trang web công ty. Nếu không khớp, vui lòng cung cấp bằng chứng về mối liên quan trong phần mô tả bên dưới.

6. Điền trang web công ty. Trang web của bạn phải:
   - Có thể truy cập công khai.
   - Hợp lệ, đang hoạt động, được xây dựng hoàn chỉnh và trình bày chuyên nghiệp.
   - Trình bày nội dung kinh doanh liên quan có thể truy cập mà không yêu cầu đăng nhập, nêu chi tiết thông tin về sản phẩm và công ty của bạn.
   - Khớp với tên miền email mà bạn đã cung cấp.
   - Được lưu trữ trên tên miền thuộc sở hữu của công ty bạn. Không được chứa tên miền liên quan đến các nền tảng mạng xã hội, công ty lưu trữ của bên thứ ba, sàn thương mại điện tử, v.v.
   - Là tên miền thực tế của trang web công ty. Các đường liên kết rút gọn không được chấp nhận.
   - Là trang web của công ty chứ không phải trang web cá nhân. Hiện tại, chúng tôi chưa thể tiếp nhận các tài khoản cá nhân hoặc nhà phát triển độc lập. Nếu bạn thuộc một công ty, vui lòng sử dụng trang web công ty.

7. Chọn Vị trí chính của nhà phát triển (Primary Developer Location). Đây phải là vị trí chính của nhóm phát triển trong công ty bạn, chứ không phải nơi bạn điều hành hoạt động kinh doanh. Ví dụ: nếu công ty của bạn hoạt động kinh doanh tại Singapore nhưng nhà phát triển đặt tại Trung Quốc, hãy chọn Trung Quốc.
   > [!NOTE]
   > Đối với các nhà phát triển phát triển dịch vụ ra nước ngoài từ Trung Quốc (China-outbound developers), vui lòng chọn Trung Quốc làm Vị trí chính của nhà phát triển, bất kể công ty của bạn hoạt động kinh doanh ở đâu.

8. Cung cấp các thông tin khác về công ty và hoạt động kinh doanh của bạn, sau đó nhấp vào **Submit**. Xin lưu ý các câu hỏi này sẽ khác nhau tùy thuộc vào loại nhà phát triển của bạn. Đối với câu hỏi về kế hoạch sử dụng dữ liệu và API TikTok, vui lòng mô tả càng chi tiết càng tốt, nếu không hồ sơ có thể bị từ chối. Phần mô tả cần giải thích các trường hợp sử dụng đã chọn ở câu hỏi trước và mục đích đăng ký làm nhà phát triển. Dưới đây là ví dụ để bạn tham khảo:
   > *[Tên công ty] là một công ty thương mại điện tử có trụ sở chính tại [quốc gia/khu vực], vận hành thương hiệu [tên thương hiệu] và trang web thương mại điện tử tại [quốc gia/khu vực]. Chúng tôi là nhóm phát triển và sản phẩm, phụ trách phát triển các công cụ tích hợp Marketing API để hỗ trợ đội ngũ tiếp thị của chúng tôi.*
   > [!NOTE]
   > Bạn cũng có thể sử dụng trường mô tả để bổ sung bất kỳ thông tin nào khác muốn nêu rõ.

9. Bạn sẽ nhận được thông báo về kết quả xét duyệt trong vòng 3 ngày làm việc.

### Bước tiếp theo (`Next step`)
[Tạo ứng dụng nhà phát triển](bat-dau.md#doc-1738855242728450)

---

## Tạo ứng dụng nhà phát triển (`Create a developer app`)
<a id="doc-1738855242728450"></a>
<!-- doc_id: 1738855242728450 -->

> Đường dẫn: Get Started > Step-by-step workflow > Create a developer app

Trước khi bắt đầu tích hợp, bạn cần tạo một ứng dụng nhà phát triển. Hoàn thành các bước sau để tạo ứng dụng nhà phát triển:

> [!NOTE]
> Trước khi nộp đơn xin cấp ứng dụng nhà phát triển, hãy đảm bảo hồ sơ nhà phát triển của bạn đã được phê duyệt. Nếu không, lỗi sẽ xảy ra. Xem [tại đây](bat-dau.md#doc-1738855176671234) để biết thêm thông tin về đăng ký.

### Các bước thực hiện (`Steps`)

1. Đăng nhập vào Cổng thông tin TikTok For Business Developers và nhấp vào **Create an App**.

2. Đặt tên mô tả rõ ràng cho ứng dụng của bạn. Ví dụ: "Video Upload Tool", "TikTok Media Buy Platform", v.v.
   > [!NOTE]
   > Đây là tên của ứng dụng nhà phát triển, chứ không phải tên ứng dụng di động. Nếu bạn tích hợp API để quản lý quảng cáo TikTok quảng bá cho nhiều ứng dụng di động, bạn có thể quản lý tất cả trong cùng một ứng dụng nhà phát triển mà không cần tạo nhiều ứng dụng nhà phát triển cho từng ứng dụng di động.

3. Trong mục **App description**, hãy cung cấp thông tin về mục đích sử dụng dự kiến của ứng dụng cũng như bất kỳ nhà quảng cáo nào mà bạn có thể hợp tác cùng. Chúng tôi khuyên bạn nên định dạng thông tin theo cấu trúc dưới đây:
   - **Intended Uses** (Mục đích sử dụng dự kiến): Mô tả các chức năng dự kiến chính và tình huống sử dụng của ứng dụng nhà phát triển. Giải thích những quyền hạn cốt lõi nào cần thiết về mặt kỹ thuật để kích hoạt các chức năng chính.
   - **Developer App Access Controls** (Kiểm soát quyền truy cập ứng dụng nhà phát triển): Làm rõ liệu quyền truy cập ứng dụng nhà phát triển chỉ giới hạn trong nội bộ tổ chức hay được chia sẻ với các tài khoản hoặc tổ chức bên ngoài khác.

   Dưới đây là ví dụ tham khảo:
   > *Ứng dụng nhà phát triển này đóng vai trò là công cụ mua quảng cáo TikTok nội bộ của chúng tôi, được sử dụng bởi nhóm thu hút người dùng (user acquisition). Thông qua việc tích hợp các API của TikTok phục vụ tạo quảng cáo, tải lên nội dung sáng tạo và báo cáo dữ liệu, ứng dụng này nâng cao hiệu quả vận hành chiến dịch quảng cáo.*

4. Chỉ định **advertiser redirect URL** (URL chuyển hướng của nhà quảng cáo).
   Sau khi nhà quảng cáo chấp thuận ủy quyền, họ sẽ được chuyển hướng tới URL chuyển hướng đã được cấu hình tại đây. Mã xác thực (authentication code) sẽ được gắn vào cuối redirect URL này. Đảm bảo URL của bạn hợp lệ.
   > [!NOTE]
   > Bạn có thể cấu hình tối đa 10 URL chuyển hướng nhà quảng cáo, bao gồm cả localhost. Khi một redirect URL mới được thêm vào, bạn có thể tạo một URL ủy quyền nhà quảng cáo mới.

5. Trong mục **Scope of permission**, chọn các quyền mà bạn cần trong ứng dụng của mình.
   Các quyền hạn này quyết định những endpoint API nào bạn có quyền truy cập. Đảm bảo rằng phạm vi quyền bạn chọn phù hợp với phần mô tả ứng dụng. Bạn có thể tìm thấy **scope of permission** của từng endpoint ở cột cuối cùng trong bảng **Danh sách các endpoint hiện có**.
   > [!NOTE]
   > Để đảm bảo sử dụng Accounts API đúng quy định, bắt đầu từ ngày 20 tháng 3 năm 2026 lúc 00:00 (GMT+0), nhà phát triển phải hoàn thành [Biểu mẫu đăng ký quyền truy cập Accounts API](https://bytedance.sg.larkoffice.com/share/base/form/shrlgu4WEvtSXpEDLcCw56u4Rfc) trước khi gửi ứng dụng nhà phát triển mới hoặc yêu cầu mở rộng phạm vi quyền bao gồm phạm vi quyền "TikTok Accounts". Vui lòng làm theo hướng dẫn cẩn thận và cung cấp thông tin rõ ràng, chính xác để giúp quá trình xét duyệt đơn diễn ra thuận lợi. Để biết thêm chi tiết về các trường hợp sử dụng Accounts API, vui lòng tham khảo tài liệu [Accounts API](../10-organic-api/accounts-api.md#doc-1737944384433218).

6. Sau khi chọn tất cả các quyền bạn cần, nhấp vào **Confirm**.

7. Bạn đã nộp đơn đăng ký ứng dụng nhà phát triển để xét duyệt. Quá trình xét duyệt có thể mất từ **2 đến 3 ngày làm việc**.
   - Để kiểm tra trạng thái Ứng dụng, nhấp vào nút màu đỏ ở góc trên bên phải, điều hướng đến **My Apps** và kiểm tra trong phần **Verification Status**. Nếu ứng dụng của bạn bị từ chối, bạn có thể chỉnh sửa yêu cầu và gửi lại. Khi ứng dụng được phê duyệt, bạn có thể sử dụng mã ủy quyền để nhận access token dài hạn.
   - Nếu bạn cần tạo nhiều hơn một ứng dụng nhà phát triển, bạn có thể điều hướng đến **My Apps** và nhấp vào **Create App**. Mỗi nhà phát triển có thể tạo tối đa 5 ứng dụng nhà phát triển.

### Bước tiếp theo (`Next step`)
[Ủy quyền](bat-dau.md#doc-1781891256601602)


---

## Ủy quyền (`Authorization`)
<a id="doc-1781891256601602"></a>
<!-- doc_id: 1781891256601602 -->

> Đường dẫn: Get Started > Step-by-step workflow > Authorization

Sau khi ứng dụng nhà phát triển của bạn được phê duyệt, bạn cần nhận ủy quyền từ nhà quảng cáo, tài khoản TikTok, tài khoản TikTok Creator Marketplace (TTCM) hoặc tài khoản TikTok One (TTO) Creator Marketplace để quản lý tài khoản của họ.

**Các bước cụ thể cần thiết để ủy quyền sẽ thay đổi tùy thuộc vào loại API bạn đang sử dụng.** Vui lòng tham khảo các chủ đề sau để biết hướng dẫn chi tiết về cách hoàn tất ủy quyền:

- Ủy quyền Marketing API: Tham khảo **[Ủy quyền Marketing API](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373141733378)** để tìm hiểu cách nhận ủy quyền từ nhà quảng cáo nhằm quản lý tài khoản của họ.
- Ủy quyền Accounts API / Mentions API: Tham khảo **[Ủy quyền Accounts API](../10-organic-api/accounts-api.md#doc-1738083939371009)** hoặc **[Ủy quyền Mentions API](../10-organic-api/mentions-api.md#doc-1825103730490434)** để tìm hiểu cách nhận ủy quyền từ người dùng tài khoản TikTok nhằm quản lý tài khoản của họ.
- Ủy quyền TTO API:
  - Tham khảo **[Nhận ủy quyền từ tài khoản TTO Creator Marketplace](../10-organic-api/tiktok-one-api.md#doc-1825117875361793)** để tìm hiểu cách nhận ủy quyền từ người dùng tài khoản TTO Creator Marketplace. Access token này không bao giờ hết hạn.
- Ủy quyền Creator Marketplace API:
  - Tham khảo ****Nhận ủy quyền từ tài khoản TTCM**** để tìm hiểu cách nhận ủy quyền từ người dùng tài khoản TTCM nhằm quản lý tài khoản của họ.
  - Tham khảo **[Nhận ủy quyền từ Nhà sáng tạo](../10-organic-api/tiktok-one-api.md#doc-1768506960432130)** để tìm hiểu cách nhận ủy quyền từ các Nhà sáng tạo (Creators).
- Ủy quyền Discovery API: Tham khảo **[Ủy quyền Discovery API](../10-organic-api/discovery-api.md#doc-1825127469285442)** để tìm hiểu cách nhận ủy quyền từ nhà quảng cáo hoặc người dùng tài khoản TikTok để quản lý tài khoản của họ.
- Ủy quyền Spark Ads Recommendation API: Nhận ủy quyền từ người dùng tài khoản TikTok hoặc người dùng tài khoản TTCM để quản lý tài khoản của họ.

### So sánh ủy quyền giữa các loại API khác nhau (`Comparing authorization for different APIs`)

Bảng dưới đây nêu rõ sự khác biệt trong quy trình ủy quyền đối với Marketing API, Accounts API, Mentions API, Creator Marketplace API, TTO API, Discovery API và Spark Ads Recommendation API:

| Loại API | Mô tả | URL ủy quyền | Thời hạn hiệu lực của mã ủy quyền (`auth_code`) |
|---|---|---|---|
| Marketing API | Ủy quyền cho Marketing API được thực hiện thông qua nhà quảng cáo TikTok For Business. | URL ủy quyền nhà quảng cáo trên [My Apps](https://business-api.tiktok.com/portal/apps). Xem [Ủy quyền - Bước 1](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373141733378). | Có hiệu lực trong 1 giờ và chỉ dùng được một lần. Sau khi `auth_code` hết hạn, bạn cần thực hiện lại các bước ủy quyền từ đầu. |
| Accounts API / Mentions API | Ủy quyền cho Accounts API/Mentions API được thực hiện thông qua tài khoản TikTok tự nhiên (organic account). | URL ủy quyền chủ tài khoản TikTok trên [My Apps](https://ads.tiktok.com/i18n/login?redirect=https%3A%2F%2Fads.tiktok.com%2Fmarketing_api%2Fapps%2F). Xem [Tài khoản - Ủy quyền](../10-organic-api/accounts-api.md#doc-1738083939371009). | Có hiệu lực trong 10 phút và chỉ dùng được một lần. Sau khi `auth_code` hết hạn, bạn cần thực hiện lại các bước ủy quyền từ đầu. |
| TikTok Creator Marketplace API | Ủy quyền cho TikTok Creator Marketplace (TTCM) API được thực hiện thông qua tài khoản TTCM và tài khoản TikTok tự nhiên.<br>**Lưu ý**: TikTok Creator Marketplace API hiện đang ở giai đoạn closed beta. Bạn cần nộp đơn xin cấp quyền truy cập trước. | • Ủy quyền tài khoản TTCM: URL ủy quyền nhà quảng cáo trên [My Apps](https://business-api.tiktok.com/portal/apps). Xem **Nhận ủy quyền và xác thực từ tài khoản TTCM của bạn**.<br>• Ủy quyền Creator: URL ủy quyền chủ tài khoản TikTok trên [My Apps](https://business-api.tiktok.com/portal/apps). Xem [Nhận ủy quyền từ Creators - Bước 1](../10-organic-api/tiktok-one-api.md#doc-1768506960432130). | • Mã ủy quyền tài khoản TTCM: Có hiệu lực trong 1 giờ và chỉ dùng được một lần.<br>• Mã ủy quyền Creator: Có hiệu lực trong 10 phút và chỉ dùng được một lần. Sau khi hết hạn cần thực hiện lại các bước từ đầu. |
| TTO API | Ủy quyền cho TTO API được thực hiện thông qua tài khoản TTO Creator Marketplace. | URL ủy quyền nhà quảng cáo trên [My Apps](https://ads.tiktok.com/i18n/login?redirect=https%3A%2F%2Fads.tiktok.com%2Fmarketing_api%2Fapps%2F). Xem [Nhận ủy quyền và xác thực từ tài khoản TTO Creator Marketplace của bạn](../10-organic-api/tiktok-one-api.md#doc-1825117875361793). | Có hiệu lực trong 1 giờ và chỉ dùng được một lần. Sau khi hết hạn, bạn cần thực hiện lại các bước ủy quyền từ đầu. |
| Discovery API | Ủy quyền cho Discovery API được thực hiện thông qua nhà quảng cáo TikTok For Business hoặc tài khoản TikTok tự nhiên. | • Ủy quyền nhà quảng cáo (khi endpoint liên quan đến hashtags): URL ủy quyền nhà quảng cáo trên [My Apps](https://ads.tiktok.com/i18n/login?redirect=https%3A%2F%2Fads.tiktok.com%2Fmarketing_api%2Fapps%2F). Xem [Ủy quyền - Bước 1](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373141733378).<br>• Ủy quyền người dùng tài khoản TikTok (khi endpoint liên quan đến tracks/âm nhạc): URL ủy quyền chủ tài khoản TikTok trên My Apps. Xem [Ủy quyền Accounts API](../10-organic-api/accounts-api.md#doc-1738083939371009). | • Mã ủy quyền nhà quảng cáo: Có hiệu lực trong 1 giờ và chỉ dùng được một lần.<br>• Mã ủy quyền người dùng tài khoản TikTok: Có hiệu lực trong 10 phút và chỉ dùng được một lần. Sau khi hết hạn cần thực hiện lại các bước từ đầu. |
| Spark Ads Recommendation API | Ủy quyền cho Spark Ads Recommendation API được thực hiện thông qua tài khoản TTCM hoặc tài khoản TikTok tự nhiên. | • Ủy quyền tài khoản TTCM (dành cho [/spark_ad/recommend/](../12-api-reference/63-spark-ads-recommendation.md#doc-1825128700959746)): URL ủy quyền nhà quảng cáo trên [My Apps](https://ads.tiktok.com/i18n/login?redirect=https%3A%2F%2Fads.tiktok.com%2Fmarketing_api%2Fapps%2F). Xem **Nhận ủy quyền và xác thực từ tài khoản TTCM của bạn**.<br>• Ủy quyền người dùng tài khoản TikTok (dành cho [/business/video/recommend/](../12-api-reference/63-spark-ads-recommendation.md#doc-1825128684907522)): URL ủy quyền chủ tài khoản TikTok trên My Apps. Xem [Ủy quyền Accounts API](../10-organic-api/accounts-api.md#doc-1738083939371009). | • Mã ủy quyền tài khoản TTCM: Có hiệu lực trong 1 giờ và chỉ dùng được một lần.<br>• Mã ủy quyền người dùng tài khoản TikTok: Có hiệu lực trong 10 phút và chỉ dùng được một lần. Sau khi hết hạn cần thực hiện lại các bước từ đầu. |

---

## Cấu hình URL chuyển hướng cho chủ tài khoản TikTok (`TikTok account holder redirect URL configuration`)
<a id="doc-1832209711206401"></a>
<!-- doc_id: 1832209711206401 -->

> Đường dẫn: Get Started > Step-by-step workflow > Authorization > TikTok account holder redirect URL configuration

URL chuyển hướng (redirect URL) là thành phần then chốt trong khung ủy quyền OAuth 2.0, được thiết kế để đảm bảo các phản hồi ủy quyền được gửi an toàn đến một URL xác định. Việc đăng ký đúng cách các redirect URL giúp ngăn chặn các lỗ hổng chuyển hướng mở (open redirector vulnerabilities), vốn có thể bị khai thác trong các cuộc tấn công giả mạo (phishing) và các hoạt động độc hại khác.

**TikTok account holder redirect URL** (URL chuyển hướng của chủ tài khoản TikTok) là địa chỉ URL mà người dùng tài khoản TikTok sẽ được chuyển hướng tới sau khi ủy quyền cho ứng dụng nhà phát triển của bạn bằng các quyền tài khoản TikTok. Sau khi người dùng cấp quyền ủy quyền, redirect URL sẽ được nối thêm một `auth_code` để tạo access token ngắn hạn. Nhà phát triển có thể cấu hình redirect URL trỏ tới máy chủ của mình để tự động phân tích cú pháp `auth_code`, giúp loại bỏ nhu cầu người dùng tài khoản TikTok phải tự tìm và chia sẻ thủ công `auth_code` với nhà phát triển.

Bạn có thể cấu hình tối đa 10 URL chuyển hướng cho chủ tài khoản TikTok cho mỗi ứng dụng nhà phát triển. Mỗi redirect URL chủ tài khoản TikTok được kích hoạt sẽ tự động tạo một URL ủy quyền chủ tài khoản TikTok mới. Hệ thống duy trì một URL hoạt động tại một thời điểm (được đánh dấu màu đỏ). Khi chỉ có một redirect URL tồn tại, URL đó sẽ tự động kích hoạt theo mặc định. Với nhiều redirect URL, hãy kích hoạt URL mong muốn bằng cách nhấp vào URL đó.

### Quy tắc định dạng URL chuyển hướng (`Formatting rules for redirect URLs`)

Khi định nghĩa redirect URL chủ tài khoản TikTok cho ứng dụng nhà phát triển, bạn cần tuân thủ các quy tắc định dạng sau để đảm bảo hoạt động chính xác:

| Rules | Correct example | Bad example |
|---|---|---|
| URLs must be absolute and end with /. | `https://dev.example.com/auth/callback/` | • `https://dev.example.com/auth/callback`<br>• Thiếu dấu `/` ở cuối<br>• `/auth/callback/`<br>• Thiếu giao thức (scheme) và tên miền |
| URLs should be static, while parameters are denied and should be ignored. | `https://dev.example.com/auth/callback/` | • `https://dev.example.com/auth/callback/?id=1`<br>• Chứa tham số truy vấn `?id=1` |
| URLs cannot include anchors #. | `https://dev.example.com/auth/callback/` | • `https://dev.example.com/auth/callback/#1`<br>• Chứa anchor `#1` |
| URLs must start with https://. | `https://dev.example.com/auth/callback/` | • `http://dev.example.com/auth/callback/`<br>• Sử dụng `http` thay vì `https` |
| URLs cannot include ports. | `https://dev.example.com/auth/callback/` | • `https://dev.example.com:3000/auth/callback/`<br>• Chứa số cổng `:3000` |
| The length of the registered URI should fall within the range of 10 to 512 characters. | N/A | N/A |

Nếu không tuân thủ các quy tắc trên, bạn sẽ nhận được thông báo lỗi. Bạn có thể chỉnh sửa lại redirect URL của mình cho đúng định dạng.

### Hướng dẫn di chuyển URL chuyển hướng (`Migration instructions for redirect URL`)

Để di chuyển URL chuyển hướng của chủ tài khoản TikTok, hãy làm theo các bước sau:

1. Chỉnh sửa redirect URL bằng cách xóa mọi tham số truy vấn (được biểu thị bằng ký hiệu `?`) hoặc phân đoạn định vị (được biểu thị bằng ký hiệu `#`) có thể có ở cuối đường dẫn. URL của bạn phải kết thúc bằng dấu gạch chéo (`/`).

2. Nếu bạn xóa các tham số truy vấn khỏi redirect URL nhưng vẫn muốn đạt được hiệu quả tương tự, hãy sử dụng tham số `state` trong URL ủy quyền chủ tài khoản TikTok. Cách thực hiện là mã hóa các tham số truy vấn thành một đối tượng JSON và đưa vào làm giá trị của tham số `state` trong URL ủy quyền. Dưới đây là các ví dụ về cách mã hóa tham số truy vấn thành tham số `state`:

**Ví dụ 1**:
- URL chuyển hướng chủ tài khoản TikTok gốc: `https://www.tiktok.com/photo?source=tiktok`
- Tham số truy vấn: `?source=tiktok`
- Tham số `state` đã mã hóa để thêm vào URL ủy quyền: `&state={"source":"tiktok"}`

**Ví dụ 2**:
- URL chuyển hướng chủ tài khoản TikTok gốc: `https://www.tiktok.com/photo?source=tiktok&platform=web`
- Tham số truy vấn: `?source=tiktok&platform=web`
- Tham số `state` đã mã hóa để thêm vào URL ủy quyền: `&state={"source":"tiktok","platform":"web"}`

3. Sau khi nhận được mã ủy quyền trong redirect URL, hãy trích xuất giá trị tham số truy vấn từ tham số `state` trong URL ủy quyền chủ tài khoản TikTok. Thao tác này bao gồm việc giải mã chuỗi mã hóa JSON từ tham số `state` thành một dictionary hoặc object, sau đó truy cập các giá trị của các khóa cụ thể trong dictionary đó.

Dưới đây là ví dụ về cách giải mã tham số `state` trong Python:

```python
import json
from urllib.parse import unquote

state_value = '%7B%22source%22%3A%22tiktok%22%7D'
state = unquote(state_value)
state_dict = json.loads(state)
source = state_dict.get('source')
print(state_dict)

# Đầu ra: {'source': 'tiktok'}
```

---

## Xác thực (`Authentication`)
<a id="doc-1781892384100354"></a>
<!-- doc_id: 1781892384100354 -->

> Đường dẫn: Get Started > Step-by-step workflow > Authentication

Sau khi bạn nhận được `auth_code` từ nhà quảng cáo, người dùng tài khoản TikTok, tài khoản TikTok Creator Marketplace (TTCM) hoặc tài khoản TikTok One (TTO) Creator Marketplace, bạn có thể dùng nó để tạo **access token** (mã truy cập) cho các yêu cầu API tiếp theo.

**Các bước cụ thể cần thiết để xác thực sẽ thay đổi tùy thuộc vào loại API bạn đang sử dụng.** Vui lòng tham khảo các chủ đề sau để biết hướng dẫn chi tiết về cách hoàn tất xác thực:

- Xác thực Marketing API: Tham khảo **[Xác thực Marketing API](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162)** để tìm hiểu cách tạo access token dài hạn. Access token này không bao giờ hết hạn.
- Xác thực Accounts API / Mentions API: Tham khảo **[Xác thực Accounts API](../10-organic-api/accounts-api.md#doc-1738084387220481)** hoặc **[Xác thực Mentions API](../10-organic-api/mentions-api.md#doc-1825105003772930)** để tìm hiểu cách tạo access token. Access token này có hiệu lực trong 1 ngày. Khi access token hết hạn, bạn cần làm mới token qua endpoint [/tt_user/oauth2/refresh_token/](../10-organic-api/accounts-api.md#doc-1738084387220481).
- Xác thực TTO API:
  - Tham khảo **[Nhận xác thực từ tài khoản TTO Creator Marketplace](../10-organic-api/tiktok-one-api.md#doc-1825117875361793)** để tìm hiểu cách tạo access token cho tài khoản TTO Creator Marketplace. Access token này không bao giờ hết hạn.
- Xác thực Creator Marketplace API:
  - Tham khảo ****Xác thực tài khoản TTCM**** để tìm hiểu cách tạo access token cho tài khoản TTCM. Access token này không bao giờ hết hạn.
  - Tham khảo **[Nhận ủy quyền từ Nhà sáng tạo - Bước 3](../10-organic-api/tiktok-one-api.md#doc-1768506960432130)** để tìm hiểu cách tạo access token của Creator. Token này có hiệu lực trong 1 ngày. Khi access token hết hạn, bạn cần làm mới qua **/tt_user/oauth2/refresh_token/**.
- Xác thực Discovery API: Tham khảo **[Xác thực Discovery API](../10-organic-api/discovery-api.md#doc-1825127469285442)** để tìm hiểu cách tạo access token nhà quảng cáo hoặc access token tài khoản TikTok. Access token nhà quảng cáo không bao giờ hết hạn, trong khi access token tài khoản TikTok có hiệu lực trong 1 ngày (làm mới qua [/tt_user/oauth2/refresh_token/](../10-organic-api/accounts-api.md#doc-1738084387220481)).
- Xác thực Spark Ads Recommendation API: Tạo access token tài khoản TTCM hoặc access token tài khoản TikTok. Access token tài khoản TTCM không bao giờ hết hạn, còn access token tài khoản TikTok có hiệu lực trong 1 ngày (làm mới qua [/tt_user/oauth2/refresh_token/](../10-organic-api/accounts-api.md#doc-1738084387220481)).

### So sánh xác thực giữa các loại API khác nhau (`Comparing authentication for different APIs`)

Bảng dưới đây nêu rõ sự khác biệt trong quy trình xác thực đối với từng loại API:

| Loại API | Endpoint xác thực | Thời hạn hiệu lực của access token (`Access token expiry`) |
|---|---|---|
| Marketing API | [/oauth2/access_token/](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162) (Access token nhà quảng cáo) | Access token nhà quảng cáo không bao giờ hết hạn. Nếu muốn thu hồi/hủy hiệu lực token, hãy sử dụng [/oauth2/revoke_token/](../12-api-reference/10-authentication.md#doc-1739965949088770). |
| Accounts API / Mentions API | [/tt_user/oauth2/token/](../10-organic-api/accounts-api.md#doc-1738084387220481) (Access token tài khoản TikTok) | Access token tài khoản TikTok có hiệu lực trong 1 ngày. Sau khi hết hạn, bạn cần làm mới qua [/tt_user/oauth2/refresh_token/](../10-organic-api/accounts-api.md#doc-1738084387220481). |
| TikTok Creator Marketplace API | • [/oauth2/access_token/](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162) (Access token tài khoản TTCM)<br>• **/tt_user/oauth2/token/** (Access token Creator) | • Access token tài khoản TTCM: Không bao giờ hết hạn (thu hồi qua [/oauth2/revoke_token/](../12-api-reference/10-authentication.md#doc-1739965949088770)).<br>• Access token Creator: Có hiệu lực trong 1 ngày, làm mới qua [/tt_user/oauth2/refresh_token/](../12-api-reference/68-tiktok-one-p1.md#doc-1768493902119937). |
| TTO API | [/oauth2/access_token/](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162) (Access token TTO) | Access token tài khoản TTO không bao giờ hết hạn. Nếu muốn hủy hiệu lực, hãy dùng [/oauth2/revoke_token/](../12-api-reference/10-authentication.md#doc-1739965949088770). |
| Discovery API | • [/oauth2/access_token/](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162) (Access token nhà quảng cáo)<br>• [/tt_user/oauth2/token/](../10-organic-api/accounts-api.md#doc-1738084387220481) (Access token tài khoản TikTok) | • Access token nhà quảng cáo (khi endpoint liên quan đến hashtags): Không bao giờ hết hạn (thu hồi qua [/oauth2/revoke_token/](../12-api-reference/10-authentication.md#doc-1739965949088770)).<br>• Access token tài khoản TikTok (khi endpoint liên quan đến tracks): Có hiệu lực trong 1 ngày, làm mới qua [/tt_user/oauth2/refresh_token/](../10-organic-api/accounts-api.md#doc-1738084387220481). |
| Spark Ads Recommendation API | • [/oauth2/access_token/](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162) (Access token TTCM)<br>• [/tt_user/oauth2/token/](../10-organic-api/accounts-api.md#doc-1738084387220481) (Access token tài khoản TikTok) | • Access token TTCM (cho `/spark_ad/recommend/`): Không bao giờ hết hạn (thu hồi qua [/oauth2/revoke_token/](../12-api-reference/10-authentication.md#doc-1739965949088770)).<br>• Access token tài khoản TikTok (cho `/business/video/recommend/`): Có hiệu lực trong 1 ngày, làm mới qua [/tt_user/oauth2/refresh_token/](../10-organic-api/accounts-api.md#doc-1738084387220481). |

---

## Giới hạn tốc độ gọi (`Rate limits`)
<a id="doc-1740029171730433"></a>
<!-- doc_id: 1740029171730433 -->

> Đường dẫn: Get Started > Rate limits

Để đảm bảo tính khả dụng và hiệu năng của dịch vụ, chúng tôi áp dụng giới hạn tốc độ gọi ở cấp độ ứng dụng nhà phát triển (developer app-level) và giới hạn cụ thể theo từng endpoint (endpoint-specific rate limits).

- Giới hạn tốc độ gọi ở cấp độ ứng dụng nhà phát triển áp dụng cho các yêu cầu API gửi tới từng endpoint từ một ứng dụng nhà phát triển.
- Giới hạn tốc độ gọi cụ thể theo từng endpoint áp dụng cho các yêu cầu API gửi tới một endpoint hoặc nhóm endpoint nhất định. Giới hạn giữa các endpoint khác nhau là độc lập với nhau. Ví dụ: nếu ứng dụng đạt ngưỡng giới hạn tốc độ gọi đối với endpoint `/campaign/get`, ứng dụng vẫn có thể gửi yêu cầu bình thường tới endpoint `/ad/get/`.

### Giới hạn tốc độ gọi cấp ứng dụng nhà phát triển (`Developer app-level rate limits`)

Chúng tôi thiết lập 4 cấp hạn mức gọi khác nhau cho mỗi ứng dụng nhà phát triển, và mỗi cấp bao gồm 3 loại giới hạn: Giới hạn QPS (Queries-Per-Second - số truy vấn mỗi giây), Giới hạn QPM (Queries-Per-Minute - số truy vấn mỗi phút) và Giới hạn QPD (Queries-Per-Day - số truy vấn mỗi ngày).

Khi vượt quá giới hạn tốc độ gọi, máy chủ sẽ trả về mã lỗi `"code": 40100`, có nghĩa là yêu cầu của bạn đã bị điều tiết tốc độ (throttled). Bạn sẽ cần tạm ngừng gọi tới giao diện đó trong một khoảng thời gian và tiếp tục gọi sau khi lệnh tạm ngừng được dỡ bỏ. Thời gian tạm ngừng phụ thuộc vào loại giới hạn đã đạt tới:
- Đối với giới hạn QPM, bạn cần đợi 5 phút trước khi có thể thực hiện lại các yêu cầu API.
- Đối với giới hạn QPD, bạn cần đợi đến ngày tiếp theo (theo giờ UTC+0) để thực hiện lại các yêu cầu API. Lưu ý rằng giới hạn QPD được thiết lập lại (reset) vào lúc 00:00:00 giờ UTC+0 mỗi ngày.

#### Các cấp độ giới hạn (`Rate limit levels`)

| Level | QPS | QPM | QPD |
| --- | --- | ------- | ------ |
| Basic | 10 | 600 | 864,000 |
| Advanced | 20 | 1,200 | 1,728,000 |
| Premium | 30 | 1,800 | 2,592,000 |
| Ultimate | 50 | 3,000 | 4,320,000 |

> [!NOTE]
> • Tất cả các ứng dụng mặc định được đặt ở cấp độ `Basic`. Để thay đổi giới hạn QPS, vui lòng nộp đơn thông qua **My Apps > App Detail > Authorization**.<br>
> • Chúng tôi chỉ có thể nâng hạn mức API từng cấp một tại một thời điểm (từ Basic lên Advanced / từ Advanced lên Premium / từ Premium lên Ultimate). Khi nộp đơn, hãy cung cấp lý do cần nâng giới hạn. Dưới đây là ví dụ tham khảo:<br>
> *Hạn mức API Rate Limit hiện tại không đủ đáp ứng trong trường hợp báo cáo dữ liệu, khiến chúng tôi thỉnh thoảng gặp lỗi giới hạn. Vì vậy, chúng tôi xin nộp đơn xin nâng cấp giới hạn tốc độ gọi.*<br>
> • Bạn không cần nộp đơn thay đổi cấp giới hạn cho Events API, vì giới hạn tốc độ gọi của Events API là như nhau cho mọi cấp độ.

![Developer app level rate limit](https://images.ctfassets.net/5jqet0ab9qci/5safEQ1582dHJ5XMe4LIOf/7f1531b7e7b3d5131c9b09309f562fa2/Developer_app_level_rate_limit.png)

### Giới hạn tốc độ gọi cụ thể theo endpoint (`Endpoint-specific rate limits`)

> [!NOTE]
> Các giới hạn tốc độ gọi riêng biệt được áp dụng cho các endpoint TTO API, bao gồm [/tto/creator/authorized/](../12-api-reference/68-tiktok-one-p1.md#doc-1834913529338882), [/tto/creator/authorized/video/list/](../12-api-reference/68-tiktok-one-p1.md#doc-1834913554657282), [/tto/tcm/creator/public/](../12-api-reference/68-tiktok-one-p1.md#doc-1828185358712897), [/tto/tcm/creator/public/video/list/](../12-api-reference/68-tiktok-one-p1.md#doc-1828185411810305), [/tto/tcm/rank/](../12-api-reference/68-tiktok-one-p1.md#doc-1816378813274113) và [/tto/tcm/creator/discover/](../12-api-reference/68-tiktok-one-p1.md#doc-1825017307843585). Tham khảo tài liệu [Giới hạn tốc độ gọi cho TTO API](../10-organic-api/tiktok-one-api.md#doc-1825117901366274) để biết thêm chi tiết.

| Endpoint | Basic (QPS / QPM / QPD) | Advanced (QPS / QPM / QPD) | Premium (QPS / QPM / QPD) | Ultimate (QPS / QPM / QPD) |
|---|---|---|---|---|
| `/creative/quick_optimization/create/` | 1 / 30 / 5.000 | 2 / 60 / 10.000 | 3 / 180 / 15.000 | 3 / 180 / 15.000 |
| `/creative/smart_video/create/` | 1 / 30 / 5.000 | 2 / 60 / 10.000 | 3 / 180 / 15.000 | 3 / 180 / 15.000 |
| `/ad/create/` | 5 / 150 / 86.400 | 10 / 200 / 86.400 | 10 / 300 / 86.400 | 15 / 300 / 86.400 |
| `/video_template/task/create/` | 1 / 30 / 5.000 | 2 / 60 / 10.000 | 3 / 180 / 15.000 | 3 / 180 / 15.000 |
| `/catalog/product/file/` | 5 / 300 / 432.000 | 5 / 300 / 432.000 | 10 / 600 / 864.000 | 10 / 600 / 864.000 |
| `/catalog/product/upload/` | 5 / 300 / 432.000 | 5 / 300 / 432.000 | 10 / 600 / 864.000 | 10 / 600 / 864.000 |
| `/catalog/product/update/` | 2 / 120 / 172.800 | 2 / 120 / 172.800 | 5 / 300 / 432.000 | 5 / 300 / 432.000 |
| `/catalog/product/delete/` | 2 / 120 / 172.800 | 2 / 120 / 172.800 | 5 / 300 / 432.000 | 5 / 300 / 432.000 |
| Báo cáo bất đồng bộ (`/report/task/create/` POST) | 2 / 60 / 4.500 | 2 / 60 / 4.500 | 2 / 60 / 4.500 | 2 / 60 / 4.500 |
| `/event/track/` | 1.000 / 600.000 / 86.400.000 | 1.000 / 600.000 / 86.400.000 | 1.000 / 600.000 / 86.400.000 | 1.000 / 600.000 / 86.400.000 |
| App Events (`/app/track/` POST) | 1.000 / 600.000 / 86.400.000 | 1.000 / 600.000 / 86.400.000 | 1.000 / 600.000 / 86.400.000 | 1.000 / 600.000 / 86.400.000 |
| `/app/batch/` POST | 1.000 / 600.000 / 86.400.000 | 1.000 / 600.000 / 86.400.000 | 1.000 / 600.000 / 86.400.000 | 1.000 / 600.000 / 86.400.000 |
| Web Events (`/pixel/track/` POST) | 1.000 / 600.000 / 86.400.000 | 1.000 / 600.000 / 86.400.000 | 1.000 / 600.000 / 86.400.000 | 1.000 / 600.000 / 86.400.000 |
| `/pixel/batch/` POST | 1.000 / 600.000 / 86.400.000 | 1.000 / 600.000 / 86.400.000 | 1.000 / 600.000 / 86.400.000 | 1.000 / 600.000 / 86.400.000 |
| Offline Events (`/offline/track/` POST) | 1.000 / 600.000 / 86.400.000 | 1.000 / 600.000 / 86.400.000 | 1.000 / 600.000 / 86.400.000 | 1.000 / 600.000 / 86.400.000 |
| `/offline/batch/` POST | 1.000 / 600.000 / 86.400.000 | 1.000 / 600.000 / 86.400.000 | 1.000 / 600.000 / 86.400.000 | 1.000 / 600.000 / 86.400.000 |
| Streaming API | 10.000 / 600.000 / 864.000.000 | 20.000 / 1.200.000 / 1.728.000.000 | 30.000 / 1.800.000 / 2.592.000.000 | 50.000 / 3.000.000 / 4.320.000.000 |
| `/campaign/copy/task/create/` | 1 / 30 / 432.000 | 1 / 30 / 432.000 | 1 / 30 / 432.000 | 1 / 30 / 432.000 |
| `/campaign/copy/task/check/` | 2 / 60 / 864.000 | 2 / 60 / 864.000 | 2 / 60 / 864.000 | 2 / 60 / 864.000 |
| `/gmv_max/report/get/` | 8 / 240 / 80.000 | 12 / 360 / 120.000 | 20 / 600 / 200.000 | 20 / 600 / 200.000 |

### Thực tiễn tốt nhất (`Best practices`)

Để tránh tình trạng yêu cầu bị điều tiết tốc độ (throttled) và sử dụng tài nguyên hiệu quả hơn, bạn có thể gửi yêu cầu hàng loạt và giới hạn số lượng yêu cầu đồng thời.

#### 1. Gửi yêu cầu hàng loạt (`Make bulk requests`)

Các endpoint dạng đọc (`GET`) cho phép gửi yêu cầu hàng loạt. Với một yêu cầu duy nhất, bạn có thể thao tác trên nhiều dữ liệu cùng lúc thay vì thực hiện từng yêu cầu riêng lẻ cho từng mục dữ liệu. Điều này giúp giảm đáng kể tổng số lệnh gọi API.

Ví dụ: bạn có thể lấy thông tin nhiều nhóm quảng cáo (`ad groups`) bằng cách truyền danh sách nhiều `adgroup_ids` thay vì thực hiện nhiều yêu cầu riêng rẽ với từng `adgroup_ids`.

**Khuyến nghị (Recommended)**:

```bash
curl --get -H "Access-Token:xxx" \
  --data-urlencode "advertiser_id={{ADVERTISER_ID}}" \
  --data-urlencode "filtering={\"adgroup_ids\": [ADGROUP_ID1,ADGROUP_ID2,ADGROUP_ID3,...]}" \
  --data-urlencode "page=1" \
  --data-urlencode "page_size=100" \
  https://ads.tiktok.com/open_api/2/adgroup/get/
```

**Không khuyến nghị (Not recommended)**:

```bash
for ADGROUP_ID in {ADGROUP_ID1,ADGROUP_ID2,ADGROUP_ID3,...} do
  curl --get -H "Access-Token:xxx" \
    --data-urlencode "advertiser_id={{ADVERTISER_ID}}" \
    --data-urlencode "filtering={\"adgroup_ids\": [$ADGROUP_ID]}" \
    --data-urlencode "page=1" \
    --data-urlencode "page_size=1" \
    https://ads.tiktok.com/open_api/2/adgroup/get/
done
```

#### 2. Giới hạn số lượng yêu cầu đồng thời (`Limit the number of concurrent requests`)

Đối với dữ liệu cần đồng bộ theo thời gian thực, nếu gọi đồng thời một lượng lớn giao diện API, yêu cầu có thể bị điều tiết tốc độ (throttled).

Trong trường hợp này, bạn có thể triển khai cơ chế Giới hạn tốc độ ([Rate Limiting](https://en.wikipedia.org/wiki/Rate_limiting)) ở phía client để kiểm soát số lượng yêu cầu đồng thời. Một ví dụ điển hình là Thuật toán thùng mã thông báo ([Token Bucket Algorithm](https://en.wikipedia.org/wiki/Token_bucket)). Các token được cấp phát theo quy tắc giới hạn tốc độ (ví dụ: cấp 10 token mỗi giây). Trước khi gửi yêu cầu, client cần lấy được token; nếu hiện không có token khả dụng, hãy chờ một khoảng thời gian rồi thử lại.

Một giải pháp mạnh mẽ hơn là sử dụng Hàng đợi thông điệp ([Message Queuing](https://en.wikipedia.org/wiki/Message_queue)). Tập lệnh hẹn giờ không trực tiếp gửi yêu cầu tới API mà sử dụng mô hình [nhà sản xuất - người tiêu dùng](https://en.wikipedia.org/wiki/Producer–consumer_problem) (producer-consumer). Công việc cần gửi sẽ được đẩy vào hàng đợi thông điệp, và một tiến trình tiêu thụ chuyên dụng sẽ lấy tác vụ ra khỏi hàng đợi để thực hiện yêu cầu API. Bạn có thể giới hạn số lượng tác vụ đồng thời bằng cách giới hạn số tiến trình tiêu thụ hoặc áp dụng giới hạn tốc độ gọi. Những tác vụ thất bại có thể được đẩy ngược lại vào hàng đợi (kèm theo một độ trễ nhất định) để thử lại sau.


---

## Quyền ứng dụng (`App permissions`)
<a id="doc-1738855280338946"></a>
<!-- doc_id: 1738855280338946 -->

> Đường dẫn: Get Started > App permissions

Tham khảo **Tài liệu tham khảo API** để xem danh sách tất cả các endpoint hiện có cùng quyền hạn tương ứng.

### Cập nhật quyền ứng dụng (`Update app permissions`)

Nếu bạn cần điều chỉnh quyền hạn của mình, bạn không cần phải tạo một ứng dụng nhà phát triển mới hoặc gửi phiếu yêu cầu hỗ trợ (ticket) tại Cổng thông tin hỗ trợ nhà phát triển. Bạn hoàn toàn có thể tự cập nhật các quyền này.

Để thực hiện, vui lòng làm theo các bước sau:
1. Sau khi đăng nhập, nhấp vào **My Apps** và chọn tên ứng dụng nhà phát triển bạn muốn cập nhật.
2. Sau khi chọn, nhấp vào **Scope of permission**.
3. Nhấp vào biểu tượng chỉnh sửa (edit icon) và chọn các quyền mới bạn muốn đăng ký.
4. Vui lòng điền lý do tại sao bạn muốn cập nhật quyền và nhấp vào **Submit**. Đảm bảo rằng lý do giải trình việc mở rộng phạm vi quyền phù hợp với các phạm vi mới được chọn. Dưới đây là ví dụ tham khảo:
   > *Các nhà quản lý chiến dịch của chúng tôi mất nhiều thời gian để tải tài sản sáng tạo lên các tài khoản quảng cáo theo cách thủ công. Chúng tôi muốn tích hợp API để tải lên nội dung sáng tạo, xây dựng khả năng tự động hóa việc tải sáng tạo nhằm tiết kiệm thời gian cho các nhà quản lý chiến dịch.*
5. Đơn đăng ký của bạn sẽ được đội ngũ TikTok xét duyệt. Lưu ý rằng quá trình này có thể mất từ 2 đến 3 ngày làm việc.

---

## Tài khoản Sandbox (`Sandbox accounts`)
<a id="doc-1738855331457026"></a>
<!-- doc_id: 1738855331457026 -->

> Đường dẫn: Get Started > Sandbox accounts

Với tài khoản sandbox của TikTok API for Business, bạn có thể dễ dàng kiểm thử hoạt động tích hợp mà không làm ảnh hưởng đến tài khoản TikTok For Business thực tế của mình.

> [!NOTE]
> Nếu bạn đã tạo tài khoản sandbox trước ngày 4 tháng 11 năm 2020, bạn bắt buộc phải tạo tài khoản sandbox mới vì ID nhà quảng cáo và access token cũ không còn hiệu lực.

Với tài khoản sandbox của TikTok, nhà phát triển có thể:
- Sử dụng hầu hết các endpoint API hiện được cung cấp trong môi trường sản xuất (production) của TikTok API for Business. Xem danh sách các endpoint được hỗ trợ bên dưới.
- Lấy dữ liệu báo cáo giả lập (mock reporting data).
- Tạo một tài khoản sandbox cho mỗi ứng dụng nhà phát triển đã tạo.

> [!NOTE]
> • Quyền hạn của tài khoản sandbox mà bạn có ở cấp ứng dụng sẽ tự động được phản ánh thành quyền hạn trên tài khoản sandbox.<br>
> • Trong môi trường sandbox, giới hạn tốc độ gọi cho mỗi endpoint như sau: 1 QPS (truy vấn mỗi giây), 30 QPM (truy vấn mỗi phút) và 1.000 QPD (truy vấn mỗi ngày). Ví dụ: nếu bạn gửi yêu cầu tới 5 endpoint khác nhau, bạn có thể gửi tối đa 5 yêu cầu (1 yêu cầu cho mỗi endpoint) trong vòng 1 giây.

### Base URL cho môi trường sandbox (`Base URL for the sandbox environment`)

Định dạng URL cho các endpoint API có cấu trúc chuẩn.

Base URL cho môi trường **Sandbox** là:
```http
https://sandbox-ads.tiktok.com/open_api
```

Base URL cho môi trường **Production** (Sản xuất) là:
```http
https://business-api.tiktok.com/open_api
```

Base URL của môi trường Production được sử dụng trong phần mô tả của từng endpoint. Để gửi yêu cầu tới các endpoint trong môi trường Sandbox, hãy thay thế base URL thành base URL của Sandbox.

Sau khi thiết lập tài khoản Sandbox, bạn có thể thực hiện các lệnh gọi API tới các endpoint trong môi trường Sandbox.

### Thiết lập tài khoản sandbox của bạn (`Setting up your sandbox account`)

Việc thiết lập Tài khoản Sandbox rất dễ dàng. Như đã nêu ở trên, Tài khoản Sandbox có thể được tạo cho từng Ứng dụng bạn đã tạo thông qua TikTok API for Business. Để tạo tài khoản Sandbox, hãy làm theo hướng dẫn bên dưới:

1. Điều hướng tới [Trang chủ TikTok API for Business](https://ads.tiktok.com/marketing_api/homepage) và nhấp vào **Go to my apps**.
2. Nhấp vào Ứng dụng nhà phát triển mà bạn muốn tạo Tài khoản Sandbox bên dưới.
3. Nhấp vào **Create a Sandbox Ad Account**.
4. Điền các thông tin chi tiết cho tài khoản sandbox của bạn, bao gồm tên, quốc gia tài khoản quảng cáo, đơn vị tiền tệ và múi giờ của tài khoản quảng cáo. Sau đó nhấp vào **Create**.
5. Sau khi tạo xong, nhà phát triển có thể tạo access token và xem ID nhà quảng cáo (`advertiser_id`) của mình.

### Dữ liệu giả lập cho báo cáo đồng bộ (`Mock data for synchronous reporting`)

Để giúp nhà phát triển dễ dàng kiểm thử khả năng Báo cáo (Reporting), chúng tôi đã nạp sẵn dữ liệu giả lập (mock data) trong tất cả các tài khoản sandbox.

Dữ liệu giả lập chỉ phục vụ mục đích kiểm thử và minh họa. Định dạng dữ liệu hoàn toàn giống với dữ liệu thực tế, nhưng không dựa trên cài đặt chiến dịch quảng cáo thực tế của bạn. Ví dụ: khi chạy báo cáo tệp đối tượng để lấy mã quốc gia cho các vị trí có dữ liệu chi tiêu, các vị trí trả về có thể khác với vị trí mà quảng cáo thực sự được triển khai.

Lưu ý rằng dữ liệu giả lập không hỗ trợ báo cáo bất đồng bộ (asynchronous reports).

Để sử dụng dữ liệu giả lập, hãy gửi một yêu cầu `GET` tới endpoint `https://sandbox-ads.tiktok.com/open_api/v1.3/report/integrated/get/`. Chúng tôi khuyên bạn nên tạo ít nhất một chiến dịch, một nhóm quảng cáo và một quảng cáo trong tài khoản sandbox của mình. Dữ liệu giả lập có thể chỉ trả về các giá trị mặc định (ví dụ: `"0"`) cho các chỉ số được truy vấn hoặc trả về kết quả trống (`"list": []`).

#### Cài đặt được hỗ trợ (`Supported settings`)

- Khoảng thời gian (Time range): `2020/12/08` - `2020/12/19`.
- `service_type`: `AUCTION`.
- `report_type`: `BASIC`, `AUDIENCE`.
- `data_level`: `AUCTION_CAMPAIGN`, `AUCTION_ADGROUP`, `AUCTION_AD`.
- `dimensions`: Tất cả `dimensions` được hỗ trợ cho `report_type` tương ứng.
- `metrics`: Tất cả `metrics` được hỗ trợ cho `report_type` tương ứng. Một số chỉ số có thể trả về `0` hoặc `-`.
- `filters`: Tất cả `filters` được hỗ trợ cho `report_type` tương ứng.
- `lifetime`: Hỗ trợ giá trị `true`.
- `order_field` & `order_type`: KHÔNG hỗ trợ sắp xếp thứ tự.

#### Ví dụ (`Example`)

**Yêu cầu (Request)**:

```bash
curl --location --request GET 'https://sandbox-ads.tiktok.com/open_api/v1.3/report/integrated/get/?advertiser_id={{advertiser_id}}&report_type=BASIC&dimensions=["adgroup_id"]&service_type=AUCTION&data_level=AUCTION_ADGROUP&start_date=2020-12-11&end_date=2020-12-19&metrics=["spend"]&page_size=1' \
  --header 'Access-Token: {{Access-Token}}'
```

**Phản hồi (Response)**:

```json
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "page_info": {
            "total_number": 1,
            "page": 1,
            "page_size": 1,
            "total_page": 1
        },
        "list": [
            {
                "metrics": {
                    "spend": "0"
                },
                "dimensions": {
                    "adgroup_id": "{{adgroup_id}}"
                }
            }
        ]
    }
}
```

### Các endpoint được hỗ trợ trong tài khoản sandbox (`Endpoints supported in sandbox accounts`)

Danh sách dưới đây tổng hợp các endpoint được hỗ trợ trong tài khoản sandbox:

> [!NOTE]
> Môi trường sandbox đang được nâng cấp liên tục, và mục tiêu dài hạn là hỗ trợ tất cả các endpoint trong tài khoản sandbox.

| Endpoints supported in sandbox accounts |
|---|
| `/ad/create/` |
| `/ad/get/` |
| `/ad/update/` |
| `/ad/status/update/` |
| `/adgroup/create/` |
| `/adgroup/get/` |
| `/adgroup/update/` |
| `/adgroup/status/update/` |
| `/campaign/create/` |
| `/campaign/get/` |
| `/campaign/update/` |
| `/campaign/status/update/` |
| `/file/image/ad/upload/` |
| `/file/video/ad/upload/` |
| `/report/integrated/get/` (GET) |
| `/term/check/` |
| `/term/confirm/` |
| `/term/get/` |
| `/user/info/` |
| `/identity/create/` |
| `/identity/get/` |
| `/identity/delete/` |

---

## Bộ sưu tập Postman (`Postman collection`)
<a id="doc-1747849403155521"></a>
<!-- doc_id: 1747849403155521 -->

> Đường dẫn: Get Started > Postman collection

Chúng tôi cung cấp một bộ sưu tập Postman cho các endpoint API của chúng tôi.

Vui lòng nhấp [vào đây](https://tiktok.postman.co/workspace/TikTok-API-For-Business~cf223b0e-a943-4e26-8443-b8618153a70a/collection/33151601-6700a660-d048-429b-9626-500e2f29b7a4?action=share&creator=33151601) để tải bộ sưu tập về và tùy chỉnh để thực thi các yêu cầu API. Lưu ý rằng đây không phải là danh sách toàn bộ các endpoint API của chúng tôi.

---

## Thời gian tích hợp ước tính (`Estimated integration time`)
<a id="doc-1768657234981890"></a>
<!-- doc_id: 1768657234981890 -->

> Đường dẫn: Get Started > Estimated integration time

Bài viết này giới thiệu thời gian tích hợp ước tính cần thiết cho một số trường hợp sử dụng (use cases) tích hợp API phổ biến. Nếu bạn có nhu cầu tích hợp, thông tin dưới đây sẽ giúp bạn nắm bắt thời gian trung bình cần thiết và lập kế hoạch tích hợp phù hợp.

Dựa trên phản hồi từ hàng trăm nhà phát triển trong một cuộc khảo sát gần đây, chúng tôi đã tính toán **tổng số giờ tích hợp trung bình** (cột thứ 2 trong bảng bên dưới) và **số lượng nhà phát triển cần thiết** (cột thứ 3 trong bảng bên dưới) trong các trường hợp sử dụng sau. Đối với mỗi dự án tích hợp, tổng số giờ tích hợp là tổng thời gian làm việc của tất cả các nhà phát triển tham gia vào dự án đó. Ví dụ: **Campaign Creation** (Tạo chiến dịch) mất tổng cộng trung bình 61,16 giờ và cần 2,51 nhà phát triển.

> [!NOTE]
> Các kết quả này không mang tính tuyệt đối và chỉ nhằm mục đích tham khảo. Thời gian tích hợp cần được xem xét theo từng trường hợp cụ thể vì thời gian thực tế phụ thuộc vào nhiều yếu tố như kiến thức về sản phẩm của nhà phát triển và kinh nghiệm tích hợp trước đó.

> [!IMPORTANT]
> Nếu bạn muốn rút ngắn thời gian tích hợp, chúng tôi khuyên bạn nên sử dụng các giải pháp [SDK](../16-sdk/sdk.md#doc-1764231376750658) của chúng tôi.

| Use Case | Tổng số giờ tích hợp trung bình | Số lượng nhà phát triển cần thiết |
|---|---|---|
| **Ad Measurement** | 27.75 | 1.38 |
| **Audience Management** | 32.17 | 2.06 |
| **Business Center** | 57.71 | 3.01 |
| **Campaign Creation** | 61.16 | 2.51 |
| **Campaign Modification** | 12.00 | 1.00 |
| **Creative Management** | 17.67 | 5.89 |
| **Reporting** | 45.19 | 1.59 |
| **Authentication** | 20.00 | 1.20 |

---

## Cần hỗ trợ (`Need support`)
<a id="doc-1795190020378625"></a>
<!-- doc_id: 1795190020378625 -->

> Đường dẫn: Get Started > Need support

Nếu bạn gặp phải bất kỳ sự cố nào trong quá trình tích hợp, trước tiên chúng tôi khuyên bạn nên tham khảo [Câu hỏi thường gặp (FAQs)](../07-faqs/faq.md#doc-1740029175352322) hoặc tìm kiếm câu trả lời trong tài liệu hướng dẫn của chúng tôi. Nếu bạn vẫn không tìm thấy giải pháp mình cần, vui lòng cân nhắc các phương thức sau:

- **Sự cố kỹ thuật (Technical issues)**: Đối với các vấn đề liên quan đến tích hợp hoặc các khó khăn kỹ thuật khác, vui lòng **gửi phiếu yêu cầu (submit a ticket)** trên [Nền tảng hỗ trợ nhà phát triển (Developer Ticket Platform)](https://ads.tiktok.com/athena/requester/boards?identify_key=b25033ef7782d41050cbac74f751d547e9d8ad35a39a541a0f0efbbd51fe722f). Đội ngũ hỗ trợ của chúng tôi luôn tận tâm giải quyết các thắc mắc của bạn trong thời gian sớm nhất.

- **Vấn đề về tài liệu (Documentation issues)**: Nếu bạn phát hiện bất kỳ sự cố nào với tài liệu của chúng tôi (chẳng hạn như thiếu thông tin, thông tin không chính xác hoặc gây nhầm lẫn, liên kết bị hỏng hoặc lỗi chính tả), chúng tôi rất trân trọng phản hồi của bạn. Vui lòng nhấp vào **cửa sổ phản hồi ở góc dưới bên phải** và cung cấp thông tin chi tiết về sự cố gặp phải.
