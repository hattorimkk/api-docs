# Tham Khảo API: Quảng Cáo Shopee & Tiếp Thị Liên Kết (Shopee Ads & AMS)

Tài liệu này cung cấp chi tiết đặc tả kỹ thuật và câu lệnh **cURL** cho phân hệ Quản lý Chiến dịch Quảng cáo Tìm kiếm / Khám phá (`v2.ads`) và Tiếp thị liên kết Affiliate Marketing Solutions (`v2.ams`) trên Shopee Open Platform.

---

## PHẦN 1: QUẢNG CÁO SHOPEE (Shopee Ads)

Shopee Ads cho phép người bán quảng cáo sản phẩm lên top tìm kiếm và trang gợi ý sản phẩm liên quan.

### 1.1. Lấy Danh Sách Chiến Dịch Quảng Cáo Đang Chạy
- **Endpoint**: `v2.ads.get_campaign_list`
- **Đường dẫn**: `GET /api/v2/ads/get_campaign_list`
- **Loại API**: Shop API

```bash
curl -X GET "https://partner.shopeemobile.com/api/v2/ads/get_campaign_list?partner_id=123456&timestamp=1700000000&access_token=c71a39d892ef65a43b1234567890abcd&shop_id=98765432&sign=calculated_sign_here&page_no=1&page_size=50" \
  -H "Content-Type: application/json"
```

### 1.2. Trích Xuất Báo Cáo Hiệu Quả Quảng Cáo (Ads Performance Report)
Endpoint này dùng để trích xuất số lượt hiển thị (Impressions), số click, chi phí quảng cáo (Expense), doanh thu mang lại (GMV) và chỉ số hoàn vốn đầu tư quảng cáo (ROAS / CIR).

- **Endpoint**: `v2.ads.get_item_hourly_performance`
- **Đường dẫn**: `GET /api/v2/ads/get_item_hourly_performance`

```bash
curl -X GET "https://partner.shopeemobile.com/api/v2/ads/get_item_hourly_performance?partner_id=123456&timestamp=1700000000&access_token=c71a39d892ef65a43b1234567890abcd&shop_id=98765432&sign=calculated_sign_here&item_id=1122334455&start_date=2026-10-01&end_date=2026-10-20" \
  -H "Content-Type: application/json"
```

---

## PHẦN 2: TIẾP THỊ LIÊN KẾT (Affiliate Marketing Solutions - AMS)

Shopee AMS giúp người bán hợp tác với mạng lưới KOL/KOC và Publisher để tăng doanh số và trả hoa hồng dựa trên đơn hàng phát sinh (CPS - Cost Per Sale).

### 2.1. Lấy Danh Sách Chiến Dịch Tiếp Thị Liên Kết (Get AMS Campaigns)
- **Endpoint**: `v2.ams.get_campaign_list`
- **Đường dẫn**: `GET /api/v2/ams/get_campaign_list`
- **Loại API**: Shop API

```bash
curl -X GET "https://partner.shopeemobile.com/api/v2/ams/get_campaign_list?partner_id=123456&timestamp=1700000000&access_token=c71a39d892ef65a43b1234567890abcd&shop_id=98765432&sign=calculated_sign_here&page_size=20" \
  -H "Content-Type: application/json"
```

### 2.2. Trích Xuất Báo Cáo Doanh Thu Qua KOL/KOC (AMS Performance Report)
- **Endpoint**: `v2.ams.get_performance`
- **Đường dẫn**: `GET /api/v2/ams/get_performance`

```bash
curl -X GET "https://partner.shopeemobile.com/api/v2/ams/get_performance?partner_id=123456&timestamp=1700000000&access_token=c71a39d892ef65a43b1234567890abcd&shop_id=98765432&sign=calculated_sign_here&start_time=1698796800&end_time=1700000000" \
  -H "Content-Type: application/json"
```

