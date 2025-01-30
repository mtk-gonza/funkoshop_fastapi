from fastapi import APIRouter, status
from typing import List
from app.schemas.product_schema import ProductResponse, ProductCreate, ProductUpdate, ProductDelete
from app.config.dependency import db_dependency, user_dependency
from app.controllers import product_controller

router = APIRouter(prefix='/products', tags=['PRODUCTS'])

@router.get('/{product_id}', summary='GET Product by ID', response_model=ProductResponse)
def get_product(product_id: int, db: db_dependency, user: user_dependency):
    return product_controller.get_product(product_id, db, user)

@router.get('/', summary='GET ALL Products', response_model=List[ProductResponse], status_code=status.HTTP_200_OK)
def get_products(user: user_dependency, db: db_dependency, skip: int = 0, limit: int = 100):
    return product_controller.get_products(db, user, skip, limit)

@router.post('/', summary='CREATE new Product', response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
def create_product(product_data: ProductCreate, db: db_dependency, user: user_dependency):
    return product_controller.create_product(product_data, db, user)

@router.put('/{product_id}', summary='UPDATE Product by ID', response_model=ProductResponse, status_code=status.HTTP_202_ACCEPTED)
def update_product(product_id: int, product_data: ProductUpdate, db: db_dependency, user: user_dependency):
    return product_controller.update_product(product_id, product_data, db, user)

@router.delete('/{product_id}', summary='DELETE Product by ID', response_model=ProductDelete, status_code=status.HTTP_202_ACCEPTED)
def delete_product(product_id: int, db: db_dependency, user: user_dependency):
    return product_controller.delete_product(product_id, db, user)