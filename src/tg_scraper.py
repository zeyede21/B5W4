import os
import csv
from dotenv import load_dotenv
from telethon.sync import TelegramClient

# ✅ Load environment variables
load_dotenv()
api_id = int(os.getenv("API_ID"))  # ✅ Correct key
api_hash = os.getenv("API_HASH")   # ✅ Correct key
phone = os.getenv("PHONE")         # ✅ Optional for login

# ✅ Safety check
if not api_id or not api_hash:
    raise ValueError("❌ API ID or API HASH is missing from environment variables!")

# Function to scrape messages
async def scrape_channel(client, channel_username, writer, media_dir):
    entity = await client.get_entity(channel_username)
    channel_title = entity.title
    async for message in client.iter_messages(entity, limit=300):
        media_path = None
        if message.media and hasattr(message.media, 'photo'):
            filename = f"{channel_username}_{message.id}.jpg"
            media_path = os.path.join(media_dir, filename)
            await client.download_media(message.media, media_path)

        writer.writerow([channel_title, channel_username, message.id, message.message, message.date, media_path])

# ✅ Telegram client setup
client = TelegramClient('scraping_session', api_id, api_hash)

async def main():
    await client.start(phone=phone)  # Optional phone if login needed
    media_dir = '../data/photos'
    os.makedirs(media_dir, exist_ok=True)

    with open('../data/telegram_scraped_message.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Channel Title', 'Channel Username', 'ID', 'Message', 'Date', 'Media Path'])

        channels = [
            "ZemenExpress","kuruwear","nevacomputer", "meneshayeofficial", "ethio_brand_collection"
        ]

        for channel in channels:
            await scrape_channel(client, channel, writer, media_dir)
            print(f"✅ Scraped data from {channel}")

# Run the client
with client:
    client.loop.run_until_complete(main())
