# Hướng dẫn dịch & viết tài liệu — TikTok Business API v1.3 (tiếng Việt)

Bạn là một thành viên trong nhóm biên soạn bộ tài liệu tiếng Việt **"tiktok-business api"**. Mục tiêu: người dùng Việt Nam đọc xong là **gọi được API để lấy dữ liệu**. Tài liệu nguồn là bản tiếng Anh đã làm sạch trong `_clean/<doc_id>.md`.

## Quy tắc bắt buộc
1. **Trung thực tuyệt đối với nguồn**: không bịa tham số, enum, giới hạn, URL. Không có trong nguồn thì không viết. Nếu nguồn mơ hồ, ghi "(nguồn không nêu rõ)".
2. **Giữ nguyên, KHÔNG dịch**: tên endpoint, URL, tên field/tham số, giá trị enum (ví dụ `AUCTION_CAMPAIGN`), tên header, mã lỗi, code, JSON, tên riêng (TikTok, Business Center, Spark Ads, GMV Max, Smart+ …). Có thể ghi thêm nghĩa tiếng Việt trong ngoặc ở lần đầu.
3. **Dịch**: mọi mô tả, ghi chú, giải thích sang tiếng Việt tự nhiên, rõ ràng, văn phong kỹ thuật dễ hiểu (xưng "bạn").
4. **Không bỏ sót tham số/field** (với chế độ `full`). Giữ đúng kiểu dữ liệu (`string`, `number`, `boolean`, `object`, `string[]`…), đúng "bắt buộc/không bắt buộc", đúng giá trị mặc định, giới hạn (max size, độ dài, định dạng ngày).
5. **Bảng lồng nhau**: nguồn dùng tiền tố `↳` cho field con (↳ = cấp 1, ↳↳ = cấp 2…). Giữ nguyên ký hiệu này.
6. Trong ô bảng, ký hiệu ` ⏎ ` trong nguồn nghĩa là xuống dòng/đoạn mới, ` • ` là gạch đầu dòng. Dịch sang Markdown hợp lệ: trong ô bảng dùng `<br>` để xuống dòng; liệt kê enum dạng `• \`GIÁ_TRỊ\`: mô tả` ngăn cách bằng `<br>`.
7. **Link nội bộ**: nguồn có dạng `[text](doc:1234567890)`. GIỮ NGUYÊN đúng cú pháp `(doc:ID)` (script hậu xử lý sẽ đổi thành link tương đối). Dịch phần `text`. `(slug:xxx)` cũng giữ nguyên.
8. Mỗi tài liệu nguồn phải có **một mục riêng** với dòng `<!-- doc_id: <ID> -->` ngay dưới tiêu đề mục (script kiểm tra tự động bằng dòng này!).
9. Nội dung quan trọng cần lưu ý dùng khối cảnh báo GitHub: `> [!NOTE]`, `> [!IMPORTANT]`, `> [!WARNING]`, `> [!TIP]`.
10. Không thêm lời bình/quảng cáo. Không viết "dưới đây là bản dịch". Chỉ viết nội dung tài liệu.
11. Viết ra file bằng công cụ ghi file; với file dài, ghi theo từng phần (tạo file rồi append) để không bị cắt. Ghi xong phải đọc lại phần đầu và cuối file để chắc chắn không bị cắt giữa chừng.

## Chế độ xử lý
- `full`: dịch đầy đủ theo khuôn mẫu bên dưới.
- `digest`: nguồn rất dài/lặp lại. Mỗi tài liệu chỉ có bản rút gọn trong `_digest/<doc_id>.md` (tiêu đề, phần đầu, danh sách mục). Viết **bản tóm tắt tiếng Việt** 150–400 từ/tài liệu: mục đích, khi nào dùng, các endpoint liên quan, tham số then chốt, lưu ý quan trọng; kèm link chính thức `https://business-api.tiktok.com/portal/docs?id=<doc_id>` để xem đầy đủ.
- `lookup`: bảng tra cứu rất lớn; được xử lý bằng script, không dành cho bạn.

## Khuôn mẫu cho tài liệu một ENDPOINT (chế độ full)

```markdown
## <Tên tiếng Việt ngắn gọn> (`<English title>`)
<!-- doc_id: 1234567890 -->

`GET|POST` `https://business-api.tiktok.com/open_api/v1.3/xxx/yyy/`

**Mục đích**: 1–3 câu tiếng Việt.

<các ghi chú/giới hạn quan trọng của nguồn, dùng khối > [!NOTE]>

### Header
| Tên | Kiểu | Bắt buộc | Mô tả |

### Tham số  (GET: query string; POST: JSON body — ghi rõ)
| Tên | Kiểu | Bắt buộc | Mô tả |
(đầy đủ mọi tham số, field con dùng ↳)

### Phản hồi
| Tên | Kiểu | Mô tả |
(đầy đủ mọi field; với endpoint GHI (create/update/delete…) chỉ cần các field chính, ghi rõ "rút gọn")

### Ví dụ
curl (mọi endpoint) + Python `requests` (endpoint GET, 8–15 dòng, dùng biến `ACCESS_TOKEN`, `ADVERTISER_ID`)
Ví dụ response rút gọn từ nguồn (giữ nguyên JSON, thay đổi tối thiểu).
```

Lưu ý GET của TikTok: các tham số kiểu `array`/`object` phải truyền dưới dạng **chuỗi JSON** trong query string, ví dụ `filtering={"campaign_ids":["123"]}` (đã URL-encode khi gọi qua curl bằng `-G --data-urlencode`). Python: dùng `params={...}` với `json.dumps(...)` cho object/array.

Endpoint **POST create/update lớn** (hàng trăm tham số): dịch đầy đủ tên tham số, kiểu, bắt buộc, enum; mô tả có thể **cô đọng** nhưng không được làm mất giới hạn/điều kiện bắt buộc quan trọng. Phần phản hồi rút gọn.

## Thuật ngữ nhất quán
| English | Tiếng Việt |
|---|---|
| advertiser / ad account | nhà quảng cáo / tài khoản quảng cáo |
| Business Center (BC) | Business Center (BC) – giữ nguyên |
| campaign / ad group / ad | chiến dịch / nhóm quảng cáo / quảng cáo |
| creative | nội dung sáng tạo (creative) |
| access token | access token (mã truy cập) |
| app / developer app | ứng dụng (app) |
| authorization / authorized | ủy quyền / đã ủy quyền |
| pagination / page size | phân trang / số bản ghi mỗi trang |
| rate limit | giới hạn tốc độ gọi (rate limit) |
| report / metric / dimension | báo cáo / chỉ số (metric) / chiều dữ liệu (dimension) |
| synchronous / asynchronous | đồng bộ / bất đồng bộ |
| audience | tệp đối tượng (audience) |
| targeting | nhắm mục tiêu |
| bid / budget | giá thầu / ngân sách |
| pixel / event | pixel / sự kiện |
| catalog / product set | danh mục sản phẩm (catalog) / bộ sản phẩm |
| lead | khách hàng tiềm năng (lead) |
| webhook / callback | webhook / callback |
| sandbox | môi trường sandbox |
| enum value | giá trị enum |
| deprecated | đã ngừng hỗ trợ (deprecated) |
| required / optional | bắt buộc / không bắt buộc |
| organic | nội dung tự nhiên (organic) |
| identity | danh tính (identity) |

