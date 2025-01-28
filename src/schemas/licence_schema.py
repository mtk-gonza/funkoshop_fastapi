from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class LicenceBase(BaseModel):
    name: str
    description: Optional[str]
    image: Optional[str]

class LicenceCreate(LicenceBase):
    pass

class LicenceUpdate(BaseModel):
    pass

class LicenceResponse(LicenceBase):
    id: int 
    createdAt: datetime 
    updatedAt: datetime 
    class Config:
        from_attributes = True