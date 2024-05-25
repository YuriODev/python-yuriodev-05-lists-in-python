# Examples 👨🏼‍💻

Here are some examples to get you started.

<details close>
<summary><b>Covered topics</b></summary>

| Topic Covered                                           | Code with explanations                            |
| ------------------------------------------------------- | ------------------------------------------------- |
| Repeat Last Two Characters                              | [Detailed code](./example_1.py)                   |
| Reverse Digits                                          | [Detailed code](./example_2.py)                   |
| Check Start of String                                   | [Detailed code](./example_3.py)                   |
| Number reversal                                         | [Detailed code](./example_4.py)                   |
| Palindrome String                                       | [Detailed code](./example_5.py)                   |
| Is Digit Check                                          | [Detailed code](./example_6.py)                   |
| Digits and Characters                                   | [Detailed code](./example_7.py)                   |
| The first word in a string                              | [Detailed code](./example_8.py)                   |
| Access Code Calculation                                 | [Detailed code](./example_9.py)                   |
| ASCII Characters                                        | [Detailed code](./example_10.py)                  |
| Count Words in a String                                 | [Detailed code](./example_11.py)                  |
| String Len                                              | [Detailed code](./example_12.py)                  |
| Digits and Characters Count                             | [Detailed code](./example_13.py)                  |
| Vowel and Consonant Check                               | [Detailed code](./example_14.py)                  |
| Sum of Sequence Elements Calculation                    | [Detailed code](./example_15.py)                  |
| Uppercase, Lowercase, and Space Count                   | [Detailed code](./example_16.py)                  |
| Remove Duplicate Characters                             | [Detailed code](./example_17.py)                  |
| Find and Replace Substring                              | [Detailed code](./example_18.py)                  |
| Longest Sequence of Zeros                               | [Detailed code](./example_19.py)                  |
| Can Construct                                           | [Detailed code](./example_20.py)                  |
| Check Bracket Balance                                   | [Detailed code](./example_21.py)                  |
| Evaluate Expression                                     | [Detailed code](./example_22.py)                  |
| Count String Occurrences                                | [Detailed code](./example_23py)                   |
| Format Number with Commas                               | [Detailed code](./example_24.py)                  |
| Find and Replace Substring                              | [Detailed code](./example_25.py)                  |
| Find Shortest Word and Its Length                       | [Detailed code](./example_26.py)                  | 
| Run-Length Encoding                                     | [Detailed code](./example_27.py)                  |
| Evaluate Simple Arithmetic Expression                   | [Detailed code](./example_28.py)                  |
| Find Most Frequent Letters                              | [Detailed code](./example_29.py)                  |
| Validate IP Address                                     | [Detailed code](./example_30.py)                  |

</details>

<!-- 406 -->
## Example 1: Move Last Two Elements

**Problem:** Create a list based on a given sequence of integers and print its elements in such a way that the last two elements are moved from the end to the beginning of the list without changing their initial order.

| No. | Inputs            | Outputs            |
| --- | ----------------- | ------------------ |
| 1   | 4 10 2 9 4 7 3    | 7 3 4 10 2 9 4     |
| 2   | 1 2 3 4 5 6 7 8 9 | 8 9 1 2 3 4 5 6 7  |
| 3   | 1 2 3 4 5         | 4 5 1 2 3          |
| 4   | 1 2               | 1 2                |
| 5   | 1                 | 1                  |

<details close>
<summary><b>Python Solution</b></summary>

```python
input_sequence = input("Enter a sequence of integers: ")
numbers = list(map(int, input_sequence.split()))

if len(numbers) >= 2:
    # Extract the last two elements
    last_two = numbers[-2:]
    # Remove the last two elements
    remaining_numbers = numbers[:-2]
    # Create the new list with the last two elements at the beginning
    new_order = last_two + remaining_numbers
    print(" ".join(map(str, new_order)))
```
</details>

<!-- 409 -->
## Example 2: Reverse Language List

**Problem:** Save the names of world languages entered in a single line separated by spaces into a list. Print the elements of the list in reverse order in a single line separated by spaces.

| No. | Inputs                                          | Outputs                                         |
| --- | ----------------------------------------------- | ----------------------------------------------- |
| 1   | Ukrainian French Bulgarian Norwegian Latvian    | Latvian Norwegian Bulgarian French Ukrainian    |
| 2   | English German Spanish Italian French           | French Italian Spanish German English           |
| 3   | russian Ukrainian Belarusian Polish             | Polish Belarusian Ukrainian russian            |
| 4   | English French German Italian Spanish           | Spanish Italian German French English           |


<details close>
<summary><b>Python Solution</b></summary>

```python
input_languages = input("Enter languages separated by spaces: ")
languages = input_languages.split()
# Reverse the list
languages.reverse()
# Print the reversed list as a single space-separated string
print(" ".join(languages))
```
</details>


<!-- 410 -->
## Example 3: Print List in Reverse Order

**Problem:** Print the elements of a given list in reverse order without modifying the list itself.

