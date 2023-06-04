# Load pandas as pd
import pandas as pd
import requests
import json
import re

def count_age(url):

    r = requests.get(url)
    data = r.text
    json_data = json.loads(data)

    # Find all matches of the pattern `key=(\w+), age=(\w+),?` in the `json_data['data']` string.
    matches = re.findall("key=(\w+), age=(\w+),?", json_data['data'])

    # Create a DataFrame with two columns, one for the `key` and one for the `age`.
    df = pd.DataFrame(matches, columns=['key', 'age'])

    df = df.astype({'age':'int'})

    result = df.query('age >= 50')
    
    # return the rows with ages greater than or equal to 50
    return result

url = "https://coderbyte.com/api/challenges/json/age-counting"
print(count_age(url))