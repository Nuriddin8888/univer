import os
from aiogram import Router, types, F
from aiogram.types import FSInputFile

from services.instagram_api import download_instagram_video

router = Router()


@router.message(F.text == "📸 Instagram")
async def instagram_handler(message: types.Message):
    await message.reply("Instagram havolasini yuboring")


@router.message(F.text.startswith('http'))
async def get_instagram_url(message: types.Message):
    url = message.text

    if "instagram.com" not in url:
        await message.answer("❌ Bu Instagram havolasi emas")
        return
    
    msg = await message.answer("⏳")

    try:
        video_path = download_instagram_video(url)
        video = FSInputFile(video_path)
        await message.answer_video(video)

        os.remove(video_path)

    except Exception as e:
        await message.answer("❌ Video yuklab bo'lmadi")
        print(e)

    await msg.delete()