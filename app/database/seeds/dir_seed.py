import os
from app.database.seeds.licence_seed import LICENCES

UPLOADS_DIR = 'uploads'
IMAGES_DIR = os.path.join(UPLOADS_DIR, 'images')

def create_dir():
    os.makedirs(IMAGES_DIR, exist_ok=True)
    for licence in LICENCES:
        licence_name = licence['name']
        licence_dir = os.path.join(IMAGES_DIR, licence_name)
        os.makedirs(licence_dir, exist_ok=True)

    print('Folder structure created successfully.')