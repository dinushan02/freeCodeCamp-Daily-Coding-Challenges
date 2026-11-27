"""
What's My Age Again?

Calculate a person's age as of November 27, 2025, based on their birthday in YYYY-MM-DD format.
"""


def calculate_age(birthday):
    year, month, day = birthday.split("-")

    year = int(year)
    month = int(month)
    day = int(day)

    age = 2025 - year

    if month > 11 or (month == 11 and day > 27):
        age -= 1

    return age


if __name__ == "__main__":
    print(calculate_age("2000-11-20"))  # 25
    print(calculate_age("2000-12-01"))  # 24
    print(calculate_age("2014-10-25"))  # 11
    print(calculate_age("1994-01-06"))  # 31
    print(calculate_age("1994-12-14"))  # 30
