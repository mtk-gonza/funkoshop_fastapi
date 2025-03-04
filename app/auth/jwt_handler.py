from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
from typing import Annotated
from jose import jwt, JWTError
from fastapi import HTTPException, status, Depends
from app.config.settings import settings
from app.services.user_service import read_user_by_username
from app.schemas.auth_schema import TokenData

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')

def verify_password(plain_password, hashed_password):
    return bcrypt_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return bcrypt_context.hash(password)

def authenticate_user(username: str, password: str, db):
    user = read_user_by_username(db, username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user

def check_user(user):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Autenticación fallida.', headers={"WWW-Authenticate": "Bearer"})

async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        id_raw = payload.get('id')
        username_raw = payload.get('username')
        roles_raw = payload.get('roles')
        if id_raw is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='ID no encontrado en el token.')
        try:
            id_parsed = int(id_raw)
        except (ValueError, TypeError):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='ID inválido en el token.')
        if not isinstance(username_raw, str):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Nombre de usuario inválido en el token.')
        username_parsed = username_raw
        if not isinstance(roles_raw, list) or not all(isinstance(role, str) for role in roles_raw):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Roles inválidos en el token.')
        roles_parsed = roles_raw
        token_data = TokenData(id=id_parsed, username=username_parsed, roles=roles_parsed)
        return token_data
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='No se pudo validar el usuario.')
    
def create_access_token(id: int, username: str, roles: list[str], expires_delta: timedelta):
    encode = {
        'id': id, 
        'username': username, 
        'roles': roles
    }
    expire = datetime.utcnow() + expires_delta
    encode.update({'exp': expire})
    encoded_jwt = jwt.encode(encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

def has_role(required_role: str):
    def verify_role(user: TokenData = Depends(get_current_user)):
        roles = user.roles
        if isinstance(roles, str):
            if required_role != roles:
                raise HTTPException(status_code=403, detail='No tiene permisos para acceder a este recurso')
        elif isinstance(roles, list):
            if required_role not in roles:
                raise HTTPException(status_code=403, detail='No tiene permisos para acceder a este recurso')
        else:
            raise HTTPException(status_code=403, detail='Rol inválido')
        return user
    return verify_role