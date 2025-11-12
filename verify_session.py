"""
Session Verification Tool
Check if your Telegram session is valid and working
"""

from telethon import TelegramClient
import asyncio

# Configuration - Replace with your values
api_id = 12345678  # Your API ID
api_hash = "your_api_hash_here"  # Your API Hash
session_file = "my_telegram"  # Session file name

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
            print("  • AyuGram desktop application")
            print("  • Python scripts (telegram_cli.py)")
            print("  • Any Telegram client that supports session files")
            
        else:
            print("✗ Session is NOT authorized.")
            print("\n[2] Starting login process...")
            
            # Send code request
            await client.send_code_request(phone)
            print(f"Code sent to {phone}")
            
            code = input("Enter the code you received: ")
            
            try:
                # Try to sign in
                await client.sign_in(phone, code)
            except Exception as e:
                if "Two-steps verification" in str(e) or "password" in str(e).lower():
                    print(f"\n2FA is enabled. Using password: {twoFA}")
                    await client.sign_in(password=twoFA)
                else:
                    raise e
            
            me = await client.get_me()
            print(f"\n✓ Successfully logged in as: {me.first_name}")
            print(f"Session saved to: {session_file}.session")
        
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
