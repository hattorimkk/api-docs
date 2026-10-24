# Hướng dẫn đo lường quảng cáo (Ad Measurement) — phần 1/2

> Phân hệ: guide:Marketing API/Ad Measurement.
> Tài liệu biên dịch kỹ thuật chi tiết theo chuẩn TikTok Business API v1.3.

---

## Mục lục điều hướng
- [1. Đo lường quảng cáo (Ad Measurement) (#doc-1739583617914881)](#doc-1739583617914881)
- [2. Tổng quan (Overview) (#doc-1757985960801281)](#doc-1757985960801281)
- [3. Hướng dẫn (Guides) (#doc-1757986592010242)](#doc-1757986592010242)
- [4. Events API 2.0 (#doc-1771100779668482)](#doc-1771100779668482)
- [5. Events API cho Web (Events API for Web) (#doc-1771100799076354)](#doc-1771100799076354)
- [6. Gửi TikTok Click ID (ttclid) (#doc-1771100879787009)](#doc-1771100879787009)
- [7. Gửi Cookie TikTok (_ttp) (#doc-1771100936446977)](#doc-1771100936446977)
- [8. Thiết lập External ID (#doc-1771100952291330)](#doc-1771100952291330)
- [9. Khử trùng lặp sự kiện (Event Deduplication) (#doc-1771100965992450)](#doc-1771100965992450)
- [10. Xác minh thiết lập Events API (#doc-1771100984456193)](#doc-1771100984456193)
- [11. Sử dụng Payload Helper cho Web (#doc-1807346079965186)](#doc-1807346079965186)
- [12. Câu hỏi thường gặp - Web (FAQs) (#doc-1771101001228290)](#doc-1771101001228290)
- [13. Events API cho Ngoại tuyến (Offline) (#doc-1771100815832065)](#doc-1771100815832065)
- [14. Xác minh thiết lập Offline Events API (#doc-1771101049613313)](#doc-1771101049613313)
- [15. Câu hỏi thường gặp - Ngoại tuyến (FAQs) (#doc-1771101064635394)](#doc-1771101064635394)
- [16. Events API cho Ứng dụng (App) (#doc-1771100838106114)](#doc-1771100838106114)
- [17. Xác minh thiết lập Events API cho App (#doc-1819583269559297)](#doc-1819583269559297)
- [18. Sử dụng Payload Helper cho App (#doc-1819581869993025)](#doc-1819581869993025)
- [19. Events API cho CRM (#doc-1835052243486786)](#doc-1835052243486786)
- [20. Xác minh thiết lập Events API cho CRM (#doc-1835052369704961)](#doc-1835052369704961)
- [21. Câu hỏi thường gặp - CRM (FAQs) (#doc-1835052398174274)](#doc-1835052398174274)
- [22. Xác thực (Authentication) (#doc-1771101130925058)](#doc-1771101130925058)
- [23. Phản hồi và mã lỗi (Responses and errors) (#doc-1771101162079234)](#doc-1771101162079234)
- [24. Các sự kiện được hỗ trợ (Supported events) (#doc-1771101186666498)](#doc-1771101186666498)
- [25. Sử dụng dữ liệu hạn chế (Limited data use) (#doc-1771101204435970)](#doc-1771101204435970)
- [26. Trình hỗ trợ tạo dữ liệu (Payload Helper) (#doc-1797165504155649)](#doc-1797165504155649)
- [27. Gửi dữ liệu phân bổ tùy chỉnh qua Events API 2.0 (#doc-1875218499994561)](#doc-1875218499994561)
- [28. Events API 1.0 (#doc-1739583647070209)](#doc-1739583647070209)
- [29. Events API: Web (1.0) (#doc-1739584809311234)](#doc-1739584809311234)
- [30. Bắt đầu (Get started) (#doc-1739584855420929)](#doc-1739584855420929)
- [31. Thiết lập Khớp nâng cao (Advanced Matching) (#doc-1749819614433282)](#doc-1749819614433282)
- [32. Thiết lập TikTok Click ID và Cookie (#doc-1739584860883969)](#doc-1739584860883969)
- [33. Thiết lập External ID (#doc-1765942670613506)](#doc-1765942670613506)
- [34. Xác minh thiết lập sự kiện (#doc-1739584863252481)](#doc-1739584863252481)
- [35. Khử trùng lặp sự kiện (Event deduplication) (#doc-1739584864945154)](#doc-1739584864945154)
- [36. Câu hỏi thường gặp - Web 1.0 (FAQs) (#doc-1749819287162881)](#doc-1749819287162881)
- [37. Events API: Ngoại tuyến (Offline 1.0) (#doc-1758049779688450)](#doc-1758049779688450)
- [38. Bắt đầu (Get Started) (#doc-1758051319816193)](#doc-1758051319816193)
- [39. Câu hỏi thường gặp - Ngoại tuyến 1.0 (FAQs) (#doc-1758052897775617)](#doc-1758052897775617)
- [40. Sử dụng dữ liệu hạn chế (Limited Data Use) (#doc-1770091656601602)](#doc-1770091656601602)
- [41. Cổng Events API (Events API Gateway) (#doc-1834543156864002)](#doc-1834543156864002)
- [42. Hướng dẫn thiết lập Self-Host (Self-Host setup guide) (#doc-1835087586303106)](#doc-1835087586303106)
- [43. Người thuê / Không gian quản lý (Tenants) (#doc-1835087595419649)](#doc-1835087595419649)
- [44. Quản lý người dùng (User management) (#doc-1835087602015234)](#doc-1835087602015234)
- [45. Cài đặt (Settings) (#doc-1835087607780546)](#doc-1835087607780546)
- [46. Tích hợp Pixel với Gateway (#doc-1835087630325761)](#doc-1835087630325761)
- [47. Gỡ cài đặt Events API Gateway (#doc-1835087643351106)](#doc-1835087643351106)
- [48. Nhật ký thay đổi (Changelog) (#doc-1771101231937537)](#doc-1771101231937537)
- [49. TikTok App Events SDK (#doc-1739583650172929)](#doc-1739583650172929)
- [50. Lịch sử phát hành (Release history) (#doc-1739584951798785)](#doc-1739584951798785)
- [51. Bắt đầu sử dụng SDK (Getting started) (#doc-1862119945765889)](#doc-1862119945765889)

---

<a id="doc-1739583617914881"></a>
<!-- doc_id: 1739583617914881 -->
<!-- doc_id: 1739583617914881 -->
# Đo lường quảng cáo (Ad Measurement)
> Đường dẫn: Marketing API > Đo lường quảng cáo (Ad Measurement)
Bạn có thể sử dụng các công cụ kết nối dữ liệu sự kiện để đo lường mức độ hiệu quả của quảng cáo.

- Để xem tổng quan về các công cụ kết nối dữ liệu sự kiện và cách bắt đầu, hãy xem [Tổng quan (Overview)](do-luong-quang-cao-p1.md#doc-1757985960801281).

- Để tìm hiểu các bước cấu hình chi tiết và các Sự kiện Ứng dụng hoặc Sự kiện Web được hỗ trợ, hãy xem [Hướng dẫn (Guides)](do-luong-quang-cao-p1.md#doc-1757986592010242).
	- [Events API](do-luong-quang-cao-p1.md#doc-1739583647070209)
	
	Sử dụng [App Events API](do-luong-quang-cao-tom-tat.md#doc-1739584805049345), [Website Events API](do-luong-quang-cao-p1.md#doc-1739584809311234) và [Offline Events API](do-luong-quang-cao-p1.md#doc-1758049779688450) để đo lường các sự kiện trong ứng dụng, sự kiện trên trang web và lượt chuyển đổi ngoại tuyến, rồi gửi dữ liệu về TikTok để xử lý hạ nguồn.

	- [TikTok App Events SDK](do-luong-quang-cao-p1.md#doc-1739583650172929)

	Tích hợp SDK Sự kiện của chúng tôi vào ứng dụng di động để gửi sự kiện trực tiếp tới TikTok.

	- [Ứng dụng di động (Mobile apps)](do-luong-quang-cao-p2.md#doc-1739583651652673)

	Quản lý các ứng dụng di động mà bạn muốn quảng bá.

	- [Pixel](do-luong-quang-cao-p2.md#doc-1739583652957185)

	Quản lý các pixel dùng để đo lường hiệu suất quảng cáo trên trang web.
	
- Để tìm hiểu danh sách các API hỗ trợ cho Sự kiện Ứng dụng và Sự kiện Web, hãy xem [Tham chiếu API (API Reference)](do-luong-quang-cao-p2.md#doc-1740963089558529).

---

<a id="doc-1757985960801281"></a>
<!-- doc_id: 1757985960801281 -->
<!-- doc_id: 1757985960801281 -->
# Tổng quan (Overview)
> Đường dẫn: Marketing API > Đo lường quảng cáo (Ad Measurement) > Tổng quan (Overview)
TikTok cung cấp các công cụ kết nối dữ liệu sự kiện mạnh mẽ giúp bạn đo lường hiệu quả quảng cáo. Dưới đây là tổng quan về các giải pháp kết nối dữ liệu sự kiện:

- Sự kiện ứng dụng (App Events)
  - Bạn có thể sử dụng **App Events API** hoặc [TikTok App Events SDK](do-luong-quang-cao-p1.md#doc-1739583650172929) để chia sẻ các sự kiện trong ứng dụng. Qua đó, bạn có thể tận dụng dữ liệu sự kiện này cho mục đích nhắm mục tiêu, đo lường và tối ưu hóa chiến dịch.
  
- Sự kiện trang web (Website Events)
  - Đối với nhà quảng cáo web, bạn có thể kết hợp cả [Web Events API](do-luong-quang-cao-p1.md#doc-1739584809311234) và [TikTok Pixel](do-luong-quang-cao-p2.md#doc-1739583652957185) để đo lường đầy đủ hành vi của khách truy cập trang web.

- Sự kiện ngoại tuyến (Offline Events)
  - Bạn có thể sử dụng [Offline Events API](do-luong-quang-cao-p1.md#doc-1758049779688450) để đo lường các lượt chuyển đổi diễn ra ngoại tuyến (tại cửa hàng, qua điện thoại) từ chiến dịch quảng cáo.
  
# Hướng dẫn bắt đầu (How to start)
- Tạo ứng dụng di động trên TikTok
	- Trước khi tạo quảng cáo, bạn nên gọi các endpoint liên quan để đăng ký và quản lý ứng dụng di động của mình. Xem chi tiết tại [App Events](../12-api-reference/43-events-1-0-p1.md#doc-1740857868662786).
- Triển khai App Events API hoặc App Events SDK
	- Để triển khai App Events API hoặc App Events SDK, bạn cần thực hiện các bước thiết lập tài khoản quảng cáo và tài khoản nhà phát triển tương ứng. Xem chi tiết tại [Events API: App](do-luong-quang-cao-tom-tat.md#doc-1739584805049345) và [TikTok App Events SDK](do-luong-quang-cao-p1.md#doc-1739583650172929).
- Triển khai Web Events API và Pixel
	- Để triển khai Web Events API, trước tiên bạn cần tạo Pixel và khởi tạo mã truy cập (access token). Xem chi tiết tại [Bắt đầu với Pixel](https://ads.tiktok.com/help/article?aid=10021&lang=en&redirected=1), [Events API : Web - Bắt đầu](do-luong-quang-cao-p1.md#doc-1739584855420929) và [Cài đặt Pixel bằng mã](do-luong-quang-cao-tom-tat.md#doc-1739585702922241).
- Triển khai Offline Events API
	- Để triển khai Offline Events API, trước tiên bạn cần tạo access token và tạo Bộ sự kiện ngoại tuyến (Offline Event set). Xem chi tiết tại [Events API: Offline - Bắt đầu](do-luong-quang-cao-p1.md#doc-1758051319816193).

---

<a id="doc-1757986592010242"></a>
<!-- doc_id: 1757986592010242 -->
<!-- doc_id: 1757986592010242 -->
# Hướng dẫn (Guides)
> Đường dẫn: Marketing API > Đo lường quảng cáo (Ad Measurement) > Hướng dẫn (Guides)
Phần này hướng dẫn chi tiết về Events API, TikTok App Events SDK, Ứng dụng di động (Mobile apps) và TikTok Pixel.
	
*	**[Events API](do-luong-quang-cao-p1.md#doc-1739583647070209)**

	Sử dụng [App Events API](do-luong-quang-cao-tom-tat.md#doc-1739584805049345), [Website Events API](do-luong-quang-cao-p1.md#doc-1739584809311234) và [Offline Events API](do-luong-quang-cao-p1.md#doc-1758049779688450) để đo lường sự kiện ứng dụng, sự kiện trang web và chuyển đổi ngoại tuyến, gửi về TikTok để phục vụ xử lý và tối ưu hóa hạ nguồn.

* **[TikTok App Events SDK](do-luong-quang-cao-p1.md#doc-1739583650172929)**

	Tích hợp SDK Sự kiện của TikTok vào ứng dụng di động để chuyển tiếp dữ liệu sự kiện thời gian thực.

* **[Ứng dụng di động (Mobile apps)](do-luong-quang-cao-p2.md#doc-1739583651652673)**

	Đăng ký và quản lý các ứng dụng di động mà bạn muốn quảng bá.

* **[Pixel](do-luong-quang-cao-p2.md#doc-1739583652957185)**

	Quản lý các đoạn mã Pixel nhằm theo dõi và đo lường hiệu suất chiến dịch quảng cáo web.

---

<a id="doc-1771100779668482"></a>
<!-- doc_id: 1771100779668482 -->
<!-- doc_id: 1771100779668482 -->
# Events API 2.0
> Đường dẫn: Marketing API > Đo lường quảng cáo (Ad Measurement) > Hướng dẫn (Guides) > Events API 2.0
> **Quan trọng:** 
> Bằng việc sử dụng các endpoint Events API, bạn đồng ý với [Điều khoản sản phẩm thương mại của TikTok (Dữ liệu)](https://ads.tiktok.com/i18n/official/policy/business-products-terms) và cam kết không chia sẻ dữ liệu nhạy cảm với TikTok.

> **Lưu ý:** 
> Events API 2.0 ([/event/track/](../12-api-reference/42-events-2-0.md#doc-1771101303285761)) hiện là endpoint được khuyến nghị để báo cáo sự kiện từ tất cả các nguồn, bao gồm web, ứng dụng (app), ngoại tuyến (offline) và hệ thống CRM (quản lý quan hệ khách hàng). Endpoint này cung cấp một cấu trúc schema API thống nhất giúp các nhà quảng cáo đơn giản hóa và tối ưu quy trình tích hợp.
> Để đảm bảo quá trình chuyển đổi suôn sẻ, sáu endpoint Events API 1.0 sau đây đã bắt đầu ngừng hoạt động từ H2 2024: • [/pixel/track/](../12-api-reference/43-events-1-0-p1.md#doc-1740858531237890) và [/pixel/batch/](../12-api-reference/43-events-1-0-p1.md#doc-1740858565852225) • [/offline/track/](../12-api-reference/43-events-1-0-p1.md#doc-1758428013689857) và [/offline/batch/](../12-api-reference/43-events-1-0-p1.md#doc-1758428053652482) • [/app/track/](../12-api-reference/43-events-1-0-p1.md#doc-1740859196043266) và [/app/batch/](../12-api-reference/43-events-1-0-p1.md#doc-1740859218541569)
> Chúng tôi đặc biệt khuyến nghị người dùng mới tích hợp trực tiếp với endpoint Events API 2.0, và người dùng Events API 1.0 hiện tại bắt đầu nâng cấp lên Events API 2.0 càng sớm càng tốt để tận dụng đầy đủ các lợi ích của phiên bản mới nhất.

## Giới thiệu
TikTok for Business cung cấp nhiều công cụ cho phép bạn chia sẻ hành động của khách hàng trên trang web với TikTok. Bằng cách chia sẻ dữ liệu sự kiện này, bạn có thể tối ưu hóa chiến dịch hiệu quả hơn và đo lường chính xác hiệu suất quảng cáo.

Events API của TikTok là giải pháp tích hợp bảo mật từ máy chủ đến máy chủ (server-to-server), cho phép nhà quảng cáo chia sẻ trực tiếp các hành động của khách hàng trên **trang web**, **ứng dụng**, **kênh ngoại tuyến** hoặc hệ thống **CRM** với TikTok.

Events API 2.0 ([/event/track/](../12-api-reference/42-events-2-0.md#doc-1771101303285761)) hiện là endpoint được khuyến nghị hàng đầu để báo cáo sự kiện từ tất cả các nguồn. Endpoint này mang đến schema API hợp nhất giúp đơn giản hóa việc tích hợp.

## Xác thực (Authentication)
Để xác thực các lệnh gọi Events API, bạn cần có mã truy cập (access token). Bạn có thể tạo access token trực tiếp trong Trình quản lý sự kiện (Events Manager) (**khuyến nghị**) hoặc bằng ứng dụng nhà phát triển riêng nếu đã có. Để tìm hiểu cách lấy access token, vui lòng tham khảo [Events API 2.0 - Xác thực](do-luong-quang-cao-p1.md#doc-1771101130925058).

## Bảng tham số (Parameters) tổng quan
Dưới đây là tổng quan cấp cao về schema payload của Events API 2.0. Để xem danh sách đầy đủ các tham số và thông tin chi tiết từng trường, tham khảo [Tham chiếu API - Events 2.0](../12-api-reference/42-events-2-0.md#doc-1771101276978178).

Lưu ý rằng các nguồn sự kiện khác nhau (như web, app, offline và hệ thống CRM) có các bộ trường bắt buộc và khuyến nghị khác nhau, cũng như các phương pháp tối ưu riêng. Xem hướng dẫn thiết lập chi tiết cho từng loại:
- [Hướng dẫn thiết lập cho Web](do-luong-quang-cao-tom-tat.md#doc-1771100865818625)
- [Hướng dẫn thiết lập cho Ngoại tuyến](do-luong-quang-cao-tom-tat.md#doc-1771101027431425)
- [Hướng dẫn thiết lập cho Ứng dụng](do-luong-quang-cao-tom-tat.md#doc-1771101111730178)
- [Hướng dẫn thiết lập cho CRM](do-luong-quang-cao-tom-tat.md#doc-1835052338764993)

| Field | Data Type | Note |
|---|---|---|
| event_source  ****(Bắt buộc)**** | string | Hiện tại, các giá trị enum là `web`, `app`, `offline` và `crm`. |
| event_source_id  ****(Bắt buộc)**** | string | ID nguồn sự kiện dùng để đo lường sự kiện. |
| data  ****(Bắt buộc)**** | object[] | Mảng đối tượng chứa danh sách các sự kiện bạn muốn báo cáo. |
| ↳ event  ****(Bắt buộc)**** | string | Tên sự kiện chuyển đổi. Có thể là sự kiện chuẩn hoặc sự kiện tùy chỉnh. |
| ↳ event_time ****(Bắt buộc)**** | integer | Dấu thời gian Unix (giây) khi sự kiện xảy ra. |
| ↳ event_id | string | ID duy nhất dùng để thiết lập khử trùng lặp sự kiện. ⏎ Để tìm hiểu thêm về khử trùng lặp, tham khảo [Events API 2.0 - Khử trùng lặp sự kiện](do-luong-quang-cao-p1.md#doc-1771100965992450). |
| ↳ limited_data_use | boolean | Trường này chỉ hỗ trợ khi `event_source` là `web` hoặc `app`. ⏎ Cài đặt xử lý dữ liệu hạn chế. ⏎ Để tìm hiểu thêm về tính năng Sử dụng dữ liệu hạn chế, tham khảo [Events API 2.0 - Sử dụng dữ liệu hạn chế](do-luong-quang-cao-p1.md#doc-1771101204435970). |
| ↳ user | object | **Thông tin về người dùng.** ⏎ Để xem danh sách các trường trong đối tượng user, tham khảo phần "[Các tham số `user`](../12-api-reference/42-events-2-0.md#doc-1771101303285761)". |
| ↳ properties | object | **Thông tin về sản phẩm hoặc đơn hàng.** ⏎ Để xem danh sách các trường trong đối tượng properties, tham khảo phần "[Các tham số `properties`](../12-api-reference/42-events-2-0.md#doc-1771101303285761)". |
| ↳ page **(Điều kiện)** | object | **Thông tin về trang web** - Bắt buộc khi báo cáo sự kiện web. ⏎ Để xem danh sách các trường trong đối tượng page, tham khảo phần "[Các tham số `page`](../12-api-reference/42-events-2-0.md#doc-1771101303285761)". |
| ↳ app **(Điều kiện)** | object | **Thông tin về ứng dụng** - Bắt buộc khi báo cáo sự kiện ứng dụng. ⏎ Để xem danh sách các trường trong đối tượng app, tham khảo phần "[Các tham số `app`](../12-api-reference/42-events-2-0.md#doc-1771101303285761)". |
| ↳ ad **(Điều kiện)** | object | **Thông tin về quảng cáo** - Chỉ dùng khi báo cáo sự kiện app. ⏎ Để xem danh sách các trường trong đối tượng ad, tham khảo phần "[Các tham số `ad`](../12-api-reference/42-events-2-0.md#doc-1771101303285761)". |
| ↳ lead **(Điều kiện)** | object | **Thông tin về khách hàng tiềm năng (lead)** - Bắt buộc khi báo cáo sự kiện CRM. ⏎ Để xem danh sách các trường trong đối tượng `lead`, tham khảo phần "[Các tham số `lead`](../12-api-reference/42-events-2-0.md#doc-1771101303285761)". |

## Sự kiện đơn lẻ so với sự kiện theo lô (Single event vs. Batched event)
Endpoint `/event/track/` chấp nhận cả sự kiện đơn lẻ (khi một đối tượng duy nhất được truyền vào tham số `data`) hoặc một lô nhiều sự kiện (khi mảng nhiều đối tượng được truyền vào tham số `data`). Lưu ý rằng mỗi yêu cầu chỉ có thể gửi tối đa 1.000 sự kiện.

Mặc dù có thể gửi theo lô, chúng tôi **đặc biệt khuyến nghị** bạn nên gửi từng sự kiện đơn lẻ ngay khi máy chủ nhận được sự kiện. Phương thức này giúp TikTok tận dụng tối đa dữ liệu thời gian thực để đo lường và tối ưu hóa hiệu suất chiến dịch quảng cáo.

### Ví dụ lệnh cURL: Gửi một sự kiện đơn lẻ
Dưới đây là ví dụ gửi sự kiện web tối thiểu qua Events API bằng lệnh cURL POST:

**Điều kiện tiên quyết**: Bạn cần có ID TikTok Pixel và access token hợp lệ để thay thế cho `{{Access-Token}}` và `{{Pixel-Code}}` trong dữ liệu mẫu. Để biết cách lấy access token và ID Pixel, xem [Hướng dẫn thiết lập cho Web](do-luong-quang-cao-tom-tat.md#doc-1771100865818625).

```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/event/track/' --header 'Access-Token: {{Access-Token}}' --header 'Content-Type: application/json' --data-raw '{
  "event_source": "web",
  "event_source_id": "{{Pixel-Code}}",
  "data": [
    {
      "event": "Purchase",
      "event_time": 1684574395,
      "user": {
        "email": "848a771458438fc2ec420560d769fb9b9b86851ee338ec56517baabd79d3bb4f",
        "phone": "2f9d2b4df907e5c9a7b3434351b55700167b998a83dc479b825096486ffcf4ea",
        "ip": "139.177.225.245",
        "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.1 Safari/605.1.15"
      },
      "page": {
        "url": "http://www.example.com/purchase?q=hello"
      }
    }
  ]
}'
```

Nếu TikTok nhận sự kiện thành công, API sẽ trả về phản hồi với mã trạng thái HTTP `200` và mã phản hồi API (`code`) bằng `0`. Dưới đây là ví dụ về phản hồi thành công:

```http
// curl
HTTP 1.1 200 OK
{
  "message": "OK",
  "code": 0,
  "request_id": "{{request_id}}",
  "data":{} 
}
```

Nếu yêu cầu thất bại, bạn sẽ nhận được mã trạng thái HTTP `4XX` hoặc `5XX` kèm mã lỗi và thông báo chi tiết trong phần thân phản hồi giải thích nguyên nhân thất bại. Xem [Events API 2.0 - Phản hồi và mã lỗi](do-luong-quang-cao-p1.md#doc-1771101162079234) để biết thêm chi tiết.

## Giới hạn API (API limits)
Events API 2.0 (`/event/track/`) có giới hạn tần suất là 1.000 QPS (lượt truy vấn mỗi giây) trên mỗi tài khoản quảng cáo (khi sử dụng Events Manager để tạo access token) hoặc ứng dụng nhà phát triển (khi sử dụng ứng dụng nhà phát triển riêng). Xem chi tiết tại [Giới hạn tần suất](../04-get-started/bat-dau.md#doc-1740029171730433).

Nếu doanh nghiệp của bạn yêu cầu mức QPS cao hơn hạn mức mặc định 1.000, vui lòng liên hệ đại diện TikTok của bạn.

## Tài liệu liên quan (Related docs)
- [Giới thiệu về Events API](https://ads.tiktok.com/help/article/events-api?lang=en)
- [Events API cho Web](do-luong-quang-cao-tom-tat.md#doc-1771100865818625)
- [Events API cho Ngoại tuyến](do-luong-quang-cao-tom-tat.md#doc-1771101027431425)
- [Events API cho Ứng dụng](do-luong-quang-cao-tom-tat.md#doc-1771101111730178)
- [Events API cho CRM](do-luong-quang-cao-tom-tat.md#doc-1835052338764993)
- [Xác thực](do-luong-quang-cao-p1.md#doc-1771101130925058)
- [Các tham số](do-luong-quang-cao-tom-tat.md#doc-1771101151059969)
- [Phản hồi và mã lỗi](do-luong-quang-cao-p1.md#doc-1771101162079234)
- [Các sự kiện được hỗ trợ](do-luong-quang-cao-p1.md#doc-1771101186666498)
- [Sử dụng dữ liệu hạn chế](do-luong-quang-cao-p1.md#doc-1771101204435970)
- [Nhật ký thay đổi](do-luong-quang-cao-p1.md#doc-1771101231937537)
- [Báo cáo sự kiện App, Web, Ngoại tuyến hoặc CRM](../12-api-reference/42-events-2-0.md#doc-1771101303285761)

---

<a id="doc-1771100799076354"></a>
<!-- doc_id: 1771100799076354 -->
<!-- doc_id: 1771100799076354 -->
# Events API cho Web (Events API for Web)
> Đường dẫn: Marketing API > Đo lường quảng cáo (Ad Measurement) > Hướng dẫn (Guides) > Events API 2.0 > Events API cho Web
> **Quan trọng:** 
> Bằng việc sử dụng các endpoint Events API, bạn đồng ý với [Điều khoản sản phẩm thương mại của TikTok (Dữ liệu)](https://ads.tiktok.com/i18n/official/policy/business-products-terms) và cam kết không chia sẻ dữ liệu nhạy cảm với TikTok.

> **Lưu ý:** 
> Events API 2.0 ([/event/track/](../12-api-reference/42-events-2-0.md#doc-1771101303285761)) hiện là endpoint được khuyến nghị để báo cáo sự kiện từ tất cả các nguồn, bao gồm web, app, offline và hệ thống CRM. Endpoint này cung cấp một cấu trúc schema API hợp nhất giúp tối ưu quy trình tích hợp.
> Để đảm bảo quá trình chuyển đổi suôn sẻ, sáu endpoint Events API 1.0 sau đây đã bắt đầu ngừng hoạt động từ H2 2024: • [/pixel/track/](../12-api-reference/43-events-1-0-p1.md#doc-1740858531237890) và [/pixel/batch/](../12-api-reference/43-events-1-0-p1.md#doc-1740858565852225) • [/offline/track/](../12-api-reference/43-events-1-0-p1.md#doc-1758428013689857) và [/offline/batch/](../12-api-reference/43-events-1-0-p1.md#doc-1758428053652482) • [/app/track/](../12-api-reference/43-events-1-0-p1.md#doc-1740859196043266) và [/app/batch/](../12-api-reference/43-events-1-0-p1.md#doc-1740859218541569)
> Chúng tôi đặc biệt khuyến nghị người dùng mới tích hợp trực tiếp với Events API 2.0 và người dùng Events API 1.0 nâng cấp sớm nhất có thể.

Phần này giới thiệu cách quản lý và gửi Sự kiện Web thông qua Events API 2.0:
- [Hướng dẫn thiết lập cho Web](do-luong-quang-cao-tom-tat.md#doc-1771100865818625)

---

<a id="doc-1771100879787009"></a>
<!-- doc_id: 1771100879787009 -->
<!-- doc_id: 1771100879787009 -->
# Gửi TikTok Click ID (ttclid)
> Đường dẫn: Marketing API > Đo lường quảng cáo (Ad Measurement) > Hướng dẫn (Guides) > Events API 2.0 > Events API cho Web > Gửi TikTok Click ID (ttclid)
# TikTok Click ID (`ttclid`)
TikTok Click ID (`ttclid`) là tham số kết nối dữ liệu được tự động nối vào URL trang đích của bạn khi người dùng nhấp vào một quảng cáo TikTok. Dưới đây là ví dụ về URL có tham số `ttclid`: `https://www.example.com/landing?ttclid=E.C.P.v3fQ2RHacdksKfofPmlyuStIIHJ4Af1tKYxF9zz2c2PLx1Oaw15oHpcfl5AH`.

Chúng tôi **đặc biệt khuyến nghị** bạn gửi lại `ttclid` qua Events API 2.0 cho mọi sự kiện diễn ra trên trang web của bạn. Việc này giúp TikTok liên kết chính xác các sự kiện trên trang web với lượt nhấp vào quảng cáo, từ đó giúp TikTok báo cáo và tối ưu hóa hiệu suất chiến dịch tốt hơn.

Để biết thêm chi tiết về TikTok Click ID, hãy xem [TikTok Click ID](https://ads.tiktok.com/help/article/tiktok-click-id?redirected=2).

# Lưu trữ `ttclid` (Store the ttclid)
TikTok chỉ nối tham số `ttclid` vào URL trang đích của quảng cáo. Bạn nên lưu giữ giá trị `ttclid` trong toàn bộ phiên truy cập của người dùng trên trang web để có thể gửi kèm qua Events API cho tất cả sự kiện trong phiên đó. Có ba phương án để lưu trữ `ttclid`:
- Duy trì tham số `ttclid` trong URL khi trang web chuyển hướng giữa các trang (ví dụ từ trang đích sang trang chi tiết sản phẩm), và gửi URL đầy đủ (kèm các tham số truy vấn) trong trường `page.url` của payload API. Backend của API sẽ tự động phân tích Click ID nếu phát hiện sự hiện diện của tham số `ttclid` trong `page.url`.
- Nếu bạn đã cài đặt TikTok Pixel trên trang web, Pixel sẽ tự động trích xuất `ttclid` từ URL trang đích và lưu giá trị đó vào cookie. Bạn có thể đọc giá trị cookie này mỗi khi gửi yêu cầu Events API. Xem phần "Lấy Click ID bằng TikTok Pixel" bên dưới.
- Bạn cũng có thể tự phân tích `ttclid` từ URL trang đích và lưu trữ bằng cookie trình duyệt hoặc session storage. Xem phần "Tự lưu trữ Click ID" bên dưới.

> **Lưu ý:** Bạn đặc biệt nên triển khai ít nhất một trong ba phương án trên.

Nếu có thêm tài nguyên kỹ thuật, bạn cũng có thể lưu trữ `ttclid` trên hệ thống backend để phục vụ đối chiếu liên trình duyệt hoặc liên thiết bị. Xem phần "Lưu trữ liên trình duyệt hoặc liên thiết bị" bên dưới.

## Lấy Click ID bằng TikTok Pixel (Get Click ID with TikTok Pixel)
Nếu bạn đã cài đặt TikTok Pixel trên trang web, Pixel sẽ tự động trích xuất `ttclid` từ URL trang đích và lưu trữ giá trị dưới dạng cookie của bên thứ nhất trên miền trang web của bạn. Tên của cookie này cũng là `ttclid`.

Để truy xuất `ttclid` trên máy chủ web, bạn có thể phân tích cú pháp tiêu đề yêu cầu HTTP cookie và báo cáo qua Events API. Xem phần "Gửi ttclid qua Events API" bên dưới.

Ngoài ra, bạn có thể lấy Click ID bằng cách đọc cookie `ttclid` từ kho cookie trình duyệt phía client, sau đó gửi lên server để báo cáo qua Events API. Dưới đây là đoạn mã JavaScript mẫu để đọc cookie:

```http
// curl
function getCookie(name) {
  let cookie = {};
  document.cookie.split(';').forEach(function(el) {
    let [k,v] = el.split('=');
    cookie[k.trim()] = v;
  })
  return cookie[name];
}
getCookie('ttclid')// TikTok Click ID
```

## Tự lưu trữ Click ID (Store the Click ID on your own)
Nếu bạn chưa cài đặt TikTok Pixel trên trang web, bạn có thể tự phân tích và lưu trữ `ttclid`. Khuyến nghị sử dụng bộ lưu trữ cookie của trình duyệt hoặc HTML5 local storage:
- Thời gian sống (TTL - time-to-live) lưu trữ được khuyến nghị là 28 ngày trở lên (TikTok sẽ tự xử lý việc hết hạn của Click ID dựa trên cài đặt cửa sổ phân bổ của nhà quảng cáo).
- Nếu phát hiện thấy giá trị `ttclid` mới trên URL trang đích, bạn nên cập nhật giá trị đã lưu sang giá trị mới nhất.

Dưới đây là mã mẫu sử dụng bộ lưu trữ cookie (**khuyến nghị**):

```http
// curl
// Get the ttclid parameter from the URL
const urlSearchParams = new URLSearchParams(window.location.search);
const ttclidValue = urlSearchParams.get('ttclid');
if (ttclidValue) {
  // Set the cookie with the ttclid value and a 28-day expiration date
  expirationDate.setDate(new Date().getDate() + 28);
  // save the value in a cookie named ttclid
  document.cookie = `ttclid=${ttclidParam}; expires=${expirationDate.toUTCString()}; path=/`;
}
```
Dưới đây là mã mẫu sử dụng HTML5 local storage:
```http
// curl
// Get the ttclid parameter value from the URL
const urlParams = new URLSearchParams(window.location.search);
const ttclidValue = urlParams.get('ttclid');

// Save ttclid to local storage with expiration of 28 days
if (ttclidValue) {
  let expirationDate = new Date(new Date().getDate() + 28)
    let data = {
      value: ttclid,
      expirationDate: expirationDate.toISOString()
  }
  // save the value in local storage with key='ttclid'
  localStorage.setItem('ttclid', data);
}
```
Đối với mỗi sự kiện kích hoạt trên trang web của bạn, hãy đưa dữ liệu sự kiện kèm `ttclid` vào yêu cầu từ máy chủ để báo cáo qua Events API. Xem phần "Gửi ttclid qua Events API" bên dưới.

## Lưu trữ liên trình duyệt hoặc liên thiết bị *(Không bắt buộc)* (Cross-browser or device storage)
Nếu bạn muốn liên kết các hành động của khách hàng giữa các trình duyệt hoặc thiết bị khác nhau với một lượt nhấp vào quảng cáo (ví dụ: người dùng nhấp vào quảng cáo trên máy tính xách tay và sau đó mua hàng trên trình duyệt điện thoại di động), bạn có thể lưu trữ `ttclid` trong cơ sở dữ liệu của mình. Dưới đây là các nguyên tắc chung:
1. Thu thập và lưu giữ giá trị `ttclid` cho đến khi bạn có thể định danh người dùng:
- Để cải thiện hiệu suất quảng cáo, hãy lưu giữ `ttclid` cho đến khi bạn có thể định danh người dùng nội bộ qua tài khoản, gói đăng ký, chương trình khách hàng thân thiết, hoặc qua các mã định danh như cookie ID, email, số điện thoại hoặc anonymous ID.
2. Duy trì bảng liên kết giữa người dùng và `ttclid` trong cơ sở dữ liệu:
- Tạo một bảng trong hệ thống backend duy trì mối quan hệ giữa người dùng và giá trị `ttclid`, chẳng hạn như `ttclid <-> email`, `ttclid <-> external_id`.
- Nếu cùng một người dùng nhấp vào quảng cáo của bạn ở một thời điểm khác, một `ttclid` mới sẽ được tạo ra. Đảm bảo ghi đè giá trị `ttclid` cũ bằng giá trị mới mỗi lần người dùng nhấp vào quảng cáo.
3. Gửi sự kiện web kèm `ttclid` qua Events API:
- Khi các sự kiện web được kích hoạt, bạn sẽ tra cứu mối liên kết người dùng - `ttclid` và truyền giá trị `ttclid` vào payload API. Xem chi tiết tại phần "Gửi ttclid qua Events API" bên dưới.

# Gửi `ttclid` qua Events API (Send the ttclid via Events API)
Báo cáo các sự kiện của người dùng bằng cách đưa `ttclid` vào trường `user.ttclid` của Events API qua endpoint [/event/track/](../12-api-reference/42-events-2-0.md#doc-1771101303285761). Để xem hướng dẫn hoàn chỉnh về cách báo cáo sự kiện web và các tham số liên quan, tham khảo [Events API 2.0 - Hướng dẫn thiết lập cho Web](do-luong-quang-cao-tom-tat.md#doc-1771100865818625).
> **Lưu ý:** 
> `ttclid` có thể dài tối đa 1.000 ký tự, vì vậy hãy đảm bảo hệ thống máy chủ của bạn không cắt ngắn chuỗi này.
```http
// curl
  "user": {
  "ttclid": "E.C.P.v3fQ2RHacdksKfofPmlyuStIIHJ4Af1tKYxF9zz2c2PLx1Oaw15oHpcfl5AH",
  // ... ...
},
```

 
# Xóa `ttclid` khỏi URL trang đích (Remove ttclid from landing page URLs)
Nếu muốn xóa tham số `ttclid` khỏi URL trang đích, bạn có thể thực hiện theo chương trình hoặc chỉnh sửa mã trang web tương tự như cách quản lý các tham số truy vấn khác. Dưới đây là đoạn mã JavaScript mẫu để loại bỏ tham số `ttclid` khỏi URL:

```http
// curl
// Add this before pixel tag
<script>
  const myurl = new URL(location.href);  // build a url object from current url
  myurl.searchParams.delete('ttclid');  // remove all ttclid url parameters
  history.replaceState({}, '', myurl);  // replace current url with updated one
</script>
```

---

<a id="doc-1771100936446977"></a>
<!-- doc_id: 1771100936446977 -->
<!-- doc_id: 1771100936446977 -->
# Gửi Cookie TikTok (_ttp)
> Đường dẫn: Marketing API > Đo lường quảng cáo (Ad Measurement) > Hướng dẫn (Guides) > Events API 2.0 > Events API cho Web > Gửi Cookie TikTok (_ttp)
# Cookie `_ttp`
Khi bạn bật cookie của bên thứ nhất trong phần cài đặt TikTok Pixel, TikTok sẽ tự động lưu trữ một mã nhận dạng duy nhất trong cookie của bên thứ nhất có tên là `_ttp` trên miền trang web của bạn.

Đối với người dùng Events API 2.0 đã cài đặt TikTok Pixel trên trang web, chúng tôi khuyến nghị bạn đính kèm giá trị cookie `ttp` vào payload của Events API. Giá trị cookie này được dùng để nâng cao khả năng khớp các sự kiện của khách truy cập trang web với quảng cáo TikTok. Xem chi tiết tại [Sử dụng Cookie với TikTok Pixel](https://ads.tiktok.com/help/article/using-cookies-with-tiktok-pixel?redirected=2).

# Gửi Cookie `_ttp` qua Events API
Để lấy giá trị cookie `_ttp` trên máy chủ web, bạn có thể phân tích cú pháp từ tiêu đề HTTP cookie của yêu cầu đến.

Khi báo cáo sự kiện người dùng qua Events API, hãy đưa giá trị cookie `_ttp` vào trường `user.ttp` trong payload API. Để xem hướng dẫn chi tiết về cách báo cáo sự kiện web và các tham số liên quan, tham khảo [Events API 2.0 - Hướng dẫn thiết lập cho Web](do-luong-quang-cao-tom-tat.md#doc-1771100865818625).

Dưới đây là ví dụ về cách truyền giá trị cookie `_ttp` trong payload Events API:

```http
// curl
"user": {
  "ttp": "UqBuLHl7TuWsDXUu-ViOGOLA5YP",
  // ... ...
},
```

---

<a id="doc-1771100952291330"></a>
<!-- doc_id: 1771100952291330 -->
<!-- doc_id: 1771100952291330 -->
# Thiết lập External ID
> Đường dẫn: Marketing API > Đo lường quảng cáo (Ad Measurement) > Hướng dẫn (Guides) > Events API 2.0 > Events API cho Web > Thiết lập External ID
External ID (ID định danh bên ngoài) là mã nhận dạng đại diện cho người dùng trên nền tảng của nhà quảng cáo, chẳng hạn như ID khách hàng, số thẻ thành viên hoặc mã đơn hàng. Khi được chia sẻ, TikTok sẽ tìm cách khớp ID này với người dùng trên TikTok. Việc này làm tăng tỷ lệ khớp, mang lại lợi ích lớn trong việc đo lường và tối ưu hóa hạ nguồn.

External ID có thể được gửi tới TikTok bằng một trong các công cụ TikTok for Business: Pixel SDK hoặc Events API.

# Lợi ích (Benefits)
Nếu bạn gán ID cho người dùng truy cập trang web, External ID cho phép bạn:
- **Cải thiện hiệu suất tín hiệu**: Nâng cao tỷ lệ khớp trên các kênh và ghi nhận được nhiều sự kiện hơn.
- **Tăng cường tối ưu hóa chiến dịch**: Hỗ trợ các mô hình đặt giá thầu chiến dịch để tối đa hóa số lượng sự kiện chuyển đổi.
- **Đo lường toàn bộ phễu sự kiện**: Nắm bắt nhiều sự kiện hơn nhờ khả năng khớp dữ liệu hoàn chỉnh giữa các thiết bị và các phiên truy cập.

> **Lưu ý:** 
> Để tối đa hóa lợi ích của External ID, bạn nên thiết lập đồng thời cả Khớp thủ công (Manual Matching) và Khớp tự động (Automatic Matching). Xem hướng dẫn Khớp nâng cao cho Pixel SDK tại [đây](do-luong-quang-cao-p2.md#doc-1739585700402178).

# Cách thức hoạt động của External ID
1. Người dùng xem một sản phẩm cụ thể trên trang web của bạn.
2. Bạn gửi sự kiện `ViewContent` qua Pixel trình duyệt chứa:
- Giá trị băm của `external id` cho người dùng đó.
- Một hoặc cả hai thông tin sau:
  - Thông tin PII của khách hàng đã băm (email/số điện thoại).
  - Thông tin cookie được tự động đính kèm trong tất cả pixel.
3. Phía TikTok sử dụng dữ liệu PII đã băm liên kết với external ID để tìm kiếm kết quả khớp. Nếu tìm thấy, TikTok sẽ liên kết external ID được cung cấp với người dùng TikTok đó.
4. Vài ngày sau, chính người dùng đó hoàn tất giao dịch mua hàng trên trang web của bạn.
5. Bạn gửi cho chúng tôi một sự kiện mới qua Events API. Lần này, bạn gửi kèm `external_id`.
6. TikTok nhận được `external_id` và khớp tín hiệu này với hoạt động duyệt web trước đó của khách hàng từ kết quả khớp PII - người dùng TikTok trước đó.
7. Tín hiệu này sau đó được sử dụng ở hạ nguồn để cải thiện hiệu suất chiến dịch của bạn.

# Quản lý External ID
Nếu bạn đang chia sẻ `external_id` qua TikTok Pixel SDK hoặc Events API nhưng không muốn TikTok sử dụng tham số này cho mục đích khớp hoặc đo lường, vui lòng cập nhật lại cấu hình để loại bỏ trường `external_id`.

---

<a id="doc-1771100965992450"></a>
<!-- doc_id: 1771100965992450 -->
<!-- doc_id: 1771100965992450 -->
# Khử trùng lặp sự kiện (Event Deduplication)
> Đường dẫn: Marketing API > Đo lường quảng cáo (Ad Measurement) > Hướng dẫn (Guides) > Events API 2.0 > Events API cho Web > Khử trùng lặp sự kiện
**Để đạt hiệu suất quảng cáo tốt nhất, chúng tôi khuyến nghị nhà quảng cáo thiết lập đồng thời cả TikTok Pixel SDK và Events API để đảm bảo phạm vi bao phủ dữ liệu tối đa.**

Khử trùng lặp là tính năng cần thiết cho nhà quảng cáo đang gửi cùng một sự kiện từ cả hai nguồn TikTok Pixel SDK và Events API. Ví dụ: nếu bạn gửi cùng một sự kiện từ cả TikTok Pixel SDK và Events API, bạn cần thiết lập cơ chế khử trùng lặp bằng `event_id` hoặc cookie của bên thứ nhất (`_ttp`). Việc này cho phép TikTok loại bỏ các bản sao trùng lặp của cùng một sự kiện, giúp báo cáo và tối ưu hóa hiệu suất chiến dịch chính xác hơn. Chi tiết xem tại [Khử trùng lặp sự kiện](https://ads.tiktok.com/help/article/event-deduplication?redirected=2).

# `event_id` (Khuyến nghị)
TikTok thực hiện khử trùng lặp sự kiện dựa trên bộ giá trị `event_source_id`, `event` (ví dụ `Purchase` hoặc `AddToCart`) và `event_id`. Nhà quảng cáo nên chọn một chuỗi ký tự duy nhất làm `event_id` cho mỗi sự kiện. Số đơn hàng hoặc mã giao dịch rất phù hợp để dùng làm `event_id`. Nếu không có sẵn các mã này, bạn có thể tạo một số ngẫu nhiên duy nhất, nhưng mã này phải giống nhau hoàn toàn giữa sự kiện gửi qua Pixel SDK và sự kiện gửi qua Events API để cơ chế khử trùng lặp hoạt động.

Nếu nhận được nhiều sự kiện có cùng bộ `event_source_id`, `event` và `event_id`, chúng tôi sẽ giữ lại sự kiện đầu tiên và loại bỏ mọi sự kiện đến sau trong vòng 48 giờ kể từ sự kiện đầu tiên. Nếu sự kiện đến sau được nhận trong vòng 5 phút kể từ sự kiện đầu tiên, chúng tôi sẽ tiến hành hợp nhất dữ liệu của nó vào sự kiện đầu tiên. Ví dụ: nếu sự kiện đầu tiên không có `user.email` nhưng sự kiện trùng lặp đến sau (trong vòng 5 phút) có chứa thông tin này, hệ thống sẽ hợp nhất dữ liệu email vào sự kiện đầu tiên.

Dưới đây là một số ví dụ về cách gán `event_id` cho sự kiện TikTok Pixel SDK và sự kiện Events API:

## Ví dụ mã Pixel SDK (Pixel SDK code example)

## Ví dụ Events API dùng cURL (Events API example using curl)

# Khử trùng lặp bằng Cookie (Cookie)

Nếu bạn không gửi `event_id` từ Events API nhưng có gửi cookie TikTok (`_ttp`), chúng tôi sẽ tìm cách khử trùng lặp giữa các sự kiện từ trình duyệt và máy chủ dựa trên giá trị của cookie `_ttp`.

Để tận dụng cơ chế khử trùng lặp dựa trên cookie, bạn cần bật cookie của bên thứ nhất trong phần cài đặt pixel. Sau đó, pixel trình duyệt sẽ tự động lưu trữ một mã nhận dạng duy nhất trong cookie bên thứ nhất có tên là `_ttp`. Khi báo cáo sự kiện qua Events API, hãy gửi kèm giá trị cookie `_ttp` trong trường `user.ttp` của payload API. Xem [Gửi Cookie TikTok](do-luong-quang-cao-p1.md#doc-1771100936446977).

Cơ chế khử trùng lặp qua cookie sử dụng kết hợp bộ ba [`pixelCode`, `event`, `_ttp`] làm khóa khử trùng lặp, với cửa sổ khử trùng lặp là 5 phút. Điều này có nghĩa là sau khi nhận được sự kiện duy nhất đầu tiên, hệ thống sẽ phát hiện và loại bỏ các sự kiện đến trong 5 phút tiếp theo có cùng bộ [`pixelCode`, `event`, `_ttp`].

Một số hạn chế của phương pháp khử trùng lặp này:
- Khử trùng lặp qua cookie sẽ chỉ loại bỏ các sự kiện gửi từ Events API, cụ thể là khi có một sự kiện từ pixel trình duyệt có cùng [`pixelCode`, `event`, `_ttp`] được nhận trước đó 5 phút trở xuống so với sự kiện máy chủ. Khử trùng lặp qua cookie sẽ không bao giờ loại bỏ sự kiện gửi từ pixel trình duyệt.
- Khử trùng lặp qua cookie chỉ loại bỏ sự kiện Events API khi `event_id` không được thiết lập trong payload Events API. Do đó, nếu muốn tận dụng cơ chế này, bạn không nên gửi `event_id` trong payload Events API.

# Xác minh thiết lập khử trùng lặp của bạn (Verify your deduplication setup)
Để kiểm tra xem thiết lập khử trùng lặp có hoạt động chính xác hay không và xem số lượng sự kiện đã được khử trùng lặp, hãy truy cập vào trang chi tiết Pixel của bạn:
- Chỉ số "**Browser**" hiển thị các sự kiện riêng biệt chỉ nhận được từ Pixel SDK.
- Chỉ số "**Server**" hiển thị các sự kiện riêng biệt chỉ nhận được từ Events API.
- Chỉ số "**Server & Browser**" hiển thị số lượng sự kiện được gửi từ cả Events API và Pixel SDK (cùng một sự kiện gửi qua hai kênh sẽ được tính là 1 sự kiện). Nếu số liệu Server & Browser (tổng sự kiện và sự kiện được phân bổ) quá thấp, hãy kiểm tra lại việc triển khai khử trùng lặp và đảm bảo giá trị `event_id` trùng khớp hoàn toàn giữa Pixel SDK và Events API.
- Nhấp vào "**View details**" (Xem chi tiết) dưới cột **Event Health** (Tình trạng sự kiện) cho bất kỳ loại sự kiện nào có Phương thức kết nối "Server & Browser" để mở trang Event Health hiển thị chi tiết về tình trạng khớp và khử trùng lặp.

---

<a id="doc-1771100984456193"></a>
<!-- doc_id: 1771100984456193 -->
<!-- doc_id: 1771100984456193 -->
# Xác minh thiết lập Events API
> Đường dẫn: Marketing API > Đo lường quảng cáo (Ad Measurement) > Hướng dẫn (Guides) > Events API 2.0 > Events API cho Web > Xác minh thiết lập Events API
Bài viết này hướng dẫn cách xác minh thiết lập kết nối dữ liệu web. Quy trình bao gồm:
- Xác minh sự kiện được tiếp nhận chính xác.
- Xác minh sự kiện được cấu hình và kích hoạt chính xác.
- Xác minh sự kiện được khử trùng lặp chính xác (nếu gửi sự kiện từ cả Pixel SDK và Events API).

# Xác minh việc tiếp nhận sự kiện thành công
Bạn có thể kiểm tra xem TikTok đã nhận được sự kiện của bạn hay chưa trên trang chi tiết Pixel. Nhấp vào trang chi tiết Pixel và tại tab **Overview** (Tổng quan):
1. Nếu chúng tôi đã nhận được sự kiện gửi từ Events API, bạn sẽ thấy "**Server**" trong cột **Connection Method** (Phương thức kết nối). Vui lòng làm mới trang để cập nhật trạng thái mới nhất.
2. Nếu bạn gửi sự kiện từ cả Events API và Pixel SDK, bạn sẽ thấy "**Server & Browser**".

# Xác minh sự kiện được cấu hình và kích hoạt chính xác qua Sự kiện thử nghiệm (Test Events)
Sau khi thiết lập Pixel và sẵn sàng gửi sự kiện, bạn có thể gửi một sự kiện thử nghiệm để kiểm tra xem mọi thứ có hoạt động ổn định hay không. Đảm bảo xóa bỏ trường `test_event_code` trước khi chuyển sang chế độ chính thức ('Production').

## Các bước thực hiện
1. Trong Events Manager, nhấp vào Pixel để xem chi tiết cấu hình.
2. Trong tab **Test Events** (Sự kiện thử nghiệm), nhấp vào nút sao chép mã thử nghiệm ở **Bước 2** trong phần **Test Server Events** (Thử nghiệm sự kiện máy chủ).
3. Trong phần thân (body) của yêu cầu API báo cáo sự kiện, thêm trường mới `test_event_code` và dán mã bạn lấy từ Bước 2 làm giá trị của trường đó. Gửi yêu cầu API. Dưới đây là ví dụ yêu cầu thử nghiệm. Bạn cần thay thế các giá trị `Access-Token`, `event_source_id` và `test_event_code` bằng giá trị thực tế của bạn:

```
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/event/track/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "event_source": "web",
  "event_source_id": "{{Pixel-Code}}",
  "test_event_code": "{{YOUR_TEST_CODE}}",
  "data": [
    {
      "event": "Purchase",
      "event_time": 1684574395,
      "event_id":"1616318632825_357"
      "user": {
        "email": ["848a771458438fc2ec420560d769fb9b9b86851ee338ec56517baabd79d3bb4f",
        "dd6ff77f54e2106661089bae4d40cdb600979bf7edc9eb65c0942ba55c7c2d7f"],
        "phone": ["2f9d2b4df907e5c9a7b3434351b55700167b998a83dc479b825096486ffcf4ea"],
        "ttp":"94e2a4j9-h3j5-k2h5-98cc-c84a745mk098",
        "ttclid": "E.C.P.v3fQ2RHacdksKfofPmlyuStIIHJ4Af1tKYxF9zz2c2PLx1Oaw15oHpcfl5AH",
        "ip": "139.177.225.245",
        "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.1 Safari/605.1.15"
      },
      "page": {
        "url": "http://www.example.com/purchase?q=hello",
        "referrer": "http://demo.mywebsite.com"
      },
      "properties": {
        "contents": [
          {
            "price": 8,
            "quantity": 2,
            "content_id": "1077218",
            "content_name": "running shoes",
            "content_category": "Shoes > Sneakers > running shoes",
            "brand": "your_brand_name"
          },
          {
            "price": 30,
            "quantity": 1,
            "content_id": "1197218",
            "content_name": "running shoes",
            "content_category": "Shoes > Sneakers > running shoes",
            "brand": "your_brand_name"
          }
        ],
        "content_type": "product",
        "currency": "USD",
        "value": 46.00
      }
    }
  ]
}'
```
4. Truy cập tab **Test Events** của Pixel trong **Events Manager**, và tìm sự kiện thử nghiệm trong phần **Event Activity** (Hoạt động sự kiện). Bất kỳ lỗi nào liên quan đến payload sẽ hiển thị tại đây để giúp bạn khắc phục.

# Xác minh sự kiện được khử trùng lặp chính xác
Để có hiệu suất quảng cáo tối ưu, chúng tôi khuyến nghị nhà quảng cáo thiết lập cả TikTok Pixel SDK và Events API để đạt mức độ bao phủ dữ liệu tối đa. Trong trường hợp này, bạn cần thiết lập cơ chế khử trùng lặp để loại trừ các bản ghi trùng lặp, đảm bảo không bị tính trùng lặp sự kiện trong việc đo lường và báo cáo. Xem chi tiết tại [Khử trùng lặp sự kiện](do-luong-quang-cao-p1.md#doc-1771100965992450).

---

<a id="doc-1807346079965186"></a>
<!-- doc_id: 1807346079965186 -->
<!-- doc_id: 1807346079965186 -->
# Sử dụng Payload Helper cho Web
> Đường dẫn: Marketing API > Đo lường quảng cáo (Ad Measurement) > Hướng dẫn (Guides) > Events API 2.0 > Events API cho Web > Sử dụng Payload Helper cho Web
Bài viết này hướng dẫn các bước sử dụng công cụ Payload Helper cho Web để xây dựng dữ liệu tải trọng (payload) báo cáo Sự kiện Web qua Events API 2.0.

## Giới thiệu
Payload Helper cho Web là giao diện người dùng trực quan do TikTok API for Business cung cấp nhằm đơn giản hóa quy trình tạo payload cho Events API 2.0 Web. Công cụ này đảm bảo rằng tất cả các trường bắt buộc đều được đưa vào trước khi gửi dữ liệu đến TikTok, đồng thời hỗ trợ sinh mã mẫu theo các định dạng cURL, Python và Node.js.

## Điều kiện tiên quyết
Trước khi sử dụng Payload Helper cho Web, bạn nên đọc kỹ [Hướng dẫn thiết lập cho Web](do-luong-quang-cao-tom-tat.md#doc-1771100865818625) để nắm rõ các tham số hỗ trợ khi báo cáo sự kiện web qua Events API 2.0.

## Các bước thực hiện

### Truy cập Payload Helper
Truy cập trực tiếp [Payload Helper](do-luong-quang-cao-p1.md#doc-1797165504155649). Công cụ chỉ mất vài giây để tải và không yêu cầu đăng nhập.

### Sử dụng Payload Helper
Theo mặc định, `event_source` được đặt thành `web` và các trường khác để trống. Bạn cần điền các trường bắt buộc còn lại để tạo một payload hoàn chỉnh và hiệu quả.

#### 1. Nhập dữ liệu sự kiện (event data)
Điền ba trường dữ liệu sự kiện bắt buộc sau:
  - `event_source_id`: Nhập mã Pixel Code của bạn.
    - Để lấy Pixel Code, xem phần [Câu hỏi thường gặp - Tôi có thể tìm Pixel Code ở đâu](do-luong-quang-cao-p1.md#doc-1771101001228290).
  - `event`: Chọn tên Sự kiện chuẩn từ menu thả xuống đối với Sự kiện chuẩn, hoặc nhập tên tùy chỉnh đối với Sự kiện tùy chỉnh.
  - `event_time`: Nhập thời gian diễn ra sự kiện theo chuẩn UTC+0 dưới dạng Unix timestamp tính bằng giây. Ví dụ: `1723455457`.
  
Tùy chọn: mở rộng các trường dữ liệu sự kiện bằng cách bổ sung `event_id` và `limited_data_use` tùy theo nhu cầu.

#### 2. Thêm dữ liệu người dùng (user data)
Nhập ít nhất một trong các trường sau: `email`, `phone` và `external_id`. Nhấp vào nút **Hash** trên giao diện để tự động băm SHA-256 nhằm bảo vệ quyền riêng tư người dùng. Ví dụ: bạn có thể băm SHA-256 địa chỉ email `example_user@example.com` thành `c6239ca1f8fe9b3d73e1352629e55c3ff0c587c8897903463247fe6ce6ef747d`.

Tùy chọn: mở rộng các trường người dùng bằng cách bổ sung `ttclid`, `ttp`, `ip` và `user_agent`.

#### 3. *(Không bắt buộc)* Thêm dữ liệu thuộc tính (property data)
Chọn giá trị cho `currency` và `content_type` từ menu thả xuống.

Tùy chọn: mở rộng các trường thuộc tính bằng cách thêm `contents`, `value`, `query` và `description`.

Lưu ý: Nếu chỉ định `content_type`, chúng tôi khuyến nghị bạn truyền đồng thời `content_id` bên trong `contents` theo quy tắc sau:
  - Nếu `content_type` là `product`, hãy truyền `content_id` là mã SKU (`sku_id`) trong danh mục sản phẩm của bạn.
  - Nếu `content_type` là `product_group`, hãy truyền `content_id` là mã nhóm sản phẩm SPU (`item_group_id`) trong danh mục sản phẩm của bạn.

#### 4. Thêm dữ liệu trang web (page data)
Đặt `url` thành URL trình duyệt đầy đủ nơi sự kiện diễn ra.

Tùy chọn: mở rộng các trường trang web bằng cách thêm `referrer`.

#### 5. Tạo mã mẫu
Sau khi đã điền đầy đủ các thông tin cần thiết, bạn sẽ thấy đối tượng JSON được tự động tạo. Bạn có thể tạo mã nguồn mẫu dưới dạng lệnh cURL, Python hoặc Node.js bằng cách nhấp vào **Generate Code**.

Thay thế giá trị giữ chỗ `{{Access-Token}}` bằng mã truy cập thực tế của bạn trong đoạn mã mẫu để chạy thử nghiệm.

---

<a id="doc-1771101001228290"></a>
<!-- doc_id: 1771101001228290 -->
<!-- doc_id: 1771101001228290 -->
# Câu hỏi thường gặp - Web (FAQs)
> Đường dẫn: Marketing API > Đo lường quảng cáo (Ad Measurement) > Hướng dẫn (Guides) > Events API 2.0 > Events API cho Web > Câu hỏi thường gặp (FAQs)
## Q1: Tôi nhận được mã phản hồi 40001 thay vì 0. Tôi phải làm gì?

A1: Hãy đảm bảo bạn có vai trò Quản trị viên (Admin) hoặc Nhà điều hành (Operator) thuộc tài khoản quảng cáo này. Để tìm hiểu thêm về các mã phản hồi khác nhau, tham khảo [Phản hồi và mã lỗi - Mã phản hồi API](do-luong-quang-cao-p1.md#doc-1771101162079234).

## Q2: Tôi có thể tìm Pixel Code ở đâu?

A2: 
- (1) Nếu bạn đã có Pixel, bạn có thể tìm Pixel Code bằng cách đăng nhập vào tài khoản [TikTok Ads Manager](https://ads.tiktok.com/i18n/home) và điều hướng đến **Công cụ (Tools)** > **Sự kiện (Events)** > **Nguồn dữ liệu (Data sources)**. Giá trị Pixel Code sẽ có định dạng chuỗi ký tự (ví dụ: `CUSG5HBC77UD11VVRQEG`).

Nếu chúng tôi đã nhận được các sự kiện bạn gửi từ Events API, bạn sẽ thấy giá trị "Server" trong cột Phương thức kết nối (Connection Method) tại tab "Overview". Vui lòng làm mới trang để xem trạng thái mới nhất. Điều này có nghĩa là các sự kiện chuyển tiếp đến TikTok sẽ hiển thị dưới Pixel đó. Lưu ý: nếu bạn gửi các sự kiện trùng lặp từ cả Pixel SDK và Events API, bạn bắt buộc phải thiết lập khử trùng lặp sự kiện. Nếu bạn gửi sự kiện từ cả TikTok Pixel và Events API đến cùng một Pixel Code để [khử trùng lặp sự kiện](do-luong-quang-cao-p1.md#doc-1771100965992450), hãy chắc chắn bật tính năng Khớp nâng cao tự động (Automatic Advanced Matching).

- (2) Nếu bạn chưa có Pixel hoặc muốn tạo Pixel mới từ đầu, hãy truy cập **Công cụ (Tools)** > **Sự kiện (Events)** > **Kết nối nguồn dữ liệu (Connect data source)** > **Web**, và làm theo các bước hướng dẫn để tạo Pixel.

---

<a id="doc-1771100815832065"></a>
<!-- doc_id: 1771100815832065 -->
<!-- doc_id: 1771100815832065 -->
# Events API cho Ngoại tuyến (Events API for Offline)
> Đường dẫn: Marketing API > Đo lường quảng cáo (Ad Measurement) > Hướng dẫn (Guides) > Events API 2.0 > Events API cho Ngoại tuyến
> **Quan trọng:** 
> Bằng việc sử dụng các endpoint Events API, bạn đồng ý với [Điều khoản sản phẩm thương mại của TikTok (Dữ liệu)](https://ads.tiktok.com/i18n/official/policy/business-products-terms) và cam kết không chia sẻ dữ liệu nhạy cảm với TikTok.

> **Lưu ý:** 
> Events API 2.0 ([/event/track/](../12-api-reference/42-events-2-0.md#doc-1771101303285761)) hiện là endpoint được khuyến nghị để báo cáo sự kiện từ tất cả các nguồn, bao gồm web, app, offline và hệ thống CRM. Endpoint này cung cấp một cấu trúc schema API hợp nhất giúp đơn giản hóa việc tích hợp.
> Để đảm bảo quá trình chuyển đổi suôn sẻ, sáu endpoint Events API 1.0 đã bắt đầu ngừng hoạt động từ H2 2024: • [/pixel/track/](../12-api-reference/43-events-1-0-p1.md#doc-1740858531237890) và [/pixel/batch/](../12-api-reference/43-events-1-0-p1.md#doc-1740858565852225) • [/offline/track/](../12-api-reference/43-events-1-0-p1.md#doc-1758428013689857) và [/offline/batch/](../12-api-reference/43-events-1-0-p1.md#doc-1758428053652482) • [/app/track/](../12-api-reference/43-events-1-0-p1.md#doc-1740859196043266) và [/app/batch/](../12-api-reference/43-events-1-0-p1.md#doc-1740859218541569)
> Chúng tôi đặc biệt khuyến nghị người dùng mới tích hợp trực tiếp với endpoint Events API 2.0, và người dùng Events API 1.0 bắt đầu nâng cấp sớm nhất có thể.

Phần này giới thiệu cách quản lý Sự kiện Ngoại tuyến (Offline Events) qua Events API 2.0:
- [Hướng dẫn thiết lập cho Ngoại tuyến](do-luong-quang-cao-tom-tat.md#doc-1771101027431425)
- [Xác minh thiết lập Offline Events API](do-luong-quang-cao-p1.md#doc-1771101049613313)
- [Câu hỏi thường gặp (FAQs)](do-luong-quang-cao-p1.md#doc-1771101064635394)

---

<a id="doc-1771101049613313"></a>
<!-- doc_id: 1771101049613313 -->
<!-- doc_id: 1771101049613313 -->
# Xác minh thiết lập Offline Events API
> Đường dẫn: Marketing API > Đo lường quảng cáo (Ad Measurement) > Hướng dẫn (Guides) > Events API 2.0 > Events API cho Ngoại tuyến > Xác minh thiết lập Offline Events API
## Xác minh sự kiện được tiếp nhận chính xác
Điều hướng tới **Công cụ (Tools)** > **Sự kiện (Events)** > nút **Nguồn dữ liệu (Data sources)**. Bạn sẽ được chuyển tới trang chi tiết của Bộ sự kiện ngoại tuyến (Offline Event Set).

Tại tab **Overview** (Tổng quan), bạn có thể kiểm tra xem hệ thống đã nhận được sự kiện chưa. Hãy làm mới trang để cập nhật trạng thái mới nhất:
- Nếu chúng tôi đã nhận được sự kiện gửi qua Events API, bạn sẽ thấy "**Server**" trong cột **Connection Method**.
- Nếu sự kiện được tải lên trực tiếp từ trình duyệt qua tệp dữ liệu, bạn sẽ thấy "**Browser**" trong cột **Connection Method**.

## Sự kiện thử nghiệm (Test Events)
Sau khi thiết lập Bộ sự kiện ngoại tuyến và sẵn sàng gửi sự kiện, bạn có thể gửi một sự kiện thử nghiệm để đảm bảo toàn bộ hệ thống hoạt động chính xác. **Trước khi chuyển sang chế độ chính thức ('Production'), hãy chắc chắn xóa trường `test_event_code`.**

### Các bước thực hiện
Làm theo các bước sau để gửi sự kiện thử nghiệm:
1. Trong Events Manager, nhấp vào Bộ sự kiện ngoại tuyến để xem chi tiết cấu hình.
2. Trong tab **Test Events**, nhấp vào nút sao chép mã thử nghiệm ở **Bước 2** trong phần **Test Server Events**. Mã sẽ được sao chép vào bộ nhớ tạm.
3. Trong phần thân (body) của yêu cầu API báo cáo sự kiện, thêm trường mới `test_event_code` và dán mã thử nghiệm từ Bước 2. Sau đó gửi yêu cầu API. Dưới đây là ví dụ yêu cầu thử nghiệm. Bạn cần thay thế các giá trị `Access-Token`, `event_source_id` và `test_event_code` bằng giá trị thực tế của mình:

```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/event/track/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "event_source": "offline",
  "event_source_id": "{{Offline-Event-Set-ID}}",
  "test_event_code": "{{YOUR_TEST_CODE}}",
  "data": [
    {
      "event_id":"1616318632825_357",
      "event": "Purchase",
      "event_time": 1684574395,
      "user": {
        "email": ["848a771458438fc2ec420560d769fb9b9b86851ee338ec56517baabd79d3bb4f",
        "dd6ff77f54e2106661089bae4d40cdb600979bf7edc9eb65c0942ba55c7c2d7f"],
        "phone": ["2f9d2b4df907e5c9a7b3434351b55700167b998a83dc479b825096486ffcf4ea"]
       },
      "properties": {
        "order_id": "abc_xyz",
        "shop_id": "123abc",
        "contents": [
          {
            "price": 8,
            "quantity": 2,
            "content_id": "1077218",
            "content_name": "running shoes",
            "content_category": "Shoes > Sneakers > running shoes",
            "brand": "your_brand_name"
          },
          {
            "price": 30,
            "quantity": 1,
            "content_id": "1197218",
            "content_name": "running shoes",
            "content_category": "Shoes > Sneakers > running shoes",
            "brand": "your_brand_name"
          }
        ],
        "content_type": "product",
        "currency": "USD",
        "value": 46.00
      }
    }
  ]
}'
```

4. Đi đến tab **Test Events** và kiểm tra sự kiện thử nghiệm trong phần **Event Activity** (Hoạt động sự kiện). Mọi lỗi về cấu trúc payload sẽ được hiển thị để giúp bạn nhanh chóng khắc phục.

---

<a id="doc-1771101064635394"></a>
<!-- doc_id: 1771101064635394 -->
<!-- doc_id: 1771101064635394 -->
# Câu hỏi thường gặp - Ngoại tuyến (FAQs)
> Đường dẫn: Marketing API > Đo lường quảng cáo (Ad Measurement) > Hướng dẫn (Guides) > Events API 2.0 > Events API cho Ngoại tuyến > Câu hỏi thường gặp (FAQs)
## Q1: Có giới hạn tần suất (rate limit) nào cần lưu ý không?

A1: Để tìm hiểu về giới hạn tần suất của Events API 2.0, tham khảo [Events API 2.0 - Giới hạn API](do-luong-quang-cao-p1.md#doc-1771100779668482).

## Q2: Số lượng sự kiện tối đa có thể gửi trong một lô (batch) là bao nhiêu?

A2: Chúng tôi khuyến nghị gửi dưới **100 sự kiện trên mỗi lô**, với tổng kích thước lô nhỏ hơn **10 MB**.

## Q3: Nếu tôi tải lên các sự kiện ngoại tuyến diễn ra từ 90 ngày trước, TikTok có đối chiếu chúng với quảng cáo và hiển thị trong báo cáo không?

A3: Không, TikTok sẽ không đối chiếu và báo cáo cho các sự kiện ngoại tuyến diễn ra từ 90 ngày trước. Đối với sự kiện ngoại tuyến, bạn có 28 ngày để tải lên dữ liệu Bộ sự kiện ngoại tuyến. Cửa sổ phân bổ tối đa cho phân bổ lượt nhấp (CTA - click-through attribution) là 28 ngày, trong khi cửa sổ phân bổ tối đa cho phân bổ lượt xem (VTA - view-through attribution) là 7 ngày. Điều này có nghĩa là các sự kiện ngoại tuyến nằm ngoài các cửa sổ phân bổ này sẽ không được liên kết với quảng cáo hoặc hiển thị trong báo cáo.

---

<a id="doc-1771100838106114"></a>
<!-- doc_id: 1771100838106114 -->
<!-- doc_id: 1771100838106114 -->
# Events API cho Ứng dụng (Events API for App)
> Đường dẫn: Marketing API > Đo lường quảng cáo (Ad Measurement) > Hướng dẫn (Guides) > Events API 2.0 > Events API cho Ứng dụng
> **Quan trọng:** 
> Bằng việc sử dụng các endpoint Events API, bạn đồng ý với [Điều khoản sản phẩm thương mại của TikTok (Dữ liệu)](https://ads.tiktok.com/i18n/official/policy/business-products-terms) và cam kết không chia sẻ dữ liệu nhạy cảm với TikTok.

> **Lưu ý:** 
> Events API 2.0 ([/event/track/](../12-api-reference/42-events-2-0.md#doc-1771101303285761)) hiện là endpoint được khuyến nghị để báo cáo sự kiện từ tất cả các nguồn, bao gồm web, ứng dụng (app), ngoại tuyến (offline) và hệ thống CRM (quản lý quan hệ khách hàng). Endpoint này cung cấp một cấu trúc schema API hợp nhất giúp đơn giản hóa và tối ưu quy trình tích hợp.
> Để đảm bảo quá trình chuyển đổi suôn sẻ, sáu endpoint Events API 1.0 sau đây đã bắt đầu ngừng hoạt động từ H2 2024: • [/pixel/track/](../12-api-reference/43-events-1-0-p1.md#doc-1740858531237890) và [/pixel/batch/](../12-api-reference/43-events-1-0-p1.md#doc-1740858565852225) • [/offline/track/](../12-api-reference/43-events-1-0-p1.md#doc-1758428013689857) và [/offline/batch/](../12-api-reference/43-events-1-0-p1.md#doc-1758428053652482) • [/app/track/](../12-api-reference/43-events-1-0-p1.md#doc-1740859196043266) và [/app/batch/](../12-api-reference/43-events-1-0-p1.md#doc-1740859218541569)
> Chúng tôi đặc biệt khuyến nghị người dùng mới tích hợp trực tiếp với Events API 2.0, và người dùng Events API 1.0 nâng cấp sớm nhất có thể.

Phần này giới thiệu cách quản lý Sự kiện Ứng dụng (App Events) qua Events API 2.0:
- [Hướng dẫn thiết lập cho Ứng dụng](do-luong-quang-cao-tom-tat.md#doc-1771101111730178)

---

<a id="doc-1819583269559297"></a>
<!-- doc_id: 1819583269559297 -->
<!-- doc_id: 1819583269559297 -->
# Xác minh thiết lập Events API cho App
> Đường dẫn: Marketing API > Đo lường quảng cáo (Ad Measurement) > Hướng dẫn (Guides) > Events API 2.0 > Events API cho Ứng dụng > Xác minh thiết lập Events API
Bài viết này hướng dẫn cách xác minh thiết lập kết nối dữ liệu ứng dụng di động. Quy trình bao gồm:
- Xác minh sự kiện được tiếp nhận chính xác.
- Xác minh sự kiện được cấu hình và kích hoạt chính xác.

# Xác minh sự kiện được tiếp nhận chính xác
Bạn có thể kiểm tra xem hệ thống đã nhận được sự kiện chưa trên trang chi tiết ứng dụng. Truy cập trang chi tiết ứng dụng và tại tab **Overview** (Tổng quan), cuộn xuống phần **Reporting** (Báo cáo):

1. Đảm bảo **TikTok App Events API** được chọn tại mục **Data Source** (Nguồn dữ liệu).
2. Kiểm tra số lượng **Total Events** (Tổng số sự kiện). Lưu ý rằng số liệu này có thể có độ trễ cập nhật nhỏ.

# Xác minh sự kiện được cấu hình và kích hoạt chính xác qua Sự kiện thử nghiệm (Test Events)
Sau khi thiết lập ứng dụng và sẵn sàng báo cáo sự kiện, bạn có thể gửi một sự kiện thử nghiệm để kiểm tra tính chính xác. **Hãy chắc chắn xóa bỏ trường `test_event_code` trước khi chuyển sang môi trường thực tế ('Production').**

## Các bước thực hiện
1. Trong Events Manager, nhấp vào ứng dụng để xem chi tiết cấu hình.
2. Trong tab **Test Events**, nhấp vào nút sao chép mã thử nghiệm ở **Bước 2** để lưu mã vào bộ nhớ tạm.
3. Trong phần thân (body) của yêu cầu API báo cáo sự kiện, thêm trường `test_event_code` và dán mã thử nghiệm từ Bước 2. Gửi yêu cầu API. Dưới đây là ví dụ yêu cầu thử nghiệm. Bạn cần thay thế các giá trị `Access-Token`, `event_source_id` và `test_event_code` bằng giá trị thực tế của mình:

```
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/event/track/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "event_source": "app",
  "event_source_id": "{{TIKTOK_APP_ID}",
  "test_event_code": "{{YOUR_TEST_CODE}}",
  "data": [
    {
      "event": "InstallApp",
      "event_time": 1684574395,
      "user": {
        "phone": "{{HASHED_PHONE}}",
        "email": "{{HASHED_EMAIL}}",
        "idfa": "{{IDFA}}",
        "idfv": "{{IDFV}}",
        "gaid": "{{GAID}}",
        "att_status": "AUTHORIZED"
        "locale": "en-US"
      },
      "app": {
        "app_id": "com.test.flyingsneakers"
        "app_name": "Flying Sneakers"
        "app_version": "3.0.2"
      },
	  "ad": {
        "attributed": true,
        "callback": "{{CALLBACK}}",
        "campaign_id": "1700817380525057",
        "ad_id": "1700817380806706",
        "creative_id": "1700817378256945"
        "is_retargeting": false,
        "attribution_type": "click_through"
      },
      "properties": {
        "contents": [
          {
            "currency": "USD",
            "value": 200.0
			"content_type": "product",
          {
            "price": 100.0,
            "quantity": 2,
            "content_id": "12345",
            "content_name": "Fancy-AirMax2.0 Black",
            "content_category": "Shoes - running shoes",
            "brand": "Fancy Sneakers"
          }
        ]
      }
    }
  ]
}'
```

4. Truy cập tab **Test Events** của ứng dụng trong **Events Manager**, và kiểm tra sự kiện thử nghiệm trong phần **Event Activity**. Bất kỳ lỗi cấu trúc payload nào cũng sẽ được hiển thị để bạn xử lý.

---

<a id="doc-1819581869993025"></a>
<!-- doc_id: 1819581869993025 -->
<!-- doc_id: 1819581869993025 -->
# Sử dụng Payload Helper cho App
> Đường dẫn: Marketing API > Đo lường quảng cáo (Ad Measurement) > Hướng dẫn (Guides) > Events API 2.0 > Events API cho Ứng dụng > Sử dụng Payload Helper cho App
Bài viết này hướng dẫn các bước sử dụng công cụ Payload Helper cho App để xây dựng dữ liệu tải trọng (payload) báo cáo Sự kiện Ứng dụng qua Events API 2.0.

## Giới thiệu
Payload Helper cho App là giao diện người dùng trực quan do TikTok API for Business cung cấp nhằm đơn giản hóa quy trình tạo payload cho Events API 2.0 đối với nguồn Ứng dụng. Công cụ này đảm bảo tất cả các trường dữ liệu cần thiết được khai báo trước khi gửi đến TikTok, hỗ trợ xuất mã mẫu dạng cURL, Python và Node.js.

## Điều kiện tiên quyết
Trước khi sử dụng Payload Helper cho App, hãy tìm hiểu [Hướng dẫn thiết lập cho Ứng dụng](do-luong-quang-cao-tom-tat.md#doc-1771101111730178) để nắm rõ danh sách tham số được hỗ trợ khi báo cáo sự kiện qua Events API 2.0.

## Các bước thực hiện

### Truy cập Payload Helper
Truy cập trực tiếp [Payload Helper](do-luong-quang-cao-p1.md#doc-1797165504155649). Giao diện tải trong vài giây và không yêu cầu đăng nhập.

### Sử dụng Payload Helper
Theo mặc định, `event_source` được chọn là `app` và các trường khác để trống. Bạn cần điền các trường bắt buộc sau:

#### 1. Nhập dữ liệu sự kiện (event data)
Điền ba trường dữ liệu sự kiện bắt buộc:
  - `event_source_id`: Nhập TikTok App ID của bạn.
    - Để lấy TikTok App ID, tham khảo [Hướng dẫn thiết lập cho Ứng dụng - Lấy TikTok App ID](do-luong-quang-cao-tom-tat.md#doc-1771101111730178).
  - `event`: Chọn tên Sự kiện chuẩn từ menu thả xuống đối với Sự kiện chuẩn, hoặc nhập tên tùy chỉnh cho Sự kiện tùy chỉnh.
  - `event_time`: Nhập thời gian diễn ra sự kiện theo chuẩn UTC+0 dưới dạng Unix timestamp tính bằng giây. Ví dụ: `1723455457`.
  
Tùy chọn: mở rộng các trường sự kiện bằng cách bổ sung `event_id` và `limited_data_use` tùy nhu cầu.

#### 2. Thêm tham số ứng dụng (app parameters)
**App ID** của bạn sẽ có định dạng reverse DNS (đối với Android) hoặc chuỗi số ngắn (đối với iOS) thường thấy trong URL của Google Play Store hoặc Apple App Store.

#### 3. Thêm tham số người dùng (user parameters)
Nhập ít nhất một trong các trường định danh thiết bị: `idfa`, `gaid`.

Tùy chọn: bạn cũng có thể nhập các tham số người dùng tùy chọn khác bao gồm `email`, `phone` và `external_id`. Nhấp vào nút **Hash** trên giao diện để tự động băm SHA-256 bảo vệ dữ liệu riêng tư. Ví dụ: băm địa chỉ email `example_user@example.com` thành `c6239ca1f8fe9b3d73e1352629e55c3ff0c587c8897903463247fe6ce6ef747d`.

Các trường bổ sung bao gồm `ip`, `user_agent` và `att_status` khả dụng tùy theo nhu cầu của bạn.

#### 4. *(Không bắt buộc)* Thêm dữ liệu thuộc tính (property data)
Chọn tùy chọn cho `currency` và `content_type` từ menu thả xuống.

Tùy chọn: mở rộng các trường thuộc tính với `contents`, `value`, `query` và `description`.

Lưu ý: Nếu khai báo `content_type`, chúng tôi khuyến nghị truyền đồng thời `content_id` trong `contents` theo quy tắc:
  - Nếu `content_type` là `product`, hãy đặt `content_id` là mã SKU (`sku_id`) trong danh mục.
  - If `content_type` is set to `product_group`, specify `content_id` as a product SPU ID (`item_group_id`) within your catalog.
 
#### 5. Tạo mã mẫu
Sau khi hoàn tất nhập thông tin, đối tượng JSON sẽ được sinh tự động. Bạn có thể xuất mã mẫu dưới dạng lệnh cURL, Python hoặc Node.js bằng cách nhấp vào **Generate Code**.

Thay thế chuỗi giữ chỗ bằng access token thực tế của bạn để gửi thử nghiệm.

---

<a id="doc-1835052243486786"></a>
<!-- doc_id: 1835052243486786 -->
<!-- doc_id: 1835052243486786 -->
# Events API cho CRM (Events API for CRM)
> Đường dẫn: Marketing API > Đo lường quảng cáo (Ad Measurement) > Hướng dẫn (Guides) > Events API 2.0 > Events API cho CRM
> **Quan trọng:** 
> Bằng việc sử dụng các endpoint Events API, bạn đồng ý với [Điều khoản sản phẩm thương mại của TikTok (Dữ liệu)](https://ads.tiktok.com/i18n/official/policy/business-products-terms) và cam kết không chia sẻ dữ liệu nhạy cảm với TikTok.

> **Lưu ý:** 
> Events API 2.0 ([/event/track/](../12-api-reference/42-events-2-0.md#doc-1771101303285761)) hiện là endpoint được khuyến nghị để báo cáo sự kiện từ tất cả các nguồn, bao gồm web, ứng dụng (app), ngoại tuyến (offline) và hệ thống CRM (quản lý quan hệ khách hàng). Endpoint này cung cấp một schema API hợp nhất giúp đơn giản hóa và tối ưu quy trình tích hợp.
> Để đảm bảo quá trình chuyển đổi suôn sẻ, sáu endpoint Events API 1.0 đã bắt đầu ngừng hoạt động từ H2 2024: • [/pixel/track/](../12-api-reference/43-events-1-0-p1.md#doc-1740858531237890) và [/pixel/batch/](../12-api-reference/43-events-1-0-p1.md#doc-1740858565852225) • [/offline/track/](../12-api-reference/43-events-1-0-p1.md#doc-1758428013689857) và [/offline/batch/](../12-api-reference/43-events-1-0-p1.md#doc-1758428053652482) • [/app/track/](../12-api-reference/43-events-1-0-p1.md#doc-1740859196043266) và [/app/batch/](../12-api-reference/43-events-1-0-p1.md#doc-1740859218541569)
> Chúng tôi đặc biệt khuyến nghị người dùng mới tích hợp trực tiếp với Events API 2.0 và người dùng Events API 1.0 nâng cấp sớm nhất có thể.

Phần này giới thiệu cách quản lý Sự kiện CRM qua Events API 2.0:
- [Hướng dẫn thiết lập cho CRM](do-luong-quang-cao-tom-tat.md#doc-1835052338764993)
- [Xác minh thiết lập Events API cho CRM](do-luong-quang-cao-p1.md#doc-1835052369704961)
- [Câu hỏi thường gặp (FAQs)](do-luong-quang-cao-p1.md#doc-1835052398174274)

---

<a id="doc-1835052369704961"></a>
<!-- doc_id: 1835052369704961 -->
<!-- doc_id: 1835052369704961 -->
# Xác minh thiết lập Events API cho CRM
> Đường dẫn: Marketing API > Đo lường quảng cáo (Ad Measurement) > Hướng dẫn (Guides) > Events API 2.0 > Events API cho CRM > Xác minh thiết lập Events API
# Xác minh sự kiện được tiếp nhận chính xác
Điều hướng tới **Công cụ (Tools)** > **Sự kiện (Events)** > **Nguồn dữ liệu (Data sources)**. Bạn sẽ vào trang chi tiết của Bộ sự kiện CRM (CRM Event Set).

Tại tab **Overview** (Tổng quan), bạn có thể kiểm tra xem hệ thống đã nhận được sự kiện chưa. Hãy làm mới trang để cập nhật trạng thái mới nhất:
- Nếu chúng tôi đã nhận được sự kiện gửi từ Events API, bạn sẽ thấy "**Server**" trong cột **Connection Method**.
- Nếu sự kiện được tải lên trực tiếp từ trình duyệt qua tệp dữ liệu, bạn sẽ thấy "**Browser**" trong cột **Connection Method**.

---

<a id="doc-1835052398174274"></a>
<!-- doc_id: 1835052398174274 -->
<!-- doc_id: 1835052398174274 -->
# Câu hỏi thường gặp - CRM (FAQs)
> Đường dẫn: Marketing API > Đo lường quảng cáo (Ad Measurement) > Hướng dẫn (Guides) > Events API 2.0 > Events API cho CRM > Câu hỏi thường gặp (FAQs)
## Q1: Có giới hạn tần suất (rate limit) nào cần lưu ý không?

A1: Để tìm hiểu về giới hạn tần suất của Events API 2.0, xem [Events API 2.0 - Giới hạn API](do-luong-quang-cao-p1.md#doc-1771100779668482).

## Q2: Số lượng sự kiện tối đa có thể gửi trong một lô (batch) là bao nhiêu?

A2: Chúng tôi khuyến nghị gửi dưới **100 sự kiện trên mỗi lô**, với tổng kích thước gói tin nhỏ hơn **10 MB**.  

## Q3: Nếu tôi tải lên các sự kiện CRM diễn ra từ 90 ngày trước, TikTok có đối chiếu chúng với quảng cáo và hiển thị trong báo cáo không?

A3: Không, TikTok sẽ không đối chiếu và báo cáo cho các sự kiện CRM đã diễn ra từ 90 ngày trước. Đối với sự kiện CRM, cửa sổ phân bổ mặc định cho phân bổ lượt nhấp (CTA) là 7 ngày, trong khi cửa sổ phân bổ mặc định cho phân bổ lượt xem (VTA) là 1 ngày. Điều này có nghĩa là các sự kiện CRM nằm ngoài các cửa sổ phân bổ này sẽ không được đối chiếu với quảng cáo hoặc hiển thị trong báo cáo.

---

<a id="doc-1771101130925058"></a>
<!-- doc_id: 1771101130925058 -->
<!-- doc_id: 1771101130925058 -->
# Xác thực (Authentication)
> Đường dẫn: Marketing API > Đo lường quảng cáo (Ad Measurement) > Hướng dẫn (Guides) > Events API 2.0 > Xác thực
Để xác thực các lệnh gọi Events API 2.0, bạn cần có mã truy cập (access token). Có hai phương thức để tạo access token cho Events API:
- Sử dụng Trình quản lý sự kiện (Events Manager) - **Khuyến nghị**
  - Phương thức này hỗ trợ tạo token chỉ bằng một cú nhấp chuột. Tuy nhiên, token được tạo chỉ có thể xác thực việc gửi sự kiện với Pixel Code / App ID / Event Set ID được tạo trong cùng một tài khoản quảng cáo TikTok.
  - Xem chi tiết tại "Tùy chọn 1: Trực tiếp trong Events Manager" bên dưới.
- Sử dụng ứng dụng nhà phát triển riêng (Developer App)
  - Phương thức này yêu cầu thiết lập ứng dụng nhà phát triển TikTok for Business. Phương thức này phù hợp cho các trường hợp nâng cao hơn, khi cùng một token được dùng để xác thực sự kiện cho Pixel Code / App ID / Event Set ID thuộc nhiều tài khoản quảng cáo TikTok khác nhau.

## Tùy chọn 1: Trực tiếp trong Events Manager [Khuyến nghị]

### Điều kiện tiên quyết
- Bạn phải là Quản trị viên (Admin) hoặc Nhà điều hành (Operator) của tài khoản quảng cáo để truy cập giao diện tạo token trong Events Manager.
- Nếu không có quyền truy cập, hãy yêu cầu quản trị viên doanh nghiệp tạo token hoặc cấp quyền cần thiết cho bạn.

### Các bước thực hiện
1. Trong Events Manager, điều hướng tới Pixel và nhấp vào tab **Settings** (Cài đặt).
2. Nhấp vào **Tạo mã truy cập (Generate Access Token)**. Mã truy cập sẽ được tạo ngay lập tức. Sau đó bạn có thể sao chép token và bắt đầu thực hiện các yêu cầu API.

Lưu ý rằng mã truy cập tạo trong Events Manager chỉ có thể xác thực gửi sự kiện cho Pixel Code / TikTok App ID / Event Set ID trong cùng tài khoản quảng cáo TikTok đó.

Chúng tôi khuyến nghị bạn bắt đầu bằng mã truy cập tạo từ Events Manager. Bạn luôn có thể chuyển sang sử dụng token từ ứng dụng nhà phát triển sau này nếu doanh nghiệp cần dùng một token duy nhất trên nhiều tài khoản quảng cáo.

## Tùy chọn 2: Sử dụng ứng dụng nhà phát triển riêng (Developer App)

Nếu bạn hoặc nhà quảng cáo đã có ứng dụng nhà phát triển với phạm vi quyền hạn **"Measurement > Report Conversion Event"**, hãy tham khảo [Ủy quyền](marketing-api-xac-thuc-uy-quyen.md#doc-1738373141733378) và [Xác thực](marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162) để tạo mã truy cập qua ứng dụng nhà phát triển.

---

<a id="doc-1771101162079234"></a>
<!-- doc_id: 1771101162079234 -->
<!-- doc_id: 1771101162079234 -->
# Phản hồi và mã lỗi (Responses and errors)
> Đường dẫn: Marketing API > Đo lường quảng cáo (Ad Measurement) > Hướng dẫn (Guides) > Events API 2.0 > Phản hồi và mã lỗi
## Cấu trúc phản hồi API (API response)
Events API 2.0 trả về phản hồi chứa các trường sau:
| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|code |number|Mã phản hồi. Để xem danh sách đầy đủ các mã phản hồi và mô tả, xem [Phụ lục - Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message|string|Thông báo phản hồi. Để biết chi tiết, xem [Phụ lục - Mã trả về](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|request_id |string|Mã nhật ký log ID của yêu cầu, định danh duy nhất cho từng lệnh gọi API. |
|data |object|Dữ liệu trả về.<br>Đối với yêu cầu thành công, trường này sẽ là đối tượng rỗng (`{}`). <br>Đối với yêu cầu thất bại, trường này sẽ không được trả về.|
## Mã phản hồi API (API response codes)
Để xem danh sách đầy đủ tất cả các mã phản hồi do TikTok API for Business trả về, xem [Phụ lục - Mã trả về](../15-appendix/phu-luc-p1.md#doc-1737172488964097).

### Khi yêu cầu thành công
Nếu TikTok tiếp nhận sự kiện thành công, API sẽ trả về phản hồi với mã trạng thái HTTP Status Code `200`. Phần thân phản hồi chứa mã phản hồi API (`code`) bằng `0`.

| Return code (Mã trạng thái phản hồi) | HTTP Status Code | Description | Detail |
|---|---|---|---|
| 0 | 200 | Successful | Yêu cầu đã thành công. |

#### Ví dụ lệnh cURL (Example)
```http
// curl
HTTP 1.1 200 OK
{
  "code": 0,
  "message": "OK",
  "request_id": "{{request_id}}",
  "data":{} 
}
```
### Khi yêu cầu thất bại
Nếu yêu cầu thất bại, bạn sẽ nhận được mã HTTP Status Code `4XX` hoặc `5XX`. Phần thân phản hồi sẽ chứa mã lỗi tương ứng và thông báo giải thích chi tiết nguyên nhân. Kiểm tra trường `message` trong phần thân để biết chi tiết lỗi.

Nếu nhiều sự kiện được gửi trong cùng một lệnh gọi API, trường `message` cũng sẽ chỉ rõ chỉ mục index (bắt đầu từ 0) của sự kiện không hợp lệ đầu tiên. Ví dụ: thông báo lỗi bên dưới cho biết `event_id` của sự kiện **thứ ba** không phải là chuỗi hợp lệ.

Dưới đây là danh sách các lỗi thường gặp trong Events API 2.0:

| Return Code (Mã trả về) | HTTP Status Code | Error reason |
|---|---|---|
| 40001 | 400 | Không có quyền (No permission). ⏎ Bạn không có quyền cần thiết để thao tác trên tài khoản quảng cáo. |
| 40002 | 400 | Payload không hợp lệ (Invalid payload). ⏎ **Nguyên nhân phổ biến**: • Payload không phải JSON hợp lệ. • Thiếu trường bắt buộc hoặc sai kiểu dữ liệu (ví dụ truyền chuỗi khi cần số). • Dữ liệu chưa băm SHA256 cho trường yêu cầu băm (chẳng hạn `email`). • Gửi quá 1.000 sự kiện trong một yêu cầu. |
| 40100 | 401 | Quá nhiều yêu cầu (Vượt hạn ngạch API quota limit). ⏎ **Nguyên nhân phổ biến**: Đã chạm giới hạn tần suất của endpoint (1.000 truy vấn/giây), do đó yêu cầu bị điều tiết (throttled). |
| 40104 | 401 | Mã truy cập (Access token) để trống. |

#### Ví dụ lệnh cURL (Example)
```http
// curl
HTTP/1.1 400 Bad Request
{
  "code": 40002,
  "message": "Invalid value for email: not a valid SHA256-hashed string.",
  "request_id": "{{request_id}}"
}
```

---

<a id="doc-1771101186666498"></a>
<!-- doc_id: 1771101186666498 -->
<!-- doc_id: 1771101186666498 -->
# Các sự kiện được hỗ trợ (Supported events)
> Đường dẫn: Marketing API > Đo lường quảng cáo (Ad Measurement) > Hướng dẫn (Guides) > Events API 2.0 > Các sự kiện được hỗ trợ
Sự kiện được định nghĩa là các hành động mà khách truy cập thực hiện để đạt được một mục tiêu kinh doanh, chẳng hạn như thêm sản phẩm vào giỏ hàng, điền biểu mẫu hoặc hoàn tất giao dịch mua hàng.

TikTok hỗ trợ hai nhóm sự kiện:
- **Sự kiện chuẩn (Standard Events)**: Đây là các hành động được định nghĩa trước với tên gọi quy chuẩn do TikTok đặt ra. Sự kiện chuẩn tương thích với toàn bộ các công cụ tích hợp của TikTok và có thể được dùng để báo cáo chuyển đổi, tối ưu hóa lượt chuyển đổi và tạo tệp đối tượng tùy chỉnh. Xem danh sách chi tiết bên dưới.
- **Sự kiện tùy chỉnh (Custom Events)**: Đây là các hành động mà đối tác TikTok có thể tự định nghĩa ngoài danh sách sự kiện chuẩn. Sự kiện tùy chỉnh có thể được tạo bằng Trình tạo sự kiện (Event Builder) trong Events Manager hoặc gửi trực tiếp qua Pixel và Events API. **Sự kiện tùy chỉnh (hiện tại hỗ trợ sự kiện tùy chỉnh web, app và CRM) khả dụng cho mục đích báo cáo và tạo tệp đối tượng. Hiện CHƯA hỗ trợ tối ưu hóa giá thầu cho sự kiện tùy chỉnh.** Để tìm hiểu thêm, xem [Sự kiện chuẩn và Sự kiện tùy chỉnh](https://ads.tiktok.com/help/article/standard-events-parameters?lang=en).

## Sự kiện chuẩn trên Web (Web Standard Events)
Bảng dưới đây liệt kê tất cả các sự kiện chuẩn được hỗ trợ trên môi trường web, bao gồm cả các sự kiện ngoại tuyến có `event_source` là `web`, cùng các trường khuyến nghị cho đối tượng `properties`. Lưu ý rằng tên sự kiện có phân biệt chữ hoa - chữ thường, vì vậy bạn phải sử dụng chính xác tên hiển thị trong cột **Event** làm tham số `event` trong [/event/track/](../12-api-reference/42-events-2-0.md#doc-1771101303285761).

| Event | Description | Recommended fields in properties object |
|---|---|---|
| `AddPaymentInfo` | Khi thông tin thanh toán được nhập trong luồng thanh toán. |  |
| `AddToCart` | Khi một mặt hàng được thêm vào giỏ hàng. | `content_type`, `quantity`, `description`, `content_id`, `currency`, `value` |
| `AddToWishlist` | Khi một mặt hàng được thêm vào danh sách yêu thích. |  |
| `ApplicationApproval` | Khi một đơn đăng ký hoặc hồ sơ được phê duyệt. |  |
| `CompleteRegistration` | Khi quy trình đăng ký tài khoản được hoàn tất. |  |
| `Contact` | Khi khách hàng liên hệ tư vấn hoặc hỗ trợ. |  |
| `CustomizeProduct` | Khi người dùng tùy chỉnh thuộc tính sản phẩm. |  |
| `Download` | Khi nhấp vào nút tải xuống ứng dụng hoặc tài nguyên. |  |
| `FindLocation` | Khi khách hàng tìm kiếm địa chỉ hoặc vị trí cửa hàng. |  |
| `InitiateCheckout` | Khi khách hàng bắt đầu tiến trình thanh toán. |  |
| `Lead` | Khi biểu mẫu tìm kiếm khách hàng tiềm năng được gửi. |  |
| `Purchase` | Khi giao dịch thanh toán mua hàng hoàn tất. | `content_type`, `quantity`, `description`, `content_id`, `currency`, `value` |
| `Schedule` | Khi người dùng đặt lịch hẹn gặp hoặc tư vấn. |  |
| `Search` | Khi khách hàng thực hiện tìm kiếm trên web/app. |  |
| `StartTrial` | Khi người dùng bắt đầu dùng thử miễn phí sản phẩm/dịch vụ. | `currency`, `value` |
| `SubmitApplication` | Khi người dùng gửi đơn đăng ký hoặc hồ sơ. |  |
| `Subscribe` | Khi người dùng thanh toán gói thuê bao/đăng ký dịch vụ. |  |
| `ViewContent` | Khi người dùng xem một trang nội dung hoặc chi tiết sản phẩm. | `content_type`, `quantity`, `description`, `content_id`, `currency`, `value` |

## Sự kiện chuẩn Ngoại tuyến (Offline Standard Events)
Tập hợp các sự kiện chuẩn được hỗ trợ cho sự kiện ngoại tuyến hoàn toàn giống với danh sách sự kiện chuẩn trên web.

| Event | Description | Recommended fields in properties object |
|---|---|---|
| `AddPaymentInfo` | Khi thông tin thanh toán được nhập trong luồng thanh toán. |  |
| `AddToCart` | Khi một mặt hàng được thêm vào giỏ hàng. | `content_type`, `quantity`, `description`, `content_id`, `currency`, `value` |
| `AddToWishlist` | Khi một mặt hàng được thêm vào danh sách yêu thích. |  |
| `ApplicationApproval` | Khi một đơn đăng ký hoặc hồ sơ được phê duyệt. |  |
| `CompleteRegistration` | Khi quy trình đăng ký tài khoản được hoàn tất. |  |
| `Contact` | Khi khách hàng liên hệ tư vấn hoặc hỗ trợ. |  |
| `CustomizeProduct` | Khi người dùng tùy chỉnh thuộc tính sản phẩm. |  |
| `Download` | Khi nhấp vào nút tải xuống tài nguyên. |  |
| `FindLocation` | Khi khách hàng tìm kiếm địa điểm cửa hàng. |  |
| `InitiateCheckout` | Khi khách hàng bắt đầu tiến trình thanh toán. |  |
| `Lead` | Khi biểu mẫu liên hệ được gửi thành công. |  |
| `Purchase` | Khi giao dịch mua hàng tại cửa hàng/ngoại tuyến hoàn tất. | `content_type`, `quantity`, `description`, `content_id`, `currency`, `value` |
| `Schedule` | Khi người dùng đặt lịch hẹn trực tiếp hoặc qua điện thoại. |  |
| `Search` | Khi người dùng tìm kiếm sản phẩm. |  |
| `StartTrial` | Khi bắt đầu gói dùng thử dịch vụ. | `currency`, `value` |
| `SubmitApplication` | Khi người dùng nộp đơn đăng ký. |  |
| `Subscribe` | Khi đăng ký dịch vụ định kỳ. |  |
| `ViewContent` | Khi xem thông tin chi tiết mặt hàng. | `content_type`, `quantity`, `description`, `content_id`, `currency`, `value` |

## Sự kiện chuẩn trên Ứng dụng (App Standard Events)
> **Lưu ý:** 
> Tên sự kiện cho mục đích kết nối dữ liệu sự kiện (trường `event`) khác với tên sự kiện dùng khi tạo nhóm quảng cáo (trường `optimization_event`). Xem các cột tương ứng để chọn giá trị chính xác.

| Tên sự kiện kết nối dữ liệu ⏎ (giá trị trường event) | Mô tả | Giá trị khuyến nghị cho trường properties | Tên sự kiện khi tạo nhóm quảng cáo ⏎ (giá trị optimization_event) |
|---|---|---|---|
| `AchieveLevel` | Đạt cấp độ trong trò chơi |  | `UPDATE_LEVEL` |
| `AddPaymentInfo` | Thêm thông tin thanh toán |  | `ADD_PAYMENT_INFO` |
| `AddToCart` | Thêm vào giỏ hàng | `content_type`, `content_id`, `description`, `currency`, `value` | `IN_APP_CART` |
| `AddToWishlist` | Thêm vào danh sách yêu thích | `content_type`, `content_id`, `description`, `currency`, `value` | `ADD_TO_WISHLIST` |
| `Checkout` | Đặt đơn hàng | `content_type`, `content_id`, `quantity`, `currency`, `value` | `IN_APP_ORDER` |
| `CompleteTutorial` | Hoàn thành hướng dẫn ban đầu |  | `COMPLETE_TUTORIAL` |
| `CreateGroup` | Tạo nhóm / bang hội |  | `CREATE_GROUP` |
| `CreateRole` | Tạo nhân vật trong game |  | `CREATE_GAMEROLE` |
| `GenerateLead` | Tạo khách hàng tiềm năng |  | `SALES_LEAD` |
| `InAppADClick` | Nhấp vào quảng cáo trong ứng dụng |  | `IN_APP_AD_CLICK` |
| `InAppADImpr` | Hiển thị quảng cáo trong ứng dụng |  | `IN_APP_AD_IMPR` |
| `InstallApp` | Cài đặt ứng dụng |  | `ACTIVE` |
| `JoinGroup` | Tham gia nhóm |  | `JOIN_GROUP` |
| `LaunchAPP` | Mở/khởi chạy ứng dụng |  | `LAUNCH_APP` |
| `LoanApplication` | Nộp hồ sơ vay vốn |  | `LOAN_APPLY` |
| `LoanApproval` | Hồ sơ vay được phê duyệt |  | `LOAN_CREDIT` |
| `LoanDisbursal` | Khoản vay được giải ngân |  | `LOAN_COMPLETION` |
| `Login` | Đăng nhập thành công |  | `LOGIN` |
| `Purchase` | Hoàn tất giao dịch thanh toán | `content_type`, `content_id`, `description`, `currency`, `value` | `ACTIVE_PAY` |
| `Rate` | Đánh giá xếp hạng ứng dụng |  | `RATE` |
| `Registration` | Hoàn tất đăng ký tài khoản |  | `ACTIVE_REGISTER` |
| `Search` | Tìm kiếm trong ứng dụng |  | `SEARCH` |
| `SpendCredits` | Chi tiêu điểm thưởng / tiền ảo |  | `SPEND_CREDITS` |
| `StartTrial` | Bắt đầu dùng thử |  | `START_TRIAL` |
| `Subscribe` | Đăng ký gói thuê bao |  | `SUBSCRIBE` |
| `UnlockAchievement` | Mở khóa thành tựu |  | `UNLOCK_ACHIEVEMENT` |
| `ViewContent` | Xem nội dung chi tiết | `content_type`, `content_id`, `description`, `currency`, `value` | `IN_APP_DETAIL_UV` |

## Sự kiện chuẩn CRM (CRM Standard Events)
Tập hợp các sự kiện chuẩn được hỗ trợ cho CRM giống với danh sách sự kiện chuẩn trên web.

| Event | Description | Recommended fields in properties object |
|---|---|---|
| `AddPaymentInfo` | Khi thông tin thanh toán được nhập trong luồng thanh toán. |  |
| `AddToCart` | Khi một mặt hàng được thêm vào giỏ hàng. | `content_type`, `quantity`, `description`, `content_id`, `currency`, `value` |
| `AddToWishlist` | Khi một mặt hàng được thêm vào danh sách yêu thích. |  |
| `ApplicationApproval` | Khi một đơn đăng ký được phê duyệt. |  |
| `CompleteRegistration` | Khi quy trình đăng ký tài khoản hoàn tất. |  |
| `Contact` | Khi liên hệ tư vấn hoặc hỗ trợ. |  |
| `CustomizeProduct` | Khi người dùng tùy chỉnh cấu hình sản phẩm. |  |
| `Download` | Khi tải xuống tài liệu hoặc ứng dụng. |  |
| `FindLocation` | Khi khách hàng tìm kiếm địa điểm chi nhánh. |  |
| `InitiateCheckout` | Khi bắt đầu tiến trình thanh toán. |  |
| `Lead` | Khi biểu mẫu liên hệ được gửi. |  |
| `Purchase` | Khi thanh toán giao dịch thành công. | `content_type`, `quantity`, `description`, `content_id`, `currency`, `value` |
| `Schedule` | Khi người dùng đặt lịch hẹn làm việc hoặc tư vấn. |  |
| `Search` | Khi khách hàng tìm kiếm thông tin. |  |
| `StartTrial` | Khi bắt đầu gói dùng thử sản phẩm/dịch vụ. | `currency`, `value` |
| `SubmitApplication` | Khi nộp đơn đăng ký. |  |
| `Subscribe` | Khi đăng ký gói thuê bao định kỳ. |  |
| `ViewContent` | Khi xem trang chi tiết sản phẩm hoặc dịch vụ. | `content_type`, `quantity`, `description`, `content_id`, `currency`, `value` |

---

<a id="doc-1771101204435970"></a>
<!-- doc_id: 1771101204435970 -->
<!-- doc_id: 1771101204435970 -->
# Sử dụng dữ liệu hạn chế (Limited data use)
> Đường dẫn: Marketing API > Đo lường quảng cáo (Ad Measurement) > Hướng dẫn (Guides) > Events API 2.0 > Sử dụng dữ liệu hạn chế
Tính năng **"Sử dụng dữ liệu hạn chế" (Limited Data Use - LDU)** dành cho **Events API** và **Pixel** là tính năng giúp doanh nghiệp kiểm soát tốt hơn cách dữ liệu sự kiện được sử dụng trong các hệ thống của TikTok.

Nhằm hỗ trợ nhà quảng cáo tuân thủ quyền từ chối bán và chia sẻ dữ liệu cá nhân theo luật bảo mật thông tin của một số bang tại Hoa Kỳ, TikTok cung cấp tính năng Sử dụng dữ liệu hạn chế ("LDU"). LDU cho Pixel và Events API giúp doanh nghiệp kiểm soát cách xử lý dữ liệu sự kiện. Tính năng này khả dụng tại các bang sau của Hoa Kỳ: California, Colorado, Connecticut, Utah, Virginia, Iowa, Minnesota, Tennessee, Maryland, Delaware, Florida, Montana, Nebraska, New Hampshire, New Jersey, Oregon, Texas, Indiana, Kentucky.

Doanh nghiệp nên tham vấn cố vấn pháp lý về cách sử dụng các sản phẩm của TikTok để tuân thủ luật hiện hành. Để biết chi tiết về luật bảo vệ dữ liệu mới của các bang, vui lòng xem [điều khoản quyền tài phán](https://ads.tiktok.com/i18n/official/article?aid=10015015) đã cập nhật của chúng tôi.

# Giới thiệu về Sử dụng dữ liệu hạn chế
Doanh nghiệp có thể cung cấp cho người dùng trên trang web tùy chọn từ chối bán hoặc chia sẻ dữ liệu của họ.
- Nếu doanh nghiệp sử dụng các công cụ như Events API hoặc Pixel để chia sẻ sự kiện với TikTok, doanh nghiệp có thể gửi cho TikTok một tham số để thông báo rằng nhà quảng cáo muốn xử lý hạn chế đối với dữ liệu sự kiện được chia sẻ.
- TikTok sẽ ghi nhận tham số này như một yêu cầu xử lý dữ liệu hạn chế và sẽ hạn chế các hoạt động xử lý tương ứng nếu sự kiện được chia sẻ diễn ra tại một địa điểm đủ điều kiện.

Doanh nghiệp chọn sử dụng tính năng Sử dụng dữ liệu hạn chế có thể nhận thấy tác động đến quy mô tệp đối tượng tại các bang Hoa Kỳ đủ điều kiện và tác động đến hiệu quả chiến dịch (do dữ liệu LDU không được dùng cho mục đích tối ưu hóa giá thầu).

# Triển khai Sử dụng dữ liệu hạn chế (Events API 2.0)
Để gắn cờ xử lý dữ liệu hạn chế cho một sự kiện, doanh nghiệp chỉ cần thêm một trường bổ sung vào lệnh gọi Events API.
> **Lưu ý:** Bắt buộc phải đưa địa chỉ IP vào dữ liệu gửi đến TikTok qua Events API để bật tính năng Sử dụng dữ liệu hạn chế.

Dưới đây là ví dụ minh họa cho sự kiện "AddToCart" với trường `limited_data_use`:
```http
// curl
{
    "event_source":"web",
    "event_source_id": "{{pixel_code}}",
    "data": [
        {
            "event": "AddToCart",
            "event_time": 1687758765,
            "limited_data_use": true,
            "user": {
                "email": "848a771458438fc2ec420560d769fb9b9b86851ee338ec56517baabd79d3bb4f",
                "phone": "2f9d2b4df907e5c9a7b3434351b55700167b998a83dc479b825096486ffcf4ea",
                "ip": "139.177.225.245"
            },
            "page": {
                "url": "http://www.example.com/purchase?q=hello"
            }
        }
    ]
}
```

---

<a id="doc-1797165504155649"></a>
<!-- doc_id: 1797165504155649 -->
<!-- doc_id: 1797165504155649 -->
# Trình hỗ trợ tạo dữ liệu (Payload Helper)
> Đường dẫn: Marketing API > Đo lường quảng cáo (Ad Measurement) > Hướng dẫn (Guides) > Events API 2.0 > Trình hỗ trợ tạo dữ liệu (Payload Helper)
> **Lưu ý:** 
> Để xem hướng dẫn chi tiết về cách sử dụng Payload Helper, vui lòng tham khảo tài liệu hướng dẫn sử dụng dành cho sự kiện **web** hoặc sự kiện **ứng dụng (app)**. Các hướng dẫn này cung cấp từng bước chi tiết giúp bạn tạo và quản lý payload một cách hiệu quả tại các liên kết sau:
> - [Sử dụng Payload Helper cho Web](do-luong-quang-cao-p1.md#doc-1807346079965186)
> - [Sử dụng Payload Helper cho App](do-luong-quang-cao-p1.md#doc-1819581869993025) 

<iframe
  id="payload-helper-iframe"
  style="width: 100%; height: 100%;"
  src='https://business-api.tiktok.com/payload_helper/'
>

---

<a id="doc-1875218499994561"></a>
<!-- doc_id: 1875218499994561 -->
<!-- doc_id: 1875218499994561 -->
# Gửi dữ liệu phân bổ tùy chỉnh (Custom Attribution) qua Events API 2.0
> Đường dẫn: Marketing API > Đo lường quảng cáo (Ad Measurement) > Hướng dẫn (Guides) > Events API 2.0 > Gửi dữ liệu phân bổ tùy chỉnh qua Events API 2.0
## Tại sao nên gửi dữ liệu Phân bổ tùy chỉnh (Custom Attribution) cho TikTok
Nhà quảng cáo có thể đánh giá hiệu quả quảng cáo TikTok bằng các phương pháp phân bổ được định nghĩa bên ngoài hệ thống TikTok — ví dụ: trong hệ thống Business Intelligence (BI) nội bộ hoặc thông qua nhà cung cấp giải pháp phân bổ bên thứ ba. Các phương pháp này có thể sử dụng các mô hình phân bổ, cửa sổ xem lại (lookback window), điểm tiếp xúc (touchpoint) hoặc quy tắc ghi nhận công trạng khác với mô hình phân bổ mặc định của TikTok. Nếu không nắm bắt được các quyết định phân bổ này, TikTok có thể đánh giá và tối ưu hóa hiệu suất quảng cáo khác với cách doanh nghiệp đo lường thành công.

Dữ liệu **Phân bổ tùy chỉnh (Custom Attribution)** mang lại cho TikTok khả năng nhận diện các kết quả phân bổ mà doanh nghiệp của bạn đã xác định. Thay vì yêu cầu TikTok tự tái tạo lại mô hình phân bổ của bạn, bạn sẽ gửi trực tiếp thông tin phân bổ kết quả — bao gồm điểm tiếp xúc TikTok nào được ghi nhận công trạng và tỷ lệ phân bổ như thế nào. Việc cung cấp dữ liệu này tạo nền tảng tín hiệu vững chắc để TikTok hiểu rõ và đồng bộ với phương pháp đo lường của doanh nghiệp. Khi khả năng Phân bổ tùy chỉnh phát triển, dữ liệu này có thể hỗ trợ các trường hợp sử dụng trong các lĩnh vực đo lường, chẩn đoán, phân phối quảng cáo, tối ưu hóa và thử nghiệm.

## Tính khả dụng
Phân bổ tùy chỉnh được thiết kế để nâng cao hiệu suất chiến dịch của bạn. Dù các kết quả tối ưu hóa cụ thể và ứng dụng hạ nguồn sẽ liên tục được mở rộng, mục tiêu hàng đầu của chúng tôi là tận dụng dữ liệu của bạn để thúc đẩy tác động tối đa khi các tính năng mới được triển khai.

## Dữ liệu Phân bổ tùy chỉnh so với Dữ liệu sự kiện của bên thứ nhất
Dữ liệu sự kiện bên thứ nhất cho TikTok biết những gì đã diễn ra trên trang web hoặc ứng dụng của bạn — ví dụ như lượt mua hàng, đăng ký hoặc thêm vào giỏ hàng. Trong khi đó, dữ liệu Phân bổ tùy chỉnh cho TikTok biết hệ thống phân bổ của bạn đã phân chia công trạng cho kết quả đó như thế nào, dựa trên phương pháp mà doanh nghiệp bạn áp dụng. Hai luồng dữ liệu này bổ trợ cho nhau.

## Khi nào nên sử dụng phương thức Events API
Hãy lựa chọn phương thức tích hợp qua [Events API](../12-api-reference/42-events-2-0.md#doc-1771101303285761) khi:
- Nguồn chân lý (source of truth) cho phân bổ của bạn nằm trong **hệ thống nội bộ** hoặc kho dữ liệu do bạn toàn quyền kiểm soát.
- Bạn đã có một luồng tích hợp đang hoạt động với TikTok Events API 2.0 cho các sự kiện chuyển đổi bên thứ nhất, hoặc sẵn sàng xây dựng một luồng mới.
- Bạn yêu cầu kiểm soát toàn diện từ đầu đến cuối cấu trúc payload, mô hình phân bổ và nhịp độ truyền dữ liệu.

## Dữ liệu bạn sẽ gửi
Về mặt cấu trúc, một tín hiệu Phân bổ tùy chỉnh là một sự kiện bạn gửi bằng lệnh POST đến endpoint TikTok Events API 2.0. Nó hoạt động giống hệt một sự kiện chuyển đổi tiêu chuẩn, nhưng có ba điểm khác biệt cốt lõi:
- Tên sự kiện là một **sự kiện tùy chỉnh** có tiền tố `sot_` (ví dụ: `sot_purchase`).
- Đối tượng `ad` chứa siêu dữ liệu phân bổ do hệ thống nội bộ của bạn tạo ra, bao gồm `attribution_share`, `attribution_model`, `touchpoint_type`, `touchpoint_ts` và các trường liên quan.
- Bạn gửi **mỗi sự kiện cho một điểm tiếp xúc TikTok được phân bổ**, thay vì gửi một sự kiện cho mỗi lượt chuyển đổi.

### Quy tắc 1: Báo cáo từng điểm tiếp xúc được phân bổ như một sự kiện Phân bổ tùy chỉnh độc lập
Mọi điểm tiếp xúc TikTok được ghi nhận công trạng phải được báo cáo dưới dạng một sự kiện Phân bổ tùy chỉnh độc lập. Nếu mô hình phân bổ của bạn phân chia giá trị qua nhiều điểm tiếp xúc TikTok cho một lượt chuyển đổi đơn lẻ, bạn phải gửi một sự kiện cho mỗi điểm tiếp xúc thay vì gửi một sự kiện gộp chung duy nhất:
- **Một sự kiện cho mỗi điểm tiếp xúc được phân bổ**: Nếu một lượt chuyển đổi được chia cho ba điểm tiếp xúc TikTok theo mô hình phân bổ tuyến tính (linear model), bạn phải gửi ba sự kiện Phân bổ tùy chỉnh. Mỗi sự kiện mô tả chính xác một điểm tiếp xúc và mang tỷ lệ giá trị cụ thể trong `ad.attribution_share`.
- **Một sự kiện cho mỗi điểm tiếp xúc, trên mỗi mô hình**: Trong cùng một mô hình phân bổ, một điểm tiếp xúc cụ thể chỉ được báo cáo đúng một lần. Không gửi lại cùng một điểm tiếp xúc theo cùng một mô hình cho cùng một chuyển đổi.
- **Luồng dữ liệu độc lập cho mỗi mô hình**: Nếu bạn đánh giá một chuyển đổi theo nhiều mô hình phân bổ (ví dụ: mô hình tuyến tính và mô hình nhấp chuột cuối cùng - last-click), hãy báo cáo mỗi mô hình như một luồng sự kiện riêng biệt. TikTok sẽ xử lý từng mô hình như một kênh báo cáo riêng biệt.

### Quy tắc 2: Đặt tên mọi sự kiện Phân bổ tùy chỉnh với tiền tố `sot_` và gửi dưới dạng sự kiện tùy chỉnh
Tất cả các sự kiện Phân bổ tùy chỉnh phải tuân thủ quy ước đặt tên bắt đầu bằng `sot_` và phải được truyền dưới dạng sự kiện tùy chỉnh (custom event), không phải sự kiện chuẩn. Ví dụ: một giao dịch mua hàng được phân bổ phải được báo cáo là `sot_purchase`, không phải `purchase`.

### Quy tắc 3: Sử dụng `event_id` riêng biệt cho mỗi sự kiện Phân bổ tùy chỉnh
Gán cho mỗi sự kiện Phân bổ tùy chỉnh một mã `event_id` khác biệt hoàn toàn với `event_id` của sự kiện chuẩn tương ứng.

**Định dạng khuyến nghị**:
- Dẫn xuất mã định danh Phân bổ tùy chỉnh từ mã định danh sự kiện chuẩn ban đầu: `<original_event_id>_sot_<touchpoint_index>`.
- Hoặc tạo một mã UUID mới (Universally Unique Identifier) cho mỗi sự kiện Phân bổ tùy chỉnh.

## Cách xây dựng cấu trúc Payload
Phần này trình bày các bước cụ thể để định dạng payload sự kiện Phân bổ tùy chỉnh và gửi đến [TikTok Events API 2.0](../12-api-reference/42-events-2-0.md#doc-1771101303285761).

### 1. Xây dựng một sự kiện cho mỗi bộ ba (lượt chuyển đổi, điểm tiếp xúc, mô hình phân bổ)
Đối với mỗi lượt chuyển đổi mà hệ thống nội bộ của bạn phân bổ cho TikTok, hãy liệt kê các điểm tiếp xúc được ghi nhận theo từng mô hình báo cáo. Gửi một đối tượng sự kiện cho mỗi tổ hợp (chuyển đổi, điểm tiếp xúc, mô hình), điền các trường như sau:

**Các trường bắt buộc ở cấp sự kiện**:
- `event`: Tên sự kiện Phân bổ tùy chỉnh, có tiền tố `sot_` (ví dụ: `sot_purchase`, `sot_subscribe` hoặc `sot_lead`). Gửi dưới dạng sự kiện tùy chỉnh, không phải sự kiện chuẩn.
- `event_time`: Dấu thời gian Unix tính bằng giây (UTC+0) tại thời điểm diễn ra **lượt chuyển đổi**. Đây không phải là thời gian của điểm tiếp xúc.
- `event_id`: Mã định danh duy nhất cho sự kiện Phân bổ tùy chỉnh này, giữ nguyên không đổi qua các lần thử lại (retries). Định dạng khuyến nghị: `<id>_sot_<index>` hoặc UUID mới.

**Siêu dữ liệu phân bổ (đối tượng `ad`)**:

Đưa mọi quyết định phân bổ do hệ thống nội bộ của bạn tạo ra vào bên trong đối tượng `ad`. Chỉ điền các trường mà hệ thống của bạn có dữ liệu thực tế, để trống các trường còn lại thay vì tự phỏng đoán:
- `ad.attribution_share`: Tỷ lệ công trạng được gán cho điểm tiếp xúc này, nằm trong khoảng `[0.0, 1.0]`.
- `ad.attribution_provider`: Tên hệ thống phân bổ của bạn (ví dụ: tên hệ thống BI nội bộ hoặc đối tác MMP).
- `ad.attribution_model`: Mô hình phân bổ được áp dụng (ví dụ: `linear` hoặc `last_click`).
- `ad.attribution_value`: Giá trị tiền tệ được phân bổ cho điểm tiếp xúc TikTok này.
- `ad.campaign_id`, `ad.ad_id`, `ad.creative_id`: Các mã định danh TikTok của điểm tiếp xúc, thường được trích xuất từ URL trang đích hoặc deeplink.
- `ad.touchpoint_type`: Loại điểm tiếp xúc TikTok được ghi nhận công trạng cho sự kiện này (ví dụ: lượt nhấp hoặc lượt xem).
- `ad.touchpoint_ts`: Dấu thời gian Unix (giây, UTC+0) tại thời điểm điểm tiếp xúc diễn ra.
- `ad.touchpoint_url`: URL được ghi nhận tại điểm tiếp xúc.
- `ad.attribution_window_hr_click` / `ad.attribution_window_hr_view`: Cửa sổ phân bổ theo lượt nhấp và lượt xem được áp dụng, tính bằng giờ.
- `ad.attribution_method`: Phương pháp kỹ thuật dùng để liên kết điểm tiếp xúc với lượt chuyển đổi.
- `ad.decline_reason`: Điền khi `attribution_share = 0` để giải thích lý do không ghi nhận công trạng.
- `ad.utm_id`, `ad.utm_source`, `ad.utm_medium`, `ad.utm_campaign`: Các tham số UTM thu thập từ URL điểm tiếp xúc.

**Bối cảnh đơn hàng và doanh thu (đối tượng `properties`)**:
- `properties.order_id` (**Bắt buộc**): Mã định danh giao dịch. Giá trị này phải giống hệt nhau trên tất cả các sự kiện Phân bổ tùy chỉnh mô tả cùng một lượt chuyển đổi.
- `properties.value` và `properties.currency`: Tổng giá trị của lượt chuyển đổi và đơn vị tiền tệ tương ứng.
- `properties.customer_type`: Nhãn danh mục cho biết phân khúc khách hàng liên kết với sự kiện chuyển đổi (ví dụ: `new` hoặc `returning`).

**Định danh người dùng và bối cảnh trang web hoặc ứng dụng**:
- Điền các trường trong `user`, `page` và `app` theo đúng thiết lập tiêu chuẩn của bạn.

### 2. Ví dụ hoàn chỉnh từ đầu đến cuối (End-to-end example)
Payload mẫu dưới đây minh họa một lượt chuyển đổi đơn lẻ (`order_12345`, trị giá 120 USD) được mô hình phân bổ tuyến tính (linear) chia đều cho ba điểm tiếp xúc TikTok. Hệ thống sẽ gửi ba sự kiện Phân bổ tùy chỉnh, mỗi sự kiện ứng với một điểm tiếp xúc:

```http
// curl
{
  "event_source": "web",
  "event_source_id": "C1A2B3D4E5F6G7H8",
  "data": [
    {
      "event": "sot_purchase",
      "event_time": 1721606400,
      "event_id": "order_12345_sot_0",
      "user": {
        "email": "<sha256_hash>",
        "phone": "<sha256_hash>",
        "external_id": "<sha256_hash>"
      },
      "properties": {
        "order_id": "order_12345",
        "value": 120.00,
        "currency": "USD",
        "customer_type": "returning"
      },
      "page": {
        "url": "https://advertiser.example.com/checkout/success"
      },
      "ad": {
        "attribution_provider": "acme_bi",
        "attribution_share": 0.33,
        "attribution_value": 40.00,
        "attribution_model": "linear",
        "attribution_method": "pixel",
        "attribution_window_hr_click": 168,
        "attribution_window_hr_view": 24,
        "campaign_id": "1780000000000000001",
        "ad_id": "1780000000000000002",
        "creative_id": "1780000000000000003",
        "touchpoint_type": "click",
        "touchpoint_ts": 1721400000,
        "touchpoint_url": "https://advertiser.example.com/lp?utm_source=tiktok&utm_medium=cpc&utm_campaign=summer2026",
        "utm_source": "tiktok",
        "utm_medium": "cpc",
        "utm_campaign": "summer2026"
      }
    },
    {
      "event": "sot_purchase",
      "event_time": 1721606400,
      "event_id": "order_12345_sot_1",
      "user": { "email": "<sha256_hash>" },
      "properties": {
        "order_id": "order_12345",
        "value": 120.00,
        "currency": "USD"
      },
      "ad": {
        "attribution_provider": "acme_bi",
        "attribution_share": 0.33,
        "attribution_value": 40.00,
        "attribution_model": "linear",
        "attribution_method": "pixel",
        "campaign_id": "1780000000000000001",
        "ad_id": "1780000000000000004",
        "creative_id": "1780000000000000005",
        "touchpoint_type": "view",
        "touchpoint_ts": 1721480000
      }
    },
    {
      "event": "sot_purchase",
      "event_time": 1721606400,
      "event_id": "order_12345_sot_2",
      "user": { "email": "<sha256_hash>" },
      "properties": {
        "order_id": "order_12345",
        "value": 120.00,
        "currency": "USD"
      },
      "ad": {
        "attribution_provider": "acme_bi",
        "attribution_share": 0.34,
        "attribution_value": 40.00,
        "attribution_model": "linear",
        "attribution_method": "pixel",
        "campaign_id": "1780000000000000001",
        "ad_id": "1780000000000000006",
        "creative_id": "1780000000000000007",
        "touchpoint_type": "click",
        "touchpoint_ts": 1721560000
      }
    }
  ]
}
```

---

<a id="doc-1739583647070209"></a>
<!-- doc_id: 1739583647070209 -->
<!-- doc_id: 1739583647070209 -->
# Events API 1.0
> Đường dẫn: Marketing API > Đo lường quảng cáo (Ad Measurement) > Hướng dẫn (Guides) > Events API 1.0
> **Quan trọng:** 
> Bằng việc sử dụng các endpoint Events API, bạn đồng ý với [Điều khoản sản phẩm thương mại của TikTok (Dữ liệu)](https://ads.tiktok.com/i18n/official/policy/business-products-terms) và cam kết không chia sẻ dữ liệu nhạy cảm với TikTok.

> **Lưu ý:** 
> Events API 2.0 ([/event/track/](../12-api-reference/42-events-2-0.md#doc-1771101303285761)) hiện là endpoint được khuyến nghị để báo cáo sự kiện từ tất cả các nguồn, bao gồm web, ứng dụng (app), ngoại tuyến (offline) và hệ thống CRM (quản lý quan hệ khách hàng). Endpoint này cung cấp một cấu trúc schema API thống nhất giúp các nhà quảng cáo đơn giản hóa và tối ưu quy trình tích hợp.
> Để đảm bảo quá trình chuyển đổi suôn sẻ, sáu endpoint Events API 1.0 sau đây đã bắt đầu ngừng hoạt động từ H2 2024: • [/pixel/track/](../12-api-reference/43-events-1-0-p1.md#doc-1740858531237890) và [/pixel/batch/](../12-api-reference/43-events-1-0-p1.md#doc-1740858565852225) • [/offline/track/](../12-api-reference/43-events-1-0-p1.md#doc-1758428013689857) và [/offline/batch/](../12-api-reference/43-events-1-0-p1.md#doc-1758428053652482) • [/app/track/](../12-api-reference/43-events-1-0-p1.md#doc-1740859196043266) và [/app/batch/](../12-api-reference/43-events-1-0-p1.md#doc-1740859218541569)
> Chúng tôi đặc biệt khuyến nghị người dùng mới tích hợp trực tiếp với endpoint Events API 2.0, và người dùng Events API 1.0 hiện tại bắt đầu nâng cấp lên Events API 2.0 càng sớm càng tốt để tận dụng đầy đủ các lợi ích của phiên bản mới nhất.

Phần này cung cấp tài liệu kỹ thuật về Events API 1.0:
- [Sự kiện Web (Events API : Web)](do-luong-quang-cao-p1.md#doc-1739584809311234)
- [Sự kiện Ứng dụng (Events API: App)](do-luong-quang-cao-tom-tat.md#doc-1739584805049345)
- [Sự kiện Ngoại tuyến (Events API: Offline)](do-luong-quang-cao-p1.md#doc-1758049779688450)

---

<a id="doc-1739584809311234"></a>
<!-- doc_id: 1739584809311234 -->
<!-- doc_id: 1739584809311234 -->
# Events API : Web
> Đường dẫn: Marketing API > Đo lường quảng cáo (Ad Measurement) > Hướng dẫn (Guides) > Events API 1.0 > Events API : Web
Phần này giới thiệu cách quản lý sự kiện web thông qua Events API 1.0:
- [Bắt đầu (Get started)](do-luong-quang-cao-p1.md#doc-1739584855420929) 
- [Báo cáo sự kiện web và tham số](do-luong-quang-cao-tom-tat.md#doc-1741601162187777)
- [Thiết lập Khớp nâng cao (Set up Advanced Matching)](do-luong-quang-cao-p1.md#doc-1749819614433282)
- [Thiết lập TikTok Click ID và Cookie](do-luong-quang-cao-p1.md#doc-1739584860883969)
- [Thiết lập External ID](do-luong-quang-cao-p1.md#doc-1765942670613506)
- [Xác minh thiết lập sự kiện](do-luong-quang-cao-p1.md#doc-1739584863252481)
- [Khử trùng lặp sự kiện (Event deduplication)](do-luong-quang-cao-p1.md#doc-1739584864945154)
- [Câu hỏi thường gặp (FAQs)](do-luong-quang-cao-p1.md#doc-1749819287162881)

---

<a id="doc-1739584855420929"></a>
<!-- doc_id: 1739584855420929 -->
<!-- doc_id: 1739584855420929 -->
# Bắt đầu (Get started)
> Đường dẫn: Marketing API > Đo lường quảng cáo (Ad Measurement) > Hướng dẫn (Guides) > Events API 1.0 > Events API : Web > Bắt đầu
> **Quan trọng:** 
> Bằng việc sử dụng Events API, bạn đồng ý với [Điều khoản sản phẩm thương mại của TikTok (Dữ liệu)](https://ads.tiktok.com/i18n/official/policy/business-products-terms) và cam kết không chia sẻ dữ liệu nhạy cảm với TikTok.

Tài liệu này hướng dẫn bạn quy trình thiết lập Web Events API.

# Trước khi bắt đầu
- Bạn cần có quyền truy cập vào TikTok Ads Manager với vai trò Quản trị viên (Admin) hoặc Nhà điều hành (Operator) của tài khoản quảng cáo.
- Bạn cần có tài khoản nhà phát triển TikTok (TikTok Developer Account) và ứng dụng TikTok for Business nếu muốn tạo mã truy cập qua OAuth.

# Các bước triển khai Web Events API
Để triển khai Web Events API, bạn thực hiện theo 3 bước sau:

## Bước 1: Tạo Pixel
1. Đăng nhập vào [TikTok Ads Manager](https://ads.tiktok.com/i18n/home).
2. Điều hướng tới **Công cụ (Tools)** > **Sự kiện (Events)** > **Nguồn dữ liệu Web**.
3. Nhấp vào **Kết nối nguồn dữ liệu (Connect Data Source)** và chọn **Web**.
4. Chọn phương thức thiết lập phù hợp và đặt tên cho Pixel. Sau khi tạo xong, bạn sẽ nhận được một chuỗi **Pixel Code** (ví dụ: `CUSG5HBC77UD11VVRQEG`).

## Bước 2: Tạo mã truy cập (Access Token)
Bạn có thể tạo mã truy cập trực tiếp trong Events Manager:
1. Mở trang chi tiết Pixel vừa tạo.
2. Chuyển sang tab **Cài đặt (Settings)**.
3. Trong phần **Events API**, nhấp vào **Tạo mã truy cập (Generate Access Token)**. Lưu mã token này cẩn thận vào hệ thống máy chủ của bạn.

## Bước 3: Gọi Web Events API để báo cáo sự kiện
Sử dụng endpoint [/pixel/track/](../12-api-reference/43-events-1-0-p1.md#doc-1740858531237890) hoặc [/pixel/batch/](../12-api-reference/43-events-1-0-p1.md#doc-1740858565852225) để báo cáo các sự kiện web diễn ra trên trang của bạn.

Để xem danh sách đầy đủ các tham số và cấu trúc payload, hãy tham khảo [Báo cáo sự kiện web và tham số](do-luong-quang-cao-tom-tat.md#doc-1741601162187777).

---

<a id="doc-1749819614433282"></a>
<!-- doc_id: 1749819614433282 -->
<!-- doc_id: 1749819614433282 -->
# Thiết lập Khớp nâng cao (Set up Advanced Matching)
> Đường dẫn: Marketing API > Đo lường quảng cáo (Ad Measurement) > Hướng dẫn (Guides) > Events API 1.0 > Events API : Web > Thiết lập Khớp nâng cao
Hướng dẫn này dành cho việc triển khai Khớp nâng cao (Advanced Matching) với TikTok Events API. Để biết thêm thông tin về Khớp nâng cao, xem [tại đây](https://ads.tiktok.com/help/article?aid=10007891&redirected=1).

# Phương pháp tối ưu (Best Practices)
Để đạt hiệu quả tối ưu, chúng tôi khuyến khích bạn gửi đồng thời cả địa chỉ email và số điện thoại cho mọi sự kiện khách truy cập. Chúng tôi cũng khuyến nghị kết hợp đồng thời Khớp nâng cao thủ công và Khớp nâng cao tự động:
- **Khớp nâng cao thủ công (Manual Advanced Matching)**: Bạn tự băm thông tin nhận dạng cá nhân (PII) bằng thuật toán SHA256 trên máy chủ của mình và gửi vào các trường tương ứng trong payload API.
- **Khớp nâng cao tự động (Automatic Advanced Matching)**: Pixel TikTok sẽ tự động tìm kiếm và nhận diện các trường biểu mẫu chứa email/số điện thoại trên trang web để tối ưu hóa tỷ lệ khớp.

Xem hướng dẫn chi tiết về các tham số tại [Báo cáo sự kiện web và tham số](do-luong-quang-cao-tom-tat.md#doc-1741601162187777).

---

<a id="doc-1739584860883969"></a>
<!-- doc_id: 1739584860883969 -->
<!-- doc_id: 1739584860883969 -->
# Thiết lập TikTok Click ID và Cookie (Set up TikTok Click ID and Cookies)
> Đường dẫn: Marketing API > Đo lường quảng cáo (Ad Measurement) > Hướng dẫn (Guides) > Events API 1.0 > Events API : Web > Thiết lập TikTok Click ID và Cookie
# Cookie hoặc `_ttp`
Khi sử dụng TikTok Pixel với tính năng cookie của bên thứ nhất được bật trong phần cài đặt Pixel trên TikTok Events Manager, TikTok sẽ tự động lưu một mã nhận dạng duy nhất trong cookie bên thứ nhất có tên `_ttp` trên miền trang web của bạn. Cookie này có thời hạn lưu trữ là 13 tháng.

Chúng tôi khuyến nghị gửi lại giá trị cookie `_ttp` qua Events API để tăng cường tỷ lệ khớp sự kiện của khách truy cập trang web với quảng cáo TikTok. Xem chi tiết tại [Sử dụng Cookie với TikTok Pixel](https://ads.tiktok.com/help/article/using-cookies-with-tiktok-pixel?redirected=2).

# TikTok Click ID (`ttclid`)
TikTok Click ID (`ttclid`) là tham số theo dõi được tự động nối vào URL trang đích khi người dùng nhấp vào quảng cáo TikTok. Ví dụ: `https://www.example.com/landing?ttclid=E.C.P.v3fQ2RHacdksKfofPmlyuStIIHJ4Af1tKYxF9zz2c2PLx1Oaw15oHpcfl5AH`.

Bạn nên lưu giữ `ttclid` trong suốt phiên truy cập của người dùng trên trang web để gửi kèm trong tất cả sự kiện qua Events API. Cửa sổ phân bổ mặc định cho lượt nhấp là 28 ngày.

## Cách lấy và lưu trữ `ttclid`
1. Đọc từ URL trang đích qua tham số `ttclid`.
2. Lưu trữ giá trị vào cookie trình duyệt hoặc HTML5 local storage với thời hạn 28 ngày.

Mã mẫu đọc cookie:
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/pixel/track/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "pixel_code": "BU35TSQHT2A1QT375GMG",
    "event": "InitiateCheckout",
     "event_id":"1616318632825_357",
     "timestamp": "2020-09-17T19:49:27Z",
     "context": {
         "ad": {
             "callback": "123ATXSfe"
         },
         "page": {
             "url": "http://demo.mywebsite.com/purchase",
             "referrer": "http://demo.mywebsite.com"
         },
         "user": {
             "external_id": "f0e388f53921a51f0bb0fc8a2944109ec188b59172935d8f23020b1614cc44bc",
             "phone_number": "2f9d2b4df907e5c9a7b3434351b55700167b998a83dc479b825096486ffcf4ea",
             "email": "dd6ff77f54e2106661089bae4d40cdb600979bf7edc9eb65c0942ba55c7c2d7f",
             "ttp":"94e2a4j9-h3j5-k2h5-98cc-c84a745mk098"
         },
         "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36",
         "ip": "13.57.97.131"
     },
     "properties": {
         "contents": [
          {
             "price": 8,
             "quantity": 2,
             "content_type": "product_group",
             "content_id": "1077218"
           },
           {
             "price": 30,
             "quantity": 1,
             "content_type": "product_group",
             "content_id": "1197218"
           }
         ],
         "currency": "USD",
         "value": 46.00
     }
 }'
```

Mã mẫu lưu cookie:
```http
// curl
function getCookie(name) {
  let cookie = {};
  document.cookie.split(';').forEach(function(el) {
    let [k,v] = el.split('=');
    cookie[k.trim()] = v;
  })
  return cookie[name];
}
getCookie('ttclid') // TikTok Click ID
getCookie('_ttp') //Cookie id
```

Mã mẫu loại bỏ `ttclid` khỏi URL trang đích sau khi thu thập:
```http
// curl
  "context": {
    "ad": {
      "callback": "E.C.P.v3fQ2RHacdksKfofPmlyuStIIHJ4Af1tKYxF9zz2c2PLx1Oaw15oHpcfl5AH"
    },
```

---

<a id="doc-1765942670613506"></a>
<!-- doc_id: 1765942670613506 -->
<!-- doc_id: 1765942670613506 -->
# Thiết lập External ID (Set up External ID)
> Đường dẫn: Marketing API > Đo lường quảng cáo (Ad Measurement) > Hướng dẫn (Guides) > Events API 1.0 > Events API : Web > Thiết lập External ID
External ID (Mã định danh bên ngoài) là mã nhận dạng đại diện cho người dùng trên nền tảng của nhà quảng cáo, chẳng hạn như ID khách hàng, số thẻ thành viên hoặc mã đơn hàng. Khi được chia sẻ, TikTok sẽ tìm cách khớp ID này với người dùng trên TikTok, giúp nâng cao tỷ lệ khớp, mang lại lợi ích đo lường và tối ưu hóa hạ nguồn.

# Lợi ích (Benefits)
Nếu bạn gán ID cho người dùng truy cập trang web, External ID cho phép bạn:
- **Cải thiện hiệu suất tín hiệu**: Nâng cao tỷ lệ khớp trên các kênh và thu thập được nhiều sự kiện hơn.
- **Tăng cường tối ưu hóa chiến dịch**: Hỗ trợ các mô hình đặt giá thầu chiến dịch để tối đa hóa số lượng sự kiện chuyển đổi.
- **Đo lường toàn bộ phễu sự kiện**: Nắm bắt nhiều sự kiện hơn nhờ khả năng khớp dữ liệu hoàn chỉnh giữa các thiết bị và các phiên truy cập.

> **Lưu ý:** 
> Để tối đa hóa lợi ích của External ID, bạn nên thiết lập đồng thời cả Khớp thủ công và Khớp tự động. Xem hướng dẫn Khớp nâng cao cho Pixel SDK tại [đây](do-luong-quang-cao-p2.md#doc-1739585700402178).

# Cách thức hoạt động của External ID
1. Người dùng xem một sản phẩm cụ thể trên trang web của bạn.
2. Bạn gửi sự kiện `ViewContent` qua Pixel trình duyệt chứa giá trị băm của `external id` và thông tin PII đã băm hoặc cookie.
3. TikTok sử dụng dữ liệu PII đã băm liên kết với external ID để tìm kiếm kết quả khớp với tài khoản TikTok.
4. Vài ngày sau, người dùng đó hoàn tất giao dịch mua hàng trên trang web của bạn.
5. Bạn gửi sự kiện mới qua Events API có chứa `external_id`.
6. TikTok nhận `external_id` và khớp tín hiệu này với hoạt động duyệt web trước đó của khách hàng.
7. Tín hiệu này sau đó được sử dụng ở hạ nguồn để cải thiện hiệu suất chiến dịch của bạn.

### Thông tin nhận dạng Pixel được hỗ trợ (Pixel identity information supported)

| user_properties | Mô tả | Yêu cầu định dạng | Ví dụ nội dung |
|---|---|---|---|
| email | Địa chỉ email của khách hàng (nếu có) | Chưa băm hoặc chuyển chữ thường rồi băm SHA-256.<br><br>Đối với giá trị chưa băm:<ul><li>TikTok sẽ tự động băm sha256 trước khi lưu vào hệ thống.</li></ul>Đối với giá trị băm SHA-256:<ul><li>Xóa khoảng trắng đầu cuối, chuyển toàn bộ chữ thường trước khi băm.</li><li>Chỉ chấp nhận thuật toán SHA-256.</li></ul> | `email@example.com` |
| phone_number | Số điện thoại của khách hàng (nếu có) | Chưa băm hoặc băm SHA-256.<br><br>Chuẩn hóa số điện thoại theo định dạng E.164: + [mã quốc gia] [số điện thoại], ví dụ `+12133734253` hoặc `+84912345678`. | `+12133734253` |
| external_id | Mã ID duy nhất từ nhà quảng cáo, chẳng hạn ID thành viên thân thiết, user ID, external cookie ID. | Chưa băm hoặc băm SHA-256.<br><br>Xóa khoảng trắng thừa trước khi băm. | `USER_123456` |

## Thiết lập External ID và Khớp nâng cao cho Events API
- Tham khảo [Tài liệu nhà phát triển Events API](do-luong-quang-cao-tom-tat.md#doc-1741601162187777) để biết cách thiết lập External ID với Events API.

# Quản lý External ID
Nếu bạn đang chia sẻ `external_id` qua TikTok Pixel SDK hoặc Events API nhưng không muốn TikTok sử dụng tham số này cho mục đích khớp hoặc đo lường, vui lòng cập nhật lại cấu hình để loại bỏ trường `external_id`.

---

<a id="doc-1739584863252481"></a>
<!-- doc_id: 1739584863252481 -->
<!-- doc_id: 1739584863252481 -->
# Xác minh thiết lập sự kiện (Verify Events setup)
> Đường dẫn: Marketing API > Đo lường quảng cáo (Ad Measurement) > Hướng dẫn (Guides) > Events API 1.0 > Events API : Web > Xác minh thiết lập sự kiện
Bài viết này hướng dẫn cách xác minh thiết lập kết nối dữ liệu web trong Events API 1.0. Quy trình bao gồm:
- Xác minh sự kiện được tiếp nhận chính xác.
- Xác minh sự kiện được cấu hình và kích hoạt chính xác qua tính năng Thử nghiệm sự kiện (Test Events).
- Xác minh sự kiện được khử trùng lặp chính xác (nếu gửi từ cả Pixel SDK và Events API).

# Xác minh sự kiện được tiếp nhận chính xác
Truy cập trang chi tiết Pixel trong TikTok Ads Manager. Tại tab **Overview** (Tổng quan):
1. Nếu chúng tôi đã nhận được sự kiện gửi từ Events API, bạn sẽ thấy "**Server**" trong cột **Connection Method** (Phương thức kết nối). Hãy làm mới trang để cập nhật trạng thái mới nhất.
2. Nếu bạn gửi sự kiện từ cả Events API và Pixel SDK, bạn sẽ thấy "**Server & Browser**".

# Xác minh sự kiện qua tính năng Thử nghiệm sự kiện (Test Events)
Sau khi thiết lập Pixel và sẵn sàng gửi sự kiện, bạn có thể gửi một sự kiện thử nghiệm để kiểm tra tính chính xác. **Hãy chắc chắn xóa bỏ trường `test_event_code` trước khi chuyển sang môi trường thực tế ('Production').**

## Các bước thực hiện
1. Trong Events Manager, nhấp vào Pixel để xem chi tiết cấu hình.
2. Trong tab **Test Events**, nhấp vào nút sao chép mã thử nghiệm ở **Bước 2** trong phần **Test Server Events**.
3. Trong phần thân yêu cầu API, thêm trường `test_event_code` và dán mã thử nghiệm vừa sao chép. Gửi yêu cầu API:

```http
// http
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/pixel/track/' \
--header 'Access-Token: YOUR_ACCESS_TOKEN' \
--header 'Content-Type: application/json' \
--data-raw '{
  "pixel_code": "YOUR_PIXEL_CODE",
  "event": "Purchase",
  "event_id": "123asdios_1234",
  "timestamp": "2020-12-14T09:49:27Z",
  "test_event_code": "YOUR_TEST_CODE",
  "context": {
    "ad": {
      "callback": "123ATXSfe"
    },
    "page": {
      "url": "http://demo.mywebsite.com/purchase",
      "referrer": "http://demo.mywebsite.com"
    },
    "user": {
      "email": "a4ef46e711c986ea534c9c3d2a1fde303505b539ef5a7ec2a63f23a536d575d1"
    },
    "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36",
    "ip": "13.57.97.131"
  },
  "properties": {
    "contents": [
      {
        "price": 8,
        "quantity": 2,
        "content_id": "1077218",
        "content_name": "running shoes",
        "content_category": "Shoes > Sneakers > running shoes",
        "brand": "your brand name"
      },
      {
        "price": 30,
        "quantity": 1,
        "content_id": "1197218",
        "content_name": "running shoes",
        "content_category": "Shoes > Sneakers > running shoes",
        "brand": "your brand name"
      }
    ],
    "content_type": "product",
    "currency": "USD",
    "value": 46.00
  }
}'
```

4. Truy cập tab **Test Events** của Pixel trong **Events Manager**, và kiểm tra sự kiện trong phần **Event Activity**. Bất kỳ lỗi cấu trúc payload nào cũng sẽ được hiển thị để bạn khắc phục.

# Xác minh sự kiện được khử trùng lặp chính xác
Để có hiệu suất quảng cáo tối ưu, chúng tôi khuyến nghị thiết lập đồng thời cả TikTok Pixel SDK và Events API để đạt mức độ bao phủ dữ liệu tối đa. Trong trường hợp này, bạn cần thiết lập cơ chế khử trùng lặp để loại trừ các sự kiện trùng lặp. Xem chi tiết tại [Khử trùng lặp sự kiện](do-luong-quang-cao-p1.md#doc-1739584864945154).

---

<a id="doc-1739584864945154"></a>
<!-- doc_id: 1739584864945154 -->
<!-- doc_id: 1739584864945154 -->
# Khử trùng lặp sự kiện (Event deduplication)
> Đường dẫn: Marketing API > Đo lường quảng cáo (Ad Measurement) > Hướng dẫn (Guides) > Events API 1.0 > Events API : Web > Khử trùng lặp sự kiện
**Để đạt hiệu suất quảng cáo tốt nhất, chúng tôi khuyến nghị nhà quảng cáo thiết lập đồng thời cả TikTok Pixel SDK và Events API để đảm bảo phạm vi bao phủ dữ liệu tối đa.**

Khử trùng lặp là tính năng cần thiết cho nhà quảng cáo đang gửi cùng một sự kiện từ cả hai nguồn TikTok Pixel SDK và Events API. Ví dụ: nếu bạn gửi cùng một sự kiện từ cả TikTok Pixel SDK và Events API, bạn cần thiết lập cơ chế khử trùng lặp bằng `event_id` hoặc cookie của bên thứ nhất (`_ttp`). Việc này cho phép TikTok loại bỏ các bản sao trùng lặp của cùng một sự kiện, giúp báo cáo và tối ưu hóa hiệu suất chiến dịch chính xác hơn. Chi tiết xem tại [Khử trùng lặp sự kiện](https://ads.tiktok.com/help/article/event-deduplication?redirected=2).

# `event_id` (Khuyến nghị)
TikTok thực hiện khử trùng lặp sự kiện dựa trên bộ giá trị `pixel_code`, `event` (ví dụ `Purchase` hoặc `AddToCart`) và `event_id`. Nhà quảng cáo nên chọn một chuỗi ký tự duy nhất làm `event_id` cho mỗi sự kiện (chẳng hạn mã đơn hàng hoặc mã giao dịch).

Nếu nhận được nhiều sự kiện có cùng bộ `pixel_code`, `event` và `event_id`, chúng tôi sẽ giữ lại sự kiện đầu tiên và loại bỏ mọi sự kiện đến sau trong vòng 48 giờ. Nếu sự kiện đến sau được nhận trong vòng 5 phút kể từ sự kiện đầu tiên, chúng tôi sẽ hợp nhất dữ liệu của nó vào sự kiện đầu tiên.

## Ví dụ mã Pixel SDK:
```JavaScript
// Example
ttq.track('AddToCart', {
    contents: [
    {
      content_id: '301',
      content_name: 'running shoes',
      content_category: 'Shoes > Sneakers > running shoes',
      brand: 'your brand name',
      quantity: 1,
      price: 8,
    }],
    content_type: 'product',
    value: 9.2,
    currency: 'USD',  
},
{event_id:'1239485'});
```

## Ví dụ Events API:
```http
// Example
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/pixel/track/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "pixel_code": "BU35TSQHT2A1QT375GMG",
  "event": "AddToCart",
  "event_id":"1239485",
  "timestamp": "2020-09-17T19:49:27Z",
  "context": {
    "ad": {
      "callback": "123ATXSfe"
    },
    "user": {
      "external_id": "f0e388f53921a51f0bb0fc8a2944109ec188b59172935d8f23020b1614cc44bc",
      "phone_number": "2f9d2b4df907e5c9a7b3434351b55700167b998a83dc479b825096486ffcf4ea",
      "email": "dd6ff77f54e2106661089bae4d40cdb600979bf7edc9eb65c0942ba55c7c2d7f"
    },
    "user_agent": "Mozilla/5.0 (platform; rv:geckoversion) Gecko/geckotrail Firefox/firefoxversion",
    "ip": "13.57.97.131"
  },
  "properties": {
    "contents": [
     {
        "price": 8,
        "quantity": 2,
        "content_id": "1077218",
        "content_name": "running shoes",
        "content_category": "Shoes > Sneakers > running shoes",
        "brand": "your brand name"
      }
    ],
    "content_type": "product",
    "currency": "USD",
    "value": 46.00
  }
}'
```

# Khử trùng lặp bằng Cookie (_ttp)
Nếu bạn không gửi `event_id` từ Events API nhưng có gửi cookie TikTok (`_ttp`), hệ thống sẽ khử trùng lặp giữa các sự kiện từ trình duyệt và máy chủ dựa trên giá trị của cookie `_ttp` trong cửa sổ 5 phút.

---

<a id="doc-1749819287162881"></a>
<!-- doc_id: 1749819287162881 -->
<!-- doc_id: 1749819287162881 -->
# Câu hỏi thường gặp - Web 1.0 (FAQs)
> Đường dẫn: Marketing API > Đo lường quảng cáo (Ad Measurement) > Hướng dẫn (Guides) > Events API 1.0 > Events API : Web > Câu hỏi thường gặp
**Q1: Tôi nhận được mã phản hồi 40001 thay vì 0, tôi phải làm gì?**

A1: Hãy đảm bảo bạn là Quản trị viên (Admin) hoặc Nhà điều hành (Operator) của tài khoản quảng cáo này. Xem chi tiết tại [Mã trả về](../15-appendix/phu-luc-p1.md#doc-1737172488964097).

**Q2: Tôi có thể tìm Pixel Code ở đâu?**

A2: Đăng nhập vào TikTok Ads Manager, truy cập **Công cụ (Tools)** > **Sự kiện (Events)** > **Nguồn dữ liệu Web**. Bạn sẽ thấy mã Pixel Code hiển thị trong danh sách.

---

<a id="doc-1758049779688450"></a>
<!-- doc_id: 1758049779688450 -->
<!-- doc_id: 1758049779688450 -->
# Events API: Ngoại tuyến (Events API: Offline)
> Đường dẫn: Marketing API > Đo lường quảng cáo (Ad Measurement) > Hướng dẫn (Guides) > Events API 1.0 > Events API: Ngoại tuyến
Phần này giới thiệu cách quản lý sự kiện ngoại tuyến thông qua Events API 1.0:

- [Bắt đầu (Get started)](do-luong-quang-cao-p1.md#doc-1758051319816193) 
- [Câu hỏi thường gặp (FAQs)](do-luong-quang-cao-p1.md#doc-1758052897775617) 
- [Báo cáo sự kiện ngoại tuyến và tham số](do-luong-quang-cao-tom-tat.md#doc-1758053486938113)

---

<a id="doc-1758051319816193"></a>
<!-- doc_id: 1758051319816193 -->
<!-- doc_id: 1758051319816193 -->
# Bắt đầu (Get Started)
> Đường dẫn: Marketing API > Đo lường quảng cáo (Ad Measurement) > Hướng dẫn (Guides) > Events API 1.0 > Events API: Ngoại tuyến > Bắt đầu
Hướng dẫn này mô tả quy trình thiết lập Offline Events API 1.0.

# 1. Ủy quyền và Xác thực (Authorization and Authentication)
Có hai phương thức để lấy mã truy cập (access token):
- Sử dụng luồng OAuth 2.0 của Marketing API
- Sử dụng công cụ tạo access token trực tiếp trong Events Manager

# 2. Tạo Bộ sự kiện ngoại tuyến (Offline Event Set)
Sử dụng endpoint [/offline/create/](../12-api-reference/43-events-1-0-p1.md#doc-1739657891856385) để tạo một Bộ sự kiện ngoại tuyến (Offline Event Set). Sau khi tạo thành công, bạn sẽ nhận được `event_set_id`.

# 3. Gửi sự kiện ngoại tuyến
Sử dụng endpoint [/offline/track/](../12-api-reference/43-events-1-0-p1.md#doc-1758428013689857) để gửi sự kiện đơn lẻ hoặc [/offline/batch/](../12-api-reference/43-events-1-0-p1.md#doc-1758428053652482) để gửi nhiều sự kiện theo lô:

```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/offline/create/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "advertiser_id": "123456", 
  "name": "EVENT_SET_NAME", 
  "description": "In_store_purchases_blackfriday_2021",
  "auto_tracking": true
}
'
```

---

<a id="doc-1758052897775617"></a>
<!-- doc_id: 1758052897775617 -->
<!-- doc_id: 1758052897775617 -->
# Câu hỏi thường gặp - Ngoại tuyến 1.0 (FAQs)
> Đường dẫn: Marketing API > Đo lường quảng cáo (Ad Measurement) > Hướng dẫn (Guides) > Events API 1.0 > Events API: Ngoại tuyến > Câu hỏi thường gặp
**Q1: Tôi nhận được mã phản hồi 40002 thay vì 200, tôi phải làm gì?**

A1: Hãy kiểm tra kỹ payload yêu cầu để đảm bảo không thiếu trường bắt buộc, định dạng JSON hợp lệ và dữ liệu PII đã được băm SHA256 chính xác. Tham khảo [Mã trả về](../15-appendix/phu-luc-p1.md#doc-1737172488964097).

**Q2: Cửa sổ phân bổ cho sự kiện ngoại tuyến là bao lâu?**

A2: Cửa sổ phân bổ tối đa cho phân bổ lượt nhấp (CTA) là 28 ngày và cho phân bổ lượt xem (VTA) là 7 ngày. Bạn có tối đa 28 ngày kể từ khi sự kiện xảy ra để tải dữ liệu lên TikTok.

---

<a id="doc-1770091656601602"></a>
<!-- doc_id: 1770091656601602 -->
<!-- doc_id: 1770091656601602 -->
# Sử dụng dữ liệu hạn chế (Limited Data Use)
> Đường dẫn: Marketing API > Đo lường quảng cáo (Ad Measurement) > Hướng dẫn (Guides) > Events API 1.0 > Sử dụng dữ liệu hạn chế
Tính năng **"Sử dụng dữ liệu hạn chế" (Limited Data Use - LDU)** cho **Events API** và **Pixel** là tính năng giúp doanh nghiệp kiểm soát tốt hơn cách dữ liệu sự kiện được sử dụng trong các hệ thống của TikTok.

Nhằm hỗ trợ nhà quảng cáo tuân thủ quyền từ chối bán và chia sẻ dữ liệu cá nhân theo luật bảo mật thông tin của một số bang tại Hoa Kỳ, TikTok cung cấp tính năng Sử dụng dữ liệu hạn chế ("LDU"). LDU cho Pixel và Events API giúp doanh nghiệp kiểm soát cách thức xử lý dữ liệu sự kiện. Tính năng này khả dụng tại các bang sau của Hoa Kỳ: California, Colorado, Connecticut, Utah, Virginia, Iowa, Minnesota, Tennessee, Maryland, Delaware, Florida, Montana, Nebraska, New Hampshire, New Jersey, Oregon, Texas, Indiana, Kentucky.

Doanh nghiệp nên tham vấn cố vấn pháp lý về cách sử dụng các sản phẩm của TikTok để tuân thủ luật hiện hành. Để biết chi tiết về luật bảo vệ dữ liệu mới của các bang, vui lòng xem [điều khoản quyền tài phán](https://ads.tiktok.com/i18n/official/article?aid=10015015) đã cập nhật của chúng tôi.

Để kích hoạt tính năng LDU trong Events API 1.0, hãy thêm trường `limited_data_use: true` vào payload báo cáo sự kiện của bạn.

---

<a id="doc-1834543156864002"></a>
<!-- doc_id: 1834543156864002 -->
<!-- doc_id: 1834543156864002 -->
# Cổng Events API (Events API Gateway)
> Đường dẫn: Marketing API > Đo lường quảng cáo (Ad Measurement) > Hướng dẫn (Guides) > Cổng Events API (Events API Gateway)
## **Cổng Events API là gì (What is Events API Gateway)**
Events API Gateway là giải pháp đơn giản hóa việc chuyển giao dữ liệu từ máy chủ (server-side) đến Events API của TikTok thông qua đám mây của riêng bạn. Công cụ này hoạt động như một điểm trung chuyển bảo mật giữa trang web của bạn và TikTok.

### **Lợi ích chính**
| Lợi ích | Mô tả chi tiết |
|---|---|
| Better performance | **Hiệu suất cao hơn**: Tăng cường độ chính xác của dữ liệu sự kiện, giảm thiểu sự cố thất thoát dữ liệu do trình chặn quảng cáo hoặc chính sách cookie trình duyệt. |
| More reliable | **Đáng tin cậy hơn**: Dữ liệu được xử lý và gửi trực tiếp từ đám mây riêng của bạn tới máy chủ TikTok. |
| Easy setup | **Thiết lập dễ dàng**: Triển khai nhanh chóng thông qua các mẫu AWS CloudFormation được định cấu hình sẵn. |
| Privacy-Forward | **Định hướng quyền riêng tư**: Giữ quyền kiểm soát dữ liệu người dùng trên môi trường đám mây thuộc quyền quản lý của bạn. |
| Advertiser control | **Quyền kiểm soát cho nhà quảng cáo**: Bạn toàn quyền quản lý cơ sở hạ tầng lưu trữ và các khóa định danh. |

Phần này hướng dẫn triển khai và quản lý Events API Gateway:
- [Hướng dẫn thiết lập Self-Host (Tự lưu trữ)](do-luong-quang-cao-p1.md#doc-1835087586303106)
- [Quản lý Người thuê (Tenants)](do-luong-quang-cao-p1.md#doc-1835087595419649)
- [Quản lý người dùng (User management)](do-luong-quang-cao-p1.md#doc-1835087602015234)
- [Cài đặt cấu hình (Settings)](do-luong-quang-cao-p1.md#doc-1835087607780546)
- [Tích hợp Pixel với Gateway](do-luong-quang-cao-p1.md#doc-1835087630325761)
- [Gỡ cài đặt Events API Gateway](do-luong-quang-cao-p1.md#doc-1835087643351106)

---

<a id="doc-1835087586303106"></a>
<!-- doc_id: 1835087586303106 -->
<!-- doc_id: 1835087586303106 -->
# Hướng dẫn thiết lập Self-Host (Self-Host setup guide)
> Đường dẫn: Marketing API > Đo lường quảng cáo (Ad Measurement) > Hướng dẫn (Guides) > Events API Gateway > Hướng dẫn thiết lập Self-Host
## Điều kiện tiên quyết (Prerequisites)
1. Trước khi triển khai Events API Gateway, hãy đảm bảo bạn có tài khoản AWS. Nếu chưa có, vui lòng tạo tại [Amazon Web Services (AWS)](https://aws.amazon.com/).
2. Đảm bảo tài khoản của bạn có đủ quyền IAM để tạo các tài nguyên AWS sau:
- EC2
- EKS
- ELB
- CloudFormation
- CloudWatch
- EventBridge
- Systems Manager
- ACM (AWS Certificate Manager)
- Security Groups và IAM Roles.

## Các bước triển khai
1. Đăng nhập vào TikTok Ads Manager, truy cập **Công cụ (Tools)** > **Sự kiện (Events)** > **Nguồn dữ liệu Web**.
2. Chọn Pixel và chọn phương thức triển khai **Events API Gateway (Self-hosted)**.
3. Nhấp vào liên kết để khởi chạy mẫu **AWS CloudFormation**.
4. Trên bảng điều khiển AWS, xem lại các tham số ngăn xếp (stack) và nhấp vào **Create Stack**. Quá trình tạo tài nguyên tự động sẽ mất khoảng 15-20 phút.
5. Sau khi trạng thái stack chuyển thành `CREATE_COMPLETE`, sao chép URL đầu ra của Gateway và quay lại giao diện TikTok Ads Manager để hoàn tất xác thực kết nối.

---

<a id="doc-1835087595419649"></a>
<!-- doc_id: 1835087595419649 -->
<!-- doc_id: 1835087595419649 -->
# Người thuê / Không gian quản lý (Tenants)
> Đường dẫn: Marketing API > Đo lường quảng cáo (Ad Measurement) > Hướng dẫn (Guides) > Events API Gateway > Tenants
## Tạo tài khoản người thuê (Create tenant account)
**Quyền yêu cầu**: Quản trị viên Người thuê (Tenant Admin) hoặc Quản trị viên Máy chủ (Host Admin).
- Nhập tên của người thuê mới mà bạn muốn tạo.
- Định cấu hình thông tin định tuyến miền cho người thuê đó.

Một tài khoản Gateway có thể phục vụ nhiều người thuê (multi-tenant), giúp các đại lý (agency) hoặc tập đoàn quản lý nhiều thương hiệu và tài khoản quảng cáo TikTok khác nhau trên cùng một hạ tầng đám mây duy nhất.

## Quản lý người thuê
- Quản trị viên có thể xem danh sách toàn bộ các người thuê hiện có, trạng thái hoạt động và lưu lượng sự kiện tương ứng.
- Có thể thêm, chỉnh sửa hoặc tạm dừng một người thuê bất kỳ lúc nào mà không ảnh hưởng đến các người thuê khác.

---

<a id="doc-1835087602015234"></a>
<!-- doc_id: 1835087602015234 -->
<!-- doc_id: 1835087602015234 -->
# Quản lý người dùng (User management)
> Đường dẫn: Marketing API > Đo lường quảng cáo (Ad Measurement) > Hướng dẫn (Guides) > Events API Gateway > Quản lý người dùng
**Quyền yêu cầu**: Quản trị viên máy chủ (Host admin) hoặc Quản trị viên người thuê (Tenant admin).

## Mời người dùng mới vào vai trò Host Admin
- Nhập địa chỉ email của người dùng bạn muốn mời.
- Chọn vai trò quản trị viên phù hợp. Hệ thống sẽ gửi email chứa liên kết kích hoạt tài khoản.

## Phân quyền người dùng
1. **Host Admin**: Toàn quyền quản trị hạ tầng máy chủ Gateway, quản lý tên miền chính, cấu hình AWS và quản lý tất cả các người thuê.
2. **Tenant Admin**: Quản trị riêng trong phạm vi người thuê được phân bổ, kết nối Pixel và giám sát sự kiện của thương hiệu đó.

---

<a id="doc-1835087607780546"></a>
<!-- doc_id: 1835087607780546 -->
<!-- doc_id: 1835087607780546 -->
# Cài đặt (Settings)
> Đường dẫn: Marketing API > Đo lường quảng cáo (Ad Measurement) > Hướng dẫn (Guides) > Events API Gateway > Cài đặt
## Thiết lập tên miền chính (Primary domain setup)
**Quyền yêu cầu**: Quản trị viên máy chủ (Host admin).

### Với AWS
Dành cho chủ sở hữu tài khoản máy chủ hoặc quản trị viên đại lý:
1. Đăng ký một tên miền con (subdomain) riêng cho Gateway trên miền trang web của bạn (ví dụ: `data.yourdomain.com`).
2. Cấu hình bản ghi CNAME trên nhà cung cấp DNS để trỏ subdomain tới địa chỉ ELB của Gateway trên AWS.
3. Cấp chứng chỉ SSL/TLS miễn phí qua AWS Certificate Manager (ACM) để đảm bảo giao tiếp HTTPS an toàn.

Việc thiết lập tên miền chính trên cùng miền trang web giúp biến các yêu cầu sự kiện thành yêu cầu của bên thứ nhất (first-party context), ngăn ngừa việc bị chặn bởi cookie của bên thứ ba.

---

<a id="doc-1835087630325761"></a>
<!-- doc_id: 1835087630325761 -->
<!-- doc_id: 1835087630325761 -->
# Tích hợp Pixel với Gateway (Pixel integration with Gateway)
> Đường dẫn: Marketing API > Đo lường quảng cáo (Ad Measurement) > Hướng dẫn (Guides) > Events API Gateway > Tích hợp Pixel với Gateway
**Quyền yêu cầu**: Quyền truy cập TikTok Events Manager và là chủ sở hữu Pixel.

## Thiết lập tích hợp
1. Trong Events Manager, truy cập phần cài đặt của Pixel.
2. Tại mục kết nối Gateway, chọn Gateway đã triển khai của bạn.
3. Cập nhật mã cơ sở Pixel (Pixel base code) trên trang web của bạn để định tuyến các sự kiện trực tiếp tới tên miền Gateway thay vì trực tiếp tới TikTok.

Mã Pixel cập nhật sẽ chuyển tiếp sự kiện qua máy chủ Gateway của bạn, tại đây Gateway sẽ tự động bổ sung dữ liệu bên thứ nhất và chuyển tiếp bảo mật sang TikTok Events API.

---

<a id="doc-1835087643351106"></a>
<!-- doc_id: 1835087643351106 -->
<!-- doc_id: 1835087643351106 -->
# Gỡ cài đặt Events API Gateway (Uninstall the Events API Gateway)
> Đường dẫn: Marketing API > Đo lường quảng cáo (Ad Measurement) > Hướng dẫn (Guides) > Events API Gateway > Gỡ cài đặt
Để gỡ cài đặt Events API Gateway, bạn thực hiện theo các bước sau:
1. Ngắt kết nối Gateway khỏi TikTok Events Manager.
2. Xóa các bản ghi CNAME tương ứng trên nhà cung cấp dịch vụ quản lý DNS của bạn.
3. Truy cập vào AWS CloudFormation Console và thực hiện xóa ngăn xếp (Delete Stack) của Gateway để giải phóng toàn bộ tài nguyên đã tạo.

---

<a id="doc-1771101231937537"></a>
<!-- doc_id: 1771101231937537 -->
<!-- doc_id: 1771101231937537 -->
# Nhật ký thay đổi (Changelog)
> Đường dẫn: Marketing API > Đo lường quảng cáo (Ad Measurement) > Hướng dẫn (Guides) > Nhật ký thay đổi
Phiên bản Events API hiện tại: **v2.0**

## Các phiên bản Events API khả dụng (Available Events API Versions)
Bảng dưới đây liệt kê lộ trình ngừng hỗ trợ cụ thể cho từng phiên bản Events API:

| Version | Events API Endpoint | Trạng thái | Ngày ngừng hoạt động |
|---|---|---|---|
| v2.0 | `/event/track/` | Khả dụng (Khuyến nghị) | Hiện hành |
| v1.0 | `/pixel/track/`, `/pixel/batch/`, `/app/track/`, `/app/batch/`, `/offline/track/`, `/offline/batch/` | Không còn hỗ trợ | H2 2024 |

---

<a id="doc-1739583650172929"></a>
<!-- doc_id: 1739583650172929 -->
<!-- doc_id: 1739583650172929 -->
# TikTok App Events SDK
> Đường dẫn: Marketing API > Đo lường quảng cáo (Ad Measurement) > Hướng dẫn (Guides) > TikTok App Events SDK
## Giới thiệu về App Events SDK

> **Quan trọng:** 
> Việc sử dụng TikTok App Events SDK tuân theo [Điều khoản sản phẩm thương mại của TikTok (Dữ liệu)](https://ads.tiktok.com/i18n/official/policy/business-products-terms).

TikTok App Events SDK là một bộ thư viện phát triển phần mềm cho phép các nhà phát triển ứng dụng di động đo lường chính xác các hành động của người dùng trong ứng dụng (chẳng hạn cài đặt, mở ứng dụng, hoàn tất thanh toán) và chuyển tiếp tới TikTok.

SDK hỗ trợ đa nền tảng bao gồm:
- Android (Java, Kotlin)
- iOS (Objective-C, Swift)
- Unity
- React Native

Tài liệu trong phần này hướng dẫn bạn tích hợp và cấu hình SDK cho ứng dụng của mình:
- [Lịch sử phát hành (Release history)](do-luong-quang-cao-p1.md#doc-1739584951798785)
- [Bắt đầu sử dụng SDK (Getting started)](do-luong-quang-cao-p1.md#doc-1862119945765889)

---

<a id="doc-1739584951798785"></a>
<!-- doc_id: 1739584951798785 -->
<!-- doc_id: 1739584951798785 -->
# Lịch sử phát hành (Release history)
> Đường dẫn: Marketing API > Đo lường quảng cáo (Ad Measurement) > Hướng dẫn (Guides) > TikTok App Events SDK > Lịch sử phát hành
Dưới đây là nhật ký phát hành các phiên bản của TikTok App Events SDK trên các nền tảng iOS, Android, Unity và React Native:

| Ngày phát hành | Phiên bản (Version) | Nội dung cập nhật |
|---|---|---|
| 31/08/2026 | iOS: 1.7.2, Unity: 1.7.2, React: 0.1.3 | • [Sửa lỗi] iOS: Không báo cáo các giao dịch StoreKit chưa hoàn tất.<br>• [Cải tiến] Cập nhật khả năng tương thích nền tảng mới nhất. |
| 15/06/2026 | Android: 1.7.1, iOS: 1.7.1, Unity: 1.7.1 | • Tối ưu hóa tính năng báo cáo doanh thu quảng cáo trong ứng dụng (IAE).<br>• Cải thiện hiệu năng xử lý hàng đợi sự kiện ngoại tuyến. |
| 01/03/2026 | Android: 1.7.0, iOS: 1.7.0 | • Hỗ trợ hoàn chỉnh cho mô hình SKAdNetwork 4.0 trên iOS.<br>• Nâng cấp cơ chế phân bổ liên kết sâu (Deferred Deeplinking). |

---

<a id="doc-1862119945765889"></a>
<!-- doc_id: 1862119945765889 -->
<!-- doc_id: 1862119945765889 -->
# Bắt đầu sử dụng SDK (Getting started)
> Đường dẫn: Marketing API > Đo lường quảng cáo (Ad Measurement) > Hướng dẫn (Guides) > TikTok App Events SDK > Bắt đầu sử dụng SDK
Dưới đây là tóm tắt các bước cần thiết để cài đặt và cấu hình TikTok App Events SDK cho ứng dụng của bạn:

1. **Thêm SDK vào dự án ứng dụng**: Tích hợp gói thư viện SDK tương ứng qua CocoaPods/Swift Package Manager (cho iOS), Gradle/Maven (cho Android), Unity Package Manager (cho Unity) hoặc npm/yarn (cho React Native).
2. **Khởi tạo SDK (Initialize the SDK)**: Khởi tạo SDK trong vòng đời khởi động của ứng dụng (ví dụ trong `AppDelegate` trên iOS hoặc `Application.onCreate` trên Android) với TikTok App ID và TikTok App Secret của bạn.
3. **Cấu hình theo dõi sự kiện (Event Tracking)**: Gọi các hàm theo dõi sự kiện chuẩn hoặc sự kiện tùy chỉnh tại các điểm tương tác chính của người dùng trong ứng dụng.
4. **Kiểm tra và xác minh (Verification)**: Sử dụng tính năng Sự kiện thử nghiệm (Test Events) trong TikTok Events Manager để đảm bảo các sự kiện được gửi và tiếp nhận thành công.

Để xem hướng dẫn chi tiết theo từng nền tảng, hãy tham khảo các bài viết tương ứng:
- [Cài đặt trên Android](do-luong-quang-cao-tom-tat.md#doc-1739585434183746)
- [Cài đặt trên iOS](do-luong-quang-cao-tom-tat.md#doc-1739585432134657)
- [Cài đặt trên Unity](do-luong-quang-cao-tom-tat.md#doc-1824036608950273)
- [Cài đặt trên React Native](do-luong-quang-cao-tom-tat.md#doc-1876482381311362)

---

