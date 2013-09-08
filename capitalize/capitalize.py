import sys


def title(sentence):
    words = sentence.split(' ')
    for i, word in enumerate(words):
        words[i] = "{}{}".format(word[0].upper(), word[1:])

    return " ".join(words)


if __name__ == '__main__':
    with open(sys.argv[1]) as tests_handle:
        for line in tests_handle.readlines():
            print title(line.strip())
