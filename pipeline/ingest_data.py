#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# ## Download sample of csv data from github repository and create pandas dataframe (100 rows)

# In[3]:


prefix = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/'
df = pd.read_csv(prefix + 'yellow_tripdata_2021-01.csv.gz', nrows=100)


# In[4]:


df.head()


# In[6]:


df.dtypes


# In[7]:


df.info()


# ## Pandas automatic parsing of datatypes wasn't correct. Create a dytype map based on given taxi data and re-create dataframe correctly

# In[8]:


dtype = {
    "VendorID": "Int64",
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
    "congestion_surcharge": "float64"
}

parse_dates = [
    "tpep_pickup_datetime",
    "tpep_dropoff_datetime"
]

df = pd.read_csv(
    prefix + 'yellow_tripdata_2021-01.csv.gz',
    nrows=100,
    dtype=dtype,
    parse_dates=parse_dates
)


# In[9]:


df.head()


# In[10]:


df.info()


# ## sqlalchemy will transform the pandas dataframe into sql tables in postgres 

# In[11]:


get_ipython().system('uv add sqlalchemy')


# In[12]:


from sqlalchemy import create_engine
engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')


# In[13]:


get_ipython().system('uv add psycopg2-binary')


# In[14]:


engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')


# In[15]:


print(pd.io.sql.get_schema(df, name='yellow_taxi_data', con=engine))


# ### Create schema only with the pandas dataframe into the postgres database

# In[16]:


df.head(0).to_sql(name='yellow_taxi_data', con=engine, if_exists='replace')


# ## Add full data to postgres in smaller manageable chunks 

# In[20]:


df_iter = pd.read_csv(
    prefix + 'yellow_tripdata_2021-01.csv.gz',
    dtype=dtype,
    parse_dates=parse_dates,
    iterator=True,
    chunksize=100000
)


# In[21]:


get_ipython().system('uv add tqdm')


# In[23]:


from tqdm.auto import tqdm
#Package to check the progress of code


# In[25]:


for df_chunk in tqdm(df_iter):
    df_chunk.to_sql(name='yellow_taxi_data', con=engine, if_exists='append')


# In[ ]:




