## Data Platforms and Bruin

```bash
cd data-platforms/
curl -LsSf https://getbruin.com/install/cli | sh
bruin version

bruin init default Bruin-pipeline

curl https://install.duckdb.org | sh        # Default init must have duckdb installed

cd Bruin-pipeline/

bruin run ./assets/my_python_asset.py
```
