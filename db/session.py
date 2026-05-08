from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.config import settings
from typing import Generator

SQLALCHEMY_DATABAS_URL = settings.DATABASE_URL
# print("Database url is: ", settings.DATABASE_URL)

engine = create_engine(SQLALCHEMY_DATABAS_URL)

SESSIONLOCAL = sessionmaker(autoflush=False, autocommit=False, bind=engine)

def get_db() -> Generator:
    try:
        db = SESSIONLOCAL()
        yield db
    finally:
        db.close()







### for SQLite ###

# SQLALCHEMY_DATABAS_URL = "sqlite:///./sql_app.db"
# engine = create_engine(SQLALCHEMY_DATABAS_URL, 
#                        connect_args={"check_same_thread":False})

# SESSIONLOCAL = sessionmaker(autoflush=False, autocommit=False, bind=engine)