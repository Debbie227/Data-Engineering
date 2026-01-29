## Module 2 Homework

```bash
cd workflow-orchestration
docker compose up
```
opened kestra using port 8080
opened GCP in browser

## Quiz Questions

### 1. Within the execution for Yellow Taxi data for the year 2020 and month 12: what is the uncompressed file size?

In Kestra: backfill executed flow 09_gcp_taxi_scheduled 2020-12-01 00:00:00 - 2020-12-02 00:00:00 yellow (copy of code is in workflow-orchestration folder gcp_taxi_scheduled.yaml)

In GCP: Navigated to bucket and found yellow_tripdata_2020-12.csv

answer 134.5 MB

### 2. What is the rendered value of the variable file when the inputs taxi is set to green, year is set to 2020, and month is set to 04 during execution?

file is coded as: "{{inputs.taxi}}_tripdata_{{trigger.date | date('yyyy-MM')}}.csv" 
{inputs.taxi} = green 
{trigger.date | date('yyyy-MM')} = 2020-04

answer green_tripdata_2020_04.csv

### 3. How many rows are there for the Yellow Taxi data for all CSV files in the year 2020?

In Kestra: backfill executed flow 09_gcp_taxi_scheduled 2020-01-01 00:00:00 - 2020-11-02 00:00:00 yellow

In BigQuery:
```SQL
SELECT COUNT(*)
FROM zoomcamp.yellow_tripdata
WHERE filename LIKE '%2020%';
```

answer 24648499

### 4. How many rows are there for the Green Taxi data for all CSV files in the year 2020?

In Kestra: backfill executed flow 09_gcp_taxi_scheduled 2020-01-01 00:00:00 - 2020-12-02 00:00:00 green

In BigQuery:
```SQL
SELECT COUNT(*)
FROM zoomcamp.green_tripdata
WHERE filename LIKE '%2020%';
```
answer 1734051

### 5. How many rows are there for the Yellow Taxi data for the March 2021 CSV file?

In Kestra: backfill executed flow 09_gcp_taxi_scheduled 2021-03-01 00:00:00 - 2021-03-02 00:00:00 yellow

In BigQuery:
```SQL
SELECT COUNT(*)
FROM zoomcamp.yellow_tripdata
WHERE filename LIKE '%2021-03%';
```
answer 1925152

### 6. How would you configure the timezone to New York in a Schedule trigger?

Navigated to Kestra docs: Schedules are set default to UTC - set timezone property on the schedule trigger (for example, America/New_York)

answer Add a timezone property set to America/New_York in the Schedule trigger configuration

```bash
docker compose down
```