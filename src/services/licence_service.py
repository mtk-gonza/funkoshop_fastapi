from sqlalchemy.orm import Session
from src.models.licence_model import Licence
from src.schemas.category_schema import CategoryCreate, CategoryUpdate

def create_licence(db:Session, licence:CategoryCreate):
    db_licence = Licence(**licence.dict())
    db.add(db_licence)
    db.commit()
    db.refresh(db_licence)
    return db_licence

def read_licence(db: Session, licence_id: int):
    return db.query(Licence).filter(Licence.id == licence_id).first()

def read_clicences(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Licence).offset(skip).limit(limit).all()

def update_licence(db: Session, licence_id: int, licence: CategoryUpdate):
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