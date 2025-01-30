from sqlalchemy.orm import Session, joinedload
from sqlalchemy.exc import SQLAlchemyError
from app.models.product_model import Product
from app.schemas.product_schema import ProductCreate, ProductUpdate
import logging

def create_product(db: Session, product: ProductCreate):
    try:
        db_product = Product(**product.dict())
        db.add(db_product)
        db.commit()
        db.refresh(db_product)
        return db_product
    except SQLAlchemyError as e:
        logging.error(f'Error creating product: {e}')
        db.rollback()
        return None

def read_product(db: Session, product_id: int):
    try:
        return db.query(Product).filter(Product.id == product_id).first()
    except SQLAlchemyError as e:
        logging.error(f'Error reading product: {e}')
        return None

def read_products(db: Session, skip: int = 0, limit: int = 100):
    try:
        return db.query(Product).offset(skip).limit(limit).all()
    except SQLAlchemyError as e:
        logging.error(f'Error reading products: {e}')
        return None

def update_product(db: Session, product_id: int, product: ProductUpdate):
    try:
        db_product = db.query(Product).filter(Product.id == product_id).first()
        if db_product:
            for key, value in product.dict(exclude_unset=True).items():
                setattr(db_product, key, value)
            db.commit()
            db.refresh(db_product)
        return db_product
    except SQLAlchemyError as e:
        logging.error(f'Error updating product: {e}')
        db.rollback()
        return None

def delete_product(db: Session, product_id: int):
    try:
        db_product = db.query(Product).options(joinedload(Product.licence), joinedload(Product.category)).filter_by(id=product_id).first()
        if not db_product:
            return False
        db_product
        db.delete(db_product)
        db.commit()
        return True
    except SQLAlchemyError as e:
        logging.error(f'Error deleting product: {e}')
        db.rollback()
        return None    