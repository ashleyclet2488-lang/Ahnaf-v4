# main.py

import os
import sys
import time
from colorama import Fore, init
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, IntPrompt, Confirm

from banner import show_banner
from proxy_handler import ProxyRotator
from temp_mail import TempMail
from account_creator import InstagramAccountCreator
from instagram_actions import InstagramActions

init(autoreset=True)
console = Console()

REPORT_REASONS = {
    "1": ("Spam", 1),
    "2": ("Nudity or sexual activity", 2),
    "3": ("Hate speech or symbols", 3),
    "4": ("Violence or dangerous organizations", 4),
    "5": ("Sale of illegal or regulated goods", 5),
    "6": ("Bullying or harassment", 6),
    "7": ("Intellectual property violation", 7),
    "8": ("Suicide or self-injury", 8),
    "9": ("Eating disorders", 9),
    "10": ("Impersonation", 10),
    "11": ("Misinformation", 11),
    "12": ("Drugs", 12),
}

COMMENTS = [
    "Nice post! 🔥", "Awesome content 👏", "Great work 💯", "Love this ❤️",
    "Beautiful 🌟", "Cool stuff 😎", "Amazing 🔥🔥", "Keep it up 💪",
    "Wow 🤩", "Perfect shot 📸", "Stunning ✨", "Incredible 🙌"
]

