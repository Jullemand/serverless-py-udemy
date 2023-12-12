
# import requests

url = "https://serverless-py-run-dsh7o6h7mq-uc.a.run.app/"

import os
from fastapi import FastAPI

app = FastAPI()
app.counter = 0    # an application global var

@app.get("/")   # HTTP's GET method
def home_page():
    # API Service
    # JSON ready dictionary -½> json.dumps(<smth>)
    app.counter += 1
    return { "get_count": app.counter} 

@app.get("/reset")
def reset_counter():
    app.counter = 0
    return { "get_count": app.counter} 