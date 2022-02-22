# Specify the option to drop invalid rows
ratings = (spark
           .read
           .____(header=True, ____=____)
           .csv("/home/repl/workspace/mnt/data_lake/landing/ratings_with_invalid_rows.csv"))
ratings.show()

# ----------- #

# Specify the option to drop invalid rows
ratings = (spark
           .read
           .options(header=True, mode="DROPMALFORMED")
           .csv("/home/repl/workspace/mnt/data_lake/landing/ratings_with_invalid_rows.csv"))
ratings.show()