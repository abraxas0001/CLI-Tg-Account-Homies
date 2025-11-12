"""
Simple Telegram CLI
Basic command-line interface for sending/receiving messages
"""

from telethon import TelegramClient, events
import asyncio

# Configuration - Replace with your values
api_id = 12345678  # Your API ID
api_hash = "your_api_hash_here"  # Your API Hash
session = "my_telegram"  # Session file name

client = TelegramClient(session, api_id, api_hash)

@client.on(events.NewMessage(incoming=True))
async def handler(event):
    print(f"\nNew message from {event.sender_id}: {event.text}")

async def main():
    me = await client.get_me()
    print("Logged in as:", me.first_name, "@"+(me.username or "—"))
    print("Type '/quit' to exit.")
    while True:
        cmd = input(">> ")
        if cmd.strip() == "/quit":
            break
        if cmd.startswith("/send "):
            parts = cmd.split(" ", 2)
            if len(parts) < 3:
                print("Usage: /send <username_or_id> <message>")
                continue
            target, msg = parts[1], parts[2]
            await client.send_message(target, msg)
            print("Sent.")
        else:
            print("Commands: /send <user_or_id> <message>, /quit")

with client:
    client.loop.run_until_complete(main())
