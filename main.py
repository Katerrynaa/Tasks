from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, Session, declarative_base

DATABASE_URL = "mysql+mysqlconnector://root:rootroot11@localhost:3306/departments"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200))
    country_name = Column(String(100))


Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def insert_data(db: Session):
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


@app.put("/departments")
def push_info():
    with SessionLocal() as session:
        insert_data(session)
        return {"Data added successfully"}


@app.get("/departments")
def read_depart(db: Session = Depends(get_db)):
    departments = db.query(Department).all()
    if not departments:
        raise HTTPException(status_code=404, detail="Departments table not found")
    return departments


@app.get("departments/{department_id}")
def get_id(department_id: int, db: Session = Depends(get_db)):
    departments = db.query(Department).filter(Department.id == department_id).all()
    return {"department_id": department_id}
