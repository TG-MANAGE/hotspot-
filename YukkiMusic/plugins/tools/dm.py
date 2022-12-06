from pyrogram import Client, filters
from YukkiMusic import userbot
from YukkiMusic.core.userbot import assistants


#ub1 = Client("ayush",api_id=config.API_ID,api_hash=config.API_HASH,session_string=str(config.STRING1),no_updates=True)
account1 = userbot.one
account2 = userbot.two
reply_text_dm = str("COME => @LIFE_CODES")
counter = 0
counter2 = 0

@account1.on_message(filters.text & filters.private)
async def send_dm(client, message):
	await message.reply(reply_text_dm)


@account2.on_message(filters.text & filters.private)
async def send_dm(client, message):
	global counter2
	if counter2!=5:
		await message.reply(reply_text_dm)
		counter2+=1
	


