import os
import logging
from fastapi import UploadFile
from sqlalchemy.orm import Session, joinedload
from sqlalchemy.exc import SQLAlchemyError
from app.models.product_model import Product
from app.schemas.product_schema import ProductCreate, ProductUpdate
from app.config.settings import UPLOADS_DIR

def create_product(db: Session, product_data: ProductCreate, image_front: str, image_back: str):
    try:
        db_product = Product(
            name = product_data.name,
            description = product_data.description,
            price = product_data.price,
            stock = product_data.stock,
            discount = product_data.discount,
            sku = product_data.sku,
            dues = product_data.dues,
            special = product_data.special,
            licence_id = product_data.licence_id,
            category_id = product_data.category_id,
            image_front = image_front,
            image_back = image_back,
            specifications=product_data.specifications
        )
        db.add(db_product)
        db.commit()
        db.refresh(db_product)
        return db_product
    except SQLAlchemyError as e:
        logging.error(f'Error creating product: {e}')
        db.rollback()
        raise ValueError('Error al crear el producto. Verifica los datos proporcionados.')
    except Exception as e:
        logging.error(f'Unexpected error: {e}')
        db.rollback()
        raise ValueError('Ocurrió un error inesperado al crear el producto.')

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
    
def save_product_image(file: UploadFile, licence_name: str, category_name: str, product_name: str, is_front: bool) -> str:
    uploads_dir = UPLOADS_DIR
    images_dir = os.path.join(uploads_dir, 'images')
    licence_dir = os.path.join(images_dir, licence_name)
    category_dir = os.path.join(licence_dir, category_name)
    os.makedirs(category_dir, exist_ok=True)
    # Generar el nombre del archivo
    file_extension = file.filename.split(".")[-1]
    sanitized_product_name = product_name.replace(" ", "_").lower()
    file_name = f"{sanitized_product_name}_{'front' if is_front else 'back'}.{file_extension}"
    file_path = os.path.join(category_dir, file_name)
    # Guardar el archivo
    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())
    # Devolver la ruta relativa
    relative_path = os.path.relpath(file_path, uploads_dir)
    return relative_path