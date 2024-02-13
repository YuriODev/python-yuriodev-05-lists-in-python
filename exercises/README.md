# Exercises 🏋️‍♂️

Here are the exercises for the Python Basics module. These exercises are designed to test your understanding of the concepts covered in the module. You can use the exercises to practice and improve your Python skills.

**Covered Topics:**
- Variables and Data Types
- Numbers
- Strings
- Booleans
- User Input
- Conditional Statements

## Exercise 1: Sum of Digits - Medium 🔥 (Est. Time: 10-15 mins | Points: 10)

**Problem:** Given a five-digit decimal number, construct a new number according to specific rules: calculate the sum of the first, third, and fifth digits to form the first part of the new number, and the sum of the second and fourth digits for the second part. Output these two parts concatenated as a single number.

### Input:
- A five-digit integer.

### Output:
- A new integer formed by the specified sums.

### Examples:

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 12345  | 96      |
| 2   | 44444  | 128     |
| 3   | 11111  | 32      |

### Note:
The problem tests the ability to manipulate and process individual digits of a number.


## Exercise 2: Next Even Number - Easy 😊 (Est. Time: 5-10 mins | Points: 5)

**Problem:** Given an integer `n`, output the next even number that follows it.

### Input:
- An integer `n`.

### Output:
- The next even number after `n`.

### Examples:

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 7      | 8       |
| 2   | 10     | 12      |
| 3   | 11     | 12      |

### Note:
This exercise practices basic arithmetic operations and understanding of even numbers.


## Exercise 3: Electronic Clock - Medium 🔥 (Est. Time: 15-20 mins | Points: 10)

**Problem:** Given the number of seconds `n` that have passed since the beginning of the day, calculate what time the electronic clock will show in `h:mm:ss` format.

### Input:
- An integer `n` representing the number of seconds.

### Output:
- The time in `h:mm:ss` format.

### Examples:

| No. | Inputs   | Outputs    |
| --- | -------- | ---------- |
| 1   | 3602     | 1:00:02    |
| 2   | 4556789  | 17:46:29   |
| 3   | 4568     | 1:16:08    |

### Note:
Assumes a 24-hour clock format and tests understanding of time conversion.

## Exercise 4: Symmetric Number - Medium 🔥 (Est. Time: 10-15 mins | Points: 10)

**Problem:** Determine if a given four-digit number is symmetric. If it is, print 1; otherwise, print any other integer. Assume the number is left-padded with zeros if it has less than four digits.

### Input:
- A four-digit integer or fewer, left-padded with zeros if necessary.

### Output:
- 1 if the number is symmetric, or another integer if it is not.

### Examples:

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 2002   | 1       |
| 2   | 1234   | 0       |
| 3   | 1221   | 1       |

### Note:
This problem tests the ability to analyze and compare digits within a number.

## Exercise 5: Maximum of Two - Easy 😊 (Est. Time: 5-10 mins | Points: 5)

**Problem:** Read two integers `a` and `b`, and print the maximum value between them. Use only integer arithmetic operations; branching, loops, or functions cannot be used.

### Input:
- Two integers `a` and `b`.

### Output:
- The maximum value between `a` and `b`.

### Examples:

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 8<br>5 | 8       |
| 2   | 5<br>3 | 5       |
| 3   | 7<br>9 | 9       |

### Note:
Focuses on understanding and applying basic arithmetic operations to find the maximum of two numbers.

## Exercise 6: Divisibility Check - Easy 😊 (Est. Time: 5-10 mins | Points: 5)

**Problem:** Determine if the number `a` is divisible by `b` without a remainder using only arithmetic operations. Branching, loops, and functions are prohibited. Output "YES" if divisible, otherwise "NO".

### Input:
- Two integers `a` and `b`.

### Output:
- "YES" if `a` is divisible by `b`, otherwise "NO".

### Examples:

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 10<br>2| YES     |
| 2   | 5<br>3 | NO      |
| 3   | 15<br>5| YES     |

### Note:
Tests the application of arithmetic and boolean algeebra operations to solve divisibility.


