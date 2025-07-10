from dotenv import load_dotenv
import os

load_dotenv()  # load variables from .env

api_key = os.getenv("weather_api_key")

