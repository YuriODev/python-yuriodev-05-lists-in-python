# Read the input data
expression = input("Enter the math expression: ")

# Split the expression into parts
parts = expression.split()
a = int(parts[0])
operator = parts[1]
b = int(parts[2])

# Perform the operation based on the operator
if operator == "plus":
    result = a + b
elif operator == "minus":
    result = a - b
elif operator == "multiply":
    result = a * b
elif operator == "divide":
    result = a // b
else:
    result = "Unknown operator"

# Print the result
print(result)