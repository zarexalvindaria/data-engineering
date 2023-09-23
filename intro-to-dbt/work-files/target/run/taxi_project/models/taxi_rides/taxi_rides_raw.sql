
  
  create view "dbt"."main"."taxi_rides_raw__dbt_tmp" as (
    


with source_data as (
    select * from read_parquet('yellow_tripdata_2023-01-partial.parquet')
)

select * from source_data
  );
