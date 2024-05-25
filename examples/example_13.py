input_text = input("Enter a line of text: ")
words = input_text.split()

# Count the number of unique words
# The set() function removes duplicates from the list
# The len() function returns the number of elements in the set
unique_words = len(set(words))

# Print the result
print(unique_words)
