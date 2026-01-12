"""
ip_extractor.py
Purpose: Extract IP addresses from Received headers
"""

import re


def extract_received_ips(parsed_msg):
    """
    Extracts IP addresses from 'Received' headers
    """
    received_headers = parsed_msg.get_all("Received")
    if not received_headers:
        return []

    ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    ips = []

    for header in received_headers:
        found_ips = re.findall(ip_pattern, header)
        ips.extend(found_ips)

    # Remove duplicates
    return list(set(ips))
