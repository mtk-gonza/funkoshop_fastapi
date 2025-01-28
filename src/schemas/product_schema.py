from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from src.schemas.licence_schema import LicenceResponse
from src.schemas.category_schema import CategoryResponse
from src.schemas.product_specification_schema import ProductSpecificationResponse, ProductSpecificationCreate

class ProductBase(BaseModel):
    name: str
    description: Optional[str]
    price: float
    stock: Optional[int]
    discount: Optional[float]
    sku: str
    dues: Optional[int]
    special: Optional[bool]
    image_front: Optional[str]
    image_back: Optional[str]

class ProductCreate(ProductBase):
    licence_id: Optional[int]
    category_id: Optional[int]
    specifications : Optional[List[ProductSpecificationCreate]] = []

class ProductUpdate(ProductBase):
    licence_id: Optional[int]
    category_id: Optional[int]
    specifications : Optional[List[ProductSpecificationCreate]] = []

class ProductResponse(ProductBase):
    id: int
    licence: Optional[LicenceResponse]
    category: Optional[CategoryResponse]
    specifications : List[ProductSpecificationResponse]
    image_front: Optional[str]
    image_back: Optional[str]
    createdAt: datetime
    updatedAt: datetime
    class Config:
        from_attributes = True

class ProductDelete(BaseModel):
    message: str