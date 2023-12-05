from src.models import Department, SessionLocal


class DepartmentManager:
    @staticmethod
    def create(data: dict):
        with SessionLocal() as session:
            session.add(Department(**data))

    @staticmethod
    def get_all():
        with SessionLocal() as session:
            return session.query(Department).all()

    @staticmethod
    def get_by_id(department_id):
        with SessionLocal() as session:
            return session.query(Department).filter_by(id=department_id).first()
