# Read a csv file and set the headers
df = (spark.____
      .____(____=____)
      .csv("/home/repl/workspace/mnt/data_lake/landing/ratings.csv"))

df.show()

# --------- #

# Read a csv file and set the headers
df = (spark.read
      .options(header="true")
      .csv("/home/repl/workspace/mnt/data_lake/landing/ratings.csv"))

df.show()