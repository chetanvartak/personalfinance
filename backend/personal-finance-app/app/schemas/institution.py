from pydantic import BaseModel, HttpUrl
from typing import Optional

from app.schemas.account import AccountTypeForAccount

# Nested schemas for relationships
class InstitutionTypeForInstitution(BaseModel):
    id: int
    name: str
    class Config:
        orm_mode = True

# Shared properties
class InstitutionBase(BaseModel):
    name: str
    institution_type_id: int
    website: Optional[HttpUrl] = None

# Properties to receive on item creation
class InstitutionCreate(InstitutionBase):
    pass

# Properties to receive on item update
class InstitutionUpdate(InstitutionBase):
    pass

# Properties shared by models stored in DB
class InstitutionInDBBase(InstitutionBase):
    id: int
    class Config:
        orm_mode = True

# Properties to return to client
class Institution(InstitutionInDBBase):
    pass

class InstitutionOut(InstitutionBase):
    id: int
    institution_type: Optional[InstitutionTypeForInstitution] = None
    class Config:
        orm_mode = True