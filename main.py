from fastapi import FastAPI

app = FastAPI()

@app.get('/fruits')
def read_fruits():
    return {
	    'orange': '9',
	    'strawberry': '10',
	    'banana': '3',
	    'peach': '5',
	    'raspberry': '19',
	    'grape': '4'
	}

@app.get('/departments')
def read_depart():
    return {
        'HR': 'Norway',
        'IT Support': 'Sweden',
        'Achitecture': 'Poland',
        'Sales': 'USA',
        'Design': 'Denmark',
    }