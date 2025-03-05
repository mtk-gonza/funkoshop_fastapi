from fastapi import APIRouter, status, Depends
from typing import List
from app.schemas.licence_schema import LicenceResponse, LicenceCreate, LicenceUpdate
from app.config.dependency import db_dependency, user_dependency
from app.controllers import licence_controller
from app.auth.role_handler import has_role

router = APIRouter(prefix='/licences', tags=['LICENCES'])

@router.get('/{licence_id}', summary='GET Licence by ID', response_model=LicenceResponse, dependencies=[Depends(has_role('role_user'))])
def get_licence(licence_id: int, db: db_dependency, user: user_dependency):
    return licence_controller.get_licence(licence_id, db, user)

@router.get('/', summary='GET ALL Licences', response_model=List[LicenceResponse], dependencies=[Depends(has_role('role_user'))])
def get_licences(db: db_dependency, user: user_dependency):
    return licence_controller.get_licences(db, user)

@router.post('/', summary='CREATE new Licence', response_model=LicenceResponse, status_code=status.HTTP_201_CREATED, dependencies=[Depends(has_role('role_editor'))])
def create_licence(licence: LicenceCreate, db: db_dependency, user: user_dependency):
    return licence_controller.create_licence(licence, db, user)

@router.put('/{licence_id}', summary='UPDATE Licence by ID', response_model=LicenceResponse, dependencies=[Depends(has_role('role_editor'))])
def update_licence(licence_id: int, licence_data: LicenceUpdate, db: db_dependency, user: user_dependency):
    return licence_controller.update_licence(licence_id, licence_data, db, user)

@router.delete('/{licence_id}', summary='DELETE Licence by ID', response_model=LicenceResponse, dependencies=[Depends(has_role('role_root'))])
def delete_licence(licence_id: int, db: db_dependency, user: user_dependency):
    return licence_controller.delete_licence(licence_id, db, user)