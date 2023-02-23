from pyspark.sql.functions import col

# Select the columns and rename the "absorption_rate" column
result = ratings.____([col("brand"),
                       col("model"),
                       col("absorption_rate").____(____)])

# Show only unique values
result.____().show()

# ---------- #

from pyspark.sql.functions import col

# Select the columns and rename the "absorption_rate" column
result = ratings.select([col("brand"),
                       col("model"),
                       col("absorption_rate").alias("absorbency")])

# Show only unique values
result.distinct().show()