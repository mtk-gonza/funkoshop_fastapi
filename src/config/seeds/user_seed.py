from src.config.security import bcrypt_context
from src.enums.roles_enum import Roles

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