from fastapi import FastAPI

app = FastAPI()

@app.get('/departments')
def read_depart():
    return {
        'HR': 'Norway',
        'IT Support': 'Sweden',
        'Achitecture': 'Poland',
        'Sales': 'USA',
        'Design': 'Denmark',
    }