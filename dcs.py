from telethon import TelegramClient, events, sync
import data

api_id = data.api_id
api_hash = f'{data.api_hash}'

client = TelegramClient('anon', api_id, api_hash)

@client.on(events.NewMessage)
async def my_event_handler(event):
    if 'amaterasu' in event.raw_text:
        while 1:
            await event.respond("Error: 958\nPlease, check your security! by [Young Dragons]")

client.start()
client.run_until_disconnected()