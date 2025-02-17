from pydantic import BaseModel


class Student(BaseModel):
    id: str
    name: str
    age: int
    department: str
    area: str
    state: str
