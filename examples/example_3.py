# Read the input number from the user
t = int(input("Enter the number of minutes after midnight: "))

# Calculate the hours and minutes
hours = t // 60
minutes = t % 60

# Print the result using f-string
print(f"{hours}\n{minutes}")
