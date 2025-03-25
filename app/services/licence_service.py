import logging
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.models.licence_model import Licence
from app.schemas.licence_schema import LicenceCreate, LicenceUpdate

def create_licence(db:Session, licence:LicenceCreate):    
    try:       
        db_licence = Licence(**licence.dict())
        db.add(db_licence)
        db.commit()
        db.refresh(db_licence)   
        return db_licence
    except SQLAlchemyError as e:
        logging.error(f'Error creating Licence: {e}')
        db.rollback()
        raise ValueError('Error creating Licence. Please check the data provided.')
    except Exception as e:
        logging.error(f'Unexpected error: {e}')
        db.rollback()
        raise ValueError('An unexpected error occurred while creating the Licence.')    

def read_licence(db: Session, licence_id: int):
    return db.query(Licence).filter(Licence.id == licence_id).first()

def read_licences(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Licence).offset(skip).limit(limit).all()

def update_licence(db: Session, licence_id: int, licence: LicenceUpdate):
    db_licence = db.query(Licence).filter(Licence.id == licence_id).first()
    if db_licence:
        for key, value in licence.dict(exclude_unset=True).items():
            setattr(db_licence, key, value)
        db.commit()
        db.refresh(db_licence)
    return db_licence

def delete_licence(db: Session, licence_id: int):
    db_licence = db.query(Licence).filter(Licence.id == licence_id).first()
    if db_licence:
        db.delete(db_licence)
        db.commit()
    return db_licence