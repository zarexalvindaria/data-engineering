# Use the convenience function to query the API
tesco_items = retrieve_products("Tesco")

singer.write_schema(stream_name="products", schema=schema,
                    key_properties=[])

# Write a single record to the stream, that adheres to the schema
singer.____(stream_name="____", 
            record={**tesco_items[0], 'store_name': "Tesco"})

# -------- #

# Use the convenience function to query the API
tesco_items = retrieve_products("Tesco")

singer.write_schema(stream_name="products", schema=schema,
                    key_properties=[])

# Write a single record to the stream, that adheres to the schema
singer.write_record(stream_name="products", 
            record={**tesco_items[0], 'store_name': "Tesco"})