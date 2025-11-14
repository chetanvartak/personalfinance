from pydantic import BaseModel
from datetime import datetime

class TransactionOut(BaseModel):
    id: int
    account_id: int
    category: str
    amount: float
    currency: str
    created_at: datetime

    class Config:
        orm_mode = True
