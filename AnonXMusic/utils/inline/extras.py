from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import SUPPORT_CHAT


def botplaylist_markup(_):
    buttons = [
        [
            InlineKeyboardButton(text=_["S_B_9"], url=SUPPORT_CHAT),
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="NOI NOI"),
        ],
    ]
    return buttons


def CLOSE_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["𝐓𝐇𝐀𝐕𝐀𝐑𝐀𝐍𝐀 𝐒𝐞𝐲𝐚𝐥"],
                    callback_data="NOI NOI",
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
