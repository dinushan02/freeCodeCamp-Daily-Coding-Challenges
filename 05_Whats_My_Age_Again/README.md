# What's My Age Again? – Python Solution

## 📌 Challenge Overview

**Challenge:** What's My Age Again?  
**Platform:** freeCodeCamp Daily Coding Challenge  
**Programming Language:** Python  
**Status:** Completed ✅

The goal of this challenge is to calculate a person's age based on their birthday as of November 27, 2025.

The birthday is provided in `YYYY-MM-DD` format, and the function must return the age as an integer.

## 📝 Problem Description

Given the date of someone's birthday in the format `YYYY-MM-DD`, return the person's age as of November 27, 2025.

Requirements:

- Assume all birthdays are valid dates before November 27, 2025.
- Return the age as an integer.
- Account for whether the person has already had their birthday in 2025.

## 💡 Examples

**Example 1**

```python
calculate_age("2000-11-20")
```

Output:

```python
25
```

**Example 2**

```python
calculate_age("2000-12-01")
```

Output:

```python
24
```

**Example 3**

```python
calculate_age("2014-10-25")
```

Output:

```python
11
```

## 🧠 Problem-Solving Approach

1. Use `split("-")` to separate the birthday into year, month, and day.
2. Convert the extracted values from strings into integers using `int()`.
3. Calculate the initial age by subtracting the birth year from 2025.
4. Check whether the birthday is after November 27, 2025.
5. If the birthday has not happened yet in 2025, subtract 1 from the calculated age.
6. Return the final age.

### Important Condition

```python
if month > 11 or (month == 11 and day > 27):
    age -= 1
```

This condition checks two situations:

- If the birth month is December, the birthday has not happened yet.
- If the birth month is November and the day is after 27, the birthday has not happened yet.

Otherwise, the birthday has already passed, so the initial age is correct.

## 🐍 Python Concepts Used

- Functions
- String methods (`split()`)
- Type conversion (`int()`)
- Multiple variable assignment
- Conditional statements (`if`)
- Logical operators (`and`, `or`)
- Comparison operators
- Arithmetic operators
- Return statements

## ⏱️ Complexity Analysis

**Time Complexity: O(1)**

The function performs a fixed number of operations regardless of the input size.

**Auxiliary Space Complexity: O(1)**

Only a fixed number of variables are used to calculate the age.

## 🧪 Testing

The following freeCodeCamp test cases were successfully passed:

| Test | Birthday | Expected Output | Status |
|---|---|---:|---|
| 1 | `2000-11-20` | 25 | ✅ Passed |
| 2 | `2000-12-01` | 24 | ✅ Passed |
| 3 | `2014-10-25` | 11 | ✅ Passed |
| 4 | `1994-01-06` | 31 | ✅ Passed |
| 5 | `1994-12-14` | 30 | ✅ Passed |

**Result: All test cases passed — 100% complete!**

## 📚 What I Learned

This challenge helped me practise extracting information from strings, converting data types, and writing conditional logic.

I also learned why checking both the birth month and birth day is important when calculating someone's age on a specific date.

## 🔗 Challenge Source

[freeCodeCamp – Daily Coding Challenge](https://www.freecodecamp.org/learn/daily-coding-challenge/)

---

Part of my Python problem-solving journey through freeCodeCamp Daily Coding Challenges.

**Repository:** `freeCodeCamp-Daily-Coding-Challenges`