## Question 1

`docker run -it --entrypoint bash python:3.12.8`

`pip --version`

**Answer**: 24.3.1

## Question 2

hostname: postgres

port: 5432

**Answer**: postgres:5432

## Question 3

1. Up to 1 mile

```sql
SELECT
  COUNT(trip_distance)
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
  COUNT(trip_distance)
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
  COUNT(trip_distance)
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
  COUNT(trip_distance)
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
  COUNT(trip_distance)
FROM
  green_taxi_trips
WHERE
  lpep_pickup_datetime >= '2019-10-01'
  AND lpep_pickup_datetime < '2019-11-01'
  AND lpep_dropoff_datetime < '2019-11-01'
  AND trip_distance > 10;
```

**Answer**: 104,802; 198,924; 109,603; 27,678; 35,189

## Question 4

#### Longest trip for each day

```sql
SELECT
  DATE(lpep_pickup_datetime) AS pickup_day,
  MAX(trip_distance) AS max_trip_distance
FROM
  green_taxi_trips
GROUP BY
  DATE(lpep_pickup_datetime)
ORDER BY
  longest_trip_distance DESC
LIMIT
  1;
```

**Answer**: 2019-10-31

## Question 5

#### Three biggest pickup zones

```sql
SELECT
  z."Zone",
  SUM(g.total_amount) AS sum_total_amount
FROM
  green_taxi_trips g
  INNER JOIN zones z ON g."PULocationID" = z."LocationID"
WHERE
  g.lpep_pickup_datetime = '2019-10-18'
GROUP BY
  z."Zone"
HAVING
  SUM(g.total_amount) > 13000
ORDER BY
  sum_total_amount DESC
LIMIT
  3;
```

**Answer**: East Harlem North, East Harlem South, Morningside Heights

## Question 6

#### Largest tip

```sql
SELECT
  z."Zone",
  MAX(g.tip_amount) AS max_tip_amount
FROM
  green_taxi_trips g
  INNER JOIN zones z ON g."DOLocationID" = z."LocationID"
WHERE
  g."PULocationID" = (
    SELECT
      z."LocationID"
    FROM
      zones z
    WHERE
      z."Zone" = 'East Harlem North'
  )
  AND g.lpep_pickup_datetime >= '2019-10-01'
  AND g.lpep_pickup_datetime <= '2019-10-31'
GROUP BY
  z."Zone"
ORDER BY
  max_tip_amount DESC
LIMIT
  1;
```

**Answer**: JFK Airport

## Question 7

1. Downloading the provider plugins and setting up backend  
   command: `terraform init`
2. Generating proposed changes and auto-executing the plan  
   command: `terraform apply -auto-approve`
3. Remove all resources managed by terraform  
   command: `terraform destroy`

**Answer**: terraform init, terraform apply -auto-approve, terraform destroy
