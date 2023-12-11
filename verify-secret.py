
import google.auth
from google.cloud import secretmanager

# Verifying that Python can access Google Cloud
try:
    _, project_id = google.auth.default()
except google.auth.exceptions.DefaultCredentialsError:
    project_id = None
print(project_id)

client = secretmanager.SecretManagerServiceClient()

# name of the secret made with "gcloud secrets create"
secret_label = "py_env_file"

gcloud_secret_name = f"projects/{project_id}/secrets/{secret_label}/versions/latest"

payload = client.access_secret_version(name=gcloud_secret_name).payload.data.decode("UTF-8")
print(payload)

