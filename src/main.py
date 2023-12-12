import os
from fastapi import FastAPI
from src.env import config    # it returns a function

from google.cloud import bigquery
from google.cloud import secretmanager
from google.oauth2 import service_account
import google.auth
import bigquery_client as bqclientlib
from fastapi.responses import RedirectResponse

from fastapi.staticfiles import StaticFiles
from models import poolsearch 

# Verifying that Python can access Google Cloud
try:
    # _, project_id = google.auth.default()
    # print("Google Auth successfull")
    val[a] += 1
# except google.auth.exceptions.DefaultCredentialsError:
except:
    print("Trying to access local folder JSON file ...")
    try:
        key_path = "/application_default_credentials.json"
        credentials = service_account.Credentials.from_service_account_file(
            key_path, scopes=["https://www.googleapis.com/auth/cloud-platform"],
        )
        project_id = credentials.project_id
    except:
        project_id = None

print("Project ID:", project_id)
bq_client = bigquery.Client(project=project_id)
# bq_client = bigquery.Client(credentials=credentials, project=credentials.project_id,)
# bq_client = bigquery.Client()

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

@app.get("/solve")
async def solve():
    solve_res = poolsearch.run_test_solve()
    return { "solve_status": solve_res}


'''
@app.post("/")
def handle_data():
    return 
'''






