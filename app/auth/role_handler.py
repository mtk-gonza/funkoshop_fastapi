from fastapi import Depends, HTTPException
from app.schemas.auth_schema import TokenData
from app.auth.jwt_handler import get_current_user

def has_role(required_role: str):
    def verify_role(user: TokenData = Depends(get_current_user)):
        role_hierarchy = {
            'role_root' : ['root'],
            'role_admin': ['admin', 'root'],
            'role_editor': ['root', 'admin', 'editor'],
            'role_user': ['root', 'admin', 'editor', 'user'],
            'role_guest': ['root', 'admin', 'editor', 'rser', 'guest']
        }
        user_roles = user.roles
        if isinstance(user_roles, str):
            user_roles = [user_roles]
        elif not isinstance(user_roles, list):
            raise HTTPException(status_code=403, detail='Rol inválido')
        allowed_roles = role_hierarchy.get(required_role)
        print(allowed_roles)
        if not allowed_roles:
            raise HTTPException(status_code=500, detail='Configuración de roles inválida')
        if not any(role in allowed_roles for role in user_roles):
            raise HTTPException(status_code=403, detail='No tiene permisos para acceder a este recurso')
        return user
    return verify_role