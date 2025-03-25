from sqlalchemy.orm import Session
from app.database.database import Base, engine
from app.database.seeds.licence_seed import seed_licences
from app.database.seeds.category_seed import seed_categories
from app.database.seeds.role_seed import seed_roles
from app.database.seeds.product_seed import seed_products
from app.database.seeds.user_seed import seed_users

def create_tables():
    Base.metadata.create_all(bind=engine)

def run_seeder():
    create_tables()
    with Session(engine) as session:
        seed_categories(session)
        seed_licences(session)
        seed_roles(session)
        seed_products(session)
        seed_users(session)