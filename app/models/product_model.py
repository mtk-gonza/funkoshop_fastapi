from sqlalchemy import Column, Integer, String, DECIMAL, Boolean, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from app.database.database import Base

class Product(Base):
    __tablename__ = 'product'    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(60), nullable=False)
    description = Column(String(255), nullable=True)
    price = Column(DECIMAL(10, 2), nullable=False, default=0.00)
    stock = Column(Integer, nullable=True)
    discount = Column(DECIMAL(5, 2), default=0.00)
    sku = Column(String(50), nullable=False, unique=True)
    dues = Column(Integer, default=0)
    special = Column(Boolean, default=False)
    image_front = Column(String(255), nullable=True)
    image_back = Column(String(255), nullable=True)
    licence_id = Column(Integer, ForeignKey('licence.id'), nullable=True)
    category_id = Column(Integer, ForeignKey('category.id'), nullable=True)
    createdAt = Column(DateTime, server_default=func.now(), nullable=False)
    updatedAt = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)

    licence = relationship('Licence', back_populates='products')
    category = relationship('Category', back_populates='products')
    specifications = relationship('ProductSpecification', back_populates='product')