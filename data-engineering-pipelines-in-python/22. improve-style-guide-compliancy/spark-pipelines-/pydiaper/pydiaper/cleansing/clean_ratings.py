from pyspark.sql import SparkSession
from pyspark.sql.types import *

from pydiaper.data_catalog.catalog import catalog


def main():
    spark = SparkSession.builder.getOrCreate()
    schema = StructType([
        StructField("brand", StringType(), False),
        StructField("model", StringType(), True),
        StructField("absorption_rate", ByteType(), True),
        StructField("comfort", ByteType(), True)
    ])
    frame = (spark.read
             .options(header="true")
             .schema(schema)
             .csv(catalog["landing/ratings"]))

    frame.write.parquet(catalog["clean/ratings"])


if __name__ == "__main__":
    main()
