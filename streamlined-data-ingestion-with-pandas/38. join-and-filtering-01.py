# Query to get hpd311calls and precipitation values
query = """
SELECT hpd311calls.*, ____
  FROM hpd311calls
  ____ weather
  ____ hpd311calls.____ = ____;"""

# Load query results into the leak_calls dataframe
leak_calls = ____

# View the dataframe
print(leak_calls.head())

# ------ #

# Query to get hpd311calls and precipitation values
query = """
SELECT hpd311calls.*, weather.prcp
  FROM hpd311calls
  JOIN weather
  ON hpd311calls.created_date = weather.date;"""

# Load query results into the leak_calls dataframe
leak_calls = pd.read_sql(query, engine)

# View the dataframe
print(leak_calls.head())