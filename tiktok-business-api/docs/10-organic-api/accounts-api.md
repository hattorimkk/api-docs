# Organic API — Accounts API

> Phân hệ: guide:Organic API/Accounts API.
> Tài liệu biên dịch kỹ thuật chi tiết theo chuẩn TikTok Business API v1.3.

---

## Mục lục điều hướng
- [1. Accounts API (#doc-1737565048641538)](#doc-1737565048641538)
- [2. Tổng quan (Overview) (#doc-1737944384433218)](#doc-1737944384433218)
- [3. Hướng dẫn (Guides) (#doc-1760334514340866)](#doc-1760334514340866)
- [4. Bắt đầu (Get started) (#doc-1760334598980610)](#doc-1760334598980610)
- [5. Ủy quyền tài khoản (Authorization) (#doc-1738083939371009)](#doc-1738083939371009)
- [6. Câu hỏi thường gặp về ủy quyền (FAQs) (#doc-1766042058952706)](#doc-1766042058952706)
- [7. Xác thực tài khoản (Authentication) (#doc-1738084387220481)](#doc-1738084387220481)
- [8. Giới hạn tần suất gọi (Rate limits) (#doc-1738084416214017)](#doc-1738084416214017)
- [9. Quản lý thuộc tính URL (Manage URL properties) (#doc-1769324038780930)](#doc-1769324038780930)
- [10. Quản lý bình luận trên video TikTok sở hữu (#doc-1776065099288577)](#doc-1776065099288577)
- [11. Quản lý ủy quyền quảng cáo bài đăng TikTok (#doc-1815124785075201)](#doc-1815124785075201)
- [12. Độ trễ dữ liệu Accounts Insights (#doc-1746624508278786)](#doc-1746624508278786)
- [13. Webhooks (#doc-1759977800177665)](#doc-1759977800177665)
- [14. Các loại sự kiện Webhook (Webhook event types) (#doc-1759978319341570)](#doc-1759978319341570)
- [15. Sự kiện xuất bản bài đăng (Post publishing events) (#doc-1810515090228226)](#doc-1810515090228226)
- [16. Sự kiện cập nhật bình luận (Comment update event) (#doc-1810515104773122)](#doc-1810515104773122)
- [17. Xác minh chữ ký Webhook (Webhook verification) (#doc-1759978341579777)](#doc-1759978341579777)
- [18. Câu hỏi thường gặp (FAQs) (#doc-1776983576127490)](#doc-1776983576127490)
- [19. Danh mục API tham chiếu (API reference) (#doc-1740304387032066)](#doc-1740304387032066)

---

<a id="doc-1737565048641538"></a>
<!-- doc_id: 1737565048641538 -->
<!-- doc_id: 1737565048641538 -->
# Accounts API
> Đường dẫn: Organic API > Accounts API
Với Accounts API, bạn có thể quản lý và báo cáo hoạt động tài khoản TikTok bằng phương thức lập trình, đạt được những thông tin phân tích chuyên sâu và khả năng kiểm soát trên quy mô lớn.

> **Lưu ý:**
> Để đảm bảo việc sử dụng Accounts API đúng quy chuẩn, bắt đầu từ ngày 20 tháng 3 năm 2026 lúc 00:00 (GMT+0), các nhà phát triển bắt buộc phải hoàn thành [Biểu mẫu đăng ký quyền truy cập Accounts API](https://bytedance.sg.larkoffice.com/share/base/form/shrlgu4WEvtSXpEDLcCw56u4Rfc) trước khi gửi ứng dụng nhà phát triển mới hoặc yêu cầu mở rộng phạm vi quyền hạn bao gồm scope "TikTok Accounts". Vui lòng làm theo hướng dẫn cẩn thận và cung cấp thông tin rõ ràng, chính xác để tạo điều kiện thuận lợi cho quá trình xem xét. Để biết thêm chi tiết về các tình huống sử dụng Accounts API, vui lòng tham khảo tài liệu [Accounts API](accounts-api.md#doc-1737944384433218).

Bạn có thể tìm hiểu thêm thông tin chi tiết về Accounts API trong chương này:
- [Tổng quan](accounts-api.md#doc-1737944384433218): Giới thiệu chức năng của Accounts API và một số thuật ngữ phổ biến.
- [Ủy quyền](accounts-api.md#doc-1738083939371009): Hướng dẫn cách xin cấp quyền ủy quyền từ doanh nghiệp để quản lý tài khoản của họ.
- [Xác thực](accounts-api.md#doc-1738084387220481): Hướng dẫn cách lấy `access_token` cho các yêu cầu API tiếp theo, cũng như `refresh_token` để gia hạn mã truy cập.
- [Giới hạn tần suất gọi](accounts-api.md#doc-1738084416214017): Giới thiệu các giới hạn tần suất gọi của Accounts API.
- [Quản lý thuộc tính URL](accounts-api.md#doc-1769324038780930): Cung cấp thông tin về cách quản lý các thuộc tính URL để sử dụng với Accounts API, bao gồm các loại thuộc tính URL có thể xác minh trước khi xuất bản video, quy tắc xác minh quyền sở hữu và quy trình từng bước để thêm và xác minh thuộc tính URL.
- [Quản lý bình luận trên video TikTok sở hữu](accounts-api.md#doc-1776065099288577): Giới thiệu quy trình và tình huống sử dụng trong việc kiểm duyệt bình luận trên các video TikTok thuộc sở hữu.
- [Quản lý ủy quyền quảng cáo bài đăng TikTok](accounts-api.md#doc-1815124785075201): Giới thiệu quy trình quản lý mã ủy quyền (authorization code) của các bài đăng TikTok.
- [Độ trễ dữ liệu Accounts Insights](accounts-api.md#doc-1746624508278786): Giới thiệu độ trễ dữ liệu bạn có thể gặp phải khi sử dụng Accounts Insights API.
- [Webhooks](accounts-api.md#doc-1759977800177665): Giới thiệu các yêu cầu và giới hạn đối với URL gọi lại của webhook, các sự kiện webhook khả dụng cho Accounts API và quy trình xác minh chữ ký webhook.
- [Câu hỏi thường gặp](accounts-api.md#doc-1776983576127490): Giải đáp các thắc mắc phổ biến về Accounts API.
- [Danh mục API tham chiếu](accounts-api.md#doc-1740304387032066): Giới thiệu các endpoint khả dụng của Accounts API.

---

<a id="doc-1737944384433218"></a>
<!-- doc_id: 1737944384433218 -->
<!-- doc_id: 1737944384433218 -->
# Tổng quan (Overview)
> Đường dẫn: Organic API > Accounts API > Overview
TikTok Accounts API là chuỗi 3 dịch vụ giao diện được đội ngũ API for Business cung cấp cho các nhà phát triển. Thông qua việc tích hợp và gọi Accounts API, các nhà phát triển có thể tận dụng giao diện của chúng tôi để tương tác với tài khoản TikTok, bao gồm trích xuất Báo cáo / Thông tin phân tích (Insights), Kiểm duyệt bình luận (Moderation) và Xuất bản video (Publishing).

> **Lưu ý:**
> Để đảm bảo việc sử dụng Accounts API đúng quy chuẩn, bắt đầu từ ngày 20 tháng 3 năm 2026 lúc 00:00 (GMT+0), các nhà phát triển bắt buộc phải hoàn thành [Biểu mẫu đăng ký quyền truy cập Accounts API](https://bytedance.sg.larkoffice.com/share/base/form/shrlgu4WEvtSXpEDLcCw56u4Rfc) trước khi gửi ứng dụng nhà phát triển mới hoặc yêu cầu mở rộng phạm vi quyền hạn bao gồm scope "TikTok Accounts". Vui lòng làm theo hướng dẫn cẩn thận và cung cấp thông tin rõ ràng, chính xác. Để biết thêm chi tiết, xem tài liệu [Accounts API](accounts-api.md#doc-1737944384433218).

![Accounts API](https://images.ctfassets.net/5jqet0ab9qci/59PCyn1m0UxZO0zcDTTPWx/8aeb17c6a06153f395f12c34babfef60/Accounts_API.png)

- **Accounts Insights**: Cho phép các nhà quảng cáo có tài khoản TikTok sở hữu trên nền tảng truy cập vào các số liệu phân tích và thông tin chi tiết về lượng người theo dõi và mức độ tương tác của video.
- **Accounts Moderation**: Cho phép nhà quảng cáo kiểm duyệt bình luận trên các tài khoản TikTok của họ.
- **Accounts Video Publishing**: Cho phép nhà quảng cáo đăng tải video trực tiếp lên tài khoản TikTok của họ.

## Lợi ích của Accounts API
- **Kiểm soát bằng phương thức lập trình trên quy mô lớn**: Accounts API của TikTok cho phép các nhà quảng cáo đạt được quyền kiểm soát tự động và quy mô hóa đối với Thông tin phân tích, Kiểm duyệt và Xuất bản nội dung tài khoản.
- **Cung cấp thông tin chi tiết sâu sắc**: Accounts API cho phép các doanh nghiệp sở hữu tài khoản trên TikTok nhận được các phân tích chi tiết về tệp người theo dõi và tương tác trang cá nhân, cũng như phạm vi tiếp cận và tương tác cho các bài đăng tự nhiên (organic posts).
- **Cải thiện tính nhất quán thương hiệu**: Accounts API hỗ trợ các nhà quảng cáo quản lý hình ảnh thương hiệu trên TikTok một cách toàn diện hơn bằng cách cho phép kiểm duyệt bình luận trên các bài đăng video.
- **Tăng cường khả năng hiển thị đa kênh**: Accounts API mở rộng các khả năng báo cáo và xuất bản cho các nhà tiếp thị, cho phép họ tận dụng dữ liệu để giám sát và lập báo cáo trên nhiều nền tảng, đồng thời cung cấp khả năng xuất bản ngay trên nền tảng riêng của họ.

## Tình huống sử dụng Accounts API
Vui lòng chỉ sử dụng Accounts API theo đúng các mục đích được phép như chỉ định dưới đây. TikTok bảo lưu quyền thu hồi quyền truy cập Accounts API của nhà phát triển bất kỳ lúc nào mà không cần thông báo trước trong trường hợp sử dụng sai mục đích, vi phạm chính sách hoặc lạm dụng Accounts API.

**Các trường hợp được phép sử dụng Accounts API:**
Quản lý sự hiện diện tự nhiên của các tài khoản thương hiệu hoặc nhà sáng tạo sở hữu trên TikTok, bao gồm:
* Xuất bản các bài đăng video hoặc hình ảnh.
* Kiểm duyệt bình luận.
* Phân tích thông tin chi tiết về hồ sơ và bài đăng TikTok.
* Thực hiện ủy quyền quảng cáo cho các bài đăng TikTok.

**Các hành vi bị cấm khi sử dụng Accounts API:**
* Trích xuất báo cáo về hồ sơ và bài đăng TikTok từ tài khoản của các nhà sáng tạo được ủy quyền, rồi sử dụng dữ liệu tổng hợp đó để tự xây dựng chương trình tiếp thị người ảnh hưởng liên kết (chẳng hạn như khám phá và xếp hạng nhà sáng tạo), thay vì sử dụng nền tảng hoặc API của TikTok One.
* Tải xuống video và hình ảnh TikTok, quảng bá các giải pháp của bên thứ ba để lưu dữ liệu người dùng hoặc phương tiện từ TikTok, hoặc chuyển nội dung sang tài khoản TikTok khác hay các nền tảng mạng xã hội khác.

## Các thuật ngữ (Terms)
- **TikTok account (Tài khoản TikTok)**: Hồ sơ số hợp nhất trên nền tảng TikTok cho phép các cá nhân, nhà sáng tạo và thương hiệu tạo nội dung đa phương tiện, tương tác với cộng đồng toàn cầu và tiến hành thương mại xã hội.
- **General TikTok Account (Tài khoản TikTok thông thường - còn gọi là Personal Account)**: Đây là loại tài khoản tiêu chuẩn ban đầu của mọi người dùng. Nó cung cấp các tính năng nguyên bản của TikTok để tạo nội dung, tương tác, nhưng không bao gồm quyền truy cập vào Web Business Suite hoặc Mobile Business Suite.
- **TikTok Account with Advanced Access (Tài khoản TikTok có Quyền truy cập Nâng cao)**: Cấp độ trung gian này được cấp khi bạn liên kết tài khoản TikTok với tài khoản TikTok for Business hoặc Business Center chưa xác minh. Nó mở khóa thêm các công cụ tự nhiên và thông tin phân tích để quản lý nội dung và hiệu suất.
- **Verified Business Account (Tài khoản Doanh nghiệp Đã xác minh - trước đây gọi là Registered Business Account)**: Cấp độ cao nhất, được cấp sau khi hoàn tất xác minh doanh nghiệp. Nó mở khóa các công cụ kinh doanh nâng cao, củng cố hiện diện thương hiệu và mang lại các khả năng chuyển đổi chuyên sâu hơn.
- **Business (Doanh nghiệp)**: Doanh nghiệp sử dụng tài khoản TikTok để quảng bá sản phẩm/dịch vụ một cách tự nhiên và tương tác với khán giả trên TikTok.
- **Developer (Nhà phát triển)**: Thực thể phát triển các ứng dụng sử dụng Accounts API cho tài khoản TikTok.

---

<a id="doc-1760334514340866"></a>
<!-- doc_id: 1760334514340866 -->
<!-- doc_id: 1760334514340866 -->
# Hướng dẫn (Guides)
> Đường dẫn: Organic API > Accounts API > Guides
Tài liệu hướng dẫn này dẫn dắt bạn qua quy trình tích hợp và giới thiệu các tài nguyên hữu ích của Accounts API.

- [Bắt đầu (Get started)](accounts-api.md#doc-1760334598980610): Giới thiệu quy trình tiếp cận ban đầu và các hạn mức tần suất gọi của Accounts API.
  - [Ủy quyền](accounts-api.md#doc-1738083939371009): Hướng dẫn cách nhận sự ủy quyền từ doanh nghiệp để quản lý tài khoản của họ.
  - [Xác thực](accounts-api.md#doc-1738084387220481): Hướng dẫn cách lấy `access_token` cho các lệnh gọi API tiếp theo, cũng như `refresh_token` để gia hạn mã truy cập.
  - [Giới hạn tần suất gọi](accounts-api.md#doc-1738084416214017): Giới thiệu các giới hạn tần suất gọi của Accounts API.
- [Quản lý thuộc tính URL](accounts-api.md#doc-1769324038780930): Cung cấp thông tin về cách quản lý các thuộc tính URL trước khi xuất bản video.
- [Quản lý bình luận trên video TikTok sở hữu](accounts-api.md#doc-1776065099288577): Giới thiệu quy trình và các tình huống sử dụng trong việc quản lý bình luận.
- [Quản lý ủy quyền quảng cáo bài đăng TikTok](accounts-api.md#doc-1815124785075201): Giới thiệu quy trình quản lý mã ủy quyền của bài đăng TikTok.
- [Độ trễ dữ liệu Accounts Insights](accounts-api.md#doc-1746624508278786): Giới thiệu độ trễ dữ liệu bạn có thể gặp phải khi gọi API phân tích.
- [Webhooks](accounts-api.md#doc-1759977800177665): Giới thiệu các yêu cầu đối với URL webhook, sự kiện webhook và quy trình xác minh.
- [Câu hỏi thường gặp](accounts-api.md#doc-1776983576127490): Các thắc mắc phổ biến về Accounts API.

---

<a id="doc-1760334598980610"></a>
<!-- doc_id: 1760334598980610 -->
<!-- doc_id: 1760334598980610 -->
# Bắt đầu (Get started)
> Đường dẫn: Organic API > Accounts API > Guides > Get started
Chào mừng bạn đến với TikTok Accounts API! Với định hướng lấy nhà phát triển làm trọng tâm, việc tiếp cận và sử dụng API của chúng tôi rất đơn giản. Chỉ cần một vài bước cơ bản là bạn đã có thể bắt đầu quản lý tài khoản TikTok của mình.

## Quy trình từng bước (Step by step workflow)
1. [Tạo tài khoản TikTok For Business](../04-get-started/bat-dau.md#doc-1738855099573250).
2. [Đăng ký làm nhà phát triển](../04-get-started/bat-dau.md#doc-1738855176671234).
3. [Tạo ứng dụng nhà phát triển](../04-get-started/bat-dau.md#doc-1738855242728450).
4. [Ủy quyền tài khoản](accounts-api.md#doc-1738083939371009).
5. [Xác thực và lấy token](accounts-api.md#doc-1738084387220481).
6. Thực hiện lệnh gọi API đầu tiên của bạn.

## Các endpoint API (API endpoints)
Để tìm hiểu về các endpoint khả dụng của Accounts API, hãy xem [Danh mục API tham chiếu](accounts-api.md#doc-1740304387032066).

## Giới hạn tần suất gọi (Rate limits)
Để tìm hiểu chi tiết về hạn mức gọi API, hãy xem [Giới hạn tần suất gọi](accounts-api.md#doc-1738084416214017).

## Bảng mã lỗi (Error codes)
Để tra cứu các mã lỗi trả về khi gọi thất bại, hãy xem [Phụ lục - Mã lỗi trả về](../15-appendix/phu-luc-p1.md#doc-1737172488964097).

---

<a id="doc-1738083939371009"></a>
<!-- doc_id: 1738083939371009 -->
<!-- doc_id: 1738083939371009 -->
# Ủy quyền tài khoản (Authorization)
> Đường dẫn: Organic API > Accounts API > Guides > Get started > Authorization
Trước khi bạn sử dụng Accounts API, bạn (nhà phát triển) cần nhận được sự ủy quyền từ doanh nghiệp để quản lý tài khoản TikTok của họ.

## Điều kiện tiên quyết (Prerequisites)
* Bạn đã tạo tài khoản TikTok For Business. Để biết chi tiết, xem [Tạo tài khoản TikTok For Business](../04-get-started/bat-dau.md#doc-1738855099573250).
* Bạn đã đăng ký làm nhà phát triển. Để biết chi tiết, xem [Đăng ký làm nhà phát triển](../04-get-started/bat-dau.md#doc-1738855176671234).
* Bạn đã tạo ứng dụng nhà phát triển với phạm vi quyền hạn bắt buộc bao gồm "TikTok Accounts" để truy cập các endpoint của Accounts API. Để biết chi tiết, xem [Tạo ứng dụng nhà phát triển](../04-get-started/bat-dau.md#doc-1738855242728450).

## Các bước thực hiện (Steps)
1. Nhà phát triển chia sẻ URL ủy quyền với chủ tài khoản TikTok. Bạn có thể tìm thấy URL này bằng cách điều hướng đến **[My Apps](https://ads.tiktok.com/marketing_api/apps/)** > **App Detail** > **Basic Information** > **TikTok account holder authorization URL**.

> **Lưu ý:**
> Theo mặc định, nếu người dùng tài khoản TikTok đã từng ủy quyền ứng dụng nhà phát triển cho các quyền hạn tương tự trước đó, trang xem xét và phê duyệt phạm vi quyền hạn ở Bước 2 sẽ được bỏ qua. Thay vào đó, người dùng sẽ được chuyển hướng thẳng đến Redirect URL. **Để vô hiệu hóa cơ chế tự động chuyển hướng này**, hãy thêm `&disable_auto_auth=1` vào cuối TikTok account holder authorization URL trước khi chia sẻ với người dùng. Ví dụ: `https://www.tiktok.com/v2/auth/authorize?{parameters}&disable_auto_auth=1`.

2. Chủ tài khoản TikTok mở URL ủy quyền và cấp quyền cho ứng dụng nhà phát triển của bạn.
   - Để truy cập Accounts API, người dùng cần cấp quyền cho các phạm vi sau:
     - Quản lý bài đăng video và ảnh: `video.publish`, `video.upload`
     - Kiểm duyệt bình luận: `comment.list`, `comment.list.manage`
     - Phân tích thông tin chi tiết tài khoản: `user.info.basic`, `user.info.profile`, `user.info.stats`, `user.insights`, `video.list`, `video.insights`
     - Ủy quyền quảng cáo bài đăng: `biz.spark.auth`
3. Sau khi đồng ý ủy quyền, người dùng tài khoản TikTok sẽ được chuyển hướng đến **Redirect URL** của ứng dụng. Redirect URL sẽ đính kèm tham số `code=`, chính là mã ủy quyền (`auth_code`) dùng để tạo access token.

### Quy tắc định dạng Redirect URL
Khi cấu hình **TikTok account holder redirect URL** cho ứng dụng, hãy tuân thủ các quy tắc định dạng sau:

| No. | Rules | Correct example | Bad example |
|---|---|---|---|
| 1 | URL phải là tuyệt đối và kết thúc bằng `/`. | `https://dev.example.com/auth/callback/` | • `https://dev.example.com/auth/callback`<br>• thiếu dấu `/` ở cuối<br>• `/auth/callback/` (thiếu giao thức và tên miền) |
| 2 | URL phải là tĩnh, tham số truy vấn bị từ chối và sẽ bị bỏ qua. | `https://dev.example.com/auth/callback/` | • `https://dev.example.com/auth/callback/?id=1` (chứa tham số query `?id=1`) |
| 3 | URL không được chứa ký tự neo `#`. | `https://dev.example.com/auth/callback/` | • `https://dev.example.com/auth/callback/#1` (chứa neo `#1`) |
| 4 | URL phải bắt đầu bằng `https://`. | `https://dev.example.com/auth/callback/` | • `http://dev.example.com/auth/callback/` (dùng `http` thay vì `https`) |
| 5 | URL không được chứa cổng (port). | `https://dev.example.com/auth/callback/` | • `https://dev.example.com:3000/auth/callback/` (chứa số cổng `:3000`) |
| 6 | Độ dài URI đăng ký phải từ 10 đến 512 ký tự. | N/A | N/A |

---

<a id="doc-1766042058952706"></a>
<!-- doc_id: 1766042058952706 -->
<!-- doc_id: 1766042058952706 -->
# Câu hỏi thường gặp về ủy quyền (FAQs)
> Đường dẫn: Organic API > Accounts API > Guides > Get started > Authorization > FAQs
Tài liệu này tổng hợp các câu hỏi phổ biến về quy trình ủy quyền trước khi sử dụng Accounts API.

## Các câu hỏi thường gặp

**Hỏi: Trên trang App Detail có hai URL ủy quyền khác nhau - Advertiser authorization URL và TikTok account holder authorization URL, sự khác biệt giữa chúng là gì?**

Trả lời: URL ủy quyền nhà quảng cáo (Advertiser authorization URL) được sử dụng để lấy quyền từ nhà quảng cáo, tài khoản TikTok Creator Marketplace (TTCM) hoặc TikTok One (TTO) Creator Marketplace, trong khi URL ủy quyền chủ tài khoản TikTok (TikTok account holder authorization URL) được dùng để lấy quyền từ Creator hoặc người dùng tài khoản TikTok tự nhiên. Xem bảng bên dưới:

- **Marketing API**: Ủy quyền qua tài khoản nhà quảng cáo TikTok For Business.
- **Accounts API / Mentions API**: Ủy quyền qua tài khoản TikTok tự nhiên (TikTok organic account).
- **TikTok One API**: Ủy quyền qua tài khoản TTO Creator Marketplace và tài khoản Creator.
- **Discovery API**: Ủy quyền qua tài khoản nhà quảng cáo TikTok For Business.
- **Spark Ads Recommendation API**: Ủy quyền qua tài khoản nhà quảng cáo TikTok For Business.

**Hỏi: Mã `auth_code` có thời hạn trong bao lâu?**
Mã `auth_code` chỉ có hiệu lực trong 10 phút và chỉ sử dụng được duy nhất một lần. Sau khi hết hạn, bạn phải thực hiện lại quy trình ủy quyền để lấy mã mới.

---

<a id="doc-1738084387220481"></a>
<!-- doc_id: 1738084387220481 -->
<!-- doc_id: 1738084387220481 -->
# Xác thực tài khoản (Authentication)
> Đường dẫn: Organic API > Accounts API > Guides > Get started > Authentication
Với mã ủy quyền nhận được sau khi người dùng tài khoản TikTok cấp phép, bạn có thể gửi yêu cầu đến endpoint sau để nhận mã truy cập `access_token` cho các yêu cầu API tiếp theo, cũng như `refresh_token` để gia hạn mã truy cập.

Để kiểm tra các phạm vi quyền hạn tài khoản TikTok đã được ủy quyền, bạn có thể truyền access token vào [/tt_user/token_info/get/](../12-api-reference/01-accounts-p1.md#doc-1765927978092545).

## Thời hạn hiệu lực của Access Token
Mã truy cập tài khoản TikTok có hiệu lực trong vòng 1 ngày (24 giờ). Khi hết hạn, bạn cần gửi yêu cầu để gia hạn bằng cách truyền vào `refresh_token`.

## Thời hạn hiệu lực của Refresh Token
Mã làm mới token có hiệu lực trong vòng 1 năm. Nếu refresh token hết hạn, người dùng phải thực hiện lại toàn bộ quy trình ủy quyền.

## Lấy mã truy cập tài khoản TikTok (Obtain a TikTok account access token)
Sử dụng endpoint này để lấy `access_token` và `refresh_token`.

### Yêu cầu gọi API (Request)

**Endpoint** `https://business-api.tiktok.com/open_api/v1.3/tt_user/oauth2/token/`

**Method** POST

**Header**

| Trường (Field) | Kiểu dữ liệu | Bắt buộc | Mô tả chi tiết |
|---|---|---|---|
| Content-Type | string | Bắt buộc | Định dạng nội dung yêu cầu: `application/json`. |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Bắt buộc | Mô tả chi tiết |
|---|---|---|---|
| client_id | string | Bắt buộc | ID ứng dụng nhà phát triển (App ID). |
| client_secret | string | Bắt buộc | Mã bí mật của ứng dụng nhà phát triển (Secret). |
| grant_type | string | Bắt buộc | Phương thức cấp token: `authorization_code`. |
| auth_code | string | Bắt buộc | Mã ủy quyền thu được từ TikTok account holder authorization URL. |
| redirect_uri | string | Bắt buộc | Redirect URL đã thiết lập cho ứng dụng. |

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

### Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Mã phản hồi API. Giá trị `0` là thành công. |
| message | string | Thông báo phản hồi từ hệ thống. |
| request_id | string | Mã nhật ký yêu cầu để định danh duy nhất lượt gọi API. |
| data | object | Dữ liệu trả về. |
| ↳ access_token | string | Mã truy cập ngắn hạn để gọi các API tiếp theo (hiệu lực 1 ngày). |
| ↳ token_type | string | Loại token: `Bearer`. |
| ↳ scope | string | Danh sách các phạm vi quyền hạn được cấp cho access token. |
| ↳ expires_in | number | Thời gian hiệu lực còn lại của access token (giây). |
| ↳ refresh_token | string | Mã làm mới token để cấp lại access token (hiệu lực 1 năm). |
| ↳ refresh_token_expires_in | number | Thời gian hiệu lực còn lại của refresh token (giây). |
| ↳ open_id | string | Mã định danh duy nhất của tài khoản TikTok đối với ứng dụng. |

## Làm mới mã truy cập tài khoản TikTok (Renew a TikTok account access token)
Sử dụng endpoint `/tt_user/oauth2/refresh_token/` để đổi `refresh_token` lấy access token mới.

```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/tt_user/oauth2/refresh_token/' --header 'Content-Type: application/json' --data-raw '{
 "grant_type" : "refresh_token",
 "refresh_token" : "YOUR_REFRESH_TOKEN",
 "client_secret": "YOUR_CLIENT_SECRET",
 "client_id": "YOUR_CLIENT_ID"
}'
```

## Thu hồi mã truy cập tài khoản TikTok (Revoke a TikTok account access token)
Sử dụng endpoint `/tt_user/oauth2/revoke/` để thu hồi token khi không còn sử dụng.

```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/tt_user/oauth2/revoke/' --header 'Content-Type: application/json' --data '{
    "client_id":"YOUR_CLIENT_ID",
    "client_secret":"YOUR_CLIENT_SECRET",
    "access_token":"YOUR_ACCESS_TOKEN"
}'
```

---

<a id="doc-1738084416214017"></a>
<!-- doc_id: 1738084416214017 -->
<!-- doc_id: 1738084416214017 -->
# Giới hạn tần suất gọi (Rate limits)
> Đường dẫn: Organic API > Accounts API > Guides > Get started > Rate limits
Giới hạn tần suất gọi trên mỗi tài khoản TikTok được ủy quyền và mỗi endpoint Accounts API là 40 truy vấn/phút (QPM). Ngoài ra, có một giới hạn riêng áp dụng chung cho toàn bộ các endpoint Accounts API cộng lại, được xác định bởi cấp độ giới hạn toàn cục (global rate limit level) gán cho ứng dụng nhà phát triển của bạn:

| Global Rate Limit Level | QPM for All Accounts API Endpoints |
|---|---|
| Basic | 600 |
| Advanced | 1,000 |
| Premium | 1,000 |
| Ultimate | 1,000 |

Để tìm hiểu thêm về giới hạn tần suất toàn cục và các cấp độ hạn mức, xem [Rate limits](../04-get-started/bat-dau.md#doc-1740029171730433).

---

<a id="doc-1769324038780930"></a>
<!-- doc_id: 1769324038780930 -->
<!-- doc_id: 1769324038780930 -->
# Quản lý thuộc tính URL (Manage URL properties)
> Đường dẫn: Organic API > Accounts API > Guides > Manage URL properties
Xác minh quyền sở hữu URL video là một bước thiết yếu để tuân thủ các chính sách của TikTok về nội dung có bản quyền và an toàn cho người dùng. Hướng dẫn này sẽ hướng dẫn bạn qua quy trình thêm và xác minh các thuộc tính URL, để bạn có thể xuất bản thành công video công khai lên tài khoản TikTok sở hữu của mình bằng endpoint [/business/video/publish/](../12-api-reference/01-accounts-p1.md#doc-1762228496095234).

Trước khi gọi `/business/video/publish/`, điều cần thiết là phải xác minh rằng URL video bạn dự định truyền vào tham số `video_url` đến từ một thuộc tính URL đã được xác minh quyền sở hữu. Điều này có nghĩa là bạn cần có một trang web hoặc nền tảng trực tuyến lưu trữ video, và sau đó cung cấp URL của video đó cho TikTok khi xuất bản.

> **Lưu ý:**
> Bắt đầu từ tháng 11 năm 2024, các nhà phát triển được yêu cầu cấu hình và xác minh các thuộc tính URL của họ trước khi đăng video lên tài khoản TikTok sở hữu.

## Các loại thuộc tính URL và quy tắc xác minh quyền sở hữu
### Tên miền (Domain)
Tên miền là tên của trang web hoặc nền tảng trực tuyến mà bạn sở hữu, ví dụ: `example.com`.

#### Quy tắc xác minh
Để xác minh quyền sở hữu tên miền, bạn cần tải lên một tệp xác minh HTML do TikTok cung cấp vào thư mục gốc của trang web của bạn hoặc thêm bản ghi DNS TXT vào cấu hình DNS của tên miền.

## Các bước thực hiện
1. **Thêm thuộc tính URL**: Sử dụng endpoint [/business/url_property/add/](../12-api-reference/01-accounts-p2.md#doc-1769325280876545) để đăng ký URL tên miền của bạn.
2. **Nhận hướng dẫn xác minh**: Lấy mã tệp HTML hoặc bản ghi DNS TXT cần thiết.
3. **Triển khai tệp hoặc bản ghi**: Tải tệp HTML lên thư mục gốc hoặc cập nhật bản ghi DNS của tên miền.
4. **Xác minh thuộc tính URL**: Gọi endpoint [/business/url_property/verify/](../12-api-reference/01-accounts-p2.md#doc-1769325308162050) để hoàn tất việc xác minh.

---

<a id="doc-1776065099288577"></a>
<!-- doc_id: 1776065099288577 -->
<!-- doc_id: 1776065099288577 -->
# Quản lý bình luận trên video TikTok sở hữu
> Đường dẫn: Organic API > Accounts API > Guides > Manage comments on owned TikTok videos
Tài liệu này hướng dẫn cách quản lý và kiểm duyệt bình luận trên các video TikTok thuộc sở hữu của bạn.

## Giới thiệu
Quản lý bình luận trên tài khoản TikTok là hoạt động thiết yếu để tạo dựng trải nghiệm tích cực cho cộng đồng, thúc đẩy tương tác, thu thập phản hồi và duy trì uy tín thương hiệu trên mạng xã hội.

**Bạn có thể sử dụng Accounts API để kiểm duyệt, trả lời và phân tích bình luận hiệu quả, nâng cao năng lực quản trị tài khoản TikTok và gắn kết sâu sắc với khán giả.**

## Điều kiện tiên quyết
- Bạn đã có quyền truy cập TikTok API for Business. Xem chi tiết tại [Bắt đầu - Quy trình từng bước](../04-get-started/bat-dau.md#doc-1735713609895937).
- Bạn đã hoàn thành xác thực và nhận access token với các quyền `comment.list` và `comment.list.manage`.

## Tổng quan tình huống sử dụng và các tham số yêu cầu

| Common request parameter | How to configure the parameter |
|---|---|
| `business_id` | • Truyền giá trị `open_id` nhận được từ [/tt_user/oauth2/token/](accounts-api.md#doc-1738084387220481). |
| `video_id` | Truyền giá trị `item_id` của video TikTok thuộc sở hữu. |
| `comment_id` | Truyền giá trị `comment_id` nhận được khi tạo bình luận hoặc truy xuất danh sách bình luận. |

| Scenario | How to configure comment_ids | How to configure include_replies |
|---|---|---|
| Retrieve all top-level comments | Không truyền | Không truyền |
| Retrieve all top-level comments and the corresponding replies | Không truyền | Có truyền (`true`) |
| Retrieve specific comments or replies by ID | Có truyền | Không truyền |
| Retrieve specific top-level comments and their replies by ID in a single request | Có truyền | Có truyền (`true`) |

## Các bước thực hiện
### 1. Lấy ID của video TikTok sở hữu
Sử dụng endpoint [/business/video/list/](../12-api-reference/01-accounts-p1.md#doc-1762228421622786) để lấy danh sách video và `item_id`.

### 2. Quản lý bình luận trên video
- **Tạo bình luận mới**: Gọi [/business/comment/create/](../12-api-reference/01-accounts-p1.md#doc-1762228442072066).
- **Trả lời một bình luận**: Gọi [/business/comment/reply/](../12-api-reference/01-accounts-p1.md#doc-1762228448779266).
- **Thích bình luận**: Gọi [/business/comment/like/](../12-api-reference/01-accounts-p1.md#doc-1762228456608770).
- **Bỏ thích bình luận**: Gọi [/business/comment/unlike/](../12-api-reference/01-accounts-p1.md#doc-1762228456608770).
- **Ẩn bình luận**: Gọi [/business/comment/hide/](../12-api-reference/01-accounts-p1.md#doc-1762228474532865).
- **Bỏ ẩn bình luận**: Gọi [/business/comment/unhide/](../12-api-reference/01-accounts-p1.md#doc-1762228474532865).
- **Xóa bình luận**: Gọi [/business/comment/delete/](../12-api-reference/01-accounts-p1.md#doc-1762228483080193).
- **Lấy danh sách bình luận**: Gọi [/business/comment/list/](../12-api-reference/01-accounts-p1.md#doc-1760232109619202).
- **Lấy toàn bộ câu trả lời của bình luận**: Gọi [/business/comment/reply/list/](../12-api-reference/01-accounts-p1.md#doc-1762228430145538).
- **Đăng ký nhận cập nhật bình luận qua Webhook**: Lắng nghe sự kiện `comment.update`.

---

<a id="doc-1815124785075201"></a>
<!-- doc_id: 1815124785075201 -->
<!-- doc_id: 1815124785075201 -->
# Quản lý ủy quyền quảng cáo bài đăng TikTok (Manage TikTok post ad authorization)
> Đường dẫn: Organic API > Accounts API > Guides > Manage TikTok post ad authorization
Tài liệu này hướng dẫn cách quản lý cài đặt ủy quyền quảng cáo cho các bài đăng TikTok.

## Giới thiệu
Tính năng "Ủy quyền quảng cáo" (Ad authorization) cho phép các bài đăng TikTok tự nhiên được sử dụng làm mẫu quảng cáo cho Spark Ads. Khi bài đăng đã được ủy quyền, bạn có thể [tạo Spark Ads bằng cách trích xuất bài đăng tự nhiên thông qua mã ủy quyền](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1739470744631298).

**Bạn có thể sử dụng Accounts API để tạo, gia hạn và xóa mã ủy quyền của bài đăng TikTok một cách linh hoạt, tinh gọn quy trình quản lý mã quảng cáo.**

## Điều kiện tiên quyết
- Bạn đã có quyền truy cập TikTok API for Business và có mã truy cập với scope `biz.spark.auth`.

## Các bước thực hiện
1. **Tạo mã ủy quyền quảng cáo**: Gọi [/business/video/ad_authorization/create/](../12-api-reference/01-accounts-p2.md#doc-1815051784582210).
2. **Gia hạn thời gian ủy quyền quảng cáo**: Gọi [/business/video/ad_authorization/update/](../12-api-reference/01-accounts-p2.md#doc-1815051741912066).
3. **Xóa mã ủy quyền quảng cáo**: Gọi [/business/video/ad_authorization/delete/](../12-api-reference/01-accounts-p2.md#doc-1815051817073665).
4. **Lấy danh sách mã ủy quyền quảng cáo**: Gọi [/business/video/ad_authorization/get/](../12-api-reference/01-accounts-p2.md#doc-1815051801257986).

---

<a id="doc-1746624508278786"></a>
<!-- doc_id: 1746624508278786 -->
<!-- doc_id: 1746624508278786 -->
# Độ trễ dữ liệu Accounts Insights (Accounts Insights data latency)
> Đường dẫn: Organic API > Accounts API > Guides > Accounts Insights data latency
Có thể có độ trễ khi bạn trích xuất dữ liệu về lượng người theo dõi và tương tác hồ sơ tài khoản TikTok qua [/business/get/](../12-api-reference/01-accounts-p1.md#doc-1762228399168514), hoặc trích xuất phạm vi tiếp cận và dữ liệu tương tác cho bài đăng tự nhiên qua [/business/video/list/](../12-api-reference/01-accounts-p1.md#doc-1762228421622786).

## Các mức độ trễ dữ liệu
Độ trễ đối với các trường dữ liệu được chia làm hai loại:
- **Không có độ trễ (Thời gian thực)**: Dữ liệu thời gian thực như `username`, `display_name`, `profile_image`, `share_url` thường được cập nhật tức thì.
- **Độ trễ cấp ngày (Ngoại tuyến)**: Dữ liệu thống kê tổng hợp như `likes`, `comments`, `shares`, `reach`, `audience_countries` thường có độ trễ từ 24 đến 48 giờ (theo giờ UTC).

---

<a id="doc-1759977800177665"></a>
<!-- doc_id: 1759977800177665 -->
<!-- doc_id: 1759977800177665 -->
# Webhooks
> Đường dẫn: Organic API > Accounts API > Guides > Webhooks
Webhook là cơ chế gọi lại HTTP tự động được kích hoạt khi các sự kiện cụ thể diễn ra trên nền tảng TikTok, cho phép gửi thông báo theo thời gian thực tới URL gọi lại đã cấu hình của bạn. Cơ chế này loại bỏ nhu cầu phải liên tục thăm dò (polling) API để kiểm tra trạng thái bất đồng bộ.

## URL gọi lại Webhook (Webhook callback URL)
Để nhận thông báo webhook, bạn cần đăng ký một Webhook callback URL cho ứng dụng của mình qua endpoint [/business/webhook/update/](../12-api-reference/01-accounts-p2.md#doc-1810521279479810). URL phải dùng giao thức HTTPS và có chứng chỉ SSL hợp lệ.

## Cấu trúc dữ liệu Webhook (Webhook structure)

### Header yêu cầu (Request Headers)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| tiktok-signature | string | Chữ ký số HMAC-SHA256 mà TikTok đính kèm để máy chủ tiếp nhận xác minh nguồn gốc yêu cầu. |
| webhook-schema-version | string | Phiên bản schema của nội dung yêu cầu webhook. |
| x-tt-logid | string | Mã định danh duy nhất cho yêu cầu webhook từ TikTok. |

### Thân yêu cầu (Request Body)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| client_key | string | App ID của ứng dụng nhà phát triển trên nền tảng TikTok. |
| event | string | Tên loại sự kiện. Ví dụ: `post.publish.complete`. |
| create_time | integer | Thời điểm diễn ra sự kiện, định dạng UTC epoch tính bằng mili-giây. |
| user_openid | string | Mã định danh người dùng duy nhất của tài khoản TikTok (`open_id`). |
| content | string | Chuỗi JSON đã tuần tự hóa chứa thông tin chi tiết về sự kiện. |

---

<a id="doc-1759978319341570"></a>
<!-- doc_id: 1759978319341570 -->
<!-- doc_id: 1759978319341570 -->
# Các loại sự kiện Webhook (Webhook event types)
> Đường dẫn: Organic API > Accounts API > Guides > Webhooks > Webhook event types
TikTok cung cấp hai nhóm sự kiện Webhook chính liên quan đến tài khoản TikTok:
- **Sự kiện xuất bản bài đăng (Post publishing events)**: Kích hoạt khi các bài đăng video hoặc ảnh được xuất bản qua API, cập nhật trạng thái trong suốt vòng đời của bài đăng.
- **Sự kiện cập nhật bình luận (Comment update events)**: Kích hoạt khi có bình luận mới hoặc thay đổi đối với bình luận trên các bài đăng của tài khoản.

---

<a id="doc-1810515090228226"></a>
<!-- doc_id: 1810515090228226 -->
<!-- doc_id: 1810515090228226 -->
# Sự kiện xuất bản bài đăng (Post publishing events)
> Đường dẫn: Organic API > Accounts API > Guides > Webhooks > Webhook event types > Post publishing events
Sự kiện xuất bản bài đăng cung cấp cho bạn thông tin cập nhật theo thời gian thực về trạng thái của nội dung được đăng qua [/business/video/publish/](../12-api-reference/01-accounts-p1.md#doc-1762228496095234) hoặc [/business/photo/publish/](../12-api-reference/01-accounts-p1.md#doc-1803630424390658).

Các loại sự kiện nhận được bao gồm:
- `post.publish.failed`
- `post.publish.complete`
- `post.publish.publicly_available`
- `post.publish.no_longer_publicly_available`

## post.publish.failed
Sự kiện bắn ra khi việc xuất bản bài đăng thất bại.

### Bảng lý do thất bại (Failure reasons)

| Reason | Description |
|---|---|
| file_format_check_failed | Máy chủ TikTok không thể giải mã hoặc định dạng tệp tải lên không được hỗ trợ. |
| duration_check_failed | Thời lượng video vượt quá giới hạn tối đa hoặc ngắn hơn mức tối thiểu cho phép. |
| frame_rate_check_failed | Tốc độ khung hình (frame rate) của video không đạt tiêu chuẩn kỹ thuật. |
| picture_size_check_failed | Kích thước hoặc dung lượng hình ảnh không hợp lệ. |
| internal | Lỗi nội bộ tạm thời trên máy chủ TikTok. Vui lòng thử lại sau. |
| video_pull_failed | Máy chủ TikTok gặp lỗi kết nối mạng khi tải video từ `video_url` được cung cấp. |
| photo_pull_failed | Máy chủ TikTok gặp lỗi kết nối mạng khi tải hình ảnh từ URL được cung cấp. |
| auth_removed | Chủ tài khoản TikTok đã thu hồi quyền của ứng dụng trong lúc quá trình xuất bản đang diễn ra. |
| spam_risk_too_many_posts | Tài khoản đăng quá nhiều bài trong một khoảng thời gian ngắn, bị tạm chặn do chống spam. |
| spam_risk_user_banned_from_posting | Tài khoản TikTok hiện đang bị khóa tính năng đăng bài do vi phạm tiêu chuẩn cộng đồng. |
| spam_risk_text | Tiêu đề hoặc mô tả bài đăng chứa từ khóa rủi ro hoặc vi phạm chính sách spam. |
| spam_risk | Hệ thống phát hiện rủi ro spam cao đối với bài đăng này và từ chối xuất bản. |
| publish_cancelled | Quá trình tải lên hoặc xử lý xuất bản bài đăng đã được hủy bỏ thành công. |

Trong nội dung payload của sự kiện:
- `publish_id`: Mã định danh yêu cầu xuất bản.
- `reason`: Lý do chi tiết khiến bài đăng thất bại.

## post.publish.complete
Sự kiện bắn ra khi video hoặc ảnh đã được xử lý xong trên hệ thống TikTok.
Payload bao gồm `publish_id`.

## post.publish.publicly_available
Sự kiện bắn ra khi bài đăng chính thức được duyệt và hiển thị công khai tới người xem trên TikTok.
Payload bao gồm `publish_id`.

## post.publish.no_longer_publicly_available
Sự kiện bắn ra khi một bài đăng công khai trước đó không còn hiển thị công khai nữa (ví dụ bị ẩn hoặc chuyển sang chế độ riêng tư).
Payload bao gồm `publish_id`.

---

<a id="doc-1810515104773122"></a>
<!-- doc_id: 1810515104773122 -->
<!-- doc_id: 1810515104773122 -->
# Sự kiện cập nhật bình luận (Comment update event)
> Đường dẫn: Organic API > Accounts API > Guides > Webhooks > Webhook event types > Comment update event
Danh mục cập nhật bình luận bao gồm sự kiện `comment.update`.

Sự kiện `comment.update` được kích hoạt trong vòng 5 phút kể từ khi một bình luận hoặc câu trả lời được tạo mới, xóa bỏ, hoặc khi trạng thái hiển thị của bình luận bị thay đổi trên bất kỳ bài đăng ảnh hoặc video công khai nào của tài khoản TikTok sở hữu.

### Nội dung sự kiện (Event content)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| comment_id | number | Mã định danh duy nhất của bình luận hoặc câu trả lời bình luận. |
| video_id | number | Mã định danh duy nhất của bài đăng TikTok sở hữu có bình luận. |
| parent_comment_id | number | Chỉ trả về đối với câu trả lời bình luận: ID của bình luận cấp cha. |
| comment_type | string | Loại bình luận: `comment` hoặc `reply`. |
| comment_action | string | Hành động được thực hiện: `create`, `delete`, `hide`, `unhide`. |
| timestamp | number | Thời gian Unix epoch tính bằng mili-giây khi hành động diễn ra. |
| unique_identifier | string | Mã định danh duy nhất toàn cầu gán cho mỗi người dùng bình luận. |

---

<a id="doc-1759978341579777"></a>
<!-- doc_id: 1759978341579777 -->
<!-- doc_id: 1759978341579777 -->
# Xác minh chữ ký Webhook (Webhook verification)
> Đường dẫn: Organic API > Accounts API > Guides > Webhooks > Webhook verification
Tài liệu này hướng dẫn cách thực hiện xác minh chữ ký bảo mật cho các yêu cầu Webhook từ TikTok.

## Kiểm tra chữ ký (Check the signature)
Các webhook của TikTok được gửi kèm theo chữ ký trong header `tiktok-signature` mà máy chủ tiếp nhận có thể sử dụng để xác minh tính hợp pháp của yêu cầu, đảm bảo sự kiện bắt nguồn từ TikTok chứ không phải từ bên thứ ba độc hại.

Chúng tôi **khuyến nghị mạnh mẽ** rằng các hệ thống tiếp nhận webhook phải xác minh chữ ký này trước khi xử lý bất kỳ sự kiện nào.

## Quy trình xác minh chữ ký tin nhắn (Verify Message Signature)
Để bảo vệ ứng dụng trước các cuộc tấn công trung gian (man-in-the-middle) và tấn công gửi lại (replay attack):
1. Trích xuất chữ ký từ header `tiktok-signature`.
2. Trích xuất dấu thời gian `create_time` từ thân JSON của webhook.
3. Sử dụng khóa bí mật ứng dụng (`client_secret`) của bạn để tạo mã băm HMAC-SHA256 trên chuỗi kết hợp nội dung body và timestamp.
4. So sánh mã băm tạo được với chữ ký nhận được. Nếu trùng khớp, yêu cầu là hợp lệ.

---

<a id="doc-1776983576127490"></a>
<!-- doc_id: 1776983576127490 -->
<!-- doc_id: 1776983576127490 -->
# Câu hỏi thường gặp (FAQs)
> Đường dẫn: Organic API > Accounts API > Guides > FAQs
Tài liệu này tổng hợp các câu hỏi thường gặp khi tích hợp và sử dụng Accounts API.

## Dữ liệu không đầy đủ (Data incompleteness)
**Hỏi: Khi tôi đặt `start_date` về một ngày trong quá khứ khi gọi [/business/get/](../12-api-reference/01-accounts-p1.md#doc-1762228399168514), tại sao một số trường chỉ số trả về giá trị 0 hoặc thiếu dữ liệu?**

Trả lời: TikTok chỉ bắt đầu ghi nhận dữ liệu phân tích chi tiết kể từ thời điểm tài khoản TikTok được chuyển đổi sang Tài khoản Doanh nghiệp hoặc được cấp Quyền truy cập Nâng cao (Advanced Access). Dữ liệu lịch sử trước thời điểm đó sẽ không khả dụng.

## Sai lệch dữ liệu (Data discrepancy)
**Hỏi: Tại sao số liệu trên ứng dụng TikTok di động và số liệu trả về từ API lại có sự chênh lệch?**

Trả lời: Sự chênh lệch thường bắt nguồn từ độ trễ dữ liệu ngoại tuyến (từ 24 đến 48 giờ) đối với các số liệu tương tác như lượt thích, lượt xem trang cá nhân, và sự khác biệt về múi giờ báo cáo (API sử dụng múi giờ UTC).

---

<a id="doc-1740304387032066"></a>
<!-- doc_id: 1740304387032066 -->
<!-- doc_id: 1740304387032066 -->
# Danh mục API tham chiếu (API reference)
> Đường dẫn: Organic API > Accounts API > API reference
Tài khoản TikTok là một hồ sơ số hợp nhất trên nền tảng TikTok cho phép các cá nhân, nhà sáng tạo và thương hiệu tạo nội dung đa phương tiện, tương tác với cộng đồng toàn cầu và tiến hành thương mại xã hội.

Phân hệ Accounts API bao gồm các nhóm endpoint sau:

## Xác thực và thông tin người dùng
* [Lấy thông tin người dùng doanh nghiệp TikTok](../12-api-reference/01-accounts-p1.md#doc-1762228399168514)
* [Lấy thông tin token và quyền hạn đã ủy quyền](../12-api-reference/01-accounts-p1.md#doc-1765927978092545)

## Quản lý video và bài đăng
* [Lấy danh sách video của tài khoản TikTok](../12-api-reference/01-accounts-p1.md#doc-1762228421622786)
* [Khởi tạo phiên tải video](../12-api-reference/44-files.md#doc-1737721229896705)
* [Tải lên khối dữ liệu video](../12-api-reference/44-files.md#doc-1737721489945601)
* [Xuất bản bài đăng video](../12-api-reference/01-accounts-p1.md#doc-1762228496095234)
* [Xuất bản bài đăng ảnh](../12-api-reference/01-accounts-p1.md#doc-1803630424390658)

## Quản lý bình luận
* [Tạo bình luận mới](../12-api-reference/01-accounts-p1.md#doc-1762228442072066)
* [Trả lời bình luận](../12-api-reference/01-accounts-p1.md#doc-1762228448779266)
* [Thích bình luận](../12-api-reference/01-accounts-p1.md#doc-1762228456608770)
* [Bỏ thích bình luận](../12-api-reference/01-accounts-p1.md#doc-1762228456608770)
* [Ẩn bình luận](../12-api-reference/01-accounts-p1.md#doc-1762228474532865)
* [Bỏ ẩn bình luận](../12-api-reference/01-accounts-p1.md#doc-1762228474532865)
* [Xóa bình luận](../12-api-reference/01-accounts-p1.md#doc-1762228483080193)
* [Lấy danh sách bình luận](../12-api-reference/01-accounts-p1.md#doc-1760232109619202)
* [Lấy danh sách câu trả lời của bình luận](../12-api-reference/01-accounts-p1.md#doc-1762228430145538)

## Quản lý ủy quyền bài đăng và thuộc tính URL
* [Tạo mã ủy quyền quảng cáo cho bài đăng](../12-api-reference/01-accounts-p2.md#doc-1815051784582210)
* [Gia hạn mã ủy quyền quảng cáo cho bài đăng](../12-api-reference/01-accounts-p2.md#doc-1815051741912066)
* [Xóa mã ủy quyền quảng cáo cho bài đăng](../12-api-reference/01-accounts-p2.md#doc-1815051817073665)
* [Lấy danh sách mã ủy quyền quảng cáo](../12-api-reference/01-accounts-p2.md#doc-1815051801257986)
* [Thêm thuộc tính URL](../12-api-reference/01-accounts-p2.md#doc-1769325280876545)
* [Xác minh thuộc tính URL](../12-api-reference/01-accounts-p2.md#doc-1769325308162050)
* [Cấu hình Webhook cho tài khoản](../12-api-reference/01-accounts-p2.md#doc-1810521279479810)

---

## Hướng dẫn thực hành Data Retrieval (Python & cURL)

Dưới đây là mã nguồn mẫu minh họa quy trình gọi API thực tế cho phân hệ **Organic API — Accounts API**:

### cURL mẫu
```bash
curl -s -X GET "https://business-api.tiktok.com/open_api/v1.3/business/get/?business_id=YOUR_OPEN_ID&fields=["username","display_name","profile_image","follower_count"]"   -H "Access-Token: YOUR_ACCESS_TOKEN"
```

### Python script mẫu
```python
import requests
import json

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
BUSINESS_ID = "YOUR_OPEN_ID"
BASE_URL = "https://business-api.tiktok.com/open_api/v1.3"

headers = {
    "Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}

def get_account_info():
    url = f"{BASE_URL}/business/get/"
    params = {
        "business_id": BUSINESS_ID,
        "fields": json.dumps(["username", "display_name", "profile_image", "follower_count"])
    }
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    if data.get("code") == 0:
        print("Lấy thông tin tài khoản thành công:", data.get("data"))
        return data.get("data")
    else:
        print(f"Lỗi: {data.get('code')} - {data.get('message')}")
        return None

if __name__ == "__main__":
    get_account_info()
```
