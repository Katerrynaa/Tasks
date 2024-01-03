from pytest import fixture
from sqlalchemy import select

from src.managers import DepartmentManager
from src.models import Department, SessionLocal


class TestCreateDepartment:
    @fixture(scope="class", autouse=True)
    def create(self, department_data):
        return DepartmentManager.create(department_data)

    def test_create(self, department_data):
        query = (
            select(1)
            .select_from(Department)
            .where(
                Department.title == department_data["title"],
                Department.country_name == department_data["country_name"],
            )
            .exists()
            .select()
        )
        with SessionLocal() as session:
            assert session.execute(query).scalar()


class TestGetDepartment:
    @fixture(scope="class")
    def department_1(self, department_data):
        return DepartmentManager.create(department_data)
    
    @fixture(scope="class")
    def department_2(self, new_department_data):
        return DepartmentManager.create(new_department_data)
    
    @fixture(scope="class", autouse=True)
    def get_all(self):
        return DepartmentManager.get_all()
    
    def test_amount(self, get_all):
        assert len(get_all) == 2
    
    def test_title_department(self, get_all, department_1):
        for department in get_all:
            assert department.title == department_1.title
    
    def test_country_department(self, get_all, department_1):
        for department in get_all:
            assert department.country_name == department_1.country_name
    


class TestDepartmentId:
    @fixture(scope="class")
    def department(self, department_data):
        return DepartmentManager.create(department_data)

    @fixture(scope="class", autouse=True)
    def get_by_id(self, department):
        return DepartmentManager.get_by_id(department.id)

    def test_id(self, get_by_id, department):
        assert get_by_id.id == department.id

    def test_title(self, get_by_id, department_data):
        assert get_by_id.title == department_data["title"]

    def test_country_name(self, get_by_id, department_data):
        assert get_by_id.country_name == department_data["country_name"]
