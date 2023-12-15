from pytest import fixture
from fastapi.testclient import TestClient

from main import app
from src.models import SessionLocal


@fixture(scope="class")
def department_data():
    return {
        "title": "IT Support",
        "country_name": "Sweden",
    }

@fixture(scope="class")
def department_id():
    return {
        "id": "1",
    }

@fixture(scope="session")
def test_client():
    return TestClient(app)


@fixture(scope="class")
def test_session():
    with SessionLocal() as session:
        yield session
