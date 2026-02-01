import requests

def get_geo(ip_address):
    """Fetch geolocation data for the given IP address using ip-api.com."""
    url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "IP": ip_address,
            "City": data.get("city", "Unknown"),
            "Region": data.get("regionName", "Unknown"),
            "Country": data.get("country", "Unknown"),
            "ISP": data.get("isp", "Unknown"),
        }
    else:
        return {"IP": ip_address, "Error": "Failed to fetch geolocation data"}

def fetch_ips_and_geo(received_headers):
    """Extract IPs from Received headers and fetch geolocation."""
    geo_info = []
    for entry in received_headers:
        ip_field = entry.get("from", "")
        # Extract IP-like pattern (simple check)
        ip_address = ip_field.split()[-1] if ip_field else None
        if ip_address and ip_address.replace('.', '').isdigit():  # Basic validation
            geo_data = get_geo(ip_address)
            geo_info.append(geo_data)
    
    return geo_info