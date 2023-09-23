select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    



select fare_amount
from "dbt"."main"."taxi_rides_raw"
where fare_amount is null



      
    ) dbt_internal_test