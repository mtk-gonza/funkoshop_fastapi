from fastapi import UploadFile, HTTPException
from pathlib import Path
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.models.image_model import Image
from app.enums.image_type_enum import ImageType
from app.config.settings import IMAGES_DIR, UPLOADS_DIR
from app.schemas.image_schema import ImageCreate
import logging

def save_image( file: UploadFile, entity_type: str, entity_id: int, image_type: ImageType, is_primary:bool, path_segments:str, db: Session) -> Image:
    file_path = Path(IMAGES_DIR) / "/".join(path_segments)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with open(file_path, "wb") as buffer:
            buffer.write(file.file.read())
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error uploading image: {str(e)}')
    normalized_path = str(file_path.relative_to(UPLOADS_DIR)).replace("\\", "/")
    db_image = Image(
        path=normalized_path,
        entity_type=entity_type,
        entity_id=entity_id,
        image_type=image_type.value,
        is_primary=is_primary
    )
    db.add(db_image)  
    db.commit() 
    db.refresh(db_image)  
    return db_image

def create_image(db:Session, image:ImageCreate):
    try:
        db_image = Image(**image.dict())
        db.add(db_image)
        db.commit()
        db.refresh(db_image)
        return db_image
    except SQLAlchemyError as e:
        logging.error(f'Error creating image: {e}')
        db.rollback()
        return None