"""@bruin

name: ingestion.trips
connection: duckdb-default

materialization:
  type: table
  strategy: append

# TODO: Define output columns (names + types) for metadata, lineage, and quality checks.
# Tip: mark stable identifiers as `primary_key: true` if you plan to use `merge` later.
# Docs: https://getbruin.com/docs/bruin/assets/columns


@bruin"""

# TODO: Add imports needed for your ingestion (e.g., pandas, requests).
# - Put dependencies in the nearest `requirements.txt` (this template has one at the pipeline root).
# Docs: https://getbruin.com/docs/bruin/assets/python


# TODO: Only implement `materialize()` if you are using Bruin Python materialization.
# If you choose the manual-write approach (no `materialization:` block), remove this function and implement ingestion
# as a standard Python script instead.

import os
import io
import json
import pandas as pd
import requests

def materialize():
    start_date = os.environ["BRUIN_START_DATE"]
    end_date = os.environ["BRUIN_END_DATE"]
    taxi_types = json.loads(os.environ["BRUIN_VARS"]).get("taxi_types", ["yellow"])

    # Generate list of months between start and end dates
    months = pd.date_range(start=start_date, end=end_date, freq='MS').strftime("%Y-%m").tolist()

    # Fetch parquet files from NYC TLC website
    url_template = "https://d37ci6vzurychx.cloudfront.net/trip-data/{taxi_type}_tripdata_{year}-{month}.parquet"

    final_dataframes = []

    for month in months:
        year, month_num = month.split('-')
        for taxi_type in taxi_types:
            url = url_template.format(taxi_type=taxi_type, year=year, month=month_num)
            try:
                response = requests.get(url, timeout=30)
                if response.status_code == 200:
                    df = pd.read_parquet(io.BytesIO(response.content))
                    final_dataframes.append(df)
                else:
                    print(f"Warning: {taxi_type} data not available for {month} (status: {response.status_code})")
            except Exception as e:
                print(f"Failed to fetch {url}: {e}")
    
    # Concatenate all dataframes
    if final_dataframes:
        return pd.concat(final_dataframes, ignore_index=True)
    else:
        return pd.DataFrame()
