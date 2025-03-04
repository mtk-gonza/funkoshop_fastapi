from sqlalchemy.orm import Session
from app.database.database import Base, engine
from app.models.licence_model import Licence
from app.database.seeds.licence_seed import LICENCES
from app.models.category_model import Category
from app.database.seeds.category_seed import CATEGORIES
from app.database.seeds.role_seed import ROLES
from app.models.role_model import Role
from app.models.product_model import Product
from app.database.seeds.product_seed import PRODUCTS
from app.models.user_model import User
from app.database.seeds.user_seed import USERS
from app.auth.jwt_handler import bcrypt_context

def load_seed_data():
    with Session(engine) as session:
        existing_categories = session.query(Category).count()
        if existing_categories == 0:
            session.bulk_insert_mappings(Category, CATEGORIES)
            session.commit()
            print(f'{len(CATEGORIES)} CATEGORIES inserted correctly.')
        else:
            print('The CATEGORIES data already exists, it will not be inserted again.')

        existing_licences = session.query(Licence).count()
        if existing_licences == 0:
            session.bulk_insert_mappings(Licence, LICENCES)
            session.commit()
            print(f'{len(LICENCES)} LICENCES inserted correctly.')
        else:
            print('The LICENCES data already exists, it will not be inserted again.')

        existing_roles = session.query(Role).count()
        if existing_roles == 0:
            roles_data = [{'name': role['name'], 'description': role['description']} for role in ROLES]
            session.bulk_insert_mappings(Role, roles_data)
            session.commit()
            print(f'{len(ROLES)} ROLES inserted correctly.')
        else:
            print('The ROLES data already exists, it will not be inserted again.')

        existing_products = session.query(Product).count()
        if existing_products == 0:
            session.bulk_insert_mappings(Product, PRODUCTS)
            session.commit()
            print(f'{len(PRODUCTS)} PRODUCTS inserted correctly.')
        else:
            print('The PRODUCTS data already exists, it will not be inserted again.')

        existing_users = session.query(User).count()
        if existing_users == 0:
            roles = {role.name: role for role in session.query(Role).all()}
            users_to_insert = []
            for user_data in USERS:
                user_roles = []
                for role_name in user_data['roles']:
                    role = roles.get(role_name)
                    if not role:
                        print(f"Role '{role_name}' no encontrado para el usuario '{user_data['username']}'.")
                        continue
                    user_roles.append(role)

                # Cifrar la contraseña
                hashed_password = bcrypt_context.hash(user_data['password'])

                # Crear el objeto User
                user = User(
                    username=user_data['username'],
                    email=user_data['email'],
                    password=hashed_password,
                    first_name=user_data['first_name'],
                    last_name=user_data['last_name'],
                    telefono=user_data['telefono']
                )

                # Asignar roles al usuario
                user.roles.extend(user_roles)
                users_to_insert.append(user)

            # Insertar usuarios en la base de datos
            session.add_all(users_to_insert)
            session.commit()
            print(f'{len(users_to_insert)} USERS inserted correctly.')
        else:
            print('The USERS data already exists, it will not be inserted again.')

def create_tables():
    Base.metadata.create_all(bind=engine)
    load_seed_data()