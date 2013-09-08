import unittest

from simplesort import quicksort


class QuicksortTestCase(unittest.TestCase):
    def test_quicksort(self):
        self.assertEqual([], quicksort([]))
        self.assertEqual([1], quicksort([1]))
        self.assertEqual([-38.797, 7.581, 14.354, 70.920, 90.374, 99.323], quicksort([70.920, -38.797, 14.354, 99.323, 90.374, 7.581]))


if __name__ == '__main__':
    unittest.main()
