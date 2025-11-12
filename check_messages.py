"""
Check Messages Tool
View your recent chats and messages
"""

from telethon import TelegramClient
import asyncio

# Configuration - Replace with your values
api_id = 12345678  # Your API ID
api_hash = "your_api_hash_here"  # Your API Hash
session = "my_telegram"  # Session file name

async def check_messages():
    client = TelegramClient(session, api_id, api_hash)
    await client.start()
    
    me = await client.get_me()
    print(f"✅ Logged in as: {me.first_name} (@{me.username})")
    print(f"📱 Phone: {me.phone}")
    print("\n" + "="*70)
    print("CHECKING ALL RECENT CHATS:")
    print("="*70 + "\n")
    
    dialogs = await client.get_dialogs(limit=30)
    for i, dialog in enumerate(dialogs, 1):
        unread = f" ({dialog.unread_count} unread)" if dialog.unread_count > 0 else ""
        print(f"{i}. {dialog.name}{unread}")
        
        # Show last message
        async for message in client.iter_messages(dialog, limit=1):
            sender = await message.get_sender()
            sender_name = getattr(sender, 'first_name', 'Unknown')
            text = message.text[:50] if message.text else '[Media]'
            time = message.date.strftime('%H:%M')
            print(f"   Last: [{time}] {sender_name}: {text}")
    
    print("\n" + "="*70)
    print(f"Total chats: {len(dialogs)}")
    print("="*70)
    
    await client.disconnect()

if __name__ == "__main__":
    asyncio.run(check_messages())
    input("\nPress Enter to exit...")
