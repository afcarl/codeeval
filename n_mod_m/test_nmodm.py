import unittest

from nmodm import mod


class ModTestCase(unittest.TestCase):
    def test_mod(self):
        self.assertEqual(10 % 1, mod(10, 1))
        self.assertEqual(8 % 3, mod(8, 3))
        self.assertEqual(9 % 3, mod(9, 3))
        self.assertEqual(19 % -3, mod(19, -3))
        self.assertEqual(0 % -3, mod(0, -3))


if __name__ == '__main__':
    unittest.main()
