import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

@pytest.fixture
def example_department():
    return [
        {
            "title": "HR",
            "country_name": "Norway",
        },
        {
            "title": "Sales",
            "country_name": "USA",
        },
        {
            "title": "Architecture",
            "country_name": "Poland",
        },
        {
            "title": "IT Support",
            "country_name": "Sweden",
        },
    ]
