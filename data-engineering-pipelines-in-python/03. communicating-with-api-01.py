endpoint = "http://localhost:5000"

# Fill in the correct API key
api_key = "____"

# Create the web API’s URL
authenticated_endpoint = "{}/{}".format(____, ____)

# Get the web API’s reply to the endpoint
api_response = requests.get(____).json()
pprint.pprint(api_response)

# ----------- #

endpoint = "http://localhost:5000"

# Fill in the correct API key
api_key = "scientist007"

# Create the web API’s URL
authenticated_endpoint = "{}/{}".format(endpoint, api_key)

# Get the web API’s reply to the endpoint
api_response = requests.get(authenticated_endpoint).json()
pprint.pprint(api_response)