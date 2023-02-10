# Create a query to get month and max tmax by month
query = """
SELECT ____, 
       ____
  FROM ____ 
  ____ ____;"""

# Get dataframe of monthly weather stats
weather_by_month = pd.read_sql(query, engine)

# View weather stats by month
print(weather_by_month)

# ------------ #

# Create a query to get month and max tmax by month
query = """
SELECT month, 
       MAX(tmax)
  FROM weather 
  GROUP BY month;"""

# Get dataframe of monthly weather stats
weather_by_month = pd.read_sql(query, engine)

# View weather stats by month
print(weather_by_month)