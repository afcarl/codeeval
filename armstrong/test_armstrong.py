import unittest

from armstrong import is_armstrong


class ArmstrongTestCase(unittest.TestCase):
    def test_armstrong(self):
        self.assertTrue(is_armstrong(6))
        self.assertTrue(is_armstrong(153))
        self.assertFalse(is_armstrong(351))

if __name__ == '__main__':
    unittest.main()
