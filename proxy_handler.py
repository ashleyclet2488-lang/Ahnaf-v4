# proxy_handler.py

import random
import requests
from colorama import Fore

class ProxyRotator:
    def __init__(self):
        self.proxies = []
        self.working_proxies = []
        self.current_index = 0

    def fetch_free_proxies(self):
        """ফ্রি প্রক্সি থেকে প্রক্সি সংগ্রহ করে"""
        proxy_sources = [
            "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=5000&country=all",
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
            "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
        ]
        for url in proxy_sources:
            try:
                r = requests.get(url, timeout=10)
                if r.status_code == 200:
                    lines = r.text.strip().split("\n")
                    for line in lines:
                        if ":" in line:
                            self.proxies.append(line.strip())
            except:
                pass
        print(Fore.CYAN + f"[*] সংগৃহীত প্রক্সি: {len(self.proxies)} টি")

    def validate_proxies(self, max_check=50):
        """প্রক্সি ভ্যালিডেট করে"""
        test_url = "https://www.instagram.com"
        test_proxies = random.sample(self.proxies, min(max_check, len(self.proxies)))
        for proxy in test_proxies:
            proxy_dict = {
                "http": f"http://{proxy}",
                "https": f"http://{proxy}"
            }
            try:
                r = requests.get(test_url, proxies=proxy_dict, timeout=5)
                if r.status_code == 200:
                    self.working_proxies.append(proxy)
            except:
                pass
        print(Fore.GREEN + f"[+] কার্যকর প্রক্সি: {len(self.working_proxies)} টি")

    def get_proxy(self):
        """র‍্যান্ডম কার্যকর প্রক্সি রিটার্ন করে"""
        if not self.working_proxies:
            return None
        proxy = random.choice(self.working_proxies)
        return {
            "http": f"http://{proxy}",
            "https": f"http://{proxy}"
        }

    def setup(self):
        self.fetch_free_proxies()
        self.validate_proxies()
        return len(self.working_proxies) > 0
