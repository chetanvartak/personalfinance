from pydantic import BaseModel, Field
from typing import Optional


class AccountBase(BaseModel):
    user_id: int
    name: str
    balance: float = Field(default=0.0)


class AccountCreate(AccountBase):
    pass


class AccountUpdate(BaseModel):
    name: Optional[str] = None
    balance: Optional[float] = None


class AccountOut(AccountBase):
    id: int

    class Config:
        orm_mode = True
