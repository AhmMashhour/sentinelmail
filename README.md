# 📧 SentinelMail

**SentinelMail** is an open-source email threat detection and analysis tool designed for cybersecurity professionals, researchers, and organizations of all sizes.

It detects, classifies, and scores malicious, phishing, spoofing, or suspicious emails using AI models locally — with full offline support and no dependency on commercial APIs.

---

## 🚀 Features

- 🔍 Analyze `.eml` email files from local folders or inbox
- 🧠 Detect phishing, spoofing, malware, and social engineering
- 🔐 Local scanning of links and attachments (no cloud dependency)
- 📊 HTML reports with threat scores and breakdowns
- 🔁 Learns from user feedback (optional self-training module)
- 🧰 Command-line interface and optional web dashboard
- 🐧 Installable on Kali Linux, Ubuntu, and Debian systems
- 📡 Integration-ready with SIEM tools (Splunk, Wazuh, ELK)

---

## 🛠️ Tech Stack

| Layer            | Technology              |
|------------------|--------------------------|
| Language         | Python 3                |
| Core Analysis    | scikit-learn, spaCy, nltk |
| CLI              | argparse, rich          |
| Dashboard (optional) | Flask, Jinja2        |
| Database         | SQLite                  |
| Reports          | Jinja2, PDFKit          |

---

## 📁 Project Structure

```bash
sentinelmail/
├── cli/           # Command-line interface
├── core/          # Parser, analyzer, and NLP modules
├── models/        # Trained ML models
├── data/          # Sample emails and datasets
├── reports/       # Output reports
├── dashboard/     # Web dashboard (optional)
├── integration/   # Gmail/IMAP fetchers, SIEM exporters
├── database/      # SQLite schema and models
├── docs/          # Documentation and roadmap
├── tests/         # Unit and integration tests
```

---

## ⚙️ Installation

> ⚠️ **Note:** Installation is currently under development. Scripts will be available after Phase 1.

For now, you can clone the repository:

```bash
git clone https://github.com/AhmMashhour/sentinelmail.git
cd sentinelmail
```

Setup instructions and automated install scripts are coming soon.

---

## 📦 Run the CLI

> ⚠️ CLI functionality is currently in development. Basic usage will be released in the next phase.

Expected usage example:

```bash
python cli/mailsentinel.py --file path/to/email.eml
```

---

## 📌 Roadmap

Development is organized into clean phases. You can follow our [docs/roadmap.md](docs/roadmap.md) for detailed progress and contributions.

---

## 📜 License

This project is licensed under the **MIT License**.  
Free to use, modify, and distribute with credit

---

## 🤝 Contributors

Lead: [@AhmMashhour](https://github.com/AhmMashhour)  

We welcome contributors and collaborators at all levels
