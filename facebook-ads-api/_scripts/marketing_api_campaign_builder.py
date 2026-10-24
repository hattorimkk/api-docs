#!/usr/bin/env python3
"""
Meta Marketing API - Full Programmatic Campaign Builder (v22.0)
Xay dung luong tao chien dich quang cao tu dong 3 tang:
Campaign (ODAX) -> Ad Set (Targeting & Budget) -> Creative -> Ad
Thiet ke bang thu vien chuan Python (urllib.request), chay duoc ngay khong can cai them thu vien ngoai.
"""

import json
import sys
import urllib.request
import urllib.error

BASE_URL = "https://graph.facebook.com/v22.0"

def _post_json(url: str, payload: dict) -> dict:
    req_data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(
        url,
        data=req_data,
        headers={"Content-Type": "application/json"}
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        error_body = e.read().decode('utf-8')
        try:
            parsed = json.loads(error_body)
            raise Exception(f"HTTP {e.code} Meta Error: {parsed.get('error', parsed)}")
        except Exception:
            raise Exception(f"HTTP {e.code}: {error_body}")

def create_campaign(ad_account_id: str, access_token: str, name: str, objective: str = "OUTCOME_SALES", daily_budget: str = "1000000"):
    url = f"{BASE_URL}/act_{ad_account_id}/campaigns"
    payload = {
        "name": name,
        "objective": objective,
        "status": "PAUSED",
        "buying_type": "AUCTION",
        "special_ad_categories": [],
        "daily_budget": daily_budget,
        "access_token": access_token
    }
    res = _post_json(url, payload)
    return res["id"]

def create_adset(ad_account_id: str, access_token: str, campaign_id: str, name: str, pixel_id: str):
    url = f"{BASE_URL}/act_{ad_account_id}/adsets"
    payload = {
        "name": name,
        "campaign_id": campaign_id,
        "status": "PAUSED",
        "billing_event": "IMPRESSIONS",
        "optimization_goal": "OFFSITE_CONVERSIONS",
        "promoted_object": {
            "pixel_id": pixel_id,
            "custom_event_type": "PURCHASE"
        },
        "bid_strategy": "LOWEST_COST_WITHOUT_BID_CAP",
        "targeting": {
            "geo_locations": {"countries": ["VN"]},
            "age_min": 22,
            "age_max": 45,
            "genders": [1, 2]
        },
        "access_token": access_token
    }
    res = _post_json(url, payload)
    return res["id"]

def create_ad_creative(ad_account_id: str, access_token: str, page_id: str, image_hash: str, link_url: str, headline: str, message: str):
    url = f"{BASE_URL}/act_{ad_account_id}/adcreatives"
    payload = {
        "name": f"Creative - {headline}",
        "object_story_spec": {
            "page_id": page_id,
            "link_data": {
                "image_hash": image_hash,
                "link": link_url,
                "message": message,
                "name": headline,
                "call_to_action": {"type": "SHOP_NOW"}
            }
        },
        "access_token": access_token
    }
    res = _post_json(url, payload)
    return res["id"]

def create_ad(ad_account_id: str, access_token: str, adset_id: str, creative_id: str, name: str):
    url = f"{BASE_URL}/act_{ad_account_id}/ads"
    payload = {
        "name": name,
        "adset_id": adset_id,
        "creative": {"creative_id": creative_id},
        "status": "PAUSED",
        "url_tags": "utm_source=facebook&utm_medium={{placement}}&utm_campaign={{campaign.name}}&utm_content={{ad.name}}",
        "access_token": access_token
    }
    res = _post_json(url, payload)
    return res["id"]

if __name__ == "__main__":
    print("=== Meta Marketing API Campaign Builder (v22.0) ===")
    print("Cac ham san sang su dung:")
    print("1. create_campaign(...)")
    print("2. create_adset(...)")
    print("3. create_ad_creative(...)")
    print("4. create_ad(...)")

