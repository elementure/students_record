from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Student Management API", version="1.0")

app.include_router(router)


@app.get("/")
def root():
    return {"message": "Welcome to Student Management API"}
