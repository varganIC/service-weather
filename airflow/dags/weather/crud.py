from sqlalchemy.orm import Session

from app.schemas.weather import WeatherCreate

from .models import WeatherData


def insert_data(db: Session, data: WeatherCreate) -> None:
    db_object = WeatherData(**data.dict())
    db.add(db_object)
    db.commit()
