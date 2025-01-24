## Question 1

`docker run -it --entrypoint bash python:3.12.8`

`pip --version`

Answer: `24.3.1`

## Question 2

hostname: `postgres`
port: `5432`

Answer: `postgres:5432`

## Question 3

1. Up to 1 mile

```sql
SELECT
  count(trip_distance)
FROM
  green_taxi_trips
WHERE
  lpep_pickup_datetime >= '2019-10-01'
  AND lpep_pickup_datetime < '2019-11-01'
  AND lpep_dropoff_datetime < '2019-11-01'
  AND trip_distance <= 1;
```

2. In between 1 (exclusive) AND 3 miles (inclusive)

```sql
SELECT
  count(trip_distance)
FROM
  green_taxi_trips
WHERE
  lpep_pickup_datetime >= '2019-10-01'
  AND lpep_pickup_datetime < '2019-11-01'
  AND lpep_dropoff_datetime < '2019-11-01'
  AND trip_distance > 1
  AND trip_distance <= 3;
```

3. In between 3 (exclusive) AND 7 miles (inclusive)

```sql
SELECT
  count(trip_distance)
FROM
  green_taxi_trips
WHERE
  lpep_pickup_datetime >= '2019-10-01'
  AND lpep_pickup_datetime < '2019-11-01'
  AND lpep_dropoff_datetime < '2019-11-01'
  AND trip_distance > 3
  AND trip_distance <= 7;
```

4. In between 7 (exclusive) AND 10 miles (inclusive)

```sql
SELECT
  count(trip_distance)
FROM
  green_taxi_trips
WHERE
  lpep_pickup_datetime >= '2019-10-01'
  AND lpep_pickup_datetime < '2019-11-01'
  AND lpep_dropoff_datetime < '2019-11-01'
  AND trip_distance > 7
  AND trip_distance <= 10;
```

5. Over 10 miles

```sql

SELECT
  count(trip_distance)
FROM
  green_taxi_trips
WHERE
  lpep_pickup_datetime >= '2019-10-01'
  AND lpep_pickup_datetime < '2019-11-01'
  AND lpep_dropoff_datetime < '2019-11-01'
  AND trip_distance > 10;
```

Answer: 104,802; 198,924; 109,603; 27,678; 35,189
