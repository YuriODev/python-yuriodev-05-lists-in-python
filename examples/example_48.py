# Read the input data
input_data = input("Enter a string of words separated by spaces: ")

# Split the input data into a list of words
words = input_data.split()

# Sort the words by length
# The key parameter specifies a function that will be called on each element
# to determine the sorting key (in this case, the length of the word)
sorted_words = sorted(words, key=len)

# Join the sorted words with ", " and add a period at the end
output = ", ".join(sorted_words) + "."

# Print the result
print(output)
