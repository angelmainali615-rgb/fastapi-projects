from pydantic import BaseModel

class StudentCreate(BaseModel):
    name: str
    teacher_id: int