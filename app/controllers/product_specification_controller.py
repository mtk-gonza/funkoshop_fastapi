from fastapi import HTTPException, status
from app.services import product_specification_service
from app.auth.jwt_handler import check_user
import logging

def get_product_specification(product_specification_id, db, user):
    check_user(user)
    try:
        db_product_specification = product_specification_service.read_product_specification(db, product_specification_id)
        if db_product_specification is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Product specification not found.')
        return db_product_specification
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        logging.error(f'Error reading product specification: {e}')
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Internal server error.')

def get_product_specifications(db, user, skip, limit):
    check_user(user)
    try:
        product_specifications = product_specification_service.read_product_specifications(db, skip=skip, limit=limit)
        return product_specifications
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        logging.error(f'Error reading product specifications: {e}')
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Internal server error.')

def create_product_specification(product_specification, db, user):
    check_user(user)
    try:
        db_product_specification = product_specification_service.create_product_specification(db, product_specification)
        if db_product_specification is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Error creating product specification.')
        return db_product_specification
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        logging.error(f'Error creating product specification: {e}')
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Internal server error.')

def update_product_specification(product_specification_id, product_specification_data, db, user):
    check_user(user)
    try:
        db_product_specification = product_specification_service.update_product_specification(db, product_specification_id, product_specification_data)
        if db_product_specification is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Error updating product specification.')
        return db_product_specification
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        logging.error(f'Error updating product specification: {e}')
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Internal server error.')

def delete_product_specification(product_specification_id, db, user):
    check_user(user)
    try:
        db_product_specification = product_specification_service.delete_product_specification(db, product_specification_id)
        if db_product_specification is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Product specification not found.')
        return {'message': 'Product specification deleted successfully.'}
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        logging.error(f'Error deleting product specification: {e}')
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Internal server error.')