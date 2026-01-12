"""
Project: Email Header Analyzer (Mail Forensics)
Description:
Traces the origin of an email by analyzing header metadata.
Extracts Received-From IP addresses, performs GeoIP lookup,
and checks SPF / DKIM pass-fail status.

Tools Used:
Python, Mail parsing libraries
"""

from email import message_from_string
from ip_extractor import extract_received_ips
from geoip import geoip_lookup


def read_header_file(filename):
    """Reads raw email header from a text file"""
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


def parse_email_header(header_text):
    """Parses raw header text into structured format"""
    return message_from_string(header_text)


def display_headers(parsed_msg):
    """Displays important email header fields"""
    print("\n--- Parsed Email Headers ---\n")
    for key, value in parsed_msg.items():
        print(f"{key}: {value}")


def display_spf_dkim(parsed_msg):
    """Displays SPF and DKIM authentication results"""
    print("\n--- SPF / DKIM Status ---\n")
    print("SPF Status :", parsed_msg.get("Received-SPF", "Not Found"))
    print("DKIM Status:", parsed_msg.get("DKIM-Signature", "Not Found"))
    print("Auth Result:", parsed_msg.get("Authentication-Results", "Not Found"))


def main():
    print("\n========== EMAIL HEADER ANALYZER ==========\n")

    # Step 1: Read email header
    header_text = read_header_file("sample_header.txt")

    # Step 2: Parse header (Mail parsing)
    parsed_msg = parse_email_header(header_text)

    # Step 3: Display parsed headers (optional but useful)
    display_headers(parsed_msg)

    # Step 4: Extract Received-From IP addresses
    ips = extract_received_ips(parsed_msg)

    print("\n--- Extracted IP Addresses ---\n")
    if not ips:
        print("No IP addresses found in Received headers.")
    else:
        for ip in ips:
            print(ip)

    # Step 5: GeoIP lookup for extracted IPs
    print("\n--- GeoIP Analysis ---\n")
    for ip in ips:
        geo_info = geoip_lookup(ip)
        print(f"IP Address : {geo_info.get('IP')}")
        print(f"Country    : {geo_info.get('Country')}")
        print(f"City       : {geo_info.get('City')}")
        print(f"ISP        : {geo_info.get('ISP')}")
        print("-" * 30)

    # Step 6: SPF & DKIM check (Tip-based analysis)
    display_spf_dkim(parsed_msg)

    print("\n========== ANALYSIS COMPLETE ==========\n")


if __name__ == "__main__":
    main()
