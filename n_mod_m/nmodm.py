import sys

"""
Given two integers N and M, calculate N Mod M (without using any inbuilt
modulus operator).
"""


def mod(n, m):
    return n - m * (n / m)


if __name__ == '__main__':
    with open(sys.argv[1]) as tests_handle:
        for line in tests_handle.readlines():
            n, m = line.split(',')
            print(mod(int(n), int(m)))
