from fastapi import APIRouter, status, Depends
from typing import List
from app.schemas.product_specification_schema import ProductSpecificationResponse, ProductSpecificationCreate, ProductSpecificationUpdate, ProductSpecificationDelete
from app.config.dependency import db_dependency, user_dependency
from app.controllers import product_specification_controller
from app.auth.role_handler import has_role

router = APIRouter(prefix='/product_specifications', tags=['PRODUCT SPECIFICATIONS'])

@router.get('/{product_specification_id}', summary='GET Product Specification by ID', response_model=ProductSpecificationResponse, dependencies=Depends(has_role('role_user')))
def get_product_specification(product_specification_id: int, db: db_dependency, user: user_dependency):
    return product_specification_controller.get_product_specification(product_specification_id, db, user)

@router.get('/', summary='GET ALL Specifications by Product', response_model=List[ProductSpecificationResponse], dependencies=Depends(has_role('role_user')))
def get_product_specifications(db: db_dependency, user: user_dependency, skip: int = 0, limit: int = 100):
    return product_specification_controller.get_product_specifications(db, user, skip, limit)

@router.post('/', summary='CREATE new Product Specification', response_model=ProductSpecificationResponse, status_code=status.HTTP_201_CREATED, dependencies=Depends(has_role('role_editor')))
def create_product_specification(product_specification: ProductSpecificationCreate, db: db_dependency, user: user_dependency):
    return product_specification_controller.create_product_specification(product_specification, db, user)

@router.put('/{product_specification_id}', summary='UPDATE Product Specification by ID', response_model=ProductSpecificationResponse, dependencies=Depends(has_role('role_editor')))
def update_product_specification(product_specification_id: int, product_specification_data: ProductSpecificationUpdate, db: db_dependency, user: user_dependency):
    return product_specification_controller.update_product_specification(product_specification_id, product_specification_data, db, user)

@router.delete('/{product_specification_id}', summary='DELETE Product Specification by ID', response_model=ProductSpecificationDelete, dependencies=[Depends(has_role('role_root'))])
def delete_product_specification(product_specification_id: int, db: db_dependency, user: user_dependency):
    return product_specification_controller.delete_product_specification(product_specification_id, db, user)