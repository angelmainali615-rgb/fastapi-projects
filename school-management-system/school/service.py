from sqlalchemy.orm import Session
from school.models import School
from school.schema import SchoolCreate

def create_school(db: Session, school: SchoolCreate):
    new_school = School(
        name=school.name,
        address=school.address
    )
    db.add(new_school)
    db.commit()
    db.refresh(new_school)
    return new_school


