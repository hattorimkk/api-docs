# Tài sản Business Center (BC Assets)

Tài liệu hướng dẫn và tham chiếu toàn bộ các API quản lý Tài sản (Assets) trong Business Center trên TikTok Business API.

---

<a id="doc-1739432636922882"></a>
<!-- doc_id: 1739432636922882 -->
## 1. Tổng quan về Tài sản Business Center (BC Assets Overview)

Business Center (BC) là trung tâm quản lý tập trung toàn diện dành cho các tổ chức, doanh nghiệp và đại lý thuộc mọi quy mô nhằm triển khai các hoạt động tiếp thị, quản lý chiến dịch và tiếp cận đối tượng mục tiêu trên TikTok một cách cộng tác và an toàn.

Bộ API **BC Assets** cho phép các nhà phát triển và doanh nghiệp quản lý vòng đời của các tài sản doanh nghiệp trong Business Center, bao gồm:
- **Tài khoản quảng cáo (Ad Accounts):** Tạo tài khoản quảng cáo mới, cập nhật thông tin tài khoản và cấu hình ngân sách, vô hiệu hóa tài khoản không còn sử dụng, tải lên và xác minh giấy phép kinh doanh / chứng nhận doanh nghiệp, chứng thực UnionPay cho doanh nghiệp tại Trung Quốc Đại Lục.
- **Tài khoản tổ chức (Organization Accounts):** Tạo và liên kết tài khoản tổ chức doanh nghiệp trong Business Center.
- **Truy vấn tài sản (Asset Discovery):** Liệt kê danh sách tài sản theo quyền thành viên hoặc quyền quản trị viên Business Center.
- **Phân quyền tài sản (Asset Permission Management):** Phân quyền và hủy phân quyền quản lý tài sản cho các thành viên trong tổ chức.
- **Tài khoản TikTok (TikTok Accounts):** Yêu cầu liên kết, hủy liên kết tài khoản TikTok với Business Center, lấy URL ủy quyền phân phối quảng cáo Spark Ads, liên kết tài khoản TikTok với tài khoản quảng cáo.
- **Pixel theo dõi (Pixel Management):** Chuyển giao quyền sở hữu Pixel sang Business Center, chia sẻ liên kết Pixel với các tài khoản quảng cáo.
- **Quan hệ đối tác và thành viên (Partners & Members):** Quản lý đối tác và thành viên được chia sẻ quyền sử dụng tài sản, xóa tài sản hoặc lấy thông tin liên kết tài sản.

