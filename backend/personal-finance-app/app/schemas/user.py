from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date
from datetime import datetime
from sqlalchemy import Column, String

class UserBase(BaseModel):
    username: str
    email: EmailStr
    password_hash: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    date_of_birth:  Optional[date] = None



class UserCreate(UserBase):
    pass

class UserOut(UserBase):
    id: int
    created_at:  Optional[datetime] = None
    updated_at:  Optional[datetime] = None
    class Config:
        orm_mode = True
