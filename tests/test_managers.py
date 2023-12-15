from pytest import fixture

from src.managers import DepartmentManager
from src.models import Department


class TestCreateDepartment:
    @fixture(scope="class", autouse=True)
    def create(self, department_data):
        return DepartmentManager.create(department_data)

    def test_create(self, department_data, test_session):
        test_session.query(Department).where(
            Department.title == department_data["title"],
            Department.country_name == department_data["country_name"],
        ).exists()


class TestGetDepartment:
    @fixture(scope="class", autouse=True)
    def get_all(self):
        return DepartmentManager.get_all()
    
    def test_get_all(self, test_session):
        test_session.query(Department).all().exists()


class TestIdDepartment:
    @fixture(scope="class", autouse=True)
    def get_by_id(self, department_id):
        return DepartmentManager.get_by_id(department_id)
    
    def test_get_by_id(self, test_session, department_id):
        test_session.query(Department).filter(
            Department.id == department_id["id"],
        ).exists().first()
