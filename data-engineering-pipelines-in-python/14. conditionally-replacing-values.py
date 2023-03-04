from pyspark.sql.functions import col, when

# Add/relabel the column
categorized_ratings = ratings.____(
    "comfort",
    # Express the condition in terms of column operations
    ____(____("comfort") > 3, "sufficient").____("insufficient"))

categorized_ratings.show()


# --------- #

from pyspark.sql.functions import col, when

# Add/relabel the column
categorized_ratings = ratings.withColumn(
    "comfort",
    # Express the condition in terms of column operations
    when(col("comfort") > 3, "sufficient").otherwise("insufficient"))

categorized_ratings.show()