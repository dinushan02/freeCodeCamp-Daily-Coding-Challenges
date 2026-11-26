# BuzzFizz – Python Solution

## 📌 Challenge Overview

**Challenge:** BuzzFizz
**Platform:** freeCodeCamp Daily Coding Challenge
**Programming Language:** Python
**Status:** Completed ✅

The goal of this challenge is to determine whether a given array represents a correct FizzBuzz sequence starting from 1.

The sequence must follow the FizzBuzz rules and contain no missing or extra elements.

## 📝 Problem Description

Given an array, determine if it is a correct FizzBuzz sequence from 1 to the last item in the array.

A sequence is correct if:

- Numbers that are multiples of 3 are replaced with `"Fizz"`.
- Numbers that are multiples of 5 are replaced with `"Buzz"`.
- Numbers that are multiples of both 3 and 5 are replaced with `"FizzBuzz"`.
- All other numbers remain as integers in ascending order, starting from 1.
- The array must start at 1 and have no missing or extra elements.

## 💡 Examples

**Example 1**

```python
is_fizz_buzz([1, 2, "Fizz", 4])
```

Output:

```python
True
```

**Example 2**

```python
is_fizz_buzz([1, 2, 3, 4])
```

Output:

```python
False
```

**Example 3**

```python
is_fizz_buzz([1, 2, "Fizz", 4, "Buzz", 7])
```

Output:

```python
False
```

## 🧠 Problem-Solving Approach

1. Use `enumerate()` with `start=1` to get the correct position of each element.
2. Check whether the current position is divisible by both 3 and 5.
3. If it is divisible by both, the expected value is `"FizzBuzz"`.
4. Otherwise, check whether it is divisible by 3 or 5.
5. If neither condition is satisfied, the expected value is the original integer.
6. Compare the expected value with the actual array element.
7. Return `False` immediately if they do not match.
8. If every element matches, return `True`.

## 🐍 Python Concepts Used

- Functions
- Lists
- `for` loops
- `enumerate()`
- Conditional statements (`if`, `elif`, `else`)
- Modulo operator (`%`)
- Comparison operators
- Boolean values (`True` and `False`)
- Early return

## ⏱️ Complexity Analysis

**Time Complexity: O(n)**

The function visits each element in the sequence exactly once.

**Auxiliary Space Complexity: O(1)**

The solution uses only a few variables and does not create additional lists or dictionaries.

Where `n` represents the number of elements in the input sequence.

## 🧪 Testing

- [x] Correct sequence
- [x] Incorrect integer instead of Fizz
- [x] Incorrect sequence ending
- [x] Incorrect FizzBuzz position
- [x] Incorrect Buzz position
- [x] Long invalid sequence
- [x] Long valid sequence

**Result: All freeCodeCamp test cases passed — 100% complete!**

## 📚 What I Learned

Through this challenge, I practiced using `enumerate()` to track positions in a sequence and applying conditional logic to validate each element.

I also improved my understanding of the modulo operator, early returns, and efficient iteration.

## 🔗 Challenge Source

[freeCodeCamp – Daily Coding Challenge](https://www.freecodecamp.org/learn/daily-coding-challenge/)

---

Part of my Python problem-solving journey through freeCodeCamp Daily Coding Challenges.

**Repository:** `freeCodeCamp-Daily-Coding-Challenges`