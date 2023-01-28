# Create list of columns to use
cols = ____

# Create dataframe from csv using only selected columns
data = ____("vt_tax_data_2016.csv", ____)

# View counts of dependents and tax returns by income level
print(data.groupby("agi_stub").sum())

# ------------------------ #

# Create list of columns to use
cols = ("zipcode", "agi_stub", "mars1", 
        "MARS2", "NUMDEP")

# Create dataframe from csv using only selected columns
data = pd.read_csv("vt_tax_data_2016.csv", usecols=cols)

# View counts of dependents and tax returns by income level
print(data.groupby("agi_stub").sum())