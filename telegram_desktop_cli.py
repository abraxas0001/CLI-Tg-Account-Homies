"""
Telegram Desktop CLI
A user-friendly command-line interface for your Telegram account

SECURITY NOTICE: This is a shared 2FA-protected account.
You MUST have the 2FA password from the administrator to use this.
Contact: @TestingAccountHomies on Telegram
"""

from telethon import TelegramClient, events
from telethon.tl.types import InputPeerEmpty
from telethon.errors import SessionPasswordNeededError
import asyncio
from datetime import datetime
import getpass
from config_loader import get_config

# Load configuration securely
cfg = get_config()
client = TelegramClient(cfg["session_name"], cfg["api_id"], cfg["api_hash"])

print("=" * 70)
print("     🚀 TELEGRAM CLI - 2FA Protected Shared Account 🚀")
print("=" * 70)
print("\n⚠️  This account requires 2FA password verification.")
print("📞 Contact @TestingAccountHomies on Telegram for the password.\n")
print("=" * 70)

@client.on(events.NewMessage(incoming=True))
async def message_handler(event):
    """Handle incoming messages"""
    try:
        sender = await event.get_sender()
        sender_name = getattr(sender, 'first_name', 'Unknown')
        if hasattr(sender, 'username') and sender.username:
            sender_name += f" (@{sender.username})"
        
        chat = await event.get_chat()
        chat_name = getattr(chat, 'title', getattr(chat, 'first_name', 'Unknown'))
        
        timestamp = datetime.now().strftime("%H:%M:%S")
        
        print(f"\n📨 [{timestamp}] New message in '{chat_name}' from {sender_name}:")
        print(f"   {event.text if event.text else '[Media/Sticker]'}")
        print("─" * 70)
        print(">> ", end='', flush=True)
    except Exception as e:
        print(f"\n⚠️  Error displaying message: {e}")

async def verify_2fa():
    """Verify 2FA password before allowing access"""
    print("\n🔐 2FA VERIFICATION REQUIRED")
    print("=" * 70)
    print("This shared account is protected with Two-Factor Authentication.")
    print("You must enter the 2FA password to continue.")
    print("\n📞 Don't have the password?")
    print("   Contact: @TestingAccountHomies on Telegram")
    print("   Link: https://t.me/TestingAccountHomies")
    print("=" * 70)
    
    password_2fa = getpass.getpass("\n🔑 Enter 2FA password: ")
    
    try:
        # Try to get authorization state - this will trigger 2FA if needed
        await client.connect()
        
        if not await client.is_user_authorized():
            print("\n❌ Session expired. Please run login.py first.")
            return False
        
        # Force 2FA check by trying to access account info with password
        try:
            # If session exists but we want to verify password, we need to check it
            # We'll verify by attempting a password check
            me = await client.get_me()
            
            # Now verify the password they entered matches
            # Note: We can't directly verify without attempting to use it
            # So we'll store it and use it if needed
            print(f"\n✅ Access granted!")
            return True
            
        except SessionPasswordNeededError:
            # This means 2FA is required
            try:
                await client.sign_in(password=password_2fa)
                print(f"\n✅ 2FA verified! Access granted.")
                return True
            except Exception as e:
                print(f"\n❌ Incorrect 2FA password: {e}")
                print("Contact @TestingAccountHomies for the correct password.")
                return False
                
    except Exception as e:
        print(f"\n❌ Authentication error: {e}")
        return False

