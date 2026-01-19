# Module 1 Homework: Docker and SQL

## Question 1. Understanding Docker images

```bash
docker run -it --rm --entrypoint=bash python:3.13

pip --version
```

answer: pip 25.3 from /usr/local/lib/python3.13/site-packages/pip (python 3.13)

## Question 2. Undestanding Docker networking and docker-compose

```yaml
services:
  db:                                   # service name/hostname
    container_name: postgres            # container name/hostname - not portable across environments? Not recommended.
    image: postgres:17-alpine
    environment:
      POSTGRES_USER: 'postgres'
      POSTGRES_PASSWORD: 'postgres'
      POSTGRES_DB: 'ny_taxi'
    ports:
      - '5433:5432'                     # external-port:internal-port *containers connect to each other via the internal port
    volumes:
      - vol-pgdata:/var/lib/postgresql/data

  pgadmin:
    container_name: pgadmin
    image: dpage/pgadmin4:latest
    environment:
      PGADMIN_DEFAULT_EMAIL: "pgadmin@pgadmin.com"
      PGADMIN_DEFAULT_PASSWORD: "pgadmin"
    ports:
      - "8080:80"
    volumes:
      - vol-pgadmin_data:/var/lib/pgadmin

volumes:
  vol-pgdata:
    name: vol-pgdata
  vol-pgadmin_data:
    name: vol-pgadmin_data
```

answer: hostname = db or postgres, port = 5432

## Prepare the data

```bash
wget https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2025-11.parquet
wget https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv

 uv init --python=3.13
 uv add --dev jupyter
 uv add pandas pyarrow
 uv run jupyter notebook
 # Completed EDA in jupyter notebook
 
```