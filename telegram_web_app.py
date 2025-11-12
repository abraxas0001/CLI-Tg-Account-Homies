"""
Telegram Web Interface - Use your account in a web browser!
This creates a local web server that gives you a full Telegram interface.

SECURITY NOTICE: This is a shared 2FA-protected account.
You MUST have the 2FA password from the administrator to use this.
Contact: @TestingAccountHomies on Telegram
"""

from telethon import TelegramClient, events
from telethon.tl.types import PeerUser, PeerChat, PeerChannel
from telethon.errors import SessionPasswordNeededError
import asyncio
from flask import Flask, render_template_string, request, jsonify
import threading
import webbrowser
from datetime import datetime
import getpass
from config_loader import get_config

# Load configuration securely
cfg = get_config()

app = Flask(__name__)
client = TelegramClient(cfg["session_name"], cfg["api_id"], cfg["api_hash"])
dialogs_cache = []
messages_cache = {}
current_chat = None
me_info = None

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Telegram Web - {{ user_name }}</title>
    <meta charset="UTF-8">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { 
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
            background: #0e1621;
            color: #ffffff;
            height: 100vh;
            overflow: hidden;
        }
        .container {
            display: flex;
            height: 100vh;
        }
        .sidebar {
            width: 320px;
            background: #17212b;
            border-right: 1px solid #0e1621;
            display: flex;
            flex-direction: column;
        }
        .header {
            padding: 20px;
            background: #17212b;
            border-bottom: 1px solid #0e1621;
        }
        .header h2 {
            font-size: 20px;
            margin-bottom: 5px;
        }
        .user-info {
            font-size: 13px;
            color: #707579;
        }
        .chat-list {
            flex: 1;
            overflow-y: auto;
        }
        .chat-item {
            padding: 15px 20px;
            border-bottom: 1px solid #0e1621;
            cursor: pointer;
            transition: background 0.2s;
        }
        .chat-item:hover {
            background: #242f3d;
        }
        .chat-item.active {
            background: #2b5278;
        }
        .chat-name {
            font-weight: 500;
            margin-bottom: 5px;
            font-size: 15px;
        }
        .chat-preview {
            font-size: 13px;
            color: #707579;
            overflow: hidden;
            text-overflow: ellipsis;
            white-space: nowrap;
        }
        .main-content {
            flex: 1;
            display: flex;
            flex-direction: column;
            background: #0e1621;
        }
        .chat-header {
            padding: 15px 20px;
            background: #17212b;
            border-bottom: 1px solid #0e1621;
        }
        .chat-header h3 {
            font-size: 16px;
        }
        .messages-container {
            flex: 1;
            overflow-y: auto;
            padding: 20px;
        }
        .message {
            margin-bottom: 15px;
            max-width: 70%;
        }
        .message.sent {
            margin-left: auto;
        }
        .message-bubble {
            padding: 10px 15px;
            border-radius: 12px;
            background: #2b5278;
            display: inline-block;
        }
        .message.sent .message-bubble {
            background: #8774e1;
        }
        .message-sender {
            font-size: 13px;
            font-weight: 500;
            margin-bottom: 5px;
            color: #8774e1;
        }
        .message-text {
            font-size: 14px;
            line-height: 1.5;
            word-wrap: break-word;
        }
        .message-time {
            font-size: 11px;
            color: #a0a0a0;
            margin-top: 5px;
        }
        .input-area {
            padding: 15px 20px;
            background: #17212b;
            border-top: 1px solid #0e1621;
            display: flex;
            gap: 10px;
        }
        .message-input {
            flex: 1;
            padding: 12px 15px;
            background: #242f3d;
            border: none;
            border-radius: 20px;
            color: #ffffff;
            font-size: 14px;
            outline: none;
        }
        .send-button {
            padding: 12px 25px;
            background: #8774e1;
            border: none;
            border-radius: 20px;
            color: white;
            font-weight: 500;
            cursor: pointer;
            transition: background 0.2s;
        }
        .send-button:hover {
            background: #9f8aea;
        }
        .empty-state {
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100%;
            color: #707579;
            font-size: 16px;
        }
        .refresh-btn {
            padding: 8px 15px;
            background: #2b5278;
            border: none;
            border-radius: 15px;
            color: white;
            cursor: pointer;
            margin-top: 10px;
            font-size: 13px;
        }
        .refresh-btn:hover {
            background: #3a6591;
        }
        ::-webkit-scrollbar {
            width: 8px;
        }
        ::-webkit-scrollbar-track {
            background: #0e1621;
        }
        ::-webkit-scrollbar-thumb {
            background: #2b5278;
            border-radius: 4px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #3a6591;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="sidebar">
            <div class="header">
                <h2>Telegram</h2>
                <div class="user-info">{{ user_name }} • @{{ username }}</div>
                <button class="refresh-btn" onclick="refreshChats()">🔄 Refresh Chats</button>
            </div>
            <div class="chat-list" id="chatList">
                <!-- Chats will be loaded here -->
            </div>
        </div>
        <div class="main-content">
            <div id="emptyState" class="empty-state">
                Select a chat to start messaging
            </div>
            <div id="chatView" style="display: none; flex-direction: column; height: 100%;">
                <div class="chat-header">
                    <h3 id="currentChatName">Chat Name</h3>
                </div>
                <div class="messages-container" id="messagesContainer">
                    <!-- Messages will be loaded here -->
                </div>
                <div class="input-area">
                    <input type="text" class="message-input" id="messageInput" placeholder="Type a message..." onkeypress="handleKeyPress(event)">
                    <button class="send-button" onclick="sendMessage()">Send</button>
                </div>
            </div>
        </div>
    </div>

    <script>
        let currentChatId = null;
        let myUserId = {{ my_user_id }};

        async function refreshChats() {
            const response = await fetch('/api/chats');
            const chats = await response.json();
            const chatList = document.getElementById('chatList');
            chatList.innerHTML = '';
            
            chats.forEach(chat => {
                const div = document.createElement('div');
                div.className = 'chat-item';
                div.onclick = () => openChat(chat.id, chat.name);
                div.innerHTML = `
                    <div class="chat-name">${chat.name}</div>
                    <div class="chat-preview">${chat.unread > 0 ? '📬 ' + chat.unread + ' new messages' : 'No new messages'}</div>
                `;
                chatList.appendChild(div);
            });
        }

        async function openChat(chatId, chatName) {
            currentChatId = chatId;
            document.getElementById('currentChatName').textContent = chatName;
            document.getElementById('emptyState').style.display = 'none';
            document.getElementById('chatView').style.display = 'flex';
            
            const response = await fetch(`/api/messages/${chatId}`);
            const messages = await response.json();
            
            const container = document.getElementById('messagesContainer');
            container.innerHTML = '';
            
            messages.reverse().forEach(msg => {
                const div = document.createElement('div');
                div.className = 'message' + (msg.from_id === myUserId ? ' sent' : '');
                div.innerHTML = `
                    <div class="message-bubble">
                        ${msg.from_id !== myUserId ? `<div class="message-sender">${msg.sender_name}</div>` : ''}
                        <div class="message-text">${msg.text || '[Media]'}</div>
                        <div class="message-time">${msg.time}</div>
                    </div>
                `;
                container.appendChild(div);
            });
            
            container.scrollTop = container.scrollHeight;
            
            // Mark active chat
            document.querySelectorAll('.chat-item').forEach(item => {
                item.classList.remove('active');
            });
            event.target.closest('.chat-item').classList.add('active');
        }

        async function sendMessage() {
            if (!currentChatId) return;
            
            const input = document.getElementById('messageInput');
            const text = input.value.trim();
            if (!text) return;
            
            const response = await fetch('/api/send', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({chat_id: currentChatId, text: text})
            });
            
            if (response.ok) {
                input.value = '';
                openChat(currentChatId, document.getElementById('currentChatName').textContent);
            }
        }

        function handleKeyPress(event) {
            if (event.key === 'Enter') {
                sendMessage();
            }
        }

        // Auto-refresh chats every 5 seconds
        setInterval(refreshChats, 5000);
        
        // Auto-refresh messages if chat is open
        setInterval(() => {
            if (currentChatId) {
                const chatName = document.getElementById('currentChatName').textContent;
                openChat(currentChatId, chatName);
            }
        }, 3000);
        
        // Initial load
        refreshChats();
    </script>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(
        HTML_TEMPLATE,
        user_name=me_info['first_name'],
        username=me_info['username'] or 'no_username',
        my_user_id=me_info['id']
    )

