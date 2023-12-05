from fastapi import APIRouter, HTTPException
from src.managers import DepartmentManager

router = APIRouter(prefix="/departments")


@router.post("/")
def create_item(department: dict):
    DepartmentManager.insert_data(data=department)
    return {"Data added successfully"}


@router.get("/", name="get_departments")
def read_depart():
    department = DepartmentManager.get_info()
    return department


@router.get("/{dep_id}")
def get_id(dep_id: int):
    department = DepartmentManager.get_id(dep_id)
    if not department:
        raise HTTPException(status_code=404, detail="Departments table not found")
    return department
