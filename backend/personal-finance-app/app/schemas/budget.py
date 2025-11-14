from pydantic import BaseModel

class BudgetOut(BaseModel):
    id: int
    user_id: int
    name: str
    limit_amount: float

    class Config:
        orm_mode = True
