# 08. Thiết Kế Data Pipeline & Kho Dữ Liệu (Data Warehouse & Star Schema)

Tài liệu này cung cấp thiết kế kiến trúc kỹ thuật toàn diện cho việc xây dựng đường ống dữ liệu (Data Pipeline), hồ dữ liệu (Data Lake) và mô hình hóa kho dữ liệu (Data Warehouse / Star Schema) chuyên dụng cho dữ liệu trích xuất từ Shopee Open Platform.

---

## 1. Kiến Trúc Tổng Thể (End-to-End Data Pipeline Architecture)

```
[Shopee Open Platform]
  ├── REST APIs (Order, Product, Escrow, Logistics)
  └── Push Mechanism (Webhooks: Order Status, Tracking, Stock)
             |
             v
[Lớp Thu Thập Dữ Liệu (Ingestion Layer)]
  ├── Python Extraction Scripts / Celery Workers / Airflow DAGs
  └── Fast Webhook Receiver (FastAPI / Redis Queue)
             |
             v
[Lớp Dữ Liệu Thô (Raw Staging Layer / Bronze)]
  ├── S3 / Google Cloud Storage / Local JSON files
  └── Bảng staging lưu trữ nguyên bản JSON payload (PostgreSQL JSONB)
             |
             v (Dọn dẹp, chuẩn hóa kiểu dữ liệu, khử trùng lặp Idempotent)
[Lớp Mô Hình Hóa Dữ Liệu (Data Warehouse Layer / Silver & Gold)]
  ├── Bảng Thực Thể (Dimension Tables): dim_shops, dim_products, dim_models, dim_carriers
  └── Bảng Đo Lường (Fact Tables): fact_orders, fact_order_items, fact_escrow
             |
             v
[Lớp Phân Tích & Báo Cáo (BI & Analytics Layer)]
  └── Metabase, PowerBI, Tableau, Grafana Dashboard
```

---

## 2. Mô Hình Dữ Liệu Chuẩn Hình Sao (Star Schema Dimensional Model)

```
                    +--------------------+
                    |     dim_shops      |
                    +--------------------+
                    | * shop_id (PK)     |
                    |   shop_name        |
                    |   region (VN, TH)  |
                    +--------------------+
                              | 1
                              |
                              | N
                    +--------------------+ 1      N +-------------------------+
                    |    fact_orders     |--------->|    fact_order_items     |
                    +--------------------+          +-------------------------+
                    | * order_sn (PK)    |          | * id (PK)               |
                    |   shop_id (FK)     |          |   order_sn (FK)         |
                    |   order_status     |          |   item_id (FK)          |
                    |   total_amount     |          |   model_id (FK)         |
                    |   shipping_fee     |          |   quantity_purchased    |
                    |   create_time      |          |   discounted_price      |
                    |   city, district   |          +-------------------------+
                    +--------------------+                        | N
                              | 1                                 |
                              |                                   | 1
                              v N                                 v
                    +--------------------+          +-------------------------+
                    |    fact_escrow     |          |       dim_products      |
                    +--------------------+          +-------------------------+
                    | * order_sn (PK/FK) |          | * item_id (PK)          |
                    |   escrow_amount    |          |   item_name             |
                    |   commission_fee   |          |   category_id           |
                    |   service_fee      |          +-------------------------+
                    |   transaction_fee  |                        | 1
                    |   release_time     |                        | N
                    +--------------------+          +-------------------------+
                                                    |    dim_product_models   |
                                                    +-------------------------+
                                                    | * model_id (PK)         |
                                                    |   item_id (FK)          |
                                                    |   model_name            |
                                                    |   model_sku             |
                                                    +-------------------------+
```

---

## 3. Câu Lệnh Tạo Bảng SQL Chuẩn (DDL for PostgreSQL / MySQL)

Dưới đây là mã SQL sẵn sàng thực thi để khởi tạo hệ thống cơ sở dữ liệu hoàn chỉnh:

