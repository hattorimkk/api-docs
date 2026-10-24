# Phụ lục: mã lỗi, enum, quyền, múi giờ… — phần 1/2

Tài liệu này tổng hợp toàn bộ thông tin tra cứu quan trọng của TikTok API for Business, bao gồm danh mục phụ lục, mã trả về (Return codes), mã trạng thái HTTP (HTTP status codes), bảng tổng hợp giá trị enum, phân cấp phạm vi quyền hạn (Permission scopes), mã vị trí địa lý, múi giờ, danh mục sở thích, ID ngành hàng, độ chính xác tiền tệ, chính sách quảng cáo và các quy định kỹ thuật liên quan.

---

## Phụ lục (`Appendix`)
<a id="doc-1737172315193346"></a>
<!-- doc_id: 1737172315193346 -->

> Đường dẫn: Appendix

Chương này liệt kê các bài viết phụ lục tra cứu kỹ thuật:

* [Mã trả về (Return Codes)](phu-luc-p1.md#doc-1737172488964097)
* [Mã trạng thái HTTP (HTTP Status Codes)](phu-luc-p1.md#doc-1749734684478466)
* [Bảng giá trị Enum (Enumerations)](phu-luc-p1.md#doc-1737174886619138)
* [Phạm vi quyền hạn (Permission scope)](phu-luc-p1.md#doc-1753986142651394)
* **Location IDs**
* [Mã vị trí (Location code)](phu-luc-p1.md#doc-1737585867307010)
* [Múi giờ (Time zone)](phu-luc-p1.md#doc-1737586324313089)
* [Danh mục sở thích (Interest category)](phu-luc-p1.md#doc-1738865030529025)
* **Ngành hàng (Industries)**
* [Độ chính xác theo từng loại tiền tệ (Currency-specific precision)](phu-luc-p1.md#doc-1772544628718594)
* [Đối chiếu giữa các loại quảng bá khác nhau (Mapping between different promotion types)](phu-luc-p1.md#doc-1758485431181314)
* [Loại trang đích có thể lọc theo mục tiêu quảng cáo (Filterable destination page type for an advertising objective)](phu-luc-p1.md#doc-1764306884771842)
* [Chính sách quảng cáo (Advertising Policies)](phu-luc-p1.md#doc-1759238007931906)
* [Tính duy nhất của Object ID (Object ID uniqueness)](phu-luc-p1.md#doc-1792139804568578)
* [Tổ hợp nội dung sáng tạo quảng cáo Upgraded Smart+ theo danh tính và loại quảng cáo (Upgraded Smart+ ad creative combinations by identity and ad type)](phu-luc-p1.md#doc-1847839781968897)
* [Cài đặt nhắm mục tiêu khả dụng cho các chế độ tối ưu hóa nhắm mục tiêu trong Upgraded Smart+ Ad Groups](phu-luc-p2.md#doc-1847839827327106)

---

## Mã trả về (`Return codes`)
<a id="doc-1737172488964097"></a>
<!-- doc_id: 1737172488964097 -->

> Đường dẫn: Appendix > Return codes

Mã trả về (return codes) của TikTok API for Business là các mã trạng thái duy nhất được thiết kế riêng để phản ánh trạng thái của lệnh gọi API và cung cấp thông tin về nguyên nhân thất bại nếu lệnh gọi không thành công.

Các mã trả về này có mức độ ưu tiên cao hơn mã trạng thái HTTP (HTTP status codes) trong việc xác định xem một lệnh gọi tới endpoint TikTok API for Business có thành công hay không. Ví dụ: một phản hồi có mã trạng thái HTTP `200` đi kèm mã trả về `40002` thể hiện lệnh gọi thất bại, vì mã trả về `40002` thuộc nhóm mã trả về khi không thành công. Để tìm hiểu thêm về các hành động khuyến nghị cho từng mã trạng thái HTTP, hãy tham khảo [Mã trạng thái HTTP (HTTP Status Codes)](phu-luc-p1.md#doc-1749734684478466).

Các bảng dưới đây giới thiệu phương pháp xử lý lỗi khuyến nghị, thông báo lỗi mẫu và nguyên nhân chính gây ra các mã lỗi phổ biến. Nếu bạn gặp khó khăn trong việc tự xử lý lỗi và cần đội ngũ hỗ trợ kỹ thuật, hãy gửi ticket tại [Nền tảng gửi Ticket dành cho nhà phát triển (Developer Ticket Platform)](https://ads.tiktok.com/athena/requester/boards?identify_key=b25033ef7782d41050cbac74f751d547e9d8ad35a39a541a0f0efbbd51fe722f).

### Mã trả về cho lệnh gọi thành công

| Code | Mô tả |
|---|---|
| 0 | Thành công (`Successful`) |
| 20001 | Thành công một phần (`Partially successful`) |

### Mã trả về cho lệnh gọi không thành công

> [!NOTE]
> • Các mã trả về bắt đầu bằng chữ số 5 (ví dụ: `51003`) cho biết lỗi dịch vụ phía máy chủ, bạn có thể tham khảo trường `message` trong phản hồi để biết chi tiết.<br>
> • Lỗi HTTP `404 page not found` có thể xảy ra trong các trường hợp sau:<br>
> - Sử dụng sai phương thức API (API method). Ví dụ: endpoint yêu cầu phương thức `GET` nhưng bạn lại gửi yêu cầu `POST`.<br>
> - Sử dụng sai đường dẫn API (API path). Ví dụ: đường dẫn endpoint chính xác là `/tt_user/oauth2/refresh_token/`, nhưng bạn lại gọi tới `/tt_user/oauth2/refresh_token` (thiếu dấu gạch chéo `/` ở cuối).

#### Chung (`General`)

| Code | Mô tả |
|---|---|
| 40000 | Các tham số cung cấp không hợp lệ.<br>**Xử lý lỗi**: Tham khảo tài liệu API để biết cách sử dụng đúng tham số và thử lại. |
| 40001 | Không có quyền thực hiện thao tác liên quan.<br>**Thông báo lỗi mẫu**: `You don't have permission to operate this catalog:{catalog_id}.`<br>**Xử lý lỗi**: Đảm bảo bạn có đầy đủ quyền hạn cần thiết và thử lại. Để tìm hiểu về các cấp phạm vi quyền hạn, xem [Phạm vi quyền hạn (Permission scope)](phu-luc-p1.md#doc-1753986142651394). |
| 40002 | Lỗi tham số. Vui lòng xem thông báo lỗi để biết chi tiết.<br>**Nguyên nhân phổ biến**:<br>• Thiếu các trường bắt buộc.<br>• Định dạng giá trị trường không chính xác.<br>• Trường hoặc giá trị trường không được hỗ trợ.<br>• Không tương thích giữa các trường hoặc giá trị trường được truyền vào.<br>• Độ chính xác dữ liệu không hợp lệ.<br>• Giá trị số không hợp lệ.<br>• Tệp đối tượng (`audience`).<br>• **Thông báo lỗi mẫu**: `Audience is not editable, please check audience status.`<br>• **Nguyên nhân phổ biến**: 1. Tệp đối tượng được tạo với quy mô bằng 0 (khớp dưới 1.000 người). 2. Tệp đối tượng hiện đang được cập nhật hoặc đang xử lý.<br>• **Xử lý lỗi**: Đảm bảo quy mô tệp đối tượng đủ lớn, kiểm tra trạng thái tệp đối tượng và thử lại.<br>**Thông báo lỗi mẫu**: `Time format should be %Y-%m-%dT%H:%M. Please try again.`<br>**Xử lý lỗi**: Tham khảo tài liệu API để biết cách sử dụng tham số chính xác và thử lại. |
| 40006 | Phiên bản API được chỉ định không tương thích với các tham số cung cấp.<br>**Nguyên nhân phổ biến**:<br>• Sử dụng sản phẩm không được hỗ trợ trong phiên bản API được chỉ định.<br>• Sử dụng phiên bản API không tồn tại.<br>**Thông báo lỗi mẫu**: `The old API version does not support DPA ad.`<br>**Xử lý lỗi**: Đảm bảo bạn đang sử dụng phiên bản API hiện tại phù hợp với các tham số cung cấp và thử lại. |
| 40010 | Tên miền không được hỗ trợ trong phiên bản API hiện tại.<br>**Xử lý lỗi**: Đảm bảo `base_url` trong URL yêu cầu là chính xác (`https://business-api.tiktok.com/open_api`) và thử lại. Để biết định dạng URL yêu cầu, xem **API Reference-Request URL format**. |
| 40051 | Phiên bản API không hợp lệ.<br>**Xử lý lỗi**: Đảm bảo bạn sử dụng đúng phiên bản API và thử lại. |
| 40007 | Thao tác hoặc đối tượng không tồn tại.<br>**Nguyên nhân phổ biến**:<br>• Chỉ định đối tượng (chiến dịch, nhóm quảng cáo, quảng cáo...) không tồn tại.<br>• Chỉ định URL đã ngừng hoạt động hoặc tệp tin không tồn tại.<br>**Thông báo lỗi mẫu**: `The ad {} does not exist.`<br>**Xử lý lỗi**: Đảm bảo đối tượng bạn thao tác đang tồn tại và xác thực lại mọi URL sử dụng, sau đó thử lại. |
| 40008 | Giao diện (endpoint) chưa được triển khai.<br>**Nguyên nhân phổ biến**:<br>• Sử dụng endpoint không tồn tại.<br>• Sử dụng endpoint không được hỗ trợ trong môi trường sandbox.<br>**Xử lý lỗi**: Đảm bảo đường dẫn endpoint là chính xác và thử lại. Khi kiểm thử trong sandbox, chỉ sử dụng các endpoint được hỗ trợ. Tham khảo [Sandbox accounts - Endpoints supported in sandbox accounts](../04-get-started/bat-dau.md#doc-1738855331457026). |
| 40009 | Tham số hoặc phương thức không được hỗ trợ trong sandbox.<br>**Thông báo lỗi mẫu**: `Unsupported data_level in sandbox environment: %s.`<br>**Xử lý lỗi**: Đảm bảo giá trị tham số được hỗ trợ trong môi trường sandbox và thử lại. |
| 40011 | Quá nhiều ID được cung cấp trong một yêu cầu duy nhất.<br>**Xử lý lỗi**: Giảm tổng số ID truy vấn trong một yêu cầu, hoặc chia nhỏ danh sách ID thành nhiều đợt (batch) để truy vấn qua nhiều yêu cầu, sau đó thử lại. |
| 40013 | Tài khoản sandbox không tồn tại.<br>**Xử lý lỗi**: Tham khảo [Tài khoản Sandbox (Sandbox accounts)](../04-get-started/bat-dau.md#doc-1738855331457026) để biết cách thiết lập tài khoản sandbox và thử lại. |
| 40014 | Tính năng, thao tác hoặc endpoint được yêu cầu không được hỗ trợ trong môi trường sandbox.<br>**Xử lý lỗi**: Tham khảo [Tài khoản Sandbox (Sandbox accounts)](../04-get-started/bat-dau.md#doc-1738855331457026) để biết danh sách tính năng và endpoint hỗ trợ trong sandbox. Nếu tính năng không hỗ trợ trong sandbox, bạn cần kiểm thử trong môi trường thực tế (production). |
| 40050 | Yêu cầu trùng lặp đã được gửi. |
| 40052 | Tài liệu ACO (Tối ưu hóa nội dung sáng tạo tự động) đã tồn tại.<br>**Xử lý lỗi**: Tham khảo tài liệu Tối ưu hóa nội dung sáng tạo tự động (Automated Creative Optimization) và Tạo quảng cáo ACO để xem hướng dẫn từng bước. |
| 40053 | Video ID không hợp lệ.<br>**Xử lý lỗi**: Đảm bảo bạn sử dụng Video ID hợp lệ và thử lại. Để lấy Video ID hợp lệ, bạn có thể gọi [/file/video/ad/info/](../12-api-reference/71-video.md#doc-1740050161973250) hoặc [/file/video/ad/search/](../12-api-reference/71-video.md#doc-1740050472224769). |

#### Liên quan đến giới hạn tốc độ gọi hoặc hạn ngạch (`Rate limit or quota related`)

| Code | Mô tả |
|---|---|
| 40016 | Yêu cầu được gửi quá thường xuyên.<br>**Nguyên nhân phổ biến**: Giới hạn tốc độ gọi (rate limit) của endpoint ở cấp ứng dụng nhà phát triển (developer application) đã bị chạm ngưỡng, do đó yêu cầu bị điều tiết (throttled).<br>**Xử lý lỗi**: Tham khảo [Giới hạn tốc độ gọi (Rate limits)](../04-get-started/bat-dau.md#doc-1740029171730433) để tìm hiểu giới hạn toàn cục và theo từng endpoint. |
| 40100 | Yêu cầu được gửi quá thường xuyên.<br>**Nguyên nhân phổ biến**: Đã chạm giới hạn tốc độ gọi của endpoint ở cấp ứng dụng nhà phát triển, yêu cầu bị điều tiết.<br>**Xử lý lỗi**: Tham khảo [Giới hạn tốc độ gọi (Rate limits)](../04-get-started/bat-dau.md#doc-1740029171730433) để tìm hiểu về giới hạn toàn cục và theo từng endpoint. |
| 40133 | Yêu cầu được gửi quá thường xuyên.<br>**Nguyên nhân phổ biến**: Đã chạm giới hạn tốc độ gọi của endpoint ở cấp tài khoản nhà quảng cáo (advertiser), yêu cầu bị điều tiết.<br>**Thông báo lỗi mẫu**: `Advertiser ({ID})'s QPS ({current QPS}) reaches QPS limit {QPS limit} for current path, request is temporarily restricted.`<br>**Xử lý lỗi**: Giảm số lượng lệnh gọi API trên mỗi giây từ tài khoản nhà quảng cáo tới endpoint đó. |
| 40502 | Đã đạt số lượng quảng cáo tối đa cho phép.<br>**Xử lý lỗi**: Thử tạo quảng cáo trong nhóm quảng cáo hoặc chiến dịch khác, hoặc xóa bớt các quảng cáo hiện có. |
| 40132 | Yêu cầu được gửi quá thường xuyên đối với một giá trị trường nhất định.<br>**Nguyên nhân phổ biến**: Mã pixel (`pixel_code`) truyền trong [/pixel/track/](../12-api-reference/43-events-1-0-p1.md#doc-1740858531237890) hoặc [/pixel/batch/](../12-api-reference/43-events-1-0-p1.md#doc-1740858565852225) đã bị từ chối do: • bạn đã sử dụng pixel này trong quá nhiều lệnh gọi dẫn đến việc áp đặt giới hạn QPS lên `pixel_code`, hoặc • access token của bạn có thể đã bị rò rỉ và bị lạm dụng cho các cuộc tấn công độc hại.<br>**Thông báo lỗi mẫu**: `The request QPS is limited by pixel_code's value.`<br>**Xử lý lỗi**: Thử lại với giá trị trường mới cho trường được đề cập trong thông báo lỗi, hoặc gửi ticket lên [Developer Ticket Platform](https://ads.tiktok.com/athena/requester/boards?identify_key=b25033ef7782d41050cbac74f751d547e9d8ad35a39a541a0f0efbbd51fe722f). |

#### Liên quan đến xác thực (`Authentication related`)

| Code | Mô tả |
|---|---|
| 40110 | Mã ủy quyền (authorization code) không hợp lệ.<br>**Nguyên nhân phổ biến**: Mã ủy quyền đã bị hủy, đã được sử dụng hoặc đã hết hạn.<br>**Thông báo lỗi mẫu**: `The auth_code is canceled. Please re-authorize and try again with a new auth_code.`<br>**Xử lý lỗi**: Sử dụng mã ủy quyền hợp lệ và thử lại.<br>Để biết cách lấy mã ủy quyền cho Marketing API, xem [Ủy quyền (Authorization)](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373141733378).<br>Để biết cách lấy mã ủy quyền cho Accounts API hoặc TikTok Creator Marketplace API, xem [Accounts-Authorization](../10-organic-api/accounts-api.md#doc-1738083939371009) và **Creator Marketplace-Get authorization from creators**. |
| 40101 | Giá trị tham số xác thực không hợp lệ.<br>**Nguyên nhân phổ biến**:<br>• Secret và App ID không khớp nhau.<br>• Mã ủy quyền không hợp lệ.<br>**Thông báo lỗi mẫu**: `Invalid auth_code. Not able to get long-term access_token with an old auth_code. Please retry with the old auth_code.`<br>**Xử lý lỗi**: Đảm bảo bạn sử dụng các giá trị hợp lệ để xác thực và thử lại.<br>Để tạo access token dài hạn cho Marketing API, xem [Xác thực (Authentication)](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162).<br>Để tạo access token cho Accounts API hoặc TikTok Creator Marketplace API, xem [Accounts-Authentication](../10-organic-api/accounts-api.md#doc-1738084387220481) và **Creator Marketplace-Get authorization from creators**. |
| 40102 | Access token đã hết hạn. Endpoint cần được gọi với access token mới nhất.<br>**Xử lý lỗi**: Sử dụng access token hợp lệ và thử lại.<br>Để tạo access token dài hạn cho Marketing API, xem [Xác thực (Authentication)](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162).<br>Để tạo access token cho Accounts API hoặc TikTok Creator Marketplace API, xem [Accounts-Authentication](../10-organic-api/accounts-api.md#doc-1738084387220481) và **Creator Marketplace-Get authorization from creators**. |
| 40104 | Access token bị bỏ trống.<br>**Xử lý lỗi**: Truyền access token hợp lệ vào yêu cầu và thử lại. |
| 40105 | Access token không hợp lệ hoặc không chính xác.<br>**Xử lý lỗi**: Sử dụng access token hợp lệ và thử lại. |
| 40106 | Người dùng cốt lõi (core user) không hợp lệ.<br>**Xử lý lỗi**: Đảm bảo bạn đang sử dụng access token hợp lệ (`Access-Token`) cho ID nhà quảng cáo được chỉ định (`advertiser_id`) và thử lại. Xem [Xác thực (Authentication)](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| 40103 | Refresh token đã hết hạn.<br>**Xử lý lỗi**: Sử dụng refresh token hợp lệ và thử lại. Để nhận refresh token hợp lệ, hãy yêu cầu người dùng ủy quyền lại ứng dụng thông qua luồng ủy quyền người dùng. Xem [Accounts-Authentication](../10-organic-api/accounts-api.md#doc-1738084387220481) và **Creator Marketplace-Get authorization from creators**. |
| 40107 | Refresh token không hợp lệ hoặc không đúng.<br>**Nguyên nhân phổ biến**:<br>• Dùng refresh token để làm mới token dài hạn của Marketing API (Marketing API không dùng refresh token theo cách này).<br>• Dùng refresh token không hợp lệ.<br>**Xử lý lỗi**: Chỉ sử dụng refresh token hợp lệ để làm mới access token cho Accounts API hoặc TikTok Creator Marketplace API. Xem [FAQs](../10-organic-api/accounts-api.md#doc-1766042058952706). |
| 40108 | Loại cấp quyền (authorization type) không hợp lệ.<br>**Thông báo lỗi mẫu**: `Invalid value for grant_type: {grant_type} is not supported.`<br>**Xử lý lỗi**: Sử dụng giá trị hợp lệ cho `grant_type` và thử lại. Xem [Accounts-Authentication](../10-organic-api/accounts-api.md#doc-1738084387220481) và **Creator Marketplace-Get authorization from creators**. |
| 40131 | Lỗi xác thực khi gọi `/tt_user/oauth2/token/` hoặc `/tt_user/oauth2/refresh_token/`.<br>**Nguyên nhân phổ biến**:<br>• App ID hoặc Secret không chính xác.<br>• Mã ủy quyền đã hết hạn.<br>• Refresh token không hợp lệ hoặc đã hết hạn.<br>**Thông báo lỗi mẫu**: `"Authorization code is expired."`<br>**Xử lý lỗi**:<br>• Nếu gọi `/tt_user/oauth2/token/`, đảm bảo bạn dùng đúng App ID, Secret và mã ủy quyền, rồi thử lại. Xem [Accounts-Authorization](../10-organic-api/accounts-api.md#doc-1738083939371009) và [Get authorization from creators (New)](../10-organic-api/tiktok-one-api.md#doc-1768506960432130).<br>• Nếu gọi `/tt_user/oauth2/refresh_token/`, đảm bảo dùng refresh token hợp lệ và thử lại. Nếu đã hết hạn, yêu cầu người dùng ủy quyền lại. |
| 40109 | Lỗi giải mã (`Deciphering Error`). |
| 40112 | Mật khẩu cung cấp không chính xác. |
| 40113 | Ứng dụng đã bị chặn hoặc không tồn tại.<br>**Nguyên nhân phổ biến**:<br>• Sai App ID.<br>• Sai Secret của ứng dụng.<br>**Thông báo lỗi mẫu**: `The app_id is inconsistent with the token's app information. Please retry after correcting it.`<br>**Xử lý lỗi**: Tìm đúng **App ID** và **Secret** bằng cách vào **[My Apps](https://ads.tiktok.com/marketing_api/apps/)** > **App Detail** > **Basic Information**, sau đó thử lại. |
| 40115 | Dấu thời gian xác thực (authentication timestamp) đã hết hạn.<br>**Nguyên nhân phổ biến**:<br>• Mã ủy quyền không hợp lệ.<br>• Endpoint xác thực không khớp với mã ủy quyền.<br>**Xử lý lỗi**: Đảm bảo sử dụng các giá trị hợp lệ và thử lại. Xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| 40116 | Chữ ký xác thực không hợp lệ. |
| 40117 | Phương thức chỉ định không thể sử dụng. |
| 40118 | Ứng dụng hoặc nhà quảng cáo không nằm trong danh sách cho phép (allowlist) để truy cập tính năng.<br>**Nguyên nhân phổ biến**:<br>• Tính năng chỉ khả dụng cho nhà quảng cáo tại một số quốc gia/khu vực nhất định.<br>• Endpoint chỉ dành cho danh sách cho phép và bạn chưa đăng ký cấp quyền. |
| 40119 | Nhà phát triển và nhà quảng cáo không thuộc cùng một công ty.<br>**Xử lý lỗi**: Đảm bảo sử dụng access token hợp lệ (`Access-Token`) cho ID nhà quảng cáo chỉ định (`advertiser_id`) và thử lại. Xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| 40121 | Người dùng TikTok không phải là nhà sáng tạo TCM (TikTok Creator Marketplace).<br>**Nguyên nhân phổ biến**: Endpoint yêu cầu thông tin của nhà sáng tạo TCM (chẳng hạn như tên handle), nhưng thông tin cung cấp lại thuộc về người dùng không thuộc TCM.<br>**Xử lý lỗi**: Cung cấp thông tin của nhà sáng tạo TCM hoặc mời họ tham gia TCM, sau đó thử lại. Xem hướng dẫn tại **Mời nhà sáng tạo tham gia TTCM (Invite creators to join TTCM)**. |
| 40122 | Nhà sáng tạo TCM không thuộc khu vực hợp lệ.<br>**Xử lý lỗi**: Cung cấp thông tin của nhà sáng tạo TCM tại khu vực hoặc quốc gia khác và thử lại. |
| 40124 | Hồ sơ nhà phát triển chưa được điền đầy đủ và phê duyệt.<br>**Xử lý lỗi**: Truy cập https://ads.tiktok.com/marketing_api/developer/register để hoàn thiện hồ sơ. Sau khi hồ sơ được duyệt, hãy thử lại. Nếu gặp khó khăn, gửi ticket tại [Developer Ticket Platform](https://ads.tiktok.com/athena/requester/boards?identify_key=b25033ef7782d41050cbac74f751d547e9d8ad35a39a541a0f0efbbd51fe722f). |
| 40125 | Nhà phát triển không có quyền.<br>**Nguyên nhân phổ biến**:<br>• Thiếu quyền hạn cần thiết.<br>• Sử dụng các trường không được hỗ trợ.<br>**Xử lý lỗi**: Đảm bảo bạn có đầy đủ quyền và chỉ sử dụng các trường được hỗ trợ, sau đó thử lại. Xem [Phạm vi quyền hạn (Permission scope)](phu-luc-p1.md#doc-1753986142651394). |
| 41001 | Giao diện đã ngừng hoạt động (offline).<br>**Xử lý lỗi**: Đảm bảo đường dẫn endpoint là chính xác và được hỗ trợ trong phiên bản API chỉ định, sau đó thử lại. |
| 41002 | Các trường cung cấp hiện không được sử dụng.<br>**Xử lý lỗi**: Tham khảo tài liệu API để biết cách dùng đúng tham số và thử lại. |

#### Liên quan đến chính sách quảng cáo (`Advertising policy related`)

| Code | Mô tả |
|---|---|
| 40065 | Các tùy chọn nhắm mục tiêu không được hỗ trợ đối với nhóm tuổi 13–17 tại Hoa Kỳ.<br>**Thông báo lỗi mẫu**: `"Based on one or more of your choices, ad delivery to US audiences will be subject to age targeting restrictions"`<br>**Xử lý lỗi**:<br>• Nếu bạn muốn nhắm mục tiêu nhóm tuổi 13–17 tại Hoa Kỳ, đảm bảo chỉ sử dụng các tùy chọn nhắm mục tiêu được hỗ trợ và thử lại. Xem chi tiết tại [Giới hạn độ tuổi mới đối với quảng cáo trên TikTok (New age restrictions for ads on TikTok)](phu-luc-p1.md#doc-1788755983247362).<br>• Nếu bạn không muốn nhắm mục tiêu nhóm tuổi 13–17 tại Hoa Kỳ, hãy chỉ định thủ công giá trị `age_groups` không chứa `AGE_13_17` và thử lại. |

#### Lỗi tác vụ bất đồng bộ (`Async task error`)

| Code | Mô tả |
|---|---|
| 40200 | Lỗi tác vụ.<br>**Xử lý lỗi**: Tham khảo tài liệu API để biết cách sử dụng đúng tham số và thử lại. |
| 40201 | Tác vụ chưa sẵn sàng.<br>**Xử lý lỗi**: Đợi tác vụ hoàn tất rồi thử lại. |

#### Lỗi khi thực thi (`Runtime error`)

| Code | Mô tả |
|---|---|
| 40202 | Xung đột ghi hoặc cập nhật thực thể (entity conflict).<br>**Xử lý lỗi**: Thử lại yêu cầu có thể giải quyết được vấn đề này. |

#### Nhà quảng cáo (`Advertisers`)

| Code | Mô tả |
|---|---|
| 40300 | Nhà quảng cáo không tồn tại hoặc đã bị xóa.<br>**Nguyên nhân phổ biến**: Sai ID nhà quảng cáo (`advertiser_id`).<br>**Xử lý lỗi**: Đảm bảo `advertiser_id` là chính xác và thử lại. |
| 40301 | Không khớp được nhà quảng cáo.<br>**Nguyên nhân phổ biến**: Sai ID nhà quảng cáo (`advertiser_id`).<br>**Xử lý lỗi**: Đảm bảo `advertiser_id` hợp lệ và thử lại. |

#### Lỗi dịch vụ nội bộ (`Internal service error`)

| Code | Mô tả |
|---|---|
| 40700 | Lỗi xác thực dịch vụ nội bộ.<br>**Xử lý lỗi**: Tham khảo tài liệu API để biết cách sử dụng đúng các tham số và thử lại. |

#### Liên quan đến quản lý tệp (`File management related`)

| Code | Mô tả |
|---|---|
| 40901 | Đang trong quá trình chuyển mã video (video transcoding).<br>**Xử lý lỗi**: Chờ quá trình chuyển mã hoàn tất rồi thử lại. |
| 40902 | Không thể tải URL.<br>**Xử lý lỗi**: Thử lại yêu cầu có thể giải quyết được vấn đề. |
| 40903 | URL hình ảnh không khả dụng.<br>**Xử lý lỗi**: Thử lại yêu cầu có thể giải quyết được vấn đề. |
| 40913 | Không thể lấy hình ảnh.<br>**Xử lý lỗi**: Thử lại yêu cầu có thể giải quyết được vấn đề. |
| 40905 | Tệp tin không tồn tại.<br>**Xử lý lỗi**: Cung cấp đường dẫn tệp hoặc URL tệp chính xác và thử lại. |
| 40906 | Tệp tin rỗng.<br>**Xử lý lỗi**: Cung cấp tệp có nội dung hợp lệ và thử lại. |
| 40907 | Dung lượng tệp quá lớn.<br>**Xử lý lỗi**: Giảm dung lượng tệp xuống dưới giới hạn cho phép và thử lại. |
| 40910 | Tệp tin đã hết hạn.<br>**Xử lý lỗi**: Cung cấp đường dẫn hoặc URL tệp mới và thử lại. |
| 40914 | Tệp bạn muốn tải lên không hợp lệ.<br>**Xử lý lỗi**: Đảm bảo đường dẫn hoặc URL tệp là hợp lệ và thử lại. |
| 40908 | Loại tệp không được hỗ trợ.<br>**Xử lý lỗi**: Đảm bảo bạn sử dụng định dạng tệp được hỗ trợ và thử lại. |
| 40900 | Chữ ký chúng tôi tính toán không khớp với chữ ký bạn cung cấp cho tệp.<br>**Nguyên nhân phổ biến**: Sai chữ ký của hình ảnh, video hoặc âm thanh.<br>**Xử lý lỗi**: Đảm bảo chữ ký bạn cung cấp khớp với tệp tương ứng và thử lại. |
| 40909 | Loại mã hóa (`calculate_type`) không được hỗ trợ.<br>**Xử lý lỗi**: Đảm bảo bạn sử dụng giá trị `calculate_type` được hỗ trợ và thử lại. |
| 40911 | Tên tài liệu quảng cáo bị trùng lặp.<br>**Xử lý lỗi**: Chỉ định tên khác cho tài liệu và thử lại. Bạn có thể sử dụng endpoint [/file/name/check/](../12-api-reference/44-files.md#doc-1759130033155073) để kiểm tra xem tên tệp đã được sử dụng cho hình ảnh hoặc video hay chưa. |
| 40904 | Nội dung hình ảnh không hợp lệ.<br>**Nguyên nhân phổ biến**: Định dạng hình ảnh không được hỗ trợ.<br>**Xử lý lỗi**: Đảm bảo sử dụng định dạng hình ảnh được hỗ trợ và thử lại. |
| 40912 | URL hình ảnh không khả dụng.<br>**Xử lý lỗi**: Đảm bảo URL hình ảnh là hợp lệ và thử lại. Để lấy URL hợp lệ, bạn có thể gọi [/file/image/ad/info/](../12-api-reference/47-images.md#doc-1740051721711618) hoặc [/file/image/ad/search/](../12-api-reference/47-images.md#doc-1740052016789506). |
| 40915 | Tệp bạn muốn tải lên không đáp ứng các thông số kỹ thuật.<br>**Xử lý lỗi**: Đảm bảo tệp đáp ứng các yêu cầu kỹ thuật cụ thể của endpoint và thử lại. |

#### Chặn truy cập (`Blocked access`)

| Code | Mô tả |
|---|---|
| 41000 | Địa chỉ IP của client nằm trong danh sách quốc gia bị cấm. |

#### Liên quan đến hệ thống (`System related`)

| Code | Mô tả |
|---|---|
| 50000 | Lỗi hệ thống (`System error`). |
| 50002 | Lỗi xử lý yêu cầu phía TikTok. Vui lòng xem thông báo lỗi để biết chi tiết. |
| 51305 | Lỗi dịch vụ vệ tinh (`Satellite service error`). |

#### Bảo trì (`Maintenance`)

| Code | Mô tả |
|---|---|
| 60001 | Hệ thống đang bảo trì.<br>**Xử lý lỗi**: Đợi hệ thống hoàn tất bảo trì và thử lại sau. |

#### TikTok Creator Marketplace

Xem chi tiết tại **Mã lỗi (Error codes)**.

---

## Mã trạng thái HTTP (`HTTP Status Codes`)
<a id="doc-1749734684478466"></a>
<!-- doc_id: 1749734684478466 -->

> Đường dẫn: Appendix > HTTP Status Codes

Mã trạng thái HTTP (HTTP Status Codes) giúp bạn xử lý đúng đắn các trường hợp thành công và thất bại khi gọi TikTok API for Business.

Giá trị mã trả về (`0` hoặc `4xxxx`/`5xxxx`) sẽ được trả về nếu mã trạng thái HTTP là `200`. Do đó, khi nhận được mã trạng thái HTTP `200`, bạn vẫn cần kiểm tra mã trả về (`code`) để xác nhận xem lệnh gọi API thực sự thành công hay phát sinh lỗi. Giá trị `code: 0` biểu thị phản hồi thành công từ TikTok API for Business, và bất kỳ giá trị nào khác đều chỉ ra lỗi trong lệnh gọi API (xem [Mã trả về (Return Codes)](phu-luc-p1.md#doc-1737172488964097) để xác định lỗi cụ thể).

### Hành động khuyến nghị cho các mã trạng thái HTTP

Mặc dù hầu hết các lệnh gọi tới TikTok API for Business đều trả về mã trạng thái HTTP `200`, vẫn có những trường hợp mã trạng thái `4xx` hoặc `5xx` được trả về. Dưới đây là thông tin chi tiết về cách xử lý:

| HTTP status codes | Mô tả | Hành động khuyến nghị |
|---|---|---|
| 2xx | Yêu cầu của bạn đã thành công.<br><br>Mã trạng thái phổ biến nhất của lớp này là `200`, đây là mã trạng thái dự kiến cho tất cả các lệnh gọi tới TikTok API for Business. | Xem và xác nhận mã trả về (giá trị `code` phải bằng `0`).<br><br>Nếu giá trị `code` khác `0`, nghĩa là TikTok API for Business trả về lỗi. Vui lòng kiểm tra thông báo phản hồi (giá trị `message`) để xác định nguyên nhân. |
| 4xx | Yêu cầu của bạn không hợp lệ. Các nguyên nhân phổ biến gồm:<br>• Đường dẫn API không chính xác.<br>• Phương thức API không chính xác. | Xem phản hồi HTTP để biết chi tiết và kiểm tra xem đường dẫn cùng phương thức API đã chính xác chưa. |
| 5xx | Máy chủ không xử lý được yêu cầu của bạn. | Chờ khoảng 5 phút rồi thử lại lệnh gọi API.<br><br>Nếu bạn vẫn nhận được phản hồi tương tự, vui lòng gửi ticket Athena [tại đây](https://ads.tiktok.com/athena/requester/boards?identify_key=b25033ef7782d41050cbac74f751d547e9d8ad35a39a541a0f0efbbd51fe722f) để nhận hỗ trợ kỹ thuật. |

### Ví dụ với mã trạng thái HTTP 200

Cả hai lệnh gọi API dưới đây đều trả về mã trạng thái HTTP `200`. Bạn có thể thấy các mã trả về khác nhau cho biết lệnh gọi nào thành công và lệnh gọi nào phát sinh lỗi.

#### Lệnh gọi thành công — `"code" : 0`

```http
// Phản hồi thành công (Success-Response)
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "2022110918340701025107710223BCBDD9",
    "data": {
        "list": [],
        "page_info": {
            "page": 1,
            "page_size": 10,
            "total_page": 0,
            "total_number": 0
        }
    }
}
```

#### Lệnh gọi không thành công — `"code" : 40002`

```http
// Phản hồi lỗi (Error-Response)
HTTPS/1.1 200 OK
{
    "code": 40002,
    "message": "Missing required field(s): account_id.",
    "request_id": "2022110918305001025108614416C7CC00"
}
```

---

## Các giá trị Enum (`Enumerations`)
<a id="doc-1737174886619138"></a>
<!-- doc_id: 1737174886619138 -->

> Đường dẫn: Appendix > Enumerations

### Nhà quảng cáo (`Advertisers`)

#### Loại thanh toán của nhà quảng cáo (`Advertiser Billing Type`)

| Value | Mô tả |
|---|---|
| TRANS_TYPE_TRANSFER | Chuyển khoản (`Transfer`) |
| TRANS_TYPE_TAX | Thuế (`Tax`) |
| TRANS_TYPE_COST | Chi tiêu/Tiêu dùng (`Consumption`) |

#### Trạng thái hiển thị nhà quảng cáo (`Advertiser Display Status - advertiser_status`)

| Value | Mô tả |
|---|---|
| SHOW_ACCOUNT_STATUS_NOT_APPROVED | Không được phê duyệt (`Failed`) |
| SHOW_ACCOUNT_STATUS_APPROVED | Đã được phê duyệt (`Passed`) |
| SHOW_ACCOUNT_STATUS_IN_REVIEW | Đang chờ xét duyệt (`Under review`) |
| SHOW_ACCOUNT_STATUS_PUNISHED | Bị xử phạt (`Punishment`) |

#### Vai trò của nhà quảng cáo (`Advertiser Roles`)

| Value | Mô tả |
|---|---|
| ROLE_ADVERTISER | Nhà quảng cáo tiêu chuẩn (khách hàng trực tiếp - `direct customer`) |
| ROLE_CHILD_ADVERTISER | Nhà quảng cáo tiêu chuẩn (tài khoản phụ của đại lý - `agency sub-account`) |
| ROLE_CHILD_AGENT | Đại lý cấp 2 (`Secondary agency`) |
| ROLE_AGENT | Đại lý cấp 1 (`Primary agency`) |

#### Trạng thái tài khoản nhà quảng cáo (`Advertiser Status`)

| Value | Mô tả |
|---|---|
| STATUS_DISABLE | Tài khoản quảng cáo đã bị đóng |
| STATUS_PENDING_CONFIRM | Đơn đăng ký đang chờ xét duyệt |
| STATUS_PENDING_VERIFIED | Đang chờ xác minh |
| STATUS_CONFIRM_FAIL | Xét duyệt thất bại |
| STATUS_ENABLE | Đã phê duyệt |
| STATUS_CONFIRM_FAIL_END | Xét duyệt hệ thống CRM thất bại |
| STATUS_PENDING_CONFIRM_MODIFY | Các sửa đổi đang chờ xét duyệt |
| STATUS_CONFIRM_MODIFY_FAIL | Xét duyệt các sửa đổi thất bại |
| STATUS_LIMIT | Tài khoản quảng cáo đang bị xử phạt |
| STATUS_WAIT_FOR_BPM_AUDIT | Đang chờ hệ thống CRM xét duyệt |
| STATUS_WAIT_FOR_PUBLIC_AUTH | Đang chờ xác thực tài khoản ngân hàng doanh nghiệp |
| STATUS_SELF_SERVICE_UNAUDITED | Đang chờ xác minh điều kiện cho tài khoản tự phục vụ (`self-service`) |
| STATUS_CONTRACT_PENDING | Hợp đồng chưa có hiệu lực |

#### Trạng thái Business Center (`Business Center Status`)

| Value | Mô tả |
|---|---|
| REVIEWING | Đang xét duyệt |
| DENY | Bị từ chối |
| ENABLE | Đã phê duyệt |
| PUNISH | Bị vô hiệu hóa / Xử phạt |

#### Loại Business Center (`Business Center Type`)

| Value | Mô tả |
|---|---|
| NORMAL | Business Center thông thường |
| DIRECT | Business Center trực tiếp không tự phục vụ |
| AGENCY | Business Center đại lý không tự phục vụ |
| SELF_SERVICE | Business Center trực tiếp tự phục vụ |
| SELF_SERVICE_AGENCY | Business Center đại lý tự phục vụ |

---

### Quản lý quảng cáo (`Ad Management`)

#### Tốc độ phân phối quảng cáo (`Ad Delivery Speed - pacing`)

| Value | Mô tả |
|---|---|
| PACING_MODE_SMOOTH | Tốc độ tiêu chuẩn, ngân sách được phân bổ đều đặn trong suốt thời gian quảng cáo được lên lịch. |
| PACING_MODE_FAST | Tốc độ nhanh, tiêu hao ngân sách và mang lại kết quả nhanh nhất có thể. |

#### Trạng thái phụ của nhóm quảng cáo (`Ad group status - secondary status`)

> [!NOTE]
> Xem [Trạng thái phụ được hỗ trợ cho từng trạng thái chính](../09-marketing-api/quan-ly-chien-dich-tom-tat.md#doc-1757239620352002) để tìm hiểu các trạng thái phụ hợp lệ bạn có thể truyền qua [/adgroup/get/](../12-api-reference/07-ad-groups-p1.md#doc-1739314558673922) tương ứng với trạng thái chính được chỉ định.

| Value | Mô tả |
|---|---|
| ADGROUP_STATUS_ALL | Tất cả các trạng thái (bao gồm cả "Đã xóa" - `Deleted`) |
| ADGROUP_STATUS_NOT_DELETE | Tất cả các trạng thái (không bao gồm "Đã xóa") |
| Auction | Nhóm quảng cáo Đấu thầu (`Auction`) |
| ↳ ADGROUP_STATUS_DELETE | Đã xóa |
| ↳ ADGROUP_STATUS_CAMPAIGN_DELETE | Chiến dịch đã bị xóa |
| ↳ ADGROUP_STATUS_ADVERTISER_AUDIT_DENY | Xét duyệt nhà quảng cáo thất bại |
| ↳ ADGROUP_STATUS_ADVERTISER_AUDIT | Xét duyệt nhà quảng cáo đang diễn ra |
| ↳ ADVERTISER_CONTRACT_PENDING | Hợp đồng nhà quảng cáo chưa có hiệu lực |
| ↳ ADVERTISER_ACCOUNT_PUNISH | Tài khoản nhà quảng cáo bị xử phạt |
| ↳ ADGROUP_STATUS_CAMPAIGN_EXCEED | Chiến dịch đã vượt quá ngân sách |
| ↳ ADGROUP_STATUS_BUDGET_EXCEED | Nhóm quảng cáo đã vượt quá ngân sách |
| ↳ ADGROUP_STATUS_BALANCE_EXCEED | Số dư tài khoản không đủ |
| ↳ ADGROUP_STATUS_ADGROUP_PRE_ONLINE | Nhóm quảng cáo đang ở trạng thái chuẩn bị chạy (pre-online) và chưa được phân phối |
| ↳ ADGROUP_STATUS_AUDIT_DENY | Xét duyệt nhóm quảng cáo thất bại |
| ↳ ADGROUP_STATUS_REAUDIT | Đang xét duyệt lại các sửa đổi |
| ↳ ADGROUP_STATUS_AUDIT | Yêu cầu xét duyệt mới đã được tạo |
| ↳ ADGROUP_STATUS_CREATE | Nhóm quảng cáo mới đã được tạo |
| ↳ ADGROUP_STATUS_FROZEN | Nhóm quảng cáo đang bị đóng băng |
| ↳ ADGROUP_STATUS_NOT_START | Chưa đến thời gian phân phối theo lịch trình |
| ↳ ADGROUP_STATUS_LIVE_NOT_START | Đã đến thời gian phân phối theo lịch trình nhưng phiên Live chưa bắt đầu. Trạng thái này chỉ áp dụng cho nhóm quảng cáo đấu thầu. |
| ↳ ADGROUP_STATUS_CAMPAIGN_DISABLE | Chiến dịch bị tạm dừng |
| ↳ ADGROUP_STATUS_DISABLE | Nhóm quảng cáo bị tạm dừng |
| ↳ ADGROUP_STATUS_SHADOW_ADGROUP_REAUDIT | Nhóm quảng cáo đang trong quá trình xét duyệt lại |
| ↳ ADGROUP_STATUS_PIXEL_UNBIND | Pixel liên kết đã bị hủy liên kết |
| ↳ ADGROUP_STATUS_PARTIAL_AUDIT_NO_DELIVERY | Nhóm quảng cáo đang được xét duyệt một phần và không phân phối |
| ↳ ADGROUP_STATUS_PARTIAL_AUDIT_DELIVERY_OK | Nhóm quảng cáo đang được xét duyệt một phần và đang phân phối |
| ↳ ADGROUP_STATUS_INDUSTRY_QUALIFICATION_MISSING | Thiếu chứng nhận/giấy phép ngành hàng, vui lòng gửi bổ sung |
| ↳ ADGROUP_STATUS_INDUSTRY_QUALIFICATION_EXPIRED | Giấy phép ngành hàng đã hết hạn, vui lòng gửi lại |
| ↳ ADGROUP_STATUS_INDUSTRY_QUALIFICATION_DENY | Giấy phép ngành hàng bị từ chối |
| ↳ ADGROUP_STATUS_ASSET_AUTHORIZATION_LOST | Thiếu ủy quyền cho tài sản quảng cáo trong nhóm quảng cáo.<br>**Lưu ý**: Trạng thái này không thể dùng làm bộ lọc. |
| ↳ ADGROUP_STATUS_TRANSCODING_FAIL | Quá trình chuyển mã video trong nhóm quảng cáo thất bại.<br>**Lưu ý**: Trạng thái này không thể dùng làm bộ lọc. |
| ↳ ADGROUP_STATUS_ADGROUP_QUOTA_LIMIT | Tài khoản quảng cáo đã chạm hạn mức số lượng nhóm quảng cáo. Để tạo nhóm quảng cáo hoạt động mới, bạn cần tạm dừng hoặc xóa bớt nhóm quảng cáo đang ở trạng thái "hoạt động" hoặc "đang xét duyệt".<br>**Lưu ý**: Không dùng làm bộ lọc. |
| ↳ ADGROUP_STATUS_IDENTITY_USED_BY_GMV_MAX_AD | Danh tính bạn muốn dùng trong quảng cáo thuộc nhóm quảng cáo này không khả dụng vì đã được sử dụng bởi nhóm quảng cáo có mục tiêu tối ưu hóa GMV (`optimization_goal = GMV`). |
| ↳ ADGROUP_STATUS_SEARCH_KEYWORDS_IN_REVIEW | Tất cả từ khóa của nhóm quảng cáo trong Chiến dịch tìm kiếm (Search Campaign) đang được xét duyệt. |
| ↳ ADGROUP_STATUS_SEARCH_KEYWORDS_NOT_AVAILABLE | Tất cả từ khóa của nhóm quảng cáo trong Chiến dịch tìm kiếm bị từ chối, hoặc chưa thiết lập từ khóa nào. |
| ↳ ADGROUP_STATUS_SEARCH_KEYWORDS_PARTIAL_APPROVED | Một số từ khóa của nhóm quảng cáo trong Chiến dịch tìm kiếm đã được duyệt trong khi các từ khóa khác đang xét duyệt hoặc bị từ chối. |
| Auction or R&F | Nhóm quảng cáo Đấu thầu hoặc Tiếp cận & Tần suất (`Reach & Frequency`) |
| ↳ ADGROUP_STATUS_DELIVERY_OK | Quảng cáo đang phân phối |
| ↳ ADGROUP_STATUS_REVIEW_PARTIALLY_APPROVED | Một hoặc nhiều quảng cáo bị từ chối |
| ↳ ADGROUP_STATUS_TIME_DONE | Đã hoàn tất.<br>**Lưu ý**: Biểu thị việc phân phối của nhóm quảng cáo đã kết thúc đúng thời gian đã lên lịch. |
| R&F | Nhóm quảng cáo Tiếp cận & Tần suất (`R&F`) |
| ↳ ADGROUP_STATUS_RF_DEDUCTION_FAILED | Khấu trừ chi phí thất bại cho nhóm quảng cáo R&F |
| ↳ ADGROUP_STATUS_RF_NO_VALID_CREATIVE | Không có nội dung sáng tạo hợp lệ trong nhóm quảng cáo R&F |
| ↳ ADGROUP_STATUS_RF_CLOSED_OTHERS | Nhóm quảng cáo R&F đã bị đóng |
| ↳ ADGROUP_STATUS_RF_SHORT_BALANCE | Không đủ số dư trong nhóm quảng cáo R&F |
| ↳ ADGROUP_STATUS_RF_BOOKING | Ngân sách / dung lượng quảng cáo đã được đặt chỗ trước cho nhóm quảng cáo R&F |
| ↳ ADGROUP_STATUS_RF_NO_DELIVERY_CREATIVE | Không có nội dung sáng tạo nào trong nhóm quảng cáo R&F này |
| ↳ ADGROUP_STATUS_RF_SCHEDULE | Lịch trình phân phối đã được tạo cho nhóm quảng cáo R&F |
| ↳ ADGROUP_STATUS_RF_TERMINATE | Nhóm quảng cáo R&F đã bị chấm dứt |
| ↳ ADGROUP_STATUS_RF_AD_AUDIT_DENY | Quảng cáo R&F bị từ chối xét duyệt |
| ↳ ADVERTISER_ACCOUNT_INVALID | Tài khoản nhà quảng cáo không hợp lệ |
| ↳ ADGROUP_STATUS_RF_ADGROUP_INVALID | Nhóm quảng cáo R&F không tồn tại |
| ↳ ADGROUP_STATUS_RF_WITHDRAW_ORDER | Đơn đặt hàng R&F đã bị rút lại |
| ↳ ADGROUP_STATUS_RF_TIME_DONE | Nhóm quảng cáo R&F đã hoàn tất.<br>**Lưu ý**: Biểu thị việc phân phối kết thúc trước thời gian lên lịch do không đủ ngân sách hoặc số dư tài khoản. |
| Promote | Nhóm quảng cáo Promote (Quảng bá bài viết) |
| ↳ ADGROUP_STATUS_PROMOTE_AD_NOT_APPROVED | Một hoặc nhiều nội dung sáng tạo trong nhóm quảng cáo Promote không được phê duyệt. |
| ↳ ADGROUP_STATUS_PROMOTE_WITHDRAW_ORDER | Đơn hàng Promote đã bị rút lại. |

#### Trạng thái khiếu nại xét duyệt nhóm quảng cáo (`Ad Group Review Appeal Status - appeal_status`)

| Value | Mô tả |
|---|---|
| NOT_APPEALED | Chưa gửi khiếu nại |
| APPEALING | Khiếu nại đang được xử lý |
| APPEAL_SUCCESSFUL | Khiếu nại thành công |
| APPEAL_FAILED | Khiếu nại thất bại |
| APPEAL_DONE | Sau khi khiếu nại thành công, nhóm quảng cáo đã được xét duyệt lại và trạng thái xét duyệt đã được cập nhật tương ứng. |

#### Trạng thái phụ của quảng cáo (`Ad status - secondary status`)

> [!NOTE]
> Xem [Trạng thái phụ được hỗ trợ cho từng trạng thái chính](../09-marketing-api/quan-ly-chien-dich-tom-tat.md#doc-1757239620352002) để tìm hiểu các trạng thái phụ hợp lệ bạn có thể truyền qua [/ad/get/](../12-api-reference/02-ads-p1.md#doc-1735735588640770) tương ứng với trạng thái chính đã chỉ định.

| Value | Mô tả |
|---|---|
| AD_STATUS_ALL | Tất cả các trạng thái (bao gồm cả "Đã xóa") |
| AD_STATUS_NOT_DELETE | Tất cả các trạng thái (không bao gồm "Đã xóa") |
| AD_STATUS_CAMPAIGN_DELETE | Chiến dịch đã bị xóa |
| AD_STATUS_ADGROUP_DELETE | Nhóm quảng cáo đã bị xóa |
| AD_STATUS_DELETE | Đã xóa |
| AD_STATUS_ADVERTISER_AUDIT_DENY | Xét duyệt tài khoản thất bại |
| AD_STATUS_ADVERTISER_AUDIT | Đã công bố kết quả tóm tắt xét duyệt tài khoản |
| ADVERTISER_CONTRACT_PENDING | Hợp đồng nhà quảng cáo chưa có hiệu lực |
| ADVERTISER_ACCOUNT_PUNISH | Tài khoản nhà quảng cáo bị xử phạt |
| AD_STATUS_BALANCE_EXCEED | Số dư tài khoản không đủ |
| AD_STATUS_CAMPAIGN_EXCEED | Chiến dịch đã vượt quá ngân sách |
| AD_STATUS_BUDGET_EXCEED | Nhóm quảng cáo đã vượt quá ngân sách |
| AD_STATUS_AD_PRE_ONLINE | Quảng cáo đang ở trạng thái chuẩn bị chạy (pre-online) và chưa phân phối |
| AD_STATUS_AUDIT | Đang chờ xét duyệt |
| AD_STATUS_REAUDIT | Các sửa đổi đang được xét duyệt |
| AD_STATUS_AUDIT_DENY | Xét duyệt thất bại |
| AD_STATUS_ADGROUP_AUDIT_DENY | Xét duyệt nhóm quảng cáo thất bại |
| AD_STATUS_ADGROUP_PARTIAL_AUDIT_NO_DELIVERY | Nhóm quảng cáo đang xét duyệt một phần và không phân phối |
| AD_STATUS_REVIEW_PARTIALLY_APPROVED | Một hoặc nhiều nội dung sáng tạo của quảng cáo bị từ chối |
| AD_STATUS_PARTIAL_AUDIT_DELIVERY_OK | Quảng cáo đang xét duyệt một phần và đang phân phối |
| AD_STATUS_PARTIAL_AUDIT_NO_DELIVERY | Nội dung sáng tạo quảng cáo đang xét duyệt một phần và không phân phối |
| AD_STATUS_ADGROUP_INDUSTRY_QUALIFICATION_MISSING | Thiếu chứng nhận ngành hàng của nhóm quảng cáo, vui lòng gửi bổ sung |
| AD_STATUS_ADGROUP_INDUSTRY_QUALIFICATION_EXPIRED | Chứng nhận ngành hàng của nhóm quảng cáo đã hết hạn, vui lòng gửi lại |
| AD_STATUS_ADGROUP_INDUSTRY_QUALIFICATION_DENY | Chứng nhận ngành hàng của nhóm quảng cáo bị từ chối |
| AD_STATUS_MUSIC_AUTHORIZATION_MISSING | Thiếu ủy quyền sử dụng bản quyền âm nhạc |
| AD_STAUS_PIXEL_UNBIND | Pixel liên kết đã bị hủy liên kết |
| AD_STATUS_LIVE_OFFLINE | Phiên Live chưa bắt đầu |
| AD_STATUS_NOT_START | Chưa đến thời gian phân phối theo lịch trình |
| AD_STATUS_DONE | Đã hoàn tất |
| AD_STATUS_CAMPAIGN_DISABLE | Chiến dịch bị tạm dừng |
| AD_STATUS_ADGROUP_DISABLE | Nhóm quảng cáo bị tạm dừng |
| ADGROUP_STATUS_FROZEN | Nhóm quảng cáo bị đóng băng |
| AD_STATUS_DISABLE | Quảng cáo bị tạm dừng |
| AD_STATUS_DELIVERY_OK | Quảng cáo đang phân phối |
| AD_STATUS_PROCESS_AUDIO | Đang xử lý âm thanh.<br>**Lưu ý**: Nếu trạng thái `AD_STATUS_PROCESS_AUDIO` kéo dài (thông báo "Processing audio, if this lasts long check if your creative has audio, or upload another video file to fix"), hãy tải lên video mới có âm thanh để khắc phục. |
| AD_STATUS_TRANSCODING_FAIL | Quá trình chuyển mã video trong quảng cáo thất bại.<br>**Lưu ý**: Không dùng làm bộ lọc. |
| AD_STATUS_ADGROUP_ASSET_AUTHORIZATION_LOST | Thiếu ủy quyền tài sản trong nhóm quảng cáo.<br>**Lưu ý**: Không dùng làm bộ lọc. |
| AD_STATUS_ASSET_AUTHORIZATION_LOST | Thiếu ủy quyền tài sản trong quảng cáo.<br>**Lưu ý**: Không dùng làm bộ lọc. |
| AD_STATUS_AD_QUOTA_LIMIT | Nhóm quảng cáo nơi bạn muốn tạo quảng cáo đã bị vô hiệu hóa vì tài khoản quảng cáo đã chạm hạn mức nhóm quảng cáo. Hãy tạm dừng hoặc xóa nhóm quảng cáo đang hoạt động rồi thử lại.<br>**Lưu ý**: Không dùng làm bộ lọc. |
| AD_STATUS_PRODUCT_UNAVAILABLE | Sản phẩm bạn muốn sử dụng trong quảng cáo không khả dụng. |
| AD_STATUS_ANCHOR_UNAVAILABLE | Liên kết sản phẩm (anchor link) bạn muốn sử dụng trong quảng cáo không khả dụng. |
| AD_STATUS_NO_AUTHORIZATION_OF_SHOWCASE | Danh tính Showcase bạn muốn sử dụng trong quảng cáo không khả dụng. |
| AD_STATUS_RF_ADGROUP_CLOSED | Nhóm quảng cáo R&F đã bị đóng |
| AD_STATUS_PROMOTE_AD_OFFLINE_AUDIT | Một hoặc nhiều nội dung sáng tạo trong quảng cáo Promote không được phê duyệt. |
| AD_STATUS_PROMOTE_ADGROUP_CLOSED | Nhóm quảng cáo Promote đã bị đóng. |

#### Mục tiêu quảng cáo (`Advertising Objective - objective_type`)

| Value | Mô tả |
|---|---|
| APP_PROMOTION | Thúc đẩy cài đặt ứng dụng di động và tái tương tác với người dùng hiện tại của ứng dụng. |
| WEB_CONVERSIONS | Điều hướng người dùng đến trang web của bạn hoặc Trang tức thì của TikTok (TikTok Instant Page) để thực hiện các hành động cụ thể như mua hàng hoặc thêm vào giỏ hàng. |
| APP_INSTALL | Đã ngừng hỗ trợ (`Deprecated`). Thu hút thêm lượt cài đặt ứng dụng.<br>**Lưu ý**: Các tính năng mới sẽ được cập nhật trong mục tiêu `APP_PROMOTION`. Khuyến nghị chuyển sang dùng [Quảng bá ứng dụng (App promotion)](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1747553433902082). |
| CONVERSIONS | Đã ngừng hỗ trợ (`Deprecated`). Thúc đẩy các hành động giá trị trên trang web hoặc ứng dụng. Khuyến nghị dùng [Chuyển đổi trên trang web (Website conversions)](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1747553507237889). |
| REACH | Tiếp cận theo hình thức đấu thầu (`Auction reach`). Hiển thị quảng cáo đấu thầu tới số lượng người tối đa. |
| BRAND_CONSIDERATION | Mức độ cân nhắc thương hiệu (`Brand consideration`). Thu hút đối tượng đã thể hiện sự quan tâm đến thương hiệu của bạn.<br>**Lưu ý**: Hiện tại API không hỗ trợ tạo chiến dịch Brand Consideration. Giá trị này chỉ dùng trong [/campaign/get/](../12-api-reference/24-campaign.md#doc-1739315828649986). |
| TRAFFIC | Thu hút nhiều lượt truy cập vào trang web hoặc ứng dụng của bạn. |
| VIDEO_VIEWS | Thu hút nhiều người xem nội dung video của bạn hơn. |
| CATALOG_SALES | Đã ngừng hỗ trợ (`Deprecated`, yêu cầu danh sách cho phép). Quảng cáo Showcase động thu hút người dùng mua sản phẩm trong danh mục. Khuyến nghị chuyển sang [Video Shopping Ads](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1741942291730434) thuộc mục tiêu `PRODUCT_SALES`. |
| PRODUCT_SALES | Cung cấp phương thức trực tiếp hơn cho nhà quảng cáo thương mại để phân phối quảng cáo và bán sản phẩm từ TikTok Shop, website và ứng dụng.<br>**Lưu ý**: [Video Shopping Ads (cho Catalog)](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1750361698613249) yêu cầu allowlist đối với nhà quảng cáo Commerce App. Nhà quảng cáo Web Commerce được tự động truy cập. |
| ENGAGEMENT | Thu hút thêm lượt theo dõi tài khoản hoặc lượt truy cập hồ sơ. |
| LEAD_GENERATION | Thu thập thông tin khách hàng tiềm năng cho doanh nghiệp hoặc thương hiệu của bạn. |
| SHOP_PURCHASES | Đã ngừng hỗ trợ (`Deprecated`). Thúc đẩy người dùng mua sản phẩm trong gian hàng của bạn trên TikTok Shop. |
| RF_APP_INSTALL | Đã ngừng hỗ trợ (`Deprecated`, yêu cầu allowlist). Thu hút lượt cài đặt ứng dụng thông qua quảng cáo Tiếp cận & Tần suất (R&F). |
| RF_ENGAGEMENT | Đã ngừng hỗ trợ (`Deprecated`, yêu cầu allowlist). Thu hút lượt theo dõi hoặc xem hồ sơ qua quảng cáo R&F. |
| RF_REACH | Đặt chỗ trước Tiếp cận & Tần suất (`Reservation Reach & Frequency`) hoặc Đặt trước TikTok Pulse.<br>Hiển thị quảng cáo đặt trước với độ tiếp cận và tần suất được đảm bảo, hoặc quảng cáo đặt sau top 4% nội dung thịnh hành trên trang Dành cho bạn (For You page) với mức CPM cố định.<br>**Lưu ý**: Với mục tiêu R&F, đặt `objective_type = RF_REACH` và `rf_campaign_type = STANDARD` qua [/campaign/create/](../12-api-reference/24-campaign.md#doc-1739318962329602). Với TikTok Pulse, đặt `objective_type = RF_REACH` và `rf_campaign_type = PULSE`. |
| TOPVIEW_REACH | Đặt trước TopView (`Reservation TopView`). Hiển thị quảng cáo xuất hiện ngay khi người dùng mở ứng dụng TikTok tới số lượng người tối đa.<br>**Lưu ý**: Không thể dùng giá trị này làm bộ lọc `objective_type` trong GET campaign/adgroup/ad. Thay vào đó, đặt trường lọc `buying_types` thành `["RESERVATION_TOP_VIEW"]`. Việc tạo, sửa, sao chép quảng cáo TopView không hỗ trợ qua API, chỉ hỗ trợ truy xuất thông tin qua [TopView](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1804258360285186). |
| RF_TRAFFIC | Đã ngừng hỗ trợ (`Deprecated`, yêu cầu allowlist). Thu hút người truy cập website hoặc ứng dụng qua quảng cáo R&F. |
| RF_VIDEO_VIEW | Đã ngừng hỗ trợ (`Deprecated`, yêu cầu allowlist). Thu hút người xem nội dung video qua quảng cáo R&F. |

#### Nhóm tuổi (`Age Group - age_groups`)

| Value | Mô tả |
|---|---|
| AGE_13_17 | 13–17 tuổi |
| AGE_18_24 | 18–24 tuổi |
| AGE_25_34 | 25–34 tuổi |
| AGE_35_44 | 35–44 tuổi |
| AGE_45_54 | 45–54 tuổi |
| AGE_55_100 | 55 tuổi trở lên (55+) |

#### Loại đối tượng nhắm lại ứng dụng (`App Retargeting Audience Type - audience_type` cho `/adgroup/create/`)

| Value | Mô tả |
|---|---|
| CUSTOM_AUDIENCE | Đối tượng tùy chỉnh. Không hỗ trợ cho mục tiêu `TRAFFIC`. |
| EXCLUDE_INTERACT_USERS | Loại trừ những người dùng đã tương tác với ứng dụng của bạn. |
| INCLUDE_INTERACT_USERS | Bao gồm những người dùng đã tương tác với ứng dụng của bạn. |
| INCLUDE_SPECIFIC_EVENTS | Bao gồm những người dùng thỏa mãn quy tắc đối tượng cụ thể (`audience_rule`). |
| EXCLUDE_SPECIFIC_EVENTS | Loại trừ những người dùng thỏa mãn quy tắc đối tượng cụ thể (`audience_rule`). |
| NEW_CUSTOM_AUDIENCE | Loại đối tượng tùy chỉnh mới. Đây là loại đối tượng nhắm lại duy nhất được hỗ trợ cho các nhóm quảng cáo mới. |

#### Chiến lược giá thầu (`Bidding Strategy - bid_type`)

Bạn có thể chỉ định chiến lược giá thầu khi thiết lập quảng cáo. Mỗi chiến lược có ưu điểm riêng phù hợp với mục tiêu kinh doanh. `BID_TYPE_CUSTOM` được khuyến nghị nếu bạn ưu tiên sự ổn định chi phí, dù có thể không tận dụng hết ngân sách. Chi tiết xem tại [Chiến lược giá thầu (Bidding Strategies)](https://ads.tiktok.com/help/article?aid=6731899932019523590).

| Value | Mô tả |
|---|---|
| BID_TYPE_CUSTOM | Đặt giá thầu thủ công. Chiến lược này được gọi là "Giới hạn chi phí" (`Cost Cap`) trong Trình quản lý quảng cáo TikTok Ads Manager. |
| BID_TYPE_NO_BID | Tắt kiểm soát giá thầu, chi tiêu toàn bộ ngân sách để đạt được kết quả tối đa có thể. Chiến lược này gọi là "Phân phối tối đa" (`Maximum Delivery`) trong TikTok Ads Manager. |

#### Sự kiện tính phí (`Billing Event - billing_event` hoặc `billing_events`)

| Value | Mô tả |
|---|---|
| CPC | Chi phí mỗi lần nhấp chuột (`Cost Per Click`) |
| CPM | Chi phí mỗi nghìn lượt hiển thị (`Cost Per Mille`) |
| CPV | Chi phí mỗi lượt xem video (`Cost Per View`) |
| OCPC | Đã ngừng hỗ trợ (`deprecated`). Chi phí mỗi lượt chuyển đổi tối ưu hóa (`oCPC`, tương đương CPA). |
| GD | Phân phối đảm bảo (`Guaranteed Delivery`) |
| OCPM | Chi phí mỗi nghìn lượt hiển thị tối ưu hóa (`oCPM`) |

#### Chế độ ngân sách (`Budget Mode - budget_mode`)

Chi tiết xem tại [Ngân sách (Budget)](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1739381246298114).

| Value | Mô tả |
|---|---|
| BUDGET_MODE_DAY | Ngân sách hàng ngày (`Daily budget`) |
| BUDGET_MODE_DYNAMIC_DAILY_BUDGET | Ngân sách hàng ngày động (`Dynamic daily budget`). Yêu cầu danh sách cho phép (allowlist) đối với mục tiêu `REACH`, `VIDEO_VIEWS`, `ENGAGEMENT`. Khả dụng công khai cho các mục tiêu `TRAFFIC`, `APP_PROMOTION`, `WEB_CONVERSIONS`, `LEAD_GENERATION`, và `PRODUCT_SALES` (chỉ Video Shopping Ads). |
| BUDGET_MODE_TOTAL | Ngân sách trọn đời (`Lifetime budget`) |
| BUDGET_MODE_INFINITE | Ngân sách không giới hạn (`Unlimited budget`) |

#### Lời kêu gọi hành động (`Call-to-action - call_to_action`)

| Value | Mô tả |
|---|---|
| APPLY_NOW | Đăng ký ngay (`Apply now`) |
| BOOK_NOW | Đặt ngay (`Book now`) |
| CALL_NOW | Gọi ngay (`Call now`) |
| CHECK_AVAILABLILITY | Kiểm tra tình trạng (`Check availability`) |
| CONTACT_US | Liên hệ với chúng tôi (`Contact us`) |
| DOWNLOAD_NOW | Tải xuống (`Download`) |
| EXPERIENCE_NOW | Trải nghiệm ngay (`Experience now`) |
| GET_QUOTE | Nhận báo giá (`Get quote`) |
| GET_SHOWTIMES | Xem lịch chiếu (`Get showtimes`) |
| GET_TICKETS_NOW | Mua vé ngay (`Get tickets now`) |
| INSTALL_NOW | Cài đặt ngay (`Install now`) |
| INTERESTED | Quan tâm (`Interested`) |
| LEARN_MORE | Tìm hiểu thêm (`Learn more`) |
| LISTEN_NOW | Nghe ngay (`Listen now`) |
| ORDER_NOW | Đặt hàng ngay (`Order now`) |
| PLAY_GAME | Chơi trò chơi (`Play game`) |
| PREORDER_NOW | Đặt hàng trước ngay (`Pre-order now`) |
| READ_MORE | Đọc thêm (`Read more`) |
| SEND_MESSAGE | Gửi tin nhắn (`Send message`) |
| SHOP_NOW | Mua ngay (`Shop now`) |
| SIGN_UP | Đăng ký (`Sign up`) |
| SUBSCRIBE | Đăng ký theo dõi (`Subscribe`) |
| VIEW_NOW | Xem ngay (`View now`) |
| VIEW_PROFILE | Xem hồ sơ (`View profile` - chỉ hỗ trợ cho quảng cáo mục tiêu `ENGAGEMENT`) |
| VISIT_STORE | Ghé thăm cửa hàng (`Visit store`) |
| WATCH_LIVE | Xem Trực tiếp (`Watch LIVE` - chỉ hỗ trợ cho quảng cáo LIVE) |
| WATCH_NOW | Xem ngay (`Watch now`) |
| JOIN_THIS_HASHTAG | Tham gia hashtag này (`Join this hashtag` - chỉ hỗ trợ trong quảng cáo R&F) |
| SHOOT_WITH_THIS_EFFECT | Quay video với hiệu ứng này (`Shoot with this effect` - chỉ hỗ trợ trong quảng cáo R&F) |
| VIEW_VIDEO_WITH_THIS_EFFECT | Xem video có hiệu ứng này (`View video with this effect` - chỉ hỗ trợ trong quảng cáo R&F) |

#### Trạng thái phụ của chiến dịch (`Campaign Status - Secondary Status`)

> [!NOTE]
> Xem [Trạng thái phụ được hỗ trợ cho từng trạng thái chính](../09-marketing-api/quan-ly-chien-dich-tom-tat.md#doc-1757239620352002) để tìm hiểu các trạng thái phụ hợp lệ bạn có thể truyền qua [/campaign/get/](../12-api-reference/24-campaign.md#doc-1739315828649986).

| Value | Mô tả |
|---|---|
| CAMPAIGN_STATUS_DELETE | Đã xóa |
| CAMPAIGN_STATUS_ADVERTISER_AUDIT_DENY | Xét duyệt nhà quảng cáo thất bại (hỗ trợ cả dạng `CAMPAIGN_STATUS_ADVERT ISER_AUDIT_DENY`) |
| CAMPAIGN_STATUS_ADVERTISER_AUDIT | Xét duyệt nhà quảng cáo đang diễn ra (hỗ trợ cả dạng `CAMPAIGN_STATUS_ADVERT ISER_AUDIT`) |
| ADVERTISER_CONTRACT_PENDING | Hợp đồng nhà quảng cáo chưa có hiệu lực |
| ADVERTISER_ACCOUNT_PUNISH | Tài khoản nhà quảng cáo bị xử phạt |
| CAMPAIGN_STATUS_BUDGET_EXCEED | Vượt quá ngân sách |
| CAMPAIGN_STATUS_DISABLE | Bị tạm dừng |
| CAMPAIGN_STATUS_AWAITING_RELEASE | Chờ phát hành. Chiến dịch chuyên dụng SKAN 4.0 đang trong giai đoạn postback. Khuyến nghị chờ vài ngày để phát hành chiến dịch nhằm đảm bảo tính chính xác của báo cáo. |
| CAMPAIGN_STATUS_IDENTITY_USED_BY_GMV_MAX_AD | Danh tính bạn muốn dùng trong quảng cáo không khả dụng vì đã được nhóm quảng cáo có mục tiêu GMV (`optimization_goal = GMV`) sử dụng. |
| CAMPAIGN_STATUS_ENABLE | Đang phân phối quảng cáo |
| CAMPAIGN_STATUS_ALL | Tất cả trạng thái (bao gồm cả "Đã xóa") |
| CAMPAIGN_STATUS_NOT_DELETE | Tất cả trạng thái (không bao gồm "Đã xóa") |
| CAMPAIGN_STATUS_TTS_TT_ASSET_UNAVAILABLE | Tài sản được sử dụng trong chiến dịch của bạn không khả dụng. Kiểm tra lại cài đặt chiến dịch. |
| CAMPAIGN_STATUS_TTS_TT_IDENTITY_UNAVAILABLE | Tài khoản TikTok không khả dụng. Thử kết nối lại hoặc chọn tài khoản khác để tạo quảng cáo. |
| CAMPAIGN_STATUS_TIKTOK_SHOP_UNAVAILABLE | Cửa hàng Shop đã bị ngắt kết nối khỏi tài khoản Business Center. Kết nối lại với gian hàng. |
| CAMPAIGN_STATUS_REVIEW_DISAPPROVED | Bị từ chối phê duyệt. |
| CAMPAIGN_STATUS_AD_UNAVAILABLE | Toàn bộ chiến dịch bị tạm dừng do một hoặc nhiều nhóm quảng cáo bị từ chối hoặc một số tài sản không khả dụng. |
| CAMPAIGN_STATUS_PRODUCT_UNAVAILABLE | Các sản phẩm đã chọn không khả dụng sau khi chiến dịch được tạo. Truy cập Seller Center để quản lý hoặc thêm sản phẩm. |
| CAMPAIGN_STATUS_LIVE_GMV_MAX_AUTHORIZATION_CANCEL | Chiến dịch này bị tạm dừng vì tài khoản TikTok chính thức đã cấp quyền GMV Max cho một tài khoản quảng cáo khác. |
| CAMPAIGN_STATUS_PRODUCT_GMV_MAX_AUTHORIZATION_CANCEL | Chiến dịch này bị tạm dừng vì TikTok Shop đã cấp quyền GMV Max cho một tài khoản quảng cáo khác. |
| CAMPAIGN_STATUS_IDENTITY_USED_BY_LIVE_GMV_MAX | Chiến dịch bị tạm dừng do có chiến dịch LIVE GMV Max đang hoạt động sử dụng tài khoản TikTok này. |
| CAMPAIGN_STATUS_PRODUCT_USED_BY_PRODUCT_GMV_MAX | Chiến dịch bị tạm dừng do có chiến dịch Product GMV Max đang hoạt động được tạo cho cửa hàng này. |

#### Loại kết nối mạng (`Connection Type - network_types`)

| Value | Mô tả |
|---|---|
| WIFI | Mạng Wifi |
| 2G | Mạng di động 2G |
| 3G | Mạng di động 3G |
| 4G | Mạng di động 4G |
| 5G | Mạng di động 5G |

#### Khoảng thời gian quy kết chuyển đổi (`Conversion Window`)

| Value | Mô tả |
|---|---|
| ONE_DAY_CLICK | 1 ngày sau khi nhấp chuột (`1 day after clicking`) |
| SEVEN_DAY_CLICK | 7 ngày sau khi nhấp chuột (`7 days after clicking`) |
| ONE_DAY_CLICK_OR_ONE_DAY_VIEW | 1 ngày sau khi nhấp chuột hoặc xem quảng cáo (`1 day after clicking or viewing`) |
| SEVEN_DAY_CLICK_OR_ONE_DAY_VIEW | 7 ngày sau khi nhấp chuột hoặc 1 ngày sau khi xem quảng cáo (`7 days after clicking or 1 day after viewing`) |

#### Định dạng nội dung sáng tạo (`Creative Type - ad_format`)

| Value | Mô tả |
|---|---|
| SINGLE_IMAGE | Một hình ảnh đơn lẻ (`A single image`). |
| SINGLE_VIDEO | Một video đơn lẻ (`A single video`). |
| CAROUSEL | Đã ngừng hỗ trợ (`Deprecated`). Bộ ảnh dạng thẻ xoay cho vị trí TopBuzz. |
| LIVE_CONTENT | Sự kiện phát trực tiếp (Live events). Chỉ hợp lệ cho kịch bản mua sắm trực tiếp (`promotion_type = LIVE_SHOPPING`). |
| CAROUSEL_ADS | Bộ ảnh dạng thẻ xoay (Carousel) cho vị trí hiển thị trên TikTok. |

#### Định dạng nội dung sáng tạo cũ (`Creative Type - Deprecated image_mode`)

Trường `image_mode` đã ngừng hỗ trợ. Các giá trị enum bên dưới chỉ mang tính chất tham khảo:

| Value | Mô tả | Aspect ratio | Kích thước tối thiểu | Kích thước tối đa | Kích thước khuyến nghị |
|---|---|---|---|---|---|
| IMAGE_MODE_GIF | Ảnh GIF (không dùng để tạo/sửa quảng cáo) | - | - | - | - |
| IMAGE_MODE_GROUP | Nhóm hình ảnh (không dùng để tạo/sửa quảng cáo) | - | - | - | - |
| IMAGE_MODE_LARGE | Ảnh lớn nằm ngang | 1.91 | 600 * 314 | 2400 * 1256 | 1200 * 628 |
| IMAGE_MODE_LARGE_VERTICAL | Ảnh lớn dạng dọc | 0.62 | 187 * 302 | 750 * 1208 | 375 * 604 |
| IMAGE_MODE_SMALL | Ảnh nhỏ (không dùng để tạo/sửa quảng cáo) | - | - | - | - |
| IMAGE_MODE_BIG_ONE | Ảnh vuông lớn | 1 | 320 * 320 | 1280 * 1280 | 640 * 640 |
| IMAGE_MODE_VIDEO | Video nằm ngang | 1.78 | 1280 * 720 | 2560 * 1400 | 1280 * 720 |
| IMAGE_MODE_VIDEO_SQUARE | Video vuông | 1 | 640 * 640 | 1280 * 1280 | 640 * 640 |
| IMAGE_MODE_VIDEO_VERTICAL | Video dọc | 0.56 | 720 * 1280 | 1440 * 2560 | 720 * 1280 |
| MULTI_SQUARE_PICTURES | Nhiều hình ảnh vuông | 1 | 640 * 640 | 640 * 640 | 640 * 640 |
| MULTI_RECTANGLE_PICTURES | Nhiều hình ảnh chữ nhật | 1.91 | 1200 * 628 | 1200 * 628 | 1200 * 628 |

#### Loại nội dung sáng tạo cho Mua sắm trên Shop (`Creative Types for Shop Purchases - creative_type`)

Loại sáng tạo cho kịch bản mua sắm tại gian hàng. Bắt buộc khi `objective_type` là `SHOP_PURCHASES`.

| Value | Mô tả |
|---|---|
| SHOP_PDP | Quảng cáo Shop với liên kết sản phẩm đơn lẻ. `ad_format` bắt buộc là `SINGLE_VIDEO`. |
| SHOP_PLP | Quảng cáo Shop với danh sách từ 6–50 liên kết sản phẩm. `ad_format` bắt buộc là `SINGLE_VIDEO`. |
| SHORT_VIDEO_LIVE | Video ngắn dẫn lưu lượng truy cập vào phòng mua sắm phát trực tiếp (live shopping room). `ad_format` bắt buộc là `SINGLE_VIDEO`. |
| DIRECT_LIVE | Phòng mua sắm trực tiếp (Live shopping room). Mỗi chiến dịch chỉ được có một phòng trực tiếp. `ad_format` bắt buộc là `LIVE_CONTENT`. |

#### Chiến lược đặt thầu sự kiện sâu (`Deep Event Bidding Strategy - deep_bid_type`)

Bạn có thể tối ưu hóa các sự kiện trong ứng dụng thông qua các phương thức đặt thầu khác nhau:

| Value | Mô tả |
|---|---|
| DEFAULT | Không đặt giá thầu sự kiện sâu |
| MIN | Đặt thầu kép (`Double bid`). Phương thức vận hành: Hệ thống TikTok Ads sẽ đặt thầu nhằm giữ chi phí trung bình xoay quanh mục tiêu của bạn, bao gồm cả chi phí cài đặt và chi phí mục tiêu sự kiện. Khuyến nghị dùng để duy trì mức chi phí ổn định cho cả hai giai đoạn.<br>**Lưu ý**: Điều này có thể làm giảm khối lượng cài đặt. |
| PACING | Tối ưu hóa tự động (`Automatic optimization`). Phương thức vận hành: Hệ thống TikTok Ads sẽ đặt thầu nhằm giữ chi phí cài đặt trung bình xoay quanh mục tiêu, đồng thời nhắm tới việc thu hút số lượng sự kiện mục tiêu tối đa.<br>**Khuyến nghị**: Duy trì chi phí ổn định quanh giá thầu cài đặt và đạt chi phí tối ưu cho mục tiêu sự kiện.<br>**Lưu ý**: Chi phí cho sự kiện mục tiêu có thể cao hơn so với chế độ Multi Bid. |
| VO_MIN | Đã ngừng hỗ trợ (`Deprecated`). Đặt giá thầu với giới hạn chi phí. Chỉ áp dụng cho Tối ưu hóa giá trị (`optimization_goal = VALUE`). Xem [Value Optimization](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1739381743067137). |
| VO_MIN_ROAS | Đặt giá thầu với mục tiêu ROAS. Chỉ áp dụng cho Tối ưu hóa giá trị (`optimization_goal = VALUE`). Xem [Value Optimization](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1739381743067137). |
| VO_HIGHEST_VALUE | Đặt giá thầu không giới hạn chi phí hoặc không yêu cầu mục tiêu ROAS. Chỉ áp dụng cho Tối ưu hóa giá trị (`optimization_goal = VALUE`). Xem [Value Optimization](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1739381743067137). |
| AEO | Đặt giá thầu cho Tối ưu hóa sự kiện trong ứng dụng (`App Event Optimization`). |

#### Giới tính (`Gender - gender`)

| Value | Mô tả |
|---|---|
| GENDER_UNLIMITED | Không giới hạn giới tính |
| GENDER_MALE | Nam (`Male`) |
| GENDER_FEMALE | Nữ (`Female`) |

#### Mã ngôn ngữ (`Language Code - languages`)

Sử dụng endpoint [/tool/language/](../12-api-reference/70-tools-p1.md#doc-1737188554152962) để lấy danh sách mã ngôn ngữ mới nhất.

| Value | Mô tả |
|---|---|
| ar | Tiếng Ả Rập (Arabic) |
| as | Tiếng Assam (Assamese) |
| bgc | Tiếng Haryanavi |
| bh | Tiếng Bihari |
| bn | Tiếng Bengal (Bengali) |
| cs | Tiếng Séc (Czech) |
| de | Tiếng Đức (German) |
| el | Tiếng Hy Lạp (Greek) |
| en | Tiếng Anh (English) |
| es | Tiếng Tây Ban Nha (Spanish) |
| fi | Tiếng Phần Lan (Finnish) |
| fr | Tiếng Pháp (French) |
| gu | Tiếng Gujarati |
| he | Tiếng Do Thái (Hebrew) |
| hi | Tiếng Hindi |
| hu | Tiếng Hungary (Hungarian) |
| id | Tiếng Indonesia |
| it | Tiếng Ý (Italian) |
| ja | Tiếng Nhật (Japanese) |
| kn | Tiếng Kannada |
| ko | Tiếng Hàn (Korean) |
| ml | Tiếng Malayalam |
| mr | Tiếng Marathi |
| ms | Tiếng Mã Lai (Malay) |
| nl | Tiếng Hà Lan (Dutch) |
| or | Tiếng Oriya |
| pa | Tiếng Punjab (Punjabi) |
| pl | Tiếng Ba Lan (Polish) |
| pt | Tiếng Bồ Đào Nha (Portuguese) |
| raj | Tiếng Rajasthani |
| ro | Tiếng Romania (Romanian) |
| ru | Tiếng Nga (Russian) |
| sv | Tiếng Thụy Điển (Swedish) |
| ta | Tiếng Tamil |
| te | Tiếng Telugu |
| th | Tiếng Thái (Thai) |
| tr | Tiếng Thổ Nhĩ Kỳ (Turkish) |
| uk | Tiếng Ukraina (Ukrainian) |
| vi | Tiếng Việt (Vietnamese) |
| zh | Tiếng Trung giản thể (Simplified Chinese) |
| zh-Hant | Tiếng Trung phồn thể (Traditional Chinese) |

#### Phiên bản Android tối thiểu (`Minimum Android Version - min_android_version`)

Sử dụng [/tool/os_version/](../12-api-reference/70-tools-p1.md#doc-1738308662898689) để lấy danh sách các phiên bản Android và iOS mới nhất.

| Value | Mô tả |
|---|---|
| NONE | Không giới hạn |
| 4.0 | Android 4.0 |
| 4.1 | Android 4.1 |
| 4.2 | Android 4.2 |
| 4.3 | Android 4.3 |
| 4.4 | Android 4.4 |
| 5.0 | Android 5.0 |
| 5.1 | Android 5.1 |
| 6.0 | Android 6.0 |
| 7.0 | Android 7.0 |
| 7.1 | Android 7.1 |
| 8.0 | Android 8.0 |
| 8.1 | Android 8.1 |
| 9.0 | Android 9.0 |
| 10.0 | Android 10.0 |
| 10.1 | Android 10.1 |
| 10.2 | Android 10.2 |
| 10.3 | Android 10.3 |
| 10.5 | Android 10.5 |
| 10.6 | Android 10.6 |
| 11.0 | Android 11.0 |
| 12.0 | Android 12.0 |
| 13.0 | Android 13.0 |

#### Phiên bản iOS tối thiểu (`Minimum iOS Version - min_ios_version`)

Sử dụng [/tool/os_version/](../12-api-reference/70-tools-p1.md#doc-1738308662898689) để lấy danh sách các phiên bản Android và iOS mới nhất.

| Value | Mô tả |
|---|---|
| NONE | Không giới hạn |
| 8.0 | iOS 8.0 |
| 8.1 | iOS 8.1 |
| 8.2 | iOS 8.2 |
| 8.3 | iOS 8.3 |
| 8.4 | iOS 8.4 |
| 9.0 | iOS 9.0 |
| 9.1 | iOS 9.1 |
| 9.2 | iOS 9.2 |
| 9.3 | iOS 9.3 |
| 10.1 | iOS 10.1 |
| 10.2 | iOS 10.2 |
| 10.3 | iOS 10.3 |
| 11.0 | iOS 11.0 |
| 11.1 | iOS 11.1 |
| 11.2 | iOS 11.2 |
| 11.3 | iOS 11.3 |
| 11.4 | iOS 11.4 |
| 12.0 | iOS 12.0 |
| 12.1 | iOS 12.1 |
| 12.2 | iOS 12.2 |
| 12.3 | iOS 12.3 |
| 12.4 | iOS 12.4 |
| 13.0 | iOS 13.0 |
| 13.1 | iOS 13.1 |
| 13.2 | iOS 13.2 |
| 13.3 | iOS 13.3 |
| 13.4 | iOS 13.4 |
| 13.5 | iOS 13.5 |
| 13.6 | iOS 13.6 |
| 13.7 | iOS 13.7 |
| 14.0 | iOS 14.0 |
| 14.1 | iOS 14.1 |
| 14.2 | iOS 14.2 |
| 14.3 | iOS 14.3 |
| 14.4 | iOS 14.4 |
| 14.5 | iOS 14.5 |
| 14.6 | iOS 14.6 |
| 14.7 | iOS 14.7 |
| 14.8 | iOS 14.8 |
| 15.0 | iOS 15.0 |
| 15.1 | iOS 15.1 |
| 15.2 | iOS 15.2 |
| 15.3 | iOS 15.3 |
| 15.4 | iOS 15.4 |
| 15.5 | iOS 15.5 |
| 15.6 | iOS 15.6 |
| 16.0 | iOS 16.0 |
| 16.1 | iOS 16.1 |
| 16.2 | iOS 16.2 |
| 16.3 | iOS 16.3 |
| 16.4 | iOS 16.4 |

#### Hệ điều hành (`Operating System - operating_systems`)

| Value | Mô tả |
|---|---|
| ANDROID | Hệ điều hành Android |
| IOS | Hệ điều hành iOS |
| PCDeprecated | Máy tính để bàn (PC) - đã ngừng hỗ trợ (`Deprecated`) |

#### Mục tiêu tối ưu hóa (`Optimization Goal - optimization_goal`)

| Value | Mô tả |
|---|---|
| CLICK | Lượt nhấp chuột (`Clicks`). Tương ứng với mục tiêu Clicks khi: `shopping_ads_type = VIDEO` và `product_source` là `STORE` hoặc `SHOWCASE`; hoặc `shopping_ads_type = LIVE`; hoặc `shopping_ads_type = PRODUCT_SHOPPING_ADS` và `product_source = STORE`. |
| CONVERT | Lượt chuyển đổi / Lượt mua / Bắt đầu thanh toán (`Conversion/Purchases/Initiate checkouts`). Khi `optimization_event = SHOPPING`, tương ứng với Lượt mua hàng (Purchases). Khi `optimization_event = INITIATE_ORDER`, tương ứng với Bắt đầu thanh toán (Initiate checkouts). |
| INSTALL | Lượt cài đặt ứng dụng (`Install`). Để dùng "Cài đặt kèm sự kiện trong ứng dụng" trên vị trí Pangle hoặc Global App Bundle trong nhóm quảng cáo, đặt `optimization_goal = INSTALL`, chỉ định giá trị hợp lệ cho `secondary_optimization_event` và chỉ bao gồm `PLACEMENT_PANGLE` hoặc `PLACEMENT_GLOBAL_APP_BUNDLE`.<br>**Lưu ý**: Từ 30/11/2024 không hỗ trợ tạo mới mục tiêu này trên vị trí TikTok hoặc Vị trí tự động. |
| IN_APP_EVENT | Sự kiện trong ứng dụng (`In-app event`). |
| SHOW | Lượt hiển thị (`Impression`). |
| VIDEO_VIEW | Lượt xem video. Đã ngừng hỗ trợ (`Deprecated`). |
| REACH | Số người tiếp cận (`Reach`). |
| LEAD_GENERATION | Khách hàng tiềm năng (`Leads`). |
| LEADS | Khách hàng tiềm năng (`Leads`). Hiển thị quảng cáo tới những người có khả năng chuyển đổi hoặc chia sẻ thông tin liên hệ cao nhất. |
| WEBSITE_ENGAGEMENT | Lượt tương tác trang web (`Website engagements`). Hiển thị tới người có nhiều khả năng thực hiện hành động ý nghĩa (xem nội dung, thêm vào danh sách mong muốn...). |
| CONVERSATION | Cuộc trò chuyện (`Conversations`). Hiển thị quảng cáo tới những người có khả năng bắt đầu cuộc trò chuyện tin nhắn trực tiếp trên TikTok hoặc qua ứng dụng nhắn tin tức thì. Tính năng yêu cầu danh sách cho phép (allowlist). Khi chọn, `optimization_event` mặc định là `MESSAGE`. |
| FOLLOWERS | Lượt theo dõi (`Follows`). |
| PROFILE_VIEWS | Lượt truy cập trang hồ sơ TikTok (Sắp ngừng hỗ trợ, khuyến nghị dùng `PAGE_VISIT`). |
| PAGE_VISIT | Lượt truy cập trang TikTok. Điều hướng lưu lượng đến nhiều loại trang TikTok khác nhau (trang hồ sơ, danh sách phát, trang hashtag, trang âm nhạc, hiệu ứng thương hiệu hoặc TikTok Instant Page). Chỉ dùng khi `objective_type = ENGAGEMENT`. |
| VALUE | Giá trị / Tổng doanh thu (`Value/Gross revenue`). Xem [Bật tối ưu hóa dựa trên giá trị (Enable Value-Based Optimization)](../09-marketing-api/quan-ly-chien-dich-tom-tat.md#doc-1770019181843458). |
| AUTOMATIC_VALUE_OPTIMIZATION | Tối ưu hóa giá trị tự động (`Automatic Value Optimization`). Tự động tối ưu hóa giá trị cao nhất hoặc phân phối tối đa thông qua máy học. Yêu cầu danh sách cho phép (allowlist). |
| GMV | Bộ lọc kết hợp để chọn chiến dịch, nhóm quảng cáo và quảng cáo với: `objective_type = PRODUCT_SALES`, `optimization_goal = VALUE`, `campaign_product_source = STORE`, và `shopping_ads_type = VIDEO/LIVE/PRODUCT_SHOPPING_ADS`. Không dùng để tạo nhóm quảng cáo. |
| PURCHASES | Bộ lọc kết hợp: `objective_type = PRODUCT_SALES`, `optimization_goal = CONVERT`, `campaign_product_source = STORE`, và `optimization_event = SHOPPING`. Chỉ dùng để lọc dữ liệu. |
| INITIATE_CHECKOUTS | Bộ lọc kết hợp: `objective_type = PRODUCT_SALES`, `optimization_goal = CONVERT`, `campaign_product_source = STORE`, và `optimization_event = INITIATE_ORDER`. Chỉ dùng để lọc dữ liệu. |
| MT_LIVE_ROOM | Thời gian giữ chân người xem phòng mua sắm trực tiếp (Live shopping room viewer retention). Sự kiện tương ứng: `LIVE_STAY_TIME`. |
| PRODUCT_CLICK_IN_LIVE | Nhấp vào liên kết sản phẩm trong phiên Live. Sự kiện tương ứng: `LIVE_CLICK_PRODUCT_ACTION`. |
| ENGAGED_VIEW | Lượt xem 6 giây tập trung (`Focused view`). Số lần video được phát ít nhất 6 giây hoặc nhận được ít nhất 1 tương tác trong 1 ngày kể từ khi xem quảng cáo trả phí. |
| ENGAGED_VIEW_FIFTEEN | Lượt xem 15 giây tập trung (`15-second focused view`). Số lần video được phát ít nhất 15 giây hoặc nhận 1 tương tác trong 1 ngày. Hệ thống tự gán `ENGAGED_VIEW_FIFTEEN` vào `optimization_event`. |
| TRAFFIC_LANDING_PAGE_VIEW | Lượt xem trang đích (`Landing Page View`). Người dùng nhấp chuột và tải trang đích thành công. Sự kiện tương ứng là `LANDING_PAGE_VIEW`. Xem [Tối ưu hóa lượt xem trang đích](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1775099621140482). |
| CONVERSION_LEADS | Khách hàng tiềm năng chuyển đổi. Đã ngừng hỗ trợ (`Deprecated`). |
| DESTINATION_VISIT | Truy cập trang đích (`Destination Visit`). Giới thiệu người dùng vào trang trong ứng dụng hoặc chuyển tiếp sang website. Tính năng yêu cầu danh sách cho phép (allowlist). |
| PREFERRED_LEAD | Khách hàng tiềm năng ưu tiên (`Preferred Leads`). Hiển thị quảng cáo cho những người đáp ứng tốt nhất các điều kiện phân loại khách hàng tiềm năng ưu tiên của bạn. |

#### Vị trí hiển thị (`Placement - placements`)

| Value | Mô tả |
|---|---|
| PLACEMENT_TIKTOK | Nền tảng TikTok |
| PLACEMENT_PANGLE | Pangle (trước đây là TikTok Audience Network) |
| PLACEMENT_GLOBAL_APP_BUNDLE | Global App Bundle, hiện bao gồm CapCut và Fizzo. Không hỗ trợ mục tiêu tối ưu hóa Lượt xem trang đích (`TRAFFIC_LANDING_PAGE_VIEW`). |
| PLACEMENT_TOPBUZZ | Đã ngừng hỗ trợ (`Deprecated`). BuzzVideo/Babe |
| PLACEMENT_HELO | Đã ngừng hỗ trợ (`Deprecated`). Nền tảng Helo |

#### Trạng thái chính (`Primary Status`)

> [!NOTE]
> Xem [Trạng thái phụ được hỗ trợ cho từng trạng thái chính](../09-marketing-api/quan-ly-chien-dich-tom-tat.md#doc-1757239620352002) để biết thêm chi tiết.

| Value | Mô tả |
|---|---|
| STATUS_DELETE | Đã xóa |
| STATUS_DELIVERY_OK | Quảng cáo đang phân phối |
| STATUS_DISABLE | Bị tạm dừng |
| STATUS_NOT_DELIVERY | Quảng cáo không trong quá trình phân phối |
| STATUS_TIME_DONE | Đã hoàn tất (trạng thái này không tồn tại đối với cấp chiến dịch) |
| STATUS_RF_CLOSED | Nhóm quảng cáo R&F đã đóng (khả dụng cho nhóm quảng cáo và quảng cáo R&F) |
| STATUS_FROZEN | Nhóm quảng cáo R&F bị đóng băng (khả dụng cho quảng cáo R&F) |
| STATUS_ALL | Tất cả trạng thái (bao gồm cả "Đã xóa") |
| STATUS_NOT_DELETE | Tất cả trạng thái (không bao gồm "Đã xóa"). Đây là bộ lọc mặc định trong báo cáo đồng bộ cho các loại BASIC, AUDIENCE hoặc CATALOG. |

#### Loại quảng bá / Vị trí tối ưu hóa (`Promotion Type - promotion_type`)

| Value | Mô tả |
|---|---|
| APP_ANDROID | Ứng dụng Android |
| APP_IOS | Ứng dụng iOS |
| MINI_APP | TikTok Minis thuộc loại chuỗi phim ngắn (mini series). Chỉ áp dụng trong Upgraded Smart+ Minis Ads (`app_promotion_type = MINIS`). |
| MINI_GAME | TikTok Minis thuộc loại trò chơi nhỏ (mini game). Chỉ áp dụng trong Upgraded Smart+ Minis Ads (`app_promotion_type = MINIS`). |
| GAME | Trò chơi (Game). Chỉ áp dụng cho chiến dịch quảng bá bài viết ứng dụng (`app_promotion_type = APP_POSTS_PROMOTION`). Hiện chỉ hỗ trợ cập nhật hoặc truy xuất qua API. |
| WEBSITE | Trang đích trang web (Landing page) |
| LEAD_GENERATION | Biểu mẫu tức thì hoặc Trang web cho quảng cáo tạo khách hàng tiềm năng. Đi kèm với `promotion_target_type` là `INSTANT_PAGE` hoặc `EXTERNAL_WEBSITE`. |
| LEAD_GEN_CLICK_TO_TT_DIRECT_MESSAGE | Thu thập khách hàng tiềm năng qua tin nhắn trực tiếp TikTok. Khả dụng công khai tại khu vực APAC (bao gồm Việt Nam) và LATAM; các khu vực khác cần allowlist. |
| LEAD_GEN_CLICK_TO_SOCIAL_MEDIA_APP_MESSAGE | Thu thập khách hàng tiềm năng qua ứng dụng nhắn tin mạng xã hội / ứng dụng tin nhắn tức thì. Khả dụng công khai tại khu vực APAC (bao gồm Việt Nam); các khu vực khác cần allowlist. |
| LEAD_GEN_CLICK_TO_CALL | Thu thập khách hàng tiềm năng qua cuộc gọi điện thoại (yêu cầu allowlist). |
| WEBSITE_OR_DISPLAY | Trang đích hoặc trang hiển thị thuần túy. Chỉ dùng cho các mục tiêu chiến dịch (Reach / Video Views / Engagement) nơi `landing_page_url` là tùy chọn. |
| TIKTOK_SHOP | Gian hàng / cửa hàng TikTok Shop |
| VIDEO_SHOPPING | Áp dụng khi `shopping_ads_type = VIDEO` và `product_source` là `STORE` hoặc `SHOWCASE`. Gắn sản phẩm vào video để người dùng nhấp vào mua hàng. |
| LIVE_SHOPPING | Áp dụng khi `shopping_ads_type = LIVE`. Quảng bá sản phẩm trong video trực tiếp. |
| PSA_PRODUCT | Áp dụng khi `shopping_ads_type = PRODUCT_SHOPPING_ADS`. Tận dụng lưu lượng từ Trung tâm mua sắm (Shopping Center) và Tìm kiếm (Search). |

#### Loại mua Reach & Frequency (`Reach & Frequency Buy Type - rf_purchased_type`)

| Value | Mô tả |
|---|---|
| FIXED_SHOW | Mua để đạt được một số lượng lượt hiển thị cố định. |
| FIXED_REACH | Mua để tiếp cận một số lượng người dùng cố định. |

#### Loại lịch chạy (`Schedule Type - schedule_type`)

| Value | Mô tả |
|---|---|
| SCHEDULE_FROM_NOW | Phân phối liên tục kể từ thời điểm hiện tại |
| SCHEDULE_START_END | Thiết lập thời gian bắt đầu và kết thúc cụ thể |

---

### Báo cáo (`Reporting`)

#### Tiêu chí nhóm trong Báo cáo đối tượng (`Audience Report Grouping Criteria`)

| Value | Mô tả |
|---|---|
| GENDER | Nhóm theo giới tính |
| AGE | Nhóm theo độ tuổi |
| COUNTRY | Nhóm theo quốc gia |
| AC | Nhóm theo mạng kết nối (`network`) |
| LANGUAGE | Nhóm theo ngôn ngữ |
| PLATFORM | Nhóm theo hệ điều hành |
| INTEREST_CATEGORY | Nhóm theo sở thích |
| PLACEMENT | Nhóm theo vị trí hiển thị |

#### Thứ tự sắp xếp Báo cáo đối tượng (`Audience Report Sort Order`)

| Value | Mô tả |
|---|---|
| click_cnt | Sắp xếp theo số lượt nhấp chuột |
| convert_cnt | Sắp xếp theo số lượt chuyển đổi |
| convert_cost | Sắp xếp theo chi phí mỗi lượt chuyển đổi (CPA) |
| convert_rate | Sắp xếp theo tỷ lệ chuyển đổi (CVR) |
| ctr | Sắp xếp theo tỷ lệ nhấp chuột (CTR) |
| show_cnt | Sắp xếp theo số lượt hiển thị |
| stat_cost | Sắp xếp theo chi phí tiêu hao |

---

### Quản lý ứng dụng di động (`Mobile App Management`)

#### Dòng thiết bị (`Device Model`)

Sử dụng endpoint [Lấy dòng thiết bị (Get device models)](../12-api-reference/70-tools-p1.md#doc-1737172880570369) để lấy danh sách thiết bị mới nhất.

| Value |
|---|
| iPhone 13/13 Mini/13 Pro/13 Pro Max |
| iPhone 11 Pro Max/XS Max |
| iPhone 11 Pro/X/XS |
| iPhone 11/XR |
| iPhone 6/6s/7/8 |
| iPhone 6/7/8 Plus |
| iPhone 5/5s/5c/SE |
| iPhone 4/4s |
| OPPO A3s |
| OPPO A5s |
| OPPO A71 |
| OPPO F7 |
| OPPO F9 |
| OPPO R15 |
| VIVO Y91i |
| VIVO X20A |
| RedMi 5A |
| RedMi 6A |
| RedMi Y2 |
| Redmi Note 4 |
| RedMi Note 5 Pro |
| RedMi Note 6 Pro |
| SAMSUNG Galaxy J2 |
| SAMSUNG Galaxy J2 Prime |
| SAMSUNG Galaxy J7 Nxt |
| SAMSUNG Galaxy J7 Prime |
| SAMSUNG Galaxy A10 |
| SAMSUNG Galaxy S8 |
| HUAWEI P30 |
| Google Pixel 3XL |

#### Mẫu khung kết thúc (`Frame Template Type`)

| Value | Bố cục (Layout) | Mô tả |
|---|---|---|
| END_FRAME_HORIZONTAL_1 | Ngang (`Horizontal`) | Mẫu khung ngang với logo hình vuông, khẩu hiệu và tên thương hiệu sử dụng phông chữ nhỏ. |
| END_FRAME_HORIZONTAL_2 | Ngang (`Horizontal`) | Mẫu khung ngang với logo hình vuông, khẩu hiệu và tên thương hiệu phông lớn. |
| END_FRAME_HORIZONTAL_3 | Ngang (`Horizontal`) | Mẫu khung ngang với logo hình chữ nhật, khẩu hiệu phông nhỏ. Không hỗ trợ tên thương hiệu. |
| END_FRAME_HORIZONTAL_4 | Ngang (`Horizontal`) | Mẫu khung ngang với logo hình vuông, khẩu hiệu và tên thương hiệu phông vừa. |
| END_FRAME_HORIZONTAL_5 | Ngang (`Horizontal`) | Mẫu khung ngang với logo hình chữ nhật, khẩu hiệu phông vừa. Không hỗ trợ tên thương hiệu. |
| END_FRAME_VERTICAL_1 | Dọc (`Vertical`) | Mẫu khung dọc với logo hình vuông, khẩu hiệu và tên thương hiệu phông nhỏ. |
| END_FRAME_VERTICAL_2 | Dọc (`Vertical`) | Mẫu khung dọc với logo hình vuông, khẩu hiệu và tên thương hiệu phông lớn. |
| END_FRAME_VERTICAL_3 | Dọc (`Vertical`) | Mẫu khung dọc với logo hình chữ nhật, khẩu hiệu phông nhỏ. Không hỗ trợ tên thương hiệu. |
| END_FRAME_VERTICAL_4 | Dọc (`Vertical`) | Mẫu khung dọc với logo hình vuông, khẩu hiệu và tên thương hiệu phông vừa. |
| END_FRAME_VERTICAL_5 | Dọc (`Vertical`) | Mẫu khung dọc với logo hình chữ nhật, khẩu hiệu phông vừa. Không hỗ trợ tên thương hiệu. |

#### Thẻ tài liệu sáng tạo (`Material Tag`)

| Name | Mô tả | Kiểu áp dụng |
|---|---|---|
| title | Tên sản phẩm | Văn bản (`Text`) |
| price | Giá sản phẩm | Văn bản (`Text`) |
| description | Mô tả sản phẩm (mặc định cho văn bản) | Văn bản (`Text`) |
| logo | Logo thương hiệu | Hình ảnh (`Image`) |
| image | Hình ảnh sản phẩm (mặc định cho ảnh) | Hình ảnh (`Image`) |
| video | Video sản phẩm (mặc định cho video) | Video |

#### Trạng thái tác vụ (`Task Status`)

| Value | Mô tả |
|---|---|
| CREATED | Tác vụ đã được tạo |
| PROCESSING | Tác vụ đang được xử lý |
| SUCCESS | Tác vụ thành công |
| FAILED | Tác vụ thất bại |

#### Đối tác đo lường bên thứ ba (`Third-party Monitoring Partners`)

| Value | Mô tả |
|---|---|
| AdBrix | Adbrix |
| Adjust | Adjust |
| Adzcore | Đã ngừng hỗ trợ (`Deprecated`). Party |
| AppAdforce | Đã ngừng hỗ trợ (`Deprecated`). F.O.X |
| AppLink | Branch |
| AppMetrica | Đã ngừng hỗ trợ (`Deprecated`). AppMetrica |
| AppsFlyer | Appsflyer |
| DoubleClick | DCM (Double Click) |
| FlashTalking | FlashTalking |
| Huangbaoche | Đã ngừng hỗ trợ (`Deprecated`). Sensors Data |
| Kochava | Kochava |
| Lazada | Đã ngừng hỗ trợ (`Deprecated`). Alibaba Group |
| LeadBolt | Đã ngừng hỗ trợ (`Deprecated`). Leadbolt |
| Metaps | Đã ngừng hỗ trợ (`Deprecated`). Metaps |
| ServingsSys | Sizmek |
| Singular | Singular |
| Tenjin | Tenjin |
| TlnkIo | Tune |
| Vidoadsplus | Đã ngừng hỗ trợ (`Deprecated`). Vidoadsplus |
| myTracker | Đã ngừng hỗ trợ (`Deprecated`). myTracker |

---

### Quản lý tệp đối tượng (`Audience Management`)

#### Loại tệp đối tượng (`Audience Type`)

| Value | Mô tả |
|---|---|
| ENGAGEMENT | Đối tượng tương tác (`Engagement Audience`) |
| APP | Đối tượng hoạt động ứng dụng (`App Activity Audience`) |
| PIXEL | Đối tượng lưu lượng truy cập trang web (`Website Traffic Audience`) |
| LEAD_GENERATION | Đối tượng khách hàng tiềm năng (`Lead Generation Audience`) |
| TIKTOK_SHOP | Đối tượng hoạt động cửa hàng (`Shop Activity Audience`) |
| ENGAGEMENT_ORGANIC_VIDEO | Đối tượng tương tác video tự nhiên (`Organic Engagement Audience`) |
| ENGAGEMENT_LIVE_VIDEO | Đối tượng tương tác video trực tiếp (`Live Engagement Audience`) |
| OFFLINE | Đối tượng hoạt động ngoại tuyến (`Offline Activity Audience`) |

#### Phương thức mã hóa (`Encryption Type - calculate_type`)

| Value | Mô tả |
|---|---|
| FIRST_SHA256 | Giá trị gốc của IDFA hoặc GAID được mã hóa bằng thuật toán SHA256. |
| FIRST_MD5 | Giá trị gốc của IDFA hoặc GAID được mã hóa bằng thuật toán MD5. |
| EMAIL_SHA256 | Địa chỉ email được mã hóa bằng SHA256. |
| PHONE_SHA256 | Số điện thoại được mã hóa bằng SHA256. |
| IDFA_SHA256 | Apple IDFA (Identifier for Advertisers) được mã hóa bằng SHA256. |
| IDFA_MD5 | IDFA được mã hóa bằng MD5. |
| GAID_SHA256 | GAID (Google Advertising ID) được mã hóa bằng SHA256. |
| GAID_MD5 | GAID được mã hóa bằng MD5. |
| MULTIPLE_TYPES | Nhiều loại định danh kết hợp. Chỉ áp dụng cho Đối tượng tệp khách hàng tạo qua File API. |
| FIRST_NORMAL | Đã ngừng hỗ trợ (`deprecated`). Dữ liệu thô của IDFA hoặc GAID. |

#### Trường lọc (`Filter Field`)

| Value | Mô tả |
|---|---|
| EVENT | Trường lọc là sự kiện (`event`) |

#### Toán tử lọc (`Filter Operator`)

| Value | Mô tả |
|---|---|
| EQ | Toán tử bằng (FIELD = VALUE) |

#### Giá trị bộ lọc (`Filter Value`)

| Value | Mô tả |
|---|---|
| Engagement Audience values | Các giá trị cho đối tượng tương tác quảng cáo |
| ↳ CLICK | Sự kiện nhấp chuột vào quảng cáo video |
| ↳ IMPRESSION | Sự kiện hiển thị quảng cáo video |
| ↳ PLAY 2S | Sự kiện xem video ít nhất 2 giây |
| ↳ PLAY 6S | Sự kiện xem video ít nhất 6 giây |
| ↳ PLAY 25 | Sự kiện xem đạt 25% thời lượng video |
| ↳ PLAY 50 | Sự kiện xem đạt 50% thời lượng video |
| ↳ PLAY 75 | Sự kiện xem đạt 75% thời lượng video |
| ↳ PLAY OVER | Sự kiện xem toàn bộ 100% video |
| ↳ ENGAGEMENT APP PROFILE CLICK | Sự kiện nhấp chuột vào trang hồ sơ ứng dụng |
| ↳ ENGAGEMENT APP PROFILE IMPRESSION | Sự kiện hiển thị trang hồ sơ ứng dụng |
| ↳ ENGAGEMENT TIKTOK INSTANT CLICK | Sự kiện nhấp chuột vào TikTok Instant Page |
| ↳ ENGAGEMENT TIKTOK INSTANT IMPRESSION | Sự kiện hiển thị TikTok Instant Page |
| ↳ ENGAGEMENT COLLECTION ADS CLICK | Sự kiện nhấp chuột vào Collection ads |
| ↳ ENGAGEMENT COLLECTION ADS IMPRESSION | Sự kiện hiển thị Collection ads |
| Live Engagement Audience values | Các giá trị cho đối tượng tương tác Live |
| ↳ LIVE VIDEO VIEW | Lượt xem phiên trực tiếp |
| ↳ LIVE VIDEO ENGAGEMENT | Lượt tương tác trong phiên trực tiếp |
| Organic Engagement Audience | Các giá trị cho đối tượng tương tác video tự nhiên |
| ↳ ORGANIC VIDEO PLAY 2S | Xem video tự nhiên 2 giây |
| ↳ ORGANIC VIDEO PLAY 6S | Xem video tự nhiên 6 giây |
| ↳ ORGANIC VIDEO PLAY OVER | Xem video tự nhiên 100% |
| ↳ ORGANIC VIDEO ENGAGEMENT | Tương tác với video tự nhiên |
| App Audience values | Các giá trị cho đối tượng người dùng ứng dụng |
| ↳ INSTALL | Sự kiện cài đặt ứng dụng |
| ↳ DAY 2 RETENTION | Sự kiện giữ chân ngày thứ 2 |
| ↳ APP ADD PAYMENT INFO | Sự kiện thêm thông tin thanh toán trong ứng dụng |
| ↳ APP ADD TO CART | Sự kiện thêm vào giỏ hàng trong ứng dụng |
| ↳ ADD TO WiSHLIST | Sự kiện thêm vào danh sách mong muốn |
| ↳ LAUNCH APP | Sự kiện mở/khởi chạy ứng dụng |
| ↳ CHECKOUT | Sự kiện thanh toán |
| ↳ COMPLETE TUTORIAL | Sự kiện hoàn thành hướng dẫn |
| ↳ VIEW CONTENT | Sự kiện xem nội dung |
| ↳ CREATE GROUP | Sự kiện tạo nhóm |
| ↳ CREATE ROLE | Sự kiện tạo nhân vật/vai trò |
| ↳ GENERATE LEAD | Sự kiện tạo khách hàng tiềm năng |
| ↳ IN-APP AD CLICK | Sự kiện nhấp vào quảng cáo trong ứng dụng |
| ↳ IN-APP AD IMPRESSION | Sự kiện hiển thị quảng cáo trong ứng dụng |
| ↳ JOIN GROUP | Sự kiện tham gia nhóm |
| ↳ ACHIEVE LEVEL | Sự kiện đạt cấp độ trong trò chơi |
| ↳ LOAN APPLY | Sự kiện đăng ký khoản vay |
| ↳ LOAN APPROVAL | Sự kiện phê duyệt khoản vay |
| ↳ LOAN DISBURSAL | Sự kiện giải ngân khoản vay |
| ↳ LOGIN | Sự kiện đăng nhập |
| ↳ PURCHASE | Sự kiện mua hàng trong ứng dụng |
| ↳ RATE | Sự kiện đánh giá |
| ↳ REGISTRATION | Sự kiện đăng ký tài khoản |
| ↳ APP SEARCH | Sự kiện tìm kiếm trong ứng dụng |
| ↳ SPEND CREDITS | Sự kiện tiêu hao tín dụng/điểm thưởng |
| ↳ START TRIAL | Sự kiện bắt đầu dùng thử |
| ↳ SUBSCRIBE | Sự kiện đăng ký thuê bao |
| ↳ UNLOCK ACHIEVEMENT | Sự kiện mở khóa thành tựu |
| Pixel Audience values | Các giá trị cho đối tượng lưu lượng Pixel |
| ↳ PAGE BROWSE | Xem trang (`Page View`). Khách truy cập vào website |
| ↳ CLICK BUTTON | Sự kiện nhấp nút |
| ↳ PIXEL SUBMIT FORM | Sự kiện gửi biểu mẫu |
| ↳ CONTACT | Sự kiện liên hệ/tư vấn |
| ↳ DOWNLOAD | Sự kiện nhấp nút tải xuống |
| ↳ PIXEL ADD PAYMENT INFO | Sự kiện thêm thông tin thanh toán trên web |
| ↳ COMPLETE PAYMENT | Sự kiện hoàn tất thanh toán |
| ↳ INITIATE CHECKOUT | Sự kiện bắt đầu thanh toán |
| ↳ COMPLETE REGISTRATION | Sự kiện hoàn tất đăng ký |
| ↳ PRODUCT DETAIL PAGE BROWSE | Sự kiện xem trang chi tiết sản phẩm (`View Content`) |
| ↳ PIXEL SEARCH | Sự kiện tìm kiếm trên website |
| ↳ PIXEL ADD TO CART | Sự kiện thêm vào giỏ hàng trên website |
| ↳ PLACE AN ORDER | Sự kiện đặt đơn hàng |
| ↳ PIXEL ADD TO WISHLIST | Sự kiện thêm vào danh sách mong muốn |
| ↳ PIXEL SUBSCRIBE | Sự kiện đăng ký trên website |
| Lead Generation Audience values | Các giá trị cho đối tượng tạo khách hàng tiềm năng |
| ↳ LEAD GENERATION FORM SUBMISSION | Sự kiện gửi biểu mẫu tìm kiếm khách hàng tiềm năng |
| ↳ FORM VIEW | Sự kiện xem biểu mẫu |
| Shop Activity Audience values | Các giá trị đối tượng hoạt động gian hàng TikTok Shop |
| ↳ TIKTOK SHOP PAGE VIEW | Lượt xem trang chi tiết sản phẩm trên TikTok Shop |
| ↳ TIKTOK SHOP ADD TO CART | Thêm vào giỏ hàng trên TikTok Shop |
| ↳ TIKTOK SHOP INITIATE CHECKOUT | Bắt đầu thanh toán trên TikTok Shop |
| ↳ TIKTOK SHOP COMPLETE PAYMENT | Hoàn tất thanh toán trên TikTok Shop |
| Business Account Audience values | Các giá trị đối tượng tài khoản doanh nghiệp |
| ↳ BUSINESS ACCOUNT PROFILE FOLLOW | Theo dõi tài khoản doanh nghiệp |
| ↳ BUSINESS ACCOUNT PROFILE VISIT | Truy cập hồ sơ doanh nghiệp |
| ↳ BUSINESS ACCOUNT ENGAGEMENT | Tương tác video (Thích/Chia sẻ/Bình luận) |
| ↳ BUSINESS ACCOUNT PLAY 2S | Xem video 2 giây |
| ↳ BUSINESS ACCOUNT PLAY 6S | Xem video 6 giây |
| ↳ BUSINESS ACCOUNT PLAY OVER | Xem video 100% |
| Offline Audience values | Các giá trị đối tượng sự kiện ngoại tuyến |
| ↳ OFFLINE COMPLETE PAYMENT | Hoàn tất thanh toán ngoại tuyến |
| ↳ OFFLINE CONTACT | Liên hệ ngoại tuyến |
| ↳ OFFLINE SUBMIT FORM | Gửi biểu mẫu ngoại tuyến |
| ↳ OFFLINE SUBSCRIBE | Đăng ký ngoại tuyến |
| ↳ OFFLINE ADD PAYMENT INFO | Thêm thông tin thanh toán ngoại tuyến |
| ↳ OFFLINE ADD TO CART | Thêm vào giỏ hàng ngoại tuyến |
| ↳ OFFLINE ADD TO WISHLIST | Thêm vào danh sách mong muốn ngoại tuyến |
| ↳ OFFLINE CLICK BUTTON | Nhấp nút ngoại tuyến |
| ↳ OFFLINE COMPLETE REGISTRATION | Hoàn tất đăng ký ngoại tuyến |
| ↳ OFFLINE DOWNLOAD | Tải xuống ngoại tuyến |
| ↳ OFFLINE INITIATE CHECKOUT | Bắt đầu thanh toán ngoại tuyến |
| ↳ OFFLINE PLACE AN ORDER | Đặt đơn hàng ngoại tuyến |

#### Khu vực áp dụng đối tượng tương tự (`Lookalike Locations`)

| Value | Mô tả quốc gia / khu vực |
|---|---|
| AE | Các Tiểu vương quốc Ả Rập Thống nhất (United Arab Emirates) |
| AU | Úc (Australia) |
| AZ | Azerbaijan |
| BG | Bulgaria |
| BO | Bolivia |
| CA | Canada |
| CY | Síp (Cyprus) |
| DE | Đức (Germany) |
| DZ | Algérie (Algeria) |
| EE | Estonia |
| EG | Ai Cập (Egypt) |
| ES | Tây Ban Nha (Spain) |
| FR | Pháp (France) |
| GB | Vương quốc Anh (United Kingdom) |
| HR | Croatia |
| ID | Indonesia |
| IL | Israel |
| IN | Ấn Độ (India) |
| IT | Ý (Italy) |
| JP | Nhật Bản (Japan) |
| KE | Kenya |
| KR | Hàn Quốc (Korea) |
| LK | Sri Lanka |
| LT | Litva (Lithuania) |
| LV | Latvia |
| MY | Malaysia |
| PL | Ba Lan (Poland) |
| PR | Puerto Rico |
| PY | Paraguay |
| RS | Serbia |
| RU | Nga (Russia) |
| SA | Ả Rập Xê Út (Saudi Arabia) |
| SI | Slovenia |
| SK | Slovakia |
| TH | Thái Lan (Thailand) |
| TR | Thổ Nhĩ Kỳ (Turkey) |
| TW | Đài Loan, Trung Quốc (Taiwan, China) |
| US | Hoa Kỳ (United States) |
| VN | Việt Nam (Vietnam) |

#### Quy mô đối tượng tương tự (`Lookalike Size`)

| Value | Mô tả |
|---|---|
| NARROW | Quy mô hẹp, độ tương đồng cao nhất |
| BALANCED | Quy mô cân bằng |
| BROAD | Quy mô rộng, mở rộng phạm vi tiếp cận |

#### Hệ thống đối tượng tương tự (`Lookalike System - system`)

| Value | Mô tả |
|---|---|
| ALL | Cả hai hệ điều hành iOS và Android |
| IOS | Hệ điều hành iOS |
| ANDROID | Hệ điều hành Android |

#### Khoảng thời gian lưu giữ dữ liệu (`Lookback window - retention_days`)

| Value | Mô tả |
|---|---|
| 7 | Xem lại dữ liệu trong 7 ngày qua |
| 14 | Xem lại dữ liệu trong 14 ngày qua |
| 30 | Xem lại dữ liệu trong 30 ngày qua |
| 60 | Xem lại dữ liệu trong 60 ngày qua |
| 90 | Xem lại dữ liệu trong 90 ngày qua |
| 180 | Xem lại dữ liệu trong 180 ngày qua |

#### Toán tử bộ quy tắc (`Rule Set Operator - operator`)

| Value | Mô tả |
|---|---|
| OR | Dùng toán tử `or` để liên kết các quy tắc (rule1 hoặc rule2 hoặc...) |

---

### Quản lý nội dung sáng tạo (`Creative Management`)

#### Nhãn danh mục (`Category Labels`)

| Value |
|---|
| Action |
| Adventure |
| Arcade |
| Art&Design |
| Auto&Vehicles |
| Beauty |
| Board |
| Book |
| Books |
| Books&Reference |
| Business |
| Card |
| Casino |
| Casual |
| Catalogs |
| Comics |
| Communication |
| Dating |
| DeveloperTools |
| Education |
| Educational |
| Entertainment |
| Events |
| Finance |
| Food&Drink |
| FoodandDrink |
| Games |
| Graphics&Design |
| Health&Fitness |
| HealthandFitness |
| House&Home |
| Libraries&Demo |
| Lifestyle |
| Magazines&Newspaper |
| MagazinesandNewspapers |
| Maps&Navigation |
| Medical |
| Music |
| Music&Audio |
| Navigation |
| News |
| News&Magazines |
| Parenting |
| Personalization |
| Photo&Video |
| PhotoandVideo |
| Photography |
| Productivity |
| Puzzle |
| Racing |
| Reference |
| RolePlaying |
| Shopping |
| Simulation |
| Social |
| SocialNetworking |
| Sports |
| Stickers |
| Strategy |
| Tools |
| Travel |
| Travel&Local |
| Trivia |
| Utilities |
| VideoPlayers&Editors |
| Weather |
| Word |

#### Loại thiết bị (`Device Type`)

Sử dụng endpoint [Lấy dòng thiết bị (Get device models)](../12-api-reference/70-tools-p1.md#doc-1737172880570369) để nhận danh sách mới nhất.

#### Nguồn tài liệu sáng tạo (`Material Source - source`)

| Value | Mô tả |
|---|---|
| UPLOADED | Do người dùng tải lên |
| CREATIVE_TOOL_OTHERS | Các công cụ sáng tạo khác |
| CREATIVE_TOOL_SMART_VIDEO | Được tạo và tải lên qua Smart Video |
| OTHERS | Các nguồn khác |

#### Trạng thái ủy quyền bài đăng Spark Ads (`Spark Ads Post Authorization Status`)

| Value | Mô tả |
|---|---|
| EXPIRED | Ủy quyền đã hết hạn |
| APPLYING | Đang trong quá trình nộp đơn xin ủy quyền |
| AUTHORIZED | Ủy quyền đã được cấp thành công |
| NORESPONSE | Không có phản hồi từ chủ sở hữu bài đăng |
| REJECTED | Yêu cầu xin ủy quyền đã bị từ chối |
| CANCEL | Ủy quyền đã bị hủy |

---

### Dành cho báo cáo Upgraded Smart+ (`For Upgraded Smart+ Reports`)

#### Trạng thái chính của tài liệu sáng tạo (`material_primary_status`)

| Value | Mô tả |
|---|---|
| STATUS_DELETE | Đã xóa |
| STATUS_DISABLE | Đã tạm dừng |
| STATUS_FROZEN | Bị đóng băng |
| STATUS_TIME_DONE | Đã hoàn tất |
| STATUS_NOT_DELIVERY | Không phân phối |
| STATUS_PENDING | Đang chờ xử lý |
| STATUS_DELIVERY_OK | Đang hoạt động / phân phối tốt |
| STATUS_DELIVERY_PARTIAL | Phân phối bị hạn chế |
| STATUS_DELIVERY_CATALOG | Tài liệu sáng tạo nằm trong danh mục sản phẩm. Hiện tại trạng thái của tài liệu danh mục chưa khả dụng. |

#### Trạng thái phụ của tài liệu sáng tạo (`material_second_status_list`)

| Value | Mô tả |
|---|---|
| AD_STATUS_CAMPAIGN_DELETE | Chiến dịch đã bị xóa |
| AD_STATUS_ADGROUP_DELETE | Nhóm quảng cáo đã bị xóa |
| AD_STATUS_DELETE | Quảng cáo đã bị xóa |
| AD_STATUS_CAMPAIGN_DISABLE | Chiến dịch không hoạt động |
| AD_STATUS_ADGROUP_DISABLE | Nhóm quảng cáo không hoạt động |
| AD_STATUS_DISABLE | Quảng cáo không hoạt động |
| ADGROUP_STATUS_FROZEN | Nhóm quảng cáo bị đóng băng |
| CREATIVE_PAUSED_USED_IN_GMV_MAX | Tài liệu sáng tạo không khả dụng vì đang được quảng cáo GMV Max sử dụng |
| AD_STATUS_DONE | Đã hoàn tất |
| AD_STATUS_CAMPAIGN_EXCEED | Chiến dịch đã hết ngân sách |
| AD_STATUS_BUDGET_EXCEED | Nhóm quảng cáo đã hết ngân sách |
| AD_STATUS_ADVERTISER_AUDIT_DENY | Tài khoản không được phê duyệt |
| AD_STATUS_ADVERTISER_AUDIT | Tài khoản đang trong quá trình xét duyệt |
| ADVERTISER_CONTRACT_PENDING | Hợp đồng chưa có hiệu lực |
| ADVERTISER_ACCOUNT_PUNISH | Tài khoản bị xử phạt |
| AD_STATUS_AD_QUOTA_LIMIT | Nhóm quảng cáo bị tạm dừng do tài khoản hết hạn ngạch. Tạm dừng một nhóm quảng cáo đang chạy để tiếp tục. |
| PRODUCT_ANCHOR_UNAVAILABLE | Liên kết sản phẩm bạn muốn dùng trong quảng cáo không khả dụng |
| AD_STATUS_CREATOR_AUTHORIZATION_REVOKED | Nhà sáng tạo chưa cấp ủy quyền hoặc đã thu hồi |
| AD_STATUS_CREATIVE_ANCHOR_UNAVAILABLE | Liên kết sản phẩm không khả dụng |
| AD_STATUS_CREATIVE_PRODUCT_ALL_REJECTED | Tất cả sản phẩm bạn muốn dùng trong quảng cáo đều bị từ chối |
| AD_STATUS_ANCHOR_UNAVAILABLE | Liên kết sản phẩm không khả dụng |
| AD_STATUS_PRODUCT_UNAVAILABLE | Sản phẩm không khả dụng |
| NO_AVAILABLE_PRODUCTS | Không có sản phẩm khả dụng |
| AD_STATUS_SHOWCASE_AUTHORIZATION_LOST | Danh tính Showcase bạn dùng trong quảng cáo không khả dụng |
| AD_STATUS_ASSET_AUTHORIZATION_LOST | Tài sản quảng cáo không khả dụng hoặc ủy quyền đã bị thu hồi |
| AD_STAUS_PIXEL_UNBIND | Pixel chưa được cấp quyền hoặc bị hủy liên kết |
| AD_STATUS_AUDIT | Đang chờ xét duyệt |
| AD_STATUS_NOT_START | Ngoài lịch trình phân phối |
| AD_STATUS_AD_PRE_ONLINE | Quảng cáo ở trạng thái chuẩn bị chạy và chưa phân phối |
| ADVERTISER_REAUDIT | Các sửa đổi của tài khoản quảng cáo đang được xét duyệt |
| MATERIAL_DELETE | Tài liệu sáng tạo đã bị xóa |
| MATERIAL_DISABLE | Tài liệu sáng tạo bị tạm dừng |
| MATERIAL_AUDIT_DENY | Tài liệu sáng tạo bị từ chối xét duyệt |
| MATERIAL_AUDIT | Tài liệu sáng tạo đang chờ xét duyệt |
| MATERIAL_AUDIT_PARTIAL_APPROVED | Tài liệu sáng tạo được phê duyệt một phần |
| MATERIAL_DELIVERY_OK | Tài liệu sáng tạo đang phân phối hoạt động |
| ADVERTISER_ACCOUNT_BALANCE_EXCEED | Số dư tài khoản không đủ |

---

## Phạm vi quyền hạn (`Permission scope`)
<a id="doc-1753986142651394"></a>
<!-- doc_id: 1753986142651394 -->

> Đường dẫn: Appendix > Permission scope

Hệ thống phân quyền của TikTok API for Business bao gồm ba cấp độ: cấp 1 (first level), cấp 2 (second level), và cấp 3 (third level). Nếu một access token cấp cho bạn quyền hạn cấp 1, bạn có thể truy cập tất cả các endpoint thuộc phạm vi quyền cấp 2 và cấp 3 bên dưới quyền cấp 1 đó. Bạn có thể xem cấu trúc phân cấp quyền hạn trên cổng thông tin nhà phát triển bằng cách vào **My Apps** > Chọn App > **App Detail** > **Authorization** > **Scope of permission** trên [Cổng thông tin TikTok API for Business](https://ads.tiktok.com/marketing_api/homepage).

Sau khi nhận được trường `scope` (đại diện cho phạm vi quyền hạn của access token) từ phản hồi của [/oauth2/access_token/](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162) hoặc [/oauth/token/](../12-api-reference/10-authentication.md#doc-1739965703387137), bạn có thể tra cứu các bảng dưới đây để biết Scope ID tương ứng với quyền hạn nào và những endpoint nào liên kết với nó.

> [!NOTE]
> Ký hiệu `/` trong cột **Endpoint tương ứng** biểu thị rằng không có đường dẫn API endpoint nào gắn trực tiếp ở cấp quyền hiện tại. Ví dụ: một Scope ID thuộc quyền cấp 2 có thể có các endpoint tương ứng ở cấp 3 nhưng không có endpoint trực tiếp ở cấp 2.

### Quyền cấp 1 (`First-level permission`)

| Scope ID | Tên quyền cấp 1 (`First-level permission name`) | Endpoint tương ứng (`Corresponding endpoint`) |
|---|---|---|
| 1 | Quản lý tài khoản quảng cáo (`Ad Account Management`) | / |
| 2 | Quản lý quảng cáo (`Ads Management`) | / |
| 3 | Quản lý đối tượng (`Audience Management`) | / |
| 4 | Báo cáo (`Reporting`) | / |
| 5 | Đo lường (`Measurement`) | / |
| 6 | Quản lý nội dung sáng tạo (`Creative Management`) | / |
| 7 | Quản lý ứng dụng (`App Management`) | / |
| 8 | Quản lý Pixel (`Pixel Management`) | / |
| 9 | Quản lý danh mục DPA (`DPA Catalog Management`) | / |
| 10000 | Tiếp cận & Tần suất (`Reach & Frequency`) | / |
| 12000000 | Quản lý khách hàng tiềm năng (`Lead Management`) | / |
| 13000000 | TikTok Creator Marketplace (TCM) | / |
| 14000000 | Nhà sáng tạo TikTok (`TikTok Creator`) | / |
| 15000000 | Bình luận quảng cáo (`Ad Comments`) | / |
| 16000000 | Plugin doanh nghiệp TikTok (`TikTok business plugin`) | / |
| 17000000 | Quy tắc tự động (`Automated Rules`) | / |
| 18000000 | Tài khoản TikTok (`TikTok Accounts`) | / |
| 19000000 | Cửa hàng thương mại tại chỗ (`Onsite Commerce Store`) | `/commerce/store/create/` |
| 19000000 | Onsite Commerce Store | `/commerce/store/bind_to_catalog/` |
| 19000000 | Onsite Commerce Store | `/commerce/window/update/` |
| 19000000 | Onsite Commerce Store | `/commerce/store/get/` |
| 19000000 | Onsite Commerce Store | `/commerce/store/product/get/` |
| 19000000 | Onsite Commerce Store | `/commerce/store/trusted_create/` |
| 19000000 | Onsite Commerce Store | `/store/list/` |
| 7043626160646946818 | Quản lý sự kiện ngoại tuyến (`Offline Events Management`) | / |
| 7050363942434013185 | Chẩn đoán quảng cáo (`Ad Diagnosis`) | / |
| 7294180478502830081 | Quản lý sự kiện CRM (`CRM Event Management`) | / |

### Quyền cấp 2 (`Second-level permission`)

| Scope ID | Scope ID cấp 1 cha | Tên quyền cấp 2 (`Second-level permission name`) | Endpoint tương ứng (`Corresponding endpoint`) |
|---|---|---|---|
| 10 | 1 | Thông tin tài khoản quảng cáo (`Ad Account Information`) | / |
| 12 | 1 | Điều khoản và thỏa thuận (`Terms and Agreements`) | / |
| 13 | 1 | Quản lý danh sách chặn Pangle (`Pangle Block List Management`) | / |
| 14 | 1 | Gói đối tượng Pangle (`Pangle Audience Packages`) | / |
| 15 | 1 | Trung tâm doanh nghiệp (`Business Center`) | / |
| 20 | 2 | Chiến dịch (`Campaign`) | / |
| 21 | 2 | Nhóm quảng cáo (`Ad Group`) | / |
| 22 | 2 | Quảng cáo (`Ad`) | / |
| 23 | 2 | Nhật ký thay đổi (`Change Log`) | / |
| 24 | 2 | Kiểm thử phân tách (`Split Test`) | / |
| 7133464587805982722 | 2 | Quảng cáo tìm kiếm (`Search Ads`) | / |
| 30 | 3 | Đọc đối tượng tùy chỉnh (`Read Custom Audiences`) | `/dmp/custom_audience/list/` |
| 30 | 3 | Read Custom Audiences | `/dmp/custom_audience/get/` |
| 30 | 3 | Read Custom Audiences | `/dmp/saved_audience/list/` |
| 31 | 3 | Tạo và cập nhật đối tượng tùy chỉnh (`Create and Update Custom Audiences`) | `/dmp/custom_audience/file/upload/` |
| 31 | 3 | Create and Update Custom Audiences | `/dmp/custom_audience/create/` |
| 31 | 3 | Create and Update Custom Audiences | `/dmp/custom_audience/update/` |
| 31 | 3 | Create and Update Custom Audiences | `/dmp/custom_audience/delete/` |
| 31 | 3 | Create and Update Custom Audiences | `/dmp/custom_audience/rule/create/` |
| 31 | 3 | Create and Update Custom Audiences | `/dmp/custom_audience/lookalike/create/` |
| 31 | 3 | Create and Update Custom Audiences | `/segment/audience/` |
| 31 | 3 | Create and Update Custom Audiences | `/segment/mapping/` |
| 31 | 3 | Create and Update Custom Audiences | `/dmp/custom_audience/apply/` |
| 31 | 3 | Create and Update Custom Audiences | `/dmp/custom_audience/apply/log/` |
| 31 | 3 | Create and Update Custom Audiences | `/dmp/custom_audience/lookalike/update/` |
| 31 | 3 | Create and Update Custom Audiences | `/dmp/saved_audience/delete/` |
| 31 | 3 | Create and Update Custom Audiences | `/dmp/saved_audience/create/` |
| 32 | 3 | Chia sẻ đối tượng tùy chỉnh (`Share Custom Audiences`) | `/dmp/custom_audience/share/cancel/` |
| 32 | 3 | Share Custom Audiences | `/dmp/custom_audience/share/log/` |
| 32 | 3 | Share Custom Audiences | `/dmp/custom_audience/share/` |
| 40 | 4 | Cấp tài khoản quảng cáo (`Ad Account Level`) | / |
| 41 | 4 | Cấp chiến dịch (`Campaign Level`) | / |
| 42 | 4 | Cấp nhóm quảng cáo (`Ad Group Level`) | / |
| 43 | 4 | Cấp quảng cáo (`Ad Level`) | / |
| 44 | 4 | Báo cáo tổng hợp (`Consolidated Report`) | `/report/integrated/get/` |
| 44 | 4 | Consolidated Report | `/report/task/download/` |
| 44 | 4 | Consolidated Report | `/report/task/create/` |
| 44 | 4 | Consolidated Report | `/report/task/check/` |
| 44 | 4 | Consolidated Report | `/report/subscription/subscribe/` |
| 44 | 4 | Consolidated Report | `/report/subscription/unsubscribe/` |
| 44 | 4 | Consolidated Report | `/report/subscription/update/` |
| 44 | 4 | Consolidated Report | `/report/subscription/get/` |
| 44 | 4 | Consolidated Report | `/campaign/spc/report/get/` |
| 7043626160646815746 | 4 | Báo cáo thông tin chuyên sâu quảng cáo (`Ad Insight Report`) | `/report/ad_benchmark/get/` |
| 7043626160646815746 | 4 | Ad Insight Report | `/report/video_performance/get/` |
| 7231011733974859777 | 4 | Phân tích độ mệt mỏi của nội dung sáng tạo (`Creative Fatigue Insight`) | `/creative_fatigue/get/` |
| 50 | 5 | Báo cáo sự kiện ứng dụng (`Report App Event`) | `/app/track/` |
| 50 | 5 | Report App Event | `/app/batch/` |
| 51 | 5 | Báo cáo sự kiện Pixel (`Report Pixel Event`) | `/pixel/track/` |
| 51 | 5 | Report Pixel Event | `/pixel/batch/` |
| 7224195155857866754 | 5 | Báo cáo sự kiện chuyển đổi (`Report Conversion Event`) | `/event/track/` |
| 60 | 6 | Quản lý hình ảnh (`Image Management`) | / |
| 61 | 6 | Quản lý video (`Video Management`) | / |
| 62 | 6 | Mẫu video (`Video Template`) | `/video_template/task/create/` |
| 62 | 6 | Video Template | `/video_template/status/get/` |
| 63 | 6 | Quản lý âm nhạc (`Music management`) | / |
| 64 | 6 | Công cụ sáng tạo (`Creative tool`) | `/creative/status/get/` |
| 64 | 6 | Creative tool | `/creative/quick_optimization/create/` |
| 64 | 6 | Creative tool | `/creative/smart_video/create/` |
| 64 | 6 | Creative tool | `/creative/ads_preview/create/` |
| 64 | 6 | Creative tool | `/creative/video_soundtrack/create/` |
| 64 | 6 | Creative tool | `/creative/image/edit/` |
| 64 | 6 | Creative tool | `/creative/asset/share/` |
| 65 | 6 | Nhận báo cáo sáng tạo (`Get Creative Report`) | `/creative/report/get/` |
| 66 | 6 | Quảng cáo có thể chơi được (`Playable Ads`) | / |
| 67 | 6 | Xác thực tài liệu sáng tạo (`Creative Material Verification`) | / |
| 68 | 6 | Quản lý trang tức thì (`Instant Page Management`) | / |
| 69 | 6 | Quản lý bài đăng TikTok (`TikTok Posts Management`) | / |
| 6110000 | 6 | Đề xuất sáng tạo (`Creative Recommendation`) | / |
| 7050363942434078721 | 6 | Phân cảnh động (`Dynamic Scene`) | / |
| 7130572512626360322 | 6 | Sửa lỗi thông minh (`Smart Fix`) | / |
| 7176833266039685122 | 6 | Kiểm tra tên tệp (`File Name Check`) | / |
| 70 | 7 | Quản lý ứng dụng (`App Management`) | / |
| 80 | 8 | Quản lý Pixel (`Pixel Management`) | / |
| 90 | 9 | Quản lý danh mục (`Catalog Management`) | / |
| 91 | 9 | Quản lý sản phẩm (`Product Management`) | / |
| 92 | 9 | Quản lý bộ DPA (`DPA Set Management`) | / |
| 94 | 9 | Quản lý video danh mục (`Catalog Video Management`) | / |
| 95 | 9 | Mẫu (`Template`) | / |
| 96 | 9 | Liên kết nguồn sự kiện (`Event Source Bind`) | / |
| 97 | 9 | Nguồn cấp dữ liệu (`Feed`) | / |
| 7224195155857915906 | 9 | Chẩn đoán (`Diagnostic`) | / |
| 100000 | 10000 | Tạo và cập nhật nhóm quảng cáo (`Create and Update Ad Groups`) | `/adgroup/rf/create/` |
| 100000 | 10000 | Create and Update Ad Groups | `/adgroup/rf/update/` |
| 100000 | 10000 | Create and Update Ad Groups | `/adgroup/rf/estimated/info/` |
| 100001 | 10000 | Dung lượng và đơn đặt hàng (`Inventory and Orders`) | `/rf/inventory/estimate/` |
| 100001 | 10000 | Inventory and Orders | `/rf/order/cancel/` |
| 100002 | 10000 | Công cụ (`Tools`) | `/rf/contract/query/` |
| 100002 | 10000 | Tools | `/rf/delivery/timezone/` |
| 12010000 | 12000000 | Truy xuất khách hàng tiềm năng (`Leads Retrieval`) | / |
| 12020000 | 12000000 | Kiểm thử khách hàng tiềm năng (`Test Leads`) | / |
| 13010000 | 13000000 | Tạo và cập nhật tài khoản TCM (`Create and Update TCM Account`) | `/tcm/order/create/v2/` |
| 13020000 | 13000000 | Đọc tài khoản TCM (`Read TCM Account`) | `/tcm/creator/discover/` |
| 13020000 | 13000000 | Read TCM Account | `/tcm/similar/creator/` |
| 13020000 | 13000000 | Read TCM Account | `/tcm/report/get/` |
| 13030000 | 13000000 | Trạng thái gia nhập và mời nhà sáng tạo vào TCM | `/tcm/creator/invite/` |
| 13030000 | 13000000 | Trạng thái gia nhập và mời nhà sáng tạo vào TCM | `/tcm/creator/status/get/` |
| 13040000 | 13000000 | Gửi lời mời Spark Ads và lấy trạng thái | `/tcm/spark_ad/apply/` |
| 13040000 | 13000000 | Gửi lời mời Spark Ads và lấy trạng thái | `/tcm/spark_ad/status/get/` |
| 13040000 | 13000000 | Gửi lời mời Spark Ads và lấy trạng thái | `/tcm/tt_video/status/` |
| 13040000 | 13000000 | Gửi lời mời Spark Ads và lấy trạng thái | `/tcm/tt_video/apply/` |
| 14010000 | 14000000 | Người dùng sáng tạo (`Creator User`) | / |
| 14020000 | 14000000 | Phương tiện truyền thông sáng tạo (`Creator Media`) | / |
| 14030000 | 14000000 | Đơn hàng sáng tạo (`Creator Order`) | / |
| 15010000 | 15000000 | Quản lý bình luận quảng cáo (`Ad Comment Management`) | / |
| 15020000 | 15000000 | Quản lý từ bị chặn (`Blocked Word Management`) | / |
| 17010000 | 17000000 | Tạo và cập nhật quy tắc tự động (`Create and Update Automated Rules`) | `/optimizer/rule/create/` |
| 17010000 | 17000000 | Create and Update Automated Rules | `/optimizer/rule/update/` |
| 17010000 | 17000000 | Create and Update Automated Rules | `/optimizer/rule/batch_bind/` |
| 17010000 | 17000000 | Create and Update Automated Rules | `/optimizer/rule/update/status/` |
| 17020000 | 17000000 | Đọc quy tắc tự động và kết quả thực thi | `/optimizer/rule/get/` |
| 17020000 | 17000000 | Read Automated Rules and their Execution Results | `/optimizer/rule/list/` |
| 17020000 | 17000000 | Read Automated Rules and their Execution Results | `/optimizer/rule/result/get/` |
| 17020000 | 17000000 | Read Automated Rules and their Execution Results | `/optimizer/rule/result/list/` |
| 18010000 | 18000000 | Người dùng doanh nghiệp (`Business User`) | / |
| 18020000 | 18000000 | Phương tiện doanh nghiệp (`Business Media`) | `/business/video/list/` |
| 18030000 | 18000000 | Bình luận doanh nghiệp (`Business Comment`) | / |
| 7044139020472942593 | 18000000 | Nội dung doanh nghiệp (`Business Content`) | / |
| 7050363942434095105 | 7043626160646946818 | Tạo/Quản lý sự kiện ngoại tuyến (`Create/Manage Offline Events`) | `/offline/create/` |
| 7050363942434095105 | 7043626160646946818 | Create/Manage Offline Events | `/offline/update/` |
| 7050363942434095105 | 7043626160646946818 | Create/Manage Offline Events | `/offline/delete/` |
| 7050363942434127873 | 7043626160646946818 | Báo cáo từng sự kiện ngoại tuyến | `/offline/track/` |
| 7068127621543919617 | 7043626160646946818 | Báo cáo sự kiện ngoại tuyến hàng loạt | `/offline/batch/` |
| 7224195155857833986 | 7043626160646946818 | Đọc sự kiện ngoại tuyến (`Read Offline Events`) | `/offline/get/` |
| 7050363942434029569 | 7050363942434013185 | Nhận và áp dụng đề xuất chẩn đoán | `/tool/diagnosis/get/` |
| 7294180478502846465 | 7294180478502830081 | Đọc bộ sự kiện CRM (`Read CRM Event Sets`) | `/crm/list/` |

### Quyền cấp 3 (`Third-level permission`)

| Scope ID | Scope ID cấp 2 cha | Tên quyền cấp 3 (`Third-level permission name`) | Endpoint tương ứng (`Corresponding endpoint`) |
|---|---|---|---|
| 100 | 10 | Đọc thông tin tài khoản quảng cáo (`Read Ad Account Information`) | `/advertiser/info/` |
| 100 | 10 | Read Ad Account Information | `/oauth2/advertiser/get/` |
| 120 | 12 | Điều khoản và thỏa thuận (`Terms and Agreements`) | `/term/get/` |
| 120 | 12 | Terms and Agreements | `/term/check/` |
| 120 | 12 | Terms and Agreements | `/term/confirm/` |
| 130 | 13 | Quản lý danh sách chặn Pangle | `/pangle_block_list/get/` |
| 130 | 13 | Quản lý danh sách chặn Pangle | `/pangle_block_list/update/` |
| 140 | 14 | Gói đối tượng Pangle (`Pangle Audience Packages`) | `/pangle_audience_package/get/` |
| 150 | 15 | Đọc thông tin Business Center | `/bc/get/` |
| 150 | 15 | Đọc thông tin Business Center | `/bc/balance/get/` |
| 150 | 15 | Đọc thông tin Business Center | `/bc/transaction/get/` |
| 151 | 15 | Tạo tài khoản quảng cáo (`Create Ad Account`) | `/bc/image/upload/` |
| 151 | 15 | Create Ad Account | `/bc/advertiser/create/` |
| 151 | 15 | Create Ad Account | `/advertiser/update/` |
| 151 | 15 | Create Ad Account | `/bc/advertiser/disable/` |
| 151 | 15 | Create Ad Account | `/bc/advertiser/qualification/get/` |
| 152 | 15 | Số dư và giao dịch tài khoản quảng cáo | `/bc/transfer/` |
| 152 | 15 | Số dư và giao dịch tài khoản quảng cáo | `/advertiser/balance/get/` |
| 152 | 15 | Số dư và giao dịch tài khoản quảng cáo | `/advertiser/transaction/get/` |
| 153 | 15 | Tài sản Business Center (`Business Center Asset`) | `/bc/asset/get/` |
| 153 | 15 | Business Center Asset | `/bc/asset/admin/get/` |
| 153 | 15 | Business Center Asset | `/bc/asset/assign/` |
| 153 | 15 | Business Center Asset | `/bc/asset/unassign/` |
| 153 | 15 | Business Center Asset | `/bc/asset/partner/get/` |
| 153 | 15 | Business Center Asset | `/bc/asset/member/get/` |
| 153 | 15 | Business Center Asset | `/bc/asset/admin/delete/` |
| 153 | 15 | Business Center Asset | `/bc/pixel/link/update/` |
| 153 | 15 | Business Center Asset | `/bc/pixel/link/get/` |
| 153 | 15 | Business Center Asset | `/bc/pixel/transfer/` |
| 153 | 15 | Business Center Asset | `/asset/bind/quota/` |
| 155 | 15 | Quản lý đối tác Business Center | `/bc/partner/asset/get/` |
| 155 | 15 | Quản lý đối tác Business Center | `/bc/partner/delete/` |
| 155 | 15 | Quản lý đối tác Business Center | `/bc/partner/add/` |
| 155 | 15 | Quản lý đối tác Business Center | `/bc/partner/get/` |
| 155 | 15 | Quản lý đối tác Business Center | `/bc/partner/asset/delete/` |
| 156 | 15 | Quản lý thành viên Business Center | `/bc/member/delete/` |
| 156 | 15 | Quản lý thành viên Business Center | `/bc/member/update/` |
| 156 | 15 | Quản lý thành viên Business Center | `/bc/member/get/` |
| 156 | 15 | Quản lý thành viên Business Center | `/bc/member/invite/` |
| 157 | 15 | Quản lý nhóm thanh toán Business Center | `/bc/billing_group/update/` |
| 157 | 15 | Quản lý nhóm thanh toán Business Center | `/bc/billing_group/get/` |
| 157 | 15 | Quản lý nhóm thanh toán Business Center | `/bc/billing_group/create/` |
| 157 | 15 | Quản lý nhóm thanh toán Business Center | `/bc/billing_group/advertiser/list/` |
| 7078191955347259394 | 15 | Quản lý hóa đơn (`Invoice Management`) | `/bc/invoice/task/create/` |
| 7078191955347259394 | 15 | Invoice Management | `/bc/invoice/get/` |
| 7078191955347259394 | 15 | Invoice Management | `/bc/invoice/download/` |
| 7078191955347259394 | 15 | Invoice Management | `/bc/invoice/task/get/` |
| 7078191955347259394 | 15 | Invoice Management | `/bc/invoice/unpaid/get/` |
| 7078191955347259394 | 15 | Invoice Management | `/bc/invoice/task/list/` |
| 7153155400966176769 | 15 | Nhóm tài sản (`Asset Group`) | `/bc/asset_group/create/` |
| 7153155400966176769 | 15 | Asset Group | `/bc/asset_group/get/` |
| 7153155400966176769 | 15 | Asset Group | `/bc/asset_group/update/` |
| 7153155400966176769 | 15 | Asset Group | `/bc/asset_group/list/` |
| 7153155400966176769 | 15 | Asset Group | `/bc/asset_group/delete/` |
| 200 | 20 | Đọc chiến dịch (`Read Campaigns`) | `/campaign/get/` |
| 200 | 20 | Read Campaigns | `/campaign/quota/get/` |
| 200 | 20 | Read Campaigns | `/campaign/quota/info/` |
| 200 | 20 | Read Campaigns | `/campaign/spc/get/` |
| 200 | 20 | Read Campaigns | `/campaign/copy/task/check/` |
| 201 | 20 | Tạo và cập nhật chiến dịch (`Create and Update Campaigns`) | `/campaign/create/` |
| 201 | 20 | Create and Update Campaigns | `/campaign/update/` |
| 201 | 20 | Create and Update Campaigns | `/campaign/status/update/` |
| 201 | 20 | Create and Update Campaigns | `/campaign/spc/create/` |
| 201 | 20 | Create and Update Campaigns | `/campaign/spc/update/` |
| 201 | 20 | Create and Update Campaigns | `/campaign/copy/task/create/` |
| 210 | 21 | Đọc nhóm quảng cáo (`Read Ad Groups`) | `/adgroup/get/` |
| 210 | 21 | Read Ad Groups | `/adgroup/review_info/` |
| 210 | 21 | Read Ad Groups | `/adgroup/quota/` |
| 211 | 21 | Tạo và cập nhật nhóm quảng cáo | `/adgroup/create/` |
| 211 | 21 | Tạo và cập nhật nhóm quảng cáo | `/adgroup/update/` |
| 211 | 21 | Tạo và cập nhật nhóm quảng cáo | `/ad/audience_size/estimate/` |
| 211 | 21 | Tạo và cập nhật nhóm quảng cáo | `/adgroup/status/update/` |
| 211 | 21 | Tạo và cập nhật nhóm quảng cáo | `/adgroup/budget/update/` |
| 220 | 22 | Đọc quảng cáo (`Read Ads`) | `/ad/get/` |
| 220 | 22 | Read Ads | `/ad/review_info/` |
| 220 | 22 | Read Ads | `/ad/aco/get/` |
| 220 | 22 | Read Ads | `/showcase/product/get/` |
| 220 | 22 | Read Ads | `/showcase/identity/get/` |
| 220 | 22 | Read Ads | `/showcase/region/get/` |
| 221 | 22 | Tạo và cập nhật quảng cáo (`Create and Update Ads`) | `/ad/create/` |
| 221 | 22 | Create and Update Ads | `/ad/update/` |
| 221 | 22 | Create and Update Ads | `/ad/aco/create/` |
| 221 | 22 | Create and Update Ads | `/ad/aco/update/` |
| 221 | 22 | Create and Update Ads | `/ad/status/update/` |
| 221 | 22 | Create and Update Ads | `/ad/aco/material_status/update/` |
| 230 | 23 | Nhật ký thay đổi (`Change Log`) | `/changelog/task/create/` |
| 230 | 23 | Change Log | `/changelog/task/download/` |
| 230 | 23 | Change Log | `/changelog/task/check/` |
| 240 | 24 | Kiểm thử phân tách (`Split Test`) | `/split_test/promote/` |
| 240 | 24 | Split Test | `/split_test/result/get/` |
| 240 | 24 | Split Test | `/split_test/create/` |
| 240 | 24 | Split Test | `/split_test/end/` |
| 240 | 24 | Split Test | `/split_test/update/` |
| 7133464587805999106 | 7133464587805982722 | Từ khóa phủ định (`Negative Keywords`) | `/search_ad/negative_keyword/download/` |
| 7133464587805999106 | 7133464587805982722 | Negative Keywords | `/search_ad/negative_keyword/add/` |
| 7133464587805999106 | 7133464587805982722 | Negative Keywords | `/search_ad/negative_keyword/delete/` |
| 7133464587805999106 | 7133464587805982722 | Negative Keywords | `/search_ad/negative_keyword/update/` |
| 7133464587805999106 | 7133464587805982722 | Negative Keywords | `/search_ad/negative_keyword/get/` |
| 600 | 60 | Đọc thư viện hình ảnh (`Read Image Library`) | `/file/image/ad/search/` |
| 600 | 60 | Read Image Library | `/file/image/ad/info/` |
| 601 | 60 | Tạo và cập nhật hình ảnh (`Create and Update Images`) | `/file/image/ad/upload/` |
| 601 | 60 | Create and Update Images | `/file/image/ad/update/` |
| 610 | 61 | Đọc thư viện video (`Read Video Library`) | `/file/video/ad/search/` |
| 610 | 61 | Read Video Library | `/file/video/ad/info/` |
| 611 | 61 | Tạo và cập nhật video (`Create and Update Videos`) | `/file/video/ad/upload/` |
| 611 | 61 | Create and Update Videos | `/file/video/ad/update/` |
| 612 | 61 | Tạo ảnh thu nhỏ cho video (`Generate Thumbnails for Videos`) | `/file/video/suggestcover/` |
| 630 | 63 | Đọc thư viện âm nhạc (`Read music library`) | `/file/music/get/` |
| 631 | 63 | Tải lên tệp âm nhạc (`Upload music file`) | `/file/music/upload/` |
| 660 | 66 | Đọc quảng cáo có thể chơi (`Read Playable Ads`) | `/playable/get/` |
| 660 | 66 | Read Playable Ads | `/playable/validate/` |
| 661 | 66 | Tạo/Quản lý quảng cáo có thể chơi | `/playable/upload/` |
| 661 | 66 | Tạo/Quản lý quảng cáo có thể chơi | `/playable/save/` |
| 661 | 66 | Tạo/Quản lý quảng cáo có thể chơi | `/playable/delete/` |
| 680 | 68 | Quản lý trang tức thì (`Instant Page Management`) | `/page/get/` |
| 690 | 69 | Truy vấn bài đăng TikTok (`Query TikTok Posts`) | `/tt_video/info/` |
| 691 | 69 | Ủy quyền bài đăng TikTok (`Authorize TikTok Posts`) | `/tt_video/authorize/` |
| 691 | 69 | Authorize TikTok Posts | `/tt_video/unbind/` |
| 691 | 69 | Authorize TikTok Posts | `/tt_video/list/` |
| 692 | 69 | Tạo danh tính (`Create Identity`) | `/identity/create/` |
| 693 | 69 | Truy vấn danh tính (`Query Identity`) | `/identity/get/` |
| 693 | 69 | Query Identity | `/identity/info/` |
| 693 | 69 | Query Identity | `/identity/video/get/` |
| 693 | 69 | Query Identity | `/identity/video/info/` |
| 693 | 69 | Query Identity | `/identity/music/authorization/` |
| 693 | 69 | Query Identity | `/identity/live/get/` |
| 7176842096345694209 | 69 | Xóa danh tính (`Delete Identity`) | `/identity/delete/` |
| 6110100 | 6110000 | Đề xuất CTA (`CTA Recommendation`) | `/creative/portfolio/create/` |
| 6110100 | 6110000 | CTA Recommendation | `/creative/portfolio/get/` |
| 6110100 | 6110000 | CTA Recommendation | `/creative/cta/recommend/` |
| 6110100 | 6110000 | CTA Recommendation | `/creative/portfolio/list/` |
| 6110200 | 6110000 | Văn bản thông minh (`Smart Text`) | `/creative/smart_text/generate/` |
| 6110200 | 6110000 | Smart Text | `/creative/smart_text/feedback/` |
| 7043626160646864898 | 7050363942434078721 | Chức năng cốt lõi (`Core Functions`) | `/dynamic_scene/material/submit/` |
| 7043626160646864898 | 7050363942434078721 | Core Functions | `/dynamic_scene/task/create/` |
| 7043626160646864898 | 7050363942434078721 | Core Functions | `/dynamic_scene/get/` |
| 7043626160646864898 | 7050363942434078721 | Core Functions | `/dynamic_scene/task/get/` |
| 7043626160646864898 | 7050363942434078721 | Core Functions | `/dynamic_scene/report/get/` |
| 7132385893100437506 | 7130572512626360322 | Quản lý tác vụ sửa lỗi (`Fix Task management`) | `/video/fix/task/create/` |
| 7132385893100437506 | 7130572512626360322 | Fix Task management | `/video/fix/task/get/` |
| 700 | 70 | Đọc thông tin ứng dụng (`Read Apps`) | `/app/list/` |
| 700 | 70 | Read Apps | `/app/info/` |
| 700 | 70 | Read Apps | `/app/optimization_event/` |
| 700 | 70 | Read Apps | `/app/optimization_event/retargeting/` |
| 701 | 70 | Tạo và cập nhật ứng dụng (`Create and Update Apps`) | `/app/create/` |
| 701 | 80 | Create and Update Apps | `/app/update/` |
| 800 | 80 | Đọc Pixel (`Read Pixels`) | `/pixel/list/` |
| 801 | 80 | Tạo và cập nhật Pixel (`Create and Update Pixels`) | `/pixel/create/` |
| 801 | 80 | Create and Update Pixels | `/pixel/update/` |
| 801 | 80 | Create and Update Pixels | `/pixel/event/create/` |
| 801 | 80 | Create and Update Pixels | `/pixel/event/update/` |
| 801 | 80 | Create and Update Pixels | `/pixel/event/delete/` |
| 801 | 80 | Create and Update Pixels | `/pixel/instant_page/event/` |
| 802 | 80 | Báo cáo cấp Pixel (`Pixel Level Reporting`) | `/pixel/event/stats/` |
| 900 | 90 | Đọc danh mục (`Read Catalogs`) | `/catalog/get/` |
| 900 | 90 | Read Catalogs | `/catalog/lexicon/get/` |
| 900 | 90 | Read Catalogs | `/catalog/overview/` |
| 900 | 90 | Read Catalogs | `/catalog/location_currency/get/` |
| 900 | 90 | Read Catalogs | `/catalog/available_country/get/` |
| 901 | 90 | Tạo và cập nhật danh mục (`Create and Update Catalog`) | `/catalog/create/` |
| 901 | 90 | Create and Update Catalog | `/catalog/update/` |
| 901 | 90 | Create and Update Catalog | `/catalog/delete/` |
| 901 | 90 | Create and Update Catalog | `/catalog/capitalize/` |
| 910 | 91 | Đọc sản phẩm (`Read Products`) | `/catalog/product/get/` |
| 910 | 91 | Read Products | `/catalog/product/log/` |
| 911 | 91 | Tạo và cập nhật sản phẩm (`Create and Update Product`) | `/catalog/product/upload/` |
| 911 | 91 | Create and Update Product | `/catalog/product/delete/` |
| 911 | 91 | Create and Update Product | `/catalog/product/file/` |
| 911 | 91 | Create and Update Product | `/catalog/product/update/` |
| 920 | 92 | Lấy bộ sản phẩm danh mục (`Get Catalog Set`) | `/catalog/set/get/` |
| 920 | 92 | Get Catalog Set | `/catalog/set/product/get/` |
| 921 | 92 | Tạo/Cập nhật bộ danh mục (`Post Catalog Set`) | `/catalog/set/create/` |
| 921 | 92 | Post Catalog Set | `/catalog/set/update/` |
| 921 | 92 | Post Catalog Set | `/catalog/set/delete/` |
| 940 | 94 | Lấy gói video danh mục (`Get Catalog Video`) | `/catalog/video_package/get/` |
| 941 | 94 | Đăng gói video danh mục (`Post Catalog Video`) | `/catalog/video_package/update/` |
| 941 | 94 | Post Catalog Video | `/catalog/video_package/create/` |
| 941 | 94 | Post Catalog Video | `/catalog/video_package/delete/` |
| 950 | 95 | Mẫu danh mục (`Template`) | `/catalog/template/upload/` |
| 950 | 95 | Template | `/catalog/template_preview/create/` |
| 960 | 96 | Đọc liên kết nguồn sự kiện (`Read Event Source Bind`) | `/catalog/eventsource_bind/get/` |
| 960 | 96 | Read Event Source Bind | `/diagnostic/catalog/eventsource/metric/` |
| 960 | 96 | Read Event Source Bind | `/diagnostic/catalog/eventsource/issue/` |
| 961 | 96 | Tạo và hủy liên kết nguồn sự kiện | `/catalog/eventsource/bind/` |
| 961 | 96 | Tạo và hủy liên kết nguồn sự kiện | `/catalog/eventsource/unbind/` |
| 970 | 97 | Lấy nguồn cấp dữ liệu (`Get Feed`) | `/catalog/feed/get/` |
| 970 | 97 | Get Feed | `/catalog/feed/log/` |
| 971 | 97 | Đăng nguồn cấp dữ liệu (`Post Feed`) | `/catalog/feed/create/` |
| 971 | 97 | Post Feed | `/catalog/feed/update/` |
| 971 | 97 | Post Feed | `/catalog/feed/delete/` |
| 971 | 97 | Post Feed | `/catalog/feed/switch/` |
| 12010100 | 97 | Truy xuất khách hàng tiềm năng (`Leads Retrieval`) | `/page/field/get/` |
| 12010100 | 12010000 | Leads Retrieval | `/page/lead/get/` |
| 12020100 | 12020000 | Kiểm thử khách hàng tiềm năng (`Test Leads`) | `/page/lead/mock/create/` |
| 12020100 | 12020000 | Test Leads | `/page/lead/mock/get/` |
| 12020100 | 12020000 | Test Leads | `/page/lead/mock/delete/` |
| 12020100 | 12020000 | Test Leads | `/page/field/get/` |
| 12020100 | 12020000 | Test Leads | `/page/lead/task/download/` |
| 12020100 | 12020000 | Test Leads | `/page/lead/task/` |
| 14010100 | 14010000 | Lấy thông tin cơ bản của nhà sáng tạo | / |
| 14010200 | 14010000 | Lấy thông tin chuyên sâu nhà sáng tạo (`Get Creator Insights`) | `/tcm/creator/public/` |
| 14010200 | 14010000 | Get Creator Insights | `/tcm/creator/authorized/` |
| 14020100 | 14020000 | Lấy phương tiện của nhà sáng tạo (`Get Creator Media`) | `/tcm/creator/public/video/list/` |
| 14020100 | 14020000 | Get Creator Media | `/tcm/creator/authorized/video/list/` |
| 15010100 | 15010000 | Đọc bình luận (`Read Comments`) | `/comment/list/` |
| 15010100 | 15010000 | Read Comments | `/comment/reference/` |
| 15010100 | 15010000 | Read Comments | `/comment/task/create/` |
| 15010100 | 15010000 | Read Comments | `/comment/task/check/` |
| 15010100 | 15010000 | Read Comments | `/comment/task/download/` |
| 15010200 | 15010000 | Ghi bình luận (`Write Comments`) | `/comment/status/update/` |
| 15010200 | 15010000 | Write Comments | `/comment/delete/` |
| 15010200 | 15010000 | Write Comments | `/comment/post/` |
| 15020100 | 15020000 | Đọc từ bị chặn (`Read Blocked Words`) | `/blockedword/list/` |
| 15020100 | 15020000 | Read Blocked Words | `/blockedword/task/create/` |
| 15020100 | 15020000 | Read Blocked Words | `/blockedword/task/check/` |
| 15020100 | 15020000 | Read Blocked Words | `/blockedword/task/download/` |
| 15020100 | 15020000 | Read Blocked Words | `/blockedword/check/` |
| 15020200 | 15020000 | Thêm/Ghi từ bị chặn (`Write Blocked Words`) | `/blockedword/create/` |
| 15020200 | 15020000 | Write Blocked Words | `/blockedword/update/` |
| 15020200 | 15020000 | Write Blocked Words | `/blockedword/delete/` |
| 18010100 | 18010000 | Lấy thông tin cơ bản người dùng doanh nghiệp | `/business/get/` |
| 18030100 | 18030000 | Lấy bình luận doanh nghiệp (`Get Business Comment`) | `/business/comment/reply/list/` |
| 18030100 | 18030000 | Get Business Comment | `/business/comment/list/` |
| 18030200 | 18030000 | Quản lý bình luận doanh nghiệp (`Manage Business Comment`) | `/business/comment/create/` |
| 18030200 | 18030000 | Manage Business Comment | `/business/comment/delete/` |
| 18030200 | 18030000 | Manage Business Comment | `/business/comment/hide/` |
| 18030200 | 18030000 | Manage Business Comment | `/business/comment/reply/create/` |
| 18030200 | 18030000 | Manage Business Comment | `/business/comment/like/` |
| 7050363942433996801 | 7044139020472942593 | Xuất bản video (`Video Publish`) | `/business/video/publish/` |
| 7050363942433996801 | 7044139020472942593 | Video Publish | `/business/hashtag/suggestion/` |

---

## Mã vị trí (`Location code`)
<a id="doc-1737585867307010"></a>
<!-- doc_id: 1737585867307010 -->

> Đường dẫn: Appendix > Location code

Bảng dưới đây liệt kê danh sách tên quốc gia, vùng lãnh thổ và mã vị trí địa lý tương ứng (mã ISO 2 ký tự) được hỗ trợ trên nền tảng TikTok API for Business:

| Name | Code |
|---|---|
| Andorra | AD |
| United Arab Emirates | AE |
| Afghanistan | AF |
| Antigua and Barbuda | AG |
| Anguilla | AI |
| Albania | AL |
| Armenia | AM |
| Angola | AO |
| Antarctica | AQ |
| Argentina | AR |
| American Samoa | AS |
| Austria | AT |
| Australia | AU |
| Aruba | AW |
| Aland | AX |
| Azerbaijan | AZ |
| Bosnia & Herzegovina | BA |
| Barbados | BB |
| Bangladesh | BD |
| Belgium | BE |
| Burkina Faso | BF |
| Bulgaria | BG |
| Bahrain | BH |
| Burundi | BI |
| Benin | BJ |
| Saint Barthélemy | BL |
| Bermuda | BM |
| Brunei | BN |
| Bolivia | BO |
| Caribbean Netherlands | BQ |
| Brazil | BR |
| Commonwealth of the Bahamas | BS |
| Bhutan | BT |
| Bouvet Island | BV |
| Botswana | BW |
| Belarus | BY |
| Belize | BZ |
| Canada | CA |
| Cocos (Keeling) Islands | CC |
| Democratic Republic of the Congo | CD |
| Central African Republic | CF |
| Republic of the Congo | CG |
| Switzerland | CH |
| Cote D'Ivoire | CI |
| Cook Islands | CK |
| Chile | CL |
| Cameroon | CM |
| the Chinese mainland | CN |
| Colombia | CO |
| Costa Rica | CR |
| Cuba | CU |
| Cape Verde | CV |
| Christmas Island | CX |
| Cyprus | CY |
| Czech Republic | CZ |
| Germany | DE |
| Djibouti | DJ |
| Denmark | DK |
| Dominica | DM |
| Dominican Republic | DO |
| Algeria | DZ |
| Ecuador | EC |
| Estonia | EE |
| Egypt | EG |
| Western Sahara | EH |
| Eritrea | ER |
| Spain | ES |
| Ethiopia | ET |
| Finland | FI |
| Fiji | FJ |
| Falkland Islands | FK |
| Micronesia | FM |
| Faroe Islands | FO |
| France | FR |
| Gabon | GA |
| United Kingdom | GB |
| Grenada | GD |
| Georgia | GE |
| French Guiana | GF |
| Guernsey | GG |
| Ghana | GH |
| Gibraltar | GI |
| Greenland | GL |
| Gambia | GM |
| Guinea | GN |
| Guadeloupe | GP |
| Equatorial Guinea | GQ |
| Greece | GR |
| South Georgia and the South Sandwich Islands | GS |
| Guatemala | GT |
| Guam | GU |
| Guinea-Bissau | GW |
| Guyana | GY |
| Hong Kong, China | HK |
| Heard Island and McDonald Islands | HM |
| Honduras | HN |
| Croatia | HR |
| Haiti | HT |
| Hungary | HU |
| Indonesia | ID |
| Ireland | IE |
| Israel | IL |
| Isle of Man | IM |
| India | IN |
| British Indian Ocean Territory | IO |
| Iraq | IQ |
| Iran | IR |
| Iceland | IS |
| Italy | IT |
| Jersey | JE |
| Jamaica | JM |
| Jordan | JO |
| Japan | JP |
| Kenya | KE |
| Kyrgyzstan | KG |
| Cambodia | KH |
| Kiribati | KI |
| Comoros | KM |
| Saint Kitts and Nevis | KN |
| North Korea | KP |
| South Korea | KR |
| Kuwait | KW |
| Cayman Islands | KY |
| Kazakhstan | KZ |
| Laos | LA |
| Lebanon | LB |
| Saint Lucia | LC |
| Liechtenstein | LI |
| Sri Lanka | LK |
| Liberia | LR |
| Lesotho | LS |
| Lithuania | LT |
| Luxembourg | LU |
| Latvia | LV |
| Libya | LY |
| Morocco | MA |
| Monaco | MC |
| Moldova | MD |
| Montenegro | ME |
| Saint Martin | MF |
| Madagascar | MG |
| Marshall Islands | MH |
| North Macedonia | MK |
| Mali | ML |
| Myanmar | MM |
| Mongolia | MN |
| Macao, China | MO |
| Northern Mariana Islands | MP |
| Martinique | MQ |
| Mauritania | MR |
| Montserrat | MS |
| Malta | MT |
| Mauritius | MU |
| Maldives | MV |
| Malawi | MW |
| Mexico | MX |
| Malaysia | MY |
| Mozambique | MZ |
| Namibia | NA |
| New Caledonia | NC |
| Niger | NE |
| Norfolk Island | NF |
| Nigeria | NG |
| Nicaragua | NI |
| Netherlands | NL |
| Norway | NO |
| Nepal | NP |
| Nauru | NR |
| Niue | NU |
| New Zealand | NZ |
| Oman | OM |
| Panama | PA |
| Peru | PE |
| French Polynesia | PF |
| Papua New Guinea | PG |
| Philippines | PH |
| Pakistan | PK |
| Poland | PL |
| Saint Pierre and Miquelon | PM |
| Pitcairn Islands | PN |
| Puerto Rico | PR |
| State of Palestine | PS |
| Portugal | PT |
| Palau | PW |
| Paraguay | PY |
| Qatar | QA |
| Reunion | RE |
| Romania | RO |
| Serbia | RS |
| Russia | RU |
| Rwanda | RW |
| Saudi Arabia | SA |
| Solomon Islands | SB |
| Seychelles | SC |
| Sudan | SD |
| Sweden | SE |
| Singapore | SG |
| Saint Helena | SH |
| Slovenia | SI |
| Svalbard and Jan Mayen | SJ |
| Slovakia | SK |
| Sierra Leone | SL |
| San Marino | SM |
| Senegal | SN |
| Somalia | SO |
| Suriname | SR |
| South Sudan | SS |
| Sao Tome and Principe | ST |
| El Salvador | SV |
| Sint Maarten | SX |
| Syria | SY |
| Swaziland | SZ |
| Turks and Caicos Islands | TC |
| Chad | TD |
| French Southern Territories | TF |
| Togo | TG |
| Thailand | TH |
| Tajikistan | TJ |
| Tokelau | TK |
| Timor-Leste | TL |
| Turkmenistan | TM |
| Tunisia | TN |
| Tonga | TO |
| Turkey | TR |
| Trinidad and Tobago | TT |
| Tuvalu | TV |
| Taiwan, China | TW |
| Tanzania | TZ |
| Ukraine | UA |
| Uganda | UG |
| United States Minor Outlying Islands | UM |
| United States | US |
| Uruguay | UY |
| Uzbekistan | UZ |
| Vatican City | VA |
| Saint Vincent and the Grenadines | VC |
| Venezuela | VE |
| British Virgin Islands | VG |
| United States Virgin Islands | VI |
| Vietnam | VN |
| Vanuatu | VU |
| Wallis and Futuna | WF |
| Samoa | WS |
| Yemen | YE |
| Mayotte | YT |
| South Africa | ZA |
| Zambia | ZM |
| Zimbabwe | ZW |

---

## Múi giờ (`Time zone`)
<a id="doc-1737586324313089"></a>
<!-- doc_id: 1737586324313089 -->

> Đường dẫn: Appendix > Time zone

Bảng dưới đây liệt kê các mã múi giờ khả dụng và múi giờ tương ứng theo chuẩn UTC. Để truy xuất danh sách mã múi giờ đầy đủ và mới nhất qua API, hãy sử dụng endpoint [/tool/timezone/](../12-api-reference/70-tools-p2.md#doc-1738455961470977).

Bạn có thể sử dụng các mã múi giờ này trong các thao tác API sau:
- **Quy tắc tự động (Automated Rules)**:  
  Khi tạo, cập nhật hoặc truy xuất Quy tắc tự động qua [/optimizer/rule/create/](../12-api-reference/11-automated-rules.md#doc-1738767670852610), [/optimizer/rule/update/](../12-api-reference/11-automated-rules.md#doc-1738769123170306), hoặc [/optimizer/rule/list/](../12-api-reference/11-automated-rules.md#doc-1738768861976578), hãy truyền mã múi giờ vào tham số yêu cầu `tzone`.
- **Tải xuống nhật ký thay đổi (Change log download)**:  
  Khi tạo tác vụ tải xuống nhật ký thay đổi qua [/changelog/task/create/](../12-api-reference/34-change-log.md#doc-1738811219460097), hãy truyền mã múi giờ vào tham số yêu cầu `timezone`.
- **Trung tâm doanh nghiệp (Business Center)**:  
  Khi tạo tài khoản quảng cáo trong Business Center qua [/bc/advertiser/create/](../12-api-reference/15-bc-assets.md#doc-1739939020318721), hãy truyền mã múi giờ vào tham số yêu cầu `timezone`.
- **Đối tượng tùy chỉnh (Custom Audiences)**:  
  Khi truy xuất nhật ký áp dụng mới nhất của đối tượng tùy chỉnh qua [/dmp/custom_audience/apply/log/](../12-api-reference/09-audience.md#doc-1758615737388033), hãy truyền mã múi giờ vào tham số yêu cầu `timezone`.
- **Nguồn cấp dữ liệu danh mục (Catalog feed)**:  
  Khi tạo nguồn cấp dữ liệu danh mục qua [/catalog/feed/create/](../12-api-reference/27-catalog-feeds.md#doc-1740665161957377), hãy truyền mã múi giờ vào tham số yêu cầu `timezone`.

| Code | Time |
|---|---|
| Africa/Accra | UTC+00:00 |
| Africa/Cairo | UTC+02:00 |
| Africa/Casablanca | UTC+01:00 |
| Africa/Johannesburg | UTC+02:00 |
| Africa/Lagos | UTC+01:00 |
| Africa/Nairobi | UTC+03:00 |
| Africa/Tunis | UTC+01:00 |
| America/Anchorage | UTC-09:00 |
| America/Argentina/Buenos_Aires | UTC-03:00 |
| America/Argentina/Salta | UTC-03:00 |
| America/Argentina/San_Luis | UTC-03:00 |
| America/Asuncion | UTC-03:00 |
| America/Atikokan | UTC-05:00 |
| America/Belem | UTC-03:00 |
| America/Blanc-Sablon | UTC-04:00 |
| America/Bogota | UTC-05:00 |
| America/Campo_Grande | UTC-04:00 |
| America/Caracas | UTC-04:00 |
| America/Chicago | UTC-06:00 |
| America/Costa_Rica | UTC-06:00 |
| America/Dawson | UTC-08:00 |
| America/Dawson_Creek | UTC-07:00 |
| America/Denver | UTC-07:00 |
| America/Edmonton | UTC-07:00 |
| America/El_Salvador | UTC-06:00 |
| America/Guatemala | UTC-06:00 |
| America/Guayaquil | UTC-05:00 |
| America/Halifax | UTC-04:00 |
| America/Hermosillo | UTC-07:00 |
| America/Iqaluit | UTC-05:00 |
| America/Jamaica | UTC-05:00 |
| America/La_Paz | UTC-04:00 |
| America/Lima | UTC-05:00 |
| America/Los_Angeles | UTC-08:00 |
| America/Managua | UTC-06:00 |
| America/Mazatlan | UTC-07:00 |
| America/Mexico_City | UTC-06:00 |
| America/Montevideo | UTC-03:00 |
| America/Nassau | UTC-05:00 |
| America/New_York | UTC-05:00 |
| America/Noronha | UTC-02:00 |
| America/Panama | UTC-05:00 |
| America/Phoenix | UTC-07:00 |
| America/Port_of_Spain | UTC-04:00 |
| America/Puerto_Rico | UTC-04:00 |
| America/Rainy_River | UTC-06:00 |
| America/Regina | UTC-06:00 |
| America/Santiago | UTC-04:00 |
| America/Santo_Domingo | UTC-04:00 |
| America/Sao_Paulo | UTC-03:00 |
| America/St_Johns | UTC-04:00 |
| America/Tegucigalpa | UTC-06:00 |
| America/Tijuana | UTC-08:00 |
| America/Toronto | UTC-05:00 |
| America/Vancouver | UTC-08:00 |
| Asia/Amman | UTC+02:00 |
| Asia/Baghdad | UTC+03:00 |
| Asia/Bahrain | UTC+03:00 |
| Asia/Bangkok | UTC+07:00 |
| Asia/Beirut | UTC+02:00 |
| Asia/Colombo | UTC+05:30 |
| Asia/Dhaka | UTC+06:00 |
| Asia/Dubai | UTC+04:00 |
| Asia/Gaza | UTC+02:00 |
| Asia/Ho_Chi_Minh | UTC+07:00 |
| Asia/Hong_Kong | UTC+08:00 |
| Asia/Irkutsk | UTC+08:00 |
| Asia/Jakarta | UTC+07:00 |
| Asia/Jayapura | UTC+09:00 |
| Asia/Jerusalem | UTC+02:00 |
| Asia/Kamchatka | UTC+12:00 |
| Asia/Karachi | UTC+05:00 |
| Asia/Kolkata | UTC+05:30 |
| Asia/Krasnoyarsk | UTC+07:00 |
| Asia/Kuala_Lumpur | UTC+08:00 |
| Asia/Kuwait | UTC+03:00 |
| Asia/Magadan | UTC+11:00 |
| Asia/Makassar | UTC+08:00 |
| Asia/Manila | UTC+08:00 |
| Asia/Muscat | UTC+04:00 |
| Asia/Nicosia | UTC+02:00 |
| Asia/Omsk | UTC+06:00 |
| Asia/Phnom_Penh | UTC+07:00 |
| Asia/Qatar | UTC+03:00 |
| Asia/Riyadh | UTC+03:00 |
| Asia/Seoul | UTC+09:00 |
| Asia/Shanghai | UTC+08:00 |
| Asia/Singapore | UTC+08:00 |
| Asia/Taipei | UTC+08:00 |
| Asia/Tokyo | UTC+09:00 |
| Asia/Vladivostok | UTC+10:00 |
| Asia/Yakutsk | UTC+09:00 |
| Asia/Yekaterinburg | UTC+05:00 |
| Atlantic/Azores | UTC-01:00 |
| Atlantic/Canary | UTC+00:00 |
| Atlantic/Reykjavik | UTC+00:00 |
| Australia/Broken_Hill | UTC+09:00 |
| Australia/Perth | UTC+08:00 |
| Australia/Sydney | UTC+10:00 |
| Europe/Amsterdam | UTC+01:00 |
| Europe/Athens | UTC+02:00 |
| Europe/Belgrade | UTC+01:00 |
| Europe/Berlin | UTC+01:00 |
| Europe/Bratislava | UTC+01:00 |
| Europe/Brussels | UTC+01:00 |
| Europe/Bucharest | UTC+02:00 |
| Europe/Budapest | UTC+01:00 |
| Europe/Copenhagen | UTC+01:00 |
| Europe/Dublin | UTC+01:00 |
| Europe/Helsinki | UTC+02:00 |
| Europe/Istanbul | UTC+03:00 |
| Europe/Kaliningrad | UTC+02:00 |
| Europe/Kiev | UTC+02:00 |
| Europe/Lisbon | UTC+00:00 |
| Europe/Ljubljana | UTC+01:00 |
| Europe/London | UTC+00:00 |
| Europe/Luxembourg | UTC+01:00 |
| Europe/Madrid | UTC+01:00 |
| Europe/Malta | UTC+01:00 |
| Europe/Moscow | UTC+03:00 |
| Europe/Oslo | UTC+01:00 |
| Europe/Paris | UTC+01:00 |
| Europe/Prague | UTC+01:00 |
| Europe/Riga | UTC+02:00 |
| Europe/Rome | UTC+01:00 |
| Europe/Samara | UTC+04:00 |
| Europe/Sarajevo | UTC+01:00 |
| Europe/Skopje | UTC+01:00 |
| Europe/Sofia | UTC+02:00 |
| Europe/Stockholm | UTC+01:00 |
| Europe/Tallinn | UTC+02:00 |
| Europe/Vienna | UTC+01:00 |
| Europe/Vilnius | UTC+02:00 |
| Europe/Warsaw | UTC+01:00 |
| Europe/Zagreb | UTC+01:00 |
| Europe/Zurich | UTC+01:00 |
| Indian/Maldives | UTC+05:00 |
| Indian/Mauritius | UTC+04:00 |
| Pacific/Apia | UTC+13:00 |
| Pacific/Auckland | UTC+12:00 |
| Pacific/Easter | UTC-06:00 |
| Pacific/Galapagos | UTC-06:00 |
| Pacific/Honolulu | UTC-10:00 |
| Pacific/Majuro | UTC+12:00 |
| Pacific/Midway | UTC-11:00 |
| Pacific/Niue | UTC-11:00 |
| Pacific/Pago_Pago | UTC-11:00 |

---

## Danh mục sở thích (`Interest category`)
<a id="doc-1738865030529025"></a>
<!-- doc_id: 1738865030529025 -->

> Đường dẫn: Appendix > Interest category

Trên nền tảng TikTok API for Business, danh mục sở thích (`Interest category`) hiện được sử dụng chủ yếu theo 3 cách:

1. **Nhắm mục tiêu (Targeting)**: Bao gồm các danh mục sở thích cụ thể khi bạn thiết lập tùy chọn nhắm mục tiêu để thu hẹp phạm vi đối tượng mong muốn tiếp cận.
2. **Bộ lọc nhóm trong báo cáo (Report grouping filter)**: Truyền các danh mục sở thích chính xác làm tiêu chí gom nhóm khi tạo báo cáo. Để tìm hiểu cách sử dụng danh mục sở thích trong Báo cáo đối tượng, xem [Báo cáo đối tượng (Audience report)](../09-marketing-api/bao-cao-p3.md#doc-1738864928947201).
3. **Phân loại dữ liệu phản hồi**: Phản hồi của endpoint [/report/ad_benchmark/get/](../12-api-reference/37-creative-reports.md#doc-1738824501176321) sẽ trả về danh mục sở thích cấp 2 (thông qua trường `ad_category`) đối với dữ liệu quảng cáo trò chơi (gaming ads) để phục vụ phân tích hiệu suất chuyên sâu.

### Danh mục sở thích liên quan đến trò chơi (`Gaming-related interest category`)

Nhằm hỗ trợ phân tích hiệu suất quảng cáo ngành trò chơi, hệ thống hỗ trợ danh sách danh mục sở thích chuyên biệt cho gaming. Dữ liệu phản hồi trong trường `ad_category` sẽ trả về ID của danh mục.

TikTok API for Business hỗ trợ hai cấp danh mục sở thích trò chơi: cấp 1 (level 1) và cấp 2 (level 2). Tất cả các danh mục sở thích trò chơi đều thuộc danh mục cấp 1 là `Games` (ID bắt đầu bằng `25`). Các danh mục con cấp 2 thuộc nhóm này sẽ có ID bắt đầu bằng `25xxx`. Ví dụ: nếu `ad_category` trả về `25302`, tra cứu bảng bên dưới sẽ tương ứng với danh mục `Casino`.

| Interest category ID | Tên danh mục (Interest category name) | Tên đầy đủ (Interest category full name) |
|---|---|---|
| 25 | Games (cấp 1) | Games |
| ↳ 25300 | Hyper-Casual (cấp 2) | Games-Hyper-Casual |
| ↳ 25301 | Action (Hành động) | Games-Action |
| ↳ 25302 | Casino (Sòng bạc) | Games-Casino |
| ↳ 25303 | Match (Ghép hình) | Games-Match |
| ↳ 25304 | Puzzle (Giải đố) | Games-Puzzle |
| ↳ 25305 | Racing (Đua xe) | Games-Racing |
| ↳ 25306 | RPG (Nhập vai) | Games-RPG |
| ↳ 25307 | Shooting (Bắn súng) | Games-Shooting |
| ↳ 25308 | Simulation (Mô phỏng) | Games-Simulation |
| ↳ 25309 | Sports (Thể thao) | Games-Sports |
| ↳ 25310 | Strategy (Chiến thuật) | Games-Strategy |
| ↳ 25311 | Party (Tiệc tùng) | Games-Party |
| ↳ 25312 | Tabletop (Cờ bàn) | Games-Tabletop |
| ↳ 25313 | Kids (Trẻ em) | Games-Kids |
| ↳ 25999 | Other (Khác) | Games-Other |

---

## ID ngành hàng cho Brand Profile (`Brand Profile industry IDs`)
<a id="doc-1830336456075458"></a>
<!-- doc_id: 1830336456075458 -->

> Đường dẫn: Appendix > Industries > Brand Profile industry IDs

Bảng dưới đây liệt kê các ID ngành hàng khả dụng bạn có thể truyền vào tham số `brand_industry_id` khi tạo Hồ sơ thương hiệu (Brand Profile) qua endpoint [/tto/tcm/brand/profile/create/](../12-api-reference/68-tiktok-one-p1.md#doc-1830335387914241):

| Industry ID (brand_industry_id) | Tên ngành hàng (`Industry Name`) |
|---|---|
| 290101 | Sản phẩm liên quan đến điện tử tiêu dùng (`Consumer Electronics Related Products`) |
| 290102 | Thiết bị điện gia dụng (`Electrical Appliances`) |
| 290103 | Sản phẩm điện tử và thiết bị điện khác (`Other Consumer Electronics Products and Electric Appliances`) |
| 290104 | Điện thoại di động (`Mobile Phones`) |
| 290105 | Phụ kiện điện thoại di động (`Mobile Phone Accessories`) |
| 290106 | Máy vi tính (`Computers`) |
| 290107 | Phụ kiện máy tính (`Computer Accessories`) |
| 290108 | Thương mại điện tử thiết bị điện và điện tử (`Consumer Electronics Products and Electric Appliance E-Commerce`) |
| 290109 | Bán lẻ ngoại tuyến đồ điện tử và gia dụng (`Offline Retail of Consumer Electronics Products and Electric Appliances`) |
| 290201 | Sản phẩm vệ sinh cá nhân và chăm sóc nhà cửa (`Personal Hygiene & Home Care Products`) |
| 290202 | Mỹ phẩm thông thường (`Ordinary Cosmetics`) |
| 290203 | Mỹ phẩm cao cấp (`High-end Cosmetics`) |
| 290204 | Mỹ phẩm đặc trị/chuyên dụng (`Special Cosmetics`) |
| 290205 | Thuốc lá (`Tobacco`) |
| 290206 | Đồ dùng cho thú cưng (`Pet Supplies`) |
| 290207 | Sản phẩm mẹ và bé (`Mother & Baby Products`) |
| 290208 | Hàng tiêu dùng nhanh khác (`Other Fast-Moving Consumer Goods - FMCG`) |
| 290209 | Sản phẩm người lớn (`Adult Supplies`) |
| 290210 | Thương mại điện tử mỹ phẩm & chăm sóc cá nhân (`Cosmetics & Personal Care E-Commerce`) |
| 290211 | Bán lẻ ngoại tuyến mỹ phẩm & chăm sóc cá nhân (`Offline Retail of Cosmetics & Personal Care`) |
| 290212 | Thương mại điện tử sản phẩm mẹ & bé (`Mother & Baby Products E-Commerce`) |
| 290213 | Bán lẻ ngoại tuyến sản phẩm mẹ & bé (`Offline Retail of Mother & Baby Products`) |
| 290214 | Thương mại điện tử rượu & thuốc lá (`Tobacco & Alcohol E-Commerce`) |
| 290215 | Bán lẻ ngoại tuyến rượu & thuốc lá (`Offline Retail of Tobacco & Alcohol`) |
| 290216 | Thương mại điện tử đồ dùng thú cưng (`Pet Supplies E-Commerce`) |
| 290217 | Bán lẻ ngoại tuyến đồ dùng thú cưng (`Offline Retail of Pet Products`) |
| 290218 | Sản phẩm từ cây gai dầu (`Hemp Related Products`) |
| 290301 | Đồ ăn vặt / Snack (`Snacks`) |
| 290302 | Đồ uống không cồn (`Beverages - Non-alcoholic`) |
| 290303 | Bia, rượu vang & đồ uống có cồn (`Beer, Wine & Liquor`) |
| 290304 | Sản phẩm từ sữa & thức uống sữa (`Dairy Products & Dairy Drinks`) |
| 290305 | Nhu yếu phẩm & nguyên liệu nấu ăn (`Daily Necessities & Cooking Ingredients`) |
| 290306 | Thực phẩm tươi sống (`Fresh Food`) |
| 290307 | Thực phẩm chức năng (`Functional Food`) |
| 290308 | Nông sản khác (`Other Farm Products`) |
| 290310 | Đồ ăn & đồ uống khác (`Other Food & Drinks`) |
| 290311 | TMĐT thực phẩm & đồ uống không tươi sống (`Food and Beverage Non-Fresh E-Commerce`) |
| 290312 | Bán lẻ ngoại tuyến thực phẩm & đồ uống không tươi sống (`Offline Retail of Food and Beverage Non-Fresh`) |
| 290313 | TMĐT thực phẩm tươi sống (`Fresh Products E-Commerce`) |
| 290314 | Bán lẻ ngoại tuyến thực phẩm tươi sống (`Offline Retail of Fresh Products`) |
| 290401 | Quần áo & giày dép thông thường (`Ordinary Clothing & Shoes`) |
| 290402 | Quần áo & giày dép cao cấp / xa xỉ (`Luxury Clothing & Shoes`) |
| 290403 | Kính mắt & túi xách thông thường (`Ordinary Glasses & Bags`) |
| 290404 | Kính mắt & túi xách cao cấp (`Luxury Glasses & Bags`) |
| 290405 | Đồng hồ thông thường (`Ordinary Watches`) |
| 290406 | Đồng hồ cao cấp (`Luxury Watches`) |
| 290407 | Trang sức thông thường (`Ordinary Jewelry`) |
| 290408 | Trang sức cao cấp (`Luxury Jewelry`) |
| 290409 | Trang phục & phụ kiện khác (`Other Clothing & Accessories`) |
| 290410 | TMĐT phụ kiện thời trang (`Clothing Accessories E-Commerce`) |
| 290411 | Bán lẻ ngoại tuyến phụ kiện thời trang (`Offline Retail of Clothing Accessories`) |
| 290501 | Cơ sở y tế (`Medical Institutions`) |
| 290502 | Thiết bị y tế (`Medical Devices`) |
| 290503 | Dịch vụ y tế liên quan (`Medical-Related Services`) |
| 290504 | Y tế & dược phẩm khác (`Other Healthcare & Pharmaceutical`) |
| 290505 | Thuốc (`Medicine`) |
| 290506 | Sản phẩm thực phẩm bổ sung sức khỏe (`Health Supplement Products`) |
| 290507 | Nền tảng dịch vụ y tế tích hợp (`Integrated Medical Service Platforms`) |
| 290508 | Thuốc thú y (`Veterinary Medicine`) |
| 290509 | Nhà thuốc trực tuyến / TMĐT dược phẩm (`Online Pharmacies/Pharmaceutical E-Commerce`) |
| 290510 | Bán lẻ ngoại tuyến nhà thuốc / dược phẩm (`Offline Retail of Pharmacy/Pharmaceutical`) |
| 290511 | Thuốc kê đơn (`Prescription drugs`) |
| 290512 | Dược mỹ phẩm (`Cosmeceuticals`) |
| 290601 | Dịch vụ an ninh & an toàn (`Safety and Security Services`) |
| 290602 | Xuất bản (`Publishing`) |
| 290603 | Đóng gói & in ấn (`Packaging & Printing`) |
| 290604 | Dịch vụ đại lý trung gian (`Intermediary Agent Services`) |
| 290605 | Dịch vụ tư vấn (`Consulting Services`) |
| 290606 | Dịch vụ quảng cáo, PR & tiếp thị (`Advertising & PR & Marketing Services`) |
| 290607 | Biểu diễn thương mại & triển lãm (`Commercial Performance & Exhibition`) |
| 290608 | Thiết kế (`Design`) |
| 290609 | Kế toán & thuế (`Accounting & Taxation`) |
| 290610 | Dịch vụ pháp lý (`Legal Services`) |
| 290611 | Dịch vụ nhân sự (`HR services`) |
| 290612 | Sản xuất theo hợp đồng OEM (`OEM`) |
| 290613 | An toàn dữ liệu (`Data Security`) |
| 290614 | Dịch vụ chuyên nghiệp khác (`Other Professional Services`) |
| 290701 | Dịch vụ tổng hợp (`Comprehensive Services`) |
| 290702 | Dịch vụ sửa chữa vặt & chạy việc (`Handyman and errand services`) |
| 290703 | Dịch vụ dọn dẹp & việc nhà (`Housekeeping Services`) |
| 290704 | Dịch vụ điều dưỡng & chăm sóc (`Nursing Services`) |
| 290705 | Nhiếp ảnh (`Photography`) |
| 290706 | Dịch vụ làm đẹp (`Beauty Services`) |
| 290707 | Dịch vụ tái chế (`Recycling Services`) |
| 290708 | Dịch vụ cho thuê (`Rental Services`) |
| 290709 | Dịch vụ hẹn hò & mai mối (`Dating & Matchmaking Services`) |
| 290710 | Dịch vụ giao hàng (`Delivery Services`) |
| 290711 | Dịch vụ định cư & di trú (`Immigration Services`) |
| 290712 | Dịch vụ tiện ích công cộng (`Utility Services`) |
| 290713 | Dịch vụ tiện ích khác (`Other Convenience Services`) |
| 290715 | Dịch vụ cưới hỏi (`Marriage Services`) |
| 290716 | Dịch vụ tang lễ (`Funeral Services`) |
| 290801 | Chủ đầu tư bất động sản (`Real Estate Developers`) |
| 290802 | Đại lý môi giới bất động sản (`Real Estate Intermediary Agencies`) |
| 290803 | Công ty quản lý bất động sản (`Property Management Companies`) |
| 290804 | Đại lý phân phối bất động sản (`Real Estate Sales Agencies`) |
| 290805 | Cho thuê căn hộ (`Apartment Rentals`) |
| 290806 | Bất động sản khác bao gồm cho thuê (`Other Real Estate including leasing & rental`) |
| 290807 | Dịch vụ bất động sản toàn diện (`Real Estate Comprehensive Services`) |
| 290901 | Vật liệu trang trí nội thất (`Home Decoration Materials`) |
| 290902 | Ngũ kim & thiết bị điện (`Hardware & Electrical`) |
| 290903 | Thiết kế & thi công nội thất (`Decoration & Design`) |
| 290904 | Đồ nội thất (`Furniture`) |
| 290905 | Phụ kiện trang trí nhà cửa (`Home Accessories`) |
| 290906 | Vật liệu nội thất khác (`Other Home Furnishing Materials`) |
| 290907 | Hàng hóa tổng hợp (`General Merchandise`) |
| 290908 | Thanh lọc môi trường trong nhà (`Indoor Environment Purification`) |
| 290909 | Vật liệu nội thất bổ trợ (`Complementary Furnishing Materials`) |
| 290910 | Công trình xây dựng (`Construction Works`) |
| 290911 | Nền tảng dịch vụ vật liệu nội thất tổng hợp (`Home Furnishing Materials Comprehensive Service Platforms`) |
| 290912 | TMĐT vật liệu nội thất (`Home Furnishing Materials E-Commerce`) |
| 290913 | Bán lẻ ngoại tuyến vật liệu nội thất (`OffLine Retail of Home Furnishing Materials`) |
| 291001 | Giáo dục mầm non (`Early Childhood Education`) |
| 291002 | Giáo dục tiểu học & trung học (`Primary & Secondary Education`) |
| 291003 | Giáo dục đại học (`College Education`) |
| 291004 | Học ngôn ngữ & du học (`Language Learning & Study Abroad`) |
| 291005 | Đào tạo năng khiếu & sở thích (`Interest & Hobby Training`) |
| 291006 | Đào tạo nghề (`Vocational Training`) |
| 291007 | Phát triển doanh nghiệp & chuyên môn (`Corporate & Professional Development`) |
| 291008 | Giáo dục & đào tạo khác (`Other Education and Training`) |
| 291009 | Giáo dục đặc biệt (`Special Needs Education`) |
| 291101 | Điểm tham quan du lịch (`Tourist Attractions`) |
| 291102 | Lưu trú / Khách sạn (`Accommodation`) |
| 291103 | Đại lý du lịch trực tuyến (`OTA - Online Travel Agencies`) |
| 291104 | Đại lý du lịch truyền thống (`Offline Travel Agencies`) |
| 291105 | Giao thông công cộng (`public transport`) |
| 291109 | Đại lý vé (`Ticket Agencies`) |
| 291111 | Du lịch khác (`Other Travel`) |
| 291201 | Cơ quan chính phủ về văn hóa & du lịch (`Government Department for Culture and Traveling`) |
| 291202 | Phi lợi nhuận & tổ chức phi chính phủ (`Nonprofit & NGOs`) |
| 291203 | Xây dựng đô thị (`Municipal Construction`) |
| 291204 | Tôn giáo (`Religion`) |
| 291205 | Chính trị (`Politics`) |
| 291206 | Hành chính công khác (`Other Public Administration`) |
| 291207 | Quản lý hành chính, khoa học, giáo dục và y tế (`Administration, Science, Education, and Health`) |
| 291208 | An toàn công cộng (`Public Safety`) |
| 291301 | Trò chơi giải trí nhẹ & trí tuệ (`Casual & Brain Games`) |
| 291302 | Trò chơi bài & cờ (`Card & Board Games`) |
| 291303 | Trò chơi nhập vai (`RPG - Roleplaying Games`) |
| 291304 | Trò chơi hành động & bắn súng (`Action & Shooting Games`) |
| 291305 | Trò chơi đua xe & thể thao (`Racing & Sports Games`) |
| 291306 | Trò chơi mô phỏng (`Simulation Games`) |
| 291307 | Trò chơi chiến thuật (`Strategy Games`) |
| 291308 | Trò chơi trực tuyến nhiều người chơi (`Multiplayer Online Games`) |
| 291309 | Trò chơi khác (`Other Games`) |
| 291310 | Trò chơi cha mẹ và con cái (`Parent-Children Games`) |
| 291311 | Trò chơi phiêu lưu (`Adventure Games`) |
| 291312 | Trò chơi có yếu tố cờ bạc (`Gambling Element Games`) |
| 291313 | Dịch vụ và sản phẩm trò chơi tích hợp (`Integrated Game and Related Products and Services`) |
| 291314 | Trò chơi siêu đơn giản (`Hypercasual Games`) |
| 291401 | TMĐT B2B toàn diện (`Comprehensive 2B E-commerce`) |
| 291402 | TMĐT B2B ngành dọc (`Vertical 2B E-commerce`) |
| 291403 | TMĐT B2C toàn diện (`Comprehensive 2C E-commerce`) |
| 291404 | TMĐT mạng xã hội (`Social E-commerce`) |
| 291405 | TMĐT B2C ngành dọc (`Vertical 2C E-commerce`) |
| 291406 | Bán lẻ ngoại tuyến tổng hợp (`Comprehensive Offline Retail`) |
| 291407 | Bán lẻ ngoại tuyến chuyên ngành (`Vertical Offline Retail`) |
| 291408 | Bán lẻ & TMĐT khác (`Other Retail & E-commerce`) |
| 291501 | Chế tạo máy bay (`Aircraft Manufacturing`) |
| 291502 | Đóng tàu (`Shipbuilders`) |
| 291504 | Chế tạo phương tiện không động cơ (`Non-motor Vehicle Manufacturing`) |
| 291505 | Phương tiện chuyên dụng (`Functional Vehicles`) |
| 291506 | Giao thông vận tải khác (`Other Transport`) |
| 291507 | Sản phẩm & dịch vụ liên quan giao thông (`Transportation Related Products & Services`) |
| 291601 | Chế tạo ô tô con (`Small Vehicle Manufacturing`) |
| 291602 | Đại lý phân phối ô tô (`Automobile Dealers`) |
| 291603 | Kinh doanh ô tô đã qua sử dụng (`Second-hand Automobile Businesses`) |
| 291604 | Dịch vụ ô tô (`Automotive Services`) |
| 291605 | Ngành ô tô khác (`Other Automotive`) |
| 291606 | Nền tảng dịch vụ ô tô tích hợp (`Automotive Integrated Service Platforms`) |
| 291607 | Bán lẻ ngoại tuyến ô tô mới (`Offline Retail of New Car`) |
| 291608 | Chế tạo xe máy (`Motorbike Manufacturing`) |
| 291609 | Chế tạo xe tải và xe cỡ trung/lớn (`Medium & Large Vehicle Manufacturing`) |
| 291701 | Trồng trọt (`Crop Production`) |
| 291702 | Lâm nghiệp (`Forestry`) |
| 291703 | Nuôi trồng thủy sản (`Aquaculture`) |
| 291704 | Săn bắt (`Hunting`) |
| 291705 | Chăn nuôi gia súc, gia cầm (`Animal Husbandry`) |
| 291706 | Dịch vụ lâm nghiệp (`Forestry Services`) |
| 291707 | Chế biến nông sản (`Farm Produce Processing`) |
| 291708 | Phân bón hóa học & thuốc trừ sâu (`Chemical Fertilizers & Pesticides`) |
| 291709 | Khu vực sản xuất sơ cấp khác (`Other Primary Sector`) |
| 291801 | Sản phẩm hóa chất (`Chemical Products`) |
| 291802 | Sản phẩm khử trùng (`Disinfection Products`) |
| 291803 | Hóa chất độc hại/nguy hiểm (`Hazardous Chemicals`) |
| 291804 | Phụ gia thực phẩm (`Food Additives`) |
| 291805 | Hóa chất khác (`Other Chemicals`) |
| 291806 | Nhiên liệu năng lượng (`Fuel Energy`) |
| 291807 | Năng lượng điện (`Electrical Energy`) |
| 291808 | Năng lượng mới (`New Energy`) |
| 291809 | Tài nguyên khoáng sản (`Mineral Resources`) |
| 291810 | Xử lý ô nhiễm (`Pollution Treatment`) |
| 291811 | Tái chế chất thải (`Waste Recycling`) |
| 291812 | Tiết kiệm năng lượng (`Energy Conservation`) |
| 291813 | Năng lượng khác (`Other Energy`) |
| 291902 | Thiết bị & dụng cụ đo lường (`Instruments & Apparatus`) |
| 291903 | Thiết bị điện năng (`Power Equipment`) |
| 291904 | Chế tạo máy móc điện (`Electric Machinery Production`) |
| 291905 | Thiết bị điện & điện tử khác (`Other Electronics & Electrical`) |
| 292001 | Thiết bị cơ khí thông dụng (`General Mechanical Equipment`) |
| 292002 | Máy móc nông lâm nghiệp (`Agricultural & Forestry Machinery`) |
| 292003 | Máy móc khai khoáng, dầu khí (`Mining, Oil & Gas Machinery`) |
| 292004 | Máy móc xây dựng (`Construction Machinery`) |
| 292005 | Máy móc ngành hóa chất (`Chemical Machinery`) |
| 292006 | Máy chế biến gỗ & đá (`Wood & Stone Processing Machinery`) |
| 292007 | Máy công cụ (`Machine Tool Machinery`) |
| 292008 | Máy móc thương mại (`Commercial Machinery`) |
| 292009 | Máy móc cơ bản (`Basic Machinery`) |
| 292010 | Dụng cụ & phụ tùng cơ khí (`Tools & Accessories`) |
| 292011 | Máy móc chế biến thực phẩm (`Food Machinery`) |
| 292013 | Thiết bị làm sạch & thông gió (`Cleaning & Ventilation Equipment`) |
| 292014 | Máy móc cơ khí khác (`Other Machinery`) |
| 292101 | Sự kiện biểu diễn, lễ hội & triển lãm (`Shows, Festivals & Exhibitions`) |
| 292102 | Di tích văn hóa & đồ sưu tầm nghệ thuật (`Cultural Relics & Art Collectibles`) |
| 292103 | Văn phòng phẩm, đồ chơi & quà tặng (`Stationary, Toys & Gifts`) |
| 292104 | Nhạc cụ (`Musical Instruments`) |
| 292105 | Giải trí trong nhà (`Indoor Entertainment`) |
| 292106 | Thể dục & thể hình (`Exercise & Fitness`) |
| 292107 | Dụng cụ thể thao (`Sporting Equipment`) |
| 292108 | Dụng cụ dã ngoại ngoài trời (`Outdoor Equipment`) |
| 292109 | Địa điểm & sự kiện thể thao (`Sporting Events & Venues`) |
| 292110 | Làm vườn / Trồng trọt cảnh quan (`Horticulture`) |
| 292112 | Hoạt động giải trí ngoài trời (`Outdoor Recreation`) |
| 292113 | Văn hóa, thể thao & giải trí khác (`Other Culture, Sports & Entertainment`) |
| 292114 | Thẻ thành viên & phiếu giảm giá (`Membership Cards & Vouchers`) |
| 292115 | Sòng bạc, cá cược & xổ số (`Casinos & Betting & Lottery`) |
| 292116 | TMĐT thể thao & giải trí (`Sports & Entertainment E-Commerce`) |
| 292117 | Bán lẻ ngoại tuyến thể thao & giải trí (`Sports & Entertainment Off-Line Retail`) |
| 292201 | Đài truyền hình (`TV Stations`) |
| 292202 | Đài phát thanh (`Radio Stations`) |
| 292203 | Hãng phim (`Movie Studios`) |
| 292204 | Sản xuất âm thanh & video (`Audio & Video Production`) |
| 292205 | Sách & tạp chí trực tuyến (`Online Books & Magazines`) |
| 292207 | Kênh thông tin tổng hợp (`Comprehensive Information`) |
| 292208 | Kênh thông tin chuyên ngành (`Vertical Information`) |
| 292209 | Video & phát trực tiếp (`Video & Live Streaming`) |
| 292210 | Truyền thông & nội dung khác (`Other Media & Content`) |
| 292211 | Sách & tạp chí in ấn (`Printed Books & Magazines`) |
| 292212 | Nhà cung cấp dịch vụ OTT (`OTT Vendors`) |
| 292301 | Dịch vụ chuyển phát nhanh & vận chuyển hàng hóa (`Courier & Freight Services`) |
| 292302 | Giao nhận vận tải (`Freight Forwarding`) |
| 292303 | Vận chuyển hàng hóa đặc biệt (`Special Goods Transportation`) |
| 292304 | Hạ tầng logistics (`Logistics Infrastructure`) |
| 292305 | Logistics khác (`Other Logistics`) |
| 292401 | Nhà mạng viễn thông (`Telecom Operators`) |
| 292402 | Nhà mạng viễn thông di động ảo (`Virtual Network Operators - VNO`) |
| 292403 | Thiết bị viễn thông (`Telecommunication Equipment`) |
| 292404 | Viễn thông khác (`Other Telecommunications`) |
| 292501 | Ngân hàng (`Banking`) |
| 292502 | Chứng khoán (`Securities`) |
| 292503 | Bảo hiểm (`Insurance`) |
| 292504 | Dịch vụ quản lý ủy thác (`Trust Management Services`) |
| 292505 | Bảo lãnh & bao thanh toán (`Guarantees & Factoring`) |
| 292506 | Bán đấu giá & tiệm cầm đồ (`Auctions & Pawnshops`) |
| 292507 | Hợp đồng tương lai (`Futures`) |
| 292508 | Quỹ đầu tư (`Funds`) |
| 292509 | Dịch vụ tín dụng (`Credit Service`) |
| 292510 | Cho vay tiêu dùng nhỏ (`Small-loan Lenders`) |
| 292511 | Tài chính truyền thống khác (`Other Traditional Finance`) |
| 292512 | Tổ chức phát hành thẻ ngân hàng (`Bank Card Organizations`) |
| 292601 | Quản lý tài chính toàn diện (`Comprehensive Financial Management`) |
| 292602 | Nền tảng chứng khoán trực tuyến (`Online Securities Platforms`) |
| 292604 | Dịch vụ cho vay (`Loan Services`) |
| 292605 | Ngoại hối (`Foreign Exchange`) |
| 292606 | Kim loại quý (`Precious Metals`) |
| 292607 | Cho vay ngang hàng P2P (`P2P`) |
| 292608 | Thanh toán bên thứ ba (`Third Party Payments`) |
| 292609 | Gọi vốn cộng đồng (`Crowdfunding`) |
| 292610 | Tiền kỹ thuật số (`Digital Currencies`) |
| 292611 | Cổng thông tin tài chính điện tử (`Financial Web Portals`) |
| 292612 | Ngân hàng số trực tuyến (`Online Banking`) |
| 292613 | Bảo hiểm trực tuyến (`Internet Insurance`) |
| 292614 | Nền tảng và công cụ tài chính toàn diện (`Comprehensive Financial Platforms and Tools`) |
| 292615 | Tài chính internet khác (`Other Internet Finance`) |
| 292701 | Nhà hàng và điểm ăn uống (`Restaurants and Other Eating Places`) |
| 292702 | Quán đồ uống có cồn hoặc giải khát (`Drinking Places - Alcoholic or Beverages`) |
| 292703 | Dịch vụ ăn uống khác (`Other Catering Services`) |
| 292801 | Công cụ phần mềm (`Software Tools`) |
| 292802 | Xử lý đa phương tiện (`Multimedia Processing`) |
| 292803 | Tin nhắn mạng xã hội (`Social Messaging`) |
| 292804 | Công cụ tiện ích (`Utility Tools`) |
| 292805 | Phần mềm tiện ích khác (`Other Utility Software`) |
| 293101 | Nền tảng cơ hội nhượng quyền (`Franchise Opportunities Platforms`) |
| 293102 | Nhượng quyền sản phẩm đời sống thường ngày (`Daily Life Products Franchising`) |
| 293103 | Nhượng quyền dịch vụ tiện ích (`Convenience Service Franchising`) |
| 293104 | Nhượng quyền trang phục & phụ kiện (`Clothing & Accessories Franchising`) |
| 293105 | Nhượng quyền thẩm mỹ viện / salon làm đẹp (`Beauty Salon Franchising`) |
| 293106 | Nhượng quyền giải trí trong nhà (`Indoor Entertainment Franchising`) |
| 293107 | Nhượng quyền giáo dục & đào tạo (`Education & Training Franchising`) |
| 293108 | Nhượng quyền khách sạn (`Hotel Franchising`) |
| 293109 | Nhượng quyền nhà hàng (`Restaurant Franchising`) |
| 293110 | Nhượng quyền ngành dược (`Medicine Franchising`) |
| 293111 | Nhượng quyền bất động sản, xây dựng & vật liệu (`Real Estate, Home Building & Materials Franchising`) |
| 293112 | Nhượng quyền thực phẩm (`Food Franchising`) |
| 293113 | Nhượng quyền công nghiệp (`Industrial Franchising`) |
| 293114 | Nhượng quyền sản phẩm ô tô (`Automotive Product Franchising`) |
| 293115 | Nhượng quyền phần mềm internet (`Internet Software Franchising`) |
| 293116 | Nhượng quyền đại lý tuyển dụng (`Recruitment Agency Franchising`) |
| 293117 | Nhượng quyền khác (`Other Franchising`) |
| 293118 | Nhượng quyền giảm cân (`Weight Loss Franchising`) |
| 293119 | Nhượng quyền đồ uống & làm bánh (`Drinks & Baking Franchising`) |
| 293120 | Nhượng quyền sản phẩm chăm sóc sức khỏe (`Health Products Franchising`) |
| 293121 | Nhượng quyền đồ uống có cồn (`Alcohol Franchising`) |
| 293122 | Nhượng quyền nông nghiệp (`Agricultural Franchising`) |
| 293123 | Nhượng quyền dịch vụ doanh nghiệp (`Business Services Franchising`) |

---

## Độ chính xác theo từng loại tiền tệ (`Currency-specific precision`)
<a id="doc-1772544628718594"></a>
<!-- doc_id: 1772544628718594 -->

> Đường dẫn: Appendix > Currency-specific precision

Độ chính xác (số chữ số phần thập phân) được hỗ trợ phụ thuộc vào loại tiền tệ của tài khoản nhà quảng cáo của bạn. Tra cứu bảng dưới đây để biết độ chính xác cho phép đối với từng loại tiền tệ:

| Currency code | Precision |
|---|---|
| NIO | 0.01 |
| DZD | 0.01 |
| EGP | 0.01 |
| BOB | 0.01 |
| DKK | 0.01 |
| BWP | 0.01 |
| LBP | 0.01 |
| TZS | 0.01 |
| VND | 1 |
| AOA | 0.01 |
| GHS | 0.01 |
| LYD | 0.001 |
| UAH | 0.01 |
| JOD | 0.001 |
| SAR | 0.01 |
| HKD | 0.01 |
| CHF | 0.01 |
| BYN | 0.01 |
| BGN | 0.01 |
| HRK | 0.01 |
| THB | 0.01 |
| XAF | 1 |
| BND | 0.01 |
| ISK | 1 |
| UYU | 0.01 |
| LAK | 0.01 |
| NPR | 0.01 |
| SYP | 0.01 |
| MAD | 0.01 |
| PHP | 0.01 |
| ZAR | 0.01 |
| ALL | 0.01 |
| NGN | 0.01 |
| AED | 0.01 |
| GBP | 0.01 |
| MWK | 0.01 |
| LKR | 0.01 |
| PKR | 0.01 |
| HUF | 1 |
| MNT | 0.01 |
| UGX | 1 |
| QAR | 0.01 |
| MKD | 0.01 |
| TRY | 0.01 |
| YER | 0.01 |
| SLL | 0.01 |
| NOK | 0.01 |
| MOP | 0.01 |
| SSP | 0.01 |
| INR | 0.01 |
| MXN | 0.01 |
| CZK | 0.01 |
| COP | 0.01 |
| MYR | 0.01 |
| MUR | 0.01 |
| IDR | 1 |
| PEN | 0.01 |
| ILS | 0.01 |
| TWD | 1 |
| MDL | 0.01 |
| SEK | 0.01 |
| MVR | 0.01 |
| AUD | 0.01 |
| SRD | 0.01 |
| KRW | 1 |
| VEF | 0.01 |
| CLP | 1 |
| ZMW | 0.01 |
| EUR | 0.01 |
| KZT | 0.01 |
| RUB | 0.01 |
| OMR | 0.01 |
| BRL | 0.01 |
| MMK | 0.01 |
| PLN | 0.01 |
| PYG | 1 |
| KES | 0.01 |
| USD | 0.01 |
| IQD | 0.001 |
| BAM | 0.01 |
| CAD | 0.01 |
| KWD | 0.001 |
| SGD | 0.01 |
| UZS | 0.01 |
| IRR | 0.01 |
| CNY | 0.01 |
| TND | 0.001 |
| GYD | 0.01 |
| NZD | 0.01 |
| ARS | 0.01 |
| RON | 0.01 |
| RSD | 0.01 |
| BHD | 0.01 |
| JPY | 1 |
| SDG | 0.01 |
| HNL | 0.01 |
| GTQ | 0.01 |
| CRC | 0.01 |
| BDT | 0.01 |
| KHR | 1 |

---

## Đối chiếu giữa các loại quảng bá khác nhau (`Mapping between different promotion types`)
<a id="doc-1758485431181314"></a>
<!-- doc_id: 1758485431181314 -->

> Đường dẫn: Appendix > Mapping between different promotion types

Bảng dưới đây thể hiện mối tương quan giữa giá trị `promotion_type` dùng để lọc nhóm quảng cáo (thông qua [/smart_plus/adgroup/get/](../12-api-reference/62-upgraded-smartplus-p2.md#doc-1843314879617026) hoặc [/adgroup/get/](../12-api-reference/07-ad-groups-p1.md#doc-1739314558673922)) theo từng mục tiêu quảng cáo, và giá trị `promotion_type` tương ứng được dùng làm tham số khi tạo nhóm quảng cáo:

| Mục tiêu quảng cáo (`objective_type`) | Giá trị `promotion_type` khi lọc nhóm quảng cáo | Giá trị `promotion_type` khi tạo nhóm quảng cáo |
|---|---|---|
| `APP_PROMOTION`<br>`TRAFFIC` | `APP` | `APP_ANDROID`<br>`APP_IOS` |
| `APP_PROMOTION`<br>`TRAFFIC` | `WEBSITE` | `WEBSITE` |
| `WEB_CONVERSIONS` | `WEBSITE` | `WEBSITE` |
| `LEAD_GENERATION` | `WEBSITE` | `LEAD_GENERATION` |
| `LEAD_GENERATION` | `INSTANT_FORM` | `LEAD_GENERATION` |
| `LEAD_GENERATION` | `LEAD_GEN_CLICK_TO_TT_DIRECT_MESSAGE` | `LEAD_GEN_CLICK_TO_TT_DIRECT_MESSAGE` |
| `LEAD_GENERATION` | `LEAD_GEN_CLICK_TO_SOCIAL_MEDIA_APP_MESSAGE` | `LEAD_GEN_CLICK_TO_SOCIAL_MEDIA_APP_MESSAGE` |
| `LEAD_GENERATION` | `LEAD_GEN_CLICK_TO_CALL` | `LEAD_GEN_CLICK_TO_CALL` |

---

## Loại trang đích có thể lọc theo mục tiêu quảng cáo (`Filterable destination page type for an advertising objective`)
<a id="doc-1764306884771842"></a>
<!-- doc_id: 1764306884771842 -->

> Đường dẫn: Appendix > Filterable destination page type for an advertising objective

Bảng dưới đây liệt kê các loại trang đích được hỗ trợ mà bạn có thể lọc thông qua trường `destination` trong endpoint [/ad/get/](../12-api-reference/02-ads-p1.md#doc-1735735588640770) tương ứng với từng mục tiêu quảng cáo:

| Giá trị `objective_type` | Các giá trị `destination` được hỗ trợ |
|---|---|
| `APP_PROMOTION` | `APP`<br>`TIKTOK_INSTANT_PAGE` |
| `WEB_CONVERSIONS` | `TIKTOK_INSTANT_PAGE`<br>`WEBSITE` |
| `REACH` | `TIKTOK_INSTANT_PAGE`<br>`WEBSITE` |
| `TRAFFIC` | `APP`<br>`TIKTOK_INSTANT_PAGE`<br>`WEBSITE` |
| `VIDEO_VIEWS` | `TIKTOK_INSTANT_PAGE`<br>`WEBSITE` |
| `LEAD_GENERATION` | `TIKTOK_INSTANT_PAGE`<br>`WEBSITE`<br>`SOCIAL_MEDIA_APP`<br>`PHONE_CALL` |
| `RF_REACH` | `TIKTOK_INSTANT_PAGE`<br>`WEBSITE` |

---

## Chính sách quảng cáo (`Advertising Policies`)
<a id="doc-1759238007931906"></a>
<!-- doc_id: 1759238007931906 -->

> Đường dẫn: Appendix > Advertising Policies

Chương này bao gồm các quy định và chính sách quảng cáo quan trọng trên TikTok:
- [Chính sách quảng cáo về Chính trị, Chính phủ và Bầu cử của TikTok](phu-luc-p1.md#doc-1844612550411265)
- [Chính sách quảng cáo Chống phân biệt đối xử của TikTok](phu-luc-p1.md#doc-1759238111603713)
- [Giới hạn độ tuổi mới đối với quảng cáo trên TikTok](phu-luc-p1.md#doc-1788755983247362)

Để tìm hiểu toàn bộ Chính sách quảng cáo của TikTok, xem thêm [tại đây](https://ads.tiktok.com/help/article/advertising-on-tiktok-first-things-to-note?lang=en).

---

## Chính sách quảng cáo về Chính trị, Chính phủ và Bầu cử của TikTok (`TikTok’s Politics, Governments, and Elections Advertising Policy`)
<a id="doc-1844612550411265"></a>
<!-- doc_id: 1844612550411265 -->

> Đường dẫn: Appendix > Advertising Policies > TikTok’s Politics, Governments, and Elections Advertising Policy

Tất cả các doanh nghiệp tham gia quảng cáo trên TikTok đều phải tuân thủ chính sách quảng cáo về chính trị, chính phủ và bầu cử của nền tảng.

### Chính sách quảng cáo về Chính trị, Chính phủ và Bầu cử của TikTok là gì?

Trên TikTok, cộng đồng người dùng có thể chia sẻ nội dung chính trị một cách tự nhiên (organic) miễn là nội dung đó phù hợp với [Nguyên tắc cộng đồng (Community Guidelines)](https://www.tiktok.com/community-guidelines/en/). Tuy nhiên, TikTok **không cho phép quảng cáo chính trị trả phí** vì bản chất của quảng cáo chính trị không phù hợp với trải nghiệm trên nền tảng. Ngoài chính sách về quảng cáo chính trị trả phí, TikTok nghiêm cấm mọi hình thức quảng cáo từ các nhân vật và thực thể chính trị.

Các thực thể chính phủ và liên chính phủ đủ điều kiện quảng cáo trên TikTok với điều kiện họ phải làm việc trực tiếp với đại diện kinh doanh của TikTok, hoàn tất quy trình chứng nhận và tuân thủ tất cả chính sách nền tảng, bao gồm chính sách quảng cáo chính phủ.

Chỉ các cơ quan chính thức chịu trách nhiệm giám sát bầu cử mới đủ điều kiện quảng cáo về bầu cử hoặc trưng cầu dân ý. Mọi nội dung đề cập đến cuộc bầu cử hoặc trưng cầu dân ý sắp tới hoặc đang diễn ra — bao gồm kêu gọi bỏ phiếu, đăng ký cử tri và khuyến khích tham gia — đều bị nghiêm cấm đối với tất cả các nhà quảng cáo khác.

Xem thêm chi tiết tại [Chính sách quảng cáo chính trị, chính phủ và bầu cử của TikTok](https://ads.tiktok.com/help/article/tiktok-ads-policy-politics-government-and-elections).

### Bạn cần làm gì?

Hãy nhắc nhở các nhà quảng cáo của bạn truy cập [TikTok Ads Manager](https://ads.tiktok.com/i18n/) để hoàn tất xác nhận tuân thủ Chính sách quảng cáo về Chính trị, Chính phủ và Bầu cử trước ngày **10 tháng 1 năm 2026**.

Nếu bạn muốn kiểm tra thông tin người dùng của nhà quảng cáo (chẳng hạn như email và core user ID), hãy sử dụng endpoint **/user/info/**.

> [!WARNING]
> Nếu nhà quảng cáo của bạn không hoàn tất quy trình chứng nhận tuân thủ này trước ngày 10/01/2026, các nhà phát triển có thể sẽ không thể thực hiện bất kỳ thao tác nào đối với tài khoản người dùng TikTok for Business của họ qua API. Vui lòng phối hợp với nhà quảng cáo để hoàn thành chứng nhận càng sớm càng tốt nhằm đảm bảo hoạt động API không bị gián đoạn.

---

## Chính sách quảng cáo Chống phân biệt đối xử của TikTok (`TikTok’s Anti-Discrimination Ad Policy`)
<a id="doc-1759238111603713"></a>
<!-- doc_id: 1759238111603713 -->

> Đường dẫn: Appendix > Advertising Policies > TikTok’s Anti-Discrimination Ad Policy

Tất cả các doanh nghiệp tham gia quảng cáo trên TikTok phải tuân thủ chính sách chống phân biệt đối xử của chúng tôi.

### Chính sách quảng cáo Chống phân biệt đối xử của TikTok là gì?

Quảng cáo cá nhân hóa giúp thương hiệu và người dùng kết nối theo những cách phù hợp và hiệu quả hơn. Khi nhà quảng cáo sử dụng các sản phẩm quảng cáo như đối tượng tùy chỉnh, nhắm mục tiêu theo hành vi hoặc sở thích, TikTok yêu cầu họ tuân thủ các chính sách và tiêu chuẩn nhắm mục tiêu để đảm bảo không mang tính phân biệt đối xử:

- TikTok nghiêm cấm nhà quảng cáo sử dụng các sản phẩm quảng cáo để phân biệt đối xử trái pháp luật đối với mọi người. Do đó, nhà quảng cáo không được đưa bất kỳ nội dung phân biệt đối xử hoặc quấy rối trái pháp luật nào vào quảng cáo, cũng như không được khuyến khích các hành vi phân biệt đối xử hoặc quấy rối bất hợp pháp.
- Ngoài ra, nhà quảng cáo không được sử dụng các công cụ lựa chọn đối tượng để:
  1. Nhắm mục tiêu sai trái tới các nhóm người cụ thể vi phạm luật pháp hoặc quy định hiện hành.
  2. Loại trừ sai trái các nhóm người cụ thể khỏi việc xem quảng cáo của họ, gây vi phạm luật pháp hoặc quy định hiện hành.

Xem chi tiết tại [Chính sách quảng cáo chống phân biệt đối xử của TikTok](https://ads.tiktok.com/help/article/tiktok-anti-discrimination-ad-policy).

### Bạn cần làm gì?

Hãy nhắc nhở nhà quảng cáo của bạn truy cập [TikTok Ads Manager](https://ads.tiktok.com/i18n/) để hoàn tất xác nhận tuân thủ Chính sách quảng cáo Chống phân biệt đối xử trước ngày **1 tháng 9 năm 2023**. Nếu áp dụng, họ cũng cần xác nhận tuân thủ các yêu cầu về Nhà ở, Việc làm và Tín dụng (Housing, Employment and Credit - HEC).

Để tra cứu thông tin người dùng của nhà quảng cáo (email, core user ID), sử dụng **/user/info/**.

> [!WARNING]
> Nếu nhà quảng cáo không hoàn tất quy trình chứng nhận tuân thủ trước ngày 01/09/2023, nhà phát triển sẽ không thể thực hiện bất kỳ thao tác nào đối với tài khoản TikTok for Business của họ qua API.

---

## Giới hạn độ tuổi mới đối với quảng cáo trên TikTok (`New age restrictions for ads on TikTok`)
<a id="doc-1788755983247362"></a>
<!-- doc_id: 1788755983247362 -->

> Đường dẫn: Appendix > Advertising Policies > New age restrictions for ads on TikTok

Nhằm giữ an toàn cho cộng đồng, đặc biệt là người dùng dưới 18 tuổi, các hạn chế độ tuổi mới sau đây được áp dụng cho mọi chiến dịch phân phối đến Hoa Kỳ, Châu Mỹ Latinh, Khu vực Kinh tế Châu Âu (EEA), Vương quốc Anh, Thụy Sĩ hoặc Canada:
- Các chiến dịch có mục tiêu Tìm kiếm khách hàng tiềm năng (`LEAD_GENERATION`) chỉ được phép nhắm mục tiêu từ 18 tuổi trở lên.
- Các chiến dịch có mục tiêu Doanh số sản phẩm qua Shop (`PRODUCT_SALES` với nguồn sản phẩm `STORE`) chỉ được phép nhắm mục tiêu từ 18 tuổi trở lên.

Các chiến dịch mới được tạo sử dụng vị trí hiển thị bao gồm TikTok, Pangle hoặc Global App Bundle nhắm đến các khu vực trên sẽ áp dụng các cập nhật:

**Các thay đổi chính:**
- Nhà quảng cáo vẫn có thể tiếp cận người dùng từ 13–17 tuổi nhưng không được kết hợp với các công cụ nhắm mục tiêu cá nhân hóa.
- Được tiếp tục tiếp cận độ tuổi 13–17 qua nhắm mục tiêu vị trí, thiết bị hoặc ngôn ngữ (Đối với thiết bị: không cho phép nhắm theo giá thiết bị. Đối với vị trí: chỉ giới hạn ở quốc gia, DMA, thành phố hoặc bang — không cho phép nhắm theo mã bưu chính / zip code).
- Không được tiếp cận người dùng từ 13–17 tuổi thông qua giới tính, sở thích & hành vi hoặc bất kỳ hình thức nhắm mục tiêu dựa trên cá nhân hóa nào khác.

**Khuyến nghị:**
- Loại bỏ `AGE_13_17` khỏi trường `age_groups` trong các endpoint bị ảnh hưởng.
  > [!NOTE]
  > Nếu bạn thường để trống trường `age_groups` hoặc đặt là `[]`, hãy chỉ định rõ các nhóm tuổi bạn cần, ví dụ: `AGE_18_24`, `AGE_25_34`, `AGE_35_44`, `AGE_45_54`, `AGE_55_100`.
- Tiếp tục tiếp cận nhóm tuổi 13–17 bằng các tùy chọn thiết bị (không kèm giá thiết bị), ngôn ngữ hoặc vị trí (không kèm mã zip).

Nếu bạn không thể điều chỉnh tích hợp của mình, hệ thống cung cấp các biện pháp tương thích:
- Khi tạo nhóm quảng cáo: nếu kích hoạt quy tắc xác thực mới mà không chỉ định thủ công nhóm tuổi, hệ thống sẽ tự động đặt độ tuổi mục tiêu thành 18+ để vượt qua xác thực.
- Khi cập nhật nhóm quảng cáo: trường `exclude_age_under_eighteen` được bổ sung trong [/adgroup/update/](../12-api-reference/07-ad-groups-p3.md#doc-1739586761631745). Bạn có thể đặt `exclude_age_under_eighteen = true` để hệ thống tự động thiết lập mục tiêu tuổi 18+.

### Cho tất cả các mục tiêu (`For all objectives`)

| Tham số / Cài đặt | Cấu hình |
|---|---|
| **Cài đặt chiến dịch** (`Campaign settings`)<br>`objective_type` | `REACH`, `TRAFFIC`, `VIDEO_VIEWS`, `ENGAGEMENT`, `APP_PROMOTION`, `WEB_CONVERSIONS`, `LEAD_GENERATION`, `PRODUCT_SALES` (với `campaign_product_source` là `CATALOG`), `RF_TRAFFIC` |
| **Cài đặt nhóm quảng cáo** (`Ad group settings`)<br>• `placement_type`<br>• `placements` | Một trong các điều kiện:<br>• `placement_type` là `PLACEMENT_TYPE_AUTOMATIC`.<br>• `placement_type` là `PLACEMENT_TYPE_NORMAL` và `placements` chứa `PLACEMENT_TIKTOK`, `PLACEMENT_PANGLE`, hoặc `PLACEMENT_GLOBAL_APP_BUNDLE`. |
| `age_groups` | Trường hợp 1: Chứa `AGE_13_17`<br>Trường hợp 2: Mảng rỗng (`[]`) hoặc không truyền<br>Trường hợp 3: Chứa `AGE_13_17`, mảng rỗng hoặc không truyền |
| `location_ids` | Vị trí mục tiêu bao gồm Hoa Kỳ, Châu Mỹ Latinh, Khu vực Kinh tế Châu Âu, Vương quốc Anh, Thụy Sĩ hoặc Canada. |
| **Cài đặt khác** (`Other settings`) | Bất kỳ tùy chọn nhắm mục tiêu nào nằm ngoài các tùy chọn được hỗ trợ cho người dưới 18 tuổi. |
| **Cho phép tạo nhóm quảng cáo?** | Trường hợp 1: ❌ Không cho phép<br>Trường hợp 2: ✅ Được phép (Hệ thống mặc định gán `age_groups` thành `["AGE_18_24", "AGE_25_34", "AGE_35_44", "AGE_45_54", "AGE_55_100"]`)<br>Trường hợp 3: ❌ Không cho phép |
| **Cho phép cập nhật nhóm quảng cáo?** | ❌ Không cho phép đối với tất cả các trường hợp trên |

### Các tùy chọn nhắm mục tiêu được hỗ trợ cho người dưới 18 tuổi

| Targeting setting | Trường API (`API field`) |
|---|---|
| Demographics - Location | `location_ids`<br>**Lưu ý**: `zipcode_ids` không được hỗ trợ. |
| Demographics - Languages | `languages` |
| Device | `operating_systems`<br>`min_android_version`<br>`min_ios_version`<br>`ios14_targeting`<br>`device_model_ids`<br>`network_types`<br>`carrier_ids`<br>`isp_ids`<br>**Lưu ý**: `device_price_ranges` không được hỗ trợ. |

### Cho mục tiêu Tìm kiếm khách hàng tiềm năng (`For Lead Generation objective`)

| Cài đặt | Cấu hình |
|---|---|
| Cài đặt chiến dịch (`Campaign setting`) | `objective_type = LEAD_GENERATION` |
| Cài đặt nhóm quảng cáo | • `placement_type` là `PLACEMENT_TYPE_AUTOMATIC`, hoặc `PLACEMENT_TYPE_NORMAL` chứa `PLACEMENT_TIKTOK`, `PLACEMENT_PANGLE`, hoặc `PLACEMENT_GLOBAL_APP_BUNDLE`.<br>• `age_groups` chứa `AGE_13_17`.<br>• `location_ids` / `zipcode_ids` nhắm mục tiêu Mỹ, Mỹ Latinh, EEA, UK, Thụy Sĩ hoặc Canada. |
| **Cho phép tạo hoặc cập nhật nhóm quảng cáo?** | ❌ **Không cho phép** |

### Cho mục tiêu Doanh số sản phẩm với `campaign_product_source` là `STORE`

| Cài đặt | Cấu hình |
|---|---|
| Cài đặt chiến dịch (`Campaign setting`) | `objective_type = PRODUCT_SALES`<br>`campaign_product_source = STORE` |
| Cài đặt nhóm quảng cáo | • `placement_type` là `PLACEMENT_TYPE_AUTOMATIC`, hoặc `PLACEMENT_TYPE_NORMAL` chứa `PLACEMENT_TIKTOK`, `PLACEMENT_PANGLE`, hoặc `PLACEMENT_GLOBAL_APP_BUNDLE`.<br>• `age_groups` chứa `AGE_13_17`.<br>• `location_ids` / `zipcode_ids` nhắm mục tiêu Mỹ, Mỹ Latinh, EEA, UK, Thụy Sĩ hoặc Canada. |
| **Cho phép tạo hoặc cập nhật nhóm quảng cáo?** | ❌ **Không cho phép** |

---

## Tính duy nhất của Object ID (`Object ID uniqueness`)
<a id="doc-1792139804568578"></a>
<!-- doc_id: 1792139804568578 -->

> Đường dẫn: Appendix > Object ID uniqueness

Mỗi đối tượng trong hệ thống TikTok API for Business thường được gán một định danh duy nhất (ID). Bảng dưới đây thể hiện phạm vi duy nhất của các trường ID thông dụng:

Để tìm hiểu chi tiết về các khái niệm ID, xem thêm [Khái niệm (Concepts)](../04-get-started/bat-dau.md#doc-1738928364967937).

| ID type | Phạm vi duy nhất (`Scope of Uniqueness`) | Duy nhất toàn cầu? (`Globally Unique?`) |
|---|---|---|
| `app_id` | Toàn cầu (`Global`) | Có (`Yes`) |
| `core_user_id` | Toàn cầu (`Global`) | Có (`Yes`) |
| `advertiser_id` | Toàn cầu (`Global`) | Có (`Yes`) |
| `campaign_id` | Toàn cầu (`Global`) | Có (`Yes`) |
| `adgroup_id` | Toàn cầu (`Global`) | Có (`Yes`) |
| `ad_id` | Toàn cầu (`Global`) | Có (`Yes`) |
| `identity_id` | Toàn cầu (`Global`) | Có (`Yes`) |
| `material_id` | Toàn cầu (`Global`) | Có (`Yes`) |
| `tiktok_item_id` | Toàn cầu (`Global`) | Có (`Yes`) |
| `video_id` | Toàn cầu (`Global`) | Có (`Yes`)<br>**Lưu ý**: Nếu cùng một video được tải lên nhiều lần, các `video_id` khác nhau sẽ được tạo ra, nhưng tất cả các `video_id` này đều tương ứng với cùng một `material_id`. |
| `image_id` | Toàn cầu (`Global`) | Có (`Yes`) |
| `music_id` | Toàn cầu (`Global`) | Có (`Yes`) |
| `file_id` | Toàn cầu (`Global`) | Có (`Yes`) |
| `page_id` | Toàn cầu (`Global`) | Có (`Yes`) |
| `creative_portfolio_id` | Toàn cầu (`Global`) | Có (`Yes`) |
| `card_id` | Toàn cầu (`Global`) | Có (`Yes`) |
| `call_to_action_id` | Toàn cầu (`Global`) | Có (`Yes`) |

---

## Tổ hợp nội dung sáng tạo quảng cáo Upgraded Smart+ theo danh tính và loại quảng cáo (`Upgraded Smart+ ad creative combinations by identity and ad type`)
<a id="doc-1847839781968897"></a>
<!-- doc_id: 1847839781968897 -->

> Đường dẫn: Appendix > Upgraded Smart+ ad creative combinations by identity and ad type

Bảng dưới đây tổng hợp các tổ hợp nội dung sáng tạo quảng cáo khả dụng dựa trên loại danh tính (identity type) và loại quảng cáo (ad type) trong giải pháp Upgraded Smart+:

Để tìm hiểu thêm về Spark Ads, hãy tham khảo [Tạo quảng cáo Spark Ads (Create Spark Ads)](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1739470744631298).

| Loại danh tính (`Identity Type`) | Loại quảng cáo (`Ad Type`) | Tổ hợp sáng tạo khả dụng | Chi tiết yêu cầu | Cấu hình API |
|---|---|---|---|---|
| **Custom User** (`identity_type` trong đối tượng `ad_configuration` là `CUSTOMIZED_USER`) | Quảng cáo không phải Spark Ads (`non-Spark Ads`) | **Chỉ video** (`Videos only creatives`) | • 1 đến 50 video có ảnh bìa<br>• 1 đến 5 văn bản quảng cáo | • Chỉ định 1 đến 50 video (`video_info`) kèm ảnh bìa (`image_info`)<br>• Chỉ định 1 đến 5 văn bản quảng cáo (`ad_text_list`)<br>• Không chỉ định `music_info` và `tiktok_item_id` |
| Custom User | non-Spark Ads | **Chỉ thẻ xoay** (`Carousel only creatives`) | • 1 đến 50 bộ ảnh thẻ xoay (carousel), mỗi bộ gồm từ 1 đến 35 hình ảnh và 1 bản nhạc<br>• 1 đến 5 văn bản quảng cáo | • Chỉ định 1 đến 50 carousel, mỗi carousel tạo từ 1 đến 35 ảnh (`image_info`) và 1 bản nhạc (`music_info`)<br>• Chỉ định 1 đến 5 văn bản quảng cáo (`ad_text_list`)<br>• Không chỉ định `video_info` và `tiktok_item_id` |
| Custom User | non-Spark Ads | **Kết hợp video và thẻ xoay** (`Combination of videos and carousel creatives`) | • Tổ hợp kết hợp tối đa 50 video kèm ảnh bìa và carousel (mỗi carousel gồm 1 đến 35 ảnh và 1 bản nhạc)<br>• 1 đến 5 văn bản quảng cáo | • Chỉ định tổ hợp kết hợp tối đa 50 video (`video_info` + `image_info`) và carousel (`image_info` + `music_info`)<br>• Chỉ định 1 đến 5 văn bản (`ad_text_list`)<br>• Không chỉ định `tiktok_item_id` |
| **TikTok User / TikTok Account User in Business Center** (`identity_type` trong đối tượng `creative_info` là `TT_USER` hoặc `BC_AUTH_TT`) | Spark Ads tạo qua hình thức ĐẨY (`Spark Ads PUSH`) | **Chỉ video** (`Videos only creatives`) | • 1 đến 50 video có ảnh bìa<br>• 1 đến 5 văn bản quảng cáo<br>• (Tùy chọn) Bật "Chỉ hiển thị qua quảng cáo" để giới hạn bài đăng cho lưu lượng trả phí, hoặc tắt để bài đăng xuất hiện trên hồ sơ TikTok và nhận lưu lượng tự nhiên | • Chỉ định 1 đến 50 video (`video_info`) kèm ảnh bìa (`image_info`)<br>• Chỉ định 1 đến 5 văn bản (`ad_text_list`)<br>• Không chỉ định `music_info` và `tiktok_item_id`<br>• Đặt `dark_post_status` thành `ON` để bật "Chỉ hiển thị qua quảng cáo" hoặc `OFF` để tắt |
| TikTok User / BC User | Spark Ads PUSH | **Chỉ thẻ xoay** (`Carousel only creatives`) | • 1 đến 50 carousel (mỗi carousel tạo từ 1 đến 35 ảnh và 1 bản nhạc)<br>• 1 đến 5 văn bản quảng cáo<br>• (Tùy chọn) Bật hoặc tắt thiết lập "Chỉ hiển thị qua quảng cáo" | • Chỉ định 1 đến 50 carousel (`image_info` 1–35 ảnh + `music_info` 1 bản nhạc)<br>• Chỉ định 1 đến 5 văn bản (`ad_text_list`)<br>• Không chỉ định `video_info` và `tiktok_item_id`<br>• Thiết lập `dark_post_status` thành `ON` hoặc `OFF` |
| TikTok User / BC User | Spark Ads PUSH | **Kết hợp video và thẻ xoay** | • Tổ hợp tối đa 50 video kèm ảnh bìa và carousel<br>• 1 đến 5 văn bản quảng cáo<br>• (Tùy chọn) Bật hoặc tắt thiết lập "Chỉ hiển thị qua quảng cáo" | • Chỉ định kết hợp tối đa 50 video (`video_info` + `image_info`) và carousel (`image_info` + `music_info`)<br>• Chỉ định 1 đến 5 văn bản (`ad_text_list`)<br>• Không chỉ định `tiktok_item_id`<br>• Đặt `dark_post_status` thành `ON` hoặc `OFF` |
| **TikTok User / BC User / Authorized User** (`identity_type` trong đối tượng `creative_info` là `TT_USER`, `BC_AUTH_TT`, hoặc `AUTH_CODE`) | Spark Ads tạo qua hình thức KÉO (`Spark Ads PULL`) | **Chỉ bài đăng video** (`Video posts only creatives`) | • 1 đến 50 bài đăng video trên TikTok | • Chỉ định 1 đến 50 bài đăng video TikTok qua `tiktok_item_id`<br>• Không chỉ định `video_info`, `image_info`, `music_info` và `ad_text_list` |
| TikTok User / BC User / Authorized User | Spark Ads PULL | **Chỉ bài đăng ảnh** (`Photo posts only creatives`) | • 1 đến 50 bài đăng hình ảnh trên TikTok | • Chỉ định 1 đến 50 bài đăng hình ảnh TikTok qua `tiktok_item_id`<br>• Không chỉ định `video_info`, `image_info`, `music_info` và `ad_text_list` |
| TikTok User / BC User / Authorized User | Spark Ads PULL | **Kết hợp bài đăng video và ảnh** (`Combination of video and photo post creatives`) | • Tổ hợp kết hợp tối đa 50 bài đăng video và bài đăng ảnh trên TikTok | • Chỉ định tổ hợp lên tới 50 bài đăng video và bài đăng ảnh TikTok qua `tiktok_item_id`<br>• Không chỉ định `video_info`, `image_info`, `music_info` và `ad_text_list` |
