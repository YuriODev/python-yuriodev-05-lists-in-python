# Define constants for the number of minutes in an hour and the number of hours in a day
MINUTES_IN_AN_HOUR = 60
HOURS_IN_A_DAY = 24

# Read the input number from the user
n = int(input("Enter the number of minutes that have passed since midnight: "))

# Calculate the number of hours
hours = (n // MINUTES_IN_AN_HOUR) % HOURS_IN_A_DAY

# Calculate the number of minutes
minutes = n % MINUTES_IN_AN_HOUR

# Print the result
print(f"{hours}, {minutes}")
