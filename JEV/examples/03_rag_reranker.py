#!/usr/bin/env python3
"""
Ví Dụ 03: Tái Sắp Xếp & Lọc Dữ Liệu RAG (RAG Passage Re-ranking)
Đánh giá độ liên quan ngữ nghĩa của các đoạn trích (chunks) trước khi đưa vào LLM Context.
"""

import os
from typesafe_sdk import TypeSafeClient, Score

api_key = os.getenv("TYPESAFE_API_KEY", "jv_live_demo_key_placeholder")
client = TypeSafeClient(api_key=api_key)

def rerank_knowledge_chunks(user_query: str, chunks: list[dict], min_score=1.5) -> list[dict]:
    """
    Gửi câu hỏi của người dùng và danh sách các chunk vào Jev để chấm điểm song song.
    """
    print(f"\n[+] Câu hỏi người dùng: \"{user_query}\"")
    print(f"[+] Số lượng chunks đầu vào: {len(chunks)}")

    # Xây dựng danh sách câu hỏi Score song song cho từng chunk
    questions = {}
    for idx, c in enumerate(chunks):
        questions[f"relevance_{idx}"] = Score(
            instructions=(
                f"Đánh giá mức độ đoạn văn bản ID '{c['id']}' trả lời trực tiếp cho câu hỏi: '{user_query}'"
            ),
            criteria=[
                "Cấp 1: Không liên quan - Đoạn trích chỉ vô tình trùng một số từ khóa nhưng nội dung không ăn nhập",
                "Cấp 2: Liên quan một phần - Đề cập đến ngữ cảnh chung hoặc công nghệ liên quan nhưng không có câu trả lời cụ thể",
                "Cấp 3: Trả lời trực tiếp - Cung cấp chính xác thông số, hướng dẫn hoặc giải pháp mà câu hỏi tìm kiếm"
            ]
        )

    # Đưa toàn bộ ngữ cảnh vào state
    state_payload = {
        "query": user_query,
        "passages": chunks
    }

    response = client.system_one(
        model="jev-latest",
        state=state_payload,
        questions=questions
    )

    # Trích xuất điểm số và gán ngược lại vào từng chunk
    results = []
    for idx, c in enumerate(chunks):
        score_info = response.scores[f"relevance_{idx}"]
        results.append({
            "id": c["id"],
            "title": c["title"],
            "text": c["text"],
            "relevance_score": round(score_info.score, 2),
            "confidence": round(score_info.confidence, 4)
        })

    # Sắp xếp giảm dần theo điểm số
    results.sort(key=lambda x: x["relevance_score"], reverse=True)

    # Lọc bỏ các chunk dưới ngưỡng chất lượng
    filtered_results = [r for r in results if r["relevance_score"] >= min_score]
    return filtered_results

def main():
    query = "Làm thế nào để cấu hình thời gian hết hạn (TTL) cho một khóa trong Redis bằng lệnh Python?"

    raw_chunks = [
        {
            "id": "chunk_01",
            "title": "Cài đặt Redis Server trên Ubuntu 22.04",
            "text": "Để cài đặt Redis trên Ubuntu, bạn dùng lệnh sudo apt install redis-server. Sau đó kiểm tra trạng thái bằng systemctl status redis."
        },
        {
            "id": "chunk_02",
            "title": "Sử dụng redis-py: Thiết lập TTL với lệnh expire",
            "text": "Trong thư viện redis-py của Python, bạn có thể đặt thời gian sống cho một key bằng lệnh r.expire('my_key', 3600) (tính theo giây), hoặc truyền tham số ex=3600 trực tiếp vào hàm r.set('my_key', 'val', ex=3600)."
        },
        {
            "id": "chunk_03",
            "title": "Các kiểu dữ liệu chính trong Redis",
            "text": "Redis hỗ trợ nhiều kiểu dữ liệu phong phú bao gồm Strings, Hashes, Lists, Sets và Sorted Sets với hiệu năng cực cao trong bộ nhớ RAM."
        },
        {
            "id": "chunk_04",
            "title": "Quản lý bộ nhớ và chính sách Eviction trong Redis",
            "text": "Khi Redis hết bộ nhớ RAM được cấp phát, nó áp dụng các chính sách như volatile-lru, allkeys-lru để xóa các key có TTL hoặc key ít dùng nhất."
        }
    ]

    try:
        ranked = rerank_knowledge_chunks(query, raw_chunks)
        print("\n==> KẾT QUẢ TÁI SẮP XẾP & LỌC CHUNKS:")
        for rank, item in enumerate(ranked, 1):
            print(f"{rank}. [{item['id']}] Điểm: {item['relevance_score']}/3.0 (Conf: {item['confidence']}) - {item['title']}")
            print(f"   Trích đoạn: {item['text'][:110]}...")
    except Exception as e:
        print(f"[!] Lỗi khi gọi API: {e}")

if __name__ == "__main__":
    main()

