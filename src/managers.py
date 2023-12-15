from src.models import Department, SessionLocal, db_connect, db_disconnect


class DepartmentManager:
    @staticmethod
    def create(data: dict):
        with SessionLocal() as session:
            with session.begin():
                obj = Department(**data)
                session.add(obj)
                session.flush()
                session.refresh(obj)

    @staticmethod
    def get_all():
        with SessionLocal() as session:
            return session.query(Department).all()

    @staticmethod
    def get_by_id(department_id):
        with SessionLocal() as session:
            return session.query(Department).filter_by(id=department_id).first()
