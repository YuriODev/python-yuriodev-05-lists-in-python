# Define constants for the number of seconds in a day, hour, and minute
SECONDS_IN_A_DAY = 24 * 60 * 60
SECONDS_IN_AN_HOUR = 60 * 60
SECONDS_IN_A_MINUTE = 60

# Read the input number from the user
s = int(input("Enter the number of seconds: "))

# Calculate the number of days
days = s // SECONDS_IN_A_DAY
s %= SECONDS_IN_A_DAY

# Calculate the number of hours
hours = s // SECONDS_IN_AN_HOUR
s %= SECONDS_IN_AN_HOUR

# Calculate the number of minutes
minutes = s // SECONDS_IN_A_MINUTE
s %= SECONDS_IN_A_MINUTE

# The remaining seconds
seconds = s

# Print the result
print(f"{days} day(s), {hours} hour(s), {minutes} minute(s), {seconds} second(s)")