@app.route('/api/chats')
def get_chats():
    return jsonify(dialogs_cache)

@app.route('/api/messages/<int:chat_id>')
def get_messages(chat_id):
    if chat_id in messages_cache:
        return jsonify(messages_cache[chat_id])
    return jsonify([])

@app.route('/api/send', methods=['POST'])
def send_message():
    data = request.json
    chat_id = data.get('chat_id')
    text = data.get('text')
    
    async def send():
        await client.send_message(chat_id, text)
        await load_messages(chat_id)
    
    asyncio.run(send())
    return jsonify({'status': 'ok'})

async def load_dialogs():
    global dialogs_cache
    dialogs = await client.get_dialogs(limit=50)
    dialogs_cache = []
    for dialog in dialogs:
        dialogs_cache.append({
            'id': dialog.id,
            'name': dialog.name,
            'unread': dialog.unread_count
        })
    print(f"📋 Loaded {len(dialogs_cache)} chats")

async def load_messages(chat_id):
    messages = []
    async for message in client.iter_messages(chat_id, limit=50):
        sender = await message.get_sender()
        sender_name = getattr(sender, 'first_name', 'Unknown')
        messages.append({
            'from_id': message.sender_id,
            'sender_name': sender_name,
            'text': message.text,
            'time': message.date.strftime('%H:%M')
        })
    messages_cache[chat_id] = messages

