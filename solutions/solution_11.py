# Solution to Exercise 11

# Prompt the user to enter a URL
input_data = input("Enter a URL: ")

# Find the position of the last slash in the URL
last_slash_position = input_data.rfind('/')

# Extract the resource name from the URL
resource_name = input_data[last_slash_position + 1:]

# Print the resource name
print(resource_name)
