from telethon.sync import TelegramClient

API_ID = xxxxxxx
API_HASH = "xXXXxXXxXxxxxxxxXXxXXxxxXXXXXXXXxxx"

client = TelegramClient("session_name", API_ID, API_HASH)
client.start()
