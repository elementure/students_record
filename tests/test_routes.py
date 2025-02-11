from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_add_student():
    student_data = {
        "id": "101",
        "name": "John Doe",
        "age": 22,
        "department": "Computer Science"
    }
    response = client.post("/students/", json=student_data)
    assert response.status_code == 200
    assert response.json()["message"] == "Student data uploaded successfully"


def test_fetch_student():
    student_id = "101"
    response = client.get(f"/students/{student_id}")
    assert response.status_code == 200
    assert "name" in response.json()
