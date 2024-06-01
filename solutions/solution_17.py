# Solution to Exercise 17

# Prompt the user to enter three integers separated by commas and spaces
input_data = input("Enter three integers (day, month, year) separated by commas and spaces: ")

# Split the input data by comma and space
date_parts = input_data.split(", ")

# Extract day, month, and year from the input
day = date_parts[0]
month = date_parts[1]
year = date_parts[2]

# Print the date in the format day/month/year
print(f"{day}/{month}/{year}")
