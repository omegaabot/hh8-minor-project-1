"""
geoip.py
Purpose: Perform GeoIP lookup for extracted IP addresses
"""

import requests


def geoip_lookup(ip):
    """
    Returns geographic information for an IP address
    """
    try:
        response = requests.get(
            f"http://ip-api.com/json/{ip}",
            timeout=5
        )
        data = response.json()

        return {
            "IP": ip,
            "Country": data.get("country"),
            "City": data.get("city"),
            "ISP": data.get("isp")
        }

    except Exception:
        return {
            "IP": ip,
            "Country": "Unknown",
            "City": "Unknown",
            "ISP": "Unknown"
        }
