from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Annotated
from functools import wraps
from app.database.database import get_db
from app.auth.jwt_handler import get_current_user

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]