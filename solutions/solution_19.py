# Solution to Exercise 19

# Prompt the user to enter a string in underscore format
input_data = input("Enter a string in underscore format: ")

# Split the input string by underscores
words = input_data.split('_')

# Convert the first letter of each word to uppercase and join them without spaces
camel_case_string = ''.join(word.capitalize() for word in words)

# Print the string in CamelCase format
print(camel_case_string)
