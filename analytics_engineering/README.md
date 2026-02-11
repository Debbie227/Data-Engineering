## Module 4 Homework

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

docker compose up -d
docker compose exec dbt bash

dbt debug


```
