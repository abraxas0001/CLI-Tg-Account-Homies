# 🚀 CLI-Tg-Account-Homies

> A comprehensive Telegram automation toolkit featuring CLI and Web interfaces for managing shared Telegram accounts with 2FA protection.

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Telethon](https://img.shields.io/badge/Telethon-1.35%2B-blue.svg)](https://github.com/LonamiWebs/Telethon)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

---

## 📋 Table of Contents

- [What is This?](#-what-is-this)
- [Why is This Necessary?](#-why-is-this-necessary)
- [Key Features](#-key-features)
- [Use Cases](#-use-cases)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Security](#-security)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

---

## 🤔 What is This?

**CLI-Tg-Account-Homies** is a Python-based automation toolkit that provides multiple interfaces for interacting with Telegram accounts. It's specifically designed for shared account scenarios with robust Two-Factor Authentication (2FA) support.

### Components:

1. **🖥️ Desktop CLI Interface** (`telegram_desktop_cli.py`)
   - Real-time message monitoring
   - Send/receive messages via command-line
   - Chat management and navigation
   - Perfect for automation and scripting

2. **🌐 Web Interface** (`telegram_web_app.py`)
   - Beautiful Telegram-like UI in your browser
   - Real-time message updates
   - User-friendly chat interface
   - No mobile app required

3. **🔐 Authentication System** (`login.py`, `verify_session.py`)
   - Secure 2FA login flow
   - Session management
   - Authorization verification

4. **⚙️ Configuration Manager** (`config_loader.py`)
   - Centralized configuration
   - Secure credential handling

---

## 💡 Why is This Necessary?

### Real-World Problems This Solves:

#### 1. **Shared Account Management**
- **Problem:** Multiple team members need access to one Telegram account
- **Solution:** This toolkit allows controlled access with 2FA protection, ensuring only authorized users can access the account

#### 2. **Automation & Bot Integration**
- **Problem:** Need to automate Telegram interactions without official Bot API limitations
- **Solution:** Full user account automation with all Telegram features available (unlike Bot API)

#### 3. **Cross-Platform Access**
- **Problem:** Want to use Telegram on systems where desktop app isn't available or allowed
- **Solution:** Web interface accessible from any browser, CLI for server environments

#### 4. **Testing & Development**
- **Problem:** Developers need to test Telegram integrations
- **Solution:** Safe testing environment with session isolation and 2FA protection

#### 5. **Remote System Management**
- **Problem:** Need to access Telegram from headless servers or remote machines
- **Solution:** CLI interface perfect for SSH sessions and automated workflows

#### 6. **Privacy & Control**
- **Problem:** Want more control over Telegram session than official apps provide
- **Solution:** Complete control over session files, authentication, and data

#### 7. **Geographic Restrictions & Censorship Bypass**
- **Problem:** Many groups and channels are blocked or unavailable in Asian countries due to regional restrictions
- **Solution:** Access Telegram through alternative routes, bypassing geographic limitations and censorship. Connect to restricted content that's unavailable through official apps in your region

---

## ✨ Key Features

### 🔐 Security Features
- ✅ **2FA Protection** - Mandatory Two-Factor Authentication
- ✅ **Session Management** - Secure session file handling
- ✅ **Password Validation** - Hidden password input with getpass
- ✅ **Access Control** - Administrator-controlled account access

### 💬 Messaging Features
- ✅ **Real-Time Messages** - Instant message notifications
- ✅ **Send Messages** - To users, groups, and channels
- ✅ **Read History** - Browse past conversations
- ✅ **Chat Management** - List and navigate chats
- ✅ **Media Support** - Handle photos, videos, stickers

### 🖥️ Interface Options
- ✅ **CLI Interface** - Command-line for power users
- ✅ **Web Interface** - Beautiful browser-based UI
- ✅ **Real-Time Updates** - Auto-refresh and live notifications
- ✅ **Multi-Platform** - Works on Windows, Linux, macOS

### 🛠️ Developer Features
- ✅ **Clean Code** - Well-documented and maintainable
- ✅ **Error Handling** - Comprehensive exception management
- ✅ **Async/Await** - Modern asynchronous Python
- ✅ **Modular Design** - Easy to extend and customize

---

## 🎯 Use Cases

### For Teams
```
✓ Customer support team sharing support account
✓ Social media team managing company Telegram
✓ Development team testing integrations
✓ Multiple admins for community channels
```

### For Developers
```
✓ Automate message sending and monitoring
✓ Build custom Telegram workflows
✓ Test Telegram integrations
✓ Create notification systems
```

### For System Administrators
```
✓ Server monitoring via Telegram
✓ Remote system management
✓ Automated alert systems
✓ Log forwarding to Telegram
```

### For Power Users
```
✓ Access Telegram from any browser
✓ Use Telegram in restricted environments
✓ Script Telegram interactions
✓ Backup and archive chats
```

---

## 📦 Installation

### Prerequisites

- **Python 3.8 or higher**
- **Telegram Account**
- **Telegram API Credentials** (get from [my.telegram.org](https://my.telegram.org))

### Step 1: Clone Repository

```bash
git clone https://github.com/abraxas0001/CLI-Tg-Account-Homies.git
cd CLI-Tg-Account-Homies
```

### Step 2: Create Virtual Environment (Recommended)

**Windows:**
```powershell
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

**Dependencies:**
- `telethon>=1.35.0` - Telegram MTProto API library
- `flask>=3.0.0` - Web framework for web interface
- `cryptg>=0.4.0` - Cryptography speedup for Telethon

---

## ⚙️ Configuration

### Step 1: Get Access to Shared Account

**📱 Shared Test Account Available!**

This project includes a shared Colombian Telegram account for testing purposes.

**Phone Number:** `+573135316429`

**To get access:**
1. 📞 Contact the owner on Telegram: [@TestingAccountHomies](https://t.me/TestingAccountHomies)
2. 🔑 Request the **2FA password** for the shared account
3. 📱 Install Telegram app on your device
4. 🔐 Login using the phone number `+573135316429`
5. 💬 Get the verification code (owner will provide)
6. 🔒 Enter the 2FA password (owner will provide)

**⚠️ Important:**
- This is a **shared testing account** - multiple users may have access
- You **MUST** get the 2FA password from the owner to login
- The owner can monitor activity and revoke access anytime
- Use responsibly and follow guidelines

---

### Step 2: Get Telegram API Credentials

1. Visit [my.telegram.org](https://my.telegram.org)
2. Log in with your phone number
3. Click on **"API Development Tools"**
4. Create a new application
5. Save your `api_id` and `api_hash`

### Step 3: Create Configuration File

```bash
# Copy the example config
copy config.example.py config.py    # Windows
cp config.example.py config.py      # Linux/macOS
```

### Step 4: Edit Configuration

Open `config.py` and add your credentials:

```python
# Telegram API Configuration
api_id = 12345678  # Replace with your API ID
api_hash = "your_api_hash_here"  # Replace with your API hash
session_name = "my_telegram_session"  # Choose any name

# Optional - For shared test account
phone_number = "+573135316429"  # Colombian shared account (get 2FA from owner)
password_2fa = ""  # Enter 2FA password provided by owner
```

**⚠️ Security Note:** 
- Never commit `config.py` to Git (it's in `.gitignore`)
- Keep your API credentials private
- Don't share your session files

---

## 🚀 Usage

### 1️⃣ First-Time Login

Run the login script to authenticate:

```bash
python login.py
```

**For Shared Test Account:**
- Use phone number: `+573135316429`
- Get 2FA password from: [@TestingAccountHomies](https://t.me/TestingAccountHomies)

**What happens:**
1. Enter your phone number (with country code, e.g., `+573135316429`)
2. Receive verification code via Telegram
3. Enter the code
4. Enter 2FA password (get from owner if using shared account)
5. Session saved to `{session_name}.session`

**Example Output:**
```
═══════════════════════════════════════════════════════════════
     TELEGRAM LOGIN - 2FA PROTECTED ACCOUNT
═══════════════════════════════════════════════════════════════

⚠️  This account requires 2FA password for login.
📞 Contact the administrator to get the 2FA password.

[1] Connecting to Telegram...
[2] Starting login process...

Enter phone number (with country code, e.g., +573135316429): +573135316429

📱 Verification code sent to +573135316429
Enter the verification code: 12345

🔐 Two-Factor Authentication is enabled.
Enter 2FA password: ********

✅ Logged in successfully with 2FA!

╔══════════════════════════════════════════════════════════╗
║           LOGIN SUCCESSFUL!                               ║
╚══════════════════════════════════════════════════════════╝
  Name: John Doe
  Username: @johndoe
  Phone: +1234567890
  User ID: 123456789

✅ Session saved as: my_telegram_session.session
```

---

### 2️⃣ Using CLI Interface

Launch the command-line interface:

```bash
python telegram_desktop_cli.py
```

**Available Commands:**

| Command | Description | Example |
|---------|-------------|---------|
| `/list` | Show recent chats | `/list` |
| `/read <number>` | Read messages from chat | `/read 1` |
| `/send <target> <message>` | Send message | `/send 1 Hello!` |
| `/me` | Show account info | `/me` |
| `/quit` | Exit application | `/quit` |

**Example Session:**
```
═══════════════════════════════════════════════════════════════
     🚀 TELEGRAM CLI - 2FA Protected Shared Account 🚀
═══════════════════════════════════════════════════════════════

🔐 2FA VERIFICATION REQUIRED
Enter 2FA password: ********

✅ Connected to shared account!
   Name: John Doe
   Username: @johndoe
   Phone: +1234567890
   User ID: 123456789

📱 Fetching your recent chats...

#    Name                           Unread
──────────────────────────────────────────────────────────────
1    Alice                          3
2    Bob                            -
3    Project Team                   5
4    News Channel                   15

COMMANDS:
  /send <number_or_username> <message>  - Send a message
  /list                                  - Show chats again
  /read <number>                        - Read last messages from a chat
  /me                                   - Show your info
  /quit                                 - Exit

>> /send 1 Hello Alice!
✅ Message sent to 1

>> /read 1
📖 Last 10 messages from 'Alice':
──────────────────────────────────────────────────────────────
[2025-11-12 10:30] Alice: Hey there!
[2025-11-12 10:31] John Doe: Hello Alice!
──────────────────────────────────────────────────────────────

>> /quit
👋 Goodbye!
```

---

### 3️⃣ Using Web Interface

Launch the web interface:

```bash
python telegram_web_app.py
```

**What happens:**
1. Enter 2FA password
2. Server starts on `http://localhost:5000`
3. Browser opens automatically
4. Beautiful Telegram-like interface appears

**Features:**
- 📱 Chat list with unread counts
- 💬 Real-time messaging
- 🔄 Auto-refresh (every 3-5 seconds)
- 🎨 Telegram-inspired dark theme
- 📝 Message history browsing

**Screenshot Description:**
```
┌─────────────────────────────────────────────────────────┐
│ Sidebar (Left)          │ Chat Area (Right)             │
│ ─────────────────       │ ─────────────────             │
│ Telegram                │ Chat Name                     │
│ John Doe • @johndoe     │ ─────────────────             │
│ [🔄 Refresh Chats]      │                               │
│                         │ Message bubbles...            │
│ • Alice (3 new)         │ [Sent messages: Purple]       │
│ • Bob                   │ [Received: Blue]              │
│ • Project Team (5 new)  │                               │
│ • News Channel (15 new) │ ─────────────────             │
│                         │ [Type a message...] [Send]    │
└─────────────────────────────────────────────────────────┘
```

---

### 4️⃣ Verify Session

Check if your session is still valid:

```bash
python verify_session.py
```

**Output:**
```
═══════════════════════════════════════════════════════
TELEGRAM SESSION VERIFICATION & LOGIN
═══════════════════════════════════════════════════════

[1] Connecting to Telegram...
✓ Session is VALID and AUTHORIZED!

╔══════════════════════════════════════════════════════╗
║  LOGGED IN SUCCESSFULLY!                              ║
╚══════════════════════════════════════════════════════╝
  Name: John Doe
  Username: @johndoe
  Phone: +1234567890
  User ID: 123456789

[2] Fetching recent chats...
Found 5 recent chats:
  1. Alice
  2. Bob
  3. Project Team
  4. News Channel
  5. Support

✓ Session is working perfectly!
```

---

## 📁 Project Structure

```
CLI-Tg-Account-Homies/
│
├── 📄 telegram_desktop_cli.py     # Main CLI interface
├── 🌐 telegram_web_app.py         # Web interface with Flask
├── 🔐 login.py                    # First-time authentication
├── ✅ verify_session.py           # Session validation tool
├── ⚙️ config_loader.py            # Configuration management
│
├── 📋 config.example.py           # Configuration template
├── 🔑 config.py                   # Your credentials (gitignored)
│
├── 📦 requirements.txt            # Python dependencies
├── 📖 README.md                   # This file
├── 🤝 CONTRIBUTING.md             # Contribution guidelines
├── 📜 LICENSE                     # MIT License
│
└── 🗄️ {session_name}.session     # Session file (created after login)
```

### File Descriptions:

| File | Purpose | When to Use |
|------|---------|-------------|
| `telegram_desktop_cli.py` | Command-line interface | Daily CLI usage |
| `telegram_web_app.py` | Web-based interface | When you prefer GUI |
| `login.py` | Initial authentication | First-time setup |
| `verify_session.py` | Check session validity | Troubleshooting |
| `config_loader.py` | Load configuration | Internal use |
| `config.py` | Your API credentials | Configure once |
| `requirements.txt` | Python packages | Installation |

---

## 🔒 Security

### Best Practices

#### ✅ DO:
- ✅ Keep your `config.py` private
- ✅ Use strong 2FA passwords
- ✅ Regularly verify your session
- ✅ Keep session files secure
- ✅ Use virtual environments
- ✅ Update dependencies regularly

#### ❌ DON'T:
- ❌ Share your `api_id` or `api_hash`
- ❌ Commit `config.py` to Git
- ❌ Share session files
- ❌ Use weak 2FA passwords
- ❌ Run on untrusted networks without VPN
- ❌ Leave session files in public directories

### Security Features

1. **Two-Factor Authentication (2FA)**
   - Mandatory password verification
   - Hidden password input (getpass)
   - Failed login protection

2. **Session Security**
   - Encrypted session files
   - Session validation on startup
   - Automatic session expiry detection

3. **Code Security**
   - No hardcoded credentials
   - Secure configuration loading
   - Exception handling for errors

### For Shared Accounts

**Administrator Responsibilities:**
- 🔐 Control and manage 2FA password
- 👥 Grant access to trusted users only
- 📊 Monitor account activity
- 🚫 Revoke access when needed

**User Responsibilities:**
- 🤐 Keep 2FA password confidential
- 📞 Contact admin for access issues
- ⚠️ Report suspicious activity
- ✅ Follow security guidelines

**Contact Admin:**
- Telegram: [@TestingAccountHomies](https://t.me/TestingAccountHomies)

---

## 🐛 Troubleshooting

### Common Issues

#### 1. **"config.py not found" Error**

**Problem:** Configuration file missing

**Solution:**
```bash
# Copy example config
copy config.example.py config.py    # Windows
cp config.example.py config.py      # Linux/macOS

# Edit with your credentials
notepad config.py    # Windows
nano config.py       # Linux/macOS
```

---

#### 2. **"Session expired" Error**

**Problem:** Session file invalid or expired

**Solution:**
```bash
# Delete old session
del {session_name}.session    # Windows
rm {session_name}.session     # Linux/macOS

# Login again
python login.py
```

---

#### 3. **"Incorrect 2FA password" Error**

**Problem:** Wrong 2FA password entered

**Solution:**
- Contact account administrator for correct password
- Telegram: [@TestingAccountHomies](https://t.me/TestingAccountHomies)
- Verify you're using the current password (may change)

---

#### 4. **Import Errors**

**Problem:** Missing dependencies

**Solution:**
```bash
# Reinstall dependencies
pip install -r requirements.txt --upgrade

# Or install individually
pip install telethon flask cryptg
```

---

#### 5. **Web Interface Won't Start**

**Problem:** Port 5000 already in use or Flask issues

**Solution:**
```bash
# Check if port is in use
netstat -ano | findstr :5000    # Windows
lsof -i :5000                   # Linux/macOS

# Kill process using port (if needed)
# Then restart web interface
python telegram_web_app.py
```

---

#### 6. **"FloodWaitError" Exception**

**Problem:** Too many requests to Telegram API

**Solution:**
- Wait for the specified time (shown in error)
- Reduce frequency of requests
- This is Telegram's rate limiting

---

#### 7. **Connection Issues**

**Problem:** Can't connect to Telegram servers

**Solution:**
```bash
# Check internet connection
ping telegram.org

# Try again after a moment
python verify_session.py

# If persists, check firewall/proxy settings
```

---

### Getting Help

**Before asking for help:**
1. ✅ Check this README thoroughly
2. ✅ Read error messages carefully
3. ✅ Try troubleshooting steps above
4. ✅ Search [GitHub Issues](https://github.com/abraxas0001/CLI-Tg-Account-Homies/issues)

**How to ask for help:**
1. Open a [GitHub Issue](https://github.com/abraxas0001/CLI-Tg-Account-Homies/issues/new)
2. Include:
   - What you were trying to do
   - What actually happened
   - Error messages (full traceback)
   - System info (OS, Python version)
   - Steps to reproduce

**Contact:**
- 📧 GitHub Issues: [Create Issue](https://github.com/abraxas0001/CLI-Tg-Account-Homies/issues)
- 💬 Telegram: [@TestingAccountHomies](https://t.me/TestingAccountHomies)

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Ways to Contribute

- 🐛 **Report Bugs** - Found an issue? Let us know!
- 💡 **Suggest Features** - Have an idea? Share it!
- 📖 **Improve Documentation** - Help others understand
- 🔧 **Submit Code** - Fix bugs or add features
- ⭐ **Star the Project** - Show your support!

### Quick Start

```bash
# 1. Fork the repository
# 2. Clone your fork
git clone https://github.com/YOUR_USERNAME/CLI-Tg-Account-Homies.git

# 3. Create a branch
git checkout -b feature/amazing-feature

# 4. Make your changes
# 5. Commit your changes
git commit -m "feat: add amazing feature"

# 6. Push to your fork
git push origin feature/amazing-feature

# 7. Open a Pull Request
```

### Contribution Guidelines

Please read our [CONTRIBUTING.md](CONTRIBUTING.md) for:
- Code style guidelines
- Commit message conventions
- Pull request process
- Testing requirements

---

## 📜 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

**What this means:**
- ✅ Commercial use allowed
- ✅ Modification allowed
- ✅ Distribution allowed
- ✅ Private use allowed
- ⚠️ License and copyright notice required
- ❌ No liability or warranty

---

## 📞 Contact

### Project Maintainer
- **GitHub:** [@abraxas0001](https://github.com/abraxas0001)
- **Project:** [CLI-Tg-Account-Homies](https://github.com/abraxas0001/CLI-Tg-Account-Homies)

### For Account Access
- **Telegram:** [@TestingAccountHomies](https://t.me/TestingAccountHomies)
- **Purpose:** Get 2FA password for shared account

### Support
- **Issues:** [GitHub Issues](https://github.com/abraxas0001/CLI-Tg-Account-Homies/issues)
- **Discussions:** [GitHub Discussions](https://github.com/abraxas0001/CLI-Tg-Account-Homies/discussions)

---

## 🌟 Acknowledgments

### Built With
- **[Telethon](https://github.com/LonamiWebs/Telethon)** - Python Telegram client library
- **[Flask](https://flask.palletsprojects.com/)** - Web framework
- **[Python](https://www.python.org/)** - Programming language

### Inspiration
This project was created to solve real-world problems with:
- Shared Telegram account management
- Cross-platform Telegram access
- Automation and bot development
- Remote system administration

### Contributors
Thanks to everyone who has contributed to this project!

Want to see your name here? [Start contributing!](CONTRIBUTING.md)

---

## 🗺️ Roadmap

### Current Version: 1.0
- ✅ CLI interface with basic commands
- ✅ Web interface with real-time updates
- ✅ 2FA authentication support
- ✅ Session management
- ✅ Message sending/receiving

### Planned Features

**v1.1** (Near Future)
- 📎 Media file sending/receiving
- 🔍 Message search functionality
- 📊 Chat statistics
- 🔔 Desktop notifications

**v1.2** (Future)
- 👥 Group management features
- 🤖 Bot interaction improvements
- 📁 File downloads
- 🌙 Theme customization

**v2.0** (Long Term)
- 🐳 Docker support
- 📱 Mobile-responsive web UI
- 🔐 Enhanced security features
- 🌍 Multi-language support

[Suggest a feature →](https://github.com/abraxas0001/CLI-Tg-Account-Homies/issues/new)

---

## ❓ FAQ

### General Questions

**Q: Is this legal to use?**
> A: Yes! This uses Telegram's official MTProto API. However, follow Telegram's Terms of Service and don't abuse the API.

**Q: Can I use this with multiple accounts?**
> A: Yes! Create different `config.py` files with different `session_name` values for each account.

**Q: Does this work with Telegram bots?**
> A: No, this is for user accounts. For bots, use the official Bot API or BotFather.

**Q: Is my data safe?**
> A: Session files are encrypted by Telethon. Keep them secure and never share them.

### Technical Questions

**Q: Why does it need API credentials?**
> A: Telegram requires API credentials to connect via MTProto protocol. Get them free from my.telegram.org.

**Q: Can I run this on a server?**
> A: Yes! The CLI interface works perfectly on headless servers via SSH.

**Q: What's the difference from official Telegram apps?**
> A: This offers automation capabilities, shared account management, and more control over sessions.

**Q: Can I customize the web interface?**
> A: Yes! The HTML template is in `telegram_web_app.py`. Feel free to modify the CSS and layout.

---

## 📊 Project Stats

[![GitHub Stars](https://img.shields.io/github/stars/abraxas0001/CLI-Tg-Account-Homies?style=social)](https://github.com/abraxas0001/CLI-Tg-Account-Homies/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/abraxas0001/CLI-Tg-Account-Homies?style=social)](https://github.com/abraxas0001/CLI-Tg-Account-Homies/network/members)
[![GitHub Issues](https://img.shields.io/github/issues/abraxas0001/CLI-Tg-Account-Homies)](https://github.com/abraxas0001/CLI-Tg-Account-Homies/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/abraxas0001/CLI-Tg-Account-Homies)](https://github.com/abraxas0001/CLI-Tg-Account-Homies/pulls)

---

<div align="center">

### 💖 Support This Project

If you find this project helpful, please consider:

⭐ **Starring** the repository  
🐛 **Reporting** bugs  
💡 **Suggesting** features  
🔧 **Contributing** code  
📖 **Improving** documentation  

---

**Made with ❤️ by the community**

[⬆ Back to Top](#-cli-tg-account-homies)

</div>
