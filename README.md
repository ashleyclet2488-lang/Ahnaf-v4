# ⚡ Ahnaf v4 — Instagram Pentest Toolkit

<p align="center">
  <img src="https://img.shields.io/badge/version-4.0-brightgreen">
  <img src="https://img.shields.io/badge/platform-Termux%20%7C%20Linux-blue">
  <img src="https://img.shields.io/badge/python-3.8%2B-yellow">
  <img src="https://img.shields.io/badge/license-Educational%20Only-red">
</p>
**👑 Owner:** Ahnaf  
**📌 Version:** 4.0  
**⚙ Mode:** Multi-Proxy + Temp Mail Account Generator  
**🔥 Features:** Like · Comment · Follow · Share · Save · Report · Broadcast Join

---

## 📋 সূচিপত্র

- [পরিচিতি](#-পরিচিতি)
- [ফিচারসমূহ](#-ফিচারসমূহ)
- [ইনস্টলেশন](#-ইনস্টলেশন)
- [ব্যবহার বিধি](#-ব্যবহার-বিধি)
- [মেনু গাইড](#-মেনু-গাইড)
- [রিপোর্ট রিজন](#-রিপোর্ট-রিজন)
- [ফাইল স্ট্রাকচার](#-ফাইল-স্ট্রাকচার)
- [ট্রাবলশুটিং](#-ট্রাবলশুটিং)
- [নিরাপত্তা সতর্কতা](#-নিরাপত্তা-সতর্কতা)
- [লাইসেন্স](#-লাইসেন্স)

---

## 🌟 পরিচিতি

**Ahnaf v4** একটি সম্পূর্ণ Instagram পেন্টেস্ট টুলকিট যা বিশেষভাবে **Termux** ও **Linux** পরিবেশের জন্য ডিজাইন করা হয়েছে। এই টুলটি একাধিক প্রক্সি ও টেম্পোরারি মেইল ব্যবহার করে স্বয়ংক্রিয়ভাবে অ্যাকাউন্ট তৈরি করে এবং বিভিন্ন অ্যাকশন সম্পাদন করে।

### কেন Ahnaf v4?

| বৈশিষ্ট্য | বর্ণনা |
|-----------|--------|
| ✅ **100% রিয়াল** | সব অ্যাকশন রিয়েল Instagram API ব্যবহার করে |
| ✅ **মাল্টি-প্রক্সি** | ৫০০+ প্রক্সি অটো সংগ্রহ ও ভ্যালিডেশন |
| ✅ **টেম্প মেইল** | mail.tm API দিয়ে অটো ইমেইল জেনারেশন |
| ✅ **থ্রেডিং** | ২০টি কনকারেন্ট থ্রেড support |
| ✅ **কমপ্লিট মেনু** | ব্যবহার করা অত্যন্ত সহজ, বাংলা ভাষায় |

---

## 🚀 ফিচারসমূহ

| অপশন | ফিচার | বর্ণনা | কনকারেন্সি |
|------|--------|--------|------------|
| 1 | ❤️ **Mass Like** | এক পোস্টে হাজারো লাইক | 20 থ্রেড |
| 2 | 💬 **Mass Comment** | কাস্টম কমেন্ট পাঠানো | 15 থ্রেড |
| 3 | 👥 **Mass Follow** | ফলোয়ার বুস্ট | 20 থ্রেড |
| 4 | 🔄 **Mass Share** | DM এর মাধ্যমে শেয়ার | 15 থ্রেড |
| 5 | 💾 **Mass Save** | পোস্ট সেভ বুস্ট | 15 থ্রেড |
| 6 | 🚨 **Mass Report** | ১২টি কারণ সহ রিপোর্ট | 10 থ্রেড |
| 7 | 📡 **Join Broadcast** | লাইভ ব্রডকাস্টে জয়েন | 20 থ্রেড |
| 8 | 📧 **Create Accounts** | টেম্প মেইল দিয়ে অটো অ্যাকাউন্ট | সিরিয়াল |

---

## 📥 ইনস্টলেশন

### Termux-এর জন্য:

```bash
# 1. প্যাকেজ আপডেট
pkg update && pkg upgrade -y

# 2. প্রয়োজনীয় প্যাকেজ ইন্সটল
pkg install git python python-pip -y

# 3. টুল ক্লোন
git clone https://github.com/Ahnaf/Ahnaf-v4
cd Ahnaf-v4

# 4. ডিপেন্ডেন্সি ইন্সটল
pip install -r requirements.txt

# 5. টুল চালান
python main.py
