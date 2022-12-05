from pyrogram import filters
from YukkiMusic import userbot
from YukkiMusic.core.userbot import assistants
from config import DM_LINK


account1 = userbot.one
account2 = userbot.two
reply_text_dm = DM_LINK
counter = 0
counter2 = 0

@account1.on_message(filters.text & filters.private)
async def send_dm(client, message):
	global counter
	if counter!=5:
		await message.reply(reply_text_dm)
		counter+=1


@account2.on_message(filters.text & filters.private)
async def send_dm(client, message):
	global counter2
	if counter2!=5:
		await message.reply(reply_text_dm)
		counter2+=1
	


