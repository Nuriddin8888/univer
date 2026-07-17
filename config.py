import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
PRAYER_API = os.getenv("PRAYER_API")
WEATHER_API = os.getenv("WEATHER_API")