async def init_client():
    global me_info
    
    print("\n" + "="*70)
    print("     🚀 TELEGRAM WEB - 2FA Protected Shared Account 🚀")
    print("="*70)
    print("\n⚠️  This account requires 2FA password verification.")
    print("📞 Contact @TestingAccountHomies on Telegram for the password.")
    print("   Link: https://t.me/TestingAccountHomies")
    print("="*70)
    
    # Prompt for 2FA password
    password_2fa = getpass.getpass("\n🔑 Enter 2FA password to start web server: ")
    
    try:
        await client.connect()
        
        if not await client.is_user_authorized():
            print("\n❌ Session expired. Please run login.py first.")
            exit(1)
        
        # Verify 2FA password (if needed)
        try:
            me = await client.get_me()
            print(f"\n✅ 2FA verified! Access granted.")
        except SessionPasswordNeededError:
            try:
                await client.sign_in(password=password_2fa)
                me = await client.get_me()
                print(f"\n✅ 2FA verified! Access granted.")
            except Exception as e:
                print(f"\n❌ Incorrect 2FA password: {e}")
                print("Contact @TestingAccountHomies for the correct password.")
                exit(1)
        
        me_info = {
            'id': me.id,
            'first_name': me.first_name,
            'username': me.username
        }
        await load_dialogs()
        
        print(f"\n✅ Connected to shared account!")
        print(f"   Name: {me.first_name} (@{me.username or 'no_username'})")
        print(f"   Phone: {me.phone}")
        print(f"   User ID: {me.id}")
        print(f"\n🌐 Opening web interface at: http://localhost:5000")
        print(f"🔒 Keep this window open to use the web interface!")
        
    except Exception as e:
        print(f"\n❌ Authentication error: {e}")
        exit(1)

def run_flask():
    app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False)

async def main():
    await init_client()
    
    # Start Flask in a separate thread
    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()
    
    # Open browser
    await asyncio.sleep(2)
    webbrowser.open('http://localhost:5000')
    
    print("\n" + "="*60)
    print("Telegram Web Interface is running!")
    print("="*60)
    print("\nPress Ctrl+C to stop the server")
    print("="*60 + "\n")
    
    # Keep running
    try:
        while True:
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        print("\n\n👋 Shutting down...")

if __name__ == "__main__":
    with client:
        client.loop.run_until_complete(main())
