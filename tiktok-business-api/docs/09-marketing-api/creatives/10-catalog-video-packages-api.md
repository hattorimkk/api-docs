# Catalog Video Packages API — Gói Video Tự Động Cho Danh Mục Sản Phẩm

> **Phân hệ**: Creative API > Dynamic Catalog Video  
> **Phiên bản API**: TikTok Business Marketing API v1.3  
> **Giao thức gọi**: RESTful API với **100% lệnh mẫu bằng cURL**

---

## 📌 1. Giới thiệu tổng quan

Đối với các nhà bán lẻ thương mại điện tử có hàng nghìn mã sản phẩm (SKU) trong Catalog, việc sản xuất video thủ công cho từng sản phẩm là điều bất khả thi.

**Catalog Video Packages API** giải quyết bài toán này bằng cách:
- Tự động lấy hình ảnh sản phẩm, giá bán, tên sản phẩm và mức giảm giá từ nguồn dữ liệu Catalog (Product Feed).
- Ghép vào các mẫu video chuyển động có sẵn (Video Templates) để tự động kết xuất (render) hàng loạt video chất lượng cao cho toàn bộ danh mục sản phẩm.

---

## 🚀 2. Danh sách Endpoints & Hướng dẫn cURL

### 2.1. Tạo gói video tự động cho catalog (`/catalog/video_package/create/`)

- **Endpoint**: `POST https://business-api.tiktok.com/open_api/v1.3/catalog/video_package/create/`
- **Phương thức**: `POST`

```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/catalog/video_package/create/" \
  -H "Access-Token: 0123456789abcdef0123456789abcdef01234567" \
  -H "Content-Type: application/json" \
  -d '{
    "advertiser_id": "7123456789012345678",
    "catalog_id": "7192837465019283746",
    "package_name": "Goi_Video_Catalog_Tet_2026",
    "template_id": "7291823746501928374",
    "product_set_id": "7198273645123984512"
  }'
```

#### Phản hồi mẫu (JSON Response)

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20261023225120010245041042005M1N2O",
  "data": {
    "package_id": "vp_20261023_987654321",
    "status": "PROCESSING"
  }
}
```

---

### 2.2. Lấy thông tin gói video catalog (`/catalog/video_package/get/`)

- **Endpoint**: `GET https://business-api.tiktok.com/open_api/v1.3/catalog/video_package/get/`
- **Phương thức**: `GET`

```bash
curl -X GET "https://business-api.tiktok.com/open_api/v1.3/catalog/video_package/get/?advertiser_id=7123456789012345678&catalog_id=7192837465019283746&package_id=vp_20261023_987654321" \
  -H "Access-Token: 0123456789abcdef0123456789abcdef01234567" \
  -H "Content-Type: application/json"
```

---

### 2.3. Xem trước video sản phẩm theo mẫu template (`/catalog/template_preview/create/`)

Sinh video mẫu xem trước cho 1 sản phẩm cụ thể để kiểm tra bố cục hiển thị giá và tên sản phẩm trước khi tạo cho toàn bộ danh mục.

- **Endpoint**: `POST https://business-api.tiktok.com/open_api/v1.3/catalog/template_preview/create/`
- **Phương thức**: `POST`

```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/catalog/template_preview/create/" \
  -H "Access-Token: 0123456789abcdef0123456789abcdef01234567" \
  -H "Content-Type: application/json" \
  -d '{
    "advertiser_id": "7123456789012345678",
    "catalog_id": "7192837465019283746",
    "template_id": "7291823746501928374",
    "product_id": "SKU_AO_THUN_TET_01"
  }'
```
