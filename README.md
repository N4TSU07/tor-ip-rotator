🕵️‍♂️ Why Use This?
The internet tracks you — your IP address reveals your location, your device, and even your identity over time.

With this script:

🌍 You become anonymous by routing traffic through the Tor network.

🔁 Your IP rotates every few seconds — like a digital invisibility cloak.

🧠 You gain insight into how privacy tools like Tor, SOCKS proxies, and geolocation really work.

🛡️ Use it as a foundation for anonymous scraping, testing, or private browsing automation.

✨ Features
🔄 Rotates your public IP address automatically via Tor

🌐 Shows your IP and the full name of its country of origin

🕓 Changes identity every 3 seconds

⚙️ Fully customizable — adjust interval, proxy config, or exit nodes

💻 Works on macOS, Kali Linux, and Windows

🔧 Prerequisites
Python 3.7+

Tor installed and running

torrc configured to allow control (port 9051)

Required libraries:

requests

stem

pycountry

🛠 Installation & Setup Guide
1️⃣ Clone or Download the Script
You can download the .zip or clone using Git:

bash
Copy
Edit
git clone https://github.com/your-username/tor-ip-rotator.git
cd tor-ip-rotator
2️⃣ Install Required Python Libraries
bash
Copy
Edit
pip install requests stem pycountry
3️⃣ Install & Start Tor
macOS (Homebrew)
bash
Copy
Edit
brew install tor
brew services start tor
Kali Linux / Debian
bash
Copy
Edit
sudo apt update
sudo apt install tor
sudo systemctl start tor
sudo systemctl enable tor
Windows
Download the Tor Expert Bundle:
🔗 https://www.torproject.org/download/tor/

Extract the folder and run tor.exe

4️⃣ Configure the torrc File
🗂️ Location:

macOS/Linux: /usr/local/etc/tor/torrc or /etc/tor/torrc

Windows: in same folder as tor.exe

📝 Add this:

yaml
Copy
Edit
ControlPort 9051
CookieAuthentication 1
Or (if using password auth):

php-template
Copy
Edit
ControlPort 9051
HashedControlPassword <your-password-hash>
🔐 Generate password hash:

bash
Copy
Edit
tor --hash-password your_secure_password
5️⃣ Restart Tor After Configuration
bash
Copy
Edit
# macOS
brew services restart tor

# Linux
sudo systemctl restart tor
Windows: Close and reopen tor.exe

🚀 Run the Script
bash
Copy
Edit
python tor_ip_rotator.py


Example Output

[1] Current IP: 185.220.101.47 | Country: Germany
[2] Current IP: 199.249.230.72 | Country: United States
[3] Current IP: 185.100.87.202 | Country: Netherlands
