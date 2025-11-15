from pydantic import BaseModel
from typing import Optional
from decimal import Decimal
from datetime import datetime

# Shared properties
class TransactionBase(BaseModel):
    date: datetime
    amount: Decimal
    account_id: int
    category_id: Optional[int] = None
    currency: Optional[str] = None
    description: Optional[str] = None
    transaction_type_id: int
    related_account_id: Optional[int] = None

# Properties to receive on item creation
class TransactionCreate(TransactionBase):
    account_id: int

# Properties to receive on item update
class TransactionUpdate(TransactionBase):
    pass

# Properties shared by models stored in DB
class TransactionInDBBase(TransactionBase):
    id: int
    account_id: int
    class Config:
        orm_mode = True

# Properties to return to client
class Transaction(TransactionInDBBase):
    pass

class TransactionOut(TransactionBase):
    id: int
    created_at:  Optional[datetime] = None    
    class Config:
        orm_mode = True
