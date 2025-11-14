from pydantic import BaseModel
from typing import Optional
from decimal import Decimal
from datetime import date

# Shared properties
class AccountBase(BaseModel):
    account_name: Optional[str] = None
    account_number_last4: Optional[str] = None
    balance: Optional[Decimal] = Decimal('0.00')
    opened_date: Optional[date] = None
    currency: Optional[str] = 'USD'
    status: Optional[str] = 'active'
    institution_id: int
    account_type_id: int

# Properties to receive on item creation
class AccountCreate(AccountBase):
    user_id: int

# Properties to receive on item update
class AccountUpdate(AccountBase):
    pass

# Properties shared by models stored in DB
class AccountInDBBase(AccountBase):
    id: int
    user_id: int
    class Config:
        orm_mode = True

# Properties to return to client
class Account(AccountInDBBase):
    pass

class AccountOut(AccountBase):
    id: int

    class Config:
        orm_mode = True