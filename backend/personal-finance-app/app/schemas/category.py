from typing import Optional
from pydantic import BaseModel

# Shared properties
class CategoryBase(BaseModel):
    name: str
    parent_id: Optional[int] = None


# Properties to receive on item creation
class CategoryCreate(CategoryBase):
    pass

# Properties to receive on item update
class CategoryUpdate(CategoryBase):
    pass

# Properties shared by models stored in DB
class CategoryInDBBase(CategoryBase):    
    id: int
    class Config:
        orm_mode = True

# Properties to return to client
class Category(CategoryInDBBase):
    pass

class CategoryOut(CategoryBase):
    id: int

    class Config:
        orm_mode = True
