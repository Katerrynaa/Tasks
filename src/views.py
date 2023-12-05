from fastapi import APIRouter, HTTPException
from src.managers import DepartmentManager

router = APIRouter(prefix="/departments")


@router.post("/")
def create_department(department: dict):
    DepartmentManager.insert_data(data=department)
    return {"Data added successfully"}


@router.get("/", name="get_departments")
def read_departments():
    return DepartmentManager.get_info()


@router.get("/{dep_id}")
def get_department(dep_id: int):
    if not (department := DepartmentManager.get_id(dep_id)):
        raise HTTPException(status_code=404, detail="Departments id table not found")
    return department
