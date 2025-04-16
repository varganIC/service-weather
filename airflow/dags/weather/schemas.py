from datetime import datetime

from pydantic import BaseModel


class WeatherMain(BaseModel):
    temp: float
    humidity: float


class WeatherAPI(BaseModel):
    main: WeatherMain
    dt: datetime
