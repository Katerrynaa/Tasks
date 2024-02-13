from src.models import Department, SessionLocal, db_session


class DepartmentManager:
    @staticmethod
    def create(data: dict):
        with SessionLocal() as session:
            with session.begin():
                obj = Department(**data)
                session.add(obj)
                session.flush()
                session.refresh(obj)
                session.expunge_all()
                return obj

    @staticmethod
    def get_all():
        return db_session.query(Department).all()

    @staticmethod
    def get_by_id(department_id):
        with SessionLocal() as session:
            return session.query(Department).filter_by(id=department_id).first()
