# Hướng dẫn đo lường quảng cáo (Ad Measurement) (tóm tắt các tài liệu dài)

> Phân hệ: guide:Marketing API/Ad Measurement:digest.
> Tài liệu biên dịch kỹ thuật chi tiết theo chuẩn TikTok Business API v1.3.

---

## Mục lục điều hướng
- [1. Hướng dẫn thiết lập cho Web (Setup guide for Web) (#doc-1771100865818625)](#doc-1771100865818625)
- [2. Hướng dẫn thiết lập Ngoại tuyến (Setup guide for Offline) (#doc-1771101027431425)](#doc-1771101027431425)
- [3. Hướng dẫn thiết lập cho Ứng dụng (Setup guide for App) (#doc-1771101111730178)](#doc-1771101111730178)
- [4. Hướng dẫn thiết lập CRM (Setup guide for CRM) (#doc-1835052338764993)](#doc-1835052338764993)
- [5. Bảng tham số (Parameters) (#doc-1771101151059969)](#doc-1771101151059969)
- [6. Bộ chuyển đổi tải trọng (Payload Converter) (#doc-1805266308200514)](#doc-1805266308200514)
- [7. Events API : App (Sự kiện ứng dụng 1.0) (#doc-1739584805049345)](#doc-1739584805049345)
- [8. Báo cáo sự kiện Web và tham số (1.0) (#doc-1741601162187777)](#doc-1741601162187777)
- [9. Báo cáo sự kiện Ngoại tuyến và tham số (1.0) (#doc-1758053486938113)](#doc-1758053486938113)
- [10. Cài đặt SDK trên Android (#doc-1739585434183746)](#doc-1739585434183746)
- [11. Cài đặt SDK trên iOS (#doc-1739585432134657)](#doc-1739585432134657)
- [12. Cài đặt SDK trên Unity (#doc-1824036608950273)](#doc-1824036608950273)
- [13. Cài đặt SDK trên React Native (#doc-1876482381311362)](#doc-1876482381311362)
- [14. Báo cáo doanh thu quảng cáo trong ứng dụng (In-app ad revenue reporting) (#doc-1862351923536898)](#doc-1862351923536898)
- [15. Chia sẻ dữ liệu sau khi người dùng đồng ý (Data sharing after user consent) (#doc-1824048384831554)](#doc-1824048384831554)
- [16. Cài đặt Pixel bằng mã tùy chỉnh (Install Pixel using code) (#doc-1739585702922241)](#doc-1739585702922241)
- [17. Thiết lập đồng thời TikTok Pixel và Events API (#doc-1799004052020225)](#doc-1799004052020225)
- [18. Thiết lập sự kiện với Data Layer trong GTM (#doc-1799004097478658)](#doc-1799004097478658)

---

<a id="doc-1771100865818625"></a>
<!-- doc_id: 1771100865818625 -->
<!-- doc_id: 1771100865818625 -->
# Hướng dẫn thiết lập cho Web (Setup guide for Web)
> Đường dẫn: Marketing API > Ad Measurement > Guides > Events API 2.0 > Events API for Web > Setup guide for Web
> **Important:** 
> **Quan trọng:** Bằng việc sử dụng các điểm cuối Events API, bạn đồng ý với [Điều khoản sản phẩm thương mại TikTok (Dữ liệu)](https://ads.tiktok.com/i18n/official/policy/business-products-terms) và cam kết không chia sẻ dữ liệu nhạy cảm với TikTok.

# Bắt đầu (Get Started)
Hướng dẫn này sẽ dẫn dắt bạn qua quy trình thiết lập Events API 2.0 cho Web.

## Trước khi bắt đầu
- Bạn cần có quyền truy cập vào TikTok Ads Manager chứa chức năng kiểm tra sự kiện và các công cụ chẩn đoán giúp bạn trong quá trình thử nghiệm phát triển và xác thực sau tích hợp.
- Bạn phải tạo một pixel trong TikTok Ads Manager tại mục **Công cụ (Tools)** > **Sự kiện (Events)**.
- Khi tạo pixel xong, bạn có thể gửi sự kiện qua trang web bằng cách [cài đặt mã cơ sở pixel](do-luong-quang-cao-tom-tat.md#doc-1739585702922241) hoặc gửi sự kiện qua Events API. Phương pháp tối ưu được khuyến nghị là gửi qua cả hai kênh để tối đa hóa phạm vi thu thập sự kiện và hiệu suất chiến dịch. Thiết lập kênh đôi giúp bảo vệ chiến dịch khỏi bị gián đoạn dữ liệu vì tín hiệu vẫn được gửi từ kênh còn lại nếu một kênh gặp sự cố. Nếu gửi sự kiện từ cả Pixel SDK và Events API, bạn bắt buộc phải thiết lập [khử trùng lặp sự kiện (event deduplication)](do-luong-quang-cao-p1.md#doc-1771100965992450).

Nếu bạn chưa có pixel, hãy bắt đầu từ bước 1 để tạo pixel mới.
Nếu bạn đã có sẵn pixel, hãy bỏ qua bước 1 và bắt đầu từ bước 2.

### 1. Tạo Pixel
a. Trong [TikTok Ads Manager](https://ads.tiktok.com/i18n/home), điều hướng đến **Công cụ (Tools)** > **Sự kiện (Events)** > **Kết nối nguồn dữ liệu (Connect data source)** > **Web**.

b. Thêm trang web của bạn.

c. Chọn phương thức kết nối dữ liệu:
- Tùy chọn 1: **Tích hợp đối tác (Partner integrations)**
- Tùy chọn 2: **Thiết lập thủ công (Manual setup)**

- Nếu chọn "**Tích hợp đối tác (Partner Integrations)**", hãy làm theo các bước trên màn hình để hoàn tất quy trình thiết lập qua một trong các đối tác tích hợp.
- Nếu chọn "**Thiết lập thủ công (Manual Setup)**", bạn có các tùy chọn sau:
	- Chỉ dùng **TikTok Pixel**
	- Chỉ dùng **Events API**
	- Dùng đồng thời **TikTok Pixel + Events API**

Để đạt hiệu suất tối ưu, chúng tôi khuyến nghị thiết lập đồng thời cả TikTok Pixel và Events API. Bạn cần đặt tên và tạo Pixel, sau đó làm theo hướng dẫn trên màn hình để hoàn tất quy trình thiết lập và tạo Pixel.

### 2. Tạo mã truy cập (Access Token)
Để xác thực các lệnh gọi Events API, bạn cần có mã truy cập (Access Token). Để tìm hiểu cách lấy mã truy cập, hãy tham khảo [Events API 2.0 > Xác thực](do-luong-quang-cao-p1.md#doc-1771101130925058).

Ngoài ra, bạn có thể bấm **Tạo mã truy cập (Generate access token)** từ mục pixel > **Cài đặt (Settings)**.

## Chia sẻ sự kiện bằng Events API
Sự kiện là các hành động mà khách truy cập trang web thực hiện nhằm đạt được mục tiêu kinh doanh, chẳng hạn như thêm sản phẩm vào giỏ hàng, điền biểu mẫu hoặc mua hàng. Trước khi tích hợp với Events API, chúng tôi khuyên bạn nên xác định trước những Sự kiện nào bạn muốn chia sẻ với TikTok nhằm phục vụ mục tiêu tiếp thị. Bạn có thể thêm các sự kiện và tham số gửi kèm trong tải trọng.

Để biết chi tiết về các sự kiện web và tham số được hỗ trợ, hãy xem [Các sự kiện được hỗ trợ - Sự kiện Web tiêu chuẩn](do-luong-quang-cao-p1.md#doc-1771101186666498).

## Chia sẻ dữ liệu so khớp trong sự kiện 
Events API cho Web sử dụng thông tin khách hàng như TikTok Click ID (`ttclid`), Đối sánh nâng cao (Advanced Matching), cùng các tín hiệu bổ sung như địa chỉ IP và User Agent để khớp các sự kiện của khách truy cập trang web với người dùng TikTok. Sau khi khớp, dữ liệu được chia sẻ có thể dùng để xây dựng tệp đối tượng nhắm mục tiêu, cung cấp tín hiệu cho thuật toán tối ưu hóa và đo lường kết quả chiến dịch tốt hơn.

# Xác minh thiết lập sự kiện
Sau khi tạo sự kiện, bạn có thể xác minh thiết lập kết nối dữ liệu web và theo dõi hoạt động. Nếu bạn gửi sự kiện từ cả Pixel SDK và Events API, bạn bắt buộc phải thiết lập [khử trùng lặp sự kiện (event deduplication)](do-luong-quang-cao-p1.md#doc-1771100965992450).

Để biết các phương pháp xác minh thiết lập Events API tối ưu nhất, hãy xem [Xác minh thiết lập Events API](do-luong-quang-cao-p1.md#doc-1771100984456193).

# Các phương pháp tối ưu để đạt hiệu suất cao nhất

Để đạt hiệu suất tối ưu với Events API 2.0, chúng tôi khuyến nghị áp dụng các cài đặt sau:
1. Bật cả cookie bên thứ nhất (first-party cookies) và Khớp nâng cao tự động (Automatic Advanced Matching) trong phần cài đặt Pixel tại [TikTok Ads Manager](https://ads.tiktok.com/i18n/home) bằng cách điều hướng đến **Công cụ (Tools)** > **Sự kiện (Events)** > **Nguồn dữ liệu (Data sources)** > chọn pixel > tab **Cài đặt (Settings)**.

2. Thiết lập [TikTok Click ID](do-luong-quang-cao-p1.md#doc-1771100879787009) và [cookie](do-luong-quang-cao-p1.md#doc-1771100936446977).
3. Gửi dữ liệu Khớp nâng cao (Advanced Matching). Để tìm hiểu thêm về Khớp nâng cao, hãy tham khảo [Giới thiệu về Khớp nâng cao cho Web](https://ads.tiktok.com/help/article/advanced-matching-web?redirected=2).
Theo phương pháp tối ưu, chúng tôi khuyến khích bạn gửi cả email và số điện thoại cho tất cả các sự kiện của khách truy cập. Chúng tôi cũng khuyên bạn nên thu thập email và số điện thoại của khách sớm trong phễu chuyển đổi để đạt kết quả tốt nhất, gia tăng xác suất so khớp khách hàng với người dùng TikTok. Bạn cũng có thể truyền External ID (chẳng hạn như mã thành viên) cùng với email và số điện thoại để đạt kết quả so khớp cao nhất. Xem thêm tại [Thiết lập External ID](do-luong-quang-cao-p1.md#doc-1771100952291330).
4. Sử dụng định dạng tải trọng sự kiện được khuyến nghị. 

**Điểm cuối (Endpoint):** https://business-api.tiktok.com/open_api/v1.3/event/track/

**Method** POST

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). ⏎ To obtain an access token, refer to [Events API 2.0 - Authentication](do-luong-quang-cao-p1.md#doc-1771101130925058). |
| Content-Type  ****(Bắt buộc)**** | string | Định dạng dữ liệu yêu cầu. ⏎ Allowed format: `application/json`. |

## Bảng tham số (Parameters) để báo cáo sự kiện Web
Để biết định dạng giá trị của từng tham số, vui lòng tham khảo các danh sách bên dưới.

> **Note:** 
> Để tạo mã mẫu theo định dạng cURL, Python hoặc Node.js để báo cáo sự kiện Web qua Events API 2.0, hãy sử dụng [Công cụ hỗ trợ tải trọng cho Web (Payload Helper for Web)](do-luong-quang-cao-p1.md#doc-1807346079965186).

### Tham số cấp cao nhất (Top-level parameters)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| event_source  ****(Bắt buộc)**** | string | Trường này dùng để chỉ định loại sự kiện bạn đang tải lên qua Events API. ⏎ Các giá trị enum được phép:   •  `web`: Sự kiện diễn ra trên trang web và được đo lường bằng Pixel Code. |
| event_source_id  ****(Bắt buộc)**** | string | ID nguồn sự kiện dùng để đo lường các sự kiện. ⏎ Khi `event_source` là `web`, hãy chỉ định Pixel Code qua trường này. ⏎ To obtain a Pixel Code, refer to [FAQs - Where can I find the Pixel Code](do-luong-quang-cao-p1.md#doc-1771101001228290). |
| data  ****(Bắt buộc)**** | object[] | Mảng đối tượng chứa các sự kiện bạn muốn báo cáo. • Nếu gửi một sự kiện đơn lẻ, truyền một đối tượng trong mảng. • Nếu gom nhiều sự kiện trong một tải trọng, bạn có thể báo cáo tối đa 1.000 sự kiện trong một yêu cầu (vượt quá 1.000 sự kiện sẽ bị từ chối toàn bộ). • Để tối ưu hóa hiệu suất chiến dịch, **rất khuyến nghị gửi sự kiện theo thời gian thực (real-time, không gom batch)** ngay khi phát sinh trên máy chủ của bạn. |
| ↳ event  ****(Bắt buộc)**** | string | Tên sự kiện chuyển đổi. Có thể là Sự kiện tiêu chuẩn (Standard Event) hoặc Sự kiện tùy chỉnh (Custom Event). ⏎ To find out the supported values for Standard Events, refer to [Events API 2.0-Supported events](do-luong-quang-cao-p1.md#doc-1771101186666498). ⏎ To report a Custom Event, pass a customized name in this field. |
| ↳ event_time  ****(Bắt buộc)**** | integer | Thời điểm sự kiện diễn ra, biểu diễn bằng Unix timestamp tính bằng giây theo múi giờ UTC+0. |
| ↳ event_id **(Điều kiện)** | string | Bắt buộc nếu bạn gửi sự kiện web (`event_source` = `web`) từ cả TikTok browser pixel và Events API. ⏎ Mã ID dùng để định danh duy nhất một sự kiện. Có thể băm hoặc không băm. ⏎ TikTok sử dụng bộ ba `event_source_id`, `event_id` và `event` để khử trùng lặp cùng một sự kiện gửi nhiều lần từ một kênh hoặc giữa nhiều kênh (chẳng hạn giữa browser pixel và Events API). ⏎ For more information on event deduplication and how to complete the setup, refer to [Events API 2.0 - Event Deduplication](do-luong-quang-cao-p1.md#doc-1771100965992450). |
| ↳ user  ****(Bắt buộc)**** | object | Thông tin về khách hàng. ⏎ Để xem danh sách các trường trong đối tượng `user`, hãy xem phần "Tham số `user`" bên dưới. |
| ↳ properties | object | Thông tin về sản phẩm, đơn hàng và các giá trị bổ trợ giúp tối ưu hiệu suất quảng cáo. ⏎ Để xem danh sách các trường trong đối tượng `properties`, hãy xem phần "Tham số `properties`" bên dưới. |
| ↳ page  ****(Bắt buộc)**** | object | Thông tin về trang web. ⏎ Để xem danh sách các trường trong đối tượng `page`, hãy xem phần "Tham số `page`" bên dưới. |
| ↳ ad | object | Thông tin về quảng cáo. ⏎ Để xem danh sách các trường trong đối tượng `ad`, hãy xem phần "Tham số `ad`" bên dưới. |
| ↳ limited_data_use | boolean | Để tìm hiểu thêm về tính năng Sử dụng dữ liệu hạn chế, hãy xem [Events API 2.0 - Sử dụng dữ liệu hạn chế](do-luong-quang-cao-p1.md#doc-1771101204435970). |

#### Tham số `user` (`user` parameters)

| Field | Data Type | Recommended ? | Description |
|---|---|---|---|
| ttclid | string | ✅ | TikTok Click ID, a data connection parameter appended to a landing page URL whenever a user clicks on an ad on TikTok. ⏎ The `ttclid` valid period is the same as your CTA window setting in [Attribution Manager](https://ads.tiktok.com/help/article/attribution-manager?redirected=1). ⏎ For more information on sending TikTok Click IDs, refer to [Events API 2.0 - Send TikTok Click ID (`ttclid`)](do-luong-quang-cao-p1.md#doc-1771100879787009). |
| email | string ⏎ or string[] | ✅ | **Bắt buộc băm SHA-256.** ⏎ Địa chỉ email của khách hàng. ⏎ Follow the instructions below to obtain a valid value:  • **Trim** any leading and trailing spaces of each email before hashing.  • **Lowercase** all characters before hashing. • **Hash** the normalized email values using SHA-256.**Example**:  •  Original: " ALICE_abc@gmail.com "  •  Normalized: "alice_abc@gmail.com" (leading and trailing spaces trimmed and lowercased)  •  SHA-256 hashed: "848a771458438fc2ec420560d769fb9b9b86851ee338ec56517baabd79d3bb4f" |
| phone | string ⏎ or string[] | ✅ | **Bắt buộc băm SHA-256.** ⏎ Số điện thoại của khách hàng. ⏎ Follow the instructions below to obtain a valid value:  • **Normalize** the phone number to [E.164 format](https://www.twilio.com/docs/glossary/what-e164) (for example, "+12133734253"). We recommend using [https://github.com/catamphetamine/libphonenumber-js](https://github.com/catamphetamine/libphonenumber-js) for E.164 parsing.  • **Country code** must be included and prefixed with the `+` sign, without any parentheses or leading `0`s. For example, a US phone number should be prefixed with the `+1` country code. •  **No spaces, letters or symbols** except the `+` for the country code are included.  • **SHA-256 hash** the phone number after normalizing. **Example**:  •  Original: "(+1)2133734253" •  Normalized to E.164 format: "+12133734253" •  SHA256 hashed: "9f7ec22d72092cd3c0b58726ed9c2d91b92e51a3f29837508fb2948bb22dd2fd" |
| external_id | string ⏎ or string[] | ✅ | **Bắt buộc băm SHA-256.** ⏎ External ID, mã định danh duy nhất từ phía nhà quảng cáo như mã thành viên, ID người dùng và cookie ngoài. To learn more about the `external_id` parameter, refer to [Events API 2.0 - Set up External ID](do-luong-quang-cao-p1.md#doc-1771100952291330). ⏎ **Example**:  •  Original: "user_123" •  SHA-256 hashed: "80fba0ae1c48e3978e43e4efc365e14e12ea0c830ba8ba5b9a2dafc7e3f2ab8b" |
| ttp | string | ✅ | Cookie ID. ⏎ Nếu bạn cũng sử dụng Pixel SDK và đã bật cookie, Pixel SDK sẽ tự động lưu mã định danh duy nhất vào cookie `_ttp`. Giá trị của `_ttp` được dùng để khớp các sự kiện người truy cập với quảng cáo TikTok. Bạn có thể trích xuất giá trị `_ttp` và gắn vào đây. ⏎ To learn more about the `ttp` parameter, refer to [Events API 2.0 - Send TikTok Cookie (`_ttp`)](https://ads.tiktok.com/marketing_api/docs?id= 1771100936446977). |
| ip | string | ✅ | Địa chỉ **IP công cộng (public IP)** không băm của thiết bị người dùng. ⏎ Để tăng xác suất so khớp sự kiện với quảng cáo TikTok, khuyến nghị gửi cả `ip` và `user_agent`. Hỗ trợ cả IPv4 và IPv6 (dạng đầy đủ hoặc rút gọn). ⏎ For example: • Full format: **2001:0db8:1111:000a:00b0:0000:0000:0200** • Compressed format: **2001:db8:1111:a:b0::200** |
| user_agent | string | ✅ | Chuỗi User Agent không băm từ thiết bị người dùng. ⏎ Để tăng xác suất so khớp sự kiện với quảng cáo TikTok, khuyến nghị gửi cả `ip` và `user_agent`. |
| locale | string |  | Mã định danh ngôn ngữ theo chuẩn BCP 47. ⏎ Để tham khảo, xem [Mã tiêu chuẩn IETF BCP 47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt). |

#### Tham số `properties` (`properties` parameters)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết | Bắt buộc để báo cáo ROAS hoặc VBO | Bắt buộc cho Video Shopping Ads (VSA) |
|---|---|---|---|---|
| content_ids | string[] | ID duy nhất hoặc mảng nhiều ID của các sản phẩm hoặc nội dung. ⏎ Example: `["987", "654"]`. ⏎ Khuyến nghị sử dụng `sku_id` hoặc `item_group_id` khớp với `sku_id` hoặc `item_group_id` đã thiết lập trong danh mục sản phẩm (catalog). ⏎ Trường này là bắt buộc đối với Quảng cáo video mua sắm (VSA). |  | ✅ |
| contents | object[] | Các sản phẩm liên quan trong một sự kiện kèm theo thông tin chi tiết. ⏎ Để xem danh sách các trường trong đối tượng contents, hãy xem phần "Tham số `contents`" bên dưới. |  | ✅ |
| content_type | string | Loại nội dung trong sự kiện. ⏎ Các giá trị enum hỗ trợ: `product`, `product_group`.    • Khi `content_id` trong tham số `contents` là `sku_id`, đặt trường này là `product`.   • Khi `content_id` trong tham số `contents` là `item_group_id`, đặt trường này là `product_group`. |  | ✅ |
| currency | string | **Khuyến nghị cho các sự kiện liên quan đến doanh thu.** ⏎ Mã tiền tệ chuẩn ISO 4217. ⏎ Examples: `EUR`, `USD`, `JPY`. ⏎ **List of currencies currently supported**: `AED`, `ARS`, `AUD`, `BDT`, `BHD`, `BIF`, `BOB`, `BRL`, `CAD`, `CHF`, `CLP`, `CNY`, `COP`, `CRC`, `CZK`, `DKK`, `DZD`, `EGP`, `EUR`, `GBP`, `GTQ`, `HKD`, `HNL`, `HUF`, `IDR`, `ILS`, `INR`, `ISK`, `JPY`, `KES`, `KHR`, `KRW`, `KWD`, `KZT`, `MAD`, `MOP`, `MXN`, `MYR`, `NGN`, `NIO`, `NOK`, `NZD`, `OMR`, `PEN`, `PHP`, `PHP`, `PKR`, `PLN`, `PYG`, `QAR`, `RON`, `RUB`, `SAR`, `SEK`, `SGD`, `THB`, `TRY`, `TWD`, `UAH`, `USD`, `VES`, `VND`, `ZAR` . | ✅ |  |
| value | float | **Khuyến nghị cho các sự kiện liên quan đến doanh thu.** ⏎ Tổng giá trị của đơn hàng hoặc các mặt hàng được bán. ⏎ Giá trị phải luôn được định dạng là số nguyên hoặc số thập phân (ví dụ: `10.00`) bất kể vị trí, loại tiền tệ hay các yếu tố khác. Không chứa ký hiệu tiền tệ, ký tự đặc biệt, chữ cái hoặc dấu phẩy. ⏎ **Lưu ý**: `price` chỉ định giá cho một mặt hàng đơn lẻ, còn `value` chỉ định tổng giá trị đơn hàng. | ✅ |  |
| num_items | integer | Số lượng các mặt hàng. |  |  |
| search_string | string | Chuỗi tìm kiếm do người dùng nhập. |  |  |
| description | string | Mô tả của mặt hàng hoặc trang web. |  |  |
| order_id | string | Mã định danh đơn hàng (Order ID). |  |  |
| shop_id | string | Mã định danh cửa hàng (Shop ID). |  |  |
| customer_type | string | Nhãn phân loại phân khúc khách hàng liên quan đến sự kiện chuyển đổi. ⏎ Các giá trị enum hỗ trợ: • `new`: Khách hàng mới. • `returning`: Khách hàng quay lại. |  |  |

##### Tham số `contents` (`contents` parameters)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết | Bắt buộc để báo cáo ROAS hoặc VBO | Bắt buộc cho Video Shopping Ads (VSA) |
|---|---|---|---|---|
| price | float | Đơn giá của một mặt hàng. ⏎ **Lưu ý**: `price` chỉ định giá cho một mặt hàng đơn lẻ, còn `value` chỉ định tổng giá trị của cả đơn hàng. ⏎ Example: `10`, `10.5`. |  |  |
| content_id | string | ID duy nhất của sản phẩm hoặc nội dung. ⏎ Khuyến nghị sử dụng `sku_id` hoặc `item_group_id` nếu bạn có sẵn. ID phải khớp với `sku_id` hoặc `item_group_id` đã thiết lập trong danh mục sản phẩm. |  | ✅ |
| content_category | string | Danh mục của trang hoặc sản phẩm. |  |  |
| content_name | string | Tên của trang hoặc sản phẩm. |  |  |
| brand | string | Tên thương hiệu của mặt hàng sản phẩm. |  |  |

#### Tham số `page` (`page` parameters)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| url  ****(Bắt buộc)**** | string | URL trình duyệt nơi sự kiện diễn ra, ví dụ giá trị của `location.href` trong JavaScript phía máy khách. ⏎ Khuyến nghị sử dụng URL đầy đủ, bao gồm toàn bộ tham số truy vấn. |
| referrer | string | URL giới thiệu (referrer URL). ⏎ For example, [document.referrer ](https://developer.mozilla.org/en-US/docs/Web/API/Document/referrer) in the client side Javascript, or the server side [Referer http header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referer). ⏎ It is recommended to use the full URL, including all URL parameters. |

#### Tham số `ad` (`ad` parameters)
Sử dụng các tham số `ad` để chia sẻ thông tin về trang web của nhà quảng cáo với Events API 2.0. 

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| campaign_id | string | ID chiến dịch quảng cáo TikTok gắn với điểm chạm, thường được trích xuất từ URL trang đích hoặc deeplink. |
| ad_id | string | ID nhóm quảng cáo TikTok gắn với điểm chạm, thường được trích xuất từ URL trang đích hoặc deeplink. |
| creative_id | string | ID mẫu quảng cáo TikTok gắn với điểm chạm, thường được trích xuất từ URL trang đích hoặc deeplink. |
| attribution_provider | string | Nhà cung cấp dịch vụ phân bổ (Attribution provider). |
| attribution_share | float | Điểm tỷ lệ phân bổ (Attribution share score). ⏎ Điểm số do bạn cung cấp cho mỗi chuyển đổi, đại diện cho phần công nhận mà TikTok nhận được (từ `0.0` đến `1.0`). |
| attribution_value | float | Phần giá trị chuyển đổi mà hệ thống phân bổ của bạn gán cho điểm chạm TikTok này (thường bằng giá trị chuyển đổi nhân với `attribution_share`). ⏎ Example: an order worth $120 credited 25% to a TikTok touchpoint under a linear model yields `attribution_value = 30.0` for that event. |
| attribution_model | string | Mô hình phân bổ được sử dụng để phân bổ cho sự kiện. ⏎ Examples: • `even_weight`: alias for evenly distributed credit. • `first_click`: full credit to the first click in the journey. • `first_touch`: full credit to the first touchpoint in the journey. • `last_click`: full credit to the last click in the journey. • `last_touch`: full credit to the last touchpoint in the journey. • `linear`: equal credit across every attributed touchpoint. |
| touchpoint_type | string | Loại điểm chạm TikTok nhận được ghi nhận cho sự kiện này. ⏎ Examples: • `click`: the user clicked a TikTok ad or a link that originated from a TikTok ad. • `view`: the user was served a TikTok ad impression without clicking. • `engaged_view`: the user watched a video ad for a qualifying duration (for example, 6 seconds or more) without clicking. • `engaged_click`: the user clicked and interacted with a rich media ad format (such as a Playable Ad). • `click_to_store`: the user clicked an ad that directed them straight to an app marketplace (for example, Apple App Store or Google Play). • `hybrid`: a mix of click and view signals contributed to the touchpoint. • `other`: any touchpoint that does not fit the categories above. |
| touchpoint_ts | integer | Thời điểm điểm chạm TikTok diễn ra, biểu diễn bằng Unix timestamp tính bằng giây theo múi giờ UTC+0. |
| touchpoint_url | string | URL nơi điểm chạm được ghi nhận, ví dụ như URL trang đích mà người dùng truy cập sau khi nhấp quảng cáo TikTok. |
| attribution_window_hr_click | integer | Cửa sổ phân bổ nhấp chuột (click-through attribution window), tính bằng **giờ**. ⏎ It defines the maximum interval between a TikTok click touchpoint and the conversion for which the click is still eligible to receive credit. ⏎ Examples: `1`, `24` (1 day), `168` (7 days), `720` (30 days). |
| attribution_window_hr_view | integer | Cửa sổ phân bổ lượt xem (view-through attribution window), tính bằng **giờ**. ⏎ It defines the maximum interval between a TikTok view touchpoint (impression) and the conversion for which the view is still eligible to receive credit. ⏎ Examples: `1`, `24` (1 day), `168` (7 days) |
| attribution_method | string | Phương thức kỹ thuật được sử dụng để liên kết điểm chạm với chuyển đổi. ⏎ Examples: • `pixel`: matched through the TikTok pixel on the advertiser's website. • `PPS`: matched through Post-Purchase Survey. • `deeplink`: matched through a deeplink click identifier. • `modeled`: attribution produced by a statistical or ML model rather than a deterministic match. • `SKAN`: matched through Apple's SKAdNetwork framework. • `shop`: matched through a TikTok Shop signal. |
| decline_reason | string | Lý do hệ thống của bạn từ chối gán công nhận phân bổ cho TikTok đối với sự kiện này. ⏎ Examples: • `attributed_to_other_source`: another channel received the credit. • `organic`: no paid channel received credit; treated as an organic conversion. • `outside_attribution_window`: the TikTok touchpoint fell outside the click or view window. • `invalid_event`: the event failed a partner-side validation check. • `fraud_detected`: the touchpoint was flagged as fraudulent. • `duplicate_event`: the conversion was already counted in a prior report. • `low_confidence_match`: the touchpoint-to-conversion match did not meet the confidence threshold. • `missing_touchpoint`: no eligible TikTok touchpoint was found. • `missing_click_id`: the required TikTok click identifier was absent. • `privacy_threshold_filtered`: the event was filtered out by a privacy threshold. • `unsupported_signal`: the signal type is not supported by the attribution engine. • `other`: any other reason that does not fit the categories above. |
| utm_id | string | Mã định danh duy nhất của chiến dịch tiếp thị hoặc bộ tham số UTM tạo ra điểm chạm. ⏎ It corresponds to the `utm_id` parameter in the landing URL. ⏎ Use this field to report the custom campaign identifier from your landing page URL. This is particularly useful if your internal tracking relies on custom UTM values rather than TikTok's default campaign IDs. ⏎ Example: `summer2026_launch`. |
| utm_source | string | Nguồn lưu lượng truy cập giới thiệu người dùng đến trang đích, được ghi lại trong tham số URL `utm_source`. ⏎ It typically identifies the platform or property that hosted the ad. ⏎ Example: `tiktok`. |
| utm_medium | string | Phương tiện tiếp thị phân phối lưu lượng truy cập, được ghi lại trong tham số URL `utm_medium`. ⏎ It identifies the category of the placement rather than the platform. ⏎ Examples: `cpc`, `paid_social`, `display`. |
| utm_campaign | string | Tên chiến dịch tạo ra điểm chạm, được ghi lại trong tham số URL `utm_campaign`. ⏎ It is used to attribute performance to a specific marketing initiative within the traffic source. ⏎ Example: `summer2026_launch_us`. |

## Tải trọng mẫu (Sample payload)

```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/event/track/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "event_source": "web",
  "event_source_id": "{{PIXEL-CODE}}",
  "data": [
    {
      "event": "Purchase",
      "event_time": 1687758765,
      "event_id": "12345",
      "user": {
        "external_id": "user_12345678",
        "phone": "0c7e6a405862e402eb76a70f8a26fc732d07c32931e9fae9ab1582911d2e8a3b",
        "email": "123456405862e402eb76a70f8a26fc732d07c32931e9fae9ab1582911d2e8a3b",
        "ip": "123.456.789.1",
        "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6.1 Safari/605.1.15",
        "locale": "en_US"
      },
      "properties": {
        "currency": "USD",
        "value": 200.0,
        "content_type": "product",
        "description": "some product decription",
        "contents": [
          {
            "price": 100.0,
            "quantity": 2,
            "content_id": "12345",
            "content_name": "Fancy-AirMax2.0 Black",
            "content_category": "Shoes - Running Shoes",
            "brand": "Fancy Sneakers"
          }
        ]
      }
    }
  ]
}'
```

---

<a id="doc-1771101027431425"></a>
<!-- doc_id: 1771101027431425 -->
<!-- doc_id: 1771101027431425 -->
# Hướng dẫn thiết lập Ngoại tuyến (Setup guide for Offline)
> Đường dẫn: Marketing API > Ad Measurement > Guides > Events API 2.0 > Events API for Offline > Setup guide for Offline
# Bắt đầu (Get Started)
Hướng dẫn này sẽ dẫn dắt bạn qua quy trình thiết lập Events API 2.0 cho Ngoại tuyến (Offline).

- Nếu muốn tạo Bộ sự kiện ngoại tuyến mới, vui lòng bắt đầu từ bước 1.
- Nếu muốn sử dụng Bộ sự kiện ngoại tuyến hiện có, bạn có thể bắt đầu từ bước 2.

## 1. Tạo bộ sự kiện ngoại tuyến (Offline Event Set)

### Tùy chọn 1: Qua giao diện Trình quản lý sự kiện (Events Manager UI)

a. Trong TikTok Ads Manager, điều hướng đến **Công cụ (Tools)** > **Sự kiện (Events)**.

b. Nhấp vào **Kết nối nguồn dữ liệu (Connect data source)** > **Ngoại tuyến (Offline)**. 

c. Nhập **Tên bộ sự kiện ngoại tuyến (Offline event set name)** và chọn **Tạo (Create)**.

d. Bật **Tự động theo dõi (Auto-tracking)**: Tất cả các chiến dịch trong tương lai từ tài khoản quảng cáo này sẽ sử dụng Bộ sự kiện ngoại tuyến này để kết nối dữ liệu quảng cáo và phân bổ.

e. Sau khi tạo Bộ sự kiện ngoại tuyến, hãy ghi lại ID bộ sự kiện ngoại tuyến (giá trị này sẽ được dùng làm `event_source_id` để gửi sự kiện ngoại tuyến qua Events API).

### Tùy chọn 2: Qua API
Bạn cũng có thể tạo một Bộ sự kiện ngoại tuyến mới bằng điểm cuối `/offline/create/`.  

#### Yêu cầu gọi API (Request)
**Địa chỉ (Address):** https://business-api.tiktok.com/open_api/v1.3/offline/create/

**Method** POST

**Request Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). ⏎ To obtain an access token, refer to [Events API 2.0 - Authentication](do-luong-quang-cao-p1.md#doc-1771101130925058). |
| Content-Type  ****(Bắt buộc)**** | string | Định dạng dữ liệu yêu cầu. ⏎ Allowed format: `application/json`. |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id  ****(Bắt buộc)**** | string | ID tài khoản quảng cáo TikTok. |
| name ****(Bắt buộc)**** | string | Offline Event Set name. ⏎ Example: in_store_purchases. |
| description | string | Offline Event Setdescription. ⏎ Example: in_store_purchases_blackfriday. |
| auto_tracking | boolean | Có thực hiện enable Auto Tracking. ⏎ Các giá trị enum hỗ trợ: `true`, `false`. ⏎ If this field is set to `true`, new campaigns created afterwards under this advertiser account will use this event set for ad data connection and attribution. |

##### Ví dụ lệnh cURL (Example)
> **Lưu ý:** Bạn cần thay thế dữ liệu mẫu trong ví dụ bằng dữ liệu thực tế của bạn.

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
}'
```

#### Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Response code. For the complete list of response codes and descriptions, see [Appendix-Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | The log ID of a request, which uniquely identifies the request. |
| data | object | Returned data. ⏎ For a successful request,  this field will be an empty object (`{}`). ⏎ For a failed request, this field will not be returned. |
| ↳ event_set_id | string | ID of the Offline Event Set that you just created. |

##### Ví dụ lệnh cURL (Example)

## 2. Tạo mã truy cập (Access Token)
Để xác thực các lệnh gọi Events API 2.0, bạn cần có mã truy cập (Access Token). Để tìm hiểu cách lấy mã truy cập, hãy tham khảo [Events API 2.0 > Xác thực](do-luong-quang-cao-p1.md#doc-1771101130925058).

# Gửi sự kiện ngoại tuyến bằng Events API 2.0
1. Tải các sự kiện ngoại tuyến lên Bộ sự kiện ngoại tuyến của bạn

Sau khi tạo Bộ sự kiện ngoại tuyến, bạn cần tải các Sự kiện ngoại tuyến lên Bộ sự kiện ngoại tuyến của mình. Sự kiện được định nghĩa là các hành động mà khách hàng ngoại tuyến thực hiện để hoàn thành mục tiêu kinh doanh. Để biết chi tiết về các sự kiện ngoại tuyến được hỗ trợ, hãy xem [Các sự kiện được hỗ trợ - Sự kiện ngoại tuyến tiêu chuẩn](do-luong-quang-cao-p1.md#doc-1771101186666498).

2. Sử dụng định dạng tải trọng sự kiện được khuyến nghị.

**Điểm cuối (Endpoint):** https://business-api.tiktok.com/open_api/v1.3/event/track/

**Method** POST

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). ⏎ To obtain an access token, refer to [Events API 2.0 - Authentication](do-luong-quang-cao-p1.md#doc-1771101130925058). |
| Content-Type  ****(Bắt buộc)**** | string | Định dạng dữ liệu yêu cầu. ⏎ Allowed format: `application/json`. |

## Bảng tham số (Parameters) để báo cáo sự kiện Ngoại tuyến

Để biết định dạng giá trị của từng tham số, vui lòng tham khảo các danh sách bên dưới.

### Tham số cấp cao nhất (Top-level parameters)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| event_source  ****(Bắt buộc)**** | string | Trường này dùng để chỉ định loại sự kiện bạn đang tải lên qua Events API. ⏎ Các giá trị enum được phép:   •  `offline`: Sự kiện chuyển đổi diễn ra tại cửa hàng thực tế và được đo lường bằng Offline Event Set ID. |
| event_source_id  ****(Bắt buộc)**** | string | ID nguồn sự kiện dùng để đo lường các sự kiện. ⏎ Khi `event_source` là `offline`, hãy chỉ định Offline Event Set ID qua trường này. To obtain an Offline Event Set ID, refer to [Setup Guide for Offline-1.Create an Offline Event Set](do-luong-quang-cao-tom-tat.md#doc-1771101027431425) or the instruction below this table. |
| data  ****(Bắt buộc)**** | object[] | Mảng đối tượng chứa các sự kiện bạn muốn báo cáo. • Nếu gửi một sự kiện đơn lẻ, truyền một đối tượng trong mảng. • Nếu gom nhiều sự kiện trong một tải trọng, bạn có thể báo cáo tối đa 1.000 sự kiện trong một yêu cầu (vượt quá 1.000 sự kiện sẽ bị từ chối toàn bộ). • Để tối ưu hóa hiệu suất chiến dịch, **rất khuyến nghị gửi sự kiện theo thời gian thực (real-time, không gom batch)** ngay khi phát sinh trên máy chủ của bạn. |
| ↳ event  ****(Bắt buộc)**** | string | Conversion event name. ⏎ To find out the supported values for this field, refer to [Events API 2.0-Supported events](do-luong-quang-cao-p1.md#doc-1771101186666498). |
| ↳ event_time  ****(Bắt buộc)**** | integer | Thời điểm sự kiện diễn ra, biểu diễn bằng Unix timestamp tính bằng giây theo múi giờ UTC+0. |
| ↳ event_id **(Điều kiện)** | string | A unique value for each event. ⏎ This ID can be used to match data between partner and TikTok. We suggest a String of 32 characters, including numeric digits (0-9), uppercase letters (A-Z), and lowercase letters (a-z). |
| ↳ user  ****(Bắt buộc)**** | object | Thông tin về khách hàng. ⏎ Để xem danh sách các trường trong đối tượng `user`, hãy xem phần "Tham số `user`" bên dưới. |
| ↳ properties | object | Thông tin về sản phẩm, đơn hàng và các giá trị bổ trợ giúp tối ưu hiệu suất quảng cáo. ⏎ Để xem danh sách các trường trong đối tượng `properties`, hãy xem phần "Tham số `properties`" bên dưới. |

- `event_source_id` cho sự kiện Ngoại tuyến là ID của Bộ sự kiện ngoại tuyến mà bạn muốn gửi sự kiện tới. Bạn có thể tìm thấy ID này bằng cách vào **Công cụ (Tools)** > **Sự kiện (Events)** > nút **Nguồn dữ liệu (Data sources)**. ID của Bộ sự kiện ngoại tuyến là `"7481671978261495824"` trong ví dụ bên dưới.

#### Tham số `user` (`user` parameters)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| email | string ⏎ or string[] | **Bắt buộc băm SHA-256.** ⏎ Địa chỉ email của khách hàng. ⏎ Follow the instructions below to obtain a valid value:  • **Trim** any leading and trailing spaces of each email before hashing.  • **Lowercase** all characters before hashing. • **Hash** the normalized email values using SHA-256.**Example**:  •  Original: " ALICE_abc@gmail.com "  •  Normalized: "alice_abc@gmail.com" (leading and trailing spaces trimmed and lowercased)  •  SHA-256 hashed: "848a771458438fc2ec420560d769fb9b9b86851ee338ec56517baabd79d3bb4f" |
| phone | string ⏎ or string[] | **Bắt buộc băm SHA-256.** ⏎ Số điện thoại của khách hàng. ⏎ Follow the instructions below to obtain a valid value:  • **Normalize** the phone number to [E.164 format](https://www.twilio.com/docs/glossary/what-e164) (for example, "+12133734253"). We recommend using [https://github.com/catamphetamine/libphonenumber-js](https://github.com/catamphetamine/libphonenumber-js) for E.164 parsing.  • **Country code** must be included and prefixed with the `+` sign, without any parentheses or leading `0`s. For example, a US phone number should be prefixed with the `+1` country code. •  **No spaces, letters or symbols** except the `+` for the country code are included.  • **SHA-256 hash** the phone number after normalizing. **Example**:  •  Original: "(+1)2133734253" •  Normalized to E.164 format: "+12133734253" •  SHA256 hashed: "9f7ec22d72092cd3c0b58726ed9c2d91b92e51a3f29837508fb2948bb22dd2fd" |

#### Tham số `properties` (`properties` parameters)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| content_ids | string[] | ID duy nhất hoặc mảng nhiều ID của các sản phẩm hoặc nội dung. ⏎ Example: `["987", "654"]`. ⏎ Khuyến nghị sử dụng `sku_id` hoặc `item_group_id` khớp với `sku_id` hoặc `item_group_id` đã thiết lập trong danh mục sản phẩm (catalog). ⏎ Trường này là bắt buộc đối với Quảng cáo video mua sắm (VSA). |
| contents | object[] | Các sản phẩm liên quan trong một sự kiện kèm theo thông tin chi tiết. ⏎ Để xem danh sách các trường trong đối tượng contents, hãy xem phần "Tham số `contents`" bên dưới. |
| content_type | string | Loại nội dung trong sự kiện. ⏎ Các giá trị enum hỗ trợ: `product`, `product_group`.    • Khi `content_id` trong tham số `contents` là `sku_id`, đặt trường này là `product`.   • Khi `content_id` trong tham số `contents` là `item_group_id`, đặt trường này là `product_group`. |
| currency | string | **Khuyến nghị cho các sự kiện liên quan đến doanh thu.** ⏎ Mã tiền tệ chuẩn ISO 4217. ⏎ Examples: `EUR`, `USD`, `JPY`. ⏎ **List of currencies currently supported**: `AED`, `ARS`, `AUD`, `BDT`, `BHD`, `BIF`, `BOB`, `BRL`, `CAD`, `CHF`, `CLP`, `CNY`, `COP`, `CRC`, `CZK`, `DKK`, `DZD`, `EGP`, `EUR`, `GBP`, `GTQ`, `HKD`, `HNL`, `HUF`, `IDR`, `ILS`, `INR`, `ISK`, `JPY`, `KES`, `KHR`, `KRW`, `KWD`, `KZT`, `MAD`, `MOP`, `MXN`, `MYR`, `NGN`, `NIO`, `NOK`, `NZD`, `OMR`, `PEN`, `PHP`, `PHP`, `PKR`, `PLN`, `PYG`, `QAR`, `RON`, `RUB`, `SAR`, `SEK`, `SGD`, `THB`, `TRY`, `TWD`, `UAH`, `USD`, `VES`, `VND`, `ZAR` . |
| value | float | **Khuyến nghị cho các sự kiện liên quan đến doanh thu.** ⏎ Tổng giá trị của đơn hàng hoặc các mặt hàng được bán. ⏎ Giá trị phải luôn được định dạng là số nguyên hoặc số thập phân (ví dụ: `10.00`) bất kể vị trí, loại tiền tệ hay các yếu tố khác. Không chứa ký hiệu tiền tệ, ký tự đặc biệt, chữ cái hoặc dấu phẩy. ⏎ **Lưu ý**: `price` chỉ định giá cho một mặt hàng đơn lẻ, còn `value` chỉ định tổng giá trị đơn hàng. |
| num_items | integer | Số lượng các mặt hàng. |
| search_string | string | Chuỗi tìm kiếm do người dùng nhập. |
| description | string | Mô tả của mặt hàng hoặc trang web. |
| order_id | string | Mã định danh đơn hàng (Order ID). |
| shop_id | string | Mã định danh cửa hàng (Shop ID). |

##### Tham số `contents` (`contents` parameters)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| price | float | Đơn giá của một mặt hàng. ⏎ **Lưu ý**: `price` chỉ định giá cho một mặt hàng đơn lẻ, còn `value` chỉ định tổng giá trị của cả đơn hàng. ⏎ Example: `10`, `10.5`. |
| content_id | string | ID duy nhất của sản phẩm hoặc nội dung. ⏎ Khuyến nghị sử dụng `sku_id` hoặc `item_group_id` nếu bạn có sẵn. ID phải khớp với `sku_id` hoặc `item_group_id` đã thiết lập trong danh mục sản phẩm. |
| content_category | string | Danh mục của trang hoặc sản phẩm. |
| content_name | string | Tên của trang hoặc sản phẩm. |
| brand | string | Tên thương hiệu của mặt hàng sản phẩm. |

Lưu ý rằng một phương án thay thế khác để tải Sự kiện ngoại tuyến lên Bộ sự kiện ngoại tuyến là tải **tệp (file)** lên trong Trình quản lý sự kiện.

## Tải trọng mẫu (Sample payload)

```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/event/track/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "event_source": "offline",
  "event_source_id": "{{Offline-Event-Set-ID}}",
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
# Xác minh thiết lập sự kiện ngoại tuyến
Để biết các phương pháp xác minh thiết lập Events API tối ưu nhất, hãy xem [Xác minh thiết lập Events API](do-luong-quang-cao-p1.md#doc-1771101049613313).

# Quản lý các bộ sự kiện ngoại tuyến *(Không bắt buộc)*
Bạn có thể quản lý các Bộ sự kiện ngoại tuyến theo các cách sau:
- Cập nhật tên hoặc cài đặt Tự động theo dõi của Bộ sự kiện ngoại tuyến qua [/offline/update/](../12-api-reference/43-events-1-0-p1.md#doc-1765596741157889).
- Xóa Bộ sự kiện ngoại tuyến qua [/offline/delete/](../12-api-reference/43-events-1-0-p1.md#doc-1765596790860802).
- Lấy danh sách các Bộ sự kiện ngoại tuyến thuộc tài khoản quảng cáo qua [/offline/get/](../12-api-reference/43-events-1-0-p1.md#doc-1765596808589313).

# Đo lường các bộ sự kiện ngoại tuyến trong quảng cáo thông thường hoặc ACO
Chỉ định các Bộ sự kiện ngoại tuyến mà bạn muốn đo lường trong quảng cáo qua `tracking_offline_event_set_ids` trong [/ad/create/](../12-api-reference/02-ads-p1.md#doc-1739953377508354) hoặc [/ad/aco/create/](../12-api-reference/60-smart-creative.md#doc-1739473063234626). Lưu ý bạn có thể đo lường tối đa 50 Bộ sự kiện ngoại tuyến (trong đó có tối đa 10 bộ tự động theo dõi) trong một quảng cáo.

---

<a id="doc-1771101111730178"></a>
<!-- doc_id: 1771101111730178 -->
<!-- doc_id: 1771101111730178 -->
# Hướng dẫn thiết lập cho Ứng dụng (Setup guide for App)
> Đường dẫn: Marketing API > Ad Measurement > Guides > Events API 2.0 > Events API for App > Setup guide for App
> **Note:** 
> **Lưu ý:** Tính năng báo cáo sự kiện ứng dụng bằng Events API 2.0 hiện chỉ dành cho danh sách cho phép (allowlist). Nếu muốn truy cập, vui lòng liên hệ với đại diện TikTok của bạn.

Hướng dẫn này sẽ dẫn dắt bạn qua quy trình thiết lập Events API 2.0 cho Ứng dụng di động (App).

# Tạo ứng dụng và tạo TikTok App ID
Người dùng có vai trò Quản trị viên (Admin) hoặc Nhà điều hành (Operator) cần thực hiện các bước này trong tài khoản Ads Manager.

## Truy cập Trình quản lý sự kiện
Để bắt đầu tạo ứng dụng, hãy điều hướng đến **Công cụ (Tools) ➤ Sự kiện (Events)** trong tài khoản TikTok Ads Manager của bạn.

## Tạo ứng dụng của bạn

- Nếu bạn chưa thiết lập kết nối dữ liệu nào, chọn **"Bắt đầu (Get started)"**.
- Nếu bạn đã thiết lập các kết nối khác, chọn **"Kết nối nguồn dữ liệu (Connect data source)"**.

Chọn **"Ứng dụng (App)"** và tiếp tục.

## Cung cấp chi tiết ứng dụng

Điền URL tải xuống ứng dụng của bạn và tiếp tục. Biểu tượng ứng dụng, tên ứng dụng và ID ứng dụng sẽ tự động được điền.

Chọn **"Sử dụng TikTok Events API"** và tiếp tục.

Ứng dụng hiện đã được tạo và bạn sẽ thấy một số sự kiện được đề xuất cho ứng dụng của mình dựa theo ngành nghề cụ thể. Sau khi ghi lại, hãy nhấp vào **Hoàn tất (Finish)** để chuyển tới trang chi tiết ứng dụng.

## Tạo TikTok App ID của bạn

Hãy ghi lại **App ID** và sao chép **TikTok App ID** của bạn. Cả hai thông tin này đều bắt buộc để tích hợp.

**App ID** của bạn sẽ ở định dạng reverse DNS (Android) hoặc chuỗi số ngắn (iOS) thường thấy trong URL của App Store hoặc Google Play Store. **TikTok App ID** của bạn là một chuỗi số dài hơn, mang tính định danh riêng cho tài khoản quảng cáo của bạn. ID này sẽ được dùng làm `event_source_id` để gửi các sự kiện ứng dụng qua Events API 2.0.

## Tạo mã truy cập của bạn
Để xác thực lệnh gọi Events API, bạn cần có mã truy cập (Access Token). Bạn có thể tạo mã trong tab "**Cài đặt (Settings)**". Để tìm hiểu thêm cách tạo mã truy cập, hãy tham khảo [Events API 2.0 - Xác thực](do-luong-quang-cao-p1.md#doc-1771101130925058).

# Báo cáo sự kiện ứng dụng (Report an App Event)
Để báo cáo sự kiện (chẳng hạn như `LaunchAPP` hoặc `Purchase`) từ ứng dụng di động (Android hoặc iOS) tới TikTok, hãy gọi điểm cuối Events API 2.0 [/event/track/](../12-api-reference/42-events-2-0.md#doc-1771101303285761).

**Điểm cuối (Endpoint):** https://business-api.tiktok.com/open_api/v1.3/event/track/

**Method** POST

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). ⏎ To obtain an access token, refer to [Events API 2.0 - Authentication](do-luong-quang-cao-p1.md#doc-1771101130925058). |
| Content-Type  ****(Bắt buộc)**** | string | Định dạng dữ liệu yêu cầu. ⏎ Allowed format: `application/json`. |

## Bảng tham số (Parameters) để báo cáo sự kiện Ứng dụng

> **Note:** 
> Để tạo mã mẫu theo định dạng cURL, Python hoặc Node.js để báo cáo sự kiện Ứng dụng qua Events API 2.0, hãy sử dụng [Công cụ hỗ trợ tải trọng cho App (Payload Helper for App)](do-luong-quang-cao-p1.md#doc-1819581869993025).

### Tham số cấp cao nhất (Top-level parameters)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| event_source  ****(Bắt buộc)**** | string | Trường này dùng để chỉ định loại sự kiện bạn đang tải lên qua Events API. ⏎ Các giá trị enum được phép:   •  `app`: Sự kiện diễn ra trên ứng dụng và được đo lường bằng TikTok App ID. ⏎ **Note**: Reporting App Events using Events API 2.0 is currently an allowlist-only feature. If you would like to access it, please contact your TikTok representative. |
| event_source_id  ****(Bắt buộc)**** | string | ID nguồn sự kiện dùng để đo lường các sự kiện. ⏎ Khi `event_source` là `app`, hãy chỉ định TikTok App ID qua trường này. ⏎ To obtain a TikTok App ID, refer to the Create an App in Events Manager and obtain an access token section above. |
| data  ****(Bắt buộc)**** | object[] | Mảng đối tượng chứa các sự kiện bạn muốn báo cáo. • Nếu gửi một sự kiện đơn lẻ, truyền một đối tượng trong mảng. • Nếu gom nhiều sự kiện trong một tải trọng, bạn có thể báo cáo tối đa 1.000 sự kiện trong một yêu cầu (vượt quá 1.000 sự kiện sẽ bị từ chối toàn bộ). • Để tối ưu hóa hiệu suất chiến dịch, **rất khuyến nghị gửi sự kiện theo thời gian thực (real-time, không gom batch)** ngay khi phát sinh trên máy chủ của bạn. |
| ↳ event  ****(Bắt buộc)**** | string | Tên sự kiện chuyển đổi. Có thể là Sự kiện tiêu chuẩn (Standard Event) hoặc Sự kiện tùy chỉnh (Custom Event). ⏎ To find out the supported values for Standard Events, refer to [Events API 2.0-Supported events](do-luong-quang-cao-p1.md#doc-1771101186666498). ⏎ To report a Custom Event, pass a customized name in this field. |
| ↳ event_time  ****(Bắt buộc)**** | integer | Thời điểm sự kiện diễn ra, biểu diễn bằng Unix timestamp tính bằng giây theo múi giờ UTC+0. |
| ↳ user | object | Thông tin về khách hàng. ⏎ Để xem danh sách các trường trong đối tượng `user`, hãy xem phần "Tham số `user`" bên dưới. |
| ↳ properties | object | Thông tin về sản phẩm, đơn hàng và các giá trị bổ trợ giúp tối ưu hiệu suất quảng cáo. ⏎ Để xem danh sách các trường trong đối tượng `properties`, hãy xem phần "Tham số `properties`" bên dưới. |
| ↳ app ****(Bắt buộc)**** | object | Thông tin về ứng dụng di động. ⏎ Để xem danh sách các trường trong đối tượng `app`, hãy xem phần "Tham số `app`" bên dưới. ⏎ **Note**: Reporting App Events using Events API 2.0 is currently an allowlist-only feature. If you would like to access it, please contact your TikTok representative. |
| ↳ ad | object | Thông tin về quảng cáo. ⏎ Để xem danh sách các trường trong đối tượng `ad`, hãy xem phần "Tham số `ad`" bên dưới. |
| ↳ limited_data_use | boolean | Để tìm hiểu thêm về tính năng Sử dụng dữ liệu hạn chế, hãy xem [Events API 2.0 - Sử dụng dữ liệu hạn chế](do-luong-quang-cao-p1.md#doc-1771101204435970). |

#### Tham số `user` (`user` parameters)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| email | string ⏎ or string[] | **Bắt buộc băm SHA-256.** ⏎ Địa chỉ email của khách hàng. ⏎ Follow the instructions below to obtain a valid value:  • **Trim** any leading and trailing spaces of each email before hashing.  • **Lowercase** all characters before hashing. • **Hash** the normalized email values using SHA-256.**Example**:  •  Original: " ALICE_abc@gmail.com "  •  Normalized: "alice_abc@gmail.com" (leading and trailing spaces trimmed and lowercased)  •  SHA-256 hashed: "848a771458438fc2ec420560d769fb9b9b86851ee338ec56517baabd79d3bb4f" |
| phone | string ⏎ or string[] | **Bắt buộc băm SHA-256.** ⏎ Số điện thoại của khách hàng. ⏎ Follow the instructions below to obtain a valid value:  • **Normalize** the phone number to [E.164 format](https://www.twilio.com/docs/glossary/what-e164) (for example, "+12133734253"). We recommend using [https://github.com/catamphetamine/libphonenumber-js](https://github.com/catamphetamine/libphonenumber-js) for E.164 parsing.  • **Country code** must be included and prefixed with the `+` sign, without any parentheses or leading `0`s. For example, a US phone number should be prefixed with the `+1` country code. •  **No spaces, letters or symbols** except the `+` for the country code are included.  • **SHA-256 hash** the phone number after normalizing. **Example**:  •  Original: "(+1)2133734253" •  Normalized to E.164 format: "+12133734253" •  SHA256 hashed: "9f7ec22d72092cd3c0b58726ed9c2d91b92e51a3f29837508fb2948bb22dd2fd" |
| idfa | string | The iOS IDFA. ⏎ For iOS 14 and above, ensure that IDFA data collection follows [Apple’s policies](https://developer.apple.com/app-store/user-privacy-and-data-use/). Both raw and SHA-256 IDFAs are accepted: • For raw IDFAs, all characters must be **UPPERCASE**.  • For SHA-256 IDFAs, all characters must be **lowercase**, and any **leading/trailing spaces** must be **trimmed** before hashing. |
| idfv | string | The iOS IDFV. |
| gaid | string | The GAID (Google Advertising ID). ⏎ Both raw and SHA-256 GAIDs are accepted. ⏎ For both raw and SHA-256 GAIDs: • All characters must be **lowercase**. • **Leading/trailing spaces** must be **trimmed** before hashing |
| ip | string | Non-hashed ** public IP** address of the user's device. ⏎ To increase the probability of matching website visitor events with TikTok ads, we recommend sending both `ip` and `user_agent`. |
| user_agent | string | Chuỗi User Agent không băm từ thiết bị người dùng. ⏎ Để tăng xác suất so khớp sự kiện với quảng cáo TikTok, khuyến nghị gửi cả `ip` và `user_agent`. |
| locale | string | Mã định danh ngôn ngữ theo chuẩn BCP 47. ⏎ Để tham khảo, xem [Mã tiêu chuẩn IETF BCP 47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt). |
| att_status | string | Liệu user has authorized your mobile app to access app-related data for measuring the user or the device. This is an iOS only field. ⏎ Các giá trị enum hỗ trợ: • `AUTHORIZED`: The user has authorized access to app-related data that can be used for measuring the user or the device.  •  `DENIED`: The user has not agreed to authorize your mobile app to access app-related data for measuring the user or the device via [Apple's AppTrackingTransparency framework](https://developer.apple.com/documentation/apptrackingtransparency). ⏎ If this field is set to `DENIED`, TikTok will not use the PII data (for instance, user email address or phone number) in this App Event for user-level matching. • `NOT_DETERMINED`: The user has not yet received an authorization request to authorize access to app-related data that can be used for measuring the user or the device. • `RESTRICTED`: The authorization to access app-related data is restricted. •  `NOT_APPLICABLE`: The iOS version is below 14 or the device is running Android. |

#### Tham số `properties` (`properties` parameters)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| content_ids | string[] | ID duy nhất hoặc mảng nhiều ID của các sản phẩm hoặc nội dung. ⏎ Example: `["987", "654"]`. ⏎ Khuyến nghị sử dụng `sku_id` hoặc `item_group_id` khớp với `sku_id` hoặc `item_group_id` đã thiết lập trong danh mục sản phẩm (catalog). ⏎ Trường này là bắt buộc đối với Quảng cáo video mua sắm (VSA). |
| contents | object[] | Các sản phẩm liên quan trong một sự kiện kèm theo thông tin chi tiết. ⏎ Để xem danh sách các trường trong đối tượng contents, hãy xem phần "Tham số `contents`" bên dưới. |
| content_type | string | Loại nội dung trong sự kiện. ⏎ Các giá trị enum hỗ trợ: `product`, `product_group`.    • Khi `content_id` trong tham số `contents` là `sku_id`, đặt trường này là `product`.   • Khi `content_id` trong tham số `contents` là `item_group_id`, đặt trường này là `product_group`. |
| currency | string | **Khuyến nghị cho các sự kiện liên quan đến doanh thu.** ⏎ Mã tiền tệ chuẩn ISO 4217. ⏎ Examples: `EUR`, `USD`, `JPY`. ⏎ **List of currencies currently supported**: `AED`, `ARS`, `AUD`, `BDT`, `BHD`, `BIF`, `BOB`, `BRL`, `CAD`, `CHF`, `CLP`, `CNY`, `COP`, `CRC`, `CZK`, `DKK`, `DZD`, `EGP`, `EUR`, `GBP`, `GTQ`, `HKD`, `HNL`, `HUF`, `IDR`, `ILS`, `INR`, `ISK`, `JPY`, `KES`, `KHR`, `KRW`, `KWD`, `KZT`, `MAD`, `MOP`, `MXN`, `MYR`, `NGN`, `NIO`, `NOK`, `NZD`, `OMR`, `PEN`, `PHP`, `PHP`, `PKR`, `PLN`, `PYG`, `QAR`, `RON`, `RUB`, `SAR`, `SEK`, `SGD`, `THB`, `TRY`, `TWD`, `UAH`, `USD`, `VES`, `VND`, `ZAR` . |
| value | float | **Khuyến nghị cho các sự kiện liên quan đến doanh thu.** ⏎ Tổng giá trị của đơn hàng hoặc các mặt hàng được bán. ⏎ Giá trị phải luôn được định dạng là số nguyên hoặc số thập phân (ví dụ: `10.00`) bất kể vị trí, loại tiền tệ hay các yếu tố khác. Không chứa ký hiệu tiền tệ, ký tự đặc biệt, chữ cái hoặc dấu phẩy. ⏎ **Lưu ý**: `price` chỉ định giá cho một mặt hàng đơn lẻ, còn `value` chỉ định tổng giá trị đơn hàng. |
| num_items | integer | Số lượng các mặt hàng. |
| search_string | string | Chuỗi tìm kiếm do người dùng nhập. |
| description | string | Mô tả của mặt hàng hoặc trang web. |
| customer_type | string | Nhãn phân loại phân khúc khách hàng liên quan đến sự kiện chuyển đổi. ⏎ Các giá trị enum hỗ trợ: • `new`: Khách hàng mới. • `returning`: Khách hàng quay lại. |

##### Tham số `contents` (`contents` parameters)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| price | float | Đơn giá của một mặt hàng. ⏎ **Lưu ý**: `price` chỉ định giá cho một mặt hàng đơn lẻ, còn `value` chỉ định tổng giá trị của cả đơn hàng. ⏎ Example: `10`, `10.5`. |
| content_id | string | ID duy nhất của sản phẩm hoặc nội dung. ⏎ Khuyến nghị sử dụng `sku_id` hoặc `item_group_id` nếu bạn có sẵn. ID phải khớp với `sku_id` hoặc `item_group_id` đã thiết lập trong danh mục sản phẩm. |
| content_category | string | Danh mục của trang hoặc sản phẩm. |
| content_name | string | Tên của trang hoặc sản phẩm. |
| brand | string | Tên thương hiệu của mặt hàng sản phẩm. |

#### Tham số `app` (`app` parameters)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| app_id  ****(Bắt buộc)**** | string | ** ⏎ Mobile App ID.  •  For iOS Apps, use the app ID found in the App Store URL  •  Example: Apple Store URL: `https://apps.apple.com/us/app/angry-birds/id343200656` • `id` = `"343200656"` •  For Android Apps in the Google Play store, use the app ID found in the Google Play store URL.  •  Example: Google Play store URL: `https://play.google.com/store/apps/details?id=com.rovio.angrybird` •  `id` = `"com.rovio.angrybirds"`  •  For Android Apps not in the Google Play store, use the package name. |
| app_name | string | Application name. |
| app_version | string | App version number. ⏎ Example: `"3.0.2"`. |

#### Tham số `ad` (`ad` parameters)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| callback | string | Callback information to help attribute events |
| campaign_id | string | ID chiến dịch quảng cáo TikTok gắn với điểm chạm, thường được trích xuất từ URL trang đích hoặc deeplink. |
| ad_id | string | ID nhóm quảng cáo TikTok gắn với điểm chạm, thường được trích xuất từ URL trang đích hoặc deeplink. |
| creative_id | string | ID mẫu quảng cáo TikTok gắn với điểm chạm, thường được trích xuất từ URL trang đích hoặc deeplink. |
| is_retargeting | boolean | Liệu user is a retargeting user. |
| attributed | boolean | Liệu event is attributed. |
| attribution_type | string | Attribution type. |
| attribution_provider | string | Nhà cung cấp dịch vụ phân bổ (Attribution provider). |
| attribution_share | float | Điểm tỷ lệ phân bổ (Attribution share score). ⏎ Điểm số do bạn cung cấp cho mỗi chuyển đổi, đại diện cho phần công nhận mà TikTok nhận được (từ `0.0` đến `1.0`). |
| attribution_value | float | Phần giá trị chuyển đổi mà hệ thống phân bổ của bạn gán cho điểm chạm TikTok này (thường bằng giá trị chuyển đổi nhân với `attribution_share`). ⏎ Example: an order worth $120 credited 25% to a TikTok touchpoint under a linear model yields `attribution_value = 30.0` for that event. |
| attribution_model | string | Mô hình phân bổ được sử dụng để phân bổ cho sự kiện. ⏎ Examples: • `even_weight`: alias for evenly distributed credit. • `first_click`: full credit to the first click in the journey. • `first_touch`: full credit to the first touchpoint in the journey. • `last_click`: full credit to the last click in the journey. • `last_touch`: full credit to the last touchpoint in the journey. • `linear`: equal credit across every attributed touchpoint. |
| touchpoint_type | string | Loại điểm chạm TikTok nhận được ghi nhận cho sự kiện này. ⏎ Examples: • `click`: the user clicked a TikTok ad or a link that originated from a TikTok ad. • `view`: the user was served a TikTok ad impression without clicking. • `engaged_view`: the user watched a video ad for a qualifying duration (for example, 6 seconds or more) without clicking. • `engaged_click`: the user clicked and interacted with a rich media ad format (such as a Playable Ad). • `click_to_store`: the user clicked an ad that directed them straight to an app marketplace (for example, Apple App Store or Google Play). • `hybrid`: a mix of click and view signals contributed to the touchpoint. • `other`: any touchpoint that does not fit the categories above. |
| touchpoint_ts | integer | Thời điểm điểm chạm TikTok diễn ra, biểu diễn bằng Unix timestamp tính bằng giây theo múi giờ UTC+0. |
| touchpoint_url | string | URL nơi điểm chạm được ghi nhận, ví dụ như URL trang đích mà người dùng truy cập sau khi nhấp quảng cáo TikTok. |
| attribution_window_hr_click | integer | Cửa sổ phân bổ nhấp chuột (click-through attribution window), tính bằng **giờ**. ⏎ It defines the maximum interval between a TikTok click touchpoint and the conversion for which the click is still eligible to receive credit. ⏎ Examples: `1`, `24` (1 day), `168` (7 days), `720` (30 days). |
| attribution_window_hr_view | integer | Cửa sổ phân bổ lượt xem (view-through attribution window), tính bằng **giờ**. ⏎ It defines the maximum interval between a TikTok view touchpoint (impression) and the conversion for which the view is still eligible to receive credit. ⏎ Examples: `1`, `24` (1 day), `168` (7 days) |
| attribution_method | string | Phương thức kỹ thuật được sử dụng để liên kết điểm chạm với chuyển đổi. ⏎ Examples: • `pixel`: matched through the TikTok pixel on the advertiser's website. • `PPS`: matched through Post-Purchase Survey. • `deeplink`: matched through a deeplink click identifier. • `modeled`: attribution produced by a statistical or ML model rather than a deterministic match. • `SKAN`: matched through Apple's SKAdNetwork framework. • `shop`: matched through a TikTok Shop signal. |
| decline_reason | string | Lý do hệ thống của bạn từ chối gán công nhận phân bổ cho TikTok đối với sự kiện này. ⏎ Examples: • `attributed_to_other_source`: another channel received the credit. • `organic`: no paid channel received credit; treated as an organic conversion. • `outside_attribution_window`: the TikTok touchpoint fell outside the click or view window. • `invalid_event`: the event failed a partner-side validation check. • `fraud_detected`: the touchpoint was flagged as fraudulent. • `duplicate_event`: the conversion was already counted in a prior report. • `low_confidence_match`: the touchpoint-to-conversion match did not meet the confidence threshold. • `missing_touchpoint`: no eligible TikTok touchpoint was found. • `missing_click_id`: the required TikTok click identifier was absent. • `privacy_threshold_filtered`: the event was filtered out by a privacy threshold. • `unsupported_signal`: the signal type is not supported by the attribution engine. • `other`: any other reason that does not fit the categories above. |
| utm_id | string | Mã định danh duy nhất của chiến dịch tiếp thị hoặc bộ tham số UTM tạo ra điểm chạm. ⏎ It corresponds to the `utm_id` parameter in the landing URL. ⏎ Use this field to report the custom campaign identifier from your landing page URL. This is particularly useful if your internal tracking relies on custom UTM values rather than TikTok's default campaign IDs. ⏎ Example: `summer2026_launch`. |
| utm_source | string | Nguồn lưu lượng truy cập giới thiệu người dùng đến trang đích, được ghi lại trong tham số URL `utm_source`. ⏎ It typically identifies the platform or property that hosted the ad. ⏎ Example: `tiktok`. |
| utm_medium | string | Phương tiện tiếp thị phân phối lưu lượng truy cập, được ghi lại trong tham số URL `utm_medium`. ⏎ It identifies the category of the placement rather than the platform. ⏎ Examples: `cpc`, `paid_social`, `display`. |
| utm_campaign | string | Tên chiến dịch tạo ra điểm chạm, được ghi lại trong tham số URL `utm_campaign`. ⏎ It is used to attribute performance to a specific marketing initiative within the traffic source. ⏎ Example: `summer2026_launch_us`. |

## Tải trọng mẫu (Sample payload)
Dưới đây là một ví dụ về yêu cầu báo cáo một sự kiện ứng dụng `Purchase` (Mua hàng) đơn lẻ:
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/event/track/' \
--header 'Access-Token: {{ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "event_source": "app",
  "event_source_id": "{{TIKTOK_APP_ID}}",
  "data": [
    {
      "event": "InstallApp",
      "event_time": 1687758765,
      "user": {
        "phone": "{{HASHED_PHONE}}",
        "email": "{{HASHED_EMAIL}}",
        "idfa": "{{IDFA}}",
        "idfv": "{{IDFV}}",
        "gaid": "{{GAID}}",
        "att_status": "AUTHORIZED",
        "locale": "en-US"
      },
      "app": {
        "app_id": "com.test.flyingsneakers",
        "app_name": "Flying Sneakers",
        "app_version": "3.0.2"
      },
      "ad": {
        "attributed": true,
        "callback": "{{CALLBACK}}",
        "campaign_id": "1700817380525057",
        "ad_id": "1700817380806706",
        "creative_id": "1700817378256945",
        "is_retargeting": false,        
        "attribution_type": "click_through"
      },
      "properties": {
        "currency": "USD",
        "value": 200.0,
        "content_type": "product",
        "contents": [
          {
            "price": 100.0,
            "quantity": 2,
            "content_id": "12345",
            "content_name": "Fancy-AirMax2.0 Black",
            "content_category": "Shoes - Running Shoes",
            "brand": "Fancy Sneakers"
          }
        ]
      }
    }
  ]
}'
```

---

<a id="doc-1835052338764993"></a>
<!-- doc_id: 1835052338764993 -->
<!-- doc_id: 1835052338764993 -->
# Hướng dẫn thiết lập CRM (Setup guide for CRM)
> Đường dẫn: Marketing API > Ad Measurement > Guides > Events API 2.0 > Events API for CRM > Setup guide for CRM
# Bắt đầu (Get Started)
Hướng dẫn này sẽ dẫn dắt bạn qua quy trình thiết lập Events API 2.0 cho hệ thống CRM (Quản lý quan hệ khách hàng).
- Nếu muốn tạo Bộ sự kiện CRM mới, vui lòng bắt đầu từ bước 1.
- Nếu muốn sử dụng Bộ sự kiện CRM hiện có, bạn có thể bắt đầu từ bước 2.

## 1. Tạo bộ sự kiện CRM (CRM Event Set)
Tạo một Bộ sự kiện CRM bằng điểm cuối [/crm/create/](../12-api-reference/43-events-1-0-p2.md#doc-1861366342223874).

Sau khi tạo Bộ sự kiện CRM, hãy ghi lại ID bộ sự kiện CRM (giá trị này sẽ được dùng làm `event_source_id` để gửi sự kiện CRM qua Events API).

## 2. Tạo mã truy cập (Access Token)
Để xác thực các lệnh gọi Events API, bạn cần có mã truy cập (Access Token). Để tìm hiểu cách lấy mã truy cập, hãy tham khảo [Events API 2.0 > Xác thực](do-luong-quang-cao-p1.md#doc-1771101130925058).

# Chia sẻ sự kiện CRM bằng Events API
1. Tải các sự kiện CRM lên Bộ sự kiện CRM của bạn

Sau khi tạo Bộ sự kiện CRM, bạn cần tải các Sự kiện CRM lên Bộ sự kiện CRM của mình. Sự kiện được định nghĩa là các hành động mà khách hàng tiềm năng thực hiện trên hệ thống CRM của bạn để đạt được mục tiêu kinh doanh. 

Để biết chi tiết về các sự kiện CRM được hỗ trợ, hãy xem [Các sự kiện được hỗ trợ - Sự kiện CRM tiêu chuẩn](do-luong-quang-cao-p1.md#doc-1771101186666498).

2. Sử dụng định dạng tải trọng sự kiện được khuyến nghị.

**Điểm cuối (Endpoint):** https://business-api.tiktok.com/open_api/v1.3/event/track/

**Method** POST

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). ⏎ To obtain an access token, refer to [Events API 2.0 - Authentication](do-luong-quang-cao-p1.md#doc-1771101130925058). |
| Content-Type  ****(Bắt buộc)**** | string | Định dạng dữ liệu yêu cầu. ⏎ Allowed format: `application/json`. |

## Bảng tham số (Parameters) để báo cáo sự kiện CRM
Để biết định dạng giá trị của từng tham số, vui lòng tham khảo các danh sách bên dưới.

### Tham số cấp cao nhất (Top-level parameters)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| event_source  ****(Bắt buộc)**** | string | Trường này dùng để chỉ định loại sự kiện bạn đang tải lên qua Events API. ⏎ Các giá trị enum được phép:   •  `crm`: Sự kiện khách hàng tiềm năng diễn ra trên hệ thống CRM và được theo dõi bằng CRM Event Set ID. |
| event_source_id  ****(Bắt buộc)**** | string | ID nguồn sự kiện dùng để đo lường các sự kiện. ⏎ Khi `event_source` là `crm`, hãy chỉ định CRM Event Set ID qua trường này. ⏎ To obtain a CRM Event Set ID, refer to Create a CRM Event Set or the instruction below this table. |
| data  ****(Bắt buộc)**** | object[] | Mảng đối tượng chứa các sự kiện bạn muốn báo cáo. • Nếu gửi một sự kiện đơn lẻ, truyền một đối tượng trong mảng. • Nếu gom nhiều sự kiện trong một tải trọng, bạn có thể báo cáo tối đa 1.000 sự kiện trong một yêu cầu (vượt quá 1.000 sự kiện sẽ bị từ chối toàn bộ). • Để tối ưu hóa hiệu suất chiến dịch, **rất khuyến nghị gửi sự kiện theo thời gian thực (real-time, không gom batch)** ngay khi phát sinh trên máy chủ của bạn. |
| ↳ event  ****(Bắt buộc)**** | string | Tên sự kiện chuyển đổi. Có thể là Sự kiện tiêu chuẩn (Standard Event) hoặc Sự kiện tùy chỉnh (Custom Event). ⏎ To find out the supported values for Standard Events, refer to [Events API 2.0-Supported events](do-luong-quang-cao-p1.md#doc-1771101186666498). ⏎ To report a Custom Event, pass a customized name in this field. |
| ↳ event_time  ****(Bắt buộc)**** | integer | Thời điểm sự kiện diễn ra, biểu diễn bằng Unix timestamp tính bằng giây theo múi giờ UTC+0. |
| ↳ event_id **(Điều kiện)** | string | A unique value for each event. This ID can be used to match data between partner and TikTok. ⏎ We suggest a String of 32 characters, including numeric digits (0-9), uppercase letters (A-Z), and lowercase letters (a-z). |
| ↳ user | object | Thông tin về khách hàng. ⏎ Để xem danh sách các trường trong đối tượng `user`, hãy xem phần "Tham số `user`" bên dưới. |
| ↳ properties **(Điều kiện)** | object | Thông tin về sản phẩm, đơn hàng và các giá trị bổ trợ giúp tối ưu hiệu suất quảng cáo. ⏎ Để xem danh sách các trường trong đối tượng `properties`, hãy xem phần "Tham số `properties`" bên dưới. |
| ↳ lead | object | Information about the lead. ⏎ To view the list of fields included in the `lead` object, refer to the "`lead` parameters" section below. |

- `event_source_id` cho CRM là ID của Bộ sự kiện CRM mà bạn muốn gửi sự kiện tới. Bạn có thể xác định ID này bằng cách vào **Công cụ (Tools)** > **Sự kiện (Events)** > nút **Nguồn dữ liệu (Data sources)**. ID của Bộ sự kiện CRM là `7446580941998374913` trong ví dụ bên dưới.

#### Tham số `user` (`user` parameters)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| email | string ⏎ or string[] | **Bắt buộc băm SHA-256.** ⏎ Địa chỉ email của khách hàng. ⏎ Follow the instructions below to obtain a valid value:  • **Trim** any leading and trailing spaces of each email before hashing.  • **Lowercase** all characters before hashing. • **Hash** the normalized email values using SHA-256.**Example**:  •  Original: " ALICE_abc@gmail.com "  •  Normalized: "alice_abc@gmail.com" (leading and trailing spaces trimmed and lowercased)  •  SHA-256 hashed: "848a771458438fc2ec420560d769fb9b9b86851ee338ec56517baabd79d3bb4f" |
| phone | string ⏎ or string[] | **Bắt buộc băm SHA-256.** ⏎ Số điện thoại của khách hàng. ⏎ Follow the instructions below to obtain a valid value:  • **Normalize** the phone number to [E.164 format](https://www.twilio.com/docs/glossary/what-e164) (for example, "+12133734253"). We recommend using [https://github.com/catamphetamine/libphonenumber-js](https://github.com/catamphetamine/libphonenumber-js) for E.164 parsing.  • **Country code** must be included and prefixed with the `+` sign, without any parentheses or leading `0`s. For example, a US phone number should be prefixed with the `+1` country code. •  **No spaces, letters or symbols** except the `+` for the country code are included.  • **SHA-256 hash** the phone number after normalizing. **Example**:  •  Original: "(+1)2133734253" •  Normalized to E.164 format: "+12133734253" •  SHA256 hashed: "9f7ec22d72092cd3c0b58726ed9c2d91b92e51a3f29837508fb2948bb22dd2fd" |

#### Tham số `properties` (`properties` parameters)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| content_ids | string[] | ID duy nhất hoặc mảng nhiều ID của các sản phẩm hoặc nội dung. ⏎ Example: `["987", "654"]`. ⏎ Khuyến nghị sử dụng `sku_id` hoặc `item_group_id` khớp với `sku_id` hoặc `item_group_id` đã thiết lập trong danh mục sản phẩm (catalog). ⏎ Trường này là bắt buộc đối với Quảng cáo video mua sắm (VSA). |
| contents | object[] | Các sản phẩm liên quan trong một sự kiện kèm theo thông tin chi tiết. ⏎ Để xem danh sách các trường trong đối tượng contents, hãy xem phần "Tham số `contents`" bên dưới. |
| content_type | string | Loại nội dung trong sự kiện. ⏎ Các giá trị enum hỗ trợ: `product`, `product_group`.    • Khi `content_id` trong tham số `contents` là `sku_id`, đặt trường này là `product`.   • Khi `content_id` trong tham số `contents` là `item_group_id`, đặt trường này là `product_group`. |
| currency | string | **Khuyến nghị cho các sự kiện liên quan đến doanh thu.** ⏎ Mã tiền tệ chuẩn ISO 4217. ⏎ Examples: `EUR`, `USD`, `JPY`. ⏎ **List of currencies currently supported**: `AED`, `ARS`, `AUD`, `BDT`, `BHD`, `BIF`, `BOB`, `BRL`, `CAD`, `CHF`, `CLP`, `CNY`, `COP`, `CRC`, `CZK`, `DKK`, `DZD`, `EGP`, `EUR`, `GBP`, `GTQ`, `HKD`, `HNL`, `HUF`, `IDR`, `ILS`, `INR`, `ISK`, `JPY`, `KES`, `KHR`, `KRW`, `KWD`, `KZT`, `MAD`, `MOP`, `MXN`, `MYR`, `NGN`, `NIO`, `NOK`, `NZD`, `OMR`, `PEN`, `PHP`, `PHP`, `PKR`, `PLN`, `PYG`, `QAR`, `RON`, `RUB`, `SAR`, `SEK`, `SGD`, `THB`, `TRY`, `TWD`, `UAH`, `USD`, `VES`, `VND`, `ZAR` . |
| value | float | **Khuyến nghị cho các sự kiện liên quan đến doanh thu.** ⏎ Tổng giá trị của đơn hàng hoặc các mặt hàng được bán. ⏎ Giá trị phải luôn được định dạng là số nguyên hoặc số thập phân (ví dụ: `10.00`) bất kể vị trí, loại tiền tệ hay các yếu tố khác. Không chứa ký hiệu tiền tệ, ký tự đặc biệt, chữ cái hoặc dấu phẩy. ⏎ **Lưu ý**: `price` chỉ định giá cho một mặt hàng đơn lẻ, còn `value` chỉ định tổng giá trị đơn hàng. |
| num_items | integer | Số lượng các mặt hàng. |
| search_string | string | Chuỗi tìm kiếm do người dùng nhập. |
| description | string | Mô tả của mặt hàng hoặc trang web. |
| order_id | string | Mã định danh đơn hàng (Order ID). |
| shop_id | string | Mã định danh cửa hàng (Shop ID). |

##### Tham số `contents` (`contents` parameters)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| price | float | Đơn giá của một mặt hàng. ⏎ **Lưu ý**: `price` chỉ định giá cho một mặt hàng đơn lẻ, còn `value` chỉ định tổng giá trị của cả đơn hàng. ⏎ Example: `10`, `10.5`. |
| content_id | string | ID duy nhất của sản phẩm hoặc nội dung. ⏎ Khuyến nghị sử dụng `sku_id` hoặc `item_group_id` nếu bạn có sẵn. ID phải khớp với `sku_id` hoặc `item_group_id` đã thiết lập trong danh mục sản phẩm. |
| content_category | string | Danh mục của trang hoặc sản phẩm. |
| content_name | string | Tên của trang hoặc sản phẩm. |
| brand | string | Tên thương hiệu của mặt hàng sản phẩm. |

#### Tham số `lead` (`lead` parameters)
Sử dụng các tham số `lead` để chia sẻ thông tin về khách hàng tiềm năng trong hệ thống CRM với Events API 2.0. Tham số `lead` chỉ nên được sử dụng khi báo cáo sự kiện CRM (`event_source` = `crm`).

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| lead_id | string | **Required for CRM events**. ⏎ ID of TikTok leads. ⏎ Every lead will have its `lead_id` when exported from TikTok. ⏎ To obtain the ID of a lead, download the lead by using the endpoints [/page/lead/task/](../12-api-reference/48-leads.md#doc-1739052936772610) and [/page/lead/task/download/](../12-api-reference/48-leads.md#doc-1739053563877378), or export the lead from TikTok Leads Center, the first-party CRM platform located within TikTok Ads Manager. |
| lead_event_source | string | Lead event source. ⏎ You can set this field to the name of your CRM system, such as HubSpot or Salesforce. |

Lưu ý rằng một phương án thay thế khác để tải Sự kiện CRM lên Bộ sự kiện CRM là tải **tệp (file)** lên trong Trình quản lý sự kiện.

## Tải trọng mẫu (Sample payload)

```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/event/track/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "event_source": "crm",
  "event_source_id": "{{CRM-Event-Set-ID}}",
  "data": [
    {
      "event_id":"1616318632825_357",
      "event": "Purchase",
      "event_time": 1684574395,
      "user": {
        "email": "848a771458438fc2ec420560d769fb9b9b86851ee338ec56517baabd79d3bb4f",
        "phone": "2f9d2b4df907e5c9a7b3434351b55700167b998a83dc479b825096486ffcf4ea"
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
      },
      "lead": {
        "lead_id": "71247185198338",
        "lead_event_source": "YourCRM"
      }
    }
  ]
}'
```

# Xác minh thiết lập sự kiện CRM
Để biết các phương pháp tối ưu khi xác minh thiết lập Events API, hãy xem [Xác minh thiết lập Events API](do-luong-quang-cao-p1.md#doc-1835052369704961).

# Quản lý các bộ sự kiện CRM *(Không bắt buộc)* 
Bạn có thể quản lý các Bộ sự kiện CRM theo các cách sau:
- Lấy danh sách các Bộ sự kiện CRM thuộc tài khoản quảng cáo qua điểm cuối [/crm/list/](../12-api-reference/43-events-1-0-p2.md#doc-1780896521680898).

---

<a id="doc-1771101151059969"></a>
<!-- doc_id: 1771101151059969 -->
<!-- doc_id: 1771101151059969 -->
# Bảng tham số (Parameters)
> Đường dẫn: Marketing API > Ad Measurement > Guides > Events API 2.0 > Parameters
# Các tham số cấp cao nhất (Top-level Parameters)
Tất cả các tham số cấp cao nhất được gắn nhãn "Bắt buộc" đều bắt buộc đối với tất cả các nguồn sự kiện (hệ thống web, app, offline hoặc CRM).

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| event_source  ****(Bắt buộc)**** | string | Trường này dùng để chỉ định loại sự kiện bạn đang tải lên qua Events API. ⏎ Các giá trị enum hỗ trợ: • `web`: Sự kiện diễn ra trên website và được đo lường bằng Pixel Code. • `app`: Sự kiện diễn ra trên ứng dụng và được đo lường bằng TikTok App ID. • `offline`: Chuyển đổi diễn ra tại cửa hàng thực tế và được đo lường bằng Offline Event Set ID. • `crm`: Sự kiện lead diễn ra trong hệ thống CRM và được đo lường bằng CRM Event Set ID. ⏎ **Note**: Reporting App Events using Events API 2.0 is currently an allowlist-only feature. If you would like to access it, please contact your TikTok representative. |
| event_source_id  ****(Bắt buộc)**** | string | ID nguồn sự kiện dùng để đo lường các sự kiện.   • Khi `event_source` là `web`, hãy chỉ định Pixel Code qua trường này. ⏎ To obtain a Pixel Code, refer to [FAQs - Where can I find the pixel_code?](do-luong-quang-cao-p1.md#doc-1771101001228290).  • Khi `event_source` là `offline`, hãy chỉ định Offline Event Set ID qua trường này. ⏎ To obtain an Offline Event Set ID, refer to [Setup Guide for Offline](do-luong-quang-cao-tom-tat.md#doc-1771101027431425). • Khi `event_source` là `app`, hãy chỉ định TikTok App ID qua trường này. ⏎ To obtain a TikTok App ID, refer to [Setup Guide for App](do-luong-quang-cao-tom-tat.md#doc-1771101111730178). • Khi `event_source` là `crm`, hãy chỉ định CRM Event Set ID qua trường này. ⏎ To obtain a CRM Event Set ID, use [/crm/list/](../12-api-reference/43-events-1-0-p2.md#doc-1780896521680898). |
| data  ****(Bắt buộc)**** | object[] | Mảng đối tượng chứa các sự kiện bạn muốn báo cáo. • Nếu gửi một sự kiện đơn lẻ, truyền một đối tượng trong mảng. • Nếu gom nhiều sự kiện trong một tải trọng, bạn có thể báo cáo tối đa 1.000 sự kiện trong một yêu cầu (vượt quá 1.000 sự kiện sẽ bị từ chối toàn bộ). • Để tối ưu hóa hiệu suất chiến dịch, **rất khuyến nghị gửi sự kiện theo thời gian thực (real-time, không gom batch)** ngay khi phát sinh trên máy chủ của bạn. |
| ↳ event  ****(Bắt buộc)**** | string | **For web, app, offline, and CRM events.** ⏎ Tên sự kiện chuyển đổi. ⏎ • Với sự kiện web và app: Có thể là Sự kiện tiêu chuẩn hoặc Tùy chỉnh. • Với sự kiện offline: Chỉ hỗ trợ Sự kiện tiêu chuẩn. • Với sự kiện CRM: Chỉ hỗ trợ Sự kiện tùy chỉnh. To find out the supported values for Standard Events, refer to [Events API 2.0-Supported events](do-luong-quang-cao-p1.md#doc-1771101186666498). ⏎ To report a Custom Web Event or Custom App Event, pass a customized name in this field. ⏎ Không sử dụng các từ ngữ nhạy cảm trong tên Sự kiện tùy chỉnh; nếu không, bạn sẽ chịu trách nhiệm cho mọi hậu quả phát sinh. |
| ↳ event_time  ****(Bắt buộc)**** | integer | **For web, app, offline, and CRM events.** ⏎ Thời điểm sự kiện diễn ra, biểu diễn bằng Unix timestamp tính bằng giây theo múi giờ UTC+0. |
| ↳ event_id **(Điều kiện)** | string | **For web, offline, and CRM events.** ⏎ Bắt buộc trong các trường hợp: • Bạn gửi sự kiện web (`event_source` = `web`) từ cả TikTok pixel trình duyệt và Events API. • Bạn gửi sự kiện CRM (`event_source` = `crm`) từ cả Events API và tệp CSV trên Trình quản lý sự kiện.  Mã ID dùng để định danh duy nhất một sự kiện. Có thể băm hoặc không băm. ⏎ TikTok sử dụng bộ ba `event_source_id`, `event_id` và `event` để khử trùng lặp cùng một sự kiện gửi nhiều lần từ một kênh hoặc giữa nhiều kênh (chẳng hạn giữa browser pixel và Events API). ⏎ For more information on event deduplication and how to complete the setup, refer to [Events API 2.0 - Event Deduplication](do-luong-quang-cao-p1.md#doc-1771100965992450). |
| ↳ user | object | **For web, app, offline, and CRM events.** ⏎ Thông tin về khách hàng. ⏎ Để xem danh sách các trường trong đối tượng `user`, hãy xem phần "Tham số `user`" bên dưới. |
| ↳ properties | object | **For web, app, offline, and CRM events.** ⏎ Thông tin về sản phẩm, đơn hàng và các giá trị bổ trợ giúp tối ưu hiệu suất quảng cáo. ⏎ Để xem danh sách các trường trong đối tượng `properties`, hãy xem phần "Tham số `properties`" bên dưới. |
| ↳ page**(Điều kiện)** | object | **Required for web events.** ⏎ Thông tin về trang web. ⏎ Để xem danh sách các trường trong đối tượng `page`, hãy xem phần "Tham số `page`" bên dưới. |
| ↳ app**(Điều kiện)** | object | **Required for app events.** ⏎ Thông tin về ứng dụng di động. ⏎ Để xem danh sách các trường trong đối tượng `app`, hãy xem phần "Tham số `app`" bên dưới. ⏎ **Note**: Reporting App Events using Events API 2.0 is currently an allowlist-only feature. If you would like to access it, please contact your TikTok representative. |
| ↳ ad | object | **Only for app and web events.** ⏎ Thông tin về quảng cáo. ⏎ Để xem danh sách các trường trong đối tượng `ad`, hãy xem phần "Tham số `ad`" bên dưới. |
| ↳ limited_data_use | boolean | **For web and app events.** ⏎ Để tìm hiểu thêm về tính năng Sử dụng dữ liệu hạn chế, hãy xem [Events API 2.0 - Sử dụng dữ liệu hạn chế](do-luong-quang-cao-p1.md#doc-1771101204435970). |
| ↳ lead **(Điều kiện)** | object | **Required for CRM events. ** ⏎ Thông tin về khách hàng tiềm năng (lead). ⏎ Để xem danh sách các trường trong đối tượng `lead`, hãy xem phần "Tham số `lead`" bên dưới. |

## Tham số `user` (`user` parameters)
Events API 2.0 sử dụng thông tin khách hàng như TikTok Click ID, Đối sánh nâng cao (Advanced Matching), và các tín hiệu bổ sung như địa chỉ IP cùng User Agent để khớp các sự kiện người truy cập với người dùng TikTok. Khi khớp thành công, dữ liệu chia sẻ có thể dùng để xây dựng tệp đối tượng nhắm mục tiêu, cung cấp tín hiệu cho thuật toán tối ưu hóa và đo lường kết quả chiến dịch tốt hơn.

Để gia tăng độ chính xác của mô hình nhắm mục tiêu và tối ưu hóa, chúng tôi rất khuyến nghị bạn gửi kèm nhiều loại dữ liệu so khớp. Bạn có thể sử dụng Đối sánh nâng cao (Advanced Matching), TikTok Click ID (`ttclid`) và Cookie để phân bổ chuyển đổi.

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết | Examples |
|---|---|---|---|
| ttclid | string | **For web events only.** ⏎ TikTok Click ID, a data connection parameter appended to a landing page URL whenever a user clicks on an ad on TikTok. ⏎ The `ttclid` valid period is the same as your CTA window setting in [Attribution Manager](https://ads.tiktok.com/help/article/attribution-manager?redirected=1). ⏎ For more information on sending TikTok Click IDs, refer to [Events API 2.0 - Send TikTok Click ID (`ttclid`)](do-luong-quang-cao-p1.md#doc-1771100879787009). |  |
| email | string ⏎ or string[] | ** For web, app, offline, and CRM events.** ⏎ **Bắt buộc băm SHA-256.** ⏎ Địa chỉ email của khách hàng. ⏎ Follow the instructions below to obtain a valid value:  • **Trim** any leading and trailing spaces of each email before hashing.  • **Lowercase** all characters before hashing. • **Hash** the normalized email values using SHA-256.**Example**:  •  Original: " ALICE_abc@gmail.com "  •  Normalized: "alice_abc@gmail.com" (leading and trailing spaces trimmed and lowercased)  •  SHA-256 hashed: "848a771458438fc2ec420560d769fb9b9b86851ee338ec56517baabd79d3bb4f" | `"848a771458438fc2ec420560d769fb9b9b86851ee338ec56517baabd79d3bb4f"` |
| phone | string ⏎ or string[] | **For web, app, offline, and CRM events.** ⏎ **Bắt buộc băm SHA-256.** ⏎ Số điện thoại của khách hàng. ⏎ Follow the instructions below to obtain a valid value:  • **Normalize** the phone number to [E.164 format](https://www.twilio.com/docs/glossary/what-e164) (for example, "+12133734253"). We recommend using [https://github.com/catamphetamine/libphonenumber-js](https://github.com/catamphetamine/libphonenumber-js) for E.164 parsing.  • **Country code** must be included and prefixed with the `+` sign, without any parentheses or leading `0`s. For example, a US phone number should be prefixed with the `+1` country code. •  **No spaces, letters or symbols** except the `+` for the country code are included.  • **SHA-256 hash** the phone number after normalizing. **Example**:  •  Original: "(+1)2133734253" •  Normalized to E.164 format: "+12133734253" •  SHA256 hashed: "9f7ec22d72092cd3c0b58726ed9c2d91b92e51a3f29837508fb2948bb22dd2fd" | `"9f7ec22d72092cd3c0b58726ed9c2d91b92e51a3f29837508fb2948bb22dd2fd"` |
| external_id | string ⏎ or string[] | **For web and CRM events only.** ⏎ **Bắt buộc băm SHA-256.** ⏎ External ID, mã định danh duy nhất từ phía nhà quảng cáo như mã thành viên, ID người dùng và cookie ngoài. To learn more about the `external_id` parameter, refer to [Events API 2.0 - Set up External ID](do-luong-quang-cao-p1.md#doc-1771100952291330). ⏎ **Example**:  •  Original: "user_123" •  SHA-256 hashed: "80fba0ae1c48e3978e43e4efc365e14e12ea0c830ba8ba5b9a2dafc7e3f2ab8b" | `"80fba0ae1c48e3978e43e4efc365e14e12ea0c830ba8ba5b9a2dafc7e3f2ab8b"` |
| ttp | string | **For web events only.** ⏎ Cookie ID. ⏎ Nếu bạn cũng sử dụng Pixel SDK và đã bật cookie, Pixel SDK sẽ tự động lưu mã định danh duy nhất vào cookie `_ttp`. Giá trị của `_ttp` được dùng để khớp các sự kiện người truy cập với quảng cáo TikTok. Bạn có thể trích xuất giá trị `_ttp` và gắn vào đây. ⏎ To learn more about the `ttp` parameter, refer to [Events API 2.0 - Send TikTok Cookie (`_ttp`)](https://ads.tiktok.com/marketing_api/docs?id= 1771100936446977). |  |
| ip | string | **For web and app events only.** ⏎ Địa chỉ **IP công cộng (public IP)** không băm của thiết bị người dùng. ⏎ Để tăng xác suất so khớp sự kiện với quảng cáo TikTok, khuyến nghị gửi cả `ip` và `user_agent`. Hỗ trợ cả IPv4 và IPv6 (dạng đầy đủ hoặc rút gọn). ⏎ For example: • Full format: **2001:0db8:1111:000a:00b0:0000:0000:0200** • Compressed format: **2001:db8:1111:a:b0::200** | `"203.0.113.1"` ⏎ `"2001:0db8:85a3:0000:0000:8a2e:0370:7334"` |
| user_agent | string | **For web and app events only.** ⏎ Chuỗi User Agent không băm từ thiết bị người dùng. ⏎ Để tăng xác suất so khớp sự kiện với quảng cáo TikTok, khuyến nghị gửi cả `ip` và `user_agent`. | `"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604"` |
| first_name | string | **For web events only. ** ⏎ **SHA-256 hashing is required.** ⏎ The first name of the customer. ⏎ The name should be in lowercase without any punctuation. Special characters are allowed. ⏎ **Example 1: **   • Original: " Jane " • Normalized: "jane" (leading and trailing spaces trimmed and lowercased) • SHA-256 hashed: "81f8f6dde88365f3928796ec7aa53f72820b06db8664f5fe76a7eb13e24546a2" ⏎ **Example 2: **  • Original: "민준"  • SHA-256 hashed:   "905d70b1f90f9cbfa6dc23ce36d81c8a385849941c15490f743822b842fee426" | `"81f8f6dde88365f3928796ec7aa53f72820b06db8664f5fe76a7eb13e24546a2"` |
| last_name | string | **For web events only. ** ⏎ **SHA-256 hashing is required.** ⏎ The last name of the customer. ⏎ The name should be in lowercase without any punctuation. Special characters are allowed. ⏎ **Example: ** See `first_name` examples. | `"81f8f6dde88365f3928796ec7aa53f72820b06db8664f5fe76a7eb13e24546a2"` |
| city | string | **For web events only. ** ⏎ City of the customer's address. ⏎ The city should be in lowercase without any punctuation, special characters, or spaces. | `"seattle"`, `"newyork"` |
| state | string | **For web events only. ** ⏎ State or province of the customer's address. ⏎ • US: Use the [two-letter ANSI (American National Standards Institute) code](https://en.wikipedia.org/wiki/Federal_Information_Processing_Standard_state_code) in lowercase. • Non-US: Normalize states outside the US in lowercase without any punctuation, special characters, or spaces. | • US: `"ca"` (California) • Non-US: `"britishcolumbia"` (British Columbia (Canada)) |
| country | string | **For web events only. ** ⏎ Country of the customer's address. ⏎ Use the lowercase, two-letter [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) codes. | • `"us"`: the United States • `"sg"`: Singapore |
| zip_code | string | **For web events only. ** ⏎ **SHA-256 hashing is required.** ⏎ Zip code or postal code of customer’s address. ⏎ The code should be in lowercase without any spaces or dashes. ⏎ • For US zip codes, use only the first 5 digits.  •  For non-US zip codes or postal codes, normalize the codes in lowercase and trim the leading and trailing spaces. **Example 1: **  • Original: "95110" (US zip code)  • SHA-256 hashed:   "383f7fffd99f3b1c3066086bcf991eae7ad543589d12bd792ecb6dc8b5acebc1" ⏎ **Example 2: ** • Original: "M5V 3L9" (Canadian postal code) • Normalized: "m5v3l9"  • SHA-256 hashed:   "5c850751d57c5d887fe7807d3da801efe7e8faa1f105ea36cdcd913dd32a41c7" | `"383f7fffd99f3b1c3066086bcf991eae7ad543589d12bd792ecb6dc8b5acebc1"` |
| idfa | string | ** The iOS IDFA for app events only. ** ⏎ For iOS 14 and above, ensure that IDFA data collection follows [Apple’s policies](https://developer.apple.com/app-store/user-privacy-and-data-use/). Both raw and SHA-256 IDFAs are accepted: • For raw IDFAs, all characters must be **UPPERCASE**.  • For SHA-256 IDFAs, all characters must be **lowercase**, and any **leading/trailing spaces** must be **trimmed** before hashing. | • Raw IDFA: `"EA7583CD-A667-48BC-B806-42ECB2B48606"` • SHA-256 IDFA: `"70574fa9c8f498a7b2e5c8712b1126de7b1406fd02fdc591821c5bd33092fd1c"` |
| idfv | string | The iOS IDFV ** for app events only**. |  |
| gaid | string | The GAID (Google Advertising ID)** for app events only**. ⏎ Both raw and SHA-256 GAIDs are accepted. ⏎ For both raw and SHA-256 GAIDs: • All characters must be **lowercase**. • **Leading/trailing spaces** must be **trimmed** before hashing | • Raw GAID: `"aaaaaa-2222-1111-8787-809e92233ba0"` •  SHA-256 GAID: `"0ebad966881e1eebffe69b3abf624631cf83ec9bf8cb3ce134c7c75c6d8ee7fc"` |
| locale | string | **For web and app events only.** ⏎ Mã định danh ngôn ngữ theo chuẩn BCP 47. ⏎ Để tham khảo, xem [Mã tiêu chuẩn IETF BCP 47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt). | `"en-US"` ⏎ `"zh-CN"` |
| att_status | string | **For app events only.** ⏎ Liệu user has authorized your mobile app to access app-related data for measuring the user or the device. This is an iOS only field. ⏎ Các giá trị enum hỗ trợ: • `AUTHORIZED`: The user has authorized access to app-related data that can be used for measuring the user or the device.  •  `DENIED`: The user has not agreed to authorize your mobile app to access app-related data for measuring the user or the device via [Apple's AppTrackingTransparency framework](https://developer.apple.com/documentation/apptrackingtransparency). ⏎ If this field is set to `DENIED`, TikTok will not use the PII data (for instance, user email address or phone number) in this App Event for user-level matching. • `NOT_DETERMINED`: The user has not yet received an authorization request to authorize access to app-related data that can be used for measuring the user or the device. • `RESTRICTED`: The authorization to access app-related data is restricted. •  `NOT_APPLICABLE`: The iOS version is below 14 or the device is running Android. | `"AUTHORIZED"` |

## Tham số `properties` (`properties` parameters)
Thông tin về đơn hàng và sản phẩm liên quan đến sự kiện. Việc cung cấp thông tin này cho phép TikTok tối ưu hóa hiệu quả quảng cáo của bạn.

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết | Bắt buộc để báo cáo ROAS hoặc VBO | Bắt buộc cho Video Shopping Ads (VSA) |
|---|---|---|---|---|
| content_ids | string[] | ID duy nhất hoặc mảng nhiều ID của các sản phẩm hoặc nội dung. ⏎ Example: `["987", "654"]`. ⏎ Khuyến nghị sử dụng `sku_id` hoặc `item_group_id` khớp với `sku_id` hoặc `item_group_id` đã thiết lập trong danh mục sản phẩm (catalog). ⏎ Trường này là bắt buộc đối với Quảng cáo video mua sắm (VSA). |  | ✅ |
| contents **(Điều kiện)** | object[] | Các sản phẩm liên quan trong một sự kiện kèm theo thông tin chi tiết. ⏎ Để xem danh sách các trường trong đối tượng contents, hãy xem phần "Tham số `contents`" bên dưới. |  | ✅ |
| content_type**(Điều kiện)** | string | Loại nội dung trong sự kiện. ⏎ Các giá trị enum hỗ trợ: `product`, `product_group`.    • Khi `content_id` trong tham số `contents` là `sku_id`, đặt trường này là `product`.   • Khi `content_id` trong tham số `contents` là `item_group_id`, đặt trường này là `product_group`. |  | ✅ |
| currency**(Điều kiện)** | string | **Khuyến nghị cho các sự kiện liên quan đến doanh thu.** ⏎ Mã tiền tệ chuẩn ISO 4217. ⏎ Examples: `EUR`, `USD`, `JPY`. ⏎ **List of currencies currently supported**: `AED`, `ARS`, `AUD`, `BDT`, `BHD`, `BIF`, `BOB`, `BRL`, `CAD`, `CHF`, `CLP`, `CNY`, `COP`, `CRC`, `CZK`, `DKK`, `DZD`, `EGP`, `EUR`, `GBP`, `GTQ`, `HKD`, `HNL`, `HUF`, `IDR`, `ILS`, `INR`, `ISK`, `JPY`, `KES`, `KHR`, `KRW`, `KWD`, `KZT`, `MAD`, `MOP`, `MXN`, `MYR`, `NGN`, `NIO`, `NOK`, `NZD`, `OMR`, `PEN`, `PHP`, `PHP`, `PKR`, `PLN`, `PYG`, `QAR`, `RON`, `RUB`, `SAR`, `SEK`, `SGD`, `THB`, `TRY`, `TWD`, `UAH`, `USD`, `VES`, `VND`, `ZAR` . | ✅ |  |
| value **(Điều kiện)** | float | **Khuyến nghị cho các sự kiện liên quan đến doanh thu.** ⏎ Tổng giá trị của đơn hàng hoặc các mặt hàng được bán. ⏎ Giá trị phải luôn được định dạng là số nguyên hoặc số thập phân (ví dụ: `10.00`) bất kể vị trí, loại tiền tệ hay các yếu tố khác. Không chứa ký hiệu tiền tệ, ký tự đặc biệt, chữ cái hoặc dấu phẩy. ⏎ **Lưu ý**: `price` chỉ định giá cho một mặt hàng đơn lẻ, còn `value` chỉ định tổng giá trị đơn hàng. | ✅ |  |
| num_items | integer | Số lượng các mặt hàng. |  |  |
| search_string | string | Chuỗi tìm kiếm do người dùng nhập. |  |  |
| description | string | Mô tả của mặt hàng hoặc trang web. |  |  |
| order_id | string | Mã định danh đơn hàng (Order ID). |  |  |
| shop_id | string | Mã định danh cửa hàng (Shop ID). |  |  |
| customer_type | string | **Only for app and web events.** ⏎ Nhãn phân loại phân khúc khách hàng liên quan đến sự kiện chuyển đổi. ⏎ Các giá trị enum hỗ trợ: • `new`: Khách hàng mới. • `returning`: Khách hàng quay lại. |  |  |

### Tham số `contents` (`contents` parameters)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết | Required for reporting ROAS or for VBO | Required for VSA |
|---|---|---|---|---|
| price | float | Đơn giá của một mặt hàng. ⏎ **Lưu ý**: `price` chỉ định giá cho một mặt hàng đơn lẻ, còn `value` chỉ định tổng giá trị của cả đơn hàng. ⏎ Example: `10`, `10.5`. |  |  |
| content_id **(Điều kiện)** | string | ID duy nhất của sản phẩm hoặc nội dung. ⏎ Khuyến nghị sử dụng `sku_id` hoặc `item_group_id` nếu bạn có sẵn. ID phải khớp với `sku_id` hoặc `item_group_id` đã thiết lập trong danh mục sản phẩm. |  | ✅ |
| content_category | string | Danh mục của trang hoặc sản phẩm. |  |  |
| content_name | string | Tên của trang hoặc sản phẩm. |  |  |
| brand | string | Tên thương hiệu của mặt hàng sản phẩm. |  |  |

## Tham số `page` (`page` parameters)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết | Example |
|---|---|---|---|
| url  ****(Bắt buộc)**** | string | URL trình duyệt nơi sự kiện diễn ra, ví dụ giá trị của `location.href` trong JavaScript phía máy khách. ⏎ Khuyến nghị sử dụng URL đầy đủ, bao gồm toàn bộ tham số truy vấn. | `"http://demo.mywebsite.com/purchase?v=helloworld"` |
| referrer | string | URL giới thiệu (referrer URL). ⏎ For example, [document.referrer ](https://developer.mozilla.org/en-US/docs/Web/API/Document/referrer) in the client side Javascript, or the server side [Referer http header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referer). ⏎ It is recommended to use the full URL, including all URL parameters. | `"http://demo.mywebsite.com/purchase"` |

## Tham số `app` (`app` parameters)
Sử dụng các tham số `app` để chia sẻ thông tin về ứng dụng của nhà quảng cáo với Events API 2.0. Các tham số `app` chỉ nên được sử dụng khi báo cáo sự kiện Ứng dụng (`event_source` = `app`).
> **Note:** 
> **Lưu ý:** Tính năng báo cáo sự kiện ứng dụng bằng Events API 2.0 hiện chỉ dành cho danh sách cho phép (allowlist). Nếu muốn truy cập, vui lòng liên hệ với đại diện TikTok của bạn.

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| app_id **(Điều kiện)** | string | **Required for app events. ** ⏎ Mobile App ID.  •  For iOS Apps, use the app ID found in the App Store URL  •  Example: Apple Store URL: `https://apps.apple.com/us/app/angry-birds/id343200656` • `id` = `"343200656"` •  For Android Apps in the Google Play store, use the app ID found in the Google Play store URL.  •  Example: Google Play store URL: `https://play.google.com/store/apps/details?id=com.rovio.angrybird` •  `id` = `"com.rovio.angrybirds"`  •  For Android Apps not in the Google Play store, use the package name. |
| app_name | string | Application name. |
| app_version | string | App version number. ⏎ Example: `"3.0.2"`. |

## Tham số `ad` (`ad` parameters)
Sử dụng các tham số `ad` để chia sẻ thông tin về ứng dụng hoặc trang web của nhà quảng cáo với Events API 2.0. Các tham số `ad` chỉ nên được sử dụng khi báo cáo Sự kiện ứng dụng (App Events) hoặc Sự kiện web (Web Events) (`event_source` = `app` hoặc `web`).

> **Lưu ý:** Tính năng báo cáo sự kiện ứng dụng bằng Events API 2.0 hiện chỉ dành cho danh sách cho phép (allowlist). Nếu muốn truy cập, vui lòng liên hệ với đại diện TikTok của bạn.

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| callback | string | **For app events only.** ⏎ Callback information to help attribute events |
| campaign_id | string | **For app and web events only.** ⏎ ID chiến dịch quảng cáo TikTok gắn với điểm chạm, thường được trích xuất từ URL trang đích hoặc deeplink. |
| ad_id | string | **For app and web events only.** ⏎ ID nhóm quảng cáo TikTok gắn với điểm chạm, thường được trích xuất từ URL trang đích hoặc deeplink. |
| creative_id | string | **For app and web events only.** ⏎ ID mẫu quảng cáo TikTok gắn với điểm chạm, thường được trích xuất từ URL trang đích hoặc deeplink. |
| is_retargeting | boolean | **For app  events only.** ⏎ Liệu user is a retargeting user. |
| attributed | boolean | **For app events only.** ⏎ Liệu event is attributed. |
| attribution_type | string | **For app events only.** ⏎ Attribution type. |
| attribution_provider | string | **For app and web events only.** ⏎ Nhà cung cấp dịch vụ phân bổ (Attribution provider). |
| attribution_share | float | **For app and web events only.** ⏎ Điểm tỷ lệ phân bổ (Attribution share score). ⏎ Điểm số do bạn cung cấp cho mỗi chuyển đổi, đại diện cho phần công nhận mà TikTok nhận được (từ `0.0` đến `1.0`). |
| attribution_value | float | **For app and web events only.** ⏎ Phần giá trị chuyển đổi mà hệ thống phân bổ của bạn gán cho điểm chạm TikTok này (thường bằng giá trị chuyển đổi nhân với `attribution_share`). ⏎ Example: an order worth $120 credited 25% to a TikTok touchpoint under a linear model yields `attribution_value = 30.0` for that event. |
| attribution_model | string | **For app and web events only.** ⏎ Mô hình phân bổ được sử dụng để phân bổ cho sự kiện. ⏎ Examples: • `even_weight`: alias for evenly distributed credit. • `first_click`: full credit to the first click in the journey. • `first_touch`: full credit to the first touchpoint in the journey. • `last_click`: full credit to the last click in the journey. • `last_touch`: full credit to the last touchpoint in the journey. • `linear`: equal credit across every attributed touchpoint. |
| touchpoint_type | string | **For app and web events only.** ⏎ Loại điểm chạm TikTok nhận được ghi nhận cho sự kiện này. ⏎ Examples: • `click`: the user clicked a TikTok ad or a link that originated from a TikTok ad. • `view`: the user was served a TikTok ad impression without clicking. • `engaged_view`: the user watched a video ad for a qualifying duration (for example, 6 seconds or more) without clicking. • `engaged_click`: the user clicked and interacted with a rich media ad format (such as a Playable Ad). • `click_to_store`: the user clicked an ad that directed them straight to an app marketplace (for example, Apple App Store or Google Play). • `hybrid`: a mix of click and view signals contributed to the touchpoint. • `other`: any touchpoint that does not fit the categories above. |
| touchpoint_ts | integer | **For app and web events only.** ⏎ Thời điểm điểm chạm TikTok diễn ra, biểu diễn bằng Unix timestamp tính bằng giây theo múi giờ UTC+0. |
| touchpoint_url | string | **For app and web events only.** ⏎ URL nơi điểm chạm được ghi nhận, ví dụ như URL trang đích mà người dùng truy cập sau khi nhấp quảng cáo TikTok. |
| attribution_window_hr_click | integer | **For app and web events only.** ⏎ Cửa sổ phân bổ nhấp chuột (click-through attribution window), tính bằng **giờ**. ⏎ It defines the maximum interval between a TikTok click touchpoint and the conversion for which the click is still eligible to receive credit. ⏎ Examples: `1`, `24` (1 day), `168` (7 days), `720` (30 days). |
| attribution_window_hr_view | integer | **For app and web events only.** ⏎ Cửa sổ phân bổ lượt xem (view-through attribution window), tính bằng **giờ**. ⏎ It defines the maximum interval between a TikTok view touchpoint (impression) and the conversion for which the view is still eligible to receive credit. ⏎ Examples: `1`, `24` (1 day), `168` (7 days) |
| attribution_method | string | **For app and web events only.** ⏎ Phương thức kỹ thuật được sử dụng để liên kết điểm chạm với chuyển đổi. ⏎ Examples: • `pixel`: matched through the TikTok pixel on the advertiser's website. • `PPS`: matched through Post-Purchase Survey. • `deeplink`: matched through a deeplink click identifier. • `modeled`: attribution produced by a statistical or ML model rather than a deterministic match. • `SKAN`: matched through Apple's SKAdNetwork framework. • `shop`: matched through a TikTok Shop signal. |
| decline_reason | string | **For app and web events only.** ⏎ Lý do hệ thống của bạn từ chối gán công nhận phân bổ cho TikTok đối với sự kiện này. ⏎ Examples: • `attributed_to_other_source`: another channel received the credit. • `organic`: no paid channel received credit; treated as an organic conversion. • `outside_attribution_window`: the TikTok touchpoint fell outside the click or view window. • `invalid_event`: the event failed a partner-side validation check. • `fraud_detected`: the touchpoint was flagged as fraudulent. • `duplicate_event`: the conversion was already counted in a prior report. • `low_confidence_match`: the touchpoint-to-conversion match did not meet the confidence threshold. • `missing_touchpoint`: no eligible TikTok touchpoint was found. • `missing_click_id`: the required TikTok click identifier was absent. • `privacy_threshold_filtered`: the event was filtered out by a privacy threshold. • `unsupported_signal`: the signal type is not supported by the attribution engine. • `other`: any other reason that does not fit the categories above. |
| utm_id | string | **For app and web events only.** ⏎ Mã định danh duy nhất của chiến dịch tiếp thị hoặc bộ tham số UTM tạo ra điểm chạm. ⏎ It corresponds to the `utm_id` parameter in the landing URL. ⏎ Use this field to report the custom campaign identifier from your landing page URL. This is particularly useful if your internal tracking relies on custom UTM values rather than TikTok's default campaign IDs. ⏎ Example: `summer2026_launch`. |
| utm_source | string | **For app and web events only.** ⏎ Nguồn lưu lượng truy cập giới thiệu người dùng đến trang đích, được ghi lại trong tham số URL `utm_source`. ⏎ It typically identifies the platform or property that hosted the ad. ⏎ Example: `tiktok`. |
| utm_medium | string | **For app and web events only.** ⏎ Phương tiện tiếp thị phân phối lưu lượng truy cập, được ghi lại trong tham số URL `utm_medium`. ⏎ It identifies the category of the placement rather than the platform. ⏎ Examples: `cpc`, `paid_social`, `display`. |
| utm_campaign | string | **For app and web events only.** ⏎ Tên chiến dịch tạo ra điểm chạm, được ghi lại trong tham số URL `utm_campaign`. ⏎ It is used to attribute performance to a specific marketing initiative within the traffic source. ⏎ Example: `summer2026_launch_us`. |

## Tham số `lead` (`lead` parameters)
Sử dụng các tham số `lead` để chia sẻ thông tin về khách hàng tiềm năng trong hệ thống CRM với Events API 2.0. Tham số `lead` chỉ nên được sử dụng khi báo cáo sự kiện CRM (`event_source` = `crm`).

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| lead_id **(Điều kiện)** | string | ** Required for CRM events. ** ⏎ ID of TikTok leads. ⏎ Every lead will have its `lead_id` when exported from TikTok. ⏎ To obtain the ID of a lead, download the lead by using the endpoints [/page/lead/task/](../12-api-reference/48-leads.md#doc-1739052936772610) and [/page/lead/task/download/](../12-api-reference/48-leads.md#doc-1739053563877378), or export the lead from TikTok Leads Center, the first-party CRM platform located within TikTok Ads Manager. |
| lead_event_source | string | Lead event source. ⏎ You can set this field to the name of your CRM system, such as HubSpot or Salesforce. |

---

<a id="doc-1805266308200514"></a>
<!-- doc_id: 1805266308200514 -->
<!-- doc_id: 1805266308200514 -->
# Công cụ chuyển đổi tải trọng (Payload Converter)
> Đường dẫn: Marketing API > Ad Measurement > Guides > Events API 2.0 > Payload Converter
Hướng dẫn này sẽ dẫn dắt bạn qua quy trình sử dụng Bộ chuyển đổi tải trọng (Payload Converter) cho Events API. 

Payload Converter cung cấp một giải pháp tự động nhận diện kênh của tải trọng bên ngoài (chẳng hạn như Meta) tại phía máy chủ của TikTok, sau đó chuyển đổi sang định dạng tương đương cho TikTok. Nhờ đó, nhà quảng cáo có thể trực tiếp gửi các sự kiện đã cấu trúc sẵn sang TikTok thông qua Events API.

## Trước khi bắt đầu
Vui lòng thực hiện theo [các bước này](do-luong-quang-cao-tom-tat.md#doc-1771100865818625) để bắt đầu kết nối dữ liệu web với TikTok trước khi gửi sự kiện bằng Payload Converter.

## Gửi yêu cầu (Send Requests)
Để gửi các sự kiện mới, hãy thực hiện yêu cầu `POST` tới điểm cuối của Events API: [https://business-api.tiktok.com/open_api/v1.3/event/track/](../12-api-reference/42-events-2-0.md#doc-1771101303285761).

| Header Field | Data Type | Description |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). ⏎ To obtain an access token, refer to [Events API 2.0 - Authentication](do-luong-quang-cao-p1.md#doc-1771101130925058). |
| X-Event-Source-ID  ****(Bắt buộc)**** | string | ID TikTok Pixel. |
| Content-Type ****(Bắt buộc)**** | string | Định dạng dữ liệu yêu cầu. ⏎ Allowed format: `application/json`. |
| X-Ttp-Cookie | string | For setting up deduplication between TikTok Pixel and Events API. ⏎ See Deduplication with Payload Converter for more details |

Các **bản demo Payload Converter** sau đây minh họa cách gửi sự kiện Meta qua TikTok Events API. Khi sự kiện đến TikTok, bộ chuyển đổi tải trọng sẽ tự động kích hoạt để chuyển đổi Sự kiện Meta thành Sự kiện TikTok tương đương.

### cURL
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/event/track/' \
--header 'Access-Token: <TIKTOK_PIXEL_ACCESS_TOKEN>' \
--header 'X-Event-Source-ID: <TIKTOK_PIXEL_ID>' \
--header 'Content-Type: application/json' \
--data-raw '
{
  "data": [
    {
      "event_name": "ViewContent",
      "event_time": 1705657064,
      "user_data": {
        "em": [
          "8830eedd6c6b5ea97d181563a349476ca1bb25ace1f94b5c5e48d9cad727941b"
        ],
        "ph": [
          "254aa248acb47dd654ca3ea53f48c2c26d641d23d7e2e93a1ec56258df7674c4"
        ],
        "client_ip_address": "123.123.123.123"
      },
      "custom_data": {
        "currency": "USD",
        "value": 123.45,
        "contents": [
          {
            "id": "product123",
            "quantity": 1
          }
        ]
      },
      "event_source_url": "http://tiktok-market.com/product/123",
      "action_source": "website"
    }
  ]
}
'
```

### Java SDK

Nếu nhà quảng cáo đã sử dụng Meta Conversions API SDK, bạn có thể tái sử dụng mã Meta hiện có. Chỉ cần thêm các tiêu đề "Access-Token" và "X-Event-Source-ID", bạn có thể dễ dàng gửi các sự kiện Meta sang TikTok (xem chi tiết trong ví dụ Java SDK bên dưới).

```http
// curl
import com.facebook.ads.sdk.APIContext;
import com.facebook.ads.sdk.APIException;
import com.facebook.ads.sdk.serverside.*;
import com.google.gson.Gson;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import okhttp3.*;

import java.io.IOException;
import java.util.Arrays;

public class Main {

    public static final String ACCESS_TOKEN = "<META_CAPI_ACCESS_TOKEN>";
    public static final String PIXEL_ID = "<META_PIXEL_ID>";

    public static void main(String[] args) {

        //Example of Sending events using Meta Conversion API SDK.
        APIContext context = new APIContext(ACCESS_TOKEN).enableDebug(true);
        context.setLogger(System.out);

        UserData userData = new UserData()
            .emails(Arrays.asList("joe@eg.com"))
            .phones(Arrays.asList("12345678901"))
            .clientIpAddress("123.123.123.123");

        Content content = new Content()
            .productId("product123")
            .quantity(1L);

        CustomData customData = new CustomData()
            .addContent(content)
            .currency("USD")
            .value(123.45F);

        Event event = new Event();
        event.eventName("ViewContent")
            .eventTime(System.currentTimeMillis() / 1000L)
            .userData(userData)
            .customData(customData)
            .eventSourceUrl("http://tiktok-market.com/product/123")
            .actionSource(ActionSource.website);

        EventRequest eventRequest = new EventRequest(PIXEL_ID, context);
        eventRequest.addDataItem(event);

        try {
            EventResponse response = eventRequest.execute();
            System.out.println(String.format("Standard API response : %s ", response));
        } catch (APIException e) {
            e.printStackTrace();
        }

        //Example of Payload Converter: Sending Meta Events via the TikTok Events API.
        JsonObject metaPayload = new JsonObject();
        metaPayload.add("data", new Gson().fromJson(eventRequest.getSerializedPayload(), JsonElement.class));

        OkHttpClient client = new OkHttpClient();
        Request request = new Request.Builder()
            .url("https://business-api.tiktok.com/open_api/v1.3/event/track/")
            .addHeader("Access-Token", "<TIKTOK_PIXEL_ACCESS_TOKEN>")
            .addHeader("X-Event-Source-ID", "<TIKTOK_PIXEL_ID>")
            .addHeader("Content-Type", "application/json")
            .post(RequestBody.create(MediaType.parse("application/json; charset=utf-8"), metaPayload.toString()))
            .build();

        try {
            Response response = client.newCall(request).execute();
            System.out.println(String.format("Tiktok Standard API response : %s ", response));

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

### Mã mẫu Java không dùng SDK (Java Non-SDK Sample)
```http
// curl
import com.google.gson.JsonArray;
import com.google.gson.JsonObject;
import okhttp3.*;

public class Main {

    public static final String ACCESS_TOKEN = "<META_CAPI_ACCESS_TOKEN>";
    public static final String PIXEL_ID = "<META_PIXEL_ID>";

    public static void main(String[] args) {

        //Example of Sending Meta events using http post
        JsonObject userData = new JsonObject();
        userData.addProperty("em", "8830eedd6c6b5ea97d181563a349476ca1bb25ace1f94b5c5e48d9cad727941b");
        userData.addProperty("ph", "254aa248acb47dd654ca3ea53f48c2c26d641d23d7e2e93a1ec56258df7674c4");
        
        JsonObject contentsData = new JsonObject();
        customData.addProperty("product_id", "product123");
        customData.addProperty("quantity", 1);
        
        List<JsonObject> contentsArr = new ArrayList<>();
        contentsArr.add(contentsData);
        
        JsonObject customData = new JsonObject();
        customData.addProperty("contents", contentsArr);
        customData.addProperty("value", 123.45);
        customData.addProperty("currency", "USD");

        JsonObject event = new JsonObject();
        event.addProperty("event_name", "ViewContent");
        event.addProperty("event_time", System.currentTimeMillis() / 1000L);
        event.add("user_data", userData);
        event.add("custom_data", customData);
        event.addProperty("action_source", "website");
        event.addProperty("event_source_url", "http://tiktok-market.com/product/123");

        JsonObject metaPayload = new JsonObject();
        JsonArray data = new JsonArray();
        data.add(event);
        metaPayload.add("data", data);

        OkHttpClient client = new OkHttpClient();
        Request request = new Request.Builder()
                .url("https://graph.facebook.com/v20.0/" + PIXEL_ID + "/events?access_token=" + ACCESS_TOKEN)
                .addHeader("Content-Type", "application/json")
                .post(RequestBody.create(MediaType.parse("application/json; charset=utf-8"), metaPayload.toString()))
                .build();

        try {
            Response response = client.newCall(request).execute();
            System.out.println(String.format("Meta Standard API response : %s ", response));

        } catch (Throwable t) {
            System.out.println(t.getMessage());
        }

        //Example of Payload Converter: Sending Meta Events via the TikTok Events API.
        OkHttpClient tiktokClient = new OkHttpClient();
        Request tiktokRequest = new Request.Builder()
                .url("https://business-api.tiktok.com/open_api/v1.3/event/track/")
                .addHeader("Access-Token", "<TIKTOK_PIXEL_ACCESS_TOKEN")
                .addHeader("X-Event-Source-ID", "<TIKTOK_PIXEL_ID>")
                .addHeader("Content-Type", "application/json")
                .post(RequestBody.create(MediaType.parse("application/json; charset=utf-8"), metaPayload.toString()))
                .build();

        try {
            Response response = tiktokClient.newCall(tiktokRequest).execute();
            System.out.println(String.format("Tiktok Standard API response : %s ", response));

        } catch (Throwable t) {
            System.out.println(t.getMessage());
        }
    }
}
```

### Python SDK
```http
// curl
import json
import time

import requests
from facebook_business.adobjects.serverside.action_source import ActionSource
from facebook_business.adobjects.serverside.content import Content
from facebook_business.adobjects.serverside.custom_data import CustomData
from facebook_business.adobjects.serverside.event import Event
from facebook_business.adobjects.serverside.event_request import EventRequest
from facebook_business.adobjects.serverside.user_data import UserData
from facebook_business.api import FacebookAdsApi

# Ví dụ lệnh cURL (Example) of Sending events using Meta Conversion API SDK.
access_token = '<META_CAPI_ACCESS_TOKEN>'
pixel_id = '<META_PIXEL_ID>'

FacebookAdsApi.init(access_token=access_token)

user_data = UserData(
    emails=['joe@eg.com'],
    phones=['12345678901'],
    client_ip_address='123.123.123.123',
)

content = Content(
    product_id='product123',
    quantity=1,
)

custom_data = CustomData(
    contents=[content],
    currency='USD',
    value='123.45',
)

event = Event(
    event_name='ViewContent',
    event_time=int(time.time()),
    user_data=user_data,
    custom_data=custom_data,
    event_source_url='http://tiktok-market.com/product/123',
    action_source=ActionSource.WEBSITE,
)

events = [event]

event_request = EventRequest(
    events=events,
    pixel_id=pixel_id,
)

event_response = event_request.execute()
print(event_response)

# Ví dụ lệnh cURL (Example) of Payload Converter: Sending Meta Events via the TikTok Events API.
meta_payload = {
    'data': [event.normalize() for event in events]
}

headers = {
    'Access-Token': '<TIKTOK_PIXEL_ACCESS_TOKEN>',
    'X-Event-Source-ID': '<TIKTOK_PIXEL_ID>',
    'Content-Type': 'application/json',
}

response = requests.post('https://business-api.tiktok.com/open_api/v1.3/event/track/', headers=headers,
                         data=json.dumps(meta_payload))
print(response.text)
```

### Mã mẫu Python không dùng SDK (Python Non-SDK Sample)
```http
// curl
import json
import time

import requests

META_ACCESS_TOKEN = '<META_CAPI_ACCESS_TOKEN>'
META_PIXEL_ID = '<META_PIXEL_ID>'

def convert():
    # Ví dụ lệnh cURL (Example) Meta CAPI event
    event = {
        "event_name": "ViewContent",
        "event_time": int(time.time()),
        "action_source": "website",
        "event_source_url": "http://tiktok-market.com/product/123",
        "user_data": {
            "em": [
                # hash for joe@eg.com 
                "8830eedd6c6b5ea97d181563a349476ca1bb25ace1f94b5c5e48d9cad727941b"
            ],
            "ph": [
                # hash for 12345678901
                "254aa248acb47dd654ca3ea53f48c2c26d641d23d7e2e93a1ec56258df7674c4"
            ]
        },
        "custom_data": {
            "contents": [
                {
                    "product_id": "product123",
                    "quantity": 1
                }
            ],
            "currency": "USD",
            "value": 123.45
        }
    }

    meta_payload = {
        'data': [event]
    }
    # post event to Meta CAPI
    meta_url = "https://graph.facebook.com/v20.0/" + META_PIXEL_ID + "/events?access_token=" + META_ACCESS_TOKEN
    meta_headers = {'Content-Type': 'application/json'}
    meta_response = requests.post(url=meta_url, headers=meta_headers, data=json.dumps(meta_payload))
    print(meta_response.text)

    tiktok_headers = {
        'Access-Token': '<TIKTOK_PIXEL_ACCESS_TOKEN>',  # tiktok eAPI access token
        'X-Event-Source-ID': '<TIKTOK_PIXEL_ID>',  # tiktok ID TikTok Pixel
        'Content-Type': 'application/json',
    }
    # post same meta payload to TikTok Events API
    tiktok_response = requests.post(url='https://business-api.tiktok.com/open_api/v1.3/event/track/',
                                    headers=tiktok_headers, data=json.dumps(meta_payload))
    # Ví dụ lệnh cURL (Example) success response {"code": 0, "message": "OK", "request_id": "xxxxxxx", "data": {}}
    print(tiktok_response.text)
```

## Xác minh thiết lập sự kiện (Verify Events Setup)
Sau khi thiết lập tích hợp Payload Converter và trước khi gửi sự kiện thực tế tới TikTok, bạn có thể gửi các sự kiện kiểm tra để xác minh kết nối dữ liệu hoạt động bình thường. Vui lòng làm theo [các bước này](do-luong-quang-cao-p1.md#doc-1771100984456193) để tạo mã sự kiện kiểm tra đưa vào tải trọng gửi tới TikTok.

### cURL

```
// http
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/event/track/' \
--header 'Access-Token: <TIKTOK_PIXEL_ACCESS_TOKEN>' \
--header 'X-Event-Source-ID: <TIKTOK_PIXEL_ID>' \
--header 'Content-Type: application/json' \
--data-raw '
{
  "data": [
    {
      "event_name": "ViewContent",
      "event_time": 1705657064,
      "user_data": {
        "em": [
          "8830eedd6c6b5ea97d181563a349476ca1bb25ace1f94b5c5e48d9cad727941b"
        ],
        "ph": [
          "254aa248acb47dd654ca3ea53f48c2c26d641d23d7e2e93a1ec56258df7674c4"
        ],
        "client_ip_address": "123.123.123.123"
      },
      "custom_data": {
        "currency": "USD",
        "value": 123.45,
        "contents": [
          {
            "id": "product123",
            "quantity": 1
          }
        ]
      },
      "event_source_url": "http://tiktok-market.com/product/123",
      "action_source": "website"
    }
  ],
  <span style="background-color: green;">"test_event_code": "&#60;TIKTOK_TEST_EVENT_CODE&#62;"</span>
}
'
```

### Java SDK

```
// http
import com.facebook.ads.sdk.APIContext;
import com.facebook.ads.sdk.APIException;
import com.facebook.ads.sdk.serverside.*;
import com.google.gson.Gson;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import okhttp3.*;

import java.io.IOException;
import java.util.Arrays;

public class Main {

    public static final String ACCESS_TOKEN = "<META_CAPI_ACCESS_TOKEN>";
    public static final String PIXEL_ID = "<META_PIXEL_ID>";

    public static void main(String[] args) {

        //Example of Sending events using Meta Conversion API SDK.
        APIContext context = new APIContext(ACCESS_TOKEN).enableDebug(true);
        context.setLogger(System.out);

        UserData userData = new UserData()
            .emails(Arrays.asList("joe@eg.com"))
            .phones(Arrays.asList("12345678901"))
            .clientIpAddress("123.123.123.123");

        Content content = new Content()
            .productId("product123")
            .quantity(1L);

        CustomData customData = new CustomData()
            .addContent(content)
            .currency("USD")
            .value(123.45F);

        Event event = new Event();
        event.eventName("ViewContent")
            .eventTime(System.currentTimeMillis() / 1000L)
            .userData(userData)
            .customData(customData)
            .eventSourceUrl("http://tiktok-market.com/product/123")
            .actionSource(ActionSource.website);

        EventRequest eventRequest = new EventRequest(PIXEL_ID, context);
        eventRequest.addDataItem(event);
        <span style="background-color: green;">eventRequest.setTestEventCode("&#60;TIKTOK_TEST_EVENT_CODE&#62;");</span>

        try {
            EventResponse response = eventRequest.execute();
            System.out.println(String.format("Standard API response : %s ", response));
        } catch (APIException e) {
            e.printStackTrace();
        }

        //Example of Payload Converter: Sending Meta Events via the TikTok Events API.
        JsonObject metaPayload = new JsonObject();
        metaPayload.add("data", new Gson().fromJson(eventRequest.getSerializedPayload(), JsonElement.class));

        OkHttpClient client = new OkHttpClient();
        Request request = new Request.Builder()
            .url("https://business-api.tiktok.com/open_api/v1.3/event/track/")
            .addHeader("Access-Token", "<TIKTOK_PIXEL_ACCESS_TOKEN>")
            .addHeader("X-Event-Source-ID", "<TIKTOK_PIXEL_ID>")
            .addHeader("Content-Type", "application/json")
            .post(RequestBody.create(MediaType.parse("application/json; charset=utf-8"), metaPayload.toString()))
            .build();

        try {
            Response response = client.newCall(request).execute();
            System.out.println(String.format("Tiktok Standard API response : %s ", response));

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

### Mã mẫu Java không dùng SDK (Java Non-SDK Sample)

```
// http
import com.google.gson.JsonArray;
import com.google.gson.JsonObject;
import okhttp3.*;

public class Main {

    public static final String ACCESS_TOKEN = "<META_CAPI_ACCESS_TOKEN>";
    public static final String PIXEL_ID = "<META_PIXEL_ID>";

    public static void main(String[] args) {

        //Example of Sending Meta events using http post
        JsonObject userData = new JsonObject();
        userData.addProperty("em", "8830eedd6c6b5ea97d181563a349476ca1bb25ace1f94b5c5e48d9cad727941b");
        userData.addProperty("ph", "254aa248acb47dd654ca3ea53f48c2c26d641d23d7e2e93a1ec56258df7674c4");
        
        JsonObject contentsData = new JsonObject();
        customData.addProperty("product_id", "product123");
        customData.addProperty("quantity", 1);
        
        List<JsonObject> contentsArr = new ArrayList<>();
        contentsArr.add(contentsData);
        
        JsonObject customData = new JsonObject();
        customData.addProperty("contents", contentsArr);
        customData.addProperty("value", 123.45);
        customData.addProperty("currency", "USD");

        JsonObject event = new JsonObject();
        event.addProperty("event_name", "ViewContent");
        event.addProperty("event_time", System.currentTimeMillis() / 1000L);
        event.add("user_data", userData);
        event.add("custom_data", customData);
        event.addProperty("action_source", "website");
        event.addProperty("event_source_url", "http://tiktok-market.com/product/123");

        JsonObject metaPayload = new JsonObject();
        JsonArray data = new JsonArray();
        data.add(event);
        metaPayload.add("data", data);
        <span style="background-color: green;">metaPayload.add("test_event_code", "&#60;TIKTOK_TEST_EVENT_CODE&#62;")</span>

        OkHttpClient client = new OkHttpClient();
        Request request = new Request.Builder()
                .url("https://graph.facebook.com/v20.0/" + PIXEL_ID + "/events?access_token=" + ACCESS_TOKEN)
                .addHeader("Content-Type", "application/json")
                .post(RequestBody.create(MediaType.parse("application/json; charset=utf-8"), metaPayload.toString()))
                .build();

        try {
            Response response = client.newCall(request).execute();
            System.out.println(String.format("Meta Standard API response : %s ", response));

        } catch (Throwable t) {
            System.out.println(t.getMessage());
        }

        //Example of Payload Converter: Sending Meta Events via the TikTok Events API.
        OkHttpClient tiktokClient = new OkHttpClient();
        Request tiktokRequest = new Request.Builder()
                .url("https://business-api.tiktok.com/open_api/v1.3/event/track/")
                .addHeader("Access-Token", "<TIKTOK_PIXEL_ACCESS_TOKEN")
                .addHeader("X-Event-Source-ID", "<TIKTOK_PIXEL_ID>")
                .addHeader("Content-Type", "application/json")
                .post(RequestBody.create(MediaType.parse("application/json; charset=utf-8"), metaPayload.toString()))
                .build();

        try {
            Response response = tiktokClient.newCall(tiktokRequest).execute();
            System.out.println(String.format("Tiktok Standard API response : %s ", response));

        } catch (Throwable t) {
            System.out.println(t.getMessage());
        }
    }
}
```

### Python SDK

```
// http
import json
import time

import requests
from facebook_business.adobjects.serverside.action_source import ActionSource
from facebook_business.adobjects.serverside.content import Content
from facebook_business.adobjects.serverside.custom_data import CustomData
from facebook_business.adobjects.serverside.event import Event
from facebook_business.adobjects.serverside.event_request import EventRequest
from facebook_business.adobjects.serverside.user_data import UserData
from facebook_business.api import FacebookAdsApi

# Ví dụ lệnh cURL (Example) of Sending events using Meta Conversion API SDK.
access_token = '<META_CAPI_ACCESS_TOKEN>'
pixel_id = '<META_PIXEL_ID>'

FacebookAdsApi.init(access_token=access_token)

user_data = UserData(
    emails=['joe@eg.com'],
    phones=['12345678901'],
    client_ip_address='123.123.123.123',
)

content = Content(
    product_id='product123',
    quantity=1,
)

custom_data = CustomData(
    contents=[content],
    currency='USD',
    value='123.45',
)

event = Event(
    event_name='ViewContent',
    event_time=int(time.time()),
    user_data=user_data,
    custom_data=custom_data,
    event_source_url='http://tiktok-market.com/product/123',
    action_source=ActionSource.WEBSITE,
)

events = [event]

event_request = EventRequest(
    events=events,
    <span style="background-color: green;">test_event_code='&#60;TIKTOK_TEST_EVENT_CODE&#62;',</span>
    pixel_id=pixel_id,
)

event_response = event_request.execute()
print(event_response)

# Ví dụ lệnh cURL (Example) of Payload Converter: Sending Meta Events via the TikTok Events API.
meta_payload = {
    'data': [event.normalize() for event in events]
}

headers = {
    'Access-Token': '<TIKTOK_PIXEL_ACCESS_TOKEN>',
    'X-Event-Source-ID': '<TIKTOK_PIXEL_ID>',
    'Content-Type': 'application/json',
}

response = requests.post('https://business-api.tiktok.com/open_api/v1.3/event/track/', headers=headers,
                         data=json.dumps(meta_payload))
print(response.text)
```

### Mã mẫu Python không dùng SDK (Python Non-SDK Sample)

```
// http
import json
import time

import requests

META_ACCESS_TOKEN = '<META_CAPI_ACCESS_TOKEN>'
META_PIXEL_ID = '<META_PIXEL_ID>'

def convert():
    # Ví dụ lệnh cURL (Example) Meta CAPI event
    event = {
        "event_name": "ViewContent",
        "event_time": int(time.time()),
        "action_source": "website",
        "event_source_url": "http://tiktok-market.com/product/123",
        "user_data": {
            "em": [
                # hash for joe@eg.com 
                "8830eedd6c6b5ea97d181563a349476ca1bb25ace1f94b5c5e48d9cad727941b"
            ],
            "ph": [
                # hash for 12345678901
                "254aa248acb47dd654ca3ea53f48c2c26d641d23d7e2e93a1ec56258df7674c4"
            ]
        },
        "custom_data": {
            "contents": [
                {
                    "product_id": "product123",
                    "quantity": 1
                }
            ],
            "currency": "USD",
            "value": 123.45
        }
    }

    meta_payload = {
        'data': [event],
        <span style="background-color: green;">'test_event_code': '&#60;TIKTOK_TEST_EVENT_CODE&#62;'</span>
    }
    # post event to Meta CAPI
    meta_url = "https://graph.facebook.com/v20.0/" + META_PIXEL_ID + "/events?access_token=" + META_ACCESS_TOKEN
    meta_headers = {'Content-Type': 'application/json'}
    meta_response = requests.post(url=meta_url, headers=meta_headers, data=json.dumps(meta_payload))
    print(meta_response.text)

    tiktok_headers = {
        'Access-Token': '<TIKTOK_PIXEL_ACCESS_TOKEN>',  # tiktok eAPI access token
        'X-Event-Source-ID': '<TIKTOK_PIXEL_ID>',  # tiktok ID TikTok Pixel
        'Content-Type': 'application/json',
    }
    # post same meta payload to TikTok Events API
    tiktok_response = requests.post(url='https://business-api.tiktok.com/open_api/v1.3/event/track/',
                                    headers=tiktok_headers, data=json.dumps(meta_payload))
    # Ví dụ lệnh cURL (Example) success response {"code": 0, "message": "OK", "request_id": "xxxxxxx", "data": {}}
    print(tiktok_response.text)
```

Chuyển đến tab **Kiểm tra sự kiện (Test Events)** của Pixel trong Trình quản lý sự kiện và tìm sự kiện kiểm tra trong phần **Hoạt động sự kiện (Event Activity)**. Mọi vấn đề với tải trọng sẽ hiển thị để giúp bạn giải quyết sự cố.

Hãy đảm bảo xóa bỏ trường `test_event_code` trước khi chuyển sang chế độ sản xuất chính thức ('Production').

## Khử trùng lặp với Payload Converter
Khử trùng lặp là bắt buộc đối với nhà quảng cáo sử dụng cả TikTok Pixel SDK và Events API để gửi cùng một sự kiện, giúp TikTok báo cáo và tối ưu hóa hiệu suất chiến dịch tốt hơn. Tìm hiểu thêm về [Khử trùng lặp sự kiện](do-luong-quang-cao-p1.md#doc-1771100965992450).

Khi gửi tải trọng của nền tảng khác tới Events API (tức tận dụng tính năng Payload Converter), bạn có thể thiết lập [Khử trùng lặp qua Cookie](do-luong-quang-cao-p1.md#doc-1771100965992450) để khử trùng lặp sự kiện giữa TikTok Pixel và Events API.

Bạn sẽ cần [bật cookie bên thứ nhất](do-luong-quang-cao-p1.md#doc-1771100936446977) trong cài đặt TikTok Pixel của mình và gửi thêm tiêu đề yêu cầu HTTP `X-Ttp-Cookie` cùng với yêu cầu Events API. Giá trị của tiêu đề `X-Ttp-Cookie` phải là giá trị cookie bên thứ nhất của TikTok (`_ttp`). Ví dụ yêu cầu cURL:

```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/event/track/' \
--header 'Access-Token: <TIKTOK_PIXEL_ACCESS_TOKEN>' \
--header 'X-Event-Source-ID: <TIKTOK_PIXEL_ID>' \
--header 'X-Ttp-Cookie: <TIKTOK_TTP_COOKIE_VALUE>' \
--header 'Content-Type: application/json' \
--data-raw '{
  <SOME_PAYLOAD>
}'
```

## Phản hồi và Xử lý lỗi (Responses & Errors)
Để xử lý phản hồi lỗi API, vui lòng tham khảo [tài liệu này](do-luong-quang-cao-p1.md#doc-1771101162079234).

---

<a id="doc-1739584805049345"></a>
<!-- doc_id: 1739584805049345 -->
<!-- doc_id: 1739584805049345 -->
# Events API : App (Sự kiện ứng dụng 1.0)
> Đường dẫn: Marketing API > Ad Measurement > Guides > Events API 1.0 > Events API : App
> **Lưu ý:** Events API - App hiện đang trong giai đoạn Beta. Nếu muốn sử dụng API này, vui lòng liên hệ với đại diện TikTok của bạn. Tài khoản của bạn cần được thêm vào danh sách cho phép (allowlist) trước khi có thể báo cáo sự kiện qua [/v1.3/app/track/](../12-api-reference/43-events-1-0-p1.md#doc-1740859196043266) hoặc [/v1.3/app/batch/](../12-api-reference/43-events-1-0-p1.md#doc-1740859218541569).

## Tổng quan (Overview)
TikTok Events API là giao diện máy chủ-tới-máy chủ (server-to-server) bảo mật cho phép nhà quảng cáo chia sẻ trực tiếp các hành động mà khách hàng thực hiện trên trang web, ứng dụng hoặc tại cửa hàng ngoại tuyến với TikTok. Dữ liệu chia sẻ qua Events API được xử lý tương tự dữ liệu từ TikTok Pixel và TikTok SDK. Tùy thuộc vào dữ liệu được gửi, bạn có thể tận dụng Events API cho các giải pháp như quảng cáo sản phẩm động, nhắm mục tiêu tùy chỉnh, tối ưu hóa chiến dịch và phân bổ.

## Lợi ích (Benefits)

1. **Độ ổn định và bảo mật cao:** Tích hợp và vận hành không bị giới hạn phía máy khách như kết nối mạng chập chờn hay trình chặn quảng cáo.
2. **Kiểm soát quyền riêng tư linh hoạt:** Duy trì tuân thủ các quy định bảo mật với các quyền kiểm soát linh hoạt, cho phép bạn tùy chỉnh loại dữ liệu và thời điểm chia sẻ.
3. **Tối đa hóa hiệu quả đo lường:** Thu thập nhiều sự kiện hơn với độ chính xác cao trên các trình duyệt, ứng dụng và thiết bị khác nhau để có cái nhìn thống nhất về hành trình khách hàng từ xem trang đến mua hàng.

## Lưu ý (Notes)

* Đối với dữ liệu cấp người dùng trên iOS 14 trở lên, chúng tôi yêu cầu nhà quảng cáo tuân thủ chính sách của Apple về quyền riêng tư và sử dụng dữ liệu.
* Hiện tại, chúng tôi không chấp nhận các sự kiện tùy chỉnh hoặc thông tin nhận dạng cá nhân (PII) qua API này. Nếu có các sự kiện ứng dụng chưa được liệt kê nhưng rất quan trọng đối với hoạt động kinh doanh của nhà quảng cáo, vui lòng liên hệ với đại diện TikTok của bạn.
* Mỗi yêu cầu chỉ báo cáo sự kiện cho một Mobile App ID duy nhất, do việc ủy quyền được thực hiện ở cấp người dùng / ứng dụng di động. Xem phần Ủy quyền để biết chi tiết.
* Hệ thống hỗ trợ QPS <= 1.000 cho mỗi ứng dụng nhà phát triển (TikTok Marketing API app) trên mỗi điểm cuối. Nếu cần hạn mức cao hơn, hãy liên hệ chuyên viên giải pháp PSO.

Để báo cáo một sự kiện ứng dụng đơn lẻ tới TikTok, sử dụng điểm cuối `/app/track/`. Để báo cáo sự kiện ứng dụng hàng loạt, sử dụng điểm cuối `/app/batch/`.

## Quy trình tổng quan (Process Overview)

Tóm lại, để báo cáo các sự kiện ứng dụng qua Marketing API, nhà quảng cáo sẽ thực hiện các quy trình sau (giả định bạn đã chạy quảng cáo trên TikTok với một hoặc nhiều tài khoản quảng cáo):

1. Trước tiên, bạn cần đăng ký làm nhà phát triển quảng cáo TikTok (xem tài liệu **Đăng ký**) và tạo ứng dụng nhà phát triển TikTok Marketing API (xem tài liệu **Tạo ứng dụng**).

2. Trong tài khoản quảng cáo quảng bá ứng dụng, tạo ứng dụng di động trong TikTok Ads Manager > **Công cụ (Tools)** > **Sự kiện (Events)** > **Nguồn dữ liệu (Data sources)** > **Ứng dụng (App)** và chọn "**Tôi không dùng dịch vụ đối tác đo lường di động (MMP)**".

3. Sau khi tạo ứng dụng di động, bạn có thể nhấp vào đó để tạo TikTok App ID. Xem [Trung tâm trợ giúp doanh nghiệp](https://ads.tiktok.com/help/article?aid=10001060).

4. Tạo ứng dụng nhà phát triển TikTok với phạm vi quyền "Measurement > Report App Event".

5. Sau khi ứng dụng nhà phát triển được tạo, hãy sử dụng tài khoản người dùng từ bước 2 để mở URL ủy quyền trong trình duyệt và xác nhận cấp quyền cho ứng dụng nhà phát triển TikTok báo cáo sự kiện cho tất cả ứng dụng mà người dùng này có quyền truy cập.

   * Khuyến nghị chỉ cấp quyền "Report App Event" khi tạo mã truy cập này nhằm giảm thiểu rủi ro nếu mã truy cập bị lộ.

6. Đổi mã ủy quyền lấy mã truy cập (xem tài liệu **Ủy quyền**) và lưu mã truy cập ở nơi an toàn.

7. Sử dụng mã truy cập để xác thực trong yêu cầu Marketing API của bạn để gửi các sự kiện ứng dụng tới TikTok.

## Báo cáo sự kiện ứng dụng (Report an App Event)

Để báo cáo sự kiện ứng dụng di động (Android/iOS, ví dụ `LaunchAPP`, `Purchase`) tới TikTok, hãy thực hiện yêu cầu `POST` qua điểm cuối `/app/track/`.

### Yêu cầu gọi API (Request)

**Request address** 
https://business-api.tiktok.com/open_api/v1.3/app/track/

**Phương thức yêu cầu (Method)** POST

**Request Header**

| Field | Data Type | Desciption |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). It can be obtained through the ⏎ **"Get Access token"** interface. |
| Content-Type  ****(Bắt buộc)**** | string | Định dạng dữ liệu yêu cầu ⏎ Allowed format: `"application/json"` |

**Request parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| tiktok_app_id  ****(Bắt buộc)**** | number | TikTok App ID. ⏎ A TikTok App ID is a unique code that is generated in TikTok Ads Manager.  An advertiser can bind multiple TikTok App IDs to the same mobile app. To learn about how to generate a TikTok App ID, see [TikTok App ID](https://ads.tiktok.com/help/article?aid=10001060). |
| event | string | App event name. Examples: `INSTALLAPP`, `PURCHASE`. For supported app events, see the **Event name for event data connection** column in the tables on the [Supported event types](do-luong-quang-cao-p2.md#doc-1739585574120449). |
| timestamp  ****(Bắt buộc)**** | string | Timestamp with ISO 8601 format. See [wiki](https://en.wikipedia.org/wiki/ISO_8601). |
| context  ****(Bắt buộc)**** | object | Information about ad data connection in JSON format. For data fields in this object, see the **Context object** section below. |
| properties | object | Properties associated with the event in JSON format. For data fields in this object, see the **Properties object** section below. |

### Đối tượng Context (Context object)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| context  ****(Bắt buộc)**** | object | Information about ad data connection in JSON format. |
| ↳ app  ****(Bắt buộc)**** | object | Details about the app to report the event. |
| ↳↳ id  ****(Bắt buộc)**** | string | Mobile App ID. ⏎ Examples (bold section) are, App Store: https://apps.apple.com/us/app/angry-birds/id343200656; ⏎ Google Play：https://play.google.com/store/apps/details?id=com.rovio.angrybirds. ⏎ If it is an Android app not in Google Play store, please use the package name. |
| ↳↳ name | string | Application name |
| ↳↳ namespace | string | Android package name or iOS Bundle ID. Example: com.rovio.baba |
| ↳↳ version | string | App version number. For example, 3.0.2. |
| ↳↳ build | string | App build number. For example, 122. |
| ↳ device | object | Data used to report device-level data to match users. idfa/idfv/advertising_id are required so long as they are obtainable. iOS：idfa/idfv; Android：advertising_id. |
| ↳↳ platform | string | Operating system of user’s device; currently only accepting iOS/Android |
| ↳↳ idfa | string | iOS idfa. For iOS14+, please ensure iDFA data collection follows [Apple’s policies](https://developer.apple.com/app-store/user-privacy-and-data-use/). ⏎ Both raw and SHA-256 IDFA are accepted, but please note that: •  For raw IDFA, all characters must be UPPERCASE. For SHA-256 IDFA, all characters must be lowercase. Examples:  •  Raw IDFA: "EA7583CD-A667-48BC-B806-42ECB2B48606" •  SHA-256 IDFA: "70574fa9c8f498a7b2e5c8712b1126de7b1406fd02fdc591821c5bd33092fd1c" •  Leading/trailing spaces need to be trimmed before hashing. |
| ↳↳ idfv | string | iOS idfv |
| ↳↳ gaid | string | Google Advertising ID. ⏎ Both raw and SHA-256 GAID are accepted, but please note that: •    For both raw and SHA-256 GAID, all characters must be lowercase. Examples:  •      Raw GAID: "aaaaaa-2222-1111-8787-809e92233ba0" •      SHA-256 GAID: "0ebad966881e1eebffe69b3abf624631cf83ec9bf8cb3ce134c7c75c6d8ee7fc" •  Leading/trailing spaces need to be trimmed before hashing. |
| ↳↳ att_status | string | Liệu user has authorized your mobile app to access app-related data for measuring the user or the device. This is an iOS only field. Values:  • `AUTHORIZED`: The user has authorized access to app-related data that can be used for measuring the user or the device. • `DENIED`: The user didn't agree to authorize your mobile app to access app-related data for measuring the user or the device via [Apple's AppTrackingTransparency framework](https://developer.apple.com/documentation/apptrackingtransparency). If set to this value, TikTok will not use the PII data (e.g. User email/phone number) in this app event for user-level matching. • `NOT_DETERMINED`: The user has not yet received an authorization request to authorize access to app-related data that can be used for measuring the user or the device.  • `RESTRICTED`: The authorization to access app-related data is restricted. • `NOT_APPLICABLE`: The iOS version is below 14 or the device is running Android. |
| ↳ locale | string | Examples：zh-CN、en-US. For reference, see [the IETF BCP 47 standardized code](https://tools.ietf.org/rfc/bcp/bcp47.txt). |
| ↳ ip | string | User IP |
| ↳ user_agent | string | User agent from the user’s device. Example: Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1 |
| ↳ user | object | The personal data of the user. |
| ↳↳ external_id | string | The external user ID. ⏎ It must be hashed with SHA256 on the client side. Leading/Trailing spaces need to be trimmed before hashing. |
| ↳↳ phone_number | string | User's phone number. ⏎ It must be hashed with SHA256 on the client side. ⏎ Please include country code and format it based on the following rules: ⏎ If the country code is 86, then do not include country code (example: 13800000000). Otherwise, include country code with + and remove any other characters (spaces, '-') between numbers (example for US: +12133734253) ⏎ Hash the code with SHA256. Reference documents: https://github.com/google/libphonenumber |
| ↳↳ email | string | User's email. ⏎ It must be hashed with SHA256 on the client side. You should first lowcase all the characters and then do hash. |
| ↳ library | object | SDK version info. |
| ↳↳ name | string | Version number in string. Example: bytedance/tiktok-business-android-sdk |
| ↳↳ version | string | Version numer. Example: 1.2.0 |
| ↳ ori_attribution_partner | string | If the event is attributed by Mobile Measurement Partner to another platform, use this field to specify the platform name. Example: Facebook, Google. |
| ↳ ad | object | Ad information |
| ↳↳ callback | string | Callback information to help attribute events |
| ↳↳ campaign_id | number | ID chiến dịch quảng cáo |
| ↳↳ ad_id | number | ID nhóm quảng cáo |
| ↳↳ creative_id | number | ID mẫu quảng cáo |
| ↳↳ isRetargeting | boolean | Liệu user is a retargeting user |
| ↳↳ attributed | boolean | Liệu event is attributed |
| ↳↳ attributionType | string | Attribution type |
| ↳↳ attribution_provider | string | Attributed provider |
| ↳ location | object | User's location information |
| ↳↳ country | string | Country or region |
| ↳↳ city | string | City |

### Đối tượng Properties (Properties object)

Các thuộc tính liên kết với sự kiện theo định dạng JSON. Một số thuộc tính chỉ liên kết với một số sự kiện ứng dụng nhất định. Xem lược đồ bên dưới.

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| properties | object | Properties associated with the event in JSON format. |
| ↳ contents | object[] | Related items in an app event (e.g. items purchased in a Purchase event) |
| ↳↳ price | double | Price of item |
| ↳↳ quantity | number | Number of item |
| ↳↳ content_type | string | The type of content in the event. ⏎ Các giá trị enum hỗ trợ: `product`, `product_group`.    •  When the `content_id` in the `contents` parameter is specified as `sku_id`, set this field to `product`.   •  When the `content_id` in the `contents` parameter is specified as `item_group_id`, set this field to `product_group`. |
| ↳↳ content_id | string | ID of the product item in your system |
| ↳↳ brand | string | Brand name of the product item. |
| ↳ currency | string | ISO 4217 code. Examples: "EUR", "USD", "JPY" |
| ↳ value | double | Total value of the order or items sold |
| ↳ description | string | A string description of the app event |
| ↳ query | string | The text string that was searched for. |

#### Ví dụ lệnh cURL (Example)

```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/app/track/' \
--header 'Content-Type: application/json' \
--header 'Access-Token: {{Access-Token}}' \
--data-raw \
'{
  "tiktok_app_id": "{{TIKTOK-APP-ID}}",
  "event":"AddToCart",
  "timestamp":"2023-09-17T19:49:27Z",
  "context":{
    "app":{
      "id":"1211123727",
      "name":"Angry Birds Classic",
      "namespace":"com.rovio.baba",
      "version":"3.0.2",
      "build":"122"
    },
    "device":{
      "att_status":"AUTHORIZED",
      "platform":"iOS",
      "idfa":"30255BCE-4CDA-4F62-91DC-4758FDFF8512"
    },
    "locale":"zh-CN",
    "user":{
      "email":"12346a405862e402eb76a70f8a26fc732d07c32931e9fae9ab1582911d2e8a3b",
      "phone_number":"12346a405862e402eb76a70f8a26fc732d07c32931e9fae9ab1582911d2e8a3b"
    },
    "library":{
      "name":"1.1.0-alpha.1",
      "version":"2"
    },
    "ad":{
      "callback":"E.C.P.ExampleCallback",
      "isRetargeting":false,
      "campaign_id":"1700817380525057",
      "attributed":true,
      "ad_id":"1700817380806706",
      "attributionType":"click_through",
      "creative_id":"1700817378256945",
      "attribution_provider":"mmp"
    }
  },
  "properties":{
    "currency":"USD",
    "value":10,
    "contents": [
      {
        "quantity":5,
        "price":9.9
      }
    ]
  }
}'
```

### Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | The Mã trạng thái phản hồi (0: Thành công). Để biết chi tiết, xem [Appendix-Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097) |
| message | string | The Thông điệp phản hồi từ máy chủ. Để biết chi tiết, xem [Appendix-Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097) |
| request_id | string | The unique ID of the request. |
| data | object | Returned data |

#### Ví dụ lệnh cURL (Example)

```http
// Success-Response
HTTPS/1.1 200 OK
{
    "message": "OK",
    "code": 0,
    "request_id": "2019091810032301011023224213558"
}
```

## Báo cáo sự kiện ứng dụng hàng loạt

Sử dụng điểm cuối này để báo cáo sự kiện ứng dụng hàng loạt nhằm giảm tải lưu lượng tới Marketing API. Bạn có thể báo cáo tối đa 1.000 sự kiện trong một yêu cầu (vượt quá 1.000 sự kiện sẽ bị từ chối toàn bộ).

### Yêu cầu gọi API (Request)

**Address** 

https://business-api.tiktok.com/open_api/v1.3/app/batch/

**Method** POST

**Header**

| Field | Data Type | Desciption |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). It can be obtained through the ⏎ **"Get Access token"** interface. |
| Content-Type  ****(Bắt buộc)**** | string | Định dạng dữ liệu yêu cầu ⏎ Allowed format: `"application/json"` |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| tiktok_app_id  ****(Bắt buộc)**** | number | TikTok App ID. ⏎ TikTok App is created in event manager and linked to mobile app, which also makes it linked to the user as an asset. An advertiser can bind multiple TikTok App to a same mobile app. The ID can be generated by referring to [this article](https://ads.tiktok.com/help/article?aid=10001060). |
| batch | object[] | An array of app events reported in batch. Length must be greater than 1 and smaller than 50. |
| ↳ type | string | App event type. Currently only support "track". |
| ↳ event | string | App event name. Examples: `INSTALLAPP`, `PURCHASE`. For supported app events, see the **Event name for event data connection** column in the tables on the **Supported event types**. |
| ↳ timestamp | string | Timestamp with ISO 8601 format. See [wiki](https://en.wikipedia.org/wiki/ISO_8601). |
| ↳ context  ****(Bắt buộc)**** | object | Information about ad data connection in JSON format. For data fields in this object, see the **Context object** section above. |
| ↳ properties | object | Properties associated with the event in JSON format. For data fields in this object, see the **Properties object** section above. |

#### Ví dụ lệnh cURL (Example)

```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/app/batch/' \
--header 'Content-Type: application/json' \
--header 'Access-Token: {{Access-Token}}' \
--data-raw \
'{
  "tiktok_app_id":"{{TIKTOK-APP-ID}}",
  "batch":[
    {
      "type":"track",
      "event":"InstallApp",
      "timestamp":"2023-09-17T19:49:27Z",
      "context":{
        "app":{
          "id":"com.rovio.angrybirds"
        },
        "user":{
          "email":"12346a405862e402eb76a70f8a26fc732d07c32931e9fae9ab1582911d2e8a3b"
        },
        "device":{
          "att_status":"AUTHORIZED",
          "platform":"iOS",
          "idfa":"30255BCE-4CDA-4F62-91DC-4758FDFF8512"
        },
        "ad":{
          "callback":"E.C.P.ExampleCallback"
        }
      }
    },
    {
      "type":"track",
      "event":"Purchase",
      "timestamp":"2023-09-17T20:00:00Z",
      "context":{
        "app":{
          "id":"com.rovio.angrybirds"
        },
        "user":{
          "email":"12346a405862e402eb76a70f8a26fc732d07c32931e9fae9ab1582911d2e8a3b"
        },
        "device":{
          "att_status":"AUTHORIZED",
          "platform":"iOS",
          "idfa":"30255BCE-4CDA-4F62-91DC-4758FDFF8512"
        },
        "ad":{
          "callback":"E.C.P.ExampleCallback"
        }
      }
    }
  ]
}'
```

### Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | The Mã trạng thái phản hồi (0: Thành công). Để biết chi tiết, xem [Appendix-Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097) |
| message | string | The Thông điệp phản hồi từ máy chủ. Để biết chi tiết, xem [Appendix-Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097) |
| request_id | string | The unique ID of the request. |
| data | object | Returned data |
| ↳ partial_failure | boolean | Liệu event reporting failed partially. |
| ↳ failed_events | object[] | List of errors in the case of partial failure |
| ↳↳ order_in_batch | number | Order in batch request |
| ↳↳ error | string | Error message |

#### Ví dụ lệnh cURL (Example)

```http
// Success-Response
HTTPS/1.1 200 OK
{
    "message": "OK",
    "code": 0,
    "request_id": "2019091810032301011023224213558"
}
```
```http
// Failure
{
    "code": 40000,
    "message": "The value:{'aa'} is invalid for the associated parameter email.",
    "request_id": "2021012904054301023125302028613"
}
```
```http
// Partial-Failure
{
    "code": 20001,
    "message": "Partial success. Correct entries are forwarded while incorrect ones are dropped.",
    "request_id": "2021012904061701023125302030787",
    "data": {
        "partial_failure": true,
        "failed_events": [
            {
                "order_in_batch": 0,
                "error": "unhashed email"
            }
        ]
    }
}
```

---

<a id="doc-1741601162187777"></a>
<!-- doc_id: 1741601162187777 -->
<!-- doc_id: 1741601162187777 -->
# Báo cáo sự kiện Web và tham số (1.0)
> Đường dẫn: Marketing API > Ad Measurement > Guides > Events API 1.0 > Events API : Web > Report web events and parameters
Bài viết này liệt kê các sự kiện web và tham số được hỗ trợ khi bạn báo cáo sự kiện web qua điểm cuối [/pixel/track/](../12-api-reference/43-events-1-0-p1.md#doc-1740858531237890) hoặc [/pixel/batch/](../12-api-reference/43-events-1-0-p1.md#doc-1740858565852225).

# Các sự kiện Web được hỗ trợ 
Sự kiện được định nghĩa là các hành động mà khách truy cập trang web thực hiện nhằm đạt được mục tiêu kinh doanh, chẳng hạn như thêm sản phẩm vào giỏ hàng, điền biểu mẫu hoặc mua hàng.

Có hai danh mục sự kiện trên TikTok:
- **Sự kiện tiêu chuẩn (Standard Events)**: Là các hành động có tên được xác định trước bởi TikTok. Sự kiện tiêu chuẩn được hỗ trợ trên tất cả các công cụ tích hợp của TikTok hiện nay và có thể dùng cho báo cáo, tối ưu hóa chuyển đổi và xây dựng tệp đối tượng. Xem danh sách chi tiết bên dưới.
- **Sự kiện tùy chỉnh (Custom Events)**: Là các hành động do đối tác TikTok tự định nghĩa ngoài danh sách sự kiện tiêu chuẩn. Sự kiện tùy chỉnh có thể thiết lập bằng Event Builder trong Trình quản lý sự kiện hoặc báo cáo trực tiếp qua Pixel và Web Events API. **Sự kiện tùy chỉnh hiện chỉ hỗ trợ cho mục đích báo cáo và tạo tệp đối tượng; CHƯA hỗ trợ tối ưu hóa.**

Bảng dưới đây liệt kê 18 sự kiện web tiêu chuẩn cùng các giá trị được khuyến nghị trong đối tượng `properties`. Vui lòng đảm bảo sử dụng chính xác tên hiển thị trong cột **Event** vì tên sự kiện có phân biệt chữ hoa chữ thường. 

| Event | Event Type in Events Manager | Description | Recommended fields in properties object |
|---|---|---|---|
| ViewContent | View Content | Khi một trang được xem. | `content_type`, `quantity, description`, `content_id`, `currency`, `value` |
| Search | Search | Khi một tìm kiếm được thực hiện. |  |
| AddToWishlist | Add to Wishlist | Khi một mặt hàng được thêm vào danh sách yêu thích. |  |
| AddToCart | Add to Cart | Khi một mặt hàng được thêm vào giỏ hàng. | `content_type`, `quantity`, `description`, `content_id`,` currency`, `value` |
| ApplicationApproval | Application Approval | Khi một đơn đăng ký được phê duyệt. |  |
| InitiateCheckout | Initiate Checkout | Khi quy trình thanh toán được bắt đầu. |  |
| AddPaymentInfo | Add Payment Info | Khi thông tin thanh toán được thêm trong luồng thanh toán. |  |
| Purchase | Purchase | Khi giao dịch thanh toán hoàn tất thành công. | `content_type`, `quantity`, `description`, `content_id`, `currency`, `value` |
| Contact | Contact | Khi có liên hệ hoặc tư vấn diễn ra. |  |
| Download | Download | Khi nút mở trang tải xuống trình duyệt bên ngoài được nhấp. |  |
| Lead | Submit Form | Khi biểu mẫu khách hàng tiềm năng được gửi. |  |
| CompleteRegistration | Complete Registration | Khi đăng ký tài khoản hoàn tất. |  |
| StartTrial | Start Trial | Khi người dùng bắt đầu dùng thử miễn phí sản phẩm hoặc dịch vụ. | `currency`, `value` |
| SubmitApplication | Submit Application | Khi người dùng gửi đơn đăng ký. |  |
| Subscribe | Subscribe | Khi đăng ký thuê bao/dịch vụ được kích hoạt. |  |
| CustomizeProduct | Customize Product | Khi người dùng tùy chỉnh sản phẩm. |  |
| FindLocation | Find Location | Khi người dùng tìm kiếm vị trí cửa hàng/chi nhánh. |  |
| Schedule | Schedule | Khi người dùng đặt lịch hẹn trao đổi hoặc ghé thăm địa điểm của bạn. |  |

# Các tham số được hỗ trợ
Phần này giới thiệu các tham số sự kiện, tham số đối tượng `context`, và tham số đối tượng `properties` được hỗ trợ.

## Tham số sự kiện (Event parameters)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| pixel_code  ****(Bắt buộc)**** | string | ID TikTok Pixel that can be found in Events Manager of the TikTok Ads Manager. Để biết chi tiết, xem the "Where can I find the pixel_code?" section in the [FAQs](do-luong-quang-cao-p1.md#doc-1749819287162881). |
| event ****(Bắt buộc)**** | string | Conversion event name. ⏎ It can be either a Standard Event or a Custom Event. ⏎ To find out the supported values for Standard Events, see the the "**Event**" column in the "[Supported web events](../12-api-reference/43-events-1-0-p1.md#doc-1740858531237890)" section. ⏎ To report a Custom Event, pass a customized name in this field. |
| event_id | string | Any string or hashed ID that can identify a unique event. This is required if you are sending overlapping events from both TikTok Pixel and Events API. Please check [Event deduplication](do-luong-quang-cao-p1.md#doc-1739584864945154) for details and complete the setup. ⏎ Some examples are: ⏎ 1. RandomNumber ⏎ 2. OrderID (for Purchase event) ⏎ 3. SessionID_RandomNumber ⏎ 4. ExternalID_RandomNumber ⏎ 5. BrowserID_RandomNumber |
| timestamp | string | Timestamp that the event took place. Timestamp with ISO 8601 format. For example, 2022-11-23T03:30:52Z. See [ISO_8601](https://en.wikipedia.org/wiki/ISO_8601) for details. ⏎ Note that if timestamp is not provided, the time when TikTok receives the event via the server will be used. |
| context ****(Bắt buộc)**** | object | Information about the circumstances when the event was triggered. Required to attribute events to TikTok campaigns. ⏎ For the data fields in this object, see the "`context` oject parameters" section below. |
| properties | object | Properties associated with the event. ⏎ For the data fields in this object, see the "`properties` object parameters" section below. |

## Tham số đối tượng `properties`
Bảng dưới đây giới thiệu các trường được hỗ trợ trong đối tượng `properties`:

| Parameter | Description | Value type | Required for reporting Return on Ad Spend (ROAS) or for Value-based Optimization (VBO) | Required for Video Shopping Ads |
|---|---|---|---|---|
| properties | Properties associated with the event in JSON format. | object |  |  |
| ↳ content_type | The `content_type` object property's value must be set to either `product`, or `product_group`. ⏎ If you use `sku_id` as `content_id`, use `product`. ⏎ If you use `item_group_id` as `content_id`, use `product_group`. ⏎ This field is required for VSA. | Must be either `product` or `product_group`. |  | ✅ |
| ↳ contents | A list of content objects that represent relevant products in a web event with product information. | Must be an array of objects |  | ✅ |
| ↳↳ price | The price of the item. ⏎ **Note**: **Price** is the price for a single item, and **value** is the total price of the order. For example, if you have two items each sold for $10, the price parameter would pass 10 and the value parameter would pass 20. | number |  |  |
| ↳↳ quantity | The number of the item. | number |  |  |
| ↳↳ content_id | Unique ID of the product or content. ⏎ Recommend using `sku id` or `item_group_id`. This should match the `sku_id` or `item_group_id` you set up in the catalog (if available). ⏎ This field is required for VSA | string |  | ✅ |
| ↳↳ content_category | Category of the page/product | string |  |  |
| ↳↳ content_name | Name of the page/product | string |  |  |
| ↳↳ brand | Brand name of the product item. | string |  |  |
| ↳ currency | ISO 4217 code. Examples: `EUR`, `USD`, `JPY`. ⏎ ** List of currencies currently supported:** AED, ARS, AUD, BDT, BHD, BIF, BOB, BRL, CAD, CHF, CLP, CNY, COP, CRC, CZK, DKK, DZD, EGP, EUR, GBP, GTQ, HKD, HNL, HUF, IDR, ILS, INR, ISK, JPY, KES, KHR, KRW, KWD, KZT, MAD, MOP, MXN, MYR, NGN, NIO, NOK, NZD, OMR, PEN, PHP, PHP, PKR, PLN, PYG, QAR, RON, RUB, SAR, SEK, SGD, THB, TRY, TWD, UAH, USD, VES, VND, ZAR | enum(string) | ✅ |  |
| ↳ value | Value of the order or items sold. ⏎ **Note**:  • **Price** is the price for a single item, and **value** is the total price of the order. For example, if you have two items each sold for ten dollars, the `price` parameter would pass `10.00` and the `value` parameter would pass `20.00`. • Values should always be formatted as an integer or decimal (ex: 10.00) regardless of the location, currency, etc. It cannot contain any currency signs, special characters, letters, or commas. | number | ✅ |  |
| ↳ query | The text string that was input by a user. For instance, if a person searches for a product on your website, you can forward the keyword being searched. If a person enters a coupon code at check out, you can forward the code. | string |  |  |
| ↳ description | Description of the item or page. | string |  |  |
| ↳ status | Status of an order, item, or service. ⏎ **Note**: Depending on your use of `status`, Events API may be required in order to share status changes to TikTok. | string |  |  |

## Tham số đối tượng `context`
Events API cho Web sử dụng thông tin khách hàng như TikTok Click ID, Đối sánh nâng cao (Advanced Matching) và các tín hiệu bổ sung như địa chỉ IP cùng User Agent để khớp các sự kiện người truy cập với người dùng TikTok. Sau khi khớp, dữ liệu có thể dùng để xây dựng tệp đối tượng, tối ưu hóa thuật toán và đo lường kết quả chiến dịch tốt hơn.

Chúng tôi rất khuyến nghị bạn gửi kèm nhiều loại dữ liệu so khớp để tăng độ chính xác của mô hình nhắm mục tiêu và tối ưu hóa. Bạn có thể sử dụng [Đối sánh nâng cao](do-luong-quang-cao-p1.md#doc-1749819614433282), [TikTok Click ID (ttclid) và Cookie](do-luong-quang-cao-p1.md#doc-1739584860883969) để phân bổ chuyển đổi.

Bảng dưới đây giới thiệu các trường được hỗ trợ trong đối tượng `context`:

| Field | Description | Data Type | Formatting | Example |
|---|---|---|---|---|
| context | Context contains all customer information parameters. | object |  |  |
| ↳ ad | Ad information. | object |  |  |
| ↳↳ callback | TikTok Click ID. TikTok Click ID (`ttclid`) is a data connection parameter appended to a landing page URL whenever a user clicks on an ad on TikTok. ⏎ The `ttclid` valid period is the same as your CTA window setting in [Attribution Manager](https://ads.tiktok.com/help/article/attribution-manager?redirected=1). ⏎ Để biết chi tiết, xem [Set up TikTok Click ID and Cookies](do-luong-quang-cao-p1.md#doc-1739584860883969) section. | string | A string starting with "E.C.P". | `"E.C.P.v3fQ2RHacdksKfofPmlyuStIIHJ4Af1tKYxF9zz2c2PLx1Oaw15oHpcfl5AH"` |
| ↳ page | Page information. | object |  |  |
| ↳↳ url | Page url when event happened. | string |  | `"http://demo.mywebsite.com/purchase"` |
| ↳↳ referrer | Page referrer. | string |  | `"http://demo.mywebsite.com"` |
| ↳ user | The personal data of a user. | object |  |  |
| ↳↳ external_id | Any unique identifier on the advertiser's side, such as loyalty membership IDs, user IDs, and external cookie IDs. ⏎ It must be hashed with SHA-256 on the client side. | string | Trim any leading and trailing spaces before hashing. | `"9f7ec22d72092cd3c0b58726ed9c2d91b92e51a3f29837508fb2948bb22dd2fd"` |
| ↳↳ email | The email of the customer if available. ⏎ It must be hashed with SHA-256 on the client side. | string | • Trim any leading and trailing spaces, and lowercase all characters before hashing. • Do not perform any other types of normalization on emails prior to hashing. • Only SHA-256 is accepted. Here is the recommended package: [GitHub - emn178/js-sha256: A simple SHA-256 / SHA-224 hash function for JavaScript supports UTF-8 encoding.](https://github.com/emn178/js-sha256) | `"0c7e6a405862e402eb76a70f8a26fc732d07c32931e9fae9ab1582911d2e8a3b"` |
| ↳↳ phone_number | The phone number of the customer if available. ⏎ It must be hashed with SHA-256 on the client side. | string | • Normalize your phone numbers to E.164 format,  a combination of + ［country code]［phone number]. An example of a US number in the E.164 format: +12133734253 • Recommend using [https://github.com/catamphetamine/libphonenumber-js](https://github.com/catamphetamine/libphonenumber-js) for E.164 parsing. • Only SHA-256 is accepted. Here is the recommended package: [GitHub - emn178/js-sha256: A simple SHA-256 / SHA-224 hash function for JavaScript supports UTF-8 encoding.](https://github.com/emn178/js-sha256) | `"9f7ec22d72092cd3c0b58726ed9c2d91b92e51a3f29837508fb2948bb22dd2fd"` |
| ↳↳ ttp | Cookie ID. If you also use Pixel SDK and enabled cookie, Pixel SDK automatically saves a unique identifier in the `_ttp` cookie. The value of `_ttp` is used to match website visitor events with TikTok ads. You can extract the value of `_ttp` and attach the value here. ⏎ Để biết chi tiết, xem [Set up TikTok Click ID and Cookies](do-luong-quang-cao-p1.md#doc-1739584860883969) section. | string |  |  |
| ↳ ip | Non-hashed public IP address of the browser. ⏎ To increase the probability of matching website visitor events with TikTok ads, we recommend sending both `ip` and `user_agent`. | string | Both IPv4 and IPv6 addresses are supported. For IPv6 addresses, both full and compressed formats are acceptable. ⏎ For example: • Full format: **2001:0db8:1111:000a:00b0:0000:0000:0200** • Compressed format: **2001:db8:1111:a:b0::200** |  |
| ↳ user_agent | Non-hashed user agent from the user’s device. ⏎ To increase the probability of matching website visitor events with TikTok ads, we recommend sending both `ip` and `user_agent`. | string |  | `"Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604"` |

# Báo cáo một sự kiện Web
Bạn có thể báo cáo một sự kiện web bằng điểm cuối [/pixel/track/](../12-api-reference/43-events-1-0-p1.md#doc-1740858531237890).

## Yêu cầu gọi API (Request)

**Địa chỉ (Address):** https://business-api.tiktok.com/open_api/v1.3/pixel/track/

**Method** POST

**Request header**

| Field | Data Type | Desciption |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token), which can be obtained in Events Manager under  **Tools** > **Events** > **Web Events** >Select any pixel on [TikTok Ads Manager](https://ads.tiktok.com/i18n/home). ⏎ Be aware that all TikTok Ads Manager roles can see the Settings tab. However, only an Admin or Toán tử điều kiện role can generate a token. |
| Content-Type  ****(Bắt buộc)**** | string | Định dạng dữ liệu yêu cầu ⏎ Allowed format: `"application/json"`. |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| pixel_code ****(Bắt buộc)**** | string | ID TikTok Pixel that can be found in Events Manager of the TikTok Ads Manager. Để biết chi tiết, xem the "Where can I find the pixel_code?" section in the [FAQs](do-luong-quang-cao-p1.md#doc-1749819287162881). |
| event  ****(Bắt buộc)**** | string | Conversion event name. ⏎ It can be either a Standard Event or a Custom Event. ⏎ To find out the supported values for Standard Events, see the the "**Event**" column in the "[Supported web events](../12-api-reference/43-events-1-0-p1.md#doc-1740858531237890)" section. ⏎ To report a Custom Event, pass a customized name in this field. |
| event_id | string | Any string or hashed ID that can identify a unique event. This is required if you are sending overlapping events from both TikTok Pixel and Events API. Please check [Event deduplication](do-luong-quang-cao-p1.md#doc-1739584864945154) for details and complete the setup. ⏎ Some examples are: ⏎ 1. RandomNumber ⏎ 2. OrderID (for Purchase event) ⏎ 3. SessionID_RandomNumber ⏎ 4. ExternalID_RandomNumber ⏎ 5. BrowserID_RandomNumber |
| timestamp | string | Timestamp that the event took place. Timestamp with ISO 8601 format. See [ISO_8601](https://en.wikipedia.org/wiki/ISO_8601). Please note, if timestamp is not provided, the time when TikTok receives the event via the server will be used. |
| context ****(Bắt buộc)**** | object | Information about the circumstances when the event was triggered. Required to attribute events to TikTok campaigns. The context object can be removed for testing event fires. For the data fields in this object, see the above "`context` object parameters" section. |
| properties | object | Properties associated with the event. For the data fields in this object, see the above "`properties` object parameters" section. |

###  Example

> **Lưu ý:** Bạn cần thay thế dữ liệu mẫu trong ví dụ bằng dữ liệu thực tế của mình.

```http
// cURL
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
}'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Response code. You should handle any errors indicated in the response code. For the complete list of response codes and descriptions, see [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | The log id of a request, which uniquely identifies the request. |
| data | object | Returned data. ⏎ Empty object (`{}`) for successful actions. |

### Ví dụ lệnh cURL (Example)

```http
// Success-Response
HTTPS/1.1 200 OK
{
    "message": "OK",
    "code": 0,
    "request_id": "2019091810032301011023224213558",
    "data":{}
}
```

# Báo cáo sự kiện Web hàng loạt

Bạn có thể sử dụng điểm cuối [/pixel/batch/](../12-api-reference/43-events-1-0-p1.md#doc-1740858565852225) để báo cáo sự kiện web hàng loạt nhằm giảm tải lưu lượng tới TikTok API for Business. Bạn có thể báo cáo tối đa 1.000 sự kiện trong một yêu cầu (vượt quá 1.000 sự kiện sẽ bị từ chối toàn bộ).

## Yêu cầu gọi API (Request)

**Địa chỉ (Address):** https://business-api.tiktok.com/open_api/v1.3/pixel/batch/

**Method** POST

**Request header**

| Field | Data Type | Desciption |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token), which can be obtained in Events Manager under  **Tools** > **Events** > **Web Events** >Select any pixel on [TikTok Ads Manager](https://ads.tiktok.com/i18n/home). ⏎ Be aware that all TikTok Ads Manager roles can see the Settings tab. However, only an Admin or Toán tử điều kiện role can generate a token. |
| Content-Type  ****(Bắt buộc)**** | string | Định dạng dữ liệu yêu cầu. ⏎ Allowed format: `"application/json"`. |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| pixel_code ****(Bắt buộc)**** | string | ID that can be found in Events Manager of the TikTok Ads Manager. Để biết chi tiết, xem the "Where can I find the pixel_code?" section in the [FAQs](do-luong-quang-cao-p1.md#doc-1749819287162881). |
| batch | object[] | A list of web events. |
| ↳ type | string | Currently only accepting value `track`. |
| ↳ event | string | Conversion event name. ⏎ It can be either a Standard Event or a Custom Event. ⏎ To find out the supported values for Standard Events, see the the "**Event**" column in the "[Supported web events](../12-api-reference/43-events-1-0-p1.md#doc-1740858531237890)" section. ⏎ To report a Custom Event, pass a customized name in this field. |
| ↳ event_id | string | Any string or hashed ID that can identify a unique event. This is required if you are sending overlapping events from both TikTok Pixel and Events API. Check [Event deduplication](do-luong-quang-cao-p1.md#doc-1739584864945154) for details and complete the setup. ⏎ Some examples are: • RandomNumber • OrderID (for Purchase event) • SessionID_RandomNumber • ExternalID_RandomNumber • BrowserID_RandomNumber |
| ↳ timestamp | string | Timestamp that the event took place. Timestamp with ISO 8601 format. See [ISO_8601](https://en.wikipedia.org/wiki/ISO_8601). Please note, if timestamp is not provided, the time when TikTok receives the event via the server will be used. |
| ↳ context | object | Information about the circumstances when the event was triggered. Required to attribute events to TikTok campaigns. The context object can be removed for testing event fires. Report context info about the event. For the data fields in this object, see the above "`context` object parameters" section. |
| ↳ properties | object | Properties associated with the event. For the data fields in this object, see the above "`properties` object parameters" section. |

### Ví dụ lệnh cURL (Example)
> **Lưu ý:** Bạn cần thay thế dữ liệu mẫu trong ví dụ bằng dữ liệu thực tế của mình.

```HTTP
// cURL
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/pixel/batch/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "pixel_code": "PIXEL_CODE",
    "batch": [
        {
            "type": "track",
            "event": "EVENT",
            "event_id": "1616318632825_357",
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

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Response code. For the complete list of response codes and descriptions, see [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | The log id of a request, which uniquely identifies the request. |
| data | object | Error details. |
| ↳ partial_failure | boolean | Liệu event reporting failed partially. |
| ↳ failed_events | object[] | List of errors in the case of partial failure. |
| ↳↳ order_in_batch | number | Order in batch request. |
| ↳↳ error | string | Error message. |

### Ví dụ lệnh cURL (Example)

```http
// Success-Response
HTTPS/1.1 200 OK
{
    "message": "OK",
    "code": 0,
    "request_id": "2019091810032301011023224213558",
    "data":{}
}
```

---

<a id="doc-1758053486938113"></a>
<!-- doc_id: 1758053486938113 -->
<!-- doc_id: 1758053486938113 -->
# Báo cáo sự kiện Ngoại tuyến và tham số (1.0)
> Đường dẫn: Marketing API > Ad Measurement > Guides > Events API 1.0 > Events API: Offline > Report Offline Events and Parameters
Bài viết này liệt kê các sự kiện ngoại tuyến và tham số được hỗ trợ khi bạn báo cáo sự kiện ngoại tuyến qua điểm cuối [/v1.3/offline/track/](../12-api-reference/43-events-1-0-p1.md#doc-1758428013689857) hoặc [/v1.3/offline/batch/](../12-api-reference/43-events-1-0-p1.md#doc-1758428053652482).

# Các sự kiện Ngoại tuyến được hỗ trợ
Sự kiện được định nghĩa là các hành động mà khách hàng ngoại tuyến thực hiện để đạt mục tiêu kinh doanh. Sự kiện tiêu chuẩn là các hành động được định nghĩa trước mà TikTok For Business hỗ trợ. Bảng dưới đây liệt kê toàn bộ Sự kiện ngoại tuyến được hỗ trợ. Hãy đảm bảo sử dụng chính xác tên trong cột **Event** vì trường này phân biệt chữ hoa/chữ thường.

| Event | Examples |
|---|---|
| Purchase | In-store purchase, console purchase |
| Contact | Call-center events, over-the-chat events |
| Subscribe | In-store subscription, console subscription |
| Lead | **Note**: If advertisers cannot pass TikTok Lead ID via Events API for web, they should take the Offline path. |
| AddPaymentInfo | When a visitor adds their payment information at checkout. |
| AddToCart | When a visitor adds an item to the cart. |
| ApplicationApproval | Khi một đơn đăng ký được phê duyệt. |
| AddToWishlist | When a visitor adds an item to the wishlist. |
| CompleteRegistration | When a visitor signs up for something such as account registration. |
| Download | When a visitor downloads something from your website. |
| InitiateCheckout | When a visitor proceeds to checkout. |
| Search | When a visitor searches. |
| ViewContent | When a visitor views a specific page. |
| StartTrial | Khi người dùng bắt đầu dùng thử miễn phí sản phẩm hoặc dịch vụ. |
| SubmitApplication | Khi người dùng gửi đơn đăng ký. |
| CustomizeProduct | Khi người dùng tùy chỉnh sản phẩm. |
| FindLocation | Khi người dùng tìm kiếm vị trí cửa hàng/chi nhánh. |
| Schedule | Khi người dùng đặt lịch hẹn trao đổi hoặc ghé thăm địa điểm của bạn. |

# Báo cáo một sự kiện Ngoại tuyến
Bạn có thể báo cáo một sự kiện ngoại tuyến bằng điểm cuối [/v1.3/offline/track/](../12-api-reference/43-events-1-0-p1.md#doc-1758428013689857).

## Yêu cầu gọi API (Request)

**Địa chỉ (Address):** https://business-api.tiktok.com/open_api/v1.3/offline/track/

**Method** POST

**Request header**

| Field | Data Type | Desciption |
|---|---|---|
| Content-Type  ****(Bắt buộc)**** | string | Định dạng dữ liệu yêu cầu. ⏎ Allowed format: `"application/json"`. |
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết | Examples |
|---|---|---|---|
| event  ****(Bắt buộc)**** | string | Event type. Refer to the "Supported Offline Events" section above for supported values. | Purchase |
| event_set_id  ****(Bắt buộc)**** | string | Event Set ID. | 7057103914977558530 |
| event_id | string | A unique value for each event. This ID can be used to match data between partner and TikTok. We suggest it is a String of 32 characters, including numeric digits (0-9), uppercase letters (A-Z), and lowercase letters (a-z). | 1616318632825_357 |
| context ****(Bắt buộc)**** | object | Dictionary of extra information that provides useful context about a message. For the data fields in this object, see the "User context object parameters" section below. | See "User context object parameters" section |
| properties ****(Bắt buộc)**** | object | Free-form dictionary of properties of the event, e.g., revenue. For the data fields in this object, see the "Properties object parameters" section below. | See "Properties object parameters" section |
| timestamp ****(Bắt buộc)**** | datetime | Timestamp that the event took place. Timestamp with [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) format. | 2019-06-12T19:11:01.152Z |

### Ví dụ lệnh cURL (Example)
> **Lưu ý:** Bạn cần thay thế dữ liệu mẫu trong ví dụ bằng dữ liệu thực tế của mình.
```HTTP
// cURL
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/offline/track/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "event_set_id":"{{event_set_id}}", 
  "event": "Purchase",
  "event_id":"{{event_id}}", 
  "timestamp": "2020-09-17T19:49:27Z",     
  "context": {
    "user": {
      "phone_numbers": ["2f9d2b4df907e5c9a7b3434351b55700167b998a83dc479b825096486ffcf4ea",
      "1e7c3b4ff108e5c9a7b3434351b55700167b998a83dc479b825096486cvvf6gt"],
      "emails": ["dd6ff77f54e2106661089bae4d40cdb600979bf7edc9eb65c0942ba55c7c2d7f"]
    }
  },
  "properties": {
    "order_id": "abc_xyz", 
    "shop_id": "123abc",
    "contents": [
      {
        "price": 8,
        "quantity": 2,
        "content_type": "product",
        "content_id": "1077218",
        "content_name": "socks",
        "content_category": "Men's cloth"
      },
      {
        "price": 30,
        "quantity": 1,
        "content_type": "product",
        "content_id": "1197218",
        "content_name": "Nike Air Jordan 1",
        "content_category": "Men's shoes"
      }
    ],
    "event_channel": "in_store",
    "currency": "USD",
    "value": 46.00
  }
}
'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Response code. For the complete list of response codes and descriptions, see [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | The log id of a request, which uniquely identifies the request. |
| data | object | Error details. |

### Ví dụ lệnh cURL (Example)

```http
// Success-Response
HTTPS/1.1 200 OK
{
    "message": "OK",
    "code": 0,
    "request_id": "2019091810032301011023224213558",
    "data":{}
}
```

# Báo cáo sự kiện Ngoại tuyến hàng loạt

Bạn có thể sử dụng điểm cuối [/v1.3/offline/batch/](../12-api-reference/43-events-1-0-p1.md#doc-1740858565852225) để báo cáo sự kiện ngoại tuyến hàng loạt nhằm giảm tải lưu lượng. Khuyến nghị gửi không quá 100 sự kiện trong một yêu cầu, với tổng dung lượng dưới 10 MB.

## Yêu cầu gọi API (Request)

**Địa chỉ (Address):** https://business-api.tiktok.com/open_api/v1.3/offline/batch/

**Method** POST

**Request header**

| Field | Data Type | Desciption |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type  ****(Bắt buộc)**** | string | Định dạng dữ liệu yêu cầu. ⏎ Allowed format: `"application/json"`. |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết | Examples |
|---|---|---|---|
| event_set_id ****(Bắt buộc)**** | string | Event Set ID. | 7057103914977558530 |
| batch | object[] | A list of offline events. |  |
| ↳ event  ****(Bắt buộc)**** | string | Event type. Refer to the "Supported Offline Events" section above for supported values. | Purchase |
| ↳ event_id | string | A unique value for each event. This ID can be used to match data between partner and TikTok. We suggest it is a String of 32 characters, including numeric digits (0-9), uppercase letters (A-Z), and lowercase letters (a-z). | 1616318632825_357 |
| ↳ context ****(Bắt buộc)**** | object | Dictionary of extra information that provides useful context about a message. For the data fields in this object, see the "User context object parameters" section below. | See "User context object parameters" section |
| ↳ properties ****(Bắt buộc)**** | object | Free-form dictionary of properties of the event, e.g., revenue. For the data fields in this object, see the "Properties object parameters" section below. | See "Properties object parameters" section |
| ↳ timestamp ****(Bắt buộc)**** | datetime | Timestamp that the event took place. Timestamp with [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) format. | 2019-06-12T19:11:01.152Z |

### Ví dụ lệnh cURL (Example)
> **Lưu ý:** Bạn cần thay thế dữ liệu mẫu trong ví dụ bằng dữ liệu thực tế của mình.

```HTTP
// cURL
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/offline/batch/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data-raw '{
    "event_set_id": "{{event_set_id}}",
    "batch": [{
            "event": "Purchase",
            "event_id": "{{event_id}}",
            "timestamp": "2020-09-17T19:49:27Z",
            "context": {
                "user": {
                    "phone_numbers": ["2f9d2b4df907e5c9a7b3434351b55700167b998a83dc479b825096486ffcf4ea",
                        "1e7c3b4ff108e5c9a7b3434351b55700167b998a83dc479b825096486cvvf6gt"
                    ],
                    "emails": ["dd6ff77f54e2106661089bae4d40cdb600979bf7edc9eb65c0942ba55c7c2d7f"]
                }
            },
            "properties": {
                "order_id": "abc_xyz",
                "shop_id": "123abc",
                "contents": [{
                        "price": 8,
                        "quantity": 2,
                        "content_type": "product",
                        "content_id": "1077218",
                        "content_name": "socks",
                        "content_category": "Men's cloth"
                    },
                    {
                        "price": 30,
                        "quantity": 1,
                        "content_type": "product",
                        "content_id": "1197218",
                        "content_name": "Nike Air Jordan 1",
                        "content_category": "Men's shoes"
                    }
                ],
                "event_channel": "in_store",
                "currency": "USD",
                "value": 46.00
            }
        },
        {
            "event": "Purchase",
            "event_id": "{{event_id}}",
            "timestamp": "2020-09-18T20:50:27Z",
            "context": {
                "user": {
                    "phone_numbers": ["2f9d2b4df907e5c9a7b3434351b55700167b998a83dc479b825096486ffcf4ea",
                        "1e7c3b4ff108e5c9a7b3434351b55700167b998a83dc479b825096486cvvf6gt"
                    ],
                    "emails": ["dd6ff77f54e2106661089bae4d40cdb600979bf7edc9eb65c0942ba55c7c2d7f"]
                }
            },
            "properties": {
                "order_id": "abc_xyz_2",
                "shop_id": "123abc",
                "contents": [{
                        "price": 20,
                        "quantity": 1,
                        "content_type": "product",
                        "content_id": "1077220",
                        "content_name": "Jacket",
                        "content_category": "Men's cloth"
                    },
                    {
                        "price": 100,
                        "quantity": 1,
                        "content_type": "product",
                        "content_id": "1197221",
                        "content_name": "Jeans",
                        "content_category": "Men's cloth"
                    }
                ],
                "event_channel": "in_store",
                "currency": "USD",
                "value": 120.00
            }
        }
    ]
}
'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Response code. For the complete list of response codes and descriptions, see [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | The log id of a request, which uniquely identifies the request. |
| data | object | Error details. |

### Ví dụ lệnh cURL (Example)

```http
// Success-Response
HTTPS/1.1 200 OK
{
    "message": "OK",
    "code": 0,
    "request_id": "2019091810032301011023224213558",
    "data":{}
}
```

# Tham số đối tượng ngữ cảnh người dùng (User context)
Bảng dưới đây giới thiệu các trường được hỗ trợ trong đối tượng `context`. **Bạn bắt buộc phải truyền `phone_numbers` hoặc `emails` và cung cấp ít nhất một giá trị cho trường đã chọn.**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết | Formatting | Examples |
|---|---|---|---|---|
| user ****(Bắt buộc)**** | object | The personal data of a user. |  |  |
| ↳ phone_numbers | string[] | User's phone number. ⏎ It must be hashed with SHA-256 on the client side. You must pass in either this field or `emails`. | Prior to hashing, format the phone number: • Normalize your phone numbers to E.164 format, a combination of + ［country code]［phone number]. An example of a US number in the E.164 format: +12133734253 • Recommend using [https://github.com/catamphetamine/libphonenumber-js](https://github.com/catamphetamine/libphonenumber-js) for E.164 parsing. • Only SHA-256 is accepted. Here is the recommended package: [GitHub - emn178/js-sha256: A simple SHA-256 / SHA-224 hash function for JavaScript supports UTF-8 encoding.](https://github.com/emn178/js-sha256) | ["sha256phone1","sha256phone2"] |
| ↳ emails | string[] | User's email. ⏎ It must be hashed with SHA-256 on the client side. You must pass in either this field or `phone_numbers`. | Prior to hashing, format the email: • You should lowercase all characters before hashing. • Do not perform any other types of normalization on emails prior to hashing. • Only SHA-256 is accepted. Here is the recommended package: [GitHub - emn178/js-sha256: A simple SHA-256 / SHA-224 hash function for JavaScript supports UTF-8 encoding.](https://github.com/emn178/js-sha256) | ["sha256email1", "sha256email2"] |

# Tham số đối tượng thuộc tính (Properties object)
Bảng dưới đây giới thiệu các trường được hỗ trợ trong đối tượng `properties`:

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết | Examples |
|---|---|---|---|
| order_id | string | Order ID. | abc_xyz |
| shop_id | string | Shop ID. |  |
| contents | object[] | Product or Item array. |  |
| ↳ content_name | string | Name of the product. | socks |
| ↳ content_type | string | Product or content type. | product |
| ↳ content_category | string | Product or content category. | Men's cloth |
| ↳ content_id | string | Product or content identifier. | 230222800 |
| ↳ quantity | number | Number of item. | 1 |
| ↳ price | number | Price of the product or content. | 125.05 |
| ↳ brand | string | Brand name of the product item. |  |
| currency**(Điều kiện)** | string | ISO 4217 code. Required for revenue reporting. Example: "USD". ⏎ **List of currencies currently supported:** AED, ARS, AUD, BDT, BHD, BIF, BOB, BRL, CAD, CHF, CLP, CNY, COP, CRC, CZK, DKK, DZD, EGP, EUR, GBP, GTQ, HKD, HNL, HUF, IDR, ILS, INR, ISK, JPY, KES, KHR, KRW, KWD, KZT, MAD, MOP, MXN, MYR, NGN, NIO, NOK, NZD, OMR, PEN, PHP, PHP, PKR, PLN, PYG, QAR, RON, RUB, SAR, SEK, SGD, THB, TRY, TWD, UAH, USD, VES, VND, ZAR. | USD |
| value**(Điều kiện)** | number | Revenue of total contents. Required for revenue reporting. | 125.05 |
| event_channel | string | Event channel. Các giá trị enum hỗ trợ: • email • website • phone_call •  in_store • crm • other | in_store |

---

<a id="doc-1739585434183746"></a>
<!-- doc_id: 1739585434183746 -->
<!-- doc_id: 1739585434183746 -->
# Cài đặt SDK trên Android (Android installation)
> Đường dẫn: Marketing API > Ad Measurement > Guides > TikTok App Events SDK > Getting started > Android installation
> **Important:** 
> **Quan trọng:** Việc sử dụng TikTok App Events SDK tuân theo [Điều khoản Dịch vụ Thương mại TikTok For Business](https://ads.tiktok.com/i18n/official/policy/commercial-terms-of-service). Bằng việc sử dụng SDK, bạn cũng đồng ý với [Điều khoản sản phẩm thương mại TikTok (Dữ liệu)](https://ads.tiktok.com/i18n/official/policy/business-products-terms) và cam kết không chia sẻ dữ liệu nhạy cảm với TikTok.

TikTok App Events SDK dành cho Android được duy trì tại [kho lưu trữ GitHub công khai](https://github.com/tiktok/tiktok-business-android-sdk).
## Prerequisites
Trước khi bắt đầu, hãy đảm bảo bạn đã chuẩn bị các thông tin sau từ tài khoản TikTok For Business:
- **App ID** ứng dụng Android của bạn (ví dụ: `com.example.app`). Đây là tên package của ứng dụng.
- **TikTok App ID** lấy từ trang cài đặt ứng dụng trong Trình quản lý sự kiện.
- **App Secret** phục vụ việc xác thực bảo mật.
Nếu bạn chưa có các thông tin này, hãy tham khảo [Bắt đầu](do-luong-quang-cao-p1.md#doc-1862119945765889) trước khi tiếp tục.

## Thêm SDK làm phần phụ thuộc bản dựng (Build dependency)
### Tích hợp qua Maven (Khuyến nghị)
1. Trong tệp `build.gradle` cấp dự án, đảm bảo `mavenCentral()`, `google()` và `jitpack.io` được khai báo trong khối `repositories`.
```http
// curl
// project/build.gradle
allprojects {
    repositories {
        google()
        mavenCentral()
        maven { url 'https://jitpack.io' }
    }
}
```

2. Trong tệp `build.gradle` cấp ứng dụng (app-level), thêm các phần phụ thuộc implementation cho TikTok SDK và các thư viện liên quan.
```http
// curl
// app/build.gradle
android {
  compileOptions {
    sourceCompatibility JavaVersion.VERSION_1_8
    targetCompatibility JavaVersion.VERSION_1_8
  }
}

dependencies {
    // TikTok App Events SDK
    implementation 'com.github.tiktok:tiktok-business-android-sdk:1.7.0'

    // Required for automatic event reporting and lifecycle tracking
    implementation 'androidx.lifecycle:lifecycle-process:2.3.1'
    implementation 'androidx.lifecycle:lifecycle-common-java8:2.3.1'

    // Required for automatic in-app purchase reporting
    implementation 'com.android.billingclient:billing:6.1.0'

    // Required for Play Store install referrer attribution
    implementation 'com.android.installreferrer:installreferrer:2.2'
}
```

### Tích hợp thủ công (Manual integration)
1. Tải xuống tệp nhị phân `.aar` từ [bản phát hành GitHub mới nhất](https://github.com/tiktok/tiktok-business-android-sdk/releases/latest/).
2. Tạo thư mục `libs` trong module ứng dụng của bạn (ví dụ: `app/libs`) nếu chưa tồn tại.
3. Sao chép tệp `.aar` đã tải xuống vào thư mục `app/libs`.
4. Thêm các phần phụ thuộc vào tệp `build.gradle` cấp ứng dụng của bạn.
```http
// curl
// app/build.gradle
android {
  compileOptions {
    sourceCompatibility JavaVersion.VERSION_1_8
    targetCompatibility JavaVersion.VERSION_1_8
  }
}

dependencies {
    // TikTok App Events SDK (Manual)
    implementation files('libs/tiktok-business-android-sdk-1.6.1.aar') // Ensure the filename matches

    // Add the same required libraries as in the Maven setup
    implementation 'androidx.lifecycle:lifecycle-process:2.3.1'
    implementation 'androidx.lifecycle:lifecycle-common-java8:2.3.1'
    implementation 'com.android.billingclient:billing:6.1.0'
    implementation 'com.android.installreferrer:installreferrer:2.2'
}
```

### Khai báo quyền (Permissions)
Trong tệp `AndroidManifest.xml`, hãy khai báo các quyền `INTERNET` và `AD_ID`.
```http
// curl
<!-- AndroidManifest.xml -->
<manifest ...>
    <uses-permission android:name="android.permission.INTERNET" />
    <!-- Required for advertising and analytics purposes on Android 13+ -->
    <uses-permission android:name="com.google.android.gms.permission.AD_ID" />

    <application ...>
        ...
    </application>
</manifest>
```

### Cấu hình làm mờ mã Proguard
Để tránh việc SDK bị loại bỏ hoặc lỗi trong các bản dựng phát hành (release builds), hãy thêm các quy tắc sau vào tệp `proguard-rules.pro` của bạn:
```http
// curl
# proguard-rules.pro

# TikTok SDK
-keep class com.tiktok.** { *; }

# Google Play Billing Library
-keep class com.android.billingclient.api.** { *; }

# Google Install Referrer
-keep class com.android.installreferrer.api.** { *; }

# Android Lifecycle
-keep class androidx.lifecycle.** { *; }
```

## Cấu hình và khởi tạo SDK
Trong lớp `Application` của bạn, tạo một phiên bản `TTConfig` với App Secret, App ID và (các) TikTok App ID từ Trình quản lý sự kiện. Sau đó, gọi `TikTokBusinessSdk.initializeSdk` để khởi động SDK. Khuyến nghị sử dụng completion handler để xử lý kết quả thành công hoặc thất bại.
> **Important:** 
> **Lưu ý:** SDK chỉ hỗ trợ khởi tạo và sử dụng trong tiến trình chính và luồng chính. Trong lần khởi tạo đầu tiên, SDK cũng sẽ lấy User Agent của thiết bị qua WebView. Để tránh xung đột khóa (lock conflict), vui lòng chỉ sử dụng WebView sau khi khởi tạo thành công.

> **Note:** 
> **Xử lý nhiều TikTok App ID**
> Nếu làm việc với nhiều Tài khoản quảng cáo, bạn có thể cung cấp chuỗi các TikTok App ID phân tách bằng dấu phẩy. Đảm bảo chuỗi không chứa dấu cách và không kết thúc bằng dấu phẩy. SDK sẽ không khởi tạo nếu có sự không khớp giữa App ID và (các) TikTok App ID.

```http
// curl
// YourApplicationClass.java
import com.tiktok.TikTokBusinessSdk;
import com.tiktok.TikTokBusinessSdk.TTConfig;

public class YourApplicationClass extends Application {
    @Override
    public void onCreate() {
        super.onCreate();

        TTConfig ttConfig = new TTConfig(getApplicationContext(), "YOUR_APP_SECRET")
            .setAppId("YOUR_APP_ID") // Your app's package name, e.g., com.example.app
            .setTTAppId("YOUR_TIKTOK_APP_ID");
            
        // For multiple TikTok App IDs:
        // TTConfig ttConfig = new TTConfig(getApplicationContext(), "YOUR_APP_SECRET")
        //    .setAppId("YOUR_APP_ID") // Your app's package name, e.g., com.example.app
        //    .setTTAppId("TIKTOK_APP_ID1,TIKTOK_APP_ID2,TIKTOK_APP_ID3");
        
        // Continue to initialisation...
        TikTokBusinessSdk.initializeSdk(ttConfig, new TikTokBusinessSdk.TTInitCallback() {
            @Override
            public void success() {
                // SDK initialized successfully
            }
            @Override
            public void fail(int code, String msg) {
                // SDK initialisation failed
            }
        });
    }
}
```

### Trì hoãn truyền phát sự kiện
Khi tích hợp TikTok App Events SDK, khách hàng có thể cần cấu hình SDK để trì hoãn việc truyền dữ liệu và thu thập sự kiện theo các quy định pháp lý của từng khu vực. TikTok cung cấp các tài nguyên hỗ trợ tuân thủ và có thể tích hợp theo hướng dẫn tại [Chia sẻ dữ liệu sau khi người dùng đồng ý](do-luong-quang-cao-tom-tat.md#doc-1824048384831554).

## Báo cáo sự kiện ứng dụng
### Các sự kiện được ghi tự động
SDK tự động ghi nhật ký các sự kiện sau nếu chúng không bị vô hiệu hóa trong khi cấu hình:

| Event | Description |
|---|---|
| `InstallApp` | First-time app launch after installation. ⏎ You may notice an increase in reported install events when the SDK is integrated for the first time. This is expected, as installs are measured based on the first detectable app launch by the SDK. If this is a concern, allow a few days for your existing user base to update their apps before running paid campaigns. |
| `LaunchAPP` | On every app launch. |
| `2DRetention` | App is opened the day after the first app launch. |
| `Purchase` | A successful transaction is completed via the Google Play Billing Library. Non-Google Play transactions must be logged manually. |

Bạn có tùy chọn tắt tính năng tự động ghi nhật ký sự kiện. Tắt tính năng này đồng nghĩa với việc các sự kiện như cài đặt ứng dụng và khởi chạy ứng dụng sẽ không còn được theo dõi tự động theo mặc định. Nếu cần các sự kiện này cho mục đích đo lường, bạn phải triển khai ghi nhật ký thủ công trong mã nguồn.
```http
// curl
TTConfig ttConfig = new TTConfig(getApplicationContext(), "YOUR_APP_SECRET")
    // ... other configurations

    // Option 1: Disable ALL automatic events (Install, Launch, 2DRetention, Purchase)
    .disableAutoEvents()

    // Option 2: Disable specific automatic events
    .disableInstallLogging() // Disable install reporting only
    .disableLaunchLogging() // Disable automatic app launch reporting only
    .disableRetentionLogging() // Disable automatic 2DRetention reporting only
    .disableAutoIapTrack() // Disable automatic Purchase reporting only
    
TikTokBusinessSdk.initializeSdk(ttConfig);
```

### Các sự kiện ghi thủ công
#### Các sự kiện tiêu chuẩn (Standard events)
Đối với các sự kiện đơn giản không có thuộc tính, sử dụng `trackTTEvent()` với hằng số sự kiện từ enum `EventName`. Để xem danh sách đầy đủ các enum `EventName`, hãy tham khảo [Hằng số và lớp sự kiện chuẩn](https://business-api.tiktok.com/portal/docs/standard-event-constants-and-classes).

**Ví dụ:** Sự kiện **`Registration`**
```http
// curl
// Example: Track a user registration
TikTokBusinessSdk.trackTTEvent(EventName.REGISTRATION);
```

#### Thêm thuộc tính vào sự kiện tiêu chuẩn
Đối với các sự kiện bao gồm chi tiết về sản phẩm hoặc giá trị, sử dụng lớp builder `TTContentsEvent` cho các sự kiện tiêu chuẩn sau, và `TTBaseEvent` cho tất cả các sự kiện tiêu chuẩn khác:

| Standard event ⏎ | Builder class ⏎ |
|---|---|
| Add to Cart | `TTAddToCartEvent` |
| Add to Wishlist | `TTAddToWishlistEvent` |
| Checkout | `TTCheckoutEvent` |
| Purchase | `TTPurchaseEvent` |
| View Content | `TTViewContentEvent` |

**Ví dụ:** **Lớp builder cho sự kiện `ViewContent`**
```http
// curl
// Example: A user views a product
TTContentsEvent viewContentEvent = TTViewContentEvent.newBuilder()
    .setContentType("sku")
    .setCurrency(Currency.USD)
    .setValue(99.99)
    .setDescription("A fantastic product")
    .setContents(TTContentParams.newBuilder()
        .setPrice(99.99f)
        .setQuantity(1)
        .setContentId("12345")
        .setContentCategory("Electronics")
        .setContentName("Wireless Headphones")
        .setBrand("AudioBrand")
        .build())
    .build();

TikTokBusinessSdk.trackTTEvent(viewContentEvent);
```

**Ví dụ:** Sự kiện **`CompleteTutorial`**

Đối với các sự kiện tiêu chuẩn khác có thuộc tính chuẩn, sử dụng builder `TTBaseEvent` với hằng số từ enum `EventName`.

```http
// curl
// Example: A user completes the onboarding tutorial
TTBaseEvent tutorialEvent = TTBaseEvent.newBuilder(EventName.COMPLETE_TUTORIAL)
    .addProperty("currency", "<currency>") // The ISO 4217 currency code
    .addProperty("value", "<value>") // Value of the order or items sold
    .addProperty("content_id", "<content id value>") // Unique ID of the product or content
    .addProperty("content_type", "<content type value>") // The type of content in the event
    .addProperty("price", "<price>") // The price of the item
    .addProperty("quantity", "<quantity>") // The number of items
    .build();

TikTokBusinessSdk.trackTTEvent(tutorialEvent);
```

> **Note:** 
> Để xem danh sách đầy đủ các thuộc tính tiêu chuẩn được hỗ trợ, hãy tham khảo [Tài liệu tham khảo đối tượng Properties](https://business-api.tiktok.com/portal/docs/setup-guide-for-app/v1.3#item-link-properties%20parameters). Các khóa thuộc tính tùy chỉnh không được hỗ trợ và sẽ bị loại bỏ.

#### Doanh thu quảng cáo trong ứng dụng (In-app ad revenue)
Bắt đầu từ phiên bản SDK 1.5.0, dữ liệu doanh thu hòa giải quảng cáo trong ứng dụng có thể được báo cáo bằng `TTAdRevenueEvent`. Tham khảo [Báo cáo doanh thu quảng cáo trong ứng dụng](do-luong-quang-cao-tom-tat.md#doc-1862351923536898) để biết hướng dẫn triển khai chi tiết cho AppLovin Max, ironSource và Google AdMob.
#### Các sự kiện tùy chỉnh (Custom events)
Để theo dõi một sự kiện không nằm trong danh sách sự kiện tiêu chuẩn, sử dụng builder `TTBaseEvent` với chuỗi tên sự kiện tùy chỉnh.
```http
// curl
// Example: A user shares content to a social platform
TTBaseEvent customEvent = TTBaseEvent.newBuilder("ShareContent")
    .build();

TikTokBusinessSdk.trackTTEvent(customEvent);
```

## Bật Khớp nâng cao (Advanced Matching)
Để cải thiện khả năng so khớp tệp đối tượng, sử dụng `identify()` để thiết lập các thuộc tính khớp nâng cao khi có thông tin người dùng (ví dụ: đăng nhập, đăng ký), và `logout()` để xóa thông tin khi đăng xuất.
```http
// curl
// When user logs in or signs up
TikTokBusinessSdk.identify(
    "user-external-id-123",  // externalId
    "user-name-456",         // externalUserName
    "+15551234567",         // phoneNumber (E.164 format)
    "user@example.com"     // email
);

// When user logs out
TikTokBusinessSdk.logout();
```

## Xác minh tích hợp của bạn
Sử dụng TikTok Events Manager để xác minh các sự kiện được tiếp nhận chính xác. Thao tác này sẽ gửi các sự kiện đến một điểm cuối riêng biệt phục vụ thử nghiệm và không làm ảnh hưởng đến dữ liệu sản xuất của bạn.
### Sự kiện kiểm tra không cần viết mã (Khuyến nghị)
Phương pháp này cho phép gỡ lỗi sự kiện trên từng thiết bị cụ thể mà không cần sửa mã. Trước khi bắt đầu, hãy đảm bảo rằng:
- Phiên bản mới nhất của ứng dụng TikTok đã được cài đặt trên thiết bị của bạn
- Ứng dụng của bạn đang tích hợp SDK phiên bản 1.5.0 trở lên
- Bạn đã cấp quyền Mã định danh quảng cáo (Advertising ID) cho cả ứng dụng của bạn và ứng dụng TikTok.

| Step | Instructions |
|---|---|
| Generate QR Code | • In **Events Manager** for your app, go to the **Test Events** tab. • Click **Generate QR code**. A QR code is generated, valid for 24 hours. • To force expiry before the 24 hours is over, click **Disable code**. |
| Bind Device | • Open the TikTok app on your test device and go to your **Profile**. • Tap the menu icon (☰) in the top right, then select **My QR code**. • Tap the scan icon in the top right and scan the QR code from Events Manager. • Tap **Authorize** to bind your device and enable test mode. |
| Verify Events | • Trigger events in your app. They will appear in the **Test Event** tab in real-time. • If you configured multiple TikTok App IDs, test events will only appear in the Events Manager for the **first** ID in the list. |

### Chế độ gỡ lỗi thủ công (Manual debug mode)
> **Important:** 
> Lưu ý: Hãy nhớ tắt chế độ gỡ lỗi thủ công và nhật ký chi tiết trước khi phát hành ứng dụng ra môi trường sản xuất. Các sự kiện kiểm tra sẽ bị loại bỏ và không được dùng cho báo cáo chiến dịch.

#### Bật chế độ gỡ lỗi
SDK phải được khởi tạo ở chế độ gỡ lỗi để tất cả sự kiện phát sinh được đánh dấu là sự kiện kiểm tra. Để làm điều đó, hãy thêm `enableDebugMode()` vào `TTConfig` trong quá trình khởi tạo. Bạn cũng có thể dùng `setLogLevel()` để có đầu ra nhật ký chi tiết hơn.

```http
// curl
TTConfig ttConfig = new TTConfig(getApplicationContext(), "YOUR_APP_SECRET")
    .setAppId("YOUR_APP_ID")
    .setTTAppId("YOUR_TIKTOK_APP_ID")
    .openDebugMode() // Enable debug mode
    .setLogLevel(TikTokBusinessSdk.LogLevel.DEBUG) // Enable logging

TikTokBusinessSdk.initializeSdk(ttConfig);
```

Các cấp độ ghi nhật ký khả dụng gồm:
- `NONE`: No logging.
- `INFO`: Ghi lại các thông điệp thông tin và ngoại lệ.
- `WARN`: Ghi lại các cảnh báo và ngoại lệ.
- `DEBUG`: Ghi lại đầu ra gỡ lỗi chi tiết, ngoại lệ và thông điệp.
#### Tắt chế độ gỡ lỗi
Sau khi xác minh tích hợp thành công, hãy xóa mọi lệnh gọi `openDebugMode()` và `setLogLevel()` trước khi xuất bản ứng dụng.
```http
// curl
// REMOVEME
// ttConfig.openDebugMode()
// ttConfig.setLogLevel(TikTokBusinessSdk.LogLevel.DEBUG)
```

### Tạo và xác minh sự kiện
Sau khi bật chế độ gỡ lỗi, hãy chạy ứng dụng và kích hoạt một số sự kiện. Bạn có thể xem các sự kiện đến theo thời gian thực dưới tab **Sự kiện kiểm tra (Test Event)** trên trang Trình quản lý sự kiện của ứng dụng.

Nếu có nhiều TikTok App ID trong cấu hình SDK, các sự kiện kiểm tra sẽ chỉ hiển thị trong tài khoản quảng cáo liên kết với TikTok App ID **đầu tiên** trong chuỗi cấu hình.

![Sự kiện kiểm tra](https://images.ctfassets.net/5jqet0ab9qci/5YdxHoZ7YOJu6AnrhCHSwH/abdc782a025d645abbe91e463039e05b/Test_event.png)

## Các tính năng bổ sung và hướng dẫn
- [Deeplink và deferred deeplink](do-luong-quang-cao-p2.md#doc-1862348999629826)
- [Tăng cường postback dữ liệu](do-luong-quang-cao-p2.md#doc-1862351781303361)
- [Báo cáo doanh thu quảng cáo trong ứng dụng](do-luong-quang-cao-tom-tat.md#doc-1862351923536898)
- [Các phương pháp tuân thủ tốt nhất](do-luong-quang-cao-p2.md#doc-1862352195035138)

---

<a id="doc-1739585432134657"></a>
<!-- doc_id: 1739585432134657 -->
<!-- doc_id: 1739585432134657 -->
# Cài đặt SDK trên iOS (iOS installation)
> Đường dẫn: Marketing API > Ad Measurement > Guides > TikTok App Events SDK > Getting started > iOS installation
> **Important:** 
> **Quan trọng:** Việc sử dụng TikTok App Events SDK tuân theo [Điều khoản Dịch vụ Thương mại TikTok For Business](https://ads.tiktok.com/i18n/official/policy/commercial-terms-of-service). Bằng việc sử dụng SDK, bạn cũng đồng ý với [Điều khoản sản phẩm thương mại TikTok (Dữ liệu)](https://ads.tiktok.com/i18n/official/policy/business-products-terms) và cam kết không chia sẻ dữ liệu nhạy cảm với TikTok.

TikTok App Events SDK dành cho iOS được duy trì tại [kho lưu trữ GitHub công khai](https://github.com/tiktok/tiktok-business-ios-sdk).

## Prerequisites
Trước khi bắt đầu, hãy đảm bảo bạn đã chuẩn bị các thông tin sau từ tài khoản TikTok For Business:
- **App ID** ứng dụng Apple của bạn (ví dụ: `123456789`). Đây là ID chuỗi số trên Apple App Store.
- **TikTok App ID** lấy từ trang cài đặt ứng dụng trong Trình quản lý sự kiện.
- **App Secret** phục vụ việc xác thực bảo mật.
Nếu bạn chưa có các thông tin này, hãy tham khảo [Bắt đầu](do-luong-quang-cao-p1.md#doc-1862119945765889) trước khi tiếp tục.

## Thêm SDK làm phần phụ thuộc bản dựng (Build dependency)
### Tích hợp qua CocoaPods
1. Trong tệp `Podfile` của bạn, thêm pod `TikTokBusinessSDK`:
```http
// curl
# Podfile
pod 'TikTokBusinessSDK'
```

2. Cài đặt pod bằng cách chạy lệnh sau trong thư mục dự án của bạn:
```http
// curl
pod install
```

### Tích hợp qua Swift Package Manager (SPM)
Chúng tôi hỗ trợ Swift Package Manager từ phiên bản 1.3.8 trở lên.

1. Trong Xcode, vào **File → Add Package Dependencies**

![Thêm gói phụ thuộc](https://images.ctfassets.net/5jqet0ab9qci/5ijuHmAnshPT1jsmie8tVt/5aa0c6d0b75c6ae02cd4d02ab02945c9/Add_Package_Dependencies.png)

2. Nhập URL kho lưu trữ GitHub của TikTokBusinessSDK vào ô tìm kiếm: https://github.com/tiktok/tiktok-business-ios-sdk

![Nhập URL kho lưu trữ GitHub TikTokBusinessSDK](https://images.ctfassets.net/5jqet0ab9qci/5iknJZKfU3shqkhtvKyce9/77ea2db6d2fdbd846c7e0968b9710833/Enter_the_TikTokBusinessSDK_GitHub_repository_URL.png)

3. Chọn phiên bản SDK mong muốn và thêm vào target dự án tương ứng

4. Chọn **Add Package** để hoàn tất việc thêm SDK vào dự án của bạn.

![Thêm gói](https://images.ctfassets.net/5jqet0ab9qci/6bF0RtxIFScMcnA2ix3DNq/dc48723c25edb817f3333634ec0f6b8c/Add_Package.png)

### Tích hợp thủ công (Manual integration) (xcframework)
1. Tải xuống tệp `TikTokBusinessSDK.xcframework.zip` mới nhất từ [trang phát hành GitHub](https://github.com/tiktok/tiktok-business-ios-sdk/releases/latest).
2. Giải nén tệp đã tải xuống.
3. Trong Xcode, điều hướng đến cài đặt dự án, chọn app target và chuyển sang tab **General**.
4. Kéo và thả `TikTokBusinessSDK.xcframework` vào phần **Frameworks, Libraries, and Embedded Content**.
### Cấu hình cài đặt bản dựng (Build settings)
Trong mục **Build Settings** của app target trong Xcode, tìm **Other Linker Flags** và thêm `-ObjC` cùng `-lc++`.

### Cấu hình App Tracking Transparency (ATT)
Bắt đầu từ iOS 14.5, bạn phải yêu cầu người dùng đồng ý để truy cập mã nhận dạng quảng cáo của thiết bị (IDFA).

1. Trong tệp `Info.plist` của bạn, thêm khóa `NSUserTrackingUsageDescription` kèm thông báo giải thích lý do bạn yêu cầu quyền theo dõi.
```http
// curl
<!-- Info.plist -->
<key>NSUserTrackingUsageDescription</key>
<string>YOUR_CUSTOM_DESCRIPTION</string>
```

2. Yêu cầu người dùng ủy quyền tại thời điểm thích hợp trong vòng đời của ứng dụng.
```http
// curl
// Swift
func requestIDFA() {
  if #available(iOS 14, *) {
    TikTokBusiness.requestTrackingAuthorizationWithCompletionHandler { status in
      // Handle authorization status
    }
  }
}
```

```http
// curl
// Objective-C
- (void)requestIDFA {
  if (@available(iOS 14, *)) {
    [TikTokBusiness requestTrackingAuthorizationWithCompletionHandler:^(NSUInteger status) {
      // Handle authorization status
    }];
  }
}
```

## Cấu hình và khởi tạo SDK
> **Important:** 
> Trong `AppDelegate`, hãy cấu hình và khởi tạo SDK bên trong phương thức `application(_:didFinishLaunchingWithOptions:)` trong giai đoạn khởi động ứng dụng và lần khởi chạy đầu tiên. Điều này cho phép SDK báo cáo các sự kiện này với độ chính xác cao nhất nhằm phân bổ thành công.

Tạo đối tượng `TikTokConfig` với App Secret, App ID và (các) TikTok App ID từ Trình quản lý sự kiện. Sau đó, gọi `TikTokBusiness.initializeSdk` để khởi động SDK. Khuyến nghị sử dụng completion handler để xử lý kết quả thành công hoặc thất bại.

> **Note:** 
> **Xử lý nhiều TikTok App ID**
> Nếu làm việc với nhiều Tài khoản quảng cáo, bạn có thể cung cấp chuỗi các TikTok App ID phân tách bằng dấu phẩy. Đảm bảo chuỗi không chứa dấu cách và không kết thúc bằng dấu phẩy. SDK sẽ không khởi tạo nếu có sự không khớp giữa App ID và (các) TikTok App ID.

```http
// curl
// Swift
// AppDelegate.swift

import TikTokBusinessSDK

@main
class AppDelegate: UIResponder, UIApplicationDelegate {

    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {

        guard let config = TikTokConfig(accessToken: "YOUR_APP_SECRET", appId: "YOUR_APP_ID", tiktokAppId: "YOUR_TIKTOK_APP_ID") else {
            return true
        }

        // For multiple TikTok App IDs:
        // guard let config = TikTokConfig(accessToken: "YOUR_APP_SECRET", appId: "YOUR_APP_ID", tiktokAppId: "TIKTOK_APP_ID1,TIKTOK_APP_ID2,TIKTOK_APP_ID3") else {
        //     return true
        // }

        // Continue to initialisation...
        TikTokBusiness.initializeSdk(config) { (success, error) in
            if success {
                print("TikTok App Events SDK initialized successfully")
            } else {
                print("TikTok App Events SDK initialisation failed: \(error?.localizedDescription ?? "Unknown error")")
            }
        }

        return true
    }
}
```

```http
// curl
// Objective-C
// AppDelegate.m

#import <TikTokBusinessSDK/TikTokBusinessSDK.h>

@implementation AppDelegate

- (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {

    TikTokConfig *config = [TikTokConfig configWithAccessToken:@"YOUR_APP_SECRET" appId:@"YOUR_APP_ID" tiktokAppId:@"YOUR_TIKTOK_APP_ID"];

    // For multiple TikTok App IDs:
    // TikTokConfig *config = [TikTokConfig configWithAccessToken:@"YOUR_APP_SECRET" appId:@"YOUR_APP_ID" tiktokAppId:@"TIKTOK_APP_ID1,TIKTOK_APP_ID2,TIKTOK_APP_ID3"];

    // Continue to initialisation...
    [TikTokBusiness initializeSdk:config completionHandler:^(BOOL success, NSError * _Nullable error) {
        if (success) {
            NSLog(@"TikTok App Events SDK initialized successfully");
        } else {
            NSLog(@"TikTok App Events SDK initialisation failed: %@", error.localizedDescription);
        }
    }];
}
```

### Cấu hình cập nhật SKAdNetwork trong ứng dụng
SDK hỗ trợ khung SKAdNetwork (SKAN) của Apple nhằm phân bổ bảo vệ quyền riêng tư. Các sự kiện được theo dõi sẽ được ánh xạ tới lược đồ SKAN đã cấu hình, và các API phù hợp của Apple sẽ được gọi để cập nhật giá trị chuyển đổi. Cần có bản đồ lược đồ (schema map) để báo cáo chính xác các giá trị chuyển đổi nhận được từ Apple. Để định cấu hình bản đồ này, hãy tham khảo [Báo cáo SKAdNetwork và ánh xạ lược đồ](do-luong-quang-cao-p2.md#doc-1862352021568001).

Đảm bảo rằng chỉ có một SDK duy nhất trong ứng dụng chịu trách nhiệm cập nhật giá trị chuyển đổi SKAN. Nếu bạn sử dụng một SDK khác (như MMP) để quản lý SKAN, bạn phải tắt tính năng hỗ trợ SKAdNetwork của TikTok SDK để tránh xung đột.

Để vô hiệu hóa, gọi `disableSKAdNetworkSupport()` trên đối tượng `TikTokConfig` trước khi khởi tạo SDK.
```http
// curl
// Swift
guard let config = TikTokConfig(accessToken: "YOUR_APP_SECRET", appId: "YOUR_APP_ID", tiktokAppId: "YOUR_TIKTOK_APP_ID") else {
    return true
}
// Add this line to disable SKAN updates
config.disableSKAdNetworkSupport()
TikTokBusiness.initializeSdk(config)
```

```http
// curl
// Objective-C
TikTokConfig *config = [TikTokConfig configWithAccessToken:@"YOUR_APP_SECRET" appId:@"YOUR_APP_ID" tiktokAppId:@"YOUR_TIKTOK_APP_ID"];
// Add this line to disable SKAN updates
[config disableSKAdNetworkSupport];
[TikTokBusiness initializeSdk:config];
```

### Trì hoãn truyền phát sự kiện
Khi tích hợp TikTok App Events SDK, khách hàng có thể cần cấu hình SDK để trì hoãn việc truyền dữ liệu và thu thập sự kiện theo các quy định pháp lý của từng khu vực. TikTok cung cấp các tài nguyên hỗ trợ tuân thủ và có thể tích hợp theo hướng dẫn tại [Chia sẻ dữ liệu sau khi người dùng đồng ý](do-luong-quang-cao-tom-tat.md#doc-1824048384831554).

## Báo cáo sự kiện ứng dụng
### Các sự kiện được ghi tự động
#### Các sự kiện tiêu chuẩn (Standard events)
SDK tự động ghi nhật ký các sự kiện sau nếu chúng không bị vô hiệu hóa trong khi cấu hình:

| Event | Description |
|---|---|
| `InstallApp` | First-time app launch after installation. ⏎ You may notice an increase in reported install events when the SDK is integrated for the first time. This is expected, as installs are measured based on the first detectable app launch by the SDK. If this is a concern, allow a few days for your existing user base to update their apps before running paid campaigns. |
| `LaunchAPP` | On every app launch. |
| `2DRetention` | App is opened the day after the first app launch. |
| `Purchase` | A successful transaction is completed via Apple's StoreKit. This includes consumable, non-consumable, and subscription purchases. |

Bạn có tùy chọn tắt tính năng ghi nhật ký sự kiện tự động. Việc tắt ghi nhật ký tự động đồng nghĩa với các sự kiện như cài đặt ứng dụng và khởi chạy ứng dụng sẽ không còn được theo dõi theo mặc định.

Nếu bạn cần các sự kiện này cho mục đích đo lường hoặc phân tích, bạn phải triển khai ghi nhật ký thủ công trong mã ứng dụng để thu thập và gửi chúng.

```http
// curl
// Swift
guard let config = TikTokConfig(accessToken: "YOUR_APP_SECRET", appId: "YOUR_APP_ID", tiktokAppId: "YOUR_TIKTOK_APP_ID") else {
    return true
}

// Option 1: Disable ALL automatic events
config.disableAutomaticTracking()

// Option 2: Disable specific automatic events
config.disableInstallTracking()
config.disableLaunchTracking()
config.disableRetentionTracking()
config.disablePaymentTracking()

TikTokBusiness.initializeSdk(config)
```

```http
// curl
// Objective-C
TikTokConfig *config = [TikTokConfig configWithAccessToken:@"YOUR_APP_SECRET" appId:@"YOUR_APP_ID" tiktokAppId:@"YOUR_TIKTOK_APP_ID"];

// Option 1: Disable ALL automatic events
[config disableAutomaticTracking];

// Option 2: Disable specific automatic events
[config disableInstallTracking];
[config disableLaunchTracking];
[config disableRetentionTracking];
[config disablePaymentTracking];

[TikTokBusiness initializeSdk:config];
```

#### Về việc báo cáo giao dịch StoreKit
> **Note:** 
> Từ phiên bản SDK 1.7.2, các giao dịch StoreKit chưa hoàn tất sẽ không được SDK báo cáo.

Các giao dịch mua trong ứng dụng được xử lý qua API StoreKit của Apple sẽ tự động được SDK ghi nhật ký và báo cáo dưới dạng sự kiện `Purchase`. Bảng bên dưới phác thảo các loại sản phẩm được báo cáo tự động:

| In-app product type | StoreKit 1 | StoreKit 2 |
|---|---|---|
| Consumables: An item that can be purchased, consumed and purchased again, if needed. Examples include e-commerce items, gaming items like coins, etc. | ✅ | ❌ |
| Non-Consumables: An item that can only be purchased once and remains with the user for posterity. Examples are a gaming level upgrade or a one-time app purchase. | ✅ | ✅ |
| Auto-Renewing Subscriptions: An item that can be subscribed to on a recurring basis and whose recurring payments are processed automatically. Examples are a dating app subscription or streaming service subscription. | ✅ | ✅ |
| Non-Renewing Subscriptions: An item that can be subscribed to for a fixed period and whose payments are processed only once for that period. Subscribing to this item again after a year would require another purchase. | ✅ | ✅ |

Để tự động ghi nhật ký sự kiện cho các sản phẩm tiêu hao (consumable) được mua qua StoreKit 2, hãy thêm khóa `SKIncludeConsumableInAppPurchaseHistory` vào tệp `Info.plist` của ứng dụng và đặt thành `true`.

```http
// curl
<!-- Info.plist -->
<key>SKIncludeConsumableInAppPurchaseHistory</key>
<true/>
```

SDK cũng tự động ghi nhật ký và báo cáo riêng biệt các trạng thái giao dịch khác nhau:

| StoreKit transaction state | Logged as | StoreKit 1 | StoreKit 2 |
|---|---|---|---|
| Purchasing | Purchasing | ✅ | ❌ |
| Purchased | Purchase | ✅ | ✅ |
| Restored | PurchaseRestored | ✅ | ✅ |
| Failed | PurchaseFailed | ✅ | ❌ |
| Deferred | PurchaseDeferred | ✅ | ❌ |

Các lần mua không thành công không được tự động theo dõi trong StoreKit 2. Để báo cáo tùy chọn các lỗi này, hãy gọi `trackStoreKit2PurchaseFailed` từ luồng giao dịch StoreKit 2 của bạn:

```http
// curl
// Swift
func purchaseProduct(_ productId: String) async throws {
    let products = try await Product.products(for: [productId])
    guard let product = products.first else {
        return
    }
    do {
        let result = try await product.purchase()
        switch result {
        case .success(let verifiedTransaction):
            // Handle successful purchase.
        case .pending:
            // Handle pending purchase.
        default:
            TikTokBusiness.getInstance().trackStoreKit2PurchaseFailed(productId: product.id)
        }
    } catch {
        TikTokBusiness.getInstance().trackStoreKit2PurchaseFailed(productId: product.id)
        throw error
    }
}
```

### Các sự kiện ghi thủ công
#### Các sự kiện tiêu chuẩn (Standard events)
Đối với các sự kiện đơn giản không có thuộc tính, tạo một `TikTokBaseEvent` với hằng số sự kiện từ enum `TTEventName`. Để xem danh sách đầy đủ các enum `TTEventName`, hãy tham khảo [Hằng số sự kiện tiêu chuẩn và các lớp](do-luong-quang-cao-p2.md#doc-1862287695864834).

**Ví dụ:** Sự kiện **`Registration`**
```http
// curl
// Swift
let registrationEvent = TikTokBaseEvent(eventName: TTEventName.registration.rawValue)
TikTokBusiness.trackTTEvent(registrationEvent)
```

```http
// curl
// Objective-C
TikTokBaseEvent *registrationEvent = [TikTokBaseEvent eventWithName:TTEventNameRegistration];
[TikTokBusiness trackTTEvent:registrationEvent];
```

#### Thêm thuộc tính vào sự kiện tiêu chuẩn
Đối với các sự kiện có chi tiết sản phẩm hoặc giá trị, sử dụng lớp builder `TikTokContentsEvent` cho các sự kiện tiêu chuẩn sau, và `TikTokBaseEvent` cho tất cả sự kiện tiêu chuẩn khác:

| Standard event | Builder Class |
|---|---|
| Add to Cart | `TikTokAddToCartEvent` |
| Add to Wishlist | `TikTokAddToWishlistEvent` |
| Checkout | `TikTokCheckoutEvent` |
| Purchase | `TikTokPurchaseEvent` |
| View Content | `TikTokViewContentEvent` |

**Ví dụ:** **Lớp builder cho sự kiện `ViewContent`**
```http
// curl
// Swift
// Example: A user views a product
let contentParams = TikTokContentParams()
contentParams.price = 99.99
contentParams.quantity = 1
contentParams.contentId = "12345"
contentParams.contentCategory = "Electronics"
contentParams.contentName = "Wireless Headphones"
contentParams.brand = "AudioBrand"

let viewContentEvent: TikTokContentsEvent = TikTokViewContentEvent()
viewContentEvent.setValue("99.99")
viewContentEvent.setCurrency(TTCurrency.USD)
viewContentEvent.setDescription("A fantastic product")
viewContentEvent.setContentType("product_group")
viewContentEvent.setContents([contentParams])

TikTokBusiness.trackTTEvent(viewContentEvent)
```

```http
// curl
// Objective-C
// Example: A user views a product
TikTokContentParams *contentParams = [[TikTokContentParams alloc] init];
contentParams.price = @(99.99);
contentParams.quantity = 1;
contentParams.contentId = @"12345";
contentParams.contentCategory = @"Electronics";
contentParams.contentName = @"Wireless Headphones";
contentParams.brand = @"AudioBrand";

TikTokViewContentEvent *viewContentEvent = [[TikTokViewContentEvent alloc] init];
[viewContentEvent setValue:@"99.99"];
[viewContentEvent setCurrency:TTCurrencyUSD];
[viewContentEvent setDescription:@"A fantastic product"];
[viewContentEvent setContentType:@"product_group"];
[viewContentEvent setContents:@[contentParams]];

[TikTokBusiness trackTTEvent:viewContentEvent];
```

**Ví dụ:** Sự kiện **`CompleteTutorial`**

Đối với các sự kiện tiêu chuẩn khác có thuộc tính tiêu chuẩn, sử dụng trình dựng `TikTokBaseEvent` với hằng số từ enum `TTEventName`.
```http
// curl
// Swift
// Example: A user completes the onboarding tutorial
let tutorialEvent = TikTokBaseEvent(eventName: TTEventName.completeTutorial.rawValue)
tutorialEvent.addProperty(withKey: "currency", value: TTCurrency.USD) // ISO 4217 currency code
tutorialEvent.addProperty(withKey: "value", value: 9.99) // Order or items value
tutorialEvent.addProperty(withKey: "content_id", value: "CONTENT_ID") // Unique product/content ID
tutorialEvent.addProperty(withKey: "content_type", value: "CONTENT_TYPE") // Type of content
tutorialEvent.addProperty(withKey: "price", value: 9.99) // Item price
tutorialEvent.addProperty(withKey: "quantity", value: 1) // Number of items
TikTokBusiness.trackTTEvent(tutorialEvent)
```

```http
// curl
// Objective‑C
// Example: A user completes the onboarding tutorial
TikTokBaseEvent *tutorialEvent = [TikTokBaseEvent eventWithName:TTEventNameCompleteTutorial];
[tutorialEvent addPropertyWithKey:@"currency" value:TTCurrencyUSD]; // ISO 4217 currency code
[tutorialEvent addPropertyWithKey:@"value" value:@(9.99)]; // Order or items value
[tutorialEvent addPropertyWithKey:@"content_id" value:@"CONTENT_ID"]; // Unique product/content ID
[tutorialEvent addPropertyWithKey:@"content_type" value:@"CONTENT_TYPE"]; // Type of content
[tutorialEvent addPropertyWithKey:@"price" value:@(9.99)]; // Item price
[tutorialEvent addPropertyWithKey:@"quantity" value:@(1)]; // Number of items
[TikTokBusiness trackTTEvent:tutorialEvent];
```

> **Note:** 
> Để xem danh sách đầy đủ các thuộc tính tiêu chuẩn được hỗ trợ, hãy tham khảo [Tài liệu tham khảo đối tượng Properties](https://business-api.tiktok.com/portal/docs/setup-guide-for-app/v1.3#item-link-properties%20parameters). Các khóa thuộc tính tùy chỉnh không được hỗ trợ và sẽ bị loại bỏ.

#### Doanh thu quảng cáo trong ứng dụng (In-app ad revenue)
Bắt đầu từ SDK phiên bản 1.5.0, dữ liệu doanh thu qua trung gian quảng cáo trong ứng dụng có thể được báo cáo bằng `TikTokAdRevenueEvent`. Tham khảo [Báo cáo doanh thu quảng cáo trong ứng dụng](do-luong-quang-cao-tom-tat.md#doc-1862351923536898) để biết hướng dẫn triển khai chi tiết cho AppLovin Max, ironSource và Google AdMob.
#### Các sự kiện tùy chỉnh (Custom events)
Để theo dõi một sự kiện không có trong danh sách sự kiện tiêu chuẩn, sử dụng `TikTokBaseEvent` với chuỗi tên sự kiện tùy chỉnh.
```http
// curl
// Swift
// Example: A user shares content to a social platform
let customEvent = TikTokBaseEvent(eventName: "ShareContent")
TikTokBusiness.trackTTEvent(customEvent)
```

```http
// curl
// Objective-C
// Example: A user shares content to a social platform
TikTokBaseEvent *customEvent = [TikTokBaseEvent eventWithName:@"ShareContent"];
[TikTokBusiness trackTTEvent:customEvent];
```

## Bật Khớp nâng cao (Advanced Matching)
Để cải thiện khả năng khớp đối tượng, sử dụng `identify()` để thiết lập các thuộc tính So khớp nâng cao khi có thông tin người dùng (ví dụ: sau khi đăng nhập hoặc đăng ký), và gọi `logout()` để xóa thông tin này.
```http
// curl
// Swift
// When user logs in or signs up
TikTokBusiness.identify(
    withExternalID: "user-external-id-123",
    externalUserName: "user-name-456",
    phoneNumber: "+15551234567", // E.164 format
    email: "user@example.com"
)

// When user logs out
TikTokBusiness.logout()
```

```http
// curl
// Objective-C
// When user logs in or signs up
[TikTokBusiness identifyWithExternalID:@"user-external-id-123"
                      externalUserName:@"user-name-456"
                           phoneNumber:@"+15551234567" // E.164 format
                                 email:@"user@example.com"];

// When user logs out
[TikTokBusiness logout];
```

**Supported Properties**

Theo tiêu chuẩn bảo mật ngành, email và số điện thoại của khách hàng sẽ được băm bằng thuật toán SHA256 trước khi gửi đi khỏi thiết bị. TikTok đạt chứng nhận ISO 27001 tại Hoa Kỳ và Vương quốc Anh. Tìm hiểu thêm về cách thông tin này được sử dụng trong [Điều khoản sản phẩm thương mại TikTok (Dữ liệu)](https://ads.tiktok.com/i18n/official/policy/business-products-terms).

Property
Formatting Requirements
Example

externalId: Mã định danh duy nhất từ nhà quảng cáo, chẳng hạn như ID hội viên hoặc ID người dùng.
Văn bản thuần chưa băm. Cắt bỏ khoảng trắng ở đầu/cuối.
"user-id-abc"

externalUserName: Tên người dùng từ nhà quảng cáo.
Văn bản thuần chưa băm. Cắt bỏ khoảng trắng ở đầu/cuối.
"testuser"

email
Văn bản thuần chưa băm. Cắt bỏ khoảng trắng ở đầu/cuối và chuyển thành chữ thường.
"email@example.com"

phoneNumber
Văn bản thuần chưa băm. Chuẩn hóa theo định dạng E.164 (ví dụ: +[mã quốc gia][số điện thoại]).
"+15551234567"

## Xác minh tích hợp của bạn
Sử dụng TikTok Events Manager để xác minh các sự kiện được tiếp nhận chính xác. Thao tác này sẽ gửi các sự kiện đến một điểm cuối riêng biệt phục vụ thử nghiệm và không làm ảnh hưởng đến dữ liệu sản xuất của bạn.

### Sự kiện kiểm tra không cần viết mã (Khuyến nghị)
Phương pháp này cho phép gỡ lỗi sự kiện trên từng thiết bị cụ thể mà không cần sửa mã. Trước khi bắt đầu, hãy đảm bảo rằng:
- Phiên bản mới nhất của ứng dụng TikTok đã được cài đặt trên thiết bị kiểm tra của bạn.
- Ứng dụng của bạn đang tích hợp SDK phiên bản 1.5.0 trở lên
- Bạn đã cấp quyền App Tracking Transparency (ATT) cho cả ứng dụng của bạn và ứng dụng TikTok.

| Step | Instructions |
|---|---|
| Generate QR Code | • In **Events Manager** for your app, go to the **Test Events** tab. • Click **Generate QR code**. A QR code is generated, valid for 24 hours. • To force expiry before the 24 hours is over, click **Disable code**. |
| Bind Device | • Open the TikTok app on your test device and go to your **Profile**. • Tap the menu icon (☰) in the top right, then select **My QR code**. • Tap the scan icon in the top right and scan the QR code from Events Manager. • Tap **Authorize** to bind your device and enable test mode. |
| Verify Events | • Trigger events in your app. They will appear in the **Test Event** tab in real-time. • If you configured multiple TikTok App IDs, test events will only appear in the Events Manager for the **first** ID in the list. |

### Chế độ gỡ lỗi thủ công (Manual debug mode)
> **Important:** 
> Lưu ý: Hãy nhớ tắt chế độ gỡ lỗi thủ công và nhật ký chi tiết trước khi phát hành ứng dụng ra môi trường sản xuất. Các sự kiện kiểm tra sẽ bị loại bỏ và không được dùng cho báo cáo chiến dịch.

#### Bật chế độ gỡ lỗi
SDK phải được khởi tạo ở chế độ gỡ lỗi (debug mode) để tất cả các sự kiện được tạo ra được đánh dấu là sự kiện kiểm tra. Để thực hiện, thêm `enableDebugMode()` vào `TikTokConfig` trong khi khởi tạo. Bạn cũng có thể sử dụng `setLogLevel()` để xem thông tin chi tiết hơn trong bảng điều khiển Xcode.

```http
// curl
// Swift
guard let config = TikTokConfig(accessToken: "YOUR_APP_SECRET", appId: "YOUR_APP_ID", tiktokAppId: "YOUR_TIKTOK_APP_ID") else {
    return true
}
config.enableDebugMode()
config.setLogLevel(TikTokLogLevelVerbose) // Optional: for detailed logs

TikTokBusiness.initializeSdk(config)
```

```http
// curl
// Objective-C
TikTokConfig *config = [TikTokConfig configWithAccessToken:@"YOUR_APP_SECRET" appId:@"YOUR_APP_ID" tiktokAppId:@"YOUR_TIKTOK_APP_ID"];
[config enableDebugMode];
[config setLogLevel:TikTokLogLevelVerbose]; // Optional: for detailed logs

[TikTokBusiness initializeSdk:config];
```

Các cấp độ ghi nhật ký khả dụng gồm:
- `TikTokLogLevelNone`
- `TikTokLogLevelInfo`
- `TikTokLogLevelWarn`
- `TikTokLogLevelDebug`
- `TikTokLogLevelVerbose`
#### Tắt chế độ gỡ lỗi
Sau khi quá trình tích hợp được xác minh, hãy xóa các lệnh gọi `enableDebugMode()` và `setLogLevel()` trước khi gửi ứng dụng của bạn lên App Store.
```http
// curl
// Swift
// REMOVEME
// config.enableDebugMode()
// config.setLogLevel(TikTokLogLevelVerbose)
```

```http
// curl
// Objective-C
// REMOVEME
// [config enableDebugMode];
// [config setLogLevel:TikTokLogLevelVerbose];
```

### Tạo và xác minh sự kiện
Sau khi bật chế độ gỡ lỗi, hãy chạy ứng dụng và kích hoạt một số sự kiện. Bạn có thể xem các sự kiện đến theo thời gian thực dưới tab **Sự kiện kiểm tra (Test Event)** trên trang Trình quản lý sự kiện của ứng dụng.

Nếu có nhiều TikTok App ID trong cấu hình SDK, các sự kiện kiểm tra sẽ chỉ hiển thị trong tài khoản quảng cáo liên kết với TikTok App ID **đầu tiên** trong chuỗi cấu hình.

![Sự kiện kiểm tra iOS](https://images.ctfassets.net/5jqet0ab9qci/3dfGPuRElVFFmaKkD0bqxs/b245f2eb9d67b7ea91431ec1596237ba/iOS_test_events.png)

## Các tính năng bổ sung và hướng dẫn
- [Đo lường dự đoán nâng cao (Advanced Predictive Measurement)](do-luong-quang-cao-p2.md#doc-1862348642630658)
- [Deeplink và deferred deeplink](do-luong-quang-cao-p2.md#doc-1862348999629826)
- [Tăng cường postback dữ liệu](do-luong-quang-cao-p2.md#doc-1862351781303361)
- [Báo cáo doanh thu quảng cáo trong ứng dụng](do-luong-quang-cao-tom-tat.md#doc-1862351923536898)
- [Báo cáo SKAdNetwork và ánh xạ lược đồ](do-luong-quang-cao-p2.md#doc-1862352021568001)
- [Các phương pháp tuân thủ tốt nhất](do-luong-quang-cao-p2.md#doc-1862352195035138)

---

<a id="doc-1824036608950273"></a>
<!-- doc_id: 1824036608950273 -->
<!-- doc_id: 1824036608950273 -->
# Cài đặt SDK trên Unity (Unity installation)
> Đường dẫn: Marketing API > Ad Measurement > Guides > TikTok App Events SDK > Getting started > Unity installation
> **Important:** 
> **Quan trọng:** Việc sử dụng TikTok App Events SDK tuân theo [Điều khoản Dịch vụ Thương mại TikTok For Business](https://ads.tiktok.com/i18n/official/policy/commercial-terms-of-service). Bằng việc sử dụng SDK, bạn cũng đồng ý với [Điều khoản sản phẩm thương mại TikTok (Dữ liệu)](https://ads.tiktok.com/i18n/official/policy/business-products-terms) và cam kết không chia sẻ dữ liệu nhạy cảm với TikTok.

TikTok App Events SDK dành cho Unity được duy trì tại [kho lưu trữ GitHub công khai](https://github.com/tiktok/tiktok-business-unity-sdk).

## Prerequisites
Trước khi bắt đầu, hãy đảm bảo bạn đã chuẩn bị các thông tin sau từ tài khoản TikTok For Business:
- **App ID** ứng dụng Android của bạn (ví dụ: `com.example.app`). Đây là tên package của ứng dụng.
- **App ID** ứng dụng Apple của bạn (ví dụ: `123456789`). Đây là ID chuỗi số trên Apple App Store.
- Một **TikTok App ID** từ trang cài đặt ứng dụng trong Trình quản lý sự kiện, cho từng nền tảng.
- Một **App Secret** để xác minh, cho từng nền tảng.
Nếu bạn chưa có các thông tin này, hãy tham khảo [Bắt đầu](do-luong-quang-cao-p1.md#doc-1862119945765889) trước khi tiếp tục.

## Thêm SDK làm phần phụ thuộc bản dựng (Build dependency)
> **Note:** 
> **Lưu ý:** Newtonsoft Json là điều kiện tiên quyết để tích hợp TikTokBusinessSDK.unitypackage vào Unity. Tham khảo [tài liệu NuGet](https://www.nuget.org/packages/Newtonsoft.Json) để biết chi tiết về cách thêm phần phụ thuộc này.

Step
Description
Screenshot

0
Tải xuống tệp TikTokBusinessSDK.unitypackage mới nhất từ [kho lưu trữ GitHub](https://github.com/tiktok/tiktok-business-unity-sdk/).
N/A

1
Vào Assets > Import Package > Custom Package
Import Package > Custom Package" width="60%" style="color:#808080" />

2
Chọn TikTokBusinessSDK.unitypackage

3
Nhấp All, sau đó nhấp Import

Trong một số phiên bản Unity, tệp `.xcframework` có thể bị nhận dạng nhầm thành một thư mục (lỗi như Hình 1). Để khắc phục khi xuất cho iOS, hãy chọn nền tảng mong muốn cho các kiến trúc framework khác nhau trong thư mục. Trong Hình 2 và 3, thư mục kiến trúc ARM64 (`ios-arm64`) được chọn để xuất iOS trong inspector, và kiến trúc x86 (`ios-arm64_x86_64`) không được chọn.

![Lỗi tệp .xcframework](https://images.ctfassets.net/5jqet0ab9qci/5ZizDlPSBKky5N881NxXKb/e1fce559316d990d1f892e71aa957548/.xcframework_file_error.png)

![Thư mục kiến trúc ARM64 (ios-arm64) được chọn để xuất iOS](https://images.ctfassets.net/5jqet0ab9qci/39FJBkVUPeuFO0HYyRHZjc/7e85cd7f02f131df90efcefb8a111bb8/ARM64_architecture_folder__ios-arm64__is_selected_for_iOS_export.png)

![Kiến trúc x86 (ios-arm64 x86 64) không được chọn](https://images.ctfassets.net/5jqet0ab9qci/3FIwFS1Tfm1Te0AhHBjGH/354edd5176de7b9b984609dd62f10a40/x86_architecture__ios-arm64_x86_64__is_not_selected.png)

### Di chuyển sang Unity từ Android/iOS SDK gốc hiện có
Các nhà phát triển đã tích hợp SDK TikTok App Events gốc cho Android (Java, Kotlin) hoặc iOS (Swift, Objective-C) có thể chuyển sang Unity SDK bằng cách:
- Thay thế phương pháp tích hợp `TikTokBusinessSDK.xcframework` (iOS) và `tiktok-business-android-sdk` (Android) bằng `TikTokBusinessSDK.unitypackage` (Unity), và
- Thay thế mọi cấu hình gốc và giao diện cầu nối (bridge interface) hiện có bằng giao diện C# được cung cấp. Việc trộn lẫn các giao diện có thể dẫn đến xung đột mã và không được khuyến nghị hoặc hỗ trợ.

## Cấu hình và khởi tạo SDK
Trước khi hiển thị scene đầu tiên của game, hãy khởi tạo SDK càng sớm càng tốt. Khuyến nghị gọi tại thời điểm `Awake`.
> **Note:** 
> SDK chỉ hỗ trợ khởi tạo và sử dụng trong tiến trình chính và luồng chính.
> Trong lần khởi tạo đầu tiên, Android SDK sẽ lấy User Agent của thiết bị qua WebView. Để tránh xung đột khóa, vui lòng chỉ sử dụng WebView sau khi khởi tạo thành công.
> Nếu làm việc với nhiều Tài khoản quảng cáo, bạn có thể cung cấp chuỗi các TikTok App ID phân tách bằng dấu phẩy. Đảm bảo chuỗi không chứa dấu cách và không kết thúc bằng dấu phẩy. SDK sẽ không khởi tạo nếu có sự không khớp giữa App ID và (các) TikTok App ID.

```http
// curl
using TikTok.Business.SDK;

private void Awake()
{
    // Initialize with your iOS and Android credentials
    TikTokConfig config = new TikTokConfig(
        "YOUR_IOS_APP_SECRET", 
        "YOUR_IOS_APP_ID", 
        "YOUR_IOS_TIKTOK_APP_ID",
        "YOUR_ANDROID_APP_SECRET",
        "YOUR_ANDROID_APP_ID",
        "YOUR_ANDROID_TIKTOK_APP_ID"
    );

    // For multiple TikTok App IDs:
    // TikTokConfig config = new TikTokConfig(
    //     "YOUR_IOS_APP_SECRET", 
    //     "YOUR_IOS_APP_ID", 
    //     "IOS_TIKTOK_APP_ID_1,IOS_TIKTOK_APP_ID_2",
    //     "YOUR_ANDROID_APP_SECRET",
    //     "YOUR_ANDROID_APP_ID",
    //     "ANDROID_TIKTOK_APP_ID_1,ANDROID_TIKTOK_APP_ID_2"
    // );

    // Continue to initialisation...
    TikTokBusinessSDK.InitializeSdk(
        config,
        (success, code, message) =>
        {
            if (success)
            {
                Debug.Log("TikTok App Events SDK initialized successfully");
            }
            else
            {
                Debug.LogError($"TikTok App Events SDK initialisation failed: code={code}, message={message}");
            }
        }
    );
}
```

### Trì hoãn truyền phát sự kiện
Khi tích hợp TikTok App Events SDK, khách hàng có thể cần cấu hình SDK để trì hoãn việc truyền dữ liệu và thu thập sự kiện theo các quy định pháp lý của từng khu vực. TikTok cung cấp các tài nguyên hỗ trợ tuân thủ và có thể tích hợp theo hướng dẫn tại [Chia sẻ dữ liệu sau khi người dùng đồng ý](do-luong-quang-cao-tom-tat.md#doc-1824048384831554).

## Lưu ý thiết lập theo từng nền tảng
### Android: Quyền, Proguard và cấu hình Gradle
- **Permissions**: Trong tệp `AndroidManifest.xml`, hãy khai báo các quyền `INTERNET` và `AD_ID`.
```http
// curl
<!-- AndroidManifest.xml -->
<manifest ...>
    <uses-permission android:name="android.permission.INTERNET" />
    <!-- Required for advertising and analytics purposes on Android 13+ -->
    <uses-permission android:name="com.google.android.gms.permission.AD_ID" />

    <application ...>
        ...
    </application>
</manifest>
```

- **Proguard**: Để ngăn SDK bị loại bỏ trong các bản dựng release, hãy thêm các quy tắc này vào tệp `proguard-rules.pro` của bạn:
```http
// curl
# proguard-rules.pro

# TikTok SDK
-keep class com.tiktok.** { *; }

# Google Play Billing Library
-keep class com.android.billingclient.api.** { *; }

# Google Install Referrer
-keep class com.android.installreferrer.api.** { *; }

# Android Lifecycle
-keep class androidx.lifecycle.** { *; }
```

- **Tùy chọn Gradle**: Đảm bảo tệp `build.gradle` cấp ứng dụng hoặc `mainTemplate.gradle` của bạn nhắm mục tiêu Java 8.
```http
// curl
// app/build.gradle
android {
  compileOptions {
    sourceCompatibility JavaVersion.VERSION_1_8
    targetCompatibility JavaVersion.VERSION_1_8
  }
}
```

### iOS: AppTrackingTransparency (ATT) và SKAdNetwork
**App Tracking Transparency (ATT)**: Để truy cập mã nhận dạng quảng cáo của thiết bị (IDFA) trên iOS 14.5+, bạn phải yêu cầu người dùng đồng ý. Thêm khóa `NSUserTrackingUsageDescription` vào `Info.plist` kèm thông điệp giải thích lý do bạn cần quyền theo dõi.

**SKAdNetwork** **(SKAN)**:
- SDK hỗ trợ SKAN để phân bổ bảo vệ quyền riêng tư. Để tránh xung đột, nếu bạn dùng SDK khác (như MMP) quản lý cập nhật SKAN, bạn phải tắt hỗ trợ SKAdNetwork của App Events SDK.
```http
// curl
// In your TikTokConfig initialisation
config.IOS_DisableSKAdNetworkSupport();
```

- Cần có bản đồ lược đồ để báo cáo chính xác các giá trị chuyển đổi nhận được từ Apple. Để cấu hình bản đồ này, hãy tham khảo [Báo cáo SKAdNetwork và ánh xạ lược đồ](do-luong-quang-cao-p2.md#doc-1862352021568001).

## Báo cáo sự kiện ứng dụng
### Các sự kiện được ghi tự động
SDK tự động ghi nhật ký các sự kiện sau nếu chúng không bị vô hiệu hóa trong khi cấu hình:

| Event | Description |
|---|---|
| `InstallApp` | First-time app launch after installation. ⏎ You may notice an increase in reported install events when the SDK is integrated for the first time. This is expected, as installs are measured based on the first detectable app launch by the SDK. If this is a concern, allow a few days for your existing user base to update their apps before running paid campaigns. |
| `LaunchAPP` | On every app launch. |
| `2DRetention` | App is opened the day after the first app launch. |
| `Purchase` | A successful transaction is completed via Apple's StoreKit or the Google Play Billing Library. This includes consumable, non-consumable, and subscription purchases. |

Bạn có tùy chọn tắt tính năng ghi nhật ký sự kiện tự động. Việc tắt ghi nhật ký tự động đồng nghĩa với các sự kiện như cài đặt ứng dụng và khởi chạy ứng dụng sẽ không còn được theo dõi theo mặc định.

Nếu bạn cần các sự kiện này cho mục đích đo lường hoặc phân tích, bạn phải triển khai ghi nhật ký thủ công trong mã ứng dụng để thu thập và gửi chúng.
```http
// curl
TikTokConfig config = new TikTokConfig(/*...*/);

// Option 1: Disable ALL automatic events
config.DisableAutoTrack();

// Option 2: Disable specific automatic events
config.DisableInstallTrack();
config.DisableLaunchTrack();
config.DisableRetentionTrack();
config.DisablePayTrack();

TikTokBusinessSDK.InitializeSdk(config);
```

### Các sự kiện ghi thủ công
#### Các sự kiện tiêu chuẩn (Standard events)
Đối với các sự kiện đơn giản không có thuộc tính, tạo một `TikTokBaseEvent` với hằng số sự kiện từ enum `TTEventName`. Để xem danh sách đầy đủ các enum `TTEventName`, hãy tham khảo [Hằng số sự kiện tiêu chuẩn và các lớp](do-luong-quang-cao-p2.md#doc-1862287695864834).

**Ví dụ:** Sự kiện **`Registration`**
```http
// curl
// Example: A user completes a registration
TikTokBaseEvent registrationEvent = new TikTokBaseEvent(TTEventName.TTEventNameRegistration);
TikTokBusinessSDK.TrackTTEvent(registrationEvent);
```

#### Thêm thuộc tính vào sự kiện tiêu chuẩn
Đối với các sự kiện bao gồm chi tiết về sản phẩm hoặc giá trị, các lớp builder có sẵn cho các sự kiện Tiêu chuẩn bên dưới, và có thể dùng `TikTokBaseEvent` cho tất cả các sự kiện tiêu chuẩn khác:

| Standard event | Builder Class |
|---|---|
| Add to Cart | `TikTokAddToCartEvent` |
| Add to Wishlist | `TikTokAddToWishlistEvent` |
| Checkout | `TikTokCheckoutEvent` |
| Purchase | `TikTokPurchaseEvent` |
| View Content | `TikTokViewContentEvent` |

**Ví dụ:** Lớp builder sự kiện **`ViewContent`**
```http
// curl
// Example: A user adds an item to the cart
TikTokAddToCartEvent cartEvent = new TikTokAddToCartEvent();
cartEvent.SetDescription("Description of the product");
cartEvent.SetCurrency(TTCurrency.TTCurrencyUSD);
cartEvent.SetValue("4.99");
cartEvent.SetContentType("product_group");
cartEvent.SetContentId("ABC-123");

TikTokContentParams eventContent = new TikTokContentParams();
eventContent.price = 4.99;
eventContent.quantity = 1;
eventContent.brand = "AwesomeBrand";
eventContent.contentName = "The Best Product";
TikTokContentParams[] contents = { eventContent };

cartEvent.SetContents(contents);
TikTokBusinessSDK.TrackTTEvent(cartEvent);
```

**Ví dụ:** Sự kiện **`CompleteTutorial`**

Đối với các sự kiện tiêu chuẩn khác có thuộc tính tiêu chuẩn, sử dụng trình dựng `TikTokBaseEvent` với hằng số từ enum `TTEventName`.
```http
// curl
// Example: A user completes the onboarding tutorial
TikTokBaseEvent tutorialEvent = new TikTokBaseEvent(TTEventName.TTEventNameCompleteTutorial);

// Standard properties (replace with actual values)
tutorialEvent.AddProperty("currency", TTCurrency.TTCurrencyUSD); // ISO 4217 currency code
tutorialEvent.AddProperty("value", 9.99);                        // Order or items value
tutorialEvent.AddProperty("content_id", "CONTENT_ID");           // Unique product/content ID
tutorialEvent.AddProperty("content_type", "CONTENT_TYPE");       // Type of content in the event
tutorialEvent.AddProperty("price", 9.99);                        // Item price
tutorialEvent.AddProperty("quantity", 1);                        // Number of items

TikTokBusinessSDK.TrackTTEvent(tutorialEvent);
```

> **Note:** 
> Để xem danh sách đầy đủ các thuộc tính tiêu chuẩn được hỗ trợ, hãy tham khảo [Tài liệu tham khảo đối tượng Properties](https://business-api.tiktok.com/portal/docs/setup-guide-for-app/v1.3#item-link-properties%20parameters). Các khóa thuộc tính tùy chỉnh không được hỗ trợ và sẽ bị loại bỏ.

#### Doanh thu quảng cáo trong ứng dụng (In-app ad revenue)
Bắt đầu từ SDK phiên bản 1.5.0, dữ liệu doanh thu qua trung gian quảng cáo trong ứng dụng có thể được báo cáo bằng `TikTokAdRevenueEvent`. Tham khảo [Báo cáo doanh thu quảng cáo trong ứng dụng](do-luong-quang-cao-tom-tat.md#doc-1862351923536898) để biết hướng dẫn triển khai chi tiết cho AppLovin Max, ironSource và Google AdMob.
#### Các sự kiện tùy chỉnh (Custom events)
Để theo dõi một sự kiện không có trong danh sách sự kiện tiêu chuẩn, sử dụng `TikTokBaseEvent` với chuỗi tên sự kiện tùy chỉnh.
```http
// curl
// Example: A user shares content
TikTokBaseEvent baseEvent = new TikTokBaseEvent("ShareContent");
TikTokBusinessSDK.TrackTTEvent(baseEvent);
```

****

## Bật Khớp nâng cao (Advanced Matching)
Để cải thiện so khớp đối tượng, sử dụng `Identify()` để thiết lập các thuộc tính so khớp nâng cao khi có thông tin người dùng (ví dụ: sau khi đăng nhập hoặc đăng ký), và `Logout()` để xóa.
```http
// curl
// When user logs in or signs up
TikTokBusinessSDK.Identify(
    "user-external-id-123",  // externalId
    "user-name-456",         // externalUserName
    "+15551234567",          // phoneNumber (E.164 format)
    "user@example.com"       // email
);

// When user logs out
TikTokBusinessSDK.Logout();
```

**Supported Properties**

Property
Formatting Requirements

externalId: Mã định danh duy nhất từ nhà quảng cáo, chẳng hạn như ID hội viên hoặc ID người dùng.
Văn bản thuần chưa băm. Cắt bỏ khoảng trắng ở đầu/cuối.
"user-id-abc"

externalUserName: Tên người dùng từ nhà quảng cáo.
Văn bản thuần chưa băm. Cắt bỏ khoảng trắng ở đầu/cuối.
"testuser"

email
Văn bản thuần chưa băm. Cắt bỏ khoảng trắng ở đầu/cuối và chuyển thành chữ thường.
"email@example.com"

phoneNumber
Văn bản thuần chưa băm. Chuẩn hóa theo định dạng E.164 (ví dụ: +[mã quốc gia][số điện thoại]).
"+15551234567"

## Xác minh tích hợp của bạn
Sử dụng TikTok Events Manager để xác minh các sự kiện được tiếp nhận chính xác. Thao tác này sẽ gửi các sự kiện đến một điểm cuối riêng biệt phục vụ thử nghiệm và không làm ảnh hưởng đến dữ liệu sản xuất của bạn.
### Sự kiện kiểm tra không cần viết mã (Khuyến nghị)
Phương pháp này cho phép gỡ lỗi sự kiện trên từng thiết bị cụ thể mà không cần sửa mã. Trước khi bắt đầu, hãy đảm bảo rằng:
- Phiên bản mới nhất của ứng dụng TikTok đã được cài đặt trên thiết bị kiểm tra của bạn.
- Ứng dụng của bạn đang tích hợp SDK phiên bản 1.5.0 trở lên
- (Chỉ iOS) Bạn đã cấp quyền App Tracking Transparency (ATT) cho cả ứng dụng của bạn và ứng dụng TikTok.

| Step | Instructions |
|---|---|
| Generate QR Code | • In **Events Manager** for your app, go to the **Test Events** tab. • Click **Generate QR code**. A QR code is generated, valid for 24 hours. • To force expiry before the 24 hours is over, click **Disable code**. |
| Bind Device | • Open the TikTok app on your test device and go to your **Profile**. • Tap the menu icon (☰) in the top right, then select **My QR code**. • Tap the scan icon in the top right and scan the QR code from Events Manager. • Tap **Authorize** to bind your device and enable test mode. |
| Verify Events | • Trigger events in your app. They will appear in the **Test Event** tab in real-time. • If you configured multiple TikTok App IDs, test events will only appear in the Events Manager for the **first** ID in the list. |

### Chế độ gỡ lỗi thủ công (Manual debug mode)
> **Important:** 
> Lưu ý: Hãy nhớ tắt chế độ gỡ lỗi thủ công và nhật ký chi tiết trước khi phát hành ứng dụng ra môi trường sản xuất. Các sự kiện kiểm tra sẽ bị loại bỏ và không được dùng cho báo cáo chiến dịch.

#### Bật chế độ gỡ lỗi
Thêm `OpenDebugMode()` vào `TikTokConfig` trong quá trình khởi tạo. Bạn cũng có thể dùng `SetLogLevel()` để xem thông tin đầu ra chi tiết hơn.
```http
// curl
TikTokConfig config = new TikTokConfig(/*...*/);
config.OpenDebugMode();
config.SetLogLevel(TiktokLogLevel.VERBOSE); // Optional

TikTokBusinessSDK.InitializeSdk(config);
```

Các cấp độ ghi nhật ký khả dụng gồm `NONE`, `INFO`, `WARN`, `DEBUG` và `VERBOSE`.
#### Tắt chế độ gỡ lỗi
Sau khi quá trình tích hợp được xác minh, hãy xóa các lệnh gọi `OpenDebugMode()` và `SetLogLevel()` trước khi gửi ứng dụng của bạn.
```http
// curl
// REMOVEME
// config.OpenDebugMode();
// config.SetLogLevel(TiktokLogLevel.VERBOSE);
```

### Tạo và xác minh sự kiện
Sau khi bật chế độ gỡ lỗi, hãy chạy ứng dụng và kích hoạt một số sự kiện. Bạn có thể xem các sự kiện đến theo thời gian thực dưới tab **Sự kiện kiểm tra (Test Event)** trên trang Trình quản lý sự kiện của ứng dụng.

Nếu có nhiều TikTok App ID trong cấu hình SDK, các sự kiện kiểm tra sẽ chỉ hiển thị trong tài khoản quảng cáo liên kết với TikTok App ID **đầu tiên** trong chuỗi cấu hình.

![Sự kiện kiểm tra iOS](https://images.ctfassets.net/5jqet0ab9qci/3dfGPuRElVFFmaKkD0bqxs/b245f2eb9d67b7ea91431ec1596237ba/iOS_test_events.png)

## Các tính năng bổ sung và hướng dẫn
- [Đo lường dự đoán nâng cao (Advanced Predictive Measurement)](do-luong-quang-cao-p2.md#doc-1862348642630658)
- [Deeplink và deferred deeplink](do-luong-quang-cao-p2.md#doc-1862348999629826)
- [Tăng cường postback dữ liệu](do-luong-quang-cao-p2.md#doc-1862351781303361)
- [Báo cáo doanh thu quảng cáo trong ứng dụng](do-luong-quang-cao-tom-tat.md#doc-1862351923536898)
- [Báo cáo SKAdNetwork và ánh xạ lược đồ](do-luong-quang-cao-p2.md#doc-1862352021568001)
- [Các phương pháp tuân thủ tốt nhất](do-luong-quang-cao-p2.md#doc-1862352195035138)

---

<a id="doc-1876482381311362"></a>
<!-- doc_id: 1876482381311362 -->
<!-- doc_id: 1876482381311362 -->
# Cài đặt SDK trên React Native (React Native installation)
> Đường dẫn: Marketing API > Ad Measurement > Guides > TikTok App Events SDK > Getting started > React Native installation
> **Important:** 
> **Quan trọng:** Việc sử dụng TikTok App Events SDK tuân theo [Điều khoản Dịch vụ Thương mại TikTok For Business](https://ads.tiktok.com/i18n/official/policy/commercial-terms-of-service). Bằng việc sử dụng SDK, bạn cũng đồng ý với [Điều khoản sản phẩm thương mại TikTok (Dữ liệu)](https://ads.tiktok.com/i18n/official/policy/business-products-terms) và cam kết không chia sẻ dữ liệu nhạy cảm với TikTok.

TikTok App Events SDK cho React Native được duy trì trong [kho lưu trữ GitHub công khai](https://github.com/tiktok/tiktok-business-react-native-sdk) và xuất bản trên npm dưới dạng [`@tiktok-for-business/react-native-sdk`](https://www.npmjs.com/package/@tiktok-for-business/react-native-sdk). SDK cung cấp API TypeScript có định kiểu tĩnh bao bọc trên các SDK iOS và Android gốc của TikTok for Business.

## Prerequisites
Trước khi bắt đầu, hãy đảm bảo bạn có các thông tin sau từ tài khoản TikTok for Business của mình:
- **App ID** của ứng dụng — tên gói Android (ví dụ: `com.example.app`) hoặc Apple App Store ID dạng số (ví dụ: `123456789`), tùy thuộc vào nền tảng mục tiêu.
- Một **TikTok App ID** từ trang cài đặt ứng dụng trong Trình quản lý sự kiện, cho từng nền tảng.
- Một **App Secret** để xác minh, từ trang cài đặt ứng dụng trong Trình quản lý sự kiện.
Nếu bạn chưa có các thông tin này, hãy tham khảo [Bắt đầu](do-luong-quang-cao-p1.md#doc-1862119945765889) trước khi tiếp tục.

## Thêm SDK làm phần phụ thuộc bản dựng
### Cài đặt gói npm
```http
// curl
npm install @tiktok-for-business/react-native-sdk
# or
pnpm add @tiktok-for-business/react-native-sdk
# or
yarn add @tiktok-for-business/react-native-sdk
```

### iOS
Sau khi thêm gói npm, cài đặt các pod iOS gốc:
```http
// curl
cd ios
bundle exec pod install
```

### Android
Đảm bảo JitPack có sẵn trong cấu hình kho lưu trữ (repository) của dự án:
```http
// curl
// settings.gradle or build.gradle (repositories block)
maven { url 'https://jitpack.io' }
```

### Chuyển sang React Native từ các SDK Android hoặc iOS gốc hiện có
Các nhà phát triển đã tích hợp SDK TikTok App Events gốc cho Android (Java, Kotlin) hoặc iOS (Swift, Objective-C) có thể chuyển sang React Native SDK bằng cách:
- Thay thế các phần phụ thuộc SDK gốc bằng gói npm `@tiktok-for-business/react-native-sdk` (gói này đã tích hợp sẵn các SDK gốc), và
- Thay thế mọi cấu hình và lệnh gọi phương thức SDK gốc bằng API React Native TypeScript. Việc kết hợp giao diện native và React Native có thể gây xung đột và không được khuyến nghị hoặc hỗ trợ.

## Cấu hình và khởi tạo SDK
Khởi tạo SDK càng sớm càng tốt trong vòng đời của ứng dụng, trước khi theo dõi bất kỳ sự kiện nào. Hãy gọi `initialize()` một lần duy nhất — thường là trong root component hoặc điểm khởi nhập (entry point) của ứng dụng.

> **Lưu ý:**
> • SDK chỉ hỗ trợ khởi tạo và sử dụng trong tiến trình chính và luồng chính.
> • Trong lần khởi tạo đầu tiên, Android SDK sẽ lấy User Agent của thiết bị qua WebView. Để tránh xung đột khóa, vui lòng chỉ sử dụng WebView sau khi khởi tạo thành công.
> • Nếu bạn làm việc với nhiều Tài khoản quảng cáo, bạn có thể cung cấp một mảng các TikTok App ID. Mỗi phần tử trong mảng phải là một ID, không có dấu phẩy hoặc khoảng trắng. ID đầu tiên trong mảng được dùng cho Sự kiện thử nghiệm trong Trình quản lý sự kiện.
> • Do ứng dụng React Native được biên dịch theo từng nền tảng, hãy cung cấp `appId` thích hợp cho từng nền tảng khi chạy (ví dụ: package name cho Android hoặc Apple ID cho iOS) bằng `Platform.select()` hoặc lớp cấu hình của bạn.

```http
// curl
import TikTokBusinessSDK from '@tiktok-for-business/react-native-sdk';

// Initialize with your credentials
await TikTokBusinessSDK.initialize({
  appId: 'YOUR_APP_ID',             // Android package name or iOS Apple ID
  accessToken: 'YOUR_APP_SECRET', // From Events Manager
  tiktokAppId: ['YOUR_TIKTOK_APP_ID'],
});

// For multiple TikTok App IDs:
// await TikTokBusinessSDK.initialize({
//   appId: 'YOUR_APP_ID',
//   accessToken: 'YOUR_APP_SECRET',
//   tiktokAppId: ['TIKTOK_APP_ID_1', 'TIKTOK_APP_ID_2'],
// });
```

Đối với các ứng dụng đa nền tảng, sử dụng `Platform.select()` để truyền thông tin xác thực chính xác theo từng nền tảng:
```http
// curl
import { Platform } from 'react-native';

await TikTokBusinessSDK.initialize({
  appId: Platform.select({
    ios: 'YOUR_IOS_APPLE_ID',
    android: 'YOUR_ANDROID_PACKAGE_NAME',
  })!,
  accessToken: Platform.select({
    ios: 'YOUR_IOS_APP_SECRET',
    android: 'YOUR_ANDROID_APP_SECRET',
  })!,
  tiktokAppId: Platform.select({
    ios: ['YOUR_IOS_TIKTOK_APP_ID'],
    android: ['YOUR_ANDROID_TIKTOK_APP_ID'],
  })!,
});
```

### Trì hoãn truyền sự kiện
Khi tích hợp TikTok App Events SDK, khách hàng có thể cần cấu hình SDK để trì hoãn việc truyền dữ liệu và thu thập sự kiện theo các quy định pháp lý của từng khu vực. TikTok cung cấp các tài nguyên hỗ trợ tuân thủ và có thể tích hợp theo hướng dẫn tại [Chia sẻ dữ liệu sau khi người dùng đồng ý](do-luong-quang-cao-tom-tat.md#doc-1824048384831554).

## Lưu ý thiết lập nền tảng
### Android: Quyền, Proguard và tùy chọn Gradle
- **Quyền truy cập**: Trong tệp `AndroidManifest.xml` của bạn, khai báo các quyền `INTERNET` và `AD_ID`.
```http
// curl
<!-- AndroidManifest.xml -->
<manifest ...>
    <uses-permission android:name="android.permission.INTERNET" />
    <!-- Required for advertising and analytics purposes on Android 13+ -->
    <uses-permission android:name="com.google.android.gms.permission.AD_ID" />

    <application ...>
        ...
    </application>
</manifest>
```

- **Proguard**: Để ngăn SDK bị loại bỏ trong các bản dựng release, hãy thêm các quy tắc này vào tệp `proguard-rules.pro` của bạn:
```http
// curl
# proguard-rules.pro

# TikTok SDK
-keep class com.tiktok.** { *; }

# Google Play Billing Library
-keep class com.android.billingclient.api.** { *; }

# Google Install Referrer
-keep class com.android.installreferrer.api.** { *; }

# Android Lifecycle
-keep class androidx.lifecycle.** { *; }
```

- **Tùy chọn Gradle**: Tệp `build.gradle` của gói đã nhắm mục tiêu Java 8. Nếu `build.gradle` cấp ứng dụng của bạn chưa cấu hình, hãy đảm bảo nó cũng nhắm mục tiêu Java 8:
```http
// curl
// app/build.gradle
android {
  compileOptions {
    sourceCompatibility JavaVersion.VERSION_1_8
    targetCompatibility JavaVersion.VERSION_1_8
  }
}
```

### iOS: AppTrackingTransparency (ATT) và SKAdNetwork
**App Tracking Transparency (ATT)**: Để truy cập mã nhận dạng quảng cáo thiết bị (IDFA) trên iOS 14.5+, bạn phải yêu cầu người dùng đồng ý. Thêm khóa `NSUserTrackingUsageDescription` vào `Info.plist` kèm thông điệp giải thích lý do cần quyền theo dõi. Sau đó bạn có thể gọi `requestTrackingAuthorization()` từ SDK vào thời điểm thích hợp trong luồng đồng ý của ứng dụng.

```http
// curl
// Request ATT at your app's preferred consent moment (iOS only)
const status = await TikTokBusinessSDK.requestTrackingAuthorizationWithCompletionHandler();
```

**SKAdNetwork (SKAN)**:

SDK hỗ trợ SKAN để phân bổ bảo vệ quyền riêng tư. Để tránh xung đột, nếu bạn dùng SDK khác (như MMP) quản lý SKAN trong ứng dụng, bạn phải tắt tính năng hỗ trợ SKAdNetwork của App Events SDK.

```http
// curl
// In your initialization config
await TikTokBusinessSDK.initialize({
  appId: 'YOUR_APP_ID',
  accessToken: 'YOUR_APP_SECRET',
  tiktokAppId: ['YOUR_TIKTOK_APP_ID'],
  ios: {
    disableSKAdNetworkSupport: true,
  },
});
```

Cần có bản đồ lược đồ (schema map) để báo cáo chính xác các giá trị chuyển đổi nhận được từ Apple. Để cấu hình bản đồ này, hãy tham khảo [Báo cáo SKAdNetwork và ánh xạ lược đồ](do-luong-quang-cao-p2.md#doc-1862352021568001).

## Báo cáo sự kiện ứng dụng
### Các sự kiện được ghi nhật ký tự động
SDK tự động ghi nhật ký các sự kiện sau nếu chúng không bị vô hiệu hóa trong khi cấu hình:

| Event | Description |
|---|---|
| `InstallApp` | First-time app launch after installation. ⏎ You may notice an increase in reported install events when the SDK is integrated for the first time. This is expected, as installs are measured based on the first detectable app launch by the SDK. If this is a concern, allow a few days for your existing user base to update their apps before running paid campaigns. |
| `LaunchAPP` | On every app launch. |
| `2DRetention` | App is opened the day after the first app launch. |
| `Purchase` | A successful transaction is completed via Apple's StoreKit or the Google Play Billing Library. This includes consumable, non-consumable, and subscription purchases. |

Bạn có tùy chọn tắt tính năng ghi nhật ký sự kiện tự động. Việc tắt ghi nhật ký tự động đồng nghĩa với các sự kiện như cài đặt ứng dụng và khởi chạy ứng dụng sẽ không còn được theo dõi theo mặc định.

Nếu bạn cần các sự kiện này cho mục đích đo lường hoặc phân tích, bạn phải triển khai ghi nhật ký thủ công trong mã ứng dụng để thu thập và gửi chúng.
```http
// curl
await TikTokBusinessSDK.initialize({
  appId: 'YOUR_APP_ID',
  accessToken: 'YOUR_APP_SECRET',
  tiktokAppId: ['YOUR_TIKTOK_APP_ID'],

  // Option 1: Disable ALL automatic events
  disableAutoTrack: true,

  // Option 2: Disable specific automatic events
  disableInstallTrack: true,
  disableLaunchTrack: true,
  disableRetentionTrack: true,
  disablePayTrack: true,
});
```

### Các sự kiện được ghi nhật ký thủ công
#### Các sự kiện tiêu chuẩn
Đối với các sự kiện đơn giản không có thuộc tính, sử dụng `trackEvent()` với hằng số sự kiện từ `TikTokEventNames`. Để xem danh sách đầy đủ các hằng số tên sự kiện, tham khảo [Hằng số sự kiện tiêu chuẩn và các lớp](do-luong-quang-cao-p2.md#doc-1862287695864834).

**Ví dụ:** Sự kiện **`Registration`**
```http
// curl
import TikTokBusinessSDK, { TikTokEventNames } from '@tiktok-for-business/react-native-sdk';

// Example: A user completes a registration
await TikTokBusinessSDK.trackEvent(TikTokEventNames.Registration);
```

#### Thêm thuộc tính vào sự kiện tiêu chuẩn
Đối với các sự kiện có thông tin chi tiết về sản phẩm hoặc giá trị, sử dụng `trackContentEvent()` với hằng số sự kiện nội dung từ `TikTokContentEventNames`. Các loại sự kiện nội dung sau được hỗ trợ:

| Standard event | Content event name |
|---|---|
| Add to Cart | `TikTokContentEventNames.AddToCart` |
| Add to Wishlist | `TikTokContentEventNames.AddToWishlist` |
| Checkout | `TikTokContentEventNames.Checkout` |
| Purchase | `TikTokContentEventNames.Purchase` |
| View Content | `TikTokContentEventNames.ViewContent` |

**Ví dụ:** Sự kiện nội dung **`AddToCart`**
```http
// curl
import TikTokBusinessSDK, { TikTokContentEventNames } from '@tiktok-for-business/react-native-sdk';

// Example: A user adds an item to the cart
await TikTokBusinessSDK.trackContentEvent(TikTokContentEventNames.AddToCart, {
  properties: {
    description: 'Description of the product',
    contentId: 'ABC-123',
    contentType: 'product_group',
    currency: 'USD',
    value: 4.99,
  },
  contents: [
    {
      price: 4.99,
      quantity: 1,
      brand: 'AwesomeBrand',
      contentName: 'The Best Product',
      contentId: 'ABC-123',
    },
  ],
});
```

**Ví dụ:** Sự kiện **`CompleteTutorial`** có thuộc tính

Đối với các sự kiện tiêu chuẩn khác có thuộc tính tiêu chuẩn, sử dụng `trackEvent()` với một hằng số từ `TikTokEventNames` và đối tượng thuộc tính (properties).

```http
// curl
// Example: A user completes the onboarding tutorial
await TikTokBusinessSDK.trackEvent(TikTokEventNames.CompleteTutorial, {
  properties: {
    currency: 'USD',
    value: 9.99,
    contentId: 'CONTENT_ID',
    contentType: 'CONTENT_TYPE',
    price: 9.99,
    quantity: 1,
  },
});
```

> **Note:** 
> Để xem danh sách đầy đủ các thuộc tính tiêu chuẩn được hỗ trợ, tham khảo [Tham chiếu đối tượng Properties](https://business-api.tiktok.com/portal/docs/setup-guide-for-app/v1.3#anchor-2-1-1-2). Các khóa thuộc tính tùy chỉnh không được hỗ trợ và sẽ bị loại bỏ.

#### Doanh thu quảng cáo trong ứng dụng
Dữ liệu doanh thu trung gian quảng cáo trong ứng dụng có thể được báo cáo bằng `trackAdRevenueEvent()`. Tham khảo [Báo cáo doanh thu quảng cáo trong ứng dụng](do-luong-quang-cao-tom-tat.md#doc-1862351923536898) để biết hướng dẫn triển khai chi tiết cho AppLovin Max, ironSource và Google AdMob.

```http
// curl
await TikTokBusinessSDK.trackAdRevenueEvent({
  adNetwork: 'example-network',
  adPlatform: 'example-platform',
  revenue: 1.25,
  currency: 'USD',
  adUnit: 'rewarded-video',
});
```

#### Sự kiện tùy chỉnh
Để theo dõi một sự kiện không có trong danh sách chuẩn, hãy sử dụng `trackCustomEvent()` với chuỗi tên sự kiện tùy chỉnh.

```http
// curl
// Example: A user shares content
await TikTokBusinessSDK.trackCustomEvent('ShareContent');
```

## Bật So khớp nâng cao
Để cải thiện khả năng khớp đối tượng, sử dụng `identify()` để thiết lập các thuộc tính So khớp nâng cao khi có thông tin người dùng (ví dụ: sau khi đăng nhập hoặc đăng ký), và gọi `logout()` để xóa thông tin này.

```http
// curl
// When user logs in or signs up
await TikTokBusinessSDK.identify({
  externalId: 'user-external-id-123',   // externalId
  externalUserName: 'user-name-456',    // externalUserName
  phoneNumber: '+15551234567',          // phoneNumber (E.164 format)
  email: 'user@example.com',           // email
});

// When user logs out
await TikTokBusinessSDK.logout();
```

**Supported Properties**

Property
Formatting Requirements
Example

externalId: Mã định danh duy nhất từ nhà quảng cáo, chẳng hạn như ID hội viên hoặc ID người dùng.
Văn bản thuần chưa băm. Cắt bỏ khoảng trắng ở đầu/cuối.
"user-id-abc"

externalUserName: Tên người dùng từ nhà quảng cáo.
Văn bản thuần chưa băm. Cắt bỏ khoảng trắng ở đầu/cuối.
"testuser"

email
Văn bản thuần chưa băm. Cắt bỏ khoảng trắng ở đầu/cuối và chuyển thành chữ thường.
"email@example.com"

phoneNumber
Văn bản thuần chưa băm. Chuẩn hóa theo định dạng E.164 (ví dụ: +[mã quốc gia][số điện thoại]).
"+15551234567"

Lớp React Native không thực hiện băm, lưu giữ, chuẩn hóa hay ghi đè giá trị email hoặc số điện thoại. Lớp này chuyển các giá trị runtime tới SDK gốc để xử lý hành vi So khớp nâng cao chính thức.

## Xác minh tích hợp của bạn
Sử dụng TikTok Events Manager để xác minh các sự kiện được tiếp nhận chính xác. Thao tác này sẽ gửi các sự kiện đến một điểm cuối riêng biệt phục vụ thử nghiệm và không làm ảnh hưởng đến dữ liệu sản xuất của bạn.
### Sự kiện kiểm tra không cần viết mã (Khuyến nghị)
Phương pháp này cho phép gỡ lỗi sự kiện trên từng thiết bị cụ thể mà không cần sửa mã. Trước khi bắt đầu, hãy đảm bảo rằng:
- Phiên bản mới nhất của ứng dụng TikTok đã được cài đặt trên thiết bị kiểm tra của bạn.
- (Chỉ iOS) Bạn đã cấp quyền App Tracking Transparency (ATT) cho cả ứng dụng của bạn và ứng dụng TikTok.

| Step | Instructions |
|---|---|
| Generate QR Code | • In **Events Manager** for your app, go to the **Test Events** tab. • Click **Generate QR code**. A QR code is generated, valid for 24 hours. • To force expiry before the 24 hours is over, click **Disable code**. |
| Bind Device | • Open the TikTok app on your test device and go to your **Profile**. • Tap the menu icon (☰) in the top right, then select **My QR code**. • Tap the scan icon in the top right and scan the QR code from Events Manager. • Tap **Authorize** to bind your device and enable test mode. |
| Verify Events | • Trigger events in your app. They will appear in the **Test Event** tab in real-time. • If you configured multiple TikTok App IDs, test events will only appear in the Events Manager for the **first** ID in the list. |

### Chế độ gỡ lỗi thủ công
> **Important:** 
> Hãy nhớ tắt chế độ gỡ lỗi và ghi nhật ký chi tiết trước khi phát hành ứng dụng lên môi trường production. Các sự kiện kiểm tra sẽ bị loại bỏ và không được dùng để báo cáo chiến dịch.

#### Bật chế độ gỡ lỗi
Thêm cấu hình `debug` vào lệnh gọi `initialize()`. Bạn cũng có thể thiết lập `logLevel` để xem đầu ra chi tiết hơn.
```http
// curl
await TikTokBusinessSDK.initialize({
  appId: 'YOUR_APP_ID',
  accessToken: 'YOUR_APP_SECRET',
  tiktokAppId: ['YOUR_TIKTOK_APP_ID'],
  debug: {
    enabled: true,
    logLevel: 'verbose', // Options: 'none', 'error', 'warning', 'info', 'debug', 'verbose'
  },
});
```

#### Tắt chế độ gỡ lỗi
Sau khi quá trình tích hợp được xác minh, hãy xóa cấu hình `debug` hoặc đặt `enabled: false` trước khi gửi ứng dụng.
```http
// curl
// Remove or disable debug mode for production
await TikTokBusinessSDK.initialize({
  appId: 'YOUR_APP_ID',
  accessToken: 'YOUR_APP_SECRET',
  tiktokAppId: ['YOUR_TIKTOK_APP_ID'],
  // debug: { enabled: true, logLevel: 'verbose' },  // REMOVE THIS
});
```

### Tạo và xác minh sự kiện
Sau khi bật chế độ debug, hãy chạy ứng dụng và kích hoạt một số sự kiện. Bạn có thể xem các sự kiện gửi về theo thời gian thực trong tab **Sự kiện thử nghiệm** (Test Events) trên trang Trình quản lý sự kiện của ứng dụng.

Nếu có nhiều TikTok App ID trong cấu hình SDK, sự kiện thử nghiệm sẽ chỉ hiển thị trong tài khoản quảng cáo của Trình quản lý sự kiện được liên kết với TikTok App ID **đầu tiên** trong mảng.

![Tạo và xác minh sự kiện](https://images.ctfassets.net/5jqet0ab9qci/4YiWai9v9U9zFeh1hBQb35/a82e6afe098cfe9c87b529cde80d9cd3/Generate_and_verify_events.png)

## Các tính năng bổ sung và hướng dẫn
- [Đo lường dự đoán nâng cao (Advanced Predictive Measurement)](do-luong-quang-cao-p2.md#doc-1862348642630658)
- [Deeplink và deferred deeplink](do-luong-quang-cao-p2.md#doc-1862348999629826)
- [Tăng cường postback dữ liệu](do-luong-quang-cao-p2.md#doc-1862351781303361)
- [Báo cáo doanh thu quảng cáo trong ứng dụng](do-luong-quang-cao-tom-tat.md#doc-1862351923536898)
- [Báo cáo SKAdNetwork và ánh xạ lược đồ](do-luong-quang-cao-p2.md#doc-1862352021568001)
- [Các phương pháp tuân thủ tốt nhất](do-luong-quang-cao-p2.md#doc-1862352195035138)

---

<a id="doc-1862351923536898"></a>
<!-- doc_id: 1862351923536898 -->
<!-- doc_id: 1862351923536898 -->
# Báo cáo doanh thu quảng cáo trong ứng dụng (In-app ad revenue reporting)
> Đường dẫn: Marketing API > Ad Measurement > Guides > TikTok App Events SDK > Additional features > In-app ad revenue reporting
Bắt đầu từ phiên bản SDK 1.5.0, tính năng báo cáo doanh thu hòa giải quảng cáo trong ứng dụng (ad mediation revenue) được hỗ trợ. Hãy sử dụng các đoạn mã mẫu bên dưới dựa trên đối tác hòa giải bạn đang sử dụng.

> **Important:** 
> • Đối với nền tảng trung gian MAX và ironSource, hãy đảm bảo tất cả doanh thu được gửi theo đơn vị USD. 
>
> • **Lược đồ từ điển doanh thu quảng cáo phụ thuộc vào từng nền tảng.** Các khóa mà SDK đọc được chọn theo `device_ad_mediation_platform` và không thể hoán đổi cho nhau. Không tái sử dụng một trình tạo từ điển giữa các nhà cung cấp khác nhau.
>
> • Đảm bảo rằng các tham số không bị null.

 **** 

## Android
### [MAX](https://developers.axon.ai/en/max/android/overview/advanced-settings/#impression-level-user-revenue-api)
```http
// curl
MaxRewardedAd rewardedAd = MaxRewardedAd.getInstance("YOUR_AD_UNIT_ID", this);
rewardedAd.setRevenueListener(new MaxAdRevenueListener() {
    @Override
    public void onAdRevenuePaid(MaxAd maxAd) {
        double revenue = maxAd.getRevenue();
        String countryCode = AppLovinSdk.getInstance(context).getConfiguration().getCountryCode();
        String networkName = maxAd.getNetworkName();
        String adUnitId = maxAd.getAdUnitId();
        String format = maxAd.getFormat().toString();
        String placement = maxAd.getPlacement();
        String networkPlacement = maxAd.getNetworkPlacement();

        JSONObject adRevenueJson = new JSONObject();
        try {
            adRevenueJson.put("revenue", revenue);
            adRevenueJson.put("country_code", countryCode);
            adRevenueJson.put("network_name", networkName);
            adRevenueJson.put("ad_unit_id", adUnitId);
            adRevenueJson.put("ad_format", format);
            adRevenueJson.put("placement", placement);
            adRevenueJson.put("network_placement", networkPlacement);
            adRevenueJson.put("device_ad_mediation_platform", "applovin_max_sdk");
        } catch (JSONException e) {
        }
        
        // Make sure the App Events SDK has been initialized before calling this
        TTBaseEvent adRevenueInfo = TTAdRevenueEvent.newBuilder(adRevenueJson).build();
        TikTokBusinessSdk.trackTTEvent(adRevenueInfo);
    }
});
```

### [ironSource](https://developers.is.com/ironsource-mobile/android/ad-revenue-measurement-integration/#step-1)
```http
// curl
/**
 * If you want to add the ImpressionData listener to your application,
 * make sure you declare the listener before initializing the ironSource SDK,
 * to avoid any loss of information.
 */
IronSource.addImpressionDataListener(new ImpressionDataListener() {
    @Override
    public void onImpressionSuccess(ImpressionData impressionData) {
        String auctionId = impressionData.getAuctionId();
        String adUnit = impressionData.getAdUnit();
        String adNetwork = impressionData.getAdNetwork();
        String instanceName = impressionData.getInstanceName();
        String instanceId = impressionData.getInstanceId();
        String country = impressionData.getCountry();
        String placement = impressionData.getPlacement();
        Double revenue = impressionData.getRevenue();
        String precision = impressionData.getPrecision();
        String ab = impressionData.getAb();
        String segmentName = impressionData.getSegmentName();
        Double lifetimeRevenue = impressionData.getLifetimeRevenue();
        String encryptedCPM = impressionData.getEncryptedCPM();

        JSONObject adRevenueJson = new JSONObject();
        try {
            adRevenueJson.put("auction_id", auctionId);
            adRevenueJson.put("ad_unit", adUnit);
            adRevenueJson.put("ad_network", adNetwork);
            adRevenueJson.put("instance_name", instanceName);
            adRevenueJson.put("instance_id", instanceId);
            adRevenueJson.put("country", country);
            adRevenueJson.put("placement", placement);
            adRevenueJson.put("revenue", revenue);
            adRevenueJson.put("precision", precision);
            adRevenueJson.put("ab", ab);
            adRevenueJson.put("segment_name", segmentName);
            adRevenueJson.put("lifetime_revenue", lifetimeRevenue);
            adRevenueJson.put("encrypted_cpm", encryptedCPM);
            adRevenueJson.put("device_ad_mediation_platform", "ironsource_sdk");
        } catch (JSONException e) {
        }
        
        // Make sure the App Events SDK has been initialized before calling this
        TTBaseEvent adRevenueInfo = TTAdRevenueEvent.newBuilder(adRevenueJson).build();
        TikTokBusinessSdk.trackTTEvent(adRevenueInfo);
    }
});
```

### [AdMob](https://developers.google.com/admob/android/impression-level-ad-revenue?hl=zh-cn)
```http
// curl
AdRequest adRequest = new AdRequest.Builder().build();
RewardedAd.load(this, "your ad unit ID", adRequest, new RewardedAdLoadCallback() {
    @Override
    public void onAdLoaded(@NonNull RewardedAd rewardedAd) {
        rewardedAd.setOnPaidEventListener(new OnPaidEventListener() {
            @Override
            public void onPaidEvent(@NonNull AdValue adValue) {
                AdapterResponseInfo loadedAdapterResponseInfo = rewardedAd.getResponseInfo().getLoadedAdapterResponseInfo();
                Bundle responseExtras = rewardedAd.getResponseInfo().getResponseExtras();
                JSONObject adRevenueJson = new JSONObject();

                long value = adValue.getValueMicros();
                String currencyCode = adValue.getCurrencyCode();
                int precisionType = adValue.getPrecisionType();
                String adUnitId = rewardedAd.getAdUnitId();
                String adSourceName = "";
                String adSourceId = "";
                String adSourceInstanceName = "";
                String adSourceInstanceId = "";
                String mediationGroupName = "";
                String mediationAbTestName = "";
                String mediationAbTestVariant = "";
                if (loadedAdapterResponseInfo != null){
                    adSourceName = loadedAdapterResponseInfo.getAdSourceName();
                    adSourceId = loadedAdapterResponseInfo.getAdSourceId();
                    adSourceInstanceName = loadedAdapterResponseInfo.getAdSourceInstanceName();
                    adSourceInstanceId = loadedAdapterResponseInfo.getAdSourceInstanceId();
                }
                if (responseExtras != null){
                    mediationGroupName = responseExtras.getString("mediation_group_name");
                    mediationAbTestName = responseExtras.getString("mediation_ab_test_name");
                    mediationAbTestVariant = responseExtras.getString("mediation_ab_test_variant");
                }
                try {
                    adRevenueJson.put("value", value);
                    adRevenueJson.put("currency_code", currencyCode);
                    adRevenueJson.put("precision", precisionType);
                    adRevenueJson.put("ad_unit_id", adUnitId);
                    adRevenueJson.put("ad_source_name", adSourceName);
                    adRevenueJson.put("ad_source_id", adSourceId);
                    adRevenueJson.put("ad_source_instance_name", adSourceInstanceName);
                    adRevenueJson.put("ad_source_instance_id", adSourceInstanceId);
                    adRevenueJson.put("mediation_group_name", mediationGroupName);
                    adRevenueJson.put("mediation_ab_test_name", mediationAbTestName);
                    adRevenueJson.put("mediation_ab_test_variant", mediationAbTestVariant);
                    adRevenueJson.put("device_ad_mediation_platform", "admob_sdk");
                    
                    //banner/interstitial/rewarded/rewarded interstitial/native/splash
                    adRevenueJson.put("ad_format", "rewarded");
                } catch (JSONException e) {
                }
                
                // Make sure the App Events SDK has been initialized before calling this
                TTBaseEvent adRevenueInfo = TTAdRevenueEvent.newBuilder(adRevenueJson).build();
                TikTokBusinessSdk.trackTTEvent(adRevenueInfo);
            }
        });
    }
});
```

### Các nhà cung cấp trung gian hòa giải khác
> **Note:** 
> Không sử dụng mã này cho nền tảng trung gian MAX, ironSource hoặc AdMob.

```http
// curl
JSONObject adRevenueJson = new JSONObject();
try {
    adRevenueJson.put("device_ad_mediation_platform", "<publisher sdk>");
    adRevenueJson.put("value", "<value>");
    adRevenueJson.put("currency", "<ISO 3-letter currency code e.g. USD>");
    adRevenueJson.put("location_country", "<ISO 2-letter country code e.g. US>");
    adRevenueJson.put("ad_revenue_network", "<Ad source/network, e.g. AdMob>");
    adRevenueJson.put("ad_format", "Ad unit format, e.g. banner|interstitial|native|rewarded");
    adRevenueJson.put("precision", "Ad revenue precision level");
} catch (JSONException e) {
}
// Make sure the App Events SDK has been initialized before calling this
TTBaseEvent adRevenueInfo = TTAdRevenueEvent.newBuilder(adRevenueJson).build();
TikTokBusinessSdk.trackTTEvent(adRevenueInfo);
```

## iOS
### [MAX](https://developers.axon.ai/en/max/ios/overview/advanced-settings#impression-level-user-revenue-api)
```http
// curl
// Obj-C

- (void)didPayRevenueForAd:(MAAd *)ad {

    double revenue = ad.revenue;
    NSString *countryCode = [ALSdk shared].configuration.countryCode;
    NSString *networkName = ad.networkName;
    NSString *adUnitId = ad.adUnitIdentifier;
    MAAdFormat *adFormat = ad.format;
    NSString *placement = ad.placement ?: @"";
    NSString *networkPlacement = ad.networkPlacement ?: @"";
    NSString *adUnitIdentifier = ad.adUnitIdentifier;

    NSMutableDictionary *adRevenue = NSMutableDictionary.dictionary;
    [adRevenue setObject:@"applovin_max_sdk" forKey:@"device_ad_mediation_platform"];
    [adRevenue setObject:@(revenue) forKey:@"revenue"];
    [adRevenue setObject:countryCode forKey:@"country_code"];
    [adRevenue setObject:networkName forKey:@"network_name"];
    [adRevenue setObject:adFormat.label forKey:@"ad_format"];
    [adRevenue setObject:placement forKey:@"placement"];
    [adRevenue setObject:networkPlacement forKey:@"network_placement"];
    [adRevenue setObject:adUnitIdentifier forKey:@"ad_unit_id"];

    // Make sure the App Events SDK has been initialized before calling this
    TikTokAdRevenueEvent *adRevenueEvent = [[TikTokAdRevenueEvent alloc] initWithAdRevenue:adRevenue];
    [TikTokBusiness trackTTEvent:adRevenueEvent];
}
```

```http
// curl
// Swift

func didPayRevenue(_ ad: MAAd) {
    let revenue = ad.revenue
    let countryCode = ALSdk.shared().configuration.countryCode
    let networkName = ad.networkName
    let adFormat = ad.format
    let placement = ad.placement ?? ""
    let networkPlacement = ad.networkPlacement ?? ""
    let adUnitIdentifier = ad.adUnitIdentifier

    let adRevenue: [String: Any] = [
        "device_ad_mediation_platform": "applovin_max_sdk",
        "revenue": revenue,
        "country_code": countryCode,
        "network_name": networkName,
        "ad_format": adFormat.label,
        "placement": placement,
        "network_placement": networkPlacement,
        "ad_unit_id": adUnitIdentifier
    ]

    // Make sure the App Events SDK has been initialized before calling this
    let adRevenueEvent = TikTokAdRevenueEvent(adRevenue: adRevenue, eventId: "")
    TikTokBusiness.trackTTEvent(adRevenueEvent)
}
```

### [ironSource](https://developers.is.com/ironsource-mobile/ios/ad-revenue-measurement-integration/#step-1)
```http
// curl
// Obj-C

- (void)impressionDataDidSucceed:(ISImpressionData *)impressionData {
    if (!impressionData) return;

    NSString *auction_id = impressionData.auction_id ?: @"";
    NSString *ad_unit = impressionData.ad_unit ?: @"";
    NSString *ad_network = impressionData.ad_network ?: @"";
    NSString *instance_name = impressionData.instance_name ?: @"";
    NSString *instance_id = impressionData.instance_id ?: @"";
    NSString *country = impressionData.country ?: @"";
    NSString *placement = impressionData.placement ?: @"";
    NSNumber *revenue = impressionData.revenue ?: @0;
    NSString *precision = impressionData.precision ?: @"";
    NSString *ab = impressionData.ab ?: @"";
    NSString *segment_name = impressionData.segment_name ?: @"";
    NSNumber *lifetime_revenue = impressionData.lifetime_revenue ?: @0;
    NSString *encrypted_cpm = impressionData.encrypted_cpm ?: @"";
    NSNumber *conversion_value = impressionData.conversion_value ?: @0;

    NSMutableDictionary *adRevenue = NSMutableDictionary.dictionary;
    [adRevenue setObject:@"ironsource_sdk" forKey:@"device_ad_mediation_platform"];
    [adRevenue setObject:auction_id forKey:@"auction_id"];
    [adRevenue setObject:ad_unit forKey:@"ad_unit"];
    [adRevenue setObject:ad_network forKey:@"ad_network"];
    [adRevenue setObject:instance_name forKey:@"instance_name"];
    [adRevenue setObject:instance_id forKey:@"instance_id"];
    [adRevenue setObject:country forKey:@"country"];
    [adRevenue setObject:placement forKey:@"placement"];
    [adRevenue setObject:revenue forKey:@"revenue"];
    [adRevenue setObject:precision forKey:@"precision"];
    [adRevenue setObject:ab forKey:@"ab"];
    [adRevenue setObject:segment_name forKey:@"segment_name"];
    [adRevenue setObject:lifetime_revenue forKey:@"lifetime_revenue"];
    [adRevenue setObject:encrypted_cpm forKey:@"encrypted_cpm"];
    [adRevenue setObject:conversion_value forKey:@"conversion_value"];

    // Make sure the App Events SDK has been initialized before calling this
    TikTokAdRevenueEvent *adRevenueEvent = [[TikTokAdRevenueEvent alloc] initWithAdRevenue:adRevenue];
    [TikTokBusiness trackTTEvent:adRevenueEvent];
}
```

```http
// curl
// Swift

func impressionDataDidSucceed(_ impressionData: ISImpressionData!) {
    guard let impressionData = impressionData else { return }

    let auctionId = impressionData.auction_id ?? ""
    let adUnit = impressionData.ad_unit ?? ""
    let adNetwork = impressionData.ad_network ?? ""
    let instanceName = impressionData.instance_name ?? ""
    let instanceId = impressionData.instance_id ?? ""
    let country = impressionData.country ?? ""
    let placement = impressionData.placement ?? ""
    let revenue = impressionData.revenue ?? 0
    let precision = impressionData.precision ?? ""
    let ab = impressionData.ab ?? ""
    let segmentName = impressionData.segment_name ?? ""
    let lifetimeRevenue = impressionData.lifetime_revenue ?? 0
    let encryptedCPM = impressionData.encrypted_cpm ?? ""
    let conversionValue = impressionData.conversion_value ?? 0

    let adRevenue: [String: Any] = [
        "device_ad_mediation_platform": "ironsource_sdk",
        "auction_id": auctionId,
        "ad_unit": adUnit,
        "ad_network": adNetwork,
        "instance_name": instanceName,
        "instance_id": instanceId,
        "country": country,
        "placement": placement,
        "revenue": revenue,
        "precision": precision,
        "ab": ab,
        "segment_name": segmentName,
        "lifetime_revenue": lifetimeRevenue,
        "encrypted_cpm": encryptedCPM,
        "conversion_value": conversionValue
    ]

    // Make sure the App Events SDK has been initialized before calling this
    let adRevenueEvent = TikTokAdRevenueEvent(adRevenue: adRevenue, eventId: "")
    TikTokBusiness.trackTTEvent(adRevenueEvent)
}
```

### [AdMob](https://developers.google.com/admob/ios/impression-level-ad-revenue?hl=zh-cn)
```http
// curl
// Obj-C

@interface ViewController ()

@property(nonatomic, strong) GADRewardedAd *rewardedAd;

@end

@implementation ViewController

- (void)requestRewardedAd {
    
    __weak ViewController *weakSelf = self;
    GADRequest *request = [GADRequest request];
    
    [GADRewardedAd loadWithAdUnitID:@"ad unit ID"
                            request:request
                  completionHandler:^(GADRewardedAd *ad, NSError *error) {
        
        if (error) {
            NSLog(@"Rewarded ad failed to load with error: %@", [error localizedDescription]);
            return;
        }
        
        self.rewardedAd = ad;
        self.rewardedAd.paidEventHandler = ^void(GADAdValue *_Nonnull value) {
            
            ViewController *strongSelf = weakSelf;
            NSDecimalNumber *revenueValue = value.value;
            NSString *currencyCode = value.currencyCode;
            GADAdValuePrecision precision = value.precision;
            NSString *adUnitId = strongSelf.rewardedAd.adUnitID;
            GADAdNetworkResponseInfo *loadedAdNetworkResponseInfo = strongSelf.rewardedAd.responseInfo.loadedAdNetworkResponseInfo;
            NSString *adSourceName = loadedAdNetworkResponseInfo.adSourceName ?: @"";
            NSString *adSourceID = loadedAdNetworkResponseInfo.adSourceID ?: @"";
            NSString *adSourceInstanceName = loadedAdNetworkResponseInfo.adSourceInstanceName ?: @"";
            NSString *adSourceInstanceID = loadedAdNetworkResponseInfo.adSourceInstanceID ?: @"";
            NSDictionary<NSString *, id> *extras = strongSelf.rewardedAd.responseInfo.extrasDictionary;
            NSString *mediationGroupName = extras[@"mediation_group_name"] ?: @"";
            NSString *mediationABTestName = extras[@"mediation_ab_test_name"] ?: @"";
            NSString *mediationABTestVariant = extras[@"mediation_ab_test_variant"] ?: @"";
            
            NSMutableDictionary *adRevenue = NSMutableDictionary.dictionary;
            [adRevenue setObject:@"admob_sdk" forKey:@"device_ad_mediation_platform"];
            [adRevenue setObject:revenueValue forKey:@"value"];
            [adRevenue setObject:currencyCode forKey:@"currency_code"];
            [adRevenue setObject:@(precision) forKey:@"precision"];
            [adRevenue setObject:adUnitId forKey:@"ad_unit_id"];
            [adRevenue setObject:adSourceName forKey:@"ad_source_name"];
            [adRevenue setObject:adSourceID forKey:@"ad_source_id"];
            [adRevenue setObject:adSourceInstanceName forKey:@"ad_source_instance_name"];
            [adRevenue setObject:adSourceInstanceID forKey:@"ad_source_instance_id"];
            [adRevenue setObject:mediationGroupName forKey:@"mediation_group_name"];
            [adRevenue setObject:mediationABTestName forKey:@"mediation_ab_test_name"];
            [adRevenue setObject:mediationABTestVariant forKey:@"mediation_ab_test_variant"];

            // banner/interstitial/rewarded/rewarded interstitial/native/splash
            [adRevenue setObject:@"rewarded" forKey:@"ad_format"];

            // Make sure the App Events SDK has been initialized before calling this
            TikTokAdRevenueEvent *adRevenueEvent = [[TikTokAdRevenueEvent alloc] initWithAdRevenue:adRevenue];
            [TikTokBusiness trackTTEvent:adRevenueEvent];
        };
    }];
}

@end
```

```http
// curl
// Swift

final class ViewController: UIViewController {
    private var rewardedAd: GADRewardedAd?

    func requestRewardedAd() {
        let request = GADRequest()

        GADRewardedAd.load(
            withAdUnitID: "ad unit ID",
            request: request
        ) { [weak self] ad, error in
            if let error = error {
                print("Rewarded ad failed to load with error: \(error.localizedDescription)")
                return
            }

            guard let self = self, let ad = ad else { return }
            self.rewardedAd = ad
            ad.paidEventHandler = { [weak self] value in
                guard let self = self, let rewardedAd = self.rewardedAd else { return }

                let revenueValue = value.value
                let currencyCode = value.currencyCode
                let precision = value.precision
                let adUnitId = rewardedAd.adUnitID
                let responseInfo = rewardedAd.responseInfo
                let loadedAdNetworkResponseInfo = responseInfo.loadedAdNetworkResponseInfo
                let extras = responseInfo.extrasDictionary

                let adSourceName = loadedAdNetworkResponseInfo?.adSourceName ?? ""
                let adSourceID = loadedAdNetworkResponseInfo?.adSourceID ?? ""
                let adSourceInstanceName = loadedAdNetworkResponseInfo?.adSourceInstanceName ?? ""
                let adSourceInstanceID = loadedAdNetworkResponseInfo?.adSourceInstanceID ?? ""
                let mediationGroupName = extras["mediation_group_name"] as? String ?? ""
                let mediationABTestName = extras["mediation_ab_test_name"] as? String ?? ""
                let mediationABTestVariant = extras["mediation_ab_test_variant"] as? String ?? ""

                let adRevenue: [String: Any] = [
                    "device_ad_mediation_platform": "admob_sdk",
                    "value": revenueValue,
                    "currency_code": currencyCode,
                    "precision": precision.rawValue,
                    "ad_unit_id": adUnitId,
                    "ad_source_name": adSourceName,
                    "ad_source_id": adSourceID,
                    "ad_source_instance_name": adSourceInstanceName,
                    "ad_source_instance_id": adSourceInstanceID,
                    "mediation_group_name": mediationGroupName,
                    "mediation_ab_test_name": mediationABTestName,
                    "mediation_ab_test_variant": mediationABTestVariant,

                    // banner/interstitial/rewarded/rewarded interstitial/native/splash
                    "ad_format": "rewarded"
                ]

                // Make sure the App Events SDK has been initialized before calling this
                let adRevenueEvent = TikTokAdRevenueEvent(adRevenue: adRevenue, eventId: "")
                TikTokBusiness.trackTTEvent(adRevenueEvent)
            }
        }
    }
}
```

### Các nhà cung cấp trung gian hòa giải khác
> **Note:** 
> Không sử dụng mã này cho nền tảng trung gian MAX, ironSource hoặc AdMob.

```http
// curl
// Obj-C

NSMutableDictionary *adRevenue = NSMutableDictionary.dictionary;
[adRevenue setObject:@"<publisher sdk>" forKey:@"device_ad_mediation_platform"];
[adRevenue setObject:@"<value>" forKey:@"value"];
[adRevenue setObject:@"<ISO 3-letter currency code e.g. USD>" forKey:@"currency"];
[adRevenue setObject:@"<ISO 2-letter country code e.g. US>" forKey:@"location_country"];
[adRevenue setObject:@"<Ad source/network, e.g. AdMob>" forKey:@"ad_revenue_network"];
[adRevenue setObject:@"Ad unit format, e.g. banner|interstitial|native|rewarded" forKey:@"ad_format"];
[adRevenue setObject:@"Ad revenue precision level" forKey:@"precision"];

// Make sure the App Events SDK has been initialized before calling this
TikTokAdRevenueEvent *adRevenueEvent = [[TikTokAdRevenueEvent alloc] initWithAdRevenue:adRevenue];
[TikTokBusiness trackTTEvent:adRevenueEvent];
```

```http
// curl
// Swift

let adRevenue: [String: Any] = [
    "device_ad_mediation_platform": "<publisher sdk>",
    "value": "<value>",
    "currency": "<ISO 3-letter currency code e.g. USD>",
    "location_country": "<ISO 2-letter country code e.g. US>",
    "ad_revenue_network": "<Ad source/network, e.g. AdMob>",
    "ad_format": "Ad unit format, e.g. banner|interstitial|native|rewarded",
    "precision": "Ad revenue precision level"
]

// Make sure the App Events SDK has been initialized before calling this
let adRevenueEvent = TikTokAdRevenueEvent(adRevenue: adRevenue, eventId: "")
TikTokBusiness.trackTTEvent(adRevenueEvent)
```

## Unity
### [MAX](https://developers.axon.ai/en/max/unity/overview/advanced-settings/#ad-placements)
```http
// curl
private void OnAdRevenuePaidEvent(string adUnitId, MaxSdk.AdInfo adInfo)
{
  double revenue = adInfo.Revenue;

  // Miscellaneous data
  string countryCode = MaxSdk.GetSdkConfiguration().CountryCode;
  string networkName = adInfo.NetworkName; 
  string adUnitIdentifier = adInfo.AdUnitIdentifier; 
  string placement = adInfo.Placement ?? ""; 
  string networkPlacement = adInfo.NetworkPlacement ?? ""; 
  string format = adInfo.AdFormat;

  Dictionary<string, object> adRevenue = new Dictionary<string, object>();
  adRevenue.Add("device_ad_mediation_platform","applovin_max_sdk");
  adRevenue.Add("revenue",revenue);
  adRevenue.Add("country_code",countryCode);
  adRevenue.Add("network_name",networkName);
  adRevenue.Add("ad_format",format);  
  adRevenue.Add("ad_unit_id",adUnitIdentifier);
  adRevenue.Add("placement",placement);
  adRevenue.Add("network_placement",networkPlacement);

  // Make sure the App Events SDK has been initialized before calling this
  TikTokAdRevenueEvent adRevenueEvent = new TikTokAdRevenueEvent(adRevenue);
  TikTokBusinessSDK.TrackTTEvent(adRevenueEvent);
}
```

### [ironSource](https://developers.is.com/ironsource-mobile/unity/ad-revenue-measurement-integration/)
```http
// curl
private void ImpressionDataReadyEvent(IronSourceImpressionData impressionData)
{
    if (impressionData == null) return;

    String auction_id = impressionData.auctionId ?? "";
    String ad_unit = impressionData.adUnit ?? "";
    String ad_network = impressionData.adNetwork ?? "";
    String instance_name = impressionData.instanceName ?? "";
    String instance_id = impressionData.instanceId ?? "";
    String country = impressionData.country ?? "";
    String placement = impressionData.placement ?? "";
    Double revenue = impressionData.revenue;
    String precision = impressionData.precision ?? "";
    String ab = impressionData.ab ?? "";
    String segment_name = impressionData.segmentName ?? "";
    Double lifetime_revenue = impressionData.lifetimeRevenue;
    String encrypted_cpm = impressionData.encryptedCPM ?? "";
    String conversion_value = impressionData.conversionValue ?? "";

    Dictionary<string, object> adRevenue = new Dictionary<string, object>();
    adRevenue.Add("device_ad_mediation_platform","ironsource_sdk");
    adRevenue.Add("auction_id",auction_id);
    adRevenue.Add("ad_unit",ad_unit);
    adRevenue.Add("ad_network",ad_network);
    adRevenue.Add("instance_name",instance_name);
    adRevenue.Add("instance_id",instance_id);
    adRevenue.Add("country",country);
    adRevenue.Add("placement",placement);
    adRevenue.Add("revenue",revenue);
    adRevenue.Add("precision",precision);
    adRevenue.Add("ab",ab);
    adRevenue.Add("segment_name",segment_name);
    adRevenue.Add("lifetime_revenue",lifetime_revenue);
    adRevenue.Add("encrypted_cpm",encrypted_cpm);
    adRevenue.Add("conversion_value",conversion_value);

    // Make sure the App Events SDK has been initialized before calling this
    TikTokAdRevenueEvent adRevenueEvent = new TikTokAdRevenueEvent(adRevenue);
    TikTokBusinessSDK.TrackTTEvent(adRevenueEvent);
}
```

### [AdMob](https://developers.google.com/admob/unity/impression-level-ad-revenue?hl=zh-cn)
```http
// curl
private RewardedAd _rewardedAd;

private void LoadRewardedAd()
{
    AdRequest adRequest = new AdRequest();
    RewardedAd.Load("AD_UNIT_ID", adRequest, (RewardedAd rewardedAd, LoadAdError error) =>
   {      
       _rewardedAd = rewardedAd;
       if (error != null)      
       {         
           Debug.LogError("Rewarded ad failed to load an ad with error : " + error);              return;      
       }      
       rewardedAd.OnAdPaid += this.HandleAdPaidEvent;   
  });
}

public void HandleAdPaidEvent(AdValue adValue)
{
    long valueMicros = adValue.Value;    
    string currencyCode = adValue.CurrencyCode;    
    PrecisionType precision = adValue.Precision;    
    ResponseInfo responseInfo = _rewardedAd.GetResponseInfo();    
    string responseId = responseInfo.GetResponseId();    
    AdapterResponseInfo loadedAdapterResponseInfo = responseInfo.GetLoadedAdapterResponseInfo();    
    string adSourceId = "";    
    string adSourceInstanceId = "";    
    string adSourceInstanceName = "";    
    string adSourceName = "";    
    string adapterClassName = "";    
    long latencyMillis = 0;             
    Dictionary credentials = null; 
    if (loadedAdapterResponseInfo != null)
    {
        adSourceId = loadedAdapterResponseInfo.AdSourceId ?? "";
        adSourceInstanceId = loadedAdapterResponseInfo.AdSourceInstanceId ?? "";
        adSourceInstanceName = loadedAdapterResponseInfo.AdSourceInstanceName ?? "";
        adSourceName = loadedAdapterResponseInfo.AdSourceName ?? "";
        adapterClassName = loadedAdapterResponseInfo.AdapterClassName ?? "";
        latencyMillis = loadedAdapterResponseInfo.LatencyMillis;
        credentials = loadedAdapterResponseInfo.AdUnitMapping;
    }
    Dictionary extras = responseInfo.GetResponseExtras();    
    string mediationGroupName = "";
    string mediationABTestName = "";
    string mediationABTestVariant = "";
    if (extras != null)
    {
        extras.TryGetValue("mediation_group_name", out mediationGroupName);
        extras.TryGetValue("mediation_ab_test_name", out mediationABTestName);
        extras.TryGetValue("mediation_ab_test_variant", out mediationABTestVariant);
        mediationGroupName = mediationGroupName ?? "";
        mediationABTestName = mediationABTestName ?? "";
        mediationABTestVariant = mediationABTestVariant ?? "";
    }

    Dictionary adRevenue = new Dictionary();
    adRevenue.Add("device_ad_mediation_platform","admob_sdk");
    adRevenue.Add("value",valueMicros);
    adRevenue.Add("currency_code",currencyCode);
    adRevenue.Add("precision",precision);
    adRevenue.Add("ad_unit_id",_rewardedAd.getAdUnitId());   
    adRevenue.Add("ad_source_name",adSourceName);
    adRevenue.Add("ad_source_id",adSourceId);
    adRevenue.Add("ad_source_instance_name",adSourceInstanceName);
    adRevenue.Add("ad_source_instance_id",adSourceInstanceId);
    adRevenue.Add("mediation_group_name",mediationGroupName);
    adRevenue.Add("mediation_ab_test_name",mediationABTestName);
    adRevenue.Add("mediation_ab_test_variant",mediationABTestVariant);

    //banner/interstitial/rewarded/rewarded interstitial/native/app open ad
    adRevenue.Add("ad_format","rewarded");

    // Make sure the App Events SDK has been initialized before calling this
    TikTokAdRevenueEvent adRevenueEvent = new TikTokAdRevenueEvent(adRevenue);
    TikTokBusinessSDK.TrackTTEvent(adRevenueEvent);

}
```

### Các nhà cung cấp trung gian hòa giải khác
> **Note:** 
> Không sử dụng mã này cho nền tảng trung gian MAX, ironSource hoặc AdMob.

```http
// curl
Dictionary<string, object> adRevenue = new Dictionary<string, object>();
adRevenue.Add("device_ad_mediation_platform","<publisher sdk>");
adRevenue.Add("value","<value>");
adRevenue.Add("currency","<ISO 3-letter currency code e.g. USD>");
adRevenue.Add("location_country","<ISO 2-letter country code e.g. US>");
adRevenue.Add("ad_revenue_network","<Ad source/network, e.g. AdMob>");
adRevenue.Add("ad_format","Ad unit format, e.g. banner|interstitial|native|rewarded");  
adRevenue.Add("precision","Ad revenue precision level");

// Make sure the App Events SDK has been initialized before calling this
TikTokAdRevenueEvent adRevenueEvent = new TikTokAdRevenueEvent(adRevenue);
TikTokBusinessSDK.TrackTTEvent(adRevenueEvent);
```

---

<a id="doc-1824048384831554"></a>
<!-- doc_id: 1824048384831554 -->
<!-- doc_id: 1824048384831554 -->
# Chia sẻ dữ liệu sau khi người dùng đồng ý (Data sharing after user consent)
> Đường dẫn: Marketing API > Ad Measurement > Guides > TikTok App Events SDK > Compliance best practices > Resources for data sharing after user consent
Khi tích hợp TikTok App Events SDK, bạn bắt buộc theo [Điều khoản sản phẩm thương mại TikTok (Dữ liệu)](https://ads.tiktok.com/i18n/official/policy/business-products-terms) phải có cơ sở pháp lý hợp lệ để thu thập và xử lý dữ liệu người dùng. Tại các khu vực pháp lý chịu sự điều chỉnh của Chỉ thị ePrivacy và các khuôn khổ bảo vệ dữ liệu tương tự, điều này thường yêu cầu phải có sự đồng ý trước của người dùng trước khi bắt đầu bất kỳ hoạt động truyền dữ liệu nào qua SDK.

TikTok App Events SDK được thiết kế để tự động ghi nhật ký các sự kiện ứng dụng tiêu chuẩn như cài đặt ứng dụng, khởi chạy ứng dụng và mua hàng trong ứng dụng. Các sự kiện này được gửi tới TikTok khi mở ứng dụng và được dùng cho báo cáo thông tin chi tiết, tạo tệp đối tượng và tối ưu hóa phân phối quảng cáo.

Nhằm hỗ trợ bạn tuân thủ các yêu cầu pháp lý (bao gồm luật bảo vệ dữ liệu của EU và điều khoản dữ liệu của chúng tôi), chúng tôi đã tổng hợp các tài nguyên giúp bạn xây dựng hoặc tích hợp cơ chế đồng ý vào trải nghiệm ứng dụng của mình.

## Trì hoãn theo dõi trước khi người dùng đồng ý
TikTok App Events SDK được thiết kế để tự động truyền dữ liệu tới TikTok khi ứng dụng được mở. TikTok cung cấp các công cụ cho phép bạn trì hoãn việc truyền dữ liệu cho đến khi người dùng hoàn thành luồng đồng ý trong ứng dụng.
### Android
Theo mặc định, SDK sẽ tự động ghi nhật ký và gửi sự kiện khi khởi tạo. Nếu bạn cần nhận được sự đồng ý của người dùng trước khi gửi dữ liệu, hãy gọi `disableAutoStart()` trong quá trình cấu hình. Lệnh này cho phép SDK xếp các sự kiện vào hàng đợi cục bộ mà không gửi đi.
```http
// curl
TTConfig ttConfig = new TTConfig(getApplicationContext(), "YOUR_APP_SECRET")
    .setAppId("YOUR_APP_ID")
    .setTTAppId("YOUR_TIKTOK_APP_ID")
    .disableAutoStart(); // Add this line

TikTokBusinessSdk.initializeSdk(ttConfig);
```

Sau khi sự đồng ý được cấp, hãy gọi lệnh `startTrack()` để bắt đầu gửi tất cả các sự kiện đã xếp hàng đợi và các sự kiện trong tương lai tới TikTok.
```http
// curl
// Call this after user provides consent
TikTokBusinessSdk.startTrack();
```

### iOS
Theo mặc định, SDK tự động ghi nhật ký và gửi sự kiện khi khởi tạo. Nếu bạn cần nhận sự đồng ý của người dùng trước khi gửi dữ liệu, hãy gọi lệnh `disableTracking()` trong khi cấu hình. Thao tác này giúp SDK lưu sự kiện vào hàng đợi cục bộ thay vì gửi đi ngay.
#### Bộ hẹn giờ App Tracking Transparency (ATT)
Để trì hoãn việc gửi sự kiện trong lần khởi chạy đầu tiên cho đến khi người dùng hoàn tất luồng đồng ý ATT, bạn có thể gọi hàm `setDelayForATTUserAuthorizationInSeconds` để đợi người dùng cấp quyền ATT trước khi gửi sự kiện.

```http
// curl
// Swift
guard let config = TikTokConfig(accessToken: "YOUR_APP_SECRET", appId: "YOUR_APP_ID", tiktokAppId: "YOUR_TIKTOK_APP_ID") else {
    return true
}
config.setDelayForATTUserAuthorizationInSeconds(60) // If users need 60 seconds to finish providing ATT consent, delay the initial flush by the same period of time.

TikTokBusiness.initializeSdk(config)
```

   
```http
// curl
// Objective-C
TikTokConfig *config = [TikTokConfig configWithAccessToken:@"YOUR_APP_SECRET" appId:@"YOUR_APP_ID" tiktokAppId:@"YOUR_TIKTOK_APP_ID"];
[config setDelayForATTUserAuthorizationInSeconds:60]; // If users need 60 seconds to finish providing ATT consent, delay the initial flush by the same period of time.

[TikTokBusiness initializeSdk:config];
```

Sau đó, bạn có thể gọi `requestTrackingAuthorizationWithCompletionHandler` một cách riêng biệt để hiển thị hộp thoại nhắc cấp quyền ATT.
```http
// curl
// Swift
**func** applicationDidBecomeActive(_ application: UIApplication) {
    TikTokBusiness.requestTrackingAuthorizationWithCompletionHandler();
}
```

   
```http
// curl
*// Objective-C *
- (void)applicationDidBecomeActive:(UIApplication *)application { 
    [TikTokBusiness requestTrackingAuthorizationWithCompletionHandler]; 
}
```

##### Trì hoãn thủ công (Manual delay)
Bạn cũng có thể gọi `disableTracking()` thủ công trong quá trình cấu hình nếu cơ chế trì hoãn theo thời gian không đáp ứng yêu cầu của bạn.

```http
// curl
// Swift
guard let config = TikTokConfig(accessToken: "YOUR_APP_SECRET", appId: "YOUR_APP_ID", tiktokAppId: "YOUR_TIKTOK_APP_ID") else {
    return true
}
config.disableTracking() // Add this line

TikTokBusiness.initializeSdk(config)
```

```http
// curl
// Objective-C
TikTokConfig *config = [TikTokConfig configWithAccessToken:@"YOUR_APP_SECRET" appId:@"YOUR_APP_ID" tiktokAppId:@"YOUR_TIKTOK_APP_ID"];
[config disableTracking]; // Add this line

[TikTokBusiness initializeSdk:config];
```

Sau khi sự đồng ý được cấp, hãy gọi `setTrackingEnabled(true)` để bắt đầu gửi tất cả các sự kiện trong hàng đợi và tương lai tới TikTok.
```http
// curl
// Swift
// Call this after user provides consent
TikTokBusiness.setTrackingEnabled(true)
```

```http
// curl
// Objective-C
// Call this after user provides consent
[TikTokBusiness setTrackingEnabled:YES];
```

### Unity
Theo mặc định, SDK tự động ghi nhật ký và gửi sự kiện khi khởi tạo. Nếu bạn cần sự đồng ý của người dùng trước, hãy gọi lệnh `DisableTrack()` trong khi cấu hình để SDK xếp sự kiện vào hàng đợi cục bộ mà không gửi đi.
```http
// curl
TikTokConfig config = new TikTokConfig(/*...*/);
config.DisableTrack(); // Add this line

TikTokBusinessSDK.InitializeSdk(config);
```

Khi người dùng đã đồng ý, hãy gọi lệnh `StartTrack()` để gửi toàn bộ sự kiện đã xếp hàng đợi và các sự kiện trong tương lai.
```http
// curl
// Call this after user provides consent
TikTokBusinessSDK.StartTrack();
```

### React Native
Khởi tạo SDK với tính năng theo dõi bị tắt, sau đó tiếp tục theo dõi sau khi người dùng cấp quyền đồng ý.

```http
// curl
import TikTokBusinessSDK from '@tiktok-for-business/react-native-sdk';

await TikTokBusinessSDK.initialize({
  appId: 'YOUR_APP_ID',
  accessToken: 'YOUR_ACCESS_TOKEN',
  tiktokAppId: ['YOUR_TIKTOK_APP_ID'],
  disableTrack: true, // Add this line
});
```

Sau khi người dùng cấp quyền đồng ý:
```http
// curl
// Call this after user provides consent
await TikTokBusinessSDK.startTrack();
```

## Tắt tính năng tự động thu thập sự kiện
TikTok App Events SDK được thiết kế để tự động ghi nhật ký các sự kiện ứng dụng tiêu chuẩn như cài đặt ứng dụng, khởi chạy ứng dụng và mua hàng. Bạn có tùy chọn tắt tính năng tự động ghi nhật ký sự kiện này.
> **Important:** 
> Tắt tính năng tự động ghi nhật ký đồng nghĩa với việc các sự kiện như cài đặt ứng dụng và khởi chạy ứng dụng sẽ không còn được theo dõi theo mặc định. Nếu cần các sự kiện này cho mục đích đo lường hoặc phân tích, bạn phải triển khai ghi nhật ký thủ công trong mã nguồn ứng dụng.

### Android
```http
// curl
TTConfig ttConfig = new TTConfig(getApplicationContext(), "YOUR_APP_SECRET")
    // ... other configurations

    // Option 1: Disable ALL automatic events (Install, Launch, 2DRetention, Purchase)
    .disableAutoEvents()

    // Option 2: Disable specific automatic events
    .disableInstallLogging() // Disable install reporting only
    .disableLaunchLogging() // Disable automatic app launch reporting only
    .disableRetentionLogging() // Disable automatic 2DRetention reporting only
    .disableAutoIapTrack() // Disable automatic Purchase reporting only
    
TikTokBusinessSdk.initializeSdk(ttConfig);
```

### iOS
```http
// curl
// Swift
guard let config = TikTokConfig(accessToken: "YOUR_APP_SECRET", appId: "YOUR_APP_ID", tiktokAppId: "YOUR_TIKTOK_APP_ID") else {
    return true
}

// Option 1: Disable ALL automatic events
config.disableAutomaticTracking()

// Option 2: Disable specific automatic events
config.disableInstallTracking()
config.disableLaunchTracking()
config.disableRetentionTracking()
config.disablePaymentTracking()

TikTokBusiness.initializeSdk(config)
```

```http
// curl
// Objective-C
TikTokConfig *config = [TikTokConfig configWithAccessToken:@"YOUR_APP_SECRET" appId:@"YOUR_APP_ID" tiktokAppId:@"YOUR_TIKTOK_APP_ID"];

// Option 1: Disable ALL automatic events
[config disableAutomaticTracking];

// Option 2: Disable specific automatic events
[config disableInstallTracking];
[config disableLaunchTracking];
[config disableRetentionTracking];
[config disablePaymentTracking];

[TikTokBusiness initializeSdk:config];
```

### Unity
```http
// curl
TikTokConfig config = new TikTokConfig(/*...*/);

// Option 1: Disable ALL automatic events
config.DisableAutoTrack();

// Option 2: Disable specific automatic events
config.DisableInstallTrack();
config.DisableLaunchTrack();
config.DisableRetentionTrack();
config.DisablePayTrack();

TikTokBusinessSDK.InitializeSdk(config);
```

### React Native
```http
// curl
await TikTokBusinessSDK.initialize({
  appId: 'YOUR_APP_ID',
  accessToken: 'YOUR_ACCESS_TOKEN',
  tiktokAppId: ['YOUR_TIKTOK_APP_ID'],

  // Disable all automatic events
  disableAutoTrack: true,

  // Or selectively disable specific automatic events:
  disableInstallTrack: true,
  disableLaunchTrack: true,
  disableRetentionTrack: true,
  disablePayTrack: true,
});
```

## Tắt tính năng tăng cường gửi trả dữ liệu (Enhance data postback)
Tính năng Tăng cường gửi trả dữ liệu (Enhance data postback - hỗ trợ từ phiên bản SDK 1.4.0 trở đi) tự động thu thập thông tin trang trong ứng dụng như siêu dữ liệu (metadata) và lượt nhấp nút thông qua App Events SDK. Bạn có tùy chọn tắt tính năng thu thập tự động này. Có 3 cách để kiểm soát:

| Control type | Interface | Purpose | Scope |
|---|---|---|---|
| Front-end toggle | TikTok Events Manager | Enable or disable the feature on all devices. Use this to change the setting without having to release a new app version. ⏎ Overrides client-side global toggle, and respects client-side low-performance flags if present. | Global |
| Client-side global toggle | SDK configuration | Disable the feature on all devices. Changing this setting requires a new app version release. ⏎ Defers to front-end toggle (server-side priority). | Global |
| Client-side low performance flag | SDK configuration | Optimize feature performance on low-performance devices, if you have custom device grading logic. ⏎ Enforced when global toggles are enabled. | Device-specific |

### 1. Nút bật/tắt trên giao diện Trình quản lý sự kiện
Nút bật/tắt này có trong tab Cài đặt của ứng dụng tại Trình quản lý sự kiện. Nó cho phép bật/tắt tính năng một cách linh hoạt trong TikTok Events Manager mà không cần biên dịch lại và phát hành lại ứng dụng. Nút này **ghi đè cờ vô hiệu hóa chung**, đồng thời tuân thủ cờ thiết bị hiệu năng thấp.

Nút bật/tắt này cũng áp dụng độ ưu tiên phía máy chủ. Khi triển khai SDK lần đầu tiên, trạng thái ban đầu sẽ phản ánh cài đặt phía máy khách. Mọi thay đổi tiếp theo được thực hiện trong Trình quản lý sự kiện sẽ ghi đè các cài đặt phía máy khách.
### 2. Nút bật/tắt toàn cục phía máy khách (Client-side)
Thêm cài đặt này vào cấu hình SDK để tắt tính năng **toàn cục trên tất cả thiết bị**. Sử dụng tùy chọn này khi bạn muốn **tắt hoàn toàn tính năng** bất kể loại thiết bị hoặc điều kiện runtime.
#### Android
```http
// curl
TTConfig ttConfig = new TTConfig(getApplicationContext(), "YOUR_APP_SECRET")
    .setAppId("YOUR_APP_ID")
    .setTTAppId("YOUR_TIKTOK_APP_ID")
    .disableAutoEnhancedDataPostbackEvent() // Disable Enhanced data postback

TikTokBusinessSdk.initializeSdk(ttConfig);
```

#### iOS
```http
// curl
// Swift
guard let config = TikTokConfig(accessToken: "YOUR_APP_SECRET", appId: "YOUR_APP_ID", tiktokAppId: "YOUR_TIKTOK_APP_ID") else {
    return true
}
// Add this line to disable Enhanced data postback
config.disableAutoEnhancedDataPostbackEvent()

TikTokBusiness.initializeSdk(config)
```

```http
// curl
// Objective-C
TikTokConfig *config = [TikTokConfig configWithAccessToken:@"YOUR_APP_SECRET" appId:@"YOUR_APP_ID" tiktokAppId:@"YOUR_TIKTOK_APP_ID"];
// Add this line to disable Enhanced data postback
[config disableAutoEnhancedDataPostbackEvent];

[TikTokBusiness initializeSdk:config];
```

#### Unity
```http
// curl
// C#
TikTokConfig config = new TikTokConfig("YOUR_IOS_APP_SECRET", "YOUR_IOS_APP_ID", "YOUR_IOS_TIKTOK_APP_ID", "YOUR_ANDROID_APP_SECRET", "YOUR_ANDROID_APP_ID", "YOUR_ANDROID_TIKTOK_APP_ID");
// Add this line to disable Enhanced data postback
config.DisableEnhancedDataPostbackTrack();

TikTokBusinessSDK.InitializeSdk(config);
```

#### React Native
```http
// curl
import TikTokBusinessSDK from '@tiktok-for-business/react-native-sdk';

await TikTokBusinessSDK.initialize({
  appId: 'YOUR_APP_ID',
  accessToken: 'YOUR_ACCESS_TOKEN',
  tiktokAppId: ['YOUR_TIKTOK_APP_ID'],
  
  // Add this line to disable Enhanced data postback
  disableEnhancedDataPostbackTrack: true,
});
```

### 3. Cờ thiết bị hiệu năng thấp phía máy khách
Thêm cài đặt này vào cấu hình SDK để tối ưu hóa hiệu năng **chỉ trên các thiết bị được xác định là có hiệu năng thấp**. Sử dụng tùy chọn này nếu bạn có logic tùy chỉnh để phân loại cấu hình thiết bị và muốn tính năng hoạt động mặc định nhưng **loại trừ đối với các thiết bị bị giới hạn hiệu năng**.
#### Android
```http
// curl
TTConfig ttConfig = new TTConfig(getApplicationContext(), "YOUR_APP_SECRET")
    .setAppId("YOUR_APP_ID")
    .setTTAppId("YOUR_TIKTOK_APP_ID")
    .setIsLowPerformanceDevice(true); // Optimise feature performance on this device only

TikTokBusinessSdk.initializeSdk(ttConfig);
```

#### iOS
```http
// curl
// Swift
guard let config = TikTokConfig(accessToken: "YOUR_APP_SECRET", appId: "YOUR_APP_ID", tiktokAppId: "YOUR_TIKTOK_APP_ID") else {
    return true
}
// Add this line to optimise feature performance on this device only
config.setIsLowPerformanceDevice(true)

TikTokBusiness.initializeSdk(config)
```

```http
// curl
// Objective-C
TikTokConfig *config = [TikTokConfig configWithAccessToken:@"YOUR_APP_SECRET" appId:@"YOUR_APP_ID" tiktokAppId:@"YOUR_TIKTOK_APP_ID"];
// Add this line to optimise feature performance on this device only
[config setIsLowPerformanceDevice:YES];

[TikTokBusiness initializeSdk:config];
```

#### Unity
```http
// curl
// C#
TikTokConfig config = new TikTokConfig("YOUR_IOS_APP_SECRET", "YOUR_IOS_APP_ID", "YOUR_IOS_TIKTOK_APP_ID", "YOUR_ANDROID_APP_SECRET", "YOUR_ANDROID_APP_ID", "YOUR_ANDROID_TIKTOK_APP_ID");
// Add this line to optimise feature performance on this device only
config.SetIsLowPerformanceDevice(true);

TikTokBusinessSDK.InitializeSdk(config);
```

#### React Native
```http
// curl
await TikTokBusinessSDK.initialize({
  appId: 'YOUR_APP_ID',
  accessToken: 'YOUR_ACCESS_TOKEN',
  tiktokAppId: ['YOUR_TIKTOK_APP_ID'],
  
  // Add this line to optimise feature performance on this device only
  setIsLowPerformanceDevice: true,
});
```

---

<a id="doc-1739585702922241"></a>
<!-- doc_id: 1739585702922241 -->
<!-- doc_id: 1739585702922241 -->
# Cài đặt Pixel bằng mã tùy chỉnh (Install Pixel using code)
> Đường dẫn: Marketing API > Ad Measurement > Guides > Pixel > Install Pixel using code
# Trước khi bắt đầu
* Bạn phải tạo một pixel trong Trình quản lý sự kiện và có quyền truy cập mã cơ sở pixel. Tìm hiểu cách tạo pixel trong [Trung tâm trợ giúp](https://ads.tiktok.com/help/article?aid=10021).
* Bạn cần có nhân sự kỹ thuật để thực hiện.
* Bạn phải có quyền truy cập vào mã nguồn trang web của bạn.

# Cài đặt Pixel
Nếu bạn đã tạo pixel trước đó nhưng chưa cài đặt trên trang web, bạn phải hoàn tất việc cài đặt trước khi tiếp tục thiết lập sự kiện.
1. Lấy mã cơ sở pixel trực tiếp từ màn hình thiết lập hoặc bạn có thể sử dụng mẫu mã cơ sở của chúng tôi. Hãy nhớ thay thế phần giữ chỗ bằng ID TikTok Pixel thực tế của bạn trước khi dùng.

```javascript
// Javascript
// BASE CODE TEMPLATE:

<script>
//Part1
!function (w, d, t) {
  w.TiktokAnalyticsObject=t;var ttq=w[t]=w[t]||[];ttq.methods=["page","track","identify","instances","debug","on","off","once","ready","alias","group","enableCookie","disableCookie"],ttq.setAndDefer=function(t,e){t[e]=function(){t.push([e].concat(Array.prototype.slice.call(arguments,0)))}};for(var i=0;i<ttq.methods.length;i++)ttq.setAndDefer(ttq,ttq.methods[i]);ttq.instance=function(t){for(var e=ttq._i[t]||[],n=0;n<ttq.methods.length;n++)ttq.setAndDefer(e,ttq.methods[n]);return e},ttq.load=function(e,n){var i="https://analytics.tiktok.com/i18n/pixel/events.js";ttq._i=ttq._i||{},ttq._i[e]=[],ttq._i[e]._u=i,ttq._t=ttq._t||{},ttq._t[e]=+new Date,ttq._o=ttq._o||{},ttq._o[e]=n||{};var o=document.createElement("script");o.type="text/javascript",o.async=!0,o.src=i+"?sdkid="+e+"&lib="+t;var a=document.getElementsByTagName("script")[0];a.parentNode.insertBefore(o,a)};

//Part 2
  ttq.load('YOUR ID TikTok Pixel WILL BE LOCATED HERE');
  ttq.page();
}(window, document, 'ttq');
</script>
```
Mã cơ sở có 2 phần:
* Phần 1 dành cho các hàm chức năng chung.
* Phần 2 chứa `ttq.load('{ID TikTok Pixel placeholder}')`, giúp tải ngữ cảnh liên quan đến pixel cụ thể dựa trên cấu hình của nó. `ttq.page()` sẽ báo cáo sự kiện xem trang (pageview), dùng để xác minh việc cài đặt mã.

2. Hoàn tất cài đặt bằng cách dán mã cơ sở vào đầu phần `<head>` trên trang web của bạn. Tiêu đề trang web bắt đầu bằng thẻ `<head>` và đóng bằng thẻ `</head>`. Dưới đây là một ví dụ:

```javascript
// Javascript
// Header example:
<!DOCTYPE html >
    <head>
          "INSERT TIKTOK PIXEL CODE HERE"
    </head>
</html>
```

# Mã sự kiện (Event codes)
Trước khi cài đặt mã sự kiện, hãy đảm bảo bạn đã cài đặt mã cơ sở đúng cách ở bước trước. Mã sự kiện không thể tự hoạt động nếu thiếu mã cơ sở.
Mã sự kiện cho phép bạn báo cáo các hành động hoặc sự kiện cụ thể mà khách truy cập thực hiện nhằm phục vụ mục đích chuyển đổi. Ví dụ: đối với doanh nghiệp thương mại điện tử, các sự kiện như "thêm vào giỏ hàng" và "thanh toán hoàn tất" rất quan trọng để đo lường. Dưới đây là danh sách các Sự kiện tiêu chuẩn hiện được TikTok Pixel và Events API hỗ trợ.
Với bất kỳ sự kiện tiêu chuẩn nào, bạn có thể gửi các tham số (thông tin bổ sung về hành động của khách truy cập, như tổng giá trị đơn hàng, tên và danh mục sản phẩm). Nếu bạn không chắc chắn nên dùng tham số nào, hãy xem 'các tham số đề xuất' trong bảng.

| Event | Description | Event Code | Recommended parameters |
|---|---|---|---|
| Add Payment Info | When a visitor adds their payment information at checkout. | ttq.track('AddPaymentInfo') |  |
| Add to Cart | When a visitor adds an item to the cart. | ttq.track('AddToCart') | content_type, quantity, description, content_id, currency, value |
| Add to Wishlist | When an item is added to the wishlist. | ttq.track('AddToWishlist') |  |
| Application Approval | When an application is approved. | ttq.track('ApplicationApproval') |  |
| Purchase | When a visitor makes a payment. TikTok recommends using this event when placing an order and making a payment are the same. | ttq.track('Purchase') | content_type, quantity, description, content_id, currency, value |
| Complete Registration | When a visitor signs up for something such as account registration. | ttq.track('CompleteRegistration') |  |
| Contact | When a visitor contacts you. | ttq.track('Contact') |  |
| Customize Product | When a visitor customizes a product. | ttq.track('CustomizeProduct') |  |
| Download | When a visitor downloads something from your website. | ttq.track('Download') |  |
| Find Location | When a visitor tries to find your location. | ttq.track('FindLocation') |  |
| Initiate Checkout | When a visitor proceeds to checkout. | ttq.track('InitiateCheckout') |  |
| Lead | When a visitor submits a form. | ttq.track('Lead') |  |
| Schedule | When a visitor makes an appointment to speak with your business or visit your location. | ttq.track('Schedule') |  |
| Search | When a visitor searches. | ttq.track('Search') | query |
| Start Trial | When someone begins a free trial of a product or service. | ttq.track('StartTrial') | currency, value |
| Submit Application | When someone submits an application. | ttq.track('SubmitApplication') |  |
| Subscribe | When a visitor subscribes on your website including follows, content, or paid subscriptions. | ttq.track('Subscribe') |  |
| View Content | When a visitor views a specific page. TikTok recommends measuring pages important to your business such as product comparison, announcement, or release pages. | ttq.track('ViewContent') | content_type, quantity, description, content_id, currency, value |

> **Lưu ý:** Theo mặc định, mã cơ sở pixel luôn bao gồm sự kiện "Xem trang (Page View)" để đo lường khi khách truy cập vào trang web của bạn. Do đó, không cần thêm mã sự kiện bổ sung nào để đo lường "Page View".

## Cài đặt mã sự kiện
Bạn có thể gọi hàm `ttq.track('')` ở bất kỳ vị trí nào bên trong thẻ `<script>` của trang web, khi tải trang hoặc khi khách truy cập hoàn tất một thao tác như nhấp vào nút.

**Lưu ý quan trọng:** Các ví dụ bên dưới sử dụng "pixel_id_1", "pixel_id_2" và "pixel_id_3" làm giá trị giữ chỗ trong đoạn mã mẫu để minh họa. Hãy đảm bảo bạn sử dụng ID TikTok Pixel thực tế khi triển khai.

### Đo lường sự kiện dựa trên lượt tải trang (Page load)
Nếu bạn muốn đo lường sự kiện mua hàng sau khi khách hoàn tất giao dịch, bạn có thể gọi hàm `ttq.track('')` trên trang xác nhận mua hàng của bạn (với điều kiện trang này đã tải mã cơ sở):

```html
// Javascript
<body>
  ...
  <script>
    ttq.instance('pixel_id_1').track('Purchase')
  </script>
  ...
</body>
```

### Đo lường sự kiện dựa trên lượt nhấp nút (Button click)
Nếu bạn muốn đo lường sự kiện mua hàng khi khách nhấp vào nút mua hàng, bạn có thể gắn lệnh gọi `ttq.track('')` vào sự kiện nhấp nút mua hàng trên trang thanh toán:

```html
// Javascript
<button id="addToCartButton">Purchase</button>
<script type="text/javascript">
document.getElementById("addToCartButton").onclick = function(){
    ttq.track('AddToCart',{  
	contents: [
    {
      content_id: '301',
      content_name: 'dress',
	  quantity: 1,
      price: 8,
    }],
    content_type: 'product',
    value: 8.0,
    currency: 'USD',  })
}
</script>
```

# Bảng tham số (Parameters)
Dưới đây là danh sách các tham số được TikTok Pixel và Events API hỗ trợ. Các tham số có thể kết hợp với bất kỳ sự kiện nào. Hãy xem phần mô tả để biết ví dụ cách sử dụng tham số.

| Parameter | Description | Value type | Required for Return on Ad Spend (ROAS) | Required for Video Shopping Ads | Required for Value-Based Optimization (VBO) |
|---|---|---|---|---|---|
| content_ids | Unique ID or array of multiple IDs of the products or content. ⏎ Example: `['987','654']`. ⏎ We recommend using `sku_id` or `item_group_id` that matches the `sku_id` or `item_group_id` you set up in the catalog, if available. ⏎ This field is required for Video Shopping Ads (VSA). | Must be an array of strings |  | ✅ |  |
| content_type | The `content_type` object property's value must be set to either `product`, or `product_group`. ⏎ If you use `sku_id` as `content_id`, use `product`. ⏎ If you use `item_group_id` as `content_id`, use `product_group`. ⏎ This field is required for VSA. | Must be either `product` or `product_group`. |  | ✅ |  |
| contents | A list of content objects that represent relevant products in a web event with product information. | Must be an array of objects |  | ✅ |  |
| ↳ price | The price of the item. ⏎ **Note**: **Price** is the price for a single item, and **value** is the total price of the order. For example, if you have two items each sold for $10, the price parameter would pass 10 and the value parameter would pass 20. | number |  |  |  |
| ↳ content_id | Unique ID of the product or content. ⏎ Recommend using `sku id` or `item_group_id`. This should match the `sku_id` or `item_group_id` you set up in the catalog (if available). ⏎ This field is required for VSA | string |  | ✅ |  |
| ↳ content_category | Category of the page/product | string |  |  |  |
| ↳ content_name | Name of the page/product | string |  |  |  |
| ↳ brand | Brand name of the product item. | string |  |  |  |
| currency | ISO 4217 code. Examples: `EUR`, `USD`, `JPY`. ⏎ ** List of currencies currently supported:** AED, ARS, AUD, BDT, BHD, BIF, BOB, BRL, CAD, CHF, CLP, CNY, COP, CRC, CZK, DKK, DZD, EGP, EUR, GBP, GTQ, HKD, HNL, HUF, IDR, ILS, INR, ISK, JPY, KES, KHR, KRW, KWD, KZT, MAD, MOP, MXN, MYR, NGN, NIO, NOK, NZD, OMR, PEN, PHP, PHP, PKR, PLN, PYG, QAR, RON, RUB, SAR, SEK, SGD, THB, TRY, TWD, UAH, USD, VES, VND, ZAR | enum(string) | ✅ |  |  |
| value | Value of the order or items sold. ⏎ **Note**:  • **Price** is the price for a single item, and **value** is the total price of the order. For example, if you have two items each sold for ten dollars, the `price` parameter would pass `10.00` and the `value` parameter would pass `20.00`. • Values should always be formatted as an integer or decimal (ex: 10.00) regardless of the location, currency, etc. It cannot contain any currency signs, special characters, letters, or commas. | number | ✅ |  | ✅ |
| num_items | The quantity of items. | integer |  |  |  |
| search_string | The user-entered string for search. | string |  |  |  |
| description | Description of the item or page. | string |  |  |  |
| status | Status of an order, item, or service. ⏎ **Note**: Depending on your use of `status`, Events API may be required in order to share status changes to TikTok. | string |  |  |  |

## Thêm tham số vào mã sự kiện
Bạn có thể sử dụng `ttq.track(event, [parameters]);` cho các tham số. Dưới đây là các ví dụ mã cho sự kiện Thêm vào giỏ hàng (AddToCart) đối với **một** sản phẩm và **nhiều** sản phẩm.

```javascript
// Javascript
//taking Add to Cart event as an example
// For single product 
ttq.track('AddToCart', {
   contents: [
    {
      content_id: '301',
      content_name: 'dress',
	  quantity: 1,
      price: 8,
    }],
    content_type: 'product',
    value: 8.0,
    currency: 'USD',
});

// For multiple products  
ttq.track('AddToCart', {
   contents: [
    {
      content_id: '301',
      content_name: 'dress',
	  quantity: 1,
      price: 8,
    },
    {
      content_id: '401',
      content_name: 'dress',
	  quantity: 1,
      price: 1.2,
    }],
	content_type: 'product',
    value: 9.2,
    currency: 'USD',
});
```

## Sử dụng giá trị động trong các tham số
Bạn có thể thiết lập các giá trị động để truyền dữ liệu sự kiện theo thời gian thực tới TikTok. Nhờ đó, mã động sẽ tự động xác định giá trị chính xác của sự kiện (chẳng hạn giá mua hàng) thay vì dùng giá trị cố định.

Ví dụ, nếu khách truy cập vào trang web và thêm một cuốn sách vào giỏ hàng. Dưới đây là cách hiển thị của giá trị tĩnh (cố định):

```html
// Javascript
ttq.track('AddToCart', {
   contents: [
    {
      content_id: '301',
      content_name: 'book',
	  quantity: 1,
      price: 8,
    }],
    content_type:'product',
    value: 8.0,
    currency: 'USD',
});
```
Để chuyển thành giá trị động, hãy thay thế các giá trị cố định bằng mã lập trình truyền giá trị thực tế như 'book' hoặc '10.0' một cách tự động.
```html
// Javascript
ttq.track('AddToCart', {
   contents: [
    {
      content_id: DYNAMIC_CONTENT_ID_COMES_HERE,
      content_name: DYNAMIC_PRODUCT_NAME_COMES_HERE,
	  quantity: DYNAMIC_QUANTITY_COMES_HERE,
      price: DYNAMIC_PRICE_COMES_HERE,
    }],
    content_type:'product',
    value: DYNAMIC_ORDER_VALUE_COMES_HERE,
    currency: 'USD',
});
```

# Vô hiệu hóa Pixel khi người dùng từ chối (Opt-out)

Nếu người dùng từ chối (opt-out) việc đo lường, hãy đảm bảo trang web của bạn có giao thức hoặc mã để tắt việc kích hoạt pixel. Khi pixel bị vô hiệu hóa, mọi thông tin như cookie, timestamp và sự kiện sẽ không được ghi nhận. Dưới đây là một số giải pháp đề xuất:
* Nếu đang dùng Google Tag Manager, bạn có thể sử dụng [Chế độ đồng ý của Google (Consent Mode)](https://blog.google/products/marketingplatform/360/measure-conversions-while-respecting-user-consent-choices/) để tùy biến cách các thẻ Google hoạt động trước và sau khi người dùng đưa ra quyết định.
* Nếu không có nhân sự kỹ thuật hoặc hệ thống quản lý thẻ, TikTok Pixel có thể tích hợp với nhiều nền tảng quản lý sự đồng ý (CMP) của bên thứ ba. Các nền tảng này hỗ trợ thiết kế banner đồng ý và tùy chọn triển khai dễ dàng.
* Nếu có đội ngũ kỹ thuật và không muốn phụ thuộc bên thứ ba, TikTok cung cấp [Chế độ đồng ý Cookie Pixel](do-luong-quang-cao-p2.md#doc-1795929012554754) để kiểm soát việc sử dụng cookie của pixel.

# Xác minh thiết lập Pixel và sự kiện
Sau khi hoàn tất thiết lập, có nhiều cách để kiểm tra xem pixel có đang hoạt động chính xác hay không:
1. Cài đặt tiện ích mở rộng Chrome TikTok Pixel Helper
2. Sử dụng công cụ Kiểm tra sự kiện & Chẩn đoán trong Trình quản lý sự kiện
3. Xem trước quảng cáo
4. Sử dụng chế độ gỡ lỗi (Debug mode)

## 1. Tiện ích TikTok Pixel Helper
TikTok Pixel Helper là một tiện ích mở rộng Chrome giúp bạn xác minh và khắc phục sự cố cài đặt pixel bằng cách kiểm tra lỗi và đưa ra đề xuất triển khai cho trang web của bạn.
Với Pixel Helper, bạn có thể chẩn đoán chi tiết quá trình cài đặt pixel ở mọi cấp độ, bao gồm cấp độ pixel, sự kiện và tham số. [Tìm hiểu cách sử dụng Pixel Helper](https://ads.tiktok.com/help/article?aid=9661).
 Pixel Helper mang lại nhiều lợi ích cốt lõi bao gồm:
1. **Trạng thái Pixel (Pixel status)**: Xác minh việc triển khai pixel với khả năng truy cập nhanh chi tiết cài đặt ở cấp độ pixel, sự kiện và tham số.
2. **Chẩn đoán chi tiết (Detailed diagnostics)**: Khắc phục các sự cố thiết lập phổ biến và cải thiện hiệu suất pixel bằng cách xem lại thông báo lỗi và đề xuất triển khai.
Tiện ích Pixel Helper hiện đã khả dụng. [Tải xuống Pixel Helper tại đây](https://chrome.google.com/webstore/detail/tiktok-pixel-helper/aelgobmabdmlfmiblddjfnjodalhidnn).

## 2. Kiểm tra sự kiện và Chẩn đoán (Test Events & Diagnostics)
Trong TikTok Ads Manager, điều hướng tới Trình quản lý sự kiện bằng cách nhấp vào **Công cụ (Tools)** > **Sự kiện (Events)** > **Nguồn dữ liệu (Data sources)**. Chọn một kết nối Pixel hoặc Events API để vào trang chi tiết gồm 5 tab:
- **Tổng quan (Overview)**: Xác minh thiết lập kết nối dữ liệu web hoặc theo dõi hoạt động với khả năng truy cập nhanh vào chi tiết kết nối dữ liệu web. Trạng thái sự kiện (Event Status) cho biết sự kiện pixel đang 'Hoạt động' (Active) hay 'Không có hoạt động gần đây' (No recent activity), trong khi mục Lần nhận gần nhất (Last Received) hiển thị thời điểm sự kiện được ghi nhận gần nhất. 
- **Sự kiện kiểm tra (Test Events)**: Thử nghiệm sự kiện web theo thời gian thực trong môi trường mô phỏng. Sau khi quét mã QR (pixel) hoặc gửi tải trọng test_event (Events API), bạn có thể xác minh các sự kiện được cấu hình và kích hoạt như kỳ vọng trên trang web.
- **Chẩn đoán (Diagnostics)**: Khắc phục các sự cố phổ biến và cải thiện hiệu suất pixel bằng cách xử lý lỗi và áp dụng các giải pháp khuyến nghị trong tab 'Chẩn đoán'.
- **Nhật ký thay đổi (Change Log)**: Xem mọi thay đổi trước đó đã thực hiện đối với kết nối dữ liệu web hoặc các sự kiện đã cấu hình. Nhật ký thay đổi hỗ trợ khắc phục sự cố bằng cách chỉ rõ chính xác những thay đổi nào đã diễn ra, vào lúc nào và do ai thực hiện.
- **Cài đặt (Settings)**: Xem và quản lý cài đặt TikTok Pixel, bao gồm So khớp nâng cao tự động, sử dụng cookie, tăng cường postback dữ liệu, cấu hình sự kiện, tạo mã truy cập cho Events API và tích hợp với đối tác.

Tìm hiểu cách sử dụng các công cụ Chẩn đoán bằng cách tham khảo [Trung tâm trợ giúp](https://ads.tiktok.com/help/article?aid=10000360) của chúng tôi.

## 3. Chế độ gỡ lỗi (Debug Mode)
Nếu bạn cần xem chi tiết chuyên sâu khi gỡ lỗi thiết lập pixel, chế độ gỡ lỗi (debug mode) sẵn sàng hỗ trợ bạn.

- Có hai cách để mở chế độ gỡ lỗi (debug mode):
	1. Mở [Liên kết SDK](https://analytics.tiktok.com/i18n/pixel/events.js), và chạy: `document.cookie="pixel_debug=true; expires=Thu, 18 Dec 2043 12:00:00 GMT; path=/; SameSite=None; Secure";`
	2. Làm mới trang web của bạn
- Kiểm tra các thông báo gỡ lỗi
Vui lòng mở bảng điều khiển console của trình duyệt trước. Sau đó TikTok Pixel sẽ báo cáo nhật ký gỡ lỗi trong console. Thông tin nhật ký sẽ bắt đầu bằng `[TT]`. Ví dụ:

**Nhật ký của một số nút quan trọng**
- Khi bạn gọi `ttq.load()`

- Khi bạn gọi `ttq.identify()` hoặc `ttq.instance().identify()`

- Khi bạn gọi `ttq.page()`, `ttq.track()` hoặc `ttq.instance().track()`. Trước khi báo cáo một sự kiện, hệ thống sẽ in ra console `adInfo` và `appInfo`

- Khi chúng tôi lấy thông tin từ bộ nhớ cache, url hoặc cầu nối (bridge)

# Câu hỏi thường gặp (FAQs)

**Làm cách nào để thiết lập nhiều pixel trên trang web của tôi?**

Bạn có thể làm theo mã mẫu dưới đây để xem ví dụ về 3 mã cơ sở pixel. Hãy nhớ thay thế các giá trị giữ chỗ bằng ID TikTok Pixel của bạn trước khi sử dụng mã mẫu.

```html
// Javascript
<script>
!function (w, d, t) {
  w.TiktokAnalyticsObject=t;var ttq=w[t]=w[t]||[];ttq.methods=["page","track","identify","instances","debug","on","off","once","ready","alias","group","enableCookie","disableCookie"],ttq.setAndDefer=function(t,e){t[e]=function(){t.push([e].concat(Array.prototype.slice.call(arguments,0)))}};for(var i=0;i<ttq.methods.length;i++)ttq.setAndDefer(ttq,ttq.methods[i]);ttq.instance=function(t){for(var e=ttq._i[t]||[],n=0;n<ttq.methods.length;n++)ttq.setAndDefer(e,ttq.methods[n]);return e},ttq.load=function(e,n){var i="https://analytics.tiktok.com/i18n/pixel/events.js";ttq._i=ttq._i||{},ttq._i[e]=[],ttq._i[e]._u=i,ttq._t=ttq._t||{},ttq._t[e]=+new Date,ttq._o=ttq._o||{},ttq._o[e]=n||{};var o=document.createElement("script");o.type="text/javascript",o.async=!0,o.src=i+"?sdkid="+e+"&lib="+t;var a=document.getElementsByTagName("script")[0];a.parentNode.insertBefore(o,a)};
}(window, document, 'ttq');

ttq.load('BRU69P41M9ALI4R4B2QG');
ttq.page();
</script>

<script>
!function (w, d, t) {
  w.TiktokAnalyticsObject=t;var ttq=w[t]=w[t]||[];ttq.methods=["page","track","identify","instances","debug","on","off","once","ready","alias","group","enableCookie","disableCookie"],ttq.setAndDefer=function(t,e){t[e]=function(){t.push([e].concat(Array.prototype.slice.call(arguments,0)))}};for(var i=0;i<ttq.methods.length;i++)ttq.setAndDefer(ttq,ttq.methods[i]);ttq.instance=function(t){for(var e=ttq._i[t]||[],n=0;n<ttq.methods.length;n++)ttq.setAndDefer(e,ttq.methods[n]);return e},ttq.load=function(e,n){var i="https://analytics.tiktok.com/i18n/pixel/events.js";ttq._i=ttq._i||{},ttq._i[e]=[],ttq._i[e]._u=i,ttq._t=ttq._t||{},ttq._t[e]=+new Date,ttq._o=ttq._o||{},ttq._o[e]=n||{};var o=document.createElement("script");o.type="text/javascript",o.async=!0,o.src=i+"?sdkid="+e+"&lib="+t;var a=document.getElementsByTagName("script")[0];a.parentNode.insertBefore(o,a)};
}(window, document, 'ttq');

ttq.load('pixel_id_2');
ttq.page();
</script>

<script>
!function (w, d, t) {
  w.TiktokAnalyticsObject=t;var ttq=w[t]=w[t]||[];ttq.methods=["page","track","identify","instances","debug","on","off","once","ready","alias","group","enableCookie","disableCookie"],ttq.setAndDefer=function(t,e){t[e]=function(){t.push([e].concat(Array.prototype.slice.call(arguments,0)))}};for(var i=0;i<ttq.methods.length;i++)ttq.setAndDefer(ttq,ttq.methods[i]);ttq.instance=function(t){for(var e=ttq._i[t]||[],n=0;n<ttq.methods.length;n++)ttq.setAndDefer(e,ttq.methods[n]);return e},ttq.load=function(e,n){var i="https://analytics.tiktok.com/i18n/pixel/events.js";ttq._i=ttq._i||{},ttq._i[e]=[],ttq._i[e]._u=i,ttq._t=ttq._t||{},ttq._t[e]=+new Date,ttq._o=ttq._o||{},ttq._o[e]=n||{};var o=document.createElement("script");o.type="text/javascript",o.async=!0,o.src=i+"?sdkid="+e+"&lib="+t;var a=document.getElementsByTagName("script")[0];a.parentNode.insertBefore(o,a)};
}(window, document, 'ttq');

ttq.load('pixel_id_3');
ttq.page();
</script>
```

**Làm cách nào để thiết lập sự kiện nếu có nhiều pixel trên trang web?**
Có 2 kịch bản thiết lập sự kiện cần xem xét nếu bạn có nhiều pixel:

1. Mỗi pixel báo cáo một sự kiện khác nhau
2. Tất cả pixel cùng báo cáo các sự kiện giống nhau
Tham khảo các đoạn mã mẫu bên dưới để xem cách thiết lập từng kịch bản.

**Kịch bản 1: Mỗi pixel báo cáo các sự kiện khác nhau**

```html
// Javascript
<script>
function () {
/* xxxxx */

ttq.load('pixel_id_1')
ttq.page()
}()
</script>

<script>
function () {
/* xxxxx */ 

ttq.load('pixel_id_2')
ttq.page()
}()
</script>
<script>
function () {
/* xxxxx */

ttq.load('pixel_id_3')
ttq.page()
}()
</script>
ttq.instance('pixel_id_1').track('Purchase')
ttq.instance('pixel_id_2').track('Event 2')
ttq.instance('pixel_id_3').track('Event 3')
```

**Kịch bản 2: Tất cả pixel cùng báo cáo các sự kiện giống nhau**

```html
// Javascript
<script>
function () {
/* xxxxx */

ttq.load('pixel_id_1')
ttq.page()
}()
</script>

<script>
function () {
/* xxxxx */

ttq.load('pixel_id_2')
ttq.page()
}()
</script>

<script>
function () {
/* xxxxx */

ttq.load('pixel_id_3')
ttq.page()
}()
</script>

ttq.track('Purchase') // it will report three Purchase events for pixel_1 and pixel_2 and pixel_3
```

Trong tình huống này, `ttq.track('Purchase')` tương đương với các dòng sau:

```javascript
// Javascript
ttq.instance('pixel_id_1').track('Purchase')
ttq.instance('pixel_id_2').track('Purchase')
ttq.instance('pixel_id_3').track('Purchase')
```

Bởi vì lệnh `ttq.track()` sẽ tự động báo cáo sự kiện cho tất cả các Pixel đã cài đặt.

---

<a id="doc-1799004052020225"></a>
<!-- doc_id: 1799004052020225 -->
<!-- doc_id: 1799004052020225 -->
# Thiết lập đồng thời TikTok Pixel và Events API (Events API and Pixel setup)
> Đường dẫn: Marketing API > Ad Measurement > Guides > Google Tag Manager (GTM) Integration > Events API and Pixel setup
Để cài đặt TikTok Pixel và cấu hình gửi các sự kiện tới TikTok thông qua cả Pixel và Events API, bạn có thể thêm các thẻ TikTok Pixel vào vùng chứa Google Tag Manager (GTM) của mình. Luồng thiết lập tương tác trong Trình quản lý sự kiện TikTok sẽ hướng dẫn bạn cấu hình và cài đặt tất cả các [thẻ, trình kích hoạt và biến TikTok](do-luong-quang-cao-p2.md#doc-1799004081342466) cần thiết chỉ với vài cú nhấp chuột.

Luồng tích hợp GTM và Events API sẽ thiết lập **cả TikTok Pixel và Events API**. Thiết lập kép này được khuyến nghị để tối đa hóa phạm vi bao phủ sự kiện và hiệu suất chiến dịch. Ngoài ra, với việc thiết lập hai kênh, hiệu suất chiến dịch của bạn được bảo vệ khỏi sự gián đoạn sự kiện vì tín hiệu sự kiện vẫn được tiếp nhận từ kênh còn lại nếu một kênh gặp sự cố.

Dưới đây là các hướng dẫn thiết lập cụ thể dựa trên nhu cầu của bạn:
- Chỉ thiết lập TikTok Pixel: xem [Thiết lập chỉ dùng TikTok Pixel](do-luong-quang-cao-p2.md#doc-1799004034003969).
- Chỉ thiết lập Events API: xem Thiết lập chỉ dùng Events API.

## Prerequisites
1. Một [tài khoản Google Analytics](https://analytics.google.com/analytics/web/) và sự quen thuộc với [Google Analytics 4](https://support.google.com/analytics/answer/10089681?hl=en) (GA4).
2. Một vùng chứa web (web container) đã cài đặt trên trang web của bạn và một vùng chứa máy chủ (server container) đã tạo trong tài khoản Google Tag Manager.
  - [Tìm hiểu thêm về thiết lập Google Tag Manager](https://support.google.com/tagmanager/answer/14842164).
  - [Tìm hiểu thêm về thiết lập vùng chứa máy chủ](https://developers.google.com/tag-platform/learn/sst-fundamentals/4-sst-setup-container).
3. Quyền Xuất bản (Publish), Phê duyệt (Approve), Chỉnh sửa (Edit) và Đọc (Read) đối với vùng chứa web và máy chủ. [Tìm hiểu thêm về quyền vùng chứa](https://support.google.com/tagmanager/answer/6107011?hl=en#container_permissions).

4. Tài khoản Google Cloud Platform (GCP) và tài khoản thanh toán GCP để cấp phát máy chủ gắn thẻ của bạn. [Tìm hiểu thêm](https://developers.google.com/tag-platform/tag-manager/server-side/cloud-run-setup-guide?provisioning=automatic#prerequisites).
5. Sự quen thuộc với các khái niệm cơ bản như [thẻ, trình kích hoạt và biến](https://support.google.com/tagmanager/answer/6103657) cùng [gắn thẻ phía máy chủ](https://developers.google.com/tag-platform/tag-manager/server-side/intro).

## Hướng dẫn thiết lập
1. Trong [TikTok Ads Manager](https://ads.tiktok.com/i18n/home), nhấp **Công cụ** > **Sự kiện**, rồi nhấp **Kết nối nguồn dữ liệu** > **Web** > **Tích hợp đối tác** > **Google Tag Manager** > **Gắn thẻ phía máy chủ và phía máy khách**.

Events" width="60%" style="color:#808080" />

- Để tích hợp ID TikTok Pixel hiện có với Google Tag Manager, trong tab **Cài đặt** của pixel trong Trình quản lý sự kiện, nhấp **Chọn đối tác** > **Google Tag Manager** > **Gắn thẻ phía máy chủ và phía máy khách**.

2. Đăng nhập vào tài khoản Google được liên kết với tài khoản GTM của bạn và đảm bảo những điều sau:
  - Tài khoản Google được liên kết với tài khoản GTM của bạn.
  - **Cả vùng chứa Web và vùng chứa Máy chủ** đã được tạo trong tài khoản GTM của bạn.
  

3. Làm theo các hướng dẫn sau để thiết lập máy chủ gắn thẻ và miền tùy chỉnh cho máy chủ của bạn.
  - Để thiết lập một máy chủ gắn thẻ đầy đủ chức năng với **Google Cloud Run** cho mục đích thử nghiệm, hãy chọn **Tự động cấp phát máy chủ gắn thẻ** (khuyến nghị). Lưu ý rằng thao tác này yêu cầu tạo tài khoản thanh toán Google Cloud Platform (GCP). Máy chủ được cấp phát tự động thường không phát sinh chi phí khi chỉ dùng để thử nghiệm. [Tìm hiểu thêm](https://developers.google.com/tag-platform/tag-manager/server-side/cloud-run-setup-guide?provisioning=automatic#provision_a_preview_and_tagging_server).
    - Sau đó bạn có thể [nâng cấp cấu hình](https://developers.google.com/tag-platform/tag-manager/server-side/cloud-run-setup-guide?provisioning=automatic#edit_the_service_configuration) của máy chủ được cấp phát tự động cho mục đích production, hoặc [tạo thủ công một máy chủ gắn thẻ](https://developers.google.com/tag-platform/tag-manager/server-side/manual-setup-guide) bằng các nhà cung cấp đám mây khác (chẳng hạn như Amazon AWS hoặc Microsoft Azure) hoặc trên máy chủ riêng của bạn. [Tìm hiểu thêm về các tùy chọn triển khai máy chủ gắn thẻ](https://developers.google.com/tag-platform/learn/sst-fundamentals/4-sst-setup-container?continue=https%3A%2F%2Fdevelopers.google.com%2Ftag-platform%2Flearn%2Fsst-fundamentals%23article-https%3A%2F%2Fdevelopers.google.com%2Ftag-platform%2Flearn%2Fsst-fundamentals%2F4-sst-setup-container#tagging-server-deployment-options).
  - Để đo lường hoạt động mà không dựa vào cookie của bên thứ ba và đo lường phía máy khách, hãy thiết lập một miền tùy chỉnh. Sau khi hoàn tất tích hợp, bạn có thể định cấu hình miền tùy chỉnh cho máy chủ gắn thẻ của mình. [Tìm hiểu thêm](https://developers.google.com/tag-platform/tag-manager/server-side/custom-domain?option=same-origin).

Khuyến nghị sử dụng **cấp phát tự động** để nhanh chóng thiết lập máy chủ gắn thẻ thử nghiệm và tiếp tục phần còn lại của quy trình. Khi đã xác thực việc tích hợp Events API hoạt động chính xác, sau này bạn có thể cân nhắc chuyển sang các tùy chọn triển khai máy chủ gắn thẻ khác hoặc thêm miền tùy chỉnh cho máy chủ gắn thẻ. Xem Cập nhật URL máy chủ gắn thẻ.

<image src="https://sf16-adcdn-sg.ibytedtos.com/obj/open-api-file-public-i18n/f0c66f73538e6c9966d51efb8a1b638b" alt="Thiết lập máy chủ gắn thẻ" width="60%" style="color:#808080" />

4. Chỉ định tên cho pixel của bạn (nếu đang tạo pixel mới), chọn **Tài khoản** GTM, **Vùng chứa web**, **Vùng chứa máy chủ** và **Không gian làm việc** nơi các thẻ TikTok sẽ được cài đặt.

5. Để thiết lập các thẻ mẫu TikTok, cung cấp các thông tin sau:
  - Mã đo lường (Measurement ID): Mã định danh duy nhất cho luồng dữ liệu web Google Analytics 4 (GA4). Bạn có thể tìm thấy mã này trong [tài khoản Google Analytics](https://analytics.google.com/analytics/web). Để biết thêm chi tiết về cách tìm mã đo lường, xem [Tìm mã đo lường của bạn](https://support.google.com/analytics/answer/12270356?sjid=12416340890415772758-AP).
  - URL máy chủ gắn thẻ: URL của máy chủ gắn thẻ mà bạn đã thiết lập trước đó.

6. Xem xét, xác nhận và xuất bản các thay đổi vào tài khoản GTM của bạn. Nhấp "**Tôi xác nhận chi tiết của từng thẻ đang được xuất bản**". Thao tác này sẽ tự động cài đặt các thẻ, trình kích hoạt và biến cần thiết để TikTok Pixel và Events API hoạt động chính xác với GTM. Để biết thêm chi tiết về những gì sẽ được cài đặt, xem [Thay đổi vùng chứa GTM](do-luong-quang-cao-p2.md#doc-1799004081342466).

> **Note:** 
> • Sau khi các thay đổi được xuất bản, chúng không thể sửa đổi trực tiếp. • Nếu không gian làm việc GTM của bạn đã có thẻ, biến hoặc trình kích hoạt trùng tên với các thay đổi đang được xuất bản, những mục đó sẽ được bỏ qua để giữ nguyên cài đặt GTM sản xuất hiện có. • Nếu bạn muốn sửa đổi phiên bản đã xuất bản hoặc đặt lại thẻ, biến hoặc trình kích hoạt của TikTok, xem Cách dọn dẹp hoặc cài đặt lại để biết hướng dẫn cài đặt lại.

- Chúng tôi sẽ tự động điền ID TikTok Pixel và mã truy cập Events API vào thẻ TikTok Events API đã cài đặt trong vùng chứa máy chủ của bạn. Nếu sau này bạn chuyển sang ID TikTok Pixel khác, hãy đảm bảo làm theo phần Câu hỏi thường gặp để tạo mã mới và cập nhật các giá trị ID TikTok Pixel và Access Token trong thẻ TikTok Events API.

- Nếu gặp lỗi khi xuất bản các thay đổi, bạn có thể khắc phục các nguyên nhân phổ biến theo hướng dẫn về những việc cần làm khi xảy ra sự cố trong bước Xem xét và Xuất bản tài nguyên. Hãy giải quyết sự cố và thử lại quy trình xuất bản.

7. Sau khi các thay đổi được xuất bản, TikTok Pixel sẽ được cài đặt khi trang web tải xong. Hãy làm theo hướng dẫn trong Trình quản lý sự kiện để hoàn tất cấu hình sự kiện. Sau khi hoàn tất thiết lập sự kiện bằng phương thức bạn đã chọn trước đó (bằng lớp dữ liệu GTM hoặc thủ công), TikTok Pixel sẽ bắt đầu báo cáo các sự kiện đó trên trang web của bạn. Ngoài ra, máy chủ gắn thẻ của bạn cũng sẽ báo cáo các sự kiện đó tới TikTok Events API.
  - Để biết hướng dẫn thiết lập sự kiện TikTok bằng lớp dữ liệu GTM, xem [Thiết lập sự kiện bằng lớp dữ liệu](do-luong-quang-cao-tom-tat.md#doc-1799004097478658).
  - Để biết hướng dẫn thiết lập thủ công các sự kiện TikTok mà không dùng lớp dữ liệu GTM, xem [Thiết lập sự kiện thủ công](do-luong-quang-cao-p2.md#doc-1799004110681154).

8. Xác minh tích hợp Events API. Bạn có thể kiểm tra xem các sự kiện có được Events API tiếp nhận thành công hay không bằng cách sử dụng công cụ **Sự kiện thử nghiệm (Test Events)** trong Trình quản lý sự kiện. Ngoài ra, bạn có thể sử dụng chế độ Xem trước (Preview mode) của GTM để xác thực xem các thẻ TikTok có đang được kích hoạt hay không. Để biết thêm hướng dẫn chi tiết, xem [Xác minh thiết lập GTM](do-luong-quang-cao-p2.md#doc-1799004129683458).

## Câu hỏi thường gặp (FAQs)

### Q1: Có lỗi xảy ra trong bước Xem lại và xuất bản tài nguyên. Tôi nên làm gì?

**Đáp**: Nếu bạn gặp sự cố khi xem xét và xuất bản tài nguyên, dưới đây là một số bước khắc phục sự cố bạn có thể thực hiện:

1. Đảm bảo bạn có các quyền vùng chứa cần thiết (Xuất bản, Phê duyệt, Chỉnh sửa và Đọc) để xuất bản các thay đổi.

2. Kiểm tra xem vùng chứa của bạn có lỗi tồn tại từ trước như các biến hoặc trình kích hoạt chưa xác định hay không. Để làm điều này, sử dụng chế độ **Xem trước** (Preview) cho vùng chứa để phát hiện các sự cố trong không gian làm việc.

3. Khắc phục mọi sự cố tìm thấy, sau đó thử lại việc xuất bản các thay đổi từ luồng thiết lập của Trình quản lý sự kiện.

4. Nếu sự cố vẫn tiếp diễn, hãy thử dọn dẹp không gian làm việc của bạn. Để biết hướng dẫn về cách dọn dẹp hoặc cài đặt lại, hãy xem Cách dọn dẹp hoặc cài đặt lại.

### Q2: Làm thế nào để cập nhật URL máy chủ gắn thẻ (tagging server)?

**Đáp**: Nếu URL máy chủ gắn thẻ của bạn đã thay đổi (ví dụ: nếu bạn chuyển từ GCP sang tùy chọn triển khai máy chủ khác hoặc định cấu hình miền tùy chỉnh cho máy chủ gắn thẻ), bạn cần cập nhật thẻ GA4 Config. Thao tác này đảm bảo rằng các sự kiện được định tuyến chính xác đến URL mới. Dưới đây là cách cập nhật URL máy chủ gắn thẻ:
- Xác định vị trí thẻ TikTok GA4 Config bên trong vùng chứa web.
- Cập nhật giá trị của `server_container_url` thành URL máy chủ gắn thẻ đã cập nhật và lưu thay đổi.

### Q3: Tôi có thể tái sử dụng thiết lập máy chủ gắn thẻ hiện có để tích hợp Events API không?

**Đáp**: Có, bạn có thể tái sử dụng máy chủ gắn thẻ hiện có để tích hợp với Events API. Nếu vùng chứa Web GTM của bạn đã có một Google Tag với `server_container_url` trỏ đến máy chủ gắn thẻ, bạn có thể tiếp tục sử dụng thẻ đó. Chỉ cần xóa Google Tag được đánh dấu đã cài đặt bởi luồng thiết lập tương tác, có tên là `TT-{PixelID}-XXXXX-Web-Tag-GA4_Config`.

Tuy nhiên, hãy đảm bảo giữ lại thẻ TikTok GA4 Event có tên là `TT-{PixelID}-XXXXX-Web-Tag-GA4_Event`, cùng tất cả các biến đã cài đặt khác, vì chúng cần thiết để định dạng chính xác sự kiện cho thẻ TikTok Events API trong vùng chứa máy chủ phân tích cú pháp.

### Q4: Làm thế nào để dọn dẹp hoặc cài đặt lại?
**Đáp**: Trong một số trường hợp, bạn có thể cần xóa phần tích hợp hiện có và thực hiện cài đặt lại. Bao gồm các tình huống sau:
- Nâng cấp từ chỉ tích hợp TikTok Pixel sang tích hợp cả TikTok Pixel & Events API.
- Thực hiện "đặt lại về trạng thái ban đầu" vì các lý do khác, chẳng hạn như khắc phục lỗi thiết lập.

Để dọn dẹp và cài đặt lại trong những trường hợp này, hãy làm theo các bước sau:
1. Tạo một không gian làm việc sao lưu trong cùng một vùng chứa để lưu các cấu hình hiện có.
2. Trong không gian làm việc mặc định của bạn, hãy xóa các thẻ, biến và trình kích hoạt TikTok đã cài đặt trước đó. Xem [Thay đổi vùng chứa GTM](do-luong-quang-cao-p2.md#doc-1799004081342466).
3. Sau khi dọn dẹp, thực hiện lại luồng thiết lập tương tác để cài đặt lại tích hợp.
4. Đảm bảo sao chép lại bất kỳ tùy chỉnh quan trọng nào từ không gian làm việc sao lưu sang không gian làm việc mặc định.

### Q5: Làm thế nào để chỉ thiết lập tích hợp Events API đơn lẻ?
**Đáp**: Theo mặc định, luồng thiết lập tương tác này trong Trình quản lý sự kiện sẽ tích hợp cả Pixel và Events API với GTM. Tuy nhiên, nếu bạn chỉ muốn sử dụng Events API mà không dùng Pixel, bạn có thể gỡ cài đặt thiết lập Pixel theo cách thủ công. Lưu ý rằng thiết lập khuyến nghị là sử dụng cả Pixel và Events API để tối đa hóa phạm vi bao phủ sự kiện và hiệu suất chiến dịch.

Để chỉ thiết lập tích hợp Events API, hãy xóa các thẻ "TikTok Pixel" và "Custom HTML" khỏi vùng chứa Web dùng để tích hợp.

### Q6: Làm thế nào để tôi chọn đúng API phù hợp để sử dụng?
**Đáp**: Google Tag và Tag Manager là các khung đo lường khác nhau do Google cung cấp, cung cấp các chức năng và API tương tự có thể vận hành [lớp dữ liệu](https://support.google.com/tagmanager/answer/6164391?hl=en&ref_topic=3441647&sjid=9251457294155490283-NA) để truyền thông tin từ trang web của bạn tới vùng chứa Tag Manager.

Đối với Google Tag, API là [gtag()](https://developers.google.com/tag-platform/gtagjs/reference). Đối với Tag Manager, API là [dataLayer.push()](https://developers.google.com/tag-platform/tag-manager/datalayer). Tích hợp Events API hỗ trợ cả hai API nhưng bộ thẻ và biến được cài đặt bởi luồng tương tác của Trình quản lý sự kiện hơi khác nhau để đáp ứng hành vi cụ thể của từng API.
- Nếu trang web của bạn đã sử dụng một trong các khung (ví dụ: để đo lường trang web bằng Google Analytics), bạn cần tiếp tục sử dụng cùng một khung và API tương ứng để thiết lập các sự kiện cho TikTok. Xem [Thiết lập sự kiện bằng lớp dữ liệu](do-luong-quang-cao-tom-tat.md#doc-1799004097478658).
- Nếu trang web của bạn chưa sử dụng các API này nhưng bạn muốn triển khai một API cho việc tích hợp Events API, hãy tham khảo [Bài viết trợ giúp của Google](https://support.google.com/tagmanager/answer/7582054?hl=en) để chọn API phù hợp nhất với nhu cầu kinh doanh của bạn.

### Q7: Tôi có vẫn cần thiết lập `event_id` để khử trùng lặp giữa Events API và Pixel không?
**Đáp**: Không. Nếu bạn sử dụng luồng tương tác trong Trình quản lý sự kiện để thiết lập tích hợp Events API và Pixel, biến `event_id` sẽ được tự động cấu hình cho bạn. Bạn không cần cấu hình thêm bất cứ điều gì để tính năng khử trùng lặp hoạt động. [Tìm hiểu thêm về khử trùng lặp sự kiện](https://ads.tiktok.com/help/article/event-deduplication).

### Q8: Tôi đã cài đặt mẫu thẻ TikTok Events API (Official) thủ công từ thư viện GTM thay vì dùng luồng tương tác. Tôi có thể tiếp tục dùng nó không?
**Đáp**: Có, bạn có thể. Nếu bạn đã cài đặt thủ công thẻ mẫu từ thư viện mẫu GTM, bạn có thể tiếp tục sử dụng mà không gặp vấn đề gì và giữ lại mọi tùy chỉnh hiện có mà bạn đã thực hiện cho mẫu. Tuy nhiên, khuyến nghị bạn nâng cấp cài đặt bằng cách thực hiện luồng tương tác của Trình quản lý sự kiện. Điều này sẽ giúp các sửa đổi trong tương lai dễ dàng hơn nhiều. Để biết thêm thông tin, xem Cách dọn dẹp hoặc cài đặt lại.

### Q9: Làm thế nào để tạo mã truy cập mới cho Events API nếu tôi chuyển sang một Pixel khác?
**Đáp**: Luồng thiết lập tương tác sẽ tự động tạo một mã truy cập Events API hợp lệ và đặt mã đó vào thẻ TikTok Events API. Tuy nhiên, nếu bạn muốn chuyển sang một mã khác (ví dụ: nếu bạn đổi sang một ID TikTok Pixel khác sau này), hãy làm theo tài liệu nhà phát triển Events API về [Xác thực](do-luong-quang-cao-p1.md#doc-1771101130925058) để tạo mã mới cho ID TikTok Pixel đó.

## Hỗ trợ
- Nếu bạn có bất kỳ câu hỏi nào, vui lòng liên hệ [Bộ phận hỗ trợ khách hàng TikTok Ads](https://ads.tiktok.com/help/article/contact-tiktok-business-support) hoặc liên hệ với Đại diện bán hàng TikTok của bạn.
- Nếu bạn có bất kỳ yêu cầu tính năng nào hoặc gặp sự cố, hãy gửi vấn đề trên GitHub [tại đây](https://github.com/tiktok/gtm-template-eapi).

---

<a id="doc-1799004097478658"></a>
<!-- doc_id: 1799004097478658 -->
<!-- doc_id: 1799004097478658 -->
# Thiết lập sự kiện với Data Layer trong GTM (Set up events with data layer)
> Đường dẫn: Marketing API > Ad Measurement > Guides > Google Tag Manager (GTM) Integration > Set up events with data layer
Lớp dữ liệu (data layer) là một đối tượng được Google Tag Manager (GTM) và `gtag.js` sử dụng để truyền thông tin đến các thẻ. Mã trang web của bạn có thể tương tác với lớp dữ liệu để lưu trữ hoặc gửi dữ liệu bằng các API JavaScript của Google Tag hoặc Tag Manager, cụ thể là `gtag()` hoặc `dataLayer.push()`.

Chúng tôi đã phát triển hai mẫu: [Mẫu TikTok Pixel](https://tagmanager.google.com/gallery/#/owners/tiktok/templates/gtm-template-pixel) và [Mẫu TikTok Events API](https://tagmanager.google.com/gallery/#/owners/tiktok/templates/gtm-template-eapi), để phân tích cú pháp các sự kiện trong lớp dữ liệu và gửi các sự kiện đó đến TikTok bằng Pixel và Events API.

> **Note:** 
> Nếu bạn dự định sử dụng lớp dữ liệu để truyền thông tin đến các thẻ, bạn rất nên sử dụng luồng tương tác trong Trình quản lý sự kiện của TikTok để thiết lập tích hợp Pixel hoặc Events API với GTM. Luồng này tự động cài đặt các mẫu và tất cả các thẻ, biến cũng như trình kích hoạt cần thiết để xử lý và gửi các sự kiện lớp dữ liệu đến TikTok. Để biết thêm thông tin, hãy xem: • [Chỉ thiết lập TikTok Pixel](do-luong-quang-cao-p2.md#doc-1799004034003969) • [Thiết lập Events API và Pixel](do-luong-quang-cao-tom-tat.md#doc-1799004052020225)

Các sự kiện và tham số được các mẫu của TikTok nhận diện phù hợp với các khuyến nghị do Google cung cấp. Để biết thêm thông tin về các loại sự kiện và tham số được khuyến nghị, xem [Sự kiện được khuyến nghị](https://developers.google.com/analytics/devguides/collection/ga4/reference/events?client_type=gtm) và [Dữ liệu sự kiện chung](https://developers.google.com/tag-platform/tag-manager/server-side/common-event-data).

> **Note:** 
> Nếu bạn đã thiết lập các sự kiện theo hướng dẫn của Google, tức là [Sự kiện được khuyến nghị](https://developers.google.com/analytics/devguides/collection/ga4/reference/events?client_type=gtm) và [Dữ liệu sự kiện chung](https://developers.google.com/tag-platform/tag-manager/server-side/common-event-data), để đo lường trang web của bạn bằng Google Analytics 4 (GA4), các mẫu của TikTok sẽ tự động phát hiện và chuyển đổi các sự kiện hoặc tham số tương tự đó thành các sự kiện hoặc tham số tiêu chuẩn của TikTok.

Tài liệu này bao gồm các nội dung sau:
- Điều kiện tiên quyết để thiết lập sự kiện qua Data Layer
- Ví dụ về sự kiện mua hàng (Purchase)
- Tổng quan về lược đồ sự kiện Data Layer, bao gồm các loại sự kiện và tham số đề xuất

## Prerequisites
- Bạn cần có quyền chỉnh sửa mã nguồn của trang web.
- Trước khi tiến hành thiết lập sự kiện TikTok, chúng tôi khuyên bạn nên làm quen với các hướng dẫn dành cho nhà phát triển của Google sau đây:
  - [Lớp dữ liệu (data layer) GTM](https://developers.google.com/tag-platform/tag-manager/datalayer)
  - [Thiết lập biến lớp dữ liệu](https://support.google.com/tagmanager/answer/6164391?hl=en)
  - [Đo lường thương mại điện tử](https://developers.google.com/analytics/devguides/collection/ga4/ecommerce?client_type=gtm) và [Sự kiện được khuyến nghị](https://developers.google.com/analytics/devguides/collection/ga4/reference/events?client_type=gtm)
  
## Ví dụ sự kiện mua hàng `Purchase` đơn giản
Hãy xem qua một ví dụ để hiểu cách hoạt động. Giả sử bạn muốn gửi sự kiện `Purchase` đến TikTok. Khi người dùng thực hiện giao dịch mua trên trang web của bạn, mã JavaScript của trang web sẽ kích hoạt sự kiện `purchase` bằng lớp dữ liệu Google Tag Manager. Các mẫu TikTok sau đó sẽ phân tích cú pháp sự kiện này và gửi dưới dạng sự kiện `Purchase` tới TikTok.

```javascript
// Javascript
// Google Tag example
gtag('event', 'purchase', {
  transaction_id: 'T_12345',
  value: 200.0,
  currency: 'USD',
  user_data: {
    sha256_email_address: '0c7e6a405862e402eb76a70f8a26fc732d07c32931e9fae9ab1582911d2e8a3b',
    sha256_phone_number: '123456405862e402eb76a70f8a26fc732d07c32931e9fae9ab1582911d2e8a3b',
    address: {
      sha256_first_name: '4f23798d92708359b734a18172c9c864f1d48044a754115a0d4b843bca3a5332',
      sha256_last_name: 'fd53ef835b15485572a6e82cf470dcb41fd218ae5751ab7531c956a2a6bcd3c7',
      city: 'City Town',
      region: 'CA',
      postal_code: '54321',
      country: 'US'
    }
  },
  items: [
    {
      item_id: 'SKU_12345',
      item_name: 'Fancy-MaxSpeed2.0 Black',
      item_brand: 'Fancy Sneakers',
      item_category: 'Shoes - Running Shoes',
      price: 100.0,
      quantity: 2
    }
  ],
  tt_external_id: 'b9c5fdaea74ee1c31705b764389895371b8d416c5cae8740e7f89082a9fcdc0a',
  tt_content_type: 'product'
});
```

```javascript
// Javascript
// Tag Manager example
dataLayer.push({ ecommerce: null });
dataLayer.push({
  event: 'purchase',
  user_data: {
    sha256_email_address: '0c7e6a405862e402eb76a70f8a26fc732d07c32931e9fae9ab1582911d2e8a3b',
    sha256_phone_number: '123456405862e402eb76a70f8a26fc732d07c32931e9fae9ab1582911d2e8a3b',
    address: {
      sha256_first_name: '4f23798d92708359b734a18172c9c864f1d48044a754115a0d4b843bca3a5332',
      sha256_last_name: 'fd53ef835b15485572a6e82cf470dcb41fd218ae5751ab7531c956a2a6bcd3c7',
      city: 'City Town',
      region: 'CA',
      postal_code: '54321',
      country: 'US'
    }
  },
  ecommerce: {
    transaction_id: 'T_12345',
    value: 200.0,
    currency: 'USD',
    items: [
      {
        item_id: 'SKU_12345',
        item_name: 'Fancy-MaxSpeed2.0 Black',
        item_brand: 'Fancy Sneakers',
        item_category: 'Shoes - Running Shoes',
        price: 100.0,
        quantity: 2
      }
    ]
  },
  tt_external_id: 'b9c5fdaea74ee1c31705b764389895371b8d416c5cae8740e7f89082a9fcdc0a',
  tt_content_type: 'product'
});
```

Lấy tích hợp Events API làm ví dụ, dưới đây là tải trọng sự kiện mẫu được gửi đến TikTok Events API. Để biết thêm chi tiết về các tham số cụ thể, xem [Tham số Events API](do-luong-quang-cao-tom-tat.md#doc-1771101151059969).

```javascript
// Javascript
{
  "event_source": "web",
  "event_source_id": "{{PIXEL-CODE}}",
  "data": [
    {
      "event": "Purchase",
      "event_time": 1714176177,
      "user": {
        "phone": "0c7e6a405862e402eb76a70f8a26fc732d07c32931e9fae9ab1582911d2e8a3b",
        "email": "123456405862e402eb76a70f8a26fc732d07c32931e9fae9ab1582911d2e8a3b",
        "external_id": "b9c5fdaea74ee1c31705b764389895371b8d416c5cae8740e7f89082a9fcdc0a",
        "first_name": "4f23798d92708359b734a18172c9c864f1d48044a754115a0d4b843bca3a5332",
        "last_name": "fd53ef835b15485572a6e82cf470dcb41fd218ae5751ab7531c956a2a6bcd3c7",
        "city": "citytown",
        "state": "ca",
        "country": "us",
        "zip_code": "20f3765880a5c269b747e1e906054a4b4a3a991259f1e16b5dde4742cec2319a"
      },
      "properties": {
        "currency": "USD",
        "value": 200.0,
        "content_type": "product",
        "contents": [
          {
            "price": 100.0,
            "quantity": 2,
            "content_id": "12345",
            "content_name": "Fancy-MaxSpeed2.0 Black",
            "content_category": "Shoes - Running Shoes",
            "brand": "Fancy Sneakers"
          }
        ]
      }
    }
  ]
}
```

## Ánh xạ tên sự kiện (Event name mapping)
Khi thiết lập sự kiện TikTok bằng lớp dữ liệu GTM, bạn cần gửi trực tiếp các tên sự kiện được Google Analytics khuyến nghị. Các mẫu TikTok Pixel và Events API sẽ tự động ánh xạ chúng sang các tên sự kiện tiêu chuẩn tương ứng của TikTok.

Nếu tên sự kiện Google Analytics không có trong ánh xạ, tên đó sẽ được xử lý như một sự kiện tùy chỉnh của TikTok. Tìm hiểu thêm về [Sự kiện được TikTok hỗ trợ](do-luong-quang-cao-p1.md#doc-1771101186666498) và [Sự kiện GA4 được khuyến nghị](https://developers.google.com/analytics/devguides/collection/ga4/reference/events?client_type=gtag).

| TikTok Standard Event Name | Google Analytics Event Name |
|---|---|
| `AddPaymentInfo` | `add_payment_info` |
| `AddToCart` | `add_to_cart` |
| `AddToWishlist` | `add_to_wishlist` |
| `Purchase` | `purchase` |
| `CompleteRegistration` | `sign_up` |
| `InitiateCheckout` | `begin_checkout` |
| `Pageview` | `page_view` |
| `Search` | `search` |
| `ViewContent` | `view_item` |

Đối với các tên sự kiện tiêu chuẩn sau đây của TikTok không có tên sự kiện khuyến nghị tương ứng của GA4, bạn chỉ cần gửi tên sự kiện TikTok khi thiết lập sự kiện.
- `Contact`
- `Download`
- `Lead`
- `Subscribe`

Để cho phép các mẫu TikTok Pixel và Events API tự động chuyển đổi tên sự kiện GA4 được khuyến nghị, bạn cần sử dụng biến tích hợp sẵn của GTM `{{Event}}` làm **Event Name** trong thẻ TikTok Pixel và biến tích hợp sẵn `{{Event Name}}` làm **Event Name** trong thẻ TikTok Events API.

## Tham số sự kiện trang web 
Khi định cấu hình tham số sự kiện bằng lớp dữ liệu GTM, bạn cần tuân theo [Sự kiện được khuyến nghị của GA4](https://developers.google.com/analytics/devguides/collection/ga4/reference/events?client_type=gtag) và [Dữ liệu sự kiện chung của GTM](https://developers.google.com/tag-platform/tag-manager/server-side/common-event-data). Mẫu TikTok Pixel và mẫu Events API sẽ tự động ánh xạ các tham số GTM và GA4 sang các tham số TikTok tương ứng. Tìm hiểu thêm về [Tham số Pixel](do-luong-quang-cao-tom-tat.md#doc-1739585702922241) và [Tham số Events API](do-luong-quang-cao-tom-tat.md#doc-1771101151059969) của TikTok.

### Dữ liệu sản phẩm (Product data)
Thông tin sản phẩm là tối quan trọng nếu bạn đang quảng cáo một sản phẩm bán trên trang web. Việc gửi thông tin sản phẩm đầy đủ giúp kích hoạt khả năng đo lường và tối ưu hóa thông qua các giải pháp như Quảng cáo mua sắm dạng video TikTok (VSA) cho thương mại điện tử, Tối ưu hóa dựa trên giá trị (VBO), hoặc đo lường ROAS.

Để biết thêm thông tin về các tham số Google Analytics được khuyến nghị đưa vào, hãy xem [Sự kiện được khuyến nghị của GA4](https://developers.google.com/analytics/devguides/collection/ga4/reference/events?client_type=gtag).

TikTok parameters
Các tham số Google Analytics
Bắt buộc để báo cáo ROAS hoặc VBO
Bắt buộc cho Video Shopping Ads (VSA)

API Google tag - `gtag()`
API Tag Manager - `dataLayer.push()`

value
value
ecommerce.value
✅

currency
currency
ecommerce.currency
✅

content_type
tt_content_type
tt_content_type

✅

contents
items
ecommerce.items

contents[].price
items[].price
ecommerce.items[].price

contents[].content_id
items[].item_id
ecommerce.items[].item_id

✅

contents[].content_category
items[].item_category
ecommerce.items[].item_category

contents[].content_name
items[].item_name
ecommerce.items[].item_name

contents[].quantity
items[].quantity
ecommerce.items[].quantity

contents[].brand
items[].brand
ecommerce.items[].brand

### Dữ liệu người dùng (User data)
Để tận dụng [So khớp nâng cao](do-luong-quang-cao-p2.md#doc-1739585700402178) — tính năng giúp tối ưu hóa quảng cáo TikTok và thúc đẩy hiệu suất bằng cách khớp thông tin khách hàng với người dùng trên TikTok — bạn có thể gửi thông tin người dùng sau đây.

Để biết thêm thông tin về các tham số lớp dữ liệu GTM, xem [Dữ liệu sự kiện chung của GTM](https://developers.google.com/tag-platform/tag-manager/server-side/common-event-data).

| TikTok Events parameters | GTM data layer parameters  |
|---|---|
| `email` |<ul><li>`user_data.email_address` <ul><li>The value will be SHA256 hashed before being sent to TikTok.</li></ul></li><li>`user_data.sha256_email_address`</li></ul> |
| <ul><li>`phone_number` (for Pixel)</li><li>`phone` (for Events API)</li></ul>  |  <ul><li>`user_data.phone_number` <ul><li>The value will be SHA256 hashed before being sent to TikTok.</li></ul></li><li>`user_data.sha256_phone_number`</li></ul>|
| `external_id`| `tt_external_id`<ul><li>The value will be SHA256 hashed before being sent to TikTok.</li><li>See [Set up External ID](do-luong-quang-cao-p1.md#doc-1771100952291330) for more details.</li></ul> |
| `first_name` | <ul><li> `user_data.address.first_name` <ul><li>The value will be SHA256 hashed before being sent to TikTok.</li></ul>  </li><li> `user_data.address.sha256_first_name`</li></ul>|
| `last_name` | <ul><li> `user_data.address.last_name`  <ul><li>The value will be SHA256 hashed before being sent to TikTok.</li></ul></li><li> `user_data.address.sha256_last_name`</li></ul>|
| `city` | `user_data.address.city`<br><br> The city for the address of the user. |
|`state` | `user_data.address.region` <br><br>The state or territory for the address of the user. |
| `country`| `user_data.address.country` <br><br>The country or region code for the address of the user. |
| `zip_code` |  <ul><li> `user_data.address.postal_code`<ul><li>The value will be SHA256 hashed before being sent to TikTok.</li><li>For US zip codes, only the first five digits will be sent (hashed) to TikTok.</li></ul> |

## Gửi sự kiện Data Layer tới thẻ máy chủ (Server tags)
  
> **Note:** 
> Nếu bạn sử dụng luồng tương tác của Trình quản lý sự kiện (**khuyến nghị**) để thiết lập tích hợp Events API, bạn có thể bỏ qua các bước thiết lập sau. Điều này là do luồng tương tác sẽ tự động cài đặt [Mẫu TikTok Events API](https://tagmanager.google.com/gallery/#/owners/tiktok/templates/gtm-template-eapi) cùng tất cả các thẻ, biến và trình kích hoạt bổ sung cần thiết để gửi sự kiện đến vùng chứa máy chủ của bạn.

  Đối với tích hợp Events API, điều cốt yếu là chuyển tiếp các sự kiện trong lớp dữ liệu của bạn (kích hoạt bằng API `gtag()` hoặc `dataLayer.push()`) đến vùng chứa máy chủ nơi thẻ [Mẫu TikTok Events API](https://tagmanager.google.com/gallery/#/owners/tiktok/templates/gtm-template-eapi) được cài đặt. Để đạt được điều này, bạn cần thiết lập một Google Tag, một thẻ Google Analytics GA4 Event và một số biến bổ sung.
  
### Thiết lập thẻ Google Tag
Trong **Vùng chứa web** của bạn, thêm một **Google Tag**. Nếu bạn đã thiết lập Gắn thẻ phía máy chủ và có sẵn Google Tag với `server_container_url` đã cấu hình, bạn có thể tái sử dụng Google Tag đó.

  
Trong Google Tag của bạn, đặt `server_container_url` trỏ đến máy chủ gắn thẻ và đặt trình kích hoạt thực thi trên **Tất cả các trang** (All Pages). [Tìm hiểu thêm](https://developers.google.com/tag-platform/tag-manager/server-side/send-data?option=GTM).
  

  
### Thiết lập thẻ sự kiện GA4
Trong **Vùng chứa Web**, thêm một thẻ **Google Analytics: GA4 Event**.
  

  
Trong thẻ **Google Analytics: GA4 Event**, đặt biến tích hợp sẵn `{{Event}}` làm **Event Name**.
  

  
Sau đó bạn cần cấu hình Tham số sự kiện GA4 (GA4 Event Parameters).

#### Các tham số sự kiện GA4
- Nếu trang web của bạn triển khai lược đồ sự kiện lớp dữ liệu GA4 được khuyến nghị (xem hướng dẫn trong Tham số sự kiện trang web), hãy định cấu hình ánh xạ sau trong thẻ **Google Analytics: GA4 Event** dựa trên API chính xác mà bạn đã tích hợp (`gtag()` hoặc `dataLayer.push()`). Các **tham số sự kiện GA4** chỉ định các tham số dữ liệu và giá trị tương ứng sẽ được chuyển tiếp từ Vùng chứa web đến Vùng chứa máy chủ trên máy chủ gắn thẻ của bạn.
- Nếu trang web của bạn triển khai các lược đồ tùy chỉnh, bạn cần sử dụng mục **Ghi đè tham số** (Parameter Override) trong các mẫu TikTok để [cấu hình thủ công các tham số sự kiện TikTok](do-luong-quang-cao-p2.md#doc-1799004110681154).

| GA4 Event Parameter | Note | Value for gtag() API | Value for dataLayer.push() API |
|---|---|---|---|
| `first_party_collection` | If you want to send `user_data` to TikTok through Events API, set `first_party_collection` to `true`. | `true` | `true` |
| `user_data` |  | Variable Type: Data Layer Variable ⏎ Variable Name: `eventModel.user_data` | Variable Type: Data Layer Variable ⏎ Variable Name: `user_data` |
| `tt_external_id` |  | Variable Type: Data Layer Variable ⏎ Variable Name: `eventModel.tt_external_id` | Variable Type: Data Layer Variable ⏎ Variable Name: `tt_external_id` |
| `value` |  | Variable Type: Data Layer Variable ⏎ Variable Name: `eventModel.value` | Variable Type: Data Layer Variable ⏎ Variable Name: `ecommerce.value` |
| `currency` |  | Variable Type: Data Layer Variable ⏎ Variable Name: `eventModel.currency` | Variable Type: Data Layer Variable ⏎ Variable Name: `ecommerce.currency` |
| `tt_content_type` |  | Variable Type: Data Layer Variable ⏎ Variable Name: `eventModel.tt_content_type` | Variable Type: Data Layer Variable ⏎ Variable Name: `tt_content_type` |
| `tt_contents` | If you want to send the item data of an event that is not a GA4 recommended event or an event that does not support the `items` parameter, specify `tt_contents`. [Learn more about GA4 recommended events specification](https://developers.google.com/analytics/devguides/collection/ga4/reference/events?client_type=gtag). | Variable Type: Custom Javascript ⏎ `function() { ⏎ var tt_contents = window.google_tag_manager[{{Container ID}}].dataLayer.get('eventModel.items'); ⏎ return JSON.stringify(tt_contents); ⏎ } ` ⏎ JSON.stringify `tt_contents` as it is a TikTok defined GA4 JSON parameter. | Variable Type: Custom Javascript ⏎ `function() { ⏎ var tt_contents = window.google_tag_manager[{{Container ID}}].dataLayer.get('ecommerce.items'); ⏎ return JSON.stringify(tt_contents); ⏎ } ` ⏎ JSON.stringify `tt_contents` as it is a TikTok defined GA4 JSON parameter. |
| `event_id` |  | Variable Type: Custom JavaScript ⏎ See How to set up deduplication. | Variable Type: Custom JavaScript ⏎ See How to set up deduplication. |

Bạn cần chọn **Send Ecommerce data** với **Data Layer** làm **Data source**.

  
Cuối cùng, gán một trình kích hoạt cho thẻ GA4 Event của bạn. Trong hầu hết các trường hợp, bạn có thể đặt trình kích hoạt chạy trên Tất cả các sự kiện tùy chỉnh (All Custom Events), với biểu thức chính quy `.+` làm quy tắc so khớp tên sự kiện.
  

  
### Cấu hình mẫu 
Dưới đây là cấu hình thẻ Google Analytics: GA4 Event mẫu sau khi hoàn thành các thiết lập trước đó:

  
### Cách thiết lập khử trùng lặp (Deduplication)
  
> **Note:** 
> Nếu bạn sử dụng luồng tương tác khuyến nghị trong Trình quản lý sự kiện để thiết lập cả tích hợp Pixel và Events API, tính năng khử trùng lặp Event ID sẽ tự động được định cấu hình cho bạn.

Để thiết lập tính năng khử trùng lặp, bạn có thể định cấu hình một biến `Custom Javascript` trong GTM làm `event_id`. Biến này giúp khử trùng lặp giữa các sự kiện TikTok Pixel và Events API. [Tìm hiểu thêm về khử trùng lặp sự kiện](https://ads.tiktok.com/help/article/event-deduplication).
  
Một ví dụ về việc tạo `event_id` cho cùng một sự kiện là sử dụng các giá trị mặc định của lớp dữ liệu GTM, đó là thời gian tải thẻ (`start`) và ID trình tự sự kiện duy nhất (`uniqueEventId`).
  

  
Để thiết lập tính năng khử trùng lặp Event ID, hãy làm theo các bước sau:
- Trong Thẻ **TikTok Pixel** của vùng chứa Web, hãy đặt biến thành tham số `Event ID` (**Ghi đè tham số** > **Cấu hình khử trùng lặp** > **Event ID**).
- Trong Thẻ **Google Analytics: GA4 Event** của vùng chứa Web, đặt cùng biến đó cho tham số sự kiện `event_id`.

## Xác minh thiết lập sự kiện
Sau khi bạn đã cấu hình các sự kiện và tham số TikTok trong các mẫu Pixel hoặc Events API, bạn có thể xác minh thiết lập bằng cách làm theo [Xác minh thiết lập GTM](do-luong-quang-cao-p2.md#doc-1799004129683458).

## Hỗ trợ
Nếu bạn gặp sự cố cần hỗ trợ kỹ thuật, hãy gửi báo cáo vấn đề trong các dự án GitHub tương ứng:
- [Kho GitHub mẫu TikTok Pixel](https://github.com/tiktok/gtm-template-pixel/issues)
- [Kho GitHub mẫu TikTok Events API](https://github.com/tiktok/gtm-template-eapi/issues)
---

## Hướng dẫn thực hành Data Retrieval (Python & cURL)

Dưới đây là mã nguồn mẫu minh họa quy trình gọi API thực tế cho phân hệ **Hướng dẫn đo lường quảng cáo (Ad Measurement) (tóm tắt các tài liệu dài)**:

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