### Danh mục các Endpoint trong nhóm:
1. [Tạo tài khoản quảng cáo (Create an ad account)](#2-tạo-tài-khoản-quảng-cáo-create-an-ad-account): `POST /open_api/v1.3/bc/advertiser/create/`
2. [Cập nhật tài khoản quảng cáo (Update an ad account)](#3-cập-nhật-tài-khoản-quảng-cáo-update-an-ad-account): `POST /open_api/v1.3/advertiser/update/`
3. [Vô hiệu hóa tài khoản quảng cáo (Disable an ad account)](#4-vô-hiệu-hóa-tài-khoản-quảng-cáo-disable-an-ad-account): `POST /open_api/v1.3/bc/advertiser/disable/`
4. [Tải lên chứng nhận doanh nghiệp (Upload a business certificate)](#5-tải-lên-chứng-nhận-doanh-nghiệp-upload-a-business-certificate): `POST /open_api/v1.3/bc/image/upload/`
5. [Lấy thông tin chứng nhận trong Business Center (Get qualifications)](#6-lấy-thông-tin-chứng-nhận-trong-business-center-get-qualifications): `GET /open_api/v1.3/bc/advertiser/qualification/get/`
6. [Kiểm tra yêu cầu xác minh UnionPay (Check UnionPay requirement)](#7-kiểm-tra-yêu-cầu-xác-minh-unionpay-cho-giấy-phép-kinh-doanh): `GET /open_api/v1.3/bc/advertiser/unionpay_info/check/`
7. [Gửi xác minh UnionPay (Submit UnionPay verification)](#8-gửi-xác-minh-unionpay-cho-giấy-phép-kinh-doanh): `POST /open_api/v1.3/bc/advertiser/unionpay/submit/`
8. [Tạo tài khoản tổ chức (Create an Organization Account)](#9-tạo-tài-khoản-tổ-chức-trong-business-center): `POST /open_api/v1.3/bc/asset/organization/account/create/`
9. [Lấy danh sách tài sản (Get assets)](#10-lấy-danh-sách-tài-sản-get-assets): `GET /open_api/v1.3/bc/asset/get/`
10. [Lấy danh sách tài sản với quyền quản trị (Get assets as admin)](#11-lấy-danh-sách-tài-sản-với-quyền-quản-trị-viên-get-assets-as-admin): `GET /open_api/v1.3/bc/asset/admin/get/`
11. [Phân quyền tài sản (Assign an asset)](#12-phân-quyền-tài-sản-cho-thành-viên-assign-an-asset): `POST /open_api/v1.3/bc/asset/assign/`
12. [Hủy phân quyền tài sản (Unassign an asset)](#13-hủy-phân-quyền-tài-sản-của-thành-viên-unassign-an-asset): `POST /open_api/v1.3/bc/asset/unassign/`
13. [Yêu cầu liên kết tài khoản TikTok với BC (Link TikTok account to BC)](#14-yêu-cầu-liên-kết-tài-khoản-tiktok-với-business-center): `POST /open_api/v1.3/bc/asset/tt_account/link/`
14. [Hủy liên kết tài khoản TikTok khỏi BC (Unlink TikTok account from BC)](#15-hủy-liên-kết-tài-khoản-tiktok-khỏi-business-center): `POST /open_api/v1.3/bc/asset/tt_account/unlink/`
15. [Lấy URL ủy quyền phân phối quảng cáo Spark Ads](#16-lấy-url-ủy-quyền-phân-phối-quảng-cáo-tài-khoản-tiktok): `GET /open_api/v1.3/bc/tt_account/delivery_auth_url/get/`
16. [Liên kết tài khoản TikTok với tài khoản quảng cáo](#17-liên-kết-tài-khoản-tiktok-với-tài-khoản-quảng-cáo-trong-business-center): `POST /open_api/v1.3/bc/tt_account/ad_account/link/`
17. [Hủy liên kết tài khoản TikTok khỏi tài khoản quảng cáo](#18-hủy-liên-kết-tài-khoản-tiktok-khỏi-tài-khoản-quảng-cáo-trong-business-center): `POST /open_api/v1.3/bc/tt_account/ad_account/unlink/`
18. [Lấy danh sách tài khoản quảng cáo liên kết với tài khoản TikTok](#19-lấy-danh-sách-tài-khoản-quảng-cáo-liên-kết-với-tài-khoản-tiktok): `GET /open_api/v1.3/bc/tt_account/ad_account/list/`
19. [Quản lý Pixel (Pixel Management Overview)](#20-quản-lý-pixel-trong-business-center): Tổng quan về Pixel trong Business Center.
20. [Chuyển Pixel từ nhà quảng cáo sang BC](#21-chuyển-giao-quyền-sở-hữu-pixel-từ-nhà-quảng-cáo-sang-bc): `POST /open_api/v1.3/bc/pixel/transfer/`
21. [Liên kết / Hủy liên kết Pixel với tài khoản quảng cáo](#22-liên-kết-hoặc-hủy-liên-kết-pixel-với-tài-khoản-quảng-cáo): `POST /open_api/v1.3/bc/pixel/ad_account/link/`
22. [Lấy danh sách tài khoản quảng cáo liên kết với Pixel](#23-lấy-danh-sách-tài-khoản-quảng-cáo-liên-kết-với-pixel): `GET /open_api/v1.3/bc/pixel/ad_account/list/`
23. [Lấy danh sách đối tác theo tài sản (Get partners by asset)](#24-lấy-danh-sách-đối-tác-theo-tài-sản): `GET /open_api/v1.3/bc/asset/partner/list/`
24. [Lấy danh sách thành viên theo tài sản (Get members by asset)](#25-lấy-danh-sách-thành-viên-theo-tài-sản): `GET /open_api/v1.3/bc/asset/member/list/`
25. [Xóa tài sản khỏi Business Center (Delete assets)](#26-xóa-tài-sản-khỏi-business-center): `POST /open_api/v1.3/bc/asset/delete/`
26. [Lấy thông tin liên kết của tài sản (Get binding info)](#27-lấy-thông-tin-liên-kết-của-tài-sản): `GET /open_api/v1.3/bc/asset/binding/get/`

---

<a id="doc-1739939020318721"></a>
<!-- doc_id: 1739939020318721 -->
<a id="2-tạo-tài-khoản-quảng-cáo-create-an-ad-account"></a>
## 2. Tạo tài khoản quảng cáo (Create an ad account)

Sử dụng endpoint này để tạo một tài khoản quảng cáo đấu thầu (Auction ad account) trong Business Center loại **Agency** (Đại lý) hoặc **Direct** (Trực tiếp). Bạn cần có vai trò Quản trị viên (Admin) trong Business Center.

Để tạo tài khoản đấu thầu, hãy điền giá trị `AUCTION` vào trường `type` bên dưới đối tượng `advertiser_info`.

> **Lưu ý về giấy phép và vị trí đăng ký:**
> - Nếu tài khoản quảng cáo được đăng ký tại Trung Quốc Đại Lục, Hồng Kông, Pháp, Brazil hoặc Mexico, bạn cần sử dụng endpoint `POST /bc/image/upload/` để tải lên hình ảnh giấy phép kinh doanh hoặc các tài liệu chứng nhận năng lực trước khi gọi endpoint này.
> - Nếu tài khoản quảng cáo đăng ký tại Trung Quốc Đại Lục, bạn có thể cần phải gửi xác minh UnionPay cho giấy phép kinh doanh.
> - Endpoint không hỗ trợ tạo hàng loạt nhiều tài khoản cùng lúc. Vui lòng gọi tạo từng tài khoản một.
> - Mỗi người dùng có thể tạo tối đa 10.000 tài khoản quảng cáo trên toàn bộ các Business Center. Mỗi Business Center có hạn ngạch tạo tài khoản hàng ngày và tổng số tài khoản tối đa riêng. Khi chạm hạn mức, bạn có thể gọi endpoint `POST /bc/advertiser/disable/` để vô hiệu hóa tài khoản cũ nhằm giải phóng hạn ngạch.

### Thông tin Endpoint
- **URL:** `https://business-api.tiktok.com/open_api/v1.3/bc/advertiser/create/`
- **Phương thức:** `POST`

### Header
| Header | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Có | Access Token được cấp quyền xác thực. |
| Content-Type | string | Có | Kiểu nội dung yêu cầu: `application/json`. |

### Tham số Body (Request Body)
| Tham số | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `bc_id` | string | Có | ID của Business Center. |
| `tied_to_billing_group` | boolean | Không | Có thêm tài khoản quảng cáo vào nhóm thanh toán hay không. Mặc định: `false`. Tính năng này thuộc danh sách cho phép (allowlist). |
| `advertiser_info` | object | Có | Thông tin cấu hình tài khoản quảng cáo. |
| ↳ `name` | string | Có | Tên tài khoản quảng cáo. Chiều dài tối đa 100 ký tự. |
| ↳ `currency` | string | Có | Loại tiền tệ của tài khoản quảng cáo (cần nhất quán với Business Center, ví dụ: `USD`, `VND`, `EUR`). |
| ↳ `timezone` | string | Có | Mã múi giờ của tài khoản (ví dụ: `Asia/Ho_Chi_Minh`, `America/Los_Angeles`). |
| ↳ `type` | string | Không | Loại tài khoản quảng cáo muốn tạo. Các giá trị enum: `RESERVATION`, `AUCTION` (mặc định). BC loại `DIRECT` chỉ có thể tạo loại `AUCTION`. |
| `customer_info` | object | Có | Thông tin doanh nghiệp của nhà quảng cáo. |
| ↳ `company` | string | Có | Tên công ty của tài khoản quảng cáo. Tối đa 255 ký tự. |
| ↳ `industry` | number | Có | Mã ngành nghề quảng cáo (Industry ID). |
| ↳ `registered_area` | string | Có | Mã vùng quốc gia đăng ký kinh doanh (ví dụ: `VN`, `US`, `FR`, `BR`, `MX`, `CN`, `HK`). |
| `qualification_info` | object | Điều kiện | Bắt buộc khi Business Center thuộc loại `AGENCY` hoặc `SELF_SERVICE_AGENCY`. Không truyền đối tượng này nếu BC là loại `DIRECT`. |
| ↳ `promotion_link` | string | Điều kiện | Đường dẫn website quảng cáo của doanh nghiệp (tối đa 255 ký tự). |
| ↳ `license_no` | string | Điều kiện | Mã số giấy phép kinh doanh. Bắt buộc đối với tài khoản tại Trung Quốc Đại Lục, Hồng Kông, Brazil, Mexico. |
| ↳ `license_image_id` | string | Điều kiện | ID hình ảnh giấy phép kinh doanh đã tải lên qua endpoint upload ảnh. Bắt buộc tại Trung Quốc Đại Lục, Hồng Kông. |
| ↳ `qualification_image_ids` | string[] | Điều kiện | Danh sách ID hình ảnh chứng nhận bổ sung (bắt buộc tại Pháp, Brazil, Mexico). |
| ↳ `qualification_id` | string | Không | Mã ID thông tin chứng nhận tái sử dụng từ tài khoản quảng cáo khác đã phê duyệt. Khi truyền trường này, không truyền các trường khác trong `qualification_info`. |
| `contact_info` | object | Không | Thông tin liên hệ của nhà quảng cáo. |
| ↳ `name` | string | Không | Họ tên người liên hệ (tối đa 100 ký tự). |
| ↳ `email` | string | Điều kiện | Email liên hệ. Bắt buộc nếu đăng ký tại Pháp, Brazil hoặc Mexico. |
| ↳ `number` | string | Không | Số điện thoại liên hệ. |
| `billing_info` | object | Điều kiện | Thông tin xuất hóa đơn và thuế. Bắt buộc nếu nơi đăng ký là Pháp, Brazil hoặc Mexico. |
| ↳ `address` | string | Không | Địa chỉ xuất hóa đơn (tối đa 512 ký tự). |
| ↳ `tax_field_dict` | dict | Không | Từ điển mã số thuế tùy theo quốc gia (`vat` cho Châu Âu như Pháp, `tax_id` cho Brazil, Mexico, UAE, Mỹ; `abn` cho Úc). |
| `billing_group_info` | object | Không | Thông tin nhóm thanh toán để gom hóa đơn. |
| ↳ `invoice_group_by` | string | Có | Chế độ gom hóa đơn: `ACCOUNT` (gom chung hóa đơn trong nhóm), `ADVERTISER` (tách riêng từng tài khoản). |
| ↳ `billing_group_id` | string | Không | ID nhóm thanh toán. Hợp lệ khi `invoice_group_by` là `ACCOUNT`. |
| ↳ `invoice_payer` | string | Điều kiện | Bên thanh toán hóa đơn: `AGENCY` (Đại lý), `ADVERTISER` (Nhà quảng cáo). Bắt buộc khi đăng ký tại Pháp (`FR`). |
| `payment_info` | object | Không | Thông tin cấu hình thanh toán và danh mục thanh toán (Payment Portfolio). |
| ↳ `payment_portfolio_id` | string | Không | ID danh mục thanh toán muốn liên kết với tài khoản quảng cáo mới. |
| ↳ `budget_info` | object | Không | Chi tiết cấu hình ngân sách tài khoản quảng cáo. |
| ↳↳ `budget_mode` | string | Không | Chế độ ngân sách: `UNLIMITED` (không giới hạn), `MONTHLY_BUDGET` (ngân sách hàng tháng, mặc định), `DAILY_BUDGET` (ngân sách hàng ngày), `CUSTOM_BUDGET` (ngân sách tùy chỉnh một lần). |
| ↳↳ `budget` | number | Điều kiện | Số tiền ngân sách, làm tròn đến 2 chữ số thập phân. Bắt buộc khi `budget_mode` khác `UNLIMITED`. |

### Tham số Response
| Trường | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi từ API. `0` thể hiện thành công. |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Log ID định danh duy nhất của yêu cầu. |
| `data` | object | Dữ liệu trả về sau khi tạo tài khoản. |
| ↳ `advertiser_id` | string | ID của tài khoản quảng cáo vừa tạo thành công. |
| ↳ `payment_portfolio_binding_result` | object | Kết quả liên kết tài khoản với danh mục thanh toán (`payment_portfolio_id`). |
| ↳↳ `status` | string | Trạng thái liên kết: `SUCCESS` hoặc `FAILED`. |
| ↳↳ `error_msg` | string | Thông báo lỗi nếu thất bại (null nếu thành công). |
| ↳ `budget_setup_result` | object | Kết quả cấu hình ngân sách cho tài khoản mới tạo. |
| ↳↳ `status` | string | Trạng thái thiết lập: `SUCCESS` hoặc `FAILED`. |
| ↳↳ `error_msg` | string | Chi tiết lỗi cấu hình ngân sách nếu có. |

### Ví dụ cURL
```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/bc/advertiser/create/" \
  -H "Access-Token: YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "bc_id": "7012345678901234567",
    "advertiser_info": {
      "name": "Acme Brand VN Store",
      "currency": "USD",
      "timezone": "Asia/Ho_Chi_Minh",
      "type": "AUCTION"
    },
    "customer_info": {
      "company": "Acme Retail Corporation",
      "industry": 290501,
      "registered_area": "US"
    },
    "contact_info": {
      "name": "Nguyen Van A",
      "email": "contact@acme.com",
      "number": "+84901234567"
    },
    "payment_info": {
      "budget_info": {
        "budget_mode": "MONTHLY_BUDGET",
        "budget": 5000.00
      }
    }
  }'
```

### Ví dụ Python
```python
import requests

url = "https://business-api.tiktok.com/open_api/v1.3/bc/advertiser/create/"
headers = {
    "Access-Token": "YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}
payload = {
    "bc_id": "7012345678901234567",
    "advertiser_info": {
        "name": "Acme Brand VN Store",
        "currency": "USD",
        "timezone": "Asia/Ho_Chi_Minh",
        "type": "AUCTION"
    },
    "customer_info": {
        "company": "Acme Retail Corporation",
        "industry": 290501,
        "registered_area": "US"
    },
    "contact_info": {
        "name": "Nguyen Van A",
        "email": "contact@acme.com",
        "number": "+84901234567"
    },
    "payment_info": {
        "budget_info": {
            "budget_mode": "MONTHLY_BUDGET",
            "budget": 5000.00
        }
    }
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())
```

### Phản hồi thành công mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202610231201000001",
  "data": {
    "advertiser_id": "7112345678901234567",
    "payment_portfolio_binding_result": {
      "status": "SUCCESS",
      "error_msg": null
    },
    "budget_setup_result": {
      "status": "SUCCESS",
      "error_msg": null
    }
  }
}
```

---

<a id="doc-1739939050770434"></a>
<!-- doc_id: 1739939050770434 -->
<a id="3-cập-nhật-tài-khoản-quảng-cáo-update-an-ad-account"></a>
## 3. Cập nhật tài khoản quảng cáo (Update an ad account)

Sử dụng endpoint này để cập nhật thông tin tài khoản quảng cáo được tạo trong Business Center hoặc điều chỉnh ngân sách tài khoản quảng cáo thuộc quyền sở hữu của Business Center trong chế độ tự động phân bổ (auto-allocation mode). Hỗ trợ cập nhật từng phần (incremental update). Bạn cần có quyền Quản trị viên (Admin) của Business Center.

### Thông tin Endpoint
- **URL:** `https://business-api.tiktok.com/open_api/v1.3/advertiser/update/`
- **Phương thức:** `POST`

### Header
| Header | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Có | Access Token được cấp quyền xác thực. |
| Content-Type | string | Có | Kiểu nội dung yêu cầu: `application/json`. |

### Tham số Body (Request Body)
| Tham số | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | Điều kiện | Phải truyền `advertiser_id` hoặc `bc_id`. Truyền `advertiser_id` để cập nhật cài đặt thông tin phi ngân sách của một tài khoản quảng cáo duy nhất. |
| `advertiser_name` | string | Không | Tên tài khoản quảng cáo cần cập nhật. |
| `company` | string | Không | Tên công ty của tài khoản quảng cáo. Có thể kiểm tra khả năng chỉnh sửa qua API bằng trường `company_name_editable`. |
| `contact_name` | string | Không | Tên của người liên hệ đại diện. |
| `contact_email` | string | Không | Email của người liên hệ. |
| `contact_number` | string | Không | Số điện thoại của người liên hệ. |
| `promotion_link` | string | Không | Đường dẫn website quảng cáo (tối đa 255 ký tự). |
| `license_no` | string | Không | Mã số giấy phép kinh doanh (hỗ trợ cho tài khoản đăng ký tại Trung Quốc Đại Lục, Hồng Kông, Brazil, Mexico). |
| `license_image_id` | string | Không | ID hình ảnh của giấy phép kinh doanh. |
| `qualification_images` | object[] | Không | Danh sách các chứng nhận doanh nghiệp bổ sung. |
| ↳ `image_id` | string | Không | ID hình ảnh của chứng nhận kinh doanh. |
| `address` | string | Không | Địa chỉ doanh nghiệp hiển thị trên hóa đơn (1 - 1.024 ký tự). |
| `tax_map` | dict[string] | Không | Bản đồ mã số thuế thanh toán và hóa đơn theo từng quốc gia (`vat` cho Pháp, `tax_id` cho Brazil). |
| `need_submit_certificate` | boolean | Không | Có gửi hình ảnh chứng nhận mới để duyệt lại hay không (`true`/`false`). Chỉ đặt `true` khi có thay đổi các trường pháp lý (`company`, `promotion_link`, `license_no`, `license_image_id`, `qualification_images`). |
| `bc_id` | string | Điều kiện | Phải truyền `advertiser_id` hoặc `bc_id`. Dùng `bc_id` khi muốn cập nhật ngân sách cho một hoặc nhiều tài khoản quảng cáo thuộc Business Center. Người thực hiện cần có quyền Quản lý Tài chính (`finance_role` = `MANAGER`). |
| `budget_update_type` | string | Không | Kiểu điều chỉnh ngân sách khi truyền `bc_id`. Các giá trị enum:<ul><li>`UPDATE`: Cập nhật chế độ ngân sách và hạn mức ngân sách mới.</li><li>`RESET`: Đặt lại mức tiêu thụ ngân sách về 0 (chỉ áp dụng cho tài khoản dùng `CUSTOM_BUDGET`).</li><li>`INCREMENTAL_UPDATE`: Tăng thêm hoặc giảm bớt số tiền từ ngân sách hiện tại.</li><li>`ONE_CLICK_SET`: Thiết lập ngân sách tài khoản về mức tối thiểu.</li></ul>Mặc định: `UPDATE`. |
| `request_id` | string | Không | Mã định danh yêu cầu hỗ trợ tính lũy thừa (idempotency) khi sử dụng `budget_update_type` = `INCREMENTAL_UPDATE`. Đảm bảo không bị lặp thao tác cộng/trừ ngân sách khi thử lại yêu cầu. |
| `advertiser_budgets` | object[] | Điều kiện | Danh sách đối tượng ngân sách tài khoản quảng cáo cần cập nhật. |
| ↳ `advertiser_id` | string | Có | ID của tài khoản quảng cáo cần điều chỉnh ngân sách. |
| ↳ `budget_mode` | string | Điều kiện | Chế độ ngân sách: `UNLIMITED`, `MONTHLY_BUDGET`, `DAILY_BUDGET`, `CUSTOM_BUDGET`. |
| ↳ `budget` | number | Điều kiện | Số tiền ngân sách cần cập nhật hoặc giá trị gia số (+/-) khi dùng `INCREMENTAL_UPDATE`. |

### Tham số Response
| Trường | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi từ API (`0` là thành công). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Log ID định danh duy nhất của yêu cầu hệ thống. |
| `data` | object | Dữ liệu trả về sau khi cập nhật. |
| ↳ `advertiser_id` | string | ID của tài khoản quảng cáo được cập nhật. |
| ↳ `advertiser_budgets` | object[] | Chi tiết kết quả cập nhật ngân sách cho các tài khoản. |

### Ví dụ cURL
```bash
# 1. Cập nhật thông tin tài khoản quảng cáo
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/advertiser/update/" \
  -H "Access-Token: YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "advertiser_id": "7112345678901234567",
    "advertiser_name": "Acme Brand Global Updated",
    "contact_name": "Tran Van B",
    "contact_email": "updated@acme.com",
    "contact_number": "+84987654321",
    "address": "123 Le Loi, District 1, Ho Chi Minh City",
    "need_submit_certificate": false
  }'

# 2. Điều chỉnh tăng ngân sách tài khoản trong Business Center
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/advertiser/update/" \
  -H "Access-Token: YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "bc_id": "7012345678901234567",
    "budget_update_type": "INCREMENTAL_UPDATE",
    "request_id": "req_uuid_20261023_001",
    "advertiser_budgets": [
      {
        "advertiser_id": "7112345678901234567",
        "budget": 200.0
      }
    ]
  }'
```

### Ví dụ Python
```python
import requests

url = "https://business-api.tiktok.com/open_api/v1.3/advertiser/update/"
headers = {
    "Access-Token": "YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}

# Cập nhật ngân sách tài khoản
payload = {
    "bc_id": "7012345678901234567",
    "budget_update_type": "UPDATE",
    "advertiser_budgets": [
        {
            "advertiser_id": "7112345678901234567",
            "budget_mode": "MONTHLY_BUDGET",
            "budget": 8000.00
        }
    ]
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())
```

### Phản hồi thành công mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202610231202000001",
  "data": {
    "advertiser_id": "7112345678901234567"
  }
}
```

---

<a id="doc-1752349244331009"></a>
<!-- doc_id: 1752349244331009 -->
<a id="4-vô-hiệu-hóa-tài-khoản-quảng-cáo-disable-an-ad-account"></a>
## 4. Vô hiệu hóa tài khoản quảng cáo (Disable an ad account)

Sử dụng endpoint này để vô hiệu hóa một hoặc nhiều tài khoản quảng cáo trong Business Center. Thao tác này chỉ nên thực hiện khi bạn không còn muốn sử dụng tài khoản đó nữa, vì một khi đã vô hiệu hóa, tài khoản quảng cáo sẽ bị đóng và **không thể khôi phục** lại trạng thái hoạt động bình thường ("Approved").

### Điều kiện tiên quyết trước khi vô hiệu hóa:
- Bạn phải có vai trò Quản trị viên (Admin) trong Business Center.
- Tài khoản quảng cáo muốn vô hiệu hóa phải thuộc quyền sở hữu của Business Center này.
- Tài khoản chưa từng bị vô hiệu hóa hoặc đình chỉ trước đó.
- Tài khoản không có bất kỳ chiến dịch quảng cáo nào đang phân phối trong vòng 3 ngày qua.
- Tài khoản không có hóa đơn chưa thanh toán.
- Tài khoản không có giao dịch chuyển tiền/hoàn tiền chưa hoàn tất.
- Nếu tài khoản thanh toán tự động (Automatic Payment), tài khoản không được có bất kỳ chi phí phát sinh nào chưa lập hóa đơn.

### Thông tin Endpoint
- **URL:** `https://business-api.tiktok.com/open_api/v1.3/bc/advertiser/disable/`
- **Phương thức:** `POST`

### Header
| Header | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Có | Access Token được cấp quyền xác thực. |
| Content-Type | string | Có | Kiểu nội dung yêu cầu: `application/json`. |

### Tham số Body (Request Body)
| Tham số | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `bc_id` | string | Có | ID của Business Center. |
| `advertiser_ids` | string[] | Có | Danh sách ID các tài khoản quảng cáo cần vô hiệu hóa. |

### Tham số Response
| Trường | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi từ API. `0` thể hiện thành công. |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Log ID định danh yêu cầu. |
| `data` | object | Dữ liệu trả về (chứa danh sách tài khoản đã xử lý). |

### Ví dụ cURL
```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/bc/advertiser/disable/" \
  -H "Access-Token: YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "bc_id": "7012345678901234567",
    "advertiser_ids": [
      "7112345678901234567"
    ]
  }'
```

### Ví dụ Python
```python
import requests

url = "https://business-api.tiktok.com/open_api/v1.3/bc/advertiser/disable/"
headers = {
    "Access-Token": "YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}
payload = {
    "bc_id": "7012345678901234567",
    "advertiser_ids": ["7112345678901234567"]
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())
```

### Phản hồi thành công mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202610231203000001",
  "data": {}
}
```

---

<a id="doc-1739938996913218"></a>
<!-- doc_id: 1739938996913218 -->
<a id="5-tải-lên-chứng-nhận-doanh-nghiệp-upload-a-business-certificate"></a>
## 5. Tải lên chứng nhận doanh nghiệp (Upload a business certificate)

Sử dụng endpoint này để tải lên hình ảnh chứng nhận doanh nghiệp hoặc giấy phép kinh doanh lên hệ thống TikTok. Bạn cần có quyền Quản trị viên (Admin) của Business Center.

Nếu bạn cần tạo tài khoản quảng cáo tại Trung Quốc Đại Lục, Hồng Kông, Pháp, Brazil hoặc Mexico, bạn bắt buộc phải tải lên tài liệu pháp lý qua endpoint này trước. Endpoint sẽ trả về mã định danh hình ảnh (`image_id`). Mã này sau đó được truyền vào trường `license_image_id` hoặc `qualification_image_ids` khi gọi API tạo tài khoản quảng cáo `POST /bc/advertiser/create/`.

### Thông tin Endpoint
- **URL:** `https://business-api.tiktok.com/open_api/v1.3/bc/image/upload/`
- **Phương thức:** `POST`

### Header
| Header | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Có | Access Token được cấp quyền xác thực. |
| Content-Type | string | Có | Loại yêu cầu tải lên tệp: `multipart/form-data`. |

### Tham số Form-Data (Request Parameters)
| Tham số | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `bc_id` | string | Có | ID của Business Center. |
| `image_file` | file | Có | Tệp hình ảnh chứng nhận doanh nghiệp / giấy phép kinh doanh. Định dạng hỗ trợ: JPG, JPEG, PNG. Kích thước tối đa: 10MB. |

### Tham số Response
| Trường | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi từ API (`0` là thành công). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Log ID định danh yêu cầu. |
| `data` | object | Dữ liệu trả về. |
| ↳ `image_id` | string | ID của hình ảnh chứng nhận đã được lưu trữ trên máy chủ TikTok. |

### Ví dụ cURL
```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/bc/image/upload/" \
  -H "Access-Token: YOUR_ACCESS_TOKEN" \
  -F "bc_id=7012345678901234567" \
  -F "image_file=@/path/to/business_license.png"
```

### Ví dụ Python
```python
import requests

url = "https://business-api.tiktok.com/open_api/v1.3/bc/image/upload/"
headers = {
    "Access-Token": "YOUR_ACCESS_TOKEN"
}
data = {
    "bc_id": "7012345678901234567"
}
files = {
    "image_file": open("business_license.png", "rb")
}

response = requests.post(url, headers=headers, data=data, files=files)
print(response.json())
```

### Phản hồi thành công mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202610231204000001",
  "data": {
    "image_id": "img_v3_cert_9876543210abcdef"
  }
}
```

---

<a id="doc-1770118680584194"></a>
<!-- doc_id: 1770118680584194 -->
<a id="6-lấy-thông-tin-chứng-nhận-trong-business-center-get-qualifications"></a>
## 6. Lấy thông tin chứng nhận trong Business Center (Get qualifications)

Sử dụng endpoint này để truy xuất danh sách các chứng nhận doanh nghiệp (qualifications) hiện có bên trong Business Center. 

Khi nhận được mã `qualification_id` từ phản hồi, bạn có thể tái sử dụng thông tin chứng nhận đã được duyệt này để tạo tài khoản quảng cáo mới mà không cần phải tải lên lại giấy tờ, bằng cách truyền giá trị vào tham số `qualification_id` trong endpoint `POST /bc/advertiser/create/`.

### Điều kiện tiên quyết:
- Đảm bảo bạn đã từng tạo ít nhất một tài khoản quảng cáo qua `/bc/advertiser/create/` có khai báo thông tin `qualification_info`. Thông tin này được hệ thống sử dụng để tạo `qualification_id`. Nếu trước đó bạn không khai báo `qualification_info`, hệ thống sẽ không có `qualification_id` để tái sử dụng.
- Bạn phải có quyền Quản trị viên (Admin) của Business Center.

### Thông tin Endpoint
- **URL:** `https://business-api.tiktok.com/open_api/v1.3/bc/advertiser/qualification/get/`
- **Phương thức:** `GET`

### Header
| Header | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Có | Access Token được cấp quyền xác thực. |

### Tham số Query (Query Parameters)
| Tham số | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `bc_id` | string | Có | ID của Business Center. |
| `filtering` | object | Không | Điều kiện lọc danh sách chứng nhận. |
| ↳ `verified` | boolean | Không | Trạng thái xác thực chứng nhận (`true` là đã xác minh, `false` là chưa xác minh). |
| `page` | int | Không | Số trang hiện tại. Giá trị mặc định: `1`. Dải giá trị: ≥ 1. |
| `page_size` | int | Không | Số lượng kết quả trên mỗi trang. Giá trị mặc định: `10`. Dải giá trị: 1 - 100. |

### Tham số Response
| Trường | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi từ API (`0` là thành công). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Log ID định danh duy nhất của yêu cầu. |
| `data` | object | Dữ liệu trả về. |
| ↳ `qualifications` | object[] | Danh sách thông tin chứng nhận doanh nghiệp. |
| ↳↳ `qualification_id` | string | ID định danh của chứng nhận doanh nghiệp. |
| ↳↳ `company_name` | string | Tên công ty trên giấy chứng nhận. |
| ↳↳ `status` | string | Trạng thái xác thực chứng nhận: `VERIFIED` (đã xác thực), `UNVERIFIED` (chưa xác thực). |
| ↳↳ `owner_advertiser_id` | string | ID tài khoản quảng cáo là chủ sở hữu ban đầu của chứng nhận này. |
| ↳↳ `linked_advertiser_count` | int | Số lượng tài khoản quảng cáo đang cùng sử dụng chứng nhận này. |
| ↳↳ `region_code` | string | Mã quốc gia hoặc khu vực của chứng nhận (ví dụ: `US`, `DE`, `VN`). |
| ↳ `page_info` | object | Thông tin phân trang. |
| ↳↳ `page` | number | Số trang hiện tại. |
| ↳↳ `page_size` | number | Số lượng kết quả trên một trang. |
| ↳↳ `total_number` | number | Tổng số lượng chứng nhận tìm thấy. |
| ↳↳ `total_page` | number | Tổng số trang kết quả. |

### Ví dụ cURL
```bash
curl -X GET "https://business-api.tiktok.com/open_api/v1.3/bc/advertiser/qualification/get/?bc_id=7012345678901234567&filtering=%7B%22verified%22%3Atrue%7D&page=1&page_size=10" \
  -H "Access-Token: YOUR_ACCESS_TOKEN"
```

### Ví dụ Python
```python
import json
import requests

url = "https://business-api.tiktok.com/open_api/v1.3/bc/advertiser/qualification/get/"
headers = {
    "Access-Token": "YOUR_ACCESS_TOKEN"
}
params = {
    "bc_id": "7012345678901234567",
    "filtering": json.dumps({"verified": True}),
    "page": 1,
    "page_size": 10
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

### Phản hồi thành công mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202610231205000001",
  "data": {
    "page_info": {
      "page": 1,
      "page_size": 10,
      "total_number": 1,
      "total_page": 1
    },
    "qualifications": [
      {
        "qualification_id": "qual_7112345678901234567",
        "company_name": "Acme Retail Corporation",
        "status": "VERIFIED",
        "owner_advertiser_id": "7112345678901234567",
        "linked_advertiser_count": 2,
        "region_code": "US"
      }
    ]
  }
}
```

---

<a id="doc-1813772238056449"></a>
<!-- doc_id: 1813772238056449 -->
<a id="7-kiểm-tra-yêu-cầu-xác-minh-unionpay-cho-giấy-phép-kinh-doanh"></a>
## 7. Kiểm tra yêu cầu xác minh UnionPay cho giấy phép kinh doanh

Sử dụng endpoint này để kiểm tra xem giấy phép kinh doanh của bạn có yêu cầu bắt buộc phải xác minh qua UnionPay hay không.

Đối với các tài khoản quảng cáo đăng ký tại Trung Quốc Đại Lục thuộc một trong các loại hình doanh nghiệp sau, bạn bắt buộc phải hoàn tất xác minh UnionPay sau khi tạo tài khoản quảng cáo có cùng số giấy phép kinh doanh (`POST /bc/advertiser/create/`):
- Hộ kinh doanh cá thể (Sole Proprietorship / Individual industrial and commercial household).
- Doanh nghiệp tư nhân (Sole Proprietorship Enterprise).
- Công ty trách nhiệm hữu hạn một thành viên do cá nhân (hoặc cá nhân từ Hồng Kông, Ma Cao, Đài Loan) sở hữu.
- Công ty trách nhiệm hữu hạn do cá nhân đầu tư hoặc kiểm soát.

Nếu không hoàn tất xác minh UnionPay bắt buộc, tài khoản quảng cáo sẽ bị từ chối trong quá trình kiểm duyệt.

### Thông tin Endpoint
- **URL:** `https://business-api.tiktok.com/open_api/v1.3/bc/advertiser/unionpay_info/check/`
- **Phương thức:** `GET`

### Header
| Header | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Có | Access Token được cấp quyền xác thực. |

### Tham số Query (Query Parameters)
| Tham số | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `license_no` | string | Có | Mã số giấy phép kinh doanh cần kiểm tra. |

### Tham số Response
| Trường | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi từ API (`0` là thành công). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Log ID định danh yêu cầu. |
| `data` | object | Dữ liệu trả về. |
| ↳ `unionpay_verification_required` | boolean | Giấy phép kinh doanh có yêu cầu xác minh UnionPay hay không: `true` (bắt buộc), `false` (không bắt buộc). Nếu là `true`, bạn cần gọi endpoint gửi thông tin xác minh UnionPay. |

### Ví dụ cURL
```bash
curl -X GET "https://business-api.tiktok.com/open_api/v1.3/bc/advertiser/unionpay_info/check/?license_no=91310000XXXXXXXXXX" \
  -H "Access-Token: YOUR_ACCESS_TOKEN"
```

### Ví dụ Python
```python
import requests

url = "https://business-api.tiktok.com/open_api/v1.3/bc/advertiser/unionpay_info/check/"
headers = {
    "Access-Token": "YOUR_ACCESS_TOKEN"
}
params = {
    "license_no": "91310000XXXXXXXXXX"
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

### Phản hồi thành công mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202610231206000001",
  "data": {
    "unionpay_verification_required": true
  }
}
```

---

<a id="doc-1813772274039809"></a>
<!-- doc_id: 1813772274039809 -->
<a id="8-gửi-xác-minh-unionpay-cho-giấy-phép-kinh-doanh"></a>
## 8. Gửi xác minh UnionPay cho giấy phép kinh doanh

Sử dụng endpoint này để gửi thông tin xác minh UnionPay cho giấy phép kinh doanh liên kết với tài khoản quảng cáo.

Sau khi gửi xác minh, hãy đợi khoảng 20 giây và gọi endpoint kiểm tra thông tin tài khoản quảng cáo để xác nhận trạng thái. Nếu tài khoản bị từ chối do xác minh thất bại, bạn có thể cập nhật lại thông tin giấy phép (`license_no` và `license_image_id`) qua endpoint `/advertiser/update/` rồi gửi lại xác minh qua endpoint này.

> **Lưu ý:** Nếu bạn gửi xác minh UnionPay nhiều lần trong khi tài khoản quảng cáo đang được xem xét, chỉ lần gửi đầu tiên được tiếp nhận; các lần gửi tiếp theo sẽ bị bỏ qua.

### Điều kiện tiên quyết:
- Đã kiểm tra qua endpoint kiểm tra UnionPay và nhận kết quả `unionpay_verification_required` = `true`.
- Đã tạo tài khoản quảng cáo với cùng số giấy phép `license_no` qua endpoint `/bc/advertiser/create/`.
- Bạn phải có quyền Quản trị viên (Admin) trong Business Center và tài khoản quảng cáo.

### Thông tin Endpoint
- **URL:** `https://business-api.tiktok.com/open_api/v1.3/bc/advertiser/unionpay_info/submit/`
- **Phương thức:** `POST`

### Header
| Header | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Có | Access Token được cấp quyền xác thực. |
| Content-Type | string | Có | Kiểu nội dung yêu cầu: `application/json`. |

### Tham số Body (Request Body)
| Tham số | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `bc_id` | string | Có | ID của Business Center. Bạn cần có quyền Quản trị viên (`user_role` = `ADMIN`). |
| `advertiser_id` | string | Có | ID của tài khoản quảng cáo liên kết với giấy phép kinh doanh cần xác minh UnionPay. |
| `representative_name` | string | Có | Tên tiếng Trung của người đại diện theo pháp luật hiển thị trên giấy phép kinh doanh. |
| `representative_document_type` | string | Không | Loại giấy tờ của người đại diện. Các giá trị enum:<ul><li>`ID_CARD`: Thẻ căn cước (mặc định).</li><li>`PASSPORT`: Hộ chiếu.</li><li>`HK_MACAO_EXIT_ENTRY_PERMIT`: Giấy thông hành đi lại giữa Hồng Kông, Ma Cao.</li><li>`TAIWAN_MAINLAND_TRAVEL_PERMIT`: Giấy phép đi lại Đại Lục cho cư dân Đài Loan.</li><li>`HK_MACAO_MAINLAND_TRAVEL_PERMIT`: Giấy phép đi lại Đại Lục cho cư dân Hồng Kông, Ma Cao.</li></ul> |
| `representative_id` | string | Có | Số giấy tờ của người đại diện theo pháp luật:<br>• Với `ID_CARD`: Chuỗi 18 chữ số căn cước.<br>• Với `PASSPORT`: Chuỗi ký tự số và chữ của hộ chiếu.<br>• Với các loại giấy thông hành: Chuỗi số tương ứng theo định dạng hợp lệ. |
| `unionpay_account` | string | Có | Số tài khoản UnionPay (từ 12 đến 19 chữ số). |
| `representative_phone_number` | string | Có | Số điện thoại di động của người đại diện hợp pháp (chuỗi 11 chữ số tại Trung Quốc Đại Lục, ví dụ: `13812345678`). |

### Tham số Response
| Trường | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi từ API (`0` thể hiện gửi thành công). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Log ID định danh duy nhất của yêu cầu. |
| `data` | object | Dữ liệu trả về (rỗng). |

### Ví dụ cURL
```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/bc/advertiser/unionpay_info/submit/" \
  -H "Access-Token: YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "bc_id": "7012345678901234567",
    "advertiser_id": "7112345678901234567",
    "representative_name": "张三",
    "representative_document_type": "ID_CARD",
    "representative_id": "110101199001011234",
    "unionpay_account": "6222021234567890123",
    "representative_phone_number": "13800138000"
  }'
```

### Ví dụ Python
```python
import requests

url = "https://business-api.tiktok.com/open_api/v1.3/bc/advertiser/unionpay_info/submit/"
headers = {
    "Access-Token": "YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}
payload = {
    "bc_id": "7012345678901234567",
    "advertiser_id": "7112345678901234567",
    "representative_name": "张三",
    "representative_document_type": "ID_CARD",
    "representative_id": "110101199001011234",
    "unionpay_account": "6222021234567890123",
    "representative_phone_number": "13800138000"
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())
```

### Phản hồi thành công mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202610231207000001",
  "data": {}
}
```

---

<a id="doc-1855027199571138"></a>
<!-- doc_id: 1855027199571138 -->
<a id="9-tạo-tài-khoản-tổ-chức-trong-business-center"></a>
## 9. Tạo tài khoản tổ chức trong Business Center

Sử dụng endpoint này để tạo một Tài khoản tổ chức (Organization Account) trực tiếp bên trong Business Center.

Tài khoản tổ chức cho phép doanh nghiệp thiết lập sự hiện diện thương hiệu chính thức trên nền tảng TikTok. Bạn cần có quyền Quản trị viên (Admin) của Business Center.

> **Lưu ý về loại tài sản phát sinh:**
> Mỗi Tài khoản tổ chức mới tạo ra sẽ tạo ra hai mã định danh tài sản (`asset_id`):
> 1. Một mã cho loại tài sản `MANAGED_BUSINESS_ACCOUNT`.
> 2. Một mã cho loại tài sản `TT_ACCOUNT`.
> Bạn có thể phân quyền cho thành viên Business Center sử dụng tài khoản này tùy theo mức độ quyền hạn mong muốn bằng endpoint `POST /bc/asset/assign/`.

### Thông tin Endpoint
- **URL:** `https://business-api.tiktok.com/open_api/v1.3/bc/oa/create/`
- **Phương thức:** `POST`

### Header
| Header | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Có | Access Token được cấp quyền xác thực. |
| Content-Type | string | Có | Kiểu nội dung tệp: `multipart/form-data`. |

### Tham số Form-Data (Request Parameters)
| Tham số | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `bc_id` | string | Có | ID của Business Center. |
| `display_name` | string | Có | Tên hiển thị (display name / username) của tài khoản tổ chức. |
| `handle` | string | Có | Tên người dùng định danh duy nhất của tài khoản TikTok (TikTok handle, bắt đầu sau ký tự @). |
| `profile_image` | file | Có | Tệp hình ảnh ảnh đại diện (avatar) của tài khoản tổ chức. Định dạng hỗ trợ: JPG, JPEG, PNG. |
| `operating_region_code` | string | Có | Mã quốc gia hoặc khu vực hoạt động của tài khoản tổ chức. Xem bảng danh sách mã vùng hỗ trợ bên dưới (ví dụ: `VN`, `US`, `SG`, `JP`, `GB`, `FR`...). |
| `qualification_info` | string | Điều kiện | Chuỗi JSON chứa thông tin chứng nhận doanh nghiệp. Bắt buộc khi Business Center thuộc loại `AGENCY` hoặc `SELF_SERVICE_AGENCY`. Không sử dụng nếu BC là loại `DIRECT`. Ví dụ: `{"qualification_id": "xxx"}`. |
| ↳ `qualification_id` | string | Có | ID của chứng nhận doanh nghiệp đã xác thực liên kết với tài khoản quảng cáo của khách hàng (lấy qua endpoint `GET /bc/advertiser/qualification/get/` với `verified` = `true`). |

### Bảng một số mã vùng hoạt động (`operating_region_code`):
| Mã `operating_region_code` | Quốc gia / Khu vực |
|---|---|
| `VN` | Vietnam |
| `US` | United States |
| `GB` | United Kingdom |
| `SG` | Singapore |
| `TH` | Thailand |
| `ID` | Indonesia |
| `MY` | Malaysia |
| `PH` | Philippines |
| `JP` | Japan |
| `KR` | South Korea |
| `FR` | France |
| `DE` | Germany |
| `BR` | Brazil |
| `MX` | Mexico |
| `AE` | United Arab Emirates |

### Tham số Response
| Trường | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi từ API (`0` là thành công). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Log ID định danh duy nhất của yêu cầu. |
| `data` | object | Dữ liệu trả về. |
| ↳ `asset_id` | string | ID của Tài khoản tổ chức vừa tạo. Tương ứng với loại tài sản `MANAGED_BUSINESS_ACCOUNT`. |
| ↳ `asset_name` | string | Tên hiển thị của Tài khoản tổ chức vừa tạo. |

### Ví dụ cURL
```bash
# 1. Tạo Tài khoản tổ chức trong Business Center loại Direct
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/bc/oa/create/" \
  -H "Access-Token: YOUR_ACCESS_TOKEN" \
  -F "bc_id=7012345678901234567" \
  -F "display_name=Acme Official Store" \
  -F "handle=acme_official_vn" \
  -F "profile_image=@/path/to/avatar.png" \
  -F "operating_region_code=VN"

# 2. Tạo Tài khoản tổ chức trong Business Center loại Agency (kèm qualification_info)
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/bc/oa/create/" \
  -H "Access-Token: YOUR_ACCESS_TOKEN" \
  -F "bc_id=7012345678901234567" \
  -F "display_name=Client Brand Channel" \
  -F "handle=client_brand_us" \
  -F "profile_image=@/path/to/avatar.png" \
  -F "operating_region_code=US" \
  -F 'qualification_info={"qualification_id": "qual_7112345678901234567"}'
```

### Ví dụ Python
```python
import json
import requests

url = "https://business-api.tiktok.com/open_api/v1.3/bc/oa/create/"
headers = {
    "Access-Token": "YOUR_ACCESS_TOKEN"
}
data = {
    "bc_id": "7012345678901234567",
    "display_name": "Acme Official Store",
    "handle": "acme_official_vn",
    "operating_region_code": "VN"
}
files = {
    "profile_image": open("avatar.png", "rb")
}

response = requests.post(url, headers=headers, data=data, files=files)
print(response.json())
```

### Phản hồi thành công mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202610231208000001",
  "data": {
    "asset_id": "7223344556677889900",
    "asset_name": "Acme Official Store"
  }
}
```

---

<a id="doc-1739432717798401"></a>
<!-- doc_id: 1739432717798401 -->
<a id="10-lấy-danh-sách-tài-sản-get-assets"></a>
## 10. Lấy danh sách tài sản (Get assets)

Sử dụng endpoint này để lấy danh sách các tài sản mà bạn hoặc một người dùng cụ thể trong Business Center có quyền truy cập.

### Thông tin Endpoint
- **URL:** `https://business-api.tiktok.com/open_api/v1.3/bc/asset/get/`
- **Phương thức:** `GET`

### Header
| Header | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Có | Access Token được cấp quyền xác thực. |

### Tham số Query (Query Parameters)
| Tham số | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `bc_id` | string | Có | ID của Business Center. |
| `asset_type` | string | Có | Loại tài sản cần truy vấn. Các giá trị enum:<ul><li>`ADVERTISER`: Tài khoản quảng cáo.</li><li>`CATALOG`: Danh mục sản phẩm (Catalog).</li><li>`TIKTOK_SHOP`: Cửa hàng TikTok Shop.</li><li>`PIXEL`: Mã theo dõi sự kiện Pixel.</li><li>`LEAD`: Thư viện biểu mẫu tìm kiếm khách hàng tiềm năng (Leads).</li><li>`TT_ACCOUNT`: Tài khoản TikTok làm tài sản phân phối quảng cáo Spark Ads (tương ứng loại định danh `BC_AUTH_TT`).</li><li>`MANAGED_BUSINESS_ACCOUNT`: Tài khoản TikTok để quản lý Tài khoản Doanh nghiệp (quản lý tin nhắn, lead, biểu mẫu, bình luận, liên kết sản phẩm và phân tích chuyên sâu).</li></ul> |
| `filtering` | object | Không | Điều kiện lọc tài sản. Không sử dụng đồng thời `user_id` và `user_email`. Nếu không chỉ định, hệ thống mặc định gán `user_id` là ID của người dùng cấp quyền access token. |
| ↳ `user_id` | string | Không | ID của người dùng cần lấy danh sách tài sản (dành cho người dùng đã ở trạng thái `BOUND`). Không hỗ trợ khi `asset_type` là `MANAGED_BUSINESS_ACCOUNT`. |
| ↳ `user_email` | string | Không | Email của người dùng (dành cho người dùng ở trạng thái lời mời `PENDING` và khi `asset_type` là `ADVERTISER`). |
| ↳ `keyword` | string | Không | Từ khóa tìm kiếm tài sản theo tên hoặc ID. Không hỗ trợ với `MANAGED_BUSINESS_ACCOUNT`. |
| `page` | number | Không | Số trang hiện tại. Mặc định: `1`. |
| `page_size` | number | Không | Số lượng kết quả trên một trang. Dải giá trị: 1 - 50. Mặc định: `10`. |

### Tham số Response
| Trường | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi từ API (`0` là thành công). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Log ID định danh yêu cầu. |
| `data` | object | Dữ liệu trả về. |
| ↳ `list` | object[] | Danh sách tài sản thỏa mãn điều kiện. |
| ↳↳ `asset_id` | string | ID định danh tài sản. |
| ↳↳ `asset_name` | string | Tên của tài sản. |
| ↳↳ `role` | string | Quyền hạn của người dùng trên tài sản đó. |
| ↳ `page_info` | object | Thông tin phân trang (`page`, `page_size`, `total_number`, `total_page`). |

### Ví dụ cURL
```bash
curl -X GET "https://business-api.tiktok.com/open_api/v1.3/bc/asset/get/?bc_id=7012345678901234567&asset_type=ADVERTISER&page=1&page_size=10" \
  -H "Access-Token: YOUR_ACCESS_TOKEN"
```

### Ví dụ Python
```python
import requests

url = "https://business-api.tiktok.com/open_api/v1.3/bc/asset/get/"
headers = {
    "Access-Token": "YOUR_ACCESS_TOKEN"
}
params = {
    "bc_id": "7012345678901234567",
    "asset_type": "ADVERTISER",
    "page": 1,
    "page_size": 10
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

### Phản hồi thành công mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202610231209000001",
  "data": {
    "list": [
      {
        "asset_id": "7112345678901234567",
        "asset_name": "Acme Brand Global Store",
        "role": "ADVERTISER_ROLE_ADMIN"
      }
    ],
    "page_info": {
      "page": 1,
      "page_size": 10,
      "total_number": 1,
      "total_page": 1
    }
  }
}
```

---

<a id="doc-1739433007779841"></a>
<!-- doc_id: 1739433007779841 -->
<a id="11-lấy-danh-sách-tài-sản-với-quyền-quản-trị-viên-get-assets-as-admin"></a>
## 11. Lấy danh sách tài sản với quyền quản trị viên (Get assets as admin)

Sử dụng endpoint này để lấy thông tin mở rộng về các tài sản trong Business Center dành riêng cho người dùng Quản trị viên (Admin). 

Thông tin mở rộng có thể truy vấn và lọc bao gồm trạng thái tài khoản quảng cáo, kiểu quan hệ giữa Business Center và tài sản (sở hữu hoặc được đối tác chia sẻ), cùng trạng thái quan hệ.

### Thông tin Endpoint
- **URL:** `https://business-api.tiktok.com/open_api/v1.3/bc/asset/admin/get/`
- **Phương thức:** `GET`

### Header
| Header | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Có | Access Token được cấp quyền xác thực. |

### Tham số Query (Query Parameters)
| Tham số | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `bc_id` | string | Có | ID của Business Center. |
| `asset_type` | string | Có | Loại tài sản: `ADVERTISER`, `CATALOG`, `TIKTOK_SHOP`, `PIXEL`, `LEAD`, `TT_ACCOUNT`, `MANAGED_BUSINESS_ACCOUNT`. |
| `filtering` | object | Không | Điều kiện lọc danh sách tài sản quản trị. |
| ↳ `advertiser_status` | string | Không | Trạng thái tài khoản quảng cáo: `STATUS_ENABLE`, `STATUS_DISABLE`, `STATUS_PENDING_CONFIRM`. |
| ↳ `relation_type` | string | Không | Kiểu quan hệ với tài sản: `OWNED` (tài sản do BC trực tiếp sở hữu), `SHARED` (tài sản được đối tác chia sẻ). |
| ↳ `relation_status` | string | Không | Trạng thái quan hệ tài sản (ví dụ: `BOUND`, `PENDING`). |
| ↳ `keyword` | string | Không | Từ khóa tìm kiếm theo tên hoặc mã tài sản. |
| `page` | number | Không | Số trang hiện tại. Mặc định: `1`. |
| `page_size` | number | Không | Số lượng bản ghi trên một trang. Dải giá trị: 1 - 50. Mặc định: `10`. |

### Tham số Response
| Trường | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi từ API (`0` là thành công). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Log ID định danh yêu cầu. |
| `data` | object | Dữ liệu trả về. |
| ↳ `list` | object[] | Danh sách tài sản chi tiết của Business Center. |
| ↳↳ `asset_id` | string | ID tài sản. |
| ↳↳ `asset_name` | string | Tên tài sản. |
| ↳↳ `relation_type` | string | Kiểu quan hệ sở hữu (`OWNED` hoặc `SHARED`). |
| ↳↳ `advertiser_status` | string | Trạng thái hoạt động của tài khoản quảng cáo. |
| ↳ `page_info` | object | Thông tin phân trang (`page`, `page_size`, `total_number`, `total_page`). |

### Ví dụ cURL
```bash
curl -X GET "https://business-api.tiktok.com/open_api/v1.3/bc/asset/admin/get/?bc_id=7012345678901234567&asset_type=ADVERTISER&page=1&page_size=10" \
  -H "Access-Token: YOUR_ACCESS_TOKEN"
```

### Ví dụ Python
```python
import requests

url = "https://business-api.tiktok.com/open_api/v1.3/bc/asset/admin/get/"
headers = {
    "Access-Token": "YOUR_ACCESS_TOKEN"
}
params = {
    "bc_id": "7012345678901234567",
    "asset_type": "ADVERTISER",
    "page": 1,
    "page_size": 10
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

### Phản hồi thành công mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202610231210000001",
  "data": {
    "list": [
      {
        "asset_id": "7112345678901234567",
        "asset_name": "Acme Brand Global Store",
        "relation_type": "OWNED",
        "advertiser_status": "STATUS_ENABLE"
      }
    ],
    "page_info": {
      "page": 1,
      "page_size": 10,
      "total_number": 1,
      "total_page": 1
    }
  }
}
```

---

<a id="doc-1739438211077121"></a>
<!-- doc_id: 1739438211077121 -->
<a id="12-phân-quyền-tài-sản-cho-thành-viên-assign-an-asset"></a>
## 12. Phân quyền tài sản cho thành viên (Assign an asset)

Sử dụng endpoint này để phân quyền quản lý một tài sản trong Business Center cho một thành viên cụ thể. Bạn cần có quyền Quản trị viên (Admin) của Business Center.

### Thông tin Endpoint
- **URL:** `https://business-api.tiktok.com/open_api/v1.3/bc/asset/assign/`
- **Phương thức:** `POST`

### Header
| Header | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Có | Access Token được cấp quyền xác thực. |
| Content-Type | string | Có | Kiểu nội dung yêu cầu: `application/json`. |

### Tham số Body (Request Body)
| Tham số | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `bc_id` | string | Có | ID của Business Center. |
| `user_id` | string | Có | ID của thành viên Business Center được cấp quyền (lấy từ endpoint `GET /bc/member/get/`). |
| `asset_type` | string | Có | Loại tài sản phân quyền: `ADVERTISER`, `CATALOG`, `TIKTOK_SHOP`, `LEAD`, `TT_ACCOUNT`, `MANAGED_BUSINESS_ACCOUNT`. |
| `asset_id` | string | Có | ID của tài sản cần phân quyền. |
| `advertiser_role` | string | Điều kiện | Bắt buộc khi `asset_type` là `ADVERTISER`. Các vai trò khả dụng:<ul><li>`ROLE_ADVERTISER_ADMIN`: Quản trị viên tài khoản quảng cáo.</li><li>`ROLE_ADVERTISER_OPERATOR`: Nhà vận hành chiến dịch.</li><li>`ROLE_ADVERTISER_ANALYST`: Nhà phân tích dữ liệu quảng cáo.</li></ul> |
| `catalog_role` | string | Điều kiện | Bắt buộc khi `asset_type` là `CATALOG`. Vai trò: `ROLE_CATALOG_ADMIN`, `ROLE_CATALOG_OPERATOR`. |
| `form_library_role` | string | Điều kiện | Bắt buộc khi `asset_type` là `LEAD`. Vai trò: `ROLE_FORM_LIBRARY_ADMIN`, `ROLE_FORM_LIBRARY_OPERATOR`. |
| `store_role` | string | Điều kiện | Bắt buộc khi `asset_type` là `TIKTOK_SHOP`. Vai trò: `AD_PROMOTION` (chỉ dùng Shop để quảng cáo). |
| `tt_account_roles` | string[] | Điều kiện | Bắt buộc khi `asset_type` là `TT_ACCOUNT`. Các quyền cho tài khoản TikTok phát quảng cáo:<ul><li>`PUBLISH_VIDEO_ADS_ONLY`: Đăng video chỉ dùng cho quảng cáo (không hiện trên hồ sơ công khai).</li><li>`PUBLISH_VIDEO_SHOW_ON_TT_PROFILE_AND_ADS`: Đăng video hiển thị trên trang cá nhân và dùng chạy quảng cáo.</li><li>`LIVE`: Quyền truy cập phòng phát trực tiếp LIVE.</li><li>`SHOWCASE`: Quyền truy cập Showcase sản phẩm.</li><li>`DIRECT_MESSAGE`: Quyền quản lý và phản hồi tin nhắn trực tiếp.</li><li>`SERIES`: Quyền truy cập video trả phí Series.</li></ul> |
| `business_account_roles` | string[] | Điều kiện | Bắt buộc khi `asset_type` là `MANAGED_BUSINESS_ACCOUNT`. Quyền quản lý tài khoản doanh nghiệp:<ul><li>`BUSINESS_ACCOUNT_ADMIN`: Toàn quyền quản trị tài khoản doanh nghiệp.</li><li>`BUSINESS_ACCOUNT_OPERATOR`: Vận hành bài viết, tin nhắn, phân tích dữ liệu.</li><li>`BUSINESS_ACCOUNT_ANALYST`: Chỉ xem báo cáo phân tích hiệu suất.</li></ul>Tối đa 1 vai trò trong mảng. |

### Tham số Response
| Trường | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi API (`0` là thành công). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Log ID định danh duy nhất của yêu cầu. |
| `data` | object | Dữ liệu trả về (rỗng khi phân quyền thành công). |

### Ví dụ cURL
```bash
# Phân quyền tài khoản quảng cáo cho thành viên
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/bc/asset/assign/" \
  -H "Access-Token: YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "bc_id": "7012345678901234567",
    "user_id": "7098765432109876543",
    "asset_type": "ADVERTISER",
    "asset_id": "7112345678901234567",
    "advertiser_role": "ROLE_ADVERTISER_ADMIN"
  }'
```

### Ví dụ Python
```python
import requests

url = "https://business-api.tiktok.com/open_api/v1.3/bc/asset/assign/"
headers = {
    "Access-Token": "YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}
payload = {
    "bc_id": "7012345678901234567",
    "user_id": "7098765432109876543",
    "asset_type": "ADVERTISER",
    "asset_id": "7112345678901234567",
    "advertiser_role": "ROLE_ADVERTISER_ADMIN"
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())
```

### Phản hồi thành công mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202610231211000001",
  "data": {}
}
```

---

<a id="doc-1739448126749698"></a>
<!-- doc_id: 1739448126749698 -->
<a id="13-hủy-phân-quyền-tài-sản-của-thành-viên-unassign-an-asset"></a>
## 13. Hủy phân quyền tài sản của thành viên (Unassign an asset)

Sử dụng endpoint này để thu hồi quyền truy cập đối với một tài sản từ một thành viên trong Business Center. Bạn cần có quyền Quản trị viên (Admin) của Business Center.

### Thông tin Endpoint
- **URL:** `https://business-api.tiktok.com/open_api/v1.3/bc/asset/unassign/`
- **Phương thức:** `POST`

### Header
| Header | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Có | Access Token được cấp quyền xác thực. |
| Content-Type | string | Có | Kiểu nội dung yêu cầu: `application/json`. |

### Tham số Body (Request Body)
| Tham số | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `bc_id` | string | Có | ID của Business Center. |
| `user_id` | string | Có | ID của thành viên Business Center cần thu hồi quyền truy cập. |
| `asset_type` | string | Có | Loại tài sản: `ADVERTISER`, `CATALOG`, `LEAD`, `TT_ACCOUNT`, `MANAGED_BUSINESS_ACCOUNT`. |
| `asset_id` | string | Có | ID của tài sản cần thu hồi phân quyền. |

### Tham số Response
| Trường | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi từ API (`0` là thành công). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Log ID định danh duy nhất của yêu cầu. |
| `data` | object | Dữ liệu trả về (rỗng khi thu hồi thành công). |

### Ví dụ cURL
```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/bc/asset/unassign/" \
  -H "Access-Token: YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "bc_id": "7012345678901234567",
    "user_id": "7098765432109876543",
    "asset_type": "ADVERTISER",
    "asset_id": "7112345678901234567"
  }'
```

### Ví dụ Python
```python
import requests

url = "https://business-api.tiktok.com/open_api/v1.3/bc/asset/unassign/"
headers = {
    "Access-Token": "YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}
payload = {
    "bc_id": "7012345678901234567",
    "user_id": "7098765432109876543",
    "asset_type": "ADVERTISER",
    "asset_id": "7112345678901234567"
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())
```

### Phản hồi thành công mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202610231212000001",
  "data": {}
}
```

---

<a id="doc-1879660350792706"></a>
<!-- doc_id: 1879660350792706 -->
<a id="14-yêu-cầu-liên-kết-tài-khoản-tiktok-với-business-center"></a>
## 14. Yêu cầu liên kết tài khoản TikTok với Business Center

Sử dụng endpoint này để gửi yêu cầu liên kết một tài khoản TikTok với Business Center của bạn. Bạn cũng có thể dùng endpoint này để cập nhật phân quyền mà Business Center sở hữu đối với một tài khoản TikTok đã liên kết từ trước.

### Điều kiện tiên quyết:
- Bạn phải có quyền Quản trị viên (Admin) trong Business Center (`user_role` = `ADMIN`).
- Để liên kết bằng phương thức `HANDLE` (gửi lời mời trực tiếp trong ứng dụng TikTok), Business Center phải là loại Direct hoặc Agency đã được xác minh (`verification_status` = `VERIFIED`) và không phải là loại tự phục vụ (non-self-serve).

### Thông tin Endpoint
- **URL:** `https://business-api.tiktok.com/open_api/v1.3/bc/asset/tt_account/link/`
- **Phương thức:** `POST`

### Header
| Header | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Có | Access Token được cấp quyền xác thực. |
| Content-Type | string | Có | Kiểu nội dung yêu cầu: `application/json`. |

### Tham số Body (Request Body)
| Tham số | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `bc_id` | string | Có | ID của Business Center. |
| `linking_method` | string | Có | Phương thức liên kết tài khoản TikTok. Các giá trị enum:<ul><li>`LINK`: Yêu cầu chủ tài khoản TikTok quét mã QR để phê duyệt liên kết. API sẽ trả về URL ủy quyền (`link_url`) để tạo mã QR.</li><li>`HANDLE`: Gửi yêu cầu liên kết trực tiếp vào ứng dụng TikTok của chủ tài khoản để họ bấm xác nhận.</li></ul> |
| `permission_level` | string | Có | Cấp độ quyền hạn bạn yêu cầu từ tài khoản TikTok:<ul><li>`MANAGE_ACCOUNT`: Quản lý tài khoản toàn diện (quản lý tin nhắn, bình luận, leads, liên kết sản phẩm, phân tích video/LIVE, chạy quảng cáo tin nhắn). Một tài khoản TikTok chỉ có thể được quản lý bởi duy nhất một Business Center.</li><li>`DELIVER_ADS`: Chỉ phân phối quảng cáo Spark Ads. Cho phép truy cập bài viết có sẵn, video LIVE và đăng video quảng cáo mới. Một tài khoản TikTok có thể ủy quyền cho nhiều Business Center cùng phân phối quảng cáo.</li></ul> |
| `permission_detail` | object | Có | Chi tiết các quyền cụ thể yêu cầu từ tài khoản TikTok. |
| ↳ `tt_account_roles` | string[] | Có | Danh sách quyền đối với tài khoản TikTok. Hỗ trợ các giá trị: `VIDEO_POSTING`, `LIVE`, `SHOWCASE`, `DIRECT_MESSAGE`, `SERIES`, v.v. |
| `tt_account_handle` | string | Điều kiện | Tên người dùng tài khoản TikTok (bắt đầu sau ký hiệu @). Bắt buộc khi `linking_method` là `HANDLE`. |
| `asset_id` | string | Không | ID tài sản của tài khoản TikTok trong Business Center (khi cần cập nhật quyền cho tài khoản đã liên kết trước đó). |

### Tham số Response
| Trường | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi từ API (`0` là thành công). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Log ID định danh duy nhất của yêu cầu. |
| `data` | object | Dữ liệu trả về. |
| ↳ `asset_id` | string | ID định danh tài sản của tài khoản TikTok trong Business Center. |
| ↳ `link_url` | string | Đường dẫn URL ủy quyền dùng để tạo mã QR khi `linking_method` là `LINK`. |

### Ví dụ cURL
```bash
# 1. Yêu cầu liên kết tài khoản TikTok qua mã QR
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/bc/asset/tt_account/link/" \
  -H "Access-Token: YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "bc_id": "7012345678901234567",
    "linking_method": "LINK",
    "permission_level": "DELIVER_ADS",
    "permission_detail": {
      "tt_account_roles": [
        "VIDEO_POSTING",
        "LIVE"
      ]
    }
  }'
```

### Ví dụ Python
```python
import requests

url = "https://business-api.tiktok.com/open_api/v1.3/bc/asset/tt_account/link/"
headers = {
    "Access-Token": "YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}
payload = {
    "bc_id": "7012345678901234567",
    "linking_method": "HANDLE",
    "tt_account_handle": "my_brand_store",
    "permission_level": "MANAGE_ACCOUNT",
    "permission_detail": {
      "tt_account_roles": [
        "DIRECT_MESSAGE",
        "SHOWCASE"
      ]
    }
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())
```

### Phản hồi thành công mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202610231213000001",
  "data": {
    "asset_id": "7223344556677889901",
    "link_url": "https://ads.tiktok.com/marketing_api/auth?auth_code=sample_qr_url"
  }
}
```

---

<a id="doc-1879660354954833"></a>
<!-- doc_id: 1879660354954833 -->
<a id="15-hủy-liên-kết-tài-khoản-tiktok-khỏi-business-center"></a>
## 15. Hủy liên kết tài khoản TikTok khỏi Business Center

Sử dụng endpoint này để hủy liên kết một tài khoản TikTok khỏi Business Center. 

> **Cảnh báo:** Một khi tài khoản TikTok bị hủy liên kết khỏi Business Center, tất cả các chiến dịch quảng cáo đang hoạt động sử dụng tài khoản TikTok này có thể bị tạm dừng, và tài khoản TikTok có thể mất quyền truy cập vào [Business Suite](https://ads.tiktok.com/resources/help/article/navigate-web-business-suite).

### Thông tin Endpoint
- **URL:** `https://business-api.tiktok.com/open_api/v1.3/bc/asset/tt_account/unlink/`
- **Phương thức:** `POST`

### Header
| Header | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Có | Access Token được cấp quyền xác thực. |
| Content-Type | string | Có | Kiểu nội dung yêu cầu: `application/json`. |

### Tham số Body (Request Body)
| Tham số | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `bc_id` | string | Có | ID của Business Center. |
| `asset_ids` | string[] | Có | Danh sách mã định danh tài sản của tài khoản TikTok cần hủy liên kết. Tối đa 1 ID trong mảng. |

### Tham số Response
| Trường | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi từ API (`0` là thành công). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Log ID định danh duy nhất của yêu cầu. |
| `data` | object | Dữ liệu trả về (rỗng). |

### Ví dụ cURL
```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/bc/asset/tt_account/unlink/" \
  -H "Access-Token: YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "bc_id": "7012345678901234567",
    "asset_ids": [
      "7223344556677889901"
    ]
  }'
```

### Ví dụ Python
```python
import requests

url = "https://business-api.tiktok.com/open_api/v1.3/bc/asset/tt_account/unlink/"
headers = {
    "Access-Token": "YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}
payload = {
    "bc_id": "7012345678901234567",
    "asset_ids": ["7223344556677889901"]
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())
```

### Phản hồi thành công mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202610231214000001",
  "data": {}
}
```

---

<a id="doc-1846868897541122"></a>
<!-- doc_id: 1846868897541122 -->
<a id="16-lấy-url-ủy-quyền-phân-phối-quảng-cáo-tài-khoản-tiktok"></a>
## 16. Lấy URL ủy quyền phân phối quảng cáo tài khoản TikTok

Sử dụng endpoint này để tạo đường dẫn ủy quyền (authorization URL) dùng để xin cấp quyền phân phối quảng cáo Spark Ads từ một tài khoản TikTok.

Sau khi nhận được URL ủy quyền từ phản hồi, hãy dùng trình tạo mã QR để tạo mã QR và chia sẻ mã này cho chủ sở hữu tài khoản TikTok. Khi chủ tài khoản quét mã QR, họ có thể cấp quyền **"Existing posts"** (bài viết có sẵn cho Spark Ads Pull) và **"TikTok posts"** (đăng bài cho Spark Ads Push) cho Business Center.

### Thông tin Endpoint
- **URL:** `https://business-api.tiktok.com/open_api/v1.3/bc/asset/account/authorization/`
- **Phương thức:** `POST`

### Header
| Header | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Có | Access Token được cấp quyền xác thực. |
| Content-Type | string | Có | Kiểu nội dung yêu cầu: `application/json`. |

### Tham số Body (Request Body)
| Tham số | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `bc_id` | string | Có | ID của Business Center. |
| `is_ads_only_mode` | boolean | Không | Có bật chế độ chỉ hiển thị qua quảng cáo ("Show through ads only") hay không. Khi bật chế độ này, các video do thành viên đăng tải qua Spark Ads Push sẽ chỉ nhận lưu lượng trả phí quảng cáo và bị ẩn khỏi trang hồ sơ công khai (organic feed). Giá trị: `true`/`false`. Mặc định: `false`. |

### Tham số Response
| Trường | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi từ API (`0` là thành công). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Log ID định danh duy nhất của yêu cầu. |
| `data` | object | Dữ liệu trả về. |
| ↳ `bc_auth_qr_code` | string | Đường dẫn URL ủy quyền phân phối quảng cáo của tài khoản TikTok (dùng tạo mã QR để quét). |

### Ví dụ cURL
```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/bc/asset/account/authorization/" \
  -H "Access-Token: YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "bc_id": "7012345678901234567",
    "is_ads_only_mode": true
  }'
```

### Ví dụ Python
```python
import requests

url = "https://business-api.tiktok.com/open_api/v1.3/bc/asset/account/authorization/"
headers = {
    "Access-Token": "YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}
payload = {
    "bc_id": "7012345678901234567",
    "is_ads_only_mode": True
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())
```

### Phản hồi thành công mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202610231215000001",
  "data": {
    "bc_auth_qr_code": "https://ads.tiktok.com/business/spark_auth?qr_token=xyz123abc456"
  }
}
```

---

<a id="doc-1846868953025538"></a>
<!-- doc_id: 1846868953025538 -->
<a id="17-liên-kết-tài-khoản-tiktok-với-tài-khoản-quảng-cáo-trong-business-center"></a>
## 17. Liên kết tài khoản TikTok với tài khoản quảng cáo trong Business Center

Sử dụng endpoint này để liên kết một tài khoản TikTok với một tài khoản quảng cáo nằm trong cùng Business Center.

Sau khi liên kết thành công, các thành viên Business Center có quyền truy cập vào tài khoản quảng cáo đó có thể sử dụng tài khoản TikTok này để tạo và chạy các chiến dịch quảng cáo Spark Ads.

### Thông tin Endpoint
- **URL:** `https://business-api.tiktok.com/open_api/v1.3/bc/asset/advertiser/assign/`
- **Phương thức:** `POST`

### Header
| Header | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Có | Access Token được cấp quyền xác thực. |
| Content-Type | string | Có | Kiểu nội dung yêu cầu: `application/json`. |

### Tham số Body (Request Body)
| Tham số | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `bc_id` | string | Có | ID của Business Center. |
| `asset_id` | string | Có | ID của tài khoản TikTok trong Business Center (lấy qua `/bc/asset/get/` với `asset_type` là `TT_ACCOUNT` hoặc `MANAGED_BUSINESS_ACCOUNT`). |
| `advertiser_id` | string | Có | ID của tài khoản quảng cáo trong cùng Business Center cần được liên kết với tài khoản TikTok. |
| `asset_type` | string | Không | Loại tài sản tài khoản TikTok: `TT_ACCOUNT` (mặc định) hoặc `MANAGED_BUSINESS_ACCOUNT`. |

### Tham số Response
| Trường | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi API (`0` là thành công). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Log ID định danh duy nhất của yêu cầu. |
| `data` | object | Dữ liệu trả về (rỗng). |

### Ví dụ cURL
```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/bc/asset/advertiser/assign/" \
  -H "Access-Token: YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "bc_id": "7012345678901234567",
    "asset_id": "7223344556677889901",
    "advertiser_id": "7112345678901234567",
    "asset_type": "TT_ACCOUNT"
  }'
```

### Ví dụ Python
```python
import requests

url = "https://business-api.tiktok.com/open_api/v1.3/bc/asset/advertiser/assign/"
headers = {
    "Access-Token": "YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}
payload = {
    "bc_id": "7012345678901234567",
    "asset_id": "7223344556677889901",
    "advertiser_id": "7112345678901234567",
    "asset_type": "TT_ACCOUNT"
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())
```

### Phản hồi thành công mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202610231216000001",
  "data": {}
}
```

---

<a id="doc-1855027260369921"></a>
<!-- doc_id: 1855027260369921 -->
<a id="18-hủy-liên-kết-tài-khoản-tiktok-khỏi-tài-khoản-quảng-cáo-trong-business-center"></a>
## 18. Hủy liên kết tài khoản TikTok khỏi tài khoản quảng cáo trong Business Center

Sử dụng endpoint này để gỡ liên kết giữa một tài khoản TikTok và một tài khoản quảng cáo trong Business Center.

Một khi đã gỡ bỏ liên kết, các thành viên Business Center có quyền truy cập vào tài khoản quảng cáo đó sẽ không còn có thể sử dụng tài khoản TikTok này để chạy quảng cáo nữa.

### Thông tin Endpoint
- **URL:** `https://business-api.tiktok.com/open_api/v1.3/bc/asset/advertiser/unassign/`
- **Phương thức:** `POST`

### Header
| Header | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Có | Access Token được cấp quyền xác thực. |
| Content-Type | string | Có | Kiểu nội dung yêu cầu: `application/json`. |

### Tham số Body (Request Body)
| Tham số | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `bc_id` | string | Có | ID của Business Center. |
| `asset_id` | string | Có | ID tài sản tài khoản TikTok trong Business Center. |
| `advertiser_id` | string | Có | ID của tài khoản quảng cáo muốn gỡ liên kết. |
| `asset_type` | string | Không | Loại tài sản: `TT_ACCOUNT` (mặc định) hoặc `MANAGED_BUSINESS_ACCOUNT`. |

### Tham số Response
| Trường | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi từ API (`0` là thành công). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Log ID định danh duy nhất của yêu cầu. |
| `data` | object | Dữ liệu trả về (rỗng). |

### Ví dụ cURL
```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/bc/asset/advertiser/unassign/" \
  -H "Access-Token: YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "bc_id": "7012345678901234567",
    "asset_id": "7223344556677889901",
    "advertiser_id": "7112345678901234567",
    "asset_type": "TT_ACCOUNT"
  }'
```

### Ví dụ Python
```python
import requests

url = "https://business-api.tiktok.com/open_api/v1.3/bc/asset/advertiser/unassign/"
headers = {
    "Access-Token": "YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}
payload = {
    "bc_id": "7012345678901234567",
    "asset_id": "7223344556677889901",
    "advertiser_id": "7112345678901234567",
    "asset_type": "TT_ACCOUNT"
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())
```

### Phản hồi thành công mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202610231217000001",
  "data": {}
}
```

---

<a id="doc-1855027294743554"></a>
<!-- doc_id: 1855027294743554 -->
<a id="19-lấy-danh-sách-tài-khoản-quảng-cáo-liên-kết-với-tài-khoản-tiktok"></a>
## 19. Lấy danh sách tài khoản quảng cáo liên kết với tài khoản TikTok

Sử dụng endpoint này để truy vấn danh sách tất cả các tài khoản quảng cáo đang được liên kết với một tài khoản TikTok cụ thể trong Business Center.

### Thông tin Endpoint
- **URL:** `https://business-api.tiktok.com/open_api/v1.3/bc/asset/advertiser/assigned/`
- **Phương thức:** `GET`

### Header
| Header | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Có | Access Token được cấp quyền xác thực. |

### Tham số Query (Query Parameters)
| Tham số | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `bc_id` | string | Có | ID của Business Center. |
| `asset_id` | string | Có | ID của tài khoản TikTok trong Business Center. |
| `asset_type` | string | Có | Loại tài sản: `TT_ACCOUNT` hoặc `MANAGED_BUSINESS_ACCOUNT`. |
| `page` | number | Không | Số trang hiện tại. Giá trị mặc định: `1`. Dải giá trị: ≥ 1. |
| `page_size` | number | Không | Số lượng kết quả trên mỗi trang. Giá trị mặc định: `10`. Dải giá trị: 1 - 50. |

### Tham số Response
| Trường | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi từ API (`0` là thành công). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Log ID định danh duy nhất của yêu cầu. |
| `data` | object | Dữ liệu trả về. |
| ↳ `list` | object[] | Danh sách tài khoản quảng cáo đã liên kết. |
| ↳↳ `advertiser_id` | string | ID tài khoản quảng cáo. |
| ↳↳ `advertiser_name` | string | Tên tài khoản quảng cáo. |
| ↳ `page_info` | object | Thông tin phân trang. |
| ↳↳ `page` | number | Số trang hiện tại. |
| ↳↳ `page_size` | number | Số lượng bản ghi trên một trang. |
| ↳↳ `total_number` | number | Tổng số lượng tài khoản quảng cáo liên kết. |
| ↳↳ `total_page` | number | Tổng số trang kết quả. |

### Ví dụ cURL
```bash
curl -X GET "https://business-api.tiktok.com/open_api/v1.3/bc/asset/advertiser/assigned/?bc_id=7012345678901234567&asset_id=7223344556677889901&asset_type=TT_ACCOUNT&page=1&page_size=10" \
  -H "Access-Token: YOUR_ACCESS_TOKEN"
```

### Ví dụ Python
```python
import requests

url = "https://business-api.tiktok.com/open_api/v1.3/bc/asset/advertiser/assigned/"
headers = {
    "Access-Token": "YOUR_ACCESS_TOKEN"
}
params = {
    "bc_id": "7012345678901234567",
    "asset_id": "7223344556677889901",
    "asset_type": "TT_ACCOUNT",
    "page": 1,
    "page_size": 10
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

### Phản hồi thành công mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202610231218000001",
  "data": {
    "list": [
      {
        "advertiser_id": "7112345678901234567",
        "advertiser_name": "Acme Brand Global Store"
      }
    ],
    "page_info": {
      "page": 1,
      "page_size": 10,
      "total_number": 1,
      "total_page": 1
    }
  }
}
```

---

<a id="doc-1739659520972802"></a>
<!-- doc_id: 1739659520972802 -->
<a id="20-quản-lý-pixel-trong-business-center"></a>
## 20. Quản lý Pixel trong Business Center (Manage a pixel)

Nhóm API này cho phép bạn quản lý vòng đời và quyền truy cập của mã theo dõi sự kiện Pixel trong Business Center, bao gồm:
- Chuyển quyền sở hữu Pixel từ tài khoản quảng cáo sang Business Center.
- Chia sẻ quyền sử dụng Pixel (liên kết hoặc hủy liên kết) với nhiều tài khoản quảng cáo khác nhau.
- Truy vấn danh sách các tài khoản quảng cáo hiện đang được chia sẻ liên kết với Pixel.

### Danh sách các Endpoint quản lý Pixel:
- [Chuyển giao quyền sở hữu Pixel sang BC](#21-chuyển-giao-quyền-sở-hữu-pixel-từ-nhà-quảng-cáo-sang-bc): `POST /open_api/v1.3/bc/pixel/transfer/`
- [Liên kết hoặc hủy liên kết Pixel với tài khoản quảng cáo](#22-liên-kết-hoặc-hủy-liên-kết-pixel-với-tài-khoản-quảng-cáo): `POST /open_api/v1.3/bc/pixel/link/update/`
- [Lấy danh sách tài khoản quảng cáo liên kết với Pixel](#23-lấy-danh-sách-tài-khoản-quảng-cáo-liên-kết-với-pixel): `GET /open_api/v1.3/bc/pixel/ad_account/list/`

---

<a id="doc-1753994928261122"></a>
<!-- doc_id: 1753994928261122 -->
<a id="21-chuyển-giao-quyền-sở-hữu-pixel-từ-nhà-quảng-cáo-sang-bc"></a>
## 21. Chuyển giao quyền sở hữu Pixel từ nhà quảng cáo sang BC

Sử dụng endpoint này để chuyển quyền sở hữu của một mã theo dõi Pixel từ tài khoản quảng cáo ban đầu về Business Center quản lý tập trung.

### Điều kiện chuyển giao thành công:
1. Nếu Pixel được chuyển sang Business Center loại **Agency** (Đại lý): Thao tác phải được thực hiện bởi người dùng Quản trị viên (Admin) của Agency BC. Đồng thời, tài khoản quảng cáo gắn với Pixel ban đầu phải do chính Agency BC này sở hữu.
2. Nếu Pixel được chuyển sang Business Center loại **Direct** (Trực tiếp): Direct BC phải có quyền Quản trị viên (Admin permission) trên tài khoản quảng cáo gắn với Pixel ban đầu.

### Thông tin Endpoint
- **URL:** `https://business-api.tiktok.com/open_api/v1.3/bc/pixel/transfer/`
- **Phương thức:** `POST`

### Header
| Header | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Có | Access Token được cấp quyền xác thực. |
| Content-Type | string | Có | Kiểu nội dung yêu cầu: `application/json`. |

### Tham số Body (Request Body)
| Tham số | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `bc_id` | string | Có | ID của Business Center tiếp nhận chuyển giao quyền sở hữu Pixel. |
| `pixel_code` | string | Có | Mã Pixel (Pixel Code) bạn muốn chuyển giao sang Business Center. |

### Tham số Response
| Trường | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi từ API (`0` là thành công). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Log ID định danh duy nhất của yêu cầu. |
| `data` | object | Dữ liệu trả về. |
| ↳ `asset_id` | string | ID tài sản Pixel trong Business Center sau khi chuyển giao thành công. |

### Ví dụ cURL
```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/bc/pixel/transfer/" \
  -H "Access-Token: YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "bc_id": "7012345678901234567",
    "pixel_code": "C712345678901234567"
  }'
```

### Ví dụ Python
```python
import requests

url = "https://business-api.tiktok.com/open_api/v1.3/bc/pixel/transfer/"
headers = {
    "Access-Token": "YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}
payload = {
    "bc_id": "7012345678901234567",
    "pixel_code": "C712345678901234567"
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())
```

### Phản hồi thành công mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202610231219000001",
  "data": {
    "asset_id": "7223344556677889902"
  }
}
```

---

<a id="doc-1753994950327297"></a>
<!-- doc_id: 1753994950327297 -->
<a id="22-liên-kết-hoặc-hủy-liên-kết-pixel-với-tài-khoản-quảng-cáo"></a>
## 22. Liên kết hoặc hủy liên kết Pixel với tài khoản quảng cáo

Sử dụng endpoint này để chia sẻ quyền sử dụng một Pixel trong Business Center cho các tài khoản quảng cáo khác, hoặc thu hồi quyền sử dụng (hủy liên kết) Pixel khỏi các tài khoản quảng cáo.

### Thông tin Endpoint
- **URL:** `https://business-api.tiktok.com/open_api/v1.3/bc/pixel/link/update/`
- **Phương thức:** `POST`

### Header
| Header | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Có | Access Token được cấp quyền xác thực. |
| Content-Type | string | Có | Kiểu nội dung yêu cầu: `application/json`. |

### Tham số Body (Request Body)
| Tham số | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `bc_id` | string | Có | ID của Business Center sở hữu Pixel. |
| `pixel_code` | string | Có | Mã Pixel (Pixel Code) cần cập nhật liên kết. |
| `advertiser_ids` | string[] | Có | Danh sách ID các tài khoản quảng cáo cần liên kết hoặc hủy liên kết. |
| `relation_status` | string | Có | Hành động cập nhật quan hệ:<ul><li>`LINK`: Chia sẻ liên kết Pixel với các tài khoản quảng cáo.</li><li>`UNLINK`: Hủy liên kết Pixel khỏi các tài khoản quảng cáo.</li></ul> |

### Tham số Response
| Trường | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi từ API (`0` là thành công). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Log ID định danh duy nhất của yêu cầu. |
| `data` | object | Dữ liệu trả về (rỗng khi cập nhật thành công). |

### Ví dụ cURL
```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/bc/pixel/link/update/" \
  -H "Access-Token: YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "bc_id": "7012345678901234567",
    "pixel_code": "C712345678901234567",
    "advertiser_ids": [
      "7112345678901234567"
    ],
    "relation_status": "LINK"
  }'
```

### Ví dụ Python
```python
import requests

url = "https://business-api.tiktok.com/open_api/v1.3/bc/pixel/link/update/"
headers = {
    "Access-Token": "YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}
payload = {
    "bc_id": "7012345678901234567",
    "pixel_code": "C712345678901234567",
    "advertiser_ids": ["7112345678901234567"],
    "relation_status": "LINK"
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())
```

### Phản hồi thành công mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202610231220000001",
  "data": {}
}
```

---

<a id="doc-1753994966965249"></a>
<!-- doc_id: 1753994966965249 -->
<a id="23-lấy-danh-sách-tài-khoản-quảng-cáo-liên-kết-với-pixel"></a>
## 23. Lấy danh sách tài khoản quảng cáo liên kết với Pixel

Sử dụng endpoint này để truy vấn danh sách tất cả các tài khoản quảng cáo hiện đang được liên kết và có quyền sử dụng một Pixel cụ thể trong Business Center.

### Thông tin Endpoint
- **URL:** `https://business-api.tiktok.com/open_api/v1.3/bc/pixel/ad_account/list/`
- **Phương thức:** `GET`

### Header
| Header | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Có | Access Token được cấp quyền xác thực. |

### Tham số Query (Query Parameters)
| Tham số | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `bc_id` | string | Có | ID của Business Center sở hữu Pixel. |
| `pixel_code` | string | Có | Mã Pixel (Pixel Code) cần truy vấn. |
| `page` | number | Không | Số trang hiện tại. Mặc định: `1`. Dải giá trị: ≥ 1. |
| `page_size` | number | Không | Số lượng kết quả trên một trang. Mặc định: `10`. Dải giá trị: 1 - 50. |

### Tham số Response
| Trường | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi từ API (`0` là thành công). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Log ID định danh duy nhất của yêu cầu. |
| `data` | object | Dữ liệu trả về. |
| ↳ `list` | object[] | Danh sách tài khoản quảng cáo đang liên kết với Pixel. |
| ↳↳ `advertiser_id` | string | ID tài khoản quảng cáo. |
| ↳↳ `advertiser_name` | string | Tên tài khoản quảng cáo. |
| ↳ `page_info` | object | Thông tin phân trang (`page`, `page_size`, `total_number`, `total_page`). |

### Ví dụ cURL
```bash
curl -X GET "https://business-api.tiktok.com/open_api/v1.3/bc/pixel/ad_account/list/?bc_id=7012345678901234567&pixel_code=C712345678901234567&page=1&page_size=10" \
  -H "Access-Token: YOUR_ACCESS_TOKEN"
```

### Ví dụ Python
```python
import requests

url = "https://business-api.tiktok.com/open_api/v1.3/bc/pixel/ad_account/list/"
headers = {
    "Access-Token": "YOUR_ACCESS_TOKEN"
}
params = {
    "bc_id": "7012345678901234567",
    "pixel_code": "C712345678901234567",
    "page": 1,
    "page_size": 10
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

### Phản hồi thành công mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202610231221000001",
  "data": {
    "list": [
      {
        "advertiser_id": "7112345678901234567",
        "advertiser_name": "Acme Brand Global Store"
      }
    ],
    "page_info": {
      "page": 1,
      "page_size": 10,
      "total_number": 1,
      "total_page": 1
    }
  }
}
```

---

<a id="doc-1739663268166722"></a>
<!-- doc_id: 1739663268166722 -->
<a id="24-lấy-danh-sách-đối-tác-theo-tài-sản"></a>
## 24. Lấy danh sách đối tác theo tài sản (Get partners by asset)

Sử dụng endpoint này để lấy danh sách các đối tác (Business Center khác) đang được chia sẻ quyền sử dụng một tài sản cụ thể trong Business Center của bạn. Bạn cần có vai trò Quản trị viên (Admin) trong Business Center.

### Thông tin Endpoint
- **URL:** `https://business-api.tiktok.com/open_api/v1.3/bc/asset/partner/list/`
- **Phương thức:** `GET`

### Header
| Header | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Có | Access Token được cấp quyền xác thực. |

### Tham số Query (Query Parameters)
| Tham số | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `bc_id` | string | Có | ID của Business Center. |
| `asset_id` | string | Có | ID của tài sản cần truy vấn danh sách đối tác. |
| `asset_type` | string | Có | Loại tài sản cần truy vấn. Các giá trị enum: `ADVERTISER`, `CATALOG`, `PIXEL`, `LEAD`, `TIKTOK_SHOP`. |
| `filtering` | object | Không | Điều kiện lọc danh sách đối tác. |
| ↳ `keyword` | string | Không | Từ khóa tìm kiếm theo tên hoặc mã Business Center đối tác. |
| `page` | number | Không | Số trang hiện tại. Mặc định: `1`. Dải giá trị: ≥ 1. |
| `page_size` | number | Không | Số lượng kết quả trên một trang. Mặc định: `10`. Dải giá trị: 1 - 50. |

### Tham số Response
| Trường | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi từ API (`0` là thành công). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Log ID định danh duy nhất của yêu cầu. |
| `data` | object | Dữ liệu trả về. |
| ↳ `list` | object[] | Danh sách đối tác đang được cấp quyền. |
| ↳↳ `partner_id` | string | ID của Business Center đối tác. |
| ↳↳ `partner_name` | string | Tên của Business Center đối tác. |
| ↳↳ `role` | string | Vai trò hoặc cấp độ quyền đối tác được cấp trên tài sản. |
| ↳ `page_info` | object | Thông tin phân trang (`page`, `page_size`, `total_number`, `total_page`). |

### Ví dụ cURL
```bash
curl -X GET "https://business-api.tiktok.com/open_api/v1.3/bc/asset/partner/list/?bc_id=7012345678901234567&asset_id=7112345678901234567&asset_type=ADVERTISER&page=1&page_size=10" \
  -H "Access-Token: YOUR_ACCESS_TOKEN"
```

### Ví dụ Python
```python
import requests

url = "https://business-api.tiktok.com/open_api/v1.3/bc/asset/partner/list/"
headers = {
    "Access-Token": "YOUR_ACCESS_TOKEN"
}
params = {
    "bc_id": "7012345678901234567",
    "asset_id": "7112345678901234567",
    "asset_type": "ADVERTISER",
    "page": 1,
    "page_size": 10
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

### Phản hồi thành công mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202610231222000001",
  "data": {
    "list": [
      {
        "partner_id": "7099999888877776666",
        "partner_name": "Partner Media Agency Global",
        "role": "ADVERTISER_ROLE_OPERATOR"
      }
    ],
    "page_info": {
      "page": 1,
      "page_size": 10,
      "total_number": 1,
      "total_page": 1
    }
  }
}
```

---

<a id="doc-1739659558931458"></a>
<!-- doc_id: 1739659558931458 -->
<a id="25-lấy-danh-sách-thành-viên-theo-tài-sản"></a>
## 25. Lấy danh sách thành viên theo tài sản (Get members by asset)

Sử dụng endpoint này để lấy danh sách các thành viên trong Business Center đang được phân quyền truy cập và quản lý một tài sản cụ thể. Bạn cần có quyền Quản trị viên (Admin) của Business Center.

### Thông tin Endpoint
- **URL:** `https://business-api.tiktok.com/open_api/v1.3/bc/asset/member/list/`
- **Phương thức:** `GET`

### Header
| Header | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Có | Access Token được cấp quyền xác thực. |

### Tham số Query (Query Parameters)
| Tham số | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `bc_id` | string | Có | ID của Business Center. |
| `asset_id` | string | Có | ID của tài sản cần truy vấn danh sách thành viên. |
| `asset_type` | string | Có | Loại tài sản: `ADVERTISER`, `CATALOG`, `PIXEL`, `LEAD`, `TIKTOK_SHOP`, `TT_ACCOUNT`, `MANAGED_BUSINESS_ACCOUNT`. |
| `filtering` | object | Không | Điều kiện lọc danh sách thành viên. |
| ↳ `keyword` | string | Không | Từ khóa tìm kiếm theo tên hoặc email của thành viên. |
| `page` | number | Không | Số trang hiện tại. Mặc định: `1`. Dải giá trị: ≥ 1. |
| `page_size` | number | Không | Số lượng kết quả trên một trang. Mặc định: `10`. Dải giá trị: 1 - 50. |

### Tham số Response
| Trường | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi từ API (`0` là thành công). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Log ID định danh duy nhất của yêu cầu. |
| `data` | object | Dữ liệu trả về. |
| ↳ `list` | object[] | Danh sách thành viên được phân quyền trên tài sản. |
| ↳↳ `user_id` | string | ID của thành viên Business Center. |
| ↳↳ `user_name` | string | Tên của thành viên. |
| ↳↳ `user_email` | string | Email của thành viên. |
| ↳↳ `role` | string | Vai trò cụ thể của thành viên trên tài sản này. |
| ↳ `page_info` | object | Thông tin phân trang (`page`, `page_size`, `total_number`, `total_page`). |

### Ví dụ cURL
```bash
curl -X GET "https://business-api.tiktok.com/open_api/v1.3/bc/asset/member/list/?bc_id=7012345678901234567&asset_id=7112345678901234567&asset_type=ADVERTISER&page=1&page_size=10" \
  -H "Access-Token: YOUR_ACCESS_TOKEN"
```

### Ví dụ Python
```python
import requests

url = "https://business-api.tiktok.com/open_api/v1.3/bc/asset/member/list/"
headers = {
    "Access-Token": "YOUR_ACCESS_TOKEN"
}
params = {
    "bc_id": "7012345678901234567",
    "asset_id": "7112345678901234567",
    "asset_type": "ADVERTISER",
    "page": 1,
    "page_size": 10
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

### Phản hồi thành công mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202610231223000001",
  "data": {
    "list": [
      {
        "user_id": "7098765432109876543",
        "user_name": "Nguyen Van A",
        "user_email": "vana@example.com",
        "role": "ROLE_ADVERTISER_ADMIN"
      }
    ],
    "page_info": {
      "page": 1,
      "page_size": 10,
      "total_number": 1,
      "total_page": 1
    }
  }
}
```

---

<a id="doc-1739657251102722"></a>
<!-- doc_id: 1739657251102722 -->
<a id="26-xóa-tài-sản-khỏi-business-center"></a>
## 26. Xóa tài sản khỏi Business Center (Delete assets)

Sử dụng endpoint này để xóa các tài sản khỏi Business Center. Bạn cần có quyền Quản trị viên (Admin) của Business Center.

Các loại tài sản được hỗ trợ xóa bao gồm danh sách khách hàng tiềm năng (`LEAD`) và tài khoản TikTok (`TT_ACCOUNT`).

> **Lưu ý quan trọng:**
> - Khi `asset_type` là `LEAD`, bạn chỉ có thể xóa từng thư viện biểu mẫu lead một lần. Một khi đã xóa khỏi Business Center, biểu mẫu lead sẽ được chuyển trả về tài khoản quảng cáo ban đầu mà nó từng thuộc về.

### Thông tin Endpoint
- **URL:** `https://business-api.tiktok.com/open_api/v1.3/bc/asset/admin/delete/`
- **Phương thức:** `POST`

### Header
| Header | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Có | Access Token được cấp quyền xác thực. |
| Content-Type | string | Có | Kiểu nội dung yêu cầu: `application/json`. |

### Tham số Body (Request Body)
| Tham số | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `bc_id` | string | Có | ID của Business Center. |
| `asset_ids` | string[] | Có | Danh sách ID tài sản cần xóa. Hiện tại hệ thống chỉ cho phép truyền tối đa 1 ID trong mảng:<ul><li>`library_id` khi `asset_type` là `LEAD`.</li><li>Mã định danh tài khoản TikTok trong Business Center khi `asset_type` là `TT_ACCOUNT`.</li></ul> |
| `asset_type` | string | Có | Loại tài sản cần xóa. Các giá trị enum: `LEAD`, `TT_ACCOUNT` (tương ứng định danh `BC_AUTH_TT`). |

### Tham số Response
| Trường | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi từ API (`0` là thành công). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Log ID định danh duy nhất của yêu cầu. |
| `data` | object | Dữ liệu trả về (rỗng). |

### Ví dụ cURL
```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/bc/asset/admin/delete/" \
  -H "Access-Token: YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "bc_id": "7012345678901234567",
    "asset_ids": [
      "7223344556677889901"
    ],
    "asset_type": "TT_ACCOUNT"
  }'
```

### Ví dụ Python
```python
import requests

url = "https://business-api.tiktok.com/open_api/v1.3/bc/asset/admin/delete/"
headers = {
    "Access-Token": "YOUR_ACCESS_TOKEN",
    "Content-Type": "application/json"
}
payload = {
    "bc_id": "7012345678901234567",
    "asset_ids": ["7223344556677889901"],
    "asset_type": "TT_ACCOUNT"
}

response = requests.post(url, headers=headers, json=payload)
print(response.json())
```

### Phản hồi thành công mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202610231224000001",
  "data": {}
}
```

---

<a id="doc-1739659584022529"></a>
<!-- doc_id: 1739659584022529 -->
<a id="27-lấy-thông-tin-liên-kết-của-tài-sản"></a>
## 27. Lấy thông tin liên kết của tài sản (Get binding info)

Sử dụng endpoint này để kiểm tra xem một tài sản hiện đã được liên kết với bao nhiêu quảng cáo và tài sản này còn có thể liên kết thêm với tối đa bao nhiêu quảng cáo nữa. Mỗi tài sản chỉ có thể được sử dụng để tạo một số lượng quảng cáo nhất định theo hạn ngạch hệ thống.

### Thông tin Endpoint
- **URL:** `https://business-api.tiktok.com/open_api/v1.3/asset/bind/quota/`
- **Phương thức:** `GET`

### Header
| Header | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| Access-Token | string | Có | Access Token được cấp quyền xác thực. |

### Tham số Query (Query Parameters)
| Tham số | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | Có | ID của tài khoản quảng cáo. |
| `asset_id` | string | Có | ID của tài sản cần kiểm tra hạn mức liên kết. |
| `asset_type` | string | Có | Loại tài sản cần kiểm tra. Giá trị enum: `IDENTITY`. |

### Tham số Response
| Trường | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi từ API (`0` là thành công). |
| `message` | string | Thông báo phản hồi. |
| `request_id` | string | Log ID định danh duy nhất của yêu cầu. |
| `data` | object | Dữ liệu trả về. |
| ↳ `total_quota` | number | Tổng số lượng quảng cáo tối đa mà tài sản này có thể liên kết. |
| ↳ `used_quota` | number | Số lượng quảng cáo hiện tại mà tài sản này đã liên kết. |
| ↳ `available_quota` | number | Số lượng quảng cáo còn lại khả dụng mà tài sản có thể tiếp tục liên kết. |

### Ví dụ cURL
```bash
curl -X GET "https://business-api.tiktok.com/open_api/v1.3/asset/bind/quota/?advertiser_id=7112345678901234567&asset_id=7223344556677889901&asset_type=IDENTITY" \
  -H "Access-Token: YOUR_ACCESS_TOKEN"
```

### Ví dụ Python
```python
import requests

url = "https://business-api.tiktok.com/open_api/v1.3/asset/bind/quota/"
headers = {
    "Access-Token": "YOUR_ACCESS_TOKEN"
}
params = {
    "advertiser_id": "7112345678901234567",
    "asset_id": "7223344556677889901",
    "asset_type": "IDENTITY"
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

### Phản hồi thành công mẫu
```json
{
  "code": 0,
  "message": "OK",
  "request_id": "202610231225000001",
  "data": {
    "total_quota": 50,
    "used_quota": 12,
    "available_quota": 38
  }
}
```
