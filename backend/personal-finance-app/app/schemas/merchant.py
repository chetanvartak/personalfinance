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
    # Optional list of merchant descriptions to create together with the merchant
    descriptions: Optional[List["MerchantDescriptionCreate"]] = None

# Properties to receive on item update
class MerchantUpdate(MerchantBase):
    # Optional list of merchant descriptions to create/update together with the merchant
    descriptions: Optional[List["MerchantDescriptionCreate"]] = None

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
    descriptions: Optional[List["MerchantDescription"]] = None

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

# Resolve forward references for Pydantic models that reference each other by string
MerchantCreate.update_forward_refs()
MerchantUpdate.update_forward_refs()
MerchantBaseOut.update_forward_refs()
MerchantOut.update_forward_refs()
MerchantDescriptionCreate.update_forward_refs()
MerchantDescription.update_forward_refs()