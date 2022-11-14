import time
import asyncio
import math
import os
import shutil
import socket
import traceback
from config import LOG_GROUP_ID
from pyrogram import Client, filters
from pyrogram.types import Message
from YukkiMusic import app

from YukkiMusic.utils.database.memorydatabase import (active, activevideo)
from YukkiMusic.misc import SUDOERS
from YukkiMusic.utils.cmdforac import avoice

#------------------------------Importing Module-----------------------------#


LOGss = config.LOG_GROUP_ID
counting = []
warn = sum(counting)

def main(client: Client, message: Message):
	A = "downloads"
    B = "raw_files"
    C = "cache"
	for i in range(50):
		try:
			shutil.rmtree(A)
			shutil.rmtree(C)
            counting.append(1)
		except:
			await app.send_message(chat_id=LOGss,text=f"Automatic Clearing Failed •❌\n─────────────────────────────•\n\nReason:\n───────•\n{traceback.format_exc()}")
		await app.send_message(chat_id=LOGss,text="Automatic Clearing Done •✅\n─────────────────────────────•\n\n❄Deleted:\n─────────•\n - Downloads\n - cache")
		time.sleep(5)

if warn==5:
    await app.send_message(chat_id=LOGss,text=f"Please Restart Bot Now By /reboot\nIt's Recommend")



if __name__ == "__main__":
    main()
