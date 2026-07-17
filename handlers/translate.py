import os
from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.types import FSInputFile

from services.translate_api import translate_text, text_to_speech
from buttons.inline import language_pagination
from states.translator import TranslateState

router = Router()


@router.message(F.text == "🌐 Tarjima")
async def start_translate(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer("✍️ Tarjima qilmoqchi bo'lgan matnni yuboring")
    await state.set_state(TranslateState.text)


@router.message(TranslateState.text, F.text)
async def get_text(message: types.Message, state: FSMContext):
    await state.update_data(text=message.text)

    await message.answer(
        "🌍 Qaysi tilga tarjima qilay?",
        reply_markup=language_pagination(page=0)
    )

    await state.set_state(TranslateState.language)


@router.callback_query(TranslateState.language, F.data.startswith("page:"))
async def paginate_languages(call: types.CallbackQuery):
    page = int(call.data.split(":")[1])

    await call.message.edit_reply_markup(
        reply_markup=language_pagination(page)
    )
    await call.answer()



@router.callback_query(TranslateState.language, F.data.startswith("lang:"))
async def translate_result(call: types.CallbackQuery, state: FSMContext):
    lang = call.data.split(":")[1]
    data = await state.get_data()
    text = data["text"]

    try:
        # 1️⃣ Tarjima (BU DOIM ISHLAYDI)
        translated = await translate_text(text, dest_lang=lang)

        # 2️⃣ Avval matnni yuboramiz
        await call.message.answer(
            f"🌐 Tarjima:\n\n{translated}"
        )

        # 3️⃣ Ovozga o'girishni alohida try/except qilamiz
        try:
            audio_path = text_to_speech(translated, lang=lang)

            await call.message.answer_voice(
                FSInputFile(audio_path)
            )

            os.remove(audio_path)

        except Exception as tts_error:
            # 🔊 Ovoz chiqmasa — faqat xabar beramiz
            await call.message.answer(
                "🔇 Ushbu til uchun ovozga o'girish qo'llab-quvvatlanmaydi."
            )
            print("TTS error:", tts_error)

    except Exception as e:
        await call.message.answer("❌ Tarjima qilishda xatolik yuz berdi")
        print("Translate error:", e)

    await state.clear()
    await call.answer()