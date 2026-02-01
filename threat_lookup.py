import requests
from config import ABUSEIPDB_API_KEY  # Import the API key from the configuration file

def check_ip_reputation(ip_address):
    """Check IP reputation using AbuseIPDB API."""
    url = f"https://api.abuseipdb.com/api/v2/check"

    headers = {
        "Accept": "application/json",
        "Key": ABUSEIPDB_API_KEY,  # Fetch API key dynamically from config.py
    }

    params = {
        "ipAddress": ip_address,
        "maxAgeInDays": 90,  # Check reports from the last 90 days
    }

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        return {
            "IP": ip_address,
            "AbuseScore": data["data"].get("abuseConfidenceScore", "Unknown"),
            "TotalReports": data["data"].get("totalReports", 0),
            "Categories": data["data"].get("category", []),
        }
    else:
        return {"IP": ip_address, "Error": f"Failed to fetch data. Status Code: {response.status_code}"}