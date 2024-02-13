from src.models import Department, db_session


class DepartmentManager:
    @staticmethod
    def create(data: dict):
        session = db_session.get()
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
        return db_session.query(Department).filter_by(id=department_id).first()
