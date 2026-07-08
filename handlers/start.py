from aiogram import Router, types, F
from aiogram.filters import CommandStart

from database.crud import add_user, get_user
from buttons.default import phone_btn, main_keyboard

router = Router()


@router.message(CommandStart())
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user = get_user(user_id)
    if user:
        await message.answer("Botimizga xush kelibsiz", reply_markup=main_keyboard)
    else:
        await message.answer("Assalomu alaykum Botimizga xush kelibsiz\nBotdan to'liq foydalanish uchun ro'yxatdan o'ting👇", reply_markup=phone_btn)


@router.message(F.contact)
async def get_contact_handeler(message: types.Message):
    user_id = message.from_user.id
    full_name = message.from_user.full_name
    username = message.from_user.username
    phone_number = message.contact.phone_number
    add_user(user_id, full_name, username, phone_number)
    await message.answer("🥳")
    await message.answer("Muaffaqqiyatli ro'yxatdan o'tdingiz\nBotdan to'liq foydalanishingiz mumkin😉", reply_markup=main_keyboard)