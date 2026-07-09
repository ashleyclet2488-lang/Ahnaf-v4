# account_creator.py

import requests
import random
import string
import time
from faker import Faker
from fake_useragent import UserAgent
from colorama import Fore

fake = Faker()
ua = UserAgent()

class InstagramAccountCreator:
    def __init__(self, proxy_rotator):
        self.session = requests.Session()
        self.proxy_rotator = proxy_rotator
        self.base_url = "https://i.instagram.com/api/v1"

    def generate_user_data(self):
        """র‍্যান্ডম ইউজার ডাটা তৈরি"""
        first = fake.first_name()
        last = fake.last_name()
        username = (first + last + ''.join(random.choices(string.digits, k=4))).lower()
        return {
            "username": username,
            "password": ''.join(random.choices(string.ascii_letters + string.digits + "!@#$", k=14)),
            "first_name": first,
            "email": None  # পরে সেট হবে
        }

    def signup(self, email, password, username, first_name):
        """ইনস্টাগ্রাম সাইনআপ"""
        proxy = self.proxy_rotator.get_proxy()
        headers = {
            "User-Agent": ua.random,
            "X-IG-App-ID": "936619743392459",
            "Content-Type": "application/x-www-form-urlencoded"
        }

        data = {
            "email": email,
            "password": password,
            "username": username,
            "first_name": first_name,
            "client_id": "936619743392459",
            "seamless_login_enabled": "1",
            "tos_version": "row",
            "force_sign_up_code": "0",
        }

        try:
            r = self.session.post(
                f"{self.base_url}/accounts/create/",
                data=data,
                headers=headers,
                proxies=proxy,
                timeout=15
            )
            if r.status_code == 200:
                return True, r.json()
            return False, r.text
        except Exception as e:
            return False, str(e)

    def verify_code(self, username, code):
        """ভেরিফিকেশন কোড পাঠায়"""
        proxy = self.proxy_rotator.get_proxy()
        headers = {
            "User-Agent": ua.random,
            "X-IG-App-ID": "936619743392459",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        try:
            r = self.session.post(
                f"{self.base_url}/accounts/account_confirm_code/",
                data={"code": code, "username": username, "device_id": "android-" + ''.join(random.choices(string.hexdigits, k=16))},
                headers=headers,
                proxies=proxy,
                timeout=15
            )
            return r.status_code == 200
        except:
            return False
