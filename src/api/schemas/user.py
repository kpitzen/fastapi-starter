from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


class User(UserBase):
    class Config:
        orm_mode = True
