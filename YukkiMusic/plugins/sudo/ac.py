from pyrogram import filters
from YukkiMusic.utils.database.memorydatabase import (get_active_chats, get_active_video_chats)
from YukkiMusic.misc import SUDOERS

#Imported Modules__________Code Of Ayush & Harpreet
#-------------------------------------------------------------------#

ac_audio = await get_active_chats
ac_video = await get_active_video_chats




#--------------------------Code------------------#

@app.on_message(commandpro(["/ac"]) & SUDOERS)
async def start(client: Client, message: Message):
    await message.reply_text(f"𝗕𝗼𝘁 𝗔𝗰𝘁𝗶𝘃𝗲 𝗖𝗵𝗮𝘁𝘀 𝗜𝗻𝗳𝗼 • 📟\n•━━━━━━━━━━━━━━━━━━•\n🎙•Aᴜᴅɪᴏ  » {ac_audio} Gʀᴏᴜᴘs\n•───────•\n🖥• Vɪᴅᴇᴏ » {ac_video} Gʀᴏᴜᴘs\n•──────•", quote=True)
