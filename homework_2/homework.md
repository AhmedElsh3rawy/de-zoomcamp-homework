## Question 1

using Kestra

```yml
id: postgres_taxi
namespace: zoomcamp

inputs:
  - id: taxi
    type: SELECT
    displayName: Select taxi type
    values: ["yellow", "green"]
    defaults: "yellow"

  - id: year
    type: SELECT
    displayName: Select year
    values: ["2019", "2020"]
    defaults: "2019"

  - id: month
    type: SELECT
    displayName: Select month
    values:
      ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
    defaults: "01"

variables:
  file: "{{inputs.taxi}}_tripdata_{{inputs.year}}-{{inputs.month}}.csv"
  staging_table: "public.{{inputs.taxi}}_tripdata_staging"
  table: "public.{{inputs.taxi}}_tripdata"
  data: "{{outputs.extract.outputFiles[inputs.taxi ~ '_tripdata_' ~ 'inputs.year' ~ '-' ~ 'inputs.month' ~ '.csv']}}"

tasks:
  - id: set_label
    type: io.kestra.plugin.core.execution.Labels
    labels:
      file: "{{render(vars.file)}}"
      taxi: "{{inputs.taxi}}"

  - id: extract
    type: io.kestra.plugin.scripts.shell.Commands
    outputFiles:
      - "*.csv"
    taskRunner:
      type: io.kestra.plugin.core.runner.Process
    commands:
      - wget -qO- https://github.com/DataTalksClub/nyc-tlc-data/releases/download/{{inputs.taxi}}/{{render(vars.file)}}.gz | gunzip > {{render(vars.file)}}
```

**Answer**: 128.3 MB

## Question 2

**Answer**: `green_tripdata_2020-04.csv`

## Question 3

**Answer**: 24,648,499

## Question 4

**Answer**: 1,734,051

## Question 5

**Answer**: 1,925,152

## Question 6

```yml
triggers:
  - id: daily
    type: io.kestra.plugin.core.trigger.Schedule
    cron: "@daily"
    timezone: America/New_York
```

**Answer**: Add a `timezone` property set to `America/New_York` in the Schedule trigger configuration
