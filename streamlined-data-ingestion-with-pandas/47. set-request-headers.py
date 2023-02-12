# Create dictionary that passes Authorization and key string
headers = {____: "Bearer {}".format(____)}

# Query the Yelp API with headers and params set
response = ____



# Extract JSON data from response
data = ____

# Load "businesses" values to a dataframe and print names
cafes = ____
print(cafes.name)

# -------- #

# Create dictionary that passes Authorization and key string
headers = {"Authorization": "Bearer {}".format(api_key)}

# Query the Yelp API with headers and params set
response = requests.get(api_url,
            params=params,
            headers=headers)


# Extract JSON data from response
data = response.json()

# Load "businesses" values to a dataframe and print names
cafes = pd.DataFrame(data["businesses"])
print(cafes.name)