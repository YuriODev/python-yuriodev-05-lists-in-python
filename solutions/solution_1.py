# Read the input number without printing a prompt
number = int(input("Enter a five-digit number: "))

# Calculate the sums and print the result
first_part = (number // 10000) + ((number // 100) % 10) + (number % 10)
print(first_part)
second_part = ((number // 1000) % 10) + ((number // 10) % 10)

print(str(first_part) + str(second_part))
