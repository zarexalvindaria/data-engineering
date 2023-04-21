import logging

from pyspark.sql import DataFrame


def assert_frames_functionally_equivalent(df1: DataFrame, df2: DataFrame):
    """Validate if 2 frames have identical schemas, and data, disregarding the
    ordering of both."""

    try:
        assert set(df1.schema.fields) == set(df2.schema.fields)
    except AssertionError:
        logging.warning(df1.schema)
        logging.warning(df2.schema)
        raise
    # Change ordering of columns, then sort the results
    assert (df1.orderBy(*df1.columns).collect()
            == df2.select(df1.columns).orderBy(*df1.columns).collect())
