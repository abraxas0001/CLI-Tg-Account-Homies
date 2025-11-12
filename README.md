# CLI-Tg-Account-Homies

A lightweight, user-friendly Telegram client that works in your terminal (CLI) or your browser (local web UI). Built with Python and Telethon.

> **🌎 WHY THIS EXISTS:**
> Many Telegram channels and groups are **geo-restricted** in Asian countries. This shared Colombian phone number account allows you to **bypass regional restrictions** and access content that would otherwise be blocked in your region.

> **⚠️ IMPORTANT SECURITY NOTICE:**
> - This account is **2FA-protected** and shared for public use
> - **Contact the administrator** to get the 2FA password before login
> - The administrator monitors all activity and can change the password anytime
> - Username may change frequently (it is dynamic)
> - Do not attempt to terminate other sessions or change account settings

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

## 🎯 Use Cases

- Access Telegram on servers without GUI
- Lightweight alternative to desktop clients
- Script automation for Telegram
- Monitor messages in real-time
- Use Telegram through SSH sessions

## Prerequisites

- Python 3.8+
- **2FA password from administrator** (contact before proceeding)
- Telegram API credentials (api_id and api_hash from [my.telegram.org](https://my.telegram.org))

## Quick Start

1) **Contact Administrator First**
   - You MUST get the 2FA password before attempting to login
   - The administrator will provide it upon request

2) Install dependencies

```bash
pip install -r requirements.txt
```

3) Configure credentials (without exposing secrets)

Choose one:

**Option A:** Create `config.py` (ignored by git) from `config.example.py` and fill in:
```python
api_id = 123456
api_hash = "your_api_hash_here"
session_name = "my_session"
```

**Option B:** Use environment variables (recommended). Create `.env` from `.env.example`:
```
TELEGRAM_API_ID=123456
TELEGRAM_API_HASH=your_hash_here
TELEGRAM_SESSION_NAME=my_session
```

Get API credentials from https://my.telegram.org → API Development Tools

4) First login

```bash
python login.py
```

**When prompted:**
- Enter the phone number (provided by admin)
- Enter verification code from Telegram
- **Enter the 2FA password** (you got from admin)

Follow the prompts. The script will ask for the 2FA password during login.

## Usage

**CLI (desktop-like):** (username may change)
```bash
python telegram_desktop_cli.py
```

**Web UI** (local server at http://localhost:5000):
```bash
python telegram_web_app.py
```

**Watch incoming messages** (e.g., login codes):
```bash
python watch_messages.py
```

**Verify your session:**
```bash
python verify_session.py
```

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
- For 2FA password access, contact the repository owner

---

## ⚠️ Disclaimer

This is an unofficial Telegram client for educational and accessibility purposes. Users are responsible for complying with Telegram's Terms of Service and local laws. Use at your own risk.
