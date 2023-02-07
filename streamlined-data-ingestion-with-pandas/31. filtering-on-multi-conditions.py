# Create query for records with max temps <= 32 or snow >= 1
query = """
SELECT *
  FROM weather
  ____ ____
  ____ ____;
"""

# Query database and assign result to wintry_days
wintry_days = pd.read_sql(____)

# View summary stats about the temperatures
print(____)

# --------- #

# Create query for records with max temps <= 32 or snow >= 1
query = """
SELECT *
  FROM weather
  WHERE tmax <= 32 
  OR snow >= 1;
"""

# Query database and assign result to wintry_days
wintry_days = pd.read_sql(query,engine)

# View summary stats about the temperatures
print(wintry_days.describe())