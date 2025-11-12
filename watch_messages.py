"""
Real-time Message Monitor
Watch for incoming messages in real-time
"""

from telethon import TelegramClient, events
import asyncio

# Configuration - Replace with your values
api_id = 12345678  # Your API ID
api_hash = "your_api_hash_here"  # Your API Hash
session = "my_telegram"  # Session file name

client = TelegramClient(session, api_id, api_hash)

print("=" * 70)
print("     REAL-TIME MESSAGE MONITOR - Watch for Login Code")
print("=" * 70)
print()
print("This will show you ALL incoming messages in real-time.")
print("Perfect for getting the verification code from Telegram!")
print()
print("=" * 70)
print()

@client.on(events.NewMessage(incoming=True))
async def handler(event):
    """Show all incoming messages"""
    try:
        sender = await event.get_sender()
        sender_name = getattr(sender, 'first_name', 'Unknown')
        if hasattr(sender, 'username') and sender.username:
            sender_name += f" (@{sender.username})"
        
        chat = await event.get_chat()
        chat_name = getattr(chat, 'title', getattr(chat, 'first_name', 'Unknown'))
        
        print("\n" + "="*70)
        print(f"📨 NEW MESSAGE from: {sender_name}")
        print(f"   In chat: {chat_name}")
        print("─"*70)
        if event.text:
            print(f"   {event.text}")
        else:
            print("   [Media/Sticker/File]")
        print("="*70)
    except Exception as e:
        print(f"\n⚠️ Error: {e}")

async def main():
    await client.start()
    
    me = await client.get_me()
    print(f"✅ Logged in as: {me.first_name} (@{me.username or 'no username'})")
    print(f"   Phone: {me.phone}")
    print()
    print("=" * 70)
    print("🔔 MONITORING ALL INCOMING MESSAGES...")
    print("=" * 70)
    print()
    print("NOW START THE LOGIN PROCESS IN AYUGRAM:")
    print("1. Open AyuGram")
    print("2. Enter phone: +573135316429")
    print("3. Click 'Next'")
    print("4. Wait for the code to appear HERE")
    print("5. Enter the code in AyuGram")
    print()
    print("Waiting for messages...")
    print("Press Ctrl+C to stop")
    print()
    
    # Keep the client running
    await client.run_until_disconnected()

if __name__ == "__main__":
    try:
        with client:
            client.loop.run_until_complete(main())
    except KeyboardInterrupt:
        print("\n\n👋 Stopped monitoring")
