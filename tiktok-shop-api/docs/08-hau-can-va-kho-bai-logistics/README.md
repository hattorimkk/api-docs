# 08. Hậu Cần & Kho Bãi (Logistics API)

Phân hệ Logistics API chịu trách nhiệm quản lý hệ thống địa chỉ kho lấy hàng (Pickup Warehouse), kho nhận hàng hoàn (Return Warehouse) và danh sách các đơn vị vận chuyển bên thứ ba (3PL) được TikTok Shop chứng thực tại từng thị trường.

---

## 1. Danh Mục Các Endpoint Logistics

| Tên chức năng | Method | Endpoint Path | Mục đích |
| :--- | :--- | :--- | :--- |
| **Get Warehouse List** | `GET` | `/logistics/202309/warehouses` | Lấy danh sách kho lấy hàng và kho nhận hàng hoàn của Seller |
| **Get Global Seller Warehouses** | `GET` | `/logistics/202309/global_warehouses` | Lấy danh sách kho quốc tế dành cho người bán xuyên biên giới |
| **Get Shipping Providers** | `GET` | `/logistics/202309/shipping_providers` | Tra cứu danh sách 3PL (NinjaVan, J&T, SPX Express, GHN, GHTK...) |
| **Get Subscribed Delivery Options** | `GET` | `/logistics/202309/delivery_options` | Xem các gói vận chuyển shop đã kích hoạt (Tiết kiệm, Nhanh, Hỏa tốc) |

---

## 2. Chi Tiết Các Thao Tác Trọng Tâm

### 2.1. Lấy danh sách kho hàng Seller (Get Warehouse List)

- **Endpoint**: `/logistics/202309/warehouses`
- **Method**: `GET`
- **Mục đích**: Lấy `warehouse_id` để thiết lập địa chỉ lấy hàng khi tạo sản phẩm hoặc thiết lập địa chỉ nhận hàng hoàn khi người mua hoàn trả.

#### Mẫu cURL

```bash
curl -X GET \
  'https://open-api.tiktokglobalshop.com/logistics/202309/warehouses?app_key=YOUR_APP_KEY&timestamp=1792827493&shop_cipher=YOUR_SHOP_CIPHER&sign=CALCULATED_SIGN' \
  -H 'x-tts-access-token: YOUR_ACCESS_TOKEN' \
  -H 'Content-Type: application/json'
```

#### Phản hồi mẫu

```json
{
  "code": 0,
  "message": "success",
  "data": {
    "warehouses": [
      {
        "id": "7092819482910481",
        "name": "Tổng Kho Tân Bình - HCM",
        "type": "SALES_WAREHOUSE",
        "sub_type": "DOMESTIC_WAREHOUSE",
        "effect_status": "ENABLED",
        "is_default": true,
        "address": {
          "region": "VN",
          "state": "Hồ Chí Minh",
          "city": "Quận Tân Bình",
          "district": "Phường 2",
          "full_address": "Kho A, 45 Đường Bạch Đằng, Phường 2, Tân Bình, TP.HCM",
          "postal_code": "700000",
          "contact_person": "Trưởng Kho Nguyễn Văn B",
          "phone": "+84988776655"
        }
      },
      {
        "id": "7092819482910482",
        "name": "Kho Nhận Hàng Hoàn Trả",
        "type": "RETURN_WAREHOUSE",
        "sub_type": "DOMESTIC_WAREHOUSE",
        "effect_status": "ENABLED",
        "is_default": true
      }
    ]
  }
}
```

- `type`:
  - `SALES_WAREHOUSE`: Kho xuất hàng đi cho khách.
  - `RETURN_WAREHOUSE`: Kho tiếp nhận hàng hoàn/đổi trả.

---

### 2.2. Tra cứu Đơn vị vận chuyển (Get Shipping Providers)

- **Endpoint**: `/logistics/202309/shipping_providers`
- **Method**: `GET`

#### Mẫu cURL

```bash
curl -X GET \
  'https://open-api.tiktokglobalshop.com/logistics/202309/shipping_providers?app_key=YOUR_APP_KEY&timestamp=1792827493&shop_cipher=YOUR_SHOP_CIPHER&sign=CALCULATED_SIGN' \
  -H 'x-tts-access-token: YOUR_ACCESS_TOKEN' \
  -H 'Content-Type: application/json'
```

