# Prompt the user to enter a list of languages separated by spaces
input_languages = input("Enter languages separated by spaces: ")

# Split the input string into a list of individual languages
languages = input_languages.split()

# Reverse the order of the languages in the list
languages.reverse()

# Convert the reversed list of languages into a single string, with each language separated by a space
reversed_languages = " ".join(languages)

# Print the reversed list of languages
print(reversed_languages)
