import asyncio
from telethon import TelegramClient, events

# Telegram API ma'lumotlari
API_ID = YOUR_API_ID
API_HASH = "YOUR_API_HASH"
PHONE_NUMBER = "YOUR_PHONE_NUMBER"

# Guruhlar ro'yxati va xabar matni
groups = []  # Foydalanuvchi qo'shgan guruhlar saqlanadi
message_text = ""

async def send_messages():
    async with TelegramClient(PHONE_NUMBER, API_ID, API_HASH) as client:
        for group in groups:
            try:
                await client.send_message(group, message_text)
                print(f"✅ Xabar yuborildi: {group}")
            except Exception as e:
                print(f"❌ Xatolik: {group} - {e}")

async def main():
    global message_text
    async with TelegramClient(PHONE_NUMBER, API_ID, API_HASH) as client:
        print("Bot ishga tushdi! /addgroup orqali guruh qo'shing, /settext bilan xabar kiriting, /send bilan jo'nating.")
        
        @client.on(events.NewMessage(pattern='/addgroup'))
        async def add_group(event):
            if event.is_group:
                groups.append(event.chat_id)
                await event.reply("✅ Guruh qo'shildi!")
            else:
                await event.reply("❌ Bu buyruq faqat guruhlarda ishlaydi!")
        
        @client.on(events.NewMessage(pattern='/settext'))
        async def set_text(event):
            global message_text
            message_text = event.text.split("/settext ", 1)[-1]
            await event.reply("✅ Xabar matni o'rnatildi!")
        
        @client.on(events.NewMessage(pattern='/send'))
        async def send_now(event):
            await send_messages()
            await event.reply("✅ Reklama yuborildi!")
        
        await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())
