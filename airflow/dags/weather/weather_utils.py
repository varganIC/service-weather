import requests
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

from app.config import settings
from app.schemas.weather import WeatherCreate

from . import crud
from .schemas import WeatherAPI

API_KEY = settings.WEATHER_API_KEY
DATABASE_URL = settings.SYNC_DB_URL
CITIES = {
    "Moscow": "Москва",
    "London": "Лондон",
    "Tokyo": "Токио"
}


def fetch_and_store() -> None:
    engine = create_engine(DATABASE_URL)
    with Session(engine) as session:
        for city, rus_name in CITIES.items():
            response = requests.get(
                "https://api.openweathermap.org/data/2.5/weather",
                params={
                    "q": city,
                    "appid": API_KEY,
                    "units": "metric"
                }
            )
            if response.status_code == 200:
                data = WeatherAPI(**response.json())
                crud.insert_data(
                    session,
                    WeatherCreate(
                        city=rus_name,
                        date=data.dt.date(),
                        temperature=data.main.temp,
                        humidity=data.main.humidity
                    )
                )


def check_latest() -> None:
    engine = create_engine(DATABASE_URL)
    with engine.connect() as conn:
        query = """
            SELECT COUNT(*) FROM weather_data
            WHERE date >= CURRENT_DATE - INTERVAL '1 day'
        """
        result = conn.execute(text(query)).scalar()
        if result == 0:
            print("⚠️ ALERT: No weather data added in the last 24 hours!")
