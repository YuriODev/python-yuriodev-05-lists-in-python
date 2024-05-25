# Read the input data
grades = input("Enter the grades separated by spaces: ").split()
# The above line prompts the user to enter grades separated by spaces and stores the input as a string.
# The string is then split into a list of individual grades using the split() method.

# Calculate the fraction of students with grade A
total_students = len(grades)
# The above line calculates the total number of students by getting the length of the grades list.

count_A = grades.count('A')
# The above line counts the number of occurrences of the grade 'A' in the grades list and stores it in the variable count_A.

fraction_A = count_A / total_students
# The above line calculates the fraction of students with grade 'A' by dividing the count of 'A' grades by the total number of students.

# Print the result formatted to two decimal places
print(f"{fraction_A:.2f}")
# The above line prints the fraction_A value formatted to two decimal places using f-string formatting.
# The ":.2f" specifies that the value should be formatted as a floating-point number with two decimal places.
