from fastapi import APIRouter, HTTPException, Path, Query
from src.managers import DepartmentManager
from typing import Annotated, Optional

router = APIRouter(prefix="/departments")


@router.post("/", status_code=201)
def create(department: dict[str, str]):
    DepartmentManager.create(data=department)
    return "Data added successfully"


@router.get("/", name="get_departments")
def get_all(title: Optional[str] = Query(None), country_name: Optional[str] = Query(None)):
    return DepartmentManager.get_all()


@router.get("/{department_id}")
def get_by_id(department_id: Annotated[int, Path(title="The ID of the department item")]):
    if not (department := DepartmentManager.get_by_id(department_id)):
        raise HTTPException(status_code=404, detail="Department with such id not found")
    return department



