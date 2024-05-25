# Read the input data
input_data = input("Enter a string of words separated by spaces: ")

# Split the input data into a list of words
words = input_data.split()

# Sort the words by length
# The key function is the len function, which returns the length of each word
# The sorted function sorts the words based on their length
sorted_words = sorted(words, key=len)

# Join the sorted words with ", " and add a period at the end
output = ", ".join(sorted_words) + "."

# Print the result
print(output)

# Alternative solution using pure Python
# Read the input data
input_data = input("Enter a string of words separated by spaces: ")

# Split the input data into a list of words
words = input_data.split()

# Sort the words by length using sorting algorithm (bubble sort)
n = len(words)

# Iterate over the range of numbers from 0 to n-1
for i in range(n):
    # Iterate over the range of numbers from 0 to n-i-1
    # The range decreases with each iteration to avoid unnecessary comparisons
    for j in range(0, n-i-1):
        # Compare the length of the current word with the length of the next word
        if len(words[j]) > len(words[j+1]):
            # Swap the positions of the current word and the next word if the current word is longer
            words[j], words[j+1] = words[j+1], words[j]


# Join the sorted words with ", " and add a period at the end
output = ", ".join(words) + "."

# Print the result
print(output)

