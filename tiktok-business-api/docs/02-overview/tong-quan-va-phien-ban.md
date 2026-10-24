# Tổng quan, phiên bản và thay đổi v1.3

> Phân hệ: guide:Overview.
> Tài liệu biên dịch kỹ thuật chi tiết theo chuẩn TikTok Business API v1.3.

---

## Mục lục điều hướng
- [1. Tổng quan (Overview) (#doc-1735712062490625)](#doc-1735712062490625)
- [2. Quản lý phiên bản (Versioning) (#doc-1740029169927169)](#doc-1740029169927169)
- [3. Lộ trình phát hành (Timelines) (#doc-1740578661644289)](#doc-1740578661644289)
- [4. Cập nhật lớn trong v1.3 (V1.3 updates) (#doc-1740579480076290)](#doc-1740579480076290)
- [5. Hướng dẫn di chuyển lên v1.3 (Migrate to v1.3) (#doc-1740591846408194)](#doc-1740591846408194)
- [6. Di chuyển API quản lý chiến dịch (Migrate Campaign Management APIs) (#doc-1749537346290689)](#doc-1749537346290689)

---

<a id="doc-1735712062490625"></a>
<!-- doc_id: 1735712062490625 -->
<!-- doc_id: 1735712062490625 -->
# Tổng quan (Overview)
> Đường dẫn: Tổng quan

TikTok API for Business là chuỗi các dịch vụ giao diện lập trình được TikTok for Business cung cấp cho các nhà phát triển. Thông qua việc tích hợp và gọi API, các nhà phát triển có thể tận dụng giao diện này để tương tác theo quy mô lớn với [Trình quản lý quảng cáo TikTok (TikTok Ads Manager)](https://ads.tiktok.com/i18n/home), tài khoản TikTok doanh nghiệp và các tính năng của [Thị trường nhà sáng tạo TikTok One (TTO Creator Marketplace)](https://ads.tiktok.com/creative/creatormarketplace). Hệ sinh thái TikTok API for Business được phân chia thành các nhóm API chính sau:
- **Marketing API**: Tương tác với mọi chức năng của Trình quản lý quảng cáo TikTok theo quy mô lớn, cho phép lập trình viên truy vấn dữ liệu theo chương trình, tạo và quản trị chiến dịch, nhóm quảng cáo, nội dung sáng tạo, và tự động hóa quy trình nghiệp vụ.
- **Organic API**: Xây dựng công cụ cho các thương hiệu quản lý sự hiện diện tự nhiên (organic) trên TikTok và mở rộng ảnh hưởng thương hiệu, tạo nền tảng thúc đẩy tăng trưởng thông qua quảng cáo trả phí (bao gồm Spark Ads và Non-Spark Ads). Organic API bao gồm các phân hệ: Accounts, Mentions, TikTok One (TTO), Discovery và Spark Ads Recommendation API.
- **Business Messaging API**: Tích hợp khả năng nhắn tin trực tiếp để kết nối trực tiếp với người dùng TikTok. Sử dụng API này để gửi/nhận tin nhắn theo thời gian thực, thiết lập phản hồi tự động giúp trao đổi nhanh chóng và quản lý luồng hội thoại một cách chuyên nghiệp.

# Tại sao nên sử dụng TikTok API for Business?
Các nhà phát triển có thể sử dụng TikTok API for Business để xây dựng các chức năng nâng cao toàn diện sự hiện diện trên TikTok — từ tự động hóa quảng cáo, tối ưu hóa chiến dịch thông minh đến quản lý nội dung tự nhiên và tương tác khách hàng theo thời gian thực. Dù mục tiêu của bạn là mở rộng quy mô quảng cáo, xây dựng kết nối chân thực qua nội dung tự nhiên hay tạo trải nghiệm hội thoại liền mạch, TikTok API for Business cung cấp đầy đủ công cụ để xây dựng, mở rộng và tối ưu hóa toàn bộ chiến lược TikTok với độ chính xác và hiệu quả cao nhất.

**Bộ giải pháp API toàn diện này đặc biệt hữu ích cho các doanh nghiệp quản trị nhiều tài khoản, triển khai chiến lược nội dung đa dạng và có nhu cầu chăm sóc khách hàng phức tạp.** Bằng cách tận dụng các tính năng API, doanh nghiệp không chỉ nâng cấp năng lực quảng cáo mà còn kiến tạo sự hiện diện tự nhiên vững chắc và duy trì tương tác ý nghĩa với khách hàng tiềm năng.

- **Marketing API**: Thúc đẩy gia tăng hiệu suất chiến dịch, tối ưu hiệu quả vận hành và mở rộng quy mô quản trị chiến dịch trên TikTok, mang lại trải nghiệm cá nhân hóa và phù hợp cho khách hàng tiềm năng. Ngoài ra, lập trình viên có quyền truy cập độc quyền vào các tính năng API-First tiên tiến như Super Split Test API.
- **Organic API**: Tinh chỉnh chiến lược nội dung tự nhiên, phát hiện cơ hội hợp tác với các nhà sáng tạo nội dung (creator), và xác định nội dung chất lượng xứng đáng được đẩy mạnh qua quảng cáo trả phí. Về bản chất, Organic API thu hẹp khoảng cách giữa thành công tự nhiên và tăng trưởng trả phí, giúp thương hiệu tối đa hóa tác động và tỷ suất hoàn vốn (ROI) trên TikTok.
- **Business Messaging API**: Tối ưu hóa chiến lược hội thoại, khai thác sức mạnh tin nhắn thời gian thực để thắt chặt mối quan hệ với người dùng, đồng thời xác định các điểm chạm giao tiếp hỗ trợ hiệu quả cho chiến dịch quảng cáo trả phí.

# Đối tượng nên sử dụng TikTok API for Business?
- **Công ty công nghệ (Technology Company)**: Các công ty phát triển phần mềm SaaS/công cụ hỗ trợ người dùng tạo lập, triển khai và đo lường chiến dịch quảng cáo TikTok.
- **Nhà quảng cáo trực tiếp (Direct Advertiser)**: Các doanh nghiệp tự quản lý và phân tích hiệu suất quảng cáo của chính mình, mong muốn tích hợp tự động hóa qua TikTok API for Business.
- **Đại lý quảng cáo (Agency)**: Các đối tác truyền thông, đại lý chuyên hoạch định, sáng tạo nội dung và quản trị đa dạng chiến dịch quảng cáo cho khách hàng của họ.

---

<a id="doc-1740029169927169"></a>
<!-- doc_id: 1740029169927169 -->
<!-- doc_id: 1740029169927169 -->
# Quản lý phiên bản (Versioning)
> Đường dẫn: Tổng quan > Quản lý phiên bản

Phiên bản chính thức và mới nhất của TikTok API for Business là **v1.3**.

TikTok API for Business v1.3 được phát hành từ ngày 15 tháng 8 năm 2022. Các nhà phát triển có thời hạn 1 năm để chuyển đổi từ v1.2 lên v1.3. Kể từ sau ngày 15 tháng 8 năm 2023, phiên bản v1.2 đã ngừng nhận mọi bản cập nhật và hỗ trợ kỹ thuật. Để tránh gián đoạn dịch vụ, bạn cần đảm bảo toàn bộ lệnh gọi API được chuyển đổi sang phiên bản v1.3. **Xem chi tiết các thay đổi lớn trong v1.3 tại [Cập nhật v1.3](tong-quan-va-phien-ban.md#doc-1740579480076290).**

**Cơ chế đánh phiên bản hoạt động như thế nào?**
Chúng tôi chỉ áp dụng các thay đổi phá vỡ tương thích (breaking changes) trên các phiên bản API mới, và tuyệt đối không áp dụng breaking changes trên các phiên bản cũ đang chạy. Nhà phát triển được cung cấp khoảng thời gian chuyển tiếp hợp lý để thích ứng hoặc nâng cấp (ví dụ: thời hạn 1 năm để di chuyển từ v1.2 lên v1.3). Khi hết hạn chuyển tiếp, phiên bản cũ sẽ chính thức ngừng hoạt động (deprecated) và mọi lệnh gọi đến phiên bản đó sẽ bị từ chối.

**Lộ trình phát hành của từng phiên bản?**
Xem chi tiết tại [Lộ trình phát hành (Timelines)](tong-quan-va-phien-ban.md#doc-1740578661644289).

**TikTok xử lý tính năng mới như thế nào?**
Kể từ khi v1.3 phát hành, mọi tính năng mới, trường tham số bổ sung và tối ưu hóa hệ thống đều chỉ được cập nhật trên phiên bản v1.3.

**Các phiên bản được thể hiện như thế nào trong tài liệu?**
Tài liệu của phiên bản cũ (v1.2) được đánh dấu là không còn dùng nữa (deprecated) kể từ tháng 8/2023 khi API v1.2 chính thức hết hạn.

**Có phải xin lại quyền truy cập (API scope) khi nâng cấp từ v1.2 lên v1.3 không?**
Không cần thiết. Nếu ứng dụng của bạn đã được cấp quyền cho nhóm API tương ứng (ví dụ: Quản lý quảng cáo - Ads Management), phạm vi quyền hạn đó sẽ tự động có hiệu lực trên v1.3. Xem [v1.3 major updates - Cập nhật URL](tong-quan-va-phien-ban.md#doc-1740579480076290) để biết danh sách các URL được chuẩn hóa trong v1.3.

**Có cần đăng ký lại danh sách cho phép (allowlist) khi di chuyển sang v1.3 không?**
Không cần. Nếu tài khoản của bạn đã được cấp quyền truy cập các tính năng trong danh sách cho phép (allowlist-only) ở v1.2, bạn có thể tiếp tục sử dụng trực tiếp các tính năng đó trên v1.3.

---

<a id="doc-1740578661644289"></a>
<!-- doc_id: 1740578661644289 -->
<!-- doc_id: 1740578661644289 -->
# Lộ trình phát hành (Timelines)
> Đường dẫn: Tổng quan > Quản lý phiên bản > Lộ trình phát hành

Bảng dưới đây liệt kê các mốc thời gian phát hành và ngày ngừng hoạt động chính thức của từng phiên bản API:

| Version | Ngày phát hành | Hỗ trợ đến |
|---|---|---|
| v1.3 | 15/08/2022 | Đang hoạt động (TBD) |
| v1.2 | 19/03/2021 | 15/08/2023 |
| v1.1 | 19/08/2020 | 29/07/2021 |
| v1.0 | - | 20/01/2021 |

---

<a id="doc-1740579480076290"></a>
<!-- doc_id: 1740579480076290 -->
<!-- doc_id: 1740579480076290 -->
# Cập nhật lớn trong v1.3 (V1.3 updates)
> Đường dẫn: Tổng quan > Cập nhật lớn trong v1.3

Dựa trên phản hồi từ cộng đồng nhà phát triển, TikTok đã ra mắt phiên bản TikTok API for Business v1.3. Bản phát hành này hướng tới việc nâng cao trải nghiệm nhà phát triển, giới thiệu các tính năng tiên phong (API First) và đồng bộ tính năng hoàn toàn với Trình quản lý quảng cáo TikTok (TikTok Ads Manager).

# Mốc thời gian
Phiên bản v1.3 chính thức ra mắt ngày 15/08/2022, và v1.2 đã ngừng hoạt động vào ngày 15/08/2023. Kể từ thời điểm này, mọi lệnh gọi đến v1.2 đều bị từ chối vĩnh viễn.

# Các thay đổi cốt lõi

## Thay đổi số phiên bản trong mọi đường dẫn URL
Bạn cần cập nhật tiền tố phiên bản trong mọi endpoint từ `/open_api/v1.2/` thành `/open_api/v1.3/`.

## Nâng cao trải nghiệm lập trình viên
Chúng tôi đã thực hiện nhiều cải tiến quan trọng nhằm chuẩn hóa giao diện lập trình trên toàn bộ hệ thống API:

### Chuyển đổi toàn bộ định danh ID sang kiểu chuỗi (string)
Tất cả các tham số ID trước đây có kiểu số nguyên dài (long integer) ở v1.2 đã được chuyển thành kiểu chuỗi (string) trong v1.3. Điều này giải quyết triệt để lỗi tràn số nguyên trên các thư viện client như Node.js hoặc JavaScript.

### Chuẩn hóa tên tham số sang dạng snake_case
Trong v1.3, mọi tham số API đều tuân thủ quy ước đặt tên nhất quán `snake_case`, rõ ràng và trực quan.
- Ví dụ: Trong endpoint [/adgroup/create/](../12-api-reference/07-ad-groups-p2.md#doc-1739499616346114), `ios_osv` được đổi thành `min_ios_version`, `deep_external_action` được đổi thành `secondary_optimization_event`, và `store_authorized_bc` đổi thành `store_authorized_bc_id`.
- Tên các đối tượng lọc được thống nhất là `filtering`.

### Chuẩn hóa giá trị Boolean (True/False)
Tất cả các tham số kiểu boolean hiện nay chỉ sử dụng giá trị logic `True`/`False` thay vì số `1`/`0` hoặc chuỗi `Yes`/`No`.

### Định dạng phản hồi nhất quán (Consistent Response Format)
Cấu trúc JSON trả về được chuẩn hóa đồng bộ trên tất cả các endpoint:

```json
{
    "code": 0,
    "message": "OK",
    "request_id": "202610231200000102030405",
    "data": {}
}
```

### Định dạng thời gian chuẩn ISO 8601
Các trường thời gian như `create_time`, `modify_time` hiện được trả về dưới dạng chuỗi ngày giờ có thể đọc được: `YYYY-MM-DD HH:MM:SS` (giờ chuẩn UTC) thay vì dạng epoch timestamp bằng số.

### Chuẩn hóa đường dẫn URL sang số ít
Các thực thể trong đường dẫn URL được chuyển sang dạng danh từ số ít để đảm bảo tính nhất quán:

* **Tài khoản doanh nghiệp (Business Account)**

| Old URL | New URL |
|---|---|
| /business/get/ (POST) | /business/get/ (GET) |
| /business/videos/list/ (POST) | /business/video/list/ (GET) |
| /business/comments/list/ (POST) | /business/comment/list/ (GET) |
| /business/comments/replies/list/ (POST) | /business/comment/reply/list/ (GET) |
| /business/comments/create/ | /business/comment/create/ |
| /business/comments/replies/create/ | /business/comment/reply/create/ |
| /business/comments/delete/ | /business/comment/delete/ |
| /business/comments/hide/ | /business/comment/hide/ |
| /business/comments/like/ | /business/comment/like/ |
| /business/comments/pin/ | /business/comment/pin/ |
| /business/videos/publish/ | /business/video/publish/ |

* **Trung tâm doanh nghiệp (Business Center)**

| Old URL | New URL |
|---|---|
| /asset/ad/bind_info/ | /asset/bind/quota/ |

* **Quản trị chiến dịch (Campaign Management)**

| Old URL | New URL |
|---|---|
| /ad/tools/audience_size/ | /ad/audience_size/estimate/ |
| /adgroup/rf/inventory/estimate/ | /rf/inventory/estimate/ |
| /adgroup/rf/order/cancel/ | /rf/order/cancel/ |
| /campaign/update/status/ | /campaign/status/update/ |
| /adgroup/update/status/ | /adgroup/status/update/ |
| /ad/update/status/ | /ad/status/update/ |
| /adgroup/update/budget/ | /adgroup/budget/update/ |
| /pangle_flow_package/get/ | /pangle_audience_package/get/ |

* **Danh mục sản phẩm (Catalog)**

| Old URL | New URL |
|---|---|
| /catalog/set/info/ | /catalog/set/product/get/ |
| /catalog/video/get/ | /catalog/video_package/get/ |
| /catalog/eventsource_bind/create/ | /catalog/eventsource/bind/ |
| /catalog/available_countries/get/ | /catalog/available_country/get/ |
| /catalog/eventsource_bind/delete/ | /catalog/eventsource/unbind/ |

* **Nhật ký thay đổi (Change log)**

| Old URL | New URL |
|---|---|
| /activities/task/check/ | /changelog/task/check/ |
| /activities/task/create/ | /changelog/task/create/ |
| /activities/task/download/ | /changelog/task/download/ |

* **Nội dung sáng tạo (Creative)**

| Old URL | New URL |
|---|---|
| /creative/image/tailor/ | /creative/image/edit/ |
| /creative/reports/get/ | /creative/report/get/ |
| /creative/recommend_asset/get/ | /creative/cta/recommend/ |

* **Sự kiện (Events)**

| Old URL | New URL |
|---|---|
| /app/external_action/ | /app/optimization_event/ |
| /app/external_action/retargeting/ | /app/optimization_event/retargeting/ |

* **Khách hàng tiềm năng (Leads)**

| Old URL | New URL |
|---|---|
| /pages/leads/mock/create/ | /page/lead/mock/create/ |
| /pages/leads/mock/delete/ | /page/lead/mock/delete/ |
| /pages/leads/mock/get/ | /page/lead/mock/get/ |
| /pages/leads/task/ | /page/lead/task/ |
| /pages/leads/task/download/ | /page/lead/task/download/ |
| /pages/fields/get/ | /page/field/get/ |
| /pages/library/get/ | /page/library/get/ |
| /pages/library/transfer/ | /page/library/transfer/ |

* **Trang tức thì (Page)**

| Old URL | New URL |
|---|---|
| /pages/get/ | /page/get/ |

* **Báo cáo (Reporting)**

| Old URL | New URL |
|---|---|
| /reports/integrated/get/ (GET) | /report/integrated/get/ (GET) |
| /reports/integrated/get/ (POST) | /report/task/create/ (POST) |
| /reports/task/check/ | /report/task/check/ |
| /reports/task/download/ | /report/task/download/ |
| /reports/ad_benchmark/get/ | /report/ad_benchmark/get/ |
| /reports/video_performance/get/ | /report/video_performance/get/ |

* **Thị trường nhà sáng tạo (TikTok Creator Marketplace)**

| Old URL | New URL |
|---|---|
| /tcm/spark_ads/status/get/ | /tcm/spark_ad/status/get/ |
| /tcm/spark_ads/apply/ | /tcm/spark_ad/apply/ |
| /tcm/reports/get/ | /tcm/report/get/ |
| /tcm/item/audit_status/get/ | /tcm/video/audit_status/get/ |
| /tcm/item/audit_status/update/ | /tcm/video/audit_status/update/ |
| /creator/get/ | /tcm/creator/authorized/ |
| /creator/video/list/ | /tcm/creator/authorized/video/list/ |
| /tcm/creator/search/ | /tcm/creator/public/ |
| /tcm/creator/video/list/ | /tcm/creator/public/video/list/ |

* **Công cụ (Tool)**

| Old URL | New URL |
|---|---|
| /tools/target_recommend_tags/ | /tool/targeting_category/recommend/ |
| /tools/suggest_bid/ | /tool/bid/recommend/ |
| /tools/hashtag/recommend/ | /tool/hashtag/recommend/ |
| /tools/hashtag/get/ | /tool/hashtag/get/ |
| /tools/diagnosis/get/ | /tool/diagnosis/get/ |
| /tools/suggestion/adopt/ | /tool/diagnosis/adopt/ |
| /tools/action_category/ | /tool/action_category/ |
| /tools/carrier/ | /tool/carrier/ |
| /tools/device_model/ | /tool/device_model/ |
| /tools/interest_category/ | /tool/interest_category/ |
| /tools/interest_keywords/ | /tool/interest_keyword/ |
| /tools/language/ | /tool/language/ |
| /tools/regions/ | /tool/region/ |
| /tools/os_version/ | /tool/os_version/ |
| /tools/open_url/ | /tool/open_url/ |
| /tools/timezone/ | /tool/timezone/ |
| /tools/brand_safety/partner/authentication/ | /tool/brand_safety/partner/authorize/status/ |

## Các tính năng mới tiêu biểu

### Quản lý đối tượng (Audience Management)
* Cho phép tải lên tệp chứa một hoặc nhiều loại định danh ID thông qua File API.
* Ra mắt endpoint [/v1.3/dmp/custom_audience/apply/](../12-api-reference/09-audience.md#doc-1758615097524225) giúp áp dụng hoặc hủy liên kết Đối tượng tùy chỉnh với nhiều nhóm quảng cáo đồng thời.
* Nâng giới hạn kích thước tệp tải lên từ 50MB lên **250MB** trong endpoint upload tệp đối tượng tùy chỉnh.

### Trung tâm doanh nghiệp (Business Center)
* Ra mắt endpoint vô hiệu hóa tài khoản quảng cáo trong Business Center.
* Hỗ trợ tạo tài khoản quảng cáo Đấu thầu hoặc Đặt trước (Reservation).
* Ra mắt API Quản lý Nhóm tài sản (BC Asset Groups).

### Quản trị chiến dịch (Campaign Management)
* **Tối ưu hóa nội dung sáng tạo tự động (ACO / Smart Creative)**: Cung cấp bộ API mới (`/ad/aco/create/`, `/ad/aco/update/`, `/ad/aco/get/`, `/ad/aco/material_status/update/`) hỗ trợ tối đa 30 tư liệu sáng tạo và hỗ trợ định dạng Spark Ads.
* **Trả về toàn bộ thực thể quảng cáo**: Khi tạo hoặc cập nhật chiến dịch, nhóm quảng cáo hoặc quảng cáo, hệ thống trả về ngay dữ liệu chi tiết của thực thể vừa tạo/sửa, không cần gọi thêm lệnh GET.
* **Tối ưu hóa ngân sách chiến dịch (CBO)**: Hỗ trợ tự động phân bổ ngân sách tối ưu giữa các nhóm quảng cáo trong cùng chiến dịch.
* **Quảng cáo mua sắm (Shopping Ads)**: Giải pháp quảng cáo dựa trên danh mục sản phẩm thông minh dành cho thương mại điện tử.
* **Định dạng quảng cáo mới**: Hỗ trợ định dạng Carousel Ads (Quảng cáo xoay vòng ảnh) trên bảng tin TikTok.

---

<a id="doc-1740591846408194"></a>
<!-- doc_id: 1740591846408194 -->
<!-- doc_id: 1740591846408194 -->
# Hướng dẫn di chuyển lên v1.3 (Migrate to v1.3)
> Đường dẫn: Tổng quan > Cập nhật lớn trong v1.3 > Di chuyển lên v1.3

Để đảm bảo quá trình di chuyển từ v1.2 lên v1.3 diễn ra thuận lợi, vui lòng tuân thủ danh sách kiểm tra sau:

# Danh sách kiểm tra (Checklist)
1. Rà soát tài liệu [Cập nhật v1.3](tong-quan-va-phien-ban.md#doc-1740579480076290) để nắm bắt các thay đổi cấu trúc giữa 2 phiên bản.
2. Kiểm tra bảng so sánh chi tiết v1.2 vs v1.3 ở từng endpoint trong phần **Tham chiếu API**.
3. Cập nhật mã nguồn xử lý các **thay đổi phá vỡ tương thích (breaking changes)** trước thời hạn ngắt kết nối.

# Phân loại thay đổi
## Thay đổi phá vỡ tương thích (Breaking Changes)
Đòi hỏi bạn phải điều chỉnh mã nguồn ứng dụng để duy trì hoạt động:
- Xóa bỏ endpoint cũ không còn hỗ trợ.
- Xóa bỏ hoặc đổi tên tham số trong yêu cầu (request) hoặc phản hồi (response).
- Bổ sung thêm tham số bắt buộc mới.
- Thay đổi kiểu dữ liệu của tham số (ví dụ: chuyển từ int sang string).
- Thay đổi đường dẫn URL endpoint.

## Thay đổi tương thích ngược (Non-breaking Changes)
Không bắt buộc phải đổi code ngay, bạn có thể triển khai khi có nhu cầu:
- Bổ sung endpoint mới.
- Thêm tham số tùy chọn *(Không bắt buộc)* mới.
- Bổ sung thêm trường thông tin trong phản hồi.
- Bổ sung thông điệp lỗi chi tiết hơn.

# Lưu ý kỹ thuật quan trọng
- **Không truyền body trong yêu cầu GET**: Các API v1.3 không hỗ trợ request body trong phương thức GET. Mọi tham số phải được truyền qua URL query string.
- **Bắt buộc dấu gạch chéo cuối URL (`/`)**: Đảm bảo mọi URL endpoint luôn kết thúc bằng ký tự `/`. Nếu thiếu dấu `/`, hệ thống có thể trả về mã lỗi hoặc chuyển hướng không mong muốn.
  - **Đúng**: `https://business-api.tiktok.com/open_api/v1.3/campaign/get/`
  - **Sai**: `https://business-api.tiktok.com/open_api/v1.3/campaign/get`

---

<a id="doc-1749537346290689"></a>
<!-- doc_id: 1749537346290689 -->
<!-- doc_id: 1749537346290689 -->
# Di chuyển API quản lý chiến dịch (Migrate Campaign Management APIs)
> Đường dẫn: Tổng quan > Cập nhật lớn trong v1.3 > Di chuyển API quản lý chiến dịch

Vui lòng đọc hướng dẫn dưới đây trước khi chuyển đổi các lệnh gọi quản trị chiến dịch sang v1.3:

1. **Quản lý Chiến dịch**: Sử dụng `/open_api/v1.3/campaign/create/` để tạo chiến dịch. Xem [Tạo chiến dịch - So sánh v1.2 và v1.3](../12-api-reference/24-campaign.md#doc-1739318962329602).
2. **Quản lý Nhóm quảng cáo**: Sử dụng `/open_api/v1.3/adgroup/create/` để tạo nhóm quảng cáo. Xem [Tạo nhóm quảng cáo - So sánh v1.2 và v1.3](../12-api-reference/07-ad-groups-p2.md#doc-1739499616346114).

> [!NOTE]
> - Giá trị enum `VIDEO_VIEW` đã bị ngừng hỗ trợ trong trường `optimization_goal`. Khuyến nghị chuyển sang `ENGAGED_VIEW` hoặc `ENGAGED_VIEW_FIFTEEN` khi mục tiêu chiến dịch là xem video.
> - Khi `objective_type` là `VIDEO_VIEW` và `bid_type` là `BID_TYPE_CUSTOM`, bắt buộc dùng `bid_display_mode` là `CPV` (Cost per One View). Không còn hỗ trợ `CPMV`.
> - Trường `cpv_video_duration` đã bị loại bỏ.
> - Trường `pixel_id` chỉ áp dụng cho mục tiêu `CONVERSIONS` và `PRODUCT_SALES`. Đối với các mục tiêu khác, sử dụng `tracking_pixel_id` ở cấp độ mẫu quảng cáo.

3. **Quản lý Mẫu quảng cáo**: Sử dụng `/open_api/v1.3/ad/create/` để tạo quảng cáo tiêu chuẩn hoặc `/open_api/v1.3/ad/aco/create/` để tạo quảng cáo tối ưu hóa tự động (Smart Creative).
   - `identity_id` và `identity_type` là các trường bắt buộc ở cấp quảng cáo.

---

## Hướng dẫn thực hành Data Retrieval bằng cURL

Dưới đây là các lệnh **cURL** mẫu để truy xuất dữ liệu thông tin tài khoản và kiểm tra trạng thái hoạt động trên phiên bản v1.3:

### 1. Truy vấn thông tin người dùng được ủy quyền (Oauth User Info)
```bash
curl -s -X GET "https://business-api.tiktok.com/open_api/v1.3/user/info/"   -H "Access-Token: YOUR_ACCESS_TOKEN"
```

### 2. Lấy danh sách tài khoản quảng cáo được phân quyền (Advertiser Get)
```bash
curl -s -X GET "https://business-api.tiktok.com/open_api/v1.3/oauth2/advertiser/get/?app_id=YOUR_APP_ID&secret=YOUR_SECRET"   -H "Access-Token: YOUR_ACCESS_TOKEN"
```

### 3. Truy vấn danh sách chiến dịch đang hoạt động (Campaign Get)
```bash
curl -s -X GET "https://business-api.tiktok.com/open_api/v1.3/campaign/get/?advertiser_id=YOUR_ADVERTISER_ID&page_size=10"   -H "Access-Token: YOUR_ACCESS_TOKEN"
```
