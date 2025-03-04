from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from app.schemas.licence_schema import LicenceResponse
from app.schemas.category_schema import CategoryResponse
from app.schemas.product_specification_schema import ProductSpecificationResponse, ProductSpecificationCreate

class ProductBase(BaseModel):
    name: str
    description: Optional[str]
    price: float
    stock: Optional[int]
    discount: Optional[float]
    sku: str
    dues: Optional[int]
    special: Optional[bool]
    licence_id: Optional[int]
    category_id: Optional[int]
    image_front: Optional[str] = None
    image_back: Optional[str] = None
    specifications : Optional[List[ProductSpecificationCreate]] = []

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass
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