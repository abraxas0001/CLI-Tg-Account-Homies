# CLI-Tg-Account-Homies

A lightweight, user-friendly Telegram client that works in your terminal (CLI) or your browser (local web UI). Built with Python and Telethon.

> **🌎 WHY THIS EXISTS:**
> Many Telegram channels and groups are **geo-restricted** in Asian countries. This shared Colombian phone number account allows you to **bypass regional restrictions** and access content that would otherwise be blocked in your region.

> **⚠️ IMPORTANT SECURITY NOTICE:**
> - This account is **2FA-protected** and shared for public use
> - **Contact the administrator** to get access (easiest way - no technical setup!)
> - The administrator monitors all activity and can change the password anytime
> - Username may change frequently (it is dynamic)
> - Do not attempt to terminate other sessions or change account settings

> **👉 RECOMMENDED FOR BEGINNERS:** Contact admin for instant access (see Method 1 below) - no installation needed!

---

## 📞 Contact Admin for Access

<div align="center">

### **Need Access? Contact the Owner:**

<a href="https://t.me/TestingAccountHomies" target="_blank">
  <img src="https://img.shields.io/badge/Telegram-@TestingAccountHomies-blue?style=for-the-badge&logo=telegram" alt="Contact on Telegram"/>
</a>

**👉 Click above to message on Telegram**

**Account Details:**
- 📱 Phone Number: `+57 313 531 6429` (Colombian number)
- 🔐 2FA Password (admin provides when you request access)
- 📨 Verification codes (admin receives and forwards to you)
- 👤 User ID: `7387738015`

</div>

---

## Features

- **Bypass geo-restrictions** - Access channels/groups blocked in Asian regions
- **Colombian phone number** - Unrestricted access to most Telegram content
- CLI interface for fast, keyboard-driven use
- Web interface with a clean, Telegram-like layout
- Real-time message view and send
- Uses official Telegram API via Telethon
- Local-only hosting for privacy
- **2FA password required** - contact admin for access

## Use Cases

- ✅ Access geo-restricted channels and groups
- ✅ View content blocked in your country
- ✅ Join international communities without VPN
- ✅ Monitor messages from restricted sources
- ✅ Bypass regional Telegram limitations

---

## 🚀 How to Get Access - Two Methods

Choose the method that suits your technical level:

### 🌟 **Method 1: Easy Way (Recommended for Beginners)**
**⏱️ Takes: 5 minutes** | **Difficulty: Easy** | **Best for: Quick access without technical setup**

Contact the admin directly and get instant access through their existing sessions:

