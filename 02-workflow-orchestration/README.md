# Module 2 Homework

## Question 1

### Answer: `128.3 MB`

## Question 2

### Answer: `green_tripdata_2020-04.csv`

## Question 3

```sql
SELECT COUNT(1) total_trips
FROM yellow_taxi_2020;
```

### Answer: `24,648,499`

## Question 4

```sql
SELECT COUNT(1) total_trips
FROM green_taxi_2020;
```

### Answer: `1,925,152`

## Question 5

```sql
SELECT COUNT(1) march_2021_trip_count
FROM yellow_taxi_2021
WHERE tpep_pickup_datetime >= '2021-03-01'
  AND tpep_pickup_datetime < '2021-04-01';
```

### Answer: `1,925,152`

## Question 6

### Answer: Add a `timezone` property set to `America/New_York` in the `Schedule` trigger configuration
