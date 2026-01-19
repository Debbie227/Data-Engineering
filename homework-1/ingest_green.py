#!/usr/bin/env python
# coding: utf-8

import click
import pandas as pd
from sqlalchemy import create_engine

# Import data from CWD
green_data=pd.read_parquet('green_tripdata_2025-11.parquet')
taxi_zone=pd.read_csv('taxi_zone_lookup.csv')

# Drop all columns that have no values
green_data = green_data.dropna(axis=1, how='all')

# Set dtypes for green taxi data
dtype = {
    "VendorID": "Int64",
    "lpep_pickup_datetime": "datetime64[ns]",
    "lpep_dropoff_datetime": "datetime64[ns]",
    "passenger_count": "Int64",
    "trip_distance": "float64",
    "RatecodeID": "Int64",
    "store_and_fwd_flag": "string",
    "PULocationID": "Int64",
    "DOLocationID": "Int64",
    "payment_type": "Int64",
    "fare_amount": "float64",
    "extra": "float64",
    "mta_tax": "float64",
    "tip_amount": "float64",
    "tolls_amount": "float64",
    "improvement_surcharge": "float64",
    "total_amount": "float64",
    "trip_type": "Int64",
    "congestion_surcharge": "float64",
    "cbd_congestion_fee": "float64"
}

green_data = green_data.astype(dtype)

# Add click commands for database connection
@click.command()
@click.option('--pg_user', default='user', help='PostgreSQL user')
@click.option('--pg_pass', default='pass', help='PostgreSQL password')
@click.option('--pg_host', default='localhost', help='PostgreSQL host')
@click.option('--pg_port', default=5432, type=int, help='PostgreSQL port')
@click.option('--pg_db', default='green_taxi', help='PostgreSQL database name')
@click.option('--target_table', default='green_taxi_data', help='Target table name')

def run(pg_user, pg_pass, pg_host, pg_port, pg_db, target_table):

    engine = create_engine(f'postgresql://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}')

    # taxi data was downloaded from homework file and is hard coded. Taxi zone table is not editable - can add click option?
    green_data.to_sql(name=target_table, con=engine, if_exists='replace')
    print("table added")
    taxi_zone.to_sql(name='taxi_zone', con=engine, if_exists='replace')
    print("table added")

if __name__ == '__main__':
    run()