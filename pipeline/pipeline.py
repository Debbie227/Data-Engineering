import sys

import pandas as pd

#print("arguments", sys.argv)

month = int(sys.argv[1])

df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})

print(df.head())

print(f'hello pipeline, month={month}')

df.to_parquet(f"output_day_{month}.parquet")