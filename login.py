"""
Telegram Login Script
First-time setup to authenticate your Telegram account

IMPORTANT: This account is protected with 2FA (Two-Factor Authentication).
Contact the account administrator to get the 2FA password before proceeding.
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

print("=" * 70)
print("     TELEGRAM LOGIN - 2FA PROTECTED ACCOUNT")
print("=" * 70)
print("\n⚠️  This account requires 2FA password for login.")
print("📞 Contact the administrator to get the 2FA password.\n")
print("=" * 70)

client = TelegramClient(session_file, api_id, api_hash)

async def main():
    try:
        print("\n[1] Connecting to Telegram...")
        await client.connect()
        
        # Check if already authorized
        if await client.is_user_authorized():
            me = await client.get_me()
            print("\n✅ Already logged in!")
            print(f"   Name: {me.first_name}")
            print(f"   Username: @{me.username or 'No username'}")
            print(f"   Phone: {me.phone}")
            print("\nYou can now use the CLI or Web interface!")
        else:
            # Not authorized, need to login
            print("\n[2] Starting login process...")
            
            # Get phone number
            phone = input("\nEnter phone number (with country code, e.g., +1234567890): ").strip()
            
            # Send verification code
            await client.send_code_request(phone)
            print(f"\n📱 Verification code sent to {phone}")
            
            # Get verification code
            code = input("Enter the verification code: ").strip()
            
            try:
                # Try to sign in with code
                await client.sign_in(phone, code)
                print("\n✅ Logged in successfully!")
            except SessionPasswordNeededError:
                # 2FA is enabled, need password
                print("\n🔐 Two-Factor Authentication is enabled.")
                print("⚠️  You MUST have the 2FA password to proceed.")
                print("📞 Contact the account administrator if you don't have it.\n")
                
                # Prompt for 2FA password (hidden input)
                password_2fa = getpass.getpass("Enter 2FA password: ")
                
                try:
                    await client.sign_in(password=password_2fa)
                    print("\n✅ Logged in successfully with 2FA!")
                except Exception as e:
                    print(f"\n❌ 2FA password incorrect or error: {e}")
                    print("Contact the administrator for the correct password.")
                    return
            
            # Get account info after successful login
            me = await client.get_me()
            print(f"\n╔══════════════════════════════════════════════════════╗")
            print(f"║           LOGIN SUCCESSFUL!                           ║")
            print(f"╚══════════════════════════════════════════════════════╝")
            print(f"  Name: {me.first_name} {me.last_name or ''}")
            print(f"  Username: @{me.username or 'No username'}")
            print(f"  Phone: {me.phone}")
            print(f"  User ID: {me.id}")
            print(f"\n✅ Session saved as: {session_file}.session")
            print("\n⚠️  SECURITY NOTICE:")
            print("  - The administrator can monitor your activity")
            print("  - The administrator may change the password at any time")
            print("  - Do not attempt to terminate other active sessions")
            print("\nYou can now use the CLI or Web interface!")
    
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
    
    finally:
        await client.disconnect()

with client:
    client.loop.run_until_complete(main())

input("\nPress Enter to exit...")