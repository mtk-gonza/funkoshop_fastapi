from fastapi import HTTPException, status
from src.models.user_model import User
from src.services import user_service
from src.config.security import check_user, bcrypt_context
import logging

def get_user(user_id, db, user):
    check_user(user)
    try:
        db_user = user_service.read_user(db, user_id)
        if db_user is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found.')
        return db_user
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        logging.error(f'Error reading user: {e}')
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Internal server error.')

def get_users(db, user, skip, limit):
    check_user(user)
    try:
        users = user_service.read_users(db, skip=skip, limit=limit)
        return users
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        logging.error(f'Error reading users: {e}')
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Internal server error.')

def create_user(user_data, db):
    try:
        user_data = User(
            email=user_data.email,
            username=user_data.username,
            first_name=user_data.first_name,
            last_name=user_data.last_name,
            role=user_data.role,
            password=bcrypt_context.hash(user_data.password),
            is_active=True
        )    
        db_user = user_service.create_user(db, user_data)
        if db_user is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Error creating user.')
        return db_user
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        logging.error(f'Error creating user: {e}')
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Internal server error.')

def update_user(user_id, user_data, db, user):
    check_user(user)
    try:
        db_user = user_service.update_user(db, user_id, user_data)
        if db_user is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Error updating user.')
        return db_user
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        logging.error(f'Error updating user: {e}')
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Internal server error.')

def delete_user(user_id, db, user):
    check_user(user)
    try:
        db_user = user_service.delete_user(db, user_id)
        if db_user is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found.')
        return {'message': 'User deleted successfully'}
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        logging.error(f'Error deleting user: {e}')
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Internal server error.')