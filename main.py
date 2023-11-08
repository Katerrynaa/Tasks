from fastapi import FastAPI

app = FastAPI()

fruits = {
    'orange': '9',
    'strawberry': '10',
    'banana': '3',
    'peach': '5',
    'raspberry': '19',
    'grape': '4'
}

@app.get('/fruits')
def read_fruits():
    return fruits


departments = {
    'HR': 'Norway',
    'IT Support': 'Sweden',
    'Achitecture': 'Poland',
    'Sales': 'USA',
    'Design': 'Denmark',
}

@app.get('/departments')
def read_depart():
    return departments