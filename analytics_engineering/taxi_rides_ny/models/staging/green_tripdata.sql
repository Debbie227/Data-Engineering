SELECT *
FROM {{ source('raw_data', 'green_tripdata') }}
WHERE EXTRACT(YEAR FROM lpep_pickup_datetime) = 2019