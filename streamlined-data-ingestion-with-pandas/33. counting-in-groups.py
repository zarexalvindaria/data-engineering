# Create query to get call counts by complaint_type
query = """
____ ____, 
     ____(*)
  FROM hpd311calls
  ____ ____;
"""

# Create dataframe of call counts by issue
calls_by_issue = pd.read_sql(____, ____)

# Graph the number of calls for each housing issue
calls_by_issue.plot.barh(x="complaint_type")
plt.show()

# --------- #

# Create query to get call counts by complaint_type
query = """
SELECT complaint_type, 
     COUNT(*)
  FROM hpd311calls
  GROUP BY complaint_type;
"""

# Create dataframe of call counts by issue
calls_by_issue = pd.read_sql(query, engine)

# Graph the number of calls for each housing issue
calls_by_issue.plot.barh(x="complaint_type")
plt.show()