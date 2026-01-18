import pandas as pd

from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:password@localhost:5432/ny_taxi")

dtype_trips = {
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
    "congestion_surcharge": "float64",
}

parse_dates = ["lpep_pickup_datetime", "lpep_dropoff_datetime"]

dtype_zones = {
    "LocationId": "Int64",
    "Borough": "string",
    "Zone": "string",
    "service_zone": "string",
}

df_trips = pd.read_csv(
    "green_tripdata_2025-11.csv", dtype=dtype_trips, parse_dates=parse_dates
)

df_trips.columns = (
    df_trips.columns.str.strip().str.lower().str.replace(" ", "_").str.replace("-", "_")
)


df_zones = pd.read_csv("taxi_zone_lookup.csv", dtype=dtype_zones)

df_zones.columns = (
    df_zones.columns.str.strip().str.lower().str.replace(" ", "_").str.replace("-", "_")
)

table1 = "green_taxi_data"
table2 = "taxi_zone_lookup"

df_trips.head(0).to_sql(table1, con=engine, if_exists="replace", index=False)

df_zones.head(0).to_sql(table2, con=engine, if_exists="replace", index=False)

df_trips.to_sql(name=table1, con=engine, if_exists="append", index=False)
df_zones.to_sql(name=table2, con=engine, if_exists="append", index=False)
