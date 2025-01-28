from sqlalchemy.orm import Session
from src.models.database import Base
from src.models.database import engine
from src.models.licence_model import Licence
from src.config.seeds.licence_seed import LICENCES
from src.models.category_model import Category
from src.config.seeds.category_seed import CATEGORIES
from src.models.product_model import Product
from src.config.seeds.product_seed import PRODUCTS
from src.models.user_model import User
from src.config.seeds.user_seed import USERS

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

        existing_products = session.query(Product).count()
        if existing_products == 0:
            session.bulk_insert_mappings(Product, PRODUCTS)
            session.commit()
            print(f'{len(PRODUCTS)} PRODUCTS inserted correctly.')
        else:
            print('The PRODUCTS data already exists, it will not be inserted again.')   
    
        existing_users = session.query(User).count()
        if existing_users == 0:
            session.bulk_insert_mappings(User, USERS)
            session.commit()
            print(f'{len(USERS)} USERS inserted correctly.')
        else:
            print('The USERS data already exists, it will not be inserted again.')   

def create_tables():
    Base.metadata.create_all(bind=engine)
    load_seed_data()
