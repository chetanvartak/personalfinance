from pydantic import BaseModel, AnyUrl
from typing import Optional


class InstitutionBase(BaseModel):
    name: str
    type: Optional[str] = None
    website: Optional[AnyUrl] = None


class InstitutionCreate(InstitutionBase):
    pass


class InstitutionOut(InstitutionBase):
    id: int

    class Config:
        orm_mode = True