| No. | Inputs       | Outputs       |
| --- | ------------ | ------------- |
| 1   | 2 6 1 7 9    | 9 7 1 6 2     |
| 2   | 1 2 3 4 5    | 5 4 3 2 1     |
| 3   | 5 4 3 2 1    | 1 2 3 4 5     |
| 4   | 1 3 5 7 9    | 9 7 5 3 1     |
| 5   | 9 8 7 6 5    | 5 6 7 8 9     |

<details close>
<summary><b>Python Solution</b></summary>

```python
input_numbers = input("Enter numbers separated by spaces: ")
numbers = list(map(int, input_numbers.split()))
# Print the list in reverse order without altering the original list
print(" ".join(map(str, numbers[::-1])))

```
</details>


<!-- 411 -->
## Example 4: Print Elements at Even Indices

**Problem:** Print all elements of a list that have even indices. The list of numbers is entered on a single line.

| No. | Inputs         | Outputs    |
| --- | -------------- | ---------- |
| 1   | 1 2 3 4 5      | 1 3 5      |
| 2   | 2 4 6 8 10     | 2 6 10     |
| 3   | 3 6 9 12 15    | 3 9 15     |
| 4   | 4 8 12 16 20   | 4 12 20    |
| 5   | 5 10 15 20 25  | 5 15 25    |

<details close>
<summary><b>Python Solution</b></summary>

```python
input_numbers = input("Enter numbers separated by spaces: ")
numbers = list(map(int, input_numbers.split()))
# Select and print elements with even indices
print(" ".join(map(str, numbers[::2])))

```
</details>

<!-- 412 -->

## Example 5: Print Elements Less Than n

**Problem:** Write a program that prints only those elements from an entered list that are less than a given value `n`. The list contains unique values.

| No. | Inputs                               | Outputs                   |
| --- | ------------------------------------ | ------------------------- |
| 1   | 2 7 11 3 8 90 144 15 5<br>94        | 2 7 11 3 8 90 15 5       |
| 2   | 1 2 3 4 5 6 7 8 9 10<br>5      | 1 2 3 4                   |
| 3   | 1 2 3 4 5 6 7 8 9 10<br>10     | 1 2 3 4 5 6 7 8 9         |
| 4   | 1 2 3 4 5 6 7 8 9 10<br>1      |                           |
| 5   | 1 2 3 4 5 6 7 8 9 10<br>0      | 1 2 3 4 5 6 7 8 9         |

<details close>
<summary><b>Python Solution</b></summary>

```python
input_numbers = input("Enter numbers separated by spaces: ")
n = int(input("Enter the threshold number n: "))
numbers = list(map(int, input_numbers.split()))
# Filter and print elements less than n
filtered_numbers = [num for num in numbers if num < n]
print(" ".join(map(str, filtered_numbers)))

```
</details>


## Example 6: Count Positive Elements

**Problem:** Find the number of positive elements in an entered list. The list of numbers is entered on a single line.

| No. | Inputs          | Outputs |
| --- | --------------- | ------- |
| 1   | 2 -4 5 6 -3     | 3       |
| 2   | 1 2 3 4 5       | 5       |
| 3   | -1 -2 -3 -4 -5  | 0       |
| 4   | 0 0 0 0 0       | 0       |
| 5   | 1 2 3 4 5       | 5       |


<details close>
<summary><b>Python Solution</b></summary>

```python
input_numbers = input("Enter numbers separated by spaces: ")
numbers = list(map(int, input_numbers.split()))
# Count and print the number of positive elements
positive_count = sum(1 for num in numbers if num > 0)
print(positive_count)

```
</details>


<!-- 416 -->
## Example 7: Print Unique Elements in Order

**Problem:** Given a list of numbers entered on a single line, print those elements that appear only once in the list. The elements should be printed in the order they appear in the list.

| No. | Inputs                 | Outputs |
| --- | ---------------------- | ------- |
| 1   | 4 5 6 6 6 5 4 4 7 4   | 7       |
| 2   | 1 2 3 4 5 6 7 8 9 10  | 1 2 3 4 5 6 7 8 9 10 |
| 3   | 1 2 3 4 5 2 3 4 5 6   | 1 6     |
| 4   | 1 2 3 4 5 6 7 8 9 10  | 1 2 3 4 5 6 7 8 9 10 |


<details close>
<summary><b>Python Solution</b></summary>

```python
input_numbers = input("Enter numbers separated by spaces: ")
numbers = list(map(int, input_numbers.split()))

# List to store unique elements in order
unique_list = [num for num in numbers if numbers.count(num) == 1]

# Print unique elements in order
print(" ".join(map(str, unique_list)))

```
</details>


<!-- 418 -->
## Example 8: Access and Print Indices and Values of List Elements

**Problem:** Write a program to access the index of integer elements in a list. The numbers in the list are entered on a single line, separated by spaces.

