# 🚀 Quick Setup Guide

## ⚠️ BEFORE YOU START

**This account is 2FA-protected for shared public use.**

1. **Contact the administrator** to get the 2FA password
2. **Do not attempt** to change account settings or terminate sessions
3. **Administrator monitors** all activity
4. **Access can be revoked** at any time

---

## Step 1: Get 2FA Password from Administrator

**You cannot proceed without this!**

Contact the account owner and request:
- 2FA password (required for login)
- Phone number (needed for first login)

## Step 2: Get Telegram API Credentials

1. Visit [my.telegram.org](https://my.telegram.org)
2. Login with your Telegram phone number
3. Go to "API Development Tools"
4. Fill in the application details:
   - App title: `My Telegram CLI`
   - Short name: `telegram_cli`
   - Platform: `Desktop`
5. Click "Create Application"
6. Save your `api_id` and `api_hash`

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 3: Configure (without exposing credentials)

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

## Step 4: First Login

```bash
python login.py
```

**Follow the prompts:**
1. Enter phone number (provided by admin)
2. Enter verification code from Telegram
3. **Enter 2FA password** (the one admin gave you)

The script will securely prompt for the 2FA password without storing it.

## Step 5: Start Using!

### CLI Mode:
```bash
python telegram_desktop_cli.py
```

### Web Mode:
```bash
python telegram_web_app.py
```
Then open: http://localhost:5000

---

## ⚠️ Usage Rules

**Allowed:**
- ✅ Read and send messages
- ✅ Use CLI or Web interface
- ✅ Monitor incoming messages

**Forbidden:**
- ❌ Change account settings
- ❌ Terminate other sessions
- ❌ Attempt to change password
- ❌ Export account data

**Violation = immediate access revocation**
Then open: http://localhost:5000

## 🔧 Troubleshooting

### "No module named 'telethon'"
```bash
pip install telethon
```

### "Invalid API ID/Hash"
- Double-check your API credentials from my.telegram.org
- Make sure they're copied correctly (no extra spaces)

### "Phone number already registered"
- This is normal! Continue with the verification code

### Session Issues
- Delete the `.session` file and run `login.py` again

## 📝 Notes

- Session files are saved as `<session_name>.session`
- Keep your session files secure (they contain auth data)
- Don't share your API credentials or session files
- You can use the same session across multiple scripts

## 🎯 What to Do After Setup

1. **Test CLI**: Run `python telegram_desktop_cli.py`
2. **Try Web UI**: Run `python telegram_web_app.py`
3. **Monitor Messages**: Run `python watch_messages.py`
4. **Check Status**: Run `python verify_session.py`

Enjoy! 🎉
