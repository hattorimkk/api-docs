# Hướng dẫn Business Center

TikTok Business Center là trung tâm quản lý tập trung cho phép các tổ chức và agency quản lý hiệu quả và an toàn nhiều tài khoản quảng cáo TikTok, thành viên, đối tác, tài sản và cài đặt tài chính. Tài liệu này hướng dẫn chi tiết các tác vụ vận hành cốt lõi qua API, bao gồm tạo Business Center, phân quyền thành viên/đối tác, quản lý tài sản, xác minh doanh nghiệp, thiết lập tài chính và trích xuất báo cáo.

---

## Business Center (`Business Center`)
<a id="doc-1738864498580481"></a>
<!-- doc_id: 1738864498580481 -->

> Đường dẫn: Marketing API > Business Center

Bạn có thể sử dụng Business Center API để quản lý hiệu quả nhiều tài khoản quảng cáo TikTok, người dùng, tài sản và tài chính. Bạn cũng có thể sử dụng Reporting API để chạy [báo cáo Business Center](bao-cao-p3.md#doc-1775747432712194).
- Để tìm hiểu về các khái niệm, lợi ích và các loại Business Center, xem [Tổng quan](business-center.md#doc-1739562432184322).
- Để tìm hiểu một số trường hợp sử dụng phổ biến đối với thành viên, đối tác, tài sản, cài đặt thanh toán và báo cáo Business Center, xem [Hướng dẫn](business-center.md#doc-1739562439582722):
  - [Tạo Business Center](business-center.md#doc-1754705308039169): Việc tạo TikTok Business Center cho phép bạn quản lý các tài khoản quảng cáo TikTok giữa nhiều người dùng trong môi trường tập trung và bảo mật.
  - [Thành viên và đối tác](business-center.md#doc-1754705315233793): Bạn có thể sử dụng Business Center API để thêm người dùng vào Business Center và gán vai trò quản lý tài sản cho họ.
  - [Tài sản](business-center.md#doc-1754705318594562): Bạn có thể sử dụng Business Center API để quản lý [Tài sản](business-center.md#doc-1754705407307777) hoặc [Nhóm tài sản](business-center.md#doc-1754705410074626) trong Business Center, ví dụ như thêm tài khoản quảng cáo hoặc chuyển giao pixel.
  - [Tài chính](business-center.md#doc-1754705321657346): Bạn có thể sử dụng Business Center API để quản lý thanh toán và hóa đơn trong Business Center. Ví dụ: lấy số dư của Business Center hoặc tài khoản quảng cáo, xem lịch sử giao dịch.
  - [Báo cáo](business-center.md#doc-1775798662604802): Bạn có thể sử dụng Reporting API để lấy thông tin chi tiết về dữ liệu hiệu suất của các tài khoản quảng cáo trong Business Center.
- Để tìm hiểu danh sách các API hiện có để quản lý Business Center, xem [Tài liệu tham khảo API](business-center.md#doc-1739562438061058).

---

## Tổng quan (`Overview`)
<a id="doc-1739562432184322"></a>
<!-- doc_id: 1739562432184322 -->

> Đường dẫn: Marketing API > Business Center > Overview

Business Center là một trung tâm điều phối cho phép các tổ chức và agency quản lý hiệu quả nhiều tài khoản quảng cáo TikTok, người dùng, tài sản và tài chính trong một môi trường bảo mật. Xin lưu ý rằng nhà phát triển hoặc nhà quảng cáo bắt buộc phải sở hữu một Business Center để có thể sử dụng Business Center API. Ngoài ra, người dùng thực hiện ủy quyền ứng dụng nhà phát triển phải có quyền Quản trị viên Business Center (Business Center Admin).

Xem thêm [Giới thiệu về TikTok Business Center](https://ads.tiktok.com/help/article/tiktok-business-center?lang=en) trên Trung tâm trợ giúp doanh nghiệp TikTok để biết thêm chi tiết, bao gồm thời điểm nên dùng Business Center và cách bắt đầu.

### Lợi ích của Business Center (`Benefits of Business Center`)
TikTok Business Center mang lại các lợi thế vượt trội:
- **Nền tảng tất cả trong một để kiểm tra nhiều tài khoản quảng cáo**: Đăng nhập một lần (SSO) để truy cập tất cả các tài khoản quảng cáo được quản lý, giảm thiểu thời gian chuyển đổi giữa các tài khoản.
- **Duy trì toàn quyền kiểm soát truy cập và quản lý tài sản**: Đảm bảo tính bảo mật khi các quyền hạn cốt lõi luôn nằm trong tầm kiểm soát của quản trị viên. Nắm bắt rõ ràng danh sách người có quyền truy cập, đồng thời gán, thay đổi hoặc thu hồi vai trò khi đội ngũ nhân sự thay đổi theo thời gian.
- **Đảm bảo tính minh bạch trong hợp tác**: Trực tiếp biết được ai đã chỉnh sửa hoặc thực hiện các thay đổi đối với tài khoản quảng cáo.
- **Nâng cấp việc ra quyết định cho các chiến dịch tương lai**: Nhận thông tin chi tiết và báo cáo ở cấp độ doanh nghiệp cho hiệu suất quảng cáo trên nhiều tài khoản khác nhau.

### Các loại Business Center (`Business Center types`)
Các loại Business Center bao gồm danh sách dưới đây. Bạn có thể kiểm tra loại Business Center của mình thông qua trường `type` trả về từ endpoint [/bc/get/](../12-api-reference/12-bc-management.md#doc-1737115687501826):
- Business Center thông thường: `NORMAL`
- Business Center trực tiếp không tự phục vụ: `DIRECT`
- Agency Business Center không tự phục vụ: `AGENCY`
- Business Center trực tiếp tự phục vụ: `SELF_SERVICE`
- Agency Business Center tự phục vụ: `SELF_SERVICE_AGENCY`

---

## Hướng dẫn (`Guides`)
<a id="doc-1739562439582722"></a>
<!-- doc_id: 1739562439582722 -->

> Đường dẫn: Marketing API > Business Center > Guides

Bộ hướng dẫn này sẽ dẫn dắt bạn qua các khía cạnh: tạo Business Center, quản lý thành viên và đối tác, cài đặt thanh toán, quản lý tài sản và báo cáo dữ liệu Business Center.

- [Tạo Business Center](business-center.md#doc-1754705308039169): Cho phép quản lý tài khoản quảng cáo TikTok giữa nhiều người dùng trong môi trường bảo mật và tập trung.
- [Thành viên và đối tác](business-center.md#doc-1754705315233793): Sử dụng Business Center API để thêm nhân sự vào Business Center và gán vai trò quản lý tài sản.
- [Tài sản](business-center.md#doc-1754705318594562): Quản lý [Tài sản](business-center.md#doc-1754705407307777) hoặc [Nhóm tài sản](business-center.md#doc-1754705410074626) trong Business Center, chẳng hạn như thêm tài khoản quảng cáo hoặc chuyển quyền pixel.
- [Tài chính](business-center.md#doc-1754705321657346): Quản lý thanh toán và hóa đơn trong Business Center, bao gồm kiểm tra số dư và xem bản ghi giao dịch.
- [Báo cáo](business-center.md#doc-1775798662604802): Sử dụng Reporting API để lấy thông tin phân tích chuyên sâu cho các tài khoản quảng cáo trong Business Center.

---

## Tạo Business Center (`BC creation`)
<a id="doc-1754705308039169"></a>
<!-- doc_id: 1754705308039169 -->

> Đường dẫn: Marketing API > Business Center > Guides > BC creation

Việc tạo TikTok Business Center sẽ cho phép bạn quản lý các tài khoản quảng cáo TikTok giữa nhiều người dùng trong một môi trường an toàn và tập trung. Hãy xem [Cách tạo TikTok Business Center](https://ads.tiktok.com/help/article/create-tiktok-business-center?lang=en) trên Trung tâm trợ giúp TikTok for Business để biết các bước chi tiết.

Nếu bạn muốn lấy danh sách các Business Center mà bạn có quyền truy cập, hãy sử dụng [/bc/get/](../12-api-reference/12-bc-management.md#doc-1737115687501826).

---

## Thành viên và đối tác (`Members and partners`)
<a id="doc-1754705315233793"></a>
<!-- doc_id: 1754705315233793 -->

> Đường dẫn: Marketing API > Business Center > Guides > Members and partners

Bạn (**Người dùng Quản trị viên của Business Center**) có thể sử dụng Business Center API để thêm người dùng vào Business Center và gán vai trò quản lý tài sản cho họ.

### Về các vai trò (`About roles`)
Các vai trò cơ bản (`user_role`) trong Business Center bao gồm Admin (Quản trị viên) và Standard (Tiêu chuẩn):
- **Admin**: Có thể quản lý toàn bộ thành viên và tài sản của Business Center.
- **Standard**: Chỉ có thể làm việc trên các tài khoản quảng cáo mà họ được phân công.

Các vai trò tài chính (`finance_role`) trong Business Center bao gồm Finance Analyst (Chuyên viên phân tích tài chính) và Finance Manager (Quản lý tài chính):
- **Finance Analyst**: Có thể xem, xuất và tải xuống bản ghi giao dịch thanh toán cho tất cả các tài khoản quảng cáo do Business Center sở hữu hoặc tạo ra.
- **Finance Manager**: Có đầy đủ quyền hạn của Finance Analyst, đồng thời sở hữu chuỗi quyền chỉnh sửa: thực hiện thanh toán, nạp tiền vào tài khoản quảng cáo và sửa đổi thông tin liên hệ lập hóa đơn cho tất cả các tài khoản quảng cáo thuộc quyền sở hữu hoặc do Business Center tạo ra.

Xem [Vai trò trong Business Center](https://ads.tiktok.com/help/article/add-users-tiktok-business-center?lang=en#anchor-0:~:text=manage%20specific%20assets.-,Business%20Center%20Roles,-Roles%20specific%20to) trên Trung tâm trợ giúp TikTok Ads Manager để biết thêm chi tiết.

### Thêm thành viên vào Business Center (`Add members to your Business Center`)
Sau khi tạo tài khoản quảng cáo cho khách hàng, bạn có thể mời các thành viên trong đội ngũ vào Business Center và gán quyền cho họ.

Sử dụng endpoint [/bc/member/invite/](../12-api-reference/19-bc-members.md#doc-1739939455765505) để mời thành viên và phân quyền thông qua trường `user_role` hoặc `finance_role`.

### Thêm đối tác vào Business Center (`Add partners to your Business Center`)
Đối tác (Partner) thường là một doanh nghiệp khác mà bạn hợp tác chặt chẽ để cùng quản lý và xây dựng các chiến dịch quảng cáo TikTok. Xem [Giới thiệu về đối tác TikTok Business Center](https://ads.tiktok.com/help/article/tiktok-business-center-partners?lang=en) trên Trung tâm trợ giúp để tìm hiểu thêm.

Sử dụng endpoint [/bc/partner/add/](../12-api-reference/18-bc-partners.md#doc-1739662756510721) để thêm đối tác vào Business Center. Để gán quyền cho đối tác, sử dụng các trường `advertiser_role` hoặc `catalog_role`.

### Các endpoint liên quan (`Related endpoints`)
Xem [Tài liệu tham khảo API](business-center.md#doc-1739562438061058) để tra cứu các endpoint khả dụng dành cho **thành viên (members)** và **đối tác (partners)** của Business Center.

---

## Tài sản (`Assets`)
<a id="doc-1754705318594562"></a>
<!-- doc_id: 1754705318594562 -->

> Đường dẫn: Marketing API > Business Center > Guides > Assets

Bạn có thể sử dụng Business Center API để quản lý tài sản hoặc Nhóm tài sản (Asset Groups) trong Business Center:
- [Tài sản](business-center.md#doc-1754705407307777): Bao gồm tài khoản quảng cáo, danh mục sản phẩm, pixel, khách hàng tiềm năng (leads), tài khoản TikTok và cửa hàng (stores).
- [Nhóm tài sản](business-center.md#doc-1754705410074626): Là một tập hợp các tài sản được gom nhóm lại trong Business Center để phân quyền hàng loạt.

---

## Quản lý tài sản (`Assets`)
<a id="doc-1754705407307777"></a>
<!-- doc_id: 1754705407307777 -->

> Đường dẫn: Marketing API > Business Center > Guides > Assets > Assets

Bạn (**Người dùng Quản trị viên của Business Center**) có thể sử dụng Business Center API để quản lý các tài sản bao gồm tài khoản quảng cáo, danh mục sản phẩm, pixel, khách hàng tiềm năng, tài khoản TikTok và cửa hàng. Dưới đây là các trường hợp sử dụng phổ biến:

### Tạo tài khoản quảng cáo (`Create an ad account`)

Quản trị viên của Agency hoặc Direct Business Center có thể tạo cả hai loại tài khoản quảng cáo: đấu giá (auction) và đặt trước (reservation) thông qua endpoint [/bc/advertiser/create/](../12-api-reference/15-bc-assets.md#doc-1739939020318721).

> [!IMPORTANT]
> Kể từ ngày 26 tháng 9 năm 2024, để đảm bảo an toàn cho tài khoản quảng cáo, chúng tôi đã triển khai quy trình xác minh UnionPay đối với việc tạo tài khoản quảng cáo trong Business Center qua [/bc/advertiser/create/](../12-api-reference/15-bc-assets.md#doc-1739939020318721) cho các nhà quảng cáo đăng ký tại Trung Quốc đại lục.

> [!NOTE]
> Việc tạo tài khoản quảng cáo đặt trước (reservation ad accounts) chỉ khả dụng cho tài khoản Agency Business Center và hiện là tính năng chỉ dành cho danh sách cho phép (allowlist-only). Nếu bạn muốn truy cập tính năng này, vui lòng liên hệ với đại diện TikTok của bạn.

#### Đối với nhà quảng cáo tại Trung Quốc đại lục (`For advertisers in the Chinese Mainland`)
Nếu tài khoản quảng cáo được đăng ký tại Trung Quốc đại lục, bạn có thể sử dụng giấy phép kinh doanh mới hoặc tái sử dụng giấy phép kinh doanh đã được xác minh trước đó.

**Lựa chọn A: Sử dụng giấy phép kinh doanh mới (Using a new business license)**
1. Tải lên hình ảnh giấy phép kinh doanh bằng [/bc/image/upload/](../12-api-reference/15-bc-assets.md#doc-1739938996913218). Phản hồi sẽ bao gồm `image_id` cho từng giấy phép.
2. Kiểm tra yêu cầu xác minh UnionPay cho giấy phép kinh doanh bằng [/bc/advertiser/unionpay_info/check/](../12-api-reference/15-bc-assets.md#doc-1813772238056449):
   - Nếu `unionpay_verification_required` trả về là `false`, tạo tài khoản quảng cáo bằng [/bc/advertiser/create/](../12-api-reference/15-bc-assets.md#doc-1739939020318721) và truyền giá trị `image_id` vào trường `license_image_id`.
   - Nếu `unionpay_verification_required` trả về là `true`, thực hiện các bước sau:
     1. Tạo tài khoản quảng cáo bằng [/bc/advertiser/create/](../12-api-reference/15-bc-assets.md#doc-1739939020318721) với cùng `license_no` và `license_image_id`.
     2. Gửi xác minh UnionPay bằng [/bc/advertiser/unionpay_info/submit/](../12-api-reference/15-bc-assets.md#doc-1813772274039809).
     3. Đợi khoảng 20 giây, sau đó sử dụng [/advertiser/info/](../12-api-reference/03-ad-accounts.md#doc-1739593083610113) để xác nhận `status` của tài khoản quảng cáo.
     4. Nếu tài khoản bị từ chối do xác minh UnionPay thất bại: tải lên lại hình ảnh giấy phép mới, cập nhật lại thông tin qua [/advertiser/update/](../12-api-reference/15-bc-assets.md#doc-1739939050770434), rồi gửi lại xác minh UnionPay.

> [!NOTE]
> Nếu bạn gửi xác minh UnionPay nhiều lần trong khi tài khoản quảng cáo đang được xét duyệt, chỉ lần gửi đầu tiên được chấp nhận. Các lần gửi tiếp theo sẽ bị bỏ qua.

##### Lý do từ chối khi xác minh UnionPay thất bại (`Rejection reasons for UnionPay verification failures`)

Bảng dưới đây nêu rõ các lý do từ chối chi tiết và hướng dẫn giải quyết khi bạn gửi lại xác minh UnionPay:

| Rejection reason | How to fix |
|---|---|
| "Your UnionPay verification failed <b>because your name and ID number do not match</b>." | Chỉ định chính xác tên tiếng Trung và số CMND/CCCD của người đại diện pháp luật qua `representative_name` và `representative_id` |
| "Your UnionPay verification failed <b>due to invalid ID number</b>." | Chỉ định số CMND/CCCD chính xác qua `representative_id` |
| "Your UnionPay verification failed <b>because your name does not match the info provided when opening your bank account</b>." | Chỉ định tên tiếng Trung chính xác của người đại diện pháp luật khớp với tài khoản ngân hàng (`unionpay_account`) qua `representative_name` |
| "Your UnionPay verification failed <b>due to invalid phone number</b>." | Chỉ định số điện thoại chính xác qua `representative_phone_number` |
| "Your UnionPay verification failed <b>because your legal representative name does not match the name on your document</b>." | Chỉ định tên tiếng Trung chính xác của người đại diện pháp luật khớp với tên trên giấy phép kinh doanh qua `representative_name` |

**Lựa chọn B: Tái sử dụng giấy phép kinh doanh đã xác minh (Reuse a verified business license)**
1. Lấy danh sách các chứng chỉ đã được xác minh trong Business Center bằng [/bc/advertiser/qualification/get/](../12-api-reference/15-bc-assets.md#doc-1770118680584194) với `filtering={"verified": true}`.
2. Gọi [/bc/advertiser/create/](../12-api-reference/15-bc-assets.md#doc-1739939020318721) và truyền `qualification_id` nhận được vào yêu cầu.

#### Đối với nhà quảng cáo ngoài Trung Quốc đại lục (`For advertisers outside the Chinese Mainland`)
1. Tải lên hình ảnh chứng nhận doanh nghiệp bằng [/bc/image/upload/](../12-api-reference/15-bc-assets.md#doc-1739938996913218) để nhận `image_id`.
2. Tạo tài khoản quảng cáo bằng [/bc/advertiser/create/](../12-api-reference/15-bc-assets.md#doc-1739939020318721) với `license_image_id`.

### Quản lý pixel trong Business Center (`Manage pixels`)
Quản trị viên có thể chuyển giao pixel giữa tài khoản quảng cáo và Business Center:
- Chuyển quyền sở hữu pixel từ tài khoản quảng cáo sang Business Center: [/bc/pixel/transfer/](../12-api-reference/15-bc-assets.md#doc-1753994928261122).
- Chia sẻ pixel cho các tài khoản quảng cáo khác: [/bc/pixel/link/](../12-api-reference/15-bc-assets.md#doc-1753994950327297).
- Hủy liên kết pixel: [/bc/pixel/unlink/](../12-api-reference/15-bc-assets.md#doc-1753994950327297).
- Xem danh sách tài khoản quảng cáo liên kết với pixel: [/bc/pixel/advertiser/get/](../12-api-reference/15-bc-assets.md#doc-1753994966965249).

---

## Tài khoản tổ chức (`Organization Account`)
<a id="doc-1855026897423361"></a>
<!-- doc_id: 1855026897423361 -->

> Đường dẫn: Marketing API > Business Center > Guides > Assets > Assets > Organization Account

Tài liệu này giải thích khái niệm Tài khoản tổ chức (Organization Account), lợi ích và cách tích hợp vào quy trình làm việc của bạn.

### Giới thiệu về Tài khoản tổ chức (`About Organization Accounts`)
Tài khoản tổ chức là một danh tính TikTok thống nhất đại diện cho doanh nghiệp hoặc tổ chức trên TikTok. Nó cho phép các tổ chức tập trung hóa sự hiện diện thương hiệu, quản lý quyền hạn truy cập của nhân viên một cách an toàn và tinh giản việc phân phối quảng cáo trên nhiều tài khoản quảng cáo thuộc Business Center.

### Lợi ích cốt lõi (`Benefits`)
- **Tập trung hóa quyền sở hữu**: Giúp tài sản thương hiệu thuộc quyền sở hữu của tổ chức thay vì gắn liền với tài khoản cá nhân của từng nhân viên.
- **Phân phối quảng cáo linh hoạt**: Cho phép liên kết một Tài khoản tổ chức với nhiều tài khoản quảng cáo khác nhau trong Business Center để thực thi quảng cáo Spark Ads hoặc quảng cáo nhận diện thương hiệu.
- **Quản lý quyền hạn an toàn**: Dễ dàng phân bổ hoặc thu hồi quyền truy cập của thành viên mà không làm gián đoạn các chiến dịch đang chạy.

### Tạo Tài khoản tổ chức (`Create an Organization Account`)
1. **Tải lên chứng nhận doanh nghiệp**: Gọi [/bc/image/upload/](../12-api-reference/15-bc-assets.md#doc-1739938996913218) để tải lên tài liệu xác minh doanh nghiệp và lấy `image_id`.
2. **Lấy mã chứng nhận đã xác minh**: Gọi [/bc/advertiser/qualification/get/](../12-api-reference/15-bc-assets.md#doc-1770118680584194) với `filtering={"verified": true}` để nhận `qualification_id`.
3. **Tạo Organization Account**: Gọi [/bc/oa/create/](../12-api-reference/15-bc-assets.md#doc-1855027199571138), đưa `qualification_id` vào yêu cầu để liên kết tài khoản mới với chứng nhận hợp lệ.

### Quản lý Tài khoản tổ chức trong Business Center (`Manage Organization Accounts`)

| Tình huống sử dụng | Endpoint sử dụng | Ghi chú |
|---|---|---|
| Lấy danh sách Organization Account trong Business Center | [/bc/asset/get/](../12-api-reference/15-bc-assets.md#doc-1739432717798401) hoặc [/bc/asset/admin/get/](../12-api-reference/15-bc-assets.md#doc-1739433007779841) | Đặt `asset_type` thành một trong các giá trị: `TT_ACCOUNT` (chạy quảng cáo từ các tài khoản này) hoặc `MANAGED_BUSINESS_ACCOUNT` (chạy quảng cáo và quản lý tin nhắn, khách hàng tiềm năng, bình luận, liên kết sản phẩm và thông tin chi tiết). |
| Gán Organization Account cho thành viên | [/bc/asset/assign/](../12-api-reference/15-bc-assets.md#doc-1739438211077121) | Cấp quyền cho thành viên quản lý tài khoản. |
| Thu hồi quyền truy cập của thành viên | [/bc/asset/unassign/](../12-api-reference/15-bc-assets.md#doc-1739448126749698) | Xóa quyền của thành viên đối với tài khoản tổ chức. |

### Tích hợp Organization Account vào luồng phân phối quảng cáo (`Integrate into ad workflows`)

| Tình huống sử dụng | Chi tiết | Endpoint sử dụng | Ghi chú |
|---|---|---|---|
| Liên kết Organization Account với tài khoản quảng cáo | Khi hoàn tất liên kết, các thành viên Business Center có quyền truy cập vào tài khoản quảng cáo được liên kết có thể sử dụng Organization Account để phân phối quảng cáo. | [/bc/asset/advertiser/assign/](../12-api-reference/15-bc-assets.md#doc-1846868953025538) | Đặt `asset_type` thành `TT_ACCOUNT` hoặc `MANAGED_BUSINESS_ACCOUNT`. |
| Hủy liên kết Organization Account khỏi tài khoản quảng cáo | Sau khi hủy liên kết, các thành viên không còn có thể sử dụng Organization Account này để chạy quảng cáo từ tài khoản quảng cáo đó nữa. | [/bc/asset/advertiser/unassign/](../12-api-reference/15-bc-assets.md#doc-1855027260369921) | |
| Kiểm tra các tài khoản quảng cáo được liên kết | Truy vấn danh sách các tài khoản quảng cáo đang được liên kết với một Organization Account cụ thể. | [/bc/asset/advertiser/assigned/](../12-api-reference/15-bc-assets.md#doc-1855027294743554) | |

---

## Xác minh tài khoản Business Center hoặc tài khoản quảng cáo (`Verify your Business Center account or ad account on TikTok`)
<a id="doc-1870688178806290"></a>
<!-- doc_id: 1870688178806290 -->

> Đường dẫn: Marketing API > Business Center > Guides > Assets > Assets > Verify your Business Center account or ad account on TikTok

Khi tạo Business Center hoặc tài khoản quảng cáo trên TikTok, bạn sẽ được yêu cầu xác minh thông tin doanh nghiệp. Quá trình này giúp đảm bảo một hệ sinh thái an toàn bằng cách xác thực danh tính của tất cả các nhà quảng cáo và doanh nghiệp hoạt động trên nền tảng.

Bạn có thể hoàn tất việc xác minh Business Center hoặc tài khoản quảng cáo bằng lập trình thông qua API theo các bước dưới đây:

### Các bước thực hiện (`Steps`)

1. **Kiểm tra trạng thái xác minh hiện tại của doanh nghiệp**:
   Gọi [/account/verification/status/](../12-api-reference/72-verification.md#doc-1870687815670786) và truyền `bc_id` hoặc `advertiser_id` để lấy trạng thái xác minh `verification_status`. Nếu trạng thái trả về là `NOT_SUBMITTED`, `FAILED` hoặc `EXPIRED`, hãy xem lý do từ chối (`rejection_reason`) và chuyển sang bước 2.

2. **Kiểm tra các loại giấy tờ xác minh khả dụng**:
   Gọi [/account/verification/filetype/](../12-api-reference/72-verification.md#doc-1870687810081794) để lấy danh sách các loại giấy tờ xác minh danh tính doanh nghiệp hoặc cá nhân được hỗ trợ cho quốc gia hoặc khu vực cụ thể của bạn. Ghi lại mã loại tệp (`file_type_code`).

3. **Tải lên tài liệu xác minh**:
   Gọi [/account/verification/upload/](../12-api-reference/72-verification.md#doc-1870687812502530) để tải lên tối đa 2 tài liệu xác minh. Lưu lại các ID hình ảnh chứng nhận (`qualification_image_ids`) được trả về.

4. **Gửi yêu cầu xác minh**:
   Gọi [/account/verification/submit/](../12-api-reference/72-verification.md#doc-1870687936881281) và cung cấp `business_form` (đối với xác minh doanh nghiệp) hoặc `individual_form` (đối với xác minh danh tính cá nhân). Đồng thời đưa vào `file_type_code` từ bước 2 và `qualification_image_ids` từ bước 3.

5. **Kiểm tra lại trạng thái xác minh đã cập nhật**:
   Gọi lại [/account/verification/status/](../12-api-reference/72-verification.md#doc-1870687815670786) với `bc_id` hoặc `advertiser_id` để kiểm tra trạng thái mới. Nếu vẫn chưa đạt yêu cầu, kiểm tra lý do và tải lên tài liệu đã sửa đổi.


---

## Nhóm tài sản (`Asset Groups`)
<a id="doc-1754705410074626"></a>
<!-- doc_id: 1754705410074626 -->

> Đường dẫn: Marketing API > Business Center > Guides > Assets > Asset Groups

Bạn (**Người dùng Quản trị viên của Agency Business Center**) có thể sử dụng Business Center API để quản lý Nhóm tài sản (Asset Groups).

Nhóm tài sản là một tập hợp các tài sản (ví dụ: các tài khoản nhà quảng cáo) trong Business Center. Bạn có thể thêm nhiều tài khoản nhà quảng cáo vào một Nhóm tài sản duy nhất và phân quyền truy cập Nhóm tài sản cho các thành viên cụ thể trong cùng một lần thao tác. Để biết chi tiết, xem [Giới thiệu về Nhóm tài sản](https://ads.tiktok.com/help/article?aid=10001796&q=asset%20group) trên Trung tâm trợ giúp doanh nghiệp TikTok.

### Lợi ích của Nhóm tài sản (`Benefits`)
- **Tổ chức tài sản hàng loạt**: Bạn có thể tạo các Nhóm tài sản theo thương hiệu, khu vực địa lý, nhóm phụ trách agency, v.v. Sau khi tạo, bạn có thể nhanh chóng cấp quyền truy cập Nhóm tài sản cho thành viên, điều này đồng thời cấp quyền cho họ trên toàn bộ tài sản thuộc Nhóm tài sản đó. Ví dụ: nếu bạn đại diện khách hàng quản lý 10 tài khoản nhà quảng cáo, bạn có thể đưa tất cả 10 tài khoản này vào một Nhóm tài sản và phân quyền cho nhân viên một lần duy nhất.
- **Tự động phân quyền cho thành viên**: Khi bạn bổ sung tài sản mới vào Nhóm tài sản, các thành viên trong nhóm này sẽ tự động nhận được quyền truy cập vào tài sản mới tương ứng với vai trò đã được thiết lập. Bạn không cần phải phân quyền thủ công cho từng người nữa.

> [!NOTE]
> • Hiện tại, Asset Group API chỉ hỗ trợ tài sản là tài khoản nhà quảng cáo (`asset_type` = `ADVERTISER`).<br>
> • Chỉ Quản trị viên (`user_role` = `ADMIN`) của Business Center mới có quyền tạo Nhóm tài sản và thêm tài sản vào nhóm. Thành viên tiêu chuẩn chỉ có thể xem các Nhóm tài sản mà họ là thành viên.

### Tạo và quản lý Nhóm tài sản (`Create and manage Asset Groups`)
- Sử dụng endpoint [/bc/asset_group/create/](../12-api-reference/16-bc-asset-groups.md#doc-1749001658583105) để tạo Nhóm tài sản và thiết lập quyền hạn thành viên thông qua `asset_roles`.
- Cập nhật tài sản, thành viên hoặc đổi tên Nhóm tài sản qua [/bc/asset_group/update/](../12-api-reference/16-bc-asset-groups.md#doc-1749001662156801).
- Lấy danh sách tất cả các Nhóm tài sản trong Business Center bằng [/bc/asset_group/list/](../12-api-reference/16-bc-asset-groups.md#doc-1749001665910786).
- Lấy thông tin chi tiết về tài sản hoặc thành viên của một Nhóm tài sản qua [/bc/asset_group/get/](../12-api-reference/16-bc-asset-groups.md#doc-1749001669670913).
- Xóa quyền truy cập của thành viên khỏi Nhóm tài sản hoặc xóa Nhóm tài sản bằng [/bc/asset_group/delete/](../12-api-reference/16-bc-asset-groups.md#doc-1749001673406466).

### Các endpoint liên quan (`Related endpoints`)
Xem [Tài liệu tham khảo API](business-center.md#doc-1739562438061058) để tìm hiểu các endpoint hiện có cho **Nhóm tài sản (Asset Groups)** của Business Center.

---

## Tài chính (`Finance`)
<a id="doc-1754705321657346"></a>
<!-- doc_id: 1754705321657346 -->

> Đường dẫn: Marketing API > Business Center > Guides > Finance

Bạn (**Người dùng có quyền Quản lý tài chính - Finance Manager hoặc Chuyên viên phân tích tài chính - Finance Analyst**) có thể sử dụng Business Center API để quản lý các khoản thanh toán và hóa đơn trong Business Center. Cả Agency Business Center và Direct Business Center đều có khả năng thực hiện các hoạt động liên quan đến tài chính.

> [!NOTE]
> Chỉ người dùng có quyền Finance Manager hoặc Finance Analyst mới có thể quản lý các khoản thanh toán và hóa đơn trong Business Center.

### Xem bản ghi giao dịch tài khoản quảng cáo hoặc Business Center (`View transaction records`)

Để trích xuất các bản ghi giao dịch của một Business Center hoặc các tài khoản quảng cáo mà bạn có quyền truy cập, bạn có hai lựa chọn:
- Sử dụng một endpoint duy nhất: **/bc/account/transaction/get/**.
- Sử dụng hai endpoint riêng biệt: [/advertiser/transaction/get/](../12-api-reference/13-bc-payments.md#doc-1739939116353538) cho tài khoản quảng cáo và [/bc/transaction/get/](../12-api-reference/13-bc-payments.md#doc-1739939140408322) cho Business Center.

Khi sử dụng các endpoint `/advertiser/transaction/get/` và `/bc/transaction/get/`, bạn có thể lọc bản ghi theo loại nguồn tiền bằng tham số `funds_type`:
- `FUNDS_TYPE_CASH`: Đại diện cho tiền mặt.
- `FUNDS_TYPE_GRANT`: Đại diện cho phiếu giảm giá (coupons) hoặc chứng từ tín dụng (vouchers).

### Sử dụng Nhóm thanh toán để quản lý hóa đơn hoặc thanh toán (`Use Billing Groups`)

Nhóm lập hóa đơn (Billing Group) là một tập hợp các tài khoản quảng cáo chia sẻ cùng một cài đặt lập hóa đơn và thanh toán. Sau khi bạn tạo Billing Group, bạn sẽ nhận được một hóa đơn hàng tháng duy nhất cho tất cả các tài khoản quảng cáo trong nhóm đó, hiển thị số tiền đã chi tiêu cho từng tài khoản.

Sử dụng endpoint [/bc/billing_group/create/](../12-api-reference/17-bc-billing-groups.md#doc-1738947780033537) để tạo Billing Group:
- Nếu bạn muốn tạo Billing Group cho các tài khoản quảng cáo Đấu giá (Auction), bạn nên thêm tất cả các tài khoản quảng cáo Đấu giá vào một Billing Group duy nhất (ngoại trừ các tài khoản đăng ký tại Pháp, Brazil hoặc Mexico).
- Nếu bạn muốn tạo Billing Group cho các tài khoản quảng cáo Đặt trước (Reservation), bạn nên thêm từng tài khoản quảng cáo Đặt trước vào một Billing Group riêng biệt.

### Chia sẻ số dư (`Balance Sharing`)

Chia sẻ số dư (Balance Sharing), còn được gọi là phân bổ số dư tự động, cho phép tự động phân bổ chi phí chiến dịch từ số dư tín dụng chung của Business Center giữa các tài khoản quảng cáo thuộc quyền sở hữu của Business Center. Khi bật tính năng này, hệ thống sẽ tự động trừ chi tiêu trực tiếp từ hạn mức tín dụng chung, giúp bạn không cần phải nạp tiền thủ công vào từng tài khoản quảng cáo riêng rẽ.

---

## Quản lý phân bổ số dư của Business Center (`Manage the balance allocation of Business Centers`)
<a id="doc-1781992772171778"></a>
<!-- doc_id: 1781992772171778 -->

> Đường dẫn: Marketing API > Business Center > Guides > Finance > Manage the balance allocation of Business Centers

Bài viết này hướng dẫn chi tiết các bước quản lý việc phân bổ số dư của các Business Center đã bật tính năng Chia sẻ số dư (Balance Sharing).

### Kiểm tra trạng thái và chế độ ngân sách (`Check balance sharing and budget mode`)

Bạn có thể gọi endpoint [/bc/account/budget/get/](../12-api-reference/13-bc-payments.md#doc-1830173979548674) để kiểm tra xem tài khoản quảng cáo đã bật Chia sẻ số dư hay chưa, cũng như kiểm tra chế độ ngân sách hiện tại (`budget_mode`) và ngân sách đã phân bổ (`budget`).

Các chế độ ngân sách khả dụng:
- `INFINITE`: Không giới hạn ngân sách.
- `MONTHLY_BUDGET`: Ngân sách hàng tháng.
- `DAILY_BUDGET`: Ngân sách hàng ngày.
- `CUSTOM_BUDGET`: Ngân sách tùy chỉnh theo khoảng thời gian.

### Cập nhật phân bổ ngân sách (`Update budget allocation`)

Bạn có thể cập nhật chế độ ngân sách hoặc giá trị ngân sách cho tài khoản quảng cáo thông qua endpoint [/bc/account/budget/update/](../12-api-reference/13-bc-payments.md#doc-1830173979548674).

Khi thực hiện cập nhật ngân sách, bạn phải tuân thủ các quy tắc giới hạn số tiền ngân sách dưới đây:

| Change status of budget mode | Restrictions on budget amount |
|---|---|
| Stay in the same budget mode | Giá trị `budget` phải không thấp hơn 105% mức chi tiêu lũy kế trong chế độ ngân sách hiện tại. |
| Switch budget mode | • Chuyển sang `MONTHLY_BUDGET`: `budget` không được thấp hơn 105% mức chi tiêu của tháng hiện tại.<br>• Chuyển sang `DAILY_BUDGET`: `budget` không được thấp hơn 105% mức chi tiêu của ngày hiện tại.<br>• Chuyển sang `CUSTOM_BUDGET`: `budget` không được thấp hơn 105% mức chi tiêu của ngày hiện tại hoặc ngày hôm trước (tùy thuộc vào ngày nào có tiêu dùng thực tế). |

---

## Quản lý danh mục thanh toán (`Manage Payment Portfolios`)
<a id="doc-1839157972427970"></a>
<!-- doc_id: 1839157972427970 -->

> Đường dẫn: Marketing API > Business Center > Guides > Finance > Manage Payment Portfolios

Danh mục thanh toán (Payment Portfolio) là một cơ chế quản trị tài chính nâng cao giúp các Business Center lớn kiểm soát và phân bổ hạn mức tín dụng cho các bộ phận hoặc khách hàng khác nhau.

Sử dụng bộ Payment Portfolios API để:
- **Lấy danh sách Danh mục thanh toán**: Gọi [/bc/payment_portfolio/get/](../12-api-reference/14-bc-payment-portfolios.md#doc-1839151931301954) để truy vấn thông tin chi tiết.
- **Tạo Danh mục thanh toán mới**: Gọi [/bc/payment_portfolio/create/](../12-api-reference/14-bc-payment-portfolios.md#doc-1839151986039809) để thiết lập hạn mức tín dụng và tiền tệ.
- **Liên kết tài khoản quảng cáo với Danh mục thanh toán**: Sử dụng [/bc/payment_portfolio/advertiser/bind/](../12-api-reference/14-bc-payment-portfolios.md#doc-1839151992566081) để đưa các tài khoản quảng cáo vào danh mục.
- **Phân bổ hạn mức tín dụng**: Gọi [/bc/payment_portfolio/quota/allocate/](../12-api-reference/14-bc-payment-portfolios.md#doc-1839151998450754) để điều chỉnh hạn mức tín dụng khả dụng cho từng danh mục thanh toán.
- **Kiểm tra tài khoản quảng cáo và người dùng được ủy quyền**: Tra cứu qua [/bc/payment_portfolio/advertiser/get/](../12-api-reference/14-bc-payment-portfolios.md#doc-1839152005599234) và [/bc/payment_portfolio/user/get/](../12-api-reference/14-bc-payment-portfolios.md#doc-1839152031645121).

---

## Báo cáo (`Reporting`)
<a id="doc-1775798662604802"></a>
<!-- doc_id: 1775798662604802 -->

> Đường dẫn: Marketing API > Business Center > Guides > Reporting

Phân tích chi phí và hiệu suất của các tài khoản quảng cáo trong Business Center mang lại khả năng quản trị tập trung và an toàn cho nhiều người dùng. Với tính năng báo cáo của Business Center, bạn có thể tính toán chi phí thanh toán cho nhiều tài khoản quảng cáo một cách hiệu quả và thu thập thông tin chi tiết để đánh giá mức độ hiệu quả của quảng cáo.

Sử dụng endpoint [/report/integrated/get/](../12-api-reference/58-reporting.md#doc-1740302848100353) để chạy các báo cáo hiệu suất đồng bộ và tra cứu tiền tệ cùng khu vực đăng ký của các tài khoản quảng cáo bằng [Get currencies and registration areas for ad accounts](../12-api-reference/21-bc-reporting.md#doc-1775752357139457).

---

## Câu hỏi thường gặp (`FAQs`)
<a id="doc-1739562436183041"></a>
<!-- doc_id: 1739562436183041 -->

> Đường dẫn: Marketing API > Business Center > Guides > FAQs

### Quản trị Business Center (`BC Administration`)

**Tôi có thể sử dụng cùng một giấy phép kinh doanh để tạo nhiều Business Center không?**
Có. Một pháp nhân kinh doanh có thể tạo nhiều Business Center tùy thuộc vào cấu trúc tổ chức và nhu cầu vận hành của doanh nghiệp.

**Tôi có thể xóa một Business Center đã tạo không?**
Hiện tại, hệ thống không hỗ trợ xóa trực tiếp Business Center qua API hoặc giao diện người dùng. Nếu bạn không còn sử dụng một Business Center, hãy hủy liên kết các tài sản và xóa thành viên khỏi trung tâm đó.

**Làm thế nào để chuyển đổi quyền sở hữu tài sản giữa các Business Center?**
Bạn có thể hủy liên kết tài sản khỏi Business Center hiện tại và gửi yêu cầu liên kết tài sản từ Business Center mới bằng các endpoint quản trị tài sản tương ứng.

---

## Tài liệu tham khảo API (`API reference`)
<a id="doc-1739562438061058"></a>
<!-- doc_id: 1739562438061058 -->

> Đường dẫn: Marketing API > Business Center > API reference

Danh sách các endpoint API hiện có sẵn để quản lý Business Center:

### Quản trị Business Center (`BC Management`)
- [Lấy danh sách Business Center](../12-api-reference/12-bc-management.md#doc-1737115687501826)
- [Lấy nhật ký hoạt động của Business Center](../12-api-reference/12-bc-management.md#doc-1820767460168705)

### Thành viên (`Members`)
- [Lấy danh sách thành viên của Business Center](../12-api-reference/19-bc-members.md#doc-1739939404802049)
- [Mời thành viên vào Business Center](../12-api-reference/19-bc-members.md#doc-1739939455765505)
- [Cập nhật thông tin thành viên Business Center](../12-api-reference/19-bc-members.md#doc-1739696704424961)
- [Xóa thành viên khỏi Business Center hoặc thu hồi lời mời](../12-api-reference/19-bc-members.md#doc-1739939482851329)

### Đối tác (`Partners`)
- [Lấy danh sách đối tác của Business Center](../12-api-reference/18-bc-partners.md#doc-1739662727395330)
- [Thêm đối tác vào Business Center](../12-api-reference/18-bc-partners.md#doc-1739662756510721)
- [Xóa đối tác khỏi Business Center](../12-api-reference/18-bc-partners.md#doc-1739662779301890)
- [Hủy chia sẻ tài sản](../12-api-reference/18-bc-partners.md#doc-1739662800930817)
- [Lấy tài sản của đối tác](../12-api-reference/18-bc-partners.md#doc-1739662828320769)

### Thanh toán (`Payments`)
- [Xử lý thanh toán](../12-api-reference/13-bc-payments.md#doc-1739939095321601)
- [Lấy số dư và ngân sách của tài khoản quảng cáo](../12-api-reference/13-bc-payments.md#doc-1739939106470913)
- [Lấy số dư của Business Center](../12-api-reference/13-bc-payments.md#doc-1739939128198145)
- [Lấy bản ghi giao dịch của Business Center hoặc tài khoản quảng cáo](../12-api-reference/13-bc-payments.md#doc-1792849810925569)
- [Lấy bản ghi giao dịch của tài khoản quảng cáo](../12-api-reference/13-bc-payments.md#doc-1739939116353538)
- [Lấy bản ghi giao dịch của Business Center](../12-api-reference/13-bc-payments.md#doc-1739939140408322)
- [Lấy lịch sử thay đổi ngân sách của tài khoản quảng cáo](../12-api-reference/13-bc-payments.md#doc-1830173979548674)
- [Lấy bản ghi chi phí của Business Center và tài khoản quảng cáo](../12-api-reference/13-bc-payments.md#doc-1829079287639041)

### Danh mục thanh toán (`Payment Portfolios`)
- [Lấy danh sách Danh mục thanh toán](../12-api-reference/14-bc-payment-portfolios.md#doc-1839151931301954)
- [Tạo Danh mục thanh toán](../12-api-reference/14-bc-payment-portfolios.md#doc-1839151986039809)
- [Liên kết tài khoản quảng cáo với Danh mục thanh toán](../12-api-reference/14-bc-payment-portfolios.md#doc-1839151992566081)
- [Phân bổ hạn mức tín dụng cho Danh mục thanh toán](../12-api-reference/14-bc-payment-portfolios.md#doc-1839151998450754)
- [Lấy danh sách tài khoản quảng cáo liên kết với Danh mục thanh toán](../12-api-reference/14-bc-payment-portfolios.md#doc-1839152005599234)
- [Lấy danh sách người dùng được ủy quyền cho Danh mục thanh toán](../12-api-reference/14-bc-payment-portfolios.md#doc-1839152031645121)

### Hóa đơn (`Invoices`)
- [Lấy danh sách hóa đơn của Business Center](../12-api-reference/20-bc-invoices.md#doc-1740295890332674)
- [Lấy số tiền chưa thanh toán của Business Center](../12-api-reference/20-bc-invoices.md#doc-1740295904843777)
- [Tải hóa đơn của Business Center](../12-api-reference/20-bc-invoices.md#doc-1740295923474433)
  - [Tải xuống đồng bộ](../12-api-reference/20-bc-invoices.md#doc-1754000198430722)
  - [Tải xuống bất đồng bộ](../12-api-reference/20-bc-invoices.md#doc-1754000224141313)
    - [Tạo tác vụ tải xuống bất đồng bộ](../12-api-reference/20-bc-invoices.md#doc-1754000448122882)
    - [Lấy thông tin tác vụ tải xuống bất đồng bộ](../12-api-reference/20-bc-invoices.md#doc-1754000480307265)
    - [Lấy danh sách tác vụ tải xuống bất đồng bộ](../12-api-reference/20-bc-invoices.md#doc-1754000504437762)

### Nhóm thanh toán (`Billing Groups`)
- [Tạo Nhóm thanh toán](../12-api-reference/17-bc-billing-groups.md#doc-1738947780033537)
- [Cập nhật Nhóm thanh toán](../12-api-reference/17-bc-billing-groups.md#doc-1738947843447809)
- [Lấy danh sách Nhóm thanh toán](../12-api-reference/17-bc-billing-groups.md#doc-1738944324279297)
- [Lấy danh sách nhà quảng cáo của Nhóm thanh toán](../12-api-reference/17-bc-billing-groups.md#doc-1738458108705794)

### Tài sản (`Assets`)
- [Tạo tài khoản quảng cáo](../12-api-reference/15-bc-assets.md#doc-1739939020318721)
- [Cập nhật tài khoản quảng cáo](../12-api-reference/15-bc-assets.md#doc-1739939050770434)
- [Vô hiệu hóa tài khoản quảng cáo](../12-api-reference/15-bc-assets.md#doc-1752349244331009)
- [Tải lên chứng nhận doanh nghiệp](../12-api-reference/15-bc-assets.md#doc-1739938996913218)
- [Lấy các chứng nhận trong Business Center](../12-api-reference/15-bc-assets.md#doc-1770118680584194)
- [Kiểm tra yêu cầu xác minh UnionPay cho giấy phép kinh doanh](../12-api-reference/15-bc-assets.md#doc-1813772238056449)
- [Gửi xác minh UnionPay cho giấy phép kinh doanh](../12-api-reference/15-bc-assets.md#doc-1813772274039809)
- [Tạo Tài khoản tổ chức trong Business Center](../12-api-reference/15-bc-assets.md#doc-1855027199571138)
- [Lấy danh sách tài sản](../12-api-reference/15-bc-assets.md#doc-1739432717798401)
- [Lấy danh sách tài sản với tư cách quản trị viên](../12-api-reference/15-bc-assets.md#doc-1739433007779841)
- [Gán tài sản](../12-api-reference/15-bc-assets.md#doc-1739438211077121)
- [Hủy gán tài sản](../12-api-reference/15-bc-assets.md#doc-1739448126749698)
- [Yêu cầu liên kết tài khoản TikTok với Business Center](../12-api-reference/15-bc-assets.md#doc-1879660350792706)
- [Hủy liên kết tài khoản TikTok khỏi Business Center](../12-api-reference/15-bc-assets.md#doc-1879660354954833)
- [Lấy URL ủy quyền phân phối quảng cáo của tài khoản TikTok](../12-api-reference/15-bc-assets.md#doc-1846868897541122)
- [Liên kết tài khoản TikTok với tài khoản quảng cáo trong Business Center](../12-api-reference/15-bc-assets.md#doc-1846868953025538)
- [Hủy liên kết tài khoản TikTok khỏi tài khoản quảng cáo trong Business Center](../12-api-reference/15-bc-assets.md#doc-1855027260369921)
- [Lấy các tài khoản quảng cáo được liên kết với tài khoản TikTok trong Business Center](../12-api-reference/15-bc-assets.md#doc-1855027294743554)
- [Quản lý pixel](../12-api-reference/15-bc-assets.md#doc-1739659520972802)
  - [Chuyển giao pixel từ nhà quảng cáo sang Business Center](../12-api-reference/15-bc-assets.md#doc-1753994928261122)
  - [Liên kết / Hủy liên kết pixel với tài khoản quảng cáo](../12-api-reference/15-bc-assets.md#doc-1753994950327297)
  - [Lấy danh sách tài khoản quảng cáo liên kết với pixel](../12-api-reference/15-bc-assets.md#doc-1753994966965249)
- [Lấy đối tác theo tài sản](../12-api-reference/15-bc-assets.md#doc-1739663268166722)
- [Lấy thành viên theo tài sản](../12-api-reference/15-bc-assets.md#doc-1739659558931458)
- [Xóa tài sản khỏi Business Center](../12-api-reference/15-bc-assets.md#doc-1739657251102722)
- [Lấy thông tin ràng buộc của tài sản](../12-api-reference/15-bc-assets.md#doc-1739659584022529)

### Xác minh (`Verification`)
- [Lấy các loại tài liệu xác minh khả dụng cho một khu vực](../12-api-reference/72-verification.md#doc-1870687810081794)
- [Tải lên tài liệu xác minh](../12-api-reference/72-verification.md#doc-1870687812502530)
- [Gửi yêu cầu xác minh cho tài khoản của bạn](../12-api-reference/72-verification.md#doc-1870687936881281)
- [Kiểm tra trạng thái xác minh của tài khoản](../12-api-reference/72-verification.md#doc-1870687815670786)

### Nhóm tài sản (`Asset Groups`)
- [Tạo Nhóm tài sản](../12-api-reference/16-bc-asset-groups.md#doc-1749001658583105)
- [Cập nhật Nhóm tài sản](../12-api-reference/16-bc-asset-groups.md#doc-1749001662156801)
- [Lấy danh sách tất cả các Nhóm tài sản](../12-api-reference/16-bc-asset-groups.md#doc-1749001665910786)
- [Lấy chi tiết của một Nhóm tài sản](../12-api-reference/16-bc-asset-groups.md#doc-1749001669670913)
- [Xóa Nhóm tài sản](../12-api-reference/16-bc-asset-groups.md#doc-1749001673406466)

### Báo cáo (`Reporting`)
- [Chạy báo cáo đồng bộ](../12-api-reference/58-reporting.md#doc-1740302848100353)

### Báo cáo Business Center (`BC Reporting`)
- [Lấy đơn vị tiền tệ và khu vực đăng ký cho các tài khoản quảng cáo](../12-api-reference/21-bc-reporting.md#doc-1775752357139457)
