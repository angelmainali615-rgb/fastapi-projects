from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database import Base

class Teacher(Base):
    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    students = relationship("Student", back_populates="teacher")