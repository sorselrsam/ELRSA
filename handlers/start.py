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
 مرحبا انا بوت يمكنني تشغيل الاغاني في المكالمات الصوتيه
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

@Client.on_message(command(["مبرمج السورس" ,"افيونه" ,"سورس" ,"السورس" ,"بيمبو" ,"افيونا"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/f1298741a0af71043e210.jpg",
        caption=f""" 𝑺𝑶𝑼𝑹𝑪𝑬 𝑩𝑬𝑴𝑩Θ """,
        reply_markup=InlineKeyboardMarkup(
         [
            [
                InlineKeyboardButton("افـ ـيـ ـونـ ـا بــــ ــاشـــ ــا🇪🇬!", url=f"https://t.me/O1BOO"),
            ],
            [
                InlineKeyboardButton(
                    "𝑩𝑬𝑴𝑩Θ 𝐌𝐔𝐒𝐈𝐂🐥", url=f"https://t.me/B_e_m_0"
                ),
            ],
            [
                InlineKeyboardButton("🐥اضف البوت الى مجموعتك🐥", url=f"https://t.me/K61TBot?startgroup=true"),
            ]
         ]
     )
  )

@Client.on_message(command(["المطور", "/pempo", "مطور" ,"مطور البوت"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/f1298741a0af71043e210.jpg",
        caption=f""" الاول: هو مطور السورس🐥 \n الثاني: مطور البوت🐥 \n√""",
        reply_markup=InlineKeyboardMarkup(
         [
            [
                InlineKeyboardButton("افـ ـيـ ـونـ ـا بــــ ــاشـــ ــا🇪🇬!", url=f"https://t.me/O1BOO"),
            ],
            [
                InlineKeyboardButton(
                        DEV_NAME, url=f"https://t.me/{OWNER_NAME}"
                ),
            ],
            [
                InlineKeyboardButton("🐥ضيـف البـوت لمجمـوعتـك🐥", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
            ]
         ]
     )
  )

@Client.on_message(filters.new_chat_members)
async def new_chat(c: Client, m: Message):
    chat_id = m.chat.id
    if await is_served_chat(chat_id):
        pass
    else:
        await add_served_chat(chat_id)
    ass_uname = (await user.get_me()).username
    bot_id = (await c.get_me()).id
    for member in m.new_chat_members:
        if member.id == bot_id:
            return await m.reply(
                "🐥 **شكرا لإضافتي إلى مجموعتك لتشغيل الموسيقي!**\n\n"
                "🐥 **قم بترقيتي مسؤول في المجموعة لكي أتمكن من العمل بشكل صحيح\nولا تنسى كتابة `/انضم او بيمبو تعاله` لدعوة الحساب المساعد\nقم بكتابة`/تحديث` لتحديث قائمة المشرفين",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("⚙️ ¦ السورس ", url=f"https://t.me/{UPDATES_CHANNEL}"),
                            InlineKeyboardButton("☣️ ¦ جـروب الدعم", url=f"https://t.me/{GROUP_SUPPORT}")
                        ],
                        [
                            InlineKeyboardButton(
                        ALIVE_NAME, url=f"https://t.me/{ass_uname}"),
                        ],
                        [
                            InlineKeyboardButton(
                        "🐥اضـفني لي مـجـمـوعـتـك🐥",
                        url=f'https://t.me/K61TBot?startgroup=true'),
                        ],
                    ]
                )
            )


chat_watcher_group = 5