class AhnafV4:
    def __init__(self):
        self.proxy_rotator = ProxyRotator()
        self.temp_mail = TempMail()
        self.account_creator = None
        self.actions = None
        self.created_accounts = []
        self.target_username = None
        self.target_media_id = None
        self.target_user_id = None
        self.target_broadcast_id = None

    def setup(self):
        console.print(Fore.CYAN + "[*] প্রক্সি সেটআপ হচ্ছে...")
        if not self.proxy_rotator.setup():
            console.print(Fore.RED + "[!] কোনো কার্যকর প্রক্সি পাওয়া যায়নি!")
            return False
        self.account_creator = InstagramAccountCreator(self.proxy_rotator)
        self.actions = InstagramActions(self.proxy_rotator)
        console.print(Fore.GREEN + "[+] Ahnaf v4 সফলভাবে সেটআপ হয়েছে!\n")
        return True

    def menu(self):
        table = Table(title="⚡ AHNAF v4 — MAIN MENU ⚡", show_header=True, header_style="bold magenta")
        table.add_column("Option", style="cyan", width=8)
        table.add_column("Feature", style="green")
        table.add_column("Description", style="yellow")

        table.add_row("1", "Mass Like", "বুস্ট পোস্টে ম্যাস লাইক")
        table.add_row("2", "Mass Comment", "অটো কমেন্ট পাঠানো")
        table.add_row("3", "Mass Follow", "ফলোয়ার বাড়ানো")
        table.add_row("4", "Mass Share", "শেয়ার বুস্ট")
        table.add_row("5", "Mass Save", "সেভ বুস্ট")
        table.add_row("6", "Mass Report", "টেম্প মেইল দিয়ে রিপোর্ট")
        table.add_row("7", "Join Broadcast", "ব্রডকাস্টে অটো জয়েন")
        table.add_row("8", "Create Accounts", "নতুন টেম্প অ্যাকাউন্ট")
        table.add_row("0", "Exit", "বের হন")
        console.print(table)

    def create_accounts(self, count):
        console.print(Fore.CYAN + f"\n[*] {count} টি নতুন টেম্প অ্যাকাউন্ট তৈরি হচ্ছে...")
        accounts = []
        for i in range(count):
            console.print(Fore.YELLOW + f"\n[{i+1}/{count}] নতুন অ্যাকাউন্ট তৈরি হচ্ছে...")
            if self.temp_mail.create_account():
                console.print(Fore.GREEN + f"  [✓] ইমেইল: {self.temp_mail.email}")
                user_data = self.account_creator.generate_user_data()
                user_data["email"] = self.temp_mail.email
                success, resp = self.account_creator.signup(
                    user_data["email"],
                    user_data["password"],
                    user_data["username"],
                    user_data["first_name"]
                )
                if success:
                    console.print(Fore.GREEN + f"  [✓] ইউজারনেম: {user_data['username']}")
                    code = self.temp_mail.get_emails()
                    if code:
                        verification = self.temp_mail.extract_code(code)
                        if verification:
                            self.account_creator.verify_code(user_data["username"], verification)
                            accounts.append({
                                "email": self.temp_mail.email,
                                "username": user_data["username"],
                                "password": user_data["password"]
                            })
                            self.created_accounts.append(accounts[-1])
                else:
                    console.print(Fore.RED + f"  [-] সাইনআপ ব্যর্থ")
            time.sleep(2)
        console.print(Fore.GREEN + f"\n[✓] মোট তৈরি হয়েছে: {len(accounts)} টি অ্যাকাউন্ট")
        with open("accounts.txt", "a") as f:
            for acc in accounts:
                f.write(f"{acc['email']}:{acc['password']}:{acc['username']}\n")
        return accounts

    def get_target(self, action):
        console.print(Fore.CYAN + f"\n[*] টার্গেট সেট করুন ({action})")
        if action in ["like", "comment", "share", "save"]:
            self.target_media_id = Prompt.ask("[?] পোস্টের Media ID দিন")
        elif action == "follow":
            self.target_user_id = Prompt.ask("[?] টার্গেট User ID দিন")
        elif action == "report":
            self.target_username = Prompt.ask("[?] টার্গেট Username দিন")
        elif action == "broadcast":
            self.target_broadcast_id = Prompt.ask("[?] ব্রডকাস্ট ID দিন")

    def show_report_reasons(self):
        table = Table(title="📋 Report Reasons", show_header=True, header_style="bold red")
        table.add_column("Option", style="cyan", width=8)
        table.add_column("Reason", style="yellow")
        for k, v in REPORT_REASONS.items():
            table.add_row(k, v[0])
        console.print(table)

    def run(self):
        os.system("clear")
        show_banner()
        if not self.setup():
            return

        while True:
            self.menu()
            choice = Prompt.ask("\n[?] আপনার পছন্দ", choices=["1","2","3","4","5","6","7","8","0"])

            if choice == "0":
                console.print(Fore.YELLOW + "\n[!] Ahnaf v4 থেকে বের হচ্ছেন... ধন্যবাদ!")
                sys.exit(0)

            elif choice == "8":
                count = IntPrompt.ask("[?] কতটি অ্যাকাউন্ট তৈরি করবেন?", default=5)
                self.create_accounts(count)

            elif choice == "6":  # Report
                self.get_target("report")
                if not self.target_username:
                    continue
                self.show_report_reasons()
                reason_choice = Prompt.ask("[?] রিপোর্ট কারণ নির্বাচন করুন", choices=list(REPORT_REASONS.keys()))
                report_count = IntPrompt.ask("[?] কতটি রিপোর্ট পাঠাবেন?", default=10)

                # অ্যাকাউন্ট না থাকলে তৈরি করুক
                if not self.created_accounts:
                    console.print(Fore.YELLOW + "[!] আগে অ্যাকাউন্ট তৈরি প্রয়োজন")
                    count = IntPrompt.ask("[?] কতটি অ্যাকাউন্ট তৈরি করবেন?", default=report_count)
                    self.create_accounts(count)

                _, reason_id = REPORT_REASONS[reason_choice]
                sessions = [acc["password"] for acc in self.created_accounts[:report_count]]  # simplified
                self.actions.mass_report(self.target_username, reason_id, report_count, sessions)

            elif choice == "7":  # Broadcast Join
                self.get_target("broadcast")
                join_count = IntPrompt.ask("[?] কতটি অ্যাকাউন্ট জয়েন করবে?", default=10)
                if not self.created_accounts:
                    self.create_accounts(join_count)
                sessions = [acc["password"] for acc in self.created_accounts[:join_count]]
                self.actions.join_broadcast(self.target_broadcast_id, join_count, sessions)

            elif choice in ["1","2","3","4","5"]:
                action_map = {"1": "like", "2": "comment", "3": "follow", "4": "share", "5": "save"}
                action = action_map[choice]
                self.get_target(action)
                count = IntPrompt.ask(f"[?] কতবার {action} করবেন?", default=10)
                # একই সেশন দিয়ে (অথবা তৈরি অ্যাকাউন্ট দিয়ে)
                if not self.created_accounts:
                    self.create_accounts(1)
                sessions = [acc["password"] for acc in self.created_accounts]
                if action == "like":
                    self.actions.mass_like(self.target_media_id, count, sessions[0])
                elif action == "comment":
                    self.actions.mass_comment(self.target_media_id, count, COMMENTS, sessions[0])
                elif action == "follow":
                    self.actions.mass_follow(self.target_user_id, count, sessions[0])
                elif action == "share":
                    self.actions.mass_share(self.target_media_id, count, sessions[0])
                elif action == "save":
                    self.actions.mass_save(self.target_media_id, count, sessions[0])

            console.print(Fore.CYAN + "\n" + "="*60)
            if not Confirm.ask("[?] আরো কিছু করবেন?"):
                break

if __name__ == "__main__":
    try:
        tool = AhnafV4()
        tool.run()
    except KeyboardInterrupt:
        console.print(Fore.RED + "\n[!] বন্ধ করা হচ্ছে...")
    except Exception as e:
        console.print(Fore.RED + f"\n[!] এরর: {e}")
