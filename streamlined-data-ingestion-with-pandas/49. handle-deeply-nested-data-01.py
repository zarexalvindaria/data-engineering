# Flatten businesses records and set underscore separators
flat_cafes = ____(data["businesses"],
                  ____)

# View the data
print(flat_cafes.head())

# --------- #

# Flatten businesses records and set underscore separators
flat_cafes = json_normalize(data["businesses"],
                  sep="_")

# View the data
print(flat_cafes.head())