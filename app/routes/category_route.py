from fastapi import APIRouter, status, Depends
from typing import List
from app.schemas.category_schema import CategoryResponse, CategoryCreate, CategoryUpdate
from app.config.dependency import db_dependency, user_dependency
from app.controllers import category_controller
from app.auth.role_handler import has_role

router = APIRouter(prefix='/categories', tags=['CATEGORIES'])

@router.get('/{category_id}', summary='GET Category by ID', response_model=CategoryResponse, dependencies=Depends(has_role('role_user')))
def get_category(category_id: int, db: db_dependency, user: user_dependency):
    return category_controller.get_category(category_id, db, user)

@router.get('/', summary='GET ALL Categories', response_model=List[CategoryResponse], dependencies=Depends(has_role('role_user')))
def get_categories(db: db_dependency, user: user_dependency):
    return category_controller.get_categories(db, user)

@router.post('/', summary='CREATE new Category', response_model=CategoryResponse, status_code=status.HTTP_201_CREATED, dependencies=Depends(has_role('role_editor')))
def create_category(category: CategoryCreate, db: db_dependency, user: user_dependency):
    return category_controller.create_category(category, db, user)

@router.put('/{category_id}', summary='UPDATE Category by ID', response_model=CategoryResponse, dependencies=Depends(has_role('role_editor')))
def update_category(category_id: int, category_data: CategoryUpdate, db: db_dependency, user: user_dependency):
    return category_controller.update_category(category_id, category_data, db, user)

@router.delete('/{category_id}', summary='DELETE Category by ID', response_model=CategoryResponse, dependencies=[Depends(has_role('role_root'))])
def delete_category(category_id: int, db: db_dependency, user: user_dependency):
    return category_controller.delete_category(category_id, db, user)