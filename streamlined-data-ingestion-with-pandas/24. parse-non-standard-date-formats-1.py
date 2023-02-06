# Parse datetimes and assign result back to Part2EndTime
survey_data["Part2EndTime"] = ____(____,
                                   ____)

# ------- #

# Create variable for the date format
format_string = "%m%d%Y %H:%M:%S"

# Parse datetimes and assign result back to Part2EndTime
survey_data["Part2EndTime"] = pd.to_datetime(survey_data["Part2EndTime"],
                                   format=format_string)