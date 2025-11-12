"""
Telegram Login Script
First-time setup to authenticate your Telegram account
"""

from telethon import TelegramClient
import asyncio

# Configuration - Replace with your values
api_id = 12345678  # Your API ID from my.telegram.org
api_hash = "your_api_hash_here"  # Your API Hash
session_file = "my_telegram"  # Session file name

print("Connecting...")

client = TelegramClient(session_file, api_id, api_hash)

async def main():
    await client.start()
    
    me = await client.get_me()
    print(f"\nLOGGED IN: {me.first_name} (@{me.username or 'no username'})")
    print(f"Phone: {me.phone}")
    print(f"\n✅ Session saved as: {session_file}.session")
    print("You can now use the CLI or Web interface!")

with client:
    client.loop.run_until_complete(main())

input("\nPress Enter to exit...")