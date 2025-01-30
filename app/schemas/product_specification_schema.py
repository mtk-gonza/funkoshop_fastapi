from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ProductSpecificationBase(BaseModel):
    name: str
    value: str 

class ProductSpecificationCreate(ProductSpecificationBase):
    product_id: int

class ProductSpecificationUpdate(ProductSpecificationBase):
    product_id: int

class ProductSpecificationResponse(ProductSpecificationBase):
    id: int
    createdAt: datetime
    updatedAt: datetime
    product_id: int
    class Config:
        from_attributes = True

class ProductSpecificationDelete(BaseModel):
    message: str