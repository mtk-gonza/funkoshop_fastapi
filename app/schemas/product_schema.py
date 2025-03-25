from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from app.schemas.licence_schema import LicenceResponse
from app.schemas.category_schema import CategoryResponse
from app.schemas.image_schema import ImageResponse
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
    images: Optional[List[ImageResponse]]
    licence_id: Optional[int]
    category_id: Optional[int]
    specifications : Optional[List[ProductSpecificationCreate]] = []

class ProductCreate(BaseModel):
    name: str
    description: Optional[str]
    price: float
    stock: Optional[int]
    discount: Optional[float]
    sku: str
    dues: Optional[int]
    special: Optional[bool]
    licence_id: int
    category_id: int

class ProductUpdate(ProductBase):
    pass
class ProductResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
    price: float
    stock: Optional[int]
    discount: Optional[float]
    sku: str
    dues: Optional[int]
    special: Optional[bool]
    licence_id: int
    licence: LicenceResponse
    category_id: int
    category: CategoryResponse
    images: Optional[List[ImageResponse]] = []
    specifications: Optional[List[ProductSpecificationResponse]] = []
    createdAt: datetime
    updatedAt: datetime
    class Config:
        from_attributes = True

class ProductDelete(BaseModel):
    message: str