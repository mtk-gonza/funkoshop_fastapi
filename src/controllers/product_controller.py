from fastapi import HTTPException, status
from src.services import product_service
from src.config.security import check_user
import logging

def get_product(product_id, db, user):
    check_user(user)
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
    
def get_products(db, user, skip, limit):
    check_user(user)
    try:
        products = product_service.read_products(db, skip=skip, limit=limit)
        return products
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        logging.error(f'Error reading products: {e}')
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Internal server error.')
    
def create_product(product, db, user):
    check_user(user)
    try:
        db_product = product_service.create_product(db, product)
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