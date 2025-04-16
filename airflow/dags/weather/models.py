from sqlalchemy import (
    Column,
    Date,
    Float,
    Integer,
    Text
)
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class WeatherData(Base):
    __tablename__ = "weather_data"

    id = Column(Integer, primary_key=True)
    city = Column(Text)
    date = Column(Date)
    temperature = Column(Float)
    humidity = Column(Float)
