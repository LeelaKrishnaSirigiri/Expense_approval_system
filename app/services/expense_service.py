from sqlalchemy.orm import Session
from app.models.expense import Expense

def create_expense(db: Session, user_id: int, amount: float, category: str, description: str):
    expense = Expense(
        user_id=user_id,
        amount=amount,
        category=category,
        description=description
    )
    db.add(expense)
    db.commit()
    db.refresh(expense)
    return expense

def update_expense(db: Session, expense_id: int, amount: float, category: str, description: str):
    expense = db.query(Expense).filter(Expense.id == expense_id, Expense.status == "Pending").first()
    if not expense:
        return None
    expense.amount = amount
    expense.category = category
    expense.description = description
    db.commit()
    db.refresh(expense)
    return expense

def delete_expense(db: Session, expense_id: int):
    expense = db.query(Expense).filter(Expense.id == expense_id, Expense.status == "Pending").first()
    if not expense:
        return None
    db.delete(expense)
    db.commit()
    return True

def approve_reject_expense(db: Session, expense_id: int, status: str):
    expense = db.query(Expense).filter(Expense.id == expense_id, Expense.status == "Pending").first()
    if not expense:
        return None
    expense.status = status
    db.commit()
    db.refresh(expense)
    return expense