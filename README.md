# Tor IP Rotator 🧅🌍

**Tor IP Rotator** is a Python script that rotates your IP address through the Tor network at regular intervals. Each time the IP is rotated, the script fetches the new IP address and displays the country of origin using the IP information from `ipinfo.io`. This tool is useful for maintaining anonymity, testing privacy, or simulating different geographical locations when browsing or scraping online.

---

## 🛠 Features

- Automatically rotates IP through Tor every 3 seconds
- Uses `httpbin.org` to fetch current IP
- Uses `ipinfo.io` and `pycountry` to get full country name
- Gracefully handles errors and keeps running unless stopped

---

## ⚙️ Requirements

- Python 3.x
- Tor installed and running
- Tor ControlPort (default: 9051) with authentication enabled
- SOCKS proxy at 127.0.0.1:9050
- Python packages: `requests`, `stem`, `pycountry`

---

## 💻 Installation & Usage

### 📦 1. Install Python Dependencies

```bash
pip install requests stem pycountry
