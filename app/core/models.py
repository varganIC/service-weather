from typing import Any

from sqlalchemy import Date, Index
from sqlalchemy.orm import Mapped, mapped_column

from app.core.common import Base


class WeatherData(Base):
    __tablename__ = "weather_data"

    id: Mapped[int] = mapped_column(primary_key=True)
    city: Mapped[str] = mapped_column()
    date: Mapped[Any] = mapped_column(Date, index=True)
    temperature: Mapped[float] = mapped_column()
    humidity: Mapped[float] = mapped_column()

    __table_args__ = (
        Index(
            "ix_weather_city_hash",
            "city",
            postgresql_using="hash"
        ),
    )
