# Báo cáo (Reporting)

Tài liệu này cung cấp hướng dẫn và tài liệu tham khảo chi tiết cho các API Báo cáo (Reporting APIs) của TikTok for Business. Bạn có thể sử dụng các API này để trích xuất dữ liệu phân tích và hiệu suất quảng cáo cho cả quảng cáo đấu thầu (auction ads) và quảng cáo đặt trước (reservation ads) theo hai chế độ: **đồng bộ** (synchronous) hoặc **bất đồng bộ** (asynchronous).

Tài liệu gồm các phần chính sau:
- [Tổng quan Báo cáo (Reporting)](58-reporting.md#doc-1740302665828417)
- [Chạy báo cáo đồng bộ (Run a synchronous report)](58-reporting.md#doc-1740302848100353)
- [Tạo tác vụ báo cáo bất đồng bộ (Create an asynchronous report task)](58-reporting.md#doc-1740302766489602)
- [Kiểm tra trạng thái tác vụ báo cáo bất đồng bộ (Get the status of an async report task)](58-reporting.md#doc-1740302781443073)
- [Tải kết quả báo cáo bất đồng bộ (Download the output of an async report task)](58-reporting.md#doc-1740302808815618)
- [Hủy tác vụ báo cáo bất đồng bộ (Cancel an asynchronous report task)](58-reporting.md#doc-1803615367145537)

---

## Tổng quan Báo cáo (`Reporting`)
<a id="doc-1740302665828417"></a>
<!-- doc_id: 1740302665828417 -->

> Đường dẫn: API Reference > Reporting

Bạn có thể sử dụng Reporting API để chạy báo cáo dữ liệu quảng cáo đấu thầu và quảng cáo đặt trước ở chế độ đồng bộ (synchronous) hoặc bất đồng bộ (asynchronous).

Để xem tổng quan về Reporting API, xem [Overview](../09-marketing-api/bao-cao-p1.md#doc-1751087777884161). Để tìm hiểu chi tiết về báo cáo đồng bộ, bất đồng bộ và các loại báo cáo khác nhau, xem [Guides](../09-marketing-api/bao-cao-p1.md#doc-1751087792726017):
- [Báo cáo đồng bộ và bất đồng bộ (Synchronous and asynchronous reports)](../09-marketing-api/bao-cao-p1.md#doc-1751088469160001): hướng dẫn cách chạy báo cáo đồng bộ và bất đồng bộ.
- [Các loại báo cáo (Report types)](../09-marketing-api/bao-cao-p1.md#doc-1738864835805186): giới thiệu **trường hợp sử dụng** (use cases) của báo cáo cơ bản (`BASIC`), báo cáo đối tượng (`AUDIENCE`), báo cáo nội dung tương tác (`PLAYABLE_MATERIAL`), báo cáo quảng cáo mua sắm động DSA (`CATALOG`), báo cáo Business Center (`BC`), báo cáo GMV Max, cùng danh sách chiều dữ liệu (dimensions), chỉ số (metrics) và bộ lọc (filters) tương ứng.
- [Thực tiễn tối ưu (Best practices)](../09-marketing-api/bao-cao-p4.md#doc-1738864817670145): tổng hợp kinh nghiệm tối ưu nhằm tránh hoặc giảm thiểu hiện tượng timeout trong các truy vấn báo cáo đồng bộ.
- [Độ trễ dữ liệu cho báo cáo (Data latency for reports)](../09-marketing-api/bao-cao-p4.md#doc-1738864894606337): thông tin về độ trễ cập nhật số liệu khi sử dụng Reporting API.
- [Câu hỏi thường gặp (FAQs)](../09-marketing-api/bao-cao-p4.md#doc-1738864850353154): giải đáp các câu hỏi phổ biến liên quan đến Reporting API.

Nhóm API này bao gồm các endpoint sau:
- [Run a synchronous report](58-reporting.md#doc-1740302848100353): Chạy báo cáo đồng bộ (`/report/integrated/get/`).
- [Create an asynchronous report task](58-reporting.md#doc-1740302766489602): Tạo tác vụ báo cáo bất đồng bộ (`/report/task/create/`).
- [Get the status of an async report task](58-reporting.md#doc-1740302781443073): Kiểm tra tiến độ và trạng thái tác vụ (`/report/task/check/`).
- [Download the output of an async report task](58-reporting.md#doc-1740302808815618): Tải xuống file hoặc lấy link tải kết quả báo cáo (`/report/task/download/`).
- [Cancel an asynchronous report task](58-reporting.md#doc-1803615367145537): Hủy tác vụ báo cáo đang chờ xử lý hoặc đang chạy (`/report/task/cancel/`).

---

## Chạy báo cáo đồng bộ (`Run a synchronous report`)
<a id="doc-1740302848100353"></a>
<!-- doc_id: 1740302848100353 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/report/integrated/get/`

**Mục đích**: Chạy truy vấn lấy dữ liệu báo cáo quảng cáo tích hợp theo thời gian thực (đồng bộ).

> [!IMPORTANT]
> - Nếu bạn muốn lấy dữ liệu báo cáo của các chiến dịch GMV Max (Product GMV Max hoặc Live GMV Max), vui lòng sử dụng endpoint chuyên biệt [/gmv_max/report/get/](45-gmv-max-p2.md#doc-1824721673497601) thay vì endpoint này.
> - Endpoint này hiện hỗ trợ trả về tối đa **20.000 quảng cáo**. Nếu số lượng quảng cáo của bạn vượt quá 20.000, vui lòng sử dụng bộ lọc `campaign_ids` / `adgroup_ids` / `ad_ids` trong `filtering` để lấy dữ liệu theo từng đợt (mỗi đợt tối đa 100 ID).

> [!NOTE]
> - **So sánh dữ liệu với TikTok Ads Manager (TTAM)**: Nếu so sánh dữ liệu báo cáo đồng bộ với file báo cáo tải xuống từ giao diện TTAM, bạn có thể nhận thấy sự không nhất quán vì báo cáo tải từ TTAM tương đương với **báo cáo bất đồng bộ (asynchronous report)** của API chứ không phải báo cáo đồng bộ. Cả báo cáo tải từ TTAM và báo cáo bất đồng bộ của API đều không bị giới hạn cắt bớt 20.000 bản ghi quảng cáo.
> - Để tìm hiểu cách chạy báo cáo đồng bộ, xem [Run a synchronous report](../09-marketing-api/bao-cao-p1.md#doc-1738864778664961).
> - Để biết các chiều dữ liệu (dimensions), chỉ số (metrics) và use cases cho từng loại báo cáo, xem [Report types](../09-marketing-api/bao-cao-p1.md#doc-1738864835805186).
> - Mối quan hệ giữa loại dịch vụ quảng cáo (`service_type`), loại báo cáo (`report_type`) và cấp độ dữ liệu (`data_level`), xem [Overview-Data level](../09-marketing-api/bao-cao-p1.md#doc-1751087777884161).
> - Giải đáp thắc mắc thường gặp, xem [FAQ](../09-marketing-api/bao-cao-p4.md#doc-1738864850353154).

### Header
| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Có | Mã truy cập đã được ủy quyền (Authorized access token). Xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (GET: query string)
> [!NOTE]
> Các tham số có kiểu dữ liệu là mảng (`string[]`, `object[]`) hoặc đối tượng (`object`) khi gọi bằng GET phải được truyền dưới dạng chuỗi JSON đã URL-encode trong query string (ví dụ: `dimensions=["campaign_id","stat_time_day"]`, `filtering=[{"field_name":"adgroup_ids","filter_type":"IN","filter_value":"[\"123\"]"}]`).

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | Điều kiện | Bắt buộc truyền `advertiser_id`/`advertiser_ids` hoặc `bc_id`.<br>• Khi `report_type` là `BASIC` hoặc `AUDIENCE`: truyền `advertiser_id` hoặc `advertiser_ids`. Nếu truyền cả hai, `advertiser_id` sẽ bị bỏ qua.<br>• Khi `report_type` là `PLAYABLE_MATERIAL`, `CATALOG` hoặc `TT_SHOP`: truyền `advertiser_id`.<br>• Khi `report_type` là `BC`: truyền `bc_id`.<br>ID của tài khoản quảng cáo (Advertiser ID). |
| `advertiser_ids` | string[] | Điều kiện | Danh sách các ID nhà quảng cáo. Tối đa: 5 ID.<br>• Hợp lệ khi `report_type` là `BASIC` hoặc `AUDIENCE`.<br>• Khi dùng `advertiser_ids`, hệ thống trả về tối đa 20.000 ID sắp xếp theo thời gian tạo giảm dần (descending), không đảm bảo số lượng phân bổ đều cho từng advertiser.<br>• Dữ liệu số liệu (`metrics`) trả về sẽ bao gồm thêm `currency`, `timezone`, và `advertiser_id`.<br>• Các nhà quảng cáo có thể khác múi giờ: dùng `multi_adv_report_in_utc_time` để chọn chuyển về UTC+0 hay giữ múi giờ địa phương của từng tài khoản.<br>• Dữ liệu chi phí của mỗi tài khoản trả về theo đúng loại tiền tệ của tài khoản đó (không có dấu thập phân, ví dụ "100 USD" hiển thị là 100).<br>• Để xem tổng số liệu gộp của tất cả advertiser, bật `enable_total_metrics=true`.<br>> [!NOTE]<br>> • Nếu dùng `advertiser_ids` nhưng không đặt chiều ID nào trong `dimensions`, trường `currency`, `timezone`, `advertiser_id` sẽ có giá trị `0`, và các chỉ số chi phí (như `spend`) sẽ trả về `-`.<br>> • Tất cả tài khoản trong `advertiser_ids` phải thuộc cùng một người dùng TikTok for Business. Dùng [/oauth2/advertiser/get/](03-ad-accounts.md#doc-1738455508553729) để lấy danh sách tài khoản thuộc cùng người dùng. |
| `bc_id` | string | Điều kiện | Bắt buộc khi `report_type` là `BC`. ID của Business Center. |
| `service_type` | string | Không | Loại dịch vụ quảng cáo.<br>Giá trị enum:<br>• `AUCTION`: Quảng cáo đấu thầu (auction ads), hoặc truy vấn cả quảng cáo đấu thầu và quảng cáo đặt trước. Mặc định là `AUCTION`.<br>• `RESERVATION` *(đã ngừng hỗ trợ - deprecated)*: Quảng cáo đặt trước.<br>> [!NOTE]<br>> Để lấy dữ liệu báo cáo quảng cáo TopView, sử dụng báo cáo cơ bản (`BASIC`) hoặc báo cáo đối tượng (`AUDIENCE`) và chỉ định giá trị `RESERVATION_TOP_VIEW` cho bộ lọc `buying_type`. |
| `report_type` | string | Có | Loại báo cáo. Giá trị enum:<br>• `BASIC`: Báo cáo cơ bản (basic report).<br>• `AUDIENCE`: Báo cáo đối tượng (audience report).<br>• `PLAYABLE_MATERIAL`: Báo cáo nội dung tương tác (playable ads report).<br>• `CATALOG`: Báo cáo danh mục sản phẩm / DSA (DSA report).<br>• `BC`: Báo cáo Business Center (Business Center report).<br>• `TT_SHOP`: Báo cáo TikTok Shop.<br>Khi `service_type` là `AUCTION`, các loại báo cáo `BASIC`, `AUDIENCE`, `PLAYABLE_MATERIAL`, `CATALOG` đều được hỗ trợ.<br>> [!NOTE]<br>> Bạn có thể lấy dữ liệu cấp nội dung sáng tạo (creative level) cho Upgraded Smart+ Ads khi `report_type` là `BASIC`, `AUDIENCE` hoặc `CATALOG`. |
| `data_level` | string | Điều kiện | Cấp độ dữ liệu muốn truy vấn. Bắt buộc khi `report_type` là `BASIC`, `AUDIENCE` hoặc `CATALOG`.<br>Giá trị enum:<br>• `AUCTION_AD`: Cấp quảng cáo (ad level) cho quảng cáo đấu thầu hoặc cả đấu thầu và đặt trước.<br>• `AUCTION_ADGROUP`: Cấp nhóm quảng cáo (ad group level).<br>• `AUCTION_CAMPAIGN`: Cấp chiến dịch (campaign level).<br>• `AUCTION_ADVERTISER`: Cấp tài khoản nhà quảng cáo (advertiser level).<br>• `RESERVATION_AD` *(deprecated)*: Cấp quảng cáo đặt trước.<br>• `RESERVATION_ADGROUP` *(deprecated)*: Cấp nhóm quảng cáo đặt trước.<br>• `RESERVATION_CAMPAIGN` *(deprecated)*: Cấp chiến dịch đặt trước.<br>• `RESERVATION_ADVERTISER` *(deprecated)*: Cấp tài khoản nhà quảng cáo đặt trước. |
| `dimensions` | string[] | Có | Điều kiện nhóm dữ liệu (grouping conditions), ví dụ: `["campaign_id", "stat_time_day"]`.<br>Mỗi loại báo cáo hỗ trợ các chiều dữ liệu khác nhau:<br>• Chiều hỗ trợ trong [Báo cáo cơ bản](../09-marketing-api/bao-cao-p1.md#doc-1751443956638721)<br>• Chiều hỗ trợ trong [Báo cáo đối tượng](../09-marketing-api/bao-cao-p3.md#doc-1751454103714818)<br>• Chiều hỗ trợ trong [Báo cáo playable ad](../09-marketing-api/bao-cao-p3.md#doc-1751617879104514)<br>• Chiều hỗ trợ trong [Báo cáo DSA](../09-marketing-api/bao-cao-p3.md#doc-1751617879104514)<br>• Chiều hỗ trợ trong [Báo cáo Business Center](../09-marketing-api/bao-cao-p3.md#doc-1775747465089026)<br>> [!NOTE]<br>> • Nếu `dimensions` chỉ định nhiều hơn các trường ID (xx_id) mà không có dữ liệu quảng cáo phát sinh trong khoảng thời gian truy vấn, mảng rỗng sẽ được trả về.<br>> • Chiều `ad_id_v2` khả dụng khi `report_type` là `BASIC`, `AUDIENCE` hoặc `CATALOG`. Không thể dùng chung `ad_id_v2` với chiều `ad_id` hoặc bộ lọc `ad_ids`. Chiều này hỗ trợ lấy dữ liệu cấp quảng cáo (ad level) cho Manual Ads, Smart+ Campaigns và Upgraded Smart+ Ads. |
| `metrics` | string[] | Không | Danh sách chỉ số cần truy vấn. Chi tiết chỉ số hỗ trợ cho từng loại báo cáo xem tại [Report types](../09-marketing-api/bao-cao-p1.md#doc-1738864835805186).<br>Giá trị mặc định:<br>• Khi `report_type` là `BASIC`, `AUDIENCE`, `PLAYABLE_MATERIAL`, `CATALOG`: mặc định là `["spend", "impressions"]`.<br>• Khi `report_type` là `BC`: mặc định là tất cả chỉ số hỗ trợ bởi nhóm chiều chỉ định qua `dimensions`.<br>• Khi `report_type` là `TT_SHOP`: mặc định là `["spend", "billed_cost"]`.<br>Số tiền của các chỉ số tiền tệ dựa trên đơn vị tiền tệ thiết lập trong tài khoản quảng cáo. |
| `enable_total_metrics` | boolean | Không | Có bật dữ liệu tổng cộng gộp cho các chỉ số được yêu cầu hay không.<br>Khi bật `enable_total_metrics=true`, hệ thống cung cấp dữ liệu tổng hợp của tất cả các trang. Bạn chỉ cần chỉ định tham số này khi yêu cầu dữ liệu cho trang đầu tiên.<br>Do giới hạn cắt bớt 20.000 bản ghi, hệ thống cung cấp dữ liệu gộp cho tối đa 20.000 ID.<br>> [!NOTE]<br>> • Chỉ hỗ trợ báo cáo cơ bản đấu thầu (`AUCTION` + `BASIC`) và báo cáo quảng cáo GMV Max.<br>> • Chỉ hợp lệ khi trong `dimensions` có đúng một chiều ID và/hoặc `stat_time_day` (ví dụ: `["campaign_id"]`, `["campaign_id", "stat_time_day"]`).<br>> • Không hỗ trợ trong môi trường sandbox. |
| `start_date` | string | Điều kiện | Bắt buộc khi `query_lifetime` là `false` hoặc không được truyền.<br>Ngày bắt đầu truy vấn (khoảng đóng), định dạng `YYYY-MM-DD`. Dựa trên múi giờ của tài khoản quảng cáo.<br>> [!NOTE]<br>> • Khi `report_type` khác `BC` và `dimensions` không chứa `stat_time_day`, khoảng thời gian tối đa giữa `start_date` và `end_date` là 365 ngày.<br>> • Khi `report_type` khác `BC` và `dimensions` chứa `stat_time_day`, khoảng thời gian tối đa là 30 ngày.<br>> • Khi `report_type` là `BC`, khoảng thời gian tối đa là 365 ngày. |
| `end_date` | string | Điều kiện | Bắt buộc khi `query_lifetime` là `false` hoặc không được truyền.<br>Ngày kết thúc truy vấn (khoảng đóng), định dạng `YYYY-MM-DD`. Quy tắc giới hạn ngày tương tự như `start_date`. |
| `query_lifetime` | boolean | Không | Được hỗ trợ khi `report_type` là `BASIC` hoặc `PLAYABLE_MATERIAL`.<br>Có truy vấn số liệu tích lũy toàn thời gian (lifetime) hay không. Mặc định: `false`. Nếu đặt là `true`, tham số `start_date` và `end_date` sẽ bị bỏ qua.<br>> [!NOTE]<br>> • Không hỗ trợ phân tích theo thời gian hoặc đối tượng khi truy vấn số liệu lifetime.<br>> • Không hỗ trợ phân tích theo mã vị trí (`country_code`) khi truy vấn số liệu lifetime.<br>> • Báo cáo đối tượng (`AUDIENCE`), DSA (`CATALOG`), Business Center (`BC`) và GMV Max không hỗ trợ số liệu lifetime. |
| `multi_adv_report_in_utc_time` | boolean | Không | Được hỗ trợ khi dùng `advertiser_ids`. Có thiết lập số liệu trả về theo múi giờ UTC+0 cho tất cả nhà quảng cáo hay không. Mặc định: `false` (trả về theo múi giờ địa phương của từng tài khoản). Nếu đặt là `true`, số liệu sẽ đồng nhất về UTC+0. |
| `order_field` | string | Không | Trường dùng để sắp xếp kết quả. Tất cả các chỉ số được hỗ trợ (ngoại trừ các chỉ số thuộc tính) đều hỗ trợ sắp xếp. Mặc định không sắp xếp. |
| `order_type` | string | Không | Chiều sắp xếp. Giá trị enum:<br>• `ASC`: Tăng dần.<br>• `DESC`: Giảm dần.<br>Mặc định: `DESC`. |
| `filtering` | object[] | Không | Điều kiện lọc. Hỗ trợ khi `report_type` là `BASIC`, `AUDIENCE`, `PLAYABLE_MATERIAL`, `CATALOG` hoặc `BC`. Không hỗ trợ với `TT_SHOP`.<br>Chi tiết bộ lọc hỗ trợ theo từng loại báo cáo xem tại [Report types](../09-marketing-api/bao-cao-p1.md#doc-1738864835805186).<br>> [!NOTE]<br>> • Khi truyền `filtering`, bạn phải chỉ định đồng thời cả 3 trường `field_name`, `filter_type`, `filter_value` trong một object.<br>> • Nếu muốn dùng `country_code` làm bộ lọc nhóm, hãy chỉ định `country_code` trong tham số `dimensions`. |
| ↳ `field_name` | string | Điều kiện | Tên trường lọc (ví dụ `campaign_ids`, `adgroup_ids`, `ad_ids`, `ad_ids_v2`, `country_code`, `campaign_automation_type`).<br>Bộ lọc `ad_ids_v2` khả dụng khi `data_level` là `AUCTION_AD` và `dimensions` chứa `ad_id_v2`. Không dùng chung với `ad_id` hoặc bộ lọc `ad_ids`. Tối đa 100 giá trị. |
| ↳ `filter_type` | string | Điều kiện | Loại bộ lọc. Giá trị enum:<br>• `IN`: Chứa bất kỳ giá trị nào (khớp chính xác). Khi dùng loại này, `filter_value` phải là chuỗi JSON array hợp lệ.<br>• `CONTAIN_ANY_OF`: Chứa bất kỳ giá trị nào (khớp mờ). `filter_value` phải là chuỗi JSON array.<br>• `MATCH`: Khớp mờ, tương đương với toán tử `LIKE` trong SQL.<br>• `NOT_IN`: Không chứa bất kỳ giá trị nào (khớp chính xác). `filter_value` phải là chuỗi JSON array.<br>• `GREATER_EQUAL`: Lớn hơn hoặc bằng (>=).<br>• `GREATER_THAN`: Lớn hơn (>).<br>• `LOWER_EQUAL`: Nhỏ hơn hoặc bằng (<=).<br>• `LOWER_THAN`: Nhỏ hơn (<).<br>• `BETWEEN`: Nằm trong khoảng. Khi dùng loại này, `filter_value` phải là chuỗi JSON array chứa đúng hai phần tử chuỗi. |
| ↳ `filter_value` | string | Điều kiện | Giá trị lọc. Khi `filter_type` là `IN`, `CONTAIN_ANY_OF` hoặc `NOT_IN`, `filter_value` phải là một chuỗi biểu diễn mảng JSON hợp lệ (ví dụ `"[\"12345\",\"67890\"]"`). |
| `query_mode` | string | Không | *(Sắp ngừng hỗ trợ - To be deprecated)* Chế độ truy vấn dữ liệu. Không hỗ trợ với `BC`.<br>Giá trị enum: `REGULAR`, `CHUNK`. Mặc định: `REGULAR`.<br>> [!WARNING]<br>> Chế độ `CHUNK` sắp bị ngừng hỗ trợ hoàn toàn. TikTok khuyến nghị không nên sử dụng chế độ này. |
| `page` | number | Không | Số trang hiện tại. Mặc định: `1`. |
| `page_size` | number | Không | Số bản ghi trên mỗi trang. Phạm vi giá trị: 1–1.000. Mặc định: `10`. |

### Phản hồi

#### Response Header
| Tên | Kiểu | Mô tả |
|---|---|---|
| `X-Tt-Ads-Throttle` | string | Thông báo cảnh báo khi yêu cầu vượt quá giới hạn hệ thống. Ví dụ: khi số lượng ID quảng cáo vượt quá 20.000: `X-Tt-Ads-Throttle: "Number of ad ids is equal or more than 20k, only return the top 20k id's results, sorting by create time desc order."` |

#### Response Parameters
| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Thành công trả về `0`. Chi tiết xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | ID định danh duy nhất của yêu cầu (log ID). |
| `data` | object | Dữ liệu trả về. |
| ↳ `total_metrics` | object | Dữ liệu tổng hợp gộp của các chỉ số yêu cầu. Được trả về khi bật `enable_total_metrics=true` trong yêu cầu. |
| ↳↳ `campaign_name` | string | Tên chiến dịch đấu thầu / Tên nhóm quảng cáo đặt trước. Các chỉ số không thể tổng hợp sẽ trả về `-`. |
| ↳↳ `spend` | string | Tổng số tiền đã chi tiêu (spend). |
| ↳↳ `impressions` | string | Tổng số lượt hiển thị (impressions). |
| ↳↳ `reach` | string | Tổng số người tiếp cận (reach). |
| ↳ `list` | object[] | Danh sách dữ liệu báo cáo chi tiết. |
| ↳↳ `dimensions` | object | Dữ liệu của tất cả các chiều được yêu cầu. |
| ↳↳↳ `advertiser_id` | string | Trả về khi `dimensions` có `advertiser_id`. ID tài khoản quảng cáo. |
| ↳↳↳ `campaign_id` | string | Trả về khi `dimensions` có `campaign_id`. ID chiến dịch. |
| ↳↳↳ `adgroup_id` | string | Trả về khi `dimensions` có `adgroup_id`. ID nhóm quảng cáo. |
| ↳↳↳ `ad_id` | string | Trả về khi `dimensions` có `ad_id`. ID quảng cáo. Dữ liệu nhận được gồm: cấp ad cho Manual Ads, cấp ad cho Smart+ Campaigns, và cấp **nội dung sáng tạo (creative)** cho Upgraded Smart+ Ads. |
| ↳↳↳ `ad_id_v2` | string | Trả về khi `dimensions` có `ad_id_v2`. ID quảng cáo v2. Dữ liệu nhận được gồm: cấp ad cho Manual Ads, cấp ad cho Smart+ Campaigns, và cấp **quảng cáo (ad)** cho Upgraded Smart+ Ads. |
| ↳↳↳ `stat_time_day` | string | Trả về khi `dimensions` có `stat_time_day`. Thời gian báo cáo (ngày), định dạng `YYYY-MM-DD 00:00:00`. |
| ↳↳↳ `stat_time_hour` | string | Trả về khi `dimensions` có `stat_time_hour`. Thời gian báo cáo (giờ), định dạng `YYYY-MM-DD HH:00:00`. |
| ↳↳↳ `ac` | string | Trả về khi `dimensions` có `ac`. Loại kết nối mạng của đối tượng. Xem [Enumeration - Connection Type](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳↳↳ `age` | string | Trả về khi `dimensions` có `age`. Nhóm tuổi của đối tượng. Xem [Enumeration - Age Group](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳↳↳ `country_code` | string | Trả về khi `dimensions` có `country_code`. Mã quốc gia hoặc khu vực của đối tượng. Xem [Appendix - Location code](../15-appendix/phu-luc-p1.md#doc-1737585867307010). |
| ↳↳↳ `interest_category` | string | Trả về khi `dimensions` có `interest_category`. Danh mục sở thích cấp 1 cũ *(sắp ngừng hỗ trợ)*. |
| ↳↳↳ `interest_category_v2` | string | Trả về khi `dimensions` có `interest_category`. Danh mục sở thích cấp 1 mới. Xem [/tool/interest_category/](70-tools-p1.md#doc-1737174348712961). |
| ↳↳↳ `gender` | string | Trả về khi `dimensions` có `gender`. Giới tính nhắm mục tiêu: `FEMALE`, `MALE`, `NONE`. |
| ↳↳↳ `language` | string | Trả về khi `dimensions` có `language`. Ngôn ngữ nhắm mục tiêu. Xem [Enumeration - Languages](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳↳↳ `placement` | string | Trả về khi `dimensions` có `placement`. Vị trí hiển thị quảng cáo. Xem [Enumeration - Placement](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳↳↳ `platform` | string | Trả về khi `dimensions` có `platform`. Hệ điều hành nhắm mục tiêu. Xem [Enumeration - Operating System](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳↳↳ `contextual_tag` | string | Trả về khi `dimensions` có `contextual_tag`. Thẻ ngữ cảnh (contextual tag). |
| ↳↳ `metrics` | object | Dữ liệu của tất cả các chỉ số được yêu cầu. |
| ↳↳↳ `campaign_name` | string | Tên chiến dịch đấu thầu / Tên nhóm quảng cáo đặt trước. |
| ↳↳↳ `spend` | string | Tổng số tiền đã chi tiêu. |
| ↳↳↳ `impressions` | string | Số lượt hiển thị. |
| ↳↳↳ `reach` | string | Số lượng người dùng tiếp cận được. |
| ↳↳↳ `advertiser_id` | string | Trả về khi chỉ định `advertiser_ids`. ID nhà quảng cáo. |
| ↳↳↳ `timezone` | string | Trả về khi chỉ định `advertiser_ids`. Múi giờ của tài khoản quảng cáo. |
| ↳↳↳ `currency` | string | Trả về khi chỉ định `advertiser_ids`. Đơn vị tiền tệ của tài khoản quảng cáo. |
| ↳↳↳ `campaign_automation_type` | string | Loại tự động hóa của chiến dịch: `MANUAL`, `SMART_PLUS`, `UPGRADED_SMART_PLUS`, `UPGRADED_SMART_PLUS_CREATIVE`. Xem [Upgraded Smart+ Campaign](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1853452461203458). |
| ↳↳↳ `ad_id_v2` | string | ID quảng cáo v2 trả về khi `metrics` có `ad_id_v2`. |
| ↳↳↳ `ad_text_list` | string[] | Danh sách văn bản quảng cáo. Trả về khi `dimensions` có `ad_id_v2`, `metrics` có `ad_text` và `report_type` là `BASIC`, `AUDIENCE` hoặc `CATALOG`. |
| ↳↳↳ `call_to_action_list` | string[] | Danh sách nút kêu gọi hành động (CTA). Trả về khi `dimensions` có `ad_id_v2`, `metrics` có `call_to_action`. |
| ↳↳↳ `ad_profile_image_list` | string[] | Danh sách ảnh đại diện cấp quảng cáo. Trả về khi `dimensions` có `ad_id_v2`, `metrics` có `ad_profile_image`. |
| ↳↳↳ `ad_url_list` | string[] | Danh sách URL cấp quảng cáo. Trả về khi `dimensions` có `ad_id_v2`, `metrics` có `ad_url`. |
| ↳↳↳ `image_mode_list` | string[] | Danh sách định dạng hình ảnh/video. Trả về khi `dimensions` có `ad_id_v2`, `metrics` có `image_mode`. |
| ↳↳↳ `image_info_list` | string[] | Danh sách hình ảnh. Trả về khi `dimensions` có `ad_id_v2`, `metrics` có `image_info`. |
| ↳↳↳ `ad_display_name_list` | string[] | Danh sách tên hiển thị quảng cáo. Trả về khi `dimensions` có `ad_id_v2`, `metrics` có `ad_display_name`. |
| ↳↳↳ `identity_type_list` | string[] | Danh sách loại danh tính. Trả về khi `dimensions` có `ad_id_v2`, `metrics` có `identity_type`. |
| ↳↳↳ `profile_image_list` | string[] | Danh sách ảnh đại diện. Trả về khi `dimensions` có `ad_id_v2`, `metrics` có `profile_image`. |
| ↳ `page_info` | object | Thông tin phân trang. |
| ↳↳ `page` | number | Số trang hiện tại. |
| ↳↳ `page_size` | number | Số lượng bản ghi trên một trang. |
| ↳↳ `total_number` | number | Tổng số bản ghi kết quả. |
| ↳↳ `total_page` | number | Tổng số trang kết quả. |

### Ví dụ

#### curl (Lấy báo cáo cơ bản theo chiến dịch)
```bash
curl --location -G 'https://business-api.tiktok.com/open_api/v1.3/report/integrated/get/' \
  --header 'Access-Token: act.example12345abcdef' \
  --data-urlencode 'advertiser_id=7123456789012345678' \
  --data-urlencode 'service_type=AUCTION' \
  --data-urlencode 'report_type=BASIC' \
  --data-urlencode 'data_level=AUCTION_CAMPAIGN' \
  --data-urlencode 'dimensions=["campaign_id","stat_time_day"]' \
  --data-urlencode 'metrics=["campaign_name","spend","impressions","clicks","conversion","cost_per_conversion"]' \
  --data-urlencode 'start_date=2025-02-01' \
  --data-urlencode 'end_date=2025-02-15' \
  --data-urlencode 'page=1' \
  --data-urlencode 'page_size=100'
```

#### curl (Lọc theo quảng cáo Upgraded Smart+ bằng ad_ids_v2)
```bash
curl --location -G 'https://business-api.tiktok.com/open_api/v1.3/report/integrated/get/' \
  --header 'Access-Token: act.example12345abcdef' \
  --data-urlencode 'advertiser_id=7123456789012345678' \
  --data-urlencode 'service_type=AUCTION' \
  --data-urlencode 'report_type=BASIC' \
  --data-urlencode 'data_level=AUCTION_AD' \
  --data-urlencode 'dimensions=["ad_id_v2"]' \
  --data-urlencode 'metrics=["spend","ad_id_v2"]' \
  --data-urlencode 'filtering=[{"field_name":"ad_ids_v2","filter_type":"IN","filter_value":"[\"1723456789012345\"]"}]' \
  --data-urlencode 'start_date=2025-07-01' \
  --data-urlencode 'end_date=2025-07-30' \
  --data-urlencode 'page=1' \
  --data-urlencode 'page_size=100'
```

#### Python (Chuẩn chỉnh lấy báo cáo và xử lý phân trang)
```python
import json
import requests

ACCESS_TOKEN = "act.example12345abcdef"
ADVERTISER_ID = "7123456789012345678"

url = "https://business-api.tiktok.com/open_api/v1.3/report/integrated/get/"
headers = {
    "Access-Token": ACCESS_TOKEN
}

# Lưu ý: Các tham số array/object cần serialize bằng json.dumps()
params = {
    "advertiser_id": ADVERTISER_ID,
    "service_type": "AUCTION",
    "report_type": "BASIC",
    "data_level": "AUCTION_CAMPAIGN",
    "dimensions": json.dumps(["campaign_id", "stat_time_day"]),
    "metrics": json.dumps(["campaign_name", "spend", "impressions", "clicks", "reach"]),
    "start_date": "2025-02-01",
    "end_date": "2025-02-10",
    "page": 1,
    "page_size": 100
}

response = requests.get(url, headers=headers, params=params)
data = response.json()

if data.get("code") == 0:
    for row in data["data"].get("list", []):
        dims = row["dimensions"]
        mets = row["metrics"]
        print(f"[{dims.get('stat_time_day')}] Campaign {dims.get('campaign_id')} ({mets.get('campaign_name')}): Spend={mets.get('spend')}, Impressions={mets.get('impressions')}")
else:
    print(f"Error {data.get('code')}: {data.get('message')}")
```

#### Phản hồi thành công
```json
{
    "code": 0,
    "message": "OK",
    "request_id": "202512031200000102452431071406591A",
    "data": {
        "page_info": {
            "page": 1,
            "page_size": 2,
            "total_page": 1,
            "total_number": 2
        },
        "list": [
            {
                "dimensions": {
                    "ad_id_v2": "1723456789012345",
                    "stat_time_day": "2025-12-03 00:00:00"
                },
                "metrics": {
                    "ad_id_v2": "1723456789012345",
                    "ad_name": "Summer Promo Ad 1",
                    "impressions": "1079",
                    "spend": "14.68",
                    "campaign_automation_type": "UPGRADED_SMART_PLUS"
                }
            },
            {
                "dimensions": {
                    "ad_id_v2": "1723456789012346",
                    "stat_time_day": "2025-12-03 00:00:00"
                },
                "metrics": {
                    "ad_id_v2": "1723456789012346",
                    "ad_name": "Summer Promo Ad 2",
                    "impressions": "52",
                    "spend": "0.70",
                    "campaign_automation_type": "UPGRADED_SMART_PLUS"
                }
            }
        ]
    }
}
```


---

## Tạo tác vụ báo cáo bất đồng bộ (`Create an asynchronous report task`)
<a id="doc-1740302766489602"></a>
<!-- doc_id: 1740302766489602 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/report/task/create/`

**Mục đích**: Tạo một tác vụ báo cáo bất đồng bộ (asynchronous report task). Chế độ bất đồng bộ phù hợp cho các tập dữ liệu lớn không bị giới hạn 20.000 bản ghi như chế độ đồng bộ.

Xem thêm tại [Run an asynchronous report](../09-marketing-api/bao-cao-p1.md#doc-1738864800380930) để tìm hiểu cách thức vận hành báo cáo bất đồng bộ.

> [!NOTE]
> Bạn dùng endpoint khác nhau để tạo báo cáo chuẩn (đồng bộ - GET) và báo cáo bất đồng bộ (POST). Để biết các chiều dữ liệu, chỉ số và trường hợp sử dụng được hỗ trợ cho từng loại báo cáo, xem [Report types](../09-marketing-api/bao-cao-p1.md#doc-1738864835805186).

### Lưu ý quan trọng khi dùng báo cáo bất đồng bộ

| Mục | Chi tiết |
|---|---|
| `Rate limit` (Giới hạn tần suất) | Do giới hạn tài nguyên tính toán, giới hạn tốc độ gọi cho mỗi ứng dụng (app) là **1 QPS**. Vui lòng không tạo số lượng lớn tác vụ báo cáo bất đồng bộ trong thời gian ngắn.<br>Ngoài ra, người dùng gắn với access token (`Access-Token`) có một giới hạn riêng là tối đa **500 tác vụ tạo báo cáo bất đồng bộ** cho mỗi tài khoản quảng cáo mỗi giờ. |
| `Supported report types` (Loại báo cáo hỗ trợ) | Báo cáo nội dung tương tác (Playable ads reports) **không** được hỗ trợ trong báo cáo bất đồng bộ. |
| `Query time range` (Khoảng thời gian truy vấn) | Báo cáo bất đồng bộ không có giới hạn về khoảng thời gian bắt đầu và kết thúc (`start_date`, `end_date`). |
| `Filtering` (Bộ lọc) | • Báo cáo bất đồng bộ chỉ hỗ trợ lọc theo `campaign_ids`, `adgroup_ids`, `ad_ids` hoặc `country_code`. Bạn có thể lọc tối đa 20.000 ID.<br>• Nếu muốn dùng `country_code` làm bộ lọc nhóm, vui lòng chỉ định `country_code` trong trường `dimensions` của yêu cầu. Lưu ý `country_code` hoạt động với báo cáo cơ bản (đồng bộ và bất đồng bộ), báo cáo đối tượng (đồng bộ và bất đồng bộ), và báo cáo playable ad (chỉ đồng bộ). |
| `Compatibility between metrics and dimensions` (Tính tương thích giữa chỉ số và chiều dữ liệu) | • Truy vấn các chỉ số người dùng duy nhất (UV metrics) kết hợp với các chiều đối tượng (audience dimensions) **không** được hỗ trợ trong báo cáo bất đồng bộ. Vui lòng truy vấn các chỉ số UV mà không có chiều đối tượng hoặc truy vấn các chiều đối tượng mà không có chỉ số UV.<br>• Các chiều đối tượng gồm: `"gender"`, `"age"`, `"country_code"`, `"ac"`, `"language"`, `"platform"`, `"interest_category"`, `"placement"`, `"contextual_tag"`.<br>• Các chỉ số UV gồm: `"average_video_play_per_user"`, `"frequency"`, `"cost_per_1000_reached"`, `"real_time_result"`, `"real_time_result_rate"`, `"real_time_cost_per_result"`, `"result"`, `"result_rate"`, `"cost_per_result"`, `"reach"`, `"live_play_count"`.<br>• Các tổ hợp chiều và chỉ số hỗ trợ có thể khác nhau giữa báo cáo đồng bộ và bất đồng bộ. Do đó một tổ hợp hợp lệ ở báo cáo đồng bộ có thể không được hỗ trợ ở báo cáo bất đồng bộ. |
| `CHUNK mode` (Chế độ CHUNK) | Chế độ `CHUNK` chỉ hỗ trợ trong báo cáo cơ bản đồng bộ (`sync basic reports`), không hỗ trợ cho báo cáo bất đồng bộ. |
| `Pagination` (Phân trang) | Báo cáo bất đồng bộ xuất toàn bộ dữ liệu ra file nên **không** hỗ trợ phân trang (`page`, `page_size`). |
| `Validity period` (Thời hạn hiệu lực) | Một tác vụ báo cáo bất đồng bộ có giá trị hiệu lực trong **30 ngày**. Sau 30 ngày bạn không thể truy vấn trạng thái hoặc tải kết quả của tác vụ đó. |
| `Data` (Dữ liệu) | Dữ liệu cho báo cáo bất đồng bộ được làm mới một lần sau mỗi vài giờ. Dữ liệu của ngày hiện tại có thể chưa hoàn toàn chính xác. |
| `Known issue` (Vấn đề đã biết) | Hiện tại, báo cáo bất đồng bộ trả về chiều `country_code` (ví dụ `US`) dưới dạng tên quốc gia `country_name` (ví dụ `United States`). Đây là lỗi đã biết và sẽ được khắc phục trong phiên bản tiếp theo. |

### Header
| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Có | Mã truy cập đã được ủy quyền. Xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| `Content-Type` | string | Có | Định dạng nội dung yêu cầu: `application/json`. |

### Tham số (POST: JSON body)
| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | Điều kiện | Phải truyền một trong hai trường `advertiser_id` hoặc `advertiser_ids`. Nếu truyền cả hai, `advertiser_id` sẽ bị bỏ qua. ID tài khoản quảng cáo. |
| `advertiser_ids` | string[] | Điều kiện | Danh sách các ID tài khoản quảng cáo (tối đa 5 ID).<br>> [!NOTE]<br>> • Chỉ hợp lệ khi `report_type` là `BASIC` hoặc `AUDIENCE`.<br>> • Các tài khoản trong `advertiser_ids` phải thuộc cùng một người dùng TikTok for Business. Dùng [/oauth2/advertiser/get/](03-ad-accounts.md#doc-1738455508553729) để lấy danh sách.<br>> • Dữ liệu được lấy theo múi giờ riêng của từng tài khoản.<br>> • Khi truyền nhiều ID, bạn có thể chỉ định tối đa 2 chiều ID (`advertiser_id` + một chiều ID khác) trong `dimensions`. Khuyến nghị thêm `currency` vào `metrics` vì các tài khoản có thể dùng đơn vị tiền tệ khác nhau. |
| `service_type` | string | Không | Loại dịch vụ quảng cáo.<br>Giá trị enum:<br>• `AUCTION`: Quảng cáo đấu thầu hoặc cả đấu thầu và đặt trước. Mặc định: `AUCTION`.<br>• `RESERVATION` *(deprecated)*: Quảng cáo đặt trước.<br>> [!NOTE]<br>> Để lấy báo cáo TopView, sử dụng báo cáo `BASIC` hoặc `AUDIENCE` và lọc theo `buying_type` = `RESERVATION_TOP_VIEW`. |
| `report_type` | string | Có | Loại báo cáo. Giá trị enum:<br>• `BASIC`: Báo cáo cơ bản.<br>• `AUDIENCE`: Báo cáo đối tượng.<br>• `PLAYABLE_MATERIAL`: Báo cáo playable ad (chú ý: bất đồng bộ không hỗ trợ loại này).<br>• `CATALOG`: Báo cáo danh mục sản phẩm / DSA.<br>Khi `service_type` là `AUCTION`, các loại `BASIC`, `AUDIENCE`, `CATALOG` đều được hỗ trợ. |
| `data_level` | string | Điều kiện | Cấp độ dữ liệu cần truy vấn. Bắt buộc khi `report_type` là `BASIC`, `AUDIENCE` hoặc `CATALOG`.<br>Giá trị enum:<br>• `AUCTION_AD`: Cấp quảng cáo.<br>• `AUCTION_ADGROUP`: Cấp nhóm quảng cáo.<br>• `AUCTION_CAMPAIGN`: Cấp chiến dịch.<br>• `AUCTION_ADVERTISER`: Cấp tài khoản nhà quảng cáo.<br>• `RESERVATION_AD` *(deprecated)*: Cấp quảng cáo đặt trước.<br>• `RESERVATION_ADGROUP` *(deprecated)*: Cấp nhóm quảng cáo đặt trước.<br>• `RESERVATION_CAMPAIGN` *(deprecated)*: Cấp chiến dịch đặt trước.<br>• `RESERVATION_ADVERTISER` *(deprecated)*: Cấp tài khoản đặt trước. |
| `dimensions` | string[] | Có | Điều kiện nhóm dữ liệu, ví dụ: `["campaign_id", "stat_time_day"]`.<br>• Chiều hỗ trợ trong [Báo cáo cơ bản](../09-marketing-api/bao-cao-p1.md#doc-1751443956638721)<br>• Chiều hỗ trợ trong [Báo cáo đối tượng](../09-marketing-api/bao-cao-p3.md#doc-1751454103714818)<br>• Chiều hỗ trợ trong [Báo cáo DSA](../09-marketing-api/bao-cao-p3.md#doc-1751617879104514)<br>• Chiều hỗ trợ trong [Báo cáo Business Center](../09-marketing-api/bao-cao-p3.md#doc-1775747465089026)<br>> [!NOTE]<br>> • Nếu `dimensions` chỉ định nhiều hơn các trường ID mà không có dữ liệu quảng cáo phát sinh, mảng rỗng sẽ được trả về.<br>> • Các tổ hợp chiều và chỉ số hỗ trợ có thể khác nhau giữa đồng bộ và bất đồng bộ.<br>> • Chiều `ad_id_v2` khả dụng với `BASIC`, `AUDIENCE`, `CATALOG`. Không dùng chung với `ad_id` hoặc filter `ad_ids`. |
| `metrics` | string[] | Không | Danh sách chỉ số cần truy vấn. Xem chi tiết tại [Report types](../09-marketing-api/bao-cao-p1.md#doc-1738864835805186). Mặc định: `["spend", "impressions"]`. |
| `start_date` | string | Điều kiện | Bắt buộc khi `query_lifetime` là `false` hoặc không được truyền. Ngày bắt đầu truy vấn (khoảng đóng), định dạng `YYYY-MM-DD` theo múi giờ tài khoản quảng cáo. Báo cáo bất đồng bộ không bị giới hạn khoảng thời gian. |
| `end_date` | string | Điều kiện | Bắt buộc khi `query_lifetime` là `false` hoặc không được truyền. Ngày kết thúc truy vấn (khoảng đóng), định dạng `YYYY-MM-DD` theo múi giờ tài khoản quảng cáo. |
| `query_lifetime` | boolean | Không | Có truy vấn số liệu toàn thời gian hay không. Mặc định: `false`. Nếu là `true`, `start_date` và `end_date` bị bỏ qua.<br>> [!NOTE]<br>> Không hỗ trợ phân tích theo thời gian, đối tượng hoặc `country_code` khi truy vấn số liệu lifetime. Báo cáo DSA không hỗ trợ lifetime. |
| `order_field` | string | Không | Trường sắp xếp. Tất cả các chỉ số (ngoại trừ thuộc tính) đều hỗ trợ. Mặc định không sắp xếp. |
| `order_type` | string | Không | Thứ tự sắp xếp: `ASC`, `DESC`. Mặc định: `DESC`. |
| `enable_report_title_translation` | boolean | Không | Có bật dịch hàng tiêu đề của báo cáo bất đồng bộ (bao gồm tên chiều dữ liệu và tên chỉ số) hay không.<br>Ví dụ: nếu đặt `false`, tiêu đề sẽ giữ nguyên tên mã như `ad_id` thay vì tiêu đề đã dịch như `AD ID`. Mặc định: `true`.<br>> [!TIP]<br>> Khuyến nghị đặt `enable_report_title_translation` thành `false` trong mã code của bạn để giữ nguyên mã trường kỹ thuật, tránh bị ảnh hưởng khi TikTok định kỳ cập nhật văn bản hiển thị tiêu đề. |
| `output_format` | string | Không | Định dạng file xuất. Giá trị enum:<br>• `CSV_STRING`: Nội dung CSV dạng chuỗi.<br>• `CSV_DOWNLOAD`: File CSV tải xuống.<br>• `XLSX_DOWNLOAD`: File Excel XLSX tải xuống.<br>Mặc định: `CSV_STRING`. |
| `file_name` | string | Không | Tên file tùy chỉnh khi `output_format` là `CSV_DOWNLOAD` hoặc `XLSX_DOWNLOAD`. Độ dài tối đa: 255 ký tự. Không chứa các ký tự đặc biệt: `['/', '\t', '\b', '@', '#', '$', '%', '^', '&', '*', '(', ')', '[', ']']`. |
| `filtering` | object[] | Không | Điều kiện lọc. Với báo cáo bất đồng bộ cho basic, audience và DSA, các trường lọc duy nhất được hỗ trợ là `campaign_ids`, `adgroup_ids`, và `ad_ids`. |
| ↳ `field_name` | string | Điều kiện | Tên trường lọc (ví dụ `campaign_ids`, `adgroup_ids`, `ad_ids`, `ad_ids_v2`). Với `ad_ids_v2`, `filter_type` phải là `IN`, `data_level` phải là `AUCTION_AD`, và `dimensions` phải có `ad_id_v2`. Tối đa 100 ID. |
| ↳ `filter_type` | string | Điều kiện | Loại lọc. Giá trị enum:<br>• `IN`: Khớp chính xác (chuỗi JSON array).<br>• `MATCH`: Khớp mờ (`LIKE`).<br>• `GREATER_EQUAL`: Lớn hơn hoặc bằng.<br>• `GREATER_THAN`: Lớn hơn.<br>• `LOWER_EQUAL`: Nhỏ hơn hoặc bằng.<br>• `LOWER_THAN`: Nhỏ hơn.<br>• `BETWEEN`: Trong khoảng (chuỗi JSON array chứa 2 giá trị).<br>Khi `field_name` là `ad_id_v2`, đặt `filter_type` là `IN`. |
| ↳ `filter_value` | string | Điều kiện | Giá trị lọc. Khi `filter_type` là `IN`, phải là chuỗi JSON array hợp lệ. |

### Phản hồi
| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Thành công trả về `0`. Chi tiết xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | ID duy nhất của yêu cầu. |
| `data` | object | Dữ liệu trả về. |
| ↳ `task_id` | string | ID của tác vụ báo cáo bất đồng bộ được tạo. Sử dụng ID này để kiểm tra trạng thái và tải kết quả. |

### Ví dụ

#### curl
```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/report/task/create/' \
--header 'Access-Token: act.example12345abcdef' \
--header 'Content-Type: application/json' \
--data-raw '{
    "advertiser_id": "7123456789012345678",
    "service_type": "AUCTION",
    "report_type": "BASIC",
    "data_level": "AUCTION_AD",
    "dimensions": ["ad_id", "stat_time_day"],
    "metrics": ["spend", "impressions", "clicks", "conversion"],
    "start_date": "2025-01-01",
    "end_date": "2025-01-31",
    "output_format": "CSV_DOWNLOAD",
    "file_name": "monthly_report_jan_2025",
    "enable_report_title_translation": false,
    "filtering": [
        {
            "field_name": "adgroup_ids",
            "filter_type": "IN",
            "filter_value": "[\"1723456789012345\"]"
        }
    ]
}'
```

#### Python
```python
import json
import requests

ACCESS_TOKEN = "act.example12345abcdef"
ADVERTISER_ID = "7123456789012345678"

url = "https://business-api.tiktok.com/open_api/v1.3/report/task/create/"
headers = {
    "Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}
payload = {
    "advertiser_id": ADVERTISER_ID,
    "service_type": "AUCTION",
    "report_type": "BASIC",
    "data_level": "AUCTION_AD",
    "dimensions": ["ad_id", "stat_time_day"],
    "metrics": ["spend", "impressions", "clicks"],
    "start_date": "2025-01-01",
    "end_date": "2025-01-31",
    "output_format": "CSV_DOWNLOAD",
    "file_name": "ad_report_jan2025",
    "enable_report_title_translation": False
}

response = requests.post(url, headers=headers, json=payload)
data = response.json()
print("Task creation result:", data)
if data.get("code") == 0:
    task_id = data["data"]["task_id"]
    print(f"Created task successfully. Task ID: {task_id}")
```

#### Phản hồi thành công
```json
{
    "code": 0,
    "message": "OK",
    "request_id": "202502010930000102452431071406592B",
    "data": {
        "task_id": "1723456789098765"
    }
}
```

---

## Kiểm tra trạng thái tác vụ báo cáo bất đồng bộ (`Get the status of an async report task`)
<a id="doc-1740302781443073"></a>
<!-- doc_id: 1740302781443073 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/report/task/check/`

**Mục đích**: Kiểm tra tiến trình và trạng thái xử lý của một tác vụ báo cáo bất đồng bộ đã tạo trước đó.

### Header
| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Có | Mã truy cập đã được ủy quyền. Phải sử dụng cùng một access token đã dùng khi gọi [/report/task/create/](58-reporting.md#doc-1740302766489602). |

### Tham số (GET: query string)
| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | Có | ID tài khoản quảng cáo.<br>> [!NOTE]<br>> Nếu bạn đã dùng `advertiser_ids` khi tạo tác vụ qua [/report/task/create/](58-reporting.md#doc-1740302766489602), bạn cần điền trường này bằng một trong các ID đã chỉ định trong danh sách đó. |
| `task_id` | string | Có | ID của tác vụ báo cáo bất đồng bộ, nhận được từ phản hồi của endpoint [/report/task/create/](58-reporting.md#doc-1740302766489602). |

### Phản hồi
| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Thành công trả về `0`. Chi tiết xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | ID duy nhất của yêu cầu. |
| `data` | object | Dữ liệu trả về. |
| ↳ `status` | string | Trạng thái hiện tại của tác vụ. Giá trị enum:<br>• `QUEUING`: Đang xếp hàng chờ xử lý.<br>• `PROCESSING`: Đang trong tiến trình xử lý.<br>• `SUCCESS`: Xử lý thành công. Bạn có thể tiến hành tải kết quả qua [/report/task/download/](58-reporting.md#doc-1740302808815618).<br>• `FAILED`: Thất bại.<br>• `CANCELED`: Đã bị hủy bỏ.<br>Nếu bạn muốn hủy một tác vụ đang ở trạng thái `QUEUING` hoặc `PROCESSING`, hãy sử dụng [/report/task/cancel/](58-reporting.md#doc-1803615367145537). |
| ↳ `message` | string | Lý do thất bại. Trường này chỉ được trả về khi `status` là `FAILED`. |

### Ví dụ

#### curl
```bash
curl --location -G 'https://business-api.tiktok.com/open_api/v1.3/report/task/check/' \
  --header 'Access-Token: act.example12345abcdef' \
  --data-urlencode 'advertiser_id=7123456789012345678' \
  --data-urlencode 'task_id=1723456789098765'
```

#### Python
```python
import requests

ACCESS_TOKEN = "act.example12345abcdef"
ADVERTISER_ID = "7123456789012345678"
TASK_ID = "1723456789098765"

url = "https://business-api.tiktok.com/open_api/v1.3/report/task/check/"
headers = {
    "Access-Token": ACCESS_TOKEN
}
params = {
    "advertiser_id": ADVERTISER_ID,
    "task_id": TASK_ID
}

response = requests.get(url, headers=headers, params=params)
data = response.json()
print("Task status check:", data)

status = data.get("data", {}).get("status")
if status == "SUCCESS":
    print("Report is ready for download!")
elif status in ("QUEUING", "PROCESSING"):
    print(f"Report is still in progress: {status}")
elif status == "FAILED":
    print(f"Report generation failed: {data.get('data', {}).get('message')}")
```

#### Phản hồi thành công
```json
{
    "code": 0,
    "message": "OK",
    "request_id": "2021022606090301011517615608212B1C",
    "data": {
        "status": "SUCCESS",
        "message": ""
    }
}
```


---

## Tải kết quả báo cáo bất đồng bộ (`Download the output of an async report task`)
<a id="doc-1740302808815618"></a>
<!-- doc_id: 1740302808815618 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/report/task/download/`

**Mục đích**: Tải xuống nội dung hoặc nhận đường dẫn tải file báo cáo sau khi tác vụ báo cáo bất đồng bộ đã hoàn thành thành công (`status` = `SUCCESS`).

### Header
| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Có | Mã truy cập đã được ủy quyền. Phải sử dụng cùng một access token đã dùng khi gọi [Create an asynchronous report task](58-reporting.md#doc-1740302766489602). |

### Tham số (GET: query string)
| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | Có | ID tài khoản quảng cáo.<br>> [!NOTE]<br>> Nếu bạn đã dùng `advertiser_ids` khi gọi [/report/task/create/](58-reporting.md#doc-1740302766489602), bạn cần điền trường này bằng một trong các ID đã chỉ định trong danh sách đó. |
| `task_id` | string | Có | ID của tác vụ báo cáo bất đồng bộ. |

### Phản hồi
Phản hồi có thể ở dạng luồng file CSV (file stream) hoặc định dạng JSON:
> [!NOTE]
> Nếu `output_format` được thiết lập là `CSV_DOWNLOAD` hoặc `XLSX_DOWNLOAD` khi gọi [/report/task/create/](58-reporting.md#doc-1740302766489602), phản hồi sẽ ở định dạng JSON chứa URL tải file. Nếu `output_format` là `CSV_STRING`, phản hồi trả về trực tiếp luồng văn bản CSV.

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Thành công trả về `0`. Chi tiết xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | ID định danh duy nhất của yêu cầu (log ID). |
| `data` | object | Dữ liệu trả về khi tải dưới dạng JSON. |
| ↳ `download_url` | string | Đường dẫn URL để tải file báo cáo, có hiệu lực trong vòng **1 giờ**. Bạn có thể gọi lại endpoint [/report/task/download/](58-reporting.md#doc-1740302808815618) để lấy URL mới nếu URL cũ hết hạn. |
| ↳ `file_name` | string | Tên của file tải xuống. |
| ↳ `output_format` | string | Định dạng xuất file. Giá trị enum: `CSV_DOWNLOAD`, `XLSX_DOWNLOAD`. |

### Ví dụ

#### curl (Lấy URL tải file JSON)
```bash
curl --location -G 'https://business-api.tiktok.com/open_api/v1.3/report/task/download/' \
  --header 'Access-Token: act.example12345abcdef' \
  --data-urlencode 'advertiser_id=7123456789012345678' \
  --data-urlencode 'task_id=1723456789098765'
```

#### curl (Tải trực tiếp file stream CSV)
```bash
curl --location -G 'https://business-api.tiktok.com/open_api/v1.3/report/task/download/' \
  --header 'Access-Token: act.example12345abcdef' \
  --data-urlencode 'advertiser_id=7123456789012345678' \
  --data-urlencode 'task_id=1723456789098765' \
  --output report_output.csv
```

#### Python
```python
import requests

ACCESS_TOKEN = "act.example12345abcdef"
ADVERTISER_ID = "7123456789012345678"
TASK_ID = "1723456789098765"

url = "https://business-api.tiktok.com/open_api/v1.3/report/task/download/"
headers = {
    "Access-Token": ACCESS_TOKEN
}
params = {
    "advertiser_id": ADVERTISER_ID,
    "task_id": TASK_ID
}

response = requests.get(url, headers=headers, params=params)

# Kiểm tra nếu phản hồi là JSON (khi dùng CSV_DOWNLOAD hoặc XLSX_DOWNLOAD)
try:
    data = response.json()
    if data.get("code") == 0:
        download_url = data["data"]["download_url"]
        file_name = data["data"]["file_name"]
        print(f"Download URL (valid for 1 hour): {download_url}")
        # Tải file từ download_url về máy
        file_content = requests.get(download_url).content
        with open(file_name, "wb") as f:
            f.write(file_content)
        print(f"Saved file {file_name}")
    else:
        print(f"Error {data.get('code')}: {data.get('message')}")
except ValueError:
    # Phản hồi dạng file stream CSV trực tiếp (CSV_STRING)
    with open("report.csv", "wb") as f:
        f.write(response.content)
    print("Saved report.csv directly from stream.")
```

#### Phản hồi dạng JSON mẫu
```json
{
    "code": 0,
    "message": "OK",
    "request_id": "202207282320310102452431071406594F",
    "data": {
        "output_format": "XLSX_DOWNLOAD",
        "file_name": "monthly_report_jan_2025.xlsx",
        "download_url": "https://ads.tiktok.com/wsos_v2/statistics/object/wsos62e082e99504cb02?expire=1659054031&skipCookie=true&timeStamp=1659050431&sign=1ccc8bd4665a65a941b168652ccd392707798a1dcb9f1eec2229123aca5a0bff"
    }
}
```

#### Phản hồi dạng CSV Stream mẫu
```csv
Campaign ID,Campaign Name,Ad Group ID,Ad Group Name,Age,Gender,Cost,Impression,Click
482,Test Campaign 1,578,Test Ad Group 1,13-17,female,107.56,29056,280
482,Test Campaign 1,578,Test Ad Group 1,18-24,female,101.74,22992,203
482,Test Campaign 1,578,Test Ad Group 1,13-17,male,58.78,17063,126
482,Test Campaign 1,578,Test Ad Group 1,18-24,male,57.36,18467,115
622,Test Campaign 2,765,Test Ad Group 2,18-24,male,32.9,267635,1172
```

---

## Hủy tác vụ báo cáo bất đồng bộ (`Cancel an asynchronous report task`)
<a id="doc-1803615367145537"></a>
<!-- doc_id: 1803615367145537 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/report/task/cancel/`

**Mục đích**: Hủy một tác vụ báo cáo bất đồng bộ đang ở trạng thái xếp hàng chờ (`QUEUING`) hoặc đang xử lý (`PROCESSING`). Việc hủy các tác vụ bị cấu hình sai hoặc chạy quá lâu sẽ giúp giải phóng tài nguyên và cho phép các tác vụ khác trong hàng đợi tiến vào giai đoạn xử lý nhanh hơn.

### Header
| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Có | Mã truy cập đã được ủy quyền. Xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162).<br>> [!NOTE]<br>> Phải dùng cùng một access token đã dùng để tạo tác vụ báo cáo bất đồng bộ trước đó. |
| `Content-Type` | string | Có | Định dạng nội dung yêu cầu: `application/json`. |

### Tham số (POST: JSON body)
| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | Có | ID tài khoản quảng cáo.<br>> [!NOTE]<br>> Nếu bạn đã dùng `advertiser_ids` khi gọi [/report/task/create/](58-reporting.md#doc-1740302766489602), bạn cần điền trường này bằng một trong các ID đã chỉ định trong danh sách đó. |
| `task_id` | string | Có | ID của tác vụ báo cáo bất đồng bộ đang ở trạng thái `QUEUING` hoặc `PROCESSING`.<br>Để lấy task ID, trước tiên gọi [/report/task/create/](58-reporting.md#doc-1740302766489602). Sau đó dùng [/report/task/check/](58-reporting.md#doc-1740302781443073) để xác nhận trạng thái tác vụ trước khi gửi yêu cầu hủy. |

### Phản hồi
| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Thành công trả về `0`. Chi tiết xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | ID định danh duy nhất của yêu cầu (log ID). |
| `data` | object | Dữ liệu trả về. |
| ↳ `status` | string | Trạng thái của tác vụ. Giá trị enum: `CANCELED`. Nếu hủy thành công, giá trị trường này là `CANCELED`. Nếu hủy thất bại, hệ thống sẽ báo lỗi. |

### Ví dụ

#### curl
```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/report/task/cancel/' \
--header 'Access-Token: act.example12345abcdef' \
--header 'Content-Type: application/json' \
--data-raw '{
    "advertiser_id": "7123456789012345678",
    "task_id": "1723456789098765"
}'
```

#### Python
```python
import requests

ACCESS_TOKEN = "act.example12345abcdef"
ADVERTISER_ID = "7123456789012345678"
TASK_ID = "1723456789098765"

url = "https://business-api.tiktok.com/open_api/v1.3/report/task/cancel/"
headers = {
    "Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}
payload = {
    "advertiser_id": ADVERTISER_ID,
    "task_id": TASK_ID
}

response = requests.post(url, headers=headers, json=payload)
data = response.json()
print("Cancel response:", data)
if data.get("code") == 0:
    print(f"Task {TASK_ID} has been successfully canceled: status={data.get('data', {}).get('status')}")
else:
    print(f"Cancel failed: {data.get('message')}")
```

#### Phản hồi thành công
```json
{
    "code": 0,
    "message": "OK",
    "request_id": "202307151020300102452431071406599C",
    "data": {
        "status": "CANCELED"
    }
}
```
