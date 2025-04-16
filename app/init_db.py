import asyncio
from datetime import datetime

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.models import WeatherData
from app.db.session import AsyncSession  # noqa F811

initial_data = [
    {"city": "Москва", "date": datetime(2025, 4, 1), "temperature": -3.2, "humidity": 81.0},    # noqa E501
    {"city": "Лондон", "date": datetime(2025, 4, 1), "temperature": 5.4, "humidity": 89.6},    # noqa E501
    {"city": "Токио", "date": datetime(2025, 4, 1), "temperature": 11.7, "humidity": 78.2},    # noqa E501
]


async def init():
    async with AsyncSession() as session:
        count = (
            await session.execute(
                select(
                    func.count(WeatherData.id)
                )
            )
        ).scalar()

        if count == 0:
            for item in initial_data:
                session.add(WeatherData(**item))
            await session.commit()


if __name__ == "__main__":
    asyncio.run(init())
