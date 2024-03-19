from pytest import fixture
from fastapi.testclient import TestClient
from sqlalchemy import delete

from main import app
from src.config import read_config
from src.models import SessionLocal, db_connect, db_disconnect, Department, session_var


@fixture(scope="class")
def department_data():
    return {
        "title": "IT Support",
        "country_name": "Sweden",
    }


@fixture(scope="class")
def new_department_data():
    return {
        "title": "HR",
        "country_name": "Norway",
    }


@fixture(scope="class")
def department_id():
    return {
        "id": 1,
    }


@fixture(scope="session", autouse=True)
def test_db():
    config = read_config()
    db_connect(config.DATABASE_URL)
    yield
    db_disconnect()


@fixture(scope="session")
def test_client():
    return TestClient(app)


@fixture(scope="class", autouse=True)
def test_session():
    with SessionLocal() as session:
        with session.begin():
            token = session_var.set(session)
            yield session
            session_var.reset(token)


@fixture(scope="class", autouse=True)
def clean_db(test_session):
    test_session.execute(delete(Department))
