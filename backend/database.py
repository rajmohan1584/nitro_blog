from sqlalchemy import create_engine
from sqlalchemy.orm import (
    DeclarativeBase,
    sessionmaker,
)

SQLALCHEMY_DATABASE_URL = "sqlite:///./nitro_blog.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass

def get_db():
    print("1. get_db Opening DB")

    with SessionLocal() as session:
        print("2. get_db Giving DB to endpoint")
        yield session

        print("3. get_db Endpoint finished")

    print("4. get_db DB closed")

