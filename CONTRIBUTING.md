# Contributing to Telegram CLI & Web Client

First off, thank you for considering contributing! 🎉

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Pull Request Process](#pull-request-process)
- [Style Guidelines](#style-guidelines)

## Code of Conduct

- Be respectful and inclusive
- Welcome newcomers and help them learn
- Focus on what is best for the community
- Show empathy towards others

## How Can I Contribute?

### 🐛 Reporting Bugs

Before creating bug reports, please check existing issues. When creating a bug report, include:

- **Clear title and description**
- **Steps to reproduce**
- **Expected vs actual behavior**
- **Screenshots** (if applicable)
- **System information** (OS, Python version)

### 💡 Suggesting Features

Feature requests are welcome! Please provide:

- **Clear use case**
- **Why this feature would be useful**
- **Possible implementation approach**

### 🔧 Code Contributions

1. Fork the repository
2. Create your feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## Development Setup

```bash
# Clone your fork
git clone https://github.com/yourusername/telegram-cli-web.git
cd telegram-cli-web

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up your Telegram credentials
# Edit config files with your API credentials
```

## Pull Request Process

1. **Update documentation** if needed
2. **Add tests** for new features
3. **Follow code style** (see below)
4. **Update README.md** with details of changes
5. **Ensure all tests pass**
6. **Request review** from maintainers

### PR Checklist

- [ ] Code follows style guidelines
- [ ] Self-reviewed the code
- [ ] Commented complex code sections
- [ ] Updated documentation
- [ ] No new warnings generated
- [ ] Added tests (if applicable)
- [ ] All tests passing

## Style Guidelines

### Python Code Style

- Follow [PEP 8](https://pep8.org/)
- Use meaningful variable names
- Add docstrings to functions
- Keep functions small and focused
- Maximum line length: 88 characters

### Example:

```python
def send_message(client, recipient, text):
    """
    Send a message to a Telegram user or chat.
    
    Args:
        client: TelegramClient instance
        recipient: Username or chat ID
        text: Message text to send
        
    Returns:
        bool: True if sent successfully
    """
    try:
        client.send_message(recipient, text)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
```

### Commit Messages

- Use present tense ("Add feature" not "Added feature")
- Use imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit first line to 72 characters
- Reference issues and pull requests

Example:
```
Add real-time message sync feature

- Implement WebSocket connection
- Add message queue system
- Update UI on new messages

Fixes #123
```

## Feature Ideas

Here are some ideas for contributions:

- [ ] Add support for sending media files
- [ ] Implement group chat management
- [ ] Add emoji support in CLI
- [ ] Create configuration file system
- [ ] Add message search functionality
- [ ] Implement chat archiving
- [ ] Add desktop notifications
- [ ] Create Docker container
- [ ] Add message encryption visualization
- [ ] Implement bot interaction features

## Questions?

Feel free to open an issue with the `question` label!

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing! 🙌
