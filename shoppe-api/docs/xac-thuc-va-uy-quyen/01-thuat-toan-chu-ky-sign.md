# 01. Thuật Toán Tạo Chữ Ký Số (HMAC-SHA256 Signature)

Chữ ký số (`sign`) là cơ chế bảo mật cốt lõi nhất của Shopee Open Platform. Mọi request gửi đến Shopee nếu không có chữ ký hợp lệ đều bị từ chối ngay lập tức với lỗi `Wrong sign`.

---

## 1. Nguyên Lý Hoạt Động

Shopee sử dụng thuật toán **HMAC-SHA256 (Hash-based Message Authentication Code sử dụng hàm băm SHA-256)**:
- **Khóa bí mật (Secret Key)**: Là `partner_key` của ứng dụng.
- **Dữ liệu đầu vào (Base String)**: Là chuỗi ghép nối tuần tự không khoảng trắng từ các tham số cơ bản và đường dẫn API.
- **Kết quả đầu ra**: Chuỗi mã hóa Hexadecimal (dạng viết thường) dài 64 ký tự.

---

## 2. Quy Tắc Ghép Chuỗi Cơ Sở (Base String Construction)

Thứ tự ghép chuỗi tuyệt đối không được thay đổi. Có 3 trường hợp cơ bản:

### Trường hợp 1: Public API (Không cần token, không cần shop_id)
Dùng cho API đổi code lấy token, refresh token hoặc link ủy quyền:
$$\text{Base String} = \text{partner\_id} + \text{api\_path} + \text{timestamp}$$

**Ví dụ:**
- `partner_id` = `123456`
- `api_path` = `/api/v2/auth/token/get`
- `timestamp` = `1700000000`
- $\rightarrow$ `Base String` = `123456/api/v2/auth/token/get1700000000`

---

### Trường hợp 2: Shop API (API thao tác với Shop)
Dùng cho 95% các API quản lý đơn hàng, sản phẩm, tồn kho, doanh thu:
$$\text{Base String} = \text{partner\_id} + \text{api\_path} + \text{timestamp} + \text{access\_token} + \text{shop\_id}$$

**Ví dụ:**
- `partner_id` = `123456`
- `api_path` = `/api/v2/order/get_order_list`
- `timestamp` = `1700000000`
- `access_token` = `415a6b7c8d9e...`
- `shop_id` = `98765432`
- $\rightarrow$ `Base String` = `123456/api/v2/order/get_order_list1700000000415a6b7c8d9e...98765432`

---

### Trường hợp 3: Merchant API (API thao tác tài khoản tổng CNSC)
Dùng cho các tài khoản bán hàng toàn cầu quản lý nhiều shop xuyên biên giới:
$$\text{Base String} = \text{partner\_id} + \text{api\_path} + \text{timestamp} + \text{access\_token} + \text{merchant\_id}$$

---

## 3. Lệnh Tạo Chữ Ký Chuẩn Trực Tiếp Trên Terminal (Bash / OpenSSL & cURL)

Bạn có thể tính chữ ký trực tiếp trên dòng lệnh Terminal bằng lệnh `openssl` tích hợp sẵn trên macOS/Linux:

```bash
# 1. Khai báo các biến thông số
PARTNER_ID="123456"
PARTNER_KEY="your_partner_key_here"
API_PATH="/api/v2/shop/get_shop_info"
TIMESTAMP=$(date +%s)
ACCESS_TOKEN="your_access_token_here"
SHOP_ID="98765432"

# 2. Ghép chuỗi Base String theo đúng chuẩn Shopee v2
BASE_STRING="${PARTNER_ID}${API_PATH}${TIMESTAMP}${ACCESS_TOKEN}${SHOP_ID}"

# 3. Tạo chữ ký số HMAC-SHA256 bằng OpenSSL
SIGN=$(printf "%s" "$BASE_STRING" | openssl dgst -sha256 -hmac "$PARTNER_KEY" | awk '{print $2}')

echo "Base string: $BASE_STRING"
echo "Chữ ký sign: $SIGN"

# 4. Gửi request trực tiếp bằng cURL
curl -X GET "https://partner.shopeemobile.com${API_PATH}?partner_id=${PARTNER_ID}&timestamp=${TIMESTAMP}&access_token=${ACCESS_TOKEN}&shop_id=${SHOP_ID}&sign=${SIGN}" \
  -H "Content-Type: application/json"
```

---

## 4. Code Mẫu Tạo Chữ Ký (Python & Node.js)

### Python 3
```python
import hmac
import hashlib
import time

def generate_shopee_sign(partner_id: int, partner_key: str, api_path: str, timestamp: int, access_token: str = None, shop_id: int = None) -> str:
    # 1. Ghép chuỗi base string
    base_string = f"{partner_id}{api_path}{timestamp}"
    if access_token:
        base_string += f"{access_token}"
        if shop_id:
            base_string += f"{shop_id}"
            
    # 2. Băm HMAC-SHA256
    sign = hmac.new(
        partner_key.encode("utf-8"),
        base_string.encode("utf-8"),
        hashlib.sha256
    ).hexdigest()
    
    return sign

# Sử dụng thực tế:
p_id = 123456
p_key = "my_secret_partner_key"
path = "/api/v2/order/get_order_list"
ts = int(time.time())
token = "my_current_access_token"
s_id = 98765432

signature = generate_shopee_sign(p_id, p_key, path, ts, token, s_id)
print("Chữ ký sign:", signature)
```

### Node.js / JavaScript
```javascript
const crypto = require('crypto');

function generateShopeeSign(partnerId, partnerKey, apiPath, timestamp, accessToken = null, shopId = null) {
    let baseString = `${partnerId}${apiPath}${timestamp}`;
    if (accessToken) {
        baseString += `${accessToken}`;
        if (shopId) {
            baseString += `${shopId}`;
        }
    }
    
    return crypto
        .createHmac('sha256', partnerKey)
        .update(baseString)
        .digest('hex');
}
```

---

## 4. Những Sai Lầm Phổ Biến Gây Lỗi "Wrong sign"

1. **Lệch giờ hệ thống (Clock Skew)**:
   - Shopee chỉ chấp nhận request có `timestamp` sai lệch **không quá 5 phút (300 giây)** so với đồng hồ nguyên tử của máy chủ Shopee.
   - Giải pháp: Cài đặt phần mềm đồng bộ thời gian (như `chrony` hoặc `ntpdate`) trên server Linux của bạn:
     ```bash
     sudo apt-get install chrony
     sudo systemctl enable --now chrony
     ```
2. **Sai đường dẫn `api_path`**:
   - `api_path` phải bắt đầu bằng `/api/v2/...`.
   - Tuyệt đối không gắn domain (`https://partner.shopeemobile.com`) vào `api_path`.
   - Tuyệt đối không gắn Query string (như `?order_sn=...`) vào `api_path`.
3. **Thêm khoảng trắng hoặc ký tự phân tách**:
   - Không được dùng dấu gạch nối `-`, gạch dưới `_`, dấu hai chấm `:` hoặc khoảng trắng giữa các thành phần khi ghép chuỗi.
4. **Kiểu dữ liệu số và chuỗi**:
   - Đảm bảo `partner_id` và `shop_id` khi chuyển sang chuỗi không bị format dạng khoa học (ví dụ: `1.23456e+05`).

