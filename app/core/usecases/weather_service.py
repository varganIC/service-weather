from datetime import date
from typing import (
    List,
    Optional,
    Tuple
)

from app.core.models import WeatherData
from app.db.repository import WeatherRepository


class WeatherService:
    def __init__(self, repo: WeatherRepository):
        self.repo = repo

    async def get_weather(
        self,
        city: str,
        start_date: date,
        end_date: date
    ) -> Optional[List[WeatherData]]:
        return await self.repo.get_by_city_and_date(
            city, start_date, end_date
        )

    async def get_statistics(
        self,
        city: str,
        start_date: date,
        end_date: date
    ) -> Optional[Tuple[str, float, float]]:
        return await self.repo.get_stats(
            city, start_date, end_date
        )
