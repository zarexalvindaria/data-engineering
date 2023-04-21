import pytest
from pyspark.sql import SparkSession
from pyspark.sql.types import StructField, StringType, IntegerType, StructType

from .spark_helpers import assert_frames_functionally_equivalent


def test_assert_frames_functionally_equivalent():
    spark = SparkSession.builder.enableHiveSupport().getOrCreate()

    frame1 = spark.createDataFrame([(1,), (2,)])
    frame2 = spark.createDataFrame([(1,), (2,), (2,)])

    with pytest.raises(AssertionError):
        assert_frames_functionally_equivalent(frame1, frame2)

    # Identical frames are... well, identical.
    assert_frames_functionally_equivalent(frame1, frame1)

    fields = [StructField("name", StringType(), True),
              StructField("age", IntegerType(), True)]
    frame3 = spark.createDataFrame(
        [("Wim", 1), ("Conrad", 2)],
        schema=StructType(fields)
    )

    frame4 = spark.createDataFrame(
        [(1, "Wim"), (2, "Conrad")],
        schema=StructType(fields[::-1])
    )
    # Ordering of the columns is not important
    assert_frames_functionally_equivalent(frame3, frame4)

    # in Python 3, None is not sortable wrt to other types,
    # i.e. None < 3 errors out
    frame5 = spark.createDataFrame([(None, 1), ("Christina", 2)],
                                   schema=StructType(fields))
    assert_frames_functionally_equivalent(frame5, frame5)

    # Ordering of the data is not important
    frame6 = spark.createDataFrame(
        [("Wim", 1), ("Conrad", 2)],
        schema=StructType(fields)
    )

    frame7 = spark.createDataFrame(
        [("Conrad", 2), ("Wim", 1)],
        schema=StructType(fields)
    )
    assert_frames_functionally_equivalent(frame6, frame7)
