# Load json_normalize()
____

# Isolate the JSON data from the API response
data = ____

# Flatten business data into a dataframe, replace separator
cafes = ____(data["businesses"],
             ____)

# -------- #

# View data
print(cafes.head())

# Load json_normalize()
from pandas.io.json import json_normalize

# Isolate the JSON data from the API response
data = response.json()

# Flatten business data into a dataframe, replace separator
cafes = json_normalize(data["businesses"],
             sep="_")

# View data
print(cafes.head())