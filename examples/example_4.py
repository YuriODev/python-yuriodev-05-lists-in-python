# Read the input numbers from the user
t = int(input("Enter the number of minutes Helen needs to sleep: "))
h = int(input("Enter the hour Helen goes to bed: "))
m = int(input("Enter the minute Helen goes to bed: "))

# Calculate the total minutes from midnight when Helen should wake up
total_minutes = h * 60 + m + t

# Convert the total minutes to hours and minutes
wake_up_hour = (total_minutes // 60) % 24
wake_up_minute = total_minutes % 60

# Print the hours and minutes on separate lines
print(wake_up_hour)
print(wake_up_minute)
