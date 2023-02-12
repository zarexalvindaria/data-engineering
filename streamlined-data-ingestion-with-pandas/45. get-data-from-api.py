api_url = "https://api.yelp.com/v3/businesses/search"

# Get data about NYC cafes from the Yelp API
response = ____(____, 
                headers=headers, 
                params=params)

# Extract JSON data from the response
data = response.____

# Load data to a dataframe
cafes = ____(____)

# View the data's dtypes
print(cafes.dtypes)

# ----------- #

api_url = "https://api.yelp.com/v3/businesses/search"

# Get data about NYC cafes from the Yelp API
response = requests.get(api_url, 
                headers=headers, 
                params=params)

# Extract JSON data from the response
data = response.json()

# Load data to a dataframe
cafes = pd.DataFrame(data["businesses"])

# View the data's dtypes
print(cafes.dtypes)
# print(cafes)