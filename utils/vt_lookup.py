import requests
from config import VT_API_KEY

def vt_lookup(value, ioc_type):
    base_url = "https://www.virustotal.com/api/v3"

    if ioc_type == "ip":
        url = f"{base_url}/ip_addresses/{value}"
    elif ioc_type == "domain":
        url = f"{base_url}/domains/{value}"
    elif ioc_type == "hash":
        url = f"{base_url}/files/{value}"
    else:
        return None

    headers = {"x-apikey": VT_API_KEY}

    try:
        response = requests.get(url, headers=headers)
        data = response.json()

        stats = data["data"]["attributes"]["last_analysis_stats"]
        return stats

    except Exception as e:
        print(f"[ERROR] VT Lookup failed: {e}")
        return None