| No. | Inputs                | Outputs  |
| --- | --------------------- | -------- |
| 1   | 3 44 6 8 9 12 7       | 0 3<br>1 44<br>2 6<br>3 8<br>4 9<br>5 12<br>6 7 |
| 2   | 1 2 3 4 5 6 7 8 9 10 | 0 1<br>1 2<br>2 3<br>3 4<br>4 5<br>5 6<br>6 7<br>7 8<br>8 9<br>9 10 |
| 3   | 1 2 3 | 0 1<br>1 2<br>2 3 |


<details close>
<summary><b>Python Solution</b></summary>

```python
input_numbers = input("Enter numbers separated by spaces: ")
numbers = list(map(int, input_numbers.split()))

# Output the index and value of each element
for index, value in enumerate(numbers):
    print(index, value)

```
</details>

<!-- 419 -->
## Example 9: Find Most Frequent Number

**Problem:** Given a list of numbers entered on a single line, determine the number that occurs most frequently without modifying the list or using additional lists. If there are multiple numbers with the same highest frequency, output any one of them.

| No. | Inputs                      | Outputs |
| --- | --------------------------- | ------- |
| 1   | 1 0 0 1 0 0 1 1 0          | 0       |
| 2   | 2 4 6 9 9 2 3 2 4          | 2       |

<details close>
<summary><b>Python Solution</b></summary>

```python
input_numbers = input("Enter numbers separated by spaces: ")
numbers = list(map(int, input_numbers.split()))

# Initialize variables to track the most frequent number
most_frequent = None
max_count = 0
current_count = 0

# Sort the numbers and iterate through them to find the most frequent
sorted_numbers = sorted(numbers)
for i in range(len(sorted_numbers)):
    if i == 0 or sorted_numbers[i] == sorted_numbers[i - 1]:
        current_count += 1
    else:
        current_count = 1

    if current_count > max_count:
        max_count = current_count
        most_frequent = sorted_numbers[i]

print(most_frequent)
```
</details>


<!-- 420 -->
## Example 10: Print Elements Greater Than Previous

**Problem:** Enter a list of integers in a single line separated by spaces. Print all the elements that are greater than the previous element in the list, separated by spaces in a new line in the order they appear in the list.

| No. | Inputs                | Outputs        |
| --- | --------------------- | -------------- |
| 1   | 5 8 0 2 9 4 1         | 8 2 9          |
| 2   | 3 3 4 5 2 1 7 8 6     | 4 5 7 8        |
| 3   | 1 2 3 1 2 3 1 2 3     | 2 3 2 3 2 3    |
| 4   | 10 5 6 7 8 3 2 1      | 6 7 8          |

<details close>
<summary><b>Python Solution</b></summary>

```python
# Read the input data
input_data = input("Enter a sequence of integers separated by spaces: ")

# Convert the input data to a list of integers
numbers = list(map(int, input_data.split()))

# Find the elements greater than the previous one
result = [numbers[i] for i in range(1, len(numbers)) if numbers[i] > numbers[i-1]]

# Print the result
print(" ".join(map(str, result)))
```
</details>

<!-- 422 -->
## Example 11: Print File Extension

**Problem:** Write a program that receives the full name of a file from the user and prints the extension of the received file.

| No. | Inputs                | Outputs    |
| --- | --------------------- | ---------- |
| 1   | test.cpp              | cpp        |
| 2   | document.pdf          | pdf        |
| 3   | image.jpeg            | jpeg       |
| 4   | archive.tar.gz        | gz         |

<details close>
<summary><b>Python Solution</b></summary>

```python
# Read the input data
file_name = input("Enter the full file name: ")

# Extract the file extension
file_extension = file_name.split('.')[-1]

# Print the result
print(file_extension)
```
</details>

<!-- 424 -->
## Example 13: Count Unique Words in a Line

**Problem:** Given a line of text, determine how many unique words are present. A word is defined by sequences of characters separated by spaces. Case sensitivity should be considered, meaning "New" and "new" would count as two different words.

| No. | Inputs                                                                                                                                                          | Outputs |
| --- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| 1   | New Delhi New York Paris Prague Reykjavik                                                                                                                      | 6       |
| 2   | Happy New Year Happy New Year May we all have a vision now and then Of a world where every neighbor is a friend                                                | 19      |
| 3   | The quick brown fox jumps over the lazy dog                                                                                                                    | 9       |


<details close>
<summary><b>Python Solution</b></summary>

```python
input_text = input("Enter a line of text: ")
words = input_text.split()

# Count the number of unique words
unique_words = len(set(words))

print(unique_words)
```
</details>

<!-- 427 -->
## Example 13: List Statistics

**Problem:** Create a program that receives a sequence of integers and prints the smallest number in the list, the largest number in the list, the number of elements in the list, and the average value of the elements in the list.

| No. | Inputs                | Outputs          |
| --- | --------------------- | ---------------- |
| 1   | 1 3 7 5               | 1                |
|     |                       | 7                |
|     |                       | 4                |
|     |                       | 4.0              |
| 2   | 10 20 30 40 50        | 10               |
|     |                       | 50               |
|     |                       | 5                |
|     |                       | 30.0             |
| 3   | -5 0 5 10 15          | -5               |
|     |                       | 15               |
|     |                       | 5                |
|     |                       | 5.0              |
| 4   | 100 200 300           | 100              |
|     |                       | 300              |
|     |                       | 3                |
|     |                       | 200.0            |

