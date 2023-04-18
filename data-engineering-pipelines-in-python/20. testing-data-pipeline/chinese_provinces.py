from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lower, sum

from .catalog import catalog

spark = SparkSession.builder.getOrCreate()

frame = (spark
         .read
         .parquet(catalog["clean/demographics"])
         .filter(lower(col("country")) == "china")
         .groupBy("province")
         .agg(sum(col("inhabitants")).alias("inhabitants"))
         .write
         .parquet(catalog["business/chinese_demographics"])
         )
