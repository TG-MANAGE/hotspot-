import sys
from pyrogram import Client, filters

userbot1 = Client("Dmgaurd",api_id=config.API_ID,api_hash=config.API_HASH,session_name=str(config.STRING1),no_updates=True,)


@userbot1.on_message(filters.text & filters.private)
async def echo(client, message):
  await message.reply(message.text)

userbot1.run() 
