## Module 3 Homework

```bash
cd data-warehouse

uv init --python=3.13       # scipt needs imports that are not found - add uv
uv add google-cloud-storage # script still will not run
uv venv --python 3.8.20     # upgrade python?
source .venv/bin/activate   # did not solve problem

uv add google-cloud-vision  # Yay! This is the needed dependency
python load_yellow_taxi.py
```