from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from sqlalchemy.orm import relationship
from app.database.database import Base

class Image(Base):
    __tablename__ = "image"
    
    id = Column(Integer, primary_key=True, index=True)
    path = Column(String(255), nullable=False)
    entity_type = Column(String(50), nullable=False)
    entity_id = Column(Integer, nullable=False)
    image_type = Column(String(50))
    is_primary = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)