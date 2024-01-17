from fastapi import APIRouter, HTTPException, Request
from src.managers import DepartmentManager

router = APIRouter(prefix="/departments")


@router.post("/", status_code=201)
def create(department: dict):
    DepartmentManager.create(data=department)
    return "Data added successfully"

@router.middleware("http")
async def print_hello(request: Request, call_next):
    print("Hello")
    response = await call_next(request)
    return response 

@router.get("/", name="get_departments")
def get_all():
    return DepartmentManager.get_all()

@router.middleware("http")
async def print_goodbye(request: Request, call_next):
    print("Goodbye")
    response = await call_next(request)
    return response

@router.get("/{department_id}")
def get_by_id(department_id: int):
    if not (department := DepartmentManager.get_by_id(department_id)):
        raise HTTPException(status_code=404, detail="Department with such id not found")
    return department
