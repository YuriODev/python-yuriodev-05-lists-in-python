# Solution to Exercise 1

# Prompt the user to enter names of world languages separated by spaces
input_data = input("Enter names of world languages separated by spaces: ")

# Convert the input string into a list of languages
languages = input_data.split()

# Sort the list of languages alphabetically
languages.sort()

# Print the sorted list of languages separated by spaces
print(" ".join(languages))
