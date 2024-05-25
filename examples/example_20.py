# Input data
url = input("Enter a URL: ")

# Extract the resource name from the URL
resource_name = url.split("/")[-1]

# Print the result
print(resource_name)
