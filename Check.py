import requests
import threading

PROXY_FILE = "proxies.txt"  # File containing proxies (one per line)
OUTPUT_FILE = "working_proxies.txt"
TEST_URL = "https://www.google.com"  # Fast, reliable test site

def test_proxy(proxy):
    """Check if a proxy is working"""
    try:
        formatted_proxy = f"http://{proxy}"
        proxies = {"http": formatted_proxy, "https": formatted_proxy}
        response = requests.get(TEST_URL, proxies=proxies, timeout=5)
        if response.status_code == 200:
            print(f"[✔] Working: {proxy}")
            return proxy
    except:
        pass
    return None

def check_proxies():
    """Read proxies from file and check them"""
    with open(PROXY_FILE, "r") as file:
        proxies = [line.strip() for line in file.readlines()]

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

    with open(OUTPUT_FILE, "w") as file:
        for proxy in working_proxies:
            file.write(proxy + "\n")

    print(f"[✔] Saved {len(working_proxies)} working proxies in {OUTPUT_FILE}")

if __name__ == "__main__":
    check_proxies()
