import os
from fastapi import FastAPI
from src.env import config    # it returns a function

MODE = config("MODE", cast=str, default=None)
print("MODE", MODE)
app = FastAPI()

@app.get("/")   # HTTP's GET method
def home_page():
    # API Service
    # JSON ready dictionary -> json.dumps(<smth>)
    return {"Hello": "World", "mode": MODE} 

'''
@app.post("/")
def handle_data():
    return 
'''






