"""
Validate whether each word in a message starts
with the corresponding letter in the validation string.
"""


def is_valid_message(message, validation):
    message = message.lower()
    validation = validation.lower()

    words = message.split()

    if len(words) != len(validation):
        return False

    for index, word in enumerate(words):
        if word[0] != validation[index]:
            return False

    return True


if __name__ == "__main__":
    print(is_valid_message("hello world", "hw"))
    print(is_valid_message("ALL CAPITAL LETTERS", "acl"))
    print(is_valid_message("Coding challenge are boring.", "cca"))
    print(is_valid_message("The quick brown fox jumps over the lazy dog.", "TQBFJOTLD"))
    print(is_valid_message("The quick brown fox jumps over the lazy dog.", "TQBFJOTLDT"))
