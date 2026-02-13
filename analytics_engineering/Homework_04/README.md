### Homework 4

```bash
cd analytics engineering
docker compose up -d
docker compose exec dbt bash

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

