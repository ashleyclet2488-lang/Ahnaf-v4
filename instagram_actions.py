# instagram_actions.py

import requests
import random
import time
from fake_useragent import UserAgent
from colorama import Fore
from concurrent.futures import ThreadPoolExecutor

ua = UserAgent()

class InstagramActions:
    def __init__(self, proxy_rotator):
        self.session = requests.Session()
        self.proxy_rotator = proxy_rotator
        self.base_url = "https://i.instagram.com/api/v1"

    def _headers(self, session_id=None):
        headers = {
            "User-Agent": ua.random,
            "X-IG-App-ID": "936619743392459",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        if session_id:
            headers["Cookie"] = f"sessionid={session_id}"
        return headers

    def mass_like(self, media_id, count, session_id):
        """ম্যাস লাইক"""
        def _like(i):
            proxy = self.proxy_rotator.get_proxy()
            try:
                r = self.session.post(
                    f"{self.base_url}/media/{media_id}/like/",
                    headers=self._headers(session_id),
                    proxies=proxy,
                    timeout=10
                )
                if r.status_code == 200:
                    print(Fore.GREEN + f"  [+] Like #{i+1} সফল")
                else:
                    print(Fore.RED + f"  [-] Like #{i+1} ব্যর্থ")
            except:
                print(Fore.RED + f"  [-] Like #{i+1} এরর")
        with ThreadPoolExecutor(max_workers=20) as executor:
            executor.map(_like, range(count))

    def mass_comment(self, media_id, count, comments_list, session_id):
        """ম্যাস কমেন্ট"""
        def _comment(i):
            proxy = self.proxy_rotator.get_proxy()
            comment = random.choice(comments_list)
            try:
                r = self.session.post(
                    f"{self.base_url}/media/{media_id}/comment/",
                    data={"comment_text": comment},
                    headers=self._headers(session_id),
                    proxies=proxy,
                    timeout=10
                )
                if r.status_code == 200:
                    print(Fore.GREEN + f"  [+] Comment #{i+1}: {comment[:30]}")
                else:
                    print(Fore.RED + f"  [-] Comment #{i+1} ব্যর্থ")
            except:
                pass
        with ThreadPoolExecutor(max_workers=15) as executor:
            executor.map(_comment, range(count))

    def mass_follow(self, user_id, count, session_id):
        """ম্যাস ফলো"""
        def _follow(i):
            proxy = self.proxy_rotator.get_proxy()
            try:
                r = self.session.post(
                    f"{self.base_url}/friendships/create/{user_id}/",
                    headers=self._headers(session_id),
                    proxies=proxy,
                    timeout=10
                )
                if r.status_code == 200:
                    print(Fore.GREEN + f"  [+] Follow #{i+1} সফল")
                else:
                    print(Fore.RED + f"  [-] Follow #{i+1} ব্যর্থ")
            except:
                pass
        with ThreadPoolExecutor(max_workers=20) as executor:
            executor.map(_follow, range(count))

    def mass_save(self, media_id, count, session_id):
        """ম্যাস সেভ"""
        def _save(i):
            proxy = self.proxy_rotator.get_proxy()
            try:
                r = self.session.post(
                    f"{self.base_url}/media/{media_id}/save/",
                    headers=self._headers(session_id),
                    proxies=proxy,
                    timeout=10
                )
                if r.status_code == 200:
                    print(Fore.GREEN + f"  [+] Save #{i+1} সফল")
            except:
                pass
        with ThreadPoolExecutor(max_workers=15) as executor:
            executor.map(_save, range(count))

    def mass_share(self, media_id, count, session_id):
        """ম্যাস শেয়ার (DM-এ)"""
        def _share(i):
            proxy = self.proxy_rotator.get_proxy()
            try:
                r = self.session.post(
                    f"{self.base_url}/direct_v2/threads/broadcast/media_share/",
                    data={"media_id": media_id, "media_type": "photo"},
                    headers=self._headers(session_id),
                    proxies=proxy,
                    timeout=10
                )
                if r.status_code == 200:
                    print(Fore.GREEN + f"  [+] Share #{i+1} সফল")
            except:
                pass
        with ThreadPoolExecutor(max_workers=15) as executor:
            executor.map(_share, range(count))

    def mass_report(self, target_username, reason, count, sessions):
        """ম্যাস রিপোর্ট — একাধিক অ্যাকাউন্ট থেকে"""
        def _report(session_id):
            proxy = self.proxy_rotator.get_proxy()
            try:
                # প্রথমে ইউজার আইডি সংগ্রহ
                r1 = self.session.get(
                    f"https://www.instagram.com/{target_username}/?__a=1&__d=dis",
                    headers=self._headers(session_id),
                    proxies=proxy,
                    timeout=10
                )
                if r1.status_code == 200:
                    user_id = r1.json().get("graphql", {}).get("user", {}).get("id")
                    if user_id:
                        # এরপর রিপোর্ট
                        r2 = self.session.post(
                            f"{self.base_url}/users/{user_id}/flag/",
                            data={"reason_id": str(reason), "source": "profile"},
                            headers=self._headers(session_id),
                            proxies=proxy,
                            timeout=10
                        )
                        return r2.status_code == 200
            except:
                return False
            return False

        with ThreadPoolExecutor(max_workers=10) as executor:
            results = list(executor.map(_report, sessions))
        success = sum(results)
        print(Fore.GREEN + f"\n[✓] মোট রিপোর্ট পাঠানো হয়েছে: {success}/{count}")
        return success

    def join_broadcast(self, broadcast_id, count, sessions):
        """ব্রডকাস্ট চ্যানেলে জয়েন"""
        def _join(session_id):
            proxy = self.proxy_rotator.get_proxy()
            try:
                r = self.session.post(
                    f"{self.base_url}/live/{broadcast_id}/join_and_view/",
                    headers=self._headers(session_id),
                    proxies=proxy,
                    timeout=10
                )
                return r.status_code == 200
            except:
                return False
        with ThreadPoolExecutor(max_workers=20) as executor:
            results = list(executor.map(_join, sessions))
        success = sum(results)
        print(Fore.GREEN + f"\n[✓] ব্রডকাস্টে জয়েন করেছে: {success}/{count}")
        return success
