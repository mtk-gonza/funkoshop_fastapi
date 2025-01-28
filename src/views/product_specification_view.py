from fastapi import APIRouter, HTTPException, status
from typing import List
from src.schemas.product_specification_schema import ProductSpecificationResponse, ProductSpecificationCreate, ProductSpecificationUpdate, ProductSpecificationDelete
from src.config.dependency import db_dependency, user_dependency
from src.controllers import product_specification_controller

router = APIRouter(prefix='/product_specifications', tags=['PRODUCT SPECIFICATIONS'])

@router.get('/{product_specification_id}', summary='GET Product Specification by ID', response_model=ProductSpecificationResponse)
def get_product_specification(product_specification_id: int, db: db_dependency, user: user_dependency):
    return product_specification_controller.get_product_specification(product_specification_id, db, user)

@router.get('/', summary='GET ALL Specifications by Product', response_model=List[ProductSpecificationResponse])
def get_product_specifications(db: db_dependency, user: user_dependency, skip: int = 0, limit: int = 100):
    return product_specification_controller.get_product_specifications(db, user, skip, limit)

@router.post('/', summary='CREATE new Product Specification', response_model=ProductSpecificationResponse, status_code=status.HTTP_201_CREATED)
def create_product_specification(product_specification: ProductSpecificationCreate, db: db_dependency, user: user_dependency):
    return product_specification_controller.create_product_specification(product_specification, db, user)

@router.put('/{product_specification_id}', summary='UPDATE Product Specification by ID', response_model=ProductSpecificationResponse)
def update_product_specification(product_specification_id: int, product_specification_data: ProductSpecificationUpdate, db: db_dependency, user: user_dependency):
    return product_specification_controller.update_product_specification(product_specification_id, product_specification_data, db, user)

@router.delete('/{product_specification_id}', summary='DELETE Product Specification by ID', response_model=ProductSpecificationDelete)
def delete_product_specification(product_specification_id: int, db: db_dependency, user: user_dependency):
    return product_specification_controller.delete_product_specification(product_specification_id, db, user)