# Message Validator

## 📌 Problem Description

Given a message string and a validation string, determine whether the message is valid.

A message is valid if the first letter of each word matches the corresponding letter in the validation string, in the same order.

### Requirements

- Each word must start with its corresponding validation letter.
- Letters are case-insensitive.
- Words in the message are separated by single spaces.
- The number of words must match the number of letters in the validation string.
- Return `True` if the message is valid; otherwise, return `False`.

## 💡 Examples

**Example 1**

Input:
```python
message = "hello world"
validation = "hw"
```

Output:
```python
True
```

Explanation:

- `hello` starts with `h`.
- `world` starts with `w`.
- Both letters match the validation string `hw`.

**Example 2**

Input:
```python
message = "ALL CAPITAL LETTERS"
validation = "acl"
```

Output:
```python
True
```

Explanation:

- `ALL` starts with `A`.
- `CAPITAL` starts with `C`.
- `LETTERS` starts with `L`.

Uppercase and lowercase letters are treated equally.

**Example 3**

Input:
```python
message = "Coding challenge are boring."
validation = "cca"
```

Output:
```python
False
```

Explanation:

The message contains four words, but the validation string contains only three letters. Therefore, the message is invalid.

## 🧠 Approach

The solution uses Python string methods, a `for` loop, indexing, and conditional statements.

**Step 1: Convert strings to lowercase**

Use `lower()` to make the comparison case-insensitive.

**Step 2: Separate the message into words**

Use `split()` to convert the message into a list of words.

**Step 3: Check the lengths**

Use `len()` to compare the number of words with the number of letters in the validation string.

If they are different, return `False`.

**Step 4: Compare the first letters**

Use `enumerate()` to access both the index and each word while iterating.

Use `word[0]` to get the first character of each word.

Compare it with `validation[index]`.

**Step 5: Validate the message**

- If any corresponding letters do not match, return `False`.
- If all letters match, return `True`.

## 🛠️ Python Concepts Used

| Concept | Purpose |
|---|---|
| Strings | Process the message and validation text |
| `lower()` | Convert strings to lowercase |
| `split()` | Separate a sentence into words |
| `len()` | Compare the number of words and letters |
| `enumerate()` | Access indexes and values during iteration |
| String indexing | Access the first character using `[0]` |
| `for` loop | Iterate through the words |
| Conditional statements | Compare corresponding characters |
| Boolean values | Return `True` or `False` |

## ⏱️ Complexity Analysis

Let:

- `n` = Number of characters in the message.
- `m` = Number of characters in the validation string.

**Time Complexity: O(n + m)**

- Lowercase conversion: O(n + m)
- Splitting the message: O(n)
- Length comparison: O(1)
- Comparing the first letters: O(m)

**Space Complexity: O(n + m)**

Additional memory is used for the lowercase strings and the list of words.

## 🧪 Testing

The solution was tested against all five test cases provided by freeCodeCamp.

| Test Case | Expected Result | Status |
|---|---|---|
| `("hello world", "hw")` | `True` | ✅ Passed |
| `("ALL CAPITAL LETTERS", "acl")` | `True` | ✅ Passed |
| `("Coding challenge are boring.", "cca")` | `False` | ✅ Passed |
| `("The quick brown fox jumps over the lazy dog.", "TQBFJOTLD")` | `True` | ✅ Passed |
| `("The quick brown fox jumps over the lazy dog.", "TQBFJOTLDT")` | `False` | ✅ Passed |

**Result: All 5 test cases passed!** ✅

## 📖 What I Learned

Through this challenge, I practiced:

- Working with Python string methods.
- Separating sentences into individual words.
- Using `enumerate()` to access indexes and values.
- Comparing corresponding characters.
- Using early returns to handle invalid conditions.
- Improving logical thinking through problem-solving.

## 🔗 Challenge Source

[freeCodeCamp – Daily Coding Challenge (November 24)](https://www.freecodecamp.org/learn/daily-coding-challenge/11-24)

---

**One problem at a time. One step closer to becoming a better developer.** 🚀