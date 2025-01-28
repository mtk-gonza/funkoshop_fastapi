from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from src.models.product_specification_model import ProductSpecification
from src.schemas.product_specification_schema import ProductSpecificationCreate, ProductSpecificationUpdate
import logging

def create_product_specification(db: Session, product_specification: ProductSpecificationCreate):
    try:
        db_product_specification = ProductSpecification(**product_specification.dict())
        db.add(db_product_specification)
        db.commit()
        db.refresh(db_product_specification)
        return db_product_specification
    except SQLAlchemyError as e:
        logging.error(f'Error creating product specification: {e}')
        db.rollback()
        return None

def read_product_specification(db: Session, product_specification_id: int):
    try:
        return db.query(ProductSpecification).filter(ProductSpecification.id == product_specification_id).first()
    except SQLAlchemyError as e:
        logging.error(f'Error reading product specification: {e}')
        return None

def read_product_specifications(db: Session, skip: int = 0, limit: int = 100):
    try:
        return db.query(ProductSpecification).offset(skip).limit(limit).all()
    except SQLAlchemyError as e:
        logging.error(f'Error reading product specifications: {e}')
        return None

def update_product_specification(db: Session, product_specification_id: int, product_specification: ProductSpecificationUpdate):
    try:
        db_product_specification = db.query(ProductSpecification).filter(ProductSpecification.id == product_specification_id).first()
        if db_product_specification:
            for key, value in product_specification.dict(exclude_unset=True).items():
                setattr(db_product_specification, key, value)
            db.commit()
            db.refresh(db_product_specification)
        return db_product_specification
    except SQLAlchemyError as e:
        logging.error(f'Error updating product specification: {e}')
        db.rollback()
        return None

def delete_product_specification(db: Session, product_specification_id: int):
    try:
        db_product_specification = db.query(ProductSpecification).filter(ProductSpecification.id == product_specification_id).first()
        if db_product_specification:
            db.delete(db_product_specification)
            db.commit()
        return db_product_specification
    except SQLAlchemyError as e:
        logging.error(f'Error deleting product specification: {e}')
        db.rollback()
        return None