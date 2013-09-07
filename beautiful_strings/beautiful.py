import re
import sys

"""
Given a string s, little Johnny defined the beauty of the string as the
sum of the beauty of the letters in it. The beauty of each letter is an
integer between 1 and 26, inclusive, and no two letters have the same
beauty.
"""


def beauty_of(string):
    chars = list(re.sub('[^\w]', '', string.lower()))

    score = 26
    result = 0

    for char in sorted(set(chars), key=lambda x: chars.count(x), reverse=True):
        result += score * chars.count(char)
        score -= 1

    return result


if __name__ == '__main__':
    with open(sys.argv[1]) as tests_handle:
        for line in tests_handle.readlines():
            print(beauty_of(line.strip()))