<details close>
<summary><b>Python Solution</b></summary>

```python
# Read the input data
input_data = input("Enter a sequence of integers separated by spaces: ")

# Convert the input data to a list of integers
numbers = list(map(int, input_data.split()))

# Find the smallest number
min_number = min(numbers)

# Find the largest number
max_number = max(numbers)

# Find the number of elements
count_numbers = len(numbers)

# Find the average value
average_value = sum(numbers) / count_numbers

# Print the results
print(min_number)
print(max_number)
print(count_numbers)
print(average_value)
```
</details>

<!-- 429 -->
## Example 14: Count Days Above Average Temperature

**Problem:** Given a line of space-separated temperature readings for a series of days, determine how many days had temperatures not lower than the average temperature over the period.

| No. | Inputs                        | Outputs |
| --- | ----------------------------- | ------- |
| 1   | -3 -1 0 2 6 8 12 15          | 4       |
| 2   | 10 12 14 16 18 20 22 24 26   | 9       |
| 3   | 10 15 8 6 4 2 0 -2 -4        | 2       |

<details close>
<summary><b>Python Solution</b></summary>

```python
input_temperatures = input("Enter temperatures separated by spaces: ")

temperatures = list(map(int, input_temperatures.split()))

# Calculate the average temperature
average_temperature = sum(temperatures) / len(temperatures)

# Count the number of days with temperatures not lower than the average
days_above_average = sum(1 for temp in temperatures if temp >= average_temperature)

print(days_above_average)
```
</details>


<!-- 431 -->
## Example 15: Print Even Numbers Until a Specific Number

**Problem:** Write a program to print all even numbers from the entered list of numbers in the same order and stop printing if the number `n` or zero is encountered in the list. The list values are entered separated by spaces in one line, the number `n` is entered in a new line.

| No. | Inputs                  | Outputs |
| --- | ----------------------- | ------- |
| 1   | 1 8 9 0 4 2 5 6\n2      | 8       |
| 2   | 3 5 7 8 2 10 4\n10      | 8 2     |
| 3   | 12 14 16 0 18 20\n18    | 12 14 16|
| 4   | 2 4 6 8 10 12\n6        | 2 4     |

<details close>
<summary><b>Python Solution</b></summary>

```python
# Read the input data
input_data = input("Enter a list of numbers separated by spaces: ")
stop_number = int(input("Enter the stop number: "))

# Convert the input data to a list of integers
numbers = list(map(int, input_data.split()))

# Iterate through the list and print even numbers until stop_number or zero is encountered
for number in numbers:
    if number == stop_number or number == 0:
        break
    if number % 2 == 0:
        print(number)
```
</details>




<!-- 432 -->
## Example 16: Check If an Integer Exceeds All List Elements

**Problem:** Given a list of integers entered on a single line, separated by spaces, and an integer \( n \) entered on a new line, write a program to check if \( n \) is greater than all the elements in the list.

| No. | Inputs         | Outputs |
| --- | -------------- | ------- |
| 1   | 4 67 109 25 44 12<br>99 | False |
| 2   | 1 2 3 4 5 6 7 8 9 10<br>11 | True |
| 3   | 1 2 3 4 5 6 7 8 9 10<br>10 | False |

<details close>
<summary><b>Python Solution 1</b></summary>

```python
input_numbers = input("Enter numbers separated by spaces: ")
numbers = list(map(int, input_numbers.split()))

n = int(input("Enter an integer n: ")

# Check if n exceeds all elements in the list
exceeds_all = all(n > num for num in numbers)

print(exceeds_all)
```
</details>

<details close>
<summary><b>Python Solution 2</b></summary>

```python
input_numbers = input("Enter numbers separated by spaces: ")
numbers = list(map(int, input_numbers.split()))

n = int(input("Enter an integer n: ")

# Check if n exceeds all elements in the list
exceeds_all = n > max(numbers)

print(exceeds_all)
```
</details>


<!-- 433 -->
## Example 16: Print List of Positive Numbers

**Problem:** Integers (both positive and negative) are entered separated by spaces in one line. Write a program to print a list of only the entered positive numbers.

| No. | Inputs                 | Outputs       |
| --- | ---------------------- | ------------- |
| 1   | 0 9 -4 6 8 -15 4       | [9, 6, 8, 4]  |
| 2   | -10 -20 30 40 -50 60   | [30, 40, 60]  |
| 3   | 1 -1 2 -2 3 -3 4 -4    | [1, 2, 3, 4]  |
| 4   | -5 -10 15 20 -25 30    | [15, 20, 30]  |

<details close>
<summary><b>Python Solution</b></summary>

