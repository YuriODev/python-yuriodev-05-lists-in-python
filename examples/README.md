# Examples 👨🏼‍💻

Here are some examples to get you started.

<details open>
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

<details open>
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


<details open>
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

<details open>
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

<details open>
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

<details open>
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

<!-- 414 -->
## Example 6: Count Positive Elements

**Problem:** Find the number of positive elements in an entered list. The list of numbers is entered on a single line.

| No. | Inputs          | Outputs |
| --- | --------------- | ------- |
| 1   | 2 -4 5 6 -3     | 3       |
| 2   | 1 2 3 4 5       | 5       |
| 3   | -1 -2 -3 -4 -5  | 0       |
| 4   | 0 0 0 0 0       | 0       |
| 5   | 1 2 3 4 5       | 5       |


<details open>
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


<details open>
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


<details open>
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

<details open>
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
## Example 10: Print Elements that Exceed Previous Elements

**Problem:** Given a list of integers entered on a single line, print each element that is greater than the one preceding it. The numbers should be output in the same order as they appear in the list, separated by spaces.

| No. | Inputs            | Outputs  |
| --- | ----------------- | -------- |
| 1   | 5 8 0 2 9 4 1    | 8 2 9    |
| 2   | 3 5 7 6 9 10 8   | 5 7 9 10 |
| 3   | 1 1 2 3 2 2 5 1  | 2 3 5    |
| 4   | 10 9 8 7 6       |          |
| 5   | 6 7 7 8 10 9 10  | 7 8 10 10 |

<details open>
<summary><b>Python Solution</b></summary>

```python
input_numbers = input("Enter numbers separated by spaces: ")
numbers = list(map(int, input_numbers.split()))

# List of elements that exceed the previous element
exceeding_elements = [numbers[i] for i in range(1, len(numbers)) if numbers[i] > numbers[i - 1]]

```
</details>


<!-- 424 -->
## Example 11: Count Unique Words in a Line

**Problem:** Given a line of text, determine how many unique words are present. A word is defined by sequences of characters separated by spaces. Case sensitivity should be considered, meaning "New" and "new" would count as two different words.

| No. | Inputs                                                                                                                                                          | Outputs |
| --- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| 1   | New Delhi New York Paris Prague Reykjavik                                                                                                                      | 6       |
| 2   | Happy New Year Happy New Year May we all have a vision now and then Of a world where every neighbor is a friend                                                | 19      |

<details open>
<summary><b>Python Solution</b></summary>

```python
input_text = input("Enter a line of text: ")
words = input_text.split()

# Count the number of unique words
unique_words = len(set(words))

print(unique_words)
```
</details>

<!-- 429 -->
## Example 12: Count Days Above Average Temperature

**Problem:** Given a line of space-separated temperature readings for a series of days, determine how many days had temperatures not lower than the average temperature over the period.

### Input/Output Examples
| No. | Inputs                        | Outputs |
| --- | ----------------------------- | ------- |
| 1   | -3 -1 0 2 6 8 12 15          | 4       |


<!-- 432 -->
Напишіть програму, щоб перевірити, чи певне ціле число n перевищує всі елементи цілочисельного списку. Значення списку вводяться через пропуск в одному рядку, число n вводиться у новому рядку.

Вхідні дані:

4 67 109 25 44 12
99
Вихідні дані:

False


**Notes:** All the examples above are solved using Python. You can find the solutions in the [examples](./examples) folder. Covered with explanations and comments, these examples will help you understand the practical implementation of the concepts covered in this module. Python tests are also included to verify the correctness of the solutions.
