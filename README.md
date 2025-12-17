# Cybersecurity Portfolio: SOC Analyst & Defensive Operations
I am an aspiring SOC Analyst and Cybersecurity student (B.S. Cyber Security, Kennesaw State University) dedicated to mastering defensive operations. This repository serves as a technical portfolio of hands-on investigations, log analysis, and incident response simulations.

## 🏆 Training Progress & Certifications
* **CompTIA Security+:** In Progress (Target Exam: February 2026)
* **TryHackMe Learning Paths:**
  * ✅ SOC Level 1 (Completed Dec 2025)
  * ✅ Pre-Security (Completed Nov 2025)
  * ✅ Cybersecurity 101 (Completed Nov 2025)
---

## 🔬 Featured Technical Labs
Each lab below includes a detailed PDF investigation report documenting my methodology, findings, and escalation summaries.

### 1. Host-Based Incident Investigation (Benign)
**Scenario:** Investigated a suspected host compromise within an HR department using Splunk.
* **Tools Used:** Splunk SIEM, Windows Event Logs.
* **Key Actions:** Queried `win_eventlogs` to identify unauthorized scheduled tasks and malicious process execution (Event ID 4688).
* **Outcome:** Successfully identified the imposter user account and the malicious payload URL.
* 📄 **[View Full Investigation Report](./Benign-THM.pdf)**

### 2. Network Telemetry & C2 Detection (ItsyBitsy)
**Scenario:** Analyzed a week's worth of HTTP connection logs in Kibana to identify potential command-and-control (C2) traffic.
* **Tools Used:** Elastic Stack (Kibana), VirusTotal.
* **Key Actions:** Performed log pivoting (IP → domain → tool → URL) to detect malicious use of `bitsadmin` for file downloads.
* **Outcome:** Confirmed outbound connections to Pastebin used to retrieve malicious THM-formatted secret codes.
* 📄 **[View Full Investigation Report](./ItsyBitsy-THM.pdf)**

### 3. AsyncRAT Indicators & Escalation (Invite Only)
**Scenario:** Acted as an L1 SOC Analyst to validate threats and prepare intelligence for Tier 2 escalation.
* **Tools Used:** VirusTotal, OSINT, Threat Intelligence feeds.
* **Key Actions:** Investigated SHA256 hashes and hijacked Discord links; mapped malicious behavior to the AsyncRAT malware family.
* **Outcome:** Built a comprehensive attack timeline including multi-stage delivery and ChromeKatz credential theft attempts.
* 📄 **[View Full Investigation Report](./Invite_Only_Challenge-THM.pdf)**

### 4. Phishing & Memory Forensics (Boogeyman 2)
**Scenario:** Analyzed a volatile memory dump to reconstruct a multi-stage spear-phishing attack.
* **Tools Used:** Volatility 3, LibreOffice Basic, Linux CLI.
* **Key Actions:** De-obfuscated VBA macros to reveal Stage 2 payloads; performed process correlation to identify malicious C2 callbacks.
* **Outcome:** Identified the complete attack chain from the initial email sender to the persistent PowerShell-based C2 agent.
* 📄 **[View Full Investigation Report](./Boogeyman_2.pdf)**

## 🛠️ Technical Skills & Tools
 **SIEM & Monitoring:** Splunk (SPL), Elastic Stack (Kibana), Sysmon, Windows Event Logs.
* **Networking:** OSI Model, TCP/IP Suite, DNS, HTTP/S, Packet Analysis (Wireshark).
* **Defensive Tools:** VirusTotal, CyberChef, Zeek, Brim, Timeline Explorer.
* **Frameworks:** MITRE ATT&CK (Adversary Mapping), NIST Cybersecurity Framework (CSF), Pyramid of Pain.
* **OS Admin:** Linux CLI navigation, Windows PowerShell basics.

---

## 🚀 Continuous Growth
* **Currently Learning:** Advanced Malware Analysis and Effective Triaging.
* **Goals:** Achieve CompTIA Security+ certification and transition into a Tier 1 SOC Analyst role.

---
**Contact:** [chrisbutler7552@gmail.com](mailto:chrisbutler7552@gmail.com) | [www.linkedin.com/in/chris-butler-7b75a9322]
