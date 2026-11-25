# FizzBuzz

## 📌 Problem Description

Given an integer `n`, return a list of integers from `1` to `n` (inclusive), following these rules:

- Replace numbers divisible by 3 with `"Fizz"`.
- Replace numbers divisible by 5 with `"Buzz"`.
- Replace numbers divisible by both 3 and 5 with `"FizzBuzz"`.
- Keep all other numbers unchanged.

## 💡 Examples

**Example 1**

Input:
```python
fizz_buzz(2)
```

Output:
```python
[1, 2]
```

**Example 2**

Input:
```python
fizz_buzz(8)
```

Output:
```python
[1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8]
```

**Example 3**

Input:
```python
fizz_buzz(15)
```

Output:
```python
[1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz"]
```

## 🧠 Approach

The solution uses a `for` loop, conditional statements, the modulo operator, and a Python list.

**Step 1: Create an empty list**

Create an empty list to store the results.

**Step 2: Generate numbers**

Use `range(1, n + 1)` to generate numbers from 1 to `n`, including `n`.

**Step 3: Check divisibility by both 3 and 5**

Use the modulo operator `%` and the `and` operator.

If both conditions are satisfied, append `"FizzBuzz"`.

**Step 4: Check divisibility by 3**

If the number is divisible by 3, append `"Fizz"`.

**Step 5: Check divisibility by 5**

If the number is divisible by 5, append `"Buzz"`.

**Step 6: Handle other numbers**

If none of the conditions match, append the original number.

**Step 7: Return the result**

After processing all numbers, return the completed list.

### Important: Condition Order

Check divisibility by both 3 and 5 before checking individual conditions.

For example, `15` is divisible by both 3 and 5. If we check divisibility by 3 first, it could be classified as `"Fizz"` instead of `"FizzBuzz"`.

## 🛠️ Python Concepts Used

| Concept | Purpose |
|---|---|
| Functions | Define the `fizz_buzz()` function |
| Lists | Store the results |
| `range()` | Generate numbers from 1 to n |
| `for` loop | Process each number |
| Modulo operator `%` | Check divisibility |
| `and` operator | Check multiple conditions |
| `if / elif / else` | Apply the FizzBuzz rules |
| `append()` | Add results to the list |
| `return` | Return the completed list |

## ⏱️ Complexity Analysis

Let `n` represent the input integer.

**Time Complexity: O(n)**

The loop processes each number from 1 to `n` exactly once. Each divisibility check takes constant time.

**Space Complexity: O(n)**

The result list stores one element for every number from 1 to `n`.

## 🧪 Testing

The solution was tested against all five test cases provided by freeCodeCamp.

| Test Case | Input | Status |
|---|---|---|
| 1 | `fizz_buzz(2)` | ✅ Passed |
| 2 | `fizz_buzz(4)` | ✅ Passed |
| 3 | `fizz_buzz(8)` | ✅ Passed |
| 4 | `fizz_buzz(20)` | ✅ Passed |
| 5 | `fizz_buzz(50)` | ✅ Passed |

**Result: All 5 test cases passed!** ✅

## 📖 What I Learned

Through this challenge, I practiced:

- Using the modulo operator to check divisibility.
- Working with Python loops and conditional statements.
- Understanding the importance of condition order.
- Building and updating lists using `append()`.
- Solving problems using simple logical steps.

## 🔗 Challenge Source

[freeCodeCamp – Daily Coding Challenge](https://www.freecodecamp.org/learn/daily-coding-challenge/11-23)

---

**One problem at a time. One step closer to becoming a better developer.** 🚀