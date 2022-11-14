from pyrogram import Client, filters
from pyrogram.types import Message
from YukkiMusic import app
import asyncio
import math
import os
import shutil
import socket

import traceback

from YukkiMusic.utils.database.memorydatabase import (active, activevideo)
from YukkiMusic.misc import SUDOERS
from YukkiMusic.utils.cmdforac import avoice
#Imported Modules

#-------------------------------------------------------------------#





#--------------------------Code------------------#

@app.on_message(avoice(["/ac"]) & SUDOERS)
async def start(client: Client, message: Message):
    ac_audio = str(len(active))
    ac_video = str(len(activevideo))
    await message.reply_text(f"𝗕𝗼𝘁 𝗔𝗰𝘁𝗶𝘃𝗲 𝗖𝗵𝗮𝘁𝘀 𝗜𝗻𝗳𝗼 • 📟\n•━━━━━━━━━━━━━━━━━━•\n🎙•Aᴜᴅɪᴏ  » {ac_audio} Gʀᴏᴜᴘs\n•───────•\n🖥• Vɪᴅᴇᴏ » {ac_video} Gʀᴏᴜᴘs\n•──────•", quote=True)


#--------------------------Clean_Commands------------------------#

@app.on_message(avoice(["/fc"]) & SUDOERS)
async def cleaning(client: Client, message: Message):
    A = "downloads"
    B = "raw_files"
    C = "cache"
    try:
        shutil.rmtree(A)
        shutil.rmtree(B)
        shutil.rmtree(C)
    except:
        await message.reply_text(f"Failed To Delete Temp !!\nPlease Read\n{traceback.format_exc()}", quote=True)
    await message.reply_text(f"Successfully Deleted Below Folders:\n -Downloads\n -raw_files\n -Cache", quote=True)


