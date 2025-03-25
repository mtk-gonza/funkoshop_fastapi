import logging
from fastapi import HTTPException, status, UploadFile
from app.config.dependency import db_dependency, user_dependency
from app.services import image_service, product_service, licence_service
from app.enums.image_type_enum import ImageType
from app.auth.jwt_handler import check_user

def create_image(image_data:UploadFile, entity_type: str, entity_id: int, image_type:ImageType, db:db_dependency, user:user_dependency):
    check_user(user)
    allowed = {'jpg', 'jpeg', 'png', 'webp'}
    ext = image_data.filename.split(".")[-1].lower()
    if ext not in allowed:
        raise HTTPException(status_code=400, detail='Unsupported format.')
    try:
        match entity_type.lower():
            case 'product':
                db_entity = product_service.read_product(db, entity_id)
                if not db_entity:
                    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Product not found.')
                licence_name = db_entity.licence.name.replace(' ', '-').lower()
                category_name = db_entity.category.name.replace(' ', '-').lower()
                product_name = db_entity.name.replace(' ', '-').lower()
                path_segments = [                    
                    licence_name,
                    category_name,
                    f'{product_name}_{(image_type.value).lower()}.{ext}'
                ]
            case 'licence':
                db_entity = licence_service.read_licence(db, entity_id)
                if not db_entity:
                    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Licence not found.')
                licence_name = db_entity.name.replace(' ', '-').lower()
                path_segments = [                    
                    licence_name,
                    'licence',
                    f'{licence_name}_{(image_type.value).lower()}.{ext}'
                ]
            case _:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'{entity_type.capitalize()} Not found.')
        
        is_primary = image_type.value in ['front', 'logo']
        db_image = image_service.save_image(image_data, entity_type, entity_id, image_type, is_primary, path_segments, db)
        if db_image:
            return {"message": "Images uploaded successfully"}        

    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        logging.error(f'Error creating image: {e}')
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Internal server error.')