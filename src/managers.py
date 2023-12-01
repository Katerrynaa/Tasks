from src.models import Department, SessionLocal


class DepartmentManager:
    @staticmethod
    def insert_data(data: dict):
        with SessionLocal() as session:
            session.add(Department(**data))
