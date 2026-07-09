# temp_mail.py

import requests
import random
import string
import time
from colorama import Fore

class TempMail:
    def __init__(self):
        self.base_url = "https://api.mail.tm"
        self.session = requests.Session()
        self.email = None
        self.password = None
        self.token = None
        self.account_id = None

    def generate_credentials(self):
        """র‍্যান্ডম ইউজারনেম ও পাসওয়ার্ড তৈরি করে"""
        username = "ahnaf" + ''.join(random.choices(string.digits, k=10))
        self.password = ''.join(random.choices(string.ascii_letters + string.digits, k=14))
        return username, self.password

    def get_domain(self):
        """মেইল ডোমেইন সংগ্রহ"""
        try:
            r = self.session.get(f"{self.base_url}/domains")
            if r.status_code == 200:
                domains = r.json()["hydra:member"]
                return domains[0]["domain"]
        except:
            pass
        return "mail.tm"

    def create_account(self):
        """টেম্প মেইল অ্যাকাউন্ট তৈরি করে"""
        username, password = self.generate_credentials()
        domain = self.get_domain()
        self.email = f"{username}@{domain}"

        try:
            r = self.session.post(f"{self.base_url}/accounts", json={
                "address": self.email,
                "password": password
            })
            if r.status_code == 201:
                self.account_id = r.json()["id"]
                self._get_token()
                return True
        except:
            pass
        return False

    def _get_token(self):
        """JWT টোকেন সংগ্রহ"""
        try:
            r = self.session.post(f"{self.base_url}/token", json={
                "address": self.email,
                "password": self.password
            })
            if r.status_code == 200:
                self.token = r.json()["token"]
                self.session.headers.update({"Authorization": f"Bearer {self.token}"})
        except:
            pass

    def get_emails(self, retries=5):
        """ইনবক্স থেকে ভেরিফিকেশন কোড/লিংক সংগ্রহ"""
        for _ in range(retries):
            try:
                time.sleep(3)
                r = self.session.get(f"{self.base_url}/accounts/{self.account_id}/messages")
                if r.status_code == 200 and r.json().get("hydra:member"):
                    return r.json()["hydra:member"][0]
            except:
                time.sleep(2)
        return None

    def extract_code(self, email_data):
        """ইমেইল থেকে কোড বের করে"""
        import re
        text = email_data.get("text", "") + email_data.get("html", "")
        match = re.search(r'\b\d{6}\b', text)
        if match:
            return match.group(0)
        return None
