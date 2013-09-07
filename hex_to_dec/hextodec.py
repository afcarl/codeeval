import sys

"""
You will be given a hexadecimal (base 16) number. Convert it into
decimal (base 10).
"""


def hex_to_decimal(hex):
    hex_map = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
        '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14,
        'F': 15,
    }

    result = 0

    for i, char in enumerate(list(hex)[::-1]):
        result += hex_map[char.upper()] * 16 ** i

    return result


if __name__ == '__main__':
    with open(sys.argv[1]) as tests_handle:
        for line in tests_handle.readlines():
            print(hex_to_decimal(line.strip()))
