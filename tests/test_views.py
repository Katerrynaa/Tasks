from unittest.mock import patch

from pytest import fixture

from src.managers import DepartmentManager
from src.models import Department


class TestCreateDepartmentView:
    @fixture(scope="class")
    def manager_create_mock(self, department_data):
        with patch.object(DepartmentManager, "create") as mock:
            mock.return_value = Department(**department_data)
            yield mock

    @fixture(scope="class", autouse=True)
    def create_department(self, test_client, manager_create_mock, department_data):
        return test_client.post("/departments", json=department_data)

    def test_manager_called(self, manager_create_mock, department_data):
        manager_create_mock.assert_called_once_with(data=department_data)

    def test_result(self, create_department):
        assert create_department.json() == "Data added successfully"

    def test_status_code(self, create_department):
        assert create_department.status_code == 201


class TestGetDepartmentsView:
    @fixture(scope="class")
    def manager_get_all_mock(self):
        with patch.object(DepartmentManager, "get_all") as mock:
            yield mock

    @fixture(scope="class", autouse=True)
    def get_all_department(self, test_client, manager_get_all_mock):
        return test_client.get("/departments")

    def test_manager_called(self, manager_get_all_mock):
        manager_get_all_mock.assert_called_once_with()

    def test_result(self, get_all_department):
        assert get_all_department.json() == {}

    def test_status_code(self, get_all_department):
        assert get_all_department.status_code == 200


class TestGetDepartmentView:
    department_id = 1

    @fixture(scope="class")
    def manager_get_by_id_mock(self, department_data):
        with patch.object(DepartmentManager, "get_by_id") as mock:
            mock.return_value = Department(**department_data)
            yield mock

    @fixture(scope="class", autouse=True)
    def get_by_id_department(self, test_client, manager_get_by_id_mock):
        return test_client.get(f"departments/{self.department_id}")

    def test_manager_called(self, manager_get_by_id_mock):
        manager_get_by_id_mock.assert_called_once_with(self.department_id)

    def test_result(self, get_by_id_department):
        assert get_by_id_department.json() == {
            "title": "IT Support",
            "country_name": "Sweden",
        }

    def test_status_code(self, get_by_id_department):
        assert get_by_id_department.status_code == 200


class TestGetDepartmentViewNotFound:
    department_id = 1

    @fixture(scope="class")
    def manager_get_by_id_mock(self):
        with patch.object(DepartmentManager, "get_by_id") as mock:
            mock.return_value = None
            yield mock

    @fixture(scope="class", autouse=True)
    def get_by_id_department(self, test_client, manager_get_by_id_mock):
        return test_client.get(f"departments/{self.department_id}")

    def test_manager_called(self, manager_get_by_id_mock):
        manager_get_by_id_mock.assert_called_once_with(self.department_id)

    def test_result(self, get_by_id_department):
        assert get_by_id_department.json() == {
            "detail": "Department with such id not found"
        }

    def test_raise_status_code(self, get_by_id_department):
        assert get_by_id_department.status_code == 404
