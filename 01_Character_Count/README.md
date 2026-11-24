# Character Count

## 📌 Problem Description

Given a sentence string, return an array containing the count of each alphabetic character in alphabetical order.

### Requirements

- Treat uppercase and lowercase letters as the same.
- Ignore numbers, spaces, punctuation, and special characters.
- Return each character and its count in the format `"letter count"`.
- All returned letters must be lowercase.
- Do not include characters that are not present in the sentence.

## 💡 Examples

**Example 1**

Input:
```python
"hello world"
```

Output:
```python
["d 1", "e 1", "h 1", "l 3", "o 2", "r 1", "w 1"]
```

**Example 2**

Input:
```python
"Banana"
```

Output:
```python
["a 3", "b 1", "n 2"]
```

**Example 3**

Input:
```python
"Hello123 WORLD!"
```

Output:
```python
["d 1", "e 1", "h 1", "l 3", "o 2", "r 1", "w 1"]
```

## 🧠 Approach

The solution uses a Python dictionary to count the frequency of each character.

**Step 1: Convert to lowercase**

Use `lower()` to make uppercase and lowercase letters consistent.

**Step 2: Create an empty dictionary**

Use a dictionary to store each character and its frequency.

- Key: Character
- Value: Number of occurrences

**Step 3: Iterate through the sentence**

Use a `for` loop to examine each character.

**Step 4: Ignore non-alphabetic characters**

Use `isalpha()` to check whether the current character is a letter.

**Step 5: Count character frequency**

Use `dict.get()` to retrieve the existing count or return `0` if the character is not yet in the dictionary.

Increase the count by one.

**Step 6: Sort alphabetically**

Use `sorted()` to arrange the dictionary keys in alphabetical order.

**Step 7: Format the result**

Create a list containing each character and its corresponding count in the required `"letter count"` format.

## 🛠️ Python Concepts Used

| Concept | Purpose |
|---|---|
| Strings | Process the input sentence |
| `lower()` | Convert characters to lowercase |
| `isalpha()` | Identify alphabetic characters |
| Dictionary | Store character frequencies |
| `dict.get()` | Retrieve and update counts |
| `for` loop | Iterate through characters |
| `sorted()` | Sort characters alphabetically |
| List | Store the final result |

## ⏱️ Complexity Analysis

Let:

- `n` = Number of characters in the input sentence.
- `k` = Number of distinct alphabetic characters.

**Time Complexity:**

- Lowercase conversion: O(n)
- Frequency counting: O(n) average
- Sorting distinct characters: O(k log k)
- Building the result: O(k)

Overall: **O(n + k log k)**

**Space Complexity:**

O(n + k), including the lowercase string, frequency dictionary, and result list.

## 🧪 Testing

The solution was tested against all three test cases provided by freeCodeCamp.

**Result: All test cases passed!** ✅

## 📖 What I Learned

Through this challenge, I practiced:

- Using dictionaries for frequency counting.
- Working with Python string methods.
- Filtering characters using conditions.
- Sorting dictionary keys.
- Converting dictionary data into a formatted list.

## 🔗 Challenge Source

[freeCodeCamp – Daily Coding Challenge (November 23)](https://www.freecodecamp.org/learn/daily-coding-challenge/11-23)

---

**Learning one problem at a time. Building stronger problem-solving skills every day.** 🚀