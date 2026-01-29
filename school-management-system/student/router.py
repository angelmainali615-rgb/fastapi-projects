from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from student.schema import StudentCreate
from student.service import create_student

router = APIRouter(prefix="/students", tags=["Students"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def add_student(student: StudentCreate, db: Session = Depends(get_db)):
    return create_student(db, student)
