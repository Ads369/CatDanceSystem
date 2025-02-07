from pydantic import BaseModel, EmailStr


class DancerBase(BaseModel):
    username: str
    email: EmailStr


class DancerCreate(DancerBase):
    password: str


class DancerResponse(DancerBase):
    id: int

    class Config:
        from_attributes = True
