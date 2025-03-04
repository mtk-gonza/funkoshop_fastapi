from sqlalchemy import Column, Integer, String, Boolean, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship
from app.database.database import Base
from app.models.user_roles_model import user_roles
from app.enums.roles_enum import Roles

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(20), unique=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    first_name = Column(String(50))
    last_name = Column(String(50))
    telefono = Column(String(50))
    is_active = Column(Boolean, default=True)
    createdAt = Column(DateTime, default=func.now())
    updatedAt = Column(DateTime, default=func.now(), onupdate=func.now())

    roles = relationship('Role', secondary=user_roles, back_populates='users')