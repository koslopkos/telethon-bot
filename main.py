from telethon import TelegramClient, events

import asyncio

import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")

bot = TelegramClient("bot", API_ID, API_HASH)

@bot.on(events.NewMessage(pattern=r'(?i).*\b(hello|hi)\b'))
async def handler(event):
    await event.respond("Hi")

async def run():
    await bot.start(bot_token=BOT_TOKEN)
    await bot.run_until_disconnected()

def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())

if __name__ == "__main__":
    main()
