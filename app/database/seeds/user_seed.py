from app.auth.jwt_handler import bcrypt_context
from app.enums.roles_enum import Roles

USERS = [
    {
        'email':'root@example.com', 
        'username':'root',
        'first_name': 'root',
        'last_name': 'root',
        'telefono': '91961',
        'password': bcrypt_context.hash('root'),
        'role': Roles.ROOT
    }
]