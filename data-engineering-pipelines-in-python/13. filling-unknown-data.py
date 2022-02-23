print("BEFORE")
ratings.show()

print("AFTER")
# Replace nulls with arbitrary value on column subset
ratings = ratings.____(____, subset=["____"])
ratings.show()

# --------- #

print("BEFORE")
ratings.show()

print("AFTER")
# Replace nulls with arbitrary value on column subset
ratings = ratings.fillna(4, subset=["comfort"])
ratings.show()