```python
# Read the input data
input_data = input("Enter a list of integers separated by spaces: ")

# Convert the input data to a list of integers
numbers = list(map(int, input_data.split()))

# Create a list of positive numbers
positive_numbers = [num for num in numbers if num > 0]

# Print the result
print(positive_numbers)
```
</details>


<!-- 434 -->
## Example 17: Extract Resource Name from URL

**Problem:** Write a program to extract the part of a URL string that indicates the resource name (e.g., the filename or path segment at the end of the URL).

| No. | Inputs                                           | Outputs     |
| --- | ------------------------------------------------ | ----------- |
| 1   | https://www.namesite.com/folder/index.html       | index.html  |
| 2   | http://example.org/archive/2024/article1234.html | article1234.html |
| 3   | ftp://files.example.net/downloads/setup.exe     | setup.exe   |
| 4   | https://api.site.com/v2/user/profile             | profile     |
| 5   | https://www.example.com/                         |             |


<details close>
<summary><b>Python Solution</b></summary>

```python
url = input("Enter a URL: ")

# Extract the resource name from the URL
resource_name = url.split("/")[-1]

print(resource_name)
```
</details>


<!-- 435 -->
## Example 18: Find the Smallest Integer

**Problem:** Write a program to get the smallest integer from a list. The list values are entered separated by spaces in one line.

| No. | Inputs                | Outputs |
| --- | --------------------- | ------- |
| 1   | 87 6 25 7 105 23 56   | 6       |
| 2   | 15 20 5 10 30         | 5       |
| 3   | 1 2 3 4 5             | 1       |
| 4   | 100 200 300 400       | 100     |

<details close>
<summary><b>Python Solution</b></summary>

```python
# Read the input data
input_data = input("Enter a list of integers separated by spaces: ")

# Convert the input data to a list of integers
numbers = list(map(int, input_data.split()))

# Find the smallest number
min_number = min(numbers)

# Print the result
print(min_number)

```
</details>


<!-- 436 -->

## Example 19: Find the Second Smallest Element in a List

**Problem:** Write a program to find the second smallest element in a list of integers. The integers are entered on a single line, separated by spaces.

| No. | Inputs                 | Outputs |
| --- | ---------------------- | ------- |
| 1   | 20 56 14 9 1 15       | 9       |
| 2   | 4 3 2 1               | 2       |
| 3   | 45 22 12 8 10         | 10      |
| 4   | 100 90 80 70 60       | 70      |
| 5   | -5 -9 -1 -6 -2        | -5      |

<details close>
<summary><b>Python Solution</b></summary>

```python
input_numbers = input("Enter numbers separated by spaces: ")

numbers = list(map(int, input_numbers.split()))

# Find the second smallest element
second_smallest = sorted(set(numbers))[1]

print(second_smallest)
```
</details>

<!-- 439 -->
## Example 20: Simple Math Expression Interpreter

**Problem:** Write a simple math expression interpreter. The input is a string with an expression consisting of two numbers (0 ≤ a, b ≤ 1000) joined by a binary operator: `a operator b`, where `operator` can be one of the words: `plus`, `minus`, `multiply`, `divide` for addition, subtraction, multiplication, and integer division, respectively. The result of the computation is a string containing an integer.

| No. | Inputs                | Outputs |
| --- | --------------------- | ------- |
| 1   | 20 plus 7             | 27      |
| 2   | 15 minus 9            | 6       |
| 3   | 144 multiply 2        | 288     |
| 4   | 49 divide 7           | 7       |

<details close>
<summary><b>Python Solution</b></summary>

```python
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
    raise ValueError("Unknown operator")

# Print the result
print(result)

```
</details>


<!-- 441 -->

## Example 21: Find Largest Element and Its First Index

**Problem:** Write a program to determine the element in a list with the highest value. Print the value of the largest element followed by the index of its first occurrence. If the largest element is not unique, print the index of the first occurrence of this largest element.

| No. | Inputs                         | Outputs |
| --- | ------------------------------ | ------- |
| 1   | 2 5 10 0 4 7 11 5 8           | 11 6    |
| 2   | 23 92 34 92 55 12             | 92 1    |
| 3   | -3 -1 -7 -1 -5                | -1 1    |
| 4   | 1 2 3 4 5 6 7 8 9 10          | 10 9    |
| 5   | 5 5 5 5 5                     | 5 0     |

<details close>
<summary><b>Python Solution</b></summary>

```python
input_numbers = input("Enter numbers separated by spaces: ")

numbers = list(map(int, input_numbers.split()))

# Find the largest element and its first index
largest = max(numbers)

first_index = numbers.index(largest)

print(largest, first_index)
```
</details>

<!-- 442 -->
## Example 22: Count Non-Repeating Elements in Sorted List

**Problem:** Given a sequence of integers, determine the number of elements in the sorted list that do not repeat one after another.

| No. | Inputs                               | Outputs |
| --- | ------------------------------------ | ------- |
| 1   | 1 9 10 3 7 5 2 2 3 0 4 5 6           | 10      |
| 2   | 5 3 8 8 2 1 1 0 9 6 4 4 7            | 9       |
| 3   | 4 5 6 7 7 8 9 10 10 11               | 8       |
| 4   | 3 3 3 3 3 3                          | 1       |

