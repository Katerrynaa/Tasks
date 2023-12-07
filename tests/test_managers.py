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
