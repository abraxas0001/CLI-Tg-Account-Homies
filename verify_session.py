"""
Session Verification Tool
Check if your Telegram session is valid and working

For 2FA-protected accounts: You'll need the 2FA password to login.
Contact the account administrator if you don't have it.
"""

from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
import asyncio
import getpass
from config_loader import get_config

# Load configuration securely
cfg = get_config()
api_id = cfg["api_id"]
api_hash = cfg["api_hash"]
session_file = cfg["session_name"]

print("=" * 60)
print("TELEGRAM SESSION VERIFICATION & LOGIN")
print("=" * 60)
print(f"Session file: {session_file}")
print("=" * 60)

async def main():
    # Create client
    client = TelegramClient(session_file, api_id, api_hash)
    
    try:
        print("\n[1] Connecting to Telegram...")
        await client.connect()
        
        # Check if already authorized
        if await client.is_user_authorized():
            print("✓ Session is VALID and AUTHORIZED!")
            me = await client.get_me()
            print(f"\n╔══════════════════════════════════════════════════════╗")
            print(f"║  LOGGED IN SUCCESSFULLY!                              ║")
            print(f"╚══════════════════════════════════════════════════════╝")
            print(f"  Name: {me.first_name} {me.last_name or ''}")
            print(f"  Username: @{me.username or 'No username'}")
            print(f"  Phone: {me.phone}")
            print(f"  User ID: {me.id}")
            print(f"  Premium: {me.premium}")
            print("=" * 60)
            
            # Get dialogs (chats)
            print("\n[2] Fetching recent chats...")
            dialogs = await client.get_dialogs(limit=5)
            print(f"Found {len(dialogs)} recent chats:")
            for i, dialog in enumerate(dialogs, 1):
                print(f"  {i}. {dialog.name}")
            
            print("\n✓ Session is working perfectly!")
            print("\nYou can now use this account with:")
            print("  • Python CLI (telegram_desktop_cli.py)")
            print("  • Web interface (telegram_web_app.py)")
            print("  • AyuGram desktop application")
            
        else:
            print("✗ Session is NOT authorized.")
            print("\n[2] Starting login process...")
            print("⚠️  This account is 2FA protected.")
            print("📞 Contact the administrator for the 2FA password.\n")
            
            # Get phone number
            phone = input("Enter phone number (with country code): ").strip()
            
            # Send code request
            await client.send_code_request(phone)
            print(f"\n📱 Code sent to {phone}")
            
            code = input("Enter the verification code: ").strip()
            
            try:
                # Try to sign in
                await client.sign_in(phone, code)
            except SessionPasswordNeededError:
                print("\n🔐 2FA is enabled. Password required.")
                print("⚠️  Contact the administrator if you don't have it.\n")
                
                # Prompt for 2FA password (hidden input)
                password_2fa = getpass.getpass("Enter 2FA password: ")
                
                try:
                    await client.sign_in(password=password_2fa)
                except Exception as e:
                    print(f"\n❌ 2FA password incorrect: {e}")
                    print("Contact the administrator for the correct password.")
                    return
            
            me = await client.get_me()
            print(f"\n✓ Successfully logged in as: {me.first_name}")
            print(f"Session saved to: {session_file}.session")
            print("\n⚠️  SECURITY NOTICE:")
            print("  - Administrator can monitor your activity")
            print("  - Administrator may change password anytime")
        
    except Exception as e:
        print(f"\n✗ Error: {e}")
        import traceback
        traceback.print_exc()
    
    finally:
        await client.disconnect()
        print("\n[✓] Disconnected.")

if __name__ == "__main__":
    asyncio.run(main())
    input("\nPress Enter to exit...")
