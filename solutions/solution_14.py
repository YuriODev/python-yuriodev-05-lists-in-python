# Solution to Exercise 14

# Prompt the user to enter four integers representing the coordinates of two points
input_data = input("Enter four integers (x1, y1, x2, y2) separated by spaces: ")

# Convert the input string into a list of integers
coordinates = list(map(int, input_data.split()))

# Extract the coordinates
x1, y1, x2, y2 = coordinates

# Calculate the distance between the two points using the distance formula
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

# Print the distance rounded to two decimal places
print(f"{distance:.2f}")
