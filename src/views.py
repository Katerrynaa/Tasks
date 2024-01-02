from fastapi import APIRouter, HTTPException
from src.managers import DepartmentManager

router = APIRouter(prefix="/departments")


@router.post("/")
def create(department: dict):
    DepartmentManager.create(data=department)
    return {"Data added successfully"}


@router.get("/", name="get_departments")
def get_all():
    return DepartmentManager.get_all()


@router.get("/{dep_id}")
def get_by_id(dep_id: int):
    if not (department := DepartmentManager.get_by_id(dep_id)):
        raise HTTPException(status_code=404, detail="Department with such id not found")
    return department
