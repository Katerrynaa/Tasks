# перевірити вставку даних, тобто переконатись, що вони вставлені в базу даних
# перевірити читання даних, чи повертається список з базт даних
# чи працює обробка помилок 

import pytest
from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_read_data():
    response = client.get('/departments')
    data = response.json()
    assert response.status_code == 200

    info_data = [
        ('HR', 'Norway'),
        ('IT Support', 'Sweden'),
        ('Achitecture', 'Poland'),
        ('Sales', 'USA')
    ]

    data_tuple = [(item['title'], item['country_name']) for item in data]
    assert set(data_tuple) == set(info_data)

def test_raise():
    pass