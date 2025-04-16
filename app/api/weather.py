from datetime import date
from typing import List

from fastapi import (
    APIRouter,
    Depends,
    Query
)
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.common import BaseResponse
from app.core.usecases.weather_service import WeatherService
from app.db.repository import WeatherRepository
from app.db.session import get_db
from app.schemas.weather import Stats, Weather

router = APIRouter()


@router.get(
    "/weather",
    tags=["Данные"],
    summary="Получить данные за указанный "
            "диапазон дат и город",
    response_model=List[Weather]
)
async def read_weather(
    start_date: date = Query(..., example='2025-04-10'),
    end_date: date = Query(..., example='2025-04-21'),
    city: str = Query(..., example='Москва'),
    db: AsyncSession = Depends(get_db),
):
    service = WeatherService(WeatherRepository(db))
    return BaseResponse(Weather).get_typed_response_multi(
        await service.get_weather(city, start_date, end_date)
    )


@router.get(
    "/stats",
    tags=["Статистика"],
    summary="Получить среднюю температуру и влажность "
            "за период для выбранного города",
    response_model=Stats
)
async def read_stats(
    start_date: date = Query(..., example='2025-01-01'),
    end_date: date = Query(..., example='2025-01-01'),
    city: str = Query(...),
    db: AsyncSession = Depends(get_db)
):
    service = WeatherService(WeatherRepository(db))
    return BaseResponse(Stats).get_typed_response_single(
        await service.get_statistics(city, start_date, end_date)
    )
