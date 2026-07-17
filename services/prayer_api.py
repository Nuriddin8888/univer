import ssl
import certifi
import aiohttp
from config import PRAYER_API

ssl_context = ssl.create_default_context(cafile=certifi.where())

async def get_prayer_times():
    connector = aiohttp.TCPConnector(ssl=ssl_context)

    async with aiohttp.ClientSession(connector=connector) as session:
        async with session.get(PRAYER_API) as response:
            data = await response.json()

            timings = data["data"]["timings"]

            return {
                "Fajr": timings["Fajr"],
                "Sunrise": timings["Sunrise"],
                "Dhuhr": timings["Dhuhr"],
                "Asr": timings["Asr"],
                "Maghrib": timings["Maghrib"],
                "Isha": timings["Isha"],
            }