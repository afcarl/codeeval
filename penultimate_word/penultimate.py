import sys


def penultimate_word(sentence):
    words = sentence.split(' ')
    if len(words) <= 1:
        return sentence

    return sentence.split(' ')[-2]


if __name__ == '__main__':
    with open(sys.argv[1]) as tests_handle:
        for line in tests_handle.readlines():
            print penultimate_word(line.strip())
