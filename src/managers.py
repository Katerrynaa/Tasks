from src.models import Department, SessionLocal


class DepartmentManager:
    @staticmethod
    def insert_data(data: dict):
        with SessionLocal() as session:
            session.add(Department(**data))

    @staticmethod
    def get_info():
        with SessionLocal() as session:
            return session.query(Department).all()

    @staticmethod
    def get_id(dep_id):
        with SessionLocal() as session:
            return session.query(Department).filter_by(id=dep_id).first()
