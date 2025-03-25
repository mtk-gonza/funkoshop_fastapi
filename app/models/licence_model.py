from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship
from app.database.database import Base

class Licence(Base):
    __tablename__ = 'licence'    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(60), nullable=False)
    description = Column(String(255), nullable=False)
    createdAt = Column(DateTime, server_default=func.now(), nullable=False)
    updatedAt = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)
    
    images = relationship(
        "Image",
        primaryjoin="and_(Licence.id == Image.entity_id, Image.entity_type == 'licence')",
        foreign_keys="[Image.entity_id]",
        overlaps="product_images",
        viewonly=True
    )
    products = relationship('Product', back_populates='licence')