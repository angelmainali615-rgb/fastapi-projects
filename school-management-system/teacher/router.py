from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from teacher.schema import TeacherCreate
from teacher.service import create_teacher

router = APIRouter(prefix="/teachers", tags=["Teachers"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def add_teacher(teacher: TeacherCreate, db: Session = Depends(get_db)):
    return create_teacher(db, teacher.name)
