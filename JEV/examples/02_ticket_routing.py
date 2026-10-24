#!/usr/bin/env python3
"""
Ví Dụ 02: Phân Luồng Ticket Hỗ Trợ Khách Hàng Với Ngưỡng Tin Cậy (Confidence-Gated Routing)
Tự động hóa chuyển giao yêu cầu tới đúng phòng ban và xếp hạng độ ưu tiên SLA.
"""

import os
import json
from typesafe_sdk import TypeSafeClient, Choice, Score, Noul

api_key = os.getenv("TYPESAFE_API_KEY", "jv_live_demo_key_placeholder")
client = TypeSafeClient(api_key=api_key)

def route_customer_ticket(ticket: dict) -> dict:
    """
    Xử lý thông tin ticket và đưa ra quyết định phân luồng chính xác.
    """
    ticket_text = f"Tiêu đề: {ticket.get('subject')}\nNội dung: {ticket.get('body')}\nKhách hàng: {ticket.get('tier', 'standard')}"
    print(f"\n[+] Đang xử lý Ticket ID: {ticket.get('id')} - \"{ticket.get('subject')}\"")

    response = client.system_one(
        model="jev-1.13.0",
        state=ticket_text,
        questions={
            "department": Choice(
                instructions="Phòng ban nào chịu trách nhiệm trực tiếp xử lý ticket này?",
                criteria={
                    "billing": "Thắc mắc hóa đơn, thẻ tín dụng bị trừ 2 lần, đòi hoàn tiền, xuất hóa đơn VAT",
                    "tech_support": "Ứng dụng bị sập, lỗi kết nối cơ sở dữ liệu, lỗi xác thực API, không gửi được email",
                    "sales": "Khách hàng muốn nâng cấp gói doanh nghiệp, báo giá số lượng lớn, gia hạn hợp đồng",
                    "account_security": "Tài khoản bị xâm nhập trái phép, nghi ngờ lộ mật khẩu hoặc mất 2FA"
                }
            ),
            "sla_urgency": Score(
                instructions="Chấm điểm mức độ khẩn cấp của yêu cầu theo thang thứ tự tăng dần:",
                criteria=[
                    "Mức 1: Thắc mắc thông thường, không ảnh hưởng vận hành, SLA 24h",
                    "Mức 2: Tính năng phụ bị lỗi, khách hàng vẫn làm việc được, SLA 8h",
                    "Mức 3: Hệ thống chính bị tê liệt hoặc ảnh hưởng nghiêm trọng tới doanh thu khách hàng, SLA 1h"
                ]
            ),
            "churn_risk": Noul(
                instructions="Khách hàng có thể hiện ý định hủy hợp đồng hoặc tẩy chay sản phẩm không?"
            )
        }
    )

    dept_ans = response.choices["department"]
    urgency_ans = response.scores["sla_urgency"]
    churn_prob = response.nouls["churn_risk"].noul

    # Kiểm tra ngưỡng tin cậy (Confidence Thresholding)
    CONFIDENCE_THRESHOLD = 0.85
    if dept_ans.confidence >= CONFIDENCE_THRESHOLD:
        routing_action = "AUTOMATED_DISPATCH"
        target_queue = f"queue_{dept_ans.choice}"
    else:
        # Nếu mô hình phân vân giữa các phòng ban, chuyển sang hàng đợi kiểm tra sơ bộ
        routing_action = "MANUAL_TRIAGE_REQUIRED"
        target_queue = "queue_human_triage"

    decision_summary = {
        "ticket_id": ticket.get("id"),
        "routing_action": routing_action,
        "target_queue": target_queue,
        "predicted_department": dept_ans.choice,
        "confidence": round(dept_ans.confidence, 4),
        "department_probabilities": {k: round(v, 4) for k, v in dept_ans.probabilities.items()},
        "urgency_score": round(urgency_ans.score, 2),
        "churn_risk_prob": round(churn_prob, 4)
    }
    return decision_summary

def main():
    sample_tickets = [
        {
            "id": "TCK-1001",
            "subject": "Thẻ visa của tôi vừa bị trừ 2 lần cho cùng một hóa đơn!",
            "body": "Chào bạn, hôm nay tôi gia hạn gói tháng nhưng hệ thống trừ tiền 2 lần (2x 50$). Vui lòng kiểm tra và hoàn lại cho tôi.",
            "tier": "standard"
        },
        {
            "id": "TCK-1002",
            "subject": "Hệ thống API trả về lỗi 500 liên tục trên môi trường Production",
            "body": "Toàn bộ webhook bên tôi không nhận được dữ liệu từ 2h chiều nay. Đơn hàng khách đang bị treo, chúng tôi đang thiệt hại hàng triệu đồng mỗi phút!",
            "tier": "enterprise"
        },
        {
            "id": "TCK-1003",
            "subject": "Cần hỗ trợ",
            "body": "Tôi không rõ tài khoản của tôi đang ở gói nào và tháng sau tôi muốn đổi thẻ ngân hàng.",
            "tier": "standard"
        }
    ]

    for tck in sample_tickets:
        try:
            res = route_customer_ticket(tck)
            print("==> KẾT QUẢ ĐỊNH TUYẾN:")
            print(json.dumps(res, indent=2, ensure_ascii=False))
            print("=" * 60)
        except Exception as err:
            print(f"[!] Lỗi API: {err}")

if __name__ == "__main__":
    main()

