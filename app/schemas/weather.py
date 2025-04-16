from datetime import date

from pydantic import BaseModel


class WeatherBase(BaseModel):
    city: str
    date: date
    temperature: float
    humidity: float


class WeatherCreate(WeatherBase):
    pass


class Weather(WeatherBase):
    id: int

    class Config:
        orm_mode = True


class Stats(BaseModel):
    city: str
    avg_temp: float
    avg_humidity: float

    class Config:
        orm_mode = True
