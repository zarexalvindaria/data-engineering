# Specify record path to get categories data
flat_cafes = json_normalize(data["businesses"],
                            sep="_",
                    		____)

# View the data
print(flat_cafes.head())

# ----- #

# Specify record path to get categories data
flat_cafes = json_normalize(data["businesses"],
                            sep="_",
                    		record_path="categories")

# View the data
print(flat_cafes.head())