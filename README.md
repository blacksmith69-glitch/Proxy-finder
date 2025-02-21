# Proxy-finder
Free working proxies every 3 hours 

Here is a ready-to-paste README.md file with all commands and explanations in a clean format. It uses code blocks (```) to make copying easier.


---

README.md (Copy-Paste This in GitHub)

# 🔥 Proxy Scraper & Checker for Termux  

This script **fetches fresh proxies**, checks which ones are **working**, and saves them in a file.  

---

## **📌 Installation & Setup (Termux)**  

### **1️⃣ Install Termux & Required Packages**

pkg update -y && pkg upgrade -y pkg install python -y pkg install git -y pkg install nano -y pip install requests

---

### **2️⃣ Clone the Repository & Navigate to Folder**

git clone <your-repo-link> cd <your-repo-name>

---

### **3️⃣ Run the Proxy Scraper (Fetch Fresh Proxies)**

python main.py

✅ This will **fetch fresh proxies** and save them in `proxies.txt`.  

---

### **4️⃣ Run the Proxy Checker (Check Working Proxies)**

python check.py

✅ This will **test proxies** and save only working ones in `working_proxies.txt`.  

---

### **📌 Where to Find Proxies?**

proxies.txt           →  All fetched proxies
working_proxies.txt   →  Only working proxies

🔁 **If no proxies work, rerun the script later.**  

🚀 **Enjoy Proxy Scraping & Checking in Termux!**


---

Now you can directly paste this into GitHub, and users can easily copy commands for setup and usage.

