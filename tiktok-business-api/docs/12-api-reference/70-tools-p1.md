# Công cụ tra cứu (Tools) — phần 1/3

> Phân hệ: apiref:Tools.
> Tài liệu biên dịch kỹ thuật chi tiết theo chuẩn TikTok Business API v1.3.

---

## Mục lục điều hướng
- [1. Công cụ tra cứu (Tools) (#doc-1736271001971713)](#doc-1736271001971713)
- [2. Tìm kiếm thẻ nhắm mục tiêu vị trí (#doc-1761236883355649)](#doc-1761236883355649)
- [3. Lấy thông tin chi tiết thẻ nhắm mục tiêu vị trí theo ID (Obtain details about location targeting tags by ID) (#doc-1761237001980929)](#doc-1761237001980929)
- [4. Lấy danh sách vị trí khả dụng theo cài đặt (Get available locations by different settings) (#doc-1737189539571713)](#doc-1737189539571713)
- [5. Lấy danh sách vị trí khả dụng theo ID tài khoản quảng cáo TikTok (#doc-1773644763581441)](#doc-1773644763581441)
- [6. Lấy danh sách ngôn ngữ (Get languages) (#doc-1737188554152962)](#doc-1737188554152962)
- [7. Tìm kiếm hoặc liệt kê danh mục và hashtag nhắm mục tiêu sở thích, hành vi (#doc-1796638342793218)](#doc-1796638342793218)
- [8. Lấy danh mục sở thích chung (Get general interest categories) (#doc-1737174348712961)](#doc-1737174348712961)
- [9. Lấy danh mục sở thích bổ sung (Get additional interest categories) (#doc-1737180852720642)](#doc-1737180852720642)
- [10. Tìm kiếm danh mục sở thích bổ sung (#doc-1763590884474882)](#doc-1763590884474882)
- [11. Lấy danh mục sở thích bổ sung theo ID (Get additional interest categories by ID) (#doc-1763590894544897)](#doc-1763590894544897)
- [12. Lấy danh mục hành động (Get action categories) (#doc-1737166752522241)](#doc-1737166752522241)
- [13. Tìm kiếm hashtag nhắm mục tiêu (#doc-1736271339521025)](#doc-1736271339521025)
- [14. Lấy hashtag nhắm mục tiêu theo ID (Get targeting hashtags by ID) (#doc-1736280889167874)](#doc-1736280889167874)
- [15. Lấy danh mục sở thích và hành động được đề xuất (#doc-1736275204260866)](#doc-1736275204260866)
- [16. Lấy từ khóa tìm kiếm được đề xuất (Get recommended search keywords) (#doc-1838630375757825)](#doc-1838630375757825)
- [17. Lấy chẩn đoán sức khỏe chiến dịch Quảng cáo tìm kiếm (Get Search Ads Campaign Health diagnoses) (#doc-1848591212970082)](#doc-1848591212970082)
- [18. Khám phá từ khóa mới (Discover new keywords) (#doc-1855460985594881)](#doc-1855460985594881)
- [19. Lấy danh sách phiên bản hệ điều hành (Get OS versions) (#doc-1738308662898689)](#doc-1738308662898689)
- [20. Lấy danh sách mẫu thiết bị (Get device models) (#doc-1737172880570369)](#doc-1737172880570369)
- [21. Lấy danh sách nhà mạng viễn thông (Get carriers) (#doc-1737168013095938)](#doc-1737168013095938)

---

<a id="doc-1736271001971713"></a>
<!-- doc_id: 1736271001971713 -->
<!-- doc_id: 1736271001971713 -->
# Công cụ tra cứu (Tools)
> Đường dẫn: API Reference > Tools
Sử dụng nhóm endpoint này để lấy các giá trị liệt kê (enum) hoặc giá trị đề xuất cho các trường thường dùng như khu vực địa lý, múi giờ, mẫu thiết bị, v.v.

Nhóm này bao gồm các endpoint sau:
* [Tìm kiếm thẻ nhắm mục tiêu vị trí](70-tools-p1.md#doc-1761236883355649)
* [Lấy chi tiết thẻ nhắm mục tiêu vị trí theo ID](70-tools-p1.md#doc-1761237001980929)
* [Lấy danh sách vị trí khả dụng theo cài đặt](70-tools-p1.md#doc-1737189539571713)
* [Lấy danh sách vị trí khả dụng theo ID tài khoản quảng cáo TikTok](70-tools-p1.md#doc-1773644763581441)
* [Lấy danh sách ngôn ngữ](70-tools-p1.md#doc-1737188554152962)
* [Tìm kiếm hoặc liệt kê danh mục và hashtag nhắm mục tiêu sở thích, hành vi](70-tools-p1.md#doc-1796638342793218)
* [Lấy danh mục sở thích chung](70-tools-p1.md#doc-1737174348712961)
* [Lấy danh mục sở thích bổ sung](70-tools-p1.md#doc-1737180852720642)
	* [Tìm kiếm danh mục sở thích bổ sung](70-tools-p1.md#doc-1763590884474882)
	* [Lấy danh mục sở thích bổ sung theo ID](70-tools-p1.md#doc-1763590894544897)
* [Lấy danh mục hành động](70-tools-p1.md#doc-1737166752522241)
* [Tìm kiếm hashtag nhắm mục tiêu](70-tools-p1.md#doc-1736271339521025)
* [Lấy hashtag nhắm mục tiêu theo ID](70-tools-p1.md#doc-1736280889167874)
* [Lấy danh mục sở thích và hành động được đề xuất](70-tools-p1.md#doc-1736275204260866)
* [Lấy từ khóa tìm kiếm được đề xuất](70-tools-p1.md#doc-1838630375757825)
* [Lấy chẩn đoán sức khỏe chiến dịch Quảng cáo tìm kiếm](70-tools-p1.md#doc-1848591212970082)
* [Khám phá từ khóa mới](70-tools-p1.md#doc-1855460985594881)
* [Lấy danh sách phiên bản hệ điều hành](70-tools-p1.md#doc-1738308662898689)
* [Lấy danh sách mẫu thiết bị](70-tools-p1.md#doc-1737172880570369)
* [Lấy danh sách nhà mạng viễn thông](70-tools-p1.md#doc-1737168013095938)
* [Lấy danh sách nhà cung cấp dịch vụ Internet](70-tools-p2.md#doc-1762962378261506)
* [Lấy danh sách thẻ ngữ cảnh khả dụng](70-tools-p2.md#doc-1747747118654465)
* [Lấy chi tiết thẻ ngữ cảnh](70-tools-p2.md#doc-1747747180830722)
* [Lấy danh mục loại trừ nội dung khả dụng](70-tools-p2.md#doc-1769738074686465)
* [Lấy chi tiết danh mục loại trừ nội dung](70-tools-p2.md#doc-1769738105333826)
* [Lấy giá thầu đề xuất](70-tools-p2.md#doc-1737107845597186)
* [Kiểm tra điều kiện tối ưu hóa dựa trên giá trị (VBO)](70-tools-p2.md#doc-1770016073586753)
* [Lấy trạng thái ủy quyền của đối tác An toàn thương hiệu](70-tools-p2.md#doc-1738456743621634)
* [Lấy kết quả xác minh URL](70-tools-p2.md#doc-1774487686007810)
* [Lấy mã vùng điện thoại và mã khu vực cho số điện thoại](70-tools-p2.md#doc-1774488637039618)
* [Lấy danh sách múi giờ](70-tools-p2.md#doc-1738455961470977)
* [Lấy liên kết trong ứng dụng TikTok](70-tools-p2.md#doc-1738457335681026)
* [Lấy nhãn chiến dịch của tài khoản quảng cáo](70-tools-p2.md#doc-1851286489283585)
* [Lấy danh sách TikTok Mini trong tài khoản quảng cáo](70-tools-p2.md#doc-1853450329535490)
* [Lấy danh sách TikTok Series khả dụng trong tài khoản quảng cáo](70-tools-p2.md#doc-1863332009162754)
* [Lấy nguồn phân bổ và nguồn dữ liệu khả dụng cho ứng dụng](70-tools-p2.md#doc-1870952425111618)
* [Lấy trạng thái bảo vệ giá thầu](70-tools-p2.md#doc-1874392512912449)
* [Lấy lịch sử bảo vệ giá thầu](70-tools-p3.md#doc-1874392516418561)
* [Lấy bộ quy tắc trong tài khoản quảng cáo](70-tools-p3.md#doc-1879581236824514)
* [Tạo, cập nhật hoặc xóa bộ quy tắc trong tài khoản quảng cáo](70-tools-p3.md#doc-1879581240885250)

---

<a id="doc-1761236883355649"></a>
<!-- doc_id: 1761236883355649 -->
<!-- doc_id: 1761236883355649 -->
# Tìm kiếm thẻ nhắm mục tiêu vị trí (Search for location targeting tags)
> Đường dẫn: API Reference > Công cụ tra cứu > Tìm kiếm thẻ nhắm mục tiêu vị trí
Sử dụng endpoint này để tìm kiếm location targeting tags by keyword. 

Bạn có thể tìm kiếm hai loại thẻ nhắm mục tiêu dùng để nhắm đối tượng quảng cáo: mã bưu chính (zip code ID - hiện chỉ hỗ trợ cho Hoa Kỳ, hoặc postal code ID cho Canada, Brazil, Indonesia, Thái Lan và Việt Nam) và mã vị trí địa lý (location ID). Sau đó, để áp dụng các thẻ nhắm mục tiêu cho quảng cáo của bạn, bạn có thể truyền các mã zip code hoặc postal code trả về vào trường `zipcode_ids` hoặc mã vị trí vào trường `location_ids` khi gọi [/adgroup/create/](07-ad-groups-p2.md#doc-1739499616346114), [/adgroup/update/](07-ad-groups-p3.md#doc-1739586761631745) hoặc [/ad/audience_size/estimate/](07-ad-groups-p1.md#doc-1740302379236353).

Both [/tool/region/](70-tools-p1.md#doc-1737189539571713) and `/tool/targeting/search/` can be used to get location IDs.

>**Lưu ý:** • Endpoint này yêu cầu phương thức POST, vì đối với yêu cầu GET, độ dài của URL sẽ bị giới hạn. • Nhắm mục tiêu theo khu vực mã bưu chính tại Brazil, Indonesia, Thái Lan và Việt Nam hiện là tính năng chỉ dành cho danh sách cho phép (allowlist). Nếu bạn muốn truy cập, vui lòng liên hệ với đại diện TikTok của bạn. • Nhắm mục tiêu đến các quốc gia hoặc khu vực mới hỗ trợ (Azerbaijan, Bulgaria, Bolivia, Síp, Algeria, Estonia, Croatia, Kenya, Sri Lanka, Lithuania, Latvia, Nigeria, Puerto Rico, Paraguay, Serbia, Slovenia, Slovakia) sử dụng mục tiêu quảng cáo `TRAFFIC`, `LEAD_GENERATION`, `APP_PROMOTION`, hoặc `WEB_CONVERSIONS` và vị trí hiển thị TikTok hiện là các tính năng riêng biệt chỉ dành cho danh sách cho phép. Nếu bạn muốn sử dụng, hãy liên hệ với đại diện TikTok của bạn. Bạn cần đăng ký allowlist riêng cho từng quốc gia hoặc khu vực mới hỗ trợ. • Nhắm mục tiêu đến các quốc gia hoặc khu vực mới hỗ trợ (Azerbaijan, Bulgaria, Bolivia, Síp, Algeria, Estonia, Croatia, Kenya, Sri Lanka, Lithuania, Latvia, Puerto Rico, Paraguay, Serbia, Slovenia, Slovakia) sử dụng mục tiêu quảng cáo `REACH`, `VIDEO_VIEWS`, hoặc `ENGAGEMENT` và vị trí hiển thị TikTok hiện cũng là các tính năng riêng biệt chỉ dành cho allowlist. • Khi bạn nhắm mục tiêu đến các quốc gia hoặc khu vực này với mục tiêu quảng cáo `REACH`, `VIDEO_VIEWS`, hoặc `ENGAGEMENT`, các giải pháp An toàn thương hiệu (Brand Safety) bên thứ ba trước khi đặt thầu (pre-bid) không được hỗ trợ. Do đó, bạn không thể đặt `brand_safety_type` thành `THIRD_PARTY`.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/tool/targeting/search/

**Method** POST

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type  ****(Bắt buộc)**** | string | Định dạng dữ liệu yêu cầu. ⏎ Allowed format: `application/json`. |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
| advertiser_id ***(Bắt buộc)*** | string | ID tài khoản quảng cáo TikTok. |
| objective_type ***(Bắt buộc)*** | string | Mục tiêu chiến dịch. <br>Các giá trị enum hỗ trợ: `REACH`, `TRAFFIC`, `VIDEO_VIEWS`, `LEAD_GENERATION`, `ENGAGEMENT`, `APP_PROMOTION`, `WEB_CONVERSIONS`, `PRODUCT_SALES`.<br>Để xem mô tả các mục tiêu, xem [Mục tiêu](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1737585562434561). |
| promotion_type **(Điều kiện)** | string | Loại hình quảng bá dùng để quyết định nơi bạn muốn quảng bá sản phẩm. Bạn cần chỉ định trường này khi mục tiêu quảng cáo (`objective_type`) của chiến dịch KHÔNG được đặt là `REACH`, `VIDEO_VIEWS`, hoặc `ENGAGEMENT`. <br>Để xem danh sách giá trị enum, xem [Enumeration - Promotion Type](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| placements ***(Bắt buộc)*** | string[] | Các ứng dụng nơi bạn muốn phân phối quảng cáo của mình.<br><br>Để xem danh sách giá trị enum, xem [Enumeration - Placement](../15-appendix/phu-luc-p1.md#doc-1737174886619138).<br><br><p><span style="color:darkred"><b>Lưu ý</b></span>: Nếu bạn muốn tìm kiếm gần đúng mã zip code hoặc mã bưu chính để nhắm mục tiêu, giá trị trường này cần bao gồm `PLACEMENT_TIKTOK`.</p> |
| search_type ***(Bắt buộc)*** | string | Loại tìm kiếm bạn muốn thực hiện. <br><br>Các giá trị enum hỗ trợ: <ul><li>`FUZZY_SEARCH`: Tìm kiếm gần đúng một mã vị trí, mã zip code hoặc mã bưu chính đơn lẻ. <br>Đối với loại tìm kiếm này, bạn chỉ có thể truyền 1 từ khóa vào `keywords` và trả về tối đa 100 kết quả.</li><li>`BATCH_REGION_SEARCH`: Tìm kiếm hàng loạt mã vị trí địa lý. Hỗ trợ tìm kiếm gần đúng. <br>Đối với loại này, bạn có thể truyền tối đa 1.000 từ khóa vào `keywords`, và mỗi từ khóa trả về tối đa 5 kết quả theo độ liên quan.</li><li>`BATCH_ZIPCODE_SEARCH`: Tìm kiếm hàng loạt mã zip code hoặc mã bưu chính. Hỗ trợ tìm kiếm chính xác. <br>Đối với loại này, bạn có thể truyền tối đa 1.000 từ khóa vào `keywords`, và mỗi từ khóa trả về 1 kết quả hoặc không có kết quả.</li></ul><br><p><span style="color:darkred"><b>Lưu ý</b></span>: <ul><li>Nhắm mục tiêu theo khu vực mã bưu chính tại Brazil, Indonesia, Thái Lan và Việt Nam hiện là tính năng chỉ dành cho danh sách cho phép (allowlist). Vui lòng liên hệ với đại diện TikTok nếu cần hỗ trợ.</li><li>Các giá trị enum `BATCH_ZIPCODE_SEARCH` và `BATCH_REGION_SEARCH` chỉ dùng để tìm kiếm hàng loạt mã bưu chính hoặc vị trí. Ngược lại, `FUZZY_SEARCH` dùng để tìm kiếm một mã đơn lẻ.</li></ul> |
| keywords ***(Bắt buộc)*** | string[] | Các từ khóa bạn sử dụng để tìm kiếm thẻ nhắm mục tiêu. <br><br>Giới hạn độ dài: <ul><li>1 khi `search_type` là `FUZZY_SEARCH`.</li><li>1.000 khi `search_type` là `BATCH_REGION_SEARCH` hoặc `BATCH_ZIPCODE_SEARCH`.</li></ul> <br>Nếu bạn đặt `search_type` là `BATCH_ZIPCODE_SEARCH`, bạn cần truyền mã zip code hoặc mã bưu chính làm từ khóa vì loại này chỉ hỗ trợ tìm kiếm chính xác.<ul><li>Đối với nhắm mục tiêu zip code Hoa Kỳ, cung cấp mã zip code 5 chữ số của Hoa Kỳ. Ví dụ: `["10001","10002"]`.</li><li>Đối với nhắm mục tiêu bưu chính Canada, cung cấp phần FSA gồm 3 ký tự của mã bưu chính Canada. Ví dụ: `["A0A","A0B"]`.</li><li>Đối với nhắm mục tiêu bưu chính Brazil, cung cấp 5 chữ số đầu tiên của mã bưu chính. Ví dụ: `["81480","18072"]`.</li><li>Đối với nhắm mục tiêu bưu chính Indonesia, cung cấp mã bưu chính 5 chữ số. Ví dụ: `["20371","12120"]`.</li><li>Đối với nhắm mục tiêu bưu chính Thái Lan, cung cấp mã bưu chính 5 chữ số. Ví dụ: `["30000","40000"]`.</li><li>Đối với nhắm mục tiêu bưu chính Việt Nam, cung cấp 3 chữ số đầu tiên của mã bưu chính. Ví dụ: `["718","719"]`.</li></ul> |
| geo_types | string[] | Các loại vị trí địa lý bạn muốn lọc kết quả. Các giá trị enum hỗ trợ: `COUNTRY` (quốc gia hoặc khu vực), `PROVINCE` (tỉnh/bang), `CITY` (thành phố/quận hạt), `DISTRICT` (quận/huyện/thị xã), `DMA` (khu vực thị trường chỉ định DMA), `ZIP_CODE` (mã zip code hoặc mã bưu chính). <ul><li>Khi bạn chỉ định `search_type` là `FUZZY_SEARCH`, các giá trị enum cho phép là `ZIP_CODE`, `COUNTRY`, `PROVINCE`, `CITY`, `DISTRICT`, và `DMA`.</li><li>Khi chỉ định `search_type` là `BATCH_ZIPCODE_SEARCH`, giá trị enum cho phép là `ZIP_CODE`.</li><li>Khi chỉ định `search_type` là `BATCH_REGION_SEARCH`, các giá trị enum cho phép là `COUNTRY`, `PROVINCE`, `CITY`, `DISTRICT`, và `DMA`.</li></ul> |
| region_codes **(Điều kiện)** | string[] | Mã quốc gia hoặc khu vực mục tiêu bạn muốn lọc kết quả. <ul><li>Khi chỉ định `search_type` là `BATCH_ZIPCODE_SEARCH` hoặc `BATCH_REGION_SEARCH`, trường này là bắt buộc và phải đặt là `US` (Hoa Kỳ), `CA` (Canada), `BR` (Brazil), `ID` (Indonesia), `TH` (Thái Lan), hoặc `VN` (Việt Nam).</li><li>Khi chỉ định `search_type` là `FUZZY_SEARCH`, trường này là tùy chọn và bạn có thể truyền bất kỳ mã quốc gia/khu vực hỗ trợ nào. Để xem danh sách đầy đủ, xem [Mã vị trí](../15-appendix/phu-luc-p1.md#doc-1737585867307010).</li></ul> |
| operating_system | string | Hệ điều hành thiết bị bạn muốn nhắm mục tiêu. Các giá trị enum hỗ trợ: `ANDROID`, `IOS`. |
| brand_safety_type | string | Loại an toàn thương hiệu. Chỉ hợp lệ khi `placements` được đặt là `PLACEMENT_TIKTOK`. Giá trị mặc định: `NO_BRAND_SAFETY`. Các giá trị enum hỗ trợ: <ul><li>`NO_BRAND_SAFETY`: Không dùng giải pháp an toàn thương hiệu nào. Kho hàng đầy đủ, quảng cáo có thể xuất hiện cạnh một số nội dung người lớn.</li><li>`EXPANDED_INVENTORY`: Dùng giải pháp của TikTok. Kho hàng mở rộng loại bỏ hầu hết nội dung không phù hợp.</li><li>`STANDARD_INVENTORY`: Kho hàng tiêu chuẩn phù hợp với hầu hết thương hiệu.</li><li>`LIMITED_INVENTORY`: Kho hàng giới hạn, không xuất hiện cạnh nội dung có chủ đề người lớn.</li><li>`THIRD_PARTY`: Dùng giải pháp bên thứ ba. Bạn cần truyền giá trị cho trường `brand_safety_partner`.</li></ul>Để xem danh sách quốc gia/khu vực có thể triển khai dựa trên cài đặt an toàn thương hiệu, dùng endpoint [/tool/region/](70-tools-p1.md#doc-1737189539571713).<br><p><span style="color:darkred"><b>Lưu ý</b></span>: <ul><li>Các giải pháp pre-bid Brand Safety bên thứ nhất và bên thứ ba hiện là tính năng chỉ dành cho allowlist.</li><li>Xem [An toàn thương hiệu](../09-marketing-api/quan-ly-chien-dich-tom-tat.md#doc-1739381752981505) để biết thêm chi tiết.</li></ul> |
| brand_safety_partner **(Điều kiện)** | string | Chỉ bắt buộc khi `brand_safety_type` là `THIRD_PARTY`.<br>Đối tác an toàn thương hiệu.<br>Các giá trị enum hỗ trợ: `IAS`, `OPEN_SLATE` (Đối tác này được đặt tên là <strong>DoubleVerify</strong> trên Trình quản lý quảng cáo TikTok vì đã được DoubleVerify mua lại).<br><p><span style="color:darkred"><b>Lưu ý</b></span>: Các giải pháp pre-bid bên thứ ba hiện chỉ dành cho allowlist. Vui lòng liên hệ đại diện TikTok nếu cần hỗ trợ.</p> |

### Ví dụ lệnh cURL (Example)

#### Tìm kiếm mã bưu chính đơn lẻ của Canada
```http
// curl
curl --location  --request POST 'https://business-api.tiktok.com/open_api/v1.3/tool/targeting/search/' \
--header 'Access-Token:  {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id":"{{advertiser_id}}",
    "objective_type":"{{objective_type}}",
    "placements":["PLACEMENT_TIKTOK"],
    "promotion_type":"{{promotion_type}}",
    "search_type":"FUZZY_SEARCH",
    "keywords":["A0A"],
    "region_codes":["CA"]
}'
```

#### Tìm kiếm mã zip code đơn lẻ của Hoa Kỳ
```http
// curl
curl --location "https://business-api.tiktok.com/open_api/v1.3/tool/targeting/search/" \
--header "Access-Token: {{Access-Token}}" \
--header "Content-Type: application/json" \
--data "{
    "advertiser_id":"{{advertiser_id}}",
    "objective_type":"{{objective_type}}",
    "placements":["PLACEMENT_TIKTOK","PLACEMENT_PANGLE"],
    "promotion_type":"{{promotion_type}}",
    "search_type":"FUZZY_SEARCH",
    "keywords":["40601"]
}"
```

#### Tìm kiếm hàng loạt mã bưu chính của Brazil
```http
// curl
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/tool/targeting/search/' \
--header 'Access-Token: {{Access-Token}}' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id":"{{advertiser_id}}",
    "objective_type":"APP_PROMOTION",
    "placements":["PLACEMENT_TIKTOK"],
    "promotion_type":"APP_IOS",
    "search_type":"BATCH_ZIPCODE_SEARCH",
    "keywords":["81480","18072"],
    "region_codes":["BR"]
}'
```

#### Tìm kiếm hàng loạt mã vị trí địa lý
```http
// curl
curl --location "https://business-api.tiktok.com/open_api/v1.3/tool/targeting/search/" \
--header "Access-Token: {{Access-Token}}" \
--header "Content-Type: application/json" \
--data "{
    "advertiser_id":"{{advertiser_id}}",
    "objective_type":"{{objective_type}}",
    "placements":["PLACEMENT_TIKTOK","PLACEMENT_PANGLE"],
    "promotion_type":"{{promotion_type}}",
    "search_type":"BATCH_REGION_SEARCH",
    "keywords":["Kentucky","Virginia"],
    "region_codes":["US"]
}"
```

## Dữ liệu phản hồi (Response)
| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|-|-|-|
|code |number|Response code. For the complete list of response codes and descriptions, see [Appendix-Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message|string|Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|request_id |string|ID nhật ký (log ID) của yêu cầu, dùng để định danh duy nhất cho yêu cầu.  |
|data |object|Dữ liệu trả về.|
#| targeting_tag_list | object[] | Thông tin về các thẻ nhắm mục tiêu khớp với từ khóa được chỉ định. <br><p><span style="color:darkred"><b>Lưu ý</b></span>: Nhiều thẻ nhắm mục tiêu có tên khác nhau (`name`) có thể được trả về cho cùng một `keyword`.</p> |
##| keyword | string | Từ khóa được sử dụng để tìm kiếm thẻ nhắm mục tiêu. |
##| targeting_type | string | Loại nhắm mục tiêu mà thẻ nhắm mục tiêu được sử dụng. <br>Các giá trị enum hỗ trợ: `GEO` (Nhắm mục tiêu theo vị trí địa lý, bao gồm nhắm mục tiêu khu vực hành chính và mã bưu chính zip code/postal code). |
##| name | string | Tên của thẻ nhắm mục tiêu. |
##| status_info | object | Thông tin về trạng thái của thẻ nhắm mục tiêu. |
###| status | string | Trạng thái của thẻ nhắm mục tiêu. <br>Các giá trị enum hỗ trợ: `ENABLED` (có thể sử dụng để nhắm mục tiêu), `DISABLED` (không thể sử dụng để nhắm mục tiêu). |
###| reason | string | Lý do tại sao thẻ nhắm mục tiêu không thể sử dụng để nhắm mục tiêu. Trả về khi `status` = `DISABLED`. Các giá trị enum hỗ trợ: <ul><li>`OFFLINE`: Thẻ nhắm mục tiêu đang ngoại tuyến.</li><li>`NOT_SUPPORTED`: Thẻ không ngoại tuyến nhưng không được hỗ trợ cho các cài đặt đã chỉ định.</li></ul> |
##| geo | object | Thông tin về thẻ nhắm mục tiêu được sử dụng cho vị trí địa lý. <br>Trả về khi `targeting_type` là `GEO`. |
###| geo_id | string | ID vị trí, ID mã zip code hoặc ID mã bưu chính. <br>ID vị trí có thể dùng để nhắm mục tiêu theo khu vực hành chính trong khi mã zip code hoặc mã bưu chính dùng để nhắm theo mã bưu chính. <ul><li>Khi `geo_type` tương ứng là `ZIP_CODE`, bạn có thể truyền giá trị trường này vào `zipcode_ids` khi gọi [/adgroup/create/](07-ad-groups-p2.md#doc-1739499616346114), [/adgroup/update/](07-ad-groups-p3.md#doc-1739586761631745) hoặc [/ad/audience_size/estimate/](07-ad-groups-p1.md#doc-1740302379236353).</li><li>Khi `geo_type` tương ứng không phải là `ZIP_CODE`, bạn có thể truyền giá trị trường này vào `location_ids` khi gọi [/adgroup/create/](07-ad-groups-p2.md#doc-1739499616346114), [/adgroup/update/](07-ad-groups-p3.md#doc-1739586761631745) hoặc [/ad/audience_size/estimate/](07-ad-groups-p1.md#doc-1740302379236353).</li></ul> |
###| geo_type | string | Loại vị trí địa lý tương ứng với `geo_id`. <br>Các giá trị enum hỗ trợ: `COUNTRY` (quốc gia), `PROVINCE` (tỉnh/bang), `CITY` (thành phố/quận hạt), `DISTRICT` (quận/huyện/thị xã), `DMA` (khu vực thị trường chỉ định DMA), `ZIP_CODE` (mã zip code hoặc mã bưu chính).|
###| description | string | Mô tả về vị trí được nhắm mục tiêu. |
###| region_code | string | Mã quốc gia hoặc khu vực mà vị trí mục tiêu trực thuộc. |
###| parent_id | string | ID của vị trí cha. <br>Trả về `0` nếu không có vị trí cha. |
#| parent_tags | object[] | Thông tin về tất cả các thẻ nhắm mục tiêu cha. |
##| targeting_type | string | Loại nhắm mục tiêu mà thẻ nhắm mục tiêu cha được sử dụng. <br>Các giá trị enum hỗ trợ: `GEO` (Nhắm mục tiêu theo vị trí địa lý, bao gồm khu vực hành chính và mã bưu chính). |
##| name | string | Tên của thẻ nhắm mục tiêu cha. |
##| status_info | object | Thông tin về trạng thái của thẻ nhắm mục tiêu cha. |
###| status | string | Trạng thái của thẻ nhắm mục tiêu cha. <br>Các giá trị enum hỗ trợ: `ENABLED` (có thể sử dụng), `DISABLED` (không thể sử dụng). |
###| reason | string | Lý do thẻ nhắm mục tiêu cha không thể sử dụng để nhắm mục tiêu. <br>Trả về khi `status` = `DISABLED`. <br>Các giá trị enum hỗ trợ: <ul><li>`OFFLINE`: Thẻ cha đang ngoại tuyến.</li><li>`NOT_SUPPORTED`: Thẻ cha không ngoại tuyến nhưng không được hỗ trợ cho cài đặt chỉ định.</li></ul>  |
##| geo | object | Thông tin về thẻ nhắm mục tiêu cha dùng cho vị trí địa lý. <br>Trả về khi `targeting_type` là `GEO`. |
###| geo_id | string | ID vị trí cha, mã zip code hoặc mã bưu chính cha. <ul><li>Khi `geo_type` tương ứng là `ZIP_CODE`, bạn có thể truyền giá trị này vào `zipcode_ids`.</li><li>Khi `geo_type` tương ứng không phải `ZIP_CODE`, bạn có thể truyền giá trị này vào `location_ids`.</li></ul> |
###| geo_type | string | Loại vị trí địa lý tương ứng với `geo_id`. <br>Các giá trị enum hỗ trợ: `COUNTRY` (quốc gia), `PROVINCE` (tỉnh/bang), `CITY` (thành phố/quận hạt), `DISTRICT` (quận/huyện/thị xã), `DMA` (khu vực thị trường chỉ định DMA), `ZIP_CODE` (mã zip code hoặc mã bưu chính). |
###| description | string | Mô tả về vị trí cha. |
###| region_code | string | Mã quốc gia hoặc khu vực mà vị trí cha trực thuộc. |
###| parent_id | string | ID vị trí cha của vị trí cha. <br>Trả về `0` nếu không có. |

### Ví dụ lệnh cURL (Example)

#### Tìm kiếm mã bưu chính đơn lẻ của Canada
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "parent_tags": [
            {
                "status_info": {
                    "reason": null,
                    "status": "ENABLED"
                },
                "geo": {
                    "geo_id": "6251999",
                    "geo_type": "COUNTRY",
                    "parent_id": "0",
                    "region_code": "CA",
                    "description": "Country"
                },
                "isp": null,
                "name": "Canada",
                "targeting_type": "GEO"
            },
            {
                "status_info": {
                    "reason": null,
                    "status": "ENABLED"
                },
                "geo": {
                    "geo_id": "6354959",
                    "geo_type": "PROVINCE",
                    "parent_id": "6251999",
                    "region_code": "CA",
                    "description": "province"
                },
                "isp": null,
                "name": "Newfoundland and Labrador",
                "targeting_type": "GEO"
            }
        ],
        "targeting_tag_list": [
            {
                "keyword": "A0A",
                "status_info": {
                    "reason": null,
                    "status": "ENABLED"
                },
                "geo": {
                    "geo_id": "8124000000533",
                    "geo_type": "ZIP_CODE",
                    "parent_id": "6354959",
                    "region_code": "CA",
                    "description": "postcode"
                },
                "isp": null,
                "name": "A0A",
                "targeting_type": "GEO"
            }
        ]
    }
}
```

#### Tìm kiếm mã zip code đơn lẻ của Hoa Kỳ
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "targeting_tag_list": [
            {
                "geo": {
                    "description": "postcode",
                    "parent_id": "4292188",
                    "geo_type": "ZIP_CODE",
                    "region_code": "US",
                    "geo_id": "8840000440601"
                },
                "keyword": "40601",
                "name": "40601",
                "targeting_type": "GEO",
                "status_info": {
                    "status": "ENABLED",
                    "reason": null
                }
            }
        ],
        "parent_tags": [
            {
                "status_info": {
                    "status": "ENABLED",
                    "reason": null
                },
                "geo": {
                    "description": "State",
                    "parent_id": "6252001",
                    "geo_type": "PROVINCE",
                    "region_code": "US",
                    "geo_id": "6254925"
                },
                "targeting_type": "GEO",
                "name": "Kentucky"
            },
            {
                "status_info": {
                    "status": "ENABLED",
                    "reason": null
                },
                "geo": {
                    "description": "County",
                    "parent_id": "6254925",
                    "geo_type": "CITY",
                    "region_code": "US",
                    "geo_id": "4292202"
                },
                "targeting_type": "GEO",
                "name": "Franklin County"
            },
            {
                "status_info": {
                    "status": "ENABLED",
                    "reason": null
                },
                "geo": {
                    "description": "City",
                    "parent_id": "4292202",
                    "geo_type": "DISTRICT",
                    "region_code": "US",
                    "geo_id": "4292188"
                },
                "targeting_type": "GEO",
                "name": "Frankfort"
            },
            {
                "status_info": {
                    "status": "ENABLED",
                    "reason": null
                },
                "geo": {
                    "description": "state",
                    "parent_id": "0",
                    "geo_type": "COUNTRY",
                    "region_code": "US",
                    "geo_id": "6252001"
                },
                "targeting_type": "GEO",
                "name": "United States"
            }
        ]
    }
}
```

#### Tìm kiếm hàng loạt mã bưu chính của Brazil
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "parent_tags": [
            {
                "status_info": {
                    "reason": null,
                    "status": "ENABLED"
                },
                "isp": null,
                "name": "Parana",
                "geo": {
                    "geo_type": "PROVINCE",
                    "region_code": "BR",
                    "geo_id": "3455077",
                    "description": "state",
                    "parent_id": "3469034"
                },
                "targeting_type": "GEO"
            },
            {
                "status_info": {
                    "reason": null,
                    "status": "ENABLED"
                },
                "isp": null,
                "name": "Sao Paulo",
                "geo": {
                    "geo_type": "PROVINCE",
                    "region_code": "BR",
                    "geo_id": "3448433",
                    "description": "state",
                    "parent_id": "3469034"
                },
                "targeting_type": "GEO"
            },
            {
                "status_info": {
                    "reason": null,
                    "status": "ENABLED"
                },
                "isp": null,
                "name": "Brazil",
                "geo": {
                    "geo_type": "COUNTRY",
                    "region_code": "BR",
                    "geo_id": "3469034",
                    "description": "Country",
                    "parent_id": "0"
                },
                "targeting_type": "GEO"
            }
        ],
        "targeting_tag_list": [
            {
                "status_info": {
                    "reason": null,
                    "status": "ENABLED"
                },
                "isp": null,
                "name": "81480",
                "geo": {
                    "geo_type": "ZIP_CODE",
                    "region_code": "BR",
                    "geo_id": "8052000011871",
                    "description": "postcode",
                    "parent_id": "3455077"
                },
                "targeting_type": "GEO",
                "keyword": "81480"
            },
            {
                "status_info": {
                    "reason": null,
                    "status": "ENABLED"
                },
                "isp": null,
                "name": "18072",
                "geo": {
                    "geo_type": "ZIP_CODE",
                    "region_code": "BR",
                    "geo_id": "8052000002545",
                    "description": "postcode",
                    "parent_id": "3448433"
                },
                "targeting_type": "GEO",
                "keyword": "18072"
            }
        ]
    }
}
```

#### Tìm kiếm hàng loạt mã vị trí địa lý
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "targeting_tag_list": [
            {
                "status_info": {
                    "reason": null,
                    "status": "ENABLED"
                },
                "name": "Kentucky",
                "geo": {
                    "geo_type": "PROVINCE",
                    "description": "State",
                    "parent_id": "6252001",
                    "geo_id": "6254925",
                    "region_code": "US"
                },
                "keyword": "Kentucky",
                "targeting_type": "GEO"
            },
            {
                "status_info": {
                    "reason": null,
                    "status": "ENABLED"
                },
                "name": "Virginia Beach",
                "geo": {
                    "geo_type": "DISTRICT",
                    "description": "City",
                    "parent_id": "4791271",
                    "geo_id": "4791259",
                    "region_code": "US"
                },
                "keyword": "Virginia",
                "targeting_type": "GEO"
            },
            {
                "status_info": {
                    "reason": null,
                    "status": "ENABLED"
                },
                "name": "Virginia Beach",
                "geo": {
                    "geo_type": "CITY",
                    "description": "County",
                    "parent_id": "6254928",
                    "geo_id": "4791271",
                    "region_code": "US"
                },
                "keyword": "Virginia",
                "targeting_type": "GEO"
            },
            {
                "status_info": {
                    "reason": null,
                    "status": "ENABLED"
                },
                "name": "West Virginia",
                "geo": {
                    "geo_type": "PROVINCE",
                    "description": "State",
                    "parent_id": "6252001",
                    "geo_id": "4826850",
                    "region_code": "US"
                },
                "keyword": "Virginia",
                "targeting_type": "GEO"
            },
            {
                "status_info": {
                    "reason": null,
                    "status": "ENABLED"
                },
                "name": "Virginia",
                "geo": {
                    "geo_type": "PROVINCE",
                    "description": "State",
                    "parent_id": "6252001",
                    "geo_id": "6254928",
                    "region_code": "US"
                },
                "keyword": "Virginia",
                "targeting_type": "GEO"
            },
            {
                "status_info": {
                    "reason": null,
                    "status": "ENABLED"
                },
                "name": "Virginia",
                "geo": {
                    "geo_type": "DISTRICT",
                    "description": "City",
                    "parent_id": "5068853",
                    "geo_id": "5081185",
                    "region_code": "US"
                },
                "keyword": "Virginia",
                "targeting_type": "GEO"
            }
        ],
        "parent_tags": [
            {
                "status_info": {
                    "reason": null,
                    "status": "ENABLED"
                },
                "geo": {
                    "geo_type": "PROVINCE",
                    "description": "State",
                    "parent_id": "6252001",
                    "geo_id": "5073708",
                    "region_code": "US"
                },
                "targeting_type": "GEO",
                "name": "Nebraska"
            },
            {
                "status_info": {
                    "reason": null,
                    "status": "ENABLED"
                },
                "geo": {
                    "geo_type": "CITY",
                    "description": "County",
                    "parent_id": "5073708",
                    "geo_id": "5068853",
                    "region_code": "US"
                },
                "targeting_type": "GEO",
                "name": "Gage County"
            },
            {
                "status_info": {
                    "reason": null,
                    "status": "ENABLED"
                },
                "geo": {
                    "geo_type": "COUNTRY",
                    "description": "Country",
                    "parent_id": "0",
                    "geo_id": "6252001",
                    "region_code": "US"
                },
                "targeting_type": "GEO",
                "name": "United States"
            },
            {
                "status_info": {
                    "reason": null,
                    "status": "ENABLED"
                },
                "geo": {
                    "geo_type": "PROVINCE",
                    "description": "State",
                    "parent_id": "6252001",
                    "geo_id": "6254928",
                    "region_code": "US"
                },
                "targeting_type": "GEO",
                "name": "Virginia"
            },
            {
                "status_info": {
                    "reason": null,
                    "status": "ENABLED"
                },
                "geo": {
                    "geo_type": "CITY",
                    "description": "County",
                    "parent_id": "6254928",
                    "geo_id": "4791271",
                    "region_code": "US"
                },
                "targeting_type": "GEO",
                "name": "Virginia Beach"
            }
        ]
    }
}
```

---

<a id="doc-1761237001980929"></a>
<!-- doc_id: 1761237001980929 -->
<!-- doc_id: 1761237001980929 -->
# Lấy thông tin chi tiết thẻ nhắm mục tiêu vị trí theo ID (Obtain details about location targeting tags by ID)
> Đường dẫn: API Reference > Tools > Obtain details about location targeting tags by ID
Sử dụng endpoint này để lấy thông tin information about location targeting tags by ID. 

Bạn có thể lấy thông tin chi tiết về ba loại thẻ nhắm mục tiêu: mã zip code (hiện chỉ hỗ trợ cho Hoa Kỳ) hoặc mã bưu chính postal code (hiện chỉ hỗ trợ cho Canada, Brazil, Indonesia, Thái Lan và Việt Nam), mã vị trí địa lý (location ID) và mã nhà mạng Internet (ISP ID).

See the **"Supported parameters for different types of targeting tag"  ** section below to learn about the request parameters you need to pass for different types of targeting tags.

>**Lưu ý:** • Bạn chỉ có thể sử dụng endpoint này, thay vì [/tool/region/](70-tools-p1.md#doc-1737189539571713), để lấy thông tin về mã zip code hoặc mã bưu chính. • Endpoint này yêu cầu phương thức POST, vì đối với yêu cầu GET độ dài của URL sẽ bị giới hạn.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/tool/targeting/info/

**Method** POST

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type  ****(Bắt buộc)**** | string | Định dạng dữ liệu yêu cầu. ⏎ Allowed format: `application/json`. |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
| advertiser_id ***(Bắt buộc)*** | string | ID tài khoản quảng cáo TikTok. |
|scene|string|Loại nhắm mục tiêu mà `targeting_ids` đã chỉ định được sử dụng. <br>Các giá trị enum hỗ trợ: <ul><li>`GEO`: Nhắm mục tiêu theo vị trí địa lý, bao gồm khu vực hành chính và mã bưu chính.</li><li>`ISP`: Nhắm mục tiêu theo nhà cung cấp dịch vụ Internet (ISP).</li></ul><br>Giá trị mặc định: `GEO`. |
|targeting_ids ***(Bắt buộc)***|string[]|Danh sách ID thẻ nhắm mục tiêu.<br>Bạn có thể truyền mã vị trí (location ID), mã zip code hoặc mã bưu chính (postal code ID), hoặc mã nhà mạng ISP.<br>Kích thước tối đa: 1.000.<br>Bạn có thể lấy mã vị trí hoặc mã bưu chính qua trường `geo_id` trả về từ [/tool/targeting/search/](70-tools-p1.md#doc-1761236883355649), hoặc lấy mã vị trí qua `location_id` trả về từ [/tool/region/](70-tools-p1.md#doc-1737189539571713).<br>Bạn có thể lấy mã ISP qua `isp_id` trả về từ [/tool/targeting/list/](70-tools-p2.md#doc-1762962378261506).|
| objective_type**(Điều kiện)**| string |Bắt buộc khi `scene` được đặt là `GEO`.<br>Mục tiêu chiến dịch.<br>Các giá trị enum hỗ trợ: `REACH`, `TRAFFIC`, `VIDEO_VIEWS`, `LEAD_GENERATION`, `ENGAGEMENT`, `APP_PROMOTION`, `WEB_CONVERSIONS`, `PRODUCT_SALES`.<br>Để xem mô tả các mục tiêu, xem [Mục tiêu](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1737585562434561). |
|promotion_type**(Điều kiện)** |string|Bắt buộc khi `scene` được đặt là `GEO` và `objective_type` KHÔNG phải là `REACH`, `VIDEO_VIEWS` hoặc `ENGAGEMENT`. <br>Loại quảng bá xác định nơi bạn muốn quảng bá sản phẩm. <br>Để xem danh sách giá trị enum, xem [Phụ lục - Loại quảng bá](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
|placements **(Điều kiện)**|string[]|Bắt buộc khi `scene` được đặt là `GEO`.<br>Các ứng dụng nơi bạn muốn phân phối quảng cáo của mình. Để xem danh sách giá trị enum, xem [Enumeration - Placement](../15-appendix/phu-luc-p1.md#doc-1737174886619138).<br><p><span style="color:darkred"><b>Lưu ý</b></span>: Nếu bạn muốn lấy thông tin về mã zip code hoặc mã bưu chính để nhắm mục tiêu, giá trị của trường này cần bao gồm `PLACEMENT_TIKTOK`.</p> |
| operating_system | string |Chỉ hợp lệ khi `scene` is set as `GEO`.<br> Device operating system that you want to target. Các giá trị enum hỗ trợ: `ANDROID`, `IOS`. |
|brand_safety_type|string|Loại an toàn thương hiệu. Chỉ hợp lệ khi `scene` được đặt là `GEO` và `placements` được đặt là `PLACEMENT_TIKTOK`. Giá trị mặc định: `NO_BRAND_SAFETY`. Các giá trị enum hỗ trợ: <ul><li>`NO_BRAND_SAFETY`: Không sử dụng bất kỳ giải pháp an toàn thương hiệu nào. Kho hàng đầy đủ.</li><li>`EXPANDED_INVENTORY`: Kho hàng mở rộng.</li><li>`STANDARD_INVENTORY`: Kho hàng tiêu chuẩn.</li><li>`LIMITED_INVENTORY`: Kho hàng giới hạn.</li><li>`THIRD_PARTY`: Sử dụng giải pháp bên thứ ba.</li></ul>Xem [/tool/region/](70-tools-p1.md#doc-1737189539571713) để biết thêm chi tiết.<br><p><span style="color:darkred"><b>Lưu ý</b></span>: Các giải pháp pre-bid Brand Safety bên thứ nhất và bên thứ ba hiện chỉ dành cho allowlist.</p>|
| brand_safety_partner **(Điều kiện)** | string | Chỉ bắt buộc khi `brand_safety_type` là `THIRD_PARTY`.<br>Đối tác an toàn thương hiệu.<br>Các giá trị enum hỗ trợ: `IAS`, `OPEN_SLATE` (Đối tác này được đặt tên là <strong>DoubleVerify</strong> trên Trình quản lý quảng cáo TikTok vì đã được DoubleVerify mua lại).<br><p><span style="color:darkred"><b>Lưu ý</b></span>: Các giải pháp pre-bid bên thứ ba hiện chỉ dành cho allowlist. Vui lòng liên hệ đại diện TikTok nếu cần hỗ trợ.</p> |
### Các tham số được hỗ trợ cho từng loại thẻ nhắm mục tiêu
 See the list below to learn about the supported parameters for different types of targeting tag. The parameters can be required (✅), optional (✔) or unsupported (❌) for the type of targeting tag.

| Trường (Field) | ID mã Zip Code | ID vị trí (Location ID) | ID nhà mạng (ISP ID) |
|---|---|---|---|
| `advertiser_id` | ✅ | ✅ | ✅ |
| `scene` | ✅ ⏎ Must be set to `GEO`. | ✅ ⏎ Must be set to `GEO`. | ✅ ⏎ Must be set to `ISP`. |
| `targeting_ids` | ✅ | ✅ | ✅ |
| `objective_type` | ✅ | ✅ | ❌ |
| `promotion_type` | ✔ | ✔ | ❌ |
| `placements` | ✅ | ✅ | ❌ |
| `operating_system` | ✔ | ✔ | ❌ |
| `brand_safety_type` | ✔ | ✔ | ❌ |
| `brand_safety_partner` | ✔ | ✔ | ❌ |

### Ví dụ lệnh cURL (Example)

#### Lấy thông tin về mã zip code
```http
// curl
curl --location "https://business-api.tiktok.com/open_api/v1.3/tool/targeting//info/" \
--header "Access-Token: {{Access-Token}}" \
--header "Content-Type: application/json" \
--data "{
    "advertiser_id":"{{advertiser_id}}",
    "objective_type":"{{objective_type}}",
    "promotion_type":"{{promotion_type}}",
    "placements":["PLACEMENT_TIKTOK","PLACEMENT_PANGLE"],
    "targeting_ids":["8840000454548","8840000454525"]
}"
```
#### Lấy thông tin về mã nhà mạng Internet (ISP ID)
```http
// curl
curl --location "https://business-api.tiktok.com/open_api/v1.3/tool/targeting//info/" 
--header "Access-Token: {{Access-Token}}" 
--header "Content-Type: application/json" 
--data "{
    "advertiser_id":"{{advertiser_id}}",
    "scene":"ISP",
    "targeting_ids":["EG00045"]
}"
```

## Dữ liệu phản hồi (Response)
| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|-|-|-|
|code |number|Response code. For the complete list of response codes and descriptions, see [Appendix-Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message|string|Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|request_id |string|ID nhật ký (log ID) của yêu cầu, dùng để định danh duy nhất cho yêu cầu.  |
|data |object|Dữ liệu trả về.|
#| targeting_tag_list | object[] | Thông tin về các thẻ nhắm mục tiêu khớp với các ID thẻ nhắm mục tiêu đã chỉ định.|
##| targeting_type | string | Loại nhắm mục tiêu mà thẻ được sử dụng. <br>Các giá trị enum hỗ trợ: <ul><li>`GEO`: Nhắm mục tiêu theo vị trí địa lý, bao gồm khu vực hành chính và mã bưu chính.</li><li>`ISP`: Nhắm mục tiêu theo nhà cung cấp dịch vụ Internet.</li></ul> |
##| name | string | Tên của thẻ nhắm mục tiêu. |
##| status_info | object | Thông tin về trạng thái của thẻ nhắm mục tiêu. |
###| status | string | Trạng thái của thẻ nhắm mục tiêu. <br>Các giá trị enum hỗ trợ: `ENABLED` (có thể sử dụng để nhắm mục tiêu), `DISABLED` (không thể sử dụng để nhắm mục tiêu). |
###| reason | string | Lý do tại sao thẻ nhắm mục tiêu không thể sử dụng để nhắm mục tiêu. Trả về khi `status` = `DISABLED`. Các giá trị enum hỗ trợ: <ul><li>`OFFLINE`: Thẻ nhắm mục tiêu đang ngoại tuyến.</li><li>`NOT_SUPPORTED`: Thẻ không ngoại tuyến nhưng không được hỗ trợ cho các cài đặt đã chỉ định.</li></ul> |
##| geo | object | Thông tin về thẻ nhắm mục tiêu được sử dụng cho vị trí địa lý. <br>Trả về khi `targeting_type` là `GEO`. |
###| geo_id | string | ID vị trí, ID mã zip code hoặc ID mã bưu chính. <br>ID vị trí có thể dùng để nhắm mục tiêu theo khu vực hành chính trong khi mã zip code hoặc mã bưu chính dùng để nhắm theo mã bưu chính. <ul><li>Khi `geo_type` tương ứng là `ZIP_CODE`, bạn có thể truyền giá trị trường này vào `zipcode_ids` khi gọi [/adgroup/create/](07-ad-groups-p2.md#doc-1739499616346114), [/adgroup/update/](07-ad-groups-p3.md#doc-1739586761631745) hoặc [/ad/audience_size/estimate/](07-ad-groups-p1.md#doc-1740302379236353).</li><li>Khi `geo_type` tương ứng không phải là `ZIP_CODE`, bạn có thể truyền giá trị trường này vào `location_ids` khi gọi [/adgroup/create/](07-ad-groups-p2.md#doc-1739499616346114), [/adgroup/update/](07-ad-groups-p3.md#doc-1739586761631745) hoặc [/ad/audience_size/estimate/](07-ad-groups-p1.md#doc-1740302379236353).</li></ul> |
###| geo_type | string | Loại vị trí tương ứng với `geo_id`. <br>Các giá trị enum hỗ trợ: `COUNTRY` (quốc gia), `PROVINCE` (tỉnh/bang), `CITY` (thành phố), `DISTRICT` (quận/huyện), `DMA` (khu vực thị trường chỉ định DMA), `ZIP_CODE` (mã zip code hoặc mã bưu chính).|
###| description | string | Mô tả về vị trí được nhắm mục tiêu. |
###| region_code | string | Mã quốc gia hoặc khu vực mà vị trí mục tiêu trực thuộc. |
###| parent_id | string | ID của vị trí cha. <br>Trả về `0` nếu không có vị trí cha. |
##| isp | object | Thông tin về thẻ nhắm mục tiêu được sử dụng cho nhà mạng Internet. <br>Trả về khi `targeting_type` là `ISP`. |
###| isp_id | string | ID của nhà cung cấp dịch vụ Internet mà bạn có thể nhắm mục tiêu. |
###| location_id | string | ID vị trí địa lý mà `isp_id` có thể kết hợp sử dụng cùng. Chỉ hỗ trợ ID vị trí ở cấp quốc gia hoặc khu vực. |
###| region_code | string | Mã khu vực hoặc quốc gia mà `isp_id` trực thuộc. |
#| parent_tags | object[] | Thông tin về tất cả các thẻ nhắm mục tiêu cha. |
##| targeting_type | string | Loại nhắm mục tiêu mà thẻ nhắm mục tiêu cha được sử dụng. <br>Các giá trị enum hỗ trợ: `GEO` (Nhắm mục tiêu theo vị trí địa lý, bao gồm khu vực hành chính và mã bưu chính). |
##| name | string | Tên của thẻ nhắm mục tiêu cha. |
##| status_info | object | Thông tin về trạng thái của thẻ nhắm mục tiêu cha. |
###| status | string | Trạng thái của thẻ nhắm mục tiêu cha. <br>Các giá trị enum hỗ trợ: `ENABLED` (có thể sử dụng), `DISABLED` (không thể sử dụng). |
###| reason | string | Lý do thẻ nhắm mục tiêu cha không thể sử dụng để nhắm mục tiêu. <br>Trả về khi `status` = `DISABLED`. <br>Các giá trị enum hỗ trợ: <ul><li>`OFFLINE`: Thẻ cha đang ngoại tuyến.</li><li>`NOT_SUPPORTED`: Thẻ cha không ngoại tuyến nhưng không được hỗ trợ cho cài đặt chỉ định.</li></ul>  |
##| geo | object | Thông tin về thẻ nhắm mục tiêu cha dùng cho vị trí địa lý. <br>Trả về khi `targeting_type` là `GEO`. |
###| geo_id | string | ID vị trí cha, mã zip code hoặc mã bưu chính cha. <ul><li>Khi `geo_type` tương ứng là `ZIP_CODE`, bạn có thể truyền giá trị này vào `zipcode_ids`.</li><li>Khi `geo_type` tương ứng không phải `ZIP_CODE`, bạn có thể truyền giá trị này vào `location_ids`.</li></ul> |
###| geo_type | string | Loại vị trí tương ứng với `geo_id`. <br>Các giá trị enum hỗ trợ: `COUNTRY` (quốc gia), `PROVINCE` (tỉnh/bang), `CITY` (thành phố), `DISTRICT` (quận/huyện), `DMA` (khu vực thị trường chỉ định DMA), `ZIP_CODE` (mã zip code hoặc mã bưu chính). |
###| description | string | Mô tả về vị trí cha. |
###| region_code | string | Mã quốc gia hoặc khu vực mà vị trí cha trực thuộc. |
###| parent_id | string | ID vị trí cha của vị trí cha. <br>Trả về `0` nếu không có. |

### Ví dụ lệnh cURL (Example)

#### Lấy thông tin về mã zip code
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "parent_tags": [
            {
                "status_info": {
                    "status": "ENABLED",
                    "reason": null
                },
                "name": "United States",
                "geo": {
                    "region_code": "US",
                    "geo_type": "COUNTRY",
                    "description": "state",
                    "parent_id": "0",
                    "geo_id": "6252001"
                },
                "targeting_type": "GEO"
            },
            {
                "status_info": {
                    "status": "ENABLED",
                    "reason": null
                },
                "name": "Wisconsin",
                "geo": {
                    "region_code": "US",
                    "geo_type": "PROVINCE",
                    "description": "State",
                    "parent_id": "6252001",
                    "geo_id": "5279468"
                },
                "targeting_type": "GEO"
            },
            {
                "status_info": {
                    "status": "ENABLED",
                    "reason": null
                },
                "name": "Oneida County",
                "geo": {
                    "region_code": "US",
                    "geo_type": "CITY",
                    "description": "County",
                    "parent_id": "5279468",
                    "geo_id": "5265726"
                },
                "targeting_type": "GEO"
            },
            {
                "status_info": {
                    "status": "ENABLED",
                    "reason": null
                },
                "name": "Minocqua",
                "geo": {
                    "region_code": "US",
                    "geo_type": "DISTRICT",
                    "description": "City",
                    "parent_id": "5265726",
                    "geo_id": "5263156"
                },
                "targeting_type": "GEO"
            },
            {
                "status_info": {
                    "status": "ENABLED",
                    "reason": null
                },
                "name": "Iron County",
                "geo": {
                    "region_code": "US",
                    "geo_type": "CITY",
                    "description": "County",
                    "parent_id": "5279468",
                    "geo_id": "5257533"
                },
                "targeting_type": "GEO"
            },
            {
                "status_info": {
                    "status": "ENABLED",
                    "reason": null
                },
                "name": "Gile",
                "geo": {
                    "region_code": "US",
                    "geo_type": "DISTRICT",
                    "description": "City",
                    "parent_id": "5257533",
                    "geo_id": "116027566"
                },
                "targeting_type": "GEO"
            }
        ],
        "targeting_tag_list": [
            {
                "status_info": {
                    "status": "ENABLED",
                    "reason": null
                },
                "name": "54548",
                "geo": {
                    "region_code": "US",
                    "geo_type": "ZIP_CODE",
                    "description": "postcode",
                    "parent_id": "5263156",
                    "geo_id": "8840000454548"
                },
                "targeting_type": "GEO"
            },
            {
                "status_info": {
                    "status": "ENABLED",
                    "reason": null
                },
                "name": "54525",
                "geo": {
                    "region_code": "US",
                    "geo_type": "ZIP_CODE",
                    "description": "postcode",
                    "parent_id": "116027566",
                    "geo_id": "8840000454525"
                },
                "targeting_type": "GEO"
            }
        ]
    }
}
```

#### Lấy thông tin về mã nhà mạng Internet (ISP ID)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "targeting_tag_list": [
            {
                "status_info": {
                    "reason": null,
                    "status": "ENABLED"
                },
                "targeting_type": "ISP",
                "geo": null,
                "isp": {
                    "region_code": "EG",
                    "isp_id": "EG00045",
                    "location_id": "357994"
                },
                "name": "Etisalat Misr"
            }
        ],
        "parent_tags": []
    }
}
```

---

<a id="doc-1737189539571713"></a>
<!-- doc_id: 1737189539571713 -->
<!-- doc_id: 1737189539571713 -->
# Lấy danh sách vị trí khả dụng theo cài đặt (Get available locations by different settings)
> Đường dẫn: API Reference > Tools > Get available locations by different settings
Sử dụng endpoint này để lấy thông tin codes of locations that your ads can be delivered to **based on your objectives, placements, and optionally targeting operating systems, and brand safety settings. **
Nếu muốn lấy các vị trí khả dụng mà quảng cáo của bạn có thể được phân phối dựa trên ID nhà quảng cáo, hãy dùng endpoint **/search/region/**.

> **Note:** 
> • Nhắm mục tiêu đến các quốc gia hoặc khu vực mới hỗ trợ sử dụng mục tiêu `TRAFFIC`, `LEAD_GENERATION`, `APP_PROMOTION`, hoặc `WEB_CONVERSIONS` và vị trí TikTok hiện là các tính năng riêng biệt dành riêng cho allowlist. Bạn cần nộp đơn allowlist riêng cho từng quốc gia/khu vực. • Nhắm mục tiêu đến các quốc gia/khu vực mới hỗ trợ với mục tiêu `REACH`, `VIDEO_VIEWS`, hoặc `ENGAGEMENT` cũng là tính năng riêng chỉ dành cho allowlist. • Khi nhắm các quốc gia/khu vực này với mục tiêu `REACH`, `VIDEO_VIEWS`, hoặc `ENGAGEMENT`, các giải pháp Brand Safety bên thứ ba pre-bid không được hỗ trợ, vì vậy không thể đặt `brand_safety_type` là `THIRD_PARTY`.

Cấp độ của các vị trí được thể hiện trong sơ đồ dưới đây. Province, DMA (Designated Market Area) và Metropolitan cùng cấp. Province, City và District là các đơn vị hành chính nên `area_type` của chúng là `ADMIN`. Với DMA và Metropolitan, `area_type` là `METROPOLITAN_OR_DMA`.

## Yêu cầu gọi API (Request)

**Endpoint** `https://business-api.tiktok.com/open_api/v1.3/tool/region/`

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id  ****(Bắt buộc)**** | string | ID tài khoản quảng cáo TikTok |
| placements ****(Bắt buộc)**** | string[] | Các ứng dụng nơi bạn muốn phân phối quảng cáo của mình. Để xem danh sách giá trị enum, xem [Enumeration - Placement](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| objective_type  ****(Bắt buộc)**** | string | Mục tiêu quảng cáo của bạn. Để xem các giá trị enum và giải thích chi tiết, xem [Mục tiêu quảng cáo](../09-marketing-api/quan-ly-chien-dich-p1.md#doc-1737585562434561). |
| search_campaign_enabled | boolean | Có thực hiện create a Search Ads Campaign. ⏎ With Search Ads Campaigns, you set up your campaign to target ads in TikTok search results. Search Ads Campaigns reach those in your audience actively looking for products or information related to your brand. You'll use relevant keywords and search terms to help guide audiences to your ads. ⏎ Các giá trị được hỗ trợ: `true`, `false`. ⏎ Giá trị mặc định: `false`. ⏎ To learn more about how to create Search Ads Campaigns, see [Create Upgraded Smart+ Search Ads Campaigns](../08-use-cases/use-case-tao-chien-dich-p2.md#doc-1873144295333889). |
| app_promotion_type **(Điều kiện)** | string | Bắt buộc khi `objective_type` là `APP_PROMOTION`. ⏎ Loại quảng bá ứng dụng. ⏎ Giá trị enum: • `APP_INSTALL`: Cài đặt ứng dụng. Thu hút người dùng mới cài đặt ứng dụng của bạn. • `APP_RETARGETING`: Nhắm mục tiêu lại ứng dụng. Tái gắn kết người dùng hiện tại để họ thực hiện hành động trong ứng dụng. • `APP_PREREGISTRATION`: Đăng ký trước ứng dụng. Thu hút người dùng đăng ký trước khi ứng dụng ra mắt. Để tìm hiểu cách tạo quảng cáo Đăng ký trước ứng dụng thủ công, xem [tại đây](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1772549012687873). • `MINIS`: TikTok Minis hoặc Series. Quảng bá Series, mini series hoặc mini game bằng cách tối ưu hóa lưu lượng tự nhiên và quảng cáo. |
| level_range | string | Cấp độ vị trí bạn muốn lấy. Các giá trị enum hỗ trợ: • `ALL`: all levels • `TO_COUNTRY`: only country or region level •  `TO_PROVINCE`: country and province level; DMA and Metropolitan are at province level. • `TO_CITY`: country, province, and city levels • `TO_DISTRICT`: country, province, city, and district levels. |
| language | string | Ngôn ngữ của tên vị trí được trả về (`name`). ⏎ Giá trị mặc định: `en` (Tiếng Anh). ⏎ Để xem các giá trị cho phép, xem Danh sách giá trị cho `language`. ⏎ **Lưu ý**: • Nếu ngôn ngữ đã chỉ định không được hỗ trợ, ngôn ngữ đó sẽ bị bỏ qua và sử dụng giá trị mặc định là `en`. • Nếu chỉ định một ngôn ngữ ngoài tiếng Anh, tên các vị trí nằm ngoài quốc gia bản địa của ngôn ngữ đó có thể không được dịch. Ví dụ: nếu bạn đặt `language` là `ja` (tiếng Nhật), tên các vị trí bên ngoài Nhật Bản có thể không được dịch. |
| shopping_ads_type | string | Chỉ hợp lệ khi `objective_type` là `PRODUCT_SALES`. ⏎ Loại quảng cáo mua sắm (Shopping Ads). ⏎ Các giá trị enum hỗ trợ: • `VIDEO`: Quảng cáo mua sắm qua video. • `LIVE`: Quảng cáo mua sắm qua LIVE. • `PRODUCT_SHOPPING_ADS`: Quảng cáo mua sắm sản phẩm. ⏎ Để xem hướng dẫn chi tiết các loại quảng cáo mua sắm và quy trình tạo [Video Shopping Ads](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1741942291730434), [Live Shopping Ads](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1754162402455554) và [Product Shopping Ads](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1785886237030401), xem [Tạo quảng cáo mua sắm](../08-use-cases/use-case-tao-chien-dich-p1.md#doc-1741942179356738). |
| promotion_type | string | Promotion type (Optimization location). ⏎ Để xem danh sách giá trị enum, xem [Enumeration - Promotion Type](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| promotion_target_type | string | Hợp lệ khi `objective_type` là `LEAD_GENERATION`. ⏎ Loại hình quảng bá cho mục tiêu Tìm kiếm khách hàng tiềm năng. ⏎ Các giá trị enum hỗ trợ: • `INSTANT_PAGE`: Biểu mẫu tức thì (Instant Form) trong ứng dụng TikTok tải nhanh để thu thập thêm khách hàng tiềm năng. • `EXTERNAL_WEBSITE`: Biểu mẫu trang web (Website Form). Sử dụng trang đích có biểu mẫu trang web hoặc trang tức thì chuyển hướng đến trang web để thu thập khách hàng tiềm năng. |
| operating_system | string | Hệ điều hành bạn muốn nhắm mục tiêu. Các giá trị enum hỗ trợ: `ANDROID`, `IOS`. |
| brand_safety_type | string | Loại an toàn thương hiệu. Chỉ hợp lệ khi `placements` được đặt là `PLACEMENT_TIKTOK`. Giá trị mặc định: `NO_BRAND_SAFETY`. Các giá trị enum hỗ trợ: • `NO_BRAND_SAFETY`: Không dùng giải pháp an toàn thương hiệu. Kho hàng đầy đủ. • `EXPANDED_INVENTORY`: Kho hàng mở rộng. • `STANDARD_INVENTORY`: Kho hàng tiêu chuẩn. • `LIMITED_INVENTORY`: Kho hàng giới hạn. • `THIRD_PARTY`: Giải pháp bên thứ ba. ⏎ **Lưu ý**: Các giải pháp pre-bid Brand Safety hiện chỉ dành cho allowlist. Xem [An toàn thương hiệu](../09-marketing-api/quan-ly-chien-dich-tom-tat.md#doc-1739381752981505). |
| brand_safety_partner**(Điều kiện)** | string | Đối tác an toàn thương hiệu. Bắt buộc khi `brand_safety_type` là `THIRD_PARTY`, và `placements` cần được đặt là `PLACEMENT_TIKTOK`. Các giá trị enum hỗ trợ: `IAS`, `OPEN_SLATE` (Đối tác này được đặt tên là **DoubleVerify** trên Trình quản lý quảng cáo TikTok vì đã được DoubleVerify mua lại). ⏎ **Lưu ý**: Các giải pháp an toàn thương hiệu bên thứ ba pre-bid hiện chỉ dành cho allowlist. Vui lòng liên hệ đại diện TikTok nếu cần hỗ trợ. |
| rf_campaign_type | string | Khi `objective_type` được chỉ định là `RF_REACH`, sử dụng trường này để đặt chiến dịch là chiến dịch TikTok Pulse, từ đó bạn có thể lấy các thẻ ngữ cảnh cao cấp khả dụng. ⏎ Các giá trị enum hỗ trợ: `STANDARD` (Chiến dịch Tiếp cận & Tần suất), `PULSE` (Chiến dịch TikTok Pulse). ⏎ Nếu bạn đặt trường này là `PULSE`, chỉ có một ID vị trí (`location_id`) được trả về. ⏎ **Lưu ý**: • Không truyền trường này khi `objective_type` không phải là `RF_REACH`. • Bạn cần truyền giá trị `location_id` trả về sang `location_ids` khi dùng [/adgroup/rf/create/](57-reach-and-frequency.md#doc-1738235338194945) để tạo nhóm quảng cáo TikTok Pulse. |

### Danh sách giá trị cho `language`

| Value | Description |
|---|---|
| `af` | Afrikaans |
| `am` | Amharic |
| `ar` | Arabic |
| `az` | Azerbaijani |
| `be` | Belarusian |
| `bg` | Bulgarian |
| `bn` | Bengali |
| `bs` | Bosnian |
| `ca` | Catalan |
| `cs` | Czech |
| `da` | Danish |
| `de` | German |
| `el` | Greek |
| `en` | English |
| `es` | Spanish |
| `et` | Estonian |
| `eu` | Basque |
| `fa` | Farsi |
| `fi` | Finnish |
| `fil` | Filipino |
| `fr` | French |
| `gl` | Galician |
| `gu` | Gujarati |
| `hi` | Hindi |
| `hr` | Croatian |
| `hu` | Hungarian |
| `hy` | Armenian |
| `id` | Indonesian |
| `is` | Icelandic |
| `it` | Italian |
| `ja` | Japanese |
| `ka` | Georgian |
| `kk` | Kazakh |
| `km` | Khmer |
| `kn` | Kannada |
| `ko` | Korean |
| `ky` | Kyrgyz |
| `lo` | Lao |
| `lt` | Lithuanian |
| `lv` | Latvian |
| `mk` | Macedonian |
| `ml` | Malayalam |
| `mn` | Mongolian |
| `mr` | Marathi |
| `ms` | Malay |
| `my` | Burmese |
| `ne` | Nepali |
| `nl` | Dutch |
| `no` | Norwegian |
| `pa` | Punjabi |
| `pl` | Polish |
| `pt` | Portuguese |
| `pt-BR` | Portuguese (Brazil) |
| `ro` | Romanian |
| `ru` | Russian |
| `si` | Sinhalese |
| `sk` | Slovak |
| `sl` | Slovenian |
| `sq` | Albanian |
| `sr` | Serbian |
| `sv` | Swedish |
| `sw` | Swahili |
| `ta` | Tamil |
| `te` | Telugu |
| `th` | Thai |
| `tr` | Turkish |
| `uk` | Ukrainian |
| `ur` | Urdu |
| `uz` | Uzbek |
| `vi` | Vietnamese |
| `zh` | Chinese |
| `zh-CN` | Chinese (Simplified) |
| `zh-HK` | Chinese (Hong Kong) |
| `zh-TW` | Chinese (Traditional) |
| `zu` | Zulu |

### Ví dụ lệnh cURL (Example)
```HTTP
// cURL
curl --location -g --request GET 'https://business-api.tiktok.com/open_api/v1.3/tool/region/?advertiser_id={ADVERTISER_ID}}&placements=["PLACEMENT_TIKTOK"]&objective_type={{objective_type}}' \
--header 'Access-Token: xxxx' \
--header 'Content-Type: application/json' \
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Mã phản hồi. Để xem danh sách đầy đủ các mã phản hồi và mô tả, xem [Phụ lục - Mã trả về](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông điệp phản hồi. Để biết chi tiết, xem [Phụ lục - Mã trả về](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| data | object | Dữ liệu trả về. |
| ↳ region_list | string[] | Danh sách mã quốc gia hoặc khu vực |
| ↳ region_info | object[] | Thông tin về các vị trí khả dụng |
| ↳↳ location_id | string | Location ID |
| ↳↳ name | string | Tên vị trí địa lý. |
| ↳↳ parent_id | string | ID của vị trí cha. Trả về 0 nếu không có vị trí cha |
| ↳↳ region_code | string | Mã quốc gia hoặc khu vực. Ví dụ: "DE". |
| ↳↳ next_level_ids | string[] | Danh sách các vị trí con |
| ↳↳ area_type | string | Loại vị trí. Các giá trị enum hỗ trợ: `ADMIN`, `METROPOLITAN_OR_DMA`. |
| ↳↳ level | string | Cấp độ vị trí. Các giá trị enum hỗ trợ: `COUNTRY`(country or region level), `PROVINCE`, `CITY`(city or county level), `DISTRICT`(district or city level). DMA and metropolitans are at the province level. |
| ↳↳ support_below_18 | boolean | Liệu location supports ads to be delivered to people under 18 years of age. |
| request_id | string | ID nhật ký (log ID) của yêu cầu, dùng để định danh duy nhất cho yêu cầu. |

### Ví dụ lệnh cURL (Example)

```json
// JSON
{
    "code": 0,
    "message": "OK",
    "request_id": "2022070115265201024524610404180ECA",
    "data": {
        "region_info": [
            {
                "next_level_ids": [],
                "area_type": "ADMIN",
                "level": "COUNTRY",
                "region_code": "PE",
                "location_id": "3932488",
                "name": "Peru",
                "parent_id": "0",
                "support_below_18": true
            },
            {
                "next_level_ids": [
                    "662",
                    "525",
                    "532",
                    ...
                ],
                "area_type": "ADMIN",
                "level": "COUNTRY",
                "region_code": "US",
                "location_id": "6252001",
                "name": "United States",
                "parent_id": "0",
                "support_below_18": true
            },
            ...
        ],
        "region_list": [
            "PE",
            "US",
            "CL",
            "MX",
            "BY",
            "VN",
            ...
        ]
    }
}
```

---

<a id="doc-1773644763581441"></a>
<!-- doc_id: 1773644763581441 -->
<!-- doc_id: 1773644763581441 -->
# Lấy danh sách vị trí khả dụng theo ID tài khoản quảng cáo TikTok (Get available locations by advertiser ID)
> Đường dẫn: API Reference > Tools > Get available locations by ID tài khoản quảng cáo TikTok
Sử dụng endpoint này để lấy thông tin available locations that your ads can be delivered to **based on your advertiser IDs**.
Nếu muốn lấy các vị trí khả dụng mà quảng cáo của bạn có thể được phân phối dựa trên mục tiêu, vị trí đặt quảng cáo và tùy chọn hệ điều hành mục tiêu, cài đặt an toàn thương hiệu, hãy dùng endpoint **/tool/region/**.

## Yêu cầu gọi API (Request)

**Endpoint**  https://business-api.tiktok.com/open_api/v1.3/search/region/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**
| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
| advertiser_id ***(Bắt buộc)*** | string | ID tài khoản quảng cáo TikTok. |
| language | string | Ngôn ngữ bạn muốn dịch tên khu vực trả về. Giá trị mặc định: `en`<br>Hiện tại hỗ trợ: `zh`, `fr`, `es`, `ko`, `vi`, `en`, `hi`, `it`, `tr`, `ru`, `ja`, `id`, `de`, `ms`, `ar`, và `th`<br><p><span style="color:darkred"><b>Lưu ý</b></span>: Nếu bạn không truyền một trong các giá trị hỗ trợ trên, hệ thống sẽ trả về theo mặc định là `en`.</p>|

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/search/region/' \
--header 'Content-Type: application/json' \
--header 'Access-Token: {{Access-Token}}' \
--data-raw '{
    "advertiser_id": "{{advertiser_id}}",
    "language": "ja"
}'
```

## Dữ liệu phản hồi (Response)
| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
|code |number|Response code. For the complete list of response codes and descriptions, see [Appendix-Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message|string|Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|data|object|Dữ liệu trả về.|
#| region_list | object[] | Danh sách tất cả các khu vực khả dụng. |
##|region_id|string|Region ID.|
##|region_name|string|Region name. |
##|region_level|string|Region level. Các giá trị enum hỗ trợ: `COUNTRY`(country or region level), `PROVINCE`, `CITY`, `DISTRICT`. <br>DMA and metropolitans are at the province level.|
##|country_code|string|Country code for the country of the region.|
##| parent_id | string | ID khu vực cấp trên. Trường này sẽ không được trả về nếu `region_level` là `COUNTRY`. |
##|area_type|string|Loại vị trí. Các giá trị enum hỗ trợ: `ADMIN`, `METROPOLITAN_OR_DMA`.|
##|support_below_18|boolean|Liệu location supports ads to be delivered to people under 18 years of age.|
|request_id |string|ID nhật ký (log ID) của yêu cầu, dùng để định danh duy nhất cho yêu cầu.  |

### Ví dụ lệnh cURL (Example)
```http
// curl
HTTPS/1.1 200 OK
{
     "code": 0,
     "message": "OK",
     "request_id": "{{request_id}}",
     "data": {
        "region_list": [
             {
                "region_level": "COUNTRY",
                "support_below_18": true,
                "country_code": "US",
                "area_type": "ADMIN",
                "region_id": "6252001",
                "region_name": "アメリカ"
              },
              {
                 "region_level": "COUNTRY",
                 "support_below_18": true,
                 "country_code": "EC",
                 "area_type": "ADMIN",
                 "region_id": "3658394",
                 "region_name": "エクアドル"
              },
             {
                 "region_level": "COUNTRY",
                 "support_below_18": true,
                 "country_code": "QA",
                 "area_type": "ADMIN",
                 "region_id": "289688",
                 "region_name": "カタール"
            },
            …
        ]
    }
}
```

---

<a id="doc-1737188554152962"></a>
<!-- doc_id: 1737188554152962 -->
<!-- doc_id: 1737188554152962 -->
# Lấy danh sách ngôn ngữ (Get languages)
> Đường dẫn: API Reference > Tools > Get languages
Sử dụng endpoint này để lấy thông tin the enum values of language codes.

Sau khi lấy được mã ngôn ngữ, bạn có thể truyền chúng vào `languages` trong [/adgroup/create/](07-ad-groups-p2.md#doc-1739499616346114) để nhắm mục tiêu theo ngôn ngữ.

## Yêu cầu gọi API (Request)

**Endpoint**
https://business-api.tiktok.com/open_api/v1.3/tool/language/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id  ****(Bắt buộc)**** | string | ID tài khoản quảng cáo TikTok |

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --get -H "Access-Token:xxx" \
--data-urlencode "advertiser_id=ADVERTISER_ID" \
https://business-api.tiktok.com/open_api/v1.3/tool/language/
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Mã trạng thái phản hồi (0: Thành công). For the complete list of response codes and descriptions, see [Appendix-Return codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông điệp phản hồi từ máy chủ. Để biết chi tiết, xem [Appendix-Return codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| data | object | Dữ liệu trả về. |
| ↳ languages | object[] | Danh sách ngôn ngữ. |
| ↳↳ code | string | Mã ngôn ngữ. Bạn có thể truyền giá trị trường này vào `languages` trong [/adgroup/create/](07-ad-groups-p2.md#doc-1739499616346114) để nhắm mục tiêu ngôn ngữ. ⏎ Ví dụ: `en`. |
| ↳↳ name | string | Tên ngôn ngữ. ⏎ Ví dụ: `English`. |
| request_id | string | ID nhật ký (log ID) của yêu cầu, dùng để định danh duy nhất cho yêu cầu. |

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "20220630225329010245246039165DE9B4",
    "data": {
        "languages": [
            {
                "name": "Arabic",
                "code": "ar"
            },
            {
                "name": "Assamese",
                "code": "as"
            },
            {
                "name": "Haryanvi",
                "code": "bgc"
            },
            {
                "name": "Bihari",
                "code": "bh"
            },
            ...
        ]
    }
}
```

---

<a id="doc-1796638342793218"></a>
<!-- doc_id: 1796638342793218 -->
<!-- doc_id: 1796638342793218 -->
# Tìm kiếm hoặc liệt kê danh mục và hashtag nhắm mục tiêu sở thích, hành vi
> Đường dẫn: API Reference > Tools > Search for or list targeting categories and hashtags for interests and behaviors
Sử dụng endpoint này để tìm kiếm targeting categories and hashtags related to interests and behaviors based on seed keywords. You can also use it to list all available targeting categories and hashtags for interests and behaviors without specifying seed keywords.

<!-- ## Workflow Overview
Để tìm hiệu quả các danh mục nhắm mục tiêu hoặc hashtag phù hợp với trường hợp sử dụng của bạn, hãy làm theo quy trình trong sơ đồ sau:

-->

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/targeting/search/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
| advertiser_id ***(Bắt buộc)*** | string | ID tài khoản quảng cáo TikTok. |
| targeting_type ***(Bắt buộc)*** | string | Loại nhắm mục tiêu chính. <br><br>Giá trị enum: `INTEREST_AND_BEHAVIOR` (Sở thích & Hành vi). |
| sub_targeting_types **(Điều kiện)** | string[] | Bắt buộc khi `targeting_type` là `INTEREST_AND_BEHAVIOR` và nhiều từ khóa được truyền vào `search_keywords`. <br><br>Các loại nhắm mục tiêu phụ. <br><br>Các giá trị enum hỗ trợ: <ul><li>`GENERAL_INTEREST`: Sở thích chung.</li><li>`ADDITIONAL_INTEREST`: Sở thích bổ sung.</li><li>`PURCHASE_INTENTION`: Ý định mua hàng.</li><li>`VIDEO_INTERACTION`: Tương tác video.</li><li>`CREATOR_INTERACTION`: Tương tác với nhà sáng tạo.</li><li>`HASHTAG_INTERACTION`: Tương tác hashtag.</li></ul>|
| search_keywords | string[] | Danh sách các từ khóa hạt giống bạn cung cấp để tìm kiếm danh mục hoặc hashtag nhắm mục tiêu. <br><br>Kích thước tối đa: 10. Giới hạn độ dài mỗi từ khóa: 100 ký tự. <br><br>Nếu truyền nhiều từ khóa hạt giống vào trường này, hãy đảm bảo giá trị `sub_targeting_types` chỉ bao gồm `ADDITIONAL_INTEREST` và `HASHTAG_INTERACTION`. <br><br><p><span style="color:darkred"><b>Lưu ý</b></span>: Không hỗ trợ tìm kiếm gói hashtag (hashtag bundles). Do đó, nếu bao gồm `HASHTAG_INTERACTION` trong `sub_targeting_types` và truyền `search_keywords`, bạn chỉ có thể lấy các hashtag từ `search_result` trả về trong đối tượng `hashtag_interaction`.</p> |
| language | string | Ngôn ngữ của từ khóa hạt giống. <br><br>Giá trị mặc định: `en`. <br><br>Để xem các giá trị cho phép, xem Danh sách giá trị cho `language`. <br><br><p><span style="color:darkred"><b>Lưu ý</b></span>: Nếu bạn bao gồm `HASHTAG_INTERACTION` trong `sub_targeting_types` và truyền một hoặc nhiều từ khóa hạt giống không phải tiếng Anh vào `search_keywords`, hashtag thuộc nhiều ngôn ngữ có thể được trả về ngay cả khi bạn đã chỉ định `language`.</p> |
| filtering | object | Điều kiện lọc dữ liệu. |
#| special_industries | string[] | Danh mục quảng cáo đặc biệt. <br>Bằng cách chọn danh mục nhà ở, việc làm hoặc tín dụng, bạn cam kết không phân biệt đối xử và tuân thủ chính sách danh mục quảng cáo đặc biệt của TikTok. <br><br>Các giá trị enum hỗ trợ: <ul><li>`HOUSING`: Nhà ở.</li><li>`EMPLOYMENT`: Việc làm.</li><li>`CREDIT`: Tín dụng.</li></ul><br>Giá trị mặc định: `[]`. Mặc định không lọc theo danh mục đặc biệt. |

### Danh sách giá trị cho `language`

| Value | Description |
|---|---|
| `ar` | Arabic |
| `cs` | Czech |
| `de` | German |
| `en` | English |
| `es` | Spanish |
| `fr` | French |
| `id` | Indonesian |
| `it` | Italian |
| `ja` | Japanese |
| `ko` | Korean |
| `ms` | Malay |
| `pl` | Polish |
| `pt` | Portuguese |
| `ru` | Russian |
| `sv` | Swedish |
| `th` | Thai |
| `tr` | Turkish |
| `vi` | Vietnamese |
| `zh` | Chinese |

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location  --request GET 'https://business-api.tiktok.com/open_api/v1.3/targeting/search/?advertiser_id={{advertiser_id}}&targeting_type=INTEREST_AND_BEHAVIOR' \
--header 'Access-Token: {{Access-Token}}' \
```
## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|-|-|-|
|code |number|Response code. For the complete list of response codes and descriptions, see [Appendix-Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message|string|Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|request_id |string|ID nhật ký (log ID) của yêu cầu, dùng để định danh duy nhất cho yêu cầu.  |
|data |object|Dữ liệu trả về.|
#| general_interest | object | Danh sách các danh mục sở thích chung. |
##| list_result | object[] | Danh sách tất cả các danh mục sở thích chung khả dụng. <br><br>Nếu `search_keywords` được chỉ định và giá trị của `sub_targeting_types` bao gồm `GENERAL_INTEREST`, giá trị trường này sẽ là null. |
###| sub_targeting_type| string | Loại nhắm mục tiêu phụ. <br><br>Giá trị enum: `GENERAL_INTEREST` (Sở thích chung). |
###| id | string | ID của danh mục sở thích chung. <br><br>Bạn có thể truyền giá trị này vào `interest_category_ids` khi tạo nhóm quảng cáo bằng [/adgroup/create/](07-ad-groups-p2.md#doc-1739499616346114). |
###| name | string | Tên của danh mục sở thích chung. |
###|supported_special_industries | string[] | Các danh mục quảng cáo đặc biệt mà danh mục sở thích chung có thể kết hợp sử dụng cùng. <br><br>Các giá trị enum hỗ trợ: <ul><li>`HOUSING`: Nhà ở.</li><li>`EMPLOYMENT`: Việc làm.</li><li>`CREDIT`: Tín dụng.</li></ul> |
###| level | integer | Cấp độ phân tầng của danh mục sở thích chung. |
###|children_ids | string[] | Danh sách ID của các danh mục sở thích chung con trực thuộc danh mục hiện tại. |
###|hashtag_type | string | Loại hashtag. <br><br>Trường này luôn là null vì loại hashtag chỉ dùng trong kịch bản tương tác hashtag. |
##| search_result | map(string<>object[]) | Danh sách các danh mục sở thích chung được tạo dựa trên `search_keywords` đã chỉ định. <br><br><ul><li> Key: A seed keyword in the `search_keywords` of the request. <ul><li> Example: `"child"`.</li></ul></li><li> Value: An object array representing the generated general interest categories, following the structure of `list_result`.<ul><li> Example: `&#91;&#123;"sub_targeting_type": "GENERAL_INTEREST", "id": "10100","name": "Early Childhood & Preschool Education", "supported_special_industries": &#91;"HOUSING", "EMPLOYMENT", "CREDIT"&#93;"children_ids": null,"level": null, "hashtag_type": null&#125;&#93;`. </li></ul></li></ul> You can pass the value of id to `interest_category_ids` when creating an ad group using [/adgroup/create/](07-ad-groups-p2.md#doc-1739499616346114). |
#| additional_interest | object | Danh sách các danh mục sở thích bổ sung. <br><br>Nếu không truyền `search_keywords`, giá trị trường này sẽ là null. |
##| search_result | map(string<>object[]) | Danh sách các danh mục sở thích bổ sung được tạo dựa trên `search_keywords` đã chỉ định. <br><br><ul><li> Key: A seed keyword in the `search_keywords` of the request. <ul><li> Example: `"child"`.</li></ul></li><li> Value: An object array representing the generated additional interest categories, following the structure of `list_result` within the `general_interest` object. Note that the value of `sub_targeting_type` will always be `ADDITIONAL_INTEREST`.<ul><li> Example: `&#91;&#123;"sub_targeting_type": "ADDITIONAL_INTEREST", "id": "1915593069","name": "Childhood", "supported_special_industries": &#91;&#93;,"children_ids": null,"level": null, "hashtag_type": null&#125;&#93;`.</li></ul></li></ul>You can pass the value of id to `interest_keyword_ids` when creating an ad group using [/adgroup/create/](07-ad-groups-p2.md#doc-1739499616346114). |
#| purchase_intention | object | Danh sách các danh mục ý định mua hàng. |
##| list_result | object[] | Danh sách tất cả các danh mục ý định mua hàng khả dụng. <br><br>Nếu `search_keywords` được chỉ định và `sub_targeting_types` bao gồm `PURCHASE_INTENTION`, giá trị trường này sẽ là null. |
###| sub_targeting_type | string | Loại nhắm mục tiêu phụ. <br><br>Giá trị enum: `PURCHASE_INTENTION` (Ý định mua hàng). |
###| id | string | ID của danh mục ý định mua hàng. <br><br>Bạn có thể truyền giá trị này vào `purchase_intention_keyword_ids` khi tạo nhóm quảng cáo. |
###| name | string | Tên của danh mục ý định mua hàng. |
###|supported_special_industries | string[] | Các danh mục quảng cáo đặc biệt có thể kết hợp sử dụng cùng. <br><br>Các giá trị enum hỗ trợ: <ul><li>`HOUSING`: Nhà ở.</li><li>`EMPLOYMENT`: Việc làm.</li><li>`CREDIT`: Tín dụng.</li></ul> |
###| level | integer | Cấp độ phân tầng của danh mục ý định mua hàng. |
###| children_ids | string[] | Danh sách ID của các danh mục ý định mua hàng con trực thuộc. |
###| hashtag_type | string | Hashtag type. <br><br> This field will always be null because the hashtag type is for hashtag interactions scenarios only. |
##| search_result | map(string<>object[]) | Danh sách các danh mục ý định mua hàng được tạo dựa trên `search_keywords`. <br><br><ul><li> Key: A seed keyword in the `search_keywords` of the request.<ul><li> Example: `"child"`.</li></ul></li><li> Value: An object array representing the generated purchase intention categories, following the structure of `list_result`.<ul><li> Example: `&#91;&#123; "sub_targeting_type": "PURCHASE_INTENTION", "id": "12109","name": "Children's Apparel", "supported_special_industries": &#91;&#93;,"children_ids": null, "level": null, "hashtag_type": null&#125;&#93;`. </li></ul></li></ul>You can pass the value of id to `purchase_intention_keyword_ids` when creating an ad group using [/adgroup/create/](07-ad-groups-p2.md#doc-1739499616346114). |
#| video_interaction | object | Danh sách các danh mục tương tác video. |
##| list_result | object[] | Danh sách tất cả các danh mục tương tác video khả dụng. <br><br>Nếu `search_keywords` được chỉ định và `sub_targeting_types` bao gồm `VIDEO_INTERACTION`, giá trị trường này sẽ là null. |
###| sub_targeting_type| string | Loại nhắm mục tiêu phụ. <br><br>Giá trị enum: `VIDEO_INTERACTION` (Tương tác video). |
###| id | string | ID của danh mục tương tác video. <br><br>Bạn có thể truyền giá trị này vào `action_category_ids` khi tạo nhóm quảng cáo và đặt `action_scene` là `VIDEO_RELATED`. |
###| name | string | Tên của danh mục tương tác video. |
###|supported_special_industries | string[] | Các danh mục quảng cáo đặc biệt có thể kết hợp sử dụng cùng. <br><br>Các giá trị enum hỗ trợ: <ul><li>`HOUSING`: Nhà ở.</li><li>`EMPLOYMENT`: Việc làm.</li><li>`CREDIT`: Tín dụng.</li></ul> |
###| level | integer | Cấp độ của danh mục tương tác video. |
###| children_ids | string[] | Danh sách ID các danh mục tương tác video con. |
###| hashtag_type | string | Loại hashtag. <br><br>Trường này luôn là null vì loại hashtag chỉ dùng trong kịch bản tương tác hashtag. |
##| search_result | map(string<>object[]) | Danh sách các danh mục tương tác video được tạo dựa trên `search_keywords`. <br><br><ul> Key: A seed keyword in the `search_keywords` of the request. <li><ul><li> Example: `"fashion"`. </li></ul></li><li> Value: An object array representing the generated video interactions categories, following the structure of `list_result`. <ul><li> Example: `&#91;&#123;"sub_targeting_type": "VIDEO_INTERACTION", "id": "1612","name": "Other Fashion", "supported_special_industries": &#91;"HOUSING","EMPLOYMENT","CREDIT"&#93;,"children_ids": null,"level": null, "hashtag_type": null&#125;&#93;`. </li></ul></li></ul>You can pass the value of id to `action_category_ids` when creating an ad group using [/adgroup/create/](07-ad-groups-p2.md#doc-1739499616346114) and `action_scene` is set to `VIDEO_RELATED`. |
#| creator_interaction | object | Danh sách các danh mục tương tác với nhà sáng tạo. |
##| list_result | object[] | Danh sách tất cả các danh mục tương tác với nhà sáng tạo khả dụng. <br><br>Nếu `search_keywords` được chỉ định và `sub_targeting_types` bao gồm `CREATOR_INTERACTION`, giá trị trường này sẽ là null. |
###| sub_targeting_type | string | Loại nhắm mục tiêu phụ. <br><br>Giá trị enum: `CREATOR_INTERACTION` (Tương tác với nhà sáng tạo). |
###| id | string | ID của danh mục tương tác với nhà sáng tạo. <br><br>Bạn có thể truyền giá trị này vào `action_category_ids` khi tạo nhóm quảng cáo và đặt `action_scene` là `CREATOR_RELATED`. |
###| name | string | Tên của danh mục tương tác với nhà sáng tạo. |
###|supported_special_industries | string[] | Các danh mục quảng cáo đặc biệt có thể kết hợp sử dụng cùng. <br><br>Các giá trị enum hỗ trợ: <ul><li>`HOUSING`: Nhà ở.</li><li>`EMPLOYMENT`: Việc làm.</li><li>`CREDIT`: Tín dụng.</li></ul> |
###| level | integer | Cấp độ của danh mục tương tác với nhà sáng tạo. |
###| children_ids | string[] | Danh sách ID các danh mục tương tác với nhà sáng tạo con. |
###| hashtag_type | string | Loại hashtag. <br><br>Trường này luôn là null vì loại hashtag chỉ dùng trong kịch bản tương tác hashtag. |
##| search_result | map(string<>object[]) | Danh sách các danh mục tương tác với nhà sáng tạo được tạo dựa trên `search_keywords`. <br><br><ul><li> Key: A seed keyword in the `search_keywords` of the request.<ul><li> Example: `"fashion"`. </li></ul></li><li> Value: An object array representing the generated creator interactions categories, following the structure of `list_result`.<ul><li> Example: `&#91;&#123;"sub_targeting_type": "CREATOR_INTERACTION", "id": "10","name": "Fashion & Beauty", "supported_special_industries": &#91;"HOUSING","EMPLOYMENT","CREDIT"&#93;,"children_ids": null,"level": null, "hashtag_type": null&#125;&#93;`. </li></ul></li></ul>You can pass the value of id to `action_category_ids` when creating an ad group using [/adgroup/create/](07-ad-groups-p2.md#doc-1739499616346114) and `action_scene` is set to `CREATOR_RELATED`. |
#| hashtag_interaction | object | Danh sách các hashtag hoặc gói hashtag (hashtag bundles) liên quan đến tương tác hashtag.|
##| list_result | object[] | Danh sách tất cả các gói hashtag khả dụng. <br><br>Nếu `search_keywords` được chỉ định và `sub_targeting_types` bao gồm `HASHTAG_INTERACTION`, trường này sẽ là null. |
###| sub_targeting_type | string | Loại nhắm mục tiêu phụ. <br><br>Giá trị enum: `HASHTAG_INTERACTION` (Tương tác hashtag). |
###| id | string | ID của gói hashtag. <br><br>Bạn có thể truyền giá trị này vào `action_category_ids` khi tạo nhóm quảng cáo và đặt `action_scene` là `HASHTAG_RELATED`. |
###| name | string | Tên của gói hashtag. |
###|supported_special_industries | string[] | The special ad categories that the hashtag bundle can be used together with. <br><br>Các giá trị enum hỗ trợ: <ul><li> `HOUSING`: Ads for real estate listings, homeowners’ insurance, mortgage loans or other related opportunities.</li><li> `EMPLOYMENT`: Ads for job offers, internships, professional certification programs or other related opportunities.</li> <li>`CREDIT`: Ads for credit card offers, auto loans, long-term financing or other related opportunities. </li></ul> |
###| level | integer | Cấp độ của gói hashtag. |
###| children_ids| string[] | Danh sách ID các gói hashtag con. |
###| hashtag_type| string | Hashtag type. <br><br>Enum value: `HASHTAG_BUNDLE` (A pre-defined bundle of related hashtags focused on a common theme or event. For example, the "christmas" hashtag bundle can be used to target seasonal hashtags related to Christmas.) |
##| search_result | map(string<>object[]) | Danh sách các hashtag được tạo dựa trên `search_keywords` đã chỉ định.<br><br><ul><li> Key: A seed keyword in the `search_keywords` of the request.<ul><li> Example: `"child"`. </li></ul></li><li> Value: An object array representing the generated hashtags, following the structure of `list_result`. Note that the value of `hashtag_type` will always be `HASHTAG` (A standalone hashtag that can be used to target users interested in content associated with that specific hashtag).<ul><li> Example: `&#91;&#123;"sub_targeting_type": "HASHTAG_INTERACTION", "id": "67137517581","name": "#childbirtheducation", "supported_special_industries": &#91; &#93;,"children_ids": null,"level": null, "hashtag_type": "HASHTAG"&#125;&#93;,`.</li></ul></li></ul>You can pass the value of id to `action_category_ids` when creating an ad group using [/adgroup/create/](07-ad-groups-p2.md#doc-1739499616346114) and `action_scene` is set to `HASHTAG_RELATED`. |

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "video_interaction": {
            "list_result": [
                {
                    "id": "1311100",
                    "sub_targeting_type": "VIDEO_INTERACTION",
                    "name": "Scenery & Plants",
                    "children_ids": [],
                    "level": 3,
                    "supported_special_industries": [
                        "HOUSING",
                        "EMPLOYMENT",
                        "CREDIT"
                    ],
                    "hashtag_type": null
                },
                ...
                ],
            "search_result": null
        },
        "general_interest": {
            "list_result": [
                {
                    "id": "18110",
                    "sub_targeting_type": "GENERAL_INTEREST",
                    "name": "Cleaning Supplies",
                    "children_ids": [],
                    "level": 2,
                    "supported_special_industries": [],
                    "hashtag_type": null
                },
                ...
                ],
            "search_result": null
        },
        "creator_interaction": {
            "list_result": [
                {
                    "id": "11",
                    "sub_targeting_type": "CREATOR_INTERACTION",
                    "name": "DIY & Life Hacks",
                    "children_ids": [
                        "11001"
                    ],
                    "level": 1,
                    "supported_special_industries": [
                        "HOUSING",
                        "EMPLOYMENT",
                        "CREDIT"
                    ],
                    "hashtag_type": null
                },
                ...
                ],
            "search_result": null
        },
        "hashtag_interaction": {
            "list_result": [
                {
                    "id": "11",
                    "sub_targeting_type": "HASHTAG_INTERACTION",
                    "name": "cybermonday",
                    "children_ids": [],
                    "level": 1,
                    "supported_special_industries": [],
                    "hashtag_type": "HASHTAG_BUNDLE"
                },
                ...
                ],
            "search_result": null
        },
        "purchase_intention": {
            "list_result": [
                {
                    "id": "26101",
                    "sub_targeting_type": "PURCHASE_INTENTION",
                    "name": "Photography",
                    "children_ids": [],
                    "level": 2,
                    "supported_special_industries": [
                        "HOUSING",
                        "EMPLOYMENT",
                        "CREDIT"
                    ],
                    "hashtag_type": null
                },
                ...
                ],
            "search_result": null
        },
        "additional_interest": null
    },
    "code": 0
}
```

---

<a id="doc-1737174348712961"></a>
<!-- doc_id: 1737174348712961 -->
<!-- doc_id: 1737174348712961 -->
# Lấy danh mục sở thích chung (Get general interest categories)
> Đường dẫn: API Reference > Tools > Get general interest categories
Sử dụng endpoint này để lấy thông tin general interest category enumeration values.

> **Note:** 
> We recommend that you use the Consolidated Interest and Behavior API ([/targeting/search/](70-tools-p1.md#doc-1796638342793218)) to search for or list targeting categories and hashtags for interests and behaviors. This API provides a consolidated and efficient approach to access the necessary targeting information.

## Yêu cầu gọi API (Request)

**Endpoint**
https://business-api.tiktok.com/open_api/v1.3/tool/interest_category/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id  ****(Bắt buộc)**** | string | ID tài khoản quảng cáo TikTok. |
| version | number | Phiên bản của danh mục sở thích. ⏎ Các giá trị enum hỗ trợ: `1` (`interest_category`), `2` (`interest_category_v2`). Mặc định: `2`. |
| language | string | Ngôn ngữ của tên danh mục trong phản hồi. ⏎ Giá trị mặc định: `en`. ⏎ Các ngôn ngữ hỗ trợ: `en`, `zh`, `ja`, `de`, `es`, `fr`, `id`, `it`, `ko`, `ru`, `th`, `tr`, `vi`, `ar`, `pt`, `ms`. ⏎ Để biết chi tiết, xem [Phụ lục - Mã ngôn ngữ](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| placements | string[] | Các ứng dụng nơi bạn muốn phân phối quảng cáo. Để xem danh sách giá trị enum, xem [Enumeration - Placement](../15-appendix/phu-luc-p1.md#doc-1737174886619138). ⏎ Các danh mục sở thích khả dụng có thể khác nhau tùy vị trí hiển thị, và trường này chỉ có hiệu lực khi `version` = `2`. |
| special_industries | string[] | Danh mục quảng cáo đặc biệt. ⏎ Các giá trị enum hỗ trợ: • `HOUSING`: Ads for real estate listings, homeowners insurance, mortgage loans or other related opportunities. • `EMPLOYMENT`: Ads for job offers, internship, professional certification programs or other related opportunities. • `CREDIT`: Ads for credit card offers, auto loans, long-term financing or other related opportunities. ⏎ **Note**: This field is generally available to advertisers registered in America or Canada. Advertisers who are not registered in America or Canada but want to target these countries with special ad categories need to apply for an additional allowlist. |

### Ví dụ lệnh cURL (Example)

```http
// curl
curl --get -H "Access-Token:xxx" \
--data-urlencode "advertiser_id=ADVERTISER_ID" \
--data-urlencode "version=VERSION" \
https://business-api.tiktok.com/open_api/v1.3/tool/interest_category/
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Mã trạng thái phản hồi (0: Thành công). For the complete list of response codes and descriptions, see [Appendix-Return codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông điệp phản hồi từ máy chủ. Để biết chi tiết, xem [Appendix-Return codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| data | object | Return Data |
| ↳ interest_categories | object[] | Danh sách danh mục sở thích. ⏎ To determine the corresponding names for gaming-related interest category IDs, see [Interest category](../15-appendix/phu-luc-p1.md#doc-1738865030529025). |
| ↳↳ interest_category_id | string | ID danh mục sở thích. |
| ↳↳ interest_category_name | string | Tên danh mục sở thích. |
| ↳↳ level | number | Level |
| ↳↳ sub_category_ids | string[] | Subcategory ID list |
| ↳↳ special_industries | string[] | Danh mục quảng cáo đặc biệt. ⏎ Các giá trị enum hỗ trợ: • `HOUSING`: Nhà ở. • `EMPLOYMENT`: Việc làm. • `CREDIT`: Tín dụng. ⏎ **Lưu ý**: • Nếu giá trị trả về rỗng (`[]`), danh mục sở thích không hỗ trợ danh mục quảng cáo đặc biệt nào. |
| ↳↳ placements | string[] | Vị trí hiển thị khả dụng cho danh mục sở thích này. Danh sách trống nghĩa là không giới hạn vị trí. Xem [Phụ lục - Vị trí hiển thị](../15-appendix/phu-luc-p1.md#doc-1737174886619138) để biết chi tiết giá trị enum. |
| request_id | string | ID nhật ký (log ID) của yêu cầu, dùng để định danh duy nhất cho yêu cầu. |

### Ví dụ lệnh cURL (Example)

```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "202206302233010102452460660B5E36E5",
    "data": {
        "interest_categories": [
            {
                "special_industries": [
                    "HOUSING",
                    "EMPLOYMENT",
                    "CREDIT"
                ],
                "placements": [],
                "interest_category_id": "10",
                "level": 1,
                "interest_category_name": "Education",
                "sub_category_ids": [
                    "10100",
                    "10101",
                    "10102",
                    "10103",
                    "10104",
                    "10105",
                    "10106"
                ]
            },
            {
                "special_industries": [
                    "HOUSING",
                    "EMPLOYMENT",
                    "CREDIT"
                ],
                "placements": [],
                "interest_category_id": "11",
                "level": 1,
                "interest_category_name": "Vehicles & Transportation",
                "sub_category_ids": [
                    "11100",
                    "11101",
                    "11102",
                    "11103",
                    "11104",
                    "11105",
                    "11106",
                    "11107",
                    "11108",
                    "11109",
                    "11111",
                    "11112"
                ]
            },
            ...
        ]
    }
}
```

---

<a id="doc-1737180852720642"></a>
<!-- doc_id: 1737180852720642 -->
<!-- doc_id: 1737180852720642 -->
# Lấy danh mục sở thích bổ sung (Get additional interest categories)
> Đường dẫn: API Reference > Tools > Get additional interest categories
Dùng nhóm endpoint này để lấy các danh mục sở thích bổ sung (từ khóa sở thích). Lưu ý chỉ các danh mục sở thích bổ sung còn hiệu lực (`status` = `EFFECTIVE`) mới có thể dùng trong nhóm quảng cáo để nhắm mục tiêu đối tượng.

- If you want to search for additional interest categories based on seed keywords, see **/tool/interest_keyword/recommend/**. 
- If you want to use IDs to get additional interest categories, see **/tool/interest_keyword/get/**. 

> **Important:** Please use the keyword tool responsibly. You are responsible for your targeting decisions, including their legal compliance.

---

<a id="doc-1763590884474882"></a>
<!-- doc_id: 1763590884474882 -->
<!-- doc_id: 1763590884474882 -->
# Tìm kiếm danh mục sở thích bổ sung (Search for additional interest categories)
> Đường dẫn: API Reference > Tools > Get additional interest categories > Search for additional interest categories
Sử dụng endpoint này để tìm kiếm additional interest categories. You need to specify one or more seed keywords and the seed keyword or keywords will be used to search for related additional interest categories. 

Các danh mục sở thích bổ sung trả về (`keyword_id`) có `status` là `EFFECTIVE` có thể được truyền vào trường `interest_keyword_ids` khi gọi [/adgroup/create/](07-ad-groups-p2.md#doc-1739499616346114). Khi đó các danh mục sở thích bổ sung sẽ được dùng trong nhóm quảng cáo để nhắm mục tiêu đối tượng.

> **Note:** 
> We recommend that you use the Consolidated Interest and Behavior API ([/targeting/search/](70-tools-p1.md#doc-1796638342793218)) to search for or list targeting categories and hashtags for interests and behaviors. This API provides a consolidated and efficient approach to access the necessary targeting information.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/tool/interest_keyword/recommend/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id  ****(Bắt buộc)**** | string | ID tài khoản quảng cáo TikTok. |
| keywords **(Điều kiện)** | string[] | • Bắt buộc phải chỉ định `keywords` hoặc `keyword`. • Nếu truyền đồng thời cả hai, `keyword` sẽ bị bỏ qua. ⏎ Danh sách các từ khóa gốc do bạn cung cấp để tìm kiếm các danh mục sở thích bổ sung. ⏎ Mỗi từ khóa gốc sẽ được sử dụng độc lập để tạo ra các danh mục sở thích bổ sung tương ứng. ⏎ Kích thước tối đa: 10. |
| keyword **(Điều kiện)** | string | • Bắt buộc phải chỉ định `keywords` hoặc `keyword`. • Nếu truyền đồng thời cả hai, `keyword` sẽ bị bỏ qua. ⏎ Một từ khóa gốc do bạn cung cấp để tìm kiếm danh mục sở thích bổ sung. |
| mode | string | Chế độ tìm kiếm. ⏎ Các giá trị enum hỗ trợ: `FUZZ_MATCH`, `SEMANTIC_RECOMMEND`. ⏎ Giá trị mặc định: `FUZZ_MATCH`. |
| language | string | Ngôn ngữ từ khóa. ⏎ Các giá trị enum hỗ trợ: `fr`, `id`, `it`, `ja`, `ms`, `ar`, `vi`, `en`, `ru`, `es`, `th`, `tr`, `hi`, `zh`, `de`, `ko`. ⏎ Giá trị mặc định: `en`. ⏎ Lưu ý rằng ngôn ngữ đối tượng mục tiêu không bị giới hạn bởi ngôn ngữ từ khóa. Bạn có thể dùng các danh mục tiếng Anh để nhắm đối tượng không nói tiếng Anh. |
| limit | number | Số lượng danh mục sở thích bổ sung bạn muốn lấy. ⏎ Giá trị mặc định: 50. ⏎ Value range: 1-50. |
| audience_type | string | Loại đối tượng. ⏎ Các giá trị enum hỗ trợ: • `GENERAL_INTEREST`: Sở thích chung. Khán giả có mối quan tâm chung, dài hạn đối với danh mục video. • `PURCHASE_INTENTION` (đã ngừng sử dụng): Ý định mua hàng. Hành vi gần đây gợi ý họ có thể mua sản phẩm liên quan. ⏎ Giá trị mặc định: `GENERAL_INTEREST`. |

### Ví dụ lệnh cURL (Example)
```HTTP
// cURL
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/tool/interest_keyword/recommend/' \
--header 'Access-Token: xxxx' \
--header 'Content-Type: application/json' \
--data-raw '{
    "advertiser_id": "1234567886354716677",
    "keyword": "test",
}'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem đầy đủ danh sách mã lỗi và mô tả tại [Phụ lục - Mã lỗi trả về](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông điệp phản hồi từ hệ thống. Xem chi tiết tại [Phụ lục - Mã lỗi trả về](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | ID nhật ký (log ID) của yêu cầu, dùng để định danh duy nhất cho yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ recommended_keywords | object[] | Danh sách các danh mục sở thích bổ sung. |
| ↳↳ input_keyword | string | Chỉ trả về khi `keywords` được bao gồm trong yêu cầu và chứa nhiều hơn một từ khóa. ⏎ Từ khóa hạt giống cụ thể mà danh mục sở thích bổ sung được tạo ra cho nó. ⏎ Ví dụ: nếu danh mục "Tester" được tạo cho từ khóa hạt giống "test", `input_keyword` trả về sẽ là `"test"` và `keyword` là `"Tester"`. |
| ↳↳ keyword | string | Danh mục sở thích bổ sung. |
| ↳↳ keyword_id | string | ID of the additional interest category. |
| ↳↳ language | string | Ngôn ngữ của danh mục sở thích bổ sung. ⏎ Các giá trị enum hỗ trợ: `fr`, `id`, `it`, `ja`, `ms`, `ar`, `vi`, `en`, `ru`, `es`, `th`, `tr`, `hi`, `zh`, `de`, `ko`. |
| ↳↳ status | string | Liệu additional interest category will be effective. ⏎ Các giá trị enum hỗ trợ: •  `EFFECTIVE`: effective. An additional interest category is effective if using it can reach a reasonable number of people.  • `INEFFECTIVE`: ineffective. An additional interest category is ineffective if the estimated audience size is too small. ⏎ **Note**: Only effective additional interest categories can be used in ad groups to target audiences. |

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "202207011538040102452421060C18B592",
    "data": {
        "recommended_keywords": [
            {
                "status": "EFFECTIVE",
                "language": "1",
                "keyword": "Testament",
                "keyword_id": "1915651459"
            },
            {
                "status": "EFFECTIVE",
                "language": "1",
                "keyword": "Tester",
                "keyword_id": "1916254642"
            },
            {
                "status": "EFFECTIVE",
                "language": "1",
                "keyword": "Brain test",
                "keyword_id": "2027741302"
            },
            {
                "status": "EFFECTIVE",
                "language": "1",
                "keyword": "Test",
                "keyword_id": "2027749623"
            },
            {
                "status": "EFFECTIVE",
                "language": "1",
                "keyword": "Test drive",
                "keyword_id": "2027768725"
            },
            ...
        ]
    }
}
```

---

<a id="doc-1763590894544897"></a>
<!-- doc_id: 1763590894544897 -->
<!-- doc_id: 1763590894544897 -->
# Lấy danh mục sở thích bổ sung theo ID (Get additional interest categories by ID)
> Đường dẫn: API Reference > Tools > Get additional interest categories > Get additional interest categories by ID
Sử dụng endpoint này để lấy thông tin additional interest categories by ID.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/tool/interest_keyword/get/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id  ****(Bắt buộc)**** | string | ID tài khoản quảng cáo TikTok. |
| keyword_query | object[] | Thông tin danh mục sở thích bổ sung bạn muốn lấy. ⏎ Max size = 50. |
| ↳ keyword_id  ****(Bắt buộc)**** | string | ID danh mục sở thích bổ sung. |
| ↳ language | string | Ngôn ngữ danh mục sở thích bổ sung. Giá trị mặc định: `en`. ⏎ Supported languages: `fr`, `id`, `it`, `ja`, `ms`, `ar`, `vi`, `en`, `ru`, `es`, `th`, `tr`, `hi`, `zh`, `de`, `ko`. |
| filtering | object | Điều kiện lọc dữ liệu. |
| ↳ audience_type | string | Loại đối tượng bạn muốn lọc. Các giá trị enum hỗ trợ: • `GENERAL_INTEREST`: Sở thích chung. • `PURCHASE_INTENTION`: Ý định mua hàng. Giá trị mặc định: `GENERAL_INTEREST`. |

### Ví dụ lệnh cURL (Example)
```curl
// http
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/tool/interest_keyword/get/?advertiser_id= {{ADVERTISER_ID}}&keyword_query=[{"keyword_id": "{{keyword_id}}"}]' \
--header 'Access-Token: {{Access-Token}}' \
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Mã phản hồi từ API. Giá trị `0` biểu thị thành công. Xem đầy đủ danh sách mã lỗi và mô tả tại [Phụ lục - Mã lỗi trả về](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông điệp phản hồi từ hệ thống. Xem chi tiết tại [Phụ lục - Mã lỗi trả về](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | ID nhật ký (log ID) của yêu cầu, dùng để định danh duy nhất cho yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ keywords | object[] | Danh sách các danh mục sở thích bổ sung. |
| ↳↳ keyword | string | Danh mục sở thích bổ sung. |
| ↳↳ keyword_id | string | ID danh mục sở thích bổ sung. |
| ↳↳ status | string | Liệu an additional interest category will be effective. ⏎ Các giá trị enum hỗ trợ: `EFFECTIVE`, `INEFFECTIVE`. ⏎ An additional interest category is effective if using it can reach a reasonable number of people. ⏎ An additional interest category is ineffective if the projected audience size is too small. ⏎ **Note**: Only effective additional interest categories can be used in ad groups to target audiences. |

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "2021081206012901024503714416ABA90A",
    "data": {
        "keywords": [
            {
                "keyword_id": "2027755677",
                "status": "EFFECTIVE",
                "keyword": "movie app"
            }
        ]
    }
}
```

---

<a id="doc-1737166752522241"></a>
<!-- doc_id: 1737166752522241 -->
<!-- doc_id: 1737166752522241 -->
# Lấy danh mục hành động (Get action categories)
> Đường dẫn: API Reference > Tools > Get action categories
Sử dụng endpoint này để lấy thông tin action category enumeration values. Action categories are also referred to as behavioral categories in our documentation.

Nhắm mục tiêu theo hành động giúp nhà quảng cáo phân phối quảng cáo phù hợp tới người dùng dựa trên hành vi gần đây trong ứng dụng. Hành vi trong ứng dụng gồm hai loại: hành động liên quan đến video (xem, thích, bình luận hoặc chia sẻ) và hành động liên quan đến nhà sáng tạo (theo dõi hoặc xem trang chủ). Do đó, `action_scene` mà nhà phát triển có thể dùng danh mục hành động khi gọi [/adgroup/create/](07-ad-groups-p2.md#doc-1739499616346114) là `CREATOR_RELATED` hoặc `VIDEO_RELATED`.

> **Note:** 
> We recommend that you use the Consolidated Interest and Behavior API ([/targeting/search/](70-tools-p1.md#doc-1796638342793218)) to search for or list targeting categories and hashtags for interests and behaviors. This API provides a consolidated and efficient approach to access the necessary targeting information.

## Yêu cầu gọi API (Request)

**Endpoint**

https://business-api.tiktok.com/open_api/v1.3/tool/action_category/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id  ****(Bắt buộc)**** | string | ID tài khoản quảng cáo TikTok. |
| special_industries | string[] | Danh mục quảng cáo đặc biệt. ⏎ Các giá trị enum hỗ trợ: • `HOUSING`: Ads for real estate listings, homeowners insurance, mortgage loans or other related opportunities. • `EMPLOYMENT`: Ads for job offers, internship, professional certification programs or other related opportunities. • `CREDIT`: Ads for credit card offers, auto loans, long-term financing or other related opportunities. ⏎ **Note**: This field is generally available to advertisers registered in America or Canada. Advertisers who are not registered in America or Canada but want to target these countries with special ad categories need to apply for an additional allowlist. |
| language | string | Ngôn ngữ của tên danh mục trong phản hồi. Giá trị mặc định: `en`. ⏎ Các ngôn ngữ hỗ trợ: `en`, `zh`, `ja`, `de`, `es`, `fr`, `id`, `it`, `ko`, `ru`, `th`, `tr`, `vi`, `ar`, `pt`, `ms`. ⏎ Để biết chi tiết, xem [Phụ lục - Mã ngôn ngữ](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |

### Ví dụ lệnh cURL (Example)

```http
// curl
curl --get -H "Access-Token:xxx" \
--data-urlencode "advertiser_id=ADVERTISER_ID" \
https://business-api.tiktok.com/open_api/v1.3/tool/action_category/
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Mã trạng thái phản hồi (0: Thành công). For the complete list of response codes and descriptions, see [Appendix-Return codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông điệp phản hồi từ máy chủ. Để biết chi tiết, xem [Appendix-Return codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| data | object | Dữ liệu trả về. |
| ↳ action_categories | object[] | Action Categories list. |
| ↳↳ description | string | Mô tả hành động. |
| ↳↳ action_category_id | string | ID danh mục hành động. |
| ↳↳ level | number | Level. |
| ↳↳ sub_category_ids | string[] | Subcategory ID list. |
| ↳↳ name | string | Tên danh mục hành động. |
| ↳↳ special_industries | string[] | Danh mục quảng cáo đặc biệt. ⏎ Các giá trị enum hỗ trợ: • `HOUSING`(Ads for real estate listings, homeowners insurance, mortgage loans or other related opportunities.) • `EMPLOYMENT`(Ads for job offers, internship, professional certification programs or other related opportunities.) • `CREDIT`(Ads for credit card offers, auto loans, long-term financing or other related opportunities.) ⏎ **Note**: •  If the returned value is empty(`[]`), it means that the action categories do not support any special ad categories. |
| ↳↳ action_scene | string | Phạm vi hành động (Action scene). Các giá trị enum hỗ trợ: `CREATOR_RELATED`, `VIDEO_RELATED`. |
| request_id | string | ID nhật ký (log ID) của yêu cầu, dùng để định danh duy nhất cho yêu cầu. |

### Ví dụ lệnh cURL (Example)

```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "20220630215533010245242106175C5C29",
    "data": {
        "action_categories": [
            {
                "description": "TikTok users who have followed comedy creators.",
                "sub_category_ids": [
                    "1001"
                ],
                "special_industries": [
                    "HOUSING",
                    "EMPLOYMENT",
                    "CREDIT"
                ],
                "action_scene": "CREATOR_RELATED",
                "level": 1,
                "name": "Comedy",
                "action_category_id": "1"
            },
            {
                "description": "TikTok users who have followed creators that post original performance or original narration content.",
                "sub_category_ids": [
                    "2001"
                ],
                "special_industries": [
                    "HOUSING",
                    "EMPLOYMENT",
                    "CREDIT"
                ],
                "action_scene": "CREATOR_RELATED",
                "level": 1,
                "name": "Drama",
                "action_category_id": "2"
            },
            ...
      ]
  }
}
```

---

<a id="doc-1736271339521025"></a>
<!-- doc_id: 1736271339521025 -->
<!-- doc_id: 1736271339521025 -->
# Tìm kiếm hashtag nhắm mục tiêu (Search for targeting hashtags)
> Đường dẫn: API Reference > Tools > Search for targeting hashtags
Sử dụng endpoint này để tìm kiếm targeting hashtags based on seed keywords. 

The returned hashtag (`keyword_id`) can be passed on to the `action_category_ids` field in [/adgroup/create/](07-ad-groups-p2.md#doc-1739499616346114) to target users who watched TikTok videos with the hashtag. You need to set `action_scene` to `HASHTAG_RELATED` simultaneously.

> **Note:** 
> We recommend that you use the Consolidated Interest and Behavior API ([/targeting/search/](70-tools-p1.md#doc-1796638342793218)) to search for or list targeting categories and hashtags for interests and behaviors. This API provides a consolidated and efficient approach to access the necessary targeting information.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/tool/hashtag/recommend/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id  ****(Bắt buộc)**** | string | ID tài khoản quảng cáo TikTok. |
| keywords ****(Bắt buộc)**** | string[] | Từ khóa bạn muốn nhận hashtag đề xuất. ⏎ Nếu bạn chỉ định nhiều từ khóa không liên quan và đặt toán tử là `AND`, có thể không có hashtag nào được trả về. ⏎ Kích thước tối đa: 10. |
| operator | string | Toán tử điều kiện được sử dụng giữa các từ khóa. ⏎ Các giá trị enum hỗ trợ: • `AND`: Hashtag đề xuất sẽ được tạo dựa trên tất cả các từ khóa trong `keywords`. • `OR`: Hashtag đề xuất sẽ được tạo riêng cho từng từ khóa trong `keywords`. ⏎ Giá trị mặc định: `AND`. |

### Ví dụ lệnh cURL (Example)

```http
// curl
curl --location -g --request GET 'https://business-api.tiktok.com/open_api/v1.3/tool/hashtag/recommend/?keywords=[%22game%22]&advertiser_id=1234' \
--header 'Access-Token: xxxx' \
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Response code. For the complete list of error codes and descriptions, see [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | ID nhật ký (log ID) của yêu cầu, dùng để định danh duy nhất cho yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ recommend_keywords | object[] | Hashtag được đề xuất. |
| ↳↳ input_keyword | string | Chỉ trả về khi toán tử điều kiện được đặt là `OR` và có nhiều hơn 1 từ khóa trong yêu cầu. ⏎ Từ khóa cụ thể mà hashtag đề xuất được tạo ra. ⏎ Ví dụ: nếu "#gametime" được đề xuất cho "game", `input_keyword` sẽ là `"game"` và `keyword` là `"#gametime"`. |
| ↳↳ keyword | string | Hashtag được đề xuất. |
| ↳↳ keyword_id | string | ID từ khóa hashtag. ⏎ Có thể truyền vào trường `action_category_ids` khi tạo nhóm quảng cáo bằng [/adgroup/create/](07-ad-groups-p2.md#doc-1739499616346114) và đặt `action_scene` là `HASHTAG_RELATED`. |
| ↳↳ keyword_status | string | Trạng thái từ khóa. ⏎ Các giá trị enum hỗ trợ: `ONLINE` (available for use), `OFFLINE` (not available for use). |

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "1234",
    "data": {
        "recommend_keywords": [
              {
                "keyword": "#gameroom",
                "keyword_id": "3568527772311",
                "keyword_status": "ONLINE"
            },
            {
                "keyword": "#gametime",
                "keyword_id": "3391154394694",
                "keyword_status": "ONLINE"
            }
        ]
    }
}
```

---

<a id="doc-1736280889167874"></a>
<!-- doc_id: 1736280889167874 -->
<!-- doc_id: 1736280889167874 -->
# Lấy hashtag nhắm mục tiêu theo ID (Get targeting hashtags by ID)
> Đường dẫn: API Reference > Tools > Get targeting hashtags by ID
Sử dụng endpoint này để lấy thông tin the targeting hashtag names and statuses by ID. 

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/tool/hashtag/get/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id  ****(Bắt buộc)**** | string | ID tài khoản quảng cáo TikTok |
| keyword_ids ****(Bắt buộc)**** | string[] | Danh sách ID từ khóa |

### Ví dụ lệnh cURL (Example)

```http
// curl
curl --location -g --request GET 'https://business-api.tiktok.com/open_api/v1.3/tool/hashtag/get/?keyword_ids=["3158447993006"]&advertiser_id=1234' \
--header 'Access-Token: 1234' \
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Response code. For the complete list of error codes and descriptions, see [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | ID nhật ký (log ID) của yêu cầu, dùng để định danh duy nhất cho yêu cầu. |
| data | object | Dữ liệu trả về |
| ↳ keywords_status | object[] | Thông tin từ khóa. |
| ↳↳ keyword | string | Keyword |
| ↳↳ keyword_id | string | Keyword ID |
| ↳↳ keyword_status | string | Enum: `ONLINE` (available for use), `OFFLINE` (not available for use) |

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "1234",
    "data": {
        "keywords_status": [
            {
                "keyword": "#musicchallenge",
                "keyword_id": "2911052068069",
                "keyword_status": "ONLINE"
            }
        ]
    }
}
```

---

<a id="doc-1736275204260866"></a>
<!-- doc_id: 1736275204260866 -->
<!-- doc_id: 1736275204260866 -->
# Lấy danh mục sở thích và hành động được đề xuất (Get recommended interest and action categories)
> Đường dẫn: API Reference > Tools > Get recommended interest and action categories
Sử dụng endpoint này để lấy thông tin recommended interest and action categories based on historical performance data in the same industries.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/tool/targeting_category/recommend/

**Method** POST

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| Content-Type ****(Bắt buộc)**** | string | Loại nội dung của yêu cầu. Giá trị cho phép: `"application/json"` |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id  ****(Bắt buộc)**** | string | ID tài khoản quảng cáo TikTok. |
| region_codes ****(Bắt buộc)**** | string[] | Danh sách mã quốc gia hoặc khu vực. Ví dụ: `["US", "JP", "KR"]` |
| app_id | string | ID của ứng dụng di động bạn muốn quảng bá. Trường này là tùy chọn và chỉ hợp lệ nếu bạn muốn quảng bá ứng dụng di động. |

### Ví dụ lệnh cURL (Example)

```http
// curl
curl -H "Access-Token:xxx" -H "Content-Type:application/json" -X POST \
-d '{
    "advertiser_id": "ADVERTISER_ID",
    "region_code": [
        "REGION_CODE"
    ],
    "app_id": "APP_ID"
}' \
https://business-api.tiktok.com/open_api/v1.3/tool/targeting_category/recommend/
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Response code. For the complete list of error codes and descriptions, see [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | ID nhật ký (log ID) của yêu cầu, dùng để định danh duy nhất cho yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ interest_categories | object[] | Danh mục sở thích được đề xuất. |
| ↳↳ interest_category_id | string | ID danh mục sở thích.. It can used as one of the targeting settings when creating an ad group. |
| ↳↳ interest_category_name | string | Tên danh mục sở thích.. |
| ↳↳ placements | string[] | Danh sách vị trí hiển thị mà danh mục sở thích có thể áp dụng. Nếu để trống, có nghĩa là danh mục có thể áp dụng cho tất cả các vị trí. |
| ↳↳ special_industries | string[] | Ad categories. Các giá trị enum hỗ trợ: • `HOUSING`: Ads for real estate listings, homeowners insurance, mortgage loans or other related opportunities. • `EMPLOYMENT`: Ads for job offers, internship, professional certification programs or other related opportunities. • `CREDIT`: Ads for credit card offers, auto loans, long-term financing or other related opportunities. ⏎ **Note**:  • If the returned value is empty(`[]`), it means that the interest categories do not support any industry types. • This field is only supported for advertisers who are registered in America or Canada. |
| ↳ action_categories | object[] | Danh mục hành động được đề xuất. |
| ↳↳ action_category_id | string | ID danh mục hành động. Có thể sử dụng làm một trong các cài đặt nhắm mục tiêu khi tạo nhóm quảng cáo. |
| ↳↳ action_category_name | string | Tên danh mục hành động. |
| ↳↳ description | string | Mô tả danh mục hành động. |
| ↳↳ scene | string | Phạm vi danh mục hành động. Các giá trị enum hỗ trợ: `CREATOR_RELATED`, `VIDEO_RELATED`. |
| ↳↳ special_industries | string[] | Ad categories. Các giá trị enum hỗ trợ: • `HOUSING`: Ads for real estate listings, homeowners insurance, mortgage loans or other related opportunities. • `EMPLOYMENT`: Ads for job offers, internship, professional certification programs or other related opportunities. • `CREDIT`: Ads for credit card offers, auto loans, long-term financing or other related opportunities. ⏎ **Note**:  • If the returned value is empty(`[]`), it means that the interest categories do not support any industry types. • This field is only supported for advertisers who are registered in America or Canada. |

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "20220614231448010245246039155606FD",
    "data": {
        "interest_categories": [
            {
                "interest_category_id": "11",
                "special_industries": [
                    "HOUSING",
                    "EMPLOYMENT",
                    "CREDIT"
                ],
                "placements": [],
                "interest_category_name": "Vehicles & Transportation"
            },
            {
                "interest_category_id": "20",
                "special_industries": [
                    "HOUSING",
                    "EMPLOYMENT",
                    "CREDIT"
                ],
                "placements": [],
                "interest_category_name": "Apps"
            },
            {
                "interest_category_id": "23117104",
                "special_industries": [],
                "placement": [
                    "PLACEMENT_TIKTOK",
                    "PLACEMENT_PANGLE"
                ],
                "interest_category_name": "Talk Shows"
            },
            {
                "interest_category_id": "20105",
                "special_industries": [
                    "HOUSING",
                    "EMPLOYMENT",
                    "CREDIT"
                ],
                "placement": [],
                "interest_category_name": "Online Shopping"
            },
            {
                "interest_category_id": "10",
                "special_industries": [
                    "HOUSING",
                    "EMPLOYMENT",
                    "CREDIT"
                ],
                "placement": [],
                "interest_category_name": "Education"
            },
            {
                "interest_category_id": "26105",
                "special_industries": [
                    "HOUSING",
                    "EMPLOYMENT",
                    "CREDIT"
                ],
                "placement": [],
                "interest_category_name": "Housekeeping"
            }
        ],
        "action_categories": [
            {
                "action_category_name": "Fitness & Health",
                "action_category_id": "21",
                "special_industries": [
                    "HOUSING",
                    "EMPLOYMENT",
                    "CREDIT"
                ],
                "description": "TikTok users who have followed healthy lifestyle or fitness creators.",
                "scene": "CREATOR_RELATED"
            },
            {
                "action_category_name": "Other Transportation and Vehicle",
                "action_category_id": "22002",
                "special_industries": [
                    "HOUSING",
                    "EMPLOYMENT",
                    "CREDIT"
                ],
                "description": "TikTok users who have followed creators that post content about other types of transportation vehicles.",
                "scene": "CREATOR_RELATED"
            },
            {
                "action_category_name": "Selfie",
                "action_category_id": "27001",
                "special_industries": [
                    "HOUSING",
                    "EMPLOYMENT",
                    "CREDIT"
                ],
                "description": "TikTok users who have followed creators that post selfies.",
                "scene": "CREATOR_RELATED"
            }
        ]
    }
}
```

---

<a id="doc-1838630375757825"></a>
<!-- doc_id: 1838630375757825 -->
<!-- doc_id: 1838630375757825 -->
# Lấy từ khóa tìm kiếm được đề xuất (Get recommended search keywords)
> Đường dẫn: API Reference > Tools > Get recommended search keywords
Dùng endpoint này để lấy danh sách từ khóa tìm kiếm được đề xuất kèm lượt tìm kiếm hàng tháng dự đoán cho chiến dịch Search Ads.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/tool/search_keyword/recommend/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|--- |--- |--- |
|advertiser_id ***(Bắt buộc)***|string|ID tài khoản quảng cáo TikTok.|
|search_queries **(Điều kiện)**|string[]|Bắt buộc khi bạn muốn nhận từ khóa tìm kiếm đề xuất dựa trên truy vấn tìm kiếm.<br>Bạn chỉ có thể chỉ định một trong ba trường `search_queries`, `ad_ids` hoặc `landing_page_urls`.<br><br>Danh sách các truy vấn tìm kiếm.<br><br>Kích thước tối đa: 5.<br>Giới hạn độ dài mỗi truy vấn: 80 ký tự.<br><br><ul><li>Chỉ hỗ trợ các từ tiếng Anh.</li><li>Không hỗ trợ emoji và các ký hiệu đặc biệt như #.</li></ul> |
| ad_ids **(Điều kiện)** | string[] | Bắt buộc khi bạn muốn nhận từ khóa tìm kiếm đề xuất dựa trên quảng cáo cụ thể.<br>Bạn chỉ có thể chỉ định một trong ba trường `search_queries`, `ad_ids` hoặc `landing_page_urls`.<br><br>Danh sách ID quảng cáo.<br><br>Kích thước tối đa: 1.<br><br><p><span style="color:darkred"><b>Lưu ý</b></span>: Tính năng này hiện chỉ dành cho allowlist. Vui lòng liên hệ đại diện TikTok nếu cần hỗ trợ.</p> |
| landing_page_urls **(Điều kiện)** | string[] | Bắt buộc khi bạn muốn nhận từ khóa tìm kiếm đề xuất dựa trên URL trang đích.<br>Bạn chỉ có thể chỉ định một trong ba trường `search_queries`, `ad_ids` hoặc `landing_page_urls`.<br><br>Danh sách URL trang đích.<br><br>Kích thước tối đa: 5.<br><br><p><span style="color:darkred"><b>Lưu ý</b></span>: Tính năng này hiện chỉ dành cho allowlist. Vui lòng liên hệ đại diện TikTok nếu cần hỗ trợ.</p> |
|regions ***(Bắt buộc)***|string[]|Danh sách mã quốc gia hoặc khu vực.<br><br>Hiện tại, giá trị duy nhất được hỗ trợ là `US`.|
|order_field|string|Logic sắp xếp.<br><br>Các giá trị enum hỗ trợ: <ul><li>`RELEVANCE`: Sort the results by relevance.</li><li>`MONTHLY_SEARCHES`: Sort the results by the response parameter `monthly_searches`.</li></ul><br>Giá trị mặc định when `search_queries` is specified: `RELEVANCE`.<br><br><p><span style="color:darkred"><b>Note</b></span>: When `ad_ids` or `landing_page_urls` is specified, you can only set this field to `MONTHLY_SEARCHES`.</p> |
|order_type|string|Chỉ hợp lệ khi `order_field` là `MONTHLY_SEARCHES`.<br><br>Thứ tự sắp xếp kết quả.<br><br>Các giá trị enum hỗ trợ: <ul><li>`ASC`: Tăng dần (Ascending).</li><li>`DESC`: Giảm dần (Descending).</li></ul><br>Giá trị mặc định: `DESC`.<br><br><p><span style="color:darkred"><b>Note</b></span>: When `ad_ids` or `landing_page_urls` is specified, you can only set this field to `DESC`.</p> |
| total_size | number | Tổng số từ khóa đề xuất cần trả về.<br><br>Phạm vi giá trị: 1-1.000.<br>Giá trị mặc định: 1.000. |
|page|number|Số trang hiện tại cần lấy dữ liệu.<br><br>Value range: ≥1.<br>Giá trị mặc định: 1.|
|page_size|number|Kích thước trang (số kết quả mỗi trang).<br><br>Value range: 1-1,000.<br>Giá trị mặc định: 50.|

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/tool/search_keyword/recommend/?advertiser_id={{advertiser_id}}&search_queries=["TikTok"]&regions=["US"]&order_field=MONTHLY_SEARCHES&order_type=DESC' \
--header 'Access-Token: {{Access-Token}}'
```
## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
|code |number|Response code. For the complete list of response codes and descriptions, see [Appendix-Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
|message|string|Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097).|
|request_id |string|ID nhật ký (log ID) của yêu cầu, dùng để định danh duy nhất cho yêu cầu.  |
|data|object|Dữ liệu trả về.|
#|recommended_keywords|object[]|Danh sách các từ khóa tìm kiếm được đề xuất.|
##|recommended_keyword|string|Từ khóa tìm kiếm được đề xuất.|
##|monthly_searches|integer|Predicted monthly searches.<br>Prediction is based on historical data for your reference.|
#|page_info|object|Thông tin phân trang.|
##|page|number|Số trang hiện tại cần lấy dữ liệu.|
##|page_size|number|Kích thước trang (số kết quả mỗi trang).|
##|total_number|number|Tổng số kết quả tìm thấy.|
##|total_page|number|Tổng số trang kết quả.|

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "page_info": {
            "page": 1,
            "page_size": 50,
            "total_number": 897,
            "total_page": 18
        },
        "recommended_keywords": [
            {
                "monthly_searches": 22063,
                "recommended_keyword": "messytiktok"
            },
            ...
            {
                "monthly_searches": 9747,
                "recommended_keyword": "funny relatable tiktoks"
            }
        ]
    }
}
```

---

<a id="doc-1848591212970082"></a>
<!-- doc_id: 1848591212970082 -->
<!-- doc_id: 1848591212970082 -->
# Lấy chẩn đoán sức khỏe chiến dịch Quảng cáo tìm kiếm (Get Search Ads Campaign Health diagnoses)
> Đường dẫn: API Reference > Tools > Get Search Ads Campaign Health diagnoses
Sử dụng endpoint này để truy xuất health diagnoses for your ad groups or ads within a Search Ads Campaign. It provides insights on search volume, keyword relevance, as well as bid and budget recommendations.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/tool/diagnosis/search/health/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id  ****(Bắt buộc)**** | string | ID tài khoản quảng cáo TikTok. |
| adgroup_id | string | ID nhóm quảng cáo. ⏎ Chỉ định trường này nếu bạn muốn nhận chẩn đoán cho một nhóm quảng cáo hiện có. ⏎ Để lấy ID các nhóm quảng cáo trong Chiến dịch quảng cáo tìm kiếm, sử dụng [/adgroup/get/](07-ad-groups-p1.md#doc-1739314558673922) với trường lọc `campaign_ids` đặt thành ID chiến dịch. ⏎ **Lưu ý**: Nếu chỉ định cả `adgroup_id` và `ad_ids`, `adgroup_id` sẽ được ưu tiên. |
| ad_ids | string[] | Danh sách ID quảng cáo. ⏎ Chỉ định trường này nếu bạn muốn nhận chẩn đoán cho các quảng cáo hiện có. ⏎ Các ID quảng cáo phải thuộc cùng một nhóm quảng cáo. ⏎ Kích thước tối đa: 50. ⏎ Để lấy ID quảng cáo, sử dụng [/ad/get/](02-ads-p1.md#doc-1735735588640770) với trường lọc `adgroup_ids`. ⏎ **Lưu ý**: Nếu chỉ định cả `adgroup_id` và `ad_ids`, `adgroup_id` sẽ được ưu tiên. |

### Ví dụ lệnh cURL (Example)
#### Lấy chẩn đoán cho nhóm quảng cáo hiện có

```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/tool/diagnosis/search/health/?advertiser_id={{advertiser_id}}&adgroup_id={{adgroup_id}}' \
--header 'Access-Token: {{Access-Token}}'
```

#### Lấy chẩn đoán cho các quảng cáo hiện có

```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/tool/diagnosis/search/health/?advertiser_id={{advertiser_id}}&ad_ids=["{{ad_id}}","{{ad_id}}"]' \
--header 'Access-Token: {{Access-Token}}'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Response code. For the complete list of response codes and descriptions, see [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | ID nhật ký (log ID) của yêu cầu, dùng để định danh duy nhất cho yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ search_health_status | string | Trạng thái sức khỏe tìm kiếm tổng thể. Trạng thái này cung cấp cái nhìn tổng quan về mức độ thiết lập tốt của nhóm quảng cáo hoặc quảng cáo. ⏎ Các giá trị enum hỗ trợ: • `GOOD`: Tốt. Bạn đã thiết lập để có hiệu suất tốt hơn. • `NEED_IMPROVEMENT`: Cần cải thiện. • `NO_DATA`: Không có dữ liệu. |
| ↳ search_volume | object | Các chỉ số chi tiết về lượng tìm kiếm cho từ khóa của bạn. |
| ↳↳ diagnosis_result | string | Kết quả từ phân tích lượng tìm kiếm. ⏎ Các giá trị enum hỗ trợ: • `HIGH`: Cao. • `MEDIUM`: Trung bình. • `LOW`: Thấp. • `INVALID`: Không hợp lệ. |
| ↳↳ total_monthly_searches | number | Số lượt tìm kiếm ước tính hàng tháng mà từ khóa của bạn nhận được. ⏎ Con số này có thể thay đổi tùy thuộc vào cài đặt loại đối sánh. Đối sánh mở rộng có thể giúp tối đa hóa lượng tìm kiếm. |
| ↳ total_keyword_count | number | Tổng số lượng từ khóa tìm kiếm. |
| ↳ total_relevant_keyword_count | number | Tổng số từ khóa tìm kiếm được xác định là có liên quan đến nhóm quảng cáo hoặc quảng cáo. |
| ↳ keyword_relevance | object[] | Chi tiết về mức độ liên quan của từ khóa đối với nhóm quảng cáo hoặc quảng cáo. |
| ↳↳ adgroup_id | string | ID nhóm quảng cáo. |
| ↳↳ ad_id | string | ID mẫu quảng cáo. |
| ↳↳ keyword_relevance_status | string | Kết quả từ phân tích mức độ liên quan của từ khóa. ⏎ Các giá trị enum hỗ trợ: • `TO_BE_CALCULATED`: Đang tính toán. • `PARTIALLY_RELEVANT`: Liên quan một phần. • `RELEVANT`: Có liên quan. • `IRRELEVANT`: Không liên quan. |
| ↳↳ relevant_keyword_count | number | Số lượng từ khóa tìm kiếm có liên quan. |
| ↳↳ relevant_keywords | string[] | Danh sách các từ khóa tìm kiếm có liên quan. |
| ↳↳ irrelevant_keyword_count | number | Số lượng từ khóa tìm kiếm không liên quan. |
| ↳↳ irrelevant_keywords | string[] | Danh sách các từ khóa tìm kiếm không liên quan. |
| ↳ bid_budget | object | Chi tiết về chẩn đoán giá thầu và ngân sách. |
| ↳↳ bid_budget_status | string | Kết quả phân tích giá thầu và ngân sách. ⏎ Các giá trị enum hỗ trợ: • `GOOD`: Tốt. • `LOW_BID_AND_BUDGET`: Giá thầu và ngân sách thấp. • `LOW_BUDGET`: Ngân sách thấp. • `LOW_BID`: Giá thầu thấp. • `NO_DATA`: Không có dữ liệu. |
| ↳↳ bid_suggestion_status | string | Kết quả chẩn đoán dành riêng cho giá thầu. ⏎ Các giá trị enum hỗ trợ: • `GOOD`: Tốt. • `LOW`: Giá thầu thấp. • `NO_DATA`: Không có dữ liệu. |
| ↳↳ suggested_value | string | Mức giá thầu đề xuất. ⏎ Dựa trên dữ liệu lịch sử, các nhóm quảng cáo hoặc quảng cáo của bạn có thể nhận được nhiều chuyển đổi hơn bằng cách tăng giá thầu lên ít nhất giá trị này. |

### Ví dụ lệnh cURL (Example)
#### Lấy chẩn đoán cho nhóm quảng cáo hiện có

```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "bid_budget": {
            "bid_budget_status": "GOOD",
            "bid_suggestion_status": "GOOD"
        },
        "keyword_relevance": [
            {
                "ad_id": "{{ad_id}}",
                "adgroup_id": "{{adgroup_id}}",
                "irrelevant_keyword_count": 0,
                "keyword_relevance_status": "RELEVANT",
                "relevant_keyword_count": 1,
                "relevant_keywords": [
                    "{{relevant_keyword}}"
                ]
            }
        ],
        "search_health_status": "NEED_IMPROVEMENT",
        "search_volume": {
            "diagnosis_result": "LOW",
            "total_monthly_searches": 52689
        },
        "total_keyword_count": 1,
        "total_relevant_keyword_count": 1
    }
}
```

#### Lấy chẩn đoán cho các quảng cáo hiện có

```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "bid_budget": {
            "bid_budget_status": "LOW_BUDGET",
            "bid_suggestion_status": "GOOD"
        },
        "keyword_relevance": [
            {
                "ad_id": "{{ad_id}}",
                "adgroup_id": "{{adgroup_id}}",
                "irrelevant_keyword_count": 0,
                "keyword_relevance_status": "RELEVANT",
                "relevant_keyword_count": 2,
                "relevant_keywords": [
                    "drink",
                    "food"
                ]
            },
            {
                "ad_id": "{{ad_id}}",
                "adgroup_id": "{{adgroup_id}}",
                "irrelevant_keyword_count": 0,
                "keyword_relevance_status": "RELEVANT",
                "relevant_keyword_count": 2,
                "relevant_keywords": [
                    "drink",
                    "food"
                ]
            }
        ],
        "search_health_status": "NEED_IMPROVEMENT",
        "search_volume": {
            "diagnosis_result": "HIGH",
            "total_monthly_searches": 52472817
        },
        "total_keyword_count": 2,
        "total_relevant_keyword_count": 4
    }
}
```

---

<a id="doc-1855460985594881"></a>
<!-- doc_id: 1855460985594881 -->
<!-- doc_id: 1855460985594881 -->
# Khám phá từ khóa mới (Discover new keywords)
> Đường dẫn: API Reference > Tools > Discover new keywords
Sử dụng endpoint này để khám phá các từ khóa mới và tìm kiếm ý tưởng từ khóa nhằm tiếp cận những người quan tâm đến doanh nghiệp của bạn.

## Yêu cầu gọi API (Request)

**Endpoint** https://business-api.tiktok.com/open_api/v1.3/tool/search_keyword/keyword_idea/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id  ****(Bắt buộc)**** | string | ID tài khoản quảng cáo TikTok. |
| keywords  ****(Bắt buộc)**** | string[] | Danh sách từ khóa. ⏎ Bạn có thể chỉ định các sản phẩm hoặc dịch vụ liên quan chặt chẽ đến doanh nghiệp của mình. ⏎ Kích thước tối đa: 10. ⏎ Giới hạn độ dài mỗi từ khóa: 80 ký tự. ⏎ • Chỉ hỗ trợ các từ tiếng Anh. • Không hỗ trợ biểu tượng cảm xúc (emoji) và các ký hiệu đặc biệt như #. ⏎ **Lưu ý**: Để đạt kết quả tối ưu, hãy cung cấp tất cả các từ khóa bằng chữ thường. Không khuyến khích dùng chữ in hoa. |
| order_field | string | Logic sắp xếp. ⏎ Các giá trị enum hỗ trợ: • `AVG_MONTHLY_SEARCHES`: Sort the results by the range of average monthly searches as indicated by the response parameters `avg_monthly_searches_lower` and `avg_monthly_searches_upper`. • `THREE_MONTH_CHANGE`: Sort the results by the response parameter `three_month_change`. • `YEAR_OVER_YEAR_CHANGE`: Sort the results by the response parameter `year_over_year_change`. • `COMPETITION`: Sort the results by the response parameter `competition`.Giá trị mặc định: `AVG_MONTHLY_SEARCHES`. |
| order_type | string | Thứ tự sắp xếp kết quả. ⏎ Các giá trị enum hỗ trợ: • `ASC`: ascending. • `DESC`: descending.Giá trị mặc định: `DESC`. |
| brand_type | string | Loại thương hiệu. ⏎ Các giá trị enum hỗ trợ: • `BRAND`: Thương hiệu. • `NON_BRAND`: Phi thương hiệu. • `ALL`: Tất cả. Giá trị mặc định: `ALL`. ⏎ **Lưu ý**: Bộ lọc này chỉ khả dụng khi `country_codes` được đặt là `["US"]`. Đối với tất cả các quốc gia hoặc khu vực khác, `ALL` là giá trị mặc định và duy nhất được phép. |
| country_codes | string[] | Mã vị trí địa lý của quốc gia hoặc khu vực mà bạn muốn nhắm mục tiêu. ⏎ Kích thước tối đa: 1. ⏎ Giá trị mặc định: `US`. ⏎ Để xem danh sách giá trị enum, xem Danh sách giá trị cho `country_codes`. ⏎ **Lưu ý**: Khám phá từ khóa mới cho các vị trí ngoài Hoa Kỳ hiện là tính năng chỉ dành cho danh sách cho phép (allowlist). Vui lòng liên hệ đại diện TikTok nếu cần hỗ trợ. |

### Danh sách giá trị cho `country_codes`

| country_codes value | Description |
|---|---|
| `AU` | Australia |
| `BR` | Brazil |
| `CA` | Canada |
| `FR` | France |
| `DE` | Germany |
| `IT` | Italy |
| `MX` | Mexico |
| `SA` | Saudi Arabia |
| `ES` | Spain |
| `AE` | United Arab Emirates |
| `GB` | United Kingdom |
| `US` | United States |

### Ví dụ lệnh cURL (Example)

```http
// curl
curl --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/tool/search_keyword/keyword_idea/?advertiser_id={{advertiser_id}}&keywords=["{{keyword}}","{{keyword}}"]&order_field=AVG_MONTHLY_SEARCHES&order_type=DESC&brand_type=ALL&country_codes=["US"]' \
--header 'Access-Token: {{Access-Token}}'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Response code. For the complete list of response codes and descriptions, see [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Response message. Để biết chi tiết, xem [Appendix - Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| request_id | string | ID nhật ký (log ID) của yêu cầu, dùng để định danh duy nhất cho yêu cầu. |
| data | object | Dữ liệu trả về. |
| ↳ total_search_volume_lower | number | Giá trị bắt đầu của khoảng tổng lượng tìm kiếm cho tất cả các từ khóa gợi ý (`keywords`). |
| ↳ total_search_volume_upper | number | Giá trị kết thúc của khoảng tổng lượng tìm kiếm cho tất cả các từ khóa gợi ý (`keywords`). |
| ↳ keywords | object[] | Danh sách các từ khóa gợi ý có liên quan đến từ khóa đã chỉ định dựa trên quốc gia/khu vực mục tiêu (`country_codes`). |
| ↳↳ recommended_keyword | string | Keyword. ⏎ A suggested keyword relevant to the specified keyword or keywords. |
| ↳↳ avg_monthly_searches_lower | number | Lượng tìm kiếm trung bình hàng tháng (Thấp). ⏎ Đây là mốc dưới của khoảng lượng tìm kiếm trung bình hàng tháng trong tháng vừa qua của từ khóa và các cụm từ tương tự dựa trên quốc gia/khu vực nhắm mục tiêu. |
| ↳↳ avg_monthly_searches_upper | number | Lượng tìm kiếm trung bình hàng tháng (Cao). ⏎ Đây là mốc trên của khoảng lượng tìm kiếm trung bình hàng tháng trong tháng vừa qua của từ khóa và các cụm từ tương tự dựa trên quốc gia/khu vực nhắm mục tiêu. |
| ↳↳ three_month_change | float | Thay đổi trong 3 tháng. ⏎ Dữ liệu này so sánh lượng tìm kiếm hàng tháng của tháng gần nhất với dữ liệu từ hai tháng trước đó. |
| ↳↳ year_over_year_change | float | Thay đổi so với cùng kỳ năm trước (YoY). ⏎ Dữ liệu này so sánh lượng tìm kiếm hàng tháng của tháng trước với cùng kỳ năm ngoái. |
| ↳↳ competition | string | Mức độ cạnh tranh. ⏎ Cho biết mức độ cạnh tranh vị trí quảng cáo cho một từ khóa, dựa trên số lượng nhà quảng cáo duy nhất đấu thầu từ khóa đó trong tháng qua. ⏎ Các giá trị enum hỗ trợ: • `HIGH`: Cao. • `MEDIUM`: Trung bình. • `LOW`: Thấp. |
| ↳↳ estimated_cpc_lower | float | CPC ước tính (Thấp), tính bằng USD. ⏎ Đây là mốc dưới của khoảng CPC mà các nhà quảng cáo đã trả trong tháng trước cho vị trí quảng cáo đầu trang tìm kiếm của từ khóa theo quốc gia/khu vực nhắm mục tiêu. CPC thực tế có thể thay đổi. |
| ↳↳ estimated_cpc_upper | float | CPC ước tính (Cao), tính bằng USD. ⏎ Đây là mốc trên của khoảng CPC mà các nhà quảng cáo đã trả trong tháng trước cho vị trí quảng cáo đầu trang tìm kiếm của từ khóa theo quốc gia/khu vực nhắm mục tiêu. CPC thực tế có thể thay đổi. |

### Ví dụ lệnh cURL (Example)

```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "keywords": [
            {
                "avg_monthly_searches_lower": 500000,
                "avg_monthly_searches_upper": 1000000,
                "competition": "HIGH",
                "estimated_cpc_lower": 0.5062341041327454,
                "estimated_cpc_upper": 0.6947784896270967,
                "recommended_keyword": "shoes",
                "three_month_change": -0.3566219295724846,
                "year_over_year_change": -0.9556371579502115
            },
            {
                "avg_monthly_searches_lower": 100000,
                "avg_monthly_searches_upper": 250000,
                "competition": "HIGH",
                "estimated_cpc_lower": 0.6854101014434859,
                "estimated_cpc_upper": 0.8316111534680811,
                "recommended_keyword": "bear claw shoes",
                "three_month_change": -0.000005560127215710696,
                "year_over_year_change": 0.00040605635839757926
            },
            ...
            {
                "avg_monthly_searches_lower": 1000,
                "avg_monthly_searches_upper": 5000,
                "competition": "MEDIUM",
                "estimated_cpc_lower": 0,
                "estimated_cpc_upper": 0,
                "recommended_keyword": "mid dunks",
                "three_month_change": -0.9375,
                "year_over_year_change": -0.9999778408083673
            },
            {
                "avg_monthly_searches_lower": 1000,
                "avg_monthly_searches_upper": 5000,
                "competition": "HIGH",
                "estimated_cpc_lower": 0.0375,
                "estimated_cpc_upper": 0.07250000000000001,
                "recommended_keyword": "midnight ballerina shoes",
                "three_month_change": -0.7937971500419112,
                "year_over_year_change": -0.7861799217731421
            }
        ],
        "total_search_volume_lower": 2500000,
        "total_search_volume_upper": 5000000
    }
}
```

---

<a id="doc-1738308662898689"></a>
<!-- doc_id: 1738308662898689 -->
<!-- doc_id: 1738308662898689 -->
# Lấy danh sách phiên bản hệ điều hành (Get OS versions)
> Đường dẫn: API Reference > Tools > Get OS versions
Sử dụng endpoint này để lấy thông tin the enumeration values of operating system version.

## Yêu cầu gọi API (Request)

**Endpoint**
https://business-api.tiktok.com/open_api/v1.3/tool/os_version/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id  ****(Bắt buộc)**** | string | ID tài khoản quảng cáo TikTok. |
| os_type  ****(Bắt buộc)**** | string | OS type. Các giá trị enum hỗ trợ: `ANDROID`,`IOS`. |

### Ví dụ lệnh cURL (Example)
```http
// curl
curl --location request GET 'https://business-api.tiktok.com/open_api/v1.3/tool/os_version/?advertiser_id={{advertiser_id}}&os_type=IOS' \
--header 'Access-Token: {{Access-Token}}'
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Mã trạng thái phản hồi (0: Thành công). For the complete list of response codes and descriptions, see [Appendix-Mã trạng thái phản hồi (0: Thành công)](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông điệp phản hồi từ máy chủ. Để biết chi tiết, xem [Appendix-Return information](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| data | object | Dữ liệu trả về. |
| ↳ os_versions | object[] | OS versions list. |
| ↳↳ os_id | string | OS versions ID. |
| ↳↳ os_type | string | OS type. |
| ↳↳ version | string | OS version. |
| ↳↳ name | string | OS version name. |
| request_id | string | ID nhật ký (log ID) của yêu cầu, dùng để định danh duy nhất cho yêu cầu. |

### Ví dụ lệnh cURL (Example)
```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "{{request_id}}",
    "data": {
        "os_versions": [
            {
                "name": "{{name}}",
                "version": "{{version}}",
                "os_id": "{{os_id}}"
            },
            {
                "name": "{{name}}",
                "version": "{{version}}",
                "os_id": "{{os_id}}"
            }
            }
        ]
    }
}
```

---

<a id="doc-1737172880570369"></a>
<!-- doc_id: 1737172880570369 -->
<!-- doc_id: 1737172880570369 -->
# Lấy danh sách mẫu thiết bị (Get device models)
> Đường dẫn: API Reference > Tools > Get device models
Sử dụng endpoint này để lấy thông tin device model enumeration values.

## Yêu cầu gọi API (Request)

**Endpoint**
https://business-api.tiktok.com/open_api/v1.3/tool/device_model/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id  ****(Bắt buộc)**** | string | ID tài khoản quảng cáo TikTok |

### Ví dụ lệnh cURL (Example)

```java
// Java
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import okhttp3.*;
import org.apache.http.client.utils.URIBuilder;

import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
import java.net.URL;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

public class Demo {
    private static final String ACCESS_TOKEN = "xxx";
    private static final String PATH = "/open_api/v1.3/tool/device_model/";
    private static final ObjectMapper mapper = new ObjectMapper();

    /**
     * Build request URL
     *
     * @param path Request path
     * @return Request URL
     */
    private static String buildUrl(String path) throws URISyntaxException {
        URI uri = new URI("https", "business-api.tiktok.com", path, "", "");
        return uri.toString();
    }

    
    /**
     * Send GET request
     *
     * @param jsonStr:Args in JSON format
     * @return Response in JSON format
     */
    private static String get(String jsonStr) throws IOException, URISyntaxException {
        OkHttpClient client = new OkHttpClient().newBuilder().build();
        URIBuilder ub = new URIBuilder(buildUrl(PATH));
        Map< String, Object > map = mapper.readValue(jsonStr, Map.class);
        map.forEach((k, v) -> {
            try {
                ub.addParameter(k, v instanceof String ? (String) v : mapper.writeValueAsString(v));
            } catch (JsonProcessingException e) {
                e.printStackTrace();
            }
        });
        URL url = ub.build().toURL();

        Request request = new Request.Builder()
                .url(url)
                .method("GET", null)
                .addHeader("Access-Token", ACCESS_TOKEN)
                .build();
        Response response = client.newCall(request).execute();
        return response.body().string();
    }

    public static void main(String[] args) throws IOException, URISyntaxException {
        Long advertiser_id = ADVERTISER_ID;

        // Args in JSON format
        String myArgs = String.format("{\"advertiser_id\": \"%s\"}",advertiser_id);
        System.out.println(get(myArgs));
    }
}
```
```python
// Python
# coding=utf-8
import json
import requests

from six import string_types
from six.moves.urllib.parse import urlencode, urlunparse  # noqa

ACCESS_TOKEN = "xxx"
PATH = "/open_api/v1.3/tool/device_model/"

def build_url(path, query=""):
    # type: (str, str) -> str
    """
    Build request URL
    :param path: Request path
    :param query: Querystring
    :return: Request URL
    """
    scheme, netloc = "https", "business-api.tiktok.com"
    return urlunparse((scheme, netloc, path, "", query, ""))

def get(json_str):
    # type: (str) -> dict
    """
    Send GET request
    :param json_str: Args in JSON format
    :return: Response in JSON format
    """
    args = json.loads(json_str)
    query_string = urlencode({k: v if isinstance(v, string_types) else json.dumps(v) for k, v in args.items()})
    url = build_url(PATH, query_string)
    headers = {
        "Access-Token": ACCESS_TOKEN,
    }
    rsp = requests.get(url, headers=headers)
    return rsp.json()

if __name__ == '__main__':
    advertiser_id = ADVERTISER_ID

    # Args in JSON format
    my_args = "{\"advertiser_id\": \"%s\"}" % (advertiser_id)
    print(get(my_args))
```
```php
// PHP
$ACCESS_TOKEN = "xxx";
$PATH = "/open_api/v1.3/tool/device_model/";

/**
 * Build request URL
 * @param $path : Request path
 * @return string
 */
function build_url($path)
{
    return "https://business-api.tiktok.com" . $path;
}

/**
 * Send GET request
 * @param $json_str : Args in JSON format
 * @return bool|string : Response in JSON format
 */
function get($json_str)
{
    global $ACCESS_TOKEN, $PATH;
    $curl = curl_init();

    $args = json_decode($json_str, true);

    /* Values of querystring is also in JSON format */
    foreach ($args as $key => $value) {
        $args[$key] = is_string($value) ? $value : json_encode($value);
    }

    $url = build_url($PATH) . "?" . http_build_query(
            $args
        );

    curl_setopt_array($curl, array(
        CURLOPT_URL => $url,
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_ENCODING => "",
        CURLOPT_MAXREDIRS => 10,
        CURLOPT_TIMEOUT => 0,
        CURLOPT_FOLLOWLOCATION => true,
        CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
        CURLOPT_CUSTOMREQUEST => "GET",
        CURLOPT_HTTPHEADER => array(
            "Access-Token: " . $ACCESS_TOKEN,
        ),
    ));

    $response = curl_exec($curl);
    curl_close($curl);
    return $response;
}

$advertiser_id = ADVERTISER_ID;

/* Args in JSON format */
$my_args = sprintf("{\"advertiser_id\": \"%s\"}", $advertiser_id);
echo get($my_args);
```
```http
// curl
curl --get -H "Access-Token:xxx" \
--data-urlencode "advertiser_id=ADVERTISER_ID" \
https://business-api.tiktok.com/open_api/v1.3/tool/device_model/
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Mã phản hồi. Để xem danh sách đầy đủ các mã phản hồi và mô tả, xem [Phụ lục - Mã trả về](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông điệp phản hồi. Để biết chi tiết, xem [Phụ lục - Mã trả về](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| data | json | Dữ liệu trả về. |
| ↳ device_models | object[] | Danh sách các đối tượng mẫu thiết bị |
| ↳↳ device_model_id | string | ID mẫu thiết bị. |
| ↳↳ device_model_name | string | Tên mẫu thiết bị. |
| ↳↳ child_device_ids | string[] | Danh sách ID mẫu thiết bị con |
| ↳↳ is_active | boolean | Liệu device model is active or not. Only active device models can be targeted. |
| ↳↳ level | string | Cấp độ mẫu thiết bị. Các giá trị enum hỗ trợ: `BRAND`,`SERIES`,`MODEL`. |
| ↳↳ os_type | string | Loại hệ điều hành. Các giá trị enum hỗ trợ: `ANDROID`,`IOS` |
| request_id | string | ID nhật ký (log ID) của yêu cầu, dùng để định danh duy nhất cho yêu cầu. |

### Ví dụ lệnh cURL (Example)

```http
// Success-Response
HTTPS/1.1 200 OK
{
    "code": 0,
    "message": "OK",
    "request_id": "202206302151270102452421061A5D0C58",
    "data": {
        "device_models": [
            {
                "child_device_ids": [
                    "101001",
                    "101002",
                    "101003",
                    "101004",
                    "101005",
                    "101006",
                    "101007",
                    "101008",
                    "101009",
                    "101010",
                    "101011",
                    "101012",
                    "101013",
                    "101014",
                    "101015",
                    "101016",
                    "101017",
                    "101018",
                    "101019",
                    "101020",
                    "101021",
                    "101022",
                    "101023",
                    "101024",
                    "101025",
                    "101026"
                ],
                "os_type": "ANDROID",
                "device_meta_name": "MEIZU",
                "is_active": false,
                "level": "BRAND",
                "device_meta_id": "101"
            },
            ...
        ]
    }
}
```

---

<a id="doc-1737168013095938"></a>
<!-- doc_id: 1737168013095938 -->
<!-- doc_id: 1737168013095938 -->
# Lấy danh sách nhà mạng viễn thông (Get carriers)
> Đường dẫn: API Reference > Tools > Get carriers
Sử dụng endpoint này để lấy thông tin the carrier enumeration values that represents carriers in different countries or locations.

## Yêu cầu gọi API (Request)

**Endpoint**
https://business-api.tiktok.com/open_api/v1.3/tool/carrier/

**Method** GET

**Header**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| Access-Token  ****(Bắt buộc)**** | string | Mã truy cập được ủy quyền (Access Token). Để biết chi tiết, xem [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

**Parameters**

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| advertiser_id  ****(Bắt buộc)**** | string | ID tài khoản quảng cáo TikTok |

### Ví dụ lệnh cURL (Example)

```http
// curl
curl --get -H "Access-Token:xxx" \
--data-urlencode "advertiser_id=ADVERTISER_ID" \
https://business-api.tiktok.com/open_api/v1.3/tool/carrier/
```

## Dữ liệu phản hồi (Response)

| Trường (Field) | Kiểu dữ liệu | Mô tả chi tiết |
|---|---|---|
| code | number | Mã trạng thái phản hồi (0: Thành công). For the complete list of response codes and descriptions, see [Appendix-Return codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| message | string | Thông điệp phản hồi từ máy chủ. Để biết chi tiết, xem[Appendix-Return codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| data | object | Dữ liệu trả về |
| ↳ countries | object[] | Danh sách quốc gia hoặc vị trí địa lý. |
| ↳↳ country_code | string | Mã quốc gia hoặc vị trí địa lý. |
| ↳↳ carriers | object[] | Danh sách nhà mạng tại quốc gia hoặc khu vực. |
| ↳↳↳ carrier_id | string | ID nhà mạng viễn thông. Bạn có thể truyền giá trị này khi tạo quảng cáo. |
| ↳↳↳ in_use | boolean | Liệu carrier can be used for targeting |
| ↳↳↳ name | string | Tên nhà mạng viễn thông. |
| ↳↳↳ value | object[] | Danh sách ID HNI (MCC/MNC) |
| ↳↳↳↳ hni_id | number | HNI (MCC/MNC) ID. A unique combination formed from the MNC (Mobile Network Code) and MCC (Mobile Country Code), to form a home network identity (HNI) |
| ↳↳↳↳ in_use | boolean | Liệu HNI ID can be used for targeting |
| request_id | string | ID nhật ký (log ID) của yêu cầu, dùng để định danh duy nhất cho yêu cầu. |

### Ví dụ lệnh cURL (Example)

```http
// Success-Response
HTTPS/1.1 200 OK

{
    "code": 0,
    "message": "OK",
    "request_id": "20220630234500010245242163145E6D44",
    "data": {
        "countries": [
            {
                "carriers": [
                    {
                        "in_use": true,
                        "value": [
                            {
                                "in_use": true,
                                "hni_id": "42402"
                            }
                        ],
                        "name": "AE: Etisalat",
                        "carrier_id": "4240000"
                    },
                    {
                        "in_use": true,
                        "value": [
                            {
                                "in_use": true,
                                "hni_id": "42403"
                            }
                        ],
                        "name": "AE: du",
                        "carrier_id": "4240001"
                    }
                ],
                "country_code": "AE"
            },
            {
                "carriers": [
                    {
                        "in_use": true,
                        "value": [
                            {
                                "in_use": true,
                                "hni_id": "722310"
                            },
                            {
                                "in_use": true,
                                "hni_id": "722320"
                            },
                            {
                                "in_use": true,
                                "hni_id": "722330"
                            }
                        ],
                        "name": "AR: Claro",
                        "carrier_id": "7220000"
                    },
                    ...
                ],
                "country_code": "AR",
            },
            ...
        ]
    }
}
```
---

## Hướng dẫn thực hành Data Retrieval (Python & cURL)

Dưới đây là mã nguồn mẫu minh họa quy trình gọi API thực tế cho phân hệ **Công cụ tra cứu (Tools) — phần 1/3**:

### cURL mẫu
```bash
curl -s -X GET "https://business-api.tiktok.com/open_api/v1.3/example/get/?advertiser_id=YOUR_ADVERTISER_ID" \
  -H "Access-Token: YOUR_ACCESS_TOKEN"
```

### Python script mẫu
```python
import requests
import json

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
ADVERTISER_ID = "YOUR_ADVERTISER_ID"
BASE_URL = "https://business-api.tiktok.com/open_api/v1.3"

headers = {
    "Access-Token": ACCESS_TOKEN,
    "Content-Type": "application/json"
}

def execute_request():
    url = f"{BASE_URL}/example/get/"
    params = {"advertiser_id": ADVERTISER_ID}
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    if data.get("code") == 0:
        print("Truy vấn thành công:", data.get("data"))
        return data.get("data")
    else:
        print(f"Lỗi: {data.get('code')} - {data.get('message')}")
        return None

if __name__ == "__main__":
    execute_request()
```

