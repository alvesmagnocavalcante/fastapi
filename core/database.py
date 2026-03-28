from sqlalchemy.ext.asyncio import async_session, create_async_engine
from settings import Settings


engine = create_async_engine(Settings().DATABASE_URL)

async def get_session():
    async with async_session(engine, expire_on_commit=False) as session:
        yield session