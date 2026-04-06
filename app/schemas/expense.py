from pydantic import BaseModel, Field

class ExpenseCreate(BaseModel):
    user_id: int
    amount: float = Field(..., gt=0)
    category: str
    description: str

class ExpenseUpdate(BaseModel):
    amount: float = Field(..., gt=0)
    category: str
    description: str

class ExpenseStatusUpdate(BaseModel):
    status: str  # "Approved" or "Rejected"