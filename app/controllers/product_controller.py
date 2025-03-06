import logging
from fastapi import HTTPException, status, UploadFile
from app.services import product_service, licence_service, category_service
from app.auth.jwt_handler import check_user
from app.schemas.product_schema import ProductCreate

def get_product(product_id, db):
    try:
        db_product = product_service.read_product(db, product_id)
        if db_product is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Product not found.')
        return db_product
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        logging.error(f'Error reading product: {e}')
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Internal server error.')
    
def get_products(db, skip, limit):
    try:
        products = product_service.read_products(db, skip=skip, limit=limit)
        return products
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        logging.error(f'Error reading products: {e}')
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Internal server error.')
    
def create_product(product_data: ProductCreate, front_image: UploadFile, back_image: UploadFile, db, user):
    check_user(user)
    print(product_data)
    try:
        db_licence = licence_service.read_licence(db, product_data.licence_id)
        if not db_licence:
            raise HTTPException(status_code=404, detail='Licence not found.')
        db_category = category_service.read_category(db, product_data.category_id)
        if not db_category:
            raise HTTPException(status_code=404, detail='Category not found.')
        licence_name = db_licence.name
        category_name = db_category.name
        product_name = product_data.name
        front_image_path = product_service.save_product_image(front_image, licence_name, category_name, product_name, is_front=True)
        back_image_path = product_service.save_product_image(back_image, licence_name, category_name, product_name, is_front=False)
        db_product = product_service.create_product(db, product_data, front_image_path, back_image_path)
        if db_product is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Error creating product.')
        return db_product
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        logging.error(f'Error creating product: {e}')
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Internal server error.')

def update_product(product_id, product_data, db, user):
    check_user(user)
    try:
        db_product = product_service.update_product(db, product_id, product_data)
        if db_product is None:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Error updating product.')
        return db_product
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        logging.error(f'Error updating product: {e}')
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Internal server error.')

def delete_product(product_id, db, user):
    check_user(user)
    try:
        success = product_service.delete_product(db, product_id)
        if not success:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Product not found.')
        return {'message': 'Product deleted successfully.'}
    except HTTPException as http_exc:
        raise http_exc
    except Exception as e:
        logging.error(f'Error deleting product: {e}')
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Internal server error.')