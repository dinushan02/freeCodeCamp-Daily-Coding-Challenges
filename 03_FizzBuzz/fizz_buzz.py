"""
Generate numbers from 1 to n, replacing multiples
of 3 with Fizz, multiples of 5 with Buzz,
and multiples of both with FizzBuzz.
"""


def fizz_buzz(n):
    lst = []

    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            lst.append("FizzBuzz")
        elif i % 3 == 0:
            lst.append("Fizz")
        elif i % 5 == 0:
            lst.append("Buzz")
        else:
            lst.append(i)

    return lst


if __name__ == "__main__":
    print(fizz_buzz(2))
    print(fizz_buzz(4))
    print(fizz_buzz(8))
    print(fizz_buzz(20))
    print(fizz_buzz(50))