from pyrogram import Client, filters
from pyrogram.types import Message
from YukkiMusic import app
from YukkiMusic.utils.database.memorydatabase import (get_active_chats, get_active_video_chats)
from YukkiMusic.misc import SUDOERS
from YukkiMusic.utils.cmdforac import avoice
#Imported Modules

#-------------------------------------------------------------------#





#--------------------------Code------------------#

@app.on_message(avoice(["/ac"]) & SUDOERS)
async def start(client: Client, message: Message):
    ac_audio = await get_active_chats
    ac_video = await get_active_video_chats
    aud = str(len(ac_audio))
    vid = str(len(ac_video))
    await message.reply_text(f"𝗕𝗼𝘁 𝗔𝗰𝘁𝗶𝘃𝗲 𝗖𝗵𝗮𝘁𝘀 𝗜𝗻𝗳𝗼 • 📟\n•━━━━━━━━━━━━━━━━━━•\n🎙•Aᴜᴅɪᴏ  » {aud} Gʀᴏᴜᴘs\n•───────•\n🖥• Vɪᴅᴇᴏ » {vid} Gʀᴏᴜᴘs\n•──────•", quote=True)
