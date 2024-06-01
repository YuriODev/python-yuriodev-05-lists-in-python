# Solution to Exercise 34

# Prompt the user to enter a string of words separated by spaces
input_data = input("Enter a string of words separated by spaces: ")

# Convert the input string into a list of words
words = input_data.split()

# Find the length of the longest word(s)
max_length = max(len(word) for word in words)

# Find and print the longest word(s)
longest_words = [word for word in words if len(word) == max_length]
print(" ".join(longest_words))
