from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app.models.expense import Base, Expense
from app.schemas.expense import ExpenseCreate, ExpenseOut
from app.services.expense_service import (
    create_expense,
    get_all_expenses,
    get_total_by_category
)

router = APIRouter(prefix="/expenses", tags=["Expenses"])

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ExpenseOut)
def add_expense(expense: ExpenseCreate, db: Session = Depends(get_db)):
    db_expense = Expense(**expense.dict())
    return create_expense(db, db_expense)

@router.get("/", response_model=list[ExpenseOut])
def read_expenses(db: Session = Depends(get_db)):
    return get_all_expenses(db)

@router.get("/summary")
def category_summary(db: Session = Depends(get_db)):
    return get_total_by_category(db)
