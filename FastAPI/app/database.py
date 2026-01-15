from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Toi&moi=1@localhost/fastapi"

engine = create_engine(SQLALCHEMY_DATABASE_URL) #connects to the database

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) #creates a session

Base = declarative_base()  #base class for our models


def get_db(): #dependency to get a database session
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close() 
    