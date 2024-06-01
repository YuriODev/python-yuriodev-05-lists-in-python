# Solution to Exercise 2

# Prompt the user to enter names of world languages separated by spaces
input_data = input("Enter names of world languages separated by spaces: ")

# Convert the input string into a list of languages
languages = input_data.split()

# Sort the list of languages alphabetically
languages.sort()

# Reverse the list of languages
reversed_languages = languages[::-1]

# Solution using sorted function
reversed_languages = sorted(languages)[::-1]

# Print the reversed list of languages separated by spaces
print(" ".join(reversed_languages))
