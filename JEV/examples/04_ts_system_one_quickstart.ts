/**
 * Ví Dụ 04: TypeScript / Node.js Quickstart Với @typesafe-ai/sdk
 * Triển khai mô hình quyết định Jev trong môi trường Node.js / Bun / Next.js
 */

import { TypeSafeClient, noul, choice, score } from '@typesafe-ai/sdk';

// Tự động đọc biến môi trường TYPESAFE_API_KEY
const client = new TypeSafeClient({
  apiKey: process.env.TYPESAFE_API_KEY || 'jv_live_demo_key_placeholder'
});

interface CustomerReview {
  reviewId: string;
  userName: string;
  ratingStars: number;
  comment: string;
}

async function analyzeReview(review: CustomerReview) {
  console.log(`\n[+] Đang phân tích đánh giá: ${review.reviewId} - "${review.comment}"`);

  try {
    const response = await client.systemOne({
      model: 'jev-latest',
      state: {
        stars: review.ratingStars,
        text: review.comment,
        author: review.userName
      },
      questions: {
        isPositive: noul('Đánh giá này có nhìn chung mang hàm ý khen ngợi hoặc hài lòng không?'),
        productAspect: choice('Khía cạnh sản phẩm được nhắc tới nhiều nhất:', {
          delivery: 'Tốc độ giao hàng hoặc thái độ shipper',
          packaging: 'Quy cách đóng gói hộp sản phẩm',
          quality: 'Chất lượng độ bền và hiệu năng thực tế của sản phẩm',
          price: 'Giá cả đắt hay rẻ so với thị trường'
        }),
        retentionRisk: score('Mức độ nguy cơ khách hàng sẽ chuyển sang đối thủ cạnh tranh:', [
          'Thấp: Khách hàng trung thành hoặc chỉ góp ý nhẹ nhàng',
          'Vừa: Có sự thất vọng nhưng vẫn có khả năng tiếp tục mua',
          'Rất cao: Khách khẳng định sẽ không bao giờ quay lại mua hàng'
        ])
      }
    });

    const { answers, usage, model } = response;

    console.log(`==> Mô hình thực thi: ${model}`);
    console.log(`==> Xác suất hài lòng: ${(answers.isPositive.noul * 100).toFixed(1)}%`);
    console.log(`==> Khía cạnh chính: ${answers.productAspect.choice} (Độ tin cậy: ${answers.productAspect.confidence})`);
    console.log(`==> Điểm nguy cơ mất khách: ${answers.retentionRisk.score.toFixed(2)} / 3.0`);
    console.log(`==> Token tiêu thụ: Input=${usage.input_tokens}, Output=${usage.output_tokens} (Chi phí output: $0)`);

    // Logic rẽ nhánh nghiệp vụ phần mềm:
    if (answers.retentionRisk.score > 2.2) {
      console.log(`[ACTION] 🚨 Kích hoạt voucher 20% xoa dịu khách hàng cho ID: ${review.reviewId}`);
    } else if (answers.isPositive.noul > 0.85) {
      console.log(`[ACTION] ⭐ Đẩy đánh giá này lên mục 'Khách hàng tiêu biểu' trên trang chủ.`);
    }

  } catch (error) {
    console.error('[!] Lỗi khi gọi TypeSafe API:', error);
  }
}

async function main() {
  const sampleReviews: CustomerReview[] = [
    {
      reviewId: 'REV-01',
      userName: 'Trần Văn B',
      ratingStars: 1,
      comment: 'Tai nghe mới dùng được 2 ngày đã bị tịt một bên tai. Đã nhắn tin shop nhưng không ai thèm trả lời. Quá thất vọng, không bao giờ mua ở đây nữa!'
    },
    {
      reviewId: 'REV-02',
      userName: 'Lê Thị C',
      ratingStars: 5,
      comment: 'Giao hàng siêu nhanh, mới đặt hôm qua hôm nay đã nhận được. Chất âm rất ấm và êm tai, đóng gói bọc xốp cẩn thận.'
    }
  ];

  for (const r of sampleReviews) {
    await analyzeReview(r);
  }
}

main();

