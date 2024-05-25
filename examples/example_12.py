input_text = input("Enter a line of text: ")
words = input_text.split()

# Count the number of unique words
# The set() function removes duplicates from the list
# The len() function returns the number of elements in the set
unique_words = len(set(words))

# Print the result
print(unique_words)

# Alternatively, you can use a list to count the occurrences of each word

# Count the number of unique words using a list
unique_words_list = []

# Iterate over each word in the input text
for word in words:
    # Check if the word is not already in the list
    if word not in unique_words_list:
        # Add the word to the list
        unique_words_list.append(word)

# Print the result
print(len(unique_words_list))

# The output will be the same in both cases, but the list approach is less efficient
# because it requires checking each word against all the words in the list.
# The set approach is more efficient because it automatically removes duplicates
# and has a constant-time lookup for membership checks.
# The set approach is recommended for counting unique elements in a collection.
# The list approach is useful when you need to preserve the order of the elements
