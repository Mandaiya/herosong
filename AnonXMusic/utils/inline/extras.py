from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import SUPPORT_CHAT


def botplaylist_markup(_):
    buttons = [
        [
            InlineKeyboardButton(text=_["S_B_9"], url=SUPPORT_CHAT),
            InlineKeyboardButton(text=_["ɴᴏɪ ɴᴏɪ_BUTTON"], callback_data="ɴᴏɪ ɴᴏɪ"),
        ],
    ]
    return buttons


def ɴᴏɪ ɴᴏɪ_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["ɴᴏɪ ɴᴏɪ - 𝐓𝐇𝐀𝐕𝐀𝐑𝐀𝐍𝐀 𝐒𝐞𝐲𝐚𝐥"],
                    callback_data="ɴᴏɪ ɴᴏɪ",
                ),
            ]
        ]
    )
    return upl


def supp_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["S_B_9"],
                    url=SUPPORT_CHAT,
                ),
            ]
        ]
    )
    return upl
