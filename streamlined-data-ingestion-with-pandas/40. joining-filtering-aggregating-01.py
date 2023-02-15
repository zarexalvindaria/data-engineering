# Query to get heat/hot water call counts by created_date
query = """
SELECT hpd311calls.____, 
       ____
  FROM hpd311calls 
  ____ hpd311calls.____ = ____
  ____ hpd311calls.____;
"""

# Query database and save results as df
df = ____

# View first 5 records
print(df.head())

# ------------ #

# Query to get heat/hot water call counts by created_date
query = """
SELECT hpd311calls.created_date, 
       COUNT(*)
  FROM hpd311calls 
  WHERE hpd311calls.complaint_type = 'HEAT/HOT WATER'
  GROUP BY hpd311calls.created_date;
"""

# Query database and save results as df
df = pd.read_sql(query,engine)

# View first 5 records
print(df.head(5))