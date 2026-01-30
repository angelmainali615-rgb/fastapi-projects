from sqlalchemy.orm import Session
from app.models.expense import Expense

def create_expense(db: Session, expense: Expense):
    db.add(expense)
    db.commit()
    db.refresh(expense)
    return expense

def get_all_expenses(db: Session):
    return db.query(Expense).all()

def get_total_by_category(db: Session):
    from sqlalchemy import func
    return (
        db.query(Expense.category, func.sum(Expense.amount))
        .group_by(Expense.category)
        .all()
    )