<details close>
<summary><b>Python Solution</b></summary>

```python
# Read the input data
input_data = input("Enter a sequence of integers separated by spaces: ")

# Convert the input data to a list of integers
numbers = list(map(int, input_data.split()))

# Sort the list
numbers.sort()

# Count the number of non-repeating elements
unique_count = 0
for i in range(len(numbers)):
    if i == 0 or numbers[i] != numbers[i-1]:
        unique_count += 1

# Print the result
print(unique_count)
```
</details>


<!-- 443 -->
## Example 23: Cyclically Shift List Elements to the Right

**Problem:** Write a program that cyclically shifts the elements of a list to the right. This means the last element becomes the first, and all other elements move one position to the right. The numbers are entered on a single line.

| No. | Inputs       | Outputs    |
| --- | ------------ | ---------- |
| 1   | 2 0 2 5      | 5 2 0 2    |
| 2   | 6            | 6          |
| 3   | 1 2 3        | 3 1 2      |

<details close>
<summary><b>Python Solution</b></summary>

```python
input_numbers = input("Enter numbers separated by spaces: ")

numbers = list(map(int, input_numbers.split()))

# Check how many elements are in the list
if len(numbers) > 1:
    # Shift the elements to the right
    shifted = [numbers[-1]] + numbers[:-1]
    print(" ".join(map(str, shifted)))
else:
    print(numbers[0])
```
</details>

<!-- 445 -->
## Example 24: Swap Minimum and Maximum in a List

**Problem:** For a given sequence of unique integers, swap the positions of the minimum and maximum elements. Print the resulting list.

| No. | Inputs               | Outputs       |
| --- | -------------------- | ------------- |
| 1   | 1 9 12 5 3 8        | 12 9 1 5 3 8  |
| 2   | 5 10 15 20 25 30    | 5 10 15 20 25 30 |
| 3   | 3 2 1 4 5 6         | 3 2 1 4 5 6   |
| 4   | 1 2 3 4 5 6         | 6 2 3 4 5 1   |

<details close> 
<summary><b>Python Solution 1</b></summary>

```python
input_numbers = input("Enter numbers separated by spaces: ")

numbers = list(map(int, input_numbers.split()))

# Find the indices of the minimum and maximum elements
min_index = numbers.index(min(numbers))
max_index = numbers.index(max(numbers))

# Swap the minimum and maximum elements
numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]

print(" ".join(map(str, numbers)))
```
</details>


<details close> 
<summary><b>Python Solution 2 - Swap all mins and all max</b></summary>

```python
input_numbers = input("Enter numbers separated by spaces: ")

numbers = list(map(int, input_numbers.split()))

# Find the indices of the minimum and maximum elements
min_value = min(numbers)

max_value = max(numbers)

for i in range(len(numbers)):
    if numbers[i] == min_value:
        numbers[i] = max_value
    elif numbers[i] == max_value:
        numbers[i] = min_value

print(" ".join(map(str, numbers)))
```
</details>


<!-- 446 -->
## Example 25: Count Equal Pairs in a List

**Problem:** Given a list of numbers, count how many pairs of elements have the same value. Each pair should be considered only once, regardless of how many times the elements appear in the list.

| No. | Inputs                   | Outputs |
| --- | ------------------------ | ------- |
| 1   | 1 2 2 2 3 3 4           | 4       |
| 2   | 4 5 5 8 10 12 3 3       | 2       |
| 3   | 1 5 2 8 9 5            | 1       |

<details close>
<summary><b>Python Solution</b></summary>

```python
input_numbers = input("Enter numbers separated by spaces: ")

numbers = list(map(int, input_numbers.split()))

# Count the number of equal pairs
equal_pairs = sum(numbers.count(num) // 2 for num in set(numbers))

print(equal_pairs)
```
</details>


<!-- 448 -->
## Example 26: Swap Adjacent Elements in Pairs

**Problem:** Given a sequence of integers, swap each pair of adjacent elements (A[0] with A[1], A[2] with A[3], etc.). Print the resulting list. If the list has an odd number of elements, leave the last element in its original position.

| No. | Inputs        | Outputs       |
| --- | ------------- | ------------- |
| 1   | 1 4 5 3 7     | 4 1 3 5 7     |
| 2   | 4 2 10 5      | 2 4 5 10      |
| 3   | 2             | 2             |
| 4   | 1 2 3 4 5     | 2 1 4 3 5     |

<details close>
<summary><b>Python Solution</b></summary>

```python
input_numbers = input("Enter numbers separated by spaces: ")

numbers = list(map(int, input_numbers.split()))

# Solution 1 - Swap adjacent elements in pairs
swapped = [numbers[i + 1] if i % 2 == 0 else numbers[i - 1] for i in range(len(numbers))]

# Solution 2 - Using for loop
swapped = []
for i in range(0, len(numbers), 2):
    swapped.extend([numbers[i + 1], numbers[i]])


print(" ".join(map(str, swapped)))
```
</details>



