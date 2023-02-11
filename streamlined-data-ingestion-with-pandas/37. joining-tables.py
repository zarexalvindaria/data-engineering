# Query to join weather to call records by date columns
query = """
SELECT * 
  FROM hpd311calls
  JOIN ____ 
  ON hpd311calls.____ = ____.____;
"""

# Create dataframe of joined tables
calls_with_weather = ____

# View the dataframe to make sure all columns were joined
____

# ------------ #

# Query to join weather to call records by date columns
query = """
SELECT * 
  FROM hpd311calls
  JOIN weather 
  ON hpd311calls.created_date = weather.date;
"""

# Create dataframe of joined tables
calls_with_weather = pd.read_sql(query, engine)

# View the dataframe to make sure all columns were joined
print(calls_with_weather.head())