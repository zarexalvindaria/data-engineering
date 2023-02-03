# Load all sheets in the Excel file
all_survey_data = pd.read_excel("fcc_survey.xlsx",
                                ____)

# View the sheet names in all_survey_data
print(all_survey_data.keys())

# -------------- #

# Load all sheets in the Excel file
all_survey_data = pd.read_excel("fcc_survey.xlsx",
                                sheet_name=[0, "2017"])

# View the sheet names in all_survey_data
print(all_survey_data.keys())