## Exercise 7: Sum of Digits (Easy) - Easy 😊 (Est. Time: 5-10 mins | Points: 5)

**Problem:** Write a program to calculate the sum of digits in a 4-digit integer entered by the user.

### Input:
- A 4-digit integer.

### Output:
- The sum of the digits of the given integer.

### Examples:

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 4273   | 16      |
| 2   | 1221   | 6       |
| 3   | 3355   | 16      |

### Note:
This exercise enhances the understanding of digit manipulation and summation.


## Exercise 8: Integer Sorting - Easy 😊 (Est. Time: 10-15 mins | Points: 10)


**Problem:** Write a program to sort three integers without using conditional expressions or loops.

### Examples:

| No. | Inputs      | Outputs    |
| --- | ----------- | ---------- |
| 1   | 8<br>1<br>5 | 1<br>5<br>8 |
| 2   | 3<br>2<br>9 | 2<br>3<br>9 |
| 3   | 7<br>4<br>6 | 4<br>6<br>7 |

### Note:
The task focuses on using mathematical operations or built-in functions that do not involve explicit condition checking or iteration to sort the numbers.

## Exercise 9: Hour Hand Angle - Medium 🔥 (Est. Time: 15-20 mins | Points: 10)

**Problem:** Given `h` hours, `m` minutes, and `s` seconds have passed since the beginning of the day (with 0 < `h` < 12, 0 ≤ `m` < 60, and 0 ≤ `s` < 60), calculate and output the angle (in degrees) by which the hour hand has turned from the start of the day. Conditional constructions and cycles are not allowed for solving this problem.

### Inputs:
- `h`: Hours since the beginning of the day.
- `m`: Minutes past the hour.
- `s`: Seconds past the minute.

### Output:
- The angle in degrees of the hour hand's rotation since the start of the day.

### Examples:

| No. | Inputs         | Outputs |
| --- | -------------- | ------- |
| 1   | 2<br>30<br>0   | 75      |
| 2   | 10<br>0<br>0   | 300     |
| 3   | 6<br>0<br>0    | 180     |

### Note:
This exercise requires applying the knowledge of clock mechanics and mathematical relationships between time and angles without the use of conditionals or looping constructs.


## Exercise 10: Minute Hand Angle - Medium 🔥 (Est. Time: 15-20 mins | Points: 10)

**Problem:** Given the angle `a` by which the hour hand has turned since the beginning of the day, determine the angle by which the minute hand has turned since the beginning of the last hour. The input and output data are real numbers. Note that conditional constructions and cycles cannot be used in solving this problem.

### Variables:
- **Input (`a`)**: The angle (in degrees) by which the hour hand has turned since the beginning of the day.
- **Output**: The angle (in degrees) by which the minute hand has turned since the beginning of the last hour.

### Approach:
Understand the relationship between the hour hand's movement and the minute hand's movement:
- The hour hand moves 30 degrees per hour.
- The minute hand moves 6 degrees per minute.

Given `a`, the task is to calculate the minute hand's angle since the beginning of the last hour without using conditional constructions or cycles.

### Input-Output Data:

| No. | Inputs | Outputs |
| --- | ------ | ------- |
| 1   | 190    | 120.0   |
| 2   | 170    | 240.0   |
| 3   | 370    | 120.0   |

### Notes:
- Inputs and outputs are to be considered with respect to a 12-hour clock cycle.
- It's essential to translate the hour hand's angle into the corresponding minute position within an hour and then calculate the minute hand's angle based on this position.


## Exercise 11: Bill Denominations - Medium 🔥 (Est. Time: 10-15 mins | Points: 10)


**Problem:** After purchasing goods for a total of `s` dollars, determine the number of bills of different denominations that should be given to the seller, starting with the largest denomination. Available denominations are 1, 2, 5, 10, 100, and 500 dollars.

### Input:
- **`s`**: The total cost of the goods purchased, in dollars.

### Output:
The number of bills for each denomination to be given, starting from the largest (500 dollars) to the smallest (1 dollar).

### Examples:

