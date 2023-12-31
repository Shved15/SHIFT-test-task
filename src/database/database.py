from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from src.database.config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER

SQLALCHEMY_DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Создание асинхронного движка SQLAlchemy
engine = create_async_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(engine, class_=AsyncSession, autoflush=False, autocommit=False)
Base = declarative_base()


async def get_db():
    # Создание сеанса базы данных
    session = SessionLocal()
    try:
        yield session
    except Exception as e:
        print(e)
    finally:
        await session.close()
