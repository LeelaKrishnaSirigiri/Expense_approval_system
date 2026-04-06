from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.expense import ExpenseCreate, ExpenseUpdate, ExpenseStatusUpdate
from app.services.expense_service import create_expense, update_expense, delete_expense, approve_reject_expense
from app.models.expense import Expense

router = APIRouter()

# DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create Expense
@router.post("/expenses")
def add_expense(expense: ExpenseCreate, db: Session = Depends(get_db)):
    return create_expense(db, expense.user_id, expense.amount, expense.category, expense.description)

# Update Expense
@router.put("/expenses/{expense_id}")
def modify_expense(expense_id: int, expense: ExpenseUpdate, db: Session = Depends(get_db)):
    updated = update_expense(db, expense_id, expense.amount, expense.category, expense.description)
    if not updated:
        raise HTTPException(status_code=400, detail="Expense not found or already processed")
    return updated

# Delete Expense
@router.delete("/expenses/{expense_id}")
def remove_expense(expense_id: int, db: Session = Depends(get_db)):
    result = delete_expense(db, expense_id)
    if not result:
        raise HTTPException(status_code=400, detail="Expense not found or already processed")
    return {"detail": "Expense deleted successfully"}

# Approve/Reject Expense
@router.patch("/expenses/{expense_id}/status")
def change_status(expense_id: int, status_update: ExpenseStatusUpdate, db: Session = Depends(get_db)):
    if status_update.status not in ["Approved", "Rejected"]:
        raise HTTPException(status_code=400, detail="Status must be Approved or Rejected")
    updated = approve_reject_expense(db, expense_id, status_update.status)
    if not updated:
        raise HTTPException(status_code=400, detail="Expense not found or already processed")
    return updated
# Get all expenses
@router.get("/expenses")
def get_expenses(db: Session = Depends(get_db)):
    return db.query(Expense).all()