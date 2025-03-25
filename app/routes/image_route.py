from fastapi import APIRouter, status, UploadFile, Depends, File
from app.controllers.image_controller import create_image
from app.auth.role_handler import has_role
from app.config.dependency import db_dependency, user_dependency
from app.enums.image_type_enum import ImageType

router = APIRouter(prefix='/images', tags=['IMAGES'])

@router.post('/{entity_type}/{entity_id}/{image_type}', summary='UPLOAD images for an Entity', status_code=status.HTTP_200_OK, dependencies=[Depends(has_role('role_editor'))])
async def upload_images(db: db_dependency, user: user_dependency, entity_type: str, entity_id: int, image_type:ImageType,  image_data: UploadFile = File(...)):
    return create_image(image_data, entity_type, entity_id, image_type, db, user)