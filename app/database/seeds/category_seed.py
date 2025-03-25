from sqlalchemy.orm import Session
from app.models.category_model import Category
from app.schemas.category_schema import CategoryCreate
from app.services.category_service import create_category

CATEGORIES = [
    {
        'name':'funkos', 
        'description':'Funko Pop collectible figures'
    },
    {
        'name':'t-shirts', 
        'description':'Anime t-shirts, series, movies and more'
    },
    {
        'name':'keychains', 
        'description':'Collectible keychains'
    }
]

def seed_categories(session: Session):    
    existing_categories = session.query(Category).count()
    if existing_categories == 0:
        for category_data in CATEGORIES:
            category_create = CategoryCreate(**category_data)
            create_category(db=session, category=category_create)
        print(f'{len(CATEGORIES)} CATEGORIES inserted correctly.')
    else:
        print('The CATEGORIES data already exists, it will not be inserted again.')