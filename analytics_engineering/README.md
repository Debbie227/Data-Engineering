## Module 4 Notes

```bash
cd analytics_engineering

# Create a virtual environment
python3 -m venv env
source env/bin/activate

# install dbt
python -m pip install dbt-core dbt-bigquery

# Begin dbt project
dbt init

docker run -it --rm \
  -v ${PWD}/gcp-creds:/root/.config/gcloud \
  gcr.io/google.com/cloudsdktool/google-cloud-cli:slim \
  gcloud auth application-default login

docker run -it --rm \
  -v ${PWD}/gcp-creds:/root/.config/gcloud \
  gcr.io/google.com/cloudsdktool/google-cloud-cli:slim \
  gcloud auth application-default set-quota-project vital-plating-485118-d8

dbt debug

# Of course it can't connect to GCP...I should know that by now

# Create docker compose file to use dbt-bigquery and GCP creds along with already started project - Moved profile.yml to directory
docker compose up -d
docker compose exec dbt bash

dbt debug     # It works!

# Opened Kestra in workflow orchestration and uploaded 2019 data to gcp database

cd models
mkdir staging
cd staging
touch sources.yml
touch green_tripdata.sql

dbt show --select green_tripdata.sql # Show a preview of the table and test that everything works properly

# Made about a million other sql files from the video in various folders
```
