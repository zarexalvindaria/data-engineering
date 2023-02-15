# Complete the JSON schema
schema = {'properties': {
    'brand': {'type': 'string'},
    'model': {____: ____},
    'price': {'type': 'number'},
    'currency': {'type': ____},
    'quantity': {'type': ____, 'minimum': 1},  
    ____: {'type': 'string', 'format': 'date'},
    ____: {____: ____, 'pattern': "^[A-Z]{2}$"}, 
    'store_name': {'type': 'string'}}}

# Write the schema
singer.____(stream_name=____, schema=____, key_properties=[])

# -------- #

# Complete the JSON schema
schema = {'properties': {
    'brand': {'type': 'string'},
    'model': {'type': 'string'},
    'price': {'type': 'number'},
    'currency': {'type': 'string'},
    'quantity': {'type': 'number', 'minimum': 1},  
    'date': {'type': 'string', 'format': 'date'},
    'countrycode': {'type': 'string', 'pattern': "^[A-Z]{2}$"}, 
    'store_name': {'type': 'string'}}}

# Write the schema
singer.write_schema(stream_name="products", schema=schema, key_properties=[])