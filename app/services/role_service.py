from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.models.role_model import Role
from app.schemas.role_schema import RoleCreate, RoleUpdate
import logging

def create_role(db: Session, role_data:RoleCreate):
    try:
        db_role = Role(**role_data.dict())
        db.add(db_role)
        db.commit()
        db.refresh(db_role)
        return db_role
    except SQLAlchemyError as e:
        logging.error(f'Error creating role: {e}')
        db.rollback()
        return None

def read_role(db: Session, role_id: int):
    try:
        return db.query(Role).filter(Role.id == role_id).first()
    except SQLAlchemyError as e:
        logging.error(f'Error reading role: {e}')
        return None

def read_roles(db: Session):
    try:
        return db.query(Role).all()
    except SQLAlchemyError as e:
        logging.error(f'Error reading roles: {e}')
        return None

def update_role(db: Session, role_id: int, role: RoleUpdate):
    try:
        db_role = db.query(Role).filter(Role.id == role_id).first()
        if db_role:
            for key, value in role.dict(exclude_unset=True).items():
                setattr(db_role, key, value)
            db.commit()
            db.refresh(db_role)
        return db_role
    except SQLAlchemyError as e:
        logging.error(f'Error updating role: {e}')
        db.rollback()
        return None    

def delete_role(db: Session, role_id: int):
    try:
        db_role = db.query(Role).filter(Role.id == role_id).first()
        if db_role:
            db.delete(db_role)
            db.commit()
        return db_role
    except SQLAlchemyError as e:
        logging.error(f'Error deleting role: {e}')
        db.rollback()
        return None    