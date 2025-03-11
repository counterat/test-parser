from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import DATABASE_URL
from datetime import datetime
import asyncio 

Base = declarative_base()
engine = create_async_engine(DATABASE_URL, echo=False)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def drop_all_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

async def prepare_db():
    #спочатку видалимо все зайве (якщо є)
    await drop_all_tables()
    #потім створюємо таблиці в бд
    await create_tables()    
    
if __name__ == "__main__":
    asyncio.run(prepare_db())