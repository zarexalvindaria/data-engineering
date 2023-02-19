# Use the convenience function to query the API
tesco_items = retrieve_products("____")

singer.write_schema(stream_name="products", schema=schema,
                    key_properties=[])

# ------ #

# Use the convenience function to query the API
tesco_items = retrieve_products("Tesco")

singer.write_schema(stream_name="products", schema=schema,
                    key_properties=[])