# Read the input data
input_data = input("Enter a list of words separated by commas: ")

# Split the input data into a list of words
words = input_data.split(',')

# Strip any leading/trailing spaces from each word and convert to lowercase for sorting
words = [word.strip() for word in words]

# Sort the words in descending order without considering case
sorted_words = sorted(words, key=lambda word: word.lower(), reverse=True)

# Join the sorted words with spaces and print the result
output = " ".join(sorted_words)

print(output)
