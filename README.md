# 📱 Telegram CLI & Web Client

A lightweight, user-friendly Telegram client that works entirely in your terminal or web browser. Built with Python and Telethon.

## ✨ Features

- 🖥️ **CLI Interface** - Full-featured command-line Telegram client
- 🌐 **Web Interface** - Beautiful web UI accessible through your browser
- 🔒 **Secure** - Uses official Telegram API
- 🚀 **Fast & Lightweight** - No heavy desktop client needed
- 📨 **Real-time Messages** - Instant message notifications
- 💬 **Full Chat Support** - Send/receive messages, view chat history

## 🎯 Use Cases

- Access Telegram on servers without GUI
- Lightweight alternative to desktop clients
- Script automation for Telegram
- Monitor messages in real-time
- Use Telegram through SSH sessions

## 📋 Prerequisites

- Python 3.8+
- Telegram account
- Telegram API credentials (api_id and api_hash)

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/telegram-cli-web.git
cd telegram-cli-web
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Get Telegram API Credentials

1. Go to [my.telegram.org](https://my.telegram.org)
2. Login with your phone number
3. Go to "API Development Tools"
4. Create a new application
5. Copy your `api_id` and `api_hash`

### 4. Configure

Edit the configuration in the script files:
- Replace `api_id` with your API ID
- Replace `api_hash` with your API hash
- Replace `session` with your session name

### 5. First Login

Run the login script to authenticate:

```bash
python login.py
```

Enter your phone number and verification code when prompted.

## 🎮 Usage

### CLI Mode

Launch the interactive command-line interface:

```bash
python telegram_desktop_cli.py
```

**Available Commands:**
- `/send <number_or_username> <message>` - Send a message
- `/list` - Show all chats
- `/read <number>` - Read messages from a chat
- `/me` - Show your account info
- `/quit` - Exit

### Web Mode

Launch the web interface:

```bash
python telegram_web_app.py
```

Then open your browser to: `http://localhost:5000`

**Features:**
- View all chats in sidebar
- Click to open any chat
- Send and receive messages in real-time
- Auto-refresh for new messages
- Modern, responsive UI

### Watch Messages

Monitor incoming messages in real-time:

```bash
python watch_messages.py
```

Perfect for receiving verification codes or monitoring specific chats.

### Verify Session

Check if your session is valid:

```bash
python verify_session.py
```

## 📁 Project Structure

```
telegram-cli-web/
├── login.py                    # Initial login script
├── telegram_desktop_cli.py     # CLI interface
├── telegram_web_app.py         # Web interface
├── watch_messages.py           # Real-time message monitor
├── verify_session.py           # Session verification
├── check_messages.py           # Check recent messages
├── requirements.txt            # Python dependencies
├── README.md                   # This file
└── .gitignore                 # Git ignore file
```

## 🔐 Security Notes

- Never share your `api_id`, `api_hash`, or session files
- Session files contain authentication data - keep them private
- Add `*.session` to `.gitignore` (already included)
- Don't commit your API credentials to Git

## 🛠️ Configuration

### API Credentials

In each script file, update these variables:

```python
api_id = YOUR_API_ID
api_hash = "YOUR_API_HASH"
session = "YOUR_SESSION_NAME"
```

### Session Files

- Session files (`.session`) are created automatically on first login
- They store encrypted authentication data
- Keep them secure and never commit to Git

## 📸 Screenshots

### CLI Interface
```
┌─────────────────────────────────────────────┐
│  🚀 TELEGRAM CLI - Logged in as User 🚀     │
├─────────────────────────────────────────────┤
│  #    Name                    Unread        │
│  1    Saved Messages          -             │
│  2    Telegram                5             │
│  3    Friend Name             2             │
└─────────────────────────────────────────────┘
>> /send 2 Hello!
✅ Message sent
```

### Web Interface
Modern, Telegram-like interface with:
- Chat list sidebar
- Message view
- Send message input
- Real-time updates

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This is an unofficial Telegram client. Use at your own risk. Make sure to comply with [Telegram's Terms of Service](https://telegram.org/tos).

## 🐛 Troubleshooting

### "Database is locked" Error
- Another instance is already running
- Close all other Telegram clients using the same session

### Session Expired
- Delete the `.session` file
- Run `python login.py` again

### Can't Receive Messages
- Check your internet connection
- Verify your session with `python verify_session.py`
- Make sure no other client is using the same session

## 📞 Support

If you encounter any issues:
1. Check the [Troubleshooting](#-troubleshooting) section
2. Search existing [GitHub Issues](https://github.com/yourusername/telegram-cli-web/issues)
3. Create a new issue with detailed information

## 🌟 Star History

If you find this project useful, please consider giving it a star ⭐

## 📚 Resources

- [Telethon Documentation](https://docs.telethon.dev/)
- [Telegram API](https://core.telegram.org/api)
- [Python Documentation](https://docs.python.org/)

---

**Made with ❤️ by [Your Name]**
