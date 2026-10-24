# 03. Quản Lý & Khởi Tạo Chiến Dịch Quảng Cáo (Campaigns API)

Chiến dịch (Campaign) là tầng cao nhất trong hệ thống phân cấp quảng cáo của Meta. Đây là nơi bạn xác định **mục tiêu cốt lõi** của doanh nghiệp, hình thức mua và cấu hình ngân sách cấp chiến dịch (Advantage Campaign Budget / CBO).

Từ phiên bản **Graph API v21.0 và v22.0**, Meta đã chính thức khai tử các mục tiêu cũ và bắt buộc 100% sử dụng chuẩn **ODAX (Outcome-Driven Ad Experiences)**.

---

## 1. Chuẩn Mục Tiêu Mới ODAX (Bắt Buộc v21.0+)

Hệ thống ODAX tinh gọn lại chỉ còn 6 mục tiêu cốt lõi phản ánh chính xác kết quả kinh doanh:

| Mục tiêu ODAX (`objective`) | Tên tiếng Việt | Kết quả tối ưu tương ứng | Các mục tiêu cũ bị thay thế |
| :--- | :--- | :--- | :--- |
| `OUTCOME_SALES` | **Doanh số** | Bán hàng qua Website, Ứng dụng, Danh mục Catalog, Messenger/WhatsApp | `CONVERSIONS`, `PRODUCT_CATALOG_SALES`, `STORE_VISITS` |
| `OUTCOME_LEADS` | **Khách hàng tiềm năng** | Điền form (Instant Form), Tin nhắn tạo lead, Cuộc gọi điện thoại, Đăng ký web | `LEAD_GENERATION`, `MESSAGES` (cho mục đích lead) |
| `OUTCOME_ENGAGEMENT` | **Lượt tương tác** | Tin nhắn hội thoại, Lượt xem video, Tương tác bài viết, Lượt thích trang | `POST_ENGAGEMENT`, `PAGE_LIKES`, `EVENT_RESPONSES` |
| `OUTCOME_TRAFFIC` | **Lưu lượng truy cập** | Click vào liên kết website, Xem trang đích (Landing Page Views), Click gọi | `LINK_CLICKS` |
| `OUTCOME_AWARENESS` | **Độ nhận diện** | Tối đa hóa số người tiếp cận (Reach), Độ nhận biết thương hiệu, Lượt xem video | `BRAND_AWARENESS`, `REACH`, `VIDEO_VIEWS` |
| `OUTCOME_APP_PROMOTION`| **Quảng bá ứng dụng** | Lượt cài đặt ứng dụng (App Installs), Sự kiện hành động trong app | `APP_INSTALLS` |

---

## 2. Các Thuộc Tính Cốt Lõi Của Chiến Dịch

1. **`buying_type`**:
   - `AUCTION` (Mặc định): Đấu thầu linh hoạt theo thời gian thực (phù hợp với hầu hết chiến dịch).
   - `RESERVED`: Đặt trước tần suất và phạm vi tiếp cận (Reach & Frequency).
2. **`special_ad_categories`** (Bắt buộc):
   - Mảng khai báo danh mục quảng cáo đặc biệt. Nếu không thuộc ngành đặc biệt, **bắt buộc truyền mảng rỗng `[]` hoặc `["NONE"]`**.
   - Các giá trị ngành đặc biệt: `HOUSING` (Bất động sản), `EMPLOYMENT` (Tuyển dụng), `CREDIT` (Tín dụng/Vay vốn), `ISSUES_ELECTIONS_POLITICS` (Chính trị/Xã hội).
3. **Ngân sách cấp chiến dịch (Advantage Campaign Budget - CBO)**:
   - Nếu bạn muốn Meta tự động phân bổ ngân sách tối ưu giữa các nhóm quảng cáo: Đặt `daily_budget` hoặc `lifetime_budget` trực tiếp tại cấp Campaign.
   - Nếu muốn tự đặt ngân sách riêng cho từng nhóm quảng cáo (ABO): Để trống ngân sách ở cấp Campaign và cấu hình ở cấp Ad Set.

---

## 3. Danh Mục Các API Thao Tác Với Campaign

### 3.1. Tạo mới Chiến Dịch (POST)

Tạo một chiến dịch tăng doanh số (`OUTCOME_SALES`) sử dụng ngân sách ngày CBO là 1.000.000 VNĐ:

```bash
curl -i -X POST \
  "https://graph.facebook.com/v22.0/act_<AD_ACCOUNT_ID>/campaigns" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Tet 2026 - Chien Dich Doanh So Flash Sale",
    "objective": "OUTCOME_SALES",
    "status": "PAUSED",
    "buying_type": "AUCTION",
    "special_ad_categories": [],
    "daily_budget": "1000000",
    "access_token": "<YOUR_ACCESS_TOKEN>"
  }'
```

> **Lưu ý đơn vị tiền tệ:**
> - Nếu Ad Account dùng tiền tệ **VND**: Giá trị `"1000000"` tương đương `1.000.000 VNĐ`.
> - Nếu Ad Account dùng tiền tệ **USD**: Giá trị tính bằng **Cent**, do đó muốn đặt $50/ngày thì giá trị phải là `"5000"`.
> - Khuyến nghị khởi tạo chiến dịch ở trạng thái `"PAUSED"` để hoàn thiện Ad Set và Creative trước khi kích hoạt `ACTIVE`.

**Phản hồi thành công:**
```json
{
  "id": "120205847392810234"
}
```

---

### 3.2. Lấy Danh Sách Toàn Bộ Chiến Dịch (GET)

Truy vấn danh sách chiến dịch kèm trạng thái, ngân sách, mục tiêu và thời gian cập nhật:

```bash
curl -i -X GET \
  "https://graph.facebook.com/v22.0/act_<AD_ACCOUNT_ID>/campaigns?\
fields=id,name,objective,status,effective_status,daily_budget,lifetime_budget,start_time,stop_time,created_time\
&limit=50\
&access_token=<YOUR_ACCESS_TOKEN>"
```

**Phản hồi JSON:**
```json
{
  "data": [
    {
      "id": "120205847392810234",
      "name": "Tet 2026 - Chien Dich Doanh So Flash Sale",
      "objective": "OUTCOME_SALES",
      "status": "PAUSED",
      "effective_status": "CAMPAIGN_PAUSED",
      "daily_budget": "1000000",
      "created_time": "2026-10-24T08:30:00+0000"
    }
  ],
  "paging": {
    "cursors": {
      "before": "QVFIU...",
      "after": "QVFIU..."
    }
  }
}
```

> **Phân biệt `status` và `effective_status`:**
> - `status`: Trạng thái bạn cấu hình thủ công (`ACTIVE`, `PAUSED`, `ARCHIVED`).
> - `effective_status`: Trạng thái phân phối thực tế của hệ thống (`ACTIVE`, `PAUSED`, `CAMPAIGN_PAUSED`, `ADSET_PAUSED`, `DISAPPROVED`, `WITH_ISSUES`, `IN_PROCESS`). Hãy luôn dựa vào `effective_status` để hiển thị trên Dashboard giao diện của bạn.

---

### 3.3. Cập Nhật Chiến Dịch (POST `/{CAMPAIGN_ID}`)

Bật chiến dịch sang hoạt động (`ACTIVE`) và đổi tên hoặc tăng ngân sách:

```bash
curl -i -X POST \
  "https://graph.facebook.com/v22.0/120205847392810234" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Tet 2026 - Chien Dich Doanh So [SCALE UP]",
    "status": "ACTIVE",
    "daily_budget": "2000000",
    "access_token": "<YOUR_ACCESS_TOKEN>"
  }'
```

**Phản hồi:**
```json
{
  "success": true
}
```

---

### 3.4. Xóa Chiến Dịch (DELETE `/{CAMPAIGN_ID}`)

> ⚠️ **Cảnh báo:** Xóa chiến dịch sẽ xóa vĩnh viễn cấu hình khỏi danh sách quản lý. Nếu muốn giữ dữ liệu lịch sử để xem báo cáo, bạn nên đổi trạng thái thành `ARCHIVED` thay vì `DELETE`.

```bash
curl -i -X DELETE \
  "https://graph.facebook.com/v22.0/120205847392810234?access_token=<YOUR_ACCESS_TOKEN>"
```

**Phản hồi:**
```json
{
  "success": true
}
```

---

## 4. Lọc Nâng Cao Theo Bộ Lọc Tham Số (`filtering`)

Bạn có thể lọc danh sách chiến dịch bằng cách truyền tham số `filtering` dạng mảng JSON:

```bash
curl -i -G \
  "https://graph.facebook.com/v22.0/act_<AD_ACCOUNT_ID>/campaigns" \
  --data-urlencode 'fields=id,name,status,effective_status' \
  --data-urlencode 'filtering=[{"field":"effective_status","operator":"IN","value":["ACTIVE"]}]' \
  --data-urlencode 'access_token=<YOUR_ACCESS_TOKEN>'
```

Các toán tử lọc thông dụng: `EQUAL`, `NOT_EQUAL`, `GREATER_THAN`, `LESS_THAN`, `IN`, `NOT_IN`, `CONTAIN`.

