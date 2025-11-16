from pydantic import BaseModel
from typing import List, Optional
from decimal import Decimal
from datetime import datetime

# Nested schemas for relationships
class TransactionTypeForTransaction(BaseModel):
    id: int
    name: str
    class Config:
        orm_mode = True

class AccountForTransaction(BaseModel):
    id: int
    account_name: str
    class Config:
        orm_mode = True

class RelatedAccountForTransaction(BaseModel):
    id: int
    account_name: str
    class Config:
        orm_mode = True

class CategoryForTransaction(BaseModel):
    id: int
    name: str
    class Config:
        orm_mode = True

# Shared properties
class TransactionBase(BaseModel):
    date: datetime
    amount: Decimal
    account_id: int
    category_id: Optional[int] = None
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

class TransactionBaseOut(TransactionBase):
    id: int
    created_at:  Optional[datetime] = None    
    account: Optional[AccountForTransaction] = None
    category: Optional[CategoryForTransaction] = None
    transaction_type: Optional[TransactionTypeForTransaction] = None
    related_account: Optional[RelatedAccountForTransaction] = None

class TransactionOut(TransactionBaseOut):

    class Config:
        orm_mode = True

class TransactionListFiltered(BaseModel):
    transactions: List[TransactionBaseOut]
    total: int
    page: int
    page_size: int

    class Config:
        orm_mode = True    