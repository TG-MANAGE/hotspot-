import asyncio
from config import LOG_GROUP_ID
from YukkiMusic import userbot


ubapp = userbot.one

@ubapp.on_message(filters.text & filters.private)
async def echo(client, message):
	await ubapp.send_message(LOG_GROUP_ID, "Message sent with!!")
