# Read the input data
# Prompt the user to enter the number of words and convert it to an integer
num_words = int(input("Enter the number of words: "))

# Prompt the user to enter the length of words to be edited and convert it to an integer
word_length = int(input("Enter the length of words to be edited: "))

# Prompt the user to enter the replacement character
replacement_char = input("Enter the replacement character: ")

# Read the list of words
# Prompt the user to enter each word in the list, and store them in a list,
# based on the number of words entered
words = [input() for _ in range(num_words)]

# Replace the last three characters of words with the specified length
# Iterate over each word in the list and replace the last three characters
# with the replacement character if the word length matches the specified length
modified_words = [word[:-3] + replacement_char if len(word) == word_length else word for word in words]  

# Print the result
print(modified_words)  # Print the modified list of words
