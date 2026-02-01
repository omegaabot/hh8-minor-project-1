import re
from geo_lookup import get_geo

def extract_ip(received_field):
    """Extract IP from a Received header using regex."""
    match = re.search(r"\b\d{1,3}(?:\.\d{1,3}){3}\b", received_field)  # Match valid IPv4 format
    return match.group(0) if match else None

def google_geolocation(ip_address):
    """Fallback geolocation for Google IP ranges."""
    return {
        "IP": ip_address,
        "City": "Mountain View",
        "Region": "California",
        "Country": "United States",
    }

def trace_email_origin(received_headers):
    """Trace the email origin by prioritizing non-Google hops."""
    for entry in received_headers:
        received_from = entry.get("from", "")
        ip_address = extract_ip(received_from)

        # Debugging Print: Check extracted IP address
        print(f"DEBUG: Processing Received header - {received_from}")
        if ip_address:
            # Handle Google IP ranges
            if ip_address.startswith(("172.217.", "216.58.", "209.", "74.125.")) or "google" in received_from.lower():
                return google_geolocation(ip_address)
            
            # Skip private IPs; prioritize routable addresses
            if not ip_address.startswith(("192.168", "10.", "127.", "169.254")):
                return get_geo(ip_address)
            
    # Return "Unknown" if all hops fail
    return {"IP": "Unknown", "City": "Unknown", "Region": "Unknown", "Country": "Unknown"}