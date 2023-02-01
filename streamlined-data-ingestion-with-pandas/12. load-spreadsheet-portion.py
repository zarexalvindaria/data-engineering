# Create string of lettered columns to load
col_string = ____

# Load data with skiprows and usecols set
survey_responses = ____("fcc_survey_headers.xlsx", 
                        ____, 
                        ____)

# View the names of the columns selected
print(survey_responses.columns)

# ------------ #

# Create string of lettered columns to load
col_string = "AD, AW:BA"

# Load data with skiprows and usecols set
survey_responses = pd.read_excel("fcc_survey_headers.xlsx", 
                        skiprows=2, 
                        usecols=col_string)

# View the names of the columns selected
print(survey_responses.columns)