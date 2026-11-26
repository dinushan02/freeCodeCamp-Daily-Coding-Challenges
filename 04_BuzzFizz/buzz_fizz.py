"""
BuzzFizz

Determine whether an array represents a correct FizzBuzz
sequence starting from 1.

Rules:
- Multiples of 3 are replaced with "Fizz".
- Multiples of 5 are replaced with "Buzz".
- Multiples of both 3 and 5 are replaced with "FizzBuzz".
- All other numbers remain integers.
"""


def is_fizz_buzz(sequence):
    for index, value in enumerate(sequence, start=1):

        if index % 3 == 0 and index % 5 == 0:
            result = "FizzBuzz"
        elif index % 3 == 0:
            result = "Fizz"
        elif index % 5 == 0:
            result = "Buzz"
        else:
            result = index

        if value != result:
            return False

    return True


if __name__ == "__main__":
    print(is_fizz_buzz([1, 2, "Fizz", 4]))
    print(is_fizz_buzz([1, 2, 3, 4]))
    print(is_fizz_buzz([1, 2, "Fizz", 4, "Buzz", 7]))
    print(is_fizz_buzz([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14]))
    print(is_fizz_buzz([1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, "Buzz"]))
