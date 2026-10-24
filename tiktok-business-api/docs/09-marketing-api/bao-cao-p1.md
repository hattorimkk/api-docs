# Hướng dẫn Báo cáo (Reporting) — phần 1/4

Tài liệu này là phần đầu tiên trong bộ hướng dẫn toàn diện về hệ thống API Báo cáo (Reporting API) của TikTok for Business. Bạn có thể sử dụng Reporting API để trích xuất dữ liệu phân tích và hiệu suất quảng cáo cho cả quảng cáo đấu thầu (auction ads) và quảng cáo đặt trước (reservation ads) theo hai chế độ: **đồng bộ** (synchronous) hoặc **bất đồng bộ** (asynchronous).

Phần 1 bao gồm các chủ đề sau:
- [Tổng quan Báo cáo (Reporting)](bao-cao-p1.md#doc-1738864739862530)
- [Tổng quan hệ thống (Overview)](bao-cao-p1.md#doc-1751087777884161)
- [Mục lục hướng dẫn (Guides)](bao-cao-p1.md#doc-1751087792726017)
- [Báo cáo đồng bộ và bất đồng bộ (Synchronous and asynchronous reports)](bao-cao-p1.md#doc-1751088469160001)
- [Cách chạy báo cáo đồng bộ (Run a synchronous report)](bao-cao-p1.md#doc-1738864778664961)
- [Cách chạy báo cáo bất đồng bộ (Run an asynchronous report)](bao-cao-p1.md#doc-1738864800380930)
- [Các loại báo cáo (Report types)](bao-cao-p1.md#doc-1738864835805186)
- [Báo cáo cơ bản (Basic reports)](bao-cao-p1.md#doc-1738864915188737)
- [Các chiều dữ liệu được hỗ trợ (Supported dimensions)](bao-cao-p1.md#doc-1751443956638721)
- [Chỉ số hỗ trợ theo chiều dữ liệu trong báo cáo cơ bản (Supported metrics for a dimension in basic reports)](bao-cao-p1.md#doc-1759239462689793)
- [Chỉ số cửa sổ phân bổ 180 ngày cùng chiều minis_id (180-day attribution window metrics together with the dimension minis_id)](bao-cao-p1.md#doc-1866989577164801)

---

## Báo cáo (`Reporting`)
<a id="doc-1738864739862530"></a>
<!-- doc_id: 1738864739862530 -->

> Đường dẫn: Marketing API > Reporting

Bạn có thể sử dụng Reporting API để trích xuất báo cáo dữ liệu quảng cáo đấu thầu và quảng cáo đặt trước ở chế độ đồng bộ hoặc bất đồng bộ.
- Để xem tổng quan về Reporting API, xem [Tổng quan (Overview)](bao-cao-p1.md#doc-1751087777884161).
- Để tìm hiểu về báo cáo đồng bộ, bất đồng bộ và các loại báo cáo khác nhau, xem [Hướng dẫn (Guides)](bao-cao-p1.md#doc-1751087792726017):
  - [Synchronous and asynchronous reports](bao-cao-p1.md#doc-1751088469160001): Giới thiệu cách chạy báo cáo đồng bộ và bất đồng bộ.
  - [Report types](bao-cao-p1.md#doc-1738864835805186): Giới thiệu các **trường hợp sử dụng (use cases)** của báo cáo cơ bản (`BASIC`), báo cáo đối tượng (`AUDIENCE`), báo cáo nội dung tương tác (`PLAYABLE_MATERIAL`), báo cáo quảng cáo mua sắm động DSA (`CATALOG`), báo cáo Business Center (`BC`), báo cáo GMV Max, cùng danh sách chiều dữ liệu, chỉ số và bộ lọc tương ứng.
  - [Best practices](bao-cao-p4.md#doc-1738864817670145): Tổng hợp các thực tiễn tốt nhất để tránh hoặc giảm thiểu hiện tượng timeout trong các báo cáo đồng bộ.
  - [Data latency for reports](bao-cao-p4.md#doc-1738864894606337): Giới thiệu độ trễ dữ liệu dự kiến khi sử dụng Reporting API.
  - [FAQs](bao-cao-p4.md#doc-1738864850353154): Giải đáp các câu hỏi thường gặp về Reporting API.
- Để tra cứu các endpoint khả dụng khi chạy báo cáo, xem [API reference](bao-cao-p4.md#doc-1740649343188994).

---

## Tổng quan (`Overview`)
<a id="doc-1751087777884161"></a>
<!-- doc_id: 1751087777884161 -->

> Đường dẫn: Marketing API > Reporting > Overview

Bài viết này cung cấp cái nhìn tổng quan về hệ sinh thái Reporting API của TikTok.

### Chế độ đồng bộ và bất đồng bộ
Bạn có thể chạy báo cáo theo chế độ đồng bộ (synchronous mode) hoặc bất đồng bộ (asynchronous mode). Xem chi tiết tại [Synchronous and asynchronous reports](bao-cao-p1.md#doc-1751088469160001) để nắm rõ cách thức vận hành và lựa chọn chế độ phù hợp.

### Loại hình quảng cáo
Bạn có thể trích xuất báo cáo cho riêng dữ liệu quảng cáo đấu thầu (auction ads) hoặc kết hợp cả dữ liệu quảng cáo đấu thầu và quảng cáo đặt trước (reservation ads).

### Các loại báo cáo
TikTok cung cấp 6 loại báo cáo chuyên biệt:
1. Báo cáo cơ bản (Basic report)
2. Báo cáo đối tượng (Audience report)
3. Báo cáo nội dung tương tác (Playable ads report)
4. Báo cáo quảng cáo mua sắm động (Dynamic Showcase Ads - DSA report)
5. Báo cáo Business Center (Business Center report)
6. Báo cáo quảng cáo GMV Max (GMV max ads report)

Xem [Report types](bao-cao-p1.md#doc-1738864835805186) để tìm hiểu các trường hợp sử dụng cụ thể của từng loại.

### Cấp độ dữ liệu (Data level)
- Với **Báo cáo Business Center**, bạn không cần thiết lập thủ công loại dịch vụ (`service_type`) và cấp độ dữ liệu (`data_level`). Báo cáo Business Center hỗ trợ cả quảng cáo đấu thầu và đặt trước.
- Với **Báo cáo cơ bản, Báo cáo đối tượng, Báo cáo playable ad và Báo cáo DSA**, bạn có thể chạy báo cáo ở 4 cấp độ dữ liệu:
  - Cấp tài khoản quảng cáo (`AUCTION_ADVERTISER` / `RESERVATION_ADVERTISER`)
  - Cấp chiến dịch (`AUCTION_CAMPAIGN` / `RESERVATION_CAMPAIGN`)
  - Cấp nhóm quảng cáo (`AUCTION_ADGROUP` / `RESERVATION_ADGROUP`)
  - Cấp quảng cáo (`AUCTION_AD` / `RESERVATION_AD`)
- Với **Báo cáo quảng cáo GMV Max**, bạn có thể chạy ở cấp chiến dịch hoặc cấp tài khoản quảng cáo.

### Chiều dữ liệu, chỉ số và bộ lọc
Mỗi loại báo cáo hỗ trợ các chiều dữ liệu (`dimensions`), chỉ số (`metrics`) và bộ lọc (`filtering`) khác nhau. Xem các bài viết tương ứng dưới mục [Report types](bao-cao-p1.md#doc-1738864835805186) để tra cứu chi tiết.

### Độ trễ dữ liệu (Data latency)
Khi sử dụng Reporting API, các chỉ số khác nhau có độ trễ cập nhật khác nhau (ví dụ: chỉ số chi phí thời gian thực so với chỉ số chuyển đổi đối soát). Xem [Data latency for reports](bao-cao-p4.md#doc-1738864894606337) để nắm rõ thời gian dữ liệu sẵn sàng.

### So sánh Reporting API và Creative Reporting API
- Sử dụng **Reporting API** để truy vấn dữ liệu hiệu suất tổng hợp ở cấp chiến dịch, nhóm quảng cáo, quảng cáo hoặc tài khoản quảng cáo.
- Sử dụng **Creative Reporting API** để phân tích sâu hiệu suất ở cấp độ tài sản sáng tạo (creative asset level) như từng video, hình ảnh, văn bản quảng cáo. Chi tiết xem tại [FAQs - Creative insights](bao-cao-p4.md#doc-1738864850353154).

---

## Mục lục hướng dẫn (`Guides`)
<a id="doc-1751087792726017"></a>
<!-- doc_id: 1751087792726017 -->

> Đường dẫn: Marketing API > Reporting > Guides

Tài liệu hướng dẫn này sẽ dẫn dắt bạn qua các nội dung kỹ thuật cốt lõi:
- [Synchronous and asynchronous reports](bao-cao-p1.md#doc-1751088469160001): Phân biệt và hướng dẫn chạy báo cáo đồng bộ và bất đồng bộ.
- [Report types](bao-cao-p1.md#doc-1738864835805186): Giới thiệu các use case, chiều dữ liệu, chỉ số và bộ lọc cho 6 loại báo cáo.
- [Best practices](bao-cao-p4.md#doc-1738864817670145): Các thực tiễn tối ưu để giảm tải và hạn chế lỗi quá thời gian chờ (timeout).
- [Data latency for reports](bao-cao-p4.md#doc-1738864894606337): Mức độ trễ dữ liệu của từng nhóm chỉ số.
- [FAQs](bao-cao-p4.md#doc-1738864850353154): Các câu hỏi thường gặp về Reporting API.

---

## Báo cáo đồng bộ và bất đồng bộ (`Synchronous and asynchronous reports`)
<a id="doc-1751088469160001"></a>
<!-- doc_id: 1751088469160001 -->

> Đường dẫn: Marketing API > Reporting > Guides > Synchronous and asynchronous reports

Bạn có thể chạy báo cáo theo chế độ đồng bộ hoặc bất đồng bộ tùy theo nhu cầu và kích thước dữ liệu cần truy xuất:
- [Run a synchronous report](bao-cao-p1.md#doc-1738864778664961): Thích hợp khi cần dữ liệu tức thời cho dashboard, với tập dữ liệu nhỏ hơn 20.000 bản ghi.
- [Run an asynchronous report](bao-cao-p1.md#doc-1738864800380930): Thích hợp cho các báo cáo quy mô lớn, xuất file CSV/Excel dài hạn, không bị giới hạn 20.000 bản ghi.

---

## Chạy báo cáo đồng bộ (`Run a synchronous report`)
<a id="doc-1738864778664961"></a>
<!-- doc_id: 1738864778664961 -->

> Đường dẫn: Marketing API > Reporting > Guides > Synchronous and asynchronous reports > Run a synchronous report

Báo cáo đồng bộ trả về dữ liệu ngay lập tức trong phản hồi HTTP GET. Phương thức này lý tưởng cho việc hiển thị số liệu trực tiếp trên bảng điều khiển (dashboard) hoặc ứng dụng quản lý quảng cáo thời gian thực.

Sử dụng endpoint [/report/integrated/get/](../12-api-reference/58-reporting.md#doc-1740302848100353) để thực hiện báo cáo đồng bộ.

### Các tham số quan trọng khi chạy báo cáo đồng bộ
1. **Mã truy cập (`Access-Token`)**: Bắt buộc truyền trong header HTTP.
2. **ID tài khoản hoặc Business Center**:
   - Truyền `advertiser_id` hoặc danh sách `advertiser_ids` (tối đa 5 ID) cho các báo cáo cấp tài khoản quảng cáo.
   - Truyền `bc_id` cho báo cáo Business Center.
3. **Loại dịch vụ quảng cáo (`service_type`)**:
   - `AUCTION`: Quảng cáo đấu thầu (hoặc cả đấu thầu và đặt trước).
   - `RESERVATION` *(deprecated)*: Quảng cáo đặt trước.
4. **Loại báo cáo (`report_type`)**:
   - `BASIC`: Báo cáo cơ bản.
   - `AUDIENCE`: Báo cáo đối tượng.
   - `PLAYABLE_MATERIAL`: Báo cáo nội dung tương tác.
   - `CATALOG`: Báo cáo danh mục sản phẩm (DSA).
   - `BC`: Báo cáo Business Center.
   - `TT_SHOP`: Báo cáo TikTok Shop.
5. **Cấp độ dữ liệu (`data_level`)**: Bắt buộc khi `report_type` là `BASIC`, `AUDIENCE` hoặc `CATALOG` (`AUCTION_CAMPAIGN`, `AUCTION_ADGROUP`, `AUCTION_AD`, `AUCTION_ADVERTISER`).
6. **Khoảng thời gian (`start_date`, `end_date`)**: Định dạng `YYYY-MM-DD` theo múi giờ của tài khoản quảng cáo.
   - Khoảng cách tối đa là 365 ngày (nếu không có `stat_time_day`).
   - Khoảng cách tối đa là 30 ngày (nếu có `stat_time_day`).
7. **Chiều dữ liệu (`dimensions`)**: Bắt buộc. Xác định tiêu chí gom nhóm dữ liệu (ví dụ: `["campaign_id", "stat_time_day"]`).
8. **Chỉ số (`metrics`)**: Danh sách chỉ số muốn truy vấn (ví dụ: `["spend", "impressions", "clicks", "conversion"]`).
9. **Bộ lọc (`filtering`)**: Giới hạn phạm vi dữ liệu theo các trường cụ thể.
10. **Phân trang (`page`, `page_size`)**: Số trang (bắt đầu từ 1) và số bản ghi trên mỗi trang (tối đa 1.000).

> [!NOTE]
> Giới hạn 20.000 quảng cáo: Endpoint này cắt bớt và chỉ trả về tối đa 20.000 bản ghi quảng cáo sắp xếp theo thời gian tạo giảm dần. Nếu tài khoản có trên 20.000 quảng cáo, hãy dùng bộ lọc theo từng nhóm ID nhỏ hoặc chuyển sang sử dụng báo cáo bất đồng bộ.

---

## Chạy báo cáo bất đồng bộ (`Run an asynchronous report`)
<a id="doc-1738864800380930"></a>
<!-- doc_id: 1738864800380930 -->

> Đường dẫn: Marketing API > Reporting > Guides > Synchronous and asynchronous reports > Run an asynchronous report

Báo cáo bất đồng bộ được thiết kế để xử lý khối lượng dữ liệu khổng lồ mà không làm tắc nghẽn kết nối mạng hay gặp lỗi timeout. Báo cáo này không bị giới hạn 20.000 quảng cáo và hỗ trợ xuất dữ liệu ra file CSV hoặc Excel.

Quy trình chạy báo cáo bất đồng bộ gồm 3 bước chính:

1. **Bước 1: Tạo tác vụ báo cáo bất đồng bộ**
   - Gọi endpoint [/report/task/create/](../12-api-reference/58-reporting.md#doc-1740302766489602) bằng phương thức `POST`.
   - Cung cấp các tham số như `advertiser_id`, `report_type`, `data_level`, `dimensions`, `metrics`, `start_date`, `end_date`, `output_format` (`CSV_DOWNLOAD`, `XLSX_DOWNLOAD`, hoặc `CSV_STRING`).
   - Phản hồi sẽ trả về mã định danh tác vụ `task_id`.
   > [!NOTE]
   > Báo cáo bất đồng bộ không có giới hạn về khoảng thời gian ngày (`start_date` và `end_date`). Tuy nhiên, trong chế độ bất đồng bộ, bộ lọc `filtering` chỉ hỗ trợ các trường: `campaign_ids`, `adgroup_ids`, và `ad_ids`.

2. **Bước 2: Kiểm tra trạng thái tác vụ**
   - Định kỳ gọi endpoint [/report/task/check/](../12-api-reference/58-reporting.md#doc-1740302781443073) bằng phương thức `GET` với `advertiser_id` và `task_id`.
   - Kiểm tra trường `status`: `QUEUING` (đang chờ), `PROCESSING` (đang xử lý), `SUCCESS` (hoàn tất), `FAILED` (thất bại), `CANCELED` (đã hủy).
   - Nếu tác vụ chạy quá lâu hoặc bị cấu hình sai, bạn có thể gọi [/report/task/cancel/](../12-api-reference/58-reporting.md#doc-1803615367145537) để hủy tác vụ.

3. **Bước 3: Tải kết quả báo cáo**
   - Khi trạng thái là `SUCCESS`, gọi endpoint [/report/task/download/](../12-api-reference/58-reporting.md#doc-1740302808815618) bằng phương thức `GET`.
   - Hệ thống sẽ trả về đường dẫn `download_url` (có hiệu lực trong vòng 1 giờ) để tải file hoặc trả về trực tiếp luồng dữ liệu CSV.

---

## Các loại báo cáo (`Report types`)
<a id="doc-1738864835805186"></a>
<!-- doc_id: 1738864835805186 -->

> Đường dẫn: Marketing API > Reporting > Guides > Report types

Tùy thuộc vào loại dữ liệu bạn muốn truy vấn, TikTok cung cấp 6 loại báo cáo: Basic reports, Audience reports, Playable ad reports, DSA reports, Business Center reports, và GMV max ads reports.

Bảng dưới đây tổng hợp tổng quan về các loại báo cáo này cùng tính tương thích với quảng cáo đấu thầu (auction ads) và quảng cáo đặt trước (reservation ads):

| Loại báo cáo (Report type) | Mô tả | Hỗ trợ đấu thầu (Support auction ads) | Hỗ trợ đặt trước (Support reservation ads) |
|---|---|---|---|
| Báo cáo cơ bản (Basic report) | Sử dụng loại báo cáo này để lấy dữ liệu chi phí và hiệu suất ở 4 cấp độ: chiến dịch, nhóm quảng cáo, quảng cáo hoặc tài khoản quảng cáo.<br>Chi tiết xem tại [Basic reports](bao-cao-p1.md#doc-1738864915188737).<br>> [!NOTE]<br>> Với quảng cáo đấu thầu, đặt `service_type` = `AUCTION` và `report_type` = `BASIC`. Với quảng cáo đặt trước, đặt `service_type` = `RESERVATION` và `report_type` = `BASIC`. | ✅ | ✅<br>> [!NOTE]<br>> Bạn có thể lấy dữ liệu quảng cáo TopView từ báo cáo cơ bản. |
| Báo cáo đối tượng (Audience report) | Sử dụng loại báo cáo này để lấy dữ liệu phân tích đối tượng. Bạn có thể nhóm dữ liệu chi phí và hiệu suất theo các thuộc tính đối tượng như độ tuổi, giới tính, quốc gia/khu vực hoặc sở thích.<br>Chi tiết xem tại [Audience reports](bao-cao-p3.md#doc-1738864928947201). | ✅ | ✅<br>> [!NOTE]<br>> Bạn có thể lấy dữ liệu quảng cáo TopView từ báo cáo đối tượng. |
| Báo cáo playable (Playable ad report) | Sử dụng loại báo cáo này để lấy dữ liệu về quảng cáo nội dung tương tác (Playable Ads).<br>Chi tiết xem tại [Playable ad reports](bao-cao-p3.md#doc-1738864940608513). | ✅ | ❌ |
| Báo cáo DSA (DSA report) | Sử dụng loại báo cáo này để lấy dữ liệu về Quảng cáo danh mục động (Dynamic Showcase Ads - DSA).<br>Chi tiết xem tại [DSA reports](bao-cao-p3.md#doc-1738864960144385). | ✅ | ❌ |
| Báo cáo Business Center (Business Center report) | Sử dụng loại báo cáo này để lấy dữ liệu chi phí và hiệu suất của các tài khoản quảng cáo thuộc một Business Center.<br>Chi tiết xem tại [Business Center reports](bao-cao-p3.md#doc-1775747432712194). | ✅ | ✅ |
| Báo cáo GMV Max (GMV max ads report) *(Sắp ngừng hỗ trợ - To-be-deprecated)* | Sử dụng loại báo cáo này để lấy dữ liệu chi phí của [Product GMV max ads](https://ads.tiktok.com/help/article/how-to-create-product-gmv-max-ads-in-seller-center) và LIVE GMV max ads được tạo từ TikTok Shop ở hai cấp độ: cấp chiến dịch và cấp tài khoản quảng cáo.<br>Chi tiết xem tại [GMV max ads reports](bao-cao-p4.md#doc-1803073629472770).<br>> [!IMPORTANT]<br>> Báo cáo GMV max chỉ cung cấp dữ liệu giới hạn và sẽ bị ngừng hỗ trợ trong phiên bản API tiếp theo. Để đảm bảo tính tương thích lâu dài, vui lòng chuyển sang sử dụng [/gmv_max/report/get/](../12-api-reference/45-gmv-max-p2.md#doc-1824721673497601). | ✅ | ❌ |

---

## Báo cáo cơ bản (`Basic reports`)
<a id="doc-1738864915188737"></a>
<!-- doc_id: 1738864915188737 -->

> Đường dẫn: Marketing API > Reporting > Guides > Report types > Basic reports

Báo cáo cơ bản (Basic reports) là loại báo cáo cung cấp dữ liệu toàn diện nhất về quảng cáo của bạn, bao gồm dữ liệu chi phí, hiệu suất phân phối, lượt phát video, tương tác xã hội cũng như các sự kiện chuyển đổi trên website và trong ứng dụng.

### Các chiều dữ liệu được hỗ trợ
Xem chi tiết các chiều dữ liệu hỗ trợ trong báo cáo cơ bản tại [Supported dimensions](bao-cao-p1.md#doc-1751443956638721).

### Các chỉ số được hỗ trợ
Xem chi tiết các chỉ số được hỗ trợ trong báo cáo cơ bản tại [Supported metrics](bao-cao-p2.md#doc-1751443967255553).

### Bộ lọc được hỗ trợ
Xem chi tiết các bộ lọc hỗ trợ trong báo cáo cơ bản tại [Supported filters](bao-cao-p3.md#doc-1751443975608321).

### Hỗ trợ số liệu toàn thời gian (Lifetime metrics)
Báo cáo cơ bản hỗ trợ truy vấn các chỉ số toàn thời gian (lifetime) ở cả 4 cấp độ: Nhà quảng cáo (`AUCTION_ADVERTISER`), Chiến dịch (`AUCTION_CAMPAIGN`), Nhóm quảng cáo (`AUCTION_ADGROUP`), và Quảng cáo (`AUCTION_AD`).
> [!NOTE]
> Khi truy vấn số liệu lifetime (`query_lifetime` = `true`), hệ thống không hỗ trợ phân tách dữ liệu theo thời gian hoặc vị trí địa lý. Do đó, trường `dimensions` không được chứa `stat_time_day`, `stat_time_hour` hoặc `country_code`.

### Trường hợp sử dụng tiêu biểu (Use cases)

#### 1. Truy vấn tổng chi tiêu của tài khoản quảng cáo trong một khoảng thời gian
**Tham số yêu cầu mẫu:**
```json
{
    "advertiser_id": "7123456789012345678",
    "service_type": "AUCTION",
    "report_type": "BASIC",
    "data_level": "AUCTION_ADVERTISER",
    "dimensions": [
         "advertiser_id"
    ],
    "metrics": [
        "spend",
        "impressions",
        "reach"
    ],
    "start_date": "2025-01-01",
    "end_date": "2025-01-31",
    "page": 1,
    "page_size": 200
}
```

#### 2. Truy vấn báo cáo theo ngày của một số nhóm quảng cáo cụ thể
**Tham số yêu cầu mẫu:**
```json
{
    "advertiser_id": "7123456789012345678",
    "service_type": "AUCTION",
    "report_type": "BASIC",
    "data_level": "AUCTION_ADGROUP",
    "dimensions": [
        "adgroup_id",
        "stat_time_day"
    ],
    "metrics": [
        "spend",
        "impressions",
        "clicks",
        "conversion",
        "cost_per_conversion"
    ],
    "filtering": [
        {
            "field_name": "adgroup_ids",
            "filter_type": "IN",
            "filter_value": "[\"1723456789099888\", \"1723456789099889\"]"
        }
    ],
    "start_date": "2025-02-01",
    "end_date": "2025-02-15",
    "page": 1,
    "page_size": 100
}
```


---

## Các chiều dữ liệu được hỗ trợ (`Supported dimensions`)
<a id="doc-1751443956638721"></a>
<!-- doc_id: 1751443956638721 -->

> Đường dẫn: Marketing API > Reporting > Guides > Report types > Basic reports > Supported dimensions

Chiều dữ liệu (dimension) là thuộc tính dùng để gom nhóm dữ liệu báo cáo của bạn. Báo cáo cơ bản hỗ trợ các chiều dữ liệu dưới đây. Lưu ý rằng hiện tại API chưa hỗ trợ toàn bộ tất cả các chiều có trên giao diện TikTok Ads Manager.

### Chiến dịch thông thường (Regular campaigns)
Nếu chiến dịch của bạn là chiến dịch thông thường (không phải chiến dịch dành riêng cho iOS 14), bạn có thể sử dụng các chiều dữ liệu sau:

| Dimension Name | Description |
|---|---|
| `advertiser_id` | Nhóm theo ID nhà quảng cáo.<br>> [!NOTE]<br>> • Nếu bạn truyền `advertiser_ids` qua [/report/task/create/](../12-api-reference/58-reporting.md#doc-1740302766489602), mỗi yêu cầu có thể dùng chiều `advertiser_id` cùng với **một** chiều ID và/hoặc **một** chiều thời gian (ví dụ: `["advertiser_id", "campaign_id", "stat_time_day"]`).<br>> • Dữ liệu báo cáo của quảng cáo Nhiệm vụ thương hiệu ([Branded Mission](https://ads.tiktok.com/help/article/about-branded-mission)) chỉ có thể truy cập được khi truy vấn ở cấp tài khoản bằng chiều `advertiser_id`. Các truy vấn dùng `campaign_id`, `adgroup_id` hoặc `ad_id` sẽ không trả về dữ liệu Branded Mission. |
| `campaign_id` | Nhóm theo ID chiến dịch.<br>> [!NOTE]<br>> • Trong báo cáo cơ bản đồng bộ, bộ lọc `campaign_status` mặc định áp dụng `STATUS_NOT_DELETE`. Nếu muốn lấy dữ liệu cho cả các chiến dịch đã xóa, bạn cần đặt `campaign_status` thành `STATUS_ALL`. |
| `adgroup_id` | Nhóm theo ID nhóm quảng cáo.<br>> [!NOTE]<br>> • Mặc định bộ lọc `adgroup_status` là `STATUS_NOT_DELETE`. Đặt thành `STATUS_ALL` nếu muốn lấy cả nhóm quảng cáo đã xóa. |
| `ad_id_v2` | Nhóm theo ID quảng cáo v2.<br>Dữ liệu nhận được bao gồm:<br>• Cấp quảng cáo cho Manual Ads.<br>• Cấp quảng cáo cho Smart+ Campaigns.<br>• Cấp **quảng cáo / nhóm tài sản (ad / asset group)** cho Upgraded Smart+ Ads.<br>> [!NOTE]<br>> Không dùng chung với chiều `ad_id`, bộ lọc `ad_ids` hoặc chỉ số thuộc tính `ad_id`. |
| `ad_id` | Nhóm theo ID quảng cáo.<br>Dữ liệu nhận được bao gồm:<br>• Cấp quảng cáo cho Manual Ads.<br>• Cấp quảng cáo cho Smart+ Campaigns.<br>• Cấp **nội dung sáng tạo (creative)** cho Upgraded Smart+ Ads.<br>> [!NOTE]<br>> Mặc định bộ lọc `ad_status` là `STATUS_NOT_DELETE`. Đặt thành `STATUS_ALL` nếu muốn lấy cả quảng cáo đã xóa. |
| `stat_time_day` | Nhóm theo ngày (định dạng `YYYY-MM-DD 00:00:00`). |
| `stat_time_hour` | Nhóm theo giờ (định dạng `YYYY-MM-DD HH:00:00`). |
| `country_code` | Nhóm theo mã vị trí quốc gia/khu vực. Xem [Supported metrics for a dimension in basic reports](bao-cao-p1.md#doc-1759239462689793). |
| `ad_type` | Nhóm theo loại quảng cáo. Dùng chiều này để phân biệt giữa Quảng cáo tìm kiếm (Search Ads) và quảng cáo không phải tìm kiếm. Nếu là Search Ad, giá trị trả về là `Search`. Hỗ trợ ở tất cả các cấp độ `data_level`. |
| `custom_event_type` | Nhóm theo loại sự kiện tùy chỉnh. Hỗ trợ cho các chỉ số sự kiện Onsite App và Web (như `click_call`, `view_content`, `add_to_cart`, `complete_payment`...). |
| `event_source_id` | Nhóm theo ID nguồn sự kiện (Pixel ID hoặc App ID). |
| `video_material_id` | Nhóm theo ID tài liệu video. |
| `image_id` | Nhóm theo ID hình ảnh. |
| `search_keyword` | Nhóm theo từ khóa tìm kiếm (Search keyword) mà nhà quảng cáo thiết lập. |
| `search_terms` | Nhóm theo cụm từ tìm kiếm thực tế của người dùng (User search terms). |
| `match_type` | Nhóm theo loại đối sánh từ khóa tìm kiếm (`EXACT`, `BROAD`, `PHRASE`). |
| `page_id` | Nhóm theo ID trang Instant Page / TikTok Instant Experience. |
| `component_name` | Nhóm theo tên thành phần tương tác trong Instant Experience. |
| `room_id` | Nhóm theo ID phòng LIVE (áp dụng cho quảng cáo LIVE Shopping). |
| `minis_id` | Nhóm theo ID ứng dụng nhỏ TikTok (TikTok Minis ID). Xem [180-day attribution window metrics together with the dimension minis_id](bao-cao-p1.md#doc-1866989577164801). |
| `post_id` | Nhóm theo ID bài đăng TikTok (dành cho Spark Ads hoặc bài đăng tài khoản TikTok). |

#### Quy tắc gom nhóm chiều dữ liệu (Dimension grouping)
Các chiều dữ liệu được phân loại thành:
- **Chiều ID**: `advertiser_id`, `campaign_id`, `adgroup_id`, `ad_id`, `ad_id_v2`.
- **Chiều thời gian (Time)**: `stat_time_day`, `stat_time_hour`.
- **Chiều vị trí nhắm mục tiêu (Targeting)**: `country_code`.
- **Chiều tài sản (Asset)**: `video_material_id`, `image_id`, `page_id`, `component_name`, `post_id`.
- **Chiều tìm kiếm (Search)**: `search_keyword`, `search_terms`, `match_type`, `ad_type`.

| Dimension category (Phân loại chiều) | Grouping Rule (Quy tắc gom nhóm) |
|---|---|
| `ID & Time` | Mỗi yêu cầu chỉ được chứa tối đa **một** chiều ID và/hoặc **một** chiều thời gian (ví dụ: `["campaign_id", "stat_time_day"]`). |
| `Targeting` | Chiều `country_code` có thể đi kèm một chiều ID và/hoặc `stat_time_day` (ví dụ: `["ad_id", "stat_time_day", "country_code"]`). |
| `Asset` | Chiều tài sản (`video_material_id`, `image_id`, `page_id`...) có thể kết hợp với chiều ID và `stat_time_day`. |
| `Search` | `search_terms`, `search_keyword`, `match_type` có thể đi kèm chiều ID và `stat_time_day`. |

**Ví dụ tổ hợp hợp lệ:**
`["campaign_id"]`, `["stat_time_day"]`, `["campaign_id", "stat_time_day"]`, `["campaign_id", "stat_time_hour"]`, `["campaign_id", "country_code"]`, `["ad_id", "stat_time_day", "country_code"]`.

**Ví dụ tổ hợp không hợp lệ:**
`["stat_time_hour", "country_code"]` (không hỗ trợ kết hợp giờ với mã quốc gia).

---

### Chiến dịch dành riêng cho iOS 14 (iOS14 Dedicated Campaign)
Nếu chiến dịch của bạn là chiến dịch dành riêng cho iOS 14 (iOS 14 Dedicated Campaign), bạn có thể sử dụng các chiều dữ liệu sau:

| Dimension Name | Description |
|---|---|
| `advertiser_id` | Nhóm theo ID nhà quảng cáo. |
| `campaign_id` | Nhóm theo ID chiến dịch. |
| `adgroup_id` | Nhóm theo ID nhóm quảng cáo. |
| `ad_id` | Nhóm theo ID quảng cáo. |
| `stat_time_day` | Nhóm theo ngày. |
| `skan_postback_sequence` | Nhóm theo thứ tự Postback của khung SKAdNetwork (SKAN 4.0). Giá trị enum:<br>• `0`: Chiến dịch không áp dụng chuỗi postback SKAN.<br>• `1`: Postback đầu tiên (đo lường hoạt động trong ứng dụng từ ngày 0 đến ngày 2).<br>• `2`: Postback thứ hai (đo lường hoạt động từ ngày 3 đến ngày 7).<br>• `3`: Postback thứ ba (đo lường hoạt động từ ngày 8 đến ngày 35). |

#### Quy tắc gom nhóm chiều cho iOS 14 Dedicated Campaign
- Chiều ID: `advertiser_id`, `campaign_id`, `adgroup_id`, `ad_id`.
- Chiều thời gian: `stat_time_day`.
- Chiều tài sản: `skan_postback_sequence`.

| Dimension category | Grouping Rule |
|---|---|
| `ID & Time` | Mỗi yêu cầu chỉ có **một** chiều ID và/hoặc **một** chiều thời gian. |
| `Asset` | Có thể chỉ định `skan_postback_sequence` đứng độc lập, hoặc kèm một chiều ID, hoặc kèm `stat_time_day`, hoặc kèm cả chiều ID và `stat_time_day`. |

**Ví dụ tổ hợp hợp lệ:**
- `["advertiser_id"]`
- `["advertiser_id", "stat_time_day"]`
- `["campaign_id", "stat_time_day"]`
- `["ad_id", "stat_time_day"]`
- `["advertiser_id", "stat_time_day", "skan_postback_sequence"]`


---

## Chỉ số hỗ trợ theo chiều dữ liệu trong báo cáo cơ bản (`Supported metrics for a dimension in basic reports`)
<a id="doc-1759239462689793"></a>
<!-- doc_id: 1759239462689793 -->

> Đường dẫn: Marketing API > Reporting > Guides > Report types > Basic reports > Supported dimensions > Supported metrics for a dimension in basic reports

Khi kết hợp các chiều dữ liệu cụ thể, chỉ một tập hợp chỉ số nhất định được hệ thống hỗ trợ. Phần này liệt kê chi tiết các chỉ số khả dụng khi gom nhóm theo từng chiều dữ liệu tương ứng. Chi tiết xem thêm tại [Basic report-Supported metrics](bao-cao-p2.md#doc-1751443967255553).

### 1. Chỉ số hỗ trợ cho chiều `ad_type` (Supported metrics for `ad_type`)

| Field | Description |
|---|---|
| `Core metrics` (Chỉ số cốt lõi) | |
| ↳ `spend` | Tổng chi phí quảng cáo. |
| ↳ `cpc` | Chi phí trung bình cho mỗi lượt nhấp (CPC đích). |
| ↳ `cpm` | Chi phí cho mỗi 1.000 lượt hiển thị (CPM). |
| ↳ `impressions` | Số lượt hiển thị. |
| ↳ `gross_impressions` | Tổng số lượt hiển thị thô (bao gồm cả hiển thị không hợp lệ). |
| ↳ `clicks` | Số lượt nhấp chuột đến đích. |
| ↳ `ctr` | Tỷ lệ nhấp chuột (CTR đích). |
| ↳ `conversion` | Số lượng chuyển đổi. |
| ↳ `cost_per_conversion` | Chi phí trên mỗi chuyển đổi. |
| ↳ `conversion_rate` | Tỷ lệ chuyển đổi (CVR theo lượt nhấp). |
| ↳ `real_time_conversion` | Số chuyển đổi thời gian thực. |
| ↳ `real_time_cost_per_conversion` | Chi phí trên mỗi chuyển đổi thời gian thực. |
| ↳ `real_time_conversion_rate` | Tỷ lệ chuyển đổi thời gian thực (CVR). |
| `Videos metrics` (Chỉ số video) | |
| ↳ `video_play_actions` | Lượt phát video. |
| ↳ `video_watched_2s` | Lượt xem video từ 2 giây trở lên. |
| ↳ `video_watched_6s` | Lượt xem video từ 6 giây trở lên. |
| ↳ `average_video_play` | Thời gian phát video trung bình mỗi lượt xem. |
| ↳ `video_views_p25` | Lượt xem video đạt 25% thời lượng. |
| ↳ `video_views_p50` | Lượt xem video đạt 50% thời lượng. |
| ↳ `video_views_p75` | Lượt xem video đạt 75% thời lượng. |
| ↳ `video_views_p100` | Lượt xem video đạt 100% thời lượng. |
| ↳ `engaged_view` | Lượt xem tập trung 6 giây (Focused views). |
| ↳ `engaged_view_15s` | Lượt xem tập trung 15 giây. |
| `Clicks metrics` (Chỉ số nhấp chuột khác) | |
| ↳ `clicks_on_music_disc` | Lượt nhấp vào đĩa nhạc (Music Clicks). |
| `Social metrics` (Chỉ số tương tác mạng xã hội) | |
| ↳ `follows` | Lượt theo dõi trả phí (Paid Followers). |
| ↳ `likes` | Lượt thích trả phí (Paid Likes). |
| ↳ `comments` | Lượt bình luận trả phí (Paid Comments). |
| ↳ `shares` | Lượt chia sẻ trả phí (Paid Shares). |
| ↳ `profile_visits` | Lượt truy cập hồ sơ trả phí (Paid Profile Visits). |
| ↳ `profile_visits_rate` | Tỷ lệ truy cập trang hồ sơ trả phí. |
| `Website metrics` (Chỉ số trang web) | |
| ↳ `Landing page view` | Lượt xem trang đích. |
| ↳↳ `total_landing_page_view` | Tổng số lượt xem trang đích (website). |
| ↳↳ `cost_per_landing_page_view` | Chi phí trên mỗi lượt xem trang đích. |
| ↳↳ `landing_page_view_rate` | Tỷ lệ xem trang đích (website). |
| `Core metrics (SKAN)` | Các chỉ số SKAdNetwork cốt lõi. |
| ↳ `skan_conversion` | Lượt chuyển đổi ghi nhận qua SKAN. |
| `App metrics (SKAN)` | Chỉ số ứng dụng SKAdNetwork. |
| ↳ `skan_app_install` | Lượt cài đặt ứng dụng ghi nhận qua SKAN. |

---

### 2. Chỉ số hỗ trợ cho chiều `country_code` (Supported metrics for `country_code`)

| Field | Description | Đồng bộ (Sync) | Bất đồng bộ (Async) |
|---|---|---|---|
| `Core metrics` | | | |
| ↳ `spend` | Chi phí | ✅ | ✅ |
| ↳ `cpc` | CPC | ✅ | ✅ |
| ↳ `cpm` | CPM | ✅ | ✅ |
| ↳ `impressions` | Lượt hiển thị | ✅ | ✅ |
| ↳ `gross_impressions` | Lượt hiển thị thô | ✅ | ✅ |
| ↳ `clicks` | Lượt nhấp | ✅ | ✅ |
| ↳ `ctr` | CTR | ✅ | ✅ |
| ↳ `reach` | Người tiếp cận | ✅ | ❌ |
| ↳ `cost_per_1000_reached` | Chi phí mỗi 1.000 người tiếp cận | ✅ | ❌ |
| ↳ `conversion` | Lượt chuyển đổi | ✅ | ✅ |
| ↳ `cost_per_conversion` | Chi phí mỗi chuyển đổi | ✅ | ✅ |
| ↳ `conversion_rate` | Tỷ lệ chuyển đổi | ✅ | ✅ |
| ↳ `real_time_conversion` | Chuyển đổi thời gian thực | ✅ | ✅ |
| ↳ `real_time_cost_per_conversion` | Chi phí mỗi chuyển đổi thời gian thực | ✅ | ✅ |
| ↳ `real_time_conversion_rate` | Tỷ lệ chuyển đổi thời gian thực | ✅ | ✅ |
| ↳ `result` | Kết quả | ✅ | ❌ |
| ↳ `cost_per_result` | Chi phí mỗi kết quả | ✅ | ❌ |
| ↳ `result_rate` | Tỷ lệ kết quả | ✅ | ❌ |
| ↳ `real_time_result` | Kết quả thời gian thực | ✅ | ❌ |
| ↳ `real_time_cost_per_result` | Chi phí mỗi kết quả thời gian thực | ✅ | ❌ |
| ↳ `real_time_result_rate` | Tỷ lệ kết quả thời gian thực | ✅ | ❌ |
| ↳ `frequency` | Tần suất | ✅ | ❌ |
| `Videos metrics` | | | |
| ↳ `video_play_actions` | Lượt phát video | ✅ | ✅ |
| ↳ `video_watched_2s` | Lượt xem 2 giây | ✅ | ✅ |
| ↳ `video_watched_6s` | Lượt xem 6 giây | ✅ | ✅ |
| ↳ `average_video_play` | Thời gian xem trung bình | ✅ | ✅ |
| ↳ `video_views_p25` | Xem 25% | ✅ | ✅ |
| ↳ `video_views_p50` | Xem 50% | ✅ | ✅ |
| ↳ `video_views_p75` | Xem 75% | ✅ | ✅ |
| ↳ `video_views_p100` | Xem 100% | ✅ | ✅ |
| ↳ `engaged_view` | Lượt xem tập trung 6s | ✅ | ✅ |
| ↳ `engaged_view_15s` | Lượt xem tập trung 15s | ✅ | ✅ |
| `Clicks metrics` | | | |
| ↳ `clicks_on_music_disc` | Lượt nhấp đĩa nhạc | ✅ | ✅ |
| `Social metrics` | | | |
| ↳ `follows` | Lượt theo dõi | ✅ | ✅ |
| ↳ `likes` | Lượt thích | ✅ | ✅ |
| ↳ `comments` | Lượt bình luận | ✅ | ✅ |
| ↳ `shares` | Lượt chia sẻ | ✅ | ✅ |
| ↳ `profile_visits` | Lượt xem trang cá nhân | ✅ | ✅ |
| ↳ `profile_visits_rate` | Tỷ lệ xem trang cá nhân | ✅ | ✅ |
| `LIVE metrics` | | | |
| ↳ `live_product_clicks` | Lượt nhấp sản phẩm trong phiên LIVE | ✅ | ❌ |
| `App metrics` | | | |
| ↳ `real_time_app_install` | Lượt cài đặt ứng dụng theo thời gian thực | ✅ | ❌ |
| ↳ `real_time_app_install_cost` | Chi phí mỗi lượt cài đặt thời gian thực | ✅ | ❌ |
| ↳ `app_install` | Cài đặt ứng dụng | ✅ | ❌ |
| ↳ `cost_per_app_install` | Chi phí mỗi lượt cài đặt | ✅ | ❌ |
| ↳ `registration` | Lượt đăng ký ứng dụng | ✅ | ❌ |
| ↳ `cost_per_registration` | Chi phí mỗi lượt đăng ký | ✅ | ❌ |
| ↳ `registration_rate` | Tỷ lệ đăng ký | ✅ | ❌ |
| ↳ `purchase` | Lượt mua hàng trong app | ✅ | ❌ |
| ↳ `cost_per_purchase` | Chi phí mỗi lượt mua hàng | ✅ | ❌ |
| ↳ `purchase_rate` | Tỷ lệ mua hàng | ✅ | ❌ |
| `Website metrics` | | | |
| ↳ `complete_payment` | Lượt thanh toán hoàn tất (website) | ✅ | ❌ |
| ↳ `cost_per_complete_payment` | Chi phí mỗi lượt thanh toán hoàn tất | ✅ | ❌ |
| ↳ `complete_payment_rate` | Tỷ lệ thanh toán hoàn tất | ✅ | ❌ |
| ↳ `Landing page view` | | | |
| ↳↳ `total_landing_page_view` | Lượt xem trang đích | ✅ | ✅ |
| ↳↳ `cost_per_landing_page_view` | Chi phí mỗi lượt xem trang đích | ✅ | ✅ |
| ↳↳ `landing_page_view_rate` | Tỷ lệ xem trang đích | ✅ | ✅ |
| ↳ `page_browse_view` *(deprecated)* | Lượt duyệt trang | ✅ | ❌ |
| ↳ `button_click` | Lượt nhấp nút trên website | ✅ | ❌ |
| ↳ `online_consult` | Lượt liên hệ tư vấn trực tuyến | ✅ | ❌ |
| ↳ `form` | Lượt gửi biểu mẫu trên website | ✅ | ❌ |
| ↳ `download_start` | Lượt tải tệp xuống từ website | ✅ | ❌ |

---

### 3. Chỉ số hỗ trợ cho chiều `search_terms` (Supported metrics for `search_terms`)

| Field | Description |
|---|---|
| `Core metrics` | |
| ↳ `spend` | Chi phí quảng cáo tìm kiếm. |
| ↳ `cpc` | Chi phí trên mỗi lượt nhấp. |
| ↳ `cpm` | Chi phí trên 1.000 lượt hiển thị. |
| ↳ `impressions` | Lượt hiển thị quảng cáo tìm kiếm. |
| ↳ `clicks` | Lượt nhấp chuột. |
| ↳ `ctr` | Tỷ lệ nhấp (CTR). |
| ↳ `conversion` | Lượt chuyển đổi. |
| ↳ `cost_per_conversion` | Chi phí mỗi chuyển đổi. |
| ↳ `conversion_rate` | Tỷ lệ chuyển đổi (CVR). |
| `Videos metrics` | |
| ↳ `video_play_actions` | Lượt phát video từ kết quả tìm kiếm. |
| ↳ `video_watched_2s` | Lượt xem video 2 giây. |
| ↳ `video_watched_6s` | Lượt xem video 6 giây. |

---

### 4. Chỉ số hỗ trợ cho chiều `page_id` và `component_name`

#### Chiều `page_id` (Trang Instant Experience)
| Field | Description |
|---|---|
| `TikTok metrics` | |
| ↳ `ix_page_view` | Lượt xem trang Instant Experience. |
| ↳ `ix_view_rate` | Tỷ lệ xem trang Instant Experience. |
| ↳ `ix_average_view_time` | Thời gian xem trang trung bình. |
| `Instant experience metrics` | |
| ↳ `ix_button_click` | Lượt nhấp nút trong Instant Experience. |
| ↳ `ix_product_click` | Lượt nhấp sản phẩm trong Instant Experience. |
| `Core metrics` | |
| ↳ `spend`, `impressions`, `clicks`, `ctr`, `conversion`, `cost_per_conversion` | Các chỉ số chi phí và phân phối cơ bản. |

#### Chiều `component_name` (Thành phần trong trang Instant Experience)
| Field | Description |
|---|---|
| `Instant experience metrics` | |
| ↳ `component_click` | Lượt nhấp vào thành phần tương tác. |
| ↳ `component_click_rate` | Tỷ lệ nhấp vào thành phần. |
| `Core metrics` | |
| ↳ `spend`, `impressions`, `clicks` | Các chỉ số hiển thị và chi phí liên quan. |

---

### 5. Chỉ số hỗ trợ cho chiều `room_id` (Phòng phát trực tiếp LIVE)

| Field | Description |
|---|---|
| `Core metrics` | |
| ↳ `spend` | Chi phí thúc đẩy phòng LIVE. |
| ↳ `impressions` | Lượt hiển thị quảng cáo LIVE. |
| ↳ `clicks` | Lượt nhấp vào phòng LIVE. |
| `TikTok metrics` | |
| ↳ `live_views` | Lượt xem phiên LIVE. |
| ↳ `live_unique_views` | Người xem phiên LIVE duy nhất. |
| ↳ `live_effective_views` | Lượt xem hiệu quả (xem trên 10 giây). |
| ↳ `live_product_clicks` | Lượt nhấp vào sản phẩm trưng bày trong LIVE. |
| `Shop metrics` | |
| ↳ `live_orders` | Số lượng đơn hàng phát sinh từ phòng LIVE. |
| ↳ `live_gmv` | Tổng giá trị giao dịch phát sinh từ phòng LIVE. |

---

### 6. Chỉ số hỗ trợ cho chiều `post_id` (Bài đăng TikTok)

| Field | Description |
|---|---|
| `Core metrics` | |
| ↳ `spend` | Chi phí phân phối bài đăng. |
| ↳ `cpc` | Chi phí mỗi lượt nhấp. |
| ↳ `cpm` | Chi phí mỗi 1.000 lượt hiển thị. |
| ↳ `impressions` | Số lượt hiển thị bài đăng. |
| ↳ `clicks` | Số lượt nhấp. |
| ↳ `ctr` | Tỷ lệ nhấp. |
| ↳ `conversion` | Lượt chuyển đổi. |
| ↳ `cost_per_conversion` | Chi phí mỗi chuyển đổi. |
| ↳ `conversion_rate` | Tỷ lệ chuyển đổi. |
| `Videos metrics` | |
| ↳ `video_play_actions` | Lượt xem video bài đăng. |
| ↳ `video_watched_2s` | Lượt xem 2 giây. |
| ↳ `video_watched_6s` | Lượt xem 6 giây. |
| ↳ `engaged_view` | Lượt xem tập trung 6 giây. |
| ↳ `video_views_p25` / `video_views_p50` / `video_views_p75` / `video_views_p100` | Lượt xem theo tiến trình phần trăm. |
| ↳ `average_video_play` | Thời gian xem trung bình. |
| `TikTok metrics` | |
| ↳ `Add to wishlist` | |
| ↳↳ `onsite_add_to_wishlist` | Lượt thêm vào danh sách yêu thích trên TikTok. |
| ↳↳ `cost_per_onsite_add_to_wishlist` | Chi phí mỗi lượt thêm vào yêu thích. |
| ↳↳ `onsite_add_to_wishlist_rate` | Tỷ lệ thêm vào yêu thích. |
| ↳↳ `value_per_onsite_add_to_wishlist` | Giá trị trung bình mỗi lượt thêm vào yêu thích. |
| ↳↳ `total_onsite_add_to_wishlist_value` | Tổng giá trị danh sách yêu thích. |
| ↳ `Product clicks` | |
| ↳↳ `ix_product_click_count` | Lượt nhấp vào sản phẩm trên TikTok. |
| ↳↳ `cost_per_ix_product_click_count` | Chi phí mỗi lượt nhấp sản phẩm. |
| ↳↳ `ix_product_click_count_rate` | Tỷ lệ nhấp sản phẩm (%). |
| `Shop metrics` | |
| ↳ `ROAS` | |
| ↳↳ `onsite_shopping_roas` | Lợi tức chi tiêu quảng cáo từ TikTok Shop. |
| ↳ `Purchases` | |
| ↳↳ `onsite_shopping` | Lượt mua hàng hoàn tất trên Shop. |
| ↳↳ `cost_per_onsite_shopping` | Chi phí mỗi lượt mua hàng. |
| ↳↳ `onsite_shopping_rate` | Tỷ lệ mua hàng (%). |
| ↳↳ `value_per_onsite_shopping` | Giá trị đơn hàng trung bình (AOV). |
| ↳↳ `total_onsite_shopping_value` | Tổng doanh thu gộp (Gross Revenue) trên Shop. |
| ↳ `Checkouts initiated` | |
| ↳↳ `onsite_initiate_checkout_count` | Lượt bắt đầu thanh toán trên Shop. |
| ↳↳ `cost_per_onsite_initiate_checkout_count` | Chi phí mỗi lượt bắt đầu thanh toán. |
| ↳↳ `onsite_initiate_checkout_count_rate` | Tỷ lệ bắt đầu thanh toán (%). |
| ↳↳ `value_per_onsite_initiate_checkout_count` | Giá trị mỗi lượt bắt đầu thanh toán. |
| ↳↳ `total_onsite_initiate_checkout_count_value` | Tổng giá trị bắt đầu thanh toán. |
| ↳ `Product page views` | |
| ↳↳ `onsite_on_web_detail` | Lượt xem trang chi tiết sản phẩm trên Shop. |
| ↳↳ `cost_per_onsite_on_web_detail` | Chi phí mỗi lượt xem trang sản phẩm. |
| ↳↳ `onsite_on_web_detail_rate` | Tỷ lệ xem trang sản phẩm (%). |
| ↳↳ `value_per_onsite_on_web_detail` | Giá trị mỗi lượt xem trang sản phẩm. |
| ↳↳ `total_onsite_on_web_detail_value` | Tổng giá trị xem trang sản phẩm. |
| ↳ `Add to cart` | |
| ↳↳ `onsite_on_web_cart` | Lượt thêm sản phẩm vào giỏ hàng trên Shop. |
| ↳↳ `cost_per_onsite_on_web_cart` | Chi phí mỗi lượt thêm vào giỏ hàng. |
| ↳↳ `onsite_on_web_cart_rate` | Tỷ lệ thêm vào giỏ hàng (%). |
| ↳↳ `value_per_onsite_on_web_cart` | Giá trị mỗi lượt thêm vào giỏ hàng. |
| ↳↳ `total_onsite_on_web_cart_value` | Tổng giá trị hàng thêm vào giỏ. |

---

## Các chỉ số trong cửa sổ phân bổ 180 ngày cùng với chiều minis_id (`180-day attribution window metrics together with the dimension minis_id`)
<a id="doc-1866989577164801"></a>
<!-- doc_id: 1866989577164801 -->

> Đường dẫn: Marketing API > Reporting > Guides > Report types > Basic reports > Supported dimensions > 180-day attribution window metrics together with the dimension minis_id

Các bảng dưới đây liệt kê các chỉ số cụ thể được tính toán theo cửa sổ phân bổ 180 ngày (180-day attribution window) khi sử dụng kèm chiều dữ liệu `minis_id` (TikTok Minis).

### Chỉ số cốt lõi (Core metrics)

| Field | Description |
|---|---|
| `conversion` | Lượt chuyển đổi. |
| `cost_per_conversion` | Chi phí trên mỗi chuyển đổi. |
| `conversion_rate` | Tỷ lệ chuyển đổi (CVR theo lượt nhấp). |

### Chỉ số TikTok (TikTok metrics)

#### Chỉ số trả phí (Paid metrics)

| Field | Description |
|---|---|
| `Purchases` ROAS (TikTok) | |
| ↳ `onsite_purchases_roas` | ROAS mua hàng trên TikTok. |
| `Purchases` (TikTok) (Lượt mua hàng) | |
| ↳ `onsite_total_purchase` | Tổng số lượt mua hàng trên TikTok. |
| ↳ `onsite_cost_per_purchase` | Chi phí trên mỗi lượt mua hàng. |
| ↳ `onsite_purchase_rate` | Tỷ lệ mua hàng (%). |
| ↳ `onsite_value_per_purchase` | Giá trị trung bình mỗi lượt mua hàng. |
| ↳ `onsite_total_purchase_value` | Tổng giá trị mua hàng trên TikTok. |
| ↳ `onsite_unique_purchase` | Lượt mua hàng duy nhất (Unique purchases). |
| ↳ `onsite_cost_per_unique_purchase` | Chi phí mỗi lượt mua hàng duy nhất. |
| ↳ `onsite_total_purchase_value_calendar_day0` | Giá trị mua hàng ngày dương lịch 0 (Calendar day 0). |
| ↳ `onsite_total_purchase_value_calendar_day6` | Giá trị mua hàng ngày dương lịch 6. |
| ↳ `onsite_total_purchase_value_calendar_day13` | Giá trị mua hàng ngày dương lịch 13. |
| ↳ `onsite_total_purchase_roas_calendar_day0` | ROAS mua hàng ngày dương lịch 0. |
| ↳ `onsite_total_purchase_roas_calendar_day6` | ROAS mua hàng ngày dương lịch 6. |
| ↳ `onsite_total_purchase_roas_calendar_day13` | ROAS mua hàng ngày dương lịch 13. |
| ↳ `onsite_total_purchase_value_day0` | Giá trị mua hàng ngày 0 (Day 0). |
| ↳ `onsite_total_purchase_value_day1` | Giá trị mua hàng ngày 1. |
| ↳ `onsite_total_purchase_value_day2` | Giá trị mua hàng ngày 2. |
| ↳ `onsite_total_purchase_value_day3` | Giá trị mua hàng ngày 3. |
| ↳ `onsite_total_purchase_value_day4` | Giá trị mua hàng ngày 4. |
| ↳ `onsite_total_purchase_value_day5` | Giá trị mua hàng ngày 5. |
| ↳ `onsite_total_purchase_value_day20` | Giá trị mua hàng ngày 20. |
| ↳ `onsite_total_purchase_value_day27` | Giá trị mua hàng ngày 27. |
| ↳ `onsite_total_purchase_value_day29` | Giá trị mua hàng ngày 29. |
| ↳ `onsite_total_purchase_roas_day0` | ROAS mua hàng ngày 0. |
| ↳ `onsite_total_purchase_roas_day1` | ROAS mua hàng ngày 1. |
| ↳ `onsite_total_purchase_roas_day2` | ROAS mua hàng ngày 2. |
| ↳ `onsite_total_purchase_roas_day3` | ROAS mua hàng ngày 3. |
| ↳ `onsite_total_purchase_roas_day4` | ROAS mua hàng ngày 4. |
| ↳ `onsite_total_purchase_roas_day5` | ROAS mua hàng ngày 5. |
| ↳ `onsite_total_purchase_roas_day20` | ROAS mua hàng ngày 20. |
| ↳ `onsite_total_purchase_roas_day27` | ROAS mua hàng ngày 27. |
| ↳ `onsite_total_purchase_roas_day29` | ROAS mua hàng ngày 29. |
| `Checkouts` initiated (TikTok) (Bắt đầu thanh toán) | |
| ↳ `onsite_total_checkout_initiation` | Tổng lượt bắt đầu thanh toán trên TikTok. |
| ↳ `onsite_cost_per_checkout_initiation` | Chi phí mỗi lượt bắt đầu thanh toán. |
| ↳ `onsite_checkout_initiation_rate` | Tỷ lệ bắt đầu thanh toán (%). |
| ↳ `onsite_value_per_checkout_initiation` | Giá trị trung bình mỗi lượt bắt đầu thanh toán. |
| ↳ `onsite_total_checkout_initiation_value` | Tổng giá trị bắt đầu thanh toán. |
| ↳ `onsite_unique_checkout_initiation` | Lượt bắt đầu thanh toán duy nhất. |
| ↳ `onsite_cost_per_unique_checkout_initiation` | Chi phí mỗi lượt bắt đầu thanh toán duy nhất. |
| `Add` to cart (TikTok) (Thêm vào giỏ hàng) | |
| ↳ `onsite_total_add_to_cart` | Tổng số lượt thêm vào giỏ hàng trên TikTok. |
| ↳ `onsite_cost_per_add_to_cart` | Chi phí mỗi lượt thêm vào giỏ hàng. |
| ↳ `onsite_add_to_cart_rate` | Tỷ lệ thêm vào giỏ hàng (%). |
| ↳ `onsite_value_per_add_to_cart` | Giá trị mỗi lượt thêm vào giỏ hàng. |
| ↳ `onsite_total_add_to_cart_value` | Tổng giá trị hàng thêm vào giỏ. |
| ↳ `onsite_unique_add_to_cart` | Số lượt thêm vào giỏ hàng duy nhất. |
| ↳ `onsite_cost_per_unique_add_to_cart` | Chi phí mỗi lượt thêm vào giỏ hàng duy nhất. |
| `Launch` (Khởi chạy ứng dụng nhỏ) | |
| ↳ `onsite_unique_non_first_launch` | Số lần khởi chạy ứng dụng nhỏ không phải lần đầu (duy nhất). |
| ↳ `onsite_cost_per_unique_non_first_launch` | Chi phí trên mỗi lần khởi chạy duy nhất. |
| ↳ `onsite_total_non_first_launch` | Tổng số lần khởi chạy ứng dụng nhỏ không phải lần đầu. |
| ↳ `onsite_cost_per_non_first_launch` | Chi phí trên mỗi lượt khởi chạy. |
| `Subscriptions` (TikTok) (Đăng ký theo bao) | |
| ↳ `onsite_unique_subscribe` | Lượt đăng ký gói thuê bao duy nhất trên TikTok. |
| ↳ `onsite_cost_per_unique_subscribe` | Chi phí mỗi lượt đăng ký duy nhất. |
| ↳ `onsite_subscribe_rate` | Tỷ lệ đăng ký (%). |
| ↳ `onsite_total_subscribe` | Tổng số lượt đăng ký. |
| ↳ `onsite_cost_per_total_subscribe` | Chi phí trên mỗi lượt đăng ký. |
| ↳ `onsite_value_per_subscribe` | Giá trị trung bình mỗi gói đăng ký. |
| ↳ `onsite_total_subscribe_value` | Tổng giá trị các gói đăng ký trên TikTok. |
| ↳ `onsite_subscribe_value_day0` | Giá trị đăng ký ngày 0 (Day 0). |
| ↳ `onsite_subscribe_value_day1` | Giá trị đăng ký ngày 1. |
| ↳ `onsite_subscribe_value_day2` | Giá trị đăng ký ngày 2. |
| ↳ `onsite_subscribe_value_day3` | Giá trị đăng ký ngày 3. |
| ↳ `onsite_subscribe_value_day4` | Giá trị đăng ký ngày 4. |
| ↳ `onsite_subscribe_value_day5` | Giá trị đăng ký ngày 5. |
| ↳ `onsite_subscribe_value_day6` | Giá trị đăng ký ngày 6. |
| ↳ `onsite_subscribe_value_day13` | Giá trị đăng ký ngày 13. |
| ↳ `onsite_subscribe_value_day20` | Giá trị đăng ký ngày 20. |
| ↳ `onsite_subscribe_value_day27` | Giá trị đăng ký ngày 27. |
| ↳ `onsite_subscribe_value_day29` | Giá trị đăng ký ngày 29. |
