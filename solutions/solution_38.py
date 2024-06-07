# Solution to Exercise 38

number = input("Enter a number: ")

numbers_list = list(number)

max_number = sorted(numbers_list, reverse=True)
print("".join(max_number))

min_number = sorted(numbers_list)
count_zeros = min_number.count('0')
zeros = ['0'] * count_zeros

min_number = [min_number[count_zeros]] + zeros + min_number[count_zeros+1:]  

print("".join(min_number))

