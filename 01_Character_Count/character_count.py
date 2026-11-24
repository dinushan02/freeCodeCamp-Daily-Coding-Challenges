"""
Count the occurrences of each alphabetic character
in a sentence and return them in alphabetical order.
"""


def count_characters(sentence):
    sentence = sentence.lower()

    frequency = {}

    for char in sentence:
        if char.isalpha():
            frequency[char] = frequency.get(char, 0) + 1

    result = []

    for char in sorted(frequency):
        result.append(f"{char} {frequency[char]}")

    return result


if __name__ == "__main__":
    text = "Hello World!"

    result = count_characters(text)

    print(result)