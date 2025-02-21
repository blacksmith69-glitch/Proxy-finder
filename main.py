import requests
import threading
import time

# Proxy sources (add more if needed)
PROXY_SOURCES = [
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
    "https://www.proxy-list.download/api/v1/get?type=http",
    "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=5000",
    "https://www.proxyscan.io/api/proxy?type=http",
]

# Test URL (should be fast & responsive)
TEST_URL = "https://www.google.com"

# Save file
OUTPUT_FILE = "working_proxies.txt"


def fetch_proxies():
    """Fetch proxies from multiple sources"""
    proxies = set()
    print("[+] Fetching fresh proxies...")

    for url in PROXY_SOURCES:
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                new_proxies = response.text.strip().split("\n")
                proxies.update(new_proxies)
                print(f"[✔] Fetched {len(new_proxies)} proxies from: {url}")
            else:
                print(f"[✖] Failed to fetch from {url}")
        except Exception as e:
            print(f"[✖] Error fetching from {url}: {e}")

    print(f"[✔] Total proxies fetched: {len(proxies)}")
    return list(proxies)


def test_proxy(proxy):
    """Check if the proxy is working"""
    try:
        formatted_proxy = f"http://{proxy}"
        proxies = {"http": formatted_proxy, "https": formatted_proxy}
        start = time.time()
        response = requests.get(TEST_URL, proxies=proxies, timeout=5)
        latency = time.time() - start

        if response.status_code == 200:
            print(f"[✔] Working ({latency:.2f}s): {proxy}")
            return proxy
    except:
        pass
    return None


def filter_proxies(proxies):
    """Multithreaded proxy testing"""
    working_proxies = []
    threads = []

    def worker(proxy):
        result = test_proxy(proxy)
        if result:
            working_proxies.append(result)

    for proxy in proxies:
        thread = threading.Thread(target=worker, args=(proxy,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return working_proxies


def save_proxies(proxies):
    """Save working proxies in the required format"""
    with open(OUTPUT_FILE, "w") as file:
        for proxy in proxies:
            file.write(f"http://username:password@{proxy}\n")  # Replace with actual credentials if needed
    print(f"[✔] Saved {len(proxies)} working proxies in {OUTPUT_FILE}")


def main():
    while True:
        proxies = fetch_proxies()
        working_proxies = filter_proxies(proxies)
        save_proxies(working_proxies)

        print("[⏳] Waiting for 3 hours before next update...\n")
        time.sleep(3 * 60 * 60)  # 3 hours delay


if __name__ == "__main__":
    main()
