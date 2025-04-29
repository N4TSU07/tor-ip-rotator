import time
import requests
import pycountry
from stem import Signal
from stem.control import Controller

# Tor SOCKS proxy setup
proxies = {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050'
}

def renew_tor_ip():
    try:
        with Controller.from_port(port=9051) as controller:
            controller.authenticate()
            controller.signal(Signal.NEWNYM)
    except Exception as e:
        print(f"[!] Failed to renew Tor IP: {e}")

def get_ip():
    try:
        res = requests.get('http://httpbin.org/ip', proxies=proxies, 
timeout=10)
        return res.json()['origin']
    except Exception as e:
        return f"Error getting IP: {e}"

def get_country_name(ip):
    try:
        res = requests.get(f"https://ipinfo.io/{ip}/json", timeout=10)
        data = res.json()
        country_code = data.get("country", "")
        country = pycountry.countries.get(alpha_2=country_code)
        return country.name if country else "Unknown"
    except Exception as e:
        return f"Error getting country: {e}"

# Infinite loop until user quits
i = 1
print("[*] Starting Tor IP rotation loop. Press Ctrl+C to stop.")
while True:
    try:
        ip = get_ip()
        if "Error" in ip:
            print(f"[{i}] IP Error: {ip}")
        else:
            country = get_country_name(ip)
            print(f"[{i}] Current IP: {ip} | Country: {country}")
        renew_tor_ip()
        time.sleep(3)
        i += 1
    except KeyboardInterrupt:
        print("\n[!] Stopped by user.")
        break
    except Exception as e:
        print(f"[!] Unexpected error: {e}")
        time.sleep(5)

