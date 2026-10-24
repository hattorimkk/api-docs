# Sự kiện 2.0 (Events 2.0)
<a id="doc-1771101276978178"></a>
<!-- doc_id: 1771101276978178 -->

> [!IMPORTANT]
> Khi sử dụng các endpoint của Events API, bạn đồng ý tuân thủ [Điều khoản Dữ liệu Sản phẩm Doanh nghiệp của TikTok (TikTok Business Products (Data) Terms)](https://ads.tiktok.com/i18n/official/policy/business-products-terms) và cam kết không chia sẻ dữ liệu nhạy cảm với TikTok.

Events API 2.0 hiện là endpoint chuẩn được khuyến nghị để báo cáo các sự kiện chuyển đổi từ tất cả các nguồn dữ liệu, bao gồm web, ứng dụng (app), cửa hàng ngoại tuyến (offline) và hệ thống quản lý quan hệ khách hàng (CRM). API này cung cấp một cấu trúc lược đồ (schema) hợp nhất, giúp các nhà quảng cáo tinh gọn và đơn giản hóa quá trình tích hợp.

Nhóm API này bao gồm endpoint sau:
- [Báo cáo sự kiện App, Web, Offline hoặc CRM](42-events-2-0.md#doc-1771101303285761)

---

## Báo cáo sự kiện App, Web, Offline hoặc CRM (`Report App, Web, Offline, or CRM Events`)
<a id="doc-1771101303285761"></a>
<!-- doc_id: 1771101303285761 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/event/track/`

**Mục đích**: Sử dụng endpoint này để gửi một sự kiện đơn lẻ hoặc gửi hàng loạt (batch) nhiều sự kiện chuyển đổi từ ứng dụng (App), trang web (Web), cửa hàng thực tế (Offline) hoặc hệ thống CRM.

> [!TIP]
> - Để tối ưu hóa hiệu suất chiến dịch quảng cáo và thuật toán phân phối, **rất khuyến nghị gửi sự kiện theo thời gian thực (real-time, không gom batch)** ngay khi sự kiện được ghi nhận trên máy chủ của nhà quảng cáo.
> - Nếu gửi hàng loạt (batching), **bạn có thể báo cáo tối đa 1.000 sự kiện trong một yêu cầu**. Nếu vượt quá 1.000 sự kiện, toàn bộ yêu cầu sẽ bị từ chối.
> - Tính năng báo cáo sự kiện ứng dụng (App Events) qua Events API 2.0 hiện yêu cầu danh sách cho phép (allowlist). Hãy liên hệ với đại diện TikTok nếu bạn cần quyền truy cập.

### Header

| Field | Data Type | Bắt buộc | Description |
|---|---|---|---|
| Access-Token | string | Bắt buộc | Access token đã được cấp quyền. Xem thêm [Events API 2.0 - Xác thực](../09-marketing-api/do-luong-quang-cao-p1.md#doc-1771101130925058). |
| Content-Type | string | Bắt buộc | Định dạng bản tin yêu cầu: `application/json`. |

### Tham số Body (Parameters)

| Field | Data Type | Bắt buộc | Description |
|---|---|---|---|
| event_source | string | Bắt buộc | Loại nguồn sự kiện tải lên qua Events API. Các giá trị enum:<br>• `web`: Sự kiện diễn ra trên website của bạn và được đo lường bằng Pixel Code.<br>• `app`: Sự kiện diễn ra trên ứng dụng di động và được đo lường bằng TikTok App ID.<br>• `offline`: Sự kiện chuyển đổi diễn ra tại cửa hàng thực tế và được đo lường bằng Offline Event Set ID.<br>• `crm`: Sự kiện khách hàng tiềm năng diễn ra trong hệ thống CRM và được đo lường bằng CRM Event Set ID. |
| event_source_id | string | Bắt buộc | ID định danh nguồn sự kiện dùng để đo lường:<br>• Khi `event_source = web`: Điền Pixel Code (xem [FAQ - Tìm Pixel Code ở đâu](../09-marketing-api/do-luong-quang-cao-p1.md#doc-1771101001228290)).<br>• Khi `event_source = offline`: Điền Offline Event Set ID (xem [Hướng dẫn cài đặt Offline](../09-marketing-api/do-luong-quang-cao-tom-tat.md#doc-1771101027431425)).<br>• Khi `event_source = app`: Điền TikTok App ID (xem [Hướng dẫn cài đặt App](../09-marketing-api/do-luong-quang-cao-tom-tat.md#doc-1771101111730178)).<br>• Khi `event_source = crm`: Điền CRM Event Set ID (dùng [/crm/list/](43-events-1-0-p2.md#doc-1780896521680898)). |
| data | object[] | Bắt buộc | Mảng các đối tượng sự kiện cần báo cáo (tối đa 1.000 sự kiện/yêu cầu). |
| ↳ event | string | Bắt buộc | **Áp dụng cho web, app, offline, CRM.**<br>Tên sự kiện chuyển đổi:<br>• Với sự kiện web và app: Có thể là Sự kiện tiêu chuẩn (Standard Event) hoặc Sự kiện tùy chỉnh (Custom Event).<br>• Với sự kiện offline: Chỉ hỗ trợ Sự kiện tiêu chuẩn.<br>• Với sự kiện CRM: Chỉ hỗ trợ Sự kiện tùy chỉnh.<br>Xem danh sách sự kiện tiêu chuẩn được hỗ trợ tại [Events API 2.0 - Sự kiện hỗ trợ](../09-marketing-api/do-luong-quang-cao-p1.md#doc-1771101186666498). Không sử dụng các từ ngữ nhạy cảm cho tên sự kiện tùy chỉnh. |
| ↳ event_time | integer | Bắt buộc | **Áp dụng cho web, app, offline, CRM.**<br>Thời điểm sự kiện diễn ra, biểu diễn bằng Unix timestamp tính bằng giây theo múi giờ UTC+0. |
| ↳ event_id | string | Có điều kiện | **Áp dụng cho web, offline, CRM.**<br>Bắt buộc khi:<br>1. Bạn gửi sự kiện web (`event_source = web`) đồng thời từ cả TikTok browser pixel và Events API.<br>2. Bạn gửi sự kiện CRM (`event_source = crm`) đồng thời từ cả Events API và file CSV trên Events Manager.<br>TikTok sử dụng bộ ba `event_source_id`, `event_id` và `event` để khử trùng lặp sự kiện (deduplication). Xem [Events API 2.0 - Khử trùng lặp sự kiện](../09-marketing-api/do-luong-quang-cao-p1.md#doc-1771100965992450). |
| ↳ user | object | Không | **Áp dụng cho web, app, offline, CRM.**<br>Thông tin định danh khách hàng nhằm phục vụ khớp dữ liệu người dùng (User Matching). Xem chi tiết bảng tham số `user` bên dưới. |
| ↳ properties | object | Không | **Áp dụng cho web, app, offline, CRM.**<br>Thông tin về sản phẩm, đơn hàng và các giá trị bổ trợ giúp tối ưu phân phối quảng cáo. Xem chi tiết bảng tham số `properties` bên dưới. |
| ↳ page | object | Có điều kiện | **Bắt buộc đối với sự kiện web.**<br>Thông tin về trang web nơi diễn ra sự kiện. Xem chi tiết bảng tham số `page` bên dưới. |
| ↳ app | object | Có điều kiện | **Bắt buộc đối với sự kiện app.**<br>Thông tin về ứng dụng di động nơi diễn ra sự kiện. Xem chi tiết bảng tham số `app` bên dưới. |
| ↳ ad | object | Không | **Chỉ áp dụng cho sự kiện app và web.**<br>Thông tin phân bổ và bối cảnh quảng cáo liên quan đến điểm chạm. Xem chi tiết bảng tham số `ad` bên dưới. |
| ↳ limited_data_use | boolean | Không | **Áp dụng cho sự kiện web và app.**<br>Tính năng giới hạn sử dụng dữ liệu để tuân thủ quyền riêng tư. Xem [Events API 2.0 - Limited Data Use](../09-marketing-api/do-luong-quang-cao-p1.md#doc-1771101204435970). |
| ↳ lead | object | Có điều kiện | **Bắt buộc đối với sự kiện CRM.**<br>Thông tin về khách hàng tiềm năng trong hệ thống CRM. Xem chi tiết bảng tham số `lead` bên dưới. |

---

### Tham số `user` (`user parameters`)

Events API 2.0 sử dụng thông tin khách hàng (như TikTok Click ID, Đối sánh nâng cao - Advanced Matching, địa chỉ IP và User Agent) để khớp các sự kiện người truy cập với người dùng TikTok. Khi khớp thành công, dữ liệu giúp xây dựng tệp đối tượng tùy chỉnh, cung cấp tín hiệu cho thuật toán tối ưu hóa chiến dịch và đo lường chuyển đổi chính xác hơn.

> [!IMPORTANT]
> - Các trường thông tin định danh cá nhân (PII) như `email`, `phone`, `external_id` **bắt buộc phải băm bằng thuật toán SHA-256** sau khi chuẩn hóa.
> - Với email: Xóa khoảng trắng thừa ở hai đầu (trim) và chuyển toàn bộ sang chữ thường (lowercase) trước khi băm.
> - Với số điện thoại: Chuẩn hóa về định dạng quốc tế E.164 (ví dụ: `+84912345678`), có tiền tố mã quốc gia dấu `+`, không dấu cách, không dấu ngoặc, không số 0 ở đầu mã vùng trước khi băm SHA-256.

| Field | Data Type | Description | Ví dụ |
|---|---|---|---|
| ttclid | string | **Chỉ áp dụng cho sự kiện web.**<br>TikTok Click ID, tham số kết nối dữ liệu được gắn vào URL trang đích khi người dùng nhấp vào quảng cáo TikTok. Thời gian hiệu lực tuân theo cài đặt cửa sổ CTA trong Attribution Manager. Xem [Gửi TikTok Click ID (ttclid)](../09-marketing-api/do-luong-quang-cao-p1.md#doc-1771100879787009). | `CjwKCAjw...` |
| email | string<br>hoặc string[] | **Áp dụng cho web, app, offline, CRM.**<br>**Bắt buộc băm SHA-256.** Địa chỉ email của khách hàng sau khi chuẩn hóa (trim khoảng trắng, lowercase). | `"848a771458438fc2ec420560d769fb9b9b86851ee338ec56517baabd79d3bb4f"` |
| phone | string<br>hoặc string[] | **Áp dụng cho web, app, offline, CRM.**<br>**Bắt buộc băm SHA-256.** Số điện thoại khách hàng sau khi chuẩn hóa về định dạng E.164 (có dấu `+` và mã quốc gia). | `"9f7ec22d72092cd3c0b58726ed9c2d91b92e51a3f29837508fb2948bb22dd2fd"` |
| external_id | string<br>hoặc string[] | **Áp dụng cho web và CRM.**<br>**Bắt buộc băm SHA-256.** Mã định danh duy nhất phía nhà quảng cáo (ID thành viên, ID người dùng nội bộ, cookie ID bên ngoài). Xem [Cài đặt External ID](../09-marketing-api/do-luong-quang-cao-p1.md#doc-1771100952291330). | `"80fba0ae1c48e3978e43e4efc365e14e12ea0c830ba8ba5b9a2dafc7e3f2ab8b"` |
| ttp | string | **Chỉ áp dụng cho sự kiện web.**<br>Cookie ID. Nếu bạn sử dụng Pixel SDK và bật cookie, Pixel SDK tự động lưu định danh duy nhất trong cookie `_ttp`. Giá trị này giúp khớp sự kiện web với quảng cáo TikTok. Xem [Gửi TikTok Cookie (_ttp)](../09-marketing-api/do-luong-quang-cao-p1.md#doc-1771100936446977). | `12345678-abcd-...` |
| ip | string | **Chỉ áp dụng cho sự kiện web và app.**<br>Địa chỉ IP công cộng (public IP) không băm của thiết bị người dùng. Hỗ trợ cả IPv4 và IPv6 (dạng đầy đủ hoặc rút gọn). Khuyến nghị gửi kèm cả `ip` và `user_agent`. | `"203.0.113.1"`<br>`"2001:db8:1111:a:b0::200"` |
| user_agent | string | **Chỉ áp dụng cho sự kiện web và app.**<br>Chuỗi User Agent không băm từ trình duyệt/thiết bị của người dùng. | `"Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X)..."` |
| idfa | string | **Chỉ áp dụng cho sự kiện app.**<br>Mã IDFA của thiết bị iOS. Chấp nhận dạng nguyên bản (chữ HOA) hoặc băm SHA-256 (chữ thường, trim). Tuân thủ chính sách quyền riêng tư của Apple. | `"EA7583CD-A667-48BC-B806-42ECB2B48606"` |
| idfv | string | **Chỉ áp dụng cho sự kiện app.**<br>Mã IDFV của thiết bị iOS. | `"60856DB8-7B2F-4DA9-B94F-294747CF06A9"` |
| gaid | string | **Chỉ áp dụng cho sự kiện app.**<br>Mã quảng cáo Google Advertising ID trên Android. Chấp nhận dạng thô (chữ thường) hoặc băm SHA-256. | `"aaaaaa-2222-1111-8787-809e92233ba0"` |
| locale | string | **Áp dụng cho sự kiện web và app.**<br>Mã định danh ngôn ngữ theo chuẩn BCP 47. | `"en-US"`, `"vi-VN"`, `"zh-CN"` |
| att_status | string | **Chỉ áp dụng cho sự kiện app.**<br>Trạng thái phân quyền AppTrackingTransparency trên iOS (từ iOS 14 trở lên).<br>Các giá trị enum:<br>• `AUTHORIZED`: Người dùng đồng ý cho phép theo dõi.<br>• `DENIED`: Người dùng từ chối theo dõi (TikTok sẽ không sử dụng dữ liệu PII để khớp người dùng).<br>• `NOT_DETERMINED`: Người dùng chưa nhận lời nhắc cấp quyền.<br>• `RESTRICTED`: Quyền bị hạn chế.<br>• `NOT_APPLICABLE`: Phiên bản iOS dưới 14 hoặc thiết bị Android. | `"AUTHORIZED"` |

---

### Tham số `properties` (`properties parameters`)

Thông tin về đơn hàng và sản phẩm liên quan đến sự kiện, hỗ trợ tối ưu hóa hiệu suất chiến dịch quảng cáo ROAS và quảng cáo Video Mua sắm (Video Shopping Ads - VSA).

| Field | Data Type | Description | Bắt buộc cho ROAS / VBO | Bắt buộc cho VSA |
|---|---|---|---|---|
| content_ids | string[] | Mảng các ID duy nhất của sản phẩm hoặc nội dung (ví dụ: `["987", "654"]`). Khuyến nghị dùng `sku_id` hoặc `item_group_id` khớp với danh mục sản phẩm (catalog). | | ✅ |
| contents | object[] | Mảng các đối tượng chi tiết từng sản phẩm trong sự kiện. Xem bảng tham số `contents` bên dưới. | | ✅ |
| content_type | string | Loại nội dung trong sự kiện. Các giá trị enum:<br>• `product`: Khi `content_id` trong `contents` là `sku_id`.<br>• `product_group`: Khi `content_id` trong `contents` là `item_group_id`. | | ✅ |
| currency | string | Mã tiền tệ theo chuẩn ISO 4217 (ví dụ: `USD`, `VND`, `EUR`, `JPY`, `SGD`, `THB`). Rất khuyến nghị cho các sự kiện liên quan đến doanh thu. | ✅ | |
| value | float | Tổng giá trị đơn hàng hoặc tổng giá trị các mặt hàng bán ra (ví dụ: `200.00`). Luôn định dạng là số nguyên hoặc số thập phân, không chứa ký hiệu tiền tệ hay dấu phẩy. | ✅ | |
| num_items | integer | Tổng số lượng mặt hàng trong đơn hàng. | | |
| search_string | string | Chuỗi tìm kiếm do người dùng nhập. | | |
| description | string | Mô tả sản phẩm hoặc nội dung trang web. | | |
| order_id | string | Mã định danh đơn hàng (Order ID). | | |
| shop_id | string | Mã định danh cửa hàng (Shop ID). | | |
| customer_type | string | **Chỉ cho app và web.** Phân khúc khách hàng liên quan đến chuyển đổi. Giá trị enum:<br>• `new`: Khách hàng mới.<br>• `returning`: Khách hàng quay lại. | | |

#### Tham số con trong `contents` (`contents parameters`)

| Field | Data Type | Description | Bắt buộc cho VSA |
|---|---|---|---|
| price | float | Đơn giá của một mặt hàng (ví dụ: `100.00`). Lưu ý: `price` là giá của một sản phẩm đơn lẻ, còn `value` là tổng giá trị đơn hàng. | |
| content_id | string | ID duy nhất của sản phẩm hoặc nội dung. Khớp với `sku_id` hoặc `item_group_id` trong danh mục sản phẩm. | ✅ |
| content_category | string | Danh mục sản phẩm hoặc trang nội dung (ví dụ: `Shoes > Sneakers`). | |
| content_name | string | Tên sản phẩm hoặc tiêu đề nội dung (ví dụ: `Fancy AirMax 2.0`). | |
| brand | string | Tên thương hiệu của sản phẩm. | |

---

### Tham số `page` (`page parameters`)

Chỉ áp dụng cho sự kiện trên trang web (`event_source = web`).

| Field | Data Type | Bắt buộc | Description |
|---|---|---|---|
| url | string | Bắt buộc | URL trình duyệt nơi sự kiện diễn ra (tương đương `location.href` trong Javascript). Khuyến nghị truyền URL đầy đủ bao gồm cả các tham số query. |
| referrer | string | Không | URL giới thiệu (tương đương `document.referrer` hoặc header HTTP `Referer`). Khuyến nghị truyền URL đầy đủ. |

---

### Tham số `app` (`app parameters`)

Chỉ áp dụng cho sự kiện ứng dụng di động (`event_source = app`).

| Field | Data Type | Bắt buộc | Description |
|---|---|---|---|
| app_id | string | Bắt buộc | ID ứng dụng di động:<br>• Với iOS: ID ứng dụng trên Apple App Store (ví dụ URL `id343200656` -> `"343200656"`).<br>• Với Android trên Google Play: Package name (ví dụ `"com.rovio.angrybirds"`).<br>• Với Android ngoài Google Play: Package name của ứng dụng. |
| app_name | string | Không | Tên hiển thị của ứng dụng di động. |
| app_version | string | Không | Số phiên bản của ứng dụng di động (ví dụ: `"3.0.2"`). |

---

### Tham số `ad` (`ad parameters`)

Áp dụng cho sự kiện App và Web (`event_source = app` hoặc `web`) nhằm cung cấp tín hiệu phân bổ nâng cao.

| Field | Data Type | Description |
|---|---|---|
| callback | string | **Chỉ cho app.** Thông tin callback từ hệ thống đo lường MMP để hỗ trợ phân bổ sự kiện. |
| campaign_id | string | **Cho app và web.** ID chiến dịch quảng cáo TikTok gắn với điểm chạm, thường trích xuất từ landing URL hoặc deeplink. |
| ad_id | string | **Cho app và web.** ID nhóm quảng cáo TikTok gắn với điểm chạm, thường trích xuất từ landing URL hoặc deeplink. |
| creative_id | string | **Cho app và web.** ID quảng cáo (ad ID) TikTok gắn với điểm chạm, thường trích xuất từ landing URL hoặc deeplink. |
| is_retargeting | boolean | **Chỉ cho app.** Người dùng có phải là đối tượng tiếp thị lại (retargeting) hay không. |
| attributed | boolean | **Chỉ cho app.** Sự kiện có được phân bổ cho quảng cáo hay không. |
| attribution_type | string | **Chỉ cho app.** Loại phân bổ (ví dụ: `click_through`, `view_through`). |
| attribution_provider | string | **Cho app và web.** Nhà cung cấp dịch vụ đo lường phân bổ. |
| attribution_share | float | **Cho app và web.** Tỷ lệ phần trăm công nhận phân bổ cho TikTok trên sự kiện chuyển đổi này (từ `0.0` đến `1.0`). |
| attribution_value | float | **Cho app và web.** Phần doanh thu phân bổ của chuyển đổi mà hệ thống của bạn gán cho điểm chạm TikTok này (thường bằng tổng giá trị nhân với `attribution_share`). |
| attribution_model | string | **Cho app và web.** Mô hình phân bổ áp dụng cho sự kiện. Các giá trị ví dụ:<br>• `linear`: Chia đều công nhận cho các điểm chạm.<br>• `first_click` / `first_touch`: Công nhận toàn bộ cho lần nhấp/điểm chạm đầu tiên.<br>• `last_click` / `last_touch`: Công nhận toàn bộ cho lần nhấp/điểm chạm cuối cùng.<br>• `even_weight`: Trọng số phân bổ đều nhau. |
| touchpoint_type | string | **Cho app và web.** Loại điểm chạm TikTok nhận được phân bổ. Các giá trị ví dụ:<br>• `click`: Nhấp vào quảng cáo.<br>• `view`: Lượt hiển thị quảng cáo.<br>• `engaged_view`: Xem video quảng cáo từ 6 giây trở lên.<br>• `engaged_click`: Tương tác với định dạng quảng cáo tương tác.<br>• `click_to_store`: Nhấp chuyển thẳng tới chợ ứng dụng.<br>• `hybrid`: Kết hợp cả tín hiệu click và view.<br>• `other`: Điểm chạm khác. |
| touchpoint_ts | integer | **Cho app và web.** Thời điểm điểm chạm TikTok diễn ra, tính bằng Unix timestamp theo giây UTC+0. |
| touchpoint_url | string | **Cho app và web.** URL nơi điểm chạm được ghi nhận (ví dụ: URL trang đích sau khi nhấp quảng cáo). |
| attribution_window_hr_click | integer | **Cho app và web.** Cửa sổ phân bổ nhấp chuột tính bằng **giờ** (ví dụ: `24` cho 1 ngày, `168` cho 7 ngày, `720` cho 30 ngày). |
| attribution_window_hr_view | integer | **Cho app và web.** Cửa sổ phân bổ lượt xem tính bằng **giờ** (ví dụ: `24` cho 1 ngày, `168` cho 7 ngày). |
| attribution_method | string | **Cho app và web.** Phương thức kỹ thuật liên kết điểm chạm với chuyển đổi (ví dụ: `pixel`, `PPS`, `deeplink`, `modeled`, `SKAN`, `shop`). |
| decline_reason | string | **Cho app và web.** Lý do hệ thống của bạn từ chối gán phân bổ cho TikTok. Các giá trị ví dụ: `attributed_to_other_source`, `organic`, `outside_attribution_window`, `invalid_event`, `fraud_detected`, `duplicate_event`, `low_confidence_match`, `missing_touchpoint`, `missing_click_id`, `privacy_threshold_filtered`, `unsupported_signal`, `other`. |
| utm_id | string | **Cho app và web.** Mã định danh chiến dịch tiếp thị trích xuất từ tham số `utm_id` trong URL trang đích. |
| utm_source | string | **Cho app và web.** Nguồn lưu lượng truy cập từ tham số `utm_source` trong URL (ví dụ: `tiktok`). |
| utm_medium | string | **Cho app và web.** Phương tiện tiếp thị từ tham số `utm_medium` trong URL (ví dụ: `paid_social`, `cpc`). |
| utm_campaign | string | **Cho app và web.** Tên chiến dịch từ tham số `utm_campaign` trong URL. |

---

### Tham số `lead` (`lead parameters`)

Chỉ áp dụng cho sự kiện khách hàng tiềm năng CRM (`event_source = crm`).

| Field | Data Type | Bắt buộc | Description |
|---|---|---|---|
| lead_id | string | Bắt buộc | ID của khách hàng tiềm năng TikTok. Mỗi lead xuất từ TikTok đều có mã `lead_id`. Bạn có thể lấy ID này qua các endpoint tải lead [/page/lead/task/](48-leads.md#doc-1739052936772610), [/page/lead/task/download/](48-leads.md#doc-1739053563877378), hoặc tải từ TikTok Leads Center. |
| lead_event_source | string | Không | Tên nguồn sự kiện lead, ví dụ tên hệ thống CRM của bạn như `HubSpot` hoặc `Salesforce`. |

---

### Phản hồi

| Field | Data Type | Description |
|---|---|---|
| code | number | Mã phản hồi API. `0` biểu thị thành công. Xem [Mã trả về (Return Code)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông báo phản hồi (`OK` khi thành công). |
| request_id | string | Mã nhật ký định danh duy nhất của yêu cầu. |
| data | object | Dữ liệu trả về (object rỗng `{}` khi thành công). |

---

### Ví dụ gọi API

#### 1. Báo cáo sự kiện Web (`Web Events`)

##### cURL
```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/event/track/' \
--header 'Access-Token: act.example123456789' \
--header 'Content-Type: application/json' \
--data-raw '{
  "event_source": "web",
  "event_source_id": "C1234567890ABCDEF",
  "data": [
    {
      "event": "Purchase",
      "event_time": 1718876400,
      "event_id": "order_ord_987654321",
      "user": {
        "ttclid": "CjwKCAjw...",
        "ttp": "12345678-abcd-ef01-2345-6789abcdef01",
        "email": "848a771458438fc2ec420560d769fb9b9b86851ee338ec56517baabd79d3bb4f",
        "phone": "9f7ec22d72092cd3c0b58726ed9c2d91b92e51a3f29837508fb2948bb22dd2fd",
        "ip": "203.0.113.1",
        "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15"
      },
      "page": {
        "url": "https://www.mystore.com/checkout/success?order_id=ord_987654321",
        "referrer": "https://www.mystore.com/cart"
      },
      "properties": {
        "currency": "USD",
        "value": 150.0,
        "content_type": "product",
        "order_id": "ord_987654321",
        "contents": [
          {
            "content_id": "SKU_RUNNING_SHOE_01",
            "content_name": "Pro Running Shoe",
            "content_category": "Footwear",
            "price": 150.0,
            "brand": "ActiveGear"
          }
        ]
      }
    }
  ]
}'
```

##### Python
```python
import requests
import hashlib
import time

ACCESS_TOKEN = "act.example123456789"
PIXEL_CODE = "C1234567890ABCDEF"
url = "https://business-api.tiktok.com/open_api/v1.3/event/track/"

def hash_sha256(value: str) -> str:
    return hashlib.sha256(value.strip().lower().encode("utf-8")).hexdigest()

headers = {
    "Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}

payload = {
    "event_source": "web",
    "event_source_id": PIXEL_CODE,
    "data": [
        {
            "event": "Purchase",
            "event_time": int(time.time()),
            "event_id": "order_ord_987654321",
            "user": {
                "email": hash_sha256("customer@example.com"),
                "phone": hash_sha256("+84912345678"),
                "ip": "203.0.113.1",
                "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            },
            "page": {
                "url": "https://www.mystore.com/checkout/success",
                "referrer": "https://www.mystore.com/cart"
            },
            "properties": {
                "currency": "USD",
                "value": 150.0,
                "order_id": "ord_987654321",
                "content_type": "product",
                "contents": [
                    {
                        "content_id": "SKU_RUNNING_SHOE_01",
                        "content_name": "Pro Running Shoe",
                        "price": 150.0
                    }
                ]
            }
        }
    ]
}

response = requests.post(url, headers=headers, json=payload)
data = response.json()
print("Kết quả báo cáo sự kiện Web:", data.get("code"), data.get("message"))
```

#### 2. Báo cáo sự kiện Khách hàng tiềm năng CRM (`CRM Events`)

##### cURL
```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/event/track/' \
--header 'Access-Token: act.example123456789' \
--header 'Content-Type: application/json' \
--data-raw '{
  "event_source": "crm",
  "event_source_id": "crm_set_123456",
  "data": [
    {
      "event": "QualifiedLead",
      "event_time": 1718876400,
      "event_id": "crm_lead_qual_001",
      "lead": {
        "lead_id": "6864523782069944582",
        "lead_event_source": "Salesforce"
      },
      "user": {
        "external_id": "80fba0ae1c48e3978e43e4efc365e14e12ea0c830ba8ba5b9a2dafc7e3f2ab8b",
        "email": "848a771458438fc2ec420560d769fb9b9b86851ee338ec56517baabd79d3bb4f"
      }
    }
  ]
}'
```

#### 3. Báo cáo sự kiện Ngoại tuyến (`Offline Events`)

##### cURL
```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/event/track/' \
--header 'Access-Token: act.example123456789' \
--header 'Content-Type: application/json' \
--data-raw '{
  "event_source": "offline",
  "event_source_id": "offline_set_789012",
  "data": [
    {
      "event": "Purchase",
      "event_time": 1718876400,
      "event_id": "pos_receipt_554433",
      "user": {
        "phone": ["9f7ec22d72092cd3c0b58726ed9c2d91b92e51a3f29837508fb2948bb22dd2fd"],
        "email": ["848a771458438fc2ec420560d769fb9b9b86851ee338ec56517baabd79d3bb4f"]
      },
      "properties": {
        "order_id": "pos_receipt_554433",
        "shop_id": "store_hcm_01",
        "currency": "VND",
        "value": 2500000.0,
        "contents": [
          {
            "content_id": "SKU_JACKET_WINTER",
            "content_name": "Winter Jacket",
            "price": 2500000.0,
            "brand": "ActiveWear"
          }
        ]
      }
    }
  ]
}'
```

#### Ví dụ phản hồi thành công

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20261023120000010245035048F9E8D7",
  "data": {}
}
```
