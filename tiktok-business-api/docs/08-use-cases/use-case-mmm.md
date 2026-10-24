# Use case: yêu cầu dữ liệu Media Mix Modeling

Tài liệu này hướng dẫn quy trình từng bước yêu cầu và tải xuống dữ liệu Media Mix Modeling (MMM) thông qua TikTok API. Bạn sẽ tìm hiểu cách thiết lập điều kiện tiên quyết trong Business Center, phạm vi quyền hạn (scope) cần thiết, và các bước tạo yêu cầu, kiểm tra tiến độ cho đến khi nhận được URL tải xuống tệp dữ liệu MMM.

## Yêu cầu dữ liệu Media Mix Modeling (`Media Mix Modeling data request`)
<a id="doc-1825298892472513"></a>
<!-- doc_id: 1825298892472513 -->

> Đường dẫn: Use Cases > Media Mix Modeling data request

Bài viết này hướng dẫn bạn từng bước truy cập dữ liệu Media Mix Modeling (MMM) qua API.

### Giới thiệu (Introduction)

Mô hình hóa Phối thức Truyền thông (Media Mix Modeling - MMM) là một kỹ thuật đo lường tận dụng mô hình chuỗi thời gian để thấu hiểu tác động kinh doanh (giá trị) của tất cả các điểm chạm tiếp thị truyền thống và kỹ thuật số. Bằng cách tính toán các hoạt động vận hành như định giá, các yếu tố bên ngoài và các chỉ số kinh tế, MMM có thể định lượng ROI trên khắp các kênh truyền thông của nhà quảng cáo và cung cấp thông tin chuyên sâu cho việc lập kế hoạch chi tiêu truyền thông trong tương lai.

**Bạn có thể sử dụng MMM API để truy cập dữ liệu MMM; điều này giúp bạn hợp lý hóa trải nghiệm yêu cầu dữ liệu MMM, đồng thời nâng cao hiệu quả vận hành và khả năng mở rộng.**

### Điều kiện tiên quyết (Prerequisites)

- Bạn đã được cấp quyền truy cập TikTok API for Business. Xem chi tiết tại [Bắt đầu - Quy trình từng bước](../04-get-started/bat-dau.md#doc-1735713609895937). Đảm bảo bạn đã hoàn thành việc [ủy quyền Marketing API](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373141733378) và [xác thực](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162).
- Bạn cần các quyền liên quan. Xem **Tham chiếu API (API Reference)** để biết quyền cần thiết cho các endpoint (bao gồm các endpoint trong mục "Các bước thực hiện") và xem [Cập nhật quyền ứng dụng](../04-get-started/bat-dau.md#doc-1738855280338946) để biết cách cấu hình quyền. Hãy đảm bảo ứng dụng nhà phát triển của bạn có phạm vi quyền **MMM Data Report** trong mục **Reporting**.
- Việc truy cập dữ liệu MMM qua API yêu cầu thiết lập tài khoản quảng cáo trong Business Center trước:
  1. Thêm các tài khoản quảng cáo vào Business Center. Bạn có thể tạo tài khoản quảng cáo trong Business Center bằng [/bc/advertiser/create/](../12-api-reference/15-bc-assets.md#doc-1739939020318721) hoặc [yêu cầu quyền truy cập tài khoản quảng cáo trong Business Center](https://ads.tiktok.com/help/article/request-access-to-ad-accounts-in-business-center).
  2. Đảm bảo bạn có quyền truy cập vào các tài khoản quảng cáo mà bạn muốn lấy dữ liệu MMM. Để thực hiện việc này, hãy gọi [/bc/asset/get/](../12-api-reference/15-bc-assets.md#doc-1739432717798401) và đặt `asset_type` thành `ADVERTISER`.
Nếu `advertiser_role` trả về cho tài khoản quảng cáo không phải là `ADMIN`, `OPERATOR` hoặc `ANALYST`, bạn chưa có quyền truy cập vào các tài khoản quảng cáo này. Hãy yêu cầu quản trị viên của Business Center chia sẻ tài khoản quảng cáo với bạn và cấp quyền truy cập bằng [/bc/asset/assign/](../12-api-reference/15-bc-assets.md#doc-1739438211077121). Quản trị viên Business Center cần chỉ định `asset_type` là `ADVERTISER` và `advertiser_role` là `ADMIN`, `OPERATOR` hoặc `ANALYST`.

### Các bước thực hiện (Steps)

1. **Tạo yêu cầu dữ liệu MMM** bằng [/mmm/api/create/](../12-api-reference/49-media-mix-modeling.md#doc-1825299567855617).

**Ví dụ:**

Yêu cầu (Request)
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/mmm/api/create/' \
--header 'Access-Token: {{Access-Token}}'
--header 'Content-Type: application/json' \
--data-raw '{
    "advertiser_ids": [
        "{{advertiser_id}}"
    ],
    "request_info": {
        "targets": [
            {
                "advertiser_id": "{{advertiser_id}}"
            }
        ],
        "from_date": "2024-01-01",
        "to_date": "2024-01-03",
        "country_code": [
            "JP","US","CA"
        ],
        "media_type": "All"
    },
    "email": "{{email}}"
}'
```

Phản hồi (Response)
```http
// curl
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "mmm_request_id": "{{mmm_request_id}}"
    }
}
```

2. **Kiểm tra trạng thái yêu cầu dữ liệu** bằng [/mmm/api/check/](../12-api-reference/49-media-mix-modeling.md#doc-1825299576698882).

**Ví dụ:**

Yêu cầu (Request)
```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/mmm/api/check/?mmm_request_id={{mmm_request_id}}' \
--header 'Access-Token: {{Access-Token}}'
```

Phản hồi (Response)
```http
// curl
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "status": "completed - ready for download"
    }
}
```

3. Khi bạn xác nhận `status` của yêu cầu dữ liệu là `completed - ready for download`, **lấy URL tải xuống dữ liệu** bằng [/mmm/api/download/](../12-api-reference/49-media-mix-modeling.md#doc-1825299584678017).

Để tìm hiểu về các trường dữ liệu MMM khả dụng, hãy xem [Lược đồ dữ liệu mẫu MMM (MMM templated data schema)](https://bytedance.sg.larkoffice.com/sheets/YDwDsKe5whGQWdtaZVrlD9BHgIc).

**Ví dụ:**

Yêu cầu (Request)
```http
// curl
curl --location  --request GET 'https://business-api.tiktok.com/open_api/v1.3/mmm/api/download/?mmm_request_id={{mmm_request_id}}' \
--header 'Access-Token: {{Access-Token}}'
```

Phản hồi (Response)
```http
// curl
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "download_url": "{{download_url}}"
    }
}
```