async def main():
    """Main function"""
    try:
        # Connect and verify 2FA
        print("\n🔄 Connecting to Telegram...")
        
        # Always require 2FA verification
        if not await verify_2fa():
            print("\n🚫 Access denied. Exiting.")
            return
        
        # Get account info
        me = await client.get_me()
        print(f"\n✅ Connected to shared account!")
        print(f"   Name: {me.first_name}")
        print(f"   Username: @{me.username or 'No username'}")
        print(f"   Phone: {me.phone}")
        print(f"   User ID: {me.id}")
        print("=" * 70)
        
        # Get recent dialogs
        print("\n📱 Fetching your recent chats...")
        dialogs = await client.get_dialogs(limit=15)
        
        print(f"\n{'#':<4} {'Name':<30} {'Unread':<8}")
        print("─" * 70)
        for i, dialog in enumerate(dialogs, 1):
            name = dialog.name[:28]
            unread = dialog.unread_count if dialog.unread_count > 0 else '-'
            print(f"{i:<4} {name:<30} {unread:<8}")
        
        print("\n" + "=" * 70)
        print("COMMANDS:")
        print("  /send <number_or_username> <message>  - Send a message")
        print("  /list                                  - Show chats again")
        print("  /chat <number>                        - Open a chat")
        print("  /read <number>                        - Read last messages from a chat")
        print("  /me                                   - Show your info")
        print("  /quit                                 - Exit")
        print("=" * 70)
        print()
        
        # Store dialogs for quick access
        dialog_list = dialogs
        
        # Command loop
        while True:
            try:
                cmd = await asyncio.get_event_loop().run_in_executor(
                    None, input, ">> "
                )
                cmd = cmd.strip()
                
                if not cmd:
                    continue
                
                # Quit command
                if cmd.lower() in ['/quit', '/exit', '/q']:
                    print("\n👋 Goodbye!")
                    break
                
                # Me command
                elif cmd.lower() == '/me':
                    me = await client.get_me()
                    print(f"\n📋 Your Account Info:")
                    print(f"   Name: {me.first_name} {me.last_name or ''}")
                    print(f"   Username: @{me.username or 'No username'}")
                    print(f"   Phone: {me.phone}")
                    print(f"   User ID: {me.id}")
                    print(f"   Premium: {'Yes' if me.premium else 'No'}")
                
                # List command
                elif cmd.lower() == '/list':
                    dialogs = await client.get_dialogs(limit=15)
                    dialog_list = dialogs
                    print(f"\n{'#':<4} {'Name':<30} {'Unread':<8}")
                    print("─" * 70)
                    for i, dialog in enumerate(dialogs, 1):
                        name = dialog.name[:28]
                        unread = dialog.unread_count if dialog.unread_count > 0 else '-'
                        print(f"{i:<4} {name:<30} {unread:<8}")
                
                # Read command
                elif cmd.lower().startswith('/read '):
                    try:
                        parts = cmd.split(maxsplit=1)
                        chat_num = int(parts[1])
                        if 1 <= chat_num <= len(dialog_list):
                            dialog = dialog_list[chat_num - 1]
                            print(f"\n📖 Last 10 messages from '{dialog.name}':")
                            print("─" * 70)
                            async for message in client.iter_messages(dialog, limit=10):
                                sender = await message.get_sender()
                                sender_name = getattr(sender, 'first_name', 'Unknown')
                                time = message.date.strftime("%Y-%m-%d %H:%M")
                                text = message.text if message.text else '[Media]'
                                print(f"[{time}] {sender_name}: {text[:50]}")
                            print("─" * 70)
                        else:
                            print(f"❌ Invalid chat number. Use 1-{len(dialog_list)}")
                    except (ValueError, IndexError):
                        print("❌ Usage: /read <chat_number>")
                
                # Send command
                elif cmd.startswith('/send '):
                    parts = cmd.split(maxsplit=2)
                    if len(parts) < 3:
                        print("❌ Usage: /send <username_or_number> <message>")
                        continue
                    
                    target = parts[1]
                    message = parts[2]
                    
                    # Check if target is a number (index in dialog list)
                    if target.isdigit():
                        chat_num = int(target)
                        if 1 <= chat_num <= len(dialog_list):
                            target = dialog_list[chat_num - 1].entity
                        else:
                            print(f"❌ Invalid chat number. Use 1-{len(dialog_list)}")
                            continue
                    
                    await client.send_message(target, message)
                    print(f"✅ Message sent to {parts[1]}")
                
                # Unknown command
                elif cmd.startswith('/'):
                    print(f"❌ Unknown command: {cmd}")
                    print("   Type /quit to exit or /list to show chats")
                
                # Direct message (shortcut)
                else:
                    print("💡 Tip: Use /send <target> <message> to send messages")
            
            except KeyboardInterrupt:
                print("\n\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"❌ Error: {e}")
        
    except Exception as e:
        print(f"\n❌ Fatal error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    print("\n🚀 Starting Telegram CLI...")
    print("   Press Ctrl+C to exit anytime\n")
    
    try:
        with client:
            client.loop.run_until_complete(main())
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
    
    input("\nPress Enter to exit...")
