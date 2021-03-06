# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message


@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""Halo! I play music in Telegram Groups OwO!
        
        I have a lot of cool feature that will amaze you!\n\nDo you want me to play music in your Telegram groups'voice chats? Please click the \'š User Manual š\' button below to know how you can use me.\n\nš“ The Assistant must be in your group to play music in the voice chat of your group.\n\nš“ More info & commands mentioned in the [User Manual](https://telegra.ph/Daisy-X-04-19)\n\nA project by @TeamDaisyX""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "š User Manual š", url="https://telegra.ph/Ongaku-Robot-05-15"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "šØāš» Updates šØāš»", url="https://t.me/OngakuUpdates"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Support Chat šļø", url="https://t.me/OngakuSupport"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
    await message.reply_text(
        """**š“ Music player is online**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "šļø Support Group šļø", url="OngakuSupport"
                    )
                ]
            ]
        ),
    )
