# Load pandas as pd
____

# Load the daily report to a dataframe
pop_in_shelters = ____

# View summary stats about pop_in_shelters
print(____)

# --------- #

# Load pandas as pd
import pandas as pd

# Load the daily report to a dataframe
pop_in_shelters = pd.read_json('dhs_daily_report.json')

# View summary stats about pop_in_shelters
print(pop_in_shelters.describe())