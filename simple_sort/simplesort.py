import sys


def quicksort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    lesser = filter(lambda x: x < pivot, array[1:])
    greater = filter(lambda x: x >= pivot, array[1:])

    return quicksort(lesser) + [pivot] + quicksort(greater)


if __name__ == '__main__':
    with open(sys.argv[1]) as tests_handle:
        for line in tests_handle.readlines():
            array = [float(num) for num in line.strip().split(' ')]
            print(" ".join([str(num) for num in quicksort(array)]))
