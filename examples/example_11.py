# Read the input data
file_name = input("Enter the full file name: ")

# Extract the file extension
# Split the file name by the dot character and get the last element
file_extension = file_name.split('.')[-1]

# Print the result
print(file_extension)
