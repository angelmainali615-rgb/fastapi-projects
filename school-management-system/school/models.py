from sqlalchemy import Column, Integer, String
from database import Base

class School(Base):
    __tablename__ = "schools"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
