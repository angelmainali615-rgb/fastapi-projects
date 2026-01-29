from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from .schema import SchoolCreate
from .service import create_school

router = APIRouter(prefix="/schools", tags=["Schools"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def add_school(school: SchoolCreate, db: Session = Depends(get_db)):
    return create_school(db, school)
