from pydantic import BaseModel
from typing import List, Optional
from decimal import Decimal
from datetime import datetime

# Nested schemas for relationships
class AccountForMerchant(BaseModel):
    id: int
    account_name: str
    class Config:
        orm_mode = True

class CategoryForMerchant(BaseModel):
    id: int
    name: str
    class Config:
        orm_mode = True

# Shared properties
class MerchantBase(BaseModel):
    merchant_name: str
    default_category_id: Optional[int] = None
    default_account_id: Optional[int] = None

# Properties to receive on item creation
class MerchantCreate(MerchantBase):
    pass

# Properties to receive on item update
class MerchantUpdate(MerchantBase):
    pass

# Properties shared by models stored in DB
class MerchantInDBBase(MerchantBase):
    id: int
    class Config:
        orm_mode = True

# Properties to return to client
class Merchant(MerchantInDBBase):
    pass

class MerchantBaseOut(MerchantBase):
    id: int
    created_at:  Optional[datetime] = None 
    updated_at:  Optional[datetime] = None
    default_account: Optional[AccountForMerchant] = None
    default_category: Optional[CategoryForMerchant] = None

class MerchantOut(MerchantBaseOut):

    class Config:
        orm_mode = True

class MerchantListFiltered(BaseModel):
    merchants: List[MerchantBaseOut]
    total: int
    page: int
    page_size: int

    class Config:
        orm_mode = True    

class MerchantDescriptionBase(BaseModel):
    merchant_id: int
    description: str

class MerchantDescriptionCreate(MerchantDescriptionBase):
    pass

class MerchantDescriptionUpdate(MerchantDescriptionBase):
    pass

class MerchantDescriptionInDBBase(MerchantDescriptionBase):
    id: int
    class Config:
        orm_mode = True

class MerchantDescription(MerchantDescriptionInDBBase):
    pass     