1. **Message [@TestingAccountHomies](https://t.me/TestingAccountHomies)** on Telegram
2. Request: "I need access to the shared account"
3. Admin will provide:
   - 📱 **Pre-logged session** (ready to use)
   - 🔐 **2FA password** (in case you need to re-login)
   - 🔗 **Web interface link** (if available)
4. ✅ **Start using immediately** - no setup needed!

**What you get:**
- Instant access to geo-restricted content
- No Python installation required
- No configuration needed
- Admin handles all technical aspects

---

### 💻 **Method 2: CLI/Web Setup (Advanced)**
**⏱️ Takes: 15-20 minutes** | **Difficulty: Intermediate** | **Best for: Developers who want local control**

Set up the Telegram client on your own machine with full CLI/Web interface:

**What you need from admin:**
- 📱 Phone Number: `+57 313 531 6429`
- 🔐 2FA Password (for login)
- 📨 Verification codes (admin forwards when you login)

**What you provide yourself:**
- Your own Telegram API credentials (from my.telegram.org)
- Python 3.8+ environment
- Basic command-line knowledge

**Use this method if you want to:**
- Run the client on your own computer
- Use CLI commands or local web interface
- Have full control over the session
- Automate tasks with scripts

---

## 📖 Complete Setup Guide (Method 2 - CLI/Web)

> ⚠️ **New users: Try Method 1 first!** It's much easier. Only use this method if you need local CLI/Web access.

Follow these steps carefully to set up the client on your machine:

### **Step 1: Contact Admin for Credentials**

Before starting the technical setup:

1. Open Telegram and message: **[@TestingAccountHomies](https://t.me/TestingAccountHomies)**
2. Send: "Hi, I need access to the shared Telegram account for CLI setup"
3. Admin will provide you with:
   - 📱 **Phone Number** (Colombian number: `+57 313 531 6429`)
   - 🔐 **2FA Password** (changes regularly for security)
   - 👤 **Account Info** (User ID: `7387738015`, name varies)
4. **Save these credentials** - you'll need them during login

> ⚠️ **IMPORTANT:** You MUST use the admin's phone number (+57 313 531 6429) to login, NOT your own number. This is a shared account specifically for bypassing geo-restrictions.

### **Step 2: Clone This Repository**

```bash
git clone https://github.com/abraxas0001/CLI-Tg-Account-Homies.git
cd CLI-Tg-Account-Homies
```

### **Step 3: Install Python Dependencies**

```bash
pip install -r requirements.txt
```

This installs:
- `telethon` - Telegram client library
- `flask` - Web interface
- `python-dotenv` - Environment variable loader
- `cryptg` - Faster encryption

### **Step 4: Get Your Own Telegram API Credentials**

You need your own API credentials (these are different from the account login):

> 📌 **NOTE:** API credentials are YOUR personal developer keys to access Telegram's API. The phone number (+57 313 531 6429) is the SHARED ACCOUNT you'll login to.

1. Go to: https://my.telegram.org
2. Login with **your personal** Telegram phone number (your own number, not the shared one)
3. Click "API Development Tools"
4. Fill in:
   - App title: `My Telegram CLI`
   - Short name: `tg_cli`
   - Platform: `Desktop`
5. Click "Create Application"
6. **Copy your `api_id` and `api_hash`** (you'll need these)

> ℹ️ These API keys are like your developer license - you use them to connect to Telegram, but you'll login to the admin's shared account.

### **Step 5: Configure the Application**

Choose one method:

**Method A: Using config.py (Recommended for beginners)**

1. Copy the example config:
   ```bash
   copy config.example.py config.py
   ```

2. Edit `config.py` with your API credentials:
   ```python
   api_id = 12345678  # Your api_id from Step 4
   api_hash = "abc123def456"  # Your api_hash from Step 4
   session_name = "my_session"  # Any name you want
   ```

**Method B: Using .env file**

1. Copy the example:
   ```bash
   copy .env.example .env
   ```

2. Edit `.env`:
   ```
   TELEGRAM_API_ID=12345678
   TELEGRAM_API_HASH=abc123def456
   TELEGRAM_SESSION_NAME=my_session
   ```

### **Step 6: Login to the Shared Account (CLI)**

Now you're ready to login using the admin's shared account:

```bash
python login.py
```

**What will happen:**

1. Script asks: `Enter phone number (with country code):`
   - ⚠️ **CRITICAL:** Type the SHARED phone number: `+573135316429`
   - **DO NOT** use your own phone number
   - This is the Colombian number that bypasses geo-restrictions

2. Telegram sends verification code to that number
   - Script shows: `📱 Verification code sent to +573135316429`
   - **The admin receives this code on their phone**

3. **Immediately message the admin:** "I need the verification code that was just sent"
   - Admin will reply with the 6-digit code
   - Example: `123456`

4. Script asks: `Enter the verification code:`
   - Type the code the admin gave you
   - Press Enter

5. Script asks: `Enter 2FA password:` (hidden input - you won't see what you type)
   - Type the 2FA password the admin gave you in Step 1
   - Press Enter

6. ✅ **Success!** You'll see:
   ```
   ╔══════════════════════════════════════════════════════╗
   ║           LOGIN SUCCESSFUL!                           ║
   ╚══════════════════════════════════════════════════════╝
   Name: [Admin's Name]
   Username: @[varies - changes frequently]
   Phone: +573135316429
   User ID: 7387738015
   ```

7. Session is saved as `my_session.session` (or whatever name you chose)

> 🎉 **You're now logged into the shared Colombian account!** You can access geo-restricted channels and groups that are blocked in Asian countries.

### **Step 7: Start Using the CLI**

```bash
python telegram_desktop_cli.py
```

**You'll see:**
```
======================================================================
          🚀 TELEGRAM CLI - Logged in (username may change) 🚀
======================================================================

🔄 Connecting to Telegram...
✅ Logged in as: [Admin's Name]
   Username: @[varies - changes frequently]
   Phone: +573135316429
   User ID: 7387738015
======================================================================

📱 Fetching your recent chats...

#    Name                          Unread
──────────────────────────────────────────────────────────────────────
1    Saved Messages                -
2    Some Channel                  5
3    Friend                        2
...
```

> 🌍 **You're using the Colombian number now!** You can access channels and groups that are geo-blocked in Asian countries.

**Available Commands:**
- `/list` - Show all chats
- `/read <number>` - Read messages from a chat (e.g., `/read 2`)
- `/send <number> <message>` - Send message (e.g., `/send 2 Hello!`)
- `/me` - Show account info (will show the shared account details)
- `/quit` - Exit

### **Step 8 (Optional): Use Web Interface**

For a visual browser interface:

```bash
python telegram_web_app.py
```

Then open: http://localhost:5000

---

## 📋 Quick Reference

| Task | Command |
|------|---------|
| First login | `python login.py` |
| CLI interface | `python telegram_desktop_cli.py` |
| Web interface | `python telegram_web_app.py` |
| Watch messages | `python watch_messages.py` |
| Verify session | `python verify_session.py` |

---

## ❓ Troubleshooting

**"I don't have the 2FA password"**
- Contact [@TestingAccountHomies](https://t.me/TestingAccountHomies) on Telegram

**"I don't know the phone number"**
- Use the shared Colombian number: `+573135316429`
- Contact [@TestingAccountHomies](https://t.me/TestingAccountHomies) if you need confirmation

**"I entered my own phone number by mistake"**
- ❌ This won't work! You must use the shared number: `+573135316429`
- The whole point is to use the Colombian number to bypass geo-restrictions
- Start over with `python login.py` and enter the correct number

**"I need the verification code"**
- Ask the admin - the code goes to their phone, not yours

**"Import 'config_loader' could not be resolved"**
- Make sure you ran `pip install -r requirements.txt`
- Try: `pip install telethon flask python-dotenv cryptg`

**"Session expired"**
- Delete the `.session` file
- Run `python login.py` again
- Contact admin for 2FA password again

**"2FA password incorrect"**
- Double-check with the admin
- Password may have changed (admin updates it regularly)

---
   
## Security & Usage Rules

### What You Can Do:
- ✅ Read and send messages
- ✅ View chats and groups
- ✅ Use CLI or Web interface
- ✅ Monitor incoming messages

### What You CANNOT Do:
- ❌ Terminate other active sessions
- ❌ Change account settings
- ❌ Attempt to change phone number
- ❌ Try to disable 2FA
- ❌ Export account data

### Administrator Rights:
- 🔍 Can monitor all your activity
- 🔐 Can change 2FA password anytime (will lock you out)
- 🚫 Can terminate your session remotely
- ⚠️ Violation of rules = immediate access revocation

### How It Works:
1. You request 2FA password from admin
2. Admin provides temporary access
3. You login and use the account
4. Admin monitors activity
5. Admin changes password after your session ends

## Project Structure

```
├── login.py                    # Login with 2FA password prompt
├── telegram_desktop_cli.py     # CLI interface
├── telegram_web_app.py         # Web interface
├── watch_messages.py           # Real-time message monitor
├── verify_session.py           # Session verification
├── check_messages.py           # Check recent messages
├── config_loader.py            # Secure config loader
├── config.example.py           # Config template
├── .env.example                # Environment variables template
├── requirements.txt            # Python dependencies
├── .gitignore                  # Git ignore file
├── LICENSE                     # MIT License
└── README.md                   # This file
```

## Security Notes

- **2FA password is never stored in code** - you enter it at login time
- Never commit `.session` files or your `config.py`
- `.gitignore` already excludes session files and secrets
- Contact admin for 2FA password - don't share it with others
- Admin can see who logs in and when

## For Administrators

To change the 2FA password and lock out current users:
1. Login to Telegram (any client)
2. Settings → Privacy & Security → Two-Step Verification
3. Change password
4. All active sessions will require new password on next login

To monitor active sessions:
1. Settings → Privacy & Security → Active Sessions
2. View all logged-in devices and terminate suspicious ones

---

## 📜 License

MIT License - see [LICENSE](LICENSE) file for details.

## 👤 Credits

Created and maintained by <a href="https://github.com/abraxas0001" target="_blank" rel="noopener noreferrer">**Abra**</a>

This project was built to help users bypass geo-restrictions and access Telegram content that may be blocked in their region. The shared Colombian number provides unrestricted access to channels and groups.

**Support & Contact:**
- GitHub: [@abraxas0001](https://github.com/abraxas0001)
- Telegram: [@TestingAccountHomies](https://t.me/TestingAccountHomies)
- For 2FA password access: Message on Telegram

**🙏 If this helped you bypass geo-restrictions, please star the repo!** ⭐

---

## ⚠️ Disclaimer

This is an unofficial Telegram client for educational and accessibility purposes. Users are responsible for complying with Telegram's Terms of Service and local laws. Use at your own risk.
