# 📧 EMAIL HEADER ANALYZER 📧  
### Your Mail Forensics Sidekick!  

---

## 🚀 Introduction  
Ever wondered where that cryptic email in your inbox came from? 🕵️‍♀️ Fear not! The **Email Header Analyzer** is your personal Sherlock Holmes for email headers. Whether you're tracing the true origins of an email or validating its authenticity, this tool has got your back! Dive deep into those headers and uncover hidden details like IP addresses, SPF/DKIM results, and more. ✨  

---

## 🎯 Features & Tools Used  
Built lovingly using:  
- **Python** 🐍  
- **Mail-parser Libraries** 📤  

Key Features:  
- Analyze and parse email headers with ease.  
- Extract **Received-From IP addresses** like a pro.  
- Perform **GeoIP lookups** to pinpoint sender locations 🌏.  
- Validate critical security checks with **SPF/DKIM pass/fail statuses**.  
- Generate detailed forensic-grade reports 🕵️.  

---

## 🔍 How It Works  
### 🖋️ Step-by-Step Magic:
1. Read raw email header text from `.txt` files.  
2. Extract juicy details like **Received-From IP addresses** via mail-parsing powers.  
3. Perform **GeoIP lookups** for sender locations.  
   - Is the sender sipping coffee in Ashburn? Or somewhere suspicious? 🤔  
4. Validate the sender authenticity using **SPF and DKIM results**:  
   - **SPF** helps verify the allowed senders for domains!  
   - **DKIM** ensures secure signatures are in place.  

Results are all displayed neatly, like a well-organized detective’s notebook. 📝  

---

## 📂 Sample Output  
```
========= EMAIL HEADER ANALYZER =========

--- Parsed Email Headers ---
Received: from mail.example.com (mail.example.com. [8.8.8.8])
  by mx.google.com with ESMTP id x12s11234567qke.123.2025.01.10
    for <user@gmail.com>;
  Fri, 10 Jan 2025 10:10:10 +0530 (IST)
Authentication-Results: mx.google.com;
  spf=pass;
  dkim=pass;
DKIM-Signature: v=1; a=rsa-sha256; d=example.com;
From: Example Sender <test@example.com>
To: user@gmail.com
Subject: Test Email
Date: Fri, 10 Jan 2025 10:10:10 +0530

--- Extracted IP Addresses ---

8.8.8.8

--- GeoIP Analysis ---

IP Address : 8.8.8.8
Country    : United States
City       : Ashburn
ISP        : Google LLC

---------------------------------------

--- SPF / DKIM Status ---

SPF Status: pass (google.com: domain of example.com designates 8.8.8.8 as permitted sender)
DKIM Status: v=1; a=rsa-sha256; d=example.com;
Auth Result: mx.google.com;
  spf=pass;
  dkim=pass;

========= ANALYSIS COMPLETE =========
```

---

## 💻 Usage Instructions  
### 🏃 Run the Analyzer:
1. Clone the repository:
   ```bash
   git clone https://github.com/omegaabot/hh8-minor-project-1.git
   ```
2. Navigate to the project folder:
   ```bash
   cd hh8-minor-project-1
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Execute the script and uncover the truth:
   ```bash
   python main.py
   ```  

> Sample Header file: `sample_header.txt` 💡  

---

## 🤓 Tips & Tricks  
- 🧐 **Suspicious IPs?** IP showing up in an unexpected country? Double-check the authenticity of the sender via SPF/DKIM checks!  
- 🔍 **Investigations Made Easy:** Results marked as "pass" are trustworthy. "Fail" suggests caution.  
- 📤 **Unknown Sender?:** Dive into domain and ISP details via GeoIP analysis.  

> Fun Tip: Share findings with your friends and let them marvel at your detective skills. 🤩  

---

## 🌟 Real-Life Use Cases  
### 🏆 Practical Scenarios Where This Tool Shines:
- **Cybersecurity Enthusiasts**:  
  Trace phishing attempts, identify spoofed emails, and improve your email security awareness. 🌐  
- **IT Professionals**:  
  Fight spam emails in your company's inbox and ensure mail authenticity while delivering secure communications. 💼  
- **Journalists & Advocates**:  
  Validate sources and origins for critical whistleblower emails sent anonymously. 📰  
- **Everyday Users**:  
  Get peace of mind by verifying unknown senders in your inbox. 📩  

---

## 🔮 Future Improvements & Roadmap  
Explore the exciting plans for evolving the tool:  
- Add **multi-output support** (e.g., export results in `.txt`, `.json`, or `.csv` formats).  
- **Advanced SPF/DKIM Validation**: Dive deeper into SPF aligned domains, DMARC usage, and email replay protection.  
- **AI-Powered IP Analysis**: Integrate machine-learning models to detect suspicious IP addresses faster.  
- **Enhanced Visualizations**: Create graphs and charts for GeoIP data (like country heat maps).  
- **Localization Support**: Expand IP location lookups to include multiple languages and regional APIs.  

---

## 🎉 Conclusion  
The **Email Header Analyzer** is your trusty gadget for all things mail-forensics. Whether you're a curious user or a cybersecurity enthusiast, this tool empowers you to uncover mysteries hiding in email headers like a seasoned pro. 🚀  

So grab your magnifying glass 🧐, fire up the analyzer, and let those email secrets spill the beans!  

Happy analyzing! 🌟
