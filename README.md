🧅 Tor IP Rotator — Become Invisible Online
Want to hide your real IP and browse like a ghost?
This script auto-rotates your IP using the Tor network, giving you total privacy and country-level anonymity — every 3 seconds.

Perfect for:

🕵️ Ethical hackers

🧠 OSINT analysts

🧼 Privacy advocates

🧪 Web testers & scrapers

🌍 What It Does
✅ Changes your IP address every few seconds
✅ Shows the new IP and its country of origin
✅ Uses the Tor network to anonymize your traffic
✅ Keeps running until you stop it manually
✅ Works on macOS, Kali Linux, and Windows

🛠 Installation Guide
1. Install Tor
macOS (via Homebrew)

brew install tor
brew services start tor
Kali Linux / Debian

sudo apt update
sudo apt install tor
sudo systemctl start tor
sudo systemctl enable tor
Windows
Download the Tor Expert Bundle:
https://www.torproject.org/download/tor/

Extract and run tor.exe

2. Configure torrc File
Location:

macOS/Linux: /usr/local/etc/tor/torrc or /etc/tor/torrc

Windows: Inside your extracted Tor folder

Add these lines:

ControlPort 9051
CookieAuthentication 1
Or for password auth:

ControlPort 9051
HashedControlPassword <your-password-hash>
To create a hash:

tor --hash-password your_secure_password
Then restart Tor:

# macOS
brew services restart tor

# Linux
sudo systemctl restart tor
3. Install Required Python Packages

pip install -r requirements.txt
Contents of requirements.txt:

nginx
Copy
Edit
requests
stem
pycountry

# Tor must be installed manually (see instructions above)

4. Run the Script
   
python3 tor_ip_rotator.py

Sample output:

[1] Current IP: 185.220.101.47 | Country: Germany

[2] Current IP: 199.249.230.72 | Country: United States

🌐 Bonus: Route Firefox Through Tor
Want to make Firefox anonymous too? Follow these steps:

Open Firefox.

Go to about:preferences.

Scroll to Network Settings → Click Settings....

Choose Manual proxy configuration and enter:


SOCKS Host: 127.0.0.1
Port: 9050
✅ Check: "Proxy DNS when using SOCKS v5"

Now, all your Firefox traffic is routed through Tor — just like your Python script!

🧪 Use Cases
Anonymous browsing

IP rotation for scraping

OSINT investigations

Tor network testing

Geo-based content access

🛑 Stop the Script
To stop it, press:

Ctrl + C

🔐 Stay Private, Stay Safe

Tor IP Rotator doesn’t just rotate IPs — it empowers you with anonymity. Whether you're evading trackers, researching in secret, or testing applications globally — this tool makes your digital life borderless.