<!-- 450 -->

## Example 27: Find and Print Adjacent Elements with the Same Sign

**Problem:** Given a list of integers, identify and print adjacent elements that have the same sign. If no such pair exists, nothing should be printed.

### Input/Output Examples
| No. | Inputs                     | Outputs     |
| --- | -------------------------- | ----------- |
| 1   | 1 -2 -3 5 6 -3 7 8         | -2 -3<br>5 6<br>7 8 |

<details close>
<summary><b>Python Solution</b></summary>

```python
input_numbers = input("Enter numbers separated by spaces: ")

numbers = list(map(int, input_numbers.split()))

# Find and print adjacent elements with the same sign
for i in range(len(numbers) - 1):
    if numbers[i] * numbers[i + 1] > 0:
        print(numbers[i], numbers[i + 1])
```
</details>

<!-- 452 -->
## Example 28: Calculate the Product of Integers

**Problem:** Write a program to calculate the product of integers (without using a `for` loop) entered by the user in one line separated by spaces.

| No. | Inputs                | Outputs |
| --- | --------------------- | ------- |
| 1   | 2 5 3                 | 30      |
| 2   | 1 4 7                 | 28      |
| 3   | 6 2 9                 | 108     |
| 4   | 10 20 30              | 6000    |

<details close>
<summary><b>Python Solution</b></summary>

```python
# Read the input data
input_data = input("Enter a list of integers separated by spaces: ")

# Convert the input data to a list of integers
numbers = list(map(int, input_data.split()))

# Calculate the product without using loops or subroutines
length = len(numbers)
index = 0
product = 1

while index < length:
    product *= numbers[index]
    index += 1

# Print the result
print(product)

```
</details>


<!-- 453  -->
## Example 29: Print Squares of Sequence Elements

**Problem:** Write a program that takes a sequence of integers as input and prints the squares of all its elements.

### Input/Output Examples
| No. | Inputs               | Outputs                        |
| --- | -------------------- | ------------------------------ |
| 1   | 1 2 3 4 5 6 7 8 9   | 1 4 9 16 25 36 49 64 81       |
| 2   | 2 4 6 8 10 12 14 16  | 4 16 36 64 100 144 196 256    |
| 3   | 3 6 9 12 15 18 21 24 | 9 36 81 144 225 324 441 576   |

<details close>
<summary><b>Python Solution</b></summary>

```python
input_numbers = input("Enter numbers separated by spaces: ")

numbers = list(map(int, input_numbers.split()))

# Print the squares of the elements
squares = [num ** 2 for num in numbers]

print(" ".join(map(str, squares)))
```
</details>


<!-- 454 -->
## Example 30: Remove Even Numbers from List

**Problem:** Write a program to print the elements of a given integer list after removing the even numbers. The list values are entered separated by spaces in one line.

| No. | Inputs                | Outputs       |
| --- | --------------------- | ------------- |
| 1   | 3 44 6 8 9 12 7       | [3, 9, 7]     |
| 2   | 1 2 3 4 5 6 7 8 9     | [1, 3, 5, 7, 9]|
| 3   | 10 21 32 43 54 65 76  | [21, 43, 65]  |
| 4   | 22 33 44 55 66 77     | [33, 55, 77]  |

<details close>
<summary><b>Python Solution</b></summary>

```python
# Read the input data
input_data = input("Enter a list of integers separated by spaces: ")

# Convert the input data to a list of integers
numbers = list(map(int, input_data.split()))

# Filter out even numbers
odd_numbers = [num for num in numbers if num % 2 != 0]

# Print the result
print(odd_numbers)
```
</details>

<!-- 454 -->
## Example 31: Remove Even Numbers from List

**Problem:** Write a program to print the elements of a given integer list after removing the even numbers. The list values are entered separated by spaces in one line.

| No. | Inputs                | Outputs       |
| --- | --------------------- | ------------- |
| 1   | 3 44 6 8 9 12 7       | [3, 9, 7]     |
| 2   | 1 2 3 4 5 6 7 8 9     | [1, 3, 5, 7, 9]|
| 3   | 10 21 32 43 54 65 76  | [21, 43, 65]  |
| 4   | 22 33 44 55 66 77     | [33, 55, 77]  |

<details close>
<summary><b>Python Solution</b></summary>

```python
# Read the input data
input_data = input("Enter a list of integers separated by spaces: ")

# Convert the input data to a list of integers
numbers = list(map(int, input_data.split()))

# Filter out even numbers
odd_numbers = [num for num in numbers if num % 2 != 0]

# Print the result
print(odd_numbers)
```
</details>


<!-- 455 -->
## Example 32: Find Common Elements Between Two Sequences

**Problem:** Given two sequences of integers, with elements separated by spaces and commas, write a program that returns a sequence containing only the elements that are common between the entered sequences (without duplicates). Ensure that your program works on two sequences of different sizes.

