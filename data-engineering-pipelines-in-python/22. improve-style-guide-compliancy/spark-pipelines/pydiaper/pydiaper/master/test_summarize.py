"""This module holds a couple of dummy tests
for the DataCamp course. """

from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()


def test_calculate_unit_price_in_euros():
    assert True


def test_express_all_costs_in_euros():
    frame1 = spark.createDataFrame()
    assert  3 == 2
