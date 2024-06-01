# Solution to Exercise 15

# Prompt the user to enter a sequence of words separated by commas and without spaces
input_data = input("Enter a sequence of words separated by commas and without spaces: ")

# Convert the input string into a list of words
words = input_data.split(',')

# Sort the list of words alphabetically
words.sort()

# Print the sorted words separated by commas
print(",".join(words))
