from unittest.mock import patch

from pytest import fixture

from src.managers import DepartmentManager


class TestCreateDepartmentView:
    @fixture(scope="class")
    def manager_create_mock(self):
        with patch.object(DepartmentManager, "create") as mock:
            yield mock

    @fixture(scope="class", autouse=True)
    def create_department(self, test_client, manager_create_mock, department_data):
        return test_client.post("/departments", json=department_data)

    def test_manager_called(self, manager_create_mock, department_data):
        manager_create_mock.assert_called_once_with(data=department_data)

    def test_result(self, create_department):
        assert create_department.json() == ["Data added successfully"]

    def test_status_code(self, create_department):
        assert create_department.status_code == 200
