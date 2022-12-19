import asyncio
from YukkiMusic import userbot as ashayulifeline
from config import SUPPORT_CHANNEL
#-----------If You Publish This Repo Without My Permission, Then You Are My SON HAHA--------------#

from pyrogram import filters
from pyrogram.raw import functions
from pyrogram.types import Message
#-------------Pyrogram's Needs Loaded--------------#

acc1 = ashayulifeline.one
acc2 = ashayulifeline.two
acc3 = ashayulifeline.three
acc4 = ashayulifeline.four
acc5 = ashayulifeline.five
textofdm = SUPPORT_CHANNEL
#ALL ACCOUNTS LOADED WITH STRING

@acc1.on_message(
    filters.private
    & ~filters.me
    & ~filters.bot
)

async def ayushshield(client: acc1, message: Message):
	await acc1.send_message(
		chat_id=message.id,
		text=f"Please Do Not Spam Else I'll Block You Soon !!\n\n\nJoin >>>>> \n{textofdm}",
		reply_to_message_id=message.id
		)

@acc2.on_message(
    filters.private
    & ~filters.me
    & ~filters.bot
)

async def ayushshield2(client: acc2, message: Message):
	await acc2.send_message(
		chat_id=message.id,
		text=f"Please Join\n\n{textofdm}",
		reply_to_message_id=message.id
		)

@acc3.on_message(
    filters.private
    & ~filters.me
    & ~filters.bot
)

async def ayushshield3(client: acc3, message: Message):
	await acc3.send_message(
		chat_id=message.id,
		text=f"Please Join\n\n{textofdm}",
		reply_to_message_id=message.id
		)

@acc4.on_message(
    filters.private
    & ~filters.me
    & ~filters.bot
)

async def ayushshield4(client: acc4, message: Message):
	await acc4.send_message(
		chat_id=message.id,
		text=f"Please Join\n\n{textofdm}",
		reply_to_message_id=message.id
		)

@acc5.on_message(
    filters.private
    & ~filters.me
    & ~filters.bot
)

async def ayushshield5(client: acc5, message: Message):
	await acc5.send_message(
		chat_id=message.id,
		text=f"Please Join\n\n{textofdm}",
		reply_to_message_id=message.id
		)
