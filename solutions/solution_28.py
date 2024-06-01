# Solution to Exercise 28

# Prompt the user to enter a sequence of integers separated by spaces
input_data = input("Enter a sequence of integers separated by spaces: ")

# If the input string contains only one number, print the number and exit
if len(input_data) == 1:
    print(input_data)

else:
    # Convert the input string into a list of integers
    numbers = list(map(int, input_data.split()))

    # Use list unpacking to separate the head and the tail
    head, *tail = numbers

    # Print the head (the first element)
    print(head)

    # Print the tail (all other elements)
    print(" ".join(map(str, tail)))
