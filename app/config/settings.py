import os
from dotenv import load_dotenv
from app.database.seeds.licence_seed import LICENCES

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

def create_dir():
    os.makedirs(IMAGES_DIR, exist_ok=True)
    for licence in LICENCES:
        licence_name = licence['name'].replace(" ", "-")
        licence_dir = os.path.join(IMAGES_DIR, licence_name)
        os.makedirs(licence_dir, exist_ok=True)
    print('Folder structure created successfully.')