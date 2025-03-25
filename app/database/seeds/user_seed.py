from sqlalchemy.orm import Session
from app.auth.jwt_handler import bcrypt_context
from app.models.user_model import User
from app.models.role_model import Role

USERS = [
    {
        'username':'root',
        'email':'root@example.com', 
        'password': 'root',
        'first_name': 'root',
        'last_name': 'root',
        'telefono': '91961',
        'roles': ['root', 'admin', 'editor']
    },
    {
        'username':'admin',
        'email':'admin@example.com', 
        'password': 'admin',
        'first_name': 'admin',
        'last_name': 'admin',
        'telefono': '91961',
        'roles': ['admin', 'editor']
    },
    {
        'username':'editor',
        'email':'editor@example.com', 
        'password': 'editor',
        'first_name': 'editor',
        'last_name': 'editor',
        'telefono': '91961',
        'roles': ['editor']
    },
    {
        'username':'user',
        'email':'user@example.com', 
        'password': 'user',
        'first_name': 'user',
        'last_name': 'user',
        'telefono': '91961',
        'roles': ['user']
    },
    {
        'username':'guest',
        'email':'guest@example.com', 
        'password': 'guest',
        'first_name': 'guest',
        'last_name': 'guest',
        'telefono': '91961',
        'roles': ['guest']
    }
]

def seed_users(session: Session):
        existing_users = session.query(User).count()
        if existing_users == 0:
            roles = {role.name: role for role in session.query(Role).all()}
            users_to_insert = []
            for user_data in USERS:
                user_roles = []
                for role_name in user_data['roles']:
                    role = roles.get(role_name)
                    if not role:
                        print(f'Role: "{role_name}". not found for user: "{user_data['username']}".')
                        continue
                    user_roles.append(role)                
                hashed_password = bcrypt_context.hash(user_data['password'])
                user = User(
                    username=user_data['username'],
                    email=user_data['email'],
                    password=hashed_password,
                    first_name=user_data['first_name'],
                    last_name=user_data['last_name'],
                    telefono=user_data['telefono']
                )
                user.roles.extend(user_roles)
                users_to_insert.append(user)
            session.add_all(users_to_insert)
            session.commit()
            print(f'{len(users_to_insert)} USERS inserted correctly.')
        else:
            print('The USERS data already exists, it will not be inserted again.')