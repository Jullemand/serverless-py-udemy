import os
from fastapi import FastAPI
from src.env import config    # it returns a function

from google.cloud import bigquery
from google.cloud import secretmanager
import google.auth
import bigquery_client as bqclientlib
from fastapi.responses import RedirectResponse

from fastapi.staticfiles import StaticFiles
# from fastapi.templating import Jinja2Templates
# from fastapi import Request
# from fastapi import APIRouter

# Verifying that Python can access Google Cloud
try:
    _, project_id = google.auth.default()
except google.auth.exceptions.DefaultCredentialsError:
    project_id = None
print(project_id)
bq_client = bigquery.Client(project=project_id)

app = FastAPI()
app.counter = 0
app.mount("/ui", StaticFiles(directory="ui", html=True), name="")

MODE = config("MODE", cast=str, default=None)

# templates = Jinja2Templates(directory="templates")
# general_pages_router = APIRouter()

@app.get("/")   # HTTP's GET method
def home_page():
    return RedirectResponse(url='/ui')
    # app.counter += 1
    # return { "mode": MODE, "counter": app.counter} 

"""
@general_pages_router.get("/")
async def home(request: Request):
    return templates.TemplateResponse("ui/index.html", {"request":request})
"""

@app.get("/reset")
def reset_counter():
    app.counter = 0
    return { "mode": MODE, "counter": app.counter} 

@app.get("/additem")
async def add_bq_item():
    exit_code = bqclientlib.insert_data(bq_client, f"INSERT INTO dbtest.table1(Date) VALUES (CURRENT_DATETIME)")
    return { "status_code": exit_code }

@app.get("/getall")
async def get_all():
    query_result, exit_code = bqclientlib.query_data(bq_client, "SELECT * FROM dbtest.table1")
    return { "status_code": exit_code, "output": query_result }


'''
@app.post("/")
def handle_data():
    return 
'''






