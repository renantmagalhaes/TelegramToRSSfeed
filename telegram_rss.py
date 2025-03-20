from telethon.sync import TelegramClient
from flask import Flask, Response
from feedgen.feed import FeedGenerator
import os

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
CHANNELS = os.getenv("CHANNELS", "").split(",")

client = TelegramClient("session_name", API_ID, API_HASH)
client.connect()

if not client.is_user_authorized():
    print("❌ Not authorized! Run authentication manually first.")
    exit(1)

app = Flask(__name__)


@app.route("/rss/<channel>")
def generate_rss(channel):
    if channel not in CHANNELS:
        return "Channel not configured.", 404

    messages = client.get_messages(channel, limit=10)

    fg = FeedGenerator()
    fg.title(f"{channel} Telegram Channel")
    fg.link(href=f"https://t.me/{channel}")
    fg.description(f"Latest posts from {channel}.")

    for msg in messages:
        entry = fg.add_entry()
        entry.title(msg.text[:50] if msg.text else "Media Post")
        entry.description(msg.text if msg.text else "This post contains media.")
        entry.link(href=f"https://t.me/{channel}/{msg.id}")

    return Response(fg.rss_str(pretty=True), mimetype="application/rss+xml")


if __name__ == "__main__":
    print("🚀 Starting Flask server on port 3002...")
    app.run(host="0.0.0.0", port=3002, debug=False, threaded=False)
