from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📸 Instagram")
        ],
        [
            KeyboardButton(text="🕌 Namoz vaqti"),
            KeyboardButton(text="🤖 ChatGPT")
        ],
        [
            KeyboardButton(text="📄 PDF")
        ],
        [
            KeyboardButton(text="🌐 Tarjima"),
            KeyboardButton(text="⛅️ Ob-havo")
        ]
    ],
    resize_keyboard=True
)



phone_btn = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Telefon raqamim 📞", request_contact=True)
        ]
    ], resize_keyboard=True
)



def city_keyboard(city: str | None):
    if not city:
        return None

    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=city)]],
        resize_keyboard=True,
        one_time_keyboard=True
    )