```sql
-- 1. BẢNG CHIỀU GIAN HÀNG (DIM SHOPS)
CREATE TABLE dim_shops (
    shop_id BIGINT PRIMARY KEY,
    shop_name VARCHAR(255) NOT NULL,
    region VARCHAR(10) NOT NULL DEFAULT 'VN',
    status VARCHAR(50) DEFAULT 'NORMAL',
    is_sip BOOLEAN DEFAULT FALSE,
    auth_time TIMESTAMP,
    expire_time TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. BẢNG CHIỀU SẢN PHẨM GỐC (DIM PRODUCTS)
CREATE TABLE dim_products (
    item_id BIGINT PRIMARY KEY,
    shop_id BIGINT NOT NULL REFERENCES dim_shops(shop_id),
    item_name VARCHAR(500) NOT NULL,
    item_sku VARCHAR(100),
    category_id BIGINT,
    item_status VARCHAR(50) DEFAULT 'NORMAL',
    has_model BOOLEAN DEFAULT FALSE,
    weight_kg NUMERIC(10, 3),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 3. BẢNG CHIỀU BIẾN THỂ SKU (DIM PRODUCT MODELS)
CREATE TABLE dim_product_models (
    model_id BIGINT PRIMARY KEY,
    item_id BIGINT NOT NULL REFERENCES dim_products(item_id),
    model_name VARCHAR(255),
    model_sku VARCHAR(100),
    original_price NUMERIC(15, 2) DEFAULT 0,
    current_price NUMERIC(15, 2) DEFAULT 0,
    normal_stock INT DEFAULT 0,
    reserved_stock INT DEFAULT 0,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 4. BẢNG SỰ KIỆN ĐƠN HÀNG (FACT ORDERS)
CREATE TABLE fact_orders (
    order_sn VARCHAR(50) PRIMARY KEY,
    shop_id BIGINT NOT NULL REFERENCES dim_shops(shop_id),
    order_status VARCHAR(50) NOT NULL,
    currency VARCHAR(10) DEFAULT 'VND',
    total_amount NUMERIC(15, 2) NOT NULL DEFAULT 0,
    actual_shipping_fee NUMERIC(15, 2) DEFAULT 0,
    estimated_shipping_fee NUMERIC(15, 2) DEFAULT 0,
    payment_method VARCHAR(100),
    recipient_city VARCHAR(150),
    recipient_district VARCHAR(150),
    create_time TIMESTAMP NOT NULL,
    update_time TIMESTAMP,
    pay_time TIMESTAMP,
    ingested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tạo Index tăng tốc truy vấn theo thời gian và trạng thái
CREATE INDEX idx_orders_shop_status ON fact_orders (shop_id, order_status);
CREATE INDEX idx_orders_create_time ON fact_orders (create_time);

-- 5. BẢNG SỰ KIỆN DÒNG CHI TIẾT SẢN PHẨM MUA (FACT ORDER ITEMS)
CREATE TABLE fact_order_items (
    id BIGSERIAL PRIMARY KEY,
    order_sn VARCHAR(50) NOT NULL REFERENCES fact_orders(order_sn) ON DELETE CASCADE,
    item_id BIGINT NOT NULL,
    model_id BIGINT,
    item_name VARCHAR(500),
    item_sku VARCHAR(100),
    model_name VARCHAR(255),
    model_sku VARCHAR(100),
    quantity_purchased INT NOT NULL DEFAULT 1,
    original_price NUMERIC(15, 2) DEFAULT 0,
    discounted_price NUMERIC(15, 2) DEFAULT 0,
    ingested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_order_items_sn ON fact_order_items (order_sn);
CREATE INDEX idx_order_items_sku ON fact_order_items (model_sku);

-- 6. BẢNG SỰ KIỆN ĐỐI SOÁT TÀI CHÍNH (FACT ESCROW SETTLEMENTS)
CREATE TABLE fact_escrow_settlements (
    order_sn VARCHAR(50) PRIMARY KEY REFERENCES fact_orders(order_sn),
    buyer_user_name VARCHAR(150),
    buyer_total_amount NUMERIC(15, 2) DEFAULT 0,
    escrow_amount NUMERIC(15, 2) NOT NULL DEFAULT 0, -- Doanh thu thực nhận
    cost_of_goods_sold NUMERIC(15, 2) DEFAULT 0,
    seller_discount NUMERIC(15, 2) DEFAULT 0,
    voucher_from_seller NUMERIC(15, 2) DEFAULT 0,
    voucher_from_shopee NUMERIC(15, 2) DEFAULT 0,
    commission_fee NUMERIC(15, 2) DEFAULT 0,         -- Phí hoa hồng sàn
    service_fee NUMERIC(15, 2) DEFAULT 0,            -- Phí dịch vụ (Freeship/Hoàn xu)
    transaction_fee NUMERIC(15, 2) DEFAULT 0,        -- Phí thanh toán
    actual_shipping_fee NUMERIC(15, 2) DEFAULT 0,
    shopee_shipping_rebate NUMERIC(15, 2) DEFAULT 0,
    release_time TIMESTAMP,
    reconciled_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_escrow_release_time ON fact_escrow_settlements (release_time);
```

---

## 4. Các Câu Lệnh SQL Báo Cáo Kinh Doanh Điển Hình

### Báo cáo Doanh thu & Phí sàn thực tế theo tháng:
```sql
SELECT 
    DATE_TRUNC('month', release_time) AS month,
    COUNT(order_sn) AS total_settled_orders,
    SUM(buyer_total_amount) AS total_gmv,
    SUM(escrow_amount) AS net_revenue_received,
    SUM(commission_fee) AS total_commission_fee,
    SUM(service_fee) AS total_service_fee,
    SUM(transaction_fee) AS total_transaction_fee,
    ROUND(SUM(commission_fee + service_fee + transaction_fee) * 100.0 / NULLIF(SUM(buyer_total_amount), 0), 2) AS total_take_rate_pct
FROM fact_escrow_settlements
GROUP BY 1
ORDER BY 1 DESC;
```

### Báo cáo Top 10 SKU bán chạy nhất:
```sql
SELECT 
    COALESCE(model_sku, item_sku, 'NO-SKU') AS sku_code,
    item_name,
    model_name,
    SUM(quantity_purchased) AS total_units_sold,
    SUM(quantity_purchased * discounted_price) AS total_sales_revenue
FROM fact_order_items
GROUP BY 1, 2, 3
ORDER BY total_sales_revenue DESC
LIMIT 10;
```