| No. | Inputs                                          | Outputs      |
| --- | ----------------------------------------------- | ------------ |
| 1   | 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89            | 1 2 3 5 8 13 |
|     | 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13       |              |
| 2   | 4, 6, 9, 2, 1                                   | 1 2 6        |
|     | 1, 2, 6, 6, 6, 10                               |              |
| 3   | 10, 20, 30, 40, 50                              | 50           |
|     | 50, 60, 70                                      |              |
| 4   | 11, 22, 33, 44, 55, 66, 77                      | 22 66        |
|     | 22, 66                                          |              |

<details close>
<summary><b>Python Solution</b></summary>

```python
# Read the input data
input_data1 = input("Enter the first list of integers separated by spaces and commas: ")
input_data2 = input("Enter the second list of integers separated by spaces and commas: ")

# Convert the input data to sets of integers
set1 = set(map(int, input_data1.replace(',', '').split()))
set2 = set(map(int, input_data2.replace(',', '').split()))

# Find the intersection of the two sets
common_elements = sorted(set1.intersection(set2))

# Print the result
print(" ".join(map(str, common_elements)))
```
</details>




<!-- 456 -->

## Example 33: Filter Binary Numbers Divisible by 5

**Problem:** Write a program that takes a sequence of 4-digit binary numbers separated by commas as input, and prints those numbers which are divisible by 5, in a line separated by commas.

### Input/Output Examples
| No. | Inputs                        | Outputs  |
| --- | ----------------------------- | -------- |
| 1   | 0100,0011,1010,1001,1100      | 1010     |

<details close>
<summary><b>Python Solution 1</b></summary>

```python
input_numbers = input("Enter binary numbers separated by commas: ")

numbers = input_numbers.split(",")
# Filter and print binary numbers divisible by 5
divisible_by_5 = [num for num in numbers if int(num, 2) % 5 == 0]

print(",".join(divisible_by_5))
```
</details>

<details close>
<summary><b>Python Solution 2</b></summary>

```python
input_numbers = input("Enter binary numbers separated by commas: ")

numbers = input_numbers.split(",")

# Filter and print binary numbers using loop and manual conversion
# from binary to decimal
divisible_by_5 = []
for num in numbers:
    decimal = sum(int(bit) * 2 ** (3 - i) for i, bit in enumerate(num))

    if decimal % 5 == 0:
        divisible_by_5.append(num)

print(",".join(divisible_by_5))
```
</details>

<details close>
<summary><b>Python Solution 3</b></summary>
    
```python
input_numbers = input("Enter binary numbers separated by commas: ")

numbers = input_numbers.split(",")

# Filter and print binary numbers using loop and manual conversion
# from binary to decimal
divisible_by_5 = []
for num in numbers:
    decimal = 0
    string_num = num[::-1]

    for i in range(len(string_num)):
        decimal += int(string_num[i]) * 2 ** i
    
    if decimal % 5 == 0:
        divisible_by_5.append(num)

print(",".join(divisible_by_5))
```
</details>

<!-- 459 -->

## Example 34: Determine Position in a Descending Sequence of Heights

**Problem:** Given a descending sequence of natural numbers representing the heights of students, followed by a single height entry for a new student, determine the position where the new student should be placed among the others. The new student should stand behind others of the same height if present. All numbers are natural and do not exceed 200.

### Input/Output Examples
| No. | Inputs                              | Outputs |
| --- | ----------------------------------- | ------- |
| 1   | 165 163 160 160 157 157 155 154<br>160 | 5       |

<details close>
<summary><b>Python Solution</b></summary>

```python
input_heights = input("Enter heights separated by spaces: ")

heights = list(map(int, input_heights.split()))

new_height = int(input("Enter the height of the new student: "))

# Find the position for the new student

position = 1
for height in heights:
    if new_height >= height:
        break
    position += 1

print(position)
```
</details>


<!-- 462 -->
## Example 35: Calculate Fraction of Students with Grade A

**Problem:** Write a program that calculates the fraction of students who received a grade of `A`. The grading system uses five grades: `A`, `B`, `C`, `D`, `F`. A string of student grades separated by spaces is entered. There is always at least one grade. Output a decimal number with exactly two decimal places.

| No. | Inputs                           | Outputs |
| --- | -------------------------------- | ------- |
| 1   | A B A A B C A D F                | 0.44    |
| 2   | A A A A A                        | 1.00    |
| 3   | A F                              | 0.50    |
| 4   | B B C B F F B C F                | 0.00    |

<details close>
<summary><b>Python Solution</b></summary>

```python
# Read the input data
grades = input("Enter the grades separated by spaces: ").split()

# Calculate the fraction of students with grade A
total_students = len(grades)
count_A = grades.count('A')
fraction_A = count_A / total_students

# Print the result formatted to two decimal places
print(f"{fraction_A:.2f}")
```
</details>





**Notes:** All the examples above are solved using Python. You can find the solutions in the [examples](./examples) folder. Covered with explanations and comments, these examples will help you understand the practical implementation of the concepts covered in this module. Python tests are also included to verify the correctness of the solutions.
