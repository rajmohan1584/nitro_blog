from sqlalchemy import create_engine
from sqlalchemy.orm import (
    AsyncSession,
    DeclarativeBase,
    async_sessionmaker,
    sessionmaker,
)

SQLALCHEMY_DATABASE_URL = "sqlite:///./nitro_blog.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

AsyncSessionLocal = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

class Base(DeclarativeBase):
    pass

async def get_db():
    print("1. get_db Opening DB")

    async with AsyncSessionLocal() as session:
        print("2. get_db Giving DB to endpoint")
        yield session

        print("3. get_db Endpoint finished")

    print("4. get_db DB closed")

