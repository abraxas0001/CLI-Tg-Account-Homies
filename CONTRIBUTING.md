# Contributing to CLI-Tg-Account-Homies

First off, thank you for considering contributing! 🎉

---

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Pull Request Process](#pull-request-process)
- [Style Guidelines](#style-guidelines)
- [Feature Ideas](#feature-ideas)

---

## 🤝 Code of Conduct

By participating in this project, you agree to:

- ✅ Be respectful and inclusive
- ✅ Welcome newcomers and help them learn
- ✅ Focus on what is best for the community
- ✅ Show empathy towards others
- ✅ Accept constructive criticism gracefully

---

## 💡 How Can I Contribute?

### 🐛 Reporting Bugs

Before creating bug reports, please check existing issues to avoid duplicates.

**When reporting bugs, include:**

- ✅ **Clear title and description**
- ✅ **Steps to reproduce** the issue
- ✅ **Expected behavior** vs **actual behavior**
- ✅ **Screenshots** (if applicable)
- ✅ **System information:**
  - Operating System (Windows/Mac/Linux)
  - Python version (`python --version`)
  - Telethon version (`pip show telethon`)

**Example Bug Report:**
```markdown
## Bug: CLI crashes when sending long messages

**Expected:** Message should be sent successfully
**Actual:** Application crashes with error

**Steps to reproduce:**
1. Run `python telegram_desktop_cli.py`
2. Use command `/send 1 [very long message over 4096 characters]`
3. Application crashes

**System Info:**
- OS: Windows 11
- Python: 3.11.5
- Telethon: 1.35.0

**Error message:**
[Paste error traceback here]
```

---

### 🌟 Suggesting Features

Feature requests are welcome! Please provide:

- ✅ **Clear use case** - What problem does this solve?
- ✅ **Why this feature would be useful** - Who benefits?
- ✅ **Possible implementation approach** - How could it work?
- ✅ **Examples** - Similar features in other apps?

**Example Feature Request:**
```markdown
## Feature: Add support for voice messages

**Use case:** Users want to send voice messages from CLI

**Benefits:** 
- More natural communication
- Accessibility for users who prefer voice

**Implementation idea:**
- Add `/voice <number> <file.ogg>` command
- Use Telethon's `send_file()` with voice attribute

**Examples:**
- Telegram Desktop has voice message support
- WhatsApp CLI tools like `whatsapp-cli` support voice
```

---

### 🔧 Code Contributions

We love code contributions! Here's how:

1. **Fork** the repository
2. **Create** your feature branch (`git checkout -b feature/AmazingFeature`)
3. **Make** your changes
4. **Test** thoroughly
5. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
6. **Push** to the branch (`git push origin feature/AmazingFeature`)
7. **Open** a Pull Request

---

## 🛠️ Development Setup

### Prerequisites:
- Python 3.8 or higher
- Git
- Telegram account (for testing)

### Setup Steps:

```bash
# 1. Fork and clone your fork
git clone https://github.com/YOUR_USERNAME/CLI-Tg-Account-Homies.git
cd CLI-Tg-Account-Homies

# 2. Create virtual environment
python -m venv venv

# Activate on Windows:
venv\Scripts\activate

# Activate on Mac/Linux:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create your config file
copy config.example.py config.py

# 5. Add your Telegram API credentials to config.py
# Get them from https://my.telegram.org

# 6. Test the application
python telegram_desktop_cli.py
```

---

## 🔄 Pull Request Process

### Before Submitting:

- [ ] ✅ Code follows style guidelines (see below)
- [ ] ✅ Self-reviewed the code
- [ ] ✅ Commented complex code sections
- [ ] ✅ Updated documentation (README.md if needed)
- [ ] ✅ No new warnings or errors
- [ ] ✅ Added tests (if applicable)
- [ ] ✅ All existing tests pass
- [ ] ✅ Tested on at least one platform

### PR Description Template:

```markdown
## Description
Brief description of what this PR does

## Type of Change
- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update

## Testing
Describe how you tested your changes

## Screenshots (if applicable)
Add screenshots to demonstrate changes

## Checklist
- [ ] My code follows the style guidelines
- [ ] I have commented my code
- [ ] I have updated the documentation
- [ ] My changes generate no new warnings
- [ ] I have tested this on [OS name]
```

### Review Process:

1. Maintainer will review within 1-3 days
2. Address any requested changes
3. Once approved, maintainer will merge
4. Your contribution will be credited!

---

## 📐 Style Guidelines

### Python Code Style

Follow **PEP 8** with these specifics:

- ✅ **Line length:** Maximum 88 characters (Black formatter standard)
- ✅ **Indentation:** 4 spaces (no tabs)
- ✅ **Imports:** Grouped and sorted (standard lib, third-party, local)
- ✅ **Naming:**
  - `snake_case` for functions and variables
  - `PascalCase` for classes
  - `UPPER_CASE` for constants
- ✅ **Docstrings:** Use for all public functions and classes

**Example:**

```python
"""
Module description goes here.
"""

import asyncio
import sys
from datetime import datetime

from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError

from config_loader import get_config


async def send_message_to_chat(client, chat_id, message_text):
    """
    Send a message to a Telegram chat.

    Args:
        client (TelegramClient): Active Telegram client instance
        chat_id (int|str): Chat ID or username
        message_text (str): Text content to send

    Returns:
        bool: True if message sent successfully, False otherwise

    Raises:
        ValueError: If message_text is empty
        RuntimeError: If client is not connected

    Example:
        >>> await send_message_to_chat(client, 123456, "Hello!")
        True
    """
    if not message_text:
        raise ValueError("Message text cannot be empty")
    
    if not client.is_connected():
        raise RuntimeError("Client is not connected")
    
    try:
        await client.send_message(chat_id, message_text)
        print(f"✅ Message sent to {chat_id}")
        return True
    except Exception as e:
        print(f"❌ Error sending message: {e}")
        return False
```

---

### Commit Message Guidelines

Use **Conventional Commits** format:

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation only
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding tests
- `chore`: Maintenance tasks

**Examples:**

```bash
# Good commit messages:
git commit -m "feat(cli): add support for media files in /send command"
git commit -m "fix(web): resolve UI crash when chat list is empty"
git commit -m "docs: update installation instructions for macOS"
git commit -m "refactor(config): simplify config loading logic"

# Bad commit messages:
git commit -m "fix stuff"
git commit -m "update"
git commit -m "asdfasdf"
```

**Detailed example:**
```
feat(cli): add support for sending voice messages

- Implement /voice command
- Add audio file validation
- Update help text with new command
- Add error handling for invalid files

Closes #42
```

---

## 💡 Feature Ideas

Here are some ideas if you're looking for something to work on:

### High Priority:
- [ ] 📎 **Add support for sending media files** (images, videos, documents)
- [ ] 🔍 **Implement message search functionality**
- [ ] 🔔 **Add desktop notifications for new messages**
- [ ] 📁 **Create file download feature from chats**
- [ ] 🗃️ **Implement chat archiving and backup**

### Medium Priority:
- [ ] 😀 **Add emoji support in CLI** (emoji picker or autocomplete)
- [ ] 👥 **Implement group chat management** (add/remove users, etc.)
- [ ] 🤖 **Add bot interaction features** (inline keyboards, callbacks)
- [ ] 🎨 **Improve CLI UI** (colors, better formatting)
- [ ] ⚙️ **Add configuration file for user preferences**

### Nice to Have:
- [ ] 🐳 **Create Docker container** for easy deployment
- [ ] 📱 **Add QR code login** option
- [ ] 🔐 **Implement message encryption visualization**
- [ ] 📊 **Add chat statistics** (message count, active times)
- [ ] 🌙 **Add theme support** (dark/light mode for web UI)

**Want to work on something else?** Open an issue to discuss!

---

## 🧪 Testing

### Manual Testing:

Before submitting a PR, please test:

1. **Login flow:**
   ```bash
   python login.py
   ```
   - Test with correct credentials
   - Test with incorrect 2FA password
   - Verify session file is created

2. **CLI interface:**
   ```bash
   python telegram_desktop_cli.py
   ```
   - Test all commands (`/list`, `/read`, `/send`, `/me`, `/quit`)
   - Test with invalid inputs
   - Test with edge cases (empty chat list, etc.)

3. **Web interface:**
   ```bash
   python telegram_web_app.py
   ```
   - Test chat loading
   - Test message sending
   - Test UI responsiveness

### Automated Testing (future):

We're planning to add:
- Unit tests with `pytest`
- Integration tests
- CI/CD with GitHub Actions

Want to help set this up? Open an issue!

---

## 📝 Documentation

### Updating README:

If your changes require documentation updates:

- ✅ Update relevant sections in README.md
- ✅ Add examples for new features
- ✅ Update screenshots if UI changed
- ✅ Keep language clear and beginner-friendly

### Code Comments:

- ✅ Comment complex logic
- ✅ Explain "why" not "what" (code shows what)
- ✅ Update comments if code changes
- ❌ Don't over-comment obvious code

**Good comments:**
```python
# Use Colombian number to bypass geo-restrictions
phone_number = "+573135316429"

# Retry up to 3 times for network reliability
for attempt in range(3):
    try:
        await client.connect()
        break
    except ConnectionError:
        if attempt == 2:
            raise
        await asyncio.sleep(2)
```

**Bad comments:**
```python
# Set phone number
phone_number = "+573135316429"  # This is obvious

# Loop 3 times
for i in range(3):  # Comments should explain WHY
```

---

## ❓ Questions?

- 💬 Open a [GitHub Issue](https://github.com/abraxas0001/CLI-Tg-Account-Homies/issues) with `question` label
- 📧 Contact: [@TestingAccountHomies](https://t.me/TestingAccountHomies) on Telegram
- 📖 Check [README.md](README.md) for general information

---

## 🙏 Thank You!

Every contribution, no matter how small, makes a difference:

- ⭐ **Stars** help the project gain visibility
- 🐛 **Bug reports** help improve quality
- 💡 **Feature suggestions** guide development
- 🔧 **Code contributions** add functionality
- 📖 **Documentation** helps users

**By contributing, you agree that your contributions will be licensed under the MIT License.**

---

<div align="center">

### 🌟 Contributors

Thank you to everyone who has contributed to this project!

[![Contributors](https://img.shields.io/github/contributors/abraxas0001/CLI-Tg-Account-Homies?style=for-the-badge)](https://github.com/abraxas0001/CLI-Tg-Account-Homies/graphs/contributors)

**Want to see your name here? Start contributing today!** 🚀

</div>
