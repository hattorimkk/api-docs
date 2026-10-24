"""
Script Tự Động Nạp Dữ Liệu Vào Cơ Sở Dữ Liệu SQL (Export & Ingest to SQL)
========================================================================
Hỗ trợ:
- Tự động tạo cấu trúc bảng chuẩn Data Warehouse (Star Schema)
- Đọc các file JSON dữ liệu đã trích xuất từ scripts (sync_orders, sync_products, sync_escrow)
- Nạp tự động vào Cơ sở dữ liệu SQLite cục bộ (hoặc cấu hình sang PostgreSQL/MySQL)
- Sẵn sàng để kết nối trực tiếp với Metabase, DBeaver hoặc PowerBI
"""

import os
import json
import sqlite3
from datetime import datetime
from typing import Optional


DB_FILE = os.getenv("SQLITE_DB_PATH", "./data/shopee_warehouse.db")


def init_database(db_path: str = DB_FILE):
    """Khởi tạo cấu trúc bảng SQLite theo mô hình chuẩn Star Schema."""
    os.makedirs(os.path.dirname(os.path.abspath(db_path)), exist_ok=True)
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # 1. Bảng dim_shops
    cur.execute("""
    CREATE TABLE IF NOT EXISTS dim_shops (
        shop_id INTEGER PRIMARY KEY,
        shop_name TEXT,
        region TEXT DEFAULT 'VN',
        status TEXT DEFAULT 'NORMAL',
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # 2. Bảng dim_products
    cur.execute("""
    CREATE TABLE IF NOT EXISTS dim_products (
        item_id INTEGER PRIMARY KEY,
        shop_id INTEGER,
        item_name TEXT,
        item_sku TEXT,
        category_id INTEGER,
        item_status TEXT,
        has_model INTEGER,
        weight_kg REAL,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # 3. Bảng dim_product_models
    cur.execute("""
    CREATE TABLE IF NOT EXISTS dim_product_models (
        model_id INTEGER PRIMARY KEY,
        item_id INTEGER,
        model_name TEXT,
        model_sku TEXT,
        original_price REAL,
        current_price REAL,
        normal_stock INTEGER,
        reserved_stock INTEGER,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (item_id) REFERENCES dim_products (item_id)
    );
    """)

    # 4. Bảng fact_orders
    cur.execute("""
    CREATE TABLE IF NOT EXISTS fact_orders (
        order_sn TEXT PRIMARY KEY,
        shop_id INTEGER,
        order_status TEXT,
        currency TEXT,
        total_amount REAL,
        actual_shipping_fee REAL,
        payment_method TEXT,
        recipient_city TEXT,
        recipient_district TEXT,
        create_time TIMESTAMP,
        update_time TIMESTAMP,
        ingested_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # 5. Bảng fact_order_items
    cur.execute("""
    CREATE TABLE IF NOT EXISTS fact_order_items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_sn TEXT,
        item_id INTEGER,
        model_id INTEGER,
        item_name TEXT,
        item_sku TEXT,
        model_name TEXT,
        model_sku TEXT,
        quantity_purchased INTEGER,
        discounted_price REAL,
        FOREIGN KEY (order_sn) REFERENCES fact_orders (order_sn)
    );
    """)

    # 6. Bảng fact_escrow_settlements
    cur.execute("""
    CREATE TABLE IF NOT EXISTS fact_escrow_settlements (
        order_sn TEXT PRIMARY KEY,
        buyer_total_amount REAL,
        escrow_amount REAL,
        commission_fee REAL,
        service_fee REAL,
        transaction_fee REAL,
        actual_shipping_fee REAL,
        reconciled_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (order_sn) REFERENCES fact_orders (order_sn)
    );
    """)

    conn.commit()
    conn.close()
    print(f"[DATABASE] Khởi tạo thành công cấu trúc bảng tại: {db_path}")


def ingest_products_from_json(json_path: str = "./data/shopee_products.json", db_path: str = DB_FILE, shop_id: int = 0):
    """Nạp danh mục sản phẩm và biến thể từ JSON vào SQL."""
    if not os.path.exists(json_path):
        print(f"[SKIP] Không tìm thấy file {json_path}")
        return

    with open(json_path, "r", encoding="utf-8") as f:
        products = json.load(f)

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    count_p = 0
    count_m = 0

    for p in products:
        item_id = p.get("item_id")
        cur.execute("""
        INSERT OR REPLACE INTO dim_products (item_id, shop_id, item_name, item_sku, category_id, item_status, has_model, weight_kg)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            item_id,
            shop_id,
            p.get("item_name"),
            p.get("item_sku", ""),
            p.get("category_id"),
            p.get("item_status"),
            1 if p.get("has_model") else 0,
            float(p.get("weight") or 0.0)
        ))
        count_p += 1

        for m in p.get("models", []):
            m_price = m.get("price_info", [{}])[0] if m.get("price_info") else {}
            m_stock = m.get("stock_info_v2", {}).get("summary_info", {})
            cur.execute("""
            INSERT OR REPLACE INTO dim_product_models (model_id, item_id, model_name, model_sku, original_price, current_price, normal_stock, reserved_stock)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                m.get("model_id"),
                item_id,
                m.get("model_name"),
                m.get("model_sku"),
                m_price.get("original_price", 0),
                m_price.get("current_price", 0),
                m_stock.get("total_available_stock", 0),
                m_stock.get("total_reserved_stock", 0)
            ))
            count_m += 1

    conn.commit()
    conn.close()
    print(f"[INGEST] Đã nạp {count_p} sản phẩm và {count_m} biến thể SKU vào SQL.")


def ingest_orders_from_json(json_path: str = "./data/shopee_orders.json", db_path: str = DB_FILE, shop_id: int = 0):
    """Nạp dữ liệu đơn hàng và chi tiết sản phẩm mua từ JSON vào SQL."""
    if not os.path.exists(json_path):
        print(f"[SKIP] Không tìm thấy file {json_path}")
        return

    with open(json_path, "r", encoding="utf-8") as f:
        orders = json.load(f)

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    count_orders = 0
    count_items = 0

    for o in orders:
        order_sn = o.get("order_sn")
        recipient = o.get("recipient_address", {})
        c_time = datetime.fromtimestamp(o.get("create_time", 0)).strftime("%Y-%m-%d %H:%M:%S") if o.get("create_time") else None
        u_time = datetime.fromtimestamp(o.get("update_time", 0)).strftime("%Y-%m-%d %H:%M:%S") if o.get("update_time") else None

        cur.execute("""
        INSERT OR REPLACE INTO fact_orders (order_sn, shop_id, order_status, currency, total_amount, actual_shipping_fee, payment_method, recipient_city, recipient_district, create_time, update_time)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            order_sn,
            shop_id,
            o.get("order_status"),
            o.get("currency", "VND"),
            o.get("total_amount", 0),
            o.get("actual_shipping_fee", 0),
            o.get("payment_method"),
            recipient.get("city"),
            recipient.get("district"),
            c_time,
            u_time
        ))
        count_orders += 1

        # Xóa các dòng item cũ của đơn để nạp lại
        cur.execute("DELETE FROM fact_order_items WHERE order_sn = ?", (order_sn,))

        for item in o.get("item_list", []):
            cur.execute("""
            INSERT INTO fact_order_items (order_sn, item_id, model_id, item_name, item_sku, model_name, model_sku, quantity_purchased, discounted_price)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                order_sn,
                item.get("item_id"),
                item.get("model_id"),
                item.get("item_name"),
                item.get("item_sku"),
                item.get("model_name"),
                item.get("model_sku"),
                item.get("model_quantity_purchased", 1),
                item.get("model_discounted_price", 0)
            ))
            count_items += 1

    conn.commit()
    conn.close()
    print(f"[INGEST] Đã nạp {count_orders} đơn hàng và {count_items} dòng chi tiết mua hàng vào SQL.")


def ingest_escrow_from_json(json_path: str = "./data/shopee_escrow.json", db_path: str = DB_FILE):
    """Nạp bảng kê quyết toán tài chính từ JSON vào SQL."""
    if not os.path.exists(json_path):
        print(f"[SKIP] Không tìm thấy file {json_path}")
        return

    with open(json_path, "r", encoding="utf-8") as f:
        escrows = json.load(f)

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    count_e = 0

    for e in escrows:
        order_sn = e.get("order_sn")
        income = e.get("order_income", {})
        buyer = e.get("buyer_payment_info", {})

        cur.execute("""
        INSERT OR REPLACE INTO fact_escrow_settlements (order_sn, buyer_total_amount, escrow_amount, commission_fee, service_fee, transaction_fee, actual_shipping_fee)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            order_sn,
            buyer.get("buyer_total_amount", 0),
            income.get("escrow_amount", 0),
            income.get("commission_fee", 0),
            income.get("service_fee", 0),
            income.get("transaction_fee", 0),
            income.get("actual_shipping_fee", 0)
        ))
        count_e += 1

    conn.commit()
    conn.close()
    print(f"[INGEST] Đã nạp {count_e} bản ghi quyết toán tài chính vào SQL.")


if __name__ == "__main__":
    init_database()
    ingest_products_from_json()
    ingest_orders_from_json()
    ingest_escrow_from_json()
    print("\n[THÀNH CÔNG] Cơ sở dữ liệu SQLite đã sẵn sàng cho phân tích BI!")

