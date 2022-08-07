# Copyright (C) 2021 By AdityaPlayer

import asyncio
from pyrogram import Client, filters
from pyrogram.types import Dialog, Chat, Message
from pyrogram.errors import UserAlreadyParticipant
from modules.clientbot.clientbot import client as aditya
from modules.config import SUDO_USERS

@Client.on_message(filters.command(["gcast", "ارسال", "اذاعة"]))
async def broadcast(_, message: Message):
    sent=0
    failed=0
    if message.from_user.id not in SUDO_USERS:
        return
    else:
        wtf = await message.reply("`يابه مو يدلل مطورنة ...`")
        if not message.reply_to_message:
            await wtf.edit("**__الرجاء الرد على نص ...__**")
            return
        lmao = message.reply_to_message.text
        async for dialog in aditya.iter_dialogs():
            try:
                await aditya.send_message(dialog.chat.id, lmao)
                sent = sent+1
                await wtf.edit(f"`الاذاعة جارية` \n\n**تم الارسال:** `{sent}` مجموعة \n**فشل بـ:** {failed} مجموعة")
                await asyncio.sleep(3)
            except:
                failed=failed+1
        await message.reply_text(f"`اكتمل الاذاعة` \n\n**نم الارسال:** `{sent}` مجموعة \n**تم فشل:** {failed} مجموعة")
