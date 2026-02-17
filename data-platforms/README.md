## Data Platforms and Bruin

### Initial Bruin test
```bash
cd data-platforms/
curl -LsSf https://getbruin.com/install/cli | sh
bruin version

bruin init default Bruin-pipeline

curl https://install.duckdb.org | sh        # Default init must have duckdb installed

cd Bruin-pipeline/

bruin run ./assets/my_python_asset.py
```
### Taxi pipeline

```bash
cd data-platforms/

bruin init zoomcamp

cd zoomcamp

# created trips.py to ingest data
 bruin run --start-date 2025-02-02 --end-date 2025-02-03 ./pipeline/assets/ingestion/trips.py
# added pandas and requests to requirements so Bruin's uv can install and use them
# added table registration to the function so a duckdb table is created for the data to ingest to
# Added duckdb to requrements

# Still doesn't work
```