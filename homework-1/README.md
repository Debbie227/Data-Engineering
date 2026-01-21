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
mkdir homework-1/
wget https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2025-11.parquet
wget https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv

 uv init --python=3.13
 uv add --dev jupyter
 uv add pandas pyarrow
 uv run jupyter notebook

 # Completed EDA in jupyter notebook

 # New terminal
 cd homework-1/
 docker run -it --rm \
  -e POSTGRES_USER="user" \
  -e POSTGRES_PASSWORD="pass" \
  -e POSTGRES_DB="green_taxi" \
  -v green_taxi_data:/var/lib/postgresql \
  -p 5432:5432 \
  postgres:18

  # New terminal
  cd homework-1/
  uv run jupyter nbconvert --to=script green_taxi.ipynb
  mv green_taxi.py ingest_green.py

  # Edited ingest_green.py to script for ingesting data to sql database

  uv add click
  uv add sqlalchemy
  uv add psycopg2

  # Try data ingestion with the localhost - edited the many problems with the script ^-^
  uv run python ingest_green.py \
  --pg_user=user \
  --pg_pass=pass \
  --pg_host=localhost \
  --pg_port=5432 \
  --pg_db=green_taxi \
  --target_table=green_taxi_data

  uv add --dev pgcli
  uv run pgcli -h localhost -p 5432 -u user -d green_taxi
  \dt # Shows the tables exist finally!! \o/
  quit

  touch Dockerfile
  # Created docker ingestion file
  #Changed psycopg2 to psycopg2-binary in pyproject.toml
  uv lock
  docker build -t taxi_ingest:v001 .

  # Run docker ingestion file with postgres running
  docker run -it \
  --network=host \
  taxi_ingest:v001 \
    --pg_user=user \
    --pg_pass=pass \
    --pg_host=localhost \
    --pg_port=5432 \
    --pg_db=green_taxi \
    --target_table=green_taxi_data

  touch docker-compose.yaml
  # Created docker file to run postgres and pgadmin together

  # Stop running containers
  docker ps
  docker stop $(docker ps -q)
  docker ps

  docker compose up -d

  docker run -it \
  --network=homework-1_default \
  taxi_ingest:v001 \
    --pg_user=user \
    --pg_pass=pass \
    --pg_host=pgdatabase \
    --pg_port=5432 \
    --pg_db=green_taxi \
    --target_table=green_taxi_data

  # Entered the IP address at port 8085 into a web browser and logged into pgadmin with 'admin@admin.com' and 'root'

  # Registered server under name local docker, port 5432, username user, password pass

  # Data ingested and ready for SQL queries!

# ***Use docker compose down if you take a break!***
```

## Question 3. Counting short trips

```sql
SELECT COUNT(*)
FROM
	green_taxi_data
WHERE
	lpep_pickup_datetime >= '2025-11-01' 
	AND lpep_pickup_datetime <'2025-12-01'
	AND trip_distance <= 1;
```

answer 8007

## Question 4. Longest trip for each day

```sql
SELECT CAST(lpep_pickup_datetime AS DATE) AS date_only
FROM
	green_taxi_data
WHERE
	trip_distance = (SELECT MAX(trip_distance) FROM green_taxi_data WHERE trip_distance < 100);
```

answer 2025-11-14

## Question 5. Biggest pickup zone

```sql
SELECT t."Zone",
       SUM(g.total_amount) AS total_amount_sum
FROM green_taxi_data g
JOIN taxi_zone t
  ON t."LocationID" = g."PULocationID"
WHERE DATE(g.lpep_pickup_datetime) = '2025-11-18'
GROUP BY 
  t."Zone"
ORDER BY 
  total_amount_sum DESC
LIMIT 1;
```

answer East Harlem North

## Question 6. Largest tip

```sql
SELECT
	z."Zone",
	g.tip_amount,
	g."PULocationID",
	g."DOLocationID"
FROM
	green_taxi_data g JOIN taxi_zone z
		ON g."DOLocationID" = z."LocationID"
WHERE
	g."PULocationID" = 74
ORDER BY
	g.tip_amount DESC
LIMIT 1;
```

answer Yorkville West

## Question 7. Terraform Workflow

```bash
# This will install terraform on the system - Can be used inside a dockerfile to run terraform without system installation
wget -O - https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg

echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(grep -oP '(?<=UBUNTU_CODENAME=).*' /etc/os-release || lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list

sudo apt update && sudo apt install terraform

terraform --version
#Terraform v1.14.3
#on linux_amd64
```

answer terraform init, terraform plan -auto-apply, terraform rm