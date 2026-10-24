# Creative Portfolios API — Quản Lý Danh Mục Tài Sản Sáng Tạo

> **Phân hệ**: Creative API > Creative Portfolios & Asset Management  
> **Phiên bản API**: TikTok Business Marketing API v1.3  
> **Giao thức gọi**: RESTful API với **100% lệnh mẫu bằng cURL**

---

## 📌 1. Giới thiệu tổng quan

Creative Portfolios API giúp doanh nghiệp và Agency quản lý tập trung toàn bộ tài sản đa phương tiện:
- Nhóm các video, hình ảnh và trang đích theo từng chiến dịch hoặc dòng sản phẩm vào các danh mục (Portfolios).
- Phân quyền và **chia sẻ tài sản (Asset Sharing)** an toàn giữa nhiều tài khoản quảng cáo khác nhau trong cùng Business Center.
- Dọn dẹp và xóa các tài sản cũ không còn sử dụng để tối ưu dung lượng thư viện.

---

## 🚀 2. Danh sách Endpoints & Hướng dẫn cURL

### 2.1. Tạo danh mục sáng tạo mới (`/creative/portfolio/create/`)

- **Endpoint**: `POST https://business-api.tiktok.com/open_api/v1.3/creative/portfolio/create/`
- **Phương thức**: `POST`

```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/creative/portfolio/create/" \
  -H "Access-Token: 0123456789abcdef0123456789abcdef01234567" \
  -H "Content-Type: application/json" \
  -d '{
    "advertiser_id": "7123456789012345678",
    "portfolio_name": "Bộ Sưu Tập Tết 2026",
    "portfolio_type": "VIDEO",
    "material_ids": [
      "v10033g50000cf7m1g3c77u3g2example",
      "v10033g50000cf7m1g3c77u3g2sample2"
    ]
  }'
```

---

### 2.2. Lấy danh sách danh mục sáng tạo (`/creative/portfolio/list/`)

- **Endpoint**: `GET https://business-api.tiktok.com/open_api/v1.3/creative/portfolio/list/`
- **Phương thức**: `GET`

```bash
curl -X GET "https://business-api.tiktok.com/open_api/v1.3/creative/portfolio/list/?advertiser_id=7123456789012345678&page=1&page_size=20" \
  -H "Access-Token: 0123456789abcdef0123456789abcdef01234567" \
  -H "Content-Type: application/json"
```

---

### 2.3. Chia sẻ tài nguyên sáng tạo sang tài khoản khác (`/creative/asset/share/`)

Cho phép chia sẻ video hoặc hình ảnh sang các tài khoản quảng cáo vệ tinh mà không cần tải lại tệp tin.

- **Endpoint**: `POST https://business-api.tiktok.com/open_api/v1.3/creative/asset/share/`
- **Phương thức**: `POST`

```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/creative/asset/share/" \
  -H "Access-Token: 0123456789abcdef0123456789abcdef01234567" \
  -H "Content-Type: application/json" \
  -d '{
    "advertiser_id": "7123456789012345678",
    "target_advertiser_ids": ["7987654321098765432"],
    "asset_type": "VIDEO",
    "asset_ids": ["v10033g50000cf7m1g3c77u3g2example"]
  }'
```

---

### 2.4. Xóa tài nguyên sáng tạo (`/creative/asset/delete/`)

- **Endpoint**: `POST https://business-api.tiktok.com/open_api/v1.3/creative/asset/delete/`
- **Phương thức**: `POST`

```bash
curl -X POST "https://business-api.tiktok.com/open_api/v1.3/creative/asset/delete/" \
  -H "Access-Token: 0123456789abcdef0123456789abcdef01234567" \
  -H "Content-Type: application/json" \
  -d '{
    "advertiser_id": "7123456789012345678",
    "asset_type": "VIDEO",
    "asset_ids": ["v10033g50000cf7m1g3c77u3g2oldvideo"]
  }'
```
