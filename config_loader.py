"""
Configuration Loader
Loads Telegram API configuration from config.py file
"""

def get_config():
    """
    Load configuration from config.py
    Returns a dictionary with api_id, api_hash, session_name, etc.
    """
    try:
        # Try to import from config.py
        import config
        
        return {
            "api_id": getattr(config, 'api_id', None),
            "api_hash": getattr(config, 'api_hash', None),
            "session_name": getattr(config, 'session_name', 'telegram_session'),
            "phone_number": getattr(config, 'phone_number', ''),
            "password_2fa": getattr(config, 'password_2fa', '')
        }
    except ImportError:
        print("\n❌ Error: config.py not found!")
        print("\n📋 Please create config.py with your settings:")
        print("   1. Copy config.example.py to config.py")
        print("   2. Edit config.py with your API credentials")
        print("\nExample:")
        print("   api_id = 12345678")
        print("   api_hash = 'your_api_hash'")
        print("   session_name = 'my_session'")
        print("\nGet API credentials from: https://my.telegram.org\n")
        raise SystemExit(1)
