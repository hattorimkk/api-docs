# Chương 4: Đặc Tả Kỹ Thuật API (API Reference)

[← Chương 3: Models & Specifications](03_models_and_specifications.md) | [Mục Lục](../README.md) | [Chương 5: Tuyển Tập Cookbooks →](05_cookbooks_and_patterns.md)

> **Tài liệu tham chiếu chính thức:** [https://docs.typesafe.ai/introduction](https://docs.typesafe.ai/introduction) & OpenAPI Spec tại `https://api.typesafe.ai/openapi.json`

---

## 4.1. Tổng Quan Về Kiến Trúc Giao Thức

TypeSafe AI thiết kế hệ thống theo phong cách **Single Unified Endpoint (Một Điểm Cuối Duy Nhất)**. Thay vì phân mảnh thành hàng chục API cho phân loại, kiểm duyệt, lọc văn bản hay đo lường, toàn bộ năng lực của Jev đều được triệu gọi qua:

* **Base URL:** `https://api.typesafe.ai`
* **Endpoint:** `POST /v1/systemone`
* **Phương thức xác thực:** HTTP Bearer Token (`Authorization: Bearer <YOUR_API_KEY>`)
* **Định dạng dữ liệu:** `application/json; charset=utf-8`

---

## 4.2. Đặc Tả Request (Yêu Cầu Gửi Đi)

### 1. HTTP Headers

| Tên Header | Kiểu Dữ Liệu | Bắt Buộc | Mô Tả |
| :--- | :--- | :--- | :--- |
| `Authorization` | String | **Có** | Định dạng: `Bearer jv_live_...` (lấy từ TypeSafe Console) |
| `Content-Type` | String | **Có** | Bắt buộc là `application/json` |
| `TypeSafe-Danger-Zone-Images` | Boolean | Không | Bắt buộc là `true` nếu trong request có sử dụng trường `assets` hoặc primitive `box` |
| `TypeSafe-Danger-Zone-Long-Context` | Boolean | Không | Bắt buộc là `true` nếu `state` vượt quá 64.000 tokens (cho phép tối đa 262.144 tokens) |

---

### 2. Request Body JSON Schema

```json
{
  "model": "jev-latest",
  "state": "...",
  "questions": {
    "<question_key_1>": {
      "type": "noul",
      "instructions": "...",
      "criteria": { "true": "...", "false": "..." }
    },
    "<question_key_2>": {
      "type": "choice",
      "instructions": "...",
      "criteria": {
        "<option_a>": "...",
        "<option_b>": "..."
      }
    },
    "<question_key_3>": {
      "type": "score",
      "instructions": "...",
      "criteria": [
        "Mức 1: ...",
        "Mức 2: ...",
        "Mức 3: ..."
      ]
    }
  },
  "assets": {
    "<asset_key>": "data:image/png;base64,..."
  }
}
```

#### Chi Tiết Các Trường Dữ Liệu:

* **`model`** *(string, Tùy chọn, Mặc định: `jev-latest`)*:
  Mã định danh phiên bản mô hình xử lý: `jev-1.14.0`, `jev-1.13.0`, `jev-latest`, `jev-preview`.
* **`state`** *(string | object | array, Bắt buộc)*:
  Tài nguyên cần đánh giá. Có thể là:
  * Một chuỗi văn bản tự do (đoạn chat, email, bài báo, log hệ thống).
  * Một đối tượng JSON có cấu trúc (ví dụ: thông tin giao dịch, dữ liệu đơn hàng).
  * Một mảng (array) các bản ghi.
* **`questions`** *(map/object, Bắt buộc)*:
  Bảng ánh xạ các câu hỏi. Khóa (key) là định danh do lập trình viên tự đặt (ví dụ: `is_safe`, `category`, `urgency`). Giá trị là cấu hình của từng Primitive:
  * **`type`** *(string, Bắt buộc)*: Nhận một trong các giá trị: `"noul"`, `"choice"`, `"score"`, `"box"`.
  * **`instructions`** *(string, Bắt buộc)*: Câu lệnh tự nhiên hướng dẫn mô hình tiêu chí cần phán xét.
  * **`criteria`** *(object | array, Tùy chọn đối với Noul, Bắt buộc đối với Choice & Score)*: Định nghĩa các nhãn hoặc bậc thang đo.
* **`assets`** *(map/object, Tùy chọn)*:
  Bảng ánh xạ chứa dữ liệu hình ảnh (URL hoặc chuỗi base64 `data:image/...;base64,...`).

---

## 4.3. Đặc Tả Response (Phản Hồi Trả Về)

### Response Body JSON Schema

```json
{
  "id": "sys_01hgb899z1m8",
  "model": "jev-1.14.0",
  "answers": {
    "<question_key_1>": {
      "type": "noul",
      "noul": 0.992
    },
    "<question_key_2>": {
      "type": "choice",
      "choice": "<option_a>",
      "probabilities": {
        "<option_a>": 0.941,
        "<option_b>": 0.059
      },
      "confidence": 0.918
    },
    "<question_key_3>": {
      "type": "score",
      "score": 2.78,
      "confidence": 0.884
    }
  },
  "usage": {
    "input_tokens": 284,
    "output_tokens": 0
  }
}
```

#### Chi Tiết Các Trường Trả Về:

* **`id`** *(string)*: Mã định danh duy nhất của phiên inference, dùng cho đối soát và theo dõi logs (Audit Trail).
* **`model`** *(string)*: Tên chính xác của mô hình đã thực thi yêu cầu (ví dụ: `jev-1.14.0`).
* **`answers`** *(object)*: Chứa kết quả khớp theo từng khóa câu hỏi trong `questions` ban đầu:
  * Với `noul`: Trường `noul` chứa số thực từ `0.0` đến `1.0`.
  * Với `choice`: Trường `choice` chứa nhãn được chọn; `probabilities` chứa phân phối xác suất; `confidence` chứa điểm số tin cậy.
  * Với `score`: Trường `score` chứa điểm số liên tục; `confidence` chứa độ tin cậy.
  * Với `box`: Trường `box` chứa tọa độ `{ "top": float, "bottom": float, "left": float, "right": float }`.
* **`usage`** *(object)*:
  * `input_tokens` *(integer)*: Số lượng token đầu vào được tính phí.
  * `output_tokens` *(integer)*: **Luôn luôn là `0`** (Không bao giờ phát sinh chi phí token đầu ra).

---

## 4.4. Hướng Dẫn Sử Dụng SDKs Chính Thức

### 1. Python SDK (`typesafe-sdk`)

Cài đặt thông qua pip hoặc uv:
```bash
pip install typesafe-sdk
```

#### Mẫu Code Đồng Bộ (Synchronous Client):
```python
import os
from typesafe_sdk import TypeSafeClient, Noul, Choice, Score

client = TypeSafeClient(api_key=os.getenv("TYPESAFE_API_KEY"))

# Gửi yêu cầu đánh giá trạng thái
result = client.system_one(
    model="jev-latest",
    state={
        "user_id": "usr_9982",
        "action": "password_reset_request",
        "ip_country": "VN",
        "failed_attempts": 5
    },
    questions={
        "is_suspicious": Noul(
            instructions="Hành động này có dấu hiệu chiếm đoạt tài khoản đáng ngờ không?"
        ),
        "risk_level": Choice(
            instructions="Phân loại mức độ rủi ro:",
            criteria={
                "low": "Hành vi thông thường, tỷ lệ giả mạo thấp",
                "medium": "Có dấu hiệu bất thường nhẹ, nên yêu cầu OTP bổ sung",
                "high": "Khả năng tấn công Brute-force cao, cần khóa tạm thời"
            }
        ),
        "threat_score": Score(
            instructions="Chấm điểm mức độ đe dọa từ 1 đến 3:",
            criteria=["An toàn", "Cảnh báo", "Nguy hiểm"]
        )
    }
)

# Đọc kết quả dạng typed an toàn
print("Suspicious Prob:", result.nouls["is_suspicious"].noul)
print("Chosen Risk:", result.choices["risk_level"].choice)
print("Risk Confidence:", result.choices["risk_level"].confidence)
print("Threat Score:", result.scores["threat_score"].score)
```

#### Mẫu Code Bất Đồng Bộ (Asynchronous Client với `asyncio`):
```python
import asyncio
from typesafe_sdk import AsyncTypeSafeClient, Noul

async def check_content(text: str):
    async with AsyncTypeSafeClient() as client:
        response = await client.system_one(
            state=text,
            questions={"is_clean": Noul(instructions="Nội dung có hoàn toàn lành mạnh không?")}
        )
        return response.nouls["is_clean"].noul

# Chạy kiểm tra song song hàng loạt
async def main():
    comments = ["Bài viết rất hay!", "Đồ lừa đảo cút đi", "Giao hàng hơi lâu"]
    tasks = [check_content(c) for c in comments]
    results = await asyncio.gather(*tasks)
    print("Kết quả kiểm duyệt:", results)

asyncio.run(main())
```

---

### 2. TypeScript / JavaScript SDK (`@typesafe-ai/sdk`)

Cài đặt package:
```bash
npm install @typesafe-ai/sdk
# hoặc
pnpm add @typesafe-ai/sdk
# hoặc
bun add @typesafe-ai/sdk
```

Triển khai mã nguồn:
```typescript
import { TypeSafeClient, noul, choice, score } from '@typesafe-ai/sdk';

const client = new TypeSafeClient({
  apiKey: process.env.TYPESAFE_API_KEY
});

async function main() {
  const response = await client.systemOne({
    model: 'jev-1.13.0',
    state: 'Đơn hàng #VN-8812 giao muộn 4 ngày, thức ăn đã bị nguội lạnh.',
    questions: {
      isComplaint: noul('Khách hàng có đang khiếu nại về chất lượng dịch vụ không?'),
      department: choice('Chuyển giao tới:', {
        kitchen: 'Bộ phận bếp chế biến',
        logistics: 'Bộ phận tài xế / giao vận',
        cs: 'Bộ phận tổng đài viên hoàn tiền'
      }),
      dissatisfaction: score('Mức độ không hài lòng:', [
        'Nhẹ: Góp ý xây dựng',
        'Vừa: Bực mình nhưng chấp nhận được',
        'Nặng: Yêu cầu đền bù và hủy dùng app'
      ])
    }
  });

  const { answers } = response;
  console.log(`Khiếu nại: ${answers.isComplaint.noul > 0.8}`);
  console.log(`Phòng ban: ${answers.department.choice} (Độ tin cậy: ${answers.department.confidence})`);
  console.log(`Điểm bức xúc: ${answers.dissatisfaction.score}/3.0`);
}

main();
```

---

## 4.5. Tích Hợp Qua Các Gateway & AI Proxies Phổ Biến

### 1. Tích Hợp Qua LiteLLM Proxy
Nếu hạ tầng công ty của bạn đang sử dụng LiteLLM để quản lý tập trung các AI providers, bạn chỉ cần cấu hình model trong file `config.yaml`:

```yaml
model_list:
  - model_name: systemone-jev
    litellm_params:
      model: typesafe/jev-latest
      api_key: os.environ/TYPESAFE_API_KEY
      api_base: https://api.typesafe.ai/v1
```

### 2. Tích Hợp Qua OpenRouter
Jev được định tuyến thông qua OpenRouter với định danh mô hình:
```bash
curl -X POST https://openrouter.ai/api/v1/chat/completions \
  -H "Authorization: Bearer $OPENROUTER_API_KEY" \
  -d '{
    "model": "typesafe/jev",
    "messages": [ ... ]
  }'
```

---

## 4.6. Bảng Tra Cứu Mã Lỗi HTTP & Khắc Phục (Error Handling)

Khi xảy ra lỗi, API luôn trả về mã HTTP Status tương ứng cùng với thân phản hồi JSON chuẩn cấu trúc lỗi:

```json
{
  "error": {
    "code": "invalid_primitive_criteria",
    "message": "Primitive 'score' criteria must contain between 2 and 10 levels.",
    "param": "questions.my_score.criteria",
    "type": "invalid_request_error"
  }
}
```

| HTTP Status | Error Code | Nguyên Nhân Gốc | Hướng Khắc Phục |
| :--- | :--- | :--- | :--- |
| **`400 Bad Request`** | `missing_state` | Không cung cấp trường `state` hoặc để rỗng | Bổ sung nội dung hoặc JSON vào trường `state` |
| **`400 Bad Request`** | `invalid_primitive_criteria` | Câu hỏi `Choice` < 2 hoặc > 255 options, hoặc `Score` < 2 hoặc > 10 levels | Kiểm tra lại số lượng phần tử trong mảng/object `criteria` |
| **`401 Unauthorized`** | `invalid_api_key` | Token sai, hết hạn hoặc chưa truyền Bearer Token | Kiểm tra biến môi trường `TYPESAFE_API_KEY` trong console |
| **`403 Forbidden`** | `danger_zone_opt_in_required` | Dùng câu hỏi ảnh hoặc Box mà quên truyền header | Bổ sung header `TypeSafe-Danger-Zone-Images: true` |
| **`413 Payload Too Large`**| `context_length_exceeded` | Kích thước state vượt quá 64.000 tokens chuẩn | Kích hoạt header `TypeSafe-Danger-Zone-Long-Context: true` hoặc cắt nhỏ state |
| **`429 Too Many Requests`**| `rate_limit_exceeded` | Vượt quá giới hạn RPM hoặc TPM của Tier hiện tại | Triển khai Exponential Backoff & Jitter hoặc liên hệ nâng cấp Tier |
| **`500 Internal Error`** | `internal_system_error` | Lỗi cụm máy chủ TypeSafe AI | Thực hiện retry tự động sau 1-2 giây |
| **`503 Service Unavailable`**| `engine_overloaded` | Máy chủ đang bảo trì hoặc quá tải tạm thời | Dùng Circuit Breaker để chuyển hướng fallback |

---

## 4.7. Chiến Lược Retry & Exponential Backoff Chuẩn Production

```python
import time
import random
from typesafe_sdk import TypeSafeClient
from typesafe_sdk.errors import RateLimitError, ServiceUnavailableError

client = TypeSafeClient()

def call_jev_with_retry(payload, max_retries=4):
    base_delay = 0.5  # 500ms
    for attempt in range(max_retries):
        try:
            return client.system_one(**payload)
        except (RateLimitError, ServiceUnavailableError) as err:
            if attempt == max_retries - 1:
                raise err
            # Thuật toán Exponential Backoff kết hợp Full Jitter
            sleep_time = (base_delay * (2 ** attempt)) + random.uniform(0, 0.2)
            time.sleep(sleep_time)
```
Mã nguồn trên đảm bảo hệ thống không bị hiện tượng "thundering herd" khi gặp lỗi 429 hoặc 503, tự động khôi phục trong vòng dưới 2 giây.

---

### ⏭️ Điều Hướng Tài Liệu
* **Trang trước:** [← Chương 3: Danh Mục Models & Thông Số Kỹ Thuật](03_models_and_specifications.md)
* **Mục lục:** [🏠 Quay lại README](../README.md)
* **Trang tiếp theo:** [Chương 5: Tuyển Tập Thực Chiến Cookbooks & Kiến Trúc Mẫu →](05_cookbooks_and_patterns.md)

