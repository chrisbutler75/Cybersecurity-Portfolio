# Cybersecurity Portfolio: Cloud Security & Defensive Operations
I am a B.S. Cybersecurity student at Western Governors University (WGU) and a high-performance professional. My work focuses on architecting secure cloud environments, automating security governance with Python, and performing deep-dive forensic investigations.

## 🏆 Certifications & Education
* **B.S. Cybersecurity & Information Assurance:** Western Governors University (In Progress)
* **Google Cybersecurity Professional Certificate:** (Completed Jan 2026)
* **CompTIA Security+:** (In Progress - Target Feb 2026)
* **SOC Level 1 Professional Path:** TryHackMe (Completed Dec 2025)

---

## ☁️ Featured Cloud & Automation Projects
### 1. Secure the Cloud – Phase 1: Identity Governance (AWS)
**Objective:** Transitioned a high-risk environment from "Root" access to a production-ready **Least Privilege** model using **Role-Based Access Control (RBAC)**.
* **Tools Used:** AWS IAM, MFA, AWS Management Console, LocalStack.
* **Key Actions:** Engineered a three-tier group hierarchy (Admins, Auditors, Developers) and validated security boundaries through "Access Denied" auditing.
* **Outcome:** Eliminated Root account risks and established a scalable governance framework aligned with **NIST CSF (PR.AC)**.
* 📄 **[View Phase 1 Investigation Report](./IAM.pdf)**

### 2. Security Automation with Python
**Objective:** Developed custom scripts to automate security auditing and data management.
* **Tools Used:** Python (Boto3 SDK), Object-Oriented Programming (OOP).
* **Key Actions:** Built an automated student grade analysis tool and an office worker data encapsulation class to handle complex organizational records.
* **Outcome:** Demonstrated the ability to use **Infrastructure as Code (IaC)** principles to reduce manual administrative overhead.
* 💻 **[View Automation Scripts](./lab12.py)**

---

## 🔬 Forensic & SOC Investigations
### 3. Phishing & Memory Forensics (Boogeyman 2)
**Scenario:** Reconstructed a multi-stage spear-phishing attack using volatile memory analysis.
* **Tools Used:** Volatility 3, LibreOffice Basic, Linux CLI.
* [cite_start]**Key Actions:** De-obfuscated VBA macros and used `pstree` analysis to identify the malicious `wscript.exe` process (PID: 4260) and its C2 persistence[cite: 3047, 3054].
* **Outcome:** Identified the complete attack chain from initial email to a persistent PowerShell-based C2 agent.
* 📄 **[View Full Investigation Report](./Boogeyman_2.pdf)**

### 4. Network Telemetry & C2 Detection (ItsyBitsy)
**Scenario:** Analyzed 1,400+ HTTP connection logs in Kibana to detect command-and-control (C2) traffic.
* **Tools Used:** Elastic Stack (Kibana), VirusTotal.
* [cite_start]**Key Actions:** Performed log pivoting (IP → domain → tool → URL) to detect the unauthorized use of `bitsadmin` for background file downloads[cite: 3162, 3188].
* [cite_start]**Outcome:** Reconstructed a full attack path from an internal HR-segment IP to a Pastebin-hosted payload[cite: 3152, 3195].
* 📄 **[View Full Investigation Report](./ItsyBitsy-THM.pdf)**

---

## 🛠️ Technical Skills & Tools
* **Cloud & Infrastructure:** AWS IAM, VPC Architecture, MFA, Least Privilege Governance.
* **Automation:** Python (Security Scripting/Boto3), PowerShell basics.
* **SIEM & Monitoring:** Splunk, Elastic/Kibana, Sysmon, Windows Event Logs (ID 4688).
* **Defensive Ops:** Memory Forensics (Volatility 3), VirusTotal, Log Pivoting, NIST CSF.

---
**Contact:** [chrisbutler7552@gmail.com](mailto:chrisbutler7552@gmail.com) | [LinkedIn](https://www.linkedin.com/in/chris-butler-7b75a9322/)
