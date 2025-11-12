"""
Telegram Desktop CLI
A user-friendly command-line interface for your Telegram account
"""

from telethon import TelegramClient, events
from telethon.tl.types import InputPeerEmpty
import asyncio
from datetime import datetime

# Configuration - Replace with your values
api_id = 12345678  # Your API ID from my.telegram.org
api_hash = "your_api_hash_here"  # Your API Hash
session = "my_telegram"  # Session file name

client = TelegramClient(session, api_id, api_hash)

print("=" * 70)
print("          🚀 TELEGRAM CLI - Logged in as Janice 🚀")
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

async def main():
    """Main function"""
    try:
        # Connect
        print("\n🔄 Connecting to Telegram...")
        await client.start()
        
        # Get account info
        me = await client.get_me()
        print(f"✅ Logged in as: {me.first_name}")
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
