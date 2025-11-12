# 🚀 Quick Setup Guide

## Step 1: Get Telegram API Credentials

1. Visit [my.telegram.org](https://my.telegram.org)
2. Login with your Telegram phone number
3. Go to "API Development Tools"
4. Fill in the application details:
   - App title: `My Telegram CLI`
   - Short name: `telegram_cli`
   - Platform: `Desktop`
5. Click "Create Application"
6. Save your `api_id` and `api_hash`

## Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 3: Configure

Edit each Python file and replace:
```python
api_id = 12345678  # Replace with your API ID
api_hash = "your_api_hash_here"  # Replace with your API Hash
session = "my_telegram"  # Choose a session name
```

## Step 4: First Login

```bash
python login.py
```

Enter:
- Your phone number (with country code, e.g., +1234567890)
- Verification code from Telegram
- 2FA password (if enabled)

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
