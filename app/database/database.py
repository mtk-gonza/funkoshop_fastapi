import time
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError
from app.config.settings import settings

engine = create_engine(settings.DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def wait_for_db():
    Base.metadata.create_all(bind=engine)
    while True:
        try:
            connection = engine.connect()
            connection.close()
            print('Connection to database successful.')
            break
        except OperationalError:
            print('Waiting for the database to be available...')
            time.sleep(5)