# Create query for unique combinations of borough and complaint_type
query = """
SELECT ____ ____, 
       ____
  ____ hpd311calls;
"""

# Load results of query to a dataframe
issues_and_boros = ____

# Check assumption about issues and boroughs
print(____)

# ----------- #

# Create query for unique combinations of borough and complaint_type
query = """
SELECT DISTINCT borough, 
       complaint_type
  FROM hpd311calls;
"""

# Load results of query to a dataframe
issues_and_boros = pd.read_sql(query, engine)

# Check assumption about issues and boroughs
print(issues_and_boros)