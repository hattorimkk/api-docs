# Business Messaging API

> Phân hệ: guide:Business Messaging API.
> Tài liệu biên dịch kỹ thuật chi tiết theo chuẩn TikTok Business API v1.3.

---

## Mục lục điều hướng
- [1. Phân hệ Business Messaging API (#doc-1832183871604753)](#doc-1832183871604753)
- [2. Tổng quan (Overview) (#doc-1832184079395841)](#doc-1832184079395841)
- [3. Hướng dẫn (Guides) (#doc-1832184100272338)](#doc-1832184100272338)
- [4. Bắt đầu (Get started) (#doc-1832184116746305)](#doc-1832184116746305)
- [5. Đăng ký quyền truy cập API (#doc-1832184145137922)](#doc-1832184145137922)
- [6. Kiểm duyệt an toàn dữ liệu và quyền riêng tư (#doc-1832184206708737)](#doc-1832184206708737)
- [7. Kiểm duyệt an ninh dữ liệu thị trường Hoa Kỳ (#doc-1832184219753474)](#doc-1832184219753474)
- [8. Ủy quyền tài khoản (Authorization) (#doc-1832184159540418)](#doc-1832184159540418)
- [9. Xác thực (Authentication) (#doc-1832184175482945)](#doc-1832184175482945)
- [10. Quản lý tin nhắn trực tiếp cho tài khoản TikTok (#doc-1832184236919810)](#doc-1832184236919810)
- [11. Hạn mức gửi tin nhắn của API (#doc-1854823717597185)](#doc-1854823717597185)
- [12. Quản lý tin nhắn tự động (#doc-1832184250237954)](#doc-1832184250237954)
- [13. Quản lý tin nhắn chào mừng (Welcome message) (#doc-1832184264385538)](#doc-1832184264385538)
- [14. Quản lý câu hỏi gợi ý (Suggested questions) (#doc-1832184277518338)](#doc-1832184277518338)
- [15. Quản lý nút gợi ý trò chuyện (Chat prompts) (#doc-1832184291198977)](#doc-1832184291198977)
- [16. Quản lý tin nhắn cho người theo dõi mới (New follower message) (#doc-1877104214073346)](#doc-1877104214073346)
- [17. Khởi tạo hội thoại qua liên kết ngắn & quảng cáo (#doc-1839594049581249)](#doc-1839594049581249)
- [18. Bảng mã lỗi trả về (Return codes) (#doc-1832184306529874)](#doc-1832184306529874)
- [19. Danh mục endpoint API (API Reference) (#doc-1832184321030145)](#doc-1832184321030145)

---

<a id="doc-1832183871604753"></a>
<!-- doc_id: 1832183871604753 -->
<!-- doc_id: 1832183871604753 -->
# Business Messaging API
> Đường dẫn: Business Messaging API
TikTok Business Messaging API là bộ giao diện lập trình cho phép các tài khoản TikTok doanh nghiệp đã được ủy quyền gửi/nhận tin nhắn trực tiếp với người dùng TikTok thông qua các nền tảng tích hợp. Bộ API này giúp doanh nghiệp kết hợp liền mạch tính năng nhắn tin thời gian thực vào chiến lược chăm sóc khách hàng, hỗ trợ chuyển đổi từ tương tác tự nhiên sang quảng cáo trả phí và gia tăng sự hiện diện thương hiệu.

> **Lưu ý:**
> TikTok Business Messaging API hiện đang trong giai đoạn **Open Beta tại APAC, LATAM, METAP và Bắc Mỹ**. Để tìm hiểu thêm về tính khả dụng theo khu vực, hãy xem [Đăng ký quyền truy cập API](business-messaging-api.md#doc-1832184145137922).

Khám phá tài liệu:

- Bắt đầu
	- [Tổng quan](business-messaging-api.md#doc-1832184079395841): Làm quen với các thuật ngữ và khái niệm thiết yếu.
	- [Đăng ký quyền truy cập API](business-messaging-api.md#doc-1832184145137922): Đảm bảo bạn đã hoàn thành các bước đánh giá an ninh dữ liệu và quyền riêng tư để được cấp quyền gọi API.
	- [Ủy quyền tài khoản](business-messaging-api.md#doc-1832184159540418): Nắm vững quy trình xin cấp quyền từ doanh nghiệp để quản lý tài khoản TikTok của họ.
	- [Xác thực](business-messaging-api.md#doc-1832184175482945): Làm chủ quy trình cấp phát access token và cơ chế làm mới token.
- Triển khai kỹ thuật
	- [Đăng ký nhận sự kiện Webhook tin nhắn qua Webhooks API](../08-use-cases/use-case-webhook.md#doc-1832190670631937): Thực hiện theo hướng dẫn để thiết lập thông báo tin nhắn thời gian thực.
	- [Quản lý tin nhắn trực tiếp cho tài khoản TikTok](business-messaging-api.md#doc-1832184236919810): Tìm hiểu cách gửi, nhận và quản lý các cuộc trò chuyện trực tiếp.
	- [Quản lý tin nhắn chào mừng (Welcome message)](business-messaging-api.md#doc-1832184264385538): Nắm rõ cách tạo và cập nhật tin nhắn chào mừng tự động khi người dùng bắt đầu nhắn tin.
	- [Quản lý câu hỏi gợi ý (Suggested questions)](business-messaging-api.md#doc-1832184277518338): Khám phá cách thiết lập và quản lý danh sách câu hỏi gợi ý để tối ưu hóa tương tác.
	- [Quản lý nút gợi ý trò chuyện (Chat prompts)](business-messaging-api.md#doc-1832184291198977): Khám phá cách tạo và quản lý nút gợi ý để định hướng cuộc trò chuyện của người dùng.
	- [Danh mục endpoint API](business-messaging-api.md#doc-1832184321030145): Tham khảo toàn diện tất cả các endpoint của Business Messaging API.
- Tài nguyên tham khảo
	- [Bảng mã lỗi trả về](business-messaging-api.md#doc-1832184306529874): Tra cứu các mã lỗi thường gặp khi gọi Business Messaging API.

---

<a id="doc-1832184079395841"></a>
<!-- doc_id: 1832184079395841 -->
<!-- doc_id: 1832184079395841 -->
# Tổng quan (Overview)
> Đường dẫn: Business Messaging API > Overview
Nhắn tin là một phần thiết yếu trong cách doanh nghiệp duy trì hiện diện và giao thương với người dùng trên các nền tảng mạng xã hội. Business Messaging API là bộ giao diện lập trình cho phép các tài khoản TikTok doanh nghiệp đã được ủy quyền trao đổi tin nhắn trực tiếp với người dùng TikTok thông qua các nền tảng tích hợp API. Bộ công cụ này giúp doanh nghiệp tích hợp liền mạch dịch vụ nhắn tin tức thì vào chiến lược gắn kết khách hàng, hỗ trợ cách tiếp cận từ tự nhiên sang trả phí và nâng cao hình ảnh thương hiệu trên TikTok.

Thông qua việc tối ưu hóa quản lý tin nhắn và phản hồi tự động trên các nền tảng của bên thứ ba, API này trao quyền cho các nhà phát triển xây dựng các giải pháp toàn diện thúc đẩy tăng trưởng thương hiệu trên TikTok, kết nối hiệu quả giữa tương tác tự nhiên và các chiến dịch quảng cáo trả phí.

## Các khái niệm cốt lõi (Concepts)
- **Conversation (Cuộc trò chuyện / Hội thoại)**: Toàn bộ quá trình trao đổi giữa hai hoặc nhiều người tham gia. Hội thoại là luồng tin nhắn liên tục bao gồm toàn bộ quá trình trao đổi qua lại giữa người dùng và doanh nghiệp, được định danh bằng một ID hội thoại duy nhất (`conversation_id`).
- **Message (Tin nhắn)**: Một thông điệp đơn lẻ được gửi từ một bên tham gia tới bên kia trong cuộc hội thoại.

---

<a id="doc-1832184100272338"></a>
<!-- doc_id: 1832184100272338 -->
<!-- doc_id: 1832184100272338 -->
# Hướng dẫn (Guides)
> Đường dẫn: Business Messaging API > Guides
Các hướng dẫn này sẽ dẫn dắt bạn qua quy trình đăng ký, tích hợp và các tài nguyên quan trọng của Business Messaging API:
- [Bắt đầu (Get started)](business-messaging-api.md#doc-1832184116746305)
  - [Đăng ký quyền truy cập API](business-messaging-api.md#doc-1832184145137922)
  - [Ủy quyền tài khoản (Authorization)](business-messaging-api.md#doc-1832184159540418)
  - [Đăng ký nhận sự kiện Webhook qua Webhooks API](../08-use-cases/use-case-webhook.md#doc-1832190670631937)
  - [Xác thực (Authentication)](business-messaging-api.md#doc-1832184175482945)
- [Quản lý tin nhắn trực tiếp cho tài khoản TikTok](business-messaging-api.md#doc-1832184236919810)
- [Quản lý tin nhắn tự động](business-messaging-api.md#doc-1832184250237954)
- [Bảng mã lỗi trả về (Return codes)](business-messaging-api.md#doc-1832184306529874)

---

<a id="doc-1832184116746305"></a>
<!-- doc_id: 1832184116746305 -->
<!-- doc_id: 1832184116746305 -->
# Bắt đầu (Get started)
> Đường dẫn: Business Messaging API > Guides > Get started
Chào mừng bạn đến với Business Messaging API! Với trọng tâm tối ưu cho nhà phát triển, quy trình tiếp cận và sử dụng API được tinh gọn chỉ trong vài bước cơ bản.

## Quy trình từng bước (Step by step workflow)
Nếu bạn là nhà phát triển mới, vui lòng hoàn thành các bước sau trước khi thực hiện lệnh gọi API đầu tiên:
1. [Tạo tài khoản TikTok For Business](../04-get-started/bat-dau.md#doc-1738855099573250).
2. [Đăng ký làm nhà phát triển](../04-get-started/bat-dau.md#doc-1738855176671234).
3. [Tạo ứng dụng nhà phát triển](../04-get-started/bat-dau.md#doc-1738855242728450).
4. [Đăng ký và nhận quyền truy cập Business Messaging API](business-messaging-api.md#doc-1832184145137922).
5. [Ủy quyền tài khoản (Authorization)](business-messaging-api.md#doc-1832184159540418).
6. [Đăng ký nhận sự kiện Webhook tin nhắn qua Webhooks API](../08-use-cases/use-case-webhook.md#doc-1832190670631937).
7. [Xác thực và lấy token (Authentication)](business-messaging-api.md#doc-1832184175482945).
8. Thực hiện lệnh gọi API đầu tiên của bạn.

## Danh mục endpoint API
Để tìm hiểu về tất cả các endpoint khả dụng, hãy xem [Danh mục API Reference cho Business Messaging API](../12-api-reference/23-business-messaging.md#doc-1832184349193282).

## Giới hạn tần suất gọi (Rate limits)
Hạn mức tần suất (Rate limit) cho các endpoint Business Messaging API là 10 truy vấn/giây (QPS).

## Mã lỗi trả về (Return codes)
Để tìm hiểu các mã lỗi trả về khi gọi thất bại, xem [Bảng mã lỗi trả về của Business Messaging API](business-messaging-api.md#doc-1832184306529874).

---

<a id="doc-1832184145137922"></a>
<!-- doc_id: 1832184145137922 -->
<!-- doc_id: 1832184145137922 -->
# Đăng ký quyền truy cập API (Access to Business Messaging API)
> Đường dẫn: Business Messaging API > Guides > Get started > Access to Business Messaging API
TikTok Business Messaging API cho phép các tài khoản TikTok gửi và nhận tin nhắn trực tiếp với người dùng TikTok trên các nền tảng tích hợp API. Tính năng này giúp các doanh nghiệp nâng cao mức độ tương tác với khách hàng và tinh gọn quy trình nhắn tin thông qua các giải pháp của bên thứ ba.

Để đảm bảo tuân thủ dữ liệu với các tiêu chuẩn bảo mật và quyền riêng tư toàn cầu của TikTok, đồng thời giảm thiểu rủi ro từ bên thứ ba, các nhà phát triển Business Messaging API bắt buộc phải hoàn thành các bước kiểm duyệt an ninh như một điều kiện tiên quyết để được cấp quyền truy cập API.

## Phạm vi khả dụng theo khu vực và các đánh giá bắt buộc
- Business Messaging API hiện chưa khả dụng tại Khu vực Kinh tế Châu Âu (EEA), Thụy Sĩ và Vương quốc Anh (UK). Đối với các tài khoản TikTok đăng ký tại các khu vực này, nhà phát triển không thể gọi Business Messaging API thay mặt cho tài khoản. Ngoài ra, tin nhắn trực tiếp gửi từ các tài khoản tại các khu vực này không thể truy xuất qua API hoặc Webhook.
- Đối với các tài khoản TikTok đăng ký tại Hoa Kỳ (US), chỉ những nhà phát triển đã vượt qua [Kiểm duyệt an toàn dữ liệu và quyền riêng tư (DSPR)](business-messaging-api.md#doc-1832184206708737), [Kiểm duyệt an ninh dữ liệu Hoa Kỳ (USDS)](business-messaging-api.md#doc-1832184219753474), và đồng ý với Phụ lục USDS Addendum mới được phép gọi Business Messaging API thay mặt cho các tài khoản này. TikTok sẽ chủ động gửi email cho các nhà phát triển đã vượt qua bước kiểm duyệt USDS để ký kết phụ lục.
- Đối với Tài khoản Doanh nghiệp đăng ký tại tất cả các khu vực khác trên thế giới (Rest of World), nhà phát triển đã vượt qua [Kiểm duyệt an toàn dữ liệu và quyền riêng tư](business-messaging-api.md#doc-1832184206708737) sẽ được phép gọi Business Messaging API thay mặt cho các tài khoản đó.
- Tính khả dụng của các tính năng cụ thể trong Business Messaging API có thể khác nhau tùy từng khu vực. Vui lòng tham khảo tài liệu API chi tiết.

## Phạm vi quyền hạn và quy trình kiểm duyệt
- Trước khi bắt đầu nộp đơn xin cấp quyền Business Messaging API, hãy đảm bảo:
  - Bạn đã có ứng dụng nhà phát triển được phê duyệt và có App ID hợp lệ. Nếu chưa có, bạn có thể nộp đơn tạo ứng dụng mới và chọn các phạm vi quyền hạn "**Ad Account Management**", "**CTX Events Management**" và "**Measurement**".
  - Bạn đã đọc kỹ tài liệu [Kiểm duyệt an toàn dữ liệu và quyền riêng tư](business-messaging-api.md#doc-1832184206708737).
  - Bạn đã đọc kỹ tài liệu [Kiểm duyệt an ninh dữ liệu thị trường Hoa Kỳ](business-messaging-api.md#doc-1832184219753474), nếu bạn dự định truy cập Business Messaging API để quản lý tin nhắn cho tài khoản TikTok đăng ký tại Mỹ.

## Biểu mẫu đăng ký kiểm duyệt an toàn dữ liệu và quyền riêng tư
- **Vui lòng bắt đầu đăng ký bằng cách gửi thông tin qua** [biểu mẫu này](https://bytedance.sg.larkoffice.com/share/base/form/shrlg7vFArGhg9V20neYCEwIKrb).
- Đội ngũ TikTok API for Business sẽ xử lý yêu cầu và bắt đầu quy trình đánh giá trong vòng 10 ngày làm việc sau khi bạn nộp đơn.
- Đối với Đánh giá An toàn Dữ liệu & Quyền riêng tư (DSPR), một email với tiêu đề "**TikTok/ByteDance Third-Party Due Diligence Questionnaire**" ("DSPR DDQ") sẽ được gửi tới địa chỉ email của người liên hệ được cung cấp.
  - Nếu áp dụng Đánh giá An ninh Dữ liệu Hoa Kỳ (USDS), một email với tiêu đề "**A questionnaire request from TikTok U.S. Data Security Inc.**" ("USDS VAQ") sẽ được gửi tới địa chỉ email liên hệ. Bảng câu hỏi này thường được gửi sau DSPR DDQ khoảng một tuần.
**Lưu ý**: USDS VAQ là thủ tục quan trọng nhất đối với các nhà phát triển có ý định quản lý tài khoản TikTok đăng ký tại Mỹ. **Vui lòng ưu tiên hoàn thành và nộp đúng hạn** được nêu trong email, vì kết quả đánh giá sẽ quyết định việc cấp phép truy cập dữ liệu người dùng TikTok tại Mỹ của bạn.

## Câu hỏi thường gặp (FAQs)
**Hỏi: Thị trường mục tiêu hiện tại của tôi là APAC, LATAM và METAP. Tôi có nên đưa cả Hoa Kỳ vào đơn đăng ký ngay bây giờ để đón đầu việc phục vụ các tài khoản Mỹ trong tương lai không?**

Trả lời: Việc đưa Hoa Kỳ vào đơn đăng ký sẽ yêu cầu công ty bạn phải trải qua thêm quy trình kiểm duyệt an ninh dữ liệu Hoa Kỳ (USDS), điều này có thể kéo dài tổng thời gian xét duyệt. Nếu các tài khoản bạn dự định quản lý hiện đăng ký ngoài nước Mỹ, chúng tôi khuyến nghị bạn không chọn thị trường Mỹ trong đơn này để đẩy nhanh tốc độ phê duyệt. Bạn hoàn toàn có thể nộp đơn bổ sung thị trường Mỹ và hoàn thành kiểm duyệt USDS sau này khi doanh nghiệp có nhu cầu.

**Hỏi: Tôi cần chuẩn bị những gì để đẩy nhanh tiến độ kiểm duyệt an toàn dữ liệu và kiểm duyệt USDS?**

Trả lời: Để quá trình diễn ra nhanh chóng, hãy hoàn thành và nộp bảng câu hỏi DSPR DDQ (và USDS VAQ nếu có) ngay khi bạn nhận được. Khi điền bảng câu hỏi, hãy cung cấp câu trả lời chi tiết kèm theo các tài liệu chứng minh liên quan, chẳng hạn như chứng chỉ ISO 27001, báo cáo SOC 2, hoặc báo cáo quét lỗ hổng/kiểm thử xâm nhập (penetration testing) gần nhất. Sau khi nộp, hãy thường xuyên kiểm tra hòm thư của người liên hệ để phản hồi kịp thời các câu hỏi tiếp theo từ TikTok nếu có.

**Hỏi: Tôi có thể theo dõi tiến độ xét duyệt an toàn dữ liệu và USDS không?**

Trả lời: Hiện tại, cả hai quy trình xét duyệt đều được thực hiện thủ công bởi TikTok và chưa hỗ trợ theo dõi tiến độ trực tiếp trên cổng nhà phát triển dành cho tài khoản tự phục vụ. Nếu ứng dụng của bạn được phê duyệt mà không cần tài liệu bổ sung, bạn sẽ nhận được thông báo qua email. Lưu ý rằng hệ thống ticket hỗ trợ nhà phát triển chỉ dành cho sự cố kỹ thuật và không dùng để tra cứu trạng thái xét duyệt.

**Hỏi: Tôi phải làm gì nếu bị từ chối trong đợt kiểm duyệt USDS? Tôi có còn dùng được Business Messaging API không?**

Trả lời: Để tránh bị từ chối, hãy trả lời thật chi tiết trong bản USDS VAQ và phản hồi nhanh chóng các email tiếp theo. Nếu không vượt qua kiểm duyệt USDS, đội ngũ TikTok API for Business sẽ gửi email hỏi xem bạn có muốn tiếp tục quy trình Đánh giá An toàn Dữ liệu & Quyền riêng tư thông thường hay không. Nếu tiếp tục và được phê duyệt, bạn vẫn có thể sử dụng Business Messaging API cho các tài khoản TikTok đăng ký ngoài nước Mỹ.

**Hỏi: Điều gì sẽ xảy ra nếu tôi cố gắng quản lý tin nhắn trực tiếp cho các tài khoản TikTok đăng ký tại EEA, Thụy Sĩ, Vương quốc Anh hoặc Hoa Kỳ (khi chưa vượt qua kiểm duyệt USDS)?**

Trả lời: Trong trường hợp này, mặc dù chủ tài khoản TikTok có thể đã phê duyệt cấp quyền cho ứng dụng của bạn, nhưng ứng dụng sẽ không thể truy xuất hoặc tương tác với bất kỳ dữ liệu liên quan nào qua Business Messaging API. Mọi lượt gọi API sẽ thất bại và trả về lỗi, ngay cả khi quá trình ủy quyền về mặt kỹ thuật đã thành công.

**Hỏi: Khu vực được xác định như thế nào và tôi nên thông báo các khu vực khả dụng cho người dùng ra sao?**

Trả lời: Khu vực được xác định dựa trên địa điểm đăng ký ban đầu của tài khoản trên TikTok. Các phê duyệt kiểm duyệt của bạn sẽ quyết định phạm vi khu vực mà tích hợp của bạn được hỗ trợ. Trong các thông điệp tiếp thị, bạn có thể thông báo: "Tính năng TikTok Business Messaging khả dụng cho mọi tài khoản TikTok ngoại trừ các tài khoản đăng ký tại Hoa Kỳ, Khu vực Kinh tế Châu Âu, Thụy Sĩ và Vương quốc Anh". Bạn có thể bỏ đoạn "Hoa Kỳ" nếu đã vượt qua kiểm duyệt an ninh USDS.

**Hỏi: Tài khoản TikTok Cá nhân (General Account) có thể quản lý tin nhắn qua Business Messaging API không? Và VBA là gì?**

Trả lời: Business Messaging API chỉ hỗ trợ Tài khoản TikTok có Quyền truy cập Nâng cao (Advanced Access) hoặc Tài khoản Doanh nghiệp Đã xác minh (VBA - Verified Business Account). Tài khoản Cá nhân thông thường không đủ điều kiện, nhưng người dùng có thể nâng cấp cấp độ quyền hạn cho tài khoản của mình. Tìm hiểu thêm [về quyền hạn tài khoản TikTok](https://ads.tiktok.com/resources/help/article/about-tiktok-account-entitlements). Chúng tôi khuyến nghị nâng cấp lên VBA để mở khóa thêm nhiều công cụ và tính năng hữu ích.

**Hỏi: Tôi có thể quản lý đồng thời cả Tin nhắn trực tiếp TikTok và Tin nhắn TikTok Shop bằng Business Messaging API không?**

Trả lời: TikTok Business Messaging và TikTok Shop Messaging là hai hệ sinh thái nhắn tin tách biệt hoàn toàn. Tích hợp với TikTok Business Messaging API không hỗ trợ quản lý tin nhắn của TikTok Shop.

---

<a id="doc-1832184206708737"></a>
<!-- doc_id: 1832184206708737 -->
<!-- doc_id: 1832184206708737 -->
# Kiểm duyệt an toàn dữ liệu và quyền riêng tư (Data security and privacy review)
> Đường dẫn: Business Messaging API > Guides > Get started > Access to Business Messaging API > Data security and privacy review
## Bảo vệ dữ liệu khách hàng
TikTok, cũng như nhiều tổ chức toàn cầu khác, luôn đối mặt với các nguy cơ an ninh mạng và cam kết bảo vệ tuyệt đối dữ liệu của người dùng. Việc giữ an toàn cho dữ liệu, hệ thống và tài sản số trước các mối đe dọa an ninh mạng là ưu tiên hàng đầu, và sự cẩn trọng này được áp dụng nghiêm ngặt đối với tất cả các nhà cung cấp dịch vụ bên thứ ba.

Do tính chất nhạy cảm của dữ liệu tin nhắn trực tiếp, TikTok áp dụng quy trình thẩm định nâng cao đối với các nhà phát triển sẽ xử lý tin nhắn thay mặt cho người dùng tài khoản TikTok. Điều này đồng nghĩa với việc TikTok phải xác minh việc truy cập, xử lý và/hoặc lưu trữ Dữ liệu được bảo vệ, vị trí trụ sở chính, tỷ lệ sở hữu nước ngoài, địa điểm làm việc của nhân sự, vị trí đặt máy chủ hệ thống và việc sử dụng các nhà thầu phụ của nhà phát triển.

## Kỳ vọng của chúng tôi đối với nhà phát triển
Trước khi được cấp phạm vi quyền hạn Business Messaging cho ứng dụng, tất cả các nhà phát triển tiềm năng phải hoàn thành Đánh giá An toàn Dữ liệu và Quyền riêng tư ("DSPR"). Đánh giá này đo lường mức độ hoàn thiện của các quy trình bảo mật và quyền riêng tư của nhà phát triển, đảm bảo họ tuân thủ cả quy định pháp lý hiện hành lẫn tiêu chuẩn của TikTok trước khi tiếp cận dữ liệu khách hàng.

### Quyền riêng tư (Privacy)
Việc tuân thủ luật bảo vệ quyền riêng tư và các tiêu chuẩn ngành là bắt buộc đối với mọi bên liên quan trong hệ sinh thái TikTok Business Messaging. Mục tiêu của chúng tôi là xây dựng một hệ sinh thái an toàn hàng đầu để bảo vệ toàn diện dữ liệu thông qua việc công khai minh bạch và áp dụng các biện pháp bảo vệ trong suốt vòng đời dữ liệu (thu thập, lưu trữ, xử lý, truyền tải và hủy bỏ).

Các cơ chế quyền riêng tư dưới đây là bắt buộc để tuân thủ các đạo luật khu vực (như GDPR và CPRA), tiêu chuẩn ngành và quy định quản trị dữ liệu nội bộ. Việc không tuân thủ có thể dẫn đến các chế tài pháp lý nghiêm trọng và/hoặc bị thu hồi quyền truy cập API.

### Vai trò và trách nhiệm chuyên trách
Trong tổ chức của bạn, phải có cá nhân chịu trách nhiệm giám sát việc tuân thủ quyền riêng tư dữ liệu để đảm bảo dữ liệu cá nhân được xử lý và bảo vệ đúng cách, đồng thời là đầu mối liên hệ cho các yêu cầu liên quan. Một số khu vực pháp lý yêu cầu bắt buộc phải có Cán bộ Bảo vệ Dữ liệu (DPO).

### Thông báo quyền riêng tư (Privacy notice)
Chính sách quyền riêng tư phải giải thích rõ ràng từng khía cạnh trong vòng đời dữ liệu: dữ liệu nào được thu thập (**what**), lý do thu thập (**why**), cách sử dụng (**how**), nơi dữ liệu được truyền tới (**where**), cách bảo vệ (**how**) và thời gian lưu trữ (**how long**).

### Quyền của chủ thể dữ liệu (Data subject rights)
Chủ thể dữ liệu có quyền **kiểm soát dữ liệu của họ**, bao gồm quyền truy cập, tải xuống, chỉnh sửa và yêu cầu xóa dữ liệu. Nhà phát triển phải có khả năng hỗ trợ chủ tài khoản TikTok thực thi các quyền này khi có yêu cầu.

### Thời gian lưu giữ dữ liệu (Data retention)
Dữ liệu cá nhân **không được phép lưu giữ** lâu hơn mức cần thiết để thực hiện mục đích thu thập và xử lý ban đầu. Khi chủ tài khoản TikTok ngừng cấp quyền chia sẻ dữ liệu cho nhà phát triển, nhà phát triển phải xóa dữ liệu cá nhân đó một cách kịp thời.

### Giảm thiểu dữ liệu (Data minimization)
Nhà phát triển chỉ được yêu cầu hoặc truy cập **lượng dữ liệu tối thiểu** cần thiết cho dịch vụ mà mình cung cấp. Để đạt được điều này, nhà phát triển chỉ nên yêu cầu quyền truy cập vào các API phục vụ trực tiếp cho mục đích nghiệp vụ cụ thể.

### An ninh mạng (Security)
Bảo mật là nền tảng cho mọi quá trình truyền tải dữ liệu. Nhà phát triển bắt buộc phải có các biện pháp kiểm soát kỹ thuật và tổ chức phù hợp để bảo vệ dữ liệu nhạy cảm của người dùng, duy trì niềm tin và tuân thủ pháp luật.

### Chính sách an toàn thông tin
Nhà phát triển phải có khung chính sách an toàn thông tin rõ ràng làm cơ sở vận hành hàng ngày. Chính sách cần được rà soát định kỳ, cập nhật và phê duyệt bởi ban lãnh đạo cấp cao để đảm bảo các biện pháp bảo mật được thực thi xuyên suốt tổ chức.

### An ninh mạng nội bộ (Network security)
Nhà phát triển phải phân vùng môi trường mạng để bảo vệ quyền truy cập mạng nội bộ, đồng thời triển khai các công cụ giám sát an ninh mạng như NIDS hoặc HIPS để theo dõi các mối đe dọa bên ngoài.

### Bảo vệ thiết bị đầu cuối (Endpoint protection)
Nhà phát triển phải cài đặt phần mềm chống virus hoặc hệ thống ngăn chặn xâm nhập máy chủ (HIPS) để đảm bảo an toàn cho thiết bị đầu cuối. Cần quét bảo mật định kỳ và cập nhật cơ sở dữ liệu nhận diện virus liên tục.

### Tiêu chuẩn an ninh cơ sở (Security baselines)
Nhà phát triển phải áp dụng các biện pháp an ninh nơi làm việc như chính sách mật khẩu phức tạp (chữ hoa, chữ thường, độ dài, ký tự đặc biệt), xác thực đa yếu tố (MFA) cho tài khoản quản trị, tự động khóa màn hình sau một khoảng thời gian không hoạt động (ví dụ: 15 phút) và đào tạo nâng cao nhận thức bảo mật định kỳ.

### Bảo vệ dữ liệu (Data protection)
Nhà phát triển phải có chính sách Kiểm soát Truy cập công khai. Đối tác phải mã hóa toàn bộ dữ liệu cá nhân ở trạng thái lưu trữ (data at-rest) bằng tối thiểu AES-256 hoặc RSA-1024 trở lên, và dữ liệu trong quá trình truyền tải (data in-transit) bằng TLSv1.2 trở lên.

### Kiểm soát truy cập (Access control)
Nhà phát triển phải thực thi chính sách kiểm soát truy cập dựa trên nguyên tắc "Cần biết" (Need-to-know) và "Đặc quyền tối thiểu" (Least-privilege). Nhân viên và nhà thầu chỉ được cấp quyền theo vai trò cụ thể. Nhật ký truy cập hệ thống phải được lưu trữ và quyền hạn của người dùng phải được rà soát định kỳ ít nhất mỗi năm một lần.

### Quản lý lỗ hổng bảo mật (Vulnerability management)
Nhà phát triển phải có quy trình giám sát, theo dõi và khắc phục các lỗ hổng bảo mật liên tục. Cần tiến hành quét lỗ hổng hoặc kiểm thử xâm nhập định kỳ và lưu trữ các báo cáo kết quả.

### Quản lý sự cố an ninh mạng (Incident management)
Nhà phát triển phải ban hành quy trình ứng phó sự cố. Các buổi diễn tập ứng phó sự cố cần được tổ chức ít nhất mỗi năm một lần để kiểm tra tính hiệu quả của các quy trình khôi phục. Báo cáo sự cố phải được lưu trữ đầy đủ để phục vụ kiểm tra.

## Các lưu ý quan trọng
Quá trình đánh giá thường mất từ 2 đến 4 tuần. Để đẩy nhanh tiến độ phê duyệt, chúng tôi khuyến nghị bạn cung cấp thông tin chi tiết kèm các tài liệu chứng minh như chứng chỉ ISO 27001, báo cáo SOC 2 và báo cáo quét lỗ hổng/kiểm thử xâm nhập mới nhất. Nếu đơn đăng ký bị từ chối, vui lòng xem phản hồi của chuyên viên đánh giá để bổ sung tài liệu.

**Xin lưu ý: Không có nội dung nào trên trang này nhằm thay thế các nghĩa vụ bảo mật và quyền riêng tư của bạn theo [Điều khoản Nhà phát triển TikTok for Business](https://ads.tiktok.com/i18n/official/article?aid=10022349) hoặc được coi là tư vấn pháp lý.**

**Lời nhắc cuối cùng: Bạn sẽ không thể nhận được phạm vi quyền hạn Business Messaging cho ứng dụng nhà phát triển nếu chưa hoàn thành quy trình đánh giá an toàn dữ liệu và quyền riêng tư. Không có trường hợp ngoại lệ.**

---

<a id="doc-1832184219753474"></a>
<!-- doc_id: 1832184219753474 -->
<!-- doc_id: 1832184219753474 -->
# Kiểm duyệt an ninh dữ liệu thị trường Hoa Kỳ (US data security review)
> Đường dẫn: Business Messaging API > Guides > Get started > Access to Business Messaging API > US data security review
Bảng câu hỏi An ninh Dữ liệu Hoa Kỳ (USDS VAQ) được cung cấp và quản lý bởi đội ngũ US Data Security (USDS) của chúng tôi. Mục đích cụ thể của biểu mẫu là thu thập thông tin về nhà phát triển nhằm đảm bảo họ duy trì an toàn và bảo mật cho dữ liệu người dùng Hoa Kỳ, phù hợp với các tiêu chuẩn và thông lệ tốt nhất của TikTok. Tất cả các nhà phát triển muốn quản lý tin nhắn cho tài khoản TikTok đăng ký tại Hoa Kỳ bắt buộc phải vượt qua kỳ đánh giá này và ký kết Phụ lục USDS Addendum.

Đánh giá này được tiến hành vì lợi ích cao nhất của người dùng, nhà quảng cáo, nhà phát triển và chính các doanh nghiệp. Ứng dụng nhà phát triển không thể nhận phạm vi quyền hạn Business Messaging cho thị trường Mỹ nếu thiếu sự chấp thuận từ đội ngũ USDS và việc ký thỏa thuận phụ lục. Đội ngũ USDS sẽ đưa ra quyết định dựa trên thông tin bạn cung cấp (quy trình xét duyệt thường kéo dài từ 7-10 ngày làm việc sau khi nộp).

Có nhiều nguyên nhân khiến nhà phát triển có thể bị từ chối. Trong một số trường hợp, chúng tôi có thể yêu cầu cung cấp thêm thông tin làm rõ, và trong các trường hợp khác, chúng tôi có thể từ chối dứt khoát vì lý do an ninh. Đội ngũ TikTok API for Business sẽ liên hệ với bạn nếu cần. Sau khi được chấp thuận, TikTok sẽ gửi thông báo để hoàn tất ký kết Phụ lục USDS Addendum.

Hãy đảm bảo rằng bạn trả lời tất cả các câu hỏi một cách thấu đáo và trung thực. Chúng tôi khuyến nghị nộp kèm các tài liệu như chứng chỉ ISO 27001, báo cáo SOC 2, và kết quả kiểm thử bảo mật gần nhất để đẩy nhanh tiến độ.

## Các quốc gia bị hạn chế theo chính sách USDS (USDS Restricted Countries)
Là một phần của quy trình kiểm duyệt an ninh, USDS thực thi nghiêm ngặt các quy định an ninh quốc gia của Hoa Kỳ, bao gồm các hạn chế đối với nhà phát triển và các thực thể liên quan đến các quốc gia bị cấm vận theo OFAC hoặc do CFIUS chỉ định.

Các nhà phát triển đặt trụ sở, thành lập theo luật, hoặc có Chủ sở hữu Hưởng lợi Cuối cùng (UBO) đến từ các Quốc gia bị Hạn chế — chẳng hạn như Trung Quốc (bao gồm Hồng Kông), Nga, Iran, Triều Tiên, Cuba và Syria — có thể không đủ điều kiện phát hành ứng dụng hoặc nhận phạm vi quyền hạn Business Messaging tại thị trường Hoa Kỳ. Hạn chế này cũng áp dụng cho các thực thể có cấu trúc sở hữu mà tổng tỷ lệ sở hữu của các cá nhân/tổ chức từ các Quốc gia bị Hạn chế vượt quá 25%, ngay cả khi không có cá nhân đơn lẻ nào vượt ngưỡng.

USDS có quyền yêu cầu tài liệu bổ sung để xác minh quyền sở hữu, địa bàn hoạt động hoặc các mối liên kết của nhà phát triển. Bất kỳ sự khai báo sai lệch hoặc che giấu thông tin nào liên quan đến quyền sở hữu hoặc mối quan hệ địa lý sẽ dẫn đến việc bị loại ngay lập tức.

---

<a id="doc-1832184159540418"></a>
<!-- doc_id: 1832184159540418 -->
<!-- doc_id: 1832184159540418 -->
# Ủy quyền tài khoản (Authorization)
> Đường dẫn: Business Messaging API > Guides > Get started > Authorization
Trước khi sử dụng Business Messaging API, bạn (nhà phát triển) cần nhận được sự ủy quyền từ doanh nghiệp để quản lý tài khoản TikTok của họ.

## Điều kiện tiên quyết (Prerequisites)
- Bạn đã tạo tài khoản TikTok For Business. Để biết chi tiết, xem [Tạo tài khoản TikTok For Business](../04-get-started/bat-dau.md#doc-1738855099573250).
- Bạn đã đăng ký làm nhà phát triển. Để biết chi tiết, xem [Đăng ký làm nhà phát triển](../04-get-started/bat-dau.md#doc-1738855176671234).
- Bạn đã tạo ứng dụng nhà phát triển. Để biết chi tiết, xem [Tạo ứng dụng nhà phát triển](../04-get-started/bat-dau.md#doc-1738855242728450).
- Bạn đã tải lên Logo ứng dụng (App logo) để người dùng nhìn thấy trong giao diện cấp quyền.
  - Hình ảnh logo cần ở định dạng JPG, JPEG hoặc PNG, kích thước tối đa 512 * 512 pixel.
  - Nếu quên tải logo, người dùng sẽ gặp trang báo lỗi khi thực hiện ủy quyền.
- Redirect URL của ứng dụng đã được cấu hình đúng chuẩn để tiếp nhận mã ủy quyền (`auth_code`). Xem [Cấu hình Redirect URL](../04-get-started/bat-dau.md#doc-1832209711206401).
- Bạn [đã được cấp quyền truy cập Business Messaging API](business-messaging-api.md#doc-1832184145137922).

## Quy trình thực hiện (Workflow)

### Bước 1: Chia sẻ URL ủy quyền với doanh nghiệp
Gửi URL ủy quyền cho chủ tài khoản TikTok của doanh nghiệp. Đảm bảo bạn đã chọn quyền hạn **Business Messaging** cho ứng dụng.

Để lấy URL này, hãy truy cập [My Apps](https://ads.tiktok.com/marketing_api/apps/) > **App Detail** > **Basic Information** > **TikTok account holder authorization URL**.

> **Lưu ý:**
> Để tăng cường bảo mật, bạn có thể truyền thêm tham số `state` duy nhất trong URL ủy quyền nhằm phòng chống tấn công CSRF. Tham số này sẽ được hệ thống gửi trả lại ứng dụng của bạn trong chuỗi truy vấn khi chuyển hướng.

Nếu bạn không tìm thấy URL ủy quyền cho chủ tài khoản TikTok, hãy kiểm tra tại mục **Authorization** > **Scope of permission** và đảm bảo đã bật phạm vi quyền hạn "TikTok Accounts".

### Bước 2: Doanh nghiệp cấp quyền ủy quyền
Khi chủ doanh nghiệp mở URL ủy quyền, họ sẽ thấy màn hình yêu cầu cấp phép. Đảm bảo doanh nghiệp đồng ý phê duyệt các quyền sau:
- **Send messages or interactions to other accounts on your behalf** (Thay mặt gửi tin nhắn hoặc tương tác với tài khoản khác)
- **Read messages in your inbox (including direct messages)** (Đọc tin nhắn trong hộp thư đến)
- **Read your TikTok account type** (Đọc loại tài khoản TikTok)
- **Read and manage messages in your inbox (including direct messages)** (Đọc và quản lý tin nhắn trong hộp thư đến)

- Sau khi bấm **Authorize (Ủy quyền)**, doanh nghiệp sẽ được chuyển hướng về **Redirect URL** của ứng dụng.
- Redirect URL sẽ đính kèm tham số `code=`, chính là giá trị `auth_code` cần thiết để đổi lấy access token qua endpoint [/tt_user/oauth2/token/](business-messaging-api.md#doc-1832184175482945).

> **Lưu ý:**
> - Nếu người dùng đã từng ủy quyền ứng dụng với các quyền hạn tương tự trước đó, bước xem xét quyền hạn sẽ được bỏ qua và người dùng được chuyển thẳng về Redirect URL mà không có `auth_code`.
> - Để vô hiệu hóa cơ chế tự động chuyển hướng này, hãy gắn thêm tham số `&disable_auto_auth=1` vào cuối URL ủy quyền trước khi chia sẻ cho người dùng.

## Bước tiếp theo
[Đăng ký nhận sự kiện Webhook tin nhắn qua Webhooks API](../08-use-cases/use-case-webhook.md#doc-1832190670631937)

---

<a id="doc-1832184175482945"></a>
<!-- doc_id: 1832184175482945 -->
<!-- doc_id: 1832184175482945 -->
# Xác thực (Authentication)
> Đường dẫn: Business Messaging API > Guides > Get started > Authentication
Sử dụng mã ủy quyền (`auth_code`) nhận được sau khi doanh nghiệp chấp thuận cấp quyền, bạn có thể gửi yêu cầu tới endpoint `/tt_user/oauth2/token/` để lấy mã truy cập `access_token` cho các lượt gọi API tiếp theo, cùng với `refresh_token` để làm mới token khi cần.

Để kiểm tra danh sách các quyền hạn đã được chủ tài khoản TikTok ủy quyền, bạn có thể truyền `access_token` vừa tạo vào endpoint [/tt_user/token_info/get/](../12-api-reference/01-accounts-p1.md#doc-1765927978092545).

**Thời gian hết hạn của Access Token**

Mã `access_token` có hiệu lực trong vòng 1 ngày (24 giờ).

Khi token hết hạn, bạn cần gửi yêu cầu tới endpoint `/tt_user/oauth2/refresh_token/` để lấy token mới. Nhớ truyền `refresh_token` tương ứng vào yêu cầu làm mới.

**Thời gian hết hạn của Refresh Token**

Mã `refresh_token` có hiệu lực trong vòng 1 năm.

Nếu `refresh_token` hết hạn, nhà phát triển phải yêu cầu người dùng thực hiện lại quy trình ủy quyền từ đầu.

## Lấy mã truy cập ngắn hạn (Obtain a short-term access token)
Sử dụng endpoint này để lấy mã truy cập tài khoản TikTok (access token).

### Yêu cầu gọi API (Request)

**Endpoint** `https://business-api.tiktok.com/open_api/v1.3/tt_user/oauth2/token/`

**Method** POST

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Content-Type  ****(Bắt buộc)**** | string | Định dạng dữ liệu yêu cầu. ⏎ Định dạng được phép: `application/json`. |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| client_id  ****(Bắt buộc)**** | string | ID của ứng dụng nhà phát triển (App ID). ⏎ Để lấy **App ID**, truy cập [My Apps](https://ads.tiktok.com/marketing_api/apps/) > **App Detail** > **Basic Information**. |
| client_secret  ****(Bắt buộc)**** | string | Mã bí mật của ứng dụng nhà phát triển (Secret). ⏎ Để lấy **Secret**, truy cập [My Apps](https://ads.tiktok.com/marketing_api/apps/) > **App Detail** > **Basic Information**. |
| grant_type  ****(Bắt buộc)**** | string | Phương thức tạo mã truy cập. ⏎ Giá trị enum cho phép: • `authorization_code`: Tạo access token bằng mã ủy quyền. |
| auth_code  ****(Bắt buộc)**** | string | Mã ủy quyền (`auth_code`) được tạo qua **URL ủy quyền cho chủ tài khoản TikTok**. ⏎ Mã có hiệu lực trong 10 phút và chỉ dùng được một lần. |
| redirect_uri  ****(Bắt buộc)**** | string | URL chuyển hướng mà người dùng sẽ được đưa tới sau khi cấp quyền. ⏎ Giá trị phải trùng khớp tuyệt đối với **Redirect URL** đã đăng ký trong ứng dụng. |

#### Ví dụ lệnh cURL (Example)
```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/tt_user/oauth2/token/' --header 'Content-Type: application/json' --data '{
    "client_id":"YOUR_CLIENT_ID",
    "client_secret":"YOUR_CLIENT_SECRET",
    "grant_type":"authorization_code",
    "auth_code":"YOUR_AUTH_CODE",
    "redirect_uri":"https://dev.example.com/auth/callback/"
}'
```

### Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Mã phản hồi API. Xem danh sách đầy đủ tại [Phụ lục - Mã lỗi trả về](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi. Để biết chi tiết, xem [Phụ lục - Mã lỗi trả về](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | Mã nhật ký yêu cầu (request log ID) để định danh duy nhất cho mỗi lượt gọi API. |
| data | object | Dữ liệu trả về. |
| ↳ access_token | string | Mã token ngắn hạn dùng để xác thực quyền truy cập. Token có hiệu lực trong vòng 1 ngày. |
| ↳ token_type | string | Loại token. ⏎ Giá trị enum: • `Bearer`: Bearer token. Bất kỳ ai sở hữu token này đều có thể truy cập các tài nguyên liên kết. |
| ↳ scope | string | Danh sách các phạm vi quyền hạn được cấp cho access token. |
| ↳ expires_in | number | Thời gian hiệu lực còn lại của access token, tính bằng giây. |
| ↳ refresh_token | string | Mã làm mới token, dùng để lấy access token mới khi token cũ hết hạn. Mã có hiệu lực trong vòng 1 năm. ⏎ **Lưu ý**: Cần lưu trữ cẩn thận trường này để phục vụ gia hạn token. |
| ↳ refresh_token_expires_in | number | Thời gian hiệu lực còn lại của refresh token, tính bằng giây. |
| ↳ open_id | string | Mã định danh duy nhất của tài khoản TikTok đối với ứng dụng cụ thể. |

#### Ví dụ phản hồi thành công
```json
{
    "code": 0,
    "message": "OK",
    "request_id": "202610231234560102030405060708",
    "data": {
        "access_token": "act.example_access_token_value",
        "expires_in": 86400,
        "open_id": "usr.example_open_id",
        "refresh_token": "rft.example_refresh_token_value",
        "refresh_token_expires_in": 31536000,
        "scope": "message.list.manage,video.list,video.insights,user.insights,user.info.basic,comment.list,biz.brand.insights,biz.spark.auth,tcm.order.update,comment.list.manage,video.upload,video.publish,biz.ads.recommend,user.account.type,biz.creator.info,user.info.username,message.list.send,user.info.profile,user.info.stats,message.list.read,biz.creator.insights",
        "token_type": "Bearer"
    }
}
```

## Làm mới mã truy cập ngắn hạn (Renew a short-term access token)
Sử dụng endpoint này để làm mới `access_token` đã hết hạn thông qua `refresh_token`.

### Yêu cầu gọi API (Request)

**Endpoint** `https://business-api.tiktok.com/open_api/v1.3/tt_user/oauth2/refresh_token/`

**Method** POST

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Content-Type  ****(Bắt buộc)**** | string | Định dạng dữ liệu yêu cầu. ⏎ Định dạng được phép: `application/json`. |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| client_id  ****(Bắt buộc)**** | string | ID của ứng dụng nhà phát triển (App ID). ⏎ Lấy tại [My Apps](https://ads.tiktok.com/marketing_api/apps/) > **App Detail** > **Basic Information**. |
| client_secret  ****(Bắt buộc)**** | string | Mã bí mật của ứng dụng (Secret). ⏎ Lấy tại [My Apps](https://ads.tiktok.com/marketing_api/apps/) > **App Detail** > **Basic Information**. |
| grant_type  ****(Bắt buộc)**** | string | Phương thức làm mới token. ⏎ Giá trị enum cho phép: • `refresh_token`: Làm mới access token bằng refresh token. |
| refresh_token  ****(Bắt buộc)**** | string | Mã làm mới token dùng để gia hạn. Lấy từ phản hồi của endpoint `/tt_user/oauth2/token/`. |

#### Ví dụ lệnh cURL (Example)
```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/tt_user/oauth2/refresh_token/' --header 'Content-Type: application/json' --data '{
    "client_id":"YOUR_CLIENT_ID",
    "client_secret":"YOUR_CLIENT_SECRET",
    "grant_type":"refresh_token",
    "refresh_token":"YOUR_REFRESH_TOKEN"
}'
```

### Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Mã phản hồi API. Xem danh sách mã tại [Phụ lục - Mã lỗi trả về](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi từ hệ thống. |
| request_id | string | Mã định danh duy nhất của lượt yêu cầu (request log ID). |
| data | object | Dữ liệu trả về. |
| ↳ access_token | string | Mã truy cập mới được cấp. Token có hiệu lực trong vòng 1 ngày. |
| ↳ token_type | string | Loại token. ⏎ Giá trị enum: • `Bearer`: Bearer token. |
| ↳ scope | string | Danh sách phạm vi quyền hạn được cấp cho token. |
| ↳ expires_in | number | Thời gian hiệu lực còn lại của access token (tính bằng giây). |
| ↳ refresh_token | string | Mã làm mới token mới được cấp, có hiệu lực trong 1 năm. Lưu ý lưu trữ trường này để tiếp tục gia hạn token lần sau. |
| ↳ refresh_token_expires_in | number | Thời gian hiệu lực còn lại của refresh token (tính bằng giây). |
| ↳ open_id | string | Mã định danh duy nhất của tài khoản TikTok đối với ứng dụng. |

---

<a id="doc-1832184236919810"></a>
<!-- doc_id: 1832184236919810 -->
<!-- doc_id: 1832184236919810 -->
# Quản lý tin nhắn trực tiếp cho tài khoản TikTok
> Đường dẫn: Business Messaging API > Guides > Manage direct messages for a TikTok account
Tài liệu này hướng dẫn các bước tiếp nhận và phản hồi tin nhắn, quản lý các cuộc trò chuyện và xử lý tệp phương tiện (hình ảnh) trong tin nhắn trực tiếp qua Business Messaging API.

## Giới thiệu
Quản lý tin nhắn trực tiếp cho tài khoản TikTok là tính năng trọng tâm của Business Messaging API, cho phép doanh nghiệp tương tác hiệu quả với người dùng TikTok.

**Bạn có thể sử dụng Business Messaging API để tinh gọn quá trình giao tiếp thông qua việc tự động hóa xử lý tin nhắn, truy xuất lịch sử hội thoại và quản lý tệp media hiệu quả. Những tính năng này giúp doanh nghiệp phản hồi kịp thời, tổ chức cuộc trò chuyện khoa học và đem lại trải nghiệm nhắn tin mượt mà cho khách hàng.**

## Điều kiện tiên quyết
- Bạn đã có quyền truy cập TikTok API for Business. Xem chi tiết tại [Bắt đầu - Quy trình từng bước](../04-get-started/bat-dau.md#doc-1735713609895937).
  - Để quản lý tin nhắn trực tiếp, bạn cần các quyền hạn tương ứng. Xem mục **Danh mục API Reference** để biết các quyền cần thiết cho từng endpoint và xem [Cập nhật quyền ứng dụng](../04-get-started/bat-dau.md#doc-1738855280338946) để cấu hình quyền.
- Bạn đã hoàn thành các bước trong phần [Ủy quyền](business-messaging-api.md#doc-1832184159540418) và [Xác thực](business-messaging-api.md#doc-1832184175482945) để nhận mã `access_token` và mã định danh duy nhất của tài khoản TikTok.

## Các bước thực hiện

### Tiếp nhận tin nhắn (Receive messages)
- Khi một người dùng TikTok gửi tin nhắn tới doanh nghiệp, hệ thống sẽ gửi một thông báo Webhook tới URL của bạn.
- Tin nhắn khởi đầu từ người dùng TikTok sẽ kích hoạt một sự kiện hội thoại kèm theo mã `conversation_id` duy nhất.

### Phản hồi tin nhắn (Respond to messages)
- Bạn có thể gửi tin nhắn phản hồi tới người dùng TikTok bằng cách gọi endpoint [/business/message/send/](../12-api-reference/23-business-messaging.md#doc-1832184403754242) kèm theo `conversation_id` nhận được từ thông báo webhook.
- Các loại tin nhắn hỗ trợ gửi đi bao gồm:
  - Tin nhắn văn bản (Text message).
  - Tin nhắn hình ảnh (Image message).
  - Mẫu tin nhắn (Message templates), bao gồm:
    - **Thẻ nút hỏi đáp (Q&A button card)**: Thẻ hiển thị một câu hỏi kèm các nút bấm đại diện cho câu trả lời. Khi người dùng nhấp vào một nút, nội dung văn bản của nút đó sẽ được tự động gửi vào luồng trò chuyện thay mặt cho người dùng.
    - **Thẻ liên kết văn bản hỏi đáp (Q&A text link card)**: Thẻ hiển thị một câu hỏi kèm các liên kết văn bản tương tác. Khi nhấp vào liên kết, nội dung sẽ được gửi vào luồng trò chuyện làm câu trả lời.
  - Tin nhắn bài đăng TikTok (TikTok post message).
  - Hành động của người gửi (Sender actions) trong phiên nhắn tin, ví dụ:
    - **Đang soạn tin (Typing)**: Người gửi đang chuẩn bị câu trả lời. Giao diện sẽ hiển thị biểu tượng "Đang nhập..." và tự động biến mất sau 5 giây.
    - **Đánh dấu đã đọc (Marking as read)**: Người gửi đánh dấu tất cả tin nhắn trong phiên là đã đọc, hiển thị biểu tượng "Đã xem" cho các tin nhắn đó.

> **Lưu ý:**
> - Bạn tuyệt đối bị cấm chủ động bắt đầu cuộc trò chuyện hoặc nhắn tin cho bất kỳ người dùng TikTok nào chưa từng chủ động nhắn tin cho bạn trước đó.
> - Đối với các cuộc trò chuyện không theo dõi lẫn nhau (non-mutual follow), một số hạn mức tin nhắn sẽ được áp dụng. Xem chi tiết tại [Hạn mức gửi tin nhắn](business-messaging-api.md#doc-1854823717597185).

### Quản lý cuộc trò chuyện (Manage conversations)
- Bạn có thể lấy danh sách các cuộc hội thoại bằng endpoint [/business/message/conversation/list/](../12-api-reference/23-business-messaging.md#doc-1832184415059970), hỗ trợ trả về tối đa 100 bản ghi hội thoại.
- Để lấy danh sách các tin nhắn trong một cuộc hội thoại cụ thể, gọi endpoint [/business/message/content/list/](../12-api-reference/23-business-messaging.md#doc-1832184425841170) kèm theo `conversation_id`. Endpoint này truy xuất 20 tin nhắn gần nhất.

### Xử lý tệp phương tiện (Handle media)
- **Để gửi hình ảnh**:
	1. Tải hình ảnh lên qua endpoint [/business/message/media/upload/](../12-api-reference/23-business-messaging.md#doc-1832184437720193). Tải lên thành công sẽ trả về mã `media_id`.
> **Lưu ý:**
> - Mã `media_id` có hiệu lực trong 30 ngày. Khi hết hạn, bạn cần tải lại ảnh để nhận mã mới.
> - Tính năng gửi và nhận tệp đính kèm hình ảnh qua API chỉ khả dụng khi cả người gửi và người nhận đều ở các quốc gia hỗ trợ hình ảnh trong tin nhắn trực tiếp.
> - Bạn có thể sử dụng endpoint [/business/message/capabilities/get/](../12-api-reference/23-business-messaging.md#doc-1836061597865986) để kiểm tra xem tài khoản TikTok có quyền gửi tệp phương tiện trong cuộc hội thoại hay không.
	2. Truyền `media_id` nhận được vào trường `media_id` trong endpoint [/business/message/send/](../12-api-reference/23-business-messaging.md#doc-1832184403754242) để gửi tin nhắn ảnh cho người dùng.

- **Để tải hình ảnh về**:
	- Gọi endpoint [/business/message/media/download/](../12-api-reference/23-business-messaging.md#doc-1832184455450626) kèm theo `media_id`, `message_id` và `conversation_id`. API sẽ trả về `download_url` để tải tệp hình ảnh.

---

<a id="doc-1854823717597185"></a>
<!-- doc_id: 1854823717597185 -->
<!-- doc_id: 1854823717597185 -->
# Hạn mức gửi tin nhắn của API (Messaging limits for Business Messaging API)
> Đường dẫn: Business Messaging API > Guides > Manage direct messages for a TikTok account > Messaging limits for Business Messaging API
Đối với các cuộc hội thoại không theo dõi lẫn nhau (non-mutual follow) của tài khoản TikTok được xử lý qua Business Messaging API, các quy định hạn mức tin nhắn sau đây sẽ được áp dụng:
- **Cửa sổ 48 giờ ban đầu**: Sau khi nhận được tin nhắn đầu tiên từ người dùng TikTok, tài khoản TikTok có thể gửi tối đa 10 tin nhắn trong vòng 48 giờ tiếp theo.
- **Cửa sổ hội thoại đang hoạt động**: Nếu người dùng TikTok phản hồi tin nhắn của tài khoản, một khung tương tác mới sẽ bắt đầu. Trong vòng 48 giờ kể từ lần phản hồi cuối cùng của người dùng, tài khoản TikTok được phép gửi không giới hạn số lượng tin nhắn cho người dùng đó.
- **Giới hạn khi hội thoại không hoạt động**: Nếu đã quá 48 giờ kể từ lần phản hồi cuối cùng của người dùng TikTok mà không có tương tác mới, tài khoản TikTok chỉ được phép gửi tối đa thêm 3 tin nhắn nữa. Hạn chế này có hiệu lực cho đến khi người dùng phản hồi lại, lúc đó khung thời gian nhắn tin không giới hạn sẽ được tái kích hoạt trong 48 giờ tiếp theo.
- **Minh họa quy trình hoạt động**:
  - Người dùng TikTok gửi tin nhắn đầu tiên
  - → Tài khoản TikTok có thể gửi tối đa 10 tin nhắn trong 48 giờ
  - → Người dùng TikTok gửi phản hồi
  - → Tài khoản TikTok có thể gửi không giới hạn tin nhắn trong 48 giờ tiếp theo
  - → Nếu người dùng TikTok không phản hồi sau hơn 48 giờ
  - → Tài khoản TikTok chỉ có thể gửi thêm tối đa 3 tin nhắn nữa
  - → Người dùng TikTok gửi phản hồi trở lại
  - → Cửa sổ nhắn tin không giới hạn được mở lại trong 48 giờ tiếp theo.

---

<a id="doc-1832184250237954"></a>
<!-- doc_id: 1832184250237954 -->
<!-- doc_id: 1832184250237954 -->
# Quản lý tin nhắn tự động (Manage automatic messages for a TikTok account)
> Đường dẫn: Business Messaging API > Guides > Manage automatic messages for a TikTok account
Tài liệu này hướng dẫn các bước thiết lập và quản lý các loại tin nhắn tự động cho tài khoản TikTok.

## Giới thiệu
Tin nhắn tự động là công cụ thiết yếu để xây dựng trải nghiệm giao tiếp liền mạch với khán giả của bạn. Chúng giúp doanh nghiệp chào đón người dùng, trả lời nhanh các thắc mắc phổ biến và định hướng cuộc trò chuyện hiệu quả.

Các tính năng tin nhắn tự động chính bao gồm:
- **Tin nhắn chào mừng (Welcome messages)**: Chào đón người dùng khi họ lần đầu tương tác với tài khoản TikTok của bạn.
- **Câu hỏi gợi ý (Suggested questions)**: Cung cấp câu trả lời nhanh cho các câu hỏi thường gặp.
- **Nút gợi ý trò chuyện (Chat prompts)**: Khuyến khích người dùng chủ động mở đầu cuộc trò chuyện thông qua các nút bấm tương tác.
- **Tin nhắn cho người theo dõi mới (New follower messages)**: Gửi lời chào tới những người vừa nhấn theo dõi tài khoản TikTok và hướng dẫn họ thực hiện các hành động tiếp theo.

Bạn có thể sử dụng Business Messaging API để quản lý các tính năng này nhằm tạo nên một trải nghiệm giao tiếp hấp dẫn và hiệu quả hơn.

## Các bước thực hiện
- Để tìm hiểu cách tạo tin nhắn chào mừng, hãy xem [Quản lý tin nhắn chào mừng cho tài khoản TikTok](business-messaging-api.md#doc-1832184264385538).
- Để tìm hiểu cách cấu hình câu hỏi gợi ý, hãy xem [Quản lý câu hỏi gợi ý cho tài khoản TikTok](business-messaging-api.md#doc-1832184277518338).
- Để tìm hiểu cách tùy chỉnh nút gợi ý trò chuyện, hãy xem [Quản lý nút gợi ý trò chuyện cho tài khoản TikTok](business-messaging-api.md#doc-1832184291198977).
- Để tìm hiểu cách thiết lập tin nhắn chào người theo dõi mới, hãy xem [Quản lý tin nhắn cho người theo dõi mới](business-messaging-api.md#doc-1877104214073346).

## Tài liệu liên quan
- [Business Messaging API reference](../12-api-reference/23-business-messaging.md#doc-1832184349193282)

---

<a id="doc-1832184264385538"></a>
<!-- doc_id: 1832184264385538 -->
<!-- doc_id: 1832184264385538 -->
# Quản lý tin nhắn chào mừng (Manage the welcome message for a TikTok account)
> Đường dẫn: Business Messaging API > Guides > Manage automatic messages for a TikTok account > Manage the welcome message for a TikTok account
Tài liệu này hướng dẫn quy trình quản lý tin nhắn chào mừng cho tài khoản TikTok bằng Business Messaging API.

## Giới thiệu
Tin nhắn chào mừng là tương tác đầu tiên mà người dùng nhìn thấy khi họ mở hộp thoại với tài khoản TikTok của bạn. Chúng định hình phong cách giao tiếp và tạo ấn tượng ban đầu tích cực. Với Business Messaging API, bạn có thể tạo tin nhắn chào mừng mới hoặc chỉnh sửa mẫu tin nhắn mặc định cho phù hợp với giọng văn thương hiệu. Mỗi tài khoản TikTok có thể thiết lập một tin nhắn chào mừng tùy chỉnh.

## Điều kiện tiên quyết
- Bạn đã có quyền truy cập TikTok API for Business. Xem chi tiết tại [Bắt đầu - Quy trình từng bước](../04-get-started/bat-dau.md#doc-1735713609895937).
- Bạn đã có access token và Open ID thông qua các bước [Ủy quyền](business-messaging-api.md#doc-1832184159540418) và [Xác thực](business-messaging-api.md#doc-1832184175482945).

## Các bước thực hiện

### Lựa chọn 1: Tạo một tin nhắn chào mừng mới
1. **Thiết lập tin nhắn chào mừng mới** bằng endpoint [/business/message/auto_message/create/](../12-api-reference/23-business-messaging.md#doc-1832184584869890).
   - Đặt `auto_message_type` thành `WELCOME_MESSAGE` và chỉ định cấu hình trong đối tượng `welcome_message`.
2. **Kiểm tra trạng thái của tin nhắn chào mừng** bằng endpoint [/business/message/auto_message/get/](../12-api-reference/23-business-messaging.md#doc-1832184619749377).
   - Đặt `auto_message_type` thành `WELCOME_MESSAGE` và xác nhận rằng `audit_status` là `APPROVED` và `operation_status` là `ENABLE`.
   - **Lưu ý**: Nếu `audit_status` là `REVIEWING`, bạn cần chờ một khoảng thời gian để hệ thống xét duyệt nội dung (thường từ vài giây đến 2-3 giờ).
3. **Xử lý các tình huống phát sinh**:
   - Nếu `audit_status` là `REJECTED` (Bị từ chối): Cập nhật lại tin nhắn bằng [/business/message/auto_message/update/](../12-api-reference/23-business-messaging.md#doc-1832184596566017) rồi kiểm tra lại trạng thái.
   - Nếu `operation_status` là `DISABLE`: Bật tin nhắn bằng [/business/message/auto_message/status/update/](../12-api-reference/23-business-messaging.md#doc-1832184607786242) với `operation_status` là `ENABLE`.

### Lựa chọn 2: Chỉnh sửa tin nhắn chào mừng mặc định
1. **Kích hoạt tin nhắn chào mừng mặc định**: Gọi endpoint [/business/message/auto_message/status/update/](../12-api-reference/23-business-messaging.md#doc-1832184607786242) và đặt `operation_status` thành `ENABLE`.
2. **Lấy nội dung tin nhắn mặc định**: Gọi [/business/message/auto_message/get/](../12-api-reference/23-business-messaging.md#doc-1832184619749377).
3. **Cập nhật nội dung tin nhắn**: Gọi [/business/message/auto_message/update/](../12-api-reference/23-business-messaging.md#doc-1832184596566017).
4. **Xác nhận trạng thái sau khi cập nhật**: Gọi lại `/business/message/auto_message/get/` để xác nhận `audit_status` là `APPROVED` và `operation_status` là `ENABLE`.

---

<a id="doc-1832184277518338"></a>
<!-- doc_id: 1832184277518338 -->
<!-- doc_id: 1832184277518338 -->
# Quản lý câu hỏi gợi ý (Manage the suggested questions for a TikTok account)
> Đường dẫn: Business Messaging API > Guides > Manage automatic messages for a TikTok account > Manage the suggested questions for a TikTok account
Tài liệu này hướng dẫn cách quản lý các câu hỏi gợi ý cho tài khoản TikTok bằng Business Messaging API.

## Giới thiệu
Câu hỏi gợi ý là danh sách các câu hỏi thường gặp hiển thị ngay khi bắt đầu cuộc trò chuyện. Người dùng có thể nhấp chọn một câu hỏi để nhận câu trả lời đã được thiết lập sẵn một cách tự động, giúp giảm thiểu thời gian chờ đợi và tối ưu hóa nguồn lực chăm sóc khách hàng. Mỗi tài khoản TikTok có thể tùy chỉnh tối đa 3 câu hỏi gợi ý.

## Điều kiện tiên quyết
- Bạn đã có quyền truy cập TikTok API for Business.
- Bạn đã nhận được mã truy cập `access_token` và `open_id`.

## Các bước thực hiện
1. **Bật tính năng câu hỏi gợi ý** bằng endpoint [/business/message/auto_message/status/update/](../12-api-reference/23-business-messaging.md#doc-1832184607786242) với `auto_message_type` là `SUGGESTED_QUESTION` và `operation_status` là `ENABLE`.
2. **Tạo câu hỏi gợi ý** bằng endpoint [/business/message/auto_message/create/](../12-api-reference/23-business-messaging.md#doc-1832184584869890) với `auto_message_type` là `SUGGESTED_QUESTION` và cấu hình đối tượng `suggested_question`.
3. **Kiểm tra trạng thái câu hỏi** bằng endpoint [/business/message/auto_message/get/](../12-api-reference/23-business-messaging.md#doc-1832184619749377) để xác nhận `audit_status` là `APPROVED` và `operation_status` là `ENABLE`.
4. **Xử lý sự cố**: Nếu câu hỏi bị từ chối (`REJECTED`), hãy cập nhật lại bằng `/business/message/auto_message/update/`. Nếu tính năng bị tắt (`DISABLE`), hãy kích hoạt lại như ở Bước 1.

---

<a id="doc-1832184291198977"></a>
<!-- doc_id: 1832184291198977 -->
<!-- doc_id: 1832184291198977 -->
# Quản lý nút gợi ý trò chuyện (Manage the chat prompts for a TikTok account)
> Đường dẫn: Business Messaging API > Guides > Manage automatic messages for a TikTok account > Manage the chat prompts for a TikTok account
Tài liệu này hướng dẫn quy trình quản lý các nút gợi ý trò chuyện (chat prompts) cho tài khoản TikTok bằng Business Messaging API.

## Giới thiệu
Nút gợi ý trò chuyện là các nút tương tác hiển thị phía trên khung nhập liệu tin nhắn. Khi người dùng nhấn vào nút gợi ý, hệ thống sẽ tự động tạo một câu hỏi tương ứng, giúp người dùng mở đầu cuộc trò chuyện dễ dàng hơn. Mỗi tài khoản TikTok có thể thiết lập tối đa 6 nút gợi ý trò chuyện.

## Điều kiện tiên quyết
- Bạn đã có quyền truy cập TikTok API for Business và có mã `access_token`.

## Các bước thực hiện
1. **Bật tính năng nút gợi ý** bằng [/business/message/auto_message/status/update/](../12-api-reference/23-business-messaging.md#doc-1832184607786242) với `auto_message_type` là `CHAT_PROMPT` và `operation_status` là `ENABLE`.
2. **Tạo nút gợi ý** bằng [/business/message/auto_message/create/](../12-api-reference/23-business-messaging.md#doc-1832184584869890) với `auto_message_type` là `CHAT_PROMPT` và cấu hình đối tượng `chat_prompt`.
3. **Kiểm tra trạng thái xét duyệt** bằng [/business/message/auto_message/get/](../12-api-reference/23-business-messaging.md#doc-1832184619749377) để xác nhận `audit_status` là `APPROVED` và `operation_status` là `ENABLE`.
4. **Xử lý sự cố**: Nếu bị từ chối, cập nhật lại qua `/business/message/auto_message/update/`. Nếu bị tắt, bật lại qua bước 1.

---

<a id="doc-1877104214073346"></a>
<!-- doc_id: 1877104214073346 -->
<!-- doc_id: 1877104214073346 -->
# Quản lý tin nhắn cho người theo dõi mới (Manage the new follower message for a TikTok account)
> Đường dẫn: Business Messaging API > Guides > Manage automatic messages for a TikTok account > Manage the new follower message for a TikTok account
Tài liệu này hướng dẫn các bước quản lý tin nhắn chào mừng người theo dõi mới cho tài khoản TikTok bằng Business Messaging API.

## Giới thiệu
Tin nhắn cho người theo dõi mới là lời chào tự động được gửi tới người dùng ngay khi họ nhấn theo dõi tài khoản TikTok của bạn. Tính năng này giúp xây dựng mối quan hệ ban đầu thân thiết và thúc đẩy các hành động mong muốn từ phía khách hàng. Mỗi tài khoản TikTok có thể cài đặt một tin nhắn tùy chỉnh cho người theo dõi mới.

## Điều kiện tiên quyết
- Bạn đã có quyền truy cập TikTok API for Business và có mã truy cập `access_token`.
- Tài khoản TikTok phải là **Tài khoản Doanh nghiệp Đã xác minh (Verified Business Account - VBA)** hoặc Tài khoản TikTok có Quyền truy cập Nâng cao (Advanced Access) có lịch sử chạy [TikTok Messaging Ads](https://ads.tiktok.com/help/article/about-tiktok-messaging-ads) trong vòng 7 ngày qua.
- Bạn có thể kiểm tra điều kiện này bằng cách gọi endpoint [/business/get/](../12-api-reference/01-accounts-p1.md#doc-1762228399168514) và xác nhận tham số phản hồi `has_advanced_access` có giá trị `true`.

## Các bước thực hiện
1. **Kiểm tra tính khả dụng của tính năng** bằng endpoint [/business/message/capabilities/get/](../12-api-reference/23-business-messaging.md#doc-1836061597865986) với `capability_types` là `["FOLLOW_WELCOME"]`.
2. **Lấy các tùy chọn tin nhắn khả dụng** bằng endpoint [/business/message/auto_message/get/](../12-api-reference/23-business-messaging.md#doc-1832184619749377). Nếu `capability_result` ở bước 1 là `true`, hãy kiểm tra trường `button_options` để xác định cấu hình chính xác được hỗ trợ.
3. **Thiết lập tin nhắn cho người theo dõi mới** bằng endpoint [/business/message/auto_message/create/](../12-api-reference/23-business-messaging.md#doc-1832184584869890) với `auto_message_type` là `FOLLOW_WELCOME` và cấu hình trong đối tượng `follow_welcome`.
4. **Kiểm tra trạng thái tin nhắn** bằng endpoint [/business/message/auto_message/get/](../12-api-reference/23-business-messaging.md#doc-1832184619749377) để xác nhận `audit_status` là `APPROVED` và `operation_status` là `ENABLE`.
5. **Xử lý sự cố**: Cập nhật lại tin nhắn nếu bị từ chối hoặc bật lại nếu bị vô hiệu hóa.

---

<a id="doc-1839594049581249"></a>
<!-- doc_id: 1839594049581249 -->
<!-- doc_id: 1839594049581249 -->
# Khởi tạo hội thoại qua liên kết ngắn & quảng cáo (Unlock conversations)
> Đường dẫn: Business Messaging API > Guides > Unlock conversations
Tài liệu này cung cấp hướng dẫn tổng quan về cách tạo và sử dụng hiệu quả Liên kết ngắn TikTok.me (TikTok.me Short Links) để nâng cao sự gắn kết với khách hàng, đồng thời giới thiệu về Quảng cáo Tin nhắn trực tiếp TikTok (TikTok Direct Messaging Ads).

## Giới thiệu
Tính năng Liên kết ngắn TikTok.me mang lại cơ hội mạnh mẽ cho các doanh nghiệp kết nối với khách hàng trên TikTok. Tính năng này cho phép người dùng mở ngay cuộc trò chuyện trực tiếp với tài khoản TikTok từ bất kỳ đâu.

## Liên kết ngắn TikTok.me (TikTok.me Short Links)
Liên kết ngắn TikTok.me đơn giản hóa việc tương tác của khách hàng từ bên ngoài ứng dụng:
- **Khởi đầu cuộc trò chuyện dễ dàng**: Khách hàng có thể bắt đầu nhắn tin ngay mà không cần tìm kiếm thủ công trong ứng dụng.
- **Thúc đẩy tương tác liền mạch**: Đưa khách hàng từ mọi kênh tiếp thị bên ngoài vào thẳng hệ sinh thái TikTok.
- **Tin nhắn tự động hóa và cá nhân hóa**: Cho phép truyền thêm tham số nguồn giới thiệu (`ref`) hoặc thông điệp soạn sẵn (`message`).
  - **Lưu ý**: Các tham số `ref` hoặc tin nhắn soạn trước chỉ hoạt động trên ứng dụng di động TikTok, không hoạt động trên phiên bản TikTok Web.

### Cách tạo Liên kết ngắn TikTok.me
1. Tạo liên kết cơ sở:
```text
tiktok.me/{uniqueusername}
```
Thay `{uniqueusername}` bằng tên người dùng (username) của tài khoản TikTok của bạn.

2. *(Tùy chọn)* Bổ sung các tham số:
   - `ref`: Tham số nguồn giới thiệu để theo dõi ngữ cảnh cuộc trò chuyện từ các kênh khác nhau. Chuỗi mã hóa URL có độ dài tối đa 2.083 ký tự (chỉ hỗ trợ chữ cái, chữ số và các ký tự đặc biệt `-`, `_`, `=`).
     - Ví dụ: `tiktok.me/{uniqueusername}?ref=facebook_campaign`
   - `message`: Nội dung tin nhắn được điền sẵn trong khung nhập tin nhắn của người dùng.
     - Ví dụ: `tiktok.me/{uniqueusername}?message=Xin%20chao,%20toi%20muon%20tu%20van%20san%20pham`

### Nơi triển khai Liên kết ngắn TikTok.me
- **Trang web**: Gắn vào mục "Liên hệ" hoặc nút tư vấn trên website bán hàng, trang bio mạng xã hội.
- **Ấn phẩm in ấn**: Chuyển đổi thành mã QR in trên áp phích, menu, danh thiếp hoặc bao bì sản phẩm.
- **Nút kêu gọi hành động (CTA) trong tin nhắn**: Bổ sung vào các chiến dịch gửi tin nhắn trên các kênh khác để người dùng chọn kết nối qua TikTok.

## Quảng cáo Tin nhắn trực tiếp TikTok (TikTok Direct Messaging Ads)
Doanh nghiệp cũng có thể chạy Quảng cáo Tin nhắn trực tiếp TikTok để thu hút khách hàng mở cuộc trò chuyện ngay sau khi xem video quảng cáo trên bảng tin.

---

<a id="doc-1832184306529874"></a>
<!-- doc_id: 1832184306529874 -->
<!-- doc_id: 1832184306529874 -->
# Bảng mã lỗi trả về (Return codes)
> Đường dẫn: Business Messaging API > Return codes
Bảng dưới đây liệt kê các mã lỗi trả về phổ biến khi gọi Business Messaging API không thành công:

| Code | Description |
|---|---|
| 40001 | Không có quyền thực hiện thao tác tương ứng. ⏎ **Cách khắc phục**: Đảm bảo bạn đã được cấp đầy đủ quyền hạn cần thiết và thử lại. |
| 40002 | Lỗi tham số. Vui lòng xem thông báo lỗi chi tiết để biết nguyên nhân. ⏎ **Nguyên nhân phổ biến**: • Thiếu trường bắt buộc. • Giá trị trường không đúng định dạng. • Giá trị hoặc trường không được hỗ trợ. • Xung đột giữa các trường truyền vào. ⏎ **Cách khắc phục**: Tham khảo tài liệu API để kiểm tra lại cách dùng tham số và gọi lại. |
| 40007 | Thao tác hoặc đối tượng không tồn tại. ⏎ **Nguyên nhân phổ biến**: • Chỉ định đối tượng không tồn tại. • Chỉ định URL đã ngừng hoạt động hoặc tệp không tồn tại. ⏎ **Cách khắc phục**: Đảm bảo đối tượng cần thao tác có tồn tại trên hệ thống và URL hợp lệ trước khi thử lại. |
| 40100 | Tần suất gửi yêu cầu quá nhanh. ⏎ **Nguyên nhân phổ biến**: Đã chạm ngưỡng giới hạn tốc độ (rate limit), yêu cầu bị chặn lại. ⏎ **Cách khắc phục**: Xem lại hạn mức tần suất gọi API hoặc liên hệ đại diện TikTok để kiểm tra quy tắc áp dụng cho tài khoản của bạn. |
| 40105 | Access token không hợp lệ hoặc không chính xác. ⏎ **Cách khắc phục**: Sử dụng access token hợp lệ và thử lại. Xem hướng dẫn cấp token tại [Xác thực (Authentication)](business-messaging-api.md#doc-1832184175482945). |
| 40908 | Định dạng tệp không được hỗ trợ. ⏎ **Cách khắc phục**: Đảm bảo tệp tải lên có định dạng được hỗ trợ và thử lại. |
| 40064 | Tin nhắn bị chặn do vi phạm quy tắc tin nhắn trực tiếp. ⏎ **Cách khắc phục**: Liên hệ với đại diện TikTok để kiểm tra quy tắc điều phối tin nhắn cụ thể đang áp dụng. |
| 51065 | Lỗi hệ thống nội bộ. ⏎ **Cách khắc phục**: Thử lại sau ít phút. Nếu lỗi vẫn tiếp diễn, liên hệ với bộ phận hỗ trợ kỹ thuật của TikTok. |

---

<a id="doc-1832184321030145"></a>
<!-- doc_id: 1832184321030145 -->
<!-- doc_id: 1832184321030145 -->
# Danh mục endpoint API (API Reference)
> Đường dẫn: Business Messaging API > API Reference
Nhắn tin là một phần thiết yếu trong cách doanh nghiệp duy trì hiện diện và giao thương với người dùng trên các nền tảng mạng xã hội. Business Messaging API là bộ giao diện lập trình cho phép các tài khoản TikTok doanh nghiệp đã được ủy quyền trao đổi tin nhắn trực tiếp với người dùng TikTok thông qua các nền tảng tích hợp.

Bạn có thể tham khảo [Tài liệu hướng dẫn](business-messaging-api.md#doc-1832184100272338) để tìm hiểu thêm về quy trình xác thực, ủy quyền, cấu trúc webhook và nhiều thông tin hữu ích khác.

Phân hệ này bao gồm các nhóm endpoint sau:

**Tin nhắn trực tiếp (Direct messages)**
- [Gửi tin nhắn trong cuộc trò chuyện](../12-api-reference/23-business-messaging.md#doc-1832184403754242)
- [Lấy danh sách các cuộc hội thoại](../12-api-reference/23-business-messaging.md#doc-1832184415059970)
- [Lấy danh sách tin nhắn trong cuộc hội thoại](../12-api-reference/23-business-messaging.md#doc-1832184425841170)
- [Tải hình ảnh lên](../12-api-reference/23-business-messaging.md#doc-1832184437720193)
- [Tải hình ảnh từ tin nhắn về](../12-api-reference/23-business-messaging.md#doc-1832184455450626)
- [Kiểm tra tính năng khả dụng của tài khoản TikTok](../12-api-reference/23-business-messaging.md#doc-1836061597865986)
- [Bật hoặc tắt tính năng Chuyển bình luận thành tin nhắn (Comment-to-Message)](../12-api-reference/23-business-messaging.md#doc-1843697551083522)
- [Lấy cấu hình Comment-to-Message của tài khoản TikTok](../12-api-reference/23-business-messaging.md#doc-1843697576682497)

**Cấu hình Webhooks**
- [Tạo cấu hình Business Messaging Webhook](../12-api-reference/23-business-messaging.md#doc-1832184470423554)
- [Lấy thông tin cấu hình Business Messaging Webhook](../12-api-reference/23-business-messaging.md#doc-1832184488625234)
- [Xóa cấu hình Business Messaging Webhook](../12-api-reference/23-business-messaging.md#doc-1832184497985537)

**Tin nhắn tự động (Automatic messages)**
- [Tạo tin nhắn tự động cho tài khoản TikTok](../12-api-reference/23-business-messaging.md#doc-1832184584869890)
- [Cập nhật tin nhắn tự động cho tài khoản TikTok](../12-api-reference/23-business-messaging.md#doc-1832184596566017)
- [Bật hoặc tắt tin nhắn tự động cho tài khoản TikTok](../12-api-reference/23-business-messaging.md#doc-1832184607786242)
- [Lấy danh sách tin nhắn tự động của tài khoản TikTok](../12-api-reference/23-business-messaging.md#doc-1832184619749377)
- [Xóa tin nhắn tự động của tài khoản TikTok](../12-api-reference/23-business-messaging.md#doc-1832184630106386)
- [Sắp xếp thứ tự tin nhắn tự động cho tài khoản TikTok](../12-api-reference/23-business-messaging.md#doc-1832184641212433)

---

## Hướng dẫn thực hành Data Retrieval bằng cURL

Dưới đây là các ví dụ lệnh **cURL** chuẩn để truy vấn và vận hành hệ thống **Business Messaging API**:

### 1. Lấy danh sách cuộc hội thoại đang hoạt động (Get Conversations)
```bash
curl -s -X GET "https://business-api.tiktok.com/open_api/v1.3/business/message/conversation/list/?business_id=YOUR_BUSINESS_ID&page_size=20"   -H "Access-Token: YOUR_ACCESS_TOKEN"
```

### 2. Gửi tin nhắn phản hồi văn bản (Send Direct Message)
```bash
curl -s -X POST "https://business-api.tiktok.com/open_api/v1.3/business/message/send/"   -H "Access-Token: YOUR_ACCESS_TOKEN"   -H "Content-Type: application/json"   -d '{
    "business_id": "YOUR_BUSINESS_ID",
    "conversation_id": "YOUR_CONVERSATION_ID",
    "message_type": "TEXT",
    "content": {
      "text": "Xin chào! Cảm ơn bạn đã liên hệ với thương hiệu của chúng tôi trên TikTok."
    }
  }'
```

### 3. Lấy cấu hình tin nhắn tự động (Get Auto Message Settings)
```bash
curl -s -X GET "https://business-api.tiktok.com/open_api/v1.3/business/message/auto_message/get/?business_id=YOUR_BUSINESS_ID&auto_message_type=WELCOME_MESSAGE"   -H "Access-Token: YOUR_ACCESS_TOKEN"
```
