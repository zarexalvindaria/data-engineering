{{ config(materialized='view')}}


with source_data as (
    select * from read_parquet('yellow_tripdata_2023-01-partial.parquet')
)

select * from source_data
