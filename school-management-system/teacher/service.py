from sqlalchemy.orm import Session
from teacher.models import Teacher

def create_teacher(db: Session, name: str):
    teacher = Teacher(name=name)
    db.add(teacher)
    db.commit()
    db.refresh(teacher)
    return teacher
