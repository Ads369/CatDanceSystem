# backend/app/models.py
from typing import Optional

from sqlmodel import Field, SQLModel


class DancerBase(SQLModel):
    name: str
    category: str  # junior/senior
    gender: str  # male/female


class Dancer(DancerBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class DancerCreate(DancerBase):
    pass


class DancerRead(DancerBase):
    id: int
