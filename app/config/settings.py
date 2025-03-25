import os
from dotenv import load_dotenv

load_dotenv()
class Settings:
    DATABASE_URL: str = os.getenv('SQLALCHEMY_DATABASE_URL')
    SECRET_KEY: str = os.getenv('SECRET_KEY')
    ALGORITHM: str = os.getenv('ALGORITHM', 'HS256')
    ACCESS_TOKEN_EXPIRE_HOURS: int = int(os.getenv('ACCESS_TOKEN_EXPIRE_HOURS', 2))

settings = Settings()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UPLOADS_DIR = os.path.join(BASE_DIR, 'uploads')
IMAGES_DIR = os.path.join(UPLOADS_DIR, 'images')