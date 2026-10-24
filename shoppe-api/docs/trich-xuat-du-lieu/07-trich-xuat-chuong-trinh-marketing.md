# 07. Hướng Dẫn Trích Xuất & Đo Lường Khuyến Mãi (Marketing & Campaigns)

Tài liệu này hướng dẫn cách trích xuất dữ liệu toàn bộ các chương trình khuyến mãi, mã giảm giá (Voucher), Combo ưu đãi (Bundle Deal) và Ưu đãi người theo dõi (Follow Prize) để đo lường hiệu quả chuyển đổi và tỷ suất hoàn vốn tiếp thị (Marketing ROI).

---

## 1. Bản Đồ Các Công Cụ Marketing Trên Shopee

Shopee cung cấp 5 công cụ khuyến mãi chính thuộc quyền kiểm soát của người bán:

```
[Marketing Tools Shopee]
    ├── 1. Shop Discount (Giảm giá sản phẩm trực tiếp, gắn nhãn -XX%)
    ├── 2. Shop Voucher (Mã giảm giá nhập mã hoặc lưu vào ví voucher)
    ├── 3. Bundle Deal (Combo mua nhiều giảm sâu: Mua 2 giảm 5%, Mua 3 giảm 10%)
    ├── 4. Add-on Deal (Mua kèm giá sốc / Mua sản phẩm A được mua phụ kiện B giá 0đ)
    └── 5. Follow Prize (Tặng voucher độc quyền khi bấm Theo Dõi Shop)
```

---

## 2. Quy Trình Thu Thập Dữ Liệu Khuyến Mãi

### 1. Thu thập danh sách Voucher Shop (`get_voucher_list`)
```bash
curl -X GET "https://partner.shopeemobile.com/api/v2/voucher/get_voucher_list?partner_id=123456&timestamp=1700000000&access_token=your_token&shop_id=98765432&sign=calculated_sign_here&status=ALL&page_no=1&page_size=50" \
  -H "Content-Type: application/json"
```
- Bóc tách các chỉ số:
  - `voucher_code`: Mã voucher (ví dụ: `SUPERDEAL50K`).
  - `discount_amount`: Mức giảm giá (tiền mặt hoặc %).
  - `min_basket_price`: Đơn tối thiểu.
  - `usage_quantity`: Tổng ngân sách số lượng voucher phát ra.
  - `current_usage`: Số lượng thực tế khách hàng đã sử dụng.
  - $\rightarrow$ **Tỷ lệ sử dụng (Redemption Rate)**: $\frac{\text{current\_usage}}{\text{usage\_quantity}} \times 100\%$.

### 2. Thu thập chương trình giảm giá sản phẩm (`get_discount_list`)
```bash
curl -X GET "https://partner.shopeemobile.com/api/v2/discount/get_discount_list?partner_id=123456&timestamp=1700000000&access_token=your_token&shop_id=98765432&sign=calculated_sign_here&discount_status=ONGOING&page_no=1&page_size=50" \
  -H "Content-Type: application/json"
```
- Với mỗi `discount_id`, gọi `get_discount` để lấy danh sách các `item_id` và `model_id` được giảm giá cùng mức giá sau chiết khấu.

### 3. Thu thập hiệu quả Follow Prize (`get_follow_prize_list`)
```bash
curl -X GET "https://partner.shopeemobile.com/api/v2/follow_prize/get_follow_prize_list?partner_id=123456&timestamp=1700000000&access_token=your_token&shop_id=98765432&sign=calculated_sign_here&status=all&page_no=1&page_size=50" \
  -H "Content-Type: application/json"
```
- Đo lường số người theo dõi mới thu hút được (`new_followers_count`) so với chi phí voucher đã bỏ ra (`current_usage * discount_amount`).

---

## 3. Kết Hợp Dữ Liệu Marketing Với Dữ Liệu Đơn Hàng & Tài Chính

Để có báo cáo P&L (Lãi/Lỗ) chính xác đến từng chiến dịch:
1. Trong dữ liệu chi tiết đơn hàng (`v2.order.get_order_detail`), trường `voucher_from_seller` và `seller_discount` cho biết chính xác đơn hàng đó đã tiêu tốn bao nhiêu tiền ngân sách khuyến mãi của shop.
2. Trong dữ liệu đối soát (`v2.payment.get_escrow_detail`), Shopee bóc tách rõ phần nào giảm do Shop tài trợ và phần nào giảm do Shopee tài trợ (`voucher_from_shopee`).
3. **Công thức tính Doanh Thu / Chi Phí Marketing (ROAS/ROI)**:
   $$\text{Voucher ROI} = \frac{\text{Tổng doanh thu các đơn hàng có áp mã}}{\text{Tổng số tiền giảm giá từ Voucher}}$$

