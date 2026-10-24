#!/usr/bin/env python3
"""
Meta Insights API Exporter
Tu dong thuc thi truy van bao cao bat dong bo (Async Insights Job)
va xuat ket qua ve dinh dang JSON.
Thiet ke bang thu vien chuan Python (urllib.request), khong can cai them thu vien ngoai.
"""

import time
import json
import sys
import urllib.request
import urllib.error

BASE_URL = "https://graph.facebook.com/v22.0"

def _http_get(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": "MetaInsightsClient/1.0"})
    with urllib.request.urlopen(req, timeout=20) as resp:
        return json.loads(resp.read().decode('utf-8'))

def _http_post(url: str, payload: dict) -> dict:
    req_data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(
        url,
        data=req_data,
        headers={"Content-Type": "application/json", "User-Agent": "MetaInsightsClient/1.0"}
    )
    with urllib.request.urlopen(req, timeout=20) as resp:
        return json.loads(resp.read().decode('utf-8'))

def export_async_insights(ad_account_id: str, access_token: str, date_preset: str = "last_7d", level: str = "campaign"):
    post_url = f"{BASE_URL}/act_{ad_account_id}/insights"
    payload = {
        "level": level,
        "fields": "campaign_name,spend,impressions,reach,clicks,ctr,cpc,cpm,actions,action_values,purchase_roas",
        "date_preset": date_preset,
        "access_token": access_token
    }
    
    print(f"[*] Dang khoi tao Async Insights Job cho tai khoan act_{ad_account_id}...")
    try:
        init_res = _http_post(post_url, payload)
    except urllib.error.HTTPError as e:
        raise Exception(f"Loi khoi tao Job: {e.read().decode('utf-8')}")
        
    report_id = init_res.get("report_run_id")
    print(f"[+] Job ID thanh cong: {report_id}")
    
    # Cho tien trinh hoan thanh
    while True:
        status_url = f"{BASE_URL}/{report_id}?access_token={access_token}"
        status_res = _http_get(status_url)
        status = status_res.get("async_status")
        percent = status_res.get("async_percent_completion", 0)
        print(f"[*] Tien do xuat bao cao: {percent}% ({status})")
        
        if status == "Job Completed":
            break
        elif status in ["Job Failed", "Job Skipped"]:
            raise Exception(f"Loi tien trinh bao cao: {status}")
            
        time.sleep(3)
        
    # Lay du lieu
    data_url = f"{BASE_URL}/{report_id}/insights?limit=500&access_token={access_token}"
    data_res = _http_get(data_url)
    return data_res.get("data", [])

if __name__ == "__main__":
    print("=== Meta Insights API Exporter (v22.0) ===")
    print("Su dung ham export_async_insights(ad_account_id, access_token, date_preset='last_7d')")

