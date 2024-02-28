from src.models import Department, db_session


class DepartmentManager:
    @staticmethod
    def create(data: dict):
        obj = Department(**data)
        db_session.add(obj)
        db_session.flush()
        db_session.refresh(obj)
        db_session.expunge_all()
        return obj

    @staticmethod
    def get_all():
        return db_session.query(Department).all()

    @staticmethod
    def get_by_id(department_id):
        return db_session.query(Department).filter_by(id=department_id).first()
