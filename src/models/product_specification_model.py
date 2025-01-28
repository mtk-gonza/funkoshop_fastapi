from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from src.models.database import Base

class ProductSpecification(Base):
    __tablename__ = 'product_specification'
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('product.id'), nullable=True)
    name = Column(String(60), nullable=False)
    value = Column(String(255), nullable=False)
    createdAt = Column(DateTime, server_default=func.now(), nullable=False)
    updatedAt = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)

    product = relationship('Product', back_populates='specifications')