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

create table - From: Google Cloud Storage / Select File: sigma-cortex-48-bucket/yellow_tripdata_2024*.parquet / File Format: Parquet /
            Project: sigma-cortex-486321-h6 / Dataset: External_Yellow_Taxi / Table: External_Yellow_Taxi / Table type: External Table

create table - From: Google Cloud Storage / Select File: sigma-cortex-48-bucket/yellow_tripdata_2024*.parquet / File Format: Parquet /
            Project: sigma-cortex-486321-h6 / Dataset: External_Yellow_Taxi / Table: native_yellow_taxi / Table type: Native Table
            

## Question 1: Counting records

```sql
SELECT COUNT(*)
FROM `External_Yellow_Taxi.native_yellow_taxi`;
```

answer: 20332093

## Question 2: Data read estimation

```sql
SELECT COUNT(DISTINCT PULocationID)
FROM `External_Yellow_Taxi.External_Yellow_Taxi`;

SELECT COUNT(DISTINCT PULocationID)
FROM `External_Yellow_Taxi.native_yellow_taxi`;
```

answer: 0MB external 155.12MB internal

## Question 3: Understanding columnar storage

```sql
SELECT PULocationID
FROM `External_Yellow_Taxi.native_yellow_taxi`;

SELECT PULocationID, DOLocationID
FROM `External_Yellow_Taxi.native_yellow_taxi`;
```

answer: 155.12MB with one column 310.24MB with two columns

BigQuery is a columnar database, and it only scans the specific columns requested in the query. Querying two columns (PULocationID, DOLocationID) requires reading more data than querying one column (PULocationID), leading to a higher estimated number of bytes processed.

## Question 4. Counting zero fare trips

```sql
SELECT COUNT(*)
FROM `External_Yellow_Taxi.native_yellow_taxi`
WHERE fare_amount = 0;
```

answer: 8333

## Question 5. Partitioning and clustering

Partition by tpep_dropoff_datetime and Cluster on VendorID

## Question 6. Partition benefits

```sql
SELECT DISTINCT VendorID
FROM `External_Yellow_Taxi.native_yellow_taxi`
WHERE tpep_dropoff_datetime BETWEEN '2024-03-01' and '2024-03-15';

SELECT DISTINCT VendorID
FROM `External_Yellow_Taxi.partition_yellow_taxi`
WHERE tpep_dropoff_datetime BETWEEN '2024-03-01' and '2024-03-15';
```
answer: 310.24MB and 0B
Does not match any answers so I'm going to use: 310.24 MB for non-partitioned table and 26.84 MB for the partitioned table

## Question 7. External table storage

answer: GCP Bucket.

## Question 8. Clustering best practices

answer: False.

## Question 9. Understanding table scans

```sql
SELECT count(*)
FROM `External_Yellow_Taxi.native_yellow_taxi`;
```

answer: 0B
I assume it is because the table is not being filtered and no data is used to search. The table is simply displayed as is.