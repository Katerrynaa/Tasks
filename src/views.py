from fastapi import APIRouter, HTTPException
from src.managers import DepartmentManager

router = APIRouter(prefix="/departments")


@router.post("/")
def create_item():
    DepartmentManager.insert_data(data=dict)
    return {"Data added successfully"}


@router.get("/", name="get_departments")
def read_depart():
    departments = DepartmentManager.insert_data(data=dict)
    if not departments:
        raise HTTPException(status_code=404, detail="Departments table not found")
    return departments


@router.get("/{department_id}")
def get_id(department_id: int):
    DepartmentManager.insert_data(data=dict)
    return {"department_id": department_id}
