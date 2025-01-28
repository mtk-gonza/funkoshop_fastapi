from datetime import timedelta
from fastapi import HTTPException, status
from src.schemas.auth_schema import Token
from src.config.security import authenticate_user, create_access_token, get_current_user, check_user
from src.config.config import ACCESS_TOKEN_EXPIRE_HOURS

def access_token(form_data, db):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='User could not be validated.')
    token = create_access_token(user.username, user.id, user.role, timedelta(ACCESS_TOKEN_EXPIRE_HOURS))
    return {'access_token': token, 'token_type': 'bearer'}