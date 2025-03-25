from pydantic import BaseModel
from datetime import datetime
from app.enums.image_type_enum import ImageType

class ImageBase(BaseModel):
    path: str
    entity_id: int
    entity_type: str
    image_type: ImageType
    is_primary: bool = True

class ImageCreate(ImageBase):
    pass

class ImageResponse(ImageBase):    
    id: int
    created_at: datetime

    class Config:
        from_attributes = True