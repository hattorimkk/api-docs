# Hướng dẫn Báo cáo (Reporting) — phần 4/4

> Phân hệ Marketing API > Reporting > Guides > Report types, Optimization & Subscription API.
> Tài liệu này hướng dẫn chi tiết các chỉ số và bộ lọc của Báo cáo Business Center, báo cáo GMV Max Ads (sắp ngừng hỗ trợ), cẩm nang thực hành giảm thiểu Timeout trong báo cáo đồng bộ, bảng thời gian chốt và độ trễ dữ liệu (Data latency), tối ưu hóa hiệu năng truy vấn, giải đáp câu hỏi thường gặp (FAQs) và API đăng ký nhận báo cáo định kỳ (Reporting Subscription API).

---

## Mục lục điều hướng
- [1. Chỉ số hỗ trợ trong Báo cáo Business Center](#1-chi-so-ho-tro-trong-bao-cao-business-center)
- [2. Bộ lọc hỗ trợ trong Báo cáo Business Center](#2-bo-loc-ho-tro-trong-bao-cao-business-center)
- [3. Báo cáo GMV Max Ads (Sắp ngừng hỗ trợ)](#3-bao-cao-gmv-max-ads-sap-ngung-ho-tro)
- [4. Chiều dữ liệu GMV Max Ads](#4-chieu-du-lieu-gmv-max-ads)
- [5. Chỉ số GMV Max Ads](#5-chi-so-gmv-max-ads)
- [6. Cẩm nang giảm lỗi Timeout trong báo cáo đồng bộ](#6-cam-nang-giam-loi-timeout-trong-bao-cao-dong-bo)
- [7. Độ trễ dữ liệu báo cáo (Data Latency)](#7-do-tre-du-lieu-bao-cao-data-latency)
- [8. Cải tiến hiệu năng hệ thống báo cáo](#8-cai-tien-hieu-nang-he-thong-bao-cao)
- [9. Câu hỏi thường gặp về Reporting (FAQs)](#9-cau-hoi-thuong-gap-ve-reporting-faqs)
- [10. API đăng ký nhận dữ liệu báo cáo (Reporting Subscription API)](#10-api-dang-ky-nhan-du-lieu-bao-cao-reporting-subscription-api)
- [11. Danh mục Endpoint API Reference](#11-danh-muc-endpoint-api-reference)

---

<a id="doc-1775747476019266"></a>
<!-- doc_id: 1775747476019266 -->
<a id="1-chi-so-ho-tro-trong-bao-cao-business-center"></a>
<a id="2-bo-loc-ho-tro-trong-bao-cao-business-center"></a>
## 1. Chỉ số hỗ trợ trong Báo cáo Business Center

Trong báo cáo Business Center (sử dụng endpoint `/report/integrated/get/` hoặc `/report/task/create/` với `report_type = "BUSINESS_CENTER"`), bạn có thể truy vấn các nhóm chỉ số sau:

### Chỉ số thuộc tính tài khoản (Attribute metrics)
Cung cấp các thuộc tính cơ bản của tài khoản quảng cáo trực thuộc Business Center.

| Field | Type | Description | Detail |
|---|---|---|---|
| `advertiser_name` | string | Tên tài khoản quảng cáo | Tên hiển thị của từng tài khoản quảng cáo trực thuộc. |
| `timezone` | string | Múi giờ | Múi giờ của từng tài khoản quảng cáo. |

### Chỉ số dữ liệu cơ bản (Basic data metrics)
Cung cấp dữ liệu chi phí và hiệu suất cơ bản của quảng cáo.

| Field | Type | Description | Detail |
|---|---|---|---|
| `currency` | string | Tiền tệ | Đơn vị tiền tệ của tài khoản quảng cáo. |
| `spend` | string | Chi phí | Số tiền ước tính chi tiêu cho quảng cáo trong khoảng thời gian đã chọn. Tham chiếu hóa đơn để có số liệu cuối cùng chính xác. |
| `billed_cost` | string | Chi phí thực tính (Net cost) | Số tiền chi tiêu, không bao gồm tín dụng quảng cáo hoặc coupon được sử dụng. |
| `cash_spend` | string | Chi phí tiền mặt (Cash) | Chi phí tiền mặt mỗi ngày được cập nhật trong vòng 48 giờ sau khi kết thúc ngày đó (UTC-12). |
| `voucher_spend` | string | Chi phí voucher (Voucher) | Chi phí voucher mỗi ngày được cập nhật trong vòng 48 giờ sau khi kết thúc ngày đó (UTC-12). |
| `cashback_coupon_spend` | string | Chi phí coupon hoàn tiền (Cashback) | Coupon hoàn tiền sẽ trả lại một khoản số dư tiền mặt cố định sau khi chi tiêu. Giá trị coupon được cộng vào tài khoản vào ngày hôm sau sau khi số dư được chi tiêu. |
| `tax_spend` | string | Chi phí thuế (Tax) | Chi phí thuế mỗi ngày được cập nhật trong vòng 48 giờ sau khi kết thúc ngày đó (UTC-12). |
| `cpc` | string | CPC | Chi phí trung bình cho mỗi lượt nhấp (Cost per click). |
| `cpm` | string | CPM | Chi phí trung bình cho mỗi 1.000 lượt hiển thị (Cost per mille). |
| `impressions` | string | Lượt hiển thị | Số lần quảng cáo được hiển thị cho người dùng. |
| `clicks` | string | Lượt nhấp | Số lượt nhấp vào quảng cáo của bạn. |
| `ctr` | string | CTR (Tỷ lệ nhấp) | Tỷ lệ phần trăm người dùng nhìn thấy quảng cáo và nhấp vào đó. |
| `conversion` | string | Lượt chuyển đổi | Số lần quảng cáo đạt được kết quả, dựa trên mục tiêu và cài đặt đã chọn. |
| `cost_per_conversion` | string | CPA | Số tiền trung bình đã chi tiêu cho một lượt chuyển đổi. |
| `conversion_rate` | string | CVR (Tỷ lệ chuyển đổi) | Tỷ lệ phần trăm kết quả nhận được trên tổng số lượt nhấp vào quảng cáo. |
| `reach` | string | Số người tiếp cận | Số lượng người dùng duy nhất nhìn thấy quảng cáo ít nhất một lần (ước tính). |
| `real_time_conversion` | string | Chuyển đổi thời gian thực | Số lượt chuyển đổi tính theo thời điểm thực tế sự kiện chuyển đổi diễn ra. |
| `real_time_cost_per_conversion` | string | CPA thời gian thực | Chi phí trung bình cho mỗi chuyển đổi tính theo thời điểm thực tế sự kiện diễn ra. |
| `real_time_conversion_rate` | string | CVR thời gian thực | Tỷ lệ chuyển đổi tính theo thời điểm thực tế sự kiện diễn ra trên số lượt nhấp. |
| `account_type` | string | Loại tài khoản | Loại tài khoản quảng cáo. Giá trị hỗ trợ: `ADS_MANAGER` (trên TikTok Ads Manager), `RAP` (trên Reservation Ads Platform). |
| `skan_conversion` | string | Chuyển đổi SKAN | Số lần đạt kết quả theo SKAdNetwork (dành cho iOS). Dữ liệu có thể bị trễ hoặc không hoàn chỉnh do giới hạn của Apple SKAN. |
| `skan_cost_per_conversion` | string | CPA SKAN | Chi phí trung bình cho một chuyển đổi SKAN. |
| `skan_conversion_rate` | string | CVR SKAN | Tỷ lệ chuyển đổi SKAN trên tổng số lượt nhấp. |

### Chỉ số sự kiện trong ứng dụng (In-app events metrics)
Áp dụng cho các chiến dịch quảng bá ứng dụng thông thường (không phải Dedicated Campaigns).

| Field | Type | Description | Detail |
|---|---|---|---|
| `registration` | string | Đăng ký duy nhất | Số lượt đăng ký duy nhất được ghi nhận cho quảng cáo. |
| `cost_per_registration` | string | Chi phí mỗi lượt đăng ký | Chi phí trung bình cho mỗi lượt đăng ký duy nhất. |
| `registration_rate` | string | Tỷ lệ đăng ký | Tỷ lệ đăng ký trên số lượt cài đặt ứng dụng. |
| `app_install` | string | Lượt cài đặt ứng dụng | Số lượt cài đặt ứng dụng được phân bổ cho quảng cáo. |
| `cost_per_app_install` | string | Chi phí mỗi lượt cài đặt | Chi phí trung bình cho một lượt cài đặt ứng dụng. |
| `app_install_rate` | string | Tỷ lệ cài đặt | Tỷ lệ cài đặt trên tổng số lượt nhấp. |
| `purchase` | string | Lượt mua hàng duy nhất | Số lượt mua hàng duy nhất trong ứng dụng được phân bổ cho quảng cáo. |
| `cost_per_purchase` | string | Chi phí mỗi lượt mua hàng | Chi phí trung bình cho mỗi lượt mua hàng duy nhất. |
| `purchase_rate` | string | Tỷ lệ mua hàng | Tỷ lệ mua hàng trên số lượt cài đặt. |
| `total_purchase_value` | string | Tổng giá trị mua hàng | Tổng giá trị giao dịch mua hàng trong ứng dụng do quảng cáo mang lại. |
| `value_per_total_purchase` | string | Giá trị trung bình mỗi đơn | Giá trị trung bình của mỗi giao dịch mua hàng. |
| `real_time_app_install` | string | Cài đặt thời gian thực | Số lượt cài đặt ứng dụng tính theo thời điểm cài đặt diễn ra. |
| `real_time_app_install_cost` | string | Chi phí cài đặt thời gian thực | Chi phí trung bình mỗi lượt cài đặt thời gian thực. |
| `real_time_app_install_rate` | string | Tỷ lệ cài đặt thời gian thực | Tỷ lệ cài đặt thời gian thực trên tổng số lượt nhấp. |

### Chỉ số sự kiện ứng dụng iOS SKAN (iOS In-app event metrics)
Áp dụng cho chiến dịch Dedicated Campaigns trên iOS thông qua Apple SKAdNetwork.

| Field | Type | Description | Detail |
|---|---|---|---|
| `skan_app_install` | string | Cài đặt SKAN | Số lượt cài đặt ứng dụng ghi nhận qua SKAN API. |
| `skan_cost_per_app_install` | string | Chi phí mỗi lượt cài đặt SKAN | Chi phí trung bình cho mỗi lượt cài đặt qua SKAN. |
| `skan_registration` | string | Đăng ký SKAN | Số lượt đăng ký ứng dụng theo SKAN. |
| `skan_cost_per_registration` | string | Chi phí đăng ký SKAN | Chi phí trung bình mỗi lượt đăng ký SKAN. |
| `skan_registration_rate` | string | Tỷ lệ đăng ký SKAN | Tỷ lệ đăng ký SKAN trên số lượt cài đặt SKAN. |
| `skan_purchase` | string | Mua hàng SKAN | Số lượt mua hàng ghi nhận qua SKAN. |
| `skan_cost_per_purchase` | string | Chi phí mua hàng SKAN | Chi phí trung bình mỗi lượt mua hàng qua SKAN. |
| `skan_purchase_rate` | string | Tỷ lệ mua hàng SKAN | Tỷ lệ mua hàng SKAN trên số lượt cài đặt SKAN. |
| `skan_total_purchase` | string | Tổng số lượt mua hàng SKAN | Tổng số lần sự kiện mua hàng được ghi nhận qua SKAN. |
| `skan_cost_per_total_purchase` | string | Chi phí mỗi lượt mua tổng SKAN | Chi phí trên tổng số lượt mua hàng SKAN. |
| `skan_total_purchase_value` | string | Tổng giá trị mua hàng SKAN | Tổng doanh thu mua hàng ghi nhận qua SKAN. |
| `skan_total_registration` | string | Tổng số lượt đăng ký SKAN | Tổng số lần sự kiện đăng ký được ghi nhận qua SKAN. |
| `skan_cost_per_total_registration` | string | Chi phí mỗi lượt đăng ký tổng SKAN | Chi phí trên tổng số lượt đăng ký SKAN. |

### Chỉ số xem video (Video play metrics)
| Field | Type | Description | Detail |
|---|---|---|---|
| `video_views_p25` | string | Lượt xem 25% | Số lần video được phát đến 25% độ dài. |
| `video_views_p50` | string | Lượt xem 50% | Số lần video được phát đến 50% độ dài. |
| `video_views_p75` | string | Lượt xem 75% | Số lần video được phát đến 75% độ dài. |
| `video_views_p100` | string | Lượt xem 100% | Số lần video được phát hết 100% độ dài. |
| `video_watched_2s` | string | Lượt xem 2 giây | Số lần video được phát liên tục từ 2 giây trở lên. |
| `video_watched_6s` | string | Lượt xem 6 giây | Số lần video được phát liên tục từ 6 giây trở lên. |
| `contact_name` | string | Tên liên hệ | Tên người liên hệ đại diện tài khoản. |

---

<a id="doc-1775747484045313"></a>
<!-- doc_id: 1775747484045313 -->
## 2. Bộ lọc hỗ trợ trong Báo cáo Business Center

Trong báo cáo Business Center, bạn có thể truyền các điều kiện lọc thông qua trường `filtering` trong request body hoặc query string:

| Filter | Type | Description |
|---|---|---|
| `advertiser_id` | string | Lọc theo ID tài khoản quảng cáo trực thuộc Business Center. |
| `advertiser_name` | string | Lọc theo tên tài khoản quảng cáo. |
| `account_status` | string | Lọc theo trạng thái tài khoản quảng cáo. |
| `cost` | string | Lọc theo khoảng chi phí quảng cáo. |
| `owner_of_account` | string | Lọc theo chủ sở hữu tài khoản quảng cáo. |
| `currency_of_account` | string | Lọc theo loại tiền tệ của tài khoản quảng cáo. |
| `registered_area` | string | Lọc theo khu vực/quốc gia đăng ký tài khoản. |
| `platform_of_account` | string | Lọc theo nền tảng quản lý tài khoản (`ADS_MANAGER` hoặc `RAP`). |

---

<a id="doc-1803073629472770"></a>
<!-- doc_id: 1803073629472770 -->
<a id="3-bao-cao-gmv-max-ads-sap-ngung-ho-tro"></a>
## 3. Báo cáo GMV Max Ads (Sắp ngừng hỗ trợ)

> **Cảnh báo ngừng hỗ trợ (To-be-deprecated):** Loại báo cáo `GMV_MAX` độc lập sẽ sớm được tích hợp và thay thế hoàn toàn bởi các chỉ số GMV trong báo cáo cơ bản (`BASIC`) hoặc Upgraded Smart+ Campaign Reporting. Hãy lên kế hoạch chuyển đổi sớm.

Loại báo cáo GMV Max Ads cho phép theo dõi hiệu quả các chiến dịch tối ưu hóa tổng giá trị hàng hóa (Gross Merchandise Value) cho các nhà bán hàng TikTok Shop.

---

<a id="doc-1803073899092993"></a>
<!-- doc_id: 1803073899092993 -->
<a id="4-chieu-du-lieu-gmv-max-ads"></a>
## 4. Chiều dữ liệu GMV Max Ads

Các chiều dữ liệu (dimensions) được hỗ trợ cho loại báo cáo GMV Max:

| Dimension | Description |
|---|---|
| `advertiser_id` | ID tài khoản nhà quảng cáo. |
| `campaign_id` | ID chiến dịch quảng cáo GMV Max. |
| `stat_time_day` | Thời gian thống kê theo ngày (`YYYY-MM-DD`). |
| `country_code` | Mã quốc gia phân phối quảng cáo. |

---

<a id="doc-1803073913733121"></a>
<!-- doc_id: 1803073913733121 -->
<a id="5-chi-so-gmv-max-ads"></a>
## 5. Chỉ số GMV Max Ads

Các chỉ số (metrics) được hỗ trợ cho loại báo cáo GMV Max:

| Field | Type | Description |
|---|---|---|
| `campaign_name` | string | Tên chiến dịch quảng cáo GMV Max. |
| `spend` | string | Tổng chi phí tiêu hao của chiến dịch. |
| `billed_cost` | string | Chi phí thực tính sau khi trừ tín dụng khuyến mãi. |

---

<a id="doc-1738864817670145"></a>
<!-- doc_id: 1738864817670145 -->
<a id="6-cam-nang-giam-loi-timeout-trong-bao-cao-dong-bo"></a>
## 6. Cẩm nang giảm lỗi Timeout trong báo cáo đồng bộ

Báo cáo đồng bộ (`GET /open_api/v1.3/report/integrated/get/`) có giới hạn thời gian phản hồi nghiêm ngặt. Nếu truy vấn quét quá nhiều dữ liệu, hệ thống sẽ trả về lỗi **Gateway Timeout (HTTP 504)** hoặc mã lỗi `40001 / 40002`.

### Các nguyên tắc vàng để tránh Timeout:
1. **Thu hẹp khoảng thời gian truy vấn (`start_date` và `end_date`):**
   - Truy vấn có chiều `stat_time_day`: Chia nhỏ thành từng khoảng thời gian từ 3 đến 7 ngày thay vì truy vấn trọn 30 ngày.
   - Truy vấn theo giờ (`stat_time_hour`): Chỉ nên truy vấn trong vòng 1-2 ngày gần nhất.
2. **Hạn chế số lượng chiều dữ liệu (`dimensions`):**
   - Chỉ truyền các chiều thực sự cần thiết. Tránh kết hợp đồng thời nhiều chiều cấp sâu (ví dụ: `ad_id` + `stat_time_hour` + `country_code`).
3. **Lọc dữ liệu bằng `filtering`:**
   - Luôn sử dụng bộ lọc `campaign_ids` hoặc `adgroup_ids` để giới hạn phạm vi quét thay vì quét toàn bộ tài khoản.
4. **Giới hạn số lượng chỉ số (`metrics`):**
   - Chỉ yêu cầu các cột metrics bạn sẽ lưu vào cơ sở dữ liệu. Tránh truyền danh sách 50+ metrics cùng một lúc.
5. **Giảm `page_size`:**
   - Đặt `page_size` ở mức 100 đến 500 bản ghi mỗi trang thay vì tối đa 1.000 khi truy vấn dữ liệu chi tiết.
6. **Chuyển sang Báo cáo bất đồng bộ (Asynchronous Reports):**
   - Nếu tài khoản có hơn 10.000 quảng cáo hoặc cần dữ liệu lịch sử trên 30 ngày, bắt buộc sử dụng quy trình bất đồng bộ: `/report/task/create/` -> `/report/task/check/` -> `/report/task/download/`.

---

<a id="doc-1738864894606337"></a>
<!-- doc_id: 1738864894606337 -->
<a id="7-do-tre-du-lieu-bao-cao-data-latency"></a>
## 7. Độ trễ dữ liệu báo cáo (Data Latency)

Hiểu rõ độ trễ dữ liệu là yếu tố then chốt để xây dựng lịch trình trích xuất (ETL pipeline) dữ liệu chính xác và không bị thiếu số liệu.

### Bảng phân loại độ trễ theo từng loại báo cáo:

| Report Type | Thời gian cập nhật | Độ trễ ước tính | Lưu ý chốt số liệu |
|---|---|---|---|
| `Basic` (Cơ bản) | Liên tục trong ngày | 15 - 30 phút | Số liệu lượt nhấp, lượt xem video cập nhật gần thời gian thực. |
| `Audience` (Đối tượng) | Hằng ngày | 24 - 48 giờ | Phân tích theo độ tuổi, giới tính, sở thích cần thời gian tổng hợp mô hình. |
| `Playable` (Quảng cáo tương tác) | Hằng ngày | 12 - 24 giờ | Thống kê tương tác mini-game trong quảng cáo. |
| `DSA` (Quảng cáo tìm kiếm động) | Hằng ngày | 12 - 24 giờ | Thống kê từ khóa tìm kiếm và trang đích. |
| `Business Center` | Hằng ngày | 24 - 48 giờ (UTC-12) | Các khoản chi phí tiền mặt (`cash_spend`), voucher (`voucher_spend`), thuế (`tax_spend`) chốt sau 48 giờ. |
| `GMV Max` | Hằng ngày | 12 - 24 giờ | Doanh thu hoàn tất đơn hàng TikTok Shop cần thời gian đối soát. |

### Cửa sổ quy kết chuyển đổi (Attribution Window):
- Dữ liệu chuyển đổi (Conversions, ROAS, Purchase Value) có thể tiếp tục tăng lên trong suốt cửa sổ phân bổ (mặc định 7 ngày nhấp chuột, 1 ngày xem). Do đó, ETL pipeline nên chạy lại dữ liệu của 7 ngày trước đó mỗi ngày một lần để cập nhật các chuyển đổi phát sinh muộn.

---

<a id="doc-1757262274182145"></a>
<!-- doc_id: 1757262274182145 -->
<a id="8-cai-tien-hieu-nang-he-thong-bao-cao"></a>
## 8. Cải tiến hiệu năng hệ thống báo cáo

TikTok đã triển khai nhiều nâng cấp hạ tầng cho hệ thống Reporting API:
- **Tối ưu hóa chỉ mục (Indexing):** Tăng tốc độ lọc theo `campaign_id`, `adgroup_id`, `ad_id` lên gấp 3 lần.
- **Tách biệt luồng xử lý báo cáo lớn:** Tự động định tuyến các truy vấn nặng sang cụm máy chủ tính toán phân tán.
- **Hỗ trợ nén gzip:** Header `Accept-Encoding: gzip` giúp giảm 70% dung lượng truyền tải mạng cho các phản hồi JSON lớn.

---

<a id="doc-1738864850353154"></a>
<!-- doc_id: 1738864850353154 -->
<a id="9-cau-hoi-thuong-gap-ve-reporting-faqs"></a>
## 9. Câu hỏi thường gặp về Reporting (FAQs)

### Q1: Sự khác biệt giữa Báo cáo đồng bộ và Báo cáo bất đồng bộ là gì?
- **Báo cáo đồng bộ (`/report/integrated/get/`):** Phù hợp để hiển thị số liệu tức thời trên Dashboard, trích xuất dữ liệu nhanh trong ngày hoặc khoảng thời gian ngắn (< 30 ngày). Giới hạn tối đa 20.000 quảng cáo.
- **Báo cáo bất đồng bộ (`/report/task/create/`):** Phù hợp để kéo dữ liệu lớn, toàn bộ lịch sử (lên đến 365 ngày), tải tệp nén CSV. Không bị giới hạn 20.000 quảng cáo và không gặp lỗi HTTP 504 Timeout.

### Q2: Sự khác biệt giữa Reporting API và Creative Reporting API là gì?
- **Reporting API:** Hỗ trợ 4 cấp độ dữ liệu (`data_level`: campaign, adgroup, ad, advertiser), hỗ trợ gom nhóm chiều linh hoạt (`dimensions`), hỗ trợ cả đồng bộ và bất đồng bộ.
- **Creative Reporting API (`/creative/report/get/`):** Chỉ chạy ở cấp độ nội dung sáng tạo (`material_type`: `VIDEO`, `IMAGE`, `INSTANT_PAGE`), không hỗ trợ gom nhóm chiều.

### Q3: Làm thế nào để liên kết thông tin Ứng dụng giữa `/ad/get/` và API quản lý ứng dụng?
- Trong phản hồi của `/ad/get/`, bạn có trường `app_name`. Để lấy `app_id`, hãy gọi `/adgroup/get/` để lấy `app_id` liên kết với nhóm quảng cáo, sau đó gọi `/app/info/` để tra cứu đầy đủ chi tiết ứng dụng.

---

<a id="doc-1861445809243137"></a>
<!-- doc_id: 1861445809243137 -->
<a id="10-api-dang-ky-nhan-du-lieu-bao-cao-reporting-subscription-api"></a>
## 10. API đăng ký nhận dữ liệu báo cáo (Reporting Subscription API)

### Reporting Subscription API là gì?
Reporting Subscription API cho phép các nhà phát triển đăng ký nhận báo cáo dữ liệu được tự động tạo, giảm đáng kể số lượng request định kỳ đối với khối lượng dữ liệu lớn.
Các báo cáo này có thể được gửi định kỳ mỗi **5 phút, 15 phút, 30 phút hoặc 60 phút**. Ví dụ: nếu bạn cấu hình tần suất mỗi 5 phút, khi bất kỳ chỉ số báo cáo nào trong số `spend`, `impressions`, `clicks`, và `video_play_actions` của bất kỳ tài khoản quảng cáo nào bạn đã đăng ký có sự thay đổi trong 5 phút vừa qua, bạn sẽ nhận được tối đa một thông báo Webhook.

### Lợi ích cốt lõi:
- **Tự động nhận dữ liệu qua Webhook hoặc Email:** Thay vì phải liên tục gọi 3 endpoint bất đồng bộ (`/report/task/create/`, `/report/task/check/`, `/report/task/download/`), hệ thống chủ động đẩy dữ liệu khi có thay đổi.
- **Tùy biến tần suất linh hoạt:** Cho phép lựa chọn chu kỳ nhận dữ liệu phù hợp với nhu cầu vận hành thực tế.

---

<a id="doc-1740649343188994"></a>
<!-- doc_id: 1740649343188994 -->
<a id="11-danh-muc-endpoint-api-reference"></a>
## 11. Danh mục Endpoint API Reference

Phân hệ Reporting bao gồm các endpoint nòng cốt sau:
* [Chạy báo cáo đồng bộ (`GET /open_api/v1.3/report/integrated/get/`)](../12-api-reference/58-reporting.md#doc-1740302848100353)
* [Tạo tác vụ báo cáo bất đồng bộ (`POST /open_api/v1.3/report/task/create/`)](../12-api-reference/58-reporting.md#doc-1740302766489602)
* [Lấy trạng thái tác vụ báo cáo bất đồng bộ (`GET /open_api/v1.3/report/task/check/`)](../12-api-reference/58-reporting.md#doc-1740302781443073)
* [Tải về kết quả báo cáo bất đồng bộ (`GET /open_api/v1.3/report/task/download/`)](../12-api-reference/58-reporting.md#doc-1740302808815618)
* [Hủy tác vụ báo cáo bất đồng bộ (`POST /open_api/v1.3/report/task/cancel/`)](../12-api-reference/58-reporting.md#doc-1803615367145537)
---

## 12. Hướng dẫn thực hành: Kịch bản trích xuất Báo cáo tự động (ETL Pipeline)

Đoạn mã Python dưới đây minh họa quy trình trích xuất dữ liệu báo cáo đa cấp độ chuẩn doanh nghiệp, áp dụng các kỹ thuật chống timeout và xử lý phân trang tự động:

```python
import time
import requests
import json
from datetime import datetime, timedelta

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ADVERTISER_ID = "YOUR_ADVERTISER_ID"
BASE_URL = "https://business-api.tiktok.com/open_api/v1.3"

headers = {
    "Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}

def fetch_integrated_report(advertiser_id, start_date, end_date, metrics, dimensions):
    """
    Trích xuất báo cáo đồng bộ với cơ chế xử lý phân trang và giới hạn 30 ngày.
    Áp dụng Exponential Backoff khi gặp lỗi giới hạn tần suất (Rate Limit 40001).
    """
    url = f"{BASE_URL}/report/integrated/get/"
    page = 1
    page_size = 500
    all_records = []
    
    while True:
        params = {
            "advertiser_id": advertiser_id,
            "report_type": "BASIC",
            "data_level": "AUCTION_AD",
            "dimensions": json.dumps(dimensions),
            "metrics": json.dumps(metrics),
            "start_date": start_date,
            "end_date": end_date,
            "page": page,
            "page_size": page_size
        }
        
        retries = 3
        while retries > 0:
            response = requests.get(url, headers=headers, params=params)
            res_data = response.json()
            code = res_data.get("code")
            
            if code == 0:
                data = res_data.get("data", {})
                records = data.get("list", [])
                all_records.extend(records)
                page_info = data.get("page_info", {})
                total_page = page_info.get("total_page", 1)
                
                print(f"Trích xuất thành công trang {page}/{total_page} ({len(records)} dòng)")
                
                if page >= total_page:
                    return all_records
                page += 1
                break
            elif code == 40001:  # Rate limit exceeded
                wait_time = (4 - retries) * 5
                print(f"Chạm giới hạn tần suất gọi API, chờ {wait_time}s...")
                time.sleep(wait_time)
                retries -= 1
            elif code == 40002:  # Tham số không hợp lệ
                print(f"Lỗi tham số truy vấn: {res_data.get(message)}")
                return all_records
            else:
                print(f"Lỗi hệ thống: {code} - {res_data.get(message)}")
                return all_records

if __name__ == "__main__":
    today = datetime.now().strftime("%Y-%m-%d")
    seven_days_ago = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
    
    selected_metrics = ["spend", "impressions", "clicks", "ctr", "cpc", "conversion", "cost_per_conversion"]
    selected_dims = ["stat_time_day", "ad_id"]
    
    records = fetch_integrated_report(ADVERTISER_ID, seven_days_ago, today, selected_metrics, selected_dims)
    print(f"Tổng số bản ghi thu thập được: {len(records)}")
```
