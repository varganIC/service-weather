from datetime import date
from typing import (
    List,
    Optional,
    Tuple
)

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.models import WeatherData


class WeatherRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_city_and_date(
        self,
        city: str,
        start_date: date,
        end_date: date
    ) -> Optional[List[WeatherData]]:
        result = (
            await self.session.execute(
                select(WeatherData)
                .where(
                    WeatherData.city == city,
                    WeatherData.date >= start_date,
                    WeatherData.date <= end_date
                )
            )
        )
        return result.scalars().all()

    async def get_stats(
        self,
        city: str,
        start_date: date,
        end_date: date
    ) -> Optional[Tuple[str, float, float]]:
        result = (
            await self.session.execute(
                select(
                    WeatherData.city,
                    func.avg(WeatherData.temperature).label("avg_temp"),
                    func.avg(WeatherData.humidity).label("avg_humidity")
                )
                .where(
                    WeatherData.city == city,
                    WeatherData.date >= start_date,
                    WeatherData.date <= end_date
                )
                .group_by(WeatherData.city)
            )
        )

        return result.first()
