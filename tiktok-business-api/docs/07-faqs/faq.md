# Câu hỏi thường gặp (FAQs)

Tài liệu này tổng hợp các câu hỏi thường gặp (FAQs) liên quan đến TikTok API for Business, bao gồm hướng dẫn bắt đầu, danh sách cho phép (allowlisting), xác thực và ủy quyền, quản lý chiến dịch, nội dung sáng tạo, tệp đối tượng và báo cáo. Các câu trả lời giúp bạn nhanh chóng tháo gỡ vướng mắc trong quá trình tích hợp và vận hành API.

## Câu hỏi thường gặp (`FAQs`)
<a id="doc-1740029175352322"></a>
<!-- doc_id: 1740029175352322 -->

> Đường dẫn: FAQs

Bài viết này cung cấp bản tổng hợp các câu hỏi thường gặp (FAQs) liên quan đến TikTok API for Business.

### Bắt đầu (Get started)

**Khi tạo nhóm quảng cáo (ad group), tôi cần chỉ định App ID. Đây có phải là App ID của ứng dụng nhà phát triển (developer app) của tôi không?**

App ID (`app_id`) bắt buộc khi tạo nhóm quảng cáo là ID của ứng dụng mà bạn muốn quảng bá (promote). Bạn có thể gửi yêu cầu GET tới endpoint [/app/list/](../12-api-reference/43-events-1-0-p1.md#doc-1740859313270786). Tất cả các ứng dụng được quảng bá thuộc tài khoản quảng cáo của bạn sẽ được trả về. Hãy tìm ứng dụng bạn muốn tạo nhóm quảng cáo và ghi lại giá trị `app_id`.

**Làm thế nào để biết trạng thái xét duyệt sau khi tạo tài khoản quảng cáo bằng tài khoản Agency Business Center?**

Sau khi tạo tài khoản bằng endpoint [/bc/advertiser/create/](../12-api-reference/15-bc-assets.md#doc-1739939020318721), bạn có thể sử dụng endpoint [/advertiser/info/](../12-api-reference/03-ad-accounts.md#doc-1739593083610113) để kiểm tra trạng thái xét duyệt (review status) và thông tin xét duyệt bổ sung (chẳng hạn như lý do bị từ chối).

### Danh sách cho phép (Allowlisting)

**Làm thế nào để yêu cầu tính năng chỉ dành cho danh sách cho phép (allowlist-only feature)?**

Bạn có thể sử dụng tính năng Quản lý danh sách cho phép (Allowlist Management) trên trang web TikTok For Business Developers để yêu cầu các tính năng allowlist cho ứng dụng nhà phát triển (developer apps). Xem thêm chi tiết [tại đây](https://ads.tiktok.com/marketing_api/blog/detail/7102266224578396162).

> [!NOTE]
> Allowlist Management chỉ áp dụng cho việc đưa ứng dụng nhà phát triển vào danh sách cho phép. Mọi yêu cầu đưa vào danh sách cho phép ở cấp nhà quảng cáo (advertiser) hoặc tài khoản quảng cáo (ad account) vẫn cần được thực hiện thông qua đại diện TikTok của bạn.

### Ủy quyền (Authorization)

Vui lòng xem [Authorization-FAQs](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1766037914914818) để tìm hiểu các câu hỏi thường gặp về Ủy quyền (Authorization).

### Xác thực (Authentication)

Vui lòng xem [Authentication-FAQs](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1766041812130817) để tìm hiểu các câu hỏi thường gặp về Xác thực (Authentication).

### Quản lý chiến dịch (Campaign Management)

Vui lòng xem [tại đây](../09-marketing-api/quan-ly-chien-dich-p2.md#doc-1767309272869890) để tìm hiểu các câu hỏi thường gặp về Quản lý chiến dịch (Campaign Management).

### Nội dung sáng tạo (Creatives)

**Làm thế nào để lấy URL xem trước (preview URL) của video dùng trong quảng cáo? Endpoint [/ad/get/](../12-api-reference/02-ads-p1.md#doc-1735735588640770) không trả về URL này.**

Để lấy URL xem trước của video dùng trong quảng cáo, hãy làm theo các bước sau dựa trên danh tính (identity) được sử dụng cho quảng cáo của bạn:

1. Gọi [/ad/get/](../12-api-reference/02-ads-p1.md#doc-1735735588640770) để lấy loại danh tính (`identity_type`) và ID video (`video_id`) hoặc ID bài đăng TikTok (`tiktok_item_id`) liên kết với quảng cáo của bạn.
2. Tùy thuộc vào `identity_type` nhận được từ Bước 1, hãy chọn endpoint thích hợp để lấy URL xem trước video:
   - Đối với quảng cáo không phải Spark Ads (`identity_type`=`CUSTOMIZED_USER`): truyền giá trị `video_id` trả về từ `/ad/get/` vào endpoint [/file/video/ad/search/](../12-api-reference/71-video.md#doc-1740050472224769). Sau đó lấy URL xem trước video từ trường `preview_url` trong phản hồi.
   - Đối với Spark Ads (`identity_type` = `AUTH_CODE`, `TT_USER` hoặc `BC_AUTH_TT`): lấy giá trị `tiktok_item_id` trả về từ `/ad/get/` và truyền vào tham số `item_id` trong yêu cầu gửi tới [/identity/video/info/](../12-api-reference/46-identity.md#doc-1740218522178562). Sau đó lấy URL xem trước video từ trường `url` trong phản hồi.

> [!NOTE]
> Nếu bạn muốn lấy URL xem trước của chính **quảng cáo** (ad preview), hãy sử dụng [/creative/ads_preview/create/](../12-api-reference/38-creative-tools.md#doc-1739403070695426).

### Quản lý tệp đối tượng (Audience Management)

Vui lòng xem [tại đây](../09-marketing-api/audience.md#doc-1746998681953281) để tìm hiểu các câu hỏi thường gặp về Quản lý tệp đối tượng (Audience Management).

### Business Center

Vui lòng xem [tại đây](../09-marketing-api/business-center.md#doc-1739562436183041) để tìm hiểu các câu hỏi thường gặp về Business Center.

### Tài khoản (Accounts)

Vui lòng xem [tại đây](../10-organic-api/accounts-api.md#doc-1776983576127490) để tìm hiểu các câu hỏi thường gặp về Tài khoản (Accounts).

### Báo cáo (Reporting)

Vui lòng xem [tại đây](../09-marketing-api/bao-cao-p4.md#doc-1738864850353154) để tìm hiểu các câu hỏi thường gặp về Báo cáo (Reporting).
