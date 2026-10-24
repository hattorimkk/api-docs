# Hướng dẫn quản lý chiến dịch (tóm tắt các tài liệu dài)

Tài liệu này tổng hợp và cô đọng các hướng dẫn kỹ thuật chuyên sâu về quản lý chiến dịch quảng cáo TikTok, bao gồm câu hỏi thường gặp về di chuyển Upgraded Smart+, các giải pháp an toàn thương hiệu (Brand Safety), tối ưu hóa dựa trên giá trị (Value-Based Optimization), cấu hình cửa sổ phân bổ (Attribution window), bảng tra cứu trạng thái phụ (secondary status), cơ chế liên kết sâu (Deeplink) và trang sản phẩm tùy chỉnh (Custom Product Pages) trên Apple App Store. Mỗi mục tóm tắt nêu rõ mục đích, cách sử dụng, tham số trọng tâm và liên kết đến tài liệu gốc chính thức.

## Câu hỏi thường gặp về Upgraded Smart+ Campaign (`FAQs`)
<a id="doc-1854104036724929"></a>
<!-- doc_id: 1854104036724929 -->

- **Mục đích & Khi nào dùng:** Tài liệu này giải đáp các thắc mắc cốt lõi của nhà phát triển và nhà quảng cáo khi chuyển đổi từ chiến dịch thủ công (Manual) hoặc Smart+ cũ sang trải nghiệm Upgraded Smart+ Campaign. Áp dụng khi bạn cần kiểm tra xem tài khoản quảng cáo của mình đã đủ điều kiện tiếp cận Upgraded Smart+ hay chưa, cách phân biệt dữ liệu giữa các loại chiến dịch và cách xử lý lỗi khi gọi API.
- **Endpoint liên quan:**
  - Lấy thông tin chiến dịch: [/campaign/get/](../12-api-reference/24-campaign.md#doc-1739315828649986)
  - Lấy thông tin nhóm quảng cáo: [/smart_plus/adgroup/get/](../12-api-reference/62-upgraded-smartplus-p2.md#doc-1843314879617026)
  - Lấy thông tin quảng cáo: [/ad/get/](../12-api-reference/02-ads-p1.md#doc-1735735588640770) hoặc [/smart_plus/ad/get/](../12-api-reference/62-upgraded-smartplus-p4.md#doc-1843317378982914)
  - Báo cáo tài liệu sáng tạo: [/smart_plus/material_report/overview/](../12-api-reference/62-upgraded-smartplus-p6.md#doc-1843317489576961)
- **Tham số then chốt & Lưu ý quan trọng:**
  - Nhận diện loại chiến dịch thông qua trường `campaign_automation_type` trong phản hồi (`MANUAL`, `SMART_PLUS`, `UPGRADED_SMART_PLUS`).
  - Ở cấp quảng cáo Upgraded Smart+, trường `smart_plus_ad_id` và `ad_ids_v2` được sử dụng để lọc và định danh thay cho `ad_id` truyền thống.
  - Không thể sử dụng endpoint cũ như `/campaign/update/` hay `/campaign/spc/update/` để cập nhật chiến dịch Upgraded Smart+; bạn bắt buộc phải gọi các endpoint chuyên biệt thuộc họ `/smart_plus/`.
- **Tài liệu chính thức:** Xem chi tiết đầy đủ tại [TikTok Portal - Upgraded Smart+ FAQs](https://business-api.tiktok.com/portal/docs?id=1854104036724929).

## An toàn thương hiệu (`Brand safety`)
<a id="doc-1739381752981505"></a>
<!-- doc_id: 1739381752981505 -->

> Đường dẫn: Marketing API > Campaign Management > Guides > Ad group > Brand safety

- **Mục đích & Khi nào dùng:** Bảo vệ uy tín thương hiệu khi phân phối quảng cáo trên TikTok bằng cách ngăn chặn quảng cáo xuất hiện cạnh các nội dung không phù hợp hoặc nhạy cảm. Được áp dụng khi thiết lập nhóm quảng cáo cho các chiến dịch có yêu cầu nghiêm ngặt về an toàn thương hiệu theo tiêu chuẩn GARM (Global Alliance for Responsible Media).
- **Endpoint liên quan:**
  - Tạo nhóm quảng cáo: [/adgroup/create/](../12-api-reference/07-ad-groups-p2.md#doc-1739499616346114)
  - Cập nhật nhóm quảng cáo: [/adgroup/update/](../12-api-reference/07-ad-groups-p3.md#doc-1739586761631745)
- **Tham số then chốt & Lưu ý quan trọng:**
  - `brand_safety_type`: Bộ lọc kiểm soát nội dung trước đấu thầu của TikTok (TikTok Inventory Filter), hỗ trợ các cấp độ: `EXPANDED_INVENTORY` (Mở rộng), `STANDARD_INVENTORY` (Tiêu chuẩn), `LIMITED_INVENTORY` (Giới hạn).
  - `brand_safety_partner`: Đối tác bên thứ ba đo lường an toàn thương hiệu sau đấu thầu (`IAS`, `DOUBLE_VERIFY`, `ZEFR`, `ORACLE_MOAT`).
  - Hầu hết các giải pháp Brand Safety nâng cao từ bên thứ ba đều yêu cầu duyệt allowlist theo từng sản phẩm cụ thể.
- **Tài liệu chính thức:** Xem chi tiết đầy đủ tại [TikTok Portal - Brand Safety](https://business-api.tiktok.com/portal/docs?id=1739381752981505).

## Tối ưu hóa dựa trên giá trị trong Chiến dịch thủ công (`Enable Value-Based Optimization in Manual Campaigns`)
<a id="doc-1770019181843458"></a>
<!-- doc_id: 1770019181843458 -->

> Đường dẫn: Marketing API > Campaign Management > Guides > Ad group > Bidding > Enable Value-Based Optimization in Manual Campaigns

- **Mục đích & Khi nào dùng:** Tối ưu hóa dựa trên giá trị (Value-Based Optimization - VBO) hướng tới nhóm người dùng có khả năng tạo ra giá trị chuyển đổi (doanh thu/ROAS) cao nhất thay vì chỉ tối ưu số lượng chuyển đổi thuần túy. Áp dụng cho các chiến dịch thủ công với mục tiêu Chuyển đổi trang web (Web Conversions) hoặc Cài đặt ứng dụng (App Promotion).
- **Endpoint liên quan:**
  - Tạo nhóm quảng cáo: [/adgroup/create/](../12-api-reference/07-ad-groups-p2.md#doc-1739499616346114)
  - Cập nhật nhóm quảng cáo: [/adgroup/update/](../12-api-reference/07-ad-groups-p3.md#doc-1739586761631745)
- **Tham số then chốt & Lưu ý quan trọng:**
  - `optimization_goal`: Đặt thành `VALUE`.
  - `deep_bid_type`: Chiến lược đặt giá thầu giá trị, bao gồm `VO_MIN_ROAS` (ROAS tối thiểu - yêu cầu truyền `roas_bid`) hoặc `VO_HIGHEST_VALUE` (Giá trị cao nhất trong phạm vi ngân sách).
  - Điều kiện tiên quyết: Pixel hoặc App Event Source phải tích lũy tối thiểu 30 sự kiện chuyển đổi mua hàng (Purchase) có giá trị hợp lệ trong 7 ngày gần nhất để thuật toán học máy kích hoạt VBO.
- **Tài liệu chính thức:** Xem chi tiết đầy đủ tại [TikTok Portal - Manual VBO](https://business-api.tiktok.com/portal/docs?id=1770019181843458).

## Tối ưu hóa dựa trên giá trị trong Chiến dịch Smart+ (`Enable Value-Based Optimization in Smart+ Campaigns`)
<a id="doc-1840137502583809"></a>
<!-- doc_id: 1840137502583809 -->

> Đường dẫn: Marketing API > Campaign Management > Guides > Ad group > Bidding > Enable Value-Based Optimization in Smart+ Campaigns

- **Mục đích & Khi nào dùng:** Kích hoạt tính năng VBO kết hợp với tự động hóa AI toàn diện của Smart+ Campaign, giúp tối đa hóa tổng giá trị chuyển đổi mua sắm hoặc duy trì ROAS mục tiêu trên quy mô lớn mà không cần tinh chỉnh thủ công từng nhóm đối tượng.
- **Endpoint liên quan:**
  - Tạo chiến dịch Smart+: [/smart_plus/campaign/create/](../12-api-reference/62-upgraded-smartplus-p1.md#doc-1843312852800706) hoặc [/campaign/spc/create/](../12-api-reference/61-to-be-deprecated-legacy-smartplus.md#doc-1767334204047362)
- **Tham số then chốt & Lưu ý quan trọng:**
  - Thiết lập chiến lược đấu thầu giá trị thông qua `bid_type` và `deep_bid_type`.
  - Hệ thống tự động phân bổ ngân sách và kết hợp sáng tạo nội dung để nhắm tới các phân khúc khách hàng đem lại giá trị giỏ hàng cao nhất.
- **Tài liệu chính thức:** Xem chi tiết đầy đủ tại [TikTok Portal - Smart+ VBO](https://business-api.tiktok.com/portal/docs?id=1840137502583809).

## Cửa sổ phân bổ và cách tính sự kiện (`Attribution window and event count`)
<a id="doc-1777694366654465"></a>
<!-- doc_id: 1777694366654465 -->

> Đường dẫn: Marketing API > Campaign Management > Guides > Ad group > Attribution window and event count

- **Mục đích & Khi nào dùng:** Xác định khoảng thời gian mà các hành động chuyển đổi của người dùng được tính cho quảng cáo TikTok sau khi nhấp chuột (Click-Through) hoặc sau khi xem video quảng cáo (View-Through), cũng như cách tính số lần ghi nhận sự kiện chuyển đổi (chỉ tính 1 lần hay mỗi lần phát sinh).
- **Endpoint liên quan:**
  - Tạo nhóm quảng cáo: [/adgroup/create/](../12-api-reference/07-ad-groups-p2.md#doc-1739499616346114)
  - Cập nhật nhóm quảng cáo: [/adgroup/update/](../12-api-reference/07-ad-groups-p3.md#doc-1739586761631745)
- **Tham số then chốt & Lưu ý quan trọng:**
  - `click_attribution_window`: Cửa sổ phân bổ nhấp chuột (ví dụ: `ONE_DAY`, `SEVEN_DAYS`, `FOURTEEN_DAYS`, `TWENTY_EIGHT_DAYS`).
  - `view_attribution_window`: Cửa sổ phân bổ lượt xem (`OFF`, `ONE_DAY`, `SEVEN_DAYS`).
  - `event_count_type`: Cơ chế tính sự kiện chuyển đổi: `ONCE` (chỉ ghi nhận 1 lần chuyển đổi đầu tiên trên mỗi phiên nhấp) hoặc `EVERY_TIME` (ghi nhận tất cả các chuyển đổi lặp lại, thường dùng cho thương mại điện tử).
- **Tài liệu chính thức:** Xem chi tiết đầy đủ tại [TikTok Portal - Attribution Window](https://business-api.tiktok.com/portal/docs?id=1777694366654465).

## Trạng thái phụ được hỗ trợ cho trạng thái chính (`Supported secondary statuses for a primary status`)
<a id="doc-1757239620352002"></a>
<!-- doc_id: 1757239620352002 -->

> Đường dẫn: Marketing API > Campaign Management > Guides > Ad group > Supported secondary statuses for a primary status

- **Mục đích & Khi nào dùng:** Bảng tra cứu toàn diện mối quan hệ ánh xạ giữa trạng thái hoạt động chính (`primary_status`) và trạng thái chi tiết phụ (`secondary_status`) ở cả 3 cấp độ (Chiến dịch, Nhóm quảng cáo, Quảng cáo) cho các chiến dịch thông thường, chiến dịch Promote và chiến dịch GMV Max. Giúp lập trình viên xử lý luồng hiển thị giao diện và logic thông báo lỗi chính xác.
- **Endpoint liên quan:**
  - [/campaign/get/](../12-api-reference/24-campaign.md#doc-1739315828649986), [/adgroup/get/](../12-api-reference/07-ad-groups-p1.md#doc-1739314558673922), [/ad/get/](../12-api-reference/02-ads-p1.md#doc-1735735588640770)
- **Tham số then chốt & Lưu ý quan trọng:**
  - Với `primary_status` = `STATUS_DELIVERY_OK` (Đang phân phối bình thường): các trạng thái phụ có thể là `STATUS_DELIVERY_OK`, `STATUS_IN_IMPRESSION`, `STATUS_SCHEDULED`, v.v.
  - Với `primary_status` = `STATUS_AUDIT` (Đang kiểm duyệt): trạng thái phụ thể hiện tiến trình duyệt (`STATUS_AUDITING`) hoặc bị từ chối (`STATUS_AUDIT_DENY`).
  - Với `primary_status` = `STATUS_DISABLE` (Bị tạm dừng): trạng thái phụ thể hiện nguyên nhân dừng do người dùng tắt, vượt ngân sách ngày, hoặc tài khoản hết số dư.
- **Tài liệu chính thức:** Xem chi tiết đầy đủ tại [TikTok Portal - Secondary Statuses](https://business-api.tiktok.com/portal/docs?id=1757239620352002).

## Liên kết sâu (`Deeplink`)
<a id="doc-1779541971843073"></a>
<!-- doc_id: 1779541971843073 -->

> Đường dẫn: Marketing API > Campaign Management > Guides > Ad > Deeplink

- **Mục đích & Khi nào dùng:** Dẫn trực tiếp người dùng đã cài đặt ứng dụng vào một trang đích cụ thể trong ứng dụng di động (ví dụ trang chi tiết sản phẩm hoặc chương trình khuyến mãi) thay vì chỉ mở màn hình chính, từ đó rút ngắn hành trình khách hàng và tăng tỷ lệ chuyển đổi.
- **Endpoint liên quan:**
  - Tạo quảng cáo: [/ad/create/](../12-api-reference/02-ads-p1.md#doc-1739953377508354)
  - Cập nhật quảng cáo: [/ad/update/](../12-api-reference/02-ads-p2.md#doc-1739953405142018)
- **Tham số then chốt & Lưu ý quan trọng:**
  - Hỗ trợ 2 loại deeplink: **Non-deferred deeplink** (dành cho người dùng đã cài app, qua Custom URL Scheme `scheme://` hoặc Universal Link / App Link) và **Deferred deeplink** (dành cho người dùng chưa cài app, kích hoạt qua đối tác đo lường MMP sau khi cài đặt).
  - `deeplink_type`: Loại liên kết sâu (`NORMAL`, `DEFERRED`).
  - `fallback_type`: Cơ chế dự phòng khi người dùng không mở được liên kết sâu (`APP_INSTALL` dẫn đến kho ứng dụng hoặc `WEBSITE` dẫn đến trang web).
- **Tài liệu chính thức:** Xem chi tiết đầy đủ tại [TikTok Portal - Deeplink](https://business-api.tiktok.com/portal/docs?id=1779541971843073).

## Trang sản phẩm tùy chỉnh (`Custom Product Pages`)
<a id="doc-1798658439859202"></a>
<!-- doc_id: 1798658439859202 -->

> Đường dẫn: Marketing API > Campaign Management > Guides > Ad > Custom Product Pages

- **Mục đích & Khi nào dùng:** Tận dụng tính năng Custom Product Pages (CPP) của Apple App Store trên thiết bị iOS 14+ để điều chỉnh ảnh chụp màn hình (screenshots), văn bản quảng cáo và bản xem trước ứng dụng trên kho App Store khớp chính xác với nội dung và thông điệp của quảng cáo TikTok. Giúp tăng tính đồng nhất và nâng cao tỷ lệ chuyển đổi cài đặt ứng dụng.
- **Endpoint liên quan:**
  - Tạo quảng cáo: [/ad/create/](../12-api-reference/02-ads-p1.md#doc-1739953377508354)
  - Cập nhật quảng cáo: [/ad/update/](../12-api-reference/02-ads-p2.md#doc-1739953405142018)
- **Tham số then chốt & Lưu ý quan trọng:**
  - Áp dụng cho mục tiêu `APP_PROMOTION` trên hệ điều hành iOS.
  - Cần tạo và phát hành trước các trang CPP trên tài khoản Apple App Store Connect để lấy URL tương ứng.
  - Cấu hình qua tham số `custom_product_page_url` ở cấp quảng cáo.
  - Tính năng hiện được quản lý thông qua danh sách cho phép (allowlist).
- **Tài liệu chính thức:** Xem chi tiết đầy đủ tại [TikTok Portal - Custom Product Pages](https://business-api.tiktok.com/portal/docs?id=1798658439859202).
