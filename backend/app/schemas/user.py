from typing import List, Optional

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    name: str
    gender: str
    level: str
    email: EmailStr


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int

    class Config:
        from_attributes = True


class UserUpdate(BaseModel):
    name: Optional[str] = None
    gender: Optional[str] = None
    level: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
