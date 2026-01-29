from sqlalchemy.orm import Session
from student.models import Student
from student.schema import StudentCreate

def create_student(db: Session, student: StudentCreate):
    student = Student(name=student.name,
                      teacher_id=student.teacher_id)
    db.add(student)
    db.commit()
    db.refresh(student)
    return student
