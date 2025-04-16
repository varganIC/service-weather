from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from app.config import settings

DATABASE_URL = settings.DB_URL
engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSession = async_sessionmaker(engine, expire_on_commit=False)


async def get_db():
    async with AsyncSession() as session:
        yield session
