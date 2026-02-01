from email_analyzer_basic import parse_email, validate_authentication
from email_origin_tracing import trace_email_origin
from threat_lookup import check_ip_reputation
from geo_map import create_geo_map

def analyze_email(file_path):
    """Main function for enhanced email header analysis with result dictionary."""
    
    # Parse email headers
    headers, received_headers = parse_email(file_path)

    # Extract Received-From IP and GeoIP
    origin_info = trace_email_origin(received_headers)
    ip_address = origin_info.get("IP", "Unknown")

    # Build result dictionary
    results = {
        "spf": headers.get("Received-SPF", "SPF Result: Not Found"),
        "dkim": headers.get("Authentication-Results", "DKIM Result: Not Found"),
        "received_ip": ip_address,
        "city": origin_info.get("City", "Unknown"),
        "region": origin_info.get("Region", "Unknown"),
        "country": origin_info.get("Country", "Unknown"),
        "abuse_score": "Unknown",
        "total_reports": 0,
        "categories": [],
        "map_file": None,
    }

    # Check IP reputation
    if ip_address != "Unknown":
        reputation_info = check_ip_reputation(ip_address)
        results["abuse_score"] = reputation_info.get("AbuseScore", "Unknown")
        results["total_reports"] = reputation_info.get("TotalReports", 0)
        results["categories"] = reputation_info.get("Categories", [])

    # Generate the geolocation map
    map_file = create_geo_map(origin_info)
    results["map_file"] = map_file

    return results