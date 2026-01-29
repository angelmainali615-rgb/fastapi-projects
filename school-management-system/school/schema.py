from pydantic import BaseModel

class SchoolCreate(BaseModel):
    name: str
    address: str
