# Load required libraries
import pandas as pd
import requests
import json
import re

"""This function counts the number of ages in the dataframe
 that are greater than or equal to 50"""
def count_age(url):

    # Get the data from the api
    data = requests.get(url).text

    # Parse the data and convert it to object
    json_data = json.loads(data)

    # Find all the matches of the pattern `key=(\w+), age=(\w+),?` in the `json_data['data']` string
    matches = re.findall("key=(\w+), age=(\w+),?", json_data['data'])

    # Create a DataFrame with `key` and `age` columns
    df = pd.DataFrame(matches, columns=['key', 'age'])

    # Convert the data type of age to integer to allow querying
    df = df.astype({'age':'int'})

    # Filter the data frame with ages 50 or higher
    filtered_df = df.query('age >= 50')

    # Store the count of rows with age of 50 or higher in the result variable
    result = filtered_df.agg(['count'], axis='index')
    
    # return the rows with ages greater than or equal to 50
    return result

url = "https://coderbyte.com/api/challenges/json/age-counting"
print(count_age(url))