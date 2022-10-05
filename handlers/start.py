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
        caption=f"""** 
╭────── • ◈ • ──────╮
么 [𝙴𝙻𝚁𝙰𝚂𝙰𝙼](t.me/Mahmod777777)
么 [𝚂𝙾𝚄𝚁𝙲𝙴 𝙴𝙻𝚁𝙰𝚂𝙰𝙼](https://t.me/ELRSAM11)
么 [𝚃𝚄𝚁𝙱𝙾](t.me/A7A_BGAAD)
么  [𝙰𝙻𝚃𝚆𝙸𝙽𝚂](t.me/FATHY616)
么 [ᖇꪔᥲ️ᘔᎥᥲ️ƚ ᥱᥣᖇᥲ️᥉ᥲ️ꪔ❶💕🇨🇵](https://t.me/E_L_R_A_S_A_M)
╰────── • ◈ • ──────╯
⍟ 𝚃𝙷𝙴 𝙱𝙴𝚂𝚃 𝚂𝙾𝚄𝚁𝙲𝙴 𝙾𝙽 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼**""",
   reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " اضفني لي مجموعتك ", url=f"https://t.me/{bu}?startgroup=true"
                       ),
                  ],[
                    InlineKeyboardButton(
                        " ⚙️ ¦ السورس ", url=f"https://t.me/EL_RASA"
                    ),
                    InlineKeyboardButton(
                        " ☣️ ¦ جـروب الدعم ", url=f"https://t.me/{SUPPORT_GROUP}"
                    )
                ],[
                    InlineKeyboardButton(
                        " 🖥 ¦ الأوامــر ", url=f"https://telegra.ph/%F0%9D%91%BA%F0%9D%91%BC%F0%9D%91%B6%F0%9D%91%B9%F0%9D%91%AA%F0%9D%91%AC-%F0%9D%91%A9%F0%9D%91%AC%F0%9D%91%B4%F0%9D%91%A9%F0%9D%91%B6-06-19"
                    ),
                    InlineKeyboardButton(
                        " 🧨 ¦ مطور السورس ", url="https://t.me/Mahmod777777"
                    )]
            ]
       ),
    )

@Client.on_message(command(["مبرمج السورس" ,"التونز" ,"سورس" ,"السورس" ,"الرسام" ,"تربو" ,"الرسام"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/2ef137bfee167f549257b.jpg",
        caption=f""" 
•═════•| [𝙀ٍ𝙇ٓ𝙍َٰ𝘼َٰ𝙎َٰ𝘼ِّّ𝙈](https://t.me/EL_RASA) |•═════•
⌁么 [𝙴𝙻𝚁𝙰𝚂𝙰𝙼](t.me/Mahmod777777)
么 [𝚂𝙾𝚄𝚁𝙲𝙴 𝙴𝙻𝚁𝙰𝚂𝙰𝙼](https://t.me/ELRSAM11)
么 [𝚃𝚄𝚁𝙱𝙾](t.me/A7A_BGAAD)
么  [𝙰𝙻𝚃𝚆𝙸𝙽𝚂](t.me/FATHY616)
么 [ᖇꪔᥲ️ᘔᎥᥲ️ƚ ᥱᥣᖇᥲ️᥉ᥲ️ꪔ❶💕🇨🇵](https://t.me/E_L_R_A_S_A_M)
•═════•|  [𝙀ٍ𝙇ٓ𝙍َٰ𝘼َٰ𝙎َٰ𝘼ِّّ𝙈](https://t.me/ELRSAM11) |•═════•""",
        reply_markup=InlineKeyboardMarkup(
         [
            [
                InlineKeyboardButton("𝙴𝙻𝚁𝙰𝚂𝙰𝙼", url=f"https://t.me/Mahmod777777"),
           ],
            [
                InlineKeyboardButton("ِِ𝙰𝙻𝚃𝚆𝙸𝙽𝚂", url=f"https://t.me/FATHY616"),
            ],
            [
                InlineKeyboardButton(
                    "𝚃𝚄𝚁𝙱𝙾", url=f"https://t.me/A7A_BGAAD"
                ),
            ],
            [
                InlineKeyboardButton("🏆اضفني الى مجموعتك🏆", url=f"https://t.me/K61TBot?startgroup=true"),
            ]
         ]
     )
  )

@Client.on_message(command(["المطور", "/godzela", "مطور" ,"مطور البوت"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/b144db94dc0db0fd86526.jpg",
        caption=f""" الاول: هو مطور السورس🏆 \n الثاني: مطور البوت🏆 \n√""",
        reply_markup=InlineKeyboardMarkup(
         [
            [
                InlineKeyboardButton("𝐸𝐿𝑅𝐴𝑆𝐴𝑀", url=f"https://t.me/Mahmod777777"),
            ],
            [
                InlineKeyboardButton(
                        DEV_NAME, url=f"https://t.me/{OWNER_NAME}"
                ),
            ],
            [
                InlineKeyboardButton("🏆ضيـف البـوت لمجمـوعتـك🏆", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
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
                "🏆 **شكرا لإضافتي إلى مجموعتك لتشغيل الموسيقي!**\n\n"
                "🏆 **قم بترقيتي مسؤول في المجموعة لكي أتمكن من العمل بشكل صحيح\nولا تنسى كتابة `/انضم او بيمبو تعاله` لدعوة الحساب المساعد\nقم بكتابة`/تحديث` لتحديث قائمة المشرفين",
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
                        "🏆اضـفني لي مـجـمـوعـتـك🏆",
                        url=f'https://t.me/K61TBot?startgroup=true'),
                        ],
                    ]
                )
            )


chat_watcher_group = 5
