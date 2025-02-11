from fastapi import APIRouter, HTTPException
from app.models import Student
from app.s3_utils import upload_student, get_student

router = APIRouter()


@router.post("/students/")
async def add_student(student: Student):
    """API to add student details"""
    response = upload_student(student.id, student.dict())
    if "error" in response:
        raise HTTPException(status_code=400, detail=response["error"])
    return response


@router.get("/students/{student_id}")
async def fetch_student(student_id: str):
    """API to get student details"""
    student_data = get_student(student_id)
    if "error" in student_data:
        raise HTTPException(status_code=404, detail=student_data["error"])
    return student_data
