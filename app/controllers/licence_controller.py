from fastapi import HTTPException, status, UploadFile
from app.services import licence_service
from app.config.dependency import db_dependency, user_dependency
from app.schemas.licence_schema import LicenceCreate, LicenceUpdate
from app.auth.jwt_handler import check_user
import logging

def get_licence(licence_id: int, db: db_dependency):
    try:
        db_licence = licence_service.read_licence(db, licence_id)
        if db_licence is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Licence not found')
        return db_licence
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        logging.error(f'Error reading licence: {e}')
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Internal server error')

def get_licences(db: db_dependency):
    try:
        licences = licence_service.read_licences(db)
        return licences
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        logging.error(f'Error reading licences: {e}')
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Internal server error')

def create_licence(licence_data: LicenceCreate, db: db_dependency, user: user_dependency):
    check_user(user)
    try:
        db_licence = licence_service.create_licence(db, licence_data)
        if db_licence is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Error creating licence')
        return db_licence
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        logging.error(f'Error creating licence: {e}')
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Internal server error')

def update_licence(licence_id: int, licence_data: LicenceUpdate, db: db_dependency, user: user_dependency):
    check_user(user)
    try:
        db_licence = licence_service.update_licence(db, licence_id, licence_data)
        if db_licence is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Error updating licence')
        return db_licence
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        logging.error(f'Error updating licence: {e}')
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Internal server error')

def delete_licence(licence_id: int, db: db_dependency, user: user_dependency):
    check_user(user)
    try:
        db_licence = licence_service.delete_licence(db, licence_id)
        if db_licence is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Error deleting licence')
        return db_licence
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        logging.error(f'Error deleting licence: {e}')
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Internal server error')
