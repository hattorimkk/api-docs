# Tệp đối tượng (Audience)

Nhóm API Tệp đối tượng (Audience) cung cấp các giải pháp mạnh mẽ giúp nhà quảng cáo TikTok For Business xây dựng, quản lý và tối ưu hóa các tệp đối tượng tùy chỉnh (Custom Audience), đối tượng tương tự (Lookalike Audience), đối tượng đã lưu (Saved Audience) cũng như khám phá thông tin chuyên sâu (Audience Insights). Thông qua các phương thức tải lên tệp khách hàng (Customer File) hoặc truyền dữ liệu luồng theo thời gian thực (Streaming API), bạn có thể nhắm mục tiêu chính xác hoặc loại trừ các nhóm người dùng cụ thể trong chiến dịch quảng cáo. Tài liệu này cung cấp chi tiết kỹ thuật cho toàn bộ các endpoint thuộc nhóm Audience API trong phiên bản v1.3.

## Mục lục các endpoint

| Nhóm chức năng | Endpoint | Phương thức | Mục đích |
|---|---|---|---|
| **Customer File** | [/dmp/custom_audience/file/upload/](09-audience.md#doc-1739940567842818) | `POST` | Tải lên tệp dữ liệu khách hàng (CSV/TXT) |
| **Customer File** | [/dmp/custom_audience/create/](09-audience.md#doc-1739940570793985) | `POST` | Tạo tệp đối tượng tùy chỉnh từ tệp dữ liệu đã tải lên |
| **Streaming API** | [/segment/audience/](09-audience.md#doc-1739940583739393) | `POST` | Tạo hoặc xóa phân đoạn đối tượng (audience segment) |
| **Streaming API** | [/segment/mapping/](09-audience.md#doc-1739940585975809) | `POST` | Thêm hoặc xóa ánh xạ người dùng vào phân đoạn đối tượng |
| **Quản lý đối tượng** | [/dmp/custom_audience/update/](09-audience.md#doc-1739940572667906) | `POST` | Cập nhật tên hoặc tệp dữ liệu (Append, Remove, Replace) |
| **Quản lý đối tượng** | [/dmp/custom_audience/list/](09-audience.md#doc-1739940506015746) | `GET` | Lấy danh sách tất cả tệp đối tượng của tài khoản |
| **Quản lý đối tượng** | [/dmp/custom_audience/get/](09-audience.md#doc-1739940507792385) | `GET` | Lấy thông tin chi tiết và lịch sử cập nhật của tệp đối tượng |
| **Quản lý đối tượng** | [/dmp/custom_audience/rule/create/](09-audience.md#doc-1739940509849601) | `POST` | Tạo tệp đối tượng dựa trên quy tắc tương tác/hành vi (Rule) |
| **Đối tượng Lookalike** | [/dmp/custom_audience/lookalike/create/](09-audience.md#doc-1739940511844353) | `POST` | Tạo tệp đối tượng tương tự (Lookalike Audience) |
| **Đối tượng Lookalike** | [/dmp/custom_audience/lookalike/update/](09-audience.md#doc-1758616888158209) | `POST` | Làm mới thủ công dữ liệu tệp đối tượng tương tự |
| **Quản lý đối tượng** | [/dmp/custom_audience/delete/](09-audience.md#doc-1739940539757569) | `POST` | Xóa một hoặc nhiều tệp đối tượng |
| **Chia sẻ đối tượng** | [/dmp/custom_audience/share/](09-audience.md#doc-1740245803888706) | `POST` | Chia sẻ tệp đối tượng với các tài khoản trong cùng Business Center |
| **Chia sẻ đối tượng** | [/dmp/custom_audience/share/cancel/](09-audience.md#doc-1740245829978113) | `POST` | Hủy chia sẻ tệp đối tượng với tài khoản quảng cáo khác |
| **Chia sẻ đối tượng** | [/dmp/custom_audience/share/log/](09-audience.md#doc-1740245827044354) | `GET` | Lấy nhật ký các tài khoản đã được chia sẻ tệp đối tượng |
| **Áp dụng nhóm QC** | [/dmp/custom_audience/apply/](09-audience.md#doc-1758615097524225) | `POST` | Áp dụng (Include/Exclude) hoặc gỡ đối tượng khỏi nhóm quảng cáo |
| **Áp dụng nhóm QC** | [/dmp/custom_audience/apply/log/](09-audience.md#doc-1758615737388033) | `GET` | Lấy nhật ký lịch sử áp dụng đối tượng vào các nhóm quảng cáo |
| **Saved Audience** | [/dmp/saved_audience/create/](09-audience.md#doc-1780154541898754) | `POST` | Tạo tập thiết lập nhắm mục tiêu đã lưu (Saved Audience) |
| **Saved Audience** | [/dmp/saved_audience/list/](09-audience.md#doc-1780154619404290) | `GET` | Lấy danh sách và chi tiết các đối tượng đã lưu |
| **Saved Audience** | [/dmp/saved_audience/delete/](09-audience.md#doc-1780154666312706) | `POST` | Xóa các đối tượng đã lưu khi không còn gắn với nhóm QC |
| **Audience Insights** | [/audience/insight/info/](09-audience.md#doc-1797016593782785) | `POST` | Phân tích quy mô và đặc điểm nhân khẩu đối tượng tiềm năng |
| **Audience Insights** | [/audience/insight/overlap/](09-audience.md#doc-1797023590780930) | `GET` | Phân tích độ trùng lặp giữa tệp chuẩn và tối đa 4 tệp khác |

---

## Tổng quan Tệp đối tượng (`Audience`)
<a id="doc-1739940398505986"></a>
<!-- doc_id: 1739940398505986 -->

> Đường dẫn: API Reference > Audience

Tệp đối tượng (Audience) là một tùy chọn nhắm mục tiêu quảng cáo cho phép nhà quảng cáo TikTok For Business nhắm tới hoặc loại trừ người dùng cụ thể khi thiết lập quảng cáo:
- Để tìm hiểu thêm về phần giới thiệu và lợi ích của Audience API, hãy xem [Tổng quan](../09-marketing-api/audience.md#doc-1746998266963969).
- Để tìm hiểu về các loại đối tượng khác nhau, sự khác biệt giữa Customer File API và Streaming API, cũng như cách tạo và quản lý tệp đối tượng của bạn, hãy xem [Hướng dẫn](../09-marketing-api/audience.md#doc-1746998271267841).

Nhóm tài liệu này bao gồm các phần chính sau:
* [Tệp khách hàng (Customer file)](09-audience.md#doc-1739940501023746)
   - [Tải lên tệp đối tượng (Upload an audience file)](09-audience.md#doc-1739940567842818)
   - [Tạo tệp đối tượng từ tệp (Create an audience by file)](09-audience.md#doc-1739940570793985)
* [Phân đoạn đối tượng (Audience segment)](09-audience.md#doc-1739940504185857)
   - [Tạo/Xóa phân đoạn đối tượng (Create/Delete an audience segment)](09-audience.md#doc-1739940583739393)
   - [Ánh xạ phân đoạn đối tượng (Map audience segments)](09-audience.md#doc-1739940585975809)
* [Cập nhật tệp đối tượng (Update an audience)](09-audience.md#doc-1739940572667906)
* [Lấy danh sách tất cả tệp đối tượng (Get all audiences)](09-audience.md#doc-1739940506015746)
* [Lấy chi tiết tệp đối tượng (Get audience details)](09-audience.md#doc-1739940507792385)
* [Tạo tệp đối tượng theo quy tắc (Create an audience by rule)](09-audience.md#doc-1739940509849601)
* [Tạo tệp đối tượng tương tự (Create a lookalike audience)](09-audience.md#doc-1739940511844353)
* [Làm mới tệp đối tượng tương tự (Refresh a lookalike audience)](09-audience.md#doc-1758616888158209)
* [Xóa tệp đối tượng (Delete audiences)](09-audience.md#doc-1739940539757569)
* [Chia sẻ tệp đối tượng (Share audiences)](09-audience.md#doc-1740245803888706)
* [Hủy chia sẻ tệp đối tượng (Cancel the sharing of an audience)](09-audience.md#doc-1740245829978113)
* [Lấy nhật ký chia sẻ tệp đối tượng (Get the sharing log of an audience)](09-audience.md#doc-1740245827044354)
* [Áp dụng tệp đối tượng vào nhóm quảng cáo (Apply audiences to ad groups)](09-audience.md#doc-1758615097524225)
* [Lấy nhật ký áp dụng tệp đối tượng (Get the application log of audiences)](09-audience.md#doc-1758615737388033)
* [Đối tượng đã lưu (Saved Audience)](09-audience.md#doc-1780154462204930)
   - [Tạo đối tượng đã lưu (Create a Saved Audience)](09-audience.md#doc-1780154541898754)
   - [Lấy chi tiết đối tượng đã lưu (Get details of Saved Audiences)](09-audience.md#doc-1780154619404290)
   - [Xóa đối tượng đã lưu (Delete Saved Audiences)](09-audience.md#doc-1780154666312706)
* [Thông tin chuyên sâu về đối tượng (Audience Insights)](09-audience.md#doc-1797016417934337)
   - [Lấy chi tiết đối tượng tiềm năng (Get details of potential audiences)](09-audience.md#doc-1797016593782785)
   - [Lấy chi tiết trùng lặp đối tượng (Get details of audience overlap)](09-audience.md#doc-1797023590780930)

---

## Tệp khách hàng (`Customer File`)
<a id="doc-1739940501023746"></a>
<!-- doc_id: 1739940501023746 -->

> Đường dẫn: API Reference > Audience > Customer File

Customer File API là giải pháp API dựa trên tệp (file-based) cho phép bạn tạo tệp đối tượng tùy chỉnh từ dữ liệu khách hàng được tải lên. Để tìm hiểu thêm về Customer File API và cách phương thức này khác biệt so với Streaming API, hãy tham khảo [So sánh Customer File API và Streaming API](../09-marketing-api/audience.md#doc-1739566528222210).

Nhóm chức năng này gồm hai bước thực hiện chính:
* [Tải lên tệp đối tượng (Upload an audience file)](09-audience.md#doc-1739940567842818)
* [Tạo tệp đối tượng từ tệp (Create an audience by file)](09-audience.md#doc-1739940570793985)

---

## Tải lên tệp đối tượng (`Upload an audience file`)
<a id="doc-1739940567842818"></a>
<!-- doc_id: 1739940567842818 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/dmp/custom_audience/file/upload/`

**Mục đích**: Tải tệp dữ liệu khách hàng lên hệ thống TikTok. Sau khi tải lên thành công, hệ thống sẽ trả về một đường dẫn tệp duy nhất (`file_path`). Đường dẫn này sau đó được sử dụng để tạo hoặc cập nhật tệp đối tượng.

Tham khảo [Quy tắc chuẩn hóa định danh](../09-marketing-api/audience.md#doc-1850030360880129) để biết cách chuẩn hóa định danh trước khi mã hóa hash.

### Lưu ý quan trọng về tệp tải lên

Bảng dưới đây quy định chi tiết về giới hạn dung lượng (`Size`), định dạng (`Format`), phương thức mã hóa (`Encryption`) và cách thức tải lên tệp:

| Phân loại | Quy định chi tiết |
|---|---|
| `Size` (Giới hạn dung lượng) | Dung lượng tệp tải lên tối đa là **250MB**.<br>Các tệp vượt quá 250MB có thể được chia thành các tệp nhỏ hơn và tải lên riêng biệt. Sau đó, bạn có thể truyền danh sách tất cả các đường dẫn trong mảng `file_paths` khi tạo đối tượng bằng endpoint [Tạo tệp đối tượng từ tệp](09-audience.md#doc-1739940570793985). |
| `Format` (Định dạng tệp) | Chỉ hỗ trợ tệp định dạng `.csv` và `.txt` (phần mở rộng tệp phải chính xác là `.csv` hoặc `.txt`). |
| `Encryption` (Phương thức mã hóa) | Mã hóa bằng thuật toán MD5 hoặc SHA256 (khuyến nghị dùng SHA256).<br>Bạn bắt buộc phải sử dụng trường `calculate_type` để chỉ định phương thức mã hóa của tệp. Xem các giá trị enum tại [Enumeration - Encryption Type](../15-appendix/phu-luc-p1.md#doc-1737174886619138). Khi chọn `calculate_type` là `PHONE_SHA256`, số điện thoại phải được chuẩn hóa theo định dạng quốc tế E.164 trước khi hash (ví dụ: `+84912345678`). Dữ liệu băm SHA256 hợp lệ có độ dài 64 ký tự hex (gồm các chữ số 0-9 và chữ cái a-f, A-F). |
| Tải tệp chứa nhiều loại định danh | Bạn có thể tải lên tệp chứa một hoặc nhiều loại định danh ID.<br>Để tải lên tệp có nhiều loại định danh, `calculate_type` phải đặt là `MULTIPLE_TYPES` và tệp phải có dòng tiêu đề (header). Các tiêu đề hỗ trợ bao gồm: `MAID`, `phone_SHA256`, `email_SHA256`, `MAID_SHA256`, `MAID_MD5` (không phân biệt chữ hoa, chữ thường). Xem thêm các bước chi tiết tại [Create Customer File Audiences-Customer File API](../09-marketing-api/audience.md#doc-1747012327159809). |

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Bắt buộc | Access token đã được cấp quyền. Chi tiết xem tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| `Content-Type` | string | Bắt buộc | Định dạng nội dung gửi lên: `multipart/form-data`. |

### Tham số (POST: multipart/form-data)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | Bắt buộc | ID tài khoản quảng cáo. |
| `file` | file | Bắt buộc | Tệp dữ liệu cần tải lên. Chỉ hỗ trợ tệp CSV và TXT với đuôi tệp `.csv` hoặc `.txt`. |
| `file_signature` | string | Bắt buộc | Giá trị MD5 của toàn bộ tệp, dùng cho việc xác minh tính toàn vẹn dữ liệu ở phía máy chủ (server-side verification). |
| `calculate_type` | string | Bắt buộc | Phương thức mã hóa của dữ liệu. Giá trị của trường này phải khớp với nội dung thực tế của tệp, nếu không quá trình tải lên sẽ thất bại hoặc không thể tạo đối tượng hợp lệ. Xem chi tiết giá trị enum tại [Enumeration - Encryption Type](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Xem chi tiết tại [Appendix-Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi. |
| `request_id` | string | ID duy nhất định danh request. |
| `data` | object | Dữ liệu trả về. |
| ↳ `file_path` | string | Đường dẫn tệp duy nhất trên hệ thống TikTok, dùng để truyền vào `file_paths` khi tạo hoặc cập nhật tệp đối tượng. |

### Ví dụ gọi API

```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/dmp/custom_audience/file/upload/' \
--header 'Access-Token: your_access_token_here' \
--header 'Content-Type: multipart/form-data' \
--form 'advertiser_id="7000000000000000001"' \
--form 'file=@"/path/to/audience_data.csv"' \
--form 'file_signature="e10adc3949ba59abbe56e057f20f883e"' \
--form 'calculate_type="PHONE_SHA256"'
```

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20231023120000010188059082010",
  "data": {
    "file_path": "dmp/custom_audience/20231023/file_abc123def456.csv"
  }
}
```

---

## Tạo tệp đối tượng từ tệp (`Create an audience by file`)
<a id="doc-1739940570793985"></a>
<!-- doc_id: 1739940570793985 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/dmp/custom_audience/create/`

**Mục đích**: Tạo tệp đối tượng tùy chỉnh từ các tệp dữ liệu đã tải lên trước đó thông qua endpoint upload và thu được `file_path`.

Tham khảo [Quy tắc chuẩn hóa định danh](../09-marketing-api/audience.md#doc-1850030360880129) để biết cách chuẩn hóa các định danh trước khi hash.

### Lưu ý quan trọng và giới hạn

Bảng dưới đây tóm tắt các quy định về quy mô (`Size`), thời gian hiệu lực (`Audience` valid time), trạng thái đối tượng, thiết lập nhắm mục tiêu (`Targeting`) và endpoint liên quan (`Related`):

| Phân loại | Quy định chi tiết |
|---|---|
| `Size` limit | Mỗi tài khoản quảng cáo có thể tạo tối đa **400** tệp đối tượng. Nếu đã đạt giới hạn này, bạn cần xóa bớt đối tượng cũ trước khi tạo đối tượng mới (giới hạn ở cấp độ advertiser). |
| `Audience` valid time | Tệp đối tượng mới tạo cần tối đa **48 giờ** để hệ thống phân tích và xử lý trước khi chuyển sang trạng thái hoạt động (active). |
| Trạng thái đối tượng | Sử dụng endpoint [Lấy chi tiết tệp đối tượng](09-audience.md#doc-1739940507792385) để kiểm tra trạng thái hiện tại. Chỉ những đối tượng khả dụng (`is_valid` = `true`) mới có thể thao tác. Khi hết hạn, đối tượng sẽ chuyển sang không khả dụng (`is_valid` = `false`) và tự động bị gỡ khỏi mọi chiến dịch đang hoạt động. |
| `Targeting` setting | Nếu một chiến dịch không có thiết lập nhắm mục tiêu nào khác ngoài tệp đối tượng này, chiến dịch sẽ tự động bị tạm dừng nếu đối tượng mất hiệu lực. |
| `Related` endpoint | Nếu truyền nhầm `file_path` trong quá trình tạo đối tượng, bạn có thể chỉnh sửa lại thông qua endpoint [Cập nhật tệp đối tượng](09-audience.md#doc-1739940572667906). |

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Bắt buộc | Access token đã được cấp quyền. Chi tiết xem tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| `Content-Type` | string | Bắt buộc | Loại thông điệp request. Giá trị cho phép: `"application/json"`. |

### Tham số (POST: JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | Bắt buộc | ID tài khoản quảng cáo. |
| `custom_audience_name` | string | Bắt buộc | Tên tệp đối tượng. Độ dài tối đa 128 ký tự. |
| `audience_sub_type` | string | Không bắt buộc | Loại phụ của đối tượng, xác định loại hình quảng cáo có thể sử dụng.<br>Giá trị enum:<br>• `NORMAL`: Tệp đối tượng thông thường, dùng cho các quảng cáo không phải R&F (mặc định).<br>• `REACH_FREQUENCY`: Tệp đối tượng dùng riêng cho quảng cáo Tiếp cận & Tần suất (Reach & Frequency). |
| `file_paths` | string[] | Bắt buộc | Danh sách các đường dẫn tệp (`file_path`) đã tải lên thành công qua endpoint [Upload audience files](09-audience.md#doc-1739940567842818).<br>Khuyến nghị truyền **<50** đường dẫn mỗi request để đảm bảo tính ổn định. Bạn có thể sử dụng [/dmp/custom_audience/update/](09-audience.md#doc-1739940572667906) để bổ sung thêm tệp sau này. |
| `calculate_type` | string | Bắt buộc | Loại mã hóa. Giá trị `calculate_type` phải đồng nhất với tất cả các tệp trong mảng `file_paths`. Nếu không khớp, yêu cầu sẽ không trả về `custom_audience_id` hoặc tạo ra đối tượng không hợp lệ. Xem chi tiết giá trị enum tại [Enumeration - Encryption Type](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| `retention_in_days` | integer | Không bắt buộc | Số ngày duy trì tệp đối tượng. Khoảng giá trị: `[1, 365]`.<br>**Lưu ý**:<br>• Nếu truyền trường này, ngày hết hạn sẽ là số ngày retention tính từ ngày tạo đối tượng. Mọi thao tác cập nhật sau đó KHÔNG làm mới lại ngày hết hạn.<br>• Nếu không truyền, ngày hết hạn sẽ là 365 ngày tính từ lần cuối đối tượng được áp dụng vào nhóm quảng cáo đang hoạt động hoặc được sửa đổi. Thao tác áp dụng đối tượng vào nhóm quảng cáo hoạt động hoặc sửa đổi đối tượng sẽ đặt lại ngày hết hạn. Xem thêm tại bài viết Trợ giúp [Audience Expiration Policy](https://ads.tiktok.com/help/article/audience-expiration-policy?redirected=2). |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Xem chi tiết tại [Appendix-Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi. |
| `request_id` | string | ID duy nhất định danh request. |
| `data` | object | Dữ liệu trả về. |
| ↳ `custom_audience_id` | string | ID duy nhất của tệp đối tượng vừa tạo thành công. |

### Ví dụ gọi API

```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/dmp/custom_audience/create/' \
--header 'Access-Token: your_access_token_here' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id": "7000000000000000001",
    "custom_audience_name": "VIP_Customers_Q4",
    "file_paths": ["dmp/custom_audience/20231023/file_abc123def456.csv"],
    "calculate_type": "PHONE_SHA256",
    "retention_in_days": 180
}'
```

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20231023120000010188059082011",
  "data": {
    "custom_audience_id": "173994057079398501"
  }
}
```


---

## Phân đoạn đối tượng (`Audience segment`)
<a id="doc-1739940504185857"></a>
<!-- doc_id: 1739940504185857 -->

> Đường dẫn: API Reference > Audience > Audience segment

Streaming API (trước đây gọi là Segment API) được sử dụng để xây dựng các tệp đối tượng tùy chỉnh theo phân đoạn cho nhiều nhà quảng cáo cùng lúc, hỗ trợ cả dữ liệu bên thứ nhất (first-party) và dữ liệu bên thứ ba (third-party). Khi bạn có nhu cầu thông lượng cao (high throughput) hoặc muốn gửi dữ liệu theo luồng (stream data) theo từng lô (batch request) ngay khi có thông tin người dùng, bạn nên sử dụng nhóm API này. **Các công ty Đối tác Dữ liệu (Data Partner companies) bắt buộc phải sử dụng Streaming API.**

> [!NOTE]
> Để đăng ký quyền truy cập Streaming API, hãy sử dụng tính năng [Allowlist Management](https://ads.tiktok.com/marketing_api/blog/detail/7102266224578396162) trên TikTok Developer Portal và chọn "Streaming API" trong danh sách thả xuống. TikTok sẽ xem xét các đơn đăng ký theo định kỳ.

Để tìm hiểu thêm về Streaming API và sự khác biệt với Customer File API, hãy xem [So sánh Customer File API và Streaming API](../09-marketing-api/audience.md#doc-1739566528222210).

Nhóm chức năng này bao gồm hai endpoint:
* [Tạo/Xóa phân đoạn đối tượng (Create/Delete an audience segment)](09-audience.md#doc-1739940583739393)
* [Ánh xạ phân đoạn đối tượng (Map audience segments)](09-audience.md#doc-1739940585975809)

---

## Tạo hoặc xóa phân đoạn đối tượng (`Create/Delete an audience segment`)
<a id="doc-1739940583739393"></a>
<!-- doc_id: 1739940583739393 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/segment/audience/`

**Mục đích**: Tạo mới hoặc xóa một phân đoạn đối tượng (audience segment) trong Streaming API.

Vui lòng tham khảo [About Streaming API - Important Notes for Streaming API](../09-marketing-api/audience.md#doc-1739566528222210) để nắm rõ các lưu ý khi liên kết nhiều nhà quảng cáo với một Business Center và các phân đoạn kết hợp IDFA/AAID, cũng như [Quy tắc chuẩn hóa định danh](../09-marketing-api/audience.md#doc-1850030360880129) để chuẩn hóa định danh.

> [!NOTE]
> - **Giới hạn tần suất gọi (rate limit)**: 1 QPS cho mỗi tài khoản quảng cáo.
> - **Giới hạn số lượng**: Bạn có thể tạo tối đa **400** phân đoạn đối tượng cho mỗi tài khoản quảng cáo. Nếu đạt giới hạn này, bạn phải xóa bớt đối tượng cũ trước khi tạo mới (giới hạn ở cấp advertiser).
> - Để đăng ký quyền sử dụng Streaming API, truy cập [Allowlist Management](https://ads.tiktok.com/marketing_api/blog/detail/7102266224578396162) trên Developer Portal và chọn "Streaming API".

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Bắt buộc | Access token đã được cấp quyền. Chi tiết xem tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| `Content-Type` | string | Bắt buộc | Loại thông điệp request. Giá trị cho phép: `application/json`. |

### Tham số (POST: JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | Bắt buộc | ID tài khoản quảng cáo. |
| `action` | string | Bắt buộc | Thao tác cần thực hiện.<br>Giá trị enum:<br>• `create`: Tạo phân đoạn đối tượng. Bạn bắt buộc phải truyền kèm `custom_audience_name`.<br>• `delete`: Xóa phân đoạn đối tượng. Bạn bắt buộc phải truyền kèm `delete_audience_id`.<br>Giá trị mặc định nếu không truyền: `create`. |
| `custom_audience_name` | string | Điều kiện | Tên phân đoạn đối tượng cần tạo. Bắt buộc khi `action` là `create`. Tên dài hơn 70 ký tự sẽ tự động bị cắt gọn còn 67 ký tự và thêm dấu "...". |
| `delete_audience_id` | string | Điều kiện | ID của phân đoạn đối tượng cần xóa. Bắt buộc khi `action` là `delete`. |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Chi tiết xem tại [Appendix-Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi. |
| `request_id` | string | ID duy nhất định danh request. |
| `data` | object | Dữ liệu trả về. |
| ↳ `audience_id` | string | ID của phân đoạn đối tượng vừa tạo. Bạn sẽ sử dụng giá trị này khi thiết lập ánh xạ đối tượng qua endpoint mapping. |

### Ví dụ gọi API

```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/segment/audience/' \
--header 'Access-Token: your_access_token_here' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id": "7000000000000000001",
    "action": "create",
    "custom_audience_name": "Giay_nam_mua_thu"
}'
```

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20231023120000010188059082020",
  "data": {
    "audience_id": "173994058373939301"
  }
}
```

---

## Ánh xạ phân đoạn đối tượng (`Add/Delete audience segment mappings`)
<a id="doc-1739940585975809"></a>
<!-- doc_id: 1739940585975809 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/segment/mapping/`

**Mục đích**: Thêm hoặc xóa các ánh xạ định danh người dùng (UID/Device ID) vào một hoặc nhiều phân đoạn đối tượng theo lô.

Tham khảo [Quy tắc chuẩn hóa định danh](../09-marketing-api/audience.md#doc-1850030360880129) để biết cách chuẩn hóa định danh trước khi hash.

> [!NOTE]
> - **Cam kết chất lượng dịch vụ (SLA)**: Khi gọi API, bạn sẽ nhận được phản hồi ngay lập tức (success/error). Trong trường hợp thành công, hệ thống xử lý bất đồng bộ các ID với thời gian xử lý tối đa là **48 giờ**.
> - **Nhiều nhà quảng cáo trong cùng Business Center**: Bạn có thể dùng chung một access token để ánh xạ cùng một phân đoạn vào nhiều đối tượng thuộc các nhà quảng cáo khác nhau trong cùng một Business Center.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Bắt buộc | Access token đã được cấp quyền. Chi tiết xem tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| `Content-Type` | string | Bắt buộc | Loại thông điệp request. Định dạng cho phép: `application/json`. |

### Tham số (POST: JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_ids` | string[] | Bắt buộc | Danh sách ID nhà quảng cáo để tạo hoặc xóa ánh xạ phân đoạn. Tất cả các `advertiser_id` phải cùng thuộc một tài khoản Business Center. |
| `action` | string | Không bắt buộc | Loại thao tác thực hiện.<br>Giá trị enum:<br>• `add`: Thêm UID vào một hoặc nhiều tệp đối tượng.<br>• `delete`: Xóa UID khỏi một hoặc nhiều tệp đối tượng.<br>Giá trị mặc định: `add`.<br>**Ghi chú**: UID bao gồm:<br>• Mã định danh thiết bị đã băm (`id_type` = `IDFA_MD5`, `AAID_MD5`, `IDFA_SHA256` hoặc `AAID_SHA256`).<br>• Định danh người dùng bên ngoài đã băm như email hoặc số điện thoại (`id_type` = `EMAIL_SHA256`, `PHONE_SHA256`). |
| `id_schema` | string[] | Bắt buộc | Danh sách các loại định danh ID được dùng để tạo đối tượng.<br>Giá trị cho phép:<br>• `IDFA_MD5`: Mã MD5 của Apple IDFA trên iOS.<br>• `AAID_MD5`: Mã MD5 của Google AAID/GAID trên Android.<br>• `IDFA_SHA256`: Mã SHA256 của iOS IDFA.<br>• `AAID_SHA256`: Mã SHA256 của Android AAID/GAID.<br>• `EMAIL_SHA256`: Mã SHA256 của địa chỉ email đã chuẩn hóa.<br>• `PHONE_SHA256`: Mã SHA256 của số điện thoại chuẩn E.164 (ví dụ: `+84912345678`).<br>**Lưu ý**: Không được truyền trùng lặp loại ID. Các loại ID có thể cung cấp theo thứ tự bất kỳ và chấp nhận cả chữ thường. |
| `batch_data` | object[][] | Bắt buộc | Mảng lồng nhau chứa dữ liệu người dùng/thiết bị và danh sách `audience_ids` tương ứng. Dùng để thêm hoặc xóa nhiều ánh xạ ID cùng lúc. |
| ↳ `id` | string | Bắt buộc | Chuỗi định danh đã băm của người dùng hoặc thiết bị (tương ứng với loại trong `id_schema`). |
| ↳ `audience_ids` | string[] | Bắt buộc | Mảng các `audience_id` để thêm hoặc xóa ánh xạ. Các audience ID này phải thuộc về ít nhất một nhà quảng cáo trong `advertiser_ids`. Bạn có thể lấy `audience_id` thông qua [/segment/audience/](09-audience.md#doc-1739940583739393). |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Chi tiết xem tại [Appendix-Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi. |
| `request_id` | string | ID duy nhất định danh request. |
| `data` | object | Dữ liệu trả về (mảng rỗng `{}`). |

### Ví dụ gọi API

```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/segment/mapping/' \
--header 'Access-Token: your_access_token_here' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_ids": ["7000000000000000001"],
    "action": "add",
    "id_schema": ["PHONE_SHA256"],
    "batch_data": [
        [
            {
                "id": "a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3",
                "audience_ids": ["173994058373939301"]
            }
        ]
    ]
}'
```

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20231023120000010188059082021",
  "data": {}
}
```

---

## Cập nhật tệp đối tượng (`Update an audience`)
<a id="doc-1739940572667906"></a>
<!-- doc_id: 1739940572667906 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/dmp/custom_audience/update/`

**Mục đích**: Cập nhật thông tin của tệp đối tượng như đổi tên, chuyển đổi phân loại hoặc chỉnh sửa tệp dữ liệu khách hàng (Customer File).

TikTok API for Business hỗ trợ 3 thao tác chỉnh sửa dữ liệu đối với tệp khách hàng:
1. `REPLACE`: Thay thế toàn bộ các tệp dữ liệu cũ bằng tệp mới.
2. `APPEND`: Bổ sung thêm tệp dữ liệu mới (chỉ thêm các dữ liệu chưa từng xuất hiện).
3. `REMOVE`: Loại bỏ các định danh có trong tệp dữ liệu tải lên khỏi tệp đối tượng hiện tại.

### Lưu ý quan trọng và giới hạn

Bảng dưới đây quy định chi tiết về hạn ngạch (`Quota`), xử lý đa nhiệm (Multitasking), phạm vi hỗ trợ (`Supported`) và cam kết thời gian (`SLA`):

| Phân loại | Quy định chi tiết |
|---|---|
| `Quota` (Hạn ngạch) | • Mỗi tệp đối tượng có hạn ngạch tối đa **24 thao tác cập nhật** (Append, Remove, Replace) trong mỗi 24 giờ liên tục (giới hạn ở cấp audience).<br>• Chỉ được phép thực hiện tối đa **1 thao tác `REPLACE`** cho tệp đối tượng dựa trên tệp mỗi ngày. |
| Multitasking (Đa nhiệm) | • Vui lòng chờ cho đến khi thao tác hiện tại trên tệp đối tượng hoàn tất trước khi thử lại.<br>• Thao tác `REPLACE` sẽ bị từ chối nếu đang có một thao tác `REPLACE` khác chưa hoàn thành. |
| `Supported` scope (Phạm vi hỗ trợ) | • Chỉ tệp đối tượng khách hàng (Customer File) mới hỗ trợ thay đổi tệp dữ liệu qua `file_paths`.<br>• Các loại tệp đối tượng tương tác (Engagement), hành vi ứng dụng (App Activity), lưu lượng website (Website Traffic) và đối tượng tương tự (Lookalike) chỉ hỗ trợ cập nhật tên đối tượng (`custom_audience_name`).<br>• Đối tượng sắp hết hạn (`is_expiring` = `true`) hoặc đã hết hạn không thể sửa đổi mà chỉ có thể xóa.<br>• Các thao tác `REPLACE`, `APPEND`, và `REMOVE` sẽ thất bại nếu quy mô tệp đối tượng sau thao tác nhỏ hơn **1.000** người dùng.<br>• Thao tác `REMOVE`: Không được phép xóa toàn bộ dữ liệu tệp (không thể làm rỗng đối tượng). |
| `SLA` (Thời gian xử lý) | Sau khi gửi request, bạn sẽ nhận phản hồi thành công/thất bại ngay lập tức. Nếu thành công, hệ thống xử lý ID bất đồng bộ với thời gian cam kết SLA tối đa là **48 giờ**. |

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Bắt buộc | Access token đã được cấp quyền. Chi tiết xem tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| `Content-Type` | string | Bắt buộc | Loại thông điệp request. Giá trị cho phép: `"application/json"`. |

### Tham số (POST: JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | Bắt buộc | ID tài khoản quảng cáo. |
| `custom_audience_id` | string | Bắt buộc | ID tệp đối tượng tùy chỉnh cần cập nhật. |
| `custom_audience_name` | string | Điều kiện | Tên mới cho tệp đối tượng. Độ dài tối đa 128 ký tự. Bạn bắt buộc phải truyền trường này hoặc `file_paths`. |
| `audience_sub_type` | string | Không bắt buộc | Loại phụ của tệp đối tượng. Giá trị enum cho phép: `REACH_FREQUENCY` (cho phép đối tượng được dùng trong các chiến dịch Tiếp cận & Tần suất Reach & Frequency). Lưu ý: Chỉ có thể nâng cấp từ `NORMAL` sang `REACH_FREQUENCY`, không thể chuyển ngược lại. Nếu cập nhật trường này, các thay đổi khác sẽ bị bỏ qua. Không thể chuyển đối tượng Lookalike sang `REACH_FREQUENCY`. |
| `file_paths` | string[] | Điều kiện | Danh sách tệp tải lên để cập nhật tệp đối tượng Customer File. Bạn phải truyền trường này hoặc `custom_audience_name`. Khuyến nghị `<50` tệp mỗi request. Phương thức mã hóa của tệp phải đồng nhất với tệp ban đầu của đối tượng. |
| `action` | string | Không bắt buộc | Loại thao tác sửa đổi khi truyền `file_paths`.<br>Giá trị enum:<br>• `APPEND`: Thêm tệp để mở rộng đối tượng (chỉ dữ liệu chưa có mới được thêm).<br>• `REMOVE`: Loại bỏ dữ liệu trùng với tệp mới khỏi đối tượng.<br>• `REPLACE`: Thay thế toàn bộ dữ liệu ban đầu bằng dữ liệu mới.<br>Giá trị mặc định: `REPLACE`.<br>**Lưu ý**: Các thao tác sẽ thất bại nếu số người dùng còn lại sau thao tác nhỏ hơn 1.000. |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Xem chi tiết tại [Appendix-Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi. |
| `request_id` | string | ID duy nhất định danh request. |
| `data` | object | Dữ liệu trả về. |
| ↳ `custom_audience_id` | string | ID tệp đối tượng vừa được cập nhật. |

### Ví dụ gọi API

```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/dmp/custom_audience/update/' \
--header 'Access-Token: your_access_token_here' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id": "7000000000000000001",
    "custom_audience_id": "173994057079398501",
    "action": "APPEND",
    "file_paths": ["dmp/custom_audience/20231023/file_new_users.csv"]
}'
```

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20231023120000010188059082022",
  "data": {
    "custom_audience_id": "173994057079398501"
  }
}
```


---

## Lấy danh sách tệp đối tượng (`Get all audiences`)
<a id="doc-1739940506015746"></a>
<!-- doc_id: 1739940506015746 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/dmp/custom_audience/list/`

**Mục đích**: Lấy danh sách tệp đối tượng tùy chỉnh thuộc tài khoản quảng cáo, kèm theo thông tin tổng quan, trạng thái hiệu lực và phân trang.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Bắt buộc | Access token đã được cấp quyền. Chi tiết xem tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (GET: query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | Bắt buộc | ID tài khoản quảng cáo. |
| `custom_audience_ids` | string[] | Không bắt buộc | Danh sách các ID tệp đối tượng cần lọc dưới dạng chuỗi JSON mã hóa URL (ví dụ: `["123456"]`). Tối đa 100 ID. Nếu không truyền, hệ thống sẽ trả về tất cả các đối tượng của tài khoản quảng cáo. |
| `page` | number | Không bắt buộc | Số trang hiện tại trong phân trang. Giá trị mặc định: `1`. |
| `page_size` | number | Không bắt buộc | Số lượng bản ghi trên mỗi trang. Giá trị mặc định: `10`. Khoảng giá trị: `[1, 100]`. |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Chi tiết xem tại [Appendix-Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi. |
| `request_id` | string | ID duy nhất định danh request. |
| `data` | object | Dữ liệu trả về. |
| ↳ `page_info` | object | Thông tin phân trang. |
| ↳↳ `page` | number | Số trang hiện tại. |
| ↳↳ `page_size` | number | Số bản ghi trên mỗi trang. |
| ↳↳ `total_page` | number | Tổng số trang. |
| ↳↳ `total_number` | number | Tổng số bản ghi tìm thấy. |
| ↳ `list` | object[] | Danh sách tệp đối tượng. |
| ↳↳ `audience_id` | string | ID tệp đối tượng. |
| ↳↳ `name` | string | Tên tệp đối tượng. |
| ↳↳ `type` | string | Loại đối tượng (ví dụ: `Customer File`, `Lookalike Audience`, `Rule App`, v.v.). |
| ↳↳ `audience_sub_type` | string | Phân loại phụ (`NORMAL` hoặc `REACH_FREQUENCY`). |
| ↳↳ `is_valid` | boolean | Trạng thái đối tượng có khả dụng hay không. |
| ↳↳ `cover_num` | number | Số người dùng TikTok phù hợp được bao phủ trong tệp đối tượng. |
| ↳↳ `is_creator` | boolean | Nhà quảng cáo này có phải là người tạo ra tệp đối tượng hay không. |
| ↳↳ `is_expiring` | boolean | Tệp đối tượng có đang sắp hết hạn hay không. |
| ↳↳ `expired_time` | string | Thời điểm hết hạn của đối tượng. |
| ↳↳ `create_time` | string | Thời điểm tạo đối tượng. |
| ↳↳ `shared` | boolean | Đối tượng có đang được chia sẻ hay không. |

### Ví dụ

#### cURL
```bash
curl -G --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/dmp/custom_audience/list/' \
--header 'Access-Token: your_access_token_here' \
--data-urlencode 'advertiser_id=7000000000000000001' \
--data-urlencode 'page=1' \
--data-urlencode 'page_size=10'
```

#### Python
```python
import requests

ACCESS_TOKEN = "your_access_token_here"
ADVERTISER_ID = "7000000000000000001"

url = "https://business-api.tiktok.com/open_api/v1.3/dmp/custom_audience/list/"
headers = {"Access-Token": ACCESS_TOKEN}
params = {
    "advertiser_id": ADVERTISER_ID,
    "page": 1,
    "page_size": 10
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20231023120000010188059082030",
  "data": {
    "page_info": {
      "page": 1,
      "page_size": 10,
      "total_page": 1,
      "total_number": 1
    },
    "list": [
      {
        "audience_id": "173994057079398501",
        "name": "VIP_Customers_Q4",
        "type": "Customer File",
        "audience_sub_type": "NORMAL",
        "is_valid": true,
        "cover_num": 125000,
        "is_creator": true,
        "is_expiring": false,
        "expired_time": "2024-04-20 12:00:00",
        "create_time": "2023-10-23 12:00:00",
        "shared": false
      }
    ]
  }
}
```

---

## Lấy chi tiết tệp đối tượng (`Get audience details`)
<a id="doc-1739940507792385"></a>
<!-- doc_id: 1739940507792385 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/dmp/custom_audience/get/`

**Mục đích**: Lấy thông tin chi tiết đầy đủ của một hoặc nhiều tệp đối tượng, bao gồm quy tắc cấu hình, thông số Lookalike và lịch sử thao tác chỉnh sửa.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Bắt buộc | Access token đã được cấp quyền. Chi tiết xem tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (GET: query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | Bắt buộc | ID tài khoản quảng cáo. |
| `custom_audience_ids` | string[] | Bắt buộc | Danh sách các ID tệp đối tượng cần lấy chi tiết (dạng mảng JSON được URL-encode, ví dụ: `["123456","789012"]`). Tối đa 100 ID. |
| `history_size` | number | Không bắt buộc | Số lượng bản ghi lịch sử chỉnh sửa tối đa muốn nhận về cho mỗi đối tượng. Giá trị mặc định: `10`. Khoảng giá trị: `[1, 20]`. |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Chi tiết xem tại [Appendix-Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi. |
| `request_id` | string | ID duy nhất định danh request. |
| `data` | object | Dữ liệu trả về. |
| ↳ `list` | object[] | Danh sách chi tiết các đối tượng. |
| ↳↳ `audience_details` | object | Chi tiết thông số của tệp đối tượng. |
| ↳↳↳ `audience_id` | string | ID tệp đối tượng. |
| ↳↳↳ `name` | string | Tên tệp đối tượng. |
| ↳↳↳ `type` | string | Loại đối tượng (Customer File, Lookalike Audience, Rule Engagement...). |
| ↳↳↳ `audience_sub_type` | string | Phân loại phụ (`NORMAL` hoặc `REACH_FREQUENCY`). |
| ↳↳↳ `cover_num` | number | Quy mô bao phủ số lượng người dùng TikTok khớp được. |
| ↳↳↳ `is_valid` | boolean | Trạng thái tệp đối tượng có sẵn sàng hoạt động hay không. |
| ↳↳↳ `is_creator` | boolean | Người gọi có phải là chủ sở hữu tạo ra đối tượng hay không. |
| ↳↳↳ `is_expiring` | boolean | Có sắp hết hạn hay không. |
| ↳↳↳ `expired_time` | string | Thời điểm hết hạn của đối tượng. |
| ↳↳↳ `is_auto_refresh` | boolean | Có bật tính năng tự động làm mới theo chu kỳ hay không. |
| ↳↳↳ `rule` | string | Chuỗi JSON chứa quy tắc đối tượng (đối với đối tượng Rule). |
| ↳↳↳ `lookalike_spec` | object | Cấu hình đối tượng tương tự (chỉ trả về khi loại là Lookalike Audience). |
| ↳↳↳↳ `source_audience_id` | string | ID tệp đối tượng hạt giống (seed). |
| ↳↳↳↳ `include_source` | boolean | Có bao gồm đối tượng hạt giống trong đối tượng Lookalike hay không. |
| ↳↳↳↳ `mobile_os` | string | Hệ điều hành mục tiêu (`ALL`, `ANDROID`, `IOS`). |
| ↳↳↳↳ `placements` | string | Vị trí phân phối quảng cáo (`TikTok`, `Pangle`...). |
| ↳↳↳↳ `location_ids` | string[] | Danh sách ID vị trí địa lý mục tiêu. |
| ↳↳↳↳ `audience_size` | string | Mức độ mở rộng quy mô (`NARROW`, `BALANCED`, `BROAD`). |
| ↳↳ `audience_history` | object[] | Danh sách lịch sử các thao tác chỉnh sửa đối tượng. |
| ↳↳↳ `action` | string | Thao tác đã thực hiện (xem bảng ánh xạ bên dưới). |
| ↳↳↳ `action_detail` | string | Kết quả chi tiết của thao tác. |
| ↳↳↳ `editor` | string | Tác nhân thực hiện (giá trị là `"open_api"` nếu thao tác qua API). |
| ↳↳↳ `msg` | string | Thông báo chi tiết (nếu có lỗi một phần). |
| ↳↳↳ `opt_time` | string | Thời gian thực hiện thao tác (định dạng `YYYY-MM-DD HH:mm:ss`). |

#### Ánh xạ giữa giá trị `action` trong lịch sử và thao tác API

| Giá trị `action` | Mô tả thao tác | Thao tác tương ứng qua `/dmp/custom_audience/update/` |
|---|---|---|
| `modify` | Đã đổi tên tệp đối tượng tùy chỉnh | Truyền `custom_audience_name` |
| `upload - replace` | Đã tải lên tệp thay thế dữ liệu tệp khách hàng | Truyền `file_paths` và `action` là `REPLACE` (hoặc không truyền) |
| `upload - add` | Đã tải lên tệp bổ sung dữ liệu tệp khách hàng | Truyền `file_paths` và `action` là `APPEND` |
| `upload remove` | Đã tải lên tệp loại bỏ dữ liệu tệp khách hàng | Truyền `file_paths` và `action` là `REMOVE` |
| `convert_to_rf` | Đã kích hoạt đối tượng dùng cho chiến dịch Reach & Frequency | Truyền `audience_sub_type` là `REACH_FREQUENCY` |

### Ví dụ

#### cURL
```bash
curl -G --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/dmp/custom_audience/get/' \
--header 'Access-Token: your_access_token_here' \
--data-urlencode 'advertiser_id=7000000000000000001' \
--data-urlencode 'custom_audience_ids=["173994057079398501"]' \
--data-urlencode 'history_size=5'
```

#### Python
```python
import json
import requests

ACCESS_TOKEN = "your_access_token_here"
ADVERTISER_ID = "7000000000000000001"

url = "https://business-api.tiktok.com/open_api/v1.3/dmp/custom_audience/get/"
headers = {"Access-Token": ACCESS_TOKEN}
params = {
    "advertiser_id": ADVERTISER_ID,
    "custom_audience_ids": json.dumps(["173994057079398501"]),
    "history_size": 5
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20231023120000010188059082031",
  "data": {
    "list": [
      {
        "audience_details": {
          "audience_id": "173994057079398501",
          "name": "VIP_Customers_Q4",
          "type": "Customer File",
          "audience_sub_type": "NORMAL",
          "cover_num": 125000,
          "is_valid": true,
          "is_creator": true,
          "is_expiring": false,
          "expired_time": "2024-04-20 12:00:00",
          "create_time": "2023-10-23 12:00:00"
        },
        "audience_history": [
          {
            "action": "create",
            "action_detail": "125000",
            "editor": "open_api",
            "msg": null,
            "opt_time": "2023-10-23 12:00:00"
          }
        ]
      }
    ]
  }
}
```

---

## Tạo tệp đối tượng theo quy tắc (`Create an audience by rule`)
<a id="doc-1739940509849601"></a>
<!-- doc_id: 1739940509849601 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/dmp/custom_audience/rule/create/`

**Mục đích**: Tạo tệp đối tượng dựa trên các quy tắc tương tác hoặc hành vi người dùng (quảng cáo, video tự nhiên, livestream, sự kiện ứng dụng, pixel website, biểu mẫu lead, tài khoản doanh nghiệp hoặc sự kiện offline). Bạn cần xác định tập hợp quy tắc bao gồm (`inclusion_rule_set`) và tùy chọn thêm quy tắc loại trừ (`exclusion_rule_set`).

> [!NOTE]
> - Tệp đối tượng mới tạo cần tối đa **48 giờ** để hệ thống phân tích và kích hoạt sẵn sàng hoạt động.
> - Sử dụng [/dmp/custom_audience/get/](09-audience.md#doc-1739940507792385) để kiểm tra trạng thái hoạt động. Chỉ những đối tượng khả dụng (`is_valid` = `true`) mới có thể thao tác.
> - Khi hết hạn, đối tượng chuyển sang `Unavailable` (`is_valid` = `false`) và tự động bị gỡ khỏi chiến dịch đang chạy. Nếu chiến dịch chỉ nhắm mục tiêu vào tệp đối tượng này, chiến dịch sẽ bị tạm dừng.

### So sánh phiên bản v1.2 và v1.3

Bảng so sánh chi tiết các thay đổi giữa hai phiên bản API:

| Changes | v1.2 | v1.3 |
|---|---|---|
| Endpoint path | `/v1.2/dmp/custom_audience/rule/create/` | `/v1.3/dmp/custom_audience/rule/create/` |
| Request parameter data type | `advertiser_id`: number<br>`is_auto_refresh`: number | `advertiser_id`: string<br>`is_auto_refresh`: boolean |
| New request parameters | Không có | `retention_in_days`<br>`identity_id`<br>`identity_type`<br>`identity_authorized_bc_id`<br>`parameter_filters` (gồm tất cả các tham số bên trong mảng đối tượng) |
| Response parameter data type | `custom_audience_id`: number | `custom_audience_id`: string |

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Bắt buộc | Access token đã được cấp quyền. Chi tiết xem tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| `Content-Type` | string | Bắt buộc | Loại thông điệp request. Giá trị cho phép: `"application/json"`. |

### Tham số (POST: JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | Bắt buộc | ID tài khoản quảng cáo. |
| `custom_audience_name` | string | Bắt buộc | Tên tệp đối tượng. Giới hạn độ dài tối đa 128 ký tự. |
| `audience_type` | string | Bắt buộc | Loại tệp đối tượng quy tắc.<br>Giá trị enum:<br>• `ENGAGEMENT`: Đối tượng tương tác quảng cáo (asset type là ad group).<br>• `ENGAGEMENT_ORGANIC_VIDEO`: Đối tượng tương tác video tự nhiên (public video).<br>• `ENGAGEMENT_LIVE_VIDEO`: Đối tượng tương tác video livestream.<br>• `APP`: Đối tượng hành vi trong ứng dụng (App Activity).<br>• `PIXEL`: Đối tượng lưu lượng truy cập website qua Pixel (Website Traffic).<br>• `LEAD_GENERATION`: Đối tượng tương tác biểu mẫu khách hàng tiềm năng.<br>• `BUSINESS_ACCOUNT`: Đối tượng tương tác tài khoản TikTok doanh nghiệp.<br>• `TIKTOK_SHOP`: Đối tượng hoạt động TikTok Shop.<br>• `OFFLINE`: Đối tượng hoạt động ngoại tuyến (Offline Event). |
| `audience_sub_type` | string | Không bắt buộc | Loại phụ của đối tượng.<br>Giá trị enum:<br>• `NORMAL`: Dùng cho quảng cáo thông thường không phải Reach & Frequency (mặc định).<br>• `REACH_FREQUENCY`: Dùng riêng cho chiến dịch Reach & Frequency. |
| `retention_in_days` | integer | Không bắt buộc | Số ngày duy trì tệp đối tượng. Khoảng giá trị: `[1, 365]`.<br>• Nếu truyền trường này, ngày hết hạn sẽ tính cố định từ ngày tạo đối tượng và không thể đặt lại.<br>• Nếu không truyền, ngày hết hạn sẽ là 365 ngày tính từ lần cuối đối tượng được áp dụng vào nhóm quảng cáo đang chạy hoặc chỉnh sửa. |
| `is_auto_refresh` | boolean | Không bắt buộc | Có bật tính năng tự động làm mới đối tượng theo chu kỳ hay không.<br>Giá trị hỗ trợ: `true`, `false`. Mặc định: `true`. Khi bật, đối tượng sẽ tự động nạp dữ liệu người dùng mới nhất dựa trên cửa sổ quan sát (lookback window). |
| `identity_id` | string | Điều kiện | Bắt buộc khi `audience_type` là `ENGAGEMENT_LIVE_VIDEO` hoặc `ENGAGEMENT_ORGANIC_VIDEO`. ID danh tính (Identity ID). |
| `identity_type` | string | Điều kiện | Bắt buộc khi `audience_type` là `ENGAGEMENT_LIVE_VIDEO` hoặc `ENGAGEMENT_ORGANIC_VIDEO`. Loại danh tính. Enum: `TT_USER`, `BC_AUTH_TT`. |
| `identity_authorized_bc_id` | string | Điều kiện | Bắt buộc khi `identity_type` là `BC_AUTH_TT`. ID Business Center mà tài khoản người dùng TikTok được liên kết. |
| `rule_spec` | object | Bắt buộc | Cấu trúc quy tắc định nghĩa tệp đối tượng. |
| ↳ `inclusion_rule_set` | object | Bắt buộc | Tập hợp các quy tắc bao gồm (Inclusion rules). |
| ↳↳ `operator` | string | Bắt buộc | Toán tử kết hợp giữa các quy tắc con trong tập quy tắc bao gồm. Giá trị enum: `OR`. |
| ↳↳ `rules` | object[] | Bắt buộc | Danh sách các quy tắc con trong tập quy tắc bao gồm. |
| ↳↳↳ `event_source_ids` | string[] | Điều kiện | Bắt buộc khi `audience_type` không phải là `ENGAGEMENT` hoặc `LEAD_GENERATION`. Danh sách ID nguồn sự kiện:<br>• Với Engagement: ID nhóm quảng cáo (nếu bỏ trống, áp dụng cho tất cả).<br>• Với Organic Engagement: ID bài đăng video TikTok (tối đa 10 ID, lấy qua [/identity/video/get/](46-identity.md#doc-1740218475032577)).<br>• Với Live Engagement: ID video livestream (tối đa 10 ID, lấy qua [/identity/live/get/](46-identity.md#doc-1785238052792321)).<br>• Với App Activity: App ID.<br>• Với Website Traffic (Pixel): Pixel ID.<br>• Với Business Account: User ID nòng cốt (lấy qua **/user/info/**).<br>• Với Shop Activity: TikTok Shop ID (lấy qua [/store/list/](69-tiktok-store.md#doc-1752267762718722)).<br>• Với Offline: Offline Event set ID (lấy qua [/offline/get/](43-events-1-0-p1.md#doc-1765596808589313)).<br>• Với Lead Generation: **Không truyền** trường này. |
| ↳↳↳ `retention_days` | number | Bắt buộc | Cửa sổ quan sát (lookback window) tính bằng ngày. Xem enum tại [Enumerations - Lookback window](../15-appendix/phu-luc-p1.md#doc-1737174886619138). Lưu ý: Với `BUSINESS_ACCOUNT` (nếu hành vi không phải theo dõi trang), hoặc `ENGAGEMENT_LIVE_VIDEO`, `ENGAGEMENT_ORGANIC_VIDEO`, `retention_days` phải là `7`, `14` hoặc `30`. |
| ↳↳↳ `filter_set` | object | Bắt buộc | Tập bộ lọc điều kiện cho mỗi quy tắc bao gồm. |
| ↳↳↳↳ `operator` | string | Bắt buộc | Toán tử kết hợp bộ lọc. Giá trị enum: `OR`. |
| ↳↳↳↳ `filters` | object[] | Bắt buộc | Mảng bộ lọc hành vi trước đây của đối tượng và tùy chọn theo từ khóa URL/tham số. Tối đa 1 phần tử. |
| ↳↳↳↳↳ `field` | string | Bắt buộc | Trường lọc. Giá trị enum: `EVENT` (bao gồm những người đã thực hiện hành vi trong khoảng thời gian `retention_days`). |
| ↳↳↳↳↳ `operator` | string | Bắt buộc | Toán tử lọc giữa trường và giá trị. Giá trị enum: `EQ` (bằng). |
| ↳↳↳↳↳ `value` | string | Bắt buộc | Giá trị hành vi cụ thể. Xem chi tiết tại [Enumeration - Filter Value](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳↳↳↳↳ `parameter_filters` | object[] | Không bắt buộc | Danh sách bộ lọc trên từ khóa URL hoặc tham số sự kiện Web reported qua Pixel (xem [Web Event parameters reported via the Pixel](../09-marketing-api/do-luong-quang-cao-tom-tat.md#doc-1739585702922241)). Tối đa 1 bộ lọc URL và 10 bộ lọc tham số. Kết hợp với bộ lọc hành vi theo logic AND. |
| ↳↳↳↳↳↳ `field` | string | Điều kiện | Trường tham số cần lọc. Enum: `URL`, `CONTENT_TYPE`, `PRICE`, `VALUE`, `CONTENT_ID`, `CONTENT_CATEGORY`. |
| ↳↳↳↳↳↳ `operator` | string | Điều kiện | Toán tử so sánh. Với `URL`: `CONTAINS`, `DOES_NOT_CONTAIN`, `EQ`, `NOT_EQUAL`. Với các trường khác: hỗ trợ thêm `IS_LESS_THAN`, `IS_GREATER_THAN`, `IS_LESS_THAN_OR_EQUAL_TO`, `IS_GREATER_THAN_OR_EQUAL_TO`. |
| ↳↳↳↳↳↳ `values` | string[] | Điều kiện | Danh sách giá trị lọc. Tối đa 10 giá trị, mỗi giá trị tối đa 100 ký tự. Kết hợp bằng logic OR. |
| ↳ `exclusion_rule_set` | object | Không bắt buộc | Tập hợp các quy tắc loại trừ (Exclusion rules). Cấu trúc tương tự `inclusion_rule_set`. |
| ↳↳ `operator` | string | Điều kiện | Bắt buộc khi có `exclusion_rule_set`. Toán tử kết hợp giữa các quy tắc loại trừ. Enum: `OR`. |
| ↳↳ `rules` | object[] | Điều kiện | Danh sách các quy tắc con loại trừ. |
| ↳↳↳ `event_source_ids` | string[] | Điều kiện | Danh sách ID nguồn sự kiện cần loại trừ. |
| ↳↳↳ `retention_days` | number | Điều kiện | Cửa sổ quan sát tính bằng ngày đối với quy tắc loại trừ. |
| ↳↳↳ `filter_set` | object | Điều kiện | Tập bộ lọc điều kiện loại trừ. |
| ↳↳↳↳ `operator` | string | Điều kiện | Toán tử kết hợp. Enum: `OR`. |
| ↳↳↳↳ `filters` | object[] | Điều kiện | Mảng bộ lọc hành vi loại trừ. |
| ↳↳↳↳↳ `field` | string | Điều kiện | Trường lọc (`EVENT`). |
| ↳↳↳↳↳ `operator` | string | Điều kiện | Toán tử (`EQ`). |
| ↳↳↳↳↳ `value` | string | Điều kiện | Giá trị sự kiện loại trừ. |
| ↳↳↳↳↳ `parameter_filters` | object[] | Điều kiện | Bộ lọc bổ sung cho sự kiện loại trừ. |
| ↳↳↳↳↳↳ `field` | string | Điều kiện | Tên trường lọc. |
| ↳↳↳↳↳↳ `operator` | string | Điều kiện | Toán tử so sánh. |
| ↳↳↳↳↳↳ `values` | string[] | Điều kiện | Danh sách giá trị lọc loại trừ. |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Chi tiết xem tại [Appendix-Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi. |
| `request_id` | string | ID duy nhất định danh request. |
| `data` | object | Dữ liệu trả về. |
| ↳ `custom_audience_id` | string | ID tệp đối tượng vừa được tạo. |

### Ví dụ gọi API

```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/dmp/custom_audience/rule/create/' \
--header 'Access-Token: your_access_token_here' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id": "7000000000000000001",
    "custom_audience_name": "Pixel_Purchase_30D",
    "audience_type": "PIXEL",
    "rule_spec": {
        "inclusion_rule_set": {
            "operator": "OR",
            "rules": [
                {
                    "event_source_ids": ["7100000000000000001"],
                    "retention_days": 30,
                    "filter_set": {
                        "operator": "OR",
                        "filters": [
                            {
                                "field": "EVENT",
                                "operator": "EQ",
                                "value": "PIXEL COMPLETE PAYMENT"
                            }
                        ]
                    }
                }
            ]
        }
    }
}'
```

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20231023120000010188059082032",
  "data": {
    "custom_audience_id": "173994050984960101"
  }
}
```


---

## Tạo tệp đối tượng tương tự (`Create a lookalike audience`)
<a id="doc-1739940511844353"></a>
<!-- doc_id: 1739940511844353 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/dmp/custom_audience/lookalike/create/`

**Mục đích**: Tạo tệp đối tượng tương tự (Lookalike Audience) dựa trên một tệp đối tượng hạt giống (seed/source audience) đã có sẵn trong tài khoản quảng cáo của bạn.

> [!NOTE]
> - Tệp đối tượng mới tạo cần tối đa **48 giờ** để hệ thống phân tích và xử lý trước khi kích hoạt sẵn sàng hoạt động.
> - Sử dụng endpoint [/dmp/custom_audience/get/](09-audience.md#doc-1739940507792385) để kiểm tra trạng thái. Chỉ những đối tượng khả dụng (`is_valid` = `true`) mới có thể thao tác.
> - Quy mô tệp đối tượng nguồn (source audience) phải có ít nhất **100** người dùng.

### So sánh phiên bản v1.2 và v1.3

| Changes | v1.2 | v1.3 |
|---|---|---|
| Endpoint path | `/v1.2/dmp/custom_audience/lookalike/create/` | `/v1.3/dmp/custom_audience/lookalike/create/` |
| Request parameter name | `system` | `mobile_os` |
| Request parameter data type | `advertiser_id`: number<br>`source_audience_id`: number<br>`placements`: string | `advertiser_id`: string<br>`source_audience_id`: string<br>`placements`: string[] |
| Request parameter name and data type | `is_contain_source`: number | `include_source`: boolean |
| Response parameter data type | `custom_audience_id`: number | `custom_audience_id`: string |

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Bắt buộc | Access token đã được cấp quyền. Chi tiết xem tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| `Content-Type` | string | Bắt buộc | Loại thông điệp request. Giá trị cho phép: `"application/json"`. |

### Tham số (POST: JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | Bắt buộc | ID tài khoản quảng cáo. |
| `custom_audience_name` | string | Bắt buộc | Tên tệp đối tượng tương tự. Độ dài tối đa 128 ký tự. |
| `audience_sub_type` | string | Không bắt buộc | Loại phụ đối tượng (đã ngừng hỗ trợ - Deprecated). Giá trị: `NORMAL`, `REACH_FREQUENCY`. Mặc định: `NORMAL`. |
| `lookalike_spec` | object | Bắt buộc | Cấu trúc cấu hình chi tiết cho đối tượng Lookalike. |
| ↳ `source_audience_id` | string | Bắt buộc | ID tệp đối tượng nguồn (hạt giống). Đối tượng nguồn không thể là một đối tượng Lookalike khác. Quy mô tệp nguồn phải từ 100 người dùng trở lên. |
| ↳ `include_source` | boolean | Bắt buộc | Có bao gồm các người dùng trong tệp đối tượng nguồn vào tệp đối tượng tương tự mới hay không. |
| ↳ `mobile_os` | string | Bắt buộc | Hệ điều hành thiết bị di động mục tiêu. Hỗ trợ giá trị: `ALL` (cho cả Android và iOS), `ANDROID`, `IOS`. Chi tiết xem tại [Enumeration-Audience Management-Lookalike System](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ `placements` | string[] | Bắt buộc | Các ứng dụng bạn muốn phân phối quảng cáo tới. Giá trị enum: `TikTok`, `TopBuzz & BuzzVideo`, `Pangle`. Chi tiết xem tại [Enumeration - Audience Management-Lookalike Placement](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ `location_ids` | string[] | Bắt buộc | Danh sách ID vị trí địa lý muốn nhắm mục tiêu. Chi tiết xem tại [Enumeration-Lookalike Locations](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ `audience_size` | string | Bắt buộc | Quy mô mở rộng của đối tượng tương tự.<br>Giá trị enum:<br>• `NARROW`: Thu hẹp (độ tương đồng cao nhất).<br>• `BALANCED`: Cân bằng (mức độ tương đồng và quy mô hài hòa).<br>• `BROAD`: Mở rộng (tiếp cận tệp người dùng rộng lớn nhất). |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Chi tiết xem tại [Appendix-Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi. |
| `request_id` | string | ID duy nhất định danh request. |
| `data` | object | Dữ liệu trả về. |
| ↳ `custom_audience_id` | string | ID tệp đối tượng tương tự vừa tạo. |

### Ví dụ gọi API

```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/dmp/custom_audience/lookalike/create/' \
--header 'Access-Token: your_access_token_here' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id": "7000000000000000001",
    "custom_audience_name": "LAL_VIP_Customers_Balanced",
    "lookalike_spec": {
        "source_audience_id": "173994057079398501",
        "include_source": false,
        "mobile_os": "ALL",
        "placements": ["TikTok"],
        "location_ids": ["VN"],
        "audience_size": "BALANCED"
    }
}'
```

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20231023120000010188059082040",
  "data": {
    "custom_audience_id": "173994051184435301"
  }
}
```

---

## Làm mới tệp đối tượng tương tự (`Refresh a lookalike audience`)
<a id="doc-1758616888158209"></a>
<!-- doc_id: 1758616888158209 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/dmp/custom_audience/lookalike/update/`

**Mục đích**: Kích hoạt làm mới thủ công (manually refresh) dữ liệu cho một hoặc nhiều tệp đối tượng tương tự (Lookalike Audience) để cập nhật thông tin người dùng mới nhất từ tệp hạt giống.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Bắt buộc | Access token đã được cấp quyền. Chi tiết xem tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| `Content-Type` | string | Bắt buộc | Loại thông điệp request. Giá trị cho phép: `"application/json"`. |

### Tham số (POST: JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | Bắt buộc | ID tài khoản quảng cáo. |
| `custom_audience_ids` | string[] | Bắt buộc | Danh sách các ID tệp đối tượng tương tự cần làm mới. |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Chi tiết xem tại [Appendix-Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi. |
| `request_id` | string | ID duy nhất định danh request. |
| `data` | object | Dữ liệu trả về (mảng rỗng `{}`). |

### Ví dụ gọi API

```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/dmp/custom_audience/lookalike/update/' \
--header 'Access-Token: your_access_token_here' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id": "7000000000000000001",
    "custom_audience_ids": ["173994051184435301"]
}'
```

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20231023120000010188059082041",
  "data": {}
}
```

---

## Xóa tệp đối tượng (`Delete audiences`)
<a id="doc-1739940539757569"></a>
<!-- doc_id: 1739940539757569 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/dmp/custom_audience/delete/`

**Mục đích**: Xóa một hoặc nhiều tệp đối tượng tùy chỉnh khỏi tài khoản quảng cáo của bạn.

### So sánh phiên bản v1.2 và v1.3

| Changes | v1.2 | v1.3 |
|---|---|---|
| Endpoint path | `/v1.2/dmp/custom_audience/delete/` | `/v1.3/dmp/custom_audience/delete/` |
| Request parameter data type | `advertiser_id`: number<br>`custom_audience_ids`: number[] | `advertiser_id`: string<br>`custom_audience_ids`: string[] |

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Bắt buộc | Access token đã được cấp quyền. Chi tiết xem tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| `Content-Type` | string | Bắt buộc | Loại thông điệp request. Giá trị cho phép: `"application/json"`. |

### Tham số (POST: JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | Bắt buộc | ID tài khoản quảng cáo. |
| `custom_audience_ids` | string[] | Bắt buộc | Danh sách các ID tệp đối tượng cần xóa. Số lượng phần tử cho phép: `[1, 100]`. |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Chi tiết xem tại [Appendix-Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi. |
| `request_id` | string | ID duy nhất định danh request. |
| `data` | object | Dữ liệu trả về (mảng rỗng `{}`). |

### Ví dụ gọi API

```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/dmp/custom_audience/delete/' \
--header 'Access-Token: your_access_token_here' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id": "7000000000000000001",
    "custom_audience_ids": ["173994051184435301"]
}'
```

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20231023120000010188059082042",
  "data": {}
}
```

---

## Chia sẻ tệp đối tượng (`Share audiences`)
<a id="doc-1740245803888706"></a>
<!-- doc_id: 1740245803888706 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/dmp/custom_audience/share/`

**Mục đích**: Bắt đầu chia sẻ một hoặc nhiều tệp đối tượng tùy chỉnh hoặc đối tượng Lookalike với các tài khoản quảng cáo chỉ định trong cùng một Business Center.

Chủ tài khoản quảng cáo, hoặc người dùng có vai trò Quản trị viên (Admin) hoặc Người vận hành (Operator) có thể chia sẻ tệp đối tượng tùy chỉnh (chỉ áp dụng đối với đối tượng tạo từ [Tệp khách hàng (Customer file)](09-audience.md#doc-1739940501023746), [Phân đoạn (Segment)](09-audience.md#doc-1739940504185857), Tương tác Engagement, Hoạt động App hoặc Lưu lượng Pixel) hoặc đối tượng Lookalike.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Bắt buộc | Access token đã được cấp quyền. Chi tiết xem tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| `Content-Type` | string | Bắt buộc | Định dạng nội dung của request. Giá trị cho phép: `"application/json"`. |

### Tham số (POST: JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | Bắt buộc | ID tài khoản quảng cáo của người thực hiện thao tác chia sẻ. |
| `custom_audience_ids` | string[] | Bắt buộc | Danh sách các ID tệp đối tượng muốn chia sẻ. Kích thước mảng: `[1, 10]`. |
| `shared_advertiser_ids` | string[] | Bắt buộc | Danh sách ID các nhà quảng cáo muốn chia sẻ đối tượng cùng. Các tài khoản này bắt buộc phải nằm trong cùng một Business Center với bạn. Kích thước mảng: `[1, 10]`. |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Chi tiết xem tại [Appendix-Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi. |
| `request_id` | string | ID duy nhất định danh request. |
| `data` | object | Dữ liệu trả về (mảng rỗng `{}`). |

### Ví dụ gọi API

```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/dmp/custom_audience/share/' \
--header 'Access-Token: your_access_token_here' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id": "7000000000000000001",
    "custom_audience_ids": ["173994057079398501"],
    "shared_advertiser_ids": ["7000000000000000002"]
}'
```

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20231023120000010188059082043",
  "data": {}
}
```

---

## Hủy chia sẻ tệp đối tượng (`Cancel the sharing of an audience`)
<a id="doc-1740245829978113"></a>
<!-- doc_id: 1740245829978113 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/dmp/custom_audience/share/cancel/`

**Mục đích**: Dừng chia sẻ một tệp đối tượng tùy chỉnh với một nhà quảng cáo cụ thể.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Bắt buộc | Access token đã được cấp quyền. Chi tiết xem tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| `Content-Type` | string | Bắt buộc | Định dạng nội dung của request. Giá trị cho phép: `"application/json"`. |

### Tham số (POST: JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | Bắt buộc | ID tài khoản quảng cáo của người thực hiện hủy chia sẻ. |
| `custom_audience_id` | string | Bắt buộc | ID tệp đối tượng mà bạn muốn ngừng chia sẻ. |
| `shared_advertiser_id` | string | Bắt buộc | ID nhà quảng cáo mà bạn muốn ngừng chia sẻ tệp đối tượng tới. |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Chi tiết xem tại [Appendix-Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi. |
| `request_id` | string | ID duy nhất định danh request. |
| `data` | object | Dữ liệu trả về (mảng rỗng `{}`). |

### Ví dụ gọi API

```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/dmp/custom_audience/share/cancel/' \
--header 'Access-Token: your_access_token_here' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id": "7000000000000000001",
    "custom_audience_id": "173994057079398501",
    "shared_advertiser_id": "7000000000000000002"
}'
```

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20231023120000010188059082044",
  "data": {}
}
```

---

## Lấy nhật ký chia sẻ tệp đối tượng (`Get the sharing log of an audience`)
<a id="doc-1740245827044354"></a>
<!-- doc_id: 1740245827044354 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/dmp/custom_audience/share/log/`

**Mục đích**: Lấy nhật ký lịch sử chia sẻ của một tệp đối tượng tùy chỉnh, bao gồm danh sách ID và tên các nhà quảng cáo đã được chia sẻ tệp đối tượng này.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Bắt buộc | Access token đã được cấp quyền. Chi tiết xem tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (GET: query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `custom_audience_id` | string | Bắt buộc | ID tệp đối tượng cần tra cứu nhật ký chia sẻ. |
| `page` | number | Không bắt buộc | Số trang hiện tại. Giá trị mặc định: `1`. |
| `page_size` | number | Không bắt buộc | Số bản ghi trên mỗi trang. Giá trị mặc định: `10`. |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Chi tiết xem tại [Appendix-Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi. |
| `request_id` | string | ID duy nhất định danh request. |
| `data` | object | Dữ liệu trả về. |
| ↳ `page_info` | object | Thông tin phân trang. |
| ↳↳ `page` | number | Số trang hiện tại. |
| ↳↳ `page_size` | number | Số lượng bản ghi trên một trang. |
| ↳↳ `total_page` | number | Tổng số trang. |
| ↳↳ `total_number` | number | Tổng số bản ghi. |
| ↳ `list` | object[] | Danh sách các lượt chia sẻ. |
| ↳↳ `shared_advertiser_id` | string | ID nhà quảng cáo được chia sẻ đối tượng. |
| ↳↳ `shared_advertiser_name` | string | Tên tài khoản quảng cáo được chia sẻ đối tượng. |
| ↳↳ `shared_time` | string | Thời gian chia sẻ đối tượng. |

### Ví dụ

#### cURL
```bash
curl -G --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/dmp/custom_audience/share/log/' \
--header 'Access-Token: your_access_token_here' \
--data-urlencode 'custom_audience_id=173994057079398501' \
--data-urlencode 'page=1' \
--data-urlencode 'page_size=10'
```

#### Python
```python
import requests

ACCESS_TOKEN = "your_access_token_here"
CUSTOM_AUDIENCE_ID = "173994057079398501"

url = "https://business-api.tiktok.com/open_api/v1.3/dmp/custom_audience/share/log/"
headers = {"Access-Token": ACCESS_TOKEN}
params = {
    "custom_audience_id": CUSTOM_AUDIENCE_ID,
    "page": 1,
    "page_size": 10
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20231023120000010188059082045",
  "data": {
    "page_info": {
      "page": 1,
      "page_size": 10,
      "total_page": 1,
      "total_number": 1
    },
    "list": [
      {
        "shared_advertiser_id": "7000000000000000002",
        "shared_advertiser_name": "Agency_Sub_Account",
        "shared_time": "2023-10-23 14:00:00"
      }
    ]
  }
}
```


---

## Áp dụng tệp đối tượng vào nhóm quảng cáo (`Apply audiences to ad groups`)
<a id="doc-1758615097524225"></a>
<!-- doc_id: 1758615097524225 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/dmp/custom_audience/apply/`

**Mục đích**: Áp dụng (bao gồm hoặc loại trừ) một tệp đối tượng tùy chỉnh vào nhiều nhóm quảng cáo (ad groups), hoặc gỡ bỏ liên kết đối tượng khỏi các nhóm quảng cáo đó.

> [!NOTE]
> - `adgroup_ids` và `custom_audience_id` bắt buộc phải thuộc về cùng một tài khoản quảng cáo.
> - Tệp đối tượng tương tự (Lookalike Audience) **không được phép** sử dụng trong các nhóm quảng cáo Tiếp cận & Tần suất (Reach & Frequency). Nếu áp dụng đối tượng Lookalike vào nhóm quảng cáo R&F hoặc đối tượng Lookalike có phân loại phụ là `REACH_FREQUENCY`, hệ thống sẽ báo lỗi.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Bắt buộc | Access token đã được cấp quyền. Chi tiết xem tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| `Content-Type` | string | Bắt buộc | Loại thông điệp request. Giá trị cho phép: `"application/json"`. |

### Tham số (POST: JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | Bắt buộc | ID tài khoản quảng cáo. |
| `custom_audience_id` | string | Bắt buộc | ID tệp đối tượng tùy chỉnh. Mỗi request chỉ được truyền 1 custom audience ID. |
| `adgroup_ids` | string[] | Bắt buộc | Danh sách các ID nhóm quảng cáo cần thao tác. |
| `action_mode` | string | Bắt buộc | Thao tác cụ thể thực hiện trên đối tượng.<br>Giá trị enum:<br>• `Apply`: Áp dụng đối tượng vào các nhóm quảng cáo.<br>• `Disconnect`: Gỡ bỏ đối tượng khỏi các nhóm quảng cáo. |
| `usage_mode` | string | Điều kiện | Bắt buộc khi `action_mode` là `Apply`. Chỉ định cách thức áp dụng đối tượng vào nhóm quảng cáo.<br>Giá trị enum:<br>• `Include`: Nhắm mục tiêu bao gồm đối tượng này.<br>• `Exclude`: Loại trừ đối tượng này khỏi nhóm quảng cáo. |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Chi tiết xem tại [Appendix-Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi. |
| `request_id` | string | ID duy nhất định danh request. |
| `data` | object | Dữ liệu trả về (mảng rỗng `{}`). |

### Ví dụ gọi API

```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/dmp/custom_audience/apply/' \
--header 'Access-Token: your_access_token_here' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id": "7000000000000000001",
    "custom_audience_id": "173994057079398501",
    "adgroup_ids": ["1750000000000000001", "1750000000000000002"],
    "action_mode": "Apply",
    "usage_mode": "Include"
}'
```

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20231023120000010188059082050",
  "data": {}
}
```

---

## Lấy nhật ký áp dụng tệp đối tượng (`Get the application log of audiences`)
<a id="doc-1758615737388033"></a>
<!-- doc_id: 1758615737388033 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/dmp/custom_audience/apply/log/`

**Mục đích**: Lấy nhật ký áp dụng gần đây nhất của các tệp đối tượng tùy chỉnh vào nhóm quảng cáo. Lưu ý rằng endpoint này chỉ trả về nhật ký của các thao tác áp dụng (`action_mode` = `Apply`).

> [!NOTE]
> Tài khoản quảng cáo gọi API phải là chủ sở hữu tạo ra các tệp đối tượng trong `custom_audience_ids` (`is_creator` = `true`). Bạn có thể kiểm tra quyền sở hữu qua [/dmp/custom_audience/list/](09-audience.md#doc-1739940506015746) hoặc [/dmp/custom_audience/get/](09-audience.md#doc-1739940507792385).

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Bắt buộc | Access token đã được cấp quyền. Chi tiết xem tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (GET: query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | Bắt buộc | ID tài khoản quảng cáo. |
| `custom_audience_ids` | string[] | Bắt buộc | Danh sách ID các tệp đối tượng tùy chỉnh cần tra cứu nhật ký (mảng JSON URL-encode, ví dụ: `["173994057079398501"]`). |
| `page` | number | Không bắt buộc | Số trang hiện tại. Giá trị mặc định: `1`. |
| `page_size` | number | Không bắt buộc | Số lượng bản ghi trên một trang. Giá trị mặc định: `10`. |
| `timezone` | string | Không bắt buộc | Múi giờ hiển thị của dữ liệu thời gian trả về. Xem danh sách mã múi giờ tại [Appendix - Time Zone](../15-appendix/phu-luc-p1.md#doc-1737586324313089). Mặc định là UTC. |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Chi tiết xem tại [Appendix-Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi. |
| `request_id` | string | ID duy nhất định danh request. |
| `data` | object | Dữ liệu trả về. |
| ↳ `advertiser_id` | string | ID tài khoản quảng cáo. |
| ↳ `list` | object[] | Mảng các bản ghi nhật ký áp dụng đối tượng. |
| ↳↳ `audience_id` | string | ID tệp đối tượng tùy chỉnh. |
| ↳↳ `adgroup_id` | string | ID nhóm quảng cáo được áp dụng. |
| ↳↳ `action_mode` | string | Thao tác thực hiện (`Apply`). |
| ↳↳ `usage_mode` | string | Cách thức áp dụng (`Include` hoặc `Exclude`). |
| ↳↳ `opt_time` | string | Thời gian thực hiện thao tác. |

### Ví dụ

#### cURL
```bash
curl -G --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/dmp/custom_audience/apply/log/' \
--header 'Access-Token: your_access_token_here' \
--data-urlencode 'advertiser_id=7000000000000000001' \
--data-urlencode 'custom_audience_ids=["173994057079398501"]' \
--data-urlencode 'page=1' \
--data-urlencode 'page_size=10'
```

#### Python
```python
import json
import requests

ACCESS_TOKEN = "your_access_token_here"
ADVERTISER_ID = "7000000000000000001"

url = "https://business-api.tiktok.com/open_api/v1.3/dmp/custom_audience/apply/log/"
headers = {"Access-Token": ACCESS_TOKEN}
params = {
    "advertiser_id": ADVERTISER_ID,
    "custom_audience_ids": json.dumps(["173994057079398501"]),
    "page": 1,
    "page_size": 10
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20231023120000010188059082051",
  "data": {
    "advertiser_id": "7000000000000000001",
    "list": [
      {
        "audience_id": "173994057079398501",
        "adgroup_id": "1750000000000000001",
        "action_mode": "Apply",
        "usage_mode": "Include",
        "opt_time": "2023-10-23 15:30:00"
      }
    ]
  }
}
```

---

## Đối tượng đã lưu (`Saved Audience`)
<a id="doc-1780154462204930"></a>
<!-- doc_id: 1780154462204930 -->

> Đường dẫn: API Reference > Audience > Saved Audience

Tính năng Đối tượng đã lưu (Saved Audience) cho phép bạn lưu trữ sẵn các tập cấu hình nhắm mục tiêu (độ tuổi, giới tính, vị trí, sở thích, hành vi, thiết bị) và tái sử dụng chúng nhanh chóng khi tạo các nhóm quảng cáo trong tương lai. Xem [Create a Saved Audience](../09-marketing-api/audience.md#doc-1780156510696449) để tìm hiểu thêm về tính năng này và cách áp dụng đối tượng đã lưu vào nhóm quảng cáo.

> [!NOTE]
> Hiện tại, hệ thống chưa hỗ trợ cập nhật chỉnh sửa một đối tượng đã lưu. Bạn cần tạo đối tượng mới nếu muốn thay đổi thông số.

Nhóm chức năng này gồm các endpoint:
- [Tạo đối tượng đã lưu (Create a Saved Audience)](09-audience.md#doc-1780154541898754)
- [Lấy chi tiết đối tượng đã lưu (Get details of Saved Audiences)](09-audience.md#doc-1780154619404290)
- [Xóa đối tượng đã lưu (Delete Saved Audiences)](09-audience.md#doc-1780154666312706)

---

## Tạo đối tượng đã lưu (`Create a Saved Audience`)
<a id="doc-1780154541898754"></a>
<!-- doc_id: 1780154541898754 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/dmp/saved_audience/create/`

**Mục đích**: Tạo một tập thiết lập nhắm mục tiêu đã lưu (Saved Audience). Mỗi tài khoản quảng cáo có thể tạo tối đa **400** đối tượng đã lưu.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Bắt buộc | Access token đã được cấp quyền. Chi tiết xem tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| `Content-Type` | string | Bắt buộc | Loại thông điệp request. Định dạng chấp nhận: `"application/json"`. |

### Tham số (POST: JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | Bắt buộc | ID tài khoản quảng cáo. |
| `saved_audience_name` | string | Bắt buộc | Tên đối tượng đã lưu. Giới hạn tối đa 512 ký tự và không được chứa emoji. |
| `location_ids` | string[] | Bắt buộc | Danh sách ID vị trí địa lý muốn nhắm mục tiêu. Lấy danh sách ID khả dụng qua [/tool/region/](70-tools-p1.md#doc-1737189539571713) hoặc [/tool/targeting/search/](70-tools-p1.md#doc-1761236883355649). Lưu ý: Không hỗ trợ nhắm mục tiêu trùng lặp (ví dụ: không thể cùng lúc nhắm toàn bộ Hoa Kỳ và bang California). |
| `gender` | string | Không bắt buộc | Giới tính mục tiêu. Enum: `GENDER_FEMALE`, `GENDER_MALE`, `GENDER_UNLIMITED`. |
| `age_groups` | string[] | Không bắt buộc | Các nhóm tuổi mục tiêu. Xem giá trị enum tại [Enumeration - Targeting Age Group](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| `languages` | string[] | Không bắt buộc | Mã các ngôn ngữ mục tiêu. Lấy mã qua [/tool/language/](70-tools-p1.md#doc-1737188554152962). Nếu không giới hạn ngôn ngữ, để trống hoặc không truyền. |
| `audience_ids` | string[] | Không bắt buộc | Danh sách ID các tệp đối tượng tùy chỉnh bao gồm. Lấy ID qua [/dmp/custom_audience/list/](09-audience.md#doc-1739940506015746). |
| `excluded_audience_ids` | string[] | Không bắt buộc | Danh sách ID các tệp đối tượng tùy chỉnh loại trừ. |
| `interest_category_ids` | string[] | Không bắt buộc | Phân loại sở thích người dùng. Lấy danh mục đề xuất qua [/tool/target_recommend_tags/](70-tools-p1.md#doc-1736275204260866) hoặc toàn bộ danh mục qua [/tool/interest_category/](70-tools-p1.md#doc-1737174348712961). |
| `interest_keyword_ids` | string[] | Không bắt buộc | Danh sách ID từ khóa sở thích. Lấy từ khóa đề xuất qua [/tool/interest_keyword/recommend/](70-tools-p1.md#doc-1763590884474882). |
| `actions` | object[] | Không bắt buộc | Danh sách các đối tượng phân loại hành vi người dùng. |
| ↳ `action_category_ids` | string[] | Điều kiện | Bắt buộc khi truyền `actions` và chỉ hợp lệ khi vị trí hiển thị TikTok là vị trí duy nhất. ID danh mục hành vi hoặc hashtag (lấy qua [/tool/action_category/](70-tools-p1.md#doc-1737166752522241)). |
| ↳ `action_scene` | string | Điều kiện | Bắt buộc khi truyền `actions`. Ngữ cảnh thu thập hành vi người dùng. Enum: `VIDEO_RELATED`, `CREATOR_RELATED`, `HASHTAG_RELATED`. |
| ↳ `action_period` | number | Điều kiện | Bắt buộc khi truyền `actions`. Khoảng thời gian thu thập hành vi. Enum: `0`, `7`, `15` ngày. Nếu `action_scene` là `CREATOR_RELATED` hoặc `HASHTAG_RELATED`, giá trị `0` luôn được áp dụng (không giới hạn khung thời gian). |
| ↳ `video_user_actions` | string[] | Điều kiện | Bắt buộc khi truyền `actions`. Hành vi liên quan đến video. Nếu `action_scene` là `VIDEO_RELATED`, các giá trị hỗ trợ gồm: `WATCHED_TO_END`, `LIKED`, `COMMENTED`, `SHARED`. Nếu là `CREATOR_RELATED`: `FOLLOWING`, `VIEW_HOMEPAGE`. Nếu là `HASHTAG_RELATED`: `VIEW_HASHTAG`. |
| `operating_systems` | string[] | Không bắt buộc | Hệ điều hành mục tiêu. Enum: `ANDROID`, `IOS`. |
| `min_android_version` | string | Không bắt buộc | Phiên bản hệ điều hành Android tối thiểu (ví dụ: `"4.0"`). |
| `min_ios_version` | string | Không bắt buộc | Phiên bản hệ điều hành iOS tối thiểu (ví dụ: `"8.0"`). |
| `device_model_ids` | string[] | Không bắt buộc | Danh sách ID mẫu thiết bị nhắm mục tiêu (lấy qua [/tool/device_model/](70-tools-p1.md#doc-1737189539571713)). |
| `network_types` | string[] | Không bắt buộc | Loại kết nối mạng. Enum: `WIFI`, `2G`, `3G`, `4G`, `5G`. |
| `carrier_ids` | string[] | Không bắt buộc | Danh sách ID nhà mạng viễn thông (lấy qua [/tool/carrier/](70-tools-p1.md#doc-1737189539571713)). |
| `device_price_ranges` | number[] | Không bắt buộc | Khoảng giá thiết bị (USD). Ví dụ: `[0, 50, 100, ...]`. |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Chi tiết xem tại [Return codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi. Chi tiết xem tại [Return codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `request_id` | string | ID duy nhất định danh request. |
| `data` | object | Dữ liệu trả về. |
| ↳ `saved_audience_id` | string | ID của đối tượng đã lưu vừa tạo. |

### Ví dụ gọi API

```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/dmp/saved_audience/create/' \
--header 'Access-Token: your_access_token_here' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id": "7000000000000000001",
    "saved_audience_name": "Saved_VN_GenZ_Shoppers",
    "location_ids": ["VN"],
    "gender": "GENDER_UNLIMITED",
    "age_groups": ["AGE_18_24", "AGE_25_34"],
    "operating_systems": ["ANDROID", "IOS"]
}'
```

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20231023120000010188059082052",
  "data": {
    "saved_audience_id": "178015454189875401"
  }
}
```

---

## Lấy chi tiết đối tượng đã lưu (`Get details of Saved Audiences`)
<a id="doc-1780154619404290"></a>
<!-- doc_id: 1780154619404290 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/dmp/saved_audience/list/`

**Mục đích**: Lấy thông tin chi tiết các thiết lập nhắm mục tiêu của đối tượng đã lưu (Saved Audiences) liên kết với tài khoản quảng cáo.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Bắt buộc | Access token đã được cấp quyền. Chi tiết xem tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (GET: query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | Bắt buộc | ID tài khoản quảng cáo. |
| `saved_audience_ids` | string[] | Không bắt buộc | Danh sách ID đối tượng đã lưu cần truy xuất (dạng chuỗi mảng JSON URL-encode, ví dụ: `["178015454189875401"]`). Tối đa 100 ID. Nếu không truyền, hệ thống sẽ trả về tất cả các đối tượng đã lưu của tài khoản. |
| `page` | number | Không bắt buộc | Số trang hiện tại. Giá trị mặc định: `1`. |
| `page_size` | number | Không bắt buộc | Số bản ghi trên mỗi trang. Giá trị mặc định: `10`. |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Chi tiết xem tại [Return codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi. Chi tiết xem tại [Return codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `request_id` | string | ID duy nhất định danh request. |
| `data` | object | Dữ liệu trả về. |
| ↳ `page_info` | object | Thông tin phân trang. |
| ↳↳ `page` | number | Số trang hiện tại. |
| ↳↳ `page_size` | number | Số bản ghi trên một trang. |
| ↳↳ `total_page` | number | Tổng số trang. |
| ↳↳ `total_number` | number | Tổng số bản ghi tìm thấy. |
| ↳ `saved_audiences` | object[] | Danh sách đối tượng đã lưu cùng cấu hình nhắm mục tiêu chi tiết. |
| ↳↳ `saved_audience_id` | string | ID đối tượng đã lưu. |
| ↳↳ `saved_audience_name` | string | Tên đối tượng đã lưu. |
| ↳↳ `location_ids` | string[] | Danh sách ID vị trí mục tiêu. |
| ↳↳ `gender` | string | Giới tính mục tiêu. |
| ↳↳ `age_groups` | string[] | Nhóm tuổi mục tiêu. |
| ↳↳ `languages` | string[] | Ngôn ngữ mục tiêu. |
| ↳↳ `audience_ids` | string[] | Danh sách ID tệp đối tượng tùy chỉnh bao gồm. |
| ↳↳ `excluded_audience_ids` | string[] | Danh sách ID tệp đối tượng tùy chỉnh loại trừ. |
| ↳↳ `interest_category_ids` | string[] | ID danh mục sở thích. |
| ↳↳ `interest_keyword_ids` | string[] | ID từ khóa sở thích. |
| ↳↳ `actions` | object[] | Cấu hình hành vi người dùng. |
| ↳↳↳ `action_category_ids` | string[] | Danh mục hành vi. |
| ↳↳↳ `action_scene` | string | Ngữ cảnh hành vi. |
| ↳↳↳ `action_period` | number | Khung thời gian hành vi. |
| ↳↳↳ `video_user_actions` | string[] | Hành vi video cụ thể. |
| ↳↳ `operating_systems` | string[] | Hệ điều hành. |
| ↳↳ `min_android_version` | string | Phiên bản Android tối thiểu. |
| ↳↳ `min_ios_version` | string | Phiên bản iOS tối thiểu. |
| ↳↳ `device_model_ids` | string[] | ID mẫu thiết bị. |
| ↳↳ `network_types` | string[] | Loại mạng kết nối. |
| ↳↳ `carrier_ids` | string[] | ID nhà mạng viễn thông. |
| ↳↳ `device_price_ranges` | number[] | Khoảng giá thiết bị. |

### Ví dụ

#### cURL
```bash
curl -G --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/dmp/saved_audience/list/' \
--header 'Access-Token: your_access_token_here' \
--data-urlencode 'advertiser_id=7000000000000000001' \
--data-urlencode 'saved_audience_ids=["178015454189875401"]'
```

#### Python
```python
import json
import requests

ACCESS_TOKEN = "your_access_token_here"
ADVERTISER_ID = "7000000000000000001"

url = "https://business-api.tiktok.com/open_api/v1.3/dmp/saved_audience/list/"
headers = {"Access-Token": ACCESS_TOKEN}
params = {
    "advertiser_id": ADVERTISER_ID,
    "saved_audience_ids": json.dumps(["178015454189875401"])
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20231023120000010188059082053",
  "data": {
    "page_info": {
      "page": 1,
      "page_size": 10,
      "total_page": 1,
      "total_number": 1
    },
    "saved_audiences": [
      {
        "saved_audience_id": "178015454189875401",
        "saved_audience_name": "Saved_VN_GenZ_Shoppers",
        "location_ids": ["VN"],
        "gender": "GENDER_UNLIMITED",
        "age_groups": ["AGE_18_24", "AGE_25_34"],
        "operating_systems": ["ANDROID", "IOS"]
      }
    ]
  }
}
```

---

## Xóa đối tượng đã lưu (`Delete Saved Audiences`)
<a id="doc-1780154666312706"></a>
<!-- doc_id: 1780154666312706 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/dmp/saved_audience/delete/`

**Mục đích**: Xóa một hoặc nhiều đối tượng đã lưu (Saved Audiences) khỏi tài khoản quảng cáo.

> [!NOTE]
> Nếu bạn đã áp dụng đối tượng đã lưu này vào một nhóm quảng cáo (ad group), bạn chỉ có thể xóa đối tượng đã lưu sau khi nhóm quảng cáo đó đã bị xóa.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Bắt buộc | Access token đã được cấp quyền. Chi tiết xem tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| `Content-Type` | string | Bắt buộc | Loại thông điệp request. Giá trị cho phép: `"application/json"`. |

### Tham số (POST: JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | Bắt buộc | ID tài khoản quảng cáo. |
| `saved_audience_ids` | string[] | Bắt buộc | Danh sách ID các đối tượng đã lưu muốn xóa. Tối đa 100 ID mỗi request. |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Chi tiết xem tại [Return codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi. |
| `request_id` | string | ID duy nhất định danh request. |
| `data` | object | Dữ liệu trả về (mảng rỗng `{}`). |

### Ví dụ gọi API

```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/dmp/saved_audience/delete/' \
--header 'Access-Token: your_access_token_here' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id": "7000000000000000001",
    "saved_audience_ids": ["178015454189875401"]
}'
```

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20231023120000010188059082054",
  "data": {}
}
```


---

## Thông tin chuyên sâu về đối tượng (`Audience Insights`)
<a id="doc-1797016417934337"></a>
<!-- doc_id: 1797016417934337 -->

> Đường dẫn: API Reference > Audience > Audience Insights

Các đặc điểm nhân khẩu học, vị trí, sở thích và thiết bị của đối tượng được ước tính dựa trên các yếu tố như hành vi người dùng trên ứng dụng TikTok, thông tin do người dùng cung cấp và thông tin thiết bị. Độ chính xác của các phân tích chuyên sâu này có thể thay đổi tùy thuộc vào lượng thông tin được cung cấp và chỉ mang tính chất tham khảo.

Để tìm hiểu thêm về các khái niệm và kinh nghiệm thực hành tốt nhất, hãy truy cập [Best Practices for Audience Insights](https://ads.tiktok.com/help/article/audience-insights-best-practices?lang=en) trên Trung tâm trợ giúp TikTok Business.

> [!NOTE]
> Hiện tại, API chỉ hỗ trợ các endpoint phân tích Thông tin chuyên sâu về đối tượng trước chiến dịch (Pre-campaign Audience Insights), tương ứng với tính năng "Đối tượng tiềm năng" (Potential Audience) trong Trình quản lý quảng cáo TikTok. Chưa hỗ trợ phân tích đối tượng sau chiến dịch (Post-campaign / Reached Audience).

Nhóm chức năng này gồm hai endpoint:
- [Lấy chi tiết đối tượng tiềm năng (Get details of potential audiences)](09-audience.md#doc-1797016593782785)
- [Lấy chi tiết trùng lặp đối tượng (Get details of audience overlap)](09-audience.md#doc-1797023590780930)

---

## Lấy thông tin đối tượng tiềm năng (`Get details of potential audiences`)
<a id="doc-1797016593782785"></a>
<!-- doc_id: 1797016593782785 -->

`POST` `https://business-api.tiktok.com/open_api/v1.3/audience/insight/info/`

**Mục đích**: Lấy thông tin chi tiết về đặc điểm nhân khẩu học, vị trí, sở thích và hành vi của đối tượng tiềm năng trước khi khởi chạy chiến dịch.

> [!NOTE]
> - Endpoint này sử dụng phương thức **POST**.
> - Bạn phải truyền một trong hai trường: `locations` hoặc `custom_audience_id`. Không được truyền cả hai cùng lúc.
> - Mỗi lần gọi API, bạn chỉ có thể chỉ định **duy nhất một chiều dữ liệu** trong trường `dimensions`.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Bắt buộc | Access token đã được cấp quyền. Chi tiết xem tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |
| `Content-Type` | string | Bắt buộc | Loại thông điệp request. Giá trị cho phép: `"application/json"`. |

### Tham số (POST: JSON body)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | Bắt buộc | ID tài khoản quảng cáo. |
| `custom_audience_id` | string | Điều kiện | ID tệp đối tượng tùy chỉnh cần phân tích. Bắt buộc truyền trường này hoặc `locations`. Lưu ý: Khi đã chỉ định `custom_audience_id`, không thể dùng `selected_audience` hoặc `locations`. Audience ID phải thuộc quyền quản lý của advertiser. |
| `locations` | object[] | Điều kiện | Danh sách vị trí địa lý cần phân tích. Bắt buộc truyền trường này hoặc `custom_audience_id`. Tối đa 5 phần tử. Khi truyền `locations`, không được truyền `custom_audience_id`. |
| ↳ `country_code` | string | Bắt buộc | Mã quốc gia (2 chữ cái). Chi tiết xem tại **Appendix-Location IDs**. |
| ↳ `location_ids` | string[] | Không bắt buộc | Danh sách ID vị trí thuộc mã quốc gia chỉ định. Nếu để trống, mặc định chọn toàn bộ quốc gia. |
| `dimensions` | string[] | Bắt buộc | Chiều dữ liệu muốn nhận về trong phản hồi. Mỗi lần gọi chỉ được truyền 1 chiều dữ liệu.<br>Giá trị enum:<br>• `age`: Phân bổ độ tuổi.<br>• `gender`: Phân bổ giới tính.<br>• `country`: Phân bổ theo quốc gia.<br>• `top_regions`: Các khu vực/tỉnh thành hàng đầu.<br>• `operating_system`: Hệ điều hành thiết bị.<br>• `operating_system_version`: Phiên bản hệ điều hành.<br>• `device_price`: Khoảng giá thiết bị.<br>• `top_interests`: Các nhóm sở thích hàng đầu.<br>• `bottom_interests`: Các phân khúc sở thích cụ thể.<br>• `engagement`: Mức độ tương tác.<br>• `ad_interest_categories`: Danh mục sở thích quảng cáo.<br>• `top_hashtags`: Các hashtag nổi bật nhất. |
| `selected_audience` | object | Không bắt buộc | Cấu hình bộ lọc đối tượng cụ thể muốn phân tích (khi sử dụng `locations`). |
| ↳ `top_regions_country_code` | string | Điều kiện | Bắt buộc nếu `dimensions` chứa `top_regions` và có truyền `locations`. Chỉ định mã quốc gia để lấy danh sách các tỉnh/khu vực trực thuộc. |
| ↳ `languages` | string[] | Không bắt buộc | Mã các ngôn ngữ mục tiêu. Xem [Enumeration - Language Code](../15-appendix/phu-luc-p1.md#doc-1737174886619138) hoặc lấy qua [/tool/language/](70-tools-p1.md#doc-1737188554152962). |
| ↳ `age_groups` | string[] | Không bắt buộc | Các nhóm tuổi mục tiêu. Xem enum tại [Enumeration - Age Group](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ `gender` | string[] | Không bắt buộc | Giới tính mục tiêu (`GENDER_FEMALE`, `GENDER_MALE`). Bỏ trống để chọn cả hai. |
| ↳ `device_price_ranges` | integer[] | Không bắt buộc | Khoảng giá thiết bị mục tiêu (USD). Các số phải là bội số của 50 (ví dụ: `100`, `950`; `10000` nghĩa là trên $1000). |
| ↳ `min_ios_version` | string | Không bắt buộc | Phiên bản iOS tối thiểu. Xem enum tại [Enumeration - Minimum iOS Version](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ `min_android_version` | string | Không bắt buộc | Phiên bản Android tối thiểu. Xem enum tại [Enumeration - Minimum Android Version](../15-appendix/phu-luc-p1.md#doc-1737174886619138). |
| ↳ `operating_systems` | string[] | Điều kiện | Bắt buộc khi có truyền `min_ios_version` hoặc `min_android_version`. Hệ điều hành mục tiêu (`ANDROID` hoặc `IOS`). Chỉ cho phép 1 giá trị. Bỏ trống để chọn cả hai. |
| ↳ `interest_category_ids` | string[] | Không bắt buộc | Danh sách ID phân loại sở thích. Lấy qua [/tool/interest_category/](70-tools-p1.md#doc-1737174348712961) hoặc đề xuất qua [/tool/target_recommend_tags/](70-tools-p1.md#doc-1736275204260866). |
| ↳ `video_action_category_ids` | string[] | Không bắt buộc | Danh sách ID hành vi tương tác video. Lấy qua [/tool/action_category/](70-tools-p1.md#doc-1737166752522241) với `action_scene` là `VIDEO_RELATED`. |
| ↳ `creator_action_category_ids` | string[] | Không bắt buộc | Danh sách ID hành vi tương tác nhà sáng tạo. Lấy qua [/tool/action_category/](70-tools-p1.md#doc-1737166752522241) với `action_scene` là `CREATOR_RELATED`. |
| ↳ `hashtag_action_category_ids` | string[] | Không bắt buộc | Danh sách ID hashtag. Lấy qua [/tool/hashtag/recommend/](70-tools-p1.md#doc-1736271339521025) hoặc [/tool/hashtag/get/](70-tools-p1.md#doc-1736280889167874). |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Chi tiết xem tại [Appendix-Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi. |
| `request_id` | string | ID duy nhất định danh request. |
| `data` | object | Dữ liệu trả về theo chiều phân tích được chỉ định trong `dimensions`. |
| ↳ `age` | object | Dữ liệu phân bổ độ tuổi (trả về khi `dimensions` chứa `age`). Bao gồm mảng `all` (tổng thể) và `selected` (đã lọc). Mỗi phần tử chứa `label` (nhãn độ tuổi) và `rate` (tỷ lệ phần trăm). |
| ↳ `gender` | object | Dữ liệu phân bổ giới tính (trả về khi `dimensions` chứa `gender`). Chứa `all` và `selected` với `label` và `rate`. |
| ↳ `country` | object | Dữ liệu phân bổ theo quốc gia. |
| ↳ `top_regions` | object | Dữ liệu các tỉnh/khu vực hàng đầu. |
| ↳ `operating_system` | object | Dữ liệu tỷ lệ hệ điều hành. |
| ↳ `device_price` | object | Dữ liệu tỷ lệ khoảng giá thiết bị. |
| ↳ `top_interests` | object | Dữ liệu sở thích hàng đầu. |
| ↳ `top_hashtags` | object | Dữ liệu các hashtag được quan tâm nhất. |

### Ví dụ gọi API

```bash
curl --location --request POST 'https://business-api.tiktok.com/open_api/v1.3/audience/insight/info/' \
--header 'Access-Token: your_access_token_here' \
--header 'Content-Type: application/json' \
--data '{
    "advertiser_id": "7000000000000000001",
    "dimensions": ["age"],
    "locations": [
        {
            "country_code": "VN",
            "location_ids": []
        }
    ],
    "selected_audience": {
        "gender": ["GENDER_FEMALE"],
        "age_groups": ["AGE_18_24", "AGE_25_34"]
    }
}'
```

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20231023120000010188059082060",
  "data": {
    "age": {
      "all": [
        {
          "label": "18-24",
          "rate": 0.42
        },
        {
          "label": "25-34",
          "rate": 0.38
        }
      ],
      "selected": [
        {
          "label": "18-24",
          "rate": 0.52
        },
        {
          "label": "25-34",
          "rate": 0.48
        }
      ]
    }
  }
}
```

---

## Lấy thông tin trùng lặp đối tượng (`Get details of audience overlap`)
<a id="doc-1797023590780930"></a>
<!-- doc_id: 1797023590780930 -->

`GET` `https://business-api.tiktok.com/open_api/v1.3/audience/insight/overlap/`

**Mục đích**: Phân tích tỷ lệ và số lượng người dùng trùng lặp giữa một tệp đối tượng tùy chỉnh chuẩn (benchmark audience) và tối đa 4 tệp đối tượng tùy chỉnh so sánh khác của TikTok.

> [!NOTE]
> Các tệp đối tượng có quy mô nhỏ hơn 1.000 người dùng sẽ không được hiển thị kết quả phân tích trùng lặp. Tất cả các ID đối tượng truyền vào phải thuộc quyền truy cập của `advertiser_id`.

### Header

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `Access-Token` | string | Bắt buộc | Access token đã được cấp quyền. Chi tiết xem tại [Authentication](../09-marketing-api/marketing-api-xac-thuc-uy-quyen.md#doc-1738373164380162). |

### Tham số (GET: query string)

| Tên | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `advertiser_id` | string | Bắt buộc | ID tài khoản quảng cáo. |
| `benchmark_custom_audience_id` | string | Bắt buộc | ID tệp đối tượng tùy chỉnh được chọn làm đối tượng chuẩn (chuẩn so sánh). ID này phải thuộc quyền truy cập của advertiser. |
| `comparison_custom_audience_ids` | string[] | Không bắt buộc | Danh sách ID các tệp đối tượng tùy chỉnh cần so sánh đối chiếu (dưới dạng chuỗi mảng JSON URL-encode, ví dụ: `["173994057079398502"]`). Tối đa 4 tệp đối tượng so sánh. |

### Phản hồi

| Tên | Kiểu | Mô tả |
|---|---|---|
| `code` | number | Mã phản hồi. Chi tiết xem tại [Appendix-Return Codes](../15-appendix/phu-luc-p1.md#doc-1737172488964097). |
| `message` | string | Thông điệp phản hồi. |
| `request_id` | string | ID duy nhất định danh request. |
| `data` | object | Dữ liệu kết quả so sánh đối tượng. |
| ↳ `benchmark_audience` | object | Thông tin tệp đối tượng chuẩn. |
| ↳↳ `audience_id` | string | ID đối tượng chuẩn. |
| ↳↳ `audience_name` | string | Tên đối tượng chuẩn. |
| ↳↳ `audience_size` | number | Quy mô đối tượng chuẩn. |
| ↳↳ `targetable_users_count_range` | string | Khoảng số lượng người dùng hoạt động trong 30 ngày qua có thể nhắm mục tiêu. |
| ↳ `comparison_audiences` | object[] | Danh sách thông tin các đối tượng so sánh (trả về khi có truyền `comparison_custom_audience_ids`). |
| ↳↳ `audience_id` | string | ID đối tượng so sánh. |
| ↳↳ `audience_name` | string | Tên đối tượng so sánh. |
| ↳↳ `audience_size` | number | Quy mô đối tượng so sánh. |
| ↳↳ `targetable_users_count_range` | string | Khoảng số lượng người dùng có thể nhắm mục tiêu của đối tượng so sánh. |
| ↳↳ `benchmark_overlap_rate` | string | Tỷ lệ cơ sở người dùng từ đối tượng chuẩn có mặt trong đối tượng so sánh. |
| ↳↳ `benchmark_overlap_rate_range` | string | Khoảng tỷ lệ phần trăm người dùng trùng lặp. |
| ↳↳ `benchmark_overlap_count_range` | string | Khoảng số lượng người dùng trùng lặp. |

### Ví dụ

#### cURL
```bash
curl -G --location --request GET 'https://business-api.tiktok.com/open_api/v1.3/audience/insight/overlap/' \
--header 'Access-Token: your_access_token_here' \
--data-urlencode 'advertiser_id=7000000000000000001' \
--data-urlencode 'benchmark_custom_audience_id=173994057079398501' \
--data-urlencode 'comparison_custom_audience_ids=["173994057079398502"]'
```

#### Python
```python
import json
import requests

ACCESS_TOKEN = "your_access_token_here"
ADVERTISER_ID = "7000000000000000001"

url = "https://business-api.tiktok.com/open_api/v1.3/audience/insight/overlap/"
headers = {"Access-Token": ACCESS_TOKEN}
params = {
    "advertiser_id": ADVERTISER_ID,
    "benchmark_custom_audience_id": "173994057079398501",
    "comparison_custom_audience_ids": json.dumps(["173994057079398502"])
}

response = requests.get(url, headers=headers, params=params)
print(response.json())
```

```json
{
  "code": 0,
  "message": "OK",
  "request_id": "20231023120000010188059082061",
  "data": {
    "benchmark_audience": {
      "audience_id": "173994057079398501",
      "audience_name": "VIP_Customers_Q4",
      "audience_size": 125000,
      "targetable_users_count_range": "100k-150k"
    },
    "comparison_audiences": [
      {
        "audience_id": "173994057079398502",
        "audience_name": "Cart_Abandoners_30D",
        "audience_size": 80000,
        "targetable_users_count_range": "50k-100k",
        "benchmark_overlap_rate": "0.35",
        "benchmark_overlap_rate_range": "30%-40%",
        "benchmark_overlap_count_range": "40k-50k"
      }
    ]
  }
}
```
