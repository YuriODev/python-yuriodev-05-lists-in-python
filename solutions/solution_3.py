# Read the input
n = int(input())

# Calculate the hours, minutes, and seconds
hours = (n // 3600) % 24
minutes = (n // 60) % 60
seconds = n % 60

# Print the time in h:mm:ss format
print(f"{hours}:{minutes:02d}:{seconds:02d}")
