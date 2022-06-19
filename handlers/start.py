import asyncio

from helpers.filters import command
from config import BOT_NAME as bn, BOT_USERNAME as bu, SUPPORT_GROUP, OWNER_USERNAME as me, START_IMG
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(command("/start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.delete()
    await message.reply_photo(
        photo=f"{START_IMG}",
        caption=f"""**━━━━━━━━━━━━━━━━━━
 مرحبا انا بوت يمكنني تشغيل الاغاني في المكالمه
اضغط على زر الاوامر لمعرفة طريقة التشغيل 
قناة سورس بـــيـــمبو [قناة السورس](t.me/B_e_m_0)...
━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " 🐥اضفني لي مجموعتك🐥 ", url=f"https://t.me/{bu}?startgroup=true"
                       ),
                  ],[
                    InlineKeyboardButton(
                        " ⚙️ ¦ السورس ", url=f"https://t.me/B_e_m_0"
                    ),
                    InlineKeyboardButton(
                        " ☣️ ¦ جـروب الدعم ", url=f"https://t.me/{SUPPORT_GROUP}"
                    )
                ],[
                    InlineKeyboardButton(
                        " 🖥 ¦ الأوامــر ", url=f"https://telegra.ph/%D8%A7%D9%87%D9%84%D8%A7-%D8%A8%D9%83-%D8%A7%D9%88%D8%A7%D9%85%D8%B1-%D8%A7%D9%84%D8%A8%D9%88%D8%AA-%D8%B9%D8%B1%D8%A8%D9%8A%D9%87-06-08"
                    ),
                    InlineKeyboardButton(
                        " 🧨 ¦ مطور السورس ", url="https://t.me/O1BOO"
                    )]
            ]
       ),
    )

