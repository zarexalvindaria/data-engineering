from .chinese_provinces_improved import \
    aggregate_inhabitants_by_province
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, \
    StructField, StringType, LongType, BooleanType


def test_aggregate_inhabitants_by_province():
    """The number of inhabitants per province should be aggregated,
    regardless of their distinctive features.
    """

    spark = SparkSession.builder.getOrCreate()

    fields = [
        StructField("country", StringType(), True),
        StructField("province", StringType(), True),
        StructField("inhabitants", LongType(), True),
        StructField("foo", BooleanType(), True),  # distinctive features
    ]

    frame = spark.createDataFrame({
        ("China", "A", 3, False),
        ("China", "A", 2, True),
        ("China", "B", 14, False),
        ("US", "A", 4, False)},
        schema=StructType(fields)
    )
    actual = aggregate_inhabitants_by_province(frame).cache()

    # In the older implementation, the data was first filtered for a specific
    # country, after which you'd aggregate by province. The same province
    # name could occur in multiple countries though.
    # This test is expecting the data to be grouped by country,
    # then province from aggregate_inhabitants_by_province()
    expected = spark.createDataFrame(
        {("China", "A", 5), ("China", "B", 14), ("US", "A", 4)},
        schema=StructType(fields[:3])
    ).cache()

    assert actual.schema == expected.schema, "schemas don't match up"
    assert sorted(actual.collect()) == sorted(expected.collect()),\
        "data isn't equal"
