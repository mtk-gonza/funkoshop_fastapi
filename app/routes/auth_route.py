from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from app.config.dependency import db_dependency
from app.schemas.auth_schema import Token, TokenData
from app.controllers import auth_controller
from app.auth.jwt_handler import get_current_user, check_user

router = APIRouter(prefix='/auth', tags=['LOGIN'])

@router.post('/token', summary='GET Access Token', response_model=Token)
def login_for_acces_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency):
    return auth_controller.access_token(form_data, db)

@router.get('/current_user', summary='GET current User', status_code=status.HTTP_200_OK)
def current_user(user:Annotated[dict, Depends(get_current_user)]):
    check_user(user)
    return user