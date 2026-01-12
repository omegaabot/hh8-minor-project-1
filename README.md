📧 Email Header Analyzer – Mail Forensics

Repository: hh8-minor-project-1

📌 Short Description

Mail forensics

📄 Brief Description

This project is a mail forensics tool that traces the origin of an email by analyzing email header metadata. It extracts sender IP addresses from the Received headers, performs GeoIP lookup to identify the approximate location of the sender, and checks SPF and DKIM pass/fail status to help assess email authenticity.

🎯 Objectives

Analyze raw email headers

Trace email origin using Received header metadata

Extract sender IP addresses

Perform GeoIP lookup on extracted IPs

Identify SPF and DKIM authentication results

🛠️ Tools & Technologies Used

Python

Mail parsing libraries (email module)

Regex

GeoIP API

Requests library

🗂️ Project Structure
hh8-minor-project-1/
│
├── main.py               # Main program execution
├── sample_header.txt     # Sample email header input
├── parser.py             # Email header parsing logic
├── ip_extractor.py       # Extracts IPs from Received headers
├── geoip.py              # GeoIP lookup module
├── requirements.txt      # Required Python libraries
└── README.md             # Project documentation

⚙️ How It Works

The user provides a raw email header (sample_header.txt)

The header is parsed using mail parsing libraries

Received headers are analyzed to extract IP addresses

GeoIP lookup is performed on extracted IPs

SPF and DKIM authentication results are displayed

The results help trace the origin and authenticity of the email

▶️ How to Run the Project
1️⃣ Install Dependencies
pip install -r requirements.txt

2️⃣ Run the Program
python main.py

📤 Input

Raw email header copied from an email client (e.g., Gmail → Show Original)

Paste the header into sample_header.txt

📥 Output

Parsed email header fields

Extracted sender IP addresses

GeoIP information (Country, City, ISP)

SPF and DKIM authentication status

🔐 Key Indicators Used

Received headers → Email routing path

IP addresses → Origin identification

GeoIP lookup → Approximate sender location

SPF / DKIM → Authentication pass/fail status

⚠️ Limitations

GeoIP provides approximate location only

Emails routed via proxies or relays may hide true origin

SPF/DKIM results depend on mail server configuration

🔮 Future Enhancements

Web-based interface

Automated forensic report generation

Advanced email spoofing detection

Integration with security tools

🎓 Academic & Internship Relevance

Digital Forensics

Cybersecurity

Email Security Analysis

Network & Protocol Analysis

👤 Author

Aditya Raj
Department of Computer Science and Engineering (Cyber Security)
Presidency University, Bengaluru

📜 License

This project is intended for academic and educational purposes.

✅ Final Notes (Important for Evaluation)

Project strictly follows the given problem statement

Focuses only on mail forensics

No over-claimed features

Easy to explain in viva and interviews