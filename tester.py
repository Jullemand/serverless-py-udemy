
import os, time, json
from google.cloud import bigquery
from google.cloud import secretmanager
import google.auth

# Verifying that Python can access Google Cloud
try:
    _, project_id = google.auth.default()
except google.auth.exceptions.DefaultCredentialsError:
    project_id = None
print(project_id)

# Google Cloud Project ID
# client = secretmanager.SecretManagerServiceClient()

# name of the secret made with "gcloud secrets create"
secret_label = "py_env_file"

gcloud_secret_name = f"projects/{project_id}/secrets/{secret_label}/versions/latest"
# payload = client.access_secret_version(request={"name": gcloud_secret_name}).payload.data.decode("UTF-8")

# print(payload)
# secret_value_dict = json.loads(payload)
# print(secret_value_dict)

# client = bigquery.Client(credentials=credentials, project=credentials.project_id)
# client = bigquery.Client(project=project_id)
client = bigquery.Client()

def query_data(q):
    print("QUERY:", q)
    try:
        query_job = client.query(q)  # API request
        rows = query_job.result()  # Waits for query to finish
        for row in rows:
            print(row)
    except Exception as e:
        print(e)

# Not Valiud:
    # query_data("SELECT * FROM serverless-api-udemy-fastapi.dbtest.table1")
    # query_data("SELECT * FROM table1")

query_data("SELECT * FROM dbtest.table1")
client.query("INSERT INTO dbtest.table1(a, b) VALUES (1,1)")
time.sleep(0.5)
query_data("SELECT * FROM dbtest.table1")

# credentials = service_account.Credentials.from_service_account_info(secret_value_dict)