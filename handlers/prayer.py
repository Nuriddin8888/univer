from aiogram import Router, F, types
from services.prayer_api import get_prayer_times
from aiogram.types import FSInputFile

router = Router()

@router.message(F.text == "🕌 Namoz vaqti")
async def prayer_handler(message: types.Message):
    data = await get_prayer_times()

    caption = (
        "🕌 <b>Namoz vaqtlari (Toshkent)</b>\n\n"
        f"🌅 <b>Bomdod:</b> {data['Fajr']}\n"
        f"🌞 <b>Quyosh:</b> {data['Sunrise']}\n"
        f"🏙 <b>Peshin:</b> {data['Dhuhr']}\n"
        f"🌇 <b>Asr:</b> {data['Asr']}\n"
        f"🌆 <b>Shom:</b> {data['Maghrib']}\n"
        f"🌙 <b>Xufton:</b> {data['Isha']}"
    )

    photo = FSInputFile("weather_img/prayer.png")

    await message.answer_photo(
        photo=photo,
        caption=caption,
        parse_mode="HTML"
    )