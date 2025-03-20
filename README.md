# Telegram RSS Feed Generator

This project creates an RSS feed from a Telegram channel using Telethon and Flask. The RSS feed can be accessed via a simple HTTP request.

## 🚀 Features

- Converts Telegram channel posts into an RSS feed.
- Works inside a Docker container.
- Fetches the latest 10 messages from a configured Telegram channel.

---

## 🛠 Prerequisites

Before running the project, you need:

1. **A Telegram API Key**  
   - Go to [my.telegram.org](https://my.telegram.org/apps)  
   - Create a new app and get your `API_ID` and `API_HASH` - Save those values for later.

2. **Install Python & Telethon to Generate the Session File**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   pip install telethon
   ```

3. **Run the Following Script to Create the Session File**

   ```python
   from telethon.sync import TelegramClient

   API_ID = YOUR_API_ID  # Replace with your Telegram API ID
   API_HASH = "YOUR_API_HASH"  # Replace with your Telegram API HASH

   client = TelegramClient("session_name", API_ID, API_HASH)
   client.start()
   print("✅ Session file created successfully!")
   ```

4. **Move the Generated `session_name.session` File to the Project Folder**

   ```bash
   mv session_name.session /path/to/this/project/root/folder
   ```

---

## 🚀 Running the Project with Docker

### 1️⃣ Build & Start the Container

Edit the envs on

```bash
docker compose up -d --build
```

### 2️⃣ Access the RSS Feed

Replace `youripaddress` with your actual server IP or `localhost`:

```
http://youripaddress:3002/rss/TELEGRAMCHANNEL
```

Example:

```
http://192.168.1.100:3002/rss/YourTelegramChannel
```

---

## 📜 Environment Variables (Used in Dockerfile)

Instead of manually setting API credentials inside the script, you can store them in a `.env` file.

Example `.env` file:

```
API_ID=your_api_id
API_HASH=your_api_hash
CHANNELS=channel1,channel2,AnotherChannel
```

Then, use:

```bash
docker compose up --env-file .env -d
```

---

## 🛑 Stopping the Container

```bash
docker compose down
```

---

## 📌 Notes

- The **session file must be inside the `/app` directory** inside the container.
- If you face **authentication issues**, delete the session file and rerun the authentication step.
- Ensure **port 3002 is open** on your firewall.

---

## 🛠 Troubleshooting

- **Error: No session file found**
  - Ensure you generated the session file correctly and moved it to the project folder.

- **Error: Connection refused**
  - Ensure the container is running: `docker ps`
  - Check logs: `docker logs telegram_rss`

---

✅ **Now you can fetch Telegram channel messages as an RSS feed!** 🚀
