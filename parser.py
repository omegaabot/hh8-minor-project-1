"""
parser.py
Purpose: Parse raw email header into structured format
"""

from email import message_from_string


def parse_header(header_text):
    """
    Converts raw email header text into a parsed email object
    """
    return message_from_string(header_text)
