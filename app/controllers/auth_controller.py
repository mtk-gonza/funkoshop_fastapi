from datetime import timedelta
from fastapi import HTTPException, status
from app.auth.jwt_handler import authenticate_user, create_access_token
from app.config.settings import settings

def access_token(form_data, db):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='User could not be validated.')
    roles = [role.name for role in user.roles]
    token = create_access_token(user.id, user.username, roles, timedelta(settings.ACCESS_TOKEN_EXPIRE_HOURS))
    return {'access_token': token, 'token_type': 'bearer'}