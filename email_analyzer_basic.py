import mailparser

def parse_email(file_path):
    """Parse email file to extract headers and Received data."""
    try:
        mail = mailparser.parse_from_file(file_path)
        
        # Print headers
        print("\n--- Email Headers ---")
        for key, value in mail.headers.items():
            print(f"{key}: {value}")
        
        # Print Received-from tracing
        print("\n--- Received Headers ---")
        for received in mail.received:
            print(received)
        
        return mail.headers, mail.received
    except Exception as e:
        print(f"Error parsing email: {str(e)}")

def validate_authentication(headers):
    """Extract SPF and DKIM validation results."""
    spf_result = headers.get('Received-SPF', 'SPF Result: Not Found')
    dkim_result = headers.get('Authentication-Results', 'DKIM Result: Not Found')
    
    print("\n--- SPF & DKIM Validation ---")
    print(spf_result)
    print(dkim_result)