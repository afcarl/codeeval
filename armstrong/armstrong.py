import sys

"""
An Armstrong number is an n-digit number that is equal to the sum of the
n'th powers of its digits. Determine if the input numbers are Armstrong
numbers.
"""


def digits_in(number):
    digits = []
    while number:
        digit = number % 10
        number = number / 10

        digits.append(digit)

    return digits


def is_armstrong(number):
    digits = digits_in(number)
    n = len(digits)

    result = 0

    for digit in digits:
        result += digit ** n

    return result == number


if __name__ == '__main__':
    with open(sys.argv[1]) as tests_handle:
        for line in tests_handle.readlines():
            result = is_armstrong(int(line.strip()))
            print('True' if result else 'False')
