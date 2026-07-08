from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


lang_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Uzb 🇺🇿", callback_data="uz")
        ],
        [
            InlineKeyboardButton(text="Rus 🇷🇺", callback_data="ru")
        ],  
        [
            InlineKeyboardButton(text="Eng 🇬🇧", callback_data="en")
        ],
    ]
)