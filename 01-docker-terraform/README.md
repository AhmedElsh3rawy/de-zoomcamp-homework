# Module 1 Homework: Docker & SQL

## Question 1

```bash
docker run -it --entrypoint bash python:3.13
```

Then, inside the container, run:

```bash
pip --version
```

### Answer: `25.3`

## Question 2

### Answer: `postgres:5432`

## Question 3

#### Using SQL

```sql
SELECT
    COUNT(gtd.trip_distance) short_trips_cnt
FROM
    green_taxi_data gtd
WHERE
    gtd.trip_distance <= 1
    AND gtd.lpep_pickup_datetime BETWEEN '2025-11-01' AND '2025-12-01';
```

#### Using Pandas

```python
count = (
    (df["trip_distance"] <= 1) &
    (df["lpep_pickup_datetime"] > "2025-11-01") &
    (df["lpep_pickup_datetime"] <  "2025-12-01")
).sum()

print(count)
```

### Answer: `8007`

## Question 4

```sql
SELECT
    lpep_pickup_datetime,
    trip_distance
FROM
    green_taxi_data
WHERE
    trip_distance < 100
ORDER BY
    trip_distance DESC
LIMIT 1;
```

### Answer: `2025-11-14`

## Question 5

```sql
SELECT
    pz.zone pickup_zone,
    SUM(gtd.total_amount) total_earnings
FROM
    green_taxi_data gtd
INNER JOIN taxi_zone_lookup pz
    ON
    gtd.pulocationid = pz.locationid
WHERE
    gtd.lpep_pickup_datetime::date = '2025-11-18'
GROUP BY
    pz.zone
ORDER BY
    total_earnings DESC
LIMIT 1;
```

### Answer: `Est Harlem North`

## Question 6

```sql
SELECT
    dz.zone dropoff_zone,
    gtd.tip_amount max_tip
FROM
    green_taxi_data gtd
INNER JOIN taxi_zone_lookup pz
    ON
    gtd.pulocationid = pz.locationid
INNER JOIN taxi_zone_lookup dz
    ON
    gtd.dolocationid = dz.locationid
WHERE
    pz.zone = 'East Harlem North'
ORDER BY
    gtd.tip_amount DESC
LIMIT 1;
```

### Answer: `Yorkville West`

## Question 7

### Answer: `terraform init, terraform apply -auto-approve, terraform destroy`
