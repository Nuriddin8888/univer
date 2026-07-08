from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext

from services.translate_api import tarjimon
from buttons.inline import lang_btn
from states.translator import TranslatorState

router = Router()


@router.message(F.text == "🌐 Tarjima")
async def translate_handler(message: types.Message):
    await message.reply("Tarjima qilmoqchi bo'lgan textni yuboring")


@router.message(F.text)
async def get_user_text(message: types.Message, state: FSMContext):
    user_text = message.text
    await state.update_data(text=user_text)
    await message.answer("Qaysi tilga tarjima qilmoqchisiz", reply_markup=lang_btn)
    

@router.callback_query()
async def get_user_lang(callback: types.CallbackQuery):
    lang = callback.data
    print(lang)