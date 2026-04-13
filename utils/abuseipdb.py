import requests
from config import ABUSEIPDB_API_KEY

def check_ip(ip):
    url = "https://api.abuseipdb.com/api/v2/check"

    headers = {
        "Key": ABUSEIPDB_API_KEY,
        "Accept": "application/json"
    }

    params = {
        "ipAddress": ip,
        "maxAgeInDays": 90
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        data = response.json()

        # 🔥 FIX: Check if 'data' exists
        if "data" not in data:
            print(f"[ERROR] AbuseIPDB API issue: {data}")
            return None

        return {
            "abuse_score": data["data"]["abuseConfidenceScore"],
            "total_reports": data["data"]["totalReports"]
        }

    except Exception as e:
        print(f"[ERROR] AbuseIPDB failed: {e}")
        return None
