from fastapi import Depends, HTTPException, APIRouter
# from sqlalchemy.orm import session
from src.models import SessionLocal
from src.models import Department

router = APIRouter(prefix="/departments")


def insert_data(db):
    # todo: move it to managers.py
    #  get data from request body (remove hardcoded values)
    #  Department manager should be a separate class (DepartmentManager.insert_data(body))
    #  remove session from this file
    department_data = [
        {"title": "HR", "country_name": "Norway"},
        {"title": "IT Support", "country_name": "Sweden"},
        {"title": "Achitecture", "country_name": "Poland"},
        {"title": "Sales", "country_name": "USA"},
    ]

    for data in department_data:
        department = Department(**data)
        db.add(department)
        db.commit()


@router.post("/")
def push_info(*args, **kwargs):  # rename method please
    print("Hey there")
    print(args)
    print(kwargs)
    # DepartmentManager.insert_data(body)
    # with SessionLocal() as session:
    #     insert_data(session)
    #     return {"Data added successfully"}


# @router.get("/", name="get_departments")
# def read_depart(db: Session = Depends(get_db)):
#     departments = db.query(Department).all()
#     if not departments:
#         raise HTTPException(status_code=404, detail="Departments table not found")
#     return departments


# @router.get("/{department_id}")
# def get_id(department_id: int, db: Session = Depends(get_db)):
#     departments = db.query(Department).filter(Department.id == department_id).all()
#     return {"department_id": departments}
