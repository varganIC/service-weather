import uvicorn
from fastapi import FastAPI

from app.api import weather
from app.config import settings

app = FastAPI(title="Weather Back")
app.include_router(weather.router)


if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=settings.PORT)
