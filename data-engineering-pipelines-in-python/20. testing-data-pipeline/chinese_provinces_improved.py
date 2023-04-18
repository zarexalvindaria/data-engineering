from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lower, sum

from .catalog import catalog


def extract_demographics(sparksession, catalog):
    return sparksession.read.parquet(catalog["clean/demographics"])


def store_chinese_demographics(frame, catalog):
    frame.write.parquet(catalog["business/chinese_demographics"])


# Improved aggregation function, grouped by country and province
def aggregate_inhabitants_by_province(frame):
    return (frame
            .groupBy("country", "province")
            .agg(sum(col("inhabitants")).alias("inhabitants"))
            )


def main():
    spark = SparkSession.builder.getOrCreate()
    frame = extract_demographics(spark, catalog)
    chinese_demographics = frame.filter(lower(col("country")))
    aggregated_demographics = aggregate_inhabitants_by_province(
        chinese_demographics
    )
    store_chinese_demographics(aggregated_demographics, catalog)


if __name__ == "__main__":
    main()