| No. | Inputs | Outputs                                   |
| --- | ------ | ----------------------------------------- |
| 1   | 534    | 1 (500), 0 (100), 3 (10), 0 (5), 4 (1)    |
| 2   | 1245   | 2 (500), 2 (100), 4 (10), 1 (5), 0 (1)    |
| 3   | 12     | 0 (500), 0 (100), 1 (10), 0 (5), 2 (1)    |
| 4   | 786    | 1 (500), 2 (100), 8 (10), 1 (5), 1 (1)    |
| 5   | 377    | 0 (500), 3 (100), 7 (10), 1 (5), 2 (1)    |

### Note:
The goal is to minimize the number of bills by always starting with the largest denomination that does not exceed the remaining amount to be given.

# Problems in Order of Difficulty According to ChatGPT

The exercises provided range from basic arithmetic operations and logical reasoning to more intricate manipulations of time and numerical digits. Here's a summary of the exercises ordered by difficulty, starting with the easiest and moving to relatively more challenging problems.

## Easy 😊

1. **Exercise 2: Next Even Number** - Focuses on identifying the next even number following a given integer.
2. **Exercise 5: Maximum of Two** - Tests basic arithmetic operations to find the maximum of two integers.
3. **Exercise 6: Divisibility Check** - Requires checking divisibility without remainder using arithmetic operations.
4. **Exercise 7: Sum of Digits** - Involves calculating the sum of digits in a 4-digit integer.
5. **Exercise 8: Integer Sorting** - Aimed at sorting three integers without conditional expressions or loops.

## Medium 🔥

1. **Exercise 1: Sum of Digits** - Combines digit manipulation to form a new number based on the sum of specific digits.
2. **Exercise 3: Electronic Clock** - Involves converting seconds into `h:mm:ss` format, testing understanding of time conversion.
3. **Exercise 4: Symmetric Number** - Tests for symmetry in a four-digit number without using conditionals.
4. **Exercise 9: Hour Hand Angle** - Requires calculating the angle of the hour hand based on time passed.
5. **Exercise 10: Minute Hand Angle** - Determines the angle of the minute hand since the beginning of the last hour, given the hour hand's angle.
6. **Exercise 11: Bill Denominations** - Focuses on minimizing the number of bills returned for a given amount using specific denominations.

Each exercise is designed to test different aspects of problem-solving, from simple arithmetic to more complex calculations and logical reasoning. While none of the problems are classified as Hard, they collectively offer a comprehensive review of essential programming and mathematical concepts.

Overall, the estimated completion time for the exercises ranges from 5 minutes for the simplest tasks to 20 minutes for the more complex ones. This gives an average expected time of approximately 10-15 minutes per exercise, depending on the student's prior knowledge and experience.

# Checking Your Score with Autograder 📝

GitHub Classroom's autograder provides immediate feedback on your exercises. Each exercise is worth points based on its complexity, with a total of `90` points available across all exercises. 

When you commit and push your solution, GitHub Actions will run tests on your code. If all tests for an exercise pass, you will be awarded the full points for that exercise. If some tests fail, partial points may be awarded. 

The workflow will run all tests, even if some fail. The total score will be shown in the workflow output as `points scored/total points available`. For example, if you see `10/90`, it means you've successfully completed the first problem worth `10` points.

Please note that the workflow will show as failed if any test fails, even if you've successfully solved some problems. Look for the points tally in the output to see your score.

Remember, practice makes perfect! If you don't pass all tests the first time, review your code, make improvements, and try again. You can push new changes as many times as you need.

# Running Your Code and Tests Locally 🖥️

To run your code and tests locally, you can use the following commands:

1. Run the code:
```bash
python exercises/exercise_1.py
```

2. Run the tests:

To run the tests for an exercise, you'll use the pytest framework. First, make sure you have pytest installed: 

```bash
pip install pytest
```

Then, you can run the tests for a specific exercise using the following command:

```bash
python -m unittest exercises/test_exercise_1.py
```

Replace `exercise_1` with the exercise you're working on (e.g., `exercise_2`, `exercise_3`, etc.) and `test_exercise_1` with the corresponding test file.

