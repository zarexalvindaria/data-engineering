select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      select * 
from taxi_rides_raw
WHERE tpep_pickup_datetime = tpep_dropoff_datetime
-- Complete the test on the following line
      
    ) dbt_internal_test