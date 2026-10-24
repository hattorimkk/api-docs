# Hướng dẫn TikTok Store

Tài liệu này hướng dẫn tổng quan về việc quản lý và tích hợp TikTok Store (Cửa hàng TikTok) thông qua Marketing API. Bạn sẽ tìm hiểu các khái niệm và vai trò cốt lõi (nhà bán hàng, nhà phát triển, tài khoản doanh nghiệp, Business Center), quy trình liên kết TikTok Shop với tài khoản quảng cáo, cùng danh mục các API hỗ trợ truy xuất danh sách cửa hàng và sản phẩm để phục vụ các chiến dịch quảng cáo mua sắm.

## TikTok Store (`TikTok Store`)
<a id="doc-1739581901879298"></a>
<!-- doc_id: 1739581901879298 -->

> Đường dẫn: Marketing API > TikTok Store

TikTok Store API cho phép bạn truy xuất các cửa hàng bên thứ nhất (TikTok Shops) thuộc một tài khoản quảng cáo và danh sách sản phẩm trong các cửa hàng TikTok Shop đó.

- Để tìm hiểu về TikTok Store cùng các vai trò và khái niệm phổ biến, xem [Tổng quan (Overview)](tiktok-store.md#doc-1763572749953025).
- Để tìm hiểu quy trình làm việc chung, xem [Hướng dẫn quy trình (Guides)](tiktok-store.md#doc-1739581925704769).
- Để tra cứu các API khả dụng nhằm quản lý TikTok Store, xem [Tham chiếu API (API reference)](tiktok-store.md#doc-1740641357077505).

## Tổng quan (`Overview`)
<a id="doc-1763572749953025"></a>
<!-- doc_id: 1763572749953025 -->

> Đường dẫn: Marketing API > TikTok Store > Overview

TikTok Store là một thực thể hoặc đối tượng cho phép người bán quản lý và kinh doanh sản phẩm trên TikTok. Các nhà sáng tạo nội dung TikTok có thể liên kết tài khoản TikTok của họ với cửa hàng để bắt đầu bán sản phẩm trực tiếp từ tài khoản của mình.

Dưới đây là một số vai trò và khái niệm quan trọng liên quan đến TikTok Store:
- **Người bán (Merchant):** Cá nhân hoặc doanh nghiệp muốn bán sản phẩm trên nền tảng TikTok.
- **Nhà phát triển (Developer):** Cá nhân hoặc đối tác kỹ thuật chịu trách nhiệm tích hợp hoặc sử dụng TikTok Marketing API.
- **Tài khoản TikTok doanh nghiệp (TikTok business account):** Loại tài khoản TikTok cung cấp khả năng cho các doanh nghiệp trực tiếp quảng bá sản phẩm thông qua tài khoản của họ và nắm bắt thông tin chuyên sâu về tệp đối tượng.
- **Tài khoản TikTok For Business (TikTok For Business account):** Tài khoản được thiết kế dành cho nhà quảng cáo hoặc agency nhằm quản lý các chiến dịch quảng cáo và đo lường hiệu suất quảng cáo.
- **Ứng dụng nhà phát triển TikTok API for Business (TikTok API for Business developer application):** Thực thể mang các quyền hạn mà người bán hoặc nhà quảng cáo cấp cho nhà phát triển, từ đó nhà phát triển có thể thay mặt họ quản lý tài khoản TikTok For Business.

## Hướng dẫn quy trình (`Guides`)
<a id="doc-1739581925704769"></a>
<!-- doc_id: 1739581925704769 -->

> Đường dẫn: Marketing API > TikTok Store > Guides

Hướng dẫn này dẫn dắt bạn qua quy trình làm việc chung để quản lý TikTok Store thông qua API.

### Điều kiện tiên quyết (Prerequisites)

* Người bán có tài khoản TikTok doanh nghiệp (TikTok business account). Họ có thể nâng cấp tài khoản cá nhân lên tài khoản doanh nghiệp theo hướng dẫn tại [trang này](https://www.tiktok.com/business/en-US/apps/business-account).
* Người bán có tài khoản TikTok For Business.
* Nhà phát triển đã đăng ký làm nhà phát triển trên cổng TikTok Marketing API và tạo ứng dụng nhà phát triển. Xem chi tiết tại [Đăng ký làm nhà phát triển](../04-get-started/bat-dau.md#doc-1738855176671234) và [Tạo ứng dụng nhà phát triển](../04-get-started/bat-dau.md#doc-1738855242728450).

### Quy trình thực hiện (Workflow)

1. Tạo một Business Center. Thao tác này cần được thực hiện trên TikTok Ads Manager. Để xem hướng dẫn, xem [Cách tạo TikTok Business Center](https://ads.tiktok.com/help/article?aid=12789).
2. Tạo một TikTok Shop trong Business Center hoặc thêm một TikTok Shop hiện có vào Business Center:
   - Nếu bạn chưa có TikTok Shop, bạn có thể tạo mới trong Business Center. Xem chi tiết các bước tại [Tạo TikTok Shop từ Business Center - Tình huống B: Tạo TikTok Shop của tôi](https://ads.tiktok.com/help/article/add-tiktok-shop-from-business-center?lang=en#anchor-9).
   - Nếu bạn đã tạo TikTok Shop trong TikTok Seller Center theo các bước tại [Thiết lập TikTok Shop bằng TikTok Seller Center](https://ads.tiktok.com/help/article/set-up-tiktok-shop-using-tiktok-seller-center?lang=en), bạn có thể thêm TikTok Shop hiện có vào Business Center. Xem chi tiết các bước tại [Tạo TikTok Shop từ Business Center - Tình huống A: Thêm TikTok Shop của tôi](https://ads.tiktok.com/help/article/add-tiktok-shop-from-business-center?lang=en#anchor-4).

## Tham chiếu API (`API reference`)
<a id="doc-1740641357077505"></a>
<!-- doc_id: 1740641357077505 -->

> Đường dẫn: Marketing API > TikTok Store > API reference

Nhóm này bao gồm các endpoint API sau:

* [Lấy danh sách các cửa hàng khả dụng thuộc tài khoản quảng cáo (Get available stores under an ad account)](../12-api-reference/69-tiktok-store.md#doc-1752267762718722)
* [Lấy danh sách sản phẩm trong một cửa hàng (Get products within a store)](../12-api-reference/69-tiktok-store.md#doc-1793482248880130)
