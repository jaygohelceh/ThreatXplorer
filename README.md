<h1 align="center">🚀 ThreatXplorer</h1>

<p align="center">
  Explore, analyze, and detect malicious IOCs using real-time threat intelligence
</p>

---

## 📌 Overview

**ThreatXplorer** is a Python-based threat intelligence tool designed for SOC analysts, security engineers, and cybersecurity enthusiasts. It enables real-time analysis of Indicators of Compromise (IOCs) such as IP addresses, domains, and file hashes by integrating with multiple threat intelligence sources like VirusTotal and AbuseIPDB.

The tool aggregates and correlates threat data to provide a clear verdict on whether an IOC is malicious or benign, helping streamline threat detection and investigation workflows.

---

## ⚙️ Features

- 🔍 IOC Lookup (IP, Domain, Hash)
- 🌐 VirusTotal Integration
- 🚨 AbuseIPDB Integration (for IP analysis)
- 🎯 Malicious / Clean Verdict Detection
- 🎨 Colored CLI Output
- ⚡ Fast and Lightweight
- 🧠 SOC-style Threat Analysis

---

## 🧱 Project Structure

```text
ThreatXplorer/
│
├── main.py
├── config.py
├── requirements.txt
├── README.md
│
├── utils/
│ ├── vt_lookup.py
│ ├── abuseipdb.py
│ └── formatter.py
│
├── reports/
```

---

## 🛠️ Installation

Follow the steps below to set up **ThreatXplorer**:

```bash
### Clone the Repository
git clone https://github.com/jaygohelceh/ThreatXplorer.git
cd ThreatXplorer

### Create Virtual Environment
python3 -m venv venv

### Activate Virtual Environment

## Linux / macOS
source venv/bin/activate

## Windows
venv\Scripts\activate

### Install Dependencies
pip install -r requirements.txt
```
---
## 🔑 Configuration

Edit config.py file:
```text
VT_API_KEY = "your_virustotal_api_key"
ABUSEIPDB_API_KEY = "your_abuseipdb_api_key"
```
---


## ▶️ Usage

💡 Run commands from project directory


#### 🔹 Check IP Address
```bash
python main.py --type ip --value 8.8.8.8
```

#### 🔹 Check Domain
```bash
python main.py --type domain --value example.com
```

#### 🔹 Check File Hash
```bash
python main.py --type hash --value 44d88612fea8a8f36de82e1278abb02f
```
---

## 📊 Sample Output
```text

[+] Checking: 8.8.8.8

VirusTotal:
  Malicious: 2
  Suspicious: 1

AbuseIPDB:
  Abuse Score: 85
  Reports: 120

[!] Verdict: MALICIOUS
```
---

## 👨‍💻 Author

Jay Gohel
Cyber Security Engineer | SOC Engineer | Threat Hunter

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!

---
