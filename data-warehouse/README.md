## Module 3 Homework

```bash
cd data-warehouse

docker run -it --rm \
  -v ${PWD}/gcp-creds:/root/.config/gcloud \
  gcr.io/google.com/cloudsdktool/google-cloud-cli:slim \
  gcloud auth application-default login

docker run -it --rm \
  -v ${PWD}/gcp-creds:/root/.config/gcloud \
  gcr.io/google.com/cloudsdktool/google-cloud-cli:slim \
  gcloud auth application-default set-quota-project sigma-cortex-486321-h6

uv init --python=3.13       # scipt needs imports that are not installed - add uv
uv add google-cloud-storage # script still will not run
uv venv --python 3.8.20     # upgrade python?
source .venv/bin/activate   # did not solve problem

uv add google-cloud-vision  # Yay! *This* is the needed dependency
python load_yellow_taxi.py  # Credentials didn't work

docker build -t yellow_taxi:v001 # Let's dockerize it!

docker run -v ./gcp-creds:/root/.config/gcloud -e GOOGLE_APPLICATION_CREDENTIALS=/root/.config/gcloud/application_default_credentials.json yellow_taxi:v001

# Checked bucket and found all 6 parquet files
```

Moved to BigQuery

