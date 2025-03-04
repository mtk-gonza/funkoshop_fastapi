from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime
from app.schemas.role_schema import RoleResponse
from app.enums.roles_enum import Roles

class UserBase(BaseModel):
    username: str
    email: str
    password: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    telefono: Optional[str] = None
    is_active: bool

class UserCreate(UserBase):
    pass
class UserUpdate(UserBase):
    pass

class UserResponse(BaseModel):
    id: int
    email: str
    username: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    telefono: Optional[str] = None
    is_active: bool
    roles: List[RoleResponse] = []
    createdAt: datetime
    updatedAt: datetime
    class Config:
        from_attributes = True

class UserDelete(BaseModel):
    message: str