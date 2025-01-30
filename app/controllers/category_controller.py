from fastapi import HTTPException, status
from app.services import category_service
from app.auth.jwt_handler import check_user
import logging

def get_category(category_id, db, user):
    check_user(user)
    try:
        db_category = category_service.read_category(db, category_id)
        if db_category is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Category not found')
        return db_category
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        logging.error(f'Error reading category: {e}')
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Internal server error')

def get_categories(db, user):
    check_user(user)
    try:
        categories = category_service.read_categories(db)
        return categories
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        logging.error(f'Error reading categories: {e}')
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Internal server error')

def create_category(category, db, user):
    check_user(user)
    try:
        db_category = category_service.create_category(db, category)
        if db_category is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Error creating category')
        return db_category
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        logging.error(f'Error creating category: {e}')
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Internal server error')

def update_category(category_id, category_data, db, user):
    check_user(user)
    try:
        db_category = category_service.update_category(db, category_id, category_data)
        if db_category is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Error updating category')
        return db_category
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        logging.error(f'Error updating category: {e}')
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Internal server error')

def delete_category(category_id, db, user):
    check_user(user)
    try:
        db_category = category_service.delete_category(db, category_id)
        if db_category is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Error deleting category')
        return db_category
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        logging.error(f'Error deleting category: {e}')
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Internal server error')
