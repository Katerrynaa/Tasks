from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def check_exist_departments():
    response = client.get("/departments/")
    assert response.status_code == 200
    assert response.json() == [

    {"title": "HR", "country_name": "Norway"},
    {"title": "Sales", "country_name": "USA"},
    {"title": "Architecture", "country_name": "Poland"},
    {"title": "IT Support", "country_name": "Sweden"}

]

def check_inexistent_departments():
    response = client.get("/departments/")
    assert response.status_code == 404 
    assert response.json == {'detail': 'not found'}