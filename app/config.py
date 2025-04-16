import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    DB_URL: str = os.getenv("ASYNC_DATABASE_URL")
    SYNC_DB_URL: str = os.getenv("SYNC_DATABASE_URL")
    WEATHER_API_KEY: str = os.getenv("WEATHER_API_KEY")
    PORT: int = int(os.getenv("PORT", 8000))


settings = Settings()
