### Homework 4

```bash
# copied relevant homework files from zoomcamp repository

cd analytics engineering
docker compose up -d
docker compose exec dbt bash

dbt deps
dbt seed

# Fixed differences in variable names and added service type to int_trips_unioned
```

## Question 1. dbt Lineage and Execution

```bash
dbt run --select int_trips_unioned
```
20:00:35  1 of 1 START sql view model zoomcamp.int_trips_unioned ......................... [RUN]
20:00:36  1 of 1 OK created sql view model zoomcamp.int_trips_unioned .................... [CREATE VIEW (0 processed) in 0.87s]
20:00:36  
20:00:36  Finished running 1 view model in 0 hours 0 minutes and 1.60 seconds (1.60s).

Answer: int_trips_unioned only

## Question 2. dbt Tests

Answer: dbt will fail the test, returning a non-zero exit code

## Question 3. Counting Records in fct_monthly_zone_revenue

In BigQuery

```sql
SELECT COUNT(*)
FROM `zoomcamp.fct_monthly_zone_revenue`
```
Answer: 12459  - Added statement to filter out data from 2021 to staging data

```bash
dbt run --full-refresh --select fct_monthly_zone_revenue.sql
```

Answer: still 12456?

```sql
SELECT COUNT(*)
FROM `vital-plating-485118-d8.zoomcamp.fct_monthly_zone_revenue` 
WHERE EXTRACT(YEAR FROM revenue_month) < 2021
```
Answer: 12141 - Choosing 12,184 as best answer

## Question 4. Best Performing Zone for Green Taxis (2020)

```sql
SELECT SUM(revenue_monthly_total_amount) as total_revenue, pickup_zone 
FROM `vital-plating-485118-d8.zoomcamp.fct_monthly_zone_revenue` 
WHERE EXTRACT(YEAR FROM revenue_month) = 2020
AND service_type = 'Green'
GROUP BY pickup_zone
ORDER BY total_revenue DESC
LIMIT 1
```
Answer: Total_revenue 1817213.35 pickup_zone East Harlem North

## Question 5. Green Taxi Trip Counts (October 2019)

```sql
SELECT SUM(total_monthly_trips)
FROM `vital-plating-485118-d8.zoomcamp.fct_monthly_zone_revenue` 
WHERE EXTRACT(YEAR FROM revenue_month) = 2019
AND EXTRACT(MONTH FROM revenue_month) = 10
AND service_type = 'Green'
```

Answer: 384624

## Question 6. Build a Staging Model for FHV Data
