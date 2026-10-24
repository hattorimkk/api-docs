# API Playground

> Phân hệ: Hướng dẫn chung > Công cụ thử nghiệm API Playground.
> API Playground cung cấp môi trường trực quan, tương tác trực tiếp trên giao diện web để thử nghiệm gọi các endpoint Marketing API, kiểm tra payload yêu cầu và xác thực dữ liệu phản hồi theo thời gian thực mà không cần viết mã.

---

## Mục lục điều hướng
- [1. Giới thiệu API Playground](#1-gioi-thieu-api-playground)
- [2. Hướng dẫn sử dụng từng bước](#2-huong-dan-su-dung-tung-buoc)
- [3. Danh sách các Endpoint hỗ trợ trên API Playground](#3-danh-sach-cac-endpoint-ho-tro-tren-api-playground)

---

<a id="doc-1826537506816001"></a>
<!-- doc_id: 1826537506816001 -->
<a id="1-gioi-thieu-api-playground"></a>
## 1. Giới thiệu API Playground

Công cụ API Playground giúp các nhà phát triển xác thực hành vi của API nhanh chóng, kiểm tra định dạng dữ liệu và sao chép mã nguồn mẫu (cURL) sẵn sàng để tích hợp vào ứng dụng.

> **Lưu ý:** Hiện tại API Playground hỗ trợ một tập hợp các endpoint cốt lõi của Marketing API. Danh sách chi tiết xem tại [Danh sách các Endpoint hỗ trợ trên API Playground](api-playground.md#doc-1826537624043586).

### Điều kiện tiên quyết
- Đã tạo tài khoản TikTok For Business. Chi tiết xem [Tạo tài khoản TikTok For Business](../04-get-started/bat-dau.md#doc-1738855099573250).
- Đã đăng ký tài khoản Nhà phát triển (Developer). Chi tiết xem [Đăng ký tài khoản nhà phát triển](../04-get-started/bat-dau.md#doc-1738855176671234).
- Đã tạo ứng dụng nhà phát triển (Developer App). Chi tiết xem [Tạo ứng dụng nhà phát triển](../04-get-started/bat-dau.md#doc-1738855242728450).
- Đã hoàn tất quy trình ủy quyền Marketing API để có mã ủy quyền (`auth_code`). Chi tiết xem [Ủy quyền](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373141733378).
- Để kiểm tra payload cho các endpoint khác nhau, ứng dụng cần được cấp quyền (scopes) tương ứng. Xem chi tiết quyền hạn tại **API Reference** và cách cấu hình tại [Cập nhật quyền ứng dụng](../04-get-started/bat-dau.md#doc-1738855280338946).

---

<a id="2-huong-dan-su-dung-tung-buoc"></a>
## 2. Hướng dẫn sử dụng từng bước

### Bước 1: Truy cập API Playground
Truy cập trực tiếp vào [TikTok API Playground](https://business-api.tiktok.com/portal/api-playground). Bạn cần đăng nhập tài khoản nhà phát triển để sử dụng.

### Bước 2: Tạo Marketing API access token
Trang mặc định sẽ hiển thị màn hình thử nghiệm cho endpoint cấp token [/oauth2/access_token/](../12-api-reference/10-authentication.md#doc-1739965703387137):
1. Trong tab **Request payload**, nhập `app_id`, `auth_code`, và `secret` nhận được từ các bước ủy quyền [Authorization](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373141733378).
2. Nhấn **Submit**. Tab **Response body** sẽ hiển thị `access_token` hợp lệ dùng để gọi các Marketing API khác.

### Bước 3: Thử nghiệm các endpoint Marketing API khác
1. Sử dụng thanh tìm kiếm (search bar) để định vị endpoint cần thử nghiệm theo tên hoặc đường dẫn, ví dụ: `/v1.3/bc/get/`.
2. Nhấn nút **API Doc** để xem tài liệu schema chi tiết của endpoint đã chọn.
3. Nhập token vào trường `Access-Token` trong tab **Request Header** nếu cần.
   > **Mẹo hữu ích:** Sau khi bạn nhập access token trên trang thử nghiệm của một endpoint, trường Access Token trên tất cả các trang endpoint khác sẽ được tự động điền cùng token đó cho đến khi bạn tải lại trang.
4. Trong tab **Request payload**, tùy chỉnh payload theo nhu cầu (ví dụ: xóa `bc_id` nếu muốn lấy tất cả Business Center bạn có quyền truy cập).
5. Nhấn **Submit** và xem cấu trúc dữ liệu phản hồi tại tab **Request body**.

### Bước 4: Sao chép mã mẫu cURL
1. Ở góc trên bên phải của tab **Code example**, nhấn nút sao chép để lấy lệnh cURL hoàn chỉnh.
2. Dán trực tiếp vào terminal hoặc nhập vào Postman / công cụ tích hợp của bạn.

---

<a id="doc-1826537624043586"></a>
<!-- doc_id: 1826537624043586 -->
<a id="3-danh-sach-cac-endpoint-ho-tro-tren-api-playground"></a>
## 3. Danh sách các Endpoint hỗ trợ trên API Playground

Dưới đây là danh sách toàn bộ các endpoint hiện khả dụng trong môi trường thử nghiệm tương tác [API Playground](api-playground.md#doc-1826537506816001):

### Xác thực và Ủy quyền (Authorization and Authentication)
- `/v1.3/oauth2/access_token/` (Đổi mã ủy quyền lấy access token)
- `/v1.3/oauth2/revoke_token/` (Thu hồi token)
- `/v1.3/oauth2/advertiser/get/` (Lấy danh sách tài khoản quảng cáo được ủy quyền)

### Quản lý đối tượng (Audience Management)
- `/v1.3/segment/audience/` (Tạo phân đoạn đối tượng)
- `/v1.3/segment/mapping/` (Ánh xạ phân đoạn đối tượng)
- `/v1.3/dmp/custom_audience/update/` (Cập nhật tệp tùy chỉnh)
- `/v1.3/dmp/custom_audience/list/` (Lấy danh sách tệp đối tượng)
- `/v1.3/dmp/custom_audience/get/` (Lấy thông tin chi tiết tệp đối tượng)
- `/v1.3/dmp/custom_audience/rule/create/` (Tạo đối tượng theo quy tắc)
- `/v1.3/dmp/custom_audience/lookalike/create/` (Tạo đối tượng tương tự)
- `/v1.3/dmp/custom_audience/lookalike/update/` (Làm mới đối tượng tương tự)
- `/v1.3/dmp/custom_audience/delete/` (Xóa đối tượng tùy chỉnh)
- `/v1.3/dmp/custom_audience/share/` (Chia sẻ đối tượng tùy chỉnh)
- `/v1.3/dmp/custom_audience/share/cancel/` (Hủy chia sẻ đối tượng)
- `/v1.3/dmp/custom_audience/share/log/` (Xem nhật ký chia sẻ đối tượng)
- `/v1.3/dmp/custom_audience/apply/` (Áp dụng đối tượng vào ad group)
- `/v1.3/dmp/custom_audience/apply/log/` (Xem nhật ký áp dụng đối tượng)
- `/v1.3/dmp/saved_audience/create/` (Tạo đối tượng đã lưu)
- `/v1.3/dmp/saved_audience/list/` (Danh sách đối tượng đã lưu)
- `/v1.3/dmp/saved_audience/delete/` (Xóa đối tượng đã lưu)

### Trung tâm doanh nghiệp (Business Center)
- `/v1.3/bc/get/` (Danh sách Business Center)
- `/v1.3/bc/transfer/` (Chuyển ngân sách)
- `/v1.3/advertiser/balance/get/` (Số dư tài khoản quảng cáo)
- `/v1.3/bc/balance/get/` (Số dư Business Center)
- `/v1.3/advertiser/info/` (Thông tin chi tiết tài khoản quảng cáo)
- `/v1.3/bc/advertiser/attribute/` (Thuộc tính tài khoản quảng cáo)
- `/v1.3/bc/advertiser/create/` (Tạo tài khoản quảng cáo trong BC)
- `/v1.3/advertiser/update/` (Cập nhật tài khoản quảng cáo)
- `/v1.3/bc/advertiser/disable/` (Vô hiệu hóa tài khoản quảng cáo)
- `/v1.3/bc/image/upload/` (Tải ảnh giấy phép kinh doanh)
- `/v1.3/bc/advertiser/qualification/get/` (Lấy chứng nhận tài khoản)
- `/v1.3/bc/asset/get/` (Lấy tài sản BC)
- `/v1.3/bc/asset/admin/get/` (Lấy tài sản theo Admin)
- `/v1.3/bc/asset/assign/` (Gán quyền tài sản)
- `/v1.3/bc/asset/unassign/` (Hủy gán quyền tài sản)
- `/v1.3/bc/pixel/transfer/` (Chuyển quyền quản trị Pixel)
- `/v1.3/bc/pixel/link/update/` (Liên kết/Hủy liên kết Pixel)
- `/v1.3/bc/pixel/link/get/` (Xem danh sách liên kết Pixel)
- `/v1.3/bc/asset/partner/get/` (Lấy tài sản đối tác)
- `/v1.3/bc/asset/member/get/` (Lấy tài sản thành viên)
- `/v1.3/bc/asset/admin/delete/` (Xóa tài sản khỏi admin)
- `/v1.3/asset/bind/quota/` (Hạn ngạch liên kết tài sản)
- `/v1.3/bc/asset_group/create/` (Tạo nhóm tài sản)
- `/v1.3/bc/asset_group/update/` (Cập nhật nhóm tài sản)
- `/v1.3/bc/asset_group/list/` (Danh sách nhóm tài sản)
- `/v1.3/bc/asset_group/get/` (Chi tiết nhóm tài sản)
- `/v1.3/bc/asset_group/delete/` (Xóa nhóm tài sản)
- `/v1.3/bc/billing_group/create/` (Tạo nhóm thanh toán)
- `/v1.3/bc/billing_group/update/` (Cập nhật nhóm thanh toán)
- `/v1.3/bc/billing_group/list/` (Danh sách nhóm thanh toán)
- `/v1.3/bc/billing_group/get/` (Chi tiết nhóm thanh toán)
- `/v1.3/bc/partner/add/` (Thêm đối tác BC)
- `/v1.3/bc/partner/get/` (Danh sách đối tác BC)
- `/v1.3/bc/partner/delete/` (Xóa đối tác BC)
- `/v1.3/bc/member/invite/` (Mời thành viên vào BC)
- `/v1.3/bc/member/get/` (Danh sách thành viên BC)
- `/v1.3/bc/member/update/` (Cập nhật quyền thành viên)
- `/v1.3/bc/member/delete/` (Xóa thành viên BC)

### Quản lý Chiến dịch & Nhóm quảng cáo
- `/v1.3/campaign/get/` (Lấy danh sách chiến dịch)
- `/v1.3/campaign/create/` (Tạo chiến dịch)
- `/v1.3/campaign/update/` (Cập nhật chiến dịch)
- `/v1.3/campaign/status/update/` (Cập nhật trạng thái chiến dịch)
- `/v1.3/adgroup/get/` (Lấy danh sách nhóm quảng cáo)
- `/v1.3/adgroup/create/` (Tạo nhóm quảng cáo)
- `/v1.3/adgroup/update/` (Cập nhật nhóm quảng cáo)
- `/v1.3/adgroup/status/update/` (Cập nhật trạng thái nhóm quảng cáo)
- `/v1.3/adgroup/budget/update/` (Cập nhật ngân sách nhóm quảng cáo)

### Quản lý Quảng cáo & Báo cáo
- `/v1.3/ad/get/` (Lấy danh sách quảng cáo)
- `/v1.3/ad/create/` (Tạo quảng cáo)
- `/v1.3/ad/update/` (Cập nhật quảng cáo)
- `/v1.3/ad/status/update/` (Cập nhật trạng thái quảng cáo)
- `/v1.3/report/integrated/get/` (Chạy báo cáo đồng bộ tích hợp)
- `/v1.3/report/task/create/` (Tạo tác vụ báo cáo bất đồng bộ)
- `/v1.3/report/task/check/` (Kiểm tra trạng thái báo cáo bất đồng bộ)
- `/v1.3/report/task/download/` (Tải xuống kết quả báo cáo)

