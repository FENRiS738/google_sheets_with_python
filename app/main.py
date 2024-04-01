from fastapi import FastAPI
import app.helper_functions as helper_functions
from app.schema import User

app = FastAPI()

@app.get('/')
def server():
    return "Server is running!"


@app.get('/get_data_from_sheet')
def get_data_from_sheet():
    values = helper_functions.get_data()
    return values

@app.post('/insert_data_in_sheet')
def insert_data_in_sheet(user: User): 
    res = helper_functions.insert_data(user)
    return res