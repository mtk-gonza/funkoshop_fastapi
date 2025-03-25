import logging
from fastapi import HTTPException, status, UploadFile
from app.config.dependency import db_dependency, user_dependency
from app.services import product_service, licence_service, category_service
from app.auth.jwt_handler import check_user
from app.schemas.product_schema import ProductCreate

def get_product(product_id:int, db:db_dependency):
    try:
        db_product = product_service.read_product(db, product_id)
        if db_product is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Product not found.')
        return db_product
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        logging.error(f'Error reading product: {e}')
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Internal server error.')
    
def get_products(db, skip, limit):
    try:
        products = product_service.read_products(db, skip=skip, limit=limit)
        return products
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        logging.error(f'Error reading products: {e}')
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Internal server error.')
    
def create_product(product_data:ProductCreate, db:db_dependency, user:user_dependency):
    check_user(user)
    try:
        db_licence = licence_service.read_licence(db, product_data.licence_id)
        if not db_licence:
            raise HTTPException(status_code=404, detail='Licence not found.')
        db_category = category_service.read_category(db, product_data.category_id)
        if not db_category:
            raise HTTPException(status_code=404, detail='Category not found.')
        db_product = product_service.create_product(db, product_data)
        if db_product is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Error creating product.')
        return db_product
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        logging.error(f'Error creating product: {e}')
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Internal server error.')

def update_product(product_id, product_data, db, user):
    check_user(user)
    try:
        db_product = product_service.update_product(db, product_id, product_data)
        if db_product is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Error updating product.')
        return db_product
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        logging.error(f'Error updating product: {e}')
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Internal server error.')

def delete_product(product_id, db, user):
    check_user(user)
    try:
        success = product_service.delete_product(db, product_id)
        if not success:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Product not found.')
        return {'message': 'Product deleted successfully.'}
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        logging.error(f'Error deleting product: {e}')
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Internal server error.')