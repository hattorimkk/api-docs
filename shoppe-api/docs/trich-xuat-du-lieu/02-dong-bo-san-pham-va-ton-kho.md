# 02. Hướng Dẫn Trích Xuất Sản Phẩm, Biến Thể & Tồn Kho (Product & Inventory)

Tài liệu này hướng dẫn cách trích xuất toàn bộ danh mục sản phẩm của gian hàng, bao gồm các thuộc tính sản phẩm gốc, phân loại biến thể hàng (màu sắc, kích cỡ), đơn giá và số lượng tồn kho khả dụng.

---

## 1. Cấu Trúc Sản Phẩm Trên Shopee (Product Hierarchy)

Trên sàn Shopee, sản phẩm được chia làm hai dạng:
1. **Sản phẩm đơn (Single Item)**: Sản phẩm chỉ có 1 loại duy nhất (không có biến thể màu sắc hay size). Giá và tồn kho gắn trực tiếp vào `item_id`.
2. **Sản phẩm có biến thể (Tier-variation Item)**: Sản phẩm có nhiều lựa chọn (ví dụ: Size S/M/L, Màu Đen/Trắng). Giá, SKU và tồn kho được quản lý chi tiết ở từng biến thể con định danh bằng **`model_id`**.

```
[Sản Phẩm Gốc: item_id] (has_model = True)
    ├── Tên sản phẩm, Ngành hàng (category_id), Cân nặng, Kích thước, Hình ảnh
    │
    ├── [Biến thể 1: model_id_101] -> Màu Đỏ, Size M -> model_sku, giá, tồn kho
    ├── [Biến thể 2: model_id_102] -> Màu Đỏ, Size L -> model_sku, giá, tồn kho
    └── [Biến thể 3: model_id_103] -> Màu Đen, Size M -> model_sku, giá, tồn kho
```

---

## 2. Quy Trình Trích Xuất Dữ Liệu 3 Bước

Để lấy đầy đủ thông tin từ danh mục đến biến thể, bạn thực hiện theo quy trình sau:

### Bước 1: Lấy danh sách ID sản phẩm (`get_item_list`)
- **API**: `GET /api/v2/product/get_item_list`
- **Tham số**:
  - `offset`: Vị trí bắt đầu (bắt đầu từ `0`).
  - `page_size`: Số lượng sản phẩm mỗi trang (tối đa `100`).
  - `item_status`: Trạng thái sản phẩm cần lấy:
    - `NORMAL`: Sản phẩm đang hoạt động bình thường trên sàn.
    - `BANNED`: Sản phẩm bị khóa vi phạm.
    - `UNLIST`: Sản phẩm đang ẩn/tạm ngừng bán.

### Lệnh cURL quét danh sách ID sản phẩm:
```bash
curl -X GET "https://partner.shopeemobile.com/api/v2/product/get_item_list?partner_id=123456&timestamp=1700000000&access_token=your_token&shop_id=98765432&sign=calculated_sign_here&offset=0&page_size=100&item_status=NORMAL" \
  -H "Content-Type: application/json"
```

Phản hồi trả về danh sách các `item_id` kèm con trỏ `has_next_page` và `next_offset`.

---

### Bước 2: Lấy thông tin cơ bản của sản phẩm (`get_item_base_info`)
- **API**: `GET /api/v2/product/get_item_base_info`
- **Lệnh cURL lấy thông tin theo mẻ 50 sản phẩm**:
```bash
curl -X GET "https://partner.shopeemobile.com/api/v2/product/get_item_base_info?partner_id=123456&timestamp=1700000000&access_token=your_token&shop_id=98765432&sign=calculated_sign_here&item_id_list=10928374,10928375" \
  -H "Content-Type: application/json"
```

#### Dữ liệu trả về:
- `item_name`: Tên sản phẩm.
- `description`: Mô tả chi tiết.
- `category_id`: Mã ngành hàng Shopee.
- `item_sku`: Mã SKU của sản phẩm gốc.
- `weight`: Cân nặng sản phẩm (tính theo kg).
- `dimension`: Chiều dài, rộng, cao (để tính phí vận chuyển thể tích).
- `image`: Danh sách đường dẫn hình ảnh sản phẩm.
- `has_model`: Giá trị `true` nếu sản phẩm có biến thể, `false` nếu là sản phẩm đơn.

---

### Bước 3: Lấy danh sách biến thể & tồn kho (`get_model_list`)
Nếu sản phẩm có `has_model == true`, bạn cần gọi API này để bóc tách SKU con:
- **API**: `GET /api/v2/product/get_model_list`
- **Lệnh cURL lấy biến thể SKU & tồn kho**:
```bash
curl -X GET "https://partner.shopeemobile.com/api/v2/product/get_model_list?partner_id=123456&timestamp=1700000000&access_token=your_token&shop_id=98765432&sign=calculated_sign_here&item_id=10928374" \
  -H "Content-Type: application/json"
```

#### Dữ liệu chi tiết của từng biến thể (`model`):
- `model_id`: ID duy nhất của biến thể.
- `model_name`: Tên phân loại (ví dụ: `Đen, Size XL`).
- `model_sku`: Mã SKU quản lý kho riêng của biến thể đó.
- `price_info`:
  - `original_price`: Giá niêm yết ban đầu.
  - `current_price`: Giá bán hiện tại sau khi trừ khuyến mãi.
- `stock_info_v2`:
  - `total_available_stock`: Số lượng tồn kho khả dụng thực tế để bán (`normal_stock`).
  - `total_reserved_stock`: Số lượng tồn kho đang bị tạm giữ cho các chiến dịch Flash Sale hoặc giỏ hàng đang chờ thanh toán.

---

## 3. Khuyến Nghị Thiết Kế Bảng Cơ Sở Dữ Liệu (Database Schema)

Để đồng bộ dữ liệu vào PostgreSQL / MySQL cho hệ thống ERP hoặc Data Warehouse, mô hình chuẩn gồm 2 bảng:

```sql
-- Bảng 1: Sản phẩm gốc (Parent Items)
CREATE TABLE shopee_items (
    item_id BIGINT PRIMARY KEY,
    shop_id BIGINT NOT NULL,
    item_name VARCHAR(500) NOT NULL,
    item_sku VARCHAR(100),
    category_id BIGINT,
    item_status VARCHAR(50),
    has_model BOOLEAN DEFAULT FALSE,
    weight_kg NUMERIC(8, 3),
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Bảng 2: Biến thể SKU con & Tồn kho (Item Variations / Models)
CREATE TABLE shopee_item_models (
    model_id BIGINT PRIMARY KEY,
    item_id BIGINT REFERENCES shopee_items(item_id),
    model_name VARCHAR(255),
    model_sku VARCHAR(100),
    original_price NUMERIC(15, 2),
    current_price NUMERIC(15, 2),
    available_stock INT DEFAULT 0,
    reserved_stock INT DEFAULT